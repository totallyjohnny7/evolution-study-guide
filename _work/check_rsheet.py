"""Extract original rSheet from v2 commit."""
import sys, io, subprocess
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Read v2 HTML from git
res = subprocess.run(['git', 'show', '54d1a8e:public/index.html'],
                     capture_output=True, text=True, encoding='utf-8')
html = res.stdout

idx = html.find('function rSheet(ct)')
if idx < 0:
    print('not found')
    sys.exit()

start = html.find('{', idx)
depth = 0
in_str = False
sc = None
bs = False
end = -1
for i in range(start, len(html)):
    c = html[i]
    if bs:
        bs = False
        continue
    if in_str:
        if c == '\\':
            bs = True
            continue
        if c == sc:
            in_str = False
    else:
        if c in "'\"`":
            in_str = True
            sc = c
        elif c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                end = i + 1
                break

print(f'rSheet length: {end - idx}')
fn = html[idx:end]
print('--- function rSheet (full) ---')
print(fn)
print('--- end ---')

# Also extract the JS context around rSheet to find what rSheet expects vs what's there
print('\nContext after rSheet:')
print(html[end:end+200])
