"""Bateson-Dobzhansky-Muller incompatibility — 2x2 allele combination matrix."""

from .types import make_node, make_edge, validate_diagram


def bdm_incompatibility_matrix_diagram():
    nodes = [
        # Row headers (locus A state)
        make_node(
            id='row_A',
            label='Locus A: ancestral a',
            detail=(
                'Row 1 — the ancestral allele at locus A is "a." Populations '
                'carrying aa have not changed at this locus.'
            ),
            mnemonic='ancestral a',
            color='gray',
        ),
        make_node(
            id='row_B',
            label='Locus A: derived A',
            detail=(
                'Row 2 — population 1 evolved a derived allele "A" at locus '
                'A. This allele arose and fixed in one lineage only.'
            ),
            mnemonic='derived A (pop 1)',
            color='blue',
        ),

        # Column headers (locus B state)
        make_node(
            id='col_b',
            label='Locus B: ancestral b',
            detail=(
                'Column 1 — the ancestral allele at locus B is "b." '
                'Populations carrying bb have not changed at this locus.'
            ),
            mnemonic='ancestral b',
            color='gray',
        ),
        make_node(
            id='col_B',
            label='Locus B: derived B',
            detail=(
                'Column 2 — population 2 evolved a derived allele "B" at '
                'locus B. This allele arose and fixed in the OTHER lineage.'
            ),
            mnemonic='derived B (pop 2)',
            color='coral',
        ),

        # Cells
        make_node(
            id='aabb',
            label='Ancestral aabb',
            value='viable',
            detail=(
                'The ancestral population — both loci unchanged. All alleles '
                'have been tested together by natural selection and are '
                'compatible. Fully viable and fertile.'
            ),
            mnemonic='original genotype',
            color='green',
        ),
        make_node(
            id='AAbb',
            label='Population 1: AAbb',
            value='viable',
            detail=(
                'Population 1 fixed the derived A allele at locus A while '
                'keeping ancestral b at locus B. The combination A with '
                'ancestral b has been tested by selection in population 1 '
                'and is fully viable.'
            ),
            mnemonic='pop 1 fine on its own',
            color='blue',
        ),
        make_node(
            id='aaBB',
            label='Population 2: aaBB',
            value='viable',
            detail=(
                'Population 2 fixed the derived B allele at locus B while '
                'keeping ancestral a at locus A. The combination ancestral '
                'a with derived B has been tested by selection in '
                'population 2 and is fully viable.'
            ),
            mnemonic='pop 2 fine on its own',
            color='coral',
        ),
        make_node(
            id='AaBb',
            label='Hybrid AaBb',
            value='INVIABLE',
            detail=(
                'The F1 hybrid inherits A from pop 1 and B from pop 2. The '
                'derived alleles A and B have NEVER BEEN TESTED TOGETHER '
                'by natural selection in any parent lineage — their '
                'epistatic interaction is lethal. Classic example: Mimulus '
                'Hms1/Hms2 incompatibility kills hybrid seedlings. '
                'Formalized by Bateson (1909), Dobzhansky (1937), and '
                'Muller (1942).'
            ),
            mnemonic='novel allele combo = lethal',
            watchOut=(
                'Each derived allele is FINE in its own lineage — the '
                'incompatibility arises only between alleles that never '
                'evolved together.'
            ),
            color='red',
        ),
    ]

    edges = [
        make_edge('aabb', 'AAbb', label='pop 1 fixes A', style='arrow'),
        make_edge('aabb', 'aaBB', label='pop 2 fixes B', style='arrow'),
        make_edge('AAbb', 'AaBb', label='F1 hybrid cross', style='arrow'),
        make_edge('aaBB', 'AaBb', label='F1 hybrid cross', style='arrow'),
        make_edge('row_A', 'aabb', label='row 1', style='dashed'),
        make_edge('row_A', 'aaBB', label='row 1', style='dashed'),
        make_edge('row_B', 'AAbb', label='row 2', style='dashed'),
        make_edge('row_B', 'AaBb', label='row 2', style='dashed'),
        make_edge('col_b', 'aabb', label='col 1', style='dashed'),
        make_edge('col_b', 'AAbb', label='col 1', style='dashed'),
        make_edge('col_B', 'aaBB', label='col 2', style='dashed'),
        make_edge('col_B', 'AaBb', label='col 2', style='dashed'),
    ]

    return validate_diagram({
        'type': 'matrix',
        'title': 'Bateson-Dobzhansky-Muller Incompatibility Matrix',
        'nodes': nodes,
        'edges': edges,
        'mnemonic': 'BDM: each population fine on its own; hybrid fails because derived alleles at different loci have never been co-tested.',
    }, node_id='bdm_incompatibility_matrix')
