#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <zephyr/drivers/gpio.h>
#include <zephyr/drivers/mfd/npm13xx.h>
#include <zephyr/drivers/sensor.h>
#include <zephyr/logging/log.h>

#include "fuel_gauge.h"

LOG_MODULE_REGISTER(main, LOG_LEVEL_INF);

#define SLEEP_TIME_MS 1000

#define NPM13XX_DEVICE(dev) DEVICE_DT_GET(DT_NODELABEL(npm1300_ek_ ## dev))

static const struct device *pmic = NPM13XX_DEVICE(pmic);
static const struct device *charger = NPM13XX_DEVICE(charger);
static const struct gpio_dt_spec ant_sel = GPIO_DT_SPEC_GET(DT_ALIAS(ant_sel), gpios);

static volatile bool vbus_connected;

static void event_callback(const struct device *dev, struct gpio_callback *cb, uint32_t pins)
{
	ARG_UNUSED(dev);
	ARG_UNUSED(cb);

	if (pins & BIT(NPM13XX_EVENT_VBUS_DETECTED)) {
		LOG_INF("VBUS connected (USB or solar input)");
		vbus_connected = true;
	}

	if (pins & BIT(NPM13XX_EVENT_VBUS_REMOVED)) {
		LOG_INF("VBUS removed");
		vbus_connected = false;
	}
}

static int ant_sel_init(void)
{
	int err;

	if (!gpio_is_ready_dt(&ant_sel)) {
		LOG_ERR("ANT_SEL GPIO not ready");
		return -ENODEV;
	}

	/* Drive low to select onboard chip antenna (RF1 path). Invert if needed. */
	err = gpio_pin_configure_dt(&ant_sel, GPIO_OUTPUT_INACTIVE);
	if (err) {
		LOG_ERR("Failed to configure ANT_SEL (%d)", err);
		return err;
	}

	LOG_INF("ANT_SEL set for onboard antenna (P0.01 inactive)");
	return 0;
}

int main(void)
{
	int err;
	struct sensor_value val;
	static struct gpio_callback event_cb;

	LOG_INF("nRF54L15 soil moisture bring-up");

	err = ant_sel_init();
	if (err) {
		return 0;
	}

	if (!device_is_ready(pmic)) {
		LOG_ERR("PMIC device not ready");
		return 0;
	}

	if (!device_is_ready(charger)) {
		LOG_ERR("Charger device not ready");
		return 0;
	}

	if (fuel_gauge_init(charger) < 0) {
		LOG_ERR("Could not initialise fuel gauge");
		return 0;
	}

	gpio_init_callback(&event_cb, event_callback,
			   BIT(NPM13XX_EVENT_VBUS_DETECTED) | BIT(NPM13XX_EVENT_VBUS_REMOVED));

	err = mfd_npm13xx_add_callback(pmic, &event_cb);
	if (err) {
		LOG_ERR("Failed to add PMIC callback (%d)", err);
		return 0;
	}

	err = sensor_attr_get(charger, SENSOR_CHAN_CURRENT, SENSOR_ATTR_UPPER_THRESH, &val);
	if (err < 0) {
		LOG_WRN("Could not read initial VBUS threshold status (%d)", err);
		vbus_connected = false;
	} else {
		vbus_connected = (val.val1 != 0) || (val.val2 != 0);
	}

	LOG_INF("PMIC ready; host-int on P0.00 / pmic-int-pin GPIO1");
	LOG_INF("Initial VBUS connected=%d", vbus_connected);

	while (1) {
		fuel_gauge_update(charger, vbus_connected);
		k_msleep(SLEEP_TIME_MS);
	}
}
