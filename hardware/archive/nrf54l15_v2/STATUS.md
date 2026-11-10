# nRF54L15 v2 - Status

Project: C:\Personal-Agents\worktrees\nrf54l15-feather-branch\nrf54l15_v2\nrf54l15_v2.kicad_pro
Last reviewed: 2026-10-23

## Summary
Earlier revision of the nRF54L15 solar/sensor node (U6) with a 32 MHz crystal (X1) and a chip antenna (AE1).
- Power: nPM1300 PMIC (U2) and an **SPV1040T** solar boost converter (U3). v3 and v4 replace the SPV1040T with the AEM10330. Two JST PH 2-pin connectors (U4, U5).
- Interfaces: USB-C (J1), SWD (J3, FTSH-105), JST SH 4-pin sensor connector (CN1, SM04B-SRSS-TB).

## Current state
- PCB: about 44.38 x 34.00 mm, 4 layers. 62 footprints, 508 track segments, 161 vias, 18 zones. No mounting-hole footprints.
- ERC (kicad-cli 10.0, 2026-10-23): 15 errors, 121 warnings.
  - USB-C D+/D-/SBU pins are unconnected.
  - nPM1300 SHPHLD is unconnected.
  - U6 P1.00/P1.01 are unconnected.
  - R3, R5 and R7 inputs have no driver.
  - Same VOUT2 PWR_FLAG and C4 errors as v3/v4/feather.
- DRC (schematic parity on, 2026-10-23): 0 errors, 280 warnings, 0 unconnected items.
  - 14 net_conflict warnings on the USB-C J1 pads (GND/VBUS): the board nets don't match the schematic.
  - One GND via pair is too close (hole_to_hole). Also 2 dangling tracks and 1 footprint/symbol mismatch. The rest are silkscreen.
- Fab outputs: Gerbers and drill in the folder and in Gerber\Gerber.zip, plus CPL (nrf54l15_v2.csv), BOM (nrf54l15_v2.xlsx) and a schematic PDF.
- Enclosure / STEP: none exported.

## Open work
- None identified. This looks like a superseded revision.

## Questions for Brian
- Was v2 fabricated? Should it be marked frozen or archived, now that v3 is built and v4 is the next revision?
- The J1 net conflicts suggest the PCB and schematic drifted apart after the Gerbers were made. Does that matter for an archived board, or should it be reconciled?

## Decisions
- None recorded here.
