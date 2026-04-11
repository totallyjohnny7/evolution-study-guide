"""Final-exam extras: species concepts, biogeography, conservation, human evo,
evolutionary medicine. These were in the original study guide and cover
material from chapters the core 1-15 lecture deck didn't fully duplicate,
so we keep them verbatim and reassign them to the final-exam rows (14 and 15).
"""
import json, os

EXISTING_PATH = os.path.join(
    os.path.dirname(__file__), '..', '..', '_extracted_data.json'
)

# IDs we want to keep (history-of-life and phylogenetics are REPLACED
# by the new lecture-based Lec 14 and Lec 15 nodes).
KEEP_IDS = {
    # 'species-concepts' is replaced by the richer ch13_nodes() in lectures_16_speciation.py
    'biogeography-extinction',
    'conservation',
    'human-evolution',
    'evolutionary-medicine',
}

# Expanded quiz banks (4 questions each — replaces single-question originals)
QUIZ_OVERRIDES = {
    'biogeography-extinction': [
        {
            'question': 'After a mass extinction event, surviving lineages often diversify explosively into newly vacant niches. This pattern is called:',
            'correct': 'Adaptive radiation — rapid diversification to fill ecological opportunity created by extinction',
            'distractors': [
                'Allopatric speciation — geographic separation drives the diversification',
                'Punctuated equilibrium — evolution happens in sudden bursts with no ecological trigger',
                'Founder effect — small colonizing populations diversify due to genetic drift',
            ],
        },
        {
            'question': 'Oceanic islands like Hawaii tend to have extremely high proportions of endemic species. The BEST evolutionary explanation is:',
            'correct': 'Geographic isolation allows independent evolution; founder effects plus adaptive radiation create unique lineages with no back-migration to homogenize gene pools',
            'distractors': [
                'Islands have harsher environments, driving faster mutation rates',
                'Island species are protected from mainland predators and thus evolve faster',
                'Islands have more ecological niches per square kilometer than continents',
            ],
        },
        {
            'question': 'The Great American Biotic Interchange (~3 mya) occurred when the Isthmus of Panama closed. Which prediction does biogeography make about which fauna would OUTCOMPETE the other?',
            'correct': 'North American fauna would largely outcompete South American fauna, because North America was connected to the larger Eurasian landmass and had more diverse competing lineages',
            'distractors': [
                'South American fauna would dominate, because island species are typically better competitors',
                'Neither would outcompete — competitive exclusion does not occur between continents',
                'The outcome depends entirely on which species arrived first, not geographic origin',
            ],
        },
        {
            'question': 'Vicariance biogeography and dispersal biogeography differ in that:',
            'correct': 'Vicariance explains disjunct distributions by geological splitting of a once-continuous range; dispersal explains them by colonization across an existing barrier',
            'distractors': [
                'Vicariance applies only to islands; dispersal applies only to continents',
                'Vicariance requires convergent evolution; dispersal does not',
                'Dispersal always produces more genetic diversity than vicariance',
            ],
        },
        {
            'question': 'The "Big Five" mass extinctions in Earth history (end-Ordovician, late Devonian, end-Permian, end-Triassic, K-T) each eliminated >50% of marine species. The end-Permian (~251 Mya) was the largest at ~96% loss. What general pattern of post-extinction recovery is observed in the fossil record?',
            'correct': 'Recovery takes millions of years, but surviving lineages typically undergo rapid adaptive radiation into vacant niches — after the end-Permian, marine invertebrates took ~5-10 million years to rediversify, and the resulting ecosystems were dominated by different lineages than before the extinction',
            'distractors': [
                'Post-extinction recovery is essentially instantaneous on geological timescales — within ~1000 years, species numbers return to pre-extinction levels through rapid speciation in refugia',
                'Recovery from mass extinctions never reaches pre-extinction diversity levels — each extinction permanently reduces Earth\'s biodiversity, and modern diversity is less than half of what existed before the end-Permian',
                'The dominant groups after each extinction are always the SAME lineages that dominated before — mass extinctions act as bottlenecks that preserve only the fittest lineages, which then re-dominate ecosystems in the recovery phase',
            ],
        },
        {
            'question': 'The Great American Biotic Interchange (~3 mya) saw South American marsupials largely lose to North American placental mammals. What specific ecological/evolutionary factor best explains the asymmetric outcome?',
            'correct': 'North America had been connected via Beringia to Eurasia for most of the Cenozoic, so its fauna had been tested against a vastly larger pool of competitors and predators — South America\'s isolated fauna had evolved in the absence of this competition, so North American lineages were better-honed for interspecific interactions when the two faunas met',
            'distractors': [
                'Placental mammals are intrinsically superior to marsupials because placental reproduction is more energy-efficient, and this biological superiority automatically produces dominance whenever the two groups meet',
                'The interchange was driven by a rapid climate shift that favored tropical species from the north, and South America\'s temperate fauna could not adapt in time — the outcome reflects climate rather than competition',
                'North American fauna outcompeted South American fauna because of a chance asteroid impact in South America that happened to coincide with the isthmus closure, eliminating many marsupials before the interchange occurred',
            ],
        },
        {
            'question': 'Sixth mass extinction: many biologists argue we are currently in an anthropogenic extinction event with loss rates 100-1000× the background rate. What evidence is MOST directly used to support this claim?',
            'correct': 'Documented extinction rates (extinctions per million species-years) calculated from historical records over the past few centuries are 100-1000× higher than the background rate inferred from the fossil record — this quantitative comparison is the primary evidence, independent of speculative projections',
            'distractors': [
                'The claim is supported by the discovery of an iridium layer in modern sediments, similar to the K-T boundary layer — anthropogenic pollution has produced a chemical signature that matches the asteroid-impact extinctions',
                'The evidence comes from counting the number of endangered species on IUCN red lists — any species listed as "threatened" counts as already extinct for mass extinction calculations',
                'The primary evidence is climate change data alone — since past mass extinctions were caused by climate shifts, the current warming trend definitively proves a sixth mass extinction regardless of actual species loss rates',
            ],
        },
        {
            'question': 'Alfred Wallace, co-discoverer of natural selection, also founded biogeography by noting that Indonesian islands are split into Asian vs Australian faunas by a sharp line (Wallace\'s Line) running through the Lombok Strait. Why is Wallace\'s Line so sharp despite the islands being only ~35 km apart?',
            'correct': 'Wallace\'s Line follows a deep ocean trench that remained flooded even during Pleistocene glacial maxima when sea levels dropped ~120 m — islands to the west were connected to Asia by exposed shelf, islands to the east were connected to Australia, but the deep water in between kept the two faunas geographically isolated throughout their evolutionary history',
            'distractors': [
                'The line follows an invisible magnetic barrier that disorients migrating animals — Asian species cannot sense their way across the Lombok Strait and so never colonized the eastern islands, producing the sharp faunal break',
                'The islands east of Wallace\'s Line have tropical climates while those to the west have temperate climates — the sharp climate difference directly produces the faunal break without any geographic barrier',
                'The line was created by a recent volcanic eruption that eliminated all species in the Lombok Strait region — the sharp break reflects a mass extinction rather than a long-term biogeographic barrier',
            ],
        },
        {
            'question': 'The end-Permian mass extinction (~251 Mya) was the most severe in Earth history, eliminating ~96% of marine species. The leading cause is attributed to massive volcanic eruptions from the Siberian Traps. How did this volcanism trigger such widespread extinction?',
            'correct': 'The Siberian Traps eruptions released enormous quantities of CO2, SO2, and methane over ~1 million years, causing rapid global warming (+10°C), ocean acidification, anoxia in deep waters, and collapse of marine ecosystems — the combined stressors exceeded the adaptive capacity of most species, producing mass extinction far more severe than the better-known K-T impact',
            'distractors': [
                'The Siberian Traps released a cloud of volcanic ash that blocked sunlight globally for ~10 years, killing all photosynthesizing organisms — the mass extinction was purely due to darkness and resulting food-chain collapse, without any climate warming component',
                'The eruptions triggered a chain reaction of mantle plume activity that caused all the continents to split apart simultaneously — the extinction resulted from the physical rearrangement of Earth\'s surface rather than from any chemical or climatic effect',
                'The Siberian Traps deposited iridium globally in the same way as the K-T asteroid, and the mass extinction was actually caused by an unidentified asteroid impact that coincided with the volcanic activity, with the volcanism playing only a minor role',
            ],
        },
        {
            'question': 'Stephen Jay Gould and Niles Eldredge proposed "punctuated equilibrium" in 1972 as an alternative to phyletic gradualism in the fossil record. How does this theory relate to patterns of mass extinction and recovery?',
            'correct': 'Punctuated equilibrium holds that most species exist in long periods of morphological stasis (equilibrium) interrupted by brief episodes of rapid change, often during speciation events — this pattern matches the fossil record after mass extinctions, where vacant niches trigger rapid adaptive radiations (punctuation) that appear geologically instantaneous compared to the long stable periods between extinctions',
            'distractors': [
                'Punctuated equilibrium is a theory of how mass extinctions occur — it proposes that extinctions happen in sudden bursts driven by ecological imbalance, without any external cause like asteroid impacts or volcanism',
                'Punctuated equilibrium is incompatible with mass extinctions because it requires continuous gradual change between major events — the long stasis periods between extinctions disprove Gould and Eldredge\'s theory',
                'Punctuated equilibrium applies only to mollusks studied by Gould, and has no relevance to vertebrate evolution or to patterns of mass extinction and recovery in other taxa',
            ],
        },
    ],
    'conservation': [
        {
            'question': 'A small, isolated population of endangered birds shows high rates of genetic diseases and low reproductive success. The evolutionary diagnosis is:',
            'correct': 'Inbreeding depression — small population size increases homozygosity, exposing deleterious recessive alleles that were previously masked in heterozygotes',
            'distractors': [
                'Genetic drift alone — allele frequency change in small populations necessarily causes disease',
                'Founder effect — the original colonizing population was always genetically compromised',
                'Mutation accumulation — small populations have higher mutation rates than large ones',
            ],
        },
        {
            'question': 'Trophy hunting selectively removes large-horned male bighorn sheep. Over 40 years, average horn size in the population has decreased. This is an example of:',
            'correct': 'Unintentional artificial selection — humans act as a selective force by systematically removing a heritable phenotype, shifting allele frequencies over generations',
            'distractors': [
                'Genetic drift — removal of individuals from small populations always causes random allele frequency change',
                'Phenotypic plasticity — rams produce smaller horns in response to the stress of being hunted',
                'Natural selection — horn size is no longer advantageous in this environment',
            ],
        },
        {
            'question': 'Conservation biologists debate whether to manage populations for maximum genetic diversity or for local adaptation. Which principle underlies this tension?',
            'correct': 'Outbreeding depression — mixing genetically diverged populations can disrupt locally adapted gene combinations, reducing fitness in hybrids despite increasing overall heterozygosity',
            'distractors': [
                'The Hardy-Weinberg principle — gene flow always reduces fitness by changing allele frequencies',
                'Genetic drift — large mixed populations experience stronger drift than small pure ones',
                'Inbreeding depression — all gene mixing is harmful regardless of genetic distance',
            ],
        },
        {
            'question': 'Antibiotic resistance in hospitals evolves rapidly because:',
            'correct': 'Bacteria have short generations, large population sizes, and high mutation rates — strong directional selection on resistance traits can sweep through the population in days',
            'distractors': [
                'Bacteria intentionally mutate to resist antibiotics when threatened',
                'Antibiotics cause the mutations that create resistance',
                'Hospital environments have higher radiation levels that increase bacterial mutation rates',
            ],
        },
        {
            'question': 'The cheetah (Acinonyx jubatus) has extremely low genetic diversity — so low that unrelated cheetahs can accept skin grafts from each other without rejection. This is traced to a population bottleneck ~10,000 years ago. What specific conservation risk does this create?',
            'correct': 'Genetic monomorphism leaves the species vulnerable to novel pathogens — if a single disease emerges that exploits a common allele (e.g., a shared MHC variant), there are no resistant individuals to survive and repopulate. Low genetic diversity also limits the raw material for adaptation to environmental change',
            'distractors': [
                'Low genetic diversity means cheetahs can only breed with close relatives, causing rapid inbreeding depression that will cause extinction within a single generation if conservation efforts cease',
                'Cheetahs have slower reproduction rates than other big cats because low genetic diversity causes meiotic errors in gamete formation — conservation efforts must use artificial insemination to overcome this limitation',
                'The low genetic diversity is actually beneficial — it makes cheetahs more uniform and easier to manage in captivity, and conservation programs should aim to preserve this uniformity rather than introduce new genetic variation',
            ],
        },
        {
            'question': 'Assisted gene flow (deliberately introducing genes from warmer-adapted populations into cooler populations) is being proposed for coral reefs threatened by climate change. What evolutionary principle underlies this strategy?',
            'correct': 'Populations already adapted to warmer conditions carry heat-tolerance alleles that would take many generations to evolve de novo in cooler populations — deliberately transferring these alleles provides genetic material for selection to work on, potentially allowing threatened populations to adapt faster than climate change proceeds',
            'distractors': [
                'Assisted gene flow works by triggering DNA methylation changes that induce heritable phenotypic plasticity — the introduced alleles act as epigenetic switches rather than as standing genetic variation under selection',
                'The strategy relies on the principle that any gene flow, regardless of source, increases adaptive potential — randomly moving individuals from any population into any other will always increase fitness in the recipient population',
                'Assisted gene flow works by creating triploid hybrids that have greater heat tolerance than either parent — the key mechanism is polyploidy rather than the transfer of specific adaptive alleles',
            ],
        },
        {
            'question': 'Phylogenetic diversity (total branch length on a phylogeny) is sometimes used as a conservation priority metric instead of species counts. Why might conserving phylogenetically distinctive lineages (e.g., tuatara, horseshoe crabs, coelacanths) be especially valuable?',
            'correct': 'Phylogenetically distinctive species represent millions of years of unique evolutionary history — they often preserve ancient traits and genes not found elsewhere in living biodiversity; losing them removes entire branches of the tree of life, whereas losing a recently diverged species only removes a twig',
            'distractors': [
                'Phylogenetically distinctive species are always ecologically more important than recently diverged species — they occupy keystone positions in every ecosystem they inhabit because long-lived lineages are automatically dominant',
                'Distinctive lineages have higher extinction risk because they have fewer close relatives that could replace their ecological function — each one\'s extinction automatically triggers cascading ecosystem collapse',
                'Conserving distinct lineages maximizes the rate of future speciation — ancient lineages are more likely to undergo explosive radiations, so preserving them today produces more biodiversity tomorrow than preserving recent species',
            ],
        },
        {
            'question': 'The Florida panther population was nearly extinct by the 1990s with severe genetic defects (kinked tails, heart murmurs, male sterility). In 1995, biologists introduced 8 female Texas cougars to boost genetic diversity. Within a decade, many defects decreased and population size increased. This is an example of:',
            'correct': 'Genetic rescue — introducing individuals from a genetically diverse source population to restore heterozygosity and reduce inbreeding depression in a small isolated population; the introduced alleles mask deleterious recessive mutations and improve fitness',
            'distractors': [
                'Artificial selection — the new cougars were selected for heritable traits missing from the Florida population, and selective breeding produced the observed improvements through directional selection rather than through genetic diversity per se',
                'Species hybridization — Texas cougars and Florida panthers are separate species, and the introduction created an interspecies hybrid population; the Florida panther is now technically extinct and replaced by a hybrid',
                'Outbreeding depression reversal — the Florida population had been suffering from outbreeding depression, and the Texas introduction restored locally adapted alleles that had been lost through excessive gene flow',
            ],
        },
        {
            'question': 'Atlantic cod (Gadus morhua) off Newfoundland collapsed in the 1990s due to overfishing. Decades later, the population has been slow to recover and shows earlier maturation at smaller sizes. How is this an evolutionary phenomenon, not just an ecological one?',
            'correct': 'Intense size-selective harvesting favors individuals that mature early at small sizes (so they can reproduce before being caught) — this creates strong directional selection on maturation timing and body size, and the evolved smaller-maturing phenotype persists even after fishing pressure is reduced because the allele frequencies have shifted',
            'distractors': [
                'The population is slow to recover because fishing accidentally selects for fish that avoid fishing gear — the cod have evolved behavioral intelligence to recognize nets, and fishing is simply less effective than before, rather than the fish being genetically different',
                'The small sizes reflect phenotypic plasticity rather than evolution — cod grow to whatever size food availability allows, and reduced prey populations (not genetic change) cause the observed small mature sizes',
                'Earlier maturation is not an evolutionary response but a random consequence of the population crash — any severely reduced population shows smaller sizes due to founder effects rather than directional selection on maturation',
            ],
        },
        {
            'question': 'The "50/500 rule" in conservation genetics states that a minimum effective population size (Ne) of 50 is needed to prevent short-term inbreeding depression, and 500 is needed to maintain long-term adaptive potential. What is the reasoning behind these specific numbers?',
            'correct': 'Ne=50 corresponds to an inbreeding rate of ~1% per generation, below which deleterious recessives are not exposed too rapidly for selection to purge them; Ne=500 corresponds to the point where new mutations arising at adaptive loci balance the loss of genetic variation through drift, preserving the population\'s ability to respond to environmental change over evolutionary time',
            'distractors': [
                'The 50/500 rule is based on the number of individuals needed to maintain a stable age structure — 50 adults are sufficient for short-term reproduction while 500 individuals are needed to sustain all life-history stages simultaneously across generations',
                'The numbers reflect the IUCN\'s political thresholds for classifying species as endangered or vulnerable — populations below 50 are listed as critically endangered while populations below 500 are listed as vulnerable, without any genetic basis for the specific cutoffs',
                'The 50/500 rule was derived from observations of the minimum number of individuals needed to sustain a successful captive breeding program — 50 founders are needed to start a zoo program while 500 are needed to maintain it indefinitely',
            ],
        },
        {
            'question': 'Trophy hunting of bighorn sheep selectively removes males with the largest horns. Data from Ram Mountain (Alberta) showed that over ~30 years, average horn size declined by ~20% due to evolutionary response. Why does this represent particularly clean evidence of evolution in action on a conservation-relevant timescale?',
            'correct': 'The Ram Mountain study directly tracked individual sheep across generations, documented that horn size was heritable (h² >0), measured the selection differential from hunting kills, and observed the predicted phenotypic decline over time — this matches the quantitative genetic prediction of the breeder\'s equation (R = h²S) exactly, demonstrating that contemporary human activities can drive measurable evolutionary change in wild populations within decades',
            'distractors': [
                'The Ram Mountain data actually support an ecological rather than evolutionary interpretation — the declining horn size reflects reduced nutrition from climate change during the study period, and genetic change has not been demonstrated',
                'The horn size decline is the result of genetic drift alone — Ram Mountain has a small isolated sheep population, and any observed trait change is most parsimoniously explained by drift rather than by selection from hunting',
                'The Ram Mountain data cannot distinguish between evolution and phenotypic plasticity, so the observed decline is not evidence of any specific mechanism — larger sample sizes from multiple populations would be needed to confirm an evolutionary interpretation',
            ],
        },
    ],
    'human-evolution': [
        {
            'question': 'A fossil hominin shows a pelvis adapted for bipedal walking but a brain volume of only 430cc (similar to a chimpanzee). This fossil most likely dates from:',
            'correct': '~3–4 million years ago, consistent with Australopithecus — bipedalism evolved before large brains in our lineage',
            'distractors': [
                '~1.8 million years ago, consistent with Homo erectus, which had both bipedalism and larger brains',
                '~200,000 years ago, consistent with early Homo sapiens with modern brain size',
                'Bipedalism and large brains always evolved together — a small-brained biped is anatomically impossible',
            ],
        },
        {
            'question': 'Genetic evidence shows that modern humans outside Africa carry 1–4% Neanderthal DNA. The BEST interpretation is:',
            'correct': 'Interbreeding occurred between Homo sapiens and Neanderthals after the out-of-Africa migration, before Neanderthal extinction ~40,000 years ago',
            'distractors': [
                'Humans and Neanderthals share a common ancestor within the last 100,000 years — the similarity is recent common ancestry, not hybridization',
                'Modern lab contamination introduced Neanderthal DNA into ancient samples',
                'Neanderthal DNA entered the modern human genome through viral lateral gene transfer',
            ],
        },
        {
            'question': 'The "aquatic ape hypothesis" proposes that human ancestors went through an aquatic phase explaining hairlessness, bipedalism, and fat distribution. Why do most paleoanthropologists reject it?',
            'correct': 'The fossil record places hominins in savanna and woodland environments, not aquatic ones, and each proposed feature has better-supported alternative explanations that do not require an aquatic phase',
            'distractors': [
                'Humans cannot swim, which contradicts the hypothesis',
                'The hypothesis requires Lamarckian inheritance of acquired characters',
                'DNA evidence shows humans are more closely related to savanna mammals than to aquatic mammals',
            ],
        },
        {
            'question': 'Lactase persistence — the ability to digest milk in adulthood — evolved independently in multiple cattle-herding populations in Europe, East Africa, and the Middle East. This is evidence of:',
            'correct': 'Convergent evolution driven by parallel positive selection — the same phenotype (lactase persistence) evolved via different mutations in different populations under the same selective pressure (cattle domestication)',
            'distractors': [
                'Gene flow between cattle-herding populations spread the same allele globally',
                'A single ancestral mutation for lactase persistence predates cattle domestication and was maintained everywhere',
                'Cultural transmission of dairy practices caused genetic changes via Lamarckian inheritance',
            ],
        },
        {
            'question': 'The famous hominin fossil "Lucy" (Australopithecus afarensis, ~3.2 Mya) was discovered in Ethiopia in 1974 by Donald Johanson. Lucy\'s pelvis and femoral angle show clear bipedalism, but her brain was only ~400 cc and she retained curved finger bones suggesting some tree-climbing ability. What does Lucy\'s mosaic morphology tell us about human evolution?',
            'correct': 'Human evolution did not proceed as a simple linear progression toward modern form — different traits evolved at different rates and times. Bipedalism preceded brain expansion, and tree-climbing ability was retained long after bipedalism emerged, showing that hominin evolution was a patchwork of features rather than a coordinated march toward Homo sapiens',
            'distractors': [
                'Lucy proves that all modern human features (bipedalism, large brain, tool use, reduced body hair) evolved simultaneously ~3.2 Mya — the mosaic appearance is an illusion caused by fossil reconstruction errors, and Lucy was essentially anatomically modern',
                'Lucy demonstrates that Australopithecus was actually a dead-end lineage unrelated to modern humans — the mosaic morphology places her outside the hominin line, and she has no descendants among living species',
                'Lucy\'s small brain shows that bipedalism evolved LATER than brain expansion — earlier hominins had large brains but walked on four legs, and Lucy\'s lineage reversed this by shrinking the brain to enable bipedalism',
            ],
        },
        {
            'question': 'Denisovans were identified in 2010 from a single finger bone found in Denisova Cave (Siberia). They are genetically distinct from both Neanderthals and modern humans, but modern Papuans, Melanesians, and some East Asian populations carry ~3-6% Denisovan DNA. What does this pattern tell us about human-Denisovan interactions?',
            'correct': 'Denisovans were a separate hominin population that coexisted with Neanderthals and modern humans, and interbreeding occurred specifically between Denisovans and the ancestors of Papuans and Melanesians — the high Denisovan ancestry in these populations, but not in Europeans or Africans, shows the interbreeding was geographically restricted to Southeast Asia or Oceania',
            'distractors': [
                'Denisovans were the direct ancestors of all modern humans outside Africa — all non-African populations carry Denisovan DNA in proportion to their distance from Africa, with Papuans having the most because they migrated the farthest',
                'Denisovan DNA in modern Papuans entered the human genome through a lab contamination event in the original sequencing — the 3-6% figure is an artifact and Denisovans did not actually interbreed with any modern human population',
                'Denisovan DNA is identical to Neanderthal DNA and the two groups are actually the same species — the geographic distribution of "Denisovan" DNA reflects the range of Neanderthal populations that encountered early Pacific voyagers',
            ],
        },
        {
            'question': 'Homo floresiensis ("the hobbit") was discovered in 2003 on Flores, Indonesia, dating to ~50,000–100,000 years ago. Adults were ~1 m tall with brain volumes of ~420 cc. What evolutionary phenomenon likely explains the small body size of H. floresiensis?',
            'correct': 'Island dwarfism — large-bodied mammals on isolated islands often evolve smaller body sizes due to limited food resources and reduced predation pressure; H. floresiensis is hypothesized to have evolved from Homo erectus or earlier Homo through this common island pattern, losing body mass while maintaining relatively large brain-to-body ratios',
            'distractors': [
                'H. floresiensis was not a new species but rather a diseased individual (microcephalic or pathological dwarf) with extremely unusual development — the small size has no evolutionary significance and does not represent a separate lineage',
                'H. floresiensis evolved small body size through rapid directional selection for tool-making efficiency — smaller hands allowed finer tool manipulation, and this drove the entire body to shrink proportionally',
                'H. floresiensis was a pygmy population of modern Homo sapiens that had undergone extreme inbreeding — their small size reflects loss of growth alleles through genetic drift in a tiny isolated population rather than any specific selection pressure',
            ],
        },
        {
            'question': 'Homo erectus arose ~1.9 Mya, was the first hominin to leave Africa (reaching Asia ~1.8 Mya), and persisted until ~50,000 years ago. What anatomical and behavioral innovations distinguished H. erectus from earlier hominins?',
            'correct': 'H. erectus had a modern human-like body plan (long legs, short arms, relatively large brain ~900 cc), was the first hominin to use fire and make sophisticated Acheulean hand axes, and had the endurance running physiology that enabled long-distance persistence hunting — a combination of features that allowed dispersal across Eurasia',
            'distractors': [
                'H. erectus was the first hominin to evolve a fully modern brain size (~1400 cc) equal to Homo sapiens, and this allowed it to invent symbolic language, art, and agriculture ~1.9 Mya, long before modern humans',
                'H. erectus was primarily characterized by its small size and arboreal lifestyle — unlike earlier hominins, it retreated to the trees and specialized as a fruit eater, which is why it could spread to tropical forests across Asia',
                'H. erectus had a sagittal crest on the skull (a ridge for large jaw muscles) and powerful forelimbs for climbing — its adaptations are consistent with a chimpanzee-like lifestyle rather than with any modern human features',
            ],
        },
        {
            'question': 'The "Out of Africa" model proposes that modern Homo sapiens originated in Africa ~200,000–300,000 years ago and later migrated to replace all other hominin populations globally. What mitochondrial DNA evidence originally supported this model?',
            'correct': '"Mitochondrial Eve" — the most recent common maternal ancestor of all living humans — was traced to Africa ~150,000-200,000 years ago based on mtDNA sequence diversity; African populations also show the greatest mtDNA diversity, consistent with Africa being the ancestral homeland where the lineage has existed longest',
            'distractors': [
                'Mitochondrial DNA from ~200,000-year-old fossils in Europe and Asia matches modern African sequences exactly, proving that African mitochondria replaced all pre-existing European and Asian variants through ancient migration',
                'Mitochondrial "Eve" was a single Homo sapiens woman who lived exactly 200,000 years ago in Africa, and all modern humans are her direct descendants — no other women at her time contributed to the modern human gene pool',
                'The Out of Africa model was supported by the discovery that Neanderthal mitochondrial DNA is identical to modern African mtDNA, proving that Neanderthals were actually Africans who migrated to Europe',
            ],
        },
        {
            'question': 'The hominin lineage is traditionally traced from Ardipithecus (~4.4 Mya) to Australopithecus (e.g., Lucy, ~3.2 Mya) to early Homo (H. habilis, ~2.3 Mya) to H. erectus (~1.9 Mya) to H. sapiens (~200 kya). What best describes the shape of this transition over time?',
            'correct': 'The transition from early hominins to modern humans was not a linear ladder but a bushy tree with multiple contemporaneous species coexisting at various points — Australopithecus and early Homo overlapped, H. erectus overlapped with Neanderthals and H. sapiens, and the direct ancestral line of modern humans is often unclear, with many extinct side branches rather than a single progressive sequence',
            'distractors': [
                'The hominin lineage proceeded as a strict linear progression with each species fully replacing its predecessor — at any given time only one hominin species existed, and each evolved directly into the next without any overlap or side branches',
                'The lineage shows exponentially accelerating morphological change — Ardipithecus and Australopithecus were extremely similar, but each subsequent species shows progressively larger changes, culminating in Homo sapiens as the most derived hominin form',
                'Modern humans are not descended from any of the listed species — H. sapiens evolved from an unknown lineage that is unrelated to Ardipithecus, Australopithecus, or early Homo, and the "hominin transition" is a classification error',
            ],
        },
        {
            'question': 'The obstetrical dilemma proposes that human birth is difficult because of conflicting selection on pelvis width (narrow for bipedalism) and fetal head size (large for brain expansion). Human babies are born relatively altricial (underdeveloped) compared to other primates. How does this relate to the dilemma?',
            'correct': 'The conflict between bipedalism and brain expansion was partially resolved by shifting brain growth from prenatal to postnatal development — human babies are born with ~25% of adult brain size, then complete brain development outside the womb, allowing mothers to give birth before the head becomes too large to fit through the pelvic canal. This extends the period of infant dependency and makes human parenting uniquely prolonged',
            'distractors': [
                'The dilemma was resolved by evolving wider hips in females only — modern women have wider pelvises than men by as much as 50%, fully accommodating even the largest brained babies without any change in birth timing or infant development',
                'The dilemma was resolved when modern medicine began delivering babies by c-section — before surgical intervention, the dilemma produced routine maternal death, and altricial birth is unrelated to the evolutionary response',
                'Human babies are altricial because of reduced nutrient supply to the fetus during pregnancy — mothers cannot absorb enough nutrients to support a fully developed infant, so babies must be born early and continue growing on breastmilk, unrelated to pelvis/head conflict',
            ],
        },
    ],
    'evolutionary-medicine': [
        {
            'question': 'In malaria-endemic regions, the sickle cell allele is maintained at ~10–20% frequency despite causing severe anemia in homozygotes. This is maintained by:',
            'correct': 'Balancing selection via heterozygote advantage — HbS/HbA heterozygotes have ~25% protection against severe malaria, so both alleles are maintained in the population',
            'distractors': [
                'Mutation-selection balance — the sickle cell mutation arises frequently enough to maintain these frequencies despite selection',
                'Genetic drift — the allele is common due to a founder effect in the original African population',
                'Frequency-dependent selection — the allele is rare enough to avoid being selected against',
            ],
        },
        {
            'question': 'Why does the "evolutionary mismatch" hypothesis predict that obesity and type 2 diabetes are more common in modern industrialized populations?',
            'correct': 'Our metabolism evolved under ancestral conditions of food scarcity and high activity; modern environments with calorie abundance and low activity expose a mismatch between our evolved phenotype and current environment',
            'distractors': [
                'Industrialization introduced new genetic mutations that cause metabolic disease',
                'Natural selection has been weakened by modern medicine, allowing disease alleles to accumulate',
                'Evolutionary mismatch refers only to infectious disease — it does not apply to metabolic disease',
            ],
        },
        {
            'question': 'Fever is an evolved immune response. Evolutionary medicine would predict that routinely suppressing fever with antipyretics:',
            'correct': 'Could extend illness duration or severity — if fever is an adaptation that inhibits pathogen replication, suppressing it removes a defense and may give pathogens a replication advantage',
            'distractors': [
                'Has no effect on illness — fever is merely a symptom with no functional role',
                'Always improves outcomes — reducing metabolic costs of fever frees energy for the immune system',
                'Promotes evolution of heat-resistant pathogens within the patient',
            ],
        },
        {
            'question': 'MRSA (methicillin-resistant Staphylococcus aureus) evolved resistance in hospitals partly because:',
            'correct': 'Hospitals create strong directional selection — high antibiotic concentrations kill susceptible strains while resistant mutants survive and reproduce in an environment with many susceptible hosts',
            'distractors': [
                'Hospital patients have weakened immune systems, which causes bacteria to mutate faster',
                'Antibiotic molecules chemically induce resistance mutations in bacterial DNA',
                'Horizontal gene transfer from fungi (which naturally produce antibiotics) transferred resistance genes directly into Staph',
            ],
        },
        {
            'question': 'Morning sickness (nausea and vomiting during early pregnancy) has been proposed as an EVOLVED adaptation, not merely a side effect of hormonal changes. What evolutionary logic supports this interpretation?',
            'correct': 'Morning sickness peaks during the first trimester, exactly when fetal organ development is most sensitive to teratogens and toxins; it causes aversion to strong-smelling or bitter foods (often plants high in toxins or meats at risk of spoilage), potentially protecting the developing fetus from harmful substances during its most vulnerable period',
            'distractors': [
                'Morning sickness is evolved because women who experience it have healthier babies, and this correlation proves it is directly adaptive — pregnancies without morning sickness are invariably less successful regardless of other factors',
                'Morning sickness evolved to signal the pregnancy to male partners so they would bring food — the behavioral signaling function is the primary evolutionary explanation and has been confirmed in cross-cultural studies',
                'Morning sickness is a purely maladaptive response to human pregnancy — it is a byproduct of inefficient hormone regulation that natural selection has not yet eliminated, and has no adaptive value',
            ],
        },
        {
            'question': 'The "hygiene hypothesis" proposes that rising rates of allergies and autoimmune disease in industrialized countries are related to reduced exposure to pathogens and parasites during childhood. How does evolutionary medicine frame this idea?',
            'correct': 'The human immune system evolved in environments rich with parasites (especially helminth worms) and microbial exposure; without these stimuli, immune regulation (especially T-regulatory cells and IgE-mediated responses) becomes dysregulated, producing inappropriate responses to harmless antigens like pollen and self-tissue — another evolutionary mismatch between our evolved physiology and the modern ultra-clean environment',
            'distractors': [
                'The hygiene hypothesis predicts that exposure to ANY bacteria during childhood prevents allergies — antibiotic use specifically causes allergies because it kills all bacteria equally, and restoring any bacterial exposure would prevent autoimmune disease',
                'Rising allergy rates are caused by mutations introduced to human populations through industrialization chemicals — the hygiene hypothesis is incorrect because the real cause is DNA damage rather than immune training',
                'The hygiene hypothesis has been disproven because modern humans have stronger immune systems than ancestral populations — the increase in allergies reflects better diagnosis rather than any real change in disease incidence',
            ],
        },
        {
            'question': 'Aging and senescence are evolutionary puzzles: why would selection allow bodies to deteriorate after reproduction? The "antagonistic pleiotropy" hypothesis proposes one explanation. What is it?',
            'correct': 'Some genes have beneficial effects on fitness early in life (when they increase survival and reproduction) but harmful effects late in life (causing aging-related disease) — because selection acts most strongly on early-life fitness, these genes are favored even though they cause deterioration later, producing senescence as an evolutionary byproduct of early-life benefits',
            'distractors': [
                'Aging evolved as a deliberate adaptation to benefit the species by removing old individuals to make resources available for the young — group selection favors lineages in which individuals age rapidly, since younger members are more fecund',
                'Aging results from the gradual accumulation of random mutations over a lifetime that damage the genome — it is not under selection at all and is simply a physical process that occurs in all complex organisms regardless of evolutionary history',
                'Aging is caused by the deliberate expression of "death genes" that activate after reproduction — these genes are under selection because they prevent elderly individuals from continuing to consume resources after their reproductive value has declined',
            ],
        },
        {
            'question': 'Why does human birth involve an unusually tight fit between the baby\'s head and the mother\'s pelvis compared to other primates, resulting in difficult labor and high historical maternal mortality?',
            'correct': 'The "obstetrical dilemma" — bipedalism selected for narrow pelvises (efficient walking/running) while encephalization (brain expansion) selected for larger fetal heads; these two selective pressures conflict, producing a compromise where human birth is barely feasible and the baby must be born relatively underdeveloped to fit through the birth canal',
            'distractors': [
                'Human birth is difficult because modern obstetric practices have softened selection pressure on birth-canal width — the female pelvis has been narrowing for centuries due to c-sections allowing women with narrow pelvises to reproduce successfully',
                'Tight birth fit is a byproduct of bipedalism alone — the narrowed pelvis required for upright walking simply happened to make birth difficult, and there was no corresponding selection on head size, so the problem is entirely one-sided',
                'Difficult birth in humans is a cultural phenomenon rather than an evolutionary one — in pre-industrial societies without medical intervention, birth is actually easier than in modern settings, showing that the difficulty is not biological',
            ],
        },
        {
            'question': 'Cystic fibrosis is caused by mutations in the CFTR gene. It is fatal without treatment, yet the ΔF508 allele is maintained at ~1 in 25 in European populations. What evolutionary explanation has been proposed?',
            'correct': 'Heterozygote advantage — CF heterozygotes may have had protection against certain ancient diseases (potentially cholera or typhoid fever), because the CFTR protein is involved in chloride/water transport in intestinal epithelium; heterozygotes may have lost less fluid during infection, surviving outbreaks that killed homozygotes without resistance — similar in logic to sickle cell and malaria',
            'distractors': [
                'CF is maintained purely by mutation rate — the ΔF508 mutation arises so frequently that it cannot be purged by selection even though homozygotes die, and the frequency reflects mutation-selection equilibrium alone',
                'CF heterozygotes have no advantage and the ΔF508 allele is actively being removed from European populations — the 1/25 frequency is a transient snapshot and will decline to near-zero over the next few generations',
                'Modern medicine has allowed CF homozygotes to survive and reproduce, so the allele is rising in frequency — the current high frequency reflects recent relaxed selection rather than any past heterozygote advantage',
            ],
        },
        {
            'question': 'Evolutionary medicine organizes disease explanations into four major frameworks: trade-offs, mismatch, arms race, and defenses. Which framework best explains why TYPE 2 DIABETES and OBESITY have become epidemic in modern industrialized societies?',
            'correct': 'MISMATCH — human metabolic physiology evolved under ancestral conditions of food scarcity and high physical activity, favoring "thrifty" genotypes that efficiently stored calories as fat during times of plenty. In modern environments with constant calorie abundance and low activity, those same thrifty genotypes produce obesity and insulin resistance because they are mismatched with the environment they evolved in',
            'distractors': [
                'TRADE-OFFS — type 2 diabetes reflects a trade-off between reproductive success and metabolic health, where alleles favored for early-life reproduction cause metabolic disease in old age through antagonistic pleiotropy; this is the primary explanation regardless of modern environment',
                'ARMS RACE — type 2 diabetes evolved as a defense against bacterial infections in the gut, because high blood glucose kills pathogens; the modern epidemic reflects the cost of this ancient arms race rather than any environmental mismatch',
                'DEFENSES — type 2 diabetes is an evolved defense against toxins, with insulin resistance protecting tissues from glucose-derived damage; the modern epidemic is actually protective, and treating diabetes with insulin paradoxically causes harm by overriding the defense',
            ],
        },
        {
            'question': 'Antibiotic resistance is described as an evolutionary "arms race" between pharmaceutical development and microbial adaptation. Why does this arms race inevitably favor the bacteria over human drug development in the long run?',
            'correct': 'Bacteria evolve far faster than humans can develop drugs — they have generation times of minutes to hours (compared to ~20 years for humans), enormous population sizes (10^11 per gram of feces), high mutation rates, and horizontal gene transfer mechanisms that spread resistance alleles between species. Each new antibiotic triggers rapid resistance evolution, while new drug discovery takes years or decades, creating a permanent evolutionary disadvantage for human medicine',
            'distractors': [
                'Bacteria have a special "resistance gene reservoir" that predates antibiotics — every possible resistance mutation already exists in the environment, so no new antibiotic can work for more than a few months regardless of its mechanism',
                'The arms race is actually balanced because humans have developed antibiotic-conserving protocols that prevent resistance evolution — if doctors use antibiotics correctly, no resistance evolves at all, and the arms race metaphor is inaccurate',
                'Bacteria win the arms race because they are more ancient than humans and have had billions of years to evolve resistance mechanisms that are already pre-adapted to any drug humans could ever invent, regardless of the drug\'s mechanism of action',
            ],
        },
    ],
}

# New row assignments for the final-exam rail
ROW_REASSIGN = {
    'biogeography-extinction':14,
    'conservation':           15,
    'human-evolution':        15,
    'evolutionary-medicine':  15,
}


def final_extras_nodes():
    with open(EXISTING_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    nodes = []
    for n in data['nodes']:
        if n['id'] not in KEEP_IDS:
            continue
        n['row'] = ROW_REASSIGN[n['id']]
        if n['id'] in QUIZ_OVERRIDES:
            n['quiz'] = QUIZ_OVERRIDES[n['id']]
        nodes.append(n)
    return nodes


if __name__ == '__main__':
    ns = final_extras_nodes()
    print(f'Extracted {len(ns)} final-exam extra nodes:')
    for n in ns:
        print(f'  - {n["id"]} (row {n["row"]}, color {n["color"]})')
