# Feather sensor board template

KiCad 10 template for sensor boards that stack under the nRF54L15 feather. Each node is one feather plus one sensor board in its own enclosure (pH node, salinity node, ...). The two boards are joined by a 14-way 0.5 mm FFC between the two CN1 connectors; the R_ID resistor on the sensor board tells the firmware which board is fitted.

Derived from nrf54l15_feather_sens1 (pH) on 2026-10-25. Current numbers and open questions: STATUS.md.

## What is in the template

| Sheet | Contents | Change per board? |
|---|---|---|
| Sensor Connector | CN1 Molex 503480-1400, C1 1 uF + C2 100 nF on VSENS, R1 = R_ID (SENS_ID to GND) | Only R1's value |
| Isolation | U3 ADuM1250 I2C isolator, U4 NXE1S0303MC isolated DC-DC, C3, C4, R3/R4 4.7k isolated-side pull-ups, J5 INT_ISO test pad | Normally no. Delete it for a non-isolated board |
| Sensor | Empty. Hierarchical labels VDD_ISO, GND_ISO, SDA_ISO, SCL_ISO, INT_ISO | Yes, the sensor circuit goes here |

PCB (origin = outline top-left corner at (90, 110), the same as the feather):
- Outline 50.8 x 22.86 mm, R2.54 corners, 4 layers, same stackup, design rules and net classes as sens1.
- CN1 at (138.475, 121.43), rotation 90, pin 1 at (137.15, 124.68): exactly under the feather's CN1.
- Isolation barrier at x = 124: isolated pours (GND_ISO) end at x 122.5, host pours (GND) start at x 125.5, rule area ISOLATION_BARRIER in between on all 4 layers.
- Sensor placement area: x 90 to about 116 (isolated side), outlined on Dwgs.User. GND_ISO pours already on all 4 layers.
- Antenna-corner keep-out ANTENNA_CORNER_keepout: x 132.15 to 140.8, y 126.40 to 132.86, all copper layers, no tracks, vias or pours. It is the feather's antenna keep-out copied 1:1; the feather's chip antenna sits right above it.
- Holes at the Feather positions, 2.7 mm drill: H1 (92.54, 112.54) and H2 (92.54, 130.32) NPTH with 3.5 mm keep-outs (isolated end); H3 (138.26, 112.54) plated GND; H4 (138.26, 130.32) NPTH (inside the antenna keep-out).

## Starting a new sensor board

1. **Copy the project.** Open feather_sensor_template.kicad_pro in the KiCad project manager and use File > Save As to a new folder under hardware\sensors (for example hardware\sensors\feather_sens2_salinity\feather_sens2_salinity). KiCad renames the project files and keeps the sheet instances working.
   - Fallback by hand: copy the folder (skip any `~*.lck` files), rename the four `feather_sensor_template.kicad_*` files to the new name, and replace the project name inside them: `sed -i 's/"feather_sensor_template"/"<new_name>"/g' *.kicad_sch *.kicad_pro`. The footprint library nickname `feather_sensor_template` (fp-lib-table and the .pretty folder) can stay as it is.
   - Never edit the template itself for a real board.
2. **Set R_ID.** Pick the next free board type in the ID table (docs\notes\v4-sensor-connector.md, "Board ID - pin 11"; the R1 value field says "set per SENSORS.md", the ID register) and set R1's value to it on the Sensor Connector sheet, 1 % tolerance. Update the "SENSOR TYPE / R_ID" text on B.SilkS and record the assignment in the ID table.
3. **Fill the Sensor sheet.** Draw the sensor circuit on sensor.kicad_sch and connect it to the hierarchical labels. Delete the short wire stubs on the labels as you wire them (they only exist so the empty template passes ERC). Place new symbols in the KiCad GUI.
4. **Update the PCB** (Tools > Update PCB from Schematic), place the new parts in the sensor area, put the probe connector on the x = 90 short edge (opposite CN1, so the probe cable leaves the other end of the enclosure), route, refill the zones.
5. **Rename the board.** Title blocks on all sheets, "FEATHER SENSOR <NAME> rev" on B.SilkS, and a STATUS.md for the new board.
6. **Check.** `kicad-cli sch erc` (0 errors) and `kicad-cli pcb drc --schematic-parity --refill-zones` (0 errors, 0 unconnected, 0 parity). Export a STEP to C:\Personal-Agents\shared\handoff\<project>\ for the enclosure.

## Fixed: do not move or change

- **Outline, hole positions and origin.** The boards stack 1:1 on shared standoffs.
- **CN1**: footprint, position (138.475, 121.43), rotation 90 and pinout. Moving it breaks the straight FFC fold and the pin-1-to-pin-1 mapping.
- **Antenna-corner keep-out** under the feather's chip antenna: no copper of any kind there (no pours, tracks, vias, and no parts).
- **H1/H2 NPTH keep-outs** on an isolated board: no copper within 3.5 mm of those holes.
- **Barrier**: nothing crosses x 122.5 to 125.5 on any layer except the isolator and DC-DC packages themselves.
- All parts on the top side. The bottom stays flat (silk only), because it faces nothing and the stack height is set by the tallest top-side part.

## Sensor-board rules (from docs\notes\v4-sensor-connector.md)

1. Pin 1 at the same end on every board; print the FFC type on the silkscreen. For the U-folded cable the contacts end up on opposite faces at the two ends (opposite-side FFC); the 503480 is dual contact, so a same-side cable also works.
2. No I2C pull-ups on the host side of the sensor board. The feather has 4.7k to VSENS on SDA/SCL and 10k on CS and INT. (The isolated side needs its own: R3/R4 in the template.)
3. Fit the ID resistor (pin 11 to GND), 1 %.
4. Run logic from VSENS (switched 3.0 V, 100 mA max, shared with the feather's BUCK2). Use VBAT (pin 13) only for loads VSENS can't carry, behind a local regulator with an enable and sub-uA shutdown.
5. An analog output on pin 10 (AIN) must be buffered and stay within 0 to 3.0 V. It cannot cross the isolation barrier without extra parts.
6. INT (pin 9) is open-drain, active low.
7. All signals are 3.0 V logic. Before VSENS is switched off, firmware sets every CN1 signal to input or low so nothing back-powers the sensor.
8. Pin usage: I2C on 3/4; SPI on 5 to 8; UART on 6/7; SPI and UART can't be combined (shared instance). Leave unused CN1 pins unconnected.

## Isolated (default) vs non-isolated

**Isolated** (Atlas-style probes in a shared tank: pH, ORP, conductivity, DO). Keep the Isolation sheet. The sensor uses VDD_ISO / GND_ISO / SDA_ISO / SCL_ISO only, and the probe connector shell goes to GND_ISO, never host GND.
- INT_ISO only reaches the J5 test pad: the ADuM1250 has two channels (SDA, SCL). For a host interrupt use a 3-channel isolator or poll.
- VDD_ISO is the unregulated NXE1S0303MC output fed from VSENS (about 3.0 to 3.3 V, and it shares the 100 mA VSENS budget). Check it against the sensor's supply range and current. A sensor that needs a regulated or higher rail (for example EZO-EC, 3.3 V min) needs a different isolated supply, such as the VBAT-fed SN6505 + transformer + LDO in sensor-board-conductivity.md.
- Conformal-coat the isolated side; salt air across the gap defeats the isolation.
- **Nylon standoffs and screws at the isolated end (H1/H2) are mandatory.** The feather's H1/H2 (USB end) are plated and tied to feather GND and sit directly above this board's isolated end; metal hardware there would connect feather GND to the probe side. H4 is nylon too (antenna corner). H3 can be metal.

**Non-isolated** (sealed digital sensors that don't touch the water: temperature/humidity, light, pressure, sealed 1-Wire probes):
1. Delete the Isolation sheet (U3, U4, C3, C4, R3, R4, J5) from the root schematic.
2. On the root sheet, change the five global labels on the Sensor sheet pins to the host nets: VDD_ISO to VSENS, GND_ISO to GND, SDA_ISO to SENS_SDA, SCL_ISO to SENS_SCL, INT_ISO to SENS_INT (or rename the hierarchical labels). Keep C1, C2 and R1.
3. Do not add I2C pull-ups (the host has them).
4. On the PCB: delete the ISOLATION_BARRIER rule area and the GND_ISO zones, and stretch the GND zones over the whole board (keep the antenna-corner keep-out). The H1/H2 NPTH keep-outs can go; H1/H2 can be made plated GND if the board needs the extra ground.
5. Remove "ISOLATED SIDE: NYLON STANDOFFS ONLY" from B.SilkS.

## Files

- feather_sensor_template.kicad_pro / .kicad_sch / .kicad_pcb: project, root sheet, board.
- sensor_connector.kicad_sch, isolation.kicad_sch, sensor.kicad_sch: sub-sheets.
- feather_sensor_template.pretty: CN1 footprint (Molex_503480-1400_1x14-1MP_P0.50mm_Horizontal). 5034801400_0.stp: its 3D model (${KIPRJMOD}).
- The EasyEDA passives use the easyeda2kicad library, which isn't registered on this PC yet (library warnings in ERC/DRC, and no 3D bodies for them in STEP exports).
