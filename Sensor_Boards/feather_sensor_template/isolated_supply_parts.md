# Isolated-supply parts: JLC stock and price (review items X2, X3, X5)

- Checked: 2026-10-26 by parts-sourcing. Source: JLCPCB parts library live search (jlcpcb.com smtGood/selectSmtComponentList). The local JLCPCB database is empty, the jlcsearch lookup missed most of these parts, and LCSC pages don't show stock, so none of those were used.
- Basis: 10 boards, so unit price is the JLC qty-10 tier. Stock is JLC's `stockCount` on the check date. Prices are USD per part, parts only (no caps/resistors in the totals unless stated).
- "Ext" = JLC extended (a setup fee per unique part per order, about $3 as of my knowledge; confirm on the JLC order page). "Basic" = free. BAT54C,215 is Ext but flagged "preferred" (no fee).
- Package column is JLC's package string. Pin-out, ratings and heights marked "unverified" come from JLC listing text only, not a datasheet I could open. LCSC and Murata datasheet downloads were blocked from here.
- Nothing in the schematics or PCBs was touched.

## 1. Isolated DC-DC modules (3.3 V in)

| Part | LCSC | Stock | Price @10 | Package | JLC | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Murata NXE1S0303MC-R7 (current U4) | C20606969 | 31 | 4.7188 | SMD-5P 12.7x10.4, 4.36 mm tall (JLC attr) | Ext | 3.3 V out, 303 mA, 3 kV, 2.97-3.63 V in. Stock 31 covers 10 boards but is thin. |
| Murata NXE1S0303MC-R13 | C5185191 | 21 | 7.3637 | SMD-5P 12.7x10.4 | Ext | Same part, reel suffix R13; dearer. |
| Murata NXE1S0305MC-R7 | C6943300 | 95 | 6.4913 | SMD-5P 12.7x10.4 | Ext | 5 V out, 200 mA, 3 kV, 2.97-3.63 V in, 1 W. Same package string as the 0303, so the same land pattern is expected. Pin-out unverified. |
| Murata NXE1S0305MC-R13 | C6943298 | 0 | 2.7792 | none listed | Ext | Out of stock. |
| Murata NXJ1S0303MC-R7 | C6621950 | 2 | 6.1935 | SMD-5P 13.7x10.5 | Ext | 4.2 kV, bigger footprint, 2 in stock. Not a drop-in. |
| Murata MTU1S0305MC-R | C6704444 | 0 | 18.4395 | SMD-5P 8.4x8.2 | Ext | Out of stock. |
| Evisun / Jetek / YLPTEC B0303S-1WR3, B0305S-1WR3 (SIP 11.6x6) | C7465186 (B0305S, Evisun) | 985 | 0.9412 | SIP 11.6x6, through-hole pins | Ext | 3.3 V in (2.97-3.63 V), 5 V 200 mA, only 1.5 kV. Footprint change, and through-hole so JLC may hand-solder it. Other stock: B0305S YLPTEC C7418874 (2918, 1.167), B0303S Jetek C387584 (37, 1.1147). |

No other SMD 1 W isolated module with a 3.3 V input and Murata-size pinout is stocked at JLC. The cheap parts are SIP through-hole and only 1.5 kV.

Both NXE1 variants are unregulated and need 2.97-3.63 V in (JLC attribute). With VSENS at 3.0 V that is at the bottom of the range, as the review said.

## 2. Transformer drivers (SN6505 and equivalents)

| Part | LCSC | Stock | Price @10 | Package | JLC | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| TI SN6505BDBVR | C74518 | 2972 | 0.4960 | SOT-23-6 | Ext | 2.25-5.5 V, 1 A, higher-frequency variant (B). Best pick. |
| TI SN6505BDBVT | C2156022 | 793 | 0.6220 | SOT-23-6 | Ext | Same part, small reel. |
| TI SN6505ADBVR | C2155930 | 6217 | 1.7432 | SOT-23-6 | Ext | A variant (lower frequency), 3.5x the price of B. |
| TI SN6505ADBVT | C2650143 | 0 | 1.0803 | SOT-23-6 | Ext | Out of stock. |
| COSINE COSN6505C | C30212524 | 1852 | 0.3323 | SOT-23-6 | Ext | Clone, 2.5-5.5 V, 1 A. Unverified pin-out and frequency. Cheaper alternative, not a proven drop-in. |
| TI SN6501DBVR | C49451 | 35263 | 0.4158 | SOT-23-5 | Ext | 3.0-5.5 V, 350 mA, no soft-start. Different package (5-pin). Fallback only: 3.0 V minimum is at the VBAT floor. |
| TI SN6505BQDBVRQ1 (auto) | C1849490 | 3306 | 0.9854 | SOT-23-6 | Ext | Automotive grade, dearer. |

## 3. Transformers for SN6505 (1:1.5 to 1:2.2, 1 kV or more)

Height is not in the JLC data and I could not open a datasheet, so "unverified" means check it before layout. Sizes are JLC package strings.

| Part | LCSC | Stock | Price @10 | Package (L x W) | Height | Ratio / isolation | JLC | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| JASN CM0601S | C5352974 | 709 | 0.3258 | SMD-6, 7.6 x 6.8 mm | unverified | 1:1:2.22:2.22 (CT primary and secondary), 3 kV, 50 uH, 1 uH leakage | Ext | Ratio matches the 1:2.2 target. Smallest and cheapest. Inductance and Vs product vs SN6505 unverified. Best pick. |
| Wuxi Maxinmicro MXPP6-3K6250 | C42414210 | 1021 | 0.6695 | SMD-6, 7.1 x 6.6 mm | unverified | 1:2 (JLC attr), 3 kV, 475 uH | Ext | Second source in the same size. Winding detail (CT or not) unverified. |
| Wurth 750315371 (the family named in the task) | C5184247 | 0 | n/a | SMD | n/a | not listed | Ext | Out of stock, no spec on the JLC listing. Not usable. |
| Wurth 750313626 | C17352323 | 57 | 3.9626 | SMD, about 11.3 x 6.1 mm (from pad span, rough) | unverified | 1:2, 3.3 V to 5 V, 5 kV, 340 uH | Ext | Wurth part for 3.3 V-in designs but low stock and 12x the price. |
| Wurth 760390014 | C2802211 | 849 | 2.7088 | SMD-6, 7.1 x 6.7 mm | unverified | 1:1.3, 3.125 kV, 475 uH | Ext | Ratio too low for 3.0 V VBAT: 3.0 x 1.3 = 3.9 V before the diode drop. Only fits if VDD_ISO is lower. |
| Wurth 750315240 | C5122699 | 613 | 5.1934 | SOP-6, 12.3 x 10.4 mm | unverified | 1:1.1, 5 kV | Ext | Ratio too low, and large. |
| Coilcraft DA2304-ALD | C19190861 | 79 | 11.395 | SMD-8, 10.3 x 8.1 mm | unverified | 1:2.2, 2.5 kV, 3.3-6 V | Ext | Right ratio, 35x the price. Coilcraft DA2303-ALD C19948247 (34 in stock, 8.8286) is the same size and 1:1 class. |
| Wuxi Maxinmicro MXPP8-30-1250 | C19943837 | 1127 | 0.7677 | SMD-8, 12.1 x 8.3 mm | unverified | 1:2.5, 3 kV, 200 uH | Ext | Ratio a bit high but workable with a LDO; bigger. |
| JWD ST06D01A0 | C46628476 | 29 | 1.3929 | SMD-6, 9.4 x 8.6 mm | unverified | 1:3.4 (CT), 3 kV | Ext | Ratio too high, low stock. |

Ratio check for the designer: VBAT 3.0 V to 4.2 V through 1:2.2 gives about 6.6 V to 9.2 V before the diode and winding drops, so the LDO input needs a rating of at least 12 V (table 4 uses 16 V and 24 V parts).

## 4. Low-noise LDOs for the isolated side (Vin of 6 V or more, SOT-23-5)

The TPS7A02xx / TPS7A20xx / TLV755xx families are only rated 5.5-6.5 V in, so they don't meet the 6 V-plus input need once VBAT-fed with a 1:2.2 transformer. They are left out.

| Part | LCSC | Stock | Price @10 | Package | Vout | Vin max | Noise | JLC | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TI LP2985-33DBVR | C95414 | 152157 | 0.2186 | SOT-23-5 | 3.3 V fixed | 16 V | 30 uVrms (with bypass cap) | Ext | 150 mA. Dropout 575 mV at 150 mA, about 200 mV at 50 mA. Best 3.3 V pick. |
| onsemi NCP718ASN330T1G | C603785 | 6021 | 0.3732 | TSOT-23-5 | 3.3 V fixed | 24 V | 36 uVrms | Ext | 300 mA, 440 mV dropout at 300 mA. Second pick, higher Vin margin. |
| onsemi NCP718ASNADJT1G | C440035 | 2108 | 0.5467 | TSOT-23-5 | adjustable 1.2-5 V (about 3.9 V with a divider) | 24 V | 36 uVrms | Ext | Best pick for 3.9 V. Needs two resistors (basic parts, see section 7). |
| TI TPS70939DBVR | C2868697 | 256 | 0.8610 | SOT-23-5 | 3.9 V fixed | 30 V | 190 uVrms | Ext | Only fixed 3.9 V at JLC with enough Vin. Noisier, low stock, 150 mA. |
| TI TPS70933DBVR | C89347 | 12044 | 0.3355 | SOT-23-5 | 3.3 V fixed | 30 V | 190 uVrms | Ext | Noisier than the LP2985 and NCP718. |
| ADI LT1761ES5-3.3#TRMPBF | C655159 | 134 | 4.1983 | TSOT-23-5 | 3.3 V fixed | 20 V | 20 uVrms | Ext | Quietest, but 20x the price. Only if the OEM needs it. |
| Microchip MIC5219-3.3YM5-TR | C29613 | 5246 | 0.5925 | SOT-23-5 | 3.3 V fixed | 12 V | not given | Ext | 500 mA, lower Vin margin. |
| onsemi NCP186AMX390TAG | C892288 | 284 | 0.4223 | XDFN-8 1.2x1.6 | 3.9 V fixed | 5.5 V | 48 uVrms | Ext | Fixed 3.9 V but only 5.5 V in. Fits the NXE1S0305 option (5 V in) only, and the XDFN land pattern is tiny. |

For the NXE1S0305MC option the module output is about 5 V, so a 3.3 V or 3.9 V LDO there works with any of the above. The 3.9 V adjustable part is the only one that is both low-noise and in SOT-23-5.

## 5. Dual Schottky rectifiers, SOT-23, common cathode (full-wave from a centre-tapped secondary)

| Part | LCSC | Stock | Price @10 | Package | Vr / If | JLC | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Nexperia BAT54C,215 | C37704 | 169566 | 0.0154 | SOT-23 | 30 V / 200 mA | Ext, preferred (no setup fee) | Best pick. |
| onsemi BAT54CLT1G | C14308 | 200883 | 0.0308 | SOT-23 | 30 V / 200 mA | Ext | Drop-in. |
| Changjing BAT54C | C2135 | 223788 | 0.0275 | SOT-23 | 30 V / 200 mA | Ext | Drop-in. |
| LRC LBAT54CLT1G | C49991 | 292223 | 0.0194 | SOT-23 | 30 V | Ext | JLC lists this one as "series connection", which is wrong for a "C" part. Check the datasheet pin-out before using it. |
| Nexperia BAS40-04W,115 / onsemi BAS40-04LT1G | C8650 / C78265 | 4128 / 21989 | 0.1246 / 0.0387 | SOT-323 / SOT-23 | 40 V | Ext | These are series (-04), not common cathode. Don't use for the rectifier. |

At 50 mA and 0.5 V or so, forward drop is the reason to keep a Schottky, not a silicon diode.

## 6. I2C isolators

Important: on the ISO164x family the two sides are not the same. From the TI ISO164x datasheet (SLLSFC2D) pages 8 to 10, text extraction:
- Side 1: VCC1 3.0 to 5.5 V (UVLO rising 2.7 to 2.9 V). Output low VOL1 is about 0.65 to 0.71 V (buffered level, ISO-style).
- Side 2: VCC2 2.25 to 5.5 V (UVLO rising 2.3 to 2.6 V). Output low VOL2 is 0.4 V or lower, a normal I2C level.
So the 2.25 V minimum and the low output-low level are on the same side, side 2, not on side 1. Put the nRF host (VSENS 3.0 V, VIL 0.9 V) on side 2, and the sensor (VDD_ISO, 3.0 V or more) on side 1. The sensor then sees about 0.7 V low, which the Atlas OEM should read as low (OEM VIL at 3.3 V is about 0.9 V, unverified). The columns of the TI table came out garbled in text extraction, so confirm the VCC1/VCC2 and VOL1/VOL2 assignment on pages 8 and 10 of the datasheet before committing the schematic.

| Part | LCSC | Stock | Price @10 | Package | Channels | Isolation | JLC | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ADI ADuM1250ARZ-RL7 (current U3) | C13839 | 5066 | 3.9953 | SOIC-8 150 mil | 2 bidirectional | 2.5 kV | Ext | 3-5.5 V both sides. Side-1 VOL 0.6-0.9 V (unverified). Stock is fine; the cut-tape ADuM1250ARZ C579378 has 154 at 4.7417. |
| ADI ADuM1250ARZ-RL7-HXY | C52260392 | 4038 | 1.6793 | SOP-8 | 2 bidirectional | not given | Ext | Third-party HXY part, unverified. Cheaper but not a known-good drop-in. |
| TI ISO1640BDR | C5122339 | 5769 | 1.4191 | SOIC-8 | 2 bidirectional, SDA and SCL | 3 kV (8-pin D) | Ext | Same 8-pin order as the ADuM1250 per the TI pin figure (VCC1, SDA1, SCL1, GND1 on one side, mirrored on the other). Verify the ADuM1250 order once more on the schematic symbol. Best pick. |
| TI ISO1641BDR | C5216235 | 0 | 2.6974 | SOIC-8 | SDA bidirectional, SCL one way | 3 kV | Ext | Out of stock. |
| TI ISO1540DR | C179739 | 20922 | 0.7137 | SOIC-8 | 2 bidirectional | 2.5 kV | Ext | 3.0 V minimum both sides. Cheap, no 2.25 V side. Check its VOL. |
| Chipanalog CA-IS3020S | C528661 | 8234 | 0.7284 | SOIC-8 | 2 bidirectional | 5 kV | Ext | Third-party, spec unverified. |
| TI ISO1642DWR | C5216228 | 679 | 4.1917 | SOIC-16 wide (10.3 x 7.5) | I2C 2 bidirectional + 2 GPIO (one each way) | 5 kV | Ext | 3-channel-capable, INT can use one GPIO. Wide body means a new footprint and a longer barrier. |
| TI ISO1644DWR | C5216232 | 872 | 4.3210 | SOIC-16 wide | I2C 2 bidirectional + 3 one-way GPIO | 5 kV | Ext | Same, with 3 GPIOs. |
| TI ISO1643DWR | C5216229 | 41 | 7.3326 | SOIC-16 wide | I2C + 2 GPIO | 5 kV | Ext | Low stock, dear. |

3-channel route without changing the I2C isolator: keep ISO1640BDR (or ADuM1250) and add one single-channel isolator for INT, e.g. TI ISO7721DR (C366164, stock 28224, 0.5582, SOIC-8, 1 forward + 1 reverse, 2.25-5.5 V both sides, 5 kV, Ext) or Chipanalog CA-IS3722HS (C428879, stock 27967, 0.347, SOIC-8, Ext). Cost about 0.35 to 0.56 and one SOIC-8 more than a 16-pin part.

## 7. CN1 and the R_ID resistors

| Part | LCSC | Stock | Price @10 | Package | JLC | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Molex 503480-1400 (5034801400), CN1 | C505360 | 16549 | 0.3091 | FPC 14P 0.5 mm, SMD right angle, top and bottom entry, hinged lid | Ext | Stock is fine. Matches the schematic part (14P, 0.5 mm). |
| UNI-ROYAL 0402WGF1001TCE, 1k 1 % 0402 | C11702 | 19061469 | 0.0013 | 0402 | Basic | |
| UNI-ROYAL 0402WGF2201TCE, 2.2k 1 % 0402 | C25879 | 2987002 | 0.0011 | 0402 | Basic | |
| UNI-ROYAL 0402WGF4701TCE, 4.7k 1 % 0402 | C25900 | 14568158 | 0.0021 | 0402 | Basic | |
| UNI-ROYAL 0402WGF1002TCE, 10k 1 % 0402 | C25744 | 18534186 | 0.0024 | 0402 | Basic | |
| UNI-ROYAL 0603WAF1001T5E, 1k 1 % 0603 | C21190 | 34214403 | 0.0017 | 0603 | Basic | |
| UNI-ROYAL 0603WAF2201T5E, 2.2k 1 % 0603 | C4190 | 5954717 | 0.0018 | 0603 | Basic | |
| UNI-ROYAL 0603WAF4701T5E, 4.7k 1 % 0603 | C23162 | 16741743 | 0.0028 | 0603 | Basic | |
| UNI-ROYAL 0603WAF1002T5E, 10k 1 % 0603 | C25804 | 39434855 | 0.0021 | 0603 | Basic | |

Field changes to hand to kicad-designer (not made here): U4 (and CN1) LCSC and MPN fields as per the tables above; R1 per board as in review item X1 (EC 1k C11702, DO 2.2k C25879, ORP 4.7k C25900, pH 10k C25744, 0402). The template U3/U4/CN1 had no LCSC number (review X3). J5 should be excluded from the BOM.

## Best picks

1. **NXE1S0305MC-R7** C6943300, 95 in stock, 6.4913 each, Ext. Or keep NXE1S0303MC-R7 C20606969 (31 in stock, 4.7188) only for a bench build.
2. **LDO, 3.3 V:** LP2985-33DBVR C95414 (152157 in stock, 0.2186). **LDO, about 3.9 V:** NCP718ASNADJT1G C440035 (2108, 0.5467) plus two basic resistors.
3. **Driver:** SN6505BDBVR C74518 (2972, 0.4960). COSN6505C C30212524 is a cheaper clone, unverified.
4. **Transformer:** JASN CM0601S C5352974 (709, 0.3258, 7.6 x 6.8 mm, 1:2.22, 3 kV). Second source MXPP6-3K6250 C42414210 (1021, 0.6695, 7.1 x 6.6 mm). Heights unverified for both. Wurth 750315371 is out of stock.
5. **Rectifier:** BAT54C,215 C37704 (169566, 0.0154, preferred).
6. **I2C isolator:** ISO1640BDR C5122339 (5769, 1.4191) with the host on side 2. For INT add ISO7721DR C366164 (0.5582) or step up to ISO1644DWR C5216232 (wide SOIC-16).
7. **CN1:** C505360 (16549, 0.3091). **R_ID:** the basic UNI-ROYAL 0402 parts above.

## Out of stock or unusable at JLC (2026-10-26)

- Wurth 750315371 (0 stock, no spec).
- SN6505ADBVT C2650143 (0).
- NXE1S0305MC-R13 C6943298 (0), MTU1S0305MC-R (0).
- ISO1641BDR C5216235 (0).
- Wurth 750315240, 760390014 listed but the ratio is too low for 3.0 V VBAT.

## Added cost per board at 10 boards (parts only)

Passives (caps, divider resistors) are not included, and neither is the extended-part setup fee, which is per unique part per order.

| Option | Parts | Sum per board | Change vs the current NXE1S0303MC (4.7188) |
| --- | --- | --- | --- |
| A1: NXE1S0305MC + LDO 3.3 V | 6.4913 + 0.2186 (LP2985-33) | **6.71** | +1.99 |
| A2: NXE1S0305MC + LDO about 3.9 V | 6.4913 + 0.5467 (NCP718 ADJ) + about 0.005 (2 x 1 % 0402) | **7.04** | +2.32 |
| B1: SN6505B + transformer + diode + LDO 3.3 V | 0.4960 + 0.3258 + 0.0154 + 0.2186 | **1.06** | -3.66 |
| B2: SN6505B + transformer + diode + LDO about 3.9 V | 0.4960 + 0.3258 + 0.0154 + 0.5467 + about 0.005 | **1.39** | -3.33 |
| B1 with the 3.3 V NCP718ASN330T1G instead | 0.4960 + 0.3258 + 0.0154 + 0.3732 | 1.21 | -3.51 |

Option B also needs 4 new extended parts per order (driver, transformer, diode, LDO), one of them preferred (the diode), so about $9 of setup fees against about $3 for option A (only the LDO is new, since NXE1S0305 replaces NXE1S0303). At 10 boards that is $0.90 per board for B against $0.30 for A. B is still cheaper per board, and B uses VBAT, not the 100 mA VSENS budget.

Isolator change (optional, on top of the above): ISO1640BDR is 2.58 cheaper per board than ADuM1250ARZ-RL7 (1.4191 vs 3.9953). Adding ISO7721DR for INT adds 0.56.

Heat note for option B: at VBAT 4.2 V the rectified rail is about 9 V, so a LDO at 50 mA dissipates about 0.25 W in SOT-23-5. That is workable but near the limit. EC draws up to 26 mA, ORP 3.5 mA and DO 2.5 mA, so it is fine for these three boards.

## Open items

- Transformer heights (all) and the NXE1S0305MC pin-out: not verified, no datasheet could be opened from here (LCSC and Murata block downloads).
- ISO164x VCC1/VCC2 and VOL1/VOL2 assignment came from a text extraction with scrambled table columns. Confirm on the datasheet.
- SN6505 plus CM0601S (50 uH, Vs product) compatibility is not checked. kicad-designer's electrical comparison should confirm it.
