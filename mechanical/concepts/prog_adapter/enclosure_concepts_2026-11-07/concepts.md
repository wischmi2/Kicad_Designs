# prog_adapter enclosure concepts (2026-11-07)

Concepts only, no CAD. Side-by-side view: index.html. Sketches: 01-tray.svg, 02-console.svg, 03-quadpost.svg.

## 1. Brief
- Board: prog_adapter rev 0.1, 72 x 48 x 1.6 mm, 2 mm corner radius, four M3 NPTH holes at (3.4, 3.4), (68.6, 3.4), (3.4, 44.6), (68.6, 44.6) mm from the top-left corner (read from the top render, 21.4 px/mm; +-0.3 mm).
- Source: prog_adapter\STATUS.md, renders in shared\design\prog_adapter\, STEP 2026-11-07. A design review is running; the USB-C J6 position on the left edge may shift, so every concept leaves the whole left edge open or has a wide opening there.
- Positions read from the top render (mm from top-left, body footprints, rounded):

| Item | x | y | Note |
| --- | --- | --- | --- |
| J1 box header | 15.7-31.2 | 6.7-15.8 | notch to the top edge, plug from above |
| JP1 | 32.4-35.2 | 4.8-11.3 | shunt needs a pull-up gap |
| XM RESET (SW1) | 26.4-34.6 | 17.7-23.9 | |
| J7 FTDI pads | 6.6-8.4 | 15-22 | wires from the left; zip slots at y 12-14 and 24-26, x 1.4-4.7 |
| J3 10-pin 1.27 | 40-45.3 | 5.2-16.8 | |
| J4 1x6 | 46.7-54.7 | 4.2-20.4 | pins stand about 8.5 mm over the PCB (assumed, check STEP) |
| J2 box header | 56.2-65.4 | 6.7-22.2 | 6.6 mm from the right edge |
| SWD RESET (SW2) | 39.5-48 | 30.9-37.5 | |
| J6 USB-C | 0-7 | 30.7-40 | on the left edge |
| D1 PWR LED | 29.9-33 | 35-37 | |
| J5 1x3 | 14.5-22.5 | 43-46 | |
- Height assumption: box-header shroud and pin headers about 9 mm over the PCB top (check in the STEP before modelling). Through-hole pin tails about 2 mm under the board, so the board needs 4 mm of air below.
- Use: bench tool next to a 9160 DK, indoors, many ribbons and one cable plugged in from above and the sides, must not slide, must survive a knock off a desk. First print is plain PETG, single material (Brian 2026-10-29), TPU only as separate bodies (feet).
- Family nod (Tidemark/Ledger): Abyss navy matte PETG, coral accent (buttons, tag, feet rings), lowercase tag debossed 0.4 mm ("prog"), 2 mm walls, large radii (R6 vertical corners on the Ledger). None of it is for the first draft.

## 2. References (from Brian's own enclosures, nothing external researched)
- Ledger NOTES.md: 2 mm walls, 12.5 x 7 mm USB-C opening with R2 corners and 0.8 mm outside chamfer, 15 degree wedge stand with TPU foot strips and a cable groove under it. Teaches: wedge as a separate part, groove under for cables.
- Tidemark decisions: Abyss navy + coral + lowercase tag. Teaches the colour and label language.
- Hardware list (Amazon 2026-11-01): M2 and M2.5 inserts and screws, M2.5 nylon standoffs. No M3 items. The board holes are M3, so M3 hardware is a small new buy (see below).

## 3. Hardware common to all concepts
- The M3 holes are the only fixings. Draft: M3 x 8 self-tapping or thread-forming pan-head screws into 2.6 mm pilot holes in printed posts (no new parts beyond the screws). Better from print 2: M3 heat-set inserts, 4 mm long (about $8 per 100, new buy, not on the 2026-11-01 list), M3 x 6 button heads.
- Printed posts (4 mm tall, 6 mm diameter) hold the PCB 4 mm above the floor.
- Feet: 4 TPU 95A pads (about 12 x 12 x 1.5 mm, separate bodies, glued in 0.3 mm deep pockets). Draft prints them in PETG or leaves them off.
- Do not drive the M3 screws hard into PETG posts; stop at the first resistance.

## 4. Concept 1: BENCH TRAY (open top, tilt riser)
Idea: a shallow navy tray the board drops into. The top stays fully open, so every silk legend is readable and every ribbon plugs in from above. The extras live in the tray, not on the board.
- Form: outer 77.4 x 67.4 x about 14 mm flat. Board pocket 72.6 x 48.6, walls 2.4 mm, floor 2 mm, posts 4 mm, wall rim about 5.4 mm over the PCB top (rim below the headers, above the buttons). A 14 mm deep front bay carries a TC2030 plug pocket (size to be measured, placeholder 22 x 12 mm), a shunt pocket (7 x 3 mm slot for the JP1 shunt on its side) and a label recess 60 x 16 mm with a debossed "prog". The left wall has a 12.5 x 7 mm USB-C opening centred on J6 (enlarged vertically to 12 x 14 for position drift) and a 20 x 6 mm wire notch beside J7, with a rear-wall notch at the J2 corner for a ribbon that exits sideways. Corner radius R6.
- Tilt: separate 8 degree riser (wedge, 3 mm at the front to about 12.4 mm at the back), screwed under the tray from below with 2 M3 screws into the front bay. About 77 x 67 x 23 mm at the rear. Flat on the desk without the riser.
- Cable management: wire notch on the left wall, a 6 x 5 mm groove under the riser from the left to the back for the FTDI cable and USB-C lead, 3 mm slots in the rear wall for the ribbons.
- CMF: Abyss navy matte PETG tray and riser, coral for the pockets and the tag (print 2), TPU feet.
- Sealing: none, indoor tool.
- Build: tray floor down, no supports, 0.2 mm layers, about 5 h. Riser on its large flat face, the 8 degree top prints without supports, about 2 h. Unsupported: none except the USB-C notch (bridge 12.5 mm, fine in PETG, or a flat-top arch).
- Pros: fastest to model and print, nothing hides the legends, room for the shunt and plug, tilt improves reading.
- Cons: headers and buttons stay exposed (the tray protects edges only), footprint bigger than the board by 5 mm on each side plus the bay, plain look.
- Scores (out of 5): looks 3, fit with bench use 5, ease of printing 5, PCB change needed 5 (none).

## 5. Concept 2: CONSOLE (lid with windows)
Idea: a closed navy shell like a small instrument, with a lid that has a window cut around every connector and a button hole over each switch, legends embossed on the lid.
- Form: 77.4 x 53.4 x about 19.5 mm (plus 1.5 mm feet). Base is a tray as in concept 1 (no front bay) with walls 2.4 mm going up to the lid. The lid underside is 9.5 mm over the PCB, thickness 2.4 mm, front edge with a 45 degree chamfer. Windows 1.5 mm bigger than each part: J1 93 x 61 about 18.6 x 12.2 mm, JP1 4.6 x 8.4 mm, J2 11.6 x 18 mm, J3+J4 merged 16.8 x 18.2 mm, J5 10.4 x 5.2 mm, 10 mm holes over SW1 and SW2, a 3.2 mm hole for D1, a wire window at J7 6.8 x 10.4 mm. Left edge: USB-C opening 14 x 9 mm and wire notch.
- Interaction: lid screws (4 x M3) go through the lid, the PCB and into the base posts, so one fastener set closes it and clamps the board. Button caps are optional separate coral pieces (print 2). A shunt and TC2030 plug can be parked on a small coral bridge on the lid side, or the plug lives in a separate pouch (no storage spot in the first draft).
- Legends: lid text embossed 0.6 mm (section titles, JP1 on = BOOT, SW9 note) repeated from the PCB silk. Pin maps stay on the PCB, which is hidden, so the lid needs the pin maps for J1, J2, J3 (small 1.5 mm cap height text prints poorly at 0.4 mm nozzle; use at least 2.5 mm cap height or an engraved paper label recess instead).
- Tilt: none in the draft (flat). A wedge riser as in concept 1 can be added.
- Build: lid face down on the bed (text prints first layer, smooth), base floor down. No supports except the USB-C opening. About 4 h lid, 4 h base. Windows must be dimensionally tight (PETG shrink about 0.2 mm); print a window test.
- Pros: best protection for headers, tidy look, best family match (navy shell with coral details), one fastener set.
- Cons: the legends move to the lid and must be kept in sync with the PCB (and rev changes), board can't be seen, windows are tied to exact connector positions so a J6/J2 shift needs a lid change, JP1 shunt hard to pull in a 4.6 mm window (needs tweezers or a bigger 10 x 12 mm window).
- Scores: looks 4, fit with bench use 3, ease of printing 4, PCB change needed 4 (none required, but a J1/J2 move changes the lid).

## 6. Concept 3: QUADPOST (exposed frame)
Idea: a technical, exposed sandwich: a navy base plate, four corner posts, the board, and a top frame that grips the PCB edge on three sides. The board itself is the product, like a lab fixture.
- Form: plate 78 x 54 x 3 mm; posts 5 mm; top frame with 3 mm rails along the top, bottom and right edges (left open for USB-C, FTDI wires and the zip slots), and four towers 9 mm diameter, 10 mm above the PCB (taller than the headers). About 78 x 54 x 20 mm plus 1.5 mm feet. Towers have a coral ring (print 2) and carry the M3 screws from the top into inserts in the plate posts.
- Protection: the towers reach 10 mm above the PCB, so a drop lands on a tower and not on a header. Headers are open to ribbons from above and the sides; the open left edge takes the USB-C and the zip-tied FTDI cable.
- Cable management: the open left side with two 3 mm tie slots in the plate that line up with the PCB zip slots; ribbons exit over the rail (rail is 3 mm, no notch needed).
- Build: all parts print flat, no supports, 3 parts, about 3.5 h total. Fastest and lowest risk.
- Pros: quickest, nothing to line up with connectors, PCB labels and the LED stay visible, tolerant of a USB-C shift, least material.
- Cons: bare PCB is exposed from above (buttons and JP1 can be caught), rails have to sit on the board's silk border without touching parts (keep-out of 3 mm on three edges; J2 is 6.6 mm from the right edge, fine), looks less finished, no storage spot.
- Scores: looks 4 (for a lab-fixture taste), fit with bench use 3, ease of printing 5, PCB change needed 5 (none).

## 7. Comparison

| Concept | Idea | Looks | Fit | Print and seal | PCB change (5 = none) |
| --- | --- | --- | --- | --- | --- |
| 1 Bench Tray | open tray + tilt riser + storage bay | 3 | 5 | 5 | 5 |
| 2 Console | closed shell, window lid | 4 | 3 | 4 | 4 |
| 3 Quadpost | exposed plate/frame, corner towers | 4 | 3 | 5 | 5 |

## 8. Recommendation
Pick Bench Tray (concept 1). It matches how the tool is used (many ribbons from above, legends read from the desk, shunt and plug need a home) and it is the least sensitive to the USB-C shifting. Add the 8 degree riser only if the first flat print feels too low, since the riser is a separate part. If Brian wants a closed look later, the same base becomes Console's base (walls and posts are identical), so nothing is wasted. Quadpost is the fallback for a one-hour print.

## 9. Decisions for Brian
1. Concept 1, 2 or 3.
2. M3 hardware: draft with self-tapping M3 x 8 screws, or buy M3 heat-set inserts now (not on the hardware list)?
3. Tilt riser now or flat first?
4. Where does the 9160 DK sit (left or right of the adapter)? That decides which wall gets the ribbon notch.
5. TC2030 plug size (needed for the parking pocket): measure the actual plug.
6. Shunt storage: pocket in the bay (concept 1) or keep it fitted on one pin?

## 10. Unverified
- Connector heights (9 mm) assumed from the render; STEP not measured.
- Hole and component positions read from the render (+-0.3 mm); the USB-C may move.
- TC2030-IDC plug dimensions unknown; the pocket is a placeholder.

## 11. Optional board changes (none required)
- Move J6 USB-C so its centre is at least 10 mm from J5 and the left-edge zip slots, which gives a wider wall opening (nice to have).
- Add a silk "front" arrow or put the section titles on one side so a lid or the tray label can repeat them (concept 2).
- Move J2 about 3 mm further from the right edge, only if the Console lid window needs more wall at the corner (concept 2).
- A 1 mm rounded corner radius to 2.5 mm to match a tray pocket (tiny).
- If a bigger 12 mm gap between J1 and JP1 is wanted for finger access to the shunt, move JP1 right 2 mm. Not needed for the tray or quadpost.

## Decision (Brian 2026-11-07)
- **Concept:** 1 Bench Tray, printed flat (riser later if wanted).
- **Hardware:** M3 heat-set inserts, 4 mm long (a new buy).
- **Ribbon notch:** the 9160 DK sits to the right of the adapter, so the 10-pin ribbon notch goes in the right wall near J3.
- **Still open:**
  - the TC2030-IDC plug size for its pocket (measure the real cable)
  - whether the shunt parks in the bay
- **Modelling:** fusion-enclosure models it after the prog_adapter design review and any fixes, using the final STEP.
