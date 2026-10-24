# nRF54L15 v4 - Status

Project: C:\Personal-Agents\worktrees\nrf54l15-feather-branch\nrf54l15_v4\nrf54l15_v4\nrf54l15_v4.kicad_pro
Last reviewed: 2026-10-23
Related docs:
- C:\Personal-Agents\worktrees\nrf54l15-feather-branch\solar-analysis-v4.md (rev 2, 2026-10-08)
- C:\Personal-Agents\worktrees\nrf54l15-feather-branch\v4-sensor-connector.md (2026-10-04)

**State: PAUSED (2026-10-23, per Brian).** Brian moved to the Feather form factor, so the active board is now the nRF54L15 feather. v4 is the reference design for the solar fix and the CN1 sensor connector. Both were carried into the feather (netlists checked on 2026-10-23).

## Summary
Next revision after v3.
- Core: nRF54L15 (U6), 32 MHz crystal (X1), chip antenna (AE1).
- Power: nPM1300 PMIC (U2), AEM10330 solar harvester (IC1), two JST PH 2-pin connectors (U4, U5).
- Interfaces:
  - USB-C (J1)
  - SWD (J3, FTSH-105)
  - CN1: the 14-pin Molex 503480-1400 FFC sensor connector, which replaces the JST SH used on v3. This is the host connector pinout defined in v4-sensor-connector.md.
- Enclosure: enclosure\make_enclosure.py, with STL files for the base, lid, window and SWD plug in enclosure\stl\.

## Current state
- PCB: about 44.38 x 34.00 mm, 4 layers. 63 footprints, 753 track segments, 232 vias, 20 zones. No mounting-hole footprints.
- ERC (kicad-cli 10.0, 2026-10-23): 12 errors, 116 warnings. The errors are the same set as v3:
  - USB-C D+/D-/SBU pins unconnected
  - SHPHLD unconnected
  - P1.00/P1.01 unconnected
  - VOUT2 PWR_FLAG and C4
- DRC (schematic parity on, 2026-10-23): 0 errors, 271 warnings, 0 unconnected items, 0 parity issues. Mostly silkscreen, plus 7 lib_footprint_mismatch and 3 isolated copper.
- Changes listed in solar-analysis-v4.md as already applied in the schematic:
  - EN_SLEEP (pin 39) tied to GND
  - MPPT ratio changed to 70 %
  - MPNs added on C40-C43
- Fab outputs: only a gerber job file (nrf54l15_v4-job.gbrjob). No Gerbers yet.
- Enclosure / STEP: there's an enclosure script and STLs. No board STEP in C:\Personal-Agents\shared\handoff\.

## Open work
- None while v4 is paused. The open solar review items have moved to the feather:
  - C41/C42/C43 capacitance under DC bias
  - L11 land pattern
  - Layout check against DS §10

## Questions for Brian
- None open.

## Decisions
- 2026-10-23 (Brian): v4 is paused in favour of the Feather form factor (nrf54l15_feather).

From solar-analysis-v4.md:
- EN_SLEEP goes to GND. MPPT is 70 % (LHL).
- CN1 pinout is fixed on the host; sensor boards adapt to it.
