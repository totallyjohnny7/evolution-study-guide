"""Inspect data.json to see node shape after enrich_v3."""
import json, sys, io
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f'Nodes: {len(data["nodes"])}')
print()

n = data['nodes'][0]
print(f'Sample node[0] title: {n.get("title")}')
print(f'Top-level keys: {sorted(n.keys())}')
print()

# Check shapes
print(f'node.quiz type: {type(n.get("quiz")).__name__}')
if isinstance(n.get('quiz'), list):
    print(f'  quiz len: {len(n["quiz"])}')
elif isinstance(n.get('quiz'), dict):
    print(f'  quiz keys: {sorted(n["quiz"].keys())}')
print(f'node.flashcard type: {type(n.get("flashcard")).__name__}')
if isinstance(n.get('flashcard'), dict):
    print(f'  flashcard keys: {sorted(n["flashcard"].keys())}')
print(f'node.visual present: {"visual" in n}')
if 'visual' in n:
    v = n['visual']
    print(f'  visual keys: {sorted(v.keys()) if isinstance(v, dict) else type(v).__name__}')
    if isinstance(v, dict) and 'svg' in v:
        print(f'  visual.svg length: {len(v["svg"])}')
print(f'node.popup present: {"popup" in n}')
if 'popup' in n:
    p = n['popup']
    if isinstance(p, dict):
        print(f'  popup keys: {sorted(p.keys())}')
print(f'node.v2 present: {"v2" in n}')
if 'v2' in n:
    v2 = n['v2']
    print(f'  v2 keys: {sorted(v2.keys())}')
    if 'quiz' in v2:
        print(f'  v2.quiz type: {type(v2["quiz"]).__name__}')
        if isinstance(v2['quiz'], list):
            print(f'  v2.quiz len: {len(v2["quiz"])}')
    if 'flashcards' in v2:
        print(f'  v2.flashcards type: {type(v2["flashcards"]).__name__}')
        if isinstance(v2['flashcards'], list):
            print(f'  v2.flashcards len: {len(v2["flashcards"])}')
    if 'svg' in v2:
        print(f'  v2.svg length: {len(v2["svg"])}')
    if 'transcript' in v2:
        t = v2['transcript']
        print(f'  v2.transcript type: {type(t).__name__}, len: {len(t) if hasattr(t, "__len__") else "?"}')
print()

# Aggregate across all nodes
quiz_list_cnt = sum(1 for n in data['nodes'] if isinstance(n.get('quiz'), list))
quiz_dict_cnt = sum(1 for n in data['nodes'] if isinstance(n.get('quiz'), dict))
quiz_none_cnt = sum(1 for n in data['nodes'] if n.get('quiz') is None)
print(f'Across 57 nodes:')
print(f'  node.quiz as list: {quiz_list_cnt}')
print(f'  node.quiz as dict: {quiz_dict_cnt}')
print(f'  node.quiz missing: {quiz_none_cnt}')

v2_quiz_total = sum(len(n.get('v2', {}).get('quiz', [])) for n in data['nodes'])
v2_fc_total = sum(len(n.get('v2', {}).get('flashcards', [])) for n in data['nodes'])
v2_svg_cnt = sum(1 for n in data['nodes'] if n.get('v2', {}).get('svg'))
v2_trans_cnt = sum(1 for n in data['nodes'] if n.get('v2', {}).get('transcript'))

print(f'  v2.quiz total items: {v2_quiz_total}')
print(f'  v2.flashcards total items: {v2_fc_total}')
print(f'  nodes with v2.svg: {v2_svg_cnt}')
print(f'  nodes with v2.transcript: {v2_trans_cnt}')

# Check visual
visual_cnt = sum(1 for n in data['nodes'] if n.get('visual'))
visual_svg_cnt = sum(1 for n in data['nodes']
                    if isinstance(n.get('visual'), dict) and n['visual'].get('svg'))
print(f'  nodes with visual: {visual_cnt}')
print(f'  nodes with visual.svg: {visual_svg_cnt}')
