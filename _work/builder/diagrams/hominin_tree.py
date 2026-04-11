"""Hominin phylogeny — tree diagram.

Source: BIOL 4230 Final — Human Evolution. Ardipithecus through Homo sapiens
with key dates and brain sizes. Emphasizes BIPEDALISM BEFORE BRAIN EXPANSION.
"""

from .types import make_node, make_edge, validate_diagram


def hominin_tree_diagram():
    nodes = [
        make_node(
            id='lca',
            label='LCA with chimps ~7 Mya',
            detail=(
                'The last common ancestor of humans and chimpanzees, ~7 million years ago. '
                'Not a chimp — humans did NOT evolve from modern chimps. Instead, both lineages '
                'diverged from this shared ancestor in Africa. No complete fossil found yet.'
            ),
            watchOut='"We evolved from monkeys" is wrong — we share a common ancestor with them.',
            color='gray',
        ),
        make_node(
            id='ardi',
            label='Ardipithecus (~4.4 Mya)',
            detail=(
                'Ardipithecus ramidus — partial biped, still mostly arboreal. '
                'Grasping big toe for climbing. Shows that bipedalism evolved gradually, '
                'not all at once.'
            ),
            color='amber',
        ),
        make_node(
            id='australo',
            label='Australopithecus (3–4 Mya)',
            detail=(
                'Classic early hominins. LUCY (Au. afarensis, 3.2 Mya, Hadar Ethiopia) — '
                'bipedal pelvis, ~430 cc brain (chimp-sized). Laetoli footprints (3.6 Mya) '
                'preserved bipedal gait in volcanic ash. CONFIRMS: BIPEDALISM EVOLVED BEFORE '
                'BRAIN EXPANSION.'
            ),
            mnemonic='Lucy = Australopithecus afarensis = bipedal with small brain.',
            color='amber',
        ),
        make_node(
            id='habilis',
            label='Homo habilis (~2.4 Mya)',
            detail=(
                'Earliest member of genus Homo. Name means "handy man" — associated with '
                'first stone tools (Oldowan industry). Larger brain than Australopithecus '
                '(~600 cc) but still small by later standards.'
            ),
            color='coral',
        ),
        make_node(
            id='erectus',
            label='Homo erectus (~1.9 Mya)',
            detail=(
                'First hominin to leave Africa — major out-of-Africa dispersal reaching '
                'Georgia (Dmanisi), Java, and China. Controlled fire. Longer legs, narrower '
                'pelvis — fully modern body proportions. Brain ~900 cc.'
            ),
            color='coral',
        ),
        make_node(
            id='neanderthal',
            label='Homo neanderthalensis',
            detail=(
                'Eurasian cold-adapted lineage ~400–40 kya. Stocky build, large brain (sometimes '
                'exceeding modern humans). Non-African modern humans carry ~1–4% Neanderthal DNA '
                'from interbreeding after the out-of-Africa migration ~60 kya.'
            ),
            watchOut='Neanderthals are a SISTER species, not ancestors of modern humans.',
            color='red',
        ),
        make_node(
            id='denisovan',
            label='Denisovans',
            detail=(
                'Identified from a finger bone and teeth in Denisova Cave, Siberia. Genetic '
                'relatives of Neanderthals. Melanesian and Papuan populations carry ~3–6% '
                'Denisovan DNA. High-altitude Tibetans inherited the EPAS1 hypoxia-tolerance '
                'allele from Denisovans.'
            ),
            color='red',
        ),
        make_node(
            id='sapiens',
            label='Homo sapiens (~300 kya origin)',
            detail=(
                'Modern humans. Oldest H. sapiens fossils ~300 kya (Jebel Irhoud, Morocco); '
                'modern anatomical form ~195 kya (Omo Kibish, Ethiopia). ~60 kya major '
                'out-of-Africa dispersal. Brain ~1350 cc. Only surviving Homo species.'
            ),
            mnemonic='Mitochondrial Eve ~200 kya in Africa.',
            color='green',
        ),
        make_node(
            id='floresiensis',
            label='H. floresiensis ("hobbit")',
            detail=(
                'Discovered on Flores island, Indonesia. ~1 m tall, 420 cc brain. '
                'Lived until ~50 kya. Probably the result of insular dwarfism from an earlier '
                'Homo erectus-like ancestor isolated on the island.'
            ),
            color='pink',
        ),
    ]
    edges = [
        make_edge('lca', 'ardi', style='arrow'),
        make_edge('ardi', 'australo', style='arrow'),
        make_edge('australo', 'habilis', style='arrow'),
        make_edge('habilis', 'erectus', style='arrow'),
        make_edge('erectus', 'neanderthal', style='arrow'),
        make_edge('erectus', 'denisovan', style='arrow'),
        make_edge('erectus', 'sapiens', style='arrow'),
        make_edge('erectus', 'floresiensis', style='dashed', label='insular dwarfism'),
    ]
    return validate_diagram({
        'type': 'tree',
        'title': 'Hominin Phylogeny — Bipedalism Before Brain Expansion',
        'nodes': nodes,
        'edges': edges,
        'mnemonic': 'ABLE: Ardi → Australopithecus → Bipedal → Large brain → Evolved.',
    }, node_id='hominin_tree')
