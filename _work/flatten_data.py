"""Flatten v2.* arrays into legacy fields that the v2 renderer already reads.

Pivot strategy: instead of rewriting the renderer, reshape the data.
- node.quiz        = node.v2.quiz  (list of 4) - initQ already does Array.isArray
- node.visual.svg  = node.v2.svg                - rVis already reads n.visual.svg
- node.flashcard   = node.v2.flashcards[0]      - legacy singular retained
                                                  (initC will be patched to
                                                   prefer v2.flashcards array)
"""
import json
import sys
import io

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for n in data['nodes']:
    v2 = n.get('v2') or {}

    # 1. Quiz: promote v2.quiz (list) to legacy node.quiz
    if isinstance(v2.get('quiz'), list) and v2['quiz']:
        n['quiz'] = v2['quiz']

    # 2. Visual: graft v2.svg onto existing visual dict
    if v2.get('svg'):
        if not isinstance(n.get('visual'), dict):
            n['visual'] = {}
        n['visual']['svg'] = v2['svg']
        # Ensure 'type' exists for the badge in rVis
        if 'type' not in n['visual']:
            n['visual']['type'] = 'Diagram'

    # 3. Flashcard: keep singular legacy field = first v2 flashcard
    fcs = v2.get('flashcards')
    if isinstance(fcs, list) and fcs:
        n['flashcard'] = fcs[0]

# Write back
out = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
with open('data.json', 'w', encoding='utf-8') as f:
    f.write(out)

# Verify
counts = {
    'nodes': len(data['nodes']),
    'quiz_as_list': sum(1 for n in data['nodes'] if isinstance(n.get('quiz'), list)),
    'quiz_items_total': sum(len(n['quiz']) for n in data['nodes']
                            if isinstance(n.get('quiz'), list)),
    'visual_svg': sum(1 for n in data['nodes']
                      if isinstance(n.get('visual'), dict) and n['visual'].get('svg')),
    'flashcard_singular': sum(1 for n in data['nodes']
                              if isinstance(n.get('flashcard'), dict)),
    'v2_transcript_nodes': sum(1 for n in data['nodes']
                               if n.get('v2', {}).get('transcript')),
}
size_kb = len(out) / 1024
print('Flatten complete:')
for k, v in counts.items():
    print(f'  {k}: {v}')
print(f'  data.json size: {size_kb:.1f} KB')
