# hardware_callouts

Base pictures and label JSON for "where each piece of hardware goes" figures (Crown assembly guide). Same JSON format as ..\callouts\*.json, plus `arrow_to: [x, y]` on each hardware label (the pixel of the hole it goes into).

Pictures: 2400 x 1500, true isometric (Fusion iso-top-right or iso-bottom-right, orthographic), **transparent background** (RGBA PNG): composite on white before labelling. Pixel positions were computed from the exact camera projection (image centre = centre of the visible geometry) and each was checked against the holes and pieces in the saved image. Brass = F1/F3/F8 inserts, silver = F2 stainless, off-white = nylon.

Model state: the hardware bodies were moved/hidden only temporarily in Fusion; the Move features were deleted afterwards.

STATUS
- hw_02_hood_roof_inserts: done (png + json)
- hw_06_bonnet_screws: done (png + json)
- hw_05_hood_corner_screws: done (png + json)
