"""Sperm competition strategies under polyandry — compare diagram.

Source: BIOL 4230 Lec 11. Polyandry (females mating with multiple males) creates
post-copulatory selection on males. Four strategies emerge, each with empirical
support. Sexual conflict drives rapid antagonistic coevolution.
"""

from .types import make_node, make_edge, validate_diagram


def sperm_competition_strategies_diagram():
    nodes = [
        # Strategy 1: Remove rival sperm
        make_node(
            id='strat_remove',
            label='Remove rival sperm',
            detail=(
                'Physically evict or destroy sperm from previous males. Morphological '
                'weapons on the genitalia scrape, scoop, or displace sperm already '
                'stored in the female reproductive tract.'
            ),
            mnemonic='Scrape before you score.',
            color='coral',
        ),
        make_node(
            id='ex_remove',
            label='Seed beetle penile spines',
            detail=(
                'Callosobruchus maculatus males have hardened penile spines that damage the '
                'female reproductive tract while scraping out rival sperm. Causes harm to the '
                'female — a canonical sexual conflict system.'
            ),
            color='coral',
        ),
        # Strategy 2: Out-produce rivals
        make_node(
            id='strat_outproduce',
            label='Out-produce rivals',
            detail=(
                'Numerical advantage: more sperm from you = higher fertilization share. '
                'Drives the evolution of enlarged testes relative to body mass in species '
                'with high polyandry.'
            ),
            mnemonic='Flood the zone.',
            color='teal',
        ),
        make_node(
            id='ex_outproduce',
            label='Chimp vs gorilla testes',
            detail=(
                'Chimpanzees (polyandrous — many males mate with one female) have large '
                'testes relative to body mass. Gorillas (harem structure, one silverback) '
                'have small testes because sperm competition is rare. Humans are intermediate — '
                'a clue about our mating history.'
            ),
            color='teal',
        ),
        # Strategy 3: Cooperate (kin selection at the gamete level)
        make_node(
            id='strat_cooperate',
            label='Cooperate (brother sperm)',
            detail=(
                'Related sperm from one male aggregate and swim together, reaching the egg '
                'faster than sperm from a different male. Kin selection operating at the '
                'gamete level — Hamilton-style rB > C in miniature.'
            ),
            mnemonic='Brothers swim together.',
            color='purple',
        ),
        make_node(
            id='ex_cooperate',
            label='Peromyscus sperm trains',
            detail=(
                'Peromyscus maniculatus (promiscuous deer mouse) sperm form aggregates — '
                '"sperm trains" — that swim faster than single sperm. P. polionotus '
                '(monogamous) shows NO such aggregation, because there is no rival sperm '
                'to out-race. Direct phylogenetic test of the hypothesis.'
            ),
            color='purple',
        ),
        # Strategy 4: Prevent remating
        make_node(
            id='strat_prevent',
            label='Prevent remating',
            detail=(
                'Stop the female from mating again. Ranges from behavioral mate guarding '
                'to chemical warfare in the ejaculate to physical plugs that block the '
                'reproductive tract.'
            ),
            mnemonic='Lock the door.',
            color='amber',
        ),
        make_node(
            id='ex_prevent',
            label='Drosophila seminal toxins + plugs',
            detail=(
                'Drosophila melanogaster seminal fluid contains "Acps" (accessory gland '
                'proteins) that reduce female receptivity to remating — but also shorten '
                'female lifespan. Other species use copulatory plugs or giant sperm that '
                'fill the female storage organ.'
            ),
            color='amber',
        ),
        # Sexual conflict concept
        make_node(
            id='sexual_conflict',
            label='Sexual conflict',
            detail=(
                'Drosophila forced-monogamy experiment: after 40 generations of enforced '
                'monogamy (no sperm competition), seminal fluid became LESS toxic and '
                'females LOST defensive proteins. Confirms ongoing antagonistic coevolution — '
                'each sex is constantly evolving counter-measures against the other.'
            ),
            watchOut=(
                'Sexual conflict drives rapid reciprocal evolution — an arms race WITHIN '
                'a species, not between species.'
            ),
            color='red',
        ),
        # Testes ratio summary
        make_node(
            id='testes_ratio',
            label='Testes-mass ratio',
            value='chimp > human > gorilla',
            detail=(
                'Testes size relative to body mass tracks degree of sperm competition. '
                'A high ratio indicates the mating system is polyandrous; a low ratio '
                'indicates harem or monogamy. Humans sit in the middle — interpreted as '
                'evidence of mild but non-zero sperm competition in our ancestry.'
            ),
            color='blue',
        ),
    ]
    edges = [
        make_edge('strat_remove', 'ex_remove', label='example', style='arrow'),
        make_edge('strat_outproduce', 'ex_outproduce', label='example', style='arrow'),
        make_edge('strat_cooperate', 'ex_cooperate', label='example', style='arrow'),
        make_edge('strat_prevent', 'ex_prevent', label='example', style='arrow'),
        make_edge('ex_outproduce', 'testes_ratio', label='predicts', style='dashed'),
        make_edge('ex_prevent', 'sexual_conflict', label='drives', style='dashed'),
    ]
    return validate_diagram({
        'type': 'compare',
        'title': 'Sperm Competition Strategies Under Polyandry',
        'nodes': nodes,
        'edges': edges,
        'mnemonic': 'Remove, Out-produce, Cooperate, Prevent remating — four sperm competition strategies.',
    }, node_id='sperm_competition_strategies')
