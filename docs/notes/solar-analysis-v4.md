# Solar Harvester Analysis — nrf54l15 v3/v4 (AEM10330 + PowerFilm indoor panels)

**Scope:** the AEM10330 solar block (`power_supply.kicad_sch`) checked against **DS-AEM10330 v1.5**, the expected harvest from PowerFilm indoor panels, a review of other PowerFilm panels, and bench results from the v3 board.
**Revision:** 2026-10-08 (rev 2). Updated after the EN_SLEEP fix, bench validation on v3, and schematic fixes applied to v4.

---

## 1. Status summary

| # | Item | v3 board (built) | v4 schematic | Status |
|---|---|---|---|---|
| 1 | **EN_SLEEP (pin 39) tied to LOAD.** The AEM slept as soon as V_BAT > 3.50 V and stopped harvesting (DS §5.3.4). | ✅ Reworked: bottom-side trace cut, pin 39 bridged to GND (§7.1) | ✅ Pin 39 → **GND** | **Fixed, and confirmed on the bench** (§7.2) |
| 2 | **MPPT ratio 80 %** (R_MPP = HLL). That loses ~15 % at 200 lux on these amorphous-silicon (a-Si) panels. | Left at 80 %. It works (ratio measured at 0.80–0.86) | ✅ Changed to **70 %** (LHL): pin 11 → GND, pin 12 → VINT | Fixed on v4 |
| 3 | No MPN fields on C40–C43 | — | ✅ Added (§3.3) | Fixed on v4 |
| 4 | C41 / C42 / C43 effective capacitance under DC bias is close to the datasheet minimums | — | Open | **Verify** against the vendor DC-bias curves |
| 5 | L11 (Murata DFE252010F-100M) sits on a Sunlord SWPA252010S land pattern | Built that way and works | Open | **Verify** against Murata's recommended land before the v4 Gerbers. The LCSC field C701155 was already checked in `solar-block-review-v3.md`. |
| 6 | Panel LL200-2.4-75 #1 | Left cell shunted (§7.3) | — | **Replace**. Use solder and strain-relief practice from §6.4. |
| 7 | Board draw on battery is ~1.9 mA, but solar supplies ~0.1 mA indoors | Measured (§7.5) | — | **Firmware**: put the nRF54L15 to sleep, then re-measure |
| 8 | PCB layout checks from DS §10 | Done in `solar-block-review-v3.md` | Not yet checked | Re-check after Update PCB on v4 (§3.5) |

**Bottom line:** the harvester works. With EN_SLEEP fixed, the v3 board holds the panel at the MPPT setpoint and delivers **~0.1 mA into the system at ~450 lux** with an LL200-3.6-75, matching the model (§5). Today the limit is the board's own ~1.9 mA draw, not the solar path.

> **v4 schematic was edited on disk** (`power_supply.kicad_sch`; backup `power_supply.kicad_sch.claude_bak3`). If the sheet is open in KiCad, use **File → Revert**. Then run **Update PCB from Schematic**. Pins 11, 12 and 39 change nets, so any copper already routed to them on the v4 board must be rerouted.

---

## 2. Circuit — v4 schematic after fixes

```
U5 (JST-PH S2B)  pin1 ──SOLAR_5p5V──┬── IC1.3  SRC
                 pin2 ── GND        └── IC1.1  CS_IN
IC1.7  BUFSRC ── C40 22 µF 0603 ── GND
IC1.8  LIN ─┬─ L11 10 µH DFE252010F-100M
IC1.9  LOUT ┘
IC1.13 VINT  ── C41 10 µF 0402 ── GND     (VINT also → 12, 29, 30)
IC1.17 LOAD  ── C42 47 µF 0603 ── GND     (LOAD also → 20)
IC1.19 STO   ── VBAT ── C43 220 µF 1206 ── GND → battery / nPM1300
GND: 4,5,6,10,11,14,15,16,18,24–28,31–35,39,41(EP)
NC:  2 ZMPP, 21–23 custom-threshold pins, 36/37/38/40 status outputs
```

Verified from the saved v4 netlist after the edit.

| Function | Pins → tie | Code | Meaning | Changed? |
|---|---|---|---|---|
| R_MPP[2:0] | 11=GND, 12=VINT, 15=GND | LHL | V_MPP = **70 %** V_oc | **Yes** (was 80 %) |
| T_MPP[1:0] | 32=GND, 30=VINT | LH | 70.8 ms sample / 4.5 s | — |
| STO_CFG[3:0] | 27,35,34,33 = GND | LLLL | Li-Po 3.00 / 3.50 / 4.05 V | — |
| LOAD_CFG[1:0] | 25, 24 = GND | LL | 3.28 V (unused rail) | — |
| STO_PRIO | 29 = VINT | H | storage charged first at start-up | — |
| EN_HP | 28 = GND | L | low-power mode | — |
| EN_STO_FT | 31 = GND | L | no feed-through | — |
| EN_STO_CH | 20 = LOAD | H | charging enabled | — |
| **EN_SLEEP** | **39 = GND** | **L** | **sleep disabled; converter always available** | **Yes** (was LOAD) |
| BAL | 18 = GND | — | single cell | — |

---

## 3. Datasheet requirement checklist

### 3.1 Pins and wiring — all ✅

| Requirement (DS v1.5) | Ref | As built |
|---|---|---|
| CS_IN tied to SRC for self cold start | §5.2 | Pins 1 + 3 on SOLAR_5p5V ✅ |
| ZMPP floating if not used | Tbl 1 | NC ✅ |
| BAL to GND if not used | Tbl 1, §5.5 | GND ✅ |
| STO never floating; ≥100 µF or battery | Tbl 1 | Battery + 220 µF ✅ |
| GND pins 4, 5, 6, 10, 14, 16, 26 + EP | Tbl 2 | ✅ |
| STO_OVCH / STO_RDY / STO_OVDIS floating unless custom mode | Tbl 2 | NC ✅ |
| Status outputs may be left open | Tbl 2 | NC ✅ |

### 3.2 Logic-level domains — ✅

| Pins | HIGH = | Abs max | As built |
|---|---|---|---|
| R_MPP, T_MPP, LOAD_CFG, STO_CFG, STO_PRIO, EN_STO_FT, EN_HP | VINT (2.2 V) | 2.75 V | Highs on 12, 29, 30 → VINT; none on LOAD ✅ |
| EN_SLEEP, EN_STO_CH | LOAD | 5.5 V | 39 = GND, 20 = LOAD ✅ |

### 3.3 External components

| Part | Requirement | v4 now | Status |
|---|---|---|---|
| L11 | 10 µH, ≥1 A peak, ≥10 MHz | Murata DFE252010F-100M=P2 (Isat 1.3 A min), LCSC C701155 | ✅ part. 🟡 Land pattern still to check against Murata. |
| C40 C_SRC | 22 µF typ, ≥13 µF effective | 22 µF 0603, **MPN GRM188R61A226ME15** (DS Tbl 13) | ✅. BUFSRC sits at only ~2–3 V, so derating is mild. |
| C41 C_INT | 10 µF typ, ≥5 µF effective | 10 µF 0402, **MPN GRM155R60J106ME15** (DS Tbl 13) | 🟡 Thin margin at 2.2 V in 0402. Consider 0603. VINT has measured a steady 2.175 V on v3, so it works in practice. |
| C42 C_LOAD | 47 µF typ, ≥13 µF effective | 47 µF 0603, **MPN GRM188R60J476ME15** (DS Tbl 13) | 🟡 Check derating at 3.28 V |
| C43 C_STO | ≥100 µF, mandatory with a removable battery; ≥6.3 V | 220 µF 1206, **MPN Taiyo Yuden MSASJ31LBB5227MTCA01** (in-stock drop-in, see `aem10330-as-wired.md`) | ✅ |

DS Table 7, footnote 1: capacitor minimums apply *after* DC-bias derating and tolerance.

### 3.4 Operating limits

| Limit | Value | LL200-2.4-75 | LL200-3.6-75 |
|---|---|---|---|
| V_SRC operating | 0.1–4.5 V | max V_oc 3.7 V ✅ | avg V_oc ≤ 4.0 V indoors ✅; **max V_oc 5.5 V in sun ⚠** |
| Abs max SRC | 5.5 V | ✅ | at the limit in direct sun ⚠ |
| Cold start | 275 mV and 3–6 µW | ✅ (a few lux) | ✅ |
| Storage | Li-Po preset: 3.00 / 3.50 / 4.05 V | ✅. USB through the nPM1300 still charges to 4.20 V. Above 4.05 V the AEM stops charging. | |

### 3.5 Layout (DS §10) — check on v4 after Update PCB
- [ ] LIN/LOUT short and wide; no copper under L11 on inner or bottom layers (done on v3)
- [ ] C40/C42/C43 close to the IC with a direct GND return to the EP
- [ ] C41 close to pin 13 and to GND (v3: 1.53 mm, 0 vias)
- [ ] EP via array present. Don't run "Update Footprints from Library" on IC1, or the vias are lost.
- [ ] Widen the STO stub (0.15 mm on v3) to 0.4–0.5 mm
- [ ] Route the new nets for pins 11, 12 and 39

---

## 4. Findings in detail

### 4.1 EN_SLEEP — ✅ fixed

The datasheet's sleep conditions are: EN_SLEEP = H, V_VINT > 2.2 V and V_LOAD > V_LOAD,TYP. In sleep, *"the DCDC is disabled, no energy is harvested from SRC … the storage element … is no longer charged"* (DS §5.3.4). With LOAD unloaded, the AEM entered sleep as soon as it left START STATE (V_BAT > 3.50 V), so solar only ever charged the bottom few percent of the cell. Sleep is meant to be driven by firmware. DS Fig. 19 ties it to GND.

- **Fix:** pin 39 → GND (v3 rework, v4 schematic).
- **Cost:** about +0.45 µA quiescent current (DS Fig. 8).
- **Result:** confirmed on the bench. See §7.2.

### 4.2 MPPT ratio — ✅ 70 % on v4

V_mp / V_oc from the PowerFilm data: LL200-2.4-75 is 0.67 at 200 lux and 0.78 at 1000 lux; LL200-3.6-75 is 0.67 and 0.80. I fitted a single-diode model to each panel's published points and computed the fraction of maximum power captured at each R_MPP setting:

| Setting | 2.4-75 @200 | 2.4-75 @1000 | 3.6-75 @200 | 3.6-75 @1000 |
|---|---|---|---|---|
| **70 %** | **99 %** | **97 %** | **99 %** | **94 %** |
| 75 % | 94 % | 99.5 % | 94 % | 98 % |
| 80 % (v3) | 84 % | 99.6 % | 85 % | 100 % |

70 % is the best all-round setting for indoor light on either panel. Use 75 % (LHH: pin 15 → VINT as well) only if the deployment sits consistently above ~500 lux. Treat the model figures as ±3–5 %.

**T_MPP:** keep LH (70.8 ms every 4.5 s, 1.6 % overhead). If V_oc sampling under-reads in very dim light, HL (280 ms every 17.9 s) has the same overhead with a 4× longer settling window.

### 4.3 Capacitor derating — 🟡 verify
C41 (10 µF 0402 at 2.2 V) has the thinnest margin, although VINT is stable on v3. C42 (47 µF 0603 at 3.28 V) should be checked. C43 (220 µF at about 4 V) is the datasheet's own choice for that bias. Use Murata SimSurfing / Taiyo Yuden curves for the exact MPNs.

### 4.4 Inductor land — 🟡 verify
Same 2.5 × 2.0 × 1.0 mm body class. The v3 board, built on this land, works. Confirm it against Murata's drawing before the v4 Gerbers.

### 4.5 Optional, not applied
1. **Status pins to the nRF:** they swing to V_LOAD = 3.28–3.34 V, above the nRF's VDD + 0.3 V. If you route them, first set LOAD_CFG = LH (2.50 V) by moving pin 24 to VINT.
2. **Solar to 4.15–4.2 V:** possible with custom mode (STO_CFG = LHHH plus four resistors). Not worth it at these currents.
3. **ESD on the panel input:** a TVS with sub-µA leakage at 4 V, if you add one.
4. **Reverse polarity:** keyed JST, so no series diode. Mark cable polarity.
5. **Net name:** `SOLAR_5p5V` → `SOLAR_IN` (cosmetic).

---

## 5. Expected harvest

Model method: power law between the PowerFilm 200 / 1000 lux points; MPPT capture from §4.2; DC-DC efficiency from DS Fig. 3 (low-power mode, V_STO 3.6–4.1 V); net of 0.875 µA AEM quiescent current; cell at 3.8 V. Points outside 200–1000 lux are extrapolated (±30 %).

### 5.1 LL200-2.4-75 (healthy panel), 70 % setting

| Light | Panel P_mp | Into battery | Net current |
|---|---|---|---|
| 100 lux | 129 µW | 99 µW | ~25 µA |
| **200 lux** | 289 µW | 226 µW | **~59 µA** |
| 500 lux | 844 µW | 664 µW | ~174 µA |
| **1000 lux** | 1.90 mW | 1.50 mW | **~390 µA** |

### 5.2 LL200-3.6-75, 70 % setting

| Light | Panel P_mp | Into battery (η ≈ 0.85) | Net current |
|---|---|---|---|
| 200 lux | 206 µW | ~173 µW | ~45 µA |
| ~450 lux | ~530 µW | ~0.42 mW | ~110 µA |
| 1000 lux | 1.35 mW | ~1.1 mW | ~300 µA |

**Measured on v3** (80 % setting, ~450 lux, LL200-3.6-75 with V_oc ~15 % below typical): **~0.1 mA** (§7.5). That's consistent with the table.

### 5.3 Daily budget, LL200-2.4-75, 70 %

| Average lit level | 8 h/day | 12 h/day |
|---|---|---|
| 100 lux | supports ~8 µA average draw | ~12 µA |
| **200 lux** | ~19 µA | **~29 µA** |
| 500 lux | ~57 µA | ~86 µA |
| 1000 lux | ~130 µA | ~196 µA |

"Supports X µA" means the 24 h average battery-side draw of the whole node at energy break-even. The v3 board currently draws ~1.9 mA, so firmware sleep is the next step to make the node self-sustaining indoors.

---

## 6. Panel selection

### 6.1 PowerFilm indoor series (rated at 200 / 1000 lux)

| Model | Size (mm) | P @1000 lx | Max V_oc | µW/cm² | Fit with AEM10330 |
|---|---|---|---|---|---|
| **LL200-2.4-75** | 94 × 73 | **1.90 mW** | **3.7 V** | **27.7** | ✅ **Best**: highest output, and can never exceed the 4.5 V SRC limit |
| LL200-3.6-75 | 73 × 74 | 1.35 mW | 5.5 V | 25.1 | ⚠ Works indoors (validated on v3). Keep it out of direct sun. |
| LL200-3-37 | 114 × 36.5 | 1.09 mW | 4.6 V | 26.2 | ⚠ ~57 % of the 2.4-75's output |
| INP3.6-12x310 | 310 × 11.9 | 0.98 mW | 5.5 V | 26.7 | ⚠ Strip form factor only |
| LL200-4.8-37 | 94 × 36.5 | 0.87 mW | 7.4 V | 25.4 | ❌ Exceeds AEM abs max |
| LL200-2.4-37, INP2.4/3.6-24x44T/1.2 | small | ≤0.45 mW | — | — | ❌ Too small |

Every indoor model uses the same a-Si technology at ~23–28 µW/cm². The only way to get more energy is more panel area: add **a second LL200-2.4-75 in parallel**. No circuit change is needed.

### 6.2 Classic / WeatherPro
These are rated for sunlight, not indoor light. MP3-37 has max V_oc 4.6 V, which is marginal. The MPT and WeatherPro panels (3.6–15.4 V operating) have V_oc above the AEM range. ❌

### 6.3 Recommendation
Use the **LL200-2.4-75** (new unit), with 70 % MPPT on v4. Add a second one in parallel if the node's average draw or the deployment light needs it.

### 6.4 Panel handling — lessons from panel #1
- Solder quickly onto the exposed foil tab only, and keep the iron away from the laminate and the cell edge. See PowerFilm's handling and soldering guides.
- **Strain relief:** tape or glue both leads to the back of the panel ~1 cm from the joints.
- Before connecting, check open-circuit voltage and short-circuit current, then do the per-cell cover test: covering any one cell should collapse the voltage.
- The standard laminate is rated −25…65 °C and tolerates *intermittent* sun. Don't leave it in direct sun on a dark surface.

---

## 7. Bench results — v3 board

### 7.1 EN_SLEEP rework (2026-10-07)
Traced in `nrf54l15_v3.kicad_pcb`: pin 39 → 1 mm F.Cu stub → via (124.9, 71.0) → a dedicated 0.15 mm B.Cu trace at x = 123.8 → via (128.1, 80.9) → LOAD. That trace carries only EN_SLEEP.

Rework: the B.Cu trace was cut at y ≈ 75.6, and the pin-39 side was bridged to the adjacent B.Cu GND pour (~0.5 mm gap) at y ≈ 74.3. It's reversible. The VINT trace was nicked during the rework and repaired; C41 reads a steady **2.175 V**.

### 7.2 MPPT confirmation
V_BAT 3.78 V (in the charging window). Panel (LL200-2.4-75 #1): V_oc 1.40 V, SRC under load 1.129 V → **ratio 0.806**, matching the 80 % strap. **EN_SLEEP fix confirmed.**

### 7.3 Panel #1 failure — LL200-2.4-75
I_sc 0.42–0.52 mA (normal for the light), but V_oc only 1.40 V (expected ~2.5 V). Cover test: left cell covered → 1.319 V (barely changed); right cell covered → 0.446 V. **The left (negative-side) cell is shunted.** The likely cause is the torn and heat-marked laminate at the negative solder corner. The panel delivers about half its rated power and needs replacing.

### 7.4 LL200-3.6-75 (2026-10-08)
~450 lux (from I_sc 0.26 mA). V_oc 3.244 V, ~15 % under the expected ~3.8 V; the per-cell cover test is still to do. Connected: SRC 2.78 V with periodic jumps to 3.x V during V_oc sampling. **MPPT working.**

### 7.5 Battery current (2026-10-08)
Meter in series with the battery lead, ~450 lux, LL200-3.6-75: **1.8 mA panel uncovered, 1.9 mA covered → solar ≈ 0.1 mA** (meter resolution ±0.05 mA). This matches the model. The board's own draw is ~1.9 mA. (An earlier estimate of the draw from V_BAT decay was invalid, because resistors had been used to discharge the cell during that period.)

### 7.6 Next tests
1. Per-cell cover test on the LL200-3.6-75.
2. Board draw with J3 and any sensor board unplugged.
3. Flash a minimal sleep build, then re-measure with a µA meter or PPK2 on the battery lead. The target is tens of µA or less.
4. With the board asleep, confirm V_BAT rises under ~450 lux.
5. New LL200-2.4-75: verify ~2.5 V V_oc / ~0.5 mA I_sc at ~450 lux, then repeat §7.5.

---

## Sources

- e-peas, *DS-AEM10330 v1.5*: Tables 1, 2, 3, 6, 7, 9–13; §5.2–5.4, §6.9, §10; Figs. 3, 8, 11, 19.
- PowerFilm, *LL200-2.4-75 drawing rev 2*.
- Project docs: `aem10330-as-wired.md`, `solar-block-review-v3.md`.
- [PowerFilm LL200-2.4-75](https://powerfilmsolar.com/products/electronic-component-solar-panels/indoor-light-series/ll200-24-75)
- [PowerFilm Indoor Light Series](https://www.powerfilmsolar.com/products/electronic-component-solar-panels/indoor-light-series)
- [PowerFilm LL200-3.6-75](https://www.powerfilmsolar.com/products/electronic-component-solar-panels/indoor-light-series/ll200-3.6-75)
- [PowerFilm LL200-3-37](https://www.powerfilmsolar.com/products/electronic-component-solar-panels/indoor-light-series/ll200-3-37)
- [PowerFilm LL200-4.8-37](https://www.powerfilmsolar.com/products/electronic-component-solar-panels/indoor-light-series/ll200-4.8-37)
- [PowerFilm INP3.6-12x310](https://www.powerfilmsolar.com/products/electronic-component-solar-panels/indoor-light-series/inp3.6-12x310)
- [PowerFilm Classic Application Series](https://www.powerfilmsolar.com/products/electronic-component-solar-panels/classic-application-series)
- [PowerFilm WeatherPro Series](https://www.powerfilmsolar.com/products/electronic-component-solar-panels/weatherpro-series)
