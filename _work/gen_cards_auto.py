#!/usr/bin/env python3
"""
Auto-generate comprehensive flashcards from node content in data.json.
Uses the structured content (sections, examples, warnings, mnemonics) to create
multiple cards per node from different angles.
"""
import json, os, re, hashlib

PROJ = r'C:\Users\johnn\Desktop\evolution-study-guide'
DATA = os.path.join(PROJ, 'data.json')

with open(DATA, 'r', encoding='utf-8') as f:
    data = json.load(f)

def clean(text):
    """Clean text for card content"""
    if not text:
        return ""
    text = text.strip()
    # Collapse multiple spaces
    text = re.sub(r'\s+', ' ', text)
    return text

def make_card(front, tech, eli5):
    """Create a card dict with both answer types"""
    return {
        "front": clean(front),
        "back": f"**TECHNICAL:** {clean(tech)}\n\n**ELI5:** {clean(eli5)}"
    }

def dedupe_cards(cards):
    """Remove exact duplicate fronts"""
    seen = set()
    result = []
    for c in cards:
        key = c["front"].lower().strip()
        if key not in seen:
            seen.add(key)
            result.append(c)
    return result

# ============================================================
# HAND-CRAFTED CARDS PER NODE
# These are the highest-quality, exam-targeted cards
# ============================================================

CARDS = {}

# ─── LEC1: INTRO ───
CARDS["lec1-intro-evolution"] = [
    make_card("What is the most precise scientific definition of evolution?",
              "Evolution is a change in the frequency of alleles in a population across generations. It occurs at the POPULATION level, NOT within an individual's lifetime.",
              "Imagine a bag of M&Ms where each color is a gene version. Evolution is when the color mix changes from one refill to the next — not when a single M&M changes color."),
    make_card("Who said 'Nothing in biology makes sense except in the light of evolution,' and when?",
              "Theodosius Dobzhansky, in a 1973 essay in The American Biology Teacher.",
              "Dobzhansky basically said: trying to understand biology without evolution is like watching a movie in random scene order — you need the storyline."),
    make_card("Why is evolution considered the unifying theory of biology?",
              "Every subfield — cell bio, ecology, genetics, anatomy — relies on the insight that organisms share common ancestry and have been shaped by selection, drift, mutation, and gene flow. Without evolution, shared molecular machinery (universal genetic code), homologies, and biodiversity have no causal explanation.",
              "Evolution is like gravity for biology — it's the one rule that explains everything. Why do humans and bananas share DNA? Evolution."),
    make_card("List five practical applications of evolutionary biology.",
              "(1) Agriculture — crop breeding. (2) Medicine — antibiotic/vaccine design. (3) Conservation — managing genetic diversity. (4) Immunology — pathogen adaptation. (5) Epidemiology — predicting outbreak evolution.",
              "Evolution helps us grow better food, make better drugs, save endangered species, understand how diseases work, and predict pandemics."),
    make_card("Why is it wrong to say 'evolution means organisms improve over time'?",
              "Evolution is population-level allele frequency change, not improvement. There is no 'higher' or 'lower' — selection optimizes for the CURRENT environment, which changes. Bacteria are as evolved as humans.",
              "Evolution isn't a ladder going up — it's a bush growing in every direction. Cockroaches aren't 'less evolved' than you — they've just been evolving for a different lifestyle."),
    make_card("Why can't an individual organism evolve?",
              "An individual's genotype is fixed at conception. Evolution requires allele frequency change across generations WITHIN A POPULATION. Somatic changes (muscle gain, tanning) are not heritable.",
              "You can't evolve any more than a single playing card can change the whole deck. Evolution is about the deck's composition changing over many reshuffles (generations)."),
    make_card("A student says giraffes evolved long necks by stretching. What is wrong?",
              "This is Lamarckian inheritance of acquired characteristics. Stretching doesn't alter germline DNA. Correct: giraffes with genetically longer necks had a survival/reproduction advantage, passing those alleles to offspring over generations.",
              "Working out doesn't give your kids bigger muscles. Giraffes born with longer necks got more food, survived, and had more long-necked babies. Repeat for thousands of generations."),
    make_card("What does 'fitness' mean in evolutionary biology?",
              "Fitness = the ability to survive and reproduce RELATIVE to other individuals in the population. It is always comparative, not absolute. A fit organism leaves more copies of its alleles in the next generation.",
              "In evolution, 'fit' doesn't mean gym-buff. It means who has the most surviving babies. A scrawny mouse with 20 babies is fitter than a jacked mouse with 2."),
    make_card("What is an adaptation?",
              "A heritable trait that increases fitness relative to individuals lacking it, in a specific environment. Adaptations arise through natural selection on heritable variation.",
              "An adaptation is a cheat code for survival — but only in a specific level. Polar bear fur is great in the Arctic, terrible in the Sahara."),
    make_card("What is the difference between a scientific 'theory' and an everyday 'theory'?",
              "A scientific theory is a well-substantiated explanation supported by multiple independent lines of evidence, rigorously tested. Evolution is on the same epistemic footing as gravity and plate tectonics. Not a guess or speculation.",
              "In regular life, 'theory' = guess. In science, 'theory' = a GPS that's been tested a million times and always works. Evolution is that reliable."),
    make_card("When was On the Origin of Species published and by whom?",
              "Published by Charles Darwin in 1859.",
              "Darwin dropped the biggest science mic in 1859 with a book that said 'all life is related and nature picks winners.'"),
]

# ─── LEC1: FLU ───
CARDS["lec1-flu-case-study"] = [
    make_card("What are the two key surface proteins on influenza, and what does each do?",
              "(1) Hemagglutinin (HA) — binds virus to host cell receptors, enabling entry. (2) Neuraminidase (NA) — cleaves sialic acid bonds so new viruses can detach and spread.",
              "HA is the key that unlocks the door INTO your cells. NA is the scissors that cut the rope so new viruses can ESCAPE. Together: the flu's B&E toolkit."),
    make_card("How many genes and RNA segments does influenza have?",
              "13 genes on 8 separate RNA segments. The segmented genome enables reassortment.",
              "Flu's manual comes in 8 separate booklets. If two flu strains infect one cell, booklets get mixed — creating a totally new combo flu."),
    make_card("What is antigenic drift?",
              "Gradual accumulation of point mutations in HA/NA due to error-prone RNA replication, reducing vaccine effectiveness over time. Small, incremental changes.",
              "The flu gets a tiny nose job every year. Your immune system's wanted poster slowly stops matching. That's why you need a new flu shot annually."),
    make_card("What is antigenic shift/reassortment and how does it differ from drift?",
              "Shift = two strains co-infect one cell and exchange entire RNA segments, producing a radically different virus. Unlike drift (gradual), shift is sudden and can produce pandemic strains.",
              "Drift = slowly changing your outfit. Shift = swapping entire wardrobes with someone. Shift causes pandemics because nobody recognizes the new look."),
    make_card("How did H1N1 (2009) originate?",
              "Triple reassortment of avian, swine, and human flu RNA segments in a pig host. Pigs are 'mixing vessels' because they have receptors for both bird and human flu.",
              "A pig caught bird flu AND human flu. Inside the pig, the viruses shuffled their gene booklets, creating a new combo that jumped to humans = 2009 pandemic."),
    make_card("Describe the Hensley et al. (2009) experiment and its conclusion.",
              "Passaged flu through vaccinated mice for 9 cycles. Virus evolved altered HA (vaccine escape). Control (unvaccinated mice): NO HA change. Proved immune selection drives HA evolution.",
              "Scientists played 'tag' between flu and vaccinated mice for 9 rounds. Flu changed its disguise to escape. Flu vs unvaccinated mice didn't bother changing. Proved the vaccine FORCES evolution."),
    make_card("Why does influenza need an annual vaccine update?",
              "HA/NA accumulate mutations via antigenic drift + immune selection. Within 1-2 years, strains diverge enough that last year's vaccine antibodies no longer bind effectively.",
              "The flu changes its face every year. Last year's wanted poster doesn't match this year's criminal. Scientists update the poster (vaccine) annually."),
    make_card("Why are pigs 'mixing vessels' for influenza?",
              "Pig respiratory cells express receptors for both avian (α-2,3) and human (α-2,6) influenza. Co-infection enables reassortment of segments, producing novel strains.",
              "Pigs can catch bird flu AND human flu simultaneously. Their cells have doors for both. Two viruses + one pig = a new pandemic virus recipe."),
    make_card("Why do most flu mutations NOT lead to vaccine escape?",
              "Most mutations are neutral or deleterious. Only rare mutations that alter HA/NA epitopes while maintaining protein function provide selective advantage.",
              "Most disguise changes the flu tries make it worse — like a mask that blocks its own eyes. Only a few lucky changes fool your immune system AND still let the virus work."),
    make_card("How does influenza demonstrate real-time evolution?",
              "High mutation rate, short generation time (hours), and large populations allow evolution to be observed within a single season via genomic surveillance.",
              "Flu evolves so fast we can watch it happen live, like time-lapse evolution. New versions appear, spread, and take over in months."),
]

# ─── LEC1: TAKE-HOME ───
CARDS["lec1-takehome-course"] = [
    make_card("Why do epidemiologists monitor pig farms for new flu strains?",
              "Pigs express both avian and human flu receptors. Farms with high density + exposure to wild birds are the most likely sites for reassortment events producing novel pandemic strains.",
              "Pig farms are virus mixing bowls. Pigs catch bird + human flu simultaneously, viruses swap parts inside the pig = new pandemic recipe. Scientists watch pig farms as pandemic early warning."),
    make_card("What is Dr. Robbins' research focus?",
              "Ecology and evolution of lizards (Sceloporus), reptile physiology, life history, and thermal adaptation.",
              "Dr. Robbins is a lizard guy — he studies how lizards evolve to handle different temperatures and survive in different environments."),
    make_card("What does BIOL 4230 emphasize beyond memorization?",
              "Reading assigned material, attending lectures, and APPLYING concepts to novel problems. Passive memorization is insufficient — students must understand mechanisms and make predictions.",
              "You can't just memorize and regurgitate. You need to understand the 'why' well enough to solve problems you've never seen before."),
]

# ─── LEC2: PRE-DARWIN ───
CARDS["lec2-pre-darwin"] = [
    make_card("What was the 'Great Chain of Being'?",
              "Dominant Western framework from Ancient Greeks through 18th century. Arranged all organisms in a fixed, divinely ordained hierarchy. Species were immutable — they did not change.",
              "People thought every species was on a permanent God-made ladder — plants at the bottom, humans near the top, nothing ever moves or changes."),
    make_card("What date did Archbishop Ussher calculate for Creation?",
              "October 23, 4004 BC, at 9:00 AM. Calculated in 1664 using biblical chronology. Placed Earth at ~6,000 years old.",
              "A church leader added up all the ages in the Bible and decided Earth was born on a specific Tuesday morning in 4004 BC. That's younger than some individual trees alive today."),
    make_card("What was Linnaeus's contribution? (1707-1778)",
              "Developed binomial nomenclature (genus + species naming) and hierarchical classification (kingdom→class→order→genus→species). Organized life under a Divine Plan, but unknowingly created a framework that revealed evolutionary relationships.",
              "Linnaeus was biology's librarian — he invented the naming system (Homo sapiens) and organized species into groups. He thought he was filing God's creations, but actually showed how life is related."),
    make_card("What is uniformitarianism and who proposed it?",
              "James Hutton (1726-1797), later championed by Lyell. The idea that geological processes operating today (erosion, volcanism) have always operated at similar rates. Implies Earth must be extremely old.",
              "Hutton said: tiny stream + enough time = Grand Canyon. The Earth must be REALLY old for today's slow processes to carve the landscapes we see."),
    make_card("What did Cuvier document? (1769-1832)",
              "Georges Cuvier documented EXTINCTION using fossils — proving species can disappear. Proposed catastrophism: sudden geological events cause mass extinctions followed by new creations.",
              "Cuvier found bones of animals that don't exist anymore and proved extinction is real. Before him, people thought God made everything permanent."),
    make_card("Who proposed the first formal theory of evolution? Why was the mechanism wrong?",
              "Lamarck (1744-1829). Proposed inheritance of acquired characteristics — organisms change via use/disuse and pass changes to offspring. Wrong because somatic changes don't alter germline DNA.",
              "Lamarck was right that species change (evolution) but wrong about HOW. He thought if you work out, your kids are born buff. Nope — body changes don't rewrite DNA."),
    make_card("What did William Smith contribute? (1769-1839)",
              "Organized geological history by fossil content (faunal succession) — specific fossils associate with specific rock strata, allowing correlation across locations.",
              "Smith figured out certain fossils always appear in certain rock layers — like how clothing fashion tells you the decade in old yearbooks."),
    make_card("How did these pre-Darwin figures set the stage for natural selection?",
              "Cuvier proved extinction (species aren't permanent). Hutton/Lyell provided deep time (enough time for gradual change). Lamarck proposed species change (mechanism wrong but idea right). Linnaeus's classification hinted at shared ancestry. Together they made Darwin's insight conceptually possible.",
              "Each person added a puzzle piece: 'things die out' + 'Earth is old' + 'life can change' + 'life is organized in groups.' Darwin was the one who saw how all the pieces fit together."),
    make_card("What is the LCLLL mnemonic for pre-Darwin thinkers?",
              "Linnaeus (classification) → Cuvier (extinction) → Lamarck (first mechanism) → Lyell (deep time) → Darwin (natural selection). Captures chronological order of key contributions.",
              "The relay race of ideas: sort life → prove extinction → propose change → show time → explain HOW = Darwin."),
]

# ─── LEC2: DARWIN VOYAGE ───
CARDS["lec2-darwin-voyage"] = [
    make_card("How old was Darwin when he joined the Beagle, and what were the voyage dates?",
              "22 years old. HMS Beagle 1831-1836, a 5-year circumnavigation primarily along South America and through the Galápagos.",
              "Darwin was basically college-aged (22) when he got on a boat for 5 years and came back with ideas that changed the world."),
    make_card("What role did John Gould play in Darwin's thinking?",
              "London ornithologist who identified Darwin's Galápagos bird specimens as all FINCHES — different species adapted to different niches. Darwin hadn't realized this in the field. This was the catalytic insight for adaptive divergence.",
              "Darwin collected birds thinking they were different types. Bird expert Gould said 'These are ALL finches — just modified versions.' That was Darwin's light-bulb moment."),
    make_card("Why did the fossil and living armadillos matter to Darwin?",
              "Fossil glyptodonts resembled living armadillos in the same region. Geographic correspondence of extinct and living forms suggested descent with modification — living species descended from fossil forms.",
              "Darwin found ancient armadillo fossils near modern armadillos. Like finding your great-grandma's photo and realizing you look alike — the old ones became the new ones."),
    make_card("Why did Darwin wait 20+ years to publish?",
              "Meticulous scientist wanting overwhelming evidence. Spent decades on barnacles, pigeon breeding, plant hybridization, and biogeography. Also feared social/religious backlash.",
              "Darwin knew his idea was a bombshell and spent 20 years building an airtight case. He was also terrified of the church's reaction."),
    make_card("Who was Alfred Russel Wallace?",
              "Independently conceived natural selection while in the Malay Archipelago. Sent Darwin a letter in 1858 describing his theory. Joint 1858 Linnean Society presentation (largely unnoticed). Origin published 1859.",
              "Wallace came up with the same idea as Darwin, independently. Darwin panicked and they presented together in 1858 — nobody cared. Then Darwin published his book in 1859 and got all the fame."),
    make_card("What book did Darwin read on the Beagle that shaped his thinking?",
              "Lyell's Principles of Geology. Uniformitarianism gave Darwin the framework of deep time needed for gradual biological change.",
              "Darwin read Lyell's geology book on the ship: 'tiny changes + tons of time = huge results.' He applied that to living things: tiny differences + tons of generations = new species."),
]

# I'll continue with all remaining nodes in the next sections...
# For now let's save this checkpoint

# Write checkpoint
with open(os.path.join(PROJ, '_work', 'cards_partial.json'), 'w', encoding='utf-8') as f:
    json.dump(CARDS, f, ensure_ascii=False, indent=1)

total = sum(len(v) for v in CARDS.values())
print(f"Partial checkpoint: {total} cards across {len(CARDS)} nodes")
for nid, cards in CARDS.items():
    print(f"  {nid}: {len(cards)} cards")
