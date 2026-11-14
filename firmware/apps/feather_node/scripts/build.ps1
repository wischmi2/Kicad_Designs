# Build the feather Pouch node with NCS v3.4.0 from the Pouch workspace (C:\ncs\pouch-ncs).
# Sysbuild builds MCUboot and the application. Output (outside the repo by default):
#   <BuildDir>\mcuboot\zephyr\zephyr.hex                  -> programmed at 0x0
#   <BuildDir>\feather_node\zephyr\zephyr.signed.hex      -> programmed at 0x10000
param(
	[string]$NcsVersion = "v3.4.0",
	[string]$Workspace = "C:\ncs\pouch-ncs",
	[string]$BuildDir = "C:\ncs\pouch-builds\feather_pouch",
	[string]$Board = "nrf54l15_feather/nrf54l15/cpuapp",   # soil_moisture/nrf54l15/cpuapp also builds
	[switch]$Incremental                                     # default is a pristine build (west build -p)
)

$ErrorActionPreference = "Stop"
$AppDir = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$FwRoot = (Resolve-Path (Join-Path $AppDir "..\..")).Path   # firmware\ (BOARD_ROOT, holds boards\)

if (-not (Test-Path (Join-Path $Workspace ".west"))) {
	throw "West workspace not found at $Workspace (see firmware\README.md, SDK workspace)"
}

$env:BOARD_ROOT = ($FwRoot -replace '\\', '/')
New-Item -ItemType Directory -Force -Path $BuildDir | Out-Null

$pristine = if ($Incremental) { "auto" } else { "always" }

nrfutil sdk-manager toolchain launch --ncs-version=$NcsVersion --chdir $Workspace -- `
	west build -p $pristine -b $Board `
	-d ($BuildDir -replace '\\', '/') `
	($AppDir -replace '\\', '/')
if ($LASTEXITCODE -ne 0) { throw "west build failed ($LASTEXITCODE)" }

Write-Host "MCUboot : $(Join-Path $BuildDir 'mcuboot\zephyr\zephyr.hex')"
Write-Host "App     : $(Join-Path $BuildDir 'feather_node\zephyr\zephyr.signed.hex')"
