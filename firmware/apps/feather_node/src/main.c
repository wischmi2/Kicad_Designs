/*
 * Copyright (c) 2025 Golioth
 *
 * SPDX-License-Identifier: Apache-2.0
 *
 * nRF54L15 feather as a Golioth Pouch BLE node. Based on the Pouch ble_gatt
 * example and the nrf54l15_solar_pouch app.
 */

#include <zephyr/logging/log.h>
LOG_MODULE_REGISTER(main);

#include "credentials.h"
#include "ble_peripheral.h"
#include "feather_status.h"

#ifdef CONFIG_BOARD_NRF54L15_FEATHER
#include "feather_run5.h"
#endif

#include <zephyr/kernel.h>
#include <zephyr/drivers/gpio.h>
#include <zephyr/drivers/mfd/npm13xx.h>

#include <pouch/pouch.h>
#include <pouch/events.h>
#include <pouch/uplink.h>
#include <pouch/downlink.h>
#include <pouch/transport/bluetooth/gatt.h>

#include <golioth/settings_callbacks.h>

#include <app_version.h>

static const struct device *pmic = DEVICE_DT_GET_OR_NULL(DT_NODELABEL(npm1300_ek_pmic));
static const struct gpio_dt_spec button = GPIO_DT_SPEC_GET_OR(DT_ALIAS(sw0), gpios, {});

/* nPM1300 LEDDRV. CLR turns the pin off only while the mode is host. */
#define NPM_LED_BASE      0x0AU
#define NPM_LED_MODE_HOST 2U
#define NPM_LED_CLR       1U
static struct gpio_callback button_cb_data;

/**
 * Push timeseries application data to the cloud on every uplink
 */
static void do_uplink(void)
{
	char json[256];
	int len = feather_status_format(json, sizeof(json));

	if (len < 0) {
		LOG_ERR("Status format failed (%d)", len);
		return;
	}

	LOG_INF("Uplink %s", json);

	int err = pouch_uplink_entry_write(".s/sensor", POUCH_CONTENT_TYPE_JSON, json, (size_t)len,
					   POUCH_FOREVER);
	if (err) {
		LOG_ERR("Uplink write failed (%d)", err);
	}
}

POUCH_UPLINK_HANDLER(do_uplink);

/**
 * Settings handler for the "LED" setting. The feather keeps its LED off,
 * lighting it costs 5 mA.
 */
static int led_setting_cb(bool new_value)
{
	ARG_UNUSED(new_value);
	return 0;
}

GOLIOTH_SETTINGS_HANDLER(LED, led_setting_cb);

static void pouch_event(enum pouch_event event, void *ctx)
{
	ARG_UNUSED(ctx);

	if (event == POUCH_EVENT_SESSION_START) {
		LOG_INF("Pouch session started");
	} else if (event == POUCH_EVENT_SESSION_END) {
		LOG_INF("Pouch session ended");
	}
}

POUCH_EVENT_HANDLER(pouch_event, NULL);

/**
 * Setup pouch stack: load credentials and initialize pouch.
 */
static int setup_pouch(void)
{
	struct pouch_config config = {0};

	int err = load_certificate(&config.certificate);
	if (err) {
		LOG_ERR("Failed to load certificate (err %d)", err);
		return err;
	}

	config.private_key = load_private_key();
	if (config.private_key == PSA_KEY_ID_NULL) {
		LOG_ERR("Failed to load private key");
		return -ENOENT;
	}

	LOG_INF("Credentials loaded");

	err = pouch_init(&config);
	if (err) {
		LOG_ERR("Pouch init failed (err %d)", err);
		return err;
	}

	LOG_INF("Pouch initialized");
	return 0;
}

/**
 * Turn the nPM1300 LEDs off. The PMIC stays powered when the nRF resets, so a
 * host "on" bit survives. CLR is ignored unless the mode is host.
 */
static void setup_led(void)
{
	if (!device_is_ready(pmic)) {
		LOG_WRN("nPM1300 is not ready");
		return;
	}

	for (uint8_t led = 0; led < 3; led++) {
		int err = mfd_npm13xx_reg_write(pmic, NPM_LED_BASE, led, NPM_LED_MODE_HOST);

		if (err == 0) {
			err = mfd_npm13xx_reg_write(pmic, NPM_LED_BASE, 0x04U + (led * 2U),
						    NPM_LED_CLR);
		}

		if (err < 0) {
			LOG_WRN("Could not turn off nPM1300 LED %u (err %d)", led, err);
		}
	}
}

/**
 * Button handler for the Bluetooth OOB authentication mechanism.
 */
static void button_pressed(const struct device *dev, struct gpio_callback *cb, uint32_t pins)
{
	ble_peripheral_button_handler();
}

/**
 * Initialize the button (alias sw0). The feather has SW1 on the board but it
 * is not in the devicetree yet, so this is skipped.
 */
static void setup_button(void)
{
	if (!DT_HAS_ALIAS(sw0) || !DT_NODE_HAS_STATUS(DT_ALIAS(sw0), okay)) {
		return;
	}

	LOG_INF("Set up button at %s pin %d", button.port->name, button.pin);

	int err = gpio_pin_configure_dt(&button, GPIO_INPUT);
	if (err < 0) {
		LOG_WRN("Could not initialize Button");
		return;
	}

	err = gpio_pin_interrupt_configure_dt(&button, GPIO_INT_EDGE_TO_ACTIVE);
	if (err) {
		LOG_WRN("Error %d: failed to configure interrupt on %s pin %d", err,
			button.port->name, button.pin);
		return;
	}

	gpio_init_callback(&button_cb_data, button_pressed, BIT(button.pin));
	gpio_add_callback(button.port, &button_cb_data);
}

int main(void)
{
#ifdef CONFIG_BOARD_NRF54L15_FEATHER
	/* VRF (LDSW2) comes up in the regulator driver init, after the ANT_SEL gpio-hog. */
	(void)feather_vrf_check();
#endif

	feather_status_start();
	setup_led();

	LOG_INF("Pouch SDK Version: " STRINGIFY(APP_BUILD_VERSION));
	LOG_INF("Pouch Protocol Version: %d", POUCH_VERSION);
	LOG_INF("Pouch BLE Transport Protocol Version: %d", POUCH_GATT_VERSION);

	int err = ble_peripheral_init();
	if (err) {
		return err;
	}

	err = setup_pouch();
	if (err) {
		LOG_ERR("Pouch is not running (err %d). Still advertising so the gateway attempt is visible.",
			err);
	}

	setup_button();

	err = ble_peripheral_start();
	if (err) {
		LOG_ERR("Advertising failed (err %d)", err);
	}

	/* Stay awake and keep printing. Returning here would idle with no further logs. */
	while (1) {
		k_sleep(K_SECONDS(10));
		if (err) {
			LOG_ERR("Up, advertising is not running");
		} else if (ble_peripheral_sync_requested()) {
			LOG_INF("Up, requesting a gateway");
		} else {
			LOG_INF("Up, gateway request is off");
		}
	}
}
