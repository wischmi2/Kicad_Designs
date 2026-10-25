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
   - **CN1: origin (138.39, 121.43) rot -90, centred on the far short edge** (same edge offset and pad orientation as the old board, signal pads toward the edge at x = 139.71). Feather coordinates: centre (48.39, 11.43); courtyard fx 46.07 to 50.71, fy 6.73 to 16.13. Pin 1 is at board y 118.18 (top side of the connector), pin 14 at y 124.68.
   - AE1 chip antenna: (131.55, 130.23) rot 0 on the bottom long edge, feed pad 1 at (129.97, 130.23). Keep-out moved to x 128.55 to 134.55, y 128.75 to the edge (same 5.9 x 3.1 size as before, now running to the edge); pads allowed (AE1's own), tracks allowed for the feed line, no vias, no pours.
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
5. [next] Route (Freerouting), DRC.

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
- Feather size (see feather-size-study.md, "Decisions needed"): option (a), (b) or (c)? Drop or keep CN1? Where do VSENS and solar go? SWD as Tag-Connect or pads? What does the Feather EN pin drive?
- Mounting holes: M2.5 per the Feather spec, plated at the USB end and NPTH at the antenna end? Positions follow the option chosen above.
- Are the USB D+/D- pins left unconnected on purpose (charge-only USB)?
- Is moisture_sensor.kicad_sch meant to be empty?
- Do the Gerbers and the 7z in the folder match the current layout, or are they from an earlier revision? Was this revision ordered?

## Decisions
- 2026-10-23 (Brian): this is the active main board. Feather form factor replaces v4.
- From v4: EN_SLEEP to GND, MPPT 70 %, and the CN1 14-pin Molex 503480-1400 pinout is fixed on the host.
- 2026-10-24 (Brian): resize to the standard Feather outline (50.8 x 22.86 mm, Feather mounting-hole positions) but **without the Feather header rows or pinout**. Keep every current connector: J1 USB-C, CN1, J3 SWD, U4 battery JST, U5 solar JST. Not FeatherWing-compatible. This is a variant of option (a) in feather-size-study.md and closes its questions 1-3, 5 and 6. Placement questions still open (see Questions for Brian).
- 2026-10-24 (Brian): connector layout is Proposal C (C:\Personal-Agents\shared\design\nrf54l15_feather\feather_connector_layouts.html). USB-C centred on one short edge; CN1 centred on the far short edge so the FFC folds straight down to sens1, which stacks underneath; U5 solar and U4 battery on opposite long edges near the USB end; the antenna moves to a long edge near the far end. RF risk accepted, to be minimised in layout.
- 2026-10-24 (Brian): **all parts on the top side**, including J3, U4 and U5, so the bottom is flat and sens1 can stack close underneath. The RF1 U.FL + R11 switch (ANT_SEL) is the fallback if the chip antenna's range suffers on the long edge. Defaults accepted: M2.5 holes (plated at the USB end, NPTH + nylon at the far end), USB stays charge-only, no fab output without approval.
- 2026-10-24 (Brian): SENS_MISO on two U6 pins (pad 11 and pad 15) is intentional, not a bug.
