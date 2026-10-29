# Cost analysis: pH node (2026-10-29)

Live DigiKey (Product Information v4) and Mouser Search API price-break tables read 2026-10-29 (USD, US site, cut tape/bulk; shipping, tax, tariffs and fees excluded). N = number of complete products built in one purchase (all N bought together, so quantity breaks use the combined quantity). Scope: nrf54l15_feather + nrf54l15_feather_sens1 (pH, Atlas pH OEM, isolated) + Tidemark enclosure (Draft 2026-10-29) + battery, solar cell, FFC, RF pigtail.

Read-only analysis: no schematic, PCB or symbol was edited. Prices marked EST are labelled estimates, not quotes.

## 1. Cost per product (cost curve)

Draft = plain PETG, TPU parts left off, key/light pipe in PETG (what is being printed now). Final = TPU key, bung, boot and clip pads at TPU price. Totals per product = total order cost / N.

| N | PCB | Parts | Enclosure | Other | **Total/product (draft)** | Total/product (final) | Draft without solar cell + leaf card | Whole order (draft) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | $110.84 | $95.84 | $27.31 | $33.43 | **$267.41** | $267.44 | $262.33 | $267.41 |
| 5 | $22.17 | $92.25 | $26.35 | $25.18 | **$165.94** | $165.97 | $160.86 | $829.70 |
| 10 | $13.87 | $77.47 | $23.55 | $21.94 | **$136.83** | $136.86 | $132.72 | $1368.29 |
| 25 | $8.15 | $70.51 | $21.76 | $21.42 | **$121.84** | $121.87 | $117.61 | $3045.89 |
| 50 | $5.93 | $63.75 | $20.47 | $21.06 | **$111.21** | $111.24 | $107.03 | $5560.55 |
| 100 | $4.48 | $56.46 | $18.86 | $19.91 | **$99.70** | $99.73 | $96.28 | $9969.89 |

Split: PCB = bare boards; Parts = schematic BOM(s) incl. the Atlas OEM module and LCSC-only lines; Enclosure = printed filament + enclosure hardware (inserts, screws, o-ring, vent, desiccant, bulkhead); Other = battery, solar cell, FFC, RF pigtail parts, LCD.

Percent split of the draft total:

| N | PCB | Parts | Enclosure | Other |
|---:|---:|---:|---:|---:|
| 1 | 41 % | 36 % | 10 % | 13 % |
| 5 | 13 % | 56 % | 16 % | 15 % |
| 10 | 10 % | 57 % | 17 % | 16 % |
| 25 | 7 % | 58 % | 18 % | 18 % |
| 50 | 5 % | 57 % | 18 % | 19 % |
| 100 | 4 % | 57 % | 19 % | 20 % |

Note on PCBs: PCBWay minimum order is 5 boards, so at N=1 the PCB line carries the cost of 5 boards (4 spares); the per-product PCB cost falls steeply to N=10 then flattens.

## 2. Board and sub-assembly subtotals (stand-alone, $ per board/assembly, draft)

So other node combinations can be added up. Stand-alone figures: identical parts on two boards are not merged here, so they add up to slightly more than the merged product total.

| Item | N=1 | N=5 | N=10 | N=25 | N=50 | N=100 |
|---|---:|---:|---:|---:|---:|---:|
| Feather board (PCB + BOM) | $90.90 | $44.02 | $32.93 | $28.79 | $26.10 | $23.65 |
| pH sens1 board (PCB + BOM + Atlas OEM + J1) | $115.88 | $70.86 | $58.50 | $49.93 | $43.69 | $37.34 |
| Tidemark enclosure kit, incl. battery, FFC, pigtail parts, solar cell + leaf card | $60.74 | $51.53 | $45.49 | $43.18 | $41.53 | $38.76 |
|   of which printed filament only | $0.72 | $0.72 | $0.72 | $0.72 | $0.72 | $0.72 |
|   of which solar cell + leaf card | $5.08 | $5.08 | $4.11 | $4.23 | $4.18 | $3.42 |

## 3. Every line, ranked by extended cost per product at N=1

$/product = line cost of the whole order / N, including any buy-up (see section 5). Var: both = in draft and final; D = draft only; F = final only (counted in the Final total, not the Draft total). Src N=1 / N=100 = cheapest source (DK = DigiKey, MO = Mouser, LCSC, Atlas, WS = Waveshare, EST = my estimate, print = own printer). Rank100 = rank of the line at N=100.

| # | Line | Group | Qty/prod | Var | $ N=1 | N=5 | N=10 | N=25 | N=50 | N=100 | Src 1 / 100 | Rank100 |
|---:|---|---|---:|:--:|---:|---:|---:|---:|---:|---:|---|---:|
| 1 | PCB Feather (PCBWay 4L 1.6 mm ENIG, 11.6 cm2) | PCB | 1 | both | 55.42 | 11.08 | 6.94 | 4.07 | 2.97 | 2.24 | PCB est / PCB est | 13 |
| 2 | PCB pH sens1 (PCBWay 4L 1.6 mm ENIG, 11.6 cm2) | PCB | 1 | both | 55.42 | 11.08 | 6.94 | 4.07 | 2.97 | 2.24 | PCB est / PCB est | 14 |
| 3 | Atlas pH OEM circuit (U2) (pH sens1: U2) | Parts | 1 | both | 45.99 | 45.99 | 39.99 | 34.99 | 29.99 | 24.99 | Atlas / Atlas | 1 |
| 4 | SMA bulkhead jack IP67 (Amphenol 901-10796) | Enclosure | 1 | both | 19.68 | 19.68 | 16.93 | 15.84 | 14.55 | 13.22 | MO / MO | 2 |
| 5 | RG316 coax, 0.08 m per pigtail (Huber+Suhner ENVIROFLEX_316, sold per metre) | Other | 0.08 | both | 10.31 | 2.06 | 1.03 | 0.82 | 0.82 | 0.74 | DK / DK | 21 |
| 6 | LiPo 3.7 V ~1000 mAh (TinyCircuits ASR00012, proxy for 602050) | Other | 1 | both | 9.95 | 9.95 | 9.95 | 9.95 | 9.95 | 9.95 | DK / DK | 3 |
| 7 | ADUM1250ARZ-RL7 (pH sens1: U3) | Parts | 1 | both | 8.22 | 8.22 | 6.37 | 5.90 | 5.90 | 5.39 | DK / DK | 4 |
| 8 | MSASJ31LBB5227MTCA01 (Feather: C43) | Parts | 1 | both | 5.42 | 5.42 | 3.91 | 3.91 | 3.31 | 3.13 | DK / DK | 7 |
| 9 | Solar cell PowerFilm LL200-2.4-75 | Other | 1 | both | 4.95 | 4.95 | 3.98 | 4.10 | 4.05 | 3.29 | MO / MO! | 6 |
| 10 | nRF54L15-QFAA-R (Feather: U6) | Parts | 1 | both | 4.38 | 4.38 | 3.57 | 3.32 | 3.32 | 3.03 | DK / MO | 9 |
| 11 | FFC jumper 14-way 0.5 mm, 30 mm (Molex 15020-0139) | Other | 1 | both | 4.23 | 4.23 | 3.59 | 3.36 | 3.20 | 3.05 | DK / DK | 8 |
| 12 | AEM10330-QFN (Feather: IC1) | Parts | 1 | both | 4.22 | 4.22 | 3.29 | 3.29 | 3.29 | 3.29 | MO / MO | 5 |
| 13 | M2.5 brass insert x8 (SI IUTFB-M2.5) | Enclosure | 8 | both | 4.03 | 3.22 | 3.22 | 2.58 | 2.58 | 2.32 | MO / MO | 12 |
| 14 | SMA right-angle crimp plug for RG316 (Taoglas SMAMRA.P.DK.HT) | Other | 1 | both | 3.99 | 3.99 | 3.39 | 3.18 | 3.03 | 2.88 | DK / DK | 11 |
| 15 | NXE1S0303MC-R13 (pH sens1: U4) | Parts | 1 | both | 3.30 | 3.18 | 3.12 | 3.06 | 3.01 | 2.96 | DK / DK | 10 |
| 16 | nPM1300-QEAA-R7 (Feather: U2) | Parts | 1 | both | 2.95 | 2.95 | 2.21 | 2.02 | 2.02 | 1.81 | DK / DK | 16 |
| 17 | 5034801400 (Feather: CN1; pH sens1: CN1) | Parts | 2 | both | 2.80 | 2.38 | 2.38 | 2.12 | 2.02 | 2.02 | DK / DK | 15 |
| 18 | U.FL-R-SMT-1(10) (Feather: RF1) | Parts | 1 | both | 1.67 | 1.67 | 1.42 | 1.27 | 1.26 | 1.20 | DK / DK | 17 |
| 19 | CC0603MRX5R8BB106 (Feather: C16) | Parts | 1 | both | 1.35 | 1.35 | 0.86 | 0.86 | 0.67 | 0.62 | DK / DK | 22 |
| 20 | FTSH-105-01-L-DV-K (Feather: J3) | Parts | 1 | both | 1.19 | 1.19 | 1.19 | 1.19 | 1.19 | 0.97 | MO / MO | 19 |
| 21 | B3U-1000P (Feather: SW1) | Parts | 1 | both | 1.12 | 1.12 | 0.97 | 0.86 | 0.86 | 0.81 | MO / MO | 20 |
| 22 | O-ring cord 2.0 mm silicone/EPDM, 154 mm loop | Enclosure | 1 | both | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | EST / EST | 18 |
| 23 | GRM21BR61E106MA73L (Feather: C7,C17,C18,C20,C22) | Parts | 5 | both | 0.85 | 0.47 | 0.34 | 0.29 | 0.29 | 0.22 | DK / DK | 35 |
| 24 | TPD1E10B06DPYR (Feather: D1,D2) | Parts | 2 | both | 0.82 | 0.36 | 0.36 | 0.36 | 0.32 | 0.32 | DK / DK | 31 |
| 25 | CC0603KRX7R9BB104 | Parts | 6 | both | 0.73 | 0.44 | 0.33 | 0.25 | 0.25 | 0.20 | MO / MO | 37 |
| 26 | GRM188R60J476ME15D (Feather: C42) | Parts | 1 | both | 0.72 | 0.72 | 0.49 | 0.49 | 0.37 | 0.33 | MO / MO | 29 |
| 27 | LSCND1608HKT2R2MF (Feather: L9,L10) | Parts | 2 | both | 0.60 | 0.49 | 0.49 | 0.49 | 0.40 | 0.40 | MO / MO | 26 |
| 28 | M2.5 x 20 nylon screw x4 (Essentra 50M025045P020) | Enclosure | 4 | both | 0.60 | 0.44 | 0.40 | 0.35 | 0.35 | 0.32 | DK / DK | 30 |
| 29 | Adhesive ePTFE vent, 3.0 mm hole | Enclosure | 1 | both | 0.60 | 0.60 | 0.60 | 0.60 | 0.60 | 0.60 | EST / EST | 23 |
| 30 | 2450AT18A0100001E (Feather: AE1) | Parts | 1 | both | 0.52 | 0.52 | 0.45 | 0.42 | 0.42 | 0.38 | DK / DK | 27 |
| 31 | J1 SMA right angle BWSMA-KWE-Z001 (pH sens1: J1) | Parts | 1 | both | 0.51 | 0.51 | 0.51 | 0.51 | 0.51 | 0.51 | LCSC / LCSC | 24 |
| 32 | GRM033R61A225ME47D (Feather: C1,C10) | Parts | 2 | both | 0.50 | 0.30 | 0.30 | 0.21 | 0.18 | 0.18 | MO / MO | 39 |
| 33 | M2.5 x 6 socket cap screw x4 (stainless) | Enclosure | 4 | both | 0.48 | 0.48 | 0.48 | 0.48 | 0.48 | 0.48 | EST / EST | 25 |
| 34 | MF-FSMF020X-2 (Feather: F1) | Parts | 1 | both | 0.45 | 0.45 | 0.41 | 0.41 | 0.34 | 0.31 | MO / MO | 32 |
| 35 | SN74AUP1G34DCKR (Feather: U7) | Parts | 1 | both | 0.44 | 0.44 | 0.30 | 0.27 | 0.27 | 0.23 | DK / DK | 34 |
| 36 | SMF12A (Feather: D3) | Parts | 1 | both | 0.42 | 0.37 | 0.18 | 0.18 | 0.18 | 0.16 | MO / MO | 45 |
| 37 | GRM188R61H225KE11D (Feather: C3) | Parts | 1 | both | 0.40 | 0.40 | 0.24 | 0.24 | 0.17 | 0.15 | MO / MO | 48 |
| 38 | Tidemark sleeve (PETG) | Enclosure | 1 | both | 0.35 | 0.35 | 0.35 | 0.35 | 0.35 | 0.35 | print / print | 28 |
| 39 | GRM155R60J106ME15D (Feather: C41,C54) | Parts | 2 | both | 0.34 | 0.19 | 0.19 | 0.13 | 0.12 | 0.12 | DK / DK | 51 |
| 40 | XRCGB32M000F1S2AR0 (Feather: X1) | Parts | 1 | both | 0.33 | 0.33 | 0.28 | 0.26 | 0.26 | 0.24 | DK / MO | 33 |
| 41 | CL05A105KO5NNNC (Feather: C19; pH sens1: C1,C5) | Parts | 3 | both | 0.30 | 0.13 | 0.13 | 0.087 | 0.074 | 0.074 | DK / DK | 57 |
| 42 | RT0402BRD0710KL (Feather: R17,R18,R19) | Parts | 3 | both | 0.30 | 0.22 | 0.22 | 0.22 | 0.21 | 0.21 | DK / DK | 36 |
| 43 | SML-P12MTT86R (Feather: LED1) | Parts | 1 | both | 0.28 | 0.28 | 0.31 | 0.31 | 0.30 | 0.15 | DK / MO | 47 |
| 44 | GRM188R61C106MA73D (Feather: C46) | Parts | 1 | both | 0.26 | 0.26 | 0.15 | 0.15 | 0.15 | 0.15 | MO / MO | 46 |
| 45 | CL10A226MP8NUNE (Feather: C40) | Parts | 1 | both | 0.25 | 0.25 | 0.14 | 0.14 | 0.10 | 0.091 | MO / MO | 54 |
| 46 | LQM18PN4R7MFRL (Feather: L7) | Parts | 1 | both | 0.25 | 0.25 | 0.21 | 0.21 | 0.21 | 0.17 | DK / DK | 40 |
| 47 | DFE252010F-100M=P2 (Feather: L11) | Parts | 1 | both | 0.25 | 0.25 | 0.21 | 0.21 | 0.21 | 0.17 | DK / DK | 41 |
| 48 | LQP03HQ2N7B02D (Feather: L2,L5) | Parts | 2 | both | 0.24 | 0.20 | 0.20 | 0.20 | 0.17 | 0.17 | DK / DK | 42 |
| 49 | LQP03HQ3N5B02D (Feather: L6,L8) | Parts | 2 | both | 0.24 | 0.20 | 0.20 | 0.20 | 0.17 | 0.17 | DK / DK | 43 |
| 50 | S2B-PH-K-S(LF)(SN) (Feather: U4,U5) | Parts | 2 | both | 0.24 | 0.20 | 0.20 | 0.20 | 0.17 | 0.17 | DK / DK | 44 |
| 51 | GCM155R71C104KA55D (Feather: C45,C48) | Parts | 2 | both | 0.22 | 0.068 | 0.068 | 0.046 | 0.039 | 0.039 | DK / DK | 66 |
| 52 | CRCW04024K70FKED (pH sens1: R3,R4) | Parts | 2 | both | 0.20 | 0.040 | 0.040 | 0.038 | 0.031 | 0.031 | DK / DK | 70 |
| 53 | CL03A104KQ3NNNC (Feather: C49,C50) | Parts | 2 | both | 0.19 | 0.038 | 0.038 | 0.024 | 0.021 | 0.021 | DK / DK | 72 |
| 54 | CL05A105KA5NQNC (Feather: C51) | Parts | 1 | both | 0.19 | 0.19 | 0.11 | 0.11 | 0.077 | 0.068 | DK / DK | 58 |
| 55 | TYPE-C-31-M-12 (Feather: J1) | Parts | 1 | both | 0.19 | 0.19 | 0.19 | 0.19 | 0.19 | 0.19 | LCSC / LCSC | 38 |
| 56 | CL21A475KAQNNNE (Feather: C44) | Parts | 1 | both | 0.16 | 0.16 | 0.087 | 0.087 | 0.060 | 0.052 | MO / MO | 62 |
| 57 | GRM188R71A225KE15D (pH sens1: C3) | Parts | 1 | both | 0.16 | 0.16 | 0.087 | 0.087 | 0.061 | 0.053 | DK / DK | 59 |
| 58 | Tidemark leaf card for LL200-2.4-75 (PETG) | Enclosure | 1 | both | 0.13 | 0.13 | 0.13 | 0.13 | 0.13 | 0.13 | print / print | 49 |
| 59 | Tidemark foot cap (PETG) | Enclosure | 1 | both | 0.12 | 0.12 | 0.12 | 0.12 | 0.12 | 0.12 | print / print | 50 |
| 60 | GJM0335C1E2R0WB01D (Feather: C5) | Parts | 1 | both | 0.12 | 0.12 | 0.068 | 0.068 | 0.047 | 0.041 | DK / DK | 65 |
| 61 | CL05C101JB5NNNC (Feather: C47) | Parts | 1 | both | 0.12 | 0.060 | 0.030 | 0.030 | 0.020 | 0.017 | MO / MO | 73 |
| 62 | LQP03HQ3N9B02D (Feather: L3) | Parts | 1 | both | 0.12 | 0.12 | 0.10 | 0.10 | 0.10 | 0.084 | DK / DK | 55 |
| 63 | GJM0335C1E1R5WB01D (Feather: C8) | Parts | 1 | both | 0.11 | 0.11 | 0.060 | 0.060 | 0.041 | 0.035 | DK / DK | 68 |
| 64 | GJM0335C1E1R0WB01D (Feather: C12) | Parts | 1 | both | 0.11 | 0.11 | 0.062 | 0.062 | 0.042 | 0.037 | DK / DK | 67 |
| 65 | GJM0335C1ER30WB01D (Feather: C13) | Parts | 1 | both | 0.11 | 0.11 | 0.058 | 0.058 | 0.040 | 0.035 | DK / DK | 69 |
| 66 | RC0402FR-074K7L (Feather: R12,R13,R15,R16) | Parts | 4 | both | 0.11 | 0.044 | 0.044 | 0.028 | 0.028 | 0.028 | MO / MO | 71 |
| 67 | GCM155R71H103KA55D (Feather: C9) | Parts | 1 | both | 0.10 | 0.054 | 0.027 | 0.027 | 0.018 | 0.015 | DK / DK | 75 |
| 68 | BLM15AG121SN1D (Feather: L4) | Parts | 1 | both | 0.10 | 0.10 | 0.064 | 0.051 | 0.050 | 0.045 | DK / DK | 64 |
| 69 | NCU15XH103F60RC (Feather: R8) | Parts | 1 | both | 0.10 | 0.068 | 0.065 | 0.056 | 0.056 | 0.053 | DK / DK | 61 |
| 70 | ERJ-3GEY0R00V (Feather: R9) | Parts | 1 | both | 0.10 | 0.032 | 0.016 | 0.016 | 0.016 | 0.014 | DK / DK | 76 |
| 71 | RC0603FR-07150KL (Feather: R10) | Parts | 1 | both | 0.10 | 0.028 | 0.014 | 0.014 | 0.014 | 0.008 | DK / MO | 78 |
| 72 | RC0402FR-07560RL (Feather: R14) | Parts | 1 | both | 0.10 | 0.022 | 0.011 | 0.011 | 0.011 | 0.007 | DK / MO | 80 |
| 73 | RC0402FR-0710KL (pH sens1: R1) | Parts | 1 | both | 0.10 | 0.022 | 0.011 | 0.011 | 0.011 | 0.007 | DK / MO | 81 |
| 74 | ERJ-2GE0R00X (pH sens1: R5) | Parts | 1 | both | 0.10 | 0.022 | 0.011 | 0.011 | 0.011 | 0.009 | DK / DK | 77 |
| 75 | Silica gel 2 g sachet | Enclosure | 1 | both | 0.10 | 0.10 | 0.10 | 0.10 | 0.10 | 0.10 | EST / EST | 52 |
| 76 | Foam for battery pocket | Enclosure | 1 | both | 0.10 | 0.10 | 0.10 | 0.10 | 0.10 | 0.10 | EST / EST | 53 |
| 77 | FM8625H (Feather: R11) | Parts | 1 | both | 0.075 | 0.075 | 0.075 | 0.075 | 0.075 | 0.075 | LCSC / LCSC | 56 |
| 78 | Tidemark sled (PETG) | Enclosure | 1 | both | 0.053 | 0.053 | 0.053 | 0.053 | 0.053 | 0.053 | print / print | 60 |
| 79 | Tidemark rim clip 12 mm (PETG) | Enclosure | 1 | both | 0.050 | 0.050 | 0.050 | 0.050 | 0.050 | 0.050 | print / print | 63 |
| 80 | Tidemark SMA boot (TPU, final) | Enclosure | 1 | F | 0.016 | 0.016 | 0.016 | 0.016 | 0.016 | 0.016 | print / print | 74 |
| 81 | Tidemark board spacer x4 (PETG) | Enclosure | 4 | both | 0.008 | 0.008 | 0.008 | 0.008 | 0.008 | 0.008 | print / print | 79 |
| 82 | Tidemark USB bung (TPU, final) | Enclosure | 1 | F | 0.007 | 0.007 | 0.007 | 0.007 | 0.007 | 0.007 | print / print | 82 |
| 83 | Tidemark clip pad 1 (TPU, final) | Enclosure | 1 | F | 0.006 | 0.006 | 0.006 | 0.006 | 0.006 | 0.006 | print / print | 83 |
| 84 | Tidemark clip pad 2 (TPU, final) | Enclosure | 1 | F | 0.004 | 0.004 | 0.004 | 0.004 | 0.004 | 0.004 | print / print | 84 |
| 85 | Tidemark key (TPU, final) | Enclosure | 1 | F | 0.002 | 0.002 | 0.002 | 0.002 | 0.002 | 0.002 | print / print | 85 |
| 86 | Tidemark key (PETG stand-in, draft) | Enclosure | 1 | D | 0.002 | 0.002 | 0.002 | 0.002 | 0.002 | 0.002 | print / print | 86 |
| 87 | Tidemark light pipe (PETG; acrylic rod is the better optic) | Enclosure | 1 | both | 0.001 | 0.001 | 0.001 | 0.001 | 0.001 | 0.001 | print / print | 87 |

`!` after a source = stock at that quantity is short at every distributor (priced as if stocked); see section 6.

Totals of the table: draft = $267.41 (N=1) ... $99.70 (N=100); final = $267.44 ... $99.73.

## 4. Unit price at the quantity actually needed (qty/product x N)

Cell = unit price actually paid (total line cost / pieces bought) with the source; `(buy B)` where buying up to a higher break was cheaper than the exact quantity. Qty needed per N is qty/product x N.

| # | Line | Qty/prod | N=1 | N=5 | N=10 | N=25 | N=50 | N=100 |
|---:|---|---:|---|---|---|---|---|---|
| 1 | PCB Feather (PCBWay 4L 1.6 mm ENIG, 11.6 cm2) | 1 | $11.08/board x 5 boards | $11.08/board x 5 boards | $6.94/board x 10 boards | $4.07/board x 25 boards | $2.97/board x 50 boards | $2.24/board x 100 boards |
| 2 | PCB pH sens1 (PCBWay 4L 1.6 mm ENIG, 11.6 cm2) | 1 | $11.08/board x 5 boards | $11.08/board x 5 boards | $6.94/board x 10 boards | $4.07/board x 25 boards | $2.97/board x 50 boards | $2.24/board x 100 boards |
| 3 | Atlas pH OEM circuit (U2) | 1 | 45.99 Atlas | 45.99 Atlas | 39.99 Atlas | 34.99 Atlas | 29.99 Atlas | 24.99 Atlas |
| 4 | SMA bulkhead jack IP67 (Amphenol 901-10796) | 1 | 19.68 MO | 19.68 MO | 16.93 MO | 15.84 MO | 14.55 MO | 13.22 MO |
| 5 | RG316 coax, 0.08 m per pigtail (Huber+Suhner ENVIROFLEX_316, sold per metre) | 0.08 | 10.31 DK | 10.31 DK | 10.31 DK | 10.31 DK | 10.31 DK | 9.20 DK |
| 6 | LiPo 3.7 V ~1000 mAh (TinyCircuits ASR00012, proxy for 602050) | 1 | 9.95 DK | 9.95 DK | 9.95 DK | 9.95 DK | 9.95 DK | 9.95 DK |
| 7 | ADUM1250ARZ-RL7 | 1 | 8.22 DK | 8.22 DK | 6.37 DK | 5.90 DK | 5.90 DK | 5.39 DK |
| 8 | MSASJ31LBB5227MTCA01 | 1 | 5.42 DK | 5.42 DK | 3.91 DK | 3.91 DK | 3.31 DK | 3.13 DK |
| 9 | Solar cell PowerFilm LL200-2.4-75 | 1 | 4.95 MO | 4.95 MO | 3.98 MO | 4.10 DK | 4.05 MO+DK | 3.29 MO! |
| 10 | nRF54L15-QFAA-R | 1 | 4.38 DK | 4.38 DK | 3.57 MO | 3.32 MO | 3.32 MO | 3.03 MO |
| 11 | FFC jumper 14-way 0.5 mm, 30 mm (Molex 15020-0139) | 1 | 4.23 DK | 4.23 DK | 3.59 DK | 3.36 DK | 3.20 DK | 3.05 DK |
| 12 | AEM10330-QFN | 1 | 4.22 MO | 4.22 MO | 3.29 MO | 3.29 MO | 3.29 MO | 3.29 MO |
| 13 | M2.5 brass insert x8 (SI IUTFB-M2.5) | 8 | 0.40 MO (buy 10) | 0.40 MO | 0.32 MO (buy 100) | 0.32 MO | 0.32 MO | 0.29 MO |
| 14 | SMA right-angle crimp plug for RG316 (Taoglas SMAMRA.P.DK.HT) | 1 | 3.99 DK | 3.99 DK | 3.39 DK | 3.18 DK | 3.03 DK | 2.88 DK |
| 15 | NXE1S0303MC-R13 | 1 | 3.30 DK | 3.18 DK | 3.12 DK | 3.06 DK | 3.01 DK | 2.96 DK |
| 16 | nPM1300-QEAA-R7 | 1 | 2.95 DK | 2.95 DK | 2.21 DK | 2.02 DK | 2.02 DK | 1.81 DK |
| 17 | 5034801400 | 2 | 1.40 DK | 1.19 DK | 1.19 DK | 1.06 DK | 1.01 DK | 1.01 DK |
| 18 | U.FL-R-SMT-1(10) | 1 | 1.67 DK | 1.67 DK | 1.42 DK | 1.27 MO | 1.26 DK | 1.20 DK |
| 19 | CC0603MRX5R8BB106 | 1 | 1.35 DK | 1.35 DK | 0.86 DK | 0.86 DK | 0.67 DK | 0.62 DK |
| 20 | FTSH-105-01-L-DV-K | 1 | 1.19 MO | 1.19 MO | 1.19 MO | 1.19 MO | 1.19 MO | 0.97 MO |
| 21 | B3U-1000P | 1 | 1.12 MO | 1.12 MO | 0.97 MO | 0.86 MO | 0.86 MO | 0.81 MO |
| 22 | O-ring cord 2.0 mm silicone/EPDM, 154 mm loop | 1 | 1.00 EST | 1.00 EST | 1.00 EST | 1.00 EST | 1.00 EST | 1.00 EST |
| 23 | GRM21BR61E106MA73L | 5 | 0.17 DK | 0.095 DK | 0.0672 DK | 0.0585 DK | 0.0585 DK | 0.044 DK |
| 24 | TPD1E10B06DPYR | 2 | 0.41 DK | 0.18 MO | 0.18 MO | 0.18 DK | 0.16 DK | 0.16 DK |
| 25 | CC0603KRX7R9BB104 | 6 | 0.073 MO (buy 10) | 0.073 MO | 0.0554 DK | 0.042 MO | 0.042 MO | 0.033 MO |
| 26 | GRM188R60J476ME15D | 1 | 0.72 MO | 0.72 MO | 0.49 MO | 0.49 MO | 0.37 MO | 0.33 MO |
| 27 | LSCND1608HKT2R2MF | 2 | 0.30 MO | 0.24 MO | 0.24 MO | 0.24 MO | 0.20 MO | 0.20 MO |
| 28 | M2.5 x 20 nylon screw x4 (Essentra 50M025045P020) | 4 | 0.15 DK | 0.11 DK | 0.10 DK | 0.0867 DK | 0.0867 DK | 0.0794 DK |
| 29 | Adhesive ePTFE vent, 3.0 mm hole | 1 | 0.60 EST | 0.60 EST | 0.60 EST | 0.60 EST | 0.60 EST | 0.60 EST |
| 30 | 2450AT18A0100001E | 1 | 0.52 DK | 0.52 DK | 0.45 DK | 0.42 DK | 0.42 DK | 0.38 DK |
| 31 | J1 SMA right angle BWSMA-KWE-Z001 | 1 | 0.51 LCSC | 0.51 LCSC | 0.51 LCSC | 0.51 LCSC | 0.51 LCSC | 0.51 LCSC |
| 32 | GRM033R61A225ME47D | 2 | 0.25 MO | 0.15 MO | 0.15 MO | 0.10 MO | 0.091 MO | 0.091 MO |
| 33 | M2.5 x 6 socket cap screw x4 (stainless) | 4 | 0.12 EST | 0.12 EST | 0.12 EST | 0.12 EST | 0.12 EST | 0.12 EST |
| 34 | MF-FSMF020X-2 | 1 | 0.45 MO | 0.45 DK | 0.41 MO | 0.41 MO | 0.34 MO | 0.31 MO |
| 35 | SN74AUP1G34DCKR | 1 | 0.44 DK | 0.44 DK | 0.30 MO | 0.27 DK | 0.27 DK | 0.23 DK |
| 36 | SMF12A | 1 | 0.42 MO | 0.18 MO (buy 10) | 0.18 MO | 0.18 MO | 0.18 MO | 0.16 MO |
| 37 | GRM188R61H225KE11D | 1 | 0.40 MO | 0.40 MO | 0.24 MO | 0.24 MO | 0.17 MO | 0.15 MO |
| 38 | Tidemark sleeve (PETG) | 1 | $0.35/part (17.7 g) | same | same | same | same | same |
| 39 | GRM155R60J106ME15D | 2 | 0.17 DK | 0.095 DK | 0.095 DK | 0.0666 DK | 0.058 DK | 0.058 DK |
| 40 | XRCGB32M000F1S2AR0 | 1 | 0.33 DK | 0.33 DK | 0.28 MO | 0.26 MO | 0.26 DK | 0.24 MO |
| 41 | CL05A105KO5NNNC | 3 | 0.10 DK | 0.043 DK | 0.043 DK | 0.029 DK | 0.0248 DK | 0.0248 DK |
| 42 | RT0402BRD0710KL | 3 | 0.10 DK | 0.074 MO | 0.074 MO | 0.0734 DK | 0.0694 DK | 0.0694 DK |
| 43 | SML-P12MTT86R | 1 | 0.28 DK | 0.28 DK | 0.31 MO | 0.31 MO | 0.15 MO (buy 100) | 0.15 MO |
| 44 | GRM188R61C106MA73D | 1 | 0.26 MO | 0.26 MO | 0.15 MO | 0.15 MO | 0.15 MO | 0.15 MO |
| 45 | CL10A226MP8NUNE | 1 | 0.25 MO | 0.25 MO | 0.14 MO | 0.14 MO | 0.10 MO | 0.091 MO |
| 46 | LQM18PN4R7MFRL | 1 | 0.25 DK | 0.25 DK | 0.21 DK | 0.21 DK | 0.21 DK | 0.17 DK |
| 47 | DFE252010F-100M=P2 | 1 | 0.25 DK | 0.25 DK | 0.21 DK | 0.21 DK | 0.21 DK | 0.17 DK |
| 48 | LQP03HQ2N7B02D | 2 | 0.12 DK | 0.10 DK | 0.10 DK | 0.10 DK | 0.0837 DK | 0.0837 DK |
| 49 | LQP03HQ3N5B02D | 2 | 0.12 DK | 0.10 DK | 0.10 DK | 0.10 DK | 0.0837 DK | 0.0837 DK |
| 50 | S2B-PH-K-S(LF)(SN) | 2 | 0.12 DK | 0.099 DK | 0.099 DK | 0.099 DK | 0.0837 DK | 0.0837 DK |
| 51 | GCM155R71C104KA55D | 2 | 0.11 DK | 0.034 DK | 0.034 DK | 0.023 DK | 0.0196 DK | 0.0196 DK |
| 52 | CRCW04024K70FKED | 2 | 0.10 DK | 0.02 MO | 0.02 MO | 0.0192 DK | 0.0157 DK | 0.0123 DK (buy 250) |
| 53 | CL03A104KQ3NNNC | 2 | 0.019 DK (buy 10) | 0.019 DK | 0.019 DK | 0.0122 DK | 0.0103 DK | 0.0103 DK |
| 54 | CL05A105KA5NQNC | 1 | 0.19 DK | 0.19 DK | 0.11 DK | 0.11 DK | 0.0772 DK | 0.0675 DK |
| 55 | TYPE-C-31-M-12 | 1 | 0.19 LCSC | 0.19 LCSC | 0.19 LCSC | 0.19 LCSC | 0.19 LCSC | 0.19 LCSC |
| 56 | CL21A475KAQNNNE | 1 | 0.16 MO | 0.16 MO | 0.087 MO | 0.087 MO | 0.06 MO | 0.052 MO |
| 57 | GRM188R71A225KE15D | 1 | 0.16 DK | 0.16 DK | 0.087 DK | 0.087 DK | 0.0612 DK | 0.0532 DK |
| 58 | Tidemark leaf card for LL200-2.4-75 (PETG) | 1 | $0.13/part (6.5 g) | same | same | same | same | same |
| 59 | Tidemark foot cap (PETG) | 1 | $0.12/part (6.1 g) | same | same | same | same | same |
| 60 | GJM0335C1E2R0WB01D | 1 | 0.12 DK | 0.12 DK | 0.068 DK | 0.068 DK | 0.0472 DK | 0.0408 DK |
| 61 | CL05C101JB5NNNC | 1 | 0.12 MO | 0.03 MO (buy 10) | 0.03 MO | 0.03 MO | 0.02 MO | 0.017 MO |
| 62 | LQP03HQ3N9B02D | 1 | 0.12 DK | 0.12 DK | 0.10 DK | 0.10 DK | 0.10 DK | 0.0837 DK |
| 63 | GJM0335C1E1R5WB01D | 1 | 0.11 DK | 0.11 DK | 0.06 DK | 0.06 DK | 0.041 DK | 0.0354 DK |
| 64 | GJM0335C1E1R0WB01D | 1 | 0.11 DK | 0.11 DK | 0.062 DK | 0.062 DK | 0.0424 DK | 0.0366 DK |
| 65 | GJM0335C1ER30WB01D | 1 | 0.11 DK | 0.11 DK | 0.058 DK | 0.058 DK | 0.04 DK | 0.0345 DK |
| 66 | RC0402FR-074K7L | 4 | 0.011 MO (buy 10) | 0.011 MO | 0.011 MO | 0.007 MO | 0.007 MO | 0.007 MO |
| 67 | GCM155R71H103KA55D | 1 | 0.10 DK | 0.027 DK (buy 10) | 0.027 DK | 0.027 DK | 0.018 DK | 0.0153 DK |
| 68 | BLM15AG121SN1D | 1 | 0.10 DK | 0.10 DK | 0.064 DK | 0.051 MO | 0.0502 DK | 0.045 DK |
| 69 | NCU15XH103F60RC | 1 | 0.10 DK | 0.068 DK | 0.065 DK | 0.056 MO | 0.0558 DK | 0.0527 DK |
| 70 | ERJ-3GEY0R00V | 1 | 0.10 DK | 0.016 MO (buy 10) | 0.016 MO | 0.016 MO | 0.0158 DK | 0.0138 DK |
| 71 | RC0603FR-07150KL | 1 | 0.10 DK | 0.014 MO (buy 10) | 0.014 MO | 0.014 MO | 0.014 MO | 0.008 MO |
| 72 | RC0402FR-07560RL | 1 | 0.10 DK | 0.011 MO (buy 10) | 0.011 MO | 0.011 MO | 0.011 MO | 0.007 MO |
| 73 | RC0402FR-0710KL | 1 | 0.10 DK | 0.011 MO (buy 10) | 0.011 MO | 0.011 MO | 0.011 MO | 0.007 MO |
| 74 | ERJ-2GE0R00X | 1 | 0.10 DK | 0.011 MO (buy 10) | 0.011 MO | 0.011 MO | 0.011 DK | 0.0095 DK |
| 75 | Silica gel 2 g sachet | 1 | 0.10 EST | 0.10 EST | 0.10 EST | 0.10 EST | 0.10 EST | 0.10 EST |
| 76 | Foam for battery pocket | 1 | 0.10 EST | 0.10 EST | 0.10 EST | 0.10 EST | 0.10 EST | 0.10 EST |
| 77 | FM8625H | 1 | 0.0753 LCSC | 0.0753 LCSC | 0.0753 LCSC | 0.0753 LCSC | 0.0753 LCSC | 0.0753 LCSC |
| 78 | Tidemark sled (PETG) | 1 | $0.053/part (2.6 g) | same | same | same | same | same |
| 79 | Tidemark rim clip 12 mm (PETG) | 1 | $0.050/part (2.5 g) | same | same | same | same | same |
| 80 | Tidemark SMA boot (TPU, final) | 1 | $0.016/part (0.5 g) | same | same | same | same | same |
| 81 | Tidemark board spacer x4 (PETG) | 4 | $0.002/part (0.1 g) | same | same | same | same | same |
| 82 | Tidemark USB bung (TPU, final) | 1 | $0.007/part (0.2 g) | same | same | same | same | same |
| 83 | Tidemark clip pad 1 (TPU, final) | 1 | $0.006/part (0.2 g) | same | same | same | same | same |
| 84 | Tidemark clip pad 2 (TPU, final) | 1 | $0.004/part (0.1 g) | same | same | same | same | same |
| 85 | Tidemark key (TPU, final) | 1 | $0.002/part (0.1 g) | same | same | same | same | same |
| 86 | Tidemark key (PETG stand-in, draft) | 1 | $0.002/part (0.1 g) | same | same | same | same | same |
| 87 | Tidemark light pipe (PETG; acrylic rod is the better optic) | 1 | $0.001/part (0.0 g) | same | same | same | same | same |

## 5. Price breaks

### 5a. Top cost drivers: distributor break quantities and the N where each break is reached

Break list = quantity:unit price in USD. "Kicks in" = the product count N at which the combined quantity reaches the break (only breaks reached by N<=100). Saving = line cost per product at N=1 minus at N=100 (all effects).

- **Atlas pH OEM circuit (U2)** (qty 1): $45.99/product at N=1, $24.99 at N=100 (saves $21.00, 46 %).
  - Atlas atlas-scientific.com (stock n/a): 1:45.99 10:39.99 25:34.99 50:29.99 75:27.99 100:24.99 | kicks in at 10 (N>=10), 25 (N>=25), 50 (N>=50), 75 (N>=75), 100 (N>=100)
- **SMA bulkhead jack IP67 (Amphenol 901-10796)** (qty 1): $19.68/product at N=1, $13.22 at N=100 (saves $6.46, 33 %).
  - Mouser 523-90110796 (stock 286): 1:19.68 10:16.93 25:15.84 50:14.55 100:13.22 | kicks in at 10 (N>=10), 25 (N>=25), 50 (N>=50), 100 (N>=100)
- **RG316 coax, 0.08 m per pigtail (Huber+Suhner ENVIROFLEX_316, sold per metre)** (qty 0.08): $10.31/product at N=1, $0.74 at N=100 (saves $9.57, 93 %).
  - DK 3628-ENVIROFLEX_316-DS-ND (stock 2811): 1:10.31 5:9.204 10:8.763 | kicks in at 5 (N>=63)
- **LiPo 3.7 V ~1000 mAh (TinyCircuits ASR00012, proxy for 602050)** (qty 1): $9.95/product at N=1, $9.95 at N=100 (saves $0.000, 0 %).
  - DK 1832-1053-ND (stock 183): 1:9.95 | kicks in at no break reached by N=100
  - Mouser 406-ASR00012 (stock 690): 1:9.95 | kicks in at no break reached by N=100
- **ADUM1250ARZ-RL7** (qty 1): $8.22/product at N=1, $5.39 at N=100 (saves $2.83, 34 %).
  - DK 505-ADUM1250ARZ-RL7CT-ND (stock 1203): 1:8.22 10:6.368 25:5.9036 100:5.3935 | kicks in at 10 (N>=10), 25 (N>=25), 100 (N>=100)
  - Mouser 584-ADUM1250ARZ-R7 (stock 0): no price listed | kicks in at no break reached by N=100
- **MSASJ31LBB5227MTCA01** (qty 1): $5.42/product at N=1, $3.13 at N=100 (saves $2.29, 42 %).
  - DK 587-MSASJ31LBB5227MTCA01CT-ND (stock 1556): 1:5.42 10:3.913 50:3.3138 100:3.1284 | kicks in at 10 (N>=10), 50 (N>=50), 100 (N>=100)
  - Mouser 963-MSASJ31LBB5227MT (stock 85): 1:8.61 10:6.36 50:5.37 100:5.13 | kicks in at 10 (N>=10), 50 (N>=50), 100 (N>=100)
- **Solar cell PowerFilm LL200-2.4-75** (qty 1): $4.95/product at N=1, $3.29 at N=100 (saves $1.66, 34 %).
  - DK 1996-1019-ND (stock 48): 1:5.02 10:4.1 50:3.5704 100:3.366 | kicks in at 10 (N>=10), 50 (N>=50), 100 (N>=100)
  - Mouser 730-LL200-2.4-75 (stock 20): 1:4.95 10:3.98 50:3.54 100:3.29 | kicks in at 10 (N>=10), 50 (N>=50), 100 (N>=100)
- **nRF54L15-QFAA-R** (qty 1): $4.38/product at N=1, $3.03 at N=100 (saves $1.35, 31 %).
  - DK 4823-NRF54L15-QFAA-RCT-ND (stock 1002): 1:4.38 10:3.783 25:3.5768 100:3.2934 | kicks in at 10 (N>=10), 25 (N>=25), 100 (N>=100)
  - Mouser 949-NRF54L15-QFAA-R (stock 2177): 1:4.38 10:3.57 25:3.32 100:3.03 | kicks in at 10 (N>=10), 25 (N>=25), 100 (N>=100)
- **FFC jumper 14-way 0.5 mm, 30 mm (Molex 15020-0139)** (qty 1): $4.23/product at N=1, $3.05 at N=100 (saves $1.18, 28 %).
  - DK 0150200139-ND (stock 906): 1:4.23 10:3.59 25:3.3648 50:3.204 100:3.0509 | kicks in at 10 (N>=10), 25 (N>=25), 50 (N>=50), 100 (N>=100)
  - Mouser 538-15020-0139 (stock 1986): 1:4.23 10:3.59 25:3.37 50:3.21 100:3.06 | kicks in at 10 (N>=10), 25 (N>=25), 50 (N>=50), 100 (N>=100)
- **AEM10330-QFN** (qty 1): $4.22/product at N=1, $3.29 at N=100 (saves $0.93, 22 %).
  - Mouser 120-AEM10330-QFN (stock 725): 1:4.22 10:3.29 | kicks in at 10 (N>=10)
- **M2.5 brass insert x8 (SI IUTFB-M2.5)** (qty 8): $4.03/product at N=1, $2.32 at N=100 (saves $1.71, 42 %).
  - Mouser 153-IUTFB-M2.5 (stock 6506): 1:0.56 10:0.403 100:0.322 500:0.29 1000:0.269 | kicks in at 10 (N>=2), 100 (N>=13), 500 (N>=63)
- **SMA right-angle crimp plug for RG316 (Taoglas SMAMRA.P.DK.HT)** (qty 1): $3.99/product at N=1, $2.88 at N=100 (saves $1.11, 28 %).
  - DK 931-SMAMRA.P.DK.HT-ND (stock 732): 1:3.99 10:3.391 25:3.178 50:3.0262 100:2.8816 | kicks in at 10 (N>=10), 25 (N>=25), 50 (N>=50), 100 (N>=100)
- **NXE1S0303MC-R13** (qty 1): $3.30/product at N=1, $2.96 at N=100 (saves $0.34, 10 %).
  - DK 811-3902-1-ND (stock 1633): 1:3.3 5:3.176 10:3.124 25:3.0572 50:3.0076 100:2.9589 | kicks in at 5 (N>=5), 10 (N>=10), 25 (N>=25), 50 (N>=50), 100 (N>=100)
  - Mouser 580-NXE1S0303MC-R13 (stock 0): 1:3.25 5:3.14 10:3.1 25:3.01 50:2.96 100:2.91 | kicks in at 5 (N>=5), 10 (N>=10), 25 (N>=25), 50 (N>=50), 100 (N>=100)
- **nPM1300-QEAA-R7** (qty 1): $2.95/product at N=1, $1.81 at N=100 (saves $1.14, 39 %).
  - DK 4823-NPM1300-QEAA-R7CT-ND (stock 5445): 1:2.95 10:2.205 25:2.0184 100:1.8133 | kicks in at 10 (N>=10), 25 (N>=25), 100 (N>=100)
  - Mouser 949-NPM1300-QEAA-R7 (stock 5641): 1:3.42 10:2.55 25:2.33 100:2.09 | kicks in at 10 (N>=10), 25 (N>=25), 100 (N>=100)

### 5b. Ten lines whose cost per product falls most between N=1 and N=100 ($/product)

| Line | N=1 | N=100 | Saving | Main cause |
|---|---:|---:|---:|---|
| PCB Feather (PCBWay 4L 1.6 mm ENIG, 11.6 cm2) | $55.42 | $2.24 | $53.18 | PCBWay minimum order of 5 + per-board price |
| PCB pH sens1 (PCBWay 4L 1.6 mm ENIG, 11.6 cm2) | $55.42 | $2.24 | $53.18 | PCBWay minimum order of 5 + per-board price |
| Atlas pH OEM circuit (U2) | $45.99 | $24.99 | $21.00 | Atlas tier prices |
| RG316 coax, 0.08 m per pigtail (Huber+Suhner ENVIROFLEX_316, sold per metre) | $10.31 | $0.74 | $9.57 | distributor price breaks (and buy-up of one-per-product parts) |
| SMA bulkhead jack IP67 (Amphenol 901-10796) | $19.68 | $13.22 | $6.46 | distributor price breaks (and buy-up of one-per-product parts) |
| ADUM1250ARZ-RL7 | $8.22 | $5.39 | $2.83 | distributor price breaks (and buy-up of one-per-product parts) |
| MSASJ31LBB5227MTCA01 | $5.42 | $3.13 | $2.29 | distributor price breaks (and buy-up of one-per-product parts) |
| M2.5 brass insert x8 (SI IUTFB-M2.5) | $4.03 | $2.32 | $1.71 | distributor price breaks (and buy-up of one-per-product parts) |
| Solar cell PowerFilm LL200-2.4-75 | $4.95 | $3.29 | $1.66 | distributor price breaks (and buy-up of one-per-product parts) |
| nRF54L15-QFAA-R | $4.38 | $3.03 | $1.35 | distributor price breaks (and buy-up of one-per-product parts) |

### 5c. Where buying up to the next break is cheaper than the exact quantity

Only cases where the extra pieces cost less than the exact quantity (savings >= $0.005 on the order). The spare parts bought are included in the cost curve above.

| Line | N | Need | Buy | Exact-qty cost | Buy-up cost | Saving | Source |
|---|---:|---:|---:|---:|---:|---:|---|
| M2.5 brass insert x8 (SI IUTFB-M2.5) | 1 | 8 | 10 | $4.48 | $4.03 | $0.45 | Mouser |
| M2.5 brass insert x8 (SI IUTFB-M2.5) | 10 | 80 | 100 | $32.24 | $32.20 | $0.040 | Mouser |
| CC0603KRX7R9BB104 | 1 | 6 | 10 | $1.08 | $0.73 | $0.35 | Mouser |
| SMF12A | 5 | 5 | 10 | $2.10 | $1.85 | $0.25 | Mouser |
| SML-P12MTT86R | 50 | 50 | 100 | $15.70 | $15.00 | $0.70 | Mouser |
| CRCW04024K70FKED | 100 | 200 | 250 | $3.14 | $3.07 | $0.070 | DK |
| CL03A104KQ3NNNC | 1 | 2 | 10 | $0.20 | $0.19 | $0.010 | DK |
| CL05C101JB5NNNC | 5 | 5 | 10 | $0.60 | $0.30 | $0.30 | Mouser |
| RC0402FR-074K7L | 1 | 4 | 10 | $0.40 | $0.11 | $0.29 | Mouser |
| GCM155R71H103KA55D | 5 | 5 | 10 | $0.50 | $0.27 | $0.23 | DK |
| ERJ-3GEY0R00V | 5 | 5 | 10 | $0.50 | $0.16 | $0.34 | Mouser |
| RC0603FR-07150KL | 5 | 5 | 10 | $0.50 | $0.14 | $0.36 | Mouser |
| RC0402FR-07560RL | 5 | 5 | 10 | $0.50 | $0.11 | $0.39 | Mouser |
| RC0402FR-0710KL | 5 | 5 | 10 | $0.50 | $0.11 | $0.39 | Mouser |
| ERJ-2GE0R00X | 5 | 5 | 10 | $0.50 | $0.11 | $0.39 | Mouser |

## 6. Stock and lifecycle risks

Stock read 2026-10-29. "Need@100" = qty/product x 100. Flags: SHORT = no single distributor covers the quantity (priced as if stocked, or split where two distributors together cover it); status flags come from DigiKey ProductStatus / Mouser LifecycleStatus and the 2026-10-28 BOM notes.

| Line | Need@100 | Stock (DK / MO / other) | Flags |
|---|---:|---|---|
| 2450AT18A0100001E | 100 | DK 183115 / Mouser 0 | single-source: 0 stock at Mouser |
| GRM033R61A225ME47D | 200 | DK 0 / Mouser 6757 | single-source: 0 stock at DK |
| GRM188R61H225KE11D | 100 | DK 0 / Mouser 230891 | BOM note: original Samsung part NRND (priced part is the Murata equivalent); single-source: 0 stock at DK |
| CC0603MRX5R8BB106 | 100 | DK 48553 / Mouser 0 | single-source: 0 stock at Mouser |
| GRM188R60J476ME15D | 100 | DK 0 / Mouser 1740 | single-source: 0 stock at DK |
| CL21A475KAQNNNE | 100 | DK 0 / Mouser 9804 | single-source: 0 stock at DK |
| GCM155R71C104KA55D | 200 | DK 7344999 / Mouser 0 | single-source: 0 stock at Mouser |
| GRM188R61C106MA73D | 100 | DK 0 / Mouser 1567503 | single-source: 0 stock at DK |
| CL05C101JB5NNNC | 100 | DK 0 / Mouser 15218 | single-source: 0 stock at DK |
| LSCND1608HKT2R2MF | 200 | DK 0 / Mouser 42848 | single-source: 0 stock at DK |
| SML-P12MTT86R | 100 | DK 8 / Mouser 113 | tight: best single stock 113 < 2x need |
| ADUM1250ARZ-RL7 | 100 | DK 1203 / Mouser 0 | single-source: 0 stock at Mouser |
| NXE1S0303MC-R13 | 100 | DK 1633 / Mouser 0 | single-source: 0 stock at Mouser |
| Solar cell PowerFilm LL200-2.4-75 | 100 | DK 48 / Mouser 20 | STOCK-SHORT at N=100; first short at N=100 |

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

