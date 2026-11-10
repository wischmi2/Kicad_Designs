# ReefWatch solar node (nrf54l15_v3) - Status

Project: C:\Personal-Agents\worktrees\nrf54l15-feather-branch\nrf54l15_v3\nrf54l15_v3\nrf54l15_v3.kicad_pro
Last reviewed: 2026-10-23

## Summary
nRF54L15 node (U6) with a 32 MHz crystal (X1) and a chip antenna (AE1).
- Power: nPM1300 PMIC (U2), AEM10330 solar harvester (IC1), and two JST PH 2-pin connectors (U4, U5).
- Interfaces: USB-C (J1), SWD (J3, FTSH-105), JST SH 4-pin sensor connector (CN1, SM04B-SRSS-TB).
- It has the same sheet set as the feather. The image and DRC files in the folder are named "nrf54l15_soil_moisture".

## Current state
- PCB: about 44.38 x 34.00 mm, 4 layers. 57 footprints, 550 track segments, 168 vias, 21 zones. No mounting-hole footprints.
- ERC (2026-10-23): 12 errors, 110 warnings.
  - USB-C D+/D-/SBU pins are unconnected.
  - nPM1300 SHPHLD (pin 15) is unconnected and undriven.
  - U6 P1.00/P1.01 are unconnected.
  - Same VOUT2 PWR_FLAG and C4 errors as the feather.
- DRC (2026-10-23): 1 error and 260 warnings (mostly silkscreen).
  - The error: GND zones 'Mid_2' (In2.Cu) and 'Top' (F.Cu) aren't connected to each other.
- Fab outputs: Gerber\ folder with Gerber.zip, and nrf54l15_v3.drl.
- Enclosure / STEP: none exported.

## Open work
- Stitch or connect the In2 and F.Cu GND zones.
- Clear the ERC errors, or document why they're acceptable.

## Questions for Brian
- Is nrf54l15_v3 the ReefWatch solar node? The files say "soil_moisture", and the repo also has nrf54l15_v4. Which one is current?
- Was this revision fabricated (the Gerber.zip)? If so, should this file treat v3 as frozen?
- Should SHPHLD and P1.00/P1.01 stay unconnected?

## Decisions
- None recorded yet.
