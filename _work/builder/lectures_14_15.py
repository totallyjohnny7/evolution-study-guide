"""Node generators for Lectures 14-15 (Exam 3 coverage) with LECTURE AUDIO from recordings.

Lec 14 (History of Life, Ch 3) lecture recorded 2026-04-01.
Lec 15 (Phylogenetics, Ch 4) lecture recorded 2026-04-06.

Recording text is pulled verbatim from _work/recordings.json and attached
to the slide clusters the professor was actively discussing.
"""
import json, os
from helpers import load_lec, slides_to_sections, audio_section, build_node
from diagrams.paleozoic_timeline import paleozoic_timeline_diagram
from diagrams.mesozoic_kt_timeline import mesozoic_kt_timeline_diagram
from diagrams.tree_thinking_components import tree_thinking_components_diagram
from diagrams.cladistics_character_matrix import cladistics_character_matrix_diagram
from diagrams.mono_para_polyphyletic_compare import mono_para_polyphyletic_compare_diagram
from diagrams.tiktaalik_transition_flow import tiktaalik_transition_flow_diagram
from diagrams.feathers_before_flight_exaptation import feathers_before_flight_exaptation_diagram

REC_PATH = os.path.join(os.path.dirname(__file__), '..', 'recordings.json')

def _load_recordings():
    with open(REC_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

_REC = _load_recordings()
APR1 = _REC['2026-04-01']['text']
APR6 = _REC['2026-04-06']['text']


# --------------------------------------------------------------------------
# April 1 recording segments (Lec 14 - History of Life)
# Segments are sliced by character range from the 25,221-char transcript.
# These ranges were identified by reading the transcript in 5 ~5k parts.
# --------------------------------------------------------------------------

# Segment A: deep time intro + age-of-Earth debate + radiometric dating
# (covers slides 1-5: lecture goals, 6000 years vs Kelvin 20 My vs 4.568 bya,
#  isotopes and half-life video)
APR1_AGE_EARTH = APR1[0:7500]

# Segment B: Earth formation + "come over someday" mnemonic entry
# (covers slides 6-11 origin-of-life overlap — minimal direct coverage in audio,
#  so we attach the brief formation-of-Earth passage)
APR1_ORIGIN = APR1[7500:9200]

# Segment C: Paleozoic periods walk-through (Ordovician → Permian)
# (covers slides 20-30)
APR1_PALEOZOIC = APR1[9200:15200]

# Segment D: Mesozoic + KT boundary
# (covers slides 31-34)
APR1_MESOZOIC = APR1[15200:20400]

# Segment E: Cenozoic + take-home points
# (covers slides 35-36)
APR1_CENOZOIC = APR1[20400:]


def lec14_nodes():
    d = load_lec('lec14')
    nodes = []

    # ---- Node 1: Age of Earth & Deep Time (slides 1-5) ----
    sections = slides_to_sections(d, (1, 5))
    sections.append(audio_section(
        'Age of Earth, Deep Time, Radiometric Dating (recorded 2026-04-01)',
        APR1_AGE_EARTH,
    ))
    sections.insert(0, {
        'label': 'CORE CONCEPT',
        'body': (
            'Ussher (1664) used biblical chronology to date Earth to ~6,000 years. '
            'Lord Kelvin (late 1800s) calculated ~20 million years from rock-cooling '
            'rates — his math was correct, but he did not know Earth\'s interior '
            'generates heat via radioactive decay, so his ASSUMPTION was wrong.\n\n'
            'Modern answer: Earth is 4.568 billion years old, determined by radiometric '
            'dating. A zircon crystal from Western Australia is dated at 4.4 By using '
            'BOTH U-235 AND U-238 as cross-checks.\n\n'
            'Half-lives used in geochronology:\n'
            '  Rb → Sr:   47 billion years\n'
            '  U  → Pb:   4.5 billion years\n'
            '  K  → Ar:   1.3 billion years\n'
            '  C-14 → N-14: 5,730 years (useful to ~40,000 years)\n\n'
            'Cross-checks: tree-ring dating, ice-core dating, and multiple radiometric '
            'systems all converge on the same ages — independent lines of evidence '
            'confirm deep time.'
        ),
    })
    nodes.append(build_node(
        id='lec14-age-earth',
        title='Age of the Earth & Deep Time',
        subtitle='4.568 billion years via radiometric dating (Lec 14 slides 1-5)',
        color='blue', row=12,
        heading='Lecture 14 — History of Life: Age of the Earth',
        sections=sections,
        examples=[
            'Special Creation: ~6,000 years (incorrect — contradicted by all physical evidence).',
            'Darwin\'s estimate: several billion years based on sediment accumulation rates. Remarkably close for the 1800s.',
            'Lord Kelvin: ~20 million years based on rock cooling rates. WRONG because Kelvin didn\'t know Earth\'s interior generates heat via radioactive decay.',
            'Modern answer: 4.568 billion years via radiometric dating of the oldest zircon crystals (4.4 By old, Western Australia).',
            'Counting to 1 million seconds = 11 days. Counting to 1 billion seconds = 31 years.',
        ],
        warnings=[
            'WATCH OUT (1): Kelvin\'s MATH was correct — his ASSUMPTION (that Earth was a homogeneous, non-heat-generating cooling rock) was wrong. Radioactive decay in the mantle provides a continuous internal heat source that invalidates his cooling model. Always check assumptions, not just arithmetic.',
            'WATCH OUT (2): A half-life is a STATISTICAL property of a population of atoms, not a deterministic prediction for any individual atom. You cannot predict when a single atom will decay — only the rate at which a large population decays.',
        ],
        mnemonic='4.568 billion years — deep time beyond human intuition.',
        flashcard={
            'front': 'How does radiometric dating work, and why is it trusted?',
            'back': 'Radiometric dating relies on radioactive isotopes decaying at a CONSTANT rate into daughter isotopes. The half-life (time for 50% of parent to decay) is fixed for each isotope — unaffected by temperature, pressure, or chemistry. To date a rock: (1) measure the ratio of parent to daughter isotope, (2) know the half-life, (3) calculate elapsed time. Multiple isotope systems (U-Pb, K-Ar, Rb-Sr, C-14) with different half-lives can be applied to the same sample as independent cross-checks. Zircon crystals trap uranium but exclude lead, making them excellent time capsules — the oldest known zircon (4.4 Bya, Western Australia) was dated using both U-235 and U-238 systems and gave the same age. Results also match tree rings and ice cores for recent dates.',
        },
        quiz=[
            {
                'question': 'Why was Lord Kelvin\'s estimate of Earth\'s age (20 million years) so far off?',
                'correct': 'He didn\'t know that Earth\'s interior generates heat via radioactive decay',
                'distractors': [
                    'His math was wrong',
                    'He used the wrong isotopes',
                    'He assumed Earth was older than it is',
                ],
            },
            {
                'question': 'Radiometric dating uses multiple isotope systems (U-Pb, K-Ar, Rb-Sr) on the same rock sample rather than relying on a single system. Why is this multi-system cross-checking crucial for reliability?',
                'correct': 'Different isotope systems have different half-lives and chemical behaviors — if multiple independent systems converge on the same age, it eliminates the possibility that the result is an artifact of one system\'s assumptions or contamination',
                'distractors': [
                    'Using multiple systems averages out random measurement error, producing a more precise date than any single system could provide on its own',
                    'Each isotope system only measures one of three geological eons — U-Pb measures Precambrian, K-Ar the Paleozoic, and Rb-Sr the Mesozoic — so all three are needed for a complete timescale',
                    'Multiple systems are required because radioactive decay rates change slightly with temperature, and averaging across systems corrects for the different temperatures rocks experience',
                ],
            },
            {
                'question': 'Zircon crystals from Western Australia are dated at 4.4 billion years old using U-Pb dating. What property of zircon makes it especially ideal as a time capsule for U-Pb dating?',
                'correct': 'Zircon crystals incorporate uranium into their crystal lattice when they form but chemically exclude lead — so any lead found inside must have come from uranium decay, giving a clean parent-to-daughter ratio with no inherited lead contamination',
                'distractors': [
                    'Zircon has the slowest uranium decay rate of any mineral, so it retains parent isotopes without measurable loss over billions of years even at high temperatures',
                    'Zircon forms only in volcanic rocks, which cool quickly and freeze the initial isotope ratio at the exact moment of crystallization, unlike sedimentary rocks that reset continuously',
                    'Zircon is transparent, allowing scientists to directly observe radioactive decay events under a microscope and count them without needing to dissolve the crystal for mass spectrometry',
                ],
            },
            {
                'question': 'The analogy "counting to 1 million seconds takes 11 days, but counting to 1 billion seconds takes 31 years" is used to explain deep time. What conceptual bias does this analogy combat?',
                'correct': 'Human intuition scales linearly — we treat "1 billion" as only 1000× larger than "1 million," but the actual time difference is enormous; the analogy forces the listener to feel the non-intuitive magnitude of deep geological time',
                'distractors': [
                    'The analogy demonstrates that Earth\'s age was vastly underestimated by all pre-scientific cultures who lacked numerical systems capable of representing numbers above one million',
                    'The analogy illustrates that radioactive decay is exponential rather than linear — each half-life is the same length but the amount of parent isotope decreasing per year gets smaller over time',
                    'The analogy shows that evolution proceeds at a constant rate proportional to elapsed time, so more evolutionary change occurred in the first billion years than in the most recent million years',
                ],
            },
            {
                'question': 'Darwin\'s own estimate for Earth\'s age was "several billion years," based on the rates at which sedimentary rock layers accumulate in river deltas. Although his number was high by modern standards, why is this estimate historically significant?',
                'correct': 'Darwin used a purely mechanistic geological method (sediment accumulation rate) to deduce deep time long before radiometric dating existed — he was in the correct order of magnitude (billions rather than thousands or millions), which gave evolution by natural selection the time it needed to produce observed diversity',
                'distractors': [
                    'Darwin\'s estimate was based on counting tree rings in the oldest bristlecone pines then known, and it proved that evolutionary change could only occur over periods Earth had actually existed',
                    'Darwin borrowed his estimate from Lord Kelvin, who had also calculated billions of years from radioactive decay rates — both men arrived at the same number through independent physics derivations',
                    'Darwin used Bishop Ussher\'s biblical chronology of 6,000 years and multiplied it by the estimated number of fossil strata, producing an approximate age calibrated to religious tradition while remaining scientifically rigorous',
                ],
            },
            {
                'question': 'A student tries to date a 2-billion-year-old rock using carbon-14 dating and gets no measurable signal. What is the BEST explanation for this failure?',
                'correct': 'Carbon-14 has a half-life of ~5,730 years and is only useful for organic material up to ~50,000 years old — after roughly 10 half-lives there is essentially no C-14 left to measure, so it cannot date anything older regardless of sample quality',
                'distractors': [
                    'Carbon-14 only works on volcanic rocks, not sedimentary rocks — the student should have used U-Pb or K-Ar, which are the standard dating systems for sedimentary rock',
                    'The rock must contain too much contamination from modern carbon — C-14 dating works for any age, but contamination from handling gives false blank readings in old samples',
                    'Carbon-14 decay is temperature-sensitive — rocks that experienced deep burial at high temperatures had their C-14 decay rates accelerated, erasing the signal faster than the standard 5,730-year half-life predicts',
                ],
            },
            {
                'question': 'The oldest known zircon crystal from Western Australia is dated at 4.4 billion years old, yet Earth itself formed 4.568 billion years ago. How should the ~170 million year gap be interpreted?',
                'correct': 'Earth formed from accreting debris 4.568 Bya, but the earliest surface was molten and produced no preserved crystalline rock — the oldest zircons (~4.4 Bya) represent the time when Earth\'s crust had cooled enough to form stable minerals, setting a MINIMUM age for the preserved rock record',
                'distractors': [
                    'The gap shows that radiometric dating is inherently inaccurate by ~100-200 million years at these timescales — both dates are estimates with overlapping error bars and should be treated as essentially equivalent',
                    'Zircons dated at 4.4 Bya are contaminated by meteoritic material that pre-dates Earth — the "age" of the zircons reflects interstellar solar-system formation, not Earth formation, so the two numbers cannot be directly compared',
                    'Earth was originally estimated at 4.4 Bya from the Western Australian zircons, and the 4.568 Bya figure is a separate estimate from lunar samples — scientists disagree about which value is correct and both are commonly cited',
                ],
            },
            {
                'question': 'Rubidium-87 decays to strontium-87 with a half-life of ~47 billion years, whereas uranium-238 decays to lead-206 with a half-life of ~4.5 billion years. For dating a 4.0 billion-year-old rock, which system provides more RESOLUTION — and why?',
                'correct': 'U-Pb gives more resolution because a 4.0 By-old rock has already undergone ~0.9 U-238 half-lives, producing measurable quantities of daughter isotope; Rb-Sr has only completed ~0.08 half-lives over the same interval, so the daughter-to-parent ratio is too small to measure precisely',
                'distractors': [
                    'Rb-Sr gives more resolution because its much longer half-life means its decay rate is more stable and less affected by environmental factors during the rock\'s 4 billion-year history',
                    'Both systems give identical resolution because half-life has no effect on precision — only the quality of the mass spectrometer determines resolution for any isotope system',
                    'Rb-Sr gives more resolution for rocks older than 3 By because longer half-lives are required when dating ancient samples, while U-Pb is restricted to samples younger than the U half-life',
                ],
            },
            {
                'question': 'Tree-ring dating (dendrochronology), ice-core dating, and radiometric dating all converge on the same ages for recent geological events (the last ~50,000 years). Why is this independent convergence important for the credibility of deep-time estimates?',
                'correct': 'Three independent methods with different assumptions and different physical mechanisms all giving the same answer means any systematic error would have to independently affect all three — this is vanishingly unlikely, so convergence provides strong confirmation that the methods are accurately measuring absolute time rather than producing correlated artifacts',
                'distractors': [
                    'Convergence is important because the three methods are all calibrated against radiometric dating — when tree-ring and ice-core dates match radiometric dates, it confirms that the calibration procedure is internally consistent rather than providing independent verification',
                    'Convergence is irrelevant for credibility because deep-time estimates (billions of years) rely on radiometric dating alone — the other two methods only work for recent times and cannot confirm or refute the overall age of Earth',
                    'Convergence of the three methods shows that Earth is exactly 50,000 years old — the three dating methods only agree on the last 50,000 years because that is the entire age of the planet, and all older dates are extrapolation errors',
                ],
            },
            {
                'question': 'Ussher (1664) calculated Earth\'s age as ~6,000 years using biblical chronology, while Kelvin later arrived at ~20 million years from cooling-rate physics. What key conceptual distinction separates these two approaches from modern radiometric dating?',
                'correct': 'Ussher used textual authority (genealogies in scripture) and Kelvin used physical modeling under mistaken assumptions (no internal heat source), but neither directly MEASURED elapsed time in matter; radiometric dating measures an ongoing physical process (decay) that has been running since the rock formed, providing a direct physical clock rather than an inference from assumed conditions',
                'distractors': [
                    'Ussher used math while Kelvin used physics; modern radiometric dating uses chemistry, which is more reliable than either because chemistry is the most fundamental science',
                    'All three methods are equivalent in logic — they all estimate elapsed time from a starting condition, and the differences are only in the quality of the starting assumptions; modern radiometric dating is no more direct than Ussher or Kelvin',
                    'Ussher and Kelvin both measured decay of different materials (biblical paper and cooling rocks respectively), so all three methods are forms of radiometric dating using different isotopes',
                ],
            },
        ],
        visual={
            'type': 'timeline',
            'description': 'Competing estimates of Earth\'s age',
            'regions': [
                {'label': 'Special Creation (~6 kya)', 'color': '#e63946', 'items': ['Young Earth', 'No evidence']},
                {'label': 'Kelvin (20 Mya)', 'color': '#f77f00', 'items': ['Based on cooling', 'Ignored radioactive heat']},
                {'label': 'Darwin (~300 Mya)', 'color': '#ffc857', 'items': ['Sediment rates', 'Close for 1800s']},
                {'label': 'Modern (4.568 Bya)', 'color': '#4ea8de', 'items': ['Radiometric', 'Zircons, U-Pb']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': '4.568 billion. Remember the decimal.',
            'trap': 'Carbon-14 dating only works for organic material up to ~50,000 years. For geology, use U-Pb, K-Ar, or Rb-Sr.',
        },
    ))

    # ---- Node 2: Origin of Life & Prebiotic Chemistry (slides 6-11) ----
    sections = slides_to_sections(d, (6, 11))
    sections.append(audio_section(
        'Early Earth formation (brief mention, recorded 2026-04-01)',
        APR1_ORIGIN,
    ))
    sections.insert(0, {
        'label': 'CORE CONCEPT',
        'body': (
            'Early Earth atmosphere: methane (CH4), hydrogen (H2), ammonia (NH3), '
            'water (H2O), carbon dioxide (CO2) — and critically, NO free oxygen. '
            'Energy sources: lightning, UV radiation, volcanic activity, cosmic rays.\n\n'
            'Key experiments producing prebiotic organic molecules:\n'
            '  - MILLER-UREY (1953): Stanley Miller & Harold Urey\'s spark-discharge '
            'apparatus simulated early Earth and produced 20+ amino acids from '
            'inorganic precursors.\n'
            '  - SYDNEY FOX (1977): heating amino acids to 120°C produced peptide-'
            'like bonds.\n'
            '  - CLAUDIA HUBER (1997): carbon monoxide coupling produced stable '
            'peptide bonds on mineral surfaces.\n'
            '  - MURCHISON METEORITE (1989 analysis, fell 1969 Australia): contained '
            'carbon, purines, and pyrimidines — possible extraterrestrial input.\n\n'
            'RNA WORLD hypothesis: RNA can both store genetic information AND '
            'catalyze chemical reactions (as ribozymes). This unique dual function '
            'makes RNA a plausible single-molecule predecessor to DNA + protein life.\n\n'
            'Darwin, in an 1871 letter, imagined a "warm little pond with all sorts '
            'of ammonia and phosphoric salts, light, heat, electricity" — 80+ years '
            'before Miller-Urey tested the hypothesis experimentally.'
        ),
    })
    nodes.append(build_node(
        id='lec14-origin-life',
        title='Origin of Life & Prebiotic Soup',
        subtitle='Miller-Urey, RNA world, abiogenesis (Lec 14 slides 6-11)',
        color='teal', row=12,
        heading='Lecture 14 — Origin of Life from Non-Life',
        sections=sections,
        examples=[
            'Early Earth: no free oxygen, atmosphere of methane/hydrogen/ammonia/water/CO₂. Energy from lightning, UV, volcanoes, cosmic rays.',
            'Murchison meteorite (1989, Australia): contained carbon, purines, pyrimidines — extraterrestrial inputs may have enriched the prebiotic soup.',
            'Miller-Urey (1953): spark-discharge experiment produced 20+ amino acids including glycine, alanine, valine.',
            'Sydney Fox (1977): heated amino acids → weak peptide bonds when added to water. Claudia Huber (1997): CO made stable peptide bonds.',
            'RNA world hypothesis: RNA can BOTH store info AND catalyze reactions — likely predates DNA/protein life.',
        ],
        warnings=[
            'WATCH OUT: Abiogenesis is still an active research area — we know that the building blocks (amino acids, nucleobases, peptides) can form under plausible early-Earth conditions, but the complete pathway from abiotic molecules to a self-replicating cell is NOT fully solved. Be careful not to confuse "plausible chemistry" with "proven pathway."',
            'Darwin 1871 letter: "a warm little pond with all sorts of ammonia and phosphoric salts, light, heat, electricity" — Darwin imagined the scenario 80+ years before Miller-Urey tested it experimentally, a striking example of theoretical anticipation.',
        ],
        mnemonic='Prebiotic soup: methane + ammonia + lightning = amino acids (Miller-Urey).',
        flashcard={
            'front': 'What did the Miller-Urey experiment demonstrate, and why does it matter for origin-of-life theory?',
            'back': 'In 1953, Stanley Miller and Harold Urey built a closed apparatus simulating early Earth conditions: a flask of water (ocean), gases representing the early atmosphere (methane, ammonia, hydrogen, water vapor), and electric sparks (lightning). After running the experiment for a week, they analyzed the water and found 20+ amino acids — including glycine, alanine, and valine — the building blocks of proteins. This proved that ORGANIC molecules essential for life can form spontaneously from INORGANIC precursors under plausible early-Earth conditions. It didn\'t prove life originated this way, but it showed abiogenesis is chemically plausible. Later experiments by Sydney Fox and Claudia Huber showed those amino acids could also be strung into peptide chains.',
        },
        quiz=[
            {
                'question': 'What did the Miller-Urey experiment produce?',
                'correct': 'Over 20 amino acids from inorganic precursors',
                'distractors': [
                    'A complete living cell',
                    'DNA from RNA',
                    'Proteins with catalytic activity',
                ],
            },
            {
                'question': 'The RNA world hypothesis proposes that RNA preceded both DNA and proteins as the molecule of early life. What unique property of RNA makes this hypothesis plausible in a way that DNA-first or protein-first hypotheses are not?',
                'correct': 'RNA can both store genetic information (like DNA) AND catalyze chemical reactions as a ribozyme (like a protein) — it alone could have served as both information-carrier and functional molecule in a pre-cellular world',
                'distractors': [
                    'RNA is more thermally stable than DNA and can survive the high temperatures of early Earth hydrothermal vents, whereas DNA immediately denatures above 60°C',
                    'RNA nucleotides are simpler to synthesize abiotically than amino acids, so RNA polymers would have formed first and then catalyzed the production of amino acids needed for proteins',
                    'RNA replication is error-free because RNA polymerases have proofreading exonucleases, giving early RNA genomes a selective advantage over DNA genomes in high-mutation environments',
                ],
            },
            {
                'question': 'The Murchison meteorite (1969, Australia) contained amino acids and nucleobases. How does this extraterrestrial organic chemistry affect origin-of-life theory?',
                'correct': 'It shows that organic building blocks form spontaneously in space as well as on Earth, meaning early Earth\'s prebiotic soup could have been supplemented by meteorite delivery — abiogenesis does not require all chemistry to have occurred locally',
                'distractors': [
                    'It proves that life itself originated in space (panspermia) and was delivered to Earth fully formed — the Miller-Urey experiment is therefore irrelevant because Earth chemistry played no role',
                    'Meteoritic amino acids are all D-enantiomers, while biological amino acids are L-enantiomers — the Murchison discovery shows that life\'s homochirality must have an abiotic chemical explanation unrelated to meteorites',
                    'The amino acids in the Murchison meteorite are identical to those made in the Miller-Urey experiment, proving that spark-discharge chemistry is the only viable pathway to prebiotic organic molecules',
                ],
            },
            {
                'question': 'Darwin wrote in 1871 about "a warm little pond with ammonia and phosphoric salts, light, heat, electricity" — 80 years before Miller-Urey. Why is this historically significant for the philosophy of science?',
                'correct': 'Darwin generated a testable hypothesis about abiogenesis from first principles before the chemistry could be tested — Miller-Urey\'s experiment then confirmed the hypothesis empirically, illustrating the power of naturalistic reasoning to anticipate experimental results',
                'distractors': [
                    'Darwin\'s letter proves he had access to undisclosed chemical laboratory results from European colleagues, raising questions about whether the Miller-Urey experiment truly originated with Miller and Urey independently',
                    'Darwin\'s warm pond prediction was actually wrong because modern origin-of-life research favors deep-sea hydrothermal vents, showing that even brilliant scientists generate false hypotheses about major questions',
                    'The letter demonstrates that Darwin was not merely a biologist but the first chemist to understand prebiotic synthesis — his contributions to chemistry have been unfairly overshadowed by his work on evolution',
                ],
            },
            {
                'question': 'Sydney Fox (1977) heated dry amino acids and then added water, producing short peptide chains. Claudia Huber (1997) showed that carbon monoxide on mineral surfaces can drive stable peptide-bond formation. How do these experiments extend what Miller-Urey established?',
                'correct': 'Miller-Urey showed that amino acid MONOMERS can form abiotically; Fox and Huber showed those monomers can then polymerize into peptides without biological enzymes — together they bridge the gap from simple precursors to protein-like polymers, addressing the "just monomers is not enough" objection to abiogenesis',
                'distractors': [
                    'Fox and Huber refuted Miller-Urey by showing that amino acids cannot form under spark-discharge conditions and must instead arise on mineral surfaces — their experiments overturn the classical prebiotic soup model',
                    'Fox and Huber showed that Miller-Urey\'s amino acids were contaminants from the glassware, and that true prebiotic polymerization requires enzymes that could not have existed before life',
                    'Fox and Huber demonstrated that peptide bonds can only form at deep-sea hydrothermal vent temperatures, which contradicts the warm-pond hypothesis and supports an alkaline vent origin for life',
                ],
            },
            {
                'question': 'The early Earth atmosphere in the Miller-Urey setup was modeled as methane (CH4), ammonia (NH3), hydrogen (H2), and water vapor — notably LACKING free oxygen (O2). Why is the absence of free oxygen in the simulated early atmosphere essential to the experiment\'s outcome?',
                'correct': 'Free oxygen would rapidly oxidize reduced organic molecules as they form — amino acids and other prebiotic products cannot accumulate in an oxidizing atmosphere. Early Earth was anoxic because cyanobacteria (producing the first O2) had not yet evolved, allowing reduced organic chemistry to proceed',
                'distractors': [
                    'Free oxygen would have reacted with the electrodes in the spark discharge apparatus, producing ozone that blocks UV light needed to catalyze amino acid synthesis — the anoxic condition was a technical requirement of the apparatus rather than a biological one',
                    'The early atmosphere actually contained abundant free oxygen from volcanic outgassing; Miller-Urey deliberately removed it to simplify the chemistry, but the experiment would have produced similar amino acid yields under oxygenated conditions',
                    'Oxygen is required for amino acid synthesis but would have destroyed the simple sugars needed to form RNA backbones — Miller-Urey chose to optimize for amino acids rather than sugars, so they excluded oxygen even though it was present on early Earth',
                ],
            },
            {
                'question': 'The RNA World hypothesis predicts that modern life should retain molecular "fossils" of an RNA-dominated past. Which feature of the modern cell provides the STRONGEST molecular evidence for the RNA World?',
                'correct': 'The ribosome — the molecular machine that translates mRNA into protein — has its catalytic peptidyl transferase activity performed by ribosomal RNA, not protein. This makes the ribosome a ribozyme, supporting the idea that modern protein synthesis is a legacy of an older RNA-only catalytic world',
                'distractors': [
                    'Modern DNA is double-stranded, which would be impossible under the RNA World hypothesis — the strongest evidence is that DNA retains single-stranded segments at replication forks and in regulatory regions, preserving the ancestral RNA-like state',
                    'Human cells contain mitochondrial RNA that is not translated into any protein — this "ghost RNA" is a direct genetic relic of the RNA world preserved in our cells today',
                    'RNA viruses like influenza prove the RNA World hypothesis by showing that RNA-only life can still exist and replicate outside of DNA-based organisms, directly preserving the ancestral RNA life form',
                ],
            },
            {
                'question': 'In the Miller-Urey apparatus, water was boiled to simulate ocean evaporation, the vapor was circulated through a flask containing CH4, NH3, and H2 gases with electrical sparks simulating lightning, and the products were then condensed back into the water flask. Which specific amino acids did the 1953 experiment produce that are still among the 20 standard proteinogenic amino acids used by all modern life?',
                'correct': 'Glycine, alanine, and valine — all three are standard proteinogenic amino acids, demonstrating that a significant fraction of the modern protein alphabet can form spontaneously under plausible abiotic conditions without any biological machinery',
                'distractors': [
                    'Tryptophan, tyrosine, and phenylalanine — the aromatic amino acids were the primary products because aromatic ring structures form most readily under spark-discharge conditions',
                    'Cysteine and methionine — the sulfur-containing amino acids dominated Miller-Urey yields because early Earth was rich in volcanic sulfur compounds',
                    'No actual proteinogenic amino acids formed — the experiment produced only non-standard amino acids with structures similar to but distinct from the biological 20',
                ],
            },
            {
                'question': 'The Murchison meteorite (fell 1969 in Australia, analyzed starting in 1989) contained carbon, purines, and pyrimidines. How does the presence of nucleobases specifically (as opposed to just amino acids) strengthen origin-of-life theory?',
                'correct': 'Purines and pyrimidines are the building blocks of RNA and DNA — their presence in meteorites shows that the raw materials for genetic polymers, not just structural proteins, can form in abiotic environments in deep space; this broadens the RNA World hypothesis by providing a delivery mechanism for nucleobases to early Earth beyond local synthesis',
                'distractors': [
                    'Purines and pyrimidines in Murchison are identical to those in Miller-Urey spark discharge experiments, proving that all RNA building blocks originated from spark discharge rather than from meteorite delivery',
                    'The meteorite nucleobases are evidence that modern RNA-based life existed on Earth\'s ancestor body before the solar system formed — they are biological relics rather than prebiotic molecules',
                    'Nucleobases in meteorites are contamination from modern Earth biology — their detection is an artifact of modern laboratory protocols and does not reflect actual extraterrestrial chemistry',
                ],
            },
            {
                'question': 'The LUCA (Last Universal Common Ancestor) hypothesis proposes that all modern life descends from a single common ancestor that already possessed DNA, ribosomes, and a universal genetic code. In what sense does the RNA World hypothesis PRECEDE LUCA chronologically?',
                'correct': 'LUCA was already a DNA+protein organism with sophisticated cellular machinery — RNA World life is proposed to have existed BEFORE LUCA, as a pre-cellular or proto-cellular stage where RNA served both as genetic material and as catalyst. LUCA represents an already-evolved endpoint of earlier RNA-based life, not the starting point of biochemistry',
                'distractors': [
                    'The RNA World hypothesis and LUCA describe the same organism — RNA World is simply the molecular-level description of what LUCA looked like, and both terms refer to the same ancestor',
                    'The RNA World came AFTER LUCA — the transition from DNA-protein (LUCA) back to RNA-only was a simplification that occurred in some early lineages before being reversed later in evolution',
                    'The RNA World hypothesis contradicts LUCA — if RNA came first, then no single common ancestor can exist because RNA organisms would have had independent origins in different ponds',
                ],
            },
        ],
        visual={
            'type': 'process',
            'description': 'Prebiotic chemistry pathway',
            'regions': [
                {'label': 'Early Earth', 'color': '#6e6a80', 'items': ['No O₂', 'CH₄, NH₃, H₂', 'Lightning, UV']},
                {'label': 'Miller-Urey', 'color': '#4ea8de', 'items': ['Spark discharge', '20+ amino acids']},
                {'label': 'Polymerization', 'color': '#7de2d1', 'items': ['Fox 1977', 'Huber 1997 (CO)']},
                {'label': 'RNA world', 'color': '#ffc857', 'items': ['Self-replicating', 'Ribozymes']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Gas + spark → amino acids → peptides → RNA → life.',
            'trap': 'The early atmosphere composition is debated. Modern estimates include more CO₂ and N₂ than the original Miller-Urey mix — but amino acid production still occurs.',
        },
    ))

    # ---- Node 3: Early Life & Multicellularity (slides 12-20) ----
    # Recording doesn't densely cover this range, so we skip audio here.
    sections = slides_to_sections(d, (12, 20))
    sections.insert(0, {
        'label': 'CORE CONCEPT',
        'body': (
            'EARLIEST TRACES OF LIFE:\n'
            '  - Biomarkers ~3.8 By (Greenland rocks): C-12/C-13 isotope ratios, '
            'lipid pigments like okenane.\n'
            '  - Stromatolites ~3.45 By: layered bacterial mats; STILL ALIVE TODAY '
            'in Shark Bay, Australia.\n'
            '  - LUCA (Last Universal Common Ancestor): ~3.5-3.8 By.\n\n'
            'DIVERGENCE OF THE THREE DOMAINS:\n'
            '  - Archaea ~3.5 By (methane biomarker in Australian rocks).\n'
            '  - Bacteria (including Cyanobacteria ~2.6 By — first O2-releasing '
            'photosynthesis, driving the Great Oxidation Event).\n'
            '  - Eukaryotes ~1.8 By — arose via ENDOSYMBIOSIS: an archaeal host '
            'engulfed a bacterium that became the mitochondrion; a later engulfment '
            'of a cyanobacterium produced the chloroplast (Lynn Margulis, 1960s).\n\n'
            'MULTICELLULARITY: evolved INDEPENDENTLY at least six times — in animals, '
            'plants, fungi, red algae, brown algae, and slime molds. Dictyostelium '
            'discoideum (slime mold) shows the transition in real time: unicellular '
            'amoebae → aggregation → multicellular stalk with spores.\n\n'
            'FIRST ANIMALS: sponges 650-635 Mya, roughly 100 million years before the '
            'Cambrian explosion.'
        ),
    })
    nodes.append(build_node(
        id='lec14-early-life',
        title='Early Life, Stromatolites & Multicellularity',
        subtitle='Biomarkers, LUCA, eukaryotes, first animals (Lec 14 slides 12-20)',
        color='green', row=12,
        heading='Lecture 14 — Earliest Life Forms',
        sections=sections,
        examples=[
            'Biomarkers (3.8 Bya): DNA fragments, isotopic ratios (organic carbon has different ratios than volcanic carbon), molecules like okenane (lipid pigment).',
            'Stromatolites (3.45 Bya): layered mounds formed when biofilm bacteria trap sediment. Still alive today in Shark Bay, Australia.',
            'LUCA (Last Universal Common Ancestor): ~3.5-3.8 Bya. All extant life descends from this.',
            'Archaea (3.5 By): single-celled, biochemically distinct from bacteria and eukaryotes.',
            'Cyanobacteria (2.6 By): first photosynthesis with O₂ as byproduct. First atmospheric oxygen.',
            'Eukaryotes (1.8 By): 100× bigger than bacteria. Endosymbiosis: archaeal cell engulfed a bacterium → mitochondrion. Second event → chloroplast.',
            'Multicellularity evolved INDEPENDENTLY multiple times: animals, plants, fungi, red algae, slime molds.',
            'First animals: sponges, 650-635 Mya.',
        ],
        warnings=[
            'WATCH OUT (1): The fossil record for microbial life is fragmentary. Before ~2 Bya, biomarker evidence (carbon isotope ratios, lipid molecules like okenane) is often the only way to detect life — direct cellular fossils are rare.',
            'WATCH OUT (2): Endosymbiosis was proposed by Lynn Margulis in the 1960s and was REJECTED for years before being accepted only after accumulating molecular evidence (mitochondria/chloroplasts have their own DNA, reproduce by fission, have double membranes, and carry bacterial-type 70S ribosomes). A reminder that revolutionary ideas can be initially dismissed.',
        ],
        mnemonic='LUCA → Archaea → Bacteria → Eukaryotes (via endosymbiosis). Multicellularity: many independent origins.',
        flashcard={
            'front': 'How did eukaryotic cells arise, and what evidence supports endosymbiotic theory?',
            'back': 'Lynn Margulis\'s endosymbiotic theory proposes that eukaryotic cells formed when a larger archaeal cell engulfed (but did not digest) a free-living bacterium, which persisted inside as a mitochondrion. A later endosymbiosis brought in a cyanobacterium that became the chloroplast. Evidence: (1) Mitochondria and chloroplasts have their OWN circular DNA (like bacteria) separate from the nucleus. (2) They reproduce by binary fission, not with the cell cycle. (3) They have double membranes — the outer membrane from the host, the inner from the original bacterium. (4) Their ribosomes are bacterial (70S), not eukaryotic (80S). (5) Antibiotics targeting bacterial ribosomes also affect mitochondria. This was once radical; now it is textbook.',
        },
        quiz=[
            {
                'question': 'Which piece of evidence most strongly supports endosymbiotic theory?',
                'correct': 'Mitochondria and chloroplasts have their own DNA and double membranes',
                'distractors': [
                    'All eukaryotes have mitochondria',
                    'Bacteria are smaller than eukaryotic cells',
                    'Mitochondria generate ATP',
                ],
            },
            {
                'question': 'Lynn Margulis proposed endosymbiotic theory in the 1960s and it was initially rejected. What type of evidence eventually convinced the scientific community?',
                'correct': 'Molecular evidence — mitochondria and chloroplasts have bacterial-type 70S ribosomes (not eukaryotic 80S), and their circular DNA is closely related to free-living bacteria — multiple independent lines of molecular data converged on the same conclusion',
                'distractors': [
                    'Electron microscopy showing that mitochondria have an outer membrane structurally identical to the host cell\'s plasma membrane, proving direct invagination rather than engulfment of a separate cell',
                    'Cell culture experiments showing that if mitochondria are removed from a eukaryotic cell and introduced into a bacterium, the bacterium incorporates them as functional ATP-producing organelles',
                    'The discovery that some plants can survive without mitochondria by fermenting glucose, proving that mitochondria are optional additions rather than essential ancestral components of eukaryotes',
                ],
            },
            {
                'question': 'Cyanobacteria evolved around 2.6 billion years ago and began producing oxygen as a photosynthetic byproduct. Why did this cause a mass extinction of early life?',
                'correct': 'Most early life was anaerobic and evolved in a low-oxygen environment — free oxygen is toxic to organisms that lack antioxidant enzymes; the Great Oxidation Event (~2.4 Bya) rapidly poisoned the dominant anaerobic organisms that had no defenses against reactive oxygen species',
                'distractors': [
                    'Oxygen gas replaced hydrogen in the early atmosphere, eliminating the main fuel source for the chemosynthetic bacteria that dominated the deep ocean, causing ecosystem collapse',
                    'Cyanobacteria were such efficient photosynthesizers that they consumed all available CO₂, triggering a global cooling event that froze the oceans and killed all non-frozen life forms',
                    'Oxygen reacted with the iron dissolved in early oceans to form iron oxide (rust), removing trace minerals from the water column and starving early marine life of essential nutrients',
                ],
            },
            {
                'question': 'Multicellularity evolved independently multiple times in the history of life (animals, plants, fungi, red algae, slime molds). What does this convergent evolution of multicellularity suggest about the underlying mechanisms?',
                'correct': 'Multicellularity is evolutionarily accessible — eukaryotic cell biology (signaling, adhesion proteins, regulated gene expression) already provided the molecular toolkit needed, so the transition from single-celled to multicellular organization was favored independently when selective pressures (predation avoidance, division of labor, size benefits) arose',
                'distractors': [
                    'Each independent origin of multicellularity used an entirely different genetic mechanism, proving that there is no universal pathway and multicellularity cannot be explained by shared ancestry or pre-adaptation',
                    'Multicellularity evolved exactly twice — once in the ancestor of plants and fungi, and once in the ancestor of animals — the other apparent independent origins are actually misclassifications based on morphological convergence',
                    'The repeated evolution of multicellularity is evidence for directed evolution — life has an inherent drive toward increasing complexity that overrides the random nature of mutation and drift',
                ],
            },
            {
                'question': 'Stromatolites are layered mound structures formed when cyanobacterial biofilms trap sediment. Fossil stromatolites date to 3.45 Bya, and living stromatolites are still found today in Shark Bay, Australia. What makes stromatolites uniquely valuable as evidence of early life?',
                'correct': 'They provide DIRECT physical evidence of microbial communities that can be observed in both fossil and living forms — the continuity from 3.45 Bya fossils to modern Shark Bay mats is one of the oldest verifiable records of a single type of ecosystem persisting over billions of years',
                'distractors': [
                    'Stromatolites preserve complete microbial cells with intact DNA, allowing direct sequencing of 3.45 Bya bacterial genomes — they are the only known source of ancient genetic material from the Archean',
                    'Stromatolites are made entirely of inorganic calcium carbonate deposited by geological processes — their value is that they show life was NOT present in the Archean, contradicting claims of 3.45 Bya microbial life',
                    'Stromatolites contain embedded eukaryotic algae from the Archean, pushing the origin of eukaryotes back to 3.45 Bya and rewriting the textbook timeline by nearly 2 billion years',
                ],
            },
            {
                'question': 'LUCA (the Last Universal Common Ancestor) is dated to ~3.5–3.8 billion years ago. How do biologists infer that LUCA existed, given that no direct fossil of LUCA has been found?',
                'correct': 'ALL modern life — bacteria, archaea, and eukaryotes — shares a core set of molecular features (DNA-based heredity, the universal genetic code, ATP as energy currency, shared protein-synthesis machinery); these shared features can only be parsimoniously explained by descent from a single common ancestor that had them all',
                'distractors': [
                    'LUCA is known from a 3.5 Bya fossil discovered in South African chert in 1965 — the specimen preserves a complete cell with recognizable ribosomes, and radiometric dating of the surrounding rock establishes the age',
                    'LUCA\'s DNA has been directly sequenced from deep Earth core samples drilled in Antarctica — the DNA fragments were preserved in amber-like mineral inclusions dating to 3.8 Bya',
                    'Biologists inferred LUCA from its environmental effects on early Earth — LUCA produced abundant methane that shifted atmospheric composition detectably in 3.8 Bya rocks, even though no cellular fossils remain',
                ],
            },
            {
                'question': 'The Archaea and Bacteria are both single-celled prokaryotes with no nucleus, yet they are classified as two separate domains of life. What fundamental feature justifies this separation?',
                'correct': 'Archaea and Bacteria have distinct membrane lipid chemistry (archaea use ether-linked isoprenoid lipids; bacteria use ester-linked fatty-acid lipids) and differ in ribosomal RNA sequences, transcription machinery, and cell-wall composition — these molecular differences are as large as the differences between bacteria and eukaryotes',
                'distractors': [
                    'Archaea live exclusively in extreme environments (hot springs, salt lakes, anoxic vents) while bacteria live in moderate environments — the separation is purely habitat-based rather than molecular',
                    'Archaea have nuclei while bacteria do not, making them closer to eukaryotes — the three-domain classification therefore places Archaea with eukaryotes rather than with bacteria',
                    'Archaea reproduce only via horizontal gene transfer, while bacteria reproduce by binary fission — the difference in reproductive mode is the defining criterion separating the two domains',
                ],
            },
            {
                'question': 'Dictyostelium discoideum (a cellular slime mold) alternates between a unicellular amoeba stage, an aggregated multicellular slug stage, and a fruiting body with a stalk and spore head. Why is Dictyostelium considered a living model for the independent origin of multicellularity?',
                'correct': 'Dictyostelium shows the transition from unicellular to multicellular organization happening within a single organism\'s life cycle — when food is scarce, individual amoebae aggregate into a multicellular structure with differentiated cell types, demonstrating that multicellularity can arise through facultative cooperation among genetically identical cells without requiring any new "multicellularity gene"',
                'distractors': [
                    'Dictyostelium is the direct ancestor of all multicellular organisms (animals, plants, fungi, red algae) — its life cycle preserves the actual evolutionary transition from unicellular to multicellular that occurred once in the ancestor of all complex life',
                    'Dictyostelium evolved multicellularity in the laboratory under experimental conditions in the 1990s — the multicellular stage is an artifact of culture conditions and does not occur in natural populations',
                    'Dictyostelium slime mold stages are unicellular — the multicellular appearance is a single giant cell with multiple nuclei (a syncytium), so it does not represent true multicellularity at all',
                ],
            },
            {
                'question': 'The first sponges appeared 650-635 Mya, roughly 100 million years BEFORE the Cambrian explosion (~542 Mya). Why is it important to emphasize that animal life pre-dates the Cambrian explosion by this substantial interval?',
                'correct': 'The Cambrian explosion is often mischaracterized as the sudden origin of animal life itself — but sponges and other early animals existed tens of millions of years before the Cambrian, showing that the Cambrian event was a RADIATION of pre-existing animal body plans (especially bilaterian animals with hard parts) rather than the origin of multicellular animal life',
                'distractors': [
                    'The 100 million year gap is a dating artifact — radiometric dating of Proterozoic rocks is unreliable, and sponges actually appeared only a few million years before the Cambrian, not 100 million',
                    'Pre-Cambrian sponges were not true animals but rather bacterial colonies that mimicked sponge morphology — genuine animal life did begin at the Cambrian boundary as traditionally taught',
                    'The 100 million year gap disproves the theory of evolution — no animal lineage could persist for 100 million years without undergoing Cambrian-style diversification, so the dates must be wrong',
                ],
            },
                    {
                'question': 'L5 SYNTHESIS: Multicellularity evolved independently at least 6 times (animals, plants, fungi, red algae, brown algae, slime molds). Dictyostelium discoideum aggregates from unicellular amoebae into a slug only when food runs out. What does this reveal about the origin of multicellularity?',
                'correct': 'Multicellularity is not a rare event but a repeated solution arising whenever selection favors cooperation. Dictyostelium shows facultative multicellularity (aggregating only when beneficial) can serve as a stepping stone — the transition does not require simultaneous fixation of many traits',
                'distractors': [
                    'Multicellularity happened only once — all other apparent origins descended from that lineage via horizontal gene transfer',
                    'Dictyostelium contradicts independent origins because transient aggregation is not true multicellularity — true multicellularity requires permanent adhesion and evolved only in animals',
                    'All six origins required the same mutation in a conserved cell-adhesion gene — molecular convergence, not independent solutions',
                ],
            },
],
        visual={
            'type': 'timeline',
            'description': 'Life origins timeline',
            'regions': [
                {'label': '3.8 Bya', 'color': '#6e6a80', 'items': ['Biomarkers', 'LUCA era']},
                {'label': '3.5 Bya', 'color': '#4ea8de', 'items': ['Stromatolites', 'Archaea']},
                {'label': '2.6 Bya', 'color': '#7de2d1', 'items': ['Cyanobacteria', 'First O₂']},
                {'label': '1.8 Bya', 'color': '#ffc857', 'items': ['Eukaryotes', 'Endosymbiosis']},
                {'label': '650 Mya', 'color': '#f77f00', 'items': ['First sponges', 'First animals']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': '3.8 → 3.5 → 2.6 → 1.8 → 0.65 (Bya): life, oxygen, complexity, animals.',
            'trap': 'Oxygen almost killed early life — the Great Oxidation Event (~2.4 Bya) was a mass extinction for anaerobes. Obligate anaerobes retreated to oxygen-free niches.',
        },
    ))

    # ---- Node 4: Cambrian Explosion & Paleozoic (slides 21-30) ----
    sections = slides_to_sections(d, (21, 30))
    sections.append(audio_section(
        'Paleozoic walk-through: Ordovician → Permian (recorded 2026-04-01)',
        APR1_PALEOZOIC,
    ))
    sections.insert(0, {
        'label': 'CORE CONCEPT',
        'body': (
            'EDIACARAN (575-535 Mya): earliest definitive animal fossils (Dickinsonia, '
            'Spriggina). Many body plans disappeared before the Cambrian.\n\n'
            'CAMBRIAN (542-488 Mya): Cambrian EXPLOSION — trilobites; earliest chordates '
            '~520 Mya (Haikouichthys). Burgess Shale (British Columbia, 505 Mya) is a '
            'Lagerstätte with 65,000+ specimens and 93 species (Anomalocaris, Hallucigenia, '
            'Opabinia).\n\n'
            'ORDOVICIAN (488-444 Mya): early bony fish; land plants ~475 Mya; ended with '
            'a glaciation extinction that killed ~85% of species.\n\n'
            'SILURIAN (444-416 Mya): millipede ~428 Mya (first land animal); first vascular '
            'plants; first jawed fish.\n\n'
            'DEVONIAN (416-359 Mya) = "AGE OF FISHES": Dunkleosteus ~380 Mya (6 m predator); '
            'first tetrapods ~370 Mya; Tiktaalik.\n\n'
            'CARBONIFEROUS (359-299 Mya) = "AGE OF AMPHIBIANS": lush coal swamps; O2 reached '
            '~35% driving giant insects; first amniotic egg; synapsid/sauropsid split 300-280 Mya.\n\n'
            'PERMIAN (299-252 Mya): THE GREAT DYING — P-Tr extinction 252 Mya killed ~96% of '
            'species. Siberian Traps volcanism is the leading hypothesis.\n\n'
            'ROBBINS\' MNEMONIC: "COME OVER SOME DAY MAYBE PICKING UP HARD CASH" = '
            'Cambrian / Ordovician / Silurian / Devonian / Mississippian / Pennsylvanian / '
            'Permian / Triassic / Jurassic / Cretaceous.'
        ),
    })
    nodes.append(build_node(
        id='lec14-cambrian-paleozoic',
        title='Cambrian Explosion & Paleozoic Periods',
        subtitle='Burgess Shale to first reptiles (Lec 14 slides 21-30)',
        color='amber', row=12,
        heading='Lecture 14 — Paleozoic: Cambrian through Permian',
        sections=sections,
        examples=[
            'Ediacaran (575-535 Mya): earliest definitive multicellular animals. Many body plans disappeared before the Cambrian.',
            'Cambrian explosion (542-488 Mya): trilobites, early arthropods, first chordates (Haikouichthys, amphioxus-like). Huge burst of body plan diversity.',
            'Burgess Shale (505 Mya, Canadian Rockies): 65,000+ specimens, 93 species. Anoxic mudslides preserved soft tissues. A "Lagerstätte" — exceptional fossil site.',
            'Ordovician (488-444 Mya): early bony fish, first land plants (~475 Mya, moss/liverwort-like).',
            'Silurian (444-416 Mya): first land animals (millipede ~428 Mya). Invertebrates came out of water before vertebrates.',
            'Devonian (416-359 Mya): AGE OF FISHES. Earliest tetrapods (~370 Mya). Dunkleosteus — giant predatory fish up to 6 m long.',
            'Carboniferous (359-299 Mya): AGE OF AMPHIBIANS. Massive coal deposits from the lush land plants. Synapsid/sauropsid split (~300-280 Mya).',
            'Permian (299-251 Mya): first reptiles. Synapsids (→ mammals) vs sauropsids (→ reptiles, dinosaurs, birds). Skull window counts: anapsid, synapsid, diapsid.',
        ],
        warnings=[
            'WATCH OUT (1): "Age of X" means the period when X DOMINATES, not when X first appeared. Age of Fishes = Devonian, but fish originated earlier in the Ordovician. Dominance and origin are different concepts.',
            'WATCH OUT (2): Synapsid ≠ reptile. Synapsids (leading to mammals) are a SEPARATE lineage from sauropsids (leading to reptiles, dinosaurs, and birds). The phrase "mammal-like reptile" is outdated and misleading — synapsids were never part of the reptile lineage.',
        ],
        mnemonic='Robbins\' mnemonic: "COME OVER SOME DAY MAYBE PICKING UP HARD CASH" for Paleozoic and Mesozoic periods (Cambrian / Ordovician / Silurian / Devonian / Mississippian / Pennsylvanian / Permian / Triassic / Jurassic / Cretaceous).',
        flashcard={
            'front': 'What was the Cambrian explosion, and why is the Burgess Shale so important?',
            'back': 'The Cambrian explosion (~542-488 Mya) was a relatively brief geological interval when most major animal PHYLA first appear in the fossil record. It represents a rapid burst of body-plan diversification: trilobites, early arthropods, brachiopods, mollusks, chordates, echinoderms all show up in the Cambrian. The Burgess Shale (Canadian Rockies, 505 Mya) is one of the most important fossil sites on Earth because (1) it captures a snapshot of an entire Cambrian ecosystem, (2) the anoxic conditions from underwater mudslides preserved SOFT tissues — normally fossils only preserve hard parts, (3) it contains 65,000+ specimens representing 93 species, including bizarre forms like Hallucigenia, Opabinia, and Anomalocaris that have no close modern relatives. Because of its exceptional preservation, Burgess Shale is called a "Lagerstätte" (German: storage place).',
        },
        quiz=[
            {
                'question': 'The Devonian is called the "Age of Fishes," but which ADDITIONAL major vertebrate transition also occurred during the Devonian?',
                'correct': 'The first tetrapods appeared (~370 Mya), transitioning from lobe-finned fish to early limbed vertebrates capable of weight-bearing locomotion',
                'distractors': [
                    'The first birds evolved from theropod dinosaurs, marking the origin of powered flight in vertebrates',
                    'The first reptiles diverged into synapsids and sauropsids, establishing the lineages leading to mammals and modern reptiles',
                    'The first bony fish (Osteichthyes) appeared, eventually displacing cartilaginous fish as the dominant vertebrate group',
                ],
            },
            {
                'question': 'The Burgess Shale (~505 Mya, Canadian Rockies) preserves soft tissues that are almost never fossilized. What specific geological conditions allowed this exceptional preservation?',
                'correct': 'Anoxic underwater mudslides rapidly buried organisms and excluded oxygen and decomposers — in the absence of oxygen and scavengers, soft tissues were preserved in fine-grained anoxic sediment rather than rotting away',
                'distractors': [
                    'The Burgess Shale formed in a high-altitude glacial environment where freezing temperatures stopped decomposition, similar to how woolly mammoths are preserved in Siberian permafrost',
                    'Organisms in the Burgess Shale were mineralized while alive by high calcium concentrations in the shallow Cambrian sea, replacing organic tissues with calcite before decomposition could begin',
                    'The Cambrian sea floor at the Burgess site was hypersaline, which dehydrated organisms immediately after burial and inhibited bacterial decomposition through osmotic stress',
                ],
            },
            {
                'question': 'The Permian ended with the largest mass extinction in Earth\'s history (~251 Mya, ~96% of marine species). In the context of Paleozoic period sequence, what makes the Permian extinction particularly dramatic?',
                'correct': 'It was far larger than the K-T (dinosaur) extinction and reset nearly all marine ecosystems — yet life rebounded into the Triassic; this shows that even catastrophic losses do not terminate life, but the biotic recovery took millions of years',
                'distractors': [
                    'The Permian extinction was caused by an asteroid impact identical to the K-T boundary event, as evidenced by a matching iridium layer in Permian rocks worldwide',
                    'The Permian extinction selectively killed only marine life, while land organisms were largely unaffected — this is why terrestrial tetrapods diversified so rapidly in the Triassic',
                    'The Permian extinction marks the transition from the Paleozoic to the Mesozoic Era and was caused entirely by the Pangaea supercontinent forming, which reduced shoreline habitat area',
                ],
            },
            {
                'question': 'Invertebrates (millipedes) colonized land during the Silurian (~428 Mya), BEFORE vertebrates moved onto land in the Devonian. Why does this sequence matter for understanding tetrapod evolution?',
                'correct': 'Invertebrates colonizing land first created a terrestrial ecosystem with food resources (arthropod prey), which would have provided a selective advantage to any vertebrate capable of accessing land — the food base preceded the consumers',
                'distractors': [
                    'Invertebrate land colonization proves that the transition to land is easy and can evolve in any body plan — the Devonian tetrapod transition was therefore not a major evolutionary innovation',
                    'Vertebrates came onto land before invertebrates during the Silurian based on trackway fossils — invertebrates were already present but only the vertebrate tracks are preserved in the rock record',
                    'Invertebrates colonized land in the Silurian by following marine vertebrates that had already pioneered coastal habitats, showing that vertebrate innovation consistently preceded invertebrate diversity',
                ],
            },
            {
                'question': 'The Ediacaran period (575–535 Mya) immediately precedes the Cambrian explosion. Ediacaran fauna include bizarre soft-bodied organisms like Dickinsonia and Spriggina, many with no modern descendants. What does the Ediacaran tell us about pre-Cambrian animal evolution?',
                'correct': 'Multicellular animal life existed well before the Cambrian explosion, but many early body plans did not survive into the Cambrian — the Cambrian explosion was a turnover event where some Ediacaran lineages went extinct while new phyla with hard parts radiated, not a first appearance of all animal life',
                'distractors': [
                    'The Ediacaran fauna are not true animals but rather colonies of bacteria and protists — they show that true multicellularity did not exist before the Cambrian and all modern animal phyla originated in the explosion',
                    'The Ediacaran fauna are direct ancestors of all modern animal phyla — each Ediacaran genus can be matched to a modern phylum through continuous fossil lineages, making the Cambrian explosion merely a preservation artifact',
                    'Ediacaran fossils are all from a single geographic region (the Ediacara Hills of Australia) and represent a local fauna that went extinct without leaving descendants anywhere else — they have no bearing on global animal evolution',
                ],
            },
            {
                'question': 'The Carboniferous period (359–299 Mya) is famous for massive coal deposits, giant insects, and the "Age of Amphibians." What specific geological and biological conditions produced the enormous coal reserves we still mine today?',
                'correct': 'Lush tropical swamp forests dominated by giant lycopsid trees grew in waterlogged soils where dead plant material could not fully decompose — over millions of years, compressed peat transformed into the coal seams that still power industrial economies',
                'distractors': [
                    'Coal formed because Carboniferous atmospheric CO2 was at its highest ever recorded, causing algae in the oceans to photosynthesize at unprecedented rates and settle as organic sludge that later became coal',
                    'Coal deposits formed from the mass extinction of dinosaurs at the end of the Carboniferous — decomposing dinosaur biomass produced the carbon-rich layers that became coal seams across the globe',
                    'Coal originated from spontaneous chemical reactions in Pangaean volcanic lakes, where sulfur from erupting volcanoes reacted with deep groundwater to precipitate carbonaceous minerals',
                ],
            },
            {
                'question': 'The synapsid/sauropsid split (~300–280 Mya, Permian) is a critical branch point. What is the evolutionary significance of this divergence?',
                'correct': 'Synapsids (one skull opening behind the eye) gave rise to mammals; sauropsids (two skull openings) gave rise to modern reptiles, dinosaurs, and birds — this single split in the Permian set up the two dominant tetrapod lineages for the rest of Earth history',
                'distractors': [
                    'The synapsid/sauropsid split separated the warm-blooded amniotes (synapsids = mammals and birds) from cold-blooded amniotes (sauropsids = reptiles and amphibians), establishing endothermy as an ancestral mammalian trait',
                    'The split represents the divergence of aquatic vertebrates (synapsids, which led to whales and ichthyosaurs) from terrestrial vertebrates (sauropsids, which led to all land animals) during the Permian',
                    'The synapsid/sauropsid split was the origin of the first tetrapods — before this split, all animals were fish-like, so the Permian was actually the first time vertebrates moved onto land',
                ],
            },
            {
                'question': 'Trilobites first appeared in the Cambrian and dominated marine ecosystems for nearly 300 million years before going extinct at the end of the Permian. What does their long reign and extinction illustrate about evolutionary success and vulnerability?',
                'correct': 'Evolutionary success over geological timescales does not guarantee survival of catastrophes — trilobites were the most diverse marine arthropods for ~300 million years, yet the end-Permian extinction eliminated them completely, showing that mass extinctions can erase even the most successful lineages in a short interval',
                'distractors': [
                    'Trilobites went extinct because they failed to evolve fast enough to keep up with rising oxygen levels in the Permian oceans — lineages that cannot adapt at the same rate as their environment always go extinct over geological time',
                    'Trilobites survived until the K-T boundary 65 Mya and were wiped out alongside the non-avian dinosaurs — their Paleozoic origin and Cenozoic extinction make them the longest-lived marine lineage ever',
                    'Trilobites are still alive today in deep-sea hydrothermal vents and represent one of the few major Paleozoic lineages to survive both the Permian and K-T extinctions unchanged',
                ],
            },
            {
                'question': 'The Burgess Shale (505 Mya) contains bizarre organisms like Anomalocaris, Hallucigenia, and Opabinia that have no close modern relatives. What evolutionary interpretation does this suggest about Cambrian body-plan diversity?',
                'correct': 'The Cambrian saw experimentation with a wider variety of animal body plans than persist today — many Cambrian phyla went extinct without leaving descendants, so modern animal diversity represents only a subset of the body plans that evolved, and the Cambrian was a time of unusually open morphospace',
                'distractors': [
                    'Anomalocaris, Hallucigenia, and Opabinia are the direct ancestors of modern arthropods, mollusks, and echinoderms respectively — every bizarre Cambrian form has a living descendant in a modern phylum, and the "no modern relatives" claim reflects incomplete taxonomy',
                    'The bizarre Cambrian forms are interpretation errors from the early 20th century — modern re-analysis of Burgess Shale specimens has reclassified all of them as juvenile or malformed members of modern phyla that already existed by the Cambrian',
                    'These organisms prove that Cambrian animals were products of intelligent design rather than evolution — their unique body plans have no evolutionary precursors in the fossil record, contradicting Darwinian gradualism',
                ],
            },
            {
                'question': 'The Carboniferous atmospheric O2 level reached ~35% (compared with ~21% today), and this period produced giant insects such as Meganeura (a dragonfly with a ~70 cm wingspan) and Arthropleura (a ~2 m millipede). What is the proposed mechanistic link between high O2 and giant insect body size?',
                'correct': 'Insects respire via tracheal tubes that passively diffuse O2 into body tissues — at low O2 concentrations, diffusion limits body size because inner tissues cannot receive enough oxygen; higher atmospheric O2 relaxes this constraint and allows insects to evolve larger bodies before hitting the diffusion limit',
                'distractors': [
                    'High O2 caused direct mutations in insect Hox genes that increased body size — the mutation rate of atmospheric oxygen is proportional to the O2 concentration, so Carboniferous insects accumulated size-increasing mutations faster than modern insects',
                    'Insects grew larger because the Carboniferous had fewer vertebrate predators — high O2 is correlated with but not mechanistically responsible for the size increase, which was entirely due to relaxed selection pressure from reduced predation',
                    'High O2 levels created denser air that supported insect flight at larger body sizes — without the aerodynamic benefit of denser atmosphere, modern insects cannot fly above a few grams of body mass regardless of tracheal efficiency',
                ],
            },
            {
                'question': 'The end-Permian extinction (252 Mya, ~96% of marine species) is hypothesized to have been caused by the Siberian Traps — a massive volcanic eruption that produced vast quantities of basaltic lava over ~1 million years. What specific ecological consequences of Siberian Traps volcanism would plausibly drive a ~96% marine extinction?',
                'correct': 'Massive CO2 release drove rapid global warming (greenhouse); sulfur aerosols caused temporary cooling then acid rain; ocean acidification dissolved carbonate shells; deep ocean anoxia killed most marine life — this cascading combination of heat, acidification, and oxygen depletion is uniquely capable of reaching ~96% marine species loss',
                'distractors': [
                    'Siberian Traps basalt directly poisoned the oceans by dissolving into seawater — the unique mineral composition of the basalt released iron toxins that were fatal to all marine invertebrates but left terrestrial organisms untouched',
                    'The eruptions produced an asteroid-impact-like dust cloud that blocked sunlight for 10 million years, freezing the oceans solid and killing all photosynthetic life — the marine extinction was entirely caused by cooling, not by chemical effects',
                    'Siberian Traps emitted radioactive isotopes that caused genetic damage in all marine species — the 96% extinction reflects mutational load rather than any ecological disruption',
                ],
            },
        ],
        visual={
            'type': 'timeline',
            'description': 'Paleozoic periods',
            'regions': [
                {'label': 'Cambrian (542-488)', 'color': '#e63946', 'items': ['Explosion', 'Burgess Shale', 'Trilobites']},
                {'label': 'Ordovician (488-444)', 'color': '#f77f00', 'items': ['Early bony fish', 'First land plants']},
                {'label': 'Silurian (444-416)', 'color': '#ffc857', 'items': ['First land animals', 'Millipedes']},
                {'label': 'Devonian (416-359)', 'color': '#7de2d1', 'items': ['Age of fishes', 'First tetrapods']},
                {'label': 'Carbon. (359-299)', 'color': '#4ea8de', 'items': ['Coal deposits', 'Amphibians dominate']},
                {'label': 'Permian (299-251)', 'color': '#8a5cf6', 'items': ['First reptiles', 'Synapsid/sauropsid split']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Cambrian Ordovician Silurian Devonian Carboniferous Permian.',
            'trap': 'The Permian ended with the LARGEST mass extinction in Earth\'s history (~251 Mya, ~96% of marine species lost) — even bigger than the K-T dinosaur extinction.',
        },
        diagram=paleozoic_timeline_diagram(),
    ))

    # ---- Node 5: Mesozoic, K-T & Cenozoic (slides 31-36) ----
    sections = slides_to_sections(d, (31, 36))
    sections.append(audio_section(
        'Mesozoic + K-T boundary (recorded 2026-04-01)',
        APR1_MESOZOIC,
    ))
    sections.append(audio_section(
        'Cenozoic + take-home points (recorded 2026-04-01)',
        APR1_CENOZOIC,
    ))
    sections.insert(0, {
        'label': 'CORE CONCEPT',
        'body': (
            'TRIASSIC (250-202 Mya): first dinosaurs appear ~230 Mya.\n\n'
            'JURASSIC (202-145 Mya): dinosaur diversification; earliest mammal ancestors '
            '200-180 Mya (small, nocturnal). BIRDS arose within Dinosauria ~150 Mya '
            '(Archaeopteryx).\n\n'
            'CRETACEOUS (145-65 Mya): angiosperms (flowering plants) arose ~132 Mya, '
            'driving coevolution with insects and later enabling primate color vision.\n\n'
            'K-T BOUNDARY (66 Mya): ~10-mile-diameter asteroid impact at Chicxulub, Yucatán. '
            'Global iridium-rich layer marks the boundary; energy release ~100 trillion tons '
            'of TNT equivalent. The "K" comes from German "Kreide" (chalk) because "C" was '
            'already used for Cambrian. Non-avian dinosaurs and ~2/3 of all species went '
            'extinct. Survivors: birds, small mammals, some reptiles, invertebrates.\n\n'
            'CENOZOIC (65 Mya - now): mammals radiate into vacated niches.\n'
            '  - Primates ~50 Mya.\n'
            '  - Apes ~20 Mya.\n'
            '  - Hominins ~7 Mya.\n'
            '  - Homo sapiens ~195,000 years ago.'
        ),
    })
    nodes.append(build_node(
        id='lec14-mesozoic-cenozoic',
        title='Mesozoic, K-T Extinction & Cenozoic',
        subtitle='Dinosaurs, asteroid, mammals, humans (Lec 14 slides 31-36)',
        color='red', row=12,
        heading='Lecture 14 — Mesozoic Era through the Present',
        sections=sections,
        examples=[
            'Triassic (250-202 Mya): first dinosaurs appear ~230 Mya. Dinosaurs dominate land up to ~65 Mya.',
            'Jurassic (202-145 Mya): dinosaur diversification. First mammals (~200-180 Mya, small, nocturnal). Birds arise within Dinosauria (~150 Mya, Archaeopteryx).',
            'Cretaceous (145-65 Mya): rise of flowering plants (~132 Mya). Coevolution of flowers and pollinators → massive insect diversification.',
            'K-T boundary (65 Mya): asteroid impact at Chicxulub, Yucatán. ~10-mile diameter asteroid, ~100 trillion tons TNT equivalent. Iridium-rich layer in rocks worldwide. Global climate change → extinction of non-avian dinosaurs and ~2/3 of all species.',
            'Cenozoic (65 Mya–now): mammals radiate into vacated niches. Primates (~50 Mya, squirrel-sized arboreal). Apes (~20 Mya) as climate cooled and grasslands spread.',
            'Hominins ~7 Mya (bipedal primates). Homo sapiens ~195,000 years ago (oldest known fossils).',
        ],
        warnings=[
            'WATCH OUT (1): Birds ARE dinosaurs — the only surviving dinosaur lineage. The phrase "dinosaurs went extinct" is only true for NON-AVIAN dinosaurs. Modern cladistics places Aves within Dinosauria.',
            'WATCH OUT (2): The K-T boundary is now called the K-Pg boundary (Cretaceous-Paleogene). Mammals existed ALONGSIDE dinosaurs for ~150 million years — they simply stayed small and nocturnal while dinosaurs dominated daytime and large-body niches.',
        ],
        mnemonic='K-T: asteroid → iridium → Chicxulub → 2/3 extinction → mammalian radiation → us.',
        flashcard={
            'front': 'What is the evidence that the K-T extinction was caused by an asteroid impact?',
            'back': 'Multiple lines of evidence converge: (1) A thin global layer of IRIDIUM — an element rare on Earth but common in asteroids — is found in rocks worldwide at exactly 65 Mya, proposed by Walter and Luis Alvarez in 1980. (2) The Chicxulub crater (Yucatán, Mexico), ~180 km across, was identified in the 1990s and dates to precisely 65 Mya. (3) Shocked quartz and microtektites (glass spherules) from the impact are found in the boundary layer. (4) The impact size (~10 mile diameter asteroid) releases energy equivalent to ~100 trillion tons of TNT — enough to throw debris globally, trigger massive fires, and block sunlight for years. (5) The global extinction pattern matches an impact-driven climate collapse: 2/3 of all species lost, preferentially large-bodied animals and anything dependent on photosynthesis. The non-avian dinosaurs went extinct; birds (a dinosaur lineage) survived.',
        },
        quiz=[
            {
                'question': 'Why is iridium the "smoking gun" for the K-T extinction being caused by an asteroid?',
                'correct': 'Iridium is rare in Earth\'s crust but abundant in asteroids, and a global iridium layer dates to exactly 65 Mya',
                'distractors': [
                    'Iridium is toxic to dinosaurs specifically',
                    'Iridium only forms from impacts',
                    'Iridium was used by dinosaurs for camouflage',
                ],
            },
            {
                'question': 'Birds are the only surviving dinosaur lineage. What type of logical error do students commit when they say "dinosaurs went extinct 65 million years ago" without qualification?',
                'correct': 'It conflates "non-avian dinosaurs" with "all dinosaurs" — the statement is only accurate if you specify NON-AVIAN dinosaurs, because birds are directly descended from theropod dinosaurs and are therefore living dinosaurs by cladistic definition',
                'distractors': [
                    'The statement is completely accurate because paleontologists use "dinosaur" exclusively for Mesozoic forms — modern birds are classified in a separate clade (Aves) that is not part of Dinosauria by consensus',
                    'The error is in the date — the last non-avian dinosaurs survived until ~55 Mya in isolated refugia, so "65 million years ago" overstates the precision of the extinction timing',
                    'The error is that dinosaurs never went extinct — many dinosaur lineages are still represented by crocodilians, which are the closest living relatives of non-avian dinosaurs based on molecular data',
                ],
            },
            {
                'question': 'Mammals existed alongside dinosaurs for ~150 million years but stayed small and nocturnal. After the K-T event, mammals radiated rapidly into empty ecological niches. What evolutionary concept does this pattern best illustrate?',
                'correct': 'Adaptive radiation driven by ecological opportunity — when dominant competitors (non-avian dinosaurs) were removed, the constraints on mammalian body size and niche diversity were lifted, and selection rapidly filled vacant niches with new forms',
                'distractors': [
                    'Punctuated equilibrium — mammals were in stasis for 150 million years then changed rapidly, exactly matching Gould and Eldredge\'s prediction that most morphological change occurs in brief bursts between long periods of stasis',
                    'Sexual selection — with large dinosaurs gone, mammals could now safely display elaborate ornaments and compete openly for mates, driving rapid diversification through runaway selection on secondary sexual traits',
                    'Genetic drift — mammal populations were so small during the Mesozoic that allele frequencies fluctuated randomly; after the K-T event, founder effects repeatedly established new populations with distinct phenotypes',
                ],
            },
            {
                'question': 'Flowering plants (angiosperms) arose ~132 Mya in the Cretaceous and triggered massive insect diversification through coevolution. Why would the evolution of flowers specifically drive insect diversity rather than just insect abundance?',
                'correct': 'Flowers are diverse in color, scent, shape, timing, and reward type — different plant species specialize on different pollinator guilds, creating strong directional selection for insects to specialize on particular flower types, driving divergence and speciation in pollinator lineages',
                'distractors': [
                    'Flowers produce nectar, which is a higher-calorie food than the bark and leaf material available in the Jurassic — greater caloric density supported larger insect populations, and large populations accumulate more mutations, driving faster speciation',
                    'Angiosperms replaced gymnosperms as the dominant plants, and gymnosperms hosted specialized insect communities — the extinction of gymnosperms forced insect lineages to rapidly adapt to the new angiosperm hosts, causing bottleneck effects and founder speciation',
                    'Insect diversification drove flower diversity rather than the reverse — as insects specialized on feeding from different plant tissues, plants evolved floral structures to exploit these pre-adapted insect visitors as cheap pollinators',
                ],
            },
            {
                'question': 'Archaeopteryx (~150 Mya, Late Jurassic) famously combines features of theropod dinosaurs and modern birds (teeth, long bony tail, claws on wings, but also flight feathers and a wishbone). Why is Archaeopteryx considered a transitional fossil in the strict sense, not merely an "old bird"?',
                'correct': 'It preserves a specific combination of ancestral dinosaurian features (teeth, long bony tail, clawed fingers) alongside derived avian features (asymmetric flight feathers, wishbone), documenting an actual intermediate morphological stage between theropods and birds — not simply an early representative of one group',
                'distractors': [
                    'Archaeopteryx is considered transitional because it is the oldest known bird fossil — any fossil that predates all others of its group is by definition transitional, regardless of its actual morphology',
                    'Archaeopteryx is transitional because its feathers contain both scales and true feathers fused together, proving that feathers evolved directly from reptile scales through a single-step mutation',
                    'Archaeopteryx is transitional because it lived precisely at the K-T boundary, bridging the extinction of dinosaurs and the radiation of birds — its geological position makes it a transitional form regardless of anatomy',
                ],
            },
            {
                'question': 'The first mammals arose ~200–180 Mya in the Jurassic and remained small and nocturnal for the next ~150 million years while dinosaurs dominated. Why did mammals stay small and nocturnal rather than diversifying into large body sizes during the Mesozoic?',
                'correct': 'Large and diurnal niches were already occupied by dinosaurs, which dominated competition for resources during daylight and at larger body sizes — mammals were confined to small, nocturnal, often burrowing lifestyles where they could avoid direct competition, and only radiated after the K-T extinction freed those niches',
                'distractors': [
                    'Early mammals were physiologically incapable of growing larger than ~200 g because their metabolism had not yet evolved efficient ATP production — the mitochondrial machinery required for large-body metabolism only arose in the early Cenozoic after the K-T event',
                    'Mammals stayed small because they had not yet evolved placentas — until placental development arose in the late Cretaceous, all mammals were limited to egg-laying and could not support larger offspring or larger body sizes',
                    'Early mammals deliberately chose to avoid dinosaurs by retreating to the margins of ecosystems — this behavioral choice was passed down through learning rather than inheritance and was lost after the K-T event',
                ],
            },
            {
                'question': 'The earliest known Homo sapiens fossils date to ~195,000 years ago. Primates first appeared ~50 Mya as small squirrel-sized arboreal forms, and hominins (bipedal primates) arose ~7 Mya. What does this timeline illustrate about the pace of human evolution relative to the broader sweep of animal history?',
                'correct': 'The entire Homo sapiens history represents an extraordinarily thin sliver of geological time — from the first primates (50 Mya) to hominins (7 Mya) to our species (0.2 Mya), the timeline compresses exponentially; our species\' total existence is less than 0.5% of the time mammals have existed, emphasizing that humans are a recent twig on a very old tree',
                'distractors': [
                    'The timeline shows that human evolution accelerates over time — primates took 43 million years to produce hominins, but hominins took only 7 million years to produce Homo sapiens, proving that evolution runs faster in lineages that are closer to humans',
                    'The timeline shows that Homo sapiens appeared unusually early relative to other mammal species — most mammal lineages took tens of millions of years to diversify, but humans appeared only ~200,000 years after the first hominins, demonstrating special creation rather than gradual evolution',
                    'The pace of human evolution was directly driven by dinosaur extinction at 65 Mya — the removal of dinosaurs immediately allowed primates to evolve, and human ancestors appeared within 15 million years of the K-T event',
                ],
            },
            {
                'question': 'The letter "K" in "K-T boundary" stands for the German word "Kreide" (meaning chalk), referring to the chalky Cretaceous deposits that give the period its name. Given that the boundary is now often called the K-Pg boundary, what does "Pg" represent and why was the renaming considered an improvement?',
                'correct': 'Pg stands for Paleogene, the first period of the Cenozoic era; the renaming from K-T (Cretaceous-Tertiary) to K-Pg better reflects modern stratigraphic nomenclature because "Tertiary" has been abandoned as a formal geologic period and replaced with the Paleogene and Neogene subdivisions',
                'distractors': [
                    'Pg stands for "Post-geological" referring to the ages after the major dinosaur extinction; the renaming reflects that geological processes slowed dramatically after the Cretaceous ended, marking a new phase of planetary stability',
                    'Pg stands for "Precambrian geological" boundary, and the rename was made to acknowledge that the asteroid impact effects extended all the way back to Precambrian rocks through subsurface fracturing',
                    'Pg stands for "Primate genesis," recognizing that the first primates appeared immediately after the K-Pg boundary; the renaming was driven by primatologists who wanted to emphasize this milestone in mammalian evolution',
                ],
            },
            {
                'question': 'The K-T extinction selectively wiped out ~2/3 of species, with large-bodied animals and photosynthesis-dependent lineages hit hardest. Birds, small mammals, small reptiles, and many invertebrates survived. What single feature best explains this selectivity?',
                'correct': 'The asteroid impact ejected debris that blocked sunlight for months to years, collapsing primary productivity — large animals with high absolute food requirements starved quickly, while small-bodied survivors that could subsist on seeds, detritus, insects, or carrion persisted through the dark period until photosynthesis recovered',
                'distractors': [
                    'The asteroid\'s iridium was selectively toxic to large-bodied vertebrates because they absorbed more of it per unit surface area — small animals were spared because their thinner skin allowed iridium to pass through without accumulating in tissues',
                    'Large-bodied animals required warmer climates to regulate body temperature and could not survive the brief post-impact cooling, while small animals were automatically tolerant of cold temperatures due to their higher surface-to-volume ratios',
                    'The selective survival was random — with such a severe extinction, which lineages survived was determined entirely by chance, and there is no biological pattern to explain which groups persisted and which perished',
                ],
            },
            {
                'question': 'The K-T asteroid is estimated to have been ~10 miles (16 km) in diameter and released energy equivalent to ~100 trillion tons of TNT. Why is it significant that the impact site at Chicxulub (Yucatán Peninsula) was in shallow sulfate-rich carbonate rock rather than open ocean or granite continental crust?',
                'correct': 'The carbonate and sulfate rock released enormous quantities of CO2 and sulfur aerosols upon vaporization, producing a one-two punch of short-term global cooling (sulfur aerosols blocking sunlight) followed by long-term warming (CO2 greenhouse effect) — the specific rock chemistry at Chicxulub amplified the climate catastrophe beyond what the impact energy alone would have caused',
                'distractors': [
                    'The shallow water at Chicxulub caused massive tsunamis that were the primary kill mechanism of the K-T event — without the coastal impact location, the asteroid would have mostly caused local damage without triggering global extinction',
                    'The Yucatán rock was unusually iridium-rich, so most of the worldwide iridium layer actually came from vaporized target rock rather than from the asteroid itself — this invalidates the use of iridium as evidence for the impact',
                    'The shallow carbonate rocks absorbed most of the impact energy, actually reducing the global climate effects relative to what would have happened if the asteroid had struck continental crust — the extinction could have been much worse',
                ],
            },
        ],
        visual={
            'type': 'event',
            'description': 'K-T extinction mechanism',
            'regions': [
                {'label': 'Impact', 'color': '#e63946', 'items': ['~10 mi asteroid', 'Chicxulub crater', '100 T tons TNT']},
                {'label': 'Global effects', 'color': '#f77f00', 'items': ['Iridium layer', 'Wildfires', 'Cooling/darkness']},
                {'label': 'Extinction', 'color': '#6e6a80', 'items': ['Non-avian dinos', '2/3 of species', 'Large bodies first']},
                {'label': 'Cenozoic radiation', 'color': '#7de2d1', 'items': ['Mammals expand', 'Primates emerge', 'Us, eventually']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Asteroid → iridium → climate collapse → mammalian radiation.',
            'trap': 'The K-T event is only one of 5 MAJOR mass extinctions. The biggest was the end-Permian (~251 Mya), wiping ~96% of marine species. We may be entering a 6th (anthropogenic).',
        },
    diagram=mesozoic_kt_timeline_diagram(),
    ))

    return nodes


# --------------------------------------------------------------------------
# April 6 recording segments (Lec 15 - Phylogenetics)
# The 45,182-char transcript was split into 5 ~9k parts.
# --------------------------------------------------------------------------

# Segment A: phylogeny intro, tree components, snail island example
# (covers slides 1-12)
APR6_TREE_THINKING = APR6[0:12000]

# Segment B: synapomorphy, monophyletic vs paraphyletic, birds-as-reptiles
# (covers slides 13-22)
APR6_CLADISTICS = APR6[12000:22000]

# Segment C: parsimony, homoplasy, convergence, reversals, mammal/whale
# (covers slides 23-29)
APR6_HOMOPLASY = APR6[22000:30000]

# Segment D: fins-to-limbs, Coelacanth, Tiktaalik, Shubin prediction
# (covers slides 30-37)
APR6_FINS_LIMBS = APR6[30000:37000]

# Segment E: feathers, Archaeopteryx, velociraptor quill nodes, exaptation
# (covers slides 38-44)
APR6_FEATHERS = APR6[37000:]


def lec15_nodes():
    d = load_lec('lec15')
    nodes = []

    # ---- Node 1: Tree Thinking & Tree Components (slides 1-12) ----
    sections = slides_to_sections(d, (1, 12))
    sections.append(audio_section(
        'Tree thinking, snail island example (recorded 2026-04-06)',
        APR6_TREE_THINKING,
    ))
    nodes.append(build_node(
        id='lec15-tree-thinking',
        title='Tree Thinking: Phylogeny Basics',
        subtitle='Tips, nodes, clades, root (Lec 15 slides 1-12)',
        color='teal', row=13,
        heading='Lecture 15 — Phylogenetics: Reading Evolutionary Trees',
        sections=sections,
        examples=[
            'Tip: terminal ends of a tree — species, populations, or molecules being compared.',
            'Branch: lineage evolving through time between divergence events (speciation).',
            'Node: point where a lineage splits. Internal nodes = inferred common ancestors.',
            'Root: ancestor from which all other nodes descend. Usually chosen with an outgroup.',
            'Clade: an ancestor plus ALL of its descendants. A monophyletic group.',
            'Sister taxa: two lineages that share one immediate common ancestor (one node apart).',
            'Snail island example: populations can evolve in place (in situ) OR move to new islands. Current island 1 snails are NOT the direct ancestors of island 3 & 4 snails — evolution did not stop.',
        ],
        warnings=[
            'Trees can be drawn in MANY visual styles without changing the phylogeny. Rotations at any node are free — the topology is what matters.',
            'NEVER read trees left-to-right as "progress." Humans are NOT at the "tip" of evolution — every living species is equally "evolved."',
            'Tree orientation (horizontal, vertical, radial, circular) is a display choice, not a biological statement.',
        ],
        mnemonic='Tip, Branch, Node, Root, Clade — the five words that describe any tree.',
        flashcard={
            'front': 'Why is reading a phylogenetic tree left-to-right as "progress toward humans" (or any tip) a fundamental misconception?',
            'back': 'Phylogenetic trees show BRANCHING patterns of descent, not linear progress. Every species at the tips is equally "evolved" — they have all been evolving for the same amount of time since their last common ancestor. A tree can be rotated at ANY node without changing its biological meaning, which proves that the left-to-right order of tips has no biological significance. The "ladder of progress" or "scala naturae" view — where amoebae are "primitive" and humans are "advanced" — was explicitly rejected by Darwin, who famously wrote "never use the words higher and lower" in the margin of an early manuscript. Modern tree thinking requires reading from ROOT to TIPS, following actual ancestry, not left-to-right along the tips.',
        },
        quiz=[
            {
                'question': 'In a phylogenetic tree, what does a "node" represent?',
                'correct': 'A point where a lineage splits (a common ancestor and a speciation event)',
                'distractors': [
                    'A living species',
                    'A fossil specimen',
                    'The root of the entire tree',
                ],
            },
            {
                'question': 'A tree can be rotated at any internal node without changing its biological meaning. What key principle does this demonstrate about how to read phylogenies?',
                'correct': 'The left-to-right order of tips is biologically meaningless — only the topology (branching pattern showing which lineages share a more recent common ancestor) carries evolutionary information',
                'distractors': [
                    'Trees can be rotated because all species are equally related to one another, so any arrangement of tips is biologically equivalent to any other',
                    'Trees can be rotated because evolution has no directionality — lineages evolve backward and forward freely, so the root and tips can be switched without changing the tree\'s meaning',
                    'Tree rotations are only permissible for unresolved polytomies (nodes with three or more descendants) — fully bifurcating trees have a fixed orientation that reflects true evolutionary sequence',
                ],
            },
            {
                'question': 'In the snail island example from lecture, current snails on island 1 are NOT the direct ancestors of snails on islands 3 and 4. Why is this the correct interpretation?',
                'correct': 'Evolution is ongoing in ALL lineages simultaneously — the island 1 snails have continued evolving since the ancestor colonized islands 3 and 4; reading living organisms as "ancestral" to other living organisms mistakes tips of the tree for internal nodes',
                'distractors': [
                    'Island 1 snails are not ancestral because they went extinct and were replaced by a different snail population before the colonization of islands 3 and 4 — the true ancestor is therefore unknown',
                    'Island 1 snails are not ancestral because geographic isolation means each island population is a completely independent evolutionary experiment with no shared history after initial colonization',
                    'Islands 3 and 4 were colonized directly from the mainland, not from island 1 — the island 1 population arose from a separate colonization event unrelated to the origin of the islands 3 and 4 populations',
                ],
            },
            {
                'question': 'You are given a phylogenetic tree with humans at the far right tip and bacteria at the far left tip. A student concludes that bacteria are "less evolved" than humans because they appear earlier on the left side. What two errors is this student making?',
                'correct': 'First, tree orientation is arbitrary — rotating the tree places bacteria at the right with no biological change. Second, all tips represent organisms that have been evolving for the same elapsed time since the root — bacteria are highly adapted to their environments and are not "less evolved" in any meaningful sense',
                'distractors': [
                    'The student is correct that bacteria are less evolved, because they have not undergone the multicellular transition that represents a key increase in biological complexity — simpler organization is objective evidence of lower evolutionary advancement',
                    'The error is solely visual — the student should read the tree from tips inward to the root instead of from root outward to tips, which would reveal that bacteria are actually descended from humans in this tree\'s topology',
                    'The student is making only one error: confusing the left-right position with ancestry — the correct reading is that bacteria and humans shared a common ancestor at the root node, making them sister taxa rather than ancestor and descendant',
                ],
            },
            {
                'question': 'On a phylogenetic tree, two tips that share one IMMEDIATE common ancestor (separated by a single internal node) are called sister taxa. Why is the sister-taxa relationship important for comparative biology?',
                'correct': 'Sister taxa share more recent common ancestry with each other than with any other taxa on the tree — comparative tests of adaptation and trait evolution rely on contrasting sister taxa, where differences between them are most likely to reflect evolutionary change rather than ancient inherited similarity',
                'distractors': [
                    'Sister taxa are always morphologically identical, since they share an immediate common ancestor; any trait differences between them are evidence of convergent evolution rather than shared ancestry',
                    'Sister taxa are always the same species by definition — the term applies only to populations within a single species, not to relationships between different species on a tree',
                    'Sister taxa must have identical genetic sequences because they share the most recent common ancestor; any DNA differences between them indicate contamination or sequencing error',
                ],
            },
            {
                'question': 'The ROOT of a phylogenetic tree represents the common ancestor of all taxa on that tree. How is the root typically determined when constructing a tree?',
                'correct': 'An OUTGROUP — a taxon known to be less closely related to all ingroup taxa than they are to each other — is added to the analysis; the point where the outgroup attaches to the ingroup is the root, because the outgroup is by definition outside the group being resolved',
                'distractors': [
                    'The root is placed at the oldest fossil in the analysis — because older fossils are ancestral by default, the earliest-known taxon in the data set is always assumed to be the root of the tree',
                    'The root is determined by calculating which taxon has the fewest derived characters — a species with only ancestral traits is by definition the root because it has undergone the least evolutionary change',
                    'The root is placed arbitrarily at the center of the tree for visual balance — in modern cladistics, trees are drawn as unrooted networks and the notion of a root has no biological meaning',
                ],
            },
            {
                'question': 'A CLADE is defined as an ancestor plus ALL of its descendants (a monophyletic group). A tree can show many nested clades at different levels. Why does this nesting structure matter for classification?',
                'correct': 'Clades are nested inside one another like Russian dolls, so a single organism belongs simultaneously to many clades at different levels of inclusiveness (e.g., a human belongs to Mammalia, Tetrapoda, Vertebrata, Eukaryota, etc.) — classification should mirror this nested structure to accurately reflect evolutionary history',
                'distractors': [
                    'Clade nesting ensures that every organism belongs to exactly one clade — the largest inclusive clade is always chosen as the organism\'s "true" category, and all smaller clades within it are treated as subdivisions without classification significance',
                    'Clade nesting reflects the chronological order in which organisms evolved — outer clades formed earlier and inner clades formed later, so the position of an organism in the nesting tells you how "old" its lineage is',
                    'Clade nesting means the number of clades an organism belongs to is a measure of its evolutionary complexity — humans belong to more clades than bacteria because humans are more complex',
                ],
            },
            {
                'question': 'Darwin sketched the first known evolutionary tree in his 1837 notebook (labeled "I think") showing divergent descent with a branching pattern. Why was the concept of a branching tree (rather than a linear "Great Chain of Being") fundamentally radical for Darwin\'s time?',
                'correct': 'Pre-Darwinian biology inherited the medieval Great Chain of Being, which ordered life from simple to complex along a single ladder with humans at the top — Darwin\'s tree replaced this with a branching structure where all species are tips, no species is "higher" than another, and humans are simply one twig among millions rather than the apex of creation',
                'distractors': [
                    'Darwin\'s tree was radical because it was the first attempt to classify species by morphology — before Darwin, species were catalogued alphabetically or by color, with no attempt to group similar forms together into taxonomic hierarchies',
                    'The branching tree was radical because it required scientists to accept that all species were created simultaneously at the base of the tree, contradicting the biblical account that species were created in stages over six days',
                    'Darwin\'s tree was radical because it predicted that extinct species would outnumber living species, which no naturalist before him had anticipated — this prediction was confirmed by the fossil record',
                ],
            },
            {
                'question': 'In the snail island example, the professor notes that islands 3 and 4 hold populations that are MORE closely related to each other than either is to island 1\'s current snails. What does this tell us about how to count node distances on a tree?',
                'correct': 'Two taxa are more closely related when the number of nodes separating them (along the tree topology) is smaller — islands 3 and 4 share a more recent common ancestor (fewer nodes) than either does with island 1, so the phylogenetic distance is counted by traversing nodes back to the most recent common ancestor and forward again, not by comparing geographic proximity',
                'distractors': [
                    'Phylogenetic relatedness is measured by geographic distance — because islands 3 and 4 are closer together physically, their snails are automatically more closely related than they are to island 1 regardless of the tree topology',
                    'Relatedness is measured by how similar the taxa look — islands 3 and 4 snails have similar pink shells (vs high-spire on island 1), so they are automatically more related based on appearance alone',
                    'Relatedness between taxa is measured by adding the branch lengths from root to tip — the taxa with the longest total branch length back to the root are always the most closely related',
                ],
            },
            {
                'question': 'A student looks at a phylogeny and identifies humans and chimpanzees as sister taxa because the internal node immediately uniting them has no other branches. Why is this a correct application of the sister taxa concept and what experimental comparison would it enable?',
                'correct': 'Sister taxa share a most recent common ancestor with no other branches interposed — since humans and chimps share such a node, they qualify as sister taxa, and any trait difference between them (e.g., bipedalism, brain size) is the most statistically clean contrast for inferring what changed along the human lineage versus the chimp lineage since divergence',
                'distractors': [
                    'Humans and chimps cannot be sister taxa because gorillas and orangutans are on nearby branches — the sister-taxa relationship requires complete geographic and temporal isolation from all other closely related species, which is not true of great apes',
                    'The sister-taxa label is only applicable to taxa that look similar — since humans and chimps differ dramatically in bipedalism and brain size, they are better described as cousins rather than sister taxa regardless of the tree topology',
                    'Humans and chimps are not sister taxa because they can interbreed in theory — sister taxa must be reproductively isolated for millions of years before the label can be applied, and humans and chimps diverged too recently',
                ],
            },
        ],
        visual={
            'type': 'anatomy',
            'description': 'Parts of a phylogenetic tree',
            'regions': [
                {'label': 'Root', 'color': '#6e6a80', 'items': ['Common ancestor of everything shown']},
                {'label': 'Branch', 'color': '#4ea8de', 'items': ['Lineage through time']},
                {'label': 'Node', 'color': '#ffc857', 'items': ['Speciation', 'Common ancestor']},
                {'label': 'Tip', 'color': '#7de2d1', 'items': ['Species/population', 'Today']},
                {'label': 'Clade', 'color': '#8a5cf6', 'items': ['Ancestor + ALL descendants', 'Monophyletic']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Root → Branches → Nodes → Tips.',
            'trap': 'A "clade" must include ALL descendants. If you exclude some descendants (e.g., "reptiles minus birds"), it is PARAPHYLETIC — not a valid clade.',
        },
    diagram=tree_thinking_components_diagram(),
    ))

    # ---- Node 2: Cladistics & Synapomorphies (slides 13-22) ----
    sections = slides_to_sections(d, (13, 22))
    sections.append(audio_section(
        'Synapomorphy, mono- vs paraphyletic, character tables (recorded 2026-04-06)',
        APR6_CLADISTICS,
    ))
    nodes.append(build_node(
        id='lec15-cladistics-synapomorphy',
        title='Cladistics, Synapomorphies & Monophyletic Groups',
        subtitle='Shared derived characters build valid clades (Lec 15 slides 13-22)',
        color='blue', row=13,
        heading='Lecture 15 — Cladistics: Building Trees from Characters',
        sections=sections,
        examples=[
            'Systematics: the scientific field of classification.',
            'Synapomorphy: a shared derived character — inherited from a common ancestor by all descendants. The KEY tool for building clades.',
            'Ancestral characters (symplesiomorphies) are NOT informative for defining relationships within a group because EVERY member has them.',
            'Monophyletic group: an ancestor + ALL of its descendants. A valid clade.',
            'Paraphyletic group: an ancestor + SOME descendants. NOT a valid clade.',
            'Classic example: "reptiles" (excluding birds) is PARAPHYLETIC. To make it monophyletic, you must INCLUDE birds as reptiles — which is what modern taxonomy does (Aves is a lineage within Sauropsida).',
            'Character matrix: rows = taxa, columns = characters (wings, antennae, elytra, mandibles). Identical rows group together, with an outgroup to root the tree.',
            'With 5 taxa, there are 105 possible tree topologies. With 9 taxa, 2 million. With more, it becomes astronomical — requiring computers.',
        ],
        warnings=[
            '"Fish" as commonly used is paraphyletic — it excludes tetrapods (which descend from lobe-finned fish). A monophyletic "fish" group would include us.',
            'Morphological characters can mislead if based on ancestral features. Always use DERIVED characters for clade-building.',
            'Synapomorphy / homology / homoplasy — keep these terms straight. Homology = same due to common ancestry. Homoplasy = same NOT due to common ancestry.',
        ],
        mnemonic='Synapomorphy = Shared + Derived. Ancestral doesn\'t count, derived does.',
        flashcard={
            'front': 'Explain why "reptiles" (excluding birds) is a paraphyletic group, and how this violates cladistic principles.',
            'back': 'A MONOPHYLETIC group (clade) must include a common ancestor AND ALL of its descendants. "Reptiles" as traditionally defined (lizards, snakes, crocodiles, turtles, tuataras — but not birds) is PARAPHYLETIC because birds ARE direct descendants of the same reptilian ancestor that gave rise to crocodiles and dinosaurs. Phylogenetically, crocodiles are MORE closely related to birds than to lizards. To make "reptiles" monophyletic, birds MUST be included — hence modern taxonomy calls birds "avian reptiles" and places Aves within the clade Sauropsida/Archosauria. This is why cladists emphasize: definitions must reflect ACTUAL ancestry, not superficial similarity or traditional categories. "Fish" has the same problem — it excludes tetrapods, but tetrapods are descended from lobe-finned fish.',
        },
        quiz=[
            {
                'question': 'Why is "reptiles" (excluding birds) considered a paraphyletic group?',
                'correct': 'It excludes birds, which are direct descendants of the reptilian common ancestor',
                'distractors': [
                    'Reptiles and birds evolved independently',
                    'Reptiles are a monophyletic group by definition',
                    'Birds diverged from mammals, not reptiles',
                ],
            },
            {
                'question': 'A synapomorphy is a SHARED DERIVED character used to build a clade. Why are ancestral characters (symplesiomorphies) useless for defining relationships WITHIN a group?',
                'correct': 'Ancestral characters are present in ALL members of the group and in their outgroup relatives too — they tell you nothing about which members are more closely related to each other because they predate the divergences you are trying to resolve',
                'distractors': [
                    'Ancestral characters are useless because they evolve too rapidly — by the time you sample organisms, ancestral characters have mutated into derived forms in most lineages, making them unreliable markers',
                    'Ancestral characters cannot be identified without a time machine — without knowing which state existed in the ancestor, you cannot distinguish ancestral from derived, so neither type of character can be used in cladistics',
                    'Ancestral characters define the outgroup rather than the ingroup — by convention, cladists use only outgroup characters to root the tree, while all ingroup characters are automatically classified as derived',
                ],
            },
            {
                'question': 'With 5 taxa there are 105 possible tree topologies; with 9 taxa there are ~2 million. Why does this combinatorial explosion require computer algorithms rather than manual inspection?',
                'correct': 'The number of possible trees grows faster than exponentially with each added taxon — manually evaluating parsimony scores for millions of tree topologies is computationally impossible; algorithms like maximum parsimony, maximum likelihood, and Bayesian inference use heuristics to search the tree space efficiently',
                'distractors': [
                    'Computer algorithms are needed not for tree searching but for reading the very large character matrices required — with 9 taxa and 50 characters, the character table has 450 cells that would take months to enter manually',
                    'The combinatorial explosion is only a problem for morphological data — molecular data has a fixed number of base-pair positions that can be analyzed with simple manual alignment even for dozens of taxa',
                    'The explosion in topologies reflects the fact that more taxa always produce more accurate phylogenies — computers are needed to store and display the final result, not to evaluate competing topologies during tree building',
                ],
            },
            {
                'question': 'Crocodiles are more closely related to birds than to lizards, yet traditional taxonomy grouped crocodiles with lizards as "reptiles." What does this show about the relationship between traditional Linnaean taxonomy and cladistic classification?',
                'correct': 'Traditional Linnaean taxonomy was based on overall similarity and grades of organization rather than strict common ancestry — it often produced paraphyletic groupings that cladistics has revised because cladistics requires all groups to be monophyletic (ancestor plus ALL descendants)',
                'distractors': [
                    'Traditional taxonomy was correct — crocodiles and lizards share more derived characters than crocodiles and birds do, so grouping crocodiles with lizards accurately reflects the most recent common ancestry even under cladistic rules',
                    'The Linnaean hierarchy and cladistics are equivalent systems — any group recognized by traditional taxonomy is automatically monophyletic, and the crocodile/bird relationship is simply a naming convention dispute rather than a substantive biological disagreement',
                    'Cladistics and Linnaean taxonomy agree on the classification of most groups; the crocodile/bird relationship is an anomaly arising because molecular data was not available to Linnaeus — once molecular phylogenies are complete, most traditional groupings will be restored',
                ],
            },
            {
                'question': 'A POLYPHYLETIC group (like "warm-blooded vertebrates," which would lump mammals and birds together while excluding their common ancestor) is considered invalid in cladistics. How does a polyphyletic group differ from a paraphyletic group?',
                'correct': 'A paraphyletic group includes a common ancestor but EXCLUDES some descendants (e.g., reptiles excluding birds); a polyphyletic group EXCLUDES the common ancestor and lumps taxa together on the basis of convergent features rather than shared ancestry (e.g., endothermic mammals + birds without including their common amniote ancestor)',
                'distractors': [
                    'A paraphyletic group is monophyletic under molecular phylogeny but paraphyletic under morphological phylogeny; a polyphyletic group is paraphyletic under both types of analysis, making polyphyly the more severe classification error',
                    'A paraphyletic group is smaller than a polyphyletic group — paraphyly includes fewer taxa than required, while polyphyly includes too many taxa; both errors are quantitative deviations from the correct monophyletic group size',
                    'Paraphyletic and polyphyletic groups are synonymous terms referring to the same type of invalid grouping — the distinction is purely historical and has no biological significance in modern cladistics',
                ],
            },
            {
                'question': 'When building a phylogeny with a character matrix (rows = taxa, columns = characters), an OUTGROUP is added that is known to be less closely related to all ingroup taxa than they are to each other. What is the specific role of the outgroup in tree construction?',
                'correct': 'The outgroup establishes which character states are ANCESTRAL vs DERIVED for the ingroup — any character state shared by the outgroup AND some ingroup members is probably the ancestral state, while states found only within the ingroup are derived (and thus useful synapomorphies for building clades)',
                'distractors': [
                    'The outgroup is used as a statistical control for tree-building software — its presence allows algorithms to calculate branch support values and bootstrap percentages, but has no effect on the topology of the ingroup tree',
                    'The outgroup serves as a hypothetical ancestor of the ingroup whose character states are assumed to be entirely derived; if the outgroup shares a character with any ingroup member, that character is automatically excluded from the analysis',
                    'The outgroup is used to verify that all ingroup taxa are closely related enough to form a monophyletic group — if any ingroup taxon is more similar to the outgroup than to other ingroup members, it is removed from the analysis',
                ],
            },
            {
                'question': '"Fish" as commonly used is a paraphyletic group because it excludes tetrapods, which descend from lobe-finned fish. What is the cladistically correct way to refer to "fish"?',
                'correct': 'There is no valid cladistic term for "fish" as traditionally conceived — any monophyletic group containing all "fish" must also contain all tetrapods (including humans), so biologists often use informal phrases like "non-tetrapod vertebrates" when they need to refer to the paraphyletic grouping, while recognizing it is not a valid clade',
                'distractors': [
                    'Cladistically, "fish" refers specifically to the clade Actinopterygii (ray-finned fish) and this is the only valid use — all other fish-like groups are named by their own clade names and not collectively called fish',
                    'The cladistic solution is to redefine "fish" to exclude sharks, which are cartilaginous and therefore not true fish — with sharks excluded, the remaining bony fish form a natural monophyletic group that can legitimately be called "fish"',
                    'Cladistics accepts the traditional paraphyletic "fish" grouping as a recognized exception to the monophyly requirement because the common usage of the term is too entrenched to change — it is listed as a special category in the Linnaean system',
                ],
            },
            {
                'question': 'A classic classroom example of polyphyly is "warm-blooded vertebrates" (endothermy), which would lump mammals and birds into a single group while excluding their common amniote ancestor. Why does this grouping fail the monophyletic test, and how do we know endothermy evolved twice?',
                'correct': 'Endothermy (warm-bloodedness) evolved independently in the mammalian lineage and in the avian (dinosaurian) lineage from a cold-blooded common amniote ancestor — mammals and birds do not share the endothermic ancestor, so grouping them on the basis of endothermy creates a polyphyletic group that excludes the actual common ancestor and lumps taxa by a convergent trait',
                'distractors': [
                    'The grouping fails because birds are not actually endothermic — they have variable body temperatures during flight and torpor, so classifying them with mammals on the basis of endothermy was a factual error rather than a phylogenetic one',
                    'The grouping fails because mammals and birds are actually sister taxa under molecular phylogeny — they do share an endothermic common ancestor, but the older taxonomists grouped them incorrectly because they thought reptiles diverged before the mammal-bird split',
                    'The grouping fails because endothermy is not a genetic trait but a behavioral one — animals can become warm-blooded through behavior, so warm-bloodedness cannot be used as a phylogenetic character under any circumstances',
                ],
            },
            {
                'question': 'Tree-building with a beetle character matrix (5 beetle taxa, characters like wings/antennae/elytra/mandibles) generates 105 possible topologies; adding more taxa creates an exponential explosion (9 taxa = ~2 million trees). What practical consequence does this have for evaluating which tree is "correct"?',
                'correct': 'Because the tree space is too large to evaluate exhaustively, algorithms must use heuristic search strategies (branch-swapping, nearest-neighbor interchange) to sample plausible trees rather than checking every possibility — and because the search is not exhaustive, the reported "most parsimonious" tree is always the best tree found, not necessarily the globally optimal tree across all possibilities',
                'distractors': [
                    'The computational explosion is not a practical problem because modern computers can evaluate all 2 million trees for 9 taxa in under a second — tree-building software exhaustively searches all possible topologies for datasets of any size',
                    'The explosion means cladistics is inherently unreliable for large datasets — whenever more than 8 taxa are analyzed, the results are random selections among many equally-parsimonious trees, and no meaningful phylogeny can be recovered',
                    'The explosion is an artifact of treating each character as independent — once characters are correctly grouped by function, the number of possible trees collapses to a manageable number that can be manually verified',
                ],
            },
            {
                'question': 'Birds are classified within Dinosauria (specifically within Theropoda) by modern cladistics. What key implication does this have for defining the clade "Dinosauria" as monophyletic?',
                'correct': 'To be monophyletic, "Dinosauria" must include ALL descendants of the common dinosaur ancestor — which means birds (Aves) must be included as a sub-clade. Traditional dinosaur definitions excluding birds were paraphyletic; modern cladistic Dinosauria explicitly contains birds, so strictly speaking dinosaurs did NOT all go extinct at the K-Pg boundary — about 10,000 dinosaur species are alive today as birds',
                'distractors': [
                    'Including birds in Dinosauria is a naming convention without biological significance — because birds are warm-blooded and dinosaurs were cold-blooded, the inclusion of birds is a cladistic formality that contradicts actual biological reality',
                    'Dinosauria can remain monophyletic while excluding birds by using the "stem-based" definition that includes only organisms MORE similar to ancestral dinosaurs than to modern birds — this preserves the traditional dinosaur grouping without violating monophyly',
                    'Birds are not actually within Dinosauria in modern cladistics — they form their own separate clade that branches off before Dinosauria, and their placement within theropods is a common student misconception',
                ],
            },
        ],
        visual={
            'type': 'classification',
            'description': 'Monophyletic vs paraphyletic vs polyphyletic',
            'regions': [
                {'label': 'Monophyletic ✓', 'color': '#7de2d1', 'items': ['Ancestor + ALL descendants', 'Valid clade']},
                {'label': 'Paraphyletic ✗', 'color': '#ffc857', 'items': ['Ancestor + SOME descendants', 'e.g., "reptiles" (no birds)']},
                {'label': 'Polyphyletic ✗', 'color': '#e63946', 'items': ['Convergent lookalikes', 'Not descended from same ancestor']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Mono = all. Para = some. Poly = random.',
            'trap': 'Linnaean groupings (Class Reptilia, etc.) were often paraphyletic. Modern cladistics has forced many revisions.',
        },
    diagram=cladistics_character_matrix_diagram(),
    ))

    # ---- Node 3: Parsimony, Homoplasy & Convergence (slides 23-29) ----
    sections = slides_to_sections(d, (23, 29))
    sections.append(audio_section(
        'Parsimony, homoplasy, reversals, convergence, whale/squamate cases (recorded 2026-04-06)',
        APR6_HOMOPLASY,
    ))
    nodes.append(build_node(
        id='lec15-homoplasy-convergence',
        title='Parsimony, Homoplasy & Convergence',
        subtitle='When similarity LIES: reversals and convergent evolution (Lec 15 slides 23-29)',
        color='purple', row=13,
        heading='Lecture 15 — Testing Phylogenetic Hypotheses',
        sections=sections,
        examples=[
            'Principle of parsimony (Occam\'s razor): the tree requiring the FEWEST evolutionary steps is the best hypothesis (starting point).',
            'Phylogenetic trees are HYPOTHESES. New evidence can revise them — e.g., molecular data has reshuffled many morphological trees.',
            'Homoplasy: similarity NOT due to common ancestry. Two types: evolutionary reversal (return to ancestral state) and convergent evolution (independent origin of similar trait).',
            'Camera-eye convergence: vertebrate eyes and octopus eyes both have lens, retina, iris — but evolved INDEPENDENTLY (the tree shows separate origins requires fewer steps than "ancestral loss by all other groups").',
            'Mammal aquatic reversal: whales, dolphins, and dugongs are mammals that returned to water. Their closest living relatives are hippopotamuses (molecular and fossil evidence).',
            'Shark vs killer whale body shape: convergent, not related. Similar selective pressure (fast swimming) → similar form.',
            'Limblessness in squamates: EVOLVED INDEPENDENTLY in snakes, glass lizards, legless skinks, amphisbaenians. Some snakes still retain vestigial hind-limb spurs (boas, pythons).',
        ],
        warnings=[
            'Parsimony is a starting assumption, NOT a guarantee. Real evolution can take non-parsimonious routes (e.g., when selection pressure is strong or ancestral states are truly rare).',
            'Homoplasy is RAMPANT. Do not mistake convergent similarity for homology. Always test with independent character sets (morphology + molecules).',
            'Molecular data has overturned many morphology-based groupings. When molecular and morphological trees conflict, molecular trees are usually (but not always) more reliable.',
        ],
        mnemonic='Parsimony = fewest steps. Homoplasy = similarity that LIES (reversal or convergence).',
        flashcard={
            'front': 'How does the camera eye of vertebrates and octopuses illustrate both parsimony and convergent evolution?',
            'back': 'Both vertebrates and octopuses have complex camera eyes with a lens, retina, iris, and focusing mechanism. If camera eyes were HOMOLOGOUS (inherited from a common ancestor), then the common ancestor of vertebrates and cephalopods (~600 Mya) must have had a camera eye — and EVERY other lineage descending from that ancestor (arthropods, echinoderms, flatworms, annelids, etc.) must have LOST it. That would require many evolutionary steps. Under the CONVERGENT hypothesis, the camera eye evolved TWICE — once in the vertebrate lineage, once in the cephalopod lineage — requiring only 2 steps. Parsimony favors the convergent interpretation. Additionally, cephalopod eyes have their photoreceptors facing the light (better design), while vertebrate eyes have them facing backward (creating the blind spot) — strong evidence of independent origin through different evolutionary paths.',
        },
        quiz=[
            {
                'question': 'The principle of parsimony in phylogenetics states that:',
                'correct': 'The best hypothesis requires the fewest evolutionary steps',
                'distractors': [
                    'The simplest organism is the ancestor',
                    'Evolution always takes the shortest path',
                    'Older lineages have fewer mutations',
                ],
            },
            {
                'question': 'Snakes, glass lizards, legless skinks, and amphisbaenians have all independently evolved limblessness. Some boas and pythons still have vestigial hind-limb spurs. How do these vestigial structures help classify limblessness as homoplasy (convergence/reversal) rather than homology?',
                'correct': 'The vestigial spurs prove that the common ancestor of snakes had limbs — limblessness in snakes evolved independently AFTER that ancestor diverged from limbed relatives, rather than being inherited from a shared limbless ancestor common to all limbless squamate groups',
                'distractors': [
                    'Vestigial spurs indicate that snakes are in the process of re-evolving limbs through Lamarckian inheritance — the repeated use of substrate contact is causing the vestigial limb buds to grow again over evolutionary time',
                    'Vestigial spurs actually support homology of limblessness — they are the shared derived character (synapomorphy) that unites all limbless squamates in a single clade, and vestigial expression is the ancestral state for the group',
                    'Vestigial hind-limb spurs in boas and pythons are functionless neutral traits that have no bearing on phylogenetic classification — they are neither evidence for nor against homoplasy in limbless squamates',
                ],
            },
            {
                'question': 'Whales and dolphins are most closely related to hippopotamuses (both molecular data and Pakicetus/Ambulocetus fossil data confirm this). Why was this relationship initially surprising to morphologists?',
                'correct': 'Cetaceans are fully aquatic with flipper-like forelimbs and no hindlimbs, while hippos are large semi-aquatic ungulates with limbs — morphological convergence with fish obscured the true mammalian ancestry, and the homoplasy of aquatic body form misled morphologists who relied on overall similarity',
                'distractors': [
                    'Morphologists were surprised because molecular data consistently disagrees with fossil data — Pakicetus fossils place cetaceans with mesonychids, not hippos, so molecular and morphological phylogenies give completely contradictory results',
                    'Morphologists initially grouped whales with fish based on the principle that organisms sharing the same habitat must share a common ancestor — aquatic adaptation was mistakenly treated as a synapomorphy linking fish and cetaceans',
                    'Hippos and cetaceans were always grouped together by traditional taxonomy based on their shared semi-aquatic lifestyle — molecular data confirmed what morphologists already knew, rather than overturning a morphological classification',
                ],
            },
            {
                'question': 'Molecular data has overturned many morphologically-based phylogenetic groupings. When molecular and morphological trees conflict, molecular trees are usually (but not always) more reliable. What is the main reason molecular data is generally preferred?',
                'correct': 'Molecular characters (DNA base pairs) are vastly more numerous and evolve more independently than morphological characters — convergent evolution can produce identical morphological traits through many different genetic pathways, but identical DNA sequences across long stretches of genome are extremely unlikely without shared common ancestry',
                'distractors': [
                    'Morphological characters are subjective and based on researcher interpretation, whereas molecular data is purely objective numbers from sequencing machines — objective data is always more reliable than subjective observation regardless of the question',
                    'Molecular data is more reliable because DNA evolves at a constant rate (the molecular clock), whereas morphological change rates vary enormously — using a constant-rate process always gives more accurate phylogenetic estimates than a variable-rate process',
                    'Morphological phylogenies are only unreliable for extinct organisms because we have incomplete fossil specimens — for living organisms with fully known morphology, morphological and molecular trees give identical results and either can be used',
                ],
            },
            {
                'question': 'An EVOLUTIONARY REVERSAL is when a lineage loses a derived character and returns to the ancestral state. Why are reversals a subtype of homoplasy rather than true homology, even though the ancestral state is shared by both ancestors and the reverted descendant?',
                'correct': 'Homology requires that a trait be inherited CONTINUOUSLY from a common ancestor — in a reversal, the derived state evolved, was lost, and the ancestral state was re-expressed through independent developmental pathways; the re-expressed trait is not continuously inherited, so it is homoplastic even though it looks identical to the ancestral form',
                'distractors': [
                    'Reversals cannot actually occur under the principle that evolution is irreversible (Dollo\'s Law), so any apparent reversal is actually a case of convergent evolution arising from a completely new genetic mechanism rather than a return to the ancestral state',
                    'Reversals are homoplasy because the "returned" state is never exactly identical to the true ancestral state — small differences always remain, so the similarity is only superficial and cannot be classified as homology',
                    'Reversals are classified as homoplasy only in morphological characters; molecular reversals (e.g., a base-pair reverting to its original nucleotide) are always classified as homology because DNA has no memory of prior states',
                ],
            },
            {
                'question': 'Vertebrate and octopus camera eyes have a different orientation of photoreceptors: vertebrate photoreceptors face AWAY from incoming light (creating the blind spot), while octopus photoreceptors face TOWARD the light. What does this internal difference contribute to the argument that the two eyes are convergent rather than homologous?',
                'correct': 'If camera eyes were homologous (inherited from a common ancestor), both groups should share the same photoreceptor orientation because they would inherit the same developmental pathway — the reversed photoreceptor orientation proves that the two camera eyes arose from different developmental pathways and are convergently similar rather than common-ancestry similar',
                'distractors': [
                    'The different photoreceptor orientations show that octopuses have better vision than vertebrates — this functional difference is irrelevant to homology determination, which depends only on gross morphology (lens, retina, iris) rather than internal cellular organization',
                    'The photoreceptor orientation difference proves the octopus eye evolved FROM the vertebrate eye via a retrograde developmental reversal — octopus eyes are therefore derived from an ancestral vertebrate-like form, demonstrating common ancestry',
                    'The difference shows that octopus and vertebrate eyes are homologous at the photoreceptor level (both have photoreceptors) but convergent at the orientation level — this partial homology is common in complex structures and does not inform the overall classification',
                ],
            },
            {
                'question': 'A researcher discovers two unrelated desert lizard species with nearly identical body shapes, coloration, and behavior. Before assuming convergent evolution, what additional test should be performed to rule out the possibility that the similarity reflects true homology from a recent common ancestor?',
                'correct': 'Independent character sets (such as molecular phylogenetics, unrelated morphological systems like skeletal features, or developmental pathways) should be tested to check whether the two species are actually closely related — if multiple independent datasets agree that they are distantly related, convergence is confirmed; if molecular data places them as sister taxa, the similarity may be homology',
                'distractors': [
                    'The researcher should check whether the two species can interbreed — if they can produce viable offspring, the similarity is homology; if they cannot, the similarity must be convergent because reproductive isolation implies independent ancestry',
                    'The researcher should dissect both species and compare their internal organs — convergent evolution only affects external features, so any similarity in internal organs proves homology regardless of the external appearance',
                    'The researcher should count the number of shared characters — if they share more than 50% of characters, the similarity is homology; if less than 50%, it is convergence, regardless of whether the characters were sampled from independent systems',
                ],
            },
            {
                'question': 'Molecular and fossil evidence both place the hippopotamus as the closest living relative of whales (Cetacea), nested within the order Cetartiodactyla. Which evolutionary conclusion follows directly from this placement?',
                'correct': 'The sleek fish-like body shape of whales (dolphins, killer whales) is convergent with sharks and other fast-swimming aquatic predators, not inherited — the mammalian ancestor of whales was a terrestrial hippo-like animal, and the aquatic body plan evolved independently after whales re-entered the water, making whale/shark similarity a textbook case of homoplasy from strong hydrodynamic selection',
                'distractors': [
                    'Hippos and whales share a common aquatic ancestor that evolved in the early Cretaceous — both lineages retain the aquatic adaptations of this ancestor, and their similarity to fish is homologous rather than convergent',
                    'Because whales share ancestry with hippos, whale body shape is homologous to hippo body shape — the apparent similarity between whale and shark body forms is actually the result of sharks being descended from whales during a Mesozoic reverse transition',
                    'The hippo-whale relationship is a molecular artifact caused by rapid gene flow between the two lineages, not a true phylogenetic relationship — on morphological grounds, whales remain more closely related to other fully aquatic mammals like dugongs and manatees',
                ],
            },
            {
                'question': 'Parsimony is often called "Occam\'s razor" applied to phylogenetics. A student argues that parsimony is a law of nature and the most parsimonious tree is always the true tree. What is wrong with this claim?',
                'correct': 'Parsimony is a methodological starting assumption based on the principle that simpler explanations should be preferred over complex ones given equal evidence — it is NOT a law of nature, and real evolution can take non-parsimonious routes under strong selection pressure or when ancestral states are truly rare. Parsimony is a default hypothesis to be tested, not a guaranteed truth',
                'distractors': [
                    'Parsimony is a law of nature for morphological characters but not molecular characters — molecular evolution requires likelihood-based methods rather than parsimony because DNA evolves at a constant rate',
                    'Parsimony is never wrong in practice — every verified phylogeny has turned out to be the most parsimonious option when all data are considered, so the student is effectively correct even if parsimony is not technically a natural law',
                    'Parsimony is outdated and has been replaced by maximum likelihood in all modern phylogenetic software — the student\'s error is citing parsimony at all, since it has not been used in serious phylogenetics for decades',
                ],
            },
            {
                'question': 'The number of independent origins of limblessness in squamates (snakes, glass lizards, legless skinks, amphisbaenians) has been mapped onto a molecular phylogeny, and each limbless lineage emerges from a distinct limbed ancestor. What is the best explanation for why this particular trait has evolved so many times in this one group?',
                'correct': 'Squamates share a common body plan (elongated trunk, reduced pectoral girdle development, plasticity of Hox gene expression) that makes the limb-loss transition evolutionarily easy — strong selection for burrowing, swimming through narrow spaces, or undulatory locomotion repeatedly drives the trait because the developmental barrier to losing limbs is lower in squamates than in most other tetrapods',
                'distractors': [
                    'Limblessness has evolved many times in squamates because snakes occasionally hybridize with other limbless reptiles and transfer the limbless allele horizontally — repeated hybridization events have distributed the limbless phenotype across multiple squamate lineages',
                    'The multiple origins are illusory — all limbless squamates actually share a single common limbless ancestor, and molecular phylogenies placing limbed taxa between them are incorrect due to long-branch attraction artifacts',
                    'Squamates are unique in having a "limbless" gene that is easily activated by environmental stress — stressful burrowing conditions trigger this gene and cause limb reduction within a single generation, which is then inherited by offspring',
                ],
            },
        ],
        visual={
            'type': 'comparison',
            'description': 'Homoplasy: reversal vs convergence',
            'regions': [
                {'label': 'Homology ✓', 'color': '#7de2d1', 'items': ['Same due to common ancestry', 'e.g., tetrapod limb bones']},
                {'label': 'Convergence (homoplasy)', 'color': '#f77f00', 'items': ['Independent origin', 'Similar pressure', 'e.g., octopus/vertebrate eye']},
                {'label': 'Reversal (homoplasy)', 'color': '#e63946', 'items': ['Derived → ancestral', 'e.g., snake limb loss']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Homology = real kinship. Homoplasy = false resemblance.',
            'trap': 'Two species sharing a trait does NOT prove common ancestry. Always test with multiple independent characters.',
        },
    diagram=mono_para_polyphyletic_compare_diagram(),
    ))

    # ---- Node 4: Fins to Limbs & Tiktaalik (slides 30-37) ----
    sections = slides_to_sections(d, (30, 37))
    sections.append(audio_section(
        'Coelacanths, Tiktaalik, Shubin prediction (recorded 2026-04-06)',
        APR6_FINS_LIMBS,
    ))
    nodes.append(build_node(
        id='lec15-fins-to-limbs',
        title='Fins to Limbs: Tiktaalik as Transitional Fossil',
        subtitle='Phylogenies generate TESTABLE predictions (Lec 15 slides 30-37)',
        color='amber', row=13,
        heading='Lecture 15 — The Vertebrate Transition to Land',
        sections=sections,
        examples=[
            'Coelacanths: lobe-finned fish thought extinct since Cretaceous — found ALIVE in 1938 off South Africa. Living fossil, close living relative of tetrapods.',
            'Lobe-finned fish have fin bones HOMOLOGOUS to tetrapod limb bones (humerus, radius/ulna). They are cousins, not ancestors, but they preserve the transitional anatomy.',
            'Phylogenies generate HYPOTHESES. Given that tetrapods arose from lobe-finned fish in the Devonian (~370 Mya), transition fossils should exist in mid-Devonian coastal wetland rocks.',
            'Neil Shubin + Ted Daeschler searched exactly those rocks in Northern Canada (Ellesmere Island).',
            'Tiktaalik (2004): transitional fossil with weight-bearing elbows, bending wrist, neck (lost bony operculum), lateral line (still aquatic), eyes on top of head (looking up).',
            'Tiktaalik could do "push-ups" — support body weight on its pectoral fins. Probably not walking on land, but could prop itself at the water surface to look around.',
            'Transitional features: from fins → arms, from no neck → neck, from gills-only → lungs + gills, from aquatic ear → terrestrial ear.',
        ],
        warnings=[
            'Tiktaalik is NOT "our ancestor" in the strict sense — it\'s a cousin preserving transitional anatomy. The direct ancestor probably existed in the same environment but has not been found as a fossil.',
            '"Missing link" is a misleading phrase — evolution doesn\'t have a single chain of links. Tiktaalik is ONE of many transitional forms (Acanthostega, Ichthyostega, Eusthenopteron all show stages).',
        ],
        mnemonic='Phylogeny → prediction → dig in the right rocks → Tiktaalik (2004). Science works.',
        flashcard={
            'front': 'How did Neil Shubin use phylogenetic reasoning to predict where transitional fish-to-tetrapod fossils would be found?',
            'back': 'Shubin and Daeschler reasoned: (1) Tetrapods (4-legged vertebrates) are closely related to lobe-finned fish based on phylogenetic analysis and existing fossil evidence. (2) The transition fish → tetrapod must have occurred during the mid-to-late DEVONIAN period (~380-360 Mya) based on the age of known early tetrapod fossils (Acanthostega, Ichthyostega). (3) The environment where this transition occurred should be COASTAL WETLANDS — shallow, warm, freshwater habitats where a transitional animal could benefit from push-up style locomotion. (4) Therefore, they needed to find mid-Devonian COASTAL WETLAND rocks that were accessible. They found exactly that in Northern Canada (Ellesmere Island, Nunavut). After multiple field seasons, in 2004 they discovered TIKTAALIK — a fish with weight-bearing elbows, bending wrist, a NECK (loss of bony operculum), and other "fishapod" features. This was a triumph of phylogenetically-guided prediction: science using theory to direct empirical discovery, rather than stumbling upon fossils by accident.',
        },
        quiz=[
            {
                'question': 'Which Tiktaalik feature most strongly suggests it could support its body weight?',
                'correct': 'Weight-bearing elbows and a bending wrist',
                'distractors': [
                    'A dorsal fin',
                    'A long tail',
                    'Scales covering its body',
                ],
            },
            {
                'question': 'Neil Shubin and Ted Daeschler searched for transitional fish-to-tetrapod fossils in Ellesmere Island (Northern Canada) specifically because of the rock type and age there. What chain of phylogenetic reasoning led them to that location?',
                'correct': 'Phylogenetic analysis placed the fish-tetrapod transition in the mid-to-late Devonian (~380-360 Mya) → the transition habitat was predicted to be shallow coastal freshwater wetlands → they needed to find mid-Devonian coastal wetland rocks → Ellesmere Island had exactly that geology accessible at the surface',
                'distractors': [
                    'Earlier paleontologists had already found fragmentary transitional fossils in that region — Shubin and Daeschler simply returned with better technology to find complete specimens, rather than using phylogenetics to select the site',
                    'The Ellesmere Island site was chosen because it was the only mid-Devonian rock formation accessible without drilling — they searched there out of logistical necessity rather than phylogenetic prediction, and the discovery was fortunate',
                    'Shubin predicted the transition occurred in deep marine environments based on oxygen isotope data from Devonian rocks — Ellesmere Island had the appropriate deep-water shale, which unexpectedly turned out to contain nearshore transitional forms',
                ],
            },
            {
                'question': 'Tiktaalik had a NECK (lost the bony operculum covering the gills) but still had a lateral line. What does this combination of features tell us about its lifestyle?',
                'correct': 'Tiktaalik was still aquatic (lateral line detects water pressure/movement — useless on land) but had begun acquiring terrestrial capabilities; the neck allowed independent head movement to look around above water while propped up on its pectoral fins, consistent with a shallow-water ambush hunter',
                'distractors': [
                    'The lateral line proves Tiktaalik was a deep-water fish — the lateral line only functions below the thermocline, so its presence contradicts the hypothesis that Tiktaalik lived in shallow coastal wetlands',
                    'Tiktaalik was fully terrestrial — the lateral line is a vestigial structure inherited from fully aquatic ancestors and had already lost its sensory function in Tiktaalik, just as the vestigial hind limbs of whales are non-functional remnants',
                    'The neck plus lateral line combination indicates Tiktaalik spent equal time on land and in water — animals with both features are definitionally amphibious, and all Devonian transitional forms therefore qualify as the first amphibians',
                ],
            },
            {
                'question': 'Tiktaalik is called a "fishapod" — a transitional form between fish and tetrapods. Why is it more accurate to call it "a cousin preserving transitional anatomy" rather than "our ancestor"?',
                'correct': 'The DIRECT ancestor of tetrapods is a different, probably closely related but distinct organism that has not been found as a fossil — Tiktaalik shows the morphological stage that transitional ancestors MUST have passed through, but it is a side-branch, not the actual lineage leading to modern tetrapods',
                'distractors': [
                    'Tiktaalik cannot be our ancestor because it was found in Canadian Arctic rocks — tetrapods evolved in tropical Gondwana, so any Canadian Devonian fish is geographically disqualified from being ancestral to tetrapods',
                    'Tiktaalik cannot be our ancestor because it post-dates Acanthostega and Ichthyostega, which are fully formed early tetrapods — a transitional form must be OLDER than the group it gave rise to, so Tiktaalik is too young to be ancestral',
                    'Tiktaalik is definitively our ancestor — calling it a "cousin" is overly conservative language used by paleontologists to avoid commitment, but cladistic analysis places Tiktaalik directly on the lineage leading to all tetrapods including humans',
                ],
            },
            {
                'question': 'Coelacanths (Latimeria) were thought to have gone extinct at the end of the Cretaceous (~65 Mya) until a living specimen was found off South Africa in 1938. Why is the coelacanth considered so important for understanding the fish-to-tetrapod transition?',
                'correct': 'Coelacanths are lobe-finned fish whose fin-bone anatomy is homologous to tetrapod limb bones (humerus, radius, ulna) — as a living close relative of the ancestral lobe-finned fish group that gave rise to tetrapods, they preserve anatomy relevant to the transition and can be studied physiologically in ways fossils cannot',
                'distractors': [
                    'Coelacanths are direct ancestors of tetrapods and have not evolved since the Devonian — they are living fossils in the strict sense that they are genetically unchanged from our tetrapod ancestor',
                    'Coelacanths are the only surviving tetrapods that returned to the water during the Devonian — their existence proves that the transition from fish to tetrapod is reversible under certain ecological conditions',
                    'Coelacanths have true digits on their fins, proving that digits evolved BEFORE the origin of tetrapods — this invalidates Tiktaalik as a transitional fossil because coelacanths already had the feature Tiktaalik supposedly pioneered',
                ],
            },
            {
                'question': 'The lungs of tetrapods and the primitive lung-like organs of some extant fish (like lungfish) are HOMOLOGOUS. Tetrapods inherited lungs from their fish ancestors rather than evolving lungs de novo upon moving to land. What does this reveal about the sequence of evolutionary innovations in the fish-to-tetrapod transition?',
                'correct': 'Major terrestrial adaptations like lungs and weight-bearing limbs did NOT all evolve together on land — lungs first appeared in aquatic fish as a way to supplement gill respiration in oxygen-poor water, and were already present before the transition to land; tetrapods then co-opted this pre-existing air-breathing capacity as their primary respiratory system',
                'distractors': [
                    'The homology shows that modern lungfish are the direct ancestors of all tetrapods — tetrapods diverged from lungfish in the Devonian and retained the lung structure unchanged, while losing the gill structure that lungfish still possess',
                    'The homology proves that lungs evolved from swim bladders rather than the reverse — tetrapods converted their ancestral swim bladders into lungs upon moving to land, making swim bladders the ancestral organ and lungs the derived one',
                    'Because lungs are homologous between fish and tetrapods, any fish with lungs can breathe air indefinitely on land — the only obstacle to fish walking on land today is the absence of legs, not any respiratory limitation',
                ],
            },
            {
                'question': 'Tiktaalik fossils were found in rocks dated to ~375 Mya, which is after Acanthostega (~365 Mya) in some estimates. How can a transitional form be slightly younger than some descendants and still be considered transitional?',
                'correct': 'Phylogenetic transitional forms do not need to be the oldest members of their lineage — a species can retain transitional anatomy while its contemporaries are more derived. Tiktaalik shows the transitional morphology that the common ancestor of all tetrapods must have passed through, even if Tiktaalik itself is a "late" representative of that body plan rather than the first',
                'distractors': [
                    'Tiktaalik is not actually transitional — because it post-dates some early tetrapods, it must be a re-evolved fish form that lost the tetrapod adaptations of its ancestors, making it an evolutionary reversal rather than a true transitional',
                    'The dating of Tiktaalik and Acanthostega is uncertain to ~50 million years, so the apparent age overlap is within measurement error — one of the two dates must be wrong and Tiktaalik is actually much older than Acanthostega',
                    'Transitional forms by definition must be older than all descendants — since Tiktaalik is younger than Acanthostega, it cannot be transitional and paleontologists misclassified it',
                ],
            },
            {
                'question': 'Tiktaalik\'s eyes are positioned on TOP of its head rather than on the sides (as in typical fish). What does this anatomical detail suggest about its ecological niche?',
                'correct': 'Eyes on top of the head allow the animal to see above the water line while its body remains submerged in shallow water — this is the "crocodile" lifestyle of an ambush predator lying in shallow wetlands, waiting for prey or surveying the surface environment, consistent with Tiktaalik being a shallow-water transitional form rather than a fully terrestrial or fully pelagic fish',
                'distractors': [
                    'Top-of-head eyes are an adaptation for deep-ocean vision — light only reaches down to the top of the head in deep-sea environments, so this feature proves Tiktaalik was a deep marine predator',
                    'The eye position is actually a preservational artifact — Tiktaalik skulls were crushed during fossilization, compressing the lateral eyes upward, and the original eye position was the same as modern bony fish',
                    'Top-of-head eyes indicate that Tiktaalik was a high-diving predator that plunged into the water from above, like a modern kingfisher — the eye position optimized vision during downward plunges through water',
                ],
            },
            {
                'question': 'Neil Shubin\'s discovery of Tiktaalik in 2004 is often cited as a triumph of evolutionary prediction. The field crew had to revisit Ellesmere Island across multiple field seasons before finding Tiktaalik. Why is the Tiktaalik discovery considered a particularly rigorous test of evolutionary theory rather than just a lucky find?',
                'correct': 'The prediction (a fish-tetrapod transitional form will exist in mid-Devonian coastal wetland rocks) was made in ADVANCE of the discovery, from phylogenetic reasoning alone, and was specific enough that finding such a form in any other rock type or age would have failed the test — the prediction could have been falsified but was confirmed, which is the hallmark of a scientific test rather than post-hoc rationalization',
                'distractors': [
                    'The Tiktaalik find is only a rigorous test because it was the single field season expedition — finding the fossil on the first try proved that the prediction was precise enough to guarantee discovery without error',
                    'The test is rigorous because Tiktaalik is the exact direct ancestor of all tetrapods — direct ancestor-descendant relationships are the strongest form of evolutionary evidence and cannot be faked',
                    'The discovery is rigorous because the Ellesmere Island rocks were previously considered barren of fossils — finding any animal there at all would have been a major scientific breakthrough regardless of what species it was',
                ],
            },
            {
                'question': 'Lungfish (Australian, South American, and African species) are extant lobe-finned fish that possess functional lungs and can breathe air. Phylogenetically, are lungfish in the direct ancestry of tetrapods, and what do they tell us about the fin-to-limb transition?',
                'correct': 'Lungfish are a sister group to tetrapods, not direct ancestors — both tetrapods and lungfish descend from a common lobe-finned ancestor, and lungfish have evolved independently since that split. However, lungfish preserve features (lungs, fleshy fins) that help reconstruct the anatomy of the common ancestor, making them important "living outgroups" for understanding the conditions from which the tetrapod lineage emerged',
                'distractors': [
                    'Lungfish are the direct ancestors of all tetrapods and have remained unchanged since the Devonian — they are "living fossils" whose anatomy is identical to the first air-breathing fish, so modern lungfish DNA is identical to the tetrapod ancestor DNA',
                    'Lungfish are not related to tetrapods at all — their lungs are convergent with tetrapod lungs, and their fleshy fins evolved independently as an adaptation to low-oxygen freshwater habitats unrelated to the fish-to-tetrapod transition',
                    'Lungfish descended from early tetrapods that returned to freshwater habitats and re-evolved fish-like features — they are therefore the descendants of tetrapods rather than being part of the ancestral tetrapod lineage',
                ],
            },
        ],
        visual={
            'type': 'transition',
            'description': 'Fin-to-limb transition',
            'regions': [
                {'label': 'Lobe-finned fish', 'color': '#4ea8de', 'items': ['Bony fin bones', 'No neck', 'Fully aquatic']},
                {'label': 'Tiktaalik', 'color': '#ffc857', 'items': ['Weight-bearing elbows', 'Bending wrist', 'Neck, no operculum', 'Top-of-head eyes']},
                {'label': 'Early tetrapods', 'color': '#7de2d1', 'items': ['Acanthostega, Ichthyostega', 'True limbs with digits', 'Mostly aquatic']},
                {'label': 'Modern tetrapods', 'color': '#8a5cf6', 'items': ['Limbs, digits', 'Fully terrestrial capable']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Fins → Fishapod (Tiktaalik) → Limbs.',
            'trap': 'Tiktaalik was NOT a land-walker. It still had gills, a lateral line, and was aquatic. "Walking on land" came later with Acanthostega and Ichthyostega.',
        },
    diagram=tiktaalik_transition_flow_diagram(),
    ))

    # ---- Node 5: Feathers, Archaeopteryx & Exaptation (slides 38-44) ----
    sections = slides_to_sections(d, (38, 44))
    sections.append(audio_section(
        'Feathers before flight, Velociraptor quill nodes, exaptation, swim bladder (recorded 2026-04-06)',
        APR6_FEATHERS,
    ))
    nodes.append(build_node(
        id='lec15-feathers-exaptation',
        title='Feathers Evolved BEFORE Flight: Exaptation',
        subtitle='Archaeopteryx, quill nodes, swim bladder (Lec 15 slides 38-44)',
        color='coral', row=13,
        heading='Lecture 15 — Phylogenies Track Trait Evolution',
        sections=sections,
        examples=[
            'Archaeopteryx (discovered 1860, ~145 Mya): classic transitional form between theropod dinosaurs and modern birds. Has feathers AND teeth, claws on wings, long bony tail.',
            'Feathered non-flying dinosaurs: Velociraptor, Oviraptor, Tyrannosauroid relatives — small arms, could NOT have used feathers for flight. Feathers preceded flight.',
            'Pre-flight feather functions: species recognition, mate attraction (color), insulation, egg incubation (Oviraptor was found brooding eggs, 1993).',
            'Quill nodes: regularly-spaced bumps on the ulna where feather quills attach. Found on modern bird bones (turkey vulture example) AND on Velociraptor ulna fossils — direct evidence of feather attachment in non-flying dinosaurs.',
            'Exaptation: a trait that originally evolved for one function, later co-opted for a NEW function. Feathers (insulation) → flight. Not the same as adaptation (trait evolved FOR its current function).',
            'Another exaptation: swim bladders are HOMOLOGOUS to lungs. The earliest fish had primitive lungs to gulp air at the surface in low-oxygen water. Tetrapods kept lungs; many fish modified lungs into gas-filled buoyancy organs (swim bladders).',
            'Flight stroke may have evolved as running-assist (flapping while chasing prey or escaping predators) — wing-assisted incline running (WAIR) is hypothesized as the bridge.',
        ],
        warnings=[
            'Exaptation does NOT require gene duplication (unlike co-option at the molecular level). The same structure is REPURPOSED without gaining a copy.',
            'Birds ARE dinosaurs (theropod dinosaurs, specifically). They are the only surviving dinosaur lineage.',
            'Do not confuse exaptation with LAMARCKISM. The feather-to-flight transition was driven by SELECTION at each stage, not by an organism "striving" toward flight.',
        ],
        mnemonic='Exaptation = "ex-adaptation" — same trait, NEW function. Feathers → insulation → FLIGHT.',
        flashcard={
            'front': 'What is exaptation, and how do feathers illustrate this concept?',
            'back': 'EXAPTATION is a trait that originally evolved via selection for ONE function, but was later CO-OPTED for a different function — with or without further modification. Coined by Gould and Vrba in 1982. Feathers are the classic example: early theropod dinosaurs (long before birds and flight) had feathers that likely served INSULATION (keeping warm in cold climates, since many were small) and/or DISPLAY (mate attraction, species recognition, egg incubation). Evidence: (1) Feathered non-flying dinosaurs like Velociraptor and Sinosauropteryx, which had arms too short to fly. (2) Oviraptor fossils found brooding their eggs (1993) — feathers useful for insulation. (3) Velociraptor ulna shows QUILL NODES — regularly-spaced bumps where feathers attached, matching modern birds. Flight evolved LATER, using the already-present feathers. Another example: swim bladders are HOMOLOGOUS to lungs — early fish used primitive lungs to gulp air at the surface; many fish lineages later repurposed those lungs into buoyancy organs. Exaptation is crucial because it explains how complex adaptations can "sneak up" on a new function.',
        },
        quiz=[
            {
                'question': 'Why is the evolution of feathers considered an example of EXAPTATION rather than adaptation for flight?',
                'correct': 'Feathers evolved first for other functions (insulation, display), then were co-opted for flight',
                'distractors': [
                    'Feathers are made of the same protein as scales',
                    'All dinosaurs had feathers',
                    'Flight evolved before feathers',
                ],
            },
            {
                'question': 'Velociraptor had short arms and could NOT have used feathers for powered flight. Yet Velociraptor ulna bones show regularly-spaced quill nodes matching those of modern birds. What does this anatomical evidence directly prove?',
                'correct': 'Velociraptor had large, well-developed feathers attached to its ulna — feathers were PRESENT in non-flying dinosaurs before the origin of birds, confirming that feathers preceded flight and were used for non-flight functions (insulation, display, brooding)',
                'distractors': [
                    'Velociraptor quill nodes prove it was capable of gliding but not powered flight — quill nodes appear at an intermediate stage of feather evolution when wings are large enough to slow a fall but too small to generate lift from the ground',
                    'Quill nodes in Velociraptor fossils are convergent with birds — Velociraptor evolved them independently to reduce drag while running, and they have no connection to feather evolution in the theropod lineage leading to birds',
                    'The quill nodes prove Velociraptor is the direct ancestor of modern birds — only organisms with quill nodes on the ulna can give rise to feathered descendants, and no other non-avian dinosaur has been found with this feature',
                ],
            },
            {
                'question': 'The swim bladder of modern bony fish is homologous to tetrapod lungs. The earliest fish had lungs to gulp air in low-oxygen water; many lineages later converted those lungs into buoyancy organs. What evolutionary concept does this illustrate, and how does it differ from exaptation?',
                'correct': 'This is exaptation — the lung (originally an air-breathing organ for low-oxygen water) was co-opted for a new function (buoyancy control as a swim bladder); exaptation is the co-option of a pre-existing structure for a new function regardless of whether the structure is modified in the process',
                'distractors': [
                    'This is convergent evolution — swim bladders and lungs look similar and perform related functions, but they evolved independently from completely unrelated structures in the fish and tetrapod lineages',
                    'This is an example of Lamarckian inheritance — fish that swallowed air frequently developed larger air sacs, which were passed to offspring; over generations, the air sac became a fully functional buoyancy organ through use-inheritance',
                    'This is adaptive radiation — once lungs evolved in ancestral fish, the lung structure radiated into many different body forms (swim bladder, book lung, tracheal lung) across different lineages simultaneously during the Devonian radiation',
                ],
            },
            {
                'question': 'The wing-assisted incline running (WAIR) hypothesis proposes that the transition to powered flight involved using proto-wings to run up steep inclines. How does this hypothesis solve the "half-a-wing is useless" objection to feathered flight evolving?',
                'correct': 'WAIR shows that even small proto-wings provide an immediate fitness benefit (better traction and stability on steep slopes during escape from predators) without requiring any aerodynamic lift — each incremental improvement in wing size and stroke angle improves both WAIR efficiency AND eventually generates lift, providing continuous positive selection throughout the transition',
                'distractors': [
                    'WAIR solves the problem by showing that proto-wings did not need to be functional at all — they served as camouflage while the animal was stationary, providing a neutral fitness baseline until they accidentally became large enough for flight',
                    'WAIR is actually irrelevant to the half-a-wing objection — the objection was already answered by the discovery that early feathers served as insulation, and WAIR is merely an alternative hypothesis competing with insulation that has not been tested empirically',
                    'WAIR solves the problem by demonstrating that flight evolved from the trees down rather than the ground up — small proto-wings in tree-dwelling dinosaurs provided drag to slow gliding descents, so half-a-wing was always useful during the arboreal phase',
                ],
            },
            {
                'question': 'Archaeopteryx (discovered 1860, ~145 Mya) has feathers AND teeth AND claws on its wings AND a long bony tail. Why does this combination of features make Archaeopteryx a particularly strong example of a transitional fossil?',
                'correct': 'Archaeopteryx simultaneously possesses defining features of both ancestral theropod dinosaurs (teeth, bony tail, clawed forelimbs) and derived modern birds (asymmetric flight feathers, wishbone) — a single organism preserving both character sets is the clearest possible evidence of intermediate morphology between two groups',
                'distractors': [
                    'Archaeopteryx is considered transitional because it is extremely common in the fossil record — hundreds of specimens have been found, allowing paleontologists to document every intermediate stage between dinosaurs and birds from its fossils alone',
                    'Archaeopteryx is a strong transitional form because it was found in sedimentary rocks alongside modern bird fossils, proving direct continuity between dinosaur and bird lineages in the same ecosystem',
                    'Archaeopteryx is a transitional form only in appearance — DNA extracted from Archaeopteryx specimens places it firmly within modern birds rather than as an intermediate, so the morphological similarities to dinosaurs are convergent',
                ],
            },
            {
                'question': 'Oviraptor (a non-flying theropod dinosaur) was found in 1993 in a brooding posture on a nest of eggs. How does this discovery support the hypothesis that feathers functioned as insulation BEFORE they functioned in flight?',
                'correct': 'Brooding behavior — sitting on a nest to regulate egg temperature — requires a body covering capable of retaining heat around the eggs; the discovery of a non-flying dinosaur in a brooding posture indicates that insulating feathers were already present for thermal regulation (for both the parent and the eggs), independent of any aerial function',
                'distractors': [
                    'Oviraptor was originally thought to eat eggs (the name means "egg thief"), and its brooding posture was a hunting strategy rather than parental care — it was using its feathers as camouflage to wait for other dinosaurs to return to the nest so it could eat their eggs',
                    'The Oviraptor nest contained eggs from multiple species, proving that it was a communal nesting site for different dinosaurs — the brooding posture represents defense of the shared nest rather than insulation of a single clutch',
                    'Oviraptor was preserved in brooding posture because of a sudden sandstorm, not because it was actively incubating — the fossil shows accidental burial rather than evidence of parental care or feather function',
                ],
            },
            {
                'question': 'The term EXAPTATION was coined by Stephen Jay Gould and Elisabeth Vrba in 1982 to replace the older concept of "pre-adaptation." Why did they object to the term "pre-adaptation" and prefer "exaptation"?',
                'correct': 'The prefix "pre-" in pre-adaptation implies that a trait was somehow anticipating or prepared for its future function, which is teleological (goal-directed) and contradicts the non-directional nature of natural selection — exaptation removes the implication of foresight and correctly describes the trait as being repurposed from an existing function after the fact',
                'distractors': [
                    '"Pre-adaptation" was rejected because it implied the trait existed before organisms evolved, while "exaptation" correctly specifies that the trait arose during evolution — the terminological change reflects the shift from creationist to evolutionary thinking',
                    'Gould and Vrba renamed the concept because they discovered that "pre-adaptation" had originally been used to describe a completely different phenomenon in the 19th century, and they wanted to avoid historical confusion with an outdated definition',
                    'The term "exaptation" was created to apply specifically to molecular traits, while "pre-adaptation" was retained for morphological traits — the two terms describe different levels of biological organization rather than representing a terminological replacement',
                ],
            },
            {
                'question': 'Small theropod dinosaurs (like those that later gave rise to birds) are often found in cold paleoclimates and had relatively small body sizes. How does this information specifically support the insulation hypothesis for the origin of feathers?',
                'correct': 'Small body size means a high surface-area-to-volume ratio and rapid heat loss; combined with cold paleoclimates, small theropods would have faced strong selection for thermal insulation — an insulating body covering (such as proto-feathers or filamentous feathers) provides an immediate survival advantage independent of any eventual flight function, meeting the criterion for a feather function BEFORE flight',
                'distractors': [
                    'Small body size in cold climates is evidence AGAINST the insulation hypothesis because small animals cannot afford the metabolic cost of producing an insulating covering — only large-bodied dinosaurs had enough metabolic reserve to grow feathers, so feathers must have evolved in large theropods first',
                    'Cold climates are irrelevant to feather origins because all dinosaurs were ectothermic ("cold-blooded") and could not benefit from insulation regardless of body size — feathers must have evolved for a non-thermal function such as display',
                    'Small theropods in cold climates is a coincidence and does not support any hypothesis about feather function — correlations between paleoclimate, body size, and feather presence are spurious and have no biological meaning',
                ],
            },
            {
                'question': 'The swim-bladder-from-lung exaptation story is reversed in direction from the feather-from-insulation story. In fish, primitive LUNGS evolved first (for gulping air in low-oxygen water), and in many lineages were later converted into swim bladders for buoyancy. Why is this a useful counterpoint to the "feathers for flight" misconception?',
                'correct': 'Both examples show that complex specialized organs did not evolve FOR their current function — lungs existed for gas exchange long before being repurposed for buoyancy, and feathers existed for insulation/display long before being repurposed for flight. Both cases demonstrate that selection operates on whatever current function improves fitness, with no foresight toward future uses',
                'distractors': [
                    'The swim bladder case shows that lungs were originally a flight organ in early fish, supporting the idea that aerial locomotion (flight-like) functions precede aquatic ones — by analogy, feathers would also have served flight before other functions',
                    'The two examples are opposite rather than similar — feather evolution shows exaptation from simple to complex, while swim bladder evolution shows reversal from complex to simple, so they cannot both be used as support for the same concept',
                    'The swim bladder case is irrelevant to feathers because bony fish and dinosaurs are on completely different branches of the tree of life — exaptation in fish has no bearing on whether exaptation occurred in dinosaurs',
                ],
            },
            {
                'question': 'Exaptation differs from adaptation in that an exaptation is a trait currently useful for a function it did NOT originally evolve for. A student argues that this distinction is meaningless because, after enough time under selection for the new function, the trait becomes a "real" adaptation. How should a biologist respond to this argument?',
                'correct': 'The student is partly right — under continued selection for the new function, a trait initially exapted can be further modified and become fully adapted to that new role (e.g., flight feathers are now highly optimized asymmetric airfoils). However, the historical distinction still matters because it explains HOW the trait got its start; exaptation is about the origin of the new function, while adaptation describes the subsequent refinement, and both concepts are needed to describe the full history',
                'distractors': [
                    'The student is completely wrong — exaptations NEVER become adaptations over time, because the historical origin of a trait cannot change retroactively; a trait is classified permanently by its original function and cannot be re-classified as an adaptation to a new function',
                    'The student is completely right — the distinction is indeed meaningless, and Gould and Vrba\'s terminology is not used by practicing biologists because every exaptation rapidly becomes an adaptation under continued selection',
                    'The student is wrong because exaptations and adaptations are mutually exclusive categories — a trait is one or the other, never both, and continued selection converts an exaptation into an adaptation only by erasing its original function from the fossil record',
                ],
            },
        ],
        visual={
            'type': 'exaptation',
            'description': 'Feather functional evolution',
            'regions': [
                {'label': 'Origin', 'color': '#6e6a80', 'items': ['Small theropods', 'Insulation, display']},
                {'label': 'Expansion', 'color': '#ffc857', 'items': ['Egg incubation', 'Larger feathers', 'Quill nodes on ulna']},
                {'label': 'Flight stroke', 'color': '#f77f00', 'items': ['WAIR hypothesis', 'Running-assist', 'Escape predators']},
                {'label': 'True flight', 'color': '#7de2d1', 'items': ['Archaeopteryx ~145 Mya', 'Modern birds']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Insulation → Display → Running-assist → Flight. Exaptation every step.',
            'trap': 'Do NOT say "feathers evolved FOR flight." That is a teleological error. Feathers evolved for OTHER reasons and were LATER useful for flight.',
        },
    diagram=feathers_before_flight_exaptation_diagram(),
    ))

    return nodes
