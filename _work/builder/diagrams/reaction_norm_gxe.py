"""Reaction norms and genotype × environment interaction (V_P = V_G + V_E + V_GxE)."""
from .types import make_node, make_edge, validate_diagram


def reaction_norm_gxe_diagram():
    """Compare two genotypes whose reaction norms cross — the signature of G×E interaction."""
    nodes = [
        # LEFT COLUMN — Genotype 1
        make_node(
            id='g1_envA',
            label='Genotype 1 at env A',
            detail=(
                'Reaction norm value for Genotype 1 in environment A (e.g. Achillea millefolium '
                'yarrow clone grown at low elevation in the Mather/Stanford/Timberline common '
                'garden experiment, Clausen, Keck & Hiesey 1940s). Genotype 1 performs well at '
                'low elevation: phenotypic value is high.'
            ),
            mnemonic='Low elevation is this clone’s sweet spot.',
            watchOut='The phenotype is a plastic response, not a new genotype.',
            color='teal',
        ),
        make_node(
            id='g1_envB',
            label='Genotype 1 at env B',
            detail=(
                'Same Genotype 1 clone transplanted to environment B (e.g. high-elevation '
                'Timberline garden). Performance drops sharply — stem height, leaf number, and '
                'biomass all fall. Still the identical genotype; the environment alone shifts '
                'the phenotypic value.'
            ),
            mnemonic='Same DNA, harsher conditions → lower phenotype.',
            watchOut='Transplanting clones is how you prove variation is V_E, not V_G.',
            color='teal',
        ),
        make_node(
            id='g1_norm',
            label='Genotype 1 reaction norm shape',
            detail=(
                'The line connecting Genotype 1’s phenotype across environments A and B slopes '
                'downward (good at low elevation, bad at high). Reaction norm SHAPE is a '
                'heritable property of the genotype — the plastic response itself is not, but '
                'the capacity for it is.'
            ),
            mnemonic='Reaction norm = the genotype’s response curve.',
            watchOut='Reaction norm shape is heritable; single phenotype values are not.',
            color='teal',
        ),
        # RIGHT COLUMN — Genotype 2
        make_node(
            id='g2_envA',
            label='Genotype 2 at env A',
            detail=(
                'Genotype 2 clone in environment A performs poorly — low elevation is not its '
                'niche. In the Clausen/Keck/Hiesey Achillea common-garden study, montane '
                'ecotypes were shorter than lowland ecotypes at low elevation.'
            ),
            mnemonic='This clone prefers altitude.',
            watchOut='A poor phenotype in one environment does not mean a poor genotype overall.',
            color='coral',
        ),
        make_node(
            id='g2_envB',
            label='Genotype 2 at env B',
            detail=(
                'Genotype 2 clone in environment B (high elevation) now performs well — taller, '
                'more vigorous than Genotype 1 at the same location. The ranking of genotypes '
                'has FLIPPED between environments. This crossover is the signature of G×E '
                'interaction.'
            ),
            mnemonic='Rank order flipped = G×E, not just G + E.',
            watchOut='Crossover interaction means "best genotype" is environment-dependent.',
            color='coral',
        ),
        make_node(
            id='g2_norm',
            label='Genotype 2 reaction norm shape',
            detail=(
                'The line connecting Genotype 2’s phenotype across environments slopes upward '
                '(bad at low elevation, good at high). Because this line crosses Genotype 1’s '
                'line, the interaction term V_GxE is non-zero.'
            ),
            mnemonic='Crossing lines = G×E interaction.',
            watchOut='Parallel reaction norms produce V_E but no V_GxE.',
            color='coral',
        ),
        # Variance partition labels
        make_node(
            id='v_g',
            label='V_G (between-genotype)',
            detail=(
                'Variance in phenotype attributable to genetic differences among individuals, '
                'averaged across environments. Estimated from clonal or half-sib comparisons. '
                'V_G drives heritability (h² = V_A / V_P).'
            ),
            mnemonic='V_G = "nature" component of the variance.',
            watchOut='V_G alone does not predict response to selection — only additive V_A does.',
            value='V_G',
            color='amber',
        ),
        make_node(
            id='v_e',
            label='V_E (environmental)',
            detail=(
                'Variance in phenotype attributable to environmental differences, averaged '
                'across genotypes. In a common-garden experiment, V_E is estimated by comparing '
                'the same clone across sites.'
            ),
            mnemonic='V_E = "nurture" component of the variance.',
            watchOut='Uncontrolled micro-environmental variation can inflate V_E estimates.',
            value='V_E',
            color='amber',
        ),
        make_node(
            id='v_gxe',
            label='V_GxE interaction',
            detail=(
                'Variance arising when genotypes respond DIFFERENTLY to environmental changes — '
                'the non-parallelism of reaction norms. V_GxE > 0 implies no single genotype is '
                'universally best, and local adaptation is possible. Detected as a significant '
                'G×E term in a two-way ANOVA on clone × environment data.'
            ),
            mnemonic='Crossing reaction norms → V_GxE > 0.',
            watchOut=(
                'Plasticity is NOT evolution. The reaction norm SHAPE is heritable; the plastic '
                'response itself is not allele frequency change.'
            ),
            value='V_GxE',
            color='amber',
        ),
        make_node(
            id='cases',
            label='Classic G×E cases',
            detail=(
                'Richard Woltereck coined "Reaktionsnorm" in 1909 studying Daphnia head shape '
                'across food concentrations. Daphnia cucullata grow neck teeth when they detect '
                'Chaoborus midge-larvae chemical cues — an inducible defense. Ambystoma '
                'tigrinum salamander larvae develop cannibalistic morphs at high density and '
                'prey availability. Clausen, Keck & Hiesey’s Achillea millefolium common garden '
                'across Mather (low), Stanford, and Timberline (high) showed crossing reaction '
                'norms in stem height.'
            ),
            mnemonic='Woltereck 1909, Achillea Mather/Stanford, Daphnia, Ambystoma cannibals.',
            watchOut='Inducible defenses are plasticity, not evolution — no allele frequency change.',
            color='blue',
        ),
    ]
    edges = [
        make_edge('g1_envA', 'g1_norm', label='shape', style='arrow'),
        make_edge('g1_envB', 'g1_norm', label='shape', style='arrow'),
        make_edge('g2_envA', 'g2_norm', label='shape', style='arrow'),
        make_edge('g2_envB', 'g2_norm', label='shape', style='arrow'),
        make_edge('g1_norm', 'v_gxe', label='contributes to', style='arrow'),
        make_edge('g2_norm', 'v_gxe', label='contributes to', style='arrow'),
        make_edge('g1_envA', 'v_e', label='env effect', style='dashed'),
        make_edge('g2_envB', 'v_e', label='env effect', style='dashed'),
        make_edge('g1_norm', 'v_g', label='genotype effect', style='dashed'),
        make_edge('g2_norm', 'v_g', label='genotype effect', style='dashed'),
        make_edge('cases', 'v_gxe', label='documented by', style='dashed'),
    ]
    return validate_diagram({
        'type': 'compare',
        'title': 'Reaction Norms & G×E Interaction — V_P = V_G + V_E + V_GxE',
        'nodes': nodes,
        'edges': edges,
        'mnemonic': 'V_P = V_G + V_E + V_GxE. Crossing reaction norms = G×E interaction.',
    }, node_id='reaction_norm_gxe')
