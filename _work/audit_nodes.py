"""Phase 1 audit: score all nodes against the new 5-slot Lecture-Notes schema.
No writes. Output: scorecard + per-row breakdown + 3 sample nodes.
"""
import json
import sys
from collections import defaultdict

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

DATA = 'C:/Users/johnn/Desktop/evolution-study-guide/data.json'

with open(DATA, 'r', encoding='utf-8') as f:
    data = json.load(f)

nodes = data['nodes']
print(f'Source: {DATA}')
print(f'Title:  {data["meta"]["title"]}')
print(f'Subtit: {data["meta"]["subtitle"]}')
print()

# ----- score every node ------------------------------------------------------
scores = []
for n in nodes:
    popup    = n.get('popup', {})
    sections = popup.get('sections', [])
    subtitle = n.get('subtitle', '').strip()

    has_title = bool(n.get('title'))

    # Definition: any subtitle present OR a section labelled "definition"
    has_def = bool(subtitle)
    for sec in sections:
        if 'definition' in sec.get('label', '').lower():
            has_def = True
            break

    # >=4 terms: count bolded **term** patterns OR a vocab section
    bold_count = 0
    for sec in sections:
        body = sec.get('body', '')
        bold_count += body.count('**') // 2
    has_terms = bold_count >= 4
    if not has_terms:
        for sec in sections:
            lab = sec.get('label', '').lower()
            if any(k in lab for k in ('vocab', 'key term', 'glossary', 'definition')):
                has_terms = True
                break

    has_mnem = bool(popup.get('mnemonic'))

    warnings = popup.get('warnings', [])
    has_trap = isinstance(warnings, list) and len(warnings) > 0

    has_audio = any('LECTURE AUDIO' in sec.get('label', '') for sec in sections)

    scores.append({
        'id': n['id'],
        'row': n.get('row', 0),
        'has_title':     has_title,
        'has_def':       has_def,
        'has_4_terms':   has_terms,
        'bold_count':    bold_count,
        'has_mnem':      has_mnem,
        'has_trap':      has_trap,
        'has_audio':     has_audio,
        'sections_n':    len(sections),
    })

# ----- per-node scorecard ---------------------------------------------------
print('=== PER-NODE SCORECARD  (Y=present  .=missing) ===')
print(f'{"id":<34} {"row":<3} {"T":<2} {"D":<2} {"#bold":<6} {"4t":<3} {"M":<2} {"X":<2} {"Aud":<4} {"secs":<4}')
print('-' * 72)
Y = lambda b: 'Y' if b else '.'
for s in scores:
    print(f'{s["id"][:34]:<34} {s["row"]:<3} '
          f'{Y(s["has_title"]):<2} {Y(s["has_def"]):<2} '
          f'{s["bold_count"]:<6} {Y(s["has_4_terms"]):<3} '
          f'{Y(s["has_mnem"]):<2} {Y(s["has_trap"]):<2} '
          f'{Y(s["has_audio"]):<4} {s["sections_n"]:<4}')

# ----- totals ---------------------------------------------------------------
total = len(scores)
print()
print('=== TOTALS ===')
print(f'nodes_total:           {total}')
print(f'has_title:             {sum(s["has_title"]   for s in scores)}/{total}')
print(f'has_clear_definition:  {sum(s["has_def"]     for s in scores)}/{total}')
print(f'has_>=4_terms:         {sum(s["has_4_terms"] for s in scores)}/{total}')
print(f'has_mnemonic:          {sum(s["has_mnem"]    for s in scores)}/{total}')
print(f'has_exam_trap:         {sum(s["has_trap"]    for s in scores)}/{total}')
print(f'has_lecture_audio:     {sum(s["has_audio"]   for s in scores)}/{total}')

# ----- per-row breakdown ---------------------------------------------------
RL = {
     1: 'Lec1  Intro',         2: 'Lec2  Darwin',
     3: 'Lec3  Genetics',      4: 'Lec4  MicroEvo & HWE',
     5: 'Lec5-6 QuantGen',     6: 'Lec7  Selection',
     7: 'Lec8  Adaptation',    8: 'Lec9  Coevolution',
     9: 'Lec10-11 SexSel',    10: 'Lec12 LifeHist',
    11: 'Lec13 Game/Altru',   12: 'Lec14 HistoryOfLife',
    13: 'Lec15 Phylogenetics',14: 'FINAL Spec/Biogeo',
    15: 'FINAL Applications',
}
print()
print('=== BY LECTURE ROW ===')
by_row = defaultdict(list)
for s in scores:
    by_row[s['row']].append(s)
for r in sorted(by_row.keys()):
    rs = by_row[r]; n = len(rs)
    print(f'row {r:2} ({RL[r]:<22}) n={n:2} | '
          f'T={sum(s["has_title"]   for s in rs)} '
          f'D={sum(s["has_def"]     for s in rs)} '
          f'4t={sum(s["has_4_terms"] for s in rs)} '
          f'M={sum(s["has_mnem"]    for s in rs)} '
          f'X={sum(s["has_trap"]    for s in rs)} '
          f'Aud={sum(s["has_audio"] for s in rs)}')
