# Pouch gateway enclosure concepts (2026-10-24)

Project: pouch_gateway Rev A (PCB fixed and on order, so no PCB changes this revision).
Sketches in this folder:

| File | Content |
| --- | --- |
| 00-pcb-reference.svg | Real footprint positions from pouch_gateway.kicad_pcb (component side), the reference for every concept |
| 01-ledger.svg | Concept 1, front / side / section |
| 02-prism.svg | Concept 2, front / end section |
| 03-tide-pebble.svg | Concept 3, front / side section |
| 04-reef-fin.svg | Concept 4, front / side with cleat |
| 05-field-unit.svg | Concept 5, front / side |
| 06-family.svg | Family direction across gateway, ReefWatch node, Feather + pH, soil node |

---

## 1. Brief

**What it is.** A Golioth Pouch BLE-to-Wi-Fi gateway (Murata Type 2FR / NXP RW612). It listens to the family's BLE nodes (ReefWatch reef nodes, the pH board, soil moisture) and sends their data over Wi-Fi. A 2.0 in 240 x 320 IPS screen shows status and readings.

**Where it lives (assumed, to confirm).** Indoors near the reef tank: on a shelf or desk next to it, on the side of the aquarium cabinet, or on a wall. It may see humid air and the odd salt splash near the tank. It is not outdoors. Concepts cover desk/shelf and wall/cabinet.

**Who handles it, how often.** Brian and family glance at it every day and press USER to page the screen. The charge port is used now and then (or the device stays plugged in, with the battery as backup). SWD, Tag-Connect, UART, RESET and ISP are developer-only and used rarely; opening the case for those is acceptable.

**Environment.** Indoor, 18-30 C, high humidity near the tank, salt creep possible, no UV. PLA is acceptable for a dry desk. PETG is the default because it handles humidity and softens later than PLA (relevant near a lit hood or a warm cabinet).

**Hard constraints (verified in the board file and the docs):**

| Item | Fact | Source |
| --- | --- | --- |
| PCB | 58.0 x 35.0 x 1.6 mm, 4 layers. M2 holes on 53.0 x 30.0 (2.5 mm in from each edge), the same pattern as the LCD module | STATUS.md, DESIGN_NOTES.md, .kicad_pcb |
| USB-C J1 | Left edge, centre 23.4 mm down from the top edge, receptacle facing left | .kicad_pcb |
| Buttons | RESET x 18.6, **USER x 29.7 (centred)**, ISP x 41.7 mm, all 3.3 mm in from the **top** edge. CK KMR2, top-actuated, 1.9 mm tall | .kicad_pcb |
| LEDs | D3 / D5 / D4 at x 33.6 / 35.6 / 37.8 mm, 5 mm in from the **bottom** edge. 2 mm pitch, so one combined diffuser, not three separate pipes | .kicad_pcb |
| J5 display | JST PH 8-pin side entry on the right edge, pins from y 8.5 to 22.5 mm. The cable leaves past the right edge, so allow about 9 mm clearance. Opening direction still to be confirmed (DESIGN_NOTES item 6) | .kicad_pcb, DESIGN_NOTES |
| J3 / J7 | U.FL main antenna at x 41.0, y 22.3. J7 (second BLE antenna) at x 27.4, y 30.9, not fitted | .kicad_pcb |
| Debug | J2 SWD 2x5 1.27 mm SMD (top-left), J6 Tag-Connect TC2030 (left, pads on the component side, legs latch on the back), J4 UART 1x3 2.54 mm through-hole (centre-left) | .kicad_pcb |
| Power | USB-C 5 V only, into a TLV62569 buck. **No battery input or charger on the board.** USB_VBUS sense pin has an abs max of 5.25 V | DESIGN_NOTES |
| Display | Waveshare 2inch LCD Module (SKU 17344): 58 x 35 mm, active area 30.60 x 40.80 mm (portrait), 0.1275 mm pixel, PH2.0 8-pin, M2 x 6 standoffs, max draw 46 mA at 3.3 V | Waveshare wiki and product page |
| Antenna | Must be a type and gain filed under FCC ID HSW2FR. The filed list (below) contains only internal U.FL dipoles and a PCB trace, **no external whip or RP-SMA** | Murata radio-law app note, Table 14 |
| RF exposure | The module is approved as "mobile equipment": antenna 20 cm or more from people in normal use. A battery must not turn it into a hand-held (portable) device without new SAR testing | Murata app note 2.1.6.6 / 2.1.6.8 |
| Build | Home FDM, walls 2 mm or more, 0.5 mm clearance, M2 heat-set inserts or standoffs. Modelled later in Fusion by fusion-enclosure | Task |

**Differences between the brief and the board file (please note):**
- The buck (U2, L1) is **bottom-left**, not top-right.
- **USER is top-centre**, next to RESET and ISP. Only the LEDs are on the bottom edge.
- These change where keys and light pipes go, so every concept below uses the board-file positions.

**Constraints still missing (asked in section 9):** placement, what the battery is for and how long it must last, the measured LCD module thickness, panel offset and connector position, whether J2/J4 are fitted, printer capability (multi-material?), and colour preferences.

---

## 2. Shared engineering (applies to every concept)

### 2.1 Power and battery architecture

The board has no battery path, so every concept carries the same external power chain:

```
[USB-C charge port on enclosure] -> [charger + 5 V boost module, load sharing] -> [5 V pigtail with USB-C plug] -> J1
                                              |
                                        [1S LiPo, JST PH 2-pin]
```

- **Reference module: Adafruit PowerBoost 1000C** (verified: load sharing, so the output stays up while charging, which makes it a UPS; 5.2 V out, 1 A+; EN pin to GND switches the output off; low-battery LED below 3.2 V; 23 x 45 mm board; charger input is **micro-USB**; it must always have a battery attached). It is the reference because its load-sharing behaviour is documented. Cheaper USB-C "charge + boost" clone boards exist, but their pass-through and low-load auto-off behaviour varies, so I don't recommend them without a bench test.
- **Charge port:** a panel-mount USB-C receptacle (with 5.1 kOhm CC pull-downs so C-to-C chargers supply 5 V) wired to the PowerBoost's micro-USB input through a short adapter lead or soldered to its input. Charge-only, no data.
- **Power switch:** a small slide switch on the PowerBoost EN line, recessed so it isn't knocked. Charging still works with the output off.
- **Internal jumper to J1:** PowerBoost 5 V / GND soldered to a short right-angle or straight **USB-C plug pigtail** (power only). The plug and its overmould need about 11 mm beyond the PCB's left edge, so every concept keeps an 11 mm zone left of the gateway. The board's 5.1 kOhm CC resistors don't matter here because the boost output is always on.
- **USB data:** while the pigtail is in J1 there is no USB console. For development, open the case, unplug the pigtail and connect a laptop to J1 (Concept 5 makes this a feature).
- **VBUS margin (flag, no PCB change):** the PowerBoost puts out 5.2 V nominal. The RW612 USB_VBUS sense pin is rated 5.25 V abs max, and DESIGN_NOTES already describes depopulating the 0 Ohm on that line with a register override. Recommend confirming with kicad-designer / firmware whether to leave the 0 Ohm off for battery builds. This is an assembly (BOM) choice, not a PCB change.

**Battery proposal (for Brian to confirm):**

| Option | Size (mm) | Energy | Est. run time on battery* | Fits |
| --- | --- | --- | --- | --- |
| 603450 LiPo, 1000 mAh | 50 x 34 x 6 | 3.7 Wh | about 5-11 h | all concepts, thinnest |
| **103450 LiPo, 2000 mAh (default)** | 50 x 34 x 10 | 7.4 Wh | **about 10-22 h** | all concepts; matches the 58 x 35 board footprint |
| 18650 protected cell, 3000-3500 mAh | 19 dia x 69 | 11-13 Wh | about 15-36 h | Prism (if lengthened to ~110 mm), Field Unit pack |

*Estimate, not measured.* Basis: Wi-Fi RX on the RW612 is about 63-74 mA and 2.4 GHz TX peaks at 261 mA (DESIGN_NOTES, from the NXP datasheet). A gateway that keeps Wi-Fi associated and scans BLE is mostly receiving, so I assumed 60-100 mA for the module and 10-46 mA for the LCD (46 mA is Waveshare's maximum, backlight full). That gives 0.23-0.48 W on 3.3 V, then about 90 % buck and 88 % boost efficiency, so 0.29-0.61 W from the cell, with about 85 % of the rated capacity usable. I couldn't find a published RW612 "Wi-Fi connected, idle" current, so measure it on the real board. Dimming the backlight and using Wi-Fi power save should stretch these numbers, but by an unknown amount.

**What this means for the product:** a battery buys hours to a day, not weeks. It works best as **outage ride-through** (it keeps reporting "power lost at the tank" while the router is on a UPS) or for freedom to place the gateway away from a socket for a while. That is the main question for Brian (section 9).

### 2.2 Antenna (FCC ID HSW2FR filed list)

From Murata's Type 2FR radio-law application note, Table 14 (FCC):

| # | Part | Vendor | Peak gain 2.4 / 5 GHz | Type | Size (looked up) |
| --- | --- | --- | --- | --- | --- |
| 1 | 146153 (50 mm cable) | Molex | 3.2 / 4.25 dBi | dipole, flexible (FPC), adhesive | 34.9 x 9.0 x 0.1 mm (Molex page for the 100 mm-cable version) |
| 2 | 219611 (50 mm cable) | Molex | 2.67 / 3.67 dBi | dipole, flexible, adhesive | 35.4 x 15.4 mm |
| 3 | WT32D1-KX | Unictron | 3.0 / 4.0 dBi | dipole, U.FL | datasheet not found |
| 4 | W24P-U | Inventek | 3.2 dBi, 2.4 GHz only | PCB dipole, U.FL | 30 x 5 mm, 90 mm cable |
| 5 | Type 2FR trace | Murata | 2.6 / 3.6 dBi | PCB trace | not usable (this board uses U.FL) |

- Every concept uses an **internal FPC antenna (146153 by default, 219611 where a wider fin suits)** stuck to a plastic wall. An external whip or RP-SMA bulkhead is not on the filing, so none of the concepts use one.
- Where a concept needs a longer lead than 50 mm, use the same part with a longer cable (e.g. 146153-0100, listed by Molex at 3.0 dBi at 2.4 GHz). That is the same type with lower gain. Murata's app note (2.1.6.12) describes this as a Class I-type change backed by documentation. Keep the datasheet with the project.
- Placement rules used in every concept: 12-15 mm or more from the LCD metal frame and the gateway ground edge, 30 mm or more from the battery and the PowerBoost inductor, no metal or carbon-filled filament near it, coax kept away from the buck (bottom-left of the gateway).
- Regulatory label: "Contains FCC ID: HSW2FR" debossed on the underside or rear of every concept.

### 2.3 Screen window (shared detail)

- Active area 40.8 x 30.6 mm (landscape) or 30.6 x 40.8 mm (portrait). Window opening = active area + 0.6 mm each side, so **42.0 x 31.8 mm**, with a 45 degree outward chamfer so the edge pixels aren't shadowed at an angle.
- Where the active area sits on the 58 x 35 module, the module's thickness and where its PH connector is **are not published in text** (the Waveshare 2D drawing PDF wouldn't parse). **Measure them before CAD.** Until then, every concept puts the window in a **separate bezel insert** (a 1.2 mm thin-lip ring, printed in black), so a wrong offset costs a 20-minute reprint, not a new shell.
- Glass sits on a 0.5 mm foam or printed TPU gasket, never clamped hard.
- Optional cover lens: 1.5 mm laser-cut clear acrylic (printed "clear" PETG is not optically clear enough to read a screen through). Required only for Concept 3.

### 2.4 Stacked vs side-by-side

The LCD and gateway share the 53 x 30 M2 pattern, so they can stack on standoffs. Two consequences that shape the concepts:
- **Stacked (Concepts 2, 3, 5):** the gateway's parts must face **away** from the LCD (rear), because J5, J2 and J4 are too tall for the gap and the LCD would hide the switches anyway. So USER, RESET, ISP and the LEDs all face backwards. RESET / ISP / SWD / Tag-Connect are then easy to reach from the back, but USER needs a rear key, a lever or a "the screen is the button" mechanism. Budget **8 mm standoffs** (not Waveshare's 6 mm) until the LCD's rear connector height is measured. Stack depth is about 22 mm with J4 not fitted.
- **Side by side (Concepts 1, 4):** both boards face forward. USER, the pinholes and the LED pipe go straight through the front wall. This gives the best everyday interaction and needs no mechanism, but the device is larger in one direction. SWD / Tag-Connect need the gateway lifted out (4 screws), because those parts face the front shell.

---

## 3. References (each looked up; what it teaches)

| Reference | Link | Lesson used |
| --- | --- | --- |
| Ovyl (integrated studio) | https://ovyl.io | Electronics, enclosure, install and production designed together ("half a product isn't a product"): here that means designing the power path, antenna and service access, not only a shell |
| Ovyl / CEM Smart Roof | https://ovyl.io/work/cem-products-smart-roof | A system of sensor + controller + **gateway** with one look; installer feedback changed enclosure size for easier wiring. This drives the family direction and the cable / cleat details |
| Braun ET66 (Rams / Lubs), V&A | https://collections.vam.ac.uk/item/O1360553 | Display on top and keys below, **one coloured key** among neutrals, convex buttons. Basis of Concept 1 (USER as the single accent key) |
| Teenage Engineering computer-1 | https://www.core77.com/posts/111404/Teenage-Engineerings-Flatpack-DIY-Portable-Computer-Housing | Construction as the aesthetic: flat parts, visible assembly, a strong colour. Basis of Concept 5 |
| Nothing Phone (1), Dezeen | https://www.dezeen.com/2022/08/19/nothing-phone-1-design/ | A transparent back plus light as information. Concept 5's clear back and Concept 4's glowing crest |
| Google Nest Hub design notes | https://blog.google/products/google-nest/a-closer-look-at-the-new-nest-hubs-design-details/ | A screen that "floats" on a soft base that hides the bulky parts. Concept 3 (battery in the base, screen floating on top) |
| Tidbyt Gen 2 | https://www.tidbyt.com/products/tidbyt-gen-2 | One small display product with a kickstand **and** a built-in wall mount: two placements from one body. Concept 1 wedge plus keyholes, Concept 5 bail |
| Aranet4 HOME mounting | https://help.aranet.com/aranet4/aranet4-home/maintenance-and-safety/mounting-on-a-surface-or-wall | Desk or wall with vents on the side walls so mounting doesn't block them; a simple dedicated bracket. Used for vent placement and the cleat |
| Neptune Apex Display Module | https://www.bulkreefsupply.com/apex-display-module-neptune-systems.html | The reef-world equivalent: mechanical (not membrane) buttons chosen for saltwater rooms, status and alarms at the tank, about 86 x 103 x 17 mm. A gateway screen at the tank is a known, valued pattern |
| Red Sea ReefDose launch (Coral Magazine) | https://www.coralmagazine.com/?p=3061161 | Designed to sit on any surface in any orientation, and to reschedule after power outages. Supports "battery = outage resilience" |
| Kessil A360X review (Reef Builders) | https://reefbuilders.com/2018/11/13/kessil-a360x-review | Premium reef gear: a low-profile puck, one strong sculpted signature (the "sunflower" heatsink), and many mounting accessories (gooseneck, arm, hanging) |
| Home Assistant Voice Preview Edition | https://www.home-assistant.io/voice-pe/ | A maker-friendly product with a white or **semi-transparent** enclosure, an LED ring for status, a tactile control, and a case that opens with ordinary screws |
| IKEA DIRIGERA hub | https://www.ikea.com/au/en/p/dirigera-hub-for-smart-products-white-smart-90503407/ | A hub should be a quiet object: slim, round, one colour. A counterpoint so the gateway doesn't shout |
| Prusa fuzzy skin | https://help.prusa3d.com/en/article/fuzzy-skin_246186/ | Outside-walls-only texture hides layer lines on side walls. OrcaSlicer can paint it on, so mating faces stay smooth |
| Murata 2FR radio-law app note | https://www.murata.com/-/media/webrenewal/products/connectivitymodule/asset/pub/rfm/data/type2fr/type2fr-radio-law-approval-app-note.ashx | The filed antenna list and the mobile-equipment (20 cm) condition |
| Molex 146153 / 219611 | https://www.molex.com/ja-jp/products/part-detail/1461530100 , https://www.molex.com/en-us/products/part-detail/2196110050 | FPC sizes that set the antenna zones |
| Inventek W24P-U | https://inventeksys.com/2-4ghz-pcb | 30 x 5 mm 2.4 GHz-only alternative for tight zones |
| Waveshare 2inch LCD Module | https://www.waveshare.com/wiki/2inch_LCD_Module | Active area, pixel pitch, standoffs, current |
| Adafruit PowerBoost 1000C | https://www.adafruit.com/product/2465 | Reference charger / boost with load sharing |

---

## 4. Five concepts at a glance

| # | Name | One-line idea | Shape language | Orientation / mount |
| --- | --- | --- | --- | --- |
| 1 | **Ledger** | A small Braun-style instrument: screen above, a calm control panel with one coral key below | Architectural, Rams | Portrait; desk wedge or wall keyholes |
| 2 | **Prism** | A faceted tent with the screen on the leaning face and glowing crystal end caps | Faceted / crystalline | Landscape; desk |
| 3 | **Tide Pebble** | A soft stone you look down into; the whole screen is the button and the base glows at the waterline | Soft pebble / organic | Landscape, 35 deg lectern; desk or shelf |
| 4 | **Reef Fin** | A wave-topped plaque for the cabinet side whose translucent crest is both antenna and status light | Biomorphic (reef, fin) | Landscape; cabinet side or wall on a cleat |
| 5 | **Field Unit** | An honest instrument: orange frame, exposed screws, clear back, antenna flag, clip-on power pack | Technical / exposed | Landscape; bail as kickstand, hook or wall |

---

## 5. Concepts

### Concept 1: LEDGER (sketch 01-ledger.svg)

**Idea.** The gateway as a small, quiet instrument in the Braun ET66 tradition: the screen at the top, a neutral panel below with one coral key (USER) and a tiny status pill. The body ratio (82 x 100) echoes the screen. Why it suits: the screen is the hero, the single key matches how the device is used (page, page, page), and it reads as a well-made object on a reef-room shelf rather than a gadget.

**Form.**
- 82 W x 100 H x 24 D mm. Vertical edges R6, front edge R2.
- **Brow:** the top 14 mm of the face leans back 20 degrees and hides the FPC antenna. It is the signature detail and the family's "brow" (section 7).
- Inside, the LCD module (top) and the gateway (below) sit side by side vertically, both facing forward, 4 mm apart. 13 mm on the left (pigtail into J1), 11 mm on the right (J5 cable loop).
- Parting line: one front shell (face plus all four side walls) and a flat rear cover, set in 1 mm with a 0.5 mm shadow gap so the seam is invisible from the front.
- Dot grille (1.5 mm holes, 3 mm pitch) over the RW612 module and buck: these are the vents, styled as a speaker grille. A hidden vent slot runs under the brow lip for warm air to leave at the top.

**CMF.**
- Shell: matte PETG or matte PLA in **Sand** (warm off-white), face printed on textured PEI.
- USER key: **Coral** PETG (opaque) with a convex 10 mm dome.
- Bezel insert: matte black.
- Status pill: translucent white or coral PETG, or a piece of 3 mm acrylic, inside a black light shroud.
- Rear cover: same Sand.
- Stand: Sand with TPU foot strips.
- Alternative colourway "Abyss" (navy body, coral key) for a darker reef room.

**Interaction.**
- **USER:** a captured key cap (flange behind the wall, 3 mm stem onto the KMR2), 0.2-0.3 mm travel, a crisp click under the screen.
- **RESET / ISP:** two 1.5 mm pinholes flanking the key with printed guide tubes. They are symmetric (offsets -11.1 / +12.0 mm), so they read as part of the graphic.
- **Status:** one pill over D3-D5, about 7 mm light path from the LEDs.
- **Charge USB-C and power switch:** on the underside, with a cable channel running to the back. The wedge stand has a slot for the cable.
- **Mounting:** desk = slide onto a 15 degree wedge stand. Wall or cabinet = two keyholes plus a rear cable channel.
- **Service:** remove the rear cover (4 x M2) to reach the battery and PowerBoost. SWD / Tag-Connect / UART face the front, so lift the gateway out (4 more screws) on its leads.

**Battery / power / antenna placement.**
- 103450 LiPo on a cradle on the rear cover, behind the gateway, so it comes away with the cover.
- PowerBoost behind the LCD.
- Pigtail down the left side into J1.
- 146153 FPC (100 mm lead version) inside the brow, 12 mm or more above the LCD, about 60 mm from the battery. The coax runs up the right side, away from the pigtail and the buck.

**Sealing / environment.** Indoor. PETG recommended near the tank. No horizontal ledges at the openings, and the vents face down and under the brow, so splashes don't enter. No gasket needed.

**Build.**
- Front shell printed face-down on textured PEI: no supports. The window chamfer and grille holes print cleanly face-down.
- Bosses for the LCD and gateway with M2 heat-set inserts. Rear cover printed flat. Key, pill and guide tubes are small separate prints.
- About 5 h shell + 2 h cover + 1.5 h stand + 0.5 h small parts, so **about 9 h total. Difficulty: easy.**

**PCB fit (Rev A).** Works as is: every user-facing part already faces forward. Next-revision wishes: LED pitch of 4 mm or more (or one RGB) under a single pill position, and Tag-Connect reachable from the back.

**Scores:** Looks 4 | Fit with setting 4 | Ease of printing/sealing 5 | Works with fixed PCB 5 | **Total 18/20**

---

### Concept 2: PRISM (sketch 02-prism.svg)

**Idea.** A faceted tent, like a small crystal or a shard of coral rock, lying on the desk. The screen is set into the 62 degree front face. The two triangular end caps are translucent, faceted "crystal": one holds the antenna, and a thin light sill under the screen shows status. Why it suits: very stable, reads at a glance from across the room, and the extruded profile is about the most FDM-friendly shape there is.

**Form.**
- 104 L x 80 D x 62 H mm.
- Profile: front face 62 degrees, rear face about 53 degrees, a crisp 1 mm land at the apex.
- The LCD is stacked on the gateway with 8 mm M2 standoffs, gateway parts facing rear, mounted parallel to the front face, about 20 mm up the face (so the stack clears the floor).
- End caps 10 mm thick with three facets each.
- Parting lines: the body is one extrusion; the end caps are the parting lines, which hides the seams in the design.

**CMF.**
- Body: matte PETG in Abyss (deep navy) or Ink, fuzzy skin on the outside walls only (rock-like matte).
- End caps: translucent PETG ("glacier" clear-blue or coral translucent).
- Light sill: clear PETG.
- Feet: two TPU strips.

**Interaction.**
- **USER:** a "key facet", a small flat cut into the back face parallel to the screen, about 40 mm behind the face. A 24 mm guided plunger goes to the rear-facing switch. You reach over the apex and press. It is honest but less immediate than Ledger.
- **RESET / ISP:** pinholes in the same facet, straight onto the switches.
- **Status:** an L-shaped light pipe takes D3-D5 light from behind the stack, under it, to a slit at the foot of the face. Brightness must be tested (two bends in printed PETG lose light); a 3 mm acrylic rod is the fallback.
- **Charge USB-C and power switch:** in the left end cap.
- **Service:** the back face is a screwed cover, so removing it exposes the gateway's rear: SWD, Tag-Connect and UART are directly reachable.

**Battery / power / antenna placement.**
- 103450 on the rear floor, left half (ballast behind the leaning face), with the PowerBoost on top of it. Pigtail to J1 on the left.
- 146153 FPC flat on the inside of the **right** end cap, 30 mm or more from the battery and PowerBoost, about 15 mm from the PCB edge, 50-100 mm lead from J3.

**Sealing / environment.** Indoor; the slopes shed splashes. End caps clip in with a 0.3 mm interference rib. No gasket.

**Build.**
- Body prints **standing on one end** (profile flat on the bed): no supports anywhere. The window's top edge gets a 45 degree "roof" inside.
- Back face cover prints flat. End caps print flat on their outer facet.
- About 7 h body + 2 x 1.5 h caps + 1 h cover, so **about 11 h. Difficulty: easy to moderate.** The light pipe is the only fiddly part.

**PCB fit.** Works as is, but status and USER are indirect because the parts face rear. Next revision: LEDs and a switch on the rear-facing side positioned for a short straight pipe, or a right-angle (side-actuated) USER switch at the board edge.

**Scores:** Looks 4 | Fit with setting 3 (a desk object only; crystalline rather than reef-like) | Ease of printing/sealing 5 | Works with fixed PCB 3 | **Total 15/20**

---

### Concept 3: TIDE PEBBLE (sketch 03-tide-pebble.svg)

**Idea.** A smooth stone at the edge of the tide: you look down into its face as if into a rock pool. The whole screen is the button: press the lens and the screen module tips and clicks. A thin translucent ring at the base (the waterline) glows with status, as if the stone sits in shallow lit water. Why it suits: the most emotional, home-object form; no visible buttons at all; the battery in the base gives it weight and makes it hard to knock over.

**Form.**
- About 120 W x 92 D x 60 H mm, a superellipse plan with a soft crown.
- Screen face tilted 35 degrees up (a lectern), so it reads from above on a low shelf or desk.
- Stacked LCD + gateway (parts facing down/rear) on a **front hinge** (1.75 mm filament pin through two printed lugs). A fixed post under USER at the top edge of the stack: press anywhere on the lens, the stack tips about 0.4 mm and USER clicks. Travel is limited by the switch; a light TPU pad returns it.
- Parting line at the waterline (the widest point), so both halves print with overhangs under 45 degrees.

**CMF.**
- Upper shell: matte PLA or PETG in Sand, or a speckled "stone" filament, fuzzy skin fine setting.
- Lens: 1.5 mm clear acrylic (laser cut).
- Waterline ring: translucent coral or aqua PETG.
- Inner liner: white PLA, so the base cavity works as a light box.
- Base: Ink PETG with a TPU foot ring.

**Interaction.**
- **USER = press the screen** (2-4 N, which is the KMR2's force range).
- **Status = the glowing waterline:** the LEDs face down into a white-lined cavity, and the light leaks out through the ring. Soft and ambient, not precise.
- **RESET / ISP:** the battery blocks a straight pinhole path, so lift off the base tray (3 x M2) to reach them.
- **Charge USB-C:** rear, low. **Power switch:** underneath.
- **Service:** base off gives the battery and PowerBoost. Upper shell off (hinge pin out) gives the gateway's rear: SWD and Tag-Connect.

**Battery / power / antenna placement.**
- 103450 flat in the belly under the high (rear) end of the stack, PowerBoost in front of it.
- 146153 FPC curved gently along the inside of the rear crown: 15 mm or more from the LCD, 35 mm or more above the battery. A 1-2 mm bend radius is not allowed, so keep the curve gentle or use the flat crown area.

**Sealing / environment.** Indoor. The lens edge should get a thin TPU or foam seal so water and dust don't creep under it; it also damps the click.

**Build.**
- Upper shell dome-up about 8-9 h, base 3 h, ring 1 h, lens bought or cut, hinge lugs and liner 1 h, so **about 14 h. Difficulty: moderate to hard.**
- The hinge, post and lens stack-up needs one or two test prints to get a clean click without rattle.
- The curved shell is the hardest of the five to model in Fusion.

**PCB fit.** Works as is, but relies on a mechanism, and status is soft. Next revision: a side-firing LED or a ring of LEDs on the rear side would make the waterline even.

**Scores:** Looks 5 | Fit with setting 4 | Ease of printing/sealing 2 | Works with fixed PCB 3 | **Total 14/20**

---

### Concept 4: REEF FIN (sketch 04-reef-fin.svg)

**Idea.** A long, low plaque that hangs on the side of the aquarium cabinet (or a wall). Its top edge rises into a translucent coral crest like a fin or a wave. The crest is honest technology: it is the antenna window (the FPC is visible inside like a fin ray) and the status light. Why it suits: it lives where reef keepers already look (the stand) and keeps the gateway off the crowded hood and shelf. The shape comes straight from the tank's world.

**Form.**
- 150 W x 52 H (72 at the crest) x 26 deep at the bottom, 18 at the top: a wedge, so the face tilts up about 12 degrees for viewing from above at cabinet height. Flip the cleat and it faces level for an eye-height wall.
- Inside, side by side: LCD on the left, gateway on the right **rotated 180 degrees**, both facing forward. After the turn:
  - D3-D5 sit near the top edge, right under the crest, so one short straight pipe lights the crest.
  - USER, RESET and ISP sit along the lower edge of the gateway half.
  - J5 faces the LCD, so the display cable is short.
  - J1 is at the right end, beside the PowerBoost.
- Parting line: front body / flat back plate. The crest is a separate translucent part clipped and glued into a slot.

**CMF.**
- Body: matte PETG in Abyss (navy).
- Face: printed on textured PEI for a fine sand texture.
- Crest: translucent coral PETG.
- USER key: Coral.
- Back: shallow "growth-line" ribs (coral texture) that also stiffen the plate.
- Cleat: PETG.

**Interaction.**
- **USER:** a front key at the lower edge, under your thumb when you reach up to the plaque.
- **RESET / ISP:** pinholes either side of it.
- **Status:** the whole crest glows (soft colour, readable across the room).
- **Charge USB-C:** right end, pointing down. The cable drops straight to the outlet strip inside or beside the cabinet.
- **Power switch:** underside.
- **Mounting:** a printed 45 degree French cleat rail, fixed with 2 screws or VHB tape (no drilling into a nice cabinet). The plaque lifts off for charging or service. Installer experience: stick the rail on, level it, hang it.

**Battery / power / antenna placement.**
- 103450 behind the LCD half. PowerBoost behind the lower part of the gateway half, beside J1.
- 146153 (or the wider 219611, which suits the crest) inside the crest: 14 mm or more above the gateway top edge, about 40 mm or more from the PowerBoost, about 80 mm from the battery.

**Sealing / environment.**
- Cabinet sides near a sump see splashes and salt creep. Use PETG. The charge port points down, so drips don't sit in it.
- A drip lip runs along the top of the face below the crest.
- No gasket, but the crest slot is glued closed.
- Don't mount it over the sump opening.

**Build.**
- Body printed face-down on textured PEI: the wave top and the wedge become vertical walls, so no supports. Back plate flat, crest flat, cleat flat.
- About 7 h body + 2 h back + 1 h crest + 0.5 h cleat, so **about 10.5 h. Difficulty: moderate** (long part, warping risk on a 150 mm PETG print; use a brim).
- Two-material option: print the crest in the same job if the printer has multi-material.

**PCB fit.** Works as is; everything faces forward. Next revision: J3 near the top edge, closer to the crest.

**Scores:** Looks 4 | Fit with setting 5 | Ease of printing/sealing 4 | Works with fixed PCB 5 | **Total 18/20**

---

### Concept 5: FIELD UNIT (sketch 05-field-unit.svg)

**Idea.** A Teenage Engineering-style instrument that shows how it's made:
- an orange printed frame with exposed M2 screws;
- a black bezel plate;
- a clear rear plate showing the gateway;
- a small translucent antenna "flag" on top;
- a bail that is a kickstand, a hanging loop or flat for a wall screw;
- a **clip-on power pack** joined to J1 by a visible USB-C umbilical.

Why it suits: it fits a maker household and a developer board (debug ports on show), and the modular pack answers the "battery or not" question by making the battery optional.

**Form.**
- Core 82 W x 50 H x 26 D. With the pack 82 x 74. The flag adds 22 mm.
- Layers front to back: bezel plate 3 mm, frame 20 mm, clear back 3 mm.
- Stacked LCD + gateway, parts facing rear, behind the clear back.
- Parting lines are the layers themselves (sandwich construction), with screws through all layers into heat-set inserts in the frame.

**CMF.**
- Frame: PETG in signal orange.
- Bezel: matte black PETG.
- Back: clear PETG printed thin (frosted look) or laser-cut acrylic.
- Flag: translucent PETG.
- USER lever: yellow.
- Bail: TPU 95A (flexible, grippy) or PETG.
- Pack: grey PETG.
- Screws: black button-head M2 (the screws are metal but far from the flag).

**Interaction.**
- **USER:** a yellow lever on top on a 1.75 mm filament pin, a small bell crank that presses the rear-facing switch from behind. A visible, mechanical, satisfying action.
- **RESET / ISP:** holes in the clear back, straight onto the switches.
- **Status:** the rear-facing LEDs wash the wall or desk behind, and the frosted edge of the back plate glows at the top.
- **Pack:** LiPo + PowerBoost, own charge USB-C, power switch on its side, attached with 2 thumb screws. The umbilical (a short right-angle USB-C cable) goes into J1 on the side of the core. Unplug it and the core runs from any USB-C supply, **with USB data**, which makes development easy.
- **Service:** the back plate off gives SWD, Tag-Connect and UART directly.

**Battery / power / antenna placement.**
- Battery and PowerBoost live in the pack, below the core: about 60 mm or more from the flag.
- 219611 FPC inside the flag, 15 mm or more above the LCD frame.

**Sealing / environment.** Indoor desk or developer bench. The open umbilical and exposed holes make it the least splash-tolerant concept, so keep it away from the tank edge.

**Build.**
- All flat plates: fast, no supports, very forgiving. Frame about 3 h, plates 1 h each, pack 2.5 h, flag, lever and bail 1 h, so **about 9 h of printing.**
- The most assembly: about 16 screws, a lever with a pin, the umbilical. **Difficulty: moderate** (mechanism plus part count).

**PCB fit.** Works as is. The bell crank is the compromise for USER facing rear. Next revision: a side-actuated USER switch on the top edge would remove the crank.

**Scores:** Looks 4 | Fit with setting 3 | Ease of printing/sealing 3 | Works with fixed PCB 4 | **Total 14/20**

---

## 6. Ranking and recommendation

| Rank | Concept | Looks | Setting | Print / seal | Fixed PCB | Total | Size (mm) | Print time |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Ledger | 4 | 4 | 5 | 5 | **18** | 82 x 100 x 24 | ~9 h |
| 2 | Reef Fin | 4 | 5 | 4 | 5 | **18** | 150 x 72 x 26 | ~10.5 h |
| 3 | Prism | 4 | 3 | 5 | 3 | 15 | 104 x 80 x 62 | ~11 h |
| 4 | Tide Pebble | 5 | 4 | 2 | 3 | 14 | 120 x 92 x 60 | ~14 h |
| 5 | Field Unit | 4 | 3 | 3 | 4 | 14 | 82 x 74 (+22) x 26 | ~9 h |

"Fixed PCB" = how well the concept works with Rev A unchanged (5 = no compromise).

**Recommendation.**
1. **Ledger** as the main design, if the gateway lives on a shelf or desk (or a plain wall). It has the clearest everyday interaction (a real key under the screen, a direct status pill), needs no mechanism, prints without supports, and suits a family of devices. Ledger and Reef Fin both use the "both boards face forward" layout, so the key, pinhole and light-pipe details carry over between them.
2. **Reef Fin** if the gateway should live on the aquarium cabinet. It fits the setting best and turns the antenna placement into the signature.
3. If Brian wants the most sculptural object and accepts a harder build and a press-the-screen mechanism, **Tide Pebble** is the looker. Prototype the hinge-and-click first.

**Decisions Brian needs to make:**
1. Placement (shelf/desk, cabinet side, wall, or more than one): this chooses between Ledger and Reef Fin.
2. What the battery is for (outage ride-through or moving it around) and the target run time: this sets 1000, 2000 or 3000+ mAh.
3. Colourway: Sand body with a coral key (light rooms), or Abyss navy (dark reef rooms).
4. Open window or cover lens over the LCD.
5. Accept the external PowerBoost + pigtail for Rev A (charge-only port, no USB data on battery builds).

---

## 7. Family direction: "Brow and Tide line" (sketch 06-family.svg)

One language for the gateway, the ReefWatch nodes, the Feather + pH board and the soil node:

1. **Brow.** Every device has a sloped or rounded top band (the brow) and the antenna always sits under it. Placing the antenna becomes a recognisable feature, and it keeps antennas away from batteries (always low) by rule.
2. **Tide line.** Status light always appears as one coral pill or line near the bottom of the face. Same colour, same proportion (about 3:1), at the same relative height on every device.
3. **Geometry.** Soft rectangles, 6 mm vertical corner radius on large devices and 4 mm on small ones, flat faces, a 2 mm front-edge round, one 20 degree brow facet. No other chamfers.
4. **Palette.**
   - Sand (indoor, dry) and Abyss navy (wet zones, outdoor) for bodies.
   - Coral translucent for every light-carrying part and the one primary key.
   - Ink black for screen bezels.
   - Outdoor parts in ASA with the same colours.
5. **Mounting.** One printed 45 degree French cleat profile across the family (gateway, wall nodes, pH box), plus the same keyhole spacing, so one rail system fits the whole reef stand.
6. **Details.** Debossed lowercase labels 0.4 mm deep, M2 button heads on the back only, regulatory text on the underside, fuzzy skin on side walls only.

Applied to the siblings:
- **ReefWatch node** (about 44 x 34 mm board): about 56 x 48 x 20, Abyss PETG, PV cell set into the face, chip antenna under the brow.
- **Feather + pH board** (66 x 25.4 mm boards): about 80 x 38 x 30, PETG, an o-ring lid and a probe gland at the bottom because it sits near the sump.
- **Soil node:** ASA with a gasketed lid and a stake.

If Brian picks Reef Fin instead, the brow becomes a translucent crest and the rest stays the same.

---

## 8. PCB change requests (next revision only; nothing is possible on Rev A)

None of the concepts need a PCB change to work on Rev A. These are wishes for Rev B:

| Concept | Next-revision ideas |
| --- | --- |
| All | (a) An on-board 1S charger with power path and a JST PH 2-pin battery connector (removes the PowerBoost, pigtail, second USB-C port and VBUS-margin question, and keeps USB data on the one port). (b) A battery-voltage or "on battery" signal to a GPIO, so the screen can show charge state and the cloud can log outages. (c) J3 at the board edge nearest the planned antenna zone (also shortens the RF feed, already a layout to-do). |
| Ledger, Reef Fin | One RGB LED (or LEDs at a 4 mm or larger pitch) at a fixed "tide line" position for the family. Tag-Connect reachable from the back without removing the board. |
| Prism, Tide Pebble, Field Unit (stacked) | Put USER, RESET, ISP and the LEDs on the side facing away from the display, and/or use a side-actuated (right-angle) USER switch on the top edge. That removes the plunger, hinge or crank. |
| Tide Pebble | Side-firing LEDs at the board edge for an even waterline glow. |
| All | A display connector on the back (or an FPC) so the stacked build doesn't loop a cable around the edge. Confirm J5's opening direction before then. |

---

## 9. Questions for Brian

1. **Placement:** where will the gateway live: shelf or desk by the tank, the side of the aquarium cabinet, a wall, or somewhere else? How far from open water? (Chooses Ledger or Reef Fin; sets PETG and drip details.)
2. **Battery purpose and run time:** keep reporting through a power cut (UPS), or move it around unplugged? How many hours? My estimate is about 10-22 h for 2000 mAh (not measured). Is 1000 / 2000 / 3000+ mAh right?
3. **USB data:** is it OK that on battery builds the external USB-C is charge-only, and the console needs the case opened (or the Field Unit's unpluggable umbilical)?
4. **LCD module measurements:** can you measure (or send a photo with calipers of) the module thickness, where the active area sits on the 58 x 35 board, and the height and position of its PH connector? These set the window position and the standoff length (6 mm vs 8 mm).
5. **Fitted headers:** will J2 (SWD) and J4 (UART through-hole) be fitted on the build? J4 with pins adds about 8.5 mm of height.
6. **Antenna:** OK to standardise on the Molex 146153 FPC (dual band), using a longer-lead version where needed (lower gain, same type), or do you prefer the 219611? Is your Wi-Fi 2.4 GHz only (which would allow the smaller W24P-U)?
7. **VBUS margin:** OK with kicad-designer and firmware deciding whether to leave the USB_VBUS 0 Ohm unfitted on battery builds (5.2 V boost vs 5.25 V abs max)?
8. **Printer:** which printer and bed size? Multi-material (AMS/MMU)? Which filaments do you have (PETG, translucent PETG, TPU, PLA)? Any access to laser-cut acrylic for a lens or light pipe?
9. **Look:** a light Sand body with a coral key, or dark Abyss navy? Any colour that must or must not be used near the tank?
10. **Lens:** open window (cheapest, glass exposed) or a clear acrylic cover lens (protects the LCD, needed for Tide Pebble)?

---

## 10. Hand-off notes for fusion-enclosure (once a concept is chosen)

- Take board positions from 00-pcb-reference.svg / the .kicad_pcb, not from the brief (USER is top-centre; the buck is bottom-left).
- Model the LCD window as a separate bezel insert until the module is measured.
- Keep these clearances: 11 mm left of the gateway (pigtail plug), 9 mm right (J5 cable), 8 mm standoffs for stacked builds, 0.5 mm all round, walls 2 mm or more.
- Antenna zone 12-15 mm or more from the LCD and PCB ground edges, 30 mm or more from the battery and PowerBoost, no metal or carbon-filled material.
- Hold the 103450 cell in a cradle with foam, away from the buck and the PowerBoost inductor, and never pressed by a screw boss.
