# Programming adapter: parts reconciliation, 2026-11-22

Schematic: `hardware/prog_adapter/` at HEAD (kicad-cli 10 `sch export bom`, run 2026-11-22). Boards counted: 5 (bare boards ordered 5; build count unknown, so need = 5 x per-board qty).
Sources: schematic fields; sourcing BOM in hardware/prog_adapter/sourcing (MPN column = 2026-10-30/11-08/11-07 CSV, swaps = 2026-10-28 live CSV); the 11-10 plan (order_2026-11-10.md); what was ordered (BB shopping_list.json Ordered notes, last saved 2026-11-11 19:20, and the carts in tobuy); on hand (BB inventory.json, last saved 2026-11-11 17:59). Stock checked live 2026-11-22.

Counts (lines = groups of identical parts, refs in brackets): MISSING 1 (1), CHECK 1 (2), OK 13 (19)

## Problems

| Verdict | Refs | Schematic | Ordered | On hand | Need | Note |
|---|---|---|---|---|---|---|
| MISSING | J6 | USB4105-GF-A USB_C_Receptacle_GCT_USB4105-xx-A_16P_TopMnt_Horizontal USB4105-GF-A | - | - | 5 | No order or stock record for USB4105-GF-A (the on-hand UJ20-C-H-G-MSMT-4B-P16-TR is a different CUI USB-C). DigiKey 308,166 at $0.80, Mouser 377,802. [short by 5 vs demand 5] |
| CHECK | C1,C2 | 10u C_0805_2012Metric CC0805KKX5R8BB106 | CC0805KFX5R8BB106 x10 [DKweb] | - | 10 | Bought CC0805KFX5R8BB106 in place of CC0805KKX5R8BB106 (out of stock then): both are Yageo 10 uF 10% 25 V X5R 0805 on DigiKey/Mouser, so the spec is the same. 9 delivered, 1 backordered to Apr 2027, need 10: top up 1 (KKX is back at DigiKey, 96,155). |
| EXTRA | - | SPC02SYAN x10 (DigiKey web ID 379222461) | - | - | - | Shunts for JP1 (accessory, not a schematic part; BB needs lists it as JP1_SHUNT, need 1 per board). |
| EXTRA | - | TC2030-IDC x1 (DigiKey web ID 379222461) | - | - | - | Programming cable for the TC2030 pads (tool, not a schematic part). |
| EXTRA | - | TTL-232RG-VREG1V8-WE x1 (DigiKey web ID 379222461) | - | - | - | 1.8 V USB-UART cable for XM125 flashing (tool); backordered to about Dec 14. |
| MISSING | - | FFSD-05-D-06.00-01-N x1 (Samtec ribbon cable, BB needs line CABLE3) | - | - | - | In the BB needs file for the adapter but not in the schematic and no order record. |

## All parts

| Refs | Value / footprint | Sch MPN | Sourcing BOM MPN | 11-10 plan (whole-line buy qty) | Ordered (BB notes, whole-line qty) | On hand | Need | Stock 11-22 (write-back MPN) | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| J6 | USB4105-GF-A USB_C_Receptacle_GCT_USB4105-xx-A_16P_TopMnt_Horizontal | USB4105-GF-A | USB4105-GF-A | - | - | - | 5 | DK 308,166 / MO 377,802 | MISSING |
| C1,C2 | 10u C_0805_2012Metric | CC0805KKX5R8BB106 | CC0805KKX5R8BB106 | - | CC0805KFX5R8BB106 x10 [DKweb] | - | 10 | DK 96,155 / MO 138,950 | CHECK |
| D1 | GRN LED_0805_2012Metric | LTST-C171GKT | LTST-C171GKT | - | LTST-C171GKT x5 [DKweb] | - | 5 | DK 88,614 / MO 197,835 | OK |
| F1 | 0.5A Fuse_1206_3216Metric | MF-NSMF050-2 | MF-NSMF050-2 | - | MF-NSMF050-2 x5 [DKweb] | - | 5 | DK 41,307 / MO 16,410 | OK |
| J1,J2 | XM125 TC2030-IDC BoxHeader_SSK05-BH-254-B3_2x03_P2.54mm_Vertical | SSK05-BH-254-B3 | SSK05-BH-254-B3 | - | SSK05-BH-254-B3 x10 [DKweb] | - | 10 | DK 1,143 / MO 1,971 | OK |
| J3 | Cortex10 to DK Debug out BoxHeader_CNC_3220-10-0100-00_2x05_P1.27mm_Vertical | 3220-10-0100-00 | 3220-10-0100-00 | - | 3220-10-0100-00 x5 [DKweb] | - | 5 | DK 627,191 / MO n/a | OK |
| J4 | SWD 0.1in breakout PinHeader_1x06_P2.54mm_Vertical | PEC06SAAN | PEC06SAAN | - | PEC06SAAN x5 [DKweb] | - | 5 | DK 17,955 / MO n/a | OK |
| J5 | 3V0 OUT to TP9 TP10 PinHeader_1x03_P2.54mm_Vertical | PEC03SAAN | PEC03SAAN | - | PEC03SAAN x10 [DKweb] | - | 5 | DK 77,140 / MO n/a | OK |
| JP1 | BOOT0 PinHeader_1x02_P2.54mm_Vertical | PEC02SAAN | SPC02SYAN | - | PEC02SAAN x5 [DKweb] | - | 5 | DK 108,658 / MO n/a | OK |
| R1,R2 | 330 R_0805_2012Metric | RC0805FR-07330RL | RC0805FR-07330RL | - | RC0805FR-07330RL x10 [DKweb] | - | 10 | DK 299,479 / MO 322,881 | OK |
| R3,R6 | 1k R_0805_2012Metric | RC0805FR-071KL | RC0805FR-071KL | - | RC0805FR-071KL x10 [DKweb] | - | 10 | DK 458,659 / MO 1,971,868 | OK |
| R4,R5 | 5.1k R_0805_2012Metric | RC0805FR-075K1L | RC0805FR-075K1L | - | RMCF0805FT5K10 x10 [DKweb] | - | 10 | DK 116,022 / MO 40,757 | OK |
| R7,R8 | 100 R_0805_2012Metric | RC0805FR-07100RL | RC0805FR-07100RL | - | RC0805FR-07100RL x10 [DKweb] | - | 10 | DK 0 / MO 1,285,298 | OK |
| SW1,SW2 | XM RESET SW_PUSH_6mm | B3F-1000 | B3F-1000 | - | B3F-1000 x10 [DKweb] | - | 10 | DK 17,030 / MO 23,559 | OK |
| U1 | TLV75530PDBVR SOT-23-5 | TLV75530PDBVR | TLV75530PDBVR | - | TLV75530PDBVR x5 [DKweb] | - | 5 | DK 2,552 / MO 16,724 | OK |

## Notes per line

- J6 (MISSING): No order or stock record for USB4105-GF-A (the on-hand UJ20-C-H-G-MSMT-4B-P16-TR is a different CUI USB-C). DigiKey 308,166 at $0.80, Mouser 377,802. [short by 5 vs demand 5]
- C1,C2 (CHECK): Bought CC0805KFX5R8BB106 in place of CC0805KKX5R8BB106 (out of stock then): both are Yageo 10 uF 10% 25 V X5R 0805 on DigiKey/Mouser, so the spec is the same. 9 delivered, 1 backordered to Apr 2027, need 10: top up 1 (KKX is back at DigiKey, 96,155).
- D1 (OK): DigiKey web ID 379222461 x5.
- J5 (OK): x10 bought, need 5.
- JP1 (OK): The 2026-11-07 sourcing BOM lists SPC02SYAN for JP1 (the shunt); the schematic part is the PEC02SAAN header, the shunt SPC02SYAN x10 is bought separately.
- R4,R5 (OK): Bought Stackpole RMCF0805FT5K10 (5.1k 1% 0805 thick film) for out-of-stock RC0805FR-075K1L: same value/size/tolerance.

Sourcing-only items: The 11-07 sourcing BOM lists J7 and H1-H4: footprint-only, not in the BOM export.

## BOM Builder needs file vs schematic

None in MPNs (accessory lines only).
BB needs file board_count is 5 for this board.

Write-back proposal: `prog_adapter_writeback.csv`.
