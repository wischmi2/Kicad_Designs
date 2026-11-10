# Sensor Board — Conductivity / Salinity (CN1 plug-in)

Design outline for a CN1 plug-in board that measures conductivity / salinity / specific gravity in the reef tank.

- **Reference schematic:** MikroE **EZO Carrier Click - Conductivity** (MIKROE-6011). This is a starting point only; the board is not a Click.
- **Host:** Nordic_Solar v4 (nRF54L15 + nPM1300). Connector pinout per `v4-sensor-connector.md`.
- **Status:** outline. Items marked **[verify]** still need a datasheet check, and part numbers marked **[TBD]** are not chosen.

---

## 1. Requirements

| Item | Target |
|---|---|
| Measurement | EC (µS/cm), salinity (PSU, 0–42), specific gravity (seawater, 1.000–1.300) |
| Expected value | Natural seawater ≈ 53 mS/cm / 35 PSU / SG 1.026 |
| Accuracy | ±2 % EC (EZO-EC spec), plus temperature-compensation error |
| Probe | Conductivity probe, K 1.0 class (EZO-EC supports K 0.01–10.2, any brand) |
| Host interface | I²C only, through a digital isolator |
| Power | Off between readings (duty-cycled); must not back-power when off |
| Isolation | Probe domain galvanically isolated from the host (mandatory) |
| Connector | Molex 503480-1400, 14-pin 0.5 mm FFC, same as host |

## 2. Block diagram

```
            HOST SIDE (non-isolated)              ║        ISOLATED SIDE (probe domain)
                                                  ║
CN1.13 VBAT ──► [isolated power stage]  ═══transformer═══►  rectifier ─► LDO ─► V_ISO (≈3.9 V)
                    ▲ EN                          ║                              │
CN1.2 VSENS ────────┤                             ║                              ├─► EZO-EC VCC
            │       └── (EN = VSENS high)         ║                              └─► isolator side 2 VDD
            └──► isolator side 1 VDD              ║
                                                  ║
CN1.3 SDA ◄──► [I²C digital isolator side 1] ═════╬═════ side 2 ◄──► EZO-EC SDA (TX)
CN1.4 SCL ◄──► [                        ]  ═══════╬═════        ◄──► EZO-EC SCL (RX)
                                                  ║
CN1.11 ID ──► R_ID to GND                         ║        EZO-EC PRB1/PRB2 ──► probe connector
CN1.1/12/14 GND ── host GND                       ║        ISO_GND (separate plane)
```

## 3. CN1 signal usage

| Pin | Signal | Used? | How it is used on this board |
|---|---|---|---|
| 1 | GND | **yes** | Host-side ground. Never connected to ISO_GND. |
| 2 | VSENS (3.0 V, switched) | **yes** | (a) Isolator side-1 VDD. (b) EN for the isolated power stage, so firmware turns the whole board on and off through nPM1300 LDSW1. Load on VSENS is only the isolator side 1 plus the EN pin. |
| 3 | SDA | **yes** | I²C data to isolator side 1. **No pull-up on this board**; the host has 4.7 k to VSENS. The isolated side needs its own pull-ups to V_ISO. |
| 4 | SCL | **yes** | I²C clock to isolator side 1. Same pull-up rule as SDA. |
| 5 | SCK | no | NC |
| 6 | MOSI / TX | no* | NC. *Optional test pad (see §6, EZO mode switch). |
| 7 | MISO / RX | no* | NC. *Optional test pad. |
| 8 | CS | no | NC (host pull-up keeps it high). |
| 9 | INT | optional | NC for EZO-EC. If you change to an OEM-EC with an INT output, it needs a third isolated channel (open-drain, active low). |
| 10 | AIN | no | NC. Nothing analog can cross the isolation barrier without extra parts. |
| 11 | ID | **yes** | R_ID 1 % to GND. Proposed: **1 k → type 1 = conductivity** (`V_ID` ≈ 0.27 V). Record the assignment in `v4-sensor-connector.md`. |
| 12 | GND | **yes** | Host GND |
| 13 | VBAT (raw battery) | **yes** | Input to the isolated power stage. This gives headroom over the full LiPo range and keeps the load visible to the nPM1300 fuel gauge. |
| 14 | GND | **yes** | Host GND |
| MP | Mounting tabs | yes | Host GND |

Mode in the host firmware: **I²C only.** UART and SPI stay disabled, so pins 5–8 are free on the host.

## 4. Measurement core — EZO-EC

- **Part:** Atlas Scientific **EZO-EC**, the same module the MikroE carrier uses.
  - Alternative: **EC OEM** (smaller, lower cost, I²C only). Its operating-voltage spec conflicts between the product page and the datasheet for the pH OEM, so check the EC OEM datasheet directly **[verify]**.
- **Supply:** VCC 3.3–5.5 V per the EZO-EC datasheet. Run it from V_ISO ≈ 3.9 V, which matches Atlas's isolation reference.
- **Protocol:** set to I²C mode. Default I²C address **0x64**.
- **Read time:** ~600 ms per EC reading.
- **Outputs to enable:** `EC`, `S` (salinity), `SG`. Disable `TDS` (meaningless for seawater). Command: `O,<param>,<0|1>` **[verify syntax]**.
- **Temperature compensation:** the EZO-EC accepts a temperature value. See §7.
- **Calibration** survives power cycles, stored on the module **[verify]**, so duty-cycling power is fine.

## 5. Isolation

### 5.1 Why it is mandatory
- The probe sits in a tank shared with pH/ORP probes, pumps and heaters. Without isolation, every grounded thing in the tank becomes a current path through the probe, which ruins readings and corrodes electrodes.
- Atlas warns that conductivity readings inject significant electrical interference into the water that affects pH, ORP and DO. Isolation plus sequencing (§8) contains it.

### 5.2 Digital isolator (I²C)
- **Baseline:** Skyworks **Si8400AB** bidirectional I²C isolator, the same part the MikroE carrier uses.
- **Check before committing [verify]:** side-1 minimum VDD must be ≤ 3.0 V (VSENS). Note the part's isolation rating and its idle current.
- **Pull-ups on side 2 only**, to V_ISO. Value per the isolator datasheet; 4.7 k is a typical start.
- If INT is ever needed, choose a 3-channel part (2 bidirectional + 1 unidirectional) **[TBD]**.

### 5.3 Isolated power stage
- **Approach:** push-pull transformer driver → small isolation transformer → rectifier → LDO → V_ISO. This is the topology of the Atlas OEM isolation reference.
- **Driver candidate:** TI **SN6505** family (has an EN pin, wide input range) **[verify input range covers 3.0–4.2 V and EN threshold at 3.0 V logic]**.
- **Transformer:** choose the ratio so that at **minimum VBAT (3.0 V, AEM OVDIS)** the rectified output still exceeds **3.9 V + LDO dropout + diode drop** under full EZO load. **[TBD — calculate once the driver and the EZO peak current are known]**.
- **LDO:** low-noise, output set to ≈ 3.9 V, enable tied high on the isolated side **[TBD]**.
- **Enable:** driver EN ← VSENS (through a series resistor if the EN input needs it). When VSENS is off, the board draws only the driver's shutdown current from VBAT. Confirm that shutdown current is sub-µA **[verify]**.
- **Alternative:** power the stage from VSENS instead of VBAT. This is simpler, but it eats the 100 mA LDSW1 / 200 mA BUCK2 budget shared with the SoC and loses battery headroom. Not recommended.

### 5.4 Back-power check
- With VSENS off, the host sets SDA/SCL to disconnected inputs (per the CN1 rules).
- Confirm the isolator side 1 doesn't back-power through SDA/SCL from the host pull-ups. The pull-ups go to VSENS too, so they also drop to 0 V. This should be clean.

## 6. EZO mode switch (UART → I²C)

The EZO-EC ships in UART mode, and the MikroE carrier uses it in UART. This board is I²C-only, so the module must be switched once. Options:

1. **Bench pre-configuration (simplest).** Before soldering, set I²C mode on a bench adapter using the `I2C,100` command over UART. Address 100 = 0x64 **[verify command]**.
2. **Hardware method.** Atlas documents a pin-strap method for forcing I²C mode at power-up **[verify procedure in the EZO-EC datasheet]**. Add jumper or test pads on the isolated side so a board can be re-forced.
3. Add test pads on EZO TX/RX (isolated side) for a factory reset or recovery with an isolated USB-UART.

**Recommendation:** use 1, and also provide the pads from 3.

## 7. Temperature compensation

EC is strongly temperature-dependent, so the board needs a water temperature. Options, in order of preference:

1. **Firmware-supplied.** The host gets tank temperature from another node (RTD board) or the ReefWatch backend, then writes it to the EZO-EC before each reading (`T,<°C>` **[verify]**). No extra hardware.
2. **EZO-RTD on the same isolated domain.** A sealed PT1000 is electrically isolated from the water, so sharing the EC domain is acceptable. Add a second I²C device behind the same isolator, at a different address. This makes a "salinity + temperature" combo board; consider a different ID value for it.
3. **DS18B20 on CN1 pin 9 (1-Wire, host side).** Only use this if the probe's stainless sheath is confirmed isolated from its GND lead **[verify for the specific probe]**. Otherwise it puts host ground into the water and defeats the isolation.

## 8. Firmware sequence (host)

1. Enable LDSW1 → VSENS = 3.0 V → isolated stage starts → EZO boots. Wait the boot time **[verify ms]**.
2. Probe ID: read AIN2 and confirm board type 1.
3. Write the temperature (`T,xx.x`).
4. Send `R`, wait ~600 ms, then read EC / S / SG.
5. Optional: average N readings.
6. Set SDA/SCL to disconnected inputs, then disable LDSW1.
7. **Coordinate with other probe nodes:** don't take EC readings while a pH/ORP node in the same tank is reading. Use a time slot assigned by the gateway, or a fixed schedule offset.

Duty cycle drives the power budget. Measure the board's on-current and on-time on the bench, then set the reading interval to fit the solar budget (indoor panel ≈ 0.3–1.9 mW).

## 9. Probe & connector

- **Probe:** K 1.0 conductivity probe (Atlas K 1.0 or equivalent).
- **Connector:** match the probe's termination; Atlas probes commonly use BNC **[verify for the chosen probe]**. Alternatively, use a sealed panel connector if the board goes in an enclosure.
- The connector shield and body go to **ISO_GND**, never host GND.

## 10. Calibration

- **Dry calibration**, then **two-point** wet calibration per the EZO-EC datasheet.
- Choose the high point near seawater: for example a ~53,000 µS/cm standard, or a reef-specific 35 ppt calibration fluid **[verify the available standards]**.
- Calibration lives on the EZO module and travels with the board. Recalibrate when changing the probe.

## 11. PCB layout rules

- **Two ground planes:** host GND and ISO_GND, separated by an isolation gap under the isolator and the transformer.
  - No copper crossing the gap on any layer.
  - Keep the gap at or above the isolator's creepage spec **[verify]**.
- **Isolator and transformer straddle the gap.** Keep everything else clearly on one side.
- **EZO-EC and the probe connector** go at the far end of the isolated side, away from the transformer driver's switching node.
- **Probe traces** (PRB1/PRB2): short and symmetric, guarded with ISO_GND. No vias if avoidable.
- **Decoupling:**
  - isolator, both sides,
  - driver input,
  - rectifier output bulk,
  - LDO in/out,
  - EZO VCC. Values per datasheets.
- **FFC connector:** pin 1 at the same end as on every sensor board. Silkscreen the FFC type (same-side or opposite-side contacts).
- **Conformal coat** the isolated side. Salt air plus condensation will leak across the gap otherwise.

## 12. BOM sketch

| Function | Part | Status |
|---|---|---|
| EC circuit | Atlas EZO-EC (or EC OEM) | chosen (EZO) |
| I²C isolator | Skyworks Si8400AB | baseline, **[verify 3.0 V side 1]** |
| Transformer driver | TI SN6505 family | candidate **[verify]** |
| Isolation transformer | — | **[TBD]** |
| Rectifier diodes | Schottky, dual | **[TBD]** |
| ISO LDO (~3.9 V) | low-noise LDO | **[TBD]** |
| Side-2 I²C pull-ups | 2 × 4.7 k | typical |
| ID resistor | 1 k, 1 % | proposed type 1 |
| FFC connector | Molex 503480-1400 | chosen (matches host) |
| Probe connector | BNC or per probe | **[verify]** |

## 13. Open items

1. Confirm Si8400 side-1 operation at 3.0 V and its isolated-side current.
2. Pick the transformer driver, transformer and LDO, and do the ratio calculation at VBAT = 3.0 V.
3. Measure EZO-EC peak and average current, plus boot time → finalize the duty cycle.
4. Settle the temperature-compensation method (§7).
5. Settle the UART→I²C mode-switch procedure (§6).
6. Assign ID type 1 in `v4-sensor-connector.md`.
7. Host open item that affects this board: **VBAT fuse on CN1 pin 13** — this board is the first real VBAT load.

## References

- MikroE EZO Carrier Click - Conductivity (MIKROE-6011): https://www.mikroe.com/ezo-carrier-click-conductivity
- EZO-EC datasheet: https://download.mikroe.com/documents/datasheets/EZO-EC_datasheet.pdf
- pH OEM datasheet, for the isolation reference design: https://atlas-scientific.com/files/pH_oem_datasheet.pdf
- `v4-sensor-connector.md` — CN1 pinout and sensor-board rules
