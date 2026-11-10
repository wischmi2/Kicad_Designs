# feather_water_level: parts research

Date of all JLCPCB stock/price checks: 2026-10-25 (live JLCPCB parts search API; the local kicad-MCP JLCPCB database is empty, so it was not used). Prices are USD at qty 1 unless noted. Datasheets read: TI TPS63802, TPS63900, TPS63031, SN74AVC2T245, TXU0202, SN74LVC1T45, TPD4E05U06 (pdftotext of the TI PDFs). No schematic was edited.

## Stage 1: sensor, cable, connector

### What DFRobot documents (SEN0311 / A02YYUW)
Sources: wiki.dfrobot.com/_A02YYUW_Waterproof_Ultrasonic_Sensor_SKU_SEN0311, its reference doc (/sen0311/docs/21651), Arduino example (/sen0311/docs/21654), product page dfrobot.com/product-1935.html.

| Item | Value | Status |
|---|---|---|
| Supply | 3.3 to 5 V, average current <= 8 mA, standby <= 5 mA | confirmed (wiki) |
| Range / blind zone | 3 to 450 cm (flat target), 3 cm blind zone | confirmed |
| Accuracy | +/-1 cm (product page and DFRobot blog). Resolution 1 mm | confirmed |
| Response time | 100 ms (real-time mode); processed mode 100 to 300 ms | confirmed |
| Beam angle / rating / temp | 60 deg, IP67, -15 to 60 C operating | confirmed |
| Pins | 1 VCC, 2 GND, 3 RX (output mode select), 4 TX (UART out) | confirmed (wiki pin table) |
| UART | 9600 baud, 8N1, TTL | confirmed |
| Frame | 4 bytes: 0xFF header, DATA_H, DATA_L, SUM. Distance (mm) = DATA_H*256 + DATA_L. SUM = (0xFF + DATA_H + DATA_L) & 0xFF. Example FF 07 A1 A7 = 1953 mm | confirmed (reference doc and Arduino example) |
| RX pin | Floating or HIGH = processed (smoothed) value, 100 to 300 ms. LOW = real-time value, 100 ms. No trigger command: the sensor streams frames on its own | confirmed. Idle level of TX not stated (UART idle is normally high; unverified) |
| Plug | Shipping list says "PH2.0-4P Connector x1" (JST PH style, 2.0 mm pitch, 4 way). Product page also says "A connection cable is included" | Plug type from shipping list. Whether the plug is crimped on the cable end or supplied loose is NOT stated: unverified |
| Cable length | not stated anywhere I could fetch | UNVERIFIED |
| Wire colours / colour-to-pin map | not stated in text (only in a connection image I could not read) | UNVERIFIED |
| Plug pin order | not stated | UNVERIFIED |
| Startup time after power-on | not stated (only the 100 ms response time) | UNVERIFIED. Plan to ignore frames for the first ~0.5 s and measure on the real unit |
| Peak current | not stated (only the 8 mA average) | UNVERIFIED. Size the 3.3 V supply for the average, check the peak on the bench |
| Error / out-of-range frame values | not documented on the pages read | UNVERIFIED |

Things to measure on the first sample: cable length, colour map, whether the PH housing is fitted, plug pin order, time to first valid frame, peak current.

### Design notes that follow from the protocol
- Frame is 4 bytes at 9600 baud, about 4.2 ms on the wire, one per 100 to 300 ms. Trivial for any level shifter.
- The sensor RX pin selects the output mode. Do not leave it to chance: with a level translator on this line, a floating or low input would put the sensor in real-time mode (noisier). If processed mode is wanted, either keep the host TX line idling high, or add a 100 k pull-up to the 3.3 V rail on the sensor side of the translator. Note TXU0202 has 5 Mohm internal pull-downs on its inputs, so a tri-stated host TX would read as LOW and select real-time mode unless that pull-up is fitted.
- Firmware already sets CN1 signals to input or low before VSENS goes off. With the translator's Ioff / VCC isolation and the buck-boost's load disconnect, nothing back-powers the sensor.

### Board-side connector options (22.86 mm wide edge at x = 90, opposite CN1)
Dimensions are typical manufacturer figures, not read from drawings in this run: treat as unverified and check against the footprint.

| Option | Board part | Board space (of 22.86 mm) | Height | Cost (part + mating) | Swapping a sensor | Damp environment |
|---|---|---|---|---|---|---|
| (a) Matching header for the stock PH2.0-4P plug | JST S4B-PH-SM4-TB (SMD side entry) C265102, or S4B-PH-K-S (THT side entry) C157926 | about 8 mm wide (4 x 2.0 pitch + body) | about 6 mm (unverified) | $0.31 SMD / $0.07 THT. Plug comes with the sensor | Best: unplug and replug, no tools | Not sealed. Latch-less, can wick moisture. Conformal-coat the board, keep it inside the enclosure, add cable strain relief |
| (b) Cut plug, pluggable screw terminal | Kefa KF2EDGR-3.5-4P C441173 (3.5 mm pitch, right-angle plug-in). Header only is C441173; the plug half is a separate part | about 14 mm wide | about 8 to 10 mm (unverified) | about $0.11 header (plug half not priced here) | Needs a screwdriver, cable cut once, fine for swapping after that | Screws and bare copper corrode in damp air; wire ferrules help. Worst option for a damp box |
| (c) Cut plug, JST PH crimped by Brian | Same header as (a). Housing PHR-4 C111514 ($0.017), crimp contacts SPH-002T-P0.5S C111515 ($0.0086 each) | same as (a) | same as (a) | about $0.03 per cable plus a crimp tool | Same as (a) once crimped; a spare plug is a few cents | Same as (a). Only needed if the stock plug is missing or the cable must be shortened |
| (d) Panel-mount waterproof connector on the enclosure, short pigtail to the board PH header | Not on JLCPCB. Candidates sold elsewhere (M8 or M12 4-pin panel receptacle, GX12-4 or similar): none checked, no source verified | pigtail plugs into the same PH header, so the board footprint stays at 8 mm | adds nothing to the board | about $3 to $10 plus the panel hole (unverified estimate) | Easy, the sensor cable end must then be that connector type, which the stock cable is not: the stock probe cable would still need a cut and re-terminate | Best sealing if the enclosure is wet. Overkill if the enclosure only needs a cable gland |
| (e) Cable gland on the enclosure, stock cable passes through, plug into board PH header | PH header as (a); gland is enclosure hardware | 8 mm | none on board | gland a few dollars | Open the lid to swap | Enclosure seals the cable, board stays dry. The gland must clear the PH plug (the plug is about 8 mm wide, so a gland hole for a thin 4-core cable only works if the plug is fitted after the cable is through) |

### Recommendation
Use a JST PH 2.0 mm 4-pin SMD side-entry header on the x = 90 edge, pin order VCC, GND, RX, TX (matches the wiki table; confirm against the plug on the received sample before layout). That mates directly with the plug DFRobot ships (option a), costs about $0.31, takes about 8 mm of the 22.86 mm edge, and if the cable turns out to have bare ends or a different plug, Brian can crimp PHR-4 housings himself (option c, about $0.03 per cable). Handle damp by sealing at the enclosure (cable gland, option e) and conformal-coating the board, not by the connector; go to a panel-mount waterproof connector (d) only if the sensor must be unplugged from outside the box. The PH header also lets the TVS and footprint stay identical across (a), (c) and (e). Connector shell/GND: this board is non-isolated, so no barrier changes.

## Stage 2: parts (JLCPCB, checked 2026-10-25)

"Ext" = JLCPCB extended part (adds a per-part setup fee), "Basic" = basic library part. Almost every IC here is extended; only the Samsung 0603 caps listed are basic.

### 1. 3.3 V buck-boost (VIN 2.7 to 4.5 V, >= 100 mA, EN threshold well below 3.0 V, sub-uA shutdown)

| Role | Part | LCSC | Stock | Price qty 1 / 10 | Package | Class | Key numbers (datasheet) |
|---|---|---|---|---|---|---|---|
| Primary | TI TPS63802DLAR | C2845237 | 37,341 | $0.908 / $0.764 | VSON-10 2x3 | Ext | VIN 1.3 to 5.5 V, 2 A, 11 uA Iq, shutdown 45 nA typ / 600 nA max (-40 to 85 C), EN VIH 1.2 V / VIL 0.4 V, true load disconnect, adjustable via FB divider (R1 511 k from VOUT to FB, R2 91 k FB to GND gives 3.3 V per datasheet table), 0.47 uH inductor, 22 uF out cap. Reel part. Alt ordering code TPS63802DLAT C1849531 stock 358, $1.574 |
| Alt 1 | TI TPS63031DSKR (fixed 3.3 V) | C15516 | 4,629 | $1.108 / $0.895 | SON-10 2.5x2.5 | Ext | VIN 1.8 to 5.5 V, 800 mA (VIN >= 3.6 V buck mode, 500 mA boost), shutdown 0.1 uA typ / 0.9 uA max, EN VIH 1.2 V / VIL 0.4 V, load disconnect, FB tied to VOUT (no divider), 1.5 uH inductor, 10 uF in, 2 x 10 uF out, 0.1 uF on VINA. Fixed voltage, so no resistors to select |
| Alt 2 | TI TPS63900DSKR | C1518762 | 6,619 | $1.123 / $0.977 | WSON-10 2.5x2.5 | Ext | VIN 1.8 to 5.5 V, 400 mA, 75 nA Iq, 60 nA shutdown, EN VIH 1.2 V / VIL 0.4 V, 2.2 uH, 10 uF in, 22 uF out. Output is set by resistors on CFG pins (3.3 V with SEL high: RCFG1 36.5 k, RCFG2 0 ohm for no current limit per Table 7-2; confirm in the datasheet before drawing). Lowest standby loss, but the 36.5 k plus extra pins are fiddly. Load disconnect in shutdown not confirmed in the text I read: unverified. Datasheet notes it does not discharge the output actively |
| Also seen | TPS63000DRCR C24966 stock 23,516 $0.82; RT6150BGQW C147972 stock 1,014 $0.94 | | | | | | Not checked against the EN / shutdown requirements |

TPS63802 is the default. At 100 mA it is a large part for the job (2 A), but it has the best stock, the lowest price per piece, and the clearest EN and shutdown specs. TPS63031 is the choice if a fixed 3.3 V (no divider) is preferred. All three run from VBAT 3.0 to 4.2 V and see EN at 3.0 V from VSENS as a clean logic high.

Support parts for the TPS63802 (datasheet values):

| Part | LCSC | Stock | Price | Package | Class | Note |
|---|---|---|---|---|---|---|
| L1 0.47 uH: Murata DFE201612E-R47M=P2 | C668312 | 11,319 | $0.172 | 0806 (2016 mm) | Ext | Same family as the TI-listed Toko DFE201612E 0.47 uH, 5.5 A, 26 mohm. Isat of this exact Murata part not read: unverified |
| L1 alt: XR XRNR201610-0.47uH/N | C5289249 | 3,170 | $0.039 | 0806 | Ext | Cheap clone, ratings not read: unverified |
| L1 alt (TI reference): Coilcraft XFL4015-471MEC | C18221164 | 1,801 | $4.23 | 4x4 mm | Ext | Expensive, 5.4 A, 7.6 mohm |
| Cin 10 uF 10 V X5R: Samsung CL10A106KP8NNNC | C19702 | 13,030,358 | $0.027 | 0603 | Basic | Datasheet wants 4 uF effective at VIN |
| Cout 22 uF 6.3 V X5R: Samsung CL10A226MQ8NRNC | C59461 | 3,343,750 | $0.031 | 0603 | Basic | Datasheet wants 7 uF effective for VOUT > 2.3 V. A 6.3 V 0603 22 uF loses much of its capacitance at 3.3 V bias, so use the 0805 part below, or two in parallel, if effective capacitance matters |
| Cout alt 22 uF 0805: Samsung CL21A226MQQNNNE | C5674 | 3,709,501 | $0.044 | 0805 | Ext | Better DC-bias behaviour |
| R1 511 k 1 % 0603: 0603WAF5113T5E | C23194 | 62,720 | $0.0015 | 0603 | Ext | FB top resistor, VOUT to FB |
| R2 91 k 1 % 0603: 0603WAF9102T5E | C23265 | 134,765 | $0.002 | 0603 | Ext (preferred) | FB bottom resistor |

If TPS63031 is chosen instead: L 1.5 uH, e.g. Murata DFE252012F-1R5M=P2 C909806 (stock 6,564, $0.113, 1008) (TI lists series, not this exact part: unverified), 10 uF in and 2 x 10 uF out (use C19702), 0.1 uF VINA cap (C1591 CL10B104KB8NNNC, stock 2.29 M, $0.0077, Ext).
If TPS63900: L 2.2 uH Murata DFE201612E-2R2M=P2 C337893 (stock 34,897, $0.156, 0806) exactly as TI lists, RCFG1 36.5 k = 0603WAF3652T5E C23029 (stock 74,414), 10 uF in, 22 uF out.

### 2. Level translation (VCCA = VSENS 3.0 V host side, VCCB = 3.3 V sensor side, 9600 baud)

| Role | Part | LCSC | Stock | Price qty 1 | Package | Class | Notes |
|---|---|---|---|---|---|---|---|
| Option A (recommended) | TI TXU0202DCUR, 2-bit fixed direction | C5186957 | 15,139 | $0.861 ($0.738 at 10) | VSSOP-8 | Ext | One chip, channel 1 A1 to B1Y (host TX to sensor RX), channel 2 B2 to A2Y (sensor TX to host RX): exactly the UART pair. Ports 1.1 to 5.5 V, VCC isolation (if either rail < 100 mV or absent all outputs go high-Z), Ioff, Schmitt inputs, supply current 2.5 uA typ. OE pin can be tied to either rail. Input 5 Mohm pull-downs (see note on RX mode above). Smaller alt: TXU0202DTTR C18197534, X1SON-8 2x1 mm, stock 6,640, $0.804 |
| Option B | 2 x TI SN74LVC1T45DBVR | C7843 | 279,660 | $0.0835 each (about $0.17 for 2); $0.067 each at 50 | SOT-23-6 | Ext | Cheapest, huge stock. VCC 1.65 to 5.5 V, VCC isolation and Ioff confirmed in datasheet. DIR is referenced to VCCA: tie DIR high on the host-to-sensor channel and low on the sensor-to-host channel (A = host side, B = sensor side). No bus hold, so a floating host TX input is a real input (add a pull-up). Alt packages: DCKR C9382 SC-70-6 stock 44,657 $0.234; DBVT C116653 stock 3,852 |
| Option C | TI SN74AVC2T245RSWR | C128418 | 171,839 | $0.326 | WQFN-10 1.4x1.8 | Ext | Dual transceiver with independent DIR1, DIR2 (DIR referenced to VCCA), Ioff, VCC isolation, VCC 1.2 to 3.6 V (3.0/3.3 V is inside the range). Tiny and hard to hand-solder. VSSOP version SN74AVC2T45DCUR is a single-DIR part, not suitable. Do not use SN74LVC2T45 (one DIR pin for both channels, wrong for opposite directions) |
| Not suitable | TXB0102 (auto-direction, push-pull drivers weak and not partial-power-down friendly) | C60709 | | | | | Not recommended for UART |

Option A is the neatest (one chip, fixed directions, no DIR wiring); option B is cheapest by about $0.70 per board with two DIR ties. Both meet the neither-side-back-powered requirement per their datasheets.

### 3. Low-capacitance TVS at the cable connector

| Role | Part | LCSC | Stock | Price qty 1 | Package | Class | Key numbers |
|---|---|---|---|---|---|---|---|
| Recommended | TI TPD4E05U06DQAR (4-channel) | C138714 | 199,782 | $0.083 | USON-10 1x2.5 mm | Ext | VRWM 5.5 V, 0.42 to 0.5 pF per line, 10 nA max leakage, IEC 61000-4-2 level 4 (+/-15 kV air), surge 2.5 A (IEC 61000-4-5). Covers VCC, TX, RX and one spare line; GND pin to board GND. Datasheet read |
| Alt (pin count) | ProTek SRV05-4-P-T7 | C85364 | 46,080 | $0.234 | SOT-23-6 | Ext (preferred) | 4-line 5 V array, easier to hand-solder; capacitance and VRWM not read: unverified |
| Alt (cheap) | Semtech SRV05-4.TCT | C13612 | 101,888 | $0.163 | SOT-23-6L | Ext | As above, unverified numbers |
| Alt (clones of the TI part) | Tech Public C2827646 (stock 11,277, $0.072); MSKSEMI C2836386 (7,399, $0.069) | | | | USON-10 | Ext | Footprint-compatible with the TI part, specs not read: unverified |

Note: a 5.5 V standoff part on the 3.3 V VCC line is fine, but the VCC line can also be hit by the cable, so keep the TVS right at the connector pins with a short ground return.

### 4. Connector parts per Stage 1 option

| Option | Part | LCSC | Stock | Price qty 1 | Package | Class |
|---|---|---|---|---|---|---|
| (a)/(c)/(e) board header, SMD side entry (recommended) | JST S4B-PH-SM4-TB(LF)(SN) | C265102 | 19,414 | $0.309 | SMD 2.0 mm, right angle | Ext |
| same, top entry SMD | JST B4B-PH-SM4-TB(LF)(SN) | C160354 | 36,802 | $0.272 | SMD 2.0 mm | Ext |
| same, cheaper SMD clone | FG PH-4AWT | C2763695 | 6,195 | $0.068 | SMD 2.0 mm right angle | Ext (pin pattern needs checking against JST footprint: unverified) |
| same, THT side entry | JST S4B-PH-K-S(LF)(SN) | C157926 | 34,678 | $0.070 | THT 2.0 mm | Ext (THT is a hand or extra-cost assembly step: unverified) |
| same, THT top entry | JST B4B-PH-K-S(LF)(SN) | C131334 | 178,553 | $0.046 | THT 2.0 mm | Ext |
| (c) mating housing, 4 way | JST PHR-4 | C111514 | 71,742 | $0.0167 | | Ext |
| (c) crimp contact (need 4 per cable) | JST SPH-002T-P0.5S | C111515 | 1,736,788 | $0.0086 | | Ext |
| (b) pluggable terminal header, 3.5 mm 4P right angle | Kefa KF2EDGR-3.5-4P | C441173 | 12,732 | $0.110 | 3.5 mm pitch | Ext |
| (b) alt | SH2EDGRC-3.5-04P (Shou Han) | C54876645 | 1,295 | $0.205 | 3.5 mm pitch | Ext |
| (d) panel-mount waterproof (M8/M12/GX12 4 pin) | not on JLCPCB | | | | | source elsewhere, not priced |

## Cost per board (qty 1 board; recommended set)

| Part | Price |
|---|---|
| TPS63802DLAR C2845237 | $0.908 |
| L1 DFE201612E-R47M C668312 | $0.172 |
| Cin C19702 | $0.027 |
| Cout 22 uF 0805 C5674 | $0.044 |
| R1 + R2 | $0.004 |
| 2 x SN74LVC1T45DBVR (option B) | $0.167 |
| TPD4E05U06DQAR C138714 | $0.083 |
| JST S4B-PH-SM4-TB C265102 | $0.309 |
| Total | about $1.72 (option A translator instead: +$0.69, about $2.41) |

Unique extended parts (each carries the JLCPCB extended setup fee): TPS63802, inductor, 511 k, 91 k, translator (1 or 1), TVS, PH header, Cout 0805 = 8 extended lines; Cin on the basic list. Fewer lines if the 0603 basic caps are used for Cout.

## Unverified summary
- Sensor cable length, wire colours, plug pin order, whether the PH plug is fitted to the cable, TX idle level, startup time to first frame, peak current, error-frame codes: not found in any DFRobot text. Get from the physical sample.
- Connector dimensions in the options table: typical figures, not read from drawings.
- TPS63900 load disconnect in shutdown and its exact 3.3 V resistor set; Isat of the Murata 0.47 uH part; Murata 1.5 uH suitability for TPS63031; SRV05-4 and clone TVS specs.
- Panel-mount waterproof connector part and price.
- JLCPCB stock changes daily: recheck before ordering.
- Not committed to git: the file lives in the shared folder, outside the repo.
