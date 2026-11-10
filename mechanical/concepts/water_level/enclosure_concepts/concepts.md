# Feather water-level node (nRF54L15 feather + sensor board + A02YYUW ultrasonic probe): enclosure concepts (2026-10-25)

Concepts only, no CAD. Brian picks one, then fusion-enclosure blocks it out in Fusion.
Visual page: `index.html` (this folder). Sketches: `00-cone-and-clearances.svg`, `01-plumb.svg`, `02-cork.svg`, `03-davit.svg`, `04-bead.svg`, `05-family.svg`.
This folder is not in git.

## Summary and recommendation

| # | Name | One-line idea | Looks | Setting | Print / seal | PCB change (5 = none) | Total |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | **Bead** | The transducer lives alone in a small pod on a cable; the electronics stay dry in a Tidemark on the wall. The pod has four interchangeable bases (lid, rim saddle, pipe clamp, suction cup) | 5 | 5 | 4 | 5 | **19** |
| 2 | **Davit** | A Tidemark column on a cabinet wall with a swing arm of stock 20 mm conduit reaching over an open tank; the Eye sits on the tube end | 4 | 4 | 4 | 5 | **17** |
| 3 | **Plumb** | A Tidemark column hangs on the dry side of the wall; one hook carries a 100 mm boom over the rim to the transducer | 4 | 4 | 3 | 5 | **16** |
| 4 | **Cork** | A low pebble sits on a plastic lid and the transducer pushes through a hole in a TPU bushing, like a stopper | 4 | 3 | 4 | 5 | **16** |

**Recommendation.**
- **Build Bead as the system, and treat Davit as its open-tank base.** Both use the same two parts: **Tidemark-W** (the electronics column) and the **Eye** (the transducer holder). The container decides only the base: lid ring, rim saddle, pipe clamp, suction cup, or the Davit arm.
- Bead is the only option that keeps the electronics out of the humid tank air, keeps the transducer's sound path clean (no column or hook near the cone), and works with every container Brian listed.
- Plumb and Cork are good if Brian settles on one container type (a sump rim for Plumb, a plastic lid for Cork) and wants a single compact object. Cork is the smallest footprint but needs a hole in the lid.
- None needs a PCB change to be built. Two electronics issues need Brian's attention, though (W1 below): the probe's supply range and its standby current.

Three facts shape all four:
1. **The old Tidemark cannot hold this probe.** It hangs the probe by the wall, so the glass would sit 20-40 mm off the axis, well inside the 60 degree cone (see `00-cone-and-clearances.svg`). Every option here moves the transducer inboard of any wall.
2. **There is no solar panel on this node.** Sand ASA, PC windows and the panel "leaf" drop out. The bodies are smaller, and Abyss PETG/PCTG is right for all of them.
3. **The probe is unmeasured.** I could not find its body size, thread or cable length (details in section 1). Every holder is parametric on the probe diameter Dp and length Lp. The sketches assume Dp = 20 and Lp = 26 mm. Please measure the real part (or send a photo with a ruler) before fusion-enclosure starts.

---

## 1. Brief

**What it does.** A battery node (1S LiPo) that measures water level by ultrasound. The nRF54L15 feather and a sensor board (same 50.8 x 22.86 outline and holes) are stacked and joined by the FFC fold at the far end. A DFRobot A02YYUW (SEN0311) sealed transducer on a cable plugs into the sensor board's connector on the short edge opposite the FFC, which is the USB end.

**What I confirmed about the probe** (DFRobot wiki and product page):

| Item | Value |
| --- | --- |
| Type | Closed, separated, waterproof probe (IP67), 40 kHz +/- 1 kHz |
| Range / blind zone / angle | 3-450 cm, 3 cm blind, 60 degree reference angle |
| Interface | UART 9600 baud, 4 pins VCC / GND / RX / TX, PH2.0-4P connector on the shipping list |
| Supply | 3.3-5 V, standby up to 5 mA, average up to 8 mA (one reseller lists standby as under 5 uA; the DFRobot figure is the one to trust until measured) |
| Temperature | -15 to 60 C operating |
| DFRobot's own advice | Leave at least 3 cm between the sensor and the highest water level |

**What I could not find:** probe diameter and length, cable length, any thread or flange, the electronics-box size if there is one. The wiki has only a pinout picture, and the product listings carry a "dimension diagram" as an image I could not read. The one dimension I found, 84.6 x 29.6 x 18.5 mm, is a retailer's figure for the whole module and I don't know which part it describes. So the probe size is a **parameter** (Dp, Lp, cable O.D. about 4-5 mm assumed) and the first question for Brian.

**Where it lives.** Reef or aquarium room: a sump, an RO or top-off reservoir, perhaps a tank. Indoor, humid, salt splash and creep, condensation under lids. Brian has not fixed the container, so the four options cover different containers.

**Who handles it.** Brian. Installed once; the battery (or USB charge) is rare, and the probe may be swapped.

**Acoustic rules (all options; the drawing is `00-cone-and-clearances.svg`):**
- The face is at least **70 mm** above the highest water (30 mm blind zone plus a 40 mm margin for waves, foam, a fill overshoot and condensation).
- The axis is plumb to within about 2 degrees, so every mount has a bubble level or a flat reference.
- Nothing but air in the cone: no arm, screw, pipe or lip. The exit chamfer is 45 degrees, steeper than the 30 degree half-angle.
- A wall at lateral distance x enters the cone at a depth of x / tan 30 (1.73 x). Taking x as at least 0.58 x the distance d to the lowest water keeps the walls out of the cone completely. Less than that works only if the wall echo is weaker than the water echo, so test at the lowest level.
- Never recess the face in a nozzle or tube (the lip causes false echoes).
- Keep fill pipes, return flow, skimmer foam and bubbles out of the cone.

**Electronics constraints (from the template STATUS.md and the feather concepts):**

| Item | Fact |
| --- | --- |
| Stack | Main board and sensor board, 50.8 x 22.86 x 1.6, holes 2.7 mm at 2.54 / 48.26 and 2.54 / 20.32. Hs (standoff) sketch value 8 mm, Tm (tallest main part + 0.5) 7.0 mm, FFC loop F about 6.3 mm. Stack depth Ds = 18.2 mm |
| Probe connector | On the sensor board's x = 90 short edge (USB end). Connector type not yet chosen (PH2.0 4-pin assumed) |
| USB-C | Feather J1 at the same end. So in an upright column, the foot carries both the USB-C bung and the probe cable, 9.6 mm apart in depth |
| Key and LED | SW1 (B3U, top-actuated) and LED1 (590 nm yellow) as in the feather concepts |
| Antenna | AE1 at the far end. Plastic only within 15 mm; at least 10 mm from the battery; at least 25 mm from water |
| Battery | Sketch cell 40 x 25 x 7 (size class only). A larger cell, 50 x 34 x 10, is a parameter (Tidemark-W grows to 41 wide) |
| Build | FDM on the Snapmaker U1: PETG body, PCTG for tough or clear parts, TPU 95A for seals, grommets, pads and keys. Walls at least 2 mm, 0.5 mm clearance, M2.5 heat-set inserts, off-the-shelf o-rings |

**Electronics issues to raise (not enclosure changes; for kicad-designer and Brian):**
- **W1.** The A02YYUW is rated 3.3-5 V, but the sensor template's VSENS is about 3.0 V. Also, a standby current of up to 5 mA would flatten a 500 mAh cell in about 4 days (5 mA x 24 h = 120 mAh/day), so the probe must be power-gated (a load switch fed from VBAT or a boost) and switched on only to measure. The battery size follows from this and sets the Tidemark-W width.
- **W2.** The ultrasonic probe is not electrically in the water, so the non-isolated strip-down of the template may be enough. That is kicad-designer's call.

---

## 2. References (each looked up)

| Reference | Link | What it teaches here |
| --- | --- | --- |
| DFRobot A02YYUW wiki and product page | https://wiki.dfrobot.com/_A02YYUW_Waterproof_Ultrasonic_Sensor_SKU_SEN0311 , https://www.dfrobot.com/product-1935.html | The specs above; "leave at least 3 cm" above the highest water; PH2.0-4P. No mechanical drawing in the text, so the probe size is open |
| MaxBotix, what affects tank sensor accuracy (read via search summary; the page itself returned an error when I tried to open it) | https://maxbotix.com/blogs/blog/what-affects-ultrasonic-tank-sensor-accuracy | Mount flush and perpendicular to the liquid, keep away from walls and internal structures, don't recess the face, brackets and fittings in the beam make echoes. Basis of the cone rules |
| ncd.io ultrasonic tank-level installation guide (search summary) | https://ncd.io/blog/ultrasonic-long-range-wireless-tank-level-sensor-installation-guide/ | "Never recess the probe into a nozzle: the lip makes false echoes"; offset from the centreline to avoid fill pipes. Why the Eye is flush, with a 45 degree chamfer |
| APG ultrasonic level installation checklist (search summary) | https://apgsensors.com/ultrasonic-level-sensor-installation-checklist/ | Stilling pipes with a vent hole inside the blanking distance where a clear path is hard; keep the pipe vertical. The optional waveguide for narrow, deep containers |
| Milesight EM400-MUD installation (search summary) | https://www.milesight.com/products/docs/en/em400-mud-lora/steps/em400/installation.html | A commercial LoRa ultrasonic sensor: at least 30 cm from side walls and mounted from below a container cover with two screws through drilled holes. Supports Cork. Its sister EM500-UDL manual says not to mount at the centre of an arched or round top (multiple echoes) and not above the inlet |
| Neptune OS-1 / OS-1-M optical level sensor | https://www.bulkreefsupply.com/os-1m-optical-level-sensor-with-mount-neptune-systems-ob-a.html | The reef norm: a small sensor body through a drilled hole (5/8 in bit) or a magnetic mount for walls to 1/4 in. A top-off reservoir is already drilled for sensors, so a hole in a lid is no shock to this user |
| Crystal Water Monitor review | https://www.residentialsystems.com/technology/product-reviews/review-crystal-water-monitor-smart-pool-and-hot-tub-sensor | Electronics on the deck, probe on a cable with a locking connector, a mounting plate plus a pole adapter. The case for Bead and Davit |
| Bluelab Guardian monitor | https://support.bluelab.com/bluelab-guardian-monitor | A wall-mount monitor close to the reservoir, with a separate probe holder as an accessory |
| Seneye mag holder | https://aquanerd.com/2017/07/the-seneye-reef-monitor-mag-mount.html | Reef sensors mount on glass by suction or magnet. The pod's suction base (D) |
| RuuviTag spec | https://f.ruuvi.com/uploads/default/original/1X/2850eb7fa06ed66231eeba5bfa1e6014e5476692.pdf | The seal-plus-ePTFE-vent recipe reused for the column |
| icotek split cable glands | https://www.icotek.com/en/products/cable-glands | A cable that already has its plug gets a split seal. The cable wedge in the foot |
| Feather concepts and Ledger gateway notes | `C:\Personal-Agents\shared\design\nrf54l15_feather\enclosure_concepts\` , `C:\Personal-Agents\shared\design\pouch_gateway\enclosure_ledger\NOTES.md` | Family language: brow, coral key and eye, graphite foot, Abyss; cartridge; Ledger's brow overhang warning |
| Snapmaker U1 review | https://www.tomshardware.com/3d-printing/snapmaker-u1-review | 4 toolheads, TPU co-printing. TPU 95A prints in this workshop on the second toolhead |

I did not find a reachable design-studio case study for ultrasonic level nodes in this session. The comparison above is with commercial sensors, reef gear and the studio's own family.

---

## 3. Shared engineering (all options)

**Tidemark-W (the column).** Tidemark without the SMA heel, because the probe cable plugs in at the USB end.
- Size: 32 W x 64 H x 32 D with the sketch battery. Width = max(23.9, B_W + 2) + 5; height = 2.5 + F + 51.3 + 3 = 63.1, rounded to 64; depth = 5 + Ds + 1 + B_T + 1 = 32.2.
- Boards upright, USB end down, parts facing the front; sensor board behind; battery behind that. Brow on top over AE1 (top 20 mm leaning back 20 degrees).
- **Foot** (graphite TPU or a sealed cap with a face o-ring, 4 M2.5 inserts, more than 50 mm from AE1) carries two openings: the USB-C tunnel (12.5 x 7 mm, TPU bung) and a probe-cable slot (about 12 x 7.5 mm, sized after the PH plug is chosen). Their centres are 9.6 mm apart in depth, which leaves a wall of about 2.4 mm. Tight but printable. The slot takes a **split TPU wedge seal** around the cable (the plug passes through first, the two TPU halves then close round the cable, and a printed clamp pushes them home).
- ePTFE vent on the rear face, 2 g silica gel, conformal coat on both boards (mask AE1, connectors and SW1).
- Print as in Tidemark: sleeve roof-down (the brow is a 20 degree lean, no supports), foot cap sealing-face down. About 3.5 h sleeve + 1 h cap + 1.5 h sled = 6 h.
- Check carried over from Tidemark: SW1 (1.6 mm) must be the tallest part between fx 26 and the far edge, or the cartridge can't slide under the key plunger (then use the front-plate variant).

**Eye (the transducer holder).** One model in all four options, with the bore as a parameter.
- Graphite TPU 95A sleeve, 4 mm wall, bore = Dp - 0.5 (it stretches onto the probe). Outer collar about Dp + 10 (30 mm at Dp = 20), PETG/PCTG, holding the sleeve with a rear cap and three nylon M3 screws.
- The probe face is proud by 1.5 mm. The collar's bottom edge has a 45 degree outward chamfer so no part of it is in the cone. A coral lip ring (1 mm, TPU or PETG) marks the Eye, matching the family's single coral accent.
- Nothing covers the face: no film, no coating. It is IP67 itself, so the aim is to keep drops and salt off, not to protect it.
- Face down means condensate either falls or hangs as a drop on the face. The lip is a drip edge. Firmware should median-filter and drop out-of-range jumps (note for firmware, not for the enclosure).

**Condensation and salt creep (the electronics).**
- The electronics sit in one closed shell with as few paths from tank air as possible: face o-ring, cable wedge, USB bung, nothing else. Bead and Davit also keep the shell off the water altogether.
- Salt climbs along surfaces by capillary action. Every path from a wet surface to the shell gets a drip edge and a 1.5 mm deep "salt break" groove, and the cable has a drip loop on both sides.
- Brass inserts are fine inside the dry shell. Wet-side hardware (hook thumbscrews, clamps, clamp screws) is stainless or nylon.

**Cable.** The shipped cable length is unknown. Where the probe sits next to the electronics (Cork) the cable must be shortened and re-terminated with a PH2.0 crimp. Where it is far (Bead, Davit, Plumb) any excess is coiled in a keeper on the back of the column. The cable exits all go through the slot in the foot. An option for runs over about 2.5 m or for a swappable probe: an M8 4-pin A-coded panel connector (IP67) in place of the slot. UART at 9600 baud on a longer twisted cable should work, but I haven't verified it for this probe.

**Materials.** PETG is fine for dry-side parts. **PCTG** for parts in the humid zone or under load (hook, boom, pod, clips): tougher than PETG and more chemical-resistant. TPU 95A for seals, sleeves, pads, bungs and the key. Clear PCTG for the light pipe. No ASA or UV material is needed (indoors). Antenna rule as before: no carbon-filled or metal-filled filament within 15 mm of AE1, and check range if using a black.

**IP figures** are design targets. Claim them only after a dunk test (30 min at 15 cm with a dry tissue inside). The pod and the Eye sleeve face the water directly, so test them first.

---

## 4. Concepts

### Concept 1: BEAD (04-bead.svg) - recommended

**Idea.** Split the product at the cable. The pod holds only the transducer, so it can sit exactly where the sound path is cleanest, with nothing near the cone. The Tidemark-W column stays on a cabinet wall or a shelf, dry, with the antenna high. The pod's four bases cover the containers: a lid, a rim, a pipe, or a flat glass lid.

**Form.**
- **Pod: dia 44 x 38 high**, a pebble with a flat bottom. The Eye (30 mm collar) sits in the bottom; the probe face is proud by 1.5 mm; the coral lip is the only accent. A TPU strain relief on top, with a bubble vial (a printed vial window and a small steel ball, or a stick-on level) so the axis can be set plumb.
- Parting line: horizontal at 40 % of the height (an o-ring cord in a groove), screws from the top cap. Three bayonet lugs on the collar, identical on every base.
- **Tidemark-W** as in section 3: 32 x 64 x 32, on the family cleat or a rim clip.
- Bases:
  - **A. Lid.** A ring sits on top of the lid over a dia 30 hole (printed drill template); the pod's stem passes up through the hole and twists into the ring. Lid 1-5 mm. A TPU gasket sits under the ring.
  - **B. Rim saddle.** The Plumb saddle, but with a 60 mm boom, for sumps with a rim.
  - **C. Pipe or post clamp.** A hose-clamp collar on a 20-60 mm pipe with an arm 40 mm long.
  - **D. Suction cup / VHB plate.** For the underside of a flat glass or acrylic lid.

**CMF.**
- Pod: Abyss PCTG, graphite TPU sleeve, coral lip. Bases in Abyss PCTG with TPU pads.
- Column: Abyss PETG, coral TPU key, coral translucent eye (clear PCTG pipe), graphite foot.
- Family: the pod looks like the gateway's coral key turned into an eye.

**Interaction.**
- Install: fix the column (screws or a rim clip), choose a base, place the pod, set the bubble, route the cable with clips, press the button to pair.
- Sensor swap: twist the pod out, pull the probe out of the sleeve (undo the rear cap), fit the new one. The cable stays.
- Battery/USB: USB-C at the foot of the column, within reach (charge without moving anything). The column opens via the foot cap (4 screws), the cartridge slides out downward.
- Cable: out of the foot through the wedge seal, along the cabinet in clips, with a drip loop at each end.

**Sealing and environment.**
- The electronics never meet tank air. Column target IP66 (as Tidemark). The pod target IP67: the face o-ring plus the probe's own IP67, and the strain relief on top, facing up and away from drips.
- The sealed pod hangs in the humid air alone, which is the best place for the part that can take it.
- Drainage: the pod has no cavities that hold water; the lip is the drip edge.

**Build.**
- Pod: cup printed lip-down (the lip is the first layer), cap flat, TPU sleeve and strain relief. About 1.8 h.
- Bases: A about 0.6 h; B 1.5 h; C 0.8 h; D 0.5 h.
- Column: about 6 h.
- **Total about 9 h with one base. Difficulty: easy to moderate.**
- Risks: the drill template and the lid hole are Brian's work (A); the bayonet lugs need a tolerance test (one test print); long cables need a UART test.

**PCB:** none. Optional: a side-entry PH2.0 connector on the x = 90 edge (see section 6).
**Scores:** Looks 5 | Setting 5 | Print / seal 4 | PCB 5 | **19**

**Fusion would model:** pod (dia 44 x 38, cup + cap + o-ring groove 2.7 x 1.5, Eye collar 30 with sleeve bore Dp - 0.5, 45 degree chamfer, 3 bayonet lugs, strain relief, bubble vial pocket); the four bases; Tidemark-W (cartridge, foot with USB tunnel 12.5 x 7 and cable slot 12 x 7.5 plus wedge, brow, key, eye); the cleat.

### Concept 2: DAVIT (03-davit.svg)

**Idea.** A swing arm of stock tube carries the Eye out over an open tank from a Tidemark-W column fixed to the cabinet wall. Davit is Bead with a built-in base for the "wall plus open tank" case.

**Form.**
- Column 32 x 64 x 32 on the family cleat (a plate 90 x 50 x 6 with two screws, or 3M VHB on a smooth cabinet panel).
- **Swivel knuckle** (about 30 x 30 x 30) bolted under the foot, with a friction pivot (a TPU o-ring on a dia 10 pin) and three detents (0, 45, 90 degrees), so the arm can park along the wall.
- **Arm: 20 mm PVC electrical conduit**, 150-300 mm (220 mm shown), pushed into the knuckle and fixed with a set screw. A stock part, so no sag and no long print. The cable runs inside the tube.
- **Eye elbow cap** printed over the tube end (about 60 x 38 x 38), holding the Eye pointing down.
- The face sits 9 mm above the tank rim in the sketch. Highest water 73 mm below the face.

**CMF.** Abyss PETG column, Abyss PCTG knuckle and elbow, light grey PVC tube (or black tube for a quieter look), graphite TPU sleeve, coral lip.

**Interaction.**
- Install: screw the cleat, hang the column, push the tube into the knuckle, cut it to length, thread the cable, push on the elbow, set the bubble.
- Service: swing the arm away to reach the tank. Sensor swap: pull the elbow cap off the tube; the probe comes out of the sleeve.
- USB-C and the arm both leave from the foot.

**Sealing and environment.**
- The column is on the wall, away from splash. The arm is the only thing over the water, and a tube is easy to wipe. Both arm ends carry a drip edge so salt doesn't creep to the column.
- The tube is open at the Eye end only through the cable path: a TPU grommet in the elbow, where the cable goes in. The inside of the tube is a place for condensation to run to the lowest point: leave a 2 mm drain notch at the elbow underside (outside the cone).

**Build.** Column about 6 h, cleat 0.7 h, knuckle 1.5 h, elbow and Eye 1.2 h, parts 0.5 h. **About 10 h. Difficulty: moderate** (the swivel tolerance is the hard part).

**Risks.** The arm swings loose if the pivot is under-tuned; the cabinet wall must be within about 300 mm of the tank; a metal cabinet near the antenna is a problem (keep the antenna corner away from metal).

**PCB:** none.
**Scores:** Looks 4 | Setting 4 | Print / seal 4 | PCB 5 | **17**

**Fusion would model:** cleat (90 x 50 x 6, 2 screw holes), column, knuckle (pin dia 10, 3 detents, tube socket for dia 20, set screw), elbow cap (Eye collar 30, grommet, drain notch), tube (stock 20 mm OD, 220 mm), Eye.

### Concept 3: PLUMB (01-plumb.svg)

**Idea.** The wall is the dry line. The Tidemark-W column hangs on the **outside** face of the rim wall; a saddle hooks over the rim; and the bridge keeps going inboard as a 100 mm boom with the Eye at its tip. One piece of hardware, one gesture to install.

**Form.**
- Column 32 x 64 x 32, antenna in the brow at the top, outside the tank.
- **Saddle** (a planar profile extruded 18 mm wide): back plate 3 mm thick, bridge 9 mm thick, inner leg 40 mm tall. A thumbscrew through the inner leg with a TPU pad squeezes the wall (the rigid saddle pulls the back plate against the outer face). Rim thickness 6-19 mm by shims.
- **Boom: 100 mm** from the inner face to the transducer axis (variants 60 and 150). A cable groove under a snap-on cover, from the foot up the back plate and along the bridge. The Eye hangs below the tip.
- The face is 27 mm below the rim, so the rim-to-highest-water gap must be at least **100 mm** (a 40 mm riser block lifts the boom if not).
- The inboard wall is 100 mm off the axis, so it is clear of the cone down to 173 mm below the face.

**CMF.** Abyss PCTG saddle and boom (a tough hook), Abyss PETG column, TPU pad, coral lip, stainless or nylon thumbscrew.

**Interaction.** Hang it on the rim and tighten the thumbscrew; set the plumb with the shims; clip the cable. Charge at the foot (the foot is outside the tank, in the cabinet). Sensor swap: lift off the snap cover, pull the Eye. To reach the sump, lift the whole node off the rim.

**Sealing and environment.** Electronics are on the dry side (best case for a cabinet sump). The boom and Eye are over the open sump. The cable groove is not sealed: it ends at a grommet in the back plate, where the cable meets the column (drip loop, 1.5 mm salt break).

**Build.**
- Saddle and boom printed **on their side** (the profile lies on the bed, no supports; layers run along the hook, so it's strong). About 2.5 h.
- Column about 6 h; Eye 1 h; pad and screws 0.5 h. **About 10 h. Difficulty: moderate.**

**Risks.** The rim must be free of lids and hoods; the hanging weight puts a torque on the rim (column about 120 g outboard balances the boom, but test on an acrylic rim); the inner leg and boom stand in splash; a sump stands in a cabinet that may be too tight for a 32 mm column on the outer face.

**PCB:** none.
**Scores:** Looks 4 | Setting 4 | Print / seal 3 | PCB 5 | **16**

**Fusion would model:** column; saddle profile (plate 3 x 16, bridge 9 x 18, inner leg 40, boom 100, rim gap 6-19, thumbscrew M5 on the inner leg, TPU pad 4 x 22); cable groove and cover; shims; Eye; riser block.

### Concept 4: CORK (02-cork.svg)

**Idea.** A low pebble sits on a plastic lid and the transducer goes through a hole in a TPU bushing, like a stopper in a bottle. No arm and no hook; the lid is the mount. It is the smallest and the most self-contained option.

**Form.**
- **Head 104 x 38 x 32**, a flat-bottomed pebble that is Slate's spine without the wing. Boards lie flat, the battery is under them, the Eye is at the USB end, and the antenna is in a brow at the far end (the top 20 mm leaning back 20 degrees).
- **Eye bushing:** a double-flange TPU 95A bushing (flange dia 40) that snaps through a **dia 30 hole** in a lid 1-5 mm thick. The probe face is 8 mm below the lid underside. A printed drill template (a ring with a dia 30 hole and a pointer) marks the hole. Optional: a threaded stem and ring nut for thin or flexible lids.
- Three TPU feet under the head stop it rocking.
- USB-C tunnel runs over the transducer to a bung in the end face. The probe cable is a 40 mm hop to the sensor board connector: shorten and re-crimp.
- The lid-underside to highest-water gap must be at least **78 mm**, and the hole at least 0.58 x depth from the container wall (in a narrow, deep bucket this fails; use the optional waveguide tube or choose Bead).

**CMF.** Abyss PETG head, coral TPU key on top, coral eye (clear PCTG pipe), graphite TPU bushing and feet, coral lip on the Eye.

**Interaction.** Cut the hole with a hole saw using the template, snap the bushing in, set the head down, press the button to pair. Battery and SWD: lift the roof (4 screws); the cartridge drops in from above, so there is no slide-in constraint on SW1. Sensor swap: pull the probe out of the bushing from above.

**Sealing and environment.**
- The bushing is the only path from tank air to the head: it grips the probe body (inside) and the hole (outside). The head is a normal Tidemark-style closed shell with a roof o-ring and a vent.
- The lid underside is where condensation forms. The Eye's lip and chamfer shed it; a drip groove on the bushing keeps it off the head.

**Build.** Head shell roof-down (brow as a 20 degree lean, no supports) about 4 h; floor plate 1.5 h; sled 1.5 h; bushing (TPU) 0.7 h; template and feet 0.5 h. **About 8-9 h. Difficulty: moderate** (the TPU bushing needs a test or two).

**Risks.** Needs a hole in the lid and a lid that stays on; a rocking head on a thin lid; a narrow container fails the wall rule; the walls of the head and the lid are a long way from the water, so condensation drips may follow the bushing.

**PCB:** none.
**Scores:** Looks 4 | Setting 3 | Print / seal 4 | PCB 5 | **16**

**Fusion would model:** head (104 x 38 x 32, brow, USB tunnel, key and eye, roof o-ring groove), flat cartridge variant (boards flat, battery below), Eye bushing (flange dia 40, hole dia 30, probe bore Dp - 0.5, lid 1-5), drill template, feet.

---

## 5. Family direction: "Brow, Tide line, Service foot, and now the Eye"

How each option sits next to the feather concepts (see `05-family.svg`):
- **Plumb** pairs with **Tidemark**: the same column, brow, dovetail rail and foot, with the saddle as a new back plate.
- **Davit** pairs with **Tidemark** (the cleat) and with **Shard** (Shard's stake socket would allow a free-standing post for the arm where there is no wall).
- **Cork** pairs with **Slate**: a low spine with boards flat and the antenna at the outer edge, minus the wing and panel.
- **Bead** pairs with **Tidemark** and with the **Ledger gateway**. The gateway's single coral key and Bead's coral lip are the only two accents in a room of Abyss objects.
- **Lily** has no water-level sibling: a floating node can't hold the transducer still.

Common rules for the water-level line:
1. The antenna is in a plastic-only brow.
2. One coral key and one coral eye on the electronics; the Eye lip is the third and only accent at the water end.
3. All ports leave from one graphite foot that faces down.
4. One cartridge, one Eye, four holders.
5. Abyss PETG/PCTG with graphite TPU; no panel, so no Sand ASA.
6. The same dovetail rail and cleat for mounting.

---

## 6. PCB and electronics requests (none required for the enclosure; for kicad-designer to judge)

| ID | Options | Request | Why |
| --- | --- | --- | --- |
| W1 | All | Power the probe from a switched supply of 3.3 V or more (a load switch fed from VBAT or a boost), not the 3.0 V VSENS rail; switch it on only for a measurement | The probe is rated 3.3-5 V; DFRobot lists a standby up to 5 mA, which is 120 mAh a day if left on |
| W2 | All | Fit a side-entry PH2.0 4-pin (for example S4B-PH-K-S), pins in the order VCC / GND / RX / TX, centred on the x = 90 edge with the mouth flush at the edge | The cable then leaves straight out of the foot; a top-entry connector makes the foot taller |
| W3 | All, optional | Keep the connector within 5 mm of the board centre line | Keeps the cable slot clear of the USB tunnel and the standoff holes |
| W4 | Cork, optional | Place the connector so its latch faces away from the USB-C tunnel | The cable runs a 40 mm hop under the USB tunnel |

The antenna-corner keep-out and the plated H4 question in the template STATUS.md still apply; they are not repeated here.

---

## 7. Mechanical numbers fusion-enclosure still needs

1. **Probe:** Dp, Lp, face shape (flat or horn), cable O.D. and length, whether there is a flange, thread or a second box in the cable. Measure the real part.
2. **Connector:** the PH housing size (width x height) for the foot slot; side-entry or top-entry; the position on the sensor board.
3. **Stack:** Hs, sensor board part heights, FFC length (same open items as the feather concepts), and the battery model and size (400 mAh class or larger) once W1 is settled.
4. **Container:** type, inside depth, width, wall or lid thickness, rim shape (flat, lipped), whether the lid must close, the lowest and highest water levels.
5. **Mount site:** a cabinet wall within 300 mm for Davit and Bead? Wood, plastic or painted board for screws or VHB?
6. **Printer:** TPU 95A on hand, PCTG on hand, hole saw dia 30 (for Cork and base A), and a hose clamp range.

---

## 8. Questions for Brian

1. **What is the container?** Sump, RO or top-off reservoir, tank, or a mix? Give inside depth and width, wall and lid material and thickness, and whether the lid has to close. This picks the base (lid ring, rim saddle, pipe clamp, suction cup, or the Davit arm).
2. **Is the lid thin plastic that can take a dia 30 hole?** (Decides Cork and base A.) And is the lid held in place or often lifted?
3. **Mounting:** is there a cabinet wall or a post within about 300 mm of the container? Can you screw into it or only stick (VHB)?
4. **Highest and lowest water levels and the gap from the rim or lid to the highest level.** Needs at least 100 mm for Plumb, 78 mm for Cork, or 70 mm plus the base offset for Bead.
5. **Probe:** can you measure (or photograph with a ruler) the probe diameter, length and cable length, and say whether the cable is detachable? OK to cut the cable and re-crimp a PH2.0 plug where it is too long? Or fit an M8 connector?
6. **Battery life target:** weeks or months between charges? That sets the power gating (W1) and the cell size, which sets the column width.
7. **Looks:** is a separate small pod acceptable, or must it be one object? (Bead vs Plumb or Cork.)
8. **Printing:** do you have TPU 95A and PCTG on hand? OK with a printed drill template for lid holes?
9. **Which feather concept** (Tidemark, Slate, Shard) are you leaning towards? The water-level line follows it (Tidemark gives Plumb, Davit and Bead; Slate gives Cork).
