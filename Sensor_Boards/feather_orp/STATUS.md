# Feather ORP sensor board - Status

Project: C:\Personal-Agents\worktrees\nrf54l15-feather-branch\Sensor_Boards\feather_orp\feather_orp.kicad_pro
Last reviewed: 2026-10-28

**State: LAID OUT AND ROUTED (rev 0.1), not reviewed. 2026-10-28: isolated-supply trial (SN6505B + Wurth 760390015 + LP2985-33, U3 -> ISO1640BDR) is on this board; see the trial section. The U4 NXE1S0303MC notes further down are history.** Copied from feather_sensor_template (isolated variant), with the Atlas Scientific ORP OEM drawn on the Sensor sheet and placed and routed on the PCB. ERC and DRC are clean (0 errors). Not a fab design yet: it needs a design review, the R_ID value and the open questions below answered. No fab outputs have been made.

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

## Isolated supply trial (2026-10-28)
Trial of option (c') from Sensor_Boards\feather_sensor_template\isolated_supply_options.md, so Brian can see the SN6505B transformer supply on a real board before it goes on the template / DO / EC. Commits: 27c8c7d (stage 1 schematic), 5f9f497 (stage 2 footprint), a7d1704 (stage 3 PCB), then stage 4 (exports) and stage 5 (this section).

### What changed
- Isolation sheet: U4 NXE1S0303MC deleted. New: FB1 bead in series with VSENS -> VSENS_DRV; U5 SN6505BDBVR (EN tied to VCC, CLK to GND, internal 420 kHz oscillator); C6 100 nF at VCC, C7 10 uF 16 V at the T1 primary centre tap; T1 Wurth 760390015 (centre-tapped primary and secondary); D1 BAT54C full-wave rectifier; C8 10 uF 25 V + C9 100 nF on VISO_RAW; U6 LP2985-33DBVR (ON/OFF tied to VIN) with C10 10 nF bypass and C11 4.7 uF output; C3 2.2 uF and C4 100 nF kept on VDD_ISO. VDD_ISO is now a regulated 3.3 V.
- U3 ADuM1250 -> ISO1640BDR (project symbol feather_orp:ISO1640BDR, same SOIC-8 footprint). Side 1 (pins 1-4) = isolated / VDD_ISO, side 2 (pins 5-8) = host / VSENS. C12 100 nF added at VCC2. Still 2 channels, INT is poll-only.
- T1 primary pins: U5.D1 -> T1.3 and U5.D2 -> T1.1 (swapped against the TI figure so both route straight; a centre-tapped push-pull is symmetric, so nothing changes electrically).
- New project library items: symbols feather_orp:ISO1640BDR and feather_orp:WE_760390015; footprint feather_orp:WE-PPTI_760390015 from the Wurth datasheet rev 009.002 (2025-10-02) land pattern: pads 1.12 x 0.96 mm, rows 9.14 mm centre to centre, 2.54 mm pitch, pins 1-2-3 primary (2 = CT), 6-5-4 secondary (5 = CT). The Wurth STEP 250-1109 is in feather_orp.3dshapes, aligned with offset 5 / -3.24 / 0 and rotate -90 / 0 / 0 (checked in a 3D render: leads sit on the pads, 4.2 mm tall). The datasheet's dimension view and land-pattern view number the pins mirrored (1 bottom-left vs 1 top-left); the land-pattern view was used. Either way only 1<->3 and 4<->6 swap, which is harmless for this circuit.
- PCB: T1 at (124, 124) rot 180 straddles the barrier (primary pads x 128.57, secondary x 119.43). Host cluster U5/FB1/C6/C7 at x 129.4-133.8, y 119.4-131, clear of the antenna keep-out (x >= 132.15 and y >= 126.4). Isolated cluster D1/U6/C8-C11/C3 at x 107.8-118.5, y 122.6-132.3. U3 rotated to rot 0 and re-routed on both sides. Host I2C (SENS_SDA/SCL) now runs on B.Cu from vias next to CN1 to vias next to U3. VSENS is one F.Cu bus (CN1.2 -> FB1, C1, C2, C12, U3.8); C1/C2 moved onto it. VDD_ISO from U6 runs on In2 up x = 121.8 to the existing y = 111 trunk. CN1, the outline, holes, barrier rule area, antenna and NPTH keep-outs and the AGND guard pours are unchanged. Zones refilled.
- The board was updated with KiCad Python (pcbnew) from a kicad-cli netlist, not the MCP sync tool. Warning for the next board: pcbnew Board.Save() to a folder whose .kicad_pro was not loaded overwrites that .kicad_pro with default rules (min hole 0.3, clearance 0.2 ...). It happened once here; the .kicad_pro was restored from git before any commit. Load the board next to its own .kicad_pro, save to a scratch copy, and copy only the .kicad_pcb back.

### Parts (MPNs in the schematic fields; LCSC left empty)
| Ref | Part | MPN | Package |
| --- | --- | --- | --- |
| U5 | TI push-pull transformer driver | SN6505BDBVR | SOT-23-6 |
| T1 | Wurth WE-PPTI push-pull transformer | 760390015 | 6.73 x 10.2 x 4.19 mm SMD |
| D1 | Nexperia dual Schottky, common cathode | BAT54C,215 | SOT-23 |
| U6 | TI LDO, 3.3 V, 16 V in | LP2985-33DBVR | SOT-23-5 |
| U3 | TI I2C isolator | ISO1640BDR | SOIC-8 |
| FB1 | Murata bead, 220 ohm at 100 MHz | BLM18PG221SN1D | 0603 |
| C6, C9, C12 | 100 nF 16 V X7R | Murata GRM155R71C104KA88D | 0402 |
| C7 | 10 uF 16 V X5R | Murata GRM21BR61C106KE15L | 0805 |
| C8 | 10 uF 25 V X5R | Murata GRM21BR61E106KA73L | 0805 |
| C10 | 10 nF 50 V X7R | Murata GRM155R71H103KA88D | 0402 |
| C11 | 4.7 uF 10 V X5R | Murata GRM188R61A475KE15D | 0603 |

- **DigiKey/Mouser stock is not verified.** DigiKey returned 403 and Mouser timed out from the agent, and no DigiKey/Mouser API keys are configured. Wurth lists 760390015 as active ("expected lifetime > 10 years"). Send the table to parts-sourcing before ordering.
- Wurth's current datasheet gives the turns ratio as **1:2** (N1+N2 : N3+N4), 475 uH min, 11 V-us, 2500 Vac, -40 to +125 C, AEC-Q200. TI's SN6505 table lists it as 1:2.1. The numbers below use 1:2 for the minimum and 1:2.1 for the maximum.

### Electrical numbers (datasheet maxima unless noted)
- V-us: SN6505B fmin 363 kHz, VCC max 3.15 V (VSENS 3.0 V + 5 %): 3.15 / (2 x 363 kHz) = 4.3 V-us against the 11 V-us rating. Magnetising current about 3.15 V x 1.38 us / 475 uH = 9 mA peak.
- VISO_RAW (the LDO input) at VSENS 2.85 V (BUCK2 - 5 %):
  - 30 mA load (EC class): primary about 2 x 30 / 0.9 = 67 mA; drops in FB1 (about 0.1 ohm, bead DCR not checked) + SN6505 RON 0.31 ohm + half primary 0.175 ohm = about 40 mV, so VP about 2.81 V; VS = 2 x 2.81 x 0.97 = 5.45 V; minus BAT54C 0.50 V and about 9 mV of winding = **about 4.9 V** (5.2 V at 1:2.1).
  - ORP load, about 8 mA (OEM 3.5 mA + ISO1640 side 1 + 2 x 0.7 mA pull-ups + LDO): VS about 5.5 V, minus 0.40 V = **about 5.1 V**.
  - LP2985 needs 3.3 V + 0.225 V (dropout at 50 mA, full temperature) = 3.53 V, so there is at least **1.4 V of headroom** at VSENS 2.85 V. Regulation would hold down to about VSENS 2.1 V, below the SN6505 UVLO (2.25 V rising, 1.7 V falling), so the UVLO sets the minimum.
- No-load maximum: 3.15 V x 2.1 x 1.02 = 6.75 V before the diode, **about 6.6 V** at VISO_RAW, against the LP2985 16 V maximum (ON/OFF is tied to VIN and is rated to VIN too). C8 is 25 V, C9 16 V.
- LP2985 dissipation: at most (5.2 - 3.3) V x 30 mA = 57 mW at 30 mA; 15-30 mW at ORP load.
- VSENS current (estimate, efficiency not measured): ORP about 25-35 mA (about 40 mW at VISO_RAW at an assumed 50-60 % light-load efficiency, plus SN6505 1.4 mA max and ISO1640 side 2 up to 7.8 mA); about 70 mA at a 30 mA load. Both under the 100 mA LDSW1 limit. The old NXE1S0303MC drew about 65 mA at ORP load.
- ISO1640 side 2 VOL2 is 0.4 V max into the nRF (VIL 0.9 V at 3.0 V), which fixes review item X5. Side 1 VCC1 needs 3.0 V or more and now gets a regulated 3.3 V.

### Isolation and creepage
- T1 primary-to-secondary pad gap: **8.02 mm** (pad inner edges at x 119.99 and 128.01). Both pad rows are 2.6 mm outside the barrier rule area (x 122.6-125.4). T1 is rated 2500 Vac (functional insulation, 400 Vrms working voltage per Wurth).
- Smallest host-to-isolated copper gap on the board is still **3.00 mm**: U3 (ISO1640, SOIC-8) pad to pad, and the GND / GND_ISO planes on F.Cu, In1 and B.Cu (zone edges at x 122.5 and 125.5). In2: 3.36 mm (new VDD_ISO track at x 121.8 to the host GND plane). Same as the template.
- Measured with a bounding-box script over pads, tracks, vias and zone fills on every copper layer (conservative).

### Area and height
- Old U4: 12.7 x 10.4 = 132 mm^2 straddling the barrier (plus C3).
- New: T1 courtyard 10.8 x 7.2 = 78 mm^2 on the barrier; host cluster about 45 mm^2; isolated cluster about 60-70 mm^2 in space that was free (x 108-118, y 125-132). So the block uses roughly **180-190 mm^2 against 132 mm^2**, but less of the barrier itself. It fits without moving CN1, U2 or J1.
- Tallest part on the isolated side: **T1, 4.19 mm max** (U4 was 4.36 typical, 4.71 max), straddling the barrier. Everything else in the block is 1.45 mm or less. The tallest part on the board is still the SMA J1, 9.5 mm (not in the STEP, no model).

### ERC / DRC after the trial (kicad-cli 10.0.4)
- ERC: **0 errors**, 38 warnings: 10 pin_to_pin (EasyEDA passives), 9 footprint_link_issues + 8 lib_symbol_issues (easyeda2kicad, EasyEDA2Kicad and Connector_FFC-FPC libraries not registered on this PC), 7 isolated_pin_label (unused CN1 signals), 4 lib_symbol_mismatch.
- DRC (--schematic-parity --refill-zones): **0 errors, 0 unconnected, 0 parity**, 25 warnings: 9 lib_footprint_issues (easyeda2kicad), 9 silk_overlap (C4's EasyEDA silk outline against U3 and R3, now that C4 sits next to U3 pin 1), 7 silk_over_copper (6 EasyEDA pin-1 dots as before, plus C4 silk on an R3 pad). The reference text of the new 0402/0603 caps and FB1 is hidden (no room).

### Exports
- Renders in C:\Personal-Agents\shared\design\feather_orp\iso_supply_trial\: feather_orp_iso_3d_corner.png, feather_orp_iso_3d_top.png, feather_orp_iso_3d_bottom.png, feather_orp_iso_Fcu_silk_top.png, feather_orp_iso_Bcu_silk_bottom.png, feather_orp_iso_In2.png. The 2D ones are black-and-white copper + silk, cropped to x 104-141.
- STEP: C:\Personal-Agents\shared\handoff\feather_orp\feather_orp_2026-10-28.step. Outline and CN1 unchanged; T1 now has a model; J1, U2 and the EasyEDA passives still have no model.

### What to copy to the template, DO and EC
- The Isolation sheet as it is now (it was written by script, so copy the file and re-annotate, or redraw it in the GUI), the symbols ISO1640BDR and WE_760390015, the footprint WE-PPTI_760390015 and the STEP in feather_orp.3dshapes (rename the library to each board's own).
- The PCB block: T1 at (124, 124) rot 180, the U5 cluster at x 129-134, U3 at rot 0 with the B.Cu host I2C routing to CN1, the VSENS bus, and VDD_ISO on In2 at x 121.8. DO and EC have the same CN1, barrier and U3 positions; check that their U2/R5/C5 sit where ORP's do before copying the isolated cluster (x 108-118, y 122-132).
- EC: re-check D1 and the LP2985 at its 26 mA peak (the numbers above already use 30 mA).

### Bench-test first (before the other boards go to fab)
1. VISO_RAW and VDD_ISO at VSENS 2.85 / 3.0 / 3.15 V and loads of 0 / 5 / 30 / 50 mA (no-load VISO_RAW must stay well under 16 V; expect about 6.6 V).
2. Primary current shape at the SN6505 D1/D2 pins (no saturation at 3.15 V), and start-up into C7 and the LDO.
3. Ripple on VSENS at CN1 and on the feather's VDDIO, with and without FB1 (FB1 can become a 0R if it does nothing).
4. VSENS current at ORP load against the 100 mA LDSW1 limit, and the efficiency.
5. I2C through the ISO1640 at 100 kHz: VOL on both sides with the 4.7k pull-ups.
6. T1 and LDO temperature at a 30 mA load.

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
- Isolated supply trial: OK with the layout (renders in shared\designeather_orp\iso_supply_trial)? If so the template, DO and EC get the same block. Bench-test the supply first (list in the trial section)?
- R_ID: no SENSORS.md exists. The v4-sensor-connector.md table gives 4.7k = type 3 and the previous run picked that for ORP. Create SENSORS.md and confirm ORP = type 3 (4.7k 1 %, C25900), or another value? (conductivity has 1k proposed; DO and the others are still at the 10k placeholder.)
- U2 footprint: use the ORP datasheet pad layout (this board, even 2.3 mm pitch) or the sens1 DXF-derived land pattern? If the DXF is the more trustworthy source, sens1 and this board should be made the same.
- INT_ISO only reaches the J5 test pad (2-channel ADuM1250), so firmware has to poll register 0x07. Same template question as before: change to a 3-channel isolator so the OEM can interrupt the host?
- VDD_ISO is the unregulated NXE1S0303MC output from the 3.0 V VSENS rail, so it sits near 3.0 V, the bottom of the ORP OEM's 3.0-5.5 V range. The Atlas isolation example uses an ADM3260 at 3.9 V. Accept, or move to the VBAT-fed isolated supply being considered for conductivity?
- Stack height: the right-angle SMA on top makes the tallest part about 6.5-8 mm (as on sens1). OK, or change the probe connector?

## Decisions
- 2026-10-28 (Brian): trial option (c') on this board with the Wurth 760390015 (DigiKey/Mouser part) instead of the CM0601S, and U3 -> ISO1640BDR with the host on side 2.
- 2026-10-25 (Brian): one sensor board per feather; this board is the ORP node, isolated variant, Atlas ORP OEM with an SMA probe input whose shell is AGND_ISO.
- 2026-10-26: placement and guard-pour approach copied from sens1 (same OEM family, same SMA), with U2 at y 119.13 so PRB lines up with the SMA centre pin.
- 2026-10-26: R_ID left at the template placeholder because no SENSORS.md register exists (the previous run's 4.7k was reverted).
- 2026-10-26: ORP OEM land pattern taken from the ORP datasheet v3.3 rather than the sens1 DXF footprint (flagged as a question).
