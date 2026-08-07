param(
	[string]$NcsVersion = "v3.3.0",
	[string]$BuildDir = ""
)

$ErrorActionPreference = "Stop"
$AppDir = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$NcsDir = "c:\ncs\$NcsVersion"
if (-not $BuildDir) {
	$BuildDir = Join-Path $AppDir "build_v330"
	if (-not (Test-Path (Join-Path $BuildDir "soil_moisture_fw\zephyr\zephyr.hex"))) {
		$BuildDir = Join-Path $AppDir "build"
	}
}

Write-Host "Connected devices:"
nrfutil device list

nrfutil sdk-manager toolchain launch --ncs-version=$NcsVersion --chdir $NcsDir -- `
	west flash -d $BuildDir
