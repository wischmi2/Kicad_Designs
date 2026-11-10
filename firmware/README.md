# Firmware

nRF Connect SDK (Zephyr) firmware for the nRF54L15 boards in `hardware\`.

| Folder | What |
| --- | --- |
| `boards\nrf54l15_feather\` | Board definition `nrf54l15_feather/nrf54l15/cpuapp` (main feather, `hardware\feather\`) |
| `boards\soil_moisture\` | Board definition `soil_moisture/nrf54l15/cpuapp` (old soil-moisture board, `hardware\archive\`) |
| `apps\feather_node\` | Node application (bring-up, PMIC, fuel gauge, SENS_ID). Build/flash scripts in `scripts\`, notes in `README.md` and `HW_VERIFY.md` |

`firmware\` is the Zephyr `BOARD_ROOT` (Zephyr looks for `BOARD_ROOT\boards\**\board.yml`).
The app adds it in `CMakeLists.txt` and `sysbuild\CMakeLists.txt`, and `scripts\build.ps1` sets it in
`$env:BOARD_ROOT`. App-level board overlays (`apps\feather_node\boards\<board>.conf`) stay with the app.

Build (needs NCS v3.3.0, not installed on this PC as of 2026-11-10):

```powershell
cd C:\Personal-Agents\worktrees\nrf54l15-feather-branch\firmware\apps\feather_node
.\scripts\build.ps1 -Board nrf54l15_feather/nrf54l15/cpuapp
.\scripts\flash.ps1
```

Until 2026-11-10 this was `soil_moisture_fw\` at the repo root, with the board definitions in
`soil_moisture_fw\boards\others\`. See `docs\reorg_2026-11-10.md`.
