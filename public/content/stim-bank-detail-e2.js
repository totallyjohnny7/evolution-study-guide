/* Auto-generated detail-question pack for Exam 2 lectures (L07-L13).
   Drawn only from lecture-guide content. */
(function(){
  var detail = [
    {
      id: "STIM-DTL-L07-001",
      exam: 2,
      lecture: "L07",
      section: "A",
      topic: "Measuring selection in the wild",
      type: "mc",
      difficulty: "application",
      points: 1,
      q: "A researcher records that breeders in a generation have a mean trait value 2.0 mm higher than the population mean, with parent-offspring heritability of h² = 0.5. Using R = h² · S, what is the predicted response in the next generation?",
      choices: [
        "A predicted response of about 1.0 mm in the direction of selection.",
        "A response of approximately 2.0 mm in the same direction as selection.",
        "A response of about 0.5 mm in the opposite direction of selection.",
        "No predicted response because heritability is below 1.0."
      ],
      correct: 0,
      why: "The breeder's equation R = h² · S gives R = 0.5 · 2.0 = 1.0 mm in the direction of selection. The selection differential S is the difference between breeders and the population mean.",
      choice_why: [
        "Correct. R = 0.5 · 2.0 mm = 1.0 mm in the same direction as the selection differential.",
        "Wrong. That would assume h² = 1.0, which is rare for any field trait.",
        "Wrong. The response is in the same direction as S, not opposite, when h² is positive.",
        "Wrong. Any nonzero heritability produces a predicted response; h² need not be 1."
      ],
      source: "detail-extras · L07 §A"
    },
    {
      id: "STIM-DTL-L07-002",
      exam: 2,
      lecture: "L07",
      section: "A",
      topic: "Selection vs. evolutionary response",
      type: "mc",
      difficulty: "synthesis",
      points: 1,
      q: "A field biologist documents that big-billed birds reproduce more than small-billed birds, but never measures heritability. What can the biologist conclude?",
      choices: [
        "Selection is occurring, and an evolutionary response in beak size is also documented.",
        "The data show genetic drift rather than selection on the trait directly.",
        "No selection is happening because heritability of the trait was not measured.",
        "Selection is documented, but the evolutionary response cannot be predicted yet."
      ],
      correct: 3,
      why: "Differential reproduction by trait IS selection, but predicting the next generation requires h². Selection without heritability gives no evolutionary response. The guide explicitly flags this as a trap.",
      choice_why: [
        "Wrong. An evolutionary response is not yet documented without h² and a next-generation measurement.",
        "Wrong. The pattern matches selection, not the random sampling that defines drift.",
        "Wrong. Differential reproduction by trait value IS selection regardless of whether h² was measured.",
        "Correct. Selection is observed; the evolutionary response is not predictable without heritability."
      ],
      source: "detail-extras · L07 §A"
    },
    {
      id: "STIM-DTL-L07-003",
      exam: 2,
      lecture: "L07",
      section: "B",
      topic: "Grants Galápagos finches",
      type: "mc",
      difficulty: "recall",
      points: 1,
      q: "After the 1977 drought on Daphne Major, the Grants documented selection on Geospiza fortis acting in which direction?",
      choices: [
        "Smaller, narrower beaks were favored because soft seeds were the main food.",
        "Beak depth was unaffected — only body size shifted measurably between generations.",
        "Deeper, stronger beaks were favored because hard seeds dominated the food supply.",
        "Selection acted on plumage color rather than beak morphology that year."
      ],
      correct: 2,
      why: "After the 1977 drought, large hard seeds dominated. Birds with deeper, stronger beaks survived better, and the next generation showed measurably deeper beaks — heritable selection in real time.",
      choice_why: [
        "Wrong. Soft seeds were scarce after the drought; large hard seeds dominated the food supply.",
        "Wrong. Beak depth was the trait under selection and changed measurably across one generation.",
        "Correct. The Grants documented selection for deeper beaks following the drought of 1977.",
        "Wrong. The lecture frames the case as selection on beak depth, not plumage."
      ],
      source: "detail-extras · L07 §B"
    },
    {
      id: "STIM-DTL-L07-004",
      exam: 2,
      lecture: "L07",
      section: "B",
      topic: "Reversal of selection",
      type: "mc",
      difficulty: "synthesis",
      points: 1,
      q: "In subsequent wet years on Daphne Major, the Grants observed what pattern relative to the post-1977 drought selection?",
      choices: [
        "Selection continued to push beak depth higher in every generation studied.",
        "Selection pressure reversed — smaller seeds became favored and the trend in beak depth flipped.",
        "Hybridization wiped out heritability, so no evolutionary change was detectable.",
        "The population went extinct and could not be tracked across the wet years."
      ],
      correct: 1,
      why: "Wet years restored small-seed availability and reversed the selective pressure on beak depth. The lecture flags this as evidence that selection direction is environment-contingent.",
      choice_why: [
        "Wrong. The selection direction reversed once seed availability shifted.",
        "Correct. In wet years, smaller seeds returned and selection favored smaller beaks.",
        "Wrong. Hybridization introduced variation; it did not zero out heritability.",
        "Wrong. The population persisted; the long-term study continued for decades."
      ],
      source: "detail-extras · L07 §B"
    },
    {
      id: "STIM-DTL-L07-005",
      exam: 2,
      lecture: "L07",
      section: "C",
      topic: "Industrial melanism mechanism",
      type: "mc",
      difficulty: "application",
      points: 1,
      q: "In Biston betularia, the rise of dark (melanic) morphs to >95% in polluted regions during the Industrial Revolution was driven by which mechanism?",
      choices: [
        "Direct toxic effects of soot mutating the cortex gene in resting moths.",
        "Random genetic drift across small isolated woodland populations of the moths.",
        "A pheromone shift in melanic moths that increased mating success markedly.",
        "Differential bird predation on the more visible morph against darkened tree trunks."
      ],
      correct: 3,
      why: "The lecture states the selective agent is bird predation on resting moths against bark; pollution killed lichen and blackened trunks, making light morphs visible. Melanic morphs gained a survival edge.",
      choice_why: [
        "Wrong. Pollution did not mutate moths; the genetic basis is a transposon insertion in cortex selected from existing variation.",
        "Wrong. The frequency change was directional and rapid across regions — the signature of selection, not drift.",
        "Wrong. The lecture frames this as survival selection by predators, not mate-choice or pheromone selection.",
        "Correct. Bird predation on visible morphs against darkened bark is the documented selective agent."
      ],
      source: "detail-extras · L07 §C"
    },
    {
      id: "STIM-DTL-L07-006",
      exam: 2,
      lecture: "L07",
      section: "C",
      topic: "Genetic basis of melanism",
      type: "mc",
      difficulty: "recall",
      points: 1,
      q: "The genetic basis of industrial melanism in the peppered moth has been traced to:",
      choices: [
        "A point mutation in a melanin biosynthesis enzyme on the X chromosome.",
        "A regulatory change at a Hox locus controlling wing pigmentation patterns.",
        "A transposon insertion in the cortex gene that alters wing-color development.",
        "Loss-of-function alleles at a circadian rhythm gene used in roost selection."
      ],
      correct: 2,
      why: "The lecture identifies a transposon insertion in the cortex gene as the molecular basis of industrial melanism in Biston betularia.",
      choice_why: [
        "Wrong. The lecture cites a transposon insertion, not a melanin-enzyme point mutation.",
        "Wrong. Hox genes pattern body axes, not the moth wing-pigment switch in this case.",
        "Correct. A transposon insertion in cortex is the documented molecular basis.",
        "Wrong. Circadian genes are not implicated in industrial melanism in the lecture."
      ],
      source: "detail-extras · L07 §C"
    },
    {
      id: "STIM-DTL-L07-007",
      exam: 2,
      lecture: "L07",
      section: "C",
      topic: "Reversal after clean-air laws",
      type: "mc",
      difficulty: "synthesis",
      points: 1,
      q: "After mid-twentieth-century clean-air legislation, what happened to peppered moth morph frequencies?",
      choices: [
        "Both morphs converged to a new intermediate gray phenotype after the cleanup.",
        "The melanic morph fixed at near-100% because dark coloration is dominant.",
        "The light morph rebounded as lichen returned and bark again favored cryptic light wings.",
        "Selection on coloration ceased and morph frequencies became neutral and random."
      ],
      correct: 2,
      why: "After clean-air laws reduced soot, lichen returned to trunks and the light morph again had the camouflage advantage. Selection direction reversed and the light morph rebounded.",
      choice_why: [
        "Wrong. The system flipped between two morphs, not toward an intermediate.",
        "Wrong. The melanic morph declined as the environmental advantage disappeared.",
        "Correct. Lichen returned, bark lightened, and selection again favored the light morph.",
        "Wrong. Selection continued to act; only its direction changed with the environment."
      ],
      source: "detail-extras · L07 §C"
    },
    {
      id: "STIM-DTL-L07-008",
      exam: 2,
      lecture: "L07",
      section: "D",
      topic: "Antibiotic resistance misconception",
      type: "mc",
      difficulty: "application",
      points: 1,
      q: "Which statement about antibiotic resistance is consistent with the lecture's framing?",
      choices: [
        "Resistance mutations occur randomly; antibiotics select pre-existing resistant variants.",
        "Antibiotic exposure directly mutates bacteria into resistant strains.",
        "Bacteria sense the antibiotic and intentionally produce a resistant offspring lineage.",
        "Resistance is a Lamarckian acquired trait passed on through use of resistant proteins."
      ],
      correct: 0,
      why: "The exam-trap section is explicit: antibiotics do NOT cause the mutations. Mutations occur randomly; the antibiotic selects from existing variants. This is a textbook case of strong directional natural selection by humans.",
      choice_why: [
        "Correct. The mutations preexist; the antibiotic acts as the selective agent.",
        "Wrong. The antibiotic does not mutate the bacteria — that misconception is flagged as a trap.",
        "Wrong. Bacteria do not direct mutations toward useful outcomes; this misreads the mechanism.",
        "Wrong. Lamarckian inheritance of acquired traits is not the mechanism for antibiotic resistance."
      ],
      source: "detail-extras · L07 §D"
    },
    {
      id: "STIM-DTL-L07-009",
      exam: 2,
      lecture: "L07",
      section: "D",
      topic: "Artificial vs. natural selection",
      type: "mc",
      difficulty: "synthesis",
      points: 1,
      q: "According to the lecture, the difference between artificial selection (e.g., greyhound breeding for speed) and natural selection is best described as:",
      choices: [
        "Artificial selection is faster because it operates on heritable variation, while natural selection does not.",
        "Artificial selection produces evolutionary change; natural selection produces only short-term variation.",
        "Both follow the same logic of differential reproduction; only the agent doing the selecting differs.",
        "Artificial selection violates the laws of inheritance because human choice overrides genetics."
      ],
      correct: 2,
      why: "The lecture states explicitly that artificial selection follows the same logic as natural selection — the only difference is who or what is doing the selecting. Both require heritable variation plus differential reproduction.",
      choice_why: [
        "Wrong. Both rely on heritable variation; that is not what distinguishes them.",
        "Wrong. Both produce real evolutionary change documented across generations.",
        "Correct. The selecting agent differs (human vs. environment); the underlying logic is identical.",
        "Wrong. Artificial selection works through normal Mendelian inheritance with humans choosing breeders."
      ],
      source: "detail-extras · L07 §D"
    },
    {
      id: "STIM-DTL-L07-010",
      exam: 2,
      lecture: "L07",
      section: "D",
      topic: "Influenza antigenic variation",
      type: "mc",
      difficulty: "recall",
      points: 1,
      q: "Influenza evolves rapidly under which selective pressures, according to the lecture?",
      choices: [
        "Random drift in small founder populations carried between continents annually.",
        "Selection from host immune systems and (where used) antiviral drug exposure.",
        "Direct mutagenesis induced by host body temperature elevations during fever.",
        "Bottleneck-driven loss of antigenic diversity during transmission to children."
      ],
      correct: 1,
      why: "The lecture frames influenza as a real-time test of selection: antigenic variation is driven by host immune systems and antiviral drugs. Same structural argument as antibiotic resistance — heritable variation plus strong directional selection.",
      choice_why: [
        "Wrong. Drift cannot explain the consistent directional antigenic change documented in flu.",
        "Correct. Host immunity and antiviral drugs are the cited selective forces in the lecture.",
        "Wrong. Fever does not act as a directed mutagen; selection acts on existing variation.",
        "Wrong. Bottlenecks reduce diversity but do not produce the antigenic shift pattern."
      ],
      source: "detail-extras · L07 §D"
    },
    {
      id: "STIM-DTL-L08-001",
      exam: 2,
      lecture: "L08",
      section: "A",
      topic: "Adaptation as noun and verb",
      type: "mc",
      difficulty: "recall",
      points: 1,
      q: "In the lecture's definition, the word \"adaptation\" carries which two distinct senses?",
      choices: [
        "A trait shaped by past selection (noun) AND the process by which selection produces such traits.",
        "An ecological niche (noun) AND a behavior changing within an individual's lifetime.",
        "A heritable allele (noun) AND any phenotype produced by environmental induction.",
        "A perfectly optimal trait (noun) AND a trait that is fixed in a population."
      ],
      correct: 0,
      why: "The lecture explicitly defines adaptation in two senses: (1) noun — a heritable trait shaped by past selection in service of some function; (2) verb — the process by which selection improves fit between organism and environment.",
      choice_why: [
        "Correct. The two textbook senses, drawn directly from the lecture.",
        "Wrong. Adaptation is not equated with niche, and within-lifetime change is acclimation, not evolutionary adaptation.",
        "Wrong. Phenotypic plasticity is distinct from evolutionary adaptation in this lecture.",
        "Wrong. The lecture warns against treating adaptations as optimal; they are usually \"good enough.\""
      ],
      source: "detail-extras · L08 §A"
    },
    {
      id: "STIM-DTL-L08-002",
      exam: 2,
      lecture: "L08",
      section: "A",
      topic: "The \"half an eye\" objection",
      type: "mc",
      difficulty: "synthesis",
      points: 1,
      q: "The classic creationist objection that \"half an eye is useless\" is countered in the lecture by which point?",
      choices: [
        "Modern eye anatomy proves a designed origin once developmental biology is understood.",
        "Eyes appear suddenly in the fossil record so half-formed stages do not exist anywhere.",
        "Eye intermediates are simpler light-detecting structures with their own functional value.",
        "Selection planned ahead for a complete vertebrate eye over evolutionary time scales."
      ],
      correct: 2,
      why: "The lecture is explicit: early eyes are not failed full eyes — they are simpler structures (light patches, cups) with their own selective value. Each intermediate stage must itself be functional, since selection cannot plan ahead.",
      choice_why: [
        "Wrong. Modern eye anatomy is consistent with stepwise evolution, not design.",
        "Wrong. Living organisms today exhibit the intermediate stages — they are not hypothetical.",
        "Correct. Each intermediate is itself useful; that is the canonical answer.",
        "Wrong. Selection cannot plan ahead — that is exactly the misconception flagged."
      ],
      source: "detail-extras · L08 §A,B"
    },
    {
      id: "STIM-DTL-L08-003",
      exam: 2,
      lecture: "L08",
      section: "B",
      topic: "Stepwise eye evolution",
      type: "mc",
      difficulty: "application",
      points: 1,
      q: "In the gradual stepwise eye-evolution model, the addition of a CUP shape to a light-sensitive patch primarily provides which new capability?",
      choices: [
        "Image-forming acuity at high spatial resolution comparable to camera optics.",
        "Color discrimination via opsin diversification in the retina of the cup wall.",
        "Directional sensitivity — detection of WHERE the light is coming from.",
        "Focused image formation through a flexible lens of crystallin proteins."
      ],
      correct: 2,
      why: "Stage 2 in the lecture is the cupped patch, which adds directional sensitivity. Image formation requires later stages (pinhole, lens). Color discrimination is a separate axis.",
      choice_why: [
        "Wrong. High-acuity image formation comes only after pinhole and lens stages.",
        "Wrong. Color discrimination depends on opsin diversity, not on cup shape.",
        "Correct. The cup adds directional information about the light source.",
        "Wrong. Focused images require a lens, which appears later in the stepwise sequence."
      ],
      source: "detail-extras · L08 §B"
    },
    {
      id: "STIM-DTL-L08-004",
      exam: 2,
      lecture: "L08",
      section: "B",
      topic: "Convergent eye evolution",
      type: "mc",
      difficulty: "synthesis",
      points: 1,
      q: "According to the lecture, the camera eye of vertebrates and the camera eye of cephalopods (e.g., octopus) are best described as:",
      choices: [
        "Homologous structures inherited from a common ancestor with eyes.",
        "Examples of group selection acting at the level of vision systems in oceans.",
        "Vestigial copies of an ancient single-celled photoreceptor structure.",
        "Convergent solutions that evolved independently to a common selective problem."
      ],
      correct: 3,
      why: "Eyes have evolved INDEPENDENTLY at least 40 times across animals — the vertebrate and cephalopod camera eyes are convergent, not homologous. Same selective problem, similar solution from different starting points.",
      choice_why: [
        "Wrong. The lecture explicitly says they are convergent, not homologous.",
        "Wrong. Group selection is unrelated to convergent eye evolution.",
        "Wrong. Vestigial means lost function; these eyes are highly functional.",
        "Correct. Independent origin to a common functional challenge — the textbook example."
      ],
      source: "detail-extras · L08 §B"
    },
    {
      id: "STIM-DTL-L08-005",
      exam: 2,
      lecture: "L08",
      section: "C",
      topic: "Cis-regulatory evolution",
      type: "mc",
      difficulty: "synthesis",
      points: 1,
      q: "A change in an ENHANCER region of a Hox gene shifts that gene's expression to a new body segment, producing a novel morphology. This is best described as:",
      choices: [
        "A cis-regulatory mutation that alters when/where a gene is expressed without changing the protein.",
        "Neofunctionalization of a duplicated gene through new amino-acid substitutions occurring rapidly.",
        "Heterochrony, since timing of development is what enhancers always control specifically.",
        "A vestigial structure resulting from relaxed selection on the regulatory locus over generations."
      ],
      correct: 0,
      why: "Cis-regulatory mutations alter the expression pattern (when and where) of an unchanged protein. The lecture flags this as a major route to morphological novelty — Hox-gene expression changes reshape body plans without changing the Hox proteins themselves.",
      choice_why: [
        "Correct. Enhancer changes alter expression without altering the protein product.",
        "Wrong. Neofunctionalization involves duplication and protein-level change, not just an enhancer shift.",
        "Wrong. Heterochrony is timing change in development; enhancers can shift more than timing.",
        "Wrong. A vestigial structure is a phenotypic outcome, not a regulatory mechanism."
      ],
      source: "detail-extras · L08 §C"
    },
    {
      id: "STIM-DTL-L08-006",
      exam: 2,
      lecture: "L08",
      section: "C",
      topic: "Sub- vs. neofunctionalization",
      type: "mc",
      difficulty: "application",
      points: 1,
      q: "A gene duplicates. One copy retains its ancestral function unchanged, while the other evolves a novel function never present in the ancestor. This is:",
      choices: [
        "Subfunctionalization, in which each copy splits a portion of the original function.",
        "Heterochrony, in which the timing of expression has been pushed earlier or later.",
        "Neofunctionalization — one copy gains a new function while the other retains the original.",
        "Protein promiscuity within a single locus over evolutionary timescales of selection."
      ],
      correct: 2,
      why: "Neofunctionalization: one copy retains the original function; the other evolves a novel role. Subfunctionalization is when both copies specialize on different SUBSETS of the ancestral function. The lecture explicitly contrasts these.",
      choice_why: [
        "Wrong. Subfunctionalization splits the original role between copies; neither has a new function.",
        "Wrong. Heterochrony refers to developmental-timing changes, not duplicate-gene fates.",
        "Correct. New function in one copy, original retained in the other — neofunctionalization.",
        "Wrong. Promiscuity is a property of single proteins with weak side activities, not duplicates."
      ],
      source: "detail-extras · L08 §C"
    },
    {
      id: "STIM-DTL-L08-007",
      exam: 2,
      lecture: "L08",
      section: "D",
      topic: "Heterochrony — paedomorphosis",
      type: "mc",
      difficulty: "recall",
      points: 1,
      q: "The axolotl salamander reproduces while still in larval form. The lecture cites this as a textbook example of:",
      choices: [
        "Paedomorphosis — retention of juvenile features in the adult reproductive form.",
        "Peramorphosis, the extension of growth past the ancestral end-point in the lineage.",
        "Heterotopy, in which a developmental process shifts to a new body location.",
        "Subfunctionalization of a gene controlling thyroid hormone metabolism in the species."
      ],
      correct: 0,
      why: "Paedomorphosis = retention of juvenile features in the adult form. The axolotl is the lecture's named example. Peramorphosis is the opposite — extension of development past the ancestral state.",
      choice_why: [
        "Correct. The axolotl retains larval features as a sexually mature adult.",
        "Wrong. Peramorphosis is extension past the ancestral end-point — large antlers in the lecture.",
        "Wrong. Heterotopy is change in location of development, not retention of juvenile features.",
        "Wrong. The phenomenon is morphological, not described as gene subfunctionalization."
      ],
      source: "detail-extras · L08 §D"
    },
    {
      id: "STIM-DTL-L08-008",
      exam: 2,
      lecture: "L08",
      section: "E",
      topic: "Hox colinearity",
      type: "mc",
      difficulty: "synthesis",
      points: 1,
      q: "The principle of COLINEARITY in Hox gene clusters refers to:",
      choices: [
        "The fact that Hox proteins all bind the same DNA target sequence in any species.",
        "A gradient of Hox protein concentrations from anterior to posterior in vertebrates only.",
        "The conservation of Hox amino-acid sequences across distantly related animal phyla.",
        "A correspondence between Hox gene chromosomal order and their expression order along the body axis."
      ],
      correct: 3,
      why: "Colinearity means the chromosomal order of Hox genes mirrors their expression order along the anterior-posterior axis of the developing animal. It is one of the iconic features of the Hox cluster.",
      choice_why: [
        "Wrong. Different Hox proteins bind related but distinguishable target sequences.",
        "Wrong. Concentration gradients are not the technical definition of colinearity in the lecture.",
        "Wrong. Sequence conservation across phyla is a separate (also true) Hox feature.",
        "Correct. Colinearity = chromosomal order maps onto body-axis expression order."
      ],
      source: "detail-extras · L08 §E"
    },
    {
      id: "STIM-DTL-L08-009",
      exam: 2,
      lecture: "L08",
      section: "E",
      topic: "Hox cluster duplications",
      type: "mc",
      difficulty: "recall",
      points: 1,
      q: "How many Hox clusters does the typical vertebrate genome have, compared to the typical invertebrate genome?",
      choices: [
        "Vertebrates have 1 Hox cluster; invertebrates have 4 in nearly all species.",
        "Vertebrates have 4 Hox clusters; invertebrates typically have 1 cluster.",
        "Vertebrates and invertebrates each have 8 Hox clusters in the genomes overall.",
        "Vertebrates have 2 Hox clusters; invertebrates lack Hox genes entirely."
      ],
      correct: 1,
      why: "The lecture states the vertebrate genome has 4 Hox clusters and invertebrates typically have 1. Hox-cluster duplications correlate with major body-plan transitions.",
      choice_why: [
        "Wrong. The numbers are reversed in this distractor.",
        "Correct. The 4-vs-1 contrast is given directly in the lecture.",
        "Wrong. No animals have 8 Hox clusters according to the lecture.",
        "Wrong. Invertebrates do have Hox genes — typically organized in a single cluster."
      ],
      source: "detail-extras · L08 §E"
    },
    {
      id: "STIM-DTL-L08-010",
      exam: 2,
      lecture: "L08",
      section: "F",
      topic: "Imperfect adaptation",
      type: "mc",
      difficulty: "synthesis",
      points: 1,
      q: "The vertebrate retina has its photoreceptors oriented \"backwards\" — light passes through neurons before reaching them. The lecture cites this as evidence for:",
      choices: [
        "A designed system optimized for night-vision performance in vertebrate ancestors.",
        "A historical accident reflecting evolutionary constraint, not design or optimization.",
        "Strong recent positive selection that produced an optimal optical configuration.",
        "A textbook example of mutation-accumulation theory of senescence acting on the eye."
      ],
      correct: 1,
      why: "The inverted retina is a constraint imposed by developmental history — selection works on what is already there. The lecture frames imperfections (blind spot, inverted retina, vestigial structures) as powerful evidence of evolution by descent.",
      choice_why: [
        "Wrong. A designed system would not include a blind spot — that is the lecture's point.",
        "Correct. Historical contingency, not optimization, explains the orientation.",
        "Wrong. The orientation is a frozen accident from ancestry, not a recent optimum.",
        "Wrong. Mutation-accumulation theory belongs to senescence, not retinal architecture."
      ],
      source: "detail-extras · L08 §F"
    },
    {
      id: "STIM-DTL-L09-001",
      exam: 2,
      lecture: "L09",
      section: "A",
      topic: "Defining reciprocal coevolution",
      type: "mc",
      difficulty: "recall",
      points: 1,
      q: "Which is the lecture's definition of TRUE coevolution between two species?",
      choices: [
        "Any two species that share an ecological habitat over many generations of contact.",
        "Convergent evolution of similar traits in unrelated lineages with similar lifestyles.",
        "Reciprocal evolutionary change in interacting lineages, each responding to selection from the other.",
        "A single lineage adapting to a stable abiotic environment over geological time scales."
      ],
      correct: 2,
      why: "The lecture defines coevolution as RECIPROCAL evolutionary change — selection from one species drives change in the other, which in turn drives further change in the first. Mere coexistence or convergence does not qualify.",
      choice_why: [
        "Wrong. Mere ecological association is not coevolution; reciprocal feedback is required.",
        "Wrong. Convergent evolution lacks reciprocal feedback between lineages.",
        "Correct. Reciprocal evolutionary feedback — the textbook definition.",
        "Wrong. Adaptation to abiotic environment is not coevolution at all."
      ],
      source: "detail-extras · L09 §A"
    },
    {
      id: "STIM-DTL-L09-002",
      exam: 2,
      lecture: "L09",
      section: "B",
      topic: "Newt-snake TTX arms race",
      type: "mc",
      difficulty: "application",
      points: 1,
      q: "In the rough-skinned newt (Taricha) and garter snake (Thamnophis) system, the molecular target of newt tetrodotoxin (TTX) and the locus of snake resistance is:",
      choices: [
        "A G-protein coupled receptor in the snake olfactory epithelium that detects the toxin.",
        "A sodium channel mutation in cardiac muscle reducing TTX uptake during digestion only.",
        "Voltage-gated sodium channels — TTX blocks them; resistant snakes carry altered channels.",
        "A cytochrome P450 detoxification enzyme broadly induced by TTX exposure in snake liver."
      ],
      correct: 2,
      why: "TTX blocks voltage-gated sodium channels — the lecture's key term explicitly defines TTX as a \"potent neurotoxin produced by newts that blocks voltage-gated sodium channels.\" Garter snakes evolve TTX-resistant sodium channels.",
      choice_why: [
        "Wrong. The mechanism is at sodium channels, not olfactory receptors.",
        "Wrong. TTX blocks voltage-gated sodium channels in nerves and muscle, not via cardiac uptake only.",
        "Correct. Voltage-gated sodium channels are the molecular battleground of this arms race.",
        "Wrong. The lecture cites sodium-channel resistance, not detoxification enzymes."
      ],
      source: "detail-extras · L09 §B"
    },
    {
      id: "STIM-DTL-L09-003",
      exam: 2,
      lecture: "L09",
      section: "B",
      topic: "Geographic signature of arms races",
      type: "mc",
      difficulty: "synthesis",
      points: 1,
      q: "Which observation is highlighted as KEY EVIDENCE for an ongoing coevolutionary arms race rather than a fixed end-state adaptation?",
      choices: [
        "Uniform \"one-size-fits-all\" adaptation across the entire range of both species involved.",
        "Identical mutation rates in the two species across all populations under selection.",
        "Complete extinction of one partner shortly after the arms race begins in any region.",
        "Geographic variation — where snakes are highly resistant, newts are highly toxic, and vice versa."
      ],
      correct: 3,
      why: "The lecture flags geographic covariation — local toxicity matched to local resistance — as the diagnostic signature of ongoing coevolution. Uniformity argues against current arms-race dynamics.",
      choice_why: [
        "Wrong. Uniform traits argue AGAINST current reciprocal feedback.",
        "Wrong. Mutation rates per se are not the diagnostic the lecture emphasizes.",
        "Wrong. Extinction is not the expected outcome and is not what diagnoses ongoing coevolution.",
        "Correct. Local matched escalation is the hallmark of an active arms race."
      ],
      source: "detail-extras · L09 §B"
    },
    {
      id: "STIM-DTL-L09-004",
      exam: 2,
      lecture: "L09",
      section: "C",
      topic: "Darwin's long-spurred orchid",
      type: "mc",
      difficulty: "synthesis",
      points: 1,
      q: "Darwin famously predicted the existence of a long-tongued moth pollinator after observing a Madagascan orchid with an extraordinarily long spur. This case illustrates:",
      choices: [
        "Mutualistic coevolution: co-adapted morphology in pollinator and plant for joint benefit.",
        "Antagonistic coevolution between predators and prey involving lethal toxicity defenses.",
        "Naïve group selection acting on populations of orchids over generations of pollinator decline.",
        "Cryptic female choice in the orchid biased through the floral tube reproductive geometry."
      ],
      correct: 0,
      why: "The lecture cites Darwin's orchid as a classic mutualistic coevolution case: a long spur and a long-tongued moth co-adapt to a shared pollination interaction. Both partners gain net fitness.",
      choice_why: [
        "Correct. Co-adapted morphology between mutualists is the textbook framing.",
        "Wrong. Pollination here is mutualistic, not antagonistic.",
        "Wrong. Group selection is not invoked; reciprocal selection between species is.",
        "Wrong. Cryptic female choice is a sexual-selection concept from the sex lecture, not pollination."
      ],
      source: "detail-extras · L09 §C"
    },
    {
      id: "STIM-DTL-L09-005",
      exam: 2,
      lecture: "L09",
      section: "C",
      topic: "Endosymbiosis",
      type: "mc",
      difficulty: "recall",
      points: 1,
      q: "According to the lecture, mitochondria descend from which ancestral lineage and represent which kind of interaction?",
      choices: [
        "Cyanobacteria; an ancient antagonistic predator-prey arms race that became mutualistic.",
        "Alphaproteobacteria; the deepest mutualism, now obligate, between host cell and partner.",
        "Spirochetes; a Batesian mimicry between flagellated cells and the eukaryotic cytoskeleton.",
        "Archaeal lineages; a Müllerian mimicry of metabolic roles among eukaryotic organelles."
      ],
      correct: 1,
      why: "The lecture states mitochondria came from ancestral alphaproteobacteria and chloroplasts from cyanobacteria. Endosymbiosis is framed as the deepest mutualism — now obligate.",
      choice_why: [
        "Wrong. Cyanobacteria gave rise to chloroplasts, not mitochondria.",
        "Correct. Mitochondria from alphaproteobacteria; classic obligate mutualism.",
        "Wrong. Spirochetes/Batesian mimicry is unrelated to organelle origins.",
        "Wrong. Archaea/Müllerian mimicry is not the lecture's framing of organelles."
      ],
      source: "detail-extras · L09 §C"
    },
    {
      id: "STIM-DTL-L09-006",
      exam: 2,
      lecture: "L09",
      section: "D",
      topic: "Batesian vs. Müllerian",
      type: "mc",
      difficulty: "application",
      points: 1,
      q: "A harmless hoverfly evolves yellow-and-black banding that closely resembles a stinging wasp. Predators avoid both. This is best described as:",
      choices: [
        "Müllerian mimicry — multiple harmful species converging on a shared warning signal jointly.",
        "Convergent evolution without coevolutionary feedback between any of the species involved.",
        "Aposematism alone, since the bands themselves are simply warning coloration of toxic species.",
        "Batesian mimicry — a palatable mimic resembling an unpalatable model for protection."
      ],
      correct: 3,
      why: "A harmless mimic gaining protection from a harmful model is BATESIAN mimicry. The mimic must stay rare, or predators learn the trick. Müllerian mimicry involves multiple HARMFUL species sharing a warning signal.",
      choice_why: [
        "Wrong. Müllerian requires the mimic itself to be harmful; the hoverfly is harmless.",
        "Wrong. The hoverfly's pattern is shaped by the wasp's presence — that's coevolution.",
        "Wrong. The hoverfly is not toxic; aposematism alone does not capture mimicry.",
        "Correct. Harmless mimic on harmful model is the Batesian case."
      ],
      source: "detail-extras · L09 §D"
    },
    {
      id: "STIM-DTL-L09-007",
      exam: 2,
      lecture: "L09",
      section: "D",
      topic: "Frequency-dependence in mimicry",
      type: "mc",
      difficulty: "synthesis",
      points: 1,
      q: "Batesian mimicry breaks down at HIGH ratios of mimics to models because:",
      choices: [
        "Mimics begin to physically resemble the model species too perfectly across multiple traits.",
        "The toxic model evolves novel coloration that the mimic cannot quickly track in evolution.",
        "Predators encounter the harmless mimic too often and stop avoiding the warning signal.",
        "Group selection on mimic populations begins to overwhelm individual-level mimicry benefits."
      ],
      correct: 2,
      why: "When mimics become too common, predators sample many palatable individuals and learn that the warning signal is unreliable. Batesian mimicry requires the mimic to remain rare — frequency-dependent selection.",
      choice_why: [
        "Wrong. Better resemblance helps mimicry, not hurts it; frequency is the issue.",
        "Wrong. The model evolving away is a different (slower) failure mode than frequency.",
        "Correct. Mimic frequency is the limit; predators learn the signal is no longer reliable.",
        "Wrong. Individual-level frequency-dependent selection is the operative force, not group selection."
      ],
      source: "detail-extras · L09 §D"
    },
    {
      id: "STIM-DTL-L09-008",
      exam: 2,
      lecture: "L09",
      section: "E",
      topic: "Geographic Mosaic Theory",
      type: "mc",
      difficulty: "recall",
      points: 1,
      q: "Whose framework proposes that coevolution proceeds at different rates in different places, producing \"hotspots\" and \"coldspots\"?",
      choices: [
        "Maynard Smith's Geographic Mosaic Theory of Coevolution and adaptive landscapes.",
        "Hamilton's Geographic Mosaic Theory of Coevolution across spatially structured populations.",
        "Thompson's Geographic Mosaic Theory of Coevolution across a species' geographic range.",
        "Trivers's Geographic Mosaic Theory of Coevolution within social mating systems."
      ],
      correct: 2,
      why: "The lecture attributes the Geographic Mosaic Theory of Coevolution to Thompson. It predicts trait mismatch in some areas — evidence FOR ongoing coevolution, not against it.",
      choice_why: [
        "Wrong. Maynard Smith is associated with ESS and the cost of sex, not the mosaic theory.",
        "Wrong. Hamilton is the inclusive-fitness theorist, not the mosaic-theory architect.",
        "Correct. Thompson is the named author of the Geographic Mosaic Theory of Coevolution.",
        "Wrong. Trivers worked on parental investment and reciprocal altruism, not mosaic theory."
      ],
      source: "detail-extras · L09 §E"
    },
    {
      id: "STIM-DTL-L09-009",
      exam: 2,
      lecture: "L09",
      section: "E",
      topic: "Mosaic mismatch",
      type: "mc",
      difficulty: "synthesis",
      points: 1,
      q: "A predicted population shows mismatched coevolutionary traits — strong defense by prey but weak counter-offense by predators. According to mosaic theory, this is:",
      choices: [
        "Expected — local mismatch is part of the mosaic and supports rather than refutes coevolution.",
        "Evidence against any reciprocal coevolution between these populations of predators and prey.",
        "A signal that the predator should soon go extinct in this region of the geographic range.",
        "Proof that group selection at the level of communities is the dominant evolutionary force here."
      ],
      correct: 0,
      why: "Mosaic theory specifically predicts mismatch in some places — gene flow between hotspots and coldspots, plus local trait evolution, generates spatially variable trait combinations. Mismatch is evidence FOR ongoing coevolution.",
      choice_why: [
        "Correct. Local mismatch is a hallmark of the geographic mosaic.",
        "Wrong. Mismatch is predicted by the theory, not contrary to it.",
        "Wrong. Mismatch does not predict imminent extinction in mosaic theory.",
        "Wrong. Mosaic theory is built on individual-level reciprocal selection, not group selection."
      ],
      source: "detail-extras · L09 §E"
    },
    {
      id: "STIM-DTL-L09-010",
      exam: 2,
      lecture: "L09",
      section: "C",
      topic: "Mutualism stability",
      type: "mc",
      difficulty: "application",
      points: 1,
      q: "Why is \"for the good of the species\" a misleading framing of mutualism, according to the lecture?",
      choices: [
        "Each partner is selected for individual fitness; mutual benefit is a coincidence of interests.",
        "Mutualisms are always net costly to both partners and persist due to inertia in populations.",
        "Group selection at the species level is the only force capable of maintaining mutualism stably.",
        "Mutualisms cannot evolve unless the species literally share genomes through hybridization."
      ],
      correct: 0,
      why: "The lecture is explicit: mutualism is not \"cooperation for the good of the species\" — each partner is selected for individual fitness. Mutual benefit is a coincidence of interests, and cheating is selected against by enforcement mechanisms or partner choice.",
      choice_why: [
        "Correct. Individual fitness drives mutualism; joint benefit is incidental, not a goal.",
        "Wrong. Mutualisms are net beneficial to both partners; otherwise they break down.",
        "Wrong. Group selection is not the standard explanation for mutualism stability.",
        "Wrong. Hybridization is unnecessary; reciprocal individual benefit is what matters."
      ],
      source: "detail-extras · L09 §C"
    },
    {
      id: "STIM-DTL-L11-001",
      exam: 2,
      lecture: "L11",
      section: "A",
      topic: "Twofold cost of sex",
      type: "mc",
      difficulty: "application",
      points: 1,
      q: "The \"twofold cost of sex\" (Maynard Smith) refers to which problem with sexual reproduction?",
      choices: [
        "Sexual mothers face twice the predation risk during courtship and copulation events generally.",
        "Sexual reproduction requires twice the energy investment per offspring than asexual reproduction does.",
        "A sexual mother passes only HALF the gene copies per offspring that an asexual one would.",
        "Sex requires meiosis, which produces twice as many DNA replication errors in any generation."
      ],
      correct: 2,
      why: "Sexual mothers share parentage with males, so each offspring carries only half the mother's genes. An asexual mother would transmit her full genome to each offspring. The \"twofold cost\" is genetic transmission, not energy or risk.",
      choice_why: [
        "Wrong. The twofold cost is genetic, not predation-based, in the lecture.",
        "Wrong. The cost is in gene-copy transmission, not energy.",
        "Correct. The twofold cost is the halving of gene copies per offspring versus asexual.",
        "Wrong. Replication-error rates are not what the cost refers to."
      ],
      source: "detail-extras · L11 §A"
    },
    {
      id: "STIM-DTL-L11-002",
      exam: 2,
      lecture: "L11",
      section: "A",
      topic: "Muller's ratchet",
      type: "mc",
      difficulty: "synthesis",
      points: 1,
      q: "Muller's ratchet is the process by which:",
      choices: [
        "Sexual lineages accumulate beneficial mutations faster than asexual lineages can fix them.",
        "Genetic drift purges large-effect deleterious mutations in any sexually reproducing population.",
        "Recombination produces unwanted novel allele combinations that lower mean fitness directly.",
        "In strictly asexual lineages, deleterious mutations accumulate irreversibly without recombination."
      ],
      correct: 3,
      why: "Without recombination, the mutation-free class of an asexual population is irreversibly lost as deleterious mutations accumulate — a one-way \"ratchet.\" Sex purges deleterious mutations via recombination.",
      choice_why: [
        "Wrong. The ratchet is about deleterious mutations in asexuals, not beneficial accumulation.",
        "Wrong. The ratchet specifically applies to asexual populations, not sexual ones.",
        "Wrong. Recombination is a benefit of sex in this framing, not a cost.",
        "Correct. Irreversible accumulation of deleterious mutations in asexuals is the ratchet."
      ],
      source: "detail-extras · L11 §A"
    },
    {
      id: "STIM-DTL-L11-003",
      exam: 2,
      lecture: "L11",
      section: "A",
      topic: "Red Queen hypothesis",
      type: "mc",
      difficulty: "synthesis",
      points: 1,
      q: "The Red Queen hypothesis explains the maintenance of sex by appealing to:",
      choices: [
        "Selection from rapidly coevolving parasites that requires recombination to keep generating novel host genotypes.",
        "A constant rate of climatic change that selects for outbreeding to maximize genetic diversity over time.",
        "The need for sexual organisms to keep up with predator population cycles in stable habitats.",
        "A drift-driven loss of beneficial alleles whenever recombination is absent in any large population."
      ],
      correct: 0,
      why: "Red Queen: parasites coevolve with hosts so rapidly that hosts must keep producing genetically novel offspring to stay ahead. Sex provides the recombinational novelty. The name comes from Lewis Carroll — \"all the running you can do, to keep in the same place.\"",
      choice_why: [
        "Correct. Parasite-driven selection requiring host genotype turnover via sex.",
        "Wrong. Climate change is not the Red Queen mechanism in the lecture.",
        "Wrong. The Red Queen is about parasite coevolution, not predator population cycles.",
        "Wrong. The hypothesis is about coevolutionary pressure, not drift."
      ],
      source: "detail-extras · L11 §A"
    },
    {
      id: "STIM-DTL-L11-004",
      exam: 2,
      lecture: "L11",
      section: "B",
      topic: "Anisogamy as the definition of sex",
      type: "mc",
      difficulty: "recall",
      points: 1,
      q: "According to the lecture's OPERATIONAL definition, \"female\" is best defined as:",
      choices: [
        "The sex with secondary sex characteristics adapted for nurturing and offspring care directly.",
        "The sex that produces the larger, more costly gamete in a sexually reproducing species.",
        "The sex with two X chromosomes in mammals; analogous chromosomal arrangements in others.",
        "The sex with the higher post-zygotic parental investment after the fertilization event."
      ],
      correct: 1,
      why: "The lecture is explicit: sex is defined by GAMETE SIZE, not behavior, secondary sex characteristics, or chromosomes. Female = larger gamete; male = smaller. Anisogamy is the operational definition.",
      choice_why: [
        "Wrong. Nurturing behavior is downstream of anisogamy, not its definition.",
        "Correct. Larger gamete = female. Smaller gamete = male.",
        "Wrong. Chromosomal sex determination varies; gamete size is the universal criterion.",
        "Wrong. Parental investment correlates with sex but does not define it operationally."
      ],
      source: "detail-extras · L11 §B"
    },
    {
      id: "STIM-DTL-L11-005",
      exam: 2,
      lecture: "L11",
      section: "B",
      topic: "Anisogamy from isogamy",
      type: "mc",
      difficulty: "application",
      points: 1,
      q: "What is the lecture's framing of how anisogamy evolved from isogamy?",
      choices: [
        "A single mutation eliminating gamete size variation produced large gametes overnight.",
        "Genetic drift in small populations randomly fixed unequal gamete sizes among algal lineages.",
        "Stabilizing selection collapsed gamete-size variance until all gametes were intermediate-sized.",
        "Disruptive selection on gamete size produced two stable strategies — many small or few large."
      ],
      correct: 3,
      why: "The lecture states anisogamy evolved as a stable evolutionary endpoint of disruptive selection on gamete size. Either many small gametes (sperm strategy) or few large gametes (egg strategy) outcompete intermediate sizes.",
      choice_why: [
        "Wrong. The lecture frames it as disruptive selection, not a single mutation.",
        "Wrong. Drift is unlikely to produce a stable two-strategy equilibrium.",
        "Wrong. Stabilizing selection would maintain isogamy, not produce anisogamy.",
        "Correct. Disruptive selection on gamete size is the textbook scenario."
      ],
      source: "detail-extras · L11 §B"
    },
    {
      id: "STIM-DTL-L11-006",
      exam: 2,
      lecture: "L11",
      section: "C",
      topic: "Intra- vs. intersexual selection",
      type: "mc",
      difficulty: "application",
      points: 1,
      q: "A male elk grows large antlers used in head-to-head combat with rival males for access to females. This is an example of:",
      choices: [
        "Intersexual selection acting on male display traits driven by female mate-choice preferences.",
        "Antagonistic coevolution between males and females over reproductive interests within the species.",
        "Intrasexual selection — same-sex competition for mates, which produces weapons and large body size.",
        "Sperm competition driven by polyandrous mating in elk herds during the breeding season annually."
      ],
      correct: 2,
      why: "Male-male combat is INTRASEXUAL selection (same-sex competition). It produces weapons (antlers, horns) and large body size in the more competitive sex. Intersexual selection involves mate choice, typically female choice.",
      choice_why: [
        "Wrong. Intersexual selection involves choice across the sexes, not combat.",
        "Wrong. This is between males within the species, not antagonistic coevolution between sexes.",
        "Correct. Antlers in combat is the textbook intrasexual case.",
        "Wrong. Sperm competition acts after mating; antlers act before mating."
      ],
      source: "detail-extras · L11 §C"
    },
    {
      id: "STIM-DTL-L11-007",
      exam: 2,
      lecture: "L11",
      section: "C",
      topic: "Fisherian runaway",
      type: "mc",
      difficulty: "synthesis",
      points: 1,
      q: "In Fisherian runaway sexual selection, an arbitrary female preference for a male trait can amplify because:",
      choices: [
        "The trait directly improves male survival, and that survival benefit attracts more females.",
        "\"Sexy\" sons inherit both the trait AND the preference, producing positive feedback in subsequent generations.",
        "Group selection on the population favors any conspicuous male signal that draws predators.",
        "Genetic drift fixes the male trait independently of any female preference operating in the population."
      ],
      correct: 1,
      why: "Fisherian runaway is positive feedback: offspring inherit both the trait (from father) and the preference (from mother). Sons with the trait are preferred and pass on both. The preference can be initially arbitrary.",
      choice_why: [
        "Wrong. The trait often REDUCES survival; the gain is in mating success.",
        "Correct. Coupled inheritance of trait and preference produces runaway.",
        "Wrong. Group selection is not the runaway mechanism in the lecture.",
        "Wrong. Drift is undirected; runaway is a directional, preference-driven process."
      ],
      source: "detail-extras · L11 §C"
    },
    {
      id: "STIM-DTL-L11-008",
      exam: 2,
      lecture: "L11",
      section: "C",
      topic: "Survival cost of ornaments",
      type: "mc",
      difficulty: "application",
      points: 1,
      q: "Why do peacock tails persist despite the fact that they REDUCE survival probability?",
      choices: [
        "Mating gain from female choice exceeds the survival cost — net fitness still favors the trait.",
        "Tails are vestigial structures inherited from a dinosaur ancestor with no current function.",
        "Group selection at the population level favors species with more conspicuous males overall.",
        "The tails act primarily as antennae for thermoregulation in tropical habitats day to day."
      ],
      correct: 0,
      why: "Sexual selection can OPPOSE survival selection. Net fitness = mating gain − survival cost. As long as mating gain exceeds survival cost, the showy trait is favored despite reducing survival.",
      choice_why: [
        "Correct. Mating gain via female choice outweighs the survival cost — net fitness positive.",
        "Wrong. Peacock tails are not vestigial; they are actively favored by sexual selection.",
        "Wrong. Group selection is not the explanation for ornaments in the lecture.",
        "Wrong. Tails are display ornaments, not thermoregulatory structures."
      ],
      source: "detail-extras · L11 §C"
    },
    {
      id: "STIM-DTL-L11-009",
      exam: 2,
      lecture: "L11",
      section: "D",
      topic: "Sexual conflict — within species",
      type: "mc",
      difficulty: "synthesis",
      points: 1,
      q: "Sexual conflict is best described as:",
      choices: [
        "Inter-species coevolution between predators and prey within shared mating habitats and ranges.",
        "A subset of mutation-accumulation theory of senescence acting at the level of gametes only.",
        "A form of group selection that favors the survival of the entire breeding pair as a unit.",
        "Intra-species coevolution between males and females whose reproductive interests diverge."
      ],
      correct: 3,
      why: "Sexual conflict is INTRA-species coevolution — males and females are members of the same species but evolutionary antagonists when reproductive interests diverge (e.g., males benefiting from many matings, females from few high-quality matings).",
      choice_why: [
        "Wrong. Sexual conflict is within a species, not between species.",
        "Wrong. Sexual conflict is unrelated to mutation-accumulation theory of senescence.",
        "Wrong. Group selection is rejected as the explanation in modern evolutionary biology.",
        "Correct. Intra-species coevolution between sexes with conflicting interests."
      ],
      source: "detail-extras · L11 §D"
    },
    {
      id: "STIM-DTL-L11-010",
      exam: 2,
      lecture: "L11",
      section: "D",
      topic: "Sperm competition requires polyandry",
      type: "mc",
      difficulty: "application",
      points: 1,
      q: "Strong sperm competition is most likely to evolve in species in which:",
      choices: [
        "Females are strictly monogamous, mating only once with a single chosen male partner.",
        "Females are polyandrous — they mate with multiple males within a single breeding cycle.",
        "Males defend resources but never come into direct contact with rivals during mating attempts.",
        "Sex ratios are strictly 1:1, removing competitive selection between gametes of any kind."
      ],
      correct: 1,
      why: "Sperm competition implies polyandry (multiple mating by females). Sperm from different males compete to fertilize the female's eggs. In strictly monogamous species, sperm competition is weak.",
      choice_why: [
        "Wrong. Strict monogamy weakens sperm competition.",
        "Correct. Polyandry is the prerequisite — sperm from different males meet inside the female.",
        "Wrong. Resource defense without polyandry does not generate sperm-level competition.",
        "Wrong. The 1:1 sex ratio does not by itself drive sperm competition."
      ],
      source: "detail-extras · L11 §D"
    },
    {
      id: "STIM-DTL-L12-001",
      exam: 2,
      lecture: "L12",
      section: "A",
      topic: "Life-history trade-offs",
      type: "mc",
      difficulty: "recall",
      points: 1,
      q: "According to the lecture, life-history trade-offs (e.g., growth vs. reproduction, current vs. future reproduction) are best described as:",
      choices: [
        "Optional constraints that selection can overcome with sufficiently strong directional pressure.",
        "Group-level patterns that emerge only when populations face strong density-dependent selection.",
        "Random fluctuations that average out and impose no real limits across an organism's lifetime.",
        "Physiological constraints that selection navigates rather than escapes in any organism."
      ],
      correct: 3,
      why: "The lecture is emphatic: trade-offs are physical/physiological — they are NOT optional. Selection works WITHIN trade-offs to optimize, not to escape them. Selection maximizes lifetime reproductive success, not any single component.",
      choice_why: [
        "Wrong. Trade-offs are obligate physiological constraints, not optional.",
        "Wrong. Trade-offs operate at the individual level, not as group-level patterns.",
        "Wrong. Trade-offs impose real, persistent limits — they do not average away.",
        "Correct. Physiological constraints; selection optimizes within them, not around them."
      ],
      source: "detail-extras · L12 §A"
    },
    {
      id: "STIM-DTL-L12-002",
      exam: 2,
      lecture: "L12",
      section: "B",
      topic: "Extrinsic mortality and life history",
      type: "mc",
      difficulty: "application",
      points: 1,
      q: "Two opossum populations are compared: mainland (heavy predation) vs. predator-free island. Which life-history pattern matches the mainland opossums?",
      choices: [
        "Delayed reproduction, fewer but larger offspring, and a longer lifespan than island opossums.",
        "Identical life-history schedule to island opossums, since extrinsic mortality plays a minor role.",
        "Earlier reproduction, more offspring per litter, and shorter overall lifespan than island opossums.",
        "A reduction in heritability of life-history traits that prevents any evolutionary divergence at all."
      ],
      correct: 2,
      why: "The lecture's classic comparison: HIGH extrinsic mortality (mainland) → EARLY reproduction, MANY offspring, short lifespan. LOW extrinsic mortality (island) → DELAYED reproduction, fewer better-provisioned offspring, longer lifespan.",
      choice_why: [
        "Wrong. That is the island (low-predation) pattern, not the mainland.",
        "Wrong. Extrinsic mortality is the single most important determinant in the lecture.",
        "Correct. High predation favors fast/early reproduction — \"live fast, die young.\"",
        "Wrong. Heritability is not what changes; the optimum shifts under different mortality regimes."
      ],
      source: "detail-extras · L12 §B"
    },
    {
      id: "STIM-DTL-L12-003",
      exam: 2,
      lecture: "L12",
      section: "B",
      topic: "Speed of life-history evolution",
      type: "mc",
      difficulty: "recall",
      points: 1,
      q: "According to the lecture, life-history shifts under strong selection (e.g., predation pressure) typically evolve over what timescale?",
      choices: [
        "Within tens of generations when extrinsic mortality differs strongly between populations.",
        "Hundreds of thousands of generations under steady directional pressure across populations.",
        "Only over geological timescales of millions of years with steady directional selection across.",
        "They cannot evolve at all because life-history traits show negligible heritability in nature."
      ],
      correct: 0,
      why: "The lecture states life-history shifts evolve quickly — within tens of generations under strong selection. The opossum mainland-vs-island comparison is the named case.",
      choice_why: [
        "Correct. Tens of generations under strong selection — quoted directly.",
        "Wrong. The lecture cites tens of generations, not hundreds of thousands.",
        "Wrong. Life-history evolution is documented to be fast under strong pressure.",
        "Wrong. Life-history traits are heritable enough to respond to selection rapidly."
      ],
      source: "detail-extras · L12 §B"
    },
    {
      id: "STIM-DTL-L12-004",
      exam: 2,
      lecture: "L12",
      section: "C",
      topic: "Mutation accumulation theory (Medawar)",
      type: "mc",
      difficulty: "synthesis",
      points: 1,
      q: "Medawar's MUTATION ACCUMULATION theory of senescence proposes that aging arises because:",
      choices: [
        "A single gene with beneficial early-life effects has harmful late-life effects on the body.",
        "Late-acting deleterious mutations escape selection (carriers already reproduced) and accumulate.",
        "Cells deliberately suppress repair pathways at older ages to free resources for reproduction.",
        "Group selection favors short-lived populations that turn over more rapidly than rivals do."
      ],
      correct: 1,
      why: "Medawar's theory: late-life deleterious mutations escape selection because they affect individuals after reproduction. Such mutations accumulate over generations, causing senescence. It is a many-gene story, distinct from antagonistic pleiotropy.",
      choice_why: [
        "Wrong. That describes antagonistic pleiotropy (Williams), not mutation accumulation.",
        "Correct. Late-acting mutations escape selection and accumulate — Medawar's framing.",
        "Wrong. That sounds like disposable soma, not mutation accumulation.",
        "Wrong. Group selection is not Medawar's theory of aging."
      ],
      source: "detail-extras · L12 §C"
    },
    {
      id: "STIM-DTL-L12-005",
      exam: 2,
      lecture: "L12",
      section: "C",
      topic: "Antagonistic pleiotropy (Williams)",
      type: "mc",
      difficulty: "application",
      points: 1,
      q: "Williams's ANTAGONISTIC PLEIOTROPY theory of senescence is best illustrated by which scenario?",
      choices: [
        "A gene boosting early-life reproduction at the cost of harmful effects in late adulthood.",
        "Many independent late-acting deleterious mutations that escape selection in older organisms.",
        "A trade-off between somatic maintenance and reproduction set by overall energy budgets only.",
        "Group selection on populations preferring short-lived individuals to allow more turnover."
      ],
      correct: 0,
      why: "Antagonistic pleiotropy: a SINGLE gene with TWO effects — beneficial early in life, harmful late in life. Selection favors the early benefit because reproduction is upstream of the late cost. The lecture explicitly contrasts this with mutation accumulation (many genes).",
      choice_why: [
        "Correct. Single gene, dual effects — early benefit favored despite late cost.",
        "Wrong. That is mutation accumulation (Medawar), not antagonistic pleiotropy.",
        "Wrong. That is disposable soma (Kirkwood), not antagonistic pleiotropy.",
        "Wrong. Group selection is not part of any of the three senescence theories."
      ],
      source: "detail-extras · L12 §C"
    },
    {
      id: "STIM-DTL-L12-006",
      exam: 2,
      lecture: "L12",
      section: "C",
      topic: "Disposable soma (Kirkwood)",
      type: "mc",
      difficulty: "recall",
      points: 1,
      q: "Kirkwood's DISPOSABLE SOMA theory of senescence frames aging as:",
      choices: [
        "A trade-off in which organisms allocate finite resources between maintenance and reproduction.",
        "A consequence of late-life deleterious mutations that have escaped purifying selection over time.",
        "A single-gene effect with beneficial early-life consequences and harmful late-life consequences.",
        "A group-level adaptation favoring the rapid turnover of generations within breeding populations."
      ],
      correct: 0,
      why: "Disposable soma (Kirkwood): organisms have finite resources to split between somatic maintenance (long life) and reproduction (more offspring). Investment in soma reduces fecundity, so selection favors reproduction at the cost of long-term cell repair.",
      choice_why: [
        "Correct. Disposable soma = maintenance vs. reproduction allocation trade-off.",
        "Wrong. That is mutation accumulation, not disposable soma.",
        "Wrong. That is antagonistic pleiotropy, not disposable soma.",
        "Wrong. Group-level adaptation for turnover is not the disposable-soma framing."
      ],
      source: "detail-extras · L12 §C"
    },
    {
      id: "STIM-DTL-L12-007",
      exam: 2,
      lecture: "L12",
      section: "D",
      topic: "Offspring size-number trade-off",
      type: "mc",
      difficulty: "synthesis",
      points: 1,
      q: "A species with a fixed reproductive budget can produce either many small offspring (mice) or few large offspring (elephants). The lecture frames this contrast as:",
      choices: [
        "A demonstration of group selection among breeding individuals across competing populations annually.",
        "A purely random outcome unconnected to environment, predation, or resource competition pressure.",
        "Evidence that selection can break the size-number trade-off when environments are stable enough.",
        "The classic r-selected vs. K-selected life-history split, useful as a heuristic but not a strict dichotomy."
      ],
      correct: 3,
      why: "r-selected (mice, weeds) = many small offspring, early maturity, high mortality of each. K-selected (elephants, oaks) = few large offspring, delayed maturity, parental care. The lecture flags it as a useful heuristic, not a strict dichotomy — modern theory uses continuous variables.",
      choice_why: [
        "Wrong. The contrast is individual-level life history, not group selection.",
        "Wrong. The pattern is shaped by environment and predation, not random.",
        "Wrong. Selection works WITHIN trade-offs; it cannot break the size-number constraint.",
        "Correct. r/K is the classical heuristic, with the caveat that it is not strict."
      ],
      source: "detail-extras · L12 §D"
    },
    {
      id: "STIM-DTL-L12-008",
      exam: 2,
      lecture: "L12",
      section: "D",
      topic: "Age at maturity",
      type: "mc",
      difficulty: "application",
      points: 1,
      q: "In an environment with HIGH adult mortality risk, which age-at-maturity strategy is favored, all else equal?",
      choices: [
        "Earlier maturity — reproduce sooner before mortality strikes, even at smaller body size.",
        "Delayed maturity — invest more in growth before reproducing once, even with high adult mortality risk.",
        "Maturity timing is independent of adult mortality; only juvenile mortality shapes the schedule.",
        "A bimodal strategy in which two ages of first reproduction coexist within every population."
      ],
      correct: 0,
      why: "High extrinsic mortality favors early reproduction — get offspring out before you die, even at smaller adult size. The opposite (low mortality → delay, grow more, invest in fewer better offspring) is the K-selected pattern.",
      choice_why: [
        "Correct. Early maturity is favored when adult survival is unreliable.",
        "Wrong. That is the low-mortality pattern.",
        "Wrong. Adult mortality is one of the central determinants in the lecture.",
        "Wrong. Bimodal age-at-maturity equilibria are not the standard outcome here."
      ],
      source: "detail-extras · L12 §D"
    },
    {
      id: "STIM-DTL-L12-009",
      exam: 2,
      lecture: "L12",
      section: "E",
      topic: "Seychelles warblers — sex-biased dispersal",
      type: "mc",
      difficulty: "recall",
      points: 1,
      q: "In the Seychelles warbler (Acrocephalus sechellensis) on Cousin Island, the lecture documents which dispersal pattern?",
      choices: [
        "Male offspring stay on natal high-quality territories as helpers; females disperse to find mates.",
        "Female offspring stay on natal high-quality territories as helpers; males disperse from the natal site.",
        "Both sexes disperse equally, with no philopatric bias detectable across the long-term population.",
        "Helping behavior is absent because territory quality is uniform across the entire studied island."
      ],
      correct: 1,
      why: "Sex-biased dispersal in Seychelles warblers is FEMALE-PHILOPATRIC. Females stay on good territories; males disperse. The pattern is driven by territory quality variation. The lecture flags this as testable.",
      choice_why: [
        "Wrong. The bias is the opposite — females stay, males disperse.",
        "Correct. Female-philopatric, male-dispersing pattern is documented.",
        "Wrong. The bias is real and documented.",
        "Wrong. Territory quality varies dramatically; this is the basis of the pattern."
      ],
      source: "detail-extras · L12 §E"
    },
    {
      id: "STIM-DTL-L12-010",
      exam: 2,
      lecture: "L12",
      section: "E",
      topic: "Cooperative breeding and helping",
      type: "mc",
      difficulty: "synthesis",
      points: 1,
      q: "Why is cooperative breeding (e.g., Seychelles warblers) NOT considered pure altruism in the lecture?",
      choices: [
        "Helpers are forced into helping by parents; their own fitness is irrelevant in this framing.",
        "Cooperative breeding is purely a group-selection phenomenon at the population level overall.",
        "Helpers reproduce just as much as breeders; there is no reproductive cost paid by helpers.",
        "Helpers gain inclusive fitness by helping kin and may inherit territories later in life."
      ],
      correct: 3,
      why: "Helping is not pure altruism — helpers gain inclusive fitness through helping kin (rB) and may also inherit a high-quality territory in the future. Both indirect and direct fitness components contribute to the helper's payoff.",
      choice_why: [
        "Wrong. Helpers are not coerced; their own fitness is exactly what the framework analyzes.",
        "Wrong. Group selection is not the lecture's explanation for cooperative breeding.",
        "Wrong. Helpers DO pay a cost in deferred reproduction; that cost is offset by inclusive fitness.",
        "Correct. Indirect fitness through kin plus future territory inheritance — both apply."
      ],
      source: "detail-extras · L12 §E"
    },
    {
      id: "STIM-DTL-L13-001",
      exam: 2,
      lecture: "L13",
      section: "A",
      topic: "Selfish gene perspective",
      type: "mc",
      difficulty: "synthesis",
      points: 1,
      q: "Dawkins's \"selfish gene\" framing explains apparent altruism by saying:",
      choices: [
        "Selection favors alleles that increase their own propagation, even via altruism toward genetic relatives.",
        "Genes are conscious agents that calculate fitness payoffs in real time during interactions.",
        "Group-level selection always overrides individual-level selection in tight-knit social groups.",
        "Individuals act for the good of the species when relatives are members of the same population."
      ],
      correct: 0,
      why: "The \"selfish gene\" perspective is Dawkins's framing: selection favors alleles that propagate copies of themselves, including through helping individuals (kin) who also carry the allele. This unifies kin-directed altruism with the rest of evolutionary theory.",
      choice_why: [
        "Correct. Allele-level propagation explains apparent altruism via kin.",
        "Wrong. Genes are not conscious; \"selfish\" is a metaphor for propagation dynamics.",
        "Wrong. Modern view is that individual/genic selection dominates over group selection.",
        "Wrong. \"Good of the species\" is the rejected naïve framing, not the selfish-gene view."
      ],
      source: "detail-extras · L13 §A"
    },
    {
      id: "STIM-DTL-L13-002",
      exam: 2,
      lecture: "L13",
      section: "B",
      topic: "Hamilton's rule with r=0",
      type: "mc",
      difficulty: "application",
      points: 1,
      q: "According to Hamilton's rule, what is predicted if the relatedness coefficient r between actor and recipient is zero (i.e., the recipient is a complete stranger)?",
      choices: [
        "Altruism is favored because B remains positive and any benefit propagates the actor's genes.",
        "Hamilton's rule cannot be satisfied through kinship; some other mechanism (reciprocity, reputation) is required.",
        "Altruism is always favored when the cost C is small, regardless of the recipient's relatedness.",
        "Group selection takes over and favors altruism whenever extrinsic mortality is high in the area."
      ],
      correct: 1,
      why: "Hamilton's rule: rB > C. If r = 0, then rB = 0, which cannot exceed any positive cost C. The lecture is explicit: helping random strangers does not satisfy Hamilton's rule; reciprocity, reputation, or other mechanisms are needed.",
      choice_why: [
        "Wrong. With r = 0, the indirect fitness benefit through the recipient is zero.",
        "Correct. Strangers (r ≈ 0) require non-kin mechanisms — reciprocity or reputation.",
        "Wrong. C still matters; rB = 0 cannot exceed any positive C, no matter how small.",
        "Wrong. Group selection is not invoked to rescue Hamilton's rule for strangers."
      ],
      source: "detail-extras · L13 §B"
    },
    {
      id: "STIM-DTL-L13-003",
      exam: 2,
      lecture: "L13",
      section: "B",
      topic: "Coefficient of relatedness — half-siblings",
      type: "mc",
      difficulty: "recall",
      points: 1,
      q: "According to the lecture, the coefficient of relatedness r between two HALF-siblings is:",
      choices: [
        "0.125, the same as the value used for first cousins in the standard table.",
        "0.5, the same as full siblings and as parent-offspring pairs in diploids.",
        "0.25 — half the value of full siblings, since they share only one parent.",
        "0.75, the value used for full sisters in haplodiploid hymenopteran systems specifically."
      ],
      correct: 2,
      why: "The lecture's relatedness table: parent-offspring r = 0.5; full siblings r = 0.5; half-siblings r = 0.25; first cousins r = 0.125.",
      choice_why: [
        "Wrong. r = 0.125 is for first cousins.",
        "Wrong. r = 0.5 is for full siblings and parent-offspring.",
        "Correct. Half-siblings share one parent: r = 0.25.",
        "Wrong. r = 0.75 is for full sisters in haplodiploid systems, not for half-siblings."
      ],
      source: "detail-extras · L13 §B"
    },
    {
      id: "STIM-DTL-L13-004",
      exam: 2,
      lecture: "L13",
      section: "B",
      topic: "Haplodiploidy — sisters' relatedness",
      type: "mc",
      difficulty: "synthesis",
      points: 1,
      q: "In haplodiploid hymenopterans (bees, wasps, ants), full sisters share what value of r — and why does this favor sister-helping?",
      choices: [
        "r = 0.5, identical to mother-offspring; no asymmetry exists for sister-helping in the system.",
        "r = 0.25, lower than mother-offspring; helping sisters cannot be favored under Hamilton's rule.",
        "r = 0.75 — higher than mother-offspring r = 0.5 — favoring helping sisters over own offspring.",
        "r = 1.0 — sisters are clones in haplodiploid systems and any helping is therefore obligate."
      ],
      correct: 2,
      why: "Haplodiploidy: sisters share r = 0.75 because they inherit 100% of their father's haploid genome, plus 50% of their mother's diploid genome on average. This exceeds mother-offspring r = 0.5 — helping sisters propagates more shared alleles than helping own offspring.",
      choice_why: [
        "Wrong. The asymmetry is exactly what makes haplodiploidy interesting for kin selection.",
        "Wrong. r = 0.25 is far too low; haplodiploidy actually elevates sister-relatedness.",
        "Correct. r = 0.75 between sisters; this is the lecture's named value.",
        "Wrong. Sisters are not clones; r = 0.75 captures the elevated but partial sharing."
      ],
      source: "detail-extras · L13 §B"
    },
    {
      id: "STIM-DTL-L13-005",
      exam: 2,
      lecture: "L13",
      section: "C",
      topic: "ESS as Nash equilibrium",
      type: "mc",
      difficulty: "recall",
      points: 1,
      q: "An Evolutionarily Stable Strategy (ESS) is best characterized in game-theoretic terms as:",
      choices: [
        "The strategy that always wins head-to-head matchups against any rival in fixed conditions.",
        "A drift-driven outcome that emerges only in small populations under genetic bottleneck.",
        "The strategy that maximizes population mean fitness across the breeding generation overall.",
        "A Nash equilibrium — once common, it cannot be invaded by any rare alternative strategy."
      ],
      correct: 3,
      why: "The lecture frames ESS as a Nash equilibrium: a strategy that, when adopted by most members of a population, cannot be invaded by any rare alternative. It need not be the highest-mean-fitness strategy — mixed-strategy ESS solutions are common.",
      choice_why: [
        "Wrong. ESS is about non-invasibility, not always winning head-to-head.",
        "Wrong. ESS is a deterministic equilibrium concept, not a drift outcome.",
        "Wrong. ESS does not necessarily maximize population mean fitness.",
        "Correct. Nash-equilibrium framing — the standard ESS definition."
      ],
      source: "detail-extras · L13 §C"
    },
    {
      id: "STIM-DTL-L13-006",
      exam: 2,
      lecture: "L13",
      section: "D",
      topic: "Side-blotched lizard morphs",
      type: "mc",
      difficulty: "application",
      points: 1,
      q: "In Uta stansburiana, which male morph is described as a SNEAKER that mimics females and sneaks copulations from larger territory-holders?",
      choices: [
        "Orange — aggressive, defends large territories with multiple females in residence per male.",
        "Yellow — sneaker morph that mimics females and slips past territorial males to mate with females.",
        "Blue — vigilant, defends small territories with one mate, alert against intruders specifically.",
        "A fourth red morph that emerges only in years of low population density across the range."
      ],
      correct: 1,
      why: "Yellow is the SNEAKER morph in Uta stansburiana — yellow males mimic females and sneak copulations. Orange = aggressive territory holder; Blue = small-territory mate-guarder. The cyclic dominance is Orange > Blue > Yellow > Orange.",
      choice_why: [
        "Wrong. Orange is the aggressive territorial morph, not the sneaker.",
        "Correct. Yellow is the female-mimicking sneaker.",
        "Wrong. Blue is the vigilant small-territory morph that catches sneakers.",
        "Wrong. The lecture describes three morphs, not four."
      ],
      source: "detail-extras · L13 §D"
    },
    {
      id: "STIM-DTL-L13-007",
      exam: 2,
      lecture: "L13",
      section: "D",
      topic: "Rock-paper-scissors logic",
      type: "mc",
      difficulty: "synthesis",
      points: 1,
      q: "In the side-blotched lizard rock-paper-scissors dynamic, which dominance ordering is correct?",
      choices: [
        "Yellow beats Blue, Blue beats Orange, Orange beats Yellow as the standard cyclic ordering.",
        "Orange always wins eventually because aggressive territory defense scales with male body size.",
        "All three morphs reach a stable equal-frequency equilibrium under negative frequency-dependence.",
        "Orange beats Blue, Blue beats Yellow, Yellow beats Orange — cyclic, no single winner persists."
      ],
      correct: 3,
      why: "The cyclic dominance from the lecture: Orange > Blue (aggression overwhelms small-territory defense), Blue > Yellow (vigilance catches sneakers), Yellow > Orange (Orange spreads thin, Yellow sneaks in). No single ESS — frequencies cycle.",
      choice_why: [
        "Wrong. The ordering is reversed in this distractor.",
        "Wrong. Yellow exploits Orange when Orange is common — Orange does not always win.",
        "Wrong. The system shows cyclic dynamics, not a stable equal-frequency equilibrium.",
        "Correct. Orange > Blue > Yellow > Orange — cyclic dominance, frequencies cycle over years."
      ],
      source: "detail-extras · L13 §D"
    },
    {
      id: "STIM-DTL-L13-008",
      exam: 2,
      lecture: "L13",
      section: "E",
      topic: "Indirect reciprocity",
      type: "mc",
      difficulty: "application",
      points: 1,
      q: "A species in which helpful behavior earns a reputation that attracts later help from third-party observers is best described as relying on:",
      choices: [
        "Direct reciprocity — tit-for-tat exchanges between two specific individuals over repeated rounds.",
        "Indirect reciprocity — reputation effects that draw future help from observers and bystanders.",
        "Kin selection alone, since reputation can only operate between close genetic relatives.",
        "A naïve group-selection mechanism in which behaviors evolve for the good of the group."
      ],
      correct: 1,
      why: "Indirect reciprocity: helping confers a reputation; observers later help the helper. It requires public visibility. Direct reciprocity requires repeated interaction between the same pair (tit-for-tat).",
      choice_why: [
        "Wrong. Direct reciprocity is paired tit-for-tat, not reputation-based.",
        "Correct. Reputation-driven cooperation is indirect reciprocity.",
        "Wrong. Reputation effects work among unrelated observers, not just kin.",
        "Wrong. Group selection is not the indirect-reciprocity mechanism."
      ],
      source: "detail-extras · L13 §E"
    },
    {
      id: "STIM-DTL-L13-009",
      exam: 2,
      lecture: "L13",
      section: "E",
      topic: "Reciprocity requires repeated interaction",
      type: "mc",
      difficulty: "synthesis",
      points: 1,
      q: "Why does direct reciprocity FAIL as an explanation for cooperation in one-shot, anonymous interactions?",
      choices: [
        "Anonymity removes inclusive-fitness benefits even when the recipient is a close genetic relative.",
        "Direct reciprocity requires repeated interaction and memory; one-shot anonymous play prevents both.",
        "Group selection at the level of populations replaces direct reciprocity in any anonymous setting.",
        "Direct reciprocity is mathematically equivalent to indirect reciprocity in any environmental setting."
      ],
      correct: 1,
      why: "The lecture is explicit: reciprocity requires REPEATED INTERACTION — it doesn't work in one-shot games or anonymous encounters. Without repeat play and memory, defectors cannot be punished and cooperators cannot be rewarded.",
      choice_why: [
        "Wrong. Inclusive fitness is a separate mechanism — kinship — not direct reciprocity.",
        "Correct. Repeat play and memory are prerequisites for tit-for-tat to function.",
        "Wrong. Group selection is not introduced as a substitute for reciprocity here.",
        "Wrong. Direct and indirect reciprocity have different prerequisites and are not equivalent."
      ],
      source: "detail-extras · L13 §E"
    },
    {
      id: "STIM-DTL-L13-010",
      exam: 2,
      lecture: "L13",
      section: "A",
      topic: "Group selection — when it can work",
      type: "mc",
      difficulty: "synthesis",
      points: 1,
      q: "According to the lecture, group-level selection is generally overwhelmed by individual selection. Under what restricted conditions can SOME forms of group selection still operate?",
      choices: [
        "Only when species-level cooperation is mandated by the abiotic environment for survival reasons.",
        "When populations frequently go extinct and groups are strictly subdivided with little mixing.",
        "Whenever heritability of cooperative traits drops below 0.5 in any breeding population.",
        "In species where antagonistic pleiotropy maintains a cooperator-only morph in a population."
      ],
      correct: 1,
      why: "The lecture states special conditions — frequent population extinctions and strict subdivision — can permit some group-level selection. These are exceptions, not the rule. Most apparent group benefits arise from individual-level mechanisms.",
      choice_why: [
        "Wrong. Mandates from the abiotic environment do not override individual selection.",
        "Correct. Frequent extinctions plus strict subdivision is the named exception.",
        "Wrong. Heritability thresholds are not the lecture's stated condition.",
        "Wrong. Antagonistic pleiotropy is a senescence theory, not a group-selection mechanism."
      ],
      source: "detail-extras · L13 §A"
    }
  ];
  if (!Array.isArray(window.STIM_BANK)) window.STIM_BANK = [];
  window.STIM_BANK = window.STIM_BANK.concat(detail);
  if (window.STIM_INDEX) {
    if (!window.STIM_INDEX.byExam) window.STIM_INDEX.byExam = {};
    if (!window.STIM_INDEX.byLecture) window.STIM_INDEX.byLecture = {};
    detail.forEach(function(q){
      var ex = q.exam;
      if (!window.STIM_INDEX.byExam[ex]) window.STIM_INDEX.byExam[ex] = [];
      window.STIM_INDEX.byExam[ex].push(q.id);
      if (!window.STIM_INDEX.byLecture[q.lecture]) window.STIM_INDEX.byLecture[q.lecture] = [];
      window.STIM_INDEX.byLecture[q.lecture].push(q.id);
    });
  }
  console.log('[stim-bank-detail-e2 loaded] +' + detail.length + ' Exam 2 detail questions · STIM_BANK total = ' + window.STIM_BANK.length);
})();
