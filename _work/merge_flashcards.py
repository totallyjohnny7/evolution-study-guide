#!/usr/bin/env python3
"""Merge flashcard batch files into data.json"""
import json, os, sys, glob

PROJ = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) if '__file__' in dir() else r'C:\Users\johnn\Desktop\evolution-study-guide'
WORK = os.path.join(PROJ, '_work')
DATA = os.path.join(PROJ, 'data.json')

# Load data.json
with open(DATA, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Load all batch files
all_cards = {}
batch_files = sorted(glob.glob(os.path.join(WORK, 'cards_batch*.json')))
print(f"Found {len(batch_files)} batch files")

for bf in batch_files:
    print(f"  Loading {os.path.basename(bf)}...")
    try:
        with open(bf, 'r', encoding='utf-8') as f:
            batch = json.load(f)
        for node_id, cards in batch.items():
            if node_id not in all_cards:
                all_cards[node_id] = []
            all_cards[node_id].extend(cards)
        print(f"    -> {sum(len(v) for v in batch.values())} cards across {len(batch)} nodes")
    except Exception as e:
        print(f"    ERROR: {e}")

# Inject flashcards into data.json nodes
total_cards = 0
node_counts = []
for node in data['nodes']:
    nid = node['id']
    if nid in all_cards:
        cards = all_cards[nid]
        # Ensure v2 object exists
        if 'v2' not in node:
            node['v2'] = {}
        node['v2']['flashcards'] = cards
        total_cards += len(cards)
        node_counts.append((nid, node['title'], len(cards)))
    else:
        # Keep existing single flashcard as fallback
        existing = 1 if node.get('flashcard', {}).get('front') else 0
        total_cards += existing
        node_counts.append((nid, node['title'], existing))
        print(f"  WARNING: No batch cards for {nid}")

# Write updated data.json
with open(DATA, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)

# Print summary table
print(f"\n{'='*70}")
print(f"FLASHCARD SUMMARY")
print(f"{'='*70}")
print(f"{'Lecture':<12} {'Node':<45} {'Cards':>6}")
print(f"{'-'*12} {'-'*45} {'-'*6}")
for nid, title, count in node_counts:
    lec = nid.split('-')[0]
    print(f"{lec:<12} {title[:45]:<45} {count:>6}")
print(f"{'-'*12} {'-'*45} {'-'*6}")
print(f"{'TOTAL':<12} {'':<45} {total_cards:>6}")
print(f"\nNodes with cards: {sum(1 for _,_,c in node_counts if c > 0)}/{len(node_counts)}")
