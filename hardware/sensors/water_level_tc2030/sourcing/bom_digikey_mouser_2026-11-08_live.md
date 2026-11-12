# Feather water level TC2030 variant: DigiKey / Mouser BOM, live data (2026-11-08)

> **Update 2026-11-11:** R1 (SENS_ID R_ID) is now 220k 1% 0402, RC0402FR-07220KL (was 22k RC0402FR-0722KL), part of the x10 board-ID divider change (feather R19 100k, ratio 0.6875 unchanged). Stock checked 2026-11-11: DigiKey 1,037,777 (311-220KLRCT-ND), Mouser 835,482, so R1 no longer needs Mouser. The R1 rows and the Mouser cart CSV below and in the BOM CSV were updated; the 22k remarks in the stock-problem table are history, and kicad_bom_export_2026-11-08_raw.csv is left as the 2026-11-08 snapshot.

Live check date: 2026-11-08 (DigiKey Product Information API v4 and Mouser Search API, called from this PC with the account keys; USD, US site, cut tape). Every stock and price figure below is live from those APIs except where "Not live" says otherwise. Prices are unit prices at the quantity break for the line's total quantity; unit price at qty 1/10/100 is shown per MPN in the table. Shipping, tax and tariffs are not included.

BOM source: `kicad-cli sch export bom` (10.0.4) on feather_water_level_tc2030.kicad_sch; the raw export is kept in kicad_bom_export_2026-11-08_raw.csv. Schematic and PCB were not edited. No DNP parts in the schematic. Left out as board-only: TP1-TP10 (test pads), H1-H4 (mounting holes), J1 (the TC2030 footprint: 6 pads and 7 NPTH holes, in_bom no). 12 lines, 21 parts per board.

## Summary
- Board cost with the cheapest in-stock source per line: **28.92 USD for 1 board, 128.45 USD for 5 boards** (25.69 per board). Every line is orderable. The XM125 is 22.20 of the 1-board figure.
- Mouser only: 29.04 USD (1 board), 129.06 USD (5 boards), every line in stock. DigiKey only is not possible: C1/C3/C4 (CL05A105KO5NNNC), R1 (RC0402FR-0722KL) and U1 (XM125) have 0 stock at DigiKey (DK-only subtotal of the other lines: 6.14 / 25.91).
- DigiKey cart file: 9 lines. Mouser cart file: 3 lines (C1/C3/C4, R1, U1). Cart files are for 1 board; multiply quantities for more. 0402 passives are sold singly on cut tape, so a few spares cost pennies.
- Nothing is end-of-life or obsolete. Stock problems are below.

## BOM status table
Package check is by MPN size code and package name against the KiCad footprint name (0402/0603, SOT-23, SOT-23-5, SOT-23-6, SM8 = SSOP-8 2.95x2.8 P0.65, LGA-28, Molex 14-pos 0.5 mm R/A with mounting pin); pad geometry was not compared. Ratings match the schematic values: caps meet the stated voltage and dielectric, resistors are 1 %, the LDO is the fixed 1.8 V option (listing descriptions compared; datasheets not re-read).

| Ref(s) | Qty | Value | Package / footprint | MPN | DigiKey PN | DK stock | DK 1/10/100 | Mouser PN | Mouser stock | Mouser 1/10/100 | Buy at (1 board) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C1,C3,C4 | 3 | 1uF 16V X5R | 0402 | CL05A105KO5NNNC | 1276-1067-1-ND | 0 | 0.1/0.043/0.025 | 187-CL05A105KO5NNNC | 20,834 | 0.16/0.055/0.033 | Mouser |
| C2 | 1 | 100nF 50V X7R | 0603 | CC0603KRX7R9BB104 | 311-1344-1-ND | 3,588,632 | 0.14/0.08/0.048 | 603-CC603KRX7R9BB104 | 46,414,981 | 0.18/0.073/0.042 | DigiKey |
| C5 | 1 | 10uF 6.3V X5R | 0402 | GRM155R60J106ME15D | 490-13238-1-ND | 2,330,394 | 0.17/0.095/0.058 | 81-GRM155R60J106ME5D | 2,965,139 | 0.17/0.095/0.058 | DigiKey |
| C6-C10 | 5 | 100nF 10V X7R | 0402 | GRM155R71A104KA01D | 490-6321-1-ND | 1,423,001 | 0.1/0.025/0.014 | 81-GRM155R71A104KA1D | 2,048,969 | 0.1/0.025/0.014 | DigiKey |
| CN1 | 1 | FFC 14-pos 0.5 mm R/A, 1 MP | Molex 503480-1400 1x14 + MP | 503480-1400 | WM1442CT-ND | 29,362 | 1.4/1.189/1.011 | 538-503480-1400 | 16,604 | 1.4/1.19/1.02 | DigiKey |
| Q1 | 1 | BSS138LT1G 50V 200mA N-MOS | SOT-23 | BSS138LT1G | BSS138LT1GOSCT-ND | 27 | 0.35/0.213/0.133 | 863-BSS138LT1G | 3,022 | 0.43/0.3/0.19 | DigiKey |
| R1 | 1 | 22k 1% 0402 | 0402 | RC0402FR-0722KL | 311-22.0KLRCT-ND | 0 | 0.1/0.023/0.011 | 603-RC0402FR-0722KL | 2,797 | 0.1/0.0090/0.0070 | Mouser |
| R2-R4 | 3 | 100k 1% 0402 | 0402 | RC0402FR-07100KL | 311-100KLRCT-ND | 4,668,266 | 0.1/0.023/0.011 | 603-RC0402FR-07100KL | 10,452,358 | 0.1/0.011/0.0070 | DigiKey |
| U1 | 1 | Acconeer XM125 A121 radar module | LGA-28 (Acconeer_XM125, DS fig 6.3) | XM125 | 1891-XM125-ND | 0 | 22.2/19.556/17.574 | 925-XM125 | 3,652 | 22.2/19.56/17.58 | Mouser |
| U2 | 1 | NCP161ASN180T1G 1.8V 450mA LDO | SOT-23-5 | NCP161ASN180T1G | NCP161ASN180T1GOSCT-ND | 52,300 | 0.61/0.432/0.337 | 863-NCP161ASN180T1G | 27,231 | 0.61/0.432/0.338 | DigiKey |
| U3 | 1 | TCA9406DCTR I2C translator | SM8 / SSOP-8 2.95x2.8 P0.65 | TCA9406DCTR | 296-28108-1-ND | 18,930 | 1.49/1.089/0.877 | 595-TCA9406DCTR | 20,144 | 1.49/1.09/0.878 | DigiKey |
| U4,U5 | 2 | SN74AXC1T45DBVR 1-bit translator | SOT-23-6 | SN74AXC1T45DBVR | 296-47598-1-ND | 16,664 | 0.59/0.414/0.323 | 595-SN74AXC1T45DBVR | 17,755 | 0.59/0.414/0.324 | DigiKey |

DK PNs are the cut-tape variations. Tape-and-reel variations have large minimums and Digi-Reel has the same price as cut tape.

## Cost per build (cheapest in-stock source per line)
| Ref(s) | Source | Qty (1 board) | Unit | Line | Qty (5 boards) | Unit | Line |
|---|---|---|---|---|---|---|---|
| C1,C3,C4 | Mouser | 3 | 0.16 | 0.48 | 15 | 0.055 | 0.83 |
| C2 | DK | 1 | 0.14 | 0.14 | 5 | 0.14 | 0.70 |
| C5 | DK | 1 | 0.17 | 0.17 | 5 | 0.17 | 0.85 |
| C6-C10 | DK | 5 | 0.1 | 0.50 | 25 | 0.025 | 0.62 |
| CN1 | DK | 1 | 1.4 | 1.40 | 5 | 1.4 | 7.00 |
| Q1 | DK | 1 | 0.35 | 0.35 | 5 | 0.35 | 1.75 |
| R1 | Mouser | 1 | 0.1 | 0.10 | 5 | 0.1 | 0.50 |
| R2-R4 | DK | 3 | 0.1 | 0.30 | 15 | 0.011 | 0.17 |
| U1 | Mouser | 1 | 22.2 | 22.20 | 5 | 20.28 | 101.40 |
| U2 | DK | 1 | 0.61 | 0.61 | 5 | 0.61 | 3.05 |
| U3 | DK | 1 | 1.49 | 1.49 | 5 | 1.49 | 7.45 |
| U4,U5 | DK | 2 | 0.59 | 1.18 | 10 | 0.414 | 4.14 |

Totals: 1 board **28.92 USD**; 5 boards **128.45 USD**. Mouser-only: 29.04 / 129.06.

## Stock problems and substitutes
| Line | Problem | Drop-in substitute (no footprint change) | Source, stock, price |
|---|---|---|---|
| U1 XM125 | DigiKey 0 (tray); only Mouser stocks it (3,652; was 1,263 on 2026-10-30) | none (no pin-compatible module) | Mouser 925-XM125, 22.20 / 19.56 (10) / 17.58 (100) |
| C1, C3, C4 CL05A105KO5NNNC | DigiKey 0 on 2026-11-08 (22,889 on 2026-10-28 for the feather BOM, so DK stock varies); Mouser 20,834 | Murata GRM155R61C105KA12D, same 1 uF 16 V X5R +-10 % 0402 | DigiKey 490-10694-1-ND, 94,165, 0.10 / 0.03 (10) / 0.0171 (100). Mouser lists it with no stock figure |
| R1 RC0402FR-0722KL | DigiKey 0; Mouser 2,797 | Yageo RC0402FR-1322KL, same value, size and tolerance, different reel code. R1 stays 22 k 1 % (SENS_ID ratio 0.6875) | DigiKey 13-RC0402FR-1322KLCT-ND, 25,688, 0.10 / 0.023 (10) / 0.0108 (100); Mouser 603-RC0402FR-1322KL, 226,907 |
| C6-C10 GRM155R71A104KA01D | Mouser shows On Order, none on hand | buy at DigiKey (1,423,001) | no substitute needed |
| Q1 BSS138LT1G | DigiKey cut tape only 27 on hand (covers 5 boards); Mouser 3,022 at 0.43 | none needed | Mouser if building more than about 25 boards' worth |

For a single-shop DigiKey order use GRM155R61C105KA12D and RC0402FR-1322KL, but the XM125 still has to come from Mouser.

## Schematic and notes (reported, not fixed)
- All 12 BOM lines have an MPN and manufacturer in the schematic; no missing or wrong MPN found. C1, C2 and R1 are EasyEDA imports with easyeda2kicad footprints (C0402, C0603, R0402) and Manufacturer strings with Chinese text (cosmetic). C1 shares its MPN with C3/C4, so they are one line here; C1 uses the easyeda2kicad footprint, C3/C4 the KiCad C_0402.
- STATUS.md "Parts added 2026-10-30" table does not list C1 (1 uF) or C2 (100 nF 50 V 0603) and says TP1-TP8 (the board has TP1-TP10). The schematic has 3 x 1 uF.
- xm125_parts_2026-10-30.md suggested TCA9406DCUR (VSSOP-8); the schematic uses TCA9406DCTR (SM8), which is the package that matches the SSOP-8 2.95x2.8 footprint. Do not swap in the DCU. That file's XM125 stock (DK 0 / Mouser 1,263) is out of date: now 0 / 3,652.
- No LCSC numbers on the symbols or here (secondary, not checked). JLCPCB not used.

## Tools / one-off (not in the per-board totals)
| Item | MPN | DigiKey PN | DK stock | DK price | Mouser | Notes |
|---|---|---|---|---|---|---|
| Tag-Connect TC2030-IDC cable, legged, 6-pin plug-of-nails, 8 in, 6-pin 0.1 in IDC socket | TC2030-IDC | TC2030-IDC-ND | 245 | 44.58 (qty 1) | not listed (no match) | This is the one that fits: the board footprint is the legged one (4 leg holes 2.375 mm plus 3 alignment holes). TC2030-IDC-NL is the no-legs cable for the NL footprint (no leg holes); it returned no result in either API and does not suit this board. The cable ends in a 6-pin socket, no breakout. UART wiring in XM125_PROGRAMMING.md |
| SparkFun Qwiic XM125 breakout (bench test) | 24540 (SEN-24540) | 1568-24540-ND | 516 | 49.95 (qty 1) | not listed (searched 24540) | For the PETG radome coupon test and I2C bring-up |

Tools subtotal: 44.58 + 49.95 = 94.53 USD.

## Not live
- Everything above (12 BOM lines, substitutes, TC2030-IDC, 24540) was read from the live DigiKey and Mouser APIs on 2026-11-08; Mouser stock is the Availability field.
- Not included: PCBWay board, stencil, shipping, tax. The 1.8 V USB-UART cable from XM125_PROGRAMMING.md (FTDI TTL-232RG-VREG1V8-WE) was not rechecked; see the prog_adapter BOM.
