# Crown mounting: one dock, many adapters (2026-11-02)

Concepts only, no CAD. Visual page: `index.html`. Sketches: `00-architectures.svg`, `01-dock-ring.svg`, `a1-hang.svg` to `a8-tile.svg`, `09-can-wall-echo.svg`. Research: `research_notes.md`. Search summaries are marked as such; everything not sourced is marked UNVERIFIED. Prices are estimates, not looked up.
This folder is new. Nothing outside it was edited.

**Read section 14 first: coordinator check, with one hole-size gap and three CAD items.**

## 0. Answer in one screen
- **Interface: a dock ring on a 3 mm swappable plate (architecture C).** The ring grips the Crown's own foot (79.3 x 51.9 x 4 mm) and the plinth chamfer the hood already has, with two fixed hook tongues at the USB end and one in-plane flexure latch at the far end. The sole, window, o-ring and screws stay exactly as drawn. Requests on the sole are small (section 3).
- **Eight adapters** on that dock:

| # | Name | One line | Fits | Score /30 |
| --- | --- | --- | --- | --- |
| A1 | Hang | Saddle on the rim, arm over the opening (node about 60 mm in) | round can or bucket with a free rim of about 8 to 20 mm, lid off | 21 |
| A2 | Span | Two flat bars across the opening, node over the centre | rim OD 250 to 700 mm (printed bars to about 430, stock bars to 700), lid off | 25 |
| A3 | Collar | Printed bulkhead: flange above, thread through, nut below | hole 42.5 mm and up, top 2 to 10 mm+ | 23 |
| A4 | Umbrella | Push-in tube with a TPU skirt that opens under the top | hole 40 to 42 (variants 46, 52), top 2 to 6 mm | 22 |
| A5 | Expander | Wing-nut style plug: TPU ring squeezed by 3 screws | hole 50.5 mm and up (50.5, 57.2, 63.5, 76), top 2 to 16 mm | 24 |
| A6 | Pad | Flange and gasket sitting on a small hole | hole 25 to 33 mm, top 2 to 6 mm | 26 |
| A7 | Clamp | Screw clamp on a tank rim, shelf edge or wall top | edge 3 to 45 mm thick | 21 |
| A8 | Tile | Four magnets and four stick-on steel patches | flat surface with a hole 25 to 33 mm | 22 |

- **Print first:** the dock (ring plus a blank plate) with **A6 Pad** as the proof of fit, then **A2 Span** for the round can (best radar position of all eight), then **A5 Expander** (or A3 if Brian can reach under the top and has a 45 mm+ hole). Priority 1 (round can): A2, with A1 as a one-hour wall-echo test rig. Priority 2 (round hole in a rectangular top): A6 up to 33 mm, A5 above 50, A3 with access underneath.

## 1. Brief
Brian picked the Crown (water-level node, XM125 60 GHz radar looking down through a 1.5 mm PETG window). The container is open: round trash cans first, then a round hole in a larger rectangular plastic top, then bonus cases (tank or sump rim, drilled reservoir lid, bucket, shelf or bracket, wall arm, magnet). Question: what connection scheme lets one Crown suit many containers?
Sources: `enclosure_concepts_radar_2026-11-02\concepts.md` (sections 3 to 5) and its two Crown SVGs; `Sensor_Boards\feather_water_level\xm125_notes.md`; Tidemark NOTES.md (FitClr 0.2 mm, 2.5 mm walls, M2.5 inserts with 3.6 mm holes, 45 degree plinth chamfer, nylon hardware) and `nrf54l15_feather\enclosure_concepts\tidemark_decisions.md` (IP66 target with one face o-ring, TPU 95A on hand, PETG shell, plastic only within 15 mm of AE1, first prints plain PETG, sensor tag "lvl"); Ledger NOTES.md (Abyss navy, coral accents, plain PETG drafts). The decisions file is not in the `enclosure_tidemark` folder; it is in `enclosure_concepts`.

### 1.1 Crown coordinates used everywhere below
u runs along the Crown (positive toward the AE1 / far end), v across (positive toward the AE1 edge), d is depth below the outer face (the window face), z is height above it.
| Item | Value | Derived from |
| --- | --- | --- |
| Radar axis | centre of the A121, 16.5 mm from the USB-end board edge, centred across | bottom SVG: radar at x 16.5, y -11.43 |
| Foot (sole) edges | u -25.5 to +53.8, v +-25.93 (79.3 x 51.9) | foot x -9 to 70.3 |
| Body edges | u -19.5 to +47.8, v +-19.95 (67.3 x 39.9) | body x -3 to 64.3 |
| Radar offset from body centre | 14.15 mm toward the USB end; centred across | 30.65 - 16.5 |
| Corner screws | u -22.5 and +50.8, v +-22.93 | SVG circles |
| AE1 | u +28.17, v +8.65, z 17.1 to 18.4 above the sole bottom | AE1 at board 44.67, 20.08; feather top at 17.08 |
| Plinth | 4 mm vertical above the sole top, then a 45 degree chamfer 6 mm wide, 6 mm high (z 8 to 14) | side SVG hood path |
| USB-C tunnel | in the u -19.5 wall, z 15.2 to 22.2 | side SVG |

Consequence: a round hole, collar or can centre must sit on the radar axis, not on the body. From the axis the foot reaches 25.5 mm (USB end), 53.8 mm (far end), 25.9 mm (sides). The sole outline is taken as a plain rectangle (corner radius not drawn: UNVERIFIED). The known CAD item (posts overlapping the pocket corners) does not matter here: no adapter touches the pocket.

### 1.2 Rules used
1. **Margin line.** 45 degrees from the module face, which is 4.0 mm above the outer face. Radius at depth d: r45 = 4.0 + d. Nothing solid inside it.
2. **Minimum hole for something whose lowest edge is at depth d:** D45 = 2 x (4.0 + d); add 2 mm for drilling and print slack when recommending a size.

   | d (mm) | 3 | 4.5 | 6 | 7.5 | 9 | 10.5 | 12 | 13 | 15 | 18 |
   | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
   | D45 (mm) | 14 | 17 | 20 | 23 | 26 | 29 | 32 | 34 | 38 | 44 |
3. **-3 dB cone** (half angles 32.5 and 26.5 degrees; which plane lies along the board is UNVERIFIED): radius (4.0 + d) x 0.637 or x 0.499. The 45 degree rule (factor 1.0) is stricter. If bench tests show it is too safe, an underside at d = 7.5 (A6 on a 3 mm top) would need only 2 x 0.637 x 11.5 = 14.7 mm instead of 23.
4. **Tube or collar.** A bore of radius R stays out of the -3 dB cone while d_bot < R / 0.637 - 4 (R = 17: 22.7 mm). Every adapter here ends at d <= 18 mm. A thick tube near the beam can still act as a reflector through sidelobes, which are UNVERIFIED (bench test 3).
5. **Wall echo.** A vertical wall at lateral distance L enters the -3 dB cone at depth L / k - 4 (k = 0.637 or 0.499). Its return can arrive before the water return once the water is deeper than D* = L x sqrt(1 + k^2) / k - 4, that is 1.861 L - 4 (k 0.637) or 2.240 L - 4 (k 0.499), measured from the outer face. Derivation: slant from the module face to a wall point on the cone edge is L sqrt(1 + k^2) / k; the water slant is D + 4. With a wall leaning in by tan(tau) per mm of depth (wide at the top), entry depth is (L - 4k) / (k + tau). How strong a wall return really is stays UNVERIFIED: the ray meets a vertical wall at 32 degrees, so most energy should mirror away, and a wall-to-water bounce arrives later than the water return, not earlier.
6. **Level.** The radar must look straight down. The real tilt tolerance is UNVERIFIED; this study aims at 3 degrees or better and puts a 6 to 8 mm bull's-eye vial on every ring so the installer can see it.
7. **Minimum range.** Water at least 70 mm below the outer face. Each adapter states how far its outer face sits above the container.

## 2. Containers and sizes
### 2.1 Round cans and buckets (listings; which diameter they mean is UNVERIFIED)
| Container | Diameter | Height | Source |
| --- | --- | --- | --- |
| 5 gal bucket | top 11.91 in = 302.5 mm; bottom 10.25 in = 260 mm | 14.5 in = 368 mm | [Safeware](https://www.safewareinc.com/product/high-density-polyethylene-round-bucket-5-gal-premium-white-usp-2286-wh), [epackagesupply](https://epackagesupply.com/blog/5-gallon-bucket-dimensions) |
| Brute 20 gal | 19.5 in = 495 mm | 22.875 in = 581 mm | [Haskins](https://store.haskinsindustrial.com/product/rubbermaid-round-brute-containers-polyethylene-20-us-gal-fg262000wht-na692) |
| Brute 32 gal | about 22 in = 559 mm (21.9 to 22.375 in listed) | 27.25 in = 692 mm | [Katom](https://www.katom.com/007-2632W.html), [Staples](https://www.staples.com/rubbermaid-brute-plastic-trash-can-container-32-gallons-grey-fg263200gray/product_RCP263200GY) |
| Brute 44 gal | 24 in = 610 mm | 31.5 in = 800 mm | [distributor](https://catalogue.maschibougamau.ca/product/rubbermaid-brute-round-containers-bulk-polyethylene-44-us-gal-fg264360blue-jb466) |
| Brute 55 gal | 27 in = 686 mm | 33 in = 838 mm | [Lalema](https://lalema.com/product/2655-brute-round-waste-container-55-gal-20611) |
| 32 gal lid | flat top 22.25 in; dome 22 11/16 in | | [OnTime](https://www.ontimesupplies.com/rcp263100gy-round-flat-top-lid-for-32-gal-round-brute-containers-2225-diameter-gray.html) |

Assumed because not found (all UNVERIFIED): wall 4 mm, rolled rim 12 mm wide and 8 mm tall (the Tidemark rim clip was drawn for 12 mm), taper 3.3 degrees per side (derived from the bucket numbers: (11.91 - 10.25) / 2 = 0.83 in over 14.5 in = 0.0572; the trash cans' own taper was not found), lid thickness 2 to 4 mm, Crown mass 150 g. Search summary: rim width, wall thickness and taper of the Brute cans were in no listing.

### 2.2 Holes in a rectangular top
Hole saws and bulkheads (search summaries): 2-1/4 in = 57 mm and 2-1/2 in = 64 mm ([Guillevin chart](https://www.guillevin.com/cdn/shop/files/Fiche-Technique-_En-anglais-seulement_-c83c4ce6-6b39-442e-a00c-66b0e145c345.pdf)); 3 in = 76 mm and 3-1/2 in = 89 mm ([Klium](https://www.klium.nl/en/facom-609a40-holesaw-with-variable-teeth-length-45mm-diameter-40mm-29031)); bulkheads need a hole bigger than the nominal size: a 6 in PVC bulkhead needs an 8 in saw ([Barr](https://barrplastics.com/products/6-pvc-bulkhead-fitting-with-epdm-standard-flange-gasket-socket-x-socket-end-connections-bfa1060ses)), a reef-forum chart lists a 2 in bulkhead with a 2-7/8 in hole (no link kept), and a hole-sizing chart exists at [Univ. Arizona](https://be.arizona.edu/sites/default/files/2025-10/Hole-sizing-charts.pdf) (not opened). Other inch sizes below (1 in 25.4, 1-1/4 in 31.75, 1-3/4 in 44.5, 2 in 50.8 mm) are plain x 25.4 conversions, not listings. I do not know Brian's hole diameter or top thickness, so each adapter states its range:

| Hole dia (mm) | 25 | 32 | 38 | 42.5 | 44.5 | 50.8 | 57.2 | 63.5 | 76 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A6 Pad (top up to 6 mm) | yes | yes | no | no | no | no | no | no | no |
| A3 Collar: max top (mm) | no | no | no | 4.5 | 5.5 | 8.6 | 11.9 | 15 | wide plate |
| A5 Expander: max top (mm) | no | no | no | no | no | 4 | 7 | 10 | 16 (wide plate) |

A4 Umbrella is made to size: holes 40 to 42 (tube OD 39), 46 and 52 as variants. Smallest hole the Crown can use at all: 17 + 2 x top (A6, 45 degree rule): 21 mm in a 2 mm top, 23 mm in a 3 mm top. Below that, countersink the underside at 90 degrees until the cone line clears (cheap bit), or accept the -3 dB figure after bench test.

## 3. Connection architectures
All three leave the sealed radar head (window, pocket, o-ring groove, four corner screws, posts) as it is. All attach to the bottom of the sole, outside the o-ring, and none puts material across the window. See `00-architectures.svg`.

### A: axis bayonet (round twist-lock centred on the radar)
Three ramped hook tabs on a 44 mm circle centred on the radar, standing 3.5 mm below the sole; the adapter is a round flange with three entry slots; turn the whole Crown 25 degrees. Camera-lens and hose-coupling style.
- Good: self-centres on any round hole; no sideways play.
- Bad: new features on the sole (tabs lower than the window, so the window is no longer the lowest thing); the flange adds at least 3 mm under the sole; turning a 79 x 52 body sweeps a 60 mm radius, so it cannot work inside a bridge, clamp or rim hook; the final orientation is set by the slots.
- Verdict: good for holes, wrong for cans. Possible later variant.

### B: dovetail slide (Arca-Swiss style)
Two 45 degree undercut rails under the sole, 62 mm long, between the corner screws; the adapter is a slotted plate; a nylon set screw locks it. Borrowed from camera plates: 38 mm wide, 45 degree sides, measured parts 38.0 to 38.75 mm between makers ([Acratech](https://www.acratech.net/blog/arca-swiss-vs-bogen-manfrotto-camera-plates/), [astropix](https://astropix.com/wp/dovetail-sizes); search summaries).
- Good: radar position slides along a bridge; very rigid; familiar.
- Bad: rails stand 2.5 mm proud of the window plane and the screws need relief, so the sole is no longer plain; the 0.7 mm maker spread in the camera world warns that a printed dovetail needs a set screw; the Crown needs 80 mm of free run beside the slot; stops cover the USB end and the AE1 end.
- Verdict: keep the sliding idea inside one adapter (Span), not as the universal interface.

### C: dock ring on a swappable plate (recommended) - `01-dock-ring.svg`
The Crown's own foot is the interface. Lesson from Peak Design's Capture clip and plates: one dock, many plates, and do not change the dock afterwards ([digitec](https://www.digitec.ch/en/s1/product/peak-design-capture-clipplate-camera-straps-61012973), search summary).
- **Ring.** 85.7 x 58.3 outer, 3 mm walls, recess 79.7 x 52.3 (0.2 mm per side, Tidemark FitClr), 4 mm walls up to the sole top. Two fixed hook tongues at the USB end (12 mm wide, at v +-12, tops at z 11, hook tip at z 10.4, parallel to the 45 degree plinth chamfer with a 0.3 mm gap); one 40 mm long flexure latch at the far end with a thumb tab (hook tip z 10.7). The latch bends in the plane of the print layers (strain about 0.19 % for 1 mm deflection, 2 mm thick, 40 mm long: 1.5 x 2 x 1 / 40^2). Fit by tilt: hook the USB end, lower the far end, click. Release: press the tab, lift the far end. Four corner bosses carry brass M2.5 inserts; four screws from below join ring and plate (or glue for a fixed pair).
- **Plate.** 3.0 mm, sole face down on the smooth bed; whatever sits below it in service (tube, hook, clamp) grows upward in print. The plate may be any size. Every plate keeps a Dia 34 aperture centred on the radar axis (clears the drip lip) and an engraved datum cross at u = 0, v = 0 and the sensor tag "lvl".
- Why this works: two prints and four screws per adapter, but no supports on any part; the Crown pops off in one hand with no cable; the four corner screws become reachable; the sealed head is identical; the dock stays outside the IP66 seal, so it adds no leak path.
- Weak points: the ring fit depends on the hood chamfer being within about 0.3 mm (bench test 1); the 3 mm plate adds to d, so minimum holes are bigger than for a bare sole on a lid; no self-centring (the datum is on the plate).
- **Sole and foot requests.** (1) Optional polarity chamfer: one far-end corner 8 x 8 mm on the AE1 side, so a backwards dock (radar 28.3 mm off) cannot happen. (2) Drip lip (already a CAD item) kept inside radius 16.5 mm: a rounded rectangle 28 x 24, R5, 1.0 wall, 0.8 tall (farthest point 16.4 mm); then every aperture is Dia 34. (3) Corner screw heads flush (Tidemark counterbore practice) or four shallow pockets in each plate. (4) Nothing on the hood: tongue tops at z 11 sit 4.2 mm under the USB-C tunnel floor (15.2), so a plug is unhindered. No PCB change.

| | A axis bayonet | B dovetail | C dock ring + plate |
| --- | --- | --- | --- |
| Sole change | 3 tabs below the window | rails + screw relief | none required |
| Radar centring | automatic | slides | datum on each plate |
| Round hole | best | poor | good |
| Can bridge / rim hook | poor (turning) | good | good |
| Tool-free release | yes | set screw | yes (thumb latch) |
| Print | flange, slots | undercuts, tolerance | plate + ring, no supports |
| Risk | sole redesign | tolerance, space | chamfer fit |

## 4. Wall echo (rule 5), node at the centre against node on the rim
Node over the centre, vertical wall, inner radius L = OD / 2 - 4 mm (wall assumed). "With taper" assumes 3.3 degrees. Depths are from the outer face, in mm.

| Container | L | Wall enters -3 dB (0.637 / 0.499) | with taper | Wall return can beat the water return below (0.637 / 0.499) | Can height |
| --- | --- | --- | --- | --- | --- |
| 5 gal bucket | 147 | 227 / 291 | 208 / 261 | 270 / 325 | 368 |
| 20 gal | 244 | 379 / 485 | 348 / 435 | 450 / 543 | 581 |
| 32 gal | 275 | 428 / 547 | 393 / 491 | 508 / 612 | 692 |
| 44 gal | 301 | 469 / 599 | 430 / 538 | 556 / 670 | 800 |
| 55 gal | 339 | 528 / 675 | 485 / 606 | 627 / 755 | 838 |

Node at distance L from the nearest wall (rim mounts, clamps). Same formulas.

| L (mm) | -3 dB entry (0.637 / 0.499) | with 3.3 degree taper | beats the water return below |
| --- | --- | --- | --- |
| 25 | 35 / 46 | 32 / 41 | 43 / 52 |
| 40 | 59 / 76 | 54 / 68 | 71 / 86 |
| 60 | 90 / 116 | 83 / 104 | 108 / 130 |
| 100 | 153 / 196 | 140 / 176 | 182 / 220 |
| 150 | 232 / 297 | 212 / 266 | 275 / 332 |

Fair comparison: on a 32 gal can a centre node first sees the wall at 428 mm and can be confused only when the water is below 508 mm (the bottom 184 mm of a 692 mm can). A rim node at L = 60 sees the wall from 90 mm and can be confused below 108 mm, that is for 84 percent of the can's depth. So the rim hook (A1) and the clamp (A7) suit a can kept nearly full or a shallow tank, and are poor for a deep can; the bridge (A2) and a lid hole near the lid centre (A3, A5, A6) are the radar-friendly positions. A tapered can leans the wall into the beam, pulling the entry in by 8 to 10 percent. Orientation matters: if the narrow plane (0.499) lies along the Crown (UNVERIFIED), run the Crown's long axis radially at a rim; bench test 2 finds out. Diagram: `09-can-wall-echo.svg`.

## 5. The adapters
Common to all: ring + plate, vial, datum cross. Print as the family does (Snapmaker U1, 270 mm build volume per the [maker page](https://www.snapmaker.com/snapmaker-u1/specs), search summary; plain PETG first, TPU 95A for later rings, four perimeters, sole faces on smooth PEI). Print times are rough estimates from volume, not sliced; the ring is about 1 h on top of each. The only metal in every adapter is four brass M2.5 inserts in the ring bosses; the nearest, at ring corner (u +55, v +27.2, z about 2), is 36 mm from AE1 (sqrt(26.8^2 + 18.5^2 + 15.7^2) = 36.1). Prices are estimates; family fasteners and inserts are listed in `mechanical\hardware_lists\enclosure_hardware_amazon_2026-11-01.md`.

### A1 HANG (`a1-hang.svg`) - saddle on the rim
- **Idea.** A cantilever plate: the Crown dock at one end, a printed saddle that straddles the can's rolled rim at the other. Same logic as the Perch idea in the radar concepts, with an adjustable tongue like a bucket or tool-hook saddle.
- **Fits.** Round can, bucket or open tank with a free rim of about 8 to 20 mm (12 assumed, UNVERIFIED), lid off. No diameter limit.
- **Geometry.** USB end of the Crown points at the rim. Axis at L = 60 mm from the inner wall (arm length parameter 45 to 120). Plate 3 mm with two ribs 12 mm tall at |v| 21 (rib bottom at d = 15, margin 19 mm, so 2 mm clear). Tongue hangs 40 mm outside the wall; an M4 nylon thumbscrew with a TPU pad presses the wall.
- **Level.** Rim top is the datum (two 8 mm pads 40 mm apart along the rim); the thumbscrew trims pitch on a tapered wall. A tapered can is no problem for the rim contact; an out-of-flat rim is.
- **Wall echo.** L = 60: entry 90 / 116 mm, can beat the water below 108 / 130 mm; with taper 83 / 104. Weak for deep cans: a quick test or a nearly full tank.
- **Metal and AE1.** None except the ring inserts; the saddle is more than 100 mm from AE1 (u -72 against +28).
- **Seal.** None; open, splash only.
- **Print.** Plate sole face down, tongue and ribs grow upward, no supports. About 2.5 h.
- **Hardware.** One nylon M4 thumbscrew, a vial: about US$ 8.
- **Lid / release.** The lid stays off while the arm is on. Press the tab to free the Crown; the saddle lifts off the rim in one move.
- **Outer face** 3 mm above the rim top.

### A2 SPAN (`a2-span.svg`) - bridge over the opening
- **Idea.** Two flat bars lie across the can, the Crown dock sits in the middle, so the radar looks down the centre line, the best wall-echo position. Borrowed from a bucket cross-brace and the Arca-Swiss slide (the plate can slide along the bars to any chord).
- **Fits.** Round can, bucket or open tank, rim OD 250 to 700 mm, lid off. Printed bars (two 250 mm sections per bar, sleeved with 60 mm overlap, nylon M4 bolts through slots) are 440 mm long, so rim OD up to about 430 mm: buckets and small cans. Stock plastic flat bar (PVC or HDPE 20 x 8 mm, cut to length; availability UNVERIFIED) reaches 700 mm for the 20 to 55 gal Brutes.
- **Geometry.** Bars 20 x 8 mm at |v| 17 to 37 under the plate: the inner top corner (17, d 3) and inner bottom corner (17, d 11) are 10 and 2 mm outside the margin (r45 = 7 and 15). The plate bears on the bars over 12 mm each side. End hooks: a 3 mm tongue hangs 40 mm outside the wall with a TPU pad.
- **Level.** Rim top is the datum, four contact pads; make rail 2's sockets loose in height by 1 mm so it acts as a three-point support on a wavy rim. Sag at 560 mm span with two 20 x 8 PETG bars, 150 g, E 2 GPa (all assumed): F L^3 / (48 E I) = 1.5 x 560^3 / (48 x 2000 x 1707) = 1.6 mm, harmless because the radar is at the span centre. Pitch from a Crown mass 14 mm off centre: 21 N mm x 560 / (12 x 3.41e6) = 2.9e-4 rad, negligible.
- **Wall echo.** Centre position, section 4: the best of all eight.
- **Metal and AE1.** None. The bars sit 3 to 11 mm below the plate, plastic.
- **Seal.** Open. Condensation on the window as in the other schemes (drip lip).
- **Print.** Dock plate 86 x 58 with 2 sleeves, sole face down. Bars flat. Printed bars: 4 sections of 20 x 8 x 250 about 6 to 8 h; plate and hooks about 3 h (estimates).
- **Hardware.** 4 to 8 nylon M4 bolts and nuts, 2 stock bars if used, vial: about US$ 20 to 30.
- **Lid / release.** Lid off. Press the tab, the Crown comes away and the bars stay on the rim; or lift the whole bridge (it blocks pouring, so lift it).
- **Outer face** 11 mm above the rim top (plate 3 + bar 8); water must be at least 59 mm below the rim.

### A3 COLLAR (`a3-collar.svg`) - printed bulkhead
- **Idea.** A threaded tube hangs from the plate through the hole; a ribbed nut below the top locks it, a gasket seals the flange. Same layout as the 2 in NPT bulkhead mounts of ultrasonic tank sensors: flange, gasket, mounting nut ([Flowline LU23](https://www.commercial-industrial-supply.com/products/flowline-lu23-41), [Migatron](https://www.automation.com/article/migatron-releases-rps-409a-2p-ultrasonic-sensor), [EchoPod](https://advantagecontrols.com/downloads/pdf/D-Echopod.pdf); search summaries).
- **Fits.** Hole 42.5 mm and up, top 2 to 10 mm and more. d_bot = 3 (plate) + 1.5 (gasket) + top + 4 (nut) = 8.5 + top; bore = max(34, 2 x (4 + d_bot)) = max(34, 25 + 2 top); hole = bore + 8.5 (wall 2.5, thread depth 1.5, 0.5 slack). Top 3 mm: bore 34, hole 42.5, tube bottom d = 11.5, margin r 15.5 against bore r 17. Maximum top for a given hole = (hole - 33.5) / 2: 44.5 mm to 5.5; 50.8 to 8.6; 57.2 to 11.9; 63.5 to 15. The standard 86 x 58 plate covers holes to about 48 mm (5 mm land); bigger holes need an 80 mm plate.
- **Level.** Flange on a flat top; the gasket takes 1 degree. Not for dome lids.
- **Wall echo.** Depends on where Brian drills; at a can lid centre use the section 4 centre numbers.
- **Metal and AE1.** None. The tube wall would enter the -3 dB cone only below d = 22.7 mm; it ends at 11.5.
- **Seal.** Flange gasket (EPDM sheet or the 2 mm silicone cord ring from the family list). Splash proof; not pressure proof.
- **Print.** Plate and tube sole face down, tube pointing up 8.5 mm; 45 degree buttress thread (3 mm pitch) needs no supports; the nut prints flat. Threads are the risk: print a test pair at 0.2 mm clearance first. About 2 h plate, 0.5 h nut.
- **Hardware.** Gasket, 4 nylon M2.5 for the ring, a hole saw (set about US$ 25 to 40).
- **Release.** Tab frees the Crown; the collar stays in the top. With the Crown off, the plate and ring stand 8.5 mm above the top (tongues 15.5 mm) and the nut 4 mm below it, so a lid can be turned over on a bench.
- **Needs** hand access under the top.

### A4 UMBRELLA (`a4-umbrella.svg`) - push-in, TPU skirt
- **Idea.** A tube with a flared TPU skirt: push from above, the skirt springs open under the top. No access underneath. My own mechanism, modelled on rubber snap-in bushings (no product looked up).
- **Fits.** One size per hole: tube OD 39 for holes 40 to 42; M and L tube OD 45 and 51 for 46 and 52; tops 2 to 6 mm (the skirt flexes). d_bot = 3 + 1.5 + top + 4 = 8.5 + top; bore max(34, 25 + 2 top); at top 3 mm the tube ends at d = 11.5.
- **Level.** Flat top only; foam gasket takes about 1 degree.
- **Wall echo.** As A3.
- **Metal and AE1.** None.
- **Seal.** Foam gasket under the flange (1.5 mm closed-cell tape); the skirt is a splash barrier only.
- **Print.** Plate and tube sole face down. Skirt in TPU 95A (a separate body; Brian has it). First print: PETG skirt as a fit check only. Hold force is UNVERIFIED and depends on the true hole size (bench test 6).
- **Hardware.** Foam tape plus TPU: about US$ 8.
- **Release.** Tab frees the Crown. The plate pulls out of the top (about the effort of a snap-in grommet, not measured).

### A5 EXPANDER (`a5-expander.svg`) - TPU ring squeezed by three screws
- **Idea.** The wing-nut test plug: a rubber sleeve between two plates; tightening squeezes the plates and the rubber bulges against the hole. McMaster and Petersen expansion plugs work this way; the plate OD is 80 to 90 percent of the rubber OD so the rubber can bulge past; over-tightening injures the rubber and hand-snug may creep ([McMaster](https://www.mcmaster.com/products/expansion-plugs/pipe-size~2-1-2), [explainer](https://www.firgelliauto.com/blogs/mechanisms/expanding-pipe-stopper); search summaries). Here three nylon screws on a 39 mm circle, off the beam axis, do the squeezing.
- **Fits.** Hole 50.5 mm and up, top 2 to 16 mm. d_bot = 3 (plate) + top + 6 (TPU stack below the top) = 9 + top; bore = max(34, 26 + 2 top); hole = bore + 16.5 (body wall 5, TPU 3, 0.5 slack). Sizes: 50.5 (a 2 in saw, 50.8; top to 4), 57.2 (top to 7), 63.5 (top to 10), 76 (top to 16, wide 96 mm plate). At top 3 mm the stack ends at d = 12, margin r 16 against bore r 17. The ring grips +-1.5 mm of hole error.
- **Level.** The TPU ring lets the plate tilt about 3 degrees; trim on a dome with the vial.
- **Wall echo.** As A3.
- **Metal and AE1.** Three M3 screws at r 19.5, 120 degrees apart: nylon into printed threads (none), or 316 captive nuts. The nearest nut (19.5, 0, d 10.5) is 30.7 mm from AE1 (sqrt(8.67^2 + 8.65^2 + 28.2^2) = 30.7; the SVG text says 29, a conservative rounding). Screws sit 3.5 mm outside the margin.
- **Seal.** Best of the hole adapters: the TPU ring seals the hole to splash; add a 1 mm TPU face lip for a flange seal.
- **Print.** Plate with body sole face down; compression ring flat; TPU ring flat (6 mm tall, 3 mm wall). About 2 h + 0.4 h + 0.5 h.
- **Hardware.** 3 nylon M3 x 20, TPU: about US$ 6.
- **Release.** Tab frees the Crown. Loosen the three screws to pull the plug. On a trash can lid: lift the lid with the plug in it.

### A6 PAD (`a6-pad.svg`) - flange and gasket on a lid
- **Idea.** The plate sits on the top over a hole, a gasket ring seals the join, the radar looks through the hole. The simplest adapter and the proof of the dock. Flange-and-gasket without the thread.
- **Fits.** Hole 25 to 33 mm, top 2 to 6 mm, flat area at least 86 x 58 mm with the hole 29 mm from the near edge. Lowest edge d = 3 + 1.5 + top = 4.5 + top; D45 = 17 + 2 top (2 -> 21, 3 -> 23, 5 -> 27, 6 -> 29), plus 2 mm slack. The hole must stay inside the gasket id 34, so the top end is 33. For a 3 mm top and a 30 mm hole: underside at d = 7.5, margin r 11.5, hole r 15, 3.5 mm clear.
- **Level.** The plate rests on the flat top.
- **Wall echo.** By hole location: section 4.
- **Metal and AE1.** None (ring inserts only).
- **Seal.** Gasket ring id 34, od 48, 1.5 mm closed-cell or EPDM. Splash-tight around the Dia 34 aperture.
- **Hold.** Weight; two ears with 4.5 mm holes for M4 nylon screws, or a foam tape strip.
- **Print.** Plate sole face down, 2 ears, no supports. About 1.2 h.
- **Hardware.** Gasket sheet, two M4 nylon: about US$ 10.
- **Release.** Tab frees the Crown; the Pad stays.
- **Outer face** 4.5 mm above the top; water must be at least 65.5 - top below the underside.

### A7 CLAMP (`a7-clamp.svg`) - screw clamp on an edge
- **Idea.** A C-clamp: the plate rests on the rim top, a back plate hangs outside the wall, an M8 nylon thumbscrew with a TPU pad squeezes the wall. Like camera and phone clamps and aquarium lid brackets (no product looked up).
- **Fits.** Tank, sump or reservoir rim, shelf edge, wall top, edge 3 to 45 mm thick (back plate moves in slots). Round cans only with a thick flat rim.
- **Geometry.** L = 45 mm to the inner face. Arm plate 3 mm, ribs as A1.
- **Level.** The arm sits on the rim top; the screw pad trims pitch. Vial.
- **Wall echo.** L = 45: entry 67 / 86 mm, beats the water below 80 / 97 mm. A longer arm helps: L = 100 gives 153 / 196 and 182 / 220.
- **Metal and AE1.** None (nylon M8). Wall-arm variant: the same plate screwed to a wall with two screws; the back plate is more than 90 mm from AE1, so metal screws there are clear.
- **Seal.** None.
- **Print.** Plate with back plate sole face down, back plate grows upward, no supports. About 2.5 h.
- **Hardware.** M8 nylon thumbscrew, about US$ 6.
- **Release.** Tab frees the Crown; loosen the thumbscrew to remove the clamp.
- **Outer face** 3 mm above the rim.

### A8 TILE (`a8-tile.svg`) - magnets
- **Idea.** Four magnets in pockets of a 3.5 mm plate hold the Crown to four stick-on steel patches (or a steel shelf) around a hole. No tools. My own design (the phone magnet-ring search returned nothing).
- **Fits.** Any flat surface that takes the patches and has a hole 25 to 33 mm (A6 rule, top 2 to 6 mm): a plastic lid, a stand, a steel shelf.
- **Geometry.** Four magnets Dia 10 x 2 (typical N35, UNVERIFIED) at (u -17 or +44, v +-22), pockets 2.3 deep with a 1.2 mm floor, open upward under the sole. Patches 20 x 20 x 0.5 mm steel (self-adhesive steel tape or cut sheet), nearest corner r 13.9 from the axis at d = 4, where the margin is 8. Magnets sit 27 mm or more from the axis.
- **Metal and AE1 (arithmetic).** Nearest magnet (44, 22, z -1.3) to AE1 (28.17, 8.65, 17.7): sqrt(15.83^2 + 13.35^2 + 19^2) = 28.1 mm. Nearest patch corner (34, 12, z -4): sqrt(5.83^2 + 3.35^2 + 21.7^2) = 22.7 mm. Both clear the 15 mm plastic-only zone; a steel shelf directly below the plate is at least 20.7 mm away. A steel hole edge is a metal edge near the beam: keep the hole at Dia 34 or more.
- **Level.** Flat surface only.
- **Seal.** None (add the A6 gasket if wanted). Magnetic pull on the real surface is UNVERIFIED.
- **Print.** Plate sole face down. About 1.2 h.
- **Hardware.** 4 magnets and 4 patches: about US$ 15.
- **Release.** Pull, or the tab as usual.

## 6. Comparison (1 to 5, 5 best; same criteria for all eight)
Looks; Fit (with the container it is meant for); Print and seal (ease); Radar (clearance and wall echo); Antenna and metal; Install and level (ease).

| | Looks | Fit | Print/seal | Radar | Antenna/metal | Install/level | Total /30 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A1 Hang | 3 | 3 | 4 | 2 | 5 | 4 | 21 |
| A2 Span | 4 | 5 | 3 | 5 | 5 | 3 | 25 |
| A3 Collar | 4 | 4 | 3 | 4 | 5 | 3 | 23 |
| A4 Umbrella | 3 | 3 | 3 | 4 | 5 | 4 | 22 |
| A5 Expander | 3 | 5 | 4 | 4 | 4 | 4 | 24 |
| A6 Pad | 4 | 3 | 5 | 5 | 5 | 4 | 26 |
| A7 Clamp | 3 | 3 | 4 | 2 | 5 | 4 | 21 |
| A8 Tile | 4 | 2 | 4 | 4 | 3 | 5 | 22 |

Coverage by container:

| Container | Primary | Also |
| --- | --- | --- |
| Round trash can, lid off (priority 1) | A2 | A1 (quick test) |
| Round trash can, lid on and drilled | A5, A3 | A6 (small hole), A4 (if the hole is exact) |
| Hole in a rectangular top (priority 2) | A6 (25 to 33), A5 (50 and up), A3 (45 and up, access underneath) | A4, A8 |
| Open tank or sump rim | A7 | A1, A2 |
| Drilled reservoir lid | A6, A5 | A3, A8 |
| Bucket (5 gal) | A2 (printed bars) | A1, A5 or A3 on a drilled lid |
| Shelf or bracket above water | A7 (shelf edge) | A8 on a steel shelf with a hole |
| Wall-mounted arm | A7 variant with two wall screws | |
| Magnetic mount | A8 | |

## 7. Recommendation
1. **Interface:** the dock ring on a swappable plate (architecture C). Build the ring and a blank plate first and check the fit on a dummy sole block with the 4 + 6 mm plinth before printing anything else.
2. **Print order:** (a) ring + blank plate, then **A6 Pad** on any lid with a 25 to 33 mm hole (proves the dock, level and the aperture with the real Crown); (b) **A2 Span** in printed-bar form on a 5 gal bucket to learn the span, then stock bars for a Brute; (c) **A5 Expander** at 50.5 mm for the first big-hole top, or **A3 Collar** if Brian can reach under and has 45 mm+ holes; (d) **A1 Hang** as a one-hour rim test rig to read the wall echo at L = 60.
3. Priority 1 answer: **Span**, because it puts the radar over the centre; accept that the lid is off. If the lid must stay on, drill it and use A5 or A3, centred.
4. Priority 2 answer: **Pad** for small holes, **Expander** for big ones, **Collar** if there is underside access and a threaded seal is wanted.
5. Family direction: ring and plate in graphite later (plain PETG now), Abyss navy only on the hood, coral thumb tab on the latch as the one accent (like the Tidemark key and the Ledger pill), TPU rings and pads in graphite or coral, engraved tag "lvl". The same ring idea could later suit Tidemark's foot and Ledger's stand; not drawn.

## 8. Requests
- **PCB: none.** Sole and foot: polarity chamfer (optional), drip lip within r 16.5 (recommended), flush corner screws, plain 79.3 x 51.9 outline. Hood: none.
- For fusion-enclosure: model ring and plate as one parametric component; the plinth chamfer and sole outline come from the Crown model.

## 9. Questions only Brian can answer
1. Which cans: make and gallons, lid on or off during use, must the lid stay on? Rim width and shape (calipers), wall thickness, taper.
2. Holes in tops: which hole saws do you own or will buy, top thickness (calipers), flat or domed, can you reach under?
3. Is a hole of about 50 mm acceptable (A5), or must it be 33 mm or less (A6)?
4. Is lid-off operation acceptable for the can (A2, A1)? How full is the can kept (the "beats the water" depths in section 4)?
5. Indoor only, or humid garage and outdoors (condensation, UV)?
6. Crown mass with the cell (weigh it); is the 3 mm plate under the sole acceptable?
7. Are stock plastic bars (PVC or HDPE) acceptable for large spans, or must everything be printed?
8. Magnets near the node: OK, given the 28 mm AE1 distance?

## 10. Bench tests to add
1. **Dock fit:** ring + blank plate on a dummy sole block (79.3 x 51.9 x 4 with the 4 + 6 mm plinth); check the hook gap 0.3 mm, latch force by hand, 20 cycles.
2. **Wall echo in a real round can:** Crown on a plate at the centre and at L = 60 and 40; water at 100, 200, 300, 500 mm; repeat with the Crown turned 90 degrees to find which plane is 0.637. Log peak amplitude and extra peaks.
3. **Hole rule:** SparkFun XM125 breakout above plates of 3 mm with holes 14, 17, 21, 25, 30, 34 mm; compare amplitude with the 45 degree rule; also a 34 mm bore, 8.5 mm tube against no tube.
4. **Tilt:** radar tilted 0, 3, 6, 10 degrees over calm water; amplitude. Sets the real tilt budget.
5. **Span sag:** real Crown, bars at 450 and 560 mm; dial indicator.
6. **A4 pull-out and A5 leak:** push-in force, hose or splash test of the TPU ring.
7. **Condensation:** open aperture against gasket-sealed aperture over warm water for 24 h.
8. **Magnet / range:** magnets and steel patches against the AE1 link range, baseline without.
9. **Rim survey:** three cans' rim width, wall and lid thickness, taper (calipers).

## 11. UNVERIFIED list
Trash can rim width, wall thickness, taper, lid thickness; which diameter the listings give; which beam plane lies along the board; PETG permittivity at 60 GHz; Crown mass (150 g assumed); PETG stiffness (2 GPa assumed) and fatigue of the latch; tilt tolerance; real wall-echo strength; tube and sidelobe reflection; hook fit against the real hood chamfer; sole corner radius and screw head depth; drip lip shape; thread quality at 0.2 mm clearance; TPU skirt and ring behaviour; magnet pull; availability and price of every hardware item (estimates, not looked up); inch to mm conversions other than the four sourced; U1 build volume (maker page via search summary).

## 12. Arithmetic checks done
- Radar offset 30.65 - 16.5 = 14.15; foot reach 16.5 + 9 = 25.5 and 70.3 - 16.5 = 53.8.
- D45 = 2 x (4 + d): d 4.5 -> 17, 7.5 -> 23, 11.5 -> 31; bore 34 allows d up to 13.
- Wall entries: 147 / 0.637 = 230.8 -> 226.8; 147 / 0.499 = 294.6 -> 290.6; 275 / 0.637 = 431.7 -> 427.7; 275 / 0.499 = 551.1 -> 547.1; 339 / 0.637 = 532.2 -> 528.2; 339 / 0.499 = 679.4 -> 675.4. D*: 1.8613 x 275 - 4 = 507.9; 2.2397 x 275 - 4 = 611.9. Taper: (275 - 2.55) / 0.6942 = 392.5; (275 - 2.0) / 0.5562 = 490.8.
- Sag: 1.5 x 560^3 = 263.4e6; 48 x 2000 x 1706.7 = 163.8e6; ratio 1.61 mm.
- AE1 distances: corner insert 36.1, A5 nut 30.7, A8 magnet 28.1, A8 patch corner 22.7 mm.
- Cross-references: SVG numbers match this file. Known small differences: the A5 SVG text says 29 mm (this file 30.7); the A2 SVG says printed bars reach "about 440" (bar length) while the table says rim OD about 430.

## 13. References
See `research_notes.md` for the full list with what each teaches. Main links: Brute 32 gal [Katom](https://www.katom.com/007-2632W.html); 5 gal bucket [Safeware](https://www.safewareinc.com/product/high-density-polyethylene-round-bucket-5-gal-premium-white-usp-2286-wh); Gamma Seal ring and threaded lid [epackagesupply](https://epackagesupply.com/blogs/packaging-guide/food-storage-buckets-with-gamma-lids) (a permanent ring on the container, a removable threaded part: the idea behind keeping the plate on the container and lifting the Crown off); bulkhead and nut [Flowline LU23](https://www.commercial-industrial-supply.com/products/flowline-lu23-41); expansion plugs [McMaster](https://www.mcmaster.com/products/expansion-plugs/pipe-size~2-1-2); Arca-Swiss [Acratech](https://www.acratech.net/blog/arca-swiss-vs-bogen-manfrotto-camera-plates/); Peak Design plates [digitec](https://www.digitec.ch/en/s1/product/peak-design-capture-clipplate-camera-straps-61012973); radar installation notes [ifm](https://www.ifm.com/us/en/us/learn-more/level/lw21/installation-guidelines); U1 volume [Snapmaker](https://www.snapmaker.com/snapmaker-u1/specs).

## 14. Coordinator check (2026-11-02)
Recalculated: the hole rules, wall-echo tables, sag, AE1 distances and score totals all match, except as listed below. These notes are reasoning from the numbers in this file; none is measured, and the sketches are not redrawn for them.

1. **Hole-size gap, and a simple way to close it.** The table in 2.2 leaves holes from 33 to 40 mm with no adapter (a 1-1/2 in saw is 38 mm), and 42.5 to 50 mm has only A3, which needs access underneath. The 33 mm limit on A6 is stricter than it needs to be: a gasket can overhang into the hole as long as it keeps a land on the top. At d = 7.5 the margin is only r 11.5, so the overhang is well clear of it. With a gasket id 34, od 54 (r 27, inside the plate's 28.5 and 29 mm reach from the axis), A6 covers holes to about 44 mm with a 5 mm land. A larger plate takes it further. Check a hole near the top of the range in bench test 3 and fit the gasket before relying on it. Holding force still comes from weight, two ears or tape, so this suits flat tops; A5 or A3 are stronger.
2. **Ring corner bosses do not fit the 3 mm walls as drawn (CAD item).** A 3.6 mm insert hole at (u 55, v 27.2) leaves about 0.2 mm of wall to the outside and breaks into the recess corner by about 0.35 mm. Grow the corners outward into round bosses of about 9 to 10 mm OD. This adds a few mm at the corners, so the 86 x 58 mm flat-area figures need rechecking in CAD.
3. **The hole adapters seal the hole, not the path past the Crown.** The gaskets in A3, A4, A5 and A6 seal the plate to the top. Nothing seals the sole to the plate, so can air can still pass the Dia 34 aperture and leave through the ring's 0.2 mm clearance. The Crown itself stays sealed. If the container should be closed to humidity or evaporation, add a soft face gasket around the aperture on the plate top (for example id 36, od 48). Add it to bench test 7.
4. **A5 screw heads (CAD item).** The three screws tighten from the plate's top face, under the sole, so the Crown has to be off to adjust them and the heads must sit below the plate surface. Use countersunk heads or counterbores in the 3 mm plate.
5. **A2 sag leaves out the bars' own weight.** Two 20 x 8 x 560 mm PETG bars weigh about 228 g, which adds about 1.5 mm (5 W L^3 / (384 E I)), so about 3 mm in all. Still harmless at the centre of the span. Stock plastic bar will differ.
6. **Sketch repairs.** a2-span, a3-collar, a4-umbrella and a5-expander each had an unescaped "<" that made the SVG invalid and stopped it displaying; these are fixed and all SVGs now parse. The notes in the lower right of a2-span.svg overlap (cosmetic, not fixed).
