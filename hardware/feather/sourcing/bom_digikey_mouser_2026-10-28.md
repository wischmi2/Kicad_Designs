# nRF54L15 feather main board: DigiKey / Mouser BOM (2026-10-28)

Source: commit 6f8987f frozen copy, `kicad-cli sch export bom` (ungrouped, DNP column), 2026-10-28. Then C4 removed and one new LDO-input cap added as decided. Fitted parts per board: 72 (72 in the schematic, minus C4, plus the new cap). 52 BOM lines. DNP parts are listed at the end.

## STATUS: DigiKey and Mouser live data NOT obtained

- DigiKey: API credentials are not configured on this PC (digikey_test_connection fails); the product and search pages returned HTTP 403 to WebFetch (3 tries: search, product detail, filter URL).
- Mouser: no API key; the search, Refine and ProductDetail pages timed out after 60 s on 5 tries. (A curl with a browser User-Agent was blocked by the tool policy, so I did not retry that way.)
- Octopart and OEMSecrets: HTTP 403. Findchips loads but does not list DigiKey or Mouser, only Newark, Avnet, Rutronik, TME, Win Source and similar; I used it only for an indicative availability hint on the hard parts, always labelled.
- So **DigiKey/Mouser part numbers, stock and qty-1/qty-10 prices are all 'not checked'** for every line, and the 1- and 5-board totals could not be computed. I did not guess any distributor part number. The CSVs are keyed on manufacturer part number, which both sites' BOM importers accept; each site will resolve the DK/Mouser SKU and show stock and price on import.
- To close this gap: set DIGIKEY_CLIENT_ID/SECRET (and MOUSER_API_KEY) in the kicad MCP environment and re-run this task, or paste the two CSVs into the distributors' BOM tools and read stock/prices there (then the preferred-distributor split can be made).

## Stage 1: fitted parts

Flag column: STOCK? = hard or doubtful availability at DK/Mouser, ALT = proposed substitute MPN in the buy column, MPN FIX = schematic MPN wrong, MPN ADD = schematic MPN empty, NEW = part not yet in schematic. 'Buy MPN' is what the CSVs use. Footprint-vs-package check is by name, pin count and pitch only (pad geometry not compared).

| Ref(s) | Qty | Value | Package | Schematic MPN | Buy MPN | Manufacturer | LCSC (secondary) | Flag | Note |
|---|---|---|---|---|---|---|---|---|---|
| AE1 | 1 | 2.45 GHz chip antenna | 3.2x1.6 SMD (easyeda ANT-SMD_L3.2-W1.6) | 2450AT18A100E | 2450AT18A100E | Johanson Technology | C89334 | STOCK? | JLC lists it discontinued. Findchips (not DK/Mouser): Newark 2605, Win Source 205k. DK/Mouser stock NOT CHECKED. Alt 2450AT18D0100E is 4-pin, NOT a drop-in. |
| C1,C10 | 2 | 2.2uF 10V X5R | 0201 | GRM033R61A225KE47D | GRM033R61A225KE47D | Murata | C335106 |  |  |
| C3 | 1 | 2.2uF 50V | 0603 | CL10A225KB8NNNC | CL10A225KB8NNNC | Samsung EM | C913904 |  |  |
| C19 | 1 | 1uF 16V | 0402 | CL05A105KO5NNNC | CL05A105KO5NNNC | Samsung EM | C29266 |  | C4 (same part) removed, so qty 1. |
| C5 | 1 | 2.0pF | 0201 | GJM0335C1E2R0WB01D | GJM0335C1E2R0WB01D | Murata | C668326 |  | RF match part, keep exact. |
| C6,C14,C15,C26 | 4 | 100nF 50V X7R | 0603 | CC0603KRX7R9BB104 | CC0603KRX7R9BB104 | Yageo | C14663 |  |  |
| C7,C17,C18,C20,C22 | 5 | 10uF 25V X5R | 0805 | CL21A106KAYNNNE | CL21A106KAYNNNE | Samsung EM | C15850 |  | C18 (and L9) may go DNP, then qty 4. |
| C8 | 1 | 1.5pF | 0201 | GJM0335C1E1R5WB01D | GJM0335C1E1R5WB01D | Murata | C435397 |  | RF match part. |
| C9 | 1 | 10nF 50V X7R | 0402 | GCM155R71H103KA55D | GCM155R71H103KA55D | Murata | C91601 |  |  |
| C12 | 1 | 1.0pF | 0201 | GJM0335C1E1R0WB01D | GJM0335C1E1R0WB01D | Murata | C185624 |  | RF match part. |
| C13 | 1 | 0.3pF | 0201 | GJM0335C1ER30WB01D | GJM0335C1ER30WB01D | Murata | C161289 |  | RF match part. |
| C16 | 1 | 10uF 25V X5R | 0603 | CC0603MRX5R8BB106 | CC0603MRX5R8BB106 | Yageo | C596327 |  |  |
| C40 | 1 | 22uF 10V X5R | 0603 | GRM188R61A226ME15D | GRM188R61A226ME15D | Murata | C84419 |  |  |
| C41 | 1 | 10uF 6.3V X5R | 0402 | GRM155R60J106ME15 | GRM155R60J106ME15D | Murata | C412251 | MPN FIX | Schematic MPN lacks trailing D (parts_2026-10-27.md). |
| C42 | 1 | 47uF 6.3V X5R | 0603 | GRM188R60J476ME15D | GRM188R60J476ME15D | Murata | C140782 |  |  |
| C43 | 1 | 220uF 6.3V X5R | 1206 | MSASJ31LBB5227MTCA01 | GRM31CR60J227ME11L | Murata (was Taiyo Yuden) | C412252 | STOCK/ALT | Taiyo part had 0 stock at JLC; Murata GRM31CR60J227ME11L is the same 1206 220uF 6.3V X5R. DK/Mouser stock of either NOT CHECKED. |
| C44 | 1 | 4.7uF 25V X5R | 0805 | CL21A475KAQNNNE | CL21A475KAQNNNE | Samsung EM | C1779 |  |  |
| C45,C48 | 2 | 100nF 16V X7R | 0402 | CL05B104KO5NNNC | CL05B104KO5NNNC | Samsung EM | C1525 |  | Same MPN on both refs. C45 lacks Manufacturer/LCSC in schematic. |
| C46 | 1 | 10uF 10V X5R | 0603 | CL10A106KP8NNNC | CL10A106KP8NNNC | Samsung EM | C19702 |  |  |
| C47 | 1 | 100pF | 0402 | CL05C101JB5NNNC | CL05C101JB5NNNC | Samsung EM | C26409 |  |  |
| C49,C50 | 2 | 100nF | 0201 | CL03A104KQ3NNNC | CL03A104KQ3NNNC | Samsung EM | C160831 |  |  |
| C51 | 1 | 1uF 25V X5R | 0402 | CL05A105KA5NQNC | CL05A105KA5NQNC | Samsung EM | C52923 |  |  |
| C_NEW (U2 LDO input) | 1 | 10uF X5R, 10V | 0603 (0402 also possible) | (new part, not in schematic) | CL10A106KP8NNNC | Samsung EM | C19702 | NEW | See candidates section. Using the C46 part keeps the line count down. |
| CN1 | 1 | FFC 14-pin 0.5 mm, back flip | Molex 503480-1400 | 503480-1400 | 5034801400 | Molex | C505360 |  | Molex orderable code is 503480-1400 (also written 5034801400). DK/Mouser stock NOT CHECKED. |
| D1,D2 | 2 | TPD1E10B06 ESD | DPY0002A 0.6x1 mm | TPD1E10B06DPYR | TPD1E10B06DPYR | Texas Instruments | C48260 |  |  |
| D3 | 1 | SMF12A TVS | SOD-123FL | SMF12A | SMF12A | Littelfuse | C207255 |  |  |
| F1 | 1 | PTC 0.2 A hold, 0603 | Fuse_0603 | MF-FSMF020X-2 | MF-FSMF020X-2 | Bourns | C210356 |  | 0402 option in f1_polyfuse_options.md needs a footprint change; the fitted 0603 is kept here. |
| IC1 | 1 | AEM10330 energy harvester | QFN-40 5x5 0.5 mm (Parts_2 QFN40P500X500X85-41N-D) | (none) | AEM10330-QFN | e-peas | C22405896 | MPN ADD / STOCK? | MPN taken from the JLC listing, exact orderable code NOT confirmed. Findchips shows only Braemac, stock 0, 4.20 USD. DK/Mouser NOT CHECKED. |
| J1 | 1 | USB-C receptacle 16P | HRO TYPE-C-31-M-12 (easyeda) | (none) | TYPE-C-31-M-12 | HRO Electronics | C165948 | MPN ADD / STOCK? | Findchips has no result. Likely LCSC-only. No verified DK/Mouser drop-in (a different USB-C needs a new footprint). |
| J3 | 1 | Cortex debug 2x5 1.27 mm SMD | Samtec FTSH-105-01-L-DV-K | FTSH-105-01-L-DV-K-TR | FTSH-105-01-L-DV-K | Samtec | C5155080 | MPN FIX | -TR is the reel; for hand assembly use the non-TR code. Newark shows 6354 of the non-TR (not DK/Mouser). |
| L2,L5 | 2 | 2.7nH | 0201 | LQP03HQ2N7B02D | LQP03HQ2N7B02D | Murata | C7216765 |  | RF match part. |
| L3 | 1 | 3.9nH | 0201 | LQP03HQ3N9B02D | LQP03HQ3N9B02D | Murata | C337939 |  | RF match part. |
| L4 | 1 | Ferrite bead 120R | 0402 | CBG100505U121T | BLM15AG121SN1D | Murata (was FH) | C92616 | ALT | FH part is a Chinese brand, unlikely at DK/Mouser. Murata BLM15AG121SN1D is 120R@100MHz 0402 (from memory, datasheet NOT CHECKED; check DC resistance and current vs DECD use). |
| L6,L8 | 2 | 3.5nH | 0201 | LQP03HQ3N5B02D | LQP03HQ3N5B02D | Murata | C3911055 |  | RF match part. |
| L7 | 1 | 4.7uH | 0603 | LQM18PH4R7MFRL | LQM18PH4R7MFRL | Murata | C1858257 | STOCK? | Findchips: only TME listed, stock 0. DK/Mouser NOT CHECKED. Fallback family LQM18PN4R7MFRL (same 0603, from memory, unverified). |
| L9,L10 | 2 | 2.2uH | 0603 | LSCNB1608HKT2R2MD | LSCNB1608HKT2R2MD | Taiyo Yuden | C6079477 |  | L9 may go DNP (unused BUCK1), then qty 1. |
| L11 | 1 | 10uH | 2520 | DFE252010F-100M=P2 | DFE252010F-100M=P2 | Murata (Toko) | C701155 |  |  |
| LED1 | 1 | Red LED | 0402 | SML-P12MTT86R | SML-P12MTT86R | ROHM | C510304 |  |  |
| R8 | 1 | 10k NTC B3380 | 0402 | NCP15XH103F03RC | NCP15XH103F03RC | Murata | C77131 |  |  |
| R9 | 1 | 0R | 0603 | 0603WAF0000T5E | ERJ-3GEY0R00V | Panasonic (was Uniroyal) | C21189 | ALT | Uniroyal not a DK/Mouser staple. ERJ-3GEY0R00V is the standard 0603 jumper (from memory, NOT CHECKED). |
| R10 | 1 | 150k 1% | 0603 | FRC0603F1503TS | RC0603FR-07150KL | Yageo (was Fojan) | C2906993 | ALT | Yageo RC0603FR-07xxxKL pattern, existence NOT CHECKED. |
| R11 | 1 | FM8625H RF switch | DFN-6 1.1x0.7 0.4 mm | FM8625H | FM8625H | Fumin (FM) | C2857391 | STOCK? | Findchips has no result. No verified drop-in; any other switch needs a footprint change. Design fallback: omit R11, fit R21 (0R) per the schematic note. |
| R12,R13,R15,R16 | 4 | 4.7k 1% | 0402 | RC0402FR-074K7L | RC0402FR-074K7L | Yageo | C105871 |  |  |
| R14 | 1 | 560R 1% | 0402 | FRC0402F5600TS | RC0402FR-07560RL | Yageo (was Fojan) | C2909370 | ALT | Pattern-derived MPN, NOT CHECKED. |
| R17,R18,R19 | 3 | 10k 0.1% | 0402 | RT0402BRD0710KL | RT0402BRD0710KL | Yageo | C190095 |  | 0.1% thin film is more than needed; RC0402FR-0710KL (1%) is a cheaper option. |
| RF1 | 1 | U.FL receptacle | SMD U.FL | ECT818000500 | ECT818000500 | ECT | C437254 | ALT? | Chinese brand. Hirose U.FL-R-SMT-1(10) is the genuine part with the same standard footprint (from memory, NOT CHECKED against pads). |
| SW1 | 1 | Tact switch 3x2.5 | B3U-1000P | B3U-1000P | B3U-1000P | Omron | C231329 |  |  |
| U2 | 1 | nPM1300 PMIC | QFN-32 5x5 0.5 mm EP3.6 | nPM1300-QEAA-R7 | nPM1300-QEAA-R7 | Nordic Semiconductor | C7501206 | STOCK? | Findchips (not DK/Mouser): Newark 2482 at 1.08-1.93 USD, Avnet 0. DK/Mouser NOT CHECKED. Do not use the WLCSP variant (different package). |
| U4,U5 | 2 | JST PH 2-pin side entry | THT | S2B-PH-K-S-GW | S2B-PH-K-S(LF)(SN) | JST | C157932 | MPN FIX | Standard JST order code is S2B-PH-K-S(LF)(SN); -GW is an LCSC listing name. |
| U6 | 1 | nRF54L15 SoC | QFN-48 6x6 0.4 mm EP4.6 | nRF54L15-QFAA-R | nRF54L15-QFAA-R | Nordic Semiconductor | C42458750 | STOCK? | Findchips: Rutronik 42,000 at 2.59 USD, Win Source 28k, Braemac 1. DK/Mouser NOT CHECKED. |
| U7 | 1 | SN74AUP1G34 buffer | SC-70-5 | SN74AUP1G34DCKR | SN74AUP1G34DCKR | Texas Instruments | C2675656 |  |  |
| X1 | 1 | 32 MHz crystal 8 pF | 2016 4-pad | XL7EL89CKI-111YLC-32M | XL7EL89CKI-111YLC-32M | YXC | C2965582 | STOCK? | Chinese brand, probably LCSC-only. Candidate: NDK NX2016SA-32MHZ-EXS00A-CS11213 or -CS10925 (Findchips: only Richardson RFPD, stock 0). Load cap/tolerance NOT verified; DK/Mouser NOT CHECKED. Murata XRCGB32M000F-series also 2016 (from memory). |

DNP (not bought):

| Ref | Value | MPN | LCSC |
|---|---|---|---|
| C11 | 2.2pF 0201 | GJM0335C1E2R2WB01D | C710732 |
| C52, C53 | DNP pi pads 0201 | none | - |
| R1, R2 | 5.1k 0402 (CC pull-downs) | RCA025K1FLF | C22369457 |
| R20 | 1M 0402 | 0402WGF1004TCE | C26083 |
| R21 | 0R 0402 | 0402WGF0000TCE | C17168 |
| X2 | 32.768 kHz 2012 | X1A0000610008 (Seiko Epson) | C96341 |

MPN correction sources: parts_2026-10-27.md (C41, J3, IC1, J1), JST standard order code (U4/U5), Yageo/Panasonic/Murata series patterns (R9, R10, R14, L4: from memory, unverified).

## Stage 2: distributor data and the hard parts

Per-line DigiKey/Mouser SKU, stock and prices: **not checked** (see status above). Indicative availability from Findchips on 2026-10-28 (NOT DigiKey/Mouser; prices are ranges across quantity breaks):

| Part | Source | Stock | Price range USD | URL |
|---|---|---|---|---|
| U2 nPM1300-QEAA-R7 | Newark | 2482 | 1.08-1.93 | https://www.findchips.com/search/nPM1300-QEAA-R7 |
| U2 | Avnet / Braemac | 0 / 0 | 1.36-1.57 | same |
| U6 nRF54L15-QFAA-R | Rutronik | 42,000 | 2.59 | https://www.findchips.com/search/NRF54L15-QFAA-R |
| U6 | Win Source / Braemac | 28,140 / 1 | 2.93-4.40 / 2.17-2.45 | same |
| IC1 AEM10330-QFN | Braemac | 0 | 4.20 | https://www.findchips.com/search/AEM10330 |
| AE1 2450AT18A100E | Newark | 2605 | 0.22-0.54 | https://www.findchips.com/search/2450AT18A100E |
| J3 FTSH-105-01-L-DV-K | Newark | 6354 | 0.47-1.10 | https://www.findchips.com/search/FTSH-105-01-L-DV-K |
| L7 LQM18PH4R7MFRL | TME | 0 | 0.12-0.14 | https://www.findchips.com/search/LQM18PH4R7MFRL |
| X1 NDK NX2016SA 32 MHz | Richardson RFPD | 0 | - | https://www.findchips.com/search/NX2016SA-32M |
| R11 FM8625H, CN1 503480-1400, J1 TYPE-C-31-M-12 | - | no results on Findchips | - | https://www.findchips.com/search/FM8625H |

Hardest parts, in the order asked:
1. **U2 nPM1300-QEAA-R7**: exists, QFN-32 5x5 matches the footprint. Plentiful at Newark (not a requested distributor), DK/Mouser not checked. No drop-in alternative (the WLCSP is a different package).
2. **IC1 AEM10330**: the weakest line. Only one aggregator listing (Braemac, 0 stock). Exact orderable code unconfirmed, so check e-peas/DigiKey/Mouser before anything else. No alternative: the footprint and the solar design are specific to this IC.
3. **U6 nRF54L15-QFAA-R**: exists, deep stock elsewhere (Rutronik). DK/Mouser not checked, but both normally carry Nordic.
4. **AE1 2450AT18A100E**: JLC calls it discontinued. Stock exists at Newark and brokers. Alternative 2450AT18D0100E is 4-pin, needs a footprint and keep-out change, so not a drop-in.
5. **X1 32 MHz 2016**: the YXC part is probably not at DK/Mouser. NDK NX2016SA family is the likely replacement (same 2016 size, 4-pad) but the specific code, load capacitance and tolerance must be matched to the nRF54L15 requirement (8 pF load on the current part) before buying.
Other lines with stock or sourcing risk: R11 (FM8625H, no verified drop-in), J1 (HRO USB-C, no verified drop-in), L7 (0 at TME), C43 (use Murata GRM31CR60J227ME11L), RF1 and L4 and R9/R10/R14 (Chinese-brand parts replaced by named-brand substitutes in the buy column).

### New LDO-input cap near U2 (1-10 uF, VDDIO about 3.0 V)

Candidates, DK/Mouser stock NOT CHECKED:
1. Samsung CL10A106KP8NNNC, 10 uF 10 V X5R 0603. Same part as C46, so no extra BOM line. Best choice: the 10 V rating leaves reasonable capacitance at 3 V.
2. Murata GRM188R61A106KE69D, 10 uF 10 V X5R 0603 (from memory, existence NOT CHECKED).
3. Murata GRM155R60J106ME15D, 10 uF 6.3 V X5R 0402, same as C41, no extra line, but a 6.3 V part loses much capacitance at 3 V bias; use only if 0402 is required.

## Stage 3: totals

Not computed: no DigiKey/Mouser prices were obtained. Reference only, from the JLC check in parts_2026-10-27.md (JLC prices, not DK/Mouser; covers 43 of the older lines and omits the run-5 additions): about 12.6 USD per board, which excludes IC1 (Braemac listing 4.20 USD). DK/Mouser qty-1 prices for passives are normally well above JLC prices, so do not use this as a budget.

CSV files (keyed on manufacturer part number, quantity per ONE board, extra column Qty_x5 for five boards):
- C:\Personal-Agents\shared\design\nrf54l15_feather\bom_digikey_2026-10-28.csv
- C:\Personal-Agents\shared\design\nrf54l15_feather\bom_mouser_2026-10-28.csv
'Preferred distributor per line' could not be decided; both CSVs contain every line. Lines flagged STOCK? or ALT? are likely to fail an import on one or both sites.

## Stage 4: schematic field corrections for kicad-designer (apply later)

| Ref | Field | Old | New |
|---|---|---|---|
| C4 | (symbol) | fitted | remove from schematic (decided) |
| C41 | MPN | GRM155R60J106ME15 | GRM155R60J106ME15D |
| J3 | MPN | FTSH-105-01-L-DV-K-TR | FTSH-105-01-L-DV-K (and LCSC C5155080) |
| IC1 | MPN | (empty) | AEM10330-QFN, confirm orderable code first |
| IC1 | Manufacturer | (empty) | e-peas |
| J1 | MPN | (empty) | TYPE-C-31-M-12 |
| U4, U5 | MPN | S2B-PH-K-S-GW | S2B-PH-K-S(LF)(SN) |
| C43 | MPN | MSASJ31LBB5227MTCA01 | GRM31CR60J227ME11L; Manufacturer Taiyo Yuden -> Murata |
| All older parts (AE1, C1, C3, C5-C20, C22, C26, L2-L6, L8-L11, LED1, R10-R14, R17-R19, RF1, U4, U5, X1; R1/R2 DNP) | LCSC Part | has C-number | move into field LCSC, delete LCSC Part (one field only) |
| C44, R8, R9 | LCSC + LCSC Part | both set | keep LCSC, delete LCSC Part |
| C40, C41, C42, C43, C45, CN1, IC1, J1, J3, L7, R15, R16, SW1, U2, U6 | LCSC | (empty) | C84419, C412251, C140782, C412252, C1525, C505360, C22405896, C165948, C5155080, C1858257, C105871, C105871, C231329, C7501206, C42458750 (secondary info, from parts_2026-10-27.md) |
| C45, L7, R17-R19, J3, SW1, U2, U6, IC1 | Manufacturer | (empty) | Samsung EM, Murata, Yageo, Samtec, Omron, Nordic, Nordic, e-peas |
| New LDO-input cap | (new symbol) | - | 10 uF X5R 10 V 0603, MPN CL10A106KP8NNNC, 1 per board, near U2.28/U2.30 |
| R9, R10, R14, L4, RF1 | MPN (optional) | Uniroyal/Fojan/FH/ECT parts | ERJ-3GEY0R00V, RC0603FR-07150KL, RC0402FR-07560RL, BLM15AG121SN1D, U.FL-R-SMT-1(10): only after availability is checked and, for L4/RF1, pads confirmed. Not applied by default |

Count: 14 correction rows (7 are MPN/manufacturer errors, the rest are LCSC field cleanup, the C4 removal, the new cap and one optional substitution row).

## What was not checked
- All DigiKey and Mouser SKUs, stock, lead times, lifecycle (NRND/obsolete) flags and prices (blocked as described above).
- Datasheets and pad geometry of all suggested alternates; substitute MPNs written 'from memory' or 'pattern-derived' may not exist.
- Voltage and DC-bias derating of the caps (C40-C43 are 10/6.3/6.3/6.3 V parts).
