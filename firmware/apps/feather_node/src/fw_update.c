/*
 * Copyright (c) 2025 Golioth
 *
 * SPDX-License-Identifier: Apache-2.0
 *
 * Based on golioth/pouch examples/zephyr/ble_gatt/src/fw_update.c at 32ded9b. Changes:
 *  - the upgrade is requested in TEST mode (BOOT_UPGRADE_TEST), not PERMANENT. Upstream never
 *    confirms anything, and a permanent upgrade can never be reverted, even if the new image
 *    cannot reach the cloud any more;
 *  - the new image confirms itself (boot_write_img_confirmed) after one Pouch sync in which the
 *    cloud answered: a downlink was authenticated and decoded (the OTA manifest arrived) and the
 *    session then ended. If that never happens MCUboot reverts at the next reset;
 *  - no new download is started while the running image is still unconfirmed.
 */

#include <zephyr/logging/log.h>
LOG_MODULE_REGISTER(fw_update);

#include <zephyr/kernel.h>
#include <zephyr/dfu/flash_img.h>
#include <zephyr/dfu/mcuboot.h>
#include <zephyr/logging/log_ctrl.h>
#include <zephyr/storage/flash_map.h>
#include <zephyr/sys/reboot.h>

#include <golioth/ota.h>
#include <pouch/events.h>

#include <app_version.h>

static struct flash_img_context flash_context;

/* Set when the cloud answered in this boot (OTA manifest received and decoded). */
static atomic_t cloud_answered;

static void confirm_work_fn(struct k_work *work)
{
    ARG_UNUSED(work);

    if (boot_is_img_confirmed())
    {
        return;
    }

    int err = boot_write_img_confirmed();

    if (err)
    {
        LOG_ERR("Failed to confirm the running image: %d", err);
        return;
    }

    LOG_INF("Image confirmed (version " APP_VERSION_STRING ")");
}

static K_WORK_DEFINE(confirm_work, confirm_work_fn);

/* POUCH_EVENT_SESSION_END fires for failed sessions too (32ded9b drops the transport's success
 * flag), so it only counts together with cloud_answered. Confirm from the system work queue,
 * not from the Pouch thread.
 */
static void pouch_event(enum pouch_event event, void *ctx)
{
    ARG_UNUSED(ctx);

    if (event == POUCH_EVENT_SESSION_END && atomic_get(&cloud_answered)
        && !boot_is_img_confirmed())
    {
        k_work_submit(&confirm_work);
    }
}

POUCH_EVENT_HANDLER(pouch_event, NULL);

static void ota_fw_receive(const void *data, size_t offset, size_t len, bool is_last)
{
    LOG_DBG("Received %d bytes at offset %d", len, offset);

    int err = 0;

    if (0 == offset)
    {
        err = flash_img_init(&flash_context);
        if (err)
        {
            LOG_ERR("Failed to init flash write");
            return;
        }
    }

    err = flash_img_buffered_write(&flash_context, data, len, is_last);
    if (err)
    {
        LOG_ERR("Failed to write to flash: %d", err);
        return;
    }

    if (is_last)
    {
        /* Test mode: MCUboot boots the new image once and reverts at the next reset unless the
         * new image confirms itself (see pouch_event above).
         */
        err = boot_request_upgrade(BOOT_UPGRADE_TEST);
        if (err)
        {
            LOG_ERR("Failed to request upgrade");
            return;
        }

        LOG_INF("Rebooting to apply upgrade");

#if IS_ENABLED(CONFIG_LOG)
        while (log_process())
        {
        }
#endif

        k_sleep(K_SECONDS(3));

        sys_reboot(SYS_REBOOT_WARM);
    }
}

static void ota_manifest_receive(const struct golioth_ota_manifest_component *components,
                                 size_t num_components)
{
    atomic_set(&cloud_answered, 1);

    for (int i = 0; i < num_components; i++)
    {
        LOG_DBG("Target: %s@%s, %d bytes",
                components[i].name,
                components[i].target,
                components[i].size);
        LOG_HEXDUMP_DBG(components[i].target_hash,
                        GOLIOTH_OTA_COMPONENT_HASH_BIN_LEN,
                        "Target hash:");
        if (0 != strcmp(components[i].current, components[i].target))
        {
            if (!boot_is_img_confirmed())
            {
                /* A new upgrade request on top of an unconfirmed image would make MCUboot
                 * revert the running image first. Confirm (end of this session), then update.
                 */
                LOG_WRN("Update to %s postponed: running image not confirmed yet",
                        components[i].target);
                continue;
            }
            golioth_ota_mark_for_download(components[i].name);
        }
    }
}

GOLIOTH_OTA_COMPONENT(fw, CONFIG_EXAMPLE_FW_UPDATE_COMPONENT, APP_VERSION_STRING, ota_fw_receive);
GOLIOTH_OTA_MANIFEST_HANDLER(ota_manifest_receive);
