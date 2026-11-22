# Water level TC2030: parts reconciliation, 2026-11-22

Schematic: `hardware/sensors/water_level_tc2030/` at HEAD (kicad-cli 10 `sch export bom`, run 2026-11-22). Boards counted: 3.
Sources: schematic fields; sourcing BOM in hardware/sensors/water_level_tc2030/sourcing (MPN column = 2026-10-30/11-08/11-07 CSV, swaps = 2026-10-28 live CSV); the 11-10 plan (order_2026-11-10.md); what was ordered (BB shopping_list.json Ordered notes, last saved 2026-11-11 19:20, and the carts in tobuy); on hand (BB inventory.json, last saved 2026-11-11 17:59). Stock checked live 2026-11-22.

Counts (lines = groups of identical parts, refs in brackets): WRONG 1 (1), MISSING 1 (1), CHECK 1 (1), OK 9 (18)

## Problems

| Verdict | Refs | Schematic | Ordered | On hand | Need | Note |
|---|---|---|---|---|---|---|
| WRONG | R1 | 220k R0402 RC0402FR-07220KL | - | - | 3 | R1 is 220k since 2026-11-11. The carts hold 22k parts (ERJ-2RKF2202X x10 DigiKey, RC0402FR-0722KL x5 Mouser) bought for the old 22k value: wrong value. 220k not bought. DigiKey 967,410, Mouser plenty. [short by 3 vs demand 3] |
| MISSING | U1 | XM125 Acconeer_XM125 XM125 | XM125 x2 [MO] | - | 3 | Brian ordered 2 on Mouser (BB note; cart file had 5), need 3. Mouser 1,642 today; DigiKey 0. [short by 1 vs pool/line demand 3] |
| CHECK | Q1 | BSS138LT1G SOT-23 BSS138LT1G | BSS138LT1G x5 [MO] | - | 3 | BB note says Mouser 41073583 x5, but the Mouser cart file in tobuy has no BSS138LT1G (the DigiKey cart line has 0 stock). Confirm the Mouser order. Today: DigiKey 872,892, Mouser 3,022. |
| EXTRA | - | RC0402FR-0722KL x5 (Mouser 41073583) | - | - | - | Bought for the old 22k R_ID; R1 is 220k now. Nothing at HEAD uses it (gateway R4 takes the DigiKey 22k part instead). |

## All parts

| Refs | Value / footprint | Sch MPN | Sourcing BOM MPN | 11-10 plan (whole-line buy qty) | Ordered (BB notes, whole-line qty) | On hand | Need | Stock 11-22 (write-back MPN) | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| R1 | 220k R0402 | RC0402FR-07220KL | RC0402FR-07220KL | ERJ-2RKF2202X x18 | - | - | 3 | DK 967,410 / MO 792,810 | WRONG |
| U1 | XM125 Acconeer_XM125 | XM125 | XM125 | XM125 x3 | XM125 x2 [MO] | - | 3 | DK 0 / MO 1,642 | MISSING |
| Q1 | BSS138LT1G SOT-23 | BSS138LT1G | BSS138LT1G | BSS138-7-F x5 | BSS138LT1G x5 [MO] | - | 3 | DK 872,892 / MO 3,022 | CHECK |
| C1,C3,C4 | 1uF C0402 | CL05A105KO5NNNC | CL05A105KO5NNNC | GRM155R61C105KA12D x28 | CL05A105KO5NNNC x27 [MO] | CL05A105KO5NNNC x13 | 9 (pool 28) | DK 0 / MO 1,346 | OK |
| C2 | 100nF C0603 | CC0603KRX7R9BB104 | CC0603KRX7R9BB104 | CC0603KRX7R9BB104 x50 | GRM188R72A104KA35D x24 [MO] | GRM188R72A104KA35D x21 | 3 (pool 37) | DK 85,912 / MO 1,361,404 | OK |
| C5 | 10uF C_0402_1005Metric | GRM155R60J106ME15D | GRM155R60J106ME15D | GRM155R60J106ME15D x23 | GRM155R60J106ME15D x15 [DK] | GRM155R60J106ME15J x9 | 3 (pool 13) | DK 1,826,511 / MO 2,698,042 | OK |
| C6,C7,C8,C9,C10 | 100nF C_0402_1005Metric | GRM155R71A104KA01D | GRM155R71A104KA01D | GCM155R71C104KA55D x100 | GRM155R71A104KA01D x25 [DK] | - | 15 | DK 1,164,489 / MO 0 | OK |
| CN1 | 503480-1400 Molex_503480-1400_1x14-1MP_P0.50mm_Horizontal | 503480-1400 | 503480-1400 | 5034801400 x11 | 5034801400 x25 [DK] | - | 3 (pool 15) | DK 26,283 / MO 16,510 | OK |
| R2,R3,R4 | 100k R_0402_1005Metric | RC0402FR-07100KL | RC0402FR-07100KL | RC0402FR-07100KL x25 | RC0402FR-07100KL x25 [DK] | - | 9 (pool 16) | DK 3,692,494 / MO 15,492,618 | OK |
| U2 | NCP161ASN180T1G SOT-23-5 | NCP161ASN180T1G | NCP161ASN180T1G | NCP161ASN180T1G x4 | NCP161ASN180T1G x5 [DK] | - | 3 | DK 52,250 / MO 25,844 | OK |
| U3 | TCA9406DCTR SSOP-8_2.95x2.8mm_P0.65mm | TCA9406DCTR | TCA9406DCTR | TCA9406DCTR x4 | TCA9406DCTR x5 [DK] | - | 3 | DK 16,980 / MO 18,130 | OK |
| U4,U5 | SN74AXC1T45DBVR SOT-23-6 | SN74AXC1T45DBVR | SN74AXC1T45DBVR | SN74AXC1T45DBVR x10 | SN74AXC1T45DBVR x10 [DK] | - | 6 | DK 31,020 / MO 13,910 | OK |

## Notes per line

- R1 (WRONG): R1 is 220k since 2026-11-11. The carts hold 22k parts (ERJ-2RKF2202X x10 DigiKey, RC0402FR-0722KL x5 Mouser) bought for the old 22k value: wrong value. 220k not bought. DigiKey 967,410, Mouser plenty. [short by 3 vs demand 3]
- U1 (MISSING): Brian ordered 2 on Mouser (BB note; cart file had 5), need 3. Mouser 1,642 today; DigiKey 0. [short by 1 vs pool/line demand 3]
- Q1 (CHECK): BB note says Mouser 41073583 x5, but the Mouser cart file in tobuy has no BSS138LT1G (the DigiKey cart line has 0 stock). Confirm the Mouser order. Today: DigiKey 872,892, Mouser 3,022.
- C1,C3,C4 (OK): Shared 1 uF 0402 pool (Mouser x27 + on hand 13).
- C2 (OK): Same 100 V X7R drop-in as feather C6.
- C5 (OK): Shared with feather C41/C54.
- C6,C7,C8,C9,C10 (OK): DigiKey x25 exact (the cart bought the schematic MPN, not the plan swap GCM155R71C104KA55D).
- CN1 (OK): Shared FFC connector.
- R2,R3,R4 (OK): DigiKey x25 shared with gateway R3 and pH R1.
- U2 (OK): DigiKey x5.
- U3 (OK): DigiKey x5.
- U4,U5 (OK): DigiKey x10.

Sourcing-only items: The 11-08 sourcing BOM also lists TP1-TP10, H1-H4 and J1 (TC2030 footprint): footprint-only items, not in the BOM export.

## BOM Builder needs file vs schematic

MPNs match the schematic for every ref in the needs file.
BB needs file board_count is 5 for this board.

Write-back proposal: `water_level_tc2030_writeback.csv`.
