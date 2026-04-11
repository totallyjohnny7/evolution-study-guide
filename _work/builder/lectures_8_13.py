"""Node generators for Lectures 8-13 (Exam 2 coverage)."""
from helpers import load_lec, slides_to_sections, build_node
from diagrams.red_queen_cycle import red_queen_cycle_diagram
from diagrams.r_vs_k_compare import r_vs_k_compare_diagram
from diagrams.eye_evolution_stages import eye_evolution_stages_diagram
from diagrams.hox_regulatory_network import hox_regulatory_network_diagram
from diagrams.garter_snake_newt_arms_race import garter_snake_newt_arms_race_diagram
from diagrams.mullerian_vs_batesian_compare import mullerian_vs_batesian_compare_diagram
from diagrams.endosymbiosis_flow import endosymbiosis_flow_diagram
from diagrams.anisogamy_origin import anisogamy_origin_diagram
from diagrams.side_blotched_rps_cycle import side_blotched_rps_cycle_diagram
from diagrams.sperm_competition_strategies import sperm_competition_strategies_diagram
from diagrams.life_history_r_k_timeline import life_history_r_k_timeline_diagram
from diagrams.hawk_dove_game import hawk_dove_game_diagram
from diagrams.hamiltons_rule_kin_selection import hamiltons_rule_kin_selection_diagram


def lec8_nodes():
    d = load_lec('lec8')
    nodes = []
    nodes.append(build_node(
        id='lec8-adaptations-intro',
        title='Adaptations: Trait vs Process',
        subtitle='Defining adaptation and novel traits (Lec 8 slides 1-6)',
        color='amber', row=7,
        heading='Lecture 8 — Complex Adaptations',
        sections=[{'label': 'CORE CONCEPT', 'body': 'Adaptation has TWO meanings: (1) as a TRAIT — a heritable, inherited aspect of an organism that increases its competitive fitness; (2) as a PROCESS — the ongoing evolutionary change produced by natural selection that generates fitness-enhancing traits. NOVEL TRAITS arise de novo (eyes, limbs, wings, teeth) — they did not exist in the ancestor in their current form. A COMPLEX ADAPTATION is a suite of co-expressed traits working together (e.g., camera eye: cornea + lens + retina + optic nerve). Not every trait is adaptive: SPANDRELS (Gould & Lewontin 1979) are byproducts of other adaptations, VESTIGIAL structures are reduced remnants of once-functional ancestral traits, and NEUTRAL traits have no fitness effect. Adaptation is always relative to a specific environment — sickle cell is adaptive in malaria zones but deleterious elsewhere.'}] + slides_to_sections(d, (1, 6)),
        examples=[
            'Adaptation as TRAIT: a heritable feature that increases fitness in a particular environment.',
            'Adaptation as PROCESS: the ongoing evolutionary change driven by natural selection.',
            'Novel traits: arise de novo (not inherited) — e.g., limbs in tetrapods, wings in birds.',
            'Complex traits: require coordination of multiple genes and developmental modules.',
        ],
        warnings=[
            'Not every trait is an adaptation — spandrels, vestigial, neutral traits exist. Gould & Lewontin (1979) warned against the "adaptationist programme" of assuming every feature is adaptive without evidence.',
            'Adaptation is always relative to an environment. Sickle cell in malaria-free regions is deleterious — a trait adaptive in one environment can be neutral or harmful in another.',
        ],
        mnemonic='Trait vs Process — "adaptation" carries both meanings. Always specify which.',
        flashcard={
            'front': 'What is the difference between "adaptation" as a trait and "adaptation" as a process?',
            'back': 'As a TRAIT (noun): an adaptation is a specific heritable feature shaped by past selection that increases fitness — e.g., the woodpecker\'s long tongue, the giraffe\'s neck, antifreeze proteins in Antarctic fish. As a PROCESS (verb): adaptation is the ongoing evolutionary mechanism by which populations become better matched to their environment through natural selection. These two meanings are related but distinct: the process produces the traits. In scientific papers, careful writers specify which they mean.',
        },
        quiz=[
            {
                'question': 'Which statement best describes a "novel trait" in evolution?',
                'correct': 'A trait that arises de novo and is not directly inherited from an ancestor',
                'distractors': [
                    'Any point mutation that appears in a germ cell, regardless of phenotypic effect',
                    'A trait that results from phenotypic plasticity in response to a new environment',
                    'A trait shared by two distantly related species due to convergent evolution',
                ],
            },
            {
                'question': 'A biologist observes that humans have a blind spot in their retina but octopuses do not, and that the human spine causes back pain during bipedal walking. She argues these are evidence for evolution rather than intelligent design. Which reasoning is MOST correct?',
                'correct': 'These are "imperfect" designs that only make sense as evolutionary compromises — the vertebrate blind spot is an ancestral consequence of inverted photoreceptors in early vertebrates, and the spine was shaped by selection for quadrupedal locomotion before bipedalism, not engineered for walking upright',
                'distractors': [
                    'These flaws disprove natural selection because selection should have eliminated suboptimal traits — if selection were real, the blind spot and back pain would have been corrected millions of years ago',
                    'These flaws support creationism — an intelligent designer would intentionally include imperfections to allow the organism to adapt through learned behavior rather than relying entirely on biological structure',
                    'These features are actually optimal designs — the blind spot provides a useful location for the optic nerve to exit without vision loss, and lumbar curvature in the spine is a biomechanical advantage for absorbing impact during walking',
                ],
            },
            {
                'question': 'Antagonistic pleiotropy proposes that some genes beneficial early in life are maintained despite causing harm later. Which specific example from human biology BEST illustrates this principle?',
                'correct': 'APOE ε4 allele — associated with faster brain development and potentially better immune function in youth, but dramatically increases Alzheimer\'s risk after age 60; selection on early-life benefits maintained this allele despite its late-life cost',
                'distractors': [
                    'The CCR5-Δ32 mutation — this allele confers resistance to HIV infection in homozygotes, conferring a survival benefit throughout life; it is a simple case of positive selection rather than antagonistic pleiotropy because no late-life cost is known',
                    'Sickle cell heterozygosity — HbA/HbS individuals have malaria resistance early in life but suffer reduced oxygen transport in old age, which is a textbook example of antagonistic pleiotropy because the cost appears decades after the benefit',
                    'The BRCA1 wildtype allele — maintains functional DNA repair throughout life and protects against cancer in youth, but becomes a liability in post-reproductive age when damaged alleles accumulate; this is pure mutation accumulation, not antagonistic pleiotropy',
                ],
            },
            {
                'question': 'A researcher says that sickle cell trait (heterozygous HbA/HbS) in malaria-endemic regions is NOT an adaptation in the strict evolutionary sense. What would be the most rigorous response?',
                'correct': 'Sickle cell heterozygosity IS an adaptation — it is a heritable trait (specific allele) that increases fitness (malaria resistance) in a specific environment (high malaria burden), even though HbS causes disease in homozygotes; the distinction is that adaptation is always environment-specific',
                'distractors': [
                    'The researcher is correct — adaptation requires that the trait was directly shaped BY natural selection FOR malaria resistance. Since the HbS allele arose from a sickle-cell anemia mutation, it was selected against, not for; the malaria resistance is a coincidental byproduct',
                    'Sickle cell trait is a SPANDREL, not an adaptation — the malaria protection is an incidental byproduct of reduced red blood cell rigidity that evolved for other reasons, similar to how the space between arches in a building serves a purpose not intended by the architect',
                    'Sickle cell trait cannot be an adaptation because it causes disease — by definition, adaptations only have positive fitness effects; any trait that causes harm in any genotype is classified as a deleterious mutation maintained by mutation-selection balance',
                ],
            },
            {
                'question': 'Which of the following traits would most likely be classified as a SPANDREL rather than an adaptation?',
                'correct': 'The reddish color of vertebrate blood — hemoglobin evolved for oxygen transport (the adaptation), and its red color is an incidental chemical byproduct that was not itself selected for',
                'distractors': [
                    'The camouflage coloration of a stick insect — cryptic coloration clearly provides a direct fitness advantage through reduced predation',
                    'The thick fur of an arctic fox — insulation is a direct thermoregulatory adaptation shaped by cold-climate selection',
                    'The echolocation ability of bats — a specialized sensory system shaped by selection for nocturnal foraging',
                ],
            },
            {
                'question': 'A trait is described as "vestigial." Which statement BEST captures what vestigial means in evolutionary biology?',
                'correct': 'A vestigial trait is a reduced remnant of a structure that was functional in an ancestor but has lost most or all of its original function — e.g., the human appendix, whale pelvic bones, or cave fish eyes',
                'distractors': [
                    'Vestigial traits are entirely useless and provide no function whatsoever — the moment a structure retains any function, it is no longer vestigial by definition',
                    'Vestigial traits are new structures that have only recently begun to evolve and have not yet reached their final adaptive form',
                    'Vestigial traits are traits found only in one sex of a sexually dimorphic species, reflecting the ancestral state of the opposite sex',
                ],
            },
            {
                'question': 'A novel trait in tetrapods is the limb. Which statement MOST accurately describes what "novel" means in this context?',
                'correct': 'The tetrapod limb arose from the modification of ancestral fish fin structures — "novel" means the trait as currently constituted did not exist before, even though it evolved from pre-existing parts',
                'distractors': [
                    'Novel means "arose from scratch with no ancestral precursor" — tetrapod limbs have no evolutionary ancestry and first appeared in the fossil record without transitional forms',
                    'Novel means "unique to one species" — a trait found in multiple species cannot be novel because true novelty requires species-specific origin',
                    'Novel means "beneficial" — any trait that increases fitness is by definition novel, regardless of its evolutionary ancestry',
                ],
            },
            {
                'question': 'A student confuses "adaptation" with "acclimation." Which statement correctly distinguishes these two concepts?',
                'correct': 'Adaptation is heritable genetic change across generations driven by selection; acclimation is reversible phenotypic change within an individual\'s lifetime (e.g., tanning, altitude acclimatization) that is NOT heritable',
                'distractors': [
                    'Adaptation and acclimation are the same process at different timescales — both involve genetic change, but adaptation happens faster',
                    'Acclimation is heritable and adaptation is not — acclimated phenotypes pass to offspring via Lamarckian inheritance',
                    'Adaptation occurs only in animals while acclimation occurs only in plants — the distinction is taxonomic rather than mechanistic',
                ],
            },
            {
                'question': 'L1 RECALL: Who coined the term "spandrel" in the evolutionary biology context, and in what landmark paper?',
                'correct': 'Stephen Jay Gould and Richard Lewontin, in their 1979 paper "The Spandrels of San Marco and the Panglossian Paradigm" — they used architectural spandrels as a metaphor for non-adaptive byproducts',
                'distractors': [
                    'Charles Darwin, in "On the Origin of Species" (1859) — Darwin introduced spandrels as an alternative to his own theory of natural selection',
                    'Ernst Mayr, in "Systematics and the Origin of Species" (1942) — Mayr used spandrels to describe speciation byproducts',
                    'Richard Dawkins, in "The Selfish Gene" (1976) — Dawkins defined spandrels as gene-level byproducts',
                ],
            },
            {
                'question': 'L5 SYNTHESIS: A newly discovered cave-dwelling fish has (1) reduced eyes, (2) elongated tactile barbels, (3) pale body color, and (4) high metabolic efficiency. Classify each trait as adaptation, vestigial, spandrel, or neutral, and defend your reasoning using the principles of this lecture.',
                'correct': 'Reduced eyes = VESTIGIAL (ancestral functional structure now diminished because selection for vision relaxed in darkness); elongated barbels = ADAPTATION (enhanced tactile sensing directly increases fitness in sensory-limited environment); pale body = likely NEUTRAL or vestigial byproduct of relaxed selection on pigmentation; high metabolic efficiency = ADAPTATION to low-food cave ecology. Each classification depends on whether the trait is currently maintained by selection, is a constrained byproduct, or is a remnant of past function',
                'distractors': [
                    'All four are adaptations to cave life because any trait found in a cave species must have been selected for by the cave environment — the cave is the selective regime and every derived trait is an adaptive response',
                    'All four are vestigial because cave environments reduce selection pressure on all traits — all modifications in cave animals represent loss of ancestral function',
                    'All four are spandrels because the fish\'s basic body plan was set by its ancestor and any modifications since then are mere byproducts of a single master regulatory gene change that coincidentally produces all four changes together',
                ],
            },
            {
                'question': 'L3 APPLICATION: A trait is labeled "exaptation" (Gould & Vrba 1982). Which example BEST illustrates exaptation as opposed to adaptation?',
                'correct': 'Bird feathers were originally evolved for thermoregulation or display in ancestral theropods and were later co-opted for flight — the trait evolved for one function and acquired a new function without being originally selected for flight',
                'distractors': [
                    'The human hand evolved directly for tool use — the grasp is an adaptation, not an exaptation, because tools were the selective agent from the very beginning of hominid hand evolution',
                    'The giraffe neck evolved for reaching high foliage — it is an adaptation because its current function (feeding) matches its original function',
                    'The cheetah\'s fast running muscles evolved for chasing prey — this is a pure adaptation because the current use (running down prey) matches the selective environment that shaped it',
                ],
            },
            {
                'question': 'L4 ANALYSIS: A researcher claims a particular bird song feature is an adaptation for mate attraction. What evidence would MOST RIGOROUSLY support this adaptive hypothesis rather than alternatives (spandrel, drift, developmental byproduct)?',
                'correct': 'Demonstrating heritability of the trait, showing that individuals with the trait have higher reproductive success, confirming that the trait affects mate choice in controlled playback experiments, and ruling out correlation with non-reproductive fitness components — together establishing that the trait was shaped by directional selection FOR mate attraction specifically',
                'distractors': [
                    'Showing that the trait is present in many related species — widespread presence proves adaptive function',
                    'Showing that the trait is complex — complexity alone rules out drift and byproduct explanations',
                    'Showing that the trait differs between populations — any between-population variation proves the trait is adaptive because drift would produce uniform traits',
                ],
            },
        ],
        visual={
            'type': 'distinction',
            'description': 'Adaptation as noun vs verb',
            'regions': [
                {'label': 'Trait (noun)', 'color': '#ffc857', 'items': ['Heritable feature', 'Shaped by past selection', 'Increases fitness']},
                {'label': 'Process (verb)', 'color': '#4ea8de', 'items': ['Ongoing change', 'Population-level', 'Driven by selection']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Trait = what. Process = how.',
            'trap': 'Not every trait is an adaptation. Some are byproducts of other adaptations, some are vestigial, some are selectively neutral.',
        },
    ))
    nodes.append(build_node(
        id='lec8-evo-devo',
        title='Evo-Devo & Regulatory Networks',
        subtitle='How gene networks build body plans (Lec 8 slides 7-22)',
        color='teal', row=7,
        heading='Lecture 8 — Evolutionary Developmental Biology',
        sections=[{'label': 'CORE CONCEPT', 'body': 'Evo-devo = the fusion of developmental biology with evolution. Early ideas (Meckel, Haeckel) proposed "ontogeny recapitulates phylogeny" — now only partly accepted. HOX GENES control body plan and are conserved across all bilaterians (the same Hox genes work in flies and mice despite 570 million years of separation). Vertebrates have FOUR SETS of Hox clusters due to two whole-genome duplications. Other conserved patterning genes: Distalless (Dll), Homothorax (hth). PROMISCUOUS PROTEINS can bind multiple targets, enabling evolutionary tinkering. GENE DUPLICATION produces PARALOGS that can diverge in function (neofunctionalization). 50–70% of flowering plants are polyploid. GENE RECRUITMENT co-opts existing genes for new developmental roles. Classic examples: (1) STICKLEBACKS — Pitx1 REGULATORY change (not coding change) reduces pelvic spine in freshwater populations; (2) GALÁPAGOS FINCHES — Bmp4 and calmodulin expression differences (not new genes) produce the beak diversity Darwin observed. Key insight: SMALL REGULATORY CHANGES → BIG MORPHOLOGICAL DIFFERENCES.'}] + slides_to_sections(d, (7, 22)),
        examples=[
            'Evo-devo: the study of how developmental processes evolve and how gene regulation shapes morphology.',
            'Hox genes: conserved master regulators of body plan across animals. Small changes in Hox expression → large morphological changes.',
            'Limb development: same gene network (Hox, Tbx, Sonic hedgehog) is used by all tetrapods to build limbs.',
            'Galapagos finches: beak size differences are controlled by Bmp4 and calmodulin expression differences, not new genes.',
        ],
        warnings=[
            'Regulatory and coding evolution are NOT mutually exclusive. Evo-devo emphasizes regulatory changes for large morphological differences, but coding changes (e.g., beach mouse Mc1r) also drive adaptation.',
            'Hox gene SEQUENCE conservation does NOT equal Hox FUNCTION conservation. Changing WHEN or WHERE a Hox gene is expressed can dramatically change body plan without altering the protein sequence.',
        ],
        mnemonic='Small regulatory changes → Big morphological differences. Same toolkit, different deployment.',
        flashcard={
            'front': 'Why do evolutionary biologists emphasize regulatory evolution over protein-coding evolution for explaining body plan differences?',
            'back': 'Most animals share the SAME toolkit of developmental genes — Hox, Pax, Tbx, BMP, Wnt, Sonic hedgehog. These genes are nearly identical in fruit flies, mice, and humans. Major morphological differences (legs vs. no legs, big beak vs. small beak, limbs vs. fins) arise mostly from CHANGES IN WHEN, WHERE, AND HOW MUCH these genes are expressed — not from new protein-coding genes. A single mutation in a cis-regulatory element can shift the domain of expression, producing large phenotypic effects. This is why "small changes in networks lead to new complex traits."',
        },
        quiz=[
            {
                'question': 'The striking morphological differences in beak size among Galápagos finches are produced primarily by:',
                'correct': 'Differences in the expression levels of regulatory genes like Bmp4 and calmodulin during beak development',
                'distractors': [
                    'Completely different sets of genes in each species',
                    'New proteins that evolved only in finches',
                    'Environmental sculpting of beak bone after hatching',
                ],
            },
            {
                'question': 'In evo-devo, it is often said that "small regulatory changes lead to large morphological differences." Hox genes are the classic example. If a mutation shifts the anterior expression boundary of Hox gene Hox-c6 two vertebrae forward in a snake lineage, what macroscopic effect would you PREDICT?',
                'correct': 'The thoracic-to-lumbar boundary shifts anteriorly — ribs grow on vertebrae that previously had none, extending the ribbed trunk region further toward the tail, as seen in highly elongated snake body plans with hundreds of vertebrae',
                'distractors': [
                    'The snake would develop limbs at the anterior expression boundary of Hox-c6 because Hox genes specify limb position, and shifting the boundary anteriorly repositions where limb buds are induced',
                    'The mutation would be lethal because Hox genes are perfectly conserved across all vertebrates; any change to their expression domain disrupts the basic body plan so severely that embryonic development arrests',
                    'The snake\'s scale pattern would shift anteriorly because Hox gene expression domains solely specify surface integument patterns, not internal skeletal organization in reptiles',
                ],
            },
            {
                'question': 'Cis-regulatory elements (enhancers and silencers) are non-coding DNA sequences that control when and where genes are expressed. Why are mutations in cis-regulatory elements often BETTER candidates for evolutionary change than mutations in protein-coding sequences?',
                'correct': 'Changing a protein-coding sequence affects the protein in ALL tissues and contexts simultaneously (pleiotropic), often causing collateral damage. Cis-regulatory mutations can alter expression in ONE tissue or developmental stage without affecting the protein\'s function elsewhere — enabling modular evolution with lower pleiotropic costs',
                'distractors': [
                    'Cis-regulatory mutations are better candidates because they occur at higher rates than coding mutations — non-coding DNA has no proofreading during replication, so mutations accumulate there faster than in coding regions',
                    'Protein-coding mutations are always deleterious because proteins are already optimally shaped by billions of years of selection — the only available evolutionary change left in modern species is through non-coding regulatory variation',
                    'Cis-regulatory elements are directly translated into short peptides that modulate RNA polymerase binding — because these peptides are rapidly degraded, their mutations have lower fitness effects than coding mutations that alter stable structural proteins',
                ],
            },
            {
                'question': 'The same Sonic hedgehog (SHH) signaling pathway specifies digit identity in mouse feet, tooth development in sharks, and eye patterning in flies. If a developmental biologist says "evolution uses a common toolkit," what does this imply about how new body plans evolve?',
                'correct': 'New body plans arise not by inventing new genes but by redeploying the same conserved toolkit genes in different spatial and temporal contexts — small changes in when/where toolkit genes are expressed can produce radically different morphologies with minimal protein sequence change',
                'distractors': [
                    'It implies that all multicellular animals evolved from a single common ancestor that had a complex body plan with all modern structures already present — the toolkit is conserved because all modern structures were present in the ancestor',
                    'It implies that evolution is impossible beyond the toolkit genes — all possible phenotypic variation in animals is already encoded by the limited set of toolkit genes, and no truly novel traits can arise without acquiring new genes via horizontal transfer',
                    'It implies that natural selection acts primarily on toolkit gene sequences — the extreme conservation of SHH, Hox, and Wnt sequences shows that coding-sequence changes in these genes have the highest fitness effects and are therefore the primary targets of evolution',
                ],
            },
            {
                'question': 'A key insight of evo-devo is that Hox gene SEQUENCES are highly conserved across animals (nearly identical between flies and humans), yet body plans are radically different. What is the explanation for this apparent paradox?',
                'correct': 'Changing WHEN and WHERE a Hox gene is expressed (via cis-regulatory mutations in enhancers and silencers) produces body plan differences without altering the Hox protein itself — conservation of protein sequence does NOT mean conservation of expression pattern',
                'distractors': [
                    'Hox genes have no role in body plan formation despite being conserved — the radical morphological differences between flies and humans are explained by completely different, non-Hox gene networks',
                    'The conserved Hox sequences prove that all animals have nearly identical body plans at the molecular level — apparent morphological differences are superficial illusions produced by different cuticle or skin pigments',
                    'Hox genes are actively changing but the change has been too slow to detect — given another hundred million years, fly and human Hox sequences will diverge enough to match the observed body plan differences',
                ],
            },
            {
                'question': 'Galápagos finch beak morphology is controlled by differential expression of Bmp4 and calmodulin. If a researcher wanted to confirm that Bmp4 directly causes beak depth differences (not simply correlates with them), what experimental approach would provide the strongest evidence?',
                'correct': 'Experimentally over-express Bmp4 in the developing beak of a small-beaked species and observe whether this phenocopies the deep-beaked species morphology — direct manipulation establishes causation beyond correlation',
                'distractors': [
                    'Sequence the Bmp4 protein from all 15 Darwin finch species and show that amino acid changes correlate with beak depth — protein sequence evolution is the gold standard for proving gene function',
                    'Cross breed finches with different beak shapes and show that F1 hybrids have intermediate beaks — hybridization demonstrates genetic control but does not identify which gene causes the difference',
                    'Feed finches different diets to see if beak shape can be environmentally induced — ruling out environmental causation is equivalent to proving genetic causation',
                ],
            },
            {
                'question': 'In the context of evo-devo, the "beach mouse Mc1r" example from Lecture 7 is cited as a CONTRAST to most regulatory evolution examples. What does this contrast illustrate?',
                'correct': 'Mc1r is an example of PROTEIN-CODING evolution — a coding-sequence change in the receptor causes pale coat color in beach mice. It shows that both coding and regulatory changes can drive adaptation; evo-devo emphasizes regulatory changes for LARGE morphological differences but coding changes still matter for simpler traits',
                'distractors': [
                    'The Mc1r example proves evo-devo is wrong — all evolution proceeds through coding changes, and regulatory mutations are rare',
                    'Mc1r shows that regulatory and coding changes always co-occur — every adaptation involves both types of mutation simultaneously, making the distinction meaningless',
                    'The beach mouse example is irrelevant to evo-devo because color is not a "body plan" trait, so no conclusions about regulatory vs. coding evolution can be drawn from it',
                ],
            },
            {
                'question': 'Why is the concept of MODULARITY important to evo-devo theory?',
                'correct': 'Modularity means that developmental units (e.g., individual body segments, limbs, teeth) can evolve somewhat independently because they are controlled by semi-independent gene regulatory networks — this allows evolution of one body part without disrupting others, enabling mosaic evolution',
                'distractors': [
                    'Modularity means that all body parts evolve in lock-step — changes in one module automatically cause proportional changes in all other modules, which is why evolution is constrained',
                    'Modularity refers to the physical separation of genes on different chromosomes — genes on different chromosomes cannot influence each other and therefore evolve independently',
                    'Modularity is a property of the genome rather than of development — it means genes are arranged in modules of ~1000 bp that can be shuffled during recombination',
                ],
            },
            {
                'question': 'L1 RECALL: In three-spine sticklebacks, freshwater populations have reduced pelvic spines. What gene has been identified as the regulatory locus driving this loss, and what type of change is it?',
                'correct': 'Pitx1 — the change is in a cis-regulatory element (enhancer), not in the protein-coding sequence. Freshwater fish carry a mutation that deletes an enhancer specifically driving Pitx1 expression in the pelvic region, so the protein is normal elsewhere but absent at the pelvis',
                'distractors': [
                    'Bmp4 — the regulatory change decreases Bmp4 expression in the pelvic region',
                    'Sonic hedgehog (SHH) — a coding mutation in SHH disrupts pelvic development',
                    'Hox-c6 — the Hox-c6 protein has a new amino acid that fails to specify pelvic vertebrae',
                ],
            },
            {
                'question': 'L1 RECALL: Approximately how many years of evolutionary separation exist between flies and mice, during which their Hox gene sequences have remained remarkably similar?',
                'correct': 'Approximately 570 million years — flies and mice diverged near the base of the bilaterian radiation, yet their Hox genes are so similar that mouse Pax6 can induce eye formation in flies',
                'distractors': [
                    'Approximately 60 million years',
                    'Approximately 3 billion years',
                    'Approximately 10 million years',
                ],
            },
            {
                'question': 'L5 SYNTHESIS: Integrate evo-devo principles with regulatory evolution to explain why closely related species can have dramatically different body plans while sharing nearly identical Hox protein sequences. Use stickleback Pitx1 and finch Bmp4 as supporting examples.',
                'correct': 'Major morphological evolution proceeds primarily through CIS-REGULATORY CHANGES that alter WHEN and WHERE conserved toolkit genes are expressed, not through protein-coding changes. Stickleback pelvic loss arises from enhancer deletion at Pitx1 (protein intact, expression absent). Finch beak variation arises from differences in Bmp4 and calmodulin expression timing/levels. Both examples show that because toolkit proteins are pleiotropic (used many places), coding changes would be too disruptive — but local enhancer changes alter one tissue/stage at a time, enabling modular morphological evolution without compromising protein function elsewhere',
                'distractors': [
                    'Closely related species have different body plans because of rapid Hox protein sequence evolution that occurred after divergence — the "conservation" seen in flies/mice does not apply to closely related species',
                    'Body plan differences are produced only by whole-genome duplications that generate redundant gene copies free to evolve new functions — closely related species have different body plans because each underwent independent polyploidy events',
                    'Morphological differences arise from horizontal gene transfer between closely related species — conserved Hox proteins are inherited from a common ancestor, but body plan genes are swapped between species during evolution',
                ],
            },
            {
                'question': 'L3 APPLICATION: If the same Hox gene "toolkit" is conserved across all animals, what experimental prediction does evo-devo make about heterologous gene swaps (e.g., putting a mouse gene into a fly)?',
                'correct': 'Toolkit genes should be substantially interchangeable — the famous Halder/Callaerts/Gehring experiment showed mouse Pax6 can induce ectopic eye formation in Drosophila, demonstrating deep conservation of the eye-specification master regulator across 570 million years of separation',
                'distractors': [
                    'Toolkit genes should NOT be interchangeable across phyla — the 570 million years of divergence has produced species-specific genes that cannot function in foreign genomes',
                    'Toolkit genes should function but produce novel phenotypes not seen in either species — cross-species insertions always yield hybrid morphologies',
                    'Toolkit genes can only be swapped within the same family (e.g., mouse to human) — cross-phylum swaps never work because regulatory context differs',
                ],
            },
        ],
        visual={
            'type': 'network',
            'description': 'Regulatory network producing diversity',
            'regions': [
                {'label': 'Shared toolkit', 'color': '#4ea8de', 'items': ['Hox genes', 'BMP, Wnt, SHH', 'Pax, Tbx']},
                {'label': 'Regulatory changes', 'color': '#7de2d1', 'items': ['Cis-regulatory elements', 'Enhancer mutations', 'Expression timing/level']},
                {'label': 'Output', 'color': '#ffc857', 'items': ['Novel body plans', 'Species-specific traits']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Same genes, different expression = different species.',
            'trap': 'Coding sequence changes matter too (e.g., Mc1r in beach mice) but regulatory changes dominate for large morphological differences.',
        },
    diagram=hox_regulatory_network_diagram(),
    ))
    nodes.append(build_node(
        id='lec8-eye-evolution',
        title='Eye Evolution: From Photoreceptors to Camera Eyes',
        subtitle='Classic complex trait case study (Lec 8 slides 23-30)',
        color='blue', row=7,
        heading='Lecture 8 — Evolution of the Eye',
        sections=[{'label': 'CORE CONCEPT', 'body': 'Darwin (1859) himself called eye evolution "absurd in the highest possible degree" at first glance but then explained exactly how it could evolve gradually. OPSINS are conserved GPCR (G-protein coupled receptor) proteins that detect light. Three primary opsin types exist: C-opsins (ciliary, as in vertebrates), R-opsins (rhabdomeric, as in insects), and RGR/Go opsins. CRYSTALLINS — the transparent proteins of the lens — were RECRUITED from pre-existing heat-shock proteins and metabolic enzymes (exaptation/co-option). EYE STAGE SEQUENCE: flat photoreceptor patch → pit → pinhole → lens eye. Each stage is functional and provides fitness benefit on its own. NILSSON & PELGER (1994) calculated that going from a flat eyespot to a camera eye requires only ~350,000 generations under weak selection — trivially fast on geological timescales. PAX6 is the master control gene: mouse Pax6 placed into a fly can induce a (fly-style) eye on the fly\'s leg. MOLLUSKS today show ALL intermediate stages: flat-eyespot limpets, pit-eye abalone, pinhole-eye Nautilus, camera-eye squid and octopus. CONVERGENT CAMERA EYES: vertebrate and cephalopod camera eyes are CONVERGENT (not homologous as organs) — vertebrate retina has a blind spot due to inverted photoreceptors; octopus retina does NOT have a blind spot.'}] + slides_to_sections(d, (23, 30)),
        examples=[
            'Photoreceptive cells were the earliest step — a single opsin molecule in a light-sensitive cell.',
            'Opsin gene was duplicated twice early in animal evolution, creating different light-sensitivity classes.',
            'Crystallins: transparent proteins that make up the lens — many are recruited from pre-existing enzymes (e.g., lactate dehydrogenase in some species).',
            'Eye stages: simple photoreceptor patch → pit → pinhole → lensed camera eye.',
            'Mollusks alone show ALL intermediate eye stages today — flat eyespots (limpets), pit eyes (abalone), pinhole eyes (Nautilus), lensed eyes (squid, octopus).',
        ],
        warnings=[
            'Vertebrate and cephalopod camera eyes are CONVERGENT, not homologous as complete organs. They share the opsin toolkit but evolved camera structure independently — proven by the inverted (vertebrate) vs. non-inverted (octopus) retina.',
            'Irreducible complexity is disproved by molluskan intermediates. Each eye stage — flat patch, pit, pinhole, lensed — provides real fitness advantage, and all stages exist today in different mollusks (limpets, abalone, Nautilus, squid).',
        ],
        mnemonic='From patch to camera: each stage provides its own fitness advantage. No "half eye" problem.',
        flashcard={
            'front': 'How does eye evolution refute the creationist claim of "irreducible complexity" for complex organs?',
            'back': 'The argument from irreducible complexity claims complex organs like the eye cannot evolve because "half an eye" is useless. However, eye evolution shows INTERMEDIATE stages are each FUNCTIONAL and BENEFICIAL: (1) A photoreceptive patch detects light vs. dark (useful for circadian rhythm or shadow warning). (2) A cupped patch gives directional information. (3) A deepened cup becomes a pinhole, giving crude image formation. (4) A lens sharpens the image. All these stages exist TODAY in different mollusks (flatworms, limpets, abalone, Nautilus, squid) — providing living evidence of each intermediate. Crystallins (lens proteins) were recruited from pre-existing enzymes via gene duplication and co-option, not invented from scratch.',
        },
        quiz=[
            {
                'question': 'Why is the evolution of the eye often used to refute "irreducible complexity" arguments?',
                'correct': 'Every intermediate stage of eye evolution (patch, pit, pinhole, lensed) is functional and provides fitness benefit',
                'distractors': [
                    'The eye is identical across all animal phyla, showing a single evolutionary origin that requires no intermediate steps',
                    'Crystallin lens proteins were newly evolved specifically for vision, with no precursor function in other tissues',
                    'Vertebrate and cephalopod eyes share identical retinal organization, proving they descended from a single complex ancestor',
                ],
            },
            {
                'question': 'Lens crystallin proteins in many species are structurally similar to metabolic enzymes (e.g., lactate dehydrogenase in some vertebrates). How does this fact challenge "irreducible complexity" and support evolutionary theory?',
                'correct': 'It demonstrates gene co-option (exaptation) — lens proteins were not invented from scratch for vision but were recruited from pre-existing metabolic genes that happened to be transparent and stable in the eye. Evolution builds complexity from available parts, not from nothing',
                'distractors': [
                    'It challenges evolution because metabolic enzymes and lens crystallins serve completely different functions — the structural similarity must reflect convergent evolution to a stable protein fold, not shared ancestry',
                    'It supports irreducible complexity — lens proteins that evolved from metabolic enzymes must have been functional at each intermediate stage ONLY as metabolic enzymes, not as lens components, meaning there was never a viable intermediate that was PARTLY a lens',
                    'Crystallin genes being similar to metabolic genes proves horizontal gene transfer between eye tissue and liver tissue — lens proteins were not evolved in the eye but were acquired from metabolic organs when photoreceptors first appeared',
                ],
            },
            {
                'question': 'The Nautilus (a cephalopod mollusk) has a pinhole eye — no lens, just a small aperture. Its vision is blurry but directional. A human\'s lensed camera eye produces a sharp image. Both are in the SAME phylum. What does this co-occurrence of eye stages within Mollusca most strongly demonstrate?',
                'correct': 'All intermediate stages of eye evolution are selectively viable and have persisted in different lineages — Nautilus\'s pinhole eye is not a "failed" design but a functional solution that has been stable for hundreds of millions of years, directly proving each stage provides sufficient fitness',
                'distractors': [
                    'Nautilus represents a degenerate lineage that lost its ancestral lensed eye — the pinhole eye is a regressed stage, not an intermediate, which means eye evolution can go backward as well as forward',
                    'Nautilus and squid are distantly related within Mollusca and their eye differences reflect independent origins — the Nautilus evolved its pinhole eye from scratch while squid independently evolved their camera eye, so the two eye types share no evolutionary pathway',
                    'The co-occurrence proves that eyes evolved by horizontal transfer from arthropods — mollusks acquired different eye-development genes from different arthropod lineages, explaining why Nautilus has a simple arthropod-style eye and squid have a complex vertebrate-style eye',
                ],
            },
            {
                'question': 'Vertebrate camera eyes have photoreceptors facing AWAY from incoming light (inverted retina), creating a blind spot. Cephalopod camera eyes have photoreceptors facing TOWARD the light (non-inverted retina) with no blind spot. What does this difference MOST directly prove about the two eye types?',
                'correct': 'Vertebrate and cephalopod camera eyes are convergent (independently evolved) — their different retinal orientations reflect different developmental origins. If they had a common complex-eye ancestor, both would have the same retinal wiring; the inverted vertebrate retina traces to an ancestral inversion in early chordate neural development',
                'distractors': [
                    'The vertebrate blind spot proves that vertebrate eyes are evolutionarily newer than cephalopod eyes — older, more primitive eyes have the correct photoreceptor orientation while newer, recently evolved eyes have not yet been perfected by selection',
                    'The difference proves that cephalopods are more closely related to vertebrates than other invertebrates — only a shared ancestor very close to the vertebrate lineage would have passed on the correct retinal orientation to cephalopods',
                    'The inverted vertebrate retina proves intelligent design — no evolutionary process would produce an eye with photoreceptors facing the wrong direction, so the vertebrate eye must have been designed with the blind spot intentionally included for an unknown purpose',
                ],
            },
            {
                'question': 'Opsin genes underwent two rounds of duplication early in animal evolution, producing different light-sensitivity classes. Why was gene duplication essential to the evolution of color vision?',
                'correct': 'A single opsin can only detect one wavelength peak of light — to distinguish colors, an animal needs multiple opsins with different spectral sensitivities. Gene duplication generated extra copies that could diverge in sequence and detect different wavelengths without losing the original function',
                'distractors': [
                    'Gene duplication was needed to produce more total opsin protein in photoreceptor cells — animals with duplicated opsin genes simply made more of the same protein, increasing sensitivity but not color discrimination',
                    'Opsin duplication enabled photoreceptors to process light at different times of day — one copy works at night and another during the day, but both detect the same wavelength range',
                    'Duplication was required because opsins degrade rapidly in light — having multiple gene copies provides a constant replacement supply for the functional protein',
                ],
            },
            {
                'question': 'Identify the correct sequence of eye evolution stages as typically presented:',
                'correct': 'Photoreceptor patch → pit → pinhole → lensed camera eye — each stage builds directly on the previous, with pinhole stage achieving crude image formation BEFORE the evolution of a lens',
                'distractors': [
                    'Lensed eye → pit → pinhole → patch — complex eyes evolved first and then degenerated in simpler organisms',
                    'Patch → pinhole → pit → lens — the pinhole stage preceded the cupped pit stage in cephalopod evolution',
                    'Patch → lens → pit → pinhole → camera — the lens evolved first as a separate structure before being incorporated into a pit eye',
                ],
            },
            {
                'question': 'Darwin himself wrote that the evolution of the eye "seems absurd in the highest degree" when considered at first glance. Why did he write this, and what was his resolution?',
                'correct': 'Darwin acknowledged that the eye APPEARS too complex to evolve gradually — this was a rhetorical acknowledgment of the challenge. He resolved it by showing that intermediate stages (as seen today in different species) provide functional vision at each level, demonstrating that "half an eye" IS useful',
                'distractors': [
                    'Darwin genuinely believed the eye could not evolve and admitted natural selection had one major failure — his theory of eye evolution was rejected by later biologists',
                    'Darwin said eye evolution was absurd because it violated his principles — he argued the eye was designed and used this admission to reconcile his theory with natural theology',
                    'Darwin said the eye could not evolve gradually, but proposed it evolved by sudden saltation — all at once in a single generation via a massive mutation in a single ancestor',
                ],
            },
            {
                'question': 'L1 RECALL: In the famous Nilsson & Pelger (1994) simulation of eye evolution, approximately how many generations did they calculate were needed to evolve a camera eye from a flat photoreceptor patch under modest selection?',
                'correct': 'Approximately 350,000 generations — a geologically trivial time span showing that the eye could evolve quickly and repeatedly under even weak selection',
                'distractors': [
                    'Approximately 100 million generations',
                    'Approximately 50 generations',
                    'Approximately 10 billion generations',
                ],
            },
            {
                'question': 'L1 RECALL: Which gene is referred to as the "master control gene" for eye development across animals, such that its mouse version can induce ectopic eyes when inserted into flies?',
                'correct': 'Pax6 — the master regulator of eye development conserved across bilaterians. Mouse Pax6 inserted into fruit fly legs or antennae induces formation of (fly-style) eyes, demonstrating extreme conservation of the eye-development program',
                'distractors': [
                    'Sonic hedgehog (SHH) — the master regulator of eye development across animals',
                    'Hox-b6 — the primary eye-specification gene across all animal phyla',
                    'Wnt7a — the gene that induces ectopic eyes when inserted into flies from mice',
                ],
            },
            {
                'question': 'L4 ANALYSIS: A mutation in an ancestral animal produces a shallow cup-shaped depression in its light-sensitive patch. How would this structural change directly improve fitness compared to a flat photoreceptor patch, and why is this the critical first "real eye" step?',
                'correct': 'A cup gives DIRECTIONAL INFORMATION — an organism can now sense not just presence/absence of light but the direction from which light is coming. This lets it orient toward/away from light sources, detect approaching shadows (predators), and navigate — all of which are substantial fitness improvements over detecting only ambient brightness. It is the first step toward image formation',
                'distractors': [
                    'The cup shape amplifies light intensity by concentrating photons onto fewer cells — brighter images are the fitness advantage over flat patches',
                    'The cup protects photoreceptors from UV damage — UV protection, not directional sensing, is the first fitness advantage',
                    'The cup has no functional advantage over a flat patch until it deepens into a pinhole — the intermediate cup stage is selectively neutral and exists only as a transitional form',
                ],
            },
            {
                'question': 'L5 SYNTHESIS: A creationist argues that the VERTEBRATE EYE could not evolve because removing any component (lens, retina, cornea) destroys vision entirely. Construct a rebuttal integrating (a) molluscan eye diversity, (b) crystallin exaptation, (c) opsin gene duplication, (d) the Nilsson & Pelger calculation, and (e) the functional intermediate-stage principle.',
                'correct': 'The creationist\'s "irreducible complexity" argument fails on all five fronts: (a) Mollusks TODAY show every eye stage (limpet patch, abalone pit, Nautilus pinhole, squid/octopus lens) proving each is functional; (b) Crystallin lens proteins were CO-OPTED from heat-shock and metabolic enzymes, so lens material was not invented from scratch; (c) Opsins arose from gene duplication producing functional light receptors incrementally; (d) Nilsson & Pelger showed only ~350,000 generations are required under weak selection — trivially fast geologically; (e) Every intermediate provides real fitness benefit, so selection could proceed at each step. The vertebrate eye is not a step-removal puzzle but a step-ADDITION success story',
                'distractors': [
                    'The creationist is correct that the vertebrate eye is irreducibly complex, but this does not disprove evolution because God may have used evolution as a tool to build the eye',
                    'The rebuttal should focus only on molluscan eye diversity — the crystallin, opsin, and simulation evidence are irrelevant because they deal with molecular details rather than the fitness question',
                    'Irreducible complexity is a valid concept and the vertebrate eye really is irreducibly complex — the resolution is that the vertebrate eye was acquired by horizontal gene transfer from cephalopods rather than evolving incrementally',
                ],
            },
        ],
        visual={
            'type': 'stages',
            'description': 'Eye evolution stages',
            'regions': [
                {'label': '1. Patch', 'color': '#6e6a80', 'items': ['Opsin photoreceptors', 'Light/dark only']},
                {'label': '2. Pit', 'color': '#8a5cf6', 'items': ['Directional light', 'Crude vision']},
                {'label': '3. Pinhole', 'color': '#4ea8de', 'items': ['Image formation', 'No lens']},
                {'label': '4. Lensed', 'color': '#7de2d1', 'items': ['Focused image', 'Crystallin lens']},
                {'label': '5. Camera eye', 'color': '#ffc857', 'items': ['Variable focus', 'Iris, cornea']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Patch → Pit → Pinhole → Lens → Camera.',
            'trap': 'Vertebrate and cephalopod camera eyes are CONVERGENT (not homologous as complete organs) — they share the opsin toolkit but arrived at the camera design independently.',
        },
    diagram=eye_evolution_stages_diagram(),
    ))
    nodes.append(build_node(
        id='lec8-flaws-pleiotropy',
        title='Imperfect Adaptations & Antagonistic Pleiotropy',
        subtitle='Why organisms are not optimally designed (Lec 8 slides 31-35)',
        color='red', row=7,
        heading='Lecture 8 — Flaws in Complex Adaptations',
        sections=[{'label': 'CORE CONCEPT', 'body': 'Evolution can only modify what already exists — it is TINKERING, not engineering. This produces IMPERFECT ADAPTATIONS: (1) the vertebrate RETINA has photoreceptors facing AWAY from incoming light, creating a blind spot where the optic nerve exits; cephalopod retinas do not have this flaw. (2) The RECURRENT LARYNGEAL NERVE detours around the aorta (extreme case in giraffes — meters of unnecessary nerve length), a vestige of the fish jaw-to-gill pathway in ancestors. (3) The HUMAN SPINE evolved from a quadruped\'s horizontal backbone and causes chronic back pain under bipedalism. (4) The CROSSED PHARYNX (food and air pass the same tube) causes choking. ANTAGONISTIC PLEIOTROPY: genes beneficial EARLY in life but detrimental LATE are favored by selection because early benefits come before late costs. Examples: Hox genes controlling cervical vertebrae are linked to metabolism and pediatric cancers — this is why mammals ALL have 7 cervical vertebrae (manatees have 6, sloths have 5/6/8/9 exceptions); p53 and testosterone also show AP. Williams\' AP theory connects to aging (see Lec 12).'}] + slides_to_sections(d, (31, 35)),
        examples=[
            'Vertebrate retina: photoreceptors face AWAY from incoming light; blood vessels and optic nerve pass in front of the retina, creating a blind spot. Cephalopod retinas do NOT have this flaw.',
            'Human spine: evolved from a quadruped\'s horizontal backbone — bipedalism causes chronic back pain.',
            'Antagonistic pleiotropy: a gene that increases early reproduction but shortens lifespan (or causes disease later) will be favored because reproduction happens first.',
        ],
        warnings=[
            'Evolution optimizes LOCALLY, not globally. There is no perfect design — only the best modification of what already exists given developmental and ancestral constraints.',
        ],
        mnemonic='AP + Tinkering = Flaws. Evolution optimizes locally.',
        flashcard={
            'front': 'What is antagonistic pleiotropy and how does it explain why aging and age-related diseases persist in human populations?',
            'back': 'ANTAGONISTIC PLEIOTROPY: one gene affects multiple traits (pleiotropy), with OPPOSING (antagonistic) fitness effects — beneficial for one trait but harmful for another. A classic example: a gene allele that INCREASES REPRODUCTIVE SUCCESS in young adulthood but CAUSES DISEASE or death in old age. Because reproduction happens first, the early benefit outweighs the late cost in terms of passing the allele on — so selection FAVORS the allele. This explains why humans suffer age-related diseases (Alzheimer\'s, cancer, heart disease): alleles contributing to these conditions in old age were (and are) maintained because they improved reproductive success earlier in life. This is why "why do organisms age" has a clear evolutionary answer: selection is weak on traits expressed after reproduction.',
        },
        quiz=[
            {
                'question': 'The vertebrate retina has a blind spot because photoreceptors face away from incoming light and the optic nerve passes in front. This is best explained as:',
                'correct': 'Evolutionary tinkering — constrained by ancestral developmental pathways, not optimal design',
                'distractors': [
                    'Optimal design for human vision',
                    'A necessary consequence of using opsins',
                    'A sign that vision evolved recently',
                ],
            },
            {
                'question': 'Antagonistic pleiotropy predicts that alleles with early benefits and late costs will be favored by natural selection. In which population would such alleles be MOST strongly favored?',
                'correct': 'A population with high extrinsic mortality (predators, disease) where few individuals survive to old age — selection on late-life effects is inherently weak because most individuals die before those effects are expressed',
                'distractors': [
                    'A large, highly outbred population where all individuals reproduce early and late — large population size maximizes selection efficiency, making the early benefit dominate even over large late-life costs',
                    'A population that reproduces slowly with few offspring and long lifespan — K-selected organisms invest heavily in each offspring and can afford late-life costs because their reproductive span is long enough for late-life effects to accumulate reproductive consequences',
                    'A population with no extrinsic mortality and low reproductive rate — the lack of predators means all individuals reach old age and experience the late-life cost, which creates strong selection to eliminate the allele',
                ],
            },
            {
                'question': 'The recurrent laryngeal nerve in mammals (including humans and giraffes) descends from the brain, loops around the aorta, and then travels back UP to the larynx. In a giraffe, this creates a nerve that is several meters longer than necessary. Why is this considered evidence for evolution by descent with modification?',
                'correct': 'The looping pathway made sense in the common ancestor of vertebrates (where the heart and neck were close together in fish), and as the neck and chest elongated in the tetrapod lineage, selection could not efficiently redesign the nerve path — it was trapped in its ancestral route by developmental constraints',
                'distractors': [
                    'The looping nerve in giraffes provides a strong evidence for optimal design — the long nerve slows nerve impulse transmission, which gives the larynx muscles more reaction time to coordinate swallowing with the giraffe\'s long esophageal peristalsis',
                    'The recurrent laryngeal nerve evolved its looping path due to directional mutation pressure on chromosome regions encoding neural developmental genes — it is an example of neutral molecular evolution producing a non-adaptive anatomical oddity',
                    'The long nerve loop supports group selection — it reduces individual giraffe fitness but slows nerve signal speed uniformly across the population, keeping vocal signal timing consistent for coordinated group behavior',
                ],
            },
            {
                'question': 'If antagonistic pleiotropy truly explains human aging, what prediction does this make about the optimal lifespan in a population with VERY low extrinsic mortality (e.g., modern medicine greatly extended lifespan)?',
                'correct': 'The prediction is that modern humans will be increasingly exposed to late-life costs of alleles previously maintained for early benefits, meaning age-related disease prevalence should INCREASE as average lifespan extends beyond the ancestral reproductive period — which is consistent with observed rising rates of Alzheimer\'s, cancer, and cardiovascular disease',
                'distractors': [
                    'Low extrinsic mortality will allow selection to eventually purge all antagonistically pleiotropic alleles because individuals now live long enough for the late-life costs to be expressed before reproduction ends — so Alzheimer\'s and cancer genes will be eliminated within a few thousand generations',
                    'The prediction is that the optimal lifespan should decrease in modern populations — without predators to exert early extrinsic mortality, selection pressure on reproductive rate is eliminated and r-selection takes over, favoring fast maturation and early death',
                    'Low extrinsic mortality makes antagonistic pleiotropy irrelevant — once medicine can treat the late-life costs (cancer, heart disease), selection pressure is equalized across the lifespan and all pleiotropic alleles are maintained at mutation-selection balance regardless of their early benefits',
                ],
            },
            {
                'question': 'Why is the human spine cited as an example of evolutionary "tinkering" rather than design?',
                'correct': 'The spine evolved to support a horizontal quadrupedal backbone; when human ancestors became bipedal, the existing vertebral structure was modified into a weight-bearing column it was never "designed" for — producing chronic back problems that an engineer could have avoided',
                'distractors': [
                    'The spine is an example of optimal design because it supports the full body weight over a narrow column with efficient lever mechanics — chronic back pain is caused by poor posture, not the underlying anatomy',
                    'The spine supports perfect bipedal walking; back pain is a modern lifestyle problem caused by sitting rather than any evolutionary imperfection',
                    'The spine evolved directly for bipedalism from an ancestor that was already upright — there was no quadrupedal ancestor in the human lineage',
                ],
            },
            {
                'question': 'Humans share a crossed airway and esophagus, which allows choking when food accidentally enters the trachea. What is the best evolutionary explanation for this anatomical flaw?',
                'correct': 'The crossed airway-esophagus pathway is a holdover from aquatic ancestors in which the respiratory and digestive passages evolved from a shared pharyngeal tube — terrestrial vertebrates inherited this overlap because redesigning the throat anatomy would require radical developmental reorganization',
                'distractors': [
                    'The crossed design is optimal for speech — without the overlapping passages, humans could not produce the range of vocal sounds required for language, so the choking risk is a fair trade-off',
                    'Choking is an unrelated problem caused by learned behaviors — anatomical crossing of airways evolved for a different adaptive purpose entirely and has nothing to do with ancestral constraints',
                    'The crossed passages evolved during bipedalism — walking upright required a radical rearrangement of throat anatomy that happened to create the choking hazard as a necessary consequence of bipedalism',
                ],
            },
            {
                'question': 'A student argues: "Anatomical flaws like the blind spot and back pain are proof that evolution is false — a perfect designer would not make such mistakes." How should an evolutionary biologist respond?',
                'correct': 'The flaws are actually strong EVIDENCE FOR evolution because they are exactly what descent-with-modification predicts: ancestral constraints produce jury-rigged solutions. A rational designer starting from scratch would not produce these flaws, but evolution cannot start from scratch — it can only modify what already exists',
                'distractors': [
                    'The student is correct — anatomical flaws do disprove evolution by natural selection, but they do not disprove evolution itself; they just show that selection is not the mechanism',
                    'Anatomical flaws support intelligent design because the designer intentionally included imperfections to make each species distinct, and these imperfections became the species identifiers',
                    'Anatomical flaws disprove selection but support genetic drift as the main evolutionary mechanism — since the flaws are selectively neutral, they must have drifted to fixation',
                ],
            },
            {
                'question': 'Which of these human anatomical features is BEST explained as a result of antagonistic pleiotropy rather than simple developmental constraint?',
                'correct': 'Testosterone production in young men — boosts early reproductive success by increasing muscle mass, aggression, and mate competition, but also increases late-life risk of cardiovascular disease and prostate cancer',
                'distractors': [
                    'The blind spot in the retina — this is a clear case of antagonistic pleiotropy because photoreceptors trade off vision quality for metabolic efficiency',
                    'The recurrent laryngeal nerve\'s long loop — the nerve length provides an antagonistic pleiotropic benefit through slower nerve signal timing',
                    'The wisdom teeth that often cause impaction — these are antagonistically pleiotropic because they benefited early hominids with larger jaws but now cause problems',
                ],
            },
            {
                'question': 'L1 RECALL: Most mammals have 7 cervical vertebrae regardless of neck length (mouse, giraffe, human). What are the rare exceptions cited in the lecture?',
                'correct': 'Manatees have 6 cervical vertebrae, and sloths vary (5, 6, 8, or 9 depending on species) — these exceptions suggest the "7-only" rule is tied to Hox gene pleiotropy with metabolism and pediatric cancer risk',
                'distractors': [
                    'Elephants have 12 cervical vertebrae; whales have 4',
                    'All mammals without exception have 7 cervical vertebrae — the "rule" has no known violators',
                    'Bats have 10 cervical vertebrae; marsupials have 3',
                ],
            },
            {
                'question': 'L1 RECALL: The giraffe recurrent laryngeal nerve provides a dramatic example of evolutionary tinkering. Approximately how much longer is its path than the direct route from brain to larynx?',
                'correct': 'Several meters — the nerve descends from the brain down the neck, loops around the aorta in the chest, and travels back up to the larynx, producing a total length of around 4-5 meters compared to a direct route of only ~10 cm',
                'distractors': [
                    'A few centimeters — the nerve takes a slightly longer path but not dramatically so',
                    'Exactly twice the length — the nerve loops once and returns, doubling the direct distance',
                    'Less than the direct route — the looping actually shortens the total nerve path by taking advantage of internal body structures',
                ],
            },
            {
                'question': 'L5 SYNTHESIS: Integrate antagonistic pleiotropy, the force-of-selection concept, and the constraint of "tinkering" to explain why modern humans suffer more age-related disease (Alzheimer\'s, cancer, cardiovascular disease) than our ancestral environment would have produced.',
                'correct': 'Ancestral humans had high extrinsic mortality and short life expectancies, so selection operated strongly on traits expressed before ~40-50 years. Many alleles conferring EARLY benefits (e.g., strong testosterone, robust inflammation, cell proliferation) also cause LATE costs (cardiovascular disease, cancer, Alzheimer\'s) — antagonistic pleiotropy allowed these to persist because the late costs rarely occurred. Modern medicine extends lifespan well beyond the ancestral reproductive period, EXPOSING the late-life costs that selection never purged. Additionally, tinkering (not engineering) means evolution could not design a clean separation between early-benefit and late-cost pathways',
                'distractors': [
                    'Modern disease burden is due entirely to diet and lifestyle — evolution produced optimal humans and modern diseases are cultural, not biological',
                    'Modern humans are genetically inferior to ancestors because selection has relaxed — we are accumulating new deleterious mutations',
                    'Age-related diseases are a sign that humans are at an evolutionary dead end — natural selection has failed and will not resume without intervention',
                ],
            },
        ],
        visual={
            'type': 'concept',
            'description': 'Flaws reveal tinkering',
            'regions': [
                {'label': 'Examples of flaws', 'color': '#ff6b6b', 'items': ['Blind spot (vertebrate retina)', 'Back pain (bipedal spine)', 'Choking (crossed food/air paths)', 'Aging (antagonistic pleiotropy)']},
                {'label': 'Why', 'color': '#ffc857', 'items': ['Constrained by ancestry', 'Selection optimizes locally', 'No global design']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Design ≠ Evolution. Tinkering leaves traces.',
            'trap': 'Flaws DO NOT refute evolution — they support it. They show the jury-rigged nature of descent with modification.',
        },
    ))
    return nodes


def lec9_nodes():
    d = load_lec('lec9')
    nodes = []
    nodes.append(build_node(
        id='lec9-coevolution-intro',
        title='Coevolution: Species as Selective Agents',
        subtitle='When evolution of one species drives evolution of another (Lec 9 slides 1-5)',
        color='purple', row=8,
        heading='Lecture 9 — Coevolution Introduction',
        sections=[{'label': 'CORE CONCEPT', 'body': 'COEVOLUTION = RECIPROCAL evolutionary change in two or more interacting species, with each species acting as a selective force on the other. Requirements: (1) close ecological interaction, (2) heritable variation in interacting traits in both species, (3) fitness effects on BOTH species. Both species must show reciprocal selection — if only one species is evolving in response to the other, it is adaptation but NOT coevolution. OUTCOMES can be (a) mutualistic (both benefit), (b) commensal (one benefits, other unaffected), or (c) antagonistic (one benefits at the other\'s cost — arms race). Classic fungi/plant examples illustrate tight mutualistic coevolution. Coevolution is strongest in intimate, long-term, specific interactions. Generalist predators don\'t coevolve tightly with any single prey because they spread selective pressure across many species.'}] + slides_to_sections(d, (1, 5)),
        examples=[
            'Coevolution: reciprocal evolutionary change in two or more interacting species.',
            'Types of interaction: antagonistic (predator-prey, parasite-host), mutualistic (pollinator-flower), neutral/commensal.',
            'Strong coevolution requires intimate, long-term, specific interaction — generalists coevolve weakly.',
        ],
        warnings=[
            'Coevolution requires RECIPROCAL evolution. If only one species is changing in response to the other, that is adaptation — not coevolution.',
            'Generalist predators don\'t tightly coevolve with any single prey species because selective pressure is diluted across the many prey they consume.',
        ],
        mnemonic='Coevolution = Reciprocal change. Both species adapt to each other.',
        flashcard={
            'front': 'What is the difference between coevolution and simple adaptation to another species?',
            'back': 'COEVOLUTION requires RECIPROCAL evolutionary change: species A adapts to species B, AND species B adapts to species A in response. Each species acts as a selective force on the other. SIMPLE ADAPTATION occurs when one species evolves to use another as a resource without that other species evolving in response — e.g., a generalist herbivore that eats many plants doesn\'t significantly affect any single plant\'s evolution. True coevolution is most visible in tightly coupled pairs: predator-prey arms races (newt/snake TTX), mutualisms (fig/fig wasp), parasite-host (Red Queen dynamics). The key test: did the second species evolve specifically in response to the first?',
        },
        quiz=[
            {
                'question': 'Which of these best illustrates true coevolution?',
                'correct': 'The garter snake and rough-skinned newt, where newts evolved TTX toxicity and snakes evolved TTX resistance in tight reciprocal fashion',
                'distractors': [
                    'A deer eating tree leaves',
                    'A bird building a nest in a tree',
                    'Humans domesticating dogs over 15,000 years',
                ],
            },
            {
                'question': 'A generalist herbivore (like a rabbit) eats many different plant species. A specialist moth caterpillar eats only ONE plant genus. Which species is expected to participate in tighter coevolution with its host plant, and why?',
                'correct': 'The specialist moth — because its entire reproductive fitness depends on that single plant genus, each selective pressure from the plant is concentrated on the moth population; the plant in turn is under intense selection from the moth and evolves defenses specifically targeting it',
                'distractors': [
                    'The generalist rabbit — because it eats more plant species, it exerts stronger total selective pressure on the plant community as a whole, causing more plants to evolve defenses and driving faster plant diversification',
                    'Both are equally likely to coevolve — the intensity of coevolution depends only on population size and generation time, not on dietary specialization. Rabbits with larger populations drive stronger coevolution even if they eat many plants',
                    'Neither is likely to coevolve tightly because coevolution only occurs in aquatic environments where parasites and hosts have sufficiently high contact rates — terrestrial herbivore-plant interactions are too slow and diffuse for measurable reciprocal evolution',
                ],
            },
            {
                'question': 'The geographic mosaic theory of coevolution (Thompson) states that coevolution varies by location. In a "hotspot" population, both the newt and snake show extreme traits (very toxic, very resistant). In a "coldspot" population, both are relatively mild. What maintains this geographic variation rather than one level becoming universal?',
                'correct': 'Local ecological conditions determine whether the coevolutionary interaction is intense — food web composition, population densities, alternative prey/predators, and local selection pressures differ by location; gene flow between hotspots and coldspots slows but does not eliminate geographic variation',
                'distractors': [
                    'Geographic variation is maintained by genetic drift — hotspot populations are small and drift to high toxicity/resistance by chance, while coldspot populations drift to low values; there is no selective explanation for the pattern',
                    'The geographic mosaic is maintained by frequency-dependent selection — as the newt becomes highly toxic in a population, selection for resistance in snakes reaches a maximum; above a threshold toxicity level, selection for further resistance DECREASES, stabilizing the interaction at different levels in different locations',
                    'Geographic variation is an artifact of incomplete sampling — if enough years of data were collected from each location, all populations would converge on the same intermediate toxicity and resistance values at evolutionary equilibrium',
                ],
            },
            {
                'question': 'A student claims: "Coevolution always leads to arms races, and arms races always lead to extinction of one species." Identify BOTH errors in this statement.',
                'correct': 'First, not all coevolution is antagonistic — mutualistic coevolution (pollinator-flower) benefits both species and does not produce arms races. Second, arms races are self-limiting because costs on both sides prevent infinite escalation; the TTX-resistant snake example shows both species persisting despite decades of arms-race coevolution',
                'distractors': [
                    'First, coevolution cannot cause extinction because natural selection always produces adaptation — if one species were being driven to extinction, selection would produce a new adaptation before the species disappeared. Second, arms races always end in a stable equilibrium, not extinction',
                    'First, coevolution only occurs between parasites and hosts — it does not occur between predators and prey or between mutualistic species. Second, arms races do lead to extinction of the weaker species because selection cannot be reciprocal; the species with shorter generation time always wins',
                    'There is only one error — the claim that arms races lead to extinction is wrong. The claim that coevolution always leads to arms races is actually correct: even mutualistic interactions involve reciprocal evolutionary change in which each partner pushes the other toward higher investment levels',
                ],
            },
            {
                'question': 'Which of the following is a COMMENSAL interaction rather than coevolution?',
                'correct': 'Cattle egrets following cattle to catch insects stirred up by the grazing — the birds benefit but the cattle are essentially unaffected, and neither species has driven evolutionary change in the other',
                'distractors': [
                    'Garter snakes evolving TTX resistance while newts evolve higher TTX levels — both species are reciprocally changing',
                    'Figs and fig wasps coevolving matching flower and ovipositor structures — both species depend on each other for reproduction',
                    'Cleaner fish and their client fish — both species have evolved specific cues and behaviors for the relationship',
                ],
            },
            {
                'question': 'The statement "generalists coevolve weakly" is central to coevolution theory. What is the mechanistic reason?',
                'correct': 'A generalist predator spreads its selective pressure across many prey species, so no single prey species experiences strong enough selection from that predator to drive reciprocal evolution; the selective force is diluted across the generalist\'s diet',
                'distractors': [
                    'Generalist species have lower genetic variation than specialists, so they cannot respond to selective pressures from their prey',
                    'Generalist predators are always larger than specialists, and larger species evolve more slowly due to longer generation times',
                    'Generalists are always mutualists rather than antagonists, so coevolution cannot involve them by definition',
                ],
            },
            {
                'question': 'A biologist observes that oak trees evolved thicker acorn shells over the past 50,000 years while acorn weevils evolved longer ovipositors. The biologist calls this "diffuse coevolution." How does diffuse coevolution differ from specific coevolution?',
                'correct': 'Diffuse coevolution occurs when selection comes from many species simultaneously (multiple weevil species, multiple seed predators) rather than from a single pairwise interaction — the evolutionary response is shaped by the community rather than by a single partner',
                'distractors': [
                    'Diffuse coevolution is a misnomer — all coevolution is pairwise, and any "community-level" effects are simply the sum of independent pairwise interactions',
                    'Diffuse coevolution refers to coevolution that occurs over very large geographic scales, while specific coevolution occurs locally — the scale is geographic, not ecological',
                    'Diffuse coevolution is slower than specific coevolution because multiple species dilute the selective pressure, making measurable evolution take ten times longer',
                ],
            },
            {
                'question': 'Humans domesticated dogs over 15,000 years. Is this an example of coevolution?',
                'correct': 'Yes, it is coevolution — both species reciprocally adapted to each other: dogs evolved traits like digesting starch and reading human social cues, while humans evolved behaviors and cultural practices that accommodated dogs',
                'distractors': [
                    'No, because humans are the only species that changed — dogs are simply tame wolves with no genetic differences from their ancestors',
                    'No, because coevolution requires wild species interacting naturally — domestication is artificial selection and does not count as coevolution by definition',
                    'No, because 15,000 years is too short a timescale for any measurable evolutionary change to occur in either species',
                ],
            },
            {
                'question': 'L1 RECALL: What three requirements must be met for coevolution to occur between two species?',
                'correct': '(1) Close ecological interaction between the species; (2) heritable variation in interacting traits in BOTH species; (3) fitness effects on BOTH species. All three are needed — without any one, selection cannot drive reciprocal evolutionary change',
                'distractors': [
                    'Geographic overlap, similar body size, and shared habitat — these three ecological requirements must all be met',
                    'Coevolution requires common ancestry — the two species must have diverged from the same recent ancestor to share enough genetic machinery for reciprocal evolution',
                    'Coevolution requires only a single generation of interaction — any species pair that interacts in one generation will begin coevolving immediately',
                ],
            },
            {
                'question': 'L2 COMPREHENSION: Which of the following lists the three main categories of coevolutionary outcome?',
                'correct': 'Mutualism (both species benefit), commensalism (one benefits, other unaffected), and antagonism (one benefits at the cost of the other)',
                'distractors': [
                    'Gradualism, punctuated equilibrium, and stasis',
                    'Geographic, sympatric, and parapatric',
                    'Directional, stabilizing, and disruptive',
                ],
            },
            {
                'question': 'L5 SYNTHESIS: A plant community contains 30 herb species and 10 herbivore species. A new pathogen arrives that infects 2 of the herbs. Predict which type of coevolution (tight/specific vs. diffuse) will dominate for (a) the herbs and herbivores, and (b) the herbs and the pathogen. Justify using the reciprocal-evolution and selective-pressure-concentration principles.',
                'correct': '(a) HERBIVORES × HERBS: diffuse coevolution — with many species on each side, selection from any one herbivore is spread across many herbs (and vice versa), weakening reciprocal change. (b) HERBS × PATHOGEN: tight/specific coevolution between pathogen and the two specific host herbs — selection from the pathogen is concentrated on just two species (driving strong selection for resistance) and the pathogen experiences strong selection from those two hosts\' defenses. Specificity concentrates reciprocal selection',
                'distractors': [
                    'Both relationships will be tight/specific because all species interactions involve pairwise selection regardless of community composition',
                    'Both relationships will be diffuse because any ecological interaction involving more than one species on either side dilutes selective pressure',
                    'Neither relationship qualifies as coevolution because coevolution requires populations of identical size and generation time',
                ],
            },
        ],
        visual={
            'type': 'interaction',
            'description': 'Types of species interactions',
            'regions': [
                {'label': 'Antagonistic', 'color': '#ff6b6b', 'items': ['Predator/prey', 'Parasite/host', 'Arms race']},
                {'label': 'Mutualistic', 'color': '#7de2d1', 'items': ['Pollinator/flower', 'Gut microbe/host', 'Cleaner fish/client']},
                {'label': 'Commensal', 'color': '#6e6a80', 'items': ['One benefits', 'Other unaffected']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Antagonistic, Mutualistic, Commensal.',
            'trap': 'Not all species interactions are coevolutionary. Coevolution requires RECIPROCAL evolution — both sides respond to each other.',
        },
    ))
    nodes.append(build_node(
        id='lec9-antagonistic-arms',
        title='Antagonistic Coevolution & Arms Races',
        subtitle='Garter snake vs newt + geographic mosaic (Lec 9 slides 6-16)',
        color='red', row=8,
        heading='Lecture 9 — Antagonistic Coevolution',
        sections=[{'label': 'CORE CONCEPT', 'body': 'ANTAGONISTIC COEVOLUTION drives arms races via negative frequency-dependent selection. Predator and prey populations can oscillate like Lotka-Volterra models, and Cortez & Weitz (2014, PNAS) showed coevolutionary alternation of dominance between hosts and parasites. An ARMS RACE requires heritable variation on both sides and reciprocal selection. CLASSIC CASE: the garter snake × rough-skinned newt system. Rough-skinned newts (Taricha granulosa) produce TETRODOTOXIN (TTX), which blocks voltage-gated sodium channels and paralyzes most predators. Western garter snakes (Thamnophis sirtalis) have evolved TTX-RESISTANT sodium channels via point mutations in the Na+ channel gene — sometimes a single amino-acid substitution suffices. COSTS: non-resistant snakes move fast, resistant snakes move slow (ion-channel efficiency trade-off); highly toxic newts pay an energetic cost. TTX and resistance levels vary geographically — matching hotspots and coldspots. GEOGRAPHIC MOSAIC THEORY (John Thompson): hotspots of intense reciprocal selection + coldspots of weak selection + gene flow between them produces geographic variation in coevolutionary intensity.'}] + slides_to_sections(d, (6, 16)),
        examples=[
            'Rough-skinned newt (Taricha granulosa) produces tetrodotoxin (TTX) — powerful neurotoxin.',
            'Garter snake (Thamnophis sirtalis) evolved TTX-resistant sodium channels, can eat newts without dying.',
            'Both toxicity and resistance have COSTS: TTX-resistant snakes move slower; highly toxic newts are energetically expensive.',
            'Geographic mosaic theory (Thompson): coevolution is locally variable — some populations are coevolutionary "hotspots," others "coldspots."',
        ],
        warnings=[
            'Arms races are NOT infinitely escalating — costs on both sides limit escalation. TTX-resistant snakes move slower, which sets an upper limit on resistance evolution.',
            'Geographic mosaic does NOT mean coevolution fails in coldspots — intensity varies by local conditions. Gene flow between hotspots and coldspots can spread coevolutionary outcomes across the range.',
        ],
        mnemonic='Arms race: each side escalates + pays costs. Locally variable = mosaic.',
        flashcard={
            'front': 'Describe the garter snake / rough-skinned newt arms race and why it illustrates the costs of coevolutionary escalation.',
            'back': 'Rough-skinned newts (Taricha granulosa) produce TETRODOTOXIN (TTX), one of the most powerful neurotoxins known — it blocks voltage-gated sodium channels, causing paralysis and death in most predators. Garter snakes (Thamnophis sirtalis) in contact with toxic newts have evolved MUTATIONS IN THEIR Na+ CHANNEL GENES that prevent TTX binding — making them resistant. The snakes eat newts, and newts respond by becoming MORE toxic, driving further snake resistance — an escalating arms race. CRUCIALLY, BOTH SIDES PAY COSTS: (1) Resistant snakes have slower movement because their Na+ channels work less efficiently, (2) Highly toxic newts expend energy producing TTX. The geographic mosaic theory (Thompson) explains why coevolution varies by location — some populations are coevolutionary HOTSPOTS with extreme toxicity and resistance, while others are COLDSPOTS with little of either. The snake-newt system is a paradigmatic example of coevolution in action.',
        },
        quiz=[
            {
                'question': 'The garter snake/newt arms race demonstrates that coevolutionary escalation:',
                'correct': 'Carries fitness costs on both sides, because the traits that win the arms race come at a price',
                'distractors': [
                    'Always produces perfectly adapted species',
                    'Only occurs in laboratory conditions',
                    'Has no measurable impact on population fitness',
                ],
            },
            {
                'question': 'TTX-resistant garter snakes (Thamnophis sirtalis) in newt-free populations have LOWER resistance than snakes in populations with toxic newts. According to the arms race model, why don\'t all snake populations evolve maximum resistance?',
                'correct': 'TTX resistance carries a locomotion cost — resistant Na+ channels conduct ions less efficiently, making resistant snakes slower. In newt-free populations the cost outweighs the benefit, so selection removes resistance alleles; only where newts are present does the benefit exceed the locomotion cost',
                'distractors': [
                    'All snake populations evolve maximum resistance within a few generations — it is the newts that limit the arms race by being unable to evolve TTX concentrations higher than a physiological maximum, not locomotion costs in snakes',
                    'TTX resistance alleles are maintained in all populations at low frequency by mutation-selection balance regardless of whether newts are present — the variation seen between populations simply reflects recent colonization rather than ongoing local adaptation',
                    'In newt-free populations, resistance alleles drift to fixation or loss randomly — the between-population variation in resistance is entirely due to genetic drift because selection for or against resistance is neutral when newts are absent',
                ],
            },
            {
                'question': 'A researcher compares snake TTX resistance and newt TTX levels across 20 populations spanning from Oregon to California. She finds that three populations have extremely high resistance AND extremely high toxicity (hotspots), while 17 populations have low-low (coldspots). Which observation would MOST strongly confirm the geographic mosaic theory?',
                'correct': 'That the hotspot and coldspot populations show genetic differentiation at resistance/toxicity loci DESPITE gene flow between them — indicating that local selection is strong enough to maintain the geographic structure against homogenizing gene flow',
                'distractors': [
                    'That all 20 populations show the same resistance-to-toxicity ratio — this would confirm the geographic mosaic theory because it shows a stable evolutionary equilibrium maintained uniformly across the entire range',
                    'That the hotspot populations are geographically isolated from coldspot populations with no gene flow — geographic isolation is required for the mosaic to develop; shared gene flow would blend the populations into a single intermediate phenotype',
                    'That hotspot populations have higher snake population densities than coldspot populations — the mosaic is driven by population size rather than ecological factors, because larger populations can maintain more genetic variation for resistance and toxicity simultaneously',
                ],
            },
            {
                'question': 'TTX blocks voltage-gated sodium channels (Na+) throughout the nervous system, causing paralysis. Garter snakes evolved resistance via mutations in their Na+ channel GENE (not by producing a TTX-neutralizing enzyme). Why is this molecular mechanism particularly informative for evolutionary biology?',
                'correct': 'It shows that resistance evolved at the SPECIFIC molecular target of the toxin — the same gene encoding the protein that TTX binds to was modified to prevent binding. This is direct evidence that selection acts at the molecular level on the exact protein-toxin interaction, tracing the evolutionary arms race to specific amino acid substitutions in the Na+ channel',
                'distractors': [
                    'The Na+ channel mechanism is less informative than an enzyme-based resistance would be, because enzyme evolution involves gene duplication and neofunctionalization while channel mutation is a simpler single-amino-acid change that tells us nothing about the molecular mechanism of arms races',
                    'Na+ channel mutations are uniquely informative because they prove Lamarckian inheritance — individual snakes exposed to TTX during their lifetime must have developed Na+ channel mutations that were then passed to offspring, which is the only way the resistance could have evolved so precisely',
                    'The Na+ channel mechanism proves that TTX resistance is a spandrel (byproduct) rather than a direct adaptation — the channel mutations were originally selected for other reasons (e.g., better cold-temperature nerve function) and the TTX resistance is an incidental byproduct that happened to be useful when snakes encountered newts',
                ],
            },
            {
                'question': 'What is the scientific (Latin) name of the rough-skinned newt and the garter snake in the classic TTX arms race?',
                'correct': 'Taricha granulosa (newt) and Thamnophis sirtalis (garter snake) — this pair has been the subject of decades of coevolutionary research',
                'distractors': [
                    'Triturus cristatus (newt) and Thamnophis elegans (snake) — European crested newts are the iconic TTX producers',
                    'Notophthalmus viridescens (newt) and Nerodia sipedon (snake) — eastern red-spotted newts and northern water snakes',
                    'Ambystoma tigrinum (salamander) and Crotalus horridus (rattlesnake) — tiger salamanders and timber rattlesnakes',
                ],
            },
            {
                'question': 'TTX is produced not by the newt itself but by symbiotic bacteria in some species. If this is also true for Taricha, how does it affect the interpretation of the arms race?',
                'correct': 'If TTX is bacterial in origin, the newt\'s "evolution of higher toxicity" may involve evolving to tolerate and concentrate more TTX from symbionts — the fundamental reciprocal dynamic still holds because the snake experiences higher toxin dose either way, but the genetic target of selection in the newt is different',
                'distractors': [
                    'If TTX is bacterial, then the arms race is not coevolution at all — it is a three-way interaction that cannot be analyzed with pairwise coevolution models',
                    'Bacterial production would completely falsify the coevolution interpretation — the snake cannot be coevolving with a bacterium and a newt simultaneously',
                    'The bacterial origin means the newt has no evolutionary response capability, so the arms race reduces to the snake simply evolving resistance without the newt changing',
                ],
            },
            {
                'question': 'John Thompson proposed the "geographic mosaic theory" of coevolution. What is the key insight of this theory compared to earlier coevolution models?',
                'correct': 'Coevolutionary outcomes vary across space — hotspots of intense reciprocal selection exist alongside coldspots of weak or no selection, and gene flow between them, combined with local selection differences, maintains a dynamic geographic mosaic rather than a single uniform outcome',
                'distractors': [
                    'Coevolution occurs faster in the tropics than at temperate latitudes because of higher species diversity and shorter generation times — the mosaic is simply a latitudinal gradient',
                    'The mosaic theory holds that coevolution always proceeds through geographic isolation followed by sympatric fusion — each coevolved trait originates in allopatry',
                    'Coevolution is driven primarily by vicariance events (continental drift, river formation) that separate populations, and the mosaic pattern results from these ancient separations',
                ],
            },
            {
                'question': 'A classic prediction of arms-race theory is that extreme trait values should be COSTLY. Which observation about the snake-newt system best confirms this cost prediction?',
                'correct': 'Highly TTX-resistant snakes crawl more slowly than non-resistant snakes — this locomotion cost is a direct trade-off of the Na+ channel mutations, demonstrating that resistance comes at a measurable fitness cost',
                'distractors': [
                    'Highly resistant snakes have larger testes than non-resistant ones, suggesting they redirect energy from reproduction to resistance',
                    'Highly toxic newts live shorter lives than less toxic newts due to self-poisoning from their own TTX',
                    'Highly resistant snakes produce fewer offspring because Na+ channel mutations reduce embryonic development rate',
                ],
            },
            {
                'question': 'L1 RECALL: Who proposed the Geographic Mosaic Theory of coevolution?',
                'correct': 'John N. Thompson — his theory emphasizes that coevolution varies geographically with hotspots and coldspots connected by gene flow',
                'distractors': [
                    'Paul Ehrlich and Peter Raven — proposers of the mosaic theory in their 1964 paper on plant-butterfly coevolution',
                    'Leigh Van Valen — author of the Red Queen hypothesis, which is synonymous with the geographic mosaic',
                    'Edward Brodie Jr. and Edmund Brodie III — the newt-snake researchers first proposed the mosaic theory',
                ],
            },
            {
                'question': 'L1 RECALL: Tetrodotoxin (TTX) works at what specific molecular target?',
                'correct': 'Voltage-gated sodium (Na+) channels — TTX binds to the outer pore and blocks Na+ influx, preventing nerve action potentials and causing paralysis',
                'distractors': [
                    'Voltage-gated potassium (K+) channels — TTX blocks K+ efflux',
                    'GABA receptors — TTX acts as a GABA antagonist',
                    'Acetylcholine receptors — TTX prevents muscle contraction by blocking ACh binding',
                ],
            },
            {
                'question': 'L4 ANALYSIS: Cortez & Weitz (2014, PNAS) described "coevolutionary alternation" between hosts and parasites. How does this extend simple arms race theory?',
                'correct': 'Instead of monotonic escalation (both sides always getting more extreme), coevolutionary alternation describes oscillating dynamics where host and parasite dominance ALTERNATES over time — similar to Lotka-Volterra predator-prey cycles but driven by reciprocal genetic change rather than demographic feedback alone',
                'distractors': [
                    'Coevolutionary alternation means the two species alternate which one evolves in any given generation — only one species changes at a time',
                    'Coevolutionary alternation refers to geographic alternation between hotspots — it is a synonym for the mosaic theory',
                    'Cortez & Weitz showed that arms races always end in alternating extinction of host and parasite',
                ],
            },
            {
                'question': 'L5 SYNTHESIS: Consider the garter snake × newt TTX arms race. Explain why this system does NOT evolve toward infinite escalation, integrating (a) the cost of resistance, (b) the cost of toxicity, (c) the geographic mosaic, and (d) Lotka-Volterra-like population dynamics.',
                'correct': '(a) Resistant snakes move slower due to altered Na+ channel efficiency, imposing a locomotion cost that sets a ceiling on resistance. (b) Toxic newts pay an energetic cost producing TTX, capping toxicity evolution. (c) The geographic mosaic means different populations reach different equilibrium levels based on local conditions — hotspots see extreme values, coldspots see mild values. (d) Population-level oscillations (predator suppression → prey recovery → predator recovery) prevent any lineage from running away to infinity because population crashes interrupt directional selection. Together these produce a bounded, locally-variable, oscillating arms race rather than monotonic escalation',
                'distractors': [
                    'The arms race does not escalate because both species lack the genetic variation needed for further evolution — all TTX and resistance alleles have been fixed long ago',
                    'The arms race has ended because the snake won completely — TTX no longer poses any fitness cost to snakes, so newts stopped evolving toxicity',
                    'The arms race continues to infinity in principle but has been artificially limited by human conservation interventions that prevent further escalation',
                ],
            },
        ],
        visual={
            'type': 'arms-race',
            'description': 'Snake-newt reciprocal evolution',
            'regions': [
                {'label': 'Newt', 'color': '#ff6b6b', 'items': ['TTX toxin', 'More toxic over time', 'Energetic cost']},
                {'label': 'Snake', 'color': '#4ea8de', 'items': ['Na+ channel mutations', 'More resistant over time', 'Slower movement cost']},
                {'label': 'Mosaic', 'color': '#ffc857', 'items': ['Hotspots: high escalation', 'Coldspots: weak escalation', 'Varies by geography']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Poison + Resistance + Costs + Mosaic.',
            'trap': 'Arms races are not infinitely escalating — costs constrain how far escalation can go.',
        },
    diagram=garter_snake_newt_arms_race_diagram(),
    ))
    nodes.append(build_node(
        id='lec9-mutualistic',
        title='Mutualistic Coevolution',
        subtitle='Flowers, pollinators, and mutual benefit (Lec 9 slides 17-20)',
        color='pink', row=8,
        heading='Lecture 9 — Mutualistic Coevolution',
        sections=[{'label': 'CORE CONCEPT', 'body': 'MUTUALISTIC COEVOLUTION is driven by positive frequency-dependent selection — both species gain fitness from the interaction, so alleles favoring cooperation spread in both. Classic example: the South African fly Prosoeca ganglbaueri pollinates Zaluzianskya microsiphon (a flower with a deep tube), and the two have coevolved matching proboscis and tube lengths. DARWIN\'S ORCHID PREDICTION (1862): examining a Madagascar orchid (Angraecum sesquipedale) with a 28–30 cm nectary spur, Darwin predicted a moth with a matching long proboscis must exist. The moth Xanthopan morganii praedicta was discovered and confirmed in 1903 — 40+ years AFTER Darwin made the prediction (and over 20 years after Darwin died in 1882). MUTUALISMS CAN BREAK DOWN INTO PARASITISM via cheating (one species takes reward without providing benefit). Stability depends on policing, partner choice, or sanctions against cheaters.'}] + slides_to_sections(d, (17, 20)),
        examples=[
            'Mutualisms: both species benefit from the interaction.',
            'Specialized fly pollinators and matching flowers — e.g., long-tongued flies and long-spurred orchids coevolved.',
            'Darwin\'s prediction: seeing a Madagascar orchid with a 30 cm nectary, Darwin predicted a moth with a matching 30 cm proboscis existed — confirmed 40 years later (Xanthopan morganii praedicta).',
        ],
        warnings=[
            'Darwin predicted the moth in 1862 and it was confirmed in 1903 — 40+ years AFTER Darwin died in 1882. Darwin did NOT confirm his own prediction.',
            'Mutualisms can evolve into antagonistic relationships if one species begins to cheat (take reward without providing benefit). Stability depends on partner choice and sanctions.',
        ],
        mnemonic='Mutual benefit = coevolution with reward not punishment.',
        flashcard={
            'front': 'Give an example of mutualistic coevolution where a specific prediction was made and later confirmed.',
            'back': 'DARWIN\'S MADAGASCAR ORCHID PREDICTION: In 1862, Darwin examined a Madagascar orchid (Angraecum sesquipedale) with an unusually long nectary spur — 28-30 cm. He predicted that a pollinator with a matching 25-30 cm proboscis must exist, even though none was known at the time, because the orchid\'s nectar would otherwise be inaccessible. This was a bold prediction from coevolutionary theory. FORTY YEARS LATER (1903), after Darwin\'s death, the moth Xanthopan morganii praedicta (the "predicted" one) was discovered with exactly that proboscis length. This is a textbook case of a successful evolutionary prediction — and it demonstrated that coevolution can produce matching morphologies without either species having to "know" what the other is doing.',
        },
        quiz=[
            {
                'question': 'Darwin predicted the existence of a Madagascar moth with a 25+ cm proboscis based on what observation?',
                'correct': 'A Madagascar orchid with a nectary 28-30 cm long that no known pollinator could reach',
                'distractors': [
                    'Fossil evidence of ancient moths',
                    'DNA analysis of modern moths',
                    'Direct observation of pollination',
                ],
            },
            {
                'question': 'Darwin\'s Madagascar moth prediction is often cited as an example of evolutionary theory making TESTABLE PREDICTIONS. Why is this a particularly strong illustration of good science?',
                'correct': 'The prediction was specific (a moth with ~30 cm proboscis in Madagascar), falsifiable (if no such moth existed, the coevolution framework would be challenged), and confirmed independently 40 years later — showing that evolutionary theory has predictive power beyond explaining already-known facts',
                'distractors': [
                    'The prediction was strong because Darwin made it before the orchid was discovered — predicting a plant\'s nectary length from a moth\'s proboscis length is a more impressive demonstration of theory than predicting a moth\'s proboscis from a plant\'s nectary',
                    'It is a strong illustration because Darwin was wrong about the moth\'s exact size (he predicted 25 cm but the moth has 30 cm) — this partial inaccuracy shows that science accepts approximate predictions, making evolutionary theory more falsifiable than an exact prediction would be',
                    'The prediction illustrates deductive reasoning: given that the orchid nectary is 30 cm, a moth with 30 cm proboscis MUST exist by logical necessity. This is not a prediction but a mathematical certainty derivable from the rules of natural selection without any empirical uncertainty',
                ],
            },
            {
                'question': 'Mutualisms can break down if one partner begins to "cheat" — taking resources without providing benefit. In the orchid-moth mutualism, what kind of "cheating" would threaten the mutualism, and what would prevent the stable mutualism from collapsing?',
                'correct': 'An orchid that mimics the long-spurred shape but produces no nectar would still be pollinated by moths that arrive expecting nectar, without paying the cost of nectar production — but if most orchids cheated, moths would learn to avoid all long-spurred orchids and the whole mutualism would collapse; the mutualism is stabilized as long as honest nectar producers are more common than cheaters',
                'distractors': [
                    'The moth could cheat by developing a shorter proboscis that accesses nectar from other flower species — but since nectary length and proboscis length are perfectly matched, a shorter proboscis would cause the moth to fail to pollinate the orchid, immediately collapsing the mutualism from the moth side',
                    'Cheating cannot occur in obligate mutualisms like this one — because neither species can survive without the other, selection permanently prevents any individual from defecting; obligate mutualisms are the most evolutionarily stable interactions known',
                    'The mutualism is maintained by kin selection: each individual moth helps pollinate the orchid because the seeds will grow near the same orchid the moth\'s offspring will need to visit, so there is indirect fitness benefit to honest pollination that prevents cheating from spreading',
                ],
            },
            {
                'question': 'Some orchid species in Europe MIMIC the appearance of female bees and wasps to attract male pollinators (sexual deception). These orchids provide NO nectar. What category of coevolution does this represent, and how is it maintained despite the lack of reward?',
                'correct': 'This is a form of Batesian mimicry applied to mutualism — the orchid is a "cheater" that exploits the pre-existing mating drive of male bees without offering a benefit. It is maintained because the bee population cannot evolve perfect discrimination fast enough, especially since orchids are rare relative to real females and males make occasional mistakes',
                'distractors': [
                    'This is Müllerian mimicry — the orchid and the female bee both benefit from resembling each other because it reduces the amount of time male bees spend inspecting flowers, lowering the orchid\'s energy spent on floral display',
                    'This represents antagonistic coevolution — the orchid is evolving to reduce pollinator choice while the bee is evolving to avoid being deceived. Over time, the arms race between bee discrimination and orchid deception accuracy will drive both to extinction',
                    'Sexual deception orchids represent a mutualism because the male bee receives practice for mating behavior by interacting with the orchid — this behavioral training increases the male\'s reproductive success, making the interaction mutualistic despite the lack of nectar reward',
                ],
            },
            {
                'question': 'In what year was Darwin\'s Madagascar moth prediction finally confirmed by the discovery of Xanthopan morganii praedicta?',
                'correct': '1903 — approximately 40 years after Darwin\'s 1862 prediction and more than 20 years after Darwin\'s death in 1882',
                'distractors': [
                    '1862 — Darwin confirmed his own prediction the same year he made it, after a specimen was shipped from Madagascar',
                    '1882 — the moth was discovered in the year Darwin died, providing him with final validation',
                    '1950 — confirmation came only after modern insect collecting expeditions, a full century after the prediction',
                ],
            },
            {
                'question': 'What is the name of the Madagascar orchid that prompted Darwin\'s famous moth prediction?',
                'correct': 'Angraecum sesquipedale — a Madagascar orchid with a 28-30 cm nectary spur that Darwin examined in 1862',
                'distractors': [
                    'Ophrys apifera — the bee orchid, which mimics female bees to attract male pollinators',
                    'Angraecum eburneum — a smaller-flowered relative without the extreme nectary length',
                    'Xanthopan angraeci — the scientific name of the orchid is taken from its matching moth',
                ],
            },
            {
                'question': 'A fig wasp enters a fig flower, lays eggs, and pollinates the fig in the process. The wasp larvae develop inside the fig and emerge as adults. What features of this relationship make it an OBLIGATE mutualism, and what does this imply about extinction risk?',
                'correct': 'Neither species can reproduce without the other — figs cannot be pollinated by any other pollinator, and fig wasps cannot develop in any other host plant. This obligate dependency means extinction of one species immediately causes extinction of the other, making obligate mutualisms particularly vulnerable to ecological disruption',
                'distractors': [
                    'Obligate mutualisms are the most evolutionarily stable interactions known because natural selection prevents extinction of either partner; if one partner becomes threatened, selection automatically rescues the other',
                    'Fig-wasp mutualism is facultative, not obligate — both species can survive independently but prefer to interact when both are present',
                    'Obligate mutualisms increase extinction risk by reducing genetic diversity — because partners must precisely match each other, both species evolve toward fixation of single alleles, eliminating variation needed to survive environmental change',
                ],
            },
            {
                'question': 'Cheaters can destabilize mutualisms. Which mechanism prevents cheater invasion in many stable mutualisms?',
                'correct': 'Partner choice and sanctions — legitimate partners recognize cheaters and either refuse to interact (partner choice) or punish them by withholding resources (sanctions), as seen in yucca moth / yucca plant mutualisms where plants abort fruits containing too many moth larvae',
                'distractors': [
                    'Cheater invasion is prevented by species-specific chemical signals that cheaters cannot replicate — no known cheater has ever been able to mimic the chemical signals required for partner recognition',
                    'Cheaters are prevented by high mutation rates at the recognition loci — constantly changing signal sequences make cheating impossible on evolutionary timescales',
                    'Cheaters cannot evolve because mutualisms are the most primitive form of interaction — ancestral species always fully cooperated, and cheating is a modern human-induced phenomenon',
                ],
            },
            {
                'question': 'L1 RECALL: Name the South African fly and the flower species cited in the lecture as a textbook case of matching long-tongue / long-tube coevolution.',
                'correct': 'Prosoeca ganglbaueri (the long-tongued fly) and Zaluzianskya microsiphon (the deep-tubed flower) — a classic example of tight mutualistic coevolution in South Africa',
                'distractors': [
                    'Xanthopan morganii praedicta and Angraecum sesquipedale — the Darwin Madagascar case, but this is a moth, not a fly',
                    'Bombus terrestris and Trifolium pratense — the common bumblebee and red clover',
                    'Apis mellifera and Helianthus annuus — the honeybee and sunflower',
                ],
            },
            {
                'question': 'L1 RECALL: In which year did Darwin die, and in which year was Xanthopan morganii praedicta finally confirmed?',
                'correct': 'Darwin died in 1882; Xanthopan morganii praedicta was confirmed in 1903 — meaning the moth was discovered more than 20 years after Darwin\'s death, and 41 years after his 1862 prediction',
                'distractors': [
                    'Darwin died in 1903; the moth was confirmed in 1862 — Darwin made the prediction and died before it was verified',
                    'Darwin died in 1862; the moth was confirmed in 1882 — the same year the prediction was made',
                    'Darwin died in 1859; the moth was discovered in 1870 — Darwin lived to see his prediction confirmed',
                ],
            },
            {
                'question': 'L4 ANALYSIS: Mutualisms driven by positive frequency-dependent selection differ mechanistically from antagonistic coevolution driven by negative frequency-dependent selection. Why does positive frequency-dependence tend to stabilize mutualisms rather than destabilize them?',
                'correct': 'In positive frequency-dependence, the fitness of a cooperative genotype INCREASES as its partner\'s cooperative genotypes become more common — both species mutually reinforce cooperation until a stable equilibrium of mutual benefit is reached. In negative frequency-dependence (antagonism), rare variants are favored, driving constant turnover and escalation rather than stable equilibrium',
                'distractors': [
                    'Positive frequency-dependence destabilizes mutualisms because it drives cheater invasion — any rare cheater gains the mutualistic reward without the cost',
                    'Positive and negative frequency-dependence have identical effects on mutualism — both lead to cycling between cooperation and defection',
                    'Frequency-dependence plays no role in mutualism — mutualisms are maintained entirely by mutual benefit regardless of genotype frequency',
                ],
            },
            {
                'question': 'L5 SYNTHESIS: Darwin\'s orchid-moth prediction is often presented as the "perfect prediction" in evolutionary biology. Evaluate why this case qualifies as a Popperian falsifiable prediction and integrate the historical timeline (1862 prediction → 1882 Darwin death → 1903 moth discovery) with the logical structure of coevolutionary reasoning.',
                'correct': 'Darwin\'s prediction satisfies Popperian falsifiability: (1) It was specific — a moth with a proboscis of at least ~25-30 cm in Madagascar. (2) It was risky — if no such moth existed after sufficient searching, the mutualism/coevolution framework predicting obligate long-tongued pollinators would be challenged. (3) It was confirmed INDEPENDENTLY by researchers (1903) who were not the predictor — and crucially 21 years after Darwin\'s 1882 death, preventing any possibility of confirmation bias by the predictor. (4) The logic was deductive: obligate nectar reward at extreme depth requires an obligate long-proboscis pollinator; absence of such a pollinator would mean the orchid\'s nectary serves a non-pollination function or Darwin\'s mutualism theory needs revision',
                'distractors': [
                    'The prediction is not really Popperian because coevolution theory could have accommodated any result — Darwin could have explained either the presence or absence of the moth by different ad hoc mechanisms',
                    'The prediction fails Popperian standards because Darwin waited 40 years for the result — only predictions confirmed within the predictor\'s lifetime are scientifically valid',
                    'The prediction is not falsifiable at all because orchids and moths are natural products — Popperian falsifiability applies only to laboratory experiments',
                ],
            },
        ],
        visual={
            'type': 'match',
            'description': 'Mutualistic morphological matching',
            'regions': [
                {'label': 'Orchid', 'color': '#7de2d1', 'items': ['Long nectar spur', '28-30 cm']},
                {'label': 'Moth', 'color': '#ffc857', 'items': ['Long proboscis', '25-30 cm match']},
                {'label': 'Benefit', 'color': '#4ea8de', 'items': ['Pollen transfer', 'Nectar reward']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Length matches length. Darwin predicted, nature confirmed.',
            'trap': 'Many mutualisms can break down if one partner evolves to cheat — obligate mutualisms can be vulnerable.',
        },
    ))
    nodes.append(build_node(
        id='lec9-mimicry',
        title='Mullerian & Batesian Mimicry',
        subtitle='Signal evolution under predator selection (Lec 9 slides 21-29)',
        color='coral', row=8,
        heading='Lecture 9 — Mimicry',
        sections=[{'label': 'CORE CONCEPT', 'body': 'MÜLLERIAN MIMICRY: several HARMFUL species resemble each other, sharing a common warning signal. Mutual benefit — predators learn the shared signal faster and fewer individuals of each mimicking species are sampled during predator learning. This is CONVERGENT evolution driven by aposematic signaling. Classic examples: Heliconius butterflies in the Neotropics (many toxic species share wing patterns) and coral snakes. Proposed by Fritz Müller (1821–1897). BATESIAN MIMICRY: a HARMLESS species mimics a HARMFUL model. Benefits the mimic (escaping predation by bluffing) at a COST to the model (predators occasionally test the pattern and may not encounter a real toxic model). Example: millipede Brachoria mimics Apheloria (cyanide-producing). Proposed by Henry Bates (1825–1892). APOSEMATISM = warning coloration. FREQUENCY-DEPENDENCE: rare Batesian mimics are protected, but if mimics become too common, predators sample the pattern more, learn it is usually safe, and the toxic model suffers attacks → a coevolutionary chase where the model may evolve a new pattern. NZ TŪĪ bird example of deceptive pollination. Bird-squirrel-crossbill-pine coevolution is another classic case.'}] + slides_to_sections(d, (21, 29)),
        examples=[
            'MÜLLERIAN mimicry: multiple UNPALATABLE/dangerous species converge on similar warning signals. Benefits both — predators learn faster. e.g., Heliconius butterflies, coral snakes.',
            'BATESIAN mimicry: a PALATABLE species mimics a dangerous/unpalatable model. Benefits only the mimic — cost to the model as predators sometimes attack (naive or if mimic becomes too common).',
            'Mimicry requires (1) a model, (2) a mimic, (3) a deceivable predator.',
            'Tūī bird (New Zealand): Some plants mimic flowers normally pollinated by tūīs to attract them.',
        ],
        warnings=[
            'Batesian mimicry is deceptive — if mimics become too common relative to the model, predators sample the pattern more often, learn it is often safe, and the deception breaks down.',
        ],
        mnemonic='Müllerian = Mutual (both toxic). Batesian = Bluffing (mimic is safe).',
        flashcard={
            'front': 'Compare Müllerian and Batesian mimicry. Which is a mutualism and which is a form of parasitism?',
            'back': 'MÜLLERIAN MIMICRY: Multiple UNPALATABLE/dangerous species converge on similar warning colorations (often bright red/yellow/black bands). All the mimicking species BENEFIT because predators only need to learn ONE aposematic signal to avoid all of them — pooling the "teaching cost" of predator learning across many species. This is a MUTUALISM: every species gains. Example: Heliconius butterflies in the Amazon, where many toxic species share similar wing patterns. BATESIAN MIMICRY: A PALATABLE species mimics an unpalatable model. Only the MIMIC benefits (escaping predation by bluffing); the MODEL pays a cost because naive or confused predators may attack mistaken individuals. This is a form of PARASITISM — the mimic exploits the model\'s honest signal. Example: some flies and moths resemble stinging bees or wasps despite being harmless. KEY DIFFERENCE: Müllerian = both defended, mutual. Batesian = one defended, one not, parasitic.',
        },
        quiz=[
            {
                'question': 'Two unrelated toxic butterfly species gradually evolve the same warning color pattern. This is:',
                'correct': 'Müllerian mimicry — mutually beneficial convergence on a shared warning signal',
                'distractors': [
                    'Batesian mimicry — one is palatable, one is not',
                    'Camouflage — both are trying to hide',
                    'Coincidental convergence with no fitness effect',
                ],
            },
            {
                'question': 'A predatory bird learns to avoid orange-and-black butterflies after eating one toxic Heliconius species. It then also avoids a second, slightly different-looking species. Over evolutionary time, a third Heliconius species in the same region is expected to:',
                'correct': 'Converge toward the orange-and-black pattern of the first two species (Müllerian mimicry), because the predator\'s avoidance learning is triggered by the shared signal — joining the mimicry ring reduces the total "teaching cost" spread across all participating species',
                'distractors': [
                    'Evolve away from the orange-and-black pattern to avoid being confused with the two already-recognized toxic species — predators learn to attack orange-and-black butterflies after experiencing one that turned out to be toxic, creating selection against the shared pattern',
                    'Remain unchanged — once two toxic species share a pattern, any third species joining would dilute the signal and confuse predators, making the three-species mimicry ring less effective than a two-species one and reducing selection to converge',
                    'Evolve toward a PALATABLE form that mimics the orange-and-black pattern (Batesian strategy) — since the pattern is well-established as a warning signal, it is more advantageous for the third species to be a palatable mimic than to pay the cost of toxin production',
                ],
            },
            {
                'question': 'In an area where Batesian mimics (palatable) outnumber their toxic model (in a 10:1 ratio), what evolutionary prediction would you make about predator behavior and mimic fitness?',
                'correct': 'Predators will sample the orange-and-black pattern more often, eventually discovering that it usually leads to a palatable prey — as predator avoidance of the pattern weakens, the mimic\'s protective benefit decreases, and selection may favor either a different mimic pattern or a return to the model species\' toxicity',
                'distractors': [
                    'At a 10:1 ratio, mimic fitness would be maximized because more mimics means more predator encounters with the pattern, reinforcing avoidance learning more quickly — high mimic frequency amplifies the signal rather than diluting it',
                    'The 10:1 ratio has no fitness effect on mimics because predators learn to avoid the pattern after encountering the first toxic model and never subsequently test the pattern again regardless of how many mimics exist',
                    'The 10:1 ratio would select for the model species to evolve a NEW warning pattern that the mimics have not yet copied, driving an evolutionary chase between model and mimic that maintains low mimic-to-model ratios over time',
                ],
            },
            {
                'question': 'Henry Bates observed in the Amazon that harmless flies often resembled stinging wasps. Fritz Müller later observed that multiple toxic butterfly species shared patterns. Both made evolutionary predictions — but HOW they reasoned was fundamentally different. Which statement BEST captures this difference?',
                'correct': 'Bates argued from ASYMMETRY (one palatable, one toxic = one benefits, one pays) — a prediction about natural selection; Müller argued from SYMMETRY (both toxic, both benefit from shared teaching cost) — a mathematical prediction about the probability of predator sampling being reduced for ALL members of a mimicry ring',
                'distractors': [
                    'Bates reasoned from MORPHOLOGY (similar appearance proves common ancestry) while Müller reasoned from ECOLOGY (shared habitat explains shared pattern regardless of ancestry) — illustrating a conflict between phylogenetic and ecological explanations for convergence',
                    'Bates made his predictions from direct field experiments removing mimics and testing predator response, while Müller relied entirely on theoretical mathematics — making Bates\'s work empirical and Müller\'s work purely theoretical',
                    'There is no fundamental difference in their reasoning — both Bates and Müller observed that similar patterns prevent predation and both predicted that natural selection would favor convergence on the pattern; they differed only in which species they studied',
                ],
            },
            {
                'question': 'Mimicry requires three components to function. Which three?',
                'correct': 'A model (honest dangerous/unpalatable signal source), a mimic (the imitator), and a deceivable predator (or receiver) capable of learning — without any one component, the mimicry cannot operate',
                'distractors': [
                    'A toxic plant, a herbivore, and a pollinator — this trio is required for any cross-trophic mimicry to evolve',
                    'A parent species, an offspring species, and environmental pressure — mimicry evolves through descent with modification in the offspring',
                    'Two model species and a single mimic — mimicry requires at least two honest signalers to establish the pattern',
                ],
            },
            {
                'question': 'Milk snakes (Lampropeltis) have red, yellow, and black bands similar to venomous coral snakes. Milk snakes are non-venomous. What is the specific type of mimicry here, and what is the main limitation of this system?',
                'correct': 'Batesian mimicry — milk snake is the palatable mimic, coral snake is the toxic model. The main limitation is that predators must survive encounters with coral snakes to learn the warning signal; since coral snake bites are often fatal, naive predators may not have the chance to learn, weakening the selective pressure maintaining the mimicry',
                'distractors': [
                    'Müllerian mimicry — both snakes are venomous but pool their teaching effect; milk snakes have mild venom that would still harm a predator',
                    'Camouflage — both snakes use their banding to hide among forest debris; predators never actually see the bands as warning signals',
                    'Aggressive mimicry — milk snakes use their coloration to attract prey rather than to deter predators, which is the reverse of Batesian deception',
                ],
            },
            {
                'question': 'Heliconius butterflies in Central and South America form large mimicry rings where many species share a common wing pattern. Genomic analysis shows they converged on these patterns through gene expression changes at a single locus (optix). What does this finding demonstrate about the molecular basis of mimicry evolution?',
                'correct': 'Major morphological convergence can be achieved through changes at a single regulatory gene — this is consistent with evo-devo principles that small regulatory changes produce large phenotypic effects, and also shows that independent species can find the same "genetic solution" to the same selective problem',
                'distractors': [
                    'Mimicry must involve many loci with small effects because wing patterns are too complex to be governed by a single gene — the optix finding must be experimental error',
                    'The optix finding proves that mimicry is Lamarckian — butterflies acquired similar wing patterns by behavioral learning and transmitted them to offspring as epigenetic modifications',
                    'Convergent mimicry proves all Heliconius species share a recent common ancestor with the same wing pattern — the optix gene is an ancestral trait, not a convergent adaptation',
                ],
            },
            {
                'question': 'A predator encountering a toxic butterfly for the first time must LEARN to associate the warning color with the bad taste. Why is this learning phase critical to aposematic (warning) signaling and mimicry?',
                'correct': 'Predator learning is the mechanism by which warning signals become effective — without learning, the warning color would provide no deterrent. Both Batesian and Müllerian mimicry depend entirely on predator learning, which is why patterns must be conspicuous and memorable',
                'distractors': [
                    'Predators are born knowing to avoid warning colors — learning is irrelevant because aposematic avoidance is instinctive and hardwired at birth',
                    'Learning only matters for mammals, which are long-lived enough to remember past experiences — birds and reptiles rely on innate color avoidance that does not require learning',
                    'Aposematic signals work through direct toxicity — the bright color warns predators by emitting a chemical signal detected by olfaction, not by visual learning',
                ],
            },
            {
                'question': 'L1 RECALL: Who proposed Müllerian mimicry, and what were his dates?',
                'correct': 'Fritz Müller (1821–1897) — a German naturalist who studied Brazilian butterflies and proposed that mutually toxic species benefit from sharing a warning signal',
                'distractors': [
                    'Henry Walter Bates (1825–1892) — Bates proposed Müllerian mimicry while in the Amazon',
                    'Alfred Russel Wallace (1823–1913) — co-discoverer of natural selection and of Müllerian mimicry',
                    'Charles Darwin (1809–1882) — Darwin first described Müllerian mimicry in his later editions of the Origin',
                ],
            },
            {
                'question': 'L1 RECALL: What millipede species is cited in the lecture as a Batesian mimic, and what is the toxic model species it resembles?',
                'correct': 'Brachoria (mimic) resembles Apheloria (model, a cyanide-producing millipede that releases hydrogen cyanide when threatened)',
                'distractors': [
                    'Narceus americanus (mimic) resembles Spirobolus (model, a rattlesnake-mimicking millipede)',
                    'Polydesmus (mimic) resembles Helix (model)',
                    'Sigmoria (mimic) resembles Limacus (model)',
                ],
            },
            {
                'question': 'L5 SYNTHESIS: A Batesian mimic population is initially rare (1 mimic : 100 models) and increases over time to 100 mimics : 1 model. Trace the step-by-step predicted evolutionary consequences for predators, mimics, and models, and explain why this example illustrates negative frequency-dependent selection.',
                'correct': 'STAGE 1 (rare mimic): predators encounter mostly toxic models, learn to avoid the pattern, and mimics gain full protection. STAGE 2 (rising mimic frequency): predators increasingly encounter palatable mimics, their avoidance learning weakens, and they sample the pattern more often. STAGE 3 (common mimic): the pattern no longer reliably predicts toxicity; predators attack both mimics and models; the MODEL species suffers disproportionately (it pays toxin-production costs AND gets attacked). STAGE 4: selection favors the model evolving a NEW pattern the mimic has not yet copied, starting a coevolutionary chase. This is negative frequency-dependence because the mimic\'s fitness DECREASES as its frequency INCREASES',
                'distractors': [
                    'The mimic always benefits regardless of frequency because mimics are always protected by pattern recognition — mimic frequency has no effect on predator learning',
                    'The model always benefits because predators remember the signal permanently after a single encounter with a toxic individual — mimic frequency is irrelevant',
                    'The example illustrates positive frequency-dependence because more mimics means more pattern reinforcement for predators, making mimicry more effective as it becomes more common',
                ],
            },
            {
                'question': 'L3 APPLICATION: You observe three butterfly species in the same Amazonian habitat. Species A and B are both toxic and share a very similar black-and-red wing pattern. Species C is palatable but has a subtly different red-and-yellow pattern. Classify the relationships and justify.',
                'correct': 'Species A and B show MÜLLERIAN mimicry — both are toxic and share a warning pattern for mutual benefit. Species C is NOT currently participating in Batesian mimicry of A and B because its pattern is sufficiently different. Species C could potentially evolve toward the A/B pattern over time if selection for Batesian resemblance is strong enough; whether it does depends on current predator discrimination',
                'distractors': [
                    'All three species show Batesian mimicry regardless of pattern differences — palatability alone determines the category',
                    'Species A and B are Batesian mimics of each other because they share a pattern; Species C is a Müllerian mimic because it has a different pattern',
                    'None of the species are mimics because mimicry requires species from different genera and all three are butterflies',
                ],
            },
        ],
        visual={
            'type': 'comparison',
            'description': 'Mimicry types',
            'regions': [
                {'label': 'Müllerian', 'color': '#ff6b6b', 'items': ['Both toxic', 'Mutual benefit', 'Faster predator learning']},
                {'label': 'Batesian', 'color': '#ffc857', 'items': ['Mimic palatable', 'Model toxic', 'Parasitic on model']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'M = Mutual. B = Bluff.',
            'trap': 'Batesian mimics only work if rare relative to model. If mimics outnumber models, predators learn the signal is unreliable.',
        },
    diagram=mullerian_vs_batesian_compare_diagram(),
    ))
    nodes.append(build_node(
        id='lec9-endosymbiosis',
        title='Endosymbiosis & Microbes',
        subtitle='Mitochondria, chloroplasts, and leafhopper symbionts (Lec 9 slides 30-36)',
        color='green', row=8,
        heading='Lecture 9 — Microbes and Endosymbiosis',
        sections=[{'label': 'CORE CONCEPT', 'body': 'ENDOSYMBIONTS live inside host cells. Humans carry ~100 trillion microbes (more microbial than human cells). Aster leafhoppers harbor Nasuia and Sulcia bacteria in specialized bacteriomes, with 260–280 million years of coevolution producing congruent host–symbiont phylogenies. ENDOSYMBIOSIS THEORY: popularized by Lynn Margulis in the 1960s-70s (her paper was initially REJECTED before being accepted), proposing that mitochondria and chloroplasts descend from free-living bacteria engulfed by ancestral eukaryotes. Mitochondria\'s closest known relative is Pelagibacteracea (the marine SAR11 clade of alpha-proteobacteria). EVIDENCE: (1) own circular DNA, (2) double membranes, (3) 70S (bacterial-type) ribosomes, (4) binary fission division. Over evolutionary time, mitochondria have LOST most of their original bacterial genes to the nuclear genome (endosymbiotic gene transfer); modern mito genomes encode only ~13 proteins in humans. CHLOROPLASTS descend from cyanobacteria. EUGLENA results from SECONDARY endosymbiosis (a eukaryote engulfed another eukaryote containing plastids).'}] + slides_to_sections(d, (30, 36)),
        examples=[
            'Endosymbiosis theory (Margulis): mitochondria and chloroplasts are descendants of free-living bacteria engulfed by ancestral eukaryotes.',
            'Evidence: mitochondria and chloroplasts have their own circular DNA, double membranes, and divide by binary fission like bacteria.',
            'Aster leafhoppers carry bacterial endosymbionts that provide essential amino acids.',
            'Plant plastids are derived from free-living cyanobacteria.',
            'Many insects depend on bacterial symbionts for survival — without them, they cannot develop.',
        ],
        warnings=[
            'Margulis\'s theory was initially REJECTED by the scientific community. It was accepted only after molecular evidence (mitochondrial DNA, 70S ribosomes, double membranes). Do not assume scientists immediately accepted it.',
            'Mitochondria have LOST most original bacterial genes to the nucleus via endosymbiotic gene transfer. Modern mitochondrial genomes are much smaller than free-living alpha-proteobacterial genomes — evidence of deep integration.',
        ],
        mnemonic='Endosymbiosis: not just historical — happening today. Life is collaborative.',
        flashcard={
            'front': 'What is the endosymbiotic theory, and what evidence supports it for mitochondria and chloroplasts?',
            'back': 'ENDOSYMBIOTIC THEORY (Lynn Margulis, 1967): mitochondria and chloroplasts originated as FREE-LIVING BACTERIA that were engulfed by (or entered) ancestral eukaryotic cells and became permanent intracellular symbionts. Mitochondria descend from an alpha-proteobacterium; chloroplasts descend from a cyanobacterium. EVIDENCE: (1) Mitochondria and chloroplasts have their OWN circular DNA (like bacteria), separate from the nuclear genome. (2) They have DOUBLE MEMBRANES — the inner membrane derived from the bacterial cell membrane, the outer from the host phagosome. (3) They DIVIDE BY BINARY FISSION, like bacteria. (4) Their ribosomes are 70S (bacterial type), not 80S (eukaryotic). (5) Some antibiotics that target bacterial ribosomes also affect mitochondria (but not cytoplasmic ribosomes). (6) Phylogenetic analysis of mitochondrial/chloroplast DNA places them within specific bacterial clades. The theory is now universally accepted and is one of the most important ideas in evolution.',
        },
        quiz=[
            {
                'question': 'Which feature of mitochondria provides the strongest evidence for their bacterial origin?',
                'correct': 'They have their own circular DNA, double membrane, and divide by binary fission',
                'distractors': [
                    'They contain ATP',
                    'They are found only in animal cells',
                    'They produce oxygen as a byproduct',
                ],
            },
            {
                'question': 'Modern mitochondrial genomes encode only ~13 proteins in humans, compared to the ~1,500 proteins encoded by their closest free-living relatives (alpha-proteobacteria like Rickettsia). What happened to all the "missing" mitochondrial genes?',
                'correct': 'Most ancestral mitochondrial genes were transferred to the nuclear genome over evolutionary time (endosymbiotic gene transfer), and their products are now translated in the cytoplasm and imported into mitochondria — this integration deepened the host-organelle dependency and is evidence of long coexistence',
                'distractors': [
                    'The missing genes were deleted entirely because mitochondria no longer need them — over billions of years in an oxygen-rich host, the ancestral bacterial metabolic pathways became obsolete and their genes were eliminated by relaxed selection',
                    'The missing genes were acquired by horizontal gene transfer from the host nucleus to the mitochondrial genome, causing mitochondrial genome EXPANSION relative to bacteria — modern mitochondrial genomes are actually larger than alpha-proteobacterial genomes, not smaller',
                    'Mitochondria lost most genes due to Muller\'s ratchet — as an asexual lineage with a small, bottlenecked genome, mitochondria cannot purge deleterious mutations by recombination, so nearly all genes have been lost or degenerated into pseudogenes over evolutionary time',
                ],
            },
            {
                'question': 'Chloroplasts descended from cyanobacteria, while mitochondria descended from alpha-proteobacteria. These are two SEPARATE endosymbiotic events in eukaryotic evolution. What evidence most strongly supports that these were SEPARATE events rather than a single engulfment of one ancestor?',
                'correct': 'Phylogenetic analysis of organelle DNA places mitochondria within alpha-proteobacteria and chloroplasts within cyanobacteria — two completely different bacterial lineages. If it were one event, both organelles would share a single common bacterial ancestor, and their genomes would cluster together in the bacterial tree',
                'distractors': [
                    'Mitochondria and chloroplasts have DIFFERENT sizes in the cell — mitochondria are smaller than chloroplasts, which reflects their independent origins from bacteria of different sizes; a single engulfment event would produce organelles of the same size',
                    'Both organelles divide by binary fission at DIFFERENT rates within the same cell — if they shared one origin, they would divide in synchrony because they would still respond to the same ancestral regulatory signals from their shared progenitor',
                    'The two events must have been separate because mitochondria are found in ALL eukaryotes while chloroplasts are only in plants and algae — if both came from one event, both would be universal in eukaryotes or both would be restricted to the same lineages',
                ],
            },
            {
                'question': 'Margulis\'s endosymbiotic theory was initially rejected by the scientific community when she proposed it in the late 1960s. What does this historical episode MOST reveal about the scientific process?',
                'correct': 'Revolutionary ideas require strong independent evidence to overcome skepticism and existing consensus — Margulis\'s theory was eventually accepted because molecular biology independently confirmed mitochondrial DNA, 70S ribosomes, and double membranes; scientific rejection followed by acceptance with evidence is the normal process for paradigm-shifting claims',
                'distractors': [
                    'It reveals that the scientific community is biased against female scientists — Margulis\'s theory was rejected because she was a woman, not because of the quality of her evidence, and the rejection would not have occurred if the same hypothesis had been proposed by a male biologist',
                    'It reveals that science cannot evaluate ideas about past events because endosymbiosis is unobservable — the eventual acceptance of endosymbiotic theory was not based on evidence but on a consensus shift driven by Margulis\'s persistence and persuasion',
                    'It reveals that new theories in biology are always accepted once mathematical proofs are provided — Margulis\'s theory was finally accepted when she derived a formal population-genetics proof showing that engulfment of bacteria by early eukaryotes was mathematically inevitable given their generation times',
                ],
            },
            {
                'question': 'Aster leafhoppers (and many other insects) cannot survive without their bacterial endosymbionts. Why are these obligate bacterial symbionts considered examples of ONGOING endosymbiosis rather than historical events only?',
                'correct': 'These bacteria currently live inside host cells, provide essential nutrients (amino acids the host cannot make), and have lost genes needed for free-living existence — endosymbiosis is a continuous evolutionary process, not a one-time event from billions of years ago',
                'distractors': [
                    'These examples are not really endosymbiosis because the bacteria retain their own cell walls — only mitochondria and chloroplasts qualify as true endosymbionts because they lost their cell walls',
                    'Leafhopper symbionts are commensal, not mutualistic — the bacteria benefit but the leafhopper is merely a passive host',
                    'These bacteria will not become organelles because horizontal gene transfer does not occur in modern insects, unlike in ancient eukaryote ancestors',
                ],
            },
            {
                'question': 'Mitochondria have 70S ribosomes while eukaryotic cytoplasm has 80S ribosomes. Why does this difference specifically support the endosymbiotic origin of mitochondria?',
                'correct': '70S ribosomes are characteristic of BACTERIA, while 80S ribosomes are characteristic of EUKARYOTES — the presence of bacterial-type ribosomes inside a eukaryotic cell is direct evidence that mitochondria retain their bacterial ancestry, distinct from the host cell\'s ribosomes',
                'distractors': [
                    '70S ribosomes are smaller than 80S and therefore more efficient at high metabolic rates — mitochondria evolved 70S ribosomes secondarily to optimize ATP production',
                    'The 70S/80S difference is arbitrary — ribosome size is not taxonomically meaningful and varies randomly across organisms',
                    'Mitochondrial 70S ribosomes are a laboratory artifact from contamination with bacterial cells during organelle isolation',
                ],
            },
            {
                'question': 'Certain antibiotics (e.g., chloramphenicol, streptomycin) that target bacterial ribosomes ALSO affect mitochondrial protein synthesis but NOT cytoplasmic protein synthesis. How does this observation support endosymbiotic theory?',
                'correct': 'The differential antibiotic sensitivity directly confirms that mitochondrial ribosomes are bacterial in character (70S) — the same drugs that target bacterial protein synthesis work on mitochondria because mitochondrial ribosomes retain the bacterial features the antibiotics target',
                'distractors': [
                    'Antibiotic sensitivity is unrelated to ribosomal origin — it simply reflects metabolic rate; mitochondria are more metabolically active than cytoplasm so they are more sensitive to drugs',
                    'The effect is coincidental — the shared sensitivity arose by convergent evolution of drug binding sites, not shared ancestry',
                    'Mitochondrial sensitivity to antibiotics proves they are not really organelles but opportunistic bacterial infections that modern cells still carry',
                ],
            },
            {
                'question': 'Which SEQUENCE of events most accurately describes the origin of eukaryotes according to serial endosymbiosis theory?',
                'correct': 'An ancestral host cell (possibly archaeal-like) engulfed an alpha-proteobacterium that became mitochondria; later, a lineage of this mitochondria-containing cell engulfed a cyanobacterium that became chloroplasts — two separate endosymbiotic events in a specific order',
                'distractors': [
                    'Mitochondria and chloroplasts were engulfed simultaneously in a single event, and later eukaryotic diversification separated the two organelles into different lineages',
                    'Chloroplasts evolved first, then mitochondria were engulfed by cells that already had chloroplasts — this is why plants have both organelles and animals lost their chloroplasts',
                    'Both organelles arose by spontaneous de novo assembly of membranes around bacterial genes, without any actual engulfment events',
                ],
            },
            {
                'question': 'L1 RECALL: Current molecular phylogenetics places mitochondria\'s closest known living relatives within which marine bacterial clade?',
                'correct': 'Pelagibacteracea (the SAR11 clade) — an abundant marine alpha-proteobacterial lineage that shares sequence similarity with mitochondrial genomes',
                'distractors': [
                    'Rickettsia — the intracellular typhus-causing bacteria',
                    'Cyanobacteria — the photosynthetic bacteria',
                    'Escherichia — the gut bacterial genus',
                ],
            },
            {
                'question': 'L1 RECALL: Aster leafhoppers carry two endosymbiotic bacteria in bacteriomes. Name them and state the approximate duration of coevolution.',
                'correct': 'Nasuia and Sulcia — these two bacteria have been in continuous endosymbiotic association with aster leafhopper ancestors for approximately 260–280 million years, with congruent host-symbiont phylogenies showing strict co-inheritance',
                'distractors': [
                    'Buchnera and Wolbachia, coevolving for about 100 million years',
                    'Rickettsia and Mycoplasma, coevolving for about 500 million years',
                    'Serratia and Pseudomonas, coevolving for only the last 10,000 years',
                ],
            },
            {
                'question': 'L3 APPLICATION: Euglena cells contain chloroplasts that are surrounded by THREE (or four) membranes rather than the typical two of primary chloroplasts. What does this observation imply about the origin of Euglena plastids?',
                'correct': 'Euglena chloroplasts arose from SECONDARY endosymbiosis — a heterotrophic eukaryote engulfed a photosynthetic eukaryote (such as a green alga) that already had primary chloroplasts. The extra membrane(s) derive from the engulfed eukaryote\'s plasma membrane and the host phagosome',
                'distractors': [
                    'Euglena chloroplasts are primary like those of plants — the extra membranes are a recent evolutionary modification unrelated to engulfment',
                    'Euglena chloroplasts arose from engulfing a cyanobacterium directly — the three membranes are artifacts of laboratory preparation',
                    'Euglena does not actually have chloroplasts — it is a pure heterotroph, so the three-membrane structure is a false observation',
                ],
            },
            {
                'question': 'L5 SYNTHESIS: Design an experiment that would distinguish between the Margulis endosymbiosis hypothesis and an alternative "autogenous origin" hypothesis in which mitochondria arose by membrane invagination of an ancestral cell without engulfment. Use molecular, structural, and phylogenetic lines of evidence.',
                'correct': 'MOLECULAR: Sequence mitochondrial DNA and compare to free-living bacteria vs. nuclear genes — endosymbiosis predicts mtDNA clusters within a specific bacterial clade (confirmed for alpha-proteobacteria/SAR11); autogenous origin predicts mtDNA is a subset of nuclear genes. STRUCTURAL: Examine the inner membrane for bacterial-type lipids (e.g., cardiolipin) — endosymbiosis predicts bacterial-specific lipid composition. PHYLOGENETIC: Test for congruence between mtDNA phylogeny and free-living bacterial phylogeny — endosymbiosis predicts a clean nested placement. RIBOSOMAL: 70S mito ribosomes and their sensitivity to bacterial-specific antibiotics (chloramphenicol) strongly support the endosymbiotic origin',
                'distractors': [
                    'The two hypotheses cannot be distinguished experimentally because both predict the same observable features of mitochondria today',
                    'The only distinguishing evidence is direct observation of engulfment events — since these occurred billions of years ago, endosymbiosis is unprovable',
                    'The experiment is unnecessary because autogenous origin has been disproved by consensus — no empirical test is needed',
                ],
            },
        ],
        visual={
            'type': 'origin',
            'description': 'Endosymbiosis: two major events',
            'regions': [
                {'label': 'Mitochondria', 'color': '#ff6b6b', 'items': ['Alpha-proteobacterium', '~2 Ga engulfment', 'Universal in eukaryotes']},
                {'label': 'Chloroplasts', 'color': '#7de2d1', 'items': ['Cyanobacterium', '~1.5 Ga engulfment', 'Plants & algae only']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Two bacterial ancestors, two major leaps.',
            'trap': 'Only some eukaryotes (plants, algae) have chloroplasts — all eukaryotes have mitochondria (or mitochondrial remnants).',
        },
    diagram=endosymbiosis_flow_diagram(),
    ))
    return nodes


def lec10_11_nodes():
    d = load_lec('lec10_11')
    nodes = []
    nodes.append(build_node(
        id='lec1011-why-sex',
        title='Why Sex? Costs & Benefits',
        subtitle='The twofold cost of sex and the Red Queen (Lec 10-11 slides 1-13)',
        color='pink', row=9,
        heading='Lecture 10-11 — Why Sexual Reproduction?',
        sections=[{'label': 'CORE CONCEPT', 'body': 'TWOFOLD COST OF SEX: asexual lineages reproduce 2× faster because ALL asexual offspring reproduce (all female), whereas only HALF of sexual offspring reproduce (females only). Other costs of sex: break up favorable co-adapted gene combinations, mate search effort, sexually transmitted diseases. Of ~42,000 vertebrate species, only ~0.17% reproduce asexually — sex is nearly universal despite its cost. BENEFITS OF SEX: (1) combining beneficial mutations from different lineages; (2) clearing deleterious mutations via Muller\'s Ratchet reversal through recombination; (3) reduced sibling competition when variable offspring exploit different microhabitats (shown in NZ snail Potamopyrgus antipodarum); (4) THE RED QUEEN HYPOTHESIS — parasites specialize on common host genotypes, so sex (which generates novel genotypes each generation) provides a moving target parasites cannot keep up with. Named after Lewis Carroll\'s Through the Looking-Glass: "It takes all the running you can do, to keep in the same place." Curtis Lively\'s work on Potamopyrgus snails shows more sex where there are more parasites. Water fleas (Daphnia) switch to sex in unpredictable environments.'}] + slides_to_sections(d, (1, 13)),
        examples=[
            'Twofold cost of sex: an asexual female passes 100% of her genes to each offspring; a sexual female passes only 50%. Asexual lineages should grow twice as fast.',
            'Other costs: finding a mate, courtship energy, risk of STDs, loss of coadapted gene combinations.',
            'Benefits: (1) combining beneficial mutations, (2) clearing deleterious mutations (Muller\'s ratchet), (3) reducing sibling competition through variation, (4) Red Queen effect — staying ahead of coevolving parasites.',
        ],
        warnings=[
            'The twofold cost of sex is about GENE TRANSMISSION (50% dilution per sexual female) — not about energetic cost of producing offspring. An asexual female transmits 2× more genome copies per offspring.',
            'The Red Queen does NOT mean sex always wins — in stable, low-parasite environments, asexual lineages can outcompete sexual ones (Potamopyrgus snail data).',
        ],
        mnemonic='Red Queen: "It takes all the running you can do, to keep in the same place."',
        flashcard={
            'front': 'What is the Red Queen hypothesis for the maintenance of sexual reproduction, and what evidence supports it?',
            'back': 'The RED QUEEN HYPOTHESIS (named after Lewis Carroll\'s Red Queen): sexual reproduction persists despite its twofold cost because it allows hosts to stay AHEAD of rapidly coevolving parasites. Parasites evolve fast (short generations, large populations) and constantly generate new genotypes that evade host defenses. Asexual hosts cannot shuffle their genes, so parasites adapt to them. Sexual hosts produce genetically variable offspring, some of which are resistant to current parasite genotypes — a moving target. EVIDENCE: (1) Lively studied New Zealand freshwater snails (Potamopyrgus antipodarum) that have both sexual and asexual lineages. In populations with high parasite pressure, sexual lineages dominate; in low-parasite populations, asexuals dominate. (2) Experimental coevolution of bacteria and phages shows sexual hosts maintain higher fitness under parasite pressure. The Red Queen provides the strongest answer to why sex is worth its twofold cost.',
        },
        quiz=[
            {
                'question': 'The "twofold cost of sex" refers to:',
                'correct': 'An asexual female passes 100% of her genes to each offspring, while a sexual female passes only 50%',
                'distractors': [
                    'Sexual reproduction requires twice as much energy per offspring',
                    'Males are twice as likely to get sick as females',
                    'Sexual offspring have half the survival rate of asexual offspring',
                ],
            },
            {
                'question': 'Curtis Lively\'s study of New Zealand freshwater snails (Potamopyrgus antipodarum) found that sexual snail lineages dominate in high-parasite lake populations while asexual lineages dominate in low-parasite populations. What does this DIRECTLY support?',
                'correct': 'The Red Queen hypothesis — sexual reproduction is advantageous primarily when parasite pressure is high because genetic diversity in offspring creates moving targets that coevolving parasites cannot track as efficiently as a clonal population\'s fixed genotype',
                'distractors': [
                    'Muller\'s ratchet hypothesis — asexual snails accumulate deleterious mutations faster than sexual snails in high-parasite environments because parasites provide an external source of DNA damage; sexual reproduction repairs this damage by recombination',
                    'The parasite diversity hypothesis — high-parasite lakes contain more diverse parasite species, which independently selects for sexual reproduction as a bet-hedging strategy against taxonomically varied threats rather than a coevolutionary response to any single parasite species',
                    'The environmental heterogeneity hypothesis — parasites create more variable environments that require plastic genotypes; sexual lineages produce more phenotypic plasticity per unit time than asexual lineages because recombination generates new reaction norms each generation',
                ],
            },
            {
                'question': 'Muller\'s ratchet describes the irreversible accumulation of deleterious mutations in asexual lineages. How does sexual reproduction prevent the ratchet from "clicking"?',
                'correct': 'Recombination creates offspring that combine chromosomes from two parents — some offspring inherit a LOWER mutation load than either parent if crossing over assembles a chromosome with the beneficial alleles from both parental chromosomes, reversing or resetting the ratchet that clicks one notch per asexual generation',
                'distractors': [
                    'Sexual reproduction prevents Muller\'s ratchet by allowing heterozygosity — deleterious recessive mutations are masked in heterozygotes and never expressed phenotypically, so they cannot reduce fitness and the ratchet cannot click',
                    'Sexual reproduction prevents Muller\'s ratchet by reducing the per-individual mutation rate — the meiotic DNA repair machinery is more accurate than mitotic DNA replication, so sexual organisms accumulate fewer mutations per generation than asexual organisms',
                    'The ratchet does not apply to sexual organisms because they have two genome copies — with a backup copy available, deleterious mutations in one copy are always compensated by the functional copy on the homolog, preventing any fitness reduction',
                ],
            },
            {
                'question': 'Some organisms reproduce BOTH sexually and asexually depending on conditions (e.g., aphids: clonal in summer, sexual in fall). What environmental cues would evolutionary theory predict TRIGGER a switch to sexual reproduction?',
                'correct': 'Increasing parasite pressure or environmental unpredictability in fall — the Red Queen and environmental heterogeneity benefits of sex outweigh the twofold cost when parasites are rapidly evolving or when the environment is unpredictable and variable offspring genotypes provide a hedging advantage',
                'distractors': [
                    'Decreasing food availability triggers sex because sexual offspring are smaller and require less nutrition — the switch to sexual reproduction is a starvation response, not related to genetic or parasite benefits',
                    'Increasing population density triggers sex because sexual offspring can recognize and mate with the nearest individual more easily than asexual clones can find empty niches — the shift is about competition for space, not genetic benefits',
                    'Decreasing temperature triggers sex because meiosis is temperature-sensitive and only functions below a threshold temperature; asexual reproduction is simply the default when it is too warm for meiosis to complete correctly',
                ],
            },
            {
                'question': 'What is the scientific name of the New Zealand freshwater snail studied by Curtis Lively as evidence for the Red Queen hypothesis?',
                'correct': 'Potamopyrgus antipodarum — this species has both sexual and asexual lineages within populations, making it ideal for testing Red Queen predictions',
                'distractors': [
                    'Achatina fulica — the giant African land snail, famous for invasive biology and parasite studies',
                    'Biomphalaria glabrata — the medically important snail vector for schistosomiasis in South America',
                    'Helix aspersa — the common garden snail, studied for its shell polymorphisms',
                ],
            },
            {
                'question': 'The Red Queen hypothesis takes its name from which literary source, and what is the key quote?',
                'correct': 'Lewis Carroll\'s "Through the Looking-Glass" — the Red Queen tells Alice "it takes all the running you can do, to keep in the same place." Hosts must constantly evolve just to maintain the same level of parasite resistance',
                'distractors': [
                    'Shakespeare\'s Macbeth — the Red Queen quote "to-morrow and to-morrow" represents endless coevolutionary time',
                    'The Game of Thrones TV series — the Red Queen Melisandre represents rapid genetic change under parasite pressure',
                    'Greek mythology — the Red Queen refers to Persephone, whose seasonal emergence mirrors the sexual/asexual switching seen in aphids',
                ],
            },
            {
                'question': 'In the absence of parasites and in a stable environment, what does theory predict about the outcome of competition between sexual and asexual lineages?',
                'correct': 'Asexual lineages should outcompete sexual ones due to the twofold advantage in gene transmission — without parasite pressure or other benefits of genetic diversity, the 2x gene transmission advantage of asexuals becomes decisive',
                'distractors': [
                    'Sexual lineages always win regardless of environment because sexual reproduction is evolutionarily advanced and asexual reproduction is primitive',
                    'The two strategies are always equal because any benefit of sex must be balanced by an equal cost, producing neutral competition in all environments',
                    'Asexual lineages go extinct immediately because asexual reproduction violates natural laws of genetic variation',
                ],
            },
            {
                'question': 'An asexual female produces 4 offspring; a sexual female also produces 4 offspring (2 male, 2 female). Assuming equal survival, how many granddaughters will each female have in generation 2?',
                'correct': 'The asexual female has 4 granddaughters (her 4 asexual daughters each produce another 4 asexual daughters, but counting only the 4 daughters themselves per generation shows she doubles each generation); the sexual female has only ~2 granddaughters (her 2 daughters each produce 4 offspring of which only 2 are daughters) — the asexual female is ahead by roughly 2× per generation',
                'distractors': [
                    'Both have the same number of granddaughters — sexual reproduction does not reduce reproductive output at the population level',
                    'The sexual female has more granddaughters because her offspring are more genetically diverse and survive better',
                    'The asexual female has fewer granddaughters because clonal offspring compete more intensely with each other for resources',
                ],
            },
            {
                'question': 'If sexual reproduction has multiple benefits (Red Queen, Muller\'s ratchet, combining beneficial mutations, reducing sibling competition), what does this mean for the "mystery of sex"?',
                'correct': 'No single benefit is likely to fully explain sex in isolation — most evolutionary biologists now believe that MULTIPLE benefits operate simultaneously, and their combined effect (not any single mechanism) outweighs the twofold cost of sex',
                'distractors': [
                    'The mystery is solved by the Red Queen alone — all other proposed benefits are negligible and only parasite pressure matters',
                    'Sex has no real benefit — it persists only due to phylogenetic inertia from ancestral traits that cannot be reversed',
                    'Each benefit operates in different species but never in the same species — each sexual species has only one specific benefit',
                ],
            },
            {
                'question': 'L1 RECALL: Approximately what percentage of ~42,000 known vertebrate species are obligately asexual?',
                'correct': 'Approximately 0.17% — fewer than 100 vertebrate species reproduce asexually, despite the twofold cost advantage',
                'distractors': [
                    'Approximately 25% — about one-quarter of vertebrates are asexual',
                    'Approximately 5% — roughly 2,000 species are asexual',
                    'Approximately 50% — half of all vertebrate species use asexual reproduction',
                ],
            },
            {
                'question': 'L1 RECALL: What animal taxon does "water fleas" refer to, and what key behavior do they exhibit with respect to sex?',
                'correct': 'Water fleas = Daphnia (crustaceans) — they switch between asexual (clonal) reproduction in stable conditions and sexual reproduction when the environment becomes unpredictable or stressful',
                'distractors': [
                    'Water fleas = mosquitoes — they are purely sexual regardless of environment',
                    'Water fleas = Potamopyrgus — they are asexual in all conditions',
                    'Water fleas = rotifers — they are always obligately sexual',
                ],
            },
            {
                'question': 'L4 ANALYSIS: Muller\'s ratchet describes the irreversible accumulation of deleterious mutations in asexual lineages. Why does recombination in sexual reproduction reset or reverse the ratchet?',
                'correct': 'Recombination during meiosis can assemble chromosomes that combine beneficial alleles from two parental chromosomes — producing offspring with FEWER deleterious mutations than either parent. This reverses the "one-way ratchet" of asexual lineages in which mutations only accumulate and never clean up',
                'distractors': [
                    'Recombination directly repairs mutations by detecting and fixing damaged bases — meiosis has higher fidelity DNA repair than mitosis',
                    'Recombination dilutes mutations by mixing them across more chromosomes — but does not actually remove any',
                    'Recombination prevents new mutations from occurring — sexual organisms have lower per-generation mutation rates',
                ],
            },
            {
                'question': 'L5 SYNTHESIS: Curtis Lively\'s Potamopyrgus antipodarum studies, experimental phage-bacteria coevolution, and water flea sex-switching observations all converge on a single explanation for why sex persists despite its twofold cost. Synthesize these lines of evidence into a unified argument.',
                'correct': 'All three lines converge on the RED QUEEN HYPOTHESIS: (1) Potamopyrgus shows more sex where parasite loads are high — field observation. (2) Experimental phage-bacteria coevolution shows sexual bacterial lineages (those with horizontal gene transfer) maintain higher fitness under parasite pressure — laboratory demonstration. (3) Water flea facultative sex shows that environmental unpredictability (which correlates with parasite variation) triggers the switch — adaptive plasticity. Together, the evidence shows that SEX GENERATES NOVEL GENOTYPES THAT COEVOLVING PARASITES CANNOT TRACK, providing a benefit that outweighs the twofold cost specifically under parasite pressure',
                'distractors': [
                    'All three lines support Muller\'s ratchet as the primary explanation for sex — Lively, the phage experiments, and Daphnia all show mutation-purging benefits',
                    'The three lines contradict each other and there is no unified explanation for sex',
                    'The three lines support phylogenetic inertia as the explanation — sex persists only because ancestral species were sexual',
                ],
            },
        ],
        visual={
            'type': 'cost-benefit',
            'description': 'Why sex persists despite costs',
            'regions': [
                {'label': 'Costs', 'color': '#ff6b6b', 'items': ['2× gene dilution', 'Mate finding', 'STDs', 'Lost gene combos']},
                {'label': 'Benefits', 'color': '#7de2d1', 'items': ['Combine beneficials', 'Clear deleterious', 'Red Queen', 'Reduced sib competition']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Costs 2×, Benefits variable.',
            'trap': 'No single benefit fully explains sex — most evolutionary biologists believe multiple benefits (not one alone) outweigh the costs.',
        },
        diagram=red_queen_cycle_diagram(),
    ))
    nodes.append(build_node(
        id='lec1011-anisogamy',
        title='Anisogamy: The Origin of Sexual Selection',
        subtitle='Why males and females exist + investment asymmetry (Lec 10-11 slides 14-22)',
        color='purple', row=9,
        heading='Lecture 10-11 — Anisogamy and Sexual Selection',
        sections=[{'label': 'CORE CONCEPT', 'body': 'ANISOGAMY = gametes of dissimilar size. Extreme cases: a kiwi male produces ~1 trillion sperm with the total energy content of just 1 egg; a cow ovum is ~20,000× larger than a single sperm. Anisogamy evolved from ISOGAMY (equal-sized gametes) via disruptive selection favoring two strategies — many small cheap gametes (sperm) or few large well-provisioned gametes (eggs) — with intermediates losing to both. DIFFERENTIAL INVESTMENT: females are limited by RESOURCES (egg production and parental care), males by ACCESS TO FEMALES (mating opportunities). The OPERATIONAL SEX RATIO (OSR) — ratio of sexually receptive males to females — is usually male-biased, increasing male-male competition. SEXUAL SELECTION (Darwin\'s definition): selection for traits that enhance reproductive success via mating, either through INTRASEXUAL competition (usually male-male fights) or INTERSEXUAL choice (usually female mate choice). This produces ARMAMENTS (weapons for fighting: antlers, horns) and ORNAMENTS (display traits: peacock tails, bright plumage). Classic example: elephant seal harems, where dominant bulls monopolize many females.'}] + slides_to_sections(d, (14, 22)),
        examples=[
            'Anisogamy: gametes of unequal size. Small cheap gametes (sperm) = male. Large expensive gametes (egg) = female.',
            'Isogamy → anisogamy evolved because disruptive selection on gamete size: a few large, well-provisioned gametes + many small, cheap gametes outperform intermediates.',
            'Anisogamy leads to differential reproductive investment: females invest more per offspring → fewer offspring per female.',
            'Result: males benefit from MORE MATINGS, females benefit from BETTER MATES. Leads to sexual selection.',
        ],
        warnings=[
            'Sex ROLES are NOT fixed — in pipefish and seahorses, males invest more per offspring and females compete, males choose. The rule is: the sex investing MORE per offspring is the choosy sex.',
            'Anisogamy defines male/female biologically (sperm = male, egg = female), but investment levels determine who is choosy — the two can decouple in species with male parental care.',
        ],
        mnemonic='Small sperm, Big eggs → different strategies → Sexual selection.',
        flashcard={
            'front': 'Explain how anisogamy leads to differential reproductive investment and, ultimately, sexual selection.',
            'back': 'ANISOGAMY = unequal gamete sizes. It evolved from isogamy (equal gametes) because disruptive selection favored two strategies: (A) a few large, nutrient-rich gametes (EGGS) that give each offspring a survival advantage, and (B) many small, cheap gametes (SPERM) that can contact more eggs. Intermediates lose to both strategies. Because EGGS are expensive, each female can produce only a LIMITED number of eggs per lifetime. Because SPERM are cheap, males can produce nearly unlimited sperm. CONSEQUENCE: Females are limited by RESOURCES (to make eggs and invest in offspring). Males are limited by MATINGS (access to females). This creates an ASYMMETRY: males benefit from many matings with any available female; females benefit from selective mating with the BEST male. This is the foundation of sexual selection — male-male competition AND female choice both arise directly from anisogamy. This logic (Bateman 1948, Trivers 1972) is one of the most important ideas in evolutionary biology.',
        },
        quiz=[
            {
                'question': 'Why do anisogamy and differential investment lead to sexual selection?',
                'correct': 'Males compete for limited female matings while females choose carefully among many available males',
                'distractors': [
                    'Males and females are fundamentally equal in reproductive strategy',
                    'Sexual selection is independent of gamete size',
                    'Only females experience sexual selection',
                ],
            },
            {
                'question': 'In seahorses and pipefish, MALES carry developing embryos in a brood pouch. How does this shift the direction of sexual selection compared to typical mammals?',
                'correct': 'Males become the sex with higher parental investment per offspring, making males the "limiting resource" — so females compete for access to males and males choose females, the REVERSE of the typical pattern, as predicted by Trivers\'s parental investment theory',
                'distractors': [
                    'Males brood the embryos but are not investing more per offspring than females because females produce the eggs — egg production is always the limiting investment regardless of who carries the embryos post-fertilization',
                    'Seahorse males and females should have equal competition because the investment is shared: females produce eggs, males brood embryos — both investments are equivalent, so neither sex is choosier',
                    'Role reversal in seahorses is due to their phylogenetic position, not parental investment — all members of the family Syngnathidae have reversed sex roles because they evolved from an ancestor that used external fertilization, which always leads to male parental care regardless of investment levels',
                ],
            },
            {
                'question': 'Anisogamy (unequal gametes) is thought to have evolved from isogamy (equal gametes) through disruptive selection. In an ancestral isogamous population, what selection pressure would drive the evolution of two distinct gamete types?',
                'correct': 'Disruptive selection on gamete size: large, nutrient-rich gametes improved offspring survival; small, numerous gametes maximized fertilization encounters. Intermediates were out-competed by both strategies — so the population split into large-few (eggs) vs. small-many (sperm) gamete producers',
                'distractors': [
                    'Directional selection for larger gametes — over time, gametes got progressively larger to provide more nutrients to offspring, until the population hit a constraint where some gametes had to stay small to move toward eggs, creating the binary we see today',
                    'Sexual conflict drove the evolution of anisogamy — male ancestors actively prevented female ancestors from controlling fertilization by evolving smaller gametes that could fertilize eggs without female consent, driving females to evolve larger, harder-to-fertilize eggs in defense',
                    'Isogamy broke down due to genetic drift in small founding populations — the initial size difference between gametes was random, and once it appeared, it was amplified by drift until two distinct gamete types existed; selection played no role in the initial divergence',
                ],
            },
            {
                'question': 'Bateman\'s 1948 experiments with Drosophila showed that male reproductive success was more variable than female reproductive success (some males fathered many offspring; others fathered none). Why does this variance asymmetry PREDICT the patterns we see in sexual selection?',
                'correct': 'High male variance means the "stakes" of mate choice/competition are higher for males — a male that wins many matings gets vastly more offspring than an average male. This creates strong selection for traits (weapons, ornaments, persistence) that increase competitive success, producing the exaggerated secondary sexual traits we observe in males of many species',
                'distractors': [
                    'High male variance means most males die without reproducing, which reduces effective population size and makes genetic drift the dominant evolutionary force on male traits — the exaggerated male ornaments we see are not sexually selected but are neutral traits fixed by drift in small effective populations',
                    'High male variance means females control male evolution — because most males fail to reproduce, any female preference (however arbitrary) determines which male genes persist. Therefore females drive evolution via drift-like random preferences, not via selection for genetic quality',
                    'The variance asymmetry predicts that FEMALES should have more exaggerated traits because highly variable male success means females must compete harder for the "winning" males — in species with high male variance, females are always the competing sex and males are always the choosing sex',
                ],
            },
            {
                'question': 'Trivers\'s (1972) parental investment theory builds directly on Bateman\'s observations. What is the core rule Trivers proposed linking investment to sexual selection?',
                'correct': 'The sex that invests more per offspring becomes the choosy sex, while the sex that invests less competes for access to the investing sex — this is a general rule that applies regardless of whether the higher-investing sex is male or female',
                'distractors': [
                    'The sex with the larger gametes always invests more and is always the choosy sex — this is a fixed biological rule that cannot be reversed regardless of parental care patterns',
                    'The sex with higher parental investment experiences stronger sexual selection pressure — high-investing individuals are the competing sex because they must maximize their return on investment',
                    'Parental investment is irrelevant to sexual selection — competition vs. choosiness is determined entirely by gamete size, not parental care',
                ],
            },
            {
                'question': 'In an isogamous species where all gametes are the same size, could sexual selection still operate?',
                'correct': 'Sexual selection would be very weak or absent because isogamy produces no asymmetry in gamete investment — without anisogamy, there is no "limiting sex" and no differential competition or choice, so the selective pressures underlying male-female asymmetries do not exist',
                'distractors': [
                    'Sexual selection operates equally strongly in isogamous species because gamete size is irrelevant — only mating behavior determines selection pressure',
                    'Sexual selection is stronger in isogamous species because equal gametes create more intense competition between all individuals simultaneously',
                    'Isogamous species cannot exist because any variation in gamete size immediately produces anisogamy within a single generation',
                ],
            },
            {
                'question': 'A male Drosophila in Bateman\'s experiment with 5 matings on average sired 4 times as many offspring as a female with 5 matings. What mechanistic explanation does anisogamy provide for this result?',
                'correct': 'Female reproductive output is limited by the number of eggs she can produce, regardless of how many times she mates — additional matings do not produce more offspring. Male reproductive output is limited by matings, so each extra mating dramatically increases his offspring count. This variance in male returns per mating is the direct consequence of anisogamy',
                'distractors': [
                    'Males produce healthier sperm than females produce eggs, so male-fathered offspring have higher survival rates, explaining the 4x difference',
                    'Drosophila males are physiologically capable of more matings per hour than females, so the observed difference reflects pure mechanical mating rate rather than anisogamy',
                    'The result is an experimental artifact — in nature, male and female fly reproductive success is equal',
                ],
            },
            {
                'question': 'Which outcome BEST illustrates the general rule that the "limiting sex" becomes the choosy one?',
                'correct': 'In mammals, females carry embryos internally and lactate — they invest far more per offspring than males and are therefore the choosy sex; in pipefish, males brood embryos and are the choosy sex; in both cases the higher-investing sex is choosy regardless of being male or female',
                'distractors': [
                    'In all species, females are always choosy because females produce eggs — the "limiting sex" concept is a restatement of the universal rule that females choose and males compete',
                    'The choosy sex is always determined by body size — the larger sex is always choosy because larger individuals are higher quality',
                    'There is no general rule — choosiness vs. competition is species-specific and cannot be predicted from investment patterns',
                ],
            },
            {
                'question': 'L1 RECALL: Approximately how many sperm does a male kiwi produce, and how does this compare energetically to one egg?',
                'correct': 'Approximately 1 trillion sperm — together carrying the energy equivalent of a single egg, illustrating the extreme difference in per-gamete investment between the sexes',
                'distractors': [
                    'About 1,000 sperm, with each sperm carrying 10x the energy of one egg',
                    'Exactly the same number as eggs the female produces — kiwis are isogamous',
                    'About 1 million sperm with each carrying 5x the energy of one egg',
                ],
            },
            {
                'question': 'L1 RECALL: The Operational Sex Ratio (OSR) is typically biased in which direction, and what is its main consequence for sexual selection?',
                'correct': 'Typically male-biased — more sexually receptive males than receptive females at any given time, which intensifies male-male competition for access to females',
                'distractors': [
                    'Typically female-biased — more receptive females means males can afford to be choosy',
                    'Always exactly 1:1 — OSR matches the overall population sex ratio',
                    'Varies randomly by year with no consistent direction',
                ],
            },
            {
                'question': 'L3 APPLICATION: Which example demonstrates the ARMAMENT side of sexual selection rather than the ORNAMENT side?',
                'correct': 'Male elephant seal harem defense — males use their massive bulk and canine teeth as weapons in intrasexual combat, directly fighting rival males for access to female harems',
                'distractors': [
                    'Peacock tail feathers — large colorful displays attract female mates',
                    'Long-distance bird songs — males advertise their quality through complex vocalizations',
                    'Bowerbird nest decorations — males build elaborate displays to attract females',
                ],
            },
            {
                'question': 'L5 SYNTHESIS: Trace the logical chain from ISOGAMY → ANISOGAMY → DIFFERENTIAL INVESTMENT → SEXUAL SELECTION, explaining why each step follows necessarily from the previous one.',
                'correct': 'STEP 1: Isogamy (equal gametes) is unstable under disruptive selection — extreme large-few and small-many gametes each out-compete intermediates. STEP 2: Anisogamy establishes two gamete types, defining sexes biologically. STEP 3: Large gametes (eggs) cost more to produce, limiting female reproductive output by RESOURCES; small gametes (sperm) are nearly unlimited, making male reproductive output limited by ACCESS TO FEMALES. STEP 4: This asymmetry creates male-male competition (for limiting females) and female choice (selecting best mates among many competing males), which is SEXUAL SELECTION. Each step follows because the previous one establishes the necessary condition for the next',
                'distractors': [
                    'The chain is not deterministic — any of the steps could reverse or fail to occur, and sexual selection is not a necessary consequence of anisogamy',
                    'The chain runs in reverse: sexual selection drove anisogamy, not the other way around',
                    'Anisogamy has nothing to do with sexual selection — the two are independent evolutionary phenomena that happen to co-occur in most species',
                ],
            },
        ],
        visual={
            'type': 'asymmetry',
            'description': 'Anisogamy drives sexual asymmetry',
            'regions': [
                {'label': 'Egg', 'color': '#ff6b6b', 'items': ['Large', 'Expensive', 'Limited per lifetime', '→ Female is choosy']},
                {'label': 'Sperm', 'color': '#4ea8de', 'items': ['Small', 'Cheap', 'Nearly unlimited', '→ Male competes']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Small + Many + Cheap vs Big + Few + Expensive.',
            'trap': 'Sex ROLES are not fixed — in some species (pipefish, seahorses) males invest more and females compete. The rule is: the sex investing MORE becomes the choosy one.',
        },
    diagram=anisogamy_origin_diagram(),
    ))
    nodes.append(build_node(
        id='lec1011-male-female-strategies',
        title='Male Strategies & Female Choice',
        subtitle='Ornaments, leks, nuptial gifts, sensory bias (Lec 10-11 slides 23-37)',
        color='teal', row=9,
        heading='Lecture 10-11 — Sexual Selection Strategies',
        sections=[{'label': 'CORE CONCEPT', 'body': 'SIDE-BLOTCHED LIZARDS (Uta stansburiana): three male morphs — orange (territorial bully), blue (mate guarder), yellow (female mimic / sneaker) — maintained in a rock-paper-scissors game by negative frequency-dependent selection, with 12-year frequency cycles (Sinervo & Lively 1996). NONE of the three is an ESS alone. DIRECT vs INDIRECT BENEFITS: females may get resources (direct) or "good genes" for offspring (indirect). SEXY SON HYPOTHESIS: a female choosing an attractive male produces attractive sons who themselves mate more. NUPTIAL GIFTS: katydid spermatophores, redback spider sacrifice. LEKS: male aggregation sites — sage grouse, golden-collared manakin. SENSORY BIAS: female preference exists BEFORE the signal evolves — guppy orange preference (also used in eating orange fruit), swordtail fish preferring swords even in sword-less species. HANDICAP PRINCIPLE (Zahavi 1975): ornaments are HONEST signals precisely because they are COSTLY — only high-quality males can afford them. FISHERIAN RUNAWAY: female preference and male ornament coevolve via genetic correlation, amplifying both to extreme levels without any "quality" component.'}] + slides_to_sections(d, (23, 37)),
        examples=[
            'Side-blotched lizards: three morphs (rock-paper-scissors) maintained by negative frequency-dependent selection.',
            'Nuptial gifts: male provides food to female (e.g., scorpionflies, crickets, spiders). Female evaluates gift quality as a signal of male quality.',
            'Redback spiders: males voluntarily sacrifice themselves to be eaten, prolonging copulation and siring more offspring.',
            'Leks: males gather at display sites for female inspection (sage grouse, manakins).',
            'Sensory bias: female preferences may arise from pre-existing sensory biases (e.g., swordtail fish — females prefer swords even in species without them).',
            'Ornaments can signal GENETIC QUALITY (handicap principle) or arbitrary runaway selection.',
        ],
        warnings=[
            'Handicap principle (Zahavi 1975) and Fisherian runaway are DIFFERENT explanations. Handicap = costly honest signal of real genetic quality. Runaway = preference and trait coevolve via genetic correlation. Both can co-operate in the same system.',
            'Sensory bias is NOT the same as runaway selection. Sensory bias = preference exists BEFORE the signal evolves (the signal exploits the bias). Runaway = preference and signal coevolve and amplify each other simultaneously.',
        ],
        mnemonic='Costly signal = honest. Ornaments can\'t be faked if genuinely handicapping.',
        flashcard={
            'front': 'What is the "handicap principle" for sexual ornaments, and why must the ornaments be costly to function as honest signals?',
            'back': 'The HANDICAP PRINCIPLE (Zahavi 1975): exaggerated male ornaments (peacock tails, elaborate colors, long calls) evolve because they serve as HONEST SIGNALS OF QUALITY precisely BECAUSE they are costly. Only a high-quality male can afford to grow and maintain an extravagant ornament — low-quality males would die or fail to reproduce under the handicap. Therefore, a male with a massive ornament is demonstrating "I can thrive even with this burden." If ornaments were cheap, ANY male could grow one, and the signal would become uninformative (dishonest). The cost ENFORCES honesty — it\'s a signal that cannot be faked. Low-quality males could grow fake ornaments only at unsustainable fitness cost, so they don\'t. This is why peacock tails, male deer antlers, and stag beetle mandibles are so extravagant and metabolically expensive — the expense is the point.',
        },
        quiz=[
            {
                'question': 'According to the handicap principle, why do peacock tails evolve to be so large and metabolically expensive?',
                'correct': 'The cost ensures the signal is honest — only high-quality males can afford it, so the tail truthfully signals genetic quality',
                'distractors': [
                    'Runaway (Fisherian) sexual selection causes tail size to increase without limit until males die, so large tails are a neutral by-product',
                    'Peahens prefer large tails as a learned cultural tradition rather than an evolved response to tail quality',
                    'Large tails improve thermoregulation in tropical climates where peacocks live, so the selection pressure is ecological rather than sexual',
                ],
            },
            {
                'question': 'Fisherian runaway selection and the handicap principle both predict large male ornaments. Which observation MOST effectively distinguishes between the two as explanations for peacock tails?',
                'correct': 'Finding that tail size correlates with parasite load, immune function, or offspring survival — if ornament size honestly indicates genetic quality (e.g., healthier males have larger tails), the handicap principle is supported; if tail size shows NO correlation with health or offspring fitness but females still prefer it, runaway selection is more likely',
                'distractors': [
                    'Finding that male-male competition involves direct combat over tail size — if males fight over ornaments directly, the handicap principle is confirmed; Fisherian runaway selection requires the ornament to be evaluated only by females with no male-male component',
                    'Finding that tail size is heritable — both the handicap principle and Fisherian runaway require heritability, so confirming h² > 0 for tail size cannot distinguish between the two hypotheses',
                    'Finding that peahens in captivity still prefer large-tailed males — laboratory preference tests can only confirm female choice exists, not whether it tracks genetic quality; distinguishing the two hypotheses requires field data on fitness correlates',
                ],
            },
            {
                'question': 'Side-blotched lizards (Uta stansburiana) have three male morphs: orange-throats (hold large territories, outcompete blue-throats), blue-throats (guard mates, outcompete yellow-throats), and yellow-throats (mimic females, cuckold orange-throats). This system is maintained by:',
                'correct': 'Negative frequency-dependent selection (rock-paper-scissors) — each morph has the highest fitness when it is RARE (because the morph it beats is then common), preventing any single morph from fixing and maintaining all three at fluctuating frequencies',
                'distractors': [
                    'Heterozygote advantage — all three throat-color alleles are maintained because heterozygous individuals that carry two different color alleles have the highest reproductive success by using both territorial and sneaker strategies simultaneously',
                    'Positive frequency-dependent selection — each morph gains an advantage when common because more individuals using the same strategy means more coordinated behavior; the rock-paper-scissors is maintained because all three morphs reach frequency-dependent equilibria simultaneously',
                    'Genetic drift — the three morphs are selectively neutral and are maintained at roughly equal frequencies only by chance; in small populations, one morph occasionally goes to fixation and the other two are lost, explaining why morph ratios fluctuate between years',
                ],
            },
            {
                'question': 'Swordtail fish females (Xiphophorus helleri) show a preference for males with an artificially added "sword" (color extension) even though their species naturally LACKS swords. What does this finding MOST directly support?',
                'correct': 'Sensory bias — the female preference for sword-like extensions pre-existed the sword trait itself, suggesting the sword in swordtail species evolved to exploit a pre-existing sensory preference rather than the preference evolving in response to the sword (challenging the assumption that mate preferences and ornaments co-evolve)',
                'distractors': [
                    'Fisherian runaway selection — the female preference amplified independently of the male trait, which is exactly what Fisherian theory predicts: preferences can evolve arbitrarily and spread to fixation before the male trait evolves to match them',
                    'The handicap principle — sword-less females prefer sword-like extensions because swords are costly to produce and maintain; the preference evolved before the sword in anticipation of the honest-signal value the sword would eventually provide',
                    'Cultural transmission — female swordtail fish copy each other\'s mate preferences, and the preference for sword-like extensions spread through the population culturally from a few individuals who happened to be exposed to swordtail-fish aquarium pictures',
                ],
            },
            {
                'question': 'Redback spider males exhibit one of the most extreme forms of male investment — they somersault their abdomen into the female\'s jaws during copulation, allowing themselves to be cannibalized. Why would selection favor this behavior?',
                'correct': 'Being consumed prolongs the copulation time, allowing the male to transfer more sperm, and may also discourage the female from re-mating with another male. The male sacrifices his future reproductive opportunities for a larger share of the current female\'s eggs — a rational trade-off when future mating chances are slim',
                'distractors': [
                    'Male cannibalism evolved to provide nutrition to the developing offspring, ensuring that eggs fertilized by a sacrificed male have higher survival rates than those fertilized by a non-sacrificed male',
                    'Male cannibalism is a form of altruism toward the species — males sacrifice themselves to reduce population density, benefiting the group as a whole',
                    'The cannibalism is actually a female behavior unrelated to sexual selection — females eat males because they are hungry, not because of any reproductive benefit',
                ],
            },
            {
                'question': 'In lekking species (e.g., sage grouse, manakins), males aggregate at display sites where females visit to evaluate them. What does lek mating predict about female choice?',
                'correct': 'Females can directly compare many males at once with minimal search cost, and typically a few top-ranked males sire most offspring — leks create strong skew in male reproductive success and intense sexual selection for display traits',
                'distractors': [
                    'Lek mating produces low variance in male reproductive success because all males at the lek have roughly equal access to females',
                    'Lek mating eliminates female choice because females mate with whichever male approaches them first at the display site',
                    'Leks are pair-bonded systems — each male establishes a monogamous bond with one female who visits his display area',
                ],
            },
            {
                'question': 'Nuptial gifts (e.g., the male scorpionfly provides a protein-rich secretion to the female during mating) can signal both direct and indirect benefits to females. What are the two categories of benefits?',
                'correct': 'DIRECT benefits — the nutritional content of the gift itself boosts the female\'s immediate survival and egg production; INDIRECT benefits — gift quality may correlate with male genetic quality, so accepting a large gift also means choosing a genetically superior mate',
                'distractors': [
                    'Direct benefits to the male (higher paternity) and direct benefits to the female (more eggs) — the gift is always a selfish strategy that benefits both players equally',
                    'Nutritional benefits and territorial benefits — the female gains access to the male\'s territory as part of the gift exchange',
                    'Immediate benefits and reputational benefits — females build social status by accepting large gifts from high-ranking males',
                ],
            },
            {
                'question': 'Which researcher proposed the handicap principle, and in what year?',
                'correct': 'Amotz Zahavi, 1975 — Zahavi argued that ornaments must be costly to function as honest signals, because only cost can enforce honesty',
                'distractors': [
                    'R.A. Fisher, 1930 — Fisher first articulated the handicap principle as an extension of his runaway selection model',
                    'W.D. Hamilton, 1982 — Hamilton\'s version emphasized parasite resistance as the handicap',
                    'John Maynard Smith, 1973 — Maynard Smith derived the handicap principle from game theory',
                ],
            },
            {
                'question': 'The Fisherian runaway selection hypothesis (R.A. Fisher 1930) proposes that female preferences and male ornaments can coevolve rapidly. What is the mechanism?',
                'correct': 'A genetic correlation builds up between the gene for the male trait and the gene for female preference — sons inherit both elaborated traits and the preference. As ornaments become exaggerated, females with strong preferences produce sexier sons, creating a positive feedback loop that drives both traits to extremes even without any link to male quality',
                'distractors': [
                    'Runaway selection operates through direct benefits — ornamented males provide more parental care, so females with preferences for ornaments have better offspring survival',
                    'Runaway is driven by cultural transmission — females copy each other\'s preferences until one preference dominates the population through social learning rather than genetics',
                    'Runaway requires that males evolve ornaments first, which then induce females to evolve preferences as a response — the trait leads, the preference follows',
                ],
            },
            {
                'question': 'L1 RECALL: Which researchers documented the 12-year rock-paper-scissors cycle of three throat-color morphs in side-blotched lizards?',
                'correct': 'Sinervo and Lively (1996) — their foundational Nature paper showed that orange, blue, and yellow male morphs oscillated in frequency over ~12-year cycles driven by negative frequency-dependent selection',
                'distractors': [
                    'Darwin and Wallace (1858) — the original researchers on lizard polymorphisms',
                    'Maynard Smith and Price (1973) — they first observed the phenomenon while developing ESS theory',
                    'Zahavi (1975) — documented the cycles while developing the handicap principle',
                ],
            },
            {
                'question': 'L1 RECALL: What is the SEXY SON HYPOTHESIS?',
                'correct': 'Females who mate with attractive males produce attractive SONS who themselves gain higher mating success, so the benefit to the female comes not from direct resources or good-genes survival but from having sons who inherit the attractive trait and reproduce prolifically',
                'distractors': [
                    'Females should always produce more sons than daughters because sons gain more reproductive success from being attractive',
                    'Females prefer attractive males because sons inherit reduced lifespans — the hypothesis predicts shorter-lived but more reproductive sons',
                    'The hypothesis states that male attractiveness is a direct predictor of paternal care quality',
                ],
            },
            {
                'question': 'L1 RECALL: Name two iconic lekking species discussed in the lecture.',
                'correct': 'Sage grouse (Centrocercus urophasianus) and golden-collared manakin (Manacus vitellinus) — both species form male aggregations at display sites where females visit to choose mates, producing extreme skew in male reproductive success',
                'distractors': [
                    'Peacocks and red deer — both are classic lekking species',
                    'Elephant seals and bighorn sheep — both form leks for female choice',
                    'Chimpanzees and gorillas — primate leks',
                ],
            },
            {
                'question': 'L5 SYNTHESIS: A biologist discovers a bird species where males have extravagant tail feathers. She wants to determine whether the trait is maintained by (a) handicap/good-genes, (b) Fisherian runaway, or (c) sensory bias. Design an experimental program to distinguish between the three hypotheses.',
                'correct': '(a) HANDICAP: measure correlation between tail size and independent fitness metrics (parasite load, immune function, offspring survival). If tail size honestly signals quality, correlations should be positive. (b) FISHERIAN RUNAWAY: estimate genetic correlation between male tail-size gene and female preference gene — runaway predicts strong linkage. Also test if preferences exceed any quality correlation (preference without fitness payoff). (c) SENSORY BIAS: survey related species WITHOUT the tail — if females in those species ALSO prefer artificially added tails, the preference predates the signal and sensory bias is supported. Combining these three tests can distinguish among the hypotheses and may reveal that multiple mechanisms operate together',
                'distractors': [
                    'The three hypotheses cannot be distinguished experimentally because they all predict the same outcome (extravagant male tails and female preference)',
                    'Only hypothesis (a) is testable because runaway and sensory bias are untestable theoretical constructs',
                    'Sensory bias is always the correct answer in all cases — test only for ancestral preferences and ignore the other hypotheses',
                ],
            },
        ],
        visual={
            'type': 'strategies',
            'description': 'Male reproductive strategies',
            'regions': [
                {'label': 'Competition', 'color': '#ff6b6b', 'items': ['Male-male fighting', 'Weaponry', 'Territory defense']},
                {'label': 'Choice', 'color': '#7de2d1', 'items': ['Ornaments', 'Handicap signals', 'Lek display', 'Nuptial gifts']},
                {'label': 'Alternatives', 'color': '#ffc857', 'items': ['Sneaker males', 'Alt morphs', 'Freq-dependent']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Fight, Display, or Cheat.',
            'trap': 'Runaway selection (Fisherian) and handicap signals (Zahavian) are not mutually exclusive — both can operate simultaneously.',
        },
    diagram=side_blotched_rps_cycle_diagram(),
    ))
    nodes.append(build_node(
        id='lec1011-sperm-competition',
        title='Sperm Competition & Sexual Conflict',
        subtitle='When females mate with multiple males (Lec 10-11 slides 38-45)',
        color='red', row=9,
        heading='Lecture 10-11 — Sperm Competition and Sexual Conflict',
        sections=[{'label': 'CORE CONCEPT', 'body': 'When females mate with multiple males, sperm from different males compete to fertilize eggs. FOUR MALE STRATEGIES: (1) REMOVE RIVAL SPERM — seed beetles have penile spines that scrape rival sperm from the female reproductive tract; dragonflies do the same. (2) PRODUCE MORE SPERM — chimpanzees (highly polyandrous) have very LARGE testes relative to body size, gorillas (harem-holding) have small testes, humans are intermediate; testes-size/body-size ratio predicts mating system. (3) SPERM COOPERATION — Peromyscus maniculatus (promiscuous mice) sperm form cooperative "brother sperm" swimming trains, while P. polionotus (monogamous) show indiscriminate aggregation with no selective cooperation. (4) PREVENT FEMALE REMATING — mate guarding, toxic seminal proteins (Drosophila accessory gland proteins), giant sperm, copulatory plugs. SEXUAL CONFLICT: Drosophila seminal fluid proteins increase female egg-laying but reduce female lifespan; females evolve defensive proteins in reciprocal response. A 40-generation forced-monogamy experiment in Drosophila reduced male toxicity AND reduced female defenses — showing rapid reciprocal evolution within a species.'}] + slides_to_sections(d, (38, 45)),
        examples=[
            'Sperm competition: when multiple males\' sperm compete within the female reproductive tract to fertilize eggs.',
            'Male strategies: (1) Spines remove rival sperm (Odonata), (2) Larger testes produce more sperm (primates with promiscuous females), (3) Sperm cooperate by forming swimming trains (some rodents), (4) Mate guarding / mating plugs / copulatory prolongation.',
            'Drosophila seminal fluid contains chemicals that suppress female remating and reduce sperm of previous males — BUT also shorten female lifespan (sexually antagonistic).',
            'Sexual conflict: what is optimal for males may harm females.',
        ],
        warnings=[
            'Sexual conflict drives rapid reciprocal evolution — an intersexual arms race WITHIN a single species, producing rapid coevolution of male offense and female defense.',
        ],
        mnemonic='Remove, Out-produce, Cooperate, Prevent remating = 4 sperm strategies.',
        flashcard={
            'front': 'What is sexual conflict and how does it manifest in Drosophila seminal fluid proteins?',
            'back': 'SEXUAL CONFLICT arises when what is optimal for male reproductive success is HARMFUL to female fitness (or vice versa). Because males and females share most of their genomes, evolution of male-beneficial traits can reduce female fitness and drive counter-adaptations in females — a sexually antagonistic coevolutionary arms race WITHIN a species. DROSOPHILA EXAMPLE: Male seminal fluid contains proteins (ACPs) that (1) suppress female remating with other males, (2) increase female egg-laying rate, and (3) kill sperm of previously mated males. These adaptations BENEFIT the male (by monopolizing paternity and accelerating reproduction). HOWEVER, the same chemicals ALSO SHORTEN FEMALE LIFESPAN and REDUCE HER LIFETIME REPRODUCTIVE SUCCESS. Females experience selection to resist the harmful effects, potentially by evolving detoxifying enzymes or refusing to mate. This drives reciprocal evolution between male offense and female defense — a form of intragenomic arms race. Sexual conflict is one of the most important insights of modern sexual selection theory.',
        },
        quiz=[
            {
                'question': 'A species where females mate with many males during one estrus period is most likely to have evolved:',
                'correct': 'Relatively large testes to produce more sperm for competition',
                'distractors': [
                    'Elaborate male display ornaments for female choice',
                    'Complete monogamy',
                    'Reduced sexual dimorphism',
                ],
            },
            {
                'question': 'Dragonfly males have penile structures that can scrape rival sperm from the female\'s reproductive tract before depositing their own sperm. Which aspect of sperm competition theory MOST directly predicts this adaptation?',
                'correct': 'When females commonly mate with multiple males before a single fertilization event, the last-male advantage hypothesis predicts selection for mechanisms that reduce the success of rival sperm already present — scraping is one strategy to achieve sperm precedence',
                'distractors': [
                    'The dragonfly structure evolved to prevent physical injury to the female during mating — sperm scraping is a cooperative adaptation that protects the female\'s reproductive tract from damage by rival males\' sperm, which would otherwise cause inflammation',
                    'The sperm-scraping structure is evidence of sexual conflict, where males have evolved a device that HARMS females by removing their option to use stored sperm from chosen previous mates — females have co-evolved resistance by reducing the efficiency of scraping with modified sperm-storage morphology',
                    'The scraping structure evolved through Müllerian mimicry between dragonfly species — multiple species converged on the same penile design because it optimally transfers sperm in the shared aquatic environment where all dragonflies breed',
                ],
            },
            {
                'question': 'Drosophila seminal fluid proteins (ACPs) increase female egg-laying rate AND suppress female remating BUT also shorten female lifespan. From the FEMALE\'s perspective, what is the evolutionarily optimal response to receiving these proteins?',
                'correct': 'Females should evolve resistance to the harmful components of ACPs (e.g., enzymes to degrade lifespan-shortening compounds) while retaining sensitivity to beneficial components — this is an intrasexual arms race where males evolve more effective ACPs and females evolve countermeasures',
                'distractors': [
                    'Females should evolve to maximize their uptake of ACPs because the increased egg-laying rate more than compensates for the shortened lifespan — from a lifetime fitness standpoint, more eggs per day always outweighs a shorter reproductive period',
                    'Females should evolve to REJECT sperm from males whose ACPs are most harmful — by co-evolving receptors that detect harmful ACPs, females can choose mates whose proteins increase reproduction without the lifespan cost',
                    'Females have no evolutionary recourse because ACPs are delivered internally during mating — natural selection cannot act on a trait that is only expressed internally after mating has already occurred, so female resistance to ACPs cannot evolve',
                ],
            },
            {
                'question': 'In gorillas (highly polygynous, one male per many females), testes are relatively SMALL compared to body size. In chimpanzees (promiscuous, females mate with many males), testes are very LARGE relative to body size. Humans fall between the two. What mating system does human testes size SUGGEST our evolutionary history included?',
                'correct': 'Moderate polygyny or mild promiscuity — human testes size (intermediate between gorilla and chimpanzee) suggests our lineage experienced sperm competition at moderate levels, consistent with a mating system where females occasionally mated with more than one male but not at the high frequency seen in chimpanzees',
                'distractors': [
                    'Strict monogamy throughout our evolutionary history — human testes are LARGER than gorilla testes, which is only consistent with a monogamous system where sperm competition is zero; gorilla testes are small because the single dominant male wastes no resources on sperm competition',
                    'Strict polygyny with no sperm competition — humans evolved in harem systems like gorillas; the slight increase over gorilla testes size reflects recent cultural changes from polygyny to serial monogamy, not ancient sperm competition',
                    'Testes size has no evolutionary significance for mating system inference because testes size is primarily determined by developmental temperature regulation, not by any sperm-competition-related selection pressure',
                ],
            },
            {
                'question': 'In some rodent species (e.g., wood mice), sperm physically form "sperm trains" that swim faster as a group than individual sperm. What selective pressure drives this cooperation between sperm from the same male?',
                'correct': 'All sperm in a single ejaculate are genetically related (they all carry copies of the same male\'s genome), so cooperation among them increases the inclusive fitness of each sperm — faster group swimming gives the cooperating male\'s sperm a competitive advantage over sperm from rival males',
                'distractors': [
                    'Sperm trains evolve to reduce energy expenditure — sperm save ATP by drafting behind each other like cyclists, not for any competitive advantage',
                    'Sperm trains are accidental clumping caused by seminal fluid viscosity, not an adaptation — there is no reproductive benefit',
                    'Sperm cooperation requires sperm to carry different alleles so they can recognize each other as distinct — this only works in highly outbred populations',
                ],
            },
            {
                'question': 'Mating plugs (gelatinous secretions that block a female\'s reproductive tract after mating) are found in many species. What is the adaptive function from the male\'s perspective?',
                'correct': 'Mating plugs prevent the female from receiving sperm from subsequent males, ensuring the plugging male\'s sperm sire the offspring — a form of post-copulatory mate guarding that reduces sperm competition',
                'distractors': [
                    'Mating plugs protect the female from infection during vulnerable post-mating periods — they are a cooperative adaptation that benefits both sexes',
                    'Mating plugs serve as nutrition for the developing embryos — the male provides post-fertilization resources through the plug',
                    'Mating plugs signal to other males that the female is unavailable, preventing wasteful mating attempts that would harm the male-female bond',
                ],
            },
            {
                'question': 'What is the KEY concept distinguishing SEXUAL CONFLICT from regular sexual selection?',
                'correct': 'Sexual conflict occurs when the evolutionary optimum for males differs from the optimum for females — traits beneficial to one sex can reduce the fitness of the other, driving an arms race WITHIN a species. Regular sexual selection can involve mutual benefit or one-sided choice without such intrasexual conflict',
                'distractors': [
                    'Sexual conflict occurs only between species (e.g., interspecific hybridization attempts), while sexual selection occurs within species',
                    'Sexual conflict is about physical aggression between individuals, while sexual selection is purely about mate choice without combat',
                    'Sexual conflict is a hypothetical concept that has not been experimentally verified, while sexual selection has extensive experimental support',
                ],
            },
            {
                'question': 'A female Drosophila that has received ACPs (accessory gland proteins) shows increased egg-laying and reduced interest in re-mating. If she could evolutionarily resist ACPs, what conflict does this illustrate?',
                'correct': 'Intersexual (sexual) conflict — male ACPs benefit the male by monopolizing paternity and accelerating egg-laying, but harm the female by shortening her lifespan. Female counter-adaptations (e.g., enzymes that degrade ACPs) represent her evolutionary response to the male strategy',
                'distractors': [
                    'Intrasexual conflict — ACPs are male-male competition tools that do not affect the female directly; the female is a passive vehicle',
                    'Parent-offspring conflict — ACPs affect the offspring\'s development at the expense of the mother, creating a dispute over resource allocation',
                    'Kin conflict — ACPs reduce the inclusive fitness of the female\'s relatives who share her genes',
                ],
            },
            {
                'question': 'L1 RECALL: In what Peromyscus species does sperm form cooperative "brother sperm" swimming trains, and what is the mating system?',
                'correct': 'Peromyscus maniculatus — a PROMISCUOUS species where female mice mate with multiple males. Sperm from a single ejaculate form cooperative swimming trains that out-race rival sperm from competing males',
                'distractors': [
                    'Peromyscus polionotus — a monogamous species where sperm cooperation evolved first and was later lost in promiscuous relatives',
                    'Peromyscus leucopus — a species with no sperm cooperation',
                    'Peromyscus californicus — the only known primate-like Peromyscus species',
                ],
            },
            {
                'question': 'L1 RECALL: In the forced-monogamy Drosophila experiment (40 generations), what changes occurred in male seminal fluid toxicity and female defenses?',
                'correct': 'After 40 generations of enforced monogamy, male seminal fluid became LESS toxic (no longer needed because no sperm competition) AND female defensive proteins DECREASED (no longer needed because males stopped harming them) — demonstrating rapid reciprocal de-escalation in sexual conflict',
                'distractors': [
                    'Males became more toxic and females more defensive — enforced monogamy intensified the arms race',
                    'No detectable changes occurred within 40 generations — sexual conflict evolves too slowly',
                    'Males became more toxic and females became less defensive, leading to female extinction in the experimental lines',
                ],
            },
            {
                'question': 'L3 APPLICATION: Gorillas have small testes relative to body size; chimpanzees have very large testes. What does testes size ratio PREDICT about the mating system that shapes a species?',
                'correct': 'Small testes relative to body size indicate LOW sperm competition (monogamous or harem systems where a single male monopolizes matings); large testes indicate HIGH sperm competition (promiscuous systems where multiple males mate with each female and sperm compete in the female tract). The predictive relationship is robust across primates',
                'distractors': [
                    'Testes size ratio is random and has no predictive value for mating system',
                    'Large testes predict monogamy because fewer matings require each ejaculate to be larger',
                    'Small testes predict promiscuity because smaller sperm are faster swimmers',
                ],
            },
            {
                'question': 'L5 SYNTHESIS: Integrate the four sperm-competition strategies (remove, out-produce, cooperate, prevent remating) into a unified framework explaining how mating-system promiscuity predicts which strategies dominate. Provide specific examples.',
                'correct': 'Mating system dictates sperm competition intensity which shapes strategy selection: (1) REMOVE — favored when females store sperm and last-male precedence is common (dragonflies, seed beetles). (2) OUT-PRODUCE — favored when multiple males ejaculate sequentially (chimps vs gorillas testes size ratio). (3) COOPERATE — favored when sperm from one ejaculate must out-swim rivals (Peromyscus maniculatus brother-sperm trains). (4) PREVENT REMATING — favored when monopolizing paternity is possible (Drosophila ACPs, mating plugs). Species commonly deploy multiple strategies; the relative importance depends on whether competition happens within the female or between ejaculate volumes',
                'distractors': [
                    'All four strategies are equally effective in all species and their distribution is random',
                    'Only one strategy can evolve in a given lineage because they are mutually exclusive',
                    'Species use whichever strategy their ancestors used regardless of current mating system — phylogenetic inertia dominates',
                ],
            },
        ],
        visual={
            'type': 'strategies',
            'description': 'Sperm competition strategies',
            'regions': [
                {'label': 'Remove rivals', 'color': '#ff6b6b', 'items': ['Dragonfly penis spines', 'Scrape previous sperm']},
                {'label': 'Out-produce', 'color': '#4ea8de', 'items': ['Bigger testes', 'More sperm per ejaculate']},
                {'label': 'Cooperate', 'color': '#7de2d1', 'items': ['Sperm trains', 'Cooperative swimming']},
                {'label': 'Prevent remating', 'color': '#ffc857', 'items': ['Mating plugs', 'Mate guarding', 'Chemicals in semen']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'RCOP: Remove, Cooperate, Out-produce, Prevent.',
            'trap': 'Testis size (relative to body mass) is a strong predictor of mating system — promiscuous species have large testes, monogamous species have small ones.',
        },
    diagram=sperm_competition_strategies_diagram(),
    ))
    return nodes


def lec12_nodes():
    d = load_lec('lec12')
    nodes = []
    nodes.append(build_node(
        id='lec12-life-history-intro',
        title='Life History Strategies & Trade-offs',
        subtitle='r-K strategies, energy and time trade-offs (Lec 12 slides 1-11)',
        color='amber', row=10,
        heading='Lecture 12 — Life History Evolution',
        sections=[{'label': 'CORE CONCEPT', 'body': 'Energy and time are FINITE — every organism faces trade-offs between growth, maintenance, immune defense, and reproduction. Extreme life-history examples: Adactylidium mites are born already sexually mature, are inseminated by their own brothers (who die shortly after) inside the mother, then consume the mother from within; adults live ~4 days. Kiwis lay a SINGLE huge egg relative to body size. Mayflies live only hours as adults but can lay thousands of eggs. Elephants take 10–12 years to reach reproductive maturity. Bristlecone pines can live over 4000 years. The r/K-SELECTION continuum characterizes these strategies: r-selected = fast growth (rabbits, insects, weeds) with many small offspring, little parental care, short lifespan; K-selected = slow, stable growth (elephants, humans, long-lived trees) with few large offspring, heavy parental investment, long lifespan. Two polar strategies are MAXIMIZE SIZE (grow big to dominate at carrying capacity) vs MINIMIZE TIME (reproduce fast before you die). Opossums have been shown to shift energy allocation between reproduction and maintenance as they age.'}] + slides_to_sections(d, (1, 11)),
        examples=[
            'Life history: the schedule of birth, maturation, reproduction, and death.',
            'r-strategy: many small offspring, little parental care, fast maturation (insects, weeds).',
            'K-strategy: few large offspring, heavy parental care, slow maturation (elephants, humans, oak trees).',
            'Trade-offs: energy spent on reproduction CANNOT be spent on growth or survival. Time spent finding a mate cannot be spent foraging.',
        ],
        warnings=[
            'r/K is a CONTINUUM, not a binary. Most species fall somewhere in between — do not treat r vs K as mutually exclusive categories.',
            'r and K are POPULATION GROWTH parameters. r-selected species thrive when population is below carrying capacity (high r); K-selected species are competitive at carrying capacity. The strategy is about environment stability, not just offspring number.',
        ],
        mnemonic='r vs K: rabbits (r) vs K-apes. Live fast die young OR slow and steady.',
        flashcard={
            'front': 'What are the classic r vs K life history strategies, and what trade-off underlies the distinction?',
            'back': 'The r/K strategy framework describes two ends of a continuum of life-history strategies. r-SELECTED species (named for r in population growth models) live in unstable or unpredictable environments. They evolve FAST reproduction: many small offspring, rapid maturation, little parental care, short lifespan. Examples: insects, dandelions, mice. Each offspring has low survival probability, but sheer numbers compensate. K-SELECTED species (K = carrying capacity) live in stable, competitive environments. They evolve SLOW reproduction: few large offspring, long maturation, heavy parental investment, long lifespan. Examples: elephants, humans, oak trees. Each offspring has high survival probability. The UNDERLYING TRADE-OFF is that energy/time devoted to reproduction cannot be used for growth or maintenance, and vice versa. The r/K framework is now considered a simplification — modern life history theory uses continuous traits and optimization models — but it remains a useful conceptual starting point.',
        },
        quiz=[
            {
                'question': 'An r-selected species is most likely to:',
                'correct': 'Produce many small offspring with little parental care and mature quickly',
                'distractors': [
                    'Produce few large offspring with heavy parental care',
                    'Have very long lifespans',
                    'Live in highly stable environments',
                ],
            },
            {
                'question': 'A dandelion produces ~15,000 seeds per plant with no parental care. A giant tortoise produces 1-4 eggs per year and takes 30 years to mature. According to life-history theory, what underlying trade-off explains this difference?',
                'correct': 'Energy and time devoted to reproduction cannot simultaneously be invested in offspring quality, growth, or maintenance — the dandelion allocates all reproductive investment into quantity, while the tortoise invests heavily in each offspring\'s quality and in its own survival to reproduce repeatedly',
                'distractors': [
                    'The difference is purely taxonomic — dandelions are angiosperms and tortoises are reptiles; life-history differences between plants and animals cannot be explained by the same trade-off logic because they occupy fundamentally different ecological roles',
                    'The difference reflects mutation accumulation — dandelions are annuals with high generation turnover, allowing mutations to accumulate faster and driving faster evolution toward high fecundity; tortoises accumulate few mutations per unit time due to long lifespan',
                    'The difference is primarily driven by body size — larger organisms always evolve lower reproductive rates because metabolic costs scale with body mass, not because of any evolutionary optimization of investment trade-offs',
                ],
            },
            {
                'question': 'A conservationist is comparing two endangered species: Species A matures at age 2 and produces 200 eggs per year (r-selected). Species B matures at age 20 and produces 1 offspring per year (K-selected). If both species have had populations reduced to 50 individuals by habitat loss, which faces greater extinction risk, and why?',
                'correct': 'Species B faces greater extinction risk because its slow recovery rate (1 offspring/yr, 20-yr maturation delay) means the population cannot rebound quickly even if habitat is restored — r-selected Species A can recover much faster from low population size because reproductive rate is high relative to generation time',
                'distractors': [
                    'Species A faces greater extinction risk because r-selected species naturally experience boom-bust population cycles — with only 50 individuals, Species A is in a bust phase and may crash to zero before the next boom, while Species B\'s stable K-strategy makes it resilient at low population densities',
                    'Both face identical extinction risk because extinction probability depends only on population SIZE, not on life-history strategy — any population below 50 individuals has the same probability of going extinct regardless of reproductive rate or generation time',
                    'Species B faces less extinction risk because K-selected species evolved in stable environments where population crashes are rare — their slow reproduction is an evolved response to near-zero extinction risk, so being reduced to 50 individuals is an anomalous condition they are evolutionarily prepared for',
                ],
            },
            {
                'question': 'Iteroparous organisms (reproduce multiple times) vs. semelparous organisms (reproduce once and die, like Pacific salmon). Under what environmental conditions should semelparity be evolutionarily favored over iteroparity?',
                'correct': 'When adult survival rate is low (high extrinsic mortality) AND a single large reproductive episode produces dramatically more offspring than multiple small ones — in high-mortality environments, investing everything in a single massive reproductive effort has higher expected fitness than surviving to reproduce again (which is unlikely)',
                'distractors': [
                    'Semelparity is favored when environments are stable and predictable — semelparous organisms evolved to match their single reproductive event to a predictable resource peak, which requires environmental stability, while unpredictable environments always favor iteroparity',
                    'Semelparity is favored when juveniles have HIGH survival rates — if offspring are very likely to survive, producing large numbers at once is beneficial; when juvenile survival is low, iteroparity is favored to continuously try again with each small brood',
                    'Semelparity is always favored in aquatic organisms because water buoyancy reduces the metabolic cost of egg production — the high mass of Pacific salmon eggs is only possible underwater, making semelparity an ecological constraint of aquatic life rather than an evolved life-history strategy',
                ],
            },
            {
                'question': 'What do the letters "r" and "K" stand for in r/K selection theory?',
                'correct': 'r = the intrinsic rate of population increase in logistic growth models (dN/dt = rN(1-N/K)); K = carrying capacity, the maximum sustainable population size of the environment',
                'distractors': [
                    'r = reproductive rate per year; K = number of offspring per clutch',
                    'r = random mating; K = selective (non-random) mating — the distinction is about mating system',
                    'r = rapid; K = slow — these are descriptive terms for life history pace, not population parameters',
                ],
            },
            {
                'question': 'Why is the r/K framework considered a "continuum" rather than a binary classification?',
                'correct': 'Most real species show a mix of r and K traits and fall somewhere between the extremes — e.g., a medium-sized mammal with moderate offspring numbers and moderate parental care is neither fully r nor fully K. Treating r/K as a binary misrepresents the gradient of life history strategies',
                'distractors': [
                    'The framework is a continuum because all species cycle between r and K strategies seasonally — every species is r-selected in spring and K-selected in fall',
                    'r/K is a continuum because the framework has been replaced by numerical rates (0-100 scale) rather than qualitative categories — there is no meaningful distinction between r and K anymore',
                    'The r/K framework is a strict binary, not a continuum — each species is definitively classified as one or the other based on reproductive rate alone',
                ],
            },
            {
                'question': 'Identify which species is r-selected and which is K-selected: (a) a field mouse with 4 litters per year of 6 pups each, 1-year lifespan; (b) an elephant with 1 calf every 4-6 years, 60-year lifespan.',
                'correct': 'The field mouse is r-selected (high reproductive rate, short lifespan, many small offspring); the elephant is K-selected (low reproductive rate, long lifespan, few large offspring with heavy parental investment)',
                'distractors': [
                    'Both are K-selected because they are mammals — all mammals are K-selected by definition',
                    'The mouse is K-selected because it reproduces multiple times per year (iteroparous); the elephant is r-selected because it has few offspring',
                    'Neither is r or K selected — both fall in the middle of the continuum and the distinction does not apply to vertebrates',
                ],
            },
            {
                'question': 'Which ONE of these is NOT a typical trait of an r-selected species?',
                'correct': 'Heavy parental investment per offspring — r-selected species typically provide LITTLE parental care (the "r" strategy relies on producing many offspring with low individual survival rather than investing heavily in each)',
                'distractors': [
                    'Fast maturation time — r-selected species reach reproductive age quickly',
                    'High fecundity (many offspring) — r-selected species produce many offspring per reproductive event',
                    'Thrives in unstable or unpredictable environments — r-selection is favored where population crashes and recoveries are frequent',
                ],
            },
            {
                'question': 'L1 RECALL: The Adactylidium mite is cited as an extreme life-history case. What is unusual about its reproductive biology?',
                'correct': 'Adactylidium females are born already mature; their brothers inseminate them while still inside the mother; the developing offspring then consume the mother from within, emerging as adults after only about 4 days',
                'distractors': [
                    'Adactylidium females carry eggs for 10 years before laying them',
                    'Adactylidium females live for decades and reproduce only once',
                    'Adactylidium is a hermaphroditic species that self-fertilizes every hour',
                ],
            },
            {
                'question': 'L1 RECALL: Bristlecone pines are cited as an extreme longevity example. Approximately how long can they live?',
                'correct': 'Over 4000 years — some individual bristlecone pines (Pinus longaeva) are among the oldest known non-clonal organisms on Earth, representing the extreme K-selected end of the continuum',
                'distractors': [
                    'About 500 years',
                    'About 100 years',
                    'About 50,000 years',
                ],
            },
            {
                'question': 'L3 APPLICATION: A plant species produces exactly 1 large, well-provisioned seed per year and lives for 200 years before dying. A second species produces 10,000 tiny seeds per year and lives for only 1 year. Which is r-selected and which is K-selected, and what trade-off does the difference illustrate?',
                'correct': 'The 1-seed 200-year plant is K-selected (low fecundity, long life, high per-offspring investment); the 10,000-seed 1-year plant is r-selected (high fecundity, short life, low per-offspring investment). The trade-off is between OFFSPRING NUMBER and OFFSPRING QUALITY — finite resources cannot simultaneously maximize both',
                'distractors': [
                    'Both are K-selected because both are plants and all plants are K-selected by taxonomy',
                    'The 10,000-seed plant is K-selected because it has more total offspring',
                    'The 1-seed plant is r-selected because it invests the same resources in one large seed',
                ],
            },
            {
                'question': 'L5 SYNTHESIS: Integrate the finite-energy constraint, the r/K continuum, and iteroparity vs semelparity into an explanation of why semelparous Pacific salmon (single massive spawning event, then death) are evolutionarily stable despite "wasting" their adult body in one reproductive event.',
                'correct': 'Pacific salmon face EXTREMELY HIGH ADULT MORTALITY from the arduous upstream migration — surviving to a second reproductive event is very unlikely. Because finite energy must be allocated, and because future reproduction is nearly impossible, optimizing CURRENT reproduction by pouring all energy into one massive spawning event produces more lifetime offspring than reserving energy for a second unlikely attempt. Iteroparity would be favored if adult survival were higher. Semelparity + maximum per-event investment is the ESS when adult survival is ~0',
                'distractors': [
                    'Pacific salmon are K-selected species that happen to die after reproduction due to arbitrary developmental programming unrelated to life-history theory',
                    'Semelparity is an evolutionary mistake that will eventually be corrected in Pacific salmon lineages via selection for iteroparity',
                    'Salmon semelparity is driven by group selection for population control',
                ],
            },
        ],
        visual={
            'type': 'continuum',
            'description': 'r-K strategy continuum',
            'regions': [
                {'label': 'r-strategy', 'color': '#ff6b6b', 'items': ['Many small offspring', 'Fast maturation', 'Unstable environments']},
                {'label': 'K-strategy', 'color': '#4ea8de', 'items': ['Few large offspring', 'Slow maturation', 'Stable environments']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'r = reckless; K = careful.',
            'trap': 'r/K is a continuum, not a binary. Most species are somewhere between the extremes.',
        },
        diagram=r_vs_k_compare_diagram(),
    ))
    nodes.append(build_node(
        id='lec12-aging',
        title='Extrinsic Mortality, Aging, & Senescence',
        subtitle='Why organisms age — Medawar and Williams (Lec 12 slides 12-27)',
        color='gray', row=10,
        heading='Lecture 12 — Why Organisms Age',
        sections=[{'label': 'CORE CONCEPT', 'body': 'Extrinsic mortality (random death from predation, accident, disease) causes the FORCE OF SELECTION to decline with age — older individuals are a shrinking fraction of the population so selection on late-life traits is weak. MUTATION ACCUMULATION (Medawar): mutations with only late-life deleterious effects are not efficiently purged by selection because they express only in individuals who have largely already reproduced. ANTAGONISTIC PLEIOTROPY (Williams 1957): a gene with early benefit and late cost is FAVORED because the early benefit is selected strongly while the late cost experiences weak selection. AUSTAD\'S OPOSSUM STUDY: Sepelo Island (Georgia, USA) opossums have lived on a predator-free island for ~5000 years, evolving slower aging than mainland opossums. GARTER SNAKE STUDY at Eagle Lake: "meadow" populations (low predation) mature slowly, produce ~4 babies, and live 8 years; "lake" populations (high predation) mature fast, produce ~8 babies, and live 4 years. REZNICK\'S GUPPY 11-year transplant experiment in Trinidad directly confirmed these predictions: transplanted guppies evolved faster life histories within ~30 generations. About 100,000 people die daily worldwide from age-related diseases.'}] + slides_to_sections(d, (12, 27)),
        examples=[
            'High extrinsic mortality (predators, disease) favors fast reproduction and short lifespan — there\'s no point "saving" resources for old age if you probably won\'t reach it.',
            'Low extrinsic mortality favors slow development and longer lifespan — energy investment in maintenance pays off.',
            'Reznick\'s guppy experiment: high-predation Trinidad populations evolve faster maturation and higher reproductive rates than low-predation populations. Experimentally confirmed in 11 years after transplant.',
            'MEDAWAR\'S THEORY: mutations with late-life harmful effects escape selection because most individuals die before expressing them.',
            'WILLIAMS\' antagonistic pleiotropy theory: genes beneficial early in life can be maintained even if harmful later.',
        ],
        warnings=[
            'Aging is NOT inevitable — some organisms (hydra, certain clams, lobsters) show negligible senescence because their force of selection does not decline with age.',
        ],
        mnemonic='MEDI = Mutation accumulation + Extrinsic mortality → Declining selection → Inevitable aging.',
        flashcard={
            'front': 'Why does high extrinsic mortality favor the evolution of shorter lifespans and earlier reproduction?',
            'back': 'EXTRINSIC MORTALITY = death from environmental sources (predation, disease, accidents, starvation) that are NOT age-related. When extrinsic mortality is HIGH, few individuals survive to old age regardless of their biology — so selection for traits that extend life has little effect (because the life extension never happens before extrinsic death). Instead, selection strongly favors EARLY, RAPID REPRODUCTION to pass on genes before random death strikes. GUPPY EXPERIMENTS (Reznick et al.): In Trinidad streams, guppies below waterfalls face predation from pike cichlids (high extrinsic mortality) and evolve FAST maturation and HIGH reproductive rates. Guppies above waterfalls face killifish (low extrinsic mortality) and evolve SLOW maturation and LOWER reproductive rates. When Reznick experimentally transplanted low-predation guppies to high-predation sites, within 11 years (roughly 30 guppy generations) they evolved the fast life history of native high-predation fish. This is a textbook demonstration that extrinsic mortality shapes life history evolution.',
        },
        quiz=[
            {
                'question': 'Reznick\'s guppy transplant experiment showed that after 11 years in high-predation streams, guppies evolved:',
                'correct': 'Faster maturation and earlier, higher reproductive rates',
                'distractors': [
                    'Longer lifespans and delayed reproduction',
                    'Increased body size and reduced fertility',
                    'No detectable evolutionary change',
                ],
            },
            {
                'question': 'Reznick\'s team transplanted LOW-predation guppies into HIGH-predation streams and observed evolution within 11 years (~30 generations). They also raised guppies from each population in COMMON GARDEN lab conditions and still found the differences. Why was the common garden experiment essential?',
                'correct': 'Without common garden, the life-history differences observed in high-predation streams could reflect phenotypic plasticity (individuals responding to predators) rather than genetic evolution — common garden conditions eliminate environmental differences, confirming that the divergence is heritable (genetic) rather than plastic',
                'distractors': [
                    'The common garden experiment was needed to confirm that the Pike cichlid was the selective agent — by raising guppies without predators and measuring their life-history traits, the team confirmed that the cichlid itself, not some correlated environmental variable, caused the evolutionary change',
                    'Common garden conditions were needed to boost guppy generation time — wild guppies in fast-flowing streams have extended generation times, so lab conditions were required to get the ~30 generations needed within the 11-year study period',
                    'The common garden was used to measure heritability of life-history traits using parent-offspring regression — without this step, the researchers could not apply the breeders equation to predict whether 30 generations was sufficient to produce the observed evolutionary response',
                ],
            },
            {
                'question': 'Medawar\'s mutation accumulation theory and Williams\'s antagonistic pleiotropy theory both explain aging. For an exam question, how would you distinguish which is operating in a given case?',
                'correct': 'Mutation accumulation predicts that late-acting genes have only deleterious effects (no early benefit) — their persistence is due to the declining force of selection at old ages. Antagonistic pleiotropy predicts late-acting genes also have early BENEFICIAL effects — removing them would reduce early fitness. Experimentally: delete a candidate aging gene and check whether early-life fitness decreases (AP) or stays the same (mutation accumulation)',
                'distractors': [
                    'They cannot be distinguished because both theories predict identical outcomes: late-acting deleterious alleles maintained at higher frequency than expected from mutation-selection balance alone — the only distinguishing criterion is the theoretical framework used, not empirical data',
                    'Mutation accumulation operates in high-extrinsic-mortality environments while antagonistic pleiotropy operates in low-extrinsic-mortality environments — you distinguish them by measuring the survival rate of juveniles rather than by examining gene effects',
                    'Antagonistic pleiotropy applies only to genes with large effect sizes (s > 0.1), while mutation accumulation applies to small-effect alleles (s < 0.01) — you distinguish them by measuring the selection coefficient of each late-acting deleterious gene',
                ],
            },
            {
                'question': 'Some species show negligible senescence — they do not show increasing mortality with age (e.g., hydra, Greenland sharks, some clams). How does this observation relate to Williams\'s antagonistic pleiotropy theory and Medawar\'s theory?',
                'correct': 'Negligible senescence is consistent with both theories when the force of selection remains HIGH throughout life — in clonal organisms like hydra (where reproduction continues indefinitely) or extremely slow-growing organisms in low-extrinsic-mortality environments, selection against late-life deleterious alleles remains strong rather than declining with age',
                'distractors': [
                    'Negligible senescence DISPROVES both theories — if some organisms do not age, then aging cannot be an evolutionary inevitability; the existence of non-aging organisms means aging must be due to a specific degenerative disease process rather than the declining force of natural selection',
                    'Negligible senescence in clonal organisms proves Lamarckian inheritance — hydra have maintained perfect genome integrity across hundreds of clonal generations because environmental signals that would cause somatic damage are repaired and the repaired sequences are inherited, preventing senescence',
                    'Negligible senescence proves that mutation accumulation is the correct theory while antagonistic pleiotropy is wrong — if some organisms can live without aging, no organism needs antagonistically pleiotropic genes; those organisms simply evolved away from having them, while aging species were stuck with them due to developmental constraints',
                ],
            },
            {
                'question': 'In Reznick\'s guppy studies, what species was the HIGH-predation predator below waterfalls and the LOW-predation predator above waterfalls?',
                'correct': 'Pike cichlids (Crenicichla) preyed heavily on adult guppies below waterfalls creating high extrinsic mortality; killifish (Rivulus) above the waterfalls preyed only on juvenile guppies creating low adult extrinsic mortality',
                'distractors': [
                    'Piranhas (below) and tetras (above) — these were the ancestral predators that shaped guppy life histories',
                    'Herons (below) and kingfishers (above) — avian predators dominated both habitats',
                    'Electric eels (below) and frogs (above) — these aquatic predators created the mortality gradient Reznick measured',
                ],
            },
            {
                'question': 'The KEY prediction of Medawar\'s mutation accumulation theory of aging is about the "force of selection." What does this phrase mean?',
                'correct': 'The force of selection DECLINES with age because an increasing fraction of the population has already died (from any cause) by older ages, so selection acting on late-life traits affects fewer individuals and has less power to purge deleterious mutations that only manifest late in life',
                'distractors': [
                    'The force of selection is a physical force that pushes old individuals toward death — aging is an active process driven by selection itself',
                    'The force of selection refers to the strength of natural selection in the environment, which varies geographically but not with age',
                    'Force of selection means the rate at which mutations arise in germline vs. somatic cells, with germline selection being stronger in young individuals',
                ],
            },
            {
                'question': 'Which statement most accurately characterizes the relationship between aging and natural selection?',
                'correct': 'Aging is NOT programmed by selection — it emerges as an unintended consequence of weakened selection at older ages, either through mutation accumulation (Medawar) or through antagonistic pleiotropy (Williams). There is no "aging gene" evolved "for" killing old individuals',
                'distractors': [
                    'Aging is an evolved "death program" that has been selected to remove old individuals so younger ones can have more resources — this is a form of group selection favoring population turnover',
                    'Aging is purely entropy — it is a physical law of thermodynamics and has no evolutionary explanation',
                    'Aging is an adaptation selected to promote genetic turnover and speed up evolution — species that age evolve faster than non-aging species',
                ],
            },
            {
                'question': 'A gene that codes for strong testosterone response in young male humans increases muscle mass and aggression (beneficial for competing for mates) but also increases prostate cancer risk after age 60. This is a classic example of:',
                'correct': 'Antagonistic pleiotropy (Williams) — the same gene has opposing fitness effects at different life stages, and because early-life benefits come before late-life costs, the allele is maintained by selection despite the late-life harm',
                'distractors': [
                    'Mutation accumulation (Medawar) — the late-life harmful effect escapes selection because few individuals reach old age',
                    'Heterozygote advantage — the gene is maintained because heterozygotes have intermediate testosterone levels with optimal fitness',
                    'Mutation-selection balance — the late-life cost creates weak selection against the allele, but high mutation rate reintroduces it each generation',
                ],
            },
            {
                'question': 'L1 RECALL: Where did Steven Austad conduct his famous opossum study on island vs mainland aging differences?',
                'correct': 'Sepelo Island, Georgia — Austad compared opossums on this predator-free island (inhabited ~5000 years) to mainland populations and found island opossums show slower aging consistent with reduced extrinsic mortality',
                'distractors': [
                    'Galápagos Islands — Austad studied opossum descendants of Darwin\'s Beagle visit',
                    'Madagascar — where Austad compared lemurs and opossums',
                    'Santa Catalina Island — off the California coast',
                ],
            },
            {
                'question': 'L1 RECALL: In the Eagle Lake garter snake aging study, how did the "lake" vs "meadow" populations differ in reproduction and lifespan?',
                'correct': 'LAKE (high predation): fast maturation, ~8 babies per clutch, ~4 year lifespan. MEADOW (low predation): slow maturation, ~4 babies per clutch, ~8 year lifespan. This mirrors the r/K trade-off and confirms extrinsic mortality shapes life-history evolution',
                'distractors': [
                    'Both populations had identical reproductive output and lifespan',
                    'Lake snakes had fewer babies and longer lifespans than meadow snakes',
                    'Meadow snakes had fewer babies and shorter lifespans than lake snakes',
                ],
            },
            {
                'question': 'L5 SYNTHESIS: The Medawar and Williams theories of aging are OFTEN PRESENTED AS ALTERNATIVES but actually address different but compatible mechanisms. Integrate them into a unified explanation of why aging is nearly universal but not inevitable.',
                'correct': 'MEDAWAR explains why DELETERIOUS late-acting mutations accumulate unpurged — the force of selection weakens with age. WILLIAMS adds that some late-acting harmful alleles are not merely tolerated but ACTIVELY FAVORED because of early-life benefits (antagonistic pleiotropy). Both mechanisms operate simultaneously in most species. Aging is NEARLY universal because most species have some extrinsic mortality, producing a declining force of selection; but it is NOT inevitable in species where the force of selection remains high throughout life (hydra, some clams, lobsters) because of indefinite growth, clonal reproduction, or sheltered environments. Aging is thus emergent, not programmed',
                'distractors': [
                    'Medawar and Williams are mutually exclusive — only one can be correct in any given species',
                    'Both theories have been disproven by the existence of non-aging species',
                    'Aging is a programmed death mechanism selected by group selection regardless of extrinsic mortality',
                ],
            },
            {
                'question': 'L4 ANALYSIS: A colony of hydra has been kept in the lab for over a decade with no increase in individual mortality rate and no detectable senescence. Why does this NOT violate the evolutionary theory of aging?',
                'correct': 'Hydra reproduce clonally by budding and grow indefinitely — their "soma" and "germline" are not clearly separated, and the force of selection on their biology does NOT decline with age because every part of the hydra is effectively a germ cell. Evolutionary aging theory predicts aging arises when the force of selection declines; hydra avoid this because their reproductive mode keeps the force of selection constant',
                'distractors': [
                    'Hydra violate the theory by showing aging cannot be universal — the theory must therefore be wrong',
                    'Hydra are an artifact of lab conditions and do in fact senesce in the wild',
                    'Hydra are special exceptions explained by the absence of mitochondria',
                ],
            },
        ],
        visual={
            'type': 'comparison',
            'description': 'Mortality regime shapes life history',
            'regions': [
                {'label': 'High extrinsic mortality', 'color': '#ff6b6b', 'items': ['Fast maturation', 'Early reproduction', 'Short lifespan', 'e.g., high-predation guppies']},
                {'label': 'Low extrinsic mortality', 'color': '#4ea8de', 'items': ['Slow maturation', 'Late reproduction', 'Long lifespan', 'e.g., low-predation guppies']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Dangerous world → live fast. Safe world → live slow.',
            'trap': 'Aging is not "programmed" — it emerges from weakened selection at older ages, not from an evolved death program.',
        },
    diagram=life_history_r_k_timeline_diagram(),
    ))
    nodes.append(build_node(
        id='lec12-sex-allocation',
        title='Parental Investment & Sex Allocation',
        subtitle='When to invest in which sex (Lec 12 slides 28-41)',
        color='pink', row=10,
        heading='Lecture 12 — Parental Investment and Sex Allocation',
        sections=[{'label': 'CORE CONCEPT', 'body': 'PARENTAL INVESTMENT (Trivers 1972) = any contribution by a parent to one offspring that increases the offspring\'s survival at the cost of the parent\'s ability to invest in other offspring. SEX ROLE REVERSAL examples: wattled jacana (males incubate eggs, females defend territories) and syngnathid fish (pipefish, seahorses — males brood eggs in pouches). FLEXIBLE ALLOCATION: in humans, ~90% of miscarriages involve chromosomally abnormal embryos (quality-control allocation); sand goby males sometimes eat their own eggs when conditions are poor. FISHER\'S PRINCIPLE (R.A. Fisher 1930, Genetical Theory of Natural Selection): at equilibrium, parents invest equally in male and female offspring. If males are rare, each male gains disproportionate reproductive success, so producing sons pays — selection shifts the ratio until investment is equal. TRIVERS-WILLARD HYPOTHESIS (1973): high-condition mothers should overproduce SONS (in polygynous species, high-quality sons reap disproportionate rewards); low-condition mothers should overproduce DAUGHTERS (safer reproductive returns). WARNER et al. (2007) confirmed this in lizards. SEYCHELLES WARBLER (Komdeur 1997): females in high-quality territories overproduce female helpers (daughters help raise siblings), females in low-quality territories overproduce male dispersers (sons leave).'}] + slides_to_sections(d, (28, 41)),
        examples=[
            'Parental investment: any contribution of resources or time to one offspring that reduces the parent\'s ability to invest in others.',
            'Sex role reversal: pipefish and seahorses — males carry offspring in brood pouches; females compete for male mates.',
            'Female-biased operational sex ratios create male choice and female competition.',
            'Fisher\'s principle: at equilibrium, parents should invest equally in males and females. If one sex is rare, selection favors producing more of it.',
            'Trivers-Willard: parents in good condition should invest in sons (in species where male RS depends on condition); poor-condition parents should invest in daughters (safer reproductive return).',
        ],
        warnings=[
            'Fisher predicts equal INVESTMENT, not equal numbers. If sons cost 2× more to produce, expect a 2:1 daughter:son ratio at birth — equal investment with unequal counts.',
            'Trivers-Willard applies only when male reproductive success is MORE condition-dependent than female RS. In species where female RS is equally condition-dependent, the effect weakens or disappears.',
        ],
        mnemonic='Fisher says 50/50. Trivers-Willard says adjust by condition.',
        flashcard={
            'front': 'State Fisher\'s principle of sex allocation and explain why the equilibrium sex ratio is 1:1.',
            'back': 'FISHER\'S PRINCIPLE (R.A. Fisher 1930): at evolutionary equilibrium, parents should invest equally in male and female offspring, which produces (roughly) a 1:1 SEX RATIO at sexual maturity. REASONING: Suppose males become rare. Each male then has higher mating success than each female (because there are fewer males to share the females). Parents who happen to produce more sons gain a fitness advantage because their sons have higher per-capita reproductive success. Selection favors producing more sons, UNTIL males stop being rare. The reverse applies if females become rare. The only STABLE (evolutionarily stable strategy) equilibrium is when producing either sex yields equal expected fitness returns — which happens when the SEX RATIO is 1:1 (weighted by INVESTMENT cost, not counts, if sexes are unequally costly). This explains why most species with genetic sex determination produce ~50/50 sex ratios despite the apparent waste of producing "surplus" males.',
        },
        quiz=[
            {
                'question': 'In a pipefish species where males carry offspring in a brood pouch and females compete for males, who is expected to be the choosier sex?',
                'correct': 'Males, because they invest more per offspring and have limited brood capacity',
                'distractors': [
                    'Females, because they produce eggs',
                    'Neither — pipefish mate randomly',
                    'Both are equally choosy',
                ],
            },
            {
                'question': 'Fisher\'s principle predicts a 1:1 sex ratio at evolutionary equilibrium. In some Hymenoptera (ants, bees, wasps), queens can control offspring sex ratio by choosing whether to fertilize eggs. If sons are currently rare (and thus have higher reproductive value), what does Fisher\'s principle predict the queen should do, and why?',
                'correct': 'Produce more sons until the sex ratio returns to equal INVESTMENT — Fisher\'s principle is frequency-dependent: when males are rare, each male sires more offspring on average than each female, so parents who produce more sons leave more grandchildren; this advantage disappears when the sex ratio returns to the investment-equal equilibrium',
                'distractors': [
                    'Produce more daughters permanently — in eusocial Hymenoptera, daughters (workers and future queens) always have higher inclusive fitness than sons because haplodiploidy makes sisters more related to each other than to their offspring, so daughters are always the optimal sex to produce',
                    'Maintain a fixed 1:1 sex ratio at all times regardless of current male rarity — Fisher\'s principle is an evolutionarily stable strategy that cannot be invaded by any alternative, so any queen that responds to male rarity is adopting an inferior strategy',
                    'Produce only daughters when males are rare, because the scarcity of males means fertilized eggs (daughters) are more likely to find mates — queens should produce more of the sex that benefits from rare opposite-sex mating partners, which is daughters when males are rare',
                ],
            },
            {
                'question': 'Trivers-Willard theory predicts that high-condition mothers in polygynous mammals should bias offspring sex ratios toward sons. What is the MECHANISM linking maternal condition to fitness return from sons vs. daughters?',
                'correct': 'In polygynous species, high-quality males monopolize many matings while low-quality males reproduce little — so a son\'s reproductive success is more CONDITION-DEPENDENT than a daughter\'s. High-condition mothers produce high-condition offspring, and this condition advantage translates into disproportionately higher reproductive success for sons than daughters, making sons the better investment for high-condition mothers',
                'distractors': [
                    'High-condition mothers bias toward daughters because daughters can benefit from maternal resources through extended lactation and social learning — mothers in good condition can afford the larger investment that daughters require because daughters stay in the social group while sons disperse',
                    'High-condition mothers produce more sons because sons are physiologically cheaper to produce — male embryos require less glucose and fewer hormones to develop, so high-condition mothers with more resources can afford the "waste" of producing the cheaper sex',
                    'Trivers-Willard applies only when there is a strict 1:1 sex ratio requirement — in species where sex ratios are already skewed, the condition effect disappears because Fisher\'s principle overrides parental condition effects on sex allocation',
                ],
            },
            {
                'question': 'In a monogamous bird species where both parents provide equal care and extrinsic mortality is identical for both sexes, what mating system components does Fisher\'s principle predict, and how would the parental investment prediction change if one parent died, leaving single-parent broods?',
                'correct': 'Equal investment predicts a 1:1 sex ratio at hatching. If one parent dies and single-parent care becomes common, selection would favor producing the sex that requires less care (typically smaller bodies or faster independence), because that sex has lower cost and similar reproductive return — shifting the optimal sex ratio slightly toward the lower-cost sex',
                'distractors': [
                    'Fisher\'s principle predicts that surviving parents should overproduce the sex they CAN successfully raise alone — because survival of the higher-investment sex (requiring two parents) is compromised by single parenting, the remaining parent should switch entirely to producing the hardier sex',
                    'A parent death has no effect on sex ratio predictions — Fisher\'s principle applies across the entire population level and not to individual families; individual variation in parental death cannot systematically shift population-level sex ratios',
                    'Fisher\'s principle predicts that after a parent death, the surviving parent should abandon the brood and re-mate quickly — the optimal strategy is to maximize future reproduction rather than invest in potentially lower-quality single-parent offspring',
                ],
            },
            {
                'question': 'Fisher published his principle of sex allocation in what year, and what was the key rationale?',
                'correct': '1930 — in "The Genetical Theory of Natural Selection." Fisher argued that the rarer sex has higher per-capita reproductive success, so selection favors producing that sex until the ratio returns to equal INVESTMENT (usually 1:1 in count if sexes are equally costly)',
                'distractors': [
                    '1859 — in "On the Origin of Species." Darwin himself first articulated the principle and Fisher merely formalized it',
                    '1964 — in "The Genetical Evolution of Social Behaviour." Fisher derived sex allocation as a corollary of Hamilton\'s rule',
                    '1975 — in a paper on the handicap principle. Zahavi and Fisher collaborated on both sex allocation and costly signaling theory',
                ],
            },
            {
                'question': 'Parental investment is defined (Trivers 1972) as:',
                'correct': 'Any contribution by a parent to one offspring that INCREASES that offspring\'s survival (and thus reproductive success) at the COST of the parent\'s ability to invest in other current or future offspring — it is a zero-sum trade-off with lifetime reproductive output',
                'distractors': [
                    'The total energy a parent spends on reproduction summed across all offspring — parental investment is measured as a total, not per offspring',
                    'The gender-specific investment a male or female parent makes in offspring — parental investment is defined by the sex of the parent',
                    'The number of offspring a parent produces — more offspring = more investment, regardless of per-offspring cost',
                ],
            },
            {
                'question': 'An OPERATIONAL sex ratio (OSR) refers to what, and how does it differ from a population sex ratio?',
                'correct': 'OSR is the ratio of sexually receptive/available males to sexually receptive females at a given time — it may differ from the overall population sex ratio if one sex has a longer receptive window. A male-biased OSR intensifies competition among males; a female-biased OSR leads to male choice',
                'distractors': [
                    'OSR is the ratio of fertile males to infertile males — it tracks male reproductive health across populations',
                    'OSR is the physiological readiness ratio — it measures only hormone levels, not actual mating availability',
                    'OSR and population sex ratio are identical by definition — any differences are statistical sampling errors',
                ],
            },
            {
                'question': 'If a parent bird produces a clutch in which sons are twice as energetically costly to raise as daughters, Fisher\'s principle predicts what sex ratio at fledging?',
                'correct': '2 daughters per 1 son — Fisher\'s principle is about equal INVESTMENT, not equal numbers. With sons costing 2x more, producing twice as many daughters equalizes total investment in each sex',
                'distractors': [
                    '1:1 ratio — Fisher\'s principle always predicts equal numbers regardless of cost',
                    '1 daughter per 2 sons — if sons are more expensive they are more valuable and should be overproduced',
                    '3 daughters per 1 son — because sons are more expensive, they should be minimized entirely',
                ],
            },
            {
                'question': 'L1 RECALL: Jan Komdeur\'s 1997 study on Seychelles warblers showed adaptive sex-ratio adjustment based on territory quality. How did territory quality affect sex ratios?',
                'correct': 'Females in HIGH-quality territories overproduced FEMALE offspring (who stay and help raise siblings, increasing indirect fitness); females in LOW-quality territories overproduced MALE offspring (who disperse to better territories). This is a classic example of adaptive sex allocation beyond Fisher\'s baseline',
                'distractors': [
                    'Seychelles warblers always produced 1:1 sex ratios regardless of territory quality',
                    'High-quality territories overproduced males; low-quality territories overproduced females — the opposite of what occurred',
                    'Komdeur found no relationship between territory quality and offspring sex ratio',
                ],
            },
            {
                'question': 'L1 RECALL: In what species did Warner et al. (2007) demonstrate support for the Trivers-Willard hypothesis?',
                'correct': 'A lizard — Warner and colleagues showed that female lizards in better condition produced offspring sex ratios biased toward sons, consistent with Trivers-Willard predictions',
                'distractors': [
                    'Red deer — the original Trivers-Willard test organism',
                    'Drosophila — a lab test of Trivers-Willard',
                    'Japanese macaques — the only primate test',
                ],
            },
            {
                'question': 'L3 APPLICATION: A wattled jacana is a sex-role-reversed bird in which males incubate eggs and defend nests while females compete for males. Given Trivers\' parental investment framework, what predictions follow about (a) who is choosier, (b) who has larger body size, and (c) who has more elaborate displays?',
                'correct': '(a) MALES are choosier because they invest more per offspring. (b) FEMALES are typically LARGER than males because they compete with other females for access to males — sexual selection on size is reversed. (c) FEMALES have more elaborate displays (colorful wattles, loud calls) because the usual male-ornamentation is reversed along with the limiting-sex roles. All three reversals follow from the reversed investment pattern',
                'distractors': [
                    'All three patterns match typical birds because wattled jacanas are not actually sex-role reversed',
                    'Only sex choosiness is reversed — body size and ornaments remain typical',
                    'Males are both choosier and larger — the reversal is only partial',
                ],
            },
            {
                'question': 'L5 SYNTHESIS: A student asks why Trivers-Willard predicts high-condition mothers should overproduce SONS. Build a complete mechanistic explanation using polygyny, condition-dependence of male reproductive success, and the limiting-sex concept.',
                'correct': 'In polygynous species, HIGH-CONDITION MALES monopolize many mates while LOW-CONDITION MALES may fail to mate at all — so male reproductive success is HIGHLY CONDITION-DEPENDENT. Female reproductive success is less condition-dependent (females produce similar numbers of offspring regardless of condition, up to resource limits). High-condition mothers produce high-condition offspring. Because male RS rewards disproportionately depend on condition, a high-condition son gains FAR MORE reproductive return than a high-condition daughter — so investing in sons has higher expected fitness for high-condition mothers. Low-condition mothers do the reverse: their sons would likely fail as adults, while their daughters will still produce some offspring, so daughters are safer',
                'distractors': [
                    'High-condition mothers should overproduce daughters because daughters require more resources',
                    'The Trivers-Willard prediction is purely empirical with no mechanistic basis',
                    'High-condition mothers should overproduce sons because sons have higher mutation rates and benefit from fitness insurance',
                ],
            },
        ],
        visual={
            'type': 'principle',
            'description': 'Sex allocation principles',
            'regions': [
                {'label': 'Fisher', 'color': '#4ea8de', 'items': ['1:1 investment', 'Frequency-dependent', 'Stable equilibrium']},
                {'label': 'Trivers-Willard', 'color': '#7de2d1', 'items': ['Adjust by condition', 'Good parents → sons', 'Poor parents → daughters']},
                {'label': 'Role reversal', 'color': '#ffc857', 'items': ['Pipefish, seahorses', 'Males invest more', 'Females compete']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Fisher = baseline. Trivers-Willard = condition. Pipefish = reverse.',
            'trap': 'Fisher\'s principle is about INVESTMENT not COUNT. If males are cheaper to produce, more males are expected.',
        },
    ))
    return nodes


def lec13_nodes():
    d = load_lec('lec13')
    nodes = []
    nodes.append(build_node(
        id='lec13-ess-game',
        title='Game Theory & Evolutionarily Stable Strategies',
        subtitle='ESS, hawk-dove, frequency-dependent selection (Lec 13 slides 1-7)',
        color='purple', row=11,
        heading='Lecture 13 — Evolutionary Game Theory',
        sections=[{'label': 'CORE CONCEPT', 'body': 'An EVOLUTIONARILY STABLE STRATEGY (ESS) is a strategy that, once common, cannot be invaded by an alternative strategy introduced at low frequency. Game theory is essential because fitness payoffs are FREQUENCY-DEPENDENT — your fitness depends on what others are doing. Classic example: side-blotched lizards (Uta stansburiana) with orange (bully)/blue (guarder)/yellow (sneaker) throat morphs form a ROCK-PAPER-SCISSORS dynamic where NONE of the three morphs is an ESS alone — the stable state requires all three coexisting at oscillating frequencies. HAWK-DOVE GAME (Maynard Smith 1973, with George Price): hawks escalate contests (risk injury); doves display but never fight (share or retreat). At rare hawk frequency, hawks win (invasion succeeds); at common hawk frequency, hawks mostly fight other hawks and pay injury costs. This produces a MIXED ESS — some hawks, some doves, at a specific equilibrium frequency determined by the ratio of resource value (V) to injury cost (C). INDIVIDUAL vs GROUP SELECTION: individual selection wins because a "selfish" mutation invades any "cooperative" group.'}] + slides_to_sections(d, (1, 7)),
        examples=[
            'ESS: a strategy that, if adopted by most of the population, cannot be invaded by a rare alternative.',
            'Hawk-Dove game (Maynard Smith 1973): hawks fight for resources, doves share. At equilibrium, a mixed population of hawks and doves is stable.',
            'Rock-paper-scissors dynamics: side-blotched lizards with orange/yellow/blue throat morphs maintained by negative frequency-dependent selection.',
            'Game theory assumes frequency-dependent payoff — your fitness depends on what others are doing.',
        ],
        warnings=[
            'ESS is not necessarily the BEST in absolute fitness terms — it is STABLE against invasion. An all-doves population would have higher total fitness than the ESS mixed population, but all-doves is not stable because a rare hawk mutant invades.',
            'ESS can be a PURE strategy (always hawk) OR a MIXED strategy (60% hawk, 40% dove, or each individual plays hawk with probability 0.6). Both are valid ESSs.',
        ],
        mnemonic='ESS = Evolutionarily Stable Strategy. Stable = can\'t be invaded.',
        flashcard={
            'front': 'What is an Evolutionarily Stable Strategy (ESS) and why can a population of hawks-only or doves-only NOT be an ESS in the Hawk-Dove game?',
            'back': 'An EVOLUTIONARILY STABLE STRATEGY (ESS; Maynard Smith & Price 1973) is a strategy that, once common in a population, CANNOT be invaded by any rare alternative mutant strategy — that is, a rare mutant playing something different has LOWER fitness than the common strategy. HAWK-DOVE GAME: Hawks always fight over resources (high win-or-lose payoff). Doves always share/retreat (low but safe payoff). (1) PURE HAWK POPULATION: Every contest results in a fight, so every hawk suffers expected injury. A rare DOVE mutant avoids all fights and gets lower but consistent payoff — sometimes higher than the hawks. So Dove INVADES — hawk-only is NOT an ESS. (2) PURE DOVE POPULATION: Every contest is shared peacefully. A rare HAWK mutant takes all resources without competition and has much higher fitness than doves. Hawk INVADES — dove-only is NOT an ESS. (3) MIXED EQUILIBRIUM: At a specific ratio of hawks to doves, both strategies have equal expected fitness, and neither can invade. This mixed ratio IS the ESS — and shows how multiple strategies can coexist within a single species.',
        },
        quiz=[
            {
                'question': 'Why are side-blotched lizards (with orange, yellow, and blue throat morphs) maintained in a rock-paper-scissors pattern?',
                'correct': 'Negative frequency-dependent selection — each morph is favored when the morph it beats is common',
                'distractors': [
                    'Random mutation constantly generates new morphs',
                    'Genetic drift randomly shifts morph frequencies',
                    'The environment changes each year',
                ],
            },
            {
                'question': 'In the Hawk-Dove game, the ESS is a mixed population with both hawks and doves. If the resource value V = 10 fitness units and injury cost C = 20 fitness units, what proportion of hawks is the ESS?',
                'correct': 'V/C = 10/20 = 0.5 — in the ESS mixed population, 50% are hawks and 50% are doves, because at this frequency the expected payoffs for both strategies are equal and neither can increase in frequency',
                'distractors': [
                    'C/V = 20/10 = 2.0 — but since a frequency cannot exceed 1.0, all individuals should be hawks; injury cost larger than resource value means hawks are always superior when they can win larger contests',
                    '100% doves — because C > V, fighting is never worth it on average, so selection always drives the population to all-dove regardless of current frequencies',
                    'V/(V+C) = 10/30 ≈ 0.33 — one-third hawks, two-thirds doves, because the ESS is determined by the fraction of fights that result in injury, not by the ratio V/C',
                ],
            },
            {
                'question': 'An ESS is described as "stable against invasion by rare mutants." If a new "bourgeois" strategy evolves in the Hawk-Dove game (bourgeois = fight if you are the owner, retreat if you are the intruder), under what conditions could bourgeois INVADE the ESS mixed population?',
                'correct': 'If the contest can be reliably resolved by ownership status (residents have an advantage), bourgeois can invade because it wins contests as a resident at no injury cost and avoids injury as an intruder — it gets the resource often but at lower cost than a pure hawk, producing higher expected payoff than the hawk-dove ESS',
                'distractors': [
                    'Bourgeois cannot invade any ESS by definition — an ESS is mathematically stable and no strategy can invade it regardless of its properties; the only way to escape an ESS is through a change in the underlying payoff values',
                    'Bourgeois can invade only if it completely replaces hawks — partial invasion is impossible because frequency-dependent payoffs always restore the original hawk-dove equilibrium unless the invader goes to fixation within one generation',
                    'Bourgeois invades when V > C — when the resource is worth more than the injury cost, all strategies that contest resources are equivalent, and bourgeois only spreads by drift rather than by any intrinsic strategic advantage over hawk-dove mixing',
                ],
            },
            {
                'question': 'Frequency-dependent selection maintains multiple strategies (ESS) in populations. How does frequency-dependent maintenance of variation differ from heterozygote advantage (overdominance) as a mechanism for maintaining genetic polymorphism?',
                'correct': 'Frequency-dependence operates when the fitness of a genotype depends on its FREQUENCY — rare morphs are favored, common ones are disadvantaged. Overdominance (heterozygote advantage) operates regardless of frequency — heterozygotes always have higher fitness than EITHER homozygote regardless of allele frequencies; both maintain variation but through fundamentally different selection dynamics',
                'distractors': [
                    'They are the same mechanism with different names — any polymorphism maintained by selection involves heterozygote advantage, because only heterozygotes carry both alleles simultaneously and must therefore experience a fitness advantage to maintain both alleles',
                    'Frequency-dependence requires multiple alleles at multiple loci, while overdominance works with only two alleles at a single locus — this is the only structural difference; the population-level outcome (maintained polymorphism) is identical for both mechanisms',
                    'Overdominance maintains polymorphism at a single stable equilibrium point, while frequency-dependent selection maintains polymorphism by cycling through frequencies indefinitely without ever reaching a stable equilibrium — only overdominance can produce a true equilibrium',
                ],
            },
            {
                'question': 'Who introduced the concept of the Evolutionarily Stable Strategy, and in what year?',
                'correct': 'John Maynard Smith and George Price, 1973 — their foundational paper "The Logic of Animal Conflict" in Nature established ESS as a central concept in evolutionary game theory',
                'distractors': [
                    'John Nash, 1950 — the ESS is another name for the Nash equilibrium from non-cooperative game theory',
                    'R.A. Fisher, 1930 — Fisher first proposed ESS as part of his sex allocation theorem',
                    'W.D. Hamilton, 1964 — Hamilton derived ESS as part of his inclusive fitness framework',
                ],
            },
            {
                'question': 'In the Hawk-Dove game, what is the payoff for Dove vs. Dove encounter?',
                'correct': 'Doves share the resource — each gets V/2 (half the resource value) with no injury cost. This is a peaceful, low-payoff but also low-cost interaction',
                'distractors': [
                    'Doves fight briefly with reduced injury — each gets (V-C)/4 as a reduced version of the hawk-hawk interaction',
                    'Doves both retreat and get 0 — the encounter produces no payoff for either individual',
                    'One dove randomly gets V and the other gets 0 — doves resolve conflicts by random chance rather than sharing',
                ],
            },
            {
                'question': 'A MIXED ESS can mean two things: a mixed population (some hawks, some doves) OR a mixed strategy (each individual plays hawk part of the time, dove the rest). How do these differ mathematically at equilibrium?',
                'correct': 'Both can produce the same equilibrium frequencies of hawk and dove plays. In a mixed POPULATION, different individuals play pure strategies with the proportions of hawks and doves matching the ESS frequency. In a mixed STRATEGY, each individual plays hawk with probability p and dove with probability 1-p, where p equals the ESS frequency. The game-theoretic predictions are identical, but the underlying genetic architecture differs',
                'distractors': [
                    'Mixed populations are ESS only with discrete genetic determination, while mixed strategies require continuous genetic variation — the two are mutually exclusive forms of polymorphism',
                    'Mixed populations produce stable equilibria while mixed strategies produce oscillations — only one is a true ESS at any given time',
                    'Mixed populations and mixed strategies are identical terms — there is no meaningful distinction in game theory literature',
                ],
            },
            {
                'question': 'In the side-blotched lizard rock-paper-scissors system, which male morph beats which?',
                'correct': 'Orange-throat beats blue-throat (orange is highly aggressive and takes blue territories); blue-throat beats yellow-throat (blue mate-guards and stops yellow sneakers); yellow-throat beats orange-throat (yellow mimics females and sneaks matings past orange, who holds too large a territory to guard effectively)',
                'distractors': [
                    'Orange beats yellow, yellow beats blue, blue beats orange — the opposite direction of the actual system',
                    'All three morphs are equally matched in pairwise contests — the rock-paper-scissors label is metaphorical rather than literal',
                    'Blue always wins because it is the most aggressive; yellow and orange coexist at lower frequencies due to drift',
                ],
            },
            {
                'question': 'What does it mean to say an ESS is stable "against invasion by a rare mutant"?',
                'correct': 'If the population plays the ESS and a new mutant strategy arises at very low frequency, the mutant will have LOWER fitness than the resident ESS strategy and will not spread — the resident strategy cannot be displaced by any rare alternative, which is the formal definition of evolutionary stability',
                'distractors': [
                    'Stability means the strategy cannot be changed by any process — mutation, drift, selection, and environmental change are all prevented',
                    'Stability requires that mutants go extinct within a single generation — any strategy that allows mutants to persist at all is not truly stable',
                    'Stability means the mutant will always increase in frequency — ESS attracts alternative strategies that converge on it',
                ],
            },
            {
                'question': 'L5 SYNTHESIS: Derive WHY the side-blotched lizard rock-paper-scissors system CANNOT settle into a single-morph ESS, integrating the three pairwise interactions and the resulting frequency-dependent dynamics.',
                'correct': 'Each morph wins against one other and loses against the third. If all orange: yellow sneakers invade (yellow beats orange). If all yellow: blue guarders invade (blue beats yellow). If all blue: orange bullies invade (orange beats blue). Because no single strategy can resist invasion by all others, no pure ESS exists. Instead, the system settles into a CYCLING equilibrium where the three morphs oscillate in frequency — a stable cycle rather than a stable point. Sinervo & Lively (1996) documented this 12-year cycle in the field',
                'distractors': [
                    'The system can reach a single-morph ESS if yellow goes extinct first, leaving a stable orange-vs-blue equilibrium',
                    'Rock-paper-scissors cycles are unstable and side-blotched lizards will soon converge on a single morph',
                    'The three morphs coexist by genetic drift rather than selection',
                ],
            },
            {
                'question': 'L4 ANALYSIS: In the Hawk-Dove game, what happens if V (resource value) > C (injury cost)?',
                'correct': 'When V > C, hawks always do better than doves regardless of frequency — fighting is worth the risk because the resource value exceeds the injury cost. The ESS becomes PURE HAWK (all hawks). A mixed ESS requires V < C, so injuries genuinely penalize hawks in hawk-hawk contests',
                'distractors': [
                    'When V > C, doves always dominate because fighting is wasteful',
                    'V > C has no effect on the ESS because ESS depends only on the ratio of hawks to doves',
                    'When V > C, the system cycles between hawk and dove dominance indefinitely',
                ],
            },
        ],
        visual={
            'type': 'payoff-matrix',
            'description': 'Hawk-Dove game',
            'regions': [
                {'label': 'Hawk vs Hawk', 'color': '#ff6b6b', 'items': ['Fight', 'Win - Injury cost']},
                {'label': 'Hawk vs Dove', 'color': '#ffc857', 'items': ['Hawk wins resource', 'Dove yields']},
                {'label': 'Dove vs Dove', 'color': '#7de2d1', 'items': ['Share resource', 'No injury']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Rock beats scissors beats paper beats rock — cycles without winner.',
            'trap': 'Frequency-dependent selection can maintain multiple alleles indefinitely — heterozygote advantage is only ONE way genetic variation is maintained.',
        },
    diagram=hawk_dove_game_diagram(),
    ))
    nodes.append(build_node(
        id='lec13-group-individual',
        title='Levels of Selection: Group vs Individual',
        subtitle='Why selection mostly acts on individuals (Lec 13 slides 8-13)',
        color='blue', row=11,
        heading='Lecture 13 — Levels of Selection',
        sections=[{'label': 'CORE CONCEPT', 'body': 'Classical group selection usually FAILS because a selfish mutant can invade any cooperative group and take over. Within-group selection favoring selfish individuals typically acts faster than between-group selection favoring cooperative groups. Apparent "group benefits" are almost always explained by individual-level fitness gains. BENEFITS OF GROUP LIVING operate through INDIVIDUAL advantages: (1) DILUTION effect — your odds of being picked off by a predator decrease as group size grows; (2) VIGILANCE — more eyes watching means earlier threat detection; (3) COOPERATIVE DEFENSE against predators; (4) COOPERATIVE FORAGING — African wild dogs in larger packs each get more energy per day than solo hunters; (5) CLIFF SWALLOWS form colonies where predator vigilance benefits each individual. GROUP SIZE COSTS: conspicuousness to predators, within-group food and mate competition, and disease transmission. The correct framing is always to ask "how does this behavior increase the INDIVIDUAL\'s fitness?" — not "how does it help the species?"'}] + slides_to_sections(d, (8, 13)),
        examples=[
            'Classical group selection (Wynne-Edwards) proposed that traits "good for the species" evolve because groups with those traits outcompete others.',
            'Williams\' critique (1966): naive group selection usually fails because individual-level selection is stronger — selfish individuals in a group invade and destroy group traits.',
            'Group hunting in African wild dogs works not because it helps the species but because each individual hunter gets more food than hunting alone.',
            'Cliff swallows: colonies provide anti-predator vigilance, but each individual benefits from being in the group.',
        ],
        warnings=[
            '"This behavior evolved for the good of the species" is almost always WRONG on an evolution exam. You must explain how individual-level fitness benefits maintain the trait.',
            'Lemmings do NOT intentionally leap off cliffs to control population — this is a myth popularized by the 1958 Disney documentary. Mass deaths are accidental panic-flight, not deliberate sacrifice. It is a classic example of falsely invoking group selection.',
        ],
        mnemonic='Selection acts on the INDIVIDUAL. "Good for the species" = wrong framing.',
        flashcard={
            'front': 'Why is "group selection" controversial and why does most modern evolutionary biology emphasize individual-level selection?',
            'back': 'GROUP SELECTION hypothesizes that traits evolve because they benefit the GROUP (or species), even if they reduce individual fitness. CLASSICAL EXAMPLE: "Lemmings leap off cliffs to prevent overpopulation." PROBLEM (Williams 1966): individual selection is much STRONGER than group selection in most cases, because the fitness differences between individuals WITHIN a group are larger and change faster than fitness differences between groups. A "selfish" individual who does NOT cooperate gains an immediate fitness advantage within the group — their genes spread. Within a few generations, the cooperative trait is replaced by the selfish one. For group selection to work, groups must have very restricted gene flow, very high extinction/founding rates, and the group-beneficial trait must be strongly heritable at the group level. Modern biology generally explains "group-like" behavior through (1) KIN SELECTION (helping relatives who share your genes), (2) RECIPROCAL ALTRUISM (I help you expecting future help), or (3) MUTUALISTIC BENEFIT (cooperation that also helps the cooperator directly). MODERN MULTI-LEVEL SELECTION theory accepts some group selection under narrow conditions but emphasizes that most apparent "group selection" is really selection at lower levels.',
        },
        quiz=[
            {
                'question': 'A population of wolves hunts in packs. What level of selection best explains pack hunting?',
                'correct': 'Individual selection — each wolf gets more food per hunt when hunting as a pack than alone',
                'distractors': [
                    'Group selection only — for the good of the pack',
                    'Kin selection only — because wolves are related',
                    'Pure altruism with no individual benefit',
                ],
            },
            {
                'question': 'George Williams (1966) argued that naive group selection fails. What is the core reason invading selfish individuals destroy a group-beneficial cooperative trait?',
                'correct': 'Within-group selection favoring selfish individuals is stronger than between-group selection favoring cooperative groups — selfish cheaters spread faster than cooperative groups go extinct',
                'distractors': [
                    'Groups with cooperative traits go extinct faster because they use more resources',
                    'Selfish individuals always have lower fitness than cooperators within the same group',
                    'Gene flow between groups is too high for group-level selection to act, but too low for individual-level selection to work',
                ],
            },
            {
                'question': 'Lemmings supposedly leap off cliffs to control population density — a classic "group selection" story. Why do biologists reject this explanation?',
                'correct': 'The deaths are accidental (panic-flight behavior, not intentional sacrifice), and even if they were deliberate, individual-level selection would immediately favor any lemming that refused to leap — eliminating the suicidal trait within generations',
                'distractors': [
                    'Lemmings are solitary animals and would have no mechanism to coordinate mass behavior, so group selection cannot apply',
                    'Group selection could work in lemmings if relatedness within groups is high enough — the real problem is that r values have never been measured',
                    'The lemming behavior does evolve by group selection, but only because lemming groups have very high extinction rates which satisfies the special conditions Williams required',
                ],
            },
            {
                'question': 'Modern multi-level selection theory accepts group selection under narrow conditions. Which combination of conditions makes group selection most plausible?',
                'correct': 'High heritability of group-level traits, very low gene flow between groups (small founding groups), and high between-group extinction/replacement rates — so group composition is stable long enough for between-group fitness differences to matter',
                'distractors': [
                    'Large group sizes with high internal relatedness, so Hamilton\'s rule is satisfied and kin selection amplifies group-level effects',
                    'Frequency-dependent selection within each group, so cheaters are penalized by their own success and cooperation is maintained without any group-level component',
                    'Strong sexual selection within groups, so cooperators attract more mates and outreproduce cheaters before cheating can spread through the group',
                ],
            },
            {
                'question': 'Who proposed the strong critique of group selection in 1966 that shifted evolutionary biology toward individual-level thinking?',
                'correct': 'George C. Williams, in his book "Adaptation and Natural Selection" — Williams argued that appeals to group selection should be used only when individual-level explanations fail, and most "group-for-the-good-of-the-species" claims could be explained by individual selection',
                'distractors': [
                    'V.C. Wynne-Edwards, 1962 — Wynne-Edwards actually supported group selection with examples like clutch size regulation',
                    'Richard Dawkins, 1976 — Dawkins wrote "The Selfish Gene" but did not formally critique group selection until later',
                    'E.O. Wilson, 1975 — Wilson later revived group selection theory rather than critiquing it',
                ],
            },
            {
                'question': 'The cliff swallow (Petrochelidon pyrrhonota) forms dense colonies that appear to provide group-level benefits such as predator vigilance. Why is this NOT a clean example of group selection?',
                'correct': 'Each individual swallow benefits directly by being in the colony — it has earlier warning of predators, more eyes to spot threats, and can benefit from others\' alarm calls. This is explained by individual-level selection, not group selection; the colony is a byproduct of individual benefits',
                'distractors': [
                    'Cliff swallows are actually solitary and do not form colonies — the textbook example is incorrect',
                    'Colonies cannot evolve by group selection because swallows are asexual and group selection requires sexual reproduction',
                    'The colony is a clear case of group selection because no single swallow can defend against predators alone, proving that cooperation is for the group\'s benefit',
                ],
            },
            {
                'question': 'The myth that lemmings deliberately commit mass suicide was popularized by what?',
                'correct': 'A 1958 Disney documentary ("White Wilderness") staged lemming mass drownings for dramatic effect — the footage created a cultural myth that real lemmings do not actually exhibit. Actual lemming population crashes are due to food shortages and dispersal accidents, not intentional suicide',
                'distractors': [
                    'Wynne-Edwards documented intentional lemming suicide in his 1962 book, providing the original scientific basis for the myth',
                    'Historical reports from medieval Scandinavia accurately described lemming suicide behavior, which has since declined due to climate change',
                    'The myth originated from scientific papers in the 1970s that mis-measured lemming mortality rates as deliberate rather than accidental',
                ],
            },
            {
                'question': 'Which of the following is MOST likely to be correctly explained by group selection under modern multi-level selection theory?',
                'correct': 'Reduced virulence in pathogens that depend on host survival for transmission — pathogens that kill hosts too quickly go extinct with their hosts, so between-host selection favors less virulent strains even when within-host selection favors more virulent ones',
                'distractors': [
                    'Altruistic alarm calls in ground squirrels — modern explanation is kin selection (Hamilton\'s rule), not group selection',
                    'Pack hunting in wolves — this is individual-level selection because each wolf benefits',
                    'Human cooperation in large societies — this is explained by reciprocal altruism and cultural group selection, not naive group selection',
                ],
            },
            {
                'question': 'L1 RECALL: In African wild dog packs, what observed empirical pattern supports an individual-fitness explanation for group hunting?',
                'correct': 'Each individual dog obtains MORE energy per day in larger packs than when hunting alone or in smaller packs — cooperative hunting is not altruistic sacrifice but a behavior that directly increases per-capita food intake for every participant',
                'distractors': [
                    'Individual dogs receive less food per hunt in larger packs — they cooperate despite personal cost',
                    'Pack size has no effect on individual food intake',
                    'Only dominant individuals benefit from larger packs while subordinates starve',
                ],
            },
            {
                'question': 'L1 RECALL: Name at least two benefits of group living at the INDIVIDUAL (not group) level.',
                'correct': 'Dilution effect (lower individual predation probability), increased vigilance (more eyes detecting threats), cooperative defense, cooperative foraging with higher per-capita yield, and shared information about food or predators — each of these directly benefits the individual in the group',
                'distractors': [
                    'Altruistic self-sacrifice and willingness to die for the group',
                    'Group-level resource sharing that equalizes fitness across all members',
                    'Population-level regulation of reproduction to prevent overpopulation',
                ],
            },
            {
                'question': 'L3 APPLICATION: Cliff swallows (Petrochelidon pyrrhonota) form dense nesting colonies. A critic argues this "proves group selection because colony members reduce predation for everyone." Refute this with an individual-level explanation.',
                'correct': 'Colony formation evolved because EACH INDIVIDUAL benefits from: (1) dilution (predation risk is distributed across many birds, so any individual bird is less likely to be the victim); (2) vigilance (more eyes see predators earlier); (3) information transfer about food sources. These individual benefits are sufficient to explain colony evolution without invoking group selection — each swallow gains fitness by joining the colony regardless of what others do',
                'distractors': [
                    'The critic is correct — cliff swallow coloniality is solid evidence for group selection',
                    'Colony formation is a byproduct with no adaptive explanation — neither individual nor group selection applies',
                    'Colony formation is maintained only by phylogenetic inertia from ancestral solitary behaviors',
                ],
            },
            {
                'question': 'L5 SYNTHESIS: Explain why "lemmings throw themselves off cliffs to control population" is BOTH an empirical error (the behavior does not occur as described) AND a conceptual error (even if it occurred, it could not evolve by group selection).',
                'correct': 'EMPIRICAL ERROR: real lemming mass deaths are accidental drowning during migration panic, not intentional population control. The cliff-jumping myth was staged for the 1958 Disney documentary "White Wilderness" and is not a real behavior. CONCEPTUAL ERROR: even if lemmings DID intentionally sacrifice themselves, group selection could not maintain this because a mutant lemming who refused to jump would have higher fitness than the sacrificing ones; selfish refusers would rapidly replace self-sacrificers within a few generations. Both errors must be addressed to correctly reject the claim',
                'distractors': [
                    'The claim is correct on both levels — lemmings do jump and this is a stable group-selected trait',
                    'The empirical claim is false but the conceptual claim is valid — lemmings could theoretically evolve such a trait if they actually existed',
                    'Only the conceptual error matters because the empirical claim is irrelevant to evolutionary theory',
                ],
            },
        ],
        visual={
            'type': 'levels',
            'description': 'Levels of selection',
            'regions': [
                {'label': 'Gene', 'color': '#8a5cf6', 'items': ['Selfish gene view', 'Dawkins 1976']},
                {'label': 'Individual', 'color': '#4ea8de', 'items': ['Classical Darwinian', 'Most cases']},
                {'label': 'Kin group', 'color': '#7de2d1', 'items': ['Inclusive fitness', 'Hamilton\'s rule']},
                {'label': 'Group/Species', 'color': '#ff6b6b', 'items': ['Rarely works', 'Requires strict conditions']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Gene → Individual → Kin → Rarely group.',
            'trap': 'Do NOT say a trait evolved "for the good of the species" unless you can rule out individual-level explanations.',
        },
    ))
    nodes.append(build_node(
        id='lec13-kin-altruism',
        title='Kin Selection, Inclusive Fitness & Altruism',
        subtitle='Hamilton\'s rule and the evolution of helping (Lec 13 slides 14-21)',
        color='teal', row=11,
        heading='Lecture 13 — Kin Selection and Altruism',
        sections=[{'label': 'CORE CONCEPT', 'body': 'An individual\'s total fitness has TWO components: DIRECT FITNESS (own reproduction) + INDIRECT FITNESS (through helped relatives\' reproduction, weighted by relatedness) = INCLUSIVE FITNESS. COEFFICIENT OF RELATEDNESS (r) = probability two individuals share an allele identical by descent: offspring r=0.5, full siblings r=0.5, half-siblings r=0.25, grandchildren r=0.25, first cousins r=0.125. HAMILTON\'S RULE (1964): altruism evolves when rB > C, where r=relatedness of actor to recipient, B=fitness benefit to recipient, C=fitness cost to actor. Note: ONLY benefit is discounted by relatedness; cost is not. HALDANE\'S JOKE: "I would lay down my life for two brothers or eight cousins" — exactly satisfies rB ≥ C (2×0.5 = 1 and 8×0.125 = 1). Classic examples: meerkats share sentry duty among kin; Peromyscus brother-sperm cooperation. HAPLODIPLOIDY (Hymenoptera — ants, bees, wasps): females diploid, males haploid, so full sisters share r=0.75 (higher than parent-offspring r=0.5); this MAY HAVE FACILITATED the evolution of eusociality, though it is not sufficient alone — many haplodiploid species are NOT eusocial.'}] + slides_to_sections(d, (14, 21)),
        examples=[
            'Coefficient of relatedness (r): the probability that two individuals share an allele by descent. Full siblings: r = 0.5. Half siblings: r = 0.25. First cousins: r = 0.125.',
            'Hamilton\'s rule: altruism evolves when rB > C, where r = relatedness, B = benefit to recipient, C = cost to actor.',
            'Inclusive fitness: an individual\'s total fitness = direct fitness (own reproduction) + indirect fitness (from helping relatives reproduce).',
            'Haldane: "I would lay down my life for two brothers or eight cousins" — illustrates rB > C logic.',
            'Haplodiploidy in Hymenoptera: sisters are more related to each other (r = 0.75) than to their own offspring (r = 0.5), which may have facilitated eusociality in ants, bees, wasps.',
        ],
        warnings=[
            'Hamilton\'s rule is rB > C, NOT B > rC or rB > rC. ONLY the benefit is discounted by relatedness; the cost is NOT discounted. Getting the formula wrong is a common exam error.',
            'Haplodiploidy (r = 0.75 for sisters) FACILITATES but does NOT automatically cause eusociality. Many haplodiploid species are not eusocial — haplodiploidy is one contributing factor among several (ecological constraint, nest defense, iteroparity).',
        ],
        mnemonic='Hamilton\'s rule: rB > C. Relatedness × Benefit > Cost.',
        flashcard={
            'front': 'State Hamilton\'s rule and use it to explain why an alarm call that alerts relatives to a predator can evolve despite putting the caller at risk.',
            'back': 'HAMILTON\'S RULE (1964): an altruistic behavior can evolve whenever rB > C, where r = the COEFFICIENT OF RELATEDNESS between actor and recipient (probability of sharing an allele by descent), B = the FITNESS BENEFIT received by the beneficiary, and C = the FITNESS COST to the altruist. APPLICATION TO ALARM CALLS: Suppose a ground squirrel spots a hawk. Calling out attracts the hawk\'s attention (COST = increased risk of predation on the caller). But the alarm alerts nearby squirrels who escape to burrows (BENEFIT to them). If the nearby squirrels are RELATIVES (mother, siblings, cousins), they share many alleles with the caller — so genes for alarm-calling behavior benefit copies of themselves in the bodies of saved relatives. When rB > C (where r is typically averaged across all beneficiaries), alarm-calling spreads even though individual callers suffer. This is INCLUSIVE FITNESS: the actor\'s fitness = own direct reproduction + indirect reproduction through helped relatives. HALDANE QUOTE: "I would lay down my life for two brothers [r = 0.5, 2 × 0.5 = 1.0] or eight cousins [r = 0.125, 8 × 0.125 = 1.0]" — the math of kin selection in one joke.',
        },
        quiz=[
            {
                'question': 'According to Hamilton\'s rule, an altruistic behavior is favored when:',
                'correct': 'rB > C, where r is the coefficient of relatedness, B is the benefit to the recipient, and C is the cost to the actor',
                'distractors': [
                    'B > rC — benefit exceeds cost scaled by relatedness',
                    'r + B > C — relatedness plus benefit exceeds cost',
                    'r > B/C — relatedness exceeds benefit-to-cost ratio',
                ],
            },
            {
                'question': 'In Hymenoptera (ants, bees, wasps), females develop from fertilized eggs (diploid) and males from unfertilized eggs (haploid). A worker bee is more related to her sisters (r = 0.75) than to her own daughters (r = 0.5). How does this haplodiploidy hypothesis explain eusociality using Hamilton\'s rule?',
                'correct': 'Rearing sisters (r = 0.75) propagates MORE copies of the worker\'s alleles than producing daughters (r = 0.5) would — so the rB term for helping sisters exceeds the rB term for direct reproduction, making worker sterility fitness-neutral or even favored',
                'distractors': [
                    'Males are haploid, so they carry only one copy of every gene; workers help the queen to protect the genetic integrity of the haploid males from mutation accumulation',
                    'Haplodiploidy raises relatedness between all colony members including males (r = 0.75), so any helping behavior among nestmates automatically satisfies rB > C',
                    'Worker bees have r = 0 to their brothers, so Hamilton\'s rule predicts they should harm brothers while helping sisters — eusociality arises from conflict avoidance within the colony',
                ],
            },
            {
                'question': 'J.B.S. Haldane said "I would lay down my life for two brothers or eight cousins." What is the quantitative logic behind this statement?',
                'correct': 'Two brothers each share r = 0.5 with Haldane, so 2 × 0.5 = 1.0 expected allele copies saved; eight cousins each share r = 0.125, so 8 × 0.125 = 1.0 — in both cases rB = 1.0 equals the C = 1.0 of sacrificing his own life',
                'distractors': [
                    'Two brothers can replace Haldane\'s reproductive output of two offspring, so the fitness cost is exactly balanced — cousins are included as extra insurance against accidental death',
                    'Haldane was referring to inclusive fitness of the FAMILY UNIT, not to allele-sharing — two brothers plus eight cousins together constitute a full social unit worth preserving',
                    'The calculation uses r = 1.0 for brothers and r = 0.25 for cousins, so two brothers (2 × 1.0 = 2.0 > 1.0) and eight cousins (8 × 0.25 = 2.0 > 1.0) both EXCEED the death cost with room to spare',
                ],
            },
            {
                'question': 'Many haplodiploid insect species are NOT eusocial. What does this tell us about the haplodiploidy hypothesis for eusociality?',
                'correct': 'Haplodiploidy increases relatedness among sisters and makes eusociality easier to evolve via kin selection, but it is neither necessary nor sufficient — other factors (ecological constraints, nest defense, iteroparity) must also be present',
                'distractors': [
                    'It proves haplodiploidy is irrelevant to eusociality and that eusociality must be explained entirely by reciprocal altruism among unrelated nest-mates',
                    'Haplodiploid species that are not eusocial must have unusually high dispersal rates that break up kin groups before inclusive fitness benefits can accumulate',
                    'Since most haplodiploid species lack eusociality, Hamilton\'s rule cannot apply to haplodiploid organisms — eusociality in Hymenoptera must have a non-kin-selection explanation',
                ],
            },
            {
                'question': 'W.D. Hamilton published his foundational paper on inclusive fitness in what year, and what was its title?',
                'correct': '1964 — "The Genetical Evolution of Social Behaviour" (in two parts, published in the Journal of Theoretical Biology). This paper formalized kin selection and introduced the rB > C rule',
                'distractors': [
                    '1859 — "On the Origin of Species." Darwin himself formalized kin selection as part of his theory',
                    '1976 — "The Selfish Gene." Hamilton\'s ideas were first widely published by Richard Dawkins in this book',
                    '1930 — "The Genetical Theory of Natural Selection." Hamilton worked with R.A. Fisher to develop inclusive fitness',
                ],
            },
            {
                'question': 'Calculate the coefficient of relatedness (r) for full siblings.',
                'correct': 'r = 0.5 — full siblings share both parents; on average, half of their alleles are identical by descent because each inherits 50% of each parent\'s genome independently',
                'distractors': [
                    'r = 1.0 — full siblings share both parents and therefore share all their genes',
                    'r = 0.25 — full siblings share only a quarter of their genes because each parent contributes only half a genome',
                    'r = 0.125 — full siblings are equivalent to first cousins in terms of relatedness',
                ],
            },
            {
                'question': 'What is the coefficient of relatedness (r) between first cousins, and between half-siblings?',
                'correct': 'First cousins: r = 0.125 (they share one grandparent pair, and their common alleles are halved twice). Half-siblings: r = 0.25 (they share one parent, so half the alleles of full siblings)',
                'distractors': [
                    'First cousins: r = 0.25; half-siblings: r = 0.5 — these are the same as full siblings and first cousins reversed',
                    'First cousins: r = 0.5; half-siblings: r = 0.5 — both have the same relatedness as full siblings',
                    'First cousins: r = 0.0625; half-siblings: r = 0.125 — the values are halved because of additional generational distance',
                ],
            },
            {
                'question': 'INCLUSIVE FITNESS is defined as:',
                'correct': 'An individual\'s DIRECT fitness (from its own reproduction) PLUS its INDIRECT fitness (from helping relatives reproduce, weighted by relatedness r) — it is the total contribution of an individual\'s genes to the next generation, whether through its own offspring or through relatives\' offspring',
                'distractors': [
                    'The total offspring produced by all members of a family group, divided by the number of members — it is a per-capita measure of group reproductive success',
                    'The lifetime reproductive success of an individual, including offspring from all matings but excluding any contributions from relatives',
                    'The number of alleles an individual contributes to the population, counted by direct descent only and excluding indirect contributions',
                ],
            },
            {
                'question': 'Hamilton\'s rule is rB > C. If a ground squirrel can save 4 nieces/nephews (r = 0.25 each) by giving an alarm call that has a 30% chance of killing the caller, should alarm-calling evolve? (Assume 1 unit of fitness is 1 offspring equivalent)',
                'correct': 'Yes — B = 4 saved relatives × 0.25 r = 1.0 expected gene copies; C = 0.3 (30% chance of death × 1 unit of self); rB = 1.0 > C = 0.3, so alarm calling is favored by kin selection',
                'distractors': [
                    'No — C = 1 (death), rB = 1.0, so rB is NOT greater than C and alarm calling is selectively neutral',
                    'Yes — C = 0.3 and B = 4, so B is much greater than C regardless of relatedness; kin selection always favors saving multiple individuals at any cost',
                    'No — saving non-offspring relatives never increases fitness because only direct descendants count in Darwinian selection',
                ],
            },
            {
                'question': 'If altruism evolves via kin selection, what predicts the DIRECTION of helping behavior within a family group?',
                'correct': 'Help should flow preferentially toward the MOST related individuals — an individual should prefer to help full siblings (r = 0.5) over half siblings (r = 0.25) over cousins (r = 0.125), with cost-benefit analysis also shaped by the ages and reproductive values of potential recipients',
                'distractors': [
                    'Help should be distributed equally among all family members regardless of relatedness — fairness rather than genetic calculation drives cooperation',
                    'Help should flow only to direct offspring — Hamilton\'s rule does not apply to sibling or cousin relationships because they are not genealogical descendants',
                    'Help should flow to less related individuals because more related individuals are already genetically close and gain less benefit from assistance',
                ],
            },
            {
                'question': 'L1 RECALL: Give one classic example of kin selection behavior in mammals discussed in the lecture.',
                'correct': 'Meerkat sentry behavior — individual meerkats take turns standing guard and calling alarm when predators approach, at personal risk, while their close kin forage safely. Because sentries and foragers are typically highly related within a group, rB > C is satisfied and alarm-calling is maintained by kin selection',
                'distractors': [
                    'Solitary hunting in tigers — tigers help unrelated individuals at high cost',
                    'Territorial defense in lions — lions help strangers defend territories regardless of relatedness',
                    'Long-distance migration in wildebeest — migration is driven by kin-selected altruism',
                ],
            },
            {
                'question': 'L5 SYNTHESIS: Sterile worker bees cannot reproduce yet devote their lives to helping their mother (the queen) raise sisters. Integrate haplodiploidy, relatedness calculations, and Hamilton\'s rule to explain why sterile helping is evolutionarily favored, AND explain why haplodiploidy alone is not sufficient.',
                'correct': 'HAPLODIPLOIDY: males haploid (1 chromosome set), females diploid. Full sisters share: (a) 100% of the father\'s haploid genome + (b) 50% of the mother\'s genome, averaging r = 0.75. Because sisters share MORE genes (r = 0.75) than workers would share with their own daughters (r = 0.5), helping a sister raise MORE sisters propagates worker genes MORE efficiently than direct reproduction would — Hamilton\'s rule (rB > C) is satisfied with high r. NOT SUFFICIENT: many haplodiploid species (most bees, wasps, ants) are NOT eusocial. Ecological factors — stable nest defense opportunities, iteroparity, protected larval development sites — must also be present. Termites (diploid-diploid) are eusocial without haplodiploidy, showing kin-selection logic works beyond haplodiploidy alone',
                'distractors': [
                    'Worker bees help because individual selection favors sterility — any bee that attempted to reproduce would be killed by the queen',
                    'Haplodiploidy is the sole cause of eusociality and any eusocial species must be haplodiploid',
                    'Sterile workers violate Hamilton\'s rule and persist only by phylogenetic inertia',
                ],
            },
            {
                'question': 'L4 ANALYSIS: A biologist observes an altruistic behavior (C = 0.1) that yields a benefit (B = 0.3) to a cousin (r = 0.125). Does Hamilton\'s rule favor this altruism?',
                'correct': 'No — rB = 0.125 × 0.3 = 0.0375, which is LESS than C = 0.1. Hamilton\'s rule requires rB > C (0.0375 > 0.1 is FALSE), so altruism toward a cousin at this cost-benefit ratio is NOT favored by kin selection. The relatedness is too low to compensate for the cost',
                'distractors': [
                    'Yes — rB = 0.125 > C = 0.1, so altruism is favored',
                    'Yes — any altruism toward relatives satisfies Hamilton\'s rule regardless of numerical values',
                    'Yes — the cost is discounted by relatedness (rC = 0.0125) which is less than B = 0.3, so it is favored',
                ],
            },
        ],
        visual={
            'type': 'equation',
            'description': 'Hamilton\'s rule visualized',
            'regions': [
                {'label': 'r', 'color': '#4ea8de', 'items': ['Relatedness', 'Siblings: 0.5', 'Cousins: 0.125']},
                {'label': 'B', 'color': '#7de2d1', 'items': ['Benefit to recipient', 'Measured in offspring']},
                {'label': 'C', 'color': '#ff6b6b', 'items': ['Cost to actor', 'Lost direct reproduction']},
                {'label': 'Test', 'color': '#ffc857', 'items': ['rB > C → altruism evolves', 'rB < C → altruism fails']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Two brothers or eight cousins.',
            'trap': 'Altruism doesn\'t require conscious calculation — the rB > C condition operates through selection over evolutionary time.',
        },
    diagram=hamiltons_rule_kin_selection_diagram(),
    ))
    return nodes
