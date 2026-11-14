# Pouch gateway for the Pouch gateway board (Murata Type 2FR, NXP RW612).
# Based on golioth/pouch examples/zephyr/gateway at 32ded9b (Copyright (c) 2025 Golioth, Inc.,
# Apache-2.0). Differences: builds out of this repo, firmware\ is added to BOARD_ROOT, the
# git_describe.h step no longer runs a .sh script (that hangs the build on Windows), the CA
# certificate is taken from the Pouch checkout instead of being copied here.
# SPDX-License-Identifier: Apache-2.0

cmake_minimum_required(VERSION 3.20.0)

# BOARD_ROOT = firmware (board definitions in firmware/boards/)
get_filename_component(FW_ROOT ${CMAKE_CURRENT_SOURCE_DIR}/../.. ABSOLUTE)
list(APPEND BOARD_ROOT ${FW_ROOT})

find_package(Zephyr REQUIRED HINTS $ENV{ZEPHYR_BASE})
project(pouch_gateway)

target_sources(app PRIVATE
  src/credentials.c
  src/fatal_error.c
  src/main.c
)

if(CONFIG_WIFI)
  target_sources(app PRIVATE src/wifi.c)
endif()

# GIT_DESCRIBE = describe of this repo at configure time
execute_process(COMMAND git describe --always --dirty
  WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}
  OUTPUT_VARIABLE GW_GIT_DESCRIBE
  OUTPUT_STRIP_TRAILING_WHITESPACE
  ERROR_QUIET)
if(NOT GW_GIT_DESCRIBE)
  set(GW_GIT_DESCRIBE "unknown")
endif()
file(WRITE ${CMAKE_CURRENT_BINARY_DIR}/git_describe.h
  "#define GIT_DESCRIBE ${GW_GIT_DESCRIBE}\n")
target_include_directories(app PRIVATE ${CMAKE_CURRENT_BINARY_DIR})

if (NOT CONFIG_EXAMPLE_COAP_CLIENT_DTLS_LOAD_CA_FROM_FILESYSTEM)
  # ISRG Root X1 (public CA certificate) from the Pouch checkout
  generate_inc_file_for_target(app
    ${ZEPHYR_POUCH_MODULE_DIR}/examples/zephyr/http_client/src/isrgrootx1.der
    ${ZEPHYR_BINARY_DIR}/include/generated/pouch-ca-crt.inc)
endif()
