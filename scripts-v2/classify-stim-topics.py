"""Classify each stim question into a study-guide topic tile based on lecture+keywords.
Outputs both a JSON manifest and a JS file the page loads at runtime.

Tile definitions follow the 3 Evolution exam study guides (Spring 2025):
- Exam 1: Evolutionary mechanisms, genetics/genomics, evol history, population genetics
- Exam 2: Complex adaptations (Ch10), sexual reproduction (Ch11), life history (Ch12), coevolution (Ch15), social behavior (Ch16)
- Exam 3: History of life (Ch3-4), phylogenetics (Ch8), species concepts (Ch13), biogeography (Ch14), conservation (Ch17), human evolution (Ch17), evolutionary medicine (Ch18)

Lecture map:
- L01 What Is Evolution / Course intro
- L02 Pre-Darwinian / Darwin / Natural selection
- L03 Genes and Heritable Variation
- L04 Hardy-Weinberg
- L05 Quantitative Genetics, Selection, Plasticity
- L07 Empirical Studies of Natural Selection
- L08 Complex Adaptations
- L09 Coevolution
- L11 Sex and Sexual Selection
- L12 Life History Evolution
- L13 Evolution of Social Behavior
- L14 History of Life
- L15 Phylogenetics and Tree of Life
- L16 Species Concepts and Reproductive Isolation
- L17 Biogeography, Speciation, Extinction
- L18 Conservation and Humans as Selective Force
- L19 Human Evolution
- L20 Evolutionary Medicine
"""
import json, os, re
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(ROOT, "public", "data", "stim-bank")
OUT_JSON = os.path.join(ROOT, "public", "data", "stim-topic-manifest.json")
OUT_JS = os.path.join(ROOT, "public", "content", "stim-topic-manifest.js")

# Order: most specific first; broadest catch-all per lecture LAST.
# Fallback uses the LAST tile that lists this lecture.
STUDY_GUIDE_TILES = [
    # ===================== EXAM 1 =====================
    # ---- L02 history of evolutionary thought (specific tiles first) ----
    {"id": "e1-figures",     "exam": 1, "group": "Evol History",  "title": "Lamarck · Lyell · Darwin · Wallace",      "lectures": ["L02"], "kw": r"Lamarck|Lyell|Darwin|Wallace|uniformitarian|acquired (trait|character)"},
    {"id": "e1-scimethod",   "exam": 1, "group": "Evol History",  "title": "Scientific method · hypothesis vs theory","lectures": ["L01","L02"], "kw": r"hypothesis|scientific theory|scientific method|tentative.*explanation|substantiated"},
    {"id": "e1-greatchain",  "exam": 1, "group": "Evol History",  "title": "Great Chain of Being · pre-Darwinian",   "lectures": ["L02"], "kw": r"Great Chain of Being|pre.?Darwinian|fixed hierarch|scala naturae"},
    {"id": "e1-extinction-hist","exam":1,"group":"Evol History",  "title": "Extinction · William Smith · fossils",   "lectures": ["L02"], "kw": r"William Smith|extinction.*establish|fossil.*stratigraph|stratigraphy"},
    # ---- L03 genetics ----
    {"id": "e1-genome",      "exam": 1, "group": "Genetics",      "title": "Genome structure · pseudogenes · mobile elements","lectures":["L03"], "kw": r"genome structure|protein.coding|noncoding DNA|pseudogene|mobile genetic element|transposon|composition of genome"},
    {"id": "e1-geneexpr",    "exam": 1, "group": "Genetics",      "title": "Gene expression regulation · methylation · miRNA","lectures":["L03"], "kw": r"DNA methylat|histone|chromatin|transcriptional regulat|post.transcriptional|microRNA|miRNA|post.translational|splicing.*regulat"},
    {"id": "e1-alleles",     "exam": 1, "group": "Genetics",      "title": "Alleles · dominant / recessive / additive","lectures":["L03","L04"], "kw": r"\bdominant\b|\brecessive\b|\badditive\b allele|allele.*type|dominance|heterozygot.*express|homozygot.*express"},
    {"id": "e1-mutation",    "exam": 1, "group": "Mechanisms",    "title": "Mutation · randomness · source of variation","lectures":["L03"], "kw": r"\bmutation|DNA change|random.*fitness|new genetic variation|mutation rate"},
    # ---- L04 Hardy-Weinberg / pop gen ----
    {"id": "e1-hw",          "exam": 1, "group": "Pop Gen",       "title": "Hardy–Weinberg equilibrium · p² + 2pq + q²","lectures":["L04"], "kw": r"Hardy.?Weinberg|allele frequency|genotype frequency|equilibrium|\bp²|\bq²|\bp.{0,3}\+.{0,3}2pq|expected genotype"},
    {"id": "e1-fst",         "exam": 1, "group": "Pop Gen",       "title": "FST · genetic differentiation",          "lectures": ["L04"], "kw": r"\bFST\b|F.statistic|genetic differentiation|population differentiation|homogeniz"},
    {"id": "e1-inbreeding",  "exam": 1, "group": "Mechanisms",    "title": "Inbreeding · homozygosity · depression", "lectures": ["L03","L04"], "kw": r"inbreeding|homozygosity|inbreeding depression|deleterious recessive|consanguin"},
    {"id": "e1-geneflow",    "exam": 1, "group": "Mechanisms",    "title": "Gene flow · migration · allele exchange","lectures": ["L03","L04"], "kw": r"gene flow|migration|allele exchange|movement of (genes|alleles)"},
    {"id": "e1-drift",       "exam": 1, "group": "Mechanisms",    "title": "Genetic drift · bottleneck · founder",   "lectures": ["L02","L03","L04"], "kw": r"genetic drift|drift|bottleneck|founder effect|small population|chance event|Tasmanian devil"},
    # ---- L05 quantitative genetics ----
    {"id": "e1-plasticity",  "exam": 1, "group": "Quant Gen",     "title": "Phenotypic plasticity · G×E · reaction norm","lectures":["L05"], "kw": r"phenotypic plasticity|reaction norm|polyphenic|VG.?E|genotype.by.environment|\bG.{1,2}E\b"},
    {"id": "e1-heritability","exam": 1, "group": "Quant Gen",     "title": "Heritability · h² · selection differential·response","lectures":["L05"], "kw": r"narrow.sense heritability|\bh²\b|\bh\^2\b|VA\b|VP\b|VG\b|VE\b|additive genetic|selection differential|response to selection|breeder.*equation|parent.offspring regression"},
    {"id": "e1-quantvar",    "exam": 1, "group": "Quant Gen",     "title": "Quantitative variance partitioning · VA / VD / VI","lectures":["L05"], "kw": r"phenotypic variance|VP\s*=\s*VA|dominance variance|epistat|interaction variance|quantitative trait"},
    # ---- L02 mechanisms (broad catch-all kept last for L02) ----
    {"id": "e1-sexsel",      "exam": 1, "group": "Mechanisms",    "title": "Sexual selection · mate choice · dimorphism","lectures":["L02","L05","L07"], "kw": r"sexual selection|mate choice|sexual dimorphism|secondary sexual"},
    {"id": "e1-homology",    "exam": 1, "group": "Mechanisms",    "title": "Homology vs analogy · common ancestry",  "lectures": ["L02","L07"], "kw": r"homolog|analog|common ancestry|divergent evolution|convergent evolution"},
    {"id": "e1-natsel",      "exam": 1, "group": "Mechanisms",    "title": "Natural selection · fitness · adaptation","lectures":["L02","L03","L05","L07"], "kw": r"natural selection|fitness|adaptation|selective pressure|differential (survival|reproduction)|heritabl"},
    {"id": "e1-applied",     "exam": 1, "group": "Pop Gen",       "title": "Applied · influenza · drug resistance · domestication","lectures":["L05","L07"], "kw": r"influenza|antibiotic resistance|drug resistance|domesticat|greyhound|peppered moth|Galápagos finch|finches"},
    {"id": "e1-selvsevol",   "exam": 1, "group": "Mechanisms",    "title": "Selection vs evolution · adaptive vs non",  "lectures": ["L01","L02","L05"], "kw": r"selection.*without.*evolution|evolution.*not.*completely random|adaptive.*nonadaptive|selection.*environmen"},

    # ===================== EXAM 2 =====================
    # ---- L07 empirical (technically before L08, kept in exam 2 per stim bank) ----
    {"id": "e2-empirical",   "exam": 2, "group": "Empirical",     "title": "Empirical case studies of selection",    "lectures": ["L07"], "kw": r"peppered moth|Galápagos|finch|Bumpus|guppy|Trinidad|Endler|stickleback|empirical|case study"},
    # ---- L08 complex adaptations / EvoDevo ----
    {"id": "e2-eye",         "exam": 2, "group": "Complex Adapt", "title": "Vertebrate eye evolution",               "lectures": ["L08"], "kw": r"vertebrate eye|eye evolution|eye spot|photoreceptor|rhodopsin|opsin|lens"},
    {"id": "e2-hox",         "exam": 2, "group": "Complex Adapt", "title": "Hox genes · body plans",                 "lectures": ["L08"], "kw": r"\bHox\b|homeobox|body plan|antennapedia"},
    {"id": "e2-evodevo",     "exam": 2, "group": "Complex Adapt", "title": "Evo-Devo · regulatory networks · heterochrony","lectures":["L08"], "kw": r"\bevo.?devo\b|evolutionary developmental|regulatory network|heterochrony|gene duplication|protein promiscui|cooption"},
    {"id": "e2-complex",     "exam": 2, "group": "Complex Adapt", "title": "Complex traits · stepwise · imperfect",  "lectures": ["L08"], "kw": r"complex (trait|adaptation)|stepwise mutation|gradual.*improve|imperfect|good enough|historical constraint"},
    # ---- L09 coevolution ----
    {"id": "e2-armsrace",    "exam": 2, "group": "Coevolution",   "title": "Arms races · predator-prey · garter/newts","lectures":["L09"], "kw": r"arms race|garter snake|newt|TTX|tetrodotoxin|predator.prey coevol"},
    {"id": "e2-mimicry",     "exam": 2, "group": "Coevolution",   "title": "Mimicry · Batesian · Mullerian",          "lectures": ["L09"], "kw": r"\bmimicry\b|Batesian|Mullerian|Müllerian|mimic|aposematic"},
    {"id": "e2-mosaic",      "exam": 2, "group": "Coevolution",   "title": "Geographic mosaic theory",               "lectures": ["L09"], "kw": r"geographic mosaic|coevolution.*geograph|mosaic theory"},
    {"id": "e2-mutual",      "exam": 2, "group": "Coevolution",   "title": "Mutualism vs antagonism · endosymbiosis","lectures":["L09"], "kw": r"mutualism|antagonism|endosymbio|mitochondri.*origin|chloroplast.*origin|symbio"},
    {"id": "e2-coev",        "exam": 2, "group": "Coevolution",   "title": "Coevolution dynamics · reciprocal adaptation","lectures":["L09"], "kw": r"coevol|reciprocal|reciprocal adaptation"},
    # ---- L11 sex / sexual selection ----
    {"id": "e2-cost-sex",    "exam": 2, "group": "Sex & Selection","title": "Cost of sex · twofold cost",            "lectures": ["L11"], "kw": r"twofold cost|cost of sex|cost of sexual|asexual.*advantage"},
    {"id": "e2-mullers",     "exam": 2, "group": "Sex & Selection","title": "Muller's ratchet · benefit of sex",     "lectures": ["L11"], "kw": r"Muller.{0,3}s ratchet|deleterious mutation accum|recombination clears"},
    {"id": "e2-redqueen",    "exam": 2, "group": "Sex & Selection","title": "Red Queen · parasite-driven sex",       "lectures": ["L11"], "kw": r"Red Queen|parasit.*sex|host.parasite coevol"},
    {"id": "e2-anisogamy",   "exam": 2, "group": "Sex & Selection","title": "Anisogamy · sperm vs egg · dimorphism", "lectures": ["L11"], "kw": r"anisogamy|isogamy|sperm.{0,3}egg|gamete size|sexual dimorphism"},
    {"id": "e2-sexconflict", "exam": 2, "group": "Sex & Selection","title": "Sexual conflict · sperm competition",   "lectures": ["L11"], "kw": r"sexual conflict|sperm competition|cryptic female choice|antagonistic coevol.*sex"},
    {"id": "e2-mate",        "exam": 2, "group": "Sex & Selection","title": "Mate choice · sexual selection",         "lectures": ["L11"], "kw": r"mate choice|female choice|male.{0,3}competition|reproductive success|sexual selection"},
    # ---- L12 life history ----
    {"id": "e2-tradeoffs",   "exam": 2, "group": "Life History",  "title": "Trade-offs · energy allocation",         "lectures": ["L12"], "kw": r"trade.off|energy allocation|growth.*reproduction|reproductive cost"},
    {"id": "e2-mortality",   "exam": 2, "group": "Life History",  "title": "Extrinsic mortality · age of maturity",  "lectures": ["L12"], "kw": r"extrinsic mortality|predation rate|age (at|of) maturity|age.*reproduction"},
    {"id": "e2-aging",       "exam": 2, "group": "Life History",  "title": "Aging · antagonistic pleiotropy",        "lectures": ["L12"], "kw": r"aging|senescen|antagonistic pleiotropy|mutation accumulation|longevity|lifespan"},
    {"id": "e2-warblers",    "exam": 2, "group": "Life History",  "title": "Seychelle's warblers · sex-biased dispersal","lectures":["L12"], "kw": r"Seychelle|warbler|sex.biased dispersal|territory quality"},
    {"id": "e2-offspring",   "exam": 2, "group": "Life History",  "title": "Offspring number / size · parental investment","lectures":["L12"], "kw": r"offspring (size|number)|parental investment|clutch size|reproductive timing"},
    # ---- L13 social behavior ----
    {"id": "e2-ess",         "exam": 2, "group": "Social Behavior","title": "ESS · side-blotched lizards · rock-paper","lectures":["L13"], "kw": r"\bESS\b|evolutionarily stable|side.blotched|rock.paper.scissors|stable strateg"},
    {"id": "e2-altruism",    "exam": 2, "group": "Social Behavior","title": "Altruism · kin selection · inclusive fitness","lectures":["L13"], "kw": r"altruism|kin selection|inclusive fitness|Hamilton.*rule|relatedness|\brB\s*>\s*C\b"},
    {"id": "e2-groupsel",    "exam": 2, "group": "Social Behavior","title": "Group vs individual selection",          "lectures": ["L13"], "kw": r"group selection|individual selection|selfish.*cooperative"},
    {"id": "e2-cooperation", "exam": 2, "group": "Social Behavior","title": "Cooperation vs selfishness · social",   "lectures": ["L13"], "kw": r"cooperation|cooperative|selfish|public good|tit.for.tat|reciprocal altruism"},

    # ===================== EXAM 3 =====================
    # ---- L14 history of life ----
    {"id": "e3-earth-age",   "exam": 3, "group": "History",       "title": "Earth's age · 4.568 Ga · debates",       "lectures": ["L14"], "kw": r"Earth.{0,3}s age|4\.5.{0,3} billion|Kelvin|age of (the )?Earth|deep time"},
    {"id": "e3-timeline",    "exam": 3, "group": "History",       "title": "Geologic timeline · Cambrian → Permian", "lectures": ["L14"], "kw": r"Ordovician|Silurian|Devonian|Cambrian|Carboniferous|Permian|Mesozoic|Cenozoic|geologic time"},
    {"id": "e3-kt",          "exam": 3, "group": "History",       "title": "K-T / K-Pg extinction · asteroid",       "lectures": ["L14"], "kw": r"\bK.?T\b|\bK.?Pg\b|K.?T boundary|asteroid impact|Chicxulub|iridium|Cretaceous"},
    {"id": "e3-dating",      "exam": 3, "group": "History",       "title": "Radiometric dating · biomarkers · half-life","lectures":["L14"], "kw": r"radiometric|radioactive decay|half.life|biomarker|isotope|carbon.14|U.Pb|Ar.Ar"},
    # ---- L15 phylogenetics ----
    {"id": "e3-trees",       "exam": 3, "group": "Phylogenetics", "title": "Phylogenetic trees · monophyletic",      "lectures": ["L15"], "kw": r"phylogen.*tree|cladogram|monophylet|paraphylet|polyphylet|root|tip"},
    {"id": "e3-synap",       "exam": 3, "group": "Phylogenetics", "title": "Synapomorphies · shared derived traits", "lectures": ["L15"], "kw": r"synapomorph|symplesiomorph|derived (trait|character)|shared.*derived|character state|outgroup"},
    {"id": "e3-species",     "exam": 3, "group": "Phylogenetics", "title": "Species concepts · biological / morpho / phylo","lectures":["L15","L16"], "kw": r"species concept|biological species|morphospecies|phylogenetic species|ring species|cryptic species"},
    # ---- L16 reproductive isolation ----
    {"id": "e3-isolation",   "exam": 3, "group": "Speciation",    "title": "Reproductive isolation · prezygotic / postzygotic","lectures":["L16"], "kw": r"reproductive isolation|prezygotic|postzygotic|temporal isolation|behavioral isolation|mechanical isolation|hybrid (inviab|steril)|gametic isolation"},
    {"id": "e3-speciation",  "exam": 3, "group": "Speciation",    "title": "Speciation · allopatric / sympatric / polyploid","lectures":["L16","L17"], "kw": r"\bspeciation\b|allopatric|sympatric|peripatric|parapatric|polyploid|hybrid speciation"},
    # ---- L17 biogeography ----
    {"id": "e3-biogeo",      "exam": 3, "group": "Biogeography",  "title": "Dispersal vs vicariance",                 "lectures": ["L17"], "kw": r"biogeograph|dispersal|vicariance|vicariant|continental drift|land bridge"},
    {"id": "e3-diversity",   "exam": 3, "group": "Biogeography",  "title": "Standing diversity · turnover · speciation rate","lectures":["L17"], "kw": r"standing diversity|turnover rate|species richness|origination rate|extinction rate|equilibrium diversity"},
    {"id": "e3-massext",     "exam": 3, "group": "Biogeography",  "title": "Mass extinctions · Big Five",            "lectures": ["L14","L17"], "kw": r"mass extinction|Big Five|Permian.Triassic|Cretaceous.Paleogene|Ordovician.Silurian|background extinction"},
    # ---- L18 conservation ----
    {"id": "e3-human-impact","exam": 3, "group": "Conservation",  "title": "Humans as a selective force",            "lectures": ["L18"], "kw": r"human.*selective force|selective breeding|domesticat|harvest.induced|fishing.*induced|hunting.*induced|trophy hunt"},
    {"id": "e3-conservation","exam": 3, "group": "Conservation",  "title": "Conservation strategies · biodiversity", "lectures": ["L18"], "kw": r"conservation|biodiversity|endangered|extinction risk|protected area|habitat destruction|fragmentation"},
    # ---- L19 human evolution ----
    {"id": "e3-bipedal",     "exam": 3, "group": "Human Evol",    "title": "Bipedalism · 6-7 Ma · Sahelanthropus",   "lectures": ["L19"], "kw": r"bipedal|Sahelanthropus|tchadensis|Chad|foramen magnum|Lucy|Australopithecus"},
    {"id": "e3-hominins",    "exam": 3, "group": "Human Evol",    "title": "Hominin lineage · Homo · Neanderthal",   "lectures": ["L19"], "kw": r"hominin|hominid|Homo (erectus|sapiens|neanderthal|habilis|floresiensis)|Neandertal|Denisovan|out.of.Africa"},
    # ---- L20 evolutionary medicine ----
    {"id": "e3-antibiotic",  "exam": 3, "group": "Evol Medicine", "title": "Antibiotic resistance",                  "lectures": ["L20"], "kw": r"antibiotic resistance|MRSA|tuberculosis|drug.resistant|resistance gene|broad.spectrum"},
    {"id": "e3-virulence",   "exam": 3, "group": "Evol Medicine", "title": "Virulence · pathogen evolution",         "lectures": ["L20"], "kw": r"virulence|pathogen.*evolv|trade.off.*virulence|transmission rate|host.pathogen"},
    {"id": "e3-evomed",      "exam": 3, "group": "Evol Medicine", "title": "Co-evolution · disease · mismatch",      "lectures": ["L20"], "kw": r"co.?evolution|evolutionary medicine|mismatch.*disease|Darwinian medicine|pathogen co.?evol"},
]

def load_all_questions():
    questions = []
    for fn in sorted(os.listdir(SRC_DIR)):
        if not fn.startswith("L") or not fn.endswith(".json"):
            continue
        with open(os.path.join(SRC_DIR, fn), "r", encoding="utf-8") as f:
            d = json.load(f)
        if isinstance(d, dict) and isinstance(d.get("questions"), list):
            questions.extend(d["questions"])
        elif isinstance(d, list):
            questions.extend(d)
    return questions

def classify(q, tiles):
    """Pass 1: keyword match in topic+q+source. Pass 2: fall back to LAST tile that lists this lecture."""
    text = (q.get("topic","") + " | " + q.get("q","") + " | " + q.get("source",""))
    lec = q.get("lecture", "")
    ex = q.get("exam", 0)
    for tile in tiles:
        if tile["exam"] != ex: continue
        if lec not in tile.get("lectures", []): continue
        kw = tile.get("kw")
        if not kw:
            return tile["id"]
        if re.search(kw, text, re.IGNORECASE):
            return tile["id"]
    fallback = None
    for tile in tiles:
        if tile["exam"] != ex: continue
        if lec in tile.get("lectures", []):
            fallback = tile["id"]
    return fallback

def main():
    qs = load_all_questions()
    tile_to_qids = defaultdict(list)
    qid_to_tile = {}
    unassigned = []
    for q in qs:
        tid = classify(q, STUDY_GUIDE_TILES)
        if tid:
            tile_to_qids[tid].append(q["id"])
            qid_to_tile[q["id"]] = tid
        else:
            unassigned.append({
                "qid": q["id"],
                "exam": q.get("exam"),
                "lecture": q.get("lecture"),
                "section": q.get("section"),
                "topic": q.get("topic"),
                "stem": q.get("q","")[:120]
            })

    manifest = {
        "tiles": [
            {**{k: v for k, v in t.items() if k != "kw"},
             "qids": tile_to_qids.get(t["id"], []),
             "count": len(tile_to_qids.get(t["id"], []))}
            for t in STUDY_GUIDE_TILES
        ],
        "qid_to_tile": qid_to_tile,
        "unassigned_count": len(unassigned),
        "unassigned": unassigned,
    }

    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    with open(OUT_JS, "w", encoding="utf-8") as f:
        f.write("/* Auto-generated by scripts-v2/classify-stim-topics.py — do not edit by hand. */\n")
        f.write("window.STIM_TOPIC_MANIFEST = ")
        json.dump(manifest, f, ensure_ascii=False)
        f.write(";\nconsole.log('[stim-topic-manifest loaded]', window.STIM_TOPIC_MANIFEST.tiles.length, 'tiles,', Object.keys(window.STIM_TOPIC_MANIFEST.qid_to_tile).length, 'qids assigned');\n")

    print(f"Wrote {OUT_JSON}")
    print(f"Wrote {OUT_JS}")
    print(f"Total questions: {len(qs)}")
    print(f"Assigned: {len(qid_to_tile)} / {len(qs)}")
    print(f"Unassigned: {len(unassigned)}")
    print()
    print("Per-tile counts:")
    for t in STUDY_GUIDE_TILES:
        n = len(tile_to_qids.get(t["id"], []))
        bar = "█" * min(n, 30)
        print(f"  [E{t['exam']}] {t['id']:22s} {n:3d}  {bar}  — {t['title']}")
    if unassigned:
        print()
        print("UNASSIGNED:")
        for u in unassigned:
            print(f"  {u['qid']} [E{u['exam']} {u['lecture']}§{u['section']}] {u['topic']!r}: {u['stem']}")

if __name__ == "__main__":
    main()
