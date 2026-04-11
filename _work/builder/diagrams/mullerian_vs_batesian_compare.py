"""Mullerian vs Batesian mimicry — compare diagram."""

from .types import make_node, make_edge, validate_diagram


def mullerian_vs_batesian_compare_diagram():
    nodes = [
        # ===== Left column: Mullerian mimicry =====
        make_node(
            id='mul_header',
            label='Mullerian mimicry',
            detail=(
                'Fritz Mueller (1821-1897) described the situation where two or more unpalatable '
                'species converge on a shared warning pattern. Classic examples: Heliconius '
                'butterflies in the Neotropics and the North American coral snakes.'
            ),
            mnemonic='Mullerian = Mutual (both taste bad).',
            color='purple',
        ),
        make_node(
            id='mul_both_toxic',
            label='Both species toxic/harmful',
            detail=(
                'All participants in a Mullerian ring are genuinely defended — cyanogenic, '
                'alkaloid-loaded, venomous, or otherwise unprofitable to eat. Predators that '
                'attack any species in the ring are punished.'
            ),
            mnemonic='Everyone in the ring is armed.',
            color='purple',
        ),
        make_node(
            id='mul_warning',
            label='Shared warning signal (aposematism)',
            detail=(
                'Species converge on the SAME bold color pattern — red/yellow/black bands, '
                'orange-and-black wings — so predators need learn only one pattern to avoid '
                'the whole complex. The signal is honest advertising of real toxicity.'
            ),
            mnemonic='Honest aposematic billboard.',
            color='purple',
        ),
        make_node(
            id='mul_coev',
            label='Convergent coevolution',
            detail=(
                'Each species exerts selection on the others to match its own signal, producing '
                'reciprocal convergence on a common phenotype. Heliconius erato and H. melpomene '
                'track each other across Amazonia, producing matching geographic race mosaics.'
            ),
            mnemonic='Mutual convergence on one billboard.',
            color='purple',
        ),
        make_node(
            id='mul_shared_cost',
            label='Both benefit — shared advertising cost',
            detail=(
                'Because predators need only one bad experience per pattern, the "teaching cost" '
                '(individuals killed during predator learning) is spread across all participating '
                'species. Every species pays less per capita than it would alone.'
            ),
            mnemonic='Shared signal = shared cost.',
            color='purple',
        ),
        make_node(
            id='mul_example',
            label='Example: Heliconius',
            detail=(
                'Heliconius erato and H. melpomene are two distantly related but co-distributed '
                'butterfly species that share nearly identical wing patterns across dozens of '
                'Amazonian geographic races — a classic Mullerian ring driven by convergent '
                'cis-regulatory changes at the optix pigmentation locus.'
            ),
            value='Heliconius erato and H. melpomene',
            mnemonic='Heliconius ring = textbook Mullerian.',
            color='purple',
        ),

        # ===== Right column: Batesian mimicry =====
        make_node(
            id='bat_header',
            label='Batesian mimicry',
            detail=(
                'Henry Walter Bates (1825-1892) described the situation where a harmless mimic '
                'evolves to resemble a dangerous model, freeloading on the model\'s reputation. '
                'Bates developed the idea during his 11 years in the Amazon alongside Wallace.'
            ),
            mnemonic='Batesian = Bluffing (mimic is safe).',
            color='coral',
        ),
        make_node(
            id='bat_asymmetry',
            label='Only model is harmful; mimic is harmless',
            detail=(
                'The model carries a real defense — toxin, venom, sting — but the mimic has no '
                'defense at all. Its only protection is the predator\'s memory of a bad '
                'experience with the model.'
            ),
            mnemonic='Model dangerous, mimic bluffing.',
            color='coral',
        ),
        make_node(
            id='bat_learned',
            label='Mimic exploits learned avoidance',
            detail=(
                'Predators must first encounter the harmful model and learn to avoid its warning '
                'pattern. Once trained, they generalize avoidance to the harmless mimic. The '
                'mimic contributes nothing to the training — it only freerides on the model.'
            ),
            mnemonic='Predator training is paid by the model only.',
            color='coral',
        ),
        make_node(
            id='bat_asym_benefit',
            label='Asymmetric benefit',
            detail=(
                'The mimic gains enormous protection at zero investment. The model PAYS because '
                'predators who encounter a harmless mimic first learn the pattern is safe and '
                'then attack genuine models. Mimic wins, model loses.'
            ),
            mnemonic='Parasitic mimicry — mimic wins, model loses.',
            color='coral',
        ),
        make_node(
            id='bat_freq_dep',
            label='Frequency-dependent stability',
            detail=(
                'Batesian mimicry is stable only when mimics remain RARE relative to models, so '
                'most predator encounters remain with the real thing. As mimics become more '
                'common, predators learn the pattern is often safe, the system collapses, and '
                'a coevolutionary chase follows — models evolve new signals and mimics race to '
                'follow.'
            ),
            mnemonic='Rare mimic = stable. Common mimic = collapse.',
            watchOut='If mimics become too common relative to models, predators learn the pattern is safe and a coevolutionary chase ensues.',
            color='coral',
        ),
        make_node(
            id='bat_example',
            label='Example: Brachoria mimics Apheloria',
            detail=(
                'Apheloria millipedes secrete hydrogen cyanide and are genuinely lethal to '
                'predators. Brachoria millipedes — which lack the cyanide defense or produce '
                'far less — have converged on nearly identical bright warning colors in the '
                'southern Appalachians, producing striking mimetic rings documented by Hensley '
                '2009 Science.'
            ),
            value='Hensley 2009 Science',
            mnemonic='Cyanide Apheloria, bluffing Brachoria.',
            color='coral',
        ),
    ]
    edges = [
        make_edge('mul_header', 'mul_both_toxic', style='solid'),
        make_edge('mul_both_toxic', 'mul_warning', style='solid'),
        make_edge('mul_warning', 'mul_coev', style='solid'),
        make_edge('mul_coev', 'mul_shared_cost', style='solid'),
        make_edge('mul_shared_cost', 'mul_example', style='solid'),
        make_edge('bat_header', 'bat_asymmetry', style='solid'),
        make_edge('bat_asymmetry', 'bat_learned', style='solid'),
        make_edge('bat_learned', 'bat_asym_benefit', style='solid'),
        make_edge('bat_asym_benefit', 'bat_freq_dep', style='solid'),
        make_edge('bat_freq_dep', 'bat_example', style='solid'),
        make_edge('mul_header', 'bat_header', label='contrast', style='dashed'),
    ]
    return validate_diagram({
        'type': 'compare',
        'title': 'Mullerian vs Batesian Mimicry',
        'nodes': nodes,
        'edges': edges,
        'mnemonic': 'Mullerian = Mutual (both toxic). Batesian = Bluffing (mimic is safe).',
    }, node_id='mullerian_vs_batesian_compare')
