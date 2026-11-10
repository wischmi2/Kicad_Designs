# pH sensor - Status

Project: C:\Personal-Agents\worktrees\nrf54l15-feather-branch\ph_sensor\ph_sensor.kicad_pro
Last reviewed: 2026-10-23

**State: SUPERSEDED (2026-10-23, per Brian).** The active pH board is nrf54l15_feather_sens1.

## Summary
Standalone isolated pH board carrying a XIAO nRF54LM20A module (U1).
- Measurement side: Atlas pH OEM (U2), ADuM1250 I2C isolator (U3), NXE1S0303MC isolated DC-DC (U4), SMA probe input (J1).
- Other connectors: JST PH 3-pin (J2), JST PH 2-pin (J3), JST SH 4-pin (J4).

## Current state
- Schematic: a single sheet.
- PCB: about 70.11 x 39.96 mm, 2 layers. 19 footprints, 205 track segments, 120 vias, 12 zones. No mounting-hole footprints.
- ERC (2026-10-23): 1 error (C1 pin 2 power input has no driver) and 22 warnings, mostly pin_to_pin.
- DRC (schematic parity on, 2026-10-23): 0 errors, 45 warnings, 0 unconnected items.
  - Parity: C3 pad 2 is on GND_ISO but the schematic says GND. J5 (Conn_01x01) is missing from the PCB.
  - Also: one pair of co-located GND_ISO vias, 31 silk-over-copper warnings, and 4 footprint library mismatches.
- An older DRC.rpt (2026-07-16) reports 53 violations.
- Fab outputs: CPL (ph_sensor.csv), BOM xlsx, a render (ph_sensor.png) and ph_sensor.kicad_pcb.zip. No Gerbers in the folder.
- Enclosure / STEP: none exported.

## Open work
- None while superseded. The C3 GND vs GND_ISO conflict is worth checking in sens1, which uses the same circuit.

## Questions for Brian
- Was a revision of this board ordered? This only matters for the history.

## Decisions
- 2026-10-23 (Brian): superseded by nrf54l15_feather_sens1.
