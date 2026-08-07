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
$env:BOARD_ROOT = "c:/Users/Brian/Kicad_Designs/soil_moisture_fw"
nrfutil sdk-manager toolchain launch --ncs-version=v3.3.0 --chdir c:\ncs\v3.3.0 -- `
  west build -p -b soil_moisture/nrf54l15/cpuapp `
  -d c:\Users\Brian\Kicad_Designs\soil_moisture_fw\build_v330 `
  c:\Users\Brian\Kicad_Designs\soil_moisture_fw
```

Artifact: `build_v330/soil_moisture_fw/zephyr/zephyr.hex`

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
