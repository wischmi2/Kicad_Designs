# nRF54L15 Soil Moisture — Bring-up Firmware

Freestanding nRF Connect SDK application for the custom nRF54L15 + nPM1300 + SPV1040T board.

## Hardware (verified KiCad netlist 2026-07-16)

See [HW_VERIFY.md](HW_VERIFY.md).

| Signal | Connection |
| --- | --- |
| I2C SCL | P1.03 |
| I2C SDA | P1.04 |
| PMIC INT | P0.00 ← nPM1300 GPIO1 |
| ANT_SEL | P0.01 → FM8625H VCTL |
| MCU VDD / VDDIO / I2C pull-ups | VOUT2 ≈ 3.0 V (same net) |
| RF switch VDD | VOUT1 ≈ 1.8 V |

## SDK

Primary: **NCS v3.3.0** at `c:\ncs\v3.3.0` (installed via `west init` / `west update`; toolchain via nrfutil).

## Build

```powershell
.\scripts\build.ps1
```

Or manually:

```powershell
# BOARD_ROOT is firmware\ (board definitions live in firmware\boards\)
$env:BOARD_ROOT = "C:/Personal-Agents/worktrees/nrf54l15-feather-branch/firmware"
nrfutil sdk-manager toolchain launch --ncs-version=v3.3.0 --chdir c:\ncs\v3.3.0 -- `
  west build -p -b soil_moisture/nrf54l15/cpuapp `
  -d C:\Personal-Agents\worktrees\nrf54l15-feather-branch\firmware\apps\feather_node\build_v330 `
  C:\Personal-Agents\worktrees\nrf54l15-feather-branch\firmware\apps\feather_node
```

Artifact: `build_v330/feather_node/zephyr/zephyr.hex` (sysbuild names the image after the app folder; before the 2026-11-10 reorg it was `soil_moisture_fw`).

## Flash (TC2030 / J-Link)

```powershell
.\scripts\flash.ps1
```

## Logs / charge validation

No UART on this board — use SEGGER RTT.

1. Flash firmware and open RTT.
2. Confirm boot: `ANT_SEL set…`, `PMIC ready…`.
3. Attach battery; connect USB-C — expect `VBUS connected` and charging status / rising SoC.
4. Disconnect USB; illuminate solar panel feeding SPV1040T — expect `VBUS connected` again and charge current while illuminated.

## Feather run 5 firmware

Status: devicetree, Kconfig and code written 2026-10-28, **NOT BUILT**. The build needs NCS v3.3.0 (named by `scripts\build.ps1`), which is not installed: `C:\ncs` has v2.9.0, v2.9.1, v3.0.1, v3.0.2, v3.1.0 and v3.2.3 only, and `nrfutil sdk-manager` is not installed on this PC. Nothing was flashed. Property names were checked by reading the NCS v3.2.3 sources (`zephyr/dts/bindings/regulator/nordic,npm13xx-regulator-common.yaml`, `sensor/nordic,npm13xx-charger-common.yaml`, `nordic,npm1300-charger.yaml`, `drivers/regulator/regulator_npm13xx.c`, `regulator_common.c`); v3.3.0 may differ.

Target: new board `nrf54l15_feather/nrf54l15/cpuapp` in `firmware\boards\nrf54l15_feather\` (was `soil_moisture_fw\boards\others\nrf54l15_feather\` before 2026-11-10; copied from `soil_moisture`; the existing soil_moisture board is untouched and the app still builds for it). Build: `.\scripts\build.ps1 -Board nrf54l15_feather/nrf54l15/cpuapp -BuildDir <dir>`. Feather-only code is `src\feather_run5.c` (compiled when `CONFIG_BOARD_NRF54L15_FEATHER`) and `boards\nrf54l15_feather_nrf54l15_cpuapp.conf` (`CONFIG_ADC=y`).

Pins from the netlist (kicad-cli export of `nrf54l15_feather.kicad_sch`, 2026-10-28): I2C SCL P1.03, SDA P1.04; PMIC_INT P0.00 (U2 GPIO1); ANT_SEL P0.01 (U6.24 -> U7.2 -> ANT_VCTL -> R11.6); SENS_ID P1.06 (U6.7, SAADC AIN2, R19 10k to VSENS); VSENS = U2.29 LSOUT1 (LDSW1, node LDO1); VRF = U2.31 LSOUT2 (LDSW2, node LDO2).

| Item | Where | Setting | Source |
| --- | --- | --- | --- |
| 1 VRF | board dts `LDO2` | `regulator-initial-mode = NPM13XX_LDSW_MODE_LDO`, `regulator-init-microvolt = 2.5 V`, `regulator-always-on`, `startup-delay-us = 1000` | STATUS.md run 5 stage 1 item 2 and stage 2 to-do 4; driver `regulator_common_init` applies mode, then voltage, then enable, then the delay |
| 2 ANT_SEL | board dts `&gpio0` `ant-sel-hog` (output-low), plus the `ant-sel` gpio-leds alias that `main.c` still drives inactive | P0.01 low = VCTL 0 = ANT-RF1 = chip antenna (FM8625H truth table, review report B4 update; U7 is non-inverting). Hog init is POST_KERNEL priority 41, the nPM1300 regulators init at 85/86, so P0.01 is driven before VRF is on | FM8625H v1.2 via the review report; SN74AUP1G34 SCES603K |
| 3 BUCK1 | board dts | no `BUCK1` node at all, so the driver creates no BUCK1 device and nothing can write BUCK1ENASET. VSET1 is grounded via R9 0R (off). BUCK2 (VDDIO) is `always-on` with a 2.9-3.1 V window and no software voltage write | STATUS.md item 3 |
| 4 NTC | `charger` node | `thermistor-ohms = 10000`, `thermistor-beta = 3380` | R8 Murata NCP15XH103F03RC, B25/50 3380 K |
| 5 SENS_ID | `feather_read_sens_id()` + dts `&adc channel@0` | `regulator_enable(VSENS)`, wait 20 ms, SAADC read on AIN2 (gain 1/4, internal ref, 40 us acquisition, 4x oversampling), `regulator_disable(VSENS)`. Rid is estimated as 10k * V / (3.0 V - V); open pin (above 2.9 V) gives 0 | STATUS.md item 7 |
| 6 Currents | `charger` node | charge `current-microamp = 150000` (cap is 300 mA; raise to at most 300000), `vbus-limit-microamp = 300000` (binding range 100-1500 mA in 100 mA steps) | STATUS.md stage 3.4 (0.25 mm VBAT/VBUS sections) |

VRF: always on from boot is the simple safe choice (load about 50-90 uA, U7 0.9 uA). Switching it around TX/RX would save that current (matters on the 20-30 uA solar budget of other boards) but needs the 10 us switch settling and the U7 input handling on every cycle; do that only if the bench shows the current matters. If it is switched, drive P0.01 first and switch VRF off only after the radio is idle.

Needs a bench test:
- VRF: rise time and the real settling of R11 (the 1 ms startup delay is a placeholder, the need is about 10 us after the rail is up); check VRF = 2.5 V on the scope and that VCTL follows ANT_SEL.
- P0.01 between reset and the hog (MCU reset while the PMIC keeps VRF on): U7's input floats for a short time. Fit R20 (1M pull-down, DNP) if the VCTL glitch matters.
- NTC: read the charger's battery temperature with the real R8 and a battery; check the 10k/3380 setting against room temperature.
- Dead-battery USB attach: the nPM1300 default VBUS limit is 100 mA until set; check that the board starts from a dead battery on USB, that the 300 mA VBUS limit holds with 150 mA charge plus the load, and that charging resumes. Also check whether the Rd on CC1/CC2 works with R1/R2 DNP.
- SENS_ID: voltages for 1k, 2.2k, 4.7k, 10k and open; confirm the settle time on a real sensor board.
- LFCLK: X2 is DNP; select the LFCLK source in Kconfig before using BLE.
