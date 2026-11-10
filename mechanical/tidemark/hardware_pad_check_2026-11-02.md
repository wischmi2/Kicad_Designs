# Tidemark hardware vs pads check, 2026-11-02

Read-only check of both boards with KiCad Python (pcbnew, no save). Nothing in the repo was changed.
Hole centres are the same on both boards: H1 (92.54, 112.54), H2 (92.54, 130.32), H3 (138.26, 112.54), H4 (138.26, 130.32).
Distances are from the hole centre to the nearest copper edge or part edge, in mm.
Footprints: hex corners r 2.72 (flats r 2.35), screw head r 2.5, sled post r 4.0.
Hole types: main H1/H2 plated GND (drill 2.7, pad 3.4). Main H3/H4 NPTH. Sens1 H1/H2/H4 NPTH. Sens1 H3 plated GND (drill 2.7, pad 3.4).
Solder mask expansion is 0, so tracks, vias and pours are masked; only pads are bare.
Part heights come from the 3D model names (AE1 1.3, C26 0.8, L7 0.5, L4 0.5, C10 0.3, CN1 about 1.0). I could not read the SMA height reliably from the STEP (it is about 6.3 mm wide).

## Main board

| Hole | Face | Hardware | Nearest item | Distance | Verdict |
| --- | --- | --- | --- | --- | --- |
| H1 | Top (F) | screw head r 2.5 | H1 pad 3.4 (GND, bare) and GND pour; USB-C J1 pads/courtyard | pad under head; J1 at 3.96 | TOUCHES COPPER ONLY (bare GND pad). J1 CLEAR by 1.46 |
| H1 | Bottom (B) | hex r 2.72 | H1 pad and GND pour; no parts | 0 | TOUCHES COPPER ONLY, CLEAR of parts |
| H2 | Top (F) | screw head | H2 pad, GND pour; J1 shell pad 2 | J1 at 3.96 | TOUCHES COPPER ONLY (bare GND pad). J1 CLEAR |
| H2 | Bottom (B) | hex | H2 pad and GND pour; no parts | 0 | TOUCHES COPPER ONLY, CLEAR of parts |
| H3 | Top (F) | screw head | via SENS_ID 1.77; VBAT tracks 2.11 to 2.65; via VBAT 2.56; pad L4.1 3.10; C10 3.03; L7 4.21; C26 3.85 | 1.77 | TOUCHES COPPER ONLY (masked via and tracks). No part under the head. CLEAR |
| H3 | Bottom (B) | hex | via SENS_ID 1.77, SENS_ID track 1.68, via VBAT 2.56, via GND 3.11; no pads or parts | 1.68 | TOUCHES COPPER ONLY (masked). CLEAR |
| H4 | Top (F) | screw head | AE1 fab/courtyard edge 2.74 to 2.76, AE1 pad 2 at 2.84, AE1 silk 2.41; R18 4.03; CN1 4.21; GND pour 4.0 | 2.74 | CLEAR (0.24 to the AE1 body, head is taller than AE1 but not over it). Silk under head only |
| H4 | Bottom (B) | hex | nothing within 4.0 (AE1 keep-out, no fill) | over 4.0 | CLEAR |

## Sens1 board

| Hole | Face | Hardware | Nearest item | Distance | Verdict |
| --- | --- | --- | --- | --- | --- |
| H1 | Top (F) | bottom standoff hex | 7 mm square no-copper keep-out; pour at 3.5 (GND_ISO) and 4.5 (AGND_ISO); SMA J1 pads 5.2 | 3.5 | CLEAR |
| H1 | Bottom (B) | sled post r 4.0 | GND_ISO pour at 3.5, AGND_ISO at 4.5; no parts | 3.5 | TOUCHES COPPER ONLY (post overlaps the masked pour edge by 0.5). CLEAR of parts |
| H2 | Top (F) | hex | AGND_ISO pour 3.5; SMA J1 pads about 5.2 (bbox 4.72) | 3.5 | CLEAR |
| H2 | Bottom (B) | sled post | AGND_ISO pour 3.5; no parts | 3.5 | TOUCHES COPPER ONLY (0.5 overlap). CLEAR of parts |
| H3 | Top (F) | hex | H3 pad 3.4 (GND, bare) and GND pour; via GND 2.69 from edge; CN1 courtyard 4.21 | 0 | TOUCHES COPPER ONLY (bare GND pad). CLEAR of parts |
| H3 | Bottom (B) | sled post | H3 pad and GND pour; via GND 2.69; no parts | 0 | TOUCHES COPPER ONLY. CLEAR |
| H4 | Top (F) | hex | R1 keep-out (no copper); pour 4.0; CN1 courtyard 4.21 | 4.0 | CLEAR |
| H4 | Bottom (B) | sled post | pour at 4.0; no parts | 4.0 | CLEAR (post edge just reaches the pour) |

## Stack gap

- No sens1 top part lies within 3.7 mm of any hole, so no tall part sits just outside a hex. Nearest are SMA J1 (about 5.2) and CN1 (4.21, about 1 mm tall).
- Sens1 has no bottom-side part within 4.0 of any hole, so the sled posts do not hit anything.
- No main bottom-side part lies within 3.4 mm of any hole.
- The SMA J1 on sens1 is the tallest part. Its height against the 14 mm gap is not measured here. It is 5.2 mm from H1/H2, so it is not a hardware clash, but check its top against the main board underside in the Fusion model.

## AE1 plastic-only zone (main, 15 mm keep-out x 132.15 to 141.0, y 126.4 to 133.1)

- H4 is inside it. The hardware there is nylon only (screw, two standoffs). No metal hardware, and no copper within 4.0 mm of H4 on either layer.
- Sens1 has the same keep-out copper-free area. The sled insert under sens1 H4 is in the same plan view 14 mm or more below AE1. If it is a brass insert, note it; it is not in the main-board zone.

## Problems

1. No CLASH items.
2. H4 screw head is 0.24 mm from the AE1 body and 0.34 mm from its pad 2. Tight but clear. Fix if wanted: use a low-profile or smaller head, or skip the H4 screw (the standoff hex can hold the board with a flat nylon washer under the head, not over AE1). Also note the nylon head may detune AE1 slightly; bench check.
3. Sleds posts at sens1 H1/H2 overlap the pour by 0.5 mm. Nylon/PETG on masked copper, harmless. Only matters if the post has a sharp lip: keep a small chamfer.
4. Main H3 has a via and a track (SENS_ID) 1.7 mm from centre under the hex. Masked, harmless. If worried about pressure on the mask, a thin washer spreads the load.
5. Exposed bare GND pads at main H1/H2 and sens1 H3 contact nylon only. No electrical issue.
