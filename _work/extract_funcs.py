"""Extract specific JS functions from the minified HTML by bracket-matching."""
import re
import os
import sys
import io

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
HTML = os.path.join(ROOT, 'public', 'index_prod.html')

with open(HTML, 'r', encoding='utf-8') as f:
    html = f.read()

def extract_function(src, needle):
    """Starting from `needle`, find the matching closing brace for the function body."""
    idx = src.find(needle)
    if idx < 0:
        return None
    # Find the first { after needle
    start = src.find('{', idx)
    if start < 0:
        return None
    depth = 0
    i = start
    in_str = False
    str_ch = None
    while i < len(src):
        c = src[i]
        if in_str:
            if c == '\\':
                i += 2
                continue
            if c == str_ch:
                in_str = False
        else:
            if c in "'\"`":
                in_str = True
                str_ch = c
            elif c == '{':
                depth += 1
            elif c == '}':
                depth -= 1
                if depth == 0:
                    return src[idx:i+1]
        i += 1
    return None

targets = [
    'function initC(',
    'function initQ(',
    'function rCards(',
    'function rQuiz(',
    'function rVis(',
    'function rSheet(',
    'function rV2(',
    'function rMap(',
]

for t in targets:
    fn = extract_function(html, t)
    if fn:
        print(f'=== {t} ({len(fn)} chars) ===')
        # Print first 1500 and last 400 if too long
        if len(fn) > 2000:
            print(fn[:1500])
            print('... [snip] ...')
            print(fn[-400:])
        else:
            print(fn)
        print()
    else:
        print(f'=== {t} NOT FOUND ===')
        print()
