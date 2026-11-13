# Crown battery lead path check (2026-11-12)

Measured in Fusion doc `feather_water_level_enclosure_crown v1` (unsaved view-state changes only; model not changed). World coords as in NOTES.md (z 0 = window face). All mm.

## Important: what the model really contains at U4
The Board_Feather STEP has **no 3D model for U4**. What is in the doc are two placeholder boxes in `Ref_Feather_Parts`:
- `PH_U4_JST_batt` (socket): x 8.5 to 14.85 (6.35 wide, centre 11.675), y -22.69 to -15.09, z 16.985 to 22.985 (6.0 tall on the PCB top).
- `PH_U4_PH2_plug` (plug): x 8.5 to 14.85, y -25.86 to -22.69 (only **3.17 long**), z 17.385 to 20.885 (3.5 tall, centre z 19.135).
Differences from the coordinator's STL numbers: socket centre x 11.675 here vs 11.95 (0.275 off); socket front face y -22.69 here vs board edge -22.86 (0.17). The plug box is not a JST PHR-2 shape. Treat it as a stand-in.

## Measurements
| Item | Value |
| --- | --- |
| Feather PCB | y -22.86 to 0, z 15.475 to 16.985 (top 16.985) |
| U4 socket front face | y -22.69 (model box); coordinator: board edge -22.86 |
| U4 socket top | z 22.985 |
| Hood inner -y wall | y -28.86 (outer body -31.36, wall 2.5) |
| Gap socket front to wall | 6.17 (6.00 from the board edge) |
| Roof | z 23.985 (underside) to 26.485 (top), 2.5 thick |
| Roof hole | dia 4.0 (cylinder r 2.0 checked), centre (10.5, -26.5), x 8.5-12.5, y -28.5 to -24.5 |
| Socket top to roof underside | 1.00 |
| PCB top to roof underside | 7.0 |
| Hole -y edge to wall inner face | 0.36 (in plan; solid roof above, no print issue) |
| Hole vs pins | hole centre is 1.45 toward -x of the pin pair centre (pins x 10.95 / 12.95, per coordinator); 1.18 from the placeholder centre. Right pin (x 12.95) is 0.45 outside the hole circle edge |
| Hole vs plug back (model plug) | plug back y -25.86 lies 0.64 on the +y side of the hole centre; the hole covers y -24.5 to -28.5, so 1.36 of the plug rear is under the hole and 2.64 beyond the plug back is open down to the hole edge |
| Neighbouring bosses under the roof | insert bosses at (2, -26.3) and (19, -26.3), r 3.2, hang to z 20.985. Hole edge to boss edge: 3.3 each side (clear) |
| Cell (Ref_Battery, with 1 mm pad) | x -0.5 to 19.5, y -20.0 to 0, pad z 26.485-27.485, cell 27.485-32.485 |
| Cell -y edge to hole | 6.5 to the hole centre, 4.5 to the hole's +y edge |
| Bonnet (outer) | x -3 to 22, y -31.36 to 8.5, z 26.485 to 34.985; walls 2; inner ceiling z 32.985 |
| Divider rib in bonnet | full width x -1 to 20, y -22.5 to -20.5, hangs from the ceiling down to z 28.485. Gap under it to the roof top: 2.0 |
| Splice compartment (-y of the rib) | y -29.36 to -22.5 (6.86), z 26.485 to 32.985 (6.5), x -1 to 20 but the two screw bosses (r about 3.1, at x 2 and 19, y -26.3) take the ends. Free between bosses: **x 5.1 to 16.0 (10.9) x y -29.36 to -22.5 (6.9) x 6.5 high** |

Pictures in this folder: `section_x11.95_U4_wall_roof.png` (plane x = 11.95 through U4, hole and wall), `section_y-26.5_roof_hole.png` (plane y = -26.5 through the hole, seen from +y so +x is left), `top_roof_hole_bonnet_hidden_zoom.png` and `top_roof_hole_bonnet_hidden.png` (top view, bonnet and cell hidden: top of the hole shows plug/socket, the rest is open to the hood cavity), `section_z27.5_bonnet_plan.png` and `section_z30.5_bonnet_plan.png` (plan of the bonnet compartment, hole visible through the floor; z 30.5 shows the rib), `section_x11.95_overview.png` (first, wider shot).

## Mated plug and bend room
Plug length beyond the socket front (p) decides everything. Room behind the plug before the wall = 6.17 - p:
| p | Plug back y | Room to wall | Room to hole far edge (-28.5) |
| --- | --- | --- | --- |
| 3.17 (model box) | -25.86 | 3.0 | 2.64 |
| 4.5 | -27.19 | 1.7 | 1.3 |
| 6.0 (coordinator assumption: 6.0 wide x 4.5 high, 6 mm out, wires straight from the back; check against the JST PH datasheet, I could not open it) | -28.69 | **0.17** | none: plug back is outside the hole and almost on the wall |

Vertical: wire exit about z 19.1-19.7 (plug mid height), roof underside 23.985, so 4.3-4.9 to rise, then 2.5 through the roof. The plug (3.5 or 4.5 tall) clears the roof by at least 1.8, so the plug itself fits under the hood.

- With the model box (p 3.17): the wire must go from horizontal to vertical inside the hole. Largest centre-line bend radius that still lands in the hole is about 2.0 (wire centre at y -27.85 with 1.3 mm wire). Works for thin wire (AWG 28 silicone, OD about 1.0, radius about 2 x OD); too tight for AWG 26 PVC.
- With p 6.0: the path does not work. The wires cannot leave the plug back (0.17 mm from the wall), and the hole is beside the plug, not behind it.
- X alignment: straight wires at 2.0 pitch (x 10.95 / 12.95) do not fit the hole (right wire 0.45 outside the circle). The pair has to be bundled or twisted and shifted at least 1.1 toward -x over the 4-5 mm rise. Easy with flexible wire, not with stiff wire.

## Verdict
1. **Does the path work as modelled?** Not proven. It works only if the real PHR-2 plug sticks out about 3.5 mm or less beyond the socket and the wire is thin and flexible (AWG 28 or smaller). With the coordinator's 6 mm plug it fails (bend room 0.17, under the 3 mm threshold). Check the JST PH/PHR datasheet length first: that single number decides it.
2. **Assembly order (plug PH into U4 with the stack out, thread wires up through the hole while lowering the hood, then splice to the cell and fit the bonnet):** possible in principle, and it is the only order that works, because the plug sits under the roof and cannot be reached once the hood is on. Needs bare wire ends (nothing wider than the 4 mm hole going through), a bundled pair, and the plug fully seated before the hood comes down. The hole is 1.0 above the socket top, so check the hood does not push the wires into the socket top while lowering.
3. **Splice room:** compartment between the bosses is 10.9 x 6.9 x 6.5. A standard 15-20 mm inline heat-shrink splice does not fit straight (diagonal about 12.8). Stagger the two solder joints (each about 6 mm with its own sleeve), or splice at the cell chamber's -y corner. The cell's own 12 mm lead plus SH plug reaches the compartment through the 2.0 mm gap under the rib if the cell lead leaves on its -y edge (6.5 mm from the hole); where the cell lead really exits is not in the model, so check on the part. Alternative: skip the splice and put a JST SH socket pigtail on the PH side (a PH-to-SH adapter lead), which then plugs onto the cell lead plug in the compartment.
4. **Pigtail length** (plug back to free end): about 10 mm to reach the hole and rise to the roof, plus 15 mm beyond the roof top to work with, plus 5-10 mm of slack for lifting the hood off with the stack out: order or make **40-45 mm** from plug back to bare end, trim to fit. About 25 mm of it ends up inside the hood and compartment.

## Proposed smallest model changes (not made)
- If the datasheet plug is about 3.5 mm or less: no change needed; use AWG 28 silicone wire. Optional: stretch the hole into a slot toward +y (y -28.5 to -23.5, 4 wide) so the wire can rise anywhere over the plug back and the bend radius is not limited by the hole. The slot still clears the rib (y -22.5) and the bosses.
- If the plug sticks out 6 mm (bend room under 3 mm): the hole alone cannot fix it. Smallest change is to push the hood -y wall (and the bonnet -y wall and the hole) out: `CableSide` from 6 to about 11 mm (+5), hole centre to about y -31.2, x about 11, and the compartment grows by the same amount. This enlarges the foot, the dock ring recess and the plates by 5 mm in y, so it is a real change, not a tweak. A cheaper way to get the room is a sunken pocket in the hood -y wall behind the plug, but the wall is only 2.5 thick, so I do not recommend it. Cheapest of all: a different cable direction (right-angle crimp or a pre-bent plug), if the part exists.

## Fusion doc state
No model change. Hid and re-showed bodies, toggled the origin/construction/sketch/joint display folders (all set back to visible; individual entity visibility was not touched), set the camera to a top view, orthographic. Added section analyses Section4 to Section8 and cleared them all (none left). No temporary sketches or bodies. Not saved, saved-as, uploaded or deleted. The doc was already "modified" with unsaved view state before this check and still is. Other open docs untouched.


## Coordinator follow-up 2026-11-12: JST datasheet
JST PH catalogue (jst-mfg.com ePH.pdf, page 3), read by the coordinator:
- PHR-2 housing: 5.8 wide (B), 4.5 thick, **6.85 long** along the mating axis.
- S2B-PH-K-S side-entry header: 4.8 high, 7.6 long along the mating axis (incl. the 3.4 pin tail).
- The catalogue gives no mated dimension. The housing sits inside the header shroud, so it sticks out beyond the header front by 6.85 minus the insertion depth. With an estimated insertion depth of about 3.5-4 mm (header 6.0 tall top-entry, minus a ~2 mm base), that is **about 3 mm**. This matches the 3.17 mm placeholder plug in the model, so the 3.0 mm bend room row applies. It's an estimate: measure a real mated pair (calipers, plug back to header front) before printing.
- Result: path works with AWG 28 silicone wire. Optional: stretch the roof hole to a slot toward +y (y -28.5 to -23.5, 4 wide) for more bend room.
