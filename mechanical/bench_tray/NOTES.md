# prog_adapter Bench Tray, first-draft print (plain PETG), 2026-11-07

Concept 1 "Bench Tray" from `..\enclosure_concepts_2026-11-07\concepts.md`, Brian's decisions of 2026-11-07 (printed flat, no riser yet, M3 x 4 heat-set inserts, ribbon notch in the right wall near J3, plain PETG single material, TPU feet as separate bodies).

Fusion document: `prog_adapter_enclosure_bench_tray` (project Fish_Stuff, folder Prog_Adapter), URN urn:adsk.wipprod:dm.lineage:w81Ea0ZrRaeVThbitRWpOQ.
Versions: v1 = board STEP imported, v2 = stage 1 (tray body, pocket, posts, pillars, insert holes, wall openings, bay pockets), v3 = stage 2 (strain-relief tab, underside features, TPU feet, hardware reference bodies), v4 = stage 3 (checks, screenshots). STLs and STEP exported from v4 (no geometry change after v4).

Board STEP used: C:\Personal-Agents\shared\handoff\prog_adapter\prog_adapter_2026-11-07.step (occurrence `prog_adapter_2026-11-07 1:1`, moved by (-100, +148, 0) and captured as Position1). Nothing on the board was changed.

Nothing was sent to a slicer or printer.

## Files
| File | What |
| --- | --- |
| print_draft_2026-11-07\prog_adapter_bench_tray_PETG_floor-down.stl | The tray, as modelled = print orientation (floor on the bed) |
| print_draft_2026-11-07\tpu_parts_optional\prog_adapter_bench_tray_feet_x4_TPU95A.stl | Four 8.8 x 8.8 x 1.5 mm feet (one STL, four bodies). Optional; leave off for the draft or print in TPU later |
| bench_tray_iso.png, bench_tray_top.png | Views with the board and the M3 screws fitted |
| bench_tray_section_J6.png | Section on the XZ plane at Y 12.7 (through the USB-C axis), seen from the back, so the left wall is on the right of the picture |
| bench_tray_section_J3.png | Section on the XZ plane at Y 36.96 (through J3, J1, J2, JP1, J4), seen from the back: the right wall with the ribbon notch is on the left of the picture, the strain-relief tab on the right |
| C:\Personal-Agents\shared\handoff\prog_adapter\enclosure\prog_adapter_bench_tray_2026-11-07.step | Whole assembly: board, tray, TPU feet, inserts and screws (review only) |

## Model frame
X = board x (0 at the left edge, J6/J7 side; 72 at the right edge, the 9160 DK side). Y = 48 - KiCad y (Y 0 = front edge at J5, Y 48 = rear edge at J1/J2). Board bottom Z 0, board top Z 1.6 (STEP board body is 1.51 thick; parts sit at Z 1.595). Front of the tray (the bay) is -Y.

## Measured from the STEP (not from the concept renders)
| Item | X | Y | Z top | Note |
| --- | --- | --- | --- | --- |
| H1-H4 (M3, 3.2 mm) | 3.5 / 68.5 | 3.5 / 44.5 | | Concept said 3.4; STEP is 3.5 from each edge |
| J6 USB-C shell | 0 - 7.78 | 8.23 - 17.17 | 4.905 | Axis Y 12.7, Z 3.255; mouth flush with the board edge |
| J7 FTDI pads | 7.6 | 26, 29, 32 | | Zip slots 1.5 wide at Y 23.1 and 34.9, X 1.0 - 5.2 |
| J1 box header | 15.82 - 31.10 | 32.06 - 41.16 | 10.695 | 9.1 above the board |
| JP1 | 32.53 - 35.07 | 36.73 - 41.81 | 10.135 | |
| J3 (STEP model) | 40.94 - 44.34 | 33.79 - 40.14 | 5.595 | STEP has a plain 2x5 header. Shroud from the CNC drawing: 5.1 x 11.25 centred at (42.64, 36.96), i.e. X 40.09 - 45.19, Y 31.34 - 42.59; shroud height not known |
| J4 1x6 | 47.23 - 49.77 | 28.03 - 43.27 | 10.135 | |
| J2 box header | 56.35 - 65.45 | 25.82 - 41.10 | 10.695 | |
| SW1 / SW2 | 26.56 - 33.74 / 40.06 - 47.24 | 24.25 - 30.25 / 10.75 - 16.75 | 5.895 | Button tops 4.3 above the board |
| D1 | 30.4 - 32.4 | 11.33 - 12.58 | 2.695 | |
| J5 1x3 | 14.73 - 22.35 | 2.23 - 4.77 | 10.135 | |
| Underside | | | -1.905 | Lowest point = SW legs; header tails -1.405, J3 tails -0.705. No SMD parts on the bottom |

## Overall size
| | X x Y x Z, mm |
| --- | --- |
| Tray with the strain-relief tab | 85.6 x 67.2 x 12.6 |
| Tray without the tab | 77.6 x 67.2 x 12.6 |
| On TPU feet | +1.0 mm height (feet 1.5 thick, 0.5 in their pockets) |
| Header tops above the desk (no feet) | 16.7 (J1/J2), 16.1 (J4/J5/JP1) |
Volume 26.3 cm3 (solid). The board pocket is 72.8 x 48.8 with R2.4 corners; the front bay is a solid deck 16 mm deep, flush with the rim.

## User parameters (Modify > Change Parameters)
| Name | Value | Drives |
| --- | --- | --- |
| Wall | 2.4 mm | Side, rear and left/right wall thickness (outline = board + 2 (BoardClr + Wall)) |
| BoardClr | 0.4 mm | Board edge to inner wall, each side |
| PcbT | 1.6 mm | Board thickness |
| RimH | 5 mm | Rim above the board top (rim at Z 6.6); also the bay deck top |
| FloorT | 2 mm | Floor thickness |
| PostH | 4 mm | Floor top to board bottom (air under the pin tails) |
| PostOD | 7.5 mm | Corner posts |
| InsertD / InsertDepth | 4.1 / 5 mm | Heat-set insert holes (4 corner posts and the 2 riser holes) |
| PillarD | 3.5 mm | 12 support pillars under the press points |
| CornerR | 6 mm | Outer vertical corners |
| BayD | 16 mm | Front bay depth |
| PlugL / PlugW / PlugDepth | 22 / 12 / 8 mm | TC2030-IDC plug pocket, **placeholder** |
| ShuntL / ShuntW / ShuntDepth | 5.6 / 3.0 / 4 mm | JP1 shunt pocket (shunt stands upright, 2 mm proud) |
| LabelDepth | 0.6 mm | Label recess (34 x 10 mm, fixed size) |
| UsbW / UsbH | 13.5 / 8 mm | USB-C opening, centred on the J6 axis |
| WireNotchW | 10 mm | FTDI wire notch, centred on Y 29 (J7) |
| RibbonNotchW / RibbonNotchDepth | 10 / 2 mm | J3 ribbon notch in the right wall, centred on Y 36.96 |
| FootPocketD / FootT | 0.5 / 1.5 mm | TPU foot pockets and pads (9 x 9 pockets, 8.8 x 8.8 pads) |
| TieGrooveD | 1.5 mm | Zip-tie groove under the strain-relief tab |
| TieRecessD | 1 mm | Floor recess under the J7 zip slots (room for the tie lock) |
Not parameter-driven (fixed coordinates from the STEP): post, pillar and insert positions, the USB/wire/ribbon centre lines, bay pocket X positions, label recess size, feet and riser hole positions, the strain-relief tab and its slots. The sketch profile order in TR_bay and TR_wallcuts is used by index; check the cuts after a big parameter change.

## Features
- **Board support:** four posts at H1-H4 (7.5 mm, merge into the walls at the corners) with insert holes, plus 12 pillars (3.5 mm) touching the board bottom: SW1 centre, SW2 centre, both ends of J1 and J2 (under the shroud ends), front and rear of J3, beside J4, either side of J5, beside JP1. Each pillar was placed against the hole list from the STEP; nearest pin tail 1.39-1.57 mm from a pillar edge (bare pin; a normal solder fillet still leaves about 1 mm).
- **Left wall:** USB-C opening 13.5 x 8 mm centred on the J6 axis, open at the top (the 8 mm height runs above the rim, so it is a U notch and needs no bridge); its floor is at Z -0.75. FTDI wire notch 10 mm wide (Y 24-34, between the J7 zip slots), floor at the board top. Outside it, a strain-relief tab (8 mm long, 17 mm wide, top at the notch floor) with two 3.0 x 1.8 mm zip-tie slots lined up with the board's J7 zip slots (Y 23.1 and 34.9) and a 1.5 mm groove under it, so a second 2.5 mm tie can clamp the cable jacket to the tab.
- **Floor recess** 6 x 18 x 1 mm under the J7 zip slots for the board tie's lock head (5 mm of air there).
- **Right wall:** 10 mm wide, 2 mm deep notch centred on J3's row (Y 36.96) for the 10-pin ribbon (see open question 3).
- **Front bay:** JP1 shunt pocket (X 3-8.6), TC2030-IDC plug pocket (X 11-33, placeholder), label recess 34 x 10 x 0.6 (X 37-71).
- **Riser provision (cheap, unused now):** two blind M3 insert holes (4.1 x 5 mm) in the bay underside at (40, -8.4) and (58, -8.4), under the label recess. A riser can screw on from below later; the concept's 8 degree riser needs only these two plus its own feet.
- **Feet:** four 9 x 9 x 0.5 mm pockets in the bottom; TPU pads are separate bodies (component Feet_TPU).

## Checks
- **Interference (whole design, assembly_inspect_interference):** tray vs board and all its parts: **none**. Feet vs tray: none. The only tray overlap is with the insert reference bodies (103 mm3 = the 5.0 mm insert OD melting into the 4.1 mm holes, by design). The two SW-to-PCB hits are inside the vendor STEP (legs in their holes, zero volume), not the tray.
- **Clearances (Fusion measure, tray body to part):**
  - USB-C J6: 1.26 mm (FL post top to the shell tab at the board, Z 0 to 0.745); 2.31 mm from the opening sides to the shell sides; opening floor 2.39 mm under the shell bottom. Opening vs a 12.5 x 7 mm plug overmould: 0.5 mm each side, 0.5 mm under it, open above.
  - J1 box header: 1.48 mm (pillar to pin tail); shroud to rear wall 7.2 mm.
  - J2 box header: 1.55 mm (pillar to pin tail); shroud to right wall 6.95 mm.
  - J3: 1.48 mm (pillar to pin tail); shroud (CNC drawing size) to rear wall 5.8 mm.
  - J5: 2.6 mm to the bay deck face (the deck top is 3.5 mm below the J5 pin tips).
  - M3 screw heads (5.7 mm) to the nearest parts: J6 1.9 mm, J2 1.7 mm.
  - Rim Z 6.6: below every header top (J1/J2 10.7, J4/J5/JP1 10.1); above the button tops (5.9), but the buttons are 18 mm or more from any wall. All silk, JP1, SW1, SW2, J4, J5 and D1 are open from above.
  - Floor to the lowest pin tail (SW legs): 2.1 mm.

## Hardware (new buys, not on the 2026-11-01 Amazon list)
| Qty | Item | Where | Notes |
| --- | --- | --- | --- |
| 4 (+2 for a riser later) | M3 brass heat-set insert, 4 mm long x 5 mm OD (the common Amazon "M3 x 4 x 5" knurled insert) | Corner posts; 2 riser holes | **Assumption:** these inserts are usually listed for a 4.0-4.2 mm hole; the model uses 4.1 mm (`InsertD`), 5 mm deep. If the listing gives another hole size, change `InsertD`. Insert flush with the post top. No ASIN picked (Amazon not checked in this run) |
| 4 | M3 x 6 button head socket screw, 304 stainless | Board to posts | 1.6 board + 4.4 into the insert; tip 0.4 past the insert, inside the 5 mm hole. M3 x 5 also works (3.4 engagement) |
| optional | TPU 95A for the feet, or stick-on rubber feet about 8-10 mm square | Feet pockets | Draft: leave the feet off |
| 1-2 | 2.5 mm wide cable tie | J7 board slots (already planned) + strain-relief tab | |
In the model: `Hardware_Ref` has the inserts (tube 5.0 OD x 3.0 bore x 4 mm, Z -4 to 0) and the screws (head 5.7 x 1.65 on the board top, shank 3.0 x 6). Not printed, not in the STLs.

## Print (PETG, first draft)
- Orientation: as exported, floor on the bed. **No supports.** Every opening is open at the top (USB-C, wire notch, ribbon notch, bay pockets, insert holes). The only bridges are on the bed side: the 9 mm foot pocket ceilings (0.5 mm deep), the 3 mm wide groove under the strain-relief tab, and the 4.1 mm riser hole ceilings.
- Suggested: 0.4 nozzle, 0.2 mm layers, 3 perimeters, 20-30 % gyroid, 240 C / 75 C (adjust to the spool). The bay deck is solid in the model; infill keeps it light.
- Print time and filament: **not sliced** (no slicer run, per the rules). Rough estimate from the volume (26.3 cm3 solid): about 2.5-3.5 h and 15-20 g at the settings above. The concept guessed 5 h.
- Heat-set the inserts with the tray on a flat surface; stop flush with the post top.

## Assumptions
- Board bottom at Z 0, top at Z 1.6 (STEP board body 1.51, parts at 1.595).
- USB-C plug overmould up to 12.5 x 7 mm (opening 13.5 x 8, open top).
- FTDI TTL-232RG cable jacket about 4.5-5 mm round; it lies on the board top through the 10 mm notch (notch is 5 mm deep).
- J3 shroud: 5.1 x 11.25 mm from the CNC drawing (STATUS.md), height unknown; it is 5.8 mm or more from every wall in plan, so its height does not matter for the tray.
- TC2030-IDC plug pocket size is a placeholder (22 x 12 x 8).
- JP1 shunt (Sullins SPC02SYAN, about 5.1 x 2.5 x 6) parks upright in the shunt pocket.
- J7 wire tails (not in the STEP) trimmed to less than 3 mm under the board (4 mm of air; the 1 mm floor recess only covers the zip-slot area X 0.2-6.2, not the pads at X 7.6).

## Conflicts with the PCB
None blocking. No part is in the way of an opening, and the holes match (3.5 mm from each edge; the concept's 3.4 was a render reading).
- Note on the J3 ribbon (not a board conflict, a routing fact): J3 sits in the middle of the board (X 40-45), and its ribbon exits sideways toward +X across J4 (pins 8.5 above the board) and J2 (box header 9.1 above, plus the TC2030-IDC socket when section B is in use). So the ribbon passes the right wall above J2 at roughly Z 12-16, well over the 6.6 mm rim. The 2 mm notch is only a guide; a deeper notch would not let the ribbon go lower.

## Open questions for Brian
1. TC2030-IDC plug size: measure the real plug (length, width, height) and set `PlugL`, `PlugW`, `PlugDepth`.
2. Shunt pocket in the bay: keep it, or keep the shunt parked on one JP1 pin?
3. J3 ribbon notch: OK as a shallow guide over J2, or would you rather route the ribbon out the rear wall at the right-rear corner (a rear notch near X 60-70)?
4. Insert hole: confirm the hole size on the insert listing you buy (model 4.1 mm).
5. TPU feet now, stick-on feet, or none for the draft?
6. Strain-relief tab on the left (adds 8 mm of width): keep, or rely on the board's own J7 zip slots only?
