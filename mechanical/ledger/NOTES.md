# Pouch gateway enclosure - Concept 1 LEDGER (Fusion model, 2026-10-24)

Fusion document: `pouch_gateway_enclosure_ledger` (project Fish_Stuff / Pouch_Gateway, v2; v3 saved 2026-10-29 with the draft STL export, model unchanged),
URN urn:adsk.wipprod:dm.lineage:RtSr47dsR86jeo1An8NXmg
Review STEP (whole assembly, not for printing): C:\Personal-Agents\shared\handoff\pouch_gateway\enclosure\pouch_gateway_ledger_assembly.step
First draft print STLs: see "First draft print (2026-10-29)" at the end. Nothing was sent to a slicer or printer.

Screenshots in this folder:
- ledger_front.png - front view (window, coral key, RESET/ISP pinholes, grille, status pill)
- ledger_side_section.png - section through the USER key axis (X = 1.72). The image is rotated: face at the top, device bottom on the left, stand at lower left
- ledger_rear_cover_off.png - from behind with the rear cover and stand hidden (mirrored left/right because it is viewed from the back)
- ledger_iso_on_stand.png - iso view with the stand

## Overall size
- Body: 82.0 W x 100.0 H x 24.0 D mm (26.3 D including the key dome).
- On the 15 degree wedge stand: about 82 W x 112 H x 55 D footprint (stand 70 W, base raised 10 mm, 1 mm TPU feet).
- Frame used in the model: X = width, Y = height (Y 0 = bottom), Z = depth (face at Z 24, rear rim at Z 0). The stand is modelled in this frame, so the desk plane is tilted 15 degrees.

## Parts (components)
| Part | Material / colour | Key numbers |
| --- | --- | --- |
| Front_Shell | PETG, Abyss navy | Side/top/bottom walls 2.0, front wall 2.5. R6 vertical corners, R2 front edge. Brow is the top 14 mm leaning back 20 deg |
| Rear_Cover | PETG, Abyss navy | 77 x 95 x 2.0, set 1 mm into the rim with a 0.5 mm shadow gap. 4 x M2 button head (counterbored). "Contains FCC ID: HSW2FR" debossed 0.4 mm |
| Bezel_Insert | PETG, black (separate print) | 48.4 x 38.2 x 1.2 plate in a 48.7 x 38.5 x 1.2 recess. Window 42.0 x 31.8 at the back, 45 deg outward chamfer to 44.4 x 34.2 at the face. Centred on the active area |
| Key_Cap | PETG, coral | 10 mm cylinder through a 10.4 hole, R7.07 dome 2.3 mm proud, 45 deg cone flange (dia 13) behind the wall, dia 2.5 stem 0.2 mm above the USER switch |
| Status_Pill | Translucent coral PETG/PCTG | 8.0 x 2.7 face, flush; flange 9.6 x 4.3 behind the wall; stem ends 0.5 mm above D3/D5/D4 inside a navy collar (opaque shroud) |
| Wedge_Stand | PETG, Abyss navy + 3 TPU foot strips (separate bodies) | 15 deg; front lip, rear back-rest, 7 x 5 mm cable groove on the underside from the left end to the rear |
| Antenna_Molex146153 | placeholder only | 34.9 x 9.0 x 0.1 FPC on the underside of the top wall, under the brow |

Board placement: gateway PCB X -28..30, Y 8..43, back face Z 13.84 (KMR2 tops Z 17.3). LCD active-area centre X 1.72 / Y 65.5 (on the USER key axis), glass top Z 21.0, connector end to the right.

## Fasteners (assumed)
- Gateway: 4 x M2 heat-set inserts (3.2 hole, 4 deep) in dia 5 bosses on the front wall; M2 x 5 from the board back.
- LCD: 4 x M2 x 5 self-tapping (PT) screws from the module back into dia 3.6 bosses (1.6 pilot, 3.5 deep). Waveshare's hex studs and front screws are not used.
- Rear cover: 4 x M2 heat-set inserts in the corner bosses; M2 x 5 button heads.

## Clearances checked
- Interference check (whole design): no enclosure part touches a board part. The only overlap reported is J5's pins inside the PCB's own holes in the supplied board STEP (0.0001 cm3), which is not an enclosure issue.
- LCD glass to front wall: 0.5 mm (room for the 0.5 mm foam/TPU gasket; the glass is not clamped).
- Tallest gateway part (J5, 4.85 mm) to front wall: 1.25 mm.
- Pill stem to LED tops: 0.5 mm. Pill collar to board top: 1.6 mm.
- RESET/ISP guide tubes to switch tops: 0.5 mm. Pinholes 1.5 mm.
- LCD bosses to LCD panel edge: 0.62 mm (FPC end) and 0.79 mm (connector end).
- Antenna: 15.9 mm above the LCD PCB edge (about 15 mm above the panel), 54.9 mm from the gateway ground edge, 18.5 mm from the nearest metal (top cover-screw inserts). No metal in the brow.
- USB-C: J1 to the outside of the left wall is 13 mm (11 mm plug zone + 2 mm wall). Opening 12.5 x 7.0 with R2 corners and a 0.8 mm outside chamfer (14.1 x 8.6 at the surface), centred on J1 (Y 19.65, Z 17.05).
- J5 / LCD cable: 9 mm from the gateway's right edge to the wall, about 10 mm from the LCD's right edge.

## Values I had to assume
1. J1 has no 3D model. Placeholder 9.0 x 7.4 x 3.3 mm placed from the shell-leg holes in the PCB (centre 23.35 mm below the top edge), with the receptacle mouth flush with the board edge. If the HRO TYPE-C-31-M-12 mouth sits proud or recessed, the plug reaches in by that amount more or less.
2. U1 (Murata Type 2FR) is also missing from the board STEP. Placeholder 12 x 11 x 1.6 mm at the footprint from 00-pcb-reference.svg; 1.6 mm height assumed (conservative).
3. USB-C cable overmould must be no larger than about 12 x 6.5 mm and must reach about 6.5 mm into the case. Thick or right-angle overmoulds will not fit; test with the intended cable.
4. The LCD connector cable leaves towards the module's connector end (MEASUREMENTS.md says "expected"); only the bounding box was checked. The display cable must be PH2.0 8-pin to PH2.0 8-pin, about 60-80 mm. Waveshare ships a PH-to-jumper-wire cable, so this needs a made-up cable (pin order to be confirmed by kicad-designer).
5. Bezel insert retention is a 0.15 mm/side slip fit plus a thin double-sided adhesive ring or CA dots. No clips (a 1.2 mm lip can't hold one reliably).
6. Key pre-travel 0.2 mm above the KMR2 actuator, on purpose (below the usual 0.5 mm clearance), so the click comes after a short free travel. Tune after the first print.
7. Coax: Molex 146153-0100 (100 mm lead) from J3 up the right-hand side, sharing the gap with the J5 cable. Not modelled.
8. The gateway bosses (dia 5) pass the interference check; only the bottom-left one was measured to its nearest part (C_0603, about 4.6 mm). The other three are not individually measured against the 0.5 mm rule.

## Conflicts and deviations
- None with the PCB that block a connector or button. J1, USER/RESET/ISP, D3-D5, J5 and the M2 holes all line up with the board STEP.
- Key hole vs bezel: with the window on the active area and USER at Y 39.73, a 10 mm key and the concept's bezel rim overlapped by 0.08 mm. Fixed by raising the LCD 1 mm (5 mm gap between boards instead of 4) and trimming the bezel rim to 2.0 mm. There is now 1.3 mm of navy between the key hole and the bezel, and 1.25 mm between the bezel and the brow crease.
- Front wall behind the bezel recess is 1.3 mm (2.5 minus 1.2 recess). This is under the 2 mm rule, but only in that ring, and the insert lies on it, giving 2.5 mm combined. The bezel insert itself is 1.2 mm (the concept's thin lip).
- Print risk, brow: the concept says the shell prints face-down without supports. The 20 deg brow facet is a 70 deg overhang (20 deg from the bed) in that orientation, over 5.1 mm of height across the full width. Options: variable layer height of 0.08-0.10 mm through the brow band with slow overhang settings, painted supports on the brow facet only, or splitting the brow into a separate cap that also carries the antenna. Brian to decide before printing. DECIDED 2026-10-29 (Brian): option (a), painted supports on the brow facet only; no model change.
- Other overhangs: the USB-C opening roof is a 12.5 mm bridge (fine in PETG). Everything else on the shell is vertical in the face-down orientation.
- Vents: the dot grille (13 x 5 holes, 1.5 mm, 3 mm pitch) over U1/J3 is kept. The bottom vents and the "hidden slot under the brow" are left out. The device sits on the stand seat, which would block bottom vents, and top slots would let splashes in. Heat load is about 0.3-0.5 W.
- Battery, PowerBoost, pigtail, charge port, power switch and wall keyholes are not modelled (per Brian's decisions). J1 is the only external port, with data.
- Debug: Tag-Connect J6 faces the front shell, so remove the gateway (4 screws) to reach it. J2/J4 are not fitted and were removed from the model.
- The stand is solid (about 80 cm3). Print it on its ground face (feet face down; the cable groove becomes a 7 mm bridge) with low infill, or shell it in a later pass.

## Suggested print orientations (Snapmaker U1)
- Front shell: face down on textured PEI (see the brow note above).
- Rear cover: outer face down.
- Bezel insert: back face down (the chamfer opens upward, so no overhang).
- Key cap: dome down on its 4 mm flat (45 deg dome edge).
- Status pill: flange down.
- Stand: ground face down; TPU feet printed separately or with the TPU toolhead as the first layers.

## First draft print (2026-10-29)
Decisions (Brian 2026-10-29): first prints are drafts in plain PETG, one material, one colour. Parts meant for TPU or a second colour are exported as PETG fit-check parts in `tpu_or_accent_optional\` and can be left off. Brow approach (a): painted supports on the brow facet only.

Folder: C:\Personal-Agents\shared\design\pouch_gateway\enclosure_ledger\print_draft_2026-10-29\ (STL in mm, one body per file, already in print orientation, bottom of each part at or near Z 0 so the slicer drops it to the bed). Fusion model v3, unchanged from v2 (the temporary print-orientation moves used for export were deleted again). Board STEP was not refreshed (see below).

| File | Orientation | Supports | Size (bbox) |
| --- | --- | --- | --- |
| Front_Shell_PETG_face_down.stl | front face on the bed (rotated 180 deg about X from the model) | Painted supports on the 20 deg brow facet only (about 5.1 mm tall band, full width). Nothing else: USB-C roof is a 12.5 mm bridge | 82 x 100 x 24 mm |
| Rear_Cover_PETG_outer_face_down.stl | outer face on the bed (as modelled) | None | 77 x 95 x 2 mm |
| Wedge_Stand_PETG_ground_face_down.stl | ground face on the bed (rotated 75 deg about X from the model so the 15 deg ground plane is flat) | None; the 7 x 5 mm cable groove on the underside becomes a 7 mm bridge | 70 x 54.6 x 48.6 mm |
| tpu_or_accent_optional\Bezel_Insert_PETG_back_face_down.stl | back face down (as modelled), chamfer opens upward | None | 48.4 x 38.2 x 1.2 mm |
| tpu_or_accent_optional\Key_Cap_PETG_dome_down.stl | dome down (rotated 180 deg about X) | None expected; check the dome edge. Flip and print flange-down with supports if the dome surface is poor | 13 x 13 x 8.8 mm |
| tpu_or_accent_optional\Status_Pill_PETG_stem_down.stl | as modelled: stem end on the bed, face up (not flange down, because the flange sits mid-height: a 0.8 mm overhang each side) | None | 9.6 x 4.3 x 7 mm |
| tpu_or_accent_optional\TPU_Foot_1/2/3_PETG_flat.stl | flat, 1 mm thick strips (60 x 4, 29 x 4, 15 x 4 mm) | None | - |

Notes on the export:
- Wedge stand: the model has the stand body floating 1 mm above the ground plane on the three TPU foot strips. For the draft the stand STL sits on the bed with no feet, so it is 1 mm lower than the design height. Stick-on rubber or the PETG foot strips (glue) bring it back to the modelled height.
- The stand is solid, about 80 cm3 (about 100 g of PETG if printed solid). Use low infill (10-15 percent gyroid) or accept the print time.
- Key cap and status pill: the pill is meant to be translucent. In plain PETG it will be opaque, so the LED will show only if the print is thin enough; use it for fit only.

Suggested PETG settings (Snapmaker U1, adjust to your profile): 0.2 mm layer (0.12 mm through the brow band if the surface matters), 0.4 nozzle, 4 walls on the shell and stand (min 2 mm walls in the model), 3 top/bottom layers, 20 percent gyroid infill (shell), nozzle 240 C, bed 80 C, textured PEI, part cooling 30-50 percent (lower on the first layers, higher on the brow overhang), slow overhang speed, brim 5 mm on the stand and rear cover for adhesion. Dry the filament.

Hardware list (assumed, per the Fasteners section):
- 4 x M2 heat-set inserts, 3.2 mm hole, 4 mm deep, for the gateway board bosses (front wall); 4 x M2 x 5 screws.
- 4 x M2 x 5 self-tapping (PT) screws for the LCD, into dia 3.6 bosses (1.6 pilot).
- 4 x M2 heat-set inserts in the corner bosses for the rear cover; 4 x M2 x 5 button head screws.
- Optional: 0.5 mm foam or TPU gasket between the LCD glass and front wall; thin double-sided adhesive ring or CA dots for the bezel; USB-C cable with overmould no larger than 12 x 6.5 mm and reaching 6.5 mm in.

Board check: the gateway PCB changed on 2026-10-28 (outline, M2 holes and connectors did not). The model's board is a 60-part imported assembly plus placeholder J1/U1 solids positioned from the old STEP, so swapping in C:\Personal-Agents\shared\handoff\pouch_gateway\pouch_gateway_2026-10-28.step is not a simple replace. Skipped. No new interference check was run (nothing changed in the model). Re-import the new STEP if a later review needs the new component positions.

Check after printing (Brian):
- Key pre-travel: the cap is 0.2 mm above the KMR2 actuator by design; check the click feel, free play and that the cap does not stick in the 10.4 mm hole (dome-down print may leave rough layers on the dome).
- LCD fit: glass window vs the 42.0 x 31.8 bezel window, boss spacing 0.62/0.79 mm to the panel edge, screw pilots, and the 0.5 mm glass-to-wall gap.
- USB-C opening: 12.5 x 7.0 with 0.8 mm chamfer, plug reach about 6.5 mm in, with the intended cable overmould.
- Brow: surface under the painted supports, and whether it is flat enough.
- Rear cover: 0.5 mm shadow gap, counterbore depth, FCC text legibility.
- Bezel slip fit (0.15 mm per side) in the 1.2 mm recess; pill light transmission with a translucent filament later.
- Insert pull-out and boss walls (dia 5 bosses) after heat-setting.

## Fit check, current board STEP (2026-11-07, Fusion v5)
Check only: no enclosure body, feature, parameter or export was changed. The Ledger Fusion doc is now v5 (v4 plus the fit-check component, saved "fit check current board 2026-11-07").
- Added component Board_GW_fitcheck_2026-11-07 (hidden) from pouch_gateway_2026-10-28.step, as in the Tidemark Board_ORP_fitcheck. The old Gateway_PCB assembly and the J1/U1 placeholders are untouched and shown.
- Alignment: pure translation (-138.0, +113.0, +13.844) mm, no rotation. The four M2 hole centres (-25.5/27.5, 10.5/40.5, Z 14.5795) and the PCB bounding box (X -28..30, Y 8..43, Z 13.844..15.315) match the old board to the displayed precision (0.001 mm or better; residual well under 0.05 mm). J5 and J3/U.FL bounding boxes match the old ones exactly. J1 and U1 have no 3D model in the STEP, so J1 alignment is by the PCB outline only.
- Interference (whole design, hidden bodies included, coincident faces off): no enclosure body (Front_Shell, Rear_Cover, Bezel_Insert, Key_Cap, Status_Pill, Antenna, Wedge_Stand, LCD module, hardware) touches the new board except one item. The other hits were old-board versus new-board duplicates (expected, same place), pins in the PCB's own holes (J5, 0.0001 cm3) and Front_Shell vs Hardware_Ref 0.0112 cm3 (not board related, an insert or screw against the shell; body not identified, not checked whether v4 had it too).
- One hit: Front_Shell vs the PinHeader_1x03 (J4 UART, DNP, not in the old model), 0.001 cm3. Its pin tips reach Z 23.94 against the inner front wall at Z 21.5. J4 is not fitted (Brian 2026-10-24), so this is only a model artefact. Do not fit a tall header there. J2 (2x05 SMD header, also DNP) tops at Z 19.8, clear.
- C2 (0402, now at X -9.30..-8.80, Y 13.55..14.55, moved +1.46 mm in Y from 12.59 centre to 14.05): nearest enclosure body is the Front_Shell inner front wall at 5.6 mm (part top Z 15.9, wall Z 21.5). Hardware 14.8 mm away. No issue.
- Bosses (dia 5, ends at Z 15.4) to nearest board part, edge to edge in the board plane:
  - Bottom-left (-25.5, 10.5): J1 placeholder 2.15 mm (placeholder body, real J1 not modelled); nearest real 3D part C_0603 4.56 mm. U1 placeholder 20.8 mm.
  - Bottom-right (27.5, 10.5): J5 5.58 mm.
  - Top-right (27.5, 40.5): J5 1.52 mm (J5 body to boss, Z overlap 15.4..20.25).
  - Top-left (-25.5, 40.5): J2 SMD header 2.6 mm (DNP); with J2 not fitted the nearest part is SW1 at about 11.3 mm.
  All are above the 0.5 mm rule. Smallest is top-right at J5 1.52 mm.
- Needs a change: nothing on the board or enclosure. Open point: J1 shell and mouth position are still unchecked against a real model (placeholder).
