# nRF54L15 feather main board: DigiKey / Mouser BOM, live data (2026-10-28)

Live check date: 2026-10-28; revised later the same day (stage 1 C43, stage 2 substitute datasheet checks; see the 'Revision' section at the end). (DigiKey Product Information API v4 and Mouser Search API, called with the account keys on this PC; USD, US site, cut tape). Replaces the no-data version bom_digikey_mouser_2026-10-28.md. Build quantities: 1 board and 5 boards. 51 BOM lines (72 fitted parts); DNP parts are listed at the end and not priced.

BOM source: kicad-cli sch export bom on nrf54l15_feather.kicad_sch (read-only). Differences from the earlier BOM file: C4 is gone; the new LDO-input cap is C54 CL05A106MQ5NUNC (0402), not a 0603 CL10A106KP8NNNC as the old file assumed; C41 MPN still lacks the trailing D. Package check is by MPN size code against the footprint name (0201/0402/0603/0805/1206, QFN pin count, DK package field for U6); pad geometry was not compared.

## Method and caveats
- Stock: DK = quantity available across packagings; Mouser = the Availability field. Mouser "On Order" or no availability text counts as 0 on hand. A line only counts for a distributor if its stock covers the quantity for that build.
- The DigiKey API reports 0 stock for many Samsung/Murata MLCCs and for SN6505BDBVR. The kicad MCP digikey_search_parts gives the same 0 for SN6505BDBVR in every packaging (ManufacturerPublicQuantity also 0), so it is reported as 0 at DigiKey. Mouser has stock for most of these. The DK web page returns 403 to the tools here, so the DK zeros could not be compared with the site. Cross-check done in the revision: every DK stock figure was re-read through the Product API `productdetails` endpoint and per-packaging counts; all zeros were reproduced (in the API a missing top-level QuantityAvailable means 0). In the first run the DK stock of the Taiyo C43 part was missed; that is the only wrong zero found.
- Price is the unit price at the quantity break for that build (1 board = qty per board; 5 boards = 5x). Shipping, tax, tariffs, minimum-order and Digi-Reel fees are not included.
- The kicad-pro stock tool only looks at the first packaging (often the reel), so it can show 0 or fail; the Product API was used directly instead. Mouser limits calls to 30 per minute.

## Cost per build

| Build | DigiKey only | Mouser only | Cheapest split (per line) |
|---|---|---|---|
| 1 board | 27.86 USD, 12 lines not orderable | 38.41 USD, 5 lines not orderable | 36.06 USD, 2 lines not orderable |
| 5 boards (total) | 131.14 USD, 12 lines not orderable | 178.92 USD, 5 lines not orderable | 165.80 USD, 2 lines not orderable |

Per board at 5 boards: split 33.16 USD, DK only 26.23 (partial), Mouser only 35.78 (partial). The totals above are recomputed from the two CSVs and replace the earlier 30.29 / 138.46 split (the CSVs added up to 30.56 / 138.52 before the revision, so the first run's totals were off by 0.27 / 0.06). C43 is now the most expensive line, 5.42 USD of the 36.06.

Totals only include lines the distributor can fill from stock, so single-distributor totals are partial and not comparable with each other. The split is the realistic figure.
- Lines not orderable in the split: J1, R11 (C43 is now orderable). Rough add-on for 1 board: J1 0.19 + R11 0.08 USD (LCSC prices, JLC list of 2026-10-27, bought from LCSC), about 0.27 USD.
- Not orderable at DK only (1 board): C1,C10, C3, C7,C17,C18,C20,C22, C40, C42, C44, C46, C47, IC1, J1, L9,L10 (the Taiyo substitute is Mouser only), R11
- Not orderable at Mouser only (1 board): AE1, C16, C45,C48, J1, R11

## BOM status table

Buy MPN is what the CSVs use; Sch MPN is the schematic field. Stock is on hand at the check date. Unit price is at the 1-board quantity. Split = distributor the cheapest-split total uses (5-board choice in brackets if different).

| Ref(s) | Qty | Value | Package | Sch MPN | Buy MPN | DK PN | DK stock | DK unit | Mouser PN | Mouser stock | Mouser unit | Split | Note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AE1 | 1 | 2.45 GHz chip antenna | 3.2x1.6 SMD | 2450AT18A100E | 2450AT18A0100001E | 712-2450AT18A0100001ECT-ND | 184,515 | 0.52 | 609-2450AT18A0100001 | 0 | 0.52 | DK | Old MPN is marked 'Part Number Change' at Mouser (points to global MPN 2450AT18A0100001E). Same Johanson chip antenna, new number; DK package data not compared with the footprint. |
| C1,C10 | 2 | 2.2uF 10V X5R | 0201 | GRM033R61A225KE47D | GRM033R61A225ME47D | 490-13228-1-ND | 0 | 0.17 | 81-GRM033R61A225ME7D | 6,757 | 0.17 | Mouser | KE47D (+-10%) is 0 at DK and unstocked at Mouser. ME47D is the same part at +-20%. |
| C3 | 1 | 2.2uF 50V X5R | 0603 | CL10A225KB8NNNC | GRM188R61H225KE11D | 490-10733-1-ND | 0 | 0.23 | 81-GRM188R61H225KE1D | 231,827 | 0.40 | Mouser | Samsung part is NRND, 0 at DK, unstocked at Mouser. Murata 2.2uF 50V X5R 0603. DK shows 0 for the Murata too; Mouser has 231,827. |
| C19 | 1 | 1uF 16V X5R | 0402 | CL05A105KO5NNNC | CL05A105KO5NNNC | 1276-1067-1-ND | 22,889 | 0.10 | 187-CL05A105KO5NNNC | 20,834 | 0.16 | DK |  |
| C5 | 1 | 2.0pF | 0201 | GJM0335C1E2R0WB01D | GJM0335C1E2R0WB01D | 490-12592-1-ND | 277,248 | 0.12 | 81-GJM0335C1E2R0WB1D | 87,317 | 0.12 | DK | RF match, keep exact. |
| C6,C14,C15,C26 | 4 | 100nF 50V X7R | 0603 | CC0603KRX7R9BB104 | CC0603KRX7R9BB104 | 311-1344-1-ND | 3,890,838 | 0.14 | 603-CC603KRX7R9BB104 | 46,544,313 | 0.18 | DK (5: Mouser) |  |
| C7,C17,C18,C20,C22 | 5 | 10uF 25V X5R | 0805 | CL21A106KAYNNNE | GRM21BR61E106MA73L | 490-10748-1-ND | 0 | 0.17 | 81-GRM21BR61E106MA3L | 303,452 | 0.25 | Mouser | CL21A106KAYNNNE is 0 at DK and on order only at Mouser. Murata 25V X5R 0805, +-20% (Mouser 303,452; DK 0). C18 may go DNP. |
| C8 | 1 | 1.5pF | 0201 | GJM0335C1E1R5WB01D | GJM0335C1E1R5WB01D | 490-11176-1-ND | 165,338 | 0.11 | 81-GJM0335C1E1R5WB1D | 63,652 | 0.11 | DK | RF match, keep exact. |
| C9 | 1 | 10nF 50V X7R | 0402 | GCM155R71H103KA55D | GCM155R71H103KA55D | 490-4762-1-ND | 1,852,815 | 0.10 | 81-GCM155R71H103KA5D | 43,479 | 0.58 | DK |  |
| C12 | 1 | 1.0pF | 0201 | GJM0335C1E1R0WB01D | GJM0335C1E1R0WB01D | 490-10677-1-ND | 208,856 | 0.11 | 81-GJM0335C1E1R0WB1D | 254,740 | 0.11 | DK | RF match, keep exact. |
| C13 | 1 | 0.3pF | 0201 | GJM0335C1ER30WB01D | GJM0335C1ER30WB01D | 490-8073-1-ND | 4,839 | 0.11 | 81-GJM0335C1ER30WB1D | 228,495 | 0.11 | DK | RF match, keep exact. |
| C16 | 1 | 10uF 25V X5R | 0603 | CC0603MRX5R8BB106 | CC0603MRX5R8BB106 | 311-3494-1-ND | 50,188 | 1.35 | 603-CC0603MRX58BB106 | 0 | 1.94 | DK | Pricey at DK ($1.35); Mouser lists it with no stock. Cheaper if the rail is 5 V or less: GRM188R61C106MA73D (16V, Mouser 1.57 M, $0.26). |
| C40 | 1 | 22uF 10V X5R | 0603 | GRM188R61A226ME15D | CL10A226MP8NUNE | 1276-1274-1-ND | 0 | 0.19 | 187-CL10A226MP8NUNE | 1,215 | 0.31 | Mouser | Murata part is 0 at DK and unstocked at Mouser. Samsung 22uF 10V X5R 0603 (Mouser 1215; DK 0). |
| C41,C54 | 2 | 10uF 6.3V X5R | 0402 | GRM155R60J106ME15 / CL05A106MQ5NUNC | GRM155R60J106ME15D | 490-13238-1-ND | 2,411,767 | 0.17 | 81-GRM155R60J106ME5D | 3,061,511 | 0.17 | DK (5: Mouser) | Schematic C41 MPN lacks the trailing D. Schematic C54 (new LDO-input cap) is CL05A106MQ5NUNC: 0 at DK, on order at Mouser; using C41's Murata part for both. |
| C42 | 1 | 47uF 6.3V X5R | 0603 | GRM188R60J476ME15D | GRM188R60J476ME15D | 490-13247-1-ND | 0 | 0.43 | 81-GRM188R60J476ME5D | 1,740 | 0.72 | Mouser | 0 at DK; Mouser 1740. |
| C43 | 1 | 220uF 6.3V X5R | 1206 | MSASJ31LBB5227MTCA01 | MSASJ31LBB5227MTCA01 | 587-MSASJ31LBB5227MTCA01CT-ND | 1,556 | 5.42 | 963-MSASJ31LBB5227MT | 85 | 8.61 | DK | Schematic part is in stock (the first run missed it). It is AEM10330 CSTO: 100 uF effective minimum on STO is required when the battery can be unplugged (datasheet 6.1, 6.9.1). Bias loss at 4.2 V not verified. Options with a 1210 footprint in c43_substitutes_2026-10-28.md (GRM32ER60J227ME05L, DK 490-16308-1-ND, 102,936, 1.57). |
| C44 | 1 | 4.7uF 25V X5R | 0805 | CL21A475KAQNNNE | CL21A475KAQNNNE | 1276-1244-1-ND | 0 | 0.13 | 187-CL21A475KAQNNNE | 9,804 | 0.16 | Mouser | 0 at DK; Mouser 9804. |
| C45,C48 | 2 | 100nF 16V X7R | 0402 | CL05B104KO5NNNC | GCM155R71C104KA55D | 490-4759-1-ND | 7,580,291 | 0.11 | 81-GCM155R71C104KA5D | 0 | 0.11 | DK | Samsung part is 0 at DK, on order at Mouser. Murata 16V X7R 0402 (DK 7.58 M). Also OK: Yageo CC0402KRX7R7BB104 (both distributors). |
| C46 | 1 | 10uF 10V X5R | 0603 | CL10A106KP8NNNC | GRM188R61C106MA73D | 490-7201-1-ND | 0 | 0.26 | 81-GRM188R61C106MA3D | 1,572,963 | 0.26 | Mouser | Samsung part 0 at DK and unstocked at Mouser. Murata 16V X5R 0603 +-20% (Mouser 1.57 M; DK 0). |
| C47 | 1 | 100pF | 0402 | CL05C101JB5NNNC | CL05C101JB5NNNC | 1276-1025-1-ND | 0 | 0.10 | 187-CL05C101JB5NNNC | 15,351 | 0.12 | Mouser | 0 at DK; Mouser 15,351. |
| C49,C50 | 2 | 100nF | 0201 | CL03A104KQ3NNNC | CL03A104KQ3NNNC | 1276-1013-1-ND | 4,267,100 | 0.10 | 187-CL03A104KQ3NNNC | 17,515 | 0.10 | DK |  |
| C51 | 1 | 1uF 25V X5R | 0402 | CL05A105KA5NQNC | CL05A105KA5NQNC | 1276-1445-1-ND | 2,196,661 | 0.19 | 187-CL05A105KA5NQNC | 44,007 | 0.22 | DK |  |
| CN1 | 1 | FFC 14-pin 0.5 mm | Molex 503480-1400 | 503480-1400 | 5034801400 | WM1442CT-ND | 29,488 | 1.40 | 538-503480-1400 | 16,839 | 1.40 | DK | DK WM1442CT-ND; Mouser 538-503480-1400. |
| D1,D2 | 2 | TPD1E10B06 ESD | DPY0002A | TPD1E10B06DPYR | TPD1E10B06DPYR | 296-30406-1-ND | 120,000 | 0.41 | 595-TPD1E10B06DPYR | 2,632 | 0.41 | DK (5: Mouser) |  |
| D3 | 1 | SMF12A TVS | SOD-123FL | SMF12A | SMF12A | F5747CT-ND | 66,159 | 0.52 | 821-SMF12A | 21,016 | 0.42 | Mouser | Littelfuse at DK (F5747CT-ND). Mouser 821-SMF12A is a different brand listing; check the manufacturer before ordering. |
| F1 | 1 | PTC 0.2A hold | 0603 | MF-FSMF020X-2 | MF-FSMF020X-2 | MF-FSMF020X-2CT-ND | 117,251 | 0.54 | 652-MFFSMF020X-2 | 19,761 | 0.45 | Mouser (5: DK) |  |
| IC1 | 1 | AEM10330 harvester | QFN-40 5x5 | (empty) | AEM10330-QFN | - | - | - | 120-AEM10330-QFN | 725 | 4.22 | Mouser | Resolved: Mouser 120-AEM10330-QFN, 725 in stock, $4.22 (e-peas). DK lists only the evaluation kit (IN1BN-DKA0-AEM100-C1, $63.07, 0 stock), not the IC. The earlier '0 stock' was JLC only. Package not compared with the footprint beyond the QFN-40 name. |
| J1 | 1 | USB-C receptacle 16P | HRO TYPE-C-31-M-12 | (empty) | TYPE-C-31-M-12 | - | - | - | - | - | - | none | BLOCKER: not listed at DK or Mouser. LCSC C165948 (JLC price 0.187 USD, 2026-10-27). A DK/Mouser USB-C part (e.g. GCT USB4105-GF-A, DK 85,282, $0.80) is a different footprint, so it needs a board change. |
| J3 | 1 | Cortex debug 2x5 1.27mm | Samtec FTSH-105 | FTSH-105-01-L-DV-K-TR | FTSH-105-01-L-DV-K | SAM8799-ND | 104,787 | 1.37 | 200-FTSH10501LDVK | 59,922 | 1.18 | Mouser | Schematic MPN has -TR (reel); the non-TR code is right for hand assembly. |
| L2,L5 | 2 | 2.7nH | 0201 | LQP03HQ2N7B02D | LQP03HQ2N7B02D | 490-13909-1-ND | 12,639 | 0.12 | 81-LQP03HQ2N7B02D | 35,689 | 0.12 | DK | RF match, keep exact. |
| L3 | 1 | 3.9nH | 0201 | LQP03HQ3N9B02D | LQP03HQ3N9B02D | 490-13933-1-ND | 16,502 | 0.12 | 81-LQP03HQ3N9B02D | 29,189 | 0.12 | DK | RF match, keep exact. |
| L4 | 1 | Ferrite bead 120R | 0402 | CBG100505U121T | BLM15AG121SN1D | 490-1005-1-ND | 407,700 | 0.10 | 81-BLM15AG121SN1D | 280,471 | 0.10 | DK | PASS. Datasheet read: 120 ohm +-25% at 100 MHz, 550 mA at 85C, DCR 0.19 ohm typ / 0.29 ohm max. Original CBG100505U121T datasheet not obtainable (LCSC blocked), so no side-by-side. |
| L6,L8 | 2 | 3.5nH | 0201 | LQP03HQ3N5B02D | LQP03HQ3N5B02D | 490-13925-1-ND | 374,693 | 0.12 | 81-LQP03HQ3N5B02D | 88,147 | 0.12 | DK | RF match, keep exact. |
| L7 | 1 | 4.7uH | 0603 | LQM18PH4R7MFRL | LQM18PN4R7MFRL | 490-12065-1-ND | 48,432 | 0.25 | 81-LQM18PN4R7MFRL | 182,094 | 0.25 | DK | PASS. PN is the non-automotive twin of the PH (same table: 4.7 uH +-20%, DCR 0.44 typ / 0.55 max, 620 mA rated, SRF 40 MHz). PH datasheet adds 70 mA at -30% inductance; PN datasheet gives no such figure but the electrical table is the same. |
| L9,L10 | 2 | 2.2uH | 0603 | LSCNB1608HKT2R2MD | LSCND1608HKT2R2MF | 587-LSCND1608HKT2R2MFCT-ND | 0 | 0.25 | 963-LSCND1608HKT2R2M | 46,848 | 0.30 | Mouser | Changed from LQM18PN2R2MFRL, which FAILS on Isat (see revision section). Taiyo LSCND is the same family and size (Isat 1.3 A, DCR 250 mohm max). L9 carries no current (BUCK1 off) and may go DNP. |
| L11 | 1 | 10uH | 2520 | DFE252010F-100M=P2 | DFE252010F-100M=P2 | 490-13039-1-ND | 16,454 | 0.25 | 81-DFE252010F-100MP2 | 5,328 | 0.25 | DK |  |
| LED1 | 1 | Red LED | 0402 | SML-P12MTT86R | SML-P12MTT86R | 846-1201-1-ND | 8 | 0.28 | 755-SML-P12MTT86R | 163 | 0.58 | DK | DK has only 8 on hand (enough for 5 boards only); Mouser 163 at $0.58. |
| R8 | 1 | 10k NTC B3380 | 0402 | NCP15XH103F03RC | NCU15XH103F60RC | 490-18149-1-ND | 43,443 | 0.10 | 81-NCU15XH103F60RC | 279,028 | 0.10 | Mouser (5: DK) | PASS. Same R25 10k +-1% and B25/50 3380 K +-1% as the NRND NCP15XH103F03RC. Firmware dts already has thermistor-ohms 10000, thermistor-beta 3380. |
| R9 | 1 | 0R | 0603 | 0603WAF0000T5E | ERJ-3GEY0R00V | P0.0GCT-ND | 4,531,263 | 0.10 | 667-ERJ-3GEY0R00V | 2,236,883 | 0.10 | DK |  |
| R10 | 1 | 150k 1% | 0603 | FRC0603F1503TS | RC0603FR-07150KL | 311-150KHRCT-ND | 176,869 | 0.10 | 603-RC0603FR-07150KL | 362,012 | 0.10 | DK |  |
| R11 | 1 | FM8625H RF switch | DFN-6 1.1x0.7 | FM8625H | FM8625H | - | - | - | - | - | - | none | BLOCKER: not listed at DK or Mouser. LCSC C2857391 (JLC price 0.0753 USD, 30,982 in stock on 2026-10-27). Design fallback: omit R11 and fit R21 0R per the schematic note. |
| R12,R13,R15,R16 | 4 | 4.7k 1% | 0402 | RC0402FR-074K7L | RC0402FR-074K7L | 311-4.7KLRCT-ND | 832,503 | 0.10 | 603-RC0402FR-074K7L | 5,547,669 | 0.10 | DK (5: Mouser) |  |
| R14 | 1 | 560R 1% | 0402 | FRC0402F5600TS | RC0402FR-07560RL | 311-560LRCT-ND | 181,947 | 0.10 | 603-RC0402FR-07560RL | 1,497,952 | 0.10 | DK |  |
| R17,R18,R19 | 3 | 10k 0.1% | 0402 | RT0402BRD0710KL | RT0402BRD0710KL | YAG1346CT-ND | 400,800 | 0.10 | 603-RT0402BRD0710KL | 466,593 | 0.10 | DK (5: Mouser) | RC0402FR-0710KL (1%) is cheaper if 0.1% is not needed. |
| RF1 | 1 | U.FL receptacle | SMD U.FL | ECT818000500 | U.FL-R-SMT-1(10) (placeholder) | H11891CT-ND | 351,552 | 1.67 | 798-U.FL-R-SMT-110 | 150,504 | 1.67 | DK | FAIL as drop-in: Hirose U.FL land pattern (about 4.1x4.0 mm) does not match the RF1 footprint (about 3.5x2.5 mm, body 1.7x1.7x0.8). Part still to be chosen; price is a placeholder. |
| SW1 | 1 | Tact switch 3x2.5 | B3U-1000P | B3U-1000P | B3U-1000P | SW1020CT-ND | 112,002 | 1.17 | 653-B3U-1000P | 53,274 | 1.12 | Mouser |  |
| U2 | 1 | nPM1300 PMIC | QFN-32 5x5 | nPM1300-QEAA-R7 | nPM1300-QEAA-R7 | 4823-NPM1300-QEAA-R7CT-ND | 6,145 | 2.95 | 949-NPM1300-QEAA-R7 | 5,641 | 3.42 | DK | DK 6145 at $2.95, Mouser 5641 at $3.42. Not the WLCSP. |
| U4,U5 | 2 | JST PH 2-pin side | THT | S2B-PH-K-S-GW | S2B-PH-K-S(LF)(SN) | 455-1719-ND | 613,988 | 0.12 | 306-S2BPHKSLFSNPP | 41,114 | 0.12 | DK | DK lists it as S2B-PH-K-S (455-1719-ND); Mouser 306-S2BPHKSLFSNPP. The schematic -GW suffix is an LCSC name. |
| U6 | 1 | nRF54L15 SoC | QFN-48 6x6 | nRF54L15-QFAA-R | nRF54L15-QFAA-R | 4823-NRF54L15-QFAA-RCT-ND | 1,054 | 4.38 | 949-NRF54L15-QFAA-R | 2,177 | 4.38 | DK | DK 1054 (cut tape), Mouser 2177. DK package 48-QFN 6x6 confirmed. The -R7 variant is 0 at DK. |
| U7 | 1 | SN74AUP1G34 buffer | SC-70-5 | SN74AUP1G34DCKR | SN74AUP1G34DCKR | 296-19081-1-ND | 17,205 | 0.44 | 595-SN74AUP1G34DCKR | 6,569 | 0.44 | DK |  |
| X1 | 1 | 32 MHz crystal 8pF | 2016 4-pad | XL7EL89CKI-111YLC-32M | XRCGB32M000F1S2AR0 | 490-XRCGB32M000F1S2AR0CT-ND | 7,007 | 0.33 | 81-XRCGB32M000F1S2AR | 2,699 | 0.33 | DK | PASS on pads and CL (8 pF); ESR 50 ohm max, +-10 ppm, +-20 ppm over temperature. Nordic's ESR/tolerance limit not retrieved, so confirm against the nRF54L15 PS before fab. |

Lifecycle flags seen: R8 NCP15XH103F03RC NRND (DK) / End of Life (Mouser); C3 original CL10A225KB8NNNC NRND; AE1 old MPN replaced; LQP03TQ RF inductors are NRND (not used, the HQ series is active).

## Problem parts and alternatives

| Ref | Problem | Alternative (buy MPN) | Drop-in / what changes | Stock | Price USD | Source |
|---|---|---|---|---|---|---|
| C43 | Murata GRM31CR60J227ME11L/-K unavailable | MSASJ31LBB5227MTCA01 (the schematic Taiyo part) | Same part, no footprint change. Cheaper option with a 1210 footprint: GRM32ER60J227ME05L | 1,556 DK / 85 Mouser | 5.42 DK / 8.61 Mouser (1210: 1.57 DK) | DK |
| J1 | HRO TYPE-C-31-M-12 not at DK/Mouser | LCSC C165948 | Same part, LCSC only (JLC stock 302,673 on 2026-10-27). A DK/Mouser USB-C (e.g. GCT USB4105-GF-A) needs a new footprint | 85,282 DK (USB4105) | 0.80 (USB4105) | LCSC / DK |
| R11 | FM8625H RF switch not at DK/Mouser | LCSC C2857391, or omit R11 and fit R21 0R | Same part, LCSC only (JLC stock 30,982). The 0R option drops the antenna switch | 30,982 JLC | 0.0753 | LCSC |
| X1 | YXC XL7EL89CKI-111YLC-32M not at DK/Mouser | XRCGB32M000F1S2AR0 (Murata) | 32 MHz, 8 pF, +-10 ppm, 2.0x1.6 mm; pads fit inside the current footprint, ESR 50 ohm max (checked in the revision). Second choice NDK CS11336-32M (8 pF, +-10 ppm, DK 51,126, $0.52). Do not use NDK CS11213/CS10925 (6 pF) | 7,007 DK / 2,699 Mouser | 0.33 | DK, Mouser |
| AE1 | 2450AT18A100E: Mouser says part number changed | 2450AT18A0100001E | Johanson global MPN for the same antenna (schematic field should change) | 184,515 DK | 0.52 | DK |
| IC1 | AEM10330: JLC had 0 stock; no DK listing | AEM10330-QFN at Mouser (120-AEM10330-QFN) | Same part; DK lists only the eval kit | 725 Mouser | 4.22 (3.29 at 10) | Mouser |
| L7 | LQM18PH4R7MFRL 0 at DK and Mouser | LQM18PN4R7MFRL | Same size, inductance and electrical table (PH is the AEC-Q200 grade); PASS | 48,432 DK / 182,094 Mouser | 0.25 | DK, Mouser |
| L9,L10 | LSCNB1608HKT2R2MD 0 at DK, unstocked at Mouser | LSCND1608HKT2R2MF (not LQM18PN2R2MFRL, which fails on Isat) | Same Taiyo family and 1608 size; Isat 1.3 A vs 1.5 A | 46,848 Mouser (DK 0) | 0.30 | Mouser |
| L4 | CBG100505U121T not at DK/Mouser | BLM15AG121SN1D | 0402 120R bead; PASS (550 mA, DCR 0.29 max) | 407,700 DK | 0.10 | DK |
| RF1 | ECT818000500 not at DK/Mouser | none yet (U.FL-R-SMT-1(10) fails) | Land pattern differs; needs the ECT datasheet to pick MHF4 or MHF I and a pad check | - | - | - |
| C7,C17,C18,C20,C22 | CL21A106KAYNNNE 0 DK, on order Mouser | GRM21BR61E106MA73L | 10uF 25V X5R 0805, +-20% | 303,452 Mouser | 0.25 | Mouser |
| C1,C10 | GRM033R61A225KE47D 0 DK, unstocked Mouser | GRM033R61A225ME47D | Same part, +-20% | 6,757 Mouser | 0.17 | Mouser |
| C3 | CL10A225KB8NNNC NRND | GRM188R61H225KE11D | 2.2uF 50V X5R 0603 | 231,827 Mouser | 0.40 | Mouser |
| C40 | GRM188R61A226ME15D 0 DK, unstocked Mouser | CL10A226MP8NUNE | 22uF 10V X5R 0603 | 1,215 Mouser | 0.31 | Mouser |
| C45,C48 | CL05B104KO5NNNC 0 DK, on order Mouser | GCM155R71C104KA55D (or CC0402KRX7R7BB104) | 100nF 16V X7R 0402 | 7,580,291 DK | 0.11 | DK |
| C46 | CL10A106KP8NNNC 0 DK, unstocked Mouser | GRM188R61C106MA73D | 10uF 16V X5R 0603 (higher voltage rating) | 1,572,963 Mouser | 0.26 | Mouser |
| C54 | CL05A106MQ5NUNC 0 DK, on order Mouser | GRM155R60J106ME15D | Same 10uF 6.3V X5R 0402 as C41 | 2,411,767 DK | 0.17 | DK |
| C16 | CC0603MRX5R8BB106 $1.35 at DK | GRM188R61C106MA73D if the rail is 5 V or less | Cheaper 10uF 0603 | 1,572,963 Mouser | 0.26 | Mouser |
| C42, C44, C47 | 0 at DK | same MPN from Mouser | In stock at Mouser | 1,740 / 9,804 / 15,351 | 0.72 / 0.16 / 0.12 | Mouser |
| R8 | NRND / EOL | NCU15XH103F60RC | Successor, same B constant and tolerance; PASS | 43,443 DK / 279,028 Mouser | 0.10 | DK, Mouser |
| LED1 | DK has only 8 | same MPN at Mouser | Same part | 163 Mouser | 0.58 | Mouser |

## DNP parts (not priced)

C11 GJM0335C1E2R2WB01D; C52, C53 (pi pads, no part); R1, R2 RCA025K1FLF 5.1k 0402; R20 0402WGF1004TCE 1M; R21 0402WGF0000TCE 0R; X2 X1A0000610008 32.768 kHz.

## Schematic field changes for kicad-designer (not applied by me)

- AE1 MPN -> 2450AT18A0100001E. C1,C10 -> GRM033R61A225ME47D. C3 -> GRM188R61H225KE11D. C7,C17,C18,C20,C22 -> GRM21BR61E106MA73L. C40 -> CL10A226MP8NUNE. C41 MPN: add trailing D. C45,C48 -> GCM155R71C104KA55D. C46 -> GRM188R61C106MA73D. C54 -> GRM155R60J106ME15D. C43 stays MSASJ31LBB5227MTCA01 (in stock at DK; add DigiKey PN 587-MSASJ31LBB5227MTCA01CT-ND). J3 -> drop -TR. IC1 MPN -> AEM10330-QFN, Manufacturer e-peas. J1 MPN -> TYPE-C-31-M-12. L4 -> BLM15AG121SN1D. L7 -> LQM18PN4R7MFRL. L9,L10 -> LSCND1608HKT2R2MF. RF1: leave as is until a pad-compatible part is chosen (U.FL-R-SMT-1(10) does not fit). R8 -> NCU15XH103F60RC. U4,U5 -> S2B-PH-K-S(LF)(SN). X1 -> XRCGB32M000F1S2AR0 (pads and ESR checked). R9, R10, R14 -> ERJ-3GEY0R00V, RC0603FR-07150KL, RC0402FR-07560RL.

## Revision 2026-10-28 (later): substitute checks and C43

Sources: Murata specs (pim.murata.com) for LQM18PN, LQM18PH, BLM15AG, XRCGB and NCU15; DigiKey parametric data for the Taiyo LSCN parts; KiCad stock footprints for pad comparison; the board file (read only) for X1 and RF1 pads; the firmware dts for the NTC. Not reachable from here: docs.nordicsemi.com (403 / 404 after three attempts), LCSC datasheets, Murata SimSurfing, DigiKey web pages (403).

| Ref | Substitute | Verdict | Basis |
|---|---|---|---|
| C43 | MSASJ31LBB5227MTCA01 (original) | PASS on stock and footprint; capacitance margin unverified | It is AEM10330 CSTO on VBAT. The datasheet needs 100 uF effective minimum when the battery can be unplugged; the 4.2 V bias loss of a 6.3 V X5R 220 uF is not known (no vendor curve reachable). Details in c43_substitutes_2026-10-28.md |
| L4 | BLM15AG121SN1D | PASS | 120 ohm +-25%, 550 mA, DCR 0.19 / 0.29 ohm max, 1.0x0.5 mm, against a few mA on DECA. Original not compared (datasheet not obtainable) |
| L7 | LQM18PN4R7MFRL | PASS | Identical table to the schematic PH part (4.7 uH, DCR 0.44 / 0.55 ohm, 620 mA, SRF 40 MHz). PN is non-automotive, PH is AEC-Q200 |
| L9, L10 | LQM18PN2R2MFRL | FAIL | Murata: 2.2 uH, DCR 0.30 typ / 0.375 max, 750 mA rated (40 K temperature rise), SRF 70 MHz, no Isat given; the PH sister part lists 150 mA at -30% inductance. Original LSCNB1608HKT2R2MD: Isat 1.5 A, 1.2 A rated, DCR 292 mohm max. The nPM1300 reference BOM asks for 2.2 uH with DCR below 400 mohm, so DCR passes, but BUCK2 can deliver up to 200 mA (L10 feeds VDDIO and the sensor load switch) and this inductor would sag well before that |
| L9, L10 | LSCND1608HKT2R2MF (Taiyo) | PASS (recommended) | 2.2 uH, Isat 1.3 A, rated 1.4 A, DCR 250 mohm max, 1.6x0.8x0.8 mm. Mouser 46,848 at 0.30; DK 0 |
| X1 | XRCGB32M000F1S2AR0 | PASS (Nordic limit open) | CL 8.0 pF, +-10 ppm, +-20 ppm over -40..105C, aging +-2 ppm/yr, ESR 50 ohm max, drive 300 uW max. Murata land pattern is four 0.75x0.70 mm pads with 0.60 / 0.30 mm gaps (centres +-0.675, +-0.50 mm); the current X1 pads are 0.9x0.8 at +-0.70, +-0.55 mm and contain them. Pins 2 and 4 are no-connect on the part (GND on the board is fine). The nRF54L15 HFXO ESR and tolerance limits could not be fetched; compare 50 ohm and the roughly 32 ppm worst case (10+20+2) with the PS before fab |
| RF1 | U.FL-R-SMT-1(10) | FAIL | KiCad Hirose U.FL footprint: signal pad 1.05x1.0 at x -1.525, two ground pads 2.2x1.05 at y +-1.475, about 4.1x4.0 mm overall. RF1 footprint: pads 1 and 3 at x +-1.0 (1.5x0.6), pads 2 and 4 at y +0.95 / -0.95 (about 0.5-0.65x0.55), body 1.7x1.7x0.8 mm. Not interchangeable, and the cable type (U.FL vs MHF4 class) of the ECT818000500 is unknown without its datasheet. Candidates to check against it: I-PEX 20449-001E-03 (MHF4, DK 78,260, 0.74), I-PEX 20279-001E-03 (MHF I, DK 151,959, 1.06) |
| R8 | NCU15XH103F60RC | PASS | 10k +-1% at 25C, B25/50 3380 K +-1%, B25/85 3434 K, same as NCP15XH103F03RC. Firmware: soil_moisture_fw boards/others/nrf54l15_feather dts has thermistor-ohms 10000 and thermistor-beta 3380. No firmware change needed |

### DigiKey zero check
The DK zero lines (C1,C10 GRM033R61A225ME47D; C3 GRM188R61H225KE11D; C7.. GRM21BR61E106MA73L; C40 CL10A226MP8NUNE; C42 GRM188R60J476ME15D; C44 CL21A475KAQNNNE; C46 GRM188R61C106MA73D; C47 CL05C101JB5NNNC; C43 GRM31CR60J227ME11L) and the non-BOM-line zeros (Samsung CL05B104KO5NNNC, CL05A106MQ5NUNC, CL10A225KB8NNNC, SN6505BDBVR) were re-read with the Product API (keyword search and `productdetails`) and, for one part, with the kicad MCP digikey_search_parts. All still report 0 in every packaging, with 17 to 61 week manufacturer lead times, so they look like real out-of-stock states rather than a data fault. Only C43 changed, because the Taiyo MPN had not been looked up. The DigiKey site itself could not be opened to confirm.
Small drifts in the other DK counts (for example C6 4,099,456 vs 3,890,838, C41 2,511,767 vs 2,411,767) do not change any decision.

### Still not checked
- Pad geometry of the other substituted parts (passives are same-size catalogue parts; only X1, RF1 and C43 were compared).
- Nordic limits for the HFXO crystal and the DCC and BUCK inductor peak currents (docs.nordicsemi.com not reachable from here).
- DC-bias curves for C43 and the other bulk caps.
- Shipping, tax, tariff and fees. Lead times of on-order Mouser parts (the Mouser listing of the Taiyo C43 part shows a 77 day lead time for out-of-stock quantities).
