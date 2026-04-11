"""Anisogamy origin — flow diagram (isogamy -> anisogamy -> sexual selection)."""

from .types import make_node, make_edge, validate_diagram


def anisogamy_origin_diagram():
    nodes = [
        make_node(
            id='isogamy',
            label='Ancestral isogamy',
            detail=(
                'The ancestral eukaryotic condition: a single gamete type in which all fusing '
                'cells are of equal size. Modern isogamous species are still found among some '
                'green algae (Chlamydomonas) and fungi. No "male" or "female" — just + and - '
                'mating types.'
            ),
            mnemonic='One gamete, one size, no sexes.',
            color='gray',
        ),
        make_node(
            id='disruptive_selection',
            label='Disruptive selection on gamete size',
            detail=(
                'Parker, Baker & Smith (1972) showed that intermediate-sized gametes lose under '
                'disruptive selection: large gametes provision zygotes better and survive, while '
                'tiny cheap gametes can be produced in huge numbers and find partners. '
                'Intermediates fail at both.'
            ),
            mnemonic='Big OR tiny — anything in between loses.',
            color='purple',
        ),
        make_node(
            id='anisogamy',
            label='Anisogamy evolves',
            detail=(
                'Disruptive selection produces two gamete sizes: large, rare, resource-rich '
                'gametes (eggs, by definition the female gamete) and small, numerous, mobile '
                'gametes (sperm, by definition the male gamete). Sexes are DEFINED by gamete '
                'size, not by chromosomes.'
            ),
            mnemonic='Sex IS gamete size.',
            color='amber',
        ),
        make_node(
            id='sperm_strategy',
            label='Males: many cheap sperm',
            detail=(
                'Males invest minimally per gamete and produce huge numbers. A male kiwi '
                '(Apteryx) produces roughly a trillion sperm over its lifetime. Male reproductive '
                'success is therefore limited by ACCESS TO FEMALES, not gamete supply.'
            ),
            value='~1 trillion sperm (kiwi)',
            mnemonic='Sperm are cheap — males compete for eggs.',
            color='blue',
        ),
        make_node(
            id='egg_strategy',
            label='Females: few expensive eggs',
            detail=(
                'Females invest heavily per gamete. A cow ovum is roughly 20,000 times the '
                'volume of a sperm and is produced in single units per cycle. Female '
                'reproductive success is limited by RESOURCES and mate quality, not by finding '
                'partners.'
            ),
            value='ovum ~20000x sperm (cow)',
            mnemonic='Eggs are costly — females choose carefully.',
            color='coral',
        ),
        make_node(
            id='osr_bias',
            label='Operational sex ratio (OSR) bias',
            detail=(
                'The OSR is the ratio of sexually available males to sexually available females '
                'at any moment. Because females are usually tied up with gestation or parental '
                'care while males keep cycling back to the mating pool, the OSR is usually '
                'male-biased — intensifying male-male competition.'
            ),
            mnemonic='OSR = who is currently in the mating market.',
            color='teal',
        ),
        make_node(
            id='sexual_selection',
            label='Intrasexual + intersexual selection',
            detail=(
                'Asymmetric investment creates the classical pattern: males compete with other '
                'males (intrasexual selection — horns, size, song) and females choose among '
                'males (intersexual selection — ornaments, displays). Sexual selection is the '
                'direct downstream consequence of anisogamy + skewed OSR.'
            ),
            mnemonic='Sex roles follow INVESTMENT, not chromosomes.',
            watchOut='Sex roles are NOT fixed — pipefish and seahorse males invest more than females, so females compete and males choose.',
            color='green',
        ),
    ]
    edges = [
        make_edge('isogamy', 'disruptive_selection', label='size variance appears', style='arrow'),
        make_edge('disruptive_selection', 'anisogamy', label='two stable extremes', style='arrow'),
        make_edge('anisogamy', 'sperm_strategy', label='small-gamete strategy', style='arrow'),
        make_edge('anisogamy', 'egg_strategy', label='large-gamete strategy', style='arrow'),
        make_edge('sperm_strategy', 'osr_bias', label='males cycle back fast', style='arrow'),
        make_edge('egg_strategy', 'osr_bias', label='females tied up longer', style='arrow'),
        make_edge('osr_bias', 'sexual_selection', label='drives competition and choice', style='arrow'),
    ]
    return validate_diagram({
        'type': 'flow',
        'title': 'Anisogamy — The Origin of Sexes and Sexual Selection',
        'nodes': nodes,
        'edges': edges,
        'mnemonic': 'Small sperm, big eggs -> different strategies -> sexual selection.',
    }, node_id='anisogamy_origin')
