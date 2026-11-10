# nrf54l15_feather_sens1 (pH): DigiKey / Mouser BOM, live data (2026-10-28)

Live check date: 2026-10-28 (DigiKey Product Information API v4 and Mouser Search API, called directly with the account keys on this PC; USD, US site, cut tape). Board: nrf54l15_feather_sens1 (pH sensor, Brian kept the old isolated supply: U3 ADuM1250 and U4 NXE1S0303MC). Build quantities: 1 board and 5 boards.

BOM source: `kicad-cli sch export bom` on nrf54l15_feather_sens1.kicad_sch (read only). 11 lines, 14 fitted parts. J5 is a test pad (no part). There is no older BOM file in the folder. **Five fields in the schematic are empty:** J1, R5, U2, U3, U4 have no MPN; the buy MPNs below are my proposals and need to be written into the schematic by kicad-designer.

## Method and caveats
- Stock: DigiKey = quantity available across packagings for the MPN; Mouser = the Availability field (no availability text counts as 0). A line only counts for a distributor if its stock covers the quantity. Price is the unit price at the quantity break for the build (cut tape). Shipping, tax, tariffs, minimum order and Digi-Reel fees are not included.
- The kicad-pro stock tool only checks the first packaging, so the Product API was used directly.
- Package check is by DigiKey package field and MPN size code against the footprint name (0402/0603, SOIC-8 3.9 mm, Molex 503480-1400); pad geometry was not compared. DigiKey ratings: C1/C5 16 V, C2/C4 50 V, C3 10 V, all above the 3.3 V rails.

## Cost per build (excluding U2 Atlas pH OEM and J1 SMA)

| Build | DigiKey only | Mouser only | Cheapest split (per line) |
|---|---|---|---|
| 1 board | **13.96 USD** (all 9 priced lines in stock) | not possible: U3, U4 have no Mouser stock | 13.96 USD (all DigiKey) |
| 5 boards (total) | **67.33 USD** (13.47 per board) | not possible | 67.14 USD (two cheap passive lines at Mouser save 0.19 USD, not worth a second order) |

No stock blockers: every DigiKey line is in stock for 5 boards. Recommendation: one DigiKey order.

| Build | DK total | U2 Atlas pH OEM | J1 SMA at LCSC | All-in |
|---|---|---|---|---|
| 1 board | 13.96 | 45.99 | 0.51 | **60.46 USD** |
| 5 boards | 67.33 | 229.95 (5 x 45.99; 39.99 each only from 10) | 2.57 | **299.85 USD** |

## Lines only at one source
- **J1 BWSMA-KWE-Z001 (SMA right angle): LCSC only.** C496551, 0.5141 USD each, 122,999 in stock (jlcsearch via kicad-pro, 2026-10-28). Not at DigiKey or Mouser. The schematic symbol has no MPN; the footprint name identifies it.
- **U2 Atlas pH OEM: Atlas Scientific only.** 45.99 USD (1), 39.99 (10), 34.99 (25); page shows in stock. Price read from the product page text on 2026-10-28; the ORP OEM page returned the identical table, so double check at checkout.

## Parts with MPN proposals (no stock problem, but the schematic needs a number)
| Ref | Proposal | Why | DigiKey | Price |
|---|---|---|---|---|
| U3 ADuM1250 | ADUM1250ARZ-RL7 (505-ADUM1250ARZ-RL7CT-ND) | ADUM1250ARZ in tubes is 0 at DK; the -RL7 reel part is the same die and package (SOIC-8 3.9 mm, 2 channels, 3-5.5 V, 2500 Vrms per DK). Cut tape works for hand soldering | 4,503 | 8.22 (1), 6.37 (10) |
| U4 NXE1S0303MC | NXE1S0303MC-R13 (811-3902-1-ND), or -R7 (811-3098-1-ND) | Same Murata module, only the reel differs (R13 13 in., R7 7 in.). 14-SMD module, 3.3 V in (2.97-3.63 V) and out, 1 W, 3 kV isolation | 1,633 (R13) / 2,937 (R7) | 3.30 (R13) / 3.49 (R7) |
| R5 0R | ERJ-2GE0R00X (P0.0JCT-ND) | Same part the ORP board uses; 0402 jumper. Not marked DNP here, so it is fitted | 14.8 M | 0.10 |
| J1 | BWSMA-KWE-Z001 | See above | - | - |

Datasheet checks for alternatives: not needed, because nothing is out of stock. ADuM1250ARZ-RL7 and NXE1S0303MC-R13 are the same parts as the originally intended ones (packaging variants), not substitutes, so no pinout or rating comparison was done beyond the DigiKey parametric fields above. U3 and U4 are the two expensive lines (8.22 + 3.30 of 13.96); ISO1540DR at Mouser (55 on hand, 4.79) is a cheaper isolator but has not been compared with the ADuM1250 pinout or rated for this design, so it is only a pointer.

## BOM status table (unit price at 1 board)

Stock is on hand at the check date. Split = distributor the cheapest-split total uses for 1 board / 5 boards.

| Ref(s) | Qty | Value | Package | Sch MPN | Buy MPN | DK PN | DK stock | DK unit | Mouser PN | Mouser stock | Mouser unit | Split (1 / 5 boards) | Note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C1,C5 | 2 | 1uF 16V X5R | 0402 | CL05A105KO5NNNC | CL05A105KO5NNNC | 1276-1067-1-ND | 22,489 | 0.10 | 187-CL05A105KO5NNNC | 20,834 | 0.16 | DK / DK | DK package 0402, 16 V, X5R, +-10%. |
| C2,C4 | 2 | 100nF 50V X7R | 0603 | CC0603KRX7R9BB104 | CC0603KRX7R9BB104 | 311-1344-1-ND | 4,099,456 | 0.14 | 603-CC603KRX7R9BB104 | 46,544,313 | 0.18 | DK / Mouser | 0603, 50 V, X7R. |
| C3 | 1 | 2.2uF 10V X7R | 0603 | GRM188R71A225KE15D | GRM188R71A225KE15D | 490-4520-1-ND | 326,995 | 0.16 | 81-GRM188R71A225KE15 | 76,494 | 0.22 | DK / DK | 0603, 10 V, X7R, +-10%. |
| CN1 | 1 | FFC 14-pin 0.5 mm | Molex 503480-1400 | 503480-1400 | 503480-1400 | WM1442CT-ND | 29,488 | 1.40 | 538-503480-1400 | 16,839 | 1.40 | DK / DK | DK lists it under 5034801400 (WM1442CT-ND). 14 positions, 0.50 mm. |
| J1 | 1 | SMA right angle (pH probe) | BAT Wireless BWSMA-KWE-Z001 THT | (empty) | BWSMA-KWE-Z001 | - | - | - | - | - | - | LCSC only | Schematic MPN is empty; the footprint is SMA_BAT_Wireless_BWSMA-KWE-Z001, so this is the part (same as the ORP board). Not at DigiKey or Mouser. LCSC C496551, 0.514 USD, 122,999 in stock (jlcsearch, 2026-10-28). Not in the totals below. |
| R1 | 1 | 10k 1% (SENS_ID, pH) | 0402 | RC0402FR-0710KL | RC0402FR-0710KL | 311-10.0KLRCT-ND | 8,629,234 | 0.10 | 603-RC0402FR-0710KL | 16,878,588 | 0.10 | DK / DK | SENS_ID resistor. |
| R3,R4 | 2 | 4.7k 1% | 0402 | CRCW04024K70FKED | CRCW04024K70FKED | 541-4.70KLCT-ND | 2,706,888 | 0.10 | 71-CRCW0402-4.7K-E3 | 701,704 | 0.10 | DK / Mouser | I2C pull-ups. |
| R5 | 1 | 0R (AGND_ISO to GND_ISO link) | 0402 | (empty) | ERJ-2GE0R00X | P0.0JCT-ND | 14,773,138 | 0.10 | 667-ERJ-2GE0R00X | 7,926,905 | 0.10 | DK / DK | Schematic MPN is empty and the part is NOT marked DNP on this board, so it is priced (the ORP board uses the same ERJ-2GE0R00X). Field needs filling. |
| U2 | 1 | Atlas pH OEM circuit | Atlas pH OEM module | (empty) | OEM pH circuit | - | - | - | - | - | - | Atlas Scientific | Bought from Atlas Scientific: 45.99 USD each (1), 39.99 at 10 (atlas-scientific.com pH OEM page, read 2026-10-28, listed in stock). 5 boards = 229.95 USD. Not in the DK/Mouser totals. |
| U3 | 1 | ADuM1250 I2C isolator | SOIC-8 | (empty) | ADUM1250ARZ-RL7 | 505-ADUM1250ARZ-RL7CT-ND | 4,503 | 8.22 | 584-ADUM1250ARZ-R7 | 0 |  | DK / DK | Schematic MPN is empty. ADUM1250ARZ (tube) is 0 at DigiKey; the reel version ADUM1250ARZ-RL7 is the same die and package, 4,503 on hand as cut tape (SOIC-8 3.9 mm, 2 channels, 2500 Vrms, 3-5.5 V). Mouser lists it without stock or price. |
| U4 | 1 | NXE1S0303MC isolated DC-DC | Murata NXE 14-SMD, 5 leads | (empty) | NXE1S0303MC-R13 | 811-3902-1-ND | 1,633 | 3.30 | 580-NXE1S0303MC-R13 | 0 | 3.25 | DK / DK | Schematic MPN is empty. The DK numbers are NXE1S0303MC-R7 (7 in. reel, 2,937) and -R13 (13 in. reel, 1,633); same part, only the reel differs. R13 is 0.19 cheaper as cut tape (3.30 vs 3.49). Mouser shows 0 stock for both. 3.3 V in/out, 1 W, 3 kV. |

## Schematic field changes for kicad-designer (not applied by me)
- U3 MPN -> ADUM1250ARZ-RL7. U4 MPN -> NXE1S0303MC-R13 (or -R7). R5 MPN -> ERJ-2GE0R00X. J1 MPN -> BWSMA-KWE-Z001, LCSC C496551. U2: Atlas pH OEM (set an MPN such as the Atlas part name, check on the Atlas page). R1, R3, R4, C1-C5 already have MPNs that exist and match.

## Not checked
- Pad geometry against footprints; the U4 footprint (Converter_DCDC_Murata_NXExSxxxxMC_SMD) was not compared with the Murata drawing.
- Shipping, tax, tariffs, fees. Whether the Atlas price on its page matches checkout.

Files: bom_digikey_2026-10-28_live.csv and bom_mouser_2026-10-28_live.csv (MPN-keyed, same layout as the feather ones; Mouser rows for U3/U4 show no stock).
