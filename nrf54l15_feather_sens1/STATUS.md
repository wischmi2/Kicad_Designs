# Feather sensor board 1 - Status

Project: C:\Personal-Agents\worktrees\nrf54l15-feather-branch\nrf54l15_feather_sens1\nrf54l15_feather_sens1\nrf54l15_feather_sens1.kicad_pro
Last reviewed: 2026-10-23

**State: ACTIVE sensor board for the nRF54L15 feather (2026-10-23, per Brian).** It replaces ph_sensor.

## Summary
Isolated pH sensor board in Feather form factor. It connects to the feather through CN1. The CN1 pinout matches the feather pin for pin (netlist checked 2026-10-23).
- Parts on the PCB: Atlas pH OEM (U2), ADuM1250 I2C isolator (U3), NXE1S0303MC isolated 3.3 V DC-DC (U4), SMA/coax probe input (J1), and the 14-pin Molex 503480-1400 connector (CN1).
- The project still carries copies of the feather sheets (nrf54l15, npm1300, power_supply, usb, antenna, battery, SWD_Debug) plus ph_sensor and sensor_connector. The PCB has only 15 footprints, so most of those sheets don't appear to be used on this board.

## Current state
- Schematic: root sheet plus sub-sheets copied from the feather project.
- PCB: about 66.04 x 25.40 mm, the same outline as the feather. 4 layers. 15 footprints, 14 track segments, 3 vias, 10 zones. **Mostly unrouted.**
- ERC (2026-10-23): 0 errors, 24 warnings (10 pin_to_pin, 7 isolated_pin_label, 4 lib_symbol_mismatch, 3 lib_symbol_issues).
- DRC (2026-10-23): 38 errors, all unconnected items on the isolated side (AGND_ISO, GND_ISO, SDA_ISO, +3v3V_ISO). Also 17 warnings: silkscreen, and 2 dangling vias.
- Fab outputs: only a gerber job file (nrf54l15_feather_sens1-job.gbrjob). No Gerbers.
- Enclosure / STEP: none exported.

## Open work
- Route the isolated side (38 unconnected items).
- Remove or confirm the unused copied sheets.

## Questions for Brian
- How does it sit relative to the feather: stacked directly above it on standoffs, or side by side on an FFC? This sets the CN1 position and the enclosure.
- Should it get the same mounting-hole pattern as the feather? (Recommended if it stacks.)
- Are the copied MCU/PMIC sheets meant to stay in this project?
- J5 (Conn_01x01) is on the PCB. What is it for?

## Decisions
- 2026-10-23 (Brian): this is the active sensor board. It replaces ph_sensor.
