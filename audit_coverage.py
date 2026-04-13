#!/usr/bin/env python3
"""Coverage audit: check every quiz question against study guide content."""
import json, re, sys

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
nodes = data['nodes']

def get_node_text(n):
    parts = [n.get('title',''), n.get('subtitle','')]
    if n.get('popup'):
        p = n['popup']
        parts.append(p.get('heading',''))
        for s in p.get('sections',[]):
            parts.append(s.get('label',''))
            parts.append(s.get('body',''))
        parts.extend(p.get('quotes',[]))
        parts.extend(p.get('examples',[]))
        parts.extend(p.get('warnings',[]))
        parts.append(p.get('mnemonic',''))
    if n.get('flashcard'):
        parts.extend([n['flashcard'].get('front',''), n['flashcard'].get('back','')])
    if n.get('v2') and n['v2'].get('flashcards'):
        for fc in n['v2']['flashcards']:
            parts.extend([fc.get('front',''), fc.get('back','')])
    if n.get('visual'):
        v = n['visual']
        parts.append(v.get('description',''))
        if v.get('regions'):
            for r in v['regions']:
                parts.append(r.get('label',''))
                parts.extend(r.get('items',[]))
    if n.get('diagram'):
        d = n['diagram']
        parts.extend([d.get('description',''), d.get('title','')])
        if d.get('nodes'):
            for dn in d['nodes']:
                parts.extend([dn.get('label',''), dn.get('detail','')])
    return ' '.join(str(p) for p in parts if p).lower()

# Build corpus
corpus = {}
all_parts = []
for n in nodes:
    t = get_node_text(n)
    corpus[n['id']] = t
    all_parts.append(t)
global_corpus = ' '.join(all_parts)
print(f"Corpus: {len(global_corpus):,} chars, {len(corpus)} nodes")

# Key bio concepts with regex patterns
CONCEPTS = [
    ('hamiltons_rule', r"hamilton.?s.?rule|rb\s*>\s*c"),
    ('hawk_dove', r'hawk.?dove'),
    ('kin_selection', r'kin\s+selection'),
    ('inclusive_fitness', r'inclusive\s+fitness'),
    ('reciprocal_altruism', r'reciprocal\s+altruism'),
    ('coevolution', r'coevolution|co-evolution'),
    ('evo_devo', r'evo.?devo|evolutionary\s+development'),
    ('hox_genes', r'hox\s+gene'),
    ('hardy_weinberg', r'hardy.?weinberg'),
    ('genetic_drift', r'genetic\s+drift'),
    ('bottleneck', r'bottleneck'),
    ('founder_effect', r'founder\s+effect'),
    ('gene_flow', r'gene\s+flow'),
    ('directional_sel', r'directional\s+selection'),
    ('stabilizing_sel', r'stabilizing\s+selection'),
    ('disruptive_sel', r'disruptive\s+selection'),
    ('freq_dependent', r'frequency.?dependent'),
    ('allopatric', r'allopatric'),
    ('sympatric', r'sympatric'),
    ('parapatric', r'parapatric'),
    ('prezygotic', r'prezygotic'),
    ('postzygotic', r'postzygotic'),
    ('phylogeny', r'phylogen'),
    ('cladistics', r'cladist'),
    ('synapomorphy', r'synapomorph'),
    ('parsimony', r'parsimony'),
    ('homoplasy', r'homoplasy'),
    ('convergent', r'convergent\s+evolution'),
    ('fitness_landscape', r'fitness\s+landscape'),
    ('plasticity', r'phenotypic\s+plasticity'),
    ('reaction_norm', r'reaction\s+norm'),
    ('heritability', r'heritability'),
    ('breeders_eq', r"breeder.?s.?equation"),
    ('exaptation', r'exaptation'),
    ('vestigial', r'vestigial'),
    ('batesian_mimicry', r'batesian'),
    ('mullerian_mimicry', r'mullerian|m.llerian'),
    ('endosymbiosis', r'endosymbiosis'),
    ('red_queen', r'red\s+queen'),
    ('anisogamy', r'anisogamy'),
    ('sperm_competition', r'sperm\s+competition'),
    ('sexual_conflict', r'sexual\s+conflict'),
    ('life_history', r'life\s+history'),
    ('senescence', r'senescence'),
    ('antag_pleiotropy', r'antagonistic\s+pleiotropy'),
    ('parental_invest', r'parental\s+investment'),
    ('game_theory', r'game\s+theory'),
    ('ess', r'evolutionarily\s+stable'),
    ('group_selection', r'group\s+selection'),
    ('tiktaalik', r'tiktaalik'),
    ('cambrian', r'cambrian'),
    ('mass_extinction', r'mass\s+extinction'),
    ('bdm', r'bateson.?dobzhansky.?muller|bdm\s+incompatib'),
    ('cryptic_species', r'cryptic\s+species'),
    ('mullers_ratchet', r"muller.?s.?ratchet"),
    ('good_genes', r'good\s+genes'),
    ('handicap', r'handicap\s+principle'),
    ('runaway', r'runaway\s+selection|fisherian\s+runaway'),
    ('reinforcement', r'reinforcement'),
    ('ring_species', r'ring\s+species'),
    ('peripatric', r'peripatric'),
    ('sexual_selection', r'sexual\s+selection'),
    ('intersexual', r'intersexual'),
    ('intrasexual', r'intrasexual'),
    ('operational_sex_ratio', r'operational\s+sex\s+ratio|osr'),
    ('sex_allocation', r'sex\s+allocation'),
    ('charnov', r'charnov'),
    ('inbreeding', r'inbreeding'),
    ('heterozygote_adv', r'heterozygote\s+advantage|overdominance'),
    ('balancing_sel', r'balancing\s+selection'),
    ('artificial_sel', r'artificial\s+selection'),
    ('homologous', r'homolog'),
    ('analogous', r'analogous'),
    ('monophyletic', r'monophyletic'),
    ('paraphyletic', r'paraphyletic'),
    ('polyphyletic', r'polyphyletic'),
    ('clade', r'\bclade\b'),
    ('outgroup', r'outgroup'),
    ('molecular_clock', r'molecular\s+clock'),
    ('neutral_theory', r'neutral\s+theory'),
    ('epigenetics', r'epigenetic'),
    ('punctuated_eq', r'punctuated\s+equilib'),
    ('gradualism', r'gradualism|phyletic\s+gradualism'),
    ('adaptive_radiation', r'adaptive\s+radiation'),
    ('polyploidy', r'polyploid'),
    ('allopolyploidy', r'allopolyploid'),
    ('autopolyploidy', r'autopolyploid'),
]

# STOP WORDS for filtering
STOP = {'following','because','through','between','example','however','another',
        'without','whether','usually','already','always','should','before',
        'during','several','against','certain','rather','primarily','represent',
        'statement','describes','correctly','according','identify','consider',
        'scenario','predict','expected','prediction','hypothesis','question',
        'likely','select','answer','choice','process','result','occurs'}

# Audit
audit_gaps = []
stats = {'full': 0, 'partial': 0, 'missing': 0}
lec_stats = {}

for n in nodes:
    nid = n['id']
    node_text = corpus[nid]
    lec = str(n.get('row', '?'))
    if lec not in lec_stats:
        lec_stats[lec] = {'full': 0, 'partial': 0, 'missing': 0, 'total': 0}

    for qi, q in enumerate(n.get('quiz', [])):
        qt = q.get('question', '').lower()
        ct = q.get('correct', '').lower()
        dt = ' '.join(q.get('distractors', [])).lower()
        all_q = qt + ' ' + ct + ' ' + dt

        gaps = []
        concepts_tested = []

        # Check which concepts this question tests
        for cname, cpat in CONCEPTS:
            if re.search(cpat, all_q):
                concepts_tested.append(cname)
                if not re.search(cpat, global_corpus):
                    gaps.append(f'{cname} missing from entire study guide')

        # Check correct answer key terms
        c_words = set(re.findall(r'\b[a-z]{6,}\b', ct)) - STOP
        missing_cw = [w for w in c_words if w not in node_text and w not in global_corpus]
        if len(missing_cw) > 2:
            gaps.append(f'Answer terms absent: {", ".join(missing_cw[:5])}')

        # Check question stem key terms
        q_words = set(re.findall(r'\b[a-z]{7,}\b', qt)) - STOP
        missing_qw = [w for w in q_words if w not in node_text and w not in global_corpus]
        if len(missing_qw) > 2:
            gaps.append(f'Question terms absent: {", ".join(missing_qw[:5])}')

        status = 'full' if not gaps else ('partial' if len(gaps) <= 1 else 'missing')
        stats[status] += 1
        lec_stats[lec][status] += 1
        lec_stats[lec]['total'] += 1

        if gaps:
            audit_gaps.append({
                'qid': f'{nid}_q{qi}',
                'lec': lec,
                'node': n['title'][:45],
                'q': qt[:120],
                'correct': ct[:80],
                'status': status,
                'concepts': concepts_tested,
                'gaps': gaps
            })

# Save
with open('coverage-audit.json', 'w', encoding='utf-8') as f:
    json.dump(audit_gaps, f, indent=2, ensure_ascii=False)

# Print summary
print(f"\n{'='*70}")
print(f"COVERAGE AUDIT RESULTS")
print(f"{'='*70}")
print(f"Total questions:     {sum(stats.values())}")
print(f"  Fully covered:     {stats['full']} ({100*stats['full']//sum(stats.values())}%)")
print(f"  Partially covered: {stats['partial']}")
print(f"  NOT covered:       {stats['missing']}")
print(f"\nGap entries saved: {len(audit_gaps)}")

print(f"\nBy lecture:")
for lec in sorted(lec_stats.keys(), key=lambda x: int(x) if x.isdigit() else 99):
    ls = lec_stats[lec]
    pct = 100 * ls['full'] // ls['total'] if ls['total'] else 0
    bar = '#' * (pct // 5) + '.' * (20 - pct // 5)
    print(f"  Lec{lec:>2s}: {ls['full']:>3d}/{ls['total']:>3d} full ({pct}%) [{bar}] partial={ls['partial']} missing={ls['missing']}")

# Gap concept counts
print(f"\nTop gap patterns:")
gap_counts = {}
for a in audit_gaps:
    for g in a['gaps']:
        key = g.split(':')[0].strip() if ':' in g else g.split(' ')[0]
        gap_counts[key] = gap_counts.get(key, 0) + 1
for g, c in sorted(gap_counts.items(), key=lambda x: -x[1])[:15]:
    print(f"  [{c:>3d}x] {g}")

# Show specific gap questions
print(f"\n{'='*70}")
print(f"QUESTIONS WITH GAPS (first 30):")
print(f"{'='*70}")
for a in audit_gaps[:30]:
    print(f"\n  [{a['status'].upper()}] Lec{a['lec']} | {a['node']}")
    print(f"  Q: {a['q']}")
    print(f"  Gaps: {'; '.join(a['gaps'])}")
