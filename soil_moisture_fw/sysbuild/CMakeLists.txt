# Sysbuild sees BOARD_ROOT before the application CMakeLists.txt runs.
get_filename_component(APP_DIR ${CMAKE_CURRENT_LIST_DIR}/.. ABSOLUTE)
list(APPEND BOARD_ROOT ${APP_DIR})

find_package(Sysbuild REQUIRED HINTS $ENV{ZEPHYR_BASE})

project(sysbuild LANGUAGES)
