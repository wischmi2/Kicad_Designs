# hardware_callouts

Base pictures and label JSON for "where each piece of hardware goes" figures (Crown assembly guide). Same JSON format as ..\callouts\*.json, plus `arrow_to: [x, y]` on each hardware label (the pixel of the hole it goes into).

Pictures: 2400 x 1500, true isometric (Fusion iso-top-right or iso-bottom-right, orthographic), **transparent background** (RGBA PNG): composite on white before labelling. Pixel positions were computed from the exact camera projection (image centre = centre of the visible geometry) and each was checked against the holes and pieces in the saved image. Brass = F1/F3/F8 inserts, silver = F2 stainless (looks dark grey from below), off-white = nylon.

Projection used (for adding more points): px = 1200 + S*(dx - dy)/sqrt2 ; top iso: py = 750 - S*(-dx - dy + 2dz)/sqrt6 ; bottom iso: py = 750 - S*(dx + dy + 2dz)/sqrt6 ; (dx,dy,dz) = world point minus the centre of the visible bounding box, S about 11-16 px/mm (differs per picture).

Model state: the hardware bodies were moved/hidden only temporarily in Fusion; the Move features were deleted, visibility and colours were reset.

Not made: hw_08_a6_ears, hw_09_a2_clips, hw_10_a5_squeeze. The Fusion model has no F10-F14 hardware (no M4/M3 screws or nuts); the Hardware_Ref component only holds F1-F7. Ear, clip and squeeze holes exist in the plates.

STATUS
- hw_02_hood_roof_inserts: done (png + json)
- hw_06_bonnet_screws: done (png + json)
- hw_05_hood_corner_screws: done (png + json)
- hw_01_hood_plinth_inserts: done (png + json)
- hw_04_board_stack: done (png + json)
- hw_03_dock_ring_inserts: done (png + json)
- hw_07_dock_plate_screws: done (png + json)
- hw_08, hw_09, hw_10: skipped (hardware not in the model)
