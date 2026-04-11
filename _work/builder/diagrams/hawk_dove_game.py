"""Hawk-Dove game and ESS — matrix diagram.

Source: BIOL 4230 Lec 11. Maynard Smith & Price 1973 "The logic of animal
conflict" (Nature). First formal application of game theory to evolution.
V = value of contested resource, C = cost of injury in escalated fight.
"""

from .types import make_node, make_edge, validate_diagram


def hawk_dove_game_diagram():
    nodes = [
        # Row headers (row player)
        make_node(
            id='row_Hawk',
            label='Row: Hawk',
            detail=(
                'Row player adopts the Hawk strategy — always escalates and is willing '
                'to fight until injured or the opponent retreats.'
            ),
            color='red',
        ),
        make_node(
            id='row_Dove',
            label='Row: Dove',
            detail=(
                'Row player adopts the Dove strategy — displays but never escalates. '
                'Retreats immediately if the opponent attacks.'
            ),
            color='teal',
        ),
        # Column headers (col player)
        make_node(
            id='col_Hawk',
            label='Col: Hawk',
            detail=(
                'Column player adopts the Hawk strategy — always escalates.'
            ),
            color='red',
        ),
        make_node(
            id='col_Dove',
            label='Col: Dove',
            detail=(
                'Column player adopts the Dove strategy — displays only.'
            ),
            color='teal',
        ),
        # Matrix cells — payoffs to the row player
        make_node(
            id='HvH',
            label='Hawk vs Hawk',
            value='(V-C)/2',
            detail=(
                'Both escalate. One wins the resource V, one gets injured at cost C, '
                'and each outcome is equally likely → expected payoff is (V - C) / 2. '
                'Negative when C > V (the cost of losing a fight exceeds the prize).'
            ),
            color='red',
        ),
        make_node(
            id='HvD',
            label='Hawk vs Dove',
            value='V',
            detail=(
                'Hawk attacks, Dove retreats immediately. Hawk takes the full resource '
                'with no cost. This is the best-case payoff for Hawk — and the basis for '
                'why Hawks always invade a pure-Dove population.'
            ),
            color='amber',
        ),
        make_node(
            id='DvH',
            label='Dove vs Hawk',
            value='0',
            detail=(
                'Dove displays then immediately retreats when the opponent escalates. '
                'No resource gained, but also no injury. The floor payoff of the game.'
            ),
            color='gray',
        ),
        make_node(
            id='DvD',
            label='Dove vs Dove',
            value='V/2',
            detail=(
                'Both display. The resource is shared (or won at random), yielding '
                'expected payoff V / 2 per player with no cost. A cooperative outcome '
                'that is nonetheless unstable against invasion by Hawks.'
            ),
            color='teal',
        ),
        # Standalone concept nodes
        make_node(
            id='mixed_ess',
            label='Mixed ESS',
            detail=(
                'When C > V (injury cost exceeds resource value), neither pure Hawk nor '
                'pure Dove is an evolutionarily stable strategy. The population stabilizes '
                'at a mixed equilibrium with Hawk frequency p = V / C. Below p*, Hawks do '
                'better and increase; above p*, Hawks do worse and decline.'
            ),
            mnemonic='evolutionary stability = cannot be invaded',
            watchOut=(
                'An ESS is not necessarily the highest-fitness outcome — it is the '
                'strategy STABLE against invasion. A pure-Dove population would have higher '
                'mean payoff but is not an ESS.'
            ),
            color='purple',
        ),
        make_node(
            id='maynard_smith',
            label='Maynard Smith & Price 1973',
            detail=(
                'Published in Nature. First formal application of game theory to '
                'evolutionary biology and the founding paper of evolutionary game theory. '
                'Introduced the ESS concept: a strategy that, if adopted by most of the '
                'population, cannot be invaded by any alternative.'
            ),
            color='blue',
        ),
    ]
    edges = [
        make_edge('row_Hawk', 'HvH', label='vs Hawk'),
        make_edge('row_Hawk', 'HvD', label='vs Dove'),
        make_edge('row_Dove', 'DvH', label='vs Hawk'),
        make_edge('row_Dove', 'DvD', label='vs Dove'),
        make_edge('col_Hawk', 'HvH', style='dashed'),
        make_edge('col_Hawk', 'DvH', style='dashed'),
        make_edge('col_Dove', 'HvD', style='dashed'),
        make_edge('col_Dove', 'DvD', style='dashed'),
        make_edge('HvH', 'mixed_ess', label='when C > V'),
        make_edge('maynard_smith', 'mixed_ess', label='formalized', style='arrow'),
    ]
    return validate_diagram({
        'type': 'matrix',
        'title': 'Hawk-Dove Game and the Mixed ESS',
        'nodes': nodes,
        'edges': edges,
        'mnemonic': 'Hawk vs Dove: mixed ESS when C > V. Hawks win when rare, lose when common.',
    }, node_id='hawk_dove_game')
