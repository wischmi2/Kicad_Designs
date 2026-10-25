# Feather water level sensor board - Status

Project: C:\Personal-Agents\worktrees\nrf54l15-feather-branch\Sensor_Boards\feather_water_level\feather_water_level.kicad_pro
Last reviewed: 2026-10-25

**State: SET-UP ONLY (rev 0.1).** Project created from feather_sensor_template (README there: "Starting a new sensor board") and stripped to the non-isolated variant. The sensor circuit is NOT drawn or laid out yet. Not a fab design.

## Summary
- Purpose: water-level node. Sensor is the DFRobot A02YYUW ultrasonic module, UART 9600 on CN1 pins 6/7. The sensor does not touch the water, so the board is non-isolated.
- Planned circuit (decided by Brian 2026-10-25, not drawn yet):
  - VBAT -> 3.3 V buck-boost, EN tied to VSENS (so it only runs while the host switches the sensor on).
  - 2-channel level translation VSENS (3.0 V) <-> 3.3 V with partial-power-down (no back-powering when VSENS is off).
  - TVS + series resistors at the sensor connector.
  - Sensor connector on the x = 90 short edge (type not decided; parts research: C:\Personal-Agents\shared\design\feather_water_level\parts.md).
  - Sensor RX driven from host TX (SENS_TX, CN1 pin 6) so firmware picks the output mode; sensor TX goes to host RX (SENS_RX, CN1 pin 7).
- Existing parts: CN1 Molex 503480-1400, C1 1 uF + C2 100 nF on VSENS, R1 = R_ID (SENS_ID to GND, value still "10k (set per SENSORS.md)", to be assigned). No new parts, so no LCSC lookups this run.

## Current state (2026-10-25)
- Schematic: root + Sensor Connector + Sensor (empty). Isolation sheet deleted. Sensor sheet hierarchical labels VSENS, GND, VBAT, SENS_TX, SENS_RX, wired on the root to global labels of the same names (stub wires on the empty sheet only keep labels from being dangling). CN1 pin 6 net renamed SENS_MOSI -> SENS_TX, pin 7 SENS_MISO -> SENS_RX. SDA, SCL, SCK, CS, INT, AIN left as unconnected global labels (no parts). A PWR_FLAG was added on GND (sensor_connector sheet) because the removed isolation parts were the only GND driver. Title blocks rev 0.1.
- PCB: 50.8 x 22.86 mm, R2.54, 4 layers, same outline/origin/holes as the template. Parts: CN1, C1, C2, R1, H1-H4. ISOLATION_BARRIER, GND_ISO zones and the H1/H2 3.5 mm keep-outs removed; GND pours cover the whole board on all 4 layers (antenna-corner keep-out kept). Silk: B.SilkS "FEATHER WATER LEVEL rev 0.1". Isolation tracks and VSENS/GND stubs to the removed parts deleted.
- H1/H2/H4 are NPTH, H3 plated GND. H1/H2 could be plated GND now that the board is non-isolated; left NPTH as asked.
- ERC (kicad-cli 10.0.4): **0 errors**, 32 warnings: 15 isolated_pin_label (unused CN1 signals + VBAT, and the 5 Sensor-sheet labels), 5 unconnected_wire_endpoint (sensor-sheet stubs), 3 footprint_link_issues + 3 lib_symbol_issues (easyeda2kicad / EasyEDA2Kicad / Connector_FFC-FPC libs not registered), 4 lib_symbol_mismatch (GND), 2 pin_to_pin.
- DRC (--schematic-parity --refill-zones): **0 errors, 0 unconnected, 0 parity**, 5 warnings (3 lib_footprint_issues, 2 silk_over_copper EasyEDA pin-1 dots on R1/C1).
- STEP: C:\Personal-Agents\shared\handoff\feather_water_level\feather_water_level_2026-10-25.step (outline, holes, CN1; passives have no 3D model on this PC). No sensor connector yet.
- Fab outputs: none.

## Open work
- Draw the circuit on the Sensor sheet (buck-boost, level translator, TVS, series resistors, sensor connector) and the GUI placement of symbols; replace the sensor-sheet stubs.
- Choose the sensor connector, place on the x = 90 edge, place and route, refill zones.
- Set R1 (R_ID) from SENSORS.md (does not exist yet) and update the "SENSOR TYPE / R_ID" silk.
- Re-export the STEP once the connector is placed.
- Decide whether H1/H2 become plated GND.

## Decisions
- 2026-10-25 (Brian): non-isolated, UART, circuit as listed above.
- 2026-10-25: CN1 pins 6/7 named SENS_TX / SENS_RX on this board (the feather's own net names for those pins are SENS_MOSI / SENS_MISO; the link is point to point so the name difference does not matter).
