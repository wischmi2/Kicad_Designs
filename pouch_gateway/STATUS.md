# Pouch gateway - Status

Project: C:\Personal-Agents\worktrees\nrf54l15-feather-branch\pouch_gateway\pouch_gateway.kicad_pro
Last reviewed: 2026-10-28 (pre-fab fixes from the 2026-10-28 design review)
Design notes: C:\Personal-Agents\worktrees\nrf54l15-feather-branch\pouch_gateway\docs\DESIGN_NOTES.md (Rev A)

## Summary
Golioth Pouch BLE to Wi-Fi gateway, Rev A.
- Module: Murata Type 2FR (U1, LBES0ZZ2FR, NXP RW612). Wi-Fi backhaul only.
- Power: USB-C only, with a TLV62569 buck to 3.3 V (U2).
- Interfaces:
  - USB-C (J1)
  - SWD header (J2) and Tag-Connect TC2030 (J6)
  - UART (J4)
  - 8-pin JST PH connector for a 2.0 in Waveshare LCD (J5)
  - Two U.FL connectors (J3 for the main antenna, J7 for an optional second BLE antenna)
  - RESET, ISP and USER buttons, and LEDs
- Sub-sheets: mcu, power, reset_debug, rf, ui_io, usb.

## Current state
- **Not on order yet.** Brian will resubmit to PCBWay once he approves new fab output: standard 4L 1.6 mm, ENIG, stencil. Bare boards only, parts from DigiKey/Mouser, self-assembly.
- PCB: 58.0 x 35.0 mm, 4 layers, 70 footprints, 13 zones. Four M2 mounting holes (H1-H4) on the Waveshare 53 x 30 mm pattern. Outline, holes and connectors unchanged on 2026-10-28.
- ERC (2026-10-28): 0 errors, 195 warnings (140 endpoint_off_grid, 53 lib_symbol_mismatch, 2 unconnected wire endpoints; all cosmetic, unchanged).
- DRC (2026-10-28, --schematic-parity --refill-zones --severity-all): 0 errors, 0 warnings, 0 unconnected, 0 parity.
- STEP: C:\Personal-Agents\shared\handoff\pouch_gateway\pouch_gateway_2026-10-28.step (outline and connectors unchanged; U1 and J1 have no 3D model).
- **Fab files in this folder are stale** (Gerbers, .drl, .gbrjob, pouch_gateway.7z from 2026-10-20, pouch_gateway.csv and the two PCBWay BOM xlsx). They predate the 2026-10-28 fixes and the xlsx/csv are for the old PCBWay turnkey route. Don't upload them. Left in place on purpose; regenerating fab output needs Brian's approval.

### 2026-10-28 pre-fab fixes (review: C:\Personal-Agents\shared\reports\2026-10-28-review-pouch-gateway-prefab.md)
- S3: footprint references are now SW1/SW2/SW3 (were RESET/ISP/USER); the function text RESET/ISP/USER stays on silk as the visible Value field, the SW refs sit inside the switch outlines. Parity 6 -> 0.
- S6 (part): J2 (SWD header) and J4 (UART) marked DNP in schematic and board. J6 Tag-Connect is the debug path.
- S1: +3V3 pour on In2 ("In2 3V3", priority 5) from the L1/C4/C5 corner up the left of U1 to the VCC33 corner; kept about 1 mm off the In2 USB DP/DM lines and clear of the RF lines and U.FLs (In1 stays solid GND). F.Cu +3V3 slab from C6/C12 to U1.26/27, extra vias at L1.2 (2) and between C6 and C12. L1.2 -> U1.26/27 resistance (finite-difference estimate, 35 um Cu, about 1.2 mohm per via): **about 9 mohm (8.7), 5 mV at 576 mA (DPD peak), 4 mV at 469 mA**. Before the fix the same model gives about 280-300 mohm (the old path was one ~115 mm run of 0.2 mm track at 2.45 mohm/mm), i.e. about 160 mV at 576 mA; the review's 92 mohm looks about 3x low. Worst case at U1 is now about 3.24 - 0.005 = 3.23 V vs the 3.14 V minimum. DC estimate only (no pad/solder/module-internal resistance, no load-step droop).
- N3: In1/In2 GND zone clearance 0.5 -> 0.25 mm.
- S2: C2 (100 nF 0402, same part) moved right next to U2.4; its GND pad returns on a 0.3 mm F.Cu track straight to U2.2 under the package. The under-body +5V diagonal is gone; C1/C2 are fed by a 0.5 mm B.Cu track from the +5V feed. R3/C3 +3V3 via moved. +5V F.Cu 0.5 mm, SW_3V3 0.6 mm, L1.2 -> C4/C5 0.8 mm. No new parts.
- N1: D1 reference moved off U2 pin 1, R6 reference moved. R13 (was on J3 pad 1) moved. R12, R21, C11, C16, C17 refs were hidden at first (no free spot within 3 mm); see the silk follow-up below. Silk DRC warnings 16 -> 0.
- S5 (part): stackup copper finish set to ENIG.
- S4: R5 0R stays fitted (direct VBUS link as on the EVK), Brian 2026-10-28. No change.
- LCD stack check (report only, no change): see "LCD clearance" below.

### 2026-10-28 silk follow-up: hidden references made visible
- R12, R13, R21, C11, C16, C17 references are visible on F.SilkS again (0.8 mm high, 0.15 mm stroke), each with a 0.15 mm F.SilkS leader line to its part. Silk only: no copper, no part moved. Text and leaders keep clear of all pads (including J3 pad 1 and the RF pads); leaders cross covered tracks only, no exposed copper.
  - R21: label at (154.2, 81.5), straight leader along y 82.3 from R21 to the label (looks like an underline of TP1, but it is the R21 leader).
  - C17: label at (154.3, 86.5), leader along y 87.3-87.5 from the label to C17 (passes between R23 and C18).
  - R13: label (vertical) at (153.9, 93.9) below-right of J3, leader runs from R13 round the J3 right side.
  - C11: label at (146.4, 76.4) above C15/R7, leader down the right side of C15 to C11.
  - C16: label (vertical) at (148.7, 80.1), leader down past C11's right side to C16.
  - R12: label (vertical) at (140.7, 95.9), short leader to R12.
- DRC (--schematic-parity --refill-zones --severity-all): 0 errors, 0 warnings, 0 unconnected, 0 parity (no silk warnings). Render: C:\Personal-Agents\shared\design\pouch_gateway\silk_2026-10-28.png.
- Leaders in the C11/C16/R13 area are long and bendy because the module/RF area is dense. If Brian wants it tidier, the alternative is moving the R20/R22/R23 reference texts to open space.
- Decision 2026-10-28 (Brian): the LCD mounts in its own holder in the Ledger enclosure, offset from the board as in the 2026-10-24 Fusion model, not stacked on the M2x6 standoffs. The J5/J1 clash found in the "LCD clearance" check above therefore does not apply; that section is kept as a record only.

### LCD clearance (stacked on the shared M2 standoffs, 2026-10-28)
Inputs: shared\design\pouch_gateway\lcd_module\MEASUREMENTS.md (Waveshare STEP): PH2.0 8-pin SMT side-entry on the LCD's back, 5.6 mm tall, body 4.25-12.75 mm in from the LCD's connector end, centred across the short axis over 19.9 mm (y 77.55-97.45 on this board). Standoffs M2 x 6 (Waveshare wiki and STEP), so the LCD back is 6.0 mm above the gateway top and the connector leaves **0.4 mm** above the gateway surface. The LCD can only sit with its back towards the gateway, so its connector end is over either the right (J5) end or the left (J1) end. Gateway heights are datasheet/model values, not measured: J5 4.85 mm (board STEP, per enclosure_ledger\NOTES.md), J1 about 3.2-3.3 mm (enclosure placeholder 3.3), 0603 about 0.9, 0402 about 0.35-0.5, SOT-143 about 1.1.
- **Connector end over the right edge (J5 end): clash.** LCD connector x 155.25-163.75 overlaps J5 (courtyard x 158.4-167.1) over x 158.4-163.75 by y 77.55-94.97 (5.35 x 17.4 mm). 4.85 + 5.6 = 10.45 mm in a 6.0 mm gap: **4.45 mm interference**. C20 (0603) and C21 (0402) are also under it and taller than 0.4 mm. The LCD cable plug would also sit right on top of J5 and its cable.
- **Connector end over the left edge (J1 end): clash.** LCD connector x 114.25-122.75 overlaps J1 (courtyard x 110.2-119.7) over x 114.25-119.69 by y 87.98-97.45 (5.4 x 9.5 mm). 3.3 + 5.6 = 8.9 mm: **about 2.9 mm interference**. FB1 (0603), D1 edge (SOT-143, 0.06 mm overlap), R1/R2 (0402, borderline) and the J6 Tag-Connect pads are also under it; J2 is pads only (DNP).
- Rest of the LCD footprint at 6 mm: fine for the parts outside the connector zone (J5 4.85, L1 about 2.0, KMR2 about 1.9, mated U.FL about 2.4, U1 about 1.6). Only the connector was modelled on the LCD back; other back-side parts were not checked.
- Other consequences of stacking: J6 Tag-Connect can't be used with the LCD fitted (the TC2030 head needs top access), and SW1/SW2/SW3 and D3-D5 are covered (concepts.md 2.4).
- Note: the current Fusion Ledger model (shared\design\pouch_gateway\enclosure_ledger\NOTES.md) does **not** stack them; it mounts the LCD above the gateway, side by side with a 5 mm offset, so this clash does not occur there. The 2026-10-28 task says the LCD sits over the board on the shared standoffs; which is intended needs confirming.
- Options (no connector moved): (1) longer standoffs: LCD connector over J1 with M2 x 10 (about 0.8-1.1 mm margin over J1) or over J5 with M2 x 12 (about 1.5 mm margin); (2) remove the LCD's PH connector and solder the cable to its pads, then M2 x 6 works (cable exit to be checked); (3) side by side as in the Ledger model; (4) next rev: J5 and the LCD connector at opposite ends, or a J5 top-entry/FPC.

### LCD cable W1 (2026-10-29)
- Cable W1 (J5 to LCD, PHR-8 x2 + ASPHSPH24K102 x8) is in the live BOM (sourcing/bom_digikey_mouser_2026-10-28_live.md, section "Cable assembly W1"). Wiring map: C:\Personal-Agents\shared\design\pouch_gateway\lcd_module\cable_W1_wiring.md. All nets match the module; the module schematic numbers its PH connector VCC=8 to BL=1, so the cable is probably reversed (slot n to slot 9-n), not 1:1 as DESIGN_NOTES says. Confirm with continuity first.

### BOM pricing (live, 2026-10-28)
- Files: sourcing\bom_digikey_mouser_2026-10-28_live.md plus DigiKey and Mouser CSVs (copies in shared\design\pouch_gateway\). parts-sourcing, DigiKey/Mouser API.
- U1 LBES0ZZ2FR-580 is available singly: DigiKey 103 in stock, MOQ 1, 23.41 USD (Mouser 0 stock, 266-day lead). Single DigiKey stock line is the supply risk.
- Cheapest split: 36.71 USD for 1 board, 173.14 USD for 5 (excl. J1 and LCD). Add J1 0.19 USD (LCSC only) and the Waveshare LCD 10.99 USD (cable included): about 47.9 USD for 1 board, 229 USD for 5.
- LCSC-only line: J1 TYPE-C-31-M-12 (C165948). Not at DigiKey/Mouser; a DK/Mouser USB-C needs a footprint change.
- Zero stock at the schematic MPN, substitutes chosen (field changes for kicad-designer in the BOM file): D1 PRTR5V0U2X -> Wurth 8240026 (check land pattern), D2 -> Panjit RB521S30-AU, L1 -> SWPA4020S2R2NT (+-30%), C6 -> CL21A226MOQNNNE (Mouser), 10 uF and 100 nF MLCCs, R4, 0R.
- Not checked: other U1 distributors, pad geometry of substitutes, Amazon LCD price.

## Open work
- Brian: decide the LCD stack (standoff length or LCD orientation, see LCD clearance), then approve new fab output (Gerbers + drill only; archive the old fab files first).
- parts-sourcing: done 2026-10-28, see "BOM pricing" above. Open: schematic MPN fields, D1 land pattern check, J1 (LCSC only).
- Review items not done (nice to have): N2 RF width 0.30-0.32 mm, N4 USB as a 90 ohm pair, N5 D4 resistor 470R-1k, N6 CC ESD, N7 long low-speed routes.
- Open items listed in DESIGN_NOTES.md:
  - Antenna part from the HSW2FR FCC filing
  - pSRAM requirement for the Golioth gateway
  - Zephyr console UART pins
- Layout to-dos listed in DESIGN_NOTES.md: physical stackup and 50 ohm CPWG, RF feed length, zone fill, silkscreen cleanup.
- Update the "Layout status" section of DESIGN_NOTES.md.
- Next rev (possible upgrade, Brian 2026-10-24): on-board 1S LiPo charger with power path, JST PH 2-pin battery connector and an "on battery"/battery-voltage signal to a GPIO, for power-cut ride-through. See concepts.md section 8.

## Questions for Brian
- LCD: stacked on the shared M2 standoffs (then pick M2 x 10 with the LCD connector over J1, M2 x 12 over J5, or remove the LCD's PH connector) or side by side as in the Ledger Fusion model? See LCD clearance.
- OK that R13, R12, R21, C11, C16 and C17 have no silk reference (they print on F.Fab)? The alternative is overlapping silk that the fab clips.
- OK to archive the old Gerbers/7z/csv/xlsx and generate new Gerbers + drill for PCBWay?
- (Answered by the 2026-10-28 review: the stackup matches PCBWay standard 4L and RF is about 51-55 ohm; the buck is TLV62569DBVR; the old Gerbers are stale.)

## Decisions
- 2026-10-24 (Brian): the gateway PCB has no battery circuit. It's powered only by USB-C. A battery, if used, needs an external charger/5 V boost module feeding J1, inside the enclosure.
- 2026-10-28 (Brian): Rev A is not on order yet (this replaces "the PCB is fixed and on order"). Fix S1, S2, S3, the J2/J4 DNP part of S6 and the silkscreen (N1); keep R5 0R fitted (S4); order PCBWay standard 4L 1.6 mm, ENIG, stencil. The LCD sits over the board on the shared M2 standoffs.
- 2026-10-24 (Brian): enclosure placement is a shelf or desk with AC (USB) power available all the time. This answers question 1 in shared\design\pouch_gateway\concepts\2026-10-24-enclosure\concepts.md and points to the Ledger concept.
- 2026-10-24 (Brian): printer is a Snapmaker U1 (4-toolhead toolchanger, 270 x 270 x 270 mm, 300 °C nozzle, 100 °C bed, no top cover mentioned). Open to filament suggestions; proposed PETG body + translucent PETG/PCTG light pipe + TPU feet (answers question 8).
- 2026-10-24 (Brian): Rev A is wall (USB-C) power only, with no battery, PowerBoost or pigtail in the enclosure. This replaces the earlier "small pack for power cuts" answer. External USB-C keeps data, and the USB_VBUS 0 ohm stays fitted (closes concepts questions 2, 3 and 7). Checked the schematic: no charger, battery connector or power path on the board.
- 2026-10-24 (Brian): enclosure concept is Ledger (concepts.md section 5). Desk/shelf placement means the wedge stand; no wall keyholes needed.
- 2026-10-24 (Brian): antenna is the Molex 146153 FPC as proposed (concepts question 6).
- 2026-10-24 (Brian): open window over the LCD, no cover lens (concepts question 10).
- 2026-10-24 (Brian): J2 (SWD) and J4 (UART) are not fitted on the build; Tag-Connect J6 is the debug path (concepts question 5).
- 2026-10-24 (Brian): colourway is Abyss navy with a coral key (concepts question 9).
- 2026-10-24: LCD module dimensions taken from Waveshare's STEP model, so no hand measurement is needed (concepts question 4). See shared\design\pouch_gateway\lcd_module\MEASUREMENTS.md. Active area is 1.71 mm off-centre towards the connector end; the module is 4.0 mm thick; the PH connector on its back is 5.6 mm tall.

## Decisions (from DESIGN_NOTES.md)
- 4 layers. M2 holes on the display hole pattern, which replaces the earlier mounting plan.
- SWD selected with a 5.1 kohm pull-down on RF_CNTL_2. RF_CNTL_0 left open (40 MHz XOSC).
- VBUS goes to pin 33 through a 0 ohm resistor that can be removed.
