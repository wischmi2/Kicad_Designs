# Firmware

nRF Connect SDK (Zephyr) firmware for the nRF54L15 boards in `hardware\`.

| Folder | What |
| --- | --- |
| `boards\nrf54l15_feather\` | Board definition `nrf54l15_feather/nrf54l15/cpuapp` (main feather, `hardware\feather\`) |
| `boards\soil_moisture\` | Board definition `soil_moisture/nrf54l15/cpuapp` (old soil-moisture board, `hardware\archive\`) |
| `boards\pouch_gateway\` | Board definition `pouch_gateway/rw612` (gateway, Murata Type 2FR / NXP RW612, `hardware\gateway\`); see "Gateway board definition" below |
| `apps\feather_node\` | Golioth Pouch BLE node (MCUboot, LittleFS credentials, nPM1300 fuel gauge, SENS_ID uplink on `.s/sensor`). Build/flash/provision scripts in `scripts\`, notes in `README.md` and `HW_VERIFY.md` |
| `apps\pouch_gateway\` | Golioth Pouch gateway (BLE to Wi-Fi), the Pouch `examples/zephyr/gateway` app at 32ded9b built from this repo; needs the separate Zephyr workspace `C:\ncs\pouch-zephyr` (see "SDK workspace (Zephyr v4.4.0 ...)" below) |

`firmware\` is the Zephyr `BOARD_ROOT` (Zephyr looks for `BOARD_ROOT\boards\**\board.yml`).
The app adds it in `CMakeLists.txt` and `sysbuild\CMakeLists.txt`, and `scripts\build.ps1` sets it in
`$env:BOARD_ROOT`. App-level board overlays (`apps\feather_node\boards\<board>.conf`) stay with the app.

## SDK workspace (NCS v3.4.0 + Golioth Pouch), set up 2026-11-13

The Pouch node build uses its own west workspace, not the `C:\ncs\v*` ones:

| Item | Value |
| --- | --- |
| Toolchain | `nrfutil sdk-manager toolchain install --ncs-version v3.4.0`, bundle id `dcbdc366a1` (`C:\ncs\toolchains\dcbdc366a1`, Zephyr SDK 1.0.1, GCC 14.3.0), nrfutil sdk-manager 1.17.0 (added with `nrfutil install sdk-manager`) |
| Workspace | `C:\ncs\pouch-ncs`, `west init -m https://github.com/golioth/pouch --mf west-ncs.yml`, manifest repo `C:\ncs\pouch-ncs\pouch` checked out at `32ded9b` (golioth/pouch main, v0.2.0 + 18) |
| `west update` | run with `-o=--depth=1 -n` (shallow, no tags) |
| Patches | `zephyr\patches.yml` only applies on the `west-zephyr.yml` manifest (each entry is guarded by `west config manifest.file = west-zephyr.yml`), so `west patch apply` is not needed with `west-ncs.yml` and was not run |
| Extra | `zcbor` 0.9.1 installed into the toolchain's Python (`nrfutil sdk-manager toolchain launch --ncs-version=v3.4.0 -- python -m pip install zcbor==0.9.1`). The bundled zcbor 0.8.1 fails on Pouch's absolute `--output-c` path on Windows (`OSError ... './C:'`) |

`west list` (2026-11-13):

```
manifest     pouch                        HEAD (32ded9b)
nrf          nrf                          f30459884d7f4c3769e5b61409d101d4baedc91e
zephyr       zephyr                       b836543f5393f1869dda32604fe60dbd43ee0c70   (Zephyr 4.4.1)
mcuboot      bootloader/mcuboot           ncs-v3.4.0
mbedtls      modules/crypto/mbedtls       ncs-v3.4.0
oberon-psa-crypto modules/crypto/oberon-psa-crypto ncs-v3.4.0
nrfxlib      nrfxlib                      74b7aaaa99a96c54113525d135d4645bf172edf9
trusted-firmware-m modules/tee/tf-m/trusted-firmware-m ncs-v3.4.0
cmsis_6      modules/hal/cmsis_6          30a859f44ef8ab4dc8f84b03ed586fd16ccf9d74
hal_nordic   modules/hal/nordic           18da0cc9726f8759c627dba3180b3ba9294e433c
libmetal     modules/hal/libmetal         66e084293b2a7ced5a73fbd247deddba8915883a
littlefs     modules/fs/littlefs          8f5ca347843363882619d8f96c00d8dbd88a8e79
open-amp     modules/lib/open-amp         5efe7974f9546582e99f5a842a816ea4b65f5227
segger       modules/debug/segger         50892fdbcf2f570e67baa72b8894a66b16946f72
tf-psa-crypto modules/crypto/tf-psa-crypto efdf9e209cc3b2c7be93ac81c7c96cd2550bbe27
zcbor        modules/lib/zcbor            9164bd18dcd88ff9d9ef98279501fc1093571017
```

Proof build: `pouch\examples\zephyr\ble_gatt` for `nrf54l15dk/nrf54l15/cpuapp` into `C:\ncs\pouch-builds\ble_gatt_dk` (outside the repo), pristine, no errors. App 313,824 B flash (44 % of the 712,560 B slot), 67,784 B RAM (25.9 %); MCUboot 40,252 B / 62 KB, 20,568 B RAM. Warnings: Kconfig `BOOT_MAX_IMG_SECTORS` assigned 256 but unsatisfied dependency (MCUboot), `NRF_PLATFORM_LUMOS` deprecated (twice), CMake "default MCUboot signing key, debug use only", and `lto-wrapper: using serial compilation of 2 LTRANS jobs` (benign).

Build command (the scripts wrap this): `nrfutil sdk-manager toolchain launch --ncs-version=v3.4.0 --chdir C:\ncs\pouch-ncs -- west build -p -b <board> -d <dir> <app>`.

Build and program (NCS v3.4.0, workspace above; nothing has been run on hardware yet):

```powershell
cd C:\Personal-Agents\worktrees\nrf54l15-feather-branch\firmware\apps\feather_node
.\scripts\build.ps1                            # nrf54l15_feather/nrf54l15/cpuapp, pristine, C:\ncs\pouch-builds\feather_pouch
.\scripts\flash.ps1 -Serial <J-Link serial>    # nrfutil device program, ERASE_NONE, no west flash
python .\scripts\provision_credentials.py --crt c.der --key k.der --serial <J-Link serial>   # prints commands only
```

`flash.ps1` has no default serial on purpose. Credentials (`*.der`, `*.pem`, credential hex) are gitignored and never committed. Details, sizes, warnings and the Pouch differences are in `apps\feather_node\README.md`.

## SDK workspace (Zephyr v4.4.0 + Golioth Pouch, NXP RW612 gateway), set up 2026-11-13

The gateway (`hardware\gateway`, Murata Type 2FR / LBES0ZZ2FR, NXP RW612, Wi-Fi only) uses a plain Zephyr workspace with the Pouch `west-zephyr.yml` manifest. NCS has no `hal_nxp`, so it can't share the feather's NCS workspace. Nothing here touches `C:\ncs\pouch-ncs` or `C:\ncs\v*`.

| Item | Value |
| --- | --- |
| Toolchain | NCS v3.4.0 bundle `dcbdc366a1` (`nrfutil sdk-manager toolchain launch --ncs-version v3.4.0`), Zephyr SDK 1.0.1, GCC 14.3.0. Zephyr v4.4.0's own `SDK_VERSION` is 1.0.1, so no extra SDK install was needed. `zcbor` 0.9.1 is already in that Python (installed for the feather) |
| Workspace | `C:\ncs\pouch-zephyr`. `git clone https://github.com/golioth/pouch pouch`, `git checkout 32ded9b` (golioth/pouch main, v0.2.0 + 18), `west init -l pouch --mf west-zephyr.yml`. (`west init -m <url> --mr <sha>` does not take a commit id.) |
| `west update` | `-o=--depth=1 -n` (shallow, no tags). Zephyr is at tag `v4.4.0` (684c9e8f, `VERSION` 4.4.0) |
| Patches | `west patch apply` reports "8 patches applied successfully" but applied nothing here: each patch's `apply-command` runs `bash -c 'if [ $(west config manifest.file) = "west-zephyr.yml" ] ...'` and `bash` inside the nrfutil toolchain shell has no `west`, so the test is false. Applied by hand in Git Bash instead: `cd C:\ncs\pouch-zephyr\zephyr; git am ../pouch/zephyr/patches/zephyr/zephyr/000*.patch` (8 commits on top of v4.4.0, HEAD 0b2959d2). The one that matters for the RW612 is 0008 (re-power TDDR PLL when enabling Ethernet after MCUboot); 0001-0007 are NSOS / BabbleSim only |
| Blobs | `west blobs fetch hal_nxp` fetched the `rw61x` blobs (`rw61x_sb_wifi_a2.bin` 351,804 B, `rw61x_sb_ble_a2.bin`, `rw61x_sb_ble_15d4_combo_a2.bin`) and then stopped at an i.MX95 boot-firmware blob that needs a licence click-through. That licence was **not** accepted (not needed for RW612). The Wi-Fi blob is linked into the app image (`firmwares.ld`), so there is no separate flash step for it in this Zephyr version |

`west list` (2026-11-13):

```
manifest      pouch                     32ded9b
zephyr        zephyr                    v4.4.0 (684c9e8f) + 8 patches
hal_nxp       modules/hal/nxp           2c2f28ac333e995d7279777409817c4b4f92c1ec
cmsis_6       modules/hal/cmsis_6       30a859f44ef8ab4dc8f84b03ed586fd16ccf9d74
hal_nordic    modules/hal/nordic        44fd3d44b15cb75f80a25b4679f91d2787e28664
littlefs      modules/fs/littlefs       8f5ca347843363882619d8f96c00d8dbd88a8e79
mbedtls       modules/crypto/mbedtls    a3e190fe44c78d1ba67f55979e1257328cc7d0d8
mcuboot       bootloader/mcuboot        ee39e2d694bd827ffd1bebbce2f571a9154e6ec2
picolibc      modules/lib/picolibc      01254932e8e81085817ed61fd858648584ffe37c
segger        modules/debug/segger      50892fdbcf2f570e67baa72b8894a66b16946f72
tf-psa-crypto modules/crypto/tf-psa-crypto          dc575a2ddcc8cb16275d24c42a52eaf79ebe2231
trusted-firmware-m modules/tee/tf-m/trusted-firmware-m 9a4cb1a280b63a5e66bd469e82eb75f2b3e05a78
zcbor         modules/lib/zcbor         9164bd18dcd88ff9d9ef98279501fc1093571017
(plus nrf_hw_models and the BabbleSim components, unused)
```

Proof build (upstream, unmodified except the fix below): `pouch\examples\zephyr\gateway` for `frdm_rw612` with `-DEXTRA_CONF_FILE=boards/frdm_rw612_wifi.conf`, into `C:\ncs\pouch-builds\gw_frdm_proof` (outside the repo). Compiles and links with **no warnings**: flash 1,243,924 B (1.85 % of the 64 MB FRDM flash), RAM 569,804 B (57.96 % of 960 KB); SMU1/SMU2 are fixed regions.

Windows problem in upstream: the gateway `CMakeLists.txt` generates `git_describe.h` by running a `.sh` script through `cmd /C`, which on Windows hangs the build forever (`Generating git_describe.h, always_run`). The proof build was finished after temporarily replacing that block with `execute_process(git describe ...)` + `file(WRITE ...)` in the pouch checkout (reverted afterwards; the checkout is clean at 32ded9b). Our own gateway app (`apps\pouch_gateway`) carries the same fix.

## Gateway board definition `pouch_gateway/rw612` (2026-11-13)

`boards\pouch_gateway\`, derived from Zephyr's `frdm_rw612`, for the Murata Type 2FR module (LBES0ZZ2FR, NXP RW612, Wi-Fi only) on `hardware\gateway`. Pins come from the KiCad netlist (`kicad-cli sch export netlist` on `hardware\gateway\pouch_gateway.kicad_sch`, 2026-11-13; no KiCad file was edited). Module pin names `GPIO_nn` are the RW612 GPIO numbers (Murata datasheet SP-ZZ2FR Rev 5.1 table 8, which also gives the supply domain); on the RW612 `hsgpio0` is GPIO_0-31 and `hsgpio1` is GPIO_32-63.

| Function | Net / part | U1 pin | RW612 pin | Zephyr | Supply |
| --- | --- | --- | --- | --- | --- |
| Console UART RX | UART_RX, J4.3 (DNP; J4.1 GND, J4.2 is TX) | 97 | GPIO_24, FC3 USART | `flexcomm3` 115200 8N1, console, shell, mcumgr | VIO_3, 3.3 V |
| Console UART TX | UART_TX, J4.2 (DNP) | 99 | GPIO_26, FC3 USART | `flexcomm3` | VIO_3 |
| USB-C data | USB_DP / USB_DM via D1 to J1 | 29 / 30 | dedicated | `zephyr_udc0` = `usb_otg` enabled (no CDC-ACM node yet) | AVDD33_USB |
| USB VBUS sense | R5 0R from +5V | 33 | USB_VBUS | n/a | abs max 5.25 V |
| LED red D3 (R14 470R) | LED_R | 63 | GPIO_51 = `hsgpio1` 19 | `led_red` (`led1`), active low | VIO_1 |
| LED green D4 (R15 100R) | LED_G | 113 | GPIO_53 = `hsgpio1` 21 | `led_green` (`led0`), active low | VIO_1 |
| LED blue D5 (R16 100R) | LED_B | 64 | GPIO_52 = `hsgpio1` 20 | `led_blue` (`led2`), active low | VIO_1 |
| USER button SW3 (R17 100R, R18 10k pull-up) | BTN_USER | 87 | GPIO_25 = `hsgpio0` 25 | `user_button` (`sw0`), active low; Pouch uses it to enable bonding | VIO_3 |
| LCD SCK, J5.4 via R21 33R | LCD_SCK | 82 | GPIO_48 | `&lcdic` LCD_SPI_SCK (`IO_MUX_LCD_SPI_IO48`) | VIO_6 |
| LCD DIN, J5.3 via R20 33R | LCD_DIN | 75 | GPIO_46 | `&lcdic` LCD_SPI_DATA | VIO_6 |
| LCD CS, J5.5 | LCD_CS | 81 | GPIO_49 | `&lcdic` LCD_SPI_SS | VIO_6 |
| LCD DC, J5.6 via R22 33R | LCD_DC | 12 | GPIO_47 | `&lcdic` LCD_SPI_DC | VIO_6 |
| LCD RST, J5.7 | LCD_RST | 115 | GPIO_44 | `&lcdic` LCD_SPI_RESET (function pin, `sleep-output = "high"`) | VIO_6 |
| LCD TE (TP1 only, panel has no TE) | LCD_TE | 111 | GPIO_45 | `&lcdic` LCD_SPI_TE muxed, unused | VIO_6 |
| LCD backlight, J5.8 via R23 0R | LCD_BL | 109 | GPIO_55 | SCT0 OUT9, `pwm-leds` `lcd_backlight` (1 kHz) | VIO_1 |
| SWD clock / data (J6 TC2030, J2 DNP) | SWCLK / SWDIO | 43 / 106 | GPIO_13 / GPIO_14 | not in devicetree (ROM debug port, selected by R10 5.1k on RF_CNTL_2 pin 55) | VIO_2 |
| Boot strap ISP (SW2, R11 5.1k) | EXT_REQ | 69 | EXT_REQ (not a GPIO) | not in devicetree; hold SW2 at reset for ISP mode | AVDD18 |
| Reset (SW1, R9 100R, R8 10k, C16) | PDN | 11 | PDn | not in devicetree | |
| Flash chip select | CS_Int_Flash to GPIO_28 via R6 0R, R7 10k to VDD18 | 80 / 98 | FlexSPI A | `&flexspi` `ext_flash_ctrl` | VDD18 |

J5 pin order (JST PH 8-pin): 1 +3V3, 2 GND, 3 DIN, 4 CLK, 5 CS, 6 DC, 7 RST, 8 BL. The panel (Waveshare 2in, ST7789VW, 240x320) is described as a **disabled** `sitronix,st7789v` node under `&lcdic` with the generic Zephyr parameter set; no display driver or LVGL work was done. All other U1 GPIOs are unconnected in the netlist (62 of them), as is USB_ID, RF_CNTL_0/1/3 and EXT_FREQ/GNT/PRI.

Flash: the module has 16 MB on FlexSPI port A. DT: `size = 16 MB`, partitions as FRDM (128 KB boot, 3 MB image-0 at 0x20000, 3 MB image-1 at 0x320000) with `storage` = 0x620000 to 16 MB (10,112 KB); `/lfs1` (Pouch credentials, settings) is on `storage`. The flash part number and JEDEC id are not in the datasheet ("16MB Winbond" only), so `jedec-id` is omitted and the driver skips the id check. The boot-ROM flash configuration block (`LBES0ZZ2FR_FCB.c`) is not the FRDM one (64 MB W25Q512JV, 32-bit addresses, which breaks boot on this module, Murata EVK guide for Zephyr section 7.1.1): it is the FCB at 0x400..0x603 of Murata's own prebuilt Type 2FR image (`github.com/murata-wireless/2FR`, `internal_flash_binaries\rdrw610_wifi_cli_intFlash_singleAnt.bin`, BSD-3-Clause). The built `zephyr.bin` was checked: bytes 0x400..0x603 are identical to Murata's.

Removed from the FRDM definition: Ethernet MAC/MDIO/KSZ8081 PHY, Arduino/mikroBUS/PMOD headers, flexcomm1 SPI, flexcomm2 I2C and the P3T1755 sensor, ADC, DAC, pSRAM, the 64 MB flash. The 32.768 kHz crystal is not fitted (`xtal32` stays disabled). Kept: NBU/IMU/HCI (Wi-Fi + BLE firmware is linked into the app), watchdog, DMA, PM states, `init.c` (iBuck, as FRDM and the Murata EVK).

Not clear from the netlist / datasheets (not guessed, see the report for the list): whether `init.c`'s `iBuck = true` is right for our supply scheme, the exact flash part (QE sequence in the FCB, `deviceModeArg 0x200`), the LCD backlight drive, and the Wi-Fi TX power tables (Murata publishes region tables for the 2FR; the FRDM default WW table is used).

Until 2026-11-10 this was `soil_moisture_fw\` at the repo root, with the board definitions in
`soil_moisture_fw\boards\others\`. See `docs\reorg_2026-11-10.md`.
