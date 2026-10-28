cmake_minimum_required(VERSION 3.20.0)

# Absolute BOARD_ROOT for non-sysbuild builds; sysbuild uses sysbuild/CMakeLists.txt
list(APPEND BOARD_ROOT ${CMAKE_CURRENT_SOURCE_DIR})

find_package(Zephyr REQUIRED HINTS $ENV{ZEPHYR_BASE})

project(soil_moisture_bringup)

target_sources(app PRIVATE
	src/main.c
	src/fuel_gauge.c
)

if(CONFIG_BOARD_NRF54L15_FEATHER)
	target_sources(app PRIVATE src/feather_run5.c)
endif()
