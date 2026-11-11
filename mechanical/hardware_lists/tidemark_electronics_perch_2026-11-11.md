# Tidemark electronics and Perch hardware: part picks (2026-11-11)

Sourcing check by parts-sourcing, live DigiKey (kicad MCP, API) and Mouser (kicad-pro MCP, API) data read on 2026-11-11.
Nothing was ordered or added to a cart. Quantities are per enclosure; the "5" column is for 5 enclosures (5 feather boards were ordered).
Price breaks: DigiKey breaks were read for the Essentra parts (K030, N025, M6 nut) and the Molex FFC. Mouser returned only the 1-piece price, so the 5-piece Mouser figure is 5 x the 1-piece price (the real price may be slightly lower). The "about" prices were not read at the 5-piece break.

## Summary

| # | Item | Pick | Source | Qty | Price for 1 | Price for 5 | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 14-way 0.5 mm FFC, 30 mm, **Type D (contacts on opposite sides)** | Molex 0150200140 (15020-0140) | DigiKey 0150200140-ND | 1 | $3.82 | $19.10 | stocked (1,936). Cable thickness not confirmed, see item 1 |
| 2+3 | RG316 pigtail with RA SMA plug and IP68 SMA bulkhead jack, one assembly | Molex 73230-7070 (152.4 mm) | Mouser (DigiKey: 0 stock, MOQ 200) | 1 | $30.51 | $152.55 | stocked at Mouser (49). **Too long: 152 mm, not 60-80 mm.** Hole/flat not verified |
| 4 | 602050 LiPo, JST PH 2-pin | none | - | 1 | - | - | **not stocked at DigiKey or Mouser**, see item 4 |
| 5a | M6 x 30 knurled nylon thumbscrew | none found at DigiKey/Mouser. Stand-in: Essentra 50M060100K030 (nylon M6 x 30 hex bolt, 10 mm head) | DigiKey 145-50M060100K030-ND | 1 | $0.32 | $1.30 | thumbscrew **not found**, hex bolt is a stand-in |
| 5b | M6 nylon hex nut, 10 mm AF | Essentra 04M060100HN | DigiKey RPC7080-ND | 1 | $0.15 | $0.63 | stocked (23,415) |
| 5c | M4 x 25 nylon pan screw | Essentra 50M040070N025 | DigiKey 145-50M040070N025-ND | 1 | $0.16 | $0.65 | stocked (1,715) |
| 5d | M4 nylon hex nut | Essentra 04M040070HN | DigiKey (PN not read) | 1 | $0.16 | about $0.65 | stocked (4,838); Mouser 9,103 |
| 5e | M4 x 10 nylon pan screw | Essentra 50M040070N010 | DigiKey (PN not read) | 2 | $0.30 | about $1.20 | stocked (29,618); Mouser 6,500 |

Total for the parts that have a pick (items 1, 2+3, 5a-5e): about $35.42 for one enclosure, about $176 for five (the cable assembly is 86 percent of it). The battery is not included.

## 1. FFC, 14-way, 0.5 mm, 30 mm

**Contact type needed: Type D (opposite sides). Confidence: high on the geometry, but it rests on the facts listed under "Not confirmed".**

How I got there:
- Both CN1 are the same part, Molex 503480-1400 (the sales drawing is `hardware\sensors\ph\nrf54l15_feather_sens1\5034801400_sd.pdf`). The drawing gives the mating FPC as 0.3 +-0.05 mm thick, 0.5 mm pitch, 3.5 mm insertion depth. It does not state in extractable text which side the contacts are on, but that does not matter here because both boards carry the identical connector in the identical orientation.
- In the PCB files both CN1 are placed at (138.475, 121.43), rotation 90, on F.Cu. Pad 1 is at board y 124.68 and pad 14 at y 118.18 on both boards (main and sens1 STATUS agree; I re-read the sens1 .kicad_pcb: pad 1 at local (-3.25, -1.325)).
- Assembly (ASSEMBLY.md steps 2-6, NOTES.md): both boards have their component sides facing the same way (front), main in front of sens1, 14 mm apart. The FFC leaves the main CN1 heading outward, makes a 180 degree U-turn round the far short edge, and comes back into sens1's CN1 in the gap between the boards. At both connectors the board is behind the cable (same direction), with identical contact orientation.
- In a 180 degree fold the face of the cable that is on the outside of the bend at one end is on the inside at the other end. The contacts must face the same way relative to the board at both ends, so in the flat cable the contacts are on opposite faces at the two ends. That is Type D (Molex wording "Opposite Side Contacts (Type D)"; DigiKey wording "Top on One Side, Bottom on Other"). A Type A cable (same side at both ends) would have one end's contacts facing away from the connector's contacts.
- The fold axis runs along y and the conductors run along x, so conductor n stays at the same y. Pin 1 meets pin 1 on both boards (no pinout reversal). This agrees with the sens1 STATUS note "CN1 and the FFC fold".

Not confirmed (be sure before ordering 5):
1. **Cable thickness.** The 503480 wants 0.3 +-0.05 mm at the contacts. The DigiKey and Mouser pages give no thickness. The Molex Premo-Flex brochure (987651-6282, read) lists the 15020 series at 0.5 mm pitch but its thickness column was garbled in the text extraction. Molex's own 15020 page timed out, and Molex PDFs and Mouser product pages did not load for me. 0.3 mm total at the stiffened ends is what 0.5 mm FFC connectors normally take, but I could not read the number. Check "thickness 0.30" on the Molex 15020 page, or measure the stiffened end with calipers (buy 1 and test-fit it in CN1 before buying more).
2. **Type D comes from the geometry above.** If a test fit on the real boards shows the contacts face the wrong way at one end, use the Type A twin (Molex 15020-0139 at Mouser, 1,986 in stock, $4.23).

Candidates (stock read 2026-11-11):

| MPN | Source | Type | Length | Stock | Price | Note |
| --- | --- | --- | --- | --- | --- | --- |
| **Molex 0150200140** (15020-0140) | DigiKey 0150200140-ND | D | 29.97 mm | 1,936 | $3.82 (1), $3.243 (10) | the pick. Bag, MOQ 1. Mouser shows 0 stock for it |
| Molex 15120-0140 | Mouser | D, Au, series "Premo-Flex 15120" (XFLEX) | 30 mm | 248 | $3.12 | DigiKey 0 stock, MOQ 1000. Different series (extra flex, thickness unknown): do not use unless the thickness is checked |
| Molex 15020-0139 | Mouser | A (wrong type for this stack unless the test fit says otherwise) | 30 mm | 1,986 | $4.23 | fallback only |
| GCT 05-14-D-0030-A-4-06-4-T | DigiKey | D | 30 mm | 0 | MOQ 1000 | not buyable |
| Koratech 014N0030A06330404S0002 | DigiKey | D | 30 mm | 500 | $15 each, MOQ 10 | not worth it |

Length: the pick is 29.97 mm and the model assumes 30 mm. The 4 mm bare ends each side (3.5 mm goes into the connector) leave about 22 mm free for the U-turn; NOTES.md already says a standard 30 mm FFC fits.
Rating check: 0.5 mm pitch and 14 conductors match CN1. Current per conductor is not on the listing; the CN1 contact rating is 0.5 A and the polyfuse F1 on CN1.13 trips at 0.5 A.

## 2 and 3. RG316 pigtail and SMA bulkhead jack

**J1 on sens1:** BWSMA-KWE-Z001 (BAT Wireless), footprint `SMA_BAT_Wireless_BWSMA-KWE-Z001`, "SMA right angle" per the sens1 sourcing md, LCSC C496551. I could not read its datasheet (not at DigiKey/Mouser). SMA "K" parts are female jacks (centre socket), so the pigtail end must be a male SMA plug; both listed assemblies have that. Not verified against the BAT Wireless drawing.

I found no 60-80 mm RG316 assembly with an RA SMA plug and a bulkhead jack. The shortest standard length is 6 in (152.4 mm). Options:

| MPN | Source | Jack | Plug | Length | Stock | Price | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Molex 73230-7070** | Mouser (Mouser PN not read); DigiKey 900-0732307070-ND has 0 stock and MOQ 200 | SMA straight bulkhead, IP68 rated | SMA RA male | 152.4 mm | Mouser 49 | $30.51 | the pick: IP rated, 49 covers 5 |
| Amphenol 095-902-570-006 | Mouser | SMA straight bulkhead, IP67 | SMA RA | 6 in | 168 | $34.33 | same length, IP67 stated, more stock |
| Molex 73230-7100 | Mouser | SMA bulkhead, no IP rating listed | SMA RA | 152.4 mm | 83 | $21.20 | cheaper, no seal rating |
| Amphenol 135111-01-06.00 | DigiKey ACX1635-ND (886), Mouser (81) | SMA bulkhead, no IP rating listed | SMA RA | 152.4 mm | see left | $28.80 | non-IP |

**Problem: 152 mm is about twice the 60-80 mm the enclosure assumed.** NOTES.md gives the plug nut only 0.54 mm from the heel wall and no spare room, so about 70-90 mm of RG316 would have to be coiled in the sleeve. RG316 has roughly a 15 mm bend radius. I have not checked the cavity for a loop; kicad-designer / fusion-enclosure should. If it does not fit, the options are (a) a custom-length assembly (Amphenol Custom Cable quick-build "Q-" assemblies at DigiKey, made to order, price not checked), or (b) build the pigtail from RG316 cable plus a crimp RA SMA plug and a crimp bulkhead jack, which needs a crimp tool.

Bulkhead check, not done: hole diameter and any D-flat on the Molex 73230 jack (NOTES say the heel hole is 6.5 mm and the D-flat is not modelled). A standard SMA bulkhead thread is 1/4-36 (6.35 mm), so a 6.5 mm round hole suits a round-thread jack, but a jack with flats needs a D hole or the nut will not stop it turning. The Molex drawing did not load for me. The listing says "Front Side Nut"; whether an o-ring is included is not stated (the IP68 rating implies one).

## 4. 602050 LiPo with JST PH 2-pin

**No 602050 (6 x 20 x 50 mm, about 600 mAh) cell is stocked at DigiKey or Mouser.** I searched both for "602050", "LP602050", "ICP602050" and for 3.7 V cells by dimensions.

Closest stocked cells, none a drop-in:

| MPN | Source | Size | Capacity | Stock | Price | Why not |
| --- | --- | --- | --- | --- | --- | --- |
| Renata ICP402050PR | Mouser | 52.5 x 20.7 x 4.5 mm | 420 mAh | 5 | $16.98 | thinner, but 2.5 mm longer and 0.7 mm wider than the 50 x 20 pocket; connector type not listed; only 5 in stock |
| Jauch LP503040JH+PCM+2 WIRES 50MM | DigiKey 1908-LP503040JH+PCM+2WIRES50MM-ND | 42 x 30.5 x 5.4 mm | 600 mAh | 1,601 | $10.81 | 30.5 mm wide, does not fit the 20 mm cradle; bare wires |
| GlobTek BL0750F5030481S1PCTC | DigiKey 1939-BL0750F5030481S1PCTC-ND | 50.5 x 30.5 x 5.3 mm | 700 mAh | 1,632 | $11.85 | 30.5 mm wide |
| Adafruit 3898 | DigiKey 1528-2731-ND | 37 x 17.5 x 8.2 mm | 400 mAh | 1,624 | $6.95 | 8.2 mm thick (pocket is 6 mm), JST PH |
| Adafruit 1578 | Mouser | not read | 500 mAh | 433 | $7.95 | dimensions not checked |

I could not name a vendor that stocks a 602050 with a JST PH plug. Adafruit's battery category page showed no 600-800 mAh cell and no dimensions, so I will not name one. 602050 is a generic cell size from many cell makers; a cell bought outside DigiKey/Mouser needs a JST PH 2-pin (2.0 mm pitch) plug with the polarity below, or a re-terminated bare lead. Any other cell size needs the cradle and pocket (BattT/BattW/BattL 6/20/50 mm in NOTES) changed.

**Polarity check against U4.** U4 is a JST S2B-PH-K-S (2-pin, side entry, 2.0 mm pitch): pad 1 = VBAT (+), pad 2 = GND (nets on the U4 pads in the main .kicad_pcb). The plug must carry the red (+) wire in the housing position that meets pad 1. Cells from different vendors often differ in this (Adafruit-style and SparkFun-style cells are commonly wired in opposite order). Before first plug-in, measure the plug and compare with U4 pad 1 (+); if reversed, re-seat the wires in the PHR-2 housing. The board's "BATT FIRST" rule also applies. No stocked fitting cell was identified, so no specific cell was checked.

## 5. Perch nylon hardware (Amazon list rows 13-17)

Amazon pages would not load for me (HTTP 503 on the search page), so no ASIN was picked and none is guessed. The picks are DigiKey/Mouser parts from Essentra (MicroPlastics series), all nylon, in stock.

| Row | Need | Pick | DigiKey PN | Qty | Price 1 | Price 5 | Stock | Check |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 13 | M6 x 30 knurled thumbscrew, head up to 20 mm | **no thumbscrew found** at DigiKey or Mouser (6 searches; the Essentra code 50M060100T0xx is 0 stock at Mouser and absent at DigiKey). Stand-in: Essentra 50M060100K030, nylon M6 x 1 x 30 hex-head slotted bolt, head 10 mm, 34.7 mm overall | 145-50M060100K030-ND | 1 | $0.32 | $1.30 | DK 495 | Not a thumbscrew: turn with a 10 mm spanner (gently, nylon strips), or fit a printed knob. A knurled nylon M6 x 30 thumbscrew has to come from Amazon or similar (not verified, no ASIN) |
| 14 | M6 hex nut, 10 mm AF x 5 mm | Essentra 04M060100HN | RPC7080-ND | 1 | $0.15 | $0.63 | DK 23,415 | DigiKey lists width 9.91 mm, thickness 5.4 mm. The pocket is 10.3 AF, so it fits; the nut is 0.4 mm thicker than the 5 mm in PERCH.md (pocket depth Y 66.5-72.2 is 5.7 mm) |
| 15 | M4 x 25 pan screw | Essentra 50M040070N025 | 145-50M040070N025-ND | 1 | $0.16 | $0.65 | DK 1,715 | Slotted drive, head 8.0 mm, 27.4 mm overall |
| 16 | M4 hex nut, 7 mm AF x 3.2 | Essentra 04M040070HN | not read | 1 | $0.16 | about $0.65 | DK 4,838, Mouser 9,103 | AF and thickness of this nut not read; measure against the 7 mm pocket |
| 17 | M4 x 10 pan screw (2 off) | Essentra 50M040070N010 | not read | 2 | $0.30 | about $1.20 | DK 29,618, Mouser 6,500 | Slotted drive; head about 8 mm (PERCH.md assumes about 7): check the heads do not hit the saddle |

The packs are bulk bags with MOQ 1. The DigiKey PN pattern "145-<MPN>-ND" matched where I could read it (K030 and N025); for N010 and the M4 nut I did not read it, so the upload CSV gives the MPN and leaves the PN blank.

## Checks Brian must do

1. FFC: confirm 0.30 mm thickness at the stiffened ends (Molex 15020 page) or test-fit one in CN1 first.
2. Pigtail: decide how to handle 152 mm (coil room in the heel) and check the bulkhead hole/flat on the Molex 73230 drawing.
3. Battery: no stocked 602050; pick a source or a different cell, then check JST polarity (red on U4 pad 1) with a meter.
4. Perch: no thumbscrew available here; hex-bolt stand-in or buy a knurled one elsewhere.

## Upload files (same folder)

- `tidemark_electronics_perch_digikey_2026-11-11.csv` (DigiKey, quantities for 1 enclosure)
- `tidemark_electronics_perch_mouser_2026-11-11.csv` (Mouser pigtail only; Mouser part number left blank, upload by MPN)

## Recommended field changes

None for the schematic or footprints. ASSEMBLY.md was updated with the MPNs above. The enclosure model may need a pigtail change (see item 2).
