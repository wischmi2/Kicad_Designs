# Tidemark enclosure (first PETG draft): assembly guide

2026-11-01. From Fusion model `nrf54l15_feather_enclosure_tidemark` v11, hardware updated to the McMaster-Carr purchase list. All pictures in this folder were made from v11, with the bought hardware modelled in place. Colours: **gold = brass inserts, white = nylon standoffs and screws, steel grey = stainless screws, black = o-ring, pale blue = silica bag, light disc = vent patch.** The sled, sleeve and foot cap are shown in plain light grey so the hardware stands out. In each "before" picture the part floats about 15 mm from its seat, in line with it; the "fitted" picture shows it in place.

**Big picture:** the feather stands upright with its USB end down. The boards, sled and battery form one "cartridge". The sleeve is a cover, open at the bottom, that goes over the cartridge, and the foot cap screws on underneath to seal it. The rim clip on the back hangs the whole thing on the tank rim.

---

## 1. Parts list

### Printed parts (STLs in `..\print_draft_2026-10-29\`; the new sled and sleeve are in `..\print_draft_2026-10-29\new_2026-11-01\` until the old ones are moved)
Part letter D is not used any more: the printed board spacer was replaced by a purchased nylon standoff (see Hardware).

| # | Part | Qty | Picture | What it does |
| --- | --- | --- | --- | --- |
| A | Sleeve | 1 | part_A_sleeve.png | Main body: 4 walls, roof, sloped brow on the front, flared base (plinth) at the bottom, dovetail rail on the back. Key hole (7.4 mm) and LED "eye" hole (2.7 mm) on the front wall. Plinth insert holes 4.0 mm |
| B | Foot cap | 1 | part_B_footcap_top.png, part_B_footcap_bottom.png | Bottom lid. Top face: o-ring groove and 4 screw holes. Bottom: USB-C tunnel with a bung recess, the box-shaped "heel" with the SMA bulkhead hole, a 4.5 mm solar-cable hole and a 3.0 mm vent hole |
| C | Sled | 1 | part_C_sled.png (posts side), part_C_sled_battery_side.png | 2 mm plate. Front: 4 posts (8 mm OD, 4.0 mm insert holes) for the boards. Back: 2 rails and 2 ledges that hold the battery |
| E | Key | 1 | part_E_key.png | Push button cap. Its small plunger presses SW1 on the main board. The notch in the flange clears the light pipe |
| F | Light pipe | 1 | part_F_lightpipe.png (thin rod with collar, beside the key) | 2.5 mm rod that carries the LED1 light to the front. A clear 2.5 mm acrylic rod cut to 8.8 mm and glued in works better |
| G | Rim clip ("L piece") | 1 | part_G_rimclip.png | Hook that hangs on the tank rim (12 mm rim). The channel on its lower part slides onto the sleeve's back rail. **See the warning in step 13** |
| H | Leaf card | 1 | part_H_leafcard.png | Backing card for the LL200-2.4-75 solar panel (panel sits in the 1 mm pocket, the cable leaves through the notch). It is separate from the enclosure; only the solar cable runs to the node |
| I | USB bung (optional, fit check) | 1 | part_I_usb_bung.png | Plug that closes the USB-C tunnel in the foot cap. Real part will be TPU |
| J | SMA boot (optional, fit check) | 1 | part_J_sma_boot.png | Sleeve over the SMA bulkhead and probe plug under the heel. Real part will be TPU |
| K | Clip pads (optional, fit check) | 2 | part_K_clip_pad.png | 1.5 mm pads that go on the two inner faces of the clip hook so it grips the rim. Real part will be TPU |

**What each printed part looks like:**

| | |
| --- | --- |
| <img src="part_A_sleeve.png" width="280"><br>A Sleeve | <img src="part_B_footcap_top.png" width="280"><br>B Foot cap, top (o-ring groove) |
| <img src="part_B_footcap_bottom.png" width="280"><br>B Foot cap, bottom (heel, USB tunnel) | <img src="part_C_sled.png" width="280"><br>C Sled, posts side (8 mm OD posts, 4.0 mm insert holes) |
| <img src="part_C_sled_battery_side.png" width="280"><br>C Sled, battery side | <img src="part_E_key.png" width="280"><br>E Key |
| <img src="part_F_lightpipe.png" width="280"><br>F Light pipe (rod with collar) beside the key | <img src="part_G_rimclip.png" width="280"><br>G Rim clip |
| <img src="part_H_leafcard.png" width="280"><br>H Leaf card | <img src="part_I_usb_bung.png" width="280"><br>I USB bung |
| <img src="part_J_sma_boot.png" width="280"><br>J SMA boot | <img src="part_K_clip_pad.png" width="280"><br>K Clip pad |

### Hardware (not printed). McMaster-Carr part numbers from `mechanical\hardware_lists\enclosure_hardware_mcmaster_2026-11-01.md`

<img src="hw_00_hardware_kit.png" width="640" alt="hw_00_hardware_kit.png">

*The kit, seen from above, one of each type. Left to right along the bottom: brass insert (x8), nylon standoff (x4), nylon screw (x4), steel foot-cap screw (x4), vent patch (x1); silica bag at the far right (x1); the black o-ring loop (x1) above them. The silica bag is drawn folded to a small pack (see the note under the table).*

| Item | P/N | Qty | Where |
| --- | --- | --- | --- |
| Brass heat-set insert, M2.5 x 0.45, 4 mm long (4.0 mm hole, 5 mm deep) | 94459A768 | 8 | 4 in the sled posts, 4 in the sleeve plinth corners (underside) |
| Nylon hex male-female standoff, M2.5, 14 mm body, 4.5 mm across flats, 3.9 mm male thread | 95783A060 | 4 | Between main board and sens1; the male end goes down through sens1 into the sled insert |
| Nylon pan head Phillips screw, M2.5 x 5 | 92492A709 | 4 | Main board top into the standoffs |
| 316 SS socket head screw, M2.5 x 6 | 92290A056 | 4 | Foot cap to plinth |
| EPDM o-ring cord, 2.0 mm, ~154 mm loop (join with CA glue) | 1178N19 | 1 | Foot cap groove |
| Silica gel bag, ~3 g | 2189K15 | 1 | Inside, beside the battery |
| Adhesive ePTFE vent patch | (DigiKey/Mouser) | 1 | Over the 3.0 mm vent hole in the cap |
| 14-way 0.5 mm FFC, 30 mm | (DigiKey/Mouser) | 1 | CN1 (main) to CN1 (sens1) |
| 602050 LiPo (6 x 20 x 50 mm) | (battery supplier) | 1 | Back of sled |
| RG316 pigtail, right-angle SMA plug, 60-80 mm | (DigiKey/Mouser) | 1 | sens1 J1 to the bulkhead |
| IP67 SMA bulkhead jack (6.5 mm hole) | (DigiKey/Mouser) | 1 | Heel floor of the foot cap |
| Thin foam | | some | Round the battery |

**Silica bag note.** The McMaster bag (44 x 25 mm, flat) does not lie flat beside the battery: there is only about 5 mm of width between the battery rail and the sleeve wall. In the model it is drawn as a small folded pack about 40 x 5 x 6 mm. Fold the bag lengthwise (or cut a narrower bag) before you tuck it in. This is still to be settled for the next print.

---

## 2. Before you start (prepare the printed parts)
1. Remove brims and supports. Check that the sleeve's top rim (the face the o-ring presses on) is flat and smooth.
2. **Heat-set inserts in the sled:** press one M2.5 x 4 mm insert (94459A768) into each of the 4 posts on the front of the sled (part_C_sled.png). The hole is 4.0 mm and 5 mm deep, so the insert sits flush with the post face with 1 mm of hole left below it. Keep them square to the plate.

<table><tr>
<td><img src="hw_prep2_sled_inserts_before.png" width="400" alt="hw_prep2_sled_inserts_before.png"><br>Before: 4 gold inserts (94459A768), one per post.</td>
<td><img src="hw_prep2_sled_inserts_fitted.png" width="400" alt="hw_prep2_sled_inserts_fitted.png"><br>Fitted: each insert flush with the post face.</td>
</tr></table>

3. **Heat-set inserts in the sleeve:** turn the sleeve upside down and press one M2.5 x 4 mm insert (94459A768) into each of the 4 holes (4.0 mm, 5 mm deep) in the flared base.

<table><tr>
<td><img src="hw_prep3_plinth_inserts_before.png" width="400" alt="hw_prep3_plinth_inserts_before.png"><br>Before: the sleeve seen from below, 4 inserts under the 4 corner holes.</td>
<td><img src="hw_prep3_plinth_inserts_fitted.png" width="400" alt="hw_prep3_plinth_inserts_fitted.png"><br>Fitted: inserts flush with the underside of the base.</td>
</tr></table>

4. **Clip pads (optional):** glue a pad to each inner face of the clip hook.
5. **Vent:** stick the ePTFE vent patch over the 3.0 mm hole in the foot cap, on the inside (top) face.

<table><tr>
<td><img src="hw_prep5_vent_before.png" width="400" alt="hw_prep5_vent_before.png"><br>Before: the vent patch (light disc) above the 3.0 mm hole, which is next to the cap's front-right corner.</td>
<td><img src="hw_prep5_vent_fitted.png" width="400" alt="hw_prep5_vent_fitted.png"><br>Fitted: the patch covers the hole on the top face.</td>
</tr></table>

6. Try the key and the light pipe in their holes in the sleeve. They should slide freely. Sand them if they're tight.

## 3. Build the cartridge
**Step 1. Sled** (build_01_sled_inserts.png). The sled stands upright with its posts facing you and its narrow end down. The narrow end is the USB end. The four gold inserts are already in the posts.

<img src="build_01_sled_inserts.png" width="360" alt="build_01_sled_inserts.png">


**Step 2. sens1 onto the sled** (build_02_sens1_on_sled.png). Put sens1 on the 4 posts, components facing you (away from the sled), with the SMA connector J1 at the bottom. The holes in sens1 line up with the inserts. Don't fasten it yet.

<img src="build_02_sens1_on_sled.png" width="360" alt="build_02_sens1_on_sled.png">


**Step 3. FFC into sens1.** Plug one end of the 30 mm FFC into CN1 at the top of sens1. Do it now, because CN1 is hard to reach once the main board is on.

**Step 4. Standoffs** (build_03_spacers.png is the same picture as the "fitted" one below). Take the four nylon standoffs (95783A060). Put the threaded (male, 3.9 mm) end of each one through a sens1 mounting hole and screw it into the insert in the sled post behind it, finger-tight plus a gentle nip with a 4.5 mm spanner or pliers (nylon strips easily). This clamps sens1 to the sled. The standoff stands 14 mm tall on sens1, with its female thread facing up. Hex flats are 4.5 mm; turn each hex so a flat faces the nearest component if you can.

<table><tr>
<td><img src="hw_step4_standoffs_before.png" width="400" alt="hw_step4_standoffs_before.png"><br>Before: white standoffs, thread end towards sens1, in line with the 4 mounting holes.</td>
<td><img src="hw_step4_standoffs_fitted.png" width="400" alt="hw_step4_standoffs_fitted.png"><br>Fitted: threaded ends through sens1 into the sled inserts.</td>
</tr></table>

**Step 5. Main board** (build_04_main_board.png). Plug the other end of the FFC into the main board's CN1. Then fold the main board over onto the standoffs, components facing out, with USB-C at the bottom. Put a short nylon M2.5 x 5 screw (92492A709) through each of the main board's 4 mounting holes into the top of the standoff and tighten gently. The board sits on the four standoff tops; sens1 is already held by the standoffs, so the long screws of the first draft are no longer used.

<table><tr>
<td><img src="hw_step5_nylon_screws_before.png" width="400" alt="hw_step5_nylon_screws_before.png"><br>Before: 4 white nylon screws (92492A709) in line with the main board's holes and the standoff tops.</td>
<td><img src="hw_step5_nylon_screws_fitted.png" width="400" alt="hw_step5_nylon_screws_fitted.png"><br>Fitted: heads on the main board, shanks in the standoffs.</td>
</tr></table>

<img src="build_04_main_board.png" width="360" alt="build_04_main_board.png">

**Step 6. Check the FFC** (build_05_ffc_side.png, side view). The FFC should make a smooth U-turn above the top edge of the boards without kinking. It has about 1 mm of room under the roof.

<img src="build_05_ffc_side.png" width="360" alt="build_05_ffc_side.png">


**Step 7. Battery and silica bag** (build_06_battery.png, view from the back). Turn the cartridge round. Wrap the battery in thin foam and slide it between the two rails on the back of the sled, lead end down, until it sits on the ledges. Route the lead round the side to the battery JST (U4) on the main board, but don't plug it in yet. Tuck the silica gel pack (2189K15) in beside the battery, outside the rail (see the silica bag note in the hardware section).

<img src="build_06_battery.png" width="360" alt="build_06_battery.png">

<table><tr>
<td><img src="hw_step7_silica_before.png" width="400" alt="hw_step7_silica_before.png"><br>Before (side view, sled plate on the left): the pale blue pack floats behind the sled's back face.</td>
<td><img src="hw_step7_silica_fitted.png" width="400" alt="hw_step7_silica_fitted.png"><br>Fitted: the pack lies on the sled's back face, outside the battery rail.</td>
</tr></table>

**Step 8. Pigtail.** Screw the right-angle SMA plug of the pigtail onto sens1 J1 at the bottom of the cartridge. Hand-tight is enough.

## 4. Key and light pipe into the sleeve
**Step 9** (build_07_key_pipe_position.png shows where they end up against the board). Hold the sleeve with its open bottom up. From the inside, push the key into the 7.4 mm hole on the front wall, cap first, so the flange sits in the counterbore. Push the light pipe into the 2.7 mm hole beside it, outer end first, with the notch in the key's flange round it. Nothing holds them yet, so keep the sleeve front-down until the cartridge is in.

<img src="build_07_key_pipe_position.png" width="360" alt="build_07_key_pipe_position.png">


## 5. Close the enclosure
**Step 10. Cartridge into the sleeve** (step3_cartridge_in_sleeve.png, seen from below, the 4 gold plinth inserts visible in the corners). Keep the sleeve upside down. Lower the cartridge in, top end (FFC loop) first, main board towards the front wall (the key side). The top of the sled drops into the slot between the ribs on the inside of the roof. Once it's down, the board holds the key and light pipe in place: the key plunger sits 0.2 mm off SW1.

<img src="step3_cartridge_in_sleeve.png" width="360" alt="step3_cartridge_in_sleeve.png">


**Step 11. Foot cap** (build_08_pigtail_bulkhead_cap.png, sleeve hidden).
- Push the SMA bulkhead jack up through the 6.5 mm hole in the heel floor and tighten its nut. Screw the free end of the pigtail onto it.
- Pass the solar panel cable in through the 4.5 mm hole in the toe (front-left) and plug it into the solar JST (U5).
- Plug in the battery (U4). **Battery first, before the solar panel or USB** (rule printed on the board: BATT FIRST).
- Lay the o-ring cord in the cap groove.
- Put the cap onto the sleeve's open end, heel (box) under the SMA end, USB tunnel lined up with the USB-C connector. Fit the 4 M2.5 x 6 screws (92290A056) through the cap into the plinth inserts and tighten them in a cross pattern, a little at a time, so the o-ring compresses evenly (step4_footcap_on.png). The screw heads stand about 0.5 mm proud of the cap's underside (the counterbore is 2 mm deep, the head is 2.5 mm).

<img src="build_08_pigtail_bulkhead_cap.png" width="360" alt="build_08_pigtail_bulkhead_cap.png"> <img src="step4_footcap_on.png" width="360" alt="step4_footcap_on.png">

O-ring (1178N19, 2 mm cord, glued into a loop):

<table><tr>
<td><img src="hw_step11_oring_before.png" width="400" alt="hw_step11_oring_before.png"><br>Before: the black loop above the cap's groove.</td>
<td><img src="hw_step11_oring_fitted.png" width="400" alt="hw_step11_oring_fitted.png"><br>Fitted: the cord sits in the groove and stands about 0.5 mm proud of the cap face. The sleeve squeezes it flat.</td>
</tr></table>

Foot-cap screws (92290A056, M2.5 x 6, 4 off), seen from below:

<table><tr>
<td><img src="hw_step11_footcap_screws_before.png" width="400" alt="hw_step11_footcap_screws_before.png"><br>Before: 4 steel screws below the cap, one under each corner hole, aimed at the gold plinth inserts.</td>
<td><img src="hw_step11_footcap_screws_fitted.png" width="400" alt="hw_step11_footcap_screws_fitted.png"><br>Fitted: heads in the counterbores, tips in the inserts.</td>
</tr></table>


**Step 12. Bung and boot (optional fit check).** Press the USB bung into the tunnel recess under the cap. Slide the SMA boot over the bulkhead under the heel.

<img src="build_09_sleeve_on.png" width="360" alt="build_09_sleeve_on.png">


## 6. Mounting
**Step 13. Rim clip** (step5_clip_side.png, build_11_complete.png). As designed, the clip's channel slides up onto the dovetail rail on the back of the sleeve until it hits the stop at the roof end. The stop carries the enclosure's weight when it hangs from the rim.

<img src="step5_clip_side.png" width="360" alt="step5_clip_side.png"> <img src="build_11_complete.png" width="360" alt="build_11_complete.png">


> **This step does not work on the current print.** The clip channel is 30 mm long, but there are only about 15 mm between the bottom of the rail and the flared base, so the clip can't get under the rail. **Workaround for this print:** file off the small stop block at the top of the rail, slide the clip down onto the rail from above the roof, then glue it (CA or epoxy) or drill a ~2 mm hole through the clip and rail and push in a pin. Without the glue or pin, the enclosure slides down out of the clip. The model will be changed for the next print (proposed: a hook-on cleat in place of the rail).

**Step 14.** Hang the clip over the tank rim with the back of the node against the glass. Put the leaf card with the solar panel where it gets light, and route its cable down to the node.

## Taking it apart
Undo the 4 cap screws and lower the cap. Unplug solar and battery, unscrew the pigtail from the bulkhead, and slide the cartridge out downwards. To separate the boards, remove the 4 short screws from the main board, then unscrew the standoffs from the sled (this frees sens1).
