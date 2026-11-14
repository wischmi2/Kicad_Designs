# Pouch gateway (Golioth Pouch BLE to Wi-Fi gateway, NXP RW612)

Firmware for `hardware\gateway` (Murata Type 2FR / LBES0ZZ2FR, NXP RW612, Wi-Fi only). It scans for Pouch BLE nodes (the feather node in `..\feather_node`), connects, forwards their pouches to Golioth over Wi-Fi and disconnects.

Source: golioth/pouch `examples/zephyr/gateway` at **32ded9b** (main, v0.2.0 + 18), Copyright (c) 2025 Golioth, Inc., Apache-2.0, built out of this repo. Changes from upstream: `CMakeLists.txt` adds `firmware\` to `BOARD_ROOT`, writes `git_describe.h` with `execute_process` (upstream runs a `.sh` script through `cmd`, which hangs on Windows) and takes the ISRG Root X1 CA from the Pouch checkout instead of a copied `.der`; `boards\pouch_gateway.conf` merges upstream's `frdm_rw612.conf` + `frdm_rw612_wifi.conf`. `src\`, `prj.conf`, `Kconfig` and `app.overlay` are unchanged copies.

Status 2026-11-13: **builds only**. Nothing has been flashed or run; no hardware was attached.

## Targets

| Target | Command | Notes |
| --- | --- | --- |
| `pouch_gateway` (our board) | `.\scripts\build.ps1 -Target pouch_gateway` | board definition `..\..\boards\pouch_gateway\` (pins and open questions in `..\..\README.md`) |
| `frdm_rw612` with Wi-Fi | `.\scripts\build.ps1 -Target frdm_rw612` | NXP FRDM-RW612 dev board, same app, `-DEXTRA_CONF_FILE=boards/frdm_rw612_wifi.conf` |

`.\scripts\build.ps1` builds both, pristine (`west build -p`), into `C:\ncs\pouch-builds\gateway_pouch_gateway` and `...\gateway_frdm_rw612` (outside the repo). It needs the workspace `C:\ncs\pouch-zephyr` (Zephyr v4.4.0, Pouch 32ded9b, 8 Pouch patches applied by hand, hal_nxp blobs) and uses the NCS v3.4.0 toolchain bundle (Zephyr SDK 1.0.1) through `nrfutil sdk-manager toolchain launch`. How the workspace was made is in `..\..\README.md`. The script never flashes.

### Build results (2026-11-13, pristine, no warnings)

| Target | Flash | RAM |
| --- | --- | --- |
| `pouch_gateway` | 1,243,760 B (7.41 % of the 16 MB flash) | 569,804 B (57.96 % of 960 KB) |
| `frdm_rw612` Wi-Fi | 1,243,936 B (1.85 % of the 64 MB flash) | 569,804 B (57.96 %) |

The `SMU1`/`SMU2` lines in the linker summary (510 KB, 140 KB, 100 %) are fixed regions, not a problem. The Wi-Fi firmware (`rw61x_sb_wifi_a2.bin`) is linked into the image, so there is no separate Wi-Fi flash step with this Zephyr version.

## Flashing (printed, not run)

`west flash` does not work on Windows with this setup (the Pouch runner imports `pty`/`termios`), so program with SEGGER J-Link Commander. The gateway board has the Tag-Connect TC2030 (J6, with legs) as its debug port; J2 (10-pin 1.27 mm SWD) is not fitted. Use a J-Link that supports the RW612 (check the device list of your J-Link version) and the TC2030-CTX cable. Murata's guide loads the application at `0x08000000` (the FlexSPI alias of flash offset 0; the image starts with the boot header and the flash configuration block).

Commands to run by hand once a board is on the bench (nothing here has been run):

```powershell
$bin = "C:\ncs\pouch-builds\gateway_pouch_gateway\zephyr\zephyr.bin"
@"
loadbin $bin, 0x08000000
r
g
exit
"@ | Set-Content -Encoding ascii "$env:TEMP\gw_flash.jlink"
& "C:\Program Files\SEGGER\JLink\JLink.exe" -device RW612 -if SWD -speed 4000 -autoconnect 1 -CommanderScript "$env:TEMP\gw_flash.jlink"
```

Notes:
- Do not erase the whole chip once the credentials are on the board: they live in the LittleFS `storage` partition (`0x620000`, 10,112 KB), and a chip erase wipes them. `loadbin` only writes the sectors it needs, and the image is about 1.2 MB, far below the storage partition.
- On the first power-up of a new board the boot ROM reads the flash configuration block at flash offset `0x400` (Murata's, copied into `boards\pouch_gateway\LBES0ZZ2FR_FCB.c`). If the board does not boot, ISP mode (hold SW2 ISP at reset) still works; the FCB is the first thing to check.
- J-Link with the RW612 and sleep: the same caveat as the nRF54L15 may apply (link drops when the chip sleeps); use the latest J-Link software.

## Console, Wi-Fi and Golioth credentials

The shell and mcumgr run on the UART `flexcomm3` (115200 8N1, 3.3 V) at **J4**, which is **not fitted** on Rev A (J2 and J4 are DNP). Fit a 3-pin 2.54 mm header at J4 (pins: 1 GND, 2 board TX, 3 board RX) and connect a 3.3 V USB-UART adapter (adapter RX to J4.2, adapter TX to J4.3). There is no USB console in the firmware yet (a CDC-ACM console would need a devicetree node and the USB device stack; not done). RTT is not enabled either.

### Wi-Fi

In the shell (use your own SSID and password; do not write them into a file in the repo):

```
uart:~$ wifi cred add -s <your-wifi-ssid> -p <your-wifi-password> -k 1
uart:~$ wifi cred auto_connect
```

`-k 1` is WPA2-PSK. The credentials go to the Wi-Fi credentials library (`CONFIG_WIFI_CREDENTIALS`); whether they survive a reset on this build was not tested. `wifi cred auto_connect` makes the gateway connect on its own.

### Golioth credentials (mcumgr to `/lfs1/credentials/`)

The gateway needs its own Golioth device certificate and private key (DER, mTLS), separate from the nodes'. Never commit them: `.gitignore` covers `*.der`, `*.pem`, `*.crt`, `*.key` and credential hex files. Upload over the shell UART with the mcumgr CLI (Go tool from the mynewt-mcumgr repository, as in the upstream Pouch README), with the shell UART on `COM<n>`:

```
mcumgr --conntype serial --connstring "dev=COM<n>,baud=115200" fs upload <gateway>.crt.der /lfs1/credentials/crt.der
mcumgr --conntype serial --connstring "dev=COM<n>,baud=115200" fs upload <gateway>.key.der /lfs1/credentials/key.der
```

The app creates `/lfs1/credentials` itself if it is missing. Convert PEM to DER with `openssl x509 -inform PEM -outform DER -in c.pem -out crt.der` and `openssl pkcs8 -topk8 -nocrypt -inform PEM -outform DER -in k.pem -out key.der`. After the upload, reset the board: the log shows the gateway version, the Wi-Fi connection and `Gateway pouch forwarded` lines when a node syncs.

The server CA is ISRG Root X1, built in.

## Not done / open

- Display: the J5 panel (`st7789v_lcd`) is a disabled devicetree node; no driver, LVGL or UI.
- Wi-Fi TX power: the FRDM default (WW) table is used; Murata publishes region tables for the Type 2FR (`github.com/murata-wireless/2FR`, `PowerTable\`). Apply the right one before any certification or field use.
- Flash part: the module datasheet only says "16MB Winbond". `jedec-id` is not set, and the FCB is copied from Murata's prebuilt Type 2FR image (see the board README section).
- No MCUboot / OTA yet (the FRDM-style `image-0` / `image-1` partitions exist but the app is linked at flash offset 0).
- Whether the gateway works without the external pSRAM (the FRDM board has an 8 MB part, disabled in its devicetree, so the example does not use it): consistent with this build, but unproven on hardware.
