param(
	[string]$NcsVersion = "v3.3.0",
	[string]$BuildDir = "",
	[string]$Board = "soil_moisture/nrf54l15/cpuapp"   # use nrf54l15_feather/nrf54l15/cpuapp for the feather
)

$ErrorActionPreference = "Stop"
$AppDir = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$NcsDir = "c:\ncs\$NcsVersion"
if (-not $BuildDir) {
	$BuildDir = Join-Path $AppDir "build"
}

$env:BOARD_ROOT = ($AppDir -replace '\\', '/')
New-Item -ItemType Directory -Force -Path $BuildDir | Out-Null

nrfutil sdk-manager toolchain launch --ncs-version=$NcsVersion --chdir $NcsDir -- `
	west build -p -b $Board `
	-d $BuildDir `
	$AppDir

Write-Host "HEX: $(Join-Path $BuildDir 'soil_moisture_fw\zephyr\zephyr.hex')"
