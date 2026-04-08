"""Final-exam extras: species concepts, biogeography, conservation, human evo,
evolutionary medicine. These were in the original study guide and cover
material from chapters the core 1-15 lecture deck didn't fully duplicate,
so we keep them verbatim and reassign them to the final-exam rows (14 and 15).
"""
import json, os

EXISTING_PATH = os.path.join(
    os.path.dirname(__file__), '..', '..', '_extracted_data.json'
)

# IDs we want to keep (history-of-life and phylogenetics are REPLACED
# by the new lecture-based Lec 14 and Lec 15 nodes).
KEEP_IDS = {
    # 'species-concepts' is replaced by the richer ch13_nodes() in lectures_16_speciation.py
    'biogeography-extinction',
    'conservation',
    'human-evolution',
    'evolutionary-medicine',
}

# New row assignments for the final-exam rail
ROW_REASSIGN = {
    'biogeography-extinction':14,
    'conservation':           15,
    'human-evolution':        15,
    'evolutionary-medicine':  15,
}


def final_extras_nodes():
    with open(EXISTING_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    nodes = []
    for n in data['nodes']:
        if n['id'] not in KEEP_IDS:
            continue
        n['row'] = ROW_REASSIGN[n['id']]
        nodes.append(n)
    return nodes


if __name__ == '__main__':
    ns = final_extras_nodes()
    print(f'Extracted {len(ns)} final-exam extra nodes:')
    for n in ns:
        print(f'  - {n["id"]} (row {n["row"]}, color {n["color"]})')
