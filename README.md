# Kicad_Designs

nRF54L15 sensor nodes (feather + one CN1 sensor board per node), the pouch gateway, and tools.
Layout since 2026-11-10 (old -> new map: `docs\reorg_2026-11-10.md`). Every board folder has a STATUS.md; read it first.

```
hardware\
  feather\              nRF54L15 feather, main board (KiCad project in feather\nrf54l15_feather\)
  sensors\              CN1 sensor boards + CN1_SENSOR_CONNECTOR.md, SENSORS.md (SENS_ID register)
    template\ ph\ orp\ dissolved_oxygen\ conductivity\ water_level\ water_level_tc2030\
  gateway\              pouch gateway (docs\ inside)
  prog_adapter\         programming adapter (XM125 UART, TC2030 SWD, USB-C 3.0 V)
  archive\              old/paused boards: nrf54l15_v2, v3, v4, ph_sensor, xiao_breakout,
                        pcbway_production, soil_moisture (the old root-level project)
firmware\
  boards\               Zephyr board definitions (firmware\ is BOARD_ROOT)
  apps\feather_node\    node application, build/flash scripts
mechanical\             enclosure exports: tidemark, ledger, crown, probe_nodes, bench_tray,
                        concepts\<product>, hardware_lists
docs\                   cross-board notes, datasheets, sourcing, cost analysis
CLAUDE.md               coordinator instructions and status log
```

Per board: `sourcing\` holds BOMs and part notes, `docs\` holds renders and design notes,
`archive\` / `fab_<date>\` hold fab output. KiCad project files keep their original names.
Board STEP and fab-zip handoffs live outside the repo in `C:\Personal-Agents\shared\handoff\<board>\`.
