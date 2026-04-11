"""Find JS syntax issues in the injected HTML."""
import re, sys, io
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('public/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

scripts = re.findall(r'<script(?![^>]*src)(?![^>]*application/json)[^>]*>(.*?)</script>', html, re.DOTALL)
for i, s in enumerate(scripts):
    if 'function rMap' in s or 'function rSheet' in s:
        print(f'Script #{i}: {len(s)} chars')
        print('  Has rV2:', 'function rV2(' in s)
        print('  Has rSheet:', 'function rSheet(' in s)
        print('  Has rMap:', 'function rMap(' in s)
        print('  Has rVis:', 'function rVis(' in s)
        # Check brace depth
        depth = 0
        in_str = False
        sc = None
        bs = False
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
                elif c == '}':
                    depth -= 1
        print('  Final brace depth:', depth)

        # Find any "else" not preceded by "}" (suggests broken if)
        # Look for "else if(S.mode" specifically (the dispatch line)
        idx = s.find("else if(S.mode==='cards')")
        if idx >= 0:
            print(f'  Dispatch line context @ {idx}:')
            print('  ', s[max(0,idx-100):idx+200])
        # Find an isolated "else"
        for m in re.finditer(r'(?<![a-zA-Z0-9_$\)\}])else(?![a-zA-Z0-9_$])', s):
            ctx = s[max(0,m.start()-30):m.end()+30]
            # Skip if it's "} else" or ") else" or normal pattern
            if not re.search(r'[\)\}]\s*$', s[max(0,m.start()-3):m.start()]):
                print(f'  ISOLATED else @ {m.start()}: ...{ctx}...')
        break
