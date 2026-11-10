cmake_minimum_required(VERSION 3.20.0)

# BOARD_ROOT = firmware (board defs in firmware/boards/) for non-sysbuild builds; sysbuild uses sysbuild/CMakeLists.txt
get_filename_component(FW_ROOT ${CMAKE_CURRENT_SOURCE_DIR}/../.. ABSOLUTE)
list(APPEND BOARD_ROOT ${FW_ROOT})

find_package(Zephyr REQUIRED HINTS $ENV{ZEPHYR_BASE})

project(soil_moisture_bringup)

target_sources(app PRIVATE
	src/main.c
	src/fuel_gauge.c
)

if(CONFIG_BOARD_NRF54L15_FEATHER)
	target_sources(app PRIVATE src/feather_run5.c)
endif()
