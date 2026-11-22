# nRF54L15 feather (main): parts reconciliation, 2026-11-22

Schematic: `hardware/feather/nrf54l15_feather/` at HEAD (kicad-cli 10 `sch export bom`, run 2026-11-22). Boards counted: 5.
Two builds share the board: Standard (all fitted, 2 pH nodes) and Radar (R15-R18 not fitted, 3 water level nodes). Need below counts R15-R18 for all 5; only 2 are strictly needed.
Sources: schematic fields; sourcing BOM in hardware/feather/sourcing (MPN column = 2026-10-30/11-08/11-07 CSV, swaps = 2026-10-28 live CSV); the 11-10 plan (order_2026-11-10.md); what was ordered (BB shopping_list.json Ordered notes, last saved 2026-11-11 19:20, and the carts in tobuy); on hand (BB inventory.json, last saved 2026-11-11 17:59). Stock checked live 2026-11-22.

Counts (lines = groups of identical parts, refs in brackets): WRONG 1 (1), MISSING 3 (3), CHECK 4 (4), OK 44 (64), DNP 5 (8)

## Problems

| Verdict | Refs | Schematic | Ordered | On hand | Need | Note |
|---|---|---|---|---|---|---|
| WRONG | LED1 | SML-P12MTT86R LED-SMD_L1.0-W0.6-RD_SML-P12YTT86RR SML-P12MTT86R | - | - | 5 | BB override SMLP12MTT86R -> SMLEN3EC8TT86 is wrong: that part is a green 527 nm 0603 (1.6 x 0.8 mm) LED; the footprint is 0402 (1.0 x 0.6 mm). One was ordered on Mouser (x1) and 4 are on hand: neither fits. The correct 0402 part SML-P12MTT86R was not ordered (Mouser 23 in stock, DigiKey 0, 52 wk). DigiKey lists SML-P12MTT86R as yellow-green 572 nm, not red: confirm the colour. The 11-10 md suggestion SML-P12MTT86 (no R) is a different part: DigiKey lists it green, Not For New Designs, and Mouser says the factory is not accepting orders, so do not use it. [short by 5 vs demand 5] |
| MISSING | C43 | 220uF C_1206_3216Metric MSASJ31LBB5227MTCA01 | MSASJ31LBB5227MTCA01 x2 [DK] | - | 5 | Only 2 ordered (BB note; cart file had 5). Need 5. DigiKey 892 in stock, Mouser 0. On-hand MSASJ32MAB5227MPNDT1 is 1210, not a drop-in for the 1206 pad. [short by 3 vs pool/line demand 5] |
| MISSING | J1 | TYPE-C-31-M-12 USB-C_SMD-TYPE-C-31-M-12_1 TYPE-C-31-M-12 | DX07S016JA3R1500 x2 [DK] | - | 5 (pool 10) | HRO TYPE-C-31-M-12 is not at DigiKey/Mouser (LCSC C165948 only) and no HRO order is recorded. BB override buys JAE DX07S016JA3R1500 (24 pos = 16 + 8 dummy shell, right angle SMD + THT) x2 only; footprint not compared with the EasyEDA HRO pattern. The 11-10 plan suggested GCT USB4105-GF-A (study says it fits the feather footprint) but it was not ordered. Pool need: feather 5 + gateway 5. [short by 8 vs pool/line demand 10] |
| MISSING | R19 | 100k R0402 RT0402BRD07100KL | - | - | 5 | R19 is 100k 0.1% since 2026-11-11. Nothing bought or on hand: the 11-10 plan and carts only have the 10k RT0402BRD0710KL. DigiKey 70,116 at $0.12. [short by 5 vs pool/line demand 5] |
| CHECK | C40 | 22uF C_0603_1608Metric CL10A226MP8NUNE | CL10A226MP8NUNE x5 [MO] | - | 5 | Mouser 41073583 x5 exact part but Mouser stock is 0 today (was 0 on 11-10 too), so the line is probably backordered: confirm ship date. DigiKey now has 7,009 ($0.19) as a fallback. Do not use on-hand C0603C226M9PACTU (6.3 V). |
| CHECK | J3 | FTSH-105-01-L-DV-K SAMTEC_FTSH-105-01-L-DV-K FTSH-105-01-L-DV-K | - | FTSH-105-01-L-DV-K-A x6 | 5 | Not ordered. On hand 6 x FTSH-105-01-L-DV-K-A (suffix -A is an option variant: check the Samtec drawing for alignment-pin holes the footprint may lack). Plain part: DigiKey 98,306 at $1.37, Mouser 87,981 at $1.19. |
| CHECK | R11 | FM8625H DFN-6_L1.1-W0.7-P0.40-BL FM8625H | - | BGS12P2L6E6327XTSA1 x5 | 5 | FM8625H is not at DigiKey/Mouser. BB alternate Infineon BGS12P2L6E6327XTSA1 (on hand 5; BB also records 7 received), SPDT 50 MHz-6 GHz, 1.65-3.4 V, PG-TSLP-6-4 (same 1.1 x 0.7 mm 6-pad class as the DFN-6 footprint). Pinout and control logic vs FM8625H and pad fit are not verified. 11-10 plan alternate ASWD-S2-0002-T not bought. |
| CHECK | RF1 | ECT818000500 ANT-SMD_ECT818000500 ECT818000500 | RECE.20449.001E.01 x3 [DK] | RECE.20449.001E.01 x4 | 5 | ECT818000500 not at DigiKey/Mouser. BB alternate RECE.20449.001E.01 (MHF4-compatible receptacle, DigiKey lists Taoglas; DigiKey x3 + on hand 4). Whether it fits the ECT818000500 footprint is unconfirmed (11-10 order md says the same). The 2026-10-28 sourcing BOM lists U.FL-R-SMT-1(10) for RF1, which is the wrong connector family. |
| EXTRA | - | SMLEN3EC8TT86 x1 (Mouser 41073583) | - | - | - | Green 0603 LED bought as the LED1 substitute; fits nothing in the schematic (see LED1 WRONG). |

## All parts

| Refs | Value / footprint | Sch MPN | Sourcing BOM MPN | 11-10 plan (whole-line buy qty) | Ordered (BB notes, whole-line qty) | On hand | Need | Stock 11-22 (write-back MPN) | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| LED1 | SML-P12MTT86R LED-SMD_L1.0-W0.6-RD_SML-P12YTT86RR | SML-P12MTT86R | SML-P12MTT86R | SML-P12MTT86R x10 | - | - | 5 | DK 0 / MO 23 | WRONG |
| C43 | 220uF C_1206_3216Metric | MSASJ31LBB5227MTCA01 | MSASJ31LBB5227MTCA01 | MSASJ31LBB5227MTCA01 x5 | MSASJ31LBB5227MTCA01 x2 [DK] | - | 5 | DK 892 / MO 0 | MISSING |
| J1 | TYPE-C-31-M-12 USB-C_SMD-TYPE-C-31-M-12_1 | TYPE-C-31-M-12 | TYPE-C-31-M-12 | USB4105-GF-A x12 | DX07S016JA3R1500 x2 [DK] | - | 5 (pool 10) | DK n/a / MO n/a | MISSING |
| R19 | 100k R0402 | RT0402BRD07100KL | RT0402BRD07100KL (live swap: RT0402BRD0710KL) | RT0402BRD0710KL x25 | - | - | 5 | DK 70,116 / MO 189,857 | MISSING |
| C40 | 22uF C_0603_1608Metric | CL10A226MP8NUNE | CL10A226MP8NUNE | ZRB18AR61A226ME01L x10 | CL10A226MP8NUNE x5 [MO] | - | 5 | DK 7,009 / MO 0 | CHECK |
| J3 | FTSH-105-01-L-DV-K SAMTEC_FTSH-105-01-L-DV-K | FTSH-105-01-L-DV-K | FTSH-105-01-L-DV-K | FTSH-105-01-L-DV-K x6 | - | FTSH-105-01-L-DV-K-A x6 | 5 | DK 98,306 / MO 87,981 | CHECK |
| R11 | FM8625H DFN-6_L1.1-W0.7-P0.40-BL | FM8625H | FM8625H | ASWD-S2-0002-T x6 | - | BGS12P2L6E6327XTSA1 x5 | 5 | DK 343,984 / MO 333,256 | CHECK |
| RF1 | ECT818000500 ANT-SMD_ECT818000500 | ECT818000500 | ECT818000500 (live swap: U.FL-R-SMT-1(10)) | - | RECE.20449.001E.01 x3 [DK] | RECE.20449.001E.01 x4 | 5 | DK 59,445 / MO 34,558 | CHECK |
| AE1 | 2450AT18A0100001E ANT-SMD_L3.2-W1.6 | 2450AT18A0100001E | 2450AT18A0100001E | 2450AT18A0100001E x7 | - | 2450AT18A0100001E x8 | 5 | DK 153,619 / MO 0 | OK |
| C1,C10 | 2.2uF C0201 | GRM033R61A225ME47D | GRM033R61A225ME47D | CC0201MRX5R6BB225 x14 | GRM033R61A225ME47D x10 [MO] | GRM033R61A225KE47D x11 | 10 | DK 0 / MO 6,747 | OK |
| C12 | 1.0pF C0201 | GJM0335C1E1R0WB01D | GJM0335C1E1R0WB01D | GJM0335C1E1R0WB01D x15 | - | GJM0335C1E1R0WB01D x8 | 5 | DK 203,396 / MO 239,540 | OK |
| C13 | 0.3pF C0201 | GJM0335C1ER30WB01D | GJM0335C1ER30WB01D | GJM0335C1ER30WB01D x15 | - | GJM0335C1ER30WB01D x8 | 5 | DK 3,958 / MO 198,165 | OK |
| C16 | 10uF C0603 | CC0603MRX5R8BB106 | CC0603MRX5R8BB106 | TMK107BBJ106MA-T x50 | CL10A106MA8NRNC x24 [MO]; TMK107BBJ106MA-T x5 [DK] | CC0603MRX5R8BB106 x6 | 5 (pool 35) | DK 0 / MO 0 | OK |
| C19 | 1uF C0402 | CL05A105KO5NNNC | CL05A105KO5NNNC | GRM155R61C105KA12D x28 | CL05A105KO5NNNC x27 [MO] | CL05A105KO5NNNC x13 | 5 (pool 28) | DK 0 / MO 1,346 | OK |
| C3 | 2.2uF C0603 | GRM188R61H225KE11D | GRM188R61H225KE11D | GRM188R61H225KE11J x10 | - | GRM188R61H225KE11D x7 | 5 | DK 0 / MO 12,140 | OK |
| C41,C54 | 10uF C_0402_1005Metric | GRM155R60J106ME15D | GRM155R60J106ME15D | GRM155R60J106ME15D x23 | GRM155R60J106ME15D x15 [DK] | GRM155R60J106ME15J x9 | 10 (pool 13) | DK 1,826,511 / MO 2,698,042 | OK |
| C42 | 47uF C_0603_1608Metric | GRM188R60J476ME15D | GRM188R60J476ME15D | GRM188R60J476ME01D x10 | GRM188R60J476ME15D x5 [MO] | GRM188R60J476ME01D x9 | 5 | DK 0 / MO 654 | OK |
| C44 | 4.7uF C0805 | CL21A475KAQNNNE | CL21A475KAQNNNE | CL21A475KACLRNC x10 | CL21A475KAQNNNE x5 [MO] | - | 5 | DK 15,103 / MO 9,804 | OK |
| C45,C48 | 100nF C0402 | GCM155R71C104KA55D | GCM155R71C104KA55D | GCM155R71C104KA55D x100 | GCM155R71C104KA55D x100 [DK] | - | 10 (pool 82) | DK 3,503,855 / MO 0 | OK |
| C46 | 10uF C_0603_1608Metric | GRM188R61C106MA73D | GRM188R61C106MA73D | TMK107BBJ106MA-T x50 | GRM188R61C106MA73D x5 [MO] | - | 5 | DK 0 / MO 1,345,995 | OK |
| C47 | 100pF C_0402_1005Metric | CL05C101JB5NNNC | CL05C101JB5NNNC | CC0402JRNPO9BN101 x15 | CL05C101JB5NNNC x5 [MO] | - | 5 | DK 0 / MO 48 | OK |
| C49,C50 | 100nF C_0201_0603Metric | CL03A104KQ3NNNC | CL03A104KQ3NNNC | CL03A104KQ3NNNC x20 | CL03A104KQ3NNNC x10 [DK] | - | 10 | DK 4,191,590 / MO 5,849 | OK |
| C5 | 2.0pF C0201 | GJM0335C1E2R0WB01D | GJM0335C1E2R0WB01D | GJM0335C1E2R0WB01D x15 | - | GJM0335C1E2R0WB01D x8 | 5 | DK 227,137 / MO 11,236 | OK |
| C51 | 1uF C_0402_1005Metric | CL05A105KA5NQNC | CL05A105KA5NQNC | CL05A105KA5NQNC x15 | CL05A105KA5NQNC x5 [DK] | - | 5 | DK 1,696,649 / MO 288,075 | OK |
| C6,C14,C15,C26 | 100nF C0603 | CC0603KRX7R9BB104 | CC0603KRX7R9BB104 | CC0603KRX7R9BB104 x50 | GRM188R72A104KA35D x24 [MO] | GRM188R72A104KA35D x21 | 20 (pool 37) | DK 85,912 / MO 1,361,404 | OK |
| C7,C17,C18,C20,C22 | 10uF C0805 | GRM21BR61E106MA73L | GRM21BR61E106MA73L | TMK212BBJ106MG-T x35 | GRM21BR61E106MA73L x35 [MO] | GRM21BR61E106KA73K x1000 | 25 (pool 35) | DK 47,989 / MO 6,545 | OK |
| C8 | 1.5pF C0201 | GJM0335C1E1R5WB01D | GJM0335C1E1R5WB01D | GJM0335C1E1R5WB01D x15 | - | GJM0335C1E1R5WB01D x8 | 5 | DK 192,970 / MO 0 | OK |
| C9 | 10nF C0402 | GCM155R71H103KA55D | GCM155R71H103KA55D | GCM155R71H103KA55D x15 | GCM155R71H103KA55D x2 [DK] | GCM155R71H103KA55D x8 | 5 (pool 10) | DK 1,465,276 / MO 3,808,466 | OK |
| CN1 | 503480-1400 Molex_503480-1400_1x14-1MP_P0.50mm_Horizontal | 503480-1400 | 503480-1400 (live swap: 5034801400) | 5034801400 x11 | 5034801400 x25 [DK] | - | 5 (pool 15) | DK 26,283 / MO 16,510 | OK |
| D1,D2 | TPD1E10B06DPYR Texas_DPY0002A_0.6x1mm_P0.65mm | TPD1E10B06DPYR | TPD1E10B06DPYR | TPD1E10B06DPYR x12 | TPD1E10B06DPYR x10 [DK] | - | 10 | DK 8,502 / MO 268,226 | OK |
| D3 | SMF12A D_SOD-123F | SMF12A | SMF12A | SMF12A x10 | SMF12A x10 [DK] | - | 5 | DK 50,977 / MO 8,990 | OK |
| F1 | 200mA Fuse_0603_1608Metric | MF-FSMF020X-2 | MF-FSMF020X-2 | MF-FSMF020X-2 x7 | MF-FSMF020X-2 x5 [DK] | - | 5 | DK 133,396 / MO 19,526 | OK |
| IC1 | AEM10330-QFN QFN40P500X500X85-41N-D | AEM10330-QFN | AEM10330-QFN | AEM10330-QFN x6 | AEM10330-QFN x1 [MO] | AEM10330-QFN x4 | 5 | DK n/a / MO 584 | OK |
| L11 | 10uH L_Sunlord_SWPA252010S | DFE252010F-100M=P2 | DFE252010F-100M=P2 | DFE252010F-100M=P2 x7 | DFE252010F-100M=P2 x5 [DK] | - | 5 | DK 9,840 / MO 4,080 | OK |
| L2,L5 | 2.7nH L0201 | LQP03HQ2N7B02D | LQP03HQ2N7B02D | LQP03HQ2N7B02D x20 | LQP03HQ2N7B02D x10 [DK] | - | 10 | DK 70,592 / MO 19,698 | OK |
| L3 | 3.9nH L0201 | LQP03HQ3N9B02D | LQP03HQ3N9B02D | LQP03HQ3N9B02D x15 | LQP03HQ3N9B02D x5 [DK] | - | 5 | DK 15,537 / MO 28,834 | OK |
| L4 | BLM15AG121SN1D L0402 | BLM15AG121SN1D | BLM15AG121SN1D | BLM15AG121SN1D x10 | BLM15AG121SN1D x5 [DK] | - | 5 | DK 654,902 / MO 64,177 | OK |
| L6,L8 | 3.5nH L0201 | LQP03HQ3N5B02D | LQP03HQ3N5B02D | LQP03HQ3N5B02D x20 | LQP03HQ3N5B02D x2 [DK] | LQP03HQ3N5B02D x8 | 10 | DK 369,695 / MO 49,142 | OK |
| L7 | 4.7uH L0603 | LQM18PN4R7MFRL | LQM18PN4R7MFRL | LQM18PN4R7MFRL x7 | LQM18PN4R7MFRL x5 [DK] | - | 5 | DK 81,929 / MO 159,468 | OK |
| L9,L10 | 2.2uH L0603 | LSCND1608HKT2R2MF | LSCND1608HKT2R2MF | LSCND1608HKT2R2MF x12 | LSCND1608HKT2R2MF x10 [MO] | - | 10 | DK 0 / MO 20,529 | OK |
| R10 | 150k R0603 | RC0603FR-07150KL | RC0603FR-07150KL | RC0603FR-07150KL x15 | RC0603FR-07150KL x10 [DK] | AF0603FR-07150KL x48 | 5 | DK 66,945 / MO 273,460 | OK |
| R12,R13,R15,R16 | 4.7k R0402 | RC0402FR-074K7L | RC0402FR-074K7L | RC0402FR-074K7L x34 | RC0402FR-074K7L x10 [DK] | RC0402FR-074K7L x39 | 20 (pool 34) | DK 320,000 / MO 4,737,940 | OK |
| R14 | 560 R0402 | RC0402FR-07560RL | RC0402FR-07560RL | RC0402FR-07560RL x15 | - | RC0402FR-07560RL x23 | 5 | DK 91,553 / MO 1,476,656 | OK |
| R17,R18 | 10k R0402 | RT0402BRD0710KL | RT0402BRD0710KL | RT0402BRD0710KL x25 | - | RT0402BRD0710KL x47 | 10 | DK 293,601 / MO 2,653 | OK |
| R8 | 10k NTC B3380 R0402 | NCU15XH103F60RC | NCU15XH103F60RC | NCU15XH103F60RC x15 | NCU15XH103F60RC x5 [DK] | - | 5 | DK 76,764 / MO 261,435 | OK |
| R9 | 0R R0603 | ERJ-3GEY0R00V | ERJ-3GEY0R00V | ERJ-3GEY0R00V x15 | ERJ-3GEY0R00V x25 [DK] | - | 5 | DK 4,093,399 / MO 2,187,561 | OK |
| SW1 | SW_Push SW_SPST_B3U-1000P | B3U-1000P | B3U-1000P | B3U-1000P x6 | B3U-1000P x5 [DK] | - | 5 | DK 117,657 / MO 36,368 | OK |
| U2 | nPM1300-QEXX QFN-32-1EP_5x5mm_P0.5mm_EP3.6x3.6mm_ThermalVias | nPM1300-QEAA-R7 | nPM1300-QEAA-R7 | NPM1300-QEAA-R7 x6 | - | nPM1300-QEAA-R7 x7 | 5 | DK 9,257 / MO 1,722 | OK |
| U4,U5 | S2B-PH-K-S CONN-TH_S2B-PH-K-S-GW | S2B-PH-K-S(LF)(SN) | S2B-PH-K-S(LF)(SN) | S2B-PH-K-S x12 | S2B-PH-K-S(LF)(SN) x6 [MO] | S2B-PH-K-S x4 | 10 | DK 595,192 / MO 33,964 | OK |
| U6 | nRF54L15-QFXX QFN-48-1EP_6x6mm_P0.4mm_EP4.6x4.6mm_ThermalVias | nRF54L15-QFAA-R | nRF54L15-QFAA-R | NRF54L15-QFAA-R x6 | NRF54L15-QFAA-R x2 [DK] | NRF54L15-QFAA-R7 x3 | 5 | DK 25 / MO 0 | OK |
| U7 | SN74AUP1G34DCKR SOT-353_SC-70-5 | SN74AUP1G34DCKR | SN74AUP1G34DCKR | SN74AUP1G34DCKR x10 | SN74AUP1G34DCKR x5 [DK] | - | 5 | DK 17,165 / MO 5,432 | OK |
| X1 | XRCGB32M000F1S2AR0 CRYSTAL-SMD_4P-L2.0-W1.6-BL | XRCGB32M000F1S2AR0 | XRCGB32M000F1S2AR0 | XRCGB32M000F1S2AR0 x7 | XRCGB32M000F1S2AR0 x5 [DK] | - | 5 | DK 6,953 / MO 2,678 | OK |
| C11 | 2.2pF C0201 | GJM0335C1E2R2WB01D DNP | - | - | - | GJM0335C1E2R2WB01D x6 | 0 | - | DNP |
| C52,C53 | DNP C_0201_0603Metric | - DNP | - | - | - | - | 0 | - | DNP |
| R1,R2 | 5.1k R0402 | RCA025K1FLF DNP | - | - | - | - | 0 | - | DNP |
| R20,R21 | 1M R_0402_1005Metric | 0402WGF1004TCE DNP | - | - | - | - | 0 | - | DNP |
| X2 | 32.768kHz Crystal_SMD_2012-2Pin_2.0x1.2mm | X1A0000610008 DNP | - | - | - | - | 0 | - | DNP |

## Notes per line

- LED1 (WRONG): BB override SMLP12MTT86R -> SMLEN3EC8TT86 is wrong: that part is a green 527 nm 0603 (1.6 x 0.8 mm) LED; the footprint is 0402 (1.0 x 0.6 mm). One was ordered on Mouser (x1) and 4 are on hand: neither fits. The correct 0402 part SML-P12MTT86R was not ordered (Mouser 23 in stock, DigiKey 0, 52 wk). DigiKey lists SML-P12MTT86R as yellow-green 572 nm, not red: confirm the colour. The 11-10 md suggestion SML-P12MTT86 (no R) is a different part: DigiKey lists it green, Not For New Designs, and Mouser says the factory is not accepting orders, so do not use it. [short by 5 vs demand 5]
- C43 (MISSING): Only 2 ordered (BB note; cart file had 5). Need 5. DigiKey 892 in stock, Mouser 0. On-hand MSASJ32MAB5227MPNDT1 is 1210, not a drop-in for the 1206 pad. [short by 3 vs pool/line demand 5]
- J1 (MISSING): HRO TYPE-C-31-M-12 is not at DigiKey/Mouser (LCSC C165948 only) and no HRO order is recorded. BB override buys JAE DX07S016JA3R1500 (24 pos = 16 + 8 dummy shell, right angle SMD + THT) x2 only; footprint not compared with the EasyEDA HRO pattern. The 11-10 plan suggested GCT USB4105-GF-A (study says it fits the feather footprint) but it was not ordered. Pool need: feather 5 + gateway 5. [short by 8 vs pool/line demand 10]
- R19 (MISSING): R19 is 100k 0.1% since 2026-11-11. Nothing bought or on hand: the 11-10 plan and carts only have the 10k RT0402BRD0710KL. DigiKey 70,116 at $0.12. [short by 5 vs pool/line demand 5]
- C40 (CHECK): Mouser 41073583 x5 exact part but Mouser stock is 0 today (was 0 on 11-10 too), so the line is probably backordered: confirm ship date. DigiKey now has 7,009 ($0.19) as a fallback. Do not use on-hand C0603C226M9PACTU (6.3 V).
- J3 (CHECK): Not ordered. On hand 6 x FTSH-105-01-L-DV-K-A (suffix -A is an option variant: check the Samtec drawing for alignment-pin holes the footprint may lack). Plain part: DigiKey 98,306 at $1.37, Mouser 87,981 at $1.19.
- R11 (CHECK): FM8625H is not at DigiKey/Mouser. BB alternate Infineon BGS12P2L6E6327XTSA1 (on hand 5; BB also records 7 received), SPDT 50 MHz-6 GHz, 1.65-3.4 V, PG-TSLP-6-4 (same 1.1 x 0.7 mm 6-pad class as the DFN-6 footprint). Pinout and control logic vs FM8625H and pad fit are not verified. 11-10 plan alternate ASWD-S2-0002-T not bought.
- RF1 (CHECK): ECT818000500 not at DigiKey/Mouser. BB alternate RECE.20449.001E.01 (MHF4-compatible receptacle, DigiKey lists Taoglas; DigiKey x3 + on hand 4). Whether it fits the ECT818000500 footprint is unconfirmed (11-10 order md says the same). The 2026-10-28 sourcing BOM lists U.FL-R-SMT-1(10) for RF1, which is the wrong connector family.
- AE1 (OK): On hand 8 (BB inventory); not bought; sourcing and 11-10 plan both had 7 to buy.
- C1,C10 (OK): Mouser 41073583 x10 exact (+-20%). On hand also KE47D (+-10%, 11 pcs) fits. 11-10 plan swap CC0201MRX5R6BB225 was not bought.
- C12 (OK): On hand 8.
- C13 (OK): On hand 8.
- C16 (OK): On hand 6 exact; shared 10 uF 25 V X5R 0603 pool with the gateway (CL10A106MA8NRNC x24 Mouser, TMK107BBJ106MA-T x5 DigiKey): pool total 35 = demand 35, no spare.
- C19 (OK): Mouser x27 + on hand 13 covers feather, pH, ORP and water level (pool 28 needed).
- C3 (OK): On hand 7 exact. Plan swap GRM188R61H225KE11J not bought.
- C41,C54 (OK): DigiKey x15 + on hand 9 (J packaging, same part); shared with water level C5.
- C42 (OK): Mouser x5 exact; on hand 9 of ME01D (current code of the same 47 uF 6.3 V X5R 0603).
- C44 (OK): Mouser x5 exact.
- C45,C48 (OK): DigiKey x100 shared by feather, gateway, pH, ORP (pool demand 82).
- C46 (OK): Mouser x5 exact (16 V).
- C47 (OK): Mouser x5 exact.
- C49,C50 (OK): DigiKey x10 exact.
- C5 (OK): On hand 8.
- C51 (OK): DigiKey x5 exact (25 V).
- C6,C14,C15,C26 (OK): Ordered GRM188R72A104KA35D (Mouser x24) + on hand 21: 0.1 uF X7R 10% 0603 at 100 V instead of 50 V, same dielectric/tolerance/size: verified drop-in (BB override CC0603KRX7R9BB104 -> GRM188R72A104KA35D is correct).
- C7,C17,C18,C20,C22 (OK): Mouser x35 exact (covers feather 25 + ORP 10 with no spare). On hand GRM21BR61E106KA73K (+-10% X5R 25 V 0805, 1000 pcs) is a better-tolerance drop-in spare.
- C8 (OK): On hand 8.
- C9 (OK): DigiKey x2 + on hand 8; shared with ORP C10.
- CN1 (OK): DigiKey x25 shared by feather 5, water level 3, pH 2, ORP 5 = 15 needed. Schematic MPN 503480-1400 = DigiKey MPN 5034801400 (same Molex part, only the dash differs).
- D1,D2 (OK): DigiKey x10 exact.
- D3 (OK): DigiKey x10, need 5.
- F1 (OK): DigiKey x5 exact.
- IC1 (OK): Mouser x1 + on hand 4 = 5.
- L11 (OK): DigiKey x5 exact Murata DFE252010F; footprint is the Sunlord SWPA252010S pattern, same 2.5 x 2.0 mm body, pads not overlaid.
- L2,L5 (OK): DigiKey x10 exact.
- L3 (OK): DigiKey x5 exact HQ part bought "in place of" the BB override LQP03TQ3N9B02D (on hand 8, TQ = different Q series; remove that override or mark it RF-unsafe).
- L4 (OK): DigiKey x5 exact.
- L6,L8 (OK): DigiKey x2 + on hand 8 = 10.
- L7 (OK): DigiKey x5 exact (on-hand LQM18PH4R7MFRL is a different series).
- L9,L10 (OK): Mouser x10 exact; L9 carries no current (BUCK1 off).
- R10 (OK): DigiKey x10 exact; on hand 48 AF0603FR-07150KL (same 150k 1% 0603, automotive/anti-sulfur).
- R12,R13,R15,R16 (OK): DigiKey x10 + on hand 39; shared with pH and ORP. R15-R18 only fitted on the Standard build (2 of 5 feathers) so real need is lower.
- R14 (OK): On hand 23.
- R17,R18 (OK): On hand 47 (10k 0.1% 0402). R15-R18 not fitted on Radar builds.
- R8 (OK): DigiKey x5 exact.
- R9 (OK): DigiKey x25 but only 5 needed (20 extra; the line was bought for the price break).
- SW1 (OK): DigiKey x5 exact.
- U2 (OK): On hand 7 (nPM1300-QEAA-R7).
- U4,U5 (OK): Mouser x6 + on hand 4 S2B-PH-K-S (same part without the lead-free suffix) = 10.
- U6 (OK): DigiKey x2 + on hand 3 (R7 = reel code of the same device) = 5, no spare.
- U7 (OK): DigiKey x5 exact.
- X1 (OK): DigiKey x5 exact. X1 ESR/C0 check still open per STATUS.

## BOM Builder needs file vs schematic

MPNs match the schematic for every ref in the needs file.
BB needs file board_count is 5 for this board.

Write-back proposal: `feather_writeback.csv`.
