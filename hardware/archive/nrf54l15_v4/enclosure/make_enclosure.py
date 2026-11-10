"""Two-piece enclosure for the nRF54L15 v4 board, with a 1.14 inch color LCD.

Confirmed display
-----------------
1.14 inch IPS, ST7789, 240 x 135. A typical SPI breakout is 28.0 x 31.4 x 3.1 mm
(active area 14.86 x 24.91 mm). The lid pocket is 28.6 x 40.0 mm so that module
sits in a recessed bezel and a short FPC can fold down inside the lid.

The current v4 PCB cannot drive the panel. CN1 is I2C only (GND, VDDIO, SDA, SCL).
A later respin adds one 8-pin header on the component side, left of the antenna:

    1 VDDIO   3.3 V
    2 GND
    3 SCK     P2.01
    4 MOSI    P2.02
    5 CS      P2.05
    6 DC      P2.00
    7 RST     P2.03
    8 BL      P2.06

P2.00-P2.10 are unconnected on the present board. The sensor port stays I2C-only.

Shell
-----
X runs from the USB edge to the antenna edge. Y runs from the solar edge to the
sensor edge. Z is up. The board outline in KiCad is 44.38 x 34.00 mm; connector
centers below are in that frame (origin at the board's minimum X/Y corner).

The battery bay and the screw gutters make the shell 62 x 72 x 16 mm. The right
10 mm of the board is an antenna keepout: no screws, no battery foil, and no
display ground there.
"""

from __future__ import annotations

import math
from pathlib import Path

import trimesh
from shapely.geometry import Polygon

OUT_DIR = Path(__file__).resolve().parent / "stl"

# --- confirmed 1.14 in SPI TFT ------------------------------------------------
DISPLAY_NAME = "1.14in IPS ST7789 240x135"
MODULE_X = 28.0
MODULE_Y = 31.4
MODULE_T = 3.1
ACTIVE_X = 14.864
ACTIVE_Y = 24.912
# Pocket is the module plus a cradle margin and the FPC fold (about 28 x 40).
POCKET_X = 32.4
POCKET_Y = 40.0
MODULE_INSET = 2.2
WINDOW_X = 14.2
WINDOW_Y = 24.0
BEZEL = 1.0
WINDOW_T = 0.8

# Later v4 respin. Pins are free today (unconnected on U6).
DISPLAY_HEADER = (
    (1, "VDDIO", "3V3"),
    (2, "GND", "GND"),
    (3, "SCK", "P2.01"),
    (4, "MOSI", "P2.02"),
    (5, "CS", "P2.05"),
    (6, "DC", "P2.00"),
    (7, "RST", "P2.03"),
    (8, "BL", "P2.06"),
)
FREE_P2 = {f"P2.{i:02d}" for i in range(11)}

# --- board, from nrf54l15_v4.kicad_pcb Edge.Cuts and connector origins -------
BOARD_W = 44.38
BOARD_D = 34.00
BOARD_T = 1.6
# (dx, dy) from the board's min corner. KiCad +Y is the sensor edge.
USB_DX, USB_DY = 5.30, 6.78
USB_FACE_INSET = 3.04  # mating face is this far in from the USB edge
SOLAR_DX, SOLAR_DY = 17.10, 6.56
SENSOR_DX = 14.48
SWD_DX, SWD_DY = 33.45, 28.88
ANTENNA_KEEPOUT = 10.0

# --- shell -------------------------------------------------------------------
WALL = 1.8
FLOOR_T = 1.6
LID_SKIN = 1.6
OUTER_X = 62.0
OUTER_Y = 72.0
OUTER_Z = 16.0
CORNER_R = 4.0
BASE_TOP = 10.2
SKIRT_DROP = 2.0
LIP_PLAY = 0.4
SKIRT_T = 1.2
BOSS_H = 3.0
BOSS_D = 4.5

LEFT_GUTTER = 8.4
FRONT_GUTTER = 9.5
BOARD_X0 = WALL + LEFT_GUTTER  # 10.2
BOARD_Y0 = WALL + FRONT_GUTTER  # 11.3

BAT_L, BAT_W, BAT_T = 30.0, 20.0, 6.0
BAT_X0 = BOARD_X0
BAT_Y0 = BOARD_Y0 + BOARD_D + 1.5

POST_R = 2.8
# 5.6 mm posts, 3.1 mm holes: enough wall for an M2 insert. All four stay
# left of the antenna keepout. Two are inset along the solar edge; the
# fourth sits in the USB-side gutter beside the battery bay.
SCREWS = (
    (6.6, 6.4),
    (19.0, 6.4),
    (35.5, 6.4),
    (6.6, 52.0),
)

POCKET_X0 = 6.2
POCKET_Y0 = 16.0

ENGINE = "manifold"


def confirm_display() -> None:
    """Lock the display choice and the future header pinout."""
    if len(DISPLAY_HEADER) != 8:
        raise SystemExit("display header must be 8 pins")
    if DISPLAY_HEADER[0][1] != "VDDIO" or DISPLAY_HEADER[1][1] != "GND":
        raise SystemExit("header must start with VDDIO, GND")
    used = [pin for _n, name, pin in DISPLAY_HEADER if pin.startswith("P")]
    if len(used) != 6 or len(set(used)) != 6:
        raise SystemExit("SPI header needs 6 distinct GPIO pins")
    unknown = [pin for pin in used if pin not in FREE_P2]
    if unknown:
        raise SystemExit(f"header uses pins that are not free P2 GPIO: {unknown}")
    names = [name for _n, name, _pin in DISPLAY_HEADER]
    for required in ("SCK", "MOSI", "CS", "DC", "RST", "BL"):
        if required not in names:
            raise SystemExit(f"header missing {required}")
    if MODULE_X > 30 or MODULE_Y > 36 or MODULE_T > 4:
        raise SystemExit("module is larger than the 1.14 in class this shell targets")
    if POCKET_X < MODULE_X + 2 * MODULE_INSET - 0.05:
        raise SystemExit("pocket must cradle the module, not pinch it")
    if POCKET_Y < 40.0:
        raise SystemExit("pocket must be the plan's 40 mm FPC length")


def antenna_keepout_x() -> float:
    return BOARD_X0 + BOARD_W - ANTENNA_KEEPOUT


def check_layout() -> None:
    keep = antenna_keepout_x()
    inner_x1 = OUTER_X - WALL
    inner_y1 = OUTER_Y - WALL

    if BOARD_X0 + BOARD_W > inner_x1 - 0.8:
        raise SystemExit("board does not clear the antenna-side wall")
    if BOARD_Y0 + BOARD_D > BAT_Y0 - 1.0:
        raise SystemExit("board runs into the battery bay")
    if BAT_X0 + BAT_L > keep - 1.0:
        raise SystemExit("battery foil enters the antenna keepout")
    if BAT_Y0 + BAT_W > inner_y1 - 1.0:
        raise SystemExit("battery does not fit before the sensor wall")

    pocket_x1 = POCKET_X0 + POCKET_X
    if pocket_x1 > keep - 1.0:
        raise SystemExit("display pocket enters the antenna keepout")
    if pocket_x1 > OUTER_X - 3.4 or POCKET_Y0 + POCKET_Y > OUTER_Y - 3.4:
        raise SystemExit("display pocket does not fit inside the lid")

    for x, y in SCREWS:
        if x + POST_R > keep:
            raise SystemExit(f"screw at ({x}, {y}) enters the antenna keepout")
        if x - POST_R < WALL or y - POST_R < WALL:
            raise SystemExit(f"screw at ({x}, {y}) breaks the outer wall")
        if y + POST_R > BOARD_Y0 and x + POST_R > BOARD_X0 and x - POST_R < BOARD_X0 + BOARD_W:
            # Posts may sit beside the board in the left gutter, not under it.
            if x + POST_R > BOARD_X0 and y - POST_R < BOARD_Y0 + BOARD_D:
                raise SystemExit(f"screw at ({x}, {y}) collides with the board")

    usb_y = BOARD_Y0 + USB_DY
    if not (WALL < usb_y < BOARD_Y0 + BOARD_D):
        raise SystemExit("USB slot is not on the board's USB edge")
    if BOARD_X0 + USB_FACE_INSET > 20:
        raise SystemExit("USB mating face is too far from the left wall")


def rounded_rect(w: float, h: float, r: float) -> Polygon:
    r = min(r, w / 2 - 0.01, h / 2 - 0.01)
    specs = (
        (w - r, r, -math.pi / 2),
        (w - r, h - r, 0.0),
        (r, h - r, math.pi / 2),
        (r, r, math.pi),
    )
    pts: list[tuple[float, float]] = []
    steps = 10
    for cx, cy, a0 in specs:
        for i in range(steps):
            a = a0 + i * (math.pi / 2) / steps
            pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    poly = Polygon(pts)
    if not poly.is_valid:
        poly = poly.buffer(0)
    return poly


def shift(mesh: trimesh.Trimesh, x: float, y: float, z: float = 0.0) -> trimesh.Trimesh:
    mesh.apply_translation((x, y, z))
    return mesh


def extrude(poly: Polygon, z0: float, z1: float) -> trimesh.Trimesh:
    mesh = trimesh.creation.extrude_polygon(poly, height=z1 - z0)
    return shift(mesh, 0.0, 0.0, z0)


def rr(x: float, y: float, w: float, h: float, r: float, z0: float, z1: float) -> trimesh.Trimesh:
    return shift(extrude(rounded_rect(w, h, r), z0, z1), x, y)


def cub(x0: float, y0: float, z0: float, x1: float, y1: float, z1: float) -> trimesh.Trimesh:
    extents = (x1 - x0, y1 - y0, z1 - z0)
    mesh = trimesh.creation.box(extents=extents)
    return shift(mesh, (x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2)


def cyl(x: float, y: float, z0: float, z1: float, radius: float, sections: int = 40) -> trimesh.Trimesh:
    height = z1 - z0
    mesh = trimesh.creation.cylinder(radius=radius, height=height, sections=sections)
    return shift(mesh, x, y, z0 + height / 2)


def fuse(meshes: list[trimesh.Trimesh]) -> trimesh.Trimesh:
    parts = [m for m in meshes if m is not None]
    if len(parts) == 1:
        return parts[0]
    return trimesh.boolean.union(parts, engine=ENGINE)


def cut(body: trimesh.Trimesh, tools: list[trimesh.Trimesh]) -> trimesh.Trimesh:
    tools = [t for t in tools if t is not None]
    if not tools:
        return body
    tool = tools[0] if len(tools) == 1 else trimesh.boolean.union(tools, engine=ENGINE)
    return trimesh.boolean.difference([body, tool], engine=ENGINE)


def finish(mesh: trimesh.Trimesh) -> trimesh.Trimesh:
    mesh.merge_vertices()
    mesh.update_faces(mesh.unique_faces())
    mesh.remove_unreferenced_vertices()
    mesh.fix_normals()
    return mesh


def base_mesh() -> trimesh.Trimesh:
    outer = rr(0, 0, OUTER_X, OUTER_Y, CORNER_R, 0.0, BASE_TOP)
    inner_r = max(0.8, CORNER_R - WALL)
    inner = rr(WALL, WALL, OUTER_X - 2 * WALL, OUTER_Y - 2 * WALL, inner_r, FLOOR_T, BASE_TOP + 0.2)
    shell = cut(outer, [inner])

    bosses = []
    inset = 8.0
    for dx, dy in (
        (inset, inset),
        (BOARD_W - inset, inset),
        (inset, BOARD_D - inset),
        (BOARD_W - inset, BOARD_D - inset),
    ):
        bosses.append(
            cyl(BOARD_X0 + dx, BOARD_Y0 + dy, FLOOR_T, FLOOR_T + BOSS_H, BOSS_D / 2)
        )
    # Three corner lips locate the PCB. The antenna corner is left open.
    lips = []
    lip_t = 1.2
    lip_h = FLOOR_T + BOSS_H
    corners = (
        (BOARD_X0 - lip_t, BOARD_Y0 - lip_t, BOARD_X0 + 3.5, BOARD_Y0),
        (BOARD_X0 - lip_t, BOARD_Y0, BOARD_X0, BOARD_Y0 + 3.5),
        (BOARD_X0 + BOARD_W, BOARD_Y0 - lip_t, BOARD_X0 + BOARD_W + lip_t, BOARD_Y0 + 3.0),
        (BOARD_X0 - lip_t, BOARD_Y0 + BOARD_D, BOARD_X0 + 3.0, BOARD_Y0 + BOARD_D + lip_t),
    )
    for x0, y0, x1, y1 in corners:
        lips.append(cub(x0, y0, FLOOR_T, x1, y1, lip_h))

    # Battery pocket clips along the long sides. A 0.5 mm lip holds a 6 mm cell.
    clip_z1 = FLOOR_T + BAT_T + 0.4
    clips = [
        cub(BAT_X0, BAT_Y0 - 1.2, FLOOR_T, BAT_X0 + BAT_L, BAT_Y0, clip_z1),
        cub(BAT_X0, BAT_Y0 + BAT_W, FLOOR_T, BAT_X0 + BAT_L, BAT_Y0 + BAT_W + 1.2, clip_z1),
        cub(BAT_X0 + 2, BAT_Y0 - 1.2, clip_z1 - 0.6, BAT_X0 + BAT_L - 2, BAT_Y0 + 0.5, clip_z1),
        cub(BAT_X0 + 2, BAT_Y0 + BAT_W - 0.5, clip_z1 - 0.6, BAT_X0 + BAT_L - 2, BAT_Y0 + BAT_W + 1.2, clip_z1),
    ]

    posts = [cyl(x, y, FLOOR_T, BASE_TOP, POST_R) for x, y in SCREWS]
    # Solar-cable strain rib, just inside the front wall, with a wire gap.
    solar_x = BOARD_X0 + SOLAR_DX
    rib = cub(solar_x - 4.5, WALL + 0.4, FLOOR_T + BOSS_H, solar_x + 4.5, WALL + 1.8, BASE_TOP - 0.4)
    rib_gap = cub(solar_x - 1.3, WALL + 0.2, FLOOR_T + BOSS_H + 0.4, solar_x + 1.3, WALL + 2.0, BASE_TOP)

    body = fuse([shell, *bosses, *lips, *clips, *posts, rib])
    body = cut(body, [rib_gap])

    usb_y = BOARD_Y0 + USB_DY
    usb_z0 = FLOOR_T + BOSS_H + BOARD_T - 0.2
    usb = cub(
        -1.0,
        usb_y - 5.1,
        usb_z0,
        BOARD_X0 + USB_FACE_INSET + 0.4,
        usb_y + 5.1,
        usb_z0 + 4.0,
    )
    solar = cub(
        solar_x - 3.0,
        -1.0,
        FLOOR_T + BOSS_H + 0.6,
        solar_x + 3.0,
        WALL + 0.3,
        FLOOR_T + BOSS_H + 0.6 + 3.2,
    )
    sensor_x = BOARD_X0 + SENSOR_DX
    sensor = cub(
        sensor_x - 2.5,
        OUTER_Y - WALL - 0.3,
        8.2,
        sensor_x + 2.5,
        OUTER_Y + 1.0,
        11.2,
    )
    screw_holes = [cyl(x, y, BASE_TOP - 4.2, BASE_TOP + 0.2, 1.55) for x, y in SCREWS]
    # 1.6 mm radius = 3.2 mm hole for an M2 heat-set insert in the top of each post.
    return finish(cut(body, [usb, solar, sensor, *screw_holes]))


def lid_mesh() -> trimesh.Trimesh:
    skirt_z0 = BASE_TOP - SKIRT_DROP
    cap = rr(0, 0, OUTER_X, OUTER_Y, CORNER_R, BASE_TOP, OUTER_Z)
    skirt_inset = WALL + LIP_PLAY
    skirt_r = max(0.6, CORNER_R - skirt_inset)
    skirt = rr(
        skirt_inset,
        skirt_inset,
        OUTER_X - 2 * skirt_inset,
        OUTER_Y - 2 * skirt_inset,
        skirt_r,
        skirt_z0,
        BASE_TOP + 0.05,
    )
    hollow_inset = skirt_inset + SKIRT_T
    hollow_r = max(0.5, CORNER_R - hollow_inset)
    hollow = rr(
        hollow_inset,
        hollow_inset,
        OUTER_X - 2 * hollow_inset,
        OUTER_Y - 2 * hollow_inset,
        hollow_r,
        skirt_z0 - 0.05,
        OUTER_Z - LID_SKIN,
    )
    shell = cut(fuse([cap, skirt]), [hollow])

    pocket_z1 = OUTER_Z - 0.9
    pocket_z0 = pocket_z1 - MODULE_T - 0.2
    pocket = cub(
        POCKET_X0,
        POCKET_Y0,
        pocket_z0,
        POCKET_X0 + POCKET_X,
        POCKET_Y0 + POCKET_Y,
        pocket_z1 + 0.05,
    )
    # Window through the remaining skin, plus a 0.8 mm rebate for the clear plate.
    # The module sits inset in the pocket so the corner posts land beside it.
    mod_x0, mod_y0 = module_origin()
    win_x0 = mod_x0 + (MODULE_X - WINDOW_X) / 2
    win_y0 = mod_y0 + (MODULE_Y - WINDOW_Y) / 2
    window = cub(win_x0, win_y0, pocket_z1 - 0.05, win_x0 + WINDOW_X, win_y0 + WINDOW_Y, OUTER_Z + 0.2)
    rebate = cub(
        win_x0 - BEZEL,
        win_y0 - BEZEL,
        OUTER_Z - WINDOW_T,
        win_x0 + WINDOW_X + BEZEL,
        win_y0 + WINDOW_Y + BEZEL,
        OUTER_Z + 0.2,
    )

    # Posts hang from the lid skin and pinch the module corners.
    mod_x1 = mod_x0 + MODULE_X
    mod_y1 = mod_y0 + MODULE_Y
    posts = [
        cyl(px, py, pocket_z0 + 0.45, OUTER_Z - 1.05, 1.05)
        for px, py in (
            (mod_x0 + 0.15, mod_y0 + 0.15),
            (mod_x1 - 0.15, mod_y0 + 0.15),
            (mod_x0 + 0.15, mod_y1 - 0.15),
            (mod_x1 - 0.15, mod_y1 - 0.15),
        )
    ]

    usb_y = BOARD_Y0 + USB_DY
    usb_z0 = FLOOR_T + BOSS_H + BOARD_T - 0.2
    usb_notch = cub(-1.0, usb_y - 5.1, usb_z0, WALL + LIP_PLAY + SKIRT_T + 0.4, usb_y + 5.1, usb_z0 + 4.0)

    sensor_x = BOARD_X0 + SENSOR_DX
    sensor = cub(sensor_x - 2.5, OUTER_Y - WALL - 1.0, 8.2, sensor_x + 2.5, OUTER_Y + 1.0, 11.2)

    # Lid screw clearance and M2 head counterbore. Heads sit below the outer skin.
    screw_tools = []
    for x, y in SCREWS:
        screw_tools.append(cyl(x, y, skirt_z0 - 0.2, OUTER_Z + 0.2, 1.15))
        screw_tools.append(cyl(x, y, OUTER_Z - 1.6, OUTER_Z + 0.2, 2.1))

    swd_x = BOARD_X0 + SWD_DX
    swd_y = BOARD_Y0 + SWD_DY
    swd_hole = cyl(swd_x, swd_y, OUTER_Z - LID_SKIN - 0.2, OUTER_Z + 0.2, 4.0)
    swd_rebate = cyl(swd_x, swd_y, OUTER_Z - WINDOW_T, OUTER_Z + 0.2, 4.7)

    body = cut(shell, [pocket, window, rebate, usb_notch, sensor, *screw_tools, swd_hole, swd_rebate])
    return finish(fuse([body, *posts]))


def module_origin() -> tuple[float, float]:
    return (POCKET_X0 + MODULE_INSET, POCKET_Y0 + MODULE_INSET)


def window_mesh() -> trimesh.Trimesh:
    w = WINDOW_X + 2 * BEZEL - 0.3
    h = WINDOW_Y + 2 * BEZEL - 0.3
    mod_x0, mod_y0 = module_origin()
    win_x0 = mod_x0 + (MODULE_X - WINDOW_X) / 2
    win_y0 = mod_y0 + (MODULE_Y - WINDOW_Y) / 2
    plate = rr(0, 0, w, h, 1.2, 0.0, WINDOW_T - 0.05)
    # 0.15 mm inset from the rebate so the plate drops in flush with the lid.
    return finish(shift(plate, win_x0 - BEZEL + 0.15, win_y0 - BEZEL + 0.15, OUTER_Z - WINDOW_T))


def swd_plug_mesh() -> trimesh.Trimesh:
    z0 = OUTER_Z - LID_SKIN
    nose = cyl(BOARD_X0 + SWD_DX, BOARD_Y0 + SWD_DY, z0, z0 + LID_SKIN - WINDOW_T, 3.85)
    flange = cyl(
        BOARD_X0 + SWD_DX,
        BOARD_Y0 + SWD_DY,
        z0 + LID_SKIN - WINDOW_T,
        z0 + LID_SKIN - 0.05,
        4.5,
    )
    return finish(fuse([nose, flange]))


def require_solid(name: str, mesh: trimesh.Trimesh) -> None:
    if mesh.volume < 40:
        raise SystemExit(f"{name} volume {mesh.volume:.1f} mm^3 is not a solid shell")
    if not mesh.is_watertight:
        raise SystemExit(f"{name} mesh is not watertight")
    bounds = mesh.bounds
    size = bounds[1] - bounds[0]
    print(
        f"{name:10}  {size[0]:6.2f} x {size[1]:6.2f} x {size[2]:6.2f} mm"
        f"   volume {mesh.volume:8.0f} mm^3"
    )


def expect(mesh: trimesh.Trimesh, points: list[tuple[float, float, float]], inside: bool, label: str) -> None:
    hit = mesh.contains(np_points(points))
    bad = [p for p, flag in zip(points, hit) if bool(flag) != inside]
    if bad:
        where = "inside" if inside else "outside"
        raise SystemExit(f"{label}: expected {where}, failed at {bad}")


def np_points(points: list[tuple[float, float, float]]):
    import numpy as np

    return np.asarray(points, dtype=float)


def verify(base: trimesh.Trimesh, lid: trimesh.Trimesh) -> None:
    usb_y = BOARD_Y0 + USB_DY
    usb_z = FLOOR_T + BOSS_H + BOARD_T + 1.5
    solar_x = BOARD_X0 + SOLAR_DX
    sensor_x = BOARD_X0 + SENSOR_DX
    mod_x0, mod_y0 = module_origin()
    win_x = mod_x0 + MODULE_X / 2
    win_y = mod_y0 + MODULE_Y / 2

    expect(
        base,
        [(OUTER_X / 2, OUTER_Y / 2, 0.8), (SCREWS[0][0], SCREWS[0][1], 5.0)],
        True,
        "base solid",
    )
    expect(
        base,
        [
            (BOARD_X0 + BOARD_W / 2, BOARD_Y0 + BOARD_D / 2, 7.0),
            (1.0, usb_y, usb_z),
            (solar_x, 0.6, FLOOR_T + BOSS_H + 2.0),
            (sensor_x, OUTER_Y - 0.6, 9.4),
            (BAT_X0 + BAT_L / 2, BAT_Y0 + BAT_W / 2, FLOOR_T + 2.0),
            (SCREWS[0][0], SCREWS[0][1], BASE_TOP - 1.0),
        ],
        False,
        "base openings",
    )
    expect(
        lid,
        [(8.0, 8.0, OUTER_Z - 0.4), (win_x, mod_y0 + 1.0, OUTER_Z - 0.4)],
        True,
        "lid skin",
    )
    expect(
        lid,
        [
            (win_x, win_y, OUTER_Z - 0.2),
            (mod_x0 + MODULE_X / 2, mod_y0 + MODULE_Y / 2, OUTER_Z - 2.2),
            (SCREWS[1][0], SCREWS[1][1], OUTER_Z - 0.4),
            (BOARD_X0 + SWD_DX, BOARD_Y0 + SWD_DY, OUTER_Z - 0.3),
            (sensor_x, OUTER_Y - 0.6, 9.6),
        ],
        False,
        "lid openings",
    )
    # Skirt must sit inside the base opening with the 0.4 mm lip clearance.
    skirt_z = BASE_TOP - SKIRT_DROP / 2
    expect(
        base,
        [(WALL + LIP_PLAY + 0.3, OUTER_Y / 2, skirt_z)],
        False,
        "lip clearance",
    )
    print("openings   usb, solar, sensor, screws, window, swd hatch")


def main() -> None:
    confirm_display()
    check_layout()
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    parts = {
        "base": base_mesh(),
        "lid": lid_mesh(),
        "window": window_mesh(),
        "swd_plug": swd_plug_mesh(),
    }
    for name, mesh in parts.items():
        require_solid(name, mesh)
        path = OUT_DIR / f"{name}.stl"
        mesh.export(path)
        print(f"wrote {path}")

    verify(parts["base"], parts["lid"])

    keep = antenna_keepout_x()
    print()
    print(f"display     {DISPLAY_NAME}")
    print("header      " + " ".join(f"{n}:{name}/{pin}" for n, name, pin in DISPLAY_HEADER))
    print(f"outer       {OUTER_X:.1f} x {OUTER_Y:.1f} x {OUTER_Z:.1f} mm")
    print(f"board at    ({BOARD_X0:.1f}, {BOARD_Y0:.1f})  {BOARD_W:.2f} x {BOARD_D:.2f} mm")
    print(f"battery at  ({BAT_X0:.1f}, {BAT_Y0:.1f})  {BAT_L:.0f} x {BAT_W:.0f} x {BAT_T:.0f} mm")
    print(f"keepout x > {keep:.1f} mm  (right {ANTENNA_KEEPOUT:.0f} mm of the board)")
    print(f"pocket at   ({POCKET_X0:.1f}, {POCKET_Y0:.1f})  {POCKET_X:.1f} x {POCKET_Y:.1f} mm")


if __name__ == "__main__":
    main()
