# Rebuild schematic + board from parts.py / gen_sch.py / gen_pcb.py, then ERC and DRC (no refill).
# usage: bash scripts/run.sh <scratch build dir>
set -eo pipefail
TW=${1:?build dir}
mkdir -p "$TW"
cd "$(dirname "$0")/.."
PRJ="$(pwd -W 2>/dev/null || pwd)"
python scripts/gen_sch.py . >/dev/null
kicad-cli sch erc --severity-all -o "$TW/erc.rpt" prog_adapter.kicad_sch | tail -1
kicad-cli sch export netlist --format kicadxml -o "$TW/net.xml" prog_adapter.kicad_sch >/dev/null
"/c/Program Files/KiCad/10.0/bin/python.exe" scripts/gen_pcb.py "$PRJ" "$TW/build" "$TW/net.xml" 2>&1 | tail -3
kicad-cli pcb drc --schematic-parity --severity-all --format json -o "$TW/drc.json" prog_adapter.kicad_pcb | tail -3
python scripts/drcsum.py "$TW/drc.json"
