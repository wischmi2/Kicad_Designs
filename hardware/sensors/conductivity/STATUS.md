# Feather conductivity (EC) sensor board - Status

Project: C:\Personal-Agents\worktrees\nrf54l15-feather-branch\hardware\sensors\conductivity\feather_conductivity.kicad_pro
Last reviewed: 2026-10-26

**State: DRAWN, PLACED AND ROUTED (rev 0.1), not reviewed.** Isolated Feather sensor board built from feather_sensor_template (stage 1 at 3e46ede). Not a fab design yet: no fab outputs made, and the questions below are open.

## Summary
- Purpose: conductivity / salinity node. Sensor is the Atlas Scientific EC OEM (OEM-EC) embedded conductivity circuit on the isolated side, read over I2C through the template's ADuM1250 isolator. Default address 0x64.
- Datasheet used: EC OEM datasheet v3.4 (revised 5/26), https://files.atlas-scientific.com/EC_oem_datasheet.pdf. VCC 3.0 to 5.5 V; current 10.6 mA (0 uS) to 26 mA (100,000 uS and up) at 3.3 V; SMBus/I2C 10 to 100 kHz; ready 1 ms after power-up; one reading every 640 ms. Calibration and I2C address survive power-off; active/hibernate, LED and interrupt control do not.
- Sensor sheet (same structure as feather_orp / feather_dissolved_oxygen):
  - U2 Atlas_EC_OEM: pin 1 SDA_ISO, 3 VCC = VDD_ISO, 4 and 5 probe (EC_PRB1, EC_PRB2), 6 GND_ISO, 7 INT to INT_ISO (J5 test pad only), 8 SCL_ISO, 2/9/10 NC left floating.
  - J1 SMA jack (BAT Wireless BWSMA-KWE-Z001, the sister boards' part): centre = EC_PRB1 (pin 4), shell = EC_PRB2 (pin 5).
  - C5 1 uF + C6 100 nF on U2 VCC.
  - No pull-ups (R3/R4 4.7k on the Isolation sheet), no AGND net and no AGND-to-GND_ISO link: unlike the pH/ORP/DO OEMs, the EC OEM has no probe-ground pin (the datasheet labels pins 4 and 5 both "PRB"). Both are drive/sense electrodes, so the SMA shell carries a probe signal and is not ground.
- Project libraries: feather_conductivity.kicad_sym (Atlas_EC_OEM) and feather_conductivity.pretty (Atlas_EC_OEM), registered in sym-lib-table and fp-lib-table.
  - Footprint: 10 pads 2.5 x 1.4 mm, rows 12 mm centre to centre, 2.3 mm pitch, body 12 x 11.9 mm, no-via rule area under the body. Taken from the datasheet text (p.5 dimensions, p.35 "Recommended pad layout"). Those numbers are identical to the ORP OEM datasheet and match feather_orp's Atlas_ORP_OEM. I could not render the datasheet drawing on this PC (no PDF rasteriser), so how the numbers map onto the drawing has not been checked by eye. See open work.
- R1 (R_ID) not set: there is no SENSORS.md register. The value is still "10k (set per SENSORS.md)". sensor-board-conductivity.md proposes 1k (type 1).

## Parts added (LCSC numbers checked on jlcpcb.com 2026-10-26)
| Ref | Part | LCSC | Check result |
|---|---|---|---|
| U2 | Atlas Scientific OEM-EC | none (buy from Atlas) | datasheet v3.4 |
| J1 | BAT Wireless BWSMA-KWE-Z001, SMA jack, right angle, THT | C496551 | exists, "Plugin", Extended. Matches the THT footprint Connector_Coaxial:SMA_BAT_Wireless_BWSMA-KWE-Z001 |
| C5 | Samsung CL05A105KO5NNNC 1 uF 16 V X5R 0402 | C29266 | exists, 0402, Extended. Footprint C_0402_1005Metric |
| C6 | Samsung CL05B104KO5NNNC 100 nF 16 V X7R 0402 | C1525 | exists, 0402. Footprint C_0402_1005Metric |

**Stock not verified.** The JLCPCB and LCSC part pages don't show a stock figure. The jlcsearch tool returned stock 0 for all three, including C1525, which is a common basic part, so its stock figures can't be trusted. Check stock before ordering.

## Current state (2026-10-26)
- Schematic: root + Sensor Connector + Isolation (both unchanged from the template) + Sensor (above). Title blocks renamed to conductivity.
- PCB (origin = outline top-left at 90, 110; the outline, holes, CN1, barrier and keep-outs are unchanged from the template):
  - U2 at (106.9, 119.13), rotation 0. Pads 1 to 5 face the probe edge, and pin 4 lines up with the SMA centre at y 121.43.
  - J1 at (94.4, 121.43), rotation 90. The thread points out of the x = 90 short edge, opposite CN1. The footprint body is 7.8 x 7.8 mm, x 90.5 to 98.3; the thread reaches x 82.4 (7.6 mm beyond the edge). The shell pads clear the H1/H2 3.5 mm keep-outs and the 0.5 mm edge rule.
  - C5 (97.6, 114.6) and C6 (97.6, 116.2), rotation 180, next to U2 pin 3.
  - Probe traces (datasheet p.34): top layer, 0.4 mm. EC_PRB1 runs straight from U2 pin 4 to the SMA centre (about 5 mm) and passes 1.25 mm from the shell pads. EC_PRB2 runs from pin 5 to the lower-right shell pad. The other three shell pads are joined by a 0.4 mm EC_PRB2 ring on B.Cu. GND_ISO pours surround the probe traces on all 4 layers, plus GND_ISO stitching vias at (98.6, 126.0) and (103.5, 127.0). No vias under U2 (the footprint rule area enforces this).
  - VDD_ISO: pin 3 to C6/C5 on F.Cu (x = 98.75), then a via at (98.75, 111.0) and an In2.Cu track along y = 111 to the template's VDD_ISO trunk at (118.3, 111).
  - SDA: pin 1, via at (100.9, 112.3), B.Cu along y = 112.3 to the existing SDA_ISO via (119.6, 113.85).
  - SCL: pin 8 to the existing SCL_ISO track at (117, 114.565). INT: pin 7 to J5. GND: pin 6 to the GND_ISO via (116, 123.6).
  - B.SilkS: "FEATHER SENSOR EC  rev 0.1" and "SENSOR TYPE: EC (Atlas OEM-EC 0x64)   R_ID: ______".
- ERC (kicad-cli 10.0.4): **0 errors**, 36 warnings:
  - 10 pin_to_pin (template EasyEDA passives)
  - 7 isolated_pin_label (unused CN1 signals SENS_SCK/MOSI/MISO/CS/INT/AIN and VBAT)
  - 8 lib_symbol_issues and 7 footprint_link_issues (EasyEDA2Kicad / easyeda2kicad / Parts_1 / Connector_FFC-FPC libraries not registered on this PC)
  - 4 lib_symbol_mismatch (GND)
  - The template's INT_ISO isolated-label warning and the 5 sensor-sheet stub warnings are gone.
- DRC (kicad-cli 10.0.4, --schematic-parity --refill-zones): **0 errors, 0 unconnected, 0 parity**, 11 warnings, the same as the template:
  - 7 lib_footprint_issues (easyeda2kicad not registered)
  - 4 silk_over_copper (EasyEDA pin-1 dots on R1/R3/R4/C1; the fab clips them)
- STEP: C:\Personal-Agents\shared\handoff\feather_conductivity\feather_conductivity_2026-10-26.step. It contains the board, holes, CN1, U3 and U4. U2 (EC OEM, 12 x 11.9 mm footprint body; the datasheet gives no height) has no 3D model. **The SMA J1 has no 3D body**: the BWSMA-KWE-Z001 model is not in this KiCad 10.0.4 install. Use the footprint envelope above for the enclosure. The EasyEDA passives are also missing (as in the template).
- Fab outputs: none.

## Open work
- Review the Sensor sheet and U2/J1 in the KiCad GUI. The sheet's symbols were written into sensor.kicad_sch directly as S-expressions (the same method as the sister boards), not placed through MCP or the GUI. kicad-cli loads it, ERC is clean and the PCB update links all four parts, but nobody has looked at it in the GUI.
- Check the Atlas_EC_OEM land pattern against the datasheet drawing (p.5 and p.35), or against Atlas's "OEM footprint" DXF, before fab. sens1's older Atlas_pH_OEM (from the DXF) uses 2.9 x 1.5 mm pads at +-6.2 mm. This board follows the datasheet text (2.5 x 1.4 mm at +-6.0 mm), the same as feather_orp.
- Set R1 (R_ID) once a SENSORS.md register exists, and update the R_ID silk.
- Bench-measure VDD_ISO at U2 under load at VSENS = 3.0 V (see the questions).
- Add an SMA 3D model (vendor STEP) so the enclosure STEP shows the jack.
- Firmware notes: write the temperature to registers 0x10 to 0x13 before each reading. Re-write interrupt control and active mode after every VSENS cycle (they are lost at power-off). Don't take EC readings while a pH/ORP/DO node in the same tank is measuring (Atlas: EC readings inject interference into the water).

## Questions for Brian
- **Probe connector:** SMA, the same as the sister boards. Atlas EC probes ship with a BNC plug, so you'd use a BNC-to-SMA adapter cable. The EC OEM datasheet gives no reason against SMA; it only asks for the shortest possible distance from the SMA/BNC to the OEM. One EC-specific point: the connector shell carries probe pin 5 (EC_PRB2), not ground. With an SMA, the adapter and cable shield are then a live electrode lead, which must not touch the enclosure metal or another probe's shield. OK, or use a board BNC (larger, would need a re-layout of the probe end)?
- **VDD_ISO margin:** the EC OEM minimum is 3.0 V. VDD_ISO is the unregulated NXE1S0303MC output from VSENS 3.0 V, so it sits about at that minimum, lower under load (the NXE1 numbers are from memory, not re-checked). The EC OEM draws up to 26 mA. My estimate is about 40 to 45 mA from VSENS, including the isolator, out of the 100 mA VSENS budget; the efficiency is assumed, not measured. Keep the template supply and bench-test it, or move this board to the VBAT-fed isolated supply in sensor-board-conductivity.md section 5.3 (SN6505 + transformer + LDO, about 3.9 V, as in the Atlas isolation reference)? That would be an architecture change, so it is not done.
- **R_ID:** no SENSORS.md exists. Create it, and use 1k = conductivity as proposed in sensor-board-conductivity.md?
- **INT:** INT goes to the J5 test pad only (2-channel ADuM1250), and firmware polls register 0x07. That is the same as the sister boards; OK?
- **Probe:** which K? K 1.0 suits seawater (about 53 mS/cm); the EC OEM supports K 0.01 to K 600. Set the probe type in registers 0x08/0x09.

## Decisions
- 2026-10-26 (coordinator task): Atlas EC OEM, I2C 0x64, VCC from VDD_ISO, SMA probe connector on the x = 90 edge, the same structure as feather_orp / feather_dissolved_oxygen.
- 2026-10-26: SMA centre = PRB1 (pin 4), shell = PRB2 (pin 5). No 0R link from the shell to GND_ISO, because the EC OEM has no probe ground and grounding pin 5 would short a probe electrode.
- 2026-10-26: decoupling C5 1 uF + C6 100 nF on U2 VCC, plain Device:C symbols with standard KiCad 0402 footprints (the DO board's pattern, so no new library warnings).
- 2026-10-26: U2 footprint follows the datasheet text values, consistent with feather_orp.
