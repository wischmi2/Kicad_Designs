# Feather dissolved oxygen sensor board - Status

Project: C:\Personal-Agents\worktrees\nrf54l15-feather-branch\hardware\sensors\dissolved_oxygen\feather_dissolved_oxygen.kicad_pro
Last reviewed: 2026-10-26

**State: LAID OUT AND ROUTED (rev 0.1), not reviewed.** Built from feather_sensor_template (isolated variant). ERC/DRC clean. R_ID not assigned yet. Not a fab design: no fab outputs made; needs a design review and Brian's answers below first.

## Summary
- Purpose: dissolved oxygen node. Sensor is the Atlas Scientific Dissolved Oxygen OEM (OEM-DO) castellated module, I2C/SMBus addr 0x67, with a galvanic DO probe (Atlas ENV-40-DOX, male SMA) on J1.
- Host side and isolation are the template unchanged: CN1 Molex 503480-1400, C1/C2 on VSENS, R1 = R_ID; U3 ADuM1250 I2C isolator, U4 NXE1S0303MC isolated DC-DC, C3/C4, R3/R4 4.7k pull-ups on the isolated side, J5 INT_ISO test pad.
- Sensor sheet (isolated side): U2 Atlas DO OEM (VCC from VDD_ISO, GND pin 6 to GND_ISO, SDA/SCL to SDA_ISO/SCL_ISO, INT pin 7 to INT_ISO / J5 only, NC pins 2/9/10 no-connect), C5 1 uF at U2 VCC, J1 SMA (centre = PRB pin 4, shell = PRB GND pin 5, net /Sensor/DO_PRB_GND), R5 0R DNP optional DO_PRB_GND to GND_ISO link.
- Checked against the DO OEM datasheet (v3.5, files.atlas-scientific.com/DO_OEM_Datasheet.pdf): pinout 1 SDA, 2 NC, 3 VCC, 4 PRB, 5 PRB GND, 6 GND, 7 INT, 8 SCL, 9 NC, 10 NC (matches symbol and footprint); VCC 3.0-5.5 V, about 2.5 mA at 3.3 V; 4.7k pull-ups on both sides of the isolator (as R3/R4 here and the host's own); INT unused must float (it goes only to the J5 pad); isolation of power, SDA, SCL and INT recommended (the INT is not isolated to the host, see Questions); no vias or exposed metal under the module; probe traces on top, 0.4 mm, short.
- No enable/hibernate pin: the module is hibernated over I2C (register 0x06); the whole isolated side is switched by VSENS anyway.

## Parts added (LCSC checked live on jlcpcb.com 2026-10-26)
| Ref | Part | LCSC | Package / footprint | Stock |
| --- | --- | --- | --- | --- |
| C5 | Samsung CL05A105KA5NQNC 1 uF 25 V X5R | C52923 | 0402 / C_0402_1005Metric | 11.5 M, basic |
| J1 | BAT Wireless BWSMA-KWE-Z001 SMA jack, right angle THT | C496551 | Plugin / SMA_BAT_Wireless_BWSMA-KWE-Z001 | 125 k, extended |
| R5 | UNI-ROYAL 0402WGF0000TCE 0R (DNP) | C17168 | 0402 / R_0402_1005Metric | 9.0 M, basic |
| U2 | Atlas Scientific OEM-DO | none | project footprint Atlas_DO_OEM | buy from Atlas (not on LCSC/JLCPCB) |

## Current state (2026-10-26)
- Schematic: root + Sensor Connector + Isolation + Sensor, title blocks rev 0.1 ("Feather sensor DO"). Project symbol library feather_dissolved_oxygen.kicad_sym (Atlas_DO_OEM). Project footprint library feather_dissolved_oxygen.pretty (Atlas_DO_OEM, moved there from feather_sensor_template.pretty; fp-lib-table and the symbol/schematic footprint links updated; F.Fab body and silk outline + pin-1 mark added). feather_sensor_template.pretty now only holds the CN1 Molex footprint.
- R1 (R_ID) is back at the template placeholder "10k (set per SENSORS.md)": the previous run had set 2.2k 1 % (type 2) without a register. See Questions.
- PCB: template outline, stackup, holes and keep-outs unchanged. New parts on the top side at the probe end, same geometry as sens1's pH OEM: U2 (107, 119.1), J1 (94.4, 121.425) rot 90 on the x = 90 short edge opposite CN1 (barrel past the edge as on sens1), C5 (97.8, 115.8) rot 270 next to U2 pin 3, R5 (106.1, 128) on the guard/GND_ISO boundary.
- Routing: DO_PRB 0.4 mm on F.Cu straight from U2 pin 4 to J1 centre (about 6 mm). DO_PRB_GND_guard pours (priority 1) on all 4 layers over x 90-106 (notch around U2 pins 1-3) with 5 stitching vias; U2 pin 5 and the J1 shell tie into it. VDD_ISO F.Cu along y = 111 from the R3/R4 rail to x = 98.9, then down to U2 pin 3 and C5. SDA_ISO B.Cu along y = 112 from the existing via at R3 to a via at (100.8, 112), then F.Cu to U2 pin 1. SCL_ISO F.Cu x = 117 from R4 to U2 pin 8. INT_ISO U2 pin 7 to J5. U2 pin 6 to the GND_ISO pour. Rule area U2_no_vias_under_module (x 101-113, y 113.6-124.6, all layers, vias not allowed) enforces the datasheet note.
- Silk (B.SilkS): "FEATHER SENSOR DO rev 0.1", "SENSOR TYPE: DO R_ID: ______".
- ERC (kicad-cli 10.0.4): **0 errors**, 36 warnings: 10 pin_to_pin (EasyEDA passives, as template), 8 lib_symbol_issues + 7 footprint_link_issues (EasyEDA2Kicad / easyeda2kicad / Parts_1 / Connector_FFC-FPC libraries not registered on this PC), 7 isolated_pin_label (unused CN1 signals SENS_SCK/MOSI/MISO/CS/INT/AIN and VBAT), 4 lib_symbol_mismatch (GND power symbols).
- DRC (kicad-cli 10.0.4, --schematic-parity, with and without --refill-zones): **0 errors, 0 unconnected, 0 parity**, 11 warnings: 7 lib_footprint_issues (easyeda2kicad not registered) and 4 silk_over_copper (EasyEDA pin-1 dots on R1/R3/R4/C1, as template).
- STEP: C:\Personal-Agents\shared\handoff\feather_dissolved_oxygen\feather_dissolved_oxygen_2026-10-26.step. Board, holes, CN1, U3, U4 included. **J1 (SMA, no KiCad model for BWSMA-KWE-Z001), U2 (DO OEM, no model) and the EasyEDA passives are missing**, same as sens1. Heights for the enclosure: J1 about 6.5-8 mm above the top and barrel about 7.6 mm past the x = 90 edge (sens1 estimate, not verified), U2 under 3.1 mm (Atlas tube inside height), U4 4.5 mm.
- Fab outputs: none.

## Open work
- Design review (pre-fab) of the sensor area.
- Assign R_ID once the ID register exists, then set R1 value/MPN/LCSC and the B.Silk "R_ID" text.
- 3D models for J1 and U2 (or simple bodies) so the STEP is complete for the enclosure.
- Register the easyeda2kicad / EasyEDA2Kicad / Parts_1 libraries on this PC (clears 22 library warnings, adds passive 3D models).

## Questions for Brian
- R_ID: there is no SENSORS.md. docs\notes\v4-sensor-connector.md has the ID table (1k type 1 ... 100k type 7) but no assignments. The previous run proposed DO = 2.2k (type 2); the ORP board has 4.7k (type 3), conductivity proposes 1k (type 1), sens1 pH has 10k (type 4). Create SENSORS.md with these and fit 2.2k here?
- Atlas_DO_OEM footprint pad pitch is 2.2/2.2/2.3/2.3 mm (copied from the Atlas DXF used for the sens1 pH footprint); the DO datasheet says 2.3 mm all pins. Pad 1 is about 0.2 mm off a true 2.3 mm grid but still overlaps the castellation. Keep the sens1 geometry (same as the pH board, if that was built and fitted fine) or switch to an exact 2.3 mm grid?
- Probe ground: J1 shell and U2 PRB GND are a separate DO_PRB_GND guard pour, linked to GND_ISO only through R5 (DNP), as on sens1. The datasheet only asks for a ground plane under/around the probe traces and does not say to tie PRB GND to GND. Keep R5 DNP as default, or fit it?
- INT: the 2-channel ADuM1250 leaves INT_ISO on J5 only, so firmware polls register 0x07 (new reading). OK, or move to a 3-channel isolator (template question)?
- VDD_ISO from the NXE1S0303MC is about 3.0 V at VSENS 3.0 V, the bottom of the DO OEM's 3.0-5.5 V range (Atlas's own isolation example runs the module at 3.9 V). Workable on paper with no margin; accept, or adopt the VBAT-fed isolated supply the conductivity board is planning (architecture change)?
- Stack height: the right-angle SMA sets the gap to the feather at about 8 mm, as on sens1. OK?

## Decisions
- 2026-10-25 (Brian): one sensor board per feather; isolated template is the default; CN1 point to point; R_ID identifies the board.
- 2026-10-26: placement and probe guard copied from sens1 (proven layout for the same Atlas OEM carrier and SMA); no-via rule area added under U2; Atlas_DO_OEM kept in a project library feather_dissolved_oxygen.pretty.
- 2026-10-26: R_ID left unassigned until a SENSORS.md register exists (coordinator instruction).
