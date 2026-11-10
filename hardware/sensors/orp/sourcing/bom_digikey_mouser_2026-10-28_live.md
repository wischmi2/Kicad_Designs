# feather_orp: DigiKey / Mouser BOM, live data (2026-10-28)

Live check date: 2026-10-28 (DigiKey Product Information API v4 and Mouser Search API, called directly with the account keys on this PC; USD, US site, cut tape). Board: Sensor_Boardseather_orp (rev 0.1, ISO1540DR / SN6505B supply). Build quantities: 1 board and 5 boards. **Replaces** iso_supply_parts_live_2026-10-28.md, which was priced for the old BOM (ISO1640BDR, C7 16 V, C8 GRM21BR61E106KA73L, C11 10 V, R1 pH value).

BOM source: `kicad-cli sch export bom` on feather_orp.kicad_sch (read only, grouped by value, footprint and MPN). 19 lines, 24 fitted parts. Skipped: R5 (ERJ-2GE0R00X, DNP) and J5 (test pad, no part). There is no older BOM file in the folder to compare; the only differences are against the old iso_supply_parts file named above.

## Method and caveats
- Stock: DigiKey = quantity available across packagings for the MPN; Mouser = the Availability field (no availability text counts as 0). A line only counts for a distributor if its stock covers the quantity for that build. Price is the unit price at the quantity break for that build (cut tape). Shipping, tax, tariffs, minimum order and Digi-Reel fees are not included.
- The kicad-pro stock tool only checks the first packaging, so the Product API was used directly. DigiKey zeros on Murata/Samsung MLCCs and TI parts (here C6/C9/C12, C7/C8, U3, U5) are real out-of-stock states (17-20 week lead times), as found on the feather BOM run.
- Package check is by DigiKey package field and MPN size code against the footprint name (0402/0603/0805, SOT-23-3/-5/-6, SOIC-8 3.9 mm); pad geometry was not compared. Voltage ratings read from DigiKey parameters: C1/C5 16 V, C2/C4 50 V, C3 10 V, C6/C9/C12 16 V, C7/C8 25 V, C10 50 V, C11 25 V; all are above the 3.3 V / about 5 V rails here.

## Cost per build (excluding U2 Atlas OEM-ORP and J1 SMA)

| Build | DigiKey only | Mouser only | Cheapest split (per line) |
|---|---|---|---|
| 1 board | not possible: C6/C9/C12, C7/C8, U3, U5 are 0 at DigiKey (partial 5.61 USD) | not possible: D1, U6 are 0 at Mouser (partial 13.51 USD) | **13.85 USD** (DigiKey 5.61 on 12 lines, Mouser 8.24 on 4 lines) |
| 5 boards (total) | not possible (partial 26.20 USD) | not possible (partial 62.25 USD) | **64.83 USD** (DigiKey 25.05 on 10 lines, Mouser 39.75 on 6 lines), 12.97 USD per board |

Two orders are needed: Mouser for C6/C9/C12, C7/C8, U3, U5 (and whatever else is cheaper there); DigiKey for D1 and U6. Single-order alternatives: none at one distributor. Cost including the parts bought elsewhere:

| Build | Split total above | U2 Atlas OEM-ORP | J1 SMA at LCSC | All-in |
|---|---|---|---|---|
| 1 board | 13.85 | 45.99 | 0.51 | **60.35 USD** |
| 5 boards | 64.83 | 229.95 (5 x 45.99; 39.99 each only from 10) | 2.57 | **297.35 USD** |

## Lines only at one source
- **J1 BWSMA-KWE-Z001 (SMA right angle): LCSC only.** C496551, 0.5141 USD each, 122,999 in stock (jlcsearch via kicad-pro, 2026-10-28). Not at DigiKey or Mouser (exact-MPN and keyword searches empty). A DK/Mouser SMA edge jack would need the footprint checked first.
- **U2 Atlas OEM-ORP: Atlas Scientific only.** 45.99 USD (1), 39.99 (10), 34.99 (25); the page shows in stock. Price read from the product page text on 2026-10-28; the pH OEM page returned the identical table, so double check at checkout.

## Stock notes
- U3 ISO1540DR: DigiKey 0 (20 week lead), Mouser 55. Mouser covers 5 boards but leaves 50. If it goes, ISO1640BDR was also 0 at DK/Mouser on the earlier check; no other drop-in was searched.
- U5 SN6505BDBVR: DigiKey 0, Mouser 108.
- D1 BAT54CLT1G and U6 LP2985-33DBVR: DigiKey in stock (926,290 / 19,897); Mouser shows 0 (long lead). Buy at DigiKey.
- C6/C9/C12 GRM155R71C104KA88D and C7/C8 GRM21BR61E106MA73L: DigiKey 0; Mouser 7.19 M / 303,452. Fall-back for C6/C9/C12: Yageo CC0402KRX7R7BB104 100 nF 16 V X7R 0402 (listed in stock at both on the feather run).
- R3/R4 could be the same Yageo 4.7k as R1 (RC0402FR-074K7L) to merge into one line; no price difference.

## BOM status table (unit price at 1 board)

Stock is on hand at the check date. Split = distributor the cheapest-split total uses for 1 board / 5 boards.

| Ref(s) | Qty | Value | Package | Sch MPN | Buy MPN | DK PN | DK stock | DK unit | Mouser PN | Mouser stock | Mouser unit | Split (1 / 5 boards) | Note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C1,C5 | 2 | 1uF 16V X5R | 0402 | CL05A105KO5NNNC | CL05A105KO5NNNC | 1276-1067-1-ND | 22,489 | 0.10 | 187-CL05A105KO5NNNC | 20,834 | 0.16 | DK / DK | DK package 0402, 16 V, X5R, +-10%. |
| C2,C4 | 2 | 100nF 50V X7R | 0603 | CC0603KRX7R9BB104 | CC0603KRX7R9BB104 | 311-1344-1-ND | 4,099,456 | 0.14 | 603-CC603KRX7R9BB104 | 46,544,313 | 0.18 | DK / Mouser | 0603, 50 V, X7R. |
| C3 | 1 | 2.2uF 10V X7R | 0603 | GRM188R71A225KE15D | GRM188R71A225KE15D | 490-4520-1-ND | 326,995 | 0.16 | 81-GRM188R71A225KE15 | 76,494 | 0.22 | DK / DK | 0603, 10 V, X7R, +-10%. |
| C6,C9,C12 | 3 | 100nF 16V X7R | 0402 | GRM155R71C104KA88D | GRM155R71C104KA88D | 490-3261-1-ND | 0 | 0.10 | 81-GRM155R71C104KA88 | 7,189,064 | 0.12 | Mouser / Mouser | DigiKey shows 0 in every packaging (17 week lead); Mouser has 7.2 M. Buy at Mouser. Yageo CC0402KRX7R7BB104 is the fall-back (both distributors). |
| C7,C8 | 2 | 10uF 25V X5R | 0805 | GRM21BR61E106MA73L | GRM21BR61E106MA73L | 490-10748-1-ND | 0 | 0.17 | 81-GRM21BR61E106MA3L | 303,452 | 0.25 | Mouser / Mouser | DigiKey 0 (17 week lead), Mouser 303,452. 0805, 25 V, X5R, +-20%. |
| C10 | 1 | 10nF 50V X7R | 0402 | GRM155R71H103KA88D | GRM155R71H103KA88D | 490-4516-1-ND | 3,618,992 | 0.10 | 81-GRM155R71H103KA8D | 894,087 | 0.10 | DK / DK | 0402, 50 V, X7R. |
| C11 | 1 | 4.7uF 25V X5R | 0603 | GRM188R61E475KE11D | GRM188R61E475KE11D | 490-7203-1-ND | 521,369 | 0.26 | 81-GRM188R61E475KE1D | 3,118 | 0.41 | DK / DK | 0603, 25 V, X5R, +-10%. Mouser only 3,118 on hand at 0.41; DK 521 k at 0.26. |
| CN1 | 1 | FFC 14-pin 0.5 mm | Molex 503480-1400 | 503480-1400 | 503480-1400 | WM1442CT-ND | 29,488 | 1.40 | 538-503480-1400 | 16,839 | 1.40 | DK / DK | DK lists it under 5034801400 (WM1442CT-ND). 14 positions, 0.50 mm. |
| D1 | 1 | BAT54C dual Schottky | SOT-23 | BAT54CLT1G | BAT54CLT1G | BAT54CLT1GOSCT-ND | 926,290 | 0.14 | 863-BAT54CLT1G | 0 | 0.26 | DK / DK | Common cathode pair, SOT-23-3 (pin check was done in the board STATUS). Mouser shows 0 stock (364 day lead): buy at DigiKey. |
| FB1 | 1 | 220R@100MHz bead | 0603 | BLM18PG221SN1D | BLM18PG221SN1D | 490-5221-1-ND | 216,539 | 0.14 | 81-BLM18PG221SN1D | 233,661 | 0.14 | DK / DK | 0603, 220 ohm at 100 MHz. |
| J1 | 1 | SMA right angle (ORP probe) | BAT Wireless BWSMA-KWE-Z001 THT | BWSMA-KWE-Z001 | BWSMA-KWE-Z001 | - | - | - | - | - | - | LCSC only | Not at DigiKey or Mouser (searched exact MPN, brand and 'BWSMA'). LCSC C496551, 0.514 USD, 122,999 in stock (jlcsearch, 2026-10-28). Not in the totals below. |
| R1 | 1 | 4.7k 1% | 0402 | RC0402FR-074K7L | RC0402FR-074K7L | 311-4.7KLRCT-ND | 842,613 | 0.10 | 603-RC0402FR-074K7L | 5,547,669 | 0.10 | DK / DK | SENS_ID resistor (ORP ID 4.7k). |
| R3,R4 | 2 | 4.7k 1% | 0402 | CRCW04024K70FKED | CRCW04024K70FKED | 541-4.70KLCT-ND | 2,706,888 | 0.10 | 71-CRCW0402-4.7K-E3 | 701,704 | 0.10 | DK / Mouser | I2C pull-ups. Could be the same Yageo part as R1 (one line): RC0402FR-074K7L. |
| T1 | 1 | 760390015 push-pull transformer | Wurth WE-PPTI 6.73x10.2 mm | 760390015 | 760390015 | 732-4459-1-ND | 4,238 | 1.98 | 710-760390015 | 29,042 | 2.02 | DK / DK | DK 3125 Vrms listing; Wurth datasheet rated 2500 Vac. Footprint was drawn from the Wurth land pattern, not compared again here. |
| U2 | 1 | Atlas OEM-ORP circuit | 12x11 module | OEM-ORP | OEM-ORP | - | - | - | - | - | - | Atlas Scientific | Bought from Atlas Scientific: 45.99 USD each (1), 39.99 at 10 (atlas-scientific.com ORP OEM page, read 2026-10-28, listed in stock). The 5-board price is 5 x 45.99 = 229.95 USD. Not in the DK/Mouser totals. |
| U3 | 1 | ISO1540DR I2C isolator | SOIC-8 | ISO1540DR | ISO1540DR | 296-34871-1-ND | 0 | 4.68 | 595-ISO1540DR | 55 | 4.79 | Mouser / Mouser | DigiKey 0 (20 week lead), Mouser 55 in stock. SOIC-8 3.9 mm, 2 channels, 2500 Vrms. Mouser stock covers 5 boards (5) but only 55 left. |
| U5 | 1 | SN6505BDBVR transformer driver | SOT-23-6 | SN6505BDBVR | SN6505BDBVR | 296-47311-1-ND | 0 | 2.53 | 595-SN6505BDBVR | 108 | 2.59 | Mouser / Mouser | DigiKey 0 (20 week lead), Mouser 108. SOT-23-6, 2.25-5.5 V. |
| U6 | 1 | LP2985-33DBVR 3.3 V LDO | SOT-23-5 | LP2985-33DBVR | LP2985-33DBVR | 296-18476-1-ND | 19,897 | 0.65 | 595-LP2985-33DBVR | 0 | 0.64 | DK / DK | DK SOT-23-5, 16 V in max, 150 mA. Mouser shows 0 (140 day lead): buy at DigiKey. |

## Schematic field changes for kicad-designer (not applied by me)
- J1: LCSC field C496551 (currently empty). U2: no MPN issue (OEM-ORP). All other lines already carry an MPN that exists and matches the footprint package. Optional: add DigiKey PN for CN1 (WM1442CT-ND, MPN is listed as 5034801400 there) and note that R1/R3/R4 are two brands of the same 4.7k 0402.

## Not checked
- Pad geometry of any part against the footprint (package family only); T1 land pattern was drawn from the Wurth datasheet earlier and not rechecked.
- Shipping, tax, tariffs, fees; lead times for backordered parts; Mouser stock moves quickly for U3 (55) and U5 (108).
- Whether the Atlas price on its page matches checkout.

Files: bom_digikey_2026-10-28_live.csv and bom_mouser_2026-10-28_live.csv (MPN-keyed, same layout as the feather ones).
