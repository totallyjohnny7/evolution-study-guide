"""Red Queen cycle — cycle diagram (parasite-host NFDS, Potamopyrgus, twofold cost of sex)."""

from .types import make_node, make_edge, validate_diagram


def red_queen_cycle_diagram():
    nodes = [
        make_node(
            id='host_common',
            label='Host genotype A common',
            detail=(
                'Genotype A dominates the host population. Because it is common, it presents a '
                'large, stable target for parasites — most host bodies a parasite encounters are '
                'genotype A. Selection on parasites strongly favors variants that can infect A.'
            ),
            mnemonic='Common = big target.',
            color='blue',
        ),
        make_node(
            id='parasite_adapt',
            label='Parasites specialize on A',
            detail=(
                'Parasite alleles that recognize and exploit host genotype A spread rapidly. '
                'This is positive frequency-dependent selection on the parasite side — whatever '
                'host is common, the parasite specializes on it. The specialization can be very '
                'fast (parasite generation times are short compared to hosts).'
            ),
            mnemonic='Parasites chase whatever is common.',
            color='red',
        ),
        make_node(
            id='host_crash',
            label='Genotype A fitness drops',
            detail=(
                'Specialized parasites hammer genotype A. Infected A individuals have fewer '
                'offspring, and their frequency in the next generation falls. Meanwhile, rare '
                'genotypes remain invisible to the specialized parasites and enjoy near-freedom '
                'from infection.'
            ),
            value='low RS',
            mnemonic='Common host genotype crashes under parasite load.',
            color='coral',
        ),
        make_node(
            id='host_shift',
            label='Rare genotype B rises',
            detail=(
                'Selection now favors rare host genotype B, whose frequency climbs. This is '
                'negative frequency-dependent selection on the host side — rare is good, common '
                'is bad. Potamopyrgus antipodarum (New Zealand freshwater snail) populations '
                'exposed to high parasite loads shift toward sexual reproduction, which continually '
                'generates rare genotypes.'
            ),
            mnemonic='Rare is good.',
            color='teal',
        ),
        make_node(
            id='parasite_shift',
            label='Parasites chase B',
            detail=(
                'As genotype B becomes common, the parasite selection pressure shifts to variants '
                'that can exploit B. The cycle repeats. Neither host nor parasite ever reaches '
                'a stable equilibrium — both keep running just to stay in place.'
            ),
            mnemonic='Pressure moves to the new common genotype.',
            color='red',
        ),
    ]
    edges = [
        make_edge('host_common', 'parasite_adapt', label='specializes on', style='arrow'),
        make_edge('parasite_adapt', 'host_crash', label='reduces fitness of', style='arrow'),
        make_edge('host_crash', 'host_shift', label='rare becomes common', style='arrow'),
        make_edge('host_shift', 'parasite_shift', label='pressure shifts to', style='arrow'),
        make_edge('parasite_shift', 'host_common', label='cycle repeats', style='arrow'),
    ]
    return validate_diagram({
        'type': 'cycle',
        'title': 'Red Queen Dynamics — Parasite-Host Cycling',
        'nodes': nodes,
        'edges': edges,
        'mnemonic': '"It takes all the running you can do, to keep in the same place." (Lewis Carroll). Sex creates a moving genetic target. Red Queen does NOT mean sex always wins — in stable low-parasite environments, asexual lineages can outcompete sexual ones (twofold cost of sex).',
    }, node_id='red_queen_cycle')
