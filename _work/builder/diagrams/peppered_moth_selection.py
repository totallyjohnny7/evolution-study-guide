"""Peppered moth (Biston betularia) industrial melanism selection calculation."""
from .types import make_node, make_edge, validate_diagram


def peppered_moth_selection_diagram():
    """Single-generation selection math for Biston betularia with Lec-style fitness values."""
    nodes = [
        make_node(
            id='initial',
            label='Initial population',
            detail=(
                'Starting allele frequencies at the carbonaria (B) locus: p = 0.5, q = 0.5. '
                'Under HWE this yields genotype frequencies f(BB) = 0.25, f(Bb) = 0.50, '
                'f(bb) = 0.25. Kettlewell’s 1950s mark–release–recapture experiments in '
                'polluted Birmingham vs unpolluted Dorset woodlands made this the textbook '
                'case for natural selection in action.'
            ),
            mnemonic='Start at p=q=0.5 so selection signal is easy to see.',
            watchOut='Real pre-industrial frequencies of carbonaria were <1%, not 50% — this is a teaching setup.',
            value='p=0.5, q=0.5',
            color='amber',
        ),
        make_node(
            id='bb_survival',
            label='bb survival (white)',
            detail=(
                'Homozygous recessive bb moths are light-colored ("typica" morph). On '
                'pollution-blackened bark in industrial Britain they are conspicuous to '
                'visually hunting birds. Empirical survival probability = 0.55.'
            ),
            mnemonic='White on black bark = bird food.',
            watchOut='Survival, not reproduction, is what this line measures — the two can diverge.',
            value='0.55',
            color='coral',
        ),
        make_node(
            id='bb_survival_AA',
            label='BB survival (dark)',
            detail=(
                'Homozygous dominant BB moths are dark (carbonaria). They are cryptic against '
                'soot-covered bark. Empirical survival probability = 0.90 in polluted woodlands.'
            ),
            mnemonic='Dark on black = hidden from birds.',
            watchOut='Reverse the pattern after 1956 Clean Air Act — BB became the visible morph.',
            value='0.90',
            color='teal',
        ),
        make_node(
            id='bb_survival_Aa',
            label='Bb survival (dark)',
            detail=(
                'Heterozygotes are also dark because B is dominant. Empirical survival = 0.87, '
                'slightly lower than BB homozygotes due to incomplete dominance in some '
                'populations. Dominance here is at the pigmentation level, not fitness.'
            ),
            mnemonic='Dominance hides bb from selection through heterozygotes.',
            watchOut='Heterozygote survival (0.87) is slightly below BB (0.90) — not perfectly dominant.',
            value='0.87',
            color='teal',
        ),
        make_node(
            id='rel_fitness_BB',
            label='w(BB) relative fitness',
            detail=(
                'Set the highest-surviving genotype to w = 1. BB has the highest survival '
                '(0.90), so w(BB) = 0.90 / 0.90 = 1.00. All other fitnesses are rescaled '
                'against this reference.'
            ),
            mnemonic='Highest survivor always gets w = 1.',
            watchOut='Relative fitness is unitless; absolute fitness drops out.',
            value='1.00',
            color='green',
        ),
        make_node(
            id='rel_fitness_Aa',
            label='w(Bb) relative fitness',
            detail=(
                'w(Bb) = 0.87 / 0.90 = 0.9667 ≈ 0.96. Heterozygote selection coefficient '
                's_Bb = 1 − 0.96 = 0.04, a modest disadvantage relative to BB.'
            ),
            mnemonic='w(Bb) = survival(Bb) ÷ survival(best).',
            watchOut='A 4% disadvantage per generation still causes rapid frequency shifts.',
            value='0.96',
            color='green',
        ),
        make_node(
            id='rel_fitness_bb',
            label='w(bb) relative fitness',
            detail=(
                'w(bb) = 0.55 / 0.90 = 0.6111 ≈ 0.61. Selection coefficient '
                's_bb = 1 − 0.61 = 0.39, a huge fitness disadvantage. Historically matched by '
                'observed carbonaria frequency rising from <1% to 98% in Manchester by 1895.'
            ),
            mnemonic='s = 1 − (w / w_best).',
            watchOut='Very strong selection (s = 0.39) explains the observed rapid industrial melanism.',
            value='0.61',
            color='green',
        ),
        make_node(
            id='new_p',
            label="p' after selection",
            detail=(
                'Mean fitness w̄ = p²·w(BB) + 2pq·w(Bb) + q²·w(bb) '
                '= 0.25(1.00) + 0.50(0.96) + 0.25(0.61) = 0.8825. '
                "Weighted allele contribution: p' = [p²·w(BB) + pq·w(Bb)] / w̄ "
                '= [0.25 + 0.24] / 0.8825 = 0.4917 / 0.8825 ≈ 0.557.'
            ),
            mnemonic="p' = (AA frequency + ½ Aa frequency) weighted by fitness.",
            watchOut='Do not forget the 1/2 factor for heterozygote contribution to the A allele pool.',
            value="p'=0.557",
            color='teal',
        ),
        make_node(
            id='delta',
            label='Δp = +0.057',
            detail=(
                "Δp = p' − p = 0.557 − 0.500 = +0.057. In ONE generation the B allele has "
                'increased by 5.7 percentage points. Over 20 generations at similar intensity '
                'the frequency rises from ~0.01 to >0.9 — matching the Manchester data '
                'Kettlewell documented.'
            ),
            mnemonic='Positive selection on B allele → Δp > 0.',
            watchOut='Δp depends on current p — selection slows as favored allele approaches fixation.',
            value='+0.057',
            color='green',
        ),
    ]
    edges = [
        make_edge('initial', 'bb_survival', label='observe survival', style='arrow'),
        make_edge('initial', 'bb_survival_Aa', label='observe survival', style='arrow'),
        make_edge('initial', 'bb_survival_AA', label='observe survival', style='arrow'),
        make_edge('bb_survival_AA', 'rel_fitness_BB', label='normalize to w_max', style='arrow'),
        make_edge('bb_survival_Aa', 'rel_fitness_Aa', label='normalize to w_max', style='arrow'),
        make_edge('bb_survival', 'rel_fitness_bb', label='normalize to w_max', style='arrow'),
        make_edge('rel_fitness_BB', 'new_p', label='weighted average', style='arrow'),
        make_edge('rel_fitness_Aa', 'new_p', label='weighted average', style='arrow'),
        make_edge('rel_fitness_bb', 'new_p', label='weighted average', style='arrow'),
        make_edge('new_p', 'delta', label="Δp = p' − p", style='arrow'),
    ]
    return validate_diagram({
        'type': 'flow',
        'title': 'Peppered Moth — One Generation of Selection (Biston betularia)',
        'nodes': nodes,
        'edges': edges,
        'mnemonic': 's = 1 − (w / w_best). Higher fitness → higher frequency next generation.',
    }, node_id='peppered_moth_selection')
