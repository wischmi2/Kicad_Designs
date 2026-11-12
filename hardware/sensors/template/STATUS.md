# Feather sensor board template - Status

Project: C:\Personal-Agents\worktrees\nrf54l15-feather-branch\hardware\sensors\template\feather_sensor_template.kicad_pro
Last reviewed: 2026-10-25

**State: TEMPLATE (rev 0.1).** Starting point for every sensor board that stacks under the nRF54L15 feather. Derived from nrf54l15_feather_sens1 (pH) on 2026-10-25; sens1 itself was not changed. Not a fab design: never order it as is. How to use it: README.md in this folder.

## Summary
One sensor board per feather, each pair in its own enclosure. CN1 is a point-to-point FFC link to the feather's CN1; the R_ID resistor tells the firmware which sensor board is fitted.
- Host side (non-isolated): CN1 Molex 503480-1400, C1 1 uF + C2 100 nF on VSENS, R1 = R_ID (SENS_ID to GND, value "10k (set per SENSORS.md)"). No I2C pull-ups (the host has them).
- Isolation (default variant): U3 ADuM1250 I2C isolator and U4 NXE1S0303MC isolated 3.3 V DC-DC across a 3 mm copper-free barrier; C3 2.2 uF / C4 100 nF; R3/R4 4.7k pull-ups on the isolated side; J5 INT_ISO test pad.
- Sensor sheet: empty, hierarchical labels VDD_ISO, GND_ISO, SDA_ISO, SCL_ISO, INT_ISO.
- Parts were all taken from sens1 unchanged (same footprints and part fields). No new parts were added, so no LCSC numbers were looked up for this template.

## Current state (2026-10-25)
- Schematic: root + 3 sub-sheets: Sensor Connector (CN1, C1, C2, R1), Isolation (U3, U4, C3, C4, R3, R4, J5), Sensor (empty). Title blocks rev 0.1 on all sheets.
- PCB: 50.8 x 22.86 mm, R2.54 corners, 4 layers (F.Cu / In1.Cu / In2.Cu power / B.Cu, 1.6 mm), same stackup, design rules and net classes as sens1. 11 parts + 4 board-only holes, all on the top side. Isolation block fully routed; the sensor area is empty with the GND_ISO pours in place on all 4 layers.
- ERC (kicad-cli 10.0.4): **0 errors**, 44 warnings: 10 pin_to_pin (EasyEDA passives with unspecified/input pins, same as sens1), 10 isolated_pin_label (the 7 unused CN1 signals SENS_SCK/MOSI/MISO/CS/INT/AIN + VBAT, and INT_ISO which only has J5 until a sensor is added), 8 lib_symbol_issues and 7 footprint_link_issues (EasyEDA2Kicad / easyeda2kicad / Parts_1 / Connector_FFC-FPC libraries not registered on this PC), 4 lib_symbol_mismatch (GND power symbols), 5 unconnected_wire_endpoint (the intentional stubs on the empty Sensor sheet's hierarchical labels; they keep ERC from flagging the labels as dangling errors and go away when the sensor circuit is wired).
- DRC (kicad-cli 10.0.4, --refill-zones and without, schematic parity on): **0 errors, 0 unconnected, 0 parity**, 11 warnings: 7 lib_footprint_issues (easyeda2kicad library not registered) and 4 silk_over_copper (EasyEDA pin-1 dots on R1/R3/R4/C1 touch their pads; the fab clips them).
- Unconnected items: none. The empty sensor area has no pads, so nothing is reported.
- STEP: C:\Personal-Agents\shared\handoff\feather_sensor_template\feather_sensor_template_2026-10-25.step (board, holes, CN1, U3, U4). The EasyEDA passives (C1-C4, R1, R3, R4) have no 3D model on this PC and are missing; J5 is a flat pad.
- Fab outputs: none, and none to be made from the template.

## Layout (origin = outline top-left corner at 90, 110, same as the feather and sens1)
- Outline: x 90 to 140.8, y 110 to 132.86, R2.54 corners.
- **CN1** at (138.475, 121.43), rotation 90: the feather CN1's exact position and rotation. Pin 1 (GND) at (137.15, 124.68), pin 14 at (137.15, 118.18), FFC opening facing the +x edge. Pin-1 "1" on F.SilkS next to pin 1.
- **Barrier** at x = 124: isolated pours end at x 122.5, host pours start at x 125.5, rule area ISOLATION_BARRIER x 122.6 to 125.4 on all 4 layers (no tracks, vias or pours). U3 at (124, 115.2) rot 180 and U4 at (124, 126.4) rot -90 straddle it.
- Host side parts: C1 (130.6, 118.7), C2 (129.0, 118.3), R1 (135.0, 119.68).
- Isolated block: R3 (119.6, 112.6) and R4 (117.0, 112.6) pull-ups, C4 (120.3, 118.9), C3 (117.8, 130.4), J5 INT_ISO pad (116.3, 121.425). VDD_ISO trunk on In2.Cu along x = 122 and y = 111.
- **Sensor placement area** (isolated, GND_ISO): about x 90 to 116, y 110 to 132.86, minus the H1/H2 keep-outs. Outlined on Dwgs.User. Probe connector goes on the x = 90 short edge.
- **Antenna-corner keep-out** ANTENNA_CORNER_keepout: x 132.15 to 140.8, y 126.40 to 132.86 (8.65 x 6.46 mm, clipped by the R2.54 corner), all 4 copper layers, no tracks, vias or pours (pads allowed so the NPTH H4 hole is legal). This is the feather's AE1_keepout rectangle (read from the feather PCB: x 132.15 to edge, y 126.40 to edge), copied 1:1 because the boards stack in the same plan orientation. The feather's AE1 chip antenna (134.67, 130.08) sits directly above it.
- Silk on B.SilkS (the flat bottom): "FEATHER SENSOR <NAME> rev 0.1", "SENSOR TYPE: ____ R_ID: ____", "ISOLATED SIDE: NYLON STANDOFFS ONLY", "CN1 FFC: 14P 0.5 mm OPPOSITE-SIDE".

## Mounting holes (Feather positions, 2.7 mm drill for M2.5)
- H1 (92.54, 112.54) and H2 (92.54, 130.32): NPTH, isolated/probe end, 3.5 mm radius rule-area keep-outs on all layers (as sens1).
- H3 (138.26, 112.54): plated, 3.4 mm pad, GND (as sens1).
- **H4 (138.26, 130.32): NPTH. Changed from sens1 (plated GND there)** because H4 is inside the antenna-corner keep-out: a grounded ring and metal screw 8 mm under the chip antenna is what the keep-out is meant to avoid, and the feather's H4 is NPTH with a nylon screw anyway. So the template has one plated GND hole (H3).
- Standoffs: nylon at the isolated end (H1/H2) is mandatory, because the feather's H1/H2 at the USB end are plated GND and sit right above them. H4 is nylon (antenna corner, NPTH on both boards). H3 may be metal: the feather's H3 is NPTH, so a metal standoff there only touches this board's host GND.

## CN1 and the FFC fold
Same as sens1 (see hardware\sensors\ph\STATUS.md). The feather's FFC leaves +x at x = 140.8, folds 180 degrees down round that edge and enters this board's CN1 heading -x. Pin 1 meets pin 1. A U-fold puts the conductors on opposite faces at the two ends, so the cable is opposite-side contacts; the 503480 is dual contact (SD-503480-001 note 9), so a same-side cable also works.

## Open work
- Register the easyeda2kicad / EasyEDA2Kicad / Parts_1 libraries on this PC (clears 22 ERC/DRC library warnings and adds 3D models for the passives).
- The first board built from the template (conductivity) must check the VDD_ISO budget, see Questions.

- 2026-11-11: R1 (R_ID placeholder) 10k -> 100k, RC0402FR-07100KL (x10; still reads as pH until set per SENSORS.md). Value/MPN only. ERC 0 errors, DRC 0/0/0 (no refill).

## Questions for Brian
- H4 is NPTH in the template (antenna keep-out), so only H3 is a plated GND hole. OK, or keep H4 plated as on sens1 and allow its pad inside the keep-out?
- The isolated supply is U4 NXE1S0303MC from VSENS. It is unregulated (Vout follows Vin) and VSENS is 3.0 V, at the bottom of its 3.3 V +-10 % input range (from memory of the Murata NXE1 datasheet, not re-checked today), so VDD_ISO is nearer 3.0 V than 3.3 V under load, and the whole sensor shares the 100 mA VSENS budget. Fine for the pH OEM (3.0 to 5 V). The conductivity plan (EZO-EC, 3.3 V min, sensor-board-conductivity.md section 5.3) wants a VBAT-fed SN6505 + transformer + LDO at about 3.9 V instead. Keep the NXE1S0303MC as the template default, or change the default isolation block to the VBAT-fed design once the conductivity board proves it?
- R1 value field is "10k (set per SENSORS.md)". There is no SENSORS.md yet; the ID table is in docs\notes\v4-sensor-connector.md. Create SENSORS.md as the ID register (pH = ?, conductivity = 1k proposed)?
- INT_ISO stops at J5 (2-channel ADuM1250). Make a 3-channel isolator the template default so every board can interrupt the host?

## Decisions
- 2026-10-25 (Brian): one sensor board per feather, each in its own enclosure. CN1 stays point to point; R_ID identifies the board type. Every future sensor board starts from this template.
- 2026-10-25 (Brian): isolated variant is the default; non-isolated is a documented strip-down (README.md).
- 2026-10-25: template built from sens1 by copy; pH parts (Atlas OEM U2, SMA J1, AGND_ISO guard and R5, C5) removed; C1/C2/R1 moved to the Sensor Connector sheet so they survive a non-isolated strip-down; +3v3V_ISO renamed VDD_ISO; R3 moved next to U3.
- 2026-10-25: antenna-corner keep-out added (feather AE1_keepout copied 1:1); H4 made NPTH because it lies inside it.
