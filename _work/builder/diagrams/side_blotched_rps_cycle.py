"""Side-blotched lizard rock-paper-scissors — cycle diagram (Sinervo & Lively 1996)."""

from .types import make_node, make_edge, validate_diagram


def side_blotched_rps_cycle_diagram():
    nodes = [
        make_node(
            id='orange',
            label='Orange morph',
            detail=(
                'Ultra-aggressive Uta stansburiana males. Hold large territories containing '
                'multiple females. Orange throats + high testosterone + large body size. They '
                'overpower smaller blue males by brute force and take over their territories.'
            ),
            mnemonic='Orange = ultra-dominant bully.',
            color='coral',
        ),
        make_node(
            id='orange_beats_blue',
            label='Orange beats Blue',
            detail=(
                'Orange males, bigger and more aggressive, displace mate-guarding blue males '
                'from their single-female territories and take over their matings. When Blue is '
                'common, Orange spreads.'
            ),
            mnemonic='Rock smashes scissors.',
            color='gray',
        ),
        make_node(
            id='yellow',
            label='Yellow morph',
            detail=(
                'Sneaker strategy. Yellow-throated males mimic female coloration and behavior, '
                'allowing them to slip into the edges of an orange male\'s harem unnoticed. They '
                'do not fight — they circumvent. Orange cannot guard a large territory perfectly, '
                'so yellows steal matings.'
            ),
            mnemonic='Yellow = female-mimicking sneaker.',
            color='amber',
        ),
        make_node(
            id='yellow_beats_orange',
            label='Yellow beats Orange',
            detail=(
                'Orange males cannot simultaneously guard every female in their large territory. '
                'Yellow sneakers take advantage of this gap, fertilizing females while Orange is '
                'busy elsewhere. When Orange is common, Yellow spreads.'
            ),
            mnemonic='Paper covers rock.',
            color='gray',
        ),
        make_node(
            id='blue',
            label='Blue morph',
            detail=(
                'Mate-guarder. Blue-throated males defend a SINGLE female very intensively, '
                'patrolling a small territory and driving off intruders. Because blue pairs are '
                'small and vigilant, sneakers have little room to operate.'
            ),
            mnemonic='Blue = vigilant mate-guarder.',
            color='blue',
        ),
        make_node(
            id='blue_beats_yellow',
            label='Blue beats Yellow',
            detail=(
                'A blue male watching his single mate will detect a skulking yellow sneaker and '
                'drive him away. Small, concentrated defense defeats the sneaker strategy. When '
                'Yellow is common, Blue spreads.'
            ),
            mnemonic='Scissors cut paper.',
            color='gray',
        ),
        make_node(
            id='cycle_info',
            label='~6-year RPS cycle',
            detail=(
                'Sinervo & Lively 1996 Nature tracked morph frequencies in a California population '
                'for ~12 years and found a rock-paper-scissors cycle with period of roughly 6 years. '
                'Each morph rises and falls in turn, chased by the morph that beats it. No stable '
                'equilibrium exists.'
            ),
            value='Sinervo & Lively 1996',
            mnemonic='Rock-Paper-Scissors maintains all three via negative frequency-dependent selection.',
            watchOut='NONE of these strategies is an ESS alone — frequency-dependent selection maintains all three.',
            color='purple',
        ),
    ]
    edges = [
        make_edge('orange', 'orange_beats_blue', label='overpowers', style='arrow'),
        make_edge('orange_beats_blue', 'blue', label='blue crashes', style='dashed'),
        make_edge('yellow', 'yellow_beats_orange', label='sneaks past', style='arrow'),
        make_edge('yellow_beats_orange', 'orange', label='orange crashes', style='dashed'),
        make_edge('blue', 'blue_beats_yellow', label='detects and evicts', style='arrow'),
        make_edge('blue_beats_yellow', 'yellow', label='yellow crashes', style='dashed'),
        make_edge('cycle_info', 'orange', label='~6 yr period', style='dashed'),
        make_edge('cycle_info', 'yellow', label='~6 yr period', style='dashed'),
        make_edge('cycle_info', 'blue', label='~6 yr period', style='dashed'),
    ]
    return validate_diagram({
        'type': 'cycle',
        'title': 'Side-Blotched Lizard Rock-Paper-Scissors (Sinervo & Lively 1996)',
        'nodes': nodes,
        'edges': edges,
        'mnemonic': 'Orange > Blue > Yellow > Orange. No stable equilibrium; all three persist via NFDS.',
    }, node_id='side_blotched_rps_cycle')
