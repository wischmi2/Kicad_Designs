# Acconeer XM125 - facts used for the feather water-level board

Collected 2026-10-30 (kicad-designer). Each fact has its source. Anything not read in a document is marked UNVERIFIED.

Sources (downloaded from developer.acconeer.com on 2026-10-30):
- [DS] XM125 Datasheet v1.2 (2023-10-04): https://developer.acconeer.com/download/xm125-datasheet/
- [I2C] XM125 I2C Distance Detector User Guide v1.13.0 (2026-03-27): https://developer.acconeer.com/download/xm125-i2c-distance-detector-user-guide/
- [SW] XM125 Software User Guide v1.13.0: https://developer.acconeer.com/download/xm125-software-user-guide/
- [XE] XE125 (Entry+ module EVK) hardware user guide, 2023-07-03, incl. schematics: https://developer.acconeer.com/download/xe125-user-guide/
- [HIG] Hardware and physical integration guideline, A1 PCR sensors (2025-10-02): https://developer.acconeer.com/download/hardware-integration-guideline/
- [A121] A121 PCR datasheet: https://developer.acconeer.com/download/a121-datasheet/
- [SF] SparkFun XM125 Eagle library (cross-check of the land pattern): https://github.com/sparkfun/SparkFun_Qwiic_Pulsed_Radar_Sensor_XM125/blob/main/Hardware/XM125.lbr

## Module
- LGA module, 18.6 x 15.0 mm, module PCB 1.0 mm thick [DS 2, 6, Fig 6.1]. Contains the A121 60 GHz radar (antenna in package) and an STM32L431CBY6 (Cortex-M4, 80 MHz, 128 kB flash, 64 kB RAM), 24 MHz crystal [DS 2.2, BOM].
- Total height: not given as a number. Estimate about 1.9 mm (1.0 mm PCB + 0.88 mm A121 package [A121]). **UNVERIFIED**; the box STEP uses 1.88 mm.
- MSL3, one reflow pass recommended [DS 6.1]. Brian hand-assembles: bake if the bag has been open, solder the module once (hot air or hotplate), then do the small parts.
- A121 centre is 7.80 mm from the left edge, 7.50 mm from the bottom edge (top view, pin 1 bottom-left) [DS Fig 6.1]. The A121 outline is on F.Fab of the footprint.

## Supplies
- Pin 3 "1V8": A121 analog/digital supply, 1.71 / 1.8 / 1.89 V, abs max 2.0 V [DS Table 1, 2, 3].
- Pin 1 "VIN": A121 I/O and MCU supply, either 1.8 V (1.71-1.89 V) or 3.3 V (2.97-3.45 V), abs max 3.63 V. I/O range 0 to VIN + 0.3 V [DS Table 1, 2, 3].
- A single 1.8 V supply on both pins is allowed [DS 3.1: "support a 1.8 V external single power supply or 1.8 V and 3.3 V IO interface power supply"]. **Used here: VIN = 1V8 = +1V8**, so all module I/O is 1.8 V.
- VDIG ripple must meet the A121 datasheet chapter 6.5 spec [DS 3.1]. **UNVERIFIED** (chapter not read). Mitigation: the LDO is the NCP161 family Acconeer use on the XE125 EVK (NCP161BMX180TBG, [XE] schematic sheet 2); 1 uF at the LDO output plus 10 uF + 100 nF at the module pins.
- Current: the current profile for a 2.75 m distance-detector measurement peaks at about 80 mA for about 1.5 ms, with 6-15 mA plateaus around it [DS Fig 5.1, 1.8 V]. A121 "current into any power supply" max 100 mA [A121 4.4]. No module maximum is given. **The 80 mA is a typical curve, not a max.**
- Average: 0.33 mW at 1 Hz, 2.75 m range (about 0.18 mA at 1.8 V); hibernate 17.7 uA; off 6.9 uA [DS Table 4].

## Pinout [DS Table 1]
| Pad | Signal | Used here |
| --- | --- | --- |
| 1 | VIN | +1V8 |
| 3 | 1V8 | +1V8 |
| 2, 4, 7, 10, 13, 16, 19, 22, 27 | GND | GND (solid zone connection, as [HIG 3.3.2] recommends) |
| 5 | UART_TX (module out) | XM_UART_TX -> TP5 |
| 6 | UART_RX (module in) | XM_UART_RX -> TP6 |
| 8 / 9 | UART_CTS / UART_RTS | NC |
| 11 / 12 | SWD_IO / SWD_CLK | TP1 / TP2 |
| 14 | NRESET (active low) | XM_NRESET: Q1 open drain + TP3 |
| 15 | WAKE_UP | XM_WAKE via U4 from CN1 RADAR_WAKE |
| 17 / 18 | I2C_SCL / I2C_SDA | via U3 to CN1 SENS_SCL / SENS_SDA |
| 20 | I2C_ADDRESS | NC -> address 0x52 (GND = 0x51, VIN = 0x53) [I2C 2.1, 3.1] |
| 21 / 23 | DEBUG_UART_RX / TX | NC |
| 24 / 25 | MISC_GPIO0 / 1 | NC |
| 26 | MISC_GPIO2_BOOT0 | TP4 (high during boot = ROM bootloader) |
| 28 | MCU_INT | XM_INT via U5 to CN1 SENS_INT |

Pad numbering: pad 1 bottom-left in top view, 1-14 along the bottom, 15-28 back along the top (counter-clockwise) [DS Fig 2.3]. Agrees with [SF].

## Land pattern [DS Fig 6.3]
28 pads, 0.95 x 2.40 mm, pitch 1.27 mm (gap 0.32), row span 17.46 mm, outer edge to edge 16.89 mm, inner 12.09 mm (row centres +-7.245 mm). Body assumed centred on the pad field (the drawing gives no offset; [SF] is centred, rows at +-7.21 mm with the same 2.4 x 0.95 pads). Footprint: feather_water_level.pretty/Acconeer_XM125.kicad_mod. Acconeer publishes no STEP; feather_water_level.3dshapes/Acconeer_XM125_box.step is a simple box (18.6 x 15 x 1.0 PCB + A121/crystal/MCU blocks, 1.88 mm max).

## I2C / control [I2C]
- I2C up to 100 kHz standard / 400 kHz fast mode (2.2). Register protocol: 16-bit address, 32-bit data, big endian (3.2).
- Pull-ups: none shown on the XE125 (R11/R12 DNP, [XE] sheet 3); whether the module has internal I2C pull-ups is **UNVERIFIED**. Here the TCA9406 has 10k pull-ups on both sides, so it does not matter.
- Start-up/low-power sequence (2.3): host sets WAKE_UP high, waits for MCU_INT high, then talks I2C; to sleep, wait MCU_INT high, set WAKE_UP low, wait MCU_INT low. "Measure on wake up" mode exists (2.4.3). Module reset by register command RESET MODULE (2.4.5); NRESET pad also resets (DS 3.2).
- I/O levels: STM32 at VIN (1.8 V here). The host side of CN1 is VSENS (3.0 V), so everything goes through translators.

## Firmware loading [SW 3], [XE]
- The STM32L431 ROM bootloader is enabled at manufacture [SW 3]. Flash over UART: BOOT0 high, pulse NRESET, then STM32CubeProgrammer or `stm32loader -p COMx -e -w -v <bin>`, then reset/power-cycle [SW 3.2, 3.3]. The XE125 EVK uses the main UART pins (UART_TX/UART_RX) for this ([XE] sheet 1: CP2105 to UART_TX/RX; DFU button SW1 = BOOT0, RESET button SW2 = NRESET, [XE] buttons table).
- SWD (J-Link / ST-Link) also works [SW 4.2.1, DS 2.2].
- Whether a new XM125 ships with the I2C distance detector (or any application) already flashed: **UNVERIFIED / not stated** in the documents read. Plan on flashing it: the I2C distance detector binary is in the XM125 SDK / Exploration Server download (login + licence on developer.acconeer.com).
- On this board: TP4 BOOT0 (bottom edge, below pad 26), TP3 NRST, TP5 TX, TP6 RX, TP7 1V8, TP8 GND, TP1 SWDIO, TP2 SWCLK, all on B.Cu, **1.8 V logic**. Use a 1.8 V USB-UART (or a debugger with VTref = 1.8 V). Power the board from the feather (VSENS on) or from a bench 3.0-4.2 V on VBAT with VSENS (EN) high.

## Placement and keep-outs [HIG 3.3, 3.7], [DS 2.2]
- The module radiates broadside from its top (component) side; it can sit behind plastic or glass, no aperture needed [DS 2.2]. On this board U1 is on B.Cu, so the top of the module faces down, away from the feather, out of the flat bottom of the stack.
- The A121's ground plane is the module's own PCB; the host PCB under the module does not form the antenna ground. No copper, part or silk keep-out zone beyond the module outline is specified in the XM125 datasheet. [HIG 3.3.2] advice (for the bare A121): keep routing and large parts away from the sensor; flat parts are fine. Here only flat test pads and 0402s sit on the bottom side, at least 4 mm (passives) from the module edge; the test pads are flush.
- Radome (the enclosure wall in front of U1) [HIG 3.7]: wall thickness ideally n x lambda/2 in the plastic, lambda0 = 5 mm at 60.5 GHz: 1.55 mm for er = 2.6 (ABS), about 1.5 mm for PC (er 2.75) or PLA (er 2.85, [HIG] Appendix A). PETG is not in the table (er about 2.6-3.0, **UNVERIFIED**). Gap from the sensor to the wall ideally n x lambda0/2 = n x 2.5 mm (with optimum thickness); otherwise d1 = n x lambda0/4 +- 0.5 mm for odd n. Do not press the cover onto the sensor (about 6 dB loss) [HIG 3.7.3].
- Beam: A121 HPBW about 65 deg (H-plane) / 53 deg (E-plane) [A121 features]. Keep metal (screws, standoffs) out of that cone in front of U1. H1/H2 holes are about 6 mm left of the module edge and screw heads sit behind the module face, so they are outside the cone.
