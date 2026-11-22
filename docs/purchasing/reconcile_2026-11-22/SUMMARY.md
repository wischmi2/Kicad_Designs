# Parts reconciliation, 2026-11-22 (read-only: no schematic, PCB, BOM Builder, cart or order was touched)

Four sources compared per refdes: (1) schematics at HEAD, (2) each board sourcing BOM, (3) what Brian ordered, (4) BOM Builder inventory/overrides. One file per board in this folder (`<board>.md`) plus a proposed schematic write-back table (`<board>_writeback.csv`).

Quantities: need = per-board qty x board count (feather 5, gateway 5, pH 2, water level TC2030 3). ORP and the programming adapter were not in the 11-10 plan; I used 5 each (bare boards ordered 5 each), so their needs are an upper bound.

## What "ordered" means here (read this first)

- The 11-10 upload CSVs (digikey_order_2026-11-10) were a plan and do not match what was ordered. The carts in tobuy (19520332.csv, mouser_upload.xlsx) are a different, smaller list, and the order notes below differ from the carts again.
- The only evidence of what was actually ordered is the "Ordered ..." notes in BOM Builder `shopping_list.json` (saved 2026-11-11 19:20): DigiKey order 102853405 and Mouser order 41073583 (both 2026-11-11) and DigiKey web ID 379222461 (prog adapter parts, 2026-11-11). I found no order confirmations. If an item is missing from those notes I treat it as not ordered.
- The notes carry quantities that differ from the cart files on 9 lines (Brian cut quantities at checkout): DK ADUM1250ARZ-RL7 cart 1, ordered 2; DK DX07S016JA3R1500 cart 10, ordered 2; DK ISO1540DR cart 5, ordered 2; DK LBES0ZZ2FR-580 cart 5, ordered 2; DK MSASJ31LBB5227MTCA01 cart 5, ordered 2; DK NXE1S0303MC-R13 cart 5, ordered 3; DK RECE.20449.001E.01 cart 1, ordered 3; DK U.FL-R-SMT-1(10) cart 5, ordered 3; MO XM125 cart 5, ordered 2. I used the note quantity.
- Cart file lines not in any note: DigiKey BSS138LT1G x5 (0 stock; the note says Mouser x5 instead, but the Mouser file has no BSS138LT1G), DigiKey KMR221G LFS x15 (note says x10). Notes with no cart line: LQP03HQ3N9B02D x5, TMK107BBJ106MA-T x5.
- The 11-10 add-on list (gateway antenna, W1 housings/leads, 5 more 10 uF) has no order note except TMK107BBJ106MA-T x5. The antenna and W1 parts show as not ordered.
- BOM Builder files were last saved 2026-11-11 (inventory 17:59, shopping list 19:20). Nothing delivered since is recorded, so on-hand counts are pre-delivery. Stock numbers are live API reads from 2026-11-22 (DigiKey and Mouser).

## Verdict counts (lines = groups of identical parts; refdes in brackets)

| Board | WRONG | MISSING | CHECK | OK | DNP / N/A | Refs fitted (OK / all) |
|---|---|---|---|---|---|---|
| nRF54L15 feather (main) x5 | 1 (1) | 3 (3) | 4 (4) | 44 (64) | 5 / 0 | 64 / 72 |
| Water level TC2030 x3 | 1 (1) | 1 (1) | 1 (1) | 9 (18) | 0 / 0 | 18 / 21 |
| ORP x5 | 0 (0) | 3 (3) | 1 (1) | 14 (20) | 1 / 0 | 20 / 24 |
| pH sens1 x2 | 0 (0) | 1 (1) | 1 (1) | 9 (12) | 2 / 0 | 12 / 14 |
| Pouch gateway x5 | 0 (0) | 4 (6) | 3 (3) | 18 (46) | 6 / 3 | 46 / 55 |
| Programming adapter x5 | 0 (0) | 1 (1) | 1 (2) | 13 (19) | 0 / 0 | 19 / 22 |
| **Total lines** | 2 | 13 | 11 | 107 | 14 / 3 | |

Verdicts: OK = equal part or verified drop-in and enough in hand/ordered; CHECK = likely OK, something unverified; WRONG = ordered/mapped part does not fit footprint or spec; MISSING = needed, not ordered and not on hand (or short); EXTRA = ordered, not in any schematic. A line short on quantity is MISSING even if the part is right.

## WRONG and MISSING (act on these first)

| Verdict | Board | Item |
|---|---|---|
| WRONG | nRF54L15 feather (main) | LED1 SML-P12MTT86R (0402): BB override SMLEN3EC8TT86 is a green 0603, wrong footprint; 1 bought + 4 on hand are unusable; real part not bought (Mouser 23, DigiKey 0); DigiKey lists SML-P12MTT86R as yellow-green, not red. |
| MISSING | nRF54L15 feather (main) | C43 MSASJ31LBB5227MTCA01: 2 ordered, need 5 (DigiKey 892, Mouser 0). |
| MISSING | nRF54L15 feather (main) | J1 USB-C (feather + gateway, 10 needed): HRO TYPE-C-31-M-12 not buyable at DK/Mouser; 2 x JAE DX07S016JA3R1500 ordered, footprint fit unverified. |
| MISSING | nRF54L15 feather (main) | R19 RT0402BRD07100KL (100k 0.1%, changed 11-11): not bought, not on hand (need 5). |
| WRONG | Water level TC2030 | WL R1 RC0402FR-07220KL (220k): carts hold 22k parts (ERJ-2RKF2202X, RC0402FR-0722KL), wrong value; need 3 of the 220k. |
| MISSING | Water level TC2030 | WL U1 XM125: 2 ordered (Mouser), need 3 (Mouser 1,642; DigiKey 0). |
| MISSING | ORP | ORP R1 RC0402FR-0747KL (47k, changed 11-11): not bought, not on hand (need 5; DigiKey 0, Mouser 3.27 M, DK drop-in ERJ-2RKF4702X). |
| MISSING | ORP | ORP U2 Atlas OEM-ORP x5: no order or stock record anywhere. |
| MISSING | ORP | ORP U3 ISO1540DR: 2 ordered (backordered), need 5; DigiKey and Mouser both 0 today. |
| MISSING | pH sens1 | pH U2 Atlas OEM-pH x2: no order or stock record anywhere. |
| MISSING | Pouch gateway | Gateway J1 USB-C x5: same HRO/DX07 problem as feather J1 (shared 10). |
| MISSING | Pouch gateway | Gateway J3 U.FL-R-SMT-1(10): 3 ordered, need 5. |
| MISSING | Pouch gateway | Gateway SW1-SW3 KMR221G LFS: 10 ordered, need 15. |
| MISSING | Pouch gateway | Gateway U1 LBES0ZZ2FR-580: 2 ordered, need 5; DigiKey 0 and Mouser 0 today. |
| MISSING | Programming adapter | Prog adapter J6 USB4105-GF-A x5: no order or stock record (DigiKey 308,166 at $0.80). |
| MISSING | Pouch gateway | Off-board: ANT 1461530100 (Molex FPC antenna 100 mm) x5: In the 11-10 add-on list only; no order record in BB notes. Not a schematic part. |
| MISSING | Pouch gateway | Off-board: W1 cable PHR-8 housings x10 and ASPHSPH24K102 leads x40: LCD cable, in the 11-10 add-on list only; no order record. Not a schematic part. |
| MISSING | Programming adapter | FFSD-05-D-06.00-01-N x1 (Samtec ribbon cable, BB needs line CABLE3): In the BB needs file for the adapter but not in the schematic and no order record. |

EXTRA (ordered, not at HEAD):

- nRF54L15 feather (main): SMLEN3EC8TT86 x1 (Mouser 41073583). Green 0603 LED bought as the LED1 substitute; fits nothing in the schematic (see LED1 WRONG).
- Water level TC2030: RC0402FR-0722KL x5 (Mouser 41073583). Bought for the old 22k R_ID; R1 is 220k now. Nothing at HEAD uses it (gateway R4 takes the DigiKey 22k part instead).
- Programming adapter: SPC02SYAN x10 (DigiKey web ID 379222461). Shunts for JP1 (accessory, not a schematic part; BB needs lists it as JP1_SHUNT, need 1 per board).
- Programming adapter: TC2030-IDC x1 (DigiKey web ID 379222461). Programming cable for the TC2030 pads (tool, not a schematic part).
- Programming adapter: TTL-232RG-VREG1V8-WE x1 (DigiKey web ID 379222461). 1.8 V USB-UART cable for XM125 flashing (tool); backordered to about Dec 14.
- Feather R9: ERJ-3GEY0R00V x25 bought for 5 needed (price break, not an error).

## CHECK items (what to verify)

- nRF54L15 feather (main) C40: Mouser 41073583 x5 exact part but Mouser stock is 0 today (was 0 on 11-10 too), so the line is probably backordered: confirm ship date. DigiKey now has 7,009 ($0.19) as a fallback. Do not use on-hand C0603C226M9PACTU (6.3 V).
- nRF54L15 feather (main) J3: Not ordered. On hand 6 x FTSH-105-01-L-DV-K-A (suffix -A is an option variant: check the Samtec drawing for alignment-pin holes the footprint may lack). Plain part: DigiKey 98,306 at $1.37, Mouser 87,981 at $1.19.
- nRF54L15 feather (main) R11: FM8625H is not at DigiKey/Mouser. BB alternate Infineon BGS12P2L6E6327XTSA1 (on hand 5; BB also records 7 received), SPDT 50 MHz-6 GHz, 1.65-3.4 V, PG-TSLP-6-4 (same 1.1 x 0.7 mm 6-pad class as the DFN-6 footprint). Pinout and control logic vs FM8625H and pad fit are not verified. 11-10 plan alternate ASWD-S2-0002-T not bought.
- nRF54L15 feather (main) RF1: ECT818000500 not at DigiKey/Mouser. BB alternate RECE.20449.001E.01 (MHF4-compatible receptacle, DigiKey lists Taoglas; DigiKey x3 + on hand 4). Whether it fits the ECT818000500 footprint is unconfirmed (11-10 order md says the same). The 2026-10-28 sourcing BOM lists U.FL-R-SMT-1(10) for RF1, which is the wrong connector family.
- Water level TC2030 Q1: BB note says Mouser 41073583 x5, but the Mouser cart file in tobuy has no BSS138LT1G (the DigiKey cart line has 0 stock). Confirm the Mouser order. Today: DigiKey 872,892, Mouser 3,022.
- ORP J1: BAT Wireless BWSMA-KWE-Z001 is not at DigiKey/Mouser (LCSC C496551 per 11-10 md; no order recorded). On hand 9 x SuperBat X0036NHOHB (SMA edge-mount, Amazon): geometry vs the BWSMA footprint not verified. Pool need pH 2 + ORP 5 = 7.
- pH sens1 J1: Same SMA situation as ORP J1.
- Pouch gateway D1: Schematic PRTR5V0U2X; DigiKey x5 Wurth 8240026 (WE-TVS 2-line rail-to-rail steering diode, 5 V, SOT-143-4) bought in its place. Same topology but pin-for-pin pinout vs PRTR5V0U2X and the SOT-143 land pattern were never compared: verify before soldering.
- Pouch gateway D2: Schematic RB521S30T1G (30 V Schottky SOD-523); DigiKey x5 RB521S30-AU_R1_000A1 bought in its place per design notes. Same class; datasheet not compared.
- Pouch gateway L1: Schematic SWPA4020S2R2MT (+-20%); bought SWPA4020S2R2NT (+-30%, 1.85 A, Isat 3.7 A, 4 x 4 x 2 mm per DigiKey). Same footprint; tolerance looser: confirm TLV62569 inductance range.
- Programming adapter C1,C2: Bought CC0805KFX5R8BB106 in place of CC0805KKX5R8BB106 (out of stock then): both are Yageo 10 uF 10% 25 V X5R 0805 on DigiKey/Mouser, so the spec is the same. 9 delivered, 1 backordered to Apr 2027, need 10: top up 1 (KKX is back at DigiKey, 96,155).

## BOM Builder overrides and alternates touching these boards

| BB key | Maps to | Verdict | Why |
|---|---|---|---|
| SMLP12MTT86R (feather LED1) | SMLEN3EC8TT86 (override) | WRONG | Green 527 nm 0603 vs 0402 footprint; delete the override. |
| TYPEC31M12 (feather/gateway J1) | DX07S016JA3R1500 x2 (alternate, ordered) | CHECK | JAE 24-pos right-angle (16 + 8 dummy shell); not compared with the HRO footprint; only 2 of 10. |
| ECT818000500 (feather RF1) | RECE.20449.001E.01 x9 (alternate, 6 received) | CHECK | MHF4-class receptacle; footprint fit not confirmed. |
| FM8625H (feather R11) | BGS12P2L6E6327XTSA1 x7 (alternate, 7 received) | CHECK | Same 6-pad 1.1 x 0.7 mm class; pinout/logic vs FM8625H not verified. |
| LQP03HQ3N9B02D (feather L3) | LQP03TQ3N9B02D (override) | CHECK | TQ series has different Q to HQ in an RF match; HQ was bought anyway, so remove or flag the override. |
| CC0603KRX7R9BB104 (100 nF 0603 50 V) | GRM188R72A104KA35D (override) | OK | 100 V X7R 10% 0603, higher voltage, same dielectric. |
| GRM155R71C104KA88D, CC0402KRX7R7BB104 (100 nF 0402 16 V) | GCM155R71C104KA55D | OK | Same 0.1 uF 16 V X7R 0402. |
| GRM155R71H103KA88D (10 nF 50 V) | GCM155R71H103KA55D | OK | Same value/voltage/dielectric. |
| CRCW04024K70FKED (4.7k) | RC0402FR-074K7L | OK | Same 4.7k 1% 0402. |
| RCA025K1FLF (feather R1/R2, DNP) | CR0402-FX-5101GLF (alternate) | OK | 5.1k 1% 0402; parts are DNP anyway. |
| FRC0603F1503TS (150k 0603 1%) | AF0603FR-07150KL (alternate) | OK | Same value/size/tolerance. |
| S2BPHKSGWPP (feather U4/U5) | S2B-PH-K-S (alternate) | OK | Same JST PH 2-pin side-entry header. |
| NRF54L15QFXX, NPM1300QEXX | nRF54L15-QFAA-R7, nPM1300-QEAA-R7 | OK | Same devices; R7 is the reel code. |
| 2450AT18A100E (AE1) | 2450AT18A0100001E | OK | New part number of the same Johanson antenna. |
| CC0603MRX5R8BB106 (10 uF 25 V 0603) | GRT188R61E106ME13D (alternate, buy 0) | OK | Not bought; 10 uF 25 V X5R 0603. |
| CL10A225KB8NNNC | GRM188R61H225KE11D (alternate) | OK | Same 2.2 uF 50 V X5R 0603 10%; used by feather C3. |
| F980J476MMA, FRC0402F5600TS | GRM188R60J476ME01D, RC0402FR-07560RL | n/a | Older entries of other projects; the targets happen to be our parts and are fine for the feather C42 and R14. |

No other overrides in `shopping_list.json` point at parts used by these six boards. `compare_category_overrides.json` holds only resistor/semiconductor/connector category labels and nothing for these parts.

## Plan (11-10) and sourcing BOM errors found

- 11-10 plan R19 (feather) mapped to the 10k RT0402BRD0710KL; schematic R19 is 100k (changed 11-11).
- 11-10 plan WL R1 and GW R4 share ERJ-2RKF2202X (22k); WL R1 is 220k at HEAD. pH R1 in the plan is 10k; HEAD is 100k.
- 2026-10-28 feather sourcing BOM lists U.FL-R-SMT-1(10) for RF1; the schematic part is ECT818000500 (MHF4 footprint).
- Gateway sourcing/BB needs list SWPA4020S2R2NT for L1; the gateway schematic MPN field still says SWPA4020S2R2MT.
- Prog adapter sourcing BOM lists SPC02SYAN (shunt) for JP1; the schematic part is the PEC02SAAN header.
- BB needs files all say board_count 5 (pH really 2, water level 3). Their MPNs match the schematics (checked ref by ref) except gateway L1.
- The gateway schematic has an MPN on 3 of 55 fitted parts (J5, L1, U1); the rest carry only LCSC numbers. The write-back table fills them in.

## Open questions for Brian

- USB-C (feather J1 x5, gateway J1 x5, adapter J6 x5): the HRO part only exists at LCSC. Pick: GCT USB4105-GF-A (DigiKey $0.80, fits the feather footprint within 0.05 mm per the 11-07 study, gateway shell slot 0.2 mm short), LCSC C165948, or check the JAE DX07S016JA3R1500 drawing against the HRO footprint (only 2 bought).
- LED1: the footprint is a 0402; SML-P12MTT86R is yellow-green 572 nm per DigiKey (not red). Which colour do you want? The no-R part SML-P12MTT86 is a green, not-for-new-design part, not a substitute. Delete the BB override to the green 0603.
- Gateway LBES0ZZ2FR-580: 2 bought, 5 needed, now out of stock at DigiKey and Mouser. Build 2 gateways, or wait for restock?
- ORP ISO1540DR: 2 bought (backordered), 5 needed, 0 stock at both. Accept 2 ORP nodes or pick another isolator?
- New SENS_ID resistors (feather R19 100k 0.1%, water level R1 220k, ORP R1 47k) were never bought; buy now (about $0.12 each)?
- Small top-ups needed: C43 x3, XM125 x1, gateway KMR221G x5, U.FL x2, feather LED1 x5.
- Atlas OEM-pH x2, OEM-ORP x5 and the BWSMA SMA connectors (7): no order record. Ordered elsewhere? On hand are 9 SuperBat X0036NHOHB SMA edge connectors (not the same part).
- Gateway antenna 1461530100 x5 and LCD cable W1 housings/leads: ordered? No BB note.
- Confirm the three 2026-11-11 orders (DigiKey 102853405, Mouser 41073583, DigiKey web ID 379222461) really contain the BB-note quantities; I could only see BB notes.
- Feather C40 (Mouser x5, stock 0): confirm ship date, or buy at DigiKey (7,009 now).
- R11 (BGS12P2L6) and RF1 (RECE.20449.001E.01): who checks pinout/footprint before soldering? Do you want the BB alternates written to the schematic?
- Prog adapter: Samtec FFSD-05-D-06.00-01-N ribbon cable (BB CABLE3) has no order note. Needed?

## Stuck / not done

- Datasheet pinout and footprint comparisons were not done for D1 (8240026), D2, R11, RF1, J1 substitutes; they are CHECK, not verified. Spec equivalence for passives is from DigiKey/Mouser parametric descriptions, not datasheets.
- Mouser PN and DigiKey PN are blank in the write-back where the part is not sold there (listed per row in the Note column). Mouser PNs come from carts, live sourcing files, schematic fields, or the Mouser API search on 2026-11-22.

## Files

- `feather.md`, `feather_writeback.csv`: nRF54L15 feather (main)
- `water_level_tc2030.md`, `water_level_tc2030_writeback.csv`: Water level TC2030
- `orp.md`, `orp_writeback.csv`: ORP
- `ph_sens1.md`, `ph_sens1_writeback.csv`: pH sens1
- `gateway.md`, `gateway_writeback.csv`: Pouch gateway
- `prog_adapter.md`, `prog_adapter_writeback.csv`: Programming adapter
