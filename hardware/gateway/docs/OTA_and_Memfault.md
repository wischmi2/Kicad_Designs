# pouch_gateway — Firmware Updates over Golioth, Observability with Memfault

How firmware gets onto the gateway and the Pouch sensor nodes after they ship, and where Memfault fits in.

*Written 2026-10-18 for rev A (Murata 2FR / RW612, Wi-Fi backhaul, 16 MB internal flash). Things marked **VERIFY** came from docs I couldn't fully confirm, or are assumptions — check them against the current Golioth and Memfault docs before relying on them.*

---

## 1. The big picture

Two update paths:

```
                        Golioth cloud
              ┌────────────────────────────────┐
              │  Packages / Artifacts           │
              │  Cohorts → Deployments          │──── Pipelines ──►  Memfault
              └───────────┬─────────────────────┘      (/mflt stream)  (crashes, metrics,
                          │ CoAP/DTLS over Wi-Fi                        reboot reasons)
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

- **(A) Gateway OTA:** the gateway is a normal Golioth device on Wi-Fi. It downloads its own new image directly from Golioth.
- **(B) Node OTA:** sensor nodes never touch the internet. When a node checks in over BLE, the cloud's downlink tells it a new version is available. The node pulls the image in blocks **through** the gateway, writes it to its own secondary slot, and reboots into it via MCUboot.

Golioth handles **delivery** (what version goes to which devices). Memfault handles **health** (did the new version crash, reboot, or misbehave).

---

## 2. Golioth OTA concepts

| Concept | What it is | For this product |
|---|---|---|
| **Package** | An upgradeable component on a device (firmware or an asset) | `gateway` for the gateway app; one package per node type, e.g. `ph-node` |
| **Artifact** | The binary for one version of a package | The signed MCUboot image, e.g. `zephyr.signed.bin` |
| **Deployment** | A bundle of artifacts sent together. Include *every* package a device needs, even the ones you're not changing | e.g. `gateway 1.2.0` |
| **Cohort** | A group of devices that receive the same deployment. One cohort per device, one active deployment per cohort | e.g. `gateways-dev`, `gateways-field`, `ph-nodes-dev`, `ph-nodes-field` |

Adding a device to a cohort, or starting a new deployment on a cohort, notifies the devices so they upgrade to that deployment's versions.

**Suggested cohort layout**

- `*-dev`: your bench boards. Every new build goes here first.
- `*-field`: units at your house or with customers. Promote a deployment here only after it has run cleanly in `dev` and Memfault looks quiet (§5).
- Keep gateways and nodes in **separate cohorts**. They're different packages and update on different schedules.

---

## 3. Gateway OTA, path (A)

### 3.1 One-time setup

1. **MCUboot via sysbuild:** `SB_CONFIG_BOOTLOADER_MCUBOOT=y` in `sysbuild.conf`.
2. **Flash partitions:** boot / slot0 / slot1 / scratch (or swap-using-move) / storage. The RW612's 16 MB internal flash is ample. A ~1–1.5 MB app fits comfortably with two slots plus a settings/storage partition. Start from the `frdm_rw612` partition layout.
3. **Golioth Firmware SDK FW-update support:** enable the SDK's firmware-update module and register the `gateway` package with its current version at startup. **VERIFY** the exact Kconfig symbol and API names against the Golioth Firmware SDK "Firmware Upgrade" guide for the SDK version you pin.
4. **Image confirmation:** after an update the new image boots in *test* mode. The app must confirm it (`boot_write_img_confirmed()`, or let the Golioth SDK do it) only after it has proven healthy, e.g.:
   - Wi-Fi associated **and**
   - Golioth connected **and**
   - the BLE gateway service is running.
   
   If it never confirms (crash loop, can't connect), MCUboot swaps back to the old image on the next reset. **This is your safety net.** Don't confirm unconditionally at boot.
5. **Signing key:** generate your own MCUboot key. Don't ship the default dev key. Keep it out of git.

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

Upload through the Golioth console or `goliothctl dfu` (see Golioth's `goliothctl dfu` reference). This scripts cleanly into GitHub Actions later.

### 3.3 What happens on the device

1. The device gets a "new deployment" notification (or sees it on reconnect).
2. It compares its running version with the target. If they differ, it downloads the artifact in blocks into **slot1**.
3. It marks slot1 for test boot and reboots.
4. MCUboot verifies the signature and swaps.
5. The app runs its health checks and **confirms**. Otherwise MCUboot rolls back on the next reset.
6. The device reports its new version and state to Golioth, which shows the update status per device in the console.

**Display tie-in:** the 2" LCD can show `Updating gateway 1.2.0 … 43%` during download and the running version on the status screen. That's handy when you're standing in front of it.

---

## 4. Sensor node OTA through the gateway, path (B)

Per Golioth's Bluetooth OTA write-up:

1. A node advertises that it has data to send. The gateway connects and relays.
2. The node uploads its data first. The cloud's downlink can then include "new firmware available" for that node's cohort.
3. The node compares its current and target versions. If they differ, it requests the image, receives it **in ~1 KB blocks relayed by the gateway**, writes it to its secondary slot, asks MCUboot to upgrade, and reboots.
4. The traffic is **end-to-end encrypted between node and cloud**. The gateway is a dumb pipe and can't read or tamper with the image. Keys live only in the cloud and on the node.

Implications for the design:

- **Each node needs MCUboot and its own confirm logic.** Confirm after it has successfully completed one Pouch sync on the new image.
- **The gateway firmware doesn't change to support node OTA.** It just has to stay connected long enough. A node update takes many BLE round trips, so a node with a weak link to the gateway updates slowly or retries.
- **Battery:** a full image over BLE costs a noticeable amount of energy on a coin-cell or small-battery node. Roll node updates out deliberately, not on every commit.
- **Gateway caching:** **VERIFY.** The Golioth article doesn't say whether the gateway caches images. Assume each node pulls its own copy end-to-end through the gateway.
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

The gateway doesn't talk to Memfault directly. It sends Memfault chunks to Golioth, and **Golioth Pipelines** forwards them:

1. The Memfault Firmware SDK produces opaque **chunks** (coredumps, heartbeats, events) via its packetizer.
2. The app streams them to Golioth on the **`/mflt`** path as `application/octet-stream`, using the Golioth SDK's blockwise stream upload. This needs Golioth Firmware SDK v0.14.0 or later.
3. A Golioth **Pipeline** filters on `path: /mflt` and sends to the `memfault` destination, with your Memfault project key stored as a Golioth secret (`MEMFAULT_PROJECT_KEY`).
4. Memfault decodes the chunks using the **ELF symbol file you uploaded for that exact build**. No symbols means crashes show as "Symbols Missing," so the ELF upload belongs in the release flow (§3.2).

Device-side bits: `CONFIG_MEMFAULT=y`, implement `memfault_platform_get_device_info()`, and **don't** enable Memfault's own HTTP uploader, because Golioth is the transport. One Wi-Fi connection, one TLS session, one set of credentials.

### 5.3 Rules that keep Golioth and Memfault in sync

- **One version string everywhere:** the `VERSION` file drives the MCUboot image header, the Golioth package version, and Memfault's `software_version`. If they drift, you can't line up a crash with the deployment that caused it.
- **`software_type`:** `gateway` for this board, `ph-node` for the pH node, and so on. It matches the Golioth package names.
- **`device_serial`:** use the Golioth device ID, so a device is the same thing in both dashboards.
- **`hardware_version`:** `gw-revA`, later `gw-rev2`. That way, when rev 2 drops J2/J4, you can still tell the boards apart in crash data.
- **Use Golioth for OTA, not Memfault.** Memfault *can* also do OTA (`CONFIG_MEMFAULT_ZEPHYR_FOTA` with an MCUboot backend), but running two OTA systems on one device invites conflicting updates. Leave Memfault FOTA **disabled** and use Memfault only for observability.

### 5.4 Sensor nodes and Memfault

Nodes have no IP connection, so they'd have to send Memfault chunks as Pouch uplink data and have a Pipeline route them to Memfault the same way. **VERIFY** that the Pouch uplink and Pipelines support this path and that the overhead is acceptable on battery. If not, nodes can at least report reboot reason and version as ordinary Pouch telemetry.

---

## 6. Promotion checklist (per release)

- [ ] `VERSION` bumped; MCUboot header, Golioth package version and Memfault `software_version` all match
- [ ] Signed with the production MCUboot key (not the dev key)
- [ ] ELF uploaded to Memfault **before** devices start reporting
- [ ] Artifact uploaded to the Golioth package; deployment created with **all** required packages
- [ ] Deployed to the `dev` cohort; at least one bench device updated, confirmed, and reconnected
- [ ] Rollback tested at least once per major change: a build that deliberately doesn't confirm should revert
- [ ] Soak: no new Memfault Issues, and no rise in unexpected reboots, on the new version
- [ ] Promote the same deployment to `field`
- [ ] Watch Memfault for the first day after promoting to `field`

---

## 7. Open items

1. **VERIFY** the exact Golioth Firmware SDK Kconfig and API names for firmware update on the SDK version you pin.
2. Decide the partition layout (swap-using-move vs. scratch) and app size budget once the display + LVGL + BLE gateway build size is known.
3. Confirm the Golioth bluetooth-gateway runs without the 8 MB pSRAM the FRDM-RW612 has (already in DESIGN_NOTES open items). Image download buffers count against RAM.
4. Decide what "healthy" means for confirming the gateway image (§3.1 step 4).
5. **VERIFY** whether the Memfault-over-Pouch path for nodes is supported (§5.4).

## Sources

- Golioth: Over-the-Air Updates (packages, artifacts, deployments, cohorts): https://docs.golioth.io/device-management/ota
- Golioth blog: Visualizing Bluetooth OTA Firmware Updates: https://blog.golioth.io/visualizing-bluetooth-ota-firmware-updates/
- Golioth blog: New Pipelines Data Destination: Memfault: https://blog.golioth.io/new-pipelines-data-destination-memfault/
- Memfault: Zephyr Integration Guide: https://docs.memfault.com/docs/mcu/zephyr-guide
- Zephyr: Over-the-Air Update (MCUboot): https://docs.zephyrproject.org/latest/services/device_mgmt/ota.html
