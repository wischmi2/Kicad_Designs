# nRF54L15 feather - Status

Project: C:\Personal-Agents\worktrees\nrf54l15-feather-branch\nrf54l15_feather\nrf54l15_feather\nrf54l15_feather.kicad_pro
Last reviewed: 2026-10-27 (run 5 stage 1: schematic changes, PCB updated, not yet placed or routed)

**State: ACTIVE main board (2026-10-23, per Brian).** It replaces nrf54l15_v4. The active sensor board for it is nrf54l15_feather_sens1 (pH).

## Summary
Board in Feather form factor built around the nRF54L15 (U6, nRF54L15-QFXX) with a 32 MHz crystal (X1) and a chip antenna (AE1, 2450AT18A100E).
- Power: nPM1300 PMIC (U2), AEM10330 energy harvester (IC1), and two JST PH 2-pin connectors (U4, U5).
- Interfaces: USB-C (J1, TYPE-C-31-M-12), 10-pin SWD header (J3, FTSH-105), 14-pin Molex 503480-1400 sensor connector (CN1), one push button (SW1), one LED.
- Sub-sheets: nrf54l15, npm1300, power_supply, battery, usb, antenna, SWD_Debug, sensor_connector, moisture_sensor (empty, 169 bytes).

## Feather rework progress (2026-10-25, kicad-designer)
Stages from the 2026-10-24 task. Each stage is its own commit on agent/nrf54l15-feather.
1. [done] ERC clean-up of the schematic. Netlist checked identical before/after (96 nets).
   - usb.kicad_sch: no-connect flags on J1 A6/A7/A8/B6/B7/B8 (charge-only USB, per Brian).
   - npm1300.kicad_sch: removed #FLG04 (PWR_FLAG on VOUT2/VDDIO, which U2 already drives) and a dangling 1.27 mm wire stub at (127, 33.02). No new "not driven" error appears on VOUT2/VDDIO.
   - ERC now: **1 error, 204 warnings** (was 8 errors).
   - Remaining error, accepted: power_pin_not_driven on C4 pin 1 (GND). The EasyEDA-imported symbol CL05A105KO5NNNC has its pins typed "input" instead of passive. GND does have a PWR_FLAG (#FLG41 in power_supply); a test copy with a second flag on GND in npm1300 clears this error but adds a power-out-to-power-out conflict with #FLG41, so it's a false positive. Proper fix: set the symbol's pins to passive in the library and update the symbol (GUI).
   - Warnings: 77 pin_to_pin, 57 lib_symbol_issues and 55 footprint_link_issues (the easyeda2kicad / EasyEDA2Kicad / TYPE-C-31-M-12 libraries aren't in the kicad-cli library tables on this PC; environment, not design), 5 off-grid, 5 lib_symbol_mismatch, 3 same local/global label, 2 multiple net names.
2. [done] Board outline: Edge.Cuts is now 50.8 x 22.86 mm with R2.54 corners, top-left at (90, 110) in board coordinates, so the board spans x 90 to 140.8 and y 110 to 132.86. The USB end is x = 90. To convert from Feather coordinates (origin bottom-left at the USB end, y up): X = 90 + fx, Y = 132.86 - fy. The four GND pours were reshaped to the new outline (unfilled).
   - DRC after this stage is an intermediate state (parts still at the old positions, many off-board): 120 errors (114 copper-edge clearance), 420 warnings, 132 unconnected, 0 parity.
3. [done] Placement per Proposal C, all 64 parts on top (J3, U4, U5 flipped from the bottom). All old tracks and vias (1055 items) were ripped up; the board is unrouted after this stage.
   - J1 USB-C: origin (95.32, 121.43) rot -90, centred on the USB short edge, mouth at x = 90.
   - U5 solar JST: (101.95, 116.42) rot 0, opening on the top long edge. U4 battery JST: (101.95, 126.44) rot 180, opening on the bottom long edge.
   - **CN1 (superseded by run 2 stage 1, see below): origin (138.39, 121.43) rot -90, centred on the far short edge** (same edge offset and pad orientation as the old board, signal pads toward the edge at x = 139.71). Feather coordinates: centre (48.39, 11.43); courtyard fx 46.07 to 50.71, fy 6.73 to 16.13. Pin 1 is at board y 118.18 (top side of the connector), pin 14 at y 124.68.
   - (superseded by run 2 step 1c) AE1 chip antenna: (131.55, 130.23) rot 0 on the bottom long edge, feed pad 1 at (129.97, 130.23). Keep-out moved to x 128.55 to 134.55, y 128.75 to the edge (same 5.9 x 3.1 size as before, now running to the edge); pads allowed (AE1's own), tracks allowed for the feed line, no vias, no pours.
   - RF chain (L5, C8, L6, C5, L8, C13, R11 switch, C12, L2, L3) runs straight down from U6 pin 31 at x 128.6, then C12/L3 to the antenna feed. RF1 U.FL + R11 ANT_SEL kept, RF1 at (126, 127.9) to the left of the switch.
   - U6 nRF54L15 at (128.4, 117.9) rot -90 (ANT, XTAL and SWD pins face down). X1 bottom-right of U6. DCC/DECD/DECA parts (L7, C10, L4, C1, C11, C9, C26) between U6 and CN1. Sensor pull-ups (R15 to R19) and C45 between X1 and CN1.
   - U2 nPM1300 at (117.9, 117.0) rot 180 (bucks face U6, VBUS/VBAT/VSYS face the AEM). L9/L10 and VOUT1/VDDIO caps right of U2; VSYS/VBUS/VBAT caps below it.
   - IC1 AEM10330 at (111.35, 114.0) with L11 and C40 to its left (next to U5), C41 on the VINT pins, C42/C43 below.
   - J3 SWD at (108.85, 128.6), bottom edge next to U4. SW1 at the bottom edge (116.4, 130.9) with LED1/R14 next to it.
   - Proposal C drew SW1 on top of U4, so SW1 moved to the bottom edge in the middle.
   - DRC after placement: 4 errors, 430 warnings, 193 unconnected (unrouted), 0 parity. The 4 errors are hole_clearance inside the J1 footprint (its own NPTH pegs vs pads A1B12/A4B9/B1A12/B4A9, 0.185 to 0.217 mm vs 0.25). They are in the 2026-10-23 board too when checked with kicad-cli 10.0.4 (the old board actually had 6 errors, not 0), so they're from the footprint and acceptable.
4. [done] Mounting holes at the Feather positions, board-only footprints (excluded from BOM and position files):
   - H1 (92.54, 112.54) and H2 (92.54, 130.32), USB end: plated, 2.5 mm drill, 3.2 mm pad (Feather M0 values), no net.
   - H3 (138.26, 112.54) and H4 (138.26, 130.32), far end: NPTH 2.5 mm, for nylon screws next to the antenna and CN1.
   - DRC: same 4 J1 errors, 432 warnings, 193 unconnected, 0 parity. No hole or courtyard conflicts.
   - STEP exported: C:\Personal-Agents\shared\handoff\nrf54l15_feather\nrf54l15_feather_2026-10-25.step (board, holes and CN1). The EasyEDA 3D models (${EASYEDA} path) aren't on this PC, so 56 parts have no body in the STEP; heights for J1, U4/U5 and J3 must come from their datasheets for now.
5. [partial] Routing, commit d3aea86. Done with Freerouting 2.5.0, run from a portable Temurin 25 JRE in the agent scratch folder (nothing installed).
   - Settings: GND left out of the autorouter (pours + stitching vias instead); In1.Cu kept as a solid GND plane with no routing; signals on F.Cu / In2.Cu / B.Cu; 0.2 mm tracks (0.25 mm for VBAT/VBUS/VSYS/SW1/SW2/solar); 0.6/0.3 vias so the 0.25 mm hole clearance holds; 0.45 mm edge keep-out; antenna keep-out closed to tracks during routing.
   - Five autorouter runs; the best one (route5) is imported.
   - Then a scripted GND via + stub went next to each GND pad the pours can't reach (50 added), and the antenna feed from L3 to AE1 pad 1 was drawn by hand (0.2 mm, F.Cu, inside the keep-out).
   - All four GND pours refilled.
   - DRC now: **16 errors, 438 warnings, 28 unconnected, 0 parity.**
   - Errors:
     - 4 hole clearance inside the J1 footprint (accepted, see stage 3).
     - 2 hole clearance: /Solar/VINT on B.Cu passes IC1's EP thermal vias.
     - 6 starved thermal: the GND pads of R1, R2, R8, C44 and C11 on F.Cu, and IC1's EP on B.Cu, get 1 spoke instead of 2.
     - 4 solder-mask bridge: a VDDIO F.Cu track runs under J3 between pads 03/05/07/09.
     - All of these need fixing by hand.
   - Unconnected signals (8): VBUS (U2 pin 21), VSENS (U2 pin 29 to C45/CN1), SENS_SCL (U6 pin 39), U2-SW1 (U2 pin 3 to L9), VSYS (U2 pin 4 and C20, 2 links), I2C_SCL (U2 to U6), U2-NTC (U2 pin 18 to R8).
   - Unconnected GND (20 pad links):
     - Mostly QFN GND pins with no room for a via (IC1 x8, U2 x3, U6 x3). These should get short F.Cu stubs into their exposed pads.
     - The rest are decoupling caps around U2/U6 (C1, C6, C9, C10, C13, C14, C16, C17, C22, C26, C42) and CN1 pin 12.
   - Warnings: 199 silk overlap and 170 silk over copper (reference text not moved yet), 55 lib_footprint_issues (EasyEDA library not configured in kicad-cli), 8 silk edge clearance, 4 dangling vias.
   - ERC unchanged: 1 error (C4, accepted), 204 warnings.
   - This is autorouter-quality routing. Check the AEM10330 loop (DS section 10), the nPM1300 buck loops and the RF chain by hand before fab.

## Feather rework run 2 (2026-10-25, kicad-designer)
1. [done] CN1 turned 180 degrees so the FFC opening faces the far short edge. **Orientation verified against SD-503480-001 by coordinator 2026-10-25** (back-flip: signal tails at the back, FFC enters from the front on the mounting-tab side).
   - CN1 origin **(138.475, 121.43), rotation +90**. Signal pads at x = 137.15: **pin 1 (GND) at (137.15, 124.68)**, **pin 14 (GND) at (137.15, 118.18)**; pin order runs from pin 1 at the bottom (U4 long edge side) to pin 14 at the top. MP tabs at (139.80, 117.39) and (139.80, 125.47).
   - **Housing front (FFC opening) at x = 140.45**, 0.35 mm inside the board edge (x 140.8). The limit is the MP tab copper: its outer edge is at x 140.30, which is the board's DRC copper-to-edge rule of 0.5 mm (the 0.45 mm figure was only the Freerouting keep-out; 0.45 would give a DRC error). Housing front = MP outer edge + 0.15 mm per the datasheet land pattern. Courtyard reaches x 140.795.
   - 3D model checked with kicad-cli pcb render: the model's contact tails sit over the signal pads (inner side), and the black actuator (modelled closed) covers the front 1.65 mm on the edge side, with the FFC slot facing the edge. That matches the datasheet top view (closed actuator over the front, tails visible at the back), so the model offset/rotation in the footprint was left unchanged.
   - Fan-out: pins 2 (VSENS) and 4 (SCL) go straight left on F.Cu to R16; pins 1 and 14 go on F.Cu to the MP tabs and a GND via each; every other pin has a 0.15 mm F.Cu stub to a 0.6/0.3 via in a three-column staircase under the connector body (x 138.05 / 138.80 / 139.55, all tented, inside the body outline). From there the nets run on In2.Cu / B.Cu (and short F.Cu pieces) to the old routes. The CN1 GND pads (1, 12, 14) use a solid zone connection.
   - All CN1 nets connected. DRC: 15 errors (4 J1 accepted, 2 VINT hole clearance, 5 starved thermal, 4 mask bridge, all pre-existing), 27 unconnected (none on CN1), 0 parity. ERC: 0 errors, 204 warnings (kicad-cli 10.0.4 now reports the C4 power-pin case as a warning).
1b. [done] Holes per Brian's answers: H1-H4 drill 2.5 -> 2.7 mm; H1/H2 pad 3.2 -> 3.4 mm and net GND (0.84 mm from pad to the R2.54 corner edge); H3/H4 NPTH 2.7 mm, no net. DRC unchanged (15 errors, all pre-existing; 27 unconnected; 0 parity).

1c. [done] AE1 moved to the far corner (Brian's decision, see Decisions).
   - **AE1 at (134.67, 130.08), rotation -90**: long axis at right angles to the bottom edge, pad 1 (feed) at (134.67, 128.50) toward the ground, NC pad 2 at (134.67, 131.66) pointing into the corner. Its centre x is limited by H4: the AE1 body (right edge x 135.47) just touches H4's courtyard (r 2.79 mm, screw-head/washer allowance); moving AE1 further right would put the body under the nylon screw head.
   - New rule area **AE1_keepout: x 132.15 to the board edge, y 126.40 to the board edge** (rectangle clipped by the outline, so it follows the R2.54 corner), all four copper layers: no pours, no vias; footprints/pads allowed; the only track inside is the 0.17 mm feed line. The old keep-out (x 128.55-134.55) is deleted and GND fills that area again. The left edge sits at 132.15 rather than 134.3 because the pad must be 1.6 mm from ground on that side too.
   - **Measured ground-to-pad-1 clearance: 1.60 mm** (In1 GND plane at the keep-out's top edge; the F.Cu pour on the left is 1.645 mm away). Pad 2 to nearest ground: 1.645 mm. H4 (NPTH) and CN1 unchanged.
   - Inside the keep-out besides AE1: R17.1/R18.1 (VSENS pull-up pads, not ground) reach about 0.15/0.26 mm over the top edge, about 1.35 mm from pad 1. They were left in place because moving them up makes their courtyards overlap R16/C45.
   - RF chain: C12 (1.0 pF, series) at (129.6, 128.5), L2 (2.7 nH shunt to GND) at (130.35, 129.0), L3 (3.9 nH series) at (131.1, 128.5); 0.17 mm F.Cu line (about 50 ohm over In1 at 0.1 mm dielectric, closed-form estimate) from the R11 switch RF1 pin through C12/L3 to pad 1 at y 128.5; 2.5 mm of it runs inside the keep-out. GND stitching vias at (129.9, 127.75), (131.5, 127.8), (131.6, 129.3) and the L2 GND via (130.35, 129.85). **Match values must be tuned on the real board.** RF1 U.FL + R11 unchanged as the fallback.
   - R19 (ID pull-up) moved out of the corner to (130.4, 131.3); SENS_ID, VDDIO and the CN1 VBAT link re-routed around the keep-out.
   - DRC after this step: 15 errors (all pre-existing: 4 J1, 2 VINT, 5 starved thermal, 4 J3 mask bridge), 23 unconnected, 0 parity.

2. [partial] Hand-finishing the routing (commits 90ea263, b20a3b7). Done with a small clearance-checked grid router written for this run (scratch script, not committed) plus hand-placed tracks; every step DRC-checked with kicad-cli.
   - U2 buck side reworked: L9 turned 180 deg to (121.7, 119.15) so SW1 (U2.3) and VOUT1 (U2.1) no longer cross; L10 moved up 0.5 mm to (121.7, 115.99). SW1, SW2 (0.3 mm) and U2.4 VSYS (0.25 mm, F.Cu to C22.2) now connected. PMIC_INT re-routed via B.Cu from a via next to U2.8; the VDDIO link from the L10/C7 group to the U6/J3 group re-routed on B.Cu.
   - U2 left side: VSYS (U2.20) and VBUSOUT (U2.22) fan-out vias re-placed; LED1-C moved to B.Cu so C16.2 and C20.2 (VSYS) join on F.Cu (0.4 mm). U2-NTC routed (In2).
   - QFN GND pins stubbed on F.Cu into their exposed pads: U2 pins 2 and 6, U6 pins 32 and 44, IC1 pins 24, 25, 26 and 39. GND vias/links added for C14, C16, C22, C6/C17, C26, C9, C10 and C1 (the U6-DECA loop under C1 was re-routed above it so C1.2 can reach GND).
   - **Still open (stopped after 3 attempts each, see Next steps):** VBUS from U2.21 (trapped between the VSYS and VBUSOUT fan-out vias on U2's left side; the dense via column there leaves no 0.2 mm channel), VSENS from U2.29 (no escape from the U2 bottom row and no via site within reach), SENS_SCL from U6.39 (boxed in by the SDA fan-out, C1/C9 and their GND links), I2C_SCL between U6.4 and R12/U2.14 (R12.1 sits in a closed F.Cu pocket with no via site), GND on IC1.18 + C42.2 (the /Solar/LOAD track runs between IC1's bottom pins and its EP) and GND on C13.2 (RF area), plus one small F.Cu pour island.
3. [done] DRC error fixes (commit 2fdadd7): VDDIO track moved from y 129.04 (inside J3's bottom pad row) to y 128.6 between the rows; /Solar/VINT moved from B.Cu (it ran between IC1's thermal vias) to In2; solid zone connection on the EPs/thermal vias of IC1, U2, U6 and on the GND pads of R1, R2, R8, C44, C11 (and CN1 pins 1/12/14). Result: only the 4 accepted J1 hole-clearance errors remain.
4. [done] Silkscreen and vias (commit 9014b25): 33 references re-placed at 0.8 mm, clear of pads, copper and the edge; 31 references in the dense passive clusters are hidden on silk (still on F.Fab for the assembly drawing); H1-H4 references and all silk values hidden. The 4 dangling vias (VBUS, VSENS, SENS_SCL, I2C_SCL leftovers) and their stubs removed. The remaining 170 silk_overlap / 95 silk_over_copper / 2 silk_edge warnings are all footprint outline graphics (EasyEDA footprints), not text.
5. [done] STEP exported: C:\Personal-Agents\shared\handoff\nrf54l15_feather\nrf54l15_feather_2026-10-25b.step (CN1 rotated, AE1 moved, holes 2.7 mm). EasyEDA 3D models are still missing on this PC, so most parts have no body.
   - **Final checks (kicad-cli 10.0.4): ERC 0 errors, 204 warnings (77 pin_to_pin, 57 lib_symbol_issues, 55 footprint_link_issues, 5 off-grid, 5 lib_symbol_mismatch, 3 same local/global label, 2 multiple net names). DRC 4 errors (J1 footprint hole clearance, accepted), 322 warnings (170 silk_overlap, 95 silk_over_copper, 55 lib_footprint_issues, 2 silk_edge), 7 unconnected, 0 parity.**

## Feather rework run 3 (2026-10-25, kicad-designer): the 7 unconnected items
Brian approved small placement changes (small passives and vias, about 1 mm or less) to clear the 7 unconnected items from run 2. Each step was checked with kicad-cli 10.0.4 DRC (zones refilled). No new DRC errors. Routing used a small clearance-checked grid router (scratch script, not committed).
1. [done] **VBUS** (U2.21 to C14.1/J1), commit 8dbaf71. The VSYS F.Cu path from U2.20 boxed in pins 21-24, so the VSYS via moved out of that pocket and the fan-out vias were spaced along x 114.62:
   - VSYS via (114.70, 116.80) -> (114.10, 116.80). VSYS F.Cu now runs straight left from U2.20 along y 116.75, then down x 114.05 (the old diagonal is gone). The In2 VSYS tie to U2.4/C22 gets about 0.6 mm longer. The F.Cu VSYS path to C16/C20 is about the same length.
   - VBAT F.Cu from U2.19 now runs left along y 116.25 to x 113.5, then down to the existing (113.4, 117.1) node. The old diagonal is gone, and the path is about 0.5 mm longer.
   - VBUS: new via (114.62, 117.30). B.Cu 0.25 mm down x 113.95 to a new via (114.15, 123.30), then F.Cu to C14.1.
   - VBUSOUT via (114.70, 117.75) -> (114.62, 118.00). CC1 via (114.646, 118.478) -> (114.62, 118.72). CC2 via (114.919, 119.281) -> (114.62, 119.42). The CC2 In2 lead-in was re-drawn.
2. [done] **VSENS** (U2.29 to C45/R15-R18), commit e8a6ac8.
   - C3 (118.10, 121.60) -> (118.10, 121.80), 0.2 mm down, to make room for a new VSENS via at (118.15, 120.10) under U2.29.
   - VDDIO via (120.18, 119.748) -> (120.18, 119.65).
   - VBUSOUT B.Cu re-routed: (114.62, 118.0) -> (114.85, 118.0) -> diagonal -> (119.1, 122.25) -> via (120.307, 122.261).
   - VSENS runs on In2 along y 120.2 to x 125, then down to y 124.15 (moved there in item 7) and up to a new via (134.0, 123.05) next to C45.
3. [done in run 4 by Brian] **SENS_SCL** (U6.39 to R16.2/CN1.4). Stopped after 3 attempts. C1 (0201 DECA cap at (132.696, 119.2)) sits directly in front of U6.39: C1.1 is 0.49 mm from the pin end. The SDA fan-out (pin 38) closes the path below, and the DECA via (132.203, 117.801) with its pin-43 stub closes the 0.15 mm channel above.
   - The router found no path, even in a what-if with the C1/C9 GND links and the C1 DECA links removed. The only via site would be where C1 is.
   - Fix needs: move C1 (and C11) about 0.3-0.5 mm up/right and re-route the DECA bridge (C1.1-C11.1-L4.2) and the C1/C9 GND links, or move SENS_SCL to another U6 pin (schematic + firmware change). This changes the DECA decoupling loop, so it was left for review.
4. [done] **I2C_SCL** (U6.4 to R12.1/U2.14), commit 01ed624.
   - R12 (117.53, 112.70) -> (117.60, 112.20). New SCL via (117.60, 113.20) under R12.1. The VDDIO R12.2-R13.2 link was re-drawn.
   - SENS_AIN fan-out via (130.362, 113.539) -> (130.75, 113.50), so a new SCL via (129.85, 113.70) fits above U6.4.
   - SCL runs on B.Cu: diagonal to y 111.5, west along y 111.5, then a diagonal to (117.6, 113.2).
   - R13 reference text moved to (119.30, 111.105), clear of R12's silk.
5. [done] **GND IC1.18/C42.2**, commit 7a82fe7.
   - New GND via (112.40, 117.55) next to C42.2, inside the LOAD/VBAT pocket. /Solar/LOAD is unchanged.
   - VSET1 B.Cu re-routed to clear the via: diagonal from (114.653, 114.955) to (113.4, 116.208), down x 113.4 to 118.9, then a diagonal back to x 112.511.
6. [done] **GND C13.2** (RF shunt cap), commit fa66dce.
   - C13 rotated 0 -> 180 deg in place at (127.55, 125.70), so its GND pad faces away from the ANT node. The ANT branch is now a 0.38 mm stub from the main ANT path.
   - C13.2 (now at 127.28, 125.70) goes to a new GND via (126.62, 125.75). The AE1 keep-out is untouched.
7. [done, review] **F.Cu pour island**, commit 9f9f2c1. The island was X1 pad 4 (crystal case GND) plus a 0.25 mm2 pour fragment. It's boxed in by VDDIO/DECA on F.Cu, SENS_INT on B.Cu, and VDDIO/MOSI on In2, and there is no legal via site outside the pad.
   - A GND via (0.6/0.3) sits **inside X1.4** at (131.35, 123.05). This is via-in-pad, so check the solder wicking risk, or have the fab fill/cap it.
   - The VSENS In2 tail moved from y 123.05 to y 124.15 to clear the via.
8. [done] Final checks (kicad-cli 10.0.4):
   - **ERC** (default severity, as before): 0 errors, 204 warnings (77 pin_to_pin, 57 lib_symbol_issues, 55 footprint_link_issues, 5 off-grid, 5 lib_symbol_mismatch, 3 same local/global label, 2 multiple net names). With --severity-all the known C4 power_pin_not_driven false positive shows as 1 error. The schematic was not changed.
   - **DRC**: 4 errors (J1 hole clearance, accepted), 323 warnings (164 silk_overlap, 102 silk_over_copper, 55 lib_footprint_issues, 2 silk_edge), **1 unconnected (SENS_SCL)**, 0 parity. The +8 silk_over_copper are R12's EasyEDA outline over R10/R13 pads after the R12 move.
   - STEP: C:\Personal-Agents\shared\handoff\nrf54l15_feather\nrf54l15_feather_2026-10-25c.step. Outline and connectors are unchanged from 2026-10-25b; only small parts moved.

### Next steps after run 3 (superseded by run 4)
1. SENS_SCL (see run 3 item 3): needs a DECA-area rework around C1/C11/L4, or a pin change. Ask Brian which.
2. Review the via-in-pad on X1.4 (run 3 item 7).
3. Check the AEM10330 loop (DS section 10), the nPM1300 buck loops (L9 flipped; the VSYS via moved 0.6 mm in run 3) and the RF chain (C13 turned 180 deg) by hand before fab. Tune the AE1 match on the real board.
4. Install the EasyEDA 3D models (or map them to KiCad models) so the STEP has part bodies.

## Feather rework run 4 (2026-10-26, kicad-designer)
1. [done] **SENS_SCL routed by Brian** in the KiCad GUI (hand edit, committed as-is in 309ab2e). U6.39 goes to a 0.5/0.3 via at (132.16, 119.29), B.Cu to a via at (135.2, 122.2), then F.Cu to CN1.4. This closes run 3 item 3; C1/C11/L4 were not moved.
2. [done] Three DRC errors from that edit fixed (commit 2a074ab):
   - SENS_SCL via (135.22, 122.18) moved to (135.20, 122.20), with its F.Cu and B.Cu track ends. Clearance to the U6-DECA B.Cu track goes from 0.097 to about 0.125 mm (rule 0.1 mm).
   - C45 pad 2 and C10 pad 1 (GND): solid zone connection, which clears the starved thermals (same fix as run 2 for R1, R2, R8, C44, C11).
   - Zones refilled.
3. [done] Final checks (kicad-cli 10.0.4):
   - **DRC** (--schematic-parity --refill-zones): **4 errors (J1 hole clearance, accepted), 327 warnings (165 silk_overlap, 105 silk_over_copper, 55 lib_footprint_issues, 2 silk_edge), 0 unconnected, 0 parity.** Warnings are the same as before the fixes.
   - **ERC**: 0 errors, 204 warnings (schematic not changed).
   - STEP: C:\Personal-Agents\shared\handoff\nrf54l15_feather\nrf54l15_feather_2026-10-26.step. Outline and connectors are unchanged from 2026-10-25c.

### Next steps after run 4 (superseded by run 5, see below)
1. Review the via-in-pad on X1.4 (run 3 item 7).
2. Check the AEM10330 loop (DS section 10), the nPM1300 buck loops and the RF chain by hand before fab. Tune the AE1 match on the real board.
3. Check Brian's SENS_SCL route in the design review (it runs on B.Cu under the DECA area).
4. Install the EasyEDA 3D models (or map them to KiCad models) so the STEP has part bodies.

## Run 5 stage 1 (2026-10-27, kicad-designer): schematic changes from the 2026-10-27 review decisions
Source of the decisions: C:\Personal-Agents\shared\reports\2026-10-27-review-verification-nrf54l15-feather.md ("Decision" sections). Schematic edits were made as text edits to the sheet files (not with MCP placement tools), each new symbol with its own instance path; every step was checked with a kicad-cli netlist export and ERC. The PCB was then updated with KiCad's pcbnew Python (not the MCP sync tool). New symbols sit in empty areas of their sheets and may want tidying in the GUI. One commit per step (1.1 to 1.14 below, 1.15 is this file).

Primary sources opened today (2026-10-27):
- nPM1300 PS (docs.nordicsemi.com, ps_npm1300): BUCK "Output voltage selection" and "On/Off control", BUCK "Component selection", LOADSW/LDO main page and electrical specification, pin assignments QFN32, absolute maximum ratings, recommended operating conditions, SYSREG electrical specification, VBUS overvoltage protection, battery temperature monitoring, reference circuitry configurations 1-3 (BOM tables; Figures 1 and 3 are SVG images: I could read the text labels and their coordinates, not the wiring).
- nRF54L15 PS (ps_nrf54l15): LFXO section, circuit configuration 1 (Figure 1 text).
- TI SN74AUP1G34 datasheet SCES603K (Aug 2004, rev. Oct 2014), TI TPD1E10B06 datasheet SLLSEB1G (rev. Aug 2024), Littelfuse SMF series datasheet (rev. 12/06/17, via LCSC C207255), Murata NTC thermistor catalog (via LCSC C77131), Bourns MF-FSMF series datasheet (via LCSC C210356), Johanson 2450AT18A100 datasheet (text extracted by the verifier on 2026-10-27).
- Not opened by me: the FM8625H datasheet (the 100 pF VDD cap and the 1.65-2.70 V VCTL high window come from the coordinator's reading of datasheet v1.2 in the review report, B4 update), the Molex 503480 product page (timed out; the 500 mA contact rating is from the LCSC/JLC listing of C505360), and the Epson FC-12M datasheet (crystal data from the JLC listing).
- Stock: every LCSC number below was checked on 2026-10-27 with the JLCPCB parts search API (jlcpcb.com), which reports stock; the local MCP JLC database is empty.

**Correction to the task text:** the nPM1300 VBUS overvoltage threshold is **5.5 V**, not 22 V. SYSREG electrical specification: "VBUSOVP | Overvoltage protection threshold | 5.5 V". The 22 V figure is the VBUS absolute maximum ("VBUS | -0.3 | 22"). Recommended operating VBUS is 4.0-5.5 V.

1. **[done] R1, R2 (5.1k on CC2/CC1) DNP**, footprints kept, a "DNP Reason" field added. PS USB port detection (spot-checked by the coordinator): "These pins have internal pull-downs with resistance equal to Rd"; SYSREG spec "Rd | Pull-down resistance on pins CC1 and CC2 | 5.1 kΩ". Commit 176118f.
2. **[done] VRF rail from nPM1300 LDSW2 in LDO mode.** U2.30 LSIN2/VINLDO2 -> VDDIO, U2.31 LSOUT2/VOUTLDO2 -> new net **VRF** (their NC flags removed). R11 (FM8625H) VDD moves from VOUT1 to VRF; **C15 (100 nF 0603, already R11's local VDD cap on the antenna sheet) moves with it**. Commit 20b9c21.
   - LDO spec (LOADSW/LDO electrical specification): "VINLDO | Input voltage range | 2.6 to VSYS V" (VDDIO 3.0 V is inside), "VOUTLDO 1.0 to 3.3 V, 100 mV steps", "IOUTLDO 50 mA (VOUT > 1.2 V)", "LDODROPOUT 25 mV (3.3 V out, 50 mA)", "IQLDO 500 nA typ (BUCKs in hysteretic mode)". Main page: "The load switches (and LDOs) are OFF by default", "The mode is selected using registers LDSW[n]LDOSEL", "The LDO output voltage is configurable in registers LDSW[n]VOUTSEL". Nothing to strap.
   - **Output cap: the PS text gives no LDO output-capacitor value.** The only source is reference circuit configuration 1: BOM "C2, C3, C4, C7, C8, C9, C10, C11, C12 | 10 μF | Capacitor, X5R, 25 V, ±20% | 0603", and in Figure 1 the labels C9/C10 (10 µF) sit under VINLDO1/VOUTLDO1 and C11/C12 (10 µF) under VINLDO2/VOUTLDO2 (read from the SVG text positions; the wires are not readable). So **C46 10 µF 0603** on VRF (Samsung CL10A106KP8NNNC, 10 V X5R, **C19702**, JLC basic). VINLDO2 sits on VDDIO, which already has C7/C17 10 µF.
   - **C47 100 pF 0402 C0G** at R11 VDD (Samsung CL05C101JB5NNNC, **C26409**). Source: FM8625H datasheet v1.2 application circuit "100 pF on VDD" (as recorded in the review report; I did not open the PDF).
   - VRF loads: R11 (IDD 50 µA typ / 90 µA max per the review's FM8625H reading) + U7 (0.9 µA max) + caps, far below 50 mA.
3. **[done, flagged] BUCK1 off at power-up; L9 and C18 kept.** Commit a16b84f.
   - The PS does **not** say how to leave a BUCK unused: the pin table has no "unused" notes, and the BUCK pages say nothing about unused SW/VOUT pins or PVDD caps. Reference configuration 2 (BOM: one inductor L1, one VSET resistor R3) appears to use one BUCK only, but its schematic is an image and I could not read how the second BUCK's pins are wired.
   - So, per the task, BUCK1's parts stay and VSET1 is set to the PS "off" setting. PS Output voltage selection, VSET1 table: "Grounded (<100 Ω): 0 V (OFF)", and "Do not leave VSET[n] floating". On/Off control: "If the pin is grounded, BUCK is disabled." and "If BUCK is disabled during power up, the system defaults to software control of BUCK."
   - **R9 47k -> 0R 0603** (UNI-ROYAL 0603WAF0000T5E, **C21189**, basic). VOUT1 now has only U2.1, L9 and C18 (no load).
   - Open: remove L9/C18 only after Nordic (DevZone) or the config 2 figure confirms the unused-BUCK pin handling. Firmware must never set BUCK1ENASET.
4. **[done] Level-shift buffer U7 SN74AUP1G34DCKR** (SC70-5, **C2675656**, 801 in stock, extended). A = ANT_SEL (U6.24 P0.01), Y = new net **ANT_VCTL** (R11.6 VCTL), VCC = VRF, GND; pin 1 NC flagged. **C48 100 nF 0402** VCC decoupling (Samsung CL05B104KO5NNNC, **C1525**, basic). **R20 1M 0402 DNP** pull-down on the input (UNI-ROYAL 0402WGF1004TCE, **C26083**). Commit 201e188.
   - SCES603K: pin functions DCK "NC 1, A 2, GND 3, Y 4, VCC 5"; "Inputs are overvoltage tolerant allowing them to go as high as 3.6 V at any valid VCC"; VOH "IOH = -20 µA, 0.8 V to 3.6 V: VCC - 0.1" (2.4 V at 2.5 V, inside the FM8625H 1.65-2.70 V high window); VIH 1.6 V at VCC 2.3-2.7 V; ICC "VI = GND or (VCC to 3.6 V), IO = 0: 0.9 µA"; Ioff 0.6 µA (so a 3.0 V input with VRF off is fine); section 11: "For devices with a single supply, 0.1 µF is recommended".
   - SCES603K footnote: "All unused inputs of the device must be held at VCC or GND". Firmware drives P0.01 before turning VRF on; fit R20 if that can't be guaranteed.
   - To make ERC see VRF as driven, U2 pin 31 (LSOUT2/VOUTLDO2) is typed **power_out** in the nPM1300 symbol embedded in npm1300.kicad_sch (it was "output"; a PWR_FLAG would then conflict). The hlord2000 library isn't on this PC, so the library copy is unchanged.
   - U7's symbol is KiCad's 74LVC1G34 (the 74AUP1G34 library entry is derived from it, same pinout) cached as 74xGxx:74AUP1G34; that adds one lib_symbol_mismatch warning.
5. **[done] R21 0R 0402 DNP bypass of R11** (UNI-ROYAL 0402WGF0000TCE, **C17168**): pin 1 on ANT (L8.2 / C13.1 / R11.5), pin 2 on the chip-antenna side. That side (R11.3 / C12.1, was Net-(R11-RF1)) is now named **ANT_CHIP**. Zero-current fallback: remove R11, fit R21. Commit 3311f91.
6. **[done] R8 fixed 10k -> 10k NTC**: Murata **NCP15XH103F03RC** 0402 (**C77131**, 304k in stock). Murata NCP15 table: 10 kΩ ±1 %, B25/50 3380 K ±1 %, B25/85 3434 K (pdftotext shifted the table one row; read against the JLC listing "10kΩ 3380K 3434K 3455K ±1%"). PS Monitor battery temperature, Table 2: "10 kΩ: B25/50 3380 K; B25/85 3434/3435 K", 1 % R and 1 % B. "If a capacitor is placed in parallel with the thermistor, the max capacitance is 100 pF": nothing else is on the NTC net. Footprint unchanged (0402); the symbol is still the EasyEDA resistor. Stage 2: place next to U4. Firmware: configure the 10k thermistor in the charger (the S5 alternative "BCHGDISABLESET" is no longer needed). Commit cbb58b8.
7. **[done] R19 (10k SENS_ID pull-up) top end VDDIO -> VSENS.** Firmware reads SENS_ID only with VSENS on. Commit 52d6c95.
8. **[done] USB-C ESD.** Commit dd6da97.
   - **D1 (CC1), D2 (CC2): TI TPD1E10B06DPYR**, X1SON 0.6 x 1 mm (**C48260**, 303k in stock). SLLSEB1G: "VRWM 5.5 V", "ILEAK 100 nA (pin 1 = 5 V)", "VBR 6 V min at 1 mA", "Vclamp 10 V at IPP 1 A / 14 V at IPP 5 A (8/20 µs)", "CIO 12 pF (VIO 2.5 V)", IEC 61000-4-2 ±30 kV contact. Why: the CC pins see at most the source's Rp level (≤ 5.5 V) and the nPM1300 CC abs max is 5.5 V, so a 5.5 V standoff never conducts in normal use; 100 nA leakage is negligible against the 5.1 kΩ Rd; this board does no USB PD signalling on CC, so 12 pF is not a concern. Bidirectional, so orientation doesn't matter.
   - **D3 (VBUS): Littelfuse SMF12A**, SOD-123FL, unidirectional, cathode to VBUS (**C207255**, 8k in stock). Littelfuse SMF table: "SMF12A | VBR 13.30-14.70 V at 1 mA | VR 12 V | IR 2.5 µA | Ipp 10.1 A | VC 19.9 V" (10/1000 µs), 200 W, "maximum height of 1.1mm". Why: it does not conduct at the 5.5 V VBUSOVP or with a non-compliant 9 V / 12 V source (the nPM1300 then just disconnects SYSREG), and it clamps below the 22 V VBUS absolute maximum at its full rated pulse. The lower SMF parts were rejected: SMF5.0A IR 400 µA at 5 V, SMF6.5A 250 µA.
9. **[done] C11 (2.2 pF on DECA) DNP**, pads kept. **C44 10 µF -> 4.7 µF**, same 0805 footprint: Samsung CL21A475KAQNNNE 25 V X5R (**C1779**, basic). VBUS total is now C44 4.7 + C4 1 + C51 1 + C14 0.1 = 6.8 µF nominal (USB 2.0 7.2.4.1 limit 10 µF, per the review). Commit 2f5a89f.
10. **[done] Decoupling.** **C49, C50 100 nF 0201** on VDDIO for U6 pins 22 and 36 (Samsung CL03A104KQ3NNNC 6.3 V X5R, **C160831**, 206k in stock): nRF54L15 PS config 1 Figure 1 lists C4, C7, C8 "100 nF 0201" and C10 "100 nF 0201 Optional" (which pin each sits on is in the image only). **C51 1 µF 0402 25 V** on VBUS for U2 pin 21 (Samsung CL05A105KA5NQNC, **C52923**, basic): nPM1300 config 1 BOM "C1, C5 | 1.0 μF | Capacitor, X5R, 10 V, ±10% | 0603"; in the config 2 figure C1 1.0 µF sits next to the VBUSIN label. 25 V chosen because VBUS abs max is 22 V. Note: C4 (1 µF 0402) is already on VBUS but about 8 mm from pin 21; stage 2 can drop C4 or keep both. Commit 692fbaa.
11. **[done] X2 32.768 kHz DNP** between U6.1 P1.00/XL1 and U6.2 P1.01/XL2 (new nets XL1, XL2; their NC flags removed). Epson FC-12M **X1A0000610008** 2.0 x 1.2 mm, CL 9 pF, 90 kΩ, ±20 ppm per the JLC listing (**C96341**, 24k in stock). nRF54L15 PS config 1: "X1 32.768 kHz, XTAL_2012". **No load caps added:** PS LFXO: "The device can be used with external capacitors C1 and C2 or the built-in configurable internal capacitors CINT", "CAPACITANCE is the desired capacitor value in pF, holding any value between 3 pF and 18 pF in 0.65 pF steps" (OSCILLATORS.XOSC32KI.INTCAP). Not checked: whether 9 pF CL maps into that INTCAP range (the CL formula is an image); check before fitting. Commit ee018f2.
12. **[done] Pi pads for the AE1 match.** Johanson 2450AT18A100 note: "It is recommended that the designer leave available slots for a "pi" (or shunt-series-shunt) network. The antenna matching network values here are used when antenna is mounted on Johanson's evaluation board. The matching values and topology on clinet's [sic] PCB will be different." Added two DNP 0201 shunt pads to GND (value "DNP", C or L at tuning, no LCSC number until a value is chosen): **C52 at the switch end** (net ANT_CHIP: R11.3 / C12.1 / R21.2) and **C53 at the antenna end** (L3.1 / AE1.1, net now named **ANT_FEED**, was Net-(AE1-ANT)). With the existing C12 (series 1.0 pF), L2 (shunt 2.7 nH) and L3 (series 3.9 nH) this allows: the present T; pi = C52 shunt / C12 series / L2 shunt with L3 = 0R; or pi = C52 shunt / C12+L3 series / C53 shunt with L2 removed. Stage 2: C52 right at C12 pad 1, C53 at L3 pad 1 outside the AE1 keep-out (the keep-out allows only AE1's own pads and the feed line). Commit 5b7bd74.
13. **[done] Polyfuse F1 on CN1.13**: VBAT -> F1 -> new net **VBAT_CN1** -> CN1.13. **Bourns MF-FSMF020X-2** 0603 (**C210356**, 17.8k in stock). MF-FSMF table (pdftotext rows shifted, read by column): "MF-FSMF020X | Vmax 9 V | Imax 40 A | Ihold 0.20 A | Itrip 0.50 A | RMin 0.550 Ω | R1Max 3.500 Ω | 1.00 A trip in 0.60 s"; thermal derating Ihold 0.17 A at 40 °C, 0.12 A at 60 °C. Commit 6590e8f.
   - Load: no sensor board draws from CN1.13 VBAT today (template STATUS: "unused on the sensor boards today"). Worst planned: the VBAT-fed isolated supply option (c), "VBAT current at EC load is about 70 mA" (feather_sensor_template\isolated_supply_options.md); feather_water_level's sensor is 8 mA average (DFRobot), peak unverified.
   - Choice: 0.20 A hold covers 70 mA with 2.9x margin at 23 °C and 1.7x at 60 °C; 0.50 A trip equals the CN1 contact rating (500 mA, LCSC/JLC listing of Molex 503480-1400, C505360; Molex page not reached). The next size up (MF-FSMF035X, Itrip 0.75 A) trips above the connector rating.
   - Cost: 0.55-3.5 Ω in series is 40-245 mV at 70 mA. If option (c) is adopted, check its VBAT >= 3.3 V margin with this drop, or fit a 0R in F1's place.
14. **[done] ERC, PCB update, DRC.** Commit ae98daa.
   - **ERC** (kicad-cli 10.0.4): **0 errors, 208 warnings** (80 pin_to_pin, 57 lib_symbol_issues, 55 footprint_link_issues, 6 lib_symbol_mismatch, 5 off-grid, 3 same local/global label, 2 multiple net names). +4 against run 4: 3 pin_to_pin (EasyEDA "unspecified" pins on L3/L8/R11/AE1 meeting the new passive pins, same class as before) and 1 lib_symbol_mismatch (U7, item 4).
   - **PCB update** with pcbnew Python from the kicad-cli netlist: 16 new footprints (C46-C53, D1-D3, F1, R20, R21, U7, X2) placed below the outline (y 137 and 141.5, x 93-137). Values, fields and DNP flags synced (R1, R2, C11, R20, R21, X2, C52, C53 DNP). Nothing was removed. Checked against HEAD: no existing footprint moved and the track/via geometry is identical (946 items); only the copper of the two nets renamed as a whole changed net (Net-(R11-RF1) -> ANT_CHIP, 3 items; Net-(AE1-ANT) -> ANT_FEED, 1 item). The .kicad_pcb text diff is large because pcbnew re-serialised the file.
   - **Split nets, copper left for stage 2** (old-net tracks still touch pads that moved to a new net): R19.1 (VDDIO track, pad now VSENS), R11.4 and C15.2 (VOUT1 tracks, pads now VRF), R11.6 (ANT_SEL track, pad now ANT_VCTL), CN1.13 (VBAT track, pad now VBAT_CN1).
   - **DRC** (kicad-cli 10.0.4, --schematic-parity, no refill): **18 errors, 327 warnings, 38 unconnected, 0 parity.** Errors: 4 hole_clearance in J1 (accepted, as before) and 7 shorting_items + 7 solder_mask_bridge, all on the split-net pads above (removing those track stubs is stage 2 routing). Warnings unchanged in type and count. Unconnected by net: GND 13, VRF 6, VDDIO 3, ANT_CHIP 2, ANT_SEL 2, VBUS 2, and 1 each on ANT, ANT_FEED, ANT_VCTL, CC1, CC2, VBAT, VBAT_CN1, VSENS, XL1, XL2.
   - No STEP export: the outline and connectors did not change, and the new parts are off the board.

All new parts are 1.1 mm or lower (SMF12A 1.1 mm max per Littelfuse; SC70-5 and the passives lower), so the Tidemark 1.6 mm limit (SW1 height) from fx 26 mm to the antenna end holds wherever they land. AE1 and its keep-out were not touched.

### Stage 2 to-do (placement and routing; U6 RF corner on Fable)
1. Route the split nets: cut the old stubs at R19.1, R11.4/C15.2, R11.6 and CN1.13 and connect them to VSENS, VRF, ANT_VCTL and F1.
2. Place and route the new parts: C46 at U2.31 and the VRF run to R11 with C47/C15 at R11.4; U7 + C48 (+ R20 pads) near R11; R21 bypass pads beside R11; C52/C53 on the match line; D1/D2/D3 at J1; C51 at U2.21; C49/C50 at U6.22/U6.36; X2 above U6 only if it fits; F1 next to CN1.13; R8 (NTC) next to U4.
3. The U6 RF corner (B1, B2, S2) per Nordic config 1, as planned.
4. Firmware notes for firmware-dev: LDSW2 in LDO mode at 2.5 V (LDSW2LDOSEL, LDSW2VOUTSEL), on before radio TX/RX, off after, and the switch needs about 10 µs after power-up (review decision); drive P0.01 before VRF turns on; never enable BUCK1; configure the 10k B3380 NTC; read SENS_ID only with VSENS on.

### Open questions from run 5 stage 1
- Unused BUCK1 pin handling is not in the nPM1300 PS text. Keep L9/C18 (current state) or ask Nordic, then remove them?
- C4 and C51 are both 1 µF on VBUS: drop C4 in stage 2?
- X2 CL 9 pF vs the LFXO INTCAP range (3-18 pF "CAPACITANCE"): confirm before fitting.
- The library copies of the nPM1300 symbol (pin 31 now power_out in the schematic) and of the EasyEDA symbols reused for R8/R9/C44 (their lib_id names still read the old MPNs) are not updated.

## Current state (before the rework, 2026-10-23)
- Schematic: 9 sub-sheets.
- PCB: rectangular outline, about 66.04 x 25.40 mm. 4 layers (F.Cu / In1.Cu / In2.Cu / B.Cu). 64 footprints, 831 track segments, 213 vias, 13 zones. **No mounting holes yet.**
- ERC (kicad-cli 10.0, 2026-10-23): 8 errors, 116 warnings.
  - USB-C J1 pins A6/A7/A8/B6/B7/B8 (D+/D-/SBU) are unconnected.
  - U2 VOUT2 is tied to a PWR_FLAG (#FLG04), which gives a power output to power output error.
  - C4 pin 1 has no power driver.
  - Warnings: 78 pin_to_pin, 13 lib_symbol_mismatch, 12 lib_symbol_issues, 5 off-grid.
- DRC (kicad-cli 10.0, schematic parity on, 2026-10-23): 0 errors, 323 warnings, 0 unconnected items, 0 parity issues.
  - Mostly silkscreen: 199 overlap, 85 over copper, 14 edge clearance.
  - 15 lib_footprint_mismatch and 5 dangling tracks.
  - Two GND vias are co-located or too close (0.237 mm, minimum 0.2495 mm).
- Carried over from v4 (netlist checked 2026-10-23):
  - Solar fix: AEM10330 pin 39 EN_SLEEP to GND; pin 11 to GND and pin 12 to VINT, which sets MPPT to 70 %.
  - CN1 pinout matches v4 and sens1 pin for pin: GND, VSENS, SDA, SCL, SCK, MOSI, MISO, CS, INT, AIN, ID, GND, VBAT, GND.
- Fab outputs: Gerbers (4-layer), drill file, PCBWay BOM (nrf54l15_feather_BOM_PCBWay.xlsx) and nrf54l15_feather.7z are in the project folder. I couldn't tell whether they match the current PCB.
- Enclosure / STEP: there's a vendor STEP for the 503480-1400 connector (5034801400_0.stp). No board STEP is in C:\Personal-Agents\shared\handoff\ yet.

## Open work
- **Feather-size rework (study done 2026-10-24, waiting on Brian).** Full write-up: feather-size-study.md. Baseline tag: `feather-pre-resize`.
  - The board has no Feather headers or pinout yet; only the USB-C position matches.
  - Standard 50.8 x 22.86 mm fits on area, but the edges run out: no edge left for CN1, U5 or J3.
  - Options: (a) true Feather, drop CN1, about 3 to 4 days; (b) Feather outline with connectors on the bottom, not recommended; (c) Feather headers and holes on a longer board (22.86 x about 60 to 66 mm), about 2 to 3 days.
  - Every option is a full re-place and re-route.
- Add four mounting holes (in progress, per CLAUDE.md). Hole positions depend on the Feather-size decision; the Feather spec uses M2.5.
- Check SENS_MISO: it's on two U6 pins (pad 11 and pad 15). Possible schematic bug.
- Check the AE1 keepout (3.1 x 5.9 mm now) against the 2450AT18A100E datasheet ground clearance before the antenna moves.
- Clear the ERC errors above, or document why they're acceptable.
- Fix the co-located or too-close GND vias and the dangling tracks.
- Export a board STEP for fusion-enclosure once the holes are placed.
- Solar review items carried over from v4 (solar-analysis-v4.md):
  - Check C41/C42/C43 capacitance under DC bias.
  - Check the L11 (DFE252010F-100M) land pattern against Murata's recommendation.
  - Check the layout against AEM10330 DS §10.
  - Do these before fab.

## Questions for Brian
- (closed 2026-10-24) Feather size: standard outline, keep all connectors, Proposal C (see Decisions).
- (closed 2026-10-24) USB is charge-only; D+/D-/SBU now carry no-connect flags.
- Is moisture_sensor.kicad_sch meant to be empty?
- Do the Gerbers and the 7z in the folder match the current layout, or are they from an earlier revision? Was this revision ordered?

## Decisions
- 2026-10-23 (Brian): this is the active main board. Feather form factor replaces v4.
- From v4: EN_SLEEP to GND, MPPT 70 %, and the CN1 14-pin Molex 503480-1400 pinout is fixed on the host.
- 2026-10-24 (Brian): resize to the standard Feather outline (50.8 x 22.86 mm, Feather mounting-hole positions) but **without the Feather header rows or pinout**. Keep every current connector: J1 USB-C, CN1, J3 SWD, U4 battery JST, U5 solar JST. Not FeatherWing-compatible. This is a variant of option (a) in feather-size-study.md and closes its questions 1-3, 5 and 6. Placement questions still open (see Questions for Brian).
- 2026-10-24 (Brian): connector layout is Proposal C (C:\Personal-Agents\shared\design\nrf54l15_feather\feather_connector_layouts.html). USB-C centred on one short edge; CN1 centred on the far short edge so the FFC folds straight down to sens1, which stacks underneath; U5 solar and U4 battery on opposite long edges near the USB end; the antenna moves to a long edge near the far end. RF risk accepted, to be minimised in layout.
- 2026-10-24 (Brian): **all parts on the top side**, including J3, U4 and U5, so the bottom is flat and sens1 can stack close underneath. The RF1 U.FL + R11 switch (ANT_SEL) is the fallback if the chip antenna's range suffers on the long edge. Defaults accepted: M2.5 holes (plated at the USB end, NPTH + nylon at the far end), USB stays charge-only, no fab output without approval.
- 2026-10-24 (Brian): SENS_MISO on two U6 pins (pad 11 and pad 15) is intentional, not a bug.
- 2026-10-25 (Brian): mounting holes use a 2.7 mm drill (M2.5 clearance) at the same Feather positions. Done in run 2: H1/H2 plated with a 3.4 mm pad, H3/H4 NPTH 2.7 mm. (The footprint names still read MountingHole_2.5mm*; only the pads changed.)
- 2026-10-25 (Brian): the plated USB-end holes H1/H2 are tied to GND (thermal-relief connection to the F.Cu/B.Cu pours and the In1 plane). H3/H4 stay NPTH and unconnected.
- 2026-10-25 (Brian): AE1 moved to the far corner with a ~6.5 x 6.5 mm no-ground area, per the Johanson datasheet/EVB (checked by coordinator). Done in run 2 step 1c; the pi-match values must be tuned on the real board.
