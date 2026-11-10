# DigiKey / Mouser alternates for fab-ready boards (checked 2026-11-07)

Scope: parts that fit the boards' CURRENT footprints, no layout change. No schematic, board or footprint file was edited. Stock and price are live API results from DigiKey and Mouser on 2026-11-07 (price for qty 1 / 10). Datasheets read: GCT USB4105, USB4930, USB4940 drawings; Abracon ASWD-S2-0002 (abracon.com, rev A 8/28/2025); Murata and I-PEX catalogs (RF1, partial). The HRO TYPE-C-31-M-12 drawing itself (krhro.com) returned 403, so the HRO side is taken from the KiCad stock footprint (which cites that drawing) and from the boards.

## Summary

| Item | Best DK/Mouser part | Drop-in? | Brian must decide |
| --- | --- | --- | --- |
| 1 J1 USB-C | GCT USB4105-GF-A (DK 2073-USB4105-GF-ACT-ND, Mouser 640-USB4105-GF-A); USB4930-00-A is the same land pattern, cheaper | Feather: yes in all pad and hole positions (a shell tab check remains). Gateway: near drop-in, 3 small differences listed below | Order 2 of the GCT part and test-fit on a spare board before the main order, or accept the residual risk |
| 2 R11 RF switch | Abracon ASWD-S2-0002-T (DK 535-ASWD-S2-0002-TCT-ND, Mouser 815-ASWD-S2-0002-T) | Yes on package, pinout, logic polarity, supply and VCTL levels. Pad overlap is slightly off-nominal (see below) | Accept, or fit R21 0R and leave R11 off |
| 3 RF1 U.FL | I-PEX 20449-001E-03 (MHF4, DK 5378-20449-001E-03CT-ND) is the likely pattern match, NOT confirmed | Unconfirmed. Land pattern could not be verified | Compare the I-PEX land drawing to RF1, or leave RF1 off (chip antenna works through R11/R21 without it) |
| 4 TC2030 adapter | Same Sky SSK05-BH-254-B3 box header plus Yageo 1k/330R, Sullins shunt, Bud perfboard | Yes (all through-hole, no board change) | Mouser has no TC2030-IDC; cable is DigiKey only |

## 1. J1 USB-C, HRO TYPE-C-31-M-12 (feather and gateway)

Important finding first: the two boards do not use the same land pattern for this part.
- Gateway J1: KiCad stock `Connector_USB:USB_C_Receptacle_HRO_TYPE-C-31-M-12`, at (114.37, 93.35) rot -90, board edge x = 110.
- Feather J1: EasyEDA footprint `easyeda2kicad:USB-C_SMD-TYPE-C-31-M-12_1`, at (95.32, 121.43) rot -90, board edge x = 90.
Both are for the same HRO part, but the pad row sits at a different distance from the positioning holes (table). The real HRO drawing was not readable, so I could not say which one is right for the HRO part; I compared both to the GCT drawing.

Candidate: GCT USB4105-GF-A (and -A-060 / -A-120 shell stake lengths 0.60 / 1.20 mm instead of 0.95; USB4930-00-A has an identical PCB layout drawing). All distances below are from the NPTH row (y of the two 0.65 holes), +y toward the plug mouth. GCT drawing tolerance on the layout is +-0.05 mm.

| Dimension (mm) | GCT USB4105 / 4930 | Gateway footprint (KiCad HRO) | Feather footprint (EasyEDA) |
| --- | --- | --- | --- |
| NPTH diameter / x spacing | 0.65 / +-2.89 | 0.65 / +-2.89 (match) | 0.75 / +-2.90 (hole 0.10 larger, fine) |
| Signal pad pitch (A5-B8) | 0.5 / 0.75 / 1.25 / 1.75 | same | same |
| Outer pads x (GND/VBUS) | +-3.20 / +-2.40 | +-3.25 / +-2.45 (0.05 off) | +-3.20 / +-2.40 (match) |
| Pad width | 0.60 / 0.30 | 0.60 / 0.30 | 0.60-class / 0.30 |
| Pad row centre / length | 1.075 behind NPTH / 1.15 | 1.445 behind / 1.45 | 1.26 behind / 1.3 |
| Pad coverage of GCT tail | tail spans 0.50 to 1.65 behind | pad spans 0.72 to 2.17: covers 0.93 of 1.15 | pad spans 0.61 to 1.91: covers 1.04 of 1.15 |
| Front shell slot (hole) | 0.6 x 1.7, 0.50 behind NPTH, x +-4.32 | 0.6 x 1.7, 0.53 behind (match) | 0.8 x 1.6, 0.50 behind, x +-4.33 (0.1 shorter, 0.2 wider) |
| Rear shell slot (hole) | 0.6 x 1.4, 3.68 ahead of NPTH | 0.6 x 1.2, 3.65 ahead (0.2 SHORTER) | 0.8 x 1.4, 3.68 ahead (match in length) |
| Shell stake length (below board) | 0.95 (or 0.60 / 1.20) | board is 1.6 mm, ok | ok |
| Body height | 3.31 mm | fits (HRO is 3.26 per GCT 4940 drawing of the similar part; KiCad HRO model not checked) | n/a |
| Shell front vs board edge | GCT: shell front 6.28 ahead of NPTH | 0.72 mm inside the edge (same as HRO footprint) | 0.25 mm inside the edge |

Verdict:
- Feather J1 with GCT USB4105-GF-A / USB4930-00-A: every position matches within 0.05 mm. Pad row, outer-pad x and rear slot length match; front slot is 0.1 mm short but 0.2 mm wider than the GCT slot. Remaining unknown: the GCT stake (tab) lengths, which the drawing shows only as hole sizes. Expect it to fit (holes are the GCT recommended size or larger), not guaranteed.
- Gateway J1 with the same GCT part: three differences: (a) outer pads 0.05 mm further out in x (inside tolerance for a 0.6 mm pad), (b) pad row is 0.37 mm further back than the GCT pad centre, so the pad still covers 0.93 mm of the 1.15 mm tail (the tail end sits 0.22 mm on bare mask; solder fillet will be a little short), (c) rear shell slots are 0.6 x 1.2 against the GCT 1.4 hole. If the GCT rear stake is longer than 1.2 mm it will not go in. That is the one that could make it a non-drop-in. Cannot be decided from the drawing alone.
- So: "drop-in" holds for the feather; for the gateway it is a near drop-in pending a test fit.

Stock and price (2026-11-07):

| MPN | Maker | DigiKey | DK stock | DK price 1 / 10 | Mouser | Mouser stock | Mouser price 1 / 10 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| USB4105-GF-A | GCT | 2073-USB4105-GF-ACT-ND (also -ADKR-ND) | 138,469 | 0.80 / 0.676 | 640-USB4105-GF-A | 390,294 | 0.80 / 0.676 |
| USB4105-GF-A-120 (1.20 mm stakes) | GCT | 2073-USB4105-GF-A-120CT-ND | 38,469 | 0.80 / 0.676 | 640-USB4105-GF-A-120 | 75,152 | 0.93 / 0.81 |
| USB4930-00-A (same layout drawing, 10k cycles instead of 20k, "New Product") | GCT | 2073-USB4930-00-ACT-ND | 2,320 | 0.45 / 0.384 | 640-USB4930-00-A | 7,450 | 0.45 / 0.384 |

Rejected:
- GCT USB4940-00-A (cheaper, $0.54): its layout has SMT shell pads (4 x 2.00 x 2.18 mm), no through-hole shell slots. NOT a drop-in.
- Amphenol 10155435-00011LF, 10171746-00021LF, Amphenol 12401610E4, GCT USB4500/4505/4510/4520 (mid-mount), USB4800/4805 (elevated), Attend 217B (0 stock at DK): different shell/hole layout or mounting style. Not compared dimension by dimension; mid-mount parts need a board cutout.
- Shouhan USB-C16PIN-3MD-ENIEC (DK 6652-USB-C16PIN-3MD-ENIECTR-ND): listed unshielded, no price, datasheet is a Google Drive link. Not usable.

Recommendation: GCT USB4105-GF-A (Mouser 640-USB4105-GF-A, DK 2073-USB4105-GF-ACT-ND). Order a couple and test-fit on a bare board before relying on it for the gateway.

## 2. R11, FM8625H antenna switch (feather)

How R11 is wired (STATUS.md and board, 2026-10-28): DFN-6 1.1 x 0.7 mm, 0.4 mm pitch. Pin 1 RF2 (to U.FL RF1), pin 2 GND, pin 3 RF1 (ANT_CHIP, to C12/L3/AE1), pin 4 VDD (VRF, 2.5 V from nPM1300 LDSW2), pin 5 ANT common, pin 6 VCTL (ANT_VCTL, from U7 74AUP1G34 powered from VRF, so a high is about VRF - 0.1 V = 2.4 V). Firmware drives low for the chip antenna. R21 0R DNP bypasses R11.

Candidate: Abracon ASWD-S2-0002-T, SOI SPDT reflective, 0.1-2.7 GHz (3 GHz max), 6-DFN 1.15 x 0.75 x 0.50 mm, 0.4 mm pitch, 0.25 x 0.25 mm pads.

| Check | ASWD-S2-0002 | R11 / board | Result |
| --- | --- | --- | --- |
| Pinout | 1 RF2, 2 GND, 3 RF1, 4 VDD, 5 RFC, 6 VCTL, pin 1 chamfer on the lower-left pad in top view | 1 RF2, 2 GND, 3 RF1, 4 VDD, 5 ANT, 6 VCTL, same numbering order | Match |
| Logic | VCTL 0: RF1 on / RF2 off; 1: RF1 off / RF2 on | low = chip antenna on RF1 (firmware dts) | Match (same polarity as the current firmware) |
| VDD | 1.6 to 3.3 V (rec. 2.8 V typ), IDD 35 uA typ / 60 max | VRF 2.5 V | Ok |
| VCTL | high 1.2 to 2.85 V, low max 0.4 V, abs max VDD | about 2.4 V from U7 on the same rail | Ok (control never above VDD) |
| Power order | VDD first, then VCTL; VCTL high with VDD off leaks | both come from VRF, VCTL is derived from it | Ok |
| 2.4 GHz | IL 0.37 dB typ, isolation 25 dB at 2.2-2.7 GHz, P0.1dB +34.5 dBm | | Ok |
| Land pattern | pads 0.25 x 0.25, centres 0.40 apart in x, row centres 0.45 apart in y | board pads 0.22 x 0.42 at row centres 0.66 apart | Part pads fall inside the board pads in x (+0.015 mm each side) and y. The inner edge of the part pad is 0.02 mm inside the board pad edge. Fits; fillets will be on the outer ends only. Hand soldering a 1.15 x 0.75 mm DFN needs paste and hot air or a hotplate |

Caveats: the FM8625H datasheet was never opened by anyone (see STATUS), so a side-by-side with the original is not possible; this check is against the board wiring. Datasheet RF1/RF2 symmetric ESD is rated 1.5 kV HBM. MSL 3.

| MPN | Maker | DigiKey | DK stock | DK price 1 / 10 | Mouser | Mouser stock | Mouser price 1 / 10 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ASWD-S2-0002-T | Abracon | 535-ASWD-S2-0002-TCT-ND | 4,960 | 0.37 / 0.253 | 815-ASWD-S2-0002-T | 4,005 | 0.37 / 0.253 |

Other Abracon parts in the same 1.15 x 0.75 DFN: ASWD-S2-0001-T (DC-8 GHz, 1.6-3.1 V, 14 dB isolation at 8 GHz; pinout and logic not checked, DK 535-ASWD-S2-0001-TCT-ND 4,771 / Mouser 815-ASWD-S2-0001-T 4,945, $0.47 / 0.329). Use -0002. ASWD-S2-0003/-0005 are SOT-363, not drop-in.

Fallback if Brian does not want it: leave R11 off and fit R21 0R (chip antenna only, no U.FL path); no part needed beyond the already-listed R21.

## 3. RF1 (feather)

- What it is: ECT818000500, ECT (Dongguan Electric Connect) SMD RF coaxial receptacle, LCSC C437254, labelled in the footprint as a 1.7 x 1.7 x 0.8 mm part with 2.0 mm pad spacing (EasyEDA model name ANT-SMD_L1.7-W1.7-H0.8-LS2.0). Pads: signal pad 2 (0.65 x 0.55) on net R11-RF2, GND pads 1/3 (1.5 x 0.6) at x = +-1.0 and GND pad 4 (0.5 x 0.55).
- DigiKey / Mouser: not listed at either (searched 2026-11-07, no match).
- Existing BOM entry (Hirose U.FL-R-SMT-1(10)) is a wrong footprint (about 4.1 x 4.0 mm land pattern vs about 3.5 x 2.5 here); it stays rejected. Murata MM8130-2600 (2.5 x 2.5 body with switch, land pattern 4.0 x 4.1) is also not a match.
- Likely drop-in class: a 2.0 x 2.0 mm MHF4-type receptacle (I-PEX catalog: MHF4 receptacle SMT size 2.0 x 2.0 mm, 1.2 mm mated height). I did NOT get the I-PEX land-pattern drawing, so pad sizes and positions are unconfirmed.

| MPN | Maker | DigiKey | DK stock | DK price 1 / 10 | Mouser | Mouser stock | Mouser price 1 / 10 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20449-001E-03 (MHF4) | I-PEX | 5378-20449-001E-03CT-ND | 56,733 | 0.74 / 0.626 | not found at Mouser | - | - |
| RECE.20449.001E.01 (MHF4 compatible) | Taoglas | 931-1158-1-ND | 60,788 | 1.01 / 0.859 | 960-RECE20449-001E01 | 35,480 | 0.98 / 0.836 |
| CONMHF4-SMD-G-T (MHF4) | TE / Linx | not checked | - | - | 712-CONMHF4-SMD-G-T | 15,854 | 0.35 / (0.32 at 250) |

Verdict: not confirmed as a drop-in. Action needed: put the I-PEX 20449-001E recommended land pattern next to the RF1 pads (kicad-designer). If it does not match, RF1 can be left unfitted: the chip-antenna path works without it, and the cable is only for a conducted test port. Do not buy until the pattern is checked. Whichever receptacle is chosen, the mating plug must match (MHF4 plug and cable, e.g. I-PEX MHF4 harness 8-25-0886 at 100 mm per the I-PEX catalog; DK link not checked).

## 4. TC2030 adapter parts (feather_water_level_tc2030, XM125_PROGRAMMING.md part 0)

| Need | MPN | Maker | DigiKey | DK stock | DK 1 / 10 | Mouser | Mouser stock | Mouser 1 / 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Cable (legged, 8 in, 6-pin 0.1 in IDC socket) | TC2030-IDC | Tag-Connect | TC2030-IDC-ND | 245 | 44.58 / no 10 price | none (Mouser lists only TC2030-MCP-NL, the Microchip RJ-type cable, not the IDC one) | - | - |
| Shrouded keyed 2x3 0.1 in box header, straight TH | SSK05-BH-254-B3 | Same Sky | 2223-SSK05-BH-254-B3-ND | 1,234 | 0.24 / 0.202 | 179-SSK05BH254B3 | 1,977 | 0.24 / 0.203 |
| 2-pin 0.1 in header (snap from 1x40) | PRPC040SAAN-RC | Sullins | S1011EC-40-ND | 65,250 | 1.23 / 1.041 | 649-68000-236HLF (Amphenol FCI, 1x36) | 753 | 2.68 / 2.39 |
| Shunt jumper | SPC02SYAN (gold) | Sullins | S9001-ND | 1,441,283 | 0.10 / 0.029 | 649-68786-202LF (Amphenol FCI, gold) | 14,495 | 0.29 / 0.248 |
| 1 k resistor, 1/4 W axial TH | MFR-25FBF52-1K | Yageo | 1.00KXBK-ND | 38,830 | 0.10 / 0.042 | 603-MFR-25FBF52-1K | 103,245 | 0.10 / 0.042 |
| 330 ohm x2 (also in the guide) | MFR-25FBF52-330R | Yageo | MFR-25FBF52-330R-ND | 8,644 | 0.11 / 0.044 | 603-MFR-25FBF52-330R | 13,582 | 0.11 / 0.044 |
| Perfboard, 2.54 mm PTH pads, 53.3 x 32.0 mm | EXN-23400-PCB | Bud Industries | 377-2623-ND | 525 | 2.30 / 2.25 | 563-EXN-23400-PCB | 40 | 2.30 / 2.25 |

Notes:
- TC2030-IDC: the DigiKey listing reads "PLUG-OF-NAILS 6-PIN W/ LEGS 8in", active. A no-legs IDC version (TC2030-IDC-NL) did not come up at DigiKey (search 2026-11-07), only TC2030-MCP-NL and others, which are the RJ-type cable and not the 0.1 in IDC socket. Confirm on the Tag-Connect site if the no-legs version is wanted.
- SSK05-BH-254-B3 is a 2x3, 2.54 mm box header ("H:8.9"), straight through-hole, polarised shroud. Not checked: the key notch orientation and pin 1 position in the datasheet, which has to match pin 1 on the cable socket (guide says to mark pin 1 on the board). Alternative right-angle shrouded 2x3: Amphenol FCI 75867-231LF (Mouser 649-75867-231LF, 4,738, $0.80 / 0.682) if the cable should exit sideways.
- Any 2x3 box header would mate the IDC socket. Do not substitute a bare pin header (the guide explains the reversed-plug danger).
- The Bud perfboard is 2.10 x 1.26 in; cut or leave it. The SSK05 pins are 2.54 mm pitch and fit its holes (1.30 mm).
- Total at qty 1 (DigiKey): 44.58 + 0.24 + 1.23 + 0.10 + 0.10 + 0.22 + 2.30 = about 48.77 USD, of which the cable is 44.58; the box header and shunt each have a minimum of 1 unit.

## Open items and unverified
- J1: HRO drawing not read; GCT stake (tab) lengths not on the drawing; Which of the two boards' footprints matches real HRO parts is unknown. A test fit with the GCT part on a bare board answers everything.
- R11: FM8625H datasheet never opened; ASWD-S2-0002 compared with the board wiring only. Pad overlap computed from the Abracon drawing (0.25 x 0.25 pads).
- RF1: land pattern for any replacement unconfirmed.
- Stock and prices are single API snapshots from 2026-11-07, not a cart check.
