# usage: proof.sh <scratch> <project>  -- rules-file load proof on the saved board (no refill)
S=$1; P=$2; rm -rf $S/pf; mkdir -p $S/pf/strict $S/pf/noexc
for d in strict noexc; do cp -r $P/prog_adapter.kicad_{pcb,pro,sch} $P/prog_adapter.kicad_sym $P/prog_adapter.pretty $P/fp-lib-table $P/sym-lib-table $S/pf/$d/; done
cp $P/prog_adapter.kicad_dru $S/pf/strict/; printf '(rule "strict test"\n\t(constraint track_width (min 5mm)))\n' >> $S/pf/strict/prog_adapter.kicad_dru
head -6 $P/prog_adapter.kicad_dru > $S/pf/noexc/prog_adapter.kicad_dru
for d in strict noexc; do echo "== $d"; kicad-cli pcb drc --severity-all --format json -o $S/pf/$d/drc.json $S/pf/$d/prog_adapter.kicad_pcb >/dev/null; python $P/scripts/drcsum.py $S/pf/$d/drc.json | head -2; done
