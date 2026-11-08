"""Build prog_adapter.kicad_pcb with KiCad 10 pcbnew Python.
usage: python.exe gen_pcb.py <project_dir> <build_dir> <netlist.xml>
Board is created in build_dir (next to a copy of the .kicad_pro) and only the .kicad_pcb is copied back."""
import sys, os, json, shutil, math
import xml.etree.ElementTree as ET
import pcbnew
sys.path.insert(0, os.path.dirname(__file__))
from parts import COMPS

PRJ, BLD, NETXML = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(BLD, exist_ok=True)
shutil.copy(os.path.join(PRJ, 'prog_adapter.kicad_pro'), os.path.join(BLD, 'prog_adapter.kicad_pro'))
# Custom rules. KiCad 10 needs units on every value: "(min 0.25)" without "mm" makes the whole
# file unparseable and kicad-cli then silently ignores it (review B1, 2026-11-07).
DRU = """(version 1)
# Board-wide hole clearance 0.25 mm (board setup minimum is lowered to 0.15 only so the
# J6 exception below can take effect; board-setup values are hard minimums).
(rule "hole clearance default"
	(constraint hole_clearance (min 0.25mm)))
# GCT USB4105-GF-A recommended land pattern (KiCad stock footprint): the 0.65 mm NPTH
# locating holes sit 0.175 mm from the edge of the A1/B12 and A12/B1 GND pads.
(rule "J6 NPTH to own pads"
	(condition "A.memberOfFootprint('J6') && B.memberOfFootprint('J6')")
	(constraint hole_clearance (min 0.15mm)))
"""
for d in (PRJ, BLD):
    open(os.path.join(d, 'prog_adapter.kicad_dru'), 'w', encoding='utf-8', newline='\n').write(DRU)
PCB = os.path.join(BLD, 'prog_adapter.kicad_pcb')
if os.path.exists(PCB):
    os.remove(PCB)
board = pcbnew.NewBoard(PCB)
LIBDIR = os.path.join(PRJ, 'prog_adapter.pretty')
uu = json.load(open(os.path.join(os.path.dirname(__file__), 'uuids.json')))

def V(x, y):
    return pcbnew.VECTOR2I(pcbnew.FromMM(x), pcbnew.FromMM(y))
MM = pcbnew.FromMM
F, B = pcbnew.F_Cu, pcbnew.B_Cu

# ---------------- board outline ----------------
X0, Y0, W, H, RC = 100.0, 100.0, 72.0, 48.0, 2.0
X1, Y1 = X0 + W, Y0 + H
def seg(layer, a, b, w=0.1):
    s = pcbnew.PCB_SHAPE(board); s.SetShape(pcbnew.SHAPE_T_SEGMENT)
    s.SetStart(V(*a)); s.SetEnd(V(*b)); s.SetLayer(layer); s.SetWidth(MM(w)); board.Add(s)
def arc(layer, c, start, ang, w=0.1):
    s = pcbnew.PCB_SHAPE(board); s.SetShape(pcbnew.SHAPE_T_ARC)
    s.SetCenter(V(*c)); s.SetStart(V(*start)); s.SetArcAngleAndEnd(pcbnew.EDA_ANGLE(ang, pcbnew.DEGREES_T), True)
    s.SetLayer(layer); s.SetWidth(MM(w)); board.Add(s)
E = pcbnew.Edge_Cuts
seg(E, (X0 + RC, Y0), (X1 - RC, Y0)); seg(E, (X1, Y0 + RC), (X1, Y1 - RC))
seg(E, (X1 - RC, Y1), (X0 + RC, Y1)); seg(E, (X0, Y1 - RC), (X0, Y0 + RC))
arc(E, (X1 - RC, Y0 + RC), (X1 - RC, Y0), 90); arc(E, (X1 - RC, Y1 - RC), (X1, Y1 - RC), 90)
arc(E, (X0 + RC, Y1 - RC), (X0 + RC, Y1), 90); arc(E, (X0 + RC, Y0 + RC), (X0, Y0 + RC), 90)

# ---------------- nets from schematic netlist ----------------
root = ET.parse(NETXML).getroot()
padnet, nets = {}, {}
for n in root.find('nets'):
    name = n.get('name')
    ni = pcbnew.NETINFO_ITEM(board, name); board.Add(ni); nets[name] = ni
    for nd in n:
        padnet[(nd.get('ref'), nd.get('pin'))] = name
def N(name):
    return nets['/' + name] if '/' + name in nets else nets[name]

# ---------------- placement ----------------
UY = 135.3
REFPOS = {'J1': (120.0, 105.6, 0), 'R1': (125.0, 118.5, 90), 'R2': (119.4, 118.5, 90), 'SW1': (130.25, 120.75, 0),
  'JP1': (133.8, 105.2, 0), 'R3': (135.5, 114.0, 90), 'J6': (103.5, 130.0, 0), 'R4': (111.6, UY - 2.6, 0), 'R5': (111.6, UY + 3.3, 0),
  'F1': (113.8, 139.9, 0), 'C1': (119.9, 141.0, 0), 'U1': (121.2, 134.7, 0), 'C2': (124.6, 135.0, 0), 'R6': (128.0, 134.8, 0),
  'D1': (131.4, 137.9, 0), 'J5': (113.8, 144.5, 0), 'J3': (142.6, 104.5, 0), 'J4': (148.5, 103.3, 0), 'J2': (160.8, 105.6, 0),
  'SW2': (143.75, 134.25, 0)}
PLACE = {
    # ref: (x, y, rot)
    'H1': (103.5, 103.5, 0), 'H2': (168.5, 103.5, 0), 'H3': (103.5, 144.5, 0), 'H4': (168.5, 144.5, 0),
    # A
    'J1': (126.0, 110.0, 270), 'J7': (107.6, 116.0, 0), 'R2': (120.92, 118.5, 270), 'R1': (123.46, 118.5, 90),
    'SW1': (127.0, 118.5, 0), 'JP1': (133.8, 110.0, 180), 'R3': (133.8, 114.0, 90),
    # D
    'J6': (103.675, UY, 270), 'R4': (111.6, UY - 1.25, 0), 'R5': (111.6, UY + 1.75, 0), 'F1': (113.8, 141.6, 0),
    'C1': (117.4, 140.6, 270), 'U1': (121.2, 137.0, 0), 'C2': (124.6, 137.0, 270), 'R6': (128.0, 136.05, 0),
    'D1': (131.4, 136.05, 180), 'J5': (116.0, 144.5, 90),
    # B / C
    'J3': (142.0, 108.5, 0), 'J4': (148.5, 106.0, 0), 'J2': (159.5, 112.0, 0), 'SW2': (140.5, 132.0, 0),
}
fps = {}
for ref, c in COMPS.items():
    if not c['fp']:
        continue
    fp = pcbnew.FootprintLoad(LIBDIR, c['fp'])
    fp.SetFPID(pcbnew.LIB_ID('prog_adapter', c['fp']))
    fp.SetReference(ref); fp.SetValue(c['value'])
    fp.SetPath(pcbnew.KIID_PATH('/' + uu['sym'][ref]))
    try:
        fp.SetSheetname('Root'); fp.SetSheetfile('prog_adapter.kicad_sch')
    except Exception:
        pass
    for k, v in c['f'].items():
        try:
            fld = pcbnew.PCB_FIELD(fp, pcbnew.FIELD_T_USER, k)
            fld.SetText(v); fld.SetVisible(False); fld.SetLayer(pcbnew.F_Fab)
            fp.Add(fld)
        except Exception as e:
            pass
    x, y, r = PLACE[ref]
    board.Add(fp)
    fp.SetPosition(V(x, y)); fp.SetOrientationDegrees(r)
    if not c.get('bom', True):
        fp.SetExcludedFromBOM(True)
    for p in fp.Pads():
        num = p.GetNumber()
        if num == '':
            continue
        nn = padnet.get((ref, num))
        if nn:
            p.SetNet(nets[nn])
    fps[ref] = fp
    # reference text: keep small
    fp.Reference().SetTextSize(V(0.8, 0.8)); fp.Reference().SetTextThickness(MM(0.15))
    if ref.startswith('H'):
        fp.Reference().SetVisible(False)
    if ref in REFPOS:
        rx, ry, rr = REFPOS[ref]; fp.Reference().SetPosition(V(rx, ry)); fp.Reference().SetTextAngleDegrees(rr)
    try:
        fp.GetField(pcbnew.FIELD_T_DATASHEET).SetText('~')
    except Exception as e:
        print('ds', e)

def pad(ref, num):
    for p in fps[ref].Pads():
        if p.GetNumber() == str(num):
            q = p.GetPosition(); return (pcbnew.ToMM(q.x), pcbnew.ToMM(q.y))
    raise KeyError((ref, num))

# J3 GND pads: solid zone connection (1.27 mm pitch leaves no room for spokes)
for p in fps['J3'].Pads():
    if p.GetNumber() in ('3', '5', '9'):
        p.SetLocalZoneConnection(pcbnew.ZONE_CONNECTION_FULL)

# ---------------- routing ----------------
def T(net, layer, w, pts):
    pts = [pad(*p) if isinstance(p[0], str) else p for p in pts]
    for a, b in zip(pts, pts[1:]):
        t = pcbnew.PCB_TRACK(board); t.SetStart(V(*a)); t.SetEnd(V(*b))
        t.SetLayer(layer); t.SetWidth(MM(w)); t.SetNet(N(net)); board.Add(t)
def VIA(net, x, y):
    v = pcbnew.PCB_VIA(board); v.SetPosition(V(x, y)); v.SetDrill(MM(0.3)); v.SetWidth(MM(0.6))
    v.SetLayerPair(F, B); v.SetNet(N(net)); board.Add(v)

S, P = 0.25, 0.5
# --- Section A ---
T('FTDI_RXD', F, S, [('J7', 2), ('R2', 2)])
T('XM_TX', F, S, [('R2', 1), ('J1', 6)])
T('FTDI_TXD', F, S, [('J7', 3), (123.46, 122.0), ('R1', 1)])
T('XM_RX', F, S, [('R1', 2), ('J1', 4)])
j1_1 = pad('J1', 1); sw1 = PLACE['SW1'][:2]
T('XM_NRST', B, S, [('J1', 1), (j1_1[0] + 1.6, j1_1[1] + 1.6), (j1_1[0] + 1.6, sw1[1] - 1.5), sw1])
j1_2 = pad('J1', 2); r3_1 = pad('R3', 1)
T('XM_1V8', F, S, [('J1', 2), (j1_2[0] + 2.4, r3_1[1]), ('R3', 1)])
T('BOOT_JP', F, S, [('R3', 2), ('JP1', 1)])
j1_3 = pad('J1', 3); jp2 = pad('JP1', 2)
T('XM_BOOT0', F, S, [('J1', 3), (j1_3[0], jp2[1] + 0.84), (j1_3[0] + 0.84, jp2[1]), ('JP1', 2)])
# --- Section D ---
a4 = pad('J6', 'A4'); b4 = pad('J6', 'B4')   # VBUS pad groups (A4/B9 and A9/B4 overlap)
vtop = (a4[0] + 2.1, min(a4[1], b4[1]) - 0.7); vbot = (a4[0] + 2.1, max(a4[1], b4[1]) + 0.7)
for pp, vv in ((a4, None), (b4, None)):
    pass
ytop, ybot = min(a4[1], b4[1]), max(a4[1], b4[1])
T('VBUS', F, P, [(a4[0], ytop), (a4[0] + 1.25, ytop), vtop])
T('VBUS', F, P, [(a4[0], ybot), (a4[0] + 1.25, ybot), vbot])
VIA('VBUS', *vtop); VIA('VBUS', *vbot)
T('VBUS', B, P, [vtop, vbot])
f1 = pad('F1', 1)
T('VBUS', F, P, [vbot, (f1[0] - 1.4, f1[1]), ('F1', 1)])
T('CC1', F, S, [('J6', 'A5'), ('R4', 1)])
T('CC2', F, S, [('J6', 'B5'), ('R5', 1)])
f2 = pad('F1', 2); c1 = pad('C1', 1)
T('5V_F', F, P, [('F1', 2), (f2[0] + 0.5, f2[1]), (f2[0] + 0.5, c1[1]), ('C1', 1)])
u1, u3 = pad('U1', 1), pad('U1', 3)
va, vb = (u1[0] - 1.65, u1[1]), (u1[0] - 1.65, u3[1] + 1.25)
T('5V_F', F, P, [('C1', 1), (vb[0], c1[1]), vb])
T('5V_F', F, P, [vb, (u3[0] - 0.9, u3[1]), ('U1', 3)])
T('5V_F', F, P, [('U1', 1), va]); VIA('5V_F', *va); VIA('5V_F', *vb)
T('5V_F', B, P, [va, vb])
u2 = pad('U1', 2)
T('GND', F, S, [('U1', 2), (u2[0] - 2.9, u2[1])]); VIA('GND', u2[0] - 2.9, u2[1])
T('3V0', F, P, [('U1', 5), ('C2', 1), ('R6', 1)])
c2 = pad('C2', 1); j52 = pad('J5', 2)
xd = c2[0] + 1.35
T('3V0', F, P, [(xd, c2[1]), (xd, j52[1] - 2.0), (j52[0], j52[1] - 2.0), ('J5', 2)])  # J5 moved left
T('3V0', F, P, [('J5', 2), ('J5', 1)])
T('LED_A', F, S, [('R6', 2), ('D1', 2)])
d1k = pad('D1', 1)
T('GND', F, S, [('D1', 1), (d1k[0] + 1.3, d1k[1])]); VIA('GND', d1k[0] + 1.3, d1k[1])
for ref in ('R4', 'R5'):
    q = pad(ref, 2); T('GND', F, S, [(ref, 2), (q[0] + 1.2, q[1])]); VIA('GND', q[0] + 1.2, q[1])
for ref in ('C1', 'C2'):
    q = pad(ref, 2); T('GND', F, S, [(ref, 2), (q[0], q[1] + 1.2)]); VIA('GND', q[0], q[1] + 1.2)
# USB GND pads: short stubs + vias
a1 = pad('J6', 'A1'); a12 = pad('J6', 'A12')
for g in (a1, a12):
    yy = g[1] - 0.9 if g[1] < 136.5 else g[1] + 0.9
    T('GND', F, S, [g, (g[0] + 0.6, yy)]); VIA('GND', g[0] + 0.6, yy)
# --- Section B/C ---
T('SWD_SWDIO', F, S, [('J3', 2), ('J4', 2)])
j3_4, j4_3 = pad('J3', 4), pad('J4', 3)
T('SWD_SWCLK', F, S, [('J3', 4), (j3_4[0] + 2.23, j3_4[1]), (j4_3[0] - 1.7, j4_3[1]), ('J4', 3)])
j3_6, j4_4 = pad('J3', 6), pad('J4', 4)
T('SWD_SWO', F, S, [('J3', 6), (j3_6[0] + 1.33, j3_6[1]), (j4_4[0] - 1.3, j4_4[1]), ('J4', 4)])
j3_10, j4_5 = pad('J3', 10), pad('J4', 5)
T('SWD_NRESET', F, S, [('J3', 10), (j3_10[0] + 0.93, j3_10[1]), (j4_5[0] - 1.7, j4_5[1]), ('J4', 5)])
j3_1, j4_1 = pad('J3', 1), pad('J4', 1)
T('SWD_VTREF', F, S, [('J3', 1), (j3_1[0], j3_1[1] - 1.3), (j4_1[0] - 1.2, j3_1[1] - 1.3), ('J4', 1)])
# J3 GND pins to a GND via at the left
gx = pad('J3', 3)[0] - 1.1
for n in ('3', '5', '9'):
    q = pad('J3', n); T('GND', F, S, [('J3', n), (gx, q[1])])
T('GND', F, S, [(gx, pad('J3', 3)[1]), (gx, pad('J3', 9)[1])])
T('GND', F, S, [(gx, pad('J3', 5)[1]), (gx - 1.4, pad('J3', 5)[1])]); VIA('GND', gx - 1.4, pad('J3', 5)[1])
# J4 -> J2
j2 = {n: pad('J2', n) for n in range(1, 7)}
j4 = {n: pad('J4', n) for n in range(1, 7)}
T('SWD_SWDIO', F, S, [('J4', 2), (j2[2][0] - 1.06, j4[2][1]), (j2[2][0], j4[2][1] + 1.06), ('J2', 2)])
ymid = (j2[1][1] + j2[3][1]) / 2
T('SWD_SWCLK', F, S, [('J4', 3), (j2[1][0] - 4.0, j4[3][1]), (j2[1][0] - 4.0 + (ymid - j4[3][1]), ymid),
                      (j2[4][0] - 1.27, ymid), ('J2', 4)])
T('SWD_NRESET', F, S, [('J4', 5), (j4[5][0] + 2.5, j4[5][1]), (j4[5][0] + 2.5 + (j4[5][1] - j2[3][1]), j2[3][1]), ('J2', 3)])
xs = j4[4][0] + 2.1
T('SWD_SWO', B, S, [('J4', 4), (xs, j4[4][1] + 2.1), (xs, j2[6][1] + 2.5), (j2[6][0], j2[6][1] + 2.5), ('J2', 6)])
T('SWD_VTREF', B, S, [('J4', 1), (j2[1][0] - 2.0, j4[1][1]), (j2[1][0] - 2.0, j2[1][1] - 1.4), ('J2', 1)])
sw2 = pad('SW2', 1)
sw2b = [p for p in fps['SW2'].Pads() if p.GetNumber() == '1']
sw2r = max((pcbnew.ToMM(p.GetPosition().x), pcbnew.ToMM(p.GetPosition().y)) for p in sw2b)
xr = j4[5][0] - 1.5
T('SWD_NRESET', B, S, [('J4', 5), (xr, j4[5][1] + 1.5), (xr, sw2r[1] - 1.7), sw2r])

# ---------------- GND zones (both layers) ----------------
def zone(layer, prio=0):
    z = pcbnew.ZONE(board); z.SetLayer(layer); z.SetNet(N('GND'))
    o = z.Outline(); o.NewOutline()
    for (x, y) in ((X0, Y0), (X1, Y0), (X1, Y1), (X0, Y1)):
        o.Append(MM(x), MM(y))
    z.SetLocalClearance(MM(0.3)); z.SetMinThickness(MM(0.25))
    z.SetPadConnection(pcbnew.ZONE_CONNECTION_THERMAL)
    z.SetThermalReliefGap(MM(0.3)); z.SetThermalReliefSpokeWidth(MM(0.45))
    z.SetAssignedPriority(prio); z.SetIsFilled(False)
    board.Add(z); return z
zone(F); zone(B)
# stitching vias
for (x, y) in [(108.0, 104.0), (114.0, 104.5), (136.5, 105.0), (136.5, 124.0), (116.0, 126.5), (107.5, 126.5),
               (136.5, 131.0), (136.5, 146.0), (110.0, 146.5), (130.0, 146.0), (152.0, 128.5), (165.0, 128.0),
               (152.0, 146.0), (160.0, 138.0), (170.0, 124.0), (152.5, 101.5), (143.5, 103.0), (118.0, 130.0), (128.0, 130.0)]:
    VIA('GND', x, y)

# ---------------- silkscreen ----------------
def txt(s, x, y, size=0.8, layer=pcbnew.F_SilkS, bold=False, rot=0, just='c', th=None):
    t = pcbnew.PCB_TEXT(board); t.SetText(s); t.SetPosition(V(x, y)); t.SetLayer(layer)
    t.SetTextSize(V(size, size)); t.SetTextThickness(MM(th if th else (max(0.15, size * 0.2) if bold else 0.15)))
    t.SetBold(bold)
    if rot:
        t.SetTextAngleDegrees(rot)
    t.SetHorizJustify({'c': pcbnew.GR_TEXT_H_ALIGN_CENTER, 'l': pcbnew.GR_TEXT_H_ALIGN_LEFT, 'r': pcbnew.GR_TEXT_H_ALIGN_RIGHT}[just])
    if layer == pcbnew.B_SilkS:
        t.SetMirrored(True)
    board.Add(t)
SL = pcbnew.F_SilkS
XD = 137.2   # divider between A/D and B/C
seg(SL, (XD, 101.0), (XD, 147.0), 0.2)
seg(SL, (101.0, 127.2), (XD, 127.2), 0.2)
# A
txt('A: XM125 UART ONLY', 119.5, 101.9, 1.5, bold=True)
for i, s in enumerate(['J1 XM125', '1 NRST  2 1V8', '3 BOOT0 4 RX', '5 GND   6 TX']):
    txt(s, 105.3, 106.3 + i * 1.2, just='l')
txt('RED/BRN/GRN: NC', 108.4, 124.4, just='l')
txt('XM RESET', 130.25, 116.9)
txt('BOOT0', 136.1, 108.73, rot=90)
txt('JP1 on = BOOTLOADER, off = RUN', 124.6, 125.9)
# D
txt('D: USB-C 3V0 SUPPLY', 119.5, 129.0, 1.5, bold=True)
txt('5.1k CC, no D+/D-', 110.0, 131.4, just='l')
txt('PWR', 131.4, 134.4)
txt('3V0', 116.0, 146.6); txt('3V0', 118.54, 146.6); txt('GND', 121.08, 146.6)
txt('3V0 -> TP9+TP10', 122.6, 143.9, just='l')
txt('GND -> TP8', 122.6, 145.3, just='l')
# B / C
txt('B: SWD - Tag-Connect std', 153.6, 101.9, 1.2, bold=True)
for i, s in enumerate(['J3 to DK Debug out', '1 VTref 2 SWDIO', '3 GND   4 SWCLK', '5 GND   6 SWO',
                       '7 key   8 NC', '9 GND  10 nRESET']):
    txt(s, 137.8, 122.6 + i * 1.3, just='l')
for i, s in enumerate(['J2 TC2030-IDC SWD', '1 VTref  2 SWDIO', '3 nRESET 4 SWCLK', '5 GND    6 SWO']):
    txt(s, 156.3, 123.6 + i * 1.2, just='l')
for n, s in zip(range(1, 7), ['VTref', 'SWDIO', 'SWCLK', 'SWO', 'nRESET', 'GND']):
    txt(s, j4[n][0] + 1.4, j4[n][1], just='l')
txt('C: 0.1in SWD', 150.6, 121.4, 1.0, bold=True)
bx0, by0, bx1, by1 = 146.7, 104.25, 154.65, 120.45
seg(SL, (bx0, by0), (bx1, by0), 0.15); seg(SL, (bx1, by0), (bx1, by1), 0.15)
seg(SL, (bx1, by1), (bx0, by1), 0.15); seg(SL, (bx0, by1), (bx0, by0), 0.15)
txt('SWD RESET', 143.75, 138.7)
txt('PROG ADAPTER', 159.5, 131.6, 1.6, bold=True)
txt('rev 0.1  2026-11-07', 159.5, 134.0, 0.9)
txt('9160 DK J-Link = Nordic only', 159.5, 135.6)
txt('DK SW9 VDD = target V', 159.5, 136.9)
txt('PROG ADAPTER rev 0.1 2026-11-07', 136.0, 146.3, 0.8, layer=pcbnew.B_SilkS)

# ---------------- fill + save ----------------
pcbnew.SaveBoard(PCB, board)
board = pcbnew.LoadBoard(PCB)
filler = pcbnew.ZONE_FILLER(board)
filler.Fill(board.Zones())
pcbnew.SaveBoard(PCB, board)
# The Python ZONE_FILLER does not load the .kicad_dru, so refill with kicad-cli (which does)
# and save; only the .kicad_pcb is copied back to the project.
import subprocess
subprocess.run(['kicad-cli', 'pcb', 'drc', '--refill-zones', '--save-board', '-o', os.path.join(BLD, 'refill.rpt'), PCB], check=True)
shutil.copy(PCB, os.path.join(PRJ, 'prog_adapter.kicad_pcb'))
print('saved', len(fps), 'footprints', board.GetTrackWidthList() if False else '')
