"""Speciation modes — allopatric, parapatric, sympatric, allopolyploidy — compare."""

from .types import make_node, make_edge, validate_diagram


def speciation_modes_compare_diagram():
    nodes = [
        # Column headers
        make_node(
            id='allo_title',
            label='Allopatric speciation',
            detail=(
                'Populations are split by a physical barrier that prevents '
                'any gene flow. They diverge through drift and independent '
                'selection. Most common and least controversial mode.'
            ),
            mnemonic='ALLO = other place',
            color='blue',
        ),
        make_node(
            id='para_title',
            label='Parapatric speciation',
            detail=(
                'Populations span an environmental gradient with reduced but '
                'nonzero gene flow. Strong divergent selection across the '
                'gradient can drive speciation despite ongoing contact.'
            ),
            mnemonic='PARA = alongside',
            color='teal',
        ),
        make_node(
            id='symp_title',
            label='Sympatric speciation',
            detail=(
                'Populations diverge within the SAME geographic area with no '
                'physical barrier. Requires strong disruptive selection, '
                'often mediated by ecological or host specialization.'
            ),
            mnemonic='SYM = together',
            color='coral',
        ),
        make_node(
            id='polyploid_title',
            label='Allopolyploidy',
            detail=(
                'Hybridization followed by whole-genome duplication produces '
                'a fertile polyploid that is reproductively isolated from '
                'both parent species — in a single generation.'
            ),
            mnemonic='POLY = many (genomes)',
            color='purple',
        ),

        # Row 1: Barrier type
        make_node(
            id='allo_barrier',
            label='Barrier: complete geographic',
            detail=(
                'A mountain range, river, glacier, or land bridge completely '
                'separates populations. No individuals cross during divergence.'
            ),
            color='blue',
        ),
        make_node(
            id='para_barrier',
            label='Barrier: environmental gradient',
            detail=(
                'A smooth environmental transition (e.g., soil metal '
                'concentration, elevation, temperature). Populations stay in '
                'contact but experience different selection pressures.'
            ),
            color='teal',
        ),
        make_node(
            id='symp_barrier',
            label='Barrier: none (ecological)',
            detail=(
                'No geographic or gradient separation. Divergence is driven '
                'by disruptive selection on an ecological trait (host plant, '
                'diet, mating preference).'
            ),
            color='coral',
        ),
        make_node(
            id='polyploid_barrier',
            label='Barrier: chromosome number',
            detail=(
                'Hybrid offspring of the polyploid cannot pair chromosomes '
                'with either parent species → instant reproductive isolation '
                'by karyotype mismatch.'
            ),
            color='purple',
        ),

        # Row 2: Gene flow
        make_node(
            id='allo_flow',
            label='Gene flow: zero',
            detail=(
                'No migrants move between populations during the divergence '
                'period. Evolution proceeds completely independently.'
            ),
            color='blue',
        ),
        make_node(
            id='para_flow',
            label='Gene flow: reduced but nonzero',
            detail=(
                'Some gene flow continues across the gradient, but is '
                'counteracted by strong divergent selection at the ends.'
            ),
            color='teal',
        ),
        make_node(
            id='symp_flow',
            label='Gene flow: potentially high',
            detail=(
                'Individuals could mate freely but do not because of '
                'assortative mating tied to ecology. Gene flow is high unless '
                'disruptive selection is very strong.'
            ),
            color='coral',
        ),
        make_node(
            id='polyploid_flow',
            label='Gene flow: zero (instant)',
            detail=(
                'Reproductive isolation is complete at the moment the '
                'polyploid forms. No further gene flow with parent species.'
            ),
            color='purple',
        ),

        # Row 3: Example
        make_node(
            id='allo_example',
            label='Example: Isthmus of Panama shrimp',
            detail=(
                'Nancy Knowlton sampled snapping shrimp (Alpheus) on both '
                'sides of the Isthmus of Panama after it closed ~3 Mya. '
                'Sister species across the isthmus no longer interbreed — '
                'a natural experiment in allopatric speciation.'
            ),
            color='blue',
        ),
        make_node(
            id='para_example',
            label='Example: grass on mine tailings',
            detail=(
                'Agrostis populations on heavy-metal mine spoils evolved '
                'tolerance and diverged from adjacent non-tolerant '
                'populations despite continuous contact and wind pollination.'
            ),
            color='teal',
        ),
        make_node(
            id='symp_example',
            label='Example: Rhagoletis pomonella',
            detail=(
                'Apple maggot fly. Ancestral population feeds on hawthorn; '
                'after apples were introduced to North America, a new race '
                'shifted to apple hosts. Host plant fidelity reduces gene '
                'flow — an ongoing sympatric speciation event.'
            ),
            color='coral',
        ),
        make_node(
            id='polyploid_example',
            label='Example: Tragopogon mirus, bread wheat',
            detail=(
                'Tragopogon mirus formed in the US Pacific Northwest less '
                'than 100 years ago by allopolyploidy from T. dubius × T. '
                'pratensis. Bread wheat (Triticum aestivum) is a hexaploid '
                'allopolyploid combining THREE diploid genomes.'
            ),
            color='purple',
        ),

        # Row 4: Speed
        make_node(
            id='allo_speed',
            label='Speed: gradual (1000s to millions of yr)',
            detail=(
                'Divergence accumulates slowly through drift and selection. '
                'Classic examples require geological time scales.'
            ),
            color='blue',
        ),
        make_node(
            id='para_speed',
            label='Speed: moderate',
            detail=(
                'Faster than allopatric if selection is strong, slower than '
                'sympatric because gene flow counteracts divergence.'
            ),
            color='teal',
        ),
        make_node(
            id='symp_speed',
            label='Speed: requires strong disruptive selection',
            detail=(
                'Can be fast if ecological opportunity and disruptive '
                'selection are extreme; otherwise gene flow overwhelms '
                'divergence.'
            ),
            color='coral',
        ),
        make_node(
            id='polyploid_speed',
            label='Speed: INSTANT (one generation)',
            detail=(
                'Reproductive isolation is established in the generation in '
                'which chromosome doubling occurs. The fastest documented '
                'mode of speciation.'
            ),
            color='purple',
        ),

        # Row 5: Controversy
        make_node(
            id='allo_controversy',
            label='Controversy: MOST COMMON, uncontroversial',
            detail=(
                'Accepted as the default mode of speciation for nearly all '
                'animal groups. Large body of evidence from biogeography.'
            ),
            color='blue',
        ),
        make_node(
            id='para_controversy',
            label='Controversy: accepted, less studied',
            detail=(
                'Accepted as a theoretical mode and documented in plants and '
                'a few animals. Harder to prove in practice because it '
                'requires measuring reduced gene flow in the face of contact.'
            ),
            color='teal',
        ),
        make_node(
            id='symp_controversy',
            label='Controversy: CONTROVERSIAL',
            detail=(
                'Historically resisted because gene flow is expected to '
                'homogenize populations. Now accepted with solid examples '
                '(Rhagoletis, cichlids in crater lakes), but each case '
                'requires rigorous demonstration.'
            ),
            color='coral',
        ),
        make_node(
            id='polyploid_controversy',
            label='Controversy: documented in animals too',
            detail=(
                'Often mis-taught as "plants only." Polyploidy IS most '
                'common in plants, but is documented in gray tree frogs, '
                'some fish, lizards, and even a few mammals.'
            ),
            watchOut=(
                'Allopolyploidy is NOT plant-only. Rare but real in insects, '
                'frogs, fish, lizards, and a few mammals.'
            ),
            color='purple',
        ),
    ]

    edges = [
        make_edge('allo_title', 'allo_barrier', label='row 1', style='arrow'),
        make_edge('para_title', 'para_barrier', label='row 1', style='arrow'),
        make_edge('symp_title', 'symp_barrier', label='row 1', style='arrow'),
        make_edge('polyploid_title', 'polyploid_barrier', label='row 1', style='arrow'),
        make_edge('allo_barrier', 'allo_flow', label='row 2', style='arrow'),
        make_edge('para_barrier', 'para_flow', label='row 2', style='arrow'),
        make_edge('symp_barrier', 'symp_flow', label='row 2', style='arrow'),
        make_edge('polyploid_barrier', 'polyploid_flow', label='row 2', style='arrow'),
        make_edge('allo_flow', 'allo_example', label='row 3', style='arrow'),
        make_edge('para_flow', 'para_example', label='row 3', style='arrow'),
        make_edge('symp_flow', 'symp_example', label='row 3', style='arrow'),
        make_edge('polyploid_flow', 'polyploid_example', label='row 3', style='arrow'),
        make_edge('allo_example', 'allo_speed', label='row 4', style='arrow'),
        make_edge('para_example', 'para_speed', label='row 4', style='arrow'),
        make_edge('symp_example', 'symp_speed', label='row 4', style='arrow'),
        make_edge('polyploid_example', 'polyploid_speed', label='row 4', style='arrow'),
        make_edge('allo_speed', 'allo_controversy', label='row 5', style='arrow'),
        make_edge('para_speed', 'para_controversy', label='row 5', style='arrow'),
        make_edge('symp_speed', 'symp_controversy', label='row 5', style='arrow'),
        make_edge('polyploid_speed', 'polyploid_controversy', label='row 5', style='arrow'),
    ]

    return validate_diagram({
        'type': 'compare',
        'title': 'Modes of Speciation — Allopatric vs Parapatric vs Sympatric vs Allopolyploidy',
        'nodes': nodes,
        'edges': edges,
        'mnemonic': 'APPLE = Allopatric + Parapatric + Polyploidy + Lateral (ecological) + Extra (sympatric).',
    }, node_id='speciation_modes_compare')
