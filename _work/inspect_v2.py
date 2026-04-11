"""Deeply inspect the v2 baseline renderer to understand what to patch."""
import sys, io, re
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('public/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find the main script
scripts = re.findall(
    r'<script(?![^>]*src)(?![^>]*application/json)[^>]*>(.*?)</script>',
    html, re.DOTALL
)
js = max(scripts, key=len)
print(f'Main script: {len(js)} chars')
print()


def extract_fn(js, name):
    """Bracket-matched, string-literal-aware extractor."""
    m = re.search(r'function\s+' + re.escape(name) + r'\s*\(', js)
    if not m:
        return None
    start = js.find('{', m.end())
    if start < 0:
        return None
    depth = 0
    in_str = False
    sc = None
    bs = False
    end = -1
    for i in range(start, len(js)):
        c = js[i]
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
    if end < 0:
        return None
    return js[m.start():end]


# Extract key functions
for name in ['render', 'initC', 'initQ', 'rMap', 'rCards', 'rQuiz',
             'rVis', 'rSheet', 'rV2', 'rSearch']:
    fn = extract_fn(js, name)
    if fn:
        print(f'=== {name} ({len(fn)} chars) ===')
        print(fn)
        print()
    else:
        print(f'=== {name}: NOT FOUND ===')
        print()
