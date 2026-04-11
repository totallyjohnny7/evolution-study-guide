"""Compare functions across index.html vs index_prod.html."""
import sys, io, re
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def main_script(html):
    scripts = re.findall(
        r'<script(?![^>]*src)(?![^>]*application/json)[^>]*>(.*?)</script>',
        html, re.DOTALL
    )
    return max(scripts, key=len)

def extract_fn(s, name):
    m = re.search(r'function\s+' + re.escape(name) + r'\s*\(', s)
    if not m:
        return None
    start = s.find('{', m.end())
    if start < 0:
        return None
    depth = 0
    in_str = False
    sc = None
    bs = False
    for i in range(start, len(s)):
        c = s[i]
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
                    return s[m.start():i+1]
    return None


with open('public/index_prod.html', 'r', encoding='utf-8') as f:
    prod = f.read()

print(f'prod size: {len(prod)}')
js = main_script(prod)
print(f'prod script size: {len(js)}')
print()

for name in ['initC', 'initQ', 'rV2', 'render', 'rSheet', 'rCards', 'rQuiz', 'rVis']:
    fn = extract_fn(js, name)
    if fn:
        print(f'{name}: {len(fn)} chars')
        if name in ('initC', 'initQ'):
            print(f'   {fn}')
    else:
        print(f'{name}: NOT FOUND')

print()
print('prod has Sheet tab in render tabs:',
      "['sheet'" in js or '"sheet"' in js)
