"""Darwin's five ingredients of natural selection — Lec 2 flow diagram."""
from .types import make_node, make_edge, validate_diagram


def darwin_five_ingredients_diagram():
    """Five observations → one inference → one evolutionary outcome (Darwin/Wallace 1858-1859)."""
    nodes = [
        make_node(
            id='repro_potential',
            label='High reproductive potential',
            detail=(
                'Every species can produce far more offspring than can possibly survive. '
                'Lec 2 examples: Aphis fabae can generate 524 billion aphids in a single '
                'year; Staphylococcus aureus would blanket Earth 7 feet deep in 24 hours '
                'with no limits; from one elephant pair, Darwin calculated 19 million '
                'elephants in 750 years. Thomas Malthus (1766–1834) formalized the idea '
                'in his 1798 "Essay on the Principle of Population," which Darwin read in '
                'October 1838 and explicitly credited as the spark for natural selection.'
            ),
            mnemonic='524B aphids/yr — no population actually reaches its reproductive ceiling.',
            watchOut='This is an OBSERVATION, not a cause. Overproduction alone produces no change.',
            value='524B aphids/yr',
            color='amber',
        ),
        make_node(
            id='stable_size',
            label='Populations stable in size',
            detail=(
                'Despite enormous reproductive potential, populations do not grow without '
                'bound. Malthus argued that populations grow geometrically while food '
                'supply grows arithmetically — so most offspring must die before reproducing. '
                'Alfred Russel Wallace independently reached the same insight in 1858 while '
                'in the Malay Archipelago, also citing Malthus.'
            ),
            mnemonic='Malthus: geometric births meet arithmetic food → stability is enforced by death.',
            watchOut='Short-term booms happen, but long-term equilibrium is the rule.',
            color='amber',
        ),
        make_node(
            id='limited_resources',
            label='Limited resources → struggle',
            detail=(
                'Food, mates, territory, water, and nest sites are finite. Individuals '
                'must compete — the "struggle for existence" (Darwin 1859, Ch. 3). The '
                'struggle is often passive: outgrowing a neighbor, tolerating drought, '
                'evading a parasite.'
            ),
            mnemonic='Struggle is mostly quiet, not bloody.',
            watchOut='Struggle does not require direct combat — differential survival is enough.',
            color='amber',
        ),
        make_node(
            id='variation',
            label='Phenotypic variation',
            detail=(
                'No two individuals are identical. Variation spans morphology, physiology, '
                'behavior, and performance. Darwin documented variation across pigeon breeds, '
                'barnacles, and Galápagos finches. Without phenotypic differences, selection '
                'has nothing to grip.'
            ),
            mnemonic='No variation → no selection, period.',
            watchOut='Non-heritable differences (scars, sunburn, learned tricks) don’t evolve.',
            color='amber',
        ),
        make_node(
            id='heritability',
            label='Heritability',
            detail=(
                'Trait values must be transmitted from parents to offspring. Darwin had no '
                'mechanism — Mendel’s 1866 peas were unknown to him, and genetics was not '
                'rediscovered until 1900. Yet breeders had shown heritability empirically for '
                'centuries. Wallace, co-announcing the theory at the Linnean Society on 1 July '
                '1858, also lacked a transmission mechanism.'
            ),
            mnemonic='Parents must "send" the trait to offspring for selection to stick.',
            watchOut='If heritability is zero, NS cannot occur even with perfect variation and DRS.',
            color='amber',
        ),
        make_node(
            id='drs',
            label='Differential reproductive success',
            detail=(
                'The logical inference: given overproduction, limited resources, heritable '
                'variation, and competition, individuals with advantageous heritable traits '
                'will leave disproportionately more offspring. This is the operational '
                'definition of natural selection — not "survival of the fittest" but '
                '"differential reproductive success conditional on phenotype."'
            ),
            mnemonic='VHI-DRS: Variation + Heritability + Inference → Differential Reproductive Success.',
            watchOut='Fitness = lifetime reproductive output, not just survival to adulthood.',
            color='teal',
        ),
        make_node(
            id='evolution',
            label='Evolution by natural selection',
            detail=(
                'Over generations, allele frequencies shift toward variants that improve '
                'relative fitness in the current environment. Populations — not individuals — '
                'evolve. Joint Darwin/Wallace presentation was read at the Linnean Society on '
                '1 July 1858, and Darwin’s "On the Origin of Species" followed on 24 November '
                '1859. (Wallace mention: the theory is correctly called Darwin–Wallace natural '
                'selection, though Darwin’s evidence was more extensive.)'
            ),
            mnemonic='allele frequencies change — that IS evolution.',
            watchOut='Selection acts on phenotypes, but evolution is measured as allele frequency change.',
            color='green',
        ),
    ]
    edges = [
        make_edge('repro_potential', 'stable_size', label='observation 1 → 2', style='arrow'),
        make_edge('stable_size', 'limited_resources', label='observation 3', style='arrow'),
        make_edge('limited_resources', 'drs', label='inference (struggle)', style='arrow'),
        make_edge('variation', 'drs', label='observation 4', style='arrow'),
        make_edge('heritability', 'drs', label='observation 5', style='arrow'),
        make_edge('drs', 'evolution', label='outcome (over generations)', style='arrow'),
    ]
    return validate_diagram({
        'type': 'flow',
        'title': 'Darwin — Five Ingredients of Natural Selection (Lec 2)',
        'nodes': nodes,
        'edges': edges,
        'mnemonic': 'VHI-DRS: Variation + Heritability + Inference → Differential Reproductive Success → Evolution.',
    }, node_id='darwin_five_ingredients')
