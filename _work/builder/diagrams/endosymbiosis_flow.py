"""Endosymbiosis — flow diagram (Margulis, mitochondria, chloroplasts, Euglena)."""

from .types import make_node, make_edge, validate_diagram


def endosymbiosis_flow_diagram():
    nodes = [
        make_node(
            id='host_cell',
            label='Ancestral archaeal host',
            detail=(
                'The host lineage for primary endosymbiosis was an Asgard-group archaeon — not a '
                'bacterium. Phylogenomic work places modern eukaryotes within archaea (Lokiarchaea '
                'and relatives), with the mitochondrial endosymbiont supplying the bacterial '
                'features of the eukaryotic cell.'
            ),
            mnemonic='Eukaryote = archaeal chassis + bacterial battery.',
            color='gray',
        ),
        make_node(
            id='free_bacterium',
            label='Free-living alpha-proteobacterium',
            detail=(
                'Ancestor of modern mitochondria. Its closest living relatives lie in the '
                'Pelagibacteracea (SAR11 clade) — the most abundant bacteria in the ocean. A '
                'heterotrophic, aerobically respiring alpha-proteobacterium became the mitochondrial '
                'endosymbiont.'
            ),
            mnemonic='Mitochondrion sister = SAR11 marine bacteria.',
            color='blue',
        ),
        make_node(
            id='engulf',
            label='Host engulfs bacterium',
            detail=(
                'The archaeal host physically enclosed the alpha-proteobacterium and instead of '
                'digesting it retained a long-term intracellular partnership. Primary endosymbiosis '
                'is the foundational event of eukaryogenesis.'
            ),
            mnemonic='Endosymbiosis = "living within".',
            color='teal',
        ),
        make_node(
            id='mitochondrion',
            label='Mitochondrion (endosymbiont)',
            detail=(
                'Modern mitochondria retain all the hallmarks of their bacterial origin: their own '
                'circular DNA, double membranes (the inner membrane = the original bacterial '
                'plasma membrane), 70S bacterial-type ribosomes, and division by binary fission '
                'independent of host mitosis.'
            ),
            value='2 membranes, 70S ribo',
            mnemonic='Mitochondria still act like bacteria inside you.',
            color='coral',
        ),
        make_node(
            id='gene_transfer',
            label='Gene transfer to nucleus',
            detail=(
                'Over evolutionary time, the overwhelming majority of endosymbiont genes have been '
                'transferred into the host nuclear genome. Modern human mitochondrial DNA carries '
                'only 37 genes, compared with ~1000+ in the free-living ancestor. Proteins encoded '
                'in the nucleus are imported back into the organelle.'
            ),
            mnemonic='Most organelle genes now live in the nucleus.',
            color='purple',
        ),
        make_node(
            id='chloroplast',
            label='Chloroplast',
            detail=(
                'A second, independent primary endosymbiosis event in which an archaeplastidan '
                'ancestor engulfed a cyanobacterium. All modern chloroplasts (in red algae, green '
                'algae, and land plants) descend from this single event roughly 1.5 billion years '
                'ago. Chloroplasts, like mitochondria, still carry their own bacterial-type genome.'
            ),
            mnemonic='Chloroplast = captured cyanobacterium.',
            color='green',
        ),
        make_node(
            id='euglena',
            label='Euglena — secondary endosymbiosis',
            detail=(
                'Euglena gracilis did not engulf a cyanobacterium directly. Instead, a '
                'heterotrophic eukaryote engulfed a green alga that ALREADY had a chloroplast. '
                'The result is a chloroplast wrapped in FOUR membranes: the two original '
                'chloroplast membranes, the former algal plasma membrane, and the host\'s '
                'phagosome membrane.'
            ),
            mnemonic='Four membranes = nested endosymbiosis.',
            color='teal',
        ),
        make_node(
            id='margulis',
            label='Lynn Margulis 1967',
            detail=(
                'Lynn Margulis proposed the Serial Endosymbiosis Theory in her 1967 paper "On the '
                'Origin of Mitosing Cells". The paper was rejected by roughly 15 journals before '
                'publication and widely dismissed by the biology establishment until molecular '
                'phylogenetics in the 1970s and 80s finally confirmed the bacterial ancestry of '
                'mitochondria and chloroplasts.'
            ),
            value='initially rejected',
            mnemonic='Margulis was right; the establishment was wrong.',
            watchOut='Margulis\'s endosymbiosis theory was REJECTED for decades — accepted only after molecular evidence accumulated.',
            color='amber',
        ),
    ]
    edges = [
        make_edge('host_cell', 'engulf', label='host role', style='arrow'),
        make_edge('free_bacterium', 'engulf', label='symbiont role', style='arrow'),
        make_edge('engulf', 'mitochondrion', label='primary endosymbiosis', style='arrow'),
        make_edge('mitochondrion', 'gene_transfer', label='genome reduction over time', style='arrow'),
        make_edge('engulf', 'chloroplast', label='second independent event', style='dashed'),
        make_edge('chloroplast', 'euglena', label='nested capture', style='arrow'),
        make_edge('margulis', 'engulf', label='proposed mechanism', style='dashed'),
    ]
    return validate_diagram({
        'type': 'flow',
        'title': 'Endosymbiosis — The Origin of Eukaryotic Organelles',
        'nodes': nodes,
        'edges': edges,
        'mnemonic': 'Endosymbiosis: not just history — happening today. Life is collaborative.',
    }, node_id='endosymbiosis_flow')
