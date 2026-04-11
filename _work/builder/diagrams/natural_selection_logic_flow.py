"""Darwin's logical proof of natural selection — observations → inference → outcome."""
from .types import make_node, make_edge, validate_diagram


def natural_selection_logic_flow_diagram():
    """Three observations → inference → selection → adaptation → speciation (Darwin 1859, Wallace 1858)."""
    nodes = [
        make_node(
            id='obs1',
            label='Overproduction',
            detail=(
                'Observation 1: organisms produce many more offspring than the environment '
                'can support. Darwin drew this directly from Malthus (1798). A single cod '
                'releases millions of eggs; an oak drops thousands of acorns — almost all '
                'will die before reproducing.'
            ),
            mnemonic='Overproduction = the demographic ceiling is always exceeded.',
            watchOut='Overproduction is about gametes/juveniles, not adults surviving.',
            color='amber',
        ),
        make_node(
            id='obs2',
            label='Variation',
            detail=(
                'Observation 2: individuals differ in morphology, physiology, and behavior. '
                'Darwin compiled extensive variation data from pigeon breeders, barnacles, '
                'and Galápagos mockingbirds/finches before publishing. Without variation, '
                'selection has no raw material to act on.'
            ),
            mnemonic='Variation = the raw material selection feeds on.',
            watchOut='Variation must be measurable in a trait that matters for survival/reproduction.',
            color='amber',
        ),
        make_node(
            id='obs3',
            label='Heritability',
            detail=(
                'Observation 3: offspring resemble their parents more than random members of '
                'the population. Darwin proved this qualitatively through artificial selection '
                'in pigeons (On the Origin of Species, 1859, Ch. 1). Mendel’s mechanism was '
                'unknown until 1900 — heritability was taken as an empirical fact.'
            ),
            mnemonic='Like begets like — the fidelity term in selection.',
            watchOut='If h² = 0, selection produces no response (Breeder’s Equation: R = h²S).',
            color='amber',
        ),
        make_node(
            id='inference',
            label='Differential survival/reproduction',
            detail=(
                'The inference: given overproduction, variation, and heritability, individuals '
                'with traits better matched to their environment will survive and reproduce at '
                'disproportionately higher rates. This is deduced logically from the three '
                'observations, which is why Darwin called it a "theory" in the scientific sense.'
            ),
            mnemonic='Three premises → one conclusion. It is a syllogism.',
            watchOut='"Differential" means relative to others in the same population, not absolute.',
            color='teal',
        ),
        make_node(
            id='selection',
            label='Natural selection acts',
            detail=(
                'Natural selection is the non-random, differential reproduction of genotypes. '
                'Darwin called it "the preservation of favoured races in the struggle for life" '
                '(1859 subtitle). Alfred Russel Wallace reached the same conclusion in 1858 '
                'while feverish in Ternate, prompting the joint Darwin/Wallace paper read at '
                'the Linnean Society of London on 1 July 1858.'
            ),
            mnemonic='NS is DRS operating consistently over generations.',
            watchOut='Selection ≠ evolution. Selection is the process; evolution is the measurable result.',
            color='teal',
        ),
        make_node(
            id='adaptation',
            label='Adaptations accumulate',
            detail=(
                'Over generations, alleles that increase fitness rise in frequency. Accumulated '
                'fitness-boosting changes become adaptations — traits fit to the organism’s '
                'environment. Darwin’s key insight: apparent "design" in nature arises from '
                'cumulative selection without a designer.'
            ),
            mnemonic='Cumulative selection = apparent design, no designer needed.',
            watchOut='Not every trait is an adaptation — some are byproducts or drift (see Gould & Lewontin 1979).',
            color='green',
        ),
        make_node(
            id='speciation',
            label='Speciation over time',
            detail=(
                'When populations accumulate enough divergent adaptations — aided by isolation '
                'or ecological differences — reproductive isolation follows and new species '
                'form. Darwin devoted Chapter 4 of "On the Origin of Species" (24 November 1859) '
                'to this extrapolation. Wallace (1858 Linnean Society joint presentation) '
                'shared credit for the mechanism but not the speciation framework.'
            ),
            mnemonic='Small changes + time + isolation = new species.',
            watchOut='Speciation requires reproductive isolation, not just morphological difference.',
            color='green',
        ),
    ]
    edges = [
        make_edge('obs1', 'inference', label='therefore (Malthus)', style='arrow'),
        make_edge('obs2', 'inference', label='therefore (variation matters)', style='arrow'),
        make_edge('obs3', 'inference', label='therefore (inheritance persists)', style='arrow'),
        make_edge('inference', 'selection', label='which produces', style='arrow'),
        make_edge('selection', 'adaptation', label='over generations', style='arrow'),
        make_edge('adaptation', 'speciation', label='with isolation, over deep time', style='arrow'),
    ]
    return validate_diagram({
        'type': 'flow',
        'title': 'Darwin’s Logical Proof — From Observations to Speciation',
        'nodes': nodes,
        'edges': edges,
        'mnemonic': 'Overproduction + Variation + Heritability → DRS → NS → Adaptation → Speciation.',
    }, node_id='natural_selection_logic_flow')
