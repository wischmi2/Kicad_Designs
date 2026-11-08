# Feather water level sensor board, TC2030 variant - Status

**This is the TC2030 variant of feather_water_level rev 0.2**: a copy made 2026-11-07 from commit 750fb6b, adding a Tag-Connect TC2030 legged programming port for the XM125 (Brian 2026-11-07). The original board in ..\feather_water_level\ stays untouched as the fallback (its fab zip 2026-11-04 is still valid for that board only). Library nicknames (feather_water_level symbols and footprints, feather_water_level.3dshapes) are kept as in the original; only the project was renamed. Everything under "Original rev 0.2 status" is the original file, kept for reference; "this folder" there now means this copy.

Project: C:\Personal-Agents\worktrees\nrf54l15-feather-branch\Sensor_Boards\feather_water_level_tc2030\feather_water_level_tc2030.kicad_pro

## Fab output (2026-11-07)
- **Zip:** C:\Personal-Agents\shared\handoffeather_water_level_tc2030eather_water_level_tc2030_fab_2026-11-07.zip (16 files at the zip root; unzipped copy in fab_2026-11-07\ next to it). Made after the S2 follow-up review was clean. Not uploaded or ordered.
- **Gate:** kicad-cli pcb drc --schematic-parity --severity-all, saved board, no --refill-zones: 0 errors / 0 unconnected / 0 parity (5 warnings, same as before).
- **Export options** (reproduce the original feather_water_level 2026-11-04 zip byte for byte apart from dates): `pcb export gerbers --check-zones` (kicad-cli defaults, no --subtract-soldermask, no --board-plot-params) on F.Cu, In1.Cu, In2.Cu, B.Cu, F/B.Mask, F/B.Silkscreen, F/B.Paste, Edge.Cuts plus job file; `pcb export drill --format excellon --drill-origin absolute --excellon-units mm --excellon-separate-th --generate-map --map-format pdf`.
- **Order notes (PCBWay):** 4 layers, 1.6 mm, ENIG, 4/4 mil, standard stackup with no impedance control. Stencil: 0.12 mm, bottom only, from B_Paste (ignore F_Paste). **The 7 NPTH holes of J1 (4 x 2.375 mm, 3 x 0.991 mm) are Tag-Connect holes and must be unplated** (NPTH file; H4 2.7 mm is the only plated big hole). The TC2030 cable is a tool, not a BOM part. No pos/BOM files.
- Differences from the original zip: copper, masks (J1), silk, drill (67 vias + H4 plated; 7 new NPTH), job file names/min line width 0.15. B_Paste, F_Paste, Edge_Cuts identical.

## TC2030 variant (2026-11-07)
**State: J1 TC2030 placed and routed on the copy; review fixes S1-S3, N4, N6, N8 done 2026-11-07 (follow-up run). ERC 0 errors, DRC 0 / 0 / 0. A short follow-up review of the copper change (S2) is next, before any fab output; fab output made 2026-11-07, see "Fab output".**

### Follow-up 2026-11-07 (review shared\reports\2026-11-07-review-feather-water-level-tc2030.md, items Brian picked)
- **S1 plug-head fit, verdict: clear.** No Tag-Connect 3D model could be found (product page, footprint-downloads page, site search, KiCad 10 3D library; 3 tries), so feather_water_level.3dshapes/TC2030-IDC_plug_box.step was built from the TC2030-IDC Datasheet Rev B sheet 2: pin carrier (nose) 7.35 x 3.7 mm (scaled from the drawing, no dimension given) from the board face up to 7.5 mm; grip body 9.906 x 6.096 mm (the larger, side-view dimension; the end view says 9.271) from 7.5 mm up; four legs through the leg holes. Body face height 7.5 mm = 11.328 (body face to leg tip) - 2.235 (tip past the far face) - 1.6 (board). Results along x (towards U1): nose ends at x 97.28, **1.42 mm** from the U1 body edge (x 98.70) at U1 height; the grip body ends at x 98.55 (9.906) or 98.24 (9.271) but starts about **5.6 mm above U1's top** (U1 about 1.88 mm tall, box model); worst-case envelope (9.906 mm head right down to the board face) **0.15 mm, no overlap**. U1 outline: XM125 DS v1.2 Fig 6.2 shows the pad rows centred on the 18.60 mm body (pad end 0.58 mm from the edge at both ends, footprint 0.57), so the footprint's "assumed centred" note holds. The plug overhangs the left board edge (x 90.0) by about 1.35 mm. The model is on J1 (board and library footprint) as a **hidden** model, so it isn't in the board STEP or renders; tick it visible in the footprint's 3D tab to look. Picture: C:\Personal-Agents\shared\design\feather_water_level\tc2030_2026-11-07\plug_fit_check.png. Still to confirm with a real cable (drawing says dimensions are subject to change).
- **S2 escapes:** RX (pin 4) and BOOT0 (pin 3) dog-legs replaced by single straight 0.15 mm B.Cu segments: RX (93.6,120.795) to (94.55,119.40), BOOT0 (93.6,122.065) to (94.55,123.46), then the existing x 94.55 lanes (shortened to start there). Measured: **0.581 mm** from each to the nearest other-net J1 pad (RX to pin 2, BOOT0 to pin 1; Tag-Connect note 3 wants 0.508), 0.335 mm from the diagonal and 0.323 mm from the x 94.55 lanes to the leg holes at x 92.965 (rule 0.25). Every other-net B.Cu track near J1 is now 0.58 mm or more from the pads (TX/GND/+1V8/NRST escapes 0.801). Zones refilled.
- **N6 silk:** B.SilkS "UART" (0.8 mm, 0.15 mm stroke) at (96.7, 126.7), on the J1 line next to "J1" / "TC2030" (first tried under "TC2030", but H2's mask opening clipped it). Reads "UART J1" from the bottom side. So nobody plugs in an SWD Tag-Connect cable (it would put VCC on NRST).
- **S3, N8:** XM125_PROGRAMMING.md part 0: shrouded keyed 2x3 box header with pin 1 marked on the adapter, 2-pin jumper in series with the 1 k for BOOT0 release (pull jumper or unplug J1, then power-cycle), power order (board first, then FTDI USB, or pulse NRST once; inferred), I/O limit cited correctly (DS Table 3 VIN + 0.3 V = 2.1 V operating; Table 2 3.63 V is the absolute maximum). Part 1 line fixed the same way.
- **N4:** hole-to-edge is 0.565 mm (fixed below).
- Checks (kicad-cli 10.0.4): ERC **0 errors** / 15 warnings (same list). DRC on the saved board, --schematic-parity --severity-all, **no --refill-zones: 0 errors, 0 unconnected, 0 parity**, 5 warnings (3 lib_footprint_issues easyeda2kicad, 2 silk_over_copper on R1/C1, same as before). With --refill-zones on a copy: the same. STEP re-exported (overwritten): C:\Personal-Agents\shared\handoff\feather_water_level_tc2030\feather_water_level_tc2030_2026-11-07.step (outline and connectors unchanged; plug model hidden, not in it).
- Commits: 17a57fb (S1 model), bea8b77 (S2 copper + silk), then this docs commit.

### What changed against rev 0.2
- **J1 Tag-Connect TC2030 legged footprint** (value TC2030-IDC, in_bom no, excluded from BOM and pos, MPN field "DNP (Tag-Connect pads; cable TC2030-IDC, DigiKey TC2030-IDC-ND)"). Symbol Connector_Generic:Conn_02x03_Odd_Even on the Sensor sheet, written by script into sensor.kicad_sch (not by the MCP), netlist checked pin by pin, plus a note on the sheet. Brian may want to open the sheet once in eeschema (cosmetic only).
- **Footprint** feather_water_level.pretty/Tag-Connect_TC2030-IDC-FP_2x03_P1.27mm_Vertical: copied from KiCad 10 Connector.pretty, the same footprint the pouch gateway uses for J6. Checked against Tag-Connect drawing TC2030-IDC-FP rev B (12/05/19, sheet 1 of the TC2030-IDC datasheet rev B): 6 contact pads 0.787 mm on 1.27 mm pitch, rows 1.27 mm apart; 3 alignment holes 0.991 mm; **4** leg latch holes 2.375 mm NPTH (the drawing has four, not three); hole positions match (0.200, 0.125, 0.050, 0.100, 0.040, 0.025 in). No paste, mask open on the pads; the stock keep-out zone between the pads (no vias, no pour) is kept. Added: a pad-side courtyard 9.4 x 8.6 mm for the plug head (9.27 x 7.45 mm per drawing sheet 2) and an opposite-side courtyard over the leg feet (legs stand 2.24 mm out of the far side; each foot needs 1.55 x 1.17 mm, drawn on the opposite Fab layer).
- **Side: pads on B.Cu (the XM125 side), legs latch on F.Cu.** Why: the TPs are already on B and are reached with the stack lifted off the Crown posts, so the cable plugs in from the same side; on F the feather sits 8 mm above, so the 2.24 mm leg tips fit even with the feather fitted; and the left end between H1 and H2 is the only area free on both sides (U1 fills the B side, the translator column and CN1 the F side further right).
- **Position: J1 at (93.6, 121.43), B side** (rotation 180 after the flip). Pads x 92.33 / 93.6 / 94.87; y 120.795 for pins 6, 4, 2 and y 122.065 for pins 5, 3, 1 (pin 1 nearest U1, bottom row). Leg holes at x 92.965 and 96.14, y 118.89 and 123.97; alignment holes at (96.14, 121.43), (91.06, 120.414) and (91.06, 122.446). Holes are 0.565 mm from the left board edge (alignment holes at x 91.06, edge x 90.0) and outside the 8 mm Crown post circles at H1/H2 (nearest leg hole 1.16 mm outside the H1 circle). Nothing new in front of U1 on B.Cu. Squeeze access for the legs is from the two long board edges.
- **Routing:** +1V8 (pin 2) to TP7 on B.Cu along x 97.9. BOOT0 (pin 3) to TP4 on B.Cu along the bottom edge (y 131.6). TX (pin 6), RX (pin 4) and NRST (pin 1) on In2.Cu along y 113.0 / 113.4 / 113.8 to new vias at (105.46, 112.2) TX and (107.0, 112.35) RX next to TP5/TP6, and to the existing NRST via (117.4, 112.2). GND (pin 5) to a new GND via at (91.3, 125.76). 0.15 mm tracks in the connector escapes and the In2 lanes, 0.2-0.3 mm elsewhere; new vias 0.6/0.3.
- **Removed:** 10 GND stitching vias (GND only, no tracks on them): 8 under J1 at x 91.2 / 93.6, y 118.4 / 120.8 / 123.2 / 125.6; (96.0, 113.6) in the In2 lanes; (105.4, 112.0) between TP5 and TP6, whose place the TX via takes. Added 1 GND via (91.3, 125.76). F, In1 and B GND stay tied by the remaining vias; DRC reports no isolated copper.
- **In1:** still an unbroken GND plane apart from the 7 NPTH holes of J1 (round voids at the left end, away from U1).
- **Pour keep-out:** rule area TC2030_pad_pour_keepout on B.Cu keeps the GND pour at least 0.5 mm from every J1 pad (Tag-Connect note 3; measured 1.27 mm minimum). Escape tracks: since the 2026-11-07 follow-up (S2) every other-net track is 0.58 mm or more from the J1 pads (RX and BOOT0 0.581 mm, the rest 0.8 mm or more), meeting Tag-Connect note 3 (0.508 mm). (Before: RX and BOOT0 dog-legs passed 0.369 mm from pins 2 and 1.)
- **Kept:** TP1-TP10 unchanged, outline, CN1, H1-H4, U1 position, side and paste apertures, vias 0.6/0.3, In1 GND, ENIG, stackup, design rules (4/4 mil). J1 has no paste, so the B stencil (B_Paste) is unchanged.
- **Silk:** B.SilkS "WATER LEVEL rev 0.2" now reads "WATER LEVEL rev 0.2-TC2030"; "J1" and "TC2030" under the connector, pin 1 marked, plus "UART" next to "J1" (2026-11-07). "WATER LEVEL RADAR" and "R_ID 22k (0.6875)" sat where J1 is, so they moved to F.SilkS in the middle of the board with a third line "rev 0.2-TC2030".

### J1 pin map (TC2030 pin = pin of the TC2030-IDC 6-pin 0.1 in ribbon socket, 1:1 per the Tag-Connect drawing)
| TC2030 pin | Net | XM125 | Note |
| --- | --- | --- | --- |
| 1 | XM_NRESET | NRESET, U1.14 | same net as TP3 (optional reset) |
| 2 | +1V8 | VIN / 1V8 | reference only (BOOT0 pull-up source, level check); never power the board from the cable |
| 3 | XM_BOOT0 | MISC_GPIO2_BOOT0, U1.26 | 1 k to pin 2 to enter the bootloader |
| 4 | XM_UART_RX | UART_RX (module input), U1.6 | cable TXD (orange) here |
| 5 | GND | GND | cable GND (black) |
| 6 | XM_UART_TX | UART_TX (module output), U1.5 | cable RXD (yellow) here |

+1V8 (pin 2) and GND (pin 5) are at opposite corners, not next to each other. Power comes from the feather (VSENS) or the bench supply on TP9/TP10, as before.

### Checks (kicad-cli 10.0.4, 2026-11-07)
- Stage 0 copy check: ERC 0 errors / 15 warnings; DRC (--schematic-parity --severity-all, no refill) 0 errors / 0 unconnected / 0 parity / 5 warnings. Both lists identical to the original. No new lib warnings. Left out of the copy: fab_2026-11-04\ and .mcp-backups\.
- After J1: ERC 0 errors / 15 warnings (same list). DRC on the saved board, --schematic-parity --severity-all, **no --refill-zones: 0 errors, 0 unconnected, 0 parity, 5 warnings** (the same 3 lib_footprint_issues and 2 silk_over_copper as the original). Zones were refilled in KiCad Python before saving.
- STEP: C:\Personal-Agents\shared\handoff\feather_water_level_tc2030\feather_water_level_tc2030_2026-11-07.step. Outline, CN1 and H1-H4 unchanged; J1 is pads and holes only (no 3D body).
- Images: C:\Personal-Agents\shared\design\feather_water_level\tc2030_2026-11-07\ (connector close-ups of both sides, bottom side and In2 of the whole board, 3D top and bottom).

### For the Crown enclosure
- J1 centre at board (93.6, 121.43): 3.6 mm in from the left (H1/H2) edge, on the board centre line, between the H1 and H2 posts. Pads face the sole.
- Holes through the board: 4 x 2.375 mm and 3 x 0.991 mm (positions above). The 8 mm posts stay where they are; the nearest leg hole is 1.16 mm outside the H1 post circle.
- Flashing is done with the stack out of the enclosure, as for the TPs, so the enclosure needs nothing for J1 in use. With the cable on: the plug head (about 9.3 x 7.5 mm, about 19 mm long plus cable) stands on the bottom face, overhangs the left board edge by about 1 mm, and needs finger room from both long edges; the leg tips stand 2.24 mm above the top face, inside the 8 mm standoff gap.
- A sole window for flashing in place would be about 10 x 9 mm at J1, outside the radar pocket (not drawn, not asked for).

### Open
- Short follow-up review of the S2 copper change (and a glance at the UART silk), then fab output if clean (CLAUDE.md conditions).
- Plug head fit: clear on the box model (1.42 mm at U1 height, 0.15 mm worst-case envelope, no overlap); confirm with a real TC2030-IDC cable on the first board. Unverified on hardware.
- Not tried on hardware: TC2030 fit, flashing through J1.
- The coordinator adds this board to the CLAUDE.md Boards table.

---

## Original rev 0.2 status (from feather_water_level at 750fb6b)

Last reviewed: 2026-11-04

**State: rev 0.2, Acconeer XM125 60 GHz radar, placed, fully routed, fab zip made 2026-11-04. ERC 0 errors, DRC 0 / 0 / 0. Follow-up review (shared\reports\2026-11-04-review-feather-water-level-followup.md) had no open blockers; Brian approved SF1 and SF2 and closed B3 for fab on 2026-11-04 on that review's reasoning. Crown enclosure still to model. Earlier report: shared\reports\2026-11-02-review-feather-water-level.md.** The DFRobot A02YYUW ultrasonic plan (buck-boost, UART translator, JST PH) was dropped on 2026-10-30 (Brian approved the radar architecture); it was never drawn.

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
- U1 paste (S7, 2026-11-04): copper lands carry no paste. 28 separate paste-only aperture pads, 0.80 x 1.60 mm rectangles, centred on row +-6.85 mm (module pad centre), one inside each land. The inner edge is flush with the land's inner end (0.005 mm in, 0.003 mm clear at the rounded corner) and the outer edge stops 0.795 mm short of the land's outer end. That is 56 % of the land area (superseded by SF1 below). Reviewer judgement; Acconeer gives no stencil data, not tried on real parts. Other B-side parts (C1, C2, C7-C10, R4) keep their normal paste; test pads have none. Checked on the plotted B.Paste Gerber: 42 flashes, 28 for U1 and 14 for the 7 passives.
- U1, U2-U5 and Q1 GND pads use solid zone connections. The Acconeer no-thermal-relief advice (HIG 3.3.2) is about the bare A121, so this is allowed but not required (review N1); solid pads make hand rework harder.
- Silk: references of passives and the dense translator column are on the Fab layers (assembly drawing); B.SilkS has WATER LEVEL RADAR / R_ID 22k (0.6875), WATER LEVEL rev 0.2, the test-pad legend, BOOT0, VSENS, VBAT and the CN1 FFC note, all at 0.15 mm stroke (S5). A Dwgs.User note under the board gives the radome rule.
- SF1 (2026-11-04): the 28 U1 paste-only apertures are now 0.80 x 1.50 mm at row +-6.90 mm (spans 6.15 to 7.65 mm from module centre; board y 114.53 and 128.33), X unchanged, in the footprint and on the board; footprint descr updated. B_Paste Gerber: 42 flashes, 28 of them 0.80 x 1.50 (aperture D14). Not tried on real parts.
- SF2 (2026-11-04): F.SilkS references H1, H2, H3, H4, R1, CN1 stroke 0.12 to 0.15 mm, still visible. No new DRC problem.
- Finish: stackup copper_finish set to ENIG (S6). S8 (R1.1 to GND track 0.13 mm) left as is by decision; order at 4/4 mil.
- ERC (kicad-cli 10.0.4, 2026-11-04, after SF1/SF2): **0 errors**, 15 warnings, same list as before: 3 isolated_pin_label (unused CN1 SENS_SCK / SENS_MISO / SENS_AIN), 3 lib_symbol_issues + 3 footprint_link_issues (EasyEDA2Kicad / easyeda2kicad / Connector_FFC-FPC libs not registered on this PC), 4 lib_symbol_mismatch (GND), 2 pin_to_pin (EasyEDA C1/C2 pin types).
- DRC (kicad-cli 10.0.4, 2026-11-04, after SF1/SF2, --schematic-parity --refill-zones): **0 errors, 0 unconnected, 0 parity**, 5 warnings, same list: 3 lib_footprint_issues (easyeda2kicad not registered), 2 silk_over_copper (EasyEDA pin-1 dots on R1 and C1, the fab clips them).
- STEP: C:\Personal-Agents\shared\handoff\feather_water_level\feather_water_level_2026-11-04.step (board, CN1, XM125 box, ICs and passives). Outline, CN1 (position, rotation, pins, nets) and H1-H4 are unchanged from before the fix run (compared with 3d1b810), so the enclosure dimensions stand. The XM125 on the bottom is still about 1.9 mm below the board (UNVERIFIED height).
- Fab outputs (2026-11-04): fab_2026-11-04\ in this folder, zipped to C:\Personal-Agents\shared\handoff\feather_water_level\feather_water_level_fab_2026-11-04.zip (16 files: F.Cu, In1, In2, B.Cu, F/B mask, F/B silk, F/B paste, Edge.Cuts, .gbrjob, PTH and NPTH Excellon, two drill maps as PDF). Plotted with --check-zones; the four copper plots are identical to plots made from the stored fill. PTH drill: 71 holes at 0.30 mm (all the vias) plus one 2.7 mm plated hole at (138.26,112.54), H3 (pad type plated; H1, H2, H4 are NPTH; corrected 2026-11-07 from the pre-order check). No old fab files existed to archive. No pos or BOM. Not uploaded or ordered.
- Order notes: PCBWay 4-layer 1.6 mm, ENIG, 4/4 mil, 0.15 mm min annular ring. Stencil 0.12 mm, bottom side only, from B_Paste; tell PCBWay not to use F_Paste (it holds only the F-side passives and ICs, not wanted for a stencil you don't order). XM125 height (about 1.9 mm below the board) and the paste apertures are unverified on real parts.

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
- Follow-up review done and fab zip made 2026-11-04 (see State). Next: Brian orders; first-article check of the paste apertures and XM125 height.
- Review items: B1 closed by the two-build decision (radar feather build, R15-R18 not fitted; sheet note corrected). B2, S3, S4, S5, S6, S7 fixed. S8 left as is by decision. B3: closed for fab by Brian 2026-11-04 (Crown still to model). On a standard feather R18 pulls RADAR_RST to about 2.7 V, so the radar stays in reset until firmware drives SENS_CS low; use the radar build.
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
4. Flashing (changed 2026-11-04; full procedure, cable wiring and parts in XM125_PROGRAMMING.md, this folder): 1.8 V USB-UART through the STM32 ROM bootloader (TP5 TX, TP6 RX, TP8 GND, TP4 BOOT0 held high to TP7 through a resistor, TP3 NRST as backup). Brian's programmer is the nRF9160 DK, whose on-board J-Link is restricted to Nordic targets per forum reports and SEGGER terms (not tried on the STM32L431). Candidate cable: FTDI TTL-232RG-VREG1V8-WE; its red VCC wire stays unconnected. Bench power 3.0 V on TP10 VBAT and TP9 VSENS. Connection method (soldered wires or pogo jig) not chosen yet. Every module has to be flashed: the datasheet says it's delivered with a bootloader (review S3).
5. Field update of the XM125: opening the enclosure is OK. No CN1 change.
6. Radar wall: PETG 1.5-1.6 mm, confirmed by a coupon test on a SparkFun breakout before the final print.
7. Buying: SparkFun breakout now; XM125 modules when the board is ordered, with a spare. Brian orders.
8. Review items to fix: B2, S3 test pads, S4, S5, S6, S7 (all done 2026-11-04). S8 left as is (0.13 mm gap, order at 4/4 mil).

## Questions for Brian
1. Flashing connection: soldered wires or a printed pogo jig (decision 4).
