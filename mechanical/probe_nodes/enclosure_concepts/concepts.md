# Atlas probe nodes (ORP, dissolved oxygen, conductivity): enclosure concepts (2026-10-26)

Concepts only, no CAD. Brian picks one, then fusion-enclosure blocks it out in Fusion.
Visual page: `index.html` (this folder). Sketches: `00-stack-and-probes.svg`, `01-perch.svg`, `02-berth.svg`, `03-limpet.svg`, `04-staff.svg`, `05-family.svg`.
History: the 2026-10-25 run stopped after the three SVGs (00 reference, 01 Perch, 02 Berth) with no write-up. This run kept Perch and Berth (revised, see below), added Limpet and Staff, redrew the reference, and wrote this file. The folder is not in git; the coordinator commits.

## Summary and recommendation

| # | Name | One-line idea | Looks | Setting | Print / seal | PCB change (5 = none) | Total |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | **Staff** | A round bud (dia 44 x 80) slides on a stock 20 mm tube; the probe clips lower on the same tube. The base is a ballast foot, a spike or a rim clamp | 4 | 4 | 4 | 5 | **17** |
| 2 | **Perch** | A Tidemark-style column hangs outside a sump or tub wall, a saddle carries a rigid inner leg, and a split TPU collet holds the probe vertical | 4 | 4 | 4 | 5 | **17** |
| 3 | **Limpet** | A low shell sits on a bucket lid; the probe goes through the lid beside it in a TPU bushing; a cleat takes the spare cable | 4 | 3 | 4 | 5 | **16** |
| 4 | **Berth** | A wall monolith: the node on the shoulder, a tower with a storage and calibration bay, a post for the slack cable; the probe lives on a remote Hold | 4 | 3 | 3 | 5 | **15** |

PCB column: 5 = no change needed to build it. One item still needs checking on all four (P1, SMA barrel length), see section 6.

**Recommendation.**
- **Build the shared parts once**: the cartridge (boards, battery, port plate), the SMA boot, the Collet (probe holder) and the type band. Then choose the shell by where the probe lives.
- **Staff first.** It works wherever there is water and no usable rim or lid: tubs, buckets, ponds, planters, a bench with a beaker. The tube is the stake, the cable guide, the depth gauge and the cable reel. The shell is a round tube, so the seal is a stock round o-ring (the easiest seal in this set).
- **Perch second**, for sumps and tubs with an open rim. It is the one that matches the Tidemark and Tidemark-W columns exactly, so it keeps the family tight and the Fusion work smallest.
- **Limpet only if** Brian's EC/ORP probes live in lidded mixing or dosing buckets. **Berth only if** probes are pulled out often for calibration and a wall is close to the water; its bay can also be built alone as a shared probe rack.
- **Decision for Brian: bud or column for Staff?** If he wants one shell for the whole line, the Tidemark-P column fits the same tube through the family dovetail rail and a tube clamp ("Staff-rail"). The bud costs one more shell to model and print, and gains the round o-ring and a distinct pole-mounted look.
- None needs a PCB change to be built. The one open electronics fact is how far the SMA barrel sticks out past the board edge (P1): the ORP status says 5.6 mm, the DO and EC statuses say 7.6 mm. The foot design needs about 7 mm.

Four facts shape everything here:
1. **The probe size is unconfirmed.** The Atlas product pages give cable length, connector and ratings but not the body diameter or length. Sizes in the sketches (pH/ORP/EC 12 x about 150, DO 16.5 x about 120) come from the earlier run's retailer notes. Every holder takes the bore as a parameter (11.5 or 16 mm). Measure the real probes before Fusion.
2. **The probe lives in water and the node must not.** Four of the five existing concepts in this family already keep the electronics dry, with the antenna high and 25 mm or more from water. These do the same.
3. **The EC board's SMA shell is a live electrode** (the EC OEM has no probe ground, per its STATUS.md). Nothing metal may touch the plug, its shield or the nut. All holders are plastic.
4. **Atlas probes ship with an SMA plug, not a BNC.** The Atlas pages for ORP, DO and EC K1.0 all say male SMA by default, BNC as an optional adapter (+2 USD). The EC board STATUS says the EC probes ship with BNC and need an adapter; that looks wrong and should be corrected there.

---

## 1. Brief

**What it does.** Three battery-powered nodes, one measurement each: ORP, dissolved oxygen (DO) and conductivity (EC). Each is an nRF54L15 Feather main board plus one stacked Feather-sized sensor board in its own enclosure (Brian, 2026-10-25). The sensor boards are isolated variants of the sensor template with an Atlas OEM circuit (ORP 0x66, DO 0x67, EC 0x64) on the isolated side, read over I2C through an ADuM1250. The probe plugs into an SMA jack (BAT Wireless BWSMA-KWE-Z001, right angle, through hole) on the sensor board's x = 90 short edge, the USB end. The nodes are one family with the pH node (sens1) and the water-level node.

**Where it lives.** A reef or aquarium room: sumps, tanks, salt-mix and ATO buckets, plus possibly hydroponic reservoirs, tubs or ponds. Indoor, humid, salt splash and creep, condensation under lids. Brian has not fixed the container, so the four options cover different containers and mountings.

**Who handles it.** Brian. Installed once. The probes are calibrated and swapped: Atlas lists about 3 months between recalibrations for ORP and about 12-18 months of life; DO needs a membrane service about every 18 months and a yearly recalibration; the EC K1.0 probe has no electrolyte to deplete and is calibrated at installation. So the probe is lifted out now and then and the node stays put. Battery and USB-C are rare.

**Probes (Atlas product pages, read 2026-10-26):**

| Item | ORP (ENV-30-ORP) | DO (Atlas DO probe page) | EC K1.0 |
| --- | --- | --- | --- |
| Cable / connector | 1 m, male SMA (BNC optional adapter) | 1 m, male SMA (BNC optional adapter) | 1 m, male SMA (BNC optional adapter) |
| Depth / pressure | 35 m, 50 PSI | 352 m, 500 PSI | 352 m, 500 PSI |
| Temperature | 1-60 C, no temperature sensor | 1-60 C | 1-110 C |
| Life / service | 12-18 months, recalibrate about every 3 months (retailer summary) | about 4 year life, 18 month membrane service, yearly recalibration (search summary) | Calibrate at installation, no electrolyte |
| Body size | Not on the page. Assumed 12 x 150 | Not on the page. A retailer lists 16.5 x 116 for a similar SKU. Treat as unverified | Not on the page. Earlier note: 12 x 145.5 |
| Extras | Storage solution sold separately (125 ml) | Anti-fouling probe screen DO-AF-PS (12.99 USD); membrane kit | n/a |

I could not read the datasheets in this session (the Atlas file server returned errors, and the EC datasheet came back as a binary PDF I could not parse), so storage rules for DO and EC are **not confirmed**: ORP and pH must stay wet (Bluelab says never use RO water in a pH storage cap); check Atlas's guidance for DO and EC before fixing the storage cap design. The DO page name and SKU are also unclear (the page title says "Lab Grade", the board STATUS says ENV-40-DOX): confirm which probe is bought.

**Hard constraints (from the board STATUS files, 2026-10-26):**

| Item | Fact |
| --- | --- |
| Stack | Main board and sensor board, each 50.8 x 22.86 x 1.6, holes 2.7 mm at 2.54 / 48.26 and 2.54 / 20.32. Gap between boards about 8 mm (the SMA sits in it), Tm 7.0, bottom of the sensor board flat, stack depth Ds about 19.5 mm. FFC fold at the far end |
| Probe jack J1 | At the board centre line (y 121.43), barrel pointing out of the x = 90 edge. Barrel past the edge: 7.6 mm (DO and EC STATUS) or 5.6 mm (ORP STATUS, from its footprint fab layer). Jack height 6.5-8 mm. Not verified against the BAT Wireless drawing |
| USB-C | Feather J1, same end, centred; 9.6 mm from the SMA axis in depth. In an upright column both leave from the foot |
| Key and LED | SW1 (B3U-1000P, top-actuated, fx 26.4) and LED1 (590 nm yellow, fx 30.6), as in the other concepts |
| Antenna | AE1 at the far end. Plastic only within 15 mm; at least 10 mm from the battery; at least 25 mm from water |
| Battery | Sketch cell 40 x 25 x 7 (size class only). The EC OEM draws 10.6-26 mA while measuring (ORP about 3.5 mA, DO about 2.5 mA), so EC may want a bigger cell or a low duty cycle |
| Isolation | Isolated copper sits 8 mm under the main board's plated GND hole column: nylon fasteners at the USB / probe end |
| Build | FDM on the Snapmaker U1 (4 toolheads): PETG for dry parts, PCTG for wet or loaded parts, TPU 95A for seals, boots, collets and keys. Walls at least 2 mm, 0.5 mm clearance, M2.5 heat-set inserts, off-the-shelf o-rings |
| Not in the STEPs | The SMA jack and the OEM module have no 3D bodies (only the board, holes, CN1, U3, U4). Envelope values above come from the STATUS files |

**Environment.** Salt splash and creep, condensation, and a plug that is not waterproof. IP figures below are design targets only; claim one only after a dunk test (30 min at 15 cm with a dry tissue inside). The probes themselves are submersible per Atlas; the node is not meant to be.

---

## 2. References (each looked up; items marked "earlier" were read in the 2026-10-24/25 studies)

| Reference | Link | What it teaches here |
| --- | --- | --- |
| Atlas Consumer Grade ORP probe | https://atlas-scientific.com/probes/consumer-grade-orp-probe/ | Male SMA default, 1 m cable, 35 m / 50 PSI, 1-60 C, no size on the page. Links two guides on cutting the cable and plumbing probes into a pipe |
| Atlas DO probe | https://atlas-scientific.com/probes/dissolved-oxygen-probe/ | SMA, 1 m, 352 m / 500 PSI, 18 month service, anti-fouling screen sold separately: leave room around the tip for the screen |
| Atlas Conductivity K 1.0 | https://atlas-scientific.com/probes/conductivity-probe-k-1-0/ | SMA standard, 1 m, 1-110 C, calibrate only at installation |
| Atlas ORP storage solution | https://www.robotshop.com/products/atlas-scientific-orp-probe-storage-solution | A real storage product exists for ORP: the storage cap is a wet cap (water, potassium phthalate, potassium chloride) |
| Instrument Choice DO listing | https://www.instrumentchoice.com.au/products/atlas-scientific-dissolved-oxygen-probe-ic-dissolvedoxygenprobe | Source of 16.5 x 116 mm, for a similar but not confirmed SKU. Treat as a guess |
| Neptune Magnetic Probe Rack (MPR) | https://topshelfaquatics.com/products/mpr-magnetic-probe-rack-neptune-systems | Reef norm: a rack that holds four probes on the sump glass (acrylic, about 4 in long, magnets to 1/2 in glass), one oversize hole. Loose probes float and read air. The idea behind Berth's shared rack and every Collet |
| Bluelab Guardian Monitor support | https://support.bluelab.com/bluelab-guardian-monitor | Keyhole wall mount (two fasteners 172 mm apart), monitor within 2 m of the reservoir, away from water and nutrient salts; pH probe holder is a suction cup; pH storage cap with KCl solution, never RO or distilled water. Berth's keyholes, wet cap and cable reach |
| Hanna HI981520 Marine Monitor | https://www.bulkreefsupply.com/marine-monitor-ph-salinity-temperature-hanna-instruments-ob-a.html | Probes waterproof and held on suction mounts; the monitor housing is only IP65 and sits outside the tank on adhesive strips or screws. A realistic IP target for a node that never goes in the water |
| Crystal Water Monitor review (earlier) | https://www.residentialsystems.com/technology/product-reviews/review-crystal-water-monitor-smart-pool-and-hot-tub-sensor | Electronics on the deck and the probe on a cable with a locking connector: the pattern all four options follow |
| Seneye mag holder (earlier) | https://aquanerd.com/2017/07/the-seneye-reef-monitor-mag-mount.html | Reef sensors on glass by suction or magnet. Considered for a glass-mounted variant, dropped because a magnet or the water behind the glass sits close to the antenna |
| icotek split cable glands (earlier) | https://www.icotek.com/en/products/cable-glands | A pre-terminated cable gets a split seal: the SMA boot is the printed equivalent |
| RuuviTag spec (earlier) | https://f.ruuvi.com/uploads/default/original/1X/2850eb7fa06ed66231eeba5bfa1e6014e5476692.pdf | The seal-plus-ePTFE-vent recipe reused in every shell |
| Snapmaker U1 review (earlier) | https://www.tomshardware.com/3d-printing/snapmaker-u1-review | 4 toolheads, TPU co-printing: key, boot and bands print without a second step |
| Family concepts | `C:\Personal-Agents\shared\design\nrf54l15_feather\enclosure_concepts\concepts.md`, `C:\Personal-Agents\shared\design\feather_water_level\enclosure_concepts\concepts.md`, `C:\Personal-Agents\shared\design\pouch_gateway\enclosure_ledger\NOTES.md` | Brow over the antenna, one coral key and eye, graphite foot, Abyss PETG/PCTG; cartridge; Tidemark-W; the Eye; Ledger's brow overhang warning |

I did not find a design-studio case study for wet-probe nodes in this session. The comparison is with commercial reef and hydroponic monitors and the studio's own family. The Seneye Reef Monitor's own design could not be confirmed (no results).

---

## 3. Shared engineering (all options)

**Cartridge.** The same sled as the other nodes: main board, sensor board with an 8 mm gap, battery cradle (foam, never screw pressure), and the port plate. USB-end standoffs are brass M2.5 (the isolated copper is under the plated hole, so nylon at that end per the reference sketch). Far-end standoffs are printed pegs with nylon screws. The cartridge and the foot cap (or end plate) come out as one unit.

**SMA port (the new detail).**
- The barrel (1/4-36 thread, dia 6.35) passes through a dia 6.8 hole in the 2.5 mm foot wall. It needs about 7 mm past the board edge: wall 2.5, 0.5 clearance, about 4 mm of thread for the plug nut. If the jack really protrudes only 5.6 mm (the ORP note), only about 2.6 mm is left outside and the plug will not thread on. That is PCB request P1.
- A 1.5 mm TPU washer or a thin o-ring (about 6 x 1) sits on the barrel against the inside of the wall. The jack body is pressed to it by a printed **jack cradle** on the sled, which also takes the nut torque and the cable pull so the through-hole solder legs do not.
- The plug is protected by a **TPU 95A boot** (dia 12 x 28, graphite): a bell over the nut that seats in a 14 mm pocket in the wall, tapering to a 25 mm bend relief on the cable. The plug itself is not sealed, so the node claims IP66 only with the boot fitted. A tethered TPU **cap** closes the jack when the probe is off.
- Cable strain: two snap clips take the pull, with a drip loop on both sides. The SMA plug never carries the cable weight. Minimum bend radius assumed 20 mm for a roughly 3 mm cable.
- Salt creep: the pocket has a drip edge and a 1.5 mm salt-break groove. The high-impedance probe inputs (ORP, DO) drift if the jack is wet or salty, so the boot, the silica gel and a flux-clean board matter (the OEM datasheet asks for flux washing; use only clear coat if any, no coloured potting, per the ORP STATUS).
- **EC special case:** the plug shell carries a probe electrode. All parts near the plug are plastic; clips, screws and cradles that touch the cable shield are nylon or printed.

**USB-C.** A 12.5 x 7 mm tunnel with a tethered TPU bung, 9.6 mm from the SMA axis in depth, so 2.7 mm of wall between them. The bung overmould stays 6.5 mm deep or less.

**Key and light (as the other nodes).** A coral TPU membrane key over SW1 with a 0.2 mm gap plunger (the B3U travels only 0.15 mm). A 2.5 mm clear PCTG light pipe to LED1 behind a coral translucent eye, so the 590 nm yellow reads amber. Both are part of the wall, so they add no seal. Check carried over: the cartridge slides in under the key plunger, so SW1 (1.6 mm) must be the tallest part between fx 26 and the far edge.

**Labelling: one shell, a swappable identity.** The nodes must be told apart while staying one family.
- A **type band**, a 3 mm strip that clips into a groove at the foot, in the sensor colour: ph green, orp amber, do aqua, ec violet, water level bone. Five strips, one shell.
- A **lowercase code** (ph, orp, do, ec) debossed 0.4 mm on the band or the front.
- A **cable tag** and the **Collet ring** in the same colour, so a probe plugged into the wrong node is obvious.
- **Raised dots** (1-4) on the band as a non-colour cue, because amber, green, aqua and violet can be confusing for colour-blind users. Order: ph 1, orp 2, do 3, ec 4.
- The only coral on the node stays the key and the eye; the band is the only other colour. This is more colour than Tidemark's single accent, so it is a decision for Brian (question 8).

**The Collet (the probe holder, the new family part).** A split TPU 95A sleeve with bore = probe diameter - 0.5 (11.5 for pH/ORP/EC, 16 for DO), held by a PCTG clamp ring with two nylon screws, slid along the probe to set depth. It never covers the sensing tip, so the DO anti-fouling screen still fits. Tip clearance: at least 20 mm from walls and the floor (pH/ORP rule of thumb used in the earlier sketches; the EC cell and the DO membrane may want more; not verified). The Collet ring carries the sensor colour. One model; four holders.

**Probe storage.** A TPU storage cap with a sponge parks on a peg on every option, so a lifted probe is never left drying. The wet cap is right for pH and ORP (never RO water). For DO and EC the right storage is unconfirmed (see section 1).

**Interference between nodes.** The EC datasheet (summarised in the EC STATUS) says EC readings inject interference into the water, so do not take an EC reading while a pH/ORP/DO node in the same tank is measuring. That is firmware, but it also argues for spacing the probes (at least one hand width, not measured) and giving each its own holder.

**Seals.** Face seals use 2.0 mm silicone or EPDM cord bonded in a loop, or a stock o-ring in a groove about 2.7 wide x 1.5 deep (about 25 % squeeze). Sealing faces print flat, 4+ perimeters and 100 % infill around grooves and bosses. An adhesive ePTFE vent (RuuviTag style) and 2 g of silica gel in every shell. Targets: shell **IP66** (built to IP67 geometry), plug under the boot a lower claim until tested.

**Materials.** Abyss PETG for dry parts, **PCTG** for anything in the wet zone or under load (saddle, leg, clamp, Collet ring, tube clamps), TPU 95A for seals, boots, collets, bushings and keys, nylon M3 and M2.5 screws in or near the water (no stainless in the water, because metal near a pH or ORP electrode can shift readings and the EC shell is an electrode). Indoors no ASA is needed; Sand ASA only for a pond or outdoor Staff. Antenna rule as before: no carbon- or metal-filled filament within 15 mm of AE1; check range if using black.

**Battery.** The cartridge assumes the 40 x 25 x 7 size class. EC's 26 mA peak means a duty-cycled read or a bigger cell; a 50 x 34 x 10 cell grows the column to 41 W (Tidemark-P) or the bud to dia 52.

---

## 4. Concepts

### Concept 1: STAFF (04-staff.svg) - recommended first

**Idea.** A tide staff for a probe. The node is a round bud that slides up and down a stock 20 mm plastic tube; the probe clips to the same tube below it. The tube is the stake, the cable guide, the depth gauge and the cable reel in one cheap part. The base decides where it lives: a sand-filled foot for tubs, buckets or a bench; a spike for ponds, planters and gravel; a rim clamp for a tank edge. The node rides above the splash, the antenna in a plastic crown high above the water.

**Form.**
- **Bud dia 44 x 80** (about 76 at the sketch values): a cylinder with a domed crown. Cartridge boards stand upright, USB / SMA end down, battery behind. Diameter = sqrt((board width + 1)^2 + (Ds + battery + 2)^2) = about 37 plus walls, so 44.
- A **tube channel** (ID 20.5, OD 26) runs up the back of the lower 58 mm of the bud, stopping 25 mm below the antenna zone, so the tube slides in from the bottom and a nylon thumbscrew locks the height. The channel merges into the bud wall.
- Foot disc: SMA at the centre, USB-C 9.6 mm in front, four screws and a face o-ring (stock 38 x 2) in a circular groove. The tube channel is behind both, so the boot hangs beside the tube.
- Parting lines: the foot cap with a round o-ring, and the crown cap bonded on (no screws within 15 mm of AE1).
- Tube 300-600 mm of 20 mm PVC or PP conduit (stock). Overall height 400-700 mm.

**CMF.** Abyss PCTG bud and crown, matte (textured plate on the cap faces); graphite TPU boot and collets; coral key and eye; the type band wraps the foot (amber for ORP in the sketch); pale grey tube. Foot in Abyss PCTG, filled with sand and sealed. Outdoors, Sand ASA for the bud.

**Interaction.**
- Install: push the tube into the base, slide the bud on and lock it, clip the Collet at the chosen depth, plug the probe into the boot port, wrap the spare cable round the tube (4-6 turns, TPU rings), press the key to pair.
- Calibrate: lift the whole staff out, or unclip the Collet and slide the probe out. The cable stays plugged.
- Key and eye on the front, under the crown. USB-C bung on the foot.
- Probe storage cap on a peg on the foot base.
- Battery: foot cap, 4 screws, the cartridge drops out downward with the jack and USB tunnel on the cap.

**Sealing and environment.**
- Shell target IP66. The only joint is the round foot cap (o-ring 38 x 2), with a vent and silica. The tube channel is open at the bottom; it is outside the electronics (a blind bore with its own wall), so no seal depends on it.
- The bud rides at least 60 mm above the water (antenna 25 mm minimum). The tube is in the splash zone, so use plastic, not metal, and set a drip edge under the bud.
- A pond or outdoor bud needs UV-stable ASA.

**Build.**
- Bud tube printed standing up, open at both ends (about 2.5-3 h), crown cap dome-up (0.7 h), foot cap sealing-face down (0.8 h), sled (1.5 h), Collets and clips (1 h), one base (foot 2 h, spike 0.8 h, clamp 1 h). **About 9 h with one base. Difficulty: easy to moderate.**
- Printed bridges are short: the channel and the thumbscrew boss are vertical features. The foot ballast is a hollow print that you fill.
- Risks: a tall staff in a tub can tip (needs a wide ballast foot or a clamp); cable and tube in the splash zone catch salt; the bud's size is parametric on the battery.

**PCB:** none. P1 (SMA barrel length) applies.
**Scores:** Looks 4 | Setting 4 | Print / seal 4 | PCB 5 | **17**

**Fusion would model:** bud (dia 44 x 80, channel ID 20.5, foot groove for o-ring 38 x 2, crown cap, key and eye pockets, SW1 plunger), foot cap (SMA hole 6.8, USB tunnel 12.5 x 7, 4 screws, jack cradle), boot, Collet (bore parameter), tube clips, bases A, B, C, probe cap, type band.

### Concept 2: PERCH (01-perch.svg)

**Idea.** The node straddles the rim like a bird on a branch. The electronics sit outside and dry on a Tidemark-style column; a saddle hooks over the wall; and its inner leg carries the probe, held rigid and vertical in a split TPU collet. One gesture to install, and the probe depth is set by sliding it in the collet.

**Form.**
- **Tidemark-P column 32 W x 33.5 D x 70 H** at the sketch values (width = max(23.9, battery width + 2) + 5; depth = 5 + Ds + 1 + battery + 1; height 63 plus the foot). Boards upright, USB / SMA end down, brow on top (the top 20 mm leaning back 20 degrees) over AE1.
- **Saddle:** planar profile 24 wide: back plate 3 mm, bridge 9 mm, inner leg 8 x 75 mm (40-100 variants). The column slides down the family dovetail rail on the back plate. A nylon thumbscrew with a TPU pad grips rims of 6-19 mm (shims).
- **Collet block** on the inner leg: the probe is 26 mm off the wall, tip at least 20 mm off any wall or floor.
- Foot: SMA boot and USB bung; the cable runs up the back plate groove in two snap clips and over the bridge to the probe top.
- Overall depth to the probe axis about 110 mm; the probe tip is about 190 mm below the rim top.

**CMF.** Abyss PETG column, Abyss PCTG saddle and leg (tough, wet), graphite TPU boot, pad and collet, coral key and eye, type band at the toe (amber = ORP in the sketch).

**Interaction.**
- Hang it on the rim, tighten the thumbscrew, slide the probe to depth, clip the cable, drip loop.
- Lift the probe out of the collet to calibrate; the storage cap (on a peg on the back plate) keeps pH and ORP wet.
- Battery and USB-C: foot cap, 4 screws, the cartridge slides out downward.

**Sealing and environment.**
- Column IP66 target, one face o-ring, vent, silica. The electronics are on the dry side of the wall (best case for a cabinet sump).
- The inner leg, collet and probe stand in splash and are all plastic. The plug is under the boot, facing down, with a drip loop.

**Build.** Column sleeve roof-down (the brow is a 20 degree lean, no supports) about 4 h, foot cap 1.2 h, sled 1.5 h, saddle and leg printed on their side (layers along the hook, no supports) 2.5 h, Collet and parts 1 h. **About 10 h. Difficulty: moderate.**

**Risks.** Needs a free rim with no lid or hood over it, and a tank at least 200 mm deep for a 150 mm probe. The 140 g column hangs outboard and puts a torque on the rim: a TPU heel pad on the back plate presses the outer face, and it needs a test on an acrylic rim. A sump in a tight cabinet may not fit a 32 mm column on the outer face. The probe is rigid, so waves can knock it against the wall at shallow depth.

**PCB:** none (P1 applies).
**Scores:** Looks 4 | Setting 4 | Print / seal 4 | PCB 5 | **17**

**Fusion would model:** Tidemark-P column (sleeve, brow, foot cap with SMA hole and USB tunnel, cartridge, key and eye), saddle with rail, leg and collet block, shims, thumbscrew pad, Collet, probe cap, type band, boot.

### Concept 3: LIMPET (03-limpet.svg)

**Idea.** A low shell clings to a bucket lid like a limpet to a rock. The probe passes through the lid beside it in a TPU bushing; the shell's tail is a ring around that hole, so shell and probe are one fixed unit. The spare cable wraps round two horns on the flank. No arm, no clamp, no wall: the lid is the mount.

**Form.**
- **Head about 131 L x 38 W x 34 H** on three TPU feet (3 mm). Boards lie flat, the battery under them, the antenna at the far end under a 20 degree brow.
- The probe end is a **tail with a raised eye ring** (dia 30 x 24) whose coral lip is the family accent. The probe passes through the ring and a **double-flange TPU bushing** in a dia 25 lid hole; a Collet grips the body. The plug trough between the eye ring and the head holds the SMA boot.
- The end plate faces the trough and carries the SMA hole, the USB-C tunnel (above the SMA in this orientation, 9.6 mm higher) and the face o-ring.
- Two cleat horns on the flank take the spare cable. They are on the SMA half, because a coax shield close to the chip antenna could detune it.

**CMF.** Abyss PETG head, coral TPU key on the roof, coral translucent eye, graphite TPU boot, bushing, feet and horns, coral lip on the eye ring, type band on the end plate, lowercase code on the roof.

**Interaction.**
- Cut the lid hole with a hole saw using a printed template, press the bushing in, drop the probe through and set depth with the Collet, set the head down, plug in and wrap the spare cable round the horns.
- Calibrate: lift the probe up through the bushing; the head stays. A storage cap parks on the horns.
- Battery and USB: lift the head, remove the end plate (4 screws), the cartridge slides out toward the trough with the jack and USB tunnel on the plate.

**Sealing and environment.**
- Shell IP66 target: one rounded-rectangle face o-ring on the end plate, vent, silica. The head sits on the lid, so it is above the splash and condensation.
- The bushing is the only path from the vessel air to the lid top. The eye lip and a drip groove keep condensation off the head. Lid underside to highest water at least 25 mm.

**Build.** Head shell roof-down (brow as a 20 degree lean, no supports) about 4 h, end plate 1 h, sled 1.5 h, TPU bushing 0.7 h (tolerance test needed), Collet, drill template, cleat and cap 1.5 h. **About 9 h. Difficulty: moderate.**

**Risks.** Needs a plastic lid 1-5 mm that stays on and a hole at least 25 mm from the wall. It does not suit an open tank or sump. A 131 mm head on a thin lid can rock. The probe rides on one bushing, so a pulled cable can lever the head (the cleat takes the pull). The cartridge slides in under the key plunger, so SW1 must be the tallest part along the slide path.

**PCB:** none (P1 applies).
**Scores:** Looks 4 | Setting 3 | Print / seal 4 | PCB 5 | **16**

**Fusion would model:** head (131 x 38 x 34, brow, eye ring and tail, trough, cleat horns, feet), end plate (SMA hole, USB tunnel, o-ring groove), bushing (flange dia 40, bore 11.5 or 16), Collet, drill template, probe cap, boot.

### Concept 4: BERTH (02-berth.svg)

**Idea.** A wall monolith. The node column sits on the shoulder of a tall tower; the tower has a parking bay (a soaker cup) for the probe, a post for the slack cable and, in service, the probe lives in the tank on a remote Hold. The Berth is where it rests, is cleaned and is calibrated. Several of them tile on one rail (Berth Row), with one probe rack below for all.

**Form.**
- **62 W x 36 D x 190 H** overall: the node column (32 wide, same cartridge as Perch) and a 28 wide tower beside it on a cleat plate (80 x 195 x 5, keyholes at 60 mm or VHB).
- Tower: an upper TPU clamp, a soaker cup (TPU insert, about 25 ml) with a drip tray, and a cable post for 4-6 turns of spare cable. The probe stands 18 mm clear of the plate.
- Remote Holds, each with the same collet: A rim hold (a mini saddle), B glass hold (suction or VHB), C pipe clamp.

**CMF.** Abyss PETG node and tower, PCTG Holds, graphite TPU cup, clamp, boot and collets, coral key and eye, type band at the node foot.

**Interaction.** Mount the plate, hang the node on the rail, place the Hold in the tank, run the cable (1 m, or an SMA extension). To calibrate, lift the probe from its Hold and rest it in the bay, rinse, calibrate, return it. Battery: foot cap, cartridge slides out downward.

**Sealing and environment.** The node is the same IP66 column; the tower is not sealed (no electronics). The cup holds liquid: use a sponge or a lid, as it spills when the wall is knocked. Never use RO water in a pH or ORP cup.

**Build.** Node 6.5 h, tower and plate about 6 h (190 mm tall standing, or on its back), three Holds 1.5 h each, TPU parts 1 h. **About 18 h. Difficulty: moderate.**

**Risks.** The tallest and most complex option, two-part (the wall unit plus one Hold per probe), and it needs a wall or cabinet panel within reach of the 1 m cable (an SMA extension for further). It earns its place only if the probes are pulled out for calibration often. The antenna sits in the brow at the top of the unit, as high as the cabinet allows, 15 mm clear of metal fittings.

**PCB:** none (P1 applies).
**Scores:** Looks 4 | Setting 3 | Print / seal 3 | PCB 5 | **15**

**Fusion would model:** cleat plate and rail, node column (as Perch), tower with clamp, cup, drip tray and cable post, the three Holds, probe cap.

### What changed in the two kept concepts

- **Perch (01):** the sketch was an ORP example in amber instead of pH; added the two cable snap clips, the storage cap on the back plate, the IP target and the EC electrode warning; kept the geometry.
- **Berth (02):** added the Berth Row (shared rail for all nodes), honest limits, the RO-water warning from Bluelab; kept the geometry. Both now say the probe sizes are unconfirmed.
- **00 reference:** corrected "BNC only with an adapter" to the Atlas finding (SMA standard), marked the probe sizes as unconfirmed, flagged the barrel-length discrepancy (P1), added the EC live-shell note and the type colour key.

---

## 5. Family direction: "Brow, Tide line, Service foot, the Eye and now the Collet"

How the probe nodes sit next to the rest (see `05-family.svg`):
- **Perch** pairs with **Tidemark** and **Plumb**: the same column, brow, dovetail rail and foot, with a saddle as the back plate.
- **Staff** pairs with the **Bead pod** (the same 44 mm round) and **Davit** (the same stock 20 mm tube).
- **Limpet** pairs with **Slate** and **Cork**: a low spine, boards flat, the antenna at the outer edge, a brow, and a TPU-bushed lid hole.
- **Berth** pairs with the **Ledger gateway** (a wall object) and could hold the water-level column on the same rail.
- **Lily** has no probe sibling: a floating hull cannot hold a probe rigid.

Common rules for the probe line:
1. The antenna is in a plastic-only brow or crown.
2. One coral key and one coral eye on the electronics; the type band is the only other colour.
3. All ports leave from one graphite foot or end plate that faces down.
4. One cartridge, one boot, one Collet, one type band system across pH, ORP, DO, EC and level.
5. Abyss PETG/PCTG with graphite TPU. No panel on these nodes, so no Sand ASA except outdoors.
6. The same dovetail rail and cleat for mounting.

---

## 6. PCB and electronics requests (none required for the enclosure; for kicad-designer to judge)

| ID | Options | Request | Why |
| --- | --- | --- | --- |
| P1 | All | Confirm from the BAT Wireless BWSMA-KWE-Z001 drawing (LCSC C496551) how far the barrel and its threaded tip stick out past the x = 90 board edge. The ORP STATUS says 5.6 mm, the DO and EC statuses say 7.6 mm for the same footprint. If it is 5.6, move J1 about 1.5 mm toward the edge (or accept a wall recess) so that at least 7 mm protrudes | The foot needs wall 2.5 + 0.5 + about 4 mm of thread. At 5.6 mm the plug will not thread on |
| P2 | All | Add 3D bodies for J1 (jack) and U2 (OEM) to the STEP: jack height (6.5-8 mm so far), flange, barrel start. U2 height about 2.65-3.1 mm | The gap and the cradle are drawn from STATUS estimates; fusion-enclosure needs the real envelope |
| P3 | All (stacked), optional | R1 from the feather concepts: keep the far corner of the sensor board under AE1 free of copper | The sensor board's ground plane sits about 10 mm under the chip antenna. Still open from the feather study |
| P4 | None | LED, button, antenna and board outline are fine | Nothing to change |

Open electronics questions that touch the enclosure (not repeated from the STATUS files): the 3.0 V isolated rail margin on all three boards (EC draws up to 26 mA); the R_ID values (no SENSORS.md); the INT poll-only choice. They do not change the mechanics.

---

## 7. Mechanical numbers fusion-enclosure still needs

1. **Probes:** body diameter, length, cable O.D., plug length and nut size, and whether the cable gland is larger than the body. Measure the actual ORP, DO and EC K1.0 probes; confirm the DO SKU.
2. **Jack:** BWSMA-KWE-Z001 drawing (barrel length past the edge, flange size, height) and the mated plug length (assumed about 15-20 mm).
3. **Stack:** gap and Hs, tallest part height, FFC length (same open items as the other studies), SW1 as the tallest part from fx 26.
4. **Battery:** model and size (EC may want more than 40 x 25 x 7), with NTC if any.
5. **Container:** type, inside depth and width, wall or lid material and thickness, rim shape, whether the lid must close, where each probe goes, water level.
6. **Mount site:** a wall or cabinet within 1 m, a tub or bucket for Staff, a lid for Limpet.
7. **Printer:** TPU 95A and PCTG on hand, a hole saw (dia 25) for Limpet, hose clamp range, 20 mm PVC/PP tube.

---

## 8. Questions for Brian

1. **Which containers will these probes live in?** Sump, tank, tub, bucket, pond, or a mix? Open rim or lid? This picks Perch, Limpet, Staff or Berth.
2. **Staff: bud or column?** One shell for the whole line (the Tidemark-P column on the tube through the rail) or the round bud for the pole-mounted look?
3. **Can you measure the three probes** (diameter, length, cable O.D., plug length) or send a photo with a ruler, and confirm the DO SKU?
4. **Storage and calibration:** do you pull probes out for calibration often (Berth earns its keep), or leave them in the tank for months? What does Atlas say for storing DO and EC probes (not confirmed)?
5. **Seal level:** is IP66 splash-proof enough, or must the node survive being dropped in (IP67)? I will only claim a rating after a dunk test.
6. **Colour code:** are four band colours (green, amber, aqua, violet) acceptable beside the single coral accent, with the debossed code and raised dots as the non-colour cue? Or one colour with the code only?
7. **Mounting:** is there a wall or cabinet within 1 m of each container? Can you screw into it or only stick (VHB)? Is a printed drill template for a lid hole OK?
8. **Battery and life:** target weeks or months? EC draws up to 26 mA while measuring, so this sets the cell size and the column width or bud diameter.
9. **Outdoor use?** If any node goes to a pond, the bud and column switch to Sand ASA and need the U1 top cover.
10. **Printing:** do you have TPU 95A, PCTG and nylon M2.5/M3 screws? OK to co-print TPU keys and bands with the U1's second toolhead?
11. **Correct the EC STATUS?** It says Atlas EC probes ship with BNC; the Atlas page says SMA standard. This removes a question from that board.
12. **P1:** can kicad-designer check the SMA barrel length (5.6 vs 7.6 mm) before fab?
