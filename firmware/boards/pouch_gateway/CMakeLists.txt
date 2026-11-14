# SPDX-License-Identifier: Apache-2.0

zephyr_library()
zephyr_library_sources(init.c)

if(CONFIG_NXP_RW6XX_BOOT_HEADER)
  # FCB for the 16 MB flash inside the Murata Type 2FR module. The FRDM-RW612
  # one (64 MB W25Q512JV) does not work on this module.
  zephyr_library_sources(LBES0ZZ2FR_FCB.c)
endif()

# Set TX power limit file to override the default one (same as FRDM-RW612).
# Murata publishes region power tables for the Type 2FR
# (github.com/murata-wireless/2FR, PowerTable/); they are not applied here yet.
if(CONFIG_WIFI_NXP)
  zephyr_include_directories(
      tx_pwr_limits
  )

  zephyr_compile_definitions(WIFI_BT_TX_PWR_LIMITS_OVERRIDE="wlan_txpwrlimit_cfg_WW_rw610.h")
endif()
