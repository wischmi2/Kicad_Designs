# ORP: parts reconciliation, 2026-11-22

Schematic: `hardware/sensors/orp/` at HEAD (kicad-cli 10 `sch export bom`, run 2026-11-22). Boards counted: 5 (bare boards ordered 5; build count unknown, so need = 5 x per-board qty).
Sources: schematic fields; sourcing BOM in hardware/sensors/orp/sourcing (MPN column = 2026-10-30/11-08/11-07 CSV, swaps = 2026-10-28 live CSV); the 11-10 plan (order_2026-11-10.md); what was ordered (BB shopping_list.json Ordered notes, last saved 2026-11-11 19:20, and the carts in tobuy); on hand (BB inventory.json, last saved 2026-11-11 17:59). Stock checked live 2026-11-22.

Counts (lines = groups of identical parts, refs in brackets): MISSING 3 (3), CHECK 1 (1), OK 14 (20), DNP 1 (1)

## Problems

| Verdict | Refs | Schematic | Ordered | On hand | Need | Note |
|---|---|---|---|---|---|---|
| MISSING | R1 | 47k R0402 RC0402FR-0747KL | - | - | 5 | R1 is 47k since 2026-11-11; not bought. DigiKey 0 stock; Mouser 3.27 M ($0.10). DigiKey drop-in ERJ-2RKF4702X (47k 1% 0402) 1.25 M stock. On-hand CRCW060347K0FKEC is 0603. [short by 5 vs pool/line demand 5] |
| MISSING | U2 | Atlas_ORP_OEM Atlas_ORP_OEM OEM-ORP | - | - | 5 | Atlas Scientific OEM-ORP: no order or stock record in any source (Atlas sells direct only). Need 5. [short by 5 vs demand 5] |
| MISSING | U3 | ISO1540DR SOIC-8_3.9x4.9mm_P1.27mm ISO1540DR | ISO1540DR x2 [DK] | - | 5 | Ordered 2 only (both on backorder per BB note; cart file had 5). Need 5. DigiKey 0 and Mouser 0 today. Alternative ADuM1250ARZ-RL7 (pH part) is DigiKey 0 too: look for ISO1541 / ISO1540 at other distributors. [short by 3 vs pool/line demand 5] |
| CHECK | J1 | SMA (ORP probe) SMA_BAT_Wireless_BWSMA-KWE-Z001 BWSMA-KWE-Z001 | - | SuperBat X0036NHOHB x9 | 5 (pool 7) | BAT Wireless BWSMA-KWE-Z001 is not at DigiKey/Mouser (LCSC C496551 per 11-10 md; no order recorded). On hand 9 x SuperBat X0036NHOHB (SMA edge-mount, Amazon): geometry vs the BWSMA footprint not verified. Pool need pH 2 + ORP 5 = 7. |

## All parts

| Refs | Value / footprint | Sch MPN | Sourcing BOM MPN | 11-10 plan (whole-line buy qty) | Ordered (BB notes, whole-line qty) | On hand | Need | Stock 11-22 (write-back MPN) | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| R1 | 47k R0402 | RC0402FR-0747KL | RC0402FR-0747KL (live swap: RC0402FR-074K7L) | - | - | - | 5 | DK 0 / MO 3,273,787 | MISSING |
| U2 | Atlas_ORP_OEM Atlas_ORP_OEM | OEM-ORP | OEM-ORP | - | - | - | 5 | DK n/a / MO n/a | MISSING |
| U3 | ISO1540DR SOIC-8_3.9x4.9mm_P1.27mm | ISO1540DR | ISO1540DR | - | ISO1540DR x2 [DK] | - | 5 | DK 0 / MO 0 | MISSING |
| J1 | SMA (ORP probe) SMA_BAT_Wireless_BWSMA-KWE-Z001 | BWSMA-KWE-Z001 | BWSMA-KWE-Z001 | - | - | SuperBat X0036NHOHB x9 | 5 (pool 7) | DK n/a / MO n/a | CHECK |
| C1,C5 | 1uF C0402 | CL05A105KO5NNNC | CL05A105KO5NNNC | - | CL05A105KO5NNNC x27 [MO] | CL05A105KO5NNNC x13 | 10 (pool 28) | DK 0 / MO 1,346 | OK |
| C10 | 10nF C_0402_1005Metric | GRM155R71H103KA88D | GRM155R71H103KA88D | - | GCM155R71H103KA55D x2 [DK] | GCM155R71H103KA55D x8 | 5 (pool 10) | DK 1,465,276 / MO 3,808,466 | OK |
| C11 | 4.7uF 25V C_0603_1608Metric | GRM188R61E475KE11D | GRM188R61E475KE11D | - | GRM188R61E475KE11D x5 [DK] | - | 5 | DK 135,357 / MO 0 | OK |
| C2,C4 | 100nF C0603 | CC0603KRX7R9BB104 | CC0603KRX7R9BB104 | - | GRM188R72A104KA35D x24 [MO] | GRM188R72A104KA35D x21 | 10 (pool 37) | DK 85,912 / MO 1,361,404 | OK |
| C3 | 2.2uF C0603 | GRM188R71A225KE15D | GRM188R71A225KE15D | - | GRM188R71A225KE15D x10 [DK] | - | 5 (pool 7) | DK 889,277 / MO 1,397 | OK |
| C6,C9,C12 | 100nF C_0402_1005Metric | GRM155R71C104KA88D | GRM155R71C104KA88D | - | GCM155R71C104KA55D x100 [DK] | - | 15 (pool 82) | DK 3,503,855 / MO 0 | OK |
| C7,C8 | 10uF 25V C_0805_2012Metric | GRM21BR61E106MA73L | GRM21BR61E106MA73L | - | GRM21BR61E106MA73L x35 [MO] | GRM21BR61E106KA73K x1000 | 10 (pool 35) | DK 47,989 / MO 6,545 | OK |
| CN1 | 503480-1400 Molex_503480-1400_1x14-1MP_P0.50mm_Horizontal | 503480-1400 | 503480-1400 | - | 5034801400 x25 [DK] | - | 5 (pool 15) | DK 26,283 / MO 16,510 | OK |
| D1 | BAT54CLT1G SOT-23 | BAT54CLT1G | BAT54CLT1G | - | BAT54CLT1G x5 [DK] | - | 5 | DK 569,514 / MO 0 | OK |
| FB1 | 220R@100MHz L_0603_1608Metric | BLM18PG221SN1D | BLM18PG221SN1D | - | BLM18PG221SN1D x5 [DK] | - | 5 | DK 180,533 / MO 182,710 | OK |
| R3,R4 | 4.7k R0402 | CRCW04024K70FKED | CRCW04024K70FKED | - | RC0402FR-074K7L x10 [DK] | RC0402FR-074K7L x39 | 10 (pool 34) | DK 320,000 / MO 4,737,940 | OK |
| T1 | 760390015 WE-PPTI_760390015 | 760390015 | 760390015 | - | 760390015 x5 [DK] | - | 5 | DK 12,032 / MO 26,602 | OK |
| U5 | SN6505BDBVR SOT-23-6 | SN6505BDBVR | SN6505BDBVR | - | SN6505BDBVR x5 [MO] | - | 5 | DK 0 / MO 108 | OK |
| U6 | LP2985-33DBVR SOT-23-5 | LP2985-33DBVR | LP2985-33DBVR | - | LP2985-33DBVR x5 [DK] | - | 5 | DK 34,059 / MO 538 | OK |
| R5 | 0 R0402 | ERJ-2GE0R00X DNP | - | - | ERJ-2GE0R00X x25 [DK] | - | 0 | - | DNP |

## Notes per line

- R1 (MISSING): R1 is 47k since 2026-11-11; not bought. DigiKey 0 stock; Mouser 3.27 M ($0.10). DigiKey drop-in ERJ-2RKF4702X (47k 1% 0402) 1.25 M stock. On-hand CRCW060347K0FKEC is 0603. [short by 5 vs pool/line demand 5]
- U2 (MISSING): Atlas Scientific OEM-ORP: no order or stock record in any source (Atlas sells direct only). Need 5. [short by 5 vs demand 5]
- U3 (MISSING): Ordered 2 only (both on backorder per BB note; cart file had 5). Need 5. DigiKey 0 and Mouser 0 today. Alternative ADuM1250ARZ-RL7 (pH part) is DigiKey 0 too: look for ISO1541 / ISO1540 at other distributors. [short by 3 vs pool/line demand 5]
- J1 (CHECK): BAT Wireless BWSMA-KWE-Z001 is not at DigiKey/Mouser (LCSC C496551 per 11-10 md; no order recorded). On hand 9 x SuperBat X0036NHOHB (SMA edge-mount, Amazon): geometry vs the BWSMA footprint not verified. Pool need pH 2 + ORP 5 = 7.
- C10 (OK): BB standardisation to GCM155R71H103KA55D (10 nF 50 V X7R 0402).
- C11 (OK): DigiKey x5 exact.
- C3 (OK): DigiKey x10 shared with pH C3.
- C6,C9,C12 (OK): BB standardisation 2026-11-09 to GCM155R71C104KA55D (0.1 uF 16 V X7R 0402, same spec).
- D1 (OK): DigiKey x5 exact.
- FB1 (OK): DigiKey x5 exact.
- R3,R4 (OK): BB standardisation from CRCW04024K70FKED (4.7k 1% 0402, same spec).
- T1 (OK): DigiKey x5 exact (Wurth transformer).
- U5 (OK): Mouser x5 exact (stock 108).
- U6 (OK): DigiKey x5 exact.
- R5 (DNP): DNP (R5 not fitted); ERJ-2GE0R00X x25 already bought for the gateway.

## BOM Builder needs file vs schematic

MPNs match the schematic for every ref in the needs file.
BB needs file board_count is 5 for this board.

Write-back proposal: `orp_writeback.csv`.
