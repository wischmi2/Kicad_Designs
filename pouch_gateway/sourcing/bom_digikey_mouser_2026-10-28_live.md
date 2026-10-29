# Pouch gateway Rev A: DigiKey / Mouser BOM, live data (2026-10-28)

Live check date: 2026-10-28 (DigiKey Product Information API v4 and Mouser Search API, called directly with the account keys on this PC; USD, US site, cut tape or bulk). Build quantities: 1 board and 5 boards. 26 priced BOM lines plus J1 (LCSC) and the LCD; DNP parts are listed at the end and not priced. Nothing was ordered or added to a cart.

BOM source: `kicad-cli sch export bom` on pouch_gateway.kicad_sch (read only), saved as `kicad_bom_export_2026-10-28.csv`. The schematic carries only LCSC numbers (MPNs only on U1, J2, J4, J5, L1), so the buy MPNs below are chosen here from the LCSC part descriptions (jlcsearch lookups, 2026-10-28) and the value/footprint. Schematic field changes are for kicad-designer, listed at the end; I did not edit anything.

## U1 first: Murata LBES0ZZ2FR-580 (Type 2FR, RW612)

**Available in single pieces.** Not a blocker.

| Source | Part number | Stock (2026-10-28) | MOQ | Price (1 / 10 / 25 / 100) | Note |
|---|---|---|---|---|---|
| DigiKey cut tape | 490-LBES0ZZ2FR-580CT-ND | 103 | 1 | 23.41 / 20.41 / 19.37 / 17.95 | Digi-Reel 490-LBES0ZZ2FR-580DKR-ND has the same stock and price. Tape and reel 490-LBES0ZZ2FR-580TR-ND is 0 stock, MOQ 1000, 15.78 |
| Mouser | 81-LBES0ZZ2FR-580 | 0 (no availability text) | 1 | 21.52 / 18.76 / 17.80 / 16.48 | Lead time shown 266 days; do not count on it |
| DigiKey evaluation kit | 490-LBES0ZZ2FR-EVK-ND | 42 | 1 | 81.38 | Mouser 81-LBES0ZZ2FR-EVK has 25 at 81.38. Not needed for the BOM |
Only 103 pieces are on DigiKey and 5 boards use 5, so quantity is fine today. The single DigiKey stock line is the supply risk: if it sells through, the only listed source is Mouser's 266-day backorder. Other single-piece distributors (Murata's own store, Arrow, Newark, Avnet) were not checked; Octopart returned 403 and I did not try further. Buy U1 first, or buy a spare.

## Cost per build

| Build | DigiKey only (orderable lines) | Mouser only (orderable lines) | Cheapest split (per line) | Practical: DigiKey + C6 from Mouser | Not in those totals |
|---|---|---|---|---|---|
| 1 board | 36.32 USD, 2 lines not orderable (C6, J1) | 14.21 USD, 5 lines not orderable (U1, L1, 100 nF caps, R4, J1) | 36.71 USD | 36.95 USD | J1 0.19 USD (LCSC) + LCD 10.99 USD (Waveshare, includes the 8-pin cable) |
| 5 boards (total) | 170.91 USD, 2 lines not orderable | 57.98 USD, 5 lines not orderable | 173.14 USD | 174.06 USD | J1 0.93 USD + LCD 54.95 USD |

**All-in (cheapest split + J1 + LCD): 1 board about 47.89 USD; 5 boards about 229.02 USD (45.80 per board).** U1 is 23.41 USD per board (117.05 for 5), the LCD 10.99, the antenna 2.59 and the U.FL 1.67; everything else is under 9 USD in total. Mouser-only is not possible because U1 is DigiKey only. Single-distributor totals are partial, so use the split. The split sends about six penny lines to Mouser to save a few cents; the practical column puts everything except C6 on DigiKey (one Mouser line, 0.63 USD, 3.15 for 5) and costs about 0.25 to 0.9 USD more. Shipping, tax, tariffs, minimum-order and Digi-Reel fees are not included, nor is LCSC shipping for J1.

Pricing rule: unit price at the break for the order quantity; where buying up to the next break (at most 3x the need) is cheaper in total, the table orders that quantity (for example 10 resistors for a need of 4). Order quantities are in the CSVs.

## BOM status table

Package check is by MPN/datasheet package against the KiCad footprint name (size code, pin count). Pad geometry was compared only for D1 (Wurth datasheet land pattern, not overlaid on the KiCad footprint) and not for the passives. Stock is on hand at the check date. Cost columns are the line total at the cheaper distributor (split). DigiKey/Mouser basic/extended does not apply (that is a JLCPCB assembly concept).

| Ref(s) | Qty | Value | Package | Buy MPN | DK PN | DK stock | Mouser PN | Mouser stock | Cost 1 board | Cost 5 boards | Split | Note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| U1 | 1 | Murata Type 2FR module (RW612) | Murata_LBES0ZZ2FR LGA | LBES0ZZ2FR-580 | 490-LBES0ZZ2FR-580CT-ND | 103 | 81-LBES0ZZ2FR-580 | 0 | 23.41 | 117.05 | DK | Sch MPN LBES0ZZ2FR-580. DK cut tape only; Mouser has no stock (266-day lead). |
| U2 | 1 | 3.3 V 2 A buck | SOT-23-5 | TLV62569DBVR | 296-47360-1-ND | 240901 | 595-TLV62569DBVR | 30942 | 0.28 | 1.40 | DK |  |
| D1 | 1 | USB ESD array | SOT-143 | 8240026 | 732-4470-1-ND | 3343 | 710-8240026 | 14930 | 1.09 | 5.45 | DK | Nexperia PRTR5V0U2X is 0 at DigiKey and Mouser (Mouser 365-day lead). Substitute Wurth 8240026 (checked in datasheet: SOT143-4L, pin 1 GND, 2 I/O1, 3 I/O2, 4 VDD, 5 V working, 1.2 pF, 6 V max VDD, 6 A 8/20us). Same pinout as D1 usage (1 GND, 2 D+, 3 D-, 4 VBUS). Land pattern on the datasheet is the standard SOT-143 (pitch 1.92 / 0.96 bsc); not overlaid on the KiCad footprint. |
| D2 | 1 | Schottky 30 V 200 mA | SOD-523 | RB521S30-AU_R1_000A1 | 3757-RB521S30-AU_R1_000A1CT-ND | 51375 | 241-RB521S30AUR1000A | 2882 | 0.14 | 0.63 | DK (5: MO) | onsemi RB521S30T1G is 0 at DK and Mouser. Panjit RB521S30-AU: SOD-523, 30 V, 200 mA, Vf 500 mV at 200 mA (DK parametric data), same as the schematic part. Second choice onsemi NSVRB521S30T1G (DK 1516, Mouser 16311, 0.37). |
| D3 | 1 | LED red | 0603 | LTST-C191KRKT | 160-1447-1-ND | 1366477 | 859-LTST-C191KRKT | 1372845 | 0.15 | 0.75 | DK |  |
| D4 | 1 | LED green | 0805 | LTST-C170KGKT | 160-1414-1-ND | 440975 | 859-LTST-C170KGKT | 654990 | 0.19 | 0.95 | DK |  |
| D5 | 1 | LED blue | 0603 | LTST-C190TBKT | 160-1646-1-ND | 391693 | 859-LTST-C190TBKT | 26544 | 0.26 | 1.30 | DK | Schematic part. Blue Vf is about 3.1-3.3 V at 20 mA from a 3.3 V rail with 100 R: expect a very dim LED (design note, not a sourcing issue). |
| FB1 | 1 | Ferrite 220R 2.2 A | 0603 | BLM18KG221SN1D | 490-5255-1-ND | 420145 | 81-BLM18KG221SN1D | 359817 | 0.14 | 0.70 | DK |  |
| J1 | 1 | USB-C receptacle 16P | HRO TYPE-C-31-M-12 | TYPE-C-31-M-12 | - | - | - | - | - | - | - | BLOCKER-LINE: not listed at DigiKey or Mouser. LCSC C165948 only (jlcsearch 2026-10-28: 303,407 in stock, 0.1858 USD). DK/Mouser USB-C (e.g. GCT USB4105-GF-A, DK 85,277 / Mouser 397,458, 0.80 USD) needs a footprint change. |
| J3 | 1 | U.FL receptacle | Hirose U.FL-R-SMT-1 | U.FL-R-SMT-1(10) | H11891CT-ND | 351552 | 798-U.FL-R-SMT-110 | 150504 | 1.67 | 8.35 | DK | J7 is DNP. KiCad footprint is the Hirose one, so (10) is a drop-in. |
| J5 | 1 | JST PH 8-pin side entry THT | S8B-PH-K | S8B-PH-K-S(LF)(SN) | 455-1725-ND | 19309 | 306-S8BPHKSLFSN | 11040 | 0.33 | 1.65 | DK | DigiKey lists it as S8B-PH-K-S 455-1725-ND (bulk). |
| L1 | 1 | 2.2 uH power inductor | Sunlord SWPA4020S 4x4x2 | SWPA4020S2R2NT | 3442-SWPA4020S2R2NTCT-ND | 1395 | - | - | 0.34 | 1.70 | DK | Schematic MT (+-20%) is 0 at DK and Mouser. NT is the same series and size, +-30%; DK data: 2.2 uH, Isat 3.7 A, rated 1.85 A, DCR 52 mohm max, 4.0 x 4.0 x 2.0 mm. Mouser has no NT. |
| SW1,SW2,SW3 | 3 | Tact switch KMR2 | KMR2 | KMR221GLFS | 108-KMR221GLFSCT-ND | 107334 | 611-KMR221G-LFS | 37248 | 2.01 | 8.64 | DK |  |
| C1,C4,C5,C7,C15,C20 | 6 | 10 uF X5R MLCC | 0603 | CL10A106MA8NRNC | 1276-1869-1-ND | 170829 | 187-CL10A106MA8NRNC | 2562 | 1.87 | 5.61 | DK | Schematic LCSC parts are CL10A106MA8NRNC (C1, 25 V) and CL10A106KP8NNNC (others, 10 V). One 25 V part covers all six (higher voltage rating, better bias derating). |
| C2,C8,C9,C10,C11,C12,C13,C14,C16,C19,C21 | 11 | 100 nF X7R 16 V | 0402 | GCM155R71C104KA55D | 490-4759-1-ND | 7580115 | 81-GCM155R71C104KA5D | 0 | 0.37 | 1.26 | DK | Schematic LCSC part is CL05B104KO5NNNC (0 at DK, on order at Mouser). |
| C6 | 1 | 22 uF X5R | 0805 | CL21A226MOQNNNE | 1276-2909-1-ND | 0 | 187-CL21A226MOQNNNE | 134784 | 0.63 | 3.15 | MO | Schematic LCSC part CL21A226MAQNNNE (25 V) is 0 at both. 16 V Samsung sister part is in stock at Mouser (134,784); 10 V and 25 V alternatives all 0. Better bias derating than a 6.3 V part on 3.3 V. |
| R1,R2,R10,R11 | 4 | 5.1k 1% | 0402 | RC0402FR-075K1L | 311-5.10KLRCT-ND | 595903 | 603-RC0402FR-075K1L | 1878372 | 0.11 | 0.22 | MO |  |
| R3 | 1 | 100k 1% | 0402 | RC0402FR-07100KL | 311-100KLRCT-ND | 5497576 | 603-RC0402FR-07100KL | 5233330 | 0.10 | 0.11 | DK (5: MO) |  |
| R4 | 1 | 22k 1% (Panasonic) | 0402 | ERJ-2RKF2202X | P22.0KLCT-ND | 726745 | 667-ERJ-2RKF2202X | 0 | 0.11 | 0.33 | DK | Yageo RC0402FR-0722KL (schematic LCSC C25768 class) is 0 at DK, 68,652 at Mouser. Panasonic ERJ-2RKF2202X is 22k 1% 0402 and in stock at DK (726,745), 0 at Mouser. Mouser alternative: RC0402FR-0722KL 603-RC0402FR-0722KL. |
| R5,R6,R12,R13,R23 | 5 | 0 ohm jumper (Panasonic) | 0402 | ERJ-2GE0R00X | P0.0JCT-ND | 14762508 | 667-ERJ-2GE0R00X | 7926905 | 0.11 | 0.27 | MO | R5 stays fitted (Brian 2026-10-28); R24 is DNP. Yageo RC0402JR-070RL is 0 at DK (Mouser 10.1 M); Panasonic ERJ-2GE0R00X is in stock at both. |
| R7,R8,R18 | 3 | 10k 1% | 0402 | RC0402FR-0710KL | 311-10.0KLRCT-ND | 8629234 | 603-RC0402FR-0710KL | 16878588 | 0.30 | 0.16 | DK (5: MO) |  |
| R9,R15,R16,R17 | 4 | 100R 1% | 0402 | RC0402FR-07100RL | 311-100LRCT-ND | 3401057 | 603-RC0402FR-07100RL | 6886391 | 0.11 | 0.22 | MO |  |
| R14 | 1 | 470R 1% | 0402 | RC0402FR-07470RL | 311-470LRCT-ND | 590427 | 603-RC0402FR-07470RL | 682207 | 0.10 | 0.11 | DK (5: MO) |  |
| R20,R21,R22 | 3 | 33R 1% | 0402 | RC0402FR-0733RL | 311-33.0LRCT-ND | 1371592 | 603-RC0402FR-0733RL | 1068177 | 0.30 | 0.16 | DK (5: MO) |  |
| ANT | 1 | 2.4/5 GHz FPC antenna, 100 mm U.FL lead | Off-board (on J3) | 146153-0100 | WM12218-ND | 44175 | 538-146153-0100 | 25611 | 2.59 | 12.95 | DK | 146153-0100 is the 100 mm lead version named in the Ledger notes (3.0 dBi at 2.4 GHz); the 50 mm version 146153-0050 is the default in concepts.md. Same price. Murata FCC antenna list (HSW2FR) not checked. |
| LCSC only | | | | | | | | | | | | |
| J1 | 1 | USB-C 16P | HRO TYPE-C-31-M-12 | TYPE-C-31-M-12 | - | - | - | - | 0.19 | 0.93 | LCSC | LCSC-ONLY LINE. LCSC C165948, jlcsearch 2026-10-28: 303,407 in stock, 0.1858 USD (single price; LCSC shipping not included). Not listed at DigiKey or Mouser. No footprint-matching alternative found at DK/Mouser. A DK/Mouser USB-C part (GCT USB4105-GF-A: DK 2073-USB4105-GF-ACT-ND 85,277 and Mouser 640-USB4105-GF-A 397,458, 0.80 USD) is a different footprint and needs a board change. |
| LCD | 1 | Waveshare 2inch LCD Module (SKU 17344) | module | 2inch LCD Module | - | - | - | - | 10.99 | 54.95 | Waveshare | waveshare.com/2inch-lcd-module.htm, 2026-10-28: 10.99 USD shown, with a 1-9 piece tier of 10.59; stock not stated on the page. Package includes the module and a PH2.0 20 cm 8-pin cable, so no separate cable line is needed (J5 is S8B-PH-K, mates with a PH housing). Amazon price not checked. Shipping not included. |

TP1 is a copper pad and J6 (TC2030) is footprint pads only; neither has a part.

## Problem parts and alternatives

| Ref | Problem | Alternative (buy MPN) | Drop-in / what changes | Stock | Price USD | Source |
|---|---|---|---|---|---|---|
| D1 | PRTR5V0U2X: Nexperia is 0 at DigiKey (all packagings) and Mouser (365-day lead). A GOODWORK-brand PRTR5V0U2X is 88,000 at DK but MOQ 3000 tape and reel (about 143 USD) | Wurth 8240026 | Same SOT-143 package and pinout per the Wurth datasheet (pin 1 GND, 2 I/O1, 3 I/O2, 4 VDD; 5 V working, 1.2 pF, 6 V max VDD); D1 uses pin 1 GND, 2 D+, 3 D-, 4 VBUS. Check the land pattern against the KiCad SOT-143 footprint before fab (datasheet pitch 1.92 / 0.96 bsc, pad 1.03 x 1.4). Clamp 9 V at 5 A | 3,343 DK / 14,930 Mouser | 1.09 | DK or Mouser |
| D2 | onsemi RB521S30T1G 0 at DK, 0 at Mouser (364-day lead) | Panjit RB521S30-AU_R1_000A1 | SOD-523, 30 V, 200 mA, Vf 500 mV at 200 mA (DK data), same electrical class. Second choice onsemi NSVRB521S30T1G (DK 1,516, Mouser 16,311) at 0.37 | 51,375 DK / 2,882 Mouser | 0.14 | DK |
| L1 | SWPA4020S2R2MT (+-20%) 0 at DK and Mouser | SWPA4020S2R2NT (+-30%) | Same Sunlord series and 4x4x2 mm size; 2.2 uH, Isat 3.7 A, rated 1.85 A, DCR 52 mohm max (DK data). Wider tolerance; TLV62569 is specified with a 2.2 uH inductor. Other makers are not footprint-compatible (not checked) | 1,395 DK only | 0.34 | DK |
| C6 | CL21A226MAQNNNE 22 uF 25 V 0805 is 0 at both | CL21A226MOQNNNE (16 V) | Same 0805 X5R, 16 V rating. 10 V and 25 V parts checked (CL21A226MPQNNNE, GRM21BR61A226ME44L, GRM21BR61E226ME44L, C2012X5R1C226M125AC, TMK212BBJ226MG-T) are all 0 at both. DK-only option: CL21A226MQQNNNE (6.3 V, DK 560 at 0.17; loses more capacitance on 3.3 V) | 134,784 Mouser | 0.63 | Mouser |
| C1,C4,C5,C7,C15,C20 | Schematic parts are CL10A106MA8NRNC (C1, 25 V) and CL10A106KP8NNNC (the others, 10 V); the 10 V one is 0 at DK and Mouser | CL10A106MA8NRNC for all six | 10 uF X5R 0603; the 25 V rating covers the 10 V positions with less bias loss. Murata GRM188R61C106MA73D (16 V) is Mouser only (1.57 M) and 0 at DK | 170,829 DK / 2,562 Mouser | 0.187 at 10 | DK |
| 100 nF caps | CL05B104KO5NNNC 16 V X7R 0402: 0 at DK, on order at Mouser | GCM155R71C104KA55D (Murata, 16 V X7R) | Same 0402 value, voltage and dielectric. Also Yageo CC0402KRX7R7BB104 (DK 867k, Mouser 46 M) | 7.58 M DK | 0.034 at 10 | DK |
| R4 | Yageo 22k 0402 0 at DK | ERJ-2RKF2202X (Panasonic 22k 1%) | Same 0402 value and tolerance | 726,745 DK | 0.11 | DK |
| R5,R6,R12,R13,R23 | Yageo RC0402JR-070RL 0 at DK | ERJ-2GE0R00X (Panasonic 0R) | 0402 jumper, in stock at both | 14.8 M DK / 7.9 M Mouser | 0.10 | DK or Mouser |
| J1 | not at DK/Mouser | LCSC C165948 | Same part, LCSC only | 303,407 (jlcsearch) | 0.19 | LCSC |
| U1 | Mouser 0 stock, only 103 at DK | none | No other module in the same footprint; the Type 2FR is the design | 103 DK | 23.41 | DK |

## Design notes found while sourcing (for the main agent)

- D5 blue LED (LTST-C190TBKT, Vf about 3.1-3.3 V at 20 mA) with a 100 R series resistor from a 3.3 V rail will be very dim or off (DESIGN_NOTES: anodes to 3V3, 100 R). A lower-Vf blue or a smaller resistor is a design choice for kicad-designer.
- Mouser stock is the Availability field. DigiKey zeros on Samsung/Murata MLCCs have been reproducible out-of-stock states in earlier checks (see the feather BOM).

## Optional tools and hardware (not in the totals)

- Debug cable for J6 (Tag-Connect footprint, schematic value TC2030-CTX): DigiKey TC2030-CTX-ND 748 in stock at 56.05; TC2030-IDC-ND 405 in stock at 44.58 (one-off tool). Which cable matches the footprint and the RW612 SWD pins was not verified.
- Four M2 standoffs and screws for H1-H4: not in the schematic BOM and not priced; length depends on the open LCD-stack decision in STATUS.md.
- A spare JST PH 8-pin cable is not listed.

## DNP parts (not priced)

C3 6.8 pF, C17, C18, C22, C23 (no value), J2 SWD header (FTSH-105-01-L-DV-K-TR), J4 UART header (PZ254V-11-03P), J7 U.FL (second BLE antenna), R24 0R. All marked DNP in the exported BOM. TP1 and J6 have no part.

## Differences from the old BOM files

- pouch_gateway.csv (2026-10-20, a designator list with no MPNs) still lists J2 and J4 as fitted, uses the old reference names RESET/ISP/USER (now SW1/SW2/SW3) and shows no DNP flags. The new export marks C3, C17, C18, C22, C23, J2, J4, J7 and R24 DNP. Values and quantities otherwise match.
- pouch_gateway_BOM_PCBWay.xlsx and Sample_BOM_PCBWay.xlsx are PCBWay turnkey BOMs; not parsed (no spreadsheet reader available here). They are obsolete for the self-assembly route and should not be uploaded.

## Schematic field changes for kicad-designer (not applied by me)

- U1: keep LBES0ZZ2FR-580 and add DigiKey PN 490-LBES0ZZ2FR-580CT-ND. D1 -> 8240026 (Wurth) once the footprint is confirmed. D2 -> RB521S30-AU_R1_000A1. L1 -> SWPA4020S2R2NT. C6 -> CL21A226MOQNNNE. C1,C4,C5,C7,C15,C20 -> CL10A106MA8NRNC. 100 nF caps -> GCM155R71C104KA55D. R4 -> ERJ-2RKF2202X. 0R resistors -> ERJ-2GE0R00X. Add MPNs for J1 (TYPE-C-31-M-12), J3 (U.FL-R-SMT-1(10)), SW1-SW3 (KMR221GLFS), D3-D5, FB1, U2 and the remaining resistors from the CSVs. Add the antenna Molex 146153-0100 as an off-board BOM line if the schematic should carry it.

## Still not checked

- Other distributors for U1 (see above). Amazon price for the LCD. LCSC stock/price of J1 beyond the jlcsearch figure (LCSC pages show no stock).
- Pad geometry of every substituted part against the KiCad footprints, except the D1 land pattern read from the Wurth datasheet. The Panjit diode and SWPA4020S2R2NT were checked from DigiKey parametric data only (no datasheet PDF).
- Whether the Murata FCC filing (HSW2FR) covers the 146153-0100 variant (concepts.md lists the 50 mm version).
- Mouser lead times, shipping, tax, tariffs and fees.
