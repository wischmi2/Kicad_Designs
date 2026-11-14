# Golioth Pouch v0.2.0 for the feather node and the gateway (2026-11-13)

Brian wants Pouch v0.2.0 on both the nRF54L15 feather (node) and the pouch gateway (RW612). He already has v0.2.0 working on another Bluetooth solar board as a Pouch node, with an nRF9160 DK as the gateway. This note collects what is on disk, what the two "v0.2.0" releases are, and what the feather and gateway firmware need. Nothing was built.

## Two different "v0.2.0" releases

| Repo | Tag | Date | What it is | SDK pinned |
| --- | --- | --- | --- | --- |
| golioth/pouch (node SDK) | v0.2.0, aa27b019 | 2026-07-23 | Node library and examples. Gateway code merged into this repo and rewritten on CoAP | `west-ncs.yml`: NCS v3.4-branch (f304598, Zephyr 4.4.0). `west-zephyr.yml`: Zephyr v4.4.0 + hal_nxp |
| golioth/bluetooth-gateway (was pouch-gateway) | v0.2.0, 5ce2d8c9 | 2025-10-13 | Stand-alone gateway app (FRDM-RW612 Wi-Fi/Ethernet, Thingy:91 X, nRF9160 DK) | golioth-firmware-sdk v0.20.0 -> NCS v3.0.1; Pouch at 64ee488 (v0.1.0 + 8, 2025-09-24) |

Upstream golioth/pouch has only two tags (v0.1.0, v0.2.0); main is v0.2.0 + 18 (CI, plus 2 fixes: SAR receiver stops ack retry on fatal bearer errors; over-long server-cert serial no longer silently succeeds).

The gateway v0.2.0 release carries Pouch from before the node SDK v0.2.0. So "v0.2.0 on both" can mean two things:
- (a) node on golioth/pouch v0.2.0 + gateway on golioth/bluetooth-gateway v0.2.0 (mixed Pouch library versions), or
- (b) node and gateway both from golioth/pouch v0.2.0 (`examples/zephyr/ble_gatt` + `examples/zephyr/gateway`).

Which pair ran on the solar board is not recorded in the exported files (see "Open questions").

## What is on disk

Transfer drive `G:\My Drive\Transfer\golioth_pouch_v0.2.0\` (exported from Brian's laptop 2026-11-13, clean tag exports, no local edits or credentials):
- `pouch_node_sdk\`: golioth/pouch v0.2.0.
- `pouch_gateway\`: golioth/bluetooth-gateway v0.2.0.
- `gateway_prebuilt_frdm_rw612\`: release v0.2.0 `frdm_rw612-wifi.hex/.elf`, `frdm_rw612-ethernet.hex`, J-Link scripts (`loadfile ... reset exit`).

Desktop (this PC):
- `C:\Users\Brian\pouch_gateway\`: west workspace, bluetooth-gateway v0.2.0 + 46 (6330d16, 2025-12-03, local edits to `gateway/CMakeLists.txt` and `gateway/src/main.c`), Pouch v0.1.0 + 18, NCS v3.1.1 (golioth-firmware-sdk v0.21.1 + 25). Has `nrf9160dk_nrf9160.hex` and `nrf9160dk_nrf52840.hex`, so this is most likely the 9160 DK gateway build. `pouch_gateway_clean\` is the same without the edits (v0.2.0 + 42).
- `C:\Users\Brian\pouch-node-ws\`: node workspace, Brian's fork wischmi2/pouch at v0.1.0 + 17, NCS v3.0.1, with `build_ble_gatt`, `build_gateway`, `certs`.
- `C:\Users\Brian\pouch-1\`: golioth/pouch main (v0.2.0 + 18). Untracked `nxp_rw612.crt.der/.key.der` in it (credentials, keep out of git).
- `C:\Users\Brian\pouch_xiao_nrf54l15\`: Brian's fork (v0.1.0 + 244, June 2026), XIAO nRF54L15 node + FRDM-RW612 gateway working end to end. `docs\fix-cert-verify-2700-8.md` has the fix for `cert: Failed verifying server cert: 0x2700, 8`. `prebuilt-9160\` has Golioth's pouch v0.2.0 images for the 9160 DK (gateway on nRF52840, ncs-serial-modem on nRF9160, both 2026-07-23).
- `C:\ncs\`: NCS v2.9.0 to v3.2.3 only. No v3.4 workspace, no Zephyr 4.4 workspace.

## Gateway side

Our gateway board is the Murata Type 2FR (NXP RW612), Wi-Fi only.
- bluetooth-gateway v0.2.0: FRDM-RW612 Wi-Fi supported; Wi-Fi credentials by `settings set wifi/ssid`, `wifi/psk`; Golioth PSK by `settings set golioth/psk-id`, `golioth/psk`. Prebuilt hex is on the transfer drive.
- golioth/pouch v0.2.0 `examples/zephyr/gateway`: `frdm_rw612` + `boards/frdm_rw612_wifi.conf` (Ethernet off), Wi-Fi by `wifi cred add` in the shell, credentials over mcumgr to `/lfs1/credentials/`. Builds on the Zephyr v4.4.0 manifest. nRF9160 DK now runs the gateway on the nRF52840 with `ncs-serial-modem` on the nRF9160 (the reverse of bluetooth-gateway, where the 9160 runs the gateway and the 52840 is an HCI controller).
- Either way our board needs its own Zephyr board definition derived from `frdm_rw612` (pins, LCD on J5, LEDs, flash size of the 2FR module). Not written yet.

## Feather node side

Start from golioth/pouch v0.2.0 `examples/zephyr/ble_gatt`: BLE peripheral, Secure Connections enforced (passkey confirmation added in v0.2.0), MCUboot via sysbuild, credentials in LittleFS, Golioth settings + OTA, mcumgr over the UART console for provisioning.
- No nRF54L board ships with the example (only `frdm_rw612` and `nrf52_bsim`), so the feather is our own port. Use `pouch_xiao_nrf54l15` as the reference for nRF54L15 partitions, MCUboot and the RF switch.
- The feather has no UART (RTT and SWD only), so the example's provisioning path does not work as is. Options: mcumgr over BLE (SMP), an RTT shell, or credentials built into the image.
- Existing `firmware\boards\nrf54l15_feather\` and `apps\feather_node\` code (nPM1300, fuel gauge, SENS_ID, ANT_SEL hog) carries over. nPM1300 devicetree property names were checked against NCS v3.2.3 and need a recheck on the SDK we pick.
- X2 (32 kHz) is DNP, so set the LFCLK source to the internal RC before BLE.

## SDK choice follows from the pair

| Pair | Node SDK | Gateway SDK |
| --- | --- | --- |
| (a) mixed | NCS v3.4-branch (pouch v0.2.0) | NCS v3.0.1 per the tag, v3.1.1 as built on this PC |
| (b) all golioth/pouch v0.2.0 | NCS v3.4-branch | Zephyr v4.4.0 (RW612) |

Neither NCS v3.4 nor Zephyr 4.4 is installed on this PC. The `firmware\apps\feather_node\scripts\build.ps1` still names NCS v3.3.0.

## Open questions for Brian

1. Which pair ran on the solar board: node on golioth/pouch v0.2.0 (NCS v3.4) with the 9160 DK on bluetooth-gateway v0.2.0, or the 9160 DK on golioth/pouch v0.2.0 (gateway on nRF52840 + serial modem)?
2. Which solar board was it (ReefWatch `nrf54l15_v3`, v2 SPV1040, or another), and where is its app/board code? The transfer export has no local edits, so the board definition, prj.conf changes, provisioning steps and any fixes are still on the laptop.
3. Tag v0.2.0 exactly, or golioth/pouch main (v0.2.0 + 18) for the two fixes?
4. Feather provisioning: mcumgr over BLE (recommended), RTT shell, or built-in credentials?
5. Did the `0x2700, 8` cert error come back on v0.2.0, or is it fixed upstream?
