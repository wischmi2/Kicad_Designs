# Sensor board ID register (SENS_ID)

CN1 pinout and the pins each sensor uses: CN1_SENSOR_CONNECTOR.md (this folder).

Each sensor board carries R1 = R_ID from SENS_ID to GND on the CN1 side. The feather (R19) pulls SENS_ID up with **10k to VSENS** (nrf54l15_feather, sensor_connector sheet), so firmware reads a divider:

    V(SENS_ID) = VSENS * R_ID / (R_ID + 10k)        ratio = R_ID / (R_ID + 10k)

Read SENS_ID only while VSENS is on. The reading is ratiometric to VSENS, so the ratio is the number to compare against (use SAADC with VDD or VSENS as reference, or measure VSENS in the same burst). Example column uses VSENS = 3.0 V (feather BUCK2 default today, per feather_sensor_template\isolated_supply_options.md) and a 12-bit conversion on a 3.0 V full scale (4095 counts); recompute if VSENS or the reference differs. The 1% resistor tolerance moves the ratio by under +/-0.5% of full scale, so adjacent IDs are well separated (smallest gap is 0.09 between 1k and 2.2k).

| Sensor type | Board folder | R_ID (1%, 0402) | MPN (Yageo, DigiKey stock checked 2026-10-28) | Ratio | V(SENS_ID) at 3.0 V | ADC counts (VSENS FS, 12 bit) |
| --- | --- | --- | --- | --- | --- | --- |
| EC / conductivity (Atlas EC OEM) | Sensor_Boards\feather_conductivity | 1k | RC0402FR-071KL (DigiKey 311-1.00KLRCT-ND, 3.5 M) | 0.0909 | 0.273 V | 372 |
| DO / dissolved oxygen (Atlas DO OEM) | Sensor_Boards\feather_dissolved_oxygen | 2.2k | RC0402FR-072K2L (311-2.20KLRCT-ND, 1.8 k in stock) | 0.1803 | 0.541 V | 738 |
| ORP (Atlas ORP OEM) | Sensor_Boards\feather_orp | 4.7k | RC0402FR-074K7L (311-4.7KLRCT-ND, 842 k) | 0.3197 | 0.959 V | 1309 |
| pH (sens1) | nrf54l15_feather_sens1 | 10k | RC0402FR-0710KL (311-10.0KLRCT-ND, 8.6 M) | 0.5000 | 1.500 V | 2048 |
| Water level (Acconeer XM125 60 GHz radar) | Sensor_Boards\feather_water_level | 22k | RC0402FR-0722KL (DigiKey stock 0 on 2026-10-30; Mouser 603-RC0402FR-0722KL per parts-sourcing; same part at DigiKey: RC0402FR-1322KL, 13-RC0402FR-1322KLCT-ND, 20,963) | 0.6875 | 2.063 V | 2816 |
| Template / unassigned | Sensor_Boards\feather_sensor_template | 10k placeholder | RC0402FR-0710KL | 0.5000 | 1.500 V | 2048 |

Notes
- IDs decided by Brian 2026-10-28. Open (SENS_ID no resistor fitted) reads ratio 1.0 (VSENS) and a shorted ID reads 0, so both are invalid IDs for firmware.
- Water level uses 22k (ratio 0.6875), set 2026-10-30 when the board moved to the XM125 radar. Next free value with a wide gap: 47k (0.8246).
- The pH board and the template both use 10k, so the template placeholder reads as pH until R1 is changed.
- Mouser equivalents exist for the same Yageo RC0402FR-07 series (Mouser stock not checked here).
- VSENS is 3.0 V today (coordinator 2026-10-28; the first version of this file assumed 3.3 V). The ratio and counts don't depend on it if the reading is ratiometric; only the voltage column does.
