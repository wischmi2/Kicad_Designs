# nRF54L15 feather - Status

Project: C:\Personal-Agents\worktrees\nrf54l15-feather-branch\hardware\feather\nrf54l15_feather\nrf54l15_feather.kicad_pro
Last reviewed: 2026-10-28 night (run 9: 30 vias enlarged to a 0.15 mm annular ring for PCBWay, 22 to 0.6/0.3 and 8 to 0.55/0.25, min annular rule now 0.15; no via or part moved; DRC 0 errors / 0 unconnected / 0 parity; ERC 0 errors; STEP unchanged, 2026-10-28b)

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

## Run 5 stage 2 (2026-10-28, kicad-designer on Fable 5.1): RF corner and antenna-switch area
Scope was cut by the coordinator to stages 2.1 and 2.2 only (usage limit); stages 3-7 (power parts, split-net routing, VBUS/VBAT widths, silk, J1 rule, final checks, STEP) go to a separate run. Board edits with pcbnew Python (scratch scripts), every step checked with kicad-cli 10.0.4 DRC (--schematic-parity --refill-zones). Schematic not changed. Commits: 436e86a (2.1), see git log for 2.2.

Sources read today (2026-10-28):
- nRF54L15 PS, PCB layout example (ref_circuitry.html-layout): "The PCB layout in the following figure is a reference layout for Circuit configuration no. 1 for QFAA QFN48." "Note: Pay attention to how the capacitor C6 is grounded. It is not directly connected to the ground plane, but grounded via pin 32 and to the VSS die pad. This is done to create additional filtering of harmonic components." The five layout figures (Figures 3-7) are images served from docs.nordicsemi.com/api/khub; a plain download returned an HTML page, and a download with browser headers was blocked by the tool policy, so **I could not read the reference layout images**. The corner below is laid out from the QFN48 pin geometry, the config 1 figure labels (C4/C7/C8/C10 100 nF 0201, C6 GJM0335C1E1R5WB01, C9 GJM0335C1E2R0WB01, L2 LQP03HQ2N7B02, L3 LQP03HQ3N5B02, L4 = L3, X2 32 MHz XTAL_2016) and the grounding note.
- nRF54L15 PS, Reference circuitry: "To ensure good RF performance when designing PCBs, it is highly recommended to use the PCB layouts and component values provided by Nordic Semiconductor."
- nPM1300 PS, PCB guidelines: "The BUCK supply voltage should be decoupled with high performance capacitors as close as possible to the supply pins." "All device grounds, VDD connections, and VDD bypass capacitors must be connected as close as possible to the device." "Long power supply lines on the PCB should be avoided." The nPM1300 layout example page has only figure captions (Figures 7-11, QFN) and "Note: No components on the bottom layer."
- Johanson 2450AT18A100 datasheet (pdftotext of the PDF): "It is recommended that the designer leave available slots for a "pi" (or shunt-series-shunt) network. The antenna matching network values here are used when antenna is mounted on Johanson's evaluation board. The matching values and topology on clinet's PCB will be different." "* Line width should be designed to provide 50 ohm impedance matching characteristics." EVB: "6.5mm Antenna ... No Ground", "This 50 Feedline can be as short as needed".
- e-peas DS-AEM10330 v1.5 section 10.1: "Connection between VINT and CINT must be moderately short for AEM10330 stability, even though this pins does not carry large currents. Same for connection between CINT to GND." (for stage 3, C41).

### Stage 2.1 (commit 436e86a): U6 RF corner per config 1
What moved and why (all in board mm; Feather fx = x - 90, fy = 132.86 - y):
- **DECRF (U6.33) to DECA (U6.43)**: C1 (2.2 uF 0201) now sits 0.5 mm below pin 33 at (129.35,122.67) with its GND via at (128.9,123.6); the DECRF-DECA link is a 0.45/0.25 via at (129.36,121.85), a straight In2 track and a 0.5/0.3 via at (132.3,118.15) next to pin 43. C9 (10 nF) at (133.0,118.1) and C11 (DNP) at (133.65,118.02) sit on pin 43's F.Cu stub, which then runs on to L4.2 (the DECD ferrite). An F.Cu link is impossible: pins 34/35 (XC1/XC2) sit between pin 33 and the chip corner, so any F.Cu path would cross the crystal lines. SENS_CS (In2) and SENS_INT (B.Cu) were re-routed around the new link; the SENS_SCL via that Brian placed was not moved.
- **Match network**: L5, C8, L6, C5, L8 now sit in flow order down x 128.3 (rot -90, pad 1 upstream), nothing doubles back. C8's GND pad faces pin 32 and is tied to it with a 0.15 mm stub (pin 32 keeps its stub into the exposed pad), per the Nordic note. C5 (2.0 pF shunt) hangs 0.6 mm off the L6/L8 node to the left; its GND goes down the right side of C48 to the C48/C13 GND via (see 2.2).
- **X1**: rot 0 at (131.2,123.5). Pads 4/3 are the top row, 1/2 the bottom row; XC1 drops straight down x 129.85 into pad 1, XC2 goes right along y 121.75 and down into pad 3; no track between or under the pads; the X1.4 via-in-pad is gone (pad 4 has a 0.45 via at (130.5,122.25), pad 2 is tied to the C15/C53 GND via at (132.55,125.68)).
- **C50** (100 nF 0201) at (132.45,121.35) on pin 36 (1.97 mm), **C49** at (124.0,119.0) under C22 on pin 22 (1.34 mm). The pin-36 VDDIO now goes through a 0.45 via at (131.1,121.25) to In2 (y 122.75) and the pin-22 In2 run; the old pin 36 -> R19 F.Cu/In2 run is gone (R19 is on VSENS now).
- SENS_SDA moved from B.Cu to an F.Cu run along y 119.8 (pin 38 -> R15.2) to free the pin-36 via site; SENS_MOSI In2 moved to y 123.05; RESET F.Cu leaves pin 30 diagonally; GND via at C10.1 (135.23,114.1).
- Measurements (pad centre to pad centre along copper, own script; the verifier's figures used pad edges, hence 16.9 vs 17.8 before):

| Path | Before | After |
| --- | --- | --- |
| U6.33 DECRF -> nearest DECA cap (C1.1) | 17.79 mm, 2 vias | 1.57 mm, 0 vias |
| U6.33 -> U6.43 | 19.71 mm, 2 vias | 6.97 mm, 2 vias |
| C5.2 stub to L6.2 / L8.1 | 8.91 / 7.39 mm, 2 vias | 0.66 / 0.60 mm, 0 vias |
| XC1 U6.34 -> X1.1 | 2.24 mm, 0 vias | 3.86 mm, 0 vias |
| XC2 U6.35 -> X1.3 | 5.64 mm, 2 vias | 3.30 mm, 0 vias |
| U6.31 ANT -> L5.1 | 2.38 mm | 1.22 mm |
| C8.1 -> U6.32 (GND, via pin 32) | no copper path | 1.19 mm |
| U6.36 -> nearest VDDIO cap | 33.26 mm (C26), 3 vias | 1.97 mm (C50), 0 vias |
| U6.22 -> nearest VDDIO cap | 14.34 mm (C6), 2 vias | 1.34 mm (C49), 0 vias |

- DRC after 2.1: 14 errors (4 J1 hole clearance accepted, 5 shorting_items + 5 solder_mask_bridge on the stage-1 split-net stubs), 34 unconnected, 0 parity.

### Stage 2.2: antenna-switch area
- **U7** (SN74AUP1G34, SC70-5) at (124.99,124.9) rot 0, left of the match chain and above RF1: pin 5 VCC top-right, pin 4 Y bottom-right, pin 2 A middle-left, pin 3 GND bottom-left. **C48** (100 nF) at (127.0,124.8) rot -90, 1.18 mm from VCC. **R20** (1M DNP) at (122.5,125.9) left of U7, pad 1 on the ANT_SEL via, pad 2 to a GND via at (122.5,127.0).
- ANT_SEL: U6.24 -> existing via (125.442,120.604) -> B.Cu -> via (123.5,124.9) touching U7.A (6.69 mm, 2 vias). ANT_VCTL: U7.Y -> via (125.83,124.9) under the body -> B.Cu -> via (127.5,127.25) -> F.Cu to R11.6 (5.28 mm, 2 vias). The old ANT_SEL via at (127.483,126.42) is gone.
- **VRF**: U7 VCC via (126.0,123.5) sits on the VRF inner trunk. The trunk is the old VOUT1 In2 diagonal (124.443,121.102)->(129.313,125.972) and its via (124.054,121.102), re-netted to VRF and cut from VOUT1 at C18.2 (VOUT1 now has only U2.1, L9, C18, as the schematic says). The trunk continues on In2 to a via at (129.75,126.6) for C47/R11.4 and to a via at (131.75,125.1) for C15.2. **C47** (100 pF) at (129.75,125.75) rot 90, 1.30 mm from R11.4, GND via (130.1,125.3). **C15** (100 nF) at (131.7,125.8) rot 90, 5.1 mm / 2 vias from R11.4 (no F.Cu site next to pad 4: R21 and the ANT branch take the space). **The VRF trunk is still open between the via (124.054,121.102) and U2.31 (stage 3).**
- **R21** (0R DNP bypass) at (130.8,126.25) rot -90, right of R11: pad 1 ANT fed by a branch from the chain node L8.2 along y 124.75 (above X1), pad 2 ANT_CHIP from R11.3 along y 127.2. Fitting R21 (and removing R11) gives ANT -> 5.1 mm branch -> R21 -> 2.1 mm -> ANT_CHIP; both pads are open stubs when DNP (2.5 mm on ANT off the chain node, 1.3 mm on ANT_CHIP).
- **C13** (0.3 pF) nudged to (127.6,125.9) (0.2 mm down) to clear C48; its ANT stub re-drawn at y 125.9. C48.2, C13.2 and C5.1 share the GND via at (126.9,126.35).
- **C52** (DNP pi shunt) at (128.7,128.2) rot 90, pad 1 0.63 mm from C12.1, pad 2 on the GND via (128.6,127.84). **C53** at (131.75,127.4) rot 90, pad 1 0.94 mm from L3.1 (0.17 mm stub), outside the AE1 keep-out (pads end at x 131.98); its GND pad overlaps C15.1 and both go to the via at (132.55,125.68) together with X1.2. The keep-out rule area (x 132.15-140.8, y 126.4-132.86) and the ANT_FEED line are unchanged; no new track or via inside it.
- Stitching vias deleted in the area: (125.945,123.458), (126.572,124.21), (126.08,126.05), (126.62,125.75), (130.508,125.263), (130.571,126.551), (131.35,123.05), (132.84,119.61), (131.5,127.8), (131.9,125.15).
- Tidemark zone (fx >= 26, x >= 116): U7 SC70-5 is 1.1 mm max (TI), all the new passives 0201/0402/0603 are below 0.9 mm, so nothing new exceeds SW1's 1.6 mm. D3 (SMF, 1.1 mm), F1 (0603) and X2 are not placed yet.
- **DRC now (kicad-cli 10.0.4, --schematic-parity --refill-zones): 6 errors, 451 warnings, 17 unconnected, 0 parity.** Errors: 4 hole_clearance in J1 (accepted), 1 shorting_items + 1 solder_mask_bridge at CN1.13 (VBAT track still on the VBAT_CN1 pad; stage 5). Warnings: 199 silk_overlap, 194 silk_over_copper, 55 lib_footprint_issues, 2 silk_edge, 1 via_dangling (the VRF via (124.054,121.102), waiting for stage 3). Unconnected: VRF U2.31 -> trunk, VRF C46, VDDIO U2.30, VSENS R19.1, VBAT F1.1, VBAT_CN1 F1.2 -> CN1.13, VBUS D3/C51, CC1 D1, CC2 D2, XL1/XL2 X2, GND on the off-board parts (C46, C51, D1, D2, D3).
- ERC: not re-run (schematic unchanged since 1.14: 0 errors, 208 warnings).

### Hand-off for stages 3-7 (next run)
1. **VRF to U2.31**: the trunk ends at the via (124.054,121.102) (In2 west end (124.443,121.102)). Planned path, checked against the copper but not drawn: pin 31 (119.15,119.45) down x 119.1 to y 120.25, east along y 120.25 under pin 32 to x 120.66, down x 120.66 (0.11 mm from a VBAT via moved to (120.15,120.773) and 0.135 mm from C18.2) to y 122.06, east between C18's pads to x 122.52, up to y 121.15 and east along y 120.9 to the via. This needs: C19 moved to (120.5,123.75) rot 90 with its VBUSOUT via moved to (120.307,123.0) and the B.Cu lead re-drawn; C3 moved 0.3 mm down to (118.1,122.1) with its VBAT link re-drawn along y 121.4 to the VBAT via; the old C3 VBAT F.Cu (y 120.465) deleted. C46 (10 uF) fits at C15's old spot (123.2,121.6) rot 90 on that y 120.9 run (pad 1 GND reuses the via (122.568,123.394)); nothing closer to pin 31 fits.
2. **U2.30 (LSIN2, VDDIO)**: boxed by pins 29/31; route F.Cu (118.65,119.45)->(118.75,119.55)->(118.75,120.65)->(117.387,120.65) joining the pin-28 VDDIO drop (passes 0.15 mm right of the VSENS via (118.15,120.1); C3 must be at y >= 122.1 first). No via site exists under U2's bottom row: VSENS In2 (y 120.2) and VBAT In2 (y 120.65) forbid it (0.25 mm hole clearance).
3. **C51 at U2.21**: no 0402 site within 2 mm of pin 21 (VBUS/VBUSOUT/CC1/CC2 via column at x 114.62, VSYS drop x 114.05, VBAT drop x 113.02). Best found: (114.85,123.6) rot 0 with pad 1 on the VBUS via (114.15,123.3), about 6.5 mm by track; C4 (1 uF at (112,123.3)) is then redundant (report only).
4. **C41 to IC1.13**: site (110.55,117.2) rot 0 with pad 1 over the VINT via (110.564,117.29); move the /Solar/LOAD F.Cu jog to (111.95,117.55)->(111.589,117.911) first; GND via for pad 2 at about (110.3,118.0) after the NTC via (110.998,118.196) is removed (R8 moves).
5. **D1/D2/D3 at J1**: CC1 pad A5 (97.79,120.18) has F.Cu to R2 at (104,120.4); CC2 pad B5 (97.79,123.18) to R1; VBUS runs along y 123.845 from (97.8,123.85) to C44. Space right of J1 (x 98.5-103.5, y 118-125) holds only those tracks and GND vias at (98.813,117.639)/(98.813,125.22).
6. **F1 at CN1.13**: C9's old site is free: x 134.5-136.3, y 117.8-119.4 (SDA F.Cu at x 136.46, GND via (134.65,118.75)). CN1.13 fan-out track runs east from the pad to (138.8,118.68) (VBAT net, to be cut/renamed).
7. **R8 (NTC) near U4**: site (104.6,124.2) rot 90 clear of U4/J3/C44/R1 courtyards. The NTC net ends at the via (110.998,118.196)/In2 (113.5,115.7)->(111.0,118.2); the In2 CC1/CC2 diagonals (105.9-114.4, y 118.7/119.2) and the SHPHLD B.Cu wall at x 111.65 (y 117-127.2) block a direct west route; B.Cu along y >= 127.3 under J3 is the likely path.
8. **X2**: the area above U6 pins 1/2 (x 129-132, y 112.3-114.5) holds the I2C_SCL via (129.85,113.7), I2C_SDA via (129.161,114.067), SENS_AIN via (130.75,113.5) and F.Cu, SENS_ID F.Cu/via (131.166,112.924) and the VDDIO F.Cu at y 112.41; X2's courtyard is 3.09 x 2.29 mm. It does not fit "without moving more than a cap or two": delete X2 from the PCB and note it (the DNP symbol then shows as 1 parity issue unless Brian sets "exclude from board").
9. **Stage 5 routing**: VSENS R19.1 (the VDDIO stub is gone; R19.1 at (129.97,131.3) needs VSENS from the R17/R18 group, SENS_ID B.Cu via (130.95,130.3) is next to it); CN1.13 VBAT_CN1 via F1; VBUS/VBAT widening (VBAT In2 still y 120.651 / diagonal (124.367,120.564)->(128.292,124.489) / y 124.489, 0.25 mm; note vias in the U2-bottom and crystal areas were placed to its current position).
10. Stages 6-7 as in the task (silk 1.0/0.15, J1 .kicad_dru rule, ERC/DRC, STEP, STATUS).

## Run 5 stage 3 (2026-10-28, kicad-designer on Opus): power parts, USB protection, routing, silk, final checks
Board edits with pcbnew Python (scratch scripts), each step checked with kicad-cli 10.0.4 DRC (--schematic-parity --refill-zones). The RF corner and antenna-switch area from stage 2 were not moved or re-routed; the only touch is the VRF trunk joined at its west via (124.054,121.102), as planned. Schematic: only X2's "exclude from board" flag. No new parts, so no LCSC checks were needed. Commits: 2ab0dfe (3.1), f90f68a (3.2), 4668e84 (3.3), 0fb7bb5 (3.4), a48caf0 (3.5), e9a0d10 (3.6), then this file (3.7).

### 3.1 Power parts (2ab0dfe)
- **VRF U2.31 -> trunk, with C46.** Hand-off path used: pin 31 down x 119.15 to y 120.25, east to x 120.66, down to y 122.06, east between C18's pads, up x 122.505 to y 121.15, along y 120.9 through C46.1 to the trunk via (124.054,121.102).
  - U2.31 -> C46.1 is about 7.7 mm of 0.2 mm F.Cu. The x 122.505 piece is 0.18 mm wide for 0.9 mm, between C18.2 and C46.2. Nothing closer to pin 31 fits.
  - **C46** (10 uF 0603) at (123.18,121.6) rot 270, GND to the via (122.568,123.394).
  - Done as planned: C3 moved 0.3 mm down to (118.1,122.1). Its VBAT link was redrawn along y 121.4 (0.5 mm) to the VBAT via, which moved from (120.275,120.773) to (120.15,120.773). The old C3 VBAT F.Cu (y 120.465) was deleted. C19 moved to (120.5,123.75) rot 90.
  - **Deviation:** the hand-off missed the VOUT1 track at x 120.918 (the L9.2 -> C18.2 drop plus diagonal). It was 0.06 mm from the planned VRF run, so I redrew it as a direct 0.3 mm link (121.7,119.85)-(121.6,121.06). The pin-1 stub stays.
  - **Deviation:** the planned C19 VBUSOUT via site (120.307,123.0) shorts the SWDIO In2 track (y 122.763) and the VDDIO B.Cu diagonal. I put the via (0.45/0.25) at (119.1,122.25) instead, where the existing B.Cu lead ends, plus an F.Cu link to C19.2.
  - C46 is at x 123.18, not 123.2, to keep hole clearance to the SWDIO via (124.07,122.527).
- **U2.30 LSIN2 -> VDDIO**: as in the hand-off, (118.65,119.45) -> (118.75,119.55) -> (118.75,120.65) -> (117.387,120.65), onto the pin-28 VDDIO drop.
- **C51 at U2.21**: placed at the hand-off site (114.85,123.6) rot 0.
  - Pad 1 sits on the VBUS via (114.15,123.3); the via is half on the pad edge and tented.
  - Pad 2 goes to the GND track at x 114.9 and the GND via (115.105,124.255).
  - U2.21 -> C51 is about 6.5 mm: pin, via (114.62,117.3), 0.5 mm B.Cu, via.
  - **C4 is now redundant (report only, not deleted).** C4 (1 uF at (112,123.3)) is on the same VBUS node, 2.3 mm further from that via. It adds bulk but no local decoupling. VBUS total is 4.7 + 1 + 1 + 0.1 = 6.8 uF.
- **C41 at IC1.13 (VINT). Deviation:** the hand-off site (110.55,117.2) rot 0 overlaps the IC1 and C43 courtyards (DRC errors). It would also put the VINT via between the two pads, touching the GND pad.
  - Placed at (110.75,118.4) rot 270, below pin 13. Pad 1 is 0.6 mm from the VINT via (110.564,117.29). Pin 13 -> C41.1 is about 1.4 mm (was 9 mm through 2 vias).
  - Pad 2 goes to a new GND via (110.75,119.75, 0.45/0.25) and is also tied to C43.2.
  - To make room, **C43 moved 0.6 mm left to (109.0,119.71)** and its tracks were redrawn.
  - The old C41 tracks at IC1.29/30 were removed. Pins 29/30 (STO_PRIO, T_MPP[0]) stay on VINT through the In2 link.
- **R8 (NTC) next to U4. Deviation:** the hand-off site (104.6,124.2) rot 90 puts pad 1 on the VBUS track (y 123.845).
  - Placed at (103.6,124.5) rot 0, between VBUS and U4, about 1.9 mm from U4's body. R8.1 (GND) goes to U4.2.
  - NTC route: the old NTC via (110.998,118.196) collided with C41 and was removed. In2 now runs west along y 118.2 to a new via (106.0,118.2), then B.Cu down x 106.0 to a via (104.85,124.7), then F.Cu to R8.2.
  - U2.18 -> R8 is about 18 mm. Nothing else is on the NTC net (PS limit: 100 pF in parallel).

### 3.2 USB protection, CN1, VSENS (f90f68a)
- **D1 (CC1)** at (101.0,119.68) rot 90, pad 1 on the CC1 track (y 120.03), GND via (101.0,118.65). It is about 3.3 mm from J1 A5.
- **D2 (CC2)** at (99.8,120.8) rot 90, pad 1 on CC2 (y 121.15), GND via (100.55,120.58). It is about 2.0 mm from B5.
- **D3 (VBUS)** at (101.0,122.7) rot 0, about 1.8 mm from B4A9. Pad 1 joins the VBUS track (y 123.845) with a 0.5 mm stub. Pad 2 goes to the R1 GND via (103.416,123.032) with 0.4 mm.
- **CC2 re-routed** to make room for D3: from B5 straight up x 98.766 to y 121.15, east to 101.5, then back to y 121.588 into R1. The old diagonal was removed.
- **F1 NOT placed (blocked; stopped after 3 approaches).** The courtyard (3.06 x 1.56 mm, KiCad Fuse_0603) does not fit anywhere next to CN1.13:
  - **C9's old site (the hand-off pick):** only the pads fit. The courtyard hits C11/C9/CN1 at rot 0 and R15/CN1 at rot 90. The pads also hit the DECA trace C9 -> L4.2 (frozen) and SENS_SDA at x 136.46.
  - **Above CN1:** the band below H3 is 1.4 mm high and blocked by the H3 courtyard circle.
  - **Below CN1:** this is the AE1 keep-out.
  - **Fit scan of the right half** (pads clear of all copper, courtyard clear of all courtyards): the nearest legal site is (134.6,112.5) rot 90. That is 6.7 mm from CN1.13, and both of its routes would cross the SENS_* B.Cu/In2 bundle. Nothing along the VBAT In2 branch (x 120-140) is legal either.
  - **What was done:** the CN1.13 VBAT stub was cut, which clears the shorting_items and solder_mask_bridge errors. **CN1.13 is unpowered** until F1 is resolved.
  - The VBAT In2 branch (via (120.15,120.773) ... via (138.8,118.68)) stays in place for the fix and gives 1 via_dangling warning.
  - F1 stays below the outline at (104,141.5) and is left out of the STEP.
  - Options are in Questions for Brian.
- **VSENS -> R19.1:** route, about 10 mm at 0.2 mm:
  - F.Cu from R17.1 to a via at (133.2,125.6).
  - B.Cu to (132.9,125.25), then west along y 124.5 (under X1, beside the SENS_INT B.Cu) to x 130.95.
  - Down x 130.6/130.45, between the VRF/GND vias and the SENS_ID B.Cu, to (129.6,129.2).
  - Via at (129.5,130.6), then F.Cu to R19.1.
  - Both vias are outside the AE1 keep-out. No stage-2 part, track or via was moved. It is a new B.Cu track under the antenna-switch area, with In1 GND in between.

### 3.3 X2 (4668e84)
- X2 deleted from the PCB. In nrf54l15.kicad_sch the symbol is now `(on_board no)` ("exclude from board"), with DNP kept, so **parity is 0**.
- U6.1/U6.2 (XL1/XL2) are single-pad nets. Fitting X2 later needs a re-route above U6 pins 1/2 (stage 2 hand-off, item 8).

### 3.4 Routing and VBUS/VBAT widths (0fb7bb5)
- Unconnected: 2, both F1 (F1.1 VBAT, F1.2 -> CN1.13 VBAT_CN1). Everything else is routed.
- Widening used a clearance script (0.1 mm copper, 0.25 mm hole, 0.5 mm edge), segment by segment.
  - Around C44.1 the VBUS run now jogs to y 124.05 to stay at 0.5 mm.
  - The NTC via moved from (104.8,124.5) to (104.85,124.7) to allow this.
- **VBUS** (J1 -> U2.21) is mostly 0.5 mm. The narrower parts:

| Section | Width | Length |
| --- | --- | --- |
| Inside J1's pad field (top VBUS pad) | 0.3 mm | 0.64 mm |
| Inside J1's pad field | 0.35 mm | 0.5 mm |
| C44 -> C4 (y 122.943) | 0.35 mm | 3.54 mm |
| **B.Cu (114.62,117.3) -> (113.95,117.65), at the U2 via column (narrowest)** | **0.25 mm** | **0.81 mm** |

- **VBAT** (U4 -> U2.19):
  - In2 runs 0.5 mm to the C43 via (x 108.289), 0.4 mm to the U2 via (x 113.024), then 0.3 mm to the C3 via (x 120.15).
  - **The F.Cu riser from the via (113.024,120.523) to U2.19 stays 0.25 mm, about 6.6 mm in total.** Its longest segment is x 113.024 (3.42 mm), pinched by C42's pads. The feed into pin 19 along y 116.25 is 1.95 mm.
  - Estimated resistance is 13 mOhm at 1 oz, about 4 mV at 300 mA. So the 300 mA firmware cap on charge and input current is a choice, not a copper limit.
  - C3 and C43 VBAT links are 0.5 mm. The dangling CN1 branch is 0.25-0.3 mm.

### 3.5 Silk and the J1 rule (a48caf0)
- All visible reference designators are now 1.0 mm / 0.15 mm.
  - A script moved each one to the nearest spot within about 1.3 mm of its courtyard that clears every pad (0.1 mm) and every other reference. R1, R2, R17 and R18 were placed by hand.
  - Hidden, like the neighbouring stage-2 parts, because they sit in dense clusters: C8, C46, C47, C48, C49, C50, C52, C53, R20, R21, U7, X1. F1 is hidden because it is off the board.
  - 33 references stay visible.
  - Silk warnings caused by reference text dropped from about 180 to about 38. The remaining 167 silk_over_copper and 199 silk_overlap come from footprint graphics and were there before.
- **J1 exception:** new `nrf54l15_feather.kicad_dru` with the rule "J1_NPTH_to_pad": hole_clearance min 0.18 mm, applied only when both items belong to J1. The actual values from the vendor land pattern are 0.185 mm (A1B12, B1A12) and 0.217 mm (A4B9, B4A9). **Accepted exception**; see Decisions.

### 3.6 Final checks (e9a0d10)
- Zones refilled with pcbnew ZONE_FILLER and saved.
- **DRC** (kicad-cli 10.0.4, --schematic-parity, run both with and without --refill-zones): **0 errors, 424 warnings, 2 unconnected, 0 parity.**
  - Warnings: 199 silk_overlap, 167 silk_over_copper, 55 lib_footprint_issues, 2 silk_edge_clearance, 1 via_dangling (the end of the CN1 VBAT branch at (138.8,118.68)).
  - Unconnected: F1.1 VBAT, F1.2 -> CN1.13.
- **ERC** (kicad-cli 10.0.4): **1 error, 208 warnings.**
  - The error is power_pin_not_driven on C4 pin 1 (npm1300 sheet). It is the same at HEAD 0787191 (checked with X2's flag reverted). It is the "C4 pin 1 has no power driver" item from 2026-10-23, so stage 1's "0 errors" did not reproduce.
  - Not fixed: the only schematic edit allowed was X2's flag.
  - Warnings, unchanged by type: 80 pin_to_pin, 57 lib_symbol_issues, 55 footprint_link_issues, 6 lib_symbol_mismatch, 5 endpoint_off_grid, 3 same_local_global_label, 2 multiple_net_names.
- **STEP:** C:\Personal-Agents\shared\handoff\nrf54l15_feather\nrf54l15_feather_2026-10-28.step.
  - F1 is left out with --component-filter because it is off the board.
  - The outline and connectors have not changed since 2026-10-26.
- **Tidemark zone (fx >= 26, x >= 116):** the only new or moved parts there are:

| Part | Package | Height |
| --- | --- | --- |
| C46 | 0603 MLCC | nominal 0.8 mm (datasheet not opened) |
| C19 | 0402 | under 1.6 mm |
| C3 | 0603, moved 0.3 mm | under 1.6 mm |

  - All are well under SW1's 1.6 mm.
  - D1, D2, D3 (SMF12A, 1.1 mm max), C51, C41 and R8 are all at x < 116. F1 is not placed.

### Not done / next
1. [done 2026-10-28 evening] **F1** placed and routed by Brian; see "F1 placed" below.
2. C4: keep or remove? It is redundant with C51 at the same node.
3. ERC power_pin_not_driven on C4 pin 1 (EasyEDA C0402 symbol pin type, or add a PWR_FLAG). This needs a schematic edit.
4. Before fab, a design review of the stage 2/3 layout: VRF 7.7 mm to C46, the 18 mm NTC run, and the VSENS B.Cu under the switch area. Also the footprints and the EasyEDA 3D models.

### Open questions from run 5 stage 1
- Unused BUCK1 pin handling is not in the nPM1300 PS text. Keep L9/C18 (current state) or ask Nordic, then remove them?
- C4 and C51 are both 1 µF on VBUS: drop C4 in stage 2?
- X2 CL 9 pF vs the LFXO INTCAP range (3-18 pF "CAPACITANCE"): confirm before fitting.
- The library copies of the nPM1300 symbol (pin 31 now power_out in the schematic) and of the EasyEDA symbols reused for R8/R9/C44 (their lib_id names still read the old MPNs) are not updated.

## F1 placed (2026-10-28 evening, Brian + coordinator)
- Brian placed F1 (Bourns MF-FSMF020X, 0603, C210356, same part as the schematic) at (130.23, 111.37) on F.Cu and routed VBAT -> F1.1, F1.2 -> VBAT_CN1 -> CN1.13. Commit 37d3a6f.
- Coordinator removed an old VBAT stub that ended nowhere, about 8.6 mm: 3 B.Cu segments from the branch point (120.15, 120.77), via (118.51, 124.36), 4 F.Cu segments to (114.25, 127.7). Each removal was checked with DRC so nothing connected was cut.
- **DRC** (kicad-cli 10.0.4, --schematic-parity --refill-zones): **0 errors, 424 warnings, 0 unconnected, 0 parity.** Warnings are the same set as stage 3.6: 199 silk_overlap, 167 silk_over_copper, 55 lib_footprint_issues, 2 silk_edge_clearance, 1 via_dangling (VBAT via at (138.8, 118.68), the old CN1.13 fan-out end).
- Then the coordinator removed that via (it only dropped onto an In2 VBAT track that runs straight through, so no track was left dangling). DRC now: **0 errors, 423 warnings (no dangling items), 0 unconnected, 0 parity.** STEP not re-exported for a via removal.
- ERC not re-run (no schematic change).
- **STEP:** C:\Personal-Agents\shared\handoff\nrf54l15_feather\nrf54l15_feather_2026-10-28b.step, with F1 on the board. Outline and connectors unchanged, so no new enclosure handoff. F1 is in the Tidemark zone (x >= 116) but a 0603 PTC is well under SW1's 1.6 mm.

## Pre-fab review (2026-10-28 evening, design-reviewer on Opus, HEAD c4b617e)
Full report: C:\Personal-Agents\shared\reports\2026-10-28-review-nrf54l15-feather-prefab.md. Verdict: **not ready for fab, close.** B1, B3, B4 fixed; B2 fixed except C5's ground (S1); B5 open.
- **Blockers:** BL1 old 10-23 Gerbers/drill/7z/PCBWay BOM still in the project folder (66.04 x 25.40 outline) - archive and regenerate. BL2 BOM not ready for JLC assembly: LCSC split over "LCSC" and "LCSC Part" fields; 15 fitted parts have none (C40-C43, C45, CN1, IC1, J1, J3, L7, R15, R16, SW1, U2, U6; numbers are in parts_2026-10-27.md); U2, IC1 and C43 had 0 JLC stock on 10-27 (C43 alt C412252).
- **Should fix:** S1 C5 shunt ground shares a via with C48/C13 through ~3.2 mm of 0.15 mm track (~1.1 nH), needs its own via (move VRF/VBAT In2 ~0.5 mm near (126.9,123.6)). S2 no local cap at U2.28/U2.30 (LDO inputs); add 1-10 uF. S3 U2.32 VOUT2 reaches L10 via 17.8 mm / 3 vias. S4 R21 DNP pads leave a 3.3 mm stub on ANT (~0.4 pF). S5 F1 branch 0.15 mm; widen to >= 0.3 mm, In2 piece (x 139.2, y 115.7-117.9) first. S6 R17 reference on AE1 pad 1. S7 order JLC04161H-3313 + ENIG, BOM/CPL with --exclude-dnp, MPN fixes (C41, J3, IC1, J1).
- **Notes:** F1 drop 55-260 mV at 70 mA (too much for VBAT-fed isolated supply option (c), fine for water level). VRF always on adds 50-90 uA sleep. X2 not on board, so firmware uses LFRC. 56 parts have no 3D model on this PC. C4 still fitted (dropping it also clears the only ERC error); L9/C18 still fitted.
- Not checked: FM8625H datasheet, nPM1300 pin table/layout pages, live JLC stock, D1-D3/R11/IC1/J1 land patterns.

## Run 6 (2026-10-28 night, kicad-designer on Opus): fixes from the pre-fab review
Scope: drop C4, S1, S2, S3, S5, S6 (Brian approved). S4 (R21 stub) is left for bench tuning. No fab output. LCSC/MPN fields were touched only for the new C54. Board edits were made with pcbnew Python (scratch scripts) and schematic edits as text (no MCP symbol placement). Every stage was checked with kicad-cli 10.0.4 (pcb drc --schematic-parity --refill-zones --severity-all, sch erc --severity-all). The RF corner was not touched except for the S1 via and its In2 clearances.

| Stage | Commit | Change |
| --- | --- | --- |
| 1 Drop C4 | 58703df | C4, its GND symbol and wire stub deleted (npm1300 sheet). On the PCB: footprint, GND stub and GND via (111.06,123.97) deleted. VBUS is now 4.7 + 1 (C51) + 0.1 uF. The only ERC error (C4 power_pin_not_driven) is gone. |
| 2 S1 C5 own GND via | b330751 | New GND via 0.45/0.25 at (126.75,123.6), 0.61 mm from C5.1 by a 0.25 mm F.Cu link. Removed the old 0.15 mm C5.1 -> C48.2 link (3.2 mm, sharing a via with C48/C13). C48/C13 keep their via (126.9,126.35). To clear the new via on In2: the VBAT diagonal moved 0.07 mm NE (y = x - 3.9). The VRF diagonal past the via was re-drawn from the VRF via (126,123.5) on a parallel diagonal about 0.6 mm SW, joining y 125.972 at x 128.27. No RF part moved. |
| 3 S2 C54 | 909f735 | **C54 10 uF X5R 6.3 V 0402, Samsung CL05A106MQ5NUNC** (LCSC C15525). Checked on jlcpcb.com: 0402, 10 uF, 6.3 V, X5R; jlcsearch shows 0 JLC stock. **DigiKey/Mouser stock NOT verified**: digikey.com returned 403, mouser.com timed out twice, and there are no DigiKey API credentials. Fields: Value, Footprint C_0402_1005Metric, MPN, Manufacturer, LCSC, Datasheet, Description. Placed at (118.067,124.1) rot 0 at the end of the U2.28/U2.30 F.Cu link (the x 117.387 run), with its own GND via 0.45/0.25 at (118.9,124.1). Copper: U2.28 -> C54.1 4.8 mm, U2.30 -> C54.1 6.1 mm (was 29.9 mm to the nearest VDDIO cap). Nothing closer fits: the band under U2 pins 28-30 (y 120.14-121.25) holds the VSENS via, the LSIN link and the C3/C20 courtyards, with only 0.69 mm between those courtyards. Reference hidden (dense area). |
| 4 S3 VOUT2 | cb28a87 | **No short F.Cu link is possible.** The 0.55 mm column between U2's right pads and L9/L10 carries the pin 1-8 escapes (VOUT1, SW1, VSYS, SW2, PMIC_INT). No via fits next to L10.2 (PMIC_INT via 0.53 mm away, C7 GND pad, In2 SENS_MISO/I2C_SDA). Added a 0.25 mm B.Cu link from the U2.32 via (120.18,119.65) to the existing VDDIO via (120.9,112.05) at C7.2. **U2.32 -> L10.2 is now 13.0 mm / 2 vias (was 17.8 / 3); -> C7.2 9.6 mm (was 14.4); -> C17.2 11.65 mm.** The bench VDDIO ripple / BUCK2 check is still worth doing. |
| 5 S5 F1 branch | 0a8a59f | Widths are listed below. The In2 VBAT run was re-drawn at y 124.53 (was 124.49), with a new jog at x 135.3-136.3 (y 124.3) around the SENS_CS via. The F.Cu VBAT diagonal moved to x - y = 22.4, with a +0.12 jog between y 112.0 and 114.4. The VBAT_CN1 diagonal jogs +0.12 between y 112.6 and 114.2 so it passes the C10 GND via at 0.3 mm. |
| 6 S6 R17 ref | 7c5d1a0 | Hidden (it was on AE1 pad 1 at (133.3,128.25)). Moving it beside R17 at (132.7,125.85) added 6 silk overlaps on C15/X1 and 2 silk-over-pad warnings, so it is hidden like its neighbours C15, X1 and R16. |
| 7 Final | (this commit) | Zones refilled (pcbnew ZONE_FILLER) and saved; this STATUS section. |

**S5 final widths (pad to pad):**
- VBAT, from the U2 trunk to F1.1 (branch starts at (123.65,120.65)):
  - In2: (123.65,120.65)-(123.917,120.564) 0.3.
  - **(123.917-124.282, y 120.564) 0.25 for 0.36 mm**, limited by the hole clearance to the VRF via (124.054,121.102).
  - (124.282-124.464) 0.3; diagonal to (128.43,124.53) 0.3 (5.61 mm); y 124.53 to x 135.3 0.3 (6.87 mm).
  - Jog (135.3,124.53)-(135.53,124.3)-(136.05,124.3)-(136.3,124.55) 0.3; y 124.55 to x 138.45 0.3; diagonal to (140.1,122.9) 0.3; x 140.1 down to y 120.5 0.3.
  - (140.1,120.5)-(139.45,119.85) 0.35 (unchanged).
  - **(139.45,119.85)-(139.32,119.72) 0.3, (139.32,119.72)-(139.06,119.46) 0.25 for 0.37 mm** (hole clearance to the CN1 GND via), (139.06,119.46)-(138.8,119.2) 0.3.
  - (138.8,119.2)-(138.8,118.68) 0.5 (unchanged); (138.8,118.68)-(138.8,118.26) 0.4; (138.8,118.26)-(139.2,117.86) 0.4.
  - **x 139.2, y 117.86-115.7: 0.4 (was 0.15).**
  - (139.2,115.7) to the via (138.84,115.34) 0.4.
  - F.Cu: via -> (137.74,115.34) 0.3; diagonal -> (136.8,114.4) 0.3; jog -> (136.92,114.4) 0.3; diagonal -> (134.52,112.0) 0.3; jog -> (134.4,112.0) 0.3; diagonal -> (133.185,110.785) 0.3.
  - **(133.185,110.785)-(133.05,110.65) 0.25; y 110.65 from x 133.05 to 130.16 0.25 (2.89 mm); (130.16,110.65)-(130.04,110.77) 0.25.** The 0.5 mm board-edge rule above and the F1.2 pad below leave room for 0.25 at most.
  - (130.04,110.77) -> F1.1 0.3.
- VBAT_CN1, F1.2 -> CN1.13: all F.Cu, all 0.3 mm, 13.0 mm. Path: F1.2 -> (133.172,111.37) -> (134.402,112.6) -> jog (134.52,112.6) -> (136.12,114.2) -> jog (136.002,114.2) -> (137.64,115.838) -> (137.64,117.29) -> (137.37,117.56) -> (136.87,117.56) -> (136.31,118.12) -> (136.31,118.32) -> (136.67,118.68) -> CN1.13.
- The narrowest pieces on the branch are now 0.25 mm: three short necks plus the 2.89 mm F.Cu run next to F1 (the 0.25 mm F.Cu run is 3 pieces). Nothing is 0.15 mm any more. Copper estimate (1 oz outer / 0.5 oz inner): about 60 mOhm from the U2 node to CN1.13 (was about 230 mOhm), plus F1.

**Final checks (kicad-cli 10.0.4, after zone refill):**
- DRC (--schematic-parity --refill-zones --severity-all): **0 errors, 413 warnings, 0 unconnected, 0 parity.**
  - Warnings: 192 silk_overlap, 165 silk_over_copper, 54 lib_footprint_issues, 2 silk_edge_clearance.
  - Same result without --refill-zones.
- ERC (--severity-all): **0 errors, 206 warnings.**
  - Warnings: 80 pin_to_pin, 56 lib_symbol_issues, 54 footprint_link_issues, 6 lib_symbol_mismatch, 5 endpoint_off_grid, 3 same_local_global_label, 2 multiple_net_names.
- STEP not exported: the outline and connectors did not move (C4 removed, C54 added). The latest STEP is still nrf54l15_feather_2026-10-28b.step.

**Stackup in the board file vs PCBWay (report only, no width changes):**
- Board file:
  - Layers: F.Mask 0.01 / F.Cu 0.035 / prepreg 0.1 mm (FR4, eps_r 4.5, tan d 0.02) / In1.Cu 0.035 / core 1.24 / In2.Cu 0.035 / prepreg 0.1 / B.Cu 0.035 / B.Mask 0.01, about 1.6 mm in total.
  - copper_finish is "None".
  - The RF lines (0.17 mm ANT_CHIP/ANT_FEED, 0.2 mm match chain) are F.Cu microstrip over the In1 GND plane, 0.1 mm below.
- PCBWay standard 4-layer 1.6 mm (pcbway.com/multi-layer-laminated-structure.html, fetched 2026-10-28):
  - L1: 0.5 oz plated to 1 oz.
  - **L1-L2 prepreg: 7628 RC46 %, 0.196 mm (0.1855 mm after lamination), DK 4.74.**
  - Core 1.03 mm, DK 4.6. L3-L4 is the same as L1-L2.
  - The page says: "If you need custom stackup or control impedance, we will manufacture according to your requirement" (under "Customized Services and Advanced Options").
- Closed-form microstrip estimates (kicad-pro IPC-2141/Wheeler, 1 oz, about 5-10 % from a field solver; the reviewer's Hammerstad estimate gave 52-55 Ohm for 0.17 mm at 0.1 mm / eps_r 4.1):
  - Board-file stackup: 0.17 mm = 46 Ohm, 0.2 mm = 42 Ohm.
  - **PCBWay standard stackup: 0.17 mm = 62 Ohm, 0.2 mm = 58 Ohm. 50 Ohm would need about 0.28 mm.**
  - At 0.12 mm / eps_r 4.4, a 0.18 mm line is 50 Ohm.
- **Recommendation:** don't order the PCBWay standard stackup.
  - Order with impedance control / custom stackup: 4 layers, 1.6 mm, L1-L2 (and L3-L4) dielectric about 0.1-0.12 mm (e.g. 2116, 1080 or 3313 prepreg).
  - State "50 Ohm single-ended microstrip on L1 referenced to L2, 0.17 mm design width" so PCBWay can adjust the prepreg or the width within tolerance.
  - The line runs are short (a few mm against an effective wavelength of about 66 mm at 2.44 GHz), so a 60 Ohm line by itself costs little.
  - The bigger effect is that a 0.19 mm dielectric lowers the pad-to-plane capacitance of the 0201 match parts, which moves the network away from the Nordic values. The match gets tuned on the bench either way.
  - Also ask for ENIG (copper_finish is "None" in the file).

**Not done / notes**
- S4 (R21 DNP stub) not done, per the task (bench tuning).
- The U2.28/U2.30 LSIN node still reaches the rest of VDDIO only by the long path (it now has C54 locally). Linking the LSIN run to the new U2.32 B.Cu route would need a via under U2 pins 28-30, and there is no site there (VSENS via at (118.15,120.1)).
- C54 DigiKey/Mouser stock is unverified (sites blocked from the agent). parts-sourcing should confirm CL05A106MQ5NUNC or swap it for an equivalent 10 uF 0402 X5R >= 6.3 V (e.g. Murata GRM155R60J106ME15D, also unverified).

## Run 7 (2026-10-28 night, kicad-designer on Opus): RF line re-sized to 50 Ohm on the PCBWay standard 4L stackup
Brian approved on 2026-10-28 ordering the PCBWay standard 4-layer 1.6 mm stackup and re-sizing the RF line for it (instead of a custom impedance stackup).

### Stage 1: board stackup (commit 9c81cd6)
Source: pcbway.com/multi-layer-laminated-structure.html, fetched 2026-10-28, "4-layers PCB Regular": L1 0.5 oz plated to 1 oz; PP 7628 RC46 % 0.196 mm (0.1855 mm after lamination), DK 4.74; L2/L3 1 oz; core 1.03 mm, DK 4.6; PP and L4 as L1-L2; 1.51 mm after lamination, 1.61 mm finished (+-10 %). No solder mask thickness is published, so F.Mask/B.Mask stay at 0.01 mm.
- Board file now: F.Mask 0.01 / F.Cu 0.035 / prepreg 0.1855 (FR4 7628 RC46 %, eps_r 4.74, tan d 0.02) / In1.Cu 0.035 / core 1.03 (eps_r 4.6) / In2.Cu 0.035 / prepreg 0.1855 (eps_r 4.74) / B.Cu 0.035 / B.Mask 0.01. Board thickness setting stays 1.6 mm.
- copper_finish is still "None": ENIG is recommended (0.4 mm QFN48, 0201s) but not decided by Brian, so it is not set in the file.

### Stage 2: 50 Ohm geometry (commit 3c9c83b)
Inputs: h = 0.1855 mm (F.Cu to In1 GND), eps_r 4.74, t = 0.035 mm, F.Cu GND pour clearance 0.5 mm (Top GND zone), solid In1 GND.

| Geometry | Hammerstad-Jensen, t = 35 um (own script) | t = 0 | kicad-pro si (IPC-2141/Wheeler) |
| --- | --- | --- | --- |
| Microstrip 0.17 mm (old) | 66.5 Ohm | 71.7 | about 65 (run 6: 62) |
| Microstrip 0.20 mm | 61.9 | 66.3 | 61.0 |
| Microstrip 0.28 mm | 52.5 | 55.5 | 50.0 (si width synthesis: 0.2816 mm) |
| **Microstrip 0.30 mm** | **50.6** (eps_eff 3.36) | 53.4 | **48.5** |
| Microstrip 0.33 mm | 48.1 | 50.5 | 46.0 |

Grounded coplanar (CPWG), Wadell conformal mapping (t = 0, own script; the kicad-pro "coplanar" model has no bottom ground and gives 77-123 Ohm, so it is not usable for CPWG):

| w / gap | 0.10 | 0.127 | 0.15 | 0.20 | 0.50 |
| --- | --- | --- | --- | --- | --- |
| 0.20 mm | 58.4 | 60.6 | 61.9 | 64.0 | 68.6 |
| 0.25 mm | 52.5 | 54.3 | 55.4 | 57.2 | 61.1 |
| 0.30 mm | 47.8 | 49.3 | 50.3 | 51.8 | 55.2 |

**Choice: 0.30 mm microstrip on F.Cu over the solid In1 GND, with the F.Cu GND pour kept at its 0.5 mm (2.7 h) clearance.** Calculated 50.6 Ohm (H-J with 35 um copper) / 48.5 Ohm (IPC-2141); solder mask and the 0.5 mm side pour each pull it down by roughly 1-2 Ohm, so expect about 48-50 Ohm, within the +-10 % that the PCBWay +-10 % dielectric tolerance gives anyway. Why not CPWG:
- On this thin (0.1855 mm) dielectric the In1 plane dominates, so CPWG barely narrows the line: 50 Ohm at w = 0.30 needs g = 0.15 (same width as microstrip), and w = 0.25 needs g of about 0.08 mm, below PCBWay's standard 0.1 mm (4 mil) spacing and very sensitive to etch.
- CPWG needs a continuous coplanar ground at a fixed gap on both sides, with a via fence. The line runs between 0201/0402 pads (C13, C52, C53, L2, R21, C47) and the R11 DFN, so the side ground would be broken every 0.5 mm and the impedance would be undefined; it would also need a special zone rule for the RF nets (the Top GND zone has a 0.5 mm clearance).
- 0.30 mm is close to the 0201 pad width (0.324 mm across the line), so the pads are almost no discontinuity. The R11 (FM8625H DFN-6, 0.22 mm pads at 0.4 mm pitch) and U6 (0.2 mm pin) pads need a short 0.2 mm neck either way.

What is a 50 Ohm segment (stage 3): the R11 common port (ANT, L8.2 -> R11.5), R11 RF2 -> RF1 U.FL, R11 RF1 (ANT_CHIP) -> C12, C12 -> L3 (with the L2 shunt tap), and L3 -> AE1 pad 1 (ANT_FEED). Not changed: the Nordic match network between U6.31 and L8 (L5/C8/L6/C5/L8 in 0201 pads that touch or are 0.3-0.5 mm apart, electrically about 0.01 wavelength, a lumped network per Nordic config 1; U6.31 is a 0.2 mm pin) and the DNP R21 bypass branch (a wider stub would add capacitance to the S4 stub; 0.30 mm also does not clear C47 on the y 124.75 run). The last 2.5 mm of ANT_FEED is inside the AE1 keep-out (no ground on any layer, by design), so it is part of the antenna feed, not a 50 Ohm line; it is drawn at 0.30 mm too.

### Stage 3: re-route at 0.30 mm (commit f7e2958)
Board edits with pcbnew Python (loaded next to its own .kicad_pro, saved to scratch, only the .kicad_pcb copied back). **No part moved**, so the RF corner placement and the B1/B2 work (DECRF-DECA path, match network order, C8 via pin 32, C5 own via) are unchanged, and the outline, connectors and AE1 keep-out are untouched.

| Net / segment | Before | After |
| --- | --- | --- |
| ANT: L8.2 (128.3,124.39) -> (128.3,125.75) -> (128.6,126.05) | 0.20 mm | **0.30 mm** |
| ANT: (128.6,126.05) -> R11.5 (FM8625H common port) | 0.20 | 0.20 neck, 0.37 mm (DFN pads 0.22 mm at 0.4 mm pitch) |
| ANT: C13.1 tap (128.3,125.9) -> (127.87,125.9) | 0.20 from (128.5,125.9) | 0.20, now leaves the straight run |
| Net-(R11-RF2): R11.1 -> neck (128.2,127.45) | 0.20 | 0.20 neck, 0.37 mm |
| Net-(R11-RF2): (128.2,127.45) -> (127.75,127.9) -> RF1.2 U.FL (126.95,127.9) | 0.20 | **0.30** |
| ANT_CHIP: R11.3 -> (129.2,127.28) | 0.17/0.20 | 0.20 neck, 0.28 mm |
| ANT_CHIP: (129.2,127.28) -> (129.2,128.37) -> C12.1; C52.1 -> C12.1 | 0.17 | **0.30** |
| Net-(C12-Pad2): C12.2 -> L3.2, L2.2 on the line | 0.17 | **0.30** |
| ANT_FEED: L3.1 (131.37,128.5) -> AE1.1 (134.67,128.5) | 0.17 | **0.30** (2.5 mm of it inside the AE1 keep-out, no ground by design) |
| ANT_FEED: C53.1 tap | 0.17, 3 pieces via (131.37,128.38) | 0.20, straight down x 131.75 (0.4 mm shorter) |
| Not changed: U6.31 -> L5 -> C8/L6 -> C5 -> L8 (Nordic lumped match, 0.2 mm), ANT -> R21.1 and ANT_CHIP -> R21.2 (DNP bypass stubs, 0.2 mm) | | |

Reference plane: checking the In1 fill under the new line showed two holes from the In1 zone's 0.5 mm via clearance: the ANT_VCTL via at (127.5,127.25) put a 0.75 mm radius void right under the R11 -> RF1 run (no In1 copper under the line centre), and the VRF via (129.75,126.6) bit into the area next to R11.3. Fixes:
- **New In1 GND zone "In1_RF"** (priority 5, clearance 0.2 mm, other settings copied from the In1 zone) over x 124.5-133.5, y 120.5-130.5. Same net as the In1 plane, so it only shrinks the via antipads in the RF corner from 0.75 to 0.45 mm radius. The AE1 keep-out rule area still blocks it (checked: no In1 copper at x >= 132.15, y >= 126.4).
- **ANT_VCTL via moved** (127.5,127.25) -> (127.35,126.85), with its F.Cu link to R11.6 and B.Cu link re-drawn (2 + 3 segments, 0.2 mm). Its void is now 0.6 mm clear of the R11 -> RF1 line edge.
- Result (own script, cut across the line every 0.05 mm): solid In1 at least 0.5 mm either side of every 0.30 mm segment centre outside the keep-out (1.0 mm on ANT, ANT_CHIP vertical, C12-L3 and ANT_FEED; 0.6 mm on R11 -> RF1).
- F.Cu GND pour keeps its 0.5 mm clearance from the line (as assumed in the impedance number). Closest copper to the 0.30 mm line: R11 pads 0.17-0.18 mm (DFN pitch), GND vias 0.11-0.35 mm, C52.2/L2.1 GND pads 0.15-0.21 mm.
- Stitching vias along the line (unchanged): (128.9,123.6), (126.75,123.6), (126.9,126.35), (130.1,125.3), (128.6,127.84), (129.9,127.75), (131.6,129.3), (130.35,129.85), RF1 vias. Gaps along the line are 1.2-1.7 mm, under lambda/20 (3.4 mm at eps_eff 3.36). One extra via above ANT_FEED at (131.1,127.85) was tried and dropped: it lands on the SENS_ID B.Cu run (x 130.95).

### Stage 4: checks and renders
- DRC (kicad-cli 10.0.4, --schematic-parity --refill-zones --severity-all): **0 errors, 0 unconnected, 0 parity, 413 warnings** (192 silk_overlap, 165 silk_over_copper, 54 lib_footprint_issues, 2 silk_edge_clearance), the same warnings as run 6.
- ERC (--severity-all): **0 errors, 206 warnings** (schematic not changed).
- Renders: C:\Personal-Agents\worktrees\nrf54l15-feather-branch\hardware\feather\docs\rf_50ohm_2026-10-28\ (rf_corner_FCu.png, rf_corner_FCu_silk.png, rf_corner_In1_GND.png, rf_corner_overview_FCu_silk.png, rf_corner_FCu_over_In1.png).
- STEP not exported: no part, outline or connector moved. The latest STEP is still nrf54l15_feather_2026-10-28b.step.
- The run 6 recommendation "don't order the PCBWay standard stackup" is superseded: the board is now drawn for it. Order note for PCBWay: standard 4L 1.6 mm, 1 oz outer finished / 1 oz inner, no impedance control needed (the line is a few mm long; the match is tuned on the bench). Optional: ask for impedance control "50 Ohm single-ended, L1 ref L2, 0.30 mm" if the price is the same.

### Open after run 7
- Bench-tune the match (as before). The 0201 pad-to-plane capacitance is now lower (0.1855 mm vs 0.1 mm), so the Nordic values are a starting point only.
- Copper finish not set (ENIG recommended for the 0.4 mm QFN48 and 0201s; Brian to decide at order time).
- S4 (R21 DNP stub on the ANT node) still open, for bench tuning.

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
- Solar review items carried over from v4 (docs\notes\solar-analysis-v4.md):
  - Check C41/C42/C43 capacitance under DC bias.
  - Check the L11 (DFE252010F-100M) land pattern against Murata's recommendation.
  - Check the layout against AEM10330 DS §10.
  - Do these before fab.

## Questions for Brian
- (closed 2026-10-28 evening: Brian placed the 0603 F1 at (130.23, 111.37)) **The F1 polyfuse has no legal site next to CN1.13**: courtyard, DECA and SENS_SDA conflicts (details in Run 5 stage 3, 3.2). Options:
  - (a) a smaller PTC (0402) with a smaller footprint; needs a part check and may still need room.
  - (b) put F1 at the U2 end of the CN1 VBAT branch and rebuild that branch; In2 is full there, so it is a real re-route.
  - (c) move R15 and re-route SENS_SDA near CN1; still conflicts with the frozen DECA trace, so not promising.
  - (d) drop F1 on the host (0R or direct) and fuse on the sensor board.
  - CN1.13 is unpowered until this is decided.
- (closed 2026-10-28, run 6: C4 removed) C4 (1 uF on VBUS) is redundant with C51 at the same node. Remove it?
- (closed 2026-10-24) Feather size: standard outline, keep all connectors, Proposal C (see Decisions).
- (closed 2026-10-24) USB is charge-only; D+/D-/SBU now carry no-connect flags.
- Is moisture_sensor.kicad_sch meant to be empty?
- Do the Gerbers and the 7z in the folder match the current layout, or are they from an earlier revision? Was this revision ordered?

## Decisions
- 2026-10-29 (Brian): C43 stays the single Taiyo 220 uF 1206 (option a of final-review B2). It derates to about 54 uF typical / 43 uF worst at 4.2 V, below the AEM10330 100 uF STO minimum, so the battery must stay on STO: **connect the battery before the solar panel, and never unplug the battery while solar is connected.** No board change. Matches e-peas's own minimal BOM (220 uF 1206 X5R).
- 2026-10-28 (Brian): order the PCBWay standard 4-layer 1.6 mm stackup and re-size the RF line for it (run 7: 0.30 mm microstrip over In1).
- 2026-10-28 (coordinator task, run 5 stage 3): the J1 NPTH-to-pad hole clearance is an accepted exception. The vendor land pattern gives 0.185/0.217 mm, so a J1-only rule "J1_NPTH_to_pad" (hole_clearance min 0.18 mm) is in nrf54l15_feather.kicad_dru. Board-wide hole clearance stays 0.25 mm.
- 2026-10-28 (run 5 stage 3): X2 (32.768 kHz, DNP) is excluded from the board (`on_board no`) because it does not fit above U6 pins 1/2.
- 2026-10-23 (Brian): this is the active main board. Feather form factor replaces v4.
- From v4: EN_SLEEP to GND, MPPT 70 %, and the CN1 14-pin Molex 503480-1400 pinout is fixed on the host.
- 2026-10-24 (Brian): resize to the standard Feather outline (50.8 x 22.86 mm, Feather mounting-hole positions) but **without the Feather header rows or pinout**. Keep every current connector: J1 USB-C, CN1, J3 SWD, U4 battery JST, U5 solar JST. Not FeatherWing-compatible. This is a variant of option (a) in feather-size-study.md and closes its questions 1-3, 5 and 6. Placement questions still open (see Questions for Brian).
- 2026-10-24 (Brian): connector layout is Proposal C (C:\Personal-Agents\worktrees\nrf54l15-feather-branch\hardware\feather\docs\feather_connector_layouts.html). USB-C centred on one short edge; CN1 centred on the far short edge so the FFC folds straight down to sens1, which stacks underneath; U5 solar and U4 battery on opposite long edges near the USB end; the antenna moves to a long edge near the far end. RF risk accepted, to be minimised in layout.
- 2026-10-24 (Brian): **all parts on the top side**, including J3, U4 and U5, so the bottom is flat and sens1 can stack close underneath. The RF1 U.FL + R11 switch (ANT_SEL) is the fallback if the chip antenna's range suffers on the long edge. Defaults accepted: M2.5 holes (plated at the USB end, NPTH + nylon at the far end), USB stays charge-only, no fab output without approval.
- 2026-10-24 (Brian): SENS_MISO on two U6 pins (pad 11 and pad 15) is intentional, not a bug.
- 2026-10-25 (Brian): mounting holes use a 2.7 mm drill (M2.5 clearance) at the same Feather positions. Done in run 2: H1/H2 plated with a 3.4 mm pad, H3/H4 NPTH 2.7 mm. (The footprint names still read MountingHole_2.5mm*; only the pads changed.)
- 2026-10-25 (Brian): the plated USB-end holes H1/H2 are tied to GND (thermal-relief connection to the F.Cu/B.Cu pours and the In1 plane). H3/H4 stay NPTH and unconnected.
- 2026-10-25 (Brian): AE1 moved to the far corner with a ~6.5 x 6.5 mm no-ground area, per the Johanson datasheet/EVB (checked by coordinator). Done in run 2 step 1c; the pi-match values must be tuned on the real board.

## BOM pricing (live, 2026-10-28, parts-sourcing)
- Files: C:\Personal-Agents\worktrees\nrf54l15-feather-branch\hardware\feather\sourcing\bom_digikey_mouser_2026-10-28_live.md plus bom_digikey_2026-10-28_live.csv and bom_mouser_2026-10-28_live.csv (copies in hardware\feather\sourcing\). Live DigiKey and Mouser API data, cut-tape prices, no shipping or tax.
- Cost per board (cheapest DK/Mouser split): 1 board 30.29 USD, 5 boards 138.46 USD total (27.69 per board). Excludes the three lines below that cannot be bought from DK/Mouser (about 1.4 to 2.3 USD more).
- Stock blockers: C43 220uF 1206 (DK 0, Mouser on order only, no same-footprint alternative); J1 HRO TYPE-C-31-M-12 and R11 FM8625H (not at DK or Mouser, LCSC only); X1 YXC crystal (not at DK/Mouser, Murata XRCGB32M000F1S2AR0 8 pF is the proposed drop-in, ESR/pads unchecked).
- Resolved: IC1 AEM10330-QFN is at Mouser (725, $4.22); U2 and U6 are in stock at DK and Mouser; AE1 MPN changed to 2450AT18A0100001E.
- About 14 schematic MPNs should change (out-of-stock Samsung/Murata caps, L4, L7, L9/L10, RF1); the list is in the live BOM file. Substituted inductors, bead, crystal and U.FL need a datasheet or pad check first.

## Run 8 (2026-10-28 night, kicad-designer): BOM field changes from the live DigiKey/Mouser BOM
Part fields only (Value, Manufacturer, MPN, distributor PN, LCSC); no placement or routing changes. Source: sourcing\bom_digikey_mouser_2026-10-28_live.md (field-change list and "Revision 2026-10-28 (later)") plus Brian's decisions of 2026-10-28.

### Stage 1: package and crystal checks
Package check = size code / pad count of the new MPN against the footprint on the board (pad geometry only compared for X1 earlier, by parts-sourcing).

| Ref | New MPN | Package of new part | Footprint on board | Result |
|---|---|---|---|---|
| C1, C10 | GRM033R61A225ME47D | 0201 | easyeda2kicad:C0201, 2 pads | match |
| C3 | GRM188R61H225KE11D | 0603 | C0603, 2 pads | match |
| C7, C17, C18, C20, C22 | GRM21BR61E106MA73L | 0805 | C0805, 2 pads | match |
| C40 | CL10A226MP8NUNE | 0603 | C_0603_1608Metric, 2 pads | match |
| C41, C54 | GRM155R60J106ME15D | 0402 | C_0402_1005Metric, 2 pads | match |
| C45, C48 | GCM155R71C104KA55D | 0402 | C0402 / C_0402, 2 pads | match |
| C46 | GRM188R61C106MA73D | 0603 | C_0603_1608Metric, 2 pads | match |
| L4 | BLM15AG121SN1D | 0402 (1.0 x 0.5) | L0402, 2 pads | match |
| L7 | LQM18PN4R7MFRL | 0603 (1.6 x 0.8) | L0603, 2 pads | match |
| L9, L10 | LSCND1608HKT2R2MF (Taiyo) | 1608 = 0603 | L0603, 2 pads | match |
| R8 | NCU15XH103F60RC | 0402 | R0402, 2 pads | match |
| R9, R10, R14 | ERJ-3GEY0R00V, RC0603FR-07150KL, RC0402FR-07560RL | 0603, 0603, 0402 | R0603, R0603, R0402 | match |
| X1 | XRCGB32M000F1S2AR0 | 2.0 x 1.6, 4 pads | CRYSTAL-SMD_4P-L2.0-W1.6, 4 pads | match (pad containment from parts-sourcing) |
| AE1 | 2450AT18A0100001E | same Johanson antenna, new part number | ANT-SMD_L3.2-W1.6 | unchanged part, MPN only |
| C43 | MSASJ31LBB5227MTCA01 | 1206 | C_1206_3216Metric | unchanged part, DigiKey PN added |
| U4, U5 | S2B-PH-K-S(LF)(SN) | same JST S2B-PH-K-S, no LCSC "-GW" suffix | CONN-TH_S2B-PH-K-S-GW | match |
| J3 | FTSH-105-01-L-DV-K (no -TR) | same part, loose packaging | SAMTEC_FTSH-105-01-L-DV-K, 10 pads | match |
Nothing was left unchanged for a package mismatch. RF1 stays ECT818000500 / ECT footprint (Brian: skip the Hirose suggestion).

**X1 against Nordic's HFXO limits** (nRF54L15 PS, docs.nordicsemi.com, "OSCILLATORS Electrical specification", 32 MHz crystal oscillator table, read 2026-10-28):
- Frequency tolerance requirement: +-40 ppm (BLE), +-60 ppm (2.4 GHz proprietary). XRCGB32M000F1S2AR0: +-10 ppm at 25 C, +-20 ppm over temperature, +-2 ppm/yr aging = about 32 ppm worst case. Pass for BLE, with 8 ppm margin for the load-cap/PCB error (the internal CINT can be trimmed).
- Load capacitance CL_HFXO: 6 pF min, 9 pF typ. XRCGB: 8 pF. Pass. Nordic's own characterisation crystal is 2.0 x 1.6 mm at CL 8 pF.
- Drive level PD_HFXO: 100 uW max. XRCGB rated 300 uW max (the SoC drives it, so the crystal rating is above the limit). Pass.
- ESR: **no number in the PS text.** "Crystal selection" gives it as Figure 5 "Maximum allowed combinations of ESR and C0 for a given load capacitance CL" (an image; "supported if the crystal's parameters fall on the line or below it"). The reference crystal in the electrical table has RS 35 ohm, C0 0.74 pF, LM 9.4 mH at CL 8 pF. XRCGB32M000F1S2AR0 is ESR 50 ohm max, C0 not read. So the ESR/C0 point against Figure 5 is **not verified** (I could not read the image).
- Verdict: **no readable limit is violated, so X1 is changed.** Open: check ESR 50 ohm and the XRCGB C0 against Figure 5 (Brian or the design review, from the PS in a browser) before fab. If it falls above the line, fall back to the second choice NDK CS11336-32M or the old YXC XL7EL89CKI-111YLC-32M (LCSC C2965582, kept in the history of this file).

### Stage 2: field edits (commit c8f0c93)
Edited as text in the eight sheet files and the PCB footprints (only property lines; the diff has no geometry changes). The project had no distributor PN fields, so new hidden fields "DigiKey PN" and "Mouser PN" were added to every changed part (and C43), values from the live BOM table. Manufacturer names were normalised (Murata, Samsung Electro-Mechanics, Taiyo Yuden, Panasonic, Yageo, Johanson Technology, JST, Samtec, e-peas).
- Changed MPN: C1/C10 GRM033R61A225ME47D; C3 GRM188R61H225KE11D; C7/C17/C18/C20/C22 GRM21BR61E106MA73L; C40 CL10A226MP8NUNE; C41 and C54 GRM155R60J106ME15D (C41 trailing D fixed, C54 was CL05A105...CL05A106MQ5NUNC); C45/C48 GCM155R71C104KA55D; C46 GRM188R61C106MA73D; L4 BLM15AG121SN1D (Value too); L7 LQM18PN4R7MFRL; L9/L10 LSCND1608HKT2R2MF; R8 NCU15XH103F60RC; R9 ERJ-3GEY0R00V; R10 RC0603FR-07150KL; R14 RC0402FR-07560RL; X1 XRCGB32M000F1S2AR0 (Value too); AE1 2450AT18A0100001E (Value too); U4/U5 S2B-PH-K-S(LF)(SN) (Value S2B-PH-K-S); J3 FTSH-105-01-L-DV-K (-TR dropped, MP field too); IC1 MPN AEM10330-QFN, Manufacturer e-peas; J1 MPN TYPE-C-31-M-12.
- C43 unchanged part MSASJ31LBB5227MTCA01, DigiKey PN 587-MSASJ31LBB5227MTCA01CT-ND and Mouser PN 963-MSASJ31LBB5227MT added.
- LCSC fields: J1 C165948 added; RF1 C437254 and R11 C2857391 were already set (checked in schematic and PCB). **LCSC numbers of the changed parts were cleared (emptied), because they pointed at the old parts.** The old numbers: C1/C10 C335106, C3 C913904, C7 group C15850, C45/C48 C1525 (C48), C46 C19702, C54 C15525, L4 C92616, L7 C1858257, L9/L10 C6079477, R8 C77131, R9 C21189, R10 C2906993, R14 C2909370, X1 C2965582. AE1 C89334, U4/U5 C157932 kept (same parts). The footprint "Datasheet" fields still point at the old lcsc.com datasheets (not touched).
- BOM check: MPN of every one of the 72 refs in the live BOM compared with the schematic MPN: all match except CN1 (schematic 503480-1400, live buy code 5034801400 is the same part, left as is) and RF1 (kept ECT818000500 by decision; the live BOM still lists the U.FL placeholder). kicad-cli sch export bom runs (the CLI groups rows oddly with these fields, so the comparison was done from the sheet files).
- Not changed: RF1 stays ECT818000500 (LCSC C437254); CN1 stays; other unchanged parts keep their MPNs.

### Stage 3: checks
kicad-cli 10.0.4: ERC 0 errors; DRC (--schematic-parity --refill-zones --severity-all) 0 errors, 413 warnings, 0 unconnected, 0 parity. Same as run 7 for errors/unconnected/parity. No fab output.

### Open after run 8
- X1: check ESR 50 ohm max and C0 of XRCGB32M000F1S2AR0 against Figure 5 of the Nordic PS (image, "Crystal selection"), see stage 1.
- The live BOM and its two CSVs in sourcing\ still show the old schematic MPNs; regenerate them from the schematic (parts-sourcing).
- LCSC numbers for the changed parts are empty on purpose; refill only if LCSC is used as a source.

## Run 9 (2026-10-28 night, kicad-designer on Opus): vias to PCBWay's 0.15 mm annular ring
Brian approved on 2026-10-28 (B1 of shared\reports\2026-10-28-review-orp-ph-prefab.md). PCBWay capabilities: "Min width for Annular Ring is 0.15mm(6mil)". The project rule min_via_annular_width was 0.1, so DRC did not flag these.

### Stage 1: non-compliant vias (before the change)
147 vias: 117 at 0.6/0.3 (0.15 ring, OK), **17 at 0.5/0.3 and 13 at 0.45/0.25 (0.10 ring)**. All 30 are through vias F.Cu-B.Cu. "Gap" = closest other-net copper edge on F.Cu / B.Cu now and if grown to 0.6 mm (own pcbnew script, items within 4 mm; zones not counted, they re-fill). Board minimum clearance 0.1 mm, hole clearance 0.25 mm.

| # | Area | Net | Position | Size | Next to | F.Cu gap now / at 0.6 | B.Cu gap now / at 0.6 |
|---|---|---|---|---|---|---|---|
| 1 | U6 DEC (B1 path) | Net-(U6-DECA) | (129.36,121.85) | 0.45/0.25 | C1.1, C8.1, L5 | 0.166 / **0.091** (XC1 track) | 0.265 / 0.190 (SENS_INT) |
| 2 | U6 DEC | Net-(U6-DECA) | (132.30,118.15) | 0.5/0.3 | C9, U6.42 | 0.198 / 0.146 (C9.2 GND) | 0.649 / 0.599 |
| 3 | U6 fan-out | SENS_SCL | (132.162,119.289) | 0.5/0.3 | U6.38-40 (Brian's hand route) | 0.161 / 0.111 (SENS_SDA) | 0.649 / 0.599 |
| 4 | U6 fan-out | VDDIO | (131.10,121.25) | 0.45/0.25 | U6.36, C50 | 0.176 / 0.101 (XC2 track) | 0.716 / 0.642 |
| 5 | U6 / X1 | GND | (130.50,122.25) | 0.45/0.25 | X1.4, C1 | 0.179 / 0.103 (XC2 track) | 0.226 / 0.151 (SENS_INT) |
| 6 | U6 DEC | GND | (133.50,118.90) | 0.5/0.3 | C9.2, C11.2 | 0.221 / 0.171 (SENS_SDA) | 0.705 / 0.655 |
| 7 | U6 | GND | (133.74,121.47) | 0.5/0.3 | R15.1, C50 | 0.391 / 0.341 | 0.182 / 0.130 (SENS_SCL) |
| 8 | RF corner | ANT_VCTL | (127.35,126.85) | 0.5/0.3 | R11.1/R11.6, C13.2 (run 7 move, In1_RF zone) | 0.173 / 0.123 (GND via 126.9,126.35) | same |
| 9 | RF corner | ANT_VCTL | (125.83,124.90) | 0.5/0.3 | U7.4/U7.5 | 0.226 / 0.176 (U7.5 VRF) | 0.911 / 0.861 |
| 10 | RF corner | ANT_SEL | (123.50,124.90) | 0.5/0.3 | U7.1/U7.2, R20 | 0.270 / 0.220 | 0.832 / 0.782 |
| 11 | RF corner | VRF | (126.00,123.50) | 0.5/0.3 | U7.5, C48.1, C5 | 0.283 / 0.233 | 0.283 / 0.233 |
| 12 | RF corner | VRF | (129.75,126.60) | 0.5/0.3 | C47.1, R11.3/R11.4 (next to ANT_CHIP 0.30 mm line) | 0.250 / 0.201 (ANT_CHIP) | 0.350 / 0.300 |
| 13 | RF corner | VRF | (131.75,125.10) | 0.5/0.3 | C15.2 (via at pad edge), X1.2 | 0.250 / 0.201 | 0.250 / 0.201 (VSENS) |
| 14 | RF stitching | GND | (126.75,123.60) | 0.45/0.25 | C5.1, C48.1 (match network) | 0.221 / 0.146 (C48.1 VRF) | 0.283 / 0.208 |
| 15 | RF stitching | GND | (126.90,126.35) | 0.5/0.3 | C13.2, RF1.3 | 0.173 / 0.123 (ANT_VCTL via) | 0.151 / 0.101 (ANT_VCTL B.Cu track) |
| 16 | RF stitching | GND | (128.90,123.60) | 0.5/0.3 | L6.2, L8.1, C1.2 | 0.189 / 0.139 (L6.2) | 0.860 / 0.810 |
| 17 | RF stitching | GND | (130.10,125.30) | 0.5/0.3 | C47.2, R21.1 (ANT line) | 0.201 / 0.151 (ANT) | 0.151 / 0.101 (VSENS) |
| 18 | RF corner | GND | (132.55,125.68) | 0.5/0.3 | C15, R17 (just outside the AE1 keep-out) | 0.180 / 0.130 (VSENS via) | 0.167 / 0.117 (VSENS) |
| 19 | RF corner | VSENS | (133.20,125.60) | 0.45/0.25 | R17.2 (just outside the AE1 keep-out, x>=132.15 y>=126.4) | 0.179 / 0.104 (R17.2 SENS_INT) | 0.180 / 0.105 (GND via) |
| 20 | RF corner | VSENS | (129.50,130.60) | 0.45/0.25 | R19.1, L2 | 0.609 / 0.535 | 0.609 / 0.535 |
| 21 | LED / RF | GND | (122.50,127.00) | 0.5/0.3 | R20.2, LED1 | 0.959 / 0.910 | 1.827 / 1.777 |
| 22 | U2 (S2 fix) | GND | (118.90,124.10) | 0.45/0.25 | C54.2 | 0.809 / 0.734 | 0.289 / 0.214 (VDDIO) |
| 23 | U2 | VBUSOUT | (119.10,122.25) | 0.45/0.25 | C3.1 | 0.346 / 0.271 | 0.794 / 0.719 |
| 24 | U2 | GND | (110.75,119.75) | 0.45/0.25 | C41.2, C42, C43 | 0.688 / 0.614 | 0.577 / 0.502 |
| 25 | U2 | Net-(U2-NTC) | (104.85,124.70) | 0.45/0.25 | R8.2 | 0.176 / 0.101 (VBUS) | 0.319 / 0.245 |
| 26 | U2 | Net-(U2-NTC) | (106.00,118.20) | 0.45/0.25 | L11, R2 | 1.425 / 1.351 | 1.667 / 1.592 |
| 27 | USB | GND | (100.55,120.58) | 0.45/0.25 | D1.1, D2 | 0.246 / 0.171 (CC2) | - |
| 28 | USB | GND | (101.00,118.65) | 0.45/0.25 | D1.2 | 1.006 / 0.930 | 2.038 / 1.963 |
| 29 | CN1 | VBAT | (138.84,115.34) | 0.5/0.3 | CN1.MP, H3, L4 | 0.797 / 0.747 | 0.797 / 0.747 |
| 30 | CN1 | GND | (135.23,114.10) | 0.5/0.3 | C10.1 | 0.160 / 0.110 (VBAT_CN1) | 1.085 / 1.036 |

Notes: no via is inside the AE1 keep-out. The RF stitching vias along the 0.30 mm line are #14-#17 (the other four, (128.6,127.84), (129.9,127.75), (131.6,129.3), (130.35,129.85), are already 0.6/0.3); enlarging in place keeps the spacing. Only #1 would go under 0.1 mm at 0.6 mm (0.091 to the XC1 track), so it is the 0.55/0.25 candidate. Signal vias in the In1/In1_RF zones (#8-#13, #19, #20) get a 0.05 mm (0.6) or 0.025 mm (0.55) bigger antipad; the In1 reference under the RF line is re-checked in stage 2.

### Stage 2: vias enlarged (commit 4f97681)
pcbnew Python (board loaded next to its own .kicad_pro, saved to scratch, only the .kicad_pcb copied back). **No via moved, no track moved, no part moved**; only via size/drill changed, then all zones refilled. All 22 at 0.6/0.3 were tried first; the 8 that clashed at 0.6 (6 DRC clearance errors) were set to 0.55/0.25 instead, which clears every one without a nudge.

| # | Net | Position | Old | New | Why 0.55/0.25 |
|---|---|---|---|---|---|
| 1 | Net-(U6-DECA) | (129.36,121.85) | 0.45/0.25 | **0.55/0.25** | 0.6 gives 0.090 mm to the XC1 F.Cu track; now 0.115 |
| 2 | Net-(U6-DECA) | (132.30,118.15) | 0.5/0.3 | 0.6/0.3 | |
| 3 | SENS_SCL | (132.162,119.289) | 0.5/0.3 | 0.6/0.3 | |
| 4 | VDDIO | (131.10,121.25) | 0.45/0.25 | 0.6/0.3 | |
| 5 | GND | (130.50,122.25) | 0.45/0.25 | 0.6/0.3 | |
| 6 | GND | (133.50,118.90) | 0.5/0.3 | 0.6/0.3 | |
| 7 | GND | (133.74,121.47) | 0.5/0.3 | 0.6/0.3 | |
| 8 | ANT_VCTL | (127.35,126.85) | 0.5/0.3 | **0.55/0.25** | pair with #15 (0.673 mm centre to centre): 0.6+0.6 gives 0.073 mm, 0.55+0.55 gives 0.123 |
| 9 | ANT_VCTL | (125.83,124.90) | 0.5/0.3 | 0.6/0.3 | |
| 10 | ANT_SEL | (123.50,124.90) | 0.5/0.3 | 0.6/0.3 | |
| 11 | VRF | (126.00,123.50) | 0.5/0.3 | 0.6/0.3 | |
| 12 | VRF | (129.75,126.60) | 0.5/0.3 | 0.6/0.3 | |
| 13 | VRF | (131.75,125.10) | 0.5/0.3 | 0.6/0.3 | |
| 14 | GND (RF stitch) | (126.75,123.60) | 0.45/0.25 | **0.55/0.25** | 0.6 gives 0.080 mm to the In2 VBAT track; now 0.105 |
| 15 | GND (RF stitch) | (126.90,126.35) | 0.5/0.3 | **0.55/0.25** | pair with #8 |
| 16 | GND (RF stitch) | (128.90,123.60) | 0.5/0.3 | 0.6/0.3 | |
| 17 | GND (RF stitch) | (130.10,125.30) | 0.5/0.3 | 0.6/0.3 | |
| 18 | GND | (132.55,125.68) | 0.5/0.3 | **0.55/0.25** | pair with #19 (0.655 mm centre to centre): 0.6+0.6 gives 0.055, 0.55+0.55 gives 0.105 |
| 19 | VSENS | (133.20,125.60) | 0.45/0.25 | **0.55/0.25** | pair with #18 |
| 20 | VSENS | (129.50,130.60) | 0.45/0.25 | 0.6/0.3 | |
| 21 | GND | (122.50,127.00) | 0.5/0.3 | 0.6/0.3 | |
| 22 | GND | (118.90,124.10) | 0.45/0.25 | 0.6/0.3 | |
| 23 | VBUSOUT | (119.10,122.25) | 0.45/0.25 | **0.55/0.25** | 0.6 gives 0.090 mm to the In2 nRF54_SWDCLK track; now 0.115 |
| 24 | GND | (110.75,119.75) | 0.45/0.25 | 0.6/0.3 | |
| 25 | Net-(U2-NTC) | (104.85,124.70) | 0.45/0.25 | 0.6/0.3 | |
| 26 | Net-(U2-NTC) | (106.00,118.20) | 0.45/0.25 | **0.55/0.25** | 0.6 gives 0.098 mm to the In2 CC1 track; now 0.123 |
| 27 | GND | (100.55,120.58) | 0.45/0.25 | 0.6/0.3 | |
| 28 | GND | (101.00,118.65) | 0.45/0.25 | 0.6/0.3 | |
| 29 | VBAT | (138.84,115.34) | 0.5/0.3 | 0.6/0.3 | |
| 30 | GND | (135.23,114.10) | 0.5/0.3 | 0.6/0.3 | |

Totals: 17 x 0.5/0.3 -> 13 to 0.6/0.3 and 4 to 0.55/0.25; 13 x 0.45/0.25 -> 9 to 0.6/0.3 and 4 to 0.55/0.25. Board now: **139 vias 0.6/0.3, 8 vias 0.55/0.25, none under a 0.15 mm ring. None left non-compliant.** Three vias that were 0.5/0.3 (#8, #15, #18) now have a 0.25 mm drill. PCBWay capabilities (fetched 2026-10-28): "Min drill size is 0.15mm", holes "smaller than 0.2mm will be subject to extra charges", so 0.25 mm is standard.
- Rules (.kicad_pro): min_via_annular_width 0.1 -> **0.15**, min_via_diameter 0.4 -> 0.55, Default and PWR net-class via 0.5/0.3 -> **0.6/0.3**. With the new rule and the old vias, DRC flagged exactly the 30 vias (30 annular_width + 30 via_diameter) and no footprint PTH pad, so all the footprint PTH rings already meet 0.15 mm.
- RF corner: no via inside the AE1 keep-out; the stitching vias along the 0.30 mm line (#14-#17) are enlarged in place, so the 1.2-1.7 mm spacing is unchanged. Bigger vias give 0.025-0.05 mm bigger antipads on In1. Same check as run 7 (In1 GND fill, cut across the line every 0.05 mm): solid In1 at least **0.55 mm** either side of every 0.30 mm segment centre outside the keep-out (before: 0.58; the only drop is on the R11 -> RF1 run, from the ANT_VCTL via #8 antipad, 0.60 -> 0.58 and 0.58 -> 0.55; ANT 1.00 -> 0.98; all others 1.00). Run 7 criterion was 0.5 mm.
- DEC path (B1/B2): the DECA In2 run and its two vias (#1, #2) are not moved; #1 grew to 0.55 only.
- The pcbnew save also normalised the hidden "DigiKey PN"/"Mouser PN" properties that run 8 added as text (text thickness added, uuids regenerated, property order). Values unchanged; KiCad's GUI would do the same on its first save.

### Stage 3: checks and renders
- DRC (kicad-cli 10.0.4, --schematic-parity --refill-zones --severity-all, with min annular 0.15): **0 errors, 0 unconnected, 0 parity, 413 warnings** (192 silk_overlap, 165 silk_over_copper, 54 lib_footprint_issues, 2 silk_edge_clearance), same warnings as run 8.
- ERC (--severity-all): **0 errors, 206 warnings** (schematic not changed).
- Renders (changed vias ringed in yellow): C:\Personal-Agents\worktrees\nrf54l15-feather-branch\hardware\feather\docs\vias_2026-10-28\ - before_/after_ U6_FCu_BCu.png, RF_corner_FCu_BCu.png, RF_corner_In1.png, U2_FCu_BCu.png.
- STEP not exported: no part, outline or connector moved (latest is still nrf54l15_feather_2026-10-28b.step). No fab output.
- B1 (annular ring) of the 2026-10-28 ORP/pH pre-fab review is closed for the feather. ORP (40 vias) and sens1 (36) still have 0.10/0.125 mm rings.

## Fab output 2026-10-29 (kicad-designer, Sonnet)
Brian's 2026-10-29 decisions applied: C43 option (a), S1 silk, AE1 as-is, 4/4 mil PCBWay option, "BATT FIRST" silk note. Branch agent/nrf54l15-feather, not pushed.

### Changes
- Stage 1 (38e4769): "P1"/"P14" silk stroke 0.10 -> 0.15 mm (size stays 1.0 mm). Project min_text_thickness 0.08 -> 0.15 mm (and default silk text thickness 0.1 -> 0.15); DRC flagged no other text. Silk note **"BATT FIRST"** on **B.SilkS** (mirrored, reads from the bottom), 0.8 mm high, 0.15 mm stroke, centred at (101.95, 121.43) between U4 (battery JST) and U5 (solar JST). F.SilkS had no room: a scan of 28 positions between the JSTs and several beside them all gave new silk/pad violations, and the only clean F.SilkS spot (vertical at x 96, over J1's silk) crossed J1's silk bracket. The B side is empty there. No copper changed.
- Coordinator follow-up (2026-10-29): the "P1"/"P14" silk texts at x = 151 (about 10 mm outside the board, right edge x 140.8, leftovers from the old board) were deleted. DRC still 0 errors/0 unconnected/0 parity, 413 warnings (same types). Gerbers and drill regenerated into fab_2026-10-29\ and the zip rebuilt; against the first set only F_Silkscreen changed (the two texts gone), the drill files differ only in timestamps, and all other layers and the gbrjob are identical.
- Stage 2 (0519a02): old fab files (all 2026-10-21 or earlier) moved with git mv to hardware\feather\archive\fab_2026-10-21\: 11 Gerbers (B_Cu, B_Mask, B_Paste, B_Silkscreen, Edge_Cuts, F_Cu, F_Mask, F_Paste, F_Silkscreen, In1_Cu, In2_Cu), nrf54l15_feather-job.gbrjob, nrf54l15_feather.drl, nrf54l15_feather.7z, nrf54l15_feather_BOM_PCBWay.xlsx, nrf54l15_feather.net, nrf54l15_feather.xml. Nothing else in the folder was old fab output. CN1 vendor files kept.

### Checks (kicad-cli 10.0.4, before and after: identical)
- DRC (--schematic-parity --refill-zones --severity-all): 0 errors, 0 unconnected, 0 parity, 413 warnings (192 silk_overlap, 165 silk_over_copper, 54 lib_footprint_issues, 2 silk_edge_clearance), same as run 9.
- ERC (--severity-all): 0 errors, 206 warnings.

### Fab output
- Folder: hardware\feather\nrf54l15_feather\fab_2026-10-29\ (kicad-cli from the committed board, Protel extensions, subtract soldermask from silkscreen, zones checked).
- Zip: C:\Personal-Agents\shared\handoff\nrf54l15_feather\nrf54l15_feather_fab_2026-10-29.zip (185 kB). Not uploaded, nothing ordered.
- Files: nrf54l15_feather-F_Cu.gtl, -In1_Cu.g1, -In2_Cu.g2, -B_Cu.gbl, -F_Mask.gts, -B_Mask.gbs, -F_Silkscreen.gto, -B_Silkscreen.gbo, -F_Paste.gtp, -B_Paste.gbp, -Edge_Cuts.gm1, nrf54l15_feather-job.gbrjob, nrf54l15_feather-PTH.drl, -NPTH.drl, -PTH-drl_map.pdf, -NPTH-drl_map.pdf. No pos, no BOM.
- gbrjob: 4 layers, 1.6 mm, finish ENIG, size 50.85 x 22.91 mm (the 50.8 x 22.86 outline plus the 0.05 mm Edge.Cuts line width, which KiCad adds).
- Drill (Excellon, mm, PTH and NPTH split): PTH 191 hits = 147 vias (139 x 0.30, 8 x 0.25) + 44 footprint pads (25 x 0.20, 9 x 0.30, 4 x 0.80 slots/ovals, 4 x 0.90, 2 x 2.70 for H1/H2). NPTH 4 hits (2 x 0.75 J1 pegs, 2 x 2.70 H3/H4). Total 195 = board's 147 vias + 48 hole pads, counted from the .kicad_pcb.
- **Smallest drill is 0.20 mm (25 footprint pad holes, the exposed-pad thermal holes of the QFN parts)**, exactly PCBWay's 0.2 mm minimum, no margin. Smallest via drill is 0.25 mm.

### PCBWay order notes
- Standard 4-layer, 1.6 mm, stackup 0.1855 / 1.03 / 0.1855 mm (L1-L2 prepreg 0.1855; the RF line is 0.30 mm for 50 ohm on that stackup, run 7), 1 oz outer / 1 oz inner.
- Surface finish ENIG. Board 50.8 x 22.86 mm, R2.54 corners.
- Min track/spacing option 4/4 mil (no layout change needed; the layout's rule is 0.15 mm clearance, 0.15 mm annular ring).
- Min hole 0.2 mm (smallest drill 0.20 mm, see above).
- Silk text 0.15 mm stroke minimum; "BATT FIRST" is on the bottom side.

### Bring-up rule (C43, Brian 2026-10-29 option a)
C43 is the single 220 uF 1206 and derates to about 54 uF at 4.2 V, below the AEM10330 100 uF STO minimum. **Connect the battery before the solar panel; never unplug the battery while solar is connected.** Silk "BATT FIRST" on the back between U4 and U5 reminds of it.

## Order state and enclosure hardware (2026-10-30 to 2026-11-02, coordinator)
- 2026-10-30 (Brian): this board is OK to order, with ENIG. The X1 ESR/C0 check only decides which crystal to buy.
- Enclosure (Tidemark, Fusion v17) moved to Amazon hardware: list C:\Personal-Agents\worktrees\nrf54l15-feather-branch\mechanical\hardware_lists\enclosure_hardware_amazon_2026-11-01.md, 3.6 mm insert holes, 8 mm + 6 mm nylon standoff stack. The McMaster version is Fusion v11 + enclosure_tidemark\variant_mcmaster_2026-11-01\.
- Hardware vs board pads check is clean (mechanical\tidemark\hardware_pad_check_2026-11-02.md). H4 screw head clears the AE1 body by only 0.24 mm; a low head or nylon washer is optional, check on the bench.
- No board change. Guide: mechanical\tidemark\assembly_guide_2026-11-01\ASSEMBLY.md. Report: shared\reports\2026-11-01-coordinator-enclosure-hardware.md.

## Two builds (Brian 2026-11-02)
- Standard build: all parts fitted, for pH, ORP, DO and EC sensor boards.
- Radar build, for the water level board: R15, R16, R17 and R18 not fitted; R19 stays. Same bare board and Gerbers. Mark these boards by hand.
- The schematic and BOM show the standard build. For a radar feather, buy and fit four fewer resistors.
- Details: hardware\sensors\CN1_SENSOR_CONNECTOR.md, Feather builds. Review: shared\reports\2026-11-02-review-feather-water-level.md, B1 and S2.

## Next-revision ideas (2026-11-07, Brian)
- **J3, the 10-pin 1.27 mm SWD header (FTSH-105):** consider replacing it with a Tag-Connect TC2030 footprint (legged, standard Tag-Connect SWD pinout: 1 VTref, 2 SWDIO, 3 nRESET, 4 SWCLK, 5 GND, 6 SWO). It is smaller and needs no fitted part. Flash through the TC2030-IDC cable and the SWD section of the prog_adapter board to the 9160 DK Debug out. No change on the 10-29 fab board.
- **IC1 AEM10330 land:** change to the datasheet pattern (Fig 23) and the exposed-pad vias to 0.5/0.2 (2026-11-07 pre-order check N1, N5).
- **Board name and revision on the silk** (pre-order check N6).
- **DigiKey/Mouser parts:** J1 GCT USB4105-GF-A fits the current footprint. R11 could be the Abracon ASWD-S2-0002-T (pad fit unverified). RF1 has no DigiKey/Mouser match yet. See docs\sourcing\dk_mouser_alternates_2026-11-07.md.
