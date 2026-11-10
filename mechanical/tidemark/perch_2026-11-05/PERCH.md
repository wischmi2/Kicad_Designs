# Perch rim saddle for the Tidemark node (probe on an inner leg), 2026-11-05

Status: CHOSEN by Brian 2026-11-05 (Perch for now, Berth parked). Model and STLs done (v22-v24); open questions below.

Fusion document: `nrf54l15_feather_enclosure_tidemark` (project Fish_Stuff / nRF54L15_Feather), started from v21.
Versions: **v22** = stage 1 (Perch components modelled), **v23** = stage 2 (print STLs exported from temporary rotations, rotations deleted again; geometry as v22), **v24** = stage 3 (renders and the Perch STEP; view and visibility state only, geometry as v22).
Perch is added as new components. The sleeve, foot cap, sled and the existing 12 mm RimClip were not changed. The RimClip sits in the same place as the Perch saddle, so it is hidden (view state only) and left out of the Perch interference runs. LeafFrame is hidden too: it lies flat beside the model at X 60-160 and touches the reference wall slab.

## What the parts are

| Part | Printed? | What it does |
| --- | --- | --- |
| Saddle (Perch_Saddle) | PETG | Hooks over the sump wall. Outside: back plate with the same cleat pocket as the RimClip, so the Tidemark sleeve hangs on it unchanged, plus two pads on the outside face of the wall. Top: an 8 mm bridge. Inside: a 160 mm leg with the clamp screw at the top, a dovetail rail and a row of stop holes for the Collet, and two snap clips for the cable |
| Collet (Perch_Collet) | PETG | Probe holder. Slides on the leg's rail, held between two stop screws. Split clamp round the 12 mm probe, closed by one nylon M4 screw |
| Pad (Perch_Clamp / Perch_Pad) | PETG | 18 x 4 mm disc on the thumbscrew tip; it is what presses on the inside face of the wall |
| Hardware | bought | M6 x 30 nylon thumbscrew + M6 nylon nut (wall clamp); M4 x 25 nylon screw + M4 nylon nut (Collet clamp); 2 x M4 x 10 nylon screws (Collet stops) |

Reference bodies (not printed): the 12 x 116 probe, the screws and nuts (Perch_Ref, Perch_Clamp), a 19 mm and a 6 mm sump wall slab (Perch_Wall19, Perch_Wall6) and the water at its normal level (Perch_Water).

## Decisions

- **Wall-thickness adjustment: one nylon M6 thumbscrew with a printed pad**, through the top of the inner leg, 10 mm under the rim top. It presses the wall against the two pads on the back plate. Picked over shims because:
  - it covers 6-19 mm without steps, using one part;
  - there are no loose shims to lose in the sump or mix up;
  - the node's position outside does not change with wall thickness, so the cable route and the bearing pad stay where they are;
  - it is set and checked from the sump side with one turn.
  The nut is a captive nylon M6 nut in a hex pocket in the leg.
- **Datum = the outside face of the wall** (Y 39.7, the same as the RimClip). The back plate and the node always sit in the same place. The leg is fixed relative to that face, so the probe's distance from the inside face depends on the wall: 26 mm at 19 mm, 39 mm at 6 mm (see question 1).
- **Probe depth: the Collet slides on a 45 deg dovetail rail on the leg and sits between two stop screws** (10 holes at 10 mm pitch: coarse, +-30 mm). Fine adjustment comes from sliding the probe in the Collet. The leg slot was replaced by a rail and stop holes because a 60 mm slot through a leg printed on its side would be a 60 mm bridge. Sliding the probe alone would move the grip away from the probe top by up to 60 mm.
- **The saddle prints on its side** (-X face on the bed). The whole hook profile (back plate, bridge, leg) then lies in the layers, so neither the clamp nor the node's weight loads the layer lines in tension (see the print table).
- **Rim height:** the bridge underside (rim top) is at Z 80, 17.2 mm above the roof as modelled and 17.5-17.7 mm as hung. This is the same as the RimClip, so the node's roof stays below the rim top.

## Model frame and key dimensions

Frame as in NOTES.md: Z up, roof Z 62.8, sleeve back wall Y 31.7, cleat Y 31.7-34.7 / Z 52-60. The room is at -Y and the sump at +Y. The outside face of the wall is at Y 39.7, the rim top at Z 80 and the water at Z -72 (152 mm under the rim top).

| Item | Value |
| --- | --- |
| Wall clamp range | 6-19 mm as designed. The screw can reach 0-19 mm; at 19 mm there is 1.0 mm between the leg and the wall |
| Saddle | 30 wide (36 over the cable clips) x 40.65 deep x 168 tall; Z -80 to +88 |
| Back plate | Y 32.05-38.2 (6.15 thick), Z 18-88 |
| Cleat pocket | Copied from the RimClip: 24.7 wide (X +-12.35), lip bevel 45 deg from (Y 32.05, Z 54.155) to (Y 35.05, Z 51.155), back wall Y 35.05, 3.15 mm of plate behind. Clearance to the cleat 0.35 mm (measured). Open toward the room up to a ceiling at Z 67 (cleat top Z 60, 63 when lifted to fit) |
| +X cheek | Inner face is a 45 deg slope from (X 12.35, Y 35.05) to (X 15, Y 32.4), over Z 51.155-67 (overhang fix for the side print). The cleat's lateral play is 0.35 mm at -X and 0.35-0.7 mm at +X |
| Wall pads (on the back plate) | 1.5 mm proud, full width. Top Z 70-78, low (heel) Z 18-27. Lever between them about 52 mm |
| Bridge | Y 32.05-71.7, Z 80-88 (8 thick). Outer corners R5, +X top edge R3 (cable rest), inner corner R1.5 |
| Leg | Wall face Y 59.7. 12 thick (Y 59.7-71.7) from the bridge down to Z 58, then 8 thick (Y 59.7-67.7) down to Z -80 (160 mm under the rim top) |
| Clamp | M6 hole at (X 0, Z 70), teardrop 6.4. Pad pocket teardrop 19, Y 59.2-63.7. M6 nut pocket 10.3 AF, Y 66.5-72.2. Thumbscrew tip travel Y 46.7 (6 mm wall) to 59.7 (19 mm wall) |
| Rail | 45 deg dovetail on the leg's sump face: 8 wide at the root (Y 67.7), 18 wide at the top (Y 72.7), Z -80 to +20 |
| Stop holes | 10 x dia 3.4 (self-tapping for nylon M4) at X 7, Z -75, -65, ... +15; 10.3 deep from the rail top, ending 3 mm short of the wall face |
| Collet | X +-13 x Y 68-100 x 22.5 tall. Channel 0.3 mm clearance to the rail (measured 0.30). Bore 12.3 at (X 0, Y 84.7), 1.6 mm split, M4 clamp across the split at Y 95 |
| Probe axis | 26.0 mm off the inside face at a 19 mm wall, 39.0 mm at a 6 mm wall. Probe surface to the wall: 20.0 mm (measured, 19 mm wall) to 33 mm |
| Cable clips | C1 on the leg's +X face, Z 58-66. C2 on the back plate's +X face, Z 36-44. Each is a 3.6 mm channel with a 2.6 mm snap mouth (0.5 mm lips at 45 deg), posts standing 6 mm out of the face |

### Probe depth (middle setting: lower stop at Z -45, upper stop at Z -15)

| | Z | Below the rim top | Relative to the normal water level |
| --- | --- | --- | --- |
| Collet | -41.5 to -19 | 61-99 | 30.5-53 above |
| Probe top (cable end, 8 mm above the Collet) | -11 | 91 | 61 above |
| Probe tip (sensing end) | -127 | **207** | **55 under** |

So 55 of the 116 mm (47 %) is under water at the normal level, and 61 mm stays above water.
- **Coarse adjustment:** move both stop screws together: lower stop from Z -75 to Z -15, upper stop 3 holes higher. That moves the tip **+-30 mm in 10 mm steps**: 177-237 mm under the rim top, 25-85 mm under the normal water level.
- **Fine adjustment:** slide the probe in the Collet. It can go down about 5 mm (keeping about 3 mm of the probe top above the Collet) and up about 55 mm (keeping 30 mm of the sensing end below the Collet). The Collet never covers the bottom 30 mm.
- **Overall:** the tip can sit about 120-240 mm under the rim top.
- **At the deepest coarse setting:** the Collet bottom is at Z -71.5, just above the normal water level, and the leg end (Z -80) is 8 mm under water.

## Print table (all plain PETG, support-free in the stated orientation)

| File | Part | Orientation | Supports | Bridges and overhangs |
| --- | --- | --- | --- | --- |
| tidemark_perch_saddle_PETG_side-down.stl | Saddle | Lying on its -X side (the face with no clips). The clips, rail flank and sloped cheek face up | None | The profile (hook, bridge, leg, pocket, lip bevel, pads, fillets) prints as vertical walls. Rail: lower flank 45 deg, upper flank faces up. Pocket: +X cheek slope 45 deg. Clamp hole and pad pocket are teardrops pointing up; the M6 nut pocket is a hex with a vertex up (60 deg faces). Clip lips 45 deg. **Bridges:** the 10 stop holes, dia 3.4, horizontal, 3.4 mm span. Footprint 168 x 40.65, height 36. Layers run along the hook profile, so the clamp and the node's weight act along the layers, not across them |
| tidemark_perch_collet_PETG_bottom-down.stl | Collet | Bottom face down, bore vertical (as modelled) | None | All walls vertical. **Bridge:** the M4 clamp hole, dia 4.4, horizontal, 4.4 mm span. M4 nut pocket is a hex with a vertex up |
| tidemark_perch_pad_PETG_wallface-down.stl | Pad | Wall face down, screw hole up | None | None |

Re-import check (scratch design, closed without saving):

| File | Closed / oriented | Triangles | Volume | Z range (print) | X / Y range |
| --- | --- | --- | --- | --- | --- |
| Saddle | yes / yes | 3 074 | 65 587 mm3 | -15.0 to 21.0 (36) | X -88 to 80, Y 32.05 to 72.7 |
| Collet | yes / yes | 910 | 13 629 mm3 | -41.5 to -19.0 (22.5) | X -13 to 13, Y 68 to 100 |
| Pad | yes / yes | 660 | 933 mm3 | 58.7 to 62.7 (4.0) | X -9 to 9, Y -79 to -61 |

The STLs keep model coordinates (the slicer drops them to the bed); the orientation is right as exported.

Suggested settings: as the Tidemark sleeve (0.2 mm layers, 4 perimeters, 30-40 % gyroid, 240 C / 75 C). Use 100 % infill (modifier) round the M6 nut pocket and the clamp hole, and round the stop holes, since the nylon M4 screws self-tap there. A 5 mm brim on the saddle is optional; it has a large flat base. Rough material: saddle 66 cm3 solid (about 50 g printed), Collet 14 cm3 (about 12 g), pad 1 cm3.

TPU: no TPU part in this draft. A TPU pad and a TPU split sleeve in the Collet (11.5 bore) are later items; nothing in the PETG parts blocks them (the pad pocket and bore would take a TPU pad or sleeve of the same outside size).

## Hardware (Amazon-type nylon; sizes to buy)

| Qty | Item | Use |
| --- | --- | --- |
| 1 | Nylon M6 x 30 knurled thumbscrew (head about 18-20 dia x 8; any head up to 20 dia fits) | Wall clamp. M6 x 25 is too short at a 6 mm wall; M6 x 35 also works (sticks out 5 mm more into the sump) |
| 1 | Nylon M6 hex nut, 10 mm AF x 5 | Captive in the leg's hex pocket (sump side) |
| 1 | Nylon M4 x 25 pan head screw | Collet clamp. M4 x 30 also works (tip 4 mm past the nut) |
| 1 | Nylon M4 hex nut, 7 mm AF x 3.2 | Captive in the Collet (-X side) |
| 2 | Nylon M4 x 10 pan head screws (head about 7 dia) | Collet stops, self-tapping into the 3.4 mm holes |
| optional | Silicone o-ring, 12 mm ID | Depth mark on the probe above the Collet, so the depth comes back after calibration |
| optional | Hook-and-loop cable tie | For the spare cable (about 0.55 m) |

No metal near the water: everything in or over the sump is PETG or nylon.

## Assembly and install

1. Press the M6 nut into the hex pocket on the leg's sump face, and the M4 nut into the Collet's hex pocket. A drop of CA holds each if they are loose.
2. Turn the thumbscrew in from the sump side until about 3 mm of thread shows in the pad pocket on the wall side. Push the pad on (its blind hole is 6.0 x 3 deep). A dab of silicone keeps it on while the saddle is off the wall; once clamped, the wall traps it.
3. Slide the Collet onto the rail from the bottom end of the leg. Screw a stop (M4 x 10) into the chosen hole; the middle setting is the 4th hole from the bottom (Z -45). Let the Collet sit on that stop, then fit the second stop 3 holes higher.
4. Back the thumbscrew out. Hang the saddle over the sump rim with the back plate outside, so that both outside pads touch the outside face of the wall. Tighten the thumbscrew finger-tight. Do not use a tool: about 50-100 N is plenty.
5. Hang the node as on the RimClip. Hold it with its back about 3 mm in front of the back plate and the cleat just above the pocket, move it back, and let it drop about 3 mm onto the lip.
6. Push the probe in from above through the Collet, tip first, until its top is about 8 mm above the Collet. Tighten the M4 clamp lightly; the probe must not turn by hand. Slide the o-ring down onto the Collet as the depth mark.
7. Cable route (1 m probe cable to the boot under the node's heel):
   - Up from the probe top and snap the cable into C1 on the leg's +X side.
   - Over the bridge along its rounded +X edge (R3), then down the back plate's +X side into C2.
   - From C2, outward past the foot's +X corner. The cable is clear of the sleeve and the wall there: the sleeve back is at Y 31.7 and the wall at 39.7, and the cable runs at Y 33-37. The plinth flares out to Y 37.7 below Z 9.5, so the cable must be outside X 26 by then.
   - Down to about 20-30 mm below the boot, then back up into the boot (the drip loop), plug in the SMA and fit the boot.
   - Coil the spare (about 0.55 m) loosely with a tie below the drip loop. Keep bends above about 15 mm radius. The bend over the bridge is about 14 mm radius as routed, so let it arc a little higher if the cable is stiff.
8. To calibrate: loosen the M4 clamp and lift the probe out upward; the Collet stays at depth. To move the depth by 10 mm steps, take out the upper stop, slide the Collet, and refit both stops.

## Load estimate (hand calc)

Node mass, from the model volumes × PETG at 1.27 g/cm3 (solid; a real print with infill is a little lighter):

| Item | Volume | Mass |
| --- | --- | --- |
| Sleeve | 33.67 cm3 | |
| Foot cap | 11.90 cm3 | |
| Sled | 6.31 cm3 | |
| Key and light pipe | about 1 cm3 | |
| PETG total | 52.9 cm3 | about 67 g |
| Boards and battery (given) | | 30 g |
| Brass inserts, nylon standoffs, SS foot-cap screws | | about 6 g |
| Pigtail, bulkhead, boot | | about 10 g |
| **Node total** | | **about 110-115 g (1.1 N)** |

The node's centre of mass is at about Y 12 (sleeve CoM Y 12.05, cap Y 12.6), which is 27.7 mm outboard of the outside face of the wall.

Moments about the rim:

| Load | Moment |
| --- | --- |
| Node, outboard | 1.13 N × 27.7 mm = 31 N·mm |
| Saddle, inboard (66 cm3, about 65-83 g, CoM Y 58.2, 18.5 mm inboard) | 12-15 N·mm |
| Collet + probe, inboard (17 g + about 40 g assumed, Y 84.7, 45 mm inboard) | about 25 N·mm |

- With the probe fitted, the net is about 9 N·mm toward the sump. Without the probe and Collet, it is about 16-19 N·mm outboard.
- Across the 52 mm between the two outside pads, that is under 0.4 N at the pads. The node itself hardly loads the rim, and the heel pad stops the twist even with the thumbscrew loose.
- A 20 N push down on the node: 20 × 27.7 = 554 N·mm, or about 11 N at the pads. Fine.

Section stresses:
- **Thumbscrew clamp** (the largest load; finger-tight about 50-100 N, 150 N assumed as a hard twist):
  - Bridge (30 × 8, Z = 320 mm3): M = 150 × 14 = 2 100 N·mm, so 6.6 MPa.
  - Leg root (30 × 12, Z = 720 mm3): 150 × 10 / 720 = 2.1 MPa.
  - The top pad sits directly opposite the screw (Z 70-78 vs 70), so the back plate at the cleat pocket carries mostly the node's moment, which is tiny.
- **Leg, side knock:** 10 N on the probe tip, about 215 mm below the bridge, gives 2 150 N·mm at the leg root:
  - 6.7 MPa for a knock toward or away from the wall (30 × 8 section);
  - 1.8 MPa for a sideways knock.
  - The leg end deflects about 5 mm under that 10 N (E about 2 GPa). The leg is springy but will not break.
- **Cleat:** the same geometry and load as the RimClip (1.1 N on a 24 mm bevel).
- **Margin:** PETG along the layers is about 40-50 MPa, so the safety factor is above 6 at a hard 150 N clamp. In the side print, all of these loads act along the layers. The only cross-layer loads are the clip snap force and the cleat's sideways location, and both are small.
- **Verdict:** the leg and saddle are strong enough in PETG at these sections. The real risks are over-tightening the nylon thumbscrew and creep of PETG under a constant clamp. Re-check finger-tightness after a week.

## Interference and fit checks

assembly_inspect_interference:

| Run | Occurrences | Result |
| --- | --- | --- |
| 19 mm wall, v22 | Perch_Saddle, Perch_Collet, Perch_Clamp, Perch_Ref, Perch_Wall19, Sleeve, FootCap, SMA_Boot, Reference_Parts, LeafFrame, Key_LightPipe, USB_Bung; coincident faces included | **No overlap between any Perch part and the sleeve, foot cap, boot, key or bung.** Zero-volume contacts only, all intended: pads on the wall (Saddle/Wall19, Clamp/Wall19), screws and nuts in their holes (Saddle/Ref, Collet/Ref, Clamp/Ref, Ref/Ref, Clamp/Clamp). Known older ones: Sleeve/Key_LightPipe 0, FootCap/Reference_Parts 0, FootCap/USB_Bung 0, Reference_Parts self 0.0083 cm3 (pigtail vs bulkhead). One artefact: Wall19 slab vs LeafFrame 0.21 cm3 (the leaf card is laid out flat at X 60-160 beside the model; it is not a real conflict) |
| 6 mm wall, v22 (Perch_Clamp moved -13 mm in Y, not captured, discarded afterwards) | Perch_Saddle, Perch_Collet, Perch_Clamp, Perch_Ref, Perch_Wall6, Sleeve, FootCap, SMA_Boot | No overlap. Zero-volume contacts only (saddle pads on the wall, screws and nuts). The pad touches the 6 mm wall (model_measure_between 0.0 mm) |

Measured gaps:
- saddle to sleeve 0.35 mm (cleat lip);
- saddle to foot cap 18.5 mm. The back plate ends at Z 18, 8.5 mm above the top of the plinth chamfer, so lifting the node 3 mm to unhook is clear;
- Collet to saddle 0.30 mm;
- probe to the 19 mm wall 20.0 mm.

Visual check (perch_side.png at 19 mm, perch_side_wall6.png at 6 mm): at both walls the node hangs the same; the leg clears the inside face (1 mm at 19, 14 mm at 6); the thumbscrew head stays above the probe and the Collet; the probe is vertical, half under water, 20 mm (19 wall) or 33 mm (6 wall) off the wall.
Not checked: the boards (nested occurrences) were not in the runs, but the Perch parts are all outside the sleeve.

## Renders (this folder)

- perch_iso.png: node, saddle, Collet and probe on a 19 mm wall section, with the water box at the normal level.
- perch_side.png: side view (from +X), 19 mm wall, water line and probe depth.
- perch_side_wall6.png: the same at a 6 mm wall, clamp screw run in.
- perch_parts.png: saddle (room side, cleat pocket, cable clips), Collet, pad and thumbscrew.
- perch_parts_sump_side.png: the same parts from the sump side and below (rail, clamp, Collet).

STEP of the Perch parts (saddle, Collet, pad, thumbscrew; not for printing): C:\Personal-Agents\shared\handoff\nrf54l15_feather\enclosure\tidemark_perch_parts_2026-11-05.step (182 kB, exported from v23 geometry). The node itself is in tidemark_draft_assembly_2026-11-05.step in the same folder (unchanged).

## Not done / limits

- No slicer preview; the support-free check is by geometry (face angles listed above).
- The probe storage-cap peg, the type band and the TPU pad/sleeve from the concept were not modelled.
- The cable is not modelled; the route above is checked against the geometry by hand only.
- The Collet's split clamp is PETG gripping the probe directly (bore 12.3 on a 12.0 probe). The clamp has not been tested; if it slips, or marks the probe, add a 0.5 mm TPU or tape wrap.
- The stop holes self-tap nylon M4 into PETG. After many moves they may wear; then drill them to 4.2 and use printed pins, or move one hole along.

## Open questions for Brian

1. **Probe offset:** the axis is 26 mm off the inside face at a 19 mm wall but 39 mm at a 6 mm wall, because the clamp references the outside face. What is your sump wall? If it is about 6-12 mm, I can move the leg 7-13 mm toward the wall (one sketch line; the wall range then drops to about 6-12 mm) to get about 25 mm.
2. **Sump floor:** the tip is 207 mm under the rim top at the middle setting and 237 mm at the deepest. How deep is the sump at this spot (the tip should be at least 20 mm off the floor)?
3. **Rim:** is there a clear, flat rim at least 30 mm wide, with no euro-brace, lid or hood over it? Is the outside face flat for about 62 mm below the rim (for the low pad)?
4. **Cable outside diameter:** the clips are sized for about 3-3.5 mm (3.6 channel, 2.6 mouth). Is the Atlas cable thicker?
5. **How far does the sump rise when the return pump stops?** At the middle setting the Collet bottom is 30 mm above the normal level; the leg end is 8 mm under it.
6. **Room outside:** the node hangs 81 mm below its roof (plus the 21.5 mm boot and the drip loop) on the outside of the sump. Does that fit in the cabinet at this spot?
7. Print the PETG pad as is, or wait for a TPU pad?
