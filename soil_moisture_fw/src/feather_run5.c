#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <zephyr/drivers/adc.h>
#include <zephyr/drivers/gpio.h>
#include <zephyr/drivers/regulator.h>
#include <zephyr/logging/log.h>

#include "feather_run5.h"

LOG_MODULE_REGISTER(feather, LOG_LEVEL_INF);

/* nPM1300 LDO1 node = LDSW1 = VSENS, LDO2 node = LDSW2 = VRF (see the board dts). */
static const struct device *const vsens = DEVICE_DT_GET(DT_NODELABEL(npm1300_ek_ldo1));
static const struct device *const vrf = DEVICE_DT_GET(DT_NODELABEL(npm1300_ek_ldo2));
static const struct gpio_dt_spec ant_sel = GPIO_DT_SPEC_GET(DT_ALIAS(ant_sel), gpios);
static const struct adc_dt_spec sens_id = ADC_DT_SPEC_GET_BY_IDX(DT_PATH(zephyr_user), 0);

/* R19 pull-up on SENS_ID to VSENS, nominal VSENS (VDDIO via LSIN1, load switch mode). */
#define SENS_ID_PULLUP_OHM 10000
#define VSENS_NOMINAL_MV   3000
/* Settling time after VSENS on before sampling (load switch ramp + C45 + sensor board). */
#define VSENS_SETTLE_MS    20
/* Above this fraction of VSENS the pin is treated as open (no sensor board). */
#define SENS_ID_OPEN_MV    2900

int feather_vrf_check(void)
{
	int32_t uv = 0;
	int err;

	if (!device_is_ready(vrf)) {
		LOG_ERR("VRF regulator not ready");
		return -ENODEV;
	}

	if (!regulator_is_enabled(vrf)) {
		LOG_ERR("VRF (LDSW2) is not enabled");
		return -EIO;
	}

	err = regulator_get_voltage(vrf, &uv);
	if (err) {
		LOG_ERR("VRF get voltage failed (%d)", err);
		return err;
	}

	LOG_INF("VRF on, %d mV", uv / 1000);

	if (uv != 2500000) {
		LOG_WRN("VRF is not 2.5 V");
		return -EINVAL;
	}

	/* ANT_SEL was driven low by the gpio-hog before VRF came up. Report the level. */
	if (gpio_is_ready_dt(&ant_sel)) {
		LOG_INF("ANT_SEL (P0.01) reads %d (0 = chip antenna)",
			gpio_pin_get_raw(ant_sel.port, ant_sel.pin));
	}

	return 0;
}

int feather_read_sens_id(int32_t *pin_mv, uint32_t *rid_ohm)
{
	int16_t raw = 0;
	int32_t mv;
	int err;
	struct adc_sequence seq = {
		.buffer = &raw,
		.buffer_size = sizeof(raw),
	};

	if (!device_is_ready(vsens) || !adc_is_ready_dt(&sens_id)) {
		return -ENODEV;
	}

	err = adc_channel_setup_dt(&sens_id);
	if (err) {
		return err;
	}

	err = adc_sequence_init_dt(&sens_id, &seq);
	if (err) {
		return err;
	}

	err = regulator_enable(vsens);
	if (err) {
		LOG_ERR("VSENS enable failed (%d)", err);
		return err;
	}

	k_msleep(VSENS_SETTLE_MS);

	err = adc_read_dt(&sens_id, &seq);

	/* Always switch VSENS off again; SENS_ID is only valid while VSENS is on. */
	(void)regulator_disable(vsens);

	if (err) {
		LOG_ERR("SENS_ID ADC read failed (%d)", err);
		return err;
	}

	mv = raw;
	err = adc_raw_to_millivolts_dt(&sens_id, &mv);
	if (err) {
		return err;
	}

	*pin_mv = mv;
	if (mv >= SENS_ID_OPEN_MV) {
		*rid_ohm = 0;
	} else if (mv <= 0) {
		*rid_ohm = 0; /* shorted: also not a valid ID */
	} else {
		*rid_ohm = (uint32_t)(((int64_t)SENS_ID_PULLUP_OHM * mv) /
				      (VSENS_NOMINAL_MV - mv));
	}

	return 0;
}
