# Berth block-out for the Tidemark node (visual look-and-size model), 2026-11-05

Status: modelled and checked (stages 1 and 2 done). This is a block-out for comparing with Perch, not printable parts. No STL, no STEP, no 3mf, nothing sent to a slicer or printer.

Fusion document: `nrf54l15_feather_enclosure_tidemark` (project Fish_Stuff / nRF54L15_Feather), started from v24.
Versions:
- **v25** = stage 1: all Berth parts modelled. The post, the clamp ring, the cabinet wall and the ghost probe have wrong colours in v25 (appearance only; colours were applied to the wrong bodies).
- **v26** = stage 2: colours fixed, the cable added (swept, 618 mm), renders. Use v26.

No geometry of the sleeve, foot cap, sled, RimClip or any Perch component was changed. The Berth node and the Hold use second occurrences (instances) of the same components; the Berth parts are new components (prefix Berth_). The existing Perch setup is at X 0, the Berth Hold at X 200 and the Berth wall station at X 560. The RimClip, LeafFrame and Perch_Wall6 are still hidden as in v24.
Check made after a slip: a cut I made for the receiver pocket also cut the shared Sleeve (it touched the second node). I deleted that feature straight away and re-did the cut scoped to the plate only. Sleeve volume afterwards is 33 666 mm3, the same as the 33.67 cm3 in NOTES.md, and the cleat is intact.

## What is in the model

| Component | Colour | What it is |
| --- | --- | --- |
| Berth_Plate | Abyss navy | Wall plate 80 x 195 x 5 (X 500 to 580, Z -115 to 80, Y 38.2 to 43.2) with the cleat receiver and two keyholes |
| Berth_Tower | Abyss navy | Spine, cup socket block, clamp arm (one body) |
| Berth_Post | Abyss navy | Cable post (bobbin) with its web to the plate |
| Berth_TPU | graphite | Drip tray + soaker cup (one body in the model, two parts in a real build) and the clamp ring |
| Berth_Ref | cabinet wall and ghost probe translucent; cable black | Cabinet wall slab, the ghost probe in the cup, the 1 m cable |
| Berth_Hold_Saddle | navy (PCTG blue) | The Hold saddle: an independent copy of Perch_Saddle with the node back plate cut away |
| Sleeve:2, FootCap:2, Sled:2, Key_LightPipe:2, USB_Bung:2, SMA_Boot:2, Reference_Parts:2, Hardware_Ref:2 | sleeve navy, cap, boot and bung graphite | The second Tidemark node at X 560, same pose as in Perch. The boards are not instanced (they sit inside the sleeve and are not visible) |
| Perch_Collet:2, Perch_Clamp:2, Perch_Ref:2 (probe, thumbscrew, nuts), Perch_Wall19:2, Perch_Water:2 | as Perch | The Hold's collet, thumbscrew and pad, the 12 x 116 probe, the 19 mm sump wall slab and the water box at X 200 |

The Perch node itself is still the plain pale draft colour (I did not touch its appearance), so the Berth node (navy) looks different from it in perch_vs_berth.png. That is colour only.

## Key sizes

Frame as in NOTES.md and PERCH.md: Z up, node roof Z 62.8, room at -Y, wall/sump at +Y.

**Wall plate and node**

| Item | Value |
| --- | --- |
| Plate | 80 W x 195 H x 5 thick. Top at Z 80, the same height as the sump rim top (Z 80 in Perch). Bottom Z -115 |
| Cleat receiver | A copy of the RimClip receiver: block 30 wide, Y 32.05 to 38.2, Z 30 to 64, pocket 24.7 wide with the 45 deg lip from (Y 32.05, Z 54.155) to (Y 35.05, Z 51.155), back wall Y 35.05, 0.35 mm clearance to the cleat. The node hangs exactly as on the RimClip and the Perch saddle (the node sits in the same pose relative to the receiver) |
| Keyholes | Two, 10 mm head hole plus 5.5 mm slot going down 12 mm, 60 mm apart (X 510 and 570), at the top of the plate (hole centres Z 70, 10 mm below the top). Nothing at the bottom yet |
| Node position | Node axis X 560; plate runs X 500 to 580, so the node is 20 mm from the plate's right edge and the tower is on the left. The foot cap plinth (X +-26) overhangs the plate's right edge by 6 mm (the plinth is in front of the plate, no clash) |
| Node height | Roof 17.2 mm under the plate top; the boot ends at Z -40, which is 75 mm above the plate bottom |
| Overall station | 80 W x 195 H; depth from the plate back (Y 43.2) to the node's foot front (Y -15.5): 58.7 mm. Without the plinth the tower front is at Y -2 (tray), 45.2 mm. The concept said 62 x 36 x 190, so the real station is 80 wide and about 1.6 times as deep |

**Tower (X 502 to 532, 30 wide; the concept said 28)**

| Item | Value |
| --- | --- |
| Spine | X 502 to 532, Y 32 to 38.2 (6.2 thick), Z -100 to 52 (152 tall) |
| Probe axis | X 517, Y 14.2. The back of the probe is 18.0 mm in front of the plate (the concept said 18 mm) |
| Parked probe | Z -108 (tip) to +8 (cable end), 116 long |
| Upper clamp | A navy arm (X 502 to 532, Y 26.2 to 32, Z -8 to 6) and a graphite TPU ring, OD 24, ID 12.4, 14 tall, Z -8 to 6. The ring grips the top part of the parked probe |
| Cup socket | Navy block X 502 to 532, Y 0.2 to 32, Z -100 to -70 with a 26.4 mm bore. The cup passes through it |
| Soaker cup (graphite TPU) | OD 26, ID 22, floor 3, 68 tall (Z -113 to -45). Inner depth 65, **brim volume 24.7 ml**. Sits on the tray floor |
| Cup fill | A 35 mm fill line (about 9 ml net of the probe) leaves the tip and 33 mm of the probe in liquid. The tip is 2 mm above the cup floor. At the brim 63 mm of the probe is wet and 53 mm stay above it |
| Drip tray (graphite TPU) | 32 x 38 x 12 (X 501 to 533, Y -2 to 36, Z -115 to -103), 2 mm walls and floor. Free volume round the cup is only about 4 ml, so it catches drips and a splash, not a knocked-over cup |

**Cable post**

| Item | Value |
| --- | --- |
| Core | dia 30 x 32 tall (Z -108 to -76), axis X 557.5, Y 11 (min bend radius 15 mm assumed for the cable, as in PERCH.md) |
| Flanges | dia 44 x 4 at the top (Z -76 to -72) and the bottom (Z -112 to -108) |
| Capacity | 32 mm / 3.2 mm cable = about 10 turns at about 104 mm per turn, so about 1.0 m. The concept said 4 to 6 turns |
| Position | Below the node; the cable's drip loop bottom is Z -64, 8 mm above the top flange |

**Hold (in the sump, rim version)**

| Item | Value |
| --- | --- |
| Saddle | A copy of Perch_Saddle with a 7.1 x 51 mm slab of the back plate cut away (Z 18 to 69), so no node pocket and no low pad are left. What remains: the 8 mm bridge, the upper pad (Z 70 to 78) and thumbscrew, the 160 mm leg with its rail and 10 stop holes, and the cable clip on the leg (the second clip on the back plate was cut off with the plate). Volume 57.5 cm3 (Perch 65.6) |
| Collet, thumbscrew, pad, probe | Shared with Perch (same components, second occurrence) |
| Probe depth | Same as Perch's middle setting: tip at Z -127, **55 mm under water** (water at Z -72), 207 mm under the rim top |
| Sump wall | The Perch 19 mm slab and water box, at X 200 |

**Cable**

- Swept path, 3.2 mm round, 618 mm long (from the volume of the pipe, 4.97 cm3). It runs from the Hold probe top, up and over the saddle bridge, down the outside, then across 360 mm to the node boot, with a drip loop up into the boot (the end is 2 mm under the boot).
- Horizontal distance Hold axis (X 200) to node axis (X 560): **360 mm**. The cabinet wall slab is X 440 to 640, 18 mm thick, with the plate top at the rim height. The sump wall slab ends at X 270, so there are 170 mm of free wall between the two slabs.
- Rule from this route: the cable needed in service is about the horizontal distance plus 258 mm (up and over the Hold, the drop, the drip loop, the end bends).

| Horizontal distance | Cable in service | Spare of 1 m cable | Turns on the post (104 mm each) |
| --- | --- | --- | --- |
| 300 mm | about 560 mm | 440 mm | 4.2 |
| 360 mm (as modelled) | 618 mm | 382 mm | 3.7 |
| 400 mm | about 660 mm | 340 mm | 3.3 |
| about 430 mm | about 690 mm | 310 mm | 3.0 |
| about 740 mm | 1 000 mm | none | none (the limit) |

- **Cable length you need: the supplied 1 m cable reaches a wall 300 to 400 mm from the Hold and parks 3 to 4 turns of spare on the post.** Further than about 430 mm, or if you want the cable to run round a corner, you need an SMA extension cable (the concept said the same).
- When the probe is parked in the cup, the cable run from the probe top to the boot is only about 100 mm, so about 0.9 m of cable has to go onto the post (8 to 9 turns of the 10 it holds). That is tight but fits.

## Checks

assembly_inspect_interference (hidden bodies included):

| Run | Result |
| --- | --- |
| Wall station: plate, tower, TPU, post, Berth_Ref (cabinet wall, ghost probe, cable), second node (Sleeve:2, FootCap:2, SMA_Boot:2, USB_Bung:2, Key:2, Reference_Parts:2) | No overlap between Berth parts and the node. Only zero-volume contacts, all intended (plate on tower, plate on post, plate on cabinet wall, key in sleeve, bung in cap). The cable end sits 3 mm into the pigtail plug reference body (26 mm3), which is where the cable ends. Old self-contact in Reference_Parts (8 mm3) as before |
| Hold: saddle, collet, thumbscrew, Perch_Ref:2, wall slab, cable | After I moved the cable 5 mm away from the saddle clips and over the wall top (the first route touched the saddle 12 mm3 and the wall slab 6 mm3): only 1.1 mm3 left between the cable start and the probe top, which is where the cable comes out |
| Ghost probe | Clear of the ring (0.2 mm), the cup (5 mm radial) and the socket |

Clearances by design: node plinth to tower 2 mm (X 534 to 532); ghost probe to plate 18.0 mm; cable low point to the post 8 mm.

## Pictures (this folder)

- `berth_iso.png`: render, whole Berth (sump wall, water, Hold with cable, cabinet wall with the station), from the front-right.
- `berth_front.png`: view of the station from the front-right at an angle (screenshot of v26), with the cabinet wall translucent and the Hold at the top left. It is not a flat front view because the flat front screenshot was nearly black.
- `berth_front_render.png`: flat front render of the station only (plate, tower with the parked ghost probe, cup, post, node, cable). Dark navy renders almost black, so the tower looks dark.
- `perch_vs_berth.png`: render, Perch at the left, the Berth Hold in the middle, the Berth wall station at the right.
- The renders `berth_iso.png`, `perch_vs_berth.png` and `berth_front_render.png` were made before I moved the cable's Hold end 5 mm (first route 611 mm). In those pictures the cable is within 5 mm of the final route; `berth_front.png` is from the final model.
- The renders do not show the cabinet wall as translucent; the screenshot does.

## What Berth adds over Perch

- A parking and calibration place for the probe: the cup holds storage or calibration liquid and the probe goes in tip-down in one move. The cable stays plugged in. The ghost probe in the pictures is this state. Perch has no wet storage place (only a possible storage cap on a peg, not modelled).
- The node is not at the sump. It hangs high on a dry wall, can be inside a cabinet, and nothing is on the water side except the small Hold, which carries no electronics.
- The cable post stows the slack (up to about 1 m). In Perch the spare is coiled with a tie.
- The row version (several nodes on one rail) is not modelled.
- It costs: a wall area 80 x 195 mm free next to the sump within about 400 mm, about twice the printing of Perch, a longer cable run, and a wall unit and a Hold per probe.

## Print time and part count for a real build (hand estimates, no slicer)

Volumes are the model's solid volumes. Time is my estimate from the Perch and Tidemark figures (Perch saddle 66 cm3 in 2.5 h; node about 6.5 h), with TPU at about a third of the PETG speed. Not sliced.

| Part | Material | Solid volume | Est. time | Orientation |
| --- | --- | --- | --- | --- |
| Berth node (same as Tidemark): sleeve, foot cap, sled, key, light pipe, bung, boot | PETG + TPU later | 52.9 cm3 | 6.5 h | as in NOTES.md |
| Wall plate with receiver and keyholes | PETG | 82 cm3 | 3.5 h | back face down; the receiver pocket lip has the same 24.7 mm bridge check as the RimClip |
| Tower | PETG | 43 cm3 | 2.5 h | on its back; cup socket and clamp arm stand up as vertical walls, the bore is vertical |
| Cable post | PETG | 44 cm3 | 2 h | flange undersides overhang the core by 7 mm, so print the flanges as separate discs or lay it on its side; not decided |
| Drip tray + cup (2 parts) | graphite TPU | 16.5 cm3 | 3.5 h | cup and tray as separate prints |
| Clamp ring | graphite TPU | 4.6 cm3 | 1 h | flat |
| Hold saddle | PETG | 57.5 cm3 | 2.2 h | on its side as the Perch saddle |
| Collet, pad | PETG | 14 and 1 cm3 | 1.2 h | as PERCH.md |

- Berth total about **22 h and 9 parts** (plate, tower, post, tray, cup, ring, saddle, collet, pad) plus the node's own set. The wall station alone (without the Hold) is about 19 h including the node.
- Perch for comparison: about **10 h and 3 parts** (saddle, collet, pad) plus the node. So Berth is about 2.2 times the print time and 3 times the parts.
- Extra hardware over Perch: two screws for the keyholes (size depends on the wall), a rinse sponge or lid for the cup, and the cup liquid. The Hold needs what Perch needs (M6 thumbscrew and nut, M4 screw and nut, two M4 x 10 stops).

## Not done / limits

- The tower, the plate and the post are three bodies that touch. How they join (one print, bolts, dovetail) is not designed.
- No lid or sponge for the cup is modelled. No type band, no probe cap, no Berth Row, no Glass Hold or Pipe clamp Hold.
- The Hold is only a cut-down Perch saddle. A real Hold would be a smaller part.
- The keyholes are only at the top. There is no lower fixing point and no VHB option.
- The cable path is a spline through hand-picked points; the clips on the Hold are not fitted to it (the cable passes 5 mm outside them). Spare winding on the post is not modelled.
- The antenna 15 mm metal clearance and 25 mm from water rules were not checked against a real cabinet.
- Probe size is the 12 x 116 you gave me, not measured; the cup is sized round it with 5 mm radial clearance.
- The interference check did not include the boards (not instanced).

## Open questions for Brian

1. Is a wall 300 to 400 mm from the sump realistic, or do you need an SMA extension from the start? (1 m cable: limit about 430 mm with 3 turns of spare.)
2. Tower and plate: print as one part (195 mm long on its back) or as plate plus bolt-on tower and post? The second choice lets you change the bay without reprinting the plate.
3. Cup: open with a sponge, or with a lid? The tray holds only about 4 ml, so a full 25 ml cup that is knocked over will still spill. Should the tray be bigger?
4. What goes in the cup for ORP, DO and EC? The probe storage rules for DO and EC are still unconfirmed (never RO water for pH and ORP).
5. Is one probe per wall unit enough, or do you want the Berth Row with several nodes and one shared rack?
6. Plate: widen by 6 mm so the foot cap does not overhang the right edge, or leave it?
7. Wall: what material is the cabinet wall, and screws or VHB? Two top keyholes only is probably not enough for a 0.4 kg unit; add a lower screw?
8. Is the Berth worth about 2.2 times the printing of Perch, given how often you pull probes out for calibration?
9. Do you want the Hold shortened to a real small saddle before this goes further?
