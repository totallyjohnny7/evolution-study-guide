#!/usr/bin/env python3
"""Merge 4 JSON mnemonic files → patch both HTML files with Remember-it blocks + SVG images."""
import os, sys, re, json, time
sys.stdout.reconfigure(encoding='utf-8')

REPO = "C:/Users/johnn/Desktop/School/Evolution_EVOL4230/evolution-study-guide"
WORK = f"{REPO}/_work"
REVIEW_HTML = f"{REPO}/public/exam3_review.html"
LECTURE_HTML = f"{REPO}/public/exam3_lecture.html"

JSON_FILES = [
    f"{WORK}/mnem_review_a.json",
    f"{WORK}/mnem_review_b.json",
    f"{WORK}/mnem_lecture_a.json",
    f"{WORK}/mnem_lecture_b.json",
]

# =========== Wait for JSON files =============
def wait_for_jsons(max_s=900):
    start = time.time()
    while time.time() - start < max_s:
        missing = [p for p in JSON_FILES if not os.path.exists(p)]
        if not missing:
            print(f"All 4 JSON files present after {int(time.time()-start)}s")
            return True
        print(f"Waiting... missing: {len(missing)}/4 — {[os.path.basename(p) for p in missing]}")
        time.sleep(15)
    return False

# =========== Load + merge =============
def load_all():
    mn = {}
    for p in JSON_FILES:
        if not os.path.exists(p):
            print(f"SKIP (missing): {os.path.basename(p)}")
            continue
        try:
            with open(p, encoding='utf-8') as f:
                data = json.load(f)
            for c in data.get('cards', []):
                q = c['q'].strip()
                mn[q] = {'analogy': c.get('analogy', '').strip(), 'why': c.get('why', '').strip()}
            print(f"  loaded {len(data.get('cards',[]))} from {os.path.basename(p)}")
        except Exception as e:
            print(f"  ERROR reading {p}: {e}")
    print(f"Total unique mnemonics: {len(mn)}")
    return mn

# =========== Image assignments =============
# Map question text → SVG slug for cards lacking images
IMG_MAP = {
    # Review ch3
    "Radiometric dating — mechanism": "decay_curve",
    "Half-life — definition": "halflife",
    "C-14 dating — half-life, range, what it dates": "isotopes",
    "K-Ar dating — half-life + what it dates": "kar_dating",
    "U-Pb dating — half-life + uses": "decay_curve",
    "Why Kelvin was wrong about Earth's age": "earth_clock",
    "Prebiotic soup hypothesis — what, where, when": "rna_world",
    "RNA World Hypothesis — what, why, how": "rna_world",
    "Biomarkers — what, when": "biomarkers",
    "LUCA — what, when, features": "luca",
    "Endosymbiotic Theory — what, evidence": "endosymbiosis",
    "Great Oxidation Event — what, when, consequence": "oxygenation",
    "Cambrian Explosion — when, what, why significant": "cambrian",
    "Tiktaalik roseae — why it matters": "tiktaalik",
    "K-Pg extinction — when, severity, cause": "kt_boundary",
    "Lagerstätte — definition + example": "lagerstaette",
    "Geologic period mnemonic": "geologic_timeline",
    # ch4
    "Phylogenetic tree — 5 components defined": "phylo_tree",
    "Sister taxa — definition": "sister_taxa",
    "Synapomorphy — definition + why it defines clades": "synapomorphy",
    "Monophyletic vs. Paraphyletic vs. Polyphyletic": "monophyletic",
    "Are 'Reptiles' monophyletic? Why not?": "paraphyletic",
    "Principle of parsimony": "parsimony",
    "Homoplasy — definition + 2 types": "homoplasy",
    "Homology vs. homoplasy — examples": "homology",
    "Convergent vs. parallel evolution": "convergent_examples",
    "Exaptation — definition + feather example": "exaptation",
    "Cladistics — what, who, how": "cladistics",
    "Outgroup comparison — what, why": "outgroup",
    "Molecular phylogenetics — what sequences used": "molecular_clock",
    "Phylogeography — definition": "area_phylogeny",
    "Bootstrap support — what it measures": "bootstrap",
    # ch13
    "Biological Species Concept (BSC) — definition + 3 failures": "bsc",
    "Morphospecies Concept — definition + failure": "bsc",
    "Phylogenetic Species Concept (PSC) — definition": "synapomorphy",
    "General Lineage Species Concept": "bsc",
    "3 steps of speciation (+ reinforcement)": "speciation_3step",
    "Prezygotic barriers — pre-mating (3 types)": "prezygotic",
    "Prezygotic barriers — post-mating pre-fertilization (2 types)": "gametic_incompatibility",
    "Postzygotic barriers — 2 types": "postzygotic",
    "Bateson-Dobzhansky-Muller (BDM) incompatibilities": "bdm",
    "Reinforcement — definition, mechanism, result": "reinforcement",
    "Allopatric speciation — steps, examples": "allopatric",
    "Sympatric speciation — definition, example": "sympatric",
    "Vicariance vs. dispersal — what, difference": "vicariance_vs_dispersal",
    "Allopolyploidy — instant speciation, how": "allopolyploidy",
    "Allopolyploidy — real-time examples": "allopolyploidy",
    "Haldane's Rule": "bdm",
    "Parapatric speciation": "parapatric",
    "Peripatric speciation (founder effect speciation)": "peripatric",
    "Hawaiian Laupala crickets — what they demonstrate": "peripatric",
    "Ecological speciation — what, why important": "sympatric",
    # ch14
    "Biogeography — definition": "continental_drift",
    "Continental drift — Pangaea timeline": "continental_drift",
    "Vicariance biogeography — principle": "vicariance",
    "Dispersal biogeography — principle": "dispersal_bio",
    "Island biogeography — MacArthur &amp; Wilson equilibrium": "island_biogeography",
    "Island biogeography — distance + area effects": "island_biogeography",
    "Wallace Line — what, significance": "wallace_line",
    "Species-area relationship (SAR)": "species_area",
    "Species-area relationship — habitat fragmentation consequences": "habitat_fragmentation",
    "Metapopulation dynamics": "metapopulation",
    "Conservation genetics — 50/500 rule": "50_500_rule",
    "Inbreeding depression — mechanism": "inbreeding_depression",
    "Area phylogeny — what it is": "area_phylogeny",
    "Gondwana vs. Laurasia — what each contained": "gondwana_laurasia",
    # ch8
    "Humans as selective force — 4 key examples": "pesticide_resistance",
    "Trophy hunting evolution — bighorn sheep example": "fishing_evolution",
    "Tusklessness in African elephants": "fishing_evolution",
    "Antibiotic resistance — how it evolves": "pesticide_resistance",
    "4 mechanisms of antibiotic resistance": "pesticide_resistance",
    "Atlantic cod — fishing-driven evolution": "fishing_evolution",
    "Industrial melanism — peppered moth": "pesticide_resistance",
    "Habitat fragmentation + genetic consequences": "habitat_fragmentation",
    "Selective breeding vs. natural selection": "fishing_evolution",
    "Why fishing-driven evolution is real evolution, not plasticity": "fishing_evolution",
    # ch17
    "Why Linnaeus classified humans as primates": "hominins_vs_hominids",
    "Molecular evidence of human-chimp kinship": "molecular_clock",
    "Did humans evolve FROM chimpanzees? Why not?": "hominin_timeline",
    "Sahelanthropus tchadensis — key features": "hominin_timeline",
    "Ardipithecus ramidus — key features": "hominin_timeline",
    "Homo erectus — key facts": "hominin_timeline",
    "Homo sapiens — origin + timeline": "out_of_africa",
    "Bipedalism — when did it evolve?": "bipedalism_anatomy",
    "4 anatomical markers of bipedalism": "bipedalism_anatomy",
    "Why did bipedalism evolve? 2 main hypotheses": "bipedalism_anatomy",
    "Bipedalism costs — maladaptations": "bipedalism_anatomy",
    "Hominin tool traditions in chronological order": "tool_traditions",
    "FOXP2 gene — what it is, why it matters": "brain_evolution",
    "Out of Africa hypothesis — evidence": "out_of_africa",
    "Neanderthal DNA in modern humans": "neanderthal_dna",
    "Denisovans — who, where, legacy": "denisovan",
    "Adaptive introgression — definition + examples": "adaptive_introgression",
    "Anatomically vs. behaviorally modern H. sapiens": "hominin_timeline",
    "Cooking hypothesis (Wrangham)": "cooking_hypothesis",
    "MHC and human mate choice": "mhc_diversity",
    # ch18
    "Evolutionary medicine — definition + why it matters": "nesse_6_reasons",
    "Nesse's 6 reasons we get sick": "nesse_6_reasons",
    "Reason 1: Pathogens evolve faster": "red_queen",
    "Reason 2: Evolutionary mismatch": "mismatch_disease",
    "Reason 3: Trade-offs": "sickle_cell_advantage",
    "Reason 4: Evolutionary constraints": "evolutionary_constraints",
    "Reason 5: Antagonistic pleiotropy (aging)": "antagonistic_pleiotropy",
    "Reason 6: Apparent disease = adaptation": "fever_adaptive",
    "Antagonistic pleiotropy vs. mutation accumulation (aging)": "antagonistic_pleiotropy",
    "p53 — antagonistic pleiotropy example": "p53_pleiotropy",
    "Virulence — definition + trade-off": "virulence_tradeoff",
    "Why cholera maintains high virulence": "virulence_tradeoff",
    "Antibiotic resistance — evolutionary medicine angle": "pesticide_resistance",
    "Cancer as somatic evolution": "cancer_evolution",
    "Hygiene hypothesis": "hygiene_hypothesis",
    "Myxoma virus — evolutionary case study": "myxoma_coevolution",
    "Mismatch disease examples": "mismatch_disease",
    "Evolutionary mismatch — back pain": "bipedalism_anatomy",
    "Peto's paradox — cancer resistance in large animals": "peto_paradox",
    "Conserved gene networks in evolutionary medicine": "co_evolution",
    # Traps
    "TRAP: Using C-14 to date dinosaur fossils": "isotopes",
    "TRAP: 'Reptiles' are a valid taxonomic group": "paraphyletic",
    "TRAP: K-Pg was the largest mass extinction": "big5",
    "TRAP: Antibiotics cause bacteria to mutate": "pesticide_resistance",
    "TRAP: Humans evolved from chimpanzees": "hominin_timeline",
    "TRAP: Bipedalism evolved AFTER large brains": "hominin_timeline",
    "TRAP: BSC works for all organisms": "bsc",
    "TRAP: Mule is an example of hybrid inviability": "mule_sterility",
    "TRAP: Island biogeography equilibrium never changes": "island_biogeography",
    "TRAP: Virulence always evolves lower over time": "virulence_tradeoff",
    "TRAP: FOXP2 is 'the language gene'": "brain_evolution",
    "TRAP: Global species diversity = immigration + extinction": "standing_diversity",
    "TRAP: In vicariance, organisms MOVE; in dispersal, barriers move": "vicariance_vs_dispersal",
    "TRAP: Neanderthal brain was smaller than modern human brain": "brain_evolution",
    "TRAP: Miller-Urey experiment produced living cells": "rna_world",
    "TRAP: Feathers evolved for flight": "exaptation",
    "TRAP: Antagonistic pleiotropy = one gene with two pleiotropic effects": "antagonistic_pleiotropy",
    "TRAP: Synapomorphies = any shared character": "synapomorphy",
    "TRAP: Allopolyploidy requires geographic isolation": "allopolyploidy",
    "TRAP: Sickle cell heterozygote fitness in malaria region": "sickle_cell_advantage",
    "TRAP: Cancer is not evolution": "cancer_evolution",
    "TRAP: Anatomically modern = behaviorally modern": "hominin_timeline",
    "TRAP: Denisovan DNA = same distribution as Neanderthal": "denisovan",
    # Lecture s1-s7 → SVG map
    "Radiometric Dating": "decay_curve",  # already has p002 — keep override later
    "Half-life": "halflife",
    "Isotopes": "isotopes",
    "Biomarkers": "biomarkers",
    "Stromatolites": "stromatolites",
    "K-T Boundary": "kt_boundary",
    "RNA World Hypothesis": "rna_world",
    "Earth's age": "earth_clock",
    "Okenane": "biomarkers",
    "Endosymbiotic theory": "endosymbiosis",
    "Great Oxygenation Event": "oxygenation",
    "Cambrian Explosion": "cambrian",
    "Permian Mass Extinction": "permian",
    "Devonian Period highlights": "tiktaalik",
    "How does radiometric dating work?": "decay_curve",
    "What is the K-T boundary?": "kt_boundary",
    "Evidence for endosymbiosis": "endosymbiosis",
    "Devonian tetrapod transition evidence": "tiktaalik",
    "What makes a good biomarker?": "biomarkers",
    "Natural selection vs. genetic drift": "bottleneck",
    "Evidence that life has a single common ancestor": "luca",
    "Precambrian timeline": "precambrian",
    "Earliest undisputed life evidence": "earliest_life",
    "Ribozymes": "ribozymes",
    "K-Ar dating (Potassium-Argon)": "kar_dating",
    "Burgess Shale": "burgess_shale",
    "Why is the RNA World hypothesis compelling?": "rna_world",
    "Ordovician extinction cause": "ordovician_ext",
    "What makes fossils form?": "lagerstaette",
    "Three Domains of Life": "three_domains",
    "Ediacaran Biota": "ediacaran",
    "Geological Period Timeline": "geologic_timeline",
    "Circumstellar Disk and Earth's Formation": "circumstellar_disk",
    "Synapomorphy": "synapomorphy",
    "Symplesiomorphy": "symplesiomorphy",
    "Monophyletic group (clade)": "monophyletic",
    "Paraphyletic group": "paraphyletic",
    "Polyphyletic group": "polyphyletic",
    "Homoplasy": "homoplasy",
    "Convergent evolution": "convergent_examples",
    "Principle of Parsimony": "parsimony",
    "Exaptation": "exaptation",
    "Tiktaalik": "tiktaalik",
    "Cladistics": "cladistics",
    "Tree components": "phylo_tree",
    "Homology": "homology",
    "Molecular phylogenetics": "molecular_clock",
    "Outgroup": "outgroup",
    "How do synapomorphies build phylogenetic trees?": "synapomorphy",
    "Why are paraphyletic groups problematic?": "paraphyletic",
    "Convergence vs. homology — how to distinguish?": "homology",
    "Swim bladder → lungs exaptation": "exaptation",
    "What is a transitional fossil?": "transitional_fossil",
    "Phylogeny and classification": "phylo_classification",
    "Convergent evolution examples": "convergent_examples",
    "Molecular clock": "molecular_clock",
    "Bootstrap support": "bootstrap",
    "Morphological vs. molecular phylogenetics — conflicts": "morpho_vs_molec",
    "Tree topology vs. branch length": "tree_topology",
    "Maximum likelihood phylogenetics": "max_likelihood",
    "Feathers as exaptation": "exaptation",
    "Rooting a tree": "rooting_tree",
    "Character state matrix": "character_matrix",
    "Whale evolution — exaptation example": "exaptation",
    "Biological Species Concept (BSC)": "bsc",
    "Morphospecies Concept": "bsc",
    "Phylogenetic Species Concept (PSC)": "synapomorphy",
    "General Lineage Species Concept": "bsc",
    "Three-step speciation": "speciation_3step",
    "Prezygotic barriers (pre-mating)": "prezygotic",
    "Prezygotic barriers (post-mating)": "gametic_incompatibility",
    "Postzygotic barriers": "postzygotic",
    "Allopatric speciation": "allopatric",
    "Sympatric speciation": "sympatric",
    "Reinforcement": "reinforcement",
    "Rhagoletis pomonella": "sympatric",
    "Peripatric speciation": "peripatric",
    "Primary mechanisms of reproductive isolation?": "prezygotic",
    "Why can't the BSC apply to fossils?": "bsc",
    "Rhagoletis — mechanism of sympatric speciation": "sympatric",
    "Tempo of evolution: gradualism vs. punctuated equilibrium": "tempo_evolution",
    "Character displacement": "character_displacement",
    "Hybrid zone": "hybrid_zone",
    "Polyploidy — instant sympatric speciation": "allopolyploidy",
    "Reproductive isolation continuum": "speciation_3step",
    "Temporal isolation example": "temporal_isolation",
    "Gametic incompatibility mechanism": "gametic_incompatibility",
    "Biogeography": "continental_drift",
    "Dispersal": "dispersal_bio",
    "Vicariance": "vicariance",
    "Phylogeography": "area_phylogeny",
    "Area phylogeny": "area_phylogeny",
    "Adaptive radiation": "adaptive_radiation",
    "Key innovation": "adaptive_radiation",
    "Standing Diversity equation": "standing_diversity",
    "Island Biogeography Theory": "island_biogeography",
    "Species–area relationship": "species_area",
    "Big Five mass extinctions": "big5",
    "Background extinction rate": "big5",
    "Hawaiian honeycreepers": "adaptive_radiation",
    "Marsupial biogeography": "continental_drift",
    "Turnover rate": "island_biogeography",
    "Dispersal vs. vicariance — how to distinguish?": "vicariance_vs_dispersal",
    "Why do islands support adaptive radiations?": "adaptive_radiation",
    "Island biogeography — conservation applications": "island_biogeography",
    "Continental drift and biogeography": "continental_drift",
    "Darwin's finches adaptive radiation": "darwin_finches",
    "East African cichlid radiation": "cichlid_radiation",
    "SLOSS debate": "sloss_debate",
    "Taxon cycle": "taxon_cycle",
    "Endemism": "endemism",
    "Origination vs. extinction rates": "standing_diversity",
    "Great American Biotic Interchange": "great_american_interchange",
    "Laupala Hawaiian Crickets": "peripatric",
    "Selective Pressure": "pesticide_resistance",
    "Conservation Biology": "extinction_vortex",
    "Artificial selection (domestication)": "fishing_evolution",
    "Extinction vortex": "extinction_vortex",
    "Inbreeding depression": "inbreeding_depression",
    "Greater prairie chicken case study": "genetic_rescue",
    "Four anthropogenic causes of biodiversity loss": "sixth_extinction",
    "Fishing and life-history evolution": "fishing_evolution",
    "Sixth mass extinction": "sixth_extinction",
    "Trophy hunting and evolution": "fishing_evolution",
    "Pesticide resistance evolution": "pesticide_resistance",
    "Genetic rescue": "genetic_rescue",
    "How do humans act as selective forces?": "pesticide_resistance",
    "Conservation genetics — why genetic diversity matters": "50_500_rule",
    "Minimum viable population (MVP)": "mvp",
    "Population bottleneck effects": "bottleneck",
    "Why conservation matters evolutionarily": "50_500_rule",
    "Human population growth and extinction": "sixth_extinction",
    "Habitat fragmentation effects": "habitat_fragmentation",
    "Allee effect": "allee_effect",
    "Ex situ conservation": "genetic_rescue",
    "Pollution and evolution": "pesticide_resistance",
    "Climate change and biodiversity": "sixth_extinction",
    "Effective population size (Ne)": "effective_pop_size",
    "Trophy hunting evolution — bighorn sheep": "fishing_evolution",
    "Hominids": "hominins_vs_hominids",
    "Bipedalism": "bipedalism_anatomy",
    "Fossil Evidence (human evolution)": "hominin_timeline",
    "Sahelanthropus tchadensis": "hominin_timeline",
    "Australopithecus afarensis": "hominin_timeline",
    "Laetoli footprints": "bipedalism_anatomy",
    "Homo habilis": "tool_traditions",
    "Homo erectus": "out_of_africa",
    "Homo sapiens": "hominin_timeline",
    "Out of Africa model": "out_of_africa",
    "Neanderthals": "neanderthal_dna",
    "What evidence supports bipedalism evolving first?": "bipedalism_anatomy",
    "Significance of early hominin fossils in Chad": "hominin_timeline",
    "How did environment shape human evolution?": "bipedalism_anatomy",
    "Hominin brain size evolution": "brain_evolution",
    "Molecular clock and human-chimp divergence": "molecular_clock",
    "Multiregional vs. Out of Africa": "multiregional_vs_ooa",
    "Denisovans": "denisovan",
    "Skeletal adaptations for bipedalism": "bipedalism_anatomy",
    "Oldowan vs. Acheulean tools": "tool_traditions",
    "Hominins vs. Hominids": "hominins_vs_hominids",
    "Bipedalism trade-offs": "bipedalism_anatomy",
    "Ardipithecus": "hominin_timeline",
    "Australopithecus — key species": "hominin_timeline",
    "Homo floresiensis and Homo heidelbergensis": "hominin_timeline",
    "Co-evolution": "co_evolution",
    "Virulence": "virulence_tradeoff",
    "Virulence–transmission trade-off": "virulence_tradeoff",
    "Antibiotic resistance": "pesticide_resistance",
    "Red Queen hypothesis": "red_queen",
    "Mismatch theory": "mismatch_disease",
    "Antagonistic pleiotropy": "antagonistic_pleiotropy",
    "Fever as adaptive response": "fever_adaptive",
    "MHC diversity and disease resistance": "mhc_diversity",
    "Why do pathogens evolve resistance to antibiotics?": "pesticide_resistance",
    "How do pathogens evolve alongside human hosts?": "red_queen",
    "Role of natural selection in antibiotic resistance": "pesticide_resistance",
    "Modern lifestyle and disease evolution": "mismatch_disease",
    "Sickle-cell anemia and malaria — evolutionary medicine": "sickle_cell_advantage",
    "Why sexual reproduction maintains allele diversity": "mhc_diversity",
    "Antagonistic pleiotropy aging theory": "antagonistic_pleiotropy",
    "Evolutionary medicine definition": "nesse_6_reasons",
    "Hypertension and evolutionary mismatch": "mismatch_disease",
    "Vestigial structures in medicine": "evolutionary_constraints",
    "Pathogen evolution toward lower virulence?": "myxoma_coevolution",
    "Why do we get sick? Evolutionary framework": "nesse_6_reasons",
    "Horizontal gene transfer and drug resistance": "horizontal_gene_transfer",
    "Nausea in pregnancy — evolutionary function": "nausea_pregnancy",
    "Evolution of immune specificity": "mhc_diversity",
    "Five evolutionary reasons we get sick": "nesse_6_reasons",
    "Evolutionary constraints in medicine": "evolutionary_constraints",
    "Obesity, Type 2 Diabetes, and Mismatch": "mismatch_disease",
    "Inflammation as an adaptive defense — and mismatch": "inflammation_mismatch",
    "Parapatric speciation": "parapatric",
}

# Fix the known 8 image mismatches in lecture FLASH
LECTURE_IMAGE_OVERRIDES = {
    "Monophyletic group (clade)": "/img/fc/svg_monophyletic.svg",
    "Tree components": "/img/fc/svg_phylo_tree.svg",
    "Homoplasy": "/img/fc/svg_homoplasy.svg",
    "Principle of Parsimony": "/img/fc/svg_parsimony.svg",
    "Endosymbiotic theory": "/img/fc/svg_endosymbiosis.svg",
    "Sympatric speciation": "/img/fc/svg_sympatric.svg",
    "Island biogeography — conservation applications": "/img/fc/svg_island_biogeography.svg",
    "Character state matrix": "/img/fc/svg_character_matrix.svg",
}

def html_escape(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')

def js_escape(s):
    return s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', ' ')

# =========== Patch review HTML =============
def patch_review(mn):
    with open(REVIEW_HTML, encoding='utf-8') as f:
        html = f.read()

    patched = 0
    skipped_no_mn = 0

    # Regex: match the fc2 multi-line block and extract the ff2 question text + fb2 content
    # Card structure:
    # <div class="fc2" data-ch="XX" onclick="...">\n<div class="fi2">\n<div class="ff2"><div class="chip">...</div>QUESTION</div>\n<div class="fb2">...BACK...</div>\n</div></div>

    pattern = re.compile(
        r'(<div class="fc2" data-ch="[^"]*" onclick="[^"]*">\s*<div class="fi2">\s*<div class="ff2">(?:<div class="chip">[^<]*</div>)?)([^<]+)(</div>\s*<div class="fb2">)(.*?)(</div>\s*</div></div>)',
        re.DOTALL
    )

    def replacer(m):
        nonlocal patched, skipped_no_mn
        front_prefix = m.group(1)
        question = m.group(2).strip()
        mid = m.group(3)
        back_content = m.group(4)
        suffix = m.group(5)

        # Skip if already has fc-mn
        if 'fc-mn' in back_content:
            return m.group(0)

        mnem = mn.get(question)
        # Try also HTML-decoded key (& vs &amp;)
        if not mnem:
            mnem = mn.get(question.replace('&amp;', '&'))
        if not mnem:
            mnem = mn.get(question.replace('&', '&amp;'))

        # Add image if missing
        img_html = ''
        has_img = '<img' in back_content
        if not has_img:
            slug = IMG_MAP.get(question) or IMG_MAP.get(question.replace('&amp;', '&')) or IMG_MAP.get(question.replace('&', '&amp;'))
            if slug:
                img_html = f'<img alt="" loading="lazy" src="/img/fc/svg_{slug}.svg" style="max-width:100%;max-height:140px;border-radius:8px;margin-top:10px;object-fit:contain;display:block;background:#0a1220;border:1px solid #2a2a2a"/>'

        # Add mnemonic
        mn_html = ''
        if mnem and mnem.get('analogy'):
            a = html_escape(mnem['analogy'])
            w = html_escape(mnem['why'])
            mn_html = f'<div class="fc-mn"><div class="fc-mn-l">🧠 Remember it</div><div class="fc-mn-a">{a}</div><div class="fc-mn-w">{w}</div></div>'
            patched += 1
        else:
            skipped_no_mn += 1

        return front_prefix + m.group(2) + mid + back_content + img_html + mn_html + suffix

    new_html = pattern.sub(replacer, html)

    # Add CSS if not present
    css_block = '''
.fc-mn{margin-top:10px;padding:9px 11px;background:#0d0d0d;border-left:3px solid var(--green);border-radius:5px;text-align:left;font-size:11px;line-height:1.5}
.fc-mn-l{font-size:9px;text-transform:uppercase;letter-spacing:.8px;font-weight:700;color:var(--green);margin-bottom:4px}
.fc-mn-a{color:#86efac;font-style:italic;margin-bottom:4px;font-size:12px}
.fc-mn-w{color:#cfd6dc;font-size:11px}
#dk-b .fc-mn{font-size:12px;margin-top:10px}
#dk-b .fc-mn-a{font-size:13px}
#dk-b .fc-mn-w{font-size:12px}
'''
    if '.fc-mn{' not in new_html:
        new_html = new_html.replace('</style>', css_block + '</style>', 1)

    with open(REVIEW_HTML, 'w', encoding='utf-8') as f:
        f.write(new_html)

    print(f"REVIEW: patched {patched} / skipped {skipped_no_mn}")
    return patched

# =========== Patch lecture HTML =============
def patch_lecture(mn):
    with open(LECTURE_HTML, encoding='utf-8') as f:
        html = f.read()

    # Extract FLASH array
    start = html.find('const FLASH = [')
    end = html.find('];', start) + 2
    flash_str = html[start + len('const FLASH = '):end-1].strip().rstrip(';')
    clean = re.sub(r'/\*.*?\*/', '', flash_str, flags=re.DOTALL)
    cards = json.loads(clean)

    print(f"LECTURE: {len(cards)} cards in FLASH array")

    patched = 0
    for c in cards:
        q = c['q']
        mnem = mn.get(q)
        if not mnem:
            mnem = mn.get(q.replace('&amp;', '&'))
        if mnem and mnem.get('analogy'):
            c['mnemonic'] = {'analogy': mnem['analogy'], 'why': mnem['why']}
            patched += 1
        # Image fixes
        if q in LECTURE_IMAGE_OVERRIDES:
            c['img'] = LECTURE_IMAGE_OVERRIDES[q]
        elif not c.get('img'):
            slug = IMG_MAP.get(q)
            if slug:
                c['img'] = f'/img/fc/svg_{slug}.svg'

    new_flash = 'const FLASH = ' + json.dumps(cards, ensure_ascii=False, indent=0).replace('\n', '\n') + ';'
    # Compact (one card per line)
    lines = []
    lines.append('const FLASH = [')
    for i, c in enumerate(cards):
        line = json.dumps(c, ensure_ascii=False)
        lines.append(line + (',' if i < len(cards) - 1 else ''))
    lines.append('];')
    new_flash = '\n'.join(lines)

    new_html = html[:start] + new_flash + html[end:]

    # Update the grid card builder to render mnemonic
    old_grid = r'''html += `<div class="fc2" data-ch="\$\{s\}" onclick="this\.classList\.toggle\('flipped'\)"><div class="fi2"><div class="ff2"><div class="chip">\$\{m\.chip\}</div>\$\{esc\(c\.q\)\}</div><div class="fb2"><div class="verdict">Answer</div>\$\{esc\(c\.a\)\}\$\{c\.img\?`<img class='fc-img' src='\$\{c\.img\}' alt='' loading='lazy'>`:''\}</div></div></div>`;'''
    new_grid = """html += `<div class="fc2" data-ch="${s}" onclick="this.classList.toggle('flipped')"><div class="fi2"><div class="ff2"><div class="chip">${m.chip}</div>${esc(c.q)}</div><div class="fb2"><div class="verdict">Answer</div>${esc(c.a)}${c.img?`<img class='fc-img' src='${c.img}' alt='' loading='lazy'>`:''}${c.mnemonic?`<div class='fc-mn'><div class='fc-mn-l'>🧠 Remember it</div><div class='fc-mn-a'>${esc(c.mnemonic.analogy)}</div><div class='fc-mn-w'>${esc(c.mnemonic.why)}</div></div>`:''}</div></div></div>`;"""
    if new_grid not in new_html:
        new_html = re.sub(old_grid, lambda m: new_grid, new_html, count=1)

    # Update _deck.push
    old_push = r'_deck\.push\(\{chip:m\.chip,term:c\.q,def:c\.a,img:c\.img\|\|null\}\);'
    new_push = '_deck.push({chip:m.chip,term:c.q,def:c.a,img:c.img||null,mnemonic:c.mnemonic||null});'
    if new_push not in new_html:
        new_html = re.sub(old_push, lambda m: new_push, new_html, count=1)

    # Update dk-def renderer
    old_render = r"\$\('dk-def'\)\.textContent=c\.def;"
    new_render = """var _defHtml = (c.def||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');if(c.mnemonic){_defHtml += "<div class='fc-mn'><div class='fc-mn-l'>🧠 Remember it</div><div class='fc-mn-a'>"+(c.mnemonic.analogy||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')+"</div><div class='fc-mn-w'>"+(c.mnemonic.why||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')+"</div></div>";}$('dk-def').innerHTML=_defHtml;"""
    if "_defHtml" not in new_html:
        new_html = re.sub(old_render, lambda m: new_render, new_html, count=1)

    # Add CSS
    css_block = '''
.fc-mn{margin-top:8px;padding:8px 10px;background:#14110f;border-left:3px solid #22c55e;border-radius:4px;text-align:left;font-size:10px;line-height:1.45}
.fc-mn-l{font-size:9px;text-transform:uppercase;letter-spacing:.6px;font-weight:700;color:#22c55e;margin-bottom:4px}
.fc-mn-a{color:#86efac;font-style:italic;margin-bottom:4px;font-size:10.5px}
.fc-mn-w{color:#d0d7e3;font-size:9.5px}
#dk-b .fc-mn{font-size:12px;margin-top:10px;padding:10px 12px}
#dk-b .fc-mn-l{font-size:10px}
#dk-b .fc-mn-a{font-size:12.5px}
#dk-b .fc-mn-w{font-size:11.5px}
'''
    if '.fc-mn{' not in new_html:
        new_html = new_html.replace('</style>', css_block + '</style>', 1)

    with open(LECTURE_HTML, 'w', encoding='utf-8') as f:
        f.write(new_html)

    print(f"LECTURE: patched mnemonic on {patched}/{len(cards)} cards")
    return patched

# =========== Main =============
if __name__ == '__main__':
    print("Waiting for JSON files...")
    if not wait_for_jsons():
        print("Not all JSON files arrived. Proceeding with whatever is present.")

    mn = load_all()
    print(f"\nPatching review HTML...")
    r = patch_review(mn)
    print(f"\nPatching lecture HTML...")
    l = patch_lecture(mn)

    print(f"\n=== DONE ===")
    print(f"Review mnemonics added: {r}")
    print(f"Lecture mnemonics added: {l}")
    print(f"Total mnemonics in dict: {len(mn)}")
