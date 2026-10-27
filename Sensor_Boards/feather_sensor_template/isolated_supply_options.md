# VDD_ISO supply options for the isolated Atlas boards (review items X2, X5)

- Date: 2026-10-26, kicad-designer (feasibility study only; no schematic or PCB was changed).
- Boards affected: feather_sensor_template (default isolation block), feather_orp, feather_dissolved_oxygen, feather_conductivity, nrf54l15_feather_sens1 (pH).
- Stock and price: from parts-sourcing, `isolated_supply_parts.md` in this folder (commit ed75049). This note adds the electrical check only.
- Unverified numbers are marked **[unverified]**. Everything else is from a datasheet opened today (see Sources).

## 1. Short answer

1. **Recommended: option (c'), an SN6505B push-pull stage fed from VSENS, with a 3.3 V LDO on the isolated side.** It replaces U4 in the same place. Also swap U3 to a **TI ISO1640BDR with the host on side 2**.
   - VDD_ISO is regulated (3.3 V ±2 %) over the whole battery range.
   - VSENS draw at EC load drops from about 98 mA today to about 65-70 mA.
   - Fallback: if Brian wants to keep VSENS free for other loads, use (c), the same stage fed from VBAT (CN1 pin 13). That needs VSENS raised to 3.3 V in firmware, or a small load switch, because SN6505 EN needs 0.7 x VBAT.
2. **(a), VSENS = 3.3 V in firmware, is not enough on its own.**
   - VDD_ISO at EC load stays at or above 3.0 V only while VBAT is at or above about 3.3 V.
   - The NXE1S0303MC still runs below its 10 % minimum load, and still pulls about 100 mA, which is the LDSW1 limit.
3. **(b), NXE1S0305MC + LDO, fixes the voltage but fails EC on current.**
   - Same footprint and pinout as the NXE1S0303MC (Murata p8).
   - It draws about 115-120 mA from VSENS at EC load, which is more than LDSW1's 100 mA.
   - It is fine for ORP and DO (about 65 mA), but it costs $6.5 per board.
4. **New finding, more urgent than X2 for ORP, DO and pH:** the NXE1 output can roughly **double** below 5 % load (Murata p3, "Minimum Load").
   - ORP, DO and pH load the 303 mA module at about 2-3 %: OEM 2.5-3.5 mA, plus ADuM1250 side 2, plus the pull-ups.
   - So VDD_ISO may sit well above 3.3 V, possibly near 6 V. The Atlas OEM maximum is 5.5 V [ORP/DO datasheet values per the review].
   - **Don't power an Atlas module from the current boards until the U4 output has been measured at about 5 mA load**, or use a preload. Every LDO option below removes this risk.
5. **X5 (isolator logic levels):** the ADuM1250 side-1 VOL (0.6-0.9 V [unverified]) against the nRF VIL (0.3 x VDD = 0.9 V at 3.0 V [unverified today]) leaves no margin under any supply option.
   - The ISO1640's side 2 (VCC2 2.25-5.5 V, VOL2 at most 0.4 V) fixes it if the **host goes on side 2**.
   - The parts-sourcing reading is correct; it was checked today on ISO164x datasheet pages 8 and 14.
6. **SMA J1:** the thread tip is **7.1 mm past the x = 90 edge**. The courtyard is 7.6 mm, and ORP's 5.6 mm is wrong. The body is **9.5 mm tall** above the PCB, not 6.5-8 mm. See section 7.

## 2. Inputs used

| Item | Value | Source |
| --- | --- | --- |
| Feather VDDIO | nPM1300 BUCK2 (VOUT2, VSET2 = R10 150k, 3.0 V today). Feeds nRF54L15 VDD (5 pins), LSIN1, pull-ups and J3 | feather netlist (kicad-cli export today) |
| VSENS | nPM1300 LSOUT1 (U2.29), from LSIN1 = VDDIO | feather netlist |
| BUCK | 200 mA, VOUT accuracy ±5 %, dropout 100 mV at 1 mA, VSYS min 2.7 V to enable. Output range 1.0-3.3 V [unverified, not on the fetched page] | Nordic nPM1300 PS, BUCK electrical spec |
| LOADSW | 100 mA (LSOUT >= 1.2 V), RDSON 200 mΩ at LSIN 3.3 V, soft start 1.8 ms at a 25 mA limit, 2 kΩ active pull-down, Iq 60 nA | Nordic nPM1300 PS, LOADSW electrical spec |
| VBAT | 3.0-4.2 V, CN1 pin 13, unused on the sensor boards today | task, template PCB (CN1.13 = VBAT) |
| Atlas loads | EC 10.6-26 mA, ORP about 3.5 mA, DO about 2.5 mA. VCC minimum 3.0 V on all three | review X2 |
| Isolator side load | ADuM1250 IDD2 about 2-3 mA [unverified]. ISO1640 ICC1/ICC2 3.5-9 mA max depending on bus state (ISO164x p15). Pull-ups 4.7k = 0.7 mA each at 3.3 V | |
| Total isolated load used below | EC 30 mA. ORP/DO 8 mA | sum, rounded up |
| FFC + contacts | 1 VSENS conductor, assumed 0.15 Ω incl. 2 contacts; GND has 3 conductors | [assumption: 0.5 mm FFC, about 60 mm] |

## 3. NXE1 numbers (Murata KDC_NXE1.F02)

| | NXE1S0303MC | NXE1S0305MC |
| --- | --- | --- |
| Input | 2.97 / 3.3 / 3.63 V (min/typ/max), abs max 5.5 V | same |
| Output, rated current | 3.3 V, 303 mA | 5 V, 200 mA |
| Tolerance envelope at 10 % load (nominal Vin) | +5.5 % / -1.5 % | +9.2 % / +3.9 % |
| Tolerance envelope at 100 % load | -5.4 % / -13.4 % | +0.3 % / -5.8 % |
| Line regulation | 1.1 typ, 1.2 max %/% | same |
| Minimum load | 10 %. Below 5 % "may rise to typically double the specified output voltage" | same |
| Max output capacitance | 10 µF recommended (starts into 47 µF) | same |
| Efficiency at 10 % load | about 31 % (curve, p6) | about 30 % (curve, p6) |
| Implied fixed loss | about 0.2 W, so about 60-65 mA input at near-zero load (derived from the curve, not a datasheet number) | same |
| Pinout | 1 -Vin, 3 +Vin, 7 -Vout, 8 +Vout, 14 NA | identical (one table for the whole series, p8) |
| Package | 12.70 x 10.41 mm, height 4.36 ±0.35 mm, same land pattern for both variants (pad length 1.37 mm; only the 0505 differs) | identical |
| Isolation | 3 kVDC 1 s. UL 60950 125 Vrms reinforced, 250 Vrms basic. Creepage 2.5 mm, clearance 2 mm | same |

**The fixed loss drives everything.** At EC load the NXE1S0303MC delivers about 0.1 W (about 10 % load) at about 31 % efficiency. That is about 0.32 W in, so **about 98 mA from VSENS today**: LDSW1 is at its 100 mA limit already.

## 4. The options

### (a) BUCK2 / VSENS = 3.3 V (firmware), U4 unchanged

Model at EC load (30 mA out):
- BUCK2 current about 110 mA (nRF about 10 mA + VSENS about 98 mA).
- VSYS = VBAT - 0.05 V [assumed BATFET drop, unverified].
- BUCK2 in dropout gives VDDIO = VSYS - 0.6 Ω x 110 mA [high-side switch + L10 DCR assumed 0.6 Ω, unverified].
- LDSW1 drop is 0.2 Ω x 0.1 A = 20 mV; FFC drop about 20 mV.
- U4 output = 3.3 V x (1 - 1.5 % ... 1 + 5.5 %) x (1 - (1.1 ... 1.2) x input deficit %).

| VBAT | VDDIO | U4 in | VDD_ISO at EC load (min-max) | Atlas >= 3.0 V? |
| --- | --- | --- | --- | --- |
| 3.4-4.2 V | 3.30 | 3.26 | 3.20-3.44 | yes |
| 3.3 V | 3.18 | 3.14 | 3.06-3.30 | yes, just |
| 3.2 V | 3.08 | 3.04 | 2.94-3.18 | no (worst case) |
| 3.0 V | 2.88 | 2.84 | 2.71-2.95 | no |
| Today, VSENS 3.0 V, any VBAT >= 3.1 V | 3.00 | 2.96 | 2.85-3.09 | no (worst case) |

- The BUCK ±5 % accuracy is on top of this: a -5 % part at the 3.3 V setting gives 2.98-3.20 V even at full battery.
- A LiPo spends roughly the last 5-10 % of its capacity below 3.3 V, so firmware could skip EC readings below VBAT 3.35 V.
- Light load (ORP/DO/pH) is not fixed: at about 2.5 % load the output may rise toward 6.6 V.
- VSENS current is unchanged (about 98 mA at EC). nRF54L15 VDD at 3.3 V is fine (max 3.6 V [unverified]).
- Firmware: write BUCK2 to 3.3 V over TWI at boot, before enabling LDSW1. Or change R10 VSET2 on the feather (value from the nPM1300 VSET table [unverified]).
- U3 side 1 at 3.3 V: ADuM1250 VDD1 >= 3.0 V holds only while VDDIO holds. X5 margin 0.99 V VIL against 0.9 V VOL max, and it disappears as VBAT drops. **The isolator still needs the ISO1640.**

### (b) NXE1S0305MC + 3.3 V LDO on the isolated side, VSENS 3.0 V

- **Fit:** U4 is a drop-in, with the same footprint and pinout.
- **Output at EC load** (about 135 mW, about 13 % load):
  - The envelope interpolates to +3.6 ... +8.9 %, so 5.18-5.45 V at 3.3 V in.
  - At U4 in = 2.95 V (10.6 % low, x 0.873-0.883) that gives **4.5-4.8 V**.
- **LDO headroom:** the LDO needs 3.3 V + 0.15-0.23 V (LP2985 dropout at 50 mA, 25 °C / full temp), so it has about 1 V of margin.
  - A 3.9 V output also works: 4.13 V needed, about 0.4 V margin.
- **At ORP/DO load** the module may rise to about 10 V.
  - The LDO input must be rated 12 V or more: LP2985 16 V or NCP718 24 V. **Not** the NCP186 (5.5 V).
  - LDO dissipation is at most (10 - 3.3) V x 8 mA = 54 mW.
- **VSENS current:**
  - EC: 0.135 W / 0.38 = 0.36 W, so **about 115-120 mA. Over LDSW1's 100 mA. Fails.**
  - ORP/DO: about 0.2 W, so about 65-70 mA. OK.
- **Capacitive load:** keep the NXE1 output cap at 4.7 µF or less (Murata max 10 µF). Atlas E2's 0.1 + 10 + 10 + 0.1 µF goes after the LDO, where the NXE1 does not see it.
- **U3 side 1** stays at VSENS 3.0 V (ADuM1250 VDD1 min 3.0 V [unverified]), so X5 is not fixed. Needs the ISO1640, host on side 2.

### (c) SN6505B + transformer + BAT54C + LDO, fed from VBAT, EN from VSENS

**Driver (TI SLLSEP9I).**
- VCC 2.25-5.5 V; UVLO 2.25 V rising, 1.7 V falling.
- RON 0.31 Ω max at 2.8 V / 1 A; 1 A switch current; 1.7 A current limit.
- fSW 363-517 kHz.
- IDIS 0.1 µA (EN = 0); D1/D2 leakage 0.1 µA.
- EN high = **0.7 x VCC**; EN has an internal pull-down.

**Transformer: JASN CM0601S (C5352974)** (datasheet Rev A/0).
- 1:1:2.22:2.22 ±3 %, centre-tapped primary and secondary.
- OCL 50 µH ±25 %, leakage 1 µH max.
- DCR: primary 0.22 Ω, secondary 0.45 Ω.
- Hi-pot 3000 VDC 2 s.
- **Operating temperature 0 to +70 °C.**
- Body 7.6 x 6.7 mm, 9.45 mm over the leads, **5.25 mm tall**.
- **No V·t rating is given.**
  - The SN6505B needs at least 4.62 V / (2 x 363 kHz) = 6.4 V·µs at VBAT 4.2 V (TI eq. 3).
  - Magnetising current at that worst case is 4.62 V x 1.38 µs / 37.5 µH = 0.17 A, which is comfortable.
  - Saturation is unknown, so bench-check it.
- Documented second source: Würth 760390015 (TI table 9-3: 1:2.1, 11 V·µs, 2500 Vrms, 6.73 x 10.05 x 4.19 mm, LDO type), 0 at JLC.
- **Würth 750315371 is 1:1.1** (TI table 9-3, "no LDO" type), so it can't feed an LDO. Ignore it.

**Ratio check at VBAT = 3.0 V, 30 mA** (TI eq. 5-10).
- Primary current is about 2.22 x 30 / 0.9 = 75 mA.
- VP = 3.0 - 0.075 x (0.31 + 0.22) = 2.96 V.
- VS = 2.96 x 2.22 x 0.97 = 6.37 V.
- Minus BAT54C VF (0.5 V max at 30 mA, Nexperia table 7) and the secondary DCR, the **LDO gets about 5.85 V**.
- The 3.3 V LDO needs about 3.5 V; a 3.9 V LDO needs about 4.1 V. Large margin, and it works down to the 2.25 V UVLO.

**At VBAT = 4.2 V.**
- No-load secondary is 4.2 x 2.22 x 1.03 = **9.6 V**, so the LDO must be rated 12 V or more. The LP2985-33 is rated 16 V.
- LDO dissipation at EC load: (8.9 - 3.3) V x 30 mA = 0.17 W; with θJA 206 °C/W that is about a 35 °C rise. Acceptable. For 3.9 V out: 0.15 W.
- VBAT current at EC load is about 70 mA (about 0.29 W). At ORP/DO it is about 20 mA.

**EN problem.**
- At VBAT 4.2 V, EN needs 2.94 V or more. VSENS is 3.0 V nominal and can be 2.85 V (BUCK -5 %), so **EN is not guaranteed**.
- Fix 1: raise VSENS to 3.3 V, as in (a). The worst case is then 3.135 V, which is above 2.94 V. At low VBAT, VSENS tracks VBAT, so 0.7 x VBAT is always met.
- Fix 2: add a load switch from VBAT controlled by VSENS (adds a part; not selected or verified).

**Off current:** less than 1 µA from VBAT (SN6505 IDIS + D1/D2 leakage 0.1 µA typ each). LDSW1 still switches VSENS.

**VSENS draw:** EN (10-20 µA), the isolator host side (3.5-9 mA max) and the pull-ups. LDSW1 is no longer loaded by the sensor supply.

**Risk:** VBAT (unfused, battery-direct) then runs through the FFC into a wet enclosure, and it is live whenever the battery is in. Consider a series 0R/PTC position at CN1.13.

### (c') the same SN6505B stage fed from VSENS (EN tied to VCC), recommended

- **Electrical:**
  - At VSENS 2.85-3.0 V: VP about 2.8-2.96 V, LDO input about 5.5-5.85 V at EC load, so the 3.3 V LDO is regulated.
  - No-load maximum: 3.0 x 1.05 x 2.22 x 1.03 = 7.2 V (LP2985 16 V).
  - LDO dissipation is at most (5.9 - 3.3) V x 30 mA = 80 mW.
- **VSENS current at EC load:** about 6.0 V x 30 mA / 0.9 / 3.0 V = **about 65-70 mA**, against about 98 mA today and the 100 mA LDSW1 limit.
  - At ORP/DO load it is about 20 mA.
  - BUCK2 total is about 80 mA against its 200 mA rating.
- **No VBAT on the sensor board, no EN level problem, and no firmware change.** Off current is 0 (LDSW1 off, 2 kΩ pull-down).
- **Cost:** it uses the shared BUCK2 budget, which the conductivity plan §5.3 called "not recommended". The numbers above show that it fits with about 30 % margin on LDSW1.
- **Noise:** about 150 mA primary pulses at about 424 kHz come back over the FFC to VDDIO, the nRF supply. Use 10 µF at the centre tap plus 100 nF at VCC, as TI recommends, and a ferrite-bead position in series with VSENS on the sensor board.

### Comparison table

Area: NXE1 is 12.7 x 10.4 = 132 mm². The (c) blocks are: CM0601S 9.45 x 7.6 = 72 mm²; host SOT-23-6 + 2 caps about 20 mm²; isolated SOT-23 + SOT-23-5 + 4 caps about 35 mm².

| | (a) VSENS 3.3 V | (b) NXE1S0305 + LDO | (c) SN6505B from VBAT | (c') SN6505B from VSENS |
| --- | --- | --- | --- | --- |
| VDD_ISO at EC, VBAT 3.0-4.2 V | 2.71-3.44 V, fails below VBAT about 3.3 V | 3.3 V regulated | 3.3 V regulated, down to VBAT 2.25 V | 3.3 V regulated, any VSENS 2.85 V or more |
| Light-load overvoltage (ORP/DO/pH) | not fixed (up to about 2x) | clamped by the LDO | none (LDO) | none (LDO) |
| VSENS current at EC / ORP, DO | about 98 / 65 mA | **about 118 (fails)** / 65 mA | about 5-10 mA (isolator only) | about 68 / 20 mA |
| VBAT current at EC | (via BUCK2) | (via BUCK2) | about 70 mA | (via BUCK2) |
| Off current | 0 | 0 | less than 1 µA from VBAT | 0 |
| Feather change | firmware (BUCK2 3.3 V) | none | VSENS 3.3 V (firmware) or a load switch | none |
| Sensor-board parts | 0 | U4 swap + LDO + 1-2 caps | -U4, +4 ICs, about 6 caps | same as (c), with no VBAT route |
| Area | unchanged | +about 15 mm² (LDO block) | about the same as U4 (about 127 vs 132 mm²) | same as (c) |
| Tallest isolation part | NXE1 4.36 (max 4.71) mm | same | CM0601S 5.25 mm | same |
| Tallest part on the board | SMA J1 9.5 mm | same | same | same |
| Parts cost per board (parts-sourcing, qty 10) | +0 | +1.99 (6.71) | about -3.66 (1.06 total) | same as (c) |
| U3 / X5 | still needs the ISO1640 (host on side 2) | needs the ISO1640 | needs the ISO1640 | needs the ISO1640 |
| Roll-out work | firmware only | small schematic and PCB edit x 5 | template rework, then copy the block x 4 | same as (c), minus the VBAT route |

## 5. Placement (template, applies to ORP/DO/EC)

**Today's footprint.**
- U4 (124, 126.4) rot -90: host pads at x 126.54/129.08, isolated pads at x 121.46; body y 120.55-132.25.
- The antenna-corner keep-out starts at x 132.15, y 126.4.
- The reviewer's free area x 108-116, y 128-132 is clear on all three boards: U2 ends at about x 112.9 / y 125.1, ORP R5 is at (106.6, 128), C3 is at (117.8, 130.4), and H2's keep-out ends at about x 96.

**(b).** U4 stays where it is. Put the LDO (SOT-23-5) plus input and output caps at about x 113-117, y 127-131, between U4.8 (121.46, 131.1) and U2 VCC.
- Split the net: VISO_RAW = U4.8, C3 (4.7 µF max); VDD_ISO = LDO out.

**(c)/(c').** Delete U4 and use its space.
- **CM0601S straddles the barrier:** pin rows 8.5 mm apart along x, e.g. rows at x 119.75 and 128.25, so the 1.91 mm pads stay outside the rule area x 122.6-125.4. Creepage pad-to-pad is about 6.6 mm. The body is centred at about (124, 127).
  - Note the CM0601S pin numbering: pins 1/3/2 are primary (3 = CT), pins 5/6/4 are secondary (6 = CT).
- **SN6505B + 10 µF CT cap + 100 nF** on the host side at about x 126-131, y 122-126, clear of the keep-out.
  - For (c), VBAT comes from CN1.13 (137.15, 118.68) on In2.
  - For (c'), VSENS is already routed there for U4.3.
- **BAT54C + 4.7-10 µF rectifier cap + LDO + 10 µF + 10 µF + 100 nF** on the isolated side at about x 113-120, y 124-132, reusing the C3 position.
  - The LDO out-caps are where Atlas E2 is satisfied; there is no NXE1 10 µF limit any more.
- **Height:** 5.25 mm against the NXE1's 4.71 mm max. Not the tallest part, because the SMA is 9.5 mm.
- **sens1:** different layout (it predates the template), so a hand rework of its isolation corner.

**U3 to ISO1640BDR (C5122339).**
- Same SOIC-8 and the same pin functions as the ADuM1250, in the same order: 1 VCC1, 2 SDA1, 3 SCL1, 4 GND1 | 5 GND2, 6 SCL2, 7 SDA2, 8 VCC2 (TI fig. 5-1).
- Today U3 pins 1-4 are on the host side (x 126.475). **Rotate U3 by 180° (rot 0)** so side 2 (pins 5-8) faces the host. Then re-route SDA/SCL/VCC/GND on both sides; the SDA/SCL order flips in y.
- **Side 1 (sensor):**
  - VCC1 needs 3.0 V or more, so it needs a regulated VDD_ISO (options b, c, c').
  - VOL1 0.57-0.71 V at 0.5-3.5 mA; the pull-ups must sink 0.5 mA or more. 4.7k to 3.3 V = 0.70 mA, OK.
  - The Atlas OEM must read 0.71 V as low [OEM VIL unverified; a typical MCU is 0.3 x 3.3 = 0.99 V].
- **Side 2 (host):**
  - VCC2 2.25-5.5 V.
  - VOL2 0.4 V max at 50 mA or less, against the nRF VIL of 0.9 V at 3.0 V: 0.5 V margin.

## 6. Recommendation

1. Template isolation block becomes **SN6505B (C74518) + CM0601S (C5352974) + BAT54C,215 (C37704) + LP2985-33DBVR (C95414)**, fed from VSENS (option c').
   - Use the LP2985-33 (3.3 V). Atlas's 3.9 V reference is not needed: all three OEMs need only 3.0 V or more.
   - If Brian prefers 3.9 V, use NCP718ASNADJT1G (C440035, 24 V in, Iq 4 µA typ, 1.2 V ref, θJA 235 °C/W) with a divider. Dissipation stays under 0.1 W.
2. U3 becomes **ISO1640BDR, host on side 2**.
3. Roll out: template first, then copy the Isolation sheet and the isolation-block layout to ORP, DO and EC (their Isolation sheets are identical to the template, review C3). sens1 is a separate rework.
   - About half a day for the template, then about 1-2 h per board, plus ERC/DRC/STEP each.
4. Bench before fab: measure one SN6505B + CM0601S at VSENS 2.85 and 3.0 V and loads 5 / 30 / 50 mA. Check the LDO input, saturation (primary current shape), the efficiency, and VDDIO ripple at the feather.
5. **Until then, don't connect an Atlas module to an existing NXE1S0303MC board without measuring VDD_ISO at about 5 mA load first** (light-load rise).

## 7. J1 SMA (BWSMA-KWE-Z001, C496551)

From the BAT Wireless drawing (datasheet A01, July-2-2025, p6).
- Body 6 x 6 mm square, centred on the centre pin.
- Barrel 8.5 mm past the body face, so the thread tip is 3 + 8.5 = **11.5 mm** from the centre pin. Overall length 14.5 mm.
- Thread/nut diameter 6.2 mm.
- Pins 3.5 mm long below the seat. Through 1.6 mm that leaves about **1.9 mm below the bottom side**.
- Centre-line height **6.4 mm**; top of the body **9.5 mm** above the PCB.
- PCB pattern: 5 x ⌀1.4 mm holes, the 4 shell pins on a 5.1 mm square (±2.55).

The KiCad footprint SMA_BAT_Wireless_BWSMA-KWE-Z001 matches the drawing.
- F.Fab barrel to local y -11.5, body ±3, pads ±2.55.
- The courtyard runs to -12, which is 0.5 mm of margin and not part of the part.

With J1 at x 94.4, rot 90 (all three boards):
- Body face at x 91.4.
- Thread tip at **x 82.9, 7.1 mm past the x = 90 edge** (about 1.4 mm of the barrel is over the board).
- The 7.6 mm in the DO/EC STATUS is the courtyard. The 5.6 mm in the ORP STATUS is wrong.

Against the enclosure's about 7 mm:
- 7.1 mm is right at the limit, with about ±0.15 mm tolerance.
- J1 can move toward the edge by at most about 0.25 mm: the shell pads (⌀2.2 mm at x 91.85) reach 90.75, against the 0.5 mm edge rule. That gives about 7.35 mm.
- If more thread is needed outside the wall, the wall has to be thinner at the jack, or use an SMA with a longer barrel.
- Tell fusion-enclosure: the stack gap is set by the **9.5 mm** body, not the 6.5-8 mm in the STATUS files.

## 8. Open questions for Brian

1. Option: (c') from VSENS (recommended), (c) from VBAT (needs VSENS 3.3 V or a load switch, and an always-live battery line on the FFC), (b) for ORP/DO only, or (a) as a firmware stop-gap?
2. VDD_ISO 3.3 V (LP2985-33) or Atlas's 3.9 V (NCP718 ADJ)?
3. OK to use the JASN CM0601S, rated 0-70 °C with no V·t or working-voltage rating, after a bench test? Or pay for a Würth 760390015-class part (TI-listed, 2500 Vrms, not stocked at JLC)?
4. OK to swap U3 to ISO1640BDR with the host on side 2 (needs a U3 rotation and re-route on all boards)? While at it, add INT via an ISO7721 (template question about the 3-channel isolator)?
5. Has anyone measured U4's output on sens1 (pH) at real load? If it's well above 3.3 V, the light-load rise is confirmed.
6. Enclosure: is 7.1 mm of SMA thread past the edge enough, given that the 9.5 mm body height sets the stack gap?

## 9. Sources (all opened 2026-10-26)

- Murata NXE1 series datasheet KDC_NXE1.F02 (via LCSC C6943300, NXE1S0305MC-R7; murata.com was down for maintenance). Pages 1 (selection guide, input range, line regulation, abs max), 3 (minimum load, capacitive load), 5 (tolerance envelopes), 6 (efficiency), 8 (package, pinout, footprint).
- TI SN6505A/B datasheet SLLSEP9I (Aug 2023), ti.com. Sections 6.3, 6.5, 8.4.3, 9.2.2 (eqs. 1-11), table 9-3 (p29).
- TI ISO164x datasheet SLLSFC2D (Sep 2021), ti.com. Fig. 5-1 (p3), section 6.3 (p8), section 6.9 (p14), section 6.10 (p15).
- JASN CM0601S datasheet Rev A/0 (via LCSC C5352974).
- TI LP2985 datasheet (via LCSC C95414): 16 V max in; dropout 120/150 mV at 50 mA, 225 mV over temp; θJA 206 °C/W; shutdown 0.01 µA.
- onsemi NCP718 datasheet (via LCSC C440035): 2.5-24 V in, ADJ 1.2 V ref, Iq 4 µA typ, TSOT-23-5 θJA 235 °C/W.
- Nexperia BAT54C datasheet (via LCSC C37704), table 7: VF 0.40 / 0.50 / 0.80 V max at 10 / 30 / 100 mA.
- Nordic nPM1300 PS (docs.nordicsemi.com): BUCK and LOADSW electrical specifications.
- BAT Wireless BWSMA-KWE-Z001 datasheet A01 (via LCSC C496551), p6 mechanical drawing. KiCad 10.0 footprint Connector_Coaxial:SMA_BAT_Wireless_BWSMA-KWE-Z001.
- Feather netlist exported today with kicad-cli from nrf54l15_feather.kicad_sch; template PCB pad positions read with the kicad MCP (read-only).
- **Not reachable (marked [unverified]):**
  - ADuM1250 datasheet: analog.com timed out, and the LCSC copies are placeholders.
  - nRF54L15 GPIO VIL/VOL: the Nordic page renders by script.
  - Atlas OEM VIL.
  - nPM1300 BUCK output range, BATFET drop and the VSET resistor table.
  - MXPP6-3K6250 datasheet.
