# Cost analysis summary, 2026-10-29

Three products costed from the live DigiKey/Mouser price-break tables read 2026-10-29 (cut tape, USD, no shipping/tax/fees): **pH node** = nrf54l15_feather + nrf54l15_feather_sens1 + Tidemark enclosure; **ORP node** = nrf54l15_feather + feather_orp + Tidemark enclosure; **Gateway** = pouch_gateway + Ledger enclosure + Waveshare 2inch LCD + cable W1. N = complete products bought in one go. Detail and every line: `cost_ph_node.md`, `cost_orp_node.md`, `cost_gateway.md` (+ CSV each) in this folder. Read-only: no design file was edited.

**Two things in the totals are estimates, not quotes:** (1) the PCBWay bare-board price (the online quote needs a browser calculation; modelled, about +/-30 %), (2) a few small hardware lines (o-ring cord, ePTFE vent, silica gel, foam, generic screws, about $3.5 per Tidemark and $1.3 per Ledger). Filament uses assumed $20/kg PETG, $30/kg TPU at 40 % effective fill. See the Assumptions section of each product file.

## 1. Total cost per product (draft = plain PETG)

| N | pH node | ORP node | Gateway |
|---:|---:|---:|---:|
| 1 | **$267.41** | **$266.73** | **$124.87** |
| 5 | **$165.94** | **$165.38** | **$67.07** |
| 10 | **$136.83** | **$135.69** | **$57.08** |
| 25 | **$121.84** | **$120.58** | **$51.63** |
| 50 | **$111.21** | **$109.85** | **$49.58** |
| 100 | **$99.70** | **$98.09** | **$46.09** |

Final variant (TPU key, bung, boot, clip pads / foot strips at TPU price) adds only about $0.03 per node and $0.00 per gateway, so it is not shown separately here (it is in each product file). The node totals include the PowerFilm solar cell + leaf card (about $5 at N=1, $3.4 at N=100); without them the nodes are lower by that amount (columns in the product files).

Whole order cost (draft):

| N | pH node | ORP node | Gateway |
|---:|---:|---:|---:|
| 1 | $267.41 | $266.73 | $124.87 |
| 5 | $829.70 | $826.88 | $335.36 |
| 10 | $1368.29 | $1356.86 | $570.78 |
| 25 | $3045.89 | $3014.62 | $1290.77 |
| 50 | $5560.55 | $5492.72 | $2478.88 |
| 100 | $9969.89 | $9809.20 | $4608.84 |

## 2. Split of the cost per product (draft)

| Product | N | PCB | Parts | Enclosure | Other | Total |
|---|---:|---:|---:|---:|---:|---:|
| pH node | 1 | $110.84 | $95.84 | $27.31 | $33.43 | $267.41 |
| pH node | 10 | $13.87 | $77.47 | $23.55 | $21.94 | $136.83 |
| pH node | 100 | $4.48 | $56.46 | $18.86 | $19.91 | $99.70 |
| ORP node | 1 | $110.84 | $95.16 | $27.31 | $33.43 | $266.73 |
| ORP node | 10 | $13.87 | $76.33 | $23.55 | $21.94 | $135.69 |
| ORP node | 100 | $4.48 | $54.85 | $18.86 | $19.91 | $98.09 |
| Gateway | 1 | $68.45 | $39.94 | $5.89 | $10.59 | $124.87 |
| Gateway | 10 | $9.28 | $32.19 | $5.22 | $10.39 | $57.08 |
| Gateway | 100 | $3.63 | $27.67 | $4.48 | $10.31 | $46.09 |

Other = battery, solar cell, FFC, RF pigtail parts (nodes); LCD (gateway). Enclosure = filament + inserts/screws/o-ring/vent/desiccant/SMA bulkhead.

## 3. Subtotals per board / assembly (stand-alone, draft, $ per item at N items bought)

Add these to build other node combinations (a node = feather + one sensor board + Tidemark kit; stand-alone sums are a few cents above the merged product totals because shared parts such as CN1 are bought together in the product files).

| Item | N=1 | N=5 | N=10 | N=25 | N=50 | N=100 |
|---|---:|---:|---:|---:|---:|---:|
| Feather main board (PCB + BOM) | $90.90 | $44.02 | $32.93 | $28.79 | $26.10 | $23.65 |
| pH sens1 board (PCB + BOM + Atlas pH OEM + J1 SMA) | $115.88 | $70.86 | $58.50 | $49.93 | $43.69 | $37.34 |
| ORP board (PCB + BOM + Atlas ORP OEM + J1 SMA) | $115.54 | $70.31 | $57.41 | $48.70 | $42.34 | $35.77 |
| Gateway board (PCB + BOM + W1 cable parts + antenna) | $108.39 | $51.26 | $41.47 | $36.55 | $34.57 | $31.30 |
| Tidemark enclosure kit (printed + hardware + battery + FFC + pigtail + solar cell/leaf card) | $60.74 | $51.53 | $45.49 | $43.18 | $41.53 | $38.76 |
| Ledger enclosure (printed + hardware) | $5.89 | $5.22 | $5.22 | $4.69 | $4.69 | $4.48 |
| Waveshare 2inch LCD | $10.59 | $10.59 | $10.39 | $10.39 | $10.31 | $10.31 |

PCB-only share of those: Feather/sens1/ORP PCB $55.42 (N=1, 5 boards), $11.08 (N=5), $6.94 (N=10), $4.07 (25), $2.97 (50), $2.24 (100) per board (estimate). Gateway PCB $68.45 / 13.69 / 9.28 / 5.99 / 4.62 / 3.63 (estimate).

## 4. Top 10 cost drivers overall at N=1 ($ per product, draft)

| # | Product | Line | $/product | Source | Share of product |
|---:|---|---|---:|---|---:|
| 1 | Gateway | PCB Gateway (PCBWay 4L 1.6 mm ENIG, 20.3 cm2) | $68.45 | PCBWay est | 55 % |
| 2 | pH node | PCB Feather (PCBWay 4L 1.6 mm ENIG, 11.6 cm2) | $55.42 | PCBWay est | 21 % |
| 3 | pH node | PCB pH sens1 (PCBWay 4L 1.6 mm ENIG, 11.6 cm2) | $55.42 | PCBWay est | 21 % |
| 4 | ORP node | PCB Feather (PCBWay 4L 1.6 mm ENIG, 11.6 cm2) | $55.42 | PCBWay est | 21 % |
| 5 | ORP node | PCB ORP (PCBWay 4L 1.6 mm ENIG, 11.6 cm2) | $55.42 | PCBWay est | 21 % |
| 6 | pH node | Atlas pH OEM circuit (U2) | $45.99 | Atlas | 17 % |
| 7 | ORP node | Atlas ORP OEM circuit (U2) | $45.99 | Atlas | 17 % |
| 8 | Gateway | LBES0ZZ2FR-580 | $23.41 | DK | 19 % |
| 9 | pH node | SMA bulkhead jack IP67 (Amphenol 901-10796) | $19.68 | Mouser | 7 % |
| 10 | ORP node | SMA bulkhead jack IP67 (Amphenol 901-10796) | $19.68 | Mouser | 7 % |

## 5. Top 10 cost drivers overall at N=100 ($ per product, draft)

| # | Product | Line | $/product | Source | Share of product |
|---:|---|---|---:|---|---:|
| 1 | pH node | Atlas pH OEM circuit (U2) | $24.99 | Atlas | 25 % |
| 2 | ORP node | Atlas ORP OEM circuit (U2) | $24.99 | Atlas | 25 % |
| 3 | Gateway | LBES0ZZ2FR-580 | $17.95 | DK | 39 % |
| 4 | pH node | SMA bulkhead jack IP67 (Amphenol 901-10796) | $13.22 | Mouser | 13 % |
| 5 | ORP node | SMA bulkhead jack IP67 (Amphenol 901-10796) | $13.22 | Mouser | 13 % |
| 6 | Gateway | Waveshare 2inch LCD module (SKU 17344) | $10.31 | Waveshare | 22 % |
| 7 | pH node | LiPo 3.7 V ~1000 mAh (TinyCircuits ASR00012, proxy for 602050) | $9.95 | DK | 10 % |
| 8 | ORP node | LiPo 3.7 V ~1000 mAh (TinyCircuits ASR00012, proxy for 602050) | $9.95 | DK | 10 % |
| 9 | pH node | ADUM1250ARZ-RL7 | $5.39 | DK | 5 % |
| 10 | Gateway | PCB Gateway (PCBWay 4L 1.6 mm ENIG, 20.3 cm2) | $3.63 | PCBWay est | 8 % |

## 6. Top 5 drivers per product (draft)

**pH node** at N=1: PCB Feather (PCBWay 4L 1.6 mm ENIG, 11.6 cm2) $55.42; PCB pH sens1 (PCBWay 4L 1.6 mm ENIG, 11.6 cm2) $55.42; Atlas pH OEM circuit (U2) $45.99; SMA bulkhead jack IP67 (Amphenol 901-10796) $19.68; RG316 coax, 0.08 m per pigtail (Huber+Suhner ENVIROFLEX_316, sold per metre) $10.31.

pH node at N=100: Atlas pH OEM circuit (U2) $24.99; SMA bulkhead jack IP67 (Amphenol 901-10796) $13.22; LiPo 3.7 V ~1000 mAh (TinyCircuits ASR00012, proxy for 602050) $9.95; ADUM1250ARZ-RL7 $5.39; AEM10330-QFN $3.29.

**ORP node** at N=1: PCB Feather (PCBWay 4L 1.6 mm ENIG, 11.6 cm2) $55.42; PCB ORP (PCBWay 4L 1.6 mm ENIG, 11.6 cm2) $55.42; Atlas ORP OEM circuit (U2) $45.99; SMA bulkhead jack IP67 (Amphenol 901-10796) $19.68; RG316 coax, 0.08 m per pigtail (Huber+Suhner ENVIROFLEX_316, sold per metre) $10.31.

ORP node at N=100: Atlas ORP OEM circuit (U2) $24.99; SMA bulkhead jack IP67 (Amphenol 901-10796) $13.22; LiPo 3.7 V ~1000 mAh (TinyCircuits ASR00012, proxy for 602050) $9.95; AEM10330-QFN $3.29; Solar cell PowerFilm LL200-2.4-75 $3.29.

**Gateway** at N=1: PCB Gateway (PCBWay 4L 1.6 mm ENIG, 20.3 cm2) $68.45; LBES0ZZ2FR-580 $23.41; Waveshare 2inch LCD module (SKU 17344) $10.59; M2 brass insert x8 (SI IUTB-M2-318, 3.18 mm OD) $3.33; ASPHSPH24K102 $3.20.

Gateway at N=100: LBES0ZZ2FR-580 $17.95; Waveshare 2inch LCD module (SKU 17344) $10.31; PCB Gateway (PCBWay 4L 1.6 mm ENIG, 20.3 cm2) $3.63; ASPHSPH24K102 $2.04; M2 brass insert x8 (SI IUTB-M2-318, 3.18 mm OD) $1.92.

## 7. Notable price breaks

| Part | Used in | Breaks (qty:USD) | Reached at N | Effect per product |
|---|---|---|---|---|
| Atlas pH OEM circuit (U2) | pH node | 1:45.99 10:39.99 25:34.99 50:29.99 75:27.99 100:24.99 (Atlas) | 10 (N>=10), 25 (N>=25), 50 (N>=50), 75 (N>=75), 100 (N>=100) | $45.99 -> $24.99 (N=1 -> 100) |
| Atlas ORP OEM circuit (U2) | ORP node | 1:45.99 10:39.99 25:34.99 50:29.99 75:27.99 100:24.99 (Atlas) | 10 (N>=10), 25 (N>=25), 50 (N>=50), 75 (N>=75), 100 (N>=100) | $45.99 -> $24.99 (N=1 -> 100) |
| SMA bulkhead jack IP67 (Amphenol 901-10796) | both nodes | 1:19.68 10:16.93 25:15.84 50:14.55 100:13.22 (Mouser) | 10 (N>=10), 25 (N>=25), 50 (N>=50), 100 (N>=100) | $19.68 -> $13.22 (N=1 -> 100) |
| ADUM1250ARZ-RL7 | pH node | 1:8.22 10:6.368 25:5.9036 100:5.3935 (DK) | 10 (N>=10), 25 (N>=25), 100 (N>=100) | $8.22 -> $5.39 (N=1 -> 100) |
| ISO1540DR | ORP node | 1:4.68 10:3.553 25:3.2716 100:2.962 (DK) | 10 (N>=10), 25 (N>=25), 100 (N>=100) | $4.79 -> $2.96 (N=1 -> 100) |
| MSASJ31LBB5227MTCA01 | both nodes | 1:5.42 10:3.913 50:3.3138 100:3.1284 (DK) | 10 (N>=10), 50 (N>=50), 100 (N>=100) | $5.42 -> $3.13 (N=1 -> 100) |
| nPM1300-QEAA-R7 | both nodes | 1:2.95 10:2.205 25:2.0184 100:1.8133 (DK) | 10 (N>=10), 25 (N>=25), 100 (N>=100) | $2.95 -> $1.81 (N=1 -> 100) |
| nRF54L15-QFAA-R | both nodes | 1:4.38 10:3.57 25:3.32 100:3.03 (Mouser) | 10 (N>=10), 25 (N>=25), 100 (N>=100) | $4.38 -> $3.03 (N=1 -> 100) |
| FFC jumper 14-way 0.5 mm, 30 mm (Molex 15020-0139) | both nodes | 1:4.23 10:3.59 25:3.3648 50:3.204 100:3.0509 (DK) | 10 (N>=10), 25 (N>=25), 50 (N>=50), 100 (N>=100) | $4.23 -> $3.05 (N=1 -> 100) |
| LBES0ZZ2FR-580 | Gateway (Murata Type 2FR) | 1:23.41 10:20.412 25:19.3736 100:17.9498 (DK) | 10 (N>=10), 25 (N>=25), 100 (N>=100) | $23.41 -> $17.95 (N=1 -> 100) |
| ASPHSPH24K102 | Gateway W1 leads | 1:0.4 10:0.342 25:0.321 50:0.302 100:0.289 250:0.269 500:0.255 1000:0.24 (Mouser) | 10 (N>=2), 25 (N>=4), 50 (N>=7), 100 (N>=13), 250 (N>=32), 500 (N>=63) | $3.20 -> $2.04 (N=1 -> 100) |

- **Atlas OEM circuit is the biggest break**: $45.99 -> $39.99 at 10 -> $34.99 at 25 -> $29.99 at 50 -> $27.99 at 75 -> $24.99 at 100 (N=10, 25, 50, 75 and 100 each save $3-$6 per module).
- **PCBs**: the PCBWay minimum of 5 dominates N=1 (about $55 per board for the Feather and each sensor board, $68 for the gateway); per-board PCB cost is under $3 from N=50 (estimate).
- **W1 leads (ASPHSPH24K102, 8 per cable)**: at DigiKey 8 leads cost $3.20 (8 x $0.40) and 10 leads $3.42 (10 x $0.342), so buying 10 is NOT cheaper at N=1 (the 2 spares cost $0.22). The 10-break pays off from N=2 (16 leads at $0.342 = $5.47 vs $6.40 at $0.40), the 25-break at N=4, 50 at N=7, 100 at N=13, 250 at N=32.
- **Buy-up cases** (cheaper to buy the next break than the exact quantity): see section 5c of each product file. Examples: Tidemark M2.5 inserts (need 8 at N=1, buying 10 is $0.45 cheaper), 0.1 USD passives at N=5 (10 pieces cost less than 5), SML-P12MTT86R LED at N=50 (buy 100).

Gateway buy-up detail (cases saving at least $0.05):

| Line | N | Need | Buy | Exact-qty cost | Buy-up cost | Saving |
|---|---:|---:|---:|---:|---:|---:|
| RB521S30-AU_R1_000A1 | 5 | 5 | 10 | $0.70 | $0.63 | $0.070 |
| RC0402FR-075K1L | 1 | 4 | 10 | $0.40 | $0.11 | $0.29 |
| RC0402FR-07100KL | 5 | 5 | 10 | $0.50 | $0.11 | $0.39 |
| ERJ-2RKF2202X | 5 | 5 | 10 | $0.55 | $0.33 | $0.22 |
| ERJ-2GE0R00X | 1 | 5 | 10 | $0.50 | $0.11 | $0.39 |
| RC0402FR-0710KL | 1 | 3 | 10 | $0.30 | $0.11 | $0.19 |
| RC0402FR-0710KL | 25 | 75 | 100 | $0.82 | $0.70 | $0.12 |
| RC0402FR-07100RL | 1 | 4 | 10 | $0.40 | $0.11 | $0.29 |
| RC0402FR-07470RL | 5 | 5 | 10 | $0.50 | $0.11 | $0.39 |
| RC0402FR-0733RL | 1 | 3 | 10 | $0.30 | $0.11 | $0.19 |
| RC0402FR-0733RL | 25 | 75 | 100 | $0.82 | $0.70 | $0.12 |
| M2 brass insert x8 (SI IUTB-M2-318, 3.18 mm OD) | 1 | 8 | 10 | $3.76 | $3.33 | $0.43 |

## 8. Stock and lifecycle risks (all products)

| Part | Products | Need@100 | Stock | Flag |
|---|---|---:|---|---|
| GRM188R61H225KE11D | pH node, ORP node | 100 | DK 0 / Mouser 230891 | BOM note: original Samsung part NRND (priced part is the Murata equivalent) |
| SML-P12MTT86R | pH node, ORP node | 100 | DK 8 / Mouser 113 | tight: best single stock 113 < 2x need |
| Solar cell PowerFilm LL200-2.4-75 | pH node, ORP node | 100 | DK 48 / Mouser 20 | STOCK-SHORT at N=100 |
| ISO1540DR | ORP node | 100 | DK 0 / Mouser 55 | STOCK-SHORT at N=100 |
| SN6505BDBVR | ORP node | 100 | DK 0 / Mouser 108 | tight: best single stock 108 < 2x need |
| LBES0ZZ2FR-580 | Gateway | 100 | DK 103 / Mouser 0 | tight: best single stock 103 < 2x need |

Single-source lines (one distributor has 0, the other plenty) are in each product file, section 6; they only matter if you want a single order. Highlights:

- **LL200-2.4-75 solar cell**: DK 48 + Mouser 20 = 68 pieces, so N>68 cannot be covered (nodes only).
- **ISO1540DR (ORP U3)**: Mouser 55, DK 0, so N<=55 only; **SN6505BDBVR (ORP U5)**: Mouser 108, DK 0 (tight at N=100).
- **LBES0ZZ2FR-580 (gateway U1, $23.41)**: DK 103, Mouser 0 (266-day lead): covers N=100 with 3 spare; the highest-value single-source part.
- **Feather C40 (CL10A226MP8NUNE, 22 uF 10 V 0603)**: now 0 at DK and Mouser (it was 1215 at Mouser on 2026-10-28); Murata GRM188R61A226ME15D/-J are also 0. Costed with Samsung CL10A226MQ8NRNC (22 uF 6.3 V X5R, Mouser 27,164, $0.25): same footprint but 6.3 V; rail voltage and DC-bias derating NOT checked. Needs a decision before ordering.
- AEM10330-QFN (feather IC1) is Mouser-only (725 in stock); SML-P12MTT86R LED: DK 8, Mouser 113 (tight at N=100); NXE1S0303MC-R13 (pH U4) DK-only 1,633; ADUM1250ARZ-RL7 (pH U3) DK-only 1,203. All cover N=100.
- Not at DK/Mouser: feather J1 USB-C TYPE-C-31-M-12, gateway J1 (same part) and feather R11 FM8625H (LCSC only), sens1/ORP J1 SMA BWSMA-KWE-Z001 (LCSC only), Atlas OEM modules (Atlas only), LCD (Waveshare only). Atlas/Waveshare pages show no stock.
- No obsolete part is priced. Feather C3 original (Samsung) is NRND per the BOM note; the Murata equivalent is priced (Mouser only, DK 0).

## 9. Files

- Shared: `C:\Personal-Agents\shared\design\cost_analysis_2026-10-29\` (cost_ph_node, cost_orp_node, cost_gateway as .md and .csv, cost_summary.md).
- Repo: `docs\cost_analysis_2026-10-29\` (product files) and `docs\cost_analysis_2026-10-29.md` (this summary), branch agent/nrf54l15-feather.
- Data: DigiKey Product Information v4 and Mouser Search API responses of 2026-10-29; Atlas and Waveshare pages 2026-10-29; LCSC prices via jlcsearch.