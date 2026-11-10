# Sensor connector (CN1)

CN1 is the only link between the nRF54L15 feather and its sensor board. Each node has one feather and one sensor board, joined point to point by a short FFC. The SENS_ID resistor tells firmware which board is fitted.

Pins and connections below come from `kicad-cli` netlists of each board's schematic (2026-11-02). Rail limits, peripheral rules and analog channels come from `v4-sensor-connector.md` and `feather_sensor_template\README.md`. ID values and ratios are in `SENSORS.md`.

## Connector

- **Part:** Molex 503480-1400 on both boards: FFC/FPC, 0.5 mm pitch, 14 circuits, BackFlip actuator, dual contact.
- **Cable:** 0.5 mm pitch, 14-way, 0.3 mm thick FFC. For the U-folded cable the contacts end up on opposite faces, so use an opposite-side FFC. A same-side cable also works because the connector is dual contact.
- **Mating life:** 10 cycles maximum, so treat it as semi-permanent, not a hot-swap port.
- **Reversed cable:** pin n lands on pin 15-n. Pins 1 and 14 are both GND, but VBAT (13) lands on VSENS (2).
- **Logic level:** all signals are 3.0 V, from VSENS. A sensor that needs another voltage generates it on the sensor board.

## Pinout (feather side)

| Pin | Net | Type | nRF54L15 | Feather parts on the pin |
| --- | --- | --- | --- | --- |
| 1 | GND | ground | - | |
| 2 | VSENS | switched 3.0 V out | - | nPM1300 LDSW1 (U2.29), C45 100 nF |
| 3 | SENS_SDA | I2C data | P1.10 (U6.38) | R15 4.7k to VSENS |
| 4 | SENS_SCL | I2C clock | P1.11 (U6.39) | R16 4.7k to VSENS |
| 5 | SENS_SCK | SPI clock | P2.01 (U6.12) | |
| 6 | SENS_MOSI | SPI data out, UART TX | P2.02 (U6.13) | |
| 7 | SENS_MISO | SPI data in, UART RX | P2.04 (U6.15) and P2.00 (U6.11) | |
| 8 | SENS_CS | SPI chip select | P2.05 (U6.16) | R18 10k to VSENS |
| 9 | SENS_INT | interrupt, GPIO | P1.07 (U6.8) | R17 10k to VSENS |
| 10 | SENS_AIN | analog in, 0 to 3.0 V | P1.05 = AIN1 (U6.6) | |
| 11 | SENS_ID | board ID | P1.06 = AIN2 (U6.7) | R19 10k to VSENS |
| 12 | GND | ground | - | |
| 13 | VBAT_CN1 | battery, always on | - | F1 200 mA polyfuse (MF-FSMF020X-2) |
| 14 | GND | ground | - | |
| MP | GND | mounting tabs | - | |

The net is called VBAT on the sensor boards and VBAT_CN1 on the feather. R15 to R18 are fitted on the standard build only (see Feather builds).

## Feather builds (Brian 2026-11-02)

There are two builds of the feather. The bare board, Gerbers and the rest of the BOM are the same; only these four resistors differ.

| Build | R15, R16 (4.7k I2C) | R17, R18 (10k INT, CS) | Sensor boards |
| --- | --- | --- | --- |
| Standard | Fitted | Fitted | pH, ORP, DO, EC |
| Radar | Not fitted | Not fitted | Water level |

R19 (SENS_ID) is fitted on both. Mark radar feathers by hand, because SENS_ID identifies the sensor board, not the feather build.

**Why:** the radar uses SENS_CS as an active-high reset, so R18 would hold it in reset and can back-power VSENS. R17 would draw about 300 uA while the interrupt line is low. The TCA9406 has its own 10k I2C pull-ups, so R15 and R16 would push the nRF sink current past the 1 mA TI tests at.

**If they get mixed up:**
- Radar board on a standard feather: the radar stays in reset until firmware drives SENS_CS low. It then runs with the extra current and marginal I2C. Firmware must not drive SENS_CS high with VSENS off.
- Atlas board on a radar feather: I2C doesn't work because the host-side pull-ups are missing. Fit R15 and R16 to fix it.

Neither case should damage anything according to the review, but that hasn't been tested.

Any new sensor board should use the standard build if it can. Add a build only if the board can't work with these pull-ups.

## What each resource can do

- **VSENS (pin 2):** 100 mA maximum, shared with the feather's BUCK2. Firmware turns it on only around sensor use and SENS_ID reads. Before turning it off, set every CN1 signal to input or low so nothing back-powers the sensor.
- **VBAT (pin 13):** always on and fused at 200 mA. Use it only for loads VSENS can't carry, behind a local regulator with an enable and sub-uA shutdown.
- **I2C (pins 3, 4):** a separate bus from the PMIC's I2C (P1.03, P1.04). The pull-ups are on the feather, so don't add more on the host side of a sensor board.
- **SPI (pins 5 to 8):** SPIM00, which can only use these P2 pins. CS idles high through R18.
- **UART (pins 6, 7):** UARTE00, TX on P2.02, RX on P2.00. No flow control. Pin 7 has two nRF pins because SPI MISO must be P2.04 and UART RX must be P2.00; firmware enables one and leaves the other disconnected.
- **Combinations:** SPI and UART share one hardware instance, so a board can't use both. I2C can run alongside either one.
- **INT (pin 9):** intended as open-drain, active low, and can wake the SoC. Also usable as GPIO.
- **AIN (pin 10):** must be buffered and stay within 0 to 3.0 V. It can't cross an isolation barrier without extra parts.
- **ID (pin 11):** one 1% resistor to GND. Read it only while VSENS is on.
- **Unused pins:** leave them unconnected on the sensor board.

## Resources used by each sensor

GND (pins 1, 12, 14, MP) is connected on every board. A dot means the pin has no connection on that board.

| Pin | Resource | pH | ORP | DO | EC | Water level | Template |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | VSENS | power | power | power | power | logic + LDO enable | power |
| 3 | SENS_SDA | I2C | I2C | I2C | I2C | I2C | I2C |
| 4 | SENS_SCL | I2C | I2C | I2C | I2C | I2C | I2C |
| 5 | SENS_SCK | . | . | . | . | . | . |
| 6 | SENS_MOSI | . | . | . | . | RADAR_WAKE | . |
| 7 | SENS_MISO | . | . | . | . | . | . |
| 8 | SENS_CS | . | . | . | . | RADAR_RST | . |
| 9 | SENS_INT | . | . | . | . | radar interrupt | . |
| 10 | SENS_AIN | . | . | . | . | . | . |
| 11 | SENS_ID | R1 | R1 | R1 | R1 | R1 | R1 |
| 13 | VBAT | . | . | . | . | LDO input | . |

No board uses SPI, UART or AIN today. The water level board is the only one using VBAT or more than I2C, SENS_ID and VSENS.

### pH (Atlas pH OEM): `nrf54l15_feather_sens1`
- **Pins:** VSENS, SENS_SDA, SENS_SCL, SENS_ID, GND.
- **VSENS feeds:** U3 ADuM1250 host side, U4 NXE1S0303MC isolated DC-DC, C1, C2, C6.
- **I2C:** through the U3 isolator. Address not recorded in the board's STATUS.md.
- **SENS_ID:** R1 10k.
- **Interrupt:** not wired to CN1, so firmware polls.

### ORP (Atlas ORP OEM): `Sensor_Boards\feather_orp`
- **Pins:** VSENS, SENS_SDA, SENS_SCL, SENS_ID, GND.
- **VSENS feeds:** U3 ISO1540DR host side, FB1 to the SN6505B isolated supply, C1, C2, C12.
- **I2C:** through the U3 isolator, address 0x66.
- **SENS_ID:** R1 4.7k.
- **Interrupt:** Atlas INT stops at test pad J5 on the isolated side, so firmware polls register 0x07.

### DO (Atlas DO OEM): `Sensor_Boards\feather_dissolved_oxygen`
- **Pins:** VSENS, SENS_SDA, SENS_SCL, SENS_ID, GND.
- **VSENS feeds:** U3 ADuM1250 host side, U4 NXE1S0303MC isolated DC-DC, C1, C2.
- **I2C:** through the U3 isolator, address 0x67.
- **SENS_ID:** the register says 2.2k, but **the schematic still has the 10k placeholder** (see Open issues).
- **Interrupt:** Atlas INT stops at test pad J5 on the isolated side, so firmware polls register 0x07.

### EC (Atlas EC OEM): `Sensor_Boards\feather_conductivity`
- **Pins:** VSENS, SENS_SDA, SENS_SCL, SENS_ID, GND.
- **VSENS feeds:** U3 ADuM1250 host side, U4 NXE1S0303MC isolated DC-DC, C1, C2.
- **I2C:** through the U3 isolator, address 0x64.
- **SENS_ID:** the register says 1k, but **the schematic still has the 10k placeholder** (see Open issues).
- **Interrupt:** Atlas INT stops at test pad J5 on the isolated side, so firmware polls register 0x07.

### Water level (Acconeer XM125 radar): `Sensor_Boards\feather_water_level`
- **Feather build:** radar (R15 to R18 not fitted).
- **Pins:** VSENS, VBAT, SENS_SDA, SENS_SCL, SENS_MOSI as RADAR_WAKE, SENS_CS as RADAR_RST, SENS_INT, SENS_ID, GND. Not isolated.
- **VSENS feeds:** host side of the translators (U3 TCA9406, U4 and U5 SN74AXC1T45), U2 NCP161 enable, C1, C2, C8, C9. U4 DIR is tied to VSENS.
- **VBAT feeds:** U2 NCP161 1.8 V LDO input and C3. The LDO powers the radar, so turning VSENS off turns the radar off.
- **I2C:** through U3 TCA9406 to 1.8 V, address 0x52. U3's channels are swapped for layout: SENS_SDA is on SCL_B and SENS_SCL is on SDA_B.
- **Pin 6 RADAR_WAKE:** through U4 to XM125 WAKE_UP, high = wake. R3 100k pull-down.
- **Pin 8 RADAR_RST:** drives Q1 BSS138 onto XM125 NRESET, high = held in reset. R2 100k pull-down.
- **Pin 9 SENS_INT:** from XM125 MCU_INT through U5, high = ready.
- **SENS_ID:** R1 22k.

### Template (no sensor): `Sensor_Boards\feather_sensor_template`
- **Pins:** VSENS, SENS_SDA, SENS_SCL, SENS_ID, GND.
- **VSENS feeds:** U3 ADuM1250 host side, U4 NXE1S0303MC isolated DC-DC, C1, C2.
- **SENS_ID:** R1 10k placeholder, which reads as pH until it's changed.

## Open issues (found 2026-11-02)

1. **DO and EC have the wrong ID resistor.** Both schematics have R1 = 10k, which firmware would read as pH. `SENSORS.md` assigns 2.2k (DO) and 1k (EC). Neither board has fab output yet; fix R1 before generating it.
2. **Water level notes need the radar build.** The radar reset, interrupt and I2C pull-up problems are settled by the radar feather build above (review: shared\reports\2026-11-02-review-feather-water-level.md, B1 and S2). The firmware reset default still needs checking on the bench.
3. **pH I2C address isn't recorded.** Confirm it from the Atlas datasheet and add it here.
4. **Feather firmware has no CN1 sensor pins yet, other than SENS_ID.** The board file (`soil_moisture_fw\boards\others\nrf54l15_feather`) still needs the sensor I2C bus and the water level pins.
