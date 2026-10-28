#ifndef FEATHER_RUN5_H_
#define FEATHER_RUN5_H_

/* Feather run 5 power and peripheral helpers (nrf54l15_feather board only). */

/* Check that VRF (nPM1300 LDSW2) is up at 2.5 V and ANT_SEL is low. Returns 0 if so. */
int feather_vrf_check(void);

/* Turn VSENS (nPM1300 LDSW1) on, wait, read SENS_ID (P1.06), turn VSENS off.
 * On success returns 0 and fills *pin_mv (SENS_ID pin voltage) and *rid_ohm
 * (estimated ID resistor to GND, 0 if the pin reads open, i.e. no sensor board).
 */
int feather_read_sens_id(int32_t *pin_mv, uint32_t *rid_ohm);

#endif
