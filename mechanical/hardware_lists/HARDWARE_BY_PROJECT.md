# Enclosure hardware by project (2026-11-14)

Parts-sourcing check. One document for the four enclosure projects, compared against what Brian owns, the Amazon purchase list and the Amazon cart.
Nothing was ordered or added to a cart. BOM Builder was read only.

<!-- SUMMARY_PLACEHOLDER -->

## Sources and how status was decided

Read 2026-11-14:
- Tidemark and Perch: `mechanical\tidemark\assembly_guide_2026-11-01\ASSEMBLY.md`, `mechanical\tidemark\NOTES.md`, `mechanical\tidemark\perch_2026-11-05\PERCH.md` and `perch_hardware_amazon_2026-11-05.md`, `mechanical\hardware_lists\tidemark_electronics_perch_2026-11-11.md` (+ its two CSVs).
- Ledger: `mechanical\ledger\assembly_guide_2026-11-01\ASSEMBLY.md`, `mechanical\ledger\NOTES.md`, `hardware\gateway\docs\lcd_module\cable_W1_wiring.md`, `hardware\gateway\sourcing\bom_digikey_mouser_2026-10-28_live.md`.
- Crown: `mechanical\hardware_lists\crown_2026-11-14.md` (reconciled today, reused here).
- Bench Tray: `mechanical\bench_tray\NOTES.md`; Amazon list items 10-11.
- Amazon list: `mechanical\hardware_lists\enclosure_hardware_amazon_2026-11-01.md` (items 1-17). Amazon cart (not ordered, 2026-11-14): B098QCD7TM, B0F6T5K1CW, B01F8PO7UK, B0BQD5QFP2, B0D29B9Z8G.
- Owned: `C:\Users\Brian\BOM_Builder\data\inventory.json` (file last written 2026-11-11 17:59, so it cannot show anything that arrived or was ordered after that). DigiKey order: `docs\purchasing\digikey_order_2026-11-10\`.
- McMaster variants (`enclosure_hardware_mcmaster_2026-11-01.md`, the `variant_mcmaster_*` folders) are an alternative that is not being bought; ignored.

Status words:
- **owned**: in inventory.json and delivered, or described as delivered. **arriving <date>**: in inventory.json with an arrival date (not yet confirmed on the bench).
- **in cart**: in the Amazon cart, not ordered. **check orders**: on the Amazon list, not in inventory.json, order status unknown (Brian to confirm).
- **to buy**: nothing ordered and nothing carted. **not tracked**: tools, consumables, filament, ties; inventory.json does not track them.

Kits are one inventory row each (Brian does not want kits split into rows). Piece counts for kits come from the listing contents in the existing lists, not from inventory, and are marked "listing". Kit contents that were never counted by hand are unverified.

All qty columns are per unit: 1 Tidemark node (feather + sensor board + Perch), 1 Ledger gateway, 1 Crown node, 1 Bench Tray. "Total qty" is the same as qty for one unit; the multiplier for N units is the qty column times N (the shared-stock section does 1 of each and the 5-feather order).

Distributor data: DigiKey via the kicad MCP (API) and Mouser via the kicad-pro stock tool (API, stock and 1-piece price only), read 2026-11-14.

## 1. pH / ORP node: Tidemark enclosure + Perch probe mount (per node)

Quantities are for 1 node. Each node needs its own full set (a pH node and an ORP node = 2 sets). The 5-feather order was 2 pH + 3 water level, so the Tidemark demand from that order is 2 sets (see the shared-stock section).

### Tidemark

| Item | Size | Qty / unit | Total qty (1 node) | Source | Status | Used in |
| --- | --- | --- | --- | --- | --- | --- |
| Brass heat-set insert | M2.5 x 4 mm L x 4 mm OD (3.6 mm hole) | 8 | 8 | Amazon B0DPQK6RJZ (pack of 100) | owned (100, delivered Nov 10) | ASSEMBLY prep 2 and 3: 4 sled posts, 4 plinth corners |
| Nylon M-F standoff, bottom of stack | M2.5, 8 mm, 6 mm male | 4 | 4 | MCMASKE kit B0B5M1M822 | arriving Nov 19 (15 on hand when it arrives) | Step 4: 8 mm standoff, male end through sens1 into the sled insert |
| Nylon M-F standoff, top of stack | M2.5, 6 mm, 6 mm male | 4 | 4 | MCMASKE kit B0B5M1M822 | arriving Nov 19 (15) | Step 4: 6 mm standoff on the 8 mm one (stack 14 mm) |
| Nylon pan head screw | M2.5 x 6 | 4 | 4 | MCMASKE kit B0B5M1M822 | arriving Nov 19 (50) | Step 5: main board into the 6 mm standoffs |
| Socket head cap screw, 304 stainless | M2.5 x 6 | 4 | 4 | Amazon B0GCSRG1WD (pack of 50) | **check orders** (not in inventory.json, not in the cart) | Step 11: foot cap to plinth inserts |
| Silicone o-ring cord, 70A | 2 mm, about 154 mm loop | 1 loop | 1 | Amazon B00QVB0ZG6 (10 ft) | arriving Nov 18 | Step 11: foot-cap o-ring, CA-glued |
| Silica gel packet | 1 g, about 30 x 20 x 3 mm | 1 | 1 | Amazon B0GSRKXHFT (pack of 100) | **check orders** | Step 10: slot between sled rib and sleeve left wall |
| ePTFE vent membrane | 6-10 mm disc over a 3.0 mm hole | 1 | 1 | Amazon B0F45VY7KK (100 sheets) | owned (100, delivered Nov 10) | Prep 5: cap vent |
| FFC, 14-way, 0.5 mm, 30 mm, Type D | Molex 0150200140 (29.97 mm) | 1 | 1 | DigiKey 0150200140-ND, $3.82 (1), $3.243 (10); stock 1,936 (Mouser 0) | **to buy** | Step 5: CN1 main to CN1 sens1. Thickness (0.30 mm) unconfirmed; test-fit before buying more |
| RG316 pigtail, RA SMA plug, IP68 SMA bulkhead jack | Molex 73230-7070, 152.4 mm | 1 | 1 | Mouser 73230-7070, $30.51, stock 49 (DigiKey 0 stock, $23.88 listed, MOQ 200) | **to buy** | Step 8 and step 11: sens1 J1 to the heel bulkhead. 152 mm vs the 60-80 mm assumed: coil room unchecked |
| LiPo cell with JST PH 2-pin | 602050 (6 x 20 x 50 mm), red on U4 pad 1 | 1 | 1 | none at DigiKey or Mouser | **to buy, no source** | Step 7: back of the sled |
| Thin foam | some | some | some | any | not tracked | Step 7: wrap the battery |

### Perch (probe mount, 1 per node)

| Item | Size | Qty / unit | Total qty (1 node) | Source | Status | Used in |
| --- | --- | --- | --- | --- | --- | --- |
| Nylon thumbscrew, spade head | M6 x 30 | 1 | 1 | Amazon B0DCZTKMDG (pack of 10) | owned (10, delivered Nov 10) | PERCH.md: wall clamp through the leg |
| Nylon hex nut | M6, 10 mm AF x 5 | 1 | 1 | Amazon B097R2W2VS (20 pair set) | owned (nuts 20, bolts 20, delivered Nov 11) | Captive in the hex pocket of the leg. Check the nut fits the 10.3 mm AF pocket |
| Nylon pan head screw | M4 x 25 | 1 | 1 | HVAZI kit B098QDHCDP | owned (kit delivered Nov 11; 20 per length, listing) | Collet clamp |
| Nylon hex nut | M4, 7 mm AF x 3.2 | 1 | 1 | HVAZI kit B098QDHCDP (80 nuts, listing) | owned | Captive in the Collet |
| Nylon pan head screw | M4 x 10 | 2 | 2 | HVAZI kit B098QDHCDP (20, listing) | owned | Collet stops, self-tap into 3.4 mm holes |

The Essentra DigiKey picks for the Perch (Amazon list rows 13-17, `tidemark_electronics_perch_2026-11-11.md` items 5a-5e and the DigiKey CSV lines for them) are **not needed**: the Perch parts above were bought on Amazon (inventory.json) and the Amazon list/CSV were never updated.

DigiKey 2026-11-10 order: no Tidemark/Perch enclosure items in it. Its 5034801400 line is the CN1 board connector, not the FFC cable. The FFC cable, pigtail and cell are still open.

Tidemark guide steps not hardware: solar panel (LL200-2.4-75) and leaf card are electronics/print parts, not counted here.

## 2. Pouch gateway: Ledger enclosure (per gateway)

Quantities for 1 gateway. The 2026-11-10 DigiKey upload was for 5 gateways; only 1 LCD is owned.

| Item | Size | Qty / unit | Total qty (1 unit) | Source | Status | Used in |
| --- | --- | --- | --- | --- | --- | --- |
| Brass heat-set insert, M2 | 4 mm L, hole 3.2 mm in the model | 8 | 8 | Amazon list B088QJG676 (ruthex RX-M2x4); inventory has **B08T7NDPQC** (in-saiL, 4 mm L x 3.6 mm OD) bought in its place | owned via the substitute (100; inventory says arriving Nov 13, probably here, confirm). B088QJG676 itself is not needed | Prep 2: 4 gateway-board bosses + 4 rear-cover corner bosses. Check 3.6 mm OD against the 3.2 mm boss holes (see mismatches) |
| M2 x 5 button head hex screw, 304 stainless | M2 x 5 | 8 | 8 | Amazon B0DLKCR1CQ (pack of 100) | owned (100, delivered Nov 11) | Step 6 (gateway board, 4) and step 8 (rear cover, 4) |
| M2 x 5 self-tapping Phillips pan head, 316 stainless | M2 x 5 | 4 | 4 | Amazon B07Q36GBKY (pack of 50) | arriving about Nov 17 | Step 5: LCD module, 1.6 mm pilot holes |
| Waveshare 2inch LCD module, ST7789, SPI | B082GFTZQD (SKU 17344), PH2.0 8-pin 20 cm cable included but replaced by W1 | 1 | 1 | Amazon B082GFTZQD | owned (1, delivered Nov 10) | Step 5 |
| W1 housing | JST PHR-8 | 2 | 2 | DigiKey 455-1189-ND, $0.11 (1), stock 761 (2026-11-14) | **check orders**: in the 2026-11-10 DigiKey upload (13 in the full CSV, 10 in the lean CSV, for 5 gateways); placement of that order not confirmed in the repo | Step 4: cable W1, J5 to LCD |
| W1 lead | JST ASPHSPH24K102 (102 mm, pre-crimped) | 8 | 8 | DigiKey 455-3358-ND, stock 38,896, $0.40 at 1 piece (2026-11-14); the order file priced 45 at $0.3208 | **check orders**: in the same upload (45 full, 40 lean) | Step 4: probably wired reversed (slot n to 9-n); continuity-check before fitting the second housing |
| Thin double-sided adhesive ring or CA dots | | some | some | any | not tracked | Step 2: bezel insert |

If the 2026-11-10 DigiKey order was not placed, the single-gateway W1 buy is 10 leads + 3 housings = $3.75 (`hardware\gateway\sourcing`, 2026-10-29; DigiKey prices today are within a few cents: PHR-8 $0.11 at 1).
Not enclosure hardware: the 100 mm antenna 146153-0100 and U.FL for the Ledger are gateway BOM parts (in the 2026-11-10 upload).

## 3. Water level node: Crown + dock + A6 / A2 / A5 plates (per node)

Reused from `crown_2026-11-14.md` (reconciled 2026-11-14; its full table, bench checks and distributor notes are there). Quantities are for 1 Crown with the default build: printed A2 bars, one dock ring, plates built as needed (A6 and A5 and A2 each moved on the dock).

| Item | Size | Qty / unit | Total qty (1 node) | Source | Status | Used in |
| --- | --- | --- | --- | --- | --- | --- |
| Brass heat-set insert | M2.5 x 4 x 4 OD | 8 (F1 plinth 4, F3 roof 4) | 8 | Amazon B0DPQK6RJZ | owned | Crown hood |
| Brass heat-set insert (dock ring bosses) | M2.5 x 4 x 4 OD | 4 (F8) | 4 | B0DPQK6RJZ | owned | Dock ring |
| Socket head cap screw, 304 stainless | M2.5 x 6 | 4 (F2) | 4 | Amazon B0GCSRG1WD | **check orders** (same pack as Tidemark) | Sole to hood |
| Nylon pan head screw | M2.5 x 10 | 8 (F5 board stack 4, F4 bonnet 4) | 8 | MCMASKE kit B0B5M1M822 (50, listing) | arriving Nov 19 (count uncertain, listing only) | Board stack, bonnet |
| Nylon M-F standoff | M2.5, 8 mm body | 4 (F6) | 4 | MCMASKE kit | arriving Nov 19 | Board stack |
| Nylon hex nut | M2.5 about 5 AF | 4 (F7) | 4 | MCMASKE kit (nuts, count not itemised) | arriving Nov 19 (uncertain) | |
| Nylon pan head screw, plate to ring | M2.5 x 5 (cut from M2.5 x 6) | 4 (F9; 16 if all four plates stay built) | 4 | MCMASKE kit M2.5 x 6 | arriving Nov 19 | Dock: A6/A5/A2 plate to ring; cut 1.0 mm off |
| FFC, 14-way, 0.5 mm, 30 mm, Type D | Molex 0150200140 | 1 | 1 | DigiKey 0150200140-ND, $3.82 | **to buy** | Crown board stack |
| LiPo cell | TinyCircuits ASR00003, 20.1 x 20.1 x 5.1, JST SH (cut off), 150 mAh | 1 | 1 | DigiKey 1832-1031-ND, $4.95, stock 103 (Mouser 349 at $4.95) | **to buy** | Battery. 150 mAh only |
| Battery pigtail leads | JST PH 2-pin, 28 AWG, 150 mm | 1 | 1 | Amazon B0F6T5K1CW (60 pair), $9.99 | in cart | Trim to 40-45 mm |
| Silicone hook-up wire | 28 AWG red and black | 2 pieces | 2 | Amazon B01F8PO7UK, $6.48 | in cart, optional (spare if the pigtail leads are used) | |
| Heat-shrink | about 1.5 mm | 2 | 2 | any | not tracked | |
| A6 gasket ring, closed-cell neoprene | ID 34, OD 54, 1.5 mm | 1 | 1 | Amazon B0BQD5QFP2 (4 x 4 in x 22), $8.59 | in cart | A6 Pad. 1/16 in = 1.59 mm |
| Nylon pan head screw (F10, optional) | M4 x 12 | 2 | 2 | HVAZI M4 kit B098QDHCDP | owned (kit delivered Nov 11; listing 20 each) | A6 ear screws |
| Nylon hex nut (F10) | M4 | 2 | 2 | HVAZI kit | owned | A6 |
| Bull's-eye level vial | 15 x 8 mm | 1 | 1 | Amazon B0D29B9Z8G (pack of 5), $4.55 | in cart | Moves between plates. Check room on the Crown face |
| Nylon pan head screw (F11/F12) | M4 x 10 | 4 printed bars (8 stock bars) | 4 | HVAZI kit | owned | A2 clip bridges, end caps |
| Stock flat bar, UHMW | 3/8 x 3/4 in x 702 mm | 2 (only for rim over 430 mm) | 0 (optional 2) | Amazon B07GBGSG1Y, $31.52 each | optional, to buy only if needed | A2 stock version |
| Nylon pan head screw (F13) | M3 x 12 | 3 | 3 | HVAZI M3 kit B098QCD7TM (M3 x 6-25, 80 nuts), $9.99 | in cart | A5 Expander |
| Nylon hex nut (F14) | M3, 5.5 AF x 2.4 | 3 | 3 | same kit | in cart | A5. Reviewer measured 2.84 mm thick vs a 2.5 mm pocket |
| TPU 95A filament | A5 ring | 1 | 1 | on hand | not tracked | A5 |

Tools for the Crown (iron, hex key 2.0, driver, nut driver, cutters, calipers, compass cutter, 3.4 mm drill) are not tracked in inventory.json and not counted.

## 4. Programming adapter: Bench Tray (per tray)

Source is `mechanical\bench_tray\NOTES.md` plus Amazon list items 10-11. There is no assembly guide, only NOTES. The Fusion model has 4 insert holes (4.1 x 5 mm) and 2 more for an unused riser.

| Item | Size | Qty / unit | Total qty (1 tray) | Source | Status | Used in |
| --- | --- | --- | --- | --- | --- | --- |
| Brass heat-set insert | M3 x 4 mm L x 5 mm OD | 4 (+2 for a riser later) | 4 (6 with the riser) | Amazon B0FDKYTMZ8 (pack of 100, model 242707-US); price not read (page 503 on 2026-11-07 and 2026-11-14) | **check orders** | Corner posts at H1-H4 |
| Button head socket screw, 304 stainless | M3 x 6 (M3 x 5 also works) | 4 | 4 | not picked, no ASIN. Stand-in for nylon: the HVAZI M3 kit (cart) has M3 x 6 Phillips pan head nylon, a different head and material | **to buy** (to pick) | Board to posts |
| Cable tie | 2.5 mm wide | 1-2 | 1-2 | any | not tracked | J7 board slots and the strain-relief tab |
| TPU 95A for feet or stick-on feet | 8-10 mm square | 4 feet | 4 | on hand / any | not tracked, optional | Feet pockets |

DigiKey 2026-11-10 order: no Bench Tray items. The Tag-Connect TC2030-IDC (DigiKey TC2030-IDC-ND, $44.58 in the order file) is a programming tool, not enclosure hardware, and is not counted.

## 5. Shared stock: items used by more than one project

Demand is shown for two cases. **A** = one of each project (1 Tidemark node, 1 Ledger, 1 Crown, 1 Bench Tray). **B** = the 5-feather order (2 pH nodes in Tidemark + 3 water level nodes in Crown), plus 1 Ledger and 1 Bench Tray. In B each Crown has its own dock ring and A2, and the A6/A5 plates are built once per Crown.
On hand = inventory.json (or the listing, for kit sub-items; marked "listing"), including items still arriving.

| Stock | On hand | Tidemark + Perch (per node) | Crown (per node) | Other | Demand A | Demand B | Verdict |
| --- | --- | --- | --- | --- | --- | --- | --- |
| B0DPQK6RJZ M2.5 inserts | 100 | 8 | 12 (8 hood + 4 dock) | | 20 | 52 (16 + 36) | OK |
| MCMASKE kit, 8 mm standoffs | 15 (arriving Nov 19) | 4 | 4 | | 8 | 20 (8 + 12) | **Short 5 in B** (OK in A, and OK up to 2 Tidemark + 2 Crown) |
| MCMASKE kit, 6 mm standoffs | 15 (arriving Nov 19) | 4 | 0 | | 4 | 8 | OK |
| MCMASKE kit, nylon M2.5 x 6 | 50 (arriving Nov 19) | 4 | 4 (16 if all plates stay built) | | 8 (20 worst) | 20 (56 worst: 8 + 48) | OK, except short by 6 in B if every plate stays built on every Crown |
| MCMASKE kit, nylon M2.5 x 10 | 50 (listing) | 0 | 8 | | 8 | 24 | OK (listing only) |
| MCMASKE kit, M2.5 nuts | not itemised | 0 | 4 | | 4 | 12 | Unknown (count not in inventory) |
| B0GCSRG1WD M2.5 x 6 stainless | 0 in inventory (check orders); pack of 50 | 4 | 4 | | 8 | 20 | **Not owned**: one pack covers A and B if it was ordered or is bought |
| B0GSRKXHFT silica 1 g | 0 in inventory (check orders); pack of 100 | 1 | 0 | | 1 | 2 | Not owned, one pack covers it |
| B0F45VY7KK vent membrane | 100 | 1 | 0 | | 1 | 2 | OK |
| B00QVB0ZG6 o-ring cord | 1 x 10 ft (arriving Nov 18) | 1 loop (~154 mm) | 0 | | 1 loop | 2 loops | OK (about 19 loops per 10 ft) |
| HVAZI M4 kit B098QDHCDP, M4 x 25 | 20 (listing) | 1 | 0 | | 1 | 2 | OK |
| HVAZI M4 kit, M4 x 10 | 20 (listing) | 2 | 4 printed (8 stock bars) | | 6 (10 stock) | 16 (28 stock bars) | OK with printed bars; **short 8 in B if all three Crowns use stock bars** |
| HVAZI M4 kit, M4 x 12 | 20 (listing) | 0 | 2 | | 2 | 6 | OK |
| HVAZI M4 kit, M4 nuts | 80 (listing) | 1 | 2 (A6) | | 3 | 8 | OK |
| B097R2W2VS M6 nuts / B0DCZTKMDG M6 x 30 | 20 / 10 | 1 / 1 | 0 | | 1 / 1 | 2 / 2 | OK |
| M2 inserts B08T7NDPQC | 100 | 0 | 0 | Ledger 8 | 8 | 8 | OK |
| B0DLKCR1CQ M2 x 5 button head / B07Q36GBKY PT screws | 100 / 50 (arriving ~Nov 17) | 0 | 0 | Ledger 8 / 4 | 8 / 4 | 8 / 4 | OK |
| HVAZI M3 kit B098QCD7TM (cart) | 0, in cart | 0 | 3 screws + 3 nuts (A5) | Bench Tray 4 if nylon M3 x 6 is accepted | 3 to 7 | 9 to 13 | OK if the listing contents hold (80 nuts, M3 x 6-25); not bought yet |
| B0FDKYTMZ8 M3 inserts | 0 in inventory (check orders), pack of 100 | 0 | 0 | Bench Tray 4 (6) | 4 | 4 (6) | Not owned |
| FFC Molex 0150200140 | 0 | 1 | 1 | | 2 | 5 | To buy: $3.82 each (1), $3.243 at 10 |
| TPU filament | not tracked | 0 | A5 ring | Bench Tray feet (optional) | | | on hand |

Notes: a Crown node shares the Tidemark's inserts, MCMASKE standoffs and screws, the stainless M2.5 x 6 pack, and the HVAZI M4 kit. Nothing is shared with the Ledger or Bench Tray except the M3 kit (cart) if nylon M3 x 6 is acceptable for the tray.

## 6. Mismatches between guides, lists and inventory

1. **Ledger inserts.** Amazon list item 1 and the Ledger ASSEMBLY.md name ruthex B088QJG676 (3.2 mm hole). inventory.json has B08T7NDPQC (in-saiL, 4 mm L x 3.6 mm OD), noted "bought in place of ruthex B088QJG676". The Ledger bosses have 3.2 mm holes (NOTES.md). A 3.6 mm OD insert normally needs a hole about its OD or a little under; check the in-saiL listing's recommended hole before heat-setting. If it asks for more than 3.2 mm, the Ledger model needs 3.4-3.6 mm holes or the ruthex inserts are needed after all. Guide and Amazon list were not updated.
2. **Perch hardware, three sources disagree.** `perch_hardware_amazon_2026-11-05.md` (B0DCZTKMDG, B097R2W2VS, B098QDHCDP) is what inventory.json shows bought. The main Amazon list rows 13-17 and `tidemark_electronics_perch_2026-11-11.md` items 5a-5e (and the DigiKey CSV lines for them) replaced those with Essentra DigiKey parts. Those Essentra parts are not needed. The DigiKey CSV `tidemark_electronics_perch_digikey_2026-11-11.csv` would still add 6 Perch lines if uploaded as is (only the FFC line is still needed).
3. **Amazon list is stale.** It says nothing was ordered; inventory.json shows 13 of its items delivered, arriving or substituted. Header total ($86) and items 1-9 do not reflect that. B0GCSRG1WD, B0GSRKXHFT, B0FDKYTMZ8 are on it and not in inventory.
4. **Dates in inventory.json.** The file was last written 2026-11-11 17:59. Items marked "arriving Nov 13" (B08T7NDPQC M2 inserts, B0F2ZBN1K9 1/4-20 inserts) are past due today and probably delivered but not updated; Nov 17-19 items (B07Q36GBKY, B00QVB0ZG6 Nov 18, MCMASKE kit Nov 19) are still ahead. B0F2ZBN1K9 is not used by any enclosure here.
5. **MCMASKE kit is treated as owned in the guides** (Tidemark ASSEMBLY.md, Crown ASSEMBLY.md "listed"). It arrives Nov 19, so nothing that uses standoffs, nylon M2.5 screws or M2.5 nuts can be built before then.
6. **B0GCSRG1WD.** The Tidemark ASSEMBLY.md and Crown ASSEMBLY.md treat it as an Amazon-list item; it is not in inventory.json and not in the cart (Crown doc says the same).
7. **Crown ASSEMBLY.md section 2.2 versus its cart note.** Section 2.2 says buy 8 Essentra M4 x 10 screws and M4 nuts at DigiKey; the cart note and this document use the owned HVAZI M4 kit (delivered Nov 11, contents from the listing, unmeasured). Inventory itself says "check the kit has a 25 mm length"; the Perch Amazon note says the kit has M4 x 6-30 mm, 20 each. Both are from the listing.
8. **Crown pigtail.** Section 2.2 says PHR-2 housing + contacts + silicone wire; the cart has pre-crimped PVC leads (B0F6T5K1CW), so the silicone wire (B01F8PO7UK, $6.48) is optional.
9. **Bench Tray.** NOTES.md lists "4 (+2 for a riser later)" M3 inserts; Amazon list item 10 says 4. NOTES says M3 x 6 (M3 x 5 also works); item 11 is still "to pick". The M3 insert page returned 503 on 2026-11-07 and again on 2026-11-14, so its price and OD (model uses a 4.1 mm hole, 5 mm OD) were never read.
10. **Ledger W1.** Ledger ASSEMBLY.md says cable W1 is 60-80 mm "(in the gateway BOM)"; the BOM now uses the 102 mm ASPHSPH24K102 lead (20-40 mm over; per `cable_W1_wiring.md`, which also says gateway DESIGN_NOTES.md still shows the 152 mm lead and 1:1 wiring). The DigiKey upload has three versions (full 45 leads / 13 housings, lean 40 / 10, add-on); which one was uploaded is not recorded. Either covers 5 gateways.
11. **Tidemark pigtail length.** ASSEMBLY.md assumes 60-80 mm; Molex 73230-7070 is 152.4 mm (guide row notes it). Coil room in the heel is not checked. Also the 602050 cell has no source at DigiKey or Mouser.
12. **DigiKey 73230-7070.** The 2026-11-11 list says DigiKey 900-0732307070-ND, 0 stock, MOQ 200. The API today returns DigiKey 0732307070, stock 0, $23.88 listed. Mouser has 49 at $30.51. Use Mouser.
13. **M3 nut thickness (Crown A5)** measured 2.84 mm by a reviewer against a 2.5 mm pocket: open bench check, not a list mismatch.

