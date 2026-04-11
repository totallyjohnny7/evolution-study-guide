"""Bateson-Dobzhansky-Muller incompatibility matrix.

Source: BIOL 4230 Ch13. Ancestor has alleles A1B1 (both fine). Pop 1 evolves
A2 (fine with B1). Pop 2 evolves B2 (fine with A1). Hybrids inherit A2+B2 —
a combination NEVER TESTED BY SELECTION — turns out to be incompatible.
Snowballs over time.
"""

from .types import make_node, make_edge, validate_diagram


def bdm_matrix_diagram():
    nodes = [
        # Row/column headers (the locus B alleles)
        make_node(
            id='col_B1',
            label='B₁ (ancestral)',
            detail='The ancestral allele at locus B. Present in the original shared population.',
            color='gray',
        ),
        make_node(
            id='col_B2',
            label='B₂ (pop 2 derived)',
            detail=(
                'Derived allele at locus B, evolved in Population 2 AFTER the split. '
                'Fine in combination with A₁ (the ancestral A), because it was tested by '
                'selection in Population 2 where A₁ was still present.'
            ),
            color='coral',
        ),
        make_node(
            id='row_A1',
            label='A₁ (ancestral)',
            detail='The ancestral allele at locus A. Present in the original shared population.',
            color='gray',
        ),
        make_node(
            id='row_A2',
            label='A₂ (pop 1 derived)',
            detail=(
                'Derived allele at locus A, evolved in Population 1 AFTER the split. '
                'Fine in combination with B₁ (the ancestral B), because it was tested by '
                'selection in Population 1 where B₁ was still present.'
            ),
            color='blue',
        ),
        # Matrix cells
        make_node(
            id='A1B1',
            label='A₁B₁ ✓',
            detail=(
                'Ancestral combination. Both alleles were present in the original shared population '
                'and have always worked together. No incompatibility.'
            ),
            color='teal',
        ),
        make_node(
            id='A1B2',
            label='A₁B₂ ✓',
            detail=(
                'Tested in Population 2. As B₂ evolved, it was selected for compatibility with '
                'the existing A₁ background. This combination works — it passed selection.'
            ),
            color='teal',
        ),
        make_node(
            id='A2B1',
            label='A₂B₁ ✓',
            detail=(
                'Tested in Population 1. As A₂ evolved, it was selected for compatibility with '
                'the existing B₁ background. This combination works — it passed selection.'
            ),
            color='teal',
        ),
        make_node(
            id='A2B2',
            label='A₂B₂ ✗',
            detail=(
                'The hybrid genotype. A₂ and B₂ each evolved in ISOLATION in different populations. '
                'Neither lineage ever tested the A₂B₂ combination against selection. When hybrids '
                'inherit A₂ from parent 1 and B₂ from parent 2, the combination may be incompatible '
                '— hybrid inviability or sterility results. Each allele is fine alone; the combo '
                'is novel and untested.'
            ),
            mnemonic='BDM = untested combination of derived alleles → hybrid breakdown.',
            watchOut=(
                'BDM incompatibilities SNOWBALL: more generations in isolation = more diverged '
                'loci = more potential incompatible pairs. Speciation becomes harder to reverse '
                'the longer populations are separated.'
            ),
            color='red',
        ),
    ]
    edges = [
        # Arrows showing which allele came from which parental population
        make_edge('row_A2', 'A2B2', style='dashed', label='pop 1'),
        make_edge('col_B2', 'A2B2', style='dashed', label='pop 2'),
    ]
    return validate_diagram({
        'type': 'matrix',
        'title': 'Bateson-Dobzhansky-Muller Incompatibility Matrix',
        'nodes': nodes,
        'edges': edges,
        'mnemonic': 'BDM: each allele is fine alone, but the combination in hybrids was never tested by selection.',
    }, node_id='bdm_matrix')
