# nRF54L15 feather - Status

Project: C:\Personal-Agents\worktrees\nrf54l15-feather-branch\nrf54l15_feather\nrf54l15_feather\nrf54l15_feather.kicad_pro
Last reviewed: 2026-10-25

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
5. [done] STEP exported: C:\Personal-Agents\shared\handoff
rf54l15_feather
rf54l15_feather_2026-10-25b.step (CN1 rotated, AE1 moved, holes 2.7 mm). EasyEDA 3D models are still missing on this PC, so most parts have no body.
   - **Final checks (kicad-cli 10.0.4): ERC 0 errors, 204 warnings (77 pin_to_pin, 57 lib_symbol_issues, 55 footprint_link_issues, 5 off-grid, 5 lib_symbol_mismatch, 3 same local/global label, 2 multiple net names). DRC 4 errors (J1 footprint hole clearance, accepted), 322 warnings (170 silk_overlap, 95 silk_over_copper, 55 lib_footprint_issues, 2 silk_edge), 7 unconnected, 0 parity.**

### Next steps (for the next run)
1. Finish the 7 unconnected items; each needs a small placement change, not just routing:
   - VBUS (U2.21 to C14.1/J1): move the VSYS via (now about (114.7, 116.8)) and the VBUSOUT via (about (114.7, 117.75)) apart by about 0.3 mm, or move CC1/CC2's fan-out vias down, to open a 0.25 mm channel left from U2.21.
   - VSENS (U2.29 to C45/R15-R18): needs a via site near U2's bottom-right; consider moving C3/C19 or the VBAT via below U2.
   - SENS_SCL (U6.39 to R16.2/CN1 pin 4): shift C9 right about 0.4 mm or re-route the C9 GND link so U6.39 can reach a via.
   - I2C_SCL (U6.4 to R12.1/U2.14): move R12 so its pad 1 is not in a closed pocket, then go on B.Cu/In2 along the free band at y 111-112.
   - GND on IC1.18/C42.2 (re-route /Solar/LOAD so pin 18 can stub into the EP) and on C13.2; one F.Cu pour island.
2. Check the AEM10330 loop (DS section 10), the nPM1300 buck loops (L9 now flipped) and the RF chain by hand before fab; tune the AE1 match on the real board.
3. Install the EasyEDA 3D models (or map them to KiCad models) so the STEP has part bodies.

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
