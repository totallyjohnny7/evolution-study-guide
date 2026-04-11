"""Genetic drift — bottleneck effect vs. founder effect side-by-side."""
from .types import make_node, make_edge, validate_diagram


def genetic_drift_bottleneck_vs_founder_diagram():
    """Compare bottleneck vs founder effect as two flavors of drift-mediated variation loss."""
    nodes = [
        # LEFT COLUMN — BOTTLENECK
        make_node(
            id='bn_def',
            label='Bottleneck: definition',
            detail=(
                'A dramatic reduction in population size with long-lasting genetic effects. '
                'The pre-bottleneck population continues to exist through the crash — '
                'survivors are a small, non-representative sample of the original allele pool. '
                'Random chance, not fitness, determines which alleles make it through.'
            ),
            mnemonic='Bottleneck = squeeze an existing population.',
            watchOut='Population identity is preserved — only N collapses.',
            color='purple',
        ),
        make_node(
            id='bn_example',
            label='Bottleneck: N. elephant seals',
            detail=(
                'Northern elephant seals (Mirounga angustirostris) were hunted to 10–20 '
                'individuals in the 1890s. Today the population exceeds 100,000 — a full '
                'demographic recovery — yet heterozygosity at 24 protein-coding loci is '
                'effectively zero (Bonnell & Selander 1974). Cheetahs (Acinonyx jubatus) '
                'show a similar post-Pleistocene bottleneck signature.'
            ),
            mnemonic='10–20 seals → 100,000 seals, zero allozyme variation.',
            watchOut='Demographic recovery does NOT restore lost alleles.',
            value='10–20 → 100,000',
            color='purple',
        ),
        make_node(
            id='bn_key',
            label='Bottleneck: key point',
            detail=(
                'The original population existed before and after. Random survivors carry a '
                'biased sample of the ancestral allele frequencies — rare alleles are usually '
                'lost, common alleles sometimes overrepresented.'
            ),
            mnemonic='Rare alleles die first in a bottleneck.',
            watchOut='Rare deleterious alleles CAN drift to high frequency by luck.',
            color='purple',
        ),
        make_node(
            id='bn_mechanism',
            label='Bottleneck: mechanism',
            detail=(
                'Drift acts on the small surviving population, fixing some alleles and losing '
                'others over subsequent generations. Even if size rebounds quickly, the '
                'post-bottleneck allele frequencies reflect the few survivors — a long-lasting '
                'signature detectable in genome scans for decades to millennia.'
            ),
            mnemonic='Small N → strong drift → alleles fix or disappear.',
            watchOut='Heterozygosity rebounds slowly (Ne limits mutation-drift equilibrium).',
            color='purple',
        ),
        make_node(
            id='bn_timing',
            label='Bottleneck: timing',
            detail=(
                'Happens in place, to an existing population. The temporal signature is a '
                'single crash-and-recovery. Compare: disease outbreaks, overharvesting, ice-age '
                'range contractions.'
            ),
            mnemonic='Temporal compression, no geographic move.',
            watchOut='A bottleneck can repeat — each crash strips more variation.',
            color='purple',
        ),
        # RIGHT COLUMN — FOUNDER EFFECT
        make_node(
            id='fd_def',
            label='Founder effect: definition',
            detail=(
                'Loss of allelic variation that occurs when a NEW population is founded by a '
                'small subset of individuals from a larger source population. Drift operates '
                'immediately on the small founding group, so the new population starts with '
                'allele frequencies that may differ substantially from the source.'
            ),
            mnemonic='Founder = break off a new population.',
            watchOut='The source population survives unchanged; only the daughter is bottlenecked.',
            color='pink',
        ),
        make_node(
            id='fd_example',
            label='Founder effect: Amish & Pingelap',
            detail=(
                'Pingelap atoll (Micronesia): a 1775 typhoon killed most of the ~1,000 '
                'residents; ~20 survivors rebuilt, and a carrier of autosomal-recessive '
                'achromatopsia (CNGB3 gene) was among them. Today ~10% of Pingelapese are '
                'colorblind vs ~0.003% globally. Also: the Lancaster County Amish (Ellis–van '
                'Creveld syndrome at ~7%) and founding colonizers of the Galápagos.'
            ),
            mnemonic='Pingelap atoll: 1 carrier + 20 survivors → 10% colorblind.',
            watchOut='Founder alleles can be rare globally but locally near-fixed.',
            value='~10% colorblind',
            color='pink',
        ),
        make_node(
            id='fd_key',
            label='Founder effect: key point',
            detail=(
                'A new population is established by a handful of migrants whose combined '
                'alleles are a biased sample of the source. The daughter population’s '
                'frequency differs from the source from generation zero onward, then drifts '
                'further in isolation.'
            ),
            mnemonic='Small founding group = biased allele sample from day one.',
            watchOut='Founder effects look identical to selection for low-frequency alleles — use neutral markers to distinguish.',
            color='pink',
        ),
        make_node(
            id='fd_mechanism',
            label='Founder effect: mechanism',
            detail=(
                'The small founding group is a random, biased sample of the source gene pool. '
                'Subsequent reproduction amplifies whatever alleles the founders brought; '
                'alleles absent in the founders cannot reappear without migration or new mutation.'
            ),
            mnemonic='Founders determine the starting deck; drift shuffles it.',
            watchOut='Absent alleles stay absent unless new migration or mutation reintroduces them.',
            color='pink',
        ),
        make_node(
            id='fd_timing',
            label='Founder effect: timing',
            detail=(
                'Happens at the origin of a new population — geographic colonization, '
                'refugium establishment, or captive-breeding release. The signature is '
                'immediate divergence from the source and reduced heterozygosity.'
            ),
            mnemonic='Geographic move creates the new population.',
            watchOut='Serial founder effects (wave-of-advance colonization) compound variance loss.',
            color='pink',
        ),
        # BURI REFERENCE / watchOut node
        make_node(
            id='buri',
            label='Buri 1956: drift baseline',
            detail=(
                'Peter Buri (1956) ran 107 Drosophila melanogaster populations with exactly '
                '8 males + 8 females per generation for 19 generations, tracking the brown-eye '
                'bw75 allele starting at p = 0.5. By generation 19, 28 populations had fixed '
                'bw75 and 30 had lost it entirely — demonstrating that pure drift drives '
                'alleles to fixation or loss randomly in small populations.'
            ),
            mnemonic='Buri: 107 pops, 16 flies/pop, 19 gens → 58/107 fixed or lost.',
            watchOut=(
                'Bottleneck effects PERSIST even after recovery — lost alleles are gone '
                'permanently. Only new mutation or gene flow can replace them.'
            ),
            value='107 pops × 19 gens',
            color='teal',
        ),
    ]
    edges = [
        make_edge('bn_def', 'bn_example', label='illustrated by', style='arrow'),
        make_edge('bn_example', 'bn_key', label='shows', style='arrow'),
        make_edge('bn_key', 'bn_mechanism', label='operates via', style='arrow'),
        make_edge('bn_mechanism', 'bn_timing', label='occurs as', style='arrow'),
        make_edge('fd_def', 'fd_example', label='illustrated by', style='arrow'),
        make_edge('fd_example', 'fd_key', label='shows', style='arrow'),
        make_edge('fd_key', 'fd_mechanism', label='operates via', style='arrow'),
        make_edge('fd_mechanism', 'fd_timing', label='occurs as', style='arrow'),
        make_edge('buri', 'bn_mechanism', label='quantifies drift for', style='dashed'),
        make_edge('buri', 'fd_mechanism', label='quantifies drift for', style='dashed'),
    ]
    return validate_diagram({
        'type': 'compare',
        'title': 'Genetic Drift — Bottleneck vs. Founder Effect',
        'nodes': nodes,
        'edges': edges,
        'mnemonic': 'Bottleneck = squeeze existing population. Founder = break off a new one. Both reduce variation via drift.',
    }, node_id='genetic_drift_bottleneck_vs_founder')
