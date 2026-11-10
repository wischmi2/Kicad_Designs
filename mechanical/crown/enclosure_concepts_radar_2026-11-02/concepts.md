# Feather water-level node (XM125 60 GHz radar): enclosure concepts, battery placement (2026-11-02)

Concepts only, no CAD. Brian picks one, then fusion-enclosure models it.
Visual page: `index.html` (this folder). Sketches: `00-stack-and-cone.svg`, `01-slab-*.svg`, `02-crown-*.svg`, `03-pier-*.svg`, `04-perch-*.svg`. Working notes: `research_notes.md`.
Why this exists: design review blocker B3 (`C:\Personal-Agents\shared\reports\2026-11-02-review-feather-water-level.md`). In the Tidemark stack order the radar would look straight through the sled into the LiPo. The old ultrasonic concepts (Bead, Davit, Plumb, Cork, 2026-10-25) are obsolete for the sensor and are not reused except for the use, container and family notes.
This folder is not in git. Nothing outside it was edited.

## 1. Summary and recommendation

| # | Name | One-line idea | Outer size (L x W x H, mm) | Score (max 45) |
| --- | --- | --- | --- | --- |
| 1 | Slab | The Tidemark stack laid flat; the cell lies on the sole beside the boards, level with the radar face, 14 mm sideways | 67.3 x 56.9 x 26.6 (foot 79.3 x 68.9) | 35 |
| 2 | Crown | Same flat stack, but the cell rides in a hump on the lid, over the USB half of the feather, 19.6 mm behind the radar | 67.3 x 39.9 x 26.6, hump 36.6 (foot 79.3 x 51.9) | 36 |
| 3 | Pier | A long head over the water and a low tail that lies across the container rim and carries a big cell | 123 x 39.9 x 26.6 head, 13.5 tail (foot 135 x 51.9) | 33 |
| 4 | Perch | The head overhangs the water, the rim passes under its far end, the cell stands in a leg outside the wall | 79.3 x 39.9, 26.6 above and 29 below the sole (55.6 tall) | 33 |

**Recommendation: Crown** (Slab as the fallback if Brian wants a bigger cell).
- It is the only layout where the cell is both far from the radar (19.6 mm behind the module face, behind two ground-plane boards, 180 degrees off the beam) and farthest from AE1 (25.4 mm, versus 22.7 mm in the Tidemark stack). The B3 problem disappears by geometry, not by tolerance.
- Smallest footprint on a lid or rim (79.3 x 51.9 foot; Perch has the same foot but also needs its leg outside the wall), the shortest battery lead (about 15 mm to U4), and the hump lifts off with the lid, so the battery and the SWD header J3 are reached together.
- Cost, stated plainly: the cell is limited to about 10 x 20 x 20 mm (about 4 cm3, two thirds of the 6 x 20 x 50 cell by volume) because the key and LED own the roof from fx 22.7. The stepped roof also cannot be printed roof-down without supports unless the hump is a separate bonnet (section 3.3).
- Slab shares the same sole, window, posts, hardware and hood walls as Crown, so build the radar head once and decide the carrier later. Print the Slab hood (no battery) first as the test rig for the radome.
- None of the four needs a PCB change.

## 2. Brief

**What it does.** Battery node that measures water level with an Acconeer XM125 (A121 60 GHz radar, antenna in package) looking down through the enclosure plastic. nRF54L15 feather (50.8 x 22.86 mm, parts on top, flat bottom) above the water-level board (same outline and holes), joined by a U-folded 14-way 0.5 mm FFC at the short end opposite the feather's USB-C. No solar panel. Sensors go inside the node's enclosure, small form factor (Brian's standing constraint).

**Order from the beam end:** water, wall (radome), air gap, radar, sensor board, feather. No hole in the enclosure; the radar looks through the plastic.

**Where it lives.** Reef or aquarium room: sump, RO or top-off reservoir, tank. Humid, salt creep, condensation under lids. The container type is still undecided (see section 8). Handled by Brian; installed once, battery or USB rarely, flashing now with the stack out.

**Hard numbers (from the board file and the XM125 notes, board corner x 90, y 110 = fx 0, fy 0).**
- Radar (A121) centre fx 16.5, fy 11.43; module body fx 8.7 to 27.3 (18.6 x 15). Beam taken from the datasheet position, not the SparkFun drawing (review N7). Module height about 1.6 mm, modelled as 1.88 mm: UNVERIFIED, not measured (review N6).
- Beam: HPBW about 65 x 53 degrees (A121). Half angles 32.5 and 26.5 degrees, tan 0.637 and 0.499. Which plane lies along the board is UNVERIFIED; the sketches put the wider one along the board length.
- AE1 chip antenna: fx 44.7, fy 20.1, on the feather top, at the long-edge corner. Keep-out fx 42.15 to 50.8, fy 16.4 to 22.86 (research_notes).
- Roof-side parts that fix the headroom: J3 SWD (fx 18.9, 6.0 mm tall assumed), SW1 key (fx 26.4), LED1 (fx 30.6). Nothing may sit over fx 22.7 to 32 on the roof.
- U4 battery JST is on the AE1 edge at fx 12.0 (mouth towards fy 22.86). U5 solar JST (fx 12, fy 6.4) is unused on this node and is never used for the cell.
- Hardware as in the family: nylon M-F standoffs and nylon pan screws at the four holes (H3 plated GND on this board, NPTH on the feather, H1/H2 the reverse, review N8: harmless with nylon). M2.5 brass heat-set inserts (4 mm OD, 3.6 mm hole) only in the printed posts and the foot flare.

**Cell sizes used** (1S LiPo; capacities are rough and UNVERIFIED because seller size codes do not fix capacity: 603450 listed at 1000 to 1200 mAh, 502030 at 250 mAh):
- 6 x 20 x 50 (about 6 cm3, family cell, roughly 500 to 700 mAh at the same density as the listings),
- 6 x 34 x 50 (about 10.2 cm3, 603450 class),
- 10 x 20 x 20 (about 4 cm3, roughly 330 to 470 mAh at that density).
Battery-life target is still open (Brian). Rough budget: with R15 to R18 not fitted, the review gives about 94 uA of VSENS-on idle plus the module, so about 110 uA with the DNPs. Even the smallest cell gives months if the radar is duty cycled, but the feather's own sleep current and the reading rate are not in the sources I read, so I do not state days.

## 3. The shared radar head (all four concepts)

All four use the same lower half; only the carrier above it and the battery place differ. Drawn in `00-stack-and-cone.svg`.

### 3.1 Layers (section at the radar centre, z from the outer face of the window)
| Layer | mm | Note |
| --- | --- | --- |
| Radome window, 100 % solid PETG | 1.5 | 10 layers at 0.15 mm; set by the rule below |
| Air gap (module face to wall), n = 1 | 2.5 | a pocket in the sole; HIG: do not press the cover on the sensor (about 6 dB loss) |
| XM125 (module face to board bottom) | 1.88 | modelled box, UNVERIFIED |
| Water-level board | 1.6 | radar on its bottom |
| Hs, 8 mm nylon standoff; FFC U-fold lives in this gap | 8.0 | Tidemark needs 14 mm only for its SMA; this node has no SMA |
| nRF54L15 feather | 1.6 | |
| Parts and headroom (J3 6.0 assumed, plus 0.5 clearance, plus the key plunger travel) | 7.0 | |
| Roof | 2.5 | family wall |
| **Total, outer face to roof** | **26.6** | |

### 3.2 Radome numbers (derived here, not measured)
- Wavelength at 60.5 GHz in air: 4.955 mm. In plastic the half wavelength is 4.955 / (2 x sqrt(er)). With er unknown: 1.60 mm at er 2.4, 1.515 mm at er 2.675 (the only PETG figure I found, from 75 to 110 GHz, so a proxy), 1.43 mm at er 3.0. The HIG's own tables give 1.55 mm at er 2.6 and about 1.5 mm for PLA/PC. I use **1.5 mm**; the second order (n = 2) would be about 3.0 mm.
- **PETG permittivity at 60 GHz is UNVERIFIED.** The window thickness is therefore a bench decision, not a result (section 9).
- Oblique rays: at the -3 dB edge (32.5 degrees) the path through the window is 1.5 / cos 32.5 = 1.78 mm, so the electrical thickness at the beam edge is about 19 % more than on axis. A consequence of the geometry, effect on the signal UNVERIFIED.
- Window must be 100 % solid: infill density changes the dielectric behaviour (X-band study, search summary). No ceramic, metal or carbon filled filament anywhere near the radar or AE1.
- The 1.5 mm window is below the family's 2 mm wall rule on purpose; it is the single exception, held by the 4 mm sole around it. The sole prints outer-face down on smooth PEI, window layers solid, pocket open upwards: no overhang, no supports.

### 3.3 Beam clearance (calculated)
- Cone centre is the A121 face (z = -4.0 in the sketches). At the outer face (4.0 mm below it) the -3 dB radius is **2.55 mm along the board and 2.0 mm across**. My 45-degree margin line gives r = 4.0 mm at the same plane. The window is 25 x 21 mm (half 12.5 x 10.5), so the nearest window edge is at least 6.5 mm outside even the margin line (8.5 mm along the board, 6.5 mm across). The pocket (25 x 21 x 2.5) walls are 12.5 and 10.5 mm from the axis, also outside it.
- Posts and inserts: the two nearest 8 mm posts (H1, H2) are centred 14 mm (x) and 8.9 mm (y) from the axis, the other two (H3, H4) 31.8 mm (x), and all stand above the face plane; the brass insert bottoms are 12 mm from the axis at about 2 mm below the face plane, about 80 degrees off axis. Outside the -3 dB cone and the margin; effect of brass at that angle UNVERIFIED. Nylon standoffs and screws are not metal.
- **Known conflict, CAD item (coordinator check, 2026-11-02):** the H1 and H2 posts reach fx 6.54 and fy 2.54 to 6.54 / 16.32 to 20.32 (radius 4 mm), and the 25 x 21 mm window and pocket start at fx 4. So the two posts overlap the USB-end pocket corners by about 2.5 mm in x, and the bottom sketches draw them overlapping. Notch those two pocket corners around the posts, or start the pocket and window at fx 6.6 (9.9 mm from the axis, still 5.9 mm outside the 45-degree margin line). The same applies to all four concepts.
- Beam radius at the water, outer face to water distance D: r = (D + 4.0) x 0.637 (along) and x 0.499 (across): 47 / 37 mm at 70 mm, 66 / 52 at 100, 98 / 77 at 150, 130 / 102 at 200, 194 / 152 at 300.
- A container wall at lateral distance L from the axis enters the -3 dB cone at depth D = L / 0.637 - 4 (along) or L / 0.499 - 4 (across). In most containers the beam will touch a wall at depth; Acconeer's tank-level page and use case advise a lens or reflector to narrow the field if wall echoes are a problem (search summary). Treat as a bench test. Minimum range of the tank-level app is 3 cm from the sensor (fetched page); the sketches keep the water at least 70 mm below the outer face.

### 3.4 Sole, seal and cartridge
- The sole is a separate plate (like Tidemark's foot cap) with the window, a face o-ring groove (2 mm silicone cord in a 2.7 x 1.5 groove, as in Tidemark), four M2.5 corner screws and the four 8 mm posts with heat-set inserts. The boards sit on the posts (1.88 mm high, so the module face is level with the pocket top), the 8 mm nylon standoff stands on the sensor board, the feather on the standoff, a nylon pan screw on top. The cartridge therefore comes off with the sole when the hood is lifted off.
- The hood is the roof, four walls and the flare (45-degree plinth chamfer, same as Tidemark). 2.5 mm walls, 0.5 mm clearance to parts.
- Coral key above SW1, translucent coral eye (2.5 mm rod light pipe) above LED1, both in the roof, exactly as the Tidemark and Ledger. First print: PETG key and pipe, no seal.
- 3 mm ePTFE vent disc on the hood shoulder away from the sole, one 1 g silica pack in a slot (placement is a CAD item), as Tidemark.
- USB-C: 12.5 x 7 mm tunnel in the end wall at the J1 height, same as Tidemark (bung later in TPU).
- FFC: at Hs 8 the sheet gaps are 9.6 mm, so the U-turn radius is about 4.8 mm and the minimum length about 19 mm (pi x 4.8 + 2 x 2 mm insertion, same method as the Tidemark notes). The sketches leave 11.3 mm behind the board end. Tidemark's open question of a standard 30 mm FFC applies here too: a 30 mm one bulges further than drawn, so either buy about 20 to 25 mm or widen the hood by 2 to 3 mm. Brian decides (question 6).
- Antenna in all four: plastic only over AE1; the roof and walls are plain PETG. The sensor board ground sits Hs + 1.6 = 9.6 mm behind AE1 (the Tidemark stack, at Hs 14, has 15.6 mm; the Tidemark notes already flag Hs 8 as about 10 mm). That is a property of the board pair, the same for all four concepts, and it goes on the antenna bench test.

### 3.5 Condensation on the window (all four)
Water is a strong absorber and reflector at 60 GHz, so a film or drops on the outer face will matter. The size of the effect is UNVERIFIED (expected, not measured); the SparkFun breakout test measures it.
- Drip lip: a 0.8 mm tall, 45-degree chamfered ring on the sole around the window, 14 mm or more from the axis (outside the 4 mm margin radius even at its top). Not drawn; a CAD item.
- Industrial practice (search summaries: Icon Process Controls; US 6,629,458): an inclined radome helps condensate run off, and condensate must not settle between sensor and cover. First draft is flat. Second-print experiment: tilt the window face 5 to 10 degrees; this changes the wall thickness across the beam, so only after the flat test.
- The air gap is inside the sealed shell with silica, so inner-face condensation is limited to leaks; PETG is not vapour-tight, which is why the silica pack and vent exist.
- Firmware should median-filter and reject jumps; a hydrophobic coating on the outer face is a bench option (UNVERIFIED).

### 3.6 Flashing and test pads
Flashing with the stack out of the enclosure is acceptable for now (decision pending). TP1 to TP8 face the sole inside the 1.88 mm post gap, so they are reachable only with the boards lifted off the posts (unscrew the nylon stack). If Brian later wants field flashing, a sole with a TP window is possible but it opens a leak path and puts the pads inside the beam pocket area; this is not drawn.

### 3.7 References
| Reference | Link | What it teaches here |
| --- | --- | --- |
| Acconeer HIG (hardware and physical integration guideline, 2025-10-02) | https://developer.acconeer.com/download/hardware-integration-guideline/ | Radome rule n x lambda/2 wall, gap n x lambda0/2, do not press the cover on the sensor. Read by kicad-designer; recorded in xm125_notes.md |
| Acconeer tank level reference app (fetched) | https://docs.acconeer.com/en/latest/ref_apps/a121/tank_level.html | Range 3 cm to 23 m, sensor at the top with free space in front. Says nothing on lids, condensation or tilt |
| Acconeer tank level use case (search summary) | https://docs.acconeer.com/en/latest/use_cases/tank_level.html | A lens or reflector narrows the field to cut wall reflections |
| Acconeer tank level brief, XM132 through a PP lid (search summary) | https://www.mouser.lt/pdfDocs/refappbrieftanklevel.pdf | Radar worked through a plastic lid; older platform, rough guide only |
| Univ. of Arkansas, free-space W-band measurement of 3D-printed plastics (search summary) | https://scholarworks.uark.edu/eleguht/85 | PETG er about 2.675, loss tangent under about 0.045 at 75 to 110 GHz. A proxy, 60 GHz is outside that band |
| Vega, measurement through glass (search summary) | https://vega.com/company/blog/2017/measurement-through-glass | Inclined windows deflect interfering reflections; no 60 GHz figure |
| Icon Process Controls radar datasheet; patent US 6,629,458 (search summaries) | see research_notes.md | Inclined or shaped cover leads condensation away |
| Tidemark build notes and decisions | `C:\Personal-Agents\shared\design\nrf54l15_feather\enclosure_tidemark\NOTES.md`, `tidemark_decisions.md` | Family language, hardware stack, o-ring foot cap, AE1 15 mm plastic-only zone (cell at 22.7 mm there), print rules |
| Ledger gateway notes | `C:\Personal-Agents\shared\design\pouch_gateway\enclosure_ledger\NOTES.md` | Abyss navy, coral key and status pill, 20-degree brow, 2.0 mm walls, draft PETG rule |
| Old ultrasonic concepts | `C:\Personal-Agents\shared\design\feather_water_level\enclosure_concepts\concepts.md` | Container list, humid and salt rules (drip edge, 1.5 mm salt-break groove), wet-side stainless or nylon hardware, PCTG for humid load-bearing parts |

## 4. Concepts

Scores below are out of 5 and use these criteria: **Looks, Setting fit** (works for the likely containers), **Print and seal** (ease), **Radar clearance** (cell versus beam), **Antenna** (cell versus AE1), **Size**, **Battery room**, **PCB change** (5 = none), **Family fit**. Print times are rough estimates from volume against Tidemark's 34.9 cm3 sleeve at about 3.5 h, not sliced.

### Concept 1: SLAB (`01-slab-side.svg`, `01-slab-bottom.svg`)

**What it is.** The Tidemark stack lying on its back like a paving slab, one low hood over the boards. The cell lies on the sole beside the boards on the U5 side, with its top face 6 mm up from the sole and level with the radar module.

**Mounting and containers.** The foot sits flat on a lid or a rim over an opening. For a lid it needs a hole of at least 30 x 26 mm (at the 45-degree margin the cone is 4 + lid thickness in radius, so this is enough for lids up to about 8 mm); a printed drill template marks it. Suits: plastic or glass lid with a cut-out (RO and top-off reservoirs, which reef users already drill), open sumps with a flat rim wider than the 79 x 69 foot only if they have a cut-out. It does not suit narrow open tops or bare rims thinner than the foot.

**Size.** Body 67.3 x 56.9 x 26.6 mm; foot with the 6 mm flare 79.3 x 68.9 mm. The width is driven by the cell (20 wide) plus the board plus 0.5 mm clearances.

**Beam clearance.** Shared numbers in 3.3. Cell nearest point **14.0 mm sideways** of the axis, at the face plane (90 degrees off axis, 3.5 mm beyond the window edge). Nothing in the cone. The cell is the closest of the four to the module, which is its weakness.

**Battery and antenna risk.**
- Radar: a LiPo (foil pouch) is effectively metal, 14 mm from the module at the same height. Reflections off its edge into the antenna's near field are possible. Effect UNVERIFIED; bench test with a foil-wrapped cell stand-in at 14 mm.
- AE1: cell to AE1 **23.9 mm in 3D** (22.6 plan, 7.7 height difference; the sketch label says 22.7 plan, a 0.1 mm rounding). The Tidemark reference is 22.7 mm, so it is no worse. The 15 mm plastic-only zone is clear. Mark for the bench range test.
- The cell does not need to be under the key and LED zone, so any length to 50 mm fits. A 6 x 34 x 50 cell needs the body 14 mm wider (about 71 mm) and the nearest point stays 14.0 mm; thickness to 10 mm fits under the 24 mm headroom.
- The lead runs from the cell (U5 side) over the feather to U4 on the opposite edge, about 60 to 80 mm; add a hook or clip. (The sketches' labels "U5 side" in other concepts mean the side where the cell is, not the U5 connector.)

**Printability in PETG without supports across the radome.** Yes. Sole outer face down, window solid, pocket open upward. Hood roof-down with a plain flat roof and 45-degree end chamfers: no steps, no supports. USB-C tunnel is a 12.5 mm bridge as in Tidemark. Roughly hood 2.3 h, sole 2 h, small parts 0.5 h: about 5 h. Easiest of the four.

**Condensation.** Shared (3.5). The sole sits on top of a lid with the window over the hole, so the window faces warm humid air and is the likeliest surface to sweat on a cool lid. Drip lip and later tilt.

**Assembly and access.** Screw the sole (with cartridge) to the hood by 4 corner screws; the o-ring cord sits in the sole groove. Lifting the hood exposes the feather top, J3 and U4, and the cell lies free on the sole. The cell is wrapped in foam and held by two printed ledges. Battery change and SWD with no further disassembly. USB-C through the end tunnel.

**Family fit.** Tidemark laid down: same flare, 45-degree chamfers, key and eye. No brow (AE1 is under a plain 2.5 mm roof).

**Fusion would model:** sole with window, pocket, groove, posts and inserts; hood with flare, key and eye holes, USB tunnel; cell ledges; drill template; drip lip.

**PCB:** none.
**Scores:** Looks 3, Setting 4, Print and seal 5, Radar clearance 3, Antenna 4, Size 3, Battery room 4, PCB 5, Family 4. **Total 35.**

### Concept 2: CROWN (`02-crown-side.svg`, `02-crown-bottom.svg`) - recommended

**What it is.** Same flat stack and sole, but the cell rides in a hump on the lid, over the USB half of the feather. The hump is the "crown"; it is over fx 0 to 20 only, clear of the key (fx 26) and LED.

**Mounting and containers.** Same as Slab: the foot sits flat on a lid or rim over a 30 x 26 mm minimum opening. Because the foot is only 51.9 mm wide, it also fits a rim or lid opening that Slab cannot, as long as the opening is a cut-out in a surface at least 52 mm wide. Not suited to a bare 12 mm rim.

**Size.** Body 67.3 x 39.9 x 26.6; hump 25.5 long and 36.6 high; foot 79.3 x 51.9 mm. Same foot as Perch, and smaller than Slab and Pier.

**Beam clearance.** Shared numbers in 3.3. The cell is **19.6 mm behind the module face** (cell bottom at z -23.6, face at -4.0), directly behind the radar (cell fx 0 to 20 contains the radar at fx 16.5), **180 degrees off the beam**, with the sensor board and the feather, both with ground planes, in between. Nothing in front of the radar except the window. This is the safest geometry for the radar; effect of a cell behind the module through the ground planes is UNVERIFIED, expected to be small.

**Battery and antenna risk.**
- Cell about **10 x 20 x 20 mm (about 4 cm3)**: two thirds of the family cell by volume, so roughly 330 to 470 mAh (UNVERIFIED, rough). Cell length is capped by the key hole at fx 22.7 to 30.1. A larger cell would need the key and eye moved (SW1 and LED1 are fixed on the feather), or a taller hump with thicker cell: each extra mm of cell thickness adds 1 mm of hump height.
- AE1: **25.4 mm in 3D** (24.7 plan, cell 5.9 mm above AE1). Largest of the four and 2.7 mm more than the Tidemark reference. The cell's y range includes AE1, so it faces the antenna end-on; mark for the bench range test.
- Lead to U4 is about 15 mm (cell above U4 at fx 12). The cell sits 0.5 mm above J3's assumed 6.0 mm height (J3 is at fx 15.7 to 22 under the cell): real J3 height needed.
- Heat or weight on the lid: the hump is lid-mounted, so the lid must carry the cell; fix with foam and a printed cradle.

**Printability in PETG without supports across the radome.** The radome side is as Slab (sole face down). The hood is the issue. Printed roof-down, the step from the hump (36.6) to the main roof (26.6) is a flat 38 x 37 mm downward face 10 mm above the bed, which needs supports. Two clean ways: (a) print the hump as a separate bonnet (a 25.5 x 39.9 cap with its own roof, 4 screws and a small o-ring or gasket) over an opening in the main roof, printed roof-down on its own; this also is the battery door, so I recommend it; (b) a 45-degree ramp between the hump and the roof (costs 10 mm of length and cuts into the key zone, so not preferred). The sketches draw the hump as one piece; this is the print split to carry into CAD. Estimated: hood 2 h, bonnet 0.7 h, sole 1.7 h, small parts 0.5 h: about 5 h. Moderate: one extra seal.

**Condensation.** As Slab. The cell is dry above the boards.

**Assembly and access.** Lift the whole hood to reach J3 and U4 (cell comes with the bonnet, so unplug the short lead). Or unscrew only the bonnet to swap the cell. Tools: 4 sole screws, 2 to 4 bonnet screws. USB-C through the end tunnel; LED and key as in the family.

**Family fit.** Best of the four: it reads as a Tidemark column tipped on its back with a bump where the battery lives, and the hump echoes the brow.

**Fusion would model:** sole as Slab; hood with plinth flare; bonnet and its opening; cell cradle; key and eye; USB tunnel; drip lip; drill template.

**PCB:** none.
**Scores:** Looks 4, Setting 4, Print and seal 3, Radar clearance 4, Antenna 5, Size 4, Battery room 2, PCB 5, Family 5. **Total 36.**

### Concept 3: PIER (`03-pier-side.svg`, `03-pier-bottom.svg`)

**What it is.** A long hood: the radar head overhangs the water, a low tail lies across the container rim and carries a big cell, so the cell is outside the container and 50 mm from the radar.

**Mounting and containers.** Rests on a rim and is held by a sliding hold-down with a thumbscrew pad on the outer wall face (indicated only; the counter-face and slide are CAD items). Rim band drawn 12 mm; the clamp position slides along the tail for a radar axis 50 to 100 mm from the inner wall (73.5 mm as drawn). Suits: open-top tanks, sumps with the lid off, open RO or top-off buckets with a rim of about 12 mm. Not suited to a closed lid without a cut-out.

**Size.** Body 123 x 39.9 mm; head height 26.6, tail 13.5; foot 135 x 51.9 mm. The longest by far.

**Beam clearance.** Shared numbers in 3.3. Cell nearest point **50.5 mm from the axis** (tail starts 5 mm beyond the FFC apex), at the face plane (90 degrees), outside the container. The container wall is 73.5 mm from the axis, so the -3 dB cone touches it at depth 111 mm along the board (143 mm across) at 73.5 mm: only a deep container sees it.

**Battery and antenna risk.**
- Largest cell room: 6 x 20 x 50, or 6 x 34 x 50 (about 10.2 cm3, 1000 to 1200 mAh by the seller listings, UNVERIFIED). The 34 mm cell leaves 0.45 mm per side in the 34.9 mm inner width, a little under the 0.5 rule; widen the tail 0.2 mm.
- AE1: **23.6 mm** to the nearest cell corner (dx 22.3, dz 7.7), no better than Slab. Mark for the bench range test.
- Lead is about 90 mm, from the tail along the roof to U4; one more 90 mm wire near the case but 32 mm from AE1.

**Printability in PETG without supports across the radome.** Radome side as Slab. The hood has a flat tail roof 13 mm above the head roof; roof-down, it is a 50 x 40 mm downward flat at 13 mm height and needs supports (the drawn 45-degree ramp only helps the first part). Fix by printing the tail as a separate part (lap joint, two M2.5 inserts, second o-ring or a gasket) or accept supports under the tail roof. Sole 135 x 51.9 x 4 mm is big and warp-prone: brim and a corner relief. Rough: hood 3 h, sole 2.8 h, tail extras and hold-down 1 h: about 7 h. Hardest print.

**Condensation.** The head hangs out beyond the rim, so the window sees the humid tank air, typically cooler near the lid or edge. The tail and cell sit on the dry outer side. Same drip lip.

**Assembly and access.** Lift the hood; cell in the tail is replaced through an access plate or by splitting the tail. Longest wire runs.

**Family fit.** Tidemark with a boom; reads closer to the old Plumb idea than to a column. 3.

**Fusion would model:** sole 135 long; hood with step and tail; hold-down on the tail with thumbscrew pad; cell ledges; drill template not needed.

**PCB:** none.
**Scores:** Looks 3, Setting 3, Print and seal 3, Radar clearance 5, Antenna 4, Size 2, Battery room 5, PCB 5, Family 3. **Total 33.**

### Concept 4: PERCH (`04-perch-side.svg`, `04-perch-bottom.svg`)

**What it is.** The head overhangs the water, the container rim passes under its far end, and the cell stands in a leg that hangs on the outside of the wall.

**Mounting and containers.** Gravity: the head rests on the rim (drawn 12 mm, parametric), the leg hangs 0.5 mm outside the wall. Suits: open-top tanks and sumps with a rim, where there is at least 12 mm free outside the wall for the leg. Not for lids or for tight cabinets. The leg is 12 x 26 mm in plan.

**Size.** Head 79.3 x 39.9 mm (foot with side flares 51.9 wide); height 26.6 above the sole and 29 below it, 55.6 in all.

**Beam clearance.** Shared numbers in 3.3. The rim wall is only **35.3 mm** from the axis, so the 45-degree margin meets the wall at **31 mm below the face** (the sketch label said 28; fixed in the file) and the -3 dB cone reaches the wall at 51 mm along the board and 67 mm across: before the water at any realistic level. The wall echo is part of the design, not an accident. The cell is outside the wall; its lowest corner is **59 degrees** off the beam axis, 50.8 mm over and 30 mm down, and 22.6 mm to AE1 horizontally.

**Battery and antenna risk.**
- Radar: the cell is behind the container wall (whose material may be glass, acrylic or metal; unknown), and outside the cone; the wall itself is the larger reflection risk.
- AE1: the cell is **22.6 mm** from AE1 at the same height, facing it broadside. Worst cell orientation versus AE1 of the four, equal in distance to the Tidemark reference (22.7 mm). Bench range test first.
- Cell standing, 6 x 20 x 50; a 34 wide cell widens the leg to about 40 mm (flush with the head width). Lead about 80 mm.

**Printability in PETG without supports across the radome.** Radome side as Slab. The hood is a tall L (55.6 mm) with a flat roof and a leg: roof-down, the leg walls print straight up, with no flat downward faces inside, but it is a 55 mm tall, 2.5 mm walled shape that wobbles; use a brim and slow walls. A separate leg cover (the outer 2.5 mm face) with a second o-ring is the only extra seal. Hood 2.5 h, sole 1.7 h, cover 0.5 h, small parts 0.5 h: about 5 h. Moderate.

**Condensation.** The head hangs out over the tank and the wall echo is strongest here; the leg and cell are dry outside.

**Assembly and access.** Lift the head, or remove the leg cover to change the cell without opening the boards. J3 and U4 are reached by lifting the hood. A 3D-printed leg can break if knocked; wet-side hardware is nylon or stainless.

**Family fit.** Hook-like and asymmetrical; the leg is a new element. 4 for looks, but it is the least like the column.

**Fusion would model:** sole 73.3 x 51.9; hood with leg; leg cover and o-ring; cell ledges; rim thickness parameter.

**PCB:** none.
**Scores:** Looks 4, Setting 2, Print and seal 3, Radar clearance 4, Antenna 3, Size 4, Battery room 4, PCB 5, Family 4. **Total 33.**

## 5. Container fit (the type is undecided)
| Container | Slab | Crown | Pier | Perch |
| --- | --- | --- | --- | --- |
| Closed lid with a cut-out (RO, top-off) | yes (30 x 26 hole) | yes (30 x 26 hole) | no | no |
| Open tank or sump with a rim | on a cut-out only | on a cut-out only | yes | yes (needs room outside) |
| Narrow container (under 100 mm wide) | wall in cone from about 50 mm depth: bench test | same | same | no |
| Cabinet gap around the sump | n/a | n/a | tail outside the wall | leg needs 12 mm outside |

## 6. Comparison

| Criterion (max 5) | Slab | Crown | Pier | Perch |
| --- | --- | --- | --- | --- |
| Looks | 3 | 4 | 3 | 4 |
| Setting fit | 4 | 4 | 3 | 2 |
| Print and seal | 5 | 3 | 3 | 3 |
| Radar clearance (cell vs beam) | 3 | 4 | 5 | 4 |
| Antenna (cell vs AE1) | 4 | 5 | 4 | 3 |
| Size | 3 | 4 | 2 | 4 |
| Battery room | 4 | 2 | 5 | 4 |
| PCB change needed (5 = none) | 5 | 5 | 5 | 5 |
| Family fit | 4 | 5 | 3 | 4 |
| **Total (max 45)** | **35** | **36** | **33** | **33** |

Cell distance to the radar axis / to AE1:
| | Slab | Crown | Pier | Perch |
| --- | --- | --- | --- | --- |
| Cell vs radar axis | 14.0 mm sideways, 90 deg | 19.6 mm behind, 180 deg | 50.5 mm, 90 deg | 50.8 mm, lowest corner 59 deg, behind a wall |
| Cell vs AE1 (3D) | 23.9 | 25.4 | 23.6 | 22.6 |
| Cell volume (rough) | to 10 cm3+ | about 4 cm3 | to 10 cm3+ | to 10 cm3 with a wider leg |
| Print supports | none | none with a separate bonnet | tail roof needs them, or split | none, tall |

Crown and Slab are within one point on the table. The reason to choose Crown is the radar and antenna column, which carry the risk in B3; Slab is the pick if capacity matters more than that.

## 7. PCB change requests
None of the four needs a PCB change. Optional, for kicad-designer to judge, none blocking:
- A battery pad or JST on the U5 side edge would shorten the Slab lead (60 to 80 mm); today the cell must reach U4 on the AE1 edge. Probably not worth a respin.
- Feather: a mounting hole pattern or J3 position change is not needed; the real J3 height matters (6.0 mm is assumed).
- If field flashing (decision 5 of the review) becomes a requirement, spare CN1 pins 5, 7, 10 would need to carry BOOT0 and UART; this is the review's point, not an enclosure request.

## 8. Questions only Brian can answer
1. **Container type(s).** Closed lid with a cut-out, open tank with a rim, or open sump; inside width and depth; wall or rim thickness (Tidemark assumed 12 mm); highest and lowest water level. This decides Slab/Crown versus Pier/Perch.
2. **Is a 30 x 26 mm hole in a lid acceptable** (printed drill template)? If not, only Pier and Perch work.
3. **Battery-life target and the cell.** Is a cell of about 4 cm3 (Crown, roughly 330 to 470 mAh, UNVERIFIED) enough, or do you want the family 6 x 20 x 50 cell or a 603450 class cell?
4. **VSENS off between readings or on with hibernate** (review S1). It sets the battery drain and so the cell.
5. **Field firmware update:** is opening the enclosure acceptable? Bench flashing with the stack out is assumed.
6. **FFC length:** 20 to 25 mm (shorter hood), or the standard 30 mm (hood wider by 2 to 3 mm)?
7. **Real J3 height and the SWD cable you plug** (6.0 mm assumed), since the cell in Crown sits 0.5 mm above it.
8. **First print:** which carrier, and print the radome sole as a separate test rig first? (I recommend the Slab hood as the rig.)
9. **Radar mounting height:** can the node sit at least 70 mm above the highest water?

## 9. Bench tests (before the first full print)
1. **PETG sample through the SparkFun XM125 breakout** (SparkFun_Qwiic_Pulsed_Radar_Sensor_XM125; `xm125_notes.md` lists the board): print a coupon set 1.2, 1.4, 1.5, 1.6, 1.8 and 3.0 mm thick, 100 % solid, same print settings as the sole, flat on smooth PEI. Hold each at 2.5 mm from the module face (a printed spacer), aim at a flat water surface and a metal plate at 100 mm, record peak amplitude and distance offset with and without the coupon. The best thickness gives the permittivity and replaces my 1.5 mm. Repeat at 5 mm gap and with the coupon pressed on to see the HIG's 6 dB loss.
2. **Water film:** spray a mist on the outer face of the best coupon; compare amplitude. Then try the drip lip, tilt and a hydrophobic coat.
3. **Battery near the radar:** move a foil-wrapped dummy and then a real LiPo to 14 mm sideways (Slab), 20 mm behind (Crown) and 50 mm (Pier, Perch); record amplitude and phantom peaks.
4. **Wall echo:** a wall sheet at 35 mm and 73 mm from the axis, water at 70, 150 and 300 mm.
5. **AE1 range test:** the feather with the sensor board at Hs 8, a cell at 22.6, 23.6, 23.9 and 25.4 mm (placed as in the four concepts) against a no-cell baseline, and against the Tidemark stack at 22.7 mm.
6. **Measure the XM125 height with calipers** (1.88 mm assumed) and set the 2.5 mm gap from it.
7. **Print test:** the sole with the pocket and 10-layer window at 0.15 and 0.2 mm layers, thickness by calipers; o-ring groove squeeze.
8. **J3 and FFC:** real J3 height; FFC bulge at 30 mm versus 20 to 25 mm.
9. **Condensation soak:** the sealed head in a warm humid box for 24 h, silica on and off.

## 10. Family direction
Radar head: sole, window, o-ring, posts and hardware are the same part in all four; only the carrier changes. Colours as in the family: Abyss navy hood, graphite sole later (PETG draft now), coral key, translucent coral eye. The water-level node reads as the Tidemark laid on its back. The Ledger gateway and this node share the key and eye accents.

## 11. Sketch review (2026-11-02, this run)
All nine SVGs were read and are complete and valid. Checked against the facts: radar centre 16.5 mm, board 50.8 x 22.86 mm, AE1 centre fx 44.67 / fy 20.08, stack sum 26.58 mm, beam radii and ring sizes, cell and AE1 distances. One change: `04-perch-side.svg`, the label "45 deg line meets the rim wall 28 mm below the face" was wrong (the line is at 31.3 mm); now 31 mm. Not changed: `01-slab-bottom.svg` shows the plan distance to AE1 as 22.7 mm where the model gives 22.6 mm. Not drawn: the drip lip, the Crown bonnet split, the Pier tail split, the Pier hold-down counter-face. I did not render the SVGs, only read them.
