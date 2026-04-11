"""Reproductive isolation barriers — prezygotic through postzygotic — timeline diagram."""

from .types import make_node, make_edge, validate_diagram


def reproductive_isolation_timeline_diagram():
    # x = progress through the reproductive sequence
    # 0 = before encounter, 1 = after hybrid offspring mature

    nodes = [
        make_node(
            id='habitat',
            label='Habitat isolation',
            detail=(
                'Populations use different habitats and rarely encounter each '
                'other. Rhagoletis pomonella: apple race vs hawthorn race are '
                'diverging in SYMPATRY because they never meet on the same '
                'host plant.'
            ),
            mnemonic='different addresses',
            x=0.05,
            color='purple',
        ),
        make_node(
            id='temporal',
            label='Temporal isolation',
            detail=(
                'Populations reproduce at different times. Coral mass-spawning '
                'events are synchronized to species-specific windows (minutes '
                'to hours apart). Spring-breeding vs fall-breeding salamanders.'
            ),
            mnemonic='different clocks',
            x=0.12,
            color='purple',
        ),
        make_node(
            id='behavioral',
            label='Behavioral isolation',
            detail=(
                'Species-specific courtship signals fail between species. '
                'Firefly species use unique flash patterns (flash duration, '
                'interval, color). Bird song differences between sister '
                'species. Laupala cricket pulse rates.'
            ),
            mnemonic='different songs',
            x=0.20,
            color='purple',
        ),
        make_node(
            id='mechanical',
            label='Mechanical isolation',
            detail=(
                'Reproductive structures are physically incompatible. Duck '
                'penis/vagina coevolution is a classic example. Damselfly '
                'males have species-specific abdominal appendages that fit '
                'only conspecific female thoracic plates.'
            ),
            mnemonic='wrong key wrong lock',
            x=0.28,
            color='purple',
        ),
        make_node(
            id='gametic',
            label='Gametic isolation',
            detail=(
                'Gametes meet but fail to fuse. Sea urchin sperm express '
                'BINDIN protein that matches only the species-specific VERL '
                'receptor on conspecific eggs. Rapid coevolution between '
                'sperm and egg recognition proteins.'
            ),
            mnemonic='right sperm, right egg',
            x=0.40,
            color='purple',
        ),
        make_node(
            id='zygote_form',
            label='Zygote forms',
            value='prezygotic | postzygotic',
            detail=(
                'Boundary between prezygotic barriers (everything above) and '
                'postzygotic barriers (everything below). Once a zygote '
                'forms, isolation depends on hybrid fitness.'
            ),
            x=0.50,
            color='gray',
        ),
        make_node(
            id='coyne_orr',
            label='Coyne & Orr pattern',
            value='prezygotic faster',
            detail=(
                'Coyne & Orr (1989, 1997) analyzed Drosophila sister species: '
                'prezygotic isolation evolves FASTER than postzygotic in '
                'sympatry than in allopatry. The explanation is reinforcement — '
                'selection against unfit hybrids favors prezygotic barriers.'
            ),
            mnemonic='reinforcement in sympatry',
            x=0.50,
            y=0.85,
            color='teal',
        ),
        make_node(
            id='hybrid_inviability',
            label='Hybrid inviability',
            detail=(
                'F1 hybrid zygotes form but die during development. Mimulus '
                'Hms1/Hms2 Bateson-Dobzhansky-Muller incompatibility kills '
                'hybrid seedlings — two alleles that evolved separately in '
                'parent lineages are lethal in combination.'
            ),
            mnemonic='hybrid dies',
            x=0.62,
            color='coral',
        ),
        make_node(
            id='hybrid_sterility',
            label='Hybrid sterility',
            detail=(
                'F1 hybrids survive but cannot reproduce. Mule: horse '
                '(64 chromosomes) × donkey (62) = mule (63). Meiosis fails '
                'because unpaired chromosomes cannot segregate properly, '
                'producing non-viable gametes.'
            ),
            mnemonic='mule is sterile',
            x=0.78,
            color='coral',
        ),
        make_node(
            id='hybrid_breakdown',
            label='Hybrid breakdown',
            detail=(
                'F1 hybrids are viable and fertile, but F2 or backcross '
                'generations collapse. Recombination in F2 exposes BDM '
                'incompatibilities that were masked in F1 heterozygotes.'
            ),
            mnemonic='F2 crash',
            watchOut=(
                'Prezygotic barriers come first in TIME (before zygote), but '
                'evolutionarily either type can arise first. Reinforcement '
                'preferentially strengthens PREZYGOTIC in sympatry.'
            ),
            x=0.92,
            color='coral',
        ),
    ]

    edges = [
        make_edge('habitat', 'temporal', label='next barrier', style='arrow'),
        make_edge('temporal', 'behavioral', label='next barrier', style='arrow'),
        make_edge('behavioral', 'mechanical', label='next barrier', style='arrow'),
        make_edge('mechanical', 'gametic', label='next barrier', style='arrow'),
        make_edge('gametic', 'zygote_form', label='zygote line', style='arrow'),
        make_edge('zygote_form', 'hybrid_inviability', label='postzygotic begins', style='arrow'),
        make_edge('hybrid_inviability', 'hybrid_sterility', label='next barrier', style='arrow'),
        make_edge('hybrid_sterility', 'hybrid_breakdown', label='next barrier', style='arrow'),
        make_edge('coyne_orr', 'zygote_form', label='sympatry bias', style='dashed'),
    ]

    return validate_diagram({
        'type': 'timeline',
        'title': 'Reproductive Isolation Barriers — Prezygotic to Postzygotic',
        'nodes': nodes,
        'edges': edges,
        'mnemonic': 'Pre-mating → post-mating prezygotic → postzygotic. Each layer blocks gene flow at a different stage.',
    }, node_id='reproductive_isolation_timeline')
