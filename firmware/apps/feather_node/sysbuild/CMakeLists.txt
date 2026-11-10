# Sysbuild sees BOARD_ROOT before the application CMakeLists.txt runs.
# BOARD_ROOT = firmware (board defs in firmware/boards/), two levels above the app.
get_filename_component(FW_ROOT ${CMAKE_CURRENT_LIST_DIR}/../../.. ABSOLUTE)
list(APPEND BOARD_ROOT ${FW_ROOT})

find_package(Sysbuild REQUIRED HINTS $ENV{ZEPHYR_BASE})

project(sysbuild LANGUAGES)
