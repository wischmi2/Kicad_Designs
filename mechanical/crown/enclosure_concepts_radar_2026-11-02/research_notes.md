# Research notes (stage 1), water level node radar enclosure, 2026-11-02

Working notes. The finished write-up is `concepts.md` in this folder.

## What was read (local files)
- Review of the board (B3, N6, N8, N10, point 5): `C:\Personal-Agents\shared\reports\2026-11-02-review-feather-water-level.md`
- Board status and XM125 facts: `Sensor_Boards\feather_water_level\STATUS.md`, `xm125_notes.md`
- CN1 doc: `Sensor_Boards\CN1_SENSOR_CONNECTOR.md`
- Old ultrasonic concepts (use, containers, family rules only): `...\feather_water_level\enclosure_concepts\concepts.md`
- Tidemark build notes (parameters, hardware, print rules): `...\nrf54l15_feather\enclosure_tidemark\NOTES.md`, `tidemark_decisions.md`
- Ledger gateway notes: `...\pouch_gateway\enclosure_ledger\NOTES.md`
- Feather board file (read only): positions of J1, J3, U4, U5, SW1, LED1, AE1, H1 to H4

## Feather positions I used (board coordinates minus the x=90, y=110 corner = fx, fy)
| Part | Board xy | fx, fy | Note |
| --- | --- | --- | --- |
| J1 USB-C | 95.32, 121.43 (rot -90) | 5.3, 11.4 | mouth at the x=90 edge |
| U5 solar JST | 101.95, 116.42 | 12.0, 6.4 | mouth faces the y=110 edge; unused on this node |
| U4 battery JST | 101.95, 126.44 (rot 180) | 12.0, 16.4 | mouth faces the y=132.86 edge, the same edge as AE1 |
| J3 SWD header | 108.85, 128.6 | 18.9, 18.6 | 6.0 mm tall is an assumption (Tidemark notes) |
| SW1 | 116.4, 130.77 | 26.4, 20.8 | roof key |
| LED1 | 120.6, 127.6 | 30.6, 17.6 | light pipe |
| AE1 | 134.67, 130.08 (rot -90) | 44.7, 20.1 | keep-out fx 42.15 to 50.8, fy 16.4 to 22.86 |
| H1 H2 | 92.54, 112.54 / 130.32 | 2.5, 2.5 / 20.3 | |
| H3 H4 | 138.26, 112.54 / 130.32 | 48.3, 2.5 / 20.3 | |
| Radar centre (A121) | 106.5, 121.43 | 16.5, 11.4 | module body x 98.7 to 117.3 (fx 8.7 to 27.3), y 113.9 to 128.9 |

Consequences:
1. Radar and antenna are 28 mm apart along the board, at opposite ends. Good for any placement that keeps the battery away from the FFC end.
2. SW1 (fx 26.4) and LED1 (fx 30.6) face up in a horizontal stack. Nothing may sit over fx 22.7 to 32 on the roof, which limits a battery on top of the feather to fx 0 to about 20.
3. The battery connector U4 is on the AE1 side edge, at the USB end. A battery lead from the far side has to cross the board.

## Radome numbers (derived here)
- Wavelength at 60.5 GHz: 4.955 mm in air.
- Half wavelength in the plastic: t = 4.955 / (2 x sqrt(er)).
  - er 2.675 (PETG at W-band, a proxy): 1.515 mm.
  - er 2.4: 1.60 mm. er 3.0: 1.43 mm.
  - Chosen window: 1.50 mm (10 layers of 0.15 mm). The second order (n = 2) is about 3.0 mm.
- Air gap n x 2.5 mm: 2.5 mm for n = 1 (lambda/2 in air is 2.48 mm).
- Beam: HPBW 65 deg and 53 deg, so half angles 32.5 deg (tan 0.637) and 26.5 deg (tan 0.499). Which plane lines up with which module axis is UNVERIFIED.

## External sources (looked up, search summaries unless noted)
| Source | What it gave |
| --- | --- |
| University of Arkansas thesis, free-space W-band (75 to 110 GHz) measurement of 3D-printed plastics: https://scholarworks.uark.edu/eleguht/85 | PETG er about 2.675, loss tangent below about 0.045, stable over the band. A proxy only: 60 GHz is outside 75 to 110 GHz. I read only the search summary, not the thesis |
| Springer/DOAJ papers surfaced by the same search (PETG with ceramic filler; X-band infill study) | Filler raises er by about 50 %. Infill density changes the dielectric behaviour, so the window must be 100 % solid |
| Acconeer tank level reference app: https://docs.acconeer.com/en/latest/ref_apps/a121/tank_level.html (fetched) | Range 3 cm to 23 m sensor to liquid. Sensor mounted at the top; free space in front during calibration. It says nothing about lids, covers, condensation, tilt or wall distance |
| Acconeer tank level use case: https://docs.acconeer.com/en/latest/use_cases/tank_level.html (search summary) | Advises a lens or hyperbolic reflector to narrow the field of view and cut wall reflections, metal or plastic tank |
| Mouser-hosted Acconeer tank level brief (older XM132 module through a PP lid): https://www.mouser.lt/pdfDocs/refappbrieftanklevel.pdf (search summary) | Radar worked through a plastic lid with the lens taped to the lid. Older platform, so a rough guide only |
| Vega, measurement through glass: https://vega.com/company/blog/2017/measurement-through-glass | Inclined windows deflect interfering reflections; 26 GHz needs about 20 deg, 80 GHz needs far less. No 60 GHz figure found |
| Icon Process Controls radar datasheet (search summary) | An inclined plastic cover helps condensation drip away; keep condensation from settling between sensor and cover |
| Radar level gauge patent US 6,629,458 (search summary) | A radome shaped to lead condensate away by gravity |
| Johanson 2450AT18A100E: I could not find a keep-out distance for a battery | A module vendor (Microchip) gives more than 7 mm clear in all directions for a chip antenna. That is a generic figure. The 15 mm plastic-only rule in the Tidemark notes is the one I used |
| LiPo size codes: sellers read 603450 as 6.0 x 34 x 50 mm; 603450 listed at 1000 to 1200 mAh; 502030 at 250 mAh; 602030 conflicting (300 to 500 mAh) | Capacities are not fixed by the code. All capacities in this folder are rough, UNVERIFIED |

## Gaps
- No PETG permittivity at 60 GHz. The window thickness must be set by a coupon test.
- No Acconeer figure for the A121 gain outside the half-power cone.
- No lid-thickness guidance for the A121 or XM125.
- The XM125 I2C distance detector may not offer the A121 tank level app. UNVERIFIED.
