# Tidemark: filament options (2026-10-27)

Colours from the family palette (gateway concepts, 06-family.svg; the Tidemark sketch for graphite):

| Role | Name | Target hex |
| --- | --- | --- |
| Shell, foot cap, sled, clips | Abyss navy (matte) | #1F3347 |
| Key, eye | Coral | #FF7A59 |
| Bung, boot, clip pads, (membrane) | Graphite | about #4A4F57 |
| Light pipe | Clear | n/a |

Printer: Snapmaker U1. It prints PLA, PETG, TPU and PVA as standard (ASA etc. need the seal cover); 4 toolheads.

**Caveat:** the hex values in this file are the design targets, not the filament makers' published values. None of the retailer pages found give a hex code for these spools. Order a sample or check the maker's swatch before buying 1 kg.

---

## 1. Shell: Abyss navy, PETG (about 150-200 g per enclosure)

| Option | Finish | Fit to #1F3347 | Notes |
| --- | --- | --- | --- |
| **Spectrum PET-G MATT Navy Blue** (1.75 mm, 1 kg) | Matte | Closest *finish*. Listed as RAL 5002 (ultramarine), which is likely a bit bluer/more saturated than Abyss's slate navy | 230-255 °C nozzle, 60-80 °C bed. Sold by 3DJake, RobotShop |
| **Polymaker PolyLite PETG Dark Blue** (PB01034) | Not stated (PolyLite PETG is normally glossy) | Unknown, check the swatch | 230-240 °C, bed 70-80 °C |
| **Bambu Lab PETG Basic Navy Blue** | Glossy | "Deep navy"; likely close in hue | A textured PEI plate and fuzzy skin on the side walls take most of the gloss off |
| Snapmaker PETG HF Cobalt Blue (RFID) | Glossy | Too bright for Abyss | The only official U1 blue; listed here so you know it isn't a match. Snapmaker PETG HF is $22.99 / kg (US store) |

**Recommendation:** Spectrum PET-G MATT Navy Blue, because matte is part of the look. If its blue reads too bright next to the Ledger gateway, use Bambu PETG Basic Navy Blue with textured plate and fuzzy skin. **Check:** what filament the Ledger gateway was printed in, and use the same spool if possible so the family matches exactly.

## 2. Eye (light window): translucent coral, PETG (a few grams)

| Option | Finish | Notes |
| --- | --- | --- |
| **Bambu Lab PETG Translucent Orange** | Glossy, translucent, "excellent light transmission" | About $25 / kg; one listing showed it out of stock. Behind it the yellow 590 nm LED reads warm amber, which matches the design intent |
| Siddament Translucent Orange PETG | Translucent | About $12 (Australian seller) |

No "translucent coral" PETG was found; translucent orange is the closest. **Recommendation:** Bambu PETG Translucent Orange.

## 3. Key: coral

No coral, salmon or peach **TPU 95A** is currently sold. SainSmart's "Living Coral" 95A and "Peach" 90A are both listed as discontinued. Options:

| Option | How it works | Notes |
| --- | --- | --- |
| **a. Graphite TPU membrane + coral PETG cap (recommended)** | The TPU 95A membrane is co-printed in graphite, and a small coral PETG dot or dome is co-printed on its face, like the Ledger's coral PETG key cap | Exact family colour, still sealed by the TPU. Use the same translucent orange as the eye, or an opaque coral (next row) |
| b. Opaque coral PETG cap | **Recycling Fabrik rPETG Premium Pastel Coral** (matte, opaque) | About CHF 28 / kg (3DJake); "pink/rose" coral, softer than #FF7A59. Pairs with the matte shell |
| c. Red or pink TPU 95A for the whole key | Snapmaker TPU 95A HF Red or Pink | Simplest print, but not coral |

## 4. Bung, boot, clip pads (and membrane): graphite TPU 95A (about 20 g)

| Option | Notes |
| --- | --- |
| **Snapmaker TPU 95A HF Dark Gray** (RFID) | Official U1 spool; $39.99 / kg (US store), €41.99 (EU) |
| Bambu Lab TPU 95A HF Gray | Lighter grey likely; Bambu says not AMS-compatible, but that doesn't affect the U1 |

**Recommendation:** Snapmaker TPU 95A HF Dark Gray. It's tuned for the U1 and RFID-detected.

## 5. Light pipe: clear (a few grams)

| Option | Notes |
| --- | --- |
| **2.5 mm clear acrylic rod** (cut to length) | Best light transmission; glued or press-fit into the wall. Frees a toolhead |
| Polymaker PolyLite PETG V2 Transparent | Co-printable, but printed "clear" PETG is hazy; fine for a short 6 mm pipe |

**Recommendation:** an acrylic rod. It needs no toolhead, and the concept already allows it.

---

## Toolhead plan for the U1 (4 heads)

| Head | Filament |
| --- | --- |
| T0 | Abyss navy PETG (shell) |
| T1 | Translucent orange PETG (eye + key cap) |
| T2 | Graphite TPU 95A (key membrane; bung and boot print separately) |
| T3 | Spare (clear PETG if you don't use an acrylic rod) |

## Shopping list (recommended picks)

| Item | Qty | Approx. price |
| --- | --- | --- |
| Spectrum PET-G MATT Navy Blue 1.75 mm | 1 kg | not checked |
| Bambu Lab PETG Translucent Orange 1.75 mm | 1 kg | about $25 |
| Snapmaker TPU 95A HF Dark Gray | 1 kg | $39.99 |
| 2.5 mm clear acrylic rod | 1 short length | a few dollars |
| Optional: Recycling Fabrik rPETG Pastel Coral (opaque key cap) | 1 kg | about CHF 28 |

Prices are from retailer listings found on 2026-10-27; stock and regional prices vary.

## Sources
- Snapmaker U1 filament range and compatibility: https://us.snapmaker.com/collections/snapmaker-u1-series , https://eu.snapmaker.com/collections/snapmaker-u1 , https://us.snapmaker.com/products/petg-filament
- Spectrum PET-G MATT Navy Blue: https://shop.spectrumfilaments.com/product-eng-1357-Filament-Spectrum-PET-G-MATT-1-75mm-NAVY-BLUE-1kg-RAL-5002.html , https://3djake.com/spectrum/pet-g-matt-navy-blue
- Bambu PETG Basic Navy Blue: https://www.makerpoint.nl/en-gb/3d-printing/consumables/filament/bambu-lab-petg-basic-navy-blue-30604-1kg-refill-210000008599
- Polymaker PolyLite PETG Dark Blue: https://www.3djake.ch/de-CH/polymaker/polylite-petg-dark-blue?sai=14691
- Bambu PETG Translucent Orange: https://www.3djake.com/bambu-lab/petg-translucent-orange
- Siddament Translucent Orange PETG: https://siddament.com.au/en-us/products/translucent-orange-petg
- Recycling Fabrik rPETG Pastel Coral: https://www.3djake.com/recycling-fabrik/rpetg-premium-pastel-coral
- SainSmart Living Coral TPU (discontinued): https://www.sainsmart.com/products/living-coral-flexible-tpu-filament-1-75mm-0-8kg-1-76lb
- Bambu TPU 95A HF: https://3djake.at/bambu-lab/tpu-95a-hf
- Polymaker PolyLite PETG V2 Transparent: https://www.digitec.ch/en/s1/product/polymaker-polylite-petg-v2-transparent-175mm-petg-175-mm-1000-g-3d-printer-filament-21563068

---

## US price check 2026-10-30 (live store pages via Chrome)

- Snapmaker "Steel Blue (2E4462)" is **Matte PLA**, not PETG: not for the enclosures. Snapmaker sells no navy PETG (PETG HF blues: Cobalt 0049B8, Violet 493AB2).
- Navy PETG: **Bambu PETG Basic Navy Blue (30604)**, $13.99 refill (MSRP), down to $9.09/roll when buying 10+ (mix and match), in stock. Glossy; refills need a reusable spool ($7.99) or buy "with spool". Polymaker PETG Dark Blue $19.99 (glossy, shade unchecked). Sunlu High Speed Matte PETG "Blue" $12.79 (shade unknown, probably too bright).
- Translucent orange PETG (eye, key cap): Bambu PETG Translucent Orange (32300) $15.99 refill ($10.39 at 10+); Snapmaker PETG Translucent Orange (FB8D02) $19.99 with RFID spool.
- Graphite TPU 95A: Snapmaker TPU 95A HF Dark Gray (595E69) $39.99, RFID; Bambu TPU 95A HF Gray (51101) $25.19 on sale (typical $41.99), lighter grey likely.
- Black PETG (gateway bezel): Polymaker PETG Black $18.99; Snapmaker PETG HF Black $22.99; Bambu PETG Basic Black $13.99.
- Amazon not checked.
