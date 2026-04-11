"""Lightweight JS/CSS minifier used to inject EvoDiagram assets into index.html."""
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BACKSLASH = chr(92)


def mini_css(s):
    s = re.sub(r'/\*.*?\*/', '', s, flags=re.DOTALL)
    s = re.sub(r'\s+', ' ', s)
    s = re.sub(r'\s*([{}:;,])\s*', r'\1', s)
    s = s.replace(';}', '}')
    return s.strip()


def mini_js(s):
    # Strip /* ... */ block comments
    s = re.sub(r'/\*[\s\S]*?\*/', '', s)
    # Strip // line comments (naive state machine that skips strings)
    out_lines = []
    for line in s.split('\n'):
        in_str = False
        qch = None
        cut = None
        i = 0
        while i < len(line):
            ch = line[i]
            if in_str:
                if ch == BACKSLASH:
                    i += 2
                    continue
                if ch == qch:
                    in_str = False
            else:
                if ch == '"' or ch == "'":
                    in_str = True
                    qch = ch
                elif ch == '/' and i + 1 < len(line) and line[i + 1] == '/':
                    cut = i
                    break
            i += 1
        if cut is not None:
            line = line[:cut]
        out_lines.append(line)
    s = '\n'.join(out_lines)
    s = re.sub(r'\n\s*', ' ', s)
    s = re.sub(r'  +', ' ', s)
    return s.strip()


if __name__ == '__main__':
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, 'evo_diagram.js'), encoding='utf-8') as fh:
        js_src = fh.read()
    with open(os.path.join(here, 'evo_diagram.css'), encoding='utf-8') as fh:
        css_src = fh.read()
    js_mini = mini_js(js_src)
    css_mini = mini_css(css_src)
    print('JS:', len(js_src), '->', len(js_mini))
    print('CSS:', len(css_src), '->', len(css_mini))
    with open(os.path.join(here, 'evo_diagram.min.js'), 'w', encoding='utf-8') as fh:
        fh.write(js_mini)
    with open(os.path.join(here, 'evo_diagram.min.css'), 'w', encoding='utf-8') as fh:
        fh.write(css_mini)
    print('wrote evo_diagram.min.js and evo_diagram.min.css')
