# Feather sensor board 1 - Status

Project: C:\Personal-Agents\worktrees\nrf54l15-feather-branch\nrf54l15_feather_sens1\nrf54l15_feather_sens1\nrf54l15_feather_sens1.kicad_pro
Last reviewed: 2026-10-28

**State: ACTIVE sensor board for the nRF54L15 feather.** Reworked to the Feather outline on 2026-10-25. Fully routed, DRC clean (0 errors). Tidemark R1 antenna keep-out added 2026-10-28 (H4 is now NPTH). Not released for fab.

## Summary
Isolated pH sensor board in Feather form factor. It stacks directly under the feather on shared standoffs and connects through CN1 with a 14-way 0.5 mm FFC folded around the far short edge. The CN1 pinout matches the feather pin for pin (same pad coordinates and same net names, checked against the feather PCB 2026-10-25).
- Host side (non-isolated): CN1 Molex 503480-1400, C1 1 uF and C2 100 nF on VSENS, R1 10k SENS_ID to GND.
- Barrier: U3 ADuM1250 I2C isolator and U4 NXE1S0303MC isolated 3.3 V DC-DC straddle a 3 mm copper-free gap.
- Isolated side: U2 Atlas pH OEM, J1 SMA probe input, C3/C4/C5, R3/R4 4.7k I2C pull-ups, R5 0R (AGND_ISO to GND_ISO), J5 INT_ISO test pad.

## Current state (2026-10-25)
- Schematic: root + 2 sub-sheets (Sensor Connector, pH Sensor). The 8 unreferenced copied sheet files were deleted.
- PCB: 50.8 x 22.86 mm, R2.54 corners (same outline as the feather), 4 layers, 15 parts + 4 board-only mounting holes, all parts on the top side.
- ERC (kicad-cli 10.0.4): 0 errors, 40 warnings (unchanged from before the rework: 10 pin_to_pin, 10 lib_symbol_issues, 9 footprint_link_issues, 7 isolated_pin_label, 4 lib_symbol_mismatch).
- DRC (kicad-cli 10.0.4, with and without --refill-zones, schematic parity on): 0 errors, 0 unconnected, 0 parity issues, 15 warnings: 9 lib_footprint_issues (easyeda2kicad footprint library not registered on this PC) and 6 silk_over_copper (the easyeda pin-1 dots on R1/R3/R4/R5/C1/C5 touch their pads; the fab clips them).
- STEP: C:\Personal-Agents\shared\handoff\nrf54l15_feather_sens1\nrf54l15_feather_sens1_2026-10-25.step. **U2 (pH OEM), J1 (SMA) and the easyeda passives have no 3D model on this PC, so they are missing from the STEP.** U3, U4, CN1 and the board are included.
- Fab outputs: none (only the old gerber job file). Not to be generated without Brian's approval.

## Layout (origin = outline top-left corner at 90, 110, same as the feather)
- Barrier at x = 124. Isolated zones end at x = 122.5, host zones start at x = 125.5, on all 4 layers, with a rule-area keepout for tracks, vias and fills in between. Pad-to-pad gap across the barrier: 3.0 mm at U3, 4.1 mm at U4.
- CN1 at (138.475, 121.43), rotated 90 deg: the same position and rotation as the feather's CN1. See "CN1 and the FFC fold" below.
- J1 SMA probe input at (94.4, 121.425), rotated 90 deg, on the left short edge (the USB-C end of the stack), opposite CN1. The barrel sticks out about 7.6 mm past the edge.
- U2 pH OEM at (107, 119.1). U3 at (124, 115.2) rot 180, U4 at (124, 126.4) rot -90.
- pH signal (U2 pin 4 PRB to the J1 centre pin): 0.4 mm wide, about 4.6 mm long, straight on F.Cu. Per the Atlas OEM datasheet: AGND_ISO guard zone (0.3 mm clearance) round it on all 4 layers, connected to U2 pin 5 and the J1 shell; GND_ISO (digital) under the rest of the isolated side, joined to AGND_ISO only through R5; no vias inside the OEM courtyard.
- Routing: SDA_ISO runs over the top of U2 on B.Cu, +3V3_ISO trunk on In2, everything else on F.Cu. Host GND, GND_ISO and AGND_ISO are stitched with vias.

## CN1 and the FFC fold (reasoning)
- The feather is at the top of the stack with all its parts on top, and sens1 sits underneath with **its parts on its top side, facing up at the feather's flat bottom**. Both boards face the same way, so in plan view sens1 is not mirrored: its KiCad top view lines up with the feather's top view (same origin, same hole pattern, same edges).
- The feather's FFC leaves its CN1 heading +x (outward) at the far short edge (x = 140.8), bends 180 deg down round that edge, and comes back heading -x into sens1. So sens1's CN1 has to sit at the same short edge, with its opening facing the same outside edge (+x). The fold line runs along y, which keeps each conductor at the same y. On both boards pin 1 is at y = 124.68 and pin 14 at y = 118.18, so pin 1 meets pin 1 and the pinout carries straight through.
- The mirroring only shows if sens1 is viewed from below: seen from underneath, CN1 appears on the opposite side and pin 1 appears mirrored. That view is not used in KiCad, because sens1 is drawn from its own top side, which faces up in the stack.
- The 503480 is a dual-contact connector (Molex SD-503480-001 note 9), so either FFC contact type (same-side or opposite-side) works for the U-fold. Check the loop length in Fusion against the final standoff height.
- If Brian ever wants sens1 parts facing down instead (flat side up), CN1 would move to the bottom and this has to be redone.

## Mounting holes
- Same 4 Feather positions as the feather: (92.54, 112.54), (92.54, 130.32), (138.26, 112.54), (138.26, 130.32), 2.7 mm drill.
- **2026-10-28: H4 is now NPTH (Tidemark R1, see below); only H3 is plated GND.**
- **The pattern is reversed from the feather (forced by isolation).** On sens1 the CN1 end is the non-isolated GND side, so H3/H4 (x = 138.26) were plated (3.4 mm pad, GND) until 2026-10-28. H1/H2 (x = 92.54) are at the isolated probe end, so they are NPTH, with a 3.5 mm radius no-copper keepout on all layers. On the feather it is the other way round: H1/H2 at the USB end are plated GND and H3/H4 at the CN1 end are NPTH.
- Consequence: the feather's GND-tied standoffs at the USB end land on sens1's isolated end. Use nylon standoffs/screws on that column, or at least keep metal hardware inside the 3.5 mm keepout, so feather GND never touches isolated copper. The CN1 end column is nylon on the feather anyway.

## Heights (for the standoff choice)
- Top side (faces the feather): J1 SMA about 6.5-8 mm (estimated from the 6.2 mm thread and the 7.8 mm body square; the BAT Wireless drawing is image-only and wasn't verified); U4 NXE1S0303MC 4.5 mm (KiCad 3D model); U2 pH OEM under 3.1 mm (Atlas tube inside height; no model); U3 SOIC-8 1.75 mm; CN1 1.0 mm (1.87 mm with the actuator open); passives under 1 mm.
- Bottom side: no SMD parts. Only J1's 5 through-hole pins stick out (about 1.5-2 mm unless trimmed).
- The feather's bottom is flat, so the board-to-board gap is set by J1 (about 8 mm) or by U4 (4.5 mm + margin) if J1 is changed or moved.

## J5
- J5 (Conn_01x01, TestPoint_Pad_D1.0mm) is on net INT_ISO. It is the Atlas OEM INT output (U2 pin 7), a test pad on the isolated side. The ADuM1250 has only 2 channels (SDA/SCL), so INT does not cross the barrier and the host's SENS_INT (CN1 pin 9) is unconnected on sens1. Kept; not a ground or shield point. Atlas says to leave INT floating if unused, which a test pad does.

## Tidemark R1 keep-out (2026-10-28)
Request R1 (concepts.md section 6, tidemark_decisions.md item 6, approved by Brian 2026-10-27 for sens1 only): no copper and no parts on sens1 under the main board's chip antenna AE1, because sens1's ground would otherwise sit about 10 mm under it.

**Conversion.** Both boards use the same frame: Edge.Cuts top-left at (90, 110), USB/probe end at x = 90, CN1 end at x = 140.8. Main-board STATUS run 1 stage 2: X = 90 + fx, Y = 132.86 - fy. sens1 is not mirrored or rotated relative to the main board: it sits underneath with its parts facing up, and the FFC folds round the far short edge along y, so CN1 pin 1 is at (137.15, 124.68) on both boards and the hole pattern and edges line up in plan view (see "CN1 and the FFC fold" above and main-board run 2 step 1). So the main board's AE1 area maps 1:1:

| | Feather (fx, fy) | sens1 board (x, y) |
| --- | --- | --- |
| Corner 1 | (42.15, 6.46) | (132.15, 126.40) |
| Corner 2 | (50.8, 0) | (140.8, 132.86) |

This is the same rectangle as the main board's AE1_keepout rule area (132.15-141 x 126.4-133.1, clipped by the outline, so it follows the R2.54 corner). It is the corner at the CN1 end on the bottom long edge (the y = 132.86 edge), round H4.

**Rule areas (all four copper layers):**
- **Tidemark_R1_AE1_keepout:** the rectangle above with a circular cut-out of r 2.85 mm round H4 (138.26, 130.32); tracks, vias, pads, copper pours and footprints all not allowed.
- **Tidemark_R1_H4_hole:** circle r 2.9 mm round H4 (72-point polygon, overlaps the cut-out); tracks, vias and pours not allowed, pads and footprints allowed so H4 (NPTH, courtyard r 2.75) can stay without a DRC error. Together the two areas cover the whole rectangle: no copper anywhere in it.

**What changed:**
- **H4 (138.26, 130.32) changed from plated GND (3.4 mm pad) to NPTH 2.7 mm** (footprint MountingHole_2.5mm, value "M2.5 2.7mm NPTH", same as H1/H2). Position, drill and outline unchanged. Reason: H4 is inside the area; once the GND pour is gone, its plated pad would be an unconnected GND island (DRC unconnected) or, if kept tied, a GND ring under the antenna. This matches Tidemark hole option A (nylon at the antenna end) and the main board, whose H4 is NPTH too. H3 (138.26, 112.54) stays plated GND, so the CN1 end keeps one plated hole. **Mechanical: use a nylon standoff/screw at H4 (no GND contact there any more).** Revert if Brian wants metal at that corner.
- 3 GND stitching vias removed: (134.5, 127.5), (134.5, 131.8), (136.0, 128.3). Host GND stays connected through the other stitching vias (0 unconnected).
- GND_host pours (F.Cu, In1.Cu, In2.Cu, B.Cu) reshaped with a notch: outline (125.5,110)-(140.8,110)-(140.8,126.4)-(132.15,126.4)-(132.15,132.86)-(125.5,132.86). Checked after refill: 0.000 mm2 of filled copper on any layer inside the rectangle.
- No parts moved (no footprint other than H4 was in the area; CN1's MP tab and courtyard end above y 126.4). No tracks were in the area, so no rerouting. Schematic unchanged.

**Counts (kicad-cli 10.0.4):**
| | Before | After |
| --- | --- | --- |
| ERC | 0 errors, 40 warnings | 0 errors, 40 warnings (same types) |
| DRC (--schematic-parity, --refill-zones) | 0 errors, 15 warnings, 0 unconnected, 0 parity | 0 errors, 15 warnings, 0 unconnected, 0 parity |

**STEP: not exported.** No part moved, the outline and every hole position and drill are unchanged; the only geometry change is copper (H4's pad ring, vias, pours), which the enclosure STEP does not see. The 2026-10-25 STEP stays current. Pass the H4 nylon note to fusion-enclosure.

**Tooling note:** saving the board with pcbnew Python (KiCad 10.0.4) dropped "*.Mask" from all 9 through-hole/NPTH pads (H1-H4, J1). Restored by text edit before commit; kicad-cli --save-board keeps them. Check this after any pcbnew-Python save. Also, removing vias with board.Remove() made later SWIG calls in the same script crash or return untyped objects; do via removal last.

## Open work
- Verify the J1 SMA height from the BAT Wireless drawing (C496551) and get 3D models for U2 and J1 for the enclosure STEP.
- Fusion: check the FFC loop and the standoff height against the STEP (U2/J1 bodies missing).
- Register the easyeda2kicad footprint and 3D library on this PC (this clears the 9 footprint warnings and adds the passive models).
- Stale nrf54l15_feather_sens1.net / .xml and the gerber job file still reflect the old copied project. Regenerate or delete them before any fab release.

## Questions for Brian
- H4 is now NPTH (needed for the R1 keep-out). OK, given nylon hardware at the antenna end? Otherwise H4 could stay plated with no net (a floating ring under AE1).
- Stack orientation: sens1 parts facing up (as laid out) gives a gap of about 8 mm because of the SMA. OK, or move to a lower probe connector (for example a vertical U.FL/MMCX pigtail)?
- Standoffs at the USB/probe end: nylon (recommended), or metal with the keepout only?
- R5 (0R) ties AGND_ISO to GND_ISO. The Atlas datasheet describes the analog plane as sourced from pin 5 and kept separate from the digital plane. Keep R5 fitted, or make it DNP?
- INT: is SENS_INT needed on the host? That would need a third isolator channel (ADuM1250 is 2-channel) or polling only.

## Decisions
- 2026-10-23 (Brian): this is the active sensor board. It replaces ph_sensor.
- 2026-10-25 (Brian): standard Feather outline 50.8 x 22.86 mm. sens1 stacks directly under the feather on shared standoffs. Done.
- 2026-10-25 (Brian): same 4 Feather hole positions, 2.7 mm drill. The plated holes must be on the non-isolated GND side, with nothing isolated near a plated hole. Result: H3/H4 (CN1 end) plated GND, H1/H2 (probe end) NPTH with a keepout, the reverse of the feather (see Mounting holes).
- 2026-10-25 (Brian): CN1 directly under the feather's CN1 for a straight FFC fold, pinout pin for pin. Done: same position (138.475, 121.43) and rotation 90 deg as the feather.
- 2026-10-25 (Brian): remove the unused copied sheets. Done: nrf54l15, npm1300, power_supply, usb, antenna, battery, SWD_Debug and the empty moisture_sensor deleted. ERC unchanged at 0 errors / 40 warnings; CN1 net names kept.
- 2026-10-25 (Brian): J5 to be traced. It is the INT_ISO test pad; kept.
- 2026-10-27 (Brian): Tidemark R1 antenna keep-out on sens1 only (template and other sensor boards when next revised). Done 2026-10-28; H4 made NPTH as a consequence.
- 2026-10-25: probe J1 on the short edge opposite CN1 (the USB-C end of the stack), so the probe cable exits that end of the enclosure.
