# pouch_gateway — Firmware Updates over Golioth, Observability with Memfault

How firmware gets onto the gateway and the Pouch sensor nodes after they ship, and where Memfault fits in.

*Written 2026-10-18 for rev A (Murata 2FR / RW612, Wi-Fi backhaul, 16 MB internal flash).*

> **Updated 2026-11-13 for Golioth Pouch v0.2.0.** The 2026-10-18 text assumed the older `golioth/bluetooth-gateway` app and the Golioth Firmware SDK. The gateway we build now is golioth/pouch `examples/zephyr/gateway` at **32ded9b** (v0.2.0 + 18), and it does **not** use the Golioth Firmware SDK at all. Gateway OTA, node OTA and the cloud link all run on Pouch's own `golioth_sdk` over Pouch's CoAP/DTLS transport. Each former **VERIFY** is now answered from the Pouch source (paths below are relative to the Pouch checkout, `C:\ncs\pouch-zephyr\pouch` for the gateway workspace and `C:\ncs\pouch-ncs\pouch` for the feather workspace; both are 32ded9b) or is still marked **VERIFY** if the source does not settle it. Nothing here has run on hardware: the gateway and the feather node were only built. The 2026-11-13 firmware work is in `firmware\apps\pouch_gateway\README.md` and `firmware\apps\feather_node\README.md`.
>
> Short answers:
> - Gateway OTA = Pouch `golioth_sdk` OTA (`CONFIG_GOLIOTH_OTA`) inside the gateway's own periodic Pouch sync over CoAP/DTLS to `coap.golioth.io:5684`. Not the Golioth Firmware SDK.
> - Node OTA = the same `golioth_sdk` OTA on the node (`examples/zephyr/ble_gatt/src/fw_update.c`), with the image blocks relayed by the gateway.
> - Upstream writes the image to the secondary slot with `flash_img` and requests a **permanent** MCUboot upgrade, so it never reverts and never confirms. This repo changes both firmwares to request a **test** upgrade and confirm only after a health check (see 3.1 and 4).
> - No Memfault code exists in Pouch 32ded9b. Memfault over Pouch is a possible route, not a supported one (5.2, 5.4).
> - pSRAM is not needed for OTA: the image is streamed to flash through a 512-byte buffer, so turning OTA on cost +720 B RAM and +2,140 B flash in the measured gateway build (3.1, 7).

---

## 1. The big picture

Two update paths:

```
                        Golioth cloud
              ┌────────────────────────────────┐
              │  Packages / Artifacts           │
              │  Cohorts → Deployments          │──── Pipelines ──►  Memfault
              └───────────┬─────────────────────┘      (/mflt stream)  (crashes, metrics,
                          │ Pouch over CoAP/DTLS, Wi-Fi                 reboot reasons)
                          ▼
                 ┌──────────────────┐
   (A) Gateway   │  pouch_gateway   │  RW612: app + MCUboot, A/B slots in internal flash
       OTA       │  (Golioth device)│
                 └────────┬─────────┘
                          │ BLE (Pouch, end-to-end encrypted —
                          │      gateway relays, can't read it)
                          ▼
   (B) Node OTA   ┌───────────────┐  ┌───────────────┐
                  │ pH sensor node │  │ other nodes …  │  each: app + MCUboot
                  └───────────────┘  └───────────────┘
```

- **(A) Gateway OTA:** the gateway is a Pouch device that syncs with Golioth over Wi-Fi. It receives its own new image as a Pouch downlink, in its own sync.
- **(B) Node OTA:** sensor nodes never touch the internet. When a node syncs over BLE, the cloud's downlink carries a manifest. The node asks for the image, receives it in blocks **through** the gateway, writes it to its own secondary slot, and reboots into it via MCUboot.

Golioth handles **delivery** (what version goes to which devices). Memfault handles **health** (did the new version crash, reboot, or misbehave).

---

## 2. Golioth OTA concepts

| Concept | What it is | For this product |
|---|---|---|
| **Package** | An upgradeable component on a device (firmware or an asset) | `gateway` for the gateway app; one package per node type (the feather node's default name is `ble_gatt_example`, `CONFIG_EXAMPLE_FW_UPDATE_COMPONENT`; pick e.g. `feather-node` or per sensor type before the first release) |
| **Artifact** | The binary for one version of a package | The signed MCUboot image, `zephyr.signed.bin` |
| **Deployment** | A bundle of artifacts sent together. Include *every* package a device needs, even the ones you're not changing | e.g. `gateway 1.2.0` |
| **Cohort** | A group of devices that receive the same deployment. One cohort per device, one active deployment per cohort | e.g. `gateways-dev`, `gateways-field`, `ph-nodes-dev`, `ph-nodes-field` |

Adding a device to a cohort, or starting a new deployment on a cohort, makes the cloud offer the new versions to those devices at their next sync (Pouch devices poll; there is no push notification in Pouch 32ded9b, see 3.3).

**Suggested cohort layout**

- `*-dev`: your bench boards. Every new build goes here first.
- `*-field`: units at your house or with customers. Promote a deployment here only after it has run cleanly in `dev` and Memfault looks quiet (§5).
- Keep gateways and nodes in **separate cohorts**. They're different packages and update on different schedules.

---

## 3. Gateway OTA, path (A)

### 3.1 What the v0.2.0 source does

This answers the old "VERIFY the Kconfig and API names" item.

| Question | Answer from the source |
|---|---|
| Which OTA implementation? | Pouch's own `golioth_sdk` (`golioth_sdk/Kconfig`, `golioth_sdk/ota.c`, `ota_upper.c`, `include/golioth/ota.h`). The Golioth Firmware SDK is not in the 32ded9b manifests (`west-zephyr.yml`, `west-ncs.yml`). |
| Kconfig | `CONFIG_GOLIOTH=y` and `CONFIG_GOLIOTH_OTA=y` (menu "Golioth OTA service"), plus `CONFIG_GOLIOTH_OTA_MAX_PACKAGE_NAME_LEN` (32) and `CONFIG_GOLIOTH_OTA_MAX_VERSION_LEN` (32). Flash side: `CONFIG_IMG_MANAGER=y`, `CONFIG_IMG_ERASE_PROGRESSIVELY=y`, `CONFIG_STREAM_FLASH=y`, and MCUboot through sysbuild (`SB_CONFIG_BOOTLOADER_MCUBOOT=y`). |
| API | `GOLIOTH_OTA_COMPONENT(name, package, version, receive_cb)` registers a package; `GOLIOTH_OTA_MANIFEST_HANDLER(cb)` gets the manifest; `golioth_ota_mark_for_download()`, `_mark_idle()`, `_mark_updating()` drive the state (`include/golioth/ota.h`). |
| Does the stock gateway example have OTA? | **No.** `examples/zephyr/gateway/prj.conf` has `CONFIG_GOLIOTH=y` and `CONFIG_GOLIOTH_SETTINGS=y` only, no `GOLIOTH_OTA`, no `fw_update.c`, no sysbuild MCUboot. This repo adds it. |
| Reference code | `examples/zephyr/coap_client/src/fw_update.c` (same CoAP transport as the gateway, MCUboot via `sysbuild.conf`). `examples/zephyr/ble_gatt/src/fw_update.c` is the same file for the node. |
| Package name | Whatever the app passes to `GOLIOTH_OTA_COMPONENT`. Examples read `CONFIG_EXAMPLE_FW_UPDATE_COMPONENT` (default `coap_client_example` / `ble_gatt_example`). The gateway here uses `gateway`. It must match the Golioth package name, and `ota.c` rejects names over `GOLIOTH_OTA_MAX_PACKAGE_NAME_LEN`. |
| Version source | `APP_VERSION_STRING` from `app_version.h`, i.e. the `VERSION` file in the app folder (`VERSION_MAJOR/MINOR/PATCHLEVEL/TWEAK`, `EXTRAVERSION`). Sysbuild feeds the same version to the MCUboot image header. The gateway example has no `VERSION` file (it logs `git describe`), so this repo adds one. Versions longer than 32 characters are rejected. |
| How the manifest and image arrive | In the periodic `pouch_coap_client_sync()` (`port/zephyr/transport/coap/client.c`, every `CONFIG_EXAMPLE_COAP_CLIENT_SYNC_PERIOD_S`, default 30 s in the gateway): the uplink carries the OTA status (`.u/c/<package>`: state, current version, target version; `ota.c` `ota_uplink`), the downlink carries the manifest (`/.u/desired`, a CBOR map with sequence number, hash, and per component package, version, SHA-256 hash, size) and, once the device marked a component `DOWNLOADING`, the component data (`/.u/c/<package>@<version>`). |
| Block size | CoAP Block1/Block2 with `CONFIG_POUCH_COAP_BLOCK_SIZE` (default 1024, 64 to 1024). The gateway `prj.conf` has `CONFIG_POUCH_BLOCK_SIZE=1024` and `CONFIG_POUCH_BLOCK_COUNT=12`. |
| Where the image is written | `flash_img_buffered_write()` into the secondary slot (`image-1`, `slot1_partition`) with the `flash_img` context (`CONFIG_IMG_BLOCK_BUF_SIZE`, default 512 B in `zephyr/subsys/dfu/Kconfig`). Nothing is buffered in RAM beyond that. |
| Integrity | The SHA-256 from the manifest is **passed to the app but not checked** by `golioth_sdk` (`ota_upper.c` copies it into `target_hash`; the examples only log it). The real gate is MCUboot verifying the image signature at the next boot. |
| Reboot/activate | `boot_request_upgrade(BOOT_UPGRADE_PERMANENT)`, a 3 s sleep to flush the log, `sys_reboot(SYS_REBOOT_WARM)` (upstream `fw_update.c`). |
| Who confirms? | **Nobody, upstream.** There is no `boot_write_img_confirmed()` anywhere in the Pouch tree (searched 32ded9b). With `BOOT_UPGRADE_PERMANENT` MCUboot treats the new image as final: it never reverts, even if the new image cannot connect. That is the opposite of the safety net this document wants. |

**What this repo does instead (gateway, 2026-11-13):** `firmware\apps\pouch_gateway\src\fw_update.c` requests `BOOT_UPGRADE_TEST` and the app calls `boot_write_img_confirmed()` only after the health check below. If the new image never confirms, MCUboot swaps the old one back at the next reset (watchdog, power cycle, or the 3 s reboot request loop).

**Health check for confirming (4. in the old list, now decided):**
1. Wi-Fi associated and an IPv4 address obtained (`wait_for_network()` in `main.c`),
2. Golioth reachable: the initial `pouch_gateway_cloud_ensure_ready()` succeeded **and** the first periodic `pouch_coap_client_sync()` returned 0 on this image (a full DTLS handshake plus a Pouch sync with Golioth),
3. the BLE gateway is running: `bt_enable()` succeeded and `pouch_gateway_scan_start()` was called.

Confirm once, then never again on that boot. Never confirm unconditionally at boot.

### 3.2 Release flow

```
bump VERSION → west build (sysbuild) → zephyr.signed.bin + zephyr.elf
      │                                   │                │
      │                                   │                └─► upload ELF to Memfault (symbols)
      │                                   └─► upload artifact to Golioth package "gateway" @ x.y.z
      └─► tag git vX.Y.Z
Golioth: create deployment {gateway x.y.z} → assign to cohort gateways-dev
   ...soak, watch Memfault... → assign same deployment to gateways-field
```

The artifact is **`zephyr.signed.bin`** from the gateway build's `pouch_gateway` image folder (not the merged hex and not `zephyr.bin`), signed by sysbuild. Upload it through the Golioth console or `goliothctl dfu` (see Golioth's `goliothctl dfu` reference). The exact build output paths and the J-Link commands for the first (wired) flash are in `firmware\apps\pouch_gateway\README.md`. Version rule: the new `VERSION` must differ from the running one (the manifest handler only downloads when `current != target`, so a *downgrade* also installs, but MCUboot's default swap mode does not block it either; set `CONFIG_MCUBOOT_DOWNGRADE_PREVENTION` in MCUboot later if wanted).

### 3.3 What happens on the device

1. The gateway syncs every 30 s. The cloud puts the manifest in the downlink. It does not push a notification; a newly assigned deployment is noticed at the next sync.
2. `ota_manifest_receive()` compares current and target versions; if they differ (and the running image is already confirmed) it marks the component `DOWNLOADING`.
3. The next sync's uplink reports `DOWNLOADING`, and the cloud streams the image as a downlink. Each block goes to `ota_fw_receive()`, which writes it to `image-1` through `flash_img`.
4. On the last block the app requests a **test** upgrade and reboots.
5. MCUboot verifies the signature and swaps.
6. The app runs the health check above and **confirms**. Otherwise MCUboot rolls back on the next reset.
7. The new version appears in the next uplink status (`.u/c/gateway`, state IDLE, `v` = new version), and Golioth shows it per device.

**Side effects to know about (read from the code, not yet observed):** the CoAP transport serialises all socket use with `pouch_coap_mutex` (`client.c`, comment at the top). The whole image download happens inside `pouch_coap_client_sync()` with that mutex held, so BLE nodes that want to upload during the download wait. Expect a gateway update to take on the order of minutes for a 1.2 MB image at 1 KB per CoAP round trip (a guess, not measured), during which the gateway forwards nothing. The 10 s `POUCH_COAP_REQUEST_TIMEOUT_S` and 3 retries apply per block.

**Display tie-in:** the 2" LCD can show `Updating gateway 1.2.0 … 43%` during download and the running version on the status screen. The display code is not written yet (J5 panel is a disabled devicetree node).

---

## 4. Sensor node OTA through the gateway, path (B)

From the Pouch v0.2.0 source (`examples/zephyr/ble_gatt`, `src/gateway/`, `port/zephyr/transport/coap/gateway.c`):

1. A node advertises with the "sync request" flag. The gateway scans, connects, sets BLE security and starts the Pouch GATT session (`pouch_gateway_bt_start()`).
2. The node uploads its pouch (data, plus its OTA status `.u/c/<package>`). The gateway forwards it to Golioth over its CoAP/DTLS link. The cloud's reply (the downlink) is queued in the gateway (`CONFIG_POUCH_GATEWAY_NUM_BLOCKS`, default 10 blocks, from the `pouch_buf` pool of `CONFIG_POUCH_BLOCK_COUNT` x `CONFIG_POUCH_BLOCK_SIZE`; `POUCH_GATEWAY_DOWNLINK_BLOCK_TIMEOUT` 10 s per block) and relayed to the node over the Pouch SAR layer (GATT window `CONFIG_POUCH_GATT_WINDOW_SIZE`, default 3).
3. On the node, `ota_manifest_receive()` compares versions and marks the component `DOWNLOADING`. At its **next** sync the node reports that state and the cloud streams the image as downlink blocks. `ota_fw_receive()` writes each block to the node's `image-1` slot with `flash_img` (512 B write buffer).
4. Block size: the cloud side uses 1 KB CoAP blocks (`POUCH_COAP_BLOCK_SIZE`); the BLE side re-segments them into ATT packets (the feather uses `BT_L2CAP_TX_MTU=247`, so about 244 bytes per notification, pipelined by the SAR window). Node `CONFIG_POUCH_BLOCK_SIZE` is the default 512.
5. Upstream then requests a **permanent** MCUboot upgrade and reboots. The node never confirms. This repo's feather node requests a **test** upgrade and confirms after one Pouch sync on the new image has reached the cloud (see below).
6. The traffic is **end-to-end encrypted between node and cloud** (SAEAD session with the cloud; the gateway only sees ciphertext blocks). The gateway can't read or alter the image: a modified block fails authentication, and MCUboot rejects an image with a bad signature.

Implications for the design:

- **Each node needs MCUboot and its own confirm logic.** Upstream has none; the feather node now confirms after one successful Pouch sync on the new image (only when the image is in test mode).
- **What "successful sync" means in v0.2.0:** the transport knows whether a session succeeded (`end(bearer, success)` in `src/transport/endpoints/device/uplink.c` and `downlink.c`), but 32ded9b discards that flag and `POUCH_EVENT_SESSION_END` (`include/pouch/events.h`) fires on both success and failure. The feather therefore confirms when a session ended **and** a downlink was authenticated and decoded in it (the OTA manifest handler ran). That proves node to gateway to cloud and back on the new image. It depends on the cloud sending a manifest each session (**VERIFY** on the bench; if the cloud only sends a manifest when there is a deployment, a node outside any deployment never confirms its first image).
- **The gateway firmware doesn't change to support node OTA.** It just has to stay connected long enough and have the pool blocks for the downlink. A node update takes many BLE round trips, so a node with a weak link to the gateway updates slowly or retries (`golioth_sdk` has no resume code: `ota_receive_component_start()` resets the offset to 0 for every component downlink, so assume an interrupted download starts over).
- **Battery:** a full image over BLE costs a noticeable amount of energy on a small-battery node. Roll node updates out deliberately, not on every commit.
- **Gateway caching:** no. The gateway has no image cache; each node pulls its own copy end to end (`src/gateway/downlink.c` only queues blocks for the one active session). This closes the old VERIFY.
- **LCD tie-in:** the gateway sees the BLE connection but not the payload. So it can show "node X connected / syncing" and connection duration, but not "node X is at 63% of its update." Version info for nodes has to come from the cloud side.

---

## 5. Where Memfault fits

Golioth answers **"what version is each device running?"** Memfault answers **"is that version healthy?"**

### 5.1 What Memfault gives you

- **Crash and fault capture (coredumps):** on a hard fault, assert (`CONFIG_ASSERT=y`), watchdog, or stack overflow, the Memfault SDK saves a compact coredump to RAM/flash. It uploads it on the next connection. Memfault decodes it into a symbolicated backtrace with registers and locals, and groups identical crashes into **Issues** with a count of affected devices and versions.
- **Reboot reasons:** every reset is tagged (power-on, watchdog, fault, software reset, OTA reboot …). A rising unexpected-reboot rate after a deployment is the clearest "roll this back" signal.
- **Metrics / heartbeats:** periodic summaries such as uptime, heap usage, Wi-Fi RSSI, reconnect counts, Golioth connection drops, BLE connections per hour, number of Pouch nodes seen, and display task stack high-water mark. They're charted per device and per software version.
- **Device timeline and logs:** events, reboots and log snippets around a crash on one device.
- **Filtering by version:** "crash-free devices on 1.2.0 vs 1.1.3" is the comparison that gates promoting a deployment from `dev` to `field`.

### 5.2 How the data gets there (no direct Memfault connection needed)

The gateway doesn't talk to Memfault directly. The Golioth side is documented: the Memfault pipeline destination takes `application/octet-stream` chunks, "sent to Memfault unmodified", with the Golioth device ID as the Memfault serial number unless an `alternate_id` is set (https://docs.golioth.io/data-routing/destinations/memfault, `v1.0.0`; the page does not say anything about Pouch or SDK versions).

1. The Memfault Firmware SDK produces opaque **chunks** (coredumps, heartbeats, events) via its packetizer.
2. **With the Golioth Firmware SDK** (older bluetooth-gateway line, v0.14.0 or later) the app streams chunks to the `/mflt` path with the blockwise stream upload. **Pouch 32ded9b has no equivalent code**: there is no Memfault, `mflt`, or Memfault-style stream helper anywhere in the tree (searched the whole checkout). The Pouch way to do the same is `pouch_uplink_entry_write(".s/mflt", POUCH_CONTENT_TYPE_OCTET_STREAM, chunk, len, timeout)` (or `pouch_stream_open` for a long stream). That is the same call the examples use for `.s/sensor`. Whether Golioth maps a Pouch `.s/<name>` entry to a pipeline path `/<name>` with `application/octet-stream` so that a `path: /mflt` filter matches is **VERIFY** (cloud side; the Pouch source only shows the `.s/` prefix and the example `.s/sensor` "routed into LightDB Stream" in `examples/esp_idf/http_client/pytest/README.md`). Test it with one dummy chunk before writing any Memfault integration.
3. A Golioth **Pipeline** filters on the path and sends to the `memfault` destination, with your Memfault project key stored as a Golioth secret (`MEMFAULT_PROJECT_KEY`).
4. Memfault decodes the chunks using the **ELF symbol file you uploaded for that exact build**. No symbols means crashes show as "Symbols Missing," so the ELF upload belongs in the release flow (§3.2).

Device-side bits: `CONFIG_MEMFAULT=y`, implement `memfault_platform_get_device_info()`, and **don't** enable Memfault's own HTTP uploader, because Golioth is the transport. One Wi-Fi connection, one DTLS session, one set of credentials. Memfault's Firmware SDK is not in the gateway workspace (`west-zephyr.yml`, plain Zephyr, no module for it). The feather's NCS workspace has it as a module (`nrf/west.yml`, `modules/lib/memfault-firmware-sdk`) but the Pouch manifest does not enable it for the build. Adding it is a separate decision.

### 5.3 Rules that keep Golioth and Memfault in sync

- **One version string everywhere:** the `VERSION` file drives `APP_VERSION_STRING` (the Golioth package version in `GOLIOTH_OTA_COMPONENT`), the MCUboot image header (sysbuild), and Memfault's `software_version`. If they drift, you can't line up a crash with the deployment that caused it. In this repo the gateway's `VERSION` is the single source; `git describe` is only logged at boot.
- **`software_type`:** `gateway` for this board, and the node package name for nodes. It matches the Golioth package names.
- **`device_serial`:** use the Golioth device ID, so a device is the same thing in both dashboards.
- **`hardware_version`:** `gw-revA`, later `gw-rev2`. That way, when rev 2 drops J2/J4, you can still tell the boards apart in crash data.
- **Use Golioth for OTA, not Memfault.** Memfault *can* also do OTA (`CONFIG_MEMFAULT_ZEPHYR_FOTA` with an MCUboot backend), but running two OTA systems on one device invites conflicting updates. Leave Memfault FOTA **disabled** and use Memfault only for observability.

### 5.4 Sensor nodes and Memfault

Nodes have no IP connection, so they'd send Memfault chunks as Pouch uplink entries (the same `.s/mflt` route as above) that travel through the gateway and Golioth and are routed by a Pipeline. v0.2.0 gives the transport for this (any entry path, `POUCH_CONTENT_TYPE_OCTET_STREAM`, end-to-end encrypted, forwarded by the gateway like any other pouch), but nothing Memfault-specific, and the overhead on battery is not measured. **Still VERIFY:** cloud routing of the path (5.2 item 2) and the energy cost. If it does not work out, nodes can at least report reboot reason and version as ordinary Pouch telemetry on `.s/sensor` (the feather already sends `vbat_mv`, `soc_pct` and the SENS_ID there; the running version is reported by the OTA status entry `.u/c/<package>`).

---

## 6. Promotion checklist (per release)

- [ ] `VERSION` bumped; MCUboot header, Golioth package version and Memfault `software_version` all match
- [ ] Signed with the production MCUboot key (not the dev key; the repo builds use the MCUboot debug key until a production key is chosen)
- [ ] ELF uploaded to Memfault **before** devices start reporting
- [ ] Artifact (`zephyr.signed.bin`) uploaded to the Golioth package; deployment created with **all** required packages
- [ ] Deployed to the `dev` cohort; at least one bench device updated, confirmed, and reconnected
- [ ] Rollback tested at least once per major change: a build that deliberately doesn't confirm should revert
- [ ] Soak: no new Memfault Issues, and no rise in unexpected reboots, on the new version
- [ ] Promote the same deployment to `field`
- [ ] Watch Memfault for the first day after promoting to `field`

---

## 7. Open items

1. ~~VERIFY the Golioth Firmware SDK Kconfig and API names~~ Answered: Pouch `golioth_sdk` OTA, `CONFIG_GOLIOTH_OTA`, `GOLIOTH_OTA_COMPONENT` (3.1). Still to check on hardware: that Golioth accepts the package name and that the whole flow runs.
2. Partition layout: **decided and built** for rev A: the existing `image-0` / `image-1` layout, 3 MB slots, 128 KB MCUboot partition, Zephyr 4.4.0's default mode swap using offset (no scratch partition). No layout change was needed; details in `firmware\apps\pouch_gateway\README.md`. The gateway app is 1.2 MB of the 3 MB slot (40 %). The feather node uses NCS's swap using move.
3. **pSRAM:** not needed. Today's gateway build uses none (the FRDM-RW612 8 MB APS6404L is disabled in its devicetree and removed from our board), RAM is 569,804 B of 960 KB (58 %). OTA download needs no extra buffer: `flash_img` plus `stream_flash` use one 512-byte write buffer, and the CoAP block buffers (2 x 1072 B) and the `pouch_buf` pool already exist. Measured (pristine builds 2026-11-13): turning on `GOLIOTH_OTA` + `IMG_MANAGER` + the update code cost **+720 B RAM (569,804 to 570,524 B, 58.04 %) and +2,140 B flash**; MCUboot itself is 59,804 B flash and 55,544 B RAM while it runs (not resident alongside the app). The remaining pSRAM question (does the gateway run without it) is unproven on hardware but not an OTA issue.
4. "Healthy" for confirming the gateway image: **decided** (3.1). Review whether the first sync (up to 30 s after boot) is the right gate, and whether to add a watchdog so a hung image resets instead of waiting for a power cycle.
5. **VERIFY** the cloud side of Memfault over Pouch: `.s/mflt` mapping to the `/mflt` pipeline path, and per-chunk energy on a node (5.2, 5.4).
6. **VERIFY** that the cloud sends the OTA manifest on every session for a device inside a deployment (the feather node's confirm logic relies on it, 4).
7. Production MCUboot signing key (both firmwares build with the MCUboot debug key now).
8. The upstream `golioth_sdk` does not verify the manifest SHA-256 in the device. Decide whether to add a check (hash the stream in `ota_fw_receive`) on top of MCUboot's signature check.

## Sources

- Pouch source at 32ded9b: `golioth_sdk/Kconfig`, `golioth_sdk/ota.c`, `golioth_sdk/ota_upper.c`, `golioth_sdk/include/golioth/ota.h`, `examples/zephyr/coap_client/src/fw_update.c`, `examples/zephyr/ble_gatt/src/fw_update.c`, `examples/zephyr/gateway/prj.conf`, `port/zephyr/transport/coap/client.c`, `src/gateway/`, `include/pouch/events.h`, `CHANGELOG.md` (v0.2.0)
- Golioth: Over-the-Air Updates (packages, artifacts, deployments, cohorts): https://docs.golioth.io/device-management/ota
- Golioth: Memfault data destination: https://docs.golioth.io/data-routing/destinations/memfault
- Golioth blog: Visualizing Bluetooth OTA Firmware Updates: https://blog.golioth.io/visualizing-bluetooth-ota-firmware-updates/
- Golioth blog: New Pipelines Data Destination: Memfault: https://blog.golioth.io/new-pipelines-data-destination-memfault/
- Memfault: Zephyr Integration Guide: https://docs.memfault.com/docs/mcu/zephyr-guide
- Zephyr: Over-the-Air Update (MCUboot): https://docs.zephyrproject.org/latest/services/device_mgmt/ota.html
