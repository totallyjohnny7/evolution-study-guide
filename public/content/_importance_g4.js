/* Importance content (group 4: L13, L14, L15) — written by agent. */
(function () {
  if (!window.addCardPatches) return;

  // ===================== L13: SOCIAL BEHAVIOR =====================
  window.addCardPatches('L13', {
    "Group selection": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Naive "good of the species" thinking is the #1 wrong-answer trap on social-behavior questions — Robbins will hit you on this.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Two timescales of selection: WITHIN-group (fast — generations) vs AMONG-group (slow — group lifespans).</li>
  <li>Modern view: group selection requires (1) frequent group extinctions, (2) strict subdivision/low gene flow, (3) low within-group variance — RARE in nature.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Foundation for the entire L13 pivot to kin selection.</strong> Hamilton's rule exists because naive group selection FAILS — you need a different framework to explain altruism.</li>
  <li><strong>Classic discriminator question.</strong> When the exam describes an apparent altruistic trait, the WRONG answer is "good of the species"; the RIGHT answer invokes kin selection, reciprocity, or individual benefit.</li>
  <li><strong>Cheater dynamics are the killer.</strong> Within any group, an individual that withholds the costly act keeps fitness C while still receiving B from groupmates — selfish individuals out-reproduce altruists every generation.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>"For the good of the species" is a non-explanation — always ask: what's in it for the GENE?</li>
  <li>Group selection isn't strictly impossible (haystack-mouse model), but it's swamped by individual selection in nearly all real cases.</li>
</ul>` },

    "Selfish gene perspective": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Dawkins's gene's-eye view reframes "altruism" as gene-level selfishness — this is THE conceptual unlock for the entire kin-selection module.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Hymenopteran sister r = 0.75 — higher than to own offspring (r = 0.5). The "selfish gene" wins by helping sisters, not breeding.</li>
  <li>Worker ant direct fitness = 0; indirect fitness = enormous via queen's offspring.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Reframes the unit of selection.</strong> Bodies are vehicles; genes are passengers. Ask which ALLELES increase, not which BODIES reproduce.</li>
  <li><strong>Resolves the "altruism paradox".</strong> Worker self-sacrifice is genetic selfishness in disguise — the worker's alleles propagate efficiently through related queen offspring.</li>
  <li><strong>Sets up Hamilton's rule.</strong> rB > C is the math that operationalizes the selfish-gene concept.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>"Selfish" doesn't mean conscious — it's a metaphor for differential allele propagation.</li>
  <li>Don't confuse the selfish-gene perspective with selfish-INDIVIDUAL behavior; the gene can favor altruistic bodies.</li>
</ul>` },

    "Hamilton's rule": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> rB &gt; C is THE most-tested formula in L13 — Robbins will give you r, B, C and ask whether altruism evolves. Get this wrong and you lose multiple points.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li><strong>rB &gt; C</strong>: r = relatedness, B = benefit to recipient (offspring units), C = cost to actor (offspring units).</li>
  <li>r values: parent-offspring 0.5, full sib 0.5, half-sib 0.25, first cousin 0.125, hymenopteran sister 0.75 (haplodiploidy).</li>
  <li>To save a sibling (r=0.5) at C=1, need B &gt; 2. To save a cousin (r=0.125) at C=1, need B &gt; 8.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>The exam-trap formula.</strong> Forgetting the r and writing "B &gt; C" is the classic fail — exam will explicitly punish this.</li>
  <li><strong>Quantitative test of altruism.</strong> Plug in real numbers from a worker bee or naked mole rat scenario: the math has to clear C.</li>
  <li><strong>Explains eusociality.</strong> When r = 0.75 (hymenoptera), even modest B easily clears C — the canonical haplodiploidy story.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>Helping STRANGERS does NOT satisfy Hamilton's rule (r ≈ 0). Stranger-altruism needs reciprocity or reputation, not kin selection.</li>
  <li>B and C are in OFFSPRING UNITS, not arbitrary points. Convert behavior into reproductive consequences.</li>
</ul>` },

    "Coefficient of relatedness (r)": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> r values are pure memorization — Robbins WILL ask you to compute r between specified relatives, no exceptions.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Identical twin r = 1.0</li>
  <li>Parent ↔ offspring r = 0.5</li>
  <li>Full sibling r = 0.5</li>
  <li>Half-sibling r = 0.25</li>
  <li>First cousin r = 0.125</li>
  <li>Hymenopteran sister r = 0.75 (haplodiploid asymmetry)</li>
  <li>Hymenopteran brother r = 0.25 (males come from unfertilized eggs)</li>
  <li>Heuristic: halve r at every meiosis between you and the relative.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Plug into Hamilton's rule.</strong> Without correct r, rB &gt; C math collapses.</li>
  <li><strong>Explains hymenopteran eusociality.</strong> r = 0.75 between sisters &gt; r = 0.5 to own offspring — sisters are GENETICALLY MORE VALUABLE than daughters.</li>
  <li><strong>Discriminator: r ≠ overall genome similarity.</strong> Two unrelated humans share ~99.9% sequence — but r ≈ 0 because that's not by RECENT common descent.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>r is about RECENT shared descent, not absolute genome similarity.</li>
  <li>Haplodiploidy makes r asymmetric — sisters share dad's haploid genome (r=1 from him) + half mom's (r=0.5 from her) → averaged r = 0.75.</li>
</ul>` },

    "Inclusive fitness": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Inclusive fitness = direct + indirect — this is how a sterile worker can be evolutionarily "successful" despite zero offspring.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Direct fitness = own offspring count.</li>
  <li>Indirect fitness = (extra offspring of relatives caused by your help) × r.</li>
  <li>Worker bee: direct = 0; indirect = many sisters × 0.75.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Resolves the worker bee paradox.</strong> She produces zero offspring — yet her behavior is favored because indirect fitness through the queen's offspring is massive.</li>
  <li><strong>Justifies altruism from a gene's perspective.</strong> Inclusive fitness asks "do my alleles increase?" not "did I personally breed?"</li>
  <li><strong>Mathematical extension of Hamilton's rule.</strong> Inclusive fitness is the QUANTITY rB &gt; C maximizes.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>Indirect fitness counts only the EXTRA offspring relatives produce because of your help — not all their offspring.</li>
  <li>Don't double-count: if you reduce your own breeding to help, that's a cost in direct fitness, balanced against indirect gain.</li>
</ul>` },

    "Eusociality": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Eusociality (sterile workers + queen + overlapping generations) is the EXTREME endpoint of kin selection — Robbins loves naked mole-rat and hymenoptera examples.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Three criteria: (1) reproductive division of labor (queen + sterile workers), (2) overlapping generations, (3) cooperative care of young.</li>
  <li>Hymenoptera (ants, bees, wasps): sister r = 0.75 enables eusociality.</li>
  <li>Naked mole-rat: effective r ≈ 0.8 from extreme inbreeding within colonies.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Most extreme test of kin selection.</strong> Workers fully forgo reproduction (C = lifetime fitness). For Hamilton's rule to clear, B × r must be enormous — and it is.</li>
  <li><strong>Two paths to high r.</strong> Haplodiploidy (hymenoptera) OR inbreeding (mole rats). Both produce r &gt; 0.5 within colony.</li>
  <li><strong>Predictive theory.</strong> Eusociality occurs where r is high AND outside breeding opportunities are scarce.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>Termites are eusocial but NOT haplodiploid — explanation is ecological (helpful nest, low dispersal), not genetic.</li>
  <li>Don't confuse eusocial with merely "social" — the sterile-worker caste is the diagnostic.</li>
</ul>` },

    "Evolutionarily Stable Strategy (ESS)": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> An ESS cannot be invaded by a rare alternative — this is the evolutionary version of a Nash equilibrium and the entire Hawk-Dove framework rests on it.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Mixed Hawk-Dove ESS: p* = V/C (when V &lt; C).</li>
  <li>If V ≥ C: pure-Hawk ESS.</li>
  <li>ESS payoff condition: at p*, expected payoff to Hawk = expected payoff to Dove.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Frequency-dependent fitness.</strong> ESS is the language for situations where what's optimal depends on what others are doing.</li>
  <li><strong>Predicts mixed equilibria.</strong> Pure strategies often unstable; mixed ESS at p* is the answer.</li>
  <li><strong>Side-blotched lizards demonstrate it.</strong> Three morphs cycle on ~5-6 yr period because no single strategy is uninvadable.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>An ESS is NOT necessarily the best strategy on average — it's the strategy that can't be DISPLACED once common.</li>
  <li>A mixed ESS can be a polymorphic population OR every individual playing each strategy with probability p*.</li>
</ul>` },

    "Frequency-dependent selection": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> NEGATIVE frequency-dependent selection (rare = fit) maintains polymorphism — this is the engine behind side-blotched lizard rock-paper-scissors and many ESS scenarios.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>NEGATIVE freq-dep: fitness HIGH when rare, LOW when common → maintains diversity.</li>
  <li>POSITIVE freq-dep: fitness HIGH when common (e.g., warning coloration) → drives fixation.</li>
  <li>Side-blotched lizard cycle: ~5-6 years per period.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Explains stable polymorphism.</strong> Without freq-dep selection, the best strategy fixes; with negative freq-dep, multiple strategies coexist.</li>
  <li><strong>Side-blotched lizards = textbook field demo.</strong> Robbins WILL ask which kind of selection produces those cycles.</li>
  <li><strong>Connects to ESS theory.</strong> Mixed ESS solutions exist BECAUSE of freq-dep payoffs.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>Negative freq-dep maintains diversity; positive freq-dep destroys it. Don't swap them.</li>
  <li>Cycles, not equilibria, are the diagnostic outcome of rock-paper-scissors freq-dep.</li>
</ul>` },

    "Hawk-Dove game": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Hawk-Dove is the canonical ESS exam problem — Robbins WILL give you V and C and ask for p*.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Payoff matrix: Hawk vs Hawk = ½(V−C); Hawk vs Dove = V; Dove vs Hawk = 0; Dove vs Dove = V/2.</li>
  <li>Mixed ESS Hawk frequency: <strong>p* = V/C</strong> (only when V &lt; C).</li>
  <li>If V ≥ C: pure-Hawk ESS (fighting always pays).</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Direct calculation question.</strong> V=10, C=20 → p* = 0.5 Hawks. Memorize the formula.</li>
  <li><strong>Demonstrates why pure strategies fail.</strong> Pure Hawk: too costly. Pure Dove: invaded by rare Hawk. Mix is the answer.</li>
  <li><strong>Generalizes to many real systems.</strong> Aggression-vs-display contests, contest behavior in male animals.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>If p* &gt; 1 (V &gt; C), the formula is OUT OF DOMAIN — pure-Hawk wins, not mixed.</li>
  <li>Hawk-Hawk payoff is ½(V−C), NOT (V−C). Half because each fighter has 50% chance of winning.</li>
</ul>` },

    "Side-blotched lizard (Uta stansburiana)": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Three male morphs (orange, blue, yellow) play rock-paper-scissors on a ~5-6 year cycle — the classic real-world ESS demonstration that Robbins will absolutely test.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li><strong>Orange</strong>: aggressive, defends LARGE territory with many females.</li>
  <li><strong>Blue</strong>: mate-guards ONE female, vigilant against sneakers.</li>
  <li><strong>Yellow</strong>: sneaker, mimics females, slips past oranges.</li>
  <li><strong>Cycle</strong>: Orange &gt; Blue &gt; Yellow &gt; Orange (~5-6 year period).</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Real-world rock-paper-scissors.</strong> Sinervo & Lively 1996 — proof that ESS theory predicts cycles, not just equilibria.</li>
  <li><strong>Demonstrates negative frequency-dependent selection.</strong> Each morph favored when rare, exploited when common.</li>
  <li><strong>No fixation possible.</strong> Whichever morph is currently winning is the next to be exploited — no morph can monopolize.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>Orange beats Blue, Blue beats Yellow, Yellow beats Orange — drill this order.</li>
  <li>Stable cycles ≠ equilibrium. The system NEVER settles to one frequency.</li>
</ul>` },

    "Direct reciprocity": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Tit-for-tat between PAIRS of repeated partners — vampire bats and Axelrod's tournaments are the canonical examples.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Stability condition: w &gt; C/B (probability of future interaction × benefit must clear cost).</li>
  <li>Axelrod (1984): tit-for-tat won repeated Prisoner's Dilemma tournaments.</li>
  <li>Vampire bats (Wilkinson 1984): blood-sharing among unrelated roost-mates.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Cooperation without kinship.</strong> Direct reciprocity explains how altruism toward NON-relatives can be stable.</li>
  <li><strong>Three requirements.</strong> (1) Repeat encounters with the same individual; (2) recognition/memory; (3) sufficient shadow of the future (w high).</li>
  <li><strong>Axelrod's tit-for-tat.</strong> Cooperate first, then copy partner's last move — simple rule, hard to beat.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>Direct reciprocity FAILS in one-shot or anonymous encounters (no future, no memory).</li>
  <li>Doesn't scale to large groups where you may never re-meet a partner — that's where indirect reciprocity takes over.</li>
</ul>` },

    "Indirect reciprocity": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Reputation-based cooperation — helping earns you a good rep that attracts future help from THIRD PARTIES, not the original recipient.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Three requirements: (1) behavior is OBSERVED, (2) reputations are TRACKED and shared, (3) helpers DISCRIMINATE based on reputation.</li>
  <li>Donor and eventual repayer need NEVER meet directly.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Scales to large groups.</strong> Where direct reciprocity fails (huge fluid populations), indirect reciprocity works because the reputation network does the bookkeeping.</li>
  <li><strong>Foundation of human cooperation.</strong> Language and gossip massively amplify it — the engine of human social norms.</li>
  <li><strong>Anonymous donors example.</strong> Public charity earns reputation that attracts cooperative partners later.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>Without VISIBILITY, indirect reciprocity collapses — the whole mechanism rests on observers.</li>
  <li>Discriminators must REFUSE help to defectors, otherwise free-riders invade.</li>
</ul>` },

    // ==== L13 EXTRAS ====
    "Hamilton's rule: rB > C": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> The compact form of Hamilton's rule — Robbins WILL feed you specific r, B, C and ask whether the act evolves.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>To favor saving a sibling (r=0.5) at C=1: need B &gt; 2.</li>
  <li>To favor saving a cousin (r=0.125) at C=1: need B &gt; 8.</li>
  <li>To favor saving a hymenopteran sister (r=0.75) at C=1: need B &gt; 1.33.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Direct calculation problem.</strong> Plug-and-chug: multiply r × B and check if it exceeds C.</li>
  <li><strong>Why hymenoptera evolved eusociality.</strong> r=0.75 means a tiny B clears even a large C — sisters are easy to "afford".</li>
  <li><strong>Distance dilution.</strong> The further the relative, the larger B needs to be — explains why altruism falls off rapidly with distance.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>NEVER drop the r — "B &gt; C" without r is the most common error.</li>
  <li>B and C are in OFFSPRING UNITS, not arbitrary fitness points.</li>
</ul>` },

    "Coefficient of relatedness — common values": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> The r-table is pure flashcard memorization — there is NO partial credit for "close enough" on r values.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Identical twin: r = 1.0</li>
  <li>Parent-offspring: r = 0.5</li>
  <li>Full sibling: r = 0.5</li>
  <li>Half-sibling: r = 0.25</li>
  <li>First cousin: r = 0.125</li>
  <li>Hymenopteran sister: r = 0.75 (haplodiploidy)</li>
  <li>Hymenopteran brother: r = 0.25</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Foundation for every Hamilton calculation.</strong> Wrong r → wrong rB → wrong answer.</li>
  <li><strong>Haplodiploidy asymmetry.</strong> Sisters share dad's full haploid genome (r=1 from him) + half mom's (r=0.5 from her) → averaged r=0.75. Brothers come from unfertilized eggs (different math).</li>
  <li><strong>Halving rule.</strong> Each meiosis between you and the relative halves r — useful shortcut.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>Hymenopteran SISTER is r=0.75; BROTHER is r=0.25. Don't blur them.</li>
  <li>r is about RECENT descent, not overall genome similarity.</li>
</ul>` },

    "Hawk-Dove game payoffs": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> The four payoff cells of Hawk-Dove are the test material — Robbins will absolutely ask you to fill them in.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Hawk vs Hawk: <strong>½(V−C)</strong> each (50/50 win/lose, fight cost C if you lose).</li>
  <li>Hawk vs Dove: <strong>V</strong> for Hawk, <strong>0</strong> for Dove.</li>
  <li>Dove vs Dove: <strong>V/2</strong> each (share resource).</li>
  <li>Mixed ESS Hawk frequency: <strong>p* = V/C</strong> (when V&lt;C).</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Direct numerical problem.</strong> V=10, C=20 → p_Hawk* = 10/20 = 0.5.</li>
  <li><strong>Domain check.</strong> If V ≥ C → pure-Hawk ESS (p* &gt; 1 is meaningless).</li>
  <li><strong>Average-payoff comparison.</strong> At p*, expected payoffs to Hawk and Dove are EQUAL — that's the ESS condition.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>The Hawk-Hawk payoff is HALF of (V−C), not the full thing — easy fail.</li>
  <li>Dove-vs-Hawk = 0 (Dove flees), not negative — the Dove just LOSES the resource.</li>
</ul>` },

    "Side-blotched lizard rock-paper-scissors": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> The cyclic dominance structure (Orange &gt; Blue &gt; Yellow &gt; Orange) is the field demonstration that frequency-dependent selection produces cycles, not equilibria.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Three morphs: Orange (aggressive), Blue (mate-guard), Yellow (sneaker).</li>
  <li>Cycle period: ~5-6 years.</li>
  <li>NEGATIVE frequency-dependent selection — rare-is-fit.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Sinervo & Lively 1996 classic.</strong> Real-world test of ESS theory.</li>
  <li><strong>Disproves "selection always finds the best".</strong> No single morph is unconditionally best — frequency context matters.</li>
  <li><strong>Cycle reasoning.</strong> Orange common → Yellow exploits → Yellow common → Blue catches sneakers → Blue common → Orange overpowers.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>Memorize the dominance: Orange beats Blue, Blue beats Yellow, Yellow beats Orange. Robbins WILL flip this and ask you to spot the error.</li>
  <li>It's a STABLE CYCLE, not equilibrium — the system never settles.</li>
</ul>` },

    "Direct vs indirect reciprocity": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Direct = pair-based with memory; indirect = reputation-based with observers — Robbins distinguishes these on the discriminator question.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Direct: requires REPEAT encounters with SAME individual + recognition.</li>
  <li>Indirect: requires VISIBILITY + reputation tracking + discriminators.</li>
  <li>Vampire bats = direct; anonymous public donations = indirect.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Direct scales poorly.</strong> Tit-for-tat fails in large fluid groups where you may not re-meet a partner.</li>
  <li><strong>Indirect scales massively.</strong> Reputation networks let donor and repayer NEVER meet directly.</li>
  <li><strong>Human cooperation.</strong> Language + gossip + norms supercharge indirect reciprocity — the foundation of large-scale human cooperation.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>One-shot anonymous encounter? Neither mechanism works — that's pure free-rider territory.</li>
  <li>Direct reciprocity is NOT kin selection (no r involved); it's a separate mechanism.</li>
</ul>` },

    "Group selection — why naive version fails": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Within-group selection runs FAST; among-group selection runs SLOW — that's why cheaters always win unless you have very specific group structure.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Naive group selection requires: frequent group extinctions + strict subdivision + low gene flow.</li>
  <li>Haystack-mouse model (Maynard Smith): mice colonize haystacks, breed isolated, then disperse.</li>
  <li>Modern view: multilevel selection valid only in narrow conditions; mostly dominated by individual/kin selection.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Two timescales of selection.</strong> Within-group: generations. Among-group: lifespan of groups. Generations win.</li>
  <li><strong>Cheater dynamics.</strong> Inside any group, an individual that withholds the costly act has higher fitness — selfish invades.</li>
  <li><strong>Special-conditions valid case.</strong> If groups go extinct fast and migration is rare, among-group can outpace within-group.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>"For the good of the species" is wrong by default — Robbins will mark this as the trap answer.</li>
  <li>Group selection isn't strictly impossible — but the conditions are narrow and rarely met.</li>
</ul>` },

    "Hawk-Dove ESS when V ≥ C (pure-Hawk case)": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> If V ≥ C, the formula p* = V/C exits its valid domain — pure-Hawk wins. Robbins WILL exam-trap this with V &gt; C numbers.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>V &lt; C: mixed ESS at p* = V/C, between 0 and 1.</li>
  <li>V ≥ C: pure-Hawk ESS (formula gives p* &gt; 1, nonsense).</li>
  <li>V=15, C=10: p* = 1.5 → out of domain → pure-Hawk wins.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Domain awareness.</strong> p* &gt; 1 is the signal that the mixed-ESS formula doesn't apply — switch to pure-Hawk.</li>
  <li><strong>Fight payoff stays positive.</strong> When V ≥ C, even Hawk-vs-Hawk yields ½(V−C) ≥ 0 — fighting always pays.</li>
  <li><strong>Doves can't invade.</strong> Hawks beat Doves head-to-head, and Hawk-vs-Hawk is non-negative — no entry point for Doves.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>Don't blindly compute p* = V/C without checking the V vs C ordering.</li>
  <li>Symmetric trap: p* &lt; 0 means pure-Dove ESS (extreme cost dominance).</li>
</ul>` }
  });

  // ===================== L14: HISTORY OF LIFE =====================
  window.addCardPatches('L14', {
    "Radiometric dating": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Match the isotope to the timescale — Robbins will give you a fossil age and ask which dating system to use.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li><strong>¹⁴C (carbon-14)</strong>: half-life 5,730 yr. Useful to ~50,000 yr.</li>
  <li><strong>K-Ar (potassium-argon)</strong>: half-life 1.25 Gyr. Millions to billions.</li>
  <li><strong>U-Pb (uranium-lead) in zircons</strong>: half-life 4.5 Gyr. Gold standard for deep time, dates Earth at 4.568 Gyr.</li>
  <li>Logic: Age = ln(1+D/P)/λ, where D/P = daughter/parent ratio.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Bracketing logic.</strong> Date volcanic ash above and below a fossil to bracket the fossil's age — sedimentary rock isn't datable directly.</li>
  <li><strong>Anchors the entire timeline.</strong> Every MYA on the L14 chart traces back to radiometric dates.</li>
  <li><strong>Match the isotope to the question.</strong> ¹⁴C for archaeology, U-Pb for the Hadean.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>¹⁴C cannot date dinosaurs — they're 66 Mya, too old by ~11,500 half-lives.</li>
  <li>Earth is 4.568 Gyr (radiometric of meteorites/zircons), NOT the age of the oldest rocks (~4.0 Gyr).</li>
</ul>` },

    "Half-life": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Half-life math — fraction remaining after n half-lives is (½)ⁿ. Robbins WILL ask you to compute remaining fraction at a given time.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>¹⁴C half-life: 5,730 yr.</li>
  <li>After 5 half-lives: (½)⁵ = 1/32 ≈ 3.1% remaining.</li>
  <li>Practical detection limit: ~10 half-lives → ¹⁴C maxes out at ~50,000 yr.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Direct calculation.</strong> Time / half-life = number of half-lives n; fraction = (½)ⁿ.</li>
  <li><strong>Why ¹⁴C fails on dinosaurs.</strong> 66 Mya / 5,730 yr ≈ 11,500 half-lives → essentially zero ¹⁴C left.</li>
  <li><strong>Constant rate independent of conditions.</strong> Temperature, pressure, chemistry don't affect half-life — pure nuclear decay.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>Half-life is the time for HALF the parent to decay, not all of it. After 2 half-lives you're at 1/4, not zero.</li>
  <li>Match scale to half-life: don't try ¹⁴C on a million-year-old fossil.</li>
</ul>` },

    "Biomarker": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Biomarkers are CHEMICAL fossils — stable lipid signatures that survive in rocks where bodily fossils don't.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Earliest biomarker evidence: ~3.5-3.8 Gya for life.</li>
  <li>Steranes (stable steroids) suggest eukaryotes by ~1.6 Gya.</li>
  <li>Caveat: contamination by younger biology is the main concern → some dates revised.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Chemical evidence where fossils fail.</strong> Soft-bodied early life left no morphology — biomarkers are the only signal.</li>
  <li><strong>Steranes = eukaryote signature.</strong> Sterols require O₂-dependent biosynthesis absent in most prokaryotes.</li>
  <li><strong>Weaker than fossils.</strong> Indirect — vulnerable to contamination, but valuable when nothing else exists.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>Biomarkers ≠ fossils — they're CHEMICAL signatures, not preserved bodies.</li>
  <li>A biomarker date is only as good as the absence of contamination from younger material.</li>
</ul>` },

    "Great Oxidation Event": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> ~2.4 Gya, cyanobacteria flooded the atmosphere with O₂ — Robbins WILL ask you to date and explain the GOE.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Date: <strong>~2.4 Gya</strong>.</li>
  <li>Cyanobacteria evolved oxygenic photosynthesis ~3.0 Gya.</li>
  <li>~600 Myr LAG between cyanobacterial origin and atmospheric O₂ rise — buffered by Fe²⁺ ocean (banded iron formations, BIFs).</li>
  <li>Atmospheric O₂ rose from &lt;0.001% to ~10%.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>"Mass extinction" of obligate anaerobes.</strong> O₂ is corrosive to anaerobic biochemistry — survivors retreated to anoxic refugia.</li>
  <li><strong>Aerobic respiration unlocked.</strong> ~18× more ATP per glucose than fermentation → larger cells, active animals.</li>
  <li><strong>Set up eukaryotes + multicellularity.</strong> Mitochondrial endosymbiosis (~2 Gya) and ozone layer formation depend on O₂.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>The 600-Myr buffer (BIFs) is geochemistry, not biology — iron sink had to fill before atmospheric O₂ could accumulate.</li>
  <li>Don't confuse GOE (~2.4 Gya, atmospheric O₂) with origin of cyanobacterial photosynthesis (~3.0 Gya, biological).</li>
</ul>` },

    "Cambrian explosion": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> ~541-520 MYA, most modern animal phyla appear in the fossil record over ~20 Myr — but it's partly a fossilization artifact.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Window: <strong>~541-520 MYA</strong> (~20 Myr duration).</li>
  <li>Most modern animal phyla appear (~30+ phyla in the fossil record).</li>
  <li>Burgess Shale (Anomalocaris, etc.) is a key Lagerstätte preserving soft tissues.</li>
  <li>Molecular clocks place phylum splits at 700+ Mya — predates the fossil "explosion".</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Hard parts evolved.</strong> Shells and exoskeletons preserve — soft-bodied predecessors mostly don't. The "explosion" is partly the appearance of FOSSILIZABLE forms.</li>
  <li><strong>Drivers debated.</strong> O₂ rising past metabolic threshold; Hox/Pax regulatory toolkits enabling body-plan experiments; predator-prey arms races.</li>
  <li><strong>Geological "rapid".</strong> 20 Myr is fast on geological timescales but slow biologically — plenty of time for body-plan evolution.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>The Cambrian explosion is the appearance of HARD PARTS, NOT necessarily the origin of the phyla themselves.</li>
  <li>Don't call it "instant" — 20 Myr is fast on a 4.5 Gyr scale, but not literally rapid.</li>
</ul>` },

    "Devonian": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Devonian = "Age of Fishes" + the tetrapod transition — Robbins WILL pair this period with its key biological events.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Date range: <strong>~419-359 MYA</strong>.</li>
  <li>Jawed fish radiation (placoderms, sharks, bony fish).</li>
  <li>Tiktaalik (~375 Mya): sarcopterygian fish with weight-bearing limbs, mobile neck, lungs — the canonical tetrapod intermediate.</li>
  <li>Ends with the Late Devonian mass extinction (one of Big Five).</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Tetrapod origin.</strong> Lobe-finned fish (sarcopterygians) acquire weight-bearing limbs and air-breathing lungs → first land vertebrates.</li>
  <li><strong>"Age of Fishes" — exam pairing.</strong> Devonian + jawed-vertebrate radiation is a canonical exam association.</li>
  <li><strong>Forests emerge.</strong> First true forests of vascular plants and seed plants transform continental ecosystems.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>Don't confuse Devonian (fish-to-tetrapod) with Cambrian (origin of phyla) or Permian (mass extinction).</li>
  <li>Tiktaalik is sarcopterygian (lobe-finned), NOT actinopterygian (ray-finned) — only sarcopterygians gave rise to tetrapods.</li>
</ul>` },

    "Permian": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Permian = origin of reptiles + synapsids, ends with the LARGEST mass extinction in Earth history. Robbins will absolutely test this period.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Date range: <strong>~299-252 MYA</strong>.</li>
  <li>End-Permian extinction: ~252 MYA, <strong>~95% marine species lost</strong> (estimates 81-96%).</li>
  <li>Cause: Siberian Traps flood-basalt volcanism + CO₂/SO₂ release + ocean acidification + warming + anoxia.</li>
  <li>Often called "the Great Dying."</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Largest mass extinction ever.</strong> ~95% marine species, ~70% terrestrial vertebrate species — biggest of the Big Five.</li>
  <li><strong>Origin of reptiles + synapsids.</strong> Synapsids (proto-mammals) evolved during the Permian.</li>
  <li><strong>Reset of evolutionary trajectories.</strong> Survivors gave rise to the Mesozoic dinosaur-and-mammal world.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>Don't confuse Permian-Triassic (~252 Mya, biggest) with K-Pg (~66 Mya, dinosaurs). PT &gt; K-Pg in severity.</li>
  <li>Cause = Siberian Traps (volcanism), NOT an asteroid (that's K-Pg).</li>
</ul>` },

    "Mass extinction": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Big Five mass extinctions in time order — Ordovician, Devonian, Permian, Triassic, Cretaceous. Robbins WILL ask you to rank them.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Definition: &gt;75% species loss in geologically rapid time.</li>
  <li><strong>End-Ordovician</strong>: ~444 MYA</li>
  <li><strong>Late Devonian</strong>: ~375 MYA</li>
  <li><strong>End-Permian</strong>: ~252 MYA — LARGEST (~95% marine)</li>
  <li><strong>End-Triassic</strong>: ~201 MYA</li>
  <li><strong>End-Cretaceous (K-Pg)</strong>: ~66 MYA — dinosaurs out, mammals in</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>End-Permian was most severe.</strong> Cause: Siberian Traps + acidification.</li>
  <li><strong>K-Pg was most evolutionarily consequential.</strong> Ended dinosaur reign; mammals radiated within ~10 Myr.</li>
  <li><strong>Mass extinctions create opportunity.</strong> Empty niches → adaptive radiations of survivors.</li>
  <li><strong>Sixth mass extinction.</strong> Many biologists argue we're in one now (human-driven).</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>Permian = biggest; K-Pg = most famous. Don't blur them.</li>
  <li>Big Five order: O-D-P-T-C (Ordovician, Devonian, Permian, Triassic, Cretaceous).</li>
</ul>` },

    "K-T (K-Pg) boundary": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> 66 MYA, Chicxulub asteroid → iridium layer → non-avian dinosaurs gone → mammal radiation. Most famous mass extinction.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Date: <strong>~66 MYA</strong>.</li>
  <li>Crater: Chicxulub, Yucatán Peninsula, Mexico (~150 km diameter).</li>
  <li>Iridium layer: global, in K-Pg sediments worldwide.</li>
  <li>Dinosaurs (non-avian), ammonites, mosasaurs, plesiosaurs all extinguished.</li>
  <li>Mammalian radiation: within ~10 Myr post-event.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Asteroid impact, not volcanism.</strong> The iridium layer is the smoking gun (Alvarez et al. 1980).</li>
  <li><strong>Cleared dinosaur niches.</strong> Mammals — small/nocturnal for ~150 Myr — radiated into large-body, arboreal, aquatic forms.</li>
  <li><strong>Boundary marker.</strong> K = Cretaceous, Pg = Paleogene. Old name K-T (Tertiary, deprecated).</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>K-Pg killed NON-AVIAN dinosaurs — birds (avian dinosaurs) survived.</li>
  <li>Don't conflate with Permian-Triassic (much bigger, much earlier, volcanic, no asteroid).</li>
</ul>` },

    "Iridium layer": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> The iridium layer is the GLOBAL geochemical fingerprint of the Chicxulub asteroid — it's the primary evidence for the K-Pg impact hypothesis.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Iridium: rare in Earth's crust (sank into core), abundant in chondritic asteroids.</li>
  <li>Found globally in K-Pg sediments (~66 Mya) on every continent.</li>
  <li>Co-occurs with shocked-quartz grains and microspherules — diagnostic of hypervelocity impact.</li>
  <li>Discovered by Alvarez et al. 1980.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Smoking gun for asteroid impact.</strong> No volcanic mechanism produces this combination globally.</li>
  <li><strong>Worldwide spike.</strong> Same layer in same age sediments on every continent — must be extraterrestrial.</li>
  <li><strong>Confirmed by Chicxulub crater.</strong> Buried 150-km crater off Yucatán matches the size and timing.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>Iridium itself doesn't kill dinosaurs — it's the FINGERPRINT of the impact, not the cause of extinction.</li>
  <li>Don't confuse with the K-Pg boundary itself (the layer marks the boundary, but they're different concepts).</li>
</ul>` },

    // ==== L14 EXTRAS ====
    "Major life-history milestones (timeline)": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> The full timeline (4.5 Ga to today) is pure memorization — Robbins WILL ask you to put events in chronological order.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li><strong>4.568 Gya</strong>: Earth forms.</li>
  <li><strong>3.5-3.8 Gya</strong>: first cells (microbial mats, biomarkers).</li>
  <li><strong>2.4 Gya</strong>: Great Oxidation Event (GOE).</li>
  <li><strong>2.1-1.6 Gya</strong>: first eukaryotes (mitochondrial endosymbiosis ~2 Gya).</li>
  <li><strong>~1 Gya</strong>: multicellularity; chloroplast endosymbiosis.</li>
  <li><strong>720-635 Ma</strong>: Snowball Earth.</li>
  <li><strong>541 Ma</strong>: Cambrian explosion.</li>
  <li><strong>252 Ma</strong>: end-Permian extinction.</li>
  <li><strong>66 Ma</strong>: K-Pg extinction.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Order question.</strong> Order GOE, eukaryotes, multicell, Cambrian, Permian, K-Pg from oldest to youngest. Get the sequence wrong and you fail.</li>
  <li><strong>Mnemonic GEM-CPK</strong>: GOE · Eukaryotes · Multicell · Cambrian · Permian · K-Pg.</li>
  <li><strong>Anchor every L14 question.</strong> Every other L14 fact hangs on this timeline.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>Cambrian (541 Ma) is younger than multicellularity (~1 Gya) — don't blur them.</li>
  <li>End-Permian (252) is OLDER than K-Pg (66) by ~186 Myr.</li>
</ul>` },

    "Big Five mass extinctions": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Memorize all five names, dates, and primary causes — Robbins explicitly tests this.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li><strong>End-Ordovician (~444 Ma)</strong>: glaciation + sea-level drop.</li>
  <li><strong>Late Devonian (~375 Ma)</strong>: anoxia, prolonged event.</li>
  <li><strong>End-Permian (~252 Ma)</strong>: Siberian Traps + acidification — LARGEST (~95% marine).</li>
  <li><strong>End-Triassic (~201 Ma)</strong>: Central Atlantic Magmatic Province volcanism.</li>
  <li><strong>End-Cretaceous / K-Pg (~66 Ma)</strong>: Chicxulub asteroid + iridium — dinosaurs out.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Order: O-D-P-T-C</strong> in time. Drill this.</li>
  <li><strong>Each event reshaped post-event radiation.</strong> Empty niches → survivors radiate non-randomly.</li>
  <li><strong>K-Pg = mammal radiation.</strong> Empty dinosaur niches let mammals diversify.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>Permian = biggest, K-Pg = most famous. Don't swap them.</li>
  <li>Causes vary — only K-Pg is asteroid-driven; the others are volcanic/climatic.</li>
</ul>` },

    "Radiometric dating logic": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Match the isotope's half-life to the age range you want — Robbins WILL trap you on isotope choice.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Age formula: <strong>Age = ln(1 + D/P) / λ</strong>, where D/P = daughter/parent ratio, λ = decay constant.</li>
  <li>¹⁴C: half-life 5,730 yr → useful to ~50,000 yr.</li>
  <li>K-Ar: half-life 1.25 Gyr → millions to billions.</li>
  <li>U-Pb (zircons): half-life 4.5 Gyr → billions; dates Earth at 4.568 Gyr.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Match scale to half-life.</strong> Useful range ≈ 10 half-lives.</li>
  <li><strong>Why ¹⁴C fails on dinosaurs.</strong> 66 Mya / 5,730 yr ≈ 11,500 half-lives → effectively zero parent left.</li>
  <li><strong>Zircons.</strong> U-Pb in zircons is the gold standard for deep time — zircons are robust and exclude lead at crystallization.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>Don't try ¹⁴C on anything &gt; ~50,000 yr.</li>
  <li>You date IGNEOUS rocks (volcanic ash, zircons) to bracket sedimentary fossils, not the fossils themselves.</li>
</ul>` },

    "Great Oxidation Event — cause and consequence": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> The 600-Myr buffer (Fe²⁺ ocean) explains why GOE happened ~600 Myr AFTER cyanobacteria evolved oxygenic photosynthesis.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Cyanobacteria evolved oxygenic photosynthesis: ~3.0 Gya.</li>
  <li>GOE: ~2.4 Gya.</li>
  <li>Lag: ~600 Myr.</li>
  <li>Iron sink: dissolved Fe²⁺ in oceans → reacted with O₂ → precipitated as Fe³⁺ → BANDED IRON FORMATIONS (BIFs) on seafloor.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Geochemistry sets timing, not biology.</strong> O₂ was scrubbed by Fe²⁺ for 600 Myr — only when iron sink ran out did atmospheric O₂ accumulate.</li>
  <li><strong>BIFs as proxy.</strong> Banded iron formations are the rock-record signature of the iron-buffering phase.</li>
  <li><strong>Triggers the cascade.</strong> Atmospheric O₂ → ozone layer + aerobic respiration + extinction of obligate anaerobes.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>Don't confuse GOE date (~2.4 Gya) with origin of oxygenic photosynthesis (~3.0 Gya).</li>
  <li>BIFs are PRE-GOE record (during the buffering phase) — they STOP forming once Fe²⁺ depletes and atmospheric O₂ rises.</li>
</ul>` },

    "Cambrian explosion — what drove the radiation?": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Three competing drivers: O₂ threshold, Hox toolkit, predator-prey arms race — Robbins WILL ask you to evaluate them.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Window: ~541-520 MYA (~20 Myr).</li>
  <li>~30+ animal phyla appear in fossil record.</li>
  <li>Burgess Shale (~508 Mya, BC): Anomalocaris, Hallucigenia, Opabinia — exceptional soft-tissue preservation.</li>
  <li>Molecular clocks place phylum splits at 700+ Mya.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>O₂ threshold.</strong> Active large-body animals require sustained aerobic metabolism — O₂ may have crossed the threshold then.</li>
  <li><strong>Hox/Pax/Wnt regulatory toolkit.</strong> Already in place; Cambrian saw their first body-plan experiments.</li>
  <li><strong>Arms-race hypothesis.</strong> Predators select for armor, vision, burrowing → fossilizable hard parts emerge.</li>
  <li><strong>Fossilization artifact.</strong> Soft-bodied predecessors had been diversifying for 100+ Myr (Ediacaran).</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>The "explosion" is partly the appearance of HARD PARTS, not the origin of phyla per se.</li>
  <li>Molecular clocks predate the fossil "explosion" — phyla split BEFORE they fossilize.</li>
</ul>` },

    "Geological eras — Paleozoic / Mesozoic / Cenozoic": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Three eras in time order — Paleozoic → Mesozoic → Cenozoic. Drill the date ranges and signature events.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li><strong>Paleozoic ("old life", 541-252 Mya)</strong>: Cambrian explosion, fishes, amphibians, early reptiles. Ends with Permian extinction.</li>
  <li><strong>Mesozoic ("middle life", 252-66 Mya)</strong>: Triassic, Jurassic, Cretaceous. Age of dinosaurs.</li>
  <li><strong>Cenozoic ("new life", 66 Mya-now)</strong>: mammalian radiation post-K-Pg.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Eras bookend the Big Five.</strong> Paleozoic ends at the BIGGEST extinction (Permian). Mesozoic ends at the most famous (K-Pg).</li>
  <li><strong>Mammal trajectory.</strong> Appeared in late Triassic (~225 Mya); stayed small under dinosaurs; exploded after K-Pg (66 Mya).</li>
  <li><strong>Mnemonic PMC</strong>: Paleo · Meso · Ceno.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>Don't conflate "first appeared" with "first dominated". Mammals first appeared late Triassic; first dominated early Cenozoic.</li>
  <li>Devonian (Age of Fishes) is a PERIOD inside Paleozoic, not an era of its own.</li>
</ul>` },

    "Endosymbiosis evidence (Margulis)": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Mitochondria + chloroplasts came from engulfed bacteria — Lynn Margulis's hypothesis is now consensus, with rRNA sequencing as the clincher.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Mitochondrial endosymbiosis: <strong>~2 Gya</strong> (alphaproteobacterial ancestor).</li>
  <li>Chloroplast endosymbiosis: <strong>~1 Gya</strong> (cyanobacterial ancestor).</li>
  <li>Five lines of evidence: (1) circular DNA, (2) bacterial-like ribosomes, (3) double membranes, (4) binary fission, (5) rRNA phylogeny.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>rRNA sequencing was the clincher.</strong> Mitochondrial 16S rRNA grouped with alphaproteobacteria (Rickettsia-related); chloroplast rRNA with cyanobacteria. No way around it.</li>
  <li><strong>Double membranes are diagnostic.</strong> Outer = host vesicle, inner = bacterial.</li>
  <li><strong>Resolves eukaryote origin.</strong> Eukaryotes are bacteria-archaea chimeras with energy organelles.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>Plastids ≠ "evolved chloroplasts in plants" — they're engulfed cyanobacteria, separately from mitochondria.</li>
  <li>Margulis's idea was rejected for ~15 years before sequencing vindicated it.</li>
</ul>` }
  });

  // ===================== L15: PHYLOGENETICS =====================
  window.addCardPatches('L15', {
    "Tip / Terminal taxon": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Tips = the named taxa at branch ends — every extant species in a tree is necessarily a tip.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Three tree elements: TIPS (terminal taxa), NODES (common ancestors), BRANCHES (lineages through time).</li>
  <li>Tips are labeled; nodes usually unlabeled.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Tree-thinking foundation.</strong> Robbins WILL ask you to identify a tip vs node vs branch — basic tree literacy.</li>
  <li><strong>What's being classified.</strong> Tips are the organisms; nodes are inferred ancestors.</li>
  <li><strong>Reading direction.</strong> Trace from tip back toward root for evolutionary history.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>Tips can be EXTANT or EXTINCT — fossil taxa appear at tips on internal branches that don't reach today.</li>
  <li>An "ancestor" of a modern species is a NODE, not a tip.</li>
</ul>` },

    "Node": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> A node = the most recent common ancestor of all descendants above it. NODES define relationships, not tip placement.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Each node represents one inferred common ancestor.</li>
  <li>Node depth (distance from tips) ≈ time since divergence (in time-calibrated trees).</li>
  <li>Sister groups share an IMMEDIATE common ancestor — one node.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Closeness measured by node depth.</strong> Two taxa sharing a recent node are more closely related than those sharing a deeper node.</li>
  <li><strong>NOT page distance.</strong> Trees rotate freely — tip ordering on the page is irrelevant.</li>
  <li><strong>Tree-thinking primary skill.</strong> Robbins exam-traps page-distance vs node-depth confusion.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>Two tips drawn next to each other are NOT necessarily sister groups — trace back to the node.</li>
  <li>A "ladder-tree" looks like one taxon is "more evolved" — wrong; all extant tips are equally evolved.</li>
</ul>` },

    "Branch": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> A branch = a lineage existing through time. Branch LENGTH may encode time, character changes, or nothing — read the legend.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Length can represent: (a) TIME (chronogram), (b) NUMBER OF CHANGES (phylogram), or (c) be UNINFORMATIVE (cladogram).</li>
  <li>Time-calibrated trees use radiometric/molecular-clock anchors.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Length convention matters.</strong> A long branch in a phylogram = many changes; in a chronogram = long time.</li>
  <li><strong>Long-branch attraction.</strong> Long branches that accumulate changes can spuriously cluster — parsimony fails here.</li>
  <li><strong>Reading correctly.</strong> Always check whether the tree is scaled, and to what.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>A long branch isn't necessarily an "older" lineage — could just have evolved fast.</li>
  <li>Cladograms (no length info) only show topology — don't try to time-read them.</li>
</ul>` },

    "Sister groups": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Sister groups share a single immediate common ancestor — the diagnostic of "most closely related" pairs.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Sisters share ONE NODE — the immediate common ancestor.</li>
  <li>Chimps + humans = sister groups; gorillas are an outgroup.</li>
  <li>Sister-group relationships are SYMMETRIC — neither is "more closely related" than the other to the third.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Definition of "most closely related".</strong> Closeness = recency of common ancestor = sister relationship.</li>
  <li><strong>Reading from a tree.</strong> Identify sister groups by tracing back to the NEAREST shared node.</li>
  <li><strong>Symmetry.</strong> A is sister to B iff B is sister to A — there's no "directionality".</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>Page-adjacent tips are NOT necessarily sisters — trees rotate at any node.</li>
  <li>"More derived" ≠ "more closely related" — sisterhood is symmetric.</li>
</ul>` },

    "Synapomorphy": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> ONLY SYNAPOMORPHIES — shared derived characters — define monophyletic groups. This is THE foundational discriminator on L15.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Synapomorphy = shared + derived = clade-defining.</li>
  <li>Compare: symplesiomorphy = shared + ancestral = useless for grouping.</li>
  <li>Compare: homoplasy = independent acquisition = misleading.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Foundation of cladistics.</strong> Hennig's principle: only synapomorphies build clades.</li>
  <li><strong>Level-relative.</strong> "Has a backbone" is a synapomorphy of vertebrates as a whole, but a SYMPLESIOMORPHY for any subgroup like mammals.</li>
  <li><strong>Outgroup polarizes.</strong> An outgroup tells you which state is ancestral (synapomorphy) vs derived (the new state).</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>Synapomorphies are LEVEL-DEPENDENT — a feature is a synapomorphy at one level and a symplesiomorphy at a deeper level.</li>
  <li>Without an outgroup, you can't distinguish synapomorphy from symplesiomorphy.</li>
</ul>` },

    "Symplesiomorphy": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Shared ANCESTRAL state — uninformative about which lineages cluster within a clade. The classic exam trap.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>"Has a backbone" is a synapomorphy of vertebrates → SYMPLESIOMORPHY of mammals (all mammals have one because the ancestor did).</li>
  <li>Symplesiomorphies are widespread in a clade because the COMMON ANCESTOR had the trait.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Same trait, different role at different levels.</strong> "Has hair" is a synapomorphy of mammals, but a symplesiomorphy when grouping mammal subclades.</li>
  <li><strong>Why outgroup matters.</strong> The outgroup tells you which state is ancestral (= symplesiomorphy in the ingroup).</li>
  <li><strong>Discriminator question.</strong> Robbins WILL give you a trait and ask synapomorphy vs symplesiomorphy at a stated level.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>Symplesiomorphy doesn't mean "wrong" — it just means "uninformative for grouping AT THIS LEVEL".</li>
  <li>The same character can flip role depending on the focal clade. Check the level.</li>
</ul>` },

    "Homoplasy": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Convergent traits look like synapomorphies but came from INDEPENDENT origin — bat wings vs bird wings is the textbook example.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Three flavors: CONVERGENCE (independent origin in distantly related lineages), PARALLELISM (similar trait via similar developmental pathway in close lineages), REVERSAL (loss of derived state).</li>
  <li>Bat wings vs bird wings = convergence.</li>
  <li>Long-branch attraction can spuriously group homoplasic taxa.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Misleads phylogeny.</strong> Homoplasies look like synapomorphies but aren't — they don't imply common ancestry.</li>
  <li><strong>Bat wings + bird wings.</strong> Both fly, but the COMMON ANCESTOR did NOT have wings → independent origins.</li>
  <li><strong>Distinguishing test.</strong> Check whether the common ancestor had the trait. If no, it's homoplasy.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>Distantly related lineages sharing a feature → suspect homoplasy first.</li>
  <li>Parsimony picks the tree with FEWEST changes — but penalizes homoplasy = systematic error in fast-evolving sites.</li>
</ul>` },

    "Clade / Monophyletic group": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Monophyletic = ancestor + ALL descendants. The ONLY valid taxonomic group in modern systematics.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Monophyletic = "M-all" (mnemonic): ancestor + all.</li>
  <li>Defined by SYNAPOMORPHIES.</li>
  <li>Mammals + ancestor + all descendants = mammals (monophyletic).</li>
  <li>Aves (birds) is monophyletic; "Reptilia" without birds is NOT.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Modern systematics rejects para- and polyphyletic groups.</strong> Only monophyletic groups reflect evolutionary units.</li>
  <li><strong>Defines a clade.</strong> Synapomorphies are the diagnostic; a node + everything above it = a clade.</li>
  <li><strong>Discriminator question.</strong> Robbins WILL ask you to classify a named group as mono/para/polyphyletic.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>If the group EXCLUDES some descendants → paraphyletic, not monophyletic.</li>
  <li>If the group is built from convergent traits → polyphyletic, not monophyletic.</li>
</ul>` },

    "Paraphyletic group": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Paraphyletic = ancestor + SOME descendants (not all). "Reptiles" excluding birds is the canonical example.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Paraphyletic = "P-art" (mnemonic): ancestor + part.</li>
  <li>"Reptilia" without birds = paraphyletic (birds nest within reptiles).</li>
  <li>"Fish" excluding tetrapods = paraphyletic.</li>
  <li>Modern fix: include birds in "Reptilia" (use "Sauropsida"), or use crown-group names.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>REJECTED in modern systematics.</strong> Paraphyletic groups don't reflect evolutionary units.</li>
  <li><strong>Birds nest within reptiles.</strong> Birds are descended from theropod dinosaurs → leaving them out makes "reptiles" paraphyletic.</li>
  <li><strong>Diagnostic test.</strong> If the group has a common ancestor but excludes some of its descendants → paraphyletic.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>"Reptiles" in everyday usage IS paraphyletic — that's the point of the example.</li>
  <li>"Apes excluding humans" = paraphyletic. Don't fall for it.</li>
</ul>` },

    "Polyphyletic group": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Polyphyletic = members lacking a SHARED IMMEDIATE COMMON ANCESTOR — built from CONVERGENT traits. "Warm-blooded animals" is the canonical example.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Polyphyletic = "P-ick-and-mix" (mnemonic): no shared immediate ancestor.</li>
  <li>"Warm-blooded animals" (mammals + birds) = polyphyletic — endothermy evolved INDEPENDENTLY.</li>
  <li>"Flying vertebrates" (bats + birds + pterosaurs) = polyphyletic — flight evolved 3 times.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>REJECTED in modern systematics.</strong> Polyphyletic groups are diagnostic of HOMOPLASY, not common ancestry.</li>
  <li><strong>Convergence creates polyphyly.</strong> Group built from "all who fly" combines independently evolved traits.</li>
  <li><strong>Diagnostic test.</strong> If the trait used to define the group evolved INDEPENDENTLY in lineages → polyphyletic.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>Polyphyletic ≠ paraphyletic. Para has a shared ancestor (just not all descendants); poly doesn't.</li>
  <li>"Vertebrates with wings" = polyphyletic (bats, birds, pterosaurs all evolved wings independently).</li>
</ul>` },

    "Biological Species Concept (BSC)": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Mayr's BSC = interbreeding populations reproductively isolated from others. The most famous concept BUT it has clear limits.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Strength: clear mechanism (gene flow as the test).</li>
  <li>Limit: can't apply to ASEXUAL organisms (bacteria, parthenogens).</li>
  <li>Limit: can't apply to FOSSILS (no breeding tests possible).</li>
  <li>Mules = horse × donkey hybrid, sterile → horses and donkeys ARE good biological species.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Most-cited species concept.</strong> Robbins will assume you can name and apply it.</li>
  <li><strong>Reproductive isolation as the criterion.</strong> Hybrid sterility/inviability supports BSC even with occasional hybridization.</li>
  <li><strong>Limits drive the alternatives.</strong> Where BSC fails (asexuals, fossils), use morphological or phylogenetic concepts.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>Two populations that occasionally hybridize CAN still be BSC species if hybrids have reduced fitness.</li>
  <li>Bacteria are not BSC species — they reproduce asexually and exchange genes horizontally.</li>
</ul>` },

    "Morphological species concept": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Species defined by DIAGNOSABLE FORM differences. Most useful for fossils and asexuals where BSC fails.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Strength: usable on fossils and any organism.</li>
  <li>Limit: CRYPTIC SPECIES (reproductively isolated, morphologically nearly identical).</li>
  <li>Limit: morphological PLASTICITY can mask true species boundaries.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Paleontology's workhorse.</strong> Fossils have only bones and teeth — morphology is all you've got.</li>
  <li><strong>Cryptic species break it.</strong> Cryptic skipper butterflies are reproductively isolated but look the same → BSC works, morphology fails.</li>
  <li><strong>Plasticity confounds it.</strong> Same genome can produce different morphs in different environments.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>Morphological concept FAILS on cryptic species — they're separate biologically but indistinguishable morphologically.</li>
  <li>Don't use for asexuals if you can apply phylogenetic concept instead.</li>
</ul>` },

    "Phylogenetic species concept": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Species = smallest monophyletic group identifiable by shared derived characters. Works for asexuals + fossils.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Strength: works for ASEXUALS and FOSSILS.</li>
  <li>Limit: depends on chosen MOLECULAR/MORPHOLOGICAL markers.</li>
  <li>Tendency: AGGRESSIVELY SPLITS lineages → many "species" recognized vs BSC.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Bridges BSC's limits.</strong> Asexual bacteria can be defined as species under PSC.</li>
  <li><strong>Synapomorphy-based.</strong> Same logic as cladistics — shared derived characters define the group.</li>
  <li><strong>Threshold problem.</strong> What level of genetic divergence counts? Controversial.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>PSC tends to split lineages MORE than BSC — same data can yield very different species counts.</li>
  <li>Marker choice matters — different genes can produce different "phylogenetic species".</li>
</ul>` },

    // ==== L15 EXTRAS ====
    "Reading a phylogenetic tree — closeness rule": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Closeness = NODE DEPTH, NOT page distance. Trees rotate at any node — page layout is irrelevant.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Closeness rule: trace back to the SHARED NODE; closer node = closer relationship.</li>
  <li>Trees can rotate 180° at any node without changing relationships.</li>
  <li>Information lives in TOPOLOGY (connections) + BRANCH LENGTHS, not in page layout.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>The #1 tree-reading exam trap.</strong> Robbins will draw two trees that look different but are topologically identical.</li>
  <li><strong>Mouse-human-chimp example.</strong> If tree is (mouse, (human, chimp)), human and chimp are sisters even if mouse is drawn next to one of them.</li>
  <li><strong>Reflex check.</strong> Count NODES between taxa, not pixels.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>Two taxa drawn next to each other ≠ sister groups.</li>
  <li>Trees with the same topology look very different visually — focus on connections.</li>
</ul>` },

    "Synapomorphy vs symplesiomorphy vs homoplasy": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Three character types — only synapomorphies define clades. This is THE classification question on L15.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>SYNAPOMORPHY = shared + DERIVED → defines a clade (informative).</li>
  <li>SYMPLESIOMORPHY = shared + ANCESTRAL → uninformative for grouping.</li>
  <li>HOMOPLASY = independent acquisition (convergence/parallelism/reversal) → misleading.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Foundation of cladistics.</strong> Only synapomorphies build trees correctly.</li>
  <li><strong>Examples to memorize.</strong> Feathers in birds = synapomorphy. Vertebrae in birds = symplesiomorphy (vs all vertebrates). Wings in bats + birds = homoplasy.</li>
  <li><strong>Same trait, different roles.</strong> "Has hair" is synapomorphy of mammals, symplesiomorphy of mammal subclades.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>Without an outgroup, you cannot distinguish synapomorphy from symplesiomorphy.</li>
  <li>Distantly related lineages sharing a trait → suspect homoplasy first.</li>
</ul>` },

    "Monophyletic / paraphyletic / polyphyletic": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Three group types — only monophyletic is valid. Robbins WILL ask you to classify named groups.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li><strong>MONOPHYLETIC</strong> (clade) = ancestor + ALL descendants. VALID.</li>
  <li><strong>PARAPHYLETIC</strong> = ancestor + SOME descendants. Example: "Reptilia" without birds.</li>
  <li><strong>POLYPHYLETIC</strong> = no shared immediate ancestor. Example: "warm-blooded animals" (mammals + birds).</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Modern systematics rejects para- and poly.</strong> Only mono reflects evolutionary units.</li>
  <li><strong>Mnemonic: M-all, P-art, P-ick-and-mix.</strong></li>
  <li><strong>Discriminator test.</strong> Asks: does the group include the ancestor? Does it include ALL descendants?</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>"Reptiles" excluding birds = PARAPHYLETIC, not polyphyletic.</li>
  <li>"Warm-blooded animals" = POLYPHYLETIC, not paraphyletic.</li>
  <li>The DIFFERENCE: para has a shared ancestor (just incomplete); poly doesn't share an immediate ancestor.</li>
</ul>` },

    "Outgroup": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> An outgroup is a taxon known to lie OUTSIDE the clade being studied — it ROOTS the tree and POLARIZES character states.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Used to ROOT the tree (orient direction of time).</li>
  <li>Used to POLARIZE characters (which state is ancestral, which derived).</li>
  <li>Outgroup must be CONFIDENTLY OUTSIDE the ingroup AND share enough characters to be alignable.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Without polarization, no synapomorphy.</strong> Can't distinguish synapomorphy from symplesiomorphy without an outgroup.</li>
  <li><strong>Bad outgroup ruins everything.</strong> Too close → biases tree; nested in ingroup → misroots tree.</li>
  <li><strong>Primate example.</strong> Studying primates → use tree shrews or mice as outgroup.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>The outgroup tells you the ANCESTRAL state in the ingroup — that's its information value.</li>
  <li>Without a defined outgroup, the tree can't be rooted (only unrooted tree is possible).</li>
</ul>` },

    "Crown group vs stem group": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Crown = MRCA of all LIVING members + descendants. Stem = extinct lineages branching off before the crown.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>CROWN birds: all living birds + their MRCA + descendants. Crown Aves arose ~70 MYA.</li>
  <li>STEM birds: Archaeopteryx and other early feathered dinosaurs (~150 MYA).</li>
  <li>Stem fossils preserve mosaic of ancestral + derived traits.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Resolves "transitional fossil" awkwardness.</strong> Archaeopteryx isn't a "misfit" — it's a stem bird with bird-feathers + dinosaur-teeth.</li>
  <li><strong>Separates trait origins from clade origins.</strong> Feathers ~150 Mya; modern bird crown ~70 Mya. Different events.</li>
  <li><strong>Reconciles paleontology + molecular phylogenetics.</strong> Both can agree on stem-vs-crown timings.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>"Modern birds" = crown Aves, not all stem-birds.</li>
  <li>Stem groups are EXTINCT — by definition, they branched off before the modern crown.</li>
</ul>` },

    "Maximum parsimony": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Parsimony picks the tree requiring the FEWEST evolutionary changes — but fails when long branches accumulate convergent changes.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Criterion: fewest character changes wins.</li>
  <li>Assumption: evolution is rare, homoplasy is uncommon.</li>
  <li>Failure mode: LONG-BRANCH ATTRACTION — long branches with fast-evolving sites cluster spuriously.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Simple, intuitive criterion.</strong> Two trees: 5 changes vs 8 changes → parsimony picks 5.</li>
  <li><strong>Works for slow-evolving morphology.</strong> Fine for traditional cladistic analysis.</li>
  <li><strong>Fails for fast-evolving genes.</strong> Maximum likelihood and Bayesian methods are more robust where rate variation is high.</li>
</ol>
<h4>Exam traps</h4>
<ul>
  <li>Parsimony is NOT necessarily true — it's a methodological choice, not biological reality.</li>
  <li>Long-branch attraction is the major systematic error — recognize it as the parsimony Achilles' heel.</li>
</ul>` }
  });
})();
