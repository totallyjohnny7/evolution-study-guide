#!/usr/bin/env python3
"""Fix all coverage gaps by enriching study guide popup sections."""
import json, copy

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

nodes = data['nodes']
node_map = {n['id']: n for n in nodes}

def add_section(node_id, label, body):
    """Add a new popup section to a node."""
    n = node_map[node_id]
    if 'popup' not in n:
        n['popup'] = {'heading': n['title'], 'sections': []}
    n['popup']['sections'].append({'label': label, 'body': body})

def append_to_section(node_id, section_label, extra_text):
    """Append text to an existing popup section body."""
    n = node_map[node_id]
    if not n.get('popup'):
        return add_section(node_id, section_label, extra_text)
    for s in n['popup']['sections']:
        if s.get('label','').upper() == section_label.upper():
            s['body'] = s['body'].rstrip() + '\n\n' + extra_text
            return
    add_section(node_id, section_label, extra_text)

def add_example(node_id, example_text):
    """Add an example to a node's popup."""
    n = node_map[node_id]
    if 'popup' not in n:
        n['popup'] = {'heading': n['title'], 'sections': [], 'examples': []}
    if 'examples' not in n['popup']:
        n['popup']['examples'] = []
    n['popup']['examples'].append(example_text)

def add_warning(node_id, warning_text):
    """Add a warning to a node's popup."""
    n = node_map[node_id]
    if 'popup' not in n:
        n['popup'] = {'heading': n['title'], 'sections': [], 'warnings': []}
    if 'warnings' not in n['popup']:
        n['popup']['warnings'] = []
    n['popup']['warnings'].append(warning_text)

# ═══════════════════════════════════════════════════════════
# FIX EACH GAP BY NODE
# ═══════════════════════════════════════════════════════════

# --- Lec2: Descent with Modification & Common Ancestry ---
append_to_section('lec2-descent-modification', 'KEY POINTS',
    'COMMON MISCONCEPTIONS: The "March of Progress" iconography (ape → hominid → modern human in a linear sequence) seriously misrepresents evolution. It portrays evolution as a linear, directional progression toward a "higher" endpoint. In reality, evolution is a branching tree: lineages split, some go extinct, and there is no predetermined "goal." This misleading iconography reinforces the false idea that evolution is a ladder of progress rather than a bush of divergence.')

# --- Lec5: Qualitative vs Quantitative Traits ---
append_to_section('lec56-quant-intro', 'VARIANCE PARTITIONING',
    'HERITABILITY MISCONCEPTIONS: When an agricultural scientist reports "heritability for yield is h² = 0.85," this does NOT mean 85% of a plant\'s yield is genetically determined. Heritability is the proportion of phenotypic VARIANCE in a population attributable to genetic variance. A farmer who concludes "genetics controls 85% of my crop\'s yield" confuses variance-in-a-population with the phenotype of an individual. A single plant\'s yield always depends on BOTH genes AND environment — heritability only tells you how much of the VARIATION among plants is genetic.')

# --- Lec6: Fitness Landscapes ---
append_to_section('lec7-fitness-landscape', 'KEY POINTS',
    'HIGH-DIMENSIONAL LANDSCAPES & NEUTRAL THEORY: Real fitness landscapes are >10,000-dimensional (one axis per segregating locus). In high-dimensional space, most local peaks visible in 2D projections are actually connected through ridges or neutral networks — paths of equal fitness that allow populations to traverse landscapes without crossing deep valleys. Neutral theory (Kimura, 1968) proposes that most molecular evolution occurs through neutral mutations fixed by genetic drift rather than natural selection. In high-dimensional fitness landscapes, neutral networks connect genotypes of equal fitness, enabling populations to explore sequence space through drift alone, potentially reaching new adaptive peaks without requiring selection to cross fitness valleys.')

# --- Lec7: Adaptations: Trait vs Process ---
append_to_section('lec8-adaptations-intro', 'VESTIGIAL ORGANS',
    'CASE STUDY — CAVE FISH: Cave-dwelling fish (e.g., Astyanax mexicanus) illustrate multiple adaptation categories simultaneously. Reduced eyes = vestigial (ancestral functional structure now diminished because selection maintaining eyes was relaxed in total darkness). Elongated tactile barbels = adaptation (enhanced touch sensitivity currently maintained by selection for navigating dark environments). Pale/depigmented skin may be vestigial (loss of protective melanin no longer needed without UV) or a byproduct of developmental changes in neural crest cells.')

# --- Lec7: Evo-Devo & Regulatory Networks ---
append_to_section('lec8-evo-devo', 'KEY EXPERIMENT',
    'HOX GENE INTERCHANGEABILITY: If the same Hox gene "toolkit" is conserved across all animals, toolkit genes should be substantially interchangeable between species. The famous Halder, Callaerts & Gehring (1995) experiment demonstrated this: the mouse Pax6 gene, when expressed in Drosophila, induced ectopic eye formation — a mouse gene triggering eye specification in a fly. This confirms that the master regulatory gene is functionally conserved despite >500 million years of divergence. The downstream targets differ (compound eye vs. camera eye), but the upstream switch is interchangeable.')

# --- Lec7: Eye Evolution ---
append_to_section('lec8-eye-evolution', 'MECHANISM',
    'OPSIN GENE DUPLICATIONS: Opsin genes underwent two rounds of duplication early in animal evolution, producing different light-sensitivity proteins (spectral sensitivities). A single opsin can only detect one wavelength peak of light — to distinguish colors (color vision), an organism needs multiple opsins with different spectral sensitivities (e.g., short-wave/blue, medium-wave/green, long-wave/red in humans). Each duplication + divergence event allowed detection of a new wavelength band. Molluscan eyes (e.g., octopus) evolved independently from vertebrate eyes but share the same Pax6 master regulatory gene — a striking case of deep homology at the genetic level combined with convergent evolution at the structural level.')

add_warning('lec8-eye-evolution',
    'REBUTTING "IRREDUCIBLE COMPLEXITY": The creationist argument that the eye could not evolve because "removing any component renders it nonfunctional" fails on multiple fronts: (a) simpler light-sensing structures DO function (flatworm eyespots detect light direction), (b) each intermediate stage provides a selective advantage (light detection → directional sensing → crude imaging → sharp focus), (c) modern organisms display every intermediate grade (planarian eyespot → nautilus pinhole → squid camera eye), (d) Pax6 is shared across phyla, integrating molecular evidence of common ancestry, (e) computer models (Nilsson & Pelger 1994) show a camera eye can evolve from a flat photoreceptor patch in <400,000 generations.')

# --- Lec7: Imperfect Adaptations ---
append_to_section('lec8-flaws-pleiotropy', 'KEY EXAMPLES',
    'CROSSED AIRWAY-ESOPHAGUS: Humans share a crossed airway and esophagus pathway — a holdover from aquatic ancestors in which the gill arch anatomy positioned the esophagus (digestive tract) behind the trachea (respiratory tract). Natural selection cannot "redesign" the layout from scratch because each modification must maintain function at every intermediate step. The result: food can accidentally enter the trachea, causing choking — an imperfect but historically constrained arrangement.')

# --- Lec8: Coevolution ---
append_to_section('lec9-coevolution-intro', 'KEY EXAMPLES',
    'DIFFUSE COEVOLUTION — OAK & WEEVILS: When oak trees evolved thicker acorn shells over ~50,000 years while acorn weevils (Curculio) evolved longer ovipositors (egg-laying structures), a biologist might ask: is this pairwise or diffuse coevolution? Diffuse coevolution occurs when selection comes from many species simultaneously — oaks face pressure from weevils, squirrels, jays, and fungi, so their shell thickness reflects the net selective environment, not just one antagonist.\n\nHUMAN-DOG COEVOLUTION: Humans domesticated dogs over 15,000 years. This IS coevolution — both species reciprocally adapted to each other: dogs evolved reduced aggression, floppy ears, and starch digestion genes (AMY2B duplications that accommodated human agricultural practices), while humans adjusted social practices and even immune responses to living with canines.')

# --- Lec8: Mutualistic Coevolution ---
append_to_section('lec9-mutualistic', 'KEY EXAMPLES',
    'DARWIN\'S ORCHID-MOTH PREDICTION & FALSIFIABILITY: Darwin\'s prediction about the Angraecum sesquipedale orchid (with its 30cm nectar spur) and the later-discovered Xanthopan morganii moth satisfies Popperian falsifiability — the gold standard of scientific predictions. (1) It was specific — a moth with a proboscis matching the spur length MUST exist. (2) It was deductive — derived from the mechanism of natural selection. (3) It was risky — if no such moth existed, the theory would face a genuine challenge. (4) Independent confirmation came decades later. This is not mere post-hoc confirmation but a genuinely predictive, testable application of evolutionary theory.')

# --- Lec8: Endosymbiosis ---
append_to_section('lec9-endosymbiosis', 'KEY EXPERIMENT',
    'TESTING ENDOSYMBIOSIS vs. AUTOGENOUS ORIGIN: To distinguish between the Margulis endosymbiosis hypothesis and an alternative autogenous (self-origin) hypothesis for mitochondria: (1) Molecular test: Sequence mitochondrial DNA and compare to free-living alpha-proteobacteria vs. nuclear DNA. Endosymbiosis predicts mitochondrial ribosomal RNA sequences cluster with bacteria, not with the host\'s nuclear genes — this congruence has been confirmed. (2) Structural test: Mitochondria have double membranes (outer = host-derived engulfment membrane; inner = original bacterial membrane), bacterial-size 70S ribosomes (not 80S eukaryotic ribosomes), and circular DNA — all consistent with a captured bacterium, not an internally evolved compartment.')

# --- Lec9: Male Strategies & Female Choice ---
append_to_section('lec1011-male-female-strategies', 'KEY EXAMPLES',
    'REDBACK SPIDER SEXUAL CANNIBALISM: Male redback spiders (Latrodectus hasselti) somersault their abdomen into the female\'s fangs during mating. Being consumed prolongs copulation time, allowing the male to transfer more sperm and increasing paternity. The male sacrifices his life but gains fitness through greater sperm transfer — a case where the cost of male investment (death) is outweighed by the reproductive benefit (more offspring sired). This also discourages the female from mating again quickly.\n\nLEKKING SPECIES: Classic lekking species include sage grouse (Centrocercus urophasianus) and golden-collared manakin (Manacus vitellinus). Males form display aggregations (leks) where females visit, compare, and choose mates. Typically only 1-5% of males at a lek achieve most matings — extreme variance in male reproductive success.')

# --- Lec10: Life History Strategies ---
append_to_section('lec12-life-history-intro', 'WORKED EXAMPLE',
    'PACIFIC SALMON — INTEGRATING TRADE-OFFS: Pacific salmon illustrate how the finite-energy constraint, r/K continuum, and semelparity interact. Salmon face extremely high adult mortality from the arduous upstream migration (predators, rapids, exhaustion). With survival probability near zero after spawning, natural selection favors pouring ALL remaining energy into a single massive reproductive event (semelparity) — optimizing egg number and quality rather than holding reserves for future reproduction. This is an extreme K-selected semelparous strategy: few, large, well-provisioned offspring, one lethal reproductive bout.')

# --- Lec10: Extrinsic Mortality, Aging, & Senescence ---
append_to_section('lec12-aging', 'CORE CONCEPT',
    'MEDAWAR vs. WILLIAMS — COMPLEMENTARY THEORIES: Medawar (mutation accumulation) explains why deleterious late-acting mutations accumulate unpurged — selection is too weak to remove mutations whose effects appear after most reproduction is done (the "selection shadow"). These mutations are sheltered from purging by timing alone. Williams (antagonistic pleiotropy) explains why some genes ACTIVELY cause aging — alleles that boost early reproduction but damage late survival are favored because early fitness benefits outweigh late costs. Together: Medawar explains passive accumulation of damage; Williams explains active trade-offs. Both are complementary, not competing — aging is an emergent property of both processes.')

# --- Lec11: Levels of Selection ---
append_to_section('lec13-group-individual', 'KEY EXAMPLES',
    'LEMMING MYTH DEBUNKED: The myth that lemmings deliberately commit mass suicide was popularized by a 1958 Disney documentary ("White Wilderness") that staged lemming mass drownings for dramatic footage — crews literally threw lemmings off cliffs. In reality, lemming population crashes are driven by food shortages, predation, and accidental drowning during migrations across bodies of water. The myth misrepresents lemmings as self-sacrificing for group benefit — a textbook example of naive group selectionism. Individual selection cannot favor "suicide for the good of the species" because sacrificers would be eliminated while refusers reproduce, quickly purging any suicide allele from the population. This is directly addressed by Williams (1966) in his critique of group selection.')

# --- Lec12: Age of the Earth ---
append_to_section('lec14-age-earth', 'KEY POINTS',
    'CROSS-VALIDATION WITH MULTIPLE ISOTOPE SYSTEMS: Radiometric dating uses multiple isotope systems (U-Pb, K-Ar, Rb-Sr) on the same rock. Different isotope systems have different half-lives and chemical behaviors — if all converge on the same age, this eliminates the possibility of systematic contamination or error in any single system. This cross-validation approach is fundamental to the 4.54 Ga age of Earth.\n\nUSSHER vs. KELVIN: Ussher (1664) used textual authority — biblical genealogies in scripture — to calculate Earth\'s age as ~6,000 years. Kelvin (1897) used physical modeling (heat conduction) to estimate ~20-40 million years. Both were wrong, but for different reasons: Ussher relied on non-empirical sources; Kelvin didn\'t know about radioactive decay as a heat source. Modern radiometric dating gives 4.54 billion years.')

# --- Lec12: Origin of Life ---
append_to_section('lec14-origin-life', 'MECHANISM',
    'MILLER-UREY EXPERIMENT DETAILS: In the Miller-Urey apparatus, water was boiled to simulate ocean evaporation. Vapor was circulated through a chamber of reduced gases (CH₄, NH₃, H₂, H₂O) and exposed to electrical sparks (simulating lightning). Products condensed and collected in a trap. The key amino acids produced were glycine, alanine, and valine — all standard proteinogenic amino acids found in modern proteins.\n\nFROM MONOMERS TO POLYMERS: Miller-Urey showed amino acid monomers form abiotically. But can they polymerize? Sydney Fox (1977) heated dry amino acids and added water, producing short peptide chains (proteinoids). Claudia Huber (2006) showed metal-sulfide surfaces catalyze peptide bond formation — addressing the key objection that monomers cannot spontaneously polymerize in dilute solution.\n\nRNA WORLD MOLECULAR FOSSILS: The ribosome — the molecular machine that translates mRNA into protein — has its catalytic activity in its RNA component (peptidyl transferase is a ribozyme), not its protein components. The ribosomal RNA performs the chemistry of peptide bond formation. This is a molecular "fossil" of an RNA-dominated past, supporting the RNA World hypothesis.')

# --- Lec12: Early Life ---
append_to_section('lec14-early-life', 'CORE CONCEPT',
    'LUCA (LAST UNIVERSAL COMMON ANCESTOR): LUCA is dated to ~3.5–3.8 billion years ago. All modern life — bacteria, archaea, and eukaryotes — shares a core set of molecular machinery: DNA as heredity material, RNA as intermediary, ribosomes for translation, ATP as energy currency, and the same genetic code. This shared molecular machinery is evidence of universal common ancestry — LUCA possessed all these features.\n\nARCHAEA vs. BACTERIA: Both are single-celled prokaryotes with no nucleus, yet classified as two separate domains because of fundamental molecular differences: Archaea use ether-linked isoprenoid lipids in their membranes (bacteria use ester-linked fatty acids), different ribosomal RNA sequences, different RNA polymerase machinery, and different cell wall composition (no peptidoglycan in most archaea). These differences are deep enough that archaea are actually more closely related to eukaryotes than to bacteria.')

# --- Lec12: Cambrian Explosion ---
append_to_section('lec14-cambrian-paleozoic', 'KEY EXAMPLES',
    'BURGESS SHALE PRESERVATION: The Burgess Shale (~505 Mya, Canadian Rockies) preserves soft tissues almost never fossilized because anoxic underwater mudslides rapidly buried organisms and excluded oxygen and decomposers/scavengers — preventing rotting and decay. The fine-grained sediment captured exquisite detail of soft-bodied organisms like Anomalocaris, Hallucigenia, and Opabinia.\n\nCARBONIFEROUS PERIOD (359–299 Mya): Famous for massive coal deposits, giant insects (dragonflies with 70cm wingspan), and the "age of amphibians." Lush tropical swamp forests dominated by giant lycopsid trees grew in waterlogged, low-oxygen environments. When trees fell into anoxic swamps, they didn\'t decompose fully — they compressed into coal over millions of years. High atmospheric O₂ (~35%) enabled giant insects (which breathe through passive diffusion, so larger bodies need more O₂).\n\nEND-PERMIAN EXTINCTION (252 Mya, ~96% marine species lost): Hypothesized cause: Siberian Traps volcanism. Massive CO₂ release drove rapid global warming (greenhouse effect). Sulfur aerosols caused acid rain. Ocean acidification dissolved carbonate shells. Anoxic ocean zones expanded. The result was a cascading series of environmental catastrophes — not a single kill mechanism.')

# --- Lec12: Mesozoic, K-T Extinction ---
append_to_section('lec14-mesozoic-cenozoic', 'KEY POINTS',
    'MAMMALS IN THE MESOZOIC: First mammals arose ~200–180 Mya in the Jurassic and remained small and nocturnal for ~150 million years. Large and diurnal (daylight-active) niches were already occupied by dinosaurs, which dominated competition. Small mammals survived by burrowing, being nocturnal, and eating insects — niches where dinosaurs didn\'t compete effectively.\n\nK-T EXTINCTION MECHANISM: The K-T asteroid (~10 miles / 16 km diameter) struck carbonate and sulfate rock at Chicxulub, Mexico. The impact ejected debris that blocked sunlight for months to years, collapsing photosynthesis-based food chains. Carbonate rock released CO₂ (long-term warming); sulfate rock released sulfur aerosols (short-term cooling). Survivors were species that could subsist on detritus, carrion, seeds, or stored energy — not those dependent on active primary productivity.\n\nK-T vs. K-Pg NAMING: The "K" stands for German "Kreide" (chalk). "Pg" stands for Paleogene, the first period of the Cenozoic era. The renaming from "K-T" (Cretaceous-Tertiary) to "K-Pg" (Cretaceous-Paleogene) reflects modern stratigraphic subdivisions — "Tertiary" was abandoned as a formal term because it lumped together the Paleogene and Neogene periods.\n\nHUMANS IN DEEP TIME: The entire Homo sapiens history (~195,000 years) represents an extraordinarily thin sliver of geological time — compresses to the last 0.004% of Earth\'s 4.54 billion year history. This emphasizes how recent and geologically instantaneous human evolution is.')

# --- Lec13: Tree Thinking ---
append_to_section('lec15-tree-thinking', 'KEY POINTS',
    'NESTED CLADES: Clades are nested inside one another like Russian dolls — a single organism belongs to multiple clades of increasing inclusiveness simultaneously. For example, a human is simultaneously a member of Eukaryota, Animalia, Vertebrata, Mammalia, Primates, and Hominidae. Each clade is defined by shared derived characters (synapomorphies) at different levels of the hierarchy.')

# --- Lec13: Cladistics ---
append_to_section('lec15-cladistics-synapomorphy', 'KEY POINTS',
    'COMBINATORIAL EXPLOSION IN PHYLOGENETICS: With 5 taxa there are 105 possible tree topologies; with 9 taxa there are ~2 million. The number of possible trees grows faster than exponentially with each added taxon (double factorial growth). This makes manually evaluating all possible trees impossible for datasets with more than ~20 taxa. Modern phylogeneticists use heuristics — algorithmic shortcuts that search tree space efficiently without exhaustively evaluating every possibility (e.g., branch swapping, genetic algorithms, MCMC sampling).')

# --- Lec13: Parsimony, Homoplasy & Convergence ---
append_to_section('lec15-homoplasy-convergence', 'KEY EXAMPLES',
    'WHALE PHYLOGENY & CONVERGENT MORPHOLOGY: Whales and dolphins (cetaceans) are most closely related to hippopotamuses — confirmed by both molecular data and transitional fossils (Pakicetus, Ambulocetus). Yet cetaceans are fully aquatic with flipper-like forelimbs and no hindlimbs, while hippos are semi-aquatic with four legs. Surface morphology alone would have misled morphologists into grouping cetaceans with fish or other fully aquatic vertebrates. This is why molecular phylogenetics revolutionized systematics — DNA reveals shared ancestry that convergent morphological evolution can obscure.')

# --- Lec13: Feathers & Exaptation ---
append_to_section('lec15-feathers-exaptation', 'KEY EXAMPLES',
    'OVIRAPTOR BROODING: Oviraptor (a non-flying theropod dinosaur) was found in 1993 in a brooding posture on a nest of eggs. Brooding behavior — sitting on a nest to regulate egg temperature — requires a body covering with insulating properties. This confirms feathers functioned for thermoregulation BEFORE flight evolved, and were later co-opted (exapted) as airfoils for aerial locomotion. The feathers were retained and refined for their new function.\n\nEXAPTATION vs. PRE-ADAPTATION: The term exaptation was coined by Stephen Jay Gould and Elisabeth Vrba in 1982 to replace "pre-adaptation." The prefix "pre-" in pre-adaptation implies that a trait was somehow anticipating or prepared for its future function — a teleological error. "Exaptation" avoids this: it simply describes a trait currently useful for a function it did not originally evolve for. Under continued selection for the new function, an exaptation can become optimized for that function through subsequent refinement — feathers started as insulation, were exapted for flight, then underwent further adaptive refinement as airfoils.')

# --- Lec14: Species Concepts ---
append_to_section('ch13-species-concepts', 'KEY POINTS',
    'MULE STERILITY & BSC: Mules (horse × donkey hybrids) are viable but sterile. The BSC classifies horses and donkeys as separate species because hybrid sterility prevents gene flow — no alleles are exchanged between the two gene pools. The boundary is clear-cut here, but many real cases are unsatisfying: some "species" hybridize and produce fertile offspring, blurring the BSC boundary (e.g., wolves and coyotes, polar bears and grizzlies).\n\nGENERAL LINEAGE SPECIES CONCEPT: The GLSC (Kevin de Queiroz) uses "metapopulation" to describe spatially separated populations with varying connectivity. This acknowledges that real populations are rarely uniform — they consist of subpopulations connected by different amounts of gene flow. The GLSC accommodates messy real-world situations better than the BSC.\n\nBSC IS NOT "CORRECT" BY AUTHORITY: Ernst Mayr published the BSC in 1942 as part of the Modern Synthesis. But scientific concepts are judged by their empirical utility and coverage, not by authority or historical priority. The BSC has genuine limitations (doesn\'t apply to asexual organisms, fossils, or ring species) — this is not a violation of the concept, but a limitation of its scope.')

# --- Lec14: BDM Incompatibilities ---
append_to_section('ch13-bdm-cryptic', 'KEY POINTS',
    'BACTERIAL "SPECIES" PROBLEM: 10,000+ bacterial "species" can be found in a single teaspoon of soil, and most cannot be grown in pure culture (unculturable). Most bacterial diversity is measured only through environmental DNA and 16S ribosomal RNA sequencing. Horizontal gene transfer means bacteria are constantly exchanging genes across lineage boundaries, making the species concept even murkier. The vast majority of microbial diversity remains unmeasured and uncharacterized.')

# --- Lec14: Biogeography ---
append_to_section('biogeography-extinction', 'KEY EXAMPLES',
    'GREAT AMERICAN BIOTIC INTERCHANGE (~3 Mya): When the Isthmus of Panama formed, South American marsupials largely lost in competition to North American placental mammals. Why? North America had been connected via Beringia to Eurasia for most of the Cenozoic, allowing its faunas to experience more intense interspecific competition and predation — effectively "battle-hardening" the placental mammals. South American marsupials had evolved in relative isolation and were competitively naive against these more experienced faunas.')

# --- Lec15: Human Evolution ---
append_to_section('human-evolution', 'KEY POINTS',
    'DENISOVANS: Identified in 2010 from a single finger bone in Denisova Cave (Siberia). Genetically distinct from both Neanderthals and modern Homo sapiens. Denisovans interbred with anatomically modern humans — modern Melanesians, Papuans, and other Oceania populations carry 3-6% Denisovan DNA, suggesting interbreeding occurred in Southeast Asia.\n\nHOMININ PHYLOGENY: The transition from early hominins (Ardipithecus ~4.4 Mya, Australopithecus/Lucy ~3.2 Mya) to modern Homo sapiens was NOT a linear ladder. Multiple hominin species overlapped in time and geography — they were contemporaneous, not sequential. Homo erectus, Homo neanderthalensis, Homo floresiensis, and Denisovans all coexisted with early Homo sapiens at various points. Ancestry lines are often unclear because the fossil record is fragmentary.')

# --- Lec15: Evolutionary Medicine ---
append_to_section('evolutionary-medicine', 'KEY EXAMPLES',
    'HYGIENE HYPOTHESIS: Rising rates of allergies and autoimmune disease in industrialized countries may result from reduced parasite exposure. The human immune system evolved in environments rich with parasites (especially helminths/worms). Without these stimuli, the immune system becomes dysregulated — attacking inappropriate targets (self-tissue in autoimmune disease, harmless allergens in allergies). This is an evolutionary mismatch: our immune system is calibrated for an ancestral parasite-rich environment, not modern hyper-clean conditions.\n\nOBSTETRICAL DILEMMA: Human birth involves an unusually tight fit between the baby\'s head and the mother\'s pelvis. Bipedalism selected for narrow pelvises (efficient walking requires a narrow pelvic canal), while encephalization (brain enlargement) selected for larger infant heads. The compromise: human babies are born relatively underdeveloped (altricial) compared to other primates — the head must pass through before it gets too large, making the tight fit feasible but risky.\n\nFOUR FRAMEWORKS OF EVOLUTIONARY MEDICINE: (1) Trade-offs — antagonistic pleiotropy, life history trade-offs. (2) Mismatch — human metabolic physiology evolved under ancestral conditions of food scarcity and high activity; modern abundance of calories and sedentary lifestyles lead to obesity, diabetes (thrifty genotype: insulin resistance was adaptive when food was scarce, maladaptive now). (3) Arms races — host-pathogen coevolution, antibiotic resistance. (4) Phylogenetic constraints — imperfect design due to evolutionary history (crossed airway, blind spot).')

# ═══════════════════════════════════════════════════════════
# SAVE UPDATED DATA
# ═══════════════════════════════════════════════════════════
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)

print("All gaps fixed. data.json updated.")
print(f"Nodes modified: enriched content across 20+ nodes")
