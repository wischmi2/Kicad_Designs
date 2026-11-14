# Build the Pouch gateway app from the Zephyr v4.4.0 + Pouch workspace (C:\ncs\pouch-zephyr).
# The compiler comes from the NCS v3.4.0 toolchain bundle (Zephyr SDK 1.0.1), which Zephyr 4.4.0 accepts.
# Builds go outside the repo (default C:\ncs\pouch-builds). Pristine by default. Never flashes.
#   .\build.ps1                      both targets
#   .\build.ps1 -Target pouch_gateway
#   .\build.ps1 -Target frdm_rw612
param(
	[ValidateSet("all", "pouch_gateway", "frdm_rw612")]
	[string]$Target = "all",
	[string]$NcsVersion = "v3.4.0",                      # only used to select the toolchain bundle
	[string]$Workspace = "C:\ncs\pouch-zephyr",
	[string]$BuildRoot = "C:\ncs\pouch-builds",
	[switch]$Incremental                                   # default is a pristine build (west build -p)
)

$ErrorActionPreference = "Stop"
$AppDir = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$FwRoot = (Resolve-Path (Join-Path $AppDir "..\..")).Path   # firmware\ (BOARD_ROOT, holds boards\)

if (-not (Test-Path (Join-Path $Workspace ".west"))) {
	throw "West workspace not found at $Workspace (see firmware\README.md, SDK workspace for the RW612 gateway)"
}

$env:BOARD_ROOT = $FwRoot.Replace('\', '/')
New-Item -ItemType Directory -Force -Path $BuildRoot | Out-Null
$pristine = if ($Incremental) { "auto" } else { "always" }

function Invoke-GatewayBuild([string]$Board, [string]$BuildDir, [string[]]$CmakeArgs) {
	Write-Host "=== $Board -> $BuildDir"
	$west = @("build", "-p", $pristine, "-b", $Board, "-d", $BuildDir.Replace('\', '/'), $AppDir.Replace('\', '/'))
	if ($CmakeArgs) { $west += "--"; $west += $CmakeArgs }
	nrfutil sdk-manager toolchain launch --ncs-version=$NcsVersion --chdir $Workspace -- west @west
	if ($LASTEXITCODE -ne 0) { throw "west build failed for $Board ($LASTEXITCODE)" }
	Write-Host "Image   : $(Join-Path $BuildDir 'zephyr\zephyr.hex')  (also zephyr.bin)"
}

if ($Target -in @("all", "pouch_gateway")) {
	# Our board (Murata Type 2FR, Wi-Fi only). boards\pouch_gateway.conf is picked up automatically.
	Invoke-GatewayBuild "pouch_gateway" (Join-Path $BuildRoot "gateway_pouch_gateway") @()
}
if ($Target -in @("all", "frdm_rw612")) {
	# NXP FRDM-RW612 dev board with Wi-Fi (Ethernet is the default without the extra conf).
	Invoke-GatewayBuild "frdm_rw612" (Join-Path $BuildRoot "gateway_frdm_rw612") @("-DEXTRA_CONF_FILE=boards/frdm_rw612_wifi.conf")
}
