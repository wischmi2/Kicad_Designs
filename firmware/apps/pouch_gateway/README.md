# Pouch gateway (Golioth Pouch BLE to Wi-Fi gateway, NXP RW612)

Firmware for `hardware\gateway` (Murata Type 2FR / LBES0ZZ2FR, NXP RW612, Wi-Fi only). It scans for Pouch BLE nodes (the feather node in `..\feather_node`), connects, forwards their pouches to Golioth over Wi-Fi and disconnects.

Source: golioth/pouch `examples/zephyr/gateway` at **32ded9b** (main, v0.2.0 + 18), Copyright (c) 2025 Golioth, Inc., Apache-2.0, built out of this repo. Changes from upstream: `CMakeLists.txt` adds `firmware\` to `BOARD_ROOT`, writes `git_describe.h` with `execute_process` (upstream runs a `.sh` script through `cmd`, which hangs on Windows) and takes the ISRG Root X1 CA from the Pouch checkout instead of a copied `.der`; `boards\pouch_gateway.conf` merges upstream's `frdm_rw612.conf` + `frdm_rw612_wifi.conf`. `app.overlay`, `credentials.*`, `wifi.*` and `fatal_error.c` are unchanged copies. 2026-11-13 additions for MCUboot and OTA: `sysbuild.conf`, `sysbuild\mcuboot.conf`, `VERSION`, `src\fw_update.c/.h` (from Pouch `examples/zephyr/coap_client/src/fw_update.c`, with a test-mode upgrade and the confirm function), the confirm calls in `src\main.c`, `CONFIG_GOLIOTH_OTA` + `CONFIG_IMG_MANAGER` in `prj.conf`, and the `EXAMPLE_FW_UPDATE_COMPONENT` option in `Kconfig`.

Status 2026-11-13: **builds only**. Nothing has been flashed or run; no hardware was attached. Since the same day the build is a sysbuild with MCUboot, and the gateway can update itself over Golioth (OTA). None of the boot, OTA or rollback behaviour below has been tried on hardware.

## Targets

| Target | Command | Notes |
| --- | --- | --- |
| `pouch_gateway` (our board) | `.\scripts\build.ps1 -Target pouch_gateway` | board definition `..\..\boards\pouch_gateway\` (pins and open questions in `..\..\README.md`) |
| `frdm_rw612` with Wi-Fi | `.\scripts\build.ps1 -Target frdm_rw612` | NXP FRDM-RW612 dev board, same app, `-DEXTRA_CONF_FILE=boards/frdm_rw612_wifi.conf` |

`.\scripts\build.ps1` builds both with `west build --sysbuild`, pristine (`-p`), into `C:\ncs\pouch-builds\gateway_pouch_gateway` and `...\gateway_frdm_rw612` (outside the repo). It needs the workspace `C:\ncs\pouch-zephyr` (Zephyr v4.4.0, Pouch 32ded9b, 8 Pouch patches applied by hand, hal_nxp blobs) and uses the NCS v3.4.0 toolchain bundle (Zephyr SDK 1.0.1) through `nrfutil sdk-manager toolchain launch`. How the workspace was made is in `..\..\README.md`. The script never flashes.

### Build results (2026-11-13, pristine sysbuild)

| Target | App (`pouch_gateway`) flash | App RAM | MCUboot flash | MCUboot RAM |
| --- | --- | --- | --- | --- |
| `pouch_gateway` | 1,245,900 B (39.66 % of the 3,141,296 B image-0 slot; 7.4 % of the 16 MB flash) | 570,524 B (58.04 % of 960 KB) | 59,804 B (45.63 % of the 128 KB `mcuboot` partition) | 55,544 B (5.65 %) |
| `frdm_rw612` Wi-Fi | 1,246,076 B (39.67 % of the slot) | 570,524 B (58.04 %) | 59,988 B (45.77 %) | 55,544 B (5.65 %) |

Before MCUboot and OTA (same day, single image linked at flash offset 0): flash 1,243,760 B, RAM 569,804 B. So `CONFIG_GOLIOTH_OTA` + `IMG_MANAGER` + `fw_update.c` cost **2,140 B of flash and 720 B of RAM** (the 512-byte `flash_img` write buffer plus state). The image is streamed to flash, so an update needs no pSRAM and no download buffer in RAM.

Warnings (none in the app): two CMake warnings in the MCUboot part. One is the default signing key (below). The other is `CONFIG_MBEDTLS_DECLARE_PRIVATE_IDENTIFIERS is discouraged` (`zephyr/modules/mbedtls/legacy_support.cmake`), which comes from MCUboot's default RSA-2048 signature check, not from our code (a switch to ECDSA P-256 in sysbuild would probably silence it; not tried). The `SMU1`/`SMU2` lines in the linker summary (510 KB, 140 KB, 100 %) are fixed regions, not a problem. The Wi-Fi firmware (`rw61x_sb_wifi_a2.bin`) is linked into the app image, so there is no separate Wi-Fi flash step with this Zephyr version.

### Outputs

| Image | `pouch_gateway` (our board) | `frdm_rw612` |
| --- | --- | --- |
| MCUboot | `C:\ncs\pouch-builds\gateway_pouch_gateway\mcuboot\zephyr\zephyr.bin` (and `zephyr.hex`) | `C:\ncs\pouch-builds\gateway_frdm_rw612\mcuboot\zephyr\zephyr.bin` |
| Signed app, program this | `C:\ncs\pouch-builds\gateway_pouch_gateway\pouch_gateway\zephyr\zephyr.signed.bin` (and `zephyr.signed.hex`) | `C:\ncs\pouch-builds\gateway_frdm_rw612\pouch_gateway\zephyr\zephyr.signed.bin` |
| Golioth OTA artifact | the same `zephyr.signed.bin` | the same |
| ELF (Memfault, debugging) | `...\pouch_gateway\zephyr\zephyr.elf` | same layout |

The unsigned `zephyr.bin` / `zephyr.hex` in the app folder are **not** what MCUboot boots; always use the `.signed` files. The `.hex` files use the XIP addresses (`0x18000000` and up); the J-Link commands below use the `.bin` files with explicit addresses.

### Flash layout, MCUboot and signing

Layout (`..\..\boards\pouch_gateway\pouch_gateway.dts`, unchanged: it was copied from `frdm_rw612` and already has the four partitions MCUboot needs):

| Partition | Flash offset | Size | J-Link address | CPU address (XIP) | Content |
| --- | --- | --- | --- | --- | --- |
| `mcuboot` (`boot_partition`) | `0x000000` | 128 KB | `0x08000000` | `0x18000000` | MCUboot: ROM flash configuration block at `0x400`, image vector table at `0x1000`, code from `0x1300`; 59,804 B used |
| `image-0` (`slot0_partition`) | `0x020000` | 3 MB | `0x08020000` | `0x18020000` | signed app: 1 KB MCUboot header, app code from `0x18020400` |
| `image-1` (`slot1_partition`) | `0x320000` | 3 MB | `0x08320000` | `0x18320000` | downloaded OTA image (`flash_img` writes here) |
| `storage` | `0x620000` | 10,112 KB | | | LittleFS `/lfs1`: credentials, settings |

Why the layout needed no change: the board already had `zephyr,code-partition = &slot0_partition`, so with MCUboot the app links at `0x18020000` (`CONFIG_FLASH_LOAD_OFFSET=0x20000`, `CONFIG_ROM_START_OFFSET=0x400` for the image header). MCUboot's own build keeps the NXP boot header (`CONFIG_NXP_RW6XX_BOOT_HEADER`, the board's `LBES0ZZ2FR_FCB.c`, IVT at `0x1000`) and links at `0x0` in a 128 KB region without any overlay (the feather needed an overlay for this; here the boot partition comes out right by itself, checked in the build output). The FCB tag `FCFB` is at `0x400` of MCUboot's `zephyr.bin`. Both slots are equal and the app uses 40 % of a slot. Mode: Zephyr 4.4.0's sysbuild default, **swap using offset** (no scratch partition; `flash_img` handles the one-sector offset). Zephyr 4.4.0 has no RW612 board file in MCUboot's `boot/zephyr/boards`; the SoC code supports it (`soc/nxp/rw/Kconfig`: boot header only without `BOOTLOADER_MCUBOOT`, `ROM_START_OFFSET=0x400` for apps), and Golioth's `coap_client` example builds the same way for `frdm_rw612` (`sysbuild.conf` only).

Versions: the `VERSION` file (1.0.0) is the single source. It becomes `APP_VERSION_STRING` (the Golioth package version, `1.0.0`), the MCUboot image header (`1.0.0+0`, `CONFIG_MCUBOOT_IMGTOOL_SIGN_VERSION`) and a boot log line `Gateway app version (MCUboot / Golioth package): 1.0.0`. The Golioth package name is `CONFIG_EXAMPLE_FW_UPDATE_COMPONENT`, default `gateway`.

**Signing key: the default MCUboot debug key** (`bootloader/mcuboot/root-rsa-2048.pem` in the workspace, RSA-2048, public in every MCUboot checkout). CMake warns about it at every build. That is fine for the bench only. A production key (where it is stored, and RSA or ECDSA P-256) is a later decision; images signed with the debug key will not boot on a gateway whose MCUboot carries the production key, so decide before anything ships. Never commit a private key.

### Image confirm (rollback safety net)

An OTA image is installed in **test mode** (`BOOT_UPGRADE_TEST`): MCUboot swaps it in, boots it once, and reverts to the old image at the next reset unless the app confirms it. `src\main.c` calls `fw_update_confirm_healthy()` only after all of this succeeded on the new image: Wi-Fi associated and IPv4 address (`wait_for_network()`), cloud transport ready (`pouch_gateway_cloud_ensure_ready()`), `bt_enable()` and `pouch_gateway_scan_start()`, and then the first periodic `pouch_coap_client_sync()` (30 s after boot) returning 0, i.e. a DTLS handshake and Pouch sync with Golioth. With `CONFIG_POUCH_GATEWAY_CLOUD=n` it confirms right after the scan starts. On a normal boot or a freshly flashed image the image is already confirmed and the call does nothing. The fatal error handler resets the board, so a crash loop on an unconfirmed image reverts. A hang does not reset by itself (no watchdog yet). A manifest for a newer version is ignored while the running image is unconfirmed.

## Flashing (printed, not run)

`west flash` does not work on Windows with this setup (the Pouch runner imports `pty`/`termios`), so program with SEGGER J-Link Commander. The gateway board has the Tag-Connect TC2030 (J6, with legs) as its debug port; J2 (10-pin 1.27 mm SWD) is not fitted. Use a J-Link that supports the RW612 (check the device list of your J-Link version) and the TC2030-CTX cable. Murata's guide loads at `0x08000000`, the FlexSPI alias of flash offset 0 (see the layout table above for every address).

Commands to run by hand once a board is on the bench (nothing here has been run). First programming of a board writes **both** MCUboot and the signed app:

```powershell
$b = "C:\ncs\pouch-builds\gateway_pouch_gateway"
@"
loadbin $b\mcuboot\zephyr\zephyr.bin, 0x08000000
loadbin $b\pouch_gateway\zephyr\zephyr.signed.bin, 0x08020000
r
g
exit
"@ | Set-Content -Encoding ascii "$env:TEMP\gw_flash.jlink"
& "C:\Program Files\SEGGER\JLink\JLink.exe" -device RW612 -if SWD -speed 4000 -autoconnect 1 -CommanderScript "$env:TEMP\gw_flash.jlink"
```

To reprogram only the application (MCUboot unchanged), drop the first `loadbin`. A freshly loaded signed image is treated as confirmed (it is written to slot 0 directly, not through an upgrade request), so no health check runs on it; OTA images go through the test-mode path.

Notes:
- Do not erase the whole chip once the credentials are on the board: they live in the LittleFS `storage` partition (`0x620000`, 10,112 KB), and a chip erase wipes them. `loadbin` only writes the sectors it needs; MCUboot ends below `0x10000` and the app ends near `0x155000`, far below `storage`.
- No gateway board has ever been flashed with the older single-image build (app at flash offset 0), so there is nothing to clean up. If a board did run it, the old code sits at `0x0`..`0x13c000`: the MCUboot and app writes overwrite it, and a stale tail inside `image-0` is ignored. `image-1` should read as erased (`0xFF`) at its end (the MCUboot trailer is at the end of the slot); erase only inside `0x320000`..`0x61FFFF`, never the `storage` range.
- On the first power-up of a new board the boot ROM reads the flash configuration block at flash offset `0x400` (Murata's, copied into `boards\pouch_gateway\LBES0ZZ2FR_FCB.c`, part of the MCUboot image now). If the board does not boot, ISP mode (hold SW2 ISP at reset) still works; the FCB is the first thing to check.
- J-Link with the RW612 and sleep: the same caveat as the nRF54L15 may apply (link drops when the chip sleeps); use the latest J-Link software.

## OTA update (Golioth), release steps

How it works, the Pouch v0.2.0 source facts, and the promotion checklist are in `hardware\gateway\docs\OTA_and_Memfault.md` (sections 3, 6 and 7). Short version for a gateway release:

1. Bump `VERSION` in this folder (a different version from the one running; `1.0.1` and so on).
2. `.\scripts\build.ps1 -Target pouch_gateway` (pristine sysbuild).
3. Take `C:\ncs\pouch-builds\gateway_pouch_gateway\pouch_gateway\zephyr\zephyr.signed.bin` and upload it to the Golioth package `gateway` as version `<VERSION string>` (console or `goliothctl dfu`). The package version must equal `APP_VERSION_STRING`, otherwise the device re-downloads the image after every update.
4. Create a deployment with the `gateway` artifact in a `dev` cohort, watch the gateway log (UART J4, not fitted on rev A): `Update ... postponed`, then the download, `Rebooting to apply upgrade`, MCUboot swap, `Image confirmed (version x.y.z)` about 30 s after boot.
5. Test the rollback once per major change: a build that never confirms (for example Wi-Fi credentials removed) must return to the old version at the next reset.
6. Promote the deployment to `field` after the soak.

Needs a bench test first: whether the Golioth cloud offers the manifest to this device at all (package name, cohort), the download time (the CoAP mutex blocks BLE forwarding for the whole download), flash writes while Wi-Fi and BLE run, and that MCUboot really boots from the FCB/IVT layout above.

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
- MCUboot and OTA are built but unproven: no boot test, no real update, no rollback test. Production signing key not chosen (debug key). No watchdog (a hung unconfirmed image does not revert until the next reset). The Golioth package `gateway` and its cohorts do not exist yet.
- Whether the gateway works without the external pSRAM (the FRDM board has an 8 MB part, disabled in its devicetree, so the example does not use it): consistent with this build, but unproven on hardware. OTA does not need pSRAM (the image is streamed to flash; +720 B RAM).
