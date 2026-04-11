"""r-selected vs K-selected life history — compare diagram (BIOL 4230 Lec 12)."""

from .types import make_node, make_edge, validate_diagram


def r_vs_k_compare_diagram():
    nodes = [
        # Column headers
        make_node(
            id='r_title',
            label='r-selected (fast lane)',
            detail=(
                'Selection maximizes intrinsic growth rate r. Thrives when the '
                'population sits BELOW carrying capacity so density-independent '
                'mortality dominates. Unstable, disturbed, or unpredictable '
                'environments reward this strategy.'
            ),
            mnemonic='r = rabbits — live fast, die young.',
            watchOut='r is a population growth parameter; the strategy is defined by the ENVIRONMENT (below K), not offspring count alone.',
            color='coral',
        ),
        make_node(
            id='k_title',
            label='K-selected (slow lane)',
            detail=(
                'Selection maximizes competitive ability at carrying capacity K. '
                'Stable, predictable environments at density-dependent equilibrium '
                'reward heavy investment per offspring.'
            ),
            mnemonic='K = K-apes — slow and steady.',
            watchOut='K-selected does NOT mean "smart" or "advanced." It means competitive at K.',
            color='teal',
        ),

        # Row 1 — Offspring
        make_node(
            id='r_offspring',
            label='Many small cheap offspring',
            detail=(
                'Produce enormous numbers of tiny offspring with almost no '
                'energy invested per individual. A single mayfly female lays '
                'hundreds to thousands of eggs. Most die; a few survive by luck.'
            ),
            mnemonic='quantity beats quality',
            color='coral',
        ),
        make_node(
            id='k_offspring',
            label='Few large expensive offspring',
            detail=(
                'Produce a small number of large, well-provisioned offspring. '
                'Kiwi lays one egg that is ~20% of the female\'s body mass. '
                'African elephants produce one calf every 4-5 years.'
            ),
            mnemonic='quality beats quantity',
            color='teal',
        ),

        # Row 2 — Parental care
        make_node(
            id='r_parental',
            label='Minimal parental care',
            detail=(
                'Zero or near-zero investment after laying/birth. Energy saved '
                'is re-routed into producing more offspring. Offspring survive '
                'or die based on luck, not parenting.'
            ),
            color='coral',
        ),
        make_node(
            id='k_parental',
            label='Heavy prolonged parental care',
            detail=(
                'Extended parenting, defense, and teaching. Human childhood is '
                '~18 years — the most extreme case. Offspring survival depends '
                'on continuous parental investment.'
            ),
            color='teal',
        ),

        # Row 3 — Maturation
        make_node(
            id='r_maturation',
            label='Early maturation',
            detail=(
                'Reach reproductive age quickly. Critical under high extrinsic '
                'mortality — if you will probably die young, reproduce first. '
                'Mice mature in ~6 weeks.'
            ),
            color='coral',
        ),
        make_node(
            id='k_maturation',
            label='Late maturation',
            detail=(
                'Slow growth and delayed reproduction. Bristlecone pines take '
                'decades; elephants reach maturity at 10-12 years. Low extrinsic '
                'mortality makes waiting a viable strategy.'
            ),
            color='teal',
        ),

        # Row 4 — Lifespan
        make_node(
            id='r_lifespan',
            label='Short lifespan; often semelparous',
            detail=(
                'One reproductive event then death (semelparous), or short '
                'iteroparous life. Aging is fast because selection on late-life '
                'traits is weak under high extrinsic mortality.'
            ),
            color='coral',
        ),
        make_node(
            id='k_lifespan',
            label='Long lifespan; iteroparous',
            detail=(
                'Reproduce repeatedly over many years. Bristlecone pines live '
                '>4000 years. Iteroparity is favored when adult survival is high '
                'and single reproductive events are risky.'
            ),
            color='teal',
        ),

        # Row 5 — Environment
        make_node(
            id='r_environment',
            label='Unstable variable environment; below K',
            detail=(
                'Disturbance-prone, unpredictable, density-independent mortality '
                'dominates. Population usually sits below carrying capacity, so '
                'rapid growth pays off.'
            ),
            color='coral',
        ),
        make_node(
            id='k_environment',
            label='Stable environment; competitive at K',
            detail=(
                'Predictable, saturated, density-dependent mortality dominates. '
                'Competition for limited resources at carrying capacity favors '
                'competitive ability over raw reproductive rate.'
            ),
            watchOut=(
                'r/K is a CONTINUUM, not a binary. r and K are population growth '
                'parameters — the strategy is about ENVIRONMENT, not just '
                'offspring number.'
            ),
            color='teal',
        ),

        # Examples
        make_node(
            id='r_example',
            label='r-selected examples',
            detail=(
                'Mayflies, mice, weeds, rabbits, dandelions, cane toads, '
                'most insects, bacteria. Short generations, boom-and-bust '
                'population dynamics.'
            ),
            value='mayflies, mice, weeds, rabbits',
            color='coral',
        ),
        make_node(
            id='k_example',
            label='K-selected examples',
            detail=(
                'Elephants, humans, bristlecone pine, kiwi, albatross, '
                'whales, redwoods. Long generations, stable population '
                'dynamics at carrying capacity.'
            ),
            value='elephants, humans, bristlecone pine, kiwi',
            color='teal',
        ),

        # Empirical evidence
        make_node(
            id='reznick_guppy',
            label='Reznick guppy transplant',
            detail=(
                '11 years: Trinidad guppies from high-predation pools were '
                'transplanted to low-predation streams. The transplanted '
                'populations evolved LATER maturation and LARGER offspring — '
                'a measurable r-to-K shift in 11 years of natural selection.'
            ),
            mnemonic='11 years = evolution in real time',
            color='amber',
        ),
        make_node(
            id='austad_opossum',
            label='Austad opossum study',
            detail=(
                'Mainland Virginia opossums (high predation) vs Sapelo Island, '
                'Georgia opossums (5000 years isolated, no predators). Island '
                'opossums age significantly slower — senescence evolved in just '
                '5000 years under relaxed predation.'
            ),
            mnemonic='no predators → slower aging',
            color='amber',
        ),
    ]

    edges = [
        make_edge('r_title', 'r_offspring', label='trait 1', style='arrow'),
        make_edge('k_title', 'k_offspring', label='trait 1', style='arrow'),
        make_edge('r_offspring', 'r_parental', label='trait 2', style='arrow'),
        make_edge('k_offspring', 'k_parental', label='trait 2', style='arrow'),
        make_edge('r_parental', 'r_maturation', label='trait 3', style='arrow'),
        make_edge('k_parental', 'k_maturation', label='trait 3', style='arrow'),
        make_edge('r_maturation', 'r_lifespan', label='trait 4', style='arrow'),
        make_edge('k_maturation', 'k_lifespan', label='trait 4', style='arrow'),
        make_edge('r_lifespan', 'r_environment', label='trait 5', style='arrow'),
        make_edge('k_lifespan', 'k_environment', label='trait 5', style='arrow'),
        make_edge('r_environment', 'r_example', label='examples', style='dashed'),
        make_edge('k_environment', 'k_example', label='examples', style='dashed'),
        make_edge('r_example', 'reznick_guppy', label='field test', style='dashed'),
        make_edge('k_example', 'austad_opossum', label='field test', style='dashed'),
    ]

    return validate_diagram({
        'type': 'compare',
        'title': 'r-selected vs K-selected Life History Strategies',
        'nodes': nodes,
        'edges': edges,
        'mnemonic': 'r = rabbits. K = K-apes. Live fast die young, or slow and steady.',
    }, node_id='r_vs_k_compare')
