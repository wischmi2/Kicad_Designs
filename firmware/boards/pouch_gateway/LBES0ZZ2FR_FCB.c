/*
 * FlexSPI flash configuration block for the 16 MB flash inside the Murata
 * Type 2FR module (LBES0ZZ2FR, NXP RW612).
 *
 * Source: bytes 0x400..0x603 of Murata's prebuilt image
 *   https://github.com/murata-wireless/2FR  (BSD-3-Clause)
 *   internal_flash_binaries/rdrw610_wifi_cli_intFlash_singleAnt.bin
 * which is the working Type 2FR EVK image. The Zephyr FRDM-RW612 FCB
 * (W25Q512JVFIQ_FCB.c, 64 MB, 32-bit addresses) must not be used on this
 * module (Murata's Zephyr EVK guide says the same, section 7.1.1).
 *
 * Differences from the FRDM FCB: 24-bit addresses, A1 size 16 MB, 6 dummy
 * cycles, 1-1-1 page program, serialClkFreq 7, deviceModeArg 0x200 (FRDM:
 * 0x02, its low byte is what the 0x31 sequence writes), block size 0x8000
 * (0x52 erase), no 64 KB block erase. The LUT is kept as the raw
 * words from the image so it matches Murata's byte for byte; the decoded
 * sequences are listed beside each word. The build was checked by comparing
 * bytes 0x400..0x603 of zephyr.bin with the Murata image (README.md).
 *
 * Copyright (c) Murata Manufacturing Co., Ltd. (data), 2026 (this file)
 * SPDX-License-Identifier: BSD-3-Clause
 */

#include <flash_config.h>

__attribute__((section(".flash_conf"), used)) const fc_flexspi_nor_config_t
flexspi_config = {
	.memConfig = {
		.tag = FC_BLOCK_TAG,
		.version = FC_BLOCK_VERSION,
		.readSampleClkSrc = 1,
		.csHoldTime = 3,
		.csSetupTime = 3,
		.deviceModeCfgEnable = 1,
		.deviceModeSeq = {.seqNum = 1, .seqId = 2},
		.deviceModeArg = 0x200,
		.configCmdEnable = 0,
		.deviceType = 0x1,
		.sflashPadType = kSerialFlash_4Pads,
		.serialClkFreq = 7,
		.sflashA1Size = 0x1000000U,
		.sflashA2Size = 0,
		.sflashB1Size = 0,
		.sflashB2Size = 0,
		.lookupTable = {
			/* seq 0, read: CMD 0xEB (1 pad), RADDR 24 bit (4 pads),
			 * DUMMY 6 cycles (4 pads), READ 4 bytes (4 pads) */
			[0] = 0x0a1804ebU,
			[1] = 0x26043206U,
			[2] = 0U,
			/* seq 1, read status: CMD 0x05, READ 1 byte */
			[4] = 0x24040405U,
			/* seq 2, write status 2 (QE): CMD 0x31, WRITE 1 byte */
			[8] = 0x20010431U,
			/* seq 3, write enable: CMD 0x06 */
			[12] = 0x00000406U,
			/* seq 5, sector erase 4 KB: CMD 0x20, RADDR 24 bit */
			[20] = 0x08180420U,
			/* seq 8, block erase 32 KB: CMD 0x52, RADDR 24 bit */
			[32] = 0x08180452U,
			/* seq 9, page program: CMD 0x02, RADDR 24 bit, WRITE (all 1 pad) */
			[36] = 0x08180402U,
			[37] = 0x00002000U,
			/* seq 11, chip erase: CMD 0x60 */
			[44] = 0x00000460U,
		},
	},
	.pageSize = 0x100,
	.sectorSize = 0x1000,
	.ipcmdSerialClkFreq = 0,
	.blockSize = 0x8000,
	.fcb_fill[0] = 0xFFFFFFFF,
};
