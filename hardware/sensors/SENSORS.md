# Sensor board ID register (SENS_ID)

CN1 pinout, the pins each sensor uses and the two feather builds: CN1_SENSOR_CONNECTOR.md (this folder). Water level needs the radar feather build (R15 to R18 not fitted); all other boards use the standard build.

Each sensor board carries R1 = R_ID from SENS_ID to GND on the CN1 side. The feather (R19) pulls SENS_ID up with **100k to VSENS** (was 10k until 2026-11-11, scaled x10 to cut the divider current; ratios unchanged) (nrf54l15_feather, sensor_connector sheet), so firmware reads a divider:

    V(SENS_ID) = VSENS * R_ID / (R_ID + 100k)        ratio = R_ID / (R_ID + 100k)

Read SENS_ID only while VSENS is on. The reading is ratiometric to VSENS, so the ratio is the number to compare against (use SAADC with VDD or VSENS as reference, or measure VSENS in the same burst). Example column uses VSENS = 3.0 V (feather BUCK2 default today, per feather_sensor_template\isolated_supply_options.md) and a 12-bit conversion on a 3.0 V full scale (4095 counts); recompute if VSENS or the reference differs. The 1% resistor tolerance moves the ratio by under +/-0.5% of full scale, so adjacent IDs are well separated (smallest gap is 0.09 between the EC and DO IDs).

**Firmware note (2026-11-11):** the ADC source impedance is now R19 || R_ID = about 9 kohm (EC) to 69 kohm (water level), 50 kohm for pH. Use a long SAADC acquisition time (the 40 us setting) or buffer the pin, and let the 100 nF-class pin capacitance settle before sampling; a short acquisition would read low on the high-ratio IDs.

| Sensor type | Board folder | R_ID (1%, 0402) | MPN (Yageo; DigiKey stock checked 2026-11-11) | Old R_ID (to 2026-11-11) | Ratio (unchanged) | V(SENS_ID) at 3.0 V | ADC counts (VSENS FS, 12 bit) | Divider current at 3.0 V (was) | R19 \|\| R_ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EC / conductivity (Atlas EC OEM) | hardware\sensors\conductivity | 10k | RC0402FR-0710KL (311-10.0KLRCT-ND, 6.5 M) | 1k (board had a 10k placeholder) | 0.0909 | 0.273 V | 372 | 27 uA (273 uA) | 9.1k |
| DO / dissolved oxygen (Atlas DO OEM) | hardware\sensors\dissolved_oxygen | 22k | RC0402FR-0722KL (311-22.0KLRCT-ND, DigiKey stock 0 on 2026-11-11; Mouser 603-RC0402FR-0722KL; DigiKey alt RC0402FR-1322KL) | 2.2k (board had a 10k placeholder) | 0.1803 | 0.541 V | 738 | 25 uA (246 uA) | 18.0k |
| ORP (Atlas ORP OEM) | hardware\sensors\orp | 47k | RC0402FR-0747KL (311-47.0KLRCT-ND, 440 k) | 4.7k | 0.3197 | 0.959 V | 1309 | 20 uA (204 uA) | 32.0k |
| pH (sens1) | hardware\sensors\ph
rf54l15_feather_sens1 | 100k | RC0402FR-07100KL (311-100KLRCT-ND, 4.5 M) | 10k | 0.5000 | 1.500 V | 2048 | 15 uA (150 uA) | 50.0k |
| Water level (Acconeer XM125 60 GHz radar; also the TC2030 variant) | hardware\sensors\water_level, water_level_tc2030 | 220k | RC0402FR-07220KL (311-220KLRCT-ND, 1.0 M) | 22k | 0.6875 | 2.063 V | 2816 | 9 uA (94 uA) | 68.8k |
| Template / unassigned | hardware\sensors	emplate | 100k placeholder | RC0402FR-07100KL | 10k placeholder | 0.5000 | 1.500 V | 2048 | 15 uA | 50.0k |

Ratio check 2026-11-11 (old pair -> new pair, all with the pull-up scaled x10): EC 1k/(1k+10k) = 10k/(10k+100k) = 0.0909; DO 2.2k/12.2k = 22k/122k = 0.1803; ORP 4.7k/14.7k = 47k/147k = 0.3197; pH 10k/20k = 100k/200k = 0.5000; water level 22k/32k = 220k/320k = 0.6875. Every ratio is identical, so firmware thresholds do not change. Divider current is VSENS / (R19 + R_ID), now one tenth of the old value. VSENS stays on, so this is a standing load of 9 to 27 uA per node.

Notes
- IDs decided by Brian 2026-10-28. Open (SENS_ID no resistor fitted) reads ratio 1.0 (VSENS) and a shorted ID reads 0, so both are invalid IDs for firmware.
- Water level uses 220k (ratio 0.6875), set 2026-10-30 when the board moved to the XM125 radar (22k then, x10 on 2026-11-11). Next free value with a wide gap: 470k (0.8246).
- The pH board and the template both use 100k, so the template placeholder reads as pH until R1 is changed.
- 2026-11-11 (Brian): all R_ID values and feather R19 scaled x10. Copper is unchanged; only the fitted resistor values change. Boards already ordered (feather 10-29, ORP, sens1, water level TC2030) take the new values from the BOM; nothing printed on silkscreen carries the value (it is on F.Fab only).
- Mouser equivalents exist for the same Yageo RC0402FR-07 series (Mouser stock not checked here).
- VSENS is 3.0 V today (coordinator 2026-10-28; the first version of this file assumed 3.3 V). The ratio and counts don't depend on it if the reading is ratiometric; only the voltage column does.
