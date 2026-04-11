"""Compare brace depths between v2 and v3 HTML to find where things went wrong."""
import sys, io, subprocess, re
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def script_text(html):
    """Extract the main inline script (not the JSON one, not small ones)."""
    scripts = re.findall(r'<script(?![^>]*src)(?![^>]*application/json)[^>]*>(.*?)</script>', html, re.DOTALL)
    return max(scripts, key=len)

def depth_track(s):
    depth = 0
    in_str = False
    sc = None
    bs = False
    history = []
    for j, c in enumerate(s):
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
                history.append((j, '+', depth))
            elif c == '}':
                depth -= 1
                history.append((j, '-', depth))
    return depth, history

# v2 baseline
res = subprocess.run(['git', 'show', '54d1a8e:public/index.html'],
                     capture_output=True, text=True, encoding='utf-8')
v2_html = res.stdout
v2_script = script_text(v2_html)
v2_depth, _ = depth_track(v2_script)
print(f'v2 baseline: {len(v2_script):,} chars, final depth: {v2_depth}')

# v3 current
with open('public/index.html', 'r', encoding='utf-8') as f:
    v3_html = f.read()
v3_script = script_text(v3_html)
v3_depth, v3_hist = depth_track(v3_script)
print(f'v3 current:  {len(v3_script):,} chars, final depth: {v3_depth}')

# Find first negative-depth point
for j, op, d in v3_hist:
    if d < 0:
        print(f'First negative depth at char {j}: {op} -> depth {d}')
        print(f'Context: ...{v3_script[max(0,j-80):j+80]}...')
        break
else:
    print('No negative depth found before final')
