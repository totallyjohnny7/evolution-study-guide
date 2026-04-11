"""Fish-to-tetrapod transition — flow diagram.

Source: BIOL 4230 Lec 16. Shubin & Daeschler 2004 (Nature) described Tiktaalik
roseae from Ellesmere Island — a Late Devonian intermediate between lobe-finned
fish and early tetrapods. The fossil was PREDICTED by phylogeny before being
discovered: the team targeted mid-Devonian coastal wetland rocks because that
is where transitional forms were expected.
"""

from .types import make_node, make_edge, validate_diagram


def tiktaalik_transition_flow_diagram():
    nodes = [
        make_node(
            id='eusthenopteron',
            label='Eusthenopteron',
            value='~385 Mya',
            detail=(
                'Lobe-finned fish with internal limb bone homologs — humerus, radius, and '
                'ulna already present in the fin skeleton. Still fully aquatic, with a '
                'streamlined fishy body and no neck.'
            ),
            color='blue',
        ),
        make_node(
            id='panderichthys',
            label='Panderichthys',
            value='~380 Mya',
            detail=(
                'More tetrapod-like than Eusthenopteron. Flattened body, eyes on top of '
                'the head — adaptations for shallow-water life where looking up is useful. '
                'Fins retain fish-like structure but body shape has shifted.'
            ),
            color='blue',
        ),
        make_node(
            id='tiktaalik',
            label='Tiktaalik roseae',
            value='~375 Mya',
            detail=(
                'Discovered 2004 on Ellesmere Island (Arctic Canada) by Shubin, Daeschler, '
                'and colleagues AFTER phylogeny PREDICTED a transitional form should exist '
                'in mid-Devonian coastal wetland rocks. Key features: weight-bearing elbows '
                'with bending wrists (could do "push-ups"), a functional NECK (the bony '
                'operculum is lost so the head moves independently of the shoulder girdle), '
                'lateral-line system preserved, and fins still with webbing rather than digits.'
            ),
            mnemonic='phylogeny → prediction → dig the right rocks → find the fossil',
            color='green',
        ),
        make_node(
            id='acanthostega',
            label='Acanthostega',
            value='~365 Mya',
            detail=(
                'Early tetrapod with 8 digits per limb — not 5. Pentadactyly is a later '
                'canalization, not an ancestral rule. Still mostly aquatic; the limbs were '
                'useful in shallow vegetation-choked water, not for walking on land.'
            ),
            color='teal',
        ),
        make_node(
            id='ichthyostega',
            label='Ichthyostega',
            value='~360 Mya',
            detail=(
                'More terrestrial than Acanthostega but still strongly aquatic. Stocky '
                'overlapping ribcage could briefly support body weight on land. Hind '
                'limbs resemble paddles more than walking feet.'
            ),
            color='teal',
        ),
        make_node(
            id='early_tetrapod',
            label='Fully terrestrial tetrapods',
            value='>350 Mya',
            detail=(
                'Lineage leading eventually to amphibians, reptiles (including birds), '
                'and mammals. The transition from fin to limb was not a single leap but '
                'a stepwise accumulation of features over tens of millions of years.'
            ),
            color='amber',
        ),
        make_node(
            id='science_works',
            label='Phylogeny predicted, fieldwork confirmed',
            detail=(
                'The Tiktaalik story is a canonical demonstration of how evolutionary '
                'biology makes testable predictions. Shubin\'s team used the existing '
                'phylogeny and the geologic record to decide where (Ellesmere Island) '
                'and when (Late Devonian) to dig — and the prediction held.'
            ),
            watchOut=(
                'Tiktaalik is NOT a direct ancestor — it is a COUSIN preserving '
                'transitional anatomy. "Missing link" is a misleading phrase; many '
                'transitional forms exist and the lineage is a bush, not a ladder.'
            ),
            color='purple',
        ),
    ]
    edges = [
        make_edge('eusthenopteron', 'panderichthys', label='385→380 Mya, flattens', style='arrow'),
        make_edge('panderichthys', 'tiktaalik', label='380→375 Mya, gains neck', style='arrow'),
        make_edge('tiktaalik', 'acanthostega', label='375→365 Mya, fin→limb', style='arrow'),
        make_edge('acanthostega', 'ichthyostega', label='365→360 Mya, weight-bearing ribs', style='arrow'),
        make_edge('ichthyostega', 'early_tetrapod', label='>350 Mya, walks on land', style='arrow'),
        make_edge('tiktaalik', 'science_works', label='predictive success', style='dashed'),
    ]
    return validate_diagram({
        'type': 'flow',
        'title': 'Fish-to-Tetrapod Transition — The Tiktaalik Story',
        'nodes': nodes,
        'edges': edges,
        'mnemonic': 'Eusthenopteron → Panderichthys → Tiktaalik → Acanthostega → Ichthyostega → tetrapods.',
    }, node_id='tiktaalik_transition_flow')
