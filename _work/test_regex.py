"""Test the inject_v3 regexes against v2 baseline."""
import sys, io, subprocess, re
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

res = subprocess.run(['git', 'show', '54d1a8e:public/index.html'],
                     capture_output=True, text=True, encoding='utf-8')
html = res.stdout

# Test rV2 removal
m = re.search(r'function rV2\(ct,n\)\{.*?ct\.appendChild\(panel\);\}', html, re.DOTALL)
print('rV2 removal regex:')
if m:
    print(f'  matched: chars {m.start()}-{m.end()} ({m.end()-m.start()} chars)')
    matched = m.group()
    print(f'  starts: {matched[:100]}')
    print(f'  ends: ...{matched[-100:]}')
else:
    print('  no match')
print()

# Test rSheet removal
m = re.search(r'function rSheet\(ct\)\{.*?ct\.appendChild\(wrap\);\}', html, re.DOTALL)
print('rSheet removal regex:')
if m:
    print(f'  matched: chars {m.start()}-{m.end()} ({m.end()-m.start()} chars)')
    matched = m.group()
    print(f'  starts: {matched[:100]}')
    print(f'  ends: ...{matched[-100:]}')
    # Check brace balance of what's matched
    d = 0; in_str = False; sc = None; bs = False
    for c in matched:
        if bs: bs=False; continue
        if in_str:
            if c=='\\': bs=True; continue
            if c==sc: in_str=False
        else:
            if c in "'\"`": in_str=True; sc=c
            elif c=='{': d += 1
            elif c=='}': d -= 1
    print(f'  brace balance of matched: {d:+}')
else:
    print('  no match')
print()

# Also test the second rV2 cleanup regex
m = re.search(
    r'function rV2\(ct,n\)\{var v=n\.v2;var nc=NC\[n\.color\]\|\|NC\.gray;.*?\}\}\}\}',
    html, re.DOTALL
)
print('rV2 secondary regex (the messy {}}}}):')
if m:
    print(f'  matched: chars {m.start()}-{m.end()} ({m.end()-m.start()} chars)')
    print(f'  ends: ...{m.group()[-100:]}')
else:
    print('  no match')
