# Cost analysis: Gateway (2026-10-29)

Live DigiKey (Product Information v4) and Mouser Search API price-break tables read 2026-10-29 (USD, US site, cut tape/bulk; shipping, tax, tariffs and fees excluded). N = number of complete products built in one purchase (all N bought together, so quantity breaks use the combined quantity). Scope: pouch_gateway (incl. W1 LCD cable parts and antenna) + Ledger enclosure + Waveshare 2inch LCD.

Read-only analysis: no schematic, PCB or symbol was edited. Prices marked EST are labelled estimates, not quotes.

## 1. Cost per product (cost curve)

Draft = plain PETG, TPU parts left off, key/light pipe in PETG (what is being printed now). Final = TPU key, bung, boot and clip pads at TPU price. Totals per product = total order cost / N.

| N | PCB | Parts | Enclosure | Other | **Total/product (draft)** | Total/product (final) | Whole order (draft) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | $68.45 | $39.94 | $5.89 | $10.59 | **$124.87** | $124.87 | $124.87 |
| 5 | $13.69 | $37.57 | $5.22 | $10.59 | **$67.07** | $67.07 | $335.36 |
| 10 | $9.28 | $32.19 | $5.22 | $10.39 | **$57.08** | $57.08 | $570.78 |
| 25 | $5.99 | $30.56 | $4.69 | $10.39 | **$51.63** | $51.63 | $1290.77 |
| 50 | $4.62 | $29.96 | $4.69 | $10.31 | **$49.58** | $49.58 | $2478.88 |
| 100 | $3.63 | $27.67 | $4.48 | $10.31 | **$46.09** | $46.09 | $4608.84 |

Split: PCB = bare boards; Parts = schematic BOM(s) incl. the Atlas OEM module and LCSC-only lines; Enclosure = printed filament + enclosure hardware (inserts, screws, o-ring, vent, desiccant, bulkhead); Other = battery, solar cell, FFC, RF pigtail parts, LCD.

Percent split of the draft total:

| N | PCB | Parts | Enclosure | Other |
|---:|---:|---:|---:|---:|
| 1 | 55 % | 32 % | 5 % | 8 % |
| 5 | 20 % | 56 % | 8 % | 16 % |
| 10 | 16 % | 56 % | 9 % | 18 % |
| 25 | 12 % | 59 % | 9 % | 20 % |
| 50 | 9 % | 60 % | 9 % | 21 % |
| 100 | 8 % | 60 % | 10 % | 22 % |

Note on PCBs: PCBWay minimum order is 5 boards, so at N=1 the PCB line carries the cost of 5 boards (4 spares); the per-product PCB cost falls steeply to N=10 then flattens.

## 2. Board and sub-assembly subtotals (stand-alone, $ per board/assembly, draft)

So other node combinations can be added up. Stand-alone figures: identical parts on two boards are not merged here, so they add up to slightly more than the merged product total.

| Item | N=1 | N=5 | N=10 | N=25 | N=50 | N=100 |
|---|---:|---:|---:|---:|---:|---:|
| Gateway board (PCB + BOM) | $108.39 | $51.26 | $41.47 | $36.55 | $34.57 | $31.30 |
| Ledger enclosure (filament + hardware) + LCD | $16.48 | $15.81 | $15.61 | $15.08 | $15.00 | $14.79 |
|   of which LCD | $10.59 | $10.59 | $10.39 | $10.39 | $10.31 | $10.31 |
|   of which printed filament only | $1.30 | $1.30 | $1.30 | $1.30 | $1.30 | $1.30 |

## 3. Every line, ranked by extended cost per product at N=1

$/product = line cost of the whole order / N, including any buy-up (see section 5). Var: both = in draft and final; D = draft only; F = final only (counted in the Final total, not the Draft total). Src N=1 / N=100 = cheapest source (DK = DigiKey, MO = Mouser, LCSC, Atlas, WS = Waveshare, EST = my estimate, print = own printer). Rank100 = rank of the line at N=100.

| # | Line | Group | Qty/prod | Var | $ N=1 | N=5 | N=10 | N=25 | N=50 | N=100 | Src 1 / 100 | Rank100 |
|---:|---|---|---:|:--:|---:|---:|---:|---:|---:|---:|---|---:|
| 1 | PCB Gateway (PCBWay 4L 1.6 mm ENIG, 20.3 cm2) | PCB | 1 | both | 68.45 | 13.69 | 9.28 | 5.99 | 4.62 | 3.63 | PCB est / PCB est | 3 |
| 2 | LBES0ZZ2FR-580 (Gateway: U1) | Parts | 1 | both | 23.41 | 23.41 | 20.41 | 19.37 | 19.37 | 17.95 | DK / DK | 1 |
| 3 | Waveshare 2inch LCD module (SKU 17344) | Other | 1 | both | 10.59 | 10.59 | 10.39 | 10.39 | 10.31 | 10.31 | WS / WS | 2 |
| 4 | M2 brass insert x8 (SI IUTB-M2-318, 3.18 mm OD) | Enclosure | 8 | both | 3.33 | 2.66 | 2.66 | 2.14 | 2.14 | 1.92 | MO / MO | 5 |
| 5 | ASPHSPH24K102 (Gateway: W1 (8 leads)) | Parts | 8 | both | 3.20 | 2.57 | 2.42 | 2.31 | 2.15 | 2.04 | DK / MO | 4 |
| 6 | 146153-0100 (Gateway: ANT) | Parts | 1 | both | 2.59 | 2.59 | 1.94 | 1.82 | 1.82 | 1.73 | DK / MO | 6 |
| 7 | KMR221GLFS (Gateway: SW1,SW2,SW3) | Parts | 3 | both | 2.01 | 1.73 | 1.61 | 1.61 | 1.44 | 1.33 | DK / DK | 7 |
| 8 | CL10A106MA8NRNC (Gateway: C1,C4,C5,C7,C15,C20) | Parts | 6 | both | 1.87 | 1.12 | 0.82 | 0.72 | 0.72 | 0.57 | DK / DK | 12 |
| 9 | U.FL-R-SMT-1(10) (Gateway: J3) | Parts | 1 | both | 1.67 | 1.67 | 1.42 | 1.27 | 1.26 | 1.20 | DK / DK | 8 |
| 10 | 8240026 (Gateway: D1) | Parts | 1 | both | 1.09 | 1.09 | 1.03 | 1.03 | 0.97 | 0.90 | DK / DK | 10 |
| 11 | M2 x 5 screws x12 (4 board, 4 button head, 4 PT for the LCD) | Enclosure | 12 | both | 0.96 | 0.96 | 0.96 | 0.96 | 0.96 | 0.96 | EST / EST | 9 |
| 12 | Ledger wedge stand (PETG, solid 80 cm3 part) | Enclosure | 1 | both | 0.82 | 0.82 | 0.82 | 0.82 | 0.82 | 0.82 | print / print | 11 |
| 13 | CL21A226MOQNNNE (Gateway: C6) | Parts | 1 | both | 0.63 | 0.63 | 0.37 | 0.37 | 0.26 | 0.23 | MO / MO | 16 |
| 14 | GCM155R71C104KA55D | Parts | 11 | both | 0.37 | 0.25 | 0.22 | 0.22 | 0.15 | 0.15 | DK / DK | 20 |
| 15 | SWPA4020S2R2NT (Gateway: L1) | Parts | 1 | both | 0.34 | 0.34 | 0.28 | 0.28 | 0.28 | 0.23 | DK / DK | 17 |
| 16 | S8B-PH-K-S(LF)(SN) (Gateway: J5) | Parts | 1 | both | 0.33 | 0.33 | 0.28 | 0.28 | 0.28 | 0.27 | DK / MO | 15 |
| 17 | Ledger front shell (PETG) | Enclosure | 1 | both | 0.32 | 0.32 | 0.32 | 0.32 | 0.32 | 0.32 | print / print | 13 |
| 18 | Foam/TPU gasket + bezel adhesive (optional in the notes) | Enclosure | 1 | both | 0.30 | 0.30 | 0.30 | 0.30 | 0.30 | 0.30 | EST / EST | 14 |
| 19 | TLV62569DBVR (Gateway: U2) | Parts | 1 | both | 0.28 | 0.28 | 0.19 | 0.17 | 0.17 | 0.14 | DK / MO | 22 |
| 20 | LTST-C190TBKT (Gateway: D5) | Parts | 1 | both | 0.26 | 0.26 | 0.18 | 0.18 | 0.18 | 0.12 | DK / DK | 23 |
| 21 | PHR-8 (Gateway: W1 (2 housings)) | Parts | 2 | both | 0.22 | 0.19 | 0.19 | 0.17 | 0.16 | 0.16 | DK / DK | 19 |
| 22 | LTST-C170KGKT (Gateway: D4) | Parts | 1 | both | 0.19 | 0.19 | 0.13 | 0.13 | 0.13 | 0.090 | DK / DK | 24 |
| 23 | TYPE-C-31-M-12 (Gateway J1 USB-C) (Gateway: J1) | Parts | 1 | both | 0.19 | 0.19 | 0.19 | 0.19 | 0.19 | 0.19 | LCSC / LCSC | 18 |
| 24 | LTST-C191KRKT (Gateway: D3) | Parts | 1 | both | 0.15 | 0.15 | 0.10 | 0.10 | 0.10 | 0.071 | DK / DK | 25 |
| 25 | Ledger rear cover (PETG) | Enclosure | 1 | both | 0.15 | 0.15 | 0.15 | 0.15 | 0.15 | 0.15 | print / print | 21 |
| 26 | RB521S30-AU_R1_000A1 (Gateway: D2) | Parts | 1 | both | 0.14 | 0.13 | 0.063 | 0.063 | 0.059 | 0.051 | DK / DK | 27 |
| 27 | BLM18KG221SN1D (Gateway: FB1) | Parts | 1 | both | 0.14 | 0.14 | 0.10 | 0.079 | 0.079 | 0.070 | DK / DK | 26 |
| 28 | ERJ-2RKF2202X (Gateway: R4) | Parts | 1 | both | 0.11 | 0.066 | 0.033 | 0.025 | 0.020 | 0.016 | DK / DK | 33 |
| 29 | RC0402FR-075K1L (Gateway: R1,R2,R10,R11) | Parts | 4 | both | 0.11 | 0.044 | 0.044 | 0.028 | 0.028 | 0.028 | MO / MO | 29 |
| 30 | ERJ-2GE0R00X (Gateway: R5,R6,R12,R13,R23) | Parts | 5 | both | 0.11 | 0.055 | 0.055 | 0.048 | 0.040 | 0.035 | MO / DK | 28 |
| 31 | RC0402FR-0710KL (Gateway: R7,R8,R18) | Parts | 3 | both | 0.11 | 0.033 | 0.033 | 0.028 | 0.021 | 0.021 | MO / MO | 31 |
| 32 | RC0402FR-07100RL (Gateway: R9,R15,R16,R17) | Parts | 4 | both | 0.11 | 0.044 | 0.044 | 0.028 | 0.028 | 0.028 | MO / MO | 30 |
| 33 | RC0402FR-0733RL (Gateway: R20,R21,R22) | Parts | 3 | both | 0.11 | 0.033 | 0.033 | 0.028 | 0.021 | 0.021 | MO / MO | 32 |
| 34 | RC0402FR-07100KL (Gateway: R3) | Parts | 1 | both | 0.10 | 0.022 | 0.011 | 0.011 | 0.011 | 0.007 | DK / MO | 34 |
| 35 | RC0402FR-07470RL (Gateway: R14) | Parts | 1 | both | 0.10 | 0.022 | 0.011 | 0.011 | 0.011 | 0.007 | DK / MO | 35 |
| 36 | Ledger key cap (PETG) | Enclosure | 1 | both | 0.006 | 0.006 | 0.006 | 0.006 | 0.006 | 0.006 | print / print | 36 |
| 37 | Ledger bezel insert (PETG) | Enclosure | 1 | both | 0.005 | 0.005 | 0.005 | 0.005 | 0.005 | 0.005 | print / print | 37 |
| 38 | Ledger foot strip 1 (TPU, final) | Enclosure | 1 | F | 0.003 | 0.003 | 0.003 | 0.003 | 0.003 | 0.003 | print / print | 38 |
| 39 | Ledger foot strip 1 (PETG, draft) | Enclosure | 1 | D | 0.002 | 0.002 | 0.002 | 0.002 | 0.002 | 0.002 | print / print | 39 |
| 40 | Ledger status pill (PETG; translucent PETG/PCTG in the final) | Enclosure | 1 | both | 0.002 | 0.002 | 0.002 | 0.002 | 0.002 | 0.002 | print / print | 40 |
| 41 | Ledger foot strip 2 (TPU, final) | Enclosure | 1 | F | 0.002 | 0.002 | 0.002 | 0.002 | 0.002 | 0.002 | print / print | 41 |
| 42 | Ledger foot strip 2 (PETG, draft) | Enclosure | 1 | D | 0.001 | 0.001 | 0.001 | 0.001 | 0.001 | 0.001 | print / print | 42 |
| 43 | Ledger foot strip 3 (TPU, final) | Enclosure | 1 | F | 0.001 | 0.001 | 0.001 | 0.001 | 0.001 | 0.001 | print / print | 43 |
| 44 | Ledger foot strip 3 (PETG, draft) | Enclosure | 1 | D | 0.001 | 0.001 | 0.001 | 0.001 | 0.001 | 0.001 | print / print | 44 |

`!` after a source = stock at that quantity is short at every distributor (priced as if stocked); see section 6.

Totals of the table: draft = $124.87 (N=1) ... $46.09 (N=100); final = $124.87 ... $46.09.

## 4. Unit price at the quantity actually needed (qty/product x N)

Cell = unit price actually paid (total line cost / pieces bought) with the source; `(buy B)` where buying up to a higher break was cheaper than the exact quantity. Qty needed per N is qty/product x N.

| # | Line | Qty/prod | N=1 | N=5 | N=10 | N=25 | N=50 | N=100 |
|---:|---|---:|---|---|---|---|---|---|
| 1 | PCB Gateway (PCBWay 4L 1.6 mm ENIG, 20.3 cm2) | 1 | $13.69/board x 5 boards | $13.69/board x 5 boards | $9.28/board x 10 boards | $5.99/board x 25 boards | $4.62/board x 50 boards | $3.63/board x 100 boards |
| 2 | LBES0ZZ2FR-580 | 1 | 23.41 DK | 23.41 DK | 20.41 DK | 19.37 DK | 19.37 DK | 17.95 DK |
| 3 | Waveshare 2inch LCD module (SKU 17344) | 1 | 10.59 WS | 10.59 WS | 10.39 WS | 10.39 WS | 10.31 WS | 10.31 WS |
| 4 | M2 brass insert x8 (SI IUTB-M2-318, 3.18 mm OD) | 8 | 0.33 MO (buy 10) | 0.33 MO | 0.33 MO | 0.27 MO | 0.27 MO | 0.24 MO |
| 5 | ASPHSPH24K102 | 8 | 0.40 DK | 0.32 DK | 0.30 MO | 0.29 MO | 0.27 MO | 0.26 MO |
| 6 | 146153-0100 | 1 | 2.59 DK | 2.59 DK | 1.94 MO | 1.82 MO | 1.82 MO | 1.73 MO |
| 7 | KMR221GLFS | 3 | 0.67 DK | 0.58 DK | 0.54 DK | 0.54 DK | 0.48 DK | 0.44 DK |
| 8 | CL10A106MA8NRNC | 6 | 0.19 DK (buy 10) | 0.19 DK | 0.14 DK | 0.12 DK | 0.12 DK | 0.0942 DK |
| 9 | U.FL-R-SMT-1(10) | 1 | 1.67 DK | 1.67 DK | 1.42 DK | 1.27 MO | 1.26 DK | 1.20 DK |
| 10 | 8240026 | 1 | 1.09 DK | 1.09 DK | 1.03 MO | 1.03 MO | 0.97 DK | 0.90 DK |
| 11 | M2 x 5 screws x12 (4 board, 4 button head, 4 PT for the LCD) | 12 | 0.08 EST | 0.08 EST | 0.08 EST | 0.08 EST | 0.08 EST | 0.08 EST |
| 12 | Ledger wedge stand (PETG, solid 80 cm3 part) | 1 | $0.82/part (40.9 g) | same | same | same | same | same |
| 13 | CL21A226MOQNNNE | 1 | 0.63 MO | 0.63 MO | 0.37 MO | 0.37 MO | 0.26 MO | 0.23 MO |
| 14 | GCM155R71C104KA55D | 11 | 0.034 DK | 0.023 DK | 0.0196 DK | 0.0196 DK | 0.0139 DK | 0.0139 DK |
| 15 | SWPA4020S2R2NT | 1 | 0.34 DK | 0.34 DK | 0.28 DK | 0.28 DK | 0.28 DK | 0.23 DK |
| 16 | S8B-PH-K-S(LF)(SN) | 1 | 0.33 DK | 0.33 DK | 0.28 DK | 0.28 DK | 0.28 DK | 0.27 MO |
| 17 | Ledger front shell (PETG) | 1 | $0.32/part (15.8 g) | same | same | same | same | same |
| 18 | Foam/TPU gasket + bezel adhesive (optional in the notes) | 1 | 0.30 EST | 0.30 EST | 0.30 EST | 0.30 EST | 0.30 EST | 0.30 EST |
| 19 | TLV62569DBVR | 1 | 0.28 DK | 0.28 DK | 0.19 MO | 0.17 MO | 0.17 MO | 0.14 MO |
| 20 | LTST-C190TBKT | 1 | 0.26 DK | 0.26 DK | 0.18 DK | 0.18 DK | 0.18 DK | 0.12 DK |
| 21 | PHR-8 | 2 | 0.11 DK | 0.095 DK | 0.095 DK | 0.085 DK | 0.0809 DK | 0.0809 DK |
| 22 | LTST-C170KGKT | 1 | 0.19 DK | 0.19 DK | 0.13 DK | 0.13 DK | 0.13 DK | 0.0901 DK |
| 23 | TYPE-C-31-M-12 (Gateway J1 USB-C) | 1 | 0.19 LCSC | 0.19 LCSC | 0.19 LCSC | 0.19 LCSC | 0.19 LCSC | 0.19 LCSC |
| 24 | LTST-C191KRKT | 1 | 0.15 DK | 0.15 DK | 0.10 DK | 0.10 DK | 0.10 DK | 0.0715 DK |
| 25 | Ledger rear cover (PETG) | 1 | $0.15/part (7.4 g) | same | same | same | same | same |
| 26 | RB521S30-AU_R1_000A1 | 1 | 0.14 DK | 0.063 MO (buy 10) | 0.063 MO | 0.063 MO | 0.059 DK | 0.0511 DK |
| 27 | BLM18KG221SN1D | 1 | 0.14 DK | 0.14 DK | 0.10 DK | 0.079 MO | 0.0786 DK | 0.0703 DK |
| 28 | ERJ-2RKF2202X | 1 | 0.11 DK | 0.033 DK (buy 10) | 0.033 DK | 0.0248 DK | 0.02 DK | 0.0164 DK |
| 29 | RC0402FR-075K1L | 4 | 0.011 MO (buy 10) | 0.011 MO | 0.011 MO | 0.007 MO | 0.007 MO | 0.007 MO |
| 30 | ERJ-2GE0R00X | 5 | 0.011 MO (buy 10) | 0.011 MO | 0.011 DK | 0.0095 DK | 0.008 MO | 0.0071 DK |
| 31 | RC0402FR-0710KL | 3 | 0.011 MO (buy 10) | 0.011 MO | 0.011 MO | 0.007 MO (buy 100) | 0.007 MO | 0.007 MO |
| 32 | RC0402FR-07100RL | 4 | 0.011 MO (buy 10) | 0.011 MO | 0.011 MO | 0.007 MO | 0.007 MO | 0.007 MO |
| 33 | RC0402FR-0733RL | 3 | 0.011 MO (buy 10) | 0.011 MO | 0.011 MO | 0.007 MO (buy 100) | 0.007 MO | 0.007 MO |
| 34 | RC0402FR-07100KL | 1 | 0.10 DK | 0.011 MO (buy 10) | 0.011 MO | 0.011 MO | 0.011 MO | 0.007 MO |
| 35 | RC0402FR-07470RL | 1 | 0.10 DK | 0.011 MO (buy 10) | 0.011 MO | 0.011 MO | 0.011 MO | 0.007 MO |
| 36 | Ledger key cap (PETG) | 1 | $0.006/part (0.3 g) | same | same | same | same | same |
| 37 | Ledger bezel insert (PETG) | 1 | $0.005/part (0.3 g) | same | same | same | same | same |
| 38 | Ledger foot strip 1 (TPU, final) | 1 | $0.003/part (0.1 g) | same | same | same | same | same |
| 39 | Ledger foot strip 1 (PETG, draft) | 1 | $0.002/part (0.1 g) | same | same | same | same | same |
| 40 | Ledger status pill (PETG; translucent PETG/PCTG in the final) | 1 | $0.002/part (0.1 g) | same | same | same | same | same |
| 41 | Ledger foot strip 2 (TPU, final) | 1 | $0.002/part (0.1 g) | same | same | same | same | same |
| 42 | Ledger foot strip 2 (PETG, draft) | 1 | $0.001/part (0.1 g) | same | same | same | same | same |
| 43 | Ledger foot strip 3 (TPU, final) | 1 | $0.001/part (0.0 g) | same | same | same | same | same |
| 44 | Ledger foot strip 3 (PETG, draft) | 1 | $0.001/part (0.0 g) | same | same | same | same | same |

## 5. Price breaks

### 5a. Top cost drivers: distributor break quantities and the N where each break is reached

Break list = quantity:unit price in USD. "Kicks in" = the product count N at which the combined quantity reaches the break (only breaks reached by N<=100). Saving = line cost per product at N=1 minus at N=100 (all effects).

- **LBES0ZZ2FR-580** (qty 1): $23.41/product at N=1, $17.95 at N=100 (saves $5.46, 23 %).
  - DK 490-LBES0ZZ2FR-580CT-ND (stock 103): 1:23.41 10:20.412 25:19.3736 100:17.9498 | kicks in at 10 (N>=10), 25 (N>=25), 100 (N>=100)
  - Mouser 81-LBES0ZZ2FR-580 (stock 0): 1:21.52 10:18.76 25:17.8 100:16.48 | kicks in at 10 (N>=10), 25 (N>=25), 100 (N>=100)
- **Waveshare 2inch LCD module (SKU 17344)** (qty 1): $10.59/product at N=1, $10.31 at N=100 (saves $0.28, 3 %).
  - Waveshare waveshare.com 2inch-lcd-module (stock n/a): 1:10.59 10:10.39 50:10.31 100:10.31 | kicks in at 10 (N>=10), 50 (N>=50), 100 (N>=100)
- **M2 brass insert x8 (SI IUTB-M2-318, 3.18 mm OD)** (qty 8): $3.33/product at N=1, $1.92 at N=100 (saves $1.41, 42 %).
  - Mouser 153-IUTB-M2-318 (stock 9581): 1:0.47 10:0.333 100:0.267 500:0.24 1000:0.217 | kicks in at 10 (N>=2), 100 (N>=13), 500 (N>=63)
- **ASPHSPH24K102** (qty 8): $3.20/product at N=1, $2.04 at N=100 (saves $1.16, 36 %).
  - DK 455-3358-ND (stock 41677): 1:0.4 10:0.342 25:0.3208 50:0.3054 100:0.2908 250:0.2726 500:0.2595 1000:0.2471 | kicks in at 10 (N>=2), 25 (N>=4), 50 (N>=7), 100 (N>=13), 250 (N>=32), 500 (N>=63)
  - Mouser 306-ASPHSPH24K102 (stock 829): 1:0.4 10:0.342 25:0.321 50:0.302 100:0.289 250:0.269 500:0.255 1000:0.24 | kicks in at 10 (N>=2), 25 (N>=4), 50 (N>=7), 100 (N>=13), 250 (N>=32), 500 (N>=63)
- **146153-0100** (qty 1): $2.59/product at N=1, $1.73 at N=100 (saves $0.86, 33 %).
  - DK WM12218-ND (stock 44175): 1:2.59 10:2.238 25:2.114 100:1.9429 | kicks in at 10 (N>=10), 25 (N>=25), 100 (N>=100)
  - Mouser 538-146153-0100 (stock 23085): 1:2.59 10:1.94 25:1.82 100:1.73 | kicks in at 10 (N>=10), 25 (N>=25), 100 (N>=100)
- **KMR221GLFS** (qty 3): $2.01/product at N=1, $1.33 at N=100 (saves $0.68, 34 %).
  - DK 108-KMR221GLFSCT-ND (stock 107264): 1:0.67 10:0.576 25:0.5368 100:0.4792 250:0.4438 500:0.4191 | kicks in at 10 (N>=4), 25 (N>=9), 100 (N>=34), 250 (N>=84)
  - Mouser 611-KMR221G-LFS (stock 37193): 1:0.67 10:0.576 25:0.537 100:0.48 250:0.444 500:0.42 | kicks in at 10 (N>=4), 25 (N>=9), 100 (N>=34), 250 (N>=84)
- **CL10A106MA8NRNC** (qty 6): $1.87/product at N=1, $0.57 at N=100 (saves $1.30, 70 %).
  - DK 1276-1869-1-ND (stock 147301): 1:0.32 10:0.187 50:0.136 100:0.1205 500:0.0942 | kicks in at 10 (N>=2), 50 (N>=9), 100 (N>=17), 500 (N>=84)
  - Mouser 187-CL10A106MA8NRNC (stock 2562): 1:0.63 10:0.36 50:0.26 100:0.231 500:0.181 2000:0.104 | kicks in at 10 (N>=2), 50 (N>=9), 100 (N>=17), 500 (N>=84)
- **U.FL-R-SMT-1(10)** (qty 1): $1.67/product at N=1, $1.20 at N=100 (saves $0.47, 28 %).
  - DK H11891CT-ND (stock 351360): 1:1.67 10:1.417 25:1.3276 50:1.2642 100:1.2038 | kicks in at 10 (N>=10), 25 (N>=25), 50 (N>=50), 100 (N>=100)
  - Mouser 798-U.FL-R-SMT-110 (stock 150023): 1:1.67 10:1.42 25:1.27 100:1.21 | kicks in at 10 (N>=10), 25 (N>=25), 100 (N>=100)
- **8240026** (qty 1): $1.09/product at N=1, $0.90 at N=100 (saves $0.19, 17 %).
  - DK 732-4470-1-ND (stock 3209): 1:1.09 10:1.038 50:0.969 100:0.9 | kicks in at 10 (N>=10), 50 (N>=50), 100 (N>=100)
  - Mouser 710-8240026 (stock 14880): 1:1.09 10:1.03 50:0.969 100:0.9 | kicks in at 10 (N>=10), 50 (N>=50), 100 (N>=100)
- **CL21A226MOQNNNE** (qty 1): $0.63/product at N=1, $0.23 at N=100 (saves $0.40, 63 %).
  - DK 1276-2909-1-ND (stock 0): 1:0.32 10:0.19 50:0.1384 100:0.1225 | kicks in at 10 (N>=10), 50 (N>=50), 100 (N>=100)
  - Mouser 187-CL21A226MOQNNNE (stock 133342): 1:0.63 10:0.367 50:0.264 100:0.235 | kicks in at 10 (N>=10), 50 (N>=50), 100 (N>=100)
- **GCM155R71C104KA55D** (qty 11): $0.37/product at N=1, $0.15 at N=100 (saves $0.22, 59 %).
  - DK 490-4759-1-ND (stock 7344999): 1:0.11 10:0.034 50:0.023 100:0.0196 500:0.0139 | kicks in at 10 (N>=1), 50 (N>=5), 100 (N>=10), 500 (N>=46)
  - Mouser 81-GCM155R71C104KA5D (stock 0): 1:0.11 10:0.034 50:0.023 100:0.02 500:0.014 4000:0.013 | kicks in at 10 (N>=1), 50 (N>=5), 100 (N>=10), 500 (N>=46)
- **SWPA4020S2R2NT** (qty 1): $0.34/product at N=1, $0.23 at N=100 (saves $0.11, 31 %).
  - DK 3442-SWPA4020S2R2NTCT-ND (stock 1395): 1:0.34 10:0.284 100:0.2331 | kicks in at 10 (N>=10), 100 (N>=100)
- **S8B-PH-K-S(LF)(SN)** (qty 1): $0.33/product at N=1, $0.27 at N=100 (saves $0.057, 17 %).
  - DK 455-1725-ND (stock 19309): 1:0.33 10:0.277 250:0.2208 | kicks in at 10 (N>=10)
  - Mouser 306-S8BPHKSLFSN (stock 11030): 1:0.33 10:0.277 100:0.273 | kicks in at 10 (N>=10), 100 (N>=100)
- **TLV62569DBVR** (qty 1): $0.28/product at N=1, $0.14 at N=100 (saves $0.14, 50 %).
  - DK 296-47360-1-ND (stock 240847): 1:0.28 10:0.19 25:0.168 100:0.1439 | kicks in at 10 (N>=10), 25 (N>=25), 100 (N>=100)
  - Mouser 595-TLV62569DBVR (stock 27832): 1:0.28 10:0.187 25:0.165 100:0.141 | kicks in at 10 (N>=10), 25 (N>=25), 100 (N>=100)

### 5b. Ten lines whose cost per product falls most between N=1 and N=100 ($/product)

| Line | N=1 | N=100 | Saving | Main cause |
|---|---:|---:|---:|---|
| PCB Gateway (PCBWay 4L 1.6 mm ENIG, 20.3 cm2) | $68.45 | $3.63 | $64.82 | PCBWay minimum order of 5 + per-board price |
| LBES0ZZ2FR-580 | $23.41 | $17.95 | $5.46 | distributor price breaks (and buy-up of one-per-product parts) |
| M2 brass insert x8 (SI IUTB-M2-318, 3.18 mm OD) | $3.33 | $1.92 | $1.41 | distributor price breaks (and buy-up of one-per-product parts) |
| CL10A106MA8NRNC | $1.87 | $0.57 | $1.30 | distributor price breaks (and buy-up of one-per-product parts) |
| ASPHSPH24K102 | $3.20 | $2.04 | $1.16 | distributor price breaks (and buy-up of one-per-product parts) |
| 146153-0100 | $2.59 | $1.73 | $0.86 | distributor price breaks (and buy-up of one-per-product parts) |
| KMR221GLFS | $2.01 | $1.33 | $0.68 | distributor price breaks (and buy-up of one-per-product parts) |
| U.FL-R-SMT-1(10) | $1.67 | $1.20 | $0.47 | distributor price breaks (and buy-up of one-per-product parts) |
| CL21A226MOQNNNE | $0.63 | $0.23 | $0.40 | distributor price breaks (and buy-up of one-per-product parts) |
| Waveshare 2inch LCD module (SKU 17344) | $10.59 | $10.31 | $0.28 | distributor price breaks (and buy-up of one-per-product parts) |

### 5c. Where buying up to the next break is cheaper than the exact quantity

Only cases where the extra pieces cost less than the exact quantity (savings >= $0.005 on the order). The spare parts bought are included in the cost curve above.

| Line | N | Need | Buy | Exact-qty cost | Buy-up cost | Saving | Source |
|---|---:|---:|---:|---:|---:|---:|---|
| M2 brass insert x8 (SI IUTB-M2-318, 3.18 mm OD) | 1 | 8 | 10 | $3.76 | $3.33 | $0.43 | Mouser |
| CL10A106MA8NRNC | 1 | 6 | 10 | $1.92 | $1.87 | $0.050 | DK |
| RB521S30-AU_R1_000A1 | 5 | 5 | 10 | $0.70 | $0.63 | $0.070 | Mouser |
| ERJ-2RKF2202X | 5 | 5 | 10 | $0.55 | $0.33 | $0.22 | DK |
| RC0402FR-075K1L | 1 | 4 | 10 | $0.40 | $0.11 | $0.29 | Mouser |
| ERJ-2GE0R00X | 1 | 5 | 10 | $0.50 | $0.11 | $0.39 | Mouser |
| RC0402FR-0710KL | 1 | 3 | 10 | $0.30 | $0.11 | $0.19 | Mouser |
| RC0402FR-0710KL | 25 | 75 | 100 | $0.82 | $0.70 | $0.12 | Mouser |
| RC0402FR-07100RL | 1 | 4 | 10 | $0.40 | $0.11 | $0.29 | Mouser |
| RC0402FR-0733RL | 1 | 3 | 10 | $0.30 | $0.11 | $0.19 | Mouser |
| RC0402FR-0733RL | 25 | 75 | 100 | $0.82 | $0.70 | $0.12 | Mouser |
| RC0402FR-07100KL | 5 | 5 | 10 | $0.50 | $0.11 | $0.39 | Mouser |
| RC0402FR-07470RL | 5 | 5 | 10 | $0.50 | $0.11 | $0.39 | Mouser |

## 6. Stock and lifecycle risks

Stock read 2026-10-29. "Need@100" = qty/product x 100. Flags: SHORT = no single distributor covers the quantity (priced as if stocked, or split where two distributors together cover it); status flags come from DigiKey ProductStatus / Mouser LifecycleStatus and the 2026-10-28 BOM notes.

| Line | Need@100 | Stock (DK / MO / other) | Flags |
|---|---:|---|---|
| LBES0ZZ2FR-580 | 100 | DK 103 / Mouser 0 | tight: best single stock 103 < 2x need; single-source: 0 stock at Mouser |
| GCM155R71C104KA55D | 1100 | DK 7344999 / Mouser 0 | single-source: 0 stock at Mouser |
| CL21A226MOQNNNE | 100 | DK 0 / Mouser 133342 | single-source: 0 stock at DK |
| ERJ-2RKF2202X | 100 | DK 706030 / Mouser 0 | single-source: 0 stock at Mouser |

Lines with no distributor listing at all (LCSC / Atlas / Waveshare / my estimates) have no live stock check: Atlas and Waveshare pages do not state stock; LCSC stock is from jlcsearch (the LCSC page shows none).

## 7. Assumptions and caveats

- **Prices**: DigiKey/Mouser live break tables, cheapest single distributor per line at each N (a split is used only where one distributor cannot cover the quantity). Cut-tape pricing; no Digi-Reel/shipping/tax/tariff/minimum-order fees. Both distributors give free shipping above a threshold, not modelled. Splitting one BOM across the two distributors costs two orders; the cost curve assumes Brian accepts that.
- **Changed since the 2026-10-28 BOMs** (live stock moves): e.g. feather C40 CL10A226MP8NUNE is now 0 at Mouser as well as DK (priced with a 6.3 V alternative, flagged), and several DK/Mouser stock figures are lower or higher than in the BOM CSVs.
- **PCB cost is an ESTIMATE.** PCBWay's online quote page needs a calculation run in the browser (not reachable by fetch; 3 attempts). Method: PCBWay 4-layer 1.6 mm ENIG, small board, no impedance-control surcharge (standard stackup), model total = $38 engineering/setup + boards x area (cm2) x rate, rate per cm2 per board = $0.30 (5 boards), 0.27 (10), 0.22 (25), 0.19 (50), 0.16 (100). Areas: Feather/pH/ORP 50.8 x 22.86 mm = 11.6 cm2; Gateway 58 x 35 mm = 20.3 cm2. Accuracy about +/-30 %. Shipping (typically $20-40 from PCBWay), stencil and optional options (resin-plugged vias etc.) are not included. Replace with a real quote before ordering.
- **Minimum PCB order is 5**: at N<5 the cost of 5 boards is charged to the N products.
- **Filament** (assumptions, as instructed): volume of each draft STL from a binary-STL script (matches the NOTES.md figures: Tidemark sleeve 34.9, cap 12.0, sled 5.2 cm3); grams = volume x 1.27 g/cm3 (PETG) or 1.21 g/cm3 (TPU 95A) x 40 % effective fill; PETG $20/kg, TPU $30/kg (assumed prices, not quotes). The STL volumes are already thin-wall solids, so real use is probably 50-80 % of the solid volume; at 100 % fill filament cost is about 2.5x the figure shown (still under $2 per Tidemark and under $8 per Ledger). Brims, supports, purges and failed prints are not counted. Filament has no price breaks here (spool granularity ignored).
- **Estimated hardware lines (EST)** are my guesses for items not found at DK/Mouser (o-ring cord, ePTFE vent, silica gel, foam, generic M2/M2.5 screws, gasket): each is under $1.50 per product and is flagged.
- **LCSC-only** lines (feather J1 USB-C TYPE-C-31-M-12, R11 FM8625H, sens1/ORP J1 SMA BWSMA-KWE-Z001) are priced at the LCSC single-piece price (jlcsearch, 2026-10-28/29), flat (LCSC break tables not fetched), excluding LCSC shipping. R11 can be omitted per the schematic note (fit R21 0R).
- **Atlas OEM modules** (pH, ORP): price tiers read from atlas-scientific.com 2026-10-29 (1: 45.99, 10: 39.99, 25: 34.99, 50: 29.99, 75: 27.99, 100: 24.99, 500: 19.99). The ORP page was fetched; the pH page returned the identical table. Stock not stated on the pages.
- **Battery**: DK/Mouser carry no 602050 cell; TinyCircuits ASR00012 (3.7 V 1000 mAh) is a PROXY price only; its dimensions were not compared with 6 x 20 x 50 mm.
- **Solar cell + leaf card** are counted in the headline totals (the node has an energy harvester and the leaf card is in the print list); a "without solar" column is given. DigiKey has 48 and Mouser 20 of the LL200-2.4-75, so it is stock-limited for N above about 68.
- **Quantities per product** come from the 2026-10-28/29 live BOMs (DNP parts excluded as in those BOMs); the BOM CSVs were not re-derived from the schematics in this run (read-only task; the BOM files are dated 2026-10-28, the board STATUS says the schematics were not changed afterwards except where noted). The RG316 pigtail is 0.08 m per node, bought by the whole metre.
- No assembly labour, tooling (crimper, heat-set iron), consumables (solder, flux, paste, stencil), shipping or tax are included.

