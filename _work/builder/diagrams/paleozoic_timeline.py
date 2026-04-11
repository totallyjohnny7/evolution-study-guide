"""Paleozoic era timeline — Cambrian through Permian with mass extinctions."""

from .types import make_node, make_edge, validate_diagram


def paleozoic_timeline_diagram():
    # x mapping: 0 = 542 Mya (start Cambrian), 1 = 252 Mya (end Permian)
    # x = (542 - mya) / (542 - 252) = (542 - mya) / 290

    nodes = [
        make_node(
            id='cambrian',
            label='Cambrian 542-488 Mya',
            value='Age of diversification',
            detail=(
                'The Cambrian Explosion — nearly all modern animal body plans '
                'appear in a ~20 Myr window. Burgess Shale (505 Mya, British '
                'Columbia) lagerstätte preserves Anomalocaris, Hallucigenia, '
                'Opabinia — over 65,000 specimens and ~93 species documented. '
                'First chordates (Haikouichthys, 520 Mya). Trilobites dominate '
                'shallow seas.'
            ),
            mnemonic='COME — Cambrian',
            watchOut='"Cambrian Explosion" is millions of years long, not instantaneous.',
            x=0.10,
            color='purple',
        ),
        make_node(
            id='ordovician',
            label='Ordovician 488-444 Mya',
            value='Early bony fishes',
            detail=(
                'First land plants (~475 Mya, mosses and liverwort-like forms). '
                'Marine diversification continues — brachiopods, cephalopods, '
                'early jawless fish. Ended with Gondwana glaciation driving '
                'sea level drop and a mass extinction of ~85% of marine species.'
            ),
            mnemonic='OVER — Ordovician',
            x=0.23,
            color='blue',
        ),
        make_node(
            id='ordovician_ext',
            label='End-Ordovician extinction',
            value='~444 Mya, ~85% marine spp',
            detail=(
                '2nd-largest mass extinction in Earth history by species loss. '
                'Caused by Gondwana glaciation → sea level drop → loss of '
                'shallow shelf habitats. Brachiopods and graptolites hit hard.'
            ),
            x=0.34,
            color='red',
        ),
        make_node(
            id='silurian',
            label='Silurian 444-416 Mya',
            value='First jawed fish',
            detail=(
                'First vascular plants (Cooksonia-like, with xylem and phloem). '
                'First land animals — arthropods including millipede Pneumodesmus '
                'at 428 Mya. First jawed fish (Gnathostomata) diversify. '
                'Continued post-Ordovician marine recovery.'
            ),
            mnemonic='SOME — Silurian',
            x=0.38,
            color='teal',
        ),
        make_node(
            id='devonian',
            label='Devonian 416-359 Mya',
            value='Age of Fishes',
            detail=(
                'Fishes dominate the oceans. 380 Mya Dunkleosteus — a 6-meter '
                'armored placoderm predator. 385 Mya first tree-like plants '
                '(Wattieza ~8 m tall). 375 Mya Tiktaalik, discovered 2004 on '
                'Ellesmere Island by Shubin & Daeschler — classic '
                '"fishapod" tetrapod transition. 370 Mya first true tetrapod fossils.'
            ),
            mnemonic='DAY — Devonian; Dunkleosteus',
            x=0.48,
            color='amber',
        ),
        make_node(
            id='devonian_ext',
            label='Late Devonian extinction',
            value='~372 Mya Kellwasser/Hangenberg',
            detail=(
                'A series of pulses (Kellwasser, Hangenberg events). Marine '
                'invertebrates hit hardest — coral reefs devastated and did '
                'not recover to comparable scale for ~100 Myr.'
            ),
            x=0.56,
            color='red',
        ),
        make_node(
            id='mississippian',
            label='Mississippian 359-323 Mya',
            value='Amphibian diversification',
            detail=(
                'First half of the Carboniferous. Amphibians (labyrinthodonts) '
                'diversify on land. Widespread shallow seas with extensive '
                'limestone deposition. Precursor to the great coal-swamp '
                'ecosystems of the Pennsylvanian.'
            ),
            mnemonic='MAYBE — Mississippian',
            x=0.63,
            color='green',
        ),
        make_node(
            id='pennsylvanian',
            label='Pennsylvanian 323-299 Mya',
            value='Age of Amphibians',
            detail=(
                'Vast coal-swamp forests. Lignin had evolved in plants, but '
                'fungi could not yet digest it — dead wood did not decay and '
                'was buried en masse, forming most of the world\'s coal. '
                'Atmospheric O2 reached ~35% (vs today\'s 21%) → GIANT INSECTS '
                'such as Meganeura dragonflies with 70 cm wingspans. First '
                'AMNIOTIC EGG evolved — decoupling reproduction from water.'
            ),
            mnemonic='PICKING — Pennsylvanian; giant dragonflies',
            x=0.75,
            color='green',
        ),
        make_node(
            id='permian',
            label='Permian 299-252 Mya',
            value='Synapsid/sauropsid split',
            detail=(
                'First true reptiles diversify. Pangaea is fully assembled. '
                'The amniote lineage splits into SYNAPSIDS (mammal ancestors, '
                'one temporal fenestra) and SAUROPSIDS (reptile/bird ancestors). '
                'Ends with the largest mass extinction in Earth history.'
            ),
            mnemonic='UP — Permian',
            x=0.88,
            color='pink',
        ),
        make_node(
            id='permian_ext',
            label="End-Permian 'Great Dying'",
            value='~252 Mya, ~96% species',
            detail=(
                'Largest mass extinction in the fossil record — ~96% of marine '
                'and ~70% of terrestrial vertebrate species wiped out. Driver: '
                'Siberian Traps flood basalt volcanism → CO2 release → global '
                'warming, ocean acidification, and marine anoxia. Ecosystem '
                'recovery took 5-10 Myr.'
            ),
            watchOut=(
                'Synapsid is NOT a reptile. Synapsids are a SEPARATE amniote '
                'lineage from sauropsids; "mammal-like reptile" is outdated.'
            ),
            x=1.0,
            color='red',
        ),
    ]

    edges = [
        make_edge('cambrian', 'ordovician', label='→ 488 Mya', style='arrow'),
        make_edge('ordovician', 'ordovician_ext', label='glaciation', style='arrow'),
        make_edge('ordovician_ext', 'silurian', label='recovery', style='arrow'),
        make_edge('silurian', 'devonian', label='→ 416 Mya', style='arrow'),
        make_edge('devonian', 'devonian_ext', label='Kellwasser', style='arrow'),
        make_edge('devonian_ext', 'mississippian', label='recovery', style='arrow'),
        make_edge('mississippian', 'pennsylvanian', label='→ 323 Mya', style='arrow'),
        make_edge('pennsylvanian', 'permian', label='→ 299 Mya', style='arrow'),
        make_edge('permian', 'permian_ext', label='Siberian Traps', style='arrow'),
    ]

    return validate_diagram({
        'type': 'timeline',
        'title': 'Paleozoic Era Timeline — 542 to 252 Mya',
        'nodes': nodes,
        'edges': edges,
        'mnemonic': "Robbins' 'COME OVER SOME DAY MAYBE PICKING UP HARD CASH' — Cambrian through Cretaceous.",
    }, node_id='paleozoic_timeline')
