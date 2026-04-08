"""Main assembly script.

Pulls every node-generator together, assembles the final data blob, writes
data.json at project root, and rewrites both public/index_prod.html and
public/index.html with:
  1. The new JSON blob spliced into <script id="sd">...</script>
  2. The new RL sidebar-row dictionary (15 rows)
  3. An updated <title> and header tag

Run:  python build.py
"""
import json
import os
import re

from lectures_1_7    import (lec1_nodes, lec2_nodes, lec3_nodes,
                              lec4_nodes, lec5_6_nodes, lec7_nodes)
from lectures_8_13   import (lec8_nodes, lec9_nodes, lec10_11_nodes,
                              lec12_nodes, lec13_nodes)
from lectures_14_15         import lec14_nodes, lec15_nodes
from lectures_16_speciation import ch13_nodes
from final_extras           import final_extras_nodes

ROOT      = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
DATA_JSON = os.path.join(ROOT, 'data.json')
HTML_PROD = os.path.join(ROOT, 'public', 'index_prod.html')
HTML_DEV  = os.path.join(ROOT, 'public', 'index.html')

# Sidebar row labels (matches node rows exactly).
RL = {
    1:  'LEC 1 — INTRO (Ch 1)',
    2:  'LEC 2 — DARWIN (Ch 2)',
    3:  'LEC 3 — GENETICS (Ch 5)',
    4:  'LEC 4 — MICRO-EVO & HWE (Ch 6)',
    5:  'LEC 5-6 — QUANT GENETICS (Ch 7)',
    6:  'LEC 7 — SELECTION IN ACTION (Ch 8)',
    7:  'LEC 8 — ADAPTATION (Ch 10)',
    8:  'LEC 9 — COEVOLUTION (Ch 16)',
    9:  'LEC 10-11 — SEXUAL SELECTION (Ch 11)',
    10: 'LEC 12 — LIFE HISTORY (Ch 13)',
    11: 'LEC 13 — GAME THEORY & ALTRUISM (Ch 12)',
    12: 'LEC 14 — HISTORY OF LIFE (Ch 3)',
    13: 'LEC 15 — PHYLOGENETICS (Ch 4)',
    14: 'FINAL — SPECIATION & BIOGEOGRAPHY',
    15: 'FINAL — APPLICATIONS',
}


def assemble():
    """Combine every builder into the final node list."""
    all_nodes = []
    for fn in (lec1_nodes, lec2_nodes, lec3_nodes, lec4_nodes,
               lec5_6_nodes, lec7_nodes, lec8_nodes, lec9_nodes,
               lec10_11_nodes, lec12_nodes, lec13_nodes,
               lec14_nodes, lec15_nodes, ch13_nodes, final_extras_nodes):
        all_nodes.extend(fn())

    meta = {
        'title':      'Evolution Full Course Study Guide',
        'subtitle':   'All 15 Lectures | Ch 1-8, 10-14, 16-18 | Exam 1 + 2 + 3 + Final',
        'instructor': 'Dr. Travis Robbins',
        'tag':        'BIOL 4230',
    }
    return {'meta': meta, 'nodes': all_nodes}


def rl_to_js(rl):
    """Render the RL dict as a JS object literal: {1:'…',2:'…',…}."""
    parts = []
    for row in sorted(rl.keys()):
        label = rl[row].replace("'", "\\'")
        parts.append(f"{row}:'{label}'")
    return 'RL={' + ','.join(parts) + '}'


def inject(html, blob_json, rl_js):
    """Rewrite <script id="sd"> block and RL dict in-place."""
    # 1) Swap JSON blob
    html = re.sub(
        r'(<script id="sd" type="application/json">)(.*?)(</script>)',
        lambda m: m.group(1) + blob_json + m.group(3),
        html, count=1, flags=re.DOTALL,
    )
    # 2) Swap RL dict (first occurrence of RL={...})
    html = re.sub(r"RL=\{[^}]*\}", rl_js, html, count=1)
    # 3) Update <title>
    html = re.sub(
        r'<title>.*?</title>',
        '<title>Evolution Full Course Study Guide</title>',
        html, count=1,
    )
    return html


def validate(data):
    """Sanity-check node schema before writing."""
    required = {'id', 'title', 'color', 'row', 'popup', 'flashcard', 'quiz', 'visual'}
    seen_ids = set()
    for n in data['nodes']:
        missing = required - set(n.keys())
        if missing:
            raise ValueError(f"Node {n.get('id','?')} missing keys: {missing}")
        if n['id'] in seen_ids:
            raise ValueError(f"Duplicate id: {n['id']}")
        seen_ids.add(n['id'])
        if n['row'] not in RL:
            raise ValueError(f"Node {n['id']} row {n['row']} not in RL dict")
    return len(seen_ids)


def main():
    data = assemble()
    n_unique = validate(data)

    blob_json = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
    rl_js     = rl_to_js(RL)

    # 1) Write data.json
    with open(DATA_JSON, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # 2) Patch both HTML files
    for path in (HTML_PROD, HTML_DEV):
        with open(path, 'r', encoding='utf-8') as f:
            html = f.read()
        html = inject(html, blob_json, rl_js)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)

    # 3) Report
    print(f'Wrote {DATA_JSON}')
    print(f'Patched {HTML_PROD}')
    print(f'Patched {HTML_DEV}')
    print(f'Total nodes: {len(data["nodes"])} ({n_unique} unique)')
    print(f'JSON blob: {len(blob_json):,} bytes')
    print(f'RL rows: {len(RL)}')
    # By-row summary
    by_row = {}
    for n in data['nodes']:
        by_row.setdefault(n['row'], []).append(n['id'])
    print('\nNodes per row:')
    for r in sorted(by_row):
        print(f'  row {r:2d} ({len(by_row[r])}): {RL[r]}')


if __name__ == '__main__':
    main()
