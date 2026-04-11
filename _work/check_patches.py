"""Check brace balance of each replacement string."""
import sys, io

# Import from inject_v3 BEFORE wrapping stdout (inject_v3 wraps it too)
sys.path.insert(0, '_work')
from inject_v3 import (
    RV2_FN, RSHEET_FN, INIT_C_NEW, INIT_Q_NEW,
    RVIS_OLD_PIECE, RVIS_NEW_PIECE,
    INIT_C_OLD, INIT_Q_OLD,
    RENDER_TABS_OLD, RENDER_TABS_NEW,
    RENDER_DISPATCH_OLD, RENDER_DISPATCH_NEW,
)

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def depth(s):
    d = 0
    in_str = False; sc = None; bs = False
    for c in s:
        if bs: bs = False; continue
        if in_str:
            if c == '\\':
                bs = True; continue
            if c == sc: in_str = False
        else:
            if c in "'\"`":
                in_str = True; sc = c
            elif c == '{': d += 1
            elif c == '}': d -= 1
    return d

print('Brace balance for each replacement string:')
for name, s in [
    ('RV2_FN',          RV2_FN),
    ('RSHEET_FN',       RSHEET_FN),
    ('INIT_C_OLD',      INIT_C_OLD),
    ('INIT_C_NEW',      INIT_C_NEW),
    ('INIT_Q_OLD',      INIT_Q_OLD),
    ('INIT_Q_NEW',      INIT_Q_NEW),
    ('RVIS_OLD_PIECE',  RVIS_OLD_PIECE),
    ('RVIS_NEW_PIECE',  RVIS_NEW_PIECE),
    ('RENDER_TABS_OLD', RENDER_TABS_OLD),
    ('RENDER_TABS_NEW', RENDER_TABS_NEW),
    ('RENDER_DISPATCH_OLD', RENDER_DISPATCH_OLD),
    ('RENDER_DISPATCH_NEW', RENDER_DISPATCH_NEW),
]:
    d = depth(s)
    flag = '' if d == 0 else f'   <-- IMBALANCED ({d:+})'
    print(f'  {name:24s} {len(s):6d} chars  depth {d:+}{flag}')

# Net change from each pair
print('\nNet change per replacement pair (new - old depth):')
print(f'  INIT_C: {depth(INIT_C_NEW) - depth(INIT_C_OLD):+}')
print(f'  INIT_Q: {depth(INIT_Q_NEW) - depth(INIT_Q_OLD):+}')
print(f'  RVIS:   {depth(RVIS_NEW_PIECE) - depth(RVIS_OLD_PIECE):+}')
print(f'  TABS:   {depth(RENDER_TABS_NEW) - depth(RENDER_TABS_OLD):+}')
print(f'  DISP:   {depth(RENDER_DISPATCH_NEW) - depth(RENDER_DISPATCH_OLD):+}')
print(f'  RV2 (added net): {depth(RV2_FN):+}')
print(f'  RSHEET (added net): {depth(RSHEET_FN):+}')
