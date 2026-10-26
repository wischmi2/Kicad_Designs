# Feather ORP sensor board - Status

Project: C:\Personal-Agents\worktrees\nrf54l15-feather-branch\Sensor_Boards\feather_orp\feather_orp.kicad_pro
Last reviewed: 2026-10-26

**State: LAID OUT AND ROUTED (rev 0.1), not reviewed.** Copied from feather_sensor_template (isolated variant), with the Atlas Scientific ORP OEM drawn on the Sensor sheet and placed and routed on the PCB. ERC and DRC are clean (0 errors). Not a fab design yet: it needs a design review, the R_ID value and the open questions below answered. No fab outputs have been made.

## Summary
- Purpose: ORP (redox) node. Sensor is the Atlas Scientific ORP OEM (OEM-ORP, datasheet v3.3): SMBus/I2C only (10-100 kHz), default address 0x66, VCC 3.0-5.5 V, about 3.5 mA. Probe on an SMA jack whose shell is the analog ground.
- Isolated board (template default): U3 ADuM1250 I2C isolator and U4 NXE1S0303MC isolated supply across the 3 mm barrier at x = 124. U2 runs from VDD_ISO / GND_ISO.
- Sensor sheet parts:
  - U2 Atlas ORP OEM (project symbol feather_orp:Atlas_ORP_OEM, footprint feather_orp:Atlas_ORP_OEM). Pin 1 SDA_ISO, 3 VCC = VDD_ISO, 4 PRB = ORP_PRB, 5 PRB GND = AGND_ISO, 6 GND = GND_ISO, 7 INT = INT_ISO (to the J5 test pad only), 8 SCL_ISO, 2/9/10 NC (no-connect flags, left floating as the datasheet requires).
  - J1 SMA probe input, BAT Wireless BWSMA-KWE-Z001, right-angle THT, LCSC C496551. Pin 1 ORP_PRB, shell AGND_ISO.
  - C5 1 uF 0402 X5R 16 V (Samsung CL05A105KO5NNNC, LCSC C29266) on U2 VCC.
  - R5 0R 0402 (UNI-ROYAL 0402WGF0000TCE, LCSC C17168): the single AGND_ISO to GND_ISO link.
- I2C pull-ups: R3/R4 4.7k to VDD_ISO on the Isolation sheet (template), no extra pull-ups on the Sensor sheet. Host side has its own pull-ups.
- LCSC numbers checked on 2026-10-26 against the JLCPCB catalogue (part search API): C496551 BWSMA-KWE-Z001 "Plugin", 125,098 in stock (extended); C29266 CL05A105KO5NNNC 0402, 2,544,745 in stock (extended); C17168 0402WGF0000TCE 0402, 9,034,566 in stock (basic). All match their footprints. U2 is bought from Atlas Scientific (no LCSC number).

## Current state (2026-10-26)
- Schematic: root + Sensor Connector + Isolation + Sensor. The Sensor sheet was drawn in the previous run (WIP commit bf5bbf2). This run checked it against the datasheet (pinout, NC pins, INT, decoupling, pull-ups, SMA, AGND link) and found nothing to change.
- R1 (R_ID) is back to the template placeholder "10k (set per SENSORS.md)". The previous run had set 4.7k 1 % (C25900, "board type 3 = ORP" from the ID table in v4-sensor-connector.md), but SENSORS.md doesn't exist, so the value was reverted and left as a question (see below). The B.SilkS line reads "SENSOR TYPE: ORP   R_ID: ______".
- Footprint Atlas_ORP_OEM redrawn this run to the ORP datasheet v3.3 "Recommended pad layout": pads 2.5 x 1.4 mm, rows 12 mm apart centre to centre, 2.3 mm pitch, body 12 x 11 mm on F.Fab with a pin-1 chamfer, silk and courtyard (15 x 11.5 mm), and a footprint rule area that bans vias under the module ("NEVER place vias under the OEM footprint"). **It differs from the copied sens1 pH footprint** (2.9 x 1.5 mm pads, 12.4 mm rows, uneven 2.2/2.3 mm pitch, from an "Atlas OEM Footprint.dxf"). The ORP datasheet gives the pin pitch as 2.3 mm and the pin width as 1.3 mm, so the even pitch was used. See Questions.
- PCB: 50.8 x 22.86 mm, 4 layers, outline, holes, CN1, barrier, keep-outs and isolation block unchanged from the template. New parts (all top side, isolated area):
  - J1 (94.4, 121.43) rot 90: SMA on the x = 90 short edge, opposite CN1, barrel pointing -x. The barrel sticks out about 5.6 mm past the edge (from the footprint's fab drawing; the BAT Wireless drawing was not checked).
  - U2 (107, 119.13) rot 0: pins 1-5 face J1. Pin 4 (PRB) is level with the J1 centre pin, so ORP_PRB is one straight 0.4 mm F.Cu track about 6.6 mm long.
  - C5 (97.8, 115.8) rot -90 next to U2 pin 3; R5 (106.6, 128) straddles the guard edge.
  - AGND_ISO_guard pours on all 4 layers (priority 1 over GND_ISO): x 90 to 98.6 for y > 117, and x 90 to 106.6 for y > 120.3. They cover J1, the PRB track, U2 pins 4-5 and the probe end. Four AGND_ISO stitching vias. AGND_ISO joins GND_ISO only through R5.
  - Routing: VDD_ISO In2.Cu trunk extended along y = 111 to a via at (99.3, 112) then F.Cu to C5 and U2 pin 3. SDA_ISO on F.Cu along y = 112.6 then B.Cu to the R3/U3 net. SCL_ISO on F.Cu to R4. INT_ISO to J5. U2 GND to the existing GND_ISO via (116, 123.6). No vias under U2. All zones refilled.
- ERC (kicad-cli 10.0.4): **0 errors**, 39 warnings: 10 pin_to_pin (EasyEDA passives with input/unspecified pins, as the template), 9 footprint_link_issues + 9 lib_symbol_issues (easyeda2kicad / EasyEDA2Kicad libraries not registered on this PC), 7 isolated_pin_label (unused CN1 signals SENS_SCK/MOSI/MISO/CS/INT/AIN + VBAT), 4 lib_symbol_mismatch (GND power symbols).
- DRC (kicad-cli 10.0.4, --schematic-parity --refill-zones): **0 errors, 0 unconnected, 0 parity**, 15 warnings: 9 lib_footprint_issues (easyeda2kicad library not registered), 6 silk_over_copper (EasyEDA pin-1 dots on C1, C5, R1, R3, R4, R5).
- STEP: C:\Personal-Agents\shared\handoff\feather_orp\feather_orp_2026-10-26.step (board, holes, CN1, U3, U4). **J1 (SMA), U2 (no model) and the EasyEDA passives are missing**: the BWSMA-KWE-Z001 model the KiCad footprint points to isn't installed on this PC, and the easyeda2kicad 3D folder isn't set up.
- Fab outputs: none.

## Open work
- Design review (design-reviewer) before any fab output, especially the ORP footprint change and the guard pour.
- Set R1 (R_ID) once the ID register exists, and fill in the R_ID silk.
- Get 3D models for J1 (BWSMA-KWE-Z001) and U2 (12 x 11 x about 2.65 mm block would do) and re-export the STEP for the enclosure.
- Check the J1 height and barrel length against the BAT Wireless drawing (C496551).
- Register the easyeda2kicad libraries on this PC (clears 18 ERC and 9 DRC library warnings).
- Assembly note for the BOM/fab notes: the datasheet requires all flux to be washed off after soldering the OEM (ultrasonic, flux remover, or about 20 minutes in alcohol), and clear epoxy only if conformal protection is needed (no coloured potting).

## Questions for Brian
- R_ID: no SENSORS.md exists. The v4-sensor-connector.md table gives 4.7k = type 3 and the previous run picked that for ORP. Create SENSORS.md and confirm ORP = type 3 (4.7k 1 %, C25900), or another value? (conductivity has 1k proposed; DO and the others are still at the 10k placeholder.)
- U2 footprint: use the ORP datasheet pad layout (this board, even 2.3 mm pitch) or the sens1 DXF-derived land pattern? If the DXF is the more trustworthy source, sens1 and this board should be made the same.
- INT_ISO only reaches the J5 test pad (2-channel ADuM1250), so firmware has to poll register 0x07. Same template question as before: change to a 3-channel isolator so the OEM can interrupt the host?
- VDD_ISO is the unregulated NXE1S0303MC output from the 3.0 V VSENS rail, so it sits near 3.0 V, the bottom of the ORP OEM's 3.0-5.5 V range. The Atlas isolation example uses an ADM3260 at 3.9 V. Accept, or move to the VBAT-fed isolated supply being considered for conductivity?
- Stack height: the right-angle SMA on top makes the tallest part about 6.5-8 mm (as on sens1). OK, or change the probe connector?

## Decisions
- 2026-10-25 (Brian): one sensor board per feather; this board is the ORP node, isolated variant, Atlas ORP OEM with an SMA probe input whose shell is AGND_ISO.
- 2026-10-26: placement and guard-pour approach copied from sens1 (same OEM family, same SMA), with U2 at y 119.13 so PRB lines up with the SMA centre pin.
- 2026-10-26: R_ID left at the template placeholder because no SENSORS.md register exists (the previous run's 4.7k was reverted).
- 2026-10-26: ORP OEM land pattern taken from the ORP datasheet v3.3 rather than the sens1 DXF footprint (flagged as a question).
