"""Garter snake vs rough-skinned newt — cycle diagram (antagonistic coevolution)."""

from .types import make_node, make_edge, validate_diagram


def garter_snake_newt_arms_race_diagram():
    nodes = [
        make_node(
            id='newt_ttx',
            label='Newt produces TTX',
            detail=(
                'Taricha granulosa, the rough-skinned newt, secretes tetrodotoxin (TTX) from '
                'granular skin glands. TTX is one of the most potent neurotoxins known — it '
                'blocks voltage-gated sodium channels in nerve and muscle cells, causing paralysis '
                'and death in nearly all predators.'
            ),
            value='tetrodotoxin',
            mnemonic='Newt skin = sodium-channel blocker.',
            color='amber',
        ),
        make_node(
            id='snake_dies',
            label='Snake death from TTX',
            detail=(
                'In most populations, a western garter snake (Thamnophis sirtalis) that eats a '
                'TTX-loaded newt becomes paralyzed and dies. TTX is so potent that a single newt '
                'can carry enough to kill dozens of adult humans, let alone a snake.'
            ),
            mnemonic='Newt eats snake dies.',
            color='red',
        ),
        make_node(
            id='resistant_snake',
            label='TTX-resistant Na+ channel',
            detail=(
                'Thamnophis sirtalis populations exposed to toxic newts evolved amino-acid '
                'substitutions in the pore of their voltage-gated sodium channel gene (SCN4A) '
                'that prevent TTX from binding. Sometimes a single mutation confers major '
                'resistance; stacking a few produces extreme resistance.'
            ),
            mnemonic='One mutation, big resistance jump.',
            color='teal',
        ),
        make_node(
            id='cost_to_snake',
            label='Cost: slower snake',
            detail=(
                'Edmund Brodie Jr. and Edmund Brodie III showed that highly TTX-resistant snakes '
                'crawl more slowly than their non-resistant relatives — the modified sodium channel '
                'conducts less efficiently, reducing muscle performance. Resistance is not free.'
            ),
            mnemonic='Tough skin, slow snake.',
            watchOut='Arms races are NOT infinitely escalating — physiological costs on both sides limit escalation.',
            color='gray',
        ),
        make_node(
            id='newt_escalates',
            label='Newt escalates TTX dose',
            detail=(
                'Selection now favors newts that produce even more TTX, because resistant snakes '
                'still successfully eat moderately toxic newts. Higher doses in turn select for '
                'even more resistant snakes, closing the reciprocal coevolutionary loop.'
            ),
            mnemonic='Deadlier newts drive tougher snakes drive deadlier newts.',
            color='coral',
        ),
    ]
    edges = [
        make_edge('newt_ttx', 'snake_dies', label='ingesting kills most predators', style='arrow'),
        make_edge('snake_dies', 'resistant_snake', label='selects for resistance', style='arrow'),
        make_edge('resistant_snake', 'cost_to_snake', label='resistance carries a cost', style='arrow'),
        make_edge('cost_to_snake', 'newt_escalates', label='cost limits but does not stop race', style='arrow'),
        make_edge('newt_escalates', 'newt_ttx', label='cycle repeats with higher TTX', style='arrow'),
    ]
    return validate_diagram({
        'type': 'cycle',
        'title': 'Garter Snake vs Rough-Skinned Newt — Antagonistic Coevolution',
        'nodes': nodes,
        'edges': edges,
        'mnemonic': 'Arms race: each side escalates and pays costs. Thompson\'s Geographic Mosaic — hotspots + coldspots + gene flow = variable outcomes across the range.',
    }, node_id='garter_snake_newt_arms_race')
