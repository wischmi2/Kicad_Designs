# Tidemark enclosure, first-draft print (plain PETG), 2026-10-29, hardware update 2026-11-01

Fusion document: `nrf54l15_feather_enclosure_tidemark` v9 (project Fish_Stuff / nRF54L15_Feather),
URN urn:adsk.wipprod:dm.lineage:fvkOX6_aTxKGrTD7iTSsdg.
Versions: v3 = stage 1 (model), v4 = stage 2 (checks and fixes), v5 = stage 3 (ORP fit check), v6 = stage 4 (exports),
v7 = McMaster stage 1 (4.0 mm insert holes), v8 = McMaster stage 2 (nylon standoffs and screws), v9 = McMaster stage 3 (exports and notes).
Hardware source: mechanical\hardware_lists\enclosure_hardware_mcmaster_2026-11-01.md

Board STEPs used: feather `nrf54l15_feather_2026-10-28b.step`, sens1 `nrf54l15_feather_sens1_2026-10-28.step`,
ORP `feather_orp_2026-10-29.step` (fit check only; hidden component `Board_ORP_fitcheck`, not exported).

Review STEP (whole assembly, not for printing): C:\Personal-Agents\shared\handoff\nrf54l15_feather\enclosure\tidemark_draft_assembly_2026-10-29.step (made at v6: still shows the printed spacers and the old 6 mm posts; not regenerated)

Screenshots (this folder): tidemark_front.png, tidemark_iso.png, tidemark_section_stack.png (cut on the YZ plane at X 0, through USB-C, J1 SMA and the FFC loop; front on the left), tidemark_footcap_off.png (from below, cap, bung, boot and clip hidden). All made at v6, so they still show the printed spacers.

Nothing was sent to a slicer or printer.

## Model frame
Z up = board fx (USB end down; board edge fx 0 at Z 0). X = 11.43 - fy (antenna/key side on the right seen from the front). Front = -Y. Main board top at Y 0, main bottom Y 1.6, sens1 top Y 15.6, sens1 bottom Y 17.2. Parting plane (sleeve/cap) Z -0.5.

## Overall size
| | W (X) x D (Y) x H (Z), mm |
| --- | --- |
| Column (sleeve above the plinth) | 39.9 x 41.2 (+3.5 rail) |
| Plinth / foot cap footprint | 51.9 x 53.2 |
| Sleeve alone | 51.9 x 53.2 x 63.3 |
| Assembled, roof to toe underside | 67.3 |
| Assembled, roof to heel underside | 81.3 (probe boot hangs a further 21.5) |
| Clip hook top | 20.2 above the roof (rim top 17.2 above the roof) |

The concept's 32 x 78 x 32 is not reachable with these boards. What drives the size (all fixable only on the boards):
- Depth: sens1 J1 (BWSMA-KWE-Z001, 9.6 mm tall per its EasyEDA model) and the USB-C/SMA stacking (see conflict 2) set Hs = 14; front clearance 7 (J3 and JST heights unknown, 6.0 assumed); battery pocket 7.
- Width: both JST PH side-entry connectors (U4 battery, U5 solar) exit the long edges; 6 mm per side is allowed for the mated plug and the wire bend.
- Foot: the face o-ring land plus four M2.5 inserts outside the o-ring need a 6 mm flare round the column.

## Parts and print settings
All printed parts plain PETG, one colour. STLs in `print_draft_2026-10-29\` are already in print orientation.
Update 2026-11-01: the new sled and sleeve STLs are in `print_draft_2026-10-29\new_2026-11-01\` (the Fusion agent could not move files); see `superseded_2026-11-01\README.txt` for the swap. The printed board spacer is no longer part of the print set.

| File | Part | Orientation | Supports | Notes |
| --- | --- | --- | --- | --- |
| tidemark_sleeve_PETG_roof-down.stl | Sleeve (4 walls + roof, brow, plinth, dovetail rail, roof slot ribs) | Roof down | None | Brow is a 20 deg lean; plinth top is a 45 deg chamfer. Key (7.4) and eye (2.7) holes are horizontal holes in a vertical wall. Iron the last top layer (the sealing rim face). Plinth insert holes now 4.0 mm |
| tidemark_footcap_PETG_sealface-down.stl | Foot cap: o-ring groove, toe (USB tunnel + bung recess, solar grommet hole, vent hole), heel (SMA bulkhead), 4 screw counterbores | Sealing face down | None, but bridges | 22 mm bridge over the heel pocket floor and 2.7 mm bridges over the groove. Use a smooth PEI sheet so the sealing face is smooth |
| tidemark_sled_PETG_upright-bottom-edge-down.stl | Sled: plate, 4 posts (8 mm OD, 4.0 mm insert holes), battery rails and ledges | Standing on its bottom edge | None | 61 mm tall and 2 mm thick: use a brim. Post undersides are short horizontal overhangs (8 mm cylinders); the two posts nearest the cap have a flat relief on the cap side |
| (removed) board spacer | Printed spacer D, replaced by the nylon standoff below | | | Do not print |
| tidemark_key_PETG_cap-down.stl | Key (PETG stand-in for the TPU key) | Cap down | None | Flange overhangs the cap by 1 mm; notched for the light pipe |
| tidemark_lightpipe_PETG_outer-end-down.stl | Light pipe, 2.5 rod with a retaining collar | Outer end down | None | 0.75 mm collar overhang. A 2.5 mm clear acrylic rod (cut to 8.8 mm, no collar, glued) is the better optic |
| tidemark_rimclip_12mm_PETG_bridge-down.stl | Rim clip for a 12 mm rim (ClipT) | Bridge (hook top) down | None | 45 deg cut on the channel block makes it support-free |
| tidemark_leaf_card_PETG_back-down.stl | Leaf card for the LL200-2.4-75 (100 x 79 x 2.5, 1.0 mm panel pocket, cable notch) | Back down | None | |
| tpu_parts_optional\ | USB bung, SMA boot, clip pads (PETG fit-check versions) | as named | Bung needs supports | Per the draft rule these are TPU parts for later; print in PETG for fit only, or leave them off |

Suggested PETG settings (Snapmaker U1): 0.4 nozzle, 0.2 mm layers (0.12 mm through the brow band if the lean looks stepped), 4 perimeters on the sleeve and cap, 100 % infill round the groove and the insert bosses (modifier) and about 30-40 % gyroid elsewhere, 240 C nozzle and 75 C bed (adjust to the spool). Estimated volumes (v6, before the 8 mm posts): sleeve 34.9 cm3, cap 12.0 cm3, sled 5.2 cm3.

### Purchased hardware (McMaster-Carr, from enclosure_hardware_mcmaster_2026-11-01.md)
| Qty | P/N | Item | Where |
| --- | --- | --- | --- |
| 8 | 94459A768 | Brass heat-set insert, M2.5 x 0.45, 4 mm long, 4.0 mm hole, 5 mm deep | 4 in the plinth corners, 4 in the sled posts |
| 4 | 92290A056 | 316 SS socket head screw M2.5 x 6 | Foot cap to plinth |
| 4 | 95783A060 | Nylon hex male-female standoff, M2.5, 14 mm body, 4.5 mm across flats, 3.9 mm male thread | Board stack: male end through sens1 into the sled insert, main board on top |
| 4 | 92492A709 | Nylon pan head Phillips screw M2.5 x 5 (head 5.0 dia x 2.1) | Main board top into the standoff |
| 3 ft | 1178N19 | EPDM cord 2.0 mm | Foot-cap o-ring, loop about 154 mm on the groove centreline (2.7 x 1.5 groove, about 25 % squeeze, 78 % fill) |
| 1 | 2189K15 | Silica gel bag | Beside the battery |
Not from McMaster: IP67 SMA bulkhead jack (6.5 mm hole in the heel floor, D-flat not modelled); RG316 pigtail with a right-angle SMA plug, about 60-80 mm; adhesive ePTFE vent over the 3.0 mm hole; 30 mm 14-way 0.5 mm FFC; foam for the battery pocket.

In the model the standoffs and screws are reference bodies in component `Hardware_Ref` (hex prism Y 1.6 to 15.6 plus a 2.5 mm thread cylinder to Y 19.5; pan head 5.0 x 2.1 plus 2.5 x 5 shank from Y -2.1 to 5). Hex corners point along X. They are not printed and not in the STL set. The screw shank overlaps the standoff body by design (threaded engagement, 67 mm3 total).

## User parameters (Fusion > Modify > Change Parameters)
| Name | Value | Drives |
| --- | --- | --- |
| Wall | 2.5 mm | Sleeve shell thickness (roof, walls, brow), cap heel floor depth |
| Clr | 0.5 mm | Reference only (min clearance to components) |
| FitClr | 0.2 mm | Reference for part-to-part fits (key hole, bung, sled-to-wall are cut at this value) |
| TopClr | 7 mm | Main board top to front inner wall |
| CableSide | 6 mm | Board long edge to side inner wall (JST plugs) |
| FFCLoop | 9.5 mm | Board far edge to roof inner face |
| Hs | 14 mm | Board-to-board gap (standoff length, sled planes, cavity depth) |
| SledGap / SledT | 3 / 2 mm | sens1 to sled plate; plate thickness |
| BattT / BattW / BattL / BattClr | 6 / 20 / 50 / 0.5 mm | Battery pocket depth (cavity), cradle rail spacing and length |
| UsbGap | 0.5 mm | USB-C mouth to tunnel inner face (= parting plane) |
| FlareW / PlinthH | 6 / 10 mm | Plinth flare and height (cap footprint follows) |
| OringW / OringD | 2.7 / 1.5 mm | Groove depth (OringD drives the cut; groove outline is fixed, see below) |
| CapT / HeelDepth | 4 / 14 mm | Cap plate thickness, heel depth below the toe |
| ClipT / ClipClr / PadT | 12 / 0.5 / 1.5 mm | Clip gap = ClipT + 2 PadT + ClipClr |
| BrowH / BrowAng | 20 mm / 20 deg | Brow chamfer |
| Derived | InW, YFront, YBack, InD, ZTop, Zp | Cavity box |

Not parameter-driven (fixed coordinates, edit the sketch if the parameters above change a lot): the o-ring groove outline, plinth insert and cap screw positions, key/eye holes, cap openings (tunnel, grommet, vent, bulkhead, heel box), rail and roof ribs, sled post positions, clip pads, leaf card. The insert hole and post diameters are sketch dimensions (SL_inserts d229-d232 = 4.0, SLED_holes d225-d228 = 4.0, SLED_posts d233-d236 = 8.0), not user parameters. The boards and ORP occurrences sit at Hs 14; if Hs changes, move sens1 and ORP by the same delta (assembly move, then capture position) and rebuild the Hardware_Ref standoffs (hex 14 mm, thread start offset 14). The sled and cavity depth follow Hs on their own.

## Fit results, feather + sens1
- Interference (assembly_inspect_interference, whole design, v8): no overlap between either board (or the placeholders) and the sleeve, cap, sled, key, light pipe, bung, boot, clip, standoffs or screws. Remaining hits are expected: pigtail plug nut on the J1 barrel, FFC inside both CN1s, pigtail vs bulkhead reference bodies, clip touching the rail stop (0 volume), the hidden ORP fit-check board against sens1 (same slot), and the screw shanks inside the standoffs (threaded engagement). Standoff and screw overlap was checked; a 0.5 mm clearance to board parts was not measured separately.
- Fixed in stage 2: key flange cut into the light pipe (eye is 5.26 mm from the key centre, so a round flange cannot fit), so the key is notched round the pipe. FlareW 5 -> 6 for 2.3 mm of wall round the plinth inserts (now 2.1 mm with the 4.0 mm holes). Cap counterbore 2.3 -> 2.0 so 2.0 mm stays under the screw heads. 45 deg gussets under the sled width step and a 45 deg cut on the clip channel block, both for support-free printing.
- Measured clearances: J3 and U4 placeholders to the front wall 1.0; AE1 to the brow 4.3; CN1 to the brow 2.7; FFC loop to the roof 1.2; key plunger to SW1 0.2 (intentional pre-travel, B3U travel 0.15); JST plugs to the side walls 3.0; pigtail plug nut to the heel wall 0.54; sens1 J1 tails to the sled 1.06; battery to the back wall 0.5 and to the cradle rails 0.5; sens1 J1 top to the main board 4.5.
- USB-C: tunnel 12.5 x 7 (2.5 long through the cap behind a 1.5 mm bung recess) is centred on J1 (X 0, Y -1.63). The placeholder mouth is at the board edge, so the gap is 0.5. If the real mouth sits 0.23-0.5 inside (courtyard 0.23 inside the edge), the gap is 0.73-1.0 and the plug overmould must reach about 3.5 mm into the tunnel; it must be no larger than about 12 x 6.5 mm.
- SW1/key: plunger axis on SW1 (X 9.335, Z 26.4); eye on LED1 (X 6.17, Z 30.6), pipe ends 0.5 above the LED top.
- AE1 15 mm plastic-only zone: no enclosure metal inside it. Re-measured at v8 (AE1 placeholder to the 4.0 mm insert hole of the far-end sled post): 17.2 mm, the nearest metal. The battery is at 22.7 mm. The plinth inserts are about 40 mm away. The brass inserts are outside the 15 mm zone, so brass stays in the far-end posts (question 6 closed). The nylon standoffs and screws are not metal. Not enclosure, but note: the FFC conductors pass about 4.2 mm from AE1 (CN1 is in that corner by design), and sens1's ground plane now sits 15.6 mm behind AE1 (Hs + 1.6), versus about 10 mm at the concept's Hs 8.
- Walls (v8): 2.5 nominal everywhere. Sled posts: 8.0 mm OD round a 4.0 mm hole = 2.0 mm wall; the two posts nearest the cap (Z 2.54) have a flat relief on the cap side (0.30 mm to the cap rim corner) where the wall is 1.4 mm. Sled plate under those holes: about 1.0 mm to the plate bottom edge (derived from the geometry, 2.54 - 2.0 + 0.5). Plinth insert corners: 2.1 mm to the outside (was 2.3 with 3.6 mm holes). Other local thin spots: 1.5 mm ring behind the key counterbore (front wall), 2.0 heel front wall and floor web between the USB tunnel and the heel pocket (2.1), 2.0 under the cap screw heads.
- Overhangs (roof-down sleeve): brow 20 deg from vertical, plinth chamfer 45 deg, everything else vertical. The only bridges are the cap's heel floor (22 mm) and groove (2.7 mm) and the front-wall holes.

## FFC loop vs standoff height
The 14-way 0.5 mm FFC leaves both CN1s (housing fronts at fx 50.45) heading +Z and makes a U-turn. FFC lines are 15.6 mm apart (Hs + 1.6), so the bend radius is about 7.8 mm and the minimum FFC length is about 28.5 mm (pi x 7.8 + 2 x 2 mm insertion). A standard 30 mm FFC fits: the loop apex sits 8.2 mm past the board end (FFCLoop 9.5 leaves 1.2 mm to the roof). At the concept's Hs 8 the minimum would have been about 19 mm. The connector is dual-contact, so same-side or opposite-side contacts both work.

## ORP fit check (feather_orp_2026-10-29.step in the sens1 slot)
At this design (Hs 14) nothing clashes and nothing has to change. Margins and what would clash at the concept stack:
| Item | Result |
| --- | --- |
| T1 (4.06 mm) vs stack gap | 9.98 mm to the main board. Fits at any Hs >= 4.6. Lower than sens1's U4 (4.51) |
| J1 SMA (9.6 mm) vs stack gap | 4.54 mm to the main board at Hs 14. At the concept's Hs 8 it clashes by 1.6 mm (2.1 with 0.5 clearance), the same as sens1 (same part). Hs must be >= 10.1 for J1 alone and about 14 for the USB-C/SMA-nut separation (conflict 2) |
| J1 barrel and SMA vs heel/pigtail | Same part and position as sens1 (94.4, 121.43; barrel 7.1 mm past the edge), so the same pigtail, heel and bulkhead work. Barrel to heel wall 1.99 mm; pigtail nut to heel wall 0.54 mm |
| J1 pin tails (1.94 below the board) vs battery | 1.06 mm to the sled plate, 3.56 mm to the battery (the plate is in between). Without the sled plate the battery would need >= 2.44 mm behind the board |
| U2 Atlas OEM (2.58) | No issue |
| Antenna | ORP has no Tidemark R1 copper keep-out yet; its ground is 15.6 mm behind AE1 at Hs 14. Add R1 at the next ORP revision (decision 6) |
The ORP board was not re-checked against the new standoffs (ORP hole positions are assumed equal to sens1's).

## Conflicts with the PCBs (for kicad-designer)
1. sens1 J1 height: the BWSMA-KWE-Z001 model is 9.6 mm tall, so the concept's 8 mm standoff clashes. sens1 STATUS estimated 6.5-8 mm and a 7.6 mm barrel; the model gives a 7.1 mm barrel. Check against the BAT Wireless drawing.
2. USB-C over SMA: main J1 (USB-C) and sens1 J1 (SMA) are both centred on fy 11.43 at the same end. A USB-C plug overmould (up to 6.5 mm thick) reaches Y +1.62, and the SMA coupling nut (9.2 mm across corners) starts at Y +1.5 when Hs = 11, so no wall fits between the USB tunnel and the heel. Hs = 14 gives a 2.0 mm wall with 0.38/0.54 mm clearances. Moving sens1 J1 about 7 mm off-centre in fy (or using a lower SMA) would allow Hs of about 10-11 and cut 3-4 mm of depth.
3. JST PH side-entry connectors (U4, U5) exit both long edges, so the enclosure is about 8 mm wider than the concept. Top-entry or vertical connectors, or moving them to the far end, would recover that.
4. Main-board heights not in the STEP (EasyEDA models missing): J1 USB-C (placeholder 8.94 x 7.35 x 3.26, mouth at the edge), J3 FTSH-105 (6.0 assumed), U4/U5 S2B-PH-K-S (6.0 assumed, plug 3.2 mm past the edge), AE1 (1.3), shell/pin tails under the board (1.8). TopClr and CableSide must be revisited once real heights are known.
5. Hole hardware: feather H1/H2 are plated, sens1 H1/H2 are NPTH on the isolated side with a "nylon only" note. The model uses nylon M2.5 x 5 screws and nylon hex standoffs (95783A060) at all four holes; brass is only in the sled posts behind sens1 (4.0 mm hole, insert OD about 4 mm, inside sens1's 3.5 mm copper-free ring round H1/H2) and in the plinth. The standoff hex is 4.5 mm across flats (5.2 across corners) on the main-board bottom and sens1 top; check against the pad and keep-out around the four holes on both boards, which was not done here.

## Assumptions
- Battery 602050 class, 6 x 20 x 50, lead end down, sitting on two ledges with 0.5 mm foam clearance all round.
- Pigtail: right-angle SMA plug on J1, cable running back to a solder-cup bulkhead in the heel floor at (X 0, Y 22). Bulkhead and plug envelopes are rough reference bodies.
- Rim clip: 12 mm rim, 1.5 mm pads, device back hanging against the glass, rim top 17 mm above the roof (clip pad positions are fixed coordinates; ClipT moves the finger).
- Solar lead leaves through a 4.5 mm grommet hole in the toe (front-left), not through the heel.
- The cartridge (sled + boards + battery) comes out downward with the cap removed. The sled is located by the cap at the bottom and by the roof slot ribs at the top.
- The key and the light pipe are PETG stand-ins. The key is fitted from inside before the cartridge goes in and is held between the wall counterbore and SW1 (no seal in the draft).
- Standoff male thread (3.9 mm) passes the 1.6 mm sens1 board and engages the insert by 2.3 mm; the 4 mm insert sits in the 5 mm deep hole (hole depth unchanged at 5, counted from the sens1 face through the post and 2 mm plate).

## Not done / limits
- No vendor drawings were checked; the main-board parts above are placeholders.
- TPU interference ribs (bung 0.3 mm) and the co-printed key membrane are not modelled. The TPU parts exist only as PETG-fit bodies.
- Groove outline, inserts and openings are not tied to the parameters (see the parameter section).
- No slicing, so no print time or support preview from the slicer.
- The old sled, sleeve and board spacer STLs were not moved to superseded_2026-11-01 (no file-move tool); the new sled and sleeve are in print_draft_2026-10-29\new_2026-11-01\. The sleeve STL was exported from a copy rotated 180 deg about X to match the roof-down orientation; not opened in a slicer to confirm.

## Questions for Brian
1. Size: accept about 40 x 41 mm (column) with a 52 x 53 foot and an 81 mm total height, or ask kicad-designer for the board changes above (sens1 J1 off-centre or lower, JST top-entry) to get back towards 32 x 32?
2. Rim or glass thickness for the clip (ClipT, now 12 mm), and how far below the rim the node should hang.
3. FFC: a standard 30 mm 14-way 0.5 mm FFC fits. Buy that, or a custom 28-29 mm one?
4. Real heights of J3 (FTSH-105) and the JST PH connectors, and the USB-C cable you will use (overmould size).
5. Which SMA bulkhead jack and pigtail (straight or right-angle plug)? The heel is sized for a right-angle plug.
6. CLOSED 2026-11-01: brass inserts stay in the far-end sled posts (17.2 mm from AE1, outside the 15 mm plastic-only zone).
7. O-ring groove: keep it on the cap (the groove floor is a bridged surface when printed face-down) or move it to the sleeve rim (a clean top surface)? Your decision was "on the cap", so it stays there unless you say otherwise.
8. For this first print, print the bung, boot and pads in PETG as fit checks, or leave them off?
