# v4 Sensor Connector (CN1)

One 14-pin plug, same on every sensor board. The host pinout is fixed; new sensor boards adapt to it.

Source of truth: `nrf54l15_v4\sensor_connector.kicad_sch` and `nrf54l15.kicad_sch`, read 2026-10-04. Pin capabilities checked against the nRF54L15 datasheet v1.0 (Table 79, §10.1.1–10.1.2).

## Connector

- **Part:** Molex **503480-1400** — Easy-On FFC/FPC, 0.5 mm pitch, 14 circuits, BackFlip actuator, dual contact, 1.0 mm high
- **Footprint:** `nrf54l15_v4:Molex_503480-1400_1x14-1MP_P0.50mm_Horizontal` (project library `nrf54l15_v4.pretty`, built from Molex drawing SD-503480-001 rev J1)
- **Cable:** 0.5 mm pitch, 14-way, 0.3 mm thick FFC
- **Mating life:** 10 cycles max — semi-permanent joint, not a hot-swap port

## Pinout

| Pin | Signal | Type | nRF54L15 | Host-side parts |
|---|---|---|---|---|
| 1 | GND | ground | — | |
| 2 | VSENS | switched 3.0 V out | — | nPM1300 LDSW1 out; C45 100 nF |
| 3 | SDA | I2C data | P1.10 (pin 38) | R15 4.7 k → VSENS |
| 4 | SCL | I2C clock | P1.11 (pin 39) | R16 4.7 k → VSENS |
| 5 | SCK | SPI clock | P2.01 (pin 12) | |
| 6 | MOSI / TX | SPI data out · UART TX | P2.02 (pin 13) | |
| 7 | MISO / RX | SPI data in · UART RX | P2.04 (pin 15) **and** P2.00 (pin 11) | |
| 8 | CS | SPI chip select (active low) | P2.05 (pin 16) | R18 10 k → VSENS |
| 9 | INT | interrupt / GPIO | P1.07 (pin 8) | R17 10 k → VSENS |
| 10 | AIN | analog in, 0–3.0 V | P1.05 = **AIN1** (pin 6) | |
| 11 | ID | board-ID resistor | P1.06 = **AIN2** (pin 7) | R19 10 k → VOUT2 |
| 12 | GND | ground | — | |
| 13 | VBAT | raw battery, unswitched | — | none (no fuse yet) |
| 14 | GND | ground | — | |
| MP | mounting tabs | ground | — | |

Pin 1 and pin 14 are both GND, so a reversed cable puts VBAT onto the sensor's VSENS pin rather than shorting the battery.

## Pins by communication standard

### I2C — pins 3, 4

| Pin | Use |
|---|---|
| 3 SDA | I2C data |
| 4 SCL | I2C clock |
| 9 INT | optional data-ready / alert |

- Host: TWIM2x instance on P1.10 / P1.11 (P1.11 is a dedicated clock pin). Separate bus from the nPM1300 I2C (P1.03 / P1.04).
- Pull-ups are on the host (4.7 k to VSENS). **Sensor boards must not add their own.**
- Pins 5–8 are unused in I2C mode and can be driven as plain GPIO if a board needs an enable or reset line.

### SPI — pins 5, 6, 7, 8

| Pin | Use |
|---|---|
| 5 SCK | clock |
| 6 MOSI | host → sensor |
| 7 MISO | sensor → host |
| 8 CS | chip select, active low |
| 9 INT | optional data-ready |

- Host: **SPIM00**, which can only use these dedicated P2 pins.
- CS idles high through a 10 k pull-up so the sensor is deselected at power-up.
- Keep SCK to a few MHz over the FFC.
- A second SPI device can take its chip select from INT (pin 9) as a GPIO.
- I2C and SPI use different pins and different peripheral instances, so **one board can use both buses at once**.

### UART — pins 6, 7

| Pin | Use |
|---|---|
| 6 TX | host transmits (sensor RX) |
| 7 RX | host receives (sensor TX) |

- Host: **UARTE00**, TX on P2.02, RX on **P2.00**.
- Pin 7 is wired to two nRF pins because SPI MISO must be P2.04 and UART RX must be P2.00 — no single pin does both. Firmware enables one and leaves the other as a disconnected input.
- UARTE00 and SPIM00 are the same hardware instance, so **UART and SPI cannot be used on the same board**. UART + I2C is fine.
- No hardware flow control. CS (pin 8) is free in UART mode and can serve as a module enable / reset GPIO.

### Analog — pin 10

- 0–3.0 V into SAADC channel AIN1.
- The sensor board drives it from its own buffer / front-end (pH, conductivity, etc.). Leave open if unused.

### Interrupt / GPIO / 1-Wire — pin 9

- Open-drain, active low, 10 k pull-up to VSENS on the host. Any GPIO-sense input, so it can wake the SoC.
- Can also carry: **1-Wire** (bit-banged; 10 k pull-up is adequate for a short cable and one or two devices), **pulse / frequency counting** (GPIOTE + TIMER) for flow meters or frequency-output probes, or a second chip select.

### Board ID — pin 11

- Sensor board fits one resistor from ID to GND; host reads AIN2 against the 10 k pull-up and picks the driver.

| R_ID on sensor board | V_ID (3.0 V) | Board type |
|---|---|---|
| short | 0 V | fault |
| 1 k | 0.27 V | 1 |
| 2.2 k | 0.54 V | 2 |
| 4.7 k | 0.96 V | 3 |
| 10 k | 1.50 V | 4 |
| 22 k | 2.06 V | 5 |
| 47 k | 2.47 V | 6 |
| 100 k | 2.73 V | 7 |
| open | 3.0 V | nothing connected |

Use 1 % resistors. Assign types as boards are designed.

### Allowed combinations

| Board uses | Pins | OK? |
|---|---|---|
| I2C only | 3, 4 (+9) | yes |
| SPI only | 5–8 (+9) | yes |
| UART only | 6, 7 (+8 as GPIO) | yes |
| I2C + SPI | 3–8 (+9) | yes |
| I2C + UART | 3, 4, 6, 7 | yes |
| SPI + UART | — | **no** — shared pins and instance |
| any of the above + AIN | + 10 | yes |

## Power pins

| Pin | Rail | Limit | Notes |
|---|---|---|---|
| 2 | VSENS 3.0 V | 100 mA (load switch rating) | nPM1300 LDSW1, input VOUT2. Firmware switches it off to power-cycle a hung sensor. Current-limited only during the 1.8 ms soft-start; shares BUCK2 (200 mA) with the SoC. |
| 13 | VBAT | battery | Always on. For actuators or loads above 100 mA; the sensor board needs its own regulator with an enable and sub-µA shutdown. |
| 1, 12, 14 | GND | | |

All signals are 3.0 V logic. A sensor that needs another voltage generates it locally.

Before switching VSENS off, firmware sets every signal pin to disconnected input or output-low so nothing back-powers the sensor through its I/O.

## Sensor board design rules

1. Pin 1 at the same end on every board; print the FFC type (same-side or opposite-side contacts) on the silkscreen.
2. No I2C pull-ups on the sensor board.
3. Fit the ID resistor (pin 11 to GND).
4. Run logic from VSENS. Use VBAT only for loads VSENS can't carry, behind a local enabled regulator.
5. Analog output on pin 10 must be buffered and stay within 0–3.0 V.
6. INT is open-drain, active low.

## Open items

1. **VBAT fuse** — add a PTC or 0 Ω placeholder between `VBAT` and pin 13.
2. **ID pull-up rail** — R19 goes to always-on VOUT2, so a fitted board draws up to ~270 µA continuously. Move it to VSENS.
3. **CS / INT pull-ups** — R17 / R18 could be 100 k to save current while VSENS is on.
4. **ESD** — no protection on the connector signals yet.
5. **3D model** alignment for the Molex footprint not verified.
6. Placement must clear the antenna keepout (`antenna-keepout-v3.md`) and the nPM1300 switcher loops.
