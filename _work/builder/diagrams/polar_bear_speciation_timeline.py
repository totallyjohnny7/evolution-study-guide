"""Polar bear vs brown bear divergence — Lorenzen & Liu 2014 APOB — timeline."""

from .types import make_node, make_edge, validate_diagram


def polar_bear_speciation_timeline_diagram():
    nodes = [
        make_node(
            id='common_ancestor',
            label='Common ancestor',
            detail=(
                'The shared brown bear / polar bear ancestor lived in '
                'northern Eurasia ~500 kya. It was a generalist temperate '
                'bear, not specialized for Arctic life.'
            ),
            mnemonic='single ancestral bear',
            x=0.0,
            color='gray',
        ),
        make_node(
            id='divergence',
            label='Initial divergence',
            value='479-343 kya',
            detail=(
                'Brown bear (Ursus arctos) and polar bear (Ursus maritimus) '
                'lineages split between ~479 and ~343 kya during a glacial '
                'period. The polar bear lineage was pushed into coastal '
                'Arctic habitats where sea ice and seals became key resources.'
            ),
            mnemonic='glacial isolation',
            x=0.15,
            color='blue',
        ),
        make_node(
            id='arctic_niche',
            label='Arctic niche specialization',
            detail=(
                'Polar bears adapt to seal-hunting on sea ice: white coat '
                '(translucent hollow hairs over black skin), webbed partially '
                'elongated feet for swimming, small ears, thick blubber, '
                'and a diet dominated by seal fat.'
            ),
            mnemonic='white, webbed, warm',
            x=0.30,
            color='blue',
        ),
        make_node(
            id='apob_selection',
            label='APOB gene positive selection',
            value='cholesterol binding',
            detail=(
                'Lorenzen et al. 2014 and Liu et al. 2014 identified strong '
                'positive selection on the APOB gene (apolipoprotein B). '
                'APOB encodes a protein that binds cholesterol and packages '
                'it into lipoproteins. Polar bears eat seal blubber — an '
                'extremely high-cholesterol diet that would cause '
                'cardiovascular disease in brown bears or humans — without '
                'developing atherosclerosis.'
            ),
            mnemonic='seal fat without heart disease',
            x=0.45,
            color='teal',
        ),
        make_node(
            id='interglacial_contact',
            label='Interglacial contact zones',
            detail=(
                'During warm interglacial periods brown bears expand north '
                'and polar bears come ashore, producing contact zones. '
                'Occasional hybridization produces "pizzly" or "grolar" '
                'bears, documented both in the fossil record and in '
                'present-day Arctic Canada.'
            ),
            mnemonic='pizzly bears',
            x=0.60,
            color='amber',
        ),
        make_node(
            id='one_way_gene_flow',
            label='One-way gene flow',
            detail=(
                'Genomic analysis (Liu et al. 2014) shows gene flow has been '
                'detected primarily FROM brown bears INTO polar bears during '
                'warming periods. Yet polar bears remain phenotypically, '
                'behaviorally, and ecologically distinct.'
            ),
            mnemonic='brown → polar introgression',
            x=0.75,
            color='coral',
        ),
        make_node(
            id='present_day',
            label='Distinct species today',
            value='reproductive + phenotypic',
            detail=(
                'Despite ongoing introgression, polar bears are '
                'phenotypically, behaviorally, and ecologically distinct. '
                'Divergence is MAINTAINED by strong divergent selection on '
                'Arctic-specific traits (APOB, coat color, body shape) — '
                'selection outpaces the homogenizing effect of gene flow.'
            ),
            watchOut=(
                'Gene flow does NOT automatically collapse species — strong '
                'divergent selection can maintain distinctness even with '
                'ongoing introgression.'
            ),
            x=0.95,
            color='green',
        ),
    ]

    edges = [
        make_edge('common_ancestor', 'divergence', label='~500 kya', style='arrow'),
        make_edge('divergence', 'arctic_niche', label='ice selection', style='arrow'),
        make_edge('arctic_niche', 'apob_selection', label='fat diet', style='arrow'),
        make_edge('apob_selection', 'interglacial_contact', label='warm periods', style='arrow'),
        make_edge('interglacial_contact', 'one_way_gene_flow', label='hybridization', style='arrow'),
        make_edge('one_way_gene_flow', 'present_day', label='selection wins', style='arrow'),
    ]

    return validate_diagram({
        'type': 'timeline',
        'title': 'Polar Bear Speciation — Divergence, APOB Selection, and Gene Flow',
        'nodes': nodes,
        'edges': edges,
        'mnemonic': 'Polar bears diverged ~400 kya, under APOB selection for fat diet. Gene flow continues but selection keeps them distinct.',
    }, node_id='polar_bear_speciation_timeline')
