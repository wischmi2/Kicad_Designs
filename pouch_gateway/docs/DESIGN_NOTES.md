# pouch_gateway — Rev A design notes

Golioth Pouch BLE→Wi-Fi gateway. Murata Type 2FR (LBES0ZZ2FR, NXP RW612), Wi-Fi backhaul only, USB-C power only.
Sources: [DS] Murata SP-ZZ2FR Rev 5.1 · [EVK] LBES0ZZ2FR-EVK rev A schematic + BOM · [RW] NXP RW612 DS Rev 9.0.

## Symbol
pouch_gateway.kicad_sym : LBES0ZZ2FR — all 140 pins verified name-for-number against [DS] Table 8 (0 mismatches).

## Power
- VCC33 (26, 27) 3.14–3.46 V; feeds VPA, VBAT, AVDD33_USB internally [DS].
- Current [RW §11.5 @3.3 V]: max 469 mA (5 GHz MCS7 max power, MCU+BLE active); DPD peak 576 mA.
  2.4 GHz TX @20 dBm 261 mA; Wi-Fi RX ~63–74 mA; BLE TX 0 dBm 46 mA.
- [EVK] uses an LDO (XC6227C331, 700 mA) from 5 V. Rev A plan: 5 V→3.3 V buck ≥1 A (thermal margin in an enclosure). LDO is an acceptable fallback.
- Decoupling: [EVK] 10 µF at VCC33 (C11), 10 µF at VDD18 (C12). Rev A adds 22 µF bulk + 100 nF at VCC33, and 100 nF per VIO pin.
- VIO_1/2/3/5/6 + VIO_RF → 3V3. VIO_4 (GPIO_28–34) is fixed at 1.8 V internally, with no pin [EVK].
- VDD18 (19): internal 1.8 V DCDC output → 10 µF + flash-CS pull-up only.

## Boot / flash / straps  ([RW] Table 47/48, pull a strap to 0 with ≤51 kΩ to GND; 1 = leave open)
- CS_Int_Flash (80) → GPIO_28 (98) with 0 Ω + 10 kΩ pull-up to VDD18 [EVK R10/R15]. Required to boot from the internal 16 MB flash.
- CONFIG_HOST[3:0] = EXT_FREQ(72), EXT_PRI(71), EXT_GNT(70), EXT_REQ(69): 1111 = boot from flash (default).
  ISP button: EXT_REQ → 5.1 kΩ → button → GND (1110 = ISP via UART/I2C/SPI/USB). Others open.
- RF_CNTL_2 (55) = CON[11]: 5.1 kΩ to GND → **SWD** (open = JTAG). Rev A: fit 5.1 kΩ.
- RF_CNTL_0 (4) = CON[5] XOSC select: **must stay open** (1 = 40 MHz, matches module crystal). Pulling it low selects 38.4 MHz.
- RF_CNTL_1 (53), RF_CNTL_3 (59): no config function in [RW] → NC (DNP 5.1 kΩ pads optional, matching EVK JP22).

## Reset / debug
- PDn (11): accepts 1.75–3.63 V [RW]. The module has a 51 kΩ pull-up to AVDD18 [EVK note]. Must be held low until the rails are stable.
  Rev A: 10 kΩ to 3V3 + 100 nF to GND (~1 ms delay), RESET button via 100 Ω to GND. Debug nRESET → Schottky (RB521S30) → PDn [EVK D2].
- SWD: SWCLK = GPIO_13 (43), SWDIO = GPIO_14 (106), both VIO_2 [EVK]. 10-pin 1.27 mm Cortex header: VTref = 3V3.
  (JTAG alt: TCK GPIO_6, TMS GPIO_7, TDI GPIO_8, TDO GPIO_9, TRST GPIO_10.)

## USB (USB-C, device only)
- USB_DP (29) / USB_DM (30) direct to the USB-C D+/D− (both A/B pairs), with ESD array. 5.1 kΩ on CC1/CC2.
- USB_VBUS (33): VBUS detect, operating range 4.4–5.25 V, **abs max 5.25 V** [RW]. [EVK] connects it straight to VBUS through a ferrite.
  Rev A: VBUS → 0 Ω (fit) → pin 33. If you'd rather not run pin 33 at the edge of its abs max, it can be left unconnected with a register override [RW note 5]; the 0 Ω can be depopulated.
- USB_ID (32): NC (floating = device) [EVK].
- Console: Zephyr CDC-ACM over USB, plus a 3-pin UART header (FC3: RXD GPIO_24 (97), TXD GPIO_26 (99)) matching the [EVK] FT230X wiring, as a bring-up fallback.

## RF
- Single antenna: BT_OUT (57) → 0 Ω → BT_IN (67) [EVK "shared antenna": R1 UL, R2 0R, L8 UL].
- RF_MAIN (6) → 50 Ω CPWG → pi network (EVK pi #3 for its trace antenna: series C4 2.2 pF, shunt L6 5.6 nH, L5 3.0 nH at the feed) → antenna.
- Rev A: U.FL (EVK J1 path) + pi pads DNP/0 Ω. The EVK trace-antenna geometry isn't in these docs (needs EVK Gerbers). Antenna must be a type and gain filed under FCC ID HSW2FR.
- EXT_* coexistence: only EXT_REQ is used (ISP strap). The rest are NC.

## UI
- RGB LED, common anode to 3V3: R = GPIO_51 (63) 470 Ω, B = GPIO_52 (64) 270 Ω, G = GPIO_53 (113) 2.2 kΩ [EVK values].
- USER button: GPIO_25 (87), 100 Ω series, 100 nF [EVK SW3]. Don't use GPIO_13/14 (SWD).
- 32.768 kHz crystal (GPIO_22/23): omitted.

## OPEN
1. ~~Footprint~~ DONE — pouch_gateway.pretty/Murata_LBES0ZZ2FR.kicad_mod, built from Murata type2fr2fp-footprint.dxf (see Footprint section).
2. Antenna part: pull the antenna datasheets from the HSW2FR FCC filing.
3. Buck regulator part selection (JLC basic/extended), ≥1 A.
4. Confirm Golioth bluetooth-gateway runs without external pSRAM (FRDM-RW612 has 8 MB APS6404L).
5. Confirm the Zephyr frdm_rw612 console UART instance and pins for the board port.

## Schematic status (rev A)
- **Superseded layout note:** the schematic is now hierarchical (root + USB, Power, MCU, Reset_Debug_Boot, RF, UI_IO sheets) and has grown to 66 footprints (display, Tag-Connect, mounting holes added). The bullets below are the original single-sheet notes, kept for the part choices.
- 53 parts, 36 nets, ERC 0 errors (warnings are off-grid placement + library-copy notices only).
- Netlist checked against this file: all 50 module GND pins, 6 VIO pins, VCC33 26/27, straps, flash CS, PDn, SWD, USB, RF verified.
- Changes vs the plan above:
  - RGB LED replaced by 3 discrete LEDs (couldn't verify the RGB part's pinout from its datasheet text). Red C2286 470 Ω, Green C2297 (0805) 100 Ω, Blue C125096 100 Ω, anodes to 3V3.
  - USER button has a 10 kΩ pull-up (R18) to 3V3.
- Buck: TLV62569DBVR (C141836), EN tied to +5V. FB divider R3 100k / R4 22k → 3.327 V (0.6 V ref). C3 6.8 pF feed-forward is DNP (optional per TI).
  L1 SWPA4020S2R2MT 2.2 µH (C83423) — check its saturation current in the datasheet (JLC DB lists no rating). Load is ≤576 mA peak, so any 4x4 2.2 µH should be fine.
- USB-C TYPE-C-31-M-12 (C165948); ESD PRTR5V0U2X (C21713980) on D+/D−/VBUS; FB1 BLM18KG221SN1D on VBUS → +5V.
- No LCSC on J2 (SWD 2x5 1.27 mm), J4 (UART 1x3), U1 — hand-solder / consign. U1 footprint assigned: pouch_gateway:Murata_LBES0ZZ2FR.

## Footprint (pouch_gateway:Murata_LBES0ZZ2FR)
- Source: Murata type2fr2fp-footprint.dxf (module bottom copper + bottom mask, outline 12.0 x 11.0 mm).
- DXF is a TOP view. Checks: (a) the missing center-grid pad sits bottom-right, as in [DS] Fig. 4 top view; (b) all 31 multi-via pads in Murata's copper map to GND/VCC33/VDD18/VIO_RF/USB_VBUS under this numbering, with 0 exceptions.
- Exposed land on the module = copper ∩ mask = 0.6 x 0.3 mm, r 0.05, 0.6 mm pitch on every pad (some module pads are SMD, some NSMD; the exposed area is the same).
  Host pad: 0.6 x 0.3 roundrect (rratio 0.1667), mask expansion 0.05 (= Murata's 0.7 x 0.4 opening), paste 1:1.
- Pad 1 bottom-right, pad 35 top-left (KiCad origin = body center). Pad centers match Murata's mask openings within 0.025 mm; the only offsets are a few module-side 0.65 mm mask-defined openings.
- Courtyard 12.5 x 11.5. Keep other copper, vias and silk clear of the module edge (GND-shielded sides).
- Loaded in KiCad OK (sync_schematic_to_board placed U1 and assigned its nets). The board wasn't saved because the PCB file was open/changed — run Update PCB from Schematic (F8) in KiCad.

## Antenna DXF
- type2fr2fp-evk-antenna.dxf = the EVK top-copper region: trace antenna + feed + keep-out. Available if we switch from U.FL to the PCB trace antenna (EVK pi #3: series 2.2 pF, shunt 5.6 nH, 3.0 nH at feed — tune on our board).

## Display (rev A, added 2026-10-18)
- Panel: Waveshare 2inch LCD Module, 240x320 IPS, ST7789VW, 4-wire SPI, 3.3/5 V, PH2.0 8-pin cable. Off-board, cable to J5.
- Driven by the RW612 LCDIC (Zephyr `nxp,lcdic` MIPI-DBI), pins per NXP SDK frdmrw612 lcdic pin_mux.c and Zephyr frdm_rw612 `pinmux_lcdic`:
  | Signal | RW612 fn | GPIO | U1 pin | Board |
  |---|---|---|---|---|
  | SCK | LCD_SPI_SCK | GPIO_48 | 82 | R21 33R → J5.4 |
  | DIN | LCD_SPI_DATA | GPIO_46 | 75 | R20 33R → J5.3 |
  | CS | LCD_SPI_SS | GPIO_49 | 81 | J5.5 |
  | DC | LCD_SPI_DC | GPIO_47 | 12 | R22 33R → J5.6 |
  | RST | LCD_SPI_RESET | GPIO_44 | 115 | J5.7 |
  | TE | LCD_SPI_TE | GPIO_45 | 111 | TP1 only (Waveshare module has no TE) |
  | BL | SCT0 OUT9 (PWM) | GPIO_55 | 109 | R23 0R → J5.8 |
- J5 order VCC, GND, DIN, CLK, CS, DC, RST, BL = Waveshare's standard order (confirmed on their 1.69in module) — 2inch wiki (checked 2026-10-20) lists the same order: VCC, GND, DIN, CLK, CS, DS(=DC), RST, BL. Still confirm which physical pin is pin 1 on the module's PH socket before first power-up.
- J5 footprint Connector_JST:JST_PH_S8B-PH-K_1x08_P2.00mm_Horizontal (side entry). JST S8B-PH-K-S(LF)(SN), LCSC C157915 (see Parts section below).
- R23 (BL): 0R by default. Unverified whether the module's BL pin drives its own transistor; if it's the raw LED, replace with a series R or add a low-side FET.
- C20 10uF + C21 100nF on +3V3 at J5. Max LCDIC SPI clock 32 MHz [RW §3.18.5].
- Netlist checked: all 7 U1 LCD pins land on the intended J5/R/TP nodes; ERC 0 errors.
- Firmware: `sitronix,st7789v`, 240x320, no row offset, under `&lcdic`; backlight via `pwm-leds` on SCT0 ch9.

## Tag-Connect SWD (rev A debug board, added 2026-10-18)
- J6 TC2030 (with legs) for the TC2030-CTX cable, footprint Connector:Tag-Connect_TC2030-IDC-FP_2x03_P1.27mm_Vertical. Fitted in parallel with J2 (10-pin 1.27 mm SWD); keep both on rev A, drop J2/J4 on rev 2 if Tag-Connect works out.
- Pinout per Tag-Connect TC2030-CTX sheet: 1 VCC → +3V3, 2 SWDIO → U1.106, 3 nRESET → DBG_NRST (same net as J2.10, via D2 to PDn), 4 SWCLK → U1.43, 5 GND, 6 SWO → NC (J2 SWO is NC too).
- J6 SWCLK pin set to passive in the sheet's local symbol copy so ERC doesn't flag two "output" pins (J2 and J6) on SWCLK. Only one cable is connected at a time.
- Footprint needs the three leg holes clear on the opposite side plus the keepout from the Tag-Connect drawing; don't put parts under it on the back.
- Netlist checked; ERC 0 errors.

## Mounting (added 2026-10-18) — SUPERSEDED by "Mounting update + 4-layer" below (now M2 on the display hole pattern)
- H1–H4: M3 mounting holes, footprint MountingHole:MountingHole_3.2mm_M3 (3.2 mm NPTH, no net), on the root sheet.
- Place in the four corners once the board outline is set: centers ~3.5 mm in from each edge, keep copper/parts outside the footprint keepout (screw head + boss). Mirror the same hole pattern on the enclosure bosses.

## Mounting update + 4-layer (2026-10-18)
- H1–H4 changed to **M2** (MountingHole:MountingHole_2.2mm_M2, 2.2 mm NPTH) and moved to match the Waveshare 2inch LCD Module hole pattern: centers 2.5 mm in from every edge of the 58 x 35 outline → **53.0 x 30.0 mm** pattern (board coords 112.5/165.5, 72.5/102.5).
  Source: Waveshare 2inch_LCD_Module_2D_Drawing.pdf (hole centers measured from the drawing geometry: 2.50 / 55.50 x 2.50 / 32.50 mm); Waveshare wiki specifies M2 x 6 hex standoffs.
  Same footprint as the display → one set of M2 standoffs can stack display + gateway board.
- Hole edge is 1.4 mm from the board edge; courtyard (r 2.45) just fits inside the outline. Keep copper/parts outside the courtyard.
- Board changed to **4 layers**: F.Cu / In1.Cu / In2.Cu / B.Cu. Plan: In1 = solid GND (reference for RF CPWG and SPI), In2 = GND + +3V3 pour, signals on F/B.
  Set the real stackup in Board Setup → Physical Stackup to JLC's 4-layer JLC04161H-7628 (or JLC04161H-3313) and recompute the RF_MAIN CPWG width for that stackup.

## Layout status (reviewed 2026-10-18)
Board: 58.0 x 35.0 mm (110,70)-(168,105), 4 layers F.Cu / In1.Cu / In2.Cu / B.Cu. All 66 footprints placed (R1, R2, TP1 on the bottom; everything else on top).

**Placement**
- U1 (2FR module) centered at (139.44, 86.62). USB-C J1 on the left edge, ESD D1 and FB1 next to it. SWD J2, RESET/ISP buttons and boot straps along the top-left; buck (U2, L1, C1-C5) top-right.
- RF: pi network right at U1 pin 6 (RF_MAIN): C17 shunt (147.1, 88.3) → R13 series 0R (149.1, 88.7) → C18 shunt (151.0, 88.3) → ANT_FEED → J3 U.FL at (159.2, 99.5). BT_OUT→BT_IN link R12 sits right under pins 57/67.
- Display J5 (PH 8-pin side-entry) on the right side at (160.3, 92.5); series R20–R23, C20/C21 and TP1 (bottom) between U1 and J5.
- Tag-Connect J6 at (149.2, 99.8); UART J4 bottom-left; LEDs D3–D5 and USER SW3 along the bottom.
- Mounting holes H1–H4: M2 on the Waveshare 53 x 30 mm pattern.

**Routing so far**
- 119 track segments (107 on F.Cu, 12 on B.Cu, all 0.2 mm) and 20 vias (0.6 / 0.3 mm).
- Second-row module escapes done with vias inboard of the pads: BTN_USER, LCD_SCK/CS/DIN/RST/TE/BL, FLASH_CS/IO28, UART_TX/RX, SWDIO, LED_G, EXT_REQ.
- Fully or mostly routed: EXT_REQ, FLASH_CS (+IO28), LCD_BL/CS/DIN/RST/SCK/TE, LED_G, SWDIO, UART_RX/TX, VDD18, USB CC1/CC2, USB VBUS.
- Partly routed: +3V3, BTN_USER, USB_DP/DM.
- Not yet routed: +5V, PDN, SWCLK, DBG_NRST, RST_SW, ISP_SW, RF_CNTL_2, RF_MAIN, ANT_FEED, BT_IN/BT_OUT, USB_VBUS_SNS, FB_3V3, SW_3V3, LCD_DC (+ the *_C display nets), LED_R/LED_B and the LED cathode nets, USER_SW.
- GND pours exist on all four layers (F/In1/In2/B) but are **not filled** in the saved file.

**DRC (2026-10-18):** 0 errors, 97 warnings: 16 "via dangling" (expected until the GND zones are filled), 42 silk overlap, 39 silk over copper. Courtyard check: no real overlaps (FB1/R2 flag is top vs bottom).

**Layout to-dos / review notes**
1. **Set the physical stackup** (Board Setup → Physical Stackup) to the JLC 4-layer you'll order (e.g. JLC04161H-7628), then size the RF_MAIN / ANT_FEED CPWG for 50 Ω on that stackup *before* routing them. No stackup is defined in the file yet.
2. **RF feed length:** ANT_FEED runs ~14 mm diagonally from C18 to J3, past J5 and near J6. Consider moving J3 right next to C18 (east of the pi network, toward the right edge) and moving J5 down/left, so the 50 Ω line is a few mm long with stitched GND vias both sides and solid In1 GND under it.
3. Keep In1 as an unbroken GND plane (no signal routing); use In2 for +3V3 / slow signals if needed.
4. Buck switch node (U2/L1, top-right) — keep SW_3V3 short and away from the RF corner; route FB_3V3 away from L1.
5. USB_DP/DM: route as a pair from D1 to U1 pins 29/30, keep them on F.Cu over In1 GND.
6. Confirm J5's cable opening faces the board edge (check in the 3D viewer).
7. Fill zones and re-run DRC (clears the dangling-via warnings); clean up silkscreen before fab.

## Optional 2nd BLE antenna (added 2026-10-18, RF sheet)
- Default build = **shared antenna**: R12 0R fitted (BT_OUT pin 57 → BT_IN pin 67), BLE combined onto RF_MAIN; 2.4 GHz Wi-Fi and BLE are arbitrated (time-shared) per RW612 DS §6.1.2.
- Added, all **DNP**: BT_OUT → C22 shunt (DNP) → R24 series 0R (DNP) → BT_ANT_FEED → C23 shunt (DNP) → J7 U.FL (DNP, same part as J3, LCSC C128668).
- To switch to **dual antenna** (BLE concurrent with 2.4 GHz Wi-Fi): remove R12, fit R24 + J7 (C22/C23 for matching if needed), and select the dual-antenna configuration in the NXP Wi-Fi/BLE firmware.
  **VERIFY** against the Murata 2FR EVK schematic / datasheet what BT_IN (pin 67) should see in dual-antenna mode (open vs. terminated) before relying on it.
- Layout: place R24's BT_OUT pad right at the BT_OUT / R12 node so the unpopulated branch is essentially zero-length (an RF stub on the shared path otherwise). Route BT_ANT_FEED as 50 Ω CPWG like ANT_FEED; J7 needs its own edge location away from J3.
- Run Update PCB from Schematic (F8) to bring C22, C23, R24, J7 onto the board.

## Stackup & RF net class (2026-10-20)
- Fab: PCBWay, S1000H TG150, 4-layer 1.6 mm, 1 oz all layers. Stackup entered in Board Setup (impedance controlled):
  F.Cu 35 µm / prepreg 7628 0.1855 mm Er 4.74 / In1 / core 1.03 mm Er 4.6 / In2 / prepreg 0.1855 mm Er 4.74 / B.Cu (KiCad total 1.561 mm; PCBWay finished ≈1.61 incl. plating + mask).
- RF = 50 Ω CPWG on F.Cu referenced to In1 GND: **W 0.27 mm, gap 0.20 mm** (≈48–52 Ω across Dk 4.3–4.74 and prepreg 0.17–0.19 mm).
- Net class **RF** (track 0.27, clearance 0.20) assigned to /MCU/RF_MAIN, /RF/ANT_FEED, /MCU/BT_OUT, /MCU/BT_IN, /RF/BT_ANT_FEED. Existing RF segments (4) widened to 0.27.
- F.Cu GND zone ("Top Signal") clearance changed 0.5 → 0.2 mm so the pour sits at the 0.20 mm CPWG gap (KiCad uses the larger of zone and net-class clearance). Inner/bottom zones left at 0.5.
- Still to do: GND stitching vias both sides of RF lines every 1–1.5 mm; keep In1 solid under the RF path; order with impedance control noting the RF nets / W / gap.

## Connector, LCD and cable part numbers (2026-10-20)
Added to the schematic as LCSC / Manufacturer / MPN fields (J5 also has Mating_Cable and Mates_With).

| Ref | Function | Manufacturer | MPN | LCSC |
|---|---|---|---|---|
| J2 | 10-pin Cortex SWD, 1.27 mm 2x5 SMD | Samtec | FTSH-105-01-L-DV-K-TR | C448647 |
| J4 | UART, 1x3 2.54 mm TH | XFCN | PZ254V-11-03P | C2937625 |
| J5 | LCD, JST PH 8-pin side entry | JST | S8B-PH-K-S(LF)(SN) | C157915 |

- J2: standard ARM Cortex debug header, unshrouded — use the pin-1 silk to orient the nRF9160 DK cable. Footprint is the generic KiCad PinHeader_2x05_P1.27mm_Vertical_SMD (2.4 x 0.74 mm pads, 3.9 mm row pitch); not yet checked against Samtec's recommended land pattern.

### Display
- **Waveshare 2inch LCD Module, SKU 17344** (240x320 IPS, ST7789VW, SPI, PH2.0 8-pin, 58 x 35 mm, M2 holes on a 53 x 30 mm pattern).
- The module ships with a PH2.0 8-pin to Dupont lead, which does **not** fit J5.

### LCD cable (J5 ↔ module), 8-pin JST PH, wired 1:1 (pin 1 → pin 1)
| Qty | Part | Manufacturer | MPN | Source |
|---|---|---|---|---|
| 2 | PH 8-pin receptacle housing | JST | PHR-8 | LCSC C157950 |
| 8 | Pre-crimped lead, SPH socket both ends, 24 AWG, 152 mm | JST | ASPHSPH24K152 | Digi-Key / Mouser / Future |

- No off-the-shelf 8-pin PH-to-PH cable found (Pololu stops at 6 pins; LCSC has none). Building from JST pre-crimped leads avoids needing the JST crimp tool. ASPHSPH24K series also comes in other lengths if 152 mm is wrong for the enclosure.
- Wire it straight-through so J5 pin n reaches module pin n. J5 pins 1–8 are VCC, GND, DIN, CLK, CS, DC, RST, BL, the same order the Waveshare wiki lists; the wiki doesn't say which physical pin on the module's socket is pin 1. Before the first power-up, check with a meter that J5.1 (+3V3) reaches the module's VCC pin and J5.2 reaches its GND pin.
