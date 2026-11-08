# Programming the XM125 on the water level board (1.8 V UART)

Written 2026-11-04 for board rev 0.2; part 0 added 2026-11-07 for the TC2030 variant (this folder). Not tried on real hardware yet. Pad positions and nets were read from `feather_water_level.kicad_pcb` (unchanged in `feather_water_level_tc2030.kicad_pcb`). Part 10 lists what is still unverified.

## 0. TC2030 variant: flashing through J1 (added 2026-11-07)
This copy of the guide belongs to **feather_water_level_tc2030** (rev 0.2-TC2030), which adds a Tag-Connect TC2030 legged footprint, J1, on the bottom side between H1 and H2. Everything below still applies; J1 only replaces soldered wires on TP4-TP8. The test pads are all still there. The original rev 0.2 board has no J1, so use parts 2-6 as written for it.

**J1 pin map** (looking at the bottom of the board, pin 1 is marked on the silk; pins 1-2-3... follow the Tag-Connect numbering):

| J1 / TC2030 pin | Signal | Same as | FTDI TTL-232RG-VREG1V8-WE wire |
| --- | --- | --- | --- |
| 1 | NRST | TP3 | none (optional: touch to GND to re-enter the bootloader) |
| 2 | +1V8 | TP7 | none; 1 k from here to pin 3 |
| 3 | BOOT0 | TP4 | none; 1 k to pin 2 |
| 4 | UART RX (module input) | TP6 | orange (TXD), through 330 ohm |
| 5 | GND | TP8 | black |
| 6 | UART TX (module output) | TP5 | yellow (RXD), through 330 ohm |

Red, brown and green wires stay unconnected and insulated, as in part 3. Pin 2 is a reference only: the board is powered from the bench supply on TP9 VSENS and TP10 VBAT (3.0 V, part 5) or from the feather, **never from the cable**.

**What to buy:**
- **TC2030-IDC** (legged, 8 in / 225 mm), Tag-Connect. DigiKey TC2030-IDC-ND, 246 in stock, $44.58 (live 2026-11-07, active). The legged version clips into the board, so it holds itself while you flash. The TC2030-IDC-NL (no legs) also fits these pads but has to be held by hand or with a retaining clip.
- **The cable end is a 6-pin 0.1 in (2.54 mm) IDC ribbon socket, wired 1:1 to the TC2030 pins** (Tag-Connect drawing TC2030-IDC rev B, sheet 2). It is **not** the 10-pin 1.27 mm Cortex connector; that one is on the TC2030-CTX cable. So no 10-pin 1.27 mm breakout is needed: push 2.54 mm male jumper wires or a 2x3 0.1 in header into the socket and run them to the FTDI cable. (The 2026-11-07 task asked for a 10-pin 1.27 mm breakout; that applies to the TC2030-CTX, not the TC2030-IDC.)
- **Adapter (build one):** a **shrouded, keyed 2x3 0.1 in box header** on a scrap of perfboard, with **pin 1 marked** on the board next to the shroud. The IDC socket on the cable has a key that only fits the shroud one way. Don't use a bare 2x3 pin header: the socket then goes on turned round just as easily, which swaps pin n with pin 7-n: the adapter's GND (pin 5) lands on the board's +1V8 (pin 2), shorting the 1.8 V rail to GND through the cable and PC ground, and the cable's TXD (pin 4) and RXD (pin 6) land on BOOT0 (pin 3) and NRST (pin 1). On the adapter: the 1 k from pin 2 to pin 3 **through a 2-pin jumper (shunt) in series** (see BOOT0 release below), the two 330 ohm resistors in line with pins 4 and 6, and the FTDI wires soldered on. Build it once and check every pin with a meter against the J1 table before the first board.
- **BOOT0 release:** with the 1 k now on the adapter, the module stays in the bootloader for as long as the cable is on and the jumper is fitted. To run the new application: pull the jumper (or unplug J1), then power-cycle the board (bench supply off and on). Part 6 step 5 ("Remove the 1 k from TP4") means this here; the jumper also lets you try a normal boot without unplugging.
- **Don't use Tag-Connect's own USB-UART (FTDI) cables** on this board unless the exact model's logic level has been checked: they are 3.3 V or 5 V (per the 2026-11-07 task notes; no model was looked up for this guide). The XM125 I/O operating range is 0 to VIN + 0.3 V (DS v1.2 Table 3), which is 2.1 V here because VIN is 1.8 V. The 3.63 V in DS Table 2 is the absolute maximum (stress rating, no operation implied), not a safe signal level, and a 3.3 V signal into a 1.8 V-powered (or unpowered) pin pushes current through the pin's clamp into the 1.8 V rail (inferred, not from the datasheet). Use the 1.8 V FTDI cable through the IDC socket as above.

**Power order (inferred, not from a datasheet):** the FTDI cable's TXD idles high at about 1.8 V as soon as its USB end is plugged in. If the board is still unpowered, that can back-feed the +1V8 rail through the module's UART_RX pin clamp and leave the STM32 half-powered, so the ROM bootloader may not start cleanly. So: **power the board first, then plug the FTDI USB end in** (or plug J1 on last). If the cable was already live when the board was powered, pulse NRST (J1 pin 1, or TP3) to GND once before talking to the bootloader.

**Steps:** as part 6, except step 1 becomes: FFC out, supply off, wire bench power to TP9/TP10/TP8 as in part 5, then press the TC2030 plug onto J1 from the bottom side until the legs click (the alignment pins only go in one way round). Release by squeezing the legs from the two long board edges. The legs stick 2.24 mm out of the top side; with the feather still stacked on its 8 mm standoffs they have room.

**Plug fit (S1 check 2026-11-07, box model from the Tag-Connect drawing, no vendor 3D model found):** the part of the plug that sits on the board (the pin carrier, about 7.35 mm wide, scaled from the drawing) ends 1.42 mm from the XM125 body edge. The wider grip (9.27 or 9.906 mm, the drawing gives both) starts about 7.5 mm off the board, about 5.6 mm above the module top. Even if the full 9.906 mm reached the board it would end 0.15 mm short of the module (no overlap). Picture: C:\Personal-Agents\shared\design\feather_water_level\tc2030_2026-11-07\plug_fit_check.png.

**Unverified:** fit with a real cable (the drawing says dimensions are subject to change). Not tried on hardware.

## 1. Short version
- Every XM125 has to be flashed once. The datasheet says it is delivered with a bootloader, so don't count on it having our application.
- Flash `i2c_distance_detector.bin` through the STM32 ROM bootloader, 115200 baud, 8 data bits, even parity, 1 stop bit, to address 0x08000000.
- All module signals are **1.8 V**. A 3.3 V USB-UART can damage the module: the I/O operating range is 0 to VIN + 0.3 V = 2.1 V at our 1.8 V VIN (DS v1.2 Table 3; Table 2's 3.63 V is the absolute maximum, not an operating level).
- The FFC stays out. Power comes from a bench supply at 3.0 V, **not** from the cable's red wire.
- The feather can't flash the module: BOOT0 and UART don't reach CN1. Opening the enclosure is accepted for updates (Brian, 2026-11-03).

## 2. What to buy
| Item | Part | Note |
| --- | --- | --- |
| 1.8 V USB-UART cable | FTDI TTL-232RG-VREG1V8-WE | Mouser 895-TTL232RGVREG1V8W, 881 in stock, $27.34 (live 2026-11-04; DigiKey not checked). 1.8 m, wire ends with no connector |
| BOOT0 pull-up | 1 k resistor | Pulls TP4 to TP7 (part 5) |
| Series protection (recommended) | 2 x 330 ohm | One in each of TXD and RXD. My suggestion, not from a datasheet. Limits current if a wire is wrong or the board is off; no effect at 115200 baud |
| Fine wire | 30 AWG | The cable's 24 AWG wires are too stiff for 1 mm pads. Solder them to a small adapter or header, then run 30 AWG to the board |
| Bench supply | 3.0 V, 150 mA limit | The limit is my suggestion. Normal radar peak is about 80 mA, and the bootloader should need less |

Check the part number on the cable. The other TTL-232RG versions look the same and run at 3.3 V or 5 V.

## 3. Cable wires
Colours are from the FTDI TTL-232RG datasheet v1.3, table 4.1.

| Wire | Cable signal | Connect to | Board net / U1 pad |
| --- | --- | --- | --- |
| Black | GND | **TP8** | GND |
| Orange | TXD (cable output) | 330 ohm, then **TP6 "RX"** | XM_UART_RX, U1.6 |
| Yellow | RXD (cable input) | 330 ohm, then **TP5 "TX"** | XM_UART_TX, U1.5 |
| Red | VCC output | **Nothing, insulate it** | - |
| Brown | CTS# | Nothing, insulate it | - |
| Green | RTS# | Nothing, insulate it | - |

- TX and RX cross over. The silk names TP5 and TP6 from the module's side.
- **Why the red wire stays off:** FTDI gives its output as 1.32 V min, 1.62 V typ, 1.8 V max. The XM125 needs 1.71-1.89 V, so it can be under-voltage. It also only rates 100 mA, with no margin for the module's 80 mA peak.
- stm32loader drives DTR and RTS for reset and BOOT0 on boards wired for that. Nothing is connected to them here, so you do BOOT0 and reset by hand.

## 4. Test pads
All pads are 1.0 mm on the bottom side (the XM125 side), with no paste. Coordinates are KiCad board mm.

| Pad | Signal | x, y | Use for UART flashing |
| --- | --- | --- | --- |
| TP5 | UART TX (module output) | 104.2, 111.55 | Yes |
| TP6 | UART RX (module input) | 106.4, 111.55 | Yes |
| TP8 | GND | 108.7, 111.55 | Yes |
| TP7 | +1V8 | 97.6, 111.8 | Yes, BOOT0 pull-up source and check point |
| TP4 | BOOT0 | 102.285, 131.35 | Yes (opposite edge from the others) |
| TP10 | VBAT | 132.0, 114.0 | Yes, 3.0 V in |
| TP9 | VSENS | 133.5, 122.75 | Yes, 3.0 V in |
| TP3 | NRST | 116.2, 111.55 | Optional, see part 5 |
| TP1, TP2 | SWDIO, SWCLK | 111.6 and 113.8, 111.55 | No, SWD only |

Looking at the bottom of the board, so left and right are mirrored from the KiCad view (not to scale):

```
 top edge
   TP3   TP2   TP1   TP8  TP6  TP5        TP7
   NRST  SWCLK SWDIO GND  RX   TX         1V8
 TP10 VBAT
              +---------------------------+
 TP9 VSENS    |         U1 XM125          |
              +---------------------------+
 (CN1 end)                     TP4 BOOT0      (H1/H2 end)
 bottom edge
```

The silk legend reads in the same order: "TP: NRST SWCLK SWDIO" then "GND RX TX, 1V8 far".

## 5. Power and bootloader wiring
1. **FFC out.** Never apply bench power with the FFC fitted, because it would fight the feather's VSENS.
2. Set the supply to 3.0 V and tie **TP10 VBAT and TP9 VSENS** together to it, with the return on TP8. VBAT feeds the LDO, and VSENS enables the LDO and powers the host side of the translators.
3. Fit **1 k from TP4 to TP7**. BOOT0 has a 100 k pull-down on the module (datasheet schematic), so it boots normally when this resistor is off. The resistor also protects the pin if the application ever drives it as MISC_GPIO2.

With BOOT0 already high, **powering on enters the bootloader**, so no reset wire is needed. Use TP3 only to re-enter without a power cycle: touch it to GND briefly while BOOT0 stays high.

Q1 doesn't interfere with TP3. With the FFC out, R2 keeps Q1 off.

## 6. Flashing steps
**One-time setup**
1. Install a tool. Neither was found on the desktop PC on 2026-11-04 (CubeProgrammer checked at its default path only):
   - `pip install stm32loader` (0.7.1 is the current stable version), or
   - STM32CubeProgrammer from st.com.
2. Get the binary: developer.acconeer.com (free account) > A121 Docs & Software > XM125 / XE125 > the XM125 SDK. It is in `xm125\out\i2c_distance_detector.bin`. Use the distance detector file, not `i2c_presence_detector.bin`.
3. Plug in the cable and note its COM port in Device Manager. Install the FTDI VCP driver if none appears.
4. With the cable plugged in and **not connected to the board**, measure orange to black. Expect about 1.8 V and **never above 1.89 V**. If it reads 3.3 V, you have the wrong cable.
5. Rehearse on the SparkFun breakout first. It has its own USB-UART and BOOT/RST buttons, so it checks the tool and binary before you touch the board.

**Each board**
1. FFC out, supply off. Solder or clamp the wires: part 3 signals, 1 k BOOT0, power.
2. Turn on the supply. Check TP7 = 1.71-1.89 V, TP4 close to TP7, and supply current is sane.
3. Flash with one of these:

   stm32loader (replace COM7 with your port):
   ```
   stm32loader -p COM7 -e -w -v i2c_distance_detector.bin
   ```
   The defaults are already 115200 baud, even parity and address 0x08000000. If it stops on device family detection, add `-f L4`.

   STM32CubeProgrammer GUI: choose UART, the COM port, 115200, Even, 1 stop bit, flow control off, then Connect. On the Download tab, pick the file, set start address `0x08000000`, and press Start Programming. Press Disconnect when done.

4. Check the tool reports verify OK.
5. Turn off the supply. **Remove the 1 k from TP4.** If it stays on, the module boots back into the bootloader.
6. Remove the wires and clean off flux.

## 7. Checking it worked
UART silence after flashing is normal as far as we know: the application's debug logs go to the DEBUG_UART pads, which are not connected on this board. Check over I2C instead, once it's on the radar-build feather (R15-R18 not fitted):

1. Turn on VSENS, hold RADAR_RST (SENS_CS) low, set RADAR_WAKE (SENS_MOSI) high.
2. Wait for SENS_INT high.
3. At I2C address 0x52, read register **0xFFFF, Application Id**. The register address is 16-bit and the data is 32-bit big-endian. Expect `00 00 00 01` (1 = distance detector, 2 = presence detector).
4. Read register 0x0000 for the RSS version and write it in the build log.

## 8. If it doesn't connect
| Symptom | Check |
| --- | --- |
| No response / sync failed | TX and RX swapped; TP7 not 1.8 V; TP4 not high; black wire not on TP8 |
| Worked once, then no response | The bootloader locks onto the first interface it sees activity on, so power-cycle with BOOT0 high and retry |
| COM port busy | Close any other tool holding the port, such as a terminal or CubeProgrammer |
| Application doesn't start afterwards | The 1 k is still on TP4 |
| Still no response after all of the above | Measure orange at TP6 and yellow at TP5 while connecting. Then move to SWD (part 9) |

- **Don't change option bytes** (nSWBOOT0, nBOOT0). A SparkFun forum user reported permanent UART timeouts after unticking nSWBOOT0. SWD is the likely way back from that, and that thread had no confirmed fix.
- Other SparkFun forum users with modules that would not connect turned out to have faulty units and got replacements. Try the SparkFun breakout or a spare before reworking the board.

**Level margins from the FTDI datasheet, table 4.7:**
- Cable input threshold is 1.0-1.5 V. The module drives about 1.8 V, so that direction has at least 0.3 V margin.
- Cable output high is 1.32 V min at 6 mA. The module's input draws almost nothing, so expect close to the top of the 1.32-1.8 V range. The module's input threshold at 1.8 V hasn't been read (part 10).

## 9. Backup: SWD
TP1 SWDIO, TP2 SWCLK, TP3 NRST, TP7 for VTref, TP8 GND. It needs a probe that works at 1.8 V and is licensed for STM32. The nRF9160 DK's on-board J-Link is restricted to Nordic targets per forum reports and SEGGER terms (not tried), so it would need a separate probe such as a J-Link BASE or an ST-Link, which Acconeer recommend. Check the probe's 1.8 V support before buying. Not needed unless UART fails.

## 10. Open items
**Brian to decide:** soldered wires or a pogo jig. I recommend soldered wires for the first boards and the rehearsal: nothing to design, and a jig needs pins at both board edges (TP4 is on the far side from TP5-TP8, and TP9/TP10 are elsewhere). A jig is worth building if you expect to flash more than a handful of boards. Either way, the stack has to come out of the enclosure.

**When to flash:** after the whole board is assembled, so U2 and the translators are in place. Flashing right after the hotplate step would catch a dead module sooner, but C5/C6 and U2 are on the F side and aren't fitted then, so it would need 1.8 V into TP7 and is untested.

**The TP7 power method (only if TP9/TP10 can't be used):** FFC out, 1.8 V (1.89 V max) into TP7, return on TP8, from a bench supply, not the cable. About 6.4 mA extra flows into U2's discharge path (2026-11-02 review, S3). VSENS is off, so the I2C translator doesn't hold the module's I2C lines high, which might upset the bootloader's interface detection (my inference, untested).

**Unverified:**
- **Bootloader pins:** ST AN2606 could not be opened (the STM32L431 table). That UART_TX/RX are valid bootloader pins rests on Acconeer's guide, the XE125 EVK flashing through these same pins, and the datasheet schematic (PA2/PA3). The SparkFun breakout rehearsal tests this in practice.
- **Module input threshold:** STM32L431 VIH at 1.8 V not read.
- **`-f L4`:** the flag value is from memory and stm32loader's page only shows `F1`. Run `stm32loader --help` if you need it.
- **Binary path:** the folder name is from SparkFun's page for an older SDK (v1_5_0), so it may differ in the current SDK.
- **Not tested on this board:** any of these steps. Update this file after the first flash.

## Sources
- XM125 Software User Guide, a121-v1.3.0, sect. 3-4 (BOOT0/reset order, stm32loader command, SWD). The board notes cite v1.13.0, which should say the same but wasn't re-read for this file.
- XM125 I2C Distance Detector User Guide, a121-v1.13.0: sect. 2.4.4 (debug UART) and registers 6.2.1, 6.2.41.
- `xm125_notes.md` (pinout, supplies) and `shared\reports\2026-11-02-review-feather-water-level.md` (S3, module schematic).
- [FTDI TTL-232RG cable datasheet v1.3](https://www.farnell.com/datasheets/2036188.pdf): wire colours, tables 4.6 and 4.7.
- [SparkFun: flashing the XM125](https://docs.sparkfun.com/SparkFun_Qwiic_Pulsed_Radar_Sensor_XM125/flashing_firmware_xm125/): UART settings, address, binary names.
- [stm32loader on PyPI](https://pypi.org/project/stm32loader/): options and defaults.
- [SparkFun forum: cannot flash XM125](https://community.sparkfun.com/t/cannot-flash-xm125-module-any-more/63025): faulty-unit reports. The nSWBOOT0 report came from a search-result excerpt; that thread wasn't read in full.
