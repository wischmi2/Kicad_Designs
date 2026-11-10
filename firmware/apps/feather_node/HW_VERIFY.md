# Hardware connectivity verification

Re-exported netlist with KiCad 10.0 CLI on 2026-07-16 from `nrf54l15_soil_moisture.kicad_sch`.

## Confirmed nets

| Net | Members |
| --- | --- |
| `VDDIO` (includes former VOUT2) | U2.12 VDDIO, U2.32 VOUT2, U6 VDD pins (10/22/36/47/48), R12/R13 pull-up tops, CN1.2, J2.1, decoupling |
| `I2C_SCL` | U6.4 P1.03, U2.14 SCL, R12, CN1.4 |
| `I2C_SDA` | U6.5 P1.04, U2.13 SDA, R13, CN1.3 |
| `PMIC_INT` | U2.8 GPIO1, U6.23 P0.00 |
| `ANT_SEL` | U6.24 P0.01, R11.6 VCTL (FM8625H) |
| `VOUT1` | U2.1, RF switch VDD (R11.4), BUCK1 rail |

MCU: U6 nRF54L15-QFXX. PMIC: U2 nPM1300-QEXX.
