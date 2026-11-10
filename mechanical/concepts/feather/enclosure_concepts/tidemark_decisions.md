# Tidemark: Brian's decisions

Concept: Tidemark (concepts.md §4, 01-tidemark.svg), chosen by Brian 2026-10-27 for the nRF54L15 feather node.

| # | Question | Decision (2026-10-27) |
| --- | --- | --- |
| 1 | Seal level | IP66 target, built to IP67 geometry: one face o-ring on the foot cap, every opening facing down, ePTFE vent, 2 g silica gel. Claim only what passes a dunk test; run the 15 cm / 30 min dry-tissue test on the first print |
| 2 | Probe connection | Replaceable SMA bulkhead in the heel (IP67/68 panel jack with o-ring), short RG316/RG174 pigtail to sens1 J1, TPU boot over the mated plug. Heel about 14 mm deep. A sealed PCB-mount SMA (concept R2) is deferred to a later sensor-board revision. The water-level board's JST cable will need its own grommet or gland |
| 3 | USB-C | Outside, facing down in the toe: 12.5 x 7 mm tunnel, 2.5 mm wall, J1 0.5 mm behind it, tethered TPU 95A bung with two 0.3 mm interference ribs. Check J1 alignment in Fusion (J1 courtyard is 0.23 mm inside the board edge). If the bung fails the dunk test, upgrade to a panel-mount IP67 USB-C |
| 4 | Materials / printing | PETG shell, foot cap, sled, clips, leaf frame; TPU 95A (Brian has it) for the key, bung, boot and clip pads, **co-printed** into the PETG wall on the U1; clear PETG or a 2.5 mm acrylic rod light pipe. No ASA (indoor). Plastic only within 15 mm of AE1; check range once with the chosen navy spool |
| 5 | Colours | Family colourway: Abyss navy matte PETG shell (textured roof, fuzzy skin on side walls only), coral TPU key, coral translucent PETG eye, graphite TPU bung and boot, lowercase sensor tag debossed 0.4 mm above the toe ("ph", "orp", "do", "ec", "lvl"). Filament on hand not confirmed yet |
| 6 | Sensor-board changes | R1 (copper and part keep-out under AE1, fx 42.15-50.8 / fy 0-6.46, all layers): **sens1 only for now**; template, water-level, ORP, DO and EC get it when next revised. Queue after the main-board run 5. R2 (sealed PCB SMA) deferred, see Q2 |

Related decisions: battery = 602050-class LiPo behind sens1 (sourcing in progress); hole plating option A (plated/brass at the USB end, nylon at the antenna end); on-board NTC.

## First-draft prints (Brian 2026-10-29)
All first prints of every enclosure are drafts in plain PETG, one material. No TPU co-printing, fuzzy skin, colourway or debossed tag yet. Keep the TPU parts (key, bung, boot, clip pads) as separate bodies in the model, and print them in PETG for fit only or leave them off. The full CMF above applies from the second print on.
