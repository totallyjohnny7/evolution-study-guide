"""Node generators for Lectures 1-7 (Exam 1 coverage).
Row numbering: Lec1=row 1, Lec2=row 2, Lec3=row 3, Lec4=row 4, Lec5-6=row 5, Lec7=row 6.
"""
from helpers import load_lec, slides_to_sections, build_node
from diagrams.hwe_punnett import hwe_punnett_diagram
from diagrams.darwin_five_ingredients import darwin_five_ingredients_diagram
from diagrams.natural_selection_logic_flow import natural_selection_logic_flow_diagram
from diagrams.peppered_moth_selection import peppered_moth_selection_diagram
from diagrams.tree_thinking_components import tree_thinking_components_diagram
from diagrams.hox_regulatory_network import hox_regulatory_network_diagram
from diagrams.reaction_norm_gxe import reaction_norm_gxe_diagram
from diagrams.hardy_weinberg_assumptions import hardy_weinberg_assumptions_diagram
from diagrams.genetic_drift_bottleneck_vs_founder import genetic_drift_bottleneck_vs_founder_diagram
from diagrams.beach_mice_parallel_evolution import beach_mice_parallel_evolution_diagram
from diagrams.tsd_charnov_bull import tsd_charnov_bull_diagram
from diagrams.fitness_landscape import fitness_landscape_diagram

def lec1_nodes():
    d = load_lec('lec1')
    nodes = []
    nodes.append(build_node(
        id='lec1-intro-evolution',
        title='What Is Evolution? Course Intro',
        subtitle='Why evolution unifies biology + practical applications (Lec 1 slides 1-9)',
        color='purple', row=1,
        heading='Lecture 1 — What Is Evolution?',
        sections=[
            {'label': 'CORE CONCEPT', 'body': 'Evolution = any change in the inherited traits of a population that occurs from one generation to the next. Evolution occurs ACROSS generations, NOT within an individual\'s lifetime. Evolution is a SCIENTIFIC THEORY supported by multiple independent lines of evidence — on the same epistemic footing as gravitation, plate tectonics, and aerodynamics. Dobzhansky (1973): "Nothing in biology makes sense except in the light of evolution."'},
            {'label': 'WHY IT MATTERS', 'body': 'Evolution underlies every sub-discipline of biology. Practical applications include agriculture (crop breeding), medicine (antibiotic and vaccine design), conservation (managing genetic diversity), immunology (understanding pathogen adaptation), and epidemiology (predicting outbreak evolution).'},
            {'label': 'KEY FIGURES', 'body': 'Theodosius Dobzhansky (1973 essay). Charles Darwin (Origin of Species, 1859). These authors established evolution as the central explanatory framework of modern biology.'},
        ] + slides_to_sections(d, (1, 9)),
        examples=[
            "Dobzhansky: \"Nothing in biology makes sense except in the light of evolution\"",
            "Practical applications include antibiotic resistance, vaccine design, crop improvement, conservation.",
        ],
        warnings=[
            'WATCH OUT: Evolution is NOT "organisms improving over time" — it is POPULATION-LEVEL change in allele frequencies across generations.',
            'WATCH OUT: Individuals do not evolve — populations do. A giraffe\'s neck does not grow longer because it stretches. The population shifts toward longer necks over generations.',
        ],
        mnemonic='CHANGE = Change in allele frequencies over generations — the minimal definition of evolution.',
        flashcard={
            'front': 'Why is evolution considered the unifying theory of biology?',
            'back': 'Every subfield of biology — from cell biology to ecology — rests on the insight that organisms share common ancestry and have been modified over time by natural selection, drift, mutation, and gene flow. Without evolution, biological diversity and shared traits across species have no causal explanation (Dobzhansky 1973).',
        },
        quiz=[
            {
                'question': 'Which of the following is the most precise scientific definition of evolution?',
                'correct': 'A change in the frequency of alleles in a population across generations',
                'distractors': [
                    'Organisms becoming more complex over time',
                    'The appearance of new species through sudden mutation',
                    'Improvement of individuals during their lifetime',
                ],
            },
            {
                'question': 'Dobzhansky wrote "Nothing in biology makes sense except in the light of evolution." Which scenario BEST illustrates this claim?',
                'correct': 'The fact that all organisms use the same genetic code (DNA → RNA → protein) is explained by universal common ancestry — without evolution, this shared molecular machinery would be an inexplicable coincidence',
                'distractors': [
                    'Antibiotic resistance develops fastest in hospital settings — which proves that bacteria sense when antibiotics are present and mutate in response',
                    'Organisms that live in dark caves lose their eyes over time because they stop using them — demonstrating Lamarckian inheritance still operates alongside natural selection',
                    'Humans and chimpanzees share 98.7% of their DNA — which means humans evolved FROM chimpanzees over the last 6 million years',
                ],
            },
            {
                'question': 'A student argues: "My grandfather got stronger by lifting weights, so his children inherited bigger muscles — that is evolution." What is WRONG with this reasoning?',
                'correct': 'Changes acquired by somatic (body) cells during an individual\'s lifetime cannot be passed to offspring; evolution requires heritable changes at the population level across generations',
                'distractors': [
                    'The grandfather did not produce enough offspring to affect population allele frequencies, so the effect is too small to qualify as evolution',
                    'Evolution only applies to natural, not human-influenced, environments — gym training is artificial and exempt from evolutionary theory',
                    'Muscle size is not heritable at all, so this trait can never evolve regardless of how strong selection is',
                ],
            },
            {
                'question': 'Antibiotic resistance is a textbook example of evolution. If a doctor prescribes antibiotics and the patient\'s infection is "cured" but 10 resistant bacteria survived, which statement is most accurate?',
                'correct': 'Selection has eliminated susceptible bacteria and left only the resistant variants, which will reproduce and potentially transfer resistance genes — the population has evolved even if the patient feels better',
                'distractors': [
                    'The bacteria evolved resistance in response to the antibiotic — they sensed the danger and produced resistance mutations to survive',
                    'Since only 10 bacteria survived out of millions, evolution cannot occur because the population is too small to maintain genetic variation',
                    'The antibiotic cured the infection by killing all bacteria — any survivors are a statistical fluke and cannot represent true evolutionary change',
                ],
            },
            {
                'question': 'Which practical application is NOT a standard example used to motivate the study of evolution in BIOL 4230?',
                'correct': 'Predicting earthquake patterns from tectonic plate motion',
                'distractors': [
                    'Designing antibiotics that are less likely to select for resistance',
                    'Developing annual vaccine formulations for rapidly evolving pathogens',
                    'Improving crop yields through directed breeding programs',
                ],
            },
            {
                'question': 'Conservation biologists rely on evolutionary principles to manage endangered populations. Which specific concern is MOST directly grounded in evolutionary theory?',
                'correct': 'Ensuring that captive breeding programs maintain sufficient genetic variation so the population retains its capacity to respond to future environmental change via selection',
                'distractors': [
                    'Building larger enclosures to reduce stress hormones in captive animals, improving individual welfare',
                    'Providing optimal nutrition so that captive animals reach larger adult body sizes than wild ones',
                    'Training animals with positive reinforcement to behave more cooperatively toward human handlers',
                ],
            },
            {
                'question': 'A key distinction between evolution and individual "change" is TIMESCALE and LEVEL. Which statement correctly contrasts these?',
                'correct': 'Evolution operates on populations across generations via changes in allele frequency; individual-level change (growth, learning, acclimation) operates within a single organism\'s lifetime and is not evolution',
                'distractors': [
                    'Evolution is any change in a trait, whether at the individual or population level — the timescale distinction is arbitrary',
                    'Evolution operates only on somatic cells within individuals; population-level changes are actually ecological, not evolutionary',
                    'Evolution and individual change are the same process at different scales — a fast-growing individual is evolving faster than a slow-growing one',
                ],
            },
            {
                'question': 'Dobzhansky\'s famous 1973 essay title refers to evolution as the ONLY light by which biology makes sense. Which field of biology would be MOST impoverished without evolutionary theory?',
                'correct': 'All fields equally — from molecular biology (why do homologous proteins exist) to ecology (why do niches emerge) to medicine (why do pathogens adapt) — because evolution provides the causal explanation for all shared and divergent biological features',
                'distractors': [
                    'Only systematics and paleontology — other fields like biochemistry or cell biology function perfectly well without evolutionary concepts',
                    'Only medicine — because evolutionary principles are needed for drug design, but cellular mechanisms can be understood without evolution',
                    'Only ecology — because evolution shapes species interactions, but molecular and cellular biology are independent of evolutionary theory',
                ],
            },
            {
                'question': 'L1 RECALL: In what year did Dobzhansky publish the famous essay that defined evolution as the unifying framework of biology?',
                'correct': '1973',
                'distractors': ['1859', '1942', '1996'],
            },
            {
                'question': 'L3 COMPARISON: A scientist says "evolution is JUST a theory." Evolution is referred to as a scientific THEORY — but with what other well-established scientific theories is it epistemically comparable in the lecture?',
                'correct': 'Gravitation, plate tectonics, and aerodynamics — all are scientific theories in the technical sense (well-tested explanatory frameworks), not guesses',
                'distractors': [
                    'Homeopathy, astrology, and numerology — all called "theories" in some contexts',
                    'Theories of literary criticism and political theories — which are equally rigorous scientifically',
                    'Mathematical theorems like the Pythagorean theorem — which are directly comparable to scientific theories in how they are proven',
                ],
            },
            {
                'question': 'L5 SYNTHESIS: Which single sentence BEST captures the core scientific definition of evolution as presented in Lecture 1?',
                'correct': 'Evolution is any change in the inherited traits of a population that occurs from one generation to the next',
                'distractors': [
                    'Evolution is the gradual improvement of individual organisms over the course of their lifetimes',
                    'Evolution is the spontaneous appearance of new species through single mutational events',
                    'Evolution is the extinction of species and the replacement of their ecological niches by unrelated new species',
                ],
            },
        ],
        visual={
            'type': 'concept-map',
            'description': 'Evolution as the unifying hub of biology',
            'regions': [
                {'label': 'Core claim', 'color': '#8a5cf6', 'items': ['Change in allele frequencies over generations']},
                {'label': 'Explains', 'color': '#4ea8de', 'items': ['Biodiversity', 'Shared homologies', 'Fossil record', 'Adaptation']},
                {'label': 'Practical uses', 'color': '#ffc857', 'items': ['Antibiotic resistance', 'Vaccine design', 'Crop breeding', 'Conservation']},
            ],
            'arrows': [],
            'tooltips': [],
            'mnemonic': 'Allele frequency change = evolution. Everything else is a consequence.',
            'trap': 'Common misconception: evolution means "progress" or "improvement." Evolution is directional only in the sense of local fitness — there is no global ladder.',
        },
    ))
    nodes.append(build_node(
        id='lec1-flu-case-study',
        title='Flu Virus: Evolution in Action',
        subtitle='H1N1 rapid evolution — a real-time case study (Lec 1 slides 10-21)',
        color='coral', row=1,
        heading='Lecture 1 — Influenza as Evolution Case Study',
        sections=[
            {'label': 'CORE CONCEPT', 'body': 'Influenza is a microscopic shell of protein encasing 13 genes distributed across 8 RNA segments. Hemagglutinin (HA) binds the virus to host cells; Neuraminidase (NA) enables new virus particles to detach. Evolution by mutation + selection happens in real time and can be observed within a single infection.'},
            {'label': 'MECHANISM', 'body': 'Each infected cell produces thousands of new virus copies. Error-prone RNA replication generates mutational diversity. Selection then spreads variants that escape host immunity. ANTIGENIC DRIFT = gradual HA/NA amino acid substitutions that reduce vaccine effectiveness. REASSORTMENT = two strains co-infect one host cell and exchange entire RNA segments, producing novel pandemic strains.'},
            {'label': 'KEY EXAMPLES', 'body': 'H1N1 (2009) arose by TRIPLE REASSORTMENT of bird, pig, and human flu genes. Hensley et al. (2009, Science) passaged flu through vaccinated mice for 9 cycles — the virus evolved altered HA; unvaccinated control mice showed NO HA change. This directly demonstrated selection for vaccine escape. The annual vaccine is needed because HA and NA continually accumulate amino acid substitutions.'},
            {'label': 'KEY TERMS', 'body': 'HA (hemagglutinin), NA (neuraminidase), antigenic drift, antigenic shift / reassortment, 8 RNA segments, H1N1.'},
        ] + slides_to_sections(d, (10, 21)),
        examples=[
            'H1N1 2009 pandemic: traced back to swine-origin triple reassortment of bird, pig, and human flu genes; tracked in real time via global genomic sampling.',
            'Hemagglutinin and neuraminidase surface proteins accumulate amino acid substitutions — driving antigenic drift.',
            'Hensley et al. 2009 Science: vaccinated mice → flu evolved altered HA after 9 infection cycles; unvaccinated controls showed no HA change. Direct demonstration of vaccine-escape selection.',
        ],
        warnings=[
            'WATCH OUT: Not all mutations are selected for — most are neutral or deleterious. Only rare beneficial substitutions are fixed by selection.',
        ],
        mnemonic='HA-NA = HemAgglutinin and NeurAminidase — the flu\'s two most-evolving proteins and the targets of vaccines.',
        flashcard={
            'front': 'How does influenza virus illustrate rapid evolution by natural selection?',
            'back': 'Influenza has an 8-segment RNA genome and a high error-rate RNA polymerase (no proofreading). Errors create variants constantly. Host immunity selects for variants whose surface proteins (HA, NA) evade recognition, so amino acid substitutions accumulate on the surface. Comparing samples worldwide showed that the 2009 H1N1 pandemic strain descended from reassortment between human, avian, and swine flu lineages — tracked in real time by phylogenetic analysis.',
        },
        quiz=[
            {
                'question': 'Which feature of influenza most directly explains why new vaccine formulations are needed each year?',
                'correct': 'High mutation rate in surface proteins HA and NA drives antigenic drift',
                'distractors': [
                    'The virus physically grows larger each year',
                    'Humans gradually lose immunity to all pathogens over time',
                    'New animal hosts invent new flu types annually',
                ],
            },
            {
                'question': 'Antigenic DRIFT and antigenic SHIFT both create new flu strains, but they differ in mechanism. Which scenario correctly describes antigenic SHIFT?',
                'correct': 'A pig is simultaneously infected with both a human flu strain and an avian flu strain; the two viruses\' 8-segment RNA genomes reassort inside the pig, producing a novel strain carrying surface proteins that human immune systems have never encountered',
                'distractors': [
                    'A flu virus replicates inside a human cell and the error-prone RNA polymerase substitutes one amino acid in the HA protein — gradually accumulating small surface changes over many replication cycles',
                    'A flu virus mutates so rapidly that the patient\'s immune system cannot produce antibodies fast enough, allowing the virus to evade immunity through sheer mutation rate',
                    'A new flu strain emerges each year when influenza acquires a proofreading polymerase by horizontal gene transfer from a bacterium it co-infects in the respiratory tract',
                ],
            },
            {
                'question': 'The 2009 H1N1 pandemic strain was reconstructed phylogenetically and traced to a "triple reassortment" event. What does this mean, and which evolutionary principle does it most directly illustrate?',
                'correct': 'The strain combined RNA segments from three independent lineages (human, avian, and swine flu) — illustrating that genetic variation in influenza can arise not just from mutation but from recombination between entire viral genomes (reassortment)',
                'distractors': [
                    'The strain mutated three separate hemagglutinin amino acids simultaneously in a single infected pig, illustrating the multiplicative effect of high viral mutation rates',
                    'Three separate flu pandemics merged into one dominant strain through natural selection, eliminating less fit strains and retaining only the most virulent combinations',
                    'The strain underwent three rounds of rapid evolution within a single human host whose immune system was compromised — demonstrating that intra-host evolution is the primary source of pandemic strains',
                ],
            },
            {
                'question': 'A flu vaccine researcher notes that HA mutations on the outer surface of the protein are far more common in circulating strains than HA mutations that change internal structural residues. Which evolutionary explanation is MOST correct?',
                'correct': 'Mutations on the outer surface face antibody-mediated immune selection every generation — variants that escape existing antibodies have higher fitness, so surface mutations are selectively favored and fixed faster than neutral structural mutations',
                'distractors': [
                    'Internal HA residues mutate more slowly because the RNA polymerase has lower error rates when copying sequences that code for structurally important regions',
                    'Surface mutations are more common because the outer regions of HA are encoded by a different RNA segment that has an inherently higher mutation rate than segments encoding internal proteins',
                    'Immune selection removes any mutation that changes internal HA structure because the host immune system specifically targets internal epitopes that are exposed during viral assembly',
                ],
            },
            {
                'question': 'The influenza genome consists of how many RNA segments, and why is this structure critical to antigenic shift?',
                'correct': '8 segments — a segmented genome allows reassortment (genome-level mixing) when two different flu strains co-infect the same host cell, so entire RNA segments can be exchanged wholesale',
                'distractors': [
                    '2 segments — one for HA and one for NA, so reassortment can only swap one protein at a time',
                    '1 single RNA molecule — reassortment works via recombination of this single strand during replication',
                    '23 segments — matching the number of human chromosomes, which is why humans are frequent hosts',
                ],
            },
            {
                'question': 'Flu\'s RNA polymerase is described as "error-prone" and lacks proofreading. Why is this feature the foundation of flu\'s rapid evolution?',
                'correct': 'Without proofreading, every replication cycle introduces many mutations — generating a huge pool of genetic variation each day within a single infected host, which is the raw material for immune escape and antigenic drift',
                'distractors': [
                    'Error-prone polymerase is inefficient, so flu replicates more slowly than DNA viruses, giving natural selection more time per generation to act',
                    'Error-prone polymerase directly causes reassortment by breaking RNA segments into multiple pieces during copying',
                    'The polymerase specifically targets the HA and NA genes for mutation while preserving other segments, which is why only surface proteins evolve',
                ],
            },
            {
                'question': 'HA and NA are highlighted as the two most-evolving flu proteins. Why are these TWO proteins, rather than internal proteins, the primary targets of annual vaccine redesign?',
                'correct': 'HA and NA sit on the virion surface and are the main targets of neutralizing antibodies — vaccines elicit antibodies against them, and the virus must evolve these specific proteins to escape immunity',
                'distractors': [
                    'HA and NA are the only two proteins encoded by the flu genome, so vaccines by definition target them exclusively',
                    'HA and NA mutate randomly while internal proteins are protected by evolutionary constraints that prevent any mutation at all',
                    'Internal flu proteins are identical to human proteins, so vaccines cannot target them safely; HA and NA are the only viral-specific targets',
                ],
            },
            {
                'question': 'Why is flu evolution considered a "real-time" case study of evolution rather than a historical inference?',
                'correct': 'Global genomic sampling allows researchers to sequence circulating strains week by week and directly observe allele frequency changes in HA/NA, constructing phylogenies that track evolution as it unfolds',
                'distractors': [
                    'Flu is the only pathogen that has been directly observed to speciate in the lab under controlled conditions',
                    'Flu samples are preserved in the fossil record of sedimentary rocks, allowing direct measurement of ancient mutation rates',
                    'Flu evolution is instantaneous within individual hosts, so researchers can observe complete speciation events within a single patient',
                ],
            },
            {
                'question': 'L1 RECALL: How many genes and how many RNA segments does influenza have?',
                'correct': '13 genes on 8 RNA segments',
                'distractors': [
                    '8 genes on 13 RNA segments',
                    '23 genes on 23 RNA segments',
                    '100 genes on a single circular DNA molecule',
                ],
            },
            {
                'question': 'L2 MECHANISM: In the Hensley et al. (2009) Science experiment, how did the experimenters directly demonstrate that vaccination drives HA evolution in flu?',
                'correct': 'They passaged flu through vaccinated mice for 9 infection cycles and observed altered HA sequences, while flu passaged through unvaccinated control mice showed no HA change — isolating vaccine-mediated selection as the cause',
                'distractors': [
                    'They inserted random mutations into HA and observed that vaccinated mice got sicker — demonstrating that HA mutations increase virulence independently of selection',
                    'They compared HA sequences between wild pigeons and vaccinated chickens and found that vaccinated birds carried more HA variation — evidence for vaccine-driven diversification',
                    'They used CRISPR to edit HA in vitro and confirmed that only vaccinated hosts could support replication of edited variants — showing selection at the genome-editing level',
                ],
            },
            {
                'question': 'L5 SYNTHESIS: The 2009 H1N1 pandemic strain is described as a "triple reassortment." Which three source lineages contributed genes to it?',
                'correct': 'Bird, pig, and human flu lineages — their genes reassorted inside a pig host to produce the novel pandemic strain',
                'distractors': [
                    'Bat, horse, and dog flu lineages',
                    'Three independent human flu lineages with no animal origin',
                    'Only swine flu lineages from different pig farms',
                ],
            },
        ],
        visual={
            'type': 'flow',
            'description': 'Flu evolution loop: error-prone replication → surface mutation → selection by host immunity',
            'regions': [
                {'label': '1. Replication', 'color': '#ff6b6b', 'items': ['No proofreading RNA pol', 'Mutations per replication']},
                {'label': '2. Surface change', 'color': '#ffc857', 'items': ['HA/NA amino acid substitutions', 'Antigenic drift']},
                {'label': '3. Host selection', 'color': '#4ea8de', 'items': ['Immune escape', 'Reinfection possible']},
                {'label': '4. Spread', 'color': '#7de2d1', 'items': ['New dominant strain', 'Repeat cycle']},
            ],
            'arrows': [],
            'tooltips': [],
            'mnemonic': 'Error → Drift → Escape → Spread.',
            'trap': 'Antigenic DRIFT (small mutations, gradual) ≠ antigenic SHIFT (reassortment of whole RNA segments, sudden pandemic strains).',
        },
    ))
    nodes.append(build_node(
        id='lec1-takehome-course',
        title='Lecture 1 Take-Home & Course Info',
        subtitle='Why evolution matters + course logistics (Lec 1 slides 22-30)',
        color='gray', row=1,
        heading='Lecture 1 — Take-Home & Course Information',
        sections=[
            {'label': 'CORE CONCEPT', 'body': 'Evolution is PREDICTIVE. Flu surveillance demonstrates that strains can be tracked (and predicted to spread) before widespread detection. Monitoring pig farms is evolutionarily motivated because pigs serve as "mixing vessels" for avian and human flu strains in reassortment events. The course textbook is Evolution: Making Sense of Life (2nd Edition). Dr. Travis Robbins\' own research centers on the ecology and evolution of lizards (Sceloporus), reptile physiology, life history, and thermal adaptation.'},
            {'label': 'WHY IT MATTERS', 'body': 'Understanding evolutionary principles equips students to anticipate pathogen adaptation, design conservation strategies, and engage scientifically with applied problems in medicine, agriculture, and climate change.'},
            {'label': 'COURSE EXPECTATIONS', 'body': 'BIOL 4230 emphasizes reading assigned material, attending lectures, and applying concepts — passive memorization is insufficient.'},
        ] + slides_to_sections(d, (22, 30)),
        mnemonic='Read → Attend → Apply: passive reading isn\'t enough for BIOL 4230.',
        flashcard={
            'front': 'What are the three main reasons the instructor gives for why understanding evolutionary principles is important?',
            'back': '(1) It explains patterns we observe in all living organisms; (2) It has direct practical applications (medicine, agriculture, conservation); (3) It provides the only coherent framework for asking "why" questions in biology.',
        },
        quiz=[
            {
                'question': 'According to Lecture 1, which feature most distinguishes evolutionary biology as a SCIENCE rather than just a historical account of life?',
                'correct': 'It generates testable, falsifiable predictions about allele frequencies, fitness, and adaptation — not just post-hoc narratives',
                'distractors': [
                    'It relies on direct observation of speciation events, which occur over human-observable timescales',
                    'It explains only past events and makes no predictions about future population change',
                    'Its claims are insulated from genetic evidence because behavior cannot be fossilized',
                ],
            },
            {
                'question': 'A student says "Evolution is just a theory, so we should not consider it established science." What is the BEST response using the scientific meaning of "theory"?',
                'correct': 'In science, "theory" refers to a well-tested explanatory framework supported by multiple independent lines of evidence — the same status as atomic theory or germ theory, not a guess',
                'distractors': [
                    'Evolution is actually a scientific law, not a theory, because it has been observed in the lab and in the wild and cannot be disputed',
                    'The statement is valid: until scientists observe a new species forming in nature, evolutionary theory remains speculative and cannot claim the status of established science',
                    'Science does not use the word "theory" — the correct term is "hypothesis," and evolution remains a hypothesis until it can be verified by direct experiment on deep time scales',
                ],
            },
            {
                'question': 'Which practical application most DIRECTLY depends on evolutionary principles being correct?',
                'correct': 'Designing annual flu vaccines by tracking which surface-protein variants are spreading due to immune-mediated selection in the human population',
                'distractors': [
                    'Developing better fertilizers by testing which nitrogen concentrations produce the highest crop yield in controlled greenhouse trials',
                    'Mapping the human genome by sequencing DNA fragments and assembling them based on overlapping nucleotide sequences',
                    'Producing insulin for diabetics by inserting the human insulin gene into bacterial plasmids and fermenting the bacteria at scale',
                ],
            },
            {
                'question': 'Robbins emphasizes that students should arrive to BIOL 4230 prepared to READ, ATTEND, and APPLY rather than passively memorize. Which exam question type BEST requires application rather than recall?',
                'correct': 'A novel scenario where a population of island lizards shows dramatic color divergence from the mainland — students must identify which evolutionary force(s) are operating and predict what evidence would distinguish them',
                'distractors': [
                    'Listing the five assumptions of Hardy-Weinberg equilibrium in order from most to least important',
                    'Defining "genetic drift" in two sentences as it appears in the course glossary',
                    'Matching each pre-Darwin thinker (Linnaeus, Cuvier, Lamarck, Lyell) to his major contribution',
                ],
            },
            {
                'question': 'A student asks: "Can evolutionary theory predict the FUTURE course of evolution?" What is the most scientifically rigorous answer?',
                'correct': 'Evolutionary theory generates testable short-term predictions (e.g., the breeders equation predicts response to selection one generation ahead) but long-term predictions are constrained by environmental unpredictability and the stochasticity of mutation and drift',
                'distractors': [
                    'No — evolution is purely historical and cannot make predictions; it describes only past events',
                    'Yes — evolutionary theory can predict the exact form of all future species over any timescale using the breeders equation alone',
                    'Yes, but only if the population is in Hardy-Weinberg equilibrium, since HWE is the only predictive framework in evolutionary biology',
                ],
            },
            {
                'question': 'Which of the three main reasons the instructor identifies for studying evolution aligns with Dobzhansky\'s claim that "nothing in biology makes sense except in the light of evolution"?',
                'correct': 'Evolution explains the patterns we observe in all living organisms — from shared genetic code to adaptations to geographic distributions',
                'distractors': [
                    'Evolution ensures that all species will eventually improve over geological time toward a perfect form',
                    'Evolution justifies religious interpretations of biological origins and is philosophically necessary for ethical reasoning',
                    'Evolution provides a framework for ranking species from primitive to advanced, which is the foundation of biological classification',
                ],
            },
            {
                'question': 'Robbins highlights that evolution has the three pillars: Mechanisms, Evidence, and Applications (MEA). Which course activity most directly addresses the "Evidence" pillar?',
                'correct': 'Examining fossil records, homologous structures, and phylogenetic data that document descent with modification across lineages',
                'distractors': [
                    'Calculating expected heterozygosity using the Hardy-Weinberg equation',
                    'Developing a new antibiotic drug for clinical testing',
                    'Listing the names of 19th-century naturalists in chronological order',
                ],
            },
            {
                'question': 'The course emphasizes that passive reading is insufficient for BIOL 4230. Which study strategy most closely aligns with the course\'s "Read → Attend → Apply" model?',
                'correct': 'Reading assigned material before lecture, attending to refine understanding, then working practice problems that require applying concepts to novel scenarios',
                'distractors': [
                    'Memorizing every term in the textbook glossary and reviewing flashcards exclusively',
                    'Attending lecture without reading the textbook and relying only on class notes',
                    'Reading the textbook multiple times without attempting any practice problems',
                ],
            },
            {
                'question': 'L1 RECALL: What is the textbook used in BIOL 4230 (as described in Lecture 1)?',
                'correct': 'Evolution: Making Sense of Life (2nd Edition)',
                'distractors': [
                    'On the Origin of Species, Darwin',
                    'Principles of Genetics, Hartl',
                    'The Selfish Gene, Dawkins',
                ],
            },
            {
                'question': 'L2 MECHANISM: Why does Dr. Robbins emphasize monitoring pig farms as an evolutionary concern?',
                'correct': 'Pigs serve as a "mixing vessel" in which avian and human flu strains can co-infect and reassort, producing novel pandemic strains — monitoring pigs allows early detection of such recombinant viruses',
                'distractors': [
                    'Pigs are the only mammal species in which flu can mutate — other mammals do not support flu replication',
                    'Pigs produce a unique enzyme that accelerates HA evolution beyond what is possible in other hosts',
                    'Pig farms are legally required to report all animal diseases, making them the easiest surveillance sites for flu',
                ],
            },
            {
                'question': 'L5 SYNTHESIS: Dr. Travis Robbins\' own research program focuses on:',
                'correct': 'Ecology and evolution of lizards (Sceloporus), reptile physiology, life history, and thermal adaptation',
                'distractors': [
                    'Molecular phylogenetics of bacteria',
                    'Human evolutionary psychology',
                    'Marine mammal acoustic communication',
                ],
            },
        ],
        visual={
            'type': 'bullet',
            'description': 'Course pillars',
            'regions': [
                {'label': 'Pillars', 'color': '#888', 'items': ['Mechanisms', 'Evidence', 'Applications']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'MEA: Mechanisms → Evidence → Applications.',
            'trap': '',
        },
    ))
    return nodes


def lec2_nodes():
    d = load_lec('lec2')
    nodes = []
    nodes.append(build_node(
        id='lec2-pre-darwin',
        title='Pre-Darwin Evolutionary Thinking',
        subtitle='Linnaeus, Cuvier, Lamarck — the road to Darwin (Lec 2 slides 1-9)',
        color='amber', row=2,
        heading='Lecture 2 — Evolutionary Thinking Before Darwin',
        sections=[
            {'label': 'CORE CONCEPT', 'body': 'Before Darwin, Western thought largely held that species were fixed and unchanging (the "Great Chain of Being" from the Ancient Greeks onward). A series of naturalists and geologists gradually chipped away at this view during the 18th-19th centuries — documenting extinction, deep time, and even proposing mechanisms of change — culminating in the mechanism of natural selection.'},
            {'label': 'KEY FIGURES', 'body': 'Ancient Greeks (Great Chain of Being; species fixed). Archbishop Ussher (1664): calculated Creation at October 23, 4004 BC, 9 am. Linnaeus (1707-1778): binomial nomenclature and hierarchical classification under a Divine Plan. Buffon (1707-1788): proposed "organic particles" transforming organisms; argued Earth was old. James Hutton (1726-1797): uniformitarianism. Cuvier (1769-1832): paleontologist who documented EXTINCTION and proposed catastrophism. William Smith (1769-1839): organized geological history by fossils. Lamarck (1744-1829): FIRST formal theory of evolution via inheritance of acquired characteristics (mechanism wrong, but correctly recognized change).'},
            {'label': 'WHY IT MATTERS', 'body': 'Darwin did not arrive at evolution in a vacuum. The groundwork of extinction (Cuvier), deep time (Hutton/Lyell), classification (Linnaeus), and the first mechanistic theory (Lamarck) made natural selection conceptually possible by 1859.'},
        ] + slides_to_sections(d, (1, 9)),
        quotes=['"Special creation" = the pre-Darwinian view that each species was divinely created in its present form.'],
        examples=[
            'Linnaeus (1707-1778): classified organisms into hierarchical groups — kingdom, class, order, genus, species.',
            'Cuvier (1769-1832): documented extinction using fossils, proposed catastrophism.',
            'Lamarck (1744-1829): first formal theory of evolution — inheritance of acquired characteristics (incorrect mechanism, but correctly recognized change).',
            'Lyell: uniformitarianism — geological processes are gradual and ongoing (influenced Darwin).',
            'Archbishop Ussher (1664): calculated the Creation at 9 am on October 23, 4004 BC.',
            'William Smith (1769-1839): organized geological history by fossils.',
        ],
        mnemonic='LCLLL = Linnaeus (classification) → Cuvier (extinction) → Lamarck (first mechanism) → Lyell (deep time) → Darwin.',
        flashcard={
            'front': 'What was Lamarck\'s theory of evolution and why was its mechanism ultimately rejected?',
            'back': 'Lamarck proposed that organisms change during their lifetime in response to use/disuse, and that these acquired traits are passed to offspring (e.g., giraffe necks stretching). Modern genetics shows that changes to somatic tissues are not inherited — only changes to germ line DNA pass to offspring. Lamarck was correct that evolution happens and that it is an ongoing process, but the mechanism (inheritance of acquired characteristics) is false for most traits. Lamarck deserves credit for being the first to propose a mechanistic theory.',
        },
        quiz=[
            {
                'question': 'Which of these pre-Darwin thinkers FIRST articulated a formal mechanism for evolutionary change, even though that mechanism was wrong?',
                'correct': 'Jean-Baptiste Lamarck',
                'distractors': ['Carl Linnaeus', 'Georges Cuvier', 'Charles Lyell'],
            },
            {
                'question': 'Lamarck proposed that a blacksmith\'s children would inherit stronger arms because the father developed them through use. Modern genetics shows this is false. But which modern phenomenon is sometimes superficially compared to Lamarckism, and why is the comparison misleading?',
                'correct': 'Epigenetic inheritance — chemical modifications to histones or DNA methylation can sometimes persist across one or two generations, but this involves regulatory tags on fixed DNA sequences, not the acquisition of structural changes in body tissues, and the effect rarely persists beyond F2',
                'distractors': [
                    'Genetic drift — small population effects can cause rare alleles to increase in frequency without selection, which resembles Lamarck\'s idea that the environment directly modifies the genome',
                    'Phenotypic plasticity — a frog that grows longer legs in deep water passes that trait to offspring, proving Lamarck was essentially correct about environmentally induced heritable change',
                    'Horizontal gene transfer — bacteria can acquire useful genes from other bacteria in the environment, which is the molecular equivalent of the inheritance of acquired characteristics Lamarck described',
                ],
            },
            {
                'question': 'Cuvier used catastrophism to explain why species in deeper (older) rock strata differ from those in shallower strata. How does this differ from the uniformitarianism that Lyell advocated, and which view better supported Darwin?',
                'correct': 'Lyell\'s uniformitarianism — that the same geological processes operating today (erosion, sedimentation, uplift) operated in the past at the same rates — implied Earth is enormously OLD, giving Darwin the deep time necessary for gradual natural selection to produce species-level differences',
                'distractors': [
                    'Catastrophism was actually more useful to Darwin because sudden catastrophic events could produce rapid speciation, which is more consistent with the abrupt species boundaries seen in the fossil record',
                    'Both views were equally useful to Darwin: uniformitarianism provided deep time, while catastrophism explained mass extinctions that created ecological opportunities for new species to fill vacated niches',
                    'Lyell\'s uniformitarianism undermined Darwin because gradual geological change implied environments were too stable to generate the variation in selective pressures that drives natural selection',
                ],
            },
            {
                'question': 'A 19th-century biologist who accepted Cuvier\'s work (extinctions are real, species are fixed by divine creation) but rejected Lamarck (no mechanism for change) would most likely hold which view about diversity?',
                'correct': 'Multiple separate creation events produced modern species — extinctions eliminated earlier creations, and new species were divinely created to replace them (the "progressive creationism" position)',
                'distractors': [
                    'All present-day species are descended from the original Creation and none have gone extinct — apparent fossil differences reflect incomplete preservation, not true extinction',
                    'Species gradually transform through use and disuse into the forms we see today — Cuvier\'s extinctions provide the raw material for Lamarckian change across geological time',
                    'Evolution occurs but is divinely guided — God uses Lamarckian mechanisms to improve species over time, with Cuvier\'s extinctions representing failed experiments',
                ],
            },
            {
                'question': 'Carl Linnaeus (1707-1778) is best known for which foundational contribution to biology that — despite his commitment to special creation — later aided evolutionary thinking?',
                'correct': 'Developing a hierarchical classification system (kingdom, class, order, genus, species) that organized organisms into nested groups — the nested pattern itself is a prediction of common descent',
                'distractors': [
                    'Proposing that species can transform over time through the inheritance of acquired characteristics',
                    'Documenting extinction using fossils found in distinct rock strata',
                    'Developing the principle of uniformitarianism to explain gradual geological change',
                ],
            },
            {
                'question': 'Which contribution is CORRECTLY matched to its thinker?',
                'correct': 'Lyell — uniformitarianism (geological processes are gradual and ongoing)',
                'distractors': [
                    'Lamarck — catastrophism (sudden destruction events shape species)',
                    'Cuvier — inheritance of acquired characteristics',
                    'Linnaeus — deep-time geology and the age of the Earth',
                ],
            },
            {
                'question': '"Special creation" is defined in Lecture 2 as the pre-Darwinian view that:',
                'correct': 'Each species was divinely created in its present form and has not changed since',
                'distractors': [
                    'Each species arose once through a single mutation and then gradually transformed through use and disuse',
                    'Species are created fresh with each generation to match current environmental conditions',
                    'Species are created gradually over geological time through continuous divine intervention',
                ],
            },
            {
                'question': 'Lyell\'s principle of uniformitarianism was especially important for Darwin because it implied:',
                'correct': 'The Earth is enormously old — providing the deep time required for gradual natural selection to produce species-level differences',
                'distractors': [
                    'Catastrophes periodically reset biodiversity, requiring divine re-creation of species',
                    'Geological processes operate differently in the past than today, making historical inference impossible',
                    'All species must be younger than 6,000 years because geological processes are too slow to produce older rocks',
                ],
            },
            {
                'question': 'Which statement BEST captures Lamarck\'s actual historical contribution, giving him appropriate credit while noting his error?',
                'correct': 'Lamarck deserves credit for being the first to propose a formal mechanism for evolution and correctly recognizing that evolution is ongoing — his specific mechanism (inheritance of acquired characteristics) was wrong, but proposing a mechanism at all was a breakthrough',
                'distractors': [
                    'Lamarck was entirely wrong about evolution — his work has no historical value and should be dismissed in a modern evolution course',
                    'Lamarck was entirely correct — modern genetics has confirmed that acquired traits can be inherited across generations via DNA methylation, validating his original theory',
                    'Lamarck only contributed to taxonomy and classification, not to evolutionary mechanism — he should be remembered alongside Linnaeus',
                ],
            },
            {
                'question': 'L1 RECALL: Archbishop Ussher (1664) calculated the exact date of the Creation. According to his calculation, when did it occur?',
                'correct': 'October 23, 4004 BC, at 9 am',
                'distractors': [
                    'January 1, 10000 BC, at midnight',
                    'March 21, 1000 BC, at dawn',
                    'July 4, 1776 AD, at noon',
                ],
            },
            {
                'question': 'L4 APPLICATION: A paleontologist in 1800 shows the French Academy a skeleton of an extinct mammoth recovered from Siberia. This evidence most directly supports which pre-Darwin thinker\'s work?',
                'correct': 'Cuvier — who documented extinction using fossils and argued that species could disappear completely from the Earth',
                'distractors': [
                    'Linnaeus — whose hierarchical classification depends on extinct forms',
                    'Lamarck — whose theory of acquired characteristics applies only to extinct lineages',
                    'Ussher — whose biblical chronology specifically predicted the existence of such fossils',
                ],
            },
        ],
        visual={
            'type': 'timeline',
            'description': 'Pre-Darwin influences',
            'regions': [
                {'label': 'Linnaeus', 'color': '#ffc857', 'items': ['Taxonomy', 'Nested hierarchy']},
                {'label': 'Cuvier', 'color': '#ff6b6b', 'items': ['Extinction', 'Catastrophism']},
                {'label': 'Lamarck', 'color': '#4ea8de', 'items': ['First mechanism', 'Acquired traits (wrong)']},
                {'label': 'Lyell', 'color': '#7de2d1', 'items': ['Deep time', 'Uniformitarianism']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Linnaeus named, Cuvier buried, Lamarck mechanized, Lyell stretched time.',
            'trap': 'Do NOT confuse Lamarck\'s (wrong) inheritance of acquired characteristics with modern epigenetic inheritance — the latter is real but rare and does not explain most adaptation.',
        },
    diagram=darwin_five_ingredients_diagram(),
    ))
    nodes.append(build_node(
        id='lec2-darwin-voyage',
        title='Darwin\'s Voyage of the Beagle',
        subtitle='The observational foundation of evolutionary theory (Lec 2 slides 10-12)',
        color='teal', row=2,
        heading='Lecture 2 — Darwin\'s Voyage',
        sections=[
            {'label': 'CORE CONCEPT', 'body': 'At age 22, Charles Darwin joined the HMS Beagle (1831-1836) as the ship\'s naturalist. The 5-year circumnavigation took him along South America and through the Galápagos, and he also read Lyell\'s Principles of Geology during the voyage, absorbing uniformitarianism in real time.'},
            {'label': 'KEY OBSERVATIONS', 'body': 'Darwin collected specimens of Galápagos birds that London ornithologist John GOULD later identified as all FINCHES — the key insight that catalyzed his thinking. Fossil and living armadillos in South America suggested an ancestral connection (descent with modification). The Andes uplift and volcanic island formation gave him first-hand evidence for Lyell\'s deep time.'},
            {'label': 'PUBLICATION TIMELINE', 'body': 'Darwin waited OVER 20 YEARS before publishing — meticulously collecting evidence from barnacles, pigeon breeding, plant hybridization, and biogeography. Alfred Russel WALLACE independently reached identical conclusions; their joint 1858 Linnean Society presentation went unnoticed at the time. Origin of Species was published in 1859.'},
            {'label': 'KEY FIGURES', 'body': 'Charles Darwin, John Gould, Charles Lyell, Alfred Russel Wallace.'},
        ] + slides_to_sections(d, (10, 12)),
        examples=[
            '1831-1836: HMS Beagle circumnavigation. Darwin is 22 at departure.',
            'Galápagos finches: slight morphological differences between islands — a key observation that later fueled natural selection theory.',
            'John Gould (London ornithologist) identified Darwin\'s Galápagos birds as all FINCHES — the insight that led Darwin to see adaptive divergence.',
            'Fossil and living armadillos in South America suggested ancestral connections.',
            'Darwin waited over 20 years before publishing On the Origin of Species (1859), partly due to fear of controversy.',
            'Alfred Russel Wallace independently reached the same conclusions; joint 1858 Linnean Society presentation went unnoticed.',
        ],
        mnemonic='Beagle→Book: 5 years voyage (1831-36) + 23 years thinking = Origin (1859).',
        flashcard={
            'front': 'Why did Darwin wait so long (more than 20 years) to publish his theory of evolution by natural selection?',
            'back': 'Darwin was a meticulous scientist who wanted his argument to be airtight. He spent the decades after the Beagle voyage accumulating evidence from barnacles, pigeon breeding, plant hybridization, biogeography, and correspondence with other naturalists. He also knew the theory would be religiously and socially controversial. He was finally prompted to publish in 1858 when Alfred Russel Wallace independently arrived at the same theory and sent Darwin a manuscript — both read joint papers to the Linnean Society in 1858, and Origin followed in 1859.',
        },
        quiz=[
            {
                'question': 'Darwin\'s Voyage of the Beagle (1831-1836) contributed most directly to his theory because:',
                'correct': 'He observed variation between isolated populations that no single region alone would have revealed',
                'distractors': [
                    'He isolated DNA from island species',
                    'He performed laboratory breeding experiments on finches',
                    'He measured gene frequencies across populations',
                ],
            },
            {
                'question': 'Darwin waited over 20 years after returning from the Beagle voyage before publishing Origin of Species in 1859. What event finally forced his hand?',
                'correct': 'Alfred Russel Wallace independently arrived at the same theory of natural selection and sent Darwin a manuscript — both presented joint papers at the Linnean Society in 1858, prompting Darwin to publish the following year',
                'distractors': [
                    'Charles Lyell threatened to publish his own evolution theory before Darwin, creating a competitive priority dispute that forced Darwin to rush his manuscript to press in 1859',
                    'Darwin\'s data from pigeon-breeding experiments finally met his own rigorous threshold for proof in 1858, which he set at confirming that artificial selection could produce at least 10 distinct varieties within a single decade',
                    'The Catholic Church issued an official condemnation of evolutionary ideas in 1858, which Darwin calculated would suppress the theory permanently unless he published his complete argument immediately',
                ],
            },
            {
                'question': 'Darwin observed Galápagos finches on the voyage, but did not realize their significance until after returning to England. What does this reveal about the scientific process?',
                'correct': 'Scientific insight often requires theoretical frameworks that are not yet available during data collection — Darwin needed years of reading, breeding experiments, and discussion to recognize what his observations meant',
                'distractors': [
                    'Darwin\'s observations were too limited to be scientifically valid — the voyage is overemphasized and his actual theory was developed entirely from library reading after returning to England',
                    'This reveals that the Galápagos finches were NOT actually important to Darwin\'s theory — the tortoise shells and mockingbirds were the key observations, and the finch story is a myth added later',
                    'Darwin did not notice the finches because he was untrained in ornithology — he recognized the finches\' significance only after the ornithologist John Gould identified the specimens as distinct species in London',
                ],
            },
            {
                'question': 'During the Beagle voyage Darwin also observed extinct South American mammals in rock strata that were clearly related to living South American species in the same region. How does this biogeographic pattern support evolution?',
                'correct': 'Related species appearing in the same geographic region across time (in strata) implies descent and modification, not independent creation — the extinct forms are ancestral relatives of the living ones, not unrelated creations placed in the same rocks by chance',
                'distractors': [
                    'This observation supports catastrophism — the extinct forms were destroyed by regional catastrophes and then new, similar forms were created to replace them, which explains the geographic clustering',
                    'The pattern supports special creation because God would naturally use similar "design templates" in the same region for ecological compatibility — unrelated to evolutionary change',
                    'The extinct and living forms look similar because they experience the same South American climate, which independently converges all South American mammals toward the same morphological solutions regardless of ancestry',
                ],
            },
            {
                'question': 'The HMS Beagle voyage lasted from 1831-1836, and Darwin was how old when he departed?',
                'correct': '22 years old — he was a young naturalist at the start of his career when he made the observations that would eventually transform biology',
                'distractors': [
                    '45 years old — he was an experienced senior scientist by the time of the voyage',
                    '15 years old — he was a teenage prodigy still in school',
                    '60 years old — he was already famous and used the voyage to confirm pre-existing theories',
                ],
            },
            {
                'question': 'Origin of Species was published in 1859. Roughly how long did Darwin spend developing his theory after returning from the Beagle voyage in 1836?',
                'correct': 'About 23 years — he spent over two decades accumulating evidence from barnacles, pigeon breeding, plant hybridization, biogeography, and correspondence before publishing',
                'distractors': [
                    'About 2 years — he rushed to publish immediately after returning from the voyage',
                    'About 50 years — he only published after his death was imminent at age 80',
                    'About 5 years — he published shortly after the voyage but spent decades defending the book',
                ],
            },
            {
                'question': 'Which islands provided Darwin with observations of slight morphological differences between populations that later fueled his theory of natural selection?',
                'correct': 'The Galápagos Islands — he observed variation in finch beaks and tortoise shells between islands that, in retrospect, suggested adaptive divergence',
                'distractors': [
                    'The Caribbean Islands — where he documented parrot color variation',
                    'The Hawaiian Islands — where he first observed silversword plants',
                    'The Falkland Islands — where he recorded penguin populations',
                ],
            },
            {
                'question': 'On the Beagle voyage Darwin also directly experienced geological phenomena that supported Lyell\'s uniformitarianism — including the Andes uplift and volcanic island formation. How did these observations support his later evolutionary thinking?',
                'correct': 'They gave Darwin first-hand evidence that geological processes are ongoing and gradual, supporting Lyell\'s deep-time view — which provided the enormous timescale needed for natural selection to produce species-level differences',
                'distractors': [
                    'They convinced Darwin that catastrophism was correct and that species arise suddenly after catastrophic events',
                    'They proved that the Earth is only 6,000 years old, forcing Darwin to develop rapid-speciation theories',
                    'They were unrelated to evolution — Darwin\'s geological observations had no influence on his biological thinking',
                ],
            },
            {
                'question': 'L1 RECALL: Which London-based ornithologist identified Darwin\'s Galápagos birds as all belonging to the finch group — a critical insight that helped Darwin recognize adaptive divergence between islands?',
                'correct': 'John Gould',
                'distractors': [
                    'Thomas Huxley',
                    'Alfred Russel Wallace',
                    'Charles Lyell',
                ],
            },
            {
                'question': 'L3 COMPARISON: Which statement best describes the role of Alfred Russel Wallace in the publication history of evolutionary theory?',
                'correct': 'Wallace independently arrived at a theory nearly identical to Darwin\'s natural selection; their joint 1858 Linnean Society presentation preceded Darwin\'s 1859 Origin of Species',
                'distractors': [
                    'Wallace disputed Darwin\'s theory and proposed an alternative based on Lamarckian inheritance',
                    'Wallace was Darwin\'s graduate student and merely assisted with data collection',
                    'Wallace lived in the 20th century and reinterpreted Darwin\'s theory posthumously',
                ],
            },
        ],
        visual={
            'type': 'bullet',
            'description': 'Key Beagle observations',
            'regions': [
                {'label': 'Observations', 'color': '#7de2d1', 'items': ['Finch variation across islands', 'Fossils of extinct mammals', 'Volcanic island formation', 'Andes uplift']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'FIVA: Finches, Island biogeography, Volcanoes, Andes.',
            'trap': 'Darwin did not "see evolution in action" on the Beagle — he built the theory later from the totality of his observations.',
        },
    ))
    nodes.append(build_node(
        id='lec2-natural-selection-ingredients',
        title='Natural Selection: The Four Ingredients',
        subtitle='Variation, heritability, differential reproduction → evolution (Lec 2 slides 13-23)',
        color='blue', row=2,
        heading='Lecture 2 — The Logic of Natural Selection',
        sections=[
            {'label': 'CORE CONCEPT', 'body': 'Darwin drew on Thomas Malthus (1766-1834), who observed that populations reproduce exponentially while resources are finite. Reproductive potential examples: aphids could produce 524 billion offspring in 1 year; elephants could produce 19 million in 750 years; Staphylococcus would cover Earth 7 feet deep in 24 hours. Populations do NOT grow exponentially in reality because resources constrain survival — creating a struggle for existence.'},
            {'label': 'THE FIVE INGREDIENTS', 'body': '(1) High reproductive potential. (2) Population size remains roughly stable. (3) Resources are limited → struggle to survive. (4) Phenotypic variation among individuals. (5) Heritability of that variation. INFERENCE: survival and reproduction are therefore NONRANDOM with respect to phenotype. FITNESS = ability to survive and reproduce RELATIVE to others. ADAPTATION = a trait that increases fitness relative to individuals without it.'},
            {'label': 'KEY TERMS', 'body': 'Phenotypic variation, heritability, Malthusian overproduction, differential reproductive success, fitness (relative), adaptation.'},
        ] + slides_to_sections(d, (13, 23)),
        examples=[
            'Variation: individuals in a population differ in traits (beak size, coat color, etc.)',
            'Heritability: offspring resemble parents more than unrelated individuals.',
            'Differential reproductive success: some variants leave more descendants.',
            'Inference: the successful variants\' traits become more common each generation.',
            'Reproductive potential: Staphylococcus would cover Earth 7 feet deep in 24 hours if unconstrained; elephants could produce 19 million descendants in 750 years.',
        ],
        warnings=[
            'WATCH OUT: If ANY ingredient is missing, natural selection cannot occur. Non-heritable differences (e.g., sunburn) do not evolve.',
            'WATCH OUT: Natural selection acts on PHENOTYPES, but evolution is measured as ALLELE FREQUENCY CHANGE at the genotype level.',
        ],
        mnemonic='VHI-DRS = Variation + Heritability + Inference-from-Differential-Reproductive-Success = Evolution.',
        flashcard={
            'front': 'What are the four necessary ingredients for evolution by natural selection, and what is the logical inference that follows from combining them?',
            'back': '(1) Phenotypic variation among individuals; (2) Heritability of that variation (offspring resemble parents); (3) Differential survival and reproduction based on phenotype (i.e., fitness differences); (4) More offspring produced than can survive (Malthusian overproduction). INFERENCE: The phenotypes linked to higher fitness will become more common each generation — the population evolves. If ANY ingredient is missing, no evolution by natural selection occurs.',
        },
        quiz=[
            {
                'question': 'A population of plants shows variation in leaf shape, but leaf shape is entirely determined by soil chemistry and not passed from parent to offspring. Can natural selection act on this variation?',
                'correct': 'No — without heritability, differential reproduction will not change allele frequencies',
                'distractors': [
                    'Yes — any phenotypic variation is sufficient for evolution by natural selection',
                    'Yes — but only if the variation produces differences in germination rate',
                    'No — but only because plants reproduce vegetatively rather than sexually',
                ],
            },
            {
                'question': 'A zookeeper breeds the longest-necked giraffes each generation for 15 generations. Average neck length DOES increase. What does this ALONE confirm about natural selection\'s four ingredients?',
                'correct': 'It confirms variation exists and that differential reproduction on neck length produced a response (R > 0) — but it does NOT confirm whether the force causing the change in the wild is predation, competition for high foliage, or sexual selection, which must be tested separately',
                'distractors': [
                    'It confirms all four ingredients of natural selection: variation, heritability, differential reproduction, and overproduction — because the response was observed, all must be present',
                    'It confirms only that neck length is heritable — the zookeeper\'s experiment is functionally equivalent to measuring parent-offspring regression, the gold standard for estimating h²',
                    'It does not confirm any ingredient of natural selection because artificial selection by a zookeeper does not count as natural selection — only wild populations experiencing predation or drought qualify',
                ],
            },
            {
                'question': 'Which scenario violates the requirement for DIFFERENTIAL REPRODUCTIVE SUCCESS but satisfies variation and heritability?',
                'correct': 'A population of beetles varies in shell color (heritable), but predatory birds hunt randomly and do not preferentially eat any color — survival and reproduction are equal across color variants',
                'distractors': [
                    'A population of bacteria varies in antibiotic resistance due to plasmid acquisition; the resistance trait cannot be passed to daughter cells because plasmids are lost during binary fission',
                    'A population of fish varies in body size (heritable), but all fish die at age 1 due to a sudden winter freeze before any reproduce — removing all selection pressure',
                    'A population of mice lives in a perfectly uniform environment with no predators and unlimited food; variation in fur color exists but individuals do not differ in reproductive success because there is nothing to select against',
                ],
            },
            {
                'question': 'Darwin\'s inference from the four ingredients was: "the successful variants\' traits will become more common." What makes this an INFERENCE rather than a direct observation, and what experiment would make it a direct observation?',
                'correct': 'It is an inference because we do not directly observe allele frequencies changing — we observe phenotype-fitness correlations. A direct test requires measuring allele frequencies before and after selection in a marked population (like the Grant finch study) and confirming R = h²S predicts the observed change',
                'distractors': [
                    'It is an inference only because Darwin lacked microscopes — with modern sequencing we can directly observe the variation ingredient, making the whole argument observational rather than inferential',
                    'It is an inference because differential reproduction is unobservable in wild populations — only lab experiments can directly measure which variants reproduce more, so field evolution is always inferred, never observed',
                    'It is not an inference at all — observing a changed population after several generations IS direct observation of evolution by natural selection, requiring no additional experimental confirmation',
                ],
            },
            {
                'question': 'Darwin drew on Malthus\'s observation about population growth for his fourth ingredient: overproduction. What is the logical role of "more offspring produced than can survive" in the natural selection argument?',
                'correct': 'Overproduction ensures that not all offspring can survive — creating a selective filter that differentiates between those with advantageous traits and those without, which is what "differential survival" requires',
                'distractors': [
                    'Overproduction directly causes mutations — the pressure to reproduce rapidly forces DNA to mutate at higher rates in stressed populations',
                    'Overproduction is needed to satisfy Hardy-Weinberg equilibrium, which requires a minimum offspring count per generation',
                    'Overproduction is irrelevant — natural selection operates equally well when exactly one offspring per parent survives',
                ],
            },
            {
                'question': 'Natural selection acts on which level, and evolution is measured at which level?',
                'correct': 'Natural selection acts on PHENOTYPES (individuals with their traits face environmental challenges), but evolution is measured as changes in ALLELE FREQUENCIES at the GENOTYPE level',
                'distractors': [
                    'Both selection and evolution act on alleles directly — phenotypes are irrelevant because DNA is what matters',
                    'Both selection and evolution act on whole populations simultaneously — individuals and their genes are never the unit of analysis',
                    'Selection acts on species, and evolution is measured as the rate of speciation across geological time',
                ],
            },
            {
                'question': 'A student claims that natural selection "creates" new traits by designing them for the environment. Why is this a misconception?',
                'correct': 'Natural selection only SORTS among existing variants — it cannot create new traits. The source of new variation is mutation (plus recombination and gene flow); selection just favors some pre-existing variants over others',
                'distractors': [
                    'The student is correct — selection can directly create new traits by modifying DNA in response to environmental pressure',
                    'The student is wrong only because selection creates traits slowly rather than quickly — otherwise the claim is correct',
                    'The student is correct when selection is strong, but not when it is weak — strong selection can induce new beneficial mutations',
                ],
            },
            {
                'question': 'If a population has variation in a trait, that variation is heritable, AND there is differential reproductive success based on that trait, what is the INEVITABLE outcome according to Darwin\'s logic?',
                'correct': 'The population will evolve — the variants with higher fitness will become more common each generation, shifting the population mean',
                'distractors': [
                    'The population will only evolve if natural selection is strong — weak selection produces no detectable change',
                    'The population will only evolve if the environment is changing — stable environments produce no evolution even with all four ingredients present',
                    'Nothing will happen — these three ingredients are necessary but not sufficient; a fourth requirement (mutation) must also be met',
                ],
            },
            {
                'question': 'L1 RECALL: Which 18th-19th century economist\'s work on population growth directly influenced Darwin\'s thinking on the "struggle for existence"?',
                'correct': 'Thomas Malthus (1766-1834)',
                'distractors': [
                    'Adam Smith',
                    'John Stuart Mill',
                    'Karl Marx',
                ],
            },
            {
                'question': 'L1 RECALL: Which example is given in lecture to illustrate extreme reproductive potential — a bacterium that, unconstrained, would cover Earth 7 feet deep in 24 hours?',
                'correct': 'Staphylococcus',
                'distractors': [
                    'E. coli',
                    'Streptococcus pneumoniae',
                    'Bacillus subtilis',
                ],
            },
            {
                'question': 'L3 COMPARISON: How is FITNESS defined in the context of natural selection?',
                'correct': 'The ability to survive and reproduce RELATIVE to others in the population — it is always a relative, not absolute, measure',
                'distractors': [
                    'The absolute number of offspring an individual produces in its lifetime',
                    'Physical strength and endurance, as measured by athletic performance tests',
                    'The longevity of an individual, independent of its reproductive success',
                ],
            },
        ],
        visual={
            'type': 'cycle',
            'description': 'The natural selection cycle',
            'regions': [
                {'label': '1. Variation', 'color': '#4ea8de', 'items': ['Phenotypic differences among individuals']},
                {'label': '2. Heritability', 'color': '#7de2d1', 'items': ['Traits passed to offspring']},
                {'label': '3. Overproduction', 'color': '#ffc857', 'items': ['More offspring than can survive']},
                {'label': '4. Differential fitness', 'color': '#ff6b6b', 'items': ['Some variants survive/reproduce more']},
                {'label': '5. Next generation', 'color': '#8a5cf6', 'items': ['Winning variants more common']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'VHOD→N: Variation, Heritability, Overproduction, Differential fitness → Next generation changed.',
            'trap': 'Natural selection does NOT produce traits — it only sorts among existing variants. The source of variation is mutation + recombination.',
        },
        diagram=darwin_five_ingredients_diagram(),
    ))
    nodes.append(build_node(
        id='lec2-finches-case',
        title='Galápagos Finches: Selection Case Study',
        subtitle='Grant & Grant beak size evolution (Lec 2 slides 24-31)',
        color='green', row=2,
        heading='Lecture 2 — Evolution of Beak Shape in Galápagos Finches',
        sections=[
            {'label': 'CORE CONCEPT', 'body': 'Peter and Rosemary Grant studied Geospiza fortis (medium ground finch) on Daphne Major in the Galápagos for decades. They directly measured all four conditions of natural selection on beak depth: (1) VARIATION — beak depth varied among individuals; (2) HERITABILITY — parent-offspring regression yielded h² ≈ 0.65-0.8; (3) DIFFERENTIAL SURVIVAL — during the 1977 drought, 89% of the population died before breeding; (4) NON-RANDOM SURVIVAL with respect to beak depth.'},
            {'label': 'MECHANISM', 'body': 'The 1977 drought killed small-seed plants, leaving only large, hard seeds (Tribulus cistoides). Deeper-beaked birds survived because they could crack these seeds. The next generation had a larger average beak depth — directly measured evolution by natural selection. Sexual selection also contributes to beak evolution in finches.'},
            {'label': 'KEY FIGURES', 'body': 'Peter Grant, Rosemary Grant.'},
        ] + slides_to_sections(d, (24, 31)),
        examples=[
            'Peter and Rosemary Grant measured beak depth in Geospiza fortis on Daphne Major across decades.',
            '1977 drought: small soft seeds disappeared; only large hard seeds (Tribulus cistoides) remained. 89% of the population died before breeding.',
            'Next generation had significantly larger average beak size — directly measured evolution by natural selection.',
            'Heritability of beak depth measured by parent-offspring regression: h² ≈ 0.65-0.8.',
        ],
        warnings=[
            'WATCH OUT: The Grant finch study showed selection REVERSED in wet years — larger beaks were selected AGAINST when small seeds dominated again. Selection direction tracks the environment, NOT unidirectional.',
            'WATCH OUT: Heritability of beak depth (h² ≈ 0.65-0.8) was MEASURED by parent-offspring regression, not assumed. Without measuring heritability, you cannot confirm the R = h²S prediction.',
        ],
        mnemonic='4 conditions confirmed: Variable beaks, Heritable beaks, Survival differences, Beak size mattered.',
        flashcard={
            'front': 'How did the Grants\' Galápagos finch study provide direct empirical evidence for each ingredient of natural selection?',
            'back': '(1) VARIATION: Beak depth varied among individual Geospiza fortis. (2) HERITABILITY: Parent-offspring regression showed beak depth is heritable (h² ≈ 0.65-0.8). (3) DIFFERENTIAL SURVIVAL: During the 1977 drought, birds with deeper beaks ate hard Tribulus seeds and survived while smaller-beaked birds died. (4) INFERENCE CONFIRMED: The next generation had significantly larger average beak depth — selection was measured, not inferred.',
        },
        quiz=[
            {
                'question': 'In the Grant finch study, what was the selective pressure that drove evolution of larger beaks in 1977?',
                'correct': 'A drought eliminated small, soft seeds, leaving mostly large, hard seeds that only birds with deep beaks could crack',
                'distractors': [
                    'A new predator preferred small-beaked birds',
                    'Birds intentionally grew larger beaks during the drought',
                    'Climate cooling caused beaks to grow larger',
                ],
            },
            {
                'question': 'After the 1977 drought the Grants observed that the Geospiza fortis population had larger average beaks. When wet years returned in the early 1980s, beak size started shifting BACK toward smaller. What does this pattern most directly demonstrate?',
                'correct': 'Natural selection is not unidirectional — the direction of selection tracks the current environment. Larger beaks are favored only when hard seeds dominate; smaller beaks are favored when small soft seeds are abundant again',
                'distractors': [
                    'Genetic drift reversed the 1977 selection because the finch population was still small enough after the drought for random sampling to overcome directional selection',
                    'The birds that survived the drought mated with immigrants from nearby islands who had smaller beaks, and gene flow reversed the evolutionary change',
                    'Beaks regressed to their pre-drought size because heritability of beak depth is close to zero — the 1977 change was environmental, not genetic, and disappeared when the environment normalized',
                ],
            },
            {
                'question': 'The Grant study measured beak heritability using parent-offspring regression and found h² ≈ 0.65-0.8. Why is measuring h² essential for confirming that the beak-size change across the 1977-78 drought was evolution by natural selection, rather than just environmental change?',
                'correct': 'Without confirming h² > 0, the beak-size shift could reflect individual developmental plasticity (birds eating harder seeds grow deeper beaks) rather than a true change in allele frequencies — heritability measurement proves the response was genetic',
                'distractors': [
                    'Without h², we cannot calculate the selection differential S — and without S we cannot confirm that predation pressure was acting in the correct direction to drive larger beaks',
                    'Heritability measurement is not necessary to confirm natural selection — it is only needed if you want to predict the response in the next generation using the breeders equation R = h²S',
                    'Without h², we cannot distinguish natural selection from genetic drift — only by confirming h² > 0 can we rule out that the beak-size shift was caused by random sampling in the small post-drought population',
                ],
            },
            {
                'question': 'During the 1977 drought, researchers observed that Tribulus cistoides (large-seeded plant) dominated the available food. If the Grants had NOT measured food supply, beak heritability, AND survival rates separately, which alternative explanation could NOT be ruled out?',
                'correct': 'A phenotype-fitness correlation alone could be explained by an environmental confound — perhaps well-nourished birds are both bigger-beaked AND survive better, with diet (not beak size) causing the survival difference',
                'distractors': [
                    'Without measuring food supply, we could not rule out that beak size increased due to hybridization with the larger-beaked G. magnirostris arriving from another island during the drought',
                    'Without measuring heritability, we could not rule out that beak size evolved through sexual selection rather than food-based selection — females may have preferred larger-beaked males specifically during drought years',
                    'Without measuring survival rates, we could not rule out that all finches survived the drought equally and the apparent evolutionary change was caused entirely by immigration of larger-beaked birds from other Galápagos islands',
                ],
            },
            {
                'question': 'The species of finch studied by Peter and Rosemary Grant on Daphne Major was:',
                'correct': 'Geospiza fortis — the medium ground finch',
                'distractors': [
                    'Geospiza magnirostris — the large ground finch',
                    'Darwin\'s rosy finch — a Hawaiian species',
                    'Carduelis galapagensis — the Galápagos goldfinch',
                ],
            },
            {
                'question': 'The Grants measured beak depth heritability using parent-offspring regression. What specific value range did they find for h² in Geospiza fortis?',
                'correct': 'h² ≈ 0.65-0.8 — meaning the majority of variation in beak depth is additive genetic variance that will respond to selection',
                'distractors': [
                    'h² ≈ 0.1-0.2 — meaning beak depth is mostly environmentally determined',
                    'h² = 1.0 — meaning beak depth is completely determined by genetics with no environmental influence',
                    'h² ≈ 0.5 exactly — the default value assumed for all quantitative traits',
                ],
            },
            {
                'question': 'The Grant finch study is often cited as the FIRST direct measurement of evolution by natural selection in a wild vertebrate population. What made it the first of its kind?',
                'correct': 'All four ingredients of natural selection were measured in the same population simultaneously — variation, heritability, differential survival, and response across generations — with quantitative data for each',
                'distractors': [
                    'It was the first evolution study to use genetic sequencing to measure allele frequencies directly across generations',
                    'It was the first evolution study conducted on a vertebrate — all previous studies used insects and microorganisms exclusively',
                    'It was the first evolution study to be conducted on the Galápagos Islands since Darwin\'s original voyage',
                ],
            },
            {
                'question': 'Which hard-seeded plant species is most directly associated with the 1977 drought selection event on beak size in G. fortis?',
                'correct': 'Tribulus cistoides — whose large, hard seeds dominated the food supply during the drought and could only be cracked by birds with sufficiently deep beaks',
                'distractors': [
                    'Arabidopsis thaliana — a model plant with small soft seeds',
                    'Opuntia cactus — whose fruits are the main year-round food',
                    'Scalesia pedunculata — a soft-bodied daisy tree',
                ],
            },
            {
                'question': 'L1 RECALL: What percentage of the Daphne Major finch population died before breeding during the 1977 drought?',
                'correct': '89%',
                'distractors': ['25%', '50%', '99%'],
            },
            {
                'question': 'L5 SYNTHESIS: In the Grant finch study, the measured value of h² was in what range — and what does this mean for response to selection?',
                'correct': 'h² ≈ 0.65-0.8, meaning most of the phenotypic variance in beak depth is additive genetic variance — so selection produces a substantial response each generation (R = h²S)',
                'distractors': [
                    'h² ≈ 0.1-0.2, meaning there is almost no genetic contribution — most variation is environmental and no response to selection is expected',
                    'h² = 0, meaning beak depth is entirely environmentally determined and cannot evolve',
                    'h² = 1, meaning beak depth is entirely genetic with zero environmental influence',
                ],
            },
            {
                'question': 'L2 MECHANISM: Besides food-mediated natural selection, which OTHER form of selection contributes to beak evolution in Geospiza finches, as discussed in lecture?',
                'correct': 'Sexual selection — mate choice also influences which beak morphologies reproduce most successfully',
                'distractors': [
                    'Kin selection between siblings on the same nest',
                    'Group selection at the island-level',
                    'Meiotic drive that biases beak alleles in gamete production',
                ],
            },
        ],
        visual={
            'type': 'before-after',
            'description': 'Drought-driven selection on beak size',
            'regions': [
                {'label': 'Pre-drought (1976)', 'color': '#7de2d1', 'items': ['Diverse seed sizes', 'Beak depth ~9.2 mm average']},
                {'label': 'Drought (1977)', 'color': '#ff6b6b', 'items': ['Only large hard seeds remain', 'Selection against small beaks']},
                {'label': 'Post-drought (1978)', 'color': '#4ea8de', 'items': ['Average beak depth shifted larger', '~4% increase measured']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Drought → Hard seeds → Deep beaks win.',
            'trap': 'After the drought ended, selection sometimes reversed direction (wet years favored smaller beaks). Selection is not unidirectional — it tracks environment.',
        },
    diagram=peppered_moth_selection_diagram(),
    ))
    nodes.append(build_node(
        id='lec2-descent-modification',
        title='Descent with Modification & Common Ancestry',
        subtitle='Artificial selection, homology, tree-thinking (Lec 2 slides 32-41)',
        color='pink', row=2,
        heading='Lecture 2 — Descent with Modification',
        sections=[
            {'label': 'CORE CONCEPT', 'body': 'Darwin\'s FIVE KEY POINTS about natural selection: (1) selection acts on individuals but consequences are seen in populations; (2) it acts on phenotypes, while evolution is measured as allele frequency change; (3) it is NOT forward-looking; (4) it results in descent with modification; (5) it is NOT progressive or linear — there is no higher or lower; (6) it does NOT lead to perfection.'},
            {'label': 'HOMOLOGY', 'body': 'Shared structures inherited from a common ancestor. Forelimb homology: whale flipper, bat wing, human arm, and dog foreleg all have the same bone arrangement (humerus, radius, ulna, carpals, phalanges). Embryonic homologies: pharyngeal arches and notochord appear in all vertebrate embryos. Contrast with ANALOGY (bird wing vs insect wing — same function, different origins).'},
            {'label': 'ARTIFICIAL SELECTION', 'body': 'Brassica oleracea gave rise to cabbage, broccoli, kale, Brussels sprouts, and kohlrabi — all one species, selected for different traits. Dogs came from wolves. Corn (maize) descends from teosinte.'},
            {'label': 'VESTIGIAL ORGANS', 'body': 'Reduced but still present ancestral structures: whale pelvic bones, human appendix, cave-fish eye sockets, human arrector pili (goosebump) muscles.'},
        ] + slides_to_sections(d, (32, 41)),
        examples=[
            'Artificial selection on dogs (from wolves), cabbage/broccoli/kale/Brussels sprouts/kohlrabi (all Brassica oleracea cultivars), corn (from teosinte) — proves phenotypes can be dramatically reshaped by selection in few generations.',
            'Vertebrate forelimb homology: whale flipper, bat wing, human arm, dog foreleg — same bones in same arrangement.',
            'Vertebrate embryonic homologies: pharyngeal arches, notochord — shared developmental stages reveal common ancestry.',
            'Vestigial organs: whale pelvis, human appendix, cave-fish eyes, arrector pili muscles.',
        ],
        warnings=[
            'WATCH OUT: The "march of progress" image (ape → human) is MISLEADING — evolution is branching, not linear. Humans did NOT evolve FROM modern chimpanzees; we share a common ancestor.',
        ],
        mnemonic='DHA-V = Descent + Homology + Artificial selection + Vestigial organs = evidence for common ancestry.',
        flashcard={
            'front': 'How do vestigial organs provide evidence for descent with modification?',
            'back': 'Vestigial organs (e.g., whale hip bones, human appendix, flightless bird wings, cave fish eye sockets) are structures that have lost their original function but persist as reduced, functionless remnants. Their existence is only explicable under descent with modification: an ancestor used the structure, selection pressure for that function was relaxed, and the structure degraded over generations but was not fully eliminated. Under special creation, these "useless" structures would require ad-hoc explanations.',
        },
        quiz=[
            {
                'question': 'Which evidence most directly refutes the "march of progress" interpretation of evolution?',
                'correct': 'Phylogenies show evolution is a branching tree, with modern species as tips — not a linear sequence',
                'distractors': [
                    'Mutations never happen in modern populations',
                    'All modern species are equally ancient',
                    'Fossils are rare and poorly preserved',
                ],
            },
            {
                'question': 'All cultivated cabbages — broccoli, kohlrabi, kale, cauliflower, Brussels sprouts — are varieties of the single species Brassica oleracea, produced by artificial selection. What does this most directly demonstrate about evolution?',
                'correct': 'Selection acting on standing genetic variation can produce dramatically different phenotypes within a species over relatively few generations — proving the raw material for evolution exists and responds to selection',
                'distractors': [
                    'Artificial selection proves that natural selection cannot produce such large morphological changes — humans are far more effective at directing evolution than natural forces could be',
                    'All Brassica cultivars are evidence of convergent evolution — each vegetable type independently evolved the same solution to the problem of being domesticated by humans',
                    'The Brassica example demonstrates Lamarckian inheritance — farmers selected plants they wanted, and those plants responded by producing offspring with the desired traits in the next generation',
                ],
            },
            {
                'question': 'Whale pelvic bones are vestigial — they are present but non-functional remnants of hindlimb bones. Occasionally a whale is born with small external hind-flipper nubs. What does this phenotypic reappearance ("atavism") most directly show?',
                'correct': 'The genetic pathways for hindlimb development still exist in the whale genome but are normally suppressed during development — vestigial organs can reappear when regulatory control breaks down, confirming descent from limbed ancestors',
                'distractors': [
                    'Atavisms disprove descent with modification — if whales truly descended from limbed ancestors, these developmental programs would have been completely deleted from the genome over millions of years',
                    'Whale hindlimb nubs are evidence of a Lamarckian reversion — the whale\'s body is reverting to an ancestral form because it perceives environmental pressure to walk on land again',
                    'Atavisms are purely random developmental errors with no evolutionary significance — the hindlimb nubs are caused by radiation-induced mutations during embryogenesis, unrelated to ancestry',
                ],
            },
            {
                'question': 'The vertebrate forelimb bones (humerus, radius, ulna, carpals, phalanges) appear in bat wings, whale flippers, human arms, horse legs, and bird wings — all with the same set of bones in the same positional arrangement. This structural HOMOLOGY is BEST explained by:',
                'correct': 'All tetrapods inherited the same forelimb bone developmental program from a common ancestor — the bones were modified by natural selection for different functions (flying, swimming, grasping, running) while the underlying developmental program remained conserved',
                'distractors': [
                    'Convergent evolution: all tetrapods independently evolved the same forelimb bone configuration because it is the optimal engineering solution for weight-bearing appendages',
                    'Parallel evolution: the same mutation in the same Hox gene occurred independently in all tetrapod lineages, producing identical forelimb configurations by chance',
                    'Natural selection is extremely constrained and can only produce one forelimb configuration — the homologous structure reflects a developmental constraint rather than shared ancestry',
                ],
            },
            {
                'question': 'Vertebrate embryos share features like pharyngeal arches and notochord early in development, but these features are modified differently later in development across species. What does this pattern demonstrate?',
                'correct': 'Developmental homologies reveal shared ancestry — the early developmental stages are conserved because they inherit the same basic body plan from a common ancestor, while later stages diverge to produce species-specific features',
                'distractors': [
                    'All vertebrates go through an adult "fish stage" at some point in their lives, supporting a strict Haeckelian recapitulation theory',
                    'Embryonic similarities are coincidences with no evolutionary meaning — different species independently develop similar structures at similar times by chance',
                    'Pharyngeal arches and notochord are still functional in adult humans and mammals, proving that vertebrates never really diverged from their aquatic ancestors',
                ],
            },
            {
                'question': 'Humans and chimpanzees share approximately what proportion of their DNA?',
                'correct': '~98.7% — but this does NOT mean humans evolved FROM modern chimps; instead, we share a common ancestor ~7 million years ago',
                'distractors': [
                    '~98.7% — which means humans evolved directly from chimps and are therefore just highly evolved chimpanzees',
                    '~50% — making us more distant from chimps than from bananas',
                    '~100% — there is no genetic difference between humans and chimps, only environmental differences',
                ],
            },
            {
                'question': 'The "march of progress" iconography (ape → hominid → modern human in a linear sequence) is popular but misleading. What aspect of evolutionary theory does it most seriously misrepresent?',
                'correct': 'It portrays evolution as a linear, directional progression toward a "higher" endpoint, when in reality evolution is a branching tree with modern species at the tips — all equally "evolved" from ancestral lineages',
                'distractors': [
                    'It incorrectly shows apes as extinct — modern apes still exist and share a common ancestor with humans',
                    'It depicts humans walking upright, when in fact bipedalism evolved only recently and is not a defining trait of the human lineage',
                    'It shows too many transitional forms — fossil data actually show sudden, not gradual, transitions between hominid species',
                ],
            },
            {
                'question': 'A researcher finds that the human appendix, whale pelvic bones, and cave-fish eye sockets are all described as "vestigial organs." What do these have in common evolutionarily?',
                'correct': 'All are reduced, largely non-functional remnants of structures that were fully functional in ancestral populations — their persistence reveals descent from ancestors in which they served specific functions',
                'distractors': [
                    'All are completely useless and prove that evolution is imperfect at removing unnecessary structures',
                    'All will be completely eliminated within the next 100 generations as selection continues to remove them',
                    'All are examples of Lamarckian disuse — individuals who did not use these structures passed on shortened versions to their offspring',
                ],
            },
            {
                'question': 'L1 RECALL: From which wild ancestor is domesticated corn (maize) descended?',
                'correct': 'Teosinte — a wild Mexican grass that was artificially selected over thousands of years into modern corn',
                'distractors': [
                    'Wheat (Triticum aestivum)',
                    'Rice (Oryza sativa)',
                    'Sorghum — a related wild grass',
                ],
            },
            {
                'question': 'L4 APPLICATION: A farmer notices his pig has vestigial "dew claws" on its feet — small, non-functional digits higher up on the leg. How should this be interpreted evolutionarily?',
                'correct': 'The dew claws are vestigial remnants of ancestral digits that were functional in earlier ungulate ancestors — their persistence in reduced form is direct evidence of descent with modification',
                'distractors': [
                    'The dew claws arose by a recent mutation and will become fully functional digits in future generations if selected',
                    'The dew claws are evidence of special creation — they have no evolutionary explanation and must have been placed there intentionally',
                    'The dew claws are a Lamarckian response to walking on soft ground, where the pig\'s ancestors failed to use extra digits',
                ],
            },
        ],
        visual={
            'type': 'tree',
            'description': 'Branching vs linear models of evolution',
            'regions': [
                {'label': 'WRONG: linear', 'color': '#ff6b6b', 'items': ['Implies progress toward humans', 'Implies modern species are primitive', 'Hides branching diversity']},
                {'label': 'RIGHT: branching tree', 'color': '#7de2d1', 'items': ['Common ancestors at internal nodes', 'Modern species at tips', 'All tips equally "modern"']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Tree not ladder.',
            'trap': 'Humans are not descended from chimps — humans and chimps share a common ancestor ~7 million years ago.',
        },
    diagram=tree_thinking_components_diagram(),
    ))
    return nodes


def lec3_nodes():
    d = load_lec('lec3')
    nodes = []
    nodes.append(build_node(
        id='lec3-genes-proteins',
        title='Genes, Proteins & Gene Expression',
        subtitle='DNA-RNA-protein and regulatory networks (Lec 3 slides 1-9)',
        color='blue', row=3,
        heading='Lecture 3 — Genes and Heritable Variation',
        sections=[
            {'label': 'CORE CONCEPT', 'body': 'The CENTRAL DOGMA of molecular biology: DNA → RNA → Protein. Transcription is carried out by RNA polymerase; translation is carried out by the ribosome. The universal use of DNA, RNA, and protein across all three domains of life (bacteria, archaea, eukaryotes) is itself a homology — strong evidence of common ancestry.'},
            {'label': 'KEY EXAMPLE: HUMAN CHROMOSOME 2', 'body': 'Humans have 23 chromosome pairs; great apes have 24. Human chromosome 2 is the FUSION product of two ancestral ape chromosomes — it contains two centromeres (one vestigial) and fused telomeric sequences internally, confirming the fusion.'},
            {'label': 'REGULATION', 'body': 'Gene expression is regulated by histones (chromatin state), transcription factors, hormones, and environmental signals. Dolphin hindlimb genes are STILL PRESENT in the genome but transcriptionally SILENCED — showing that evolutionary loss of a trait can occur via regulation rather than gene deletion.'},
        ] + slides_to_sections(d, (1, 9)),
        examples=[
            'DNA is a universal homology across all life — the code itself is evidence of common ancestry.',
            'Human chromosome 2 is the fusion of two ancestral ape chromosomes (has 2 centromeres, one vestigial).',
            'Dolphin hindlimb genes are still present but transcriptionally silenced — regulation, not gene loss, explains limb absence.',
            'Gene expression is regulated by complex networks: enhancers, transcription factors, histones, hormones, environment.',
        ],
        warnings=[
            'WATCH OUT: The central dogma (DNA → RNA → Protein) does NOT mean every gene is always expressed. Regulation determines which genes are ON or OFF.',
            'WATCH OUT: Reverse transcription (retroviruses, retrotransposons) does NOT contradict the central dogma — the dogma describes the direction of information flow, not an absolute prohibition.',
        ],
        mnemonic='DNA → RNA → Protein, but REGULATION determines phenotype.',
        flashcard={
            'front': 'Why are dolphin hindlimb genes a surprising illustration of gene expression regulation?',
            'back': 'Dolphins are limbless in hindquarters, but genomic sequencing reveals the genes for building hindlimbs are still present in their DNA. Their hindlimbs do not develop because the regulatory pathway controlling limb outgrowth is suppressed during development — not because the genes were deleted. This shows that evolution can "lose" traits not by removing genes but by changing expression patterns. Occasionally, a dolphin is born with vestigial hindlimbs, revealing the dormant genetic capacity.',
        },
        quiz=[
            {
                'question': 'The observation that DNA is used as the hereditary molecule in all domains of life (bacteria, archaea, eukaryotes) is evidence for:',
                'correct': 'Common ancestry of all extant life',
                'distractors': [
                    'Independent origins of each domain',
                    'Convergent molecular evolution',
                    'Horizontal gene transfer eliminating other molecules',
                ],
            },
            {
                'question': 'Dolphins do not have hindlimbs, yet their genomes contain the full set of hindlimb developmental genes. Occasionally, a dolphin is born with small external flipper nubs at the hindquarter. What does this most directly demonstrate about the relationship between genes and phenotype?',
                'correct': 'The same genome can produce different phenotypes depending on WHICH genes are expressed — evolution can "silence" traits by changing regulatory control without deleting the underlying genes',
                'distractors': [
                    'It demonstrates that dolphin hindlimb genes have accumulated enough mutations to become pseudogenes — they are present but non-functional, and the rare flipper nubs represent random developmental noise',
                    'It proves that acquired traits can be inherited — dolphins lost their hindlimbs through Lamarckian disuse, but the genes were never fully eliminated, causing occasional reversions in offspring',
                    'It demonstrates that genomic drift is the primary cause of limb loss in cetaceans — the hindlimb genes are present by chance, not because they were actively conserved under any selective pressure',
                ],
            },
            {
                'question': 'The "central dogma" states DNA → RNA → protein. A student claims retroviruses like HIV violate the central dogma because they convert RNA back to DNA using reverse transcriptase. Is the student correct?',
                'correct': 'The student is incorrect — the central dogma refers to the direction of SEQUENCE INFORMATION in normal protein synthesis. Reverse transcription does not violate it because the dogma also explicitly allows RNA → DNA as a special transfer; what it prohibits is protein → nucleic acid information flow',
                'distractors': [
                    'The student is correct — reverse transcriptase is a major exception to the central dogma because DNA was supposed to be the starting point for all information flow, not RNA',
                    'The student is incorrect — HIV is not a true retrovirus because it lacks ribosomes and cannot perform its own protein synthesis; it relies entirely on host cell machinery, so the central dogma applies only to host cell processes',
                    'The student is correct — the central dogma was specifically designed to describe eukaryotic cells; viral systems like HIV use completely different information flow rules that operate independently of the dogma',
                ],
            },
            {
                'question': 'Two organisms have identical DNA sequences at a protein-coding gene, yet one has much higher levels of the encoded protein than the other. What type of variation is responsible, and does this violate the central dogma?',
                'correct': 'Regulatory variation — differences in transcription factor binding sites, enhancers, or silencers upstream of the gene cause different transcription rates. This does NOT violate the central dogma, which describes directional information flow, not expression levels',
                'distractors': [
                    'Post-translational variation — different organisms degrade the protein at different rates through the ubiquitin-proteasome pathway; this is still consistent with the central dogma because the sequence information flows normally',
                    'Epigenetic variation — one organism has methylated the protein-coding region itself, changing the nucleotide sequence at the phenotypic level without altering the underlying DNA; this is an exception to the central dogma',
                    'Translational variation — ribosomes in one organism read the same mRNA twice per transcript, doubling protein output; this violates the central dogma because the protein output exceeds what the mRNA should encode',
                ],
            },
            {
                'question': 'Gene expression is controlled by multiple regulatory elements. Which of the following is NOT a mechanism of transcriptional regulation mentioned in Lecture 3?',
                'correct': 'Ribosomal decoding speed — how fast ribosomes read mRNA codons during translation',
                'distractors': [
                    'Enhancers — DNA sequences that increase transcription when bound by activator proteins',
                    'Transcription factors — proteins that bind DNA to activate or repress genes',
                    'Chromatin state — DNA accessibility controlled by histone modifications',
                ],
            },
            {
                'question': 'A human liver cell and a human neuron have the same DNA but produce very different proteins and perform very different functions. How is this possible?',
                'correct': 'Gene regulation determines which genes are expressed in each cell type — the same genome can produce hundreds of different cell types by turning different sets of genes ON and OFF',
                'distractors': [
                    'The two cells have different DNA sequences due to somatic mutations that accumulated during development',
                    'The two cells use different genetic codes — liver cells use a modified version of the DNA code compared to neurons',
                    'Only liver cells contain the full genome; neurons discard most of their DNA during maturation and retain only the genes they need',
                ],
            },
            {
                'question': 'The universality of DNA as the hereditary molecule across bacteria, archaea, and eukaryotes is explained by what evolutionary principle?',
                'correct': 'Common ancestry — all extant life descended from a single ancestral lineage that already used DNA, and this fundamental feature has been conserved across all descendants',
                'distractors': [
                    'Convergent molecular evolution — each domain independently arrived at DNA because it is the optimal hereditary molecule, without any shared ancestry',
                    'Horizontal gene transfer — DNA has been passed between unrelated domains so many times that all life now shares DNA despite having different origins',
                    'Environmental pressure — all cellular environments on Earth happen to favor DNA-based heredity, so all life independently evolved it',
                ],
            },
            {
                'question': 'The dolphin hindlimb example illustrates that phenotypic change during evolution can occur by:',
                'correct': 'Changes in gene REGULATION rather than gene deletion — dolphin genomes still contain the hindlimb developmental genes, but these genes are transcriptionally silenced during development, so the limbs do not form',
                'distractors': [
                    'Complete deletion of hindlimb genes from the dolphin genome',
                    'Replacement of dolphin DNA with fish DNA through horizontal gene transfer',
                    'Lamarckian loss — dolphin ancestors stopped using their hindlimbs, which caused the genes to disappear across generations',
                ],
            },
            {
                'question': 'L1 RECALL: How many chromosome pairs do humans have, and how many do most great apes have?',
                'correct': 'Humans have 23 pairs; great apes have 24. The difference is because human chromosome 2 is a fusion of two ancestral ape chromosomes',
                'distractors': [
                    'Humans have 24 pairs; great apes have 23 (the reverse)',
                    'Both humans and great apes have 23 pairs — no difference',
                    'Humans have 46 pairs; great apes have 48 pairs',
                ],
            },
            {
                'question': 'L5 SYNTHESIS: What molecular evidence specifically supports the claim that human chromosome 2 arose from a fusion of two ancestral ape chromosomes?',
                'correct': 'Human chromosome 2 contains two centromeres (one vestigial) and internal telomeric DNA sequences — signatures of a head-to-head fusion of two ancestral chromosomes',
                'distractors': [
                    'Human chromosome 2 is twice as long as any ape chromosome',
                    'Human chromosome 2 lacks a centromere entirely because it was formed by a deletion',
                    'Human chromosome 2 contains only coding genes with no regulatory elements',
                ],
            },
        ],
        visual={
            'type': 'flow',
            'description': 'Genotype to phenotype pipeline',
            'regions': [
                {'label': 'DNA', 'color': '#4ea8de', 'items': ['Sequence of nucleotides']},
                {'label': 'mRNA', 'color': '#7de2d1', 'items': ['Transcription', 'Splicing']},
                {'label': 'Protein', 'color': '#ffc857', 'items': ['Translation', 'Folding']},
                {'label': 'Phenotype', 'color': '#ff6b6b', 'items': ['Structure + function']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Genes code, regulation decides.',
            'trap': 'Having a gene does NOT mean the trait is expressed. Regulation is just as important as sequence.',
        },
    diagram=hox_regulatory_network_diagram(),
    ))
    nodes.append(build_node(
        id='lec3-mutations',
        title='Mutations: Raw Material of Evolution',
        subtitle='Types, rates, and effects (Lec 3 slides 10-17)',
        color='red', row=3,
        heading='Lecture 3 — Mutations',
        sections=[
            {'label': 'CORE CONCEPT', 'body': 'Mutations are the ultimate source of new genetic variation. Humans (and Neanderthals) have 23 chromosome pairs; other great apes have 24 — reflecting the #2 fusion. Most mutations are NEUTRAL or SLIGHTLY DELETERIOUS; strongly beneficial mutations are rare. Mutation rate examples: yeast ~3×10⁻⁸ per site; Arabidopsis ~7×10⁻⁹ per site per generation.'},
            {'label': 'SOMATIC vs GERMLINE', 'body': 'SOMATIC mutations occur in body cells and die with the individual — they are not inherited. GERMLINE mutations occur in cells that give rise to gametes and CAN be passed to offspring — they are the raw material of evolution.'},
            {'label': 'POINT MUTATION EXAMPLES', 'body': 'Albinism (FGFR3 mutations); thumb polydactyly (LMBR1 C→T substitution); Hutchinson-Gilford progeria syndrome (mutation in the Lamin A gene, causing premature aging).'},
            {'label': 'KEY TERMS', 'body': 'Point mutation, silent/missense/nonsense substitution, frameshift (insertion/deletion), germline vs somatic.'},
        ] + slides_to_sections(d, (10, 17)),
        examples=[
            'Point mutations: substitution (silent / missense / nonsense), insertion, deletion.',
            'Yeast mutation rate: ~3 × 10⁻⁸ per site per generation.',
            'Arabidopsis thaliana mutation rate: ~7 × 10⁻⁹ per site per generation.',
            'Human germ-line mutation rate: ~70 new mutations per generation (of ~3 billion bp).',
            'Albinism caused by FGFR3 mutations; polydactyly by LMBR1 C→T substitution; Hutchinson-Gilford progeria by Lamin A mutation.',
            'Mutations in multicellular organisms: only germline mutations are heritable; somatic mutations affect only the individual.',
        ],
        warnings=[
            'WATCH OUT: Most mutations are NEUTRAL or slightly deleterious. Beneficial mutations are rare.',
            'WATCH OUT: Mutation rate is NOT determined by need — mutation is a STOCHASTIC process that happens independently of whether the organism would benefit from the change.',
        ],
        mnemonic='MRS-BE = Mutations are Random, Stochastic, Beneficial-rarely, Essential.',
        flashcard={
            'front': 'Compare the evolutionary consequences of somatic versus germline mutations.',
            'back': 'SOMATIC mutations occur in non-reproductive cells (skin, liver, etc.). They affect only the individual and die with that individual — they cannot be inherited, so they do not contribute to population-level evolution. GERMLINE mutations occur in cells that give rise to gametes (eggs and sperm). These can be passed to offspring and become the raw material of evolution. Cancer is typically caused by accumulated somatic mutations; evolution is driven by germline mutations.',
        },
        quiz=[
            {
                'question': 'A woman develops a BRCA1 mutation in breast tissue during adulthood. This mutation is:',
                'correct': 'Somatic — it will not be inherited by her children',
                'distractors': [
                    'Germline — her children will inherit it with 50% probability',
                    'Both somatic and germline — all cell mutations are heritable',
                    'Not a true mutation because it occurred after birth',
                ],
            },
            {
                'question': 'The human germline mutation rate is approximately 70 new mutations per generation across ~3 billion base pairs. What is the evolutionary significance of this number?',
                'correct': 'It means each new human carries about 70 novel variants not present in either parent — providing a constant, low-level input of new alleles into the population that are the ultimate source of genetic variation for selection and drift to act on',
                'distractors': [
                    '70 mutations per generation is dangerously high — it means natural populations should accumulate mutational load faster than selection can remove it, eventually driving populations extinct through mutational meltdown',
                    '70 mutations per generation proves that Arabidopsis thaliana (with ~7 × 10⁻⁹ per site) evolves faster than humans, because 70 out of 3 billion is a lower per-site rate than Arabidopsis',
                    '70 mutations per generation means that after just 10 generations, a lineage will have accumulated 700 mutations — enough to make the descendants a different species from the founders by Hardy-Weinberg standards',
                ],
            },
            {
                'question': 'A point mutation in exon 5 of a gene changes codon GAA (Glu) to GAG (still Glu). This mutation is described as "silent." What is the most important caveat about assuming it has NO fitness effect?',
                'correct': 'Silent mutations can affect mRNA secondary structure, splicing enhancers, or codon usage bias (some codons are translated faster), potentially altering protein production rate or folding — a truly zero-effect assumption requires experimental testing',
                'distractors': [
                    'Silent mutations always have exactly zero fitness effect by definition — that is what "silent" means; any fitness effect would re-classify the mutation as a missense or regulatory variant',
                    'The caveat is that codon GAG is found only in introns in most species, so this mutation likely falls in a non-coding region and cannot be considered silent because exon/intron boundaries vary',
                    'Silent mutations can become non-silent if the amino acid they encode is later changed by a second mutation — the fitness effect is latent and only appears in double-mutant backgrounds',
                ],
            },
            {
                'question': 'Arabidopsis thaliana has a mutation rate of ~7 × 10⁻⁹ per site per generation. If a population of Arabidopsis contains 1,000 plants and each plant has 120,000,000 base pairs in its genome, approximately how many new mutations does the entire population experience each generation?',
                'correct': 'About 840 new mutations per generation (7 × 10⁻⁹ × 1.2 × 10⁸ bp ≈ 0.84 mutations/individual × 1,000 plants), providing the continuous raw material for evolution even in this small population',
                'distractors': [
                    'About 7,000 mutations per generation — one must multiply the mutation rate directly by population size alone, without accounting for genome size, to get the population-level mutation supply',
                    'Zero new mutations per generation — the mutation rate of 7 × 10⁻⁹ is so close to zero that in populations smaller than 10,000 individuals, no new mutations are expected in any given generation',
                    'About 120,000 new mutations per generation — the mutation rate applies to each individual gene rather than each base pair, and with ~120 million genes in the genome the total is very large',
                ],
            },
            {
                'question': 'Which statement about the RANDOMNESS of mutations is CORRECT?',
                'correct': 'Mutations occur randomly with respect to need — a population under antibiotic pressure does NOT mutate preferentially in genes that would confer resistance; resistance mutations occur at the same rate in stressed and unstressed populations, and selection simply favors the pre-existing variants',
                'distractors': [
                    'Mutations occur in response to environmental need — when a population experiences a new selective pressure, the mutation rate increases specifically at genes relevant to that pressure',
                    'Mutations are never truly random — each mutation occurs where the cell "knows" it would be most beneficial, which is why populations can adapt quickly',
                    'Mutations occur at the same rate at all sites equally — all base pairs have identical probabilities of mutation regardless of their chromosomal position or sequence context',
                ],
            },
            {
                'question': 'A frameshift mutation is caused by:',
                'correct': 'An insertion or deletion of a number of nucleotides that is not a multiple of 3, shifting the reading frame and typically producing a completely altered (and usually truncated) protein downstream',
                'distractors': [
                    'A single nucleotide substitution that changes one amino acid to another',
                    'A reversal of the DNA helix orientation that inverts the reading direction',
                    'A chromosomal translocation that moves a gene to a new chromosome',
                ],
            },
            {
                'question': 'A nonsense mutation creates:',
                'correct': 'A premature stop codon — causing protein translation to terminate early and producing a truncated (and usually non-functional) protein',
                'distractors': [
                    'An amino acid that has no biological meaning, which is why the mutation is called "nonsense"',
                    'A silent mutation with no protein-level effect',
                    'A codon that codes for an amino acid not present in any other protein in the organism',
                ],
            },
            {
                'question': 'Among mutation types, which generally has the LEAST protein-level effect?',
                'correct': 'Silent mutations — DNA changes that produce the same amino acid due to the redundancy of the genetic code (though some silent mutations can still affect mRNA stability, splicing, or codon usage)',
                'distractors': [
                    'Nonsense mutations — they create premature stop codons and have minimal effect because the remaining protein still folds correctly',
                    'Frameshift mutations — they shift only a few positions and rarely affect protein function',
                    'Missense mutations — they always produce a functional protein with just a different amino acid',
                ],
            },
            {
                'question': 'Most new mutations in a population are:',
                'correct': 'Neutral or slightly deleterious — strongly beneficial mutations are rare, which is why adaptive evolution is generally slow and depends on accumulating the rare beneficial variants over many generations',
                'distractors': [
                    'Strongly beneficial — which is why populations adapt quickly to changing environments',
                    'Lethal — which is why mutation rates are kept low to prevent population collapse',
                    'Reversible — meaning that any bad mutation can easily be undone by a second mutation at the same site',
                ],
            },
            {
                'question': 'L1 RECALL: Which gene was identified as the site of a C→T point mutation causing thumb polydactyly (extra digits) in humans?',
                'correct': 'LMBR1',
                'distractors': ['FGFR3', 'Lamin A', 'BRCA1'],
            },
            {
                'question': 'L3 COMPARISON: A single point mutation in the Lamin A gene causes Hutchinson-Gilford progeria. What does this syndrome illustrate about point mutations?',
                'correct': 'A single nucleotide change in one gene can produce a dramatic whole-body phenotype — in this case, premature aging — showing that mutations with large phenotypic effects are possible (though rare)',
                'distractors': [
                    'Point mutations are always silent and never produce measurable phenotypes',
                    'Lamin A mutations are Lamarckian and only affect individuals who experience aging stress',
                    'Progeria proves that mutations accumulate linearly across cell divisions regardless of DNA sequence context',
                ],
            },
        ],
        visual={
            'type': 'classification',
            'description': 'Mutation types and consequences',
            'regions': [
                {'label': 'Silent', 'color': '#7de2d1', 'items': ['Same amino acid', 'No protein change']},
                {'label': 'Missense', 'color': '#ffc857', 'items': ['Different amino acid', 'May alter protein function']},
                {'label': 'Nonsense', 'color': '#ff6b6b', 'items': ['Premature stop codon', 'Truncated protein']},
                {'label': 'Frameshift', 'color': '#8a5cf6', 'items': ['Insertion/deletion', 'Usually severe']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'SMNF: Silent, Missense, Nonsense, Frameshift — ordered by typical severity.',
            'trap': 'A "silent" mutation is not always silent — some affect mRNA stability, splicing, or codon usage and can have phenotypic effects.',
        },
    ))
    nodes.append(build_node(
        id='lec3-sex-meiosis',
        title='Sex Cells & Meiotic Variation',
        subtitle='How meiosis generates diversity (Lec 3 slides 18-19)',
        color='pink', row=3,
        heading='Lecture 3 — Meiotic Sources of Variation',
        sections=[
            {'label': 'CORE CONCEPT', 'body': 'Meiosis generates genetic variation through three mechanisms: (1) CROSSING OVER between homologous chromosomes during PROPHASE I (synaptic exchange at chiasmata); (2) INDEPENDENT ASSORTMENT of homologs during METAPHASE I — 2^n combinations for n chromosome pairs, which is 2^23 ≈ 8 million different gamete types in humans; (3) RANDOM FERTILIZATION, where any sperm can fuse with any egg, multiplying variation combinatorially.'},
            {'label': 'KEY TERMS', 'body': 'Meiosis I, prophase I, metaphase I, chiasmata, crossing over, recombination, independent assortment, random fertilization.'},
        ] + slides_to_sections(d, (18, 19)),
        examples=[
            'Meiotic crossing over (recombination) during prophase I — shuffles alleles between homologs.',
            'Independent assortment of homologs during metaphase I — 2^n possible combinations for n chromosome pairs (2^23 ≈ 8 million in humans).',
            'Random fertilization: any sperm can meet any egg, multiplying variation further.',
        ],
        warnings=[
            'WATCH OUT: Crossing over occurs during PROPHASE I (when homologs are synapsed), NOT during anaphase. Independent assortment is the METAPHASE I process.',
            'WATCH OUT: Meiosis generates variation; mitosis does NOT — mitosis produces genetically identical daughter cells.',
        ],
        mnemonic='CIR = Crossing over + Independent assortment + Random fertilization.',
        flashcard={
            'front': 'How many genetically distinct gametes can a single human potentially produce, ignoring new mutations?',
            'back': 'Humans have 23 pairs of chromosomes. Through independent assortment alone, 2²³ ≈ 8.4 million different combinations of homologs are possible. Adding crossing over (recombination) between homologs dramatically increases this number to effectively infinite (~10^1000+ depending on crossover positions). Random fertilization then multiplies this by the same factor in the partner — so each human offspring is effectively genetically unique (identical twins excepted).',
        },
        quiz=[
            {
                'question': 'Which meiotic process contributes to genetic variation by shuffling alleles between homologous chromosomes?',
                'correct': 'Crossing over (recombination) during prophase I',
                'distractors': [
                    'Independent assortment during metaphase I',
                    'Mitotic division of germ cells',
                    'Sister chromatid separation during anaphase II',
                ],
            },
            {
                'question': 'A plant reproduces ONLY by clonal vegetative propagation (no sex, no meiosis). Compared to a sexually reproducing relative, which statement about genetic variation in the clonal plant\'s population is MOST accurate?',
                'correct': 'New variation in the clonal lineage accumulates ONLY through new mutations — it cannot recombine existing alleles; the population will be far more genetically uniform and will track environmental change more slowly than the sexual relative',
                'distractors': [
                    'Clonal plants have MORE variation than sexual plants because every mutation is automatically passed to all offspring without being diluted by recombination with a second parent\'s genome',
                    'Clonal and sexual plants have equal genetic variation over evolutionary time because mutation rates are the same in both, and recombination only shuffles existing variation rather than creating new alleles',
                    'Clonal plants have zero genetic variation because without meiosis, no new chromosomal combinations can arise; all individuals in a clonal population are genetically identical regardless of mutation',
                ],
            },
            {
                'question': 'Independent assortment of chromosomes during meiosis can produce 2^23 ≈ 8.4 million different gamete combinations in humans. If a human couple each produces gametes via independent assortment alone (no crossing over), how many genetically distinct offspring are THEORETICALLY possible?',
                'correct': 'About 70 trillion (8.4 million × 8.4 million) — because each parent independently produces any of ~8.4 million gamete types, and fertilization combines one from each parent',
                'distractors': [
                    'About 8.4 million — because independent assortment applies only to the egg, while the sperm\'s chromosomes are fixed in sequence once spermatogenesis begins',
                    'About 46 — because humans have 46 chromosomes and independent assortment produces one unique combination per chromosome pair, summing to 46 possible outcomes',
                    'Infinite — because crossing over and mutation add unlimited combinations on top of independent assortment, making the 2^23 calculation meaningless as a practical limit',
                ],
            },
            {
                'question': 'Two genes on the SAME chromosome (linked genes) do NOT assort completely independently. However, crossing over can still produce recombinant gametes carrying new allele combinations. How does recombination frequency between two linked genes reflect their physical distance apart?',
                'correct': 'Genes that are far apart on a chromosome cross over more often between them — recombination frequency increases with physical distance, up to a maximum of 50% (appearing to assort independently when genes are far apart on the same chromosome)',
                'distractors': [
                    'Genes close together recombine MORE often because the chromosome is more flexible near the centromere where nearby genes cluster during prophase I, increasing chiasmata frequency',
                    'Recombination frequency is unrelated to physical distance — crossing-over hotspots are randomly distributed and equally likely at any chromosomal position regardless of gene location',
                    'Two genes on the same chromosome NEVER produce recombinant gametes because crossing over only occurs between NON-homologous chromosomes during independent assortment at metaphase I',
                ],
            },
            {
                'question': 'Random fertilization is the THIRD component of meiotic variation. How does it multiply the diversity produced by independent assortment and crossing over?',
                'correct': 'Any sperm can meet any egg — pairing one unique gamete from each parent multiplies the gametic diversity combinatorially, so total offspring possibilities equal (gamete types from parent 1) × (gamete types from parent 2)',
                'distractors': [
                    'Random fertilization adds nothing to diversity — the egg specifically selects the sperm with the most compatible genes, limiting the possible combinations',
                    'Random fertilization creates new mutations — the union of sperm and egg DNA damages both genomes, producing novel alleles not present in either parent',
                    'Random fertilization only affects species with external fertilization — in internal fertilizers, the process is deterministic and cannot add variation',
                ],
            },
            {
                'question': 'Mitosis and meiosis differ in their contributions to genetic variation. Which statement is CORRECT?',
                'correct': 'Mitosis produces genetically IDENTICAL daughter cells (aside from rare mutations), while meiosis produces genetically DIVERSE gametes through crossing over and independent assortment',
                'distractors': [
                    'Both mitosis and meiosis generate variation through crossing over — meiosis does it once, mitosis does it every cell division',
                    'Mitosis generates MORE variation than meiosis because mitotic divisions are more frequent in an organism\'s lifetime',
                    'Meiosis produces identical daughter cells while mitosis produces diverse ones — this is why sexual reproduction creates clones',
                ],
            },
            {
                'question': 'An asexual lineage (e.g., bdelloid rotifers, some aphid clones) lacks the genetic reshuffling of meiosis. What is the predicted long-term consequence?',
                'correct': 'New beneficial mutations cannot be combined with each other — they must accumulate sequentially in the same lineage, and deleterious mutations cannot be purged via recombination (Muller\'s ratchet), generally limiting long-term adaptation capacity',
                'distractors': [
                    'Asexual lineages adapt FASTER than sexual ones because they do not waste time producing males and can pass on all beneficial mutations to all offspring',
                    'Asexual lineages have no mutations because meiosis is the source of all genetic variation',
                    'Asexual and sexual lineages have identical long-term evolution because mutation rates are the same in both',
                ],
            },
            {
                'question': 'During which phase of meiosis does crossing over occur, and why is this phase specifically important?',
                'correct': 'Prophase I — this is when homologous chromosomes synapse (pair up tightly) with their chromatids aligned, allowing physical exchange of DNA segments at chiasmata. Without this synapsis, no crossing over could occur',
                'distractors': [
                    'Anaphase I — when homologs separate, they exchange segments as they pull apart',
                    'Metaphase II — when sister chromatids align at the equator, they swap segments',
                    'Telophase I — during cytokinesis, DNA is exchanged between the two daughter cells',
                ],
            },
            {
                'question': 'L1 RECALL: How many different gamete combinations can a single human theoretically produce from independent assortment alone (ignoring crossing over)?',
                'correct': 'Approximately 2^23 ≈ 8 million (8.4 million) — one combination for each of the 23 chromosome pairs',
                'distractors': [
                    'Approximately 46 — one per chromosome',
                    'Approximately 2^46 — one per chromatid',
                    'Approximately 23 million — multiplying the pairs by independent assortment directly',
                ],
            },
            {
                'question': 'L5 SYNTHESIS: Which mnemonic captures the three meiotic mechanisms that generate variation?',
                'correct': 'CIR — Crossing over, Independent assortment, Random fertilization',
                'distractors': [
                    'CPI — Crossing over, Polyploidy, Inbreeding',
                    'VHD — Variation, Heritability, Differential reproduction',
                    'MGP — Mitosis, Gametogenesis, Polyploidy',
                ],
            },
        ],
        visual={
            'type': 'diagram',
            'description': 'Sources of meiotic variation',
            'regions': [
                {'label': 'Prophase I', 'color': '#4ea8de', 'items': ['Crossing over', 'Chiasmata form']},
                {'label': 'Metaphase I', 'color': '#7de2d1', 'items': ['Independent assortment of homologs', '2^n combinations']},
                {'label': 'Fertilization', 'color': '#ffc857', 'items': ['Random gamete fusion', 'Multiplies variation further']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Three levels of mixing in sex.',
            'trap': 'Mitosis does not generate variation — only meiosis + fertilization do. This is why asexual lineages accumulate mutations linearly while sexual lineages can recombine them.',
        },
    ))
    nodes.append(build_node(
        id='lec3-genotype-phenotype',
        title='Genotype-Phenotype Map: Polygenic Traits & Environment',
        subtitle='How genes + environment shape phenotypes (Lec 3 slides 20-29)',
        color='teal', row=3,
        heading='Lecture 3 — Linking Genotype and Phenotype',
        sections=[
            {'label': 'CORE CONCEPT', 'body': 'Genotype does not map 1:1 to phenotype. There are three distinct flavors of variation: (1) GENETIC POLYMORPHISM (discrete classes) — e.g., morning glory leaf shape, where T = lobed dominant and t = entire; (2) POLYGENIC TRAITS (continuous) — Edward East\'s 1916 tobacco corolla length: 2 loci → 5 classes; 6 loci → 13 classes; (3) PHENOTYPIC PLASTICITY — Ambystoma (salamander) cannibalistic morphs develop in response to environment.'},
            {'label': 'VARIANCE PARTITIONING', 'body': 'V_P = V_G + V_E. If V_G = 0, no evolution can occur (nothing to select on). If V_G > V_E, rapid change is possible.'},
            {'label': 'KEY FIGURES', 'body': 'Edward East (1916) — classic tobacco corolla experiments demonstrating polygenic inheritance.'},
        ] + slides_to_sections(d, (20, 29)),
        examples=[
            'Genetic polymorphism: morning glory leaf shape — T (lobed) dominant, t (entire) recessive. Discrete classes from one or few loci.',
            'Polygenic traits: Edward East 1916 tobacco corolla — 2 loci produces 5 phenotypic classes; 6 loci produces 13 classes.',
            'Phenotypic plasticity: Ambystoma cannibalistic morphs develop in response to environmental cues.',
            'V_P = V_G + V_E; if V_G = 0 → no evolution possible; if V_G > V_E → rapid change.',
        ],
        warnings=[
            'WATCH OUT: Continuous variation does NOT mean environmental. Human height is ~80% heritable but still continuous because many genes contribute (polygenic). Heritability and continuous-vs-discrete are independent dimensions.',
            'WATCH OUT: A "polymorphism" is a POPULATION-level phenomenon (two or more forms coexist). An individual has alleles or a genotype, not a polymorphism.',
        ],
        mnemonic='PPE = Polymorphism (discrete) vs Polygenic (continuous) vs Environmental (plasticity).',
        flashcard={
            'front': 'What is the difference between a genetic polymorphism and a polygenic trait? Give an example of each.',
            'back': 'A POLYMORPHISM is the presence of two or more DISCRETE phenotypic variants in a population maintained by genetic variation at one or a few loci — e.g., human ABO blood types (3 alleles → 4 phenotypes), Mendelian pea flower color. A POLYGENIC trait is continuous variation controlled by MANY genes each contributing a small amount, usually producing a bell-curve distribution — e.g., human height, skin color, IQ, disease risk (BMI, hypertension). Polygenic traits can also be influenced by environment, producing gene × environment effects.',
        },
        quiz=[
            {
                'question': 'Human height is considered a polygenic trait because:',
                'correct': 'It is influenced by many genes each contributing a small amount, producing continuous variation',
                'distractors': [
                    'It is controlled by a single dominant/recessive gene pair',
                    'It is determined entirely by environment and nutrition',
                    'It does not vary within populations',
                ],
            },
            {
                'question': 'A study reports that height heritability is ~80% in wealthy countries but lower in developing countries. How should this difference be interpreted?',
                'correct': 'Heritability is population- and environment-specific: when environmental variation (nutrition) is large and variable, V_E is high and h² = V_A/V_P decreases even if V_A is unchanged — it does not mean genes matter less in poorer countries',
                'distractors': [
                    'Lower heritability in developing countries means height genes are less functional under nutritional stress — malnutrition causes mutations that reduce additive genetic variance for height',
                    'Higher heritability in wealthy countries means wealthy populations have more height alleles due to positive selection for tall individuals during industrialization over the past 200 years',
                    'The difference proves that height is primarily environmental in developing countries and primarily genetic in wealthy countries — two different mechanisms are operating in different populations',
                ],
            },
            {
                'question': 'A genetic polymorphism for human ABO blood type has alleles I^A, I^B, and i at one locus. Three blood groups (A, B, AB, O) exist simultaneously. Which statement about this polymorphism and its fitness effects is MOST likely correct?',
                'correct': 'ABO blood type is probably maintained as a balanced polymorphism — possibly by pathogen-driven selection (different blood types confer different resistance profiles to different pathogens), though the exact mechanism is still debated',
                'distractors': [
                    'ABO blood type has zero fitness effect and persists only through mutation-selection balance — all three alleles are selectively neutral and drift freely in human populations',
                    'ABO blood type represents a transient polymorphism: I^A is selectively neutral, I^B is slightly deleterious, and i is favored; given enough time, all human populations will eventually fix the i allele',
                    'Because ABO blood type is codominant (no dominance effects), it cannot be maintained by natural selection — only additive traits respond to selection, so blood type variation is maintained entirely by random genetic drift',
                ],
            },
            {
                'question': 'A trait shows continuous variation in a population. A researcher measures heritability as h² = 0.0. Which explanation is CORRECT?',
                'correct': 'All phenotypic variation in the population is due to environmental differences — there is no additive genetic variance to respond to selection, so the trait cannot evolve even with strong selection differential S',
                'distractors': [
                    'A trait with h² = 0.0 has no genetic basis at all and is entirely plastic — individuals can change their phenotype at will in response to the environment without any genetic change',
                    'h² = 0.0 means the trait is not polygenic — it must be controlled by a single gene pair, which produces discrete categories rather than continuous variation, so the continuous distribution is a measurement error',
                    'h² = 0.0 is impossible for a continuous trait — if variation is measurable, some of it must be genetic; a measured value of 0.0 indicates the researcher made an error in the parent-offspring regression',
                ],
            },
            {
                'question': 'Which of the following is an example of a GENETIC POLYMORPHISM rather than a polygenic trait?',
                'correct': 'ABO blood type — discrete categories (A, B, AB, O) controlled by a small number of alleles at one locus',
                'distractors': [
                    'Human height — continuous variation determined by many genes',
                    'Human skin color — continuous variation with many contributing loci',
                    'Human IQ — continuous distribution shaped by both genes and environment',
                ],
            },
            {
                'question': 'Which of the following is an example of a POLYGENIC TRAIT rather than a discrete polymorphism?',
                'correct': 'Human body mass index (BMI) — continuous variation controlled by hundreds of loci, each contributing a small amount',
                'distractors': [
                    'Mendelian pea flower color (purple vs white)',
                    'Human ABO blood type',
                    'Presence or absence of a tail in certain mammals',
                ],
            },
            {
                'question': 'A trait shows a perfect bell-curve distribution in a population. What can you CONCLUDE from this alone?',
                'correct': 'Very little — a bell curve is consistent with many possible scenarios: a highly heritable polygenic trait, a purely environmental trait, or any mixture of the two. The shape alone does not reveal whether genes or environment dominate',
                'distractors': [
                    'The trait must be polygenic with high heritability — bell curves only arise from many additive genetic effects',
                    'The trait must be environmentally determined — bell curves arise only from normally-distributed environmental factors',
                    'The trait must be neutral — bell curves are characteristic of traits under no selective pressure',
                ],
            },
            {
                'question': 'An individual is described as having a "polymorphism." Why is this terminology INCORRECT?',
                'correct': 'Polymorphism is a POPULATION-level concept — it refers to the coexistence of two or more discrete variants in a population. An individual has ALLELES (or a GENOTYPE), not a polymorphism',
                'distractors': [
                    'The terminology is correct in all usages — individuals, populations, and species can all "have polymorphisms" interchangeably',
                    'Individuals cannot have any genetic variation — only populations have genetic differences, so the word "polymorphism" should never apply anywhere',
                    'Polymorphism only applies to molecular traits like protein electrophoresis bands, not to phenotypic traits',
                ],
            },
            {
                'question': 'L1 RECALL: In Edward East\'s 1916 tobacco corolla experiments, how many phenotypic classes were observed when TWO loci contributed to corolla length?',
                'correct': '5 classes (2 loci → 2n+1 = 5)',
                'distractors': [
                    '2 classes — one per locus',
                    '13 classes (the number seen for 6 loci)',
                    '10 classes — twice the number of loci squared',
                ],
            },
            {
                'question': 'L2 MECHANISM: If a population has V_P = 10, V_G = 0, and V_E = 10 for a quantitative trait, what happens if strong selection is applied?',
                'correct': 'No evolutionary response — with V_G = 0, there is no heritable component to select on, so the trait mean cannot change across generations regardless of selection strength',
                'distractors': [
                    'Rapid evolution because V_E is large and environmental effects are directly selected',
                    'Slow but steady evolution because selection operates on phenotypes regardless of heritability',
                    'Evolution in the opposite direction of selection, because V_E = V_P creates feedback reversing the response',
                ],
            },
        ],
        visual={
            'type': 'distribution',
            'description': 'Polymorphism vs polygenic distributions',
            'regions': [
                {'label': 'Polymorphism', 'color': '#ff6b6b', 'items': ['Discrete classes', 'Few alleles', 'e.g., blood type']},
                {'label': 'Polygenic', 'color': '#4ea8de', 'items': ['Continuous bell curve', 'Many loci', 'e.g., height']},
                {'label': 'Plastic', 'color': '#7de2d1', 'items': ['Same genotype, many phenotypes', 'Environment-dependent']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Discrete vs Continuous vs Plastic.',
            'trap': 'Continuous variation does NOT mean purely environmental — many continuous traits are highly heritable.',
        },
    diagram=reaction_norm_gxe_diagram(),
    ))
    return nodes


def lec4_nodes():
    d = load_lec('lec4')
    nodes = []
    nodes.append(build_node(
        id='lec4-sources-evolution',
        title='Sources of Evolutionary Change',
        subtitle='The 5 mechanisms that change allele frequencies (Lec 4 slides 1-3)',
        color='amber', row=4,
        heading='Lecture 4 — Sources of Evolutionary Change',
        sections=[
            {'label': 'CORE CONCEPT', 'body': 'A population is a group of interbreeding individuals sharing a common gene pool. From the population-genetics view, evolution = change in allele frequencies across generations. There are FIVE mechanisms that change allele frequencies: natural selection, genetic drift, mutation, gene flow (migration), and non-random mating. The absence of all five forces = Hardy-Weinberg equilibrium (HWE), which serves as the NULL HYPOTHESIS for detecting evolution.'},
            {'label': 'WHY IT MATTERS', 'body': 'These five mechanisms constitute the complete explanatory toolkit for all population-level genetic change. Any observed allele frequency change must be attributable to one or a combination of these forces.'},
        ] + slides_to_sections(d, (1, 3)),
        examples=[
            'Five evolutionary forces: mutation, genetic drift, gene flow, natural selection, non-random mating.',
            'In a Hardy-Weinberg "null" population, all five forces are absent and allele frequencies do not change.',
        ],
        warnings=[
            'WATCH OUT: Non-random mating (inbreeding, assortative) changes GENOTYPE frequencies, NOT allele frequencies directly.',
            'WATCH OUT: Only MUTATION creates NEW variation; the other four (selection, drift, gene flow, non-random mating) only redistribute existing variation.',
        ],
        mnemonic='MUD-GAS = Mutation, Unequal drift, Drift, Gene flow, Assortative mating, Selection.',
        flashcard={
            'front': 'Name the five evolutionary forces that can change allele frequencies in a population, and briefly describe each.',
            'back': '(1) MUTATION — new alleles appear via DNA replication errors. (2) GENETIC DRIFT — random sampling causes allele frequencies to fluctuate between generations (stronger in small populations). (3) GENE FLOW (migration) — alleles move between populations when individuals immigrate/emigrate. (4) NATURAL SELECTION — differential reproductive success based on heritable traits. (5) NON-RANDOM MATING (assortative or inbreeding) — affects genotype frequencies (but technically not allele frequencies). All five disrupt Hardy-Weinberg equilibrium.',
        },
        quiz=[
            {
                'question': 'A population that satisfies Hardy-Weinberg assumptions will:',
                'correct': 'Have allele frequencies that do not change from generation to generation',
                'distractors': [
                    'Evolve rapidly due to random mutation',
                    'Lose all genetic variation within a few generations',
                    'Exhibit directional natural selection',
                ],
            },
            {
                'question': 'A population shows genotype frequencies of AA = 0.49, Aa = 0.42, aa = 0.09. With allele frequencies p = 0.7, q = 0.3, expected HWE frequencies are p² = 0.49, 2pq = 0.42, q² = 0.09. The observed and expected frequencies match. What can be CORRECTLY concluded?',
                'correct': 'The locus is in Hardy-Weinberg equilibrium — we cannot conclude that NO evolutionary forces are acting on the population, only that NONE of the five HWE-violating forces are detectably affecting THIS LOCUS AT THIS MOMENT',
                'distractors': [
                    'The population is not evolving at all — HWE at one locus proves all five assumptions are satisfied across the entire genome',
                    'The population is evolving by genetic drift — HWE is only expected in very large populations, so matching HWE frequencies must indicate drift is actively maintaining the equilibrium',
                    'The population is under balancing selection — only frequency-dependent or heterozygote-advantage selection can produce the exact HWE frequencies at both allele frequencies simultaneously',
                ],
            },
            {
                'question': 'In a population, inbreeding (mating between relatives) increases the frequency of homozygotes. Which statement about inbreeding and Hardy-Weinberg equilibrium is CORRECT?',
                'correct': 'Inbreeding changes GENOTYPE frequencies (increases homozygotes, decreases heterozygotes) but does NOT change ALLELE frequencies — so inbreeding violates HWE assumptions but is not itself a force that drives allele frequency change',
                'distractors': [
                    'Inbreeding changes allele frequencies by increasing the probability that deleterious recessive alleles are exposed to selection, which causes natural selection to remove them more efficiently',
                    'Inbreeding both changes genotype frequencies AND allele frequencies, because homozygotes produce different gametes than heterozygotes — so inbreeding is fully equivalent to selection in its evolutionary effects',
                    'Inbreeding maintains Hardy-Weinberg equilibrium as long as it is consistent across generations, because the ratio of homozygotes to heterozygotes stabilizes at a new equilibrium value that still satisfies the HWE equation',
                ],
            },
            {
                'question': 'Among the five forces that can change allele frequencies, which one CREATES new alleles that did not previously exist in the population?',
                'correct': 'Mutation — all other forces (drift, gene flow, selection, non-random mating) only change the frequencies of alleles that are already present; mutation is the only source of truly novel genetic variation',
                'distractors': [
                    'Gene flow — migration introduces alleles from other populations that may never have existed locally before, creating new variation in the recipient population',
                    'Genetic drift — in small populations, drift can randomly create new allele combinations that function as novel variants by rearranging existing alleles into new haplotypes',
                    'Natural selection — positive selection for a heterozygous advantage can maintain two alleles that would otherwise disappear, effectively "creating" genetic diversity that would not persist without selection',
                ],
            },
            {
                'question': 'Gene flow (migration) is one of the five evolutionary forces. What is its direct effect on allele frequencies in the recipient population?',
                'correct': 'It moves alleles between populations — immigrants bring in alleles that may not be present locally, and emigrants remove alleles from the source; over time gene flow tends to HOMOGENIZE allele frequencies between connected populations',
                'distractors': [
                    'Gene flow only adds new mutations — it has no effect on existing allele frequencies unless the migrants carry a novel mutation',
                    'Gene flow increases genetic drift because more individuals means more random sampling error',
                    'Gene flow reduces allele frequencies uniformly — every migration event reduces all allele frequencies by equal amounts',
                ],
            },
            {
                'question': 'Why is non-random mating listed as a force that disrupts Hardy-Weinberg equilibrium even though it does NOT directly change allele frequencies?',
                'correct': 'It changes GENOTYPE frequencies (e.g., increases homozygotes under inbreeding) without changing allele frequencies — but this still represents a deviation from HWE predictions and can indirectly set the stage for selection to act differently on the redistributed genotypes',
                'distractors': [
                    'Non-random mating always changes allele frequencies directly by reducing heterozygote fertility',
                    'Non-random mating is not actually one of the five forces — it was added by mistake to modern textbooks',
                    'Non-random mating only disrupts HWE when combined with mutation — by itself it has no effect on the equation',
                ],
            },
            {
                'question': 'A Hardy-Weinberg null population has allele frequencies that do not change across generations. Which of the following must be true of such a population?',
                'correct': 'No mutation, no selection, no migration, random mating, AND infinite population size — all five assumptions must hold simultaneously for HWE to be maintained',
                'distractors': [
                    'Only natural selection and mutation must be absent — drift, gene flow, and mating patterns do not affect HWE',
                    'Only population size must be sufficiently large; the other four assumptions are irrelevant to HWE',
                    'At least three of the five assumptions must hold, but any two can be violated without disrupting the equilibrium',
                ],
            },
            {
                'question': 'Genetic drift is most appropriately described as:',
                'correct': 'Random sampling error that causes allele frequencies to fluctuate between generations, with effects inversely proportional to population size — strongest in small populations',
                'distractors': [
                    'Directional change in allele frequencies caused by environmental pressure',
                    'The rate at which new mutations appear in a population',
                    'The movement of alleles between isolated populations via migration',
                ],
            },
            {
                'question': 'L1 RECALL: What is the name of the theoretical state in which all five evolutionary forces are absent, producing unchanging allele frequencies across generations?',
                'correct': 'Hardy-Weinberg equilibrium (HWE)',
                'distractors': [
                    'Fisher equilibrium',
                    'Neutral drift equilibrium',
                    'Mutation-selection balance',
                ],
            },
            {
                'question': 'L5 SYNTHESIS: Which of the five evolutionary forces is the ONLY source of truly NEW genetic variation in a population?',
                'correct': 'Mutation — the other four (natural selection, genetic drift, gene flow, non-random mating) only redistribute or filter existing variation, while mutation introduces novel alleles',
                'distractors': [
                    'Gene flow — because migrants can bring alleles never before seen in the recipient population',
                    'Genetic drift — because random sampling can create new allele combinations',
                    'Natural selection — because strong selection can induce beneficial mutations by pressure',
                ],
            },
        ],
        visual={
            'type': 'summary',
            'description': 'The five forces of evolution',
            'regions': [
                {'label': 'Forces', 'color': '#ffc857', 'items': ['Mutation', 'Drift', 'Gene flow', 'Selection', 'Non-random mating']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Five forces disrupt H-W equilibrium.',
            'trap': 'Only mutation creates NEW variation. The others sort and redistribute existing variation.',
        },
    diagram=hardy_weinberg_assumptions_diagram(),
    ))
    nodes.append(build_node(
        id='lec4-hardy-weinberg',
        title='Hardy-Weinberg Theorem',
        subtitle='The null model of population genetics (Lec 4 slides 4-12)',
        color='blue', row=4,
        heading='Lecture 4 — Hardy-Weinberg Principle',
        sections=[
            {'label': 'CORE CONCEPT', 'body': 'The Hardy-Weinberg Equilibrium (HWE) is the NULL HYPOTHESIS of population genetics. Its five assumptions are: infinite population, no selection, no migration (gene flow), no mutation, and random mating. The equations are p + q = 1 (allele frequencies) and p² + 2pq + q² = 1 (genotype frequencies: AA, Aa, aa).'},
            {'label': 'WORKED EXAMPLE', 'body': 'Drosophila ADH locus, 500 flies, p=0.7, q=0.3. EXPECTED frequencies: AA = 245 (p² × 500), Aa = 210 (2pq × 500), aa = 45 (q² × 500). OBSERVED: AA = 287, Aa = 126, aa = 87. Chi-square P = 0.02 → excess of homozygotes → population is NOT in HWE → some force (e.g., inbreeding, selection) is acting on this locus.'},
            {'label': 'WHY IT MATTERS', 'body': 'HWE gives us a mathematical standard against which to detect evolution. Any deviation from HWE expectations indicates one or more of the five evolutionary forces is operating on the tested locus.'},
        ] + slides_to_sections(d, (4, 12)),
        examples=[
            'Hardy-Weinberg equations: p + q = 1, p² + 2pq + q² = 1.',
            'Five assumptions: (1) no mutation, (2) no selection, (3) no migration, (4) random mating, (5) infinite population (no drift).',
            'Drosophila ADH example: 500 flies, p=0.7, q=0.3. Expected AA=245, Aa=210, aa=45. Observed AA=287, Aa=126, aa=87. Chi-square P=0.02 → NOT in HWE, excess homozygotes.',
        ],
        warnings=[
            'WATCH OUT: HWE is a NULL hypothesis — we test whether a population is in equilibrium to DETECT evolution.',
            'WATCH OUT: A population can be in HWE for one locus and not others — each locus must be tested independently.',
        ],
        mnemonic='p² + 2pq + q² = 1. If observed ≠ expected → evolution is happening.',
        flashcard={
            'front': 'State the five assumptions of the Hardy-Weinberg principle and explain what happens if each one is violated.',
            'back': '(1) NO MUTATION — if violated, new alleles enter the population and allele frequencies drift. (2) NO NATURAL SELECTION — if violated, fitness differences skew genotype frequencies. (3) NO MIGRATION (GENE FLOW) — if violated, alleles move in/out and frequencies change. (4) RANDOM MATING — if violated (e.g., assortative mating or inbreeding), genotype frequencies deviate from p² + 2pq + q² even without allele frequency change. (5) INFINITE POPULATION SIZE — if violated, genetic drift randomly changes allele frequencies (stronger in smaller populations). HWE gives us a NULL model: if observed genotype frequencies deviate from the predictions, one of these five assumptions is being violated.',
        },
        quiz=[
            {
                'question': 'In a population with alleles A and a at frequencies p = 0.6 and q = 0.4, what is the expected frequency of heterozygotes under Hardy-Weinberg equilibrium?',
                'correct': '0.48 (2pq = 2 × 0.6 × 0.4)',
                'distractors': [
                    '0.36 (p²)',
                    '0.16 (q²)',
                    '0.50 (always one-half)',
                ],
            },
            {
                'question': 'A recessive autosomal disorder occurs at a frequency of 1 in 10,000 in a large randomly mating population. What is the CARRIER (heterozygote) frequency?',
                'correct': 'q² = 0.0001, so q = 0.01 and p ≈ 0.99; carrier frequency = 2pq ≈ 2 × 0.99 × 0.01 ≈ 0.0198 (about 1 in 50) — far more common than affected individuals, which is why recessive diseases persist',
                'distractors': [
                    '1 in 10,000 — the carrier frequency equals the disease frequency because heterozygotes pass one copy of the allele just as affected homozygotes do, so both are equally common',
                    '1 in 5,000 — exactly twice the disease frequency, because for every one affected individual there must be two carriers who contributed the two q alleles observed in the affected person',
                    '1 in 100,000,000 — because carriers must carry BOTH a dominant and a recessive allele, and the probability of inheriting both is q × p, which is much smaller than q² for rare alleles',
                ],
            },
            {
                'question': 'A population geneticist observes that at a particular locus, the observed frequency of heterozygotes is LOWER than expected under HWE. Which of the following is the MOST likely explanation?',
                'correct': 'Inbreeding or assortative mating — both cause individuals to mate with genetically similar partners, increasing homozygosity and reducing heterozygote frequency relative to HWE predictions',
                'distractors': [
                    'Directional selection favoring the dominant allele — selection increases p and decreases q, but at any given p and q the HWE prediction is still 2pq; selection on a dominant allele would not specifically reduce heterozygote frequency below 2pq',
                    'Genetic drift in a large population — drift decreases allele frequencies uniformly across all genotype classes, so it reduces both homozygote and heterozygote frequencies proportionally and cannot produce a heterozygote deficit specifically',
                    'Mutation pressure creating new alleles — new mutations increase allelic diversity, which tends to increase the frequency of heterozygotes above the HWE prediction, not below it',
                ],
            },
            {
                'question': 'The Hardy-Weinberg principle is called a "null model" for population genetics. What does this mean in practice when a researcher detects a deviation from HWE at a locus?',
                'correct': 'A deviation from HWE is a SIGNAL that one or more evolutionary forces (selection, drift, mutation, gene flow, non-random mating) are affecting that locus — it does not identify WHICH force, only that something is operating',
                'distractors': [
                    'A deviation from HWE proves that natural selection is acting on that specific locus — it is the most sensitive test for selection available and rules out all other evolutionary forces when positive',
                    'A deviation from HWE means the Hardy-Weinberg equation was applied incorrectly — the null model is mathematically exact, so any apparent deviation must reflect a calculation or sampling error',
                    'A deviation from HWE is expected in all real populations because no population truly has infinite size and zero mutation — HWE deviations are universal and provide no information about specific evolutionary mechanisms',
                ],
            },
            {
                'question': 'In the Hardy-Weinberg equations, what does "p + q = 1" represent, and what does "p² + 2pq + q² = 1" represent?',
                'correct': 'The first equation describes ALLELE frequencies (p = frequency of A, q = frequency of a); the second describes GENOTYPE frequencies (p² = AA, 2pq = Aa, q² = aa) expected at equilibrium',
                'distractors': [
                    'The first describes genotype frequencies and the second describes allele frequencies — the two equations are interchangeable',
                    'Both equations describe allele frequencies; the second is just a more detailed version of the first',
                    'Both equations describe genotype frequencies; p + q refers to homozygous genotypes only',
                ],
            },
            {
                'question': 'A researcher using Hardy-Weinberg to estimate the frequency of a recessive allele in a population should calculate q from:',
                'correct': 'q² — the frequency of homozygous recessive individuals — because dominant alleles mask recessive ones in heterozygotes, so you cannot calculate q directly from the frequency of dominant phenotypes',
                'distractors': [
                    'p² — because the frequency of dominant homozygotes is always equal to the square of q',
                    '2pq — the heterozygote frequency, which directly gives q without needing a square root',
                    'The frequency of dominant phenotypes — which is always equal to 1-q by definition',
                ],
            },
            {
                'question': 'The ADH locus in fruit flies is often cited as an HWE-tractable example because:',
                'correct': 'Allele frequencies can be estimated from electrophoresis phenotypes — different ADH alleles produce differently migrating protein bands, and the observed phenotype frequencies can be directly compared against HWE predictions',
                'distractors': [
                    'Fruit flies are the only organism in which Hardy-Weinberg applies — the equation fails in other species due to different inheritance patterns',
                    'ADH is a single-allele locus with no variation, which makes it a perfect null for HWE tests',
                    'ADH is a lethal gene that kills carriers, which is why HWE predictions are easy to verify',
                ],
            },
            {
                'question': 'If a population is in HWE at ONE locus, can you conclude the population is in HWE at ALL loci?',
                'correct': 'No — a population can be in HWE at one locus and not others. Each locus must be tested independently, because selection, drift, or other forces may affect some loci more strongly than others',
                'distractors': [
                    'Yes — HWE is a whole-population property; if one locus satisfies it, all loci must',
                    'Yes — because HWE requires random mating across the whole population, any HWE-consistent locus implies random mating for all loci',
                    'No — but only if you can demonstrate explicit selection on other loci; without that evidence, HWE at one locus does imply HWE at all',
                ],
            },
            {
                'question': 'L4 APPLICATION: At the Drosophila ADH locus, 500 flies were sampled with p=0.7 and q=0.3. Under HWE, how many AA homozygotes would be EXPECTED?',
                'correct': '245 (p² × 500 = 0.49 × 500)',
                'distractors': [
                    '287 (the observed count)',
                    '210 (which is 2pq × 500, the heterozygote count)',
                    '350 (which is 0.7 × 500, the allele count)',
                ],
            },
            {
                'question': 'L5 SYNTHESIS: In a Drosophila ADH study, observed genotypes were AA=287, Aa=126, aa=87 when HWE predicted AA=245, Aa=210, aa=45. A chi-square test gave P=0.02. What does this pattern (excess homozygotes) most likely indicate?',
                'correct': 'Inbreeding or positive assortative mating — both increase homozygote frequency relative to HWE expectation without necessarily changing allele frequencies',
                'distractors': [
                    'Heterozygote advantage — which would increase the number of heterozygotes, not decrease them',
                    'Random mutation at the ADH locus — which would not specifically produce a homozygote excess',
                    'Random genetic drift — which affects allele frequencies but does not specifically produce excess homozygotes',
                ],
            },
        ],
        visual={
            'type': 'equation',
            'description': 'The Hardy-Weinberg equations',
            'regions': [
                {'label': 'Allele', 'color': '#4ea8de', 'items': ['p + q = 1']},
                {'label': 'Genotype', 'color': '#7de2d1', 'items': ['p² + 2pq + q² = 1']},
                {'label': 'Homozygous dom', 'color': '#ffc857', 'items': ['p² (AA)']},
                {'label': 'Heterozygous', 'color': '#ff6b6b', 'items': ['2pq (Aa)']},
                {'label': 'Homozygous rec', 'color': '#8a5cf6', 'items': ['q² (aa)']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'p² + 2pq + q² = 1 always works when population is at equilibrium.',
            'trap': 'Rare dominant alleles hide rarer recessive alleles. Always calculate q from q² (homozygous recessives), not from a count of dominant phenotypes.',
        },
        diagram=hwe_punnett_diagram(),
    ))
    nodes.append(build_node(
        id='lec4-genetic-drift',
        title='Genetic Drift, Bottlenecks & Founder Effects',
        subtitle='Random allele frequency change in finite populations (Lec 4 slides 13-22)',
        color='gray', row=4,
        heading='Lecture 4 — Genetic Drift',
        sections=[
            {'label': 'CORE CONCEPT', 'body': 'Genetic drift = RANDOM change in allele frequencies due to finite sampling. Drift is NOT directional and is STRONGEST in SMALL populations. It can fix or lose alleles regardless of fitness.'},
            {'label': 'KEY EXPERIMENT: BURI 1956', 'body': 'Peter Buri established 107 Drosophila populations, each starting with bw/bw75 heterozygotes (8 males and 8 females per population per generation). By generation 19, the bw75 allele had either gone to fixation or been lost at random in each line — dramatically illustrating drift in small populations.'},
            {'label': 'BOTTLENECK vs FOUNDER EFFECT', 'body': 'BOTTLENECK: a pre-existing population crashes to very small size. Northern elephant seals were hunted to only 10-20 individuals; they have recovered to over 100,000 but show very low diversity. FOUNDER EFFECT: a few individuals colonize a new area. Examples: Amish populations (elevated Ellis-van Creveld syndrome); Pingelap islanders (colorblindness); Galápagos colonization.'},
        ] + slides_to_sections(d, (13, 22)),
        examples=[
            'Drift in Drosophila (Buri 1956): 107 populations, 8M + 8F per generation; by generation 19, bw75 allele randomly fixed or lost.',
            'Genetic bottleneck: Northern elephant seals hunted to 10-20 individuals, now >100,000 but very low diversity.',
            'Founder effect: Amish (Ellis-van Creveld syndrome), Pingelap (colorblindness), Galápagos colonization events.',
        ],
        warnings=[
            'WATCH OUT: Drift is NOT directional — it is random. Its effects are strongest in SMALL populations.',
            'WATCH OUT: Bottleneck effects persist for many generations even after the population recovers, because LOST alleles are gone permanently.',
        ],
        mnemonic='BFS = Bottleneck, Founder effect, Small population = strong drift.',
        flashcard={
            'front': 'Explain how the founder effect differs from a genetic bottleneck, and give an example of each.',
            'back': 'A GENETIC BOTTLENECK occurs when an existing population is dramatically reduced in size (disease, disaster, overhunting), eliminating many alleles by chance. The survivors rebuild the population from a non-representative sample — example: cheetahs (~10,000 years ago bottleneck reduced genetic diversity to near-clonal levels; northern elephant seals reduced to ~20 individuals in the 1890s). A FOUNDER EFFECT occurs when a small number of individuals colonize a new habitat, bringing only a subset of the source population\'s alleles. The new population is genetically distinct from the source not by selection but by sampling chance — example: Amish populations in Pennsylvania show elevated frequencies of recessive disorders (e.g., polydactyly) because founders happened to carry those alleles. Both reduce genetic diversity through drift.',
        },
        quiz=[
            {
                'question': 'Genetic drift has the strongest effect on allele frequency change in which type of population?',
                'correct': 'Small populations',
                'distractors': [
                    'Large populations with equal sex ratios',
                    'Populations at Hardy-Weinberg equilibrium',
                    'Populations with high gene flow',
                ],
            },
            {
                'question': 'Northern elephant seals were hunted to ~20 individuals in the 1890s. Today the population has recovered to ~100,000. Despite this recovery, the population shows almost no genetic variation. What best explains this?',
                'correct': 'A severe bottleneck eliminates alleles by chance regardless of their fitness — the surviving 20 individuals carried only a small, non-representative sample of the original allelic diversity, and no amount of subsequent population growth can restore alleles that were lost',
                'distractors': [
                    'Strong directional selection during the hunting era removed all alleles that reduced resistance to human predation, leaving only the fittest alleles in the recovered population',
                    'Inbreeding among the 20 survivors fixed recessive alleles to homozygosity, and these recessive alleles are now expressed in all individuals, reducing measured heterozygosity',
                    'Genetic drift can reduce diversity only over millions of generations — the ~130 years since the bottleneck is too short to have measurably reduced variation, so the low diversity must predate the bottleneck',
                ],
            },
            {
                'question': 'The Old Order Amish community in Pennsylvania has an unusually high frequency of Ellis-van Creveld syndrome (extra fingers, short stature), caused by a rare recessive allele. The population was founded by a small group of immigrants from Europe. Which evolutionary mechanism BEST explains this elevated frequency?',
                'correct': 'Founder effect — the founding immigrants happened to carry the Ellis-van Creveld allele at higher-than-average frequency by chance, and subsequent population growth within the community amplified that initially elevated frequency',
                'distractors': [
                    'Natural selection favoring the Ellis-van Creveld phenotype in the agricultural Pennsylvania environment — individuals with extra fingers may have had manual dexterity advantages in farm work',
                    'Mutation accumulation — the isolated Amish community has a higher mutation rate at the Ellis-van Creveld locus due to inbreeding, which increases the probability that the same mutation arises repeatedly in each generation',
                    'Gene flow from neighboring Pennsylvania Dutch populations who share a similar recessive allele — intermarriage between the Amish and their neighbors introduced the allele and elevated its frequency above the European baseline',
                ],
            },
            {
                'question': 'Buri\'s 1956 classic Drosophila experiment started 107 populations, each of 16 flies (8 males, 8 females), all heterozygous at the bw75 locus. After 19 generations, most populations had FIXED one allele or the other. What would happen if the same experiment were run with 1,600 flies per population instead of 16?',
                'correct': 'Allele fixation would be much slower and fewer populations would reach fixation by generation 19, because drift is proportional to 1/(2N) — larger populations have less sampling error and allele frequencies change less per generation',
                'distractors': [
                    'The result would be identical — genetic drift is determined solely by the starting heterozygosity (50/50), not by population size, so fixation time is the same regardless of N',
                    'Larger populations would fix alleles FASTER because natural selection for or against bw75 becomes more efficient in large populations and overrides drift, deterministically driving allele frequencies to fixation',
                    'In populations of 1,600, both alleles would reach 50% frequency and be maintained there indefinitely by heterozygote advantage, because large populations always converge on the heterozygote-maximizing equilibrium',
                ],
            },
            {
                'question': 'Cheetahs have extraordinarily low genetic diversity compared to other big cats. Which evolutionary event MOST likely explains this?',
                'correct': 'A severe genetic bottleneck approximately 10,000 years ago reduced the population to a small number of individuals — the surviving lineage carried only a subset of the original genetic variation, and today\'s population is essentially descended from this narrow founding group',
                'distractors': [
                    'Strong purifying selection has eliminated all but the fittest alleles over the past 10,000 years — cheetahs are at the local fitness peak and have no room for additional variation',
                    'Cheetahs reproduce asexually, which prevents genetic recombination from generating new variation each generation',
                    'Cheetahs have the lowest mutation rate of any mammal, which explains why they accumulate very few novel alleles compared to other species',
                ],
            },
            {
                'question': 'Is genetic drift directional?',
                'correct': 'No — drift is random. An allele may increase or decrease in frequency by chance, with no consistent direction. Over time, drift tends to eliminate variation (either fix or lose alleles), but the direction of change in any particular generation is unpredictable',
                'distractors': [
                    'Yes — drift always favors the dominant allele, which is why drift and selection often act in the same direction',
                    'Yes — drift always pushes rare alleles to fixation because they are more likely to be lost by random sampling',
                    'Yes — drift is directional toward heterozygote advantage, which is why it maintains genetic variation in small populations',
                ],
            },
            {
                'question': 'Can genetic drift fix DELETERIOUS alleles in a population?',
                'correct': 'Yes — in small populations, drift can overwhelm weak selection, allowing deleterious alleles to rise in frequency and even become fixed. This is why small populations are vulnerable to "mutational meltdown" and genetic deterioration over time',
                'distractors': [
                    'No — natural selection always prevents deleterious alleles from reaching fixation regardless of population size',
                    'No — drift only affects neutral alleles; deleterious alleles are immune to drift because their fitness cost prevents random sampling',
                    'Yes, but only in populations of fewer than 10 individuals — larger populations are guaranteed protection from this effect',
                ],
            },
            {
                'question': 'The Polynesian colonization of the Pacific islands is often cited as an example of the founder effect. What does this mean in genetic terms?',
                'correct': 'Small founding groups of humans carried only a subset of the alleles present in the source (Asian mainland) population — some alleles were elevated in frequency, others absent, and the descendant island populations reflect the non-random sample rather than the original source gene pool',
                'distractors': [
                    'Polynesian colonizers specifically selected the healthiest individuals from their source population, biasing the genetic composition of descendants toward fitness alleles',
                    'Polynesian colonization introduced new mutations at higher rates than the source population because of the stress of ocean voyages',
                    'The Polynesian example shows that gene flow is more important than drift in shaping island populations',
                ],
            },
            {
                'question': 'L1 RECALL: In Buri\'s 1956 Drosophila drift experiment, how many populations were established, and how many flies (total) were maintained per generation per population?',
                'correct': '107 populations, each with 8 males and 8 females (16 flies total) per generation',
                'distractors': [
                    '10 populations of 100 flies each',
                    '500 populations of 2 flies each',
                    '107 populations of 1,000 flies each',
                ],
            },
            {
                'question': 'L4 APPLICATION: On the island of Pingelap, an unusually high frequency of colorblindness is found. This is most directly an example of:',
                'correct': 'Founder effect — a small founding population happened to carry the colorblindness allele at elevated frequency, and subsequent isolation on the island amplified it',
                'distractors': [
                    'Natural selection favoring colorblindness on a small tropical island',
                    'Balancing selection maintaining both color vision and colorblindness alleles',
                    'Reverse mutation from color vision to colorblindness driven by UV radiation',
                ],
            },
        ],
        visual={
            'type': 'comparison',
            'description': 'Bottleneck vs founder effect',
            'regions': [
                {'label': 'Bottleneck', 'color': '#ff6b6b', 'items': ['Pop crashes', 'Alleles lost', 'Recovery retains low diversity']},
                {'label': 'Founder', 'color': '#4ea8de', 'items': ['Few colonizers', 'Carry only a sample', 'New pop drifts from source']},
                {'label': 'Both', 'color': '#ffc857', 'items': ['Reduced diversity', 'Random, not directional', 'Effect stronger in small N']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Crash vs Colonize.',
            'trap': 'Drift can fix DELETERIOUS alleles if the population is small enough — selection is too weak to remove them.',
        },
    diagram=genetic_drift_bottleneck_vs_founder_diagram(),
    ))
    nodes.append(build_node(
        id='lec4-selection-mechanism',
        title='Natural Selection as Mechanism',
        subtitle='Selection coefficients, allele interactions, response to selection (Lec 4 slides 23-31)',
        color='green', row=4,
        heading='Lecture 4 — Natural Selection as a Mechanism of Evolution',
        sections=[
            {'label': 'CORE CONCEPT', 'body': 'The GENERAL SELECTION MODEL (GSM) formalizes how selection changes allele frequencies. Selection coefficient s = 1 − w, where w is relative fitness (always scaled so the most-fit genotype has w = 1).'},
            {'label': 'WORKED EXAMPLE: PEPPERED MOTH', 'body': 'Biston betularia melanism. Survival: BB = 0.9, Bb = 0.87, bb = 0.55. Relative fitness: BB = 1.0, Bb = 0.96, bb = 0.61. Starting at p = 0.5, the GSM predicts p\' = 0.557, so Δp = +0.057 in one generation.'},
            {'label': 'ALLELIC INTERACTIONS', 'body': 'Selection response depends on DOMINANCE, PLEIOTROPY, EPISTASIS, and ADDITIVE effects. Pleiotropy example: Ester1 in mosquitoes confers insecticide resistance AND increases susceptibility to predation — a trade-off that constrains selection.'},
            {'label': 'KEY TERMS', 'body': 'Selection coefficient (s), relative fitness (w), dominance, pleiotropy, epistasis, additive effects, general selection model.'},
        ] + slides_to_sections(d, (23, 31)),
        examples=[
            'Selection coefficient (s): the fitness reduction of a genotype relative to the best. Relative fitness w = 1-s.',
            'Peppered moth Biston betularia: BB=0.9, Bb=0.87, bb=0.55 survival. Relative fitness BB=1.0, Bb=0.96, bb=0.61. p\'=0.557 from p=0.5 → Δp=+0.057.',
            'Pleiotropy: Ester1 in mosquitoes confers insecticide resistance but increases predation susceptibility.',
            'Dominant, recessive, and additive allele interactions produce different rates of allele frequency change under selection.',
        ],
        warnings=[
            'WATCH OUT: Selection against a RECESSIVE deleterious allele becomes progressively LESS EFFICIENT as the allele gets rarer — it hides more and more in heterozygotes. You CANNOT fully eliminate a recessive allele by selection alone.',
            'WATCH OUT: Relative fitness is always scaled to the BEST genotype (w = 1). A selection coefficient s = 0.1 means 10% fewer offspring than the most fit genotype — NOT eliminated, just disadvantaged.',
        ],
        mnemonic='SCAR = Selection Coefficient = 1 − (fitness / best fitness).',
        flashcard={
            'front': 'How do the rates of allele frequency change differ when selection acts on a dominant versus a recessive allele?',
            'back': 'When selection FAVORS a DOMINANT allele, it rises in frequency rapidly at first because even heterozygotes express the trait — but fixing the last copies of the recessive allele is slow because rare recessives hide in heterozygotes (2pq is hard to eliminate). When selection FAVORS a RECESSIVE allele, it rises SLOWLY at first because only q² homozygotes are exposed to selection — but once it becomes common, it increases rapidly. SELECTING AGAINST a recessive deleterious allele is also inefficient: as q decreases, more and more of the remaining allele hides in heterozygotes, making it nearly impossible to fully eliminate.',
        },
        quiz=[
            {
                'question': 'A recessive lethal allele is under strong negative selection. Why does it persist at low frequencies rather than being eliminated entirely?',
                'correct': 'Heterozygotes are not exposed to selection, so rare alleles hide in 2pq',
                'distractors': [
                    'New copies are constantly replenished by back-mutation from the dominant allele at the same rate selection removes them',
                    'Balancing selection maintains both alleles because heterozygotes have higher fitness than either homozygote',
                    'Genetic drift counteracts selection in large populations, preventing fixation of the favorable dominant allele',
                ],
            },
            {
                'question': 'Sickle cell anemia in malaria-endemic regions of Africa is a classic case of heterozygote advantage. Heterozygotes (HbA/HbS) have higher fitness than BOTH homozygotes. What type of selection maintains the HbS allele at high frequency despite homozygous HbS individuals dying young?',
                'correct': 'Balancing selection via heterozygote advantage (overdominance) — because heterozygotes have the highest fitness, neither allele can be fixed, and both are maintained at a stable intermediate frequency where homozygotes of each genotype are lost at equal rates',
                'distractors': [
                    'Frequency-dependent selection — HbS allele is favored only when it is rare, so it is maintained at the low frequency at which selective advantage kicks in',
                    'Directional selection favoring HbS because it is beneficial — the death of HbS homozygotes is an incidental cost that does not reduce the overall selective advantage enjoyed by the allele',
                    'Mutation-selection balance — the HbS allele persists because new HbS mutations arise from HbA at the same rate that homozygous HbS individuals die, creating a mutation-driven equilibrium unrelated to malaria',
                ],
            },
            {
                'question': 'Selection AGAINST a dominant deleterious allele can eliminate it relatively quickly, while selection against a recessive deleterious allele takes much longer. Which scenario would take LONGEST to eliminate a deleterious allele?',
                'correct': 'A fully recessive allele with s = 0.05 starting at q = 0.001, because at such low frequency almost all copies hide in heterozygotes, and selection can only remove the tiny fraction present in q² homozygotes each generation',
                'distractors': [
                    'A fully dominant allele with s = 0.05 starting at q = 0.001, because dominant alleles are fully exposed in both heterozygotes and homozygotes, so selection removes them in both genotypic backgrounds simultaneously at this starting frequency',
                    'An additive allele with s = 0.10 starting at q = 0.3, because additive alleles experience the most efficient selection in the intermediate frequency range where the 2pq heterozygote frequency is maximized',
                    'A recessive allele with s = 1.0 (lethal) starting at q = 0.5, because even though heterozygotes shelter copies, the lethal effect on homozygotes is so strong that the frequency drops rapidly from 0.5',
                ],
            },
            {
                'question': 'A selection coefficient of s = 0.01 means the disfavored genotype produces 99% as many offspring as the most fit genotype. Over how many generations would a new beneficial mutation (starting at q = 0.001) approach fixation under additive selection with s = 0.01?',
                'correct': 'Approximately 1,000–10,000 generations — weak selection (s = 0.01) requires many generations to push a rare allele to fixation, which is why rapid evolutionary change observed in the field typically involves stronger selection coefficients',
                'distractors': [
                    'About 10 generations — because s = 0.01 means the favored allele increases by 1% per generation and starting at 0.001, it reaches fixation in 1/0.01 = 100 steps, each of which takes about 0.1 generations',
                    'About 1 million generations — because any allele starting at q = 0.001 is so rare that it will almost certainly be lost by drift before selection can act on it, and the 1 in 1 million cases where it survives take millions of generations',
                    'About 100 generations — this is the universal answer for all selection coefficients; any allele under positive selection reaches fixation in approximately N/s generations where N = 100 and s = 0.01',
                ],
            },
            {
                'question': 'Relative fitness (w) is defined as:',
                'correct': 'w = 1 - s, where s is the selection coefficient — fitness is always scaled relative to the BEST genotype (w = 1 for the most fit), and all other genotypes have w < 1',
                'distractors': [
                    'w = 1 + s, because selection always increases fitness above a baseline of 1',
                    'w = s/(1-s), a ratio that never reaches 1',
                    'w = absolute number of offspring produced — not a relative measure at all',
                ],
            },
            {
                'question': 'Selection on a beneficial DOMINANT allele causes it to rise in frequency quickly at first but fixation of the last recessive copies is slow. Why?',
                'correct': 'As the recessive allele becomes rare, most of its remaining copies hide in heterozygotes (where the dominant phenotype masks them) — selection cannot act on these hidden copies, so eliminating the final rare recessive copies becomes very inefficient',
                'distractors': [
                    'The dominant allele causes a sudden decrease in mutation rate that prevents further evolution',
                    'Recessive alleles become more deleterious as they become rarer, so selection pressure against them strengthens over time',
                    'Heterozygote advantage emerges whenever a recessive allele is rare, halting fixation',
                ],
            },
            {
                'question': 'For a new recessive beneficial allele to rise in frequency, which condition must hold initially?',
                'correct': 'Enough individuals must happen to be homozygous for the allele to experience the phenotype — at very low frequencies (q² is tiny), the allele is almost always hidden in heterozygotes and invisible to selection, so initial increase is extremely slow',
                'distractors': [
                    'Recessive alleles rise easily from any starting frequency because selection sees them directly',
                    'Recessive alleles cannot rise in frequency at all — only dominant alleles respond to selection',
                    'Recessive beneficial alleles always rise faster than dominant beneficial alleles because heterozygotes do not interfere',
                ],
            },
            {
                'question': 'A fully ADDITIVE allele has what property that makes its response to selection predictable?',
                'correct': 'Heterozygotes have a phenotype exactly intermediate between the two homozygotes — so every copy of the allele contributes a constant, independent effect regardless of the other allele, making fitness changes linear and predictable',
                'distractors': [
                    'Additive alleles have zero fitness effect by definition — selection cannot change their frequency',
                    'Additive alleles are dominant in heterozygotes, which is why they respond quickly to selection',
                    'Additive alleles are always lethal in homozygotes, creating a fixed intermediate optimum at heterozygote frequency',
                ],
            },
            {
                'question': 'L4 APPLICATION: In the peppered moth (Biston betularia) example, if BB survival = 0.9, Bb = 0.87, and bb = 0.55, what is the RELATIVE fitness of the bb genotype?',
                'correct': 'w(bb) = 0.55 / 0.9 ≈ 0.61',
                'distractors': [
                    'w(bb) = 0.55 — identical to the absolute survival',
                    'w(bb) = 1.0 — because all living moths are fit',
                    'w(bb) = 0.0 — because bb is selected against',
                ],
            },
            {
                'question': 'L5 SYNTHESIS: In Culex mosquitoes, the Ester1 allele confers resistance to organophosphate insecticides but also increases vulnerability to predation. This phenomenon — one locus affecting multiple traits — is called:',
                'correct': 'Pleiotropy',
                'distractors': [
                    'Epistasis — one gene masking another gene\'s effect',
                    'Dominance — one allele masking another at the same locus',
                    'Polygeny — multiple genes affecting one trait',
                ],
            },
        ],
        visual={
            'type': 'curve',
            'description': 'Allele frequency change under selection',
            'regions': [
                {'label': 'Dominant favored', 'color': '#4ea8de', 'items': ['Fast rise at low freq', 'Slow fixation at high freq']},
                {'label': 'Recessive favored', 'color': '#7de2d1', 'items': ['Slow rise at low freq', 'Fast rise at high freq']},
                {'label': 'Additive', 'color': '#ffc857', 'items': ['Constant selection', 'Most predictable']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Dominance hides rare alleles from selection.',
            'trap': 'You cannot eliminate a deleterious recessive allele completely by selection alone — it always hides in heterozygotes at low frequencies.',
        },
    diagram=peppered_moth_selection_diagram(),
    ))
    return nodes


def lec5_6_nodes():
    d = load_lec('lec5_6')
    nodes = []
    nodes.append(build_node(
        id='lec56-quant-intro',
        title='Qualitative vs Quantitative Traits',
        subtitle='Mendelian vs continuous inheritance (Lec 5-6 slides 1-13)',
        color='teal', row=5,
        heading='Lecture 5-6 — Introduction to Quantitative Genetics',
        sections=[
            {'label': 'CORE CONCEPT', 'body': 'QUALITATIVE traits are DISCRETE (one or two loci; Mendelian categories). QUANTITATIVE traits are CONTINUOUS (polygenic; many loci each with a small effect). Edward East\'s 1916 tobacco corolla experiment demonstrated this: 2 loci produced 5 phenotypic classes; 6 loci produced 13 phenotypic classes.'},
            {'label': 'VARIANCE DECOMPOSITION', 'body': 'V_P = V_G + V_E. V_G decomposes further into V_A (additive), V_D (dominance), and V_I (epistatic/interaction). Only V_A responds reliably to selection.'},
            {'label': 'KEY FIGURES', 'body': 'Edward East (1916) — classic tobacco corolla experiment establishing polygenic inheritance.'},
        ] + slides_to_sections(d, (1, 13)),
        examples=[
            'Qualitative: discrete categories (flower color, presence/absence) — often Mendelian, 1 or 2 loci.',
            'Quantitative: continuous variation (height, weight, yield) — many loci each contributing a small effect.',
            'Edward East 1916: tobacco corolla — 2 loci → 5 phenotypic classes; 6 loci → 13 classes.',
            'V_P = V_G + V_E. V_G = V_A (additive) + V_D (dominance) + V_I (epistatic). Only V_A responds to selection.',
        ],
        warnings=[
            'WATCH OUT: V_G includes THREE components (V_A + V_D + V_I). ONLY V_A responds to selection. Breeders equation uses h² = V_A/V_P, NOT V_G/V_P.',
            'WATCH OUT: V_P = V_G + V_E holds ONLY when G and E are uncorrelated and non-interacting. Gene-environment correlations (e.g., tall parents provide better nutrition) can inflate or deflate the apparent genetic component.',
        ],
        mnemonic='VP = VG + VE. Add interaction term V_GxE if relevant.',
        flashcard={
            'front': 'Why do quantitative (polygenic) traits show a continuous bell-curve distribution?',
            'back': 'Quantitative traits are controlled by MANY genes, each with a small additive effect. When many independent small contributions are added (multi-locus segregation), the central limit theorem produces a continuous, approximately normal distribution. Environmental variation adds further to the continuous spread. This contrasts with Mendelian traits controlled by 1-2 loci, which produce discrete categories.',
        },
        quiz=[
            {
                'question': 'The equation V_P = V_G + V_E describes:',
                'correct': 'Decomposition of phenotypic variance into genetic and environmental components',
                'distractors': [
                    'Total mutation rate in a population',
                    'The fitness of each genotype',
                    'The rate of genetic drift in small populations',
                ],
            },
            {
                'question': 'An agricultural scientist reports: "Heritability for yield in our wheat variety is h² = 0.85." A farmer concludes: "Then 85% of my field\'s yield is determined by genetics." What is WRONG with the farmer\'s interpretation?',
                'correct': 'Heritability is the proportion of phenotypic VARIANCE (not phenotype itself) attributable to additive genetic variance IN THAT SPECIFIC POPULATION AND ENVIRONMENT — a different environment or population will give a different h², and the 85% does not mean yield is 85% "caused by genes"',
                'distractors': [
                    'Nothing is wrong — h² = 0.85 means exactly 85% of each plant\'s observed yield is genetically determined; the remaining 15% is due to random developmental noise',
                    'The farmer is correct but should also note that V_G includes dominance and epistatic components, so only V_A contributes to h² — the actual genetic contribution to yield may be even higher than 85%',
                    'The farmer underestimates genetic contribution — h² = 0.85 means that IF you move the plants to a new environment, 85% of yields will remain the same, while only 15% will change due to environmental effects',
                ],
            },
            {
                'question': 'V_G can be decomposed into V_A (additive), V_D (dominance), and V_I (epistatic/interaction) components. Why does ONLY V_A respond predictably to natural selection?',
                'correct': 'V_A is the variance due to allele substitution effects that breed true from parent to offspring — dominance and epistatic effects depend on specific genotypic combinations that are broken up each generation by segregation and recombination, so only the additive portion is reliably inherited',
                'distractors': [
                    'V_A responds to selection because additive alleles are all homozygous — dominance variance disappears because heterozygotes do not exist in natural populations once selection is applied for several generations',
                    'V_D and V_I do not respond to selection because they represent environmental effects that happen to correlate with genotype — once the environment is standardized, only V_A remains, which is why the breeder\'s equation uses h² = V_A/V_P',
                    'V_A is the only component that responds to selection because it is the only type of genetic variance detectable by parent-offspring regression — V_D and V_I are invisible to all statistical methods and therefore cannot be selected',
                ],
            },
            {
                'question': 'Two siblings raised in the same family are phenotypically more similar in IQ than two random strangers. A researcher concludes "this proves IQ is highly heritable." What is the fatal flaw in this reasoning?',
                'correct': 'Shared environment (same household, same nutrition, same schools) can make siblings similar WITHOUT any genetic similarity effect — you need a design that separates genetic from environmental similarity, such as identical twins raised apart or adoption studies',
                'distractors': [
                    'The flaw is that IQ is a polygenic trait — polygenic traits have low heritability by definition because many genes each contribute a tiny, environmentally-labile effect that drowns out the genetic signal in sibling comparisons',
                    'The flaw is that siblings share only 50% of their alleles by descent — the correct comparison is between identical twins, who share 100% of alleles and therefore provide a true estimate of genetic similarity without environmental confounds',
                    'There is no flaw — greater phenotypic similarity in a shared environment is exactly what heritability measures: the correlation between a shared heritable environment (family) and phenotype (IQ)',
                ],
            },
            {
                'question': 'Qualitative and quantitative traits differ primarily in:',
                'correct': 'Qualitative traits show DISCRETE categories (often Mendelian, controlled by 1-2 loci), while quantitative traits show CONTINUOUS variation (controlled by many loci, polygenic)',
                'distractors': [
                    'Qualitative traits are always heritable, while quantitative traits are always environmentally determined',
                    'Qualitative traits are genetic, while quantitative traits are purely environmental',
                    'Qualitative traits appear only in plants, while quantitative traits appear only in animals',
                ],
            },
            {
                'question': 'V_P = V_G + V_E is the basic variance-decomposition equation in quantitative genetics. What assumption does this equation make?',
                'correct': 'It assumes G and E are uncorrelated and non-interacting — if there is gene-environment correlation or G × E interaction, additional covariance or interaction terms must be added (e.g., V_P = V_G + V_E + V_GxE + covariance terms)',
                'distractors': [
                    'It assumes heritability is exactly 0.5 — the equation only holds when genetic and environmental variance are equal',
                    'It assumes all traits are Mendelian — the equation cannot be applied to polygenic traits',
                    'It assumes the population is in Hardy-Weinberg equilibrium — otherwise V_G cannot be calculated',
                ],
            },
            {
                'question': 'V_G can be decomposed into which three components?',
                'correct': 'V_A (additive), V_D (dominance), and V_I (epistatic/interaction) — only V_A responds reliably to selection across generations',
                'distractors': [
                    'V_A (active), V_P (passive), and V_H (hybrid) — representing different phases of gene expression',
                    'V_M (mutation), V_S (selection), V_D (drift) — the three forces that generate genetic variance',
                    'V_A (autosomal), V_X (X-linked), and V_M (mitochondrial) — chromosomal inheritance modes',
                ],
            },
            {
                'question': 'Why do quantitative traits typically show a bell-curve distribution in populations?',
                'correct': 'Many genes each contribute small additive effects, and by the central limit theorem, the sum of many independent small contributions (plus environmental noise) approximates a normal distribution',
                'distractors': [
                    'Bell curves reflect the intrinsic geometry of the genome — DNA structure imposes a normal distribution on all phenotypes',
                    'Bell curves occur only for environmentally determined traits; genetic traits show discrete categories',
                    'Bell curves are a statistical illusion caused by averaging multiple discrete Mendelian traits together',
                ],
            },
            {
                'question': 'L1 RECALL: In Edward East\'s 1916 tobacco corolla experiment, how many phenotypic classes appeared when SIX loci controlled corolla length?',
                'correct': '13 classes',
                'distractors': [
                    '5 classes — the number for 2 loci',
                    '6 classes — one per locus',
                    '36 classes — 6 squared',
                ],
            },
            {
                'question': 'L5 SYNTHESIS: Which specific component of genetic variance (V_A, V_D, or V_I) is used in the NARROW-SENSE heritability formula h² = V_?/V_P?',
                'correct': 'V_A (additive genetic variance) — because only additive effects transmit reliably from parent to offspring and therefore respond to selection',
                'distractors': [
                    'V_D (dominance variance) — because dominance captures the average effect of heterozygotes',
                    'V_I (epistatic variance) — because epistasis includes all genotypic interactions',
                    'V_G overall (V_A + V_D + V_I) — because all genetic variance contributes equally to response',
                ],
            },
        ],
        visual={
            'type': 'decomposition',
            'description': 'Variance decomposition',
            'regions': [
                {'label': 'VP', 'color': '#4ea8de', 'items': ['Total phenotypic variance']},
                {'label': 'VG', 'color': '#7de2d1', 'items': ['Genetic: VA + VD + VI']},
                {'label': 'VE', 'color': '#ffc857', 'items': ['Environmental variance']},
                {'label': 'VGxE', 'color': '#ff6b6b', 'items': ['Gene × environment interaction']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Separate genes, environment, and their interaction.',
            'trap': 'VA (additive genetic variance) is the component that RESPONDS to selection. Dominance and epistatic variance do not transmit as predictably across generations.',
        },
    ))
    nodes.append(build_node(
        id='lec56-heritability-breeders',
        title='Heritability & Breeders Equation',
        subtitle='R = h² × S — predicting evolutionary response (Lec 5-6 slides 14-30)',
        color='blue', row=5,
        heading='Lecture 5-6 — Heritability and Response to Selection',
        sections=[
            {'label': 'CORE CONCEPT', 'body': 'HERITABILITY quantifies the proportion of phenotypic variance attributable to genetic variance. H² (broad-sense) = V_G/V_P. h² (narrow-sense) = V_A/V_P — the component that responds to selection. h² is most often estimated by PARENT-OFFSPRING REGRESSION (the slope of the line gives h²). BREEDERS EQUATION: R = h² × S, where S = selection differential and R = response to selection.'},
            {'label': 'WORKED EXAMPLE', 'body': 'Grant finch study: h² ≈ 0.65, S = 2 mm (larger beaks survived drought) → R = 1.3 mm/generation.'},
            {'label': 'SELECTION REGIMES', 'body': 'DIRECTIONAL: finch beaks under drought. STABILIZING: human birth weight (very large or very small babies have reduced survival). DISRUPTIVE: thoracic bristles in Drosophila; corn oil content in the Illinois long-term selection experiment since 1896.'},
        ] + slides_to_sections(d, (14, 30)),
        examples=[
            'Broad-sense heritability (H²) = VG / VP.',
            'Narrow-sense heritability (h²) = VA / VP — the proportion of phenotypic variance due to ADDITIVE genetic effects.',
            'Breeders equation: R = h² × S, where R = response to selection, S = selection differential.',
            'Grant finch example: h²≈0.65, S=2mm → R=1.3mm/gen.',
            'Parent-offspring regression: slope estimates h² directly.',
            'Illinois corn oil content: over 100 generations of disruptive selection starting 1896 produced dramatically divergent high-oil and low-oil lines.',
            'Stabilizing selection: human birth weight (very large or very small babies have reduced survival).',
        ],
        warnings=[
            'WATCH OUT: High h² does NOT mean environment doesn\'t matter. Dutch height rose ~20 cm in 100 years due to nutrition, despite height being highly heritable.',
            'WATCH OUT: Heritability is population- and environment-specific — cannot be compared across populations or environments.',
        ],
        mnemonic='R = h² × S. Any zero → no response.',
        flashcard={
            'front': 'State the breeders equation, define each term, and explain what determines the response to selection.',
            'back': 'BREEDERS EQUATION: R = h² × S. R = RESPONSE to selection (change in mean phenotype from parent generation to offspring generation). h² = NARROW-SENSE HERITABILITY = V_A / V_P (proportion of phenotypic variance due to additive genetic variance). S = SELECTION DIFFERENTIAL = mean phenotype of breeding individuals minus mean of whole population. The response depends on BOTH h² (how much heritable variation there is) AND S (how strong selection is). If h² is zero, NO response even with strong selection. If S is zero (no selection), NO response even with high h².',
        },
        quiz=[
            {
                'question': 'In a population with h² = 0.5 for body size, a selection differential of S = 10 g is imposed. What is the predicted response R in offspring?',
                'correct': '5 g (R = 0.5 × 10)',
                'distractors': [
                    '10 g (no heritability correction)',
                    '0.5 g (only additive variance matters)',
                    '20 g (R = 2 × h² × S)',
                ],
            },
            {
                'question': 'A livestock breeder selects the heaviest 10% of steers each generation. After 10 generations the average body mass of the herd has NOT changed, despite confirming that h² for body mass is 0.6. What is the MOST likely explanation?',
                'correct': 'The selection differential S ≈ 0, meaning the selected parents are not actually heavier than the population mean — perhaps the top 10% by weight are animals over-fed by accident, not genetically heavier, making S ≈ 0 and therefore R = h²×S ≈ 0',
                'distractors': [
                    'h² = 0.6 is too low for artificial selection to produce a response — body mass selection only works when h² > 0.8 because additive effects must dominate all other genetic components',
                    '10 generations is always too few to detect a response to selection on body mass — changes of this magnitude require at least 50 generations before the population mean shifts measurably',
                    'The breeder violated the HWE requirement by selecting only 10% of the population — natural selection requires random mating from the entire population, and selection on a subset prevents HWE from holding',
                ],
            },
            {
                'question': 'Parent-offspring regression is a common method to estimate h². A researcher plots offspring body weight (y-axis) against midparent body weight (x-axis) and gets a slope of 0.72. In a second study, the same species is raised in a variable field environment and the same regression gives slope = 0.45. Which statement BEST explains the difference?',
                'correct': 'The field environment introduced more V_E (environmental variance), which increased V_P while V_A remained approximately constant — a larger denominator in h² = V_A/V_P yielded a lower estimate even though the genetic architecture of the trait did not change',
                'distractors': [
                    'The field environment caused mutations that increased the dominance variance V_D, which adds to V_G but not to V_A — the measured slope reflects V_G/V_P rather than V_A/V_P when dominance effects are induced by environmental stress',
                    'The regression slope in the field study is the more accurate estimate because laboratory conditions artificially suppress environmental variation, causing laboratory h² to be systematically inflated by a factor of approximately 1.6',
                    'The difference reflects gene × environment interaction (V_GxE) — some genotypes respond differently to field conditions, which creates a correlation between genotype and environment that inflates the laboratory h² and deflates the field h²',
                ],
            },
            {
                'question': 'The Grant finch study measured S (the selection differential) during the 1977 drought. In birds that survived vs. those that died, the survivors averaged beak depth 9.96 mm vs. the pre-drought population mean of 9.42 mm. What was S, and what does this value represent biologically?',
                'correct': 'S = 9.96 − 9.42 = 0.54 mm — the selection differential quantifies how much the trait mean of surviving (breeding) parents exceeds the whole-population mean, indicating the strength of directional selection for larger beaks during the drought',
                'distractors': [
                    'S = 9.42/9.96 = 0.946 — selection differential is the ratio of pre-selection to post-selection means, representing the proportional survival advantage of larger-beaked birds as a fraction of the population mean',
                    'S = (9.96 − 9.42)/9.42 = 0.057 — selection differential is the percentage change in mean beak depth from before to after selection, expressed as a proportion of the pre-drought mean',
                    'S cannot be calculated from these numbers — the selection differential requires knowing the VARIANCE in beak depth, not just the means, to standardize the difference by the standard deviation of the trait',
                ],
            },
            {
                'question': 'What is the difference between broad-sense heritability (H²) and narrow-sense heritability (h²)?',
                'correct': 'H² = V_G/V_P includes ALL genetic variance (additive + dominance + epistatic), while h² = V_A/V_P includes only ADDITIVE genetic variance — only h² reliably predicts response to selection',
                'distractors': [
                    'H² measures heritability across species, while h² measures heritability within species',
                    'H² is measured in the lab, while h² is measured in the field',
                    'H² includes environmental variance, while h² includes only genetic variance',
                ],
            },
            {
                'question': 'Which selection regime describes human birth weight — where infants very large or very small have reduced survival compared to average-weight infants?',
                'correct': 'Stabilizing selection — intermediate phenotypes have the highest fitness, reducing variance around the mean and eliminating extreme phenotypes',
                'distractors': [
                    'Directional selection — where one extreme is favored and the population mean shifts over generations',
                    'Disruptive selection — where both extremes are favored and the population splits into two modes',
                    'Frequency-dependent selection — where fitness depends on how common a phenotype is in the population',
                ],
            },
            {
                'question': 'Which selection regime was demonstrated in the long-term Illinois corn oil content experiment, where selecting for BOTH high AND low oil content each generation caused the two lines to diverge dramatically over 100+ generations?',
                'correct': 'Disruptive (diversifying) selection — selecting against the mean and favoring both extremes produced two distinct populations with markedly different trait values',
                'distractors': [
                    'Stabilizing selection — which would have preserved the original population mean indefinitely',
                    'Directional selection — which only operates in one direction and cannot simultaneously move the population toward two extremes',
                    'Balancing selection via heterozygote advantage — maintaining all three genotypes at equal frequencies',
                ],
            },
            {
                'question': 'Parent-offspring regression estimates heritability directly. What does the SLOPE of the regression line represent?',
                'correct': 'The slope of offspring phenotype (y-axis) vs. midparent phenotype (x-axis) directly estimates narrow-sense heritability h² — because only the additive component of genetic variation transmits reliably from parent to offspring',
                'distractors': [
                    'The slope represents the selection coefficient s, not heritability',
                    'The slope represents environmental variance V_E divided by total phenotypic variance',
                    'The slope represents the number of genes contributing to the trait',
                ],
            },
            {
                'question': 'L1 RECALL: In the Illinois long-term corn oil-content experiment (begun 1896), what type of selection was applied across 100+ generations?',
                'correct': 'Disruptive (diversifying) selection — simultaneously selecting for HIGH oil content in one line and LOW oil content in another line, producing dramatic divergence between the two populations',
                'distractors': [
                    'Directional selection — only for high oil content',
                    'Stabilizing selection — maintaining intermediate oil content',
                    'Balancing selection — maintaining heterozygote advantage at the oil locus',
                ],
            },
            {
                'question': 'L4 APPLICATION: Given h² = 0.65 and S = 2 mm for Grant finch beak depth, what response R is predicted under the breeders equation?',
                'correct': 'R = 0.65 × 2 = 1.3 mm increase per generation',
                'distractors': [
                    'R = 0.65 / 2 = 0.325 mm',
                    'R = 2 × 2 = 4 mm',
                    'R = 0.65 alone = 0.65 mm (no S contribution)',
                ],
            },
        ],
        visual={
            'type': 'equation',
            'description': 'Breeders equation components',
            'regions': [
                {'label': 'R', 'color': '#4ea8de', 'items': ['Response to selection', 'Change in mean next gen']},
                {'label': 'h²', 'color': '#7de2d1', 'items': ['Narrow-sense heritability', 'V_A / V_P']},
                {'label': 'S', 'color': '#ffc857', 'items': ['Selection differential', 'Mean parents - mean pop']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'R = h² × S. Multiplicative — any zero = no response.',
            'trap': 'h² is specific to a population and environment. Changing the environment changes V_E and therefore h².',
        },
    ))
    nodes.append(build_node(
        id='lec56-reaction-norms',
        title='Phenotypic Plasticity & Reaction Norms',
        subtitle='When same genotype gives different phenotypes (Lec 5-6 slides 31-45)',
        color='green', row=5,
        heading='Lecture 5-6 — Phenotypic Plasticity',
        sections=[
            {'label': 'CORE CONCEPT', 'body': 'Phenotypic plasticity is the capacity of a single GENOTYPE to produce different PHENOTYPES in different environments. Plasticity is NOT evolution — no change in allele frequency occurs. The term "reaction norm" was coined by Woltereck (1909): it is a plot of one genotype\'s phenotype across an environmental gradient.'},
            {'label': 'G × E INTERACTION', 'body': 'When different genotypes have differently-shaped reaction norms (the lines cross), V_GxE is nonzero and there is no single "best" genotype across all environments.'},
            {'label': 'POLYPHENISM EXAMPLES', 'body': 'Discrete alternative phenotypes from one genotype in response to environment. Aphids produce winged vs wingless morphs. Daphnia grow defensive neck teeth when the predator Chaoborus is present. Nemoria caterpillars mimic flowers in spring and twigs in summer.'},
            {'label': 'EXPERIMENTAL DESIGNS', 'body': 'COMMON GARDEN: grow multiple populations in the same environment to isolate genetic differences (Achillea/yarrow experiments at Mather vs Stanford demonstrated this). RECIPROCAL TRANSPLANT: grow each population in each environment — classic result is that each population is superior in its own environment of origin (local adaptation).'},
            {'label': 'KEY FIGURES', 'body': 'Woltereck (1909) — coined "reaction norm." Clausen/Keck/Hiesey — Achillea common garden experiments.'},
        ] + slides_to_sections(d, (31, 45)),
        examples=[
            'Reaction norm: a plot showing the phenotype of one genotype across an environmental gradient (term coined by Woltereck 1909).',
            'Plasticity types: continuous (reaction norm) vs discrete (polyphenism — e.g., Daphnia neck teeth, aphid wings, Nemoria caterpillars).',
            'G × E interaction: different genotypes have different reaction-norm shapes. Detect by common-garden experiments.',
            'Common garden: Achillea (yarrow) grown at Mather vs Stanford — multiple genotypes in shared environments.',
            'Reciprocal transplant: each population shown to be superior in its own environment of origin.',
        ],
        warnings=[
            'WATCH OUT: Plasticity is NOT evolution. The REACTION NORM SHAPE is heritable and can evolve; the plastic response itself within an individual is not evolution.',
            'WATCH OUT: G × E means the BEST GENOTYPE CHANGES WITH ENVIRONMENT — adaptation is always environment-specific.',
        ],
        mnemonic='Plastic vs Genetic: Common garden test answers "is the difference genetic or environmental?"',
        flashcard={
            'front': 'What is a reaction norm, and how does a common garden experiment distinguish genetic from environmental contributions to phenotype?',
            'back': 'A REACTION NORM is the relationship between a genotype\'s phenotype and an environmental variable — plotted as a line showing how the same genotype expresses different phenotypes in different environments. A COMMON GARDEN experiment grows multiple genotypes (populations, sibships, clones) in a SHARED environment, removing environmental differences as an explanation. Any remaining phenotypic differences must be GENETIC. A reciprocal transplant (growing each genotype in multiple environments) can reveal G × E interactions — genotypes may differ in HOW they respond to environment, not just their mean.',
        },
        quiz=[
            {
                'question': 'Two plant populations from high and low elevations are grown together in a single common garden at sea level. The populations still differ in growth rate. What does this show?',
                'correct': 'The difference is at least partly genetic — environment alone cannot explain it',
                'distractors': [
                    'The difference must be entirely environmental',
                    'The two populations are the same species',
                    'Plasticity is absent in these populations',
                ],
            },
            {
                'question': 'A researcher measures the reaction norm of two fish genotypes across three water temperatures (10°C, 20°C, 30°C). Genotype A grows fastest at 10°C but slowest at 30°C. Genotype B grows slowest at 10°C but fastest at 30°C. Their reaction norms CROSS at 20°C. What is the evolutionary implication?',
                'correct': 'Genotype × Environment interaction (V_GxE) means there is NO single "best" genotype across all temperatures — which genotype is favored by selection depends entirely on the thermal environment, explaining why genetic variation persists in heterogeneous environments',
                'distractors': [
                    'Both genotypes have the same fitness overall, so genetic variation is maintained by genetic drift rather than by selection — the crossing reaction norms indicate that natural selection cannot distinguish between them',
                    'Genotype A is overall superior because it has a flatter reaction norm, indicating greater phenotypic plasticity; flat reaction norms are always selectively advantageous in variable environments',
                    'The crossing reaction norms prove that heritability of growth rate is zero — when genotypes respond differently to the same environment, it means environmental effects dominate genetic effects and V_A ≈ 0',
                ],
            },
            {
                'question': 'Some social insects (e.g., honey bees) have worker and queen castes that are genetically IDENTICAL but look and behave completely differently. Which concept BEST explains this extreme phenotypic difference within the same genotype?',
                'correct': 'Polyphenism — a discrete type of phenotypic plasticity where the same genome produces radically different phenotypes (castes) depending on environmental triggers (larval nutrition, queen pheromones) during a specific developmental window',
                'distractors': [
                    'Genetic polymorphism — queen and worker bees are actually genetically distinct castes maintained at specific frequencies by frequency-dependent selection within the colony',
                    'Genetic drift — small bee colonies randomly fix queen or worker developmental programs in different individuals, with the probability of becoming a queen determined by sampling variance in larval nutrition',
                    'Horizontal gene transfer — larvae that receive queen-destined nutrition acquire regulatory genes from the food that activate the queen developmental pathway, while worker-destined larvae do not — making caste determination a form of epigenetic HGT',
                ],
            },
            {
                'question': 'Phenotypic plasticity allows a single genotype to produce multiple phenotypes. Despite its apparent advantage, some environments contain organisms with LOW plasticity (fixed phenotypes). Under what condition would LOW plasticity (canalization) be FAVORED by natural selection?',
                'correct': 'When the environment is stable and predictable, a fixed phenotype optimally tuned to that environment outperforms a plastic phenotype that wastes energy on sensing and responding to environmental variation that never actually occurs',
                'distractors': [
                    'Low plasticity is favored when environments are variable and unpredictable — fixed phenotypes allow organisms to commit fully to one strategy and avoid the metabolic cost of developmental uncertainty',
                    'Plasticity is always selectively neutral — whether an organism is plastic or canalized depends entirely on genetic drift, not on the predictability of the environment',
                    'Low plasticity is favored in large populations because phenotypic variance (V_P) must be minimized for Hardy-Weinberg equilibrium to hold — high plasticity would inflate V_E and destabilize the population-genetic equilibrium',
                ],
            },
            {
                'question': 'A reaction norm is defined as:',
                'correct': 'The relationship between a genotype\'s phenotype and an environmental variable — plotted as a line (or curve) showing how the same genotype expresses different phenotypes across different environments',
                'distractors': [
                    'The average phenotype of a population across all environments',
                    'The minimum and maximum possible phenotype for any individual',
                    'The rate at which mutations are accepted in a given environment',
                ],
            },
            {
                'question': 'What is the difference between CONTINUOUS plasticity and a POLYPHENISM?',
                'correct': 'Continuous plasticity produces a smooth gradient of phenotypes across an environmental gradient (e.g., plant height vs. light intensity), while polyphenism produces DISCRETE alternative phenotypes from the same genotype (e.g., queen vs. worker bees, seasonal coat color)',
                'distractors': [
                    'Continuous plasticity involves genetic change, while polyphenism does not',
                    'Continuous plasticity occurs only in plants, while polyphenism occurs only in animals',
                    'Continuous plasticity is heritable, while polyphenism is not',
                ],
            },
            {
                'question': 'The critical insight about plasticity and evolution is that:',
                'correct': 'Plasticity itself (the shape of the reaction norm) is heritable and can evolve — but an individual\'s plastic response is NOT evolution, because evolution requires change in allele frequencies, not phenotypic shifts within a single genotype',
                'distractors': [
                    'Plasticity is the same thing as evolution — both involve phenotypic change over time',
                    'Plasticity prevents evolution because plastic individuals do not need to evolve',
                    'Plasticity is always adaptive and is therefore always favored by selection',
                ],
            },
            {
                'question': 'A reciprocal transplant experiment grows each genotype in multiple environments. What does it specifically test for that a single-environment common garden cannot?',
                'correct': 'G × E interaction — whether different genotypes respond differently to the environmental gradient (e.g., crossing reaction norms), which cannot be detected in a single environment',
                'distractors': [
                    'It tests for mutations that occur during transplantation',
                    'It tests for random genetic drift in the transplanted populations',
                    'It tests for inbreeding depression in the transplanted lineages',
                ],
            },
            {
                'question': 'L1 RECALL: Who coined the term "reaction norm" in 1909?',
                'correct': 'Woltereck',
                'distractors': ['Darwin', 'Fisher', 'Wright'],
            },
            {
                'question': 'L4 APPLICATION: Daphnia grow spiny "neck teeth" when the predator Chaoborus is present in their water, and do NOT grow them when Chaoborus is absent. This is best described as:',
                'correct': 'An inducible polyphenism — a discrete plastic response where the same genotype produces different alternative phenotypes in response to an environmental cue (predator presence)',
                'distractors': [
                    'An example of evolution within a single generation, since allele frequencies change when the predator is added',
                    'A genetic polymorphism, because two discrete Daphnia forms exist in the population',
                    'A purely environmental effect with no genetic basis, because the neck teeth are induced by water chemistry',
                ],
            },
        ],
        visual={
            'type': 'reaction-norm',
            'description': 'Reaction norms across environments',
            'regions': [
                {'label': 'Flat RN', 'color': '#4ea8de', 'items': ['No plasticity', 'Constant phenotype across envs']},
                {'label': 'Sloped RN', 'color': '#7de2d1', 'items': ['Linear plasticity', 'Phenotype tracks env']},
                {'label': 'Crossing RNs', 'color': '#ff6b6b', 'items': ['G × E interaction', 'Best genotype varies by env']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Crossing lines = G × E.',
            'trap': 'Plasticity itself is a heritable trait — selection can shape reaction norms. But plasticity ≠ adaptation.',
        },
    diagram=reaction_norm_gxe_diagram(),
    ))
    return nodes


def lec7_nodes():
    d = load_lec('lec7')
    nodes = []
    nodes.append(build_node(
        id='lec7-review-empirical',
        title='Empirical Natural Selection: Overview',
        subtitle='Case-study methodology for measuring selection in the wild (Lec 7 slides 1-6)',
        color='amber', row=6,
        heading='Lecture 7 — Empirical Studies of Natural Selection',
        sections=[
            {'label': 'CORE CONCEPT', 'body': 'Empirical studies of natural selection combine OBSERVATIONAL and EXPERIMENTAL approaches. To rigorously demonstrate selection, researchers must gather data on phenotypic variation, fitness differences, and heritability — then verify the prediction R = h² × S against observed response.'},
            {'label': 'KEY QUESTION', 'body': 'When observing beak-size evolution, is beak size the DIRECT target of selection, or merely CORRELATED with body size (which is actually the target)? This is the fundamental problem in inferring selection from observation alone.'},
        ] + slides_to_sections(d, (1, 6)),
        warnings=[
            'WATCH OUT: A phenotype-fitness CORRELATION is NOT sufficient proof of selection — the correlation could reflect an environmental confound.',
            'WATCH OUT: R > 0 requires h² > 0 AND S ≠ 0 — both must be confirmed to attribute observed change to selection.',
        ],
        mnemonic='MOD = Measure → Observe differential success → Document inheritance.',
        flashcard={
            'front': 'Why are empirical studies of natural selection in wild populations so difficult, and what three kinds of evidence must be gathered to prove selection is occurring?',
            'back': 'Field selection studies are difficult because: (1) populations are large and individuals must be marked and tracked; (2) the environmental variable causing selection must be identified and often experimentally manipulated; (3) heritability of the trait must be shown separately. To prove selection, you must show: (1) phenotypic VARIATION in the trait, (2) differential FITNESS (survival or reproduction) correlated with the trait, (3) HERITABILITY of the trait. Only then can you predict an evolutionary response (R = h² × S).',
        },
        quiz=[
            {
                'question': 'Which of these alone is NOT sufficient evidence that natural selection is occurring on a trait?',
                'correct': 'Observing phenotypic variation in the population',
                'distractors': [
                    'Heritable differences in fitness correlated with the trait',
                    'Measured change in mean phenotype across generations matching breeders equation',
                    'Experimental manipulation of the trait causing altered fitness',
                ],
            },
            {
                'question': 'A field study observes that larger-bodied wolves have higher survival rates. The researcher concludes natural selection is acting on body size. What additional evidence is MOST critical before this conclusion is solid?',
                'correct': 'Evidence that body size is heritable (h² > 0) in this wolf population — without heritability, the survival correlation could reflect non-genetic effects (e.g., better-fed wolves are larger AND survive better because of better nutrition, not because of body-size genes)',
                'distractors': [
                    'Evidence that the survival advantage of large wolves also applies to females — if sexual selection explains the pattern, it might be male-specific and would involve different mechanisms than ecological natural selection',
                    'Evidence that the wolf population is at Hardy-Weinberg equilibrium for body-size loci — if HWE is violated, selection cannot be inferred from phenotype-fitness correlations alone',
                    'A multi-year study showing the pattern is consistent across several seasons — single-year fluctuations could produce apparent selection signals by chance, so replication across years is more important than heritability data',
                ],
            },
            {
                'question': 'Barrett & Hoekstra tested beach mouse camouflage by placing plasticine mouse models on light and dark substrates. Models that matched their substrate were attacked less often by predators. Why is this experimental approach STRONGER evidence for natural selection than simply observing that light mice live on light sand?',
                'correct': 'The experiment directly manipulates color while controlling for all other variables — it tests whether color per se causes differential predation (a fitness difference), rather than both color and predation being independently caused by an unmeasured third variable',
                'distractors': [
                    'The experiment is stronger because plasticine models can be built with exactly the same body dimensions as real mice, eliminating size as a confound — observational studies cannot control for size differences between light and dark mice',
                    'The experiment uses artificial models, which eliminates genetic drift as an alternative explanation — real mice could differ in survival for reasons unrelated to their coat color, such as behaviorally avoiding predators',
                    'The experiment is stronger because it is conducted under controlled laboratory conditions, which removes all environmental stochasticity — field observations are inherently unreliable because weather variation creates noise in survival data',
                ],
            },
            {
                'question': 'A researcher wants to test whether the red coloration of male guppies (Poecilia reticulata) is under sexual selection by female preference. She increases red pigmentation experimentally in half the males and tracks mating success. What is the CRITICAL control condition this experiment requires?',
                'correct': 'A control group of males with the same experimental manipulation procedure but no actual color change (e.g., sham-treated or manipulated with a non-color substance) — to confirm that any mating advantage comes from the color change itself, not from stress or behavioral changes caused by the manipulation',
                'distractors': [
                    'A control group of females with different color preferences to test whether preference is heritable — without measuring female h², you cannot determine whether the mating advantage will produce an evolutionary response',
                    'A control experiment in a different guppy population where red coloration is absent — this would confirm whether the female preference is a derived trait that co-evolved with red coloration or an ancestral preference that preceded the color',
                    'A control measurement of male survival rate alongside mating success — because color could affect both predation risk and mating success simultaneously, and the net selection on color depends on the balance of both fitness components',
                ],
            },
            {
                'question': 'In empirical studies of natural selection in the wild, what are the three KEY types of evidence that must be gathered to prove that selection is occurring?',
                'correct': 'Phenotypic variation in the trait, differential fitness correlated with the trait, and heritability of the trait — only then can an evolutionary response be predicted and tested',
                'distractors': [
                    'Mutation rate, gene flow rate, and population size',
                    'Age, sex, and body size of study animals',
                    'Hardy-Weinberg equilibrium, linkage disequilibrium, and recombination rate',
                ],
            },
            {
                'question': 'Why are field studies of natural selection more difficult than laboratory studies?',
                'correct': 'Field populations are large and individuals must be marked and tracked, environmental confounds are harder to control, and heritability must often be measured separately from fitness correlations',
                'distractors': [
                    'Natural selection only operates in laboratory conditions, so field studies never actually detect selection',
                    'Field populations always have too few individuals to measure selection statistically',
                    'Wild animals cannot be identified individually, making longitudinal measurements impossible',
                ],
            },
            {
                'question': 'A correlation between a trait and fitness in the wild is NOT sufficient proof of natural selection because:',
                'correct': 'The correlation could be driven by an environmental confound — e.g., well-fed animals are both larger and healthier, so body size and survival are correlated because of nutrition, not because of a genetic body-size effect',
                'distractors': [
                    'Correlations in the wild are never statistically reliable because of noise',
                    'Natural selection requires a negative correlation, not a positive one',
                    'Wild populations cannot be measured accurately, so all field correlations are invalid',
                ],
            },
            {
                'question': 'Observing that a trait mean CHANGED across generations (R > 0) alone is not sufficient proof of natural selection because:',
                'correct': 'Without confirming h² > 0 and measuring S, the trait change could reflect environmental shifts, developmental plasticity, or drift — you must demonstrate that the change matches the breeders equation prediction R = h²S to attribute it to selection',
                'distractors': [
                    'Trait means never actually change across generations without selection, so any observed change automatically proves selection occurred',
                    'R > 0 always indicates drift rather than selection because drift is the only stochastic process in evolution',
                    'Trait changes across generations are not measurable in wild populations, so the observation itself is meaningless',
                ],
            },
            {
                'question': 'L4 APPLICATION: A researcher observes that finches with larger BEAKS have higher survival. Why is it a problem that beak size is also correlated with overall BODY SIZE?',
                'correct': 'Beak size and body size are confounded — selection might be targeting body size (with beak size along for the ride) rather than beak size itself. Without separating them statistically or experimentally, the direct target of selection cannot be identified',
                'distractors': [
                    'Because selection can only act on one trait at a time — body size automatically cancels the beak-size effect',
                    'Because body size is always inherited with lower h² than beak size, making the response impossible to predict',
                    'Because larger body size is always favored, which means beak size has no role in the analysis',
                ],
            },
            {
                'question': 'L5 SYNTHESIS: Which mnemonic summarizes the three-step process for rigorously demonstrating selection in the wild?',
                'correct': 'MOD — Measure phenotypes, Observe differential success, Document inheritance',
                'distractors': [
                    'VHI — Variation, Heritability, Inference',
                    'DNA — Direct, Natural, Adaptive',
                    'FIT — Fitness, Isolation, Transmission',
                ],
            },
        ],
        visual={
            'type': 'checklist',
            'description': 'Proving natural selection in the field',
            'regions': [
                {'label': 'Required evidence', 'color': '#ffc857', 'items': ['Variation', 'Differential fitness', 'Heritability', 'Prediction matches']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'VFHP: Variation, Fitness, Heritability, Prediction.',
            'trap': 'Showing a phenotype-fitness correlation alone is NOT proof of selection — the correlation could be due to confounded environmental effects.',
        },
    ))
    nodes.append(build_node(
        id='lec7-beach-mice',
        title='Beach Mice: Parallel Evolution of Camouflage',
        subtitle='Peromyscus polionotus — two independent origins of light coat color (Lec 7 slides 7-10)',
        color='coral', row=6,
        heading='Lecture 7 — Beach Mice Case Study',
        sections=[
            {'label': 'CORE CONCEPT', 'body': 'Peromyscus polionotus — the oldfield mouse — exists in dark (mainland) and light (beach) forms. On the GULF COAST, a single amino acid change in the Mc1r gene combined with altered Agouti expression produces the light coat. On the ATLANTIC COAST, DIFFERENT genes produce the same phenotype. This is PARALLEL EVOLUTION (Steiner et al. 2009, MBE).'},
            {'label': 'KEY EXPERIMENT', 'body': 'Vignieri et al. 2010 (Evolution) used clay mouse models placed on light and dark substrates. Models that mismatched their substrate were attacked by visual predators (owls, hawks) at higher rates — directly confirming that predators are the selective agent.'},
            {'label': 'RELATED SYSTEM', 'body': 'White Sands lizards (New Mexico) also show Mc1r involvement in pale coat evolution, but with DIFFERENT Mc1r mutations than the beach mice — a classic case of convergent selection acting on the same gene by different mutations.'},
            {'label': 'KEY FIGURES', 'body': 'Hopi Hoekstra (melanism & Mc1r), Steiner et al. 2009 MBE, Vignieri et al. 2010 Evolution.'},
        ] + slides_to_sections(d, (7, 10)),
        examples=[
            'Dark mainland Peromyscus polionotus populations gave rise to two independent light-colored beach populations.',
            'Gulf Coast: Mc1r amino acid change combined with Agouti expression change → light coat.',
            'Atlantic Coast: different genes produce the same light coat phenotype — parallel evolution (Steiner et al. 2009, MBE).',
            'Vignieri et al. 2010 Evolution: clay mouse model experiment confirmed owls and hawks as the selective agents via visual predation.',
            'White Sands lizards: Mc1r with different mutations from beach mice, showing convergent selection on the same gene.',
        ],
        warnings=[
            'WATCH OUT: PARALLEL evolution = same GENE in related populations. CONVERGENT evolution = different genes/lineages arriving at similar phenotypes.',
            'WATCH OUT: Mc1r is only ONE of several genes contributing to coat color — most but not all of the phenotype maps to Mc1r.',
        ],
        mnemonic='MMMP = Mc1r mutation → Melanin loss → Match sand → Predation protection.',
        flashcard={
            'front': 'How does the beach mouse study illustrate the interaction between genetics, phenotype, environment, and selection?',
            'back': 'MAINLAND Peromyscus polionotus have dark fur, matching forest soil. Two BEACH populations (Atlantic and Gulf coasts) have light fur, matching white sand. GENETICS: Hoekstra and colleagues identified a single amino acid change in the Mc1r gene causes the light color in both populations — but the exact mutation differs between the two beach populations. PHENOTYPE: Light fur is cryptic on sand. ENVIRONMENT: Visual predators (birds, mammals) hunt by sight. SELECTION: Predators preferentially eat mice that contrast with the substrate. Barrett & Hoekstra showed this experimentally using plasticine mouse models placed on light and dark substrates — the mismatched models were attacked at higher rates. This case study proves all four ingredients of natural selection in a single system AND shows parallel evolution.',
        },
        quiz=[
            {
                'question': 'Beach mice on the Atlantic and Gulf coasts have similar light coat colors but different Mc1r mutations. This is an example of:',
                'correct': 'Parallel evolution — same phenotypic outcome from independent genetic changes',
                'distractors': [
                    'Convergent evolution between different species',
                    'Genetic drift eliminating variation',
                    'Hybridization between populations',
                ],
            },
            {
                'question': 'The Mc1r gene in beach mice encodes a receptor involved in melanin production. A single amino acid change causes reduced melanin → lighter fur. If this same amino acid change were found in a completely unrelated pale-colored mammal (e.g., a white Arctic fox), it would BEST be described as:',
                'correct': 'Convergent evolution — the same molecular solution to the same selective pressure (camouflage on pale substrate) arose independently in two distantly related species, which is different from the parallel evolution within Peromyscus',
                'distractors': [
                    'Parallel evolution — because the same Mc1r amino acid change is involved in both species, the mechanism is identical and the term "parallel" always applies when the same gene is implicated',
                    'Horizontal gene transfer — because two unrelated species cannot arrive at the exact same amino acid substitution by chance, the Mc1r allele must have been transferred between species via a viral vector at some point',
                    'Homologous evolution — because Mc1r is homologous in all mammals (inherited from the mammalian common ancestor), any shared mutation at this locus represents shared ancestry rather than independent evolution',
                ],
            },
            {
                'question': 'In the beach mouse system, Mc1r accounts for MOST but not ALL of the coat-color difference between beach and mainland populations. Other unnamed loci contribute the remaining variation. What does this illustrate about the genetics of adaptation?',
                'correct': 'Adaptation to the same environment often involves selection on multiple loci simultaneously (polygenic selection), with one major-effect locus (Mc1r) producing most of the phenotypic change while background loci fine-tune the phenotype',
                'distractors': [
                    'It illustrates that selection cannot fully adapt a population to a new environment — the remaining variation from other loci shows that natural selection is always incomplete and populations never reach the local fitness peak',
                    'It illustrates Lamarckian inheritance — the majority of the color change is encoded in Mc1r (genetic), but the remaining variation reflects direct environmental modification of melanocytes by UV exposure on the white sand',
                    'It illustrates a limitation of the study rather than a biological principle — with modern genome-wide association studies, all the contributing loci would be identified and Mc1r would be found to explain 100% of the variation',
                ],
            },
            {
                'question': 'Hoekstra et al. demonstrated that light coat color in beach mice is under selection from visual predators. If the same beach environment suddenly became dark (e.g., volcanic ash covered the sand), what evolutionary prediction would you make over the next 200+ generations?',
                'correct': 'Dark coat color would be selectively favored — light-coated individuals would be more visible against the dark substrate and suffer higher predation; the Mc1r locus and other color loci would be subjected to selection in the opposite direction, shifting allele frequencies back toward the darker ancestral state',
                'distractors': [
                    'No evolutionary change would occur — the light color allele at Mc1r is now fixed in beach populations, and selection cannot re-create the dark ancestral allele once it has been lost from the population',
                    'The mice would evolve thicker fur to protect against the abrasive ash rather than changing color — the primary selective pressure from volcanic ash is physical, not visual, so color-related loci would remain unchanged',
                    'Selection would favor WHITE mice even more strongly, because volcanic ash is associated with high UV radiation and light fur reflects UV better than dark fur — the ash environment would reinforce rather than reverse the current selective advantage',
                ],
            },
            {
                'question': 'The species name for the beach mouse studied by Hoekstra and colleagues is:',
                'correct': 'Peromyscus polionotus — the oldfield mouse, with both mainland (dark) and beach (light) populations',
                'distractors': [
                    'Mus musculus — the common house mouse',
                    'Peromyscus maniculatus — the North American deer mouse',
                    'Microtus californicus — the California vole',
                ],
            },
            {
                'question': 'What specific gene did Hoekstra et al. identify as responsible for most of the light coat color in beach mice?',
                'correct': 'Mc1r — the melanocortin 1 receptor gene, which affects melanin production; a single amino acid change reduces melanin and produces lighter fur',
                'distractors': [
                    'Hox — a homeobox gene controlling body segmentation',
                    'p53 — a tumor suppressor gene controlling cell cycle',
                    'hemoglobin — the oxygen transport protein gene',
                ],
            },
            {
                'question': 'Barrett and Hoekstra tested beach mouse camouflage experimentally using plasticine mouse models placed on different substrates. What was the KEY finding?',
                'correct': 'Models that matched the substrate (light on sand, dark on soil) were attacked less often by visual predators than mismatched models — directly demonstrating that color per se causes differential predation risk',
                'distractors': [
                    'All plasticine models were attacked at equal rates regardless of color, disproving the selection hypothesis',
                    'Dark models were attacked less on all substrates, showing that dark color is universally protective',
                    'Only real mice were attacked; plasticine models were ignored, making the experiment inconclusive',
                ],
            },
            {
                'question': 'A student claims: "Since Mc1r accounts for most of the color difference, beach mouse adaptation is entirely due to a single gene." What is WRONG with this claim?',
                'correct': 'Mc1r accounts for MOST but not ALL of the color difference — other loci also contribute, illustrating that adaptation to a single environment often involves polygenic selection with one major-effect locus alongside several minor-effect loci',
                'distractors': [
                    'The claim is correct — single-gene adaptation is the norm for all evolutionary change',
                    'The claim is wrong because Mc1r is not actually involved — the real color gene has not been identified yet',
                    'The claim is wrong because evolution always involves hundreds of genes equally, and no single gene can dominate adaptation',
                ],
            },
            {
                'question': 'L1 RECALL: Vignieri et al. (2010, Evolution) tested predator-mediated selection in beach mice by what experimental method?',
                'correct': 'Placing clay mouse models on matching and mismatching substrates and counting predator attacks — mismatched models were attacked more, confirming visual predation as the selective agent',
                'distractors': [
                    'Sequencing Mc1r in 1,000 wild beach mice',
                    'Transplanting dark mice to light beaches and monitoring their survival',
                    'Feeding mice with different pigments to induce color change',
                ],
            },
            {
                'question': 'L4 APPLICATION: On the Gulf Coast, beach mice have light coats produced by an Mc1r change AND altered Agouti expression. On the Atlantic Coast, DIFFERENT genes produce the same light-coat phenotype. This pattern is most precisely described as:',
                'correct': 'Parallel evolution — the same phenotypic outcome arose in closely related populations via different genetic changes',
                'distractors': [
                    'Convergent evolution — because the phenotypes match, regardless of the genetic mechanism',
                    'Vestigial evolution — because ancestral light coat alleles were retained',
                    'Horizontal gene transfer — alleles crossed between coast populations via viral vectors',
                ],
            },
        ],
        visual={
            'type': 'comparison',
            'description': 'Beach mouse parallel evolution',
            'regions': [
                {'label': 'Mainland ancestor', 'color': '#6e6a80', 'items': ['Dark fur', 'Forest habitat']},
                {'label': 'Atlantic beach pop', 'color': '#ffc857', 'items': ['Light fur', 'Mc1r mutation A']},
                {'label': 'Gulf beach pop', 'color': '#7de2d1', 'items': ['Light fur', 'Mc1r mutation B']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Two beaches, two mutations, one solution.',
            'trap': 'Parallel ≠ convergent. Parallel evolution = same gene in related lineages. Convergent = different genes or lineages arriving at similar phenotypes.',
        },
    diagram=beach_mice_parallel_evolution_diagram(),
    ))
    nodes.append(build_node(
        id='lec7-tsd',
        title='Temperature-Dependent Sex Determination',
        subtitle='Plasticity as an evolved trait (Lec 7 slides 11-22)',
        color='red', row=6,
        heading='Lecture 7 — Temperature-Dependent Sex Determination (TSD)',
        sections=[
            {'label': 'CORE CONCEPT', 'body': 'TSD (temperature-dependent sex determination) vs GSD (genetic sex determination). In many reptiles (turtles, crocodilians, some lizards), egg incubation temperature determines offspring sex. Example: leopard geckos are male-biased at warm temperatures.'},
            {'label': 'CHARNOV-BULL MODEL', 'body': 'TSD is predicted to be ADAPTIVE when temperature correlates with sex-specific fitness — that is, when the environment that develops a given sex also makes that sex more successful.'},
            {'label': 'KEY EXPERIMENT: JACKY DRAGON', 'body': 'Warner & Shine 2008 (Nature): eggs incubated at 23°C, 27°C, and 33°C. Aromatase inhibitor was used to OVERRIDE the temperature-based sex determination, producing all combinations of sex × incubation temperature in 6 enclosures. Result: males reared at high temp and females reared at low temp had the highest reproductive success — confirming Charnov-Bull.'},
            {'label': 'EXTENDED PHENOTYPE: GALLFLY', 'body': 'A female gallfly lays eggs in goldenrod, inducing gall formation — the gall size is an extended phenotype. Parasitoid wasps preferentially attack SMALL galls; birds preferentially attack LARGE galls — producing STABILIZING selection on gall size.'},
            {'label': 'CLIMATE THREAT', 'body': 'Climate change threatens TSD species because rising temperatures can skew sex ratios beyond the range that produces balanced reproduction.'},
        ] + slides_to_sections(d, (11, 22)),
        examples=[
            'Leopard geckos: male-biased sex ratios at warm incubation temperatures.',
            'Jacky dragon experiment (Warner & Shine 2008 Nature): eggs at 23°C, 27°C, 33°C with aromatase inhibitor to uncouple sex from temp; males reared warm and females reared cool had highest RS — confirms Charnov-Bull.',
            'Gallfly extended phenotype: female lays eggs in goldenrod → gall forms. Parasitoid wasps prefer small galls; birds prefer large galls → stabilizing selection on gall size.',
            'Charnov-Bull model: TSD is adaptive when a temperature affects male and female fitness differently.',
            'Climate change concern: rising temperatures can skew sex ratios, threatening TSD species.',
        ],
        warnings=[
            'WATCH OUT: TSD is a DERIVED trait — it evolved multiple times independently, not a primitive feature.',
        ],
        mnemonic='Charnov-Bull: TSD is adaptive when temperature × sex-specific fitness interaction differs.',
        flashcard={
            'front': 'Under what conditions is temperature-dependent sex determination (TSD) expected to be adaptive, according to the Charnov-Bull model?',
            'back': 'The CHARNOV-BULL model predicts TSD is adaptive when the environment (temperature) experienced during development differentially affects the fitness of males versus females. If a certain temperature makes males successful but females unsuccessful (or vice versa), producing the sex that benefits more at that temperature maximizes parental fitness. For example, if warmer nest temperatures produce larger offspring and female reproductive success depends on body size more than male success, then warm-temperature eggs should develop as females. Climate change can make TSD maladaptive if temperatures exceed the historical range.',
        },
        quiz=[
            {
                'question': 'Which of the following is the greatest conservation threat posed by temperature-dependent sex determination in sea turtles?',
                'correct': 'Rising global temperatures may skew sex ratios so strongly that breeding populations cannot be sustained',
                'distractors': [
                    'Genetic drift will eliminate TSD',
                    'Predators will preferentially eat one sex',
                    'Sea turtles will lose the TSD gene entirely',
                ],
            },
            {
                'question': 'The Charnov-Bull model predicts TSD is adaptive when WHAT condition holds?',
                'correct': 'Temperature differentially affects the fitness of males versus females — the sex that benefits more from development at a particular temperature should be the sex produced there',
                'distractors': [
                    'When populations are small and genetic sex determination would reduce genetic variation in the sex ratio below the Fisher\'s principle 1:1 equilibrium',
                    'When pathogens selectively attack one sex during egg development — TSD evolved to produce whichever sex the pathogen load favors for survival at a given temperature',
                    'When nest temperature is more variable than body temperature — TSD functions as a calibration mechanism that sets the sex ratio to match the thermal variance experienced during embryonic development',
                ],
            },
            {
                'question': 'Some turtle species (Type Ia) produce males at low incubation temperatures and females at high temperatures. Under Charnov-Bull, what does this suggest about how temperature affects fitness in this species?',
                'correct': 'Higher nest temperatures produce offspring with a phenotype (e.g., larger body size) that increases female fitness more than male fitness — perhaps because female reproductive success depends on size, while male fitness does not scale as strongly with developmental temperature',
                'distractors': [
                    'Low temperatures produce males because male reptiles require less developmental energy than females, and cold nests provide less metabolic energy for embryonic development',
                    'High temperatures produce females because female sea turtles spend less time at sea (lower exposure to temperature extremes) — so they are less affected by high developmental temperatures and can benefit from their fitness advantages',
                    'Low temperatures produce males by chance, not adaptive design — Type Ia TSD evolved from ancestral genetic sex determination when a temperature-sensitive regulator of the sex-determining gene mutated, producing the current pattern as a non-adaptive side effect',
                ],
            },
            {
                'question': 'Compared to species with genetic sex determination (GSD), TSD species like sea turtles cannot rapidly evolve a new sex ratio response to changing temperatures because:',
                'correct': 'The reaction norm slope (how sex ratio changes with temperature) is heritable but changes slowly through selection — there is no simple "switch allele" that instantly recalibrates the temperature-sex relationship, unlike GSD where an alternative sex-chromosome system could invade quickly',
                'distractors': [
                    'TSD species lack genetic variation entirely — the sex-determining reaction norm is fixed by developmental physiology and cannot evolve because there are no alleles at sex-determining loci to select among',
                    'TSD species evolve sex ratios faster than GSD species because environmental sex determination can respond plastically to temperature within a generation, which is faster than allele frequency change across generations in GSD',
                    'TSD cannot evolve a new sex ratio response because Fisher\'s principle prevents any population from deviating from 1:1 investment for more than a few generations — strong frequency-dependent selection always restores equal sex ratios before adaptive change can accumulate',
                ],
            },
            {
                'question': 'In which groups of reptiles is temperature-dependent sex determination (TSD) commonly found?',
                'correct': 'Many turtles and crocodilians — in these species, egg incubation temperature during a critical developmental window determines whether the offspring becomes male or female',
                'distractors': [
                    'All snakes and all lizards universally',
                    'Only mammals, specifically in monotremes',
                    'Only birds, whose body temperatures vary during incubation',
                ],
            },
            {
                'question': 'Is TSD an ancestral or derived trait in reptiles?',
                'correct': 'TSD is DERIVED — it evolved multiple times independently in different reptile lineages, and in some cases has been lost and replaced by genetic sex determination. It is not a primitive feature of vertebrates',
                'distractors': [
                    'TSD is ancestral to all vertebrates — all mammals, birds, and reptiles originally used TSD before some lineages evolved genetic sex determination',
                    'TSD evolved once in reptiles and has never been lost since — it is a single evolutionary innovation',
                    'TSD is ancestral only in birds, where it still persists in some species',
                ],
            },
            {
                'question': 'A Type II TSD pattern (e.g., in crocodiles) produces:',
                'correct': 'Males at extreme temperatures (both high and low) and females in the intermediate temperature range — producing a more complex bimodal relationship between temperature and sex',
                'distractors': [
                    'Only males at high temperatures with no temperature sensitivity at low temperatures',
                    'Only females at all temperatures — crocodiles are all-female species',
                    'Random sex ratios independent of temperature',
                ],
            },
            {
                'question': 'Climate change is a conservation threat to TSD species like sea turtles because:',
                'correct': 'Rising temperatures may push nest incubation beyond the range that produces balanced sex ratios — in some turtle species, elevated beach temperatures are already producing almost exclusively female hatchlings, threatening long-term population viability',
                'distractors': [
                    'Climate change directly damages the DNA of TSD species, preventing reproduction',
                    'Climate change eliminates all predators of sea turtles, causing overpopulation and collapse',
                    'Climate change increases sea level and drowns all nests regardless of temperature',
                ],
            },
            {
                'question': 'L2 MECHANISM: Warner & Shine (2008, Nature) tested the Charnov-Bull model in jacky dragons by using aromatase inhibitor. What did this chemical allow them to do?',
                'correct': 'Override the natural temperature-sex relationship, producing males and females at all three incubation temperatures (23°C, 27°C, 33°C) so that the fitness of each sex × temperature combination could be measured independently',
                'distractors': [
                    'Kill all female embryos so only male sex ratios could be measured',
                    'Sequence the sex-determining gene in each embryo directly without DNA extraction',
                    'Induce mutations in the sex-determination pathway to test for genetic sex determination',
                ],
            },
            {
                'question': 'L5 SYNTHESIS: In the gallfly extended phenotype example, why is gall size under STABILIZING selection?',
                'correct': 'Parasitoid wasps preferentially attack SMALL galls while birds preferentially attack LARGE galls — these two opposing predators select against both extremes, favoring intermediate gall size',
                'distractors': [
                    'Only parasitoid wasps are predators, so small galls are selected against in one direction only — this is directional selection',
                    'Stabilizing selection means no selection at all — gall size drifts randomly',
                    'Gall size has no heritable component, so no selection can act on it',
                ],
            },
        ],
        visual={
            'type': 'curve',
            'description': 'TSD curves by species type',
            'regions': [
                {'label': 'Type Ia', 'color': '#4ea8de', 'items': ['Low T → males', 'High T → females', 'e.g., many turtles']},
                {'label': 'Type Ib', 'color': '#ffc857', 'items': ['Low T → females', 'High T → males', 'e.g., some lizards']},
                {'label': 'Type II', 'color': '#ff6b6b', 'items': ['Males at extreme temps', 'Females in middle', 'e.g., crocodiles']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Three temperature-sex curve shapes across reptiles.',
            'trap': 'TSD is NOT a primitive trait — it evolved multiple times and can be lost again. Genetic sex determination is ancestral in most vertebrates.',
        },
    diagram=tsd_charnov_bull_diagram(),
    ))
    nodes.append(build_node(
        id='lec7-fitness-landscape',
        title='Fitness Landscapes',
        subtitle='Wright\'s metaphor for evolutionary dynamics (Lec 7 slides 23-26)',
        color='purple', row=6,
        heading='Lecture 7 — Fitness Landscape',
        sections=[
            {'label': 'CORE CONCEPT', 'body': 'Introduced by Sewall Wright in 1932. A fitness landscape is a metaphorical surface where X and Y axes represent genotypes or trait values, and Z (height) represents fitness. Populations evolve by climbing up the landscape.'},
            {'label': 'DYNAMICS', 'body': 'ADAPTIVE PEAKS are high-fitness genotype combinations. VALLEYS are low-fitness regions between peaks. Natural selection moves populations locally UPHILL and can trap them on suboptimal local peaks. GENETIC DRIFT (or gene flow) can randomly push a population across a valley to reach a higher peak. EPISTASIS creates RUGGEDNESS in the landscape.'},
            {'label': 'EXAMPLES', 'body': 'Northwestern garter snakes: different morphology × behavior combinations form distinct peaks. Gallfly gall-size evolution: multivariate selection with OPPOSING agents (wasps vs birds) creates a stabilizing peak between two valleys.'},
            {'label': 'KEY FIGURE', 'body': 'Sewall Wright (1932) — introduced the fitness landscape metaphor and later the shifting balance theory.'},
        ] + slides_to_sections(d, (23, 26)),
        examples=[
            'Sewall Wright (1932): fitness landscape — a metaphorical surface where x,y axes are genotypes/traits and z (height) is fitness.',
            'Adaptive peaks: high-fitness genotype combinations.',
            'Valleys: low-fitness genotype combinations between peaks.',
            'Populations tend to climb local peaks via natural selection, but may get stuck on suboptimal peaks (can\'t cross valleys).',
            'Drift or gene flow can help populations cross valleys and reach higher peaks.',
            'Northwestern garter snake morphology × behavior combinations produce distinct peaks.',
            'Gallfly gall-size: wasp + bird selection create multivariate stabilizing peak.',
        ],
        warnings=[
            'WATCH OUT: The fitness landscape metaphor is a SIMPLIFICATION — real genotype space is thousands-dimensional, not 2D or 3D.',
            'WATCH OUT: Fitness landscapes CHANGE over time when environments change — a local peak in one environment may be a valley in another.',
        ],
        mnemonic='Peaks & Valleys: Selection → local peak; Drift/flow → cross valley to higher peak.',
        flashcard={
            'front': 'What is a fitness landscape and why can selection alone get "stuck" on a local peak?',
            'back': 'A FITNESS LANDSCAPE (Wright 1932) is a metaphorical surface where axes represent allele combinations (or trait values) and the height at each point is the fitness of that combination. Populations evolve by "climbing" up the landscape — selection pushes them toward higher fitness. However, natural selection only moves a population LOCALLY UPHILL. If a population reaches a LOCAL PEAK, any small change reduces fitness — selection prevents the population from leaving. To reach a HIGHER peak across a valley, the population must temporarily pass through lower-fitness states, which selection opposes. GENETIC DRIFT or GENE FLOW can help populations cross valleys by randomly moving them off the current peak — a classic example of how drift and flow can actually accelerate adaptation under some conditions.',
        },
        quiz=[
            {
                'question': 'A population is stuck on a local fitness peak while a much higher peak exists across a fitness valley. Which process is most likely to help the population move to the higher peak?',
                'correct': 'Genetic drift temporarily pushing the population off the local peak',
                'distractors': [
                    'Stronger stabilizing selection',
                    'Elimination of all mutations',
                    'Reduced population size to zero',
                ],
            },
            {
                'question': 'Sewall Wright proposed that large populations are subdivided into small semi-isolated demes to facilitate crossing fitness valleys. What is his "shifting balance theory" and what is its main critique?',
                'correct': 'Wright proposed that small demes drift off local peaks → selection then drives them to higher peaks → gene flow then spreads the superior genotype to the whole population. Critics argue the gene-flow phase is theoretically unlikely because migrants from the high peak would swamp the deme back to the local peak before spreading the beneficial combination',
                'distractors': [
                    'Wright proposed that all evolution occurs in large homogeneous populations via directional selection alone — drift is too random to produce adaptive change and is only relevant in artificially small laboratory populations',
                    'Wright\'s theory proposed that fitness valleys do not actually exist — the apparent valleys in 2D representations disappear in high-dimensional genotype space where all genetic combinations can be connected by paths of equal fitness',
                    'Wright\'s shifting balance theory was confirmed by the Drosophila bw75 experiment: Buri showed that small demes shift allele frequencies faster than large populations, with the shifted demes then exporting their alleles to neighboring populations via gene flow',
                ],
            },
            {
                'question': 'A fitness landscape metaphor describes evolution as "hill-climbing." In which scenario does this metaphor BREAK DOWN most seriously?',
                'correct': 'When the environment changes, the landscape itself shifts — a genotype sitting on a high peak in last year\'s environment may be in a valley this year. Directional environmental change means populations must track a moving target, and the hill-climbing metaphor implies a static landscape',
                'distractors': [
                    'When mutation rates are very high — many simultaneous mutations prevent populations from moving in a single direction, and the hill-climbing metaphor fails because populations jump randomly across the landscape rather than climbing steadily',
                    'When populations are very large — in populations of millions, all possible genotypes are present simultaneously, so the concept of a single population "position" on the landscape is meaningless and hill-climbing does not apply',
                    'When selection coefficients are greater than 0.1 — strong selection causes populations to move faster than the landscape can accommodate, so populations overshoot fitness peaks and oscillate without ever stabilizing at the optimum',
                ],
            },
            {
                'question': 'The fitness landscape is described as >10,000-dimensional in reality (one axis per segregating locus). If this is true, what important consequence does it have for interpreting real evolutionary trajectories?',
                'correct': 'In high-dimensional space, most local peaks in 2D are connected through ridges of equal or higher fitness in other dimensions — populations may not be as "trapped" as the 2D metaphor implies, because alternative evolutionary paths exist that avoid fitness valleys by moving through other dimensions',
                'distractors': [
                    'High dimensionality means natural selection is impossible in real organisms — with more than 100 loci under selection simultaneously, fitness interactions are too complex for selection to maintain any coherent direction across generations',
                    'High dimensionality proves that the neutral theory of molecular evolution is correct — in >1000-dimensional space, most mutations are equally neutral and drift, not selection, explains the majority of evolutionary change',
                    'High-dimensional fitness landscapes are identical to 2D landscapes for practical purposes because all organisms with more than 10 chromosomes experience independent assortment, which effectively collapses the high-dimensional space into 23 independent 1D selection problems',
                ],
            },
            {
                'question': 'Who introduced the fitness landscape metaphor in 1932?',
                'correct': 'Sewall Wright — his landscape concept visualized evolutionary dynamics as populations climbing a surface defined by genotype-fitness relationships',
                'distractors': [
                    'Charles Darwin — in his original Origin of Species',
                    'Ronald Fisher — in his Fundamental Theorem of Natural Selection',
                    'J.B.S. Haldane — in his population genetics work',
                ],
            },
            {
                'question': 'In Wright\'s fitness landscape metaphor, what do the AXES and HEIGHT represent?',
                'correct': 'The horizontal axes represent genotypes or trait values (allele combinations), and the height (z-axis) represents fitness — so a point on the landscape corresponds to a specific genotype\'s expected fitness',
                'distractors': [
                    'The axes represent time and population size, while height represents genetic variation',
                    'The axes represent latitude and longitude, while height represents species abundance',
                    'The axes represent mutation rate and gene flow, while height represents the number of individuals',
                ],
            },
            {
                'question': 'Why does natural selection alone tend to get a population stuck on a local peak?',
                'correct': 'Selection moves populations only LOCALLY UPHILL — any small change that reduces fitness is opposed, so a population at a local peak cannot cross a fitness valley even if a higher peak exists on the other side',
                'distractors': [
                    'Selection actively prevents populations from reaching any peaks, always pushing them toward the valleys',
                    'Selection randomly chooses between peaks regardless of their height',
                    'Selection moves populations downhill to conserve energy',
                ],
            },
            {
                'question': 'Which evolutionary forces can help a population CROSS a fitness valley to reach a higher peak?',
                'correct': 'Genetic drift (especially in small populations) or gene flow can randomly push a population off its current peak, providing the opportunity to reach higher peaks that selection alone could not access',
                'distractors': [
                    'Only stronger natural selection can help a population escape a local peak',
                    'Only Lamarckian inheritance can bridge fitness valleys',
                    'Only mutation can move populations across valleys, and only when mutation rates exceed 10% per generation',
                ],
            },
            {
                'question': 'Why can fitness landscapes CHANGE over time?',
                'correct': 'When environments change, the fitness of each genotype changes — a combination that was a high peak in one environment may become a valley in another. The landscape itself is not static; it shifts as conditions change, re-starting the evolutionary climb',
                'distractors': [
                    'Fitness landscapes never change — they are fixed by the laws of physics and biochemistry',
                    'Landscapes change only when mutation rates increase, producing new peaks',
                    'Landscapes change only during speciation events',
                ],
            },
            {
                'question': 'L1 RECALL: In what year did Sewall Wright introduce the fitness landscape metaphor?',
                'correct': '1932',
                'distractors': ['1859 (Darwin Origin)', '1900 (Mendel rediscovery)', '1959 (Modern Synthesis)'],
            },
            {
                'question': 'L3 COMPARISON: What does EPISTASIS contribute to the structure of a fitness landscape?',
                'correct': 'Epistasis makes the landscape RUGGED — interactions between loci create multiple peaks and valleys instead of a single smooth surface, which is why selection can get stuck on local optima',
                'distractors': [
                    'Epistasis smooths the landscape by averaging fitness across loci',
                    'Epistasis eliminates all peaks, producing a flat surface',
                    'Epistasis creates only one global peak and no local peaks',
                ],
            },
        ],
        visual={
            'type': 'landscape',
            'description': 'Wright\'s fitness landscape',
            'regions': [
                {'label': 'Local peak', 'color': '#ffc857', 'items': ['Selection traps here']},
                {'label': 'Global peak', 'color': '#7de2d1', 'items': ['Highest fitness combination']},
                {'label': 'Valley', 'color': '#ff6b6b', 'items': ['Low fitness', 'Selection opposes crossing']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Selection is blind to height beyond its immediate neighborhood.',
            'trap': 'Real fitness landscapes are high-dimensional (thousands of genes). 2D visualizations are radical simplifications.',
        },
    diagram=fitness_landscape_diagram(),
    ))
    return nodes
