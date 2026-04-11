"""Find tab dispatch and Sheet-related code."""
import re, os, sys, io

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
HTML = os.path.join(ROOT, 'public', 'index_prod.html')

with open(HTML, 'r', encoding='utf-8') as f:
    html = f.read()

# Find the render() function and any sheet references
def bracket_match(src, idx):
    start = src.find('{', idx)
    if start < 0:
        return None
    depth = 0
    i = start
    in_str = False; str_ch = None
    while i < len(src):
        c = src[i]
        if in_str:
            if c == '\\':
                i += 2; continue
            if c == str_ch: in_str = False
        else:
            if c in "'\"`":
                in_str = True; str_ch = c
            elif c == '{': depth += 1
            elif c == '}':
                depth -= 1
                if depth == 0: return i+1
        i += 1
    return None

# render function
idx = html.find('function render(')
if idx > 0:
    end = bracket_match(html, idx)
    print('=== render() ===')
    fn = html[idx:end]
    print(fn[:3000])
    print('... length:', len(fn))
    print()

# Search for 'sheet' or 'Sheet' — case-insensitive
for m in re.finditer(r'sheet', html, re.IGNORECASE):
    ctx = html[max(0,m.start()-60):m.end()+60]
    print(f'@{m.start()}: ...{ctx}...')
    print()
    if m.start() > 700000: break

# Find tab strings in the HTML
print('=== Tab buttons (matches "tab" with brief context) ===')
for m in list(re.finditer(r'tab-(?:label|btn|active)', html))[:10]:
    ctx = html[max(0,m.start()-30):m.end()+30]
    print(f'@{m.start()}: ...{ctx}...')
    print()

# Find the S.tab state variable
print('=== S.tab usages (first 10) ===')
for m in list(re.finditer(r"S\.tab", html))[:10]:
    ctx = html[max(0,m.start()-60):m.end()+120]
    print(f'@{m.start()}: ...{ctx}...')
    print()
