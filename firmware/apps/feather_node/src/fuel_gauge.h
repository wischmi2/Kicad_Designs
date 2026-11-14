/*
 * Copyright (c) 2023 Nordic Semiconductor ASA
 * SPDX-License-Identifier: LicenseRef-Nordic-5-Clause
 */

#ifndef __FUEL_GAUGE_H__
#define __FUEL_GAUGE_H__

#include <stdbool.h>
#include <stdint.h>

struct device;

struct fuel_gauge_sample {
	float voltage;     /* V */
	float current;     /* A, Zephyr sign: negative = discharging */
	float temp;        /* degC */
	float soc;         /* percent, -1 when no fuel gauge result */
	int32_t chg_status; /* nPM13xx BCHGCHARGESTATUS */
};

int fuel_gauge_init(const struct device *charger);

/* Fetch and run the gauge. out may be NULL. */
int fuel_gauge_update(const struct device *charger, bool vbus_connected,
		      struct fuel_gauge_sample *out);

/* Fetch only (voltage, current, temp, status); out->soc is not touched. */
int fuel_gauge_read(const struct device *charger, struct fuel_gauge_sample *out);

#endif /* __FUEL_GAUGE_H__ */
