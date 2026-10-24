# XIAO pogo stack - Status

Project: C:\Personal-Agents\worktrees\nrf54l15-feather-branch\xiao_breakout\xiao_breakout\xiao_breakout.kicad_pro
Last reviewed: 2026-10-23

## Summary
Breakout carrying three XIAO module footprints: nRF54L15 (U1), nRF54LM20A (U2) and nRF52840 (U3). Footprints come from xiao.pretty.

## Current state
- Schematic: one sheet with the three XIAO symbols. Most pins are not wired.
- PCB: about 76.90 x 60.10 mm, 2 layers. 3 footprints. **No tracks, vias or zones.** No pogo pin or connector footprints.
- ERC (2026-10-23): 102 errors, all unconnected pins on the XIAO symbols (D0-D10, SWD, RST, GND and others). 6 warnings.
- DRC (2026-10-23): 0 errors, 76 warnings (silkscreen and text height).
- Fab outputs: none. There's an older xiao_breakout_drc_violations.json in the folder.
- Enclosure / STEP: none exported.

## Open work
- Define the circuit and connectors. The board is at the placement stage only.

## Questions for Brian
- What should the pogo stack do? For example, a programming/test jig with pogo pins to the XIAO castellations, or a breakout header board.
- Which XIAO modules need to stay on it (all three)?
- Is this project still active?

## Decisions
- None recorded yet.
