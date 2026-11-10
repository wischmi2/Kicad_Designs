import sys, os, uuid, math, json, copy
sys.path.insert(0, os.path.dirname(__file__))
from sexp import parse, dump, Q, find, findall
from parts import COMPS, SYMSRC, LIB

OUT = sys.argv[1]  # project dir
KSYM = r"C:/Program Files/KiCad/10.0/share/kicad/symbols/"
NS = uuid.UUID('6f1c2a5e-0000-4000-8000-0000000000a1')
def U(name):
    return str(uuid.uuid5(NS, name))
ROOT = U('root')

_libcache = {}
def libsyms(lib):
    if lib not in _libcache:
        t = parse(open(KSYM + lib + '.kicad_sym', encoding='utf-8').read())
        _libcache[lib] = {s[1]: s for s in findall(t, 'symbol')}
    return _libcache[lib]

def flat(lib, name):
    s = copy.deepcopy(libsyms(lib)[name])
    ext = find(s, 'extends')
    if not ext:
        return s
    parent = flat(lib, ext[1])
    pname = parent[1]
    out = [ 'symbol', Q(name) ]
    dprops = {p[1]: p for p in findall(s, 'property')}
    for e in parent[2:]:
        if isinstance(e, list) and e[0] == 'property':
            out.append(dprops.pop(e[1], e))
        elif isinstance(e, list) and e[0] == 'symbol':
            e = copy.deepcopy(e)
            e[1] = Q(str(e[1]).replace(pname, name, 1))
            out.append(e)
        else:
            out.append(e)
    # insert remaining derived props after the last property
    idx = max(i for i, e in enumerate(out) if isinstance(e, list) and e[0] == 'property') + 1
    for p in dprops.values():
        out.insert(idx, p); idx += 1
    return out

def pins_of(sym):
    res = {}
    def walk(x):
        for e in x:
            if isinstance(e, list):
                if e[0] == 'pin':
                    at = find(e, 'at'); num = find(e, 'number')[1]
                    res.setdefault(str(num), []).append((float(at[1]), float(at[2]), float(at[3])))
                else:
                    walk(e)
    walk(sym)
    return res

used = sorted(set(c['sym'] for c in COMPS.values()))
symdefs = {k: flat(*SYMSRC[k]) for k in used}

# ---- local symbol library ----
lib = ['kicad_symbol_lib', ['version', '20251024'], ['generator', Q('prog_adapter_gen')], ['generator_version', Q('10.0')]]
for k in used:
    s = copy.deepcopy(symdefs[k])
    lib.append(s)
open(os.path.join(OUT, 'prog_adapter.kicad_sym'), 'w', encoding='utf-8', newline='\n').write(dump(lib) + '\n')

def g(v):  # snap to 0.01
    return round(v, 4)

def prop(name, val, x, y, hide=True, ang=0, justify=None):
    eff = ['effects', ['font', ['size', '1.27', '1.27']]]
    if justify:
        eff.append(['justify', justify])
    p = ['property', Q(name), Q(val), ['at', g(x), g(y), ang]]
    if hide:
        p.append(['hide', 'yes'])
    p += [['show_name', 'no'], ['do_not_autoplace', 'no'], eff]
    return p

sch = ['kicad_sch', ['version', '20260306'], ['generator', Q('eeschema')], ['generator_version', Q('10.0')],
       ['uuid', Q(ROOT)], ['paper', Q('A3')],
       ['title_block', ['title', Q('prog_adapter: XM125 UART / Tag-Connect SWD / USB-C 3.0 V')], ['date', Q('2026-11-07')],
        ['rev', Q('0.1')], ['company', Q('Brian Schmid')],
        ['comment', '1', Q('A XM125 UART, B TC2030 SWD to Cortex-10, C SWD breakout, D USB-C 3.0 V')],
        ['comment', '2', Q('3V0 separate from +1V8 and VTref; GND common')]]]
ls = ['lib_symbols']
for k in used:
    s = copy.deepcopy(symdefs[k]); s[1] = Q(LIB + ':' + k)
    ls.append(s)
sch.append(ls)

items = []
nwire = 0
def wire(a, b):
    global nwire
    nwire += 1
    items.append(['wire', ['pts', ['xy', g(a[0]), g(a[1])], ['xy', g(b[0]), g(b[1])]],
                  ['stroke', ['width', '0'], ['type', 'default']], ['uuid', Q(U('w%d' % nwire))]])

nl = 0
def label(name, p, outward):
    global nl
    nl += 1
    dx, dy = outward
    if abs(dx) > abs(dy):
        ang, just = (0, 'left bottom') if dx > 0 else (180, 'right bottom')
    else:
        ang, just = (90, 'left bottom') if dy < 0 else (270, 'right bottom')
    items.append(['label', Q(name), ['at', g(p[0]), g(p[1]), ang],
                  ['effects', ['font', ['size', '1.27', '1.27']], ['justify'] + just.split()], ['uuid', Q(U('l%d' % nl))]])

def noconn(p):
    items.append(['no_connect', ['at', g(p[0]), g(p[1])], ['uuid', Q(U('nc%.2f_%.2f' % p))]])

STUB = 2.54
for ref, c in COMPS.items():
    sd = symdefs[c['sym']]
    X, Y = c['pos']
    pins = pins_of(sd)
    power = c.get('power', False)
    sym = ['symbol', ['lib_id', Q(LIB + ':' + c['sym'])], ['at', g(X), g(Y), 0], ['unit', 1], ['body_style', 1],
           ['exclude_from_sim', 'no'], ['in_bom', 'yes' if c.get('bom', True) else 'no'], ['on_board', 'no' if power else 'yes'],
           ['in_pos_files', 'yes'], ['dnp', 'no'], ['uuid', Q(U('sym' + ref))]]
    sym.append(prop('Reference', ref, X + 3, Y - 6, hide=power, justify='left'))
    sym.append(prop('Value', c['value'], X + 3, Y + 6.5, hide=power, justify='left'))
    sym.append(prop('Footprint', (LIB + ':' + c['fp']) if c['fp'] else '', X, Y))
    sym.append(prop('Datasheet', '~', X, Y))
    for k in ('MPN', 'Manufacturer', 'DigiKey', 'Mouser'):
        if k in c['f']:
            sym.append(prop(k, c['f'][k], X, Y))
    for num in sorted(pins):
        sym.append(['pin', Q(num), ['uuid', Q(U('pin' + ref + num))]])
    sym.append(['instances', ['project', Q('prog_adapter'), ['path', Q('/' + ROOT), ['reference', Q(ref)], ['unit', 1]]]])
    items.append(sym)
    done = set()
    for num, net in c['nets'].items():
        for (px, py, pa) in pins[num][:1]:
            p = (X + px, Y - py)
            ox, oy = -math.cos(math.radians(pa)), math.sin(math.radians(pa))
            ox, oy = round(ox), round(oy)
            if power:
                q2 = (p[0], p[1] - STUB)
                wire(p, q2); label(net, q2, (0, -1))
                continue
            q2 = (p[0] + ox * STUB, p[1] + oy * STUB)
            if p in done:
                continue
            done.add(p)
            wire(p, q2)
            label(net, q2, (ox, oy))
    for num in c.get('nc', []):
        for (px, py, pa) in pins[num][:1]:
            noconn((X + px, Y - py))

# section headings
def text(s, x, y, size=2.54):
    items.append(['text', Q(s), ['exclude_from_sim', 'no'], ['at', x, y, 0],
                  ['effects', ['font', ['size', size, size], ['bold', 'yes']], ['justify', 'left', 'bottom']], ['uuid', Q(U('t' + s))]])
text('A. XM125 UART ONLY (TC2030-IDC to FTDI TTL-232RG-VREG1V8-WE)', 20.32, 35.56)
text('B. SWD - Tag-Connect std (TC2030-IDC to Cortex-10, nRF9160 DK Debug out)', 165.1, 35.56)
text('C. SWD 0.1in breakout (parallel with J3)', 210.82, 83.82, 1.8)
text('D. USB-C 3.0 V supply for water level TP9 VSENS + TP10 VBAT', 20.32, 116.84)
text('JP1 on = BOOTLOADER, off = RUN.  FTDI RED/BRN/GRN wires: not connected (insulate).', 20.32, 104.14, 1.5)
text('No DK-side supply on Debug out (P19 pin 1 is target VTref sense) -> no LED in section B.', 165.1, 116.84, 1.5)
text('Mounting holes', 20.32, 177.8, 1.8)

sch += items
sch.append(['sheet_instances', ['path', Q('/'), ['page', Q('1')]]])
sch.append(['embedded_fonts', 'no'])
open(os.path.join(OUT, 'prog_adapter.kicad_sch'), 'w', encoding='utf-8', newline='\n').write(dump(sch) + '\n')
json.dump({'root': ROOT, 'sym': {r: U('sym' + r) for r in COMPS}}, open(os.path.join(OUT, '..', 'uuids_tmp.json') if False else os.path.join(os.path.dirname(__file__), 'uuids.json'), 'w'))
print('ok', len(items))
