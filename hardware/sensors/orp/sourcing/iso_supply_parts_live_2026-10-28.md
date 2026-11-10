**SUPERSEDED 2026-10-28 by bom_digikey_mouser_2026-10-28_live.md (full ORP BOM with U3 ISO1540DR and the new C7/C8/C11/D1/R1; this file is for the old ISO1640BDR BOM).**

# feather_orp isolated supply trial: parts with live DigiKey / Mouser data (2026-10-28)

Live check date: 2026-10-28 (DigiKey Product Information API v4 and Mouser Search API; USD, US site, cut tape). Board: Sensor_Boards\feather_orp, BOM from kicad-cli sch export bom (schematic not edited). Replaces the "stock not verified" note in the STATUS.md trial section. All board parts are listed (19 lines); lines marked NEW are the isolated-supply trial parts (SN6505B, 760390015, BAT54C, LP2985-33, ISO1640BDR, FB1 and the new caps C6-C12).

Caveats: the DigiKey API reports 0 for several Murata/Samsung MLCCs; for SN6505BDBVR and ISO1640BDR the kicad DigiKey search tool confirms 0. Mouser "On Order" or missing availability counts as 0. Package match is by MPN and footprint name only (pads not compared). Shipping, tax and fees are not included. J5 is a test pad (no part).

## Cost per board

| Build | DigiKey only | Mouser only | Cheapest split |
|---|---|---|---|
| 1 board | 5.71 USD, 6 lines not orderable | 8.82 USD, 5 lines not orderable | 9.16 USD, 3 lines not orderable |
| 5 boards (total) | 26.70 USD, 6 lines not orderable | 38.80 USD, 5 lines not orderable | 41.38 USD, 3 lines not orderable |

Lines not orderable in the split (1 board): U3, J1, U2. J1 and U2 are not at DK/Mouser (LCSC / Atlas Scientific) and are not in any total. U3 ISO1640BDR is in none of the totals either (0 stock); with the Mouser ISO1540DR alternative at $4.79 add that to the split.

Split plus U3 as ISO1540DR (Mouser): 1 board 13.95 USD; 5 boards 65.33 USD (ISO1540DR is 4.79 each below 10 pieces; Mouser has 55 on hand).

## Status table

| Ref(s) | Qty | Value | Package | Sch MPN | Buy MPN | DK PN | DK stock | DK unit | Mouser PN | Mouser stock | Mouser unit | Split | Note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NEW U5 | 1 | Transformer driver | SOT-23-6 | SN6505BDBVR | SN6505BDBVR | 296-47311-1-ND | 0 | 2.53 | 595-SN6505BDBVR | 108 | 2.59 | Mouser | NEW. DigiKey shows 0 in every packaging (confirmed with both the kicad-pro stock tool and kicad digikey_search_parts; DK lead time 20 weeks). Mouser has 108 in stock, enough for 5 boards. Buy at Mouser. |
| NEW T1 | 1 | Push-pull transformer 1:2 | 6.73x10.2x4.19 SMD | 760390015 | 760390015 | 732-4459-1-ND | 4,238 | 1.98 | 710-760390015 | 29,042 | 2.02 | DK | NEW. Wurth WE-PPTI, active. DK 732-4459-1-ND, Mouser 710-760390015. |
| NEW D1 | 1 | Dual Schottky, common cathode | SOT-23 | BAT54C,215 | BAT54CLT1G | BAT54CLT1GOSCT-ND | 926,290 | 0.14 | 863-BAT54CLT1G | 0 | 0.26 | DK | NEW. Nexperia BAT54C,215 is listed at Mouser (771-BAT54C-T/R) with no stock. onsemi BAT54CLT1G is also common cathode SOT-23 (DK 926k); check the pin order against the SOT-23 footprint before switching (datasheet not read). DK lead time shown for it is 65 weeks, but stock is on hand. |
| NEW U6 | 1 | LDO 3.3V 150mA | SOT-23-5 | LP2985-33DBVR | LP2985-33DBVR | 296-18476-1-ND | 19,897 | 0.65 | 595-LP2985-33DBVR | 0 | 0.64 | DK | NEW. DK 19,897 on hand; Mouser lists it with no stock text. |
| NEW U3 | 1 | I2C isolator | SOIC-8 3.9mm | ISO1640BDR | ISO1640BDR | 296-ISO1640BDRCT-ND | 0 | 3.98 | 595-ISO1640BDR | 0 | 3.98 | none | NEW. BLOCKER: 0 at DigiKey (lead 20 weeks) and 0 at Mouser (140 days; 21,775 due 2026-12-18 and 24,000 due 2026-12-31). Alternatives below. |
| NEW FB1 | 1 | Ferrite bead 220R | 0603 | BLM18PG221SN1D | BLM18PG221SN1D | 490-5221-1-ND | 216,559 | 0.14 | 81-BLM18PG221SN1D | 233,661 | 0.14 | DK | NEW. |
| NEW C6,C9,C12 | 3 | 100nF 16V X7R | 0402 | GRM155R71C104KA88D | GRM155R71C104KA88D | 490-3261-1-ND | 0 | 0.10 | 81-GRM155R71C104KA88 | 7,189,064 | 0.12 | Mouser | NEW. 0 at DK, Mouser 7.19 M. DK alternative with the same size and rating: GCM155R71C104KA55D (DK 7.58 M). |
| NEW C7,C8 | 2 | 10uF 16V / 25V X5R | 0805 | GRM21BR61C106KE15L / GRM21BR61E106KA73L | GRM21BR61E106MA73L | 490-10748-1-ND | 0 | 0.17 | 81-GRM21BR61E106MA3L | 303,452 | 0.25 | Mouser | NEW. Schematic parts C7 (16V, ...KE15L) and C8 (25V, ...KA73L) are both 0 at DK and unstocked at Mouser. One 25V part fits both: Murata 10uF 25V X5R 0805 +-20% (Mouser 303,452). C7 alternative at 16V: GRM21BR61C106KE15K (Mouser 10,890). |
| NEW C10 | 1 | 10nF 50V X7R | 0402 | GRM155R71H103KA88D | GRM155R71H103KA88D | 490-4516-1-ND | 3,618,992 | 0.10 | 81-GRM155R71H103KA8D | 894,087 | 0.10 | DK | NEW. |
| NEW C11 | 1 | 4.7uF 10V X5R | 0603 | GRM188R61A475KE15D | GRM188R61E475KE11D | 490-7203-1-ND | 521,521 | 0.26 | 81-GRM188R61E475KE1D | 3,118 | 0.41 | DK | NEW. Original GRM188R61A475KE15D is Obsolete at DK and Mouser. GRM188R61E475KE11D is 4.7uF 25V X5R 0603 (higher voltage), DK 521,521. |
| C3 | 1 | 2.2uF 10V X7R | 0603 | GRM188R71A225KE15D | GRM188R71A225KE15D | 490-4520-1-ND | 326,995 | 0.16 | 81-GRM188R71A225KE15 | 76,494 | 0.22 | DK |  |
| C1,C5 | 2 | 1uF 16V X5R | 0402 | CL05A105KO5NNNC | CL05A105KO5NNNC | 1276-1067-1-ND | 22,889 | 0.10 | 187-CL05A105KO5NNNC | 20,834 | 0.16 | DK |  |
| C2,C4 | 2 | 100nF 50V X7R | 0603 | CC0603KRX7R9BB104 | CC0603KRX7R9BB104 | 311-1344-1-ND | 3,890,838 | 0.14 | 603-CC603KRX7R9BB104 | 46,544,313 | 0.18 | DK (5: Mouser) |  |
| CN1 | 1 | FFC 14-pin 0.5 mm | Molex 503480-1400 | 503480-1400 | 5034801400 | WM1442CT-ND | 29,488 | 1.40 | 538-503480-1400 | 16,839 | 1.40 | DK |  |
| R3,R4 | 2 | 4.7k 1% | 0402 | CRCW04024K70FKED | CRCW04024K70FKED | 541-4.70KLCT-ND | 2,706,888 | 0.10 | 71-CRCW0402-4.7K-E3 | 701,704 | 0.10 | DK (5: Mouser) |  |
| R5 | 1 | 0R | 0402 | 0402WGF0000TCE | ERJ-2GE0R00X | P0.0JCT-ND | 14,773,138 | 0.10 | 667-ERJ-2GE0R00X | 7,926,905 | 0.10 | DK | Original UNI-ROYAL part is at Mouser only with a 10,000 minimum. Panasonic ERJ-2GE0R00X is the standard 0402 jumper. (R5 may go DNP per the design review.) |
| R1 | 1 | R_ID placeholder 10k | 0402 | (empty) | RC0402FR-0710KL | 311-10.0KLRCT-ND | 8,629,234 | 0.10 | 603-RC0402FR-0710KL | 16,878,588 | 0.10 | DK | Value not decided (SENSORS.md). 10k Yageo used only as a price placeholder. |
| J1 | 1 | SMA right angle | THT | BWSMA-KWE-Z001 | BWSMA-KWE-Z001 | - | - | - | - | - | - | none | Not at DK or Mouser (lookup found nothing). LCSC C496551 (JLC 125,098 in stock on 2026-10-26). Not priced here. |
| U2 | 1 | Atlas ORP OEM | 12x11 module | OEM-ORP | OEM-ORP | - | - | - | - | - | - | none | Not at DK or Mouser; bought from Atlas Scientific directly. Not priced here (price not checked). |

## Problem parts and alternatives

| Ref | Problem | Alternative | Drop-in / what changes | Stock | Price USD | Source |
|---|---|---|---|---|---|---|
| U3 | ISO1640BDR 0 at DK (20 wk) and Mouser (140 days; 21,775 due 2026-12-18) | ISO1540DR (TI) | Same SOIC-8 and the same bidirectional I2C isolator family. I expect the same pinout but did not read the datasheet: check pins and the 3.0 V side-1 supply before use. ISO1540 has weaker drive and slower edges than ISO1640 (ISO1640 was chosen for its 0.4 V VOL2 into the nRF) | 55 Mouser (DK 0) | 4.79 (3.63 at 10) | Mouser |
| U3 (alt 2) |  | ISO1641BDR | Same family, also 0 at DK and Mouser; not available sooner | 0 | 3.98 | - |
| U3 (alt 3) |  | ADUM1250ARZ-RL7 | Original pre-trial isolator (ADuM1250, SOIC-8, 8.22 USD); the schematic symbol was changed to ISO1640, so pin mapping must be re-checked | 4,503 DK | 8.22 | DK |
| U5 | SN6505BDBVR 0 at DK | same MPN at Mouser | Same part | 108 Mouser | 2.59 (1.92 at 10) | Mouser |
| D1 | BAT54C,215 no Mouser stock text | BAT54CLT1G (onsemi) | Common-cathode SOT-23 dual Schottky; verify pin order | 926,290 DK | 0.14 | DK |
| C7,C8 | 16V and 25V 10uF 0805 parts both 0 at DK, unstocked at Mouser | GRM21BR61E106MA73L | 25V +-20% for both | 303,452 Mouser | 0.25 | Mouser |
| C11 | Original obsolete | GRM188R61E475KE11D | 4.7uF 25V X5R 0603 | 521,521 DK | 0.26 | DK |
| R5 | Original MOQ 10,000 at Mouser only | ERJ-2GE0R00X | 0402 0R jumper | 14,773,138 DK | 0.10 | DK |
| J1 | BWSMA-KWE-Z001 not at DK/Mouser | LCSC C496551 | Same part, LCSC only | 125,098 JLC | not priced | LCSC |
| U2 | Atlas OEM-ORP not at DK/Mouser | Atlas Scientific direct | Only source | not checked | not checked | Atlas |

## Schematic field changes for kicad-designer (not applied by me)

- Add LCSC where wanted (secondary): not checked here. MPN changes: C7 and C8 -> GRM21BR61E106MA73L (both), C11 -> GRM188R61E475KE11D, R5 -> ERJ-2GE0R00X (if kept), D1 -> BAT54CLT1G after the pin check, U3 -> ISO1540DR only after a datasheet pin and drive check. R1 MPN stays open until SENSORS.md sets the value.

## Not checked
- Datasheets for BAT54CLT1G pin order, ISO1540 pinout/drive, and any electrical difference of the 25V caps against the stated voltages.
- Atlas OEM-ORP price and SMA connector price; Mouser lead times for on-order parts other than ISO1640BDR/ISO1540DR.
- DigiKey web pages (API values only).
