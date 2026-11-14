/*
 * Gateway firmware update (Golioth OTA through Pouch's golioth_sdk) and MCUboot image confirm.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#pragma once

/**
 * Confirm the running MCUboot image if it is still in test mode (first boot after an OTA).
 *
 * Call this only after the gateway has proven itself healthy. Does nothing if the image is
 * already confirmed (normal boots, and images flashed directly).
 */
void fw_update_confirm_healthy(void);
