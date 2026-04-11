"""Allopolyploidy — step-by-step mechanism of instant speciation — flow diagram."""

from .types import make_node, make_edge, validate_diagram


def allopolyploidy_flow_diagram():
    nodes = [
        make_node(
            id='parent1',
            label='Parent species 1',
            value='2n = X₁',
            detail=(
                'Example: Tragopogon dubius (2n = 12). A diploid species with '
                'its own set of homologous chromosome pairs.'
            ),
            mnemonic='diploid parent A',
            color='amber',
        ),
        make_node(
            id='parent2',
            label='Parent species 2',
            value='2n = X₂',
            detail=(
                'Example: Tragopogon pratensis (2n = 12). A different diploid '
                'species. Its chromosomes are homologous within itself but '
                'not homologous to parent 1.'
            ),
            mnemonic='diploid parent B',
            color='coral',
        ),
        make_node(
            id='hybrid_f1',
            label='Sterile F1 hybrid',
            value='X₁/2 + X₂/2',
            detail=(
                'Interspecific cross produces a hybrid carrying one haploid '
                'set from each parent. This hybrid is STERILE: at meiosis, '
                'chromosomes from species 1 cannot pair with chromosomes '
                'from species 2 because they are not homologous. Gametes '
                'carry random unbalanced chromosome sets and fail.'
            ),
            mnemonic='no homologs → no meiosis',
            color='gray',
        ),
        make_node(
            id='whole_genome_dup',
            label='Whole-genome duplication',
            value='chromosome doubling',
            detail=(
                'Failure of meiosis (unreduced gamete) or a somatic cell '
                'chromosome doubling event produces a cell with TWO copies of '
                'each chromosome from each parent. Now every chromosome has '
                'a true homolog — meiosis can proceed normally.'
            ),
            mnemonic='2× all chromosomes',
            color='blue',
        ),
        make_node(
            id='fertile_polyploid',
            label='Fertile allopolyploid',
            value='2n = X₁ + X₂',
            detail=(
                'The doubled hybrid is now fully fertile because each '
                'chromosome has a homolog to pair with at meiosis. It is also '
                'REPRODUCTIVELY ISOLATED from both parents: backcrosses '
                'produce odd-ploidy offspring that are themselves sterile.'
            ),
            mnemonic='instant new species',
            color='green',
        ),
        make_node(
            id='tragopogon_mirus',
            label='Tragopogon mirus',
            value='<100 years old',
            detail=(
                'Documented recent allopolyploid speciation event. Tragopogon '
                'mirus formed in the US Pacific Northwest (Washington state) '
                'within the last century from Tragopogon dubius × Tragopogon '
                'pratensis. Both parents are European introductions.'
            ),
            mnemonic='speciation in living memory',
            color='teal',
        ),
        make_node(
            id='bread_wheat',
            label='Bread wheat (hexaploid)',
            value='6n',
            detail=(
                'Triticum aestivum is a three-way allopolyploid combining '
                'genomes from Triticum urartu, Aegilops speltoides, and '
                'Aegilops tauschii. Each of the three contributing species '
                'donated a diploid genome, producing a hexaploid 6n = 42 '
                'chromosome crop plant.'
            ),
            watchOut=(
                'Allopolyploidy is INSTANT speciation — reproductive isolation '
                'is established in a single generation through chromosome '
                'incompatibility with parents.'
            ),
            color='purple',
        ),
    ]

    edges = [
        make_edge('parent1', 'hybrid_f1', label='gamete 1', style='arrow'),
        make_edge('parent2', 'hybrid_f1', label='gamete 2', style='arrow'),
        make_edge('hybrid_f1', 'whole_genome_dup', label='meiotic failure', style='arrow'),
        make_edge('whole_genome_dup', 'fertile_polyploid', label='homologs restored', style='arrow'),
        make_edge('fertile_polyploid', 'tragopogon_mirus', label='example 1', style='dashed'),
        make_edge('fertile_polyploid', 'bread_wheat', label='example 2 (3-way)', style='dashed'),
    ]

    return validate_diagram({
        'type': 'flow',
        'title': 'Allopolyploidy — Instant Speciation in One Generation',
        'nodes': nodes,
        'edges': edges,
        'mnemonic': 'Hybridize → double → fertile → isolated. One generation, new species.',
    }, node_id='allopolyploidy_flow')
