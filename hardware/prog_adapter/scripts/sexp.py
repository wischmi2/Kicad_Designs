"""Minimal KiCad S-expression parser / writer."""
import re

class Q(str):
    """Quoted string atom."""
    pass

_tok = re.compile(r'\s*(\(|\)|"(?:[^"\\]|\\.)*"|[^\s()"]+)', re.S)

def parse(text):
    pos = 0
    stack = [[]]
    n = len(text)
    while True:
        m = _tok.match(text, pos)
        if not m:
            break
        t = m.group(1)
        pos = m.end()
        if t == '(':
            stack.append([])
        elif t == ')':
            x = stack.pop()
            stack[-1].append(x)
        elif t.startswith('"'):
            s = t[1:-1].replace('\\"', '"').replace('\\n', '\n').replace('\\\\', '\\')
            stack[-1].append(Q(s))
        else:
            stack[-1].append(t)
        if pos >= n:
            break
    return stack[0][0] if len(stack[0]) == 1 else stack[0]

def q(s):
    return '"' + str(s).replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n') + '"'

def dump(x, ind=0):
    if isinstance(x, list):
        if not x:
            return '()'
        simple = all(not isinstance(e, list) for e in x)
        if simple and len(x) <= 8:
            return '(' + ' '.join(dump(e) for e in x) + ')'
        parts = [dump(x[0])]
        out = '(' + parts[0]
        for e in x[1:]:
            if isinstance(e, list):
                out += '\n' + '\t' * (ind + 1) + dump(e, ind + 1)
            else:
                out += ' ' + dump(e)
        out += '\n' + '\t' * ind + ')'
        return out
    if isinstance(x, Q):
        return q(x)
    if isinstance(x, float):
        s = ('%.4f' % x).rstrip('0').rstrip('.')
        return s if s not in ('-0', '') else '0'
    return str(x)

def find(x, key):
    for e in x:
        if isinstance(e, list) and e and e[0] == key:
            return e
    return None

def findall(x, key):
    return [e for e in x if isinstance(e, list) and e and e[0] == key]
