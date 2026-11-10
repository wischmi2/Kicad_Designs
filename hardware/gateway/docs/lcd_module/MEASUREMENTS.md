# Waveshare 2inch LCD Module (SKU 17344): dimensions

Source: Waveshare's own STEP model, `2inch_LCD_Module_3D_Drawing.stp` (Creo, 2023-06-07), downloaded 2026-10-24 from
https://files.waveshare.com/wiki/2inch_LCD_Module/2inch_LCD_Module_3D_Drawing.zip.
The 2D drawing PDF from the wiki is saved next to it. Values were read from the STEP vertex geometry, not measured on a real module.

Coordinates below are from the module's PCB edges, looking at the screen, with the long axis horizontal.
"Connector end" is the short edge nearest the PH connector; "FPC end" is the other short edge, where the panel's flex cable wraps round.

| Item | Value |
| --- | --- |
| Module PCB | 58.0 x 35.0 x 1.6 mm |
| M2 holes | 2.5 mm in from every edge (53.0 x 30.0 pattern) |
| Panel (base) | 47.83 x 34.6 mm, from 4.92 mm (FPC end) to 5.09 mm (connector end), 0.2 mm from top/bottom edges |
| Cover glass (top) | 46.6 x 33.6 mm, from 6.01 mm (FPC end) to 5.39 mm (connector end), 0.7 mm from top/bottom |
| **Active area** | **40.8 x 30.6 mm, 10.31 mm from the FPC end, 6.89 mm from the connector end, 2.2 mm from top and bottom.** Its centre is 1.71 mm off the board centre, towards the connector end, and centred vertically |
| Height above the PCB top | 2.40 mm (glass top) |
| **Total thickness (PCB back to glass top)** | **4.0 mm** |
| Panel flex at the FPC end | Wraps round the short end, 20 mm wide (centred), sticks out 0.5 mm past the panel |
| PH2.0 8-pin connector (SMT, side entry) | On the **back** of the PCB, centred vertically, spanning 19.9 mm. Body is 8.5 mm long, from 4.25 to 12.75 mm in from the connector end. **5.6 mm tall** below the PCB back. The cable is expected to leave towards the connector-end edge; check in the 3D model |
| Hex standoffs (in the model) | M2 x 6 mm below the PCB, with M2 x 5 screws from the front. Screw heads are 3.5 mm in diameter and about 1 mm above the PCB top, outside the glass |

Window (concepts.md section 2.3): active area + 0.6 mm each side = 42.0 x 31.8 mm, centred on the active area (that is, 1.71 mm off the module centre, towards the connector end).
