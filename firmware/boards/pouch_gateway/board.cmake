# J-Link on J6 (Tag-Connect TC2030) or J2 (10-pin Cortex SWD, DNP by default).
# Device name as in the FRDM-RW612 board; check against the J-Link device list.
board_runner_args(jlink "--device=RW612" "--reset-after-load")

include(${ZEPHYR_BASE}/boards/common/jlink.board.cmake)
