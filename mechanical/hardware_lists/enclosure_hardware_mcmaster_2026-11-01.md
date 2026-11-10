# Enclosure hardware: McMaster-Carr purchase list (2026-11-01)

For the first PETG drafts of the Ledger (pouch gateway) and the Tidemark (feather node). Covers the
"not printed" hardware in both ASSEMBLY.md guides (assembly_guide_2026-11-01). Part numbers and
prices were read from mcmaster.com on 2026-11-01. Prices are before shipping. Nothing has been ordered.

## Order
| # | McMaster P/N | Item | Pack | Price | Used for (qty needed) |
| --- | --- | --- | --- | --- | --- |
| 1 | 94459A120 | Brass heat-set insert, M2 x 0.4, 4 mm long, max hole 3.3 mm | 50 | $9.91 | Ledger gateway bosses (4) + rear cover bosses (4) |
| 2 | 92095A452 | 18-8 SS button head hex screw, M2 x 5 | 25 | $3.80 | Ledger gateway board (4) + rear cover (4) |
| 3 | 99461A914 | 18-8 SS pan head Phillips thread-forming screw for plastic, M2 x 5 (52 ga = 1.6 mm pilot) | 25 | $5.33 | Ledger LCD module (4) |
| 4 | 94459A768 | Brass heat-set insert, M2.5 x 0.45, 4 mm long, **4.0 mm hole** | 25 | $8.18 | Tidemark sled posts (4) + plinth (4). **Model holes must change, see note 1** |
| 5 | 92290A056 | 316 SS socket head screw, M2.5 x 6 | 25 | $3.48 | Tidemark foot cap (4) |
| 6a | 95783A060 | Nylon hex standoff, M2.5 male-female, 14 mm | each | 4 x $2.87 = $11.48 | Tidemark board stack, replaces printed spacer D (4). See note 2 |
| 6b | 92492A709 | Nylon pan head Phillips screw, M2.5 x 5 | 100 | $10.73 | Main board into the standoffs (4) |
| 7 | 1178N19 | EPDM o-ring cord, 2.0 mm, 70A (water, dilute salt) | per ft, 3 ft min | 3 x $0.79 = $2.37 | Tidemark foot-cap o-ring, ~154 mm loop, join with CA glue |
| 8 | 2189K15 | Silica gel desiccant bag, 0.11 oz (~3 g), 44 x 25 mm | 10 | $9.18 | Tidemark, beside the battery (1) |

**Total about $64** before shipping. With option A in note 2 instead of rows 6a/6b, about $57.

## Notes
1. **M2.5 insert holes.** The Tidemark model has 3.5 mm (sled) and 3.6 mm (plinth) holes, 5 mm deep.
   McMaster's M2.5 heat-set inserts need a 4.0 mm hole (94459A768, 4 mm long) or a 4.1 mm hole (94459A439, 5.9 mm long).
   Either open the holes to 4.0 mm in Fusion and check the sled post wall, or buy M2.5 inserts made for a 3.5-3.6 mm hole
   somewhere else (e.g. Ruthex/CNC Kitchen M2.5) and skip row 4.
   The M2 inserts (row 1) fit the Ledger's 3.2 mm holes as modelled.
2. **No M2.5 x 20 nylon screws at McMaster** (nylon M2.5 goes up to 10 mm). Two options:
   - Recommended: rows 6a + 6b. A 14 mm nylon M-F standoff takes the place of the printed spacer. Its male end goes through sens1
     into the sled insert (3.9 mm thread: 1.6 mm board + ~2.3 mm in the insert). The main board screws into the top with an M2.5 x 5 nylon screw.
     Everything stays non-conductive, like the original design.
   - Option A: 92290A752, 316 SS socket head M2.5 x 20, 25 for $14.68, with the printed spacers. Only if metal screws through
     both boards' mounting holes are OK (check the antenna keep-out and which net the holes are on).
3. Optional heat-set tips (only if they fit your iron): 92160A341 (M2, $13.63), 92160A315 (M2.5, $9.38).
4. The make-your-own o-ring kit (9262N12, $47.54) isn't needed. A drop of CA glue (e.g. Loctite 401) on a square cut is enough for a draft.

## Not from McMaster
| Item | Where |
| --- | --- |
| Adhesive ePTFE vent patch for the 3.0 mm hole | DigiKey/Mouser (Gore or Amphenol adhesive vents). McMaster only has threaded enclosure vents |
| 14-way 0.5 mm FFC 30 mm, RG316 right-angle SMA pigtail, IP67 SMA bulkhead | DigiKey/Mouser |
| 602050 LiPo | Battery supplier (Adafruit, etc.) |
| Waveshare 2inch LCD, Molex 146153-0100 antenna, W1 cable parts (PHR-8, ASPHSPH24K102) | Already in the gateway live BOM |
| Thin foam, double-sided adhesive ring, short straight USB-C cable | Any |
