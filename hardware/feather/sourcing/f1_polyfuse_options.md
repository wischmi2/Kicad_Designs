# F1 polyfuse options (nRF54L15 feather main board)

Date: 2026-10-28. Sourcing study only; no KiCad files were edited or saved.
Board: C:\Personal-Agents\worktrees\nrf54l15-feather-branch\nrf54l15_feather (run 5 stage 3 state).

## Requirement (from STATUS.md)
- Series VBAT -> F1 -> VBAT_CN1 -> CN1.13. 1S LiPo, 4.2 V max. Load 70 mA worst, 8 mA average.
- Itrip <= ~0.5 A (CN1 contact rating 500 mA), Ihold >= ~0.1 A at 60 C, Vmax >= 6 V, low series R (about 3.3 V must stay downstream).
- Today: Bourns MF-FSMF020X-2, 0603, C210356 (Vmax 9 V, Ihold 0.20 A, Itrip 0.50 A, Rmin 0.55 ohm, R1max 3.5 ohm; Ihold 0.12 A at 60 C per the Bourns table quoted in STATUS.md).

## How the data was obtained
- The kicad MCP JLCPCB database is empty and the jlcsearch tools return fuzzy results, so the JLCPCB parts search API (jlcpcb.com selectSmtComponentList / getComponentDetail) was queried directly on 2026-10-28. Stock, price (qty 1) and the parameters below are the JLCPCB catalogue attributes of that date.
- Datasheets could NOT be read: LCSC, Littelfuse, Bourns and Mouser returned 403 or an HTML bot page, and Digi-Key credentials are not configured. So no datasheet table rows are quoted, and temperature derating is assumed (see "Verified / assumed").

## Candidates (0402; no 0201 resettable fuse exists in the JLCPCB catalogue; searched 0201 and 01005)
All are extended parts ("expand"), same as the current F1, so no new setup-fee class. All 0402 parts: Vmax 6 V, Imax 40-50 A, hold 0.2 A / trip 0.5 A unless noted.

| Part | Maker | LCSC | Ihold / Itrip | Vmax | Rmin | R1max (post-trip) | L x W x H (catalogue) | Stock | Price @1 | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| 0402L020SL6SR | LUTE | C18198352 | 0.20 / 0.50 A | 6 V | 0.10 ohm (description) but detail page says Ri min 500 mohm: conflict | 1.25 ohm | 1.15 x 0.65 x 0.6 mm | 18,265 | $0.0972 | Top pick: cheapest with deep stock. Littelfuse-style part number, not Littelfuse. |
| 0402L020/6SR | LUTE | C53280164 | not listed | 6 V (from name) | not listed | not listed | not listed | 26,666 | $0.0703 | Parameters absent in catalogue; assumed same family. Needs datasheet before use. |
| SMD0402P020SLR | Polytronics (PTTC) | C523822 | 0.20 / 0.50 A | 6 V | 0.10 ohm | 1.25 ohm | 1.15 x 0.65 x 0.6 mm | 946 | $0.3347 | Brand-name, lower stock. |
| BSMD0402L-020 | BHFUSE | C914085 | 0.20 / 0.50 A | 6 V | 0.10 ohm | 1.25 ohm | 1.15 x 0.65 x 0.6 mm | 2,669 | $0.2362 | |
| 0402L020SLKR | Littelfuse | C157518 | 0.20 / 0.50 A | 6 V | 0.10 ohm | n/a | n/a | 17 | $3.4555 | Genuine part but 17 in stock and priced high; not usable for a batch. |
| ASMD0402SL020-6V | Shenzhen JDT | C55372428 | not listed (name says 0.20 A, 6 V) | 6 V | n/a | n/a | n/a | 10,000 | $0.1589 | Parameters absent in catalogue. |
| MF-ASML020/6-2 | Bourns | C1854972 | not listed for hold/trip | 6 V (name) | 0.10 ohm | 1.6 ohm | n/a | 252 | $2.1421 | Only Bourns 0402 near this spec; price/stock poor. |

Rejected 0402 values:
- 0402L010 / SMD0402P010 / BSMD0402L-010 family (Ihold 0.10 A, Itrip 0.30 A, Rmin 0.15 ohm, R1max 2-2.8 ohm): after derating at 60 C Ihold falls to roughly 0.06-0.07 A, which is below the 70 mA worst case. Would nuisance-trip in the VBAT-fed isolated-supply option. Fine only if the load stays at the 8 mA water-level figure.
- 0402L035 family (Itrip 0.70 A): above the 500 mA contact rating.
- 0402L005/ 0402L008 etc: Ihold too low.

Voltage drop at 70 mA, using the listed resistances:
- 0402L020 (Rmin 0.10 ohm, R1max 1.25 ohm): 7 mV to 88 mV (R1max is the worst case after a trip event; the initial maximum resistance is not in the catalogue, so the in-service worst case is unverified, assumed well under R1max).
- Current 0603 FSMF020X (Rmin 0.55, R1max 3.5): 39 mV to 245 mV. The 0402 is better on every figure.

## Does the 0402 footprint fit a site? (KiCad Python, read-only, board not saved)
Method: KiCad Fuse_0402_1005Metric (pads 0.59 x 0.64 mm at +-0.485 mm, courtyard 1.95 x 1.03 mm) placed on a 0.1 mm grid within 7 mm of CN1.13 (137.15, 118.68), rotations 0 and 90, F.Cu. Checks: pads clear of all other-net F.Cu copper by 0.15 mm, courtyard clear of all footprint courtyards, inside the board outline, outside AE1_keepout. Zone fills were not checked. Routing was tested only as a straight 0.15 mm segment.

Result:
- Old 0603 site problem confirmed: the 3.05 x 1.55 courtyard does not fit. With the 0402 the courtyard shrinks to 1.95 x 1.03 and 532 grid positions pass the pad and courtyard checks.
- Nearest legal site: (135.85, 117.68) rotation 90, which is inside the old C9 site (x 134.5-136.3, y 117.8-119.4), 1.64 mm from CN1.13. Pads 0.59 x 0.64 mm: pad centres at y 117.195 and 118.165. Other legal rot-0 positions exist at (137.25..., 116.18) just north of CN1, but CN1.13 is flanked by GND pins 12 and 14 so it cannot be reached from the north.
- The remaining blocker is the route, not the footprint: pad 13 can only be entered from the west (pins 12 and 14 are GND, the east side is under the connector body, courtyard x 136.455-140.795). That west lane at y 118.68 is crossed by the SENS_SDA F.Cu track at x 136.46 (y 117.39 to 119.05, 0.2 mm). Straight route F1.2 -> CN1.13 hits SENS_SDA and GND pad 14/12 clearances in the test. So F1 at C9's old site fits, but needs either SENS_SDA moved off F.Cu around y 118.68 (SDA already has a via at (136.85, 117.0) and a B.Cu run, so a shorter F.Cu piece with an earlier via is plausible; not designed or checked), or a hop under SDA.
- Sites east of CN1.13 (x 139.0-139.5, y 118.1-118.4) have clear pads and a clear straight route if the VBAT via at (138.8, 118.68) is removed, but they sit inside the CN1 courtyard (the connector body), so they are not usable unless the connector clearance is confirmed. Not recommended.
- No site found that is clean on pads, courtyard and route without touching SENS_SDA or CN1's courtyard.

## Other options (cost only; not designed)
(b) Keep the 0603 at the nPM1300 end of the VBAT branch: part cost unchanged (C210356, $0.0518 @1, 17,839 in stock). Cost is layout: STATUS.md says In2 is full there, so the branch must be rebuilt, and the VBAT_CN1 net then runs the whole branch length to CN1.13. A 0402 would also fit there more easily. Fuse protects the whole branch, which is the better fault coverage.
(c) No fuse on the host, fuse on each sensor board: host gets VBAT straight to CN1.13 (drop 0 mV, F1 deleted, kicad-designer swaps to a link or removes it). Cost: one 0402 0.2 A fuse per sensor board at about $0.07-0.10 (extended part; setup fee only once per type per order) on 6 boards (template, sens1, water level, ORP, DO, EC) plus a footprint and route on each; the FFC and CN1 contacts have no protection on the host side, and a board without the fuse becomes unprotected. Can reuse the same C18198352 part.

## Recommendation
Replace F1 with LUTE 0402L020SL6SR, LCSC C18198352 (0402, 0.6 mm high, 18,265 in stock on 2026-10-28, $0.0972 @1, extended): Ihold 0.20 A, Itrip 0.50 A, Vmax 6 V, Rmin 0.10 ohm, R1max 1.25 ohm. Same hold/trip as the current 0603, lower resistance, 6 V rating is 1.43x the 4.2 V cell. Use the KiCad Fuse_0402_1005Metric footprint at about (135.85, 117.68) rot 90 (old C9 site) and have kicad-designer move the SENS_SDA F.Cu piece near x 136.46 so pad 2 can reach CN1.13 from the west. Fallback if SDA cannot move: option (b) with the same 0402.
Second source with brand and datasheet: Polytronics SMD0402P020SLR C523822 (946 in stock, $0.3347), or BHFUSE BSMD0402L-020 C914085 (2,669, $0.2362).

## Verified and assumed
Verified 2026-10-28 (JLCPCB catalogue attributes): existence, package 0402, extended/basic class, stock, qty-1 price, Ihold/Itrip/Vmax/R1max/height values listed in the table, no 0201 resettable fuse listed.
Verified from KiCad Python: footprint pad/courtyard geometry, site search results, the SENS_SDA track coordinates, CN1 pad coordinates and courtyard.
Not verified (no datasheet access):
- Temperature derating of the 0402L020 family. Assumed to be similar to the Bourns 0603 table (about 0.6 x Ihold at 60 C, so about 0.12 A, giving about 1.7x margin over 70 mA). Check against the LUTE datasheet (https://wmsc.lcsc.com/wmsc/upload/file/pdf/v2/lcsc/2403051430_LUTE-0402L020SL6SR_C18198352.pdf) before ordering.
- Rmin for C18198352 (listing shows both 100 mohm and 500 mohm); initial maximum resistance; Itrip rise at low temperature; trip time; 0402 land pattern recommendation.
- Whether the LUTE part is an acceptable substitute for a Littelfuse-compatible footprint (assumed, size is the standard 0402).
- Quantity pricing tiers and order quantity; cost totals were not computed (one F1 per board at about $0.10).
- Routing of the F1 pads and the SDA move; zone fills.
