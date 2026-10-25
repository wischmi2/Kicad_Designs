# Pouch gateway - Status

Project: C:\Personal-Agents\worktrees\nrf54l15-feather-branch\pouch_gateway\pouch_gateway.kicad_pro
Last reviewed: 2026-10-23
Design notes: C:\Personal-Agents\worktrees\nrf54l15-feather-branch\pouch_gateway\docs\DESIGN_NOTES.md (Rev A)

## Summary
Golioth Pouch BLE to Wi-Fi gateway, Rev A.
- Module: Murata Type 2FR (U1, LBES0ZZ2FR, NXP RW612). Wi-Fi backhaul only.
- Power: USB-C only, with a TLV62569 buck to 3.3 V (U2).
- Interfaces:
  - USB-C (J1)
  - SWD header (J2) and Tag-Connect TC2030 (J6)
  - UART (J4)
  - 8-pin JST PH connector for a 2.0 in Waveshare LCD (J5)
  - Two U.FL connectors (J3 for the main antenna, J7 for an optional second BLE antenna)
  - RESET, ISP and USER buttons, and LEDs
- Sub-sheets: mcu, power, reset_debug, rf, ui_io, usb.

## Current state
- PCB: 58.0 x 35.0 mm, 4 layers. 70 footprints, 710 track segments, 229 vias, 11 zones. Four M2 mounting holes (H1-H4) on the Waveshare 53 x 30 mm pattern.
- ERC (2026-10-23): 0 errors, 195 warnings (140 endpoint_off_grid, 53 lib_symbol_mismatch, 2 unconnected wire endpoints).
- DRC (schematic parity on, 2026-10-23): 0 errors, 22 warnings, 0 unconnected items.
  - Parity: SW1/SW2/SW3 show up as both missing and extra footprints. The footprint references look like they are "RESET", "ISP" and "USER" instead of SW1-3, so the board and schematic references are probably out of sync.
  - Silkscreen: 10 overlap, 6 over copper.
- DESIGN_NOTES.md "Layout status" (2026-10-18) describes partial routing (119 segments). The board has changed a lot since then, so those notes are out of date.
- Fab outputs: Gerbers (4-layer), drill file, CPL (pouch_gateway.csv), PCBWay BOM xlsx and pouch_gateway.7z are in the folder. I couldn't tell whether they match the current PCB.
- Enclosure / STEP: none in C:\Personal-Agents\shared\handoff\.

## Open work
- Fix the SW1-3 reference mismatch, then re-run DRC.
- Open items listed in DESIGN_NOTES.md:
  - Antenna part from the HSW2FR FCC filing
  - Buck part check (TLV62569 is now in the design, so this may be done)
  - pSRAM requirement for the Golioth gateway
  - Zephyr console UART pins
- Layout to-dos listed in DESIGN_NOTES.md: physical stackup and 50 ohm CPWG, RF feed length, zone fill, silkscreen cleanup.
- Update the "Layout status" section of DESIGN_NOTES.md.
- Next rev (possible upgrade, Brian 2026-10-24): on-board 1S LiPo charger with power path, JST PH 2-pin battery connector and an "on battery"/battery-voltage signal to a GPIO, for power-cut ride-through. See concepts.md section 8.

## Questions for Brian
- Was the physical stackup set and the RF feed sized for 50 ohm? I didn't check the stackup in the file.
- Is the buck regulator decided (TLV62569DBVR)? DESIGN_NOTES.md still lists it as open.
- Are the Gerbers and the 7z current, and were they sent to fab?

## Decisions
- 2026-10-24 (Brian): the gateway PCB has no battery circuit. It's powered only by USB-C. A battery, if used, needs an external charger/5 V boost module feeding J1, inside the enclosure. The PCB is fixed and on order.
- 2026-10-24 (Brian): enclosure placement is a shelf or desk with AC (USB) power available all the time. This answers question 1 in shared\design\pouch_gateway\concepts\2026-10-24-enclosure\concepts.md and points to the Ledger concept.
- 2026-10-24 (Brian): printer is a Snapmaker U1 (4-toolhead toolchanger, 270 x 270 x 270 mm, 300 °C nozzle, 100 °C bed, no top cover mentioned). Open to filament suggestions; proposed PETG body + translucent PETG/PCTG light pipe + TPU feet (answers question 8).
- 2026-10-24 (Brian): Rev A is wall (USB-C) power only, with no battery, PowerBoost or pigtail in the enclosure. This replaces the earlier "small pack for power cuts" answer. External USB-C keeps data, and the USB_VBUS 0 ohm stays fitted (closes concepts questions 2, 3 and 7). Checked the schematic: no charger, battery connector or power path on the board.
- 2026-10-24 (Brian): enclosure concept is Ledger (concepts.md section 5). Desk/shelf placement means the wedge stand; no wall keyholes needed.
- 2026-10-24 (Brian): antenna is the Molex 146153 FPC as proposed (concepts question 6).
- 2026-10-24 (Brian): open window over the LCD, no cover lens (concepts question 10).
- 2026-10-24 (Brian): J2 (SWD) and J4 (UART) are not fitted on the build; Tag-Connect J6 is the debug path (concepts question 5).
- 2026-10-24 (Brian): colourway is Abyss navy with a coral key (concepts question 9).
- 2026-10-24: LCD module dimensions taken from Waveshare's STEP model, so no hand measurement is needed (concepts question 4). See shared\design\pouch_gateway\lcd_module\MEASUREMENTS.md. Active area is 1.71 mm off-centre towards the connector end; the module is 4.0 mm thick; the PH connector on its back is 5.6 mm tall.

## Decisions (from DESIGN_NOTES.md)
- 4 layers. M2 holes on the display hole pattern, which replaces the earlier mounting plan.
- SWD selected with a 5.1 kohm pull-down on RF_CNTL_2. RF_CNTL_0 left open (40 MHz XOSC).
- VBUS goes to pin 33 through a 0 ohm resistor that can be removed.
