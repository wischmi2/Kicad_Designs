/*
 * Copyright (c) 2026 Golioth, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 *
 * Based on golioth/pouch examples/zephyr/coap_client/src/fw_update.c at 32ded9b. Changes:
 *  - the upgrade is requested in TEST mode (BOOT_UPGRADE_TEST), not PERMANENT, so MCUboot
 *    reverts to the old image on the next reset unless the new one confirms itself;
 *  - fw_update_confirm_healthy() confirms the image, and main.c only calls it after the health
 *    check (Wi-Fi up, Golioth sync ok, BLE scanning);
 *  - no download is started while the running image is still unconfirmed.
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

#include <app_version.h>

#include "fw_update.h"

static struct flash_img_context flash_context;

void fw_update_confirm_healthy(void)
{
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
         * new image calls boot_write_img_confirmed().
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
                 * revert the running image first. Wait for the health check.
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
