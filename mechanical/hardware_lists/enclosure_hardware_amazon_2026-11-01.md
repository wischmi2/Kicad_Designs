# Enclosure hardware: Amazon purchase list (2026-11-01)

This is the Amazon version of `enclosure_hardware_mcmaster_2026-11-01.md`, for the Ledger and Tidemark first PETG drafts.
ASINs, prices and specs were read from amazon.com on 2026-11-01. Amazon listings and prices change, so check the size on each page before buying.
Nothing has been ordered or added to a cart. Link format: https://www.amazon.com/dp/<ASIN>

## Order
| # | ASIN | Item (as listed) | Pack | Price | Used for | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | B088QJG676 | ruthex RX-M2x4 M2 heat-set inserts | 70 | $9.99 | Ledger: 8 (gateway bosses + rear cover) | 4 mm long. ruthex states a 3.2 mm hole, which is what the Ledger has (spec from memory, not shown on the page) |
| 2 | B0DPQK6RJZ | M2.5 brass heat-set inserts, 4 mm L x 4 mm OD | 100 | $7.19 | Tidemark: 8 (sled posts + plinth) | Needs a ~3.6 mm hole; the Tidemark model has had 3.6 mm holes since Fusion v14 (issue 1, closed) |
| 3 | B0DLKCR1CQ | M2 x 5 button head hex, 304 stainless | 100 | $7.86 | Ledger gateway board + rear cover (8) | |
| 4 | B07Q36GBKY | uxcell M2 x 5 self-tapping Phillips pan head, 316 stainless | 50 | $6.99 | Ledger LCD module (4) | Into the 1.6 mm pilot holes |
| 5 | B0GCSRG1WD | M2.5 x 6 socket head cap, 304 stainless | 50 | $6.19 | Tidemark foot cap (4) | Amazon has no 316 in this size; 304 will stain over time on a salt tank |
| 6 | B0B5M1M822 | 435 pc M2.5 black nylon M-F standoff kit (MCMASKE) | kit | $12.99 | Tidemark board stack | Lengths 6/8/10/12/15/18/20/22/25 mm, 15 of each, 6 mm male thread, 4.7 mm hex. Comes with 50 nylon M2.5 x 6 and 50 x 10 screws, nuts and washers. See issue 2 |
| 7 | B00QVB0ZG6 | Mr O-Ring 2 mm (0.079") silicone o-ring cord, 70A | 10 ft | $15.39 | Tidemark foot-cap o-ring (~154 mm loop) | Same 70A hardness as the McMaster EPDM. Join with CA glue |
| 8 | B0GSRKXHFT | 1 g silica gel packets | 100 | $5.84 | Tidemark | Use 1. There's no room beside the battery; the pack goes in the slot between the sled rib and the sleeve's left wall, beside the boards (Fusion v15-v17, 2026-11-02). A second pack does not fit |
| 9 | B0F45VY7KK | VOSAREA ePTFE breathable anti-fog membrane, adhesive | 100 sheets | $13.49 | Tidemark cap vent (1) | Sold for car lamps. The listing gives no disc size: anything 6-10 mm wide fits over the 3.0 mm hole |
| 10 | B0FDKYTMZ8 | 100 pcs M3 x 4 mm x 5 mm brass heat-set inserts (model 242707-US) | 100 | not read (page returned 503 on 2026-11-07) | prog_adapter Bench Tray: 4 (board posts) | Added 2026-11-07 (Brian). M3 thread, 4 mm long, 5 mm OD. The Bench Tray model uses a 4.1 mm x 5 mm deep hole, which suits this 5 mm OD insert. Other M3x4x5 packs work too; check the 5 mm OD, since some "M3x4" packs are 4.0-4.2 mm OD and need a smaller hole |
| 11 | (to pick) | M3 x 6 button-head socket screws, 304 stainless (length set by the Bench Tray model, Fusion v4) | - | - | prog_adapter Bench Tray: 4 | Choose once the Fusion model sets the length; button head, stainless |
| 12 | B082GFTZQD | Waveshare 2inch LCD Module, 240x320 IPS, ST7789, SPI (Waveshare store; manufacturer Waveshare, model "2inch IPS LCD Display Module") | 1 module + PH2.0 8-pin 20 cm cable | $17.27 | Ledger gateway display (1) | Added 2026-11-08. Same module as the gateway BOM (Waveshare SKU 17344, 58 x 35 mm, PH2.0). Ships from Amazon, sold by UeeKKoo, in stock. Waveshare.com is $10.99 plus shipping (2026-10-28). The included 20 cm cable is replaced by W1 in the Ledger; W1 parts stay in the gateway DigiKey BOM. Other Waveshare listings of the same module: B081NBBRWS $18.99, B09N2MZ2MY $17.27. Avoid the unbranded 2.0 in ST7789 modules: the Ledger bosses were modelled on the Waveshare board, and other boards' size and holes weren't checked |
| 13 | (to pick) | Nylon M6 x 30 knurled thumbscrew, head up to 20 mm dia (M6 x 35 also works; M6 x 25 is too short) | - | - | Tidemark Perch: 1 (wall clamp) | Added 2026-11-11 from `mechanical	idemark\perch_2026-11-05\PERCH.md` |
| 14 | (to pick) | Nylon M6 hex nut, 10 mm AF x 5 mm | - | - | Tidemark Perch: 1 (captive in the leg) | Added 2026-11-11. Check 10 mm across flats; the pocket is 10.3 mm |
| 15 | (to pick) | Nylon M4 x 25 pan head screw (M4 x 30 also works) | - | - | Tidemark Perch: 1 (Collet clamp) | Added 2026-11-11 |
| 16 | (to pick) | Nylon M4 hex nut, 7 mm AF x 3.2 mm | - | - | Tidemark Perch: 1 (captive in the Collet) | Added 2026-11-11 |
| 17 | (to pick) | Nylon M4 x 10 pan head screw, head about 7 mm dia | - | - | Tidemark Perch: 2 (Collet stops, self-tap into 3.4 mm holes) | Added 2026-11-11. A nylon M4 assortment kit can cover items 15-17 |

**Total about $86** before tax/shipping (items 1-9; items 10-11 added 2026-11-07 for the prog_adapter tray, prices not read; item 12, the gateway LCD at $17.27, added 2026-11-08; items 13-17, the Perch probe mount nylon hardware, added 2026-11-11, ASINs not picked yet). That's more than McMaster ($64) because Amazon sells bigger packs. Most of these ship free with Prime.

## Issues with the Amazon parts
1. **M2.5 insert size. Closed 2026-11-01 evening: option (b) chosen, Tidemark Fusion v14 has 3.6 mm holes for B0DPQK6RJZ.** The rest of this item is the original note. The Tidemark model was changed today to 4.0 mm holes to fit McMaster 94459A768. The Amazon M2.5 inserts are 3.5-4.0 mm across and need a 3.2-3.8 mm hole. None found was clearly made for a 4.0 mm hole (ruthex M2.5 is 5.7 mm long, longer than the 5 mm hole). Pick one:
   - (a) Buy only the McMaster M2.5 inserts (94459A768, 25 for $8.18) and everything else from Amazon. No model change.
   - (b) Buy B0DPQK6RJZ and change the Tidemark sled and plinth holes back to 3.6 mm (a short Fusion edit). The sled posts stay 8 mm, so the walls get thicker.
2. **Standoff length.** Amazon nylon kits don't come in 14 mm. Stack an 8 mm and a 6 mm standoff (the 6 mm male end of the top one goes into the 8 mm one) to get 14 mm. The 8 mm one goes at the bottom: its male end goes through sens1 into the sled insert.
   - That male thread is 6 mm, against McMaster's 3.9 mm. 1.6 mm passes through sens1 and 4.4 mm goes into the hole. That's 0.4 mm past the end of a 4 mm insert, which still fits in the 5 mm deep hole (0.6 mm to spare).
   - The main board goes on top with the kit's nylon M2.5 x 6 screws.
   - The hex is 4.7 mm across the flats, against 4.5 mm (about 5.4 mm across the corners). That's 0.1 mm more per side than the model has.

## Not on this list
FFC, RG316 pigtail, SMA bulkhead, LiPo, antenna and W1 cable parts are electronics, bought from DigiKey/Mouser. The parts list for those is in the McMaster file.
