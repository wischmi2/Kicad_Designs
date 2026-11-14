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

Until 2026-11-10 this was `soil_moisture_fw\` at the repo root, with the board definitions in
`soil_moisture_fw\boards\others\`. See `docs\reorg_2026-11-10.md`.
