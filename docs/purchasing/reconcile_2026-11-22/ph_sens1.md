# pH sens1: parts reconciliation, 2026-11-22

Schematic: `hardware/sensors/ph/nrf54l15_feather_sens1/` at HEAD (kicad-cli 10 `sch export bom`, run 2026-11-22). Boards counted: 2.
Sources: schematic fields; sourcing BOM in hardware/sensors/ph/sourcing (MPN column = 2026-10-30/11-08/11-07 CSV, swaps = 2026-10-28 live CSV); the 11-10 plan (order_2026-11-10.md); what was ordered (BB shopping_list.json Ordered notes, last saved 2026-11-11 19:20, and the carts in tobuy); on hand (BB inventory.json, last saved 2026-11-11 17:59). Stock checked live 2026-11-22.

Counts (lines = groups of identical parts, refs in brackets): MISSING 1 (1), CHECK 1 (1), OK 9 (12), DNP 2 (3)

## Problems

| Verdict | Refs | Schematic | Ordered | On hand | Need | Note |
|---|---|---|---|---|---|---|
| MISSING | U2 | Atlas_pH_OEM Atlas_pH_OEM OEM-pH | - | - | 2 | Atlas Scientific OEM-pH: no order or stock record in any source (11-10 md says buy at atlas-scientific.com, about 45.99 each). Need 2. [short by 2 vs demand 2] |
| CHECK | J1 | Conn_Coaxial_Small SMA_BAT_Wireless_BWSMA-KWE-Z001 BWSMA-KWE-Z001 | - | SuperBat X0036NHOHB x9 | 2 (pool 7) | Same SMA situation as ORP J1. |

## All parts

| Refs | Value / footprint | Sch MPN | Sourcing BOM MPN | 11-10 plan (whole-line buy qty) | Ordered (BB notes, whole-line qty) | On hand | Need | Stock 11-22 (write-back MPN) | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| U2 | Atlas_pH_OEM Atlas_pH_OEM | OEM-pH | OEM-pH | - | - | - | 2 | DK n/a / MO n/a | MISSING |
| J1 | Conn_Coaxial_Small SMA_BAT_Wireless_BWSMA-KWE-Z001 | BWSMA-KWE-Z001 | BWSMA-KWE-Z001 | - | - | SuperBat X0036NHOHB x9 | 2 (pool 7) | DK n/a / MO n/a | CHECK |
| C1,C5 | 1uF C0402 | CL05A105KO5NNNC | CL05A105KO5NNNC | GRM155R61C105KA12D x28 | CL05A105KO5NNNC x27 [MO] | CL05A105KO5NNNC x13 | 4 (pool 28) | DK 0 / MO 1,346 | OK |
| C2,C4 | 100nF C0603 | CC0603KRX7R9BB104 | CC0603KRX7R9BB104 | CC0603KRX7R9BB104 x50 | GRM188R72A104KA35D x24 [MO] | GRM188R72A104KA35D x21 | 4 (pool 37) | DK 85,912 / MO 1,361,404 | OK |
| C3 | 2.2uF C0603 | GRM188R71A225KE15D | GRM188R71A225KE15D | GRM188R71A225KE15D x12 | GRM188R71A225KE15D x10 [DK] | - | 2 (pool 7) | DK 889,277 / MO 1,397 | OK |
| C6 | 100nF C_0402_1005Metric | CC0402KRX7R7BB104 | CC0402KRX7R7BB104 | GCM155R71C104KA55D x100 | GCM155R71C104KA55D x100 [DK] | - | 2 (pool 82) | DK 3,503,855 / MO 0 | OK |
| CN1 | 503480-1400 Molex_503480-1400_1x14-1MP_P0.50mm_Horizontal | 503480-1400 | 503480-1400 | 5034801400 x11 | 5034801400 x25 [DK] | - | 2 (pool 15) | DK 26,283 / MO 16,510 | OK |
| R1 | 100k R0402 | RC0402FR-07100KL | RC0402FR-07100KL (live swap: RC0402FR-0710KL) | RC0402FR-0710KL x27 | RC0402FR-07100KL x25 [DK] | - | 2 (pool 16) | DK 3,692,494 / MO 15,492,618 | OK |
| R3,R4 | 4.7k R0402 | CRCW04024K70FKED | CRCW04024K70FKED | RC0402FR-074K7L x34 | RC0402FR-074K7L x10 [DK] | RC0402FR-074K7L x39 | 4 (pool 34) | DK 320,000 / MO 4,737,940 | OK |
| U3 | ADuM1250 SOIC-8_3.9x4.9mm_P1.27mm | ADUM1250ARZ-RL7 | ADUM1250ARZ-RL7 | ADUM1250ARZ-RL7 x2 | ADUM1250ARZ-RL7 x2 [DK] | ADUM1250ARZ-RL7 x4 | 2 | DK 0 / MO 0 | OK |
| U4 | NXE1S0303MC Converter_DCDC_Murata_NXExSxxxxMC_SMD | NXE1S0303MC-R13 | NXE1S0303MC-R13 | NXE1S0303MC-R13 x2 | NXE1S0303MC-R13 x3 [DK] | NXE1S0303MC-R7 x4 | 2 | DK 11,986 / MO 0 | OK |
| D1 | 5.1V D_SOD-323 | MM3Z5V1T1G DNP | - | MM3Z5V1T1G x3 | - | - | 0 | - | DNP |
| R5,R6 | 0 R0402 | ERJ-2GE0R00X DNP | - (live swap: ERJ-2GE0R00X) | - | ERJ-2GE0R00X x25 [DK] | - | 0 | - | DNP |

## Notes per line

- U2 (MISSING): Atlas Scientific OEM-pH: no order or stock record in any source (11-10 md says buy at atlas-scientific.com, about 45.99 each). Need 2. [short by 2 vs demand 2]
- J1 (CHECK): Same SMA situation as ORP J1.
- C6 (OK): BB standardisation from CC0402KRX7R7BB104 (0.1 uF 16 V X7R 0402).
- R1 (OK): R1 100k since 2026-11-11 (the 11-10 plan still had 10k RC0402FR-0710KL for pH R1: stale). DigiKey 100k line covers it.
- R3,R4 (OK): BB standardisation from CRCW04024K70FKED.
- U3 (OK): Ordered 2 (both on backorder) + on hand 4 = 6, need 2. DigiKey 0 today, so the on-hand 4 are what you will build with.
- U4 (OK): DigiKey x3 + on hand 4 (R7 reel code).
- D1 (DNP): DNP bring-up clamp (MM3Z5V1T1G, not bought).

## BOM Builder needs file vs schematic

MPNs match the schematic for every ref in the needs file.
BB needs file board_count is 5 for this board.

Write-back proposal: `ph_sens1_writeback.csv`.
