# Golioth Pouch v0.2.0 for the feather node and the gateway (2026-11-13)

Brian wants Pouch v0.2.0 on both the nRF54L15 feather (node) and the pouch gateway (RW612). He has already run v0.2.0 on the ReefWatch solar board (`hardware\archive\nrf54l15_v3`, nRF54L15 + nPM1300 + AEM10330) as a Pouch node, with an nRF9160 DK as the gateway. This note collects that work, what is on disk, and what the feather and gateway firmware need. Nothing was built in this session.

## The solar board firmware (github.com/wischmi2/nrf54l15_solar_pouch)

Five commits, 2026-10-08 to 2026-10-17. Local path on the laptop: `C:\Users\Brian\pouch_nrf54l15_v3`. SDK: NCS **v3.4.0** at `C:\ncs\pouch-ncs` (laptop; not on this desktop). Build target `nrf54l15dk/nrf54l15/cpuapp` plus `boards\nrf54l15dk_nrf54l15_cpuapp.overlay` (no custom board definition). App is golioth/pouch v0.2.0 `examples/zephyr/ble_gatt` with these changes:

- `src\solar_status.c`: nPM1300 snapshot thread; uplink is one JSON object on `.s/sensor` (`vbat_mv`, `soc_pct`, `ibat_ma`, `charge`, `vbus`, `usb_cc`, `source`, `aem`, `aem_window`, `vbat_rise_mv`). AEM10330 thresholds 4.05 / 3.50 / 3.00 V.
- Gateway sharing: sync-request flag set for 30 s (`CONFIG_EXAMPLE_ADV_WINDOW_S`), then clear for 300 s (`CONFIG_EXAMPLE_SYNC_PERIOD_S`), so one gateway can serve several nodes. Advertising restarts after a disconnect.
- prj.conf: device name `Pouch_v3`; RTT logging (deferred, drop mode, 8 KB up buffer); shell, console, serial and MCUmgr all off (the shell's 10 ms RTT poll keeps the CPU out of idle); `CONFIG_NRF_APPROTECT_DISABLE` and `CONFIG_NRF_SECURE_APPROTECT_DISABLE`; Pouch GATT/transport debug logs on.
- sysbuild: MCUboot; `CONFIG_LTO_SINGLE_THREADED=y` (parallel LTO loses objects on Windows).

### Status as of 2026-10-17

Laptop export `G:\My Drive\Transfer\solar_board_nrf54l15_v3\` (2026-11-13) has the same app at cebb66a (no device cert/key), `prebuilt\zephyr.signed.hex/.bin/.elf`, the bring-up tests (`nordic_solar_fw\`, repo wischmi2/nrf54l15_solar @ 0aaf786, uncommitted edits in `04_ble_battery_solar`), and two logs: `solar-build.log` and `gateway-vcom1.log`.

- Node boots, loads its credentials from LittleFS, initialises Pouch and advertises for a gateway. RTT works. Build: NCS v3.4.0 (f30459884d7f), Zephyr 4.4.1, Pouch from `C:\ncs\pouch-ncs\pouch`.
- The app README says no gateway session completed (9160 DK DTLS `-113`, DNS `-101`). **`gateway-vcom1.log` (2026-10-17 ~12:00) shows otherwise:** the 9160 DK gateway (`Gateway Version: v0.2.0-18-g32ded9b-dirty`, NCS v3.4.0, Zephyr 4.4.1, cellular via the nRF91 serial modem) completed 12 sessions with peripheral `F1:02:1E:C1:1A:BF`, about every 2 min 12 s: BT security level 2, `Peripheral device certificate uploaded (381 bytes)`, `Forwarding 317 bytes of peripheral data to cloud`, `Gateway pouch forwarded`. 381 bytes is the size of `nrf54l15_v3_solar.crt.der`, and the 2-minute cycle matches commit ed6e768, so that peripheral is very likely the solar board. A second Pouch board (`D9:A4:79:0F:08:02`, 371-byte cert) mostly fails with `Failed to set security (244)` / `BT security change failed ... err 9` (a bond or pairing problem) but also got some uplinks through. CoAP `request timeout (retry 0/3)` and `Ignoring piggyback ACK` warnings repeat but recover. The log doesn't show whether the data appeared in the Golioth console; confirm there.
- The DTLS/DNS failures in the README are probably from a run before or after this log. The gateway is not reliable yet, but the full chain has worked at least once.
- The image on the board is still a debug build (fast advertising, 10 s heartbeat), which draws more than the panel's ~0.1 mA.
- The device certificate `nrf54l15_v3_solar` was valid **2026-10-09 to 2026-11-06, so it has expired** (today is 2026-11-13). A new one is needed before the next try.

### Lessons that apply to the feather

| Lesson | Solar board fix | Feather today |
| --- | --- | --- |
| No 32 kHz crystal: the DK default LFXO makes GRTC wait forever and `main` never runs | `&lfxo { status = "disabled"; }`, `CONFIG_CLOCK_CONTROL_NRF_K32SRC_RC=y`, `CONFIG_NRF_GRTC_TIMER_SOURCE_LFLPRC=y`, in the app **and** in MCUboot | **Missing.** X2 is DNP on the feather, but `nrf54l15_feather_nrf54l15_cpuapp.dts` leaves `&lfxo` enabled and no K32SRC_RC is set. Would hang at boot |
| SCL is P1.03, an NFC pin | `&uicr { nfct-pins-as-gpios; }`, `&nfct { status = "disabled"; }`, in the app and in MCUboot | **Missing.** The feather uses the same P1.03 SCL; without this the PMIC I2C bus would not work |
| MCUboot linked into the app slot (the sysbuild `mcuboot.overlay` replaces MCUboot's own `app.overlay`) | `chosen { zephyr,code-partition = &boot_partition; }` at the top of `sysbuild\mcuboot.overlay` | Not set up yet (no MCUboot) |
| Access port locked once; `recover` wipes all NVM including the credentials | APPROTECT disable Kconfigs; always program with `chip_erase_mode=ERASE_NONE` | Add the same |
| `west flash` fails on Windows (pouch runner imports `pty`/`termios`) | Build with west, program with `nrfutil device program ... --options chip_erase_mode=ERASE_NONE,verify=VERIFY_READ` (MCUboot hex at 0x0, then `zephyr.signed.hex` at 0x10000, no merged.hex) | `scripts\flash.ps1` needs the same |
| J-Link V9.36 drops the link when the nRF54L15 sleeps | Use J-Link V9.82 | Same |
| RTT auto-search misses the control block (KMU-reserved RAM at 0x20000000) | Fixed address from `_SEGGER_RTT` in `zephyr.map` (0x20002070 with the 8 KB buffer) | Same |
| No UART, so the example's mcumgr provisioning can't be used | Build a LittleFS image with `littlefs-python` 0.19.0 (`/credentials/crt.der`, `/credentials/key.der`; block 4096 x 9, read/prog 16, cache 64, lookahead 32, cycles 512), write it as Intel hex at the storage partition (0x174000, 0x9000), `nrfutil device erase --pages 0x174000-0x17D000`, then program with ERASE_NONE. Never keep the hex (it holds the private key) | Same method works over the feather's TC2030 SWD. Answers the provisioning question for bench builds |
| nPM1300 LEDs sink ~5 mA and latch across an nRF reset | LED modes `host`, then write CLR | Check the feather's LED wiring |

Differences to keep: the solar board holds ANT_SEL **high** (external connector) and uses BUCK1 at 1.8 V for the RF switch. The feather holds ANT_SEL **low** (chip antenna AE1), BUCK1 stays off, the switch runs from VRF (LDO2, 2.5 V), and VSENS is LDO1. Keep the feather's own board definition (better than a DK overlay), and copy the solar board's LFXO/NFC/MCUboot/flash fixes into it.

## Two different "v0.2.0" releases

| Repo | Tag | Date | What it is | SDK pinned |
| --- | --- | --- | --- | --- |
| golioth/pouch (node SDK) | v0.2.0, aa27b019 | 2026-07-23 | Node library and examples. Gateway code merged into this repo and rewritten on CoAP | `west-ncs.yml`: NCS v3.4-branch (Zephyr 4.4.0). `west-zephyr.yml`: Zephyr v4.4.0 + hal_nxp |
| golioth/bluetooth-gateway (was pouch-gateway) | v0.2.0, 5ce2d8c9 | 2025-10-13 | Older stand-alone gateway app (FRDM-RW612, Thingy:91 X, nRF9160 DK) | golioth-firmware-sdk v0.20.0 -> NCS v3.0.1; Pouch 64ee488 (v0.1.0 + 8) |

The solar board run used golioth/pouch v0.2.0 on both sides (node `ble_gatt`, 9160 DK gateway on the nRF52840 + serial modem). The gateway was actually golioth/pouch **main at 32ded9b (v0.2.0 + 18) with local edits** ("-dirty"), the same commit as `C:\Users\Brian\pouch-1` on this desktop. The laptop's local gateway edits are not in the export. That is the pair to follow. bluetooth-gateway v0.2.0 is the older line and carries an older Pouch library; don't mix it with a v0.2.0 node.

Upstream golioth/pouch has only v0.1.0 and v0.2.0; main is v0.2.0 + 18 (CI, plus 2 fixes: SAR receiver stops ack retry on fatal bearer errors; an over-long server-cert serial no longer silently succeeds).

## What is on disk

- `G:\My Drive\Transfer\golioth_pouch_v0.2.0\` (laptop export 2026-11-13, clean tags, no credentials): `pouch_node_sdk\` = golioth/pouch v0.2.0; `pouch_gateway\` = golioth/bluetooth-gateway v0.2.0; `gateway_prebuilt_frdm_rw612\` = bluetooth-gateway release v0.2.0 RW612 Wi-Fi/Ethernet hex + J-Link scripts.
- `C:\Users\Brian\pouch_xiao_nrf54l15\prebuilt-9160\`: Golioth's pouch v0.2.0 9160 DK images (gateway on the nRF52840, `ncs-serial-modem` on the nRF9160, 2026-07-23). Same layout as the solar board's gateway.
- `C:\Users\Brian\pouch-1\`: golioth/pouch main (v0.2.0 + 18). Untracked `nxp_rw612.crt.der/.key.der` (credentials, keep out of git).
- `C:\Users\Brian\pouch_gateway\`, `pouch_gateway_clean\`: older bluetooth-gateway v0.2.0 + 46/42 workspaces on NCS v3.1.1 (9160 DK, Pouch v0.1.0 + 18). Superseded.
- `C:\Users\Brian\pouch_xiao_nrf54l15\`: XIAO nRF54L15 fork (v0.1.0 + 244, June 2026), worked end to end with an FRDM-RW612 gateway. `docs\fix-cert-verify-2700-8.md` has the `0x2700, 8` cert fix.
- `C:\ncs\` on this desktop: NCS v2.9.0 to v3.2.3 only. NCS v3.4.0 (`C:\ncs\pouch-ncs`) exists on the laptop only.

## Gateway side

Our gateway board is the Murata Type 2FR (NXP RW612), Wi-Fi only. Follow golioth/pouch v0.2.0 `examples/zephyr/gateway` on the Zephyr v4.4.0 manifest: `frdm_rw612` + `boards/frdm_rw612_wifi.conf`, Wi-Fi via `wifi cred add` in the shell, credentials over mcumgr to `/lfs1/credentials/` (the gateway has USB/UART, so this works as documented). Needs a board definition derived from `frdm_rw612` (pins, LCD on J5, LEDs, the 2FR module's flash). Not written yet.

The 9160 DK cellular gateway is still failing DTLS/DNS. The RW612 Wi-Fi path avoids the modem, and the XIAO work proved RW612 gateway -> Golioth before.

## Feather node side

1. NCS v3.4.0 workspace on the desktop (match the laptop's `C:\ncs\pouch-ncs`).
2. Port the solar board's app (`nrf54l15_solar_pouch`) onto the feather board definition: swap `solar_status.c` for the feather's PMIC/fuel gauge/SENS_ID code, add the LFXO-off/RC, NFC-pins, MCUboot overlay and APPROTECT fixes. Recheck nPM1300 devicetree properties on NCS v3.4 (last checked on v3.2.3).
3. Provisioning on the bench: the solar board's LittleFS-image method over TC2030 SWD. For field units later, consider mcumgr over BLE.
4. Low-power build: the 30 s / 300 s request pattern is in place; slow the advertising and drop the heartbeat before battery tests.

## Open questions for Brian

1. Did the solar board's `.s/sensor` data show up in the Golioth console on 2026-10-17 (the gateway log says it was forwarded)? Keep using the 9160 DK gateway for the feather, or move to the RW612 Wi-Fi gateway (FRDM-RW612 prebuilt now, our board later)?
2. Use golioth/pouch main 32ded9b (what the gateway ran) for both sides? What were the gateway's local ("-dirty") edits on the laptop?
3. OK to install NCS v3.4.0 on the desktop (several GB), and to fix the two missing feather board-definition items (LFXO/RC, NFC pins) now? Both are firmware only, no hardware change.
4. The solar board's certificate expired 2026-11-06; reissue for more tests on that board?
