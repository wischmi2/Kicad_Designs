# Cable W1 wiring map: gateway J5 to Waveshare 2inch LCD Module

Written 2026-10-29 (parts-sourcing). Sources: pouch_gateway schematic (netlist exported with kicad-cli 10.0, J5 pins), Waveshare 2inch LCD Module schematic (files.waveshare.com/upload/e/ee/2inch_LCD_Module_SchDoc.pdf), Waveshare wiki (waveshare.com/wiki/2inch_LCD_Module), module 2D drawing in this folder. Parts and prices: pouch_gateway\sourcing\bom_digikey_mouser_2026-10-28_live.md, section "Cable assembly W1".

## Result in one paragraph

All eight J5 nets match the module signals (3V3 to VCC, GND, MOSI to DIN, SCK to CLK, CS, DC, RST, BL), and 3.3 V is within the module's 3.3/5 V supply and logic range. **The cable is very likely NOT straight-through by pin number.** Waveshare's module schematic numbers its PH2.0 connector (J2) 8 = VCC down to 1 = BL, while J5 on the gateway is 1 = VCC to 8 = BL. So lead n at the J5 housing goes to slot 9-n at the module housing (1-8, 2-7, 3-6, 4-5, 5-4, 6-3, 7-2, 8-1). A 1-1 cable would put 3V3 on the module's BL pin and BL on its VCC pin. This contradicts the existing note in DESIGN_NOTES.md ("wired 1:1"), which was written before the module schematic was checked. Confirm with the continuity check below before fitting the second housing, because the module's physical pin 1 is not marked in the wiki or the 2D drawing.

## Net check (J5 against the module)

J5 pins from the gateway netlist (pouch_gateway.kicad_sch, 2026-10-29):

| J5 pin | Gateway net | Series part | U1 pin / source | Module signal | Match |
|---|---|---|---|---|---|
| 1 | +3V3 | none (C20 10 uF and C21 100 nF at J5) | 3.3 V rail | VCC | yes |
| 2 | GND | none | GND | GND | yes |
| 3 | /UI_IO/LCD_DIN_C | R20 33R | LCD_DIN, U1.75 (LCDIC data, MOSI) | DIN | yes |
| 4 | /UI_IO/LCD_SCK_C | R21 33R | LCD_SCK, U1.82 | CLK (SCK) | yes |
| 5 | /MCU/LCD_CS | none | U1.81 | CS | yes |
| 6 | /UI_IO/LCD_DC_C | R22 33R | LCD_DC, U1.12 | DC | yes |
| 7 | /MCU/LCD_RST | none | U1.115 | RST | yes |
| 8 | /UI_IO/LCD_BL_C | R23 0R | LCD_BL, U1.109 (SCT0 PWM) | BL | yes |

No net mismatch. TE (U1.111) goes only to TP1; the module has no TE pin, so nothing is missing on the cable.

Voltage and loads (Waveshare module schematic):
- VCC range 3.3 V / 5 V; there is no level shifter, so logic level = VCC. The gateway's 3.3 V signals match. Wiki FAQ: about 46 mA at 3.3 V. The wiki gives no numeric VIH/VIL.
- BL drives a 1k base resistor of an NPN (collector to the LED cathode through 10R), with a 10k pull-up from the base to VCC. So BL is active high, and the backlight is on by default if BL floats. R23 0R in series is fine (about 2-3 mA from the pin). This answers the open DESIGN_NOTES question about whether BL drives a transistor: it does.
- J5 +3V3 comes from the 3V3 buck output, so there is no 5 V on the cable.

## Module connector pin numbering (from the Waveshare schematic)

The module has two 8-position items: J1 (an unpopulated 2.54 mm hole row, pin 1 = VCC to pin 8 = BL) and J2, the JST PH2.0 SMT side-entry connector on the back, which the cable plugs into. In the schematic J2 is drawn with pin 8 at the top: **J2 pin 8 = VCC, 7 = GND, 6 = DIN, 5 = SCK, 4 = CS, 3 = DC, 2 = RST, 1 = BL.** The module's PCB silkscreen reads VCC at the top down to BL at the bottom beside J2. The wiki lists the signals as VCC, GND, DIN, CLK, CS, DC, RST, BL but gives no physical pin 1. I could not confirm the physical pin 1 of the PH connector footprint (the 2D drawing does not mark it), so the mapping rests on the schematic symbol numbering.

## Wiring table (cable W1)

Housing slots are the numbers moulded on the PHR-8 housing (the header pin that slot mates with). Seen from the wire side with the latch up, slot 1 is at the left on every PHR housing, so the two housings are the same part held the same way. The leads are all black, so tag each lead L1-L8 at both ends.

| Lead | J5 pin | Net | Signal | J5-end housing slot | Module PH pin (Waveshare J2) | LCD-end housing slot |
|---|---|---|---|---|---|---|
| L1 | 1 | +3V3 | VCC | 1 | 8 | 8 |
| L2 | 2 | GND | GND | 2 | 7 | 7 |
| L3 | 3 | LCD_DIN_C | DIN (MOSI) | 3 | 6 | 6 |
| L4 | 4 | LCD_SCK_C | CLK (SCK) | 4 | 5 | 5 |
| L5 | 5 | LCD_CS | CS | 5 | 4 | 4 |
| L6 | 6 | LCD_DC_C | DC | 6 | 3 | 3 |
| L7 | 7 | LCD_RST | RST | 7 | 2 | 2 |
| L8 | 8 | LCD_BL_C | BL | 8 | 1 | 1 |

Straight or reversed: **reversed by housing pin number (slot n at J5 to slot 9-n at the LCD)**. Seen from the wire side of both housings, L1 leaves the leftmost slot of the J5 housing and enters the rightmost slot of the LCD housing, so the leads cross as a mirror. Do not rotate a housing to get this: PH housings are polarised and will not mate the other way round.

Both ends use the same housing (PHR-8) and the same lead (ASPHSPH24K102, PH socket contact at both ends).

## Checks before first power-up

1. Module unpowered, meter on continuity: from the 2.54 mm hole row on the back (silk VCC, GND ... BL, wired straight to the PH pins) to the PH connector pins, confirm which PH pin is VCC and GND. If VCC is at the pin-8 position (GND at 7) this table is right. If the PH order turns out the other way round, build 1-1 instead (slot n to slot n).
2. With the cable built and both ends unplugged, buzz each lead between J5 pin n and the module PH pin from step 1: J5.1 must reach module VCC and J5.2 module GND.
3. On the powered gateway, confirm J5.1 reads 3.3 V and J5.2 0 V before plugging the module in.

## Items for kicad-designer and the main agent (nothing changed here)

- No net mismatch between the gateway schematic and the module, so nothing to fix on the board.
- DESIGN_NOTES.md (section "LCD cable (J5 to module)") is out of date: it says wired 1:1 and lists the 152 mm lead ASPHSPH24K152. The cable should be reversed per the module schematic (pending the continuity check), and the BOM now uses ASPHSPH24K102 (102 mm). Updating DESIGN_NOTES.md is for kicad-designer.
- The 102 mm lead is 20-40 mm longer than the 60-80 mm asked for; the next shorter lead (ASPHSPH24K51, 51 mm) is too short.
