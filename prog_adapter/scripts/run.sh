set -e
TW=C:/Users/Brian/AppData/Local/Temp/claude/7513b01dd0a8f868/852340cd-ddbc-47b4-81bb-5ac0e7492d0d/scratchpad/tools
cd /c/Personal-Agents/worktrees/nrf54l15-feather-branch/prog_adapter
python $TW/gen_sch.py . >/dev/null
kicad-cli sch erc --severity-all -o $TW/erc.rpt prog_adapter.kicad_sch | tail -1
kicad-cli sch export netlist --format kicadxml -o $TW/net.xml prog_adapter.kicad_sch >/dev/null
"/c/Program Files/KiCad/10.0/bin/python.exe" $TW/gen_pcb.py "C:/Personal-Agents/worktrees/nrf54l15-feather-branch/prog_adapter" "$TW/../build" "$TW/net.xml" 2>&1 | tail -3
kicad-cli pcb drc --schematic-parity --severity-all --format json -o $TW/drc.json prog_adapter.kicad_pcb | tail -3
python $TW/drcsum.py $TW/drc.json
