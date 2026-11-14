#ifndef FEATHER_STATUS_H_
#define FEATHER_STATUS_H_

#include <stddef.h>

/* Start the nPM1300 / fuel gauge sampling thread and read SENS_ID once.
 * Sampling runs on its own work queue so the gateway request window in
 * ble_peripheral.c keeps running between syncs.
 */
void feather_status_start(void);

/* Write the latest snapshot as one JSON object (vbat_mv, soc_pct, ibat_ma,
 * charge, vbus, sens_id_mv, sens_rid_ohm). Returns the length written,
 * excluding the terminating NUL, or a negative errno.
 */
int feather_status_format(char *buf, size_t len);

#endif /* FEATHER_STATUS_H_ */
