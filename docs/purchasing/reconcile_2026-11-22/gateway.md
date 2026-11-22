# Pouch gateway: parts reconciliation, 2026-11-22

Schematic: `hardware/gateway/` at HEAD (kicad-cli 10 `sch export bom`, run 2026-11-22). Boards counted: 5.
Sources: schematic fields; sourcing BOM in hardware/gateway/sourcing (MPN column = 2026-10-30/11-08/11-07 CSV, swaps = 2026-10-28 live CSV); the 11-10 plan (order_2026-11-10.md); what was ordered (BB shopping_list.json Ordered notes, last saved 2026-11-11 19:20, and the carts in tobuy); on hand (BB inventory.json, last saved 2026-11-11 17:59). Stock checked live 2026-11-22.

Counts (lines = groups of identical parts, refs in brackets): MISSING 4 (6), CHECK 3 (3), OK 18 (46), DNP 6 (9), N/A 3 (6)

## Problems

| Verdict | Refs | Schematic | Ordered | On hand | Need | Note |
|---|---|---|---|---|---|---|
| MISSING | J1 | TYPE-C-31-M-12 USB_C_Receptacle_HRO_TYPE-C-31-M-12 (no MPN) | DX07S016JA3R1500 x2 [DK] | - | 5 (pool 10) | Same USB-C situation as feather J1 (shared pool of 10). The 11-10 md says the gateway footprint is only a near drop-in for USB4105-GF-A (rear shell slot 0.2 mm short). [short by 8 vs pool/line demand 10] |
| MISSING | J3 | U.FL-R-SMT-1 U.FL_Hirose_U.FL-R-SMT-1_Vertical (no MPN) | U.FL-R-SMT-1(10) x3 [DK] | - | 5 | Ordered 3 (BB note; cart had 5). Need 5. [short by 2 vs pool/line demand 5] |
| MISSING | SW1,SW2,SW3 | RESET SW_Push_1P1T_NO_CK_KMR2 (no MPN) | KMR221G x10 [DK] | - | 15 | Ordered 10 (BB note, "KMR221G in place of KMR221GLFS" = same C&K part; DigiKey lists it as KMR221G LFS), need 15 (cart had 15). [short by 5 vs pool/line demand 15] |
| MISSING | U1 | LBES0ZZ2FR Murata_LBES0ZZ2FR LBES0ZZ2FR-580 | LBES0ZZ2FR-580 x2 [DK] | - | 5 | Ordered 2 (BB note; cart had 5), need 5. DigiKey 0 and Mouser 0 today (was 71 on 11-10): 3 more cannot be bought right now (Mouser lead 266 days). [short by 3 vs pool/line demand 5] |
| CHECK | D1 | PRTR5V0U2X SOT-143 (no MPN) | 8240026 x5 [DK] | - | 5 | Schematic PRTR5V0U2X; DigiKey x5 Wurth 8240026 (WE-TVS 2-line rail-to-rail steering diode, 5 V, SOT-143-4) bought in its place. Same topology but pin-for-pin pinout vs PRTR5V0U2X and the SOT-143 land pattern were never compared: verify before soldering. |
| CHECK | D2 | RB521S30T1G D_SOD-523 (no MPN) | RB521S30-AU_R1_000A1 x5 [DK] | - | 5 | Schematic RB521S30T1G (30 V Schottky SOD-523); DigiKey x5 RB521S30-AU_R1_000A1 bought in its place per design notes. Same class; datasheet not compared. |
| CHECK | L1 | 2.2uH L_Sunlord_SWPA4020S SWPA4020S2R2MT | SWPA4020S2R2NT x5 [DK] | - | 5 | Schematic SWPA4020S2R2MT (+-20%); bought SWPA4020S2R2NT (+-30%, 1.85 A, Isat 3.7 A, 4 x 4 x 2 mm per DigiKey). Same footprint; tolerance looser: confirm TLV62569 inductance range. |
| MISSING | - | Off-board: ANT 1461530100 (Molex FPC antenna 100 mm) x5 | - | - | - | In the 11-10 add-on list only; no order record in BB notes. Not a schematic part. |
| MISSING | - | Off-board: W1 cable PHR-8 housings x10 and ASPHSPH24K102 leads x40 | - | - | - | LCD cable, in the 11-10 add-on list only; no order record. Not a schematic part. |
| CHECK | - | Off-board: Waveshare 2inch LCD module x5 | - | - | - | BB inventory has 1 (Amazon B082GFTZQD, delivered 11-10); need 5, bought elsewhere per the 11-10 md, no record of the other 4. |

## All parts

| Refs | Value / footprint | Sch MPN | Sourcing BOM MPN | 11-10 plan (whole-line buy qty) | Ordered (BB notes, whole-line qty) | On hand | Need | Stock 11-22 (write-back MPN) | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| J1 | TYPE-C-31-M-12 USB_C_Receptacle_HRO_TYPE-C-31-M-12 | - | TYPE-C-31-M-12 | USB4105-GF-A x12 | DX07S016JA3R1500 x2 [DK] | - | 5 (pool 10) | DK n/a / MO n/a | MISSING |
| J3 | U.FL-R-SMT-1 U.FL_Hirose_U.FL-R-SMT-1_Vertical | - | U.FL-R-SMT-1(10) | U.FL-R-SMT-1(10) x6 | U.FL-R-SMT-1(10) x3 [DK] | - | 5 | DK 304,307 / MO 120,221 | MISSING |
| SW1,SW2,SW3 | RESET SW_Push_1P1T_NO_CK_KMR2 | - | KMR221GLFS | KMR221G LFS x16 | KMR221G x10 [DK] | - | 15 | DK 106,032 / MO 36,288 | MISSING |
| U1 | LBES0ZZ2FR Murata_LBES0ZZ2FR | LBES0ZZ2FR-580 | LBES0ZZ2FR-580 | LBES0ZZ2FR-580 x5 | LBES0ZZ2FR-580 x2 [DK] | - | 5 | DK 0 / MO 0 | MISSING |
| D1 | PRTR5V0U2X SOT-143 | - | 8240026 | 8240026 x6 | 8240026 x5 [DK] | - | 5 | DK 2,426 / MO 5,117 | CHECK |
| D2 | RB521S30T1G D_SOD-523 | - | RB521S30-AU_R1_000A1 | RB521S30-AU_R1_000A1 x10 | RB521S30-AU_R1_000A1 x5 [DK] | - | 5 | DK 44,615 / MO 2,422 | CHECK |
| L1 | 2.2uH L_Sunlord_SWPA4020S | SWPA4020S2R2MT | SWPA4020S2R2NT | SWPA4020S2R2NT x6 | SWPA4020S2R2NT x5 [DK] | - | 5 | DK 1,290 / MO n/a | CHECK |
| C1 | 10uF 25V C_0603_1608Metric | - | CL10A106MA8NRNC | TMK107BBJ106MA-T x50 | CL10A106MA8NRNC x24 [MO]; TMK107BBJ106MA-T x5 [DK] | CC0603MRX5R8BB106 x6 | 5 (pool 35) | DK 0 / MO 2,578 | OK |
| C2,C8,C9,C10,C11,C12,C13,C14,C16,C19,C21 | 100nF C_0402_1005Metric | - | GCM155R71C104KA55D | GCM155R71C104KA55D x100 | GCM155R71C104KA55D x100 [DK] | - | 55 (pool 82) | DK 3,503,855 / MO 0 | OK |
| C4,C5,C7,C15,C20 | 10uF C_0603_1608Metric | - | CL10A106MA8NRNC | TMK107BBJ106MA-T x50 | CL10A106MA8NRNC x24 [MO]; TMK107BBJ106MA-T x5 [DK] | CC0603MRX5R8BB106 x6 | 25 (pool 35) | DK 0 / MO 2,578 | OK |
| C6 | 22uF C_0805_2012Metric | - | CL21A226MOQNNNE | CL21A226MOCLRNC x10 | CL21A226MOQNNNE x5 [MO] | - | 5 | DK 0 / MO 266,670 | OK |
| D3 | Red LED_0603_1608Metric | - | LTST-C191KRKT | LTST-C191KRKT x10 | LTST-C191KRKT x5 [DK] | - | 5 | DK 1,303,231 / MO 1,259,885 | OK |
| D4 | Green LED_0805_2012Metric | - | LTST-C170KGKT | LTST-C170KGKT x10 | LTST-C170KGKT x5 [DK] | - | 5 | DK 397,590 / MO 643,324 | OK |
| D5 | Blue LED_0603_1608Metric | - | LTST-C190TBKT | LTST-C190TBKT x10 | LTST-C190TBKT x5 [DK] | - | 5 | DK 361,421 / MO 177,500 | OK |
| FB1 | BLM18KG221SN1D L_0603_1608Metric | - | BLM18KG221SN1D | BLM18KG221SN1D x7 | BLM18KG221SN1D x5 [DK] | - | 5 | DK 413,774 / MO 501,155 | OK |
| J5 | LCD 2.0in (Waveshare) JST_PH_S8B-PH-K_1x08_P2.00mm_Horizontal | S8B-PH-K-S(LF)(SN) | S8B-PH-K-S(LF)(SN) | S8B-PH-K-S x7 | S8B-PH-K-S(LF)(SN) x5 [MO] | - | 5 | DK 7,811 / MO 7,446 | OK |
| R1,R2,R10,R11 | 5.1k R_0402_1005Metric | - | RC0402FR-075K1L | RC0402FR-075K1L x30 | RC0402FR-075K1L x25 [DK] | CR0402-FX-5101GLF x46 | 20 | DK 559,241 / MO 1,760,212 | OK |
| R14 | 470R R_0402_1005Metric | - | RC0402FR-07470RL | RC0402FR-07470RL x15 | RC0402FR-07470RL x10 [DK] | - | 5 | DK 1,070,000 / MO 1,837,327 | OK |
| R20,R21,R22 | 33R R_0402_1005Metric | - | RC0402FR-0733RL | RC0402FR-0733RL x25 | RC0402FR-0733RL x15 [DK] | - | 15 | DK 214,873 / MO 2,004,397 | OK |
| R3 | 100k R_0402_1005Metric | - | RC0402FR-07100KL | RC0402FR-07100KL x25 | RC0402FR-07100KL x25 [DK] | - | 5 (pool 16) | DK 3,692,494 / MO 15,492,618 | OK |
| R4 | 22k R_0402_1005Metric | - | ERJ-2RKF2202X | ERJ-2RKF2202X x18 | ERJ-2RKF2202X x10 [DK] | - | 5 | DK 506,653 / MO 0 | OK |
| R5,R6,R12,R13,R23 | 0R R_0402_1005Metric | - | ERJ-2GE0R00X | ERJ-2GE0R00X x35 | ERJ-2GE0R00X x25 [DK] | RC0402JR-070RL x10000 | 25 | DK 12,573,566 / MO 6,211,898 | OK |
| R7,R8,R18 | 10k R_0402_1005Metric | - | RC0402FR-0710KL | RC0402FR-0710KL x27 | RC0402FR-0710KL x25 [DK] | - | 15 | DK 3,728,884 / MO 22,972,431 | OK |
| R9,R15,R16,R17 | 100R R_0402_1005Metric | - | RC0402FR-07100RL | RC0402FR-07100RL x30 | RC0402FR-07100RL x25 [DK] | - | 20 | DK 2,243,575 / MO 11,061,933 | OK |
| U2 | TLV62569DBVR SOT-23-5 | - | TLV62569DBVR | TLV62569DBVR x10 | TLV62569DBVR x5 [DK] | - | 5 | DK 235,112 / MO 27,793 | OK |
| C17,C18,C22,C23 | DNP C_0402_1005Metric | - DNP | - | - | - | - | 0 | - | DNP |
| C3 | DNP 6.8pF C_0402_1005Metric | - DNP | - | - | - | - | 0 | - | DNP |
| J2 | SWD PinHeader_2x05_P1.27mm_Vertical_SMD | FTSH-105-01-L-DV-K-TR DNP | - | - | - | - | 0 | - | DNP |
| J4 | UART PinHeader_1x03_P2.54mm_Vertical | PZ254V-11-03P DNP | - | - | - | - | 0 | - | DNP |
| J7 | U.FL-R-SMT-1 U.FL_Hirose_U.FL-R-SMT-1_Vertical | - DNP | - | - | - | - | 0 | - | DNP |
| R24 | 0R R_0402_1005Metric | - DNP | - | - | - | - | 0 | - | DNP |
| H1,H2,H3,H4 | M2 MountingHole_2.2mm_M2 | - | - | - | - | - | 0 | - | N/A |
| J6 | TC2030-CTX Tag-Connect_TC2030-IDC-FP_2x03_P1.27mm_Vertical | - | - | - | - | - | 0 | - | N/A |
| TP1 | LCD_TE TestPoint_Pad_D1.0mm | - | - | - | - | - | 0 | - | N/A |

## Notes per line

- J1 (MISSING): Same USB-C situation as feather J1 (shared pool of 10). The 11-10 md says the gateway footprint is only a near drop-in for USB4105-GF-A (rear shell slot 0.2 mm short). [short by 8 vs pool/line demand 10]
- J3 (MISSING): Ordered 3 (BB note; cart had 5). Need 5. [short by 2 vs pool/line demand 5]
- SW1,SW2,SW3 (MISSING): Ordered 10 (BB note, "KMR221G in place of KMR221GLFS" = same C&K part; DigiKey lists it as KMR221G LFS), need 15 (cart had 15). [short by 5 vs pool/line demand 15]
- U1 (MISSING): Ordered 2 (BB note; cart had 5), need 5. DigiKey 0 and Mouser 0 today (was 71 on 11-10): 3 more cannot be bought right now (Mouser lead 266 days). [short by 3 vs pool/line demand 5]
- D1 (CHECK): Schematic PRTR5V0U2X; DigiKey x5 Wurth 8240026 (WE-TVS 2-line rail-to-rail steering diode, 5 V, SOT-143-4) bought in its place. Same topology but pin-for-pin pinout vs PRTR5V0U2X and the SOT-143 land pattern were never compared: verify before soldering.
- D2 (CHECK): Schematic RB521S30T1G (30 V Schottky SOD-523); DigiKey x5 RB521S30-AU_R1_000A1 bought in its place per design notes. Same class; datasheet not compared.
- L1 (CHECK): Schematic SWPA4020S2R2MT (+-20%); bought SWPA4020S2R2NT (+-30%, 1.85 A, Isat 3.7 A, 4 x 4 x 2 mm per DigiKey). Same footprint; tolerance looser: confirm TLV62569 inductance range.
- C1 (OK): Schematic has no MPN. Sourcing: CL10A106MA8NRNC (Mouser x24); DigiKey TMK107BBJ106MA-T x5 bought in its place. Shared pool with feather C16.
- C4,C5,C7,C15,C20 (OK): Value says only 10uF: set 10uF 25V in the schematic to match C1.
- C6 (OK): Mouser x5 exact (22 uF 16 V X5R 0805). Schematic value has no voltage: add 16V. DigiKey CL21A226MOQNNNE is 0 stock today.
- D3 (OK): Red 0603, package matches footprint. Schematic has no MPN.
- D4 (OK): Green 0805, package matches footprint.
- D5 (OK): Blue 0603, package matches footprint.
- J5 (OK): Mouser x5 exact.
- R1,R2,R10,R11 (OK): DigiKey x25 + on hand 46 CR0402-FX-5101GLF (5.1k 1% 0402).
- R4 (OK): 22k 1%. DigiKey x10 (need 5).
- R5,R6,R12,R13,R23 (OK): DigiKey x25 + on hand 10,000 RC0402JR-070RL.
- J6 (N/A): Tag-Connect TC2030 footprint (no part).

Sourcing-only items: The 10-28 sourcing BOM lists W1 (LCD cable) which is not a schematic symbol.

## BOM Builder needs file vs schematic

Differences: L1: needs file SWPA4020S2R2NT, sch MPN SWPA4020S2R2MT.
BB needs file board_count is 5 for this board.

Write-back proposal: `gateway_writeback.csv`.
