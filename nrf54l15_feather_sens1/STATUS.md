# Feather sensor board 1 - Status

Project: C:\Personal-Agents\worktrees\nrf54l15-feather-branch\nrf54l15_feather_sens1\nrf54l15_feather_sens1\nrf54l15_feather_sens1.kicad_pro
Last reviewed: 2026-10-28

**State: ACTIVE sensor board for the nRF54L15 feather.** Reworked to the Feather outline on 2026-10-25. Fully routed, DRC clean (0 errors). Tidemark R1 antenna keep-out added 2026-10-28 (H4 is now NPTH). **2026-10-28 evening: all pre-fab review items B1-B3, S2-S7, N1, N2, N7, N8 fixed (see "Pre-fab fixes 2026-10-28 evening" below).** Not released for fab: no fab outputs generated (needs Brian's approval).

## Summary
Isolated pH sensor board in Feather form factor. It stacks directly under the feather on shared standoffs and connects through CN1 with a 14-way 0.5 mm FFC folded around the far short edge. The CN1 pinout matches the feather pin for pin (same pad coordinates and same net names, checked against the feather PCB 2026-10-25).
- Host side (non-isolated): CN1 Molex 503480-1400, C1 1 uF and C2 100 nF on VSENS, R1 10k SENS_ID to GND.
- Host side also: C6 100 nF at U3 VDD2 (pin 8).
- Barrier: U3 ADuM1250 I2C isolator (host on side 2, pH OEM on side 1 since 2026-10-28) and U4 NXE1S0303MC isolated 3.3 V DC-DC straddle a 3 mm copper-free gap.
- Isolated side: U2 Atlas pH OEM, J1 SMA probe input, C3/C4/C5, R3/R4 4.7k I2C pull-ups, R5 0R (AGND_ISO to GND_ISO) **DNP since 2026-10-28**, R6 220R preload (DNP) and D1 5.1 V clamp (DNP) on VDD_ISO, J5 INT_ISO test pad (not in the BOM).

## Current state (2026-10-25; see "Pre-fab fixes 2026-10-28 evening" for the current ERC/DRC and parts)
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
- U2 pH OEM at (107, 119.125) on the datasheet land pattern (since 2026-10-28; was (107, 119.1) on the old DXF footprint). U3 at (124, 115.2) **rot 0** (was rot 180 until 2026-10-28), U4 at (124, 126.4) rot -90.
- pH signal (U2 pin 4 PRB to the J1 centre pin): 0.4 mm wide, 6.6 mm pad centre to pin centre (about 4.2 mm of exposed trace between the pads), straight on F.Cu. Per the Atlas OEM datasheet: AGND_ISO guard zone (0.3 mm clearance) round it on all 4 layers, connected to U2 pin 5 and the J1 shell; GND_ISO (digital) under the rest of the isolated side, joined to AGND_ISO only through R5; no vias inside the OEM courtyard.
- Routing (2026-10-28): SDA_ISO runs from U3.2 to a via, then on B.Cu along y = 112 (north of U2, not over it) to the via at U2 pin 1. +3V3_ISO trunk on In2. SENS_SDA runs on B.Cu from a via near CN1 (132.6, 122.9) to a via next to U3.7; the VSENS branch to U3.8/C6 rises on B.Cu at x = 127.9. Everything else on F.Cu. Host GND, GND_ISO and AGND_ISO are stitched with vias. No tracks or vias under U2.

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
- Fab outputs (gerbers, drill, BOM with --exclude-dnp, position file) for PCBWay: not generated; waiting for Brian's approval.
- Bench: VDD_ISO bring-up check before fitting U2 (see Bring-up); scope the ADuM1250 low levels on both sides.
- Re-read the ADuM1250 datasheet when analog.com is reachable, to confirm side 1 is the offset side (pinout already confirmed).
- parts-sourcing: add C6 (CC0402KRX7R7BB104) and the DNP R6/D1 to the sens1 BOM files, drop R5 (DNP) from the totals.
- Verify the J1 SMA height from the BAT Wireless drawing (C496551) and get 3D models for U2 and J1 for the enclosure STEP.
- Fusion: check the FFC loop and the standoff height against the STEP (U2/J1 bodies missing).
- Register the easyeda2kicad footprint and 3D library on this PC (this clears the 9 footprint warnings and adds the passive models).

## Questions for Brian
- H4 is now NPTH (needed for the R1 keep-out). OK, given nylon hardware at the antenna end? Otherwise H4 could stay plated with no net (a floating ring under AE1).
- Stack orientation: sens1 parts facing up (as laid out) gives a gap of about 8 mm because of the SMA. OK, or move to a lower probe connector (for example a vertical U.FL/MMCX pigtail)?
- Standoffs at the USB/probe end: nylon (recommended), or metal with the keepout only?
- INT: is SENS_INT needed on the host? That would need a third isolator channel (ADuM1250 is 2-channel) or polling only.

## Decisions
- 2026-10-23 (Brian): this is the active sensor board. It replaces ph_sensor.
- 2026-10-25 (Brian): standard Feather outline 50.8 x 22.86 mm. sens1 stacks directly under the feather on shared standoffs. Done.
- 2026-10-25 (Brian): same 4 Feather hole positions, 2.7 mm drill. The plated holes must be on the non-isolated GND side, with nothing isolated near a plated hole. Result: H3/H4 (CN1 end) plated GND, H1/H2 (probe end) NPTH with a keepout, the reverse of the feather (see Mounting holes).
- 2026-10-25 (Brian): CN1 directly under the feather's CN1 for a straight FFC fold, pinout pin for pin. Done: same position (138.475, 121.43) and rotation 90 deg as the feather.
- 2026-10-25 (Brian): remove the unused copied sheets. Done: nrf54l15, npm1300, power_supply, usb, antenna, battery, SWD_Debug and the empty moisture_sensor deleted. ERC unchanged at 0 errors / 40 warnings; CN1 net names kept.
- 2026-10-25 (Brian): J5 to be traced. It is the INT_ISO test pad; kept.
- 2026-10-27 (Brian): Tidemark R1 antenna keep-out on sens1 only (template and other sensor boards when next revised). Done 2026-10-28; H4 made NPTH as a consequence.
- 2026-10-28 (Brian): pre-fab review fixes approved: R5 DNP, DNP preload/clamp on VDD_ISO with a bring-up check, ADuM1250 host on side 2, datasheet U2 land pattern, 0.15 mm via rings for PCBWay. sens1 keeps NXE1S0303MC + ADuM1250 for a bench comparison with ORP. Done (see Pre-fab fixes 2026-10-28 evening).
- 2026-10-25: probe J1 on the short edge opposite CN1 (the USB-C end of the stack), so the probe cable exits that end of the enclosure.

## Pre-fab edits 2026-10-28 (Brian's decisions)
- Decisions: R_ID = 10k for pH (register: Sensor_Boards\SENSORS.md). sens1 keeps its existing NXE1S0303MC supply (ORP is the trial of the SN6505B supply). H4 NPTH approved. Fab is PCBWay standard 4-layer 1.6 mm.
- R1 was already 10k; added Manufacturer YAGEO / MPN RC0402FR-0710KL (DigiKey 311-10.0KLRCT-ND, 8.6 M in stock 2026-10-28) in ph_sensor.kicad_sch and the PCB.
- H4 confirmed NPTH (np_thru_hole, drill 2.7, board_only). The H4 nylon-hardware note stands.
- Stackup was 0.1 / 1.24 / 0.1 mm with 35 um inner copper; changed to PCBWay standard 4L 1.6 mm. **Current (since ab32a1c, checked 2026-10-28 evening): prepreg 0.1855 / core 1.03 / prepreg 0.1855 mm, Er 4.74 / 4.6, 35 um copper on all four layers, ENIG finish.** (The 1.1 mm core, 17.5 um inner copper and no-finish figures first written here are superseded.) No RF on this board, so no width changes.
- ERC (kicad-cli): 0 errors, 40 warnings. DRC (--schematic-parity --refill-zones): 0 errors, 0 unconnected, 0 parity, 15 warnings (9 lib_footprint_issues, 6 silk_over_copper). Commit 72be7fc.

## Pre-fab fixes 2026-10-28 evening (review C:\Personal-Agents\shared\reports\2026-10-28-review-orp-ph-prefab.md, all approved by Brian 2026-10-28)
Commits 38dc67e (stage 1), 97d5885 (2), a21990b (3), fa0dd5e (4), 1a58ada (5), d44d79a (6); stage 7 is the commit with this text. Schematic-to-PCB updates were done with KiCad Python (kicad-cli netlist applied to the board, board loaded next to its .kicad_pro, saved to scratch, only the .kicad_pcb copied back). The new sub-sheet symbols (R6, D1, C6) were added by text edit of ph_sensor.kicad_sch, not with the MCP; only their labels were placed with the MCP.

- **Stage 1 (B3, S7, N1):** R5 DNP in the schematic and on the PCB (pads kept), so AGND_ISO and GND_ISO are now joined only inside the OEM, as Atlas requires. MPNs and manufacturers written: U3 ADUM1250ARZ-RL7 (Analog Devices), U4 NXE1S0303MC-R13 (Murata), R5 ERJ-2GE0R00X (Panasonic), J1 BWSMA-KWE-Z001 (BAT Wireless, LCSC C496551: checked on jlcpcb.com and jlcsearch 2026-10-28, MPN BWSMA-KWE-Z001, plug-in, 122,999 in stock), U2 OEM-pH (Atlas Scientific). J5 test pad excluded from the BOM.
- **Stage 2 (B2):** two DNP positions from VDD_ISO (+3v3V_ISO) to GND_ISO next to C3/U4 output, on the isolated side, more than 5.5 mm from host copper and clear of the U2 and U4 courtyards: **R6** 220R 0603 at (117.0, 127.6), YAGEO RC0603FR-07220RL (about 15 mA / 50 mW at 3.3 V; DigiKey 311-220HRCT-ND 290,955 and Mouser 851,183 in stock on 2026-10-28) and **D1** 5.1 V Zener SOD-323 at (116.9, 125.4), cathode on VDD_ISO, onsemi MM3Z5V1T1G (DigiKey 109,718 and Mouser 142,381 on 2026-10-28; Nexperia BZX384-C5V1 was 0 at DigiKey). Both reach the In2 VDD_ISO trunk through a new via at (119.6, 126.1). Schematic note added (see Bring-up).
- **Stage 3 (S2, S4):** ADuM1250 turned round so the host is on side 2 and the pH OEM on side 1 (as ORP did with the ISO1540): U3.8 VDD2 = VSENS, U3.7 SDA2 = SENS_SDA, U3.6 SCL2 = SENS_SCL, U3.5 GND2 = GND; U3.1 VDD1 = +3v3V_ISO, U3.2 SDA1 = SDA_ISO, U3.3 SCL1 = SCL_ISO, U3.4 GND1 = GND_ISO. In the schematic the symbol is mirrored (the labels stay where they were); on the board U3 is rot 0 (was 180) and both sides are re-routed. **C6** 100 nF 0402 (YAGEO CC0402KRX7R7BB104, DigiKey 927,918 and Mouser 46 M on 2026-10-28; Murata GRM155R71C104KA88D was 0 at DigiKey) added at U3.8, 1.8 mm centre to centre; **C4** (isolated-side 100 nF) moved to U3.1, 1.5 mm centre to centre. Barrier line, zones and rule areas unchanged.
  - **ADuM1250 side check:** the ADI datasheet could not be fetched (analog.com timed out three times; Mouser, DigiKey and alldatasheet mirrors returned HTML or 403). The pinout is confirmed from the KiCad Isolator:ADuM1250 symbol (1 VDD1, 2 SDA1, 3 SCL1, 4 GND1, 5 GND2, 6 SCL2, 7 SDA2, 8 VDD2), which matches the pin-compatible TI ISO1540 (local datasheet copy). That side 1 is the side with the raised (offset) low level rests on the review and on the ISO1540 datasheet ("offsetting the low-level output voltage on side 1"); for the ADuM1250 itself it was **not re-verified from the ADI datasheet today**. Bench check: scope the low level at the nRF side (U3.6/U3.7), expect under 0.4 V.
- **Stage 4 (S3, S5):** U2 land pattern replaced by the datasheet one (pH OEM V4.7 p.38: 2.5 x 1.4 mm pads, 2.3 mm pitch, 12 mm rows; body 12 x 11 mm; footprint rule area with no vias), copied from feather_orp's Atlas_ORP_OEM into nrf54l15_v4:Atlas_pH_OEM (same library name, so the schematic field is unchanged; the old 2.9 x 1.5 mm DXF version is in git history). U2 at (107, 119.125): pads at x 101 / 113, pin 4 still at y 121.425 in line with J1. Pins and nets unchanged. PRB/VCC/SDA/SCL/INT stubs end on the new pad centres; PRB still 0.4 mm, straight, on F.Cu, with AGND_ISO fill on both sides on F.Cu and under it on In1/In2/B.Cu (checked after refill). AGND via (99.2, 124.2) moved to (98.9, 124.2), off pad 5. No vias under the module.
- **Stage 5 (B1):** every via now has a 0.15 mm ring: 33 x 0.5/0.3 changed to 0.6/0.3; the 8 vias added in stages 2-4 were already 0.6/0.3. 41 vias, all 0.6/0.3, **none non-compliant**, no clashes, no parts moved. min_via_annular_width 0.1 -> 0.15 and the Default/PWR net-class vias 0.5/0.3 -> 0.6/0.3 in the .kicad_pro, so DRC now flags anything smaller.
- **Stage 6 (N8, N2, S6):** B.Silk (mirrored): "FEATHER pH  rev 0.1" (1.0 mm), "SENSOR TYPE: pH   R_ID: 10k" and, vertical at the H1/H2 end (x 99), "NYLON STANDOFFS ONLY" (0.8 mm, 0.15 mm stroke). All reference text at least 0.8 mm high with a 0.15 mm stroke; the "pH" F.Silk text is 1.0/0.15. EasyEDA pin-1 dots removed from the non-polar passives, C4's silk end next to U3.1 trimmed, C2/C4/C6 references moved; DRC silk warnings 6 -> 0. Deleted the stale nrf54l15_feather_sens1-job.gbrjob, .net and .xml (dated 2026-07, from nrf54l15_v2 / the soil-moisture project, with AE1, LEDs and the nRF parts).
- **Stage 7:** zones refilled and saved (kicad-cli --refill-zones --save-board). ERC 0 errors / 40 warnings (same types as before). DRC (--schematic-parity --refill-zones --severity-all) **0 errors, 0 unconnected, 0 parity**, 9 warnings (lib_footprint_issues: easyeda2kicad library not registered on this PC). Barrier re-check on a scratch copy with a physical_clearance rule (host nets against *_ISO, J1 probe and U2 NC nets, all layers): **minimum 3.000 mm** (U3 pad to pad, all four pairs), zone edges to the opposite U3 pads 3.04 mm, everything else 3.14 mm or more; U4 more than 3.5 mm. STEP: C:\Personal-Agents\shared\handoff\nrf54l15_feather_sens1\nrf54l15_feather_sens1_2026-10-28.step (outline, holes and CN1 unchanged; the U2 footprint and the new small parts differ; U2, J1 and the EasyEDA passives still have no 3D model).

## Bring-up (VDD_ISO check, B2)
The NXE1S0303MC needs about 10 % load (30 mA); below about 5 % its output can rise to about double (up to about 6.6 V). The pH OEM takes about 3.5 mA and its VCC maximum is 5.5 V. The same note is on the pH Sensor schematic sheet.
1. Assemble everything except U2, with R6 and D1 left off.
2. Power the board from the feather (or 3.0-3.3 V on VSENS). Measure VDD_ISO (C3) with no load, then with about 5 mA to GND_ISO (for example 680 ohm on the U2 pin 3 and pin 6 pads).
3. If VDD_ISO is 5.5 V or less at about 5 mA: fit U2.
4. If it is above 5.5 V: fit R6 (220 ohm, about 15 mA, about 50 mW more from VSENS) or D1 (5.1 V clamp), measure again, then fit U2.
5. Wash the OEM area after soldering (Atlas: remove flux, avoid rosin-core solder). Scope the I2C low level on the host side (U3.6/U3.7) and on the OEM side (U3.2/U3.3).

## BOM pricing (live, 2026-10-28)
- Files: nrf54l15_feather_sens1\sourcing\bom_digikey_mouser_2026-10-28_live.md plus bom_digikey_ and bom_mouser_2026-10-28_live.csv (copies in C:\Personal-Agents\shared\design\nrf54l15_feather_sens1\).
- All DigiKey, one order: 13.96 USD for 1 board, 67.33 USD for 5 boards, excluding U2 Atlas pH OEM (45.99 each) and J1 SMA (LCSC C496551, 0.51). With both: 60.46 USD for 1, 299.85 USD for 5. No stock blockers.
- Empty schematic MPNs (J1, R5, U2, U3, U4): written into the schematic and PCB 2026-10-28 evening (U3 ADUM1250ARZ-RL7, U4 NXE1S0303MC-R13, R5 ERJ-2GE0R00X (now DNP), J1 BWSMA-KWE-Z001 / LCSC C496551, U2 Atlas Scientific OEM-pH). J1 is not at DigiKey/Mouser (LCSC only). New lines since the pricing run: C6 CC0402KRX7R7BB104 (fitted, about 0.10 USD) and DNP R6/D1; R5 is now DNP (the pricing file still counts it).

## Clearance nudge 2026-10-28 night (follow-up review S1)
- min_clearance and the Default/PWR net-class clearance raised 0.1 -> 0.15 mm; DRC (--schematic-parity --refill-zones --severity-all) 0 errors, 0 unconnected, 0 parity, 9 warnings (lib_footprint_issues only). Barrier unchanged (3.000 mm).
- S1: VSENS via (127.9,113.93) -> (127.8,113.98); gap to C6.1 (same net) about 0.03 -> 0.07 mm, to U3.7 still >= 0.15. 0.15 to C6.1 is not reachable: the U3.8 to U3.7 pad gap (0.67 mm) is barely wider than the 0.6 mm via. Moving it further would break 0.15 to U3.7 (SDA).
