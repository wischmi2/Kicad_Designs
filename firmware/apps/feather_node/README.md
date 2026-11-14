# nRF54L15 Feather - Golioth Pouch BLE node

nRF Connect SDK application for the nRF54L15 feather (`nrf54l15_feather/nrf54l15/cpuapp`, board definition in `firmware\boards\nrf54l15_feather\`). Since 2026-11-13 it is a Golioth Pouch `ble_gatt` node, ported from the ReefWatch solar board app (github.com/wischmi2/nrf54l15_solar_pouch @ cebb66a). Before that it was the soil moisture bring-up (nPM1300, fuel gauge, SENS_ID), which is still in the same sources.

**Status 2026-11-13: builds, never run on hardware.** No device was attached, nothing was flashed, erased or reset. Treat every runtime statement below as an expectation to check on the bench.

## What it does

- Boots through MCUboot (sysbuild), loads `/lfs1/credentials/crt.der` and `key.der` from LittleFS (storage partition RRAM `0x174000`, `0x9000`), starts Pouch and advertises as `Feather`.
- Gateway sharing: the gateway-request flag is set for 30 s (`CONFIG_EXAMPLE_ADV_WINDOW_S`), then cleared for 300 s (`CONFIG_EXAMPLE_SYNC_PERIOD_S`), so one gateway can serve several nodes. Advertising restarts after a disconnect. The advertising is still the solar debug path (100-150 ms interval, always advertising); slow it and drop the 10 s heartbeat before battery tests.
- `src\feather_status.c` samples the nPM1300 every 5 s (`CONFIG_FEATHER_STATUS_PERIOD_S`) on its own work queue: battery voltage, current, charger state, VBUS, and the Nordic fuel gauge state of charge. SENS_ID is read about once a minute (VSENS on for 50 ms).
- On every Pouch uplink one JSON object goes to `.s/sensor`:
  `{"vbat_mv":4012,"soc_pct":87,"ibat_ma":-12,"charge":"IDLE","vbus":false,"sens_id_mv":1500,"sens_rid_ohm":100000}`
  `ibat_ma` is negative while discharging, `sens_rid_ohm` 0 means no sensor board (open pin), `soc_pct` and the SENS_ID fields are -1 until the first read or if it failed. No AEM10330 fields (the feather has no harvester IC).
- All three nPM1300 LED pins are set to host mode and cleared at boot (the pin sinks about 5 mA and the latch survives an nRF reset). The feather wires only LED0 (U2.25, LED1 via R14).
- ANT_SEL (P0.01) is held low (chip antenna AE1) by a gpio-hog in the board file. The solar board holds it high; do not copy that.

## Differences to the Pouch ble_gatt example

| Item | Setting |
| --- | --- |
| Logs | SEGGER RTT only, deferred, drop mode, 8 KB up buffer. Shell, console, serial and MCUmgr are off (no UART; the shell 10 ms RTT poll also keeps the CPU out of idle) |
| RTT control block | `_SEGGER_RTT` at `0x20002070` for the 8 KB buffer (from `zephyr.map`; KMU RAM sits at `0x20000000`, auto-search misses it). Check `zephyr.map` again if the buffer size changes |
| Access port | `CONFIG_NRF_APPROTECT_DISABLE` and `CONFIG_NRF_SECURE_APPROTECT_DISABLE`; always program with `ERASE_NONE` |
| LFCLK | internal RC (`CONFIG_CLOCK_CONTROL_NRF_K32SRC_RC`, `CONFIG_NRF_GRTC_TIMER_SOURCE_LFLPRC`), `&lfxo` disabled in the board file (X2 is DNP). In app and MCUboot |
| NFC pins | `&uicr { nfct-pins-as-gpios; }`, `&nfct` disabled (SCL is P1.03). In board file and MCUboot overlay |
| MCUboot | `sysbuild\mcuboot.overlay` starts with `zephyr,code-partition = &boot_partition` (it replaces the MCUboot app.overlay), disables the nPM1300 nodes, I2C bus and ADC (the MCUboot kernel has no multithreading, so the nPM13xx driver does not link), same LFXO/NFC/RC settings. `sysbuild\mcuboot.conf` has `CONFIG_LTO_SINGLE_THREADED=y` (parallel LTO loses its temp objects on Windows; the app image is not built with LTO, so the option is not set there) |
| Signing | MCUboot debug key (CMake warns). Pick a production key before shipping |
| Device name | `Feather` (`CONFIG_BT_DEVICE_NAME`) |

## SDK, build, flash

NCS v3.4.0 in `C:\ncs\pouch-ncs` with golioth/pouch at `32ded9b` (versions, `west list` and toolchain bundle `dcbdc366a1` are in `..\..\README.md`).

```powershell
cd C:\Personal-Agents\worktrees\nrf54l15-feather-branch\firmware\apps\feather_node
.\scripts\build.ps1                           # pristine, output in C:\ncs\pouch-builds\feather_pouch
.\scripts\flash.ps1 -Serial <J-Link serial>   # MCUboot at 0x0, then zephyr.signed.hex, ERASE_NONE
```

Sizes (2026-11-13, pristine build): app 309,668 B RRAM (43.5 % of the 712,560 B slot), 72,280 B RAM (27.6 %); MCUboot 39,024 B (61.5 % of 62 KB), 20,560 B RAM. Warnings in the build: Kconfig `BOOT_MAX_IMG_SECTORS` (MCUboot, also in the upstream example), `NRF_PLATFORM_LUMOS` deprecated (twice), CMake "default MCUboot signing key", `lto-wrapper: serial compilation of 2 LTRANS jobs` (benign). No application warnings. `soil_moisture/nrf54l15/cpuapp` still builds from the same sources (app 303,604 B, 72,040 B RAM, MCUboot 39,256 B / 21,776 B), also never run.

`west flash` does not work on Windows (the pouch runner imports `pty` and `termios`), hence `flash.ps1` calls `nrfutil device program`. Use J-Link V9.82 (V9.36 drops the link when the nRF54L15 sleeps). Do not pass a chip erase and do not use `nrfutil device recover` once credentials are on the chip: both wipe the LittleFS partition. A locked access port is the only reason to recover.

## Credentials (provisioning over SWD)

The running firmware cannot receive files (no UART, no shell, no MCUmgr), so the credential image is built on the PC and programmed into the storage partition:

```powershell
py -3.11 -m pip install littlefs-python==0.19.0       # once
python .\scripts\provision_credentials.py --crt <device>.crt.der --key <device>.key.der --serial <J-Link serial>
```

The script reads the storage partition address and size from the build `zephyr.dts`, builds the LittleFS image (block 4096, read/prog 16, cache 64, lookahead 32, block cycles 512, directory `/credentials`), writes it as Intel hex into a new folder under the system temp directory (never the repo) and **prints** the `nrfutil device erase --pages 0x174000-0x17d000` and `nrfutil device program ... ERASE_NONE` commands. It runs nothing. The hex contains the private key: delete it right after programming (the script prints the command). Certificates and keys are never committed (`.gitignore` covers `*.der`, `*.pem` and credential hex). Convert PEM with `openssl x509 -inform PEM -outform DER` and `openssl pkcs8 -topk8 -nocrypt -inform PEM -outform DER`.

The image format was checked on the PC by mounting the generated image again with littlefs-python (dummy files, 9 blocks, both files read back). It has not been mounted by the firmware.

On the first boot of an erased chip RTT shows littlefs `Corrupted dir pair` and `can't mount (LFS -84); formatting`; that is expected if the partition was not provisioned. `Failed to load certificate (err -2)` means the files are missing.

## Logs

RTT only. Open `JLinkRTTViewer.exe` (V9.82) with device `nRF54L15_M33`, SWD 4000 kHz, RTT control block address `20002070`, auto-detection off. Expected after provisioning: `Credentials loaded`, `Pouch initialized`, `Requesting a gateway for 30 s`, periodic `VBAT ... mV (..%)` lines.

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

## Charge validation (bring-up notes from before the Pouch port)

No UART on this board — use SEGGER RTT.

1. Flash firmware and open RTT.
2. Confirm boot: `VRF on, 2500 mV`, `ANT_SEL (P0.01) reads 0`, then the first `VBAT ... mV` line (the old `ANT_SEL set` and `PMIC ready` lines are gone).
3. Attach battery; connect USB-C — expect `VBUS connected` and charging status / rising SoC.
4. Disconnect USB; illuminate solar panel feeding SPV1040T — expect `VBUS connected` again and charge current while illuminated.

## Feather run 5 firmware

Status: devicetree, Kconfig and code written 2026-10-28; first built 2026-11-13 on NCS v3.4.0 (see the top of this file; NCS v3.3.0 was never installed). Nothing was flashed. 2026-11-13 recheck: the nPM1300 binding files (`nordic,npm13xx-regulator-common`, `nordic,npm13xx-charger-common`, `nordic,npm1300-charger`, `nordic,npm1300`, led, gpio) are identical in NCS v3.4.0 and v3.2.3 (the regulator driver only gained nPM1304 LDO soft-start), and every property in the board file compiles against them. Property names were checked by reading the NCS v3.2.3 sources (`zephyr/dts/bindings/regulator/nordic,npm13xx-regulator-common.yaml`, `sensor/nordic,npm13xx-charger-common.yaml`, `nordic,npm1300-charger.yaml`, `drivers/regulator/regulator_npm13xx.c`, `regulator_common.c`); v3.3.0 may differ.

Target: new board `nrf54l15_feather/nrf54l15/cpuapp` in `firmware\boards\nrf54l15_feather\` (was `soil_moisture_fw\boards\others\nrf54l15_feather\` before 2026-11-10; copied from `soil_moisture`; the existing soil_moisture board is untouched and the app still builds for it). Build: `.\scripts\build.ps1 -Board nrf54l15_feather/nrf54l15/cpuapp -BuildDir <dir>`. Feather-only code is `src\feather_run5.c` (compiled when `CONFIG_BOARD_NRF54L15_FEATHER`) and `boards\nrf54l15_feather_nrf54l15_cpuapp.conf` (`CONFIG_ADC=y`).

Pins from the netlist (kicad-cli export of `nrf54l15_feather.kicad_sch`, 2026-10-28): I2C SCL P1.03, SDA P1.04; PMIC_INT P0.00 (U2 GPIO1); ANT_SEL P0.01 (U6.24 -> U7.2 -> ANT_VCTL -> R11.6); SENS_ID P1.06 (U6.7, SAADC AIN2, R19 100k to VSENS); VSENS = U2.29 LSOUT1 (LDSW1, node LDO1); VRF = U2.31 LSOUT2 (LDSW2, node LDO2).

| Item | Where | Setting | Source |
| --- | --- | --- | --- |
| 1 VRF | board dts `LDO2` | `regulator-initial-mode = NPM13XX_LDSW_MODE_LDO`, `regulator-init-microvolt = 2.5 V`, `regulator-always-on`, `startup-delay-us = 1000` | STATUS.md run 5 stage 1 item 2 and stage 2 to-do 4; driver `regulator_common_init` applies mode, then voltage, then enable, then the delay |
| 2 ANT_SEL | board dts `&gpio0` `ant-sel-hog` (output-low), plus the `ant-sel` gpio-leds alias that `main.c` still drives inactive | P0.01 low = VCTL 0 = ANT-RF1 = chip antenna (FM8625H truth table, review report B4 update; U7 is non-inverting). Hog init is POST_KERNEL priority 41, the nPM1300 regulators init at 85/86, so P0.01 is driven before VRF is on | FM8625H v1.2 via the review report; SN74AUP1G34 SCES603K |
| 3 BUCK1 | board dts | no `BUCK1` node at all, so the driver creates no BUCK1 device and nothing can write BUCK1ENASET. VSET1 is grounded via R9 0R (off). BUCK2 (VDDIO) is `always-on` with a 2.9-3.1 V window and no software voltage write | STATUS.md item 3 |
| 4 NTC | `charger` node | `thermistor-ohms = 10000`, `thermistor-beta = 3380` | R8 Murata NCP15XH103F03RC, B25/50 3380 K |
| 5 SENS_ID | `feather_read_sens_id()` + dts `&adc channel@0` | `regulator_enable(VSENS)`, wait 50 ms, SAADC read on AIN2 (gain 1/4, internal ref, 40 us acquisition, 4x oversampling), `regulator_disable(VSENS)`. Rid is estimated as 100k * V / (3.0 V - V); open pin (above 2.9 V) gives 0 | STATUS.md item 7 |
| 6 Currents | `charger` node | charge `current-microamp = 150000` (cap is 300 mA; raise to at most 300000), `vbus-limit-microamp = 300000` (binding range 100-1500 mA in 100 mA steps) | STATUS.md stage 3.4 (0.25 mm VBAT/VBUS sections) |

VRF: always on from boot is the simple safe choice (load about 50-90 uA, U7 0.9 uA). Switching it around TX/RX would save that current (matters on the 20-30 uA solar budget of other boards) but needs the 10 us switch settling and the U7 input handling on every cycle; do that only if the bench shows the current matters. If it is switched, drive P0.01 first and switch VRF off only after the radio is idle.

Needs a bench test:
- VRF: rise time and the real settling of R11 (the 1 ms startup delay is a placeholder, the need is about 10 us after the rail is up); check VRF = 2.5 V on the scope and that VCTL follows ANT_SEL.
- P0.01 between reset and the hog (MCU reset while the PMIC keeps VRF on): U7's input floats for a short time. Fit R20 (1M pull-down, DNP) if the VCTL glitch matters.
- NTC: read the charger's battery temperature with the real R8 and a battery; check the 10k/3380 setting against room temperature.
- Dead-battery USB attach: the nPM1300 default VBUS limit is 100 mA until set; check that the board starts from a dead battery on USB, that the 300 mA VBUS limit holds with 150 mA charge plus the load, and that charging resumes. Also check whether the Rd on CC1/CC2 works with R1/R2 DNP.
- SENS_ID: voltages for 10k, 22k, 47k, 100k, 220k and open; confirm the settle time on a real sensor board.
- LFCLK: X2 is DNP; select the LFCLK source in Kconfig before using BLE.

## SENS_ID divider rescale (2026-11-11)

Hardware: R19 (VSENS to SENS_ID) 10k to 100k; sensor-board R_ID EC 10k, DO 22k, ORP 47k, pH 100k, water level 220k. Ratios are unchanged, so pin voltages and the 2.9 V open threshold are unchanged (220k gives about 2.06 V, still below open).

Firmware: `SENS_ID_PULLUP_OHM` is 100000 (the Rid estimate scales with it); `VSENS_SETTLE_MS` 20 to 50 ms (source impedance is now 50-70k, so stray capacitance on SENS_ID settles 10x slower); acquisition time stays 40 us.

Acquisition time basis: the nRF54L15 SAADC TACQ field is 9 bits, tacq = (TACQ+1) x 125 ns (up to 64 us; from the nrfx MDK SVD, NCS v3.1.0). I could not load the Nordic datasheet's acquisition-time vs source-resistance table (the docs page body did not come through). From memory, the nRF52 SAADC table allows about 100k at 10 us and about 800k at 40 us; the nRF54L15 table is unverified, so check it when the SDK is installed. 40 us leaves a large margin for 70k either way. If the bench shows reading error, raise it with a raw value such as `ADC_ACQ_TIME(ADC_ACQ_TIME_MICROSECONDS, 60)` (the nRF54L branch of the Zephyr driver takes any multiple of 125 ns).
