"""Merge V2 distillations into data.json (additive, non-destructive).

Reads:
  data.json (project root)            <- existing 57 nodes
  _work/builder/v2_distillations.py   <- new 5-slot content

Writes:
  data.json (overwritten in place)

For each node we add the following NEW top-level fields (if absent
or if --force is set):
    lecture        int 1..17
    lectureTitle   str
    order          int 1..N
    chapter        str  e.g. 'Ch 5'
    slideRange     str  e.g. '14-30'
    v2             dict (definition / keyTerms / mnemonic / examTrap / actions)

Existing fields (popup, quiz, flashcard, visual, subtitle, title,
color, row, id) are preserved untouched. The renderer will read v2
when present and fall back to popup otherwise.
"""
import json
import os
import sys
import io

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'builder'))
from v2_distillations import V2

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA = os.path.join(ROOT, 'data.json')

with open(DATA, 'r', encoding='utf-8') as f:
    data = json.load(f)

existing_ids = {n['id'] for n in data['nodes']}
v2_ids = set(V2.keys())

missing_in_v2 = existing_ids - v2_ids
missing_in_data = v2_ids - existing_ids
if missing_in_v2:
    print(f'ERROR: nodes in data.json but missing from V2: {sorted(missing_in_v2)}')
    sys.exit(1)
if missing_in_data:
    print(f'ERROR: V2 entries with no matching node in data.json: {sorted(missing_in_data)}')
    sys.exit(1)

# Merge
patched = 0
for node in data['nodes']:
    nid = node['id']
    src = V2[nid]
    node['lecture']      = src['lecture']
    node['lectureTitle'] = src['lectureTitle']
    node['order']        = src['order']
    node['chapter']      = src['chapter']
    node['slideRange']   = src['slideRange']
    node['v2']           = src['v2']
    patched += 1

# Update meta to reflect refactor
data['meta']['v2Schema']    = '5-slot Lecture-Notes (definition/keyTerms/mnemonic/examTrap/actions)'
data['meta']['v2Generated'] = '2026-04-06'
data['meta']['lectureCount'] = 17

with open(DATA, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'Patched {patched}/{len(data["nodes"])} nodes with v2 + lecture metadata')
print(f'Wrote {DATA}')

# Quick by-lecture summary
by_lec = {}
for node in data['nodes']:
    by_lec.setdefault(node['lecture'], []).append(node['id'])
print()
print('By lecture:')
for lec in sorted(by_lec):
    sample = by_lec[lec][0]
    title = next((n['lectureTitle'] for n in data['nodes'] if n['id'] == sample), '')
    print(f'  Lec {lec:2d} ({title}): {len(by_lec[lec])} nodes')
