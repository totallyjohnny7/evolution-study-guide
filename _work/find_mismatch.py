"""Track per-function brace counts to find which function lost a brace."""
import sys, io, subprocess, re
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def script_text(html):
    scripts = re.findall(r'<script(?![^>]*src)(?![^>]*application/json)[^>]*>(.*?)</script>', html, re.DOTALL)
    return max(scripts, key=len)

def function_chunks(s):
    """Find each `function name(` and return its bracket-matched body."""
    out = []
    for m in re.finditer(r'function\s+(\w+)\s*\(', s):
        name = m.group(1)
        idx = m.start()
        start = s.find('{', m.end())
        if start < 0: continue
        depth = 0
        in_str = False; sc = None; bs = False
        end = -1
        for i in range(start, len(s)):
            c = s[i]
            if bs: bs=False; continue
            if in_str:
                if c == '\\': bs=True; continue
                if c == sc: in_str=False
            else:
                if c in "'\"`":
                    in_str=True; sc=c
                elif c == '{': depth += 1
                elif c == '}':
                    depth -= 1
                    if depth == 0:
                        end = i+1; break
        if end > 0:
            out.append((name, idx, end, end - idx))
    return out

# v2 baseline
res = subprocess.run(['git', 'show', '54d1a8e:public/index.html'],
                     capture_output=True, text=True, encoding='utf-8')
v2_html = res.stdout
v2_script = script_text(v2_html)

with open('public/index.html', 'r', encoding='utf-8') as f:
    v3_script = script_text(f.read())

v2_funcs = function_chunks(v2_script)
v3_funcs = function_chunks(v3_script)

v2_set = {n: (i, e, sz) for n, i, e, sz in v2_funcs}
v3_set = {n: (i, e, sz) for n, i, e, sz in v3_funcs}

print('Functions in v2 not in v3:')
for n in v2_set:
    if n not in v3_set:
        print(f'  {n}: {v2_set[n][2]} chars')

print('\nFunctions in v3 not in v2:')
for n in v3_set:
    if n not in v2_set:
        print(f'  {n}: {v3_set[n][2]} chars')

print('\nFunctions size diff (v3 - v2, only != 0):')
for n in sorted(set(v2_set) | set(v3_set)):
    if n in v2_set and n in v3_set:
        d = v3_set[n][2] - v2_set[n][2]
        if d != 0:
            print(f'  {n}: v2={v2_set[n][2]}, v3={v3_set[n][2]}, delta {d:+}')

# Now find the FULL char-level diff
v2_chars = len(v2_script)
v3_chars = len(v3_script)
print(f'\nTotal v2 script: {v2_chars}, v3 script: {v3_chars}, delta {v3_chars-v2_chars:+}')

# Sum all v3 functions and see if there's leftover top-level code
v3_func_chars = sum(sz for _,_,_,sz in v3_funcs)
v2_func_chars = sum(sz for _,_,_,sz in v2_funcs)
print(f'v2 func sum: {v2_func_chars}, v3 func sum: {v3_func_chars}')
print(f'v2 non-func: {v2_chars - v2_func_chars}, v3 non-func: {v3_chars - v3_func_chars}')

# List top 10 functions with names
print('\nv3 function list (first 25):')
for n, i, e, sz in v3_funcs[:25]:
    print(f'  {sz:6d}  {n}  @{i}-{e}')
