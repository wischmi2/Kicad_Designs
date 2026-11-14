# Firmware

nRF Connect SDK (Zephyr) firmware for the nRF54L15 boards in `hardware\`.

| Folder | What |
| --- | --- |
| `boards\nrf54l15_feather\` | Board definition `nrf54l15_feather/nrf54l15/cpuapp` (main feather, `hardware\feather\`) |
| `boards\soil_moisture\` | Board definition `soil_moisture/nrf54l15/cpuapp` (old soil-moisture board, `hardware\archive\`) |
| `apps\feather_node\` | Golioth Pouch BLE node (MCUboot, LittleFS credentials, nPM1300 fuel gauge, SENS_ID uplink on `.s/sensor`). Build/flash/provision scripts in `scripts\`, notes in `README.md` and `HW_VERIFY.md` |

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

Until 2026-11-10 this was `soil_moisture_fw\` at the repo root, with the board definitions in
`soil_moisture_fw\boards\others\`. See `docs\reorg_2026-11-10.md`.
