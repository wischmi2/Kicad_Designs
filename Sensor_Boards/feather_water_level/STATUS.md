# Feather water level sensor board - Status

Project: C:\Personal-Agents\worktrees\nrf54l15-feather-branch\Sensor_Boards\feather_water_level\feather_water_level.kicad_pro
Last reviewed: 2026-11-04

**State: rev 0.2, Acconeer XM125 60 GHz radar, placed and fully routed. ERC 0 errors, DRC 0 / 0 / 0. Fix run from the 2026-11-02 review done 2026-11-04: B1 closed, B2, S3, S4, S5, S6, S7 fixed, S8 left as is. B3 closes once Crown is modelled. A short follow-up review of the copper changes is still pending, so no fab output yet. Report: shared\reports\2026-11-02-review-feather-water-level.md.** The DFRobot A02YYUW ultrasonic plan (buck-boost, UART translator, JST PH) was dropped on 2026-10-30 (Brian approved the radar architecture); it was never drawn.

Datasheet facts, sources and UNVERIFIED items: xm125_notes.md (this folder). Parts stock check by parts-sourcing: sourcing\xm125_parts_2026-10-30.md.

## Summary
- Measures water level by looking down through the enclosure plastic (no hole). U1 XM125 sits on the **bottom side (B.Cu)**, so its top (radiating) face points out of the flat bottom of the stack, away from the feather.
- Non-isolated. Connects to the feather only through CN1 (unchanged position, rotation, pinout and footprint). Outline 50.8 x 22.86 mm, origin, holes H1-H4 unchanged.
- Power: U2 NCP161ASN180T1G 1.8 V LDO **from VBAT, EN = VSENS**. XM125 VIN and 1V8 both on +1V8 (single 1.8 V supply, allowed by datasheet 3.1). When the host turns VSENS off the LDO shuts down (active discharge, IDIS 0.01 uA typ / 1 uA max from VBAT), the module is off, and every translator is high-Z on both sides.
- Signals (all module I/O is 1.8 V, host side is VSENS = 3.0 V):
  - I2C: U3 TCA9406DCTR (internal 10k pull-ups both sides, VCC isolation + Ioff). Channels swapped for layout: the SDA_x pins carry SCL, the SCL_x pins carry SDA (both channels are identical; noted on the sheet).
  - WAKE_UP: U4 SN74AXC1T45DBVR, VSENS -> 1.8 V. R3 100k pulls RADAR_WAKE low while the host pin floats.
  - MCU_INT: U5 SN74AXC1T45DBVR, 1.8 V -> VSENS. R4 100k pulls XM_INT low while the module boots.
  - NRESET: Q1 BSS138LT1G open drain on NRESET (the STM32 NRST is bidirectional, so it is not driven push-pull). **RADAR_RST is active high** (host high = module held in reset). R2 100k keeps Q1 off while the host pin floats.
  - I2C_ADDRESS open = 0x52.
- Test pads (B.Cu): TP1 SWDIO, TP2 SWCLK, TP3 NRST, TP4 BOOT0, TP5 UART TX, TP6 UART RX, TP7 1V8, TP8 GND (all 1.8 V), plus TP9 VSENS at (133.5,122.75) and TP10 VBAT at (132.0,114.0) for bench power (added 2026-11-03, review S3). All 1.0 mm pads with no paste. Flash the Acconeer I2C distance detector with BOOT0 high + NRST pulse + a 1.8 V USB-UART (STM32 ROM bootloader, stm32loader or STM32CubeProgrammer), or with SWD at 1.8 V. Every module has to be flashed (review S3). B.SilkS legend lists the pad names.

## CN1 pin map (point to point to the feather CN1)
| Pin | Net here | Feather net | Use |
| --- | --- | --- | --- |
| 1, 12, 14, MP | GND | GND | |
| 2 | VSENS | VSENS | translator host-side supply + LDO enable |
| 3 | SENS_SDA | SENS_SDA | I2C data (host pull-ups at VSENS) |
| 4 | SENS_SCL | SENS_SCL | I2C clock |
| 5 | SENS_SCK | SENS_SCK | not used (no connection on this board) |
| 6 | RADAR_WAKE | SENS_MOSI | XM125 WAKE_UP (high = wake) |
| 7 | SENS_MISO | SENS_MISO | not used |
| 8 | RADAR_RST | SENS_CS | XM125 reset, active high |
| 9 | SENS_INT | SENS_INT | XM125 MCU_INT (high = ready / result) |
| 10 | SENS_AIN | SENS_AIN | not used |
| 11 | SENS_ID | SENS_ID | R1 = 22k to GND (ratio 0.6875, SENSORS.md) |
| 13 | VBAT | VBAT_CN1 (feather F1 polyfuse) | LDO input |

## Current state (2026-11-04)
- Schematic: root + Sensor Connector + Sensor. The Sensor sheet holds the whole radar circuit and joins CN1 by global labels (VSENS, VBAT, GND, SENS_SDA, SENS_SCL, SENS_INT, RADAR_WAKE, RADAR_RST); the root no longer has sheet pins. **The Sensor sheet was written by a script (kicad-designer, not the MCP and not the GUI)**: every connection is a label on a pin end, netlist checked pin by pin. Brian may want to open it once in eeschema and tidy label/field placement (cosmetic only).
- Project symbol library feather_water_level.kicad_sym (XM125, TCA9406DCT, NCP161ASN) and footprint library feather_water_level.pretty (Acconeer_XM125, from datasheet Fig 6.3) registered in the project sym-lib-table / fp-lib-table. 3D: feather_water_level.3dshapes/Acconeer_XM125_box.step (simple box, Acconeer publishes no model).
- PCB: U1 on B.Cu at (108.0, 121.43); translator column U2/U5/Q1/U4/U3 on F.Cu at x = 125 between the module end and CN1; their decoupling (C7-C10), C1/C2 and R4 on B.Cu under the column; C3/C4 next to the LDO, C5 10 uF + C6 100 nF on F.Cu at y 111.3, just outside the module power lands. Routing: CN1 fan-out on F.Cu, VSENS and +1V8 trunks on B.Cu, +1V8 (0.4 mm) and XM_INT long runs on In2.Cu along the board edges; In1.Cu is an unbroken GND plane. No vias under the module body; module pads are reached from outside its outline, except XM_WAKE, which runs about 0.57 mm under the body edge into pad 15 (same net, harmless). GND zones on all four layers. ANTENNA_CORNER_keepout untouched (no copper added in it).
- Vias: 71, all 0.6/0.3 mm (0.15 mm ring, PCBWay standard; review B2), default via size in the project set to match. New since the review: GND vias at C5 (98.7,111.1) and C6 (103.0,112.2) (S4), VBAT via (133.4,114.9) for TP10. Moved for the larger via: GND (133.9,120.15) to (133.9,120.05), VSENS (135.6,124.18) to (135.6,124.3).
- U1 paste (S7, 2026-11-04): copper lands carry no paste. 28 separate paste-only aperture pads, 0.80 x 1.60 mm rectangles, centred on row +-6.85 mm (module pad centre), one inside each land. The inner edge is flush with the land's inner end (0.005 mm in, 0.003 mm clear at the rounded corner) and the outer edge stops 0.795 mm short of the land's outer end. That is 56 % of the land area. Reviewer judgement; Acconeer gives no stencil data, not tried on real parts. Other B-side parts (C1, C2, C7-C10, R4) keep their normal paste; test pads have none. Checked on the plotted B.Paste Gerber: 42 flashes, 28 for U1 and 14 for the 7 passives.
- U1, U2-U5 and Q1 GND pads use solid zone connections. The Acconeer no-thermal-relief advice (HIG 3.3.2) is about the bare A121, so this is allowed but not required (review N1); solid pads make hand rework harder.
- Silk: references of passives and the dense translator column are on the Fab layers (assembly drawing); B.SilkS has WATER LEVEL RADAR / R_ID 22k (0.6875), WATER LEVEL rev 0.2, the test-pad legend, BOOT0, VSENS, VBAT and the CN1 FFC note, all at 0.15 mm stroke (S5). A Dwgs.User note under the board gives the radome rule.
- Finish: stackup copper_finish set to ENIG (S6). S8 (R1.1 to GND track 0.13 mm) left as is by decision; order at 4/4 mil.
- ERC (kicad-cli 10.0.4, 2026-11-04): **0 errors**, 15 warnings, same list as before the fix run: 3 isolated_pin_label (unused CN1 SENS_SCK / SENS_MISO / SENS_AIN), 3 lib_symbol_issues + 3 footprint_link_issues (EasyEDA2Kicad / easyeda2kicad / Connector_FFC-FPC libs not registered on this PC), 4 lib_symbol_mismatch (GND), 2 pin_to_pin (EasyEDA C1/C2 pin types).
- DRC (kicad-cli 10.0.4, 2026-11-04, --schematic-parity, with and without --refill-zones): **0 errors, 0 unconnected, 0 parity**, 5 warnings, same list as before: 3 lib_footprint_issues (easyeda2kicad not registered), 2 silk_over_copper (EasyEDA pin-1 dots on R1 and C1, the fab clips them).
- STEP: C:\Personal-Agents\shared\handoff\feather_water_level\feather_water_level_2026-11-04.step (board, CN1, XM125 box, ICs and passives). Outline, CN1 (position, rotation, pins, nets) and H1-H4 are unchanged from before the fix run (compared with 3d1b810), so the enclosure dimensions stand. The XM125 on the bottom is still about 1.9 mm below the board (UNVERIFIED height).
- Fab outputs: none.

## Parts added 2026-10-30 (MPN + Manufacturer fields on every symbol; DigiKey stock read live on 2026-10-30 unless noted)
| Ref | Part | MPN | DigiKey stock |
| --- | --- | --- | --- |
| U1 | Acconeer XM125 radar module | XM125 | 0 (Mouser 1,263 per parts-sourcing) |
| U2 | onsemi 1.8 V 450 mA LDO, SOT-23-5 | NCP161ASN180T1G | 52,345 |
| U3 | TI I2C translator, SM8 | TCA9406DCTR | 19,574 |
| U4, U5 | TI 1-bit translator, SOT-23-6 | SN74AXC1T45DBVR | 17,046 |
| Q1 | onsemi N-MOSFET, SOT-23 | BSS138LT1G | 51,132 |
| C3, C4 | 1 uF 16 V X5R 0402 | CL05A105KO5NNNC (Samsung) | 16,103 |
| C5 | 10 uF 6.3 V X5R 0402 | GRM155R60J106ME15D (Murata) | 2,505,987 |
| C6-C10 | 100 nF 10 V X7R 0402 | GRM155R71A104KA01D (Murata) | 1,430,877 |
| R2-R4 | 100k 1 % 0402 | RC0402FR-07100KL (Yageo) | 5,319,508 |
| R1 | 22k 1 % 0402 (changed from 10k) | RC0402FR-0722KL (Yageo) | 0 (Mouser 119k per parts-sourcing; DigiKey has RC0402FR-1322KL, 20,963) |
| TP1-TP8 | 1.0 mm SMD test pads | - (board only, out of BOM) | - |
No LCSC numbers were added (DigiKey/Mouser are the sources for this board).

## Decisions
- 2026-11-02 (Brian): two feather builds. This board needs the radar build, with feather R15, R16, R17 and R18 not fitted (review B1 and S2). No copper change. See ..\CN1_SENSOR_CONNECTOR.md, Feather builds.
- 2026-10-30 (Brian): radar (XM125) replaces the A02YYUW ultrasonic plan; sensor inside the enclosure looking through the plastic; only CN1 to the feather; small form factor.
- 2026-10-30 (kicad-designer): VIN = 1.8 V, not 3.3 V. The 3.3 V VIN range is 2.97-3.45 V and VSENS is 3.0 V (30 mV margin); a 3.3 V rail from VBAT (3.0-4.2 V) would need a buck-boost. 1.8 V for both pins plus translators works over the whole battery range.
- 2026-10-30 (kicad-designer): LDO from VBAT with EN = VSENS, not from VSENS. The datasheet current profile peaks at about 80 mA typical (no maximum given; A121 alone may draw up to 100 mA per supply), which leaves no margin in the 100 mA VSENS budget. NCP161 is the LDO family Acconeer use on the XE125 EVK (VDIG ripple matters).
- 2026-10-30 (kicad-designer): translators with VCC isolation / Ioff on every module signal (TCA9406 for I2C, SN74AXC1T45 for WAKE_UP and MCU_INT), open-drain MOSFET for NRESET, so nothing back-powers the module or the host when VSENS is off.
- 2026-10-30 (kicad-designer): **H1/H2 stay NPTH.** GND reaches this board through CN1 (4 GND pins + shell); a plated GND ring would only add a second ground path through the standoffs and puts nothing useful near the radar. Re-open if the enclosure needs metal standoffs there.
- 2026-10-30: CN1 pins 6/8 renamed RADAR_WAKE / RADAR_RST, pin 7 SENS_MISO (was SENS_TX / SENS_CS / SENS_RX).

## Open work
- Short follow-up review of the 2026-11-03 copper changes (vias, TP9/TP10, S4 vias), then fab output by the coordinator.
- Review items: B1 closed by the two-build decision (radar feather build, R15-R18 not fitted; sheet note corrected). B2, S3, S4, S5, S6, S7 fixed. S8 left as is by decision. B3: the layout question is answered by Crown, but it only closes once Crown is modelled. On a standard feather R18 pulls RADAR_RST to about 2.7 V, so the radar stays in reset until firmware drives SENS_CS low; use the radar build.
- Firmware (firmware-dev): RADAR_WAKE on the feather SENS_MOSI pin, RADAR_RST (active high) on SENS_CS, SENS_INT, I2C address 0x52; SENS_ID 22k.
- Enclosure concepts for B3 (2026-11-02): shared\design\feather_water_level\enclosure_concepts_radar_2026-11-02\concepts.md. Recommends Crown (cell in a lid hump behind the radar), fallback Slab; no PCB change. Brian picked Crown (next line).
- Enclosure decision (2026-11-02): Brian picked Crown, which closes the B3 layout question once it's modelled. Mounting options: shared\design\feather_water_level\crown_mounting_2026-11-02\mounting.md (read section 14 first). Fusion modelling waits on Brian's answers there.
- Mounting decisions (Brian, 2026-11-03): can lid off, A2 Span in several lengths (printed bars to about 430 mm rim, stock PVC/HDPE bars to 700 mm). Holes: both small and large, A6 Pad (25-33 mm) and A5 Expander (50.5 mm and up). No underside access assumed, so no A3 Collar. Indoors, dry, so no face gasket or UV requirement. Model these three adapters plus the dock ring and blank plate. Not yet settled: the larger A6 gasket for 33-44 mm holes, stock bars vs printed-only details.
- Enclosure (fusion-enclosure): STEP 2026-10-30; radar faces down out of the bottom; wall in front of U1 about n x lambda/2 thick in the plastic (PETG about 1.5-1.6 mm, er UNVERIFIED) and a gap of about n x 2.5 mm, no metal in the beam (xm125_notes.md).
- Bench: confirm the XM125 boots and enumerates at 0x52 from a VSENS cold start; check the +1V8 ripple during the 80 mA burst.

## Decisions (Brian, 2026-11-03)
1. Power: VSENS stays on, radar in hibernate between readings (about 110 uA idle on the radar feather build: R19/R1 94 uA + module 17.7 uA, about 2.6 mAh a day).
2. Finish: ENIG. Stencil: B-side, with reduced U1 apertures.
3. Assembly: hotplate, module first; other F-side parts afterwards by hand or hot air.
4. Flashing: J-Link over SWD (TP1, TP2, TP3, TP7, TP8). J-Link model and its VTref range at 1.8 V still to check. Every module has to be flashed: the datasheet says it's delivered with a bootloader (review S3).
5. Field update of the XM125: opening the enclosure is OK. No CN1 change.
6. Radar wall: PETG 1.5-1.6 mm, confirmed by a coupon test on a SparkFun breakout before the final print.
7. Buying: SparkFun breakout now; XM125 modules when the board is ordered, with a spare. Brian orders.
8. Review items to fix: B2, S3 test pads, S4, S5, S6, S7 (all done 2026-11-04). S8 left as is (0.13 mm gap, order at 4/4 mil).

## Questions for Brian
1. J-Link model, to check VTref at 1.8 V.
