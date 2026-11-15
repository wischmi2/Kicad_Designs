# Crown water-level enclosure, PETG print draft (2026-11-11)

Board: feather_water_level_tc2030 (rev 0.2-TC2030, XM125 on B.Cu looking down) under the nRF54L15 feather (STEP 2026-10-28b).
Concept: Crown (Brian 2026-11-02). Mounting: dock ring on a 3 mm swappable plate, plus A6 Pad, A2 Span and A5 Expander (Brian 2026-11-03).
First print: plain PETG, single material. TPU parts are separate bodies (A5 TPU ring) and the A6 gasket is cut sheet.

**Corrections 2026-11-14 (measured for the assembly guide, `..\assembly_guide_2026-11-12\ASSEMBLY.md` section 2.1):** the sole posts have **no inserts**; the board stack is M2.5 x 10 nylon screws up from the window face into 8 mm M-F nylon standoffs, with nylon nuts on the feather (12 brass inserts in all: 4 hood plinth, 4 hood roof, 4 dock ring). Question 6 (H4 sole insert) is closed: nylon throughout. The 3 mm vent is in the +x (latch) end wall, not -x. Plate-to-ring screws must be M2.5 x 5 (a 6 mm one reaches the 5 mm hole floor).

## Fusion document and save problem
- Working doc: `crown_stage1_housing` in Fish_Stuff / nRF54L15_Feather (lineage urn:adsk.wipprod:dm.lineage:BmJnnJRXSLi8PoxvlgyBbw). It's the stage-1 local backup, uploaded through the data API (v1).
- Final model uploaded as `feather_water_level_enclosure_crown` (same folder, urn:adsk.wipprod:dm.lineage:42dpsZJhTVaUEhPj7zaevQ, v1). It holds all of stages 1-4.
- **Fusion can't save to either file:** both cloud files read `is_read_only: true`. `doc_save` and `doc_save_as` report success, but no version appears. This matches what the 2026-11-11 run saw. Likely cause (not confirmed): the Fusion Personal limit of 10 editable documents. Fix: in the Fusion data panel, make an older document read-only, then open `feather_water_level_enclosure_crown` and save it (that makes it editable). Delete the extra `crown_stage1_housing` afterwards.
- Local snapshots (one per stage, all openable in Fusion): `fusion_snapshots\crown_stage1_housing.f3d` (previous run), `crown_stage2_dock_a6.f3d`, `crown_stage3_a2_span.f3d`, `crown_stage4_a5_expander.f3d`, `feather_water_level_enclosure_crown.f3d` (final, same as stage 4 plus view state).

## Coordinates
World origin = water-level board corner (board x 0 to 50.9, y -22.86 to 0). z 0 = outer face of the sole (radar window face); +z is up into the node. Radar (A121) axis at x 16.5, y -11.43; the module face is at z 4.0, the sole top. USB end = -x, AE1/far end = +x. AE1 box in the model: x 44.7 to 46.2, y about -20.1 to -18.5, z 17.0 to 18.3 (the -y side; mounting.md says v +8.65, which is the other side).

## Stage 1 summary (previous run, checked here, not changed)
- Sole 79.3 x 51.86 x 4 (z 0 to 4): 1.5 mm window (WinT) under a pocket. Posts 1.965 mm high (PostH) under the sensor board at H1-H4. Four corner screws at x -5 / 66.3, y -33.38 / 10.52 with counterbores. A 6 x 1.5 mm pry notch through the sole edge at x 55 to 61, y -37.36.
- Hood: foot 79.3 x 51.86, a 4 mm vertical plinth (z 4 to 8), a 45 degree chamfer 6 mm in (z 8 to 14), body 67.3 x 39.86, roof at z 26.485. USB-C tunnel in the -x wall, a 3 mm vent at (x 0, y -4, z 20), roof bosses, plinth inserts.
- Bonnet (battery hump) x -3 to 22, top at z 34.985, holds the TinyCircuits ASR00003 20 x 20 x 5 cell on a 1 mm pad.
- Key and light pipe, feather part placeholders, hardware refs (8 mm nylon standoffs, post screws and nuts, plinth and roof inserts, corner and bonnet screw heads).
- User parameters: WinT 1.5, SoleT 4, PostH 1.965, Hs 8, Wall 2.5, TopClr 7, CableSide 6, UsbGap 0.5, FFCLoop 11, FlareW 6, BattL/W/T 20/20/5, BattClr 0.5, PadT 1, BonWall 2, FitClr 0.2.
- Size against the concept: foot 79.3 x 51.86 (concept 79.3 x 51.9), roof 26.5 above the window face (concept 26.6), hump 35.0 (concept 36.6).

## Parameters added (stages 2-4)
RingWall 3, PlateT 3, HookGap 0.3, ApertureD 34, A6GasketOD 54, BarW 19.05, BarT 9.525, A2RimOD 430, A2StockRimOD 700, A5TopT 3, A5Squeeze 1.5.
Driving: PlateT, BarT, A2RimOD (printed bar length), A2StockRimOD (stock bar length and cap position), A5TopT and A5Squeeze (A5 tube, TPU ring and compression ring heights). ApertureD, A6GasketOD, BarW and the hook geometry are drawn at those values but are **not linked** to the parameters (sketch values). Change them by editing the sketches.

## Stage 2: dock ring, blank plate, A6 Pad
**Dock_Ring** (one print, reused on every plate)
- Frame 85.7 x 58.26 outside, recess 79.7 x 52.26 (FitClr 0.2 per side round the sole), walls 3 mm, z 0 to 4 (the sole height).
- Four corner bosses, 9 mm OD, 6 mm tall, at (-12, -40.36), (73.3, -40.36), (73.3, 17.5), (-12, 17.5). Each has a 3.6 x 5 mm hole from the bottom for M2.5 inserts (2.16 mm wall to the recess corner, which fixes coordinator item 14.2).
- USB end: two fixed hook tongues, 12 mm wide at y 0.57 and -23.43 (v +-12), 3 mm thick, up to z 11.6. The lip underside runs parallel to the plinth chamfer with 0.3 mm normal gap and reaches 3 mm in. Lip tops at z 11.6 are 3.6 mm below the USB tunnel floor (z 15.2).
- Far end: in-plane flexure latch. Cantilever beam 2 mm thick, 40 mm long (root at y 8.57, free end at y -31.43, 1 mm gap to the wall). Riser to z 14 over y -31.43 to -17.43, lip 2 mm in (0.3 mm gap to the chamfer), 45 degree lead-in on top so lowering the Crown pushes the beam out. Thumb tab 5.5 x 5 x 10 at the free end. 2 mm of deflection gives about 0.4 % strain (3 t d / 2 L^2).
- Fit: hook the USB end under the two tongues, lower the far end, the latch clicks. Release: push the tab out (+x), lift the far end.
- The latch sits off-centre (y -24.4 against the axis -11.43). This is fine for a 150 g node, but check the hold on the bench.

**Dock_Plate (blank)**
- 3 mm thick, same outline as the ring with round corners at the bosses: 85.7 x 58.26 rectangle, 94.3 x 66.86 over the bosses.
- 34 mm aperture on the radar axis. 3 mm V datum notches on all four edges, on the radar axis lines (x 16.5, y -11.43).
- Four 2.9 mm screw holes with 5.2 x 2.0 counterbores from below. 0.4 mm relief pocket under the latch beam (x 70.5 to 74, y -32.43 to 8.57) so the beam doesn't drag.

**A6_Pad**
- The blank plate plus two ears at x 23.65 to 37.65 (centred on the plate, clear of the datum notches), each 11.7 mm out, with 4.5 mm holes at y 23.7 and -46.56 for M4 nylon screws (or use foam tape and no screws).
- A6_Gasket_sheet: ID 34, OD 54, 1.5 mm, under the plate (cut from sheet, not printed). OD 54 per coordinator item 14.1, so holes up to about 44 mm keep a 5 mm land.
- Crown outer face 4.5 mm above the lid. Hole range 25 to 44 mm (33 to 44 relies on the gasket overhang; bench test 3).

## Stage 3: A2 Span
**A2_Plate**: the blank plate plus four bar clips, which hang below the plate at x -12.2 to 1.8 and 31.2 to 45.2 (centred 21.7 mm either side of the radar axis).
- Each clip is a channel 19.45 x 9.725 inside (bar plus 0.2 mm), with 2.5 mm side walls and a 2 mm bridge underneath. The plate grows side tabs out to y 28.32 / -51.18 to carry the clips.
- A 4.5 mm hole in each bridge for an M4 x 10 nylon screw into the bar (3.4 mm self-tap hole).
- 5.6 mm access holes in the two left bridges, under the corner screw counterbores at (-12, 17.5) and (-12, -40.36), so a driver can reach the ring screws.
- Plate plus clips are 14.725 deep. Crown outer face sits 12.525 above the rim top (plate 3 + bar 9.525). Water must be at least 70 mm below the outer face, so 57.5 mm below the rim.

**A2_Bar_printed** (print 4: 2 per side)
- 3/8 x 3/4 in section (9.525 x 19.05), so a stock bar fits the same clips. Bars at |v| 18 to 37.05 (y 6.57 to 25.62 and -48.48 to -29.43).
- Each section runs from 13 mm off the radar axis out to the rim, with a 3 mm end tongue hanging 40 mm below the bar. The tongue's inner face is at RimOD/2 + 1 mm from the axis.
- Length = A2RimOD/2 - 12 mm, plus the 3 mm tongue. At the default 430 mm rim: 203 + 3 = **206 mm**, which fits a 220 mm bed. Largest rim that fits a 270 mm bed (Snapmaker U1): 250 + 3 mm pieces, rim OD about 518 mm.
- The two sections on a side butt under the plate with a 26 mm gap. The plate and clips are the splice, so there is no lap joint and no bolts in the beam (this replaces the 60 mm lapped sections of the concept).
- "Several lengths": set A2RimOD, recompute and re-export the bar STL. One STL is exported (rim 430).

**A2_Stock** (stock-bar version, rims up to 700 mm)
- Two stock 3/8 x 3/4 in HDPE or PVC bars, each A2StockRimOD + 2 mm long (702 mm for a 700 mm rim). Bar refs: A2_StockBar_ref_1/2.
- Four printed end caps (A2_StockCap): a 20 mm sleeve (0.3 mm clearance, 2.5 mm walls), and a 3 mm end wall that carries on down as the 40 mm tongue. Each has a 4.5 mm hole on the bar axis for an M4 x 10 nylon screw into a 3.4 mm hole drilled about 10 mm into the bar end.
- Drill the stock bar for the plate clips too: 3.4 mm vertical holes 21.7 mm either side of the bar centre, on the bar centre line.
- Sag at 700 mm is not calculated for the real stock material (bench test 5).

## Stage 4: A5 Expander (holes 50.5 mm and up)
- **A5_Plate**: the blank plate plus an integral body tube, OD 44, ID 34, hanging (A5TopT + 3 - A5Squeeze) = 4.5 mm below the plate.
- **A5_TPU_ring** (TPU 95A, separate body): ID 44.4, OD 50, height A5TopT + 3 = 6 mm, from the plate underside down. It covers the hole wall and reaches 3 mm below the top.
- **A5_CompRing**: ID 34, OD 50, 4 mm thick, under the TPU ring. Three nut pockets (M3 hex, 5.8 AF, 2.5 deep) on its underside.
- Three M3 nylon screws at r 19.5 (90, 210 and 330 degrees about the axis), from the plate top: 3.4 mm holes through plate, tube wall and ring, 6 x 2.5 counterbores in the plate top so the heads sit below the sole.
- The 1.5 mm gap between the tube end and the ring is the squeeze travel and the stop. Tightening closes it and the TPU bulges out against the hole wall. The Crown must be off the dock to reach the screws (coordinator item 14.4).
- Default top 3 mm: hole 50.5 mm (2 in saw 50.8). The stack bottom is 13 mm below the window face. Screw length about A5TopT + 9 mm (M3 x 12 for a 3 mm top).
- For tops thicker than 3 mm, also grow the bore to max(34, 28 + 2 x top) and the hole with it (hole = TPU OD + 0.5). That isn't automatic: only the heights follow A5TopT.
- The nut pockets break 0.4 to 0.85 mm into the bore (thin walls at r 19.5). This is cosmetic, but a bench check.

## Interference (Fusion, whole design, coincident faces excluded)
- Stage 2-4 parts against the sole, hood, hardware, boards and each other, each adapter checked in its service position: **none**.
- Remaining hits are all known from stage 1: Hood vs Hardware_Ref 0.0764 cm3 (heat-set inserts in their holes, a press fit by design), and three overlaps of 0.0001 to 0.0004 cm3 inside the water-level board STEP (C0603/C0402/R0402 models touching the PCB).
- The printed and stock A2 bars overlap each other only when both are put in service position (149.17 cm3, exactly bar against bar). In the assembly they are shown apart.
- Assembly display: the Crown sits in the dock on A6 Pad. The blank plate (y +110), A2 Span (y -130), A2 Stock (y -260) and A5 (y +240) are shown beside it (captured positions).

## Beam path (45 degree margin line r = 4 + d, d below the window face; -3 dB cone x 0.637 / 0.499)
| Part | Nearest edge to the axis | Margin there | Clear |
| --- | --- | --- | --- |
| Plate aperture (all plates) | r 17 at d 0 to 3 | r 7 | 10 mm |
| A6 gasket | r 17 at d 3 to 4.5 | r 8.5 | 8.5 mm |
| A2 bar inner face | r 18 at d 3 to 12.5 | r 16.5 | 1.5 mm |
| A2 clip inner wall | 21.2 mm radial at d up to 14.7 | r 18.7 | 2.5 mm |
| A5 bore (tube + ring) | r 17 at d 3 to 13 | r 17 at d 13 | 0 at the very bottom edge; the -3 dB cone is r 10.8 there, so 6.2 mm |
No metal anywhere in or near the beam. The only metal in stages 2-4 is the four brass ring inserts, 36 mm or more from the radar axis.

## AE1 clearance
- Dock ring: the nearest ring material is 23.1 mm from the AE1 reference box (ring wall top, z 4, against AE1 at z 17). The latch riser (z 14 max) is at x 68.5 to 72.5, about 23 mm from AE1 in x.
- Nothing in stages 2-4 rises above z 14, so AE1 (z 17 to 18.3, behind the hood wall) isn't boxed in by the dock ring or any plate.
- Brass inserts in the ring bosses: about 38 mm from AE1. A5 screws and nuts nylon. A2 and A6 screws nylon.
- Stage 1, H4: the feather's H4 nylon screw head is 0.49 mm from the AE1 reference box. H4 is inside the AE1 corner keep-out on the PCB itself, so it must stay nylon (same as Tidemark: hardware_pad_check 0.24 mm).
- The sole-post insert under H4 is about 11.8 mm below AE1. The model's Hardware_Ref bodies carry no material, so I can't confirm from the model whether stage 1 meant brass or nylon there. Use a nylon screw and nut at H4, or put it on the antenna bench test if brass is used.

## TC2030 / radar update access
- J1 pads face the sole, between the H1/H2 posts. The plug needs the board stack lifted off the sole posts, so **stack out**: lift the hood, unscrew the nylon stack, plug in. Lid-off alone is not enough.
- The dock changes nothing: press the latch tab and lift the Crown off first. The sole pry notch is covered by the ring wall while docked, so the Crown has to come off the dock before it can be opened.

## Printing (PETG, 4 perimeters, window and plates 100 % solid; no supports on any stage 2-4 part)
| STL | Count | Orientation | Notes |
| --- | --- | --- | --- |
| crown_dock_ring.stl | 1 | as exported (bottom on bed) | Hook and latch lip undersides are 45 degrees. Press inserts into the boss holes from the bottom face |
| crown_dock_plate_blank.stl | 1 | flip: plate top (sole side) on the bed | Counterbores face up |
| crown_a6_pad_plate.stl | 1 | flip: top on the bed | |
| crown_a2_span_plate.stl | 1 | flip: top on the bed, clips grow up | Clip bridges span 19.45 mm (bridging, no supports; check the first print) |
| crown_a2_bar_section_rim430_x4.stl | 4 | on its 9.525 x 206 side face, tongue lying flat | 206 mm long at rim 430 |
| crown_a2_stockbar_endcap_x4.stl | 4 | outer end face (end wall plus tongue) on the bed | Only for the stock-bar version |
| crown_a5_expander_plate_top3.stl | 1 | flip: top on the bed, tube grows up | Made for a 3 mm top |
| crown_a5_compression_ring.stl | 1 | TPU-side face on the bed, nut pockets up | |
| crown_a5_tpu_ring_top3_TPU95A.stl | 1 | flat | TPU 95A (PETG only as a fit check) |
| crown_sole.stl | 1 | outer (window) face down on smooth PEI | Window 100 % solid (stage 1 rule) |
| crown_hood.stl | 1 | roof down (stage 1 / concept 3.3); the plinth flare overhangs at 45 degrees | Orientation from the concept, not re-checked |
| crown_bonnet.stl | 1 | top down | |
| crown_key.stl, crown_lightpipe.stl | 1 each | flange down | PETG for the first print |
STLs are exported in model (service) orientation, in mm. Rotate them in the slicer as above. Nothing has been sent to a slicer or printer.

## Hardware for stages 2-4, checked against mechanical\hardware_lists\enclosure_hardware_amazon_2026-11-01.md
| Item | Qty | On the list? | Use |
| --- | --- | --- | --- |
| M2.5 brass heat-set insert 4 x 4 mm (B0DPQK6RJZ, item 2) | 4 | yes (pack of 100) | Ring bosses, 3.6 mm holes, 5 deep |
| M2.5 x 6 nylon screw from the standoff kit (B0B5M1M822, item 6) | 4 (one set moves with the ring) | yes | Plate to ring, from below. Needs a head of 2.0 mm or less (counterbore 5.2 x 2.0); head size not checked |
| M4 x 10 nylon pan head (Essentra 50M040070N010, item 17 type) | 4 printed A2; 8 stock A2 (4 clips + 4 caps) | type on the list (2 bought for Perch), **need 8 more** | Self-tap into 3.4 mm holes |
| M4 nylon screws for the A6 ears | 2, optional | not on the list | Length depends on the lid; foam tape instead |
| 1.5 mm closed-cell or EPDM gasket sheet | 1 ring 34/54 | **not on the list** | A6 |
| M3 nylon pan head screw (head 5.5 mm or less, about 2.4 tall), M3 x 12 for a 3 mm top | 3 | **not on the list** | A5 |
| M3 nylon hex nut, 5.5 AF x 2.4 | 3 | **not on the list** | A5 compression ring |
| 3/8 x 3/4 in HDPE or PVC flat bar, 702 mm | 2 | **not on the list**; availability not checked | A2 stock version |
| TPU 95A filament | A5 ring | Brian has it | |
| Bull's-eye vial 6-8 mm | 1 per adapter | not on the list, **not modelled** | Levelling (mounting.md rule 6) |

## Assumptions
- Plinth chamfer is exactly 45 degrees, 6 mm in, from z 8 to 14 (read from the stage 1 section). Hook gaps rely on it (bench test 1, mounting.md).
- XM125 face is at z 4.0 (stage 1 model). Beam half angles and which plane lies along the board are still UNVERIFIED (mounting.md).
- Stock bar section 3/8 x 3/4 in chosen so printed and stock bars share one plate. Mounting.md assumed 20 x 8 mm, which isn't a standard stock size.
- Nylon M2.5 kit screw head 2.0 mm or less, Essentra M4 nylon self-taps into 3.4 mm PETG holes, M3 nylon nut 5.5 AF: not measured.
- A2 bars rest flat on the rim. The 40 mm tongues locate on the outside of the rim with about 1 mm play. TPU pads not modelled.
- A5 hold force and seal not calculated (bench test 6).

## Open questions for Brian
1. Fusion save: free an editable-document slot (Personal plan limit, likely), then open and save `feather_water_level_enclosure_crown`, and delete `crown_stage1_housing`. Or tell me another project to use.
2. **Dock polarity:** the Crown foot is a plain rectangle, so it also fits the dock turned 180 degrees. The radar then sits 28.3 mm off the aperture centre, and the plate covers the beam. Add the 8 x 8 mm polarity chamfer (mounting.md section 3, request 1) to the sole and plinth corner and a matching block in the ring? That touches the stage 1 sole and hood.
3. A2 bar size: is 3/8 x 3/4 in HDPE or PVC bar OK, and do you have a source? Which rim diameters do you want STLs for (default 430)?
4. A5: OK to buy nylon M3 screws and nuts (DigiKey Essentra, like the Perch parts)? What top thicknesses (sets the bore, hole and screw length)?
5. A6: gasket material (closed-cell foam or EPDM), and ears with M4 screws or tape?
6. H4 sole-post insert: confirm nylon hardware at H4, or put brass on the AE1 bench test.
7. Drip lip, vial seat and "lvl" engraving not modelled. Wanted on the first print?
8. The latch is off-centre (y -24.4). Accept for the first print, or add a second latch?

## Files
- Renders: crown_stage1_iso.png, crown_stage1_section_radar_battery.png, crown_stage1_bottom.png (previous run); crown_stage2_dock_a6_iso.png, crown_stage2_section_radar_axis.png, crown_stage3_a2_span_overview.png, crown_stage3_a2_plate_clips_underside.png, crown_stage4_a5_section_radar_axis.png, crown_stage4_a5_expander_underside.png, crown_draft_assembly_overview.png.
- Assembly STEP: C:\Personal-Agents\shared\handoff\feather_water_level_tc2030\enclosure\crown_draft_assembly_2026-11-11.step (whole design, adapters shown apart as above).
