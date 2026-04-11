"""Verify the OLD strings are found exactly in v2 baseline."""
import sys, io, subprocess, re
sys.path.insert(0, '_work')
from inject_v3 import (
    INIT_C_OLD, INIT_Q_OLD, RVIS_OLD_PIECE,
    RENDER_TABS_OLD, RENDER_DISPATCH_OLD,
)
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

res = subprocess.run(['git', 'show', '54d1a8e:public/index.html'],
                     capture_output=True, text=True, encoding='utf-8')
html = res.stdout

print('Found INIT_C_OLD?',           INIT_C_OLD in html)
print('Found INIT_Q_OLD?',           INIT_Q_OLD in html)
print('Found RVIS_OLD_PIECE?',       RVIS_OLD_PIECE in html)
print('Found RENDER_TABS_OLD?',      RENDER_TABS_OLD in html)
print('Found RENDER_DISPATCH_OLD?',  RENDER_DISPATCH_OLD in html)

# Find actual initC in v2 and compare
m = re.search(r'function initC\(\)\{[^}]*\}', html)
if m:
    actual = m.group()
    print(f'\nActual v2 initC ({len(actual)} chars):')
    print(f'  {actual}')
    print(f'\nMy INIT_C_OLD ({len(INIT_C_OLD)} chars):')
    print(f'  {INIT_C_OLD}')

# Find actual initQ
idx = html.find('function initQ(')
if idx >= 0:
    # bracket-scan
    start = html.find('{', idx)
    depth = 0; end = -1
    for i in range(start, len(html)):
        c = html[i]
        if c == '{': depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                end = i+1; break
    if end > 0:
        actual = html[idx:end]
        print(f'\nActual v2 initQ ({len(actual)} chars):')
        print(f'  {actual}')
        print(f'\nMy INIT_Q_OLD ({len(INIT_Q_OLD)} chars):')
        print(f'  {INIT_Q_OLD}')
