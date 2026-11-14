#include "feather_status.h"

#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <zephyr/drivers/sensor.h>
#include <zephyr/drivers/sensor/npm13xx_charger.h>
#include <zephyr/logging/log.h>
#include <zephyr/sys/printk.h>

#include "fuel_gauge.h"

#ifdef CONFIG_BOARD_NRF54L15_FEATHER
#include "feather_run5.h"
#endif

LOG_MODULE_REGISTER(feather_status, LOG_LEVEL_INF);

#define CHARGER_NODE DT_NODELABEL(npm1300_ek_charger)

#define CHG_STATUS_COMPLETE BIT(1)
#define CHG_STATUS_TRICKLE  BIT(2)
#define CHG_STATUS_CC       BIT(3)
#define CHG_STATUS_CV       BIT(4)
#define VBUS_PRESENT        BIT(0)

/* A LiPo voltage on VBAT means a cell is fitted even while the charger is idle. */
#define VBAT_PRESENT_MIN_MV 2500
#define VBAT_PRESENT_MAX_MV 4500

#define SENS_ID_REFRESH_SAMPLES 12 /* about once a minute at the default period */

#define STATUS_STACK_SIZE 2048
#define STATUS_PRIORITY   10

struct feather_snapshot {
	uint16_t vbat_mv;
	int16_t soc_pct; /* -1 when the fuel gauge did not start */
	int16_t ibat_ma; /* Zephyr sign: negative = discharging */
	const char *charge;
	bool vbus;
	int32_t sens_id_mv; /* -1 when not read */
	int32_t sens_rid_ohm; /* 0 = open (no sensor board) or invalid, -1 when not read */
};

static const struct device *charger = DEVICE_DT_GET(CHARGER_NODE);
static struct k_mutex snap_lock;
static struct feather_snapshot snap = {
	.soc_pct = -1,
	.charge = "NO-BATT",
	.sens_id_mv = -1,
	.sens_rid_ohm = -1,
};
static bool gauge_ok;
static uint32_t sample_count;

K_KERNEL_STACK_DEFINE(status_stack, STATUS_STACK_SIZE);
static struct k_work_q status_wq;
static struct k_work_delayable sample_work;

static const char *charge_str(int32_t status, uint16_t vbat_mv)
{
	if (status & CHG_STATUS_COMPLETE) {
		return "COMPLETE";
	}
	if (status & CHG_STATUS_CV) {
		return "CV";
	}
	if (status & CHG_STATUS_CC) {
		return "CC";
	}
	if (status & CHG_STATUS_TRICKLE) {
		return "TRICKLE";
	}
	if ((vbat_mv >= VBAT_PRESENT_MIN_MV) && (vbat_mv <= VBAT_PRESENT_MAX_MV)) {
		return "IDLE";
	}
	return "NO-BATT";
}

static void read_sens_id(struct feather_snapshot *next)
{
#ifdef CONFIG_BOARD_NRF54L15_FEATHER
	int32_t id_mv;
	uint32_t rid;

	/* Switches VSENS on for about 50 ms, so only do it now and then. */
	if (feather_read_sens_id(&id_mv, &rid) == 0) {
		next->sens_id_mv = id_mv;
		next->sens_rid_ohm = (int32_t)rid;
		LOG_INF("SENS_ID %d mV, Rid about %u ohm (0 = open or invalid)", id_mv, rid);
	}
#else
	ARG_UNUSED(next);
#endif
}

static void sample_handler(struct k_work *work)
{
	struct sensor_value vbus = {0};
	struct fuel_gauge_sample fg = {0};
	struct feather_snapshot next;
	int32_t mv;
	int32_t ma;
	bool vbus_on;

	ARG_UNUSED(work);

	k_work_schedule_for_queue(&status_wq, &sample_work,
				  K_SECONDS(CONFIG_FEATHER_STATUS_PERIOD_S));

	k_mutex_lock(&snap_lock, K_FOREVER);
	next = snap;
	k_mutex_unlock(&snap_lock);

	if (!device_is_ready(charger)) {
		LOG_ERR("nPM1300 charger not ready");
		return;
	}

	if (sensor_sample_fetch(charger) < 0) {
		LOG_ERR("nPM1300 sample fetch failed");
		return;
	}
	sensor_channel_get(charger, SENSOR_CHAN_NPM13XX_CHARGER_VBUS_STATUS, &vbus);
	vbus_on = (vbus.val1 & VBUS_PRESENT) != 0;

	if (!gauge_ok && (fuel_gauge_init(charger) == 0)) {
		gauge_ok = true;
	}
	fg.soc = -1.f;
	if ((gauge_ok ? fuel_gauge_update(charger, vbus_on, &fg) :
			fuel_gauge_read(charger, &fg)) < 0) {
		LOG_ERR("Fuel gauge update failed");
		return;
	}

	mv = (int32_t)(fg.voltage * 1000.f + 0.5f);
	ma = (int32_t)(fg.current * 1000.f);

	next.vbat_mv = (uint16_t)CLAMP(mv, 0, UINT16_MAX);
	next.ibat_ma = (int16_t)CLAMP(ma, INT16_MIN, INT16_MAX);
	next.vbus = vbus_on;
	next.charge = charge_str(fg.chg_status, next.vbat_mv);
	next.soc_pct = (fg.soc < 0.f) ? -1 : (int16_t)CLAMP((int32_t)(fg.soc + 0.5f), 0, 100);

	if ((sample_count++ % SENS_ID_REFRESH_SAMPLES) == 0) {
		read_sens_id(&next);
	}

	k_mutex_lock(&snap_lock, K_FOREVER);
	snap = next;
	k_mutex_unlock(&snap_lock);

	LOG_INF("VBAT %u mV (%d%%) I %+d mA %s VBUS %s", next.vbat_mv, next.soc_pct,
		next.ibat_ma, next.charge, next.vbus ? "yes" : "no");
}

void feather_status_start(void)
{
	k_mutex_init(&snap_lock);

	if (!device_is_ready(charger)) {
		LOG_ERR("nPM1300 charger not ready, no battery data");
	} else if (fuel_gauge_init(charger) < 0) {
		LOG_ERR("Could not initialise fuel gauge");
	} else {
		gauge_ok = true;
	}

	k_work_queue_start(&status_wq, status_stack, K_KERNEL_STACK_SIZEOF(status_stack),
			   STATUS_PRIORITY, NULL);
	k_work_init_delayable(&sample_work, sample_handler);
	k_work_schedule_for_queue(&status_wq, &sample_work, K_NO_WAIT);
}

int feather_status_format(char *buf, size_t len)
{
	struct feather_snapshot copy;
	int wrote;

	if ((buf == NULL) || (len == 0U)) {
		return -EINVAL;
	}

	k_mutex_lock(&snap_lock, K_FOREVER);
	copy = snap;
	k_mutex_unlock(&snap_lock);

	wrote = snprintk(buf, len,
			 "{\"vbat_mv\":%u,\"soc_pct\":%d,\"ibat_ma\":%d,"
			 "\"charge\":\"%s\",\"vbus\":%s,"
			 "\"sens_id_mv\":%d,\"sens_rid_ohm\":%d}",
			 copy.vbat_mv, copy.soc_pct, copy.ibat_ma, copy.charge,
			 copy.vbus ? "true" : "false", (int)copy.sens_id_mv,
			 (int)copy.sens_rid_ohm);
	if ((wrote < 0) || ((size_t)wrote >= len)) {
		return -ENOMEM;
	}
	return wrote;
}
