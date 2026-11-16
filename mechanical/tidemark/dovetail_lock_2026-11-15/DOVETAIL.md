# Tidemark top-drop dovetail lock (replaces the hook-on cleat), 2026-11-15

Why: Brian 2026-11-15, "right now it kind of just hangs there and can easily come off. we need something to lock it into place." No screw and no extra piece: the node slides down from the top and gravity holds it. The first dovetail (v6-v17) failed because it had to enter from below, past the plinth.

Status: modelled, checked, STLs and drawings exported. Not printed. Nothing sent to a slicer or printer.

Fusion document `nrf54l15_feather_enclosure_tidemark` (Fish_Stuff / nRF54L15_Feather), started from v27:
- **v28**: sleeve. Cleat (feature `Cleat`) suppressed, not deleted. Two-lug dovetail rail added (sketches SL_dovetail_xy, SL_dovetail_bands, SL_dovetail_recess; features Extrude11-13, `DovetailRail` join).
- **v29**: Perch saddle and 12 mm RimClip slots. On the saddle, the old cleat pocket is filled back in (PERCH_dt_yz / Extrude11) and the new slot is cut in (PERCH_dt_* sketches, Extrude12-19, Combine1). On the RimClip, the old pocket (Extrude7) is suppressed, the block is extended down to Z 23.5 (CLIP_dt_ext), the face is trimmed to Y 32.05 (CLIP_dt_trim), and the same slot is cut (copied tool bodies, Combine2). The flex-finger detent is added to both.
- **v30**: window ceilings and the upper lug raised 1 mm (hard lift stop 12.15 mm). Saddle plinth relief deepened. RimClip delta features and a second face trim (CLIP_dt_trim2).
- **v31**: the upper lug gets 0.3 mm of vertical clearance, so the lower stop carries the weight and the upper shelf is only a backup. Checks done.
- **v32**: STLs exported from temporary Move features (deleted again; geometry as v31). Drawings rendered. View state only.

Cloud saves worked for all versions, so no local .f3d was needed.

Note on the RimClip tool bodies: they were copied from the saddle with "copy body", and the copies stay linked to the saddle's sketches. Editing PERCH_dt_slot_bands / PERCH_dt_win_bands moves the RimClip slot too (checked: both read 0.212 mm at the upper lug after the v31 edit). The RimClip delta features (CLIP_dt_bandsA/B, Combine4-6) and CLIP_dt_trim2 sit on top. If the slot bands are edited again, re-check the RimClip.

## How it works

The rail is two short dovetail blocks ("lugs") on the sleeve's back wall. The saddle (and the clip) has a matching dovetail slot with an open "window" directly above each lug's seat.

To fit: the lugs go straight back into the windows, then the node drops so each lug slides down into its dovetail slot. The lower lug sits on a closed 45 deg bottom stop. The 45 deg dovetail flanks stop the node pulling away from the wall. A small flexing finger in the slot clicks into a groove on the lower lug, so a knock cannot ride the node back up.

Splitting the rail into two 8 mm lugs, each with its own window, means the node only has to lift about the length of one lug (not the whole rail). The back plate never needs to be cut open at the top, and no headroom is needed above the rim.

Frame: as NOTES.md (Z up, roof Z 62.8, sleeve back wall Y 31.7, room at -Y, sump/wall at +Y). Below, u = Z + (Y - 31.7). Lines of constant u fall at 45 deg towards the wall. All the stop, cheek-top and window-ceiling faces are 45 deg planes of constant u, so they print support-free on all three parts.

### Key dimensions

| Item | Value |
| --- | --- |
| Lug cross-section (XY) | 45 deg dovetail, 3.0 mm proud of the wall (Y 31.7 to 34.7), 8.0 wide at the wall, 14.0 wide at the tip (built from Y 31.2 inside the wall) |
| Lug length | 8 mm each, measured along u. Top and bottom faces both slope 45 deg (higher at the wall) |
| Lower lug | u 30.4-38.4 (at the wall Z 30.4-38.4; at the tip Z 27.4-35.4) |
| Upper lug | u 52.05-60.05 (at the wall Z 52.05-60.05; top 2.75 mm below the roof) |
| Detent groove | Across the lower lug tip at Z 31.5: 3.2 wide at the tip face, 0.8 deep, 45 deg sides |
| Slot (saddle and clip) | Dovetail 9.69 wide at the mouth (Y 32.05), 15.69 at the back (Y 35.05). Clearances 0.35 mm normal to the flanks, 0.35 mm at the lug tip, 0.35 mm from the sleeve back to the slot face |
| Main bottom stop | 45 deg face under the lower lug at u 30.4 (Z 30.05 at the mouth, Z 27.05 at the back). Lug-on-stop is the bearing contact; the face is the full slot width (projected area about 33 mm2) |
| Upper shelf (backup stop) | u 50.55-51.75 (1.2 mm thick vertically, 0.85 mm normal). 0.3 mm vertical gap to the upper lug when seated (measured 0.21 mm normal) |
| Windows | Above each lug seat, cut to the slot depth (Y 35.05). 22.4 wide at the mouth (X +-11.2 at Y 32.05), 16.4 at the back (45 deg sides). Lower window u 38.75-50.55, upper window u 60.4-72.2. On the RimClip the upper window runs out through the block top |
| Cheek tops (top of each slot zone) | u 38.75 and u 60.4 (0.35 mm above each lug top) |
| Detent finger, saddle | Flexes in Y. Runs along X, root at -X: X -7.0 to 7.0, Y 35.05-36.45 (1.4 thick), Z 28.5-34.5 (6 wide). 0.6 mm gaps round it (pocket X -6.5 to 7.6, Y 35.05-37.05, Z 27.9-35.1). Bump on its free end (X 3-6.5): 45 deg triangle, apex Y 34.3 at Z 31.5, so 0.4 mm interference with the lug tip |
| Detent finger, RimClip | Same section, but runs along Z, root at the top: X +-4 (8 wide), Y 35.05-36.45, Z 28.5 (free end) to 44.5 (root). Pocket X +-4.6, Y 35.05-37.05, Z 27.9-44.0. Bump X +-3.5, same profile at Z 31.5 |
| Saddle plinth relief | 45 deg chamfer on the back plate's lower inner edge (plane Z = 23.15 - (Y - 31.7)): cuts at most 4.8 mm at Y 32.05, nothing behind Y 36.85. The heel pad is untouched |
| RimClip block | Extended down from Z 30 to Z 23.5 (X +-15, Y 32.05-38.2). Rim hook, pads and glass-side face unchanged |
| Hung position | Unchanged in the model: the node did not move, and the lower lug bottom sits exactly on the stop. Rim top 17.2 mm above the roof as modelled. On the 45 deg stop the node can settle at most 0.35 mm down and in, so 17.2-17.55 as hung (the old cleat gave 17.5-17.7). About 0.15-0.5 mm higher than before |

### Lift and clearance numbers

| | mm |
| --- | --- |
| Minimum vertical lift before the lugs are clear of the slots (into the windows) | **8.65** |
| Lift needed to pull the node straight back towards the room, horizontally | **11.0** (the cheek tops slope 45 deg, so a horizontal pull needs the extra lift; lifting 8.65 and pulling out on a 45 deg up-and-out line also works) |
| Hard stop (lug top meets the window ceiling) | **12.15**. The instruction is "lift until it stops, then pull straight out" (1.15 mm margin, measured) |
| Horizontal travel to clear the slot | about 3-4 mm (lug depth 2.65 + 0.35 clearance) |
| Clear height needed above the back plate / rim | **0**. At the stop, the roof is at Z 74.95, 5.05 mm below the saddle's rim top (Z 80). Nothing has to pass over the back plate. On the RimClip the upper window is open at the top anyway |
| Plinth to saddle at the top of travel | 0.99 mm (measured; the 45 deg relief runs parallel to the plinth chamfer, and the gap grows as the node moves out) |
| Plinth to RimClip at the top of travel | 1.87 mm (measured) |
| Minimum part-to-part gap, seated and lifted 0.5 mm | 0.35 mm (sleeve back to the slot face; same on the saddle and the clip) |
| Pull-out at the stop (12.15 up, 2.6 out) | No interference. Nearest gap 1.15 mm (upper lug bottom to the upper cheek top) |

## Fitting and removing (for Brian)

Fitting:
1. Hold the node upright with its back to the saddle (or clip), about 12 mm higher than where it ends up. Its roof is then roughly 5 mm below the top of the rim. Hold it a few mm out from the saddle.
2. Line up the two blocks on the back of the node with the two open pockets in the saddle face. Push the node straight back until its back touches the saddle.
3. Let it drop. It slides down about 12 mm, you feel a small click near the bottom, and it stops on the bottom ledge.

Removing:
1. Push the node straight up until it stops (about 12 mm). You feel the click let go on the way up.
2. Pull it straight towards you about 4 mm, then lift it away.

(Lifting only about 9 mm and pulling out at an angle, up and out together, also works.)

## Strength (hand calculations; node about 110-115 g = 1.1 N, plus a 20 N push down = 21 N)

- **Main bottom stop** (lower lug on the 45 deg ledge): projected area about 33 mm2. 21 N / 33 mm2 = 0.6 MPa bearing. The ledge sits on solid plate (saddle) or on the 3.5-6.5 mm solid block below the slot (clip). Its 45 deg slope pushes the node in towards the wall, so it seats rather than slips out.
- **Lug root on the sleeve wall** (8 x 8 mm root): shear 21 N / 64 mm2 = 0.3 MPa. Bending 21 N x 1.5 mm / (8 x 8^2 / 6) = 0.4 MPa. PETG across layers is about 20 MPa, so the safety factor is above 40.
- **Dovetail flanks** (pull-off and knocks): each flank contact is about 8 x 4.2 mm, 34 mm2, and there are 4 flanks. A 20 N pull straight off gives 0.15 MPa bearing. The cheek lip over each flank (3 mm deep, 8 mm long) sees about 0.6 MPa bending at 5 N per lip.
- **Node moment**: CoM about Y 12, 19.7 mm outboard of the back wall, so about 22 N.mm. The upper lug flanks and the lower back contact take it. Negligible.
- **Upper shelf**: only 1.2 mm (0.85 mm normal) and cantilevered about 3 mm. If it carried the full 21 N it would see about 15 MPa (side-printed saddle, along the layers: OK). On the clip (Z layers, partly across the layers) the safety factor would only be about 1.5-2. That is why it has the 0.3 mm gap: normally only the lower stop is loaded.
- **Detent finger** (PETG, E about 2 GPa, 0.4 mm interference): saddle about 2.3 N at the bump (L 11.3 mm, 6 x 1.4 mm), clip about 2.2 N (L 12.5 mm, 8 x 1.4 mm). Peak strain 0.6-0.7 % (PETG yields at about 4 %), so it will not take a set. With 45 deg ramps and friction 0.3, it takes about 4 N on top of the node's own weight to lift past the click (about 5 N in total, half a kilogram-force), and about 3 N of push to seat it. Hand-removable, but a knock has to beat about 5 N upwards. The bump rides the lug tip for about the last 7 mm of the drop, which is light drag.
- **Plate behind the finger pocket**: 1.15 mm skin (Y 37.05-38.2) over about 9 x 7 mm (saddle) or 9 x 16 mm (clip). It carries no load: the wall pads (saddle) and the glass pad (clip, Z 62-78) are elsewhere.

## Print table (all plain PETG, no supports)

| File (this folder) | Part | Orientation | Bridges and overhangs |
| --- | --- | --- | --- |
| tidemark_sleeve_dovetail_PETG_roof-down.stl | Sleeve | Roof down (as before) | Lug top faces 45 deg (grow out of the wall). Lug bottom faces face up. Detent groove: one side faces up, the other is 45 deg. Lug sides (flanks) are vertical. Everything else unchanged (brow 20 deg, plinth 45 deg, key/eye holes). No bridge added |
| tidemark_perch_saddle_dovetail_PETG_side-down.stl | Perch saddle | On its -X side (as before) | Slot +X flank 45 deg, window +X sides 45 deg. All the u-planes (stops, cheek tops, ceilings, shelf) and the plinth relief print as vertical walls. The detent finger stands upright (root at the bed side). Its pocket ceiling at X 7.6 is a small 2.0 x 7.2 mm span closed on three sides; the bump underside is a 0.75 mm overhang. The old 45 deg cheek slope (Extrude6) is still in the timeline but now buried in the refill |
| tidemark_rimclip_12mm_dovetail_PETG_hook-top-down.stl | 12 mm RimClip | Hook top down (as before) | Bottom stop and cheek tops are 45 deg overhangs, window ceilings face up, flanks and windows vertical. The upper window is open at the top. The detent finger stands upright (root at the bed side). Its pocket bottom is a 9.2 mm bridge between two walls. **The old 24.7 mm lip bridge is gone** (NOTES Q10 closed). The block bottom (Z 23.5) faces up |

Re-import check (scratch design, closed without saving):

| File | Closed / oriented | Triangles | Volume mm3 | X / Y / Z range (print frame) |
| --- | --- | --- | --- | --- |
| Sleeve | yes / yes | 1 702 | 33 803 (was 33 661) | X -25.93..25.93, Y -37.7..15.5, Z -62.8..0.5 |
| Perch saddle | yes / yes | 3 176 | 64 288 (was 65 587) | X -88..80, Y 32.05..72.7, Z -15..21 |
| 12 mm RimClip | yes / yes | 156 | 8 089 (was 7 848) | X -15..15, Y -56.2..-32.05, Z -83..-23.5 |

As before, the STLs keep model coordinates (the slicer drops them to the bed). They were exported from Move features that were then deleted, and opened only in Fusion, not in a slicer. Settings are as in NOTES.md and PERCH.md. Use 100 % infill (modifier) round the slot and the detent pocket on the saddle and the clip, so the finger and the 1.15 mm skin are solid.

## Checks done (v31)

- assembly_inspect_interference, hung, Perch: Sleeve, Perch_Saddle, FootCap, SMA_Boot, Key_LightPipe, USB_Bung, Reference_Parts, Perch_Wall19, Perch_Collet, Perch_Clamp, Perch_Ref. No overlap. Sleeve/Saddle 0 volume (lug on the stop, intended). The other contacts are the old ones (pads on the wall, screws in holes, FootCap/USB_Bung, FootCap/Reference_Parts, Sleeve/Key_LightPipe, pigtail/bulkhead 0.0083 cm3).
- Same, hung, RimClip set: no overlap. Sleeve/RimClip 0 (stop). RimClip/RimClip 0 is the pads on the body face.
- Top of travel (node up 12.15; sleeve, cap, boot, key, bung, reference parts), with both the saddle and the clip: Sleeve 0-volume contact only (lug touching the window ceiling, intended). Saddle/RimClip and RimClip/Wall19 overlap only with each other (they share a position; not a real case).
- Straight pull-out at the top of travel (up 12.15, out 2.6): no interference with the saddle or the clip.
- Up 8.7 (minimum lift): no interference, min gap 0.35 mm.
- model_measure_between: listed in the lift table above. Upper lug to the shelf: 0.212 mm normal on both the saddle and the clip.
- Plinth never meets the saddle or clip during fitting: 0.99 / 1.87 mm at the top of travel, larger everywhere else on the path.
- Timeline: recompute with 0 errors after every stage.

## Not checked / limits

- Boards and nested occurrences were not in the interference runs (all changes are outside the sleeve).
- No slicer preview. Support-free is judged by face angles.
- Detent force is a beam estimate. Real feel depends on the printed bump height. If it is too stiff, sand the bump; if too soft, add a layer of tape on it. Not test-printed.
- Friction and wear of PETG-on-PETG flanks; creep of the stop under long-term load (very low stress).
- Berth (block-out, v25-v26) was left alone, as asked. The Sleeve component is shared, so the Berth's second node (Sleeve:2) now also has the rail. Berth_Plate and Berth_Hold_Saddle still have the old cleat receiver and no longer match. Update them only if Berth comes back.
- The hw_* / build_* / assembly guide pictures and tidemark_iso.png / tidemark_section_stack.png still show the cleat. They were not re-rendered. ASSEMBLY.md step 13 still describes the cleat.
- The review STEP in shared\handoff was not re-exported.
- The old cleat features were suppressed (sleeve Cleat, RimClip Extrude7) or filled in (saddle Extrude5/6 stay, with a join on top), not deleted. They can be deleted later.

## Open questions for Brian

1. Is about 5 N (half a kilogram-force) of upward push to unclick the detent right? It can be made lighter (a smaller bump) or the detent dropped.
2. Is "lift until it stops (12 mm), pull straight out" OK? The minimum is 8.65 mm if you pull out at an angle.
3. The upper shelf (1.2 mm) and the skin behind the detent pocket (1.15 mm) are under the 2 mm wall rule. They carry no load in normal use. Accept, or thicken (that costs lift height or detent travel)?
4. Re-render the assembly guide pictures (step 13 and the clip/saddle pictures) for the dovetail?
