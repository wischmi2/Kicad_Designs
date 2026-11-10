# nRF54L15 feather + sens1 pH node: enclosure concepts (2026-10-25)

Concepts only, no CAD. Brian picks one, then fusion-enclosure models it.
Visual page: `index.html` (this folder). Sketches: `00-stack-reference.svg` to `05-family.svg`.

## Summary and recommendation

| # | Name | One-line idea | Looks | Setting | Print / seal | PCB change (5 = none) | Total |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | **Tidemark** | A slim Ledger-family column that hangs on a sump or tub rim. The probe drops straight down and the panel is a remote "leaf" card | 4 | 5 | 4 | 5 | **18** |
| 2 | **Slate** | A field instrument: an orange spine holds the boards and battery, and a thin wing carries the panel behind a window | 4 | 4 | 4 | 5 | **17** |
| 3 | **Shard** | A faceted post at the water's edge, with the panel on the sun facet and the antenna in a crystal crown above it | 4 | 4 | 3 | 5 | **16** |
| 4 | **Lily** | A floating pad with a bud. The panel faces the sky and the probe hangs through the pad's notch | 5 | 3 | 2 | 5 | **15** |

**My recommendation:**
- **Tidemark** if the node lives at an indoor tank, sump, tub or hydroponic reservoir. It is the smallest (about 32 x 78 x 32 mm), the easiest to seal (one face seal, every port facing down), and it belongs to the Ledger gateway family.
- **Slate** if the panel must be built in, or the node lives outdoors on a deck, hood or pond edge.
- Both use the same internal **cartridge**: a printed sled carrying the boards, battery and port plate. fusion-enclosure can model the cartridge once and put either shell around it.
- None of the four needs a PCB change. Two optional sens1 requests (R1, R2 below) would make every concept better.

Three facts from the brief shape everything here:
1. **The panel is bigger than the board.** The validated panel is the PowerFilm LL200-2.4-75 at 94 x 73 x 0.22 mm (solar-analysis-v4.md). The boards are 50.8 x 22.86 mm. An integrated panel therefore sets the product's footprint (Slate, Shard, Lily), so Tidemark keeps the panel remote.
2. **The panel is rated for indoor use.** It is a PET-laminated indoor cell. Outdoors it must sit behind a UV-stable window. In daylight it gives far more than the node needs, so outdoors the tilt hardly matters. Indoors, where it sits relative to the lights matters most.
3. **Keep electronics out of the water.** The team behind pHin, a floating pool monitor, later said floating units let water seep in over time. Their successor, the Crystal Water Monitor, keeps the electronics on the deck and runs a cable to the probe. Tidemark, Slate and Shard follow that pattern; Lily goes against it.

---

## 1. Brief

**What it does.** A solar-harvesting BLE node: the nRF54L15 feather (main board) with the sens1 isolated pH board (Atlas pH OEM) stacked underneath on the same 50.8 x 22.86 outline and holes. It measures pH through an SMA-connected electrode that lives in water, and reports to the Pouch gateway.

**Where it lives (to confirm, Q1).** "Outdoor/aquatic". The family notes so far place the Feather + pH node "near the sump". The solar path was tuned for indoor light (200-1000 lux), but the brief also says outdoor. So I cover both: indoor tank, sump, tub or reservoir (Tidemark, Slate), and outdoor pond, pool or garden water (Slate, Shard, Lily).

**Who handles it and how often.** Brian. It is installed once, and the probe gets calibrated and eventually replaced (pH electrodes are consumables). USB-C charging should rarely be needed because the panel charges it. SWD is developer-only, so opening the case for it is fine. The single button is used now and then (wake, pair, show status).

**Environment.** Salt splash and salt creep at a sump; condensation (a sealed box cycles warm and cold every day); UV and rain outdoors; a cell in a dark box in sun can pass LiPo charge limits; algae on anything that floats.

**Hard constraints (from the board file and STATUS.md, 2026-10-25):**

| Item | Fact (Feather coordinates: fx from the USB end, fy from the AE1/SW1 long edge) |
| --- | --- |
| Main board | 50.8 x 22.86 x 1.6, R2.54 corners, all parts on top, flat bottom |
| Holes | 2.7 mm at fx 2.54 / 48.26, fy 2.54 / 20.32. USB end plated GND (brass is fine); far end NPTH, nylon only |
| J1 USB-C | Centred on the fx = 0 edge, mouth at the edge. Charge-only |
| CN1 FFC | Molex 503480-1400, about 1.0 mm tall, centred on the fx = 50.8 edge; the FFC folds down to sens1 |
| U5 solar / U4 battery | JST PH side entry at fx 8.5-14.85. U5 opens to the fy = 22.86 edge, U4 to the fy = 0 edge |
| J3 SWD | Samtec FTSH-105 at (18.85, 4.26), roughly 5.2-6.0 mm tall (sources disagree) |
| SW1 | Omron B3U-1000P, top-actuated, at (26.40, 2.10). Listings give 1.6 mm tall, 0.15 mm travel, 1.5 N |
| LED1 | ROHM SML-P12Y, yellow 590 nm, 1.0 x 0.6 x 0.2 mm, at (30.60, 5.26) |
| AE1 | Johanson 2450AT18A100E at (44.67, 2.78); no-ground area fx 42.15-50.8, fy 0-6.46. A U.FL fallback (RF1) exists |
| sens1 | Same outline and holes (re-layout in progress). J1 SMA probe input on the USB-end edge. **Stack height unknown** |
| Panel | PowerFilm LL200-2.4-75: 94 x 73 x 0.22 mm, 1.2 g, flexible a-Si, PET laminate, foil-tape terminals, max Voc 3.7 V |
| Probe | Atlas consumer-grade pH probe: SMA male, 1 m cable. Atlas' SMA extension cable (RG179, 2.5 mm jacket) comes up to 7.5 m |
| Build | FDM on the Snapmaker U1 (4 toolheads; PETG and TPU listed; ASA needs the optional top cover). Walls 2 mm or more, 0.5 mm clearance, M2.5 heat-set inserts, off-the-shelf o-rings |

**Parameters (unknown, carried as variables; sketch values in brackets):**

| Symbol | Meaning | Sketch value |
| --- | --- | --- |
| Hs | Main board bottom to sens1 top (standoff length) | 8 |
| S1b | Tallest part on sens1's bottom side (0 if flat) | 0 |
| Tm | Main-board top envelope (tallest part + 0.5) | 7.0 |
| F | FFC loop beyond the far edge, about (Hs + 1.6)/2 + 1.5 | 6.3 |
| P1 | "Heel" for sens1's SMA at the USB end (pigtail plug) | 14 (about 3 with R2) |
| B (L x W x T) | Battery | 40 x 25 x 7 (a 702540-size pouch; size class only, not a chosen model) |

**Stack depth Ds** = Tm + 1.6 + Hs + 1.6 + S1b (18.2 mm at the sketch values). Every formula below uses Ds.

---

## 2. Shared engineering (all concepts)

**Cartridge.** A printed sled holds the main board, sens1, the battery cradle and the port plate. USB-end standoffs are M2.5 brass in heat-set inserts. Far-end standoffs are printed pegs with nylon M2.5 screws and captured nylon nuts. The battery cradle uses foam, never screw pressure. Each concept is a different shell around the same cartridge.

**Antenna rules.**
- Plastic only within 15 mm of AE1: no inserts, screws, metal trim, carbon-fibre (PETG-CF, ASA-CF) or metal-filled filament, and no conductive paint.
- At least 10 mm (preferably 15 mm) from the panel. The a-Si panel's electrode films behave like a conductive sheet, so the antenna is never under the panel.
- At least 10 mm from the battery and at least 25 mm from water. The antenna corner always points up or outward.
- In the antenna zone, prefer non-black filament or check range with the chosen colour; some blacks use carbon-black pigment.
- If RF1 (U.FL) is ever used, each concept has a plastic-only zone of about 35 x 10 mm in its brow or crown for a small flexible antenna.

**Probe exit (default: replaceable).**
- sens1 J1 connects by a short RG316/RG174 pigtail to an IP67/68 SMA bulkhead jack in the wall. Examples found: RS PRO panel jacks with silicone o-rings (IP68), GCT RFPC-SMA16-FN-A (IP67/IP68), Amphenol 901-10743 (IP67). Check the cut-out and o-ring on the datasheet.
- The probe screws on from outside, and a TPU boot covers the mated plug. The electrode can be swapped without opening the case.
- Alternative (permanent): pass the probe cable through a split TPU grommet (or an icotek-style split gland, which is made for pre-terminated cables) and plug it in inside. Water-tight, but the case must be opened to change the probe.
- A standard PG7 gland won't pass the SMA plug, and its range doesn't grip a 2.5 mm cable.
- The pH input is high impedance, so a wet or salty SMA gives drifting readings. That is another reason for the boot and the desiccant.

**USB-C.** The receptacle isn't waterproof, so the case seals the opening. A 12.5 x 7 mm tunnel (wall 2.5 mm, J1 0.5 mm behind it) takes a tethered TPU 95A bung with two 0.3 mm interference ribs. It points down wherever possible. Shard keeps USB internal.

**Key and light.**
- The key is a TPU 95A membrane co-printed into the wall (the U1's second toolhead) or clamped as a separate disc. A printed plunger stops 0.2 mm above the B3U, because the switch only travels 0.15 mm.
- The light is a clear PETG (or 2.5 mm acrylic rod) light pipe fused into the wall, ending 0.5 mm above LED1, behind a coral translucent "eye". The yellow 590 nm LED behind coral reads warm amber.
- Both are sealed by being part of the wall, with no gaps.

**Seals.**
- Face seals use 2.0 mm silicone or EPDM o-ring cord bonded into a loop, or a stock o-ring stretched into a rounded-rectangle groove.
- Starting groove: about 2.7 wide x 1.5 deep (about 25 % squeeze). Confirm with the o-ring supplier's groove calculator.
- Sealing faces print flat on the bed or get ironed. Use 4+ perimeters and 100 % infill around grooves and bosses.
- An adhesive ePTFE vent (the type RuuviTag uses) equalises pressure so daily temperature swings don't pump damp air past the seals. Add 2 g of silica gel inside.
- **IP ratings below are design targets. Claim them only after a dunk test** (30 min at 15 cm with a dry tissue inside, then IP67 at 1 m if the case should claim it). FDM can reach IP65-67, but nothing is certain until it's tested.

**Heat.** Outdoors in sun, use a light colour (Sand ASA) and keep the battery in the panel's shade. Confirm whether the battery has an NTC for the nPM1300 so charging stops when it is hot (Q3).

**Materials.**
- PETG indoors: humidity and salt splash are fine. Not for sun.
- ASA outdoors: UV-stable. Needs the U1 top cover or a draught-free room; check that Brian has it.
- TPU 95A for keys, bungs, boots and feet.
- Clear windows: laser-cut 2 mm polycarbonate (tough) or acrylic (clearer, better UV). Printed "clear" PETG is too hazy for a solar window.

---

## 3. References (each looked up)

| Reference | Link | What it teaches here |
| --- | --- | --- |
| Crystal Water Monitor review (Residential Systems) | https://www.residentialsystems.com/technology/product-reviews/review-crystal-water-monitor-smart-pool-and-hot-tub-sensor | Electronics on the deck and the probe on a 4 ft cable with a locking connector; a mounting plate plus a pole adapter. The pHin team's lesson: floaters let water in. Basis of Tidemark, Slate and Shard, and the warning on Lily |
| pHin / Sutro floating monitors (search summary, Yanko Design) | https://www.yankodesign.com/2019/09/09/sutros-floating-pool-monitor-lets-you-measure-your-pools-alkalinity-and-chlorine-levels/ | Floating is a known, loved form for pools (Lily), but the sealing risk is real |
| Bluelab Guardian Monitor support | https://support.bluelab.com/bluelab-guardian-monitor | Keyhole wall mount close to the reservoir, probes plugged in at the base, and a separate suction-cup probe holder. Bottom-facing ports; a probe holder as an accessory |
| Seneye mag holder (AquaNerd) | https://aquanerd.com/2017/07/the-seneye-reef-monitor-mag-mount.html | Reef sensors mount on glass (suction or magnet, glass up to 10 / 16 mm). Tidemark's swappable rim clips |
| Ecowitt WH51 | https://shop.ecowitt.com/collections/wifi-sensor/products/wh51 | A small garden sensor sold as IP66: the realistic target for printed outdoor shells |
| Gardena smart sensor | https://www.gardena.com/uk/products/smart/smart-system/smart-sensor/967986501/ | A low, flat outdoor sensor that a mower can pass over (it stands about 20 mm proud, per a retailer). Simple, quiet outdoor form |
| RuuviTag spec (via retailers and the Ruuvi PDF) | https://f.ruuvi.com/uploads/default/original/1X/2850eb7fa06ed66231eeba5bfa1e6014e5476692.pdf | IP67 polycarbonate case, a lubricated NBR o-ring and a Gore vent membrane: the seal-plus-vent recipe used here |
| Bang & Olufsen Beosound Explore (Wex listing) | https://www.wexphotovideo.com/bang-olufsen-beosound-explore-grey-mist-bt-speaker-3100073/ | A premium IP67 outdoor object: a hard shell plus a rubberised base. Slate and Shard's TPU foot |
| Ledger gateway (this studio) | C:\Personal-Agents\shared\design\pouch_gateway\enclosure_ledger\NOTES.md | Family language: brow over the antenna, one coral key, a status pill, Abyss PETG. Its brow print risk (70 deg overhang face-down) is why Tidemark prints roof-down |
| Teenage Engineering, Braun ET66 (from the gateway study) | see pouch_gateway concepts.md | Slate's exposed-construction language (orange body, visible screws); Tidemark's single accent key |
| PowerFilm LL200-2.4-75 | https://powerfilmsolar.com/products/electronic-component-solar-panels/indoor-light-series/ll200-24-75 | 94 x 73 x 0.22 mm, PET laminate, indoor-rated: sets the integrated-panel footprint and the window rule |
| icotek split cable glands | https://www.icotek.com/en/products/cable-glands | Glands for cables that already have connectors (IP54-IP68 by type): the "permanent probe" option |
| SMA panel jacks (RS PRO, GCT, Amphenol) | https://uk.rs-online.com/web/p/coaxial-connectors/2469411 , https://www.digikey.com.mx/en/products/detail/gct/RFPC-SMA16-FN-A/9925279 | o-ring-sealed SMA bulkheads exist off the shelf: the replaceable probe port |
| Atlas consumer-grade pH probe and SMA extension | https://atlas-scientific.com/probes/consumer-grade-ph-probe/ , https://ca.robotshop.com/products/atlas-scientific-sma-male-to-sma-female-extension-cable-green-75m | SMA male, 1 m cable; RG179 extensions up to 7.5 m, so the node can sit well away from the water |
| Snapmaker U1 review (Tom's Hardware) | https://www.tomshardware.com/3d-printing/snapmaker-u1-review | 4 toolheads (TPU co-printing works); ASA officially needs the top cover |
| MakerWorld waterproof box / jar | https://makerworld.com/en/models/454290-waterproof-box | Makers' advice: PETG over PLA (creep), 100 % infill where it seals, a bought o-ring rather than a printed gasket |

I couldn't find a reachable Ovyl outdoor case study in this session. The gateway study's Ovyl references (integrated product, installer feedback) still apply.

---

## 4. Concepts

### Concept 1: TIDEMARK (01-tidemark.svg)

**Idea.** The Ledger gateway's small sibling: a slim Abyss column with a leaning brow that hangs on the rim of a sump, tub, tank or reservoir. Under the brow are the antenna, a coral eye and a coral key. It marks where the water is, and the probe drops straight down from its foot into the water. The panel is a separate "leaf" card that goes where the light is (under the reef light, at a window). Indoors, where the panel sits is what decides the energy, and the boards are too small to carry a 94 x 73 panel anyway.

**Form.**
- **32 W x 78 H x 32 D mm** at the sketch values, portrait. The boards stand upright with the USB end down, parts facing the front, and sens1 behind.
- Parametric:
  - Width = max(23.9, B_W + 2) + 5.
  - Toe height = 2.5 + F + 51.3 + 3. The heel adds P1.
  - Depth = 5 + Ds + 1 + B_T + 1 (32.2 at the sketch values).
- **Brow:** the top 20 mm of the face leans back 20 deg. AE1 sits about 16 mm below the flat roof, inside the brow. The brow is a plastic-only zone (the family rule).
- **Toe and heel:** the bottom steps. The toe (front) carries the USB-C bung right under J1. The heel (rear, 14 mm deeper) holds sens1's SMA, the pigtail and the bulkhead, so the probe leaves at the back, straight down beside the glass.
- Vertical corners R4, front edge R1.5.
- **Parting line:** one sleeve (four walls and the roof) plus a stepped foot cap with a face o-ring. The seam is on the underside, so you can't see it in use.

**CMF.**
- Indoors: Abyss navy PETG, matte (textured-plate look where it lies on the bed; fuzzy skin on the side walls only).
- Outdoors: Sand ASA.
- Coral TPU key, coral translucent PETG eye, graphite TPU bung and boot, lowercase "ph" debossed 0.4 mm above the toe.
- Rim clips in PETG with TPU pads.

**Interaction.**
- Key: TPU membrane (dia 7) on the front, 5.2 mm plunger to the B3U.
- Eye: dia 2.5, 6.3 mm light pipe to LED1, 5.3 mm from the key centre. Key and eye form a small "face" under the brow.
- USB-C: pull the bung on the underside; the cable hangs down.
- Install: slide a clip for the wall thickness (6 / 10 / 12 / 15 / 19 mm) onto the dovetail rail on the back, hang it on the rim, screw the probe onto the heel bulkhead, add the boot, put the probe in a holder. The leaf card goes up with a suction cup or 3M Dual Lock.
- The same rail takes the family French cleat for a cabinet wall.
- Service: 4 screws on the foot cap, then the cartridge slides out downward with its leads.

**Sealing.**
- Target **IP66, built to IP67 geometry.** One face o-ring on the foot cap, everything else pointing down, a drip edge round the toe, an ePTFE vent in the heel, silica gel.
- Every opening points down, so nothing collects water. Don't hang it over an open, bubbling sump chamber (salt spray).

**Build.**
- Sleeve printed **roof-down** on the bed: the brow becomes a 20 deg lean (no supports), the roof is a crisp flat first layer, and the insert bosses face up.
- TPU key and clear pipe co-printed. Foot cap printed sealing-face down. Sled, clips and leaf frame print flat.
- 4 M2.5 inserts in the foot only, more than 50 mm from AE1.
- About 4.5 h sleeve + 1 h cap + 1.5 h sled + 1 h clips + 1.5 h leaf frame, so **about 9.5 h. Difficulty: easy to moderate.**
- Condition: the cartridge slides in far end first under the key plunger. SW1 (1.6 mm) must be the tallest part between fx 26 and the far edge (CN1 is 1.0, LED 0.2; check X1 and L9/L10). If something is taller, switch to the "front plate" variant: the front wall becomes a separate screwed plate, with a second seal.

**PCB:** no change needed. R1 and R2 are optional improvements.
**Scores:** Looks 4 | Setting 5 (indoor wet) / 3 (outdoor) | Print / seal 4 | PCB 5 | **18**

### Concept 2: SLATE (04-slate.svg)

**Idea.** A field instrument that shows how it's made. A thick signal-orange spine holds all the electronics. A thin graphite wing carries the panel behind a polycarbonate window, held by a ring of black button-head screws. It lies flat on a hood or deck, stands on a fold-out leg toward a lamp or a window, straps to a post, or hangs on the cleat. The antenna sits in the spine's outer edge, 25 mm from the panel, so it is never covered.

**Form.**
- **104 L x 116 W.** Spine 104 x 34 x 26; wing 82 wide, 8 thick at the spine tapering to 5 at the tip.
- Parametric: spine height = 5 + 1 + Ds (24.2 at the sketch values, rounded up to 26).
- Boards lie flat at the port end of the spine, parts up. The battery lies in the spine's far end, at least 14 mm from AE1, which leaves the wing thin.
- The port end steps out 14 mm at the sens1 level into a "dock" carrying the SMA bulkhead. USB-C sits in the wall above it.
- Parting lines: the spine lid (face o-ring, 6 screws) and the wing bezel (window gasket, 6 screws). The panel lead passes from wing to spine through a sealed internal hole (potted).

**CMF.**
- Signal-orange ASA spine, graphite ASA wing, black anodised-look button-head screws.
- The two screws nearest AE1 are black nylon, so they look the same as the rest.
- Yellow TPU key; coral or clear eye; laser-cut 2 mm PC window; TPU feet.
- Family colourway: Abyss spine with a coral key.

**Interaction.**
- Key and eye on top of the spine, straight over SW1 and LED1 (the key sits 4 mm from the spine's outer edge, so that edge gets a small R2).
- USB-C bung and probe boot on the dock.
- The fold-out leg (printed, 1.75 mm filament pin hinge) sets 30, 45 or 60 deg.
- Strap slots for a 20 mm hook-and-loop strap; a cleat rail under the spine.
- Service: spine lid off (6 screws) gives J3, the battery and the cartridge.

**Sealing.**
- Target **IP66.** A flat window collects water, so the wing slopes 3 deg (8 to 5 mm) to shed it, and the window seals under a bezel (compressed gasket, not glue).
- Two seals plus the panel-lead hole, so a bit more risk than Tidemark.

**Build.**
- Spine body printed upright (open top up), lid face-down, wing face-down with a recess for the window, bezel flat. No supports.
- Window laser-cut or bought.
- About 4 h spine + 1 h lid + 4 h wing + 1.5 h bezel + 1.5 h sled and leg, so **about 12 h. Difficulty: moderate.**
- A 104 x 82 wing in ASA can warp: use a brim and an enclosure.

**PCB:** none.
**Scores:** Looks 4 | Setting 4 | Print / seal 4 | PCB 5 | **17**

### Concept 3: SHARD (03-shard.svg)

**Idea.** A crystal standing at the edge of a pond or a planted bog: a faceted Sand ASA post. The 10 deg sun facet carries the panel, and a coral crystal crown above it holds the antenna. The boards stand behind the top of the panel, so AE1 sits 10 mm above the panel's top edge, and the battery hides low in the panel's shade. It is the outdoor, sculptural option, and its height keeps the radio well above the water and grass.

**Form.**
- **90 W x 56 D x 158 H.** A pentagonal plan (front sun facet, two angled side facets, flat back). The front leans back 10 deg so rain runs off.
- Parametric: height = window bottom (17) + 100 + 10 + 6.1 + F + 2.5 + crown (about 18).
- Window 100 x 79 for the 94 x 73 panel.
- Parting line runs along the side facets (front shell with the window / rear shell), so the seam reads as a facet edge.
- The crown is printed in coral ASA by toolchange, as part of the shells, so it adds no seal.

**CMF.** Sand ASA (keeps the cell cooler), coral crown, PC window, graphite TPU foot and key. The light pipe sits on the back face. A 30 mm pipe up into the crown would be lossy, so treat a glowing crown as an experiment.

**Interaction.**
- Key and eye on the back face (away from the sun) at about 106-111 mm height: easy to reach on a post.
- USB-C is internal: rear shell off (8 screws). The node charges from the sun, and SWD needs the case open anyway.
- Mount: two stainless hose clamps through slots in the back (pole 20-60 mm), about 100 mm below AE1, or a socket in the base for an ASA or aluminium stake.
- Probe: bulkhead in the base, then the probe on its 1 m cable (or a 7.5 m extension) to the water.

**Sealing.**
- Target **IP66.** Silicone cord in a groove along the facet parting line, a window gasket, a bottom-facing vent and bulkhead, and a drip edge.
- Long 3D parting line, so it is harder to seal than Tidemark.

**Build.**
- Each shell prints on its parting face, so the facets come out as walls and slopes of 45 deg or more. The crown's lower facets need a check, and painted supports may be needed under the crown's overhang on the rear shell.
- 8 M2.5 inserts below z = 100 mm; a printed hook and tongue joins the shells at the crown.
- About 6 h + 6 h shells + 2 h sled + 1 h clamp parts, so **about 15 h. Difficulty: moderate.**
- Large ASA parts need the U1 top cover.

**PCB:** none.
**Scores:** Looks 4 | Setting 4 (outdoor) | Print / seal 3 | PCB 5 | **16**

### Concept 4: LILY (02-lily.svg)

**Idea.** A lily pad that floats on a pond, pool or big reservoir.
- The panel lies in the pad, facing the sky, under a slightly crowned window.
- All the electronics stand upright in a bud with a coral screw cap. The antenna is at the top of the bud, about 55-60 mm above the water.
- The pad's natural notch is the moonpool: the probe hangs in it, so the bulkhead faces down into air and **nothing pierces the hull below the waterline**.
- The pad itself is a solid-printed buoyant body with no electronics inside.

It is the most poetic form, but it is the riskiest to seal (see the Crystal Water Monitor lesson).

**Form.**
- Pad **176 x 112 x 24**; bud dia 42-43 rising 64 above the deck; cap dome about 8. Total height about 96.
- Parametric: bud ID = sqrt((max(22.86, B_W) + 1)^2 + (Ds + B_T + 2)^2) (37.6 at the sketch values, so OD about 43 with 2.5 mm walls).
- Freeboard about 10 mm: an estimate (mass about 250-300 g). Check buoyancy and the righting moment from Fusion mass properties, and trim with washers under the panel end, more than 60 mm from AE1.

**CMF.** Sand or white ASA pad and bud (cool in sun, shows algae so you know to clean it), coral ASA cap, PC window, TPU probe collet and tether loop.

**Interaction.**
- Lift it out with the tether, unscrew the cap, pull the cartridge up by a tab.
- Key and eye on the bud's side.
- USB-C internal (cap off).
- A tether to the bank keeps it out of skimmers and filters.

**Sealing.**
- The bud needs **IP67 minimum, and IP68 is wanted** (waves, capsizing).
- The bud cap is a coarse printed thread with a face o-ring (as on the MakerWorld jar). The window needs a gasket and the panel lead a potted pass into the bud.
- The pad doesn't have to be dry, but it slowly gains weight if water gets in. Use 6+ walls, and consider an epoxy coat.

**Build.**
- About 9 h pad + 4 h bud + 1.5 h cap + 1.5 h sled + 1 h small parts, so **about 17 h. Difficulty: hard.**
- Printed threads and a buoyancy trim to tune; expect two or three test prints.

**PCB:** none.
**Scores:** Looks 5 | Setting 3 (5 on a pond, 1 at a sump) | Print / seal 2 | PCB 5 | **15**

---

## 5. Family direction: "Brow, Tide line and Service foot" (05-family.svg)

This extends the gateway's "Brow and Tide line":
1. **Brow or crown.** The antenna always lives in a marked, plastic-only top zone: a 20 deg brow (Tidemark, gateway), a crown (Shard), a cap (Lily) or the spine's outer edge (Slate).
2. **Tide line.** One coral light (pill or dot) and one coral key per device.
3. **Service foot.** Every port (USB-C bung, probe bulkhead, solar gland, vent) leaves from one graphite TPU or ASA foot that faces down or aft. Nothing faces up.
4. **Common cartridge.** The same sled, port plate and battery cradle in every Feather-node shell.
5. **Palette.** Abyss PETG for indoor wet zones; Sand ASA outdoors in sun (a cooler battery); coral for light and keys; graphite TPU for feet and bungs.
6. **Mounting.** The same dovetail rail on every node, taking rim clips or the family 45 deg cleat.

The gateway (Ledger) plus Tidemark is the tightest family. Slate is the "field kit" sub-line in orange; in Abyss with a coral key it joins the main family.

---

## 6. PCB change requests (none required; for kicad-designer to judge)

| ID | Concepts | Request | Why |
| --- | --- | --- | --- |
| R1 | All (stacked) | On sens1, keep the far corner under AE1 free of copper (match the main board's area fx 42.15-50.8, fy 0-6.46, all layers) | Otherwise sens1's ground plane sits Hs + 1.6 mm (about 10 mm) under the chip antenna, a second ground the antenna's layout didn't plan for. Recommended |
| R2 | All (optional) | sens1 J1 as an o-ring-sealed, panel-threaded PCB SMA (IP68-class parts exist) placed so it passes through the end wall, rather than a plain edge SMA | Removes the pigtail and bulkhead, and shrinks the heel or dock from 14 mm to about 3 mm. Trade-off: the probe's mating force goes into sens1 and its standoffs |
| R3 | Tidemark (only if needed) | None if SW1 is the tallest part between fx 26 and 50.8. Otherwise no PCB change: switch to the front-plate variant | Cartridge slide-in clearance |
| R4 | Shard (optional, not recommended) | LED nearer the far end to light the crown | It's crowded and next to the antenna; a longer pipe is the better test first |

---

## 7. Mechanical numbers fusion-enclosure still needs

1. **sens1 stack:**
   - Standoff length Hs; sens1 tallest top-side and bottom-side parts (S1b).
   - Whether sens1's parts face up (toward the main board) or down.
   - sens1 CN1 position and side; FFC length and contact type (same-side or opposite) for the fold.
2. **sens1 J1:** part number, edge-mount or vertical, which side of sens1, how far it sits past the USB edge, and the mating plug's length (sets P1).
3. **Battery:** model, L x W x T, capacity, lead length, whether it has an NTC (nPM1300 thermal cut-off), protection PCB size.
4. **Main-board heights not in the STEP** (most EasyEDA bodies are missing):
   - J3 FTSH-105: sources give 5.21 or 5.97 mm.
   - U4/U5 S2B-PH-K-S: distributors give 8.0 / 9.4 mm, which looks like the wrong axis. Use JST's drawing.
   - J1 TYPE-C-31-M-12 height and how far its mouth sits from the edge.
   - X1, L9/L10 and AE1 heights (for the Tidemark slide-in check).
   - The mated heights of the JST PH plugs plus the cable bend radius (they leave the long edges).
5. **Panel:** confirm the LL200-2.4-75 (or two in parallel = two windows, or one 94 x 146 area), its lead length, and remote or integrated.
6. **Probe:** which Atlas probe, its body diameter and length (holder or collet), cable length, extension.
7. **Site:** where it mounts, the rim or glass thickness (Tidemark clips), pole diameter (Shard), and the distance from the water to the mounting point.
8. **Printer:** U1 top cover (ASA), TPU hardness on hand, and whether multi-material co-printing (TPU in PETG) is OK. Access to laser cutting (window).
9. **Fasteners:** nylon M2.5 screw and nut lengths for the far holes; M2.5 brass standoff height = Hs.

---

## 8. Questions for Brian

1. **Where does this node live?** Indoor sump, tank, tub or reservoir; outdoor pond or pool; or garden water? That picks Tidemark, Slate, Shard or Lily.
2. **Panel:** remote card (Tidemark) or built in (Slate, Shard, Lily)? Is the LL200-2.4-75 still the panel? Outdoors it must sit behind a UV window because its PET laminate is indoor-rated.
3. **Battery:** which cell, and does it have an NTC? Outdoors in sun the enclosure can get hot enough to matter for LiPo charging.
4. **Seal level:** splash-proof (IP65/66), or must it survive falling in (IP67)? I'll only claim a rating after a dunk test.
5. **Probe:** replaceable from outside through an SMA bulkhead (my default), or a permanent cable through a gland?
6. **USB-C:** outside behind a TPU bung, or inside only (open the case to charge)?
7. **Printing:** do you have the U1 top cover for ASA, and TPU 95A? OK to co-print TPU keys into PETG or ASA walls? Can you get 2 mm PC or acrylic laser-cut?
8. **Colourway:** Abyss + coral (family), Sand + coral (outdoor), or the orange Slate "field kit"?
9. OK to send **R1** (sens1 copper keep-out under the antenna) and **R2** (sealed PCB SMA on sens1) to kicad-designer as requests while sens1 is being re-laid out?
