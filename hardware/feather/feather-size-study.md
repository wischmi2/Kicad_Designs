# nRF54L15 feather: moving to the standard Feather size

Study date: 2026-10-24, by kicad-designer. Read-only: no project files were changed.
Method: parsed nrf54l15_feather.kicad_pcb with KiCad 10 pcbnew Python, and Adafruit's own Eagle file for the Feather dimensions.
Baseline: git tag `feather-pre-resize` (66.04 x 25.40 mm, 64 footprints).

**Short answer:** 50.8 x 22.86 mm is possible, but it means re-placing every part and re-routing the whole board. Space isn't the limit; the board edges are. CN1, U5 and J3 can't keep their current role and form.

## 1. Feather mechanical spec

Sources:
- learn.adafruit.com/adafruit-feather/feather-specification
- "Adafruit Feather M0 Basic rev C.brd" (github.com/adafruit/Adafruit-Feather-M0-Basic-Proto-PCB), XML parsed for exact numbers.

Coordinates: origin at bottom-left, USB end at x = 0, y upward. All in mm.

- **Outline:** 50.80 x 22.86, four R2.54 corners. The M0 has an optional 0.508 mm notch on the USB edge (y 8.89 to 13.97) for micro-USB.
- **16-pin row:** y = 1.27, 2.54 pitch, pins at x = 6.35 to 44.45.
  - Order from the USB end: RST, 3V3, AREF, GND, A0, A1, A2, A3, A4, A5, SCK, MOSI, MISO, RX, TX, then the free 16th pin (GND on the M0).
  - Pads: 1.0 drill / 1.68 pad.
- **12-pin row:** y = 21.59, pins at x = 16.51 to 44.45.
  - Order: BAT, EN, USB (VBUS), D13, D12, D11, D10, D9, D6, D5, SCL, SDA.
  - The rows are 20.32 (0.8") apart and both end at x = 44.45.
- **Mounting holes:** (2.54, 2.54), (2.54, 20.32), (48.26, 2.54), (48.26, 20.32).
  - The USB-end pair is plated on the M0: 2.5 drill, 3.2 pad. The far pair is NPTH 2.54. That makes them M2.5.
- **USB:** centred on the left short edge (M0 micro-USB at x 4.445, y 11.43).
- **Battery JST PH:** about x 10.8, y 19.3, top-left, facing the 12-pin edge.

## 2. What the current board already follows

Almost nothing.

- **Headers:** no header footprints and no Feather pinout. The external interfaces are J1, CN1, J3, U4 and U5.
- **J1 USB-C:** on the left short edge, centred (y 122.70). Courtyard x 90.1 to 98.5, flush with the edge. This matches the Feather convention.
- **U4/U5 (JST PH, through-hole, bottom):** both in the left corners next to J1, facing the left edge.
- **CN1:** right short edge, top (y 110.7 to 120.0).
- **AE1:** right edge, bottom, with a 3.1 x 5.9 all-layer keepout (151.93,125.78 to 155.05,131.69).
- **J3:** on the bottom near the top edge (x 136 to 143.6).
- **Width:** 25.40, which is 2.54 too wide.
- **GPIO:** U6 uses 14 GPIOs and has 17 free. That's enough for the Feather's 21 signals if SCK/MOSI/MISO, SDA/SCL, A0 and three D pins reuse the existing SENS_* nets.
  - A0 to A5 need six AIN-capable pins. Those are only on port 1 and some are taken, so the pin map needs checking.
  - Pin map: 3V3 = VDDIO, BAT = VBAT, USB = VBUS, RST = nRF54_RESET. EN needs a decision: nPM1300 SHPHLD or a buck enable.

## 3. Area budget (courtyard area)

| | Current 66.04 x 25.40 | Feather 50.8 x 22.86 |
|---|---|---|
| Gross area per side | 1677 mm² | 1156 mm² (after corner rounding) |
| Header rows | none | 103 + 77 = 180 mm², both sides (through-hole) |
| 4 holes (3.2 pad + 0.5 keep) | none | about 55 mm² |
| Antenna keepout (estimate, about 5 x 13 at the far end) | 18 mm² now | about 65 mm² |
| **Usable per side** | about 1660 mm² | **about 855 mm²** |
| Top courtyards | 335 mm² (20 % fill) | |
| Bottom courtyards | 148 mm² (9 % fill) | |

Biggest courtyards:
- **Top:** J1 65.5, U6 49.3, CN1 39.4, IC1 38.9, U2 36.1, SW1 15.8, C43 10.5, L11 7.5 mm².
- **Bottom:** J3 50.3, U4 49.1, U5 49.1 mm². U4/U5 are through-hole, so they also block about 98 mm² of the top.

Verdict:
- Everything as it is now would fill about 57 % of one side, or about 28 % split across two sides. On area alone it fits.
- The edges are the real limit. Long edges go to the headers, the left edge to USB-C plus the battery JST, and the right edge to the antenna. That leaves no edge for CN1, U5 or a horizontal J3.
- With CN1 dropped, J3 replaced by Tag-Connect and U5 removed, the parts need about 360 mm². That fits on the top side between the header rows (x about 8 to 44, about 16 mm usable height, about 576 mm²) at roughly 40 % fill, which is comfortable on 4 layers.
- Keep the bottom side close to empty for breadboard and FeatherWing use. Today all three bottom parts are tall connectors.

## 4. Blockers, part by part

- **CN1 (Molex 503480-1400, 9.4 x 4.3):** it needs an edge for the cable and none is left.
  - Its 14 pins map onto Feather pins: GND, SDA/SCL, SCK/MOSI/MISO, CS/INT/ID to D pins, AIN to A0, VBAT to BAT.
  - VSENS is the gap. It's a switched nPM1300 output (U2 pin 29), so it needs the free 16th pin or has to go to 3V3.
  - Dropping CN1 turns sens1 into a FeatherWing and reverses the "CN1 pinout fixed on the host" decision.
- **J3 (FTSH-105 SWD, 50 mm², bottom):** bottom parts clash with breadboards (2.5 mm header standoff) and Wing doublers. Only 5 pins are used: VDDIO, SWDIO, SWDCLK, RESET, GND.
  - Replace with a Tag-Connect TC2030-NL (about a third of the area; check the keepout on the Tag-Connect drawing) or test pads. RST is already on the header.
- **U4 (VBAT JST PH):** can go to the standard top-left Feather spot, between hole (2.54, 20.32) and the 12-pin row at x about 15.2.
- **U5 (SOLAR_5p5V JST PH, into IC1):** has no edge position. Options: drop it and bring solar in on a header pin or pads; use a small JST SH/ZH inside the board; or put it on the bottom (breadboard clash).
- **RF chain (AE1 2450AT18A100E, RF1 U.FL-type, R11 FM8625H RF switch, matching network):**
  - Must sit at the far short edge (x 45.7 to 50.8), between holes (48.26, 2.54) and (48.26, 20.32), next to header pins at x 44.45.
  - Risks: screws detuning the antenna (use the NPTH far holes and nylon hardware), and any Wing stacked over the antenna.
  - **To do:** check the current 3.1 x 5.9 mm keepout against the Johanson datasheet ground clearance. The study couldn't read the PDF text.
  - The cluster is about 8 x 4 mm today (x 142 to 150, y 129 to 133) and could move as one block.
- **Inductors (10, not 11):**
  - L2, L3, L5, L6, L8: 0201 RF. L4: 0402 ferrite.
  - Power: L7 (4.7 µH, nRF DC/DC), L9/L10 (2.2 µH, nPM1300 bucks), L11 (10 µH, AEM, 2.5 x 2.0).
  - None is a size blocker.
- **AEM10330 layout (DS §10, from solar-analysis-v4.md §3.5):** no copper under L11 on inner or bottom layers; short, wide LIN/LOUT; C40/C42/C43 close to the IC with a direct return to the EP; C41 close to pin 13; 0.4 to 0.5 mm STO trace; keep the IC1 EP via array. This rules out bottom parts under L11 and needs the AEM loop kept compact.
- **IC1 and U2:** fit in the middle; not blockers. Check heat at full charge current on the smaller copper area.

## 5. Options

Any width change to 22.86 mm plus header rows along the long edges forces nearly all of the placement to move. Assume all 1055 track segments and 213 vias are ripped up and the zones rebuilt. Local clusters can move as routed blocks: RF chain, U6 decoupling and crystal, nPM1300 buck loops, AEM loop.

| Option | What changes | Effort | Main risk |
|---|---|---|---|
| **(a) True Feather**, 50.8 x 22.86, headers, 4 M2.5 holes, everything on top | Drop CN1 (sens1 becomes a Wing), TC2030 for SWD, U4 top-left, rework U5 | about 3 to 4 days plus schematic edits | Antenna near holes and under Wings; tight AEM loop; solar input |
| **(b) Feather outline, keep connectors** | CN1, J3, U5 to the bottom or interior | about 3 days | Breaks breadboard and doubler use; no CN1 cable path past a Wing. Not recommended. |
| **(c) Feather-compatible but longer**, 22.86 x about 60 to 66 | Standard header rows and USB-end holes, far holes at x 48.26 for Wing alignment; extra 10 to 15 mm holds antenna, RF1, CN1 and U5 at an edge | about 2 to 3 days | Lowest RF and solar risk; won't fit standard Feather cases; overhangs Wings and doublers |

Common to all options:
- Hole size (M2.5 per spec) and plated vs NPTH.
- Confirm the Feather pin map.
- New STEP for fusion-enclosure afterwards.
- The existing Gerbers and 7z become stale.

## Decisions needed from Brian

1. Which option: (a), (b) or (c)?
2. CN1: drop it (sens1 becomes a Wing), keep it (option c), or keep it and also bring its signals out on the headers?
3. VSENS: free 16th header pin, or tie to 3V3?
4. Solar input if U5 goes: header pin, pads, or small JST SH/ZH?
5. SWD: Tag-Connect TC2030-NL or test pads?
6. Feather EN pin: nPM1300 SHPHLD or a buck enable?
7. For option (c): final length?

## Found along the way

- **Possible schematic bug:** SENS_MISO is on two U6 pins, pad 11 and pad 15.
