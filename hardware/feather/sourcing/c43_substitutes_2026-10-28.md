# C43 (220 uF 6.3 V 1206): what it does and what to buy (checked 2026-10-28)

## What C43 is
- Net: C43.1 is VBAT, C43.2 is GND (power_supply sheet). VBAT also carries the battery connector U4, nPM1300 U2.19 (VBAT), AEM10330 IC1.19 (STO) and C3 (2.2 uF 50 V).
- It is the AEM10330 storage-element capacitor CSTO. The AEM10330 datasheet (DS-AEM10330 v1.5, section 6.1, 6.9.1 and Table 7) says: if the battery can be disconnected (user-removable connector, which U4 is), the board must have at least 100 uF on STO, and running "without this 100 uF minimum capacitance on STO will permanently damage the circuit". Table 7 footnote: consider tolerance and DC-bias derating.
- Operating voltage: STO_CFG is LLLL, so the Li-Po profile (VOVDIS 3.00 V, VCHRDY 3.50 V, VOVCH 4.05 V). The nPM1300 charger can take the pack to about 4.2 V, so size the cap for 4.2 V DC bias.
- So the requirement is at least 100 uF effective at about 4.2 V, over temperature, with +-20 % tolerance. The part rating 6.3 V is 67 % utilised.
- Leakage on STO adds to the quiescent current (datasheet 6.9.1), so ceramic is preferred over tantalum.

## Stock facts (DigiKey Product API v4 and Mouser Search API, 2026-10-28, USD, cut tape)
The earlier live BOM said the Taiyo original was gone. That was wrong: the DigiKey API puts the stock in different fields for different parts and the Taiyo part was missed.

| Option | MPN | Case / rating | DigiKey | Mouser | Pad change |
|---|---|---|---|---|---|
| Original (schematic MPN) | MSASJ31LBB5227MTCA01 (Taiyo) | 1206, 220 uF 6.3 V X5R | 1,556 in stock, 587-MSASJ31LBB5227MTCA01CT-ND, 5.42 (1), 3.91 (10) | 85 in stock, 963-MSASJ31LBB5227MT, 8.61 | none |
| 1210 swap | GRM32ER60J227ME05L (Murata) | 1210, 220 uF 6.3 V X5R | 102,936, 490-16308-1-ND, 1.57 | 979, 81-GRM32ER60J227ME5L, 1.66 | see below |
| 1210 swap | CL32A227MQVNNNE (Samsung) | 1210, 220 uF 6.3 V X5R | 86,210, 1276-3375-1-ND, 2.46 | 13,522, 187-CL32A227MQVNNNE, 4.12 | see below |
| 1210 swap (X6S) | GRM32EC80J227ME01L (Murata) | 1210, 220 uF 6.3 V X6S | 0 | 5,275, 81-GRM32EC80J227ME1L, 3.49 | see below |
| Not enough C | GRM31CR61A107MEA8L (Murata) | 1206, 100 uF 10 V X5R | 254,919, 490-GRM31CR61A107MEA8LCT-ND, 0.52 | 28,339, 0.93 | none |
| Not enough C | C3216X5R0J107M160AB (TDK) | 1206, 100 uF 6.3 V X5R | 6,915, 445-6008-1-ND, 1.11 | 35,732, 1.11 | none |
| Not enough C | CL31A107MQHNNNE (Samsung) | 1206, 100 uF 6.3 V X5R | 0 | 883, 1.41 | none |
| Murata original MPN | GRM31CR60J227ME11L / -K | 1206, 220 uF | 0 | on order only (967,655 incoming) | none |
| Polymer tantalum | T520B227M006ATE045 (KEMET) | 3528-21, 220 uF 6.3 V | 101,454, 1.43 | not checked | large (3.5 x 2.8 mm body) |

## Pad change, 1206 to 1210 (KiCad stock footprints C_1206_3216Metric and C_1210_3225Metric)
C43 is at (109.0, 119.71) rotated 90 degrees. Pad centres are the same (+-1.475 mm), pad width is the same (1.15 mm). Pad length goes from 1.8 to 2.7 mm (0.45 mm longer on each side of the part axis, so on the board that is +-0.45 mm in X), courtyard grows by 0.45 mm each side. Body is 3.2 x 2.5 mm instead of 3.2 x 1.6 mm. I did not check neighbouring copper because the PCB is being edited by another agent; the board owner needs to check the 0.45 mm growth against C41/C42 and the VBAT/GND vias near (109, 119.7).

## Derated capacitance
I could not get a vendor DC-bias curve (Murata and Samsung sites return 403 or HTML from here; the Taiyo and Samsung spec PDFs have no bias graph). So there is no verified derated figure. Rule of thumb for large-value X5R/X6S at about 65 % of rated voltage is a loss of 40 to 70 percent, which means:
- 1206 100 uF parts (any voltage rating up to 10 V): well under 100 uF effective at 4.2 V. Two of them in parallel also fall short, and need a second pair of pads, so do not use them.
- 220 uF parts (1206 or 1210): around the 100 uF limit, possibly a little under at 4.2 V and cold. This is true of the original design too.
Check the real figure with Murata SimSurfing or the Samsung/Taiyo web tools before you commit. Also consider the battery is normally connected; the 100 uF rule matters when the battery is unplugged and the harvester runs alone.

## Recommendation
1. Buy the exact specified part MSASJ31LBB5227MTCA01 from DigiKey (1,556 in stock, 587-MSASJ31LBB5227MTCA01CT-ND, 5.42 USD one-off). Footprint unchanged, so no board change, and it is the part the design assumed. Expensive, but it is one part per board.
2. If you accept a footprint change to save money and gain margin: Murata GRM32ER60J227ME05L, 1210, 220 uF 6.3 V (DigiKey 490-16308-1-ND, 102,936 in stock, 1.57 USD). Same pad centres, pads 0.9 mm longer. Same capacitance and voltage as the original, so the bias loss is similar; it does not add margin by itself.
3. If the real bias figure at 4.2 V comes out under 100 uF effective, the ceramic route needs a bigger capacitor or a different technology. The fallback is a polymer tantalum, KEMET T520B227M006ATE045 (3528-21, 101,454 at DigiKey, 1.43 USD), which keeps its value with voltage but has a leakage spec of up to about 0.1 CV (about 140 uA worst case), too high for a harvester board; ask Brian first.
Do not use the 100 uF 1206 parts.

Field change for kicad-designer (not applied by me): C43 MPN stays MSASJ31LBB5227MTCA01; add DigiKey PN 587-MSASJ31LBB5227MTCA01CT-ND.
