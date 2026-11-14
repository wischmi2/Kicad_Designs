# Program the feather Pouch node with nrfutil (west flash does not work on Windows:
# the pouch runner imports pty/termios).
#
# chip_erase_mode=ERASE_NONE is required. Omitting it makes nrfutil erase the whole
# nRF54L chip, including the LittleFS credential partition. A full erase or
# "nrfutil device recover" also wipes the credentials.
#
# MCUboot goes in first at 0x0, then the signed application (0x10000). There is no merged.hex.
# Close J-Link RTT Viewer first, it owns the probe.
#
# Usage:  .\flash.ps1 -Serial <J-Link serial number>
param(
	[Parameter(Mandatory = $true)]
	[string]$Serial,                                          # J-Link serial, no default on purpose
	[string]$BuildDir = "C:\ncs\pouch-builds\feather_pouch"
)

$ErrorActionPreference = "Stop"
$McubootHex = Join-Path $BuildDir "mcuboot\zephyr\zephyr.hex"
$AppHex = Join-Path $BuildDir "feather_node\zephyr\zephyr.signed.hex"
foreach ($f in @($McubootHex, $AppHex)) {
	if (-not (Test-Path $f)) { throw "Missing $f (run build.ps1 first)" }
}

Write-Host "Connected devices:"
nrfutil device list

$opts = "chip_erase_mode=ERASE_NONE,verify=VERIFY_READ"

nrfutil device program --serial-number $Serial --firmware $McubootHex --options $opts
if ($LASTEXITCODE -ne 0) { throw "MCUboot program failed ($LASTEXITCODE)" }

nrfutil device program --serial-number $Serial --firmware $AppHex --options "$opts,reset=RESET_SYSTEM"
if ($LASTEXITCODE -ne 0) { throw "Application program failed ($LASTEXITCODE)" }
