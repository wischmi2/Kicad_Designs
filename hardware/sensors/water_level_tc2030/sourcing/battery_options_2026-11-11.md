# Water level node (XM125 radar, TC2030 variant): 1S LiPo options and battery life

Checked 2026-11-11 (parts-sourcing). Stock and price: live DigiKey API (kicad MCP). Mouser: kicad-pro search results only (its detail lookup is unreliable, e.g. MPN "3898" returned a Mean Well supply). Datasheets read from the seller PDFs where noted. Nothing ordered or carted.

## 1. Short answer

- **Crown (10 x 20 x 20 mm incl. PCM) only has small cells: 60 to 150 mAh.** Best fit: **TinyCircuits ASR00003, 150 mAh, 20.0 x 20.0 x 5.0 mm with PCM, DigiKey 1832-1031-ND**. Life about **38 days at 5 min and 28 days at 1 min** at 80 % usable. No reputable source found for a cell above 150 mAh that fits 10 x 20 x 20 mm.
- **Slab (up to 10 x 34 x 50 mm)** has real choices: **US Electronics USE-803048-1100 mAh** (1050 mAh min, PH-2P fitted, PCM) gives about **268 days at 5 min / 193 days at 1 min**.
- **The 110 uA idle sets the life.** Idle is 2.8 of the 3.1 mAh/day at 5 min. The reading rate matters little. Cutting idle (VSENS off between readings, which Brian decided against on 2026-11-03) would multiply the Crown life several times. Stated only as the lever, not a change request.

## 2. Power budget (battery side, estimates)

| Item | Value | Source / status |
| --- | --- | --- |
| Radar feather idle: R19/R1 divider 94 uA + XM125 hibernate 17.7 uA | about 110 uA | water_level_tc2030\STATUS.md Decisions item 1; XM125 DS Table 4 (hibernate 17.7 uA, via xm125_notes.md) |
| nRF54L15 sleep (System ON idle, RTC running) | 3 uA | Nordic product page nordicsemi.com/Products/nRF54L15: sleep modes 0.7 to 2.9 uA at 3 V, System OFF with GRTC 0.8 uA. Marketing page; the datasheet current-consumption tables could not be read (page too large for the fetch tool). Which sleep mode gives which value is UNVERIFIED |
| nPM1300 quiescent, bucks on in PFM, charger idle, NTC bias off | 5 uA assumed | UNVERIFIED. Nordic product page gives only ship mode 370 nA and hibernate 500 nA. Datasheet electrical tables not read. 5 uA is deliberately pessimistic; bench-measure it |
| **Idle total** | **about 118 uA = 2.83 mAh/day** | sum of the three rows |
| Radar reading: wake from hibernate, boot, measure, back to sleep | 3.0 mC | XM125 DS Fig 5.1: peak about 80 mA for about 1.5 ms with 6 to 15 mA plateaus at 1.8 V; average 0.18 mA at 1 Hz (0.33 mW). Model: 80 mA x 1.5 ms plus about 150 ms at 10 mA, with margin. Wake-up/boot time from hibernate is UNVERIFIED (assumed 150 ms). 1.8 V comes from the NCP161 LDO off VBAT, so battery current equals the 1.8 V load current |
| nRF54L15 CPU + I2C session | 0.3 mC | Assumed: about 100 ms at about 3 mA, battery side |
| BLE per reading (a few advertising events or a short connection) | 0.5 mC | Radio 4.8 mA TX and 3.4 mA RX at 0 dBm, 3 V (Nordic product page). Event durations are my assumption (advertising, 3 channels, about 3 to 4 ms at about 5 mA; short connection about 2 s at about 50 uA average). Not a Power Profiler capture. UNVERIFIED |
| **Per reading** | **3.8 mC = 0.00106 mAh** | sum |
| Readings per day | 288 (5 min), 1440 (1 min) | |
| **Daily use** | **3.14 mAh/day at 5 min, 4.35 mAh/day at 1 min** | idle 2.83 + readings 0.30 / 1.52 |

Life = 0.8 x capacity / daily use. Not included: LiPo self-discharge (typically 2 to 3 % per month, UNVERIFIED for these sellers), cold-weather loss, and labelled versus real capacity (minimum capacities are lower than typical). Treat the days as plus or minus 30 %.

## 3. Charging and polarity (all candidates)

- **Charge current (nPM1300 ICHG): at or below 0.5C.** nPM1300 minimum ICHG is 32 mA as I recall it (UNVERIFIED, check the PS). So: 60 and 70 mAh cells sit at about 0.5C even at the minimum (Jauch states max charge 0.5C; TinyCircuits says its 70 mAh cell wants a charger of 100 mA or less); 150 mAh cell: 32 to 75 mA; 400 to 500 mAh cells: 100 to 200 mA; 1050 mAh cell: 200 to 500 mA (US Electronics rates 1C max, 0.5C = 525 mA). Charge only at 0 to 45 C (cell datasheets). R8 on the feather is a 10 k NTC on the board, not on the cell, so it reads board temperature; acceptable indoors.
- **Termination:** 4.2 V cells, about 0.01 to 0.02C cut-off on the datasheets. Keep the nPM1300 4.20 V setting.
- **Polarity (U4 = JST S2B-PH-K-S, pad 1 = VBAT+, pad 2 = GND): red must land on pad 1.** Adafruit, US Electronics (red/black stated) and GlobTek document red = +, but none states which slot of the PH plug the red wire sits in, and a PH plug can be wired either way. I did not verify the slot against U4's pad numbering or footprint (kicad-designer or a meter can). **Before the first connection, meter the plug with the cell attached; the contact in the same position as U4 pad 1 must read +. Repeat for every new cell lot.** For wire-only cells (Jauch) and the TinyCircuits SH-plug cells, Brian crimps the PH plug, so polarity is under his control.
- **Plug parts if a cell needs one:** JST PHR-2 housing DigiKey 455-1165-ND (553,790 in stock, $0.10, checked 2026-11-11). Crimp socket SPH-002T-P0.5S is DigiKey strip/reel only (455-1127-500-ND, MOQ 500, 12,000 in stock; 455-1127-1000-ND MOQ 1000), so check leftover crimps and pre-crimped leads from the earlier cable orders first.

## 4. Option A: Crown (envelope 10 x 20 x 20 mm including PCM, tape and lead exit)

Sizes are the seller's stated finished-pack size (cell + PCM). Leave about 1 mm for tape and lead exit in the pocket.

| # | Part | Source / stock / price (2026-11-11) | Dims L x W x T (incl. PCM) | Capacity | Connector, polarity | Life 5 min / 1 min (80 %) | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A1 | **TinyCircuits ASR00003** | DigiKey 1832-1031-ND, 103 in stock, $4.95. Mouser ASR00003, 349 in stock, $4.95 | 20.0 x 20.0 x 5.0 (TinyCircuits datasheet; DigiKey lists 20.1 x 20.1 x 5.1) | 150 mAh, 3.7 V | Micro JST SH 1.0 mm, wire only 12 mm. **Cut the SH plug off and fit a PH-2, or splice a short pigtail.** SH plug polarity unknown, meter it | **38 / 28 days** | Best Crown fit by capacity. PCM included (datasheet text). Exactly at the 20 mm limit; 12 mm lead is short, so the PH plug has to sit at the cell edge. Datasheet: https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/2102/ASR00003_Web.pdf |
| A2 | **TinyCircuits ASR00011** | DigiKey 1832-1045-ND, 475 in stock, $4.95. Mouser ASR00011, 172 in stock, $4.95 | 16.0 x 15.0 x 5.0 (datasheet) | 70 mAh | Micro JST SH. Wire length printed as 22.0 mm but "0.472 in" (= 12 mm); datasheet inconsistent. Same plug/polarity caveat | 18 / 13 days | Fits with room. PCM included. Datasheet: http://files.tinycircuits.com/Datasheets/TinyCircuits_ASR00011.pdf |
| A3 | **Jauch LP501218JH+PCM+2 WIRE 50MM** | DigiKey 1908-LP501218JH+PCM+2WIRE50MM-ND, 129 in stock, $10.77 | 20.0 x 12.5 x 5.4 (DigiKey size field) | 60 mAh min, 65 typ | 2 bare wires 50 mm, **no plug**, crimp PH-2 by hand. Wire colours not stated in the text I read; meter it | 15 / 11 days | UL/IEC 62133 pack with PCM parameters (overcharge 4.28 V, over-discharge 3.0 V, over-current 0.5 to 3.0 A). Datasheet warns about deep discharge (0 V = PCM tripped; do a full charge to wake). Best documented, lowest capacity |
| A4 | Near miss: Renata ICP501421PS | Mouser ICP501421PS, 24 in stock, $11.59 (not at DigiKey) | 22.5 x 14.1 x 5.2 | 115 mAh | Not verified; no datasheet read; PCM not confirmed | 29 / 21 days | 2.5 mm over the 20 mm length. Only if the pocket grows |
| A5 | Near miss: MikroE MIKROE-2759 (HPL402323 2C) | DigiKey 1471-1865-ND, 59 in stock, $8.40. Mouser 134 in stock, $7.35 | 24.5 x 23.5 x 4.2 | 190 mAh | "Wire leads with connector", type not verified (datasheet host blocked, 403) | 48 / 35 days | 4.5 mm over in length and 3.5 mm over in width |

Not suitable: SparkFun 25270 (40 mAh, 22 x 11.5 x 3.5, DigiKey 1568-25270-ND, 225 in stock, $7.39; too long and too small, 10 / 7 days); Renata ICP501022UPM 80 mAh 24 x 10 x 5.5 (Mouser, 25 in stock; too long; 20 / 15 days). Two ASR00003 in parallel (2 x 5 mm, 300 mAh) would fit but is not recommended (two PCMs in parallel, unmatched cells).

Crown conclusion: 150 mAh is the ceiling for this envelope, so 28 to 38 days between charges is the honest figure.

## 5. Option B: Slab (envelope 6 to 10 x 34 x 50 mm)

| # | Part | Source / stock / price (2026-11-11) | Dims L x W x T (incl. PCM) | Capacity | Connector, polarity | Life 5 min / 1 min (80 %) | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| B1 | **US Electronics USE-803048-1100 mAh** (HPL803048 cell, PCM G3J+8205) | DigiKey 3544-USE-803048-1100mAh-ND, 620 in stock, $9.45 (1), $8.50 (100) | max 50.0 x 30.5 x 8.1 (spec "Product Dimension"; confirm the PCM end is inside the 50.0) | 1100 typ, **1050 min** | **JST PH-2P fitted**, red and black 26 AWG UL1571, 153 mm. Red = +; slot to verify against U4 | **268 / 193 days** | Best capacity, fits with room. 1C max charge, use 0.5C. Datasheet: https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/5562/USE-803048-1100%20MAH.pdf |
| B2 | **Adafruit 1578** (PKCell 503035 with PCM) | DigiKey 1528-1841-ND, 2,432 in stock, $7.95 | 29 x 36 x 4.8 (DigiKey); the 36 mm side must run along the 50 mm axis (34 mm width is exceeded otherwise) | 500 mAh | JST PH-2 fitted, Adafruit convention red = + | 128 / 92 days | Datasheet title "Li-Polymer 503035 500mAh 3.7V with PCM". Polarity expected to match PH convention, not verified against U4 |
| B3 | **Adafruit 3898** (PKCell LIPO 801735) | DigiKey 1528-2731-ND, 1,624 in stock, $6.95 | 37 x 17.5 x 8.2 | 400 mAh (380 min) | JST PH-2 fitted, same caveat | 102 / 74 days | Slim; fits the 34 mm width easily. Datasheet has protection-board section. https://cdn-shop.adafruit.com/product-files/3898/3898_specsheet_LP801735_400mAh_3.7V_20161129.pdf |

Also checked, not shortlisted: Adafruit 4236 (420 mAh, 35 x 24 x 5.2, DigiKey 1528-4236-ND, 491 in stock, $6.95, PH; 107 / 77 days, a fine B3 alternative); Adafruit 4237 (350 mAh, 32.5 x 25.4 x 5.0, 1528-4237-ND, $5.95); Jauch LP503040JH 600 mAh wire only (42 x 30.5 x 5.4, DigiKey 1908-LP503040JH+PCM+2WIRES50MM-ND, 1,601 in stock, $10.81); Jauch LP103048JU 1.43 Ah (50 x 30.5 x 11.0, 1 mm over the 10 mm height); GlobTek BL0750F5030481S1PCTC (700 mAh, 50.5 x 30.5 x 5.3) rejected: 3-wire pack with an NTC wire, not 2-wire. Adafruit 2011 (2000 mAh, 60 x 36 x 7) is too long for the slab.

## 6. Recommendation

For **Crown**, plan on **TinyCircuits ASR00003 (150 mAh, 20 x 20 x 5 mm, DigiKey 1832-1031-ND, $4.95)**. It is the largest cell with a PCM that meets the 20 x 20 envelope, stocked at both DigiKey and Mouser, and cheap. Budget a hand-fitted JST PH-2 plug (cut the SH plug off; the 12 mm lead is short), meter the polarity against U4 pad 1 before first plug-in, and set the nPM1300 charge current to 32 to 75 mA. Expect about 4 to 5 weeks per charge at 5 min readings and about 4 weeks at 1 min, because the 110 uA idle uses most of the energy. If Brian wants months, either the Crown pocket has to grow (A5, 190 mAh, needs 24.5 x 23.5 and still gives only about 5 to 7 weeks) or idle has to drop; no larger cell exists in the 10 x 20 x 20 mm class. For **Slab**, take **US Electronics USE-803048-1100 mAh (DigiKey 3544-USE-803048-1100mAh-ND)**: 1050 mAh minimum, PCM, PH-2P fitted, about 6 to 9 months, with Adafruit 1578 (500 mAh, 3 to 4 months) as the Adafruit-sourced fallback. Buy one spare of whichever cell is chosen so the first can be metered and bench-charged with the real nPM1300 settings before the enclosure is printed around it.

## 7. Unverified list

- nRF54L15 and nPM1300 datasheet current tables (only the Nordic product-page figures were read); nPM1300 ICHG minimum of 32 mA is from memory.
- XM125 wake-from-hibernate boot time and per-reading charge; BLE event durations (my assumptions).
- Cell capacities are labels (typical); minimums are 5 to 10 % lower where given (Jauch 60/65, US Electronics 1050/1100, Adafruit 3898 380/400).
- Whether each stated size includes the PCM and lead exit: Jauch and TinyCircuits list the finished pack, US Electronics lists the pack product dimension; no drawing was read here, so measure the first cell.
- Plug polarity of every candidate against U4 pin numbering.
- Renata ICP501421PS and MIKROE-2759 connector and PCM details; Mouser stock was read from search results only.
