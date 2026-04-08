"""
SVG diagram constants for Chapter 13 nodes.
Each string is a complete inline SVG designed for the dark study-guide theme
(card bg #111118, text #e8e4d8).  Embed as visual['svg'] or in extraSvgs[].
"""

# ---------------------------------------------------------------------------
# Fig 13.4 — Coral spawning temporal isolation histogram
# M. annularis peaks early; M. franksi peaks late — two species, same reef
# ---------------------------------------------------------------------------
SVG_FIG_13_4 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 280" width="480" height="280">
  <rect width="480" height="280" fill="#111118" rx="8"/>
  <text x="240" y="22" text-anchor="middle" font-family="Georgia,serif" font-size="13" font-weight="bold" fill="#e8e4d8">Fig 13.4 — Temporal Isolation in Coral Spawning</text>
  <!-- axes -->
  <line x1="60" y1="220" x2="440" y2="220" stroke="#555" stroke-width="1.5"/>
  <line x1="60" y1="40" x2="60" y2="220" stroke="#555" stroke-width="1.5"/>
  <!-- y-axis label -->
  <text x="18" y="140" text-anchor="middle" font-family="Georgia,serif" font-size="11" fill="#aaa" transform="rotate(-90,18,140)">Proportion spawning</text>
  <!-- x-axis label -->
  <text x="250" y="256" text-anchor="middle" font-family="Georgia,serif" font-size="11" fill="#aaa">Hours past sunset</text>
  <!-- x tick labels -->
  <text x="90" y="237" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#aaa">1:20</text>
  <text x="155" y="237" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#aaa">2:00</text>
  <text x="220" y="237" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#aaa">2:40</text>
  <text x="285" y="237" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#aaa">3:20</text>
  <text x="350" y="237" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#aaa">4:00</text>
  <text x="415" y="237" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#aaa">4:40</text>
  <!-- M. annularis bars (dark red) — early peak ~1:40-2:00 -->
  <rect x="80" y="160" width="28" height="60" fill="#8b1a1a" opacity="0.85"/>
  <rect x="112" y="100" width="28" height="120" fill="#8b1a1a" opacity="0.85"/>
  <rect x="144" y="70" width="28" height="150" fill="#8b1a1a" opacity="0.85"/>
  <rect x="176" y="110" width="28" height="110" fill="#8b1a1a" opacity="0.85"/>
  <rect x="208" y="170" width="28" height="50" fill="#8b1a1a" opacity="0.85"/>
  <rect x="240" y="205" width="28" height="15" fill="#8b1a1a" opacity="0.85"/>
  <!-- M. franksi bars (orange) — late peak ~3:30-4:00 -->
  <rect x="240" y="200" width="28" height="20" fill="#d4720c" opacity="0.85"/>
  <rect x="272" y="170" width="28" height="50" fill="#d4720c" opacity="0.85"/>
  <rect x="304" y="115" width="28" height="105" fill="#d4720c" opacity="0.85"/>
  <rect x="336" y="80" width="28" height="140" fill="#d4720c" opacity="0.85"/>
  <rect x="368" y="120" width="28" height="100" fill="#d4720c" opacity="0.85"/>
  <rect x="400" y="175" width="28" height="45" fill="#d4720c" opacity="0.85"/>
  <!-- legend -->
  <rect x="70" y="42" width="12" height="12" fill="#8b1a1a"/>
  <text x="87" y="53" font-family="Georgia,serif" font-size="11" fill="#e8e4d8" font-style="italic">M. annularis</text>
  <rect x="180" y="42" width="12" height="12" fill="#d4720c"/>
  <text x="197" y="53" font-family="Georgia,serif" font-size="11" fill="#e8e4d8" font-style="italic">M. franksi</text>
  <!-- annotation arrow -->
  <line x1="158" y1="62" x2="342" y2="62" stroke="#ffc857" stroke-width="1.5" marker-end="url(#arr)" marker-start="url(#arrl)"/>
  <defs>
    <marker id="arr" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z" fill="#ffc857"/>
    </marker>
    <marker id="arrl" markerWidth="6" markerHeight="6" refX="1" refY="3" orient="auto">
      <path d="M6,0 L0,3 L6,6 Z" fill="#ffc857"/>
    </marker>
  </defs>
  <text x="250" y="58" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#ffc857">~2 hr offset = temporal isolation</text>
</svg>"""


# ---------------------------------------------------------------------------
# Fig 13.7 — Reproductive Isolating Barriers Flowchart
# Full hierarchy: geographic → reproductive → pre/post-zygotic → 9 types
# ---------------------------------------------------------------------------
SVG_FIG_13_7 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 420" width="680" height="420">
  <rect width="680" height="420" fill="#111118" rx="8"/>
  <text x="340" y="24" text-anchor="middle" font-family="Georgia,serif" font-size="14" font-weight="bold" fill="#e8e4d8">Fig 13.7 — Reproductive Isolating Barriers</text>
  <!-- Root box -->
  <rect x="240" y="34" width="200" height="30" rx="6" fill="#2a2a38" stroke="#7c6cf7" stroke-width="1.5"/>
  <text x="340" y="54" text-anchor="middle" font-family="Georgia,serif" font-size="12" font-weight="bold" fill="#c4b5fd">ISOLATING BARRIERS</text>
  <!-- Two main branches -->
  <line x1="340" y1="64" x2="340" y2="78" stroke="#555" stroke-width="1.5"/>
  <line x1="150" y1="78" x2="530" y2="78" stroke="#555" stroke-width="1.5"/>
  <line x1="150" y1="78" x2="150" y2="92" stroke="#555" stroke-width="1.5"/>
  <line x1="530" y1="78" x2="530" y2="92" stroke="#555" stroke-width="1.5"/>
  <!-- Geographic box (left) -->
  <rect x="62" y="92" width="176" height="28" rx="5" fill="#1e2a1e" stroke="#00c9a7" stroke-width="1.5"/>
  <text x="150" y="110" text-anchor="middle" font-family="Georgia,serif" font-size="11" fill="#00c9a7">GEOGRAPHIC (Extrinsic)</text>
  <text x="150" y="136" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#7fb89a">Rivers · Mountains · Oceans</text>
  <!-- Reproductive box (right) -->
  <rect x="440" y="92" width="180" height="28" rx="5" fill="#2a1e2a" stroke="#ffc857" stroke-width="1.5"/>
  <text x="530" y="110" text-anchor="middle" font-family="Georgia,serif" font-size="11" fill="#ffc857">REPRODUCTIVE (Intrinsic)</text>
  <!-- Reproductive splits to Prezygotic and Postzygotic -->
  <line x1="530" y1="120" x2="530" y2="140" stroke="#555" stroke-width="1.5"/>
  <line x1="340" y1="140" x2="620" y2="140" stroke="#555" stroke-width="1.5"/>
  <line x1="340" y1="140" x2="340" y2="154" stroke="#555" stroke-width="1.5"/>
  <line x1="620" y1="140" x2="620" y2="154" stroke="#555" stroke-width="1.5"/>
  <!-- Prezygotic box -->
  <rect x="240" y="154" width="200" height="28" rx="5" fill="#1a1e2a" stroke="#4ea8de" stroke-width="1.5"/>
  <text x="340" y="172" text-anchor="middle" font-family="Georgia,serif" font-size="11" fill="#4ea8de">PREZYGOTIC</text>
  <!-- Postzygotic box -->
  <rect x="520" y="154" width="200" height="28" rx="5" fill="#2a1a1a" stroke="#e63946" stroke-width="1.5"/>
  <text x="620" y="172" text-anchor="middle" font-family="Georgia,serif" font-size="11" fill="#e63946">POSTZYGOTIC</text>
  <!-- Prezygotic splits to Pre-mating and Post-mating -->
  <line x1="340" y1="182" x2="340" y2="200" stroke="#555" stroke-width="1.5"/>
  <line x1="230" y1="200" x2="460" y2="200" stroke="#555" stroke-width="1.5"/>
  <line x1="230" y1="200" x2="230" y2="214" stroke="#555" stroke-width="1.5"/>
  <line x1="460" y1="200" x2="460" y2="214" stroke="#555" stroke-width="1.5"/>
  <!-- Pre-mating box -->
  <rect x="130" y="214" width="200" height="26" rx="4" fill="#181f2a" stroke="#4ea8de" stroke-width="1"/>
  <text x="230" y="231" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#93c5fd">PRE-MATING</text>
  <!-- Post-mating prezygotic box -->
  <rect x="360" y="214" width="200" height="26" rx="4" fill="#181f2a" stroke="#93c5fd" stroke-width="1"/>
  <text x="460" y="231" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#93c5fd">POST-MATING PREZYGOTIC</text>
  <!-- Pre-mating 5 types -->
  <line x1="230" y1="240" x2="230" y2="252" stroke="#555" stroke-width="1"/>
  <line x1="80" y1="252" x2="380" y2="252" stroke="#555" stroke-width="1"/>
  <line x1="80" y1="252" x2="80" y2="263" stroke="#555" stroke-width="1"/>
  <line x1="155" y1="252" x2="155" y2="263" stroke="#555" stroke-width="1"/>
  <line x1="230" y1="252" x2="230" y2="263" stroke="#555" stroke-width="1"/>
  <line x1="305" y1="252" x2="305" y2="263" stroke="#555" stroke-width="1"/>
  <line x1="380" y1="252" x2="380" y2="263" stroke="#555" stroke-width="1"/>
  <!-- Type boxes -->
  <rect x="40" y="263" width="80" height="44" rx="4" fill="#141a20" stroke="#4ea8de" stroke-width="1"/>
  <text x="80" y="279" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#93c5fd">1. BEHAVIORAL</text>
  <text x="80" y="292" text-anchor="middle" font-family="Georgia,serif" font-size="8" fill="#aaa">firefly flash</text>
  <text x="80" y="303" text-anchor="middle" font-family="Georgia,serif" font-size="8" fill="#aaa">patterns</text>
  <rect x="115" y="263" width="80" height="44" rx="4" fill="#141a20" stroke="#4ea8de" stroke-width="1"/>
  <text x="155" y="279" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#93c5fd">2. HABITAT</text>
  <text x="155" y="292" text-anchor="middle" font-family="Georgia,serif" font-size="8" fill="#aaa">pond vs stream</text>
  <text x="155" y="303" text-anchor="middle" font-family="Georgia,serif" font-size="8" fill="#aaa">frogs</text>
  <rect x="190" y="263" width="80" height="44" rx="4" fill="#141a20" stroke="#4ea8de" stroke-width="1"/>
  <text x="230" y="279" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#93c5fd">3. TEMPORAL</text>
  <text x="230" y="292" text-anchor="middle" font-family="Georgia,serif" font-size="8" fill="#aaa">coral dawn vs</text>
  <text x="230" y="303" text-anchor="middle" font-family="Georgia,serif" font-size="8" fill="#aaa">dusk spawning</text>
  <rect x="265" y="263" width="80" height="44" rx="4" fill="#141a20" stroke="#4ea8de" stroke-width="1"/>
  <text x="305" y="279" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#93c5fd">4. POLLINATOR</text>
  <text x="305" y="292" text-anchor="middle" font-family="Georgia,serif" font-size="8" fill="#aaa">bee vs hummingbird</text>
  <text x="305" y="303" text-anchor="middle" font-family="Georgia,serif" font-size="8" fill="#aaa">flowers</text>
  <rect x="340" y="263" width="80" height="44" rx="4" fill="#141a20" stroke="#4ea8de" stroke-width="1"/>
  <text x="380" y="279" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#93c5fd">5. MECHANICAL</text>
  <text x="380" y="292" text-anchor="middle" font-family="Georgia,serif" font-size="8" fill="#aaa">duck genitalia</text>
  <text x="380" y="303" text-anchor="middle" font-family="Georgia,serif" font-size="8" fill="#aaa">lock-and-key</text>
  <!-- Post-mating prezygotic type -->
  <line x1="460" y1="240" x2="460" y2="263" stroke="#555" stroke-width="1"/>
  <rect x="415" y="263" width="90" height="44" rx="4" fill="#141a20" stroke="#93c5fd" stroke-width="1"/>
  <text x="460" y="279" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#7dd3fc">6. GAMETIC</text>
  <text x="460" y="292" text-anchor="middle" font-family="Georgia,serif" font-size="8" fill="#aaa">sperm arrives,</text>
  <text x="460" y="303" text-anchor="middle" font-family="Georgia,serif" font-size="8" fill="#aaa">fails to fertilize</text>
  <!-- Postzygotic 3 types -->
  <line x1="620" y1="182" x2="620" y2="200" stroke="#555" stroke-width="1"/>
  <line x1="540" y1="200" x2="700" y2="200" stroke="#555" stroke-width="1"/>
  <line x1="540" y1="200" x2="540" y2="214" stroke="#555" stroke-width="1"/>
  <line x1="620" y1="200" x2="620" y2="214" stroke="#555" stroke-width="1"/>
  <line x1="700" y1="200" x2="700" y2="214" stroke="#555" stroke-width="1"/>
  <!-- Wait - let me move postzygotic to use x 540-700 range -->
  <rect x="500" y="214" width="80" height="44" rx="4" fill="#201414" stroke="#e63946" stroke-width="1"/>
  <text x="540" y="230" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#f87171">7. INVIABILITY</text>
  <text x="540" y="243" text-anchor="middle" font-family="Georgia,serif" font-size="8" fill="#aaa">hybrid embryo</text>
  <text x="540" y="254" text-anchor="middle" font-family="Georgia,serif" font-size="8" fill="#aaa">dies</text>
  <rect x="580" y="214" width="80" height="44" rx="4" fill="#201414" stroke="#e63946" stroke-width="1"/>
  <text x="620" y="230" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#f87171">8. STERILITY</text>
  <text x="620" y="243" text-anchor="middle" font-family="Georgia,serif" font-size="8" fill="#aaa">mule (horse×</text>
  <text x="620" y="254" text-anchor="middle" font-family="Georgia,serif" font-size="8" fill="#aaa">donkey)</text>
  <rect x="660" y="214" width="80" height="44" rx="4" fill="#201414" stroke="#e63946" stroke-width="1"/>
  <text x="700" y="230" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#f87171">9. BREAKDOWN</text>
  <text x="700" y="243" text-anchor="middle" font-family="Georgia,serif" font-size="8" fill="#aaa">F2 reduced</text>
  <text x="700" y="254" text-anchor="middle" font-family="Georgia,serif" font-size="8" fill="#aaa">fitness</text>
  <!-- Key callout at bottom -->
  <rect x="62" y="326" width="556" height="38" rx="5" fill="#1e1e28" stroke="#ffc857" stroke-width="1"/>
  <text x="340" y="342" text-anchor="middle" font-family="Georgia,serif" font-size="11" fill="#ffc857">Prezygotic barriers evolve FASTER than postzygotic (Coyne &amp; Orr, Drosophila)</text>
  <text x="340" y="358" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#aaa">BDM incompatibilities = molecular mechanism behind #7 and #8</text>
</svg>"""


# ---------------------------------------------------------------------------
# Fig 13.8 — Allopatric Speciation 4-Panel (beetles + river)
# A=single pop, B=barrier appears, C=divergence, D=RI developed
# ---------------------------------------------------------------------------
SVG_FIG_13_8 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 620 300" width="620" height="300">
  <rect width="620" height="300" fill="#111118" rx="8"/>
  <text x="310" y="22" text-anchor="middle" font-family="Georgia,serif" font-size="13" font-weight="bold" fill="#e8e4d8">Fig 13.8 — Allopatric Speciation</text>
  <!-- Panel labels -->
  <text x="20" y="50" font-family="Georgia,serif" font-size="13" font-weight="bold" fill="#4ea8de">A</text>
  <text x="175" y="50" font-family="Georgia,serif" font-size="13" font-weight="bold" fill="#4ea8de">B</text>
  <text x="330" y="50" font-family="Georgia,serif" font-size="13" font-weight="bold" fill="#4ea8de">C</text>
  <text x="485" y="50" font-family="Georgia,serif" font-size="13" font-weight="bold" fill="#4ea8de">D</text>
  <!-- Panel A — Single population -->
  <rect x="15" y="55" width="140" height="160" rx="6" fill="#1a2218" stroke="#3a5a30" stroke-width="1.5"/>
  <text x="85" y="74" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#7fb89a">Single population</text>
  <!-- beetles — orange dots -->
  <circle cx="45" cy="100" r="7" fill="#d4720c"/>
  <circle cx="70" cy="90" r="7" fill="#d4720c"/>
  <circle cx="95" cy="105" r="7" fill="#d4720c"/>
  <circle cx="55" cy="125" r="7" fill="#d4720c"/>
  <circle cx="80" cy="140" r="7" fill="#d4720c"/>
  <circle cx="110" cy="118" r="7" fill="#d4720c"/>
  <circle cx="125" cy="140" r="7" fill="#d4720c"/>
  <circle cx="40" cy="155" r="7" fill="#d4720c"/>
  <circle cx="100" cy="88" r="7" fill="#d4720c"/>
  <text x="85" y="228" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#aaa">Free gene flow</text>
  <!-- Panel B — River appears -->
  <rect x="170" y="55" width="140" height="160" rx="6" fill="#1a2218" stroke="#3a5a30" stroke-width="1.5"/>
  <text x="240" y="74" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#7fb89a">Barrier forms</text>
  <!-- River -->
  <rect x="228" y="55" width="25" height="160" fill="#1a4060" stroke="#2a6090" stroke-width="1" opacity="0.9"/>
  <text x="240" y="145" text-anchor="middle" font-family="Georgia,serif" font-size="8" fill="#7dd3fc" transform="rotate(-90,240,145)">RIVER</text>
  <!-- Left beetles -->
  <circle cx="185" cy="100" r="7" fill="#d4720c"/>
  <circle cx="200" cy="120" r="7" fill="#d4720c"/>
  <circle cx="190" cy="145" r="7" fill="#d4720c"/>
  <circle cx="215" cy="100" r="7" fill="#d4720c"/>
  <!-- Right beetles -->
  <circle cx="265" cy="95" r="7" fill="#d4720c"/>
  <circle cx="285" cy="120" r="7" fill="#d4720c"/>
  <circle cx="275" cy="148" r="7" fill="#d4720c"/>
  <circle cx="296" cy="100" r="7" fill="#d4720c"/>
  <text x="240" y="228" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#aaa">Gene flow blocked</text>
  <!-- Arrow A→B -->
  <text x="162" y="142" text-anchor="middle" font-family="Georgia,serif" font-size="16" fill="#555">→</text>
  <!-- Panel C — Divergence (different colors) -->
  <rect x="325" y="55" width="140" height="160" rx="6" fill="#1a2218" stroke="#3a5a30" stroke-width="1.5"/>
  <text x="395" y="74" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#7fb89a">Independent divergence</text>
  <!-- River -->
  <rect x="383" y="55" width="25" height="160" fill="#1a4060" stroke="#2a6090" stroke-width="1" opacity="0.9"/>
  <!-- Left beetles — blue, evolved differently -->
  <circle cx="340" cy="100" r="7" fill="#4ea8de"/>
  <circle cx="355" cy="120" r="7" fill="#4ea8de"/>
  <circle cx="345" cy="148" r="7" fill="#4ea8de"/>
  <circle cx="368" cy="100" r="7" fill="#4ea8de"/>
  <!-- Right beetles — red, evolved differently -->
  <circle cx="418" cy="95" r="7" fill="#e63946"/>
  <circle cx="438" cy="120" r="7" fill="#e63946"/>
  <circle cx="428" cy="148" r="7" fill="#e63946"/>
  <circle cx="450" cy="100" r="7" fill="#e63946"/>
  <text x="395" y="228" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#aaa">Drift + selection diverge</text>
  <!-- Arrow B→C -->
  <text x="317" y="142" text-anchor="middle" font-family="Georgia,serif" font-size="16" fill="#555">→</text>
  <!-- Panel D — Barrier gone, RI developed -->
  <rect x="480" y="55" width="130" height="160" rx="6" fill="#1a2218" stroke="#3a5a30" stroke-width="1.5"/>
  <text x="545" y="74" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#7fb89a">Barrier gone — no interbreeding</text>
  <!-- Mixed beetles, different colors, don't mate — X symbols between them -->
  <circle cx="500" cy="100" r="7" fill="#4ea8de"/>
  <circle cx="515" cy="128" r="7" fill="#4ea8de"/>
  <circle cx="500" cy="155" r="7" fill="#4ea8de"/>
  <circle cx="560" cy="100" r="7" fill="#e63946"/>
  <circle cx="575" cy="128" r="7" fill="#e63946"/>
  <circle cx="590" cy="100" r="7" fill="#e63946"/>
  <!-- X between the two groups -->
  <text x="535" y="128" text-anchor="middle" font-family="Georgia,serif" font-size="16" fill="#e63946" font-weight="bold">✗</text>
  <text x="545" y="228" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#ffc857">Reproductive isolation = 2 species</text>
  <!-- Arrow C→D -->
  <text x="472" y="142" text-anchor="middle" font-family="Georgia,serif" font-size="16" fill="#555">→</text>
  <!-- Bottom summary -->
  <rect x="15" y="252" width="590" height="32" rx="5" fill="#1e1e28" stroke="#4ea8de" stroke-width="1"/>
  <text x="310" y="265" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#4ea8de">Geographic separation → Genetic divergence → Reproductive isolation (even after barrier removed)</text>
  <text x="310" y="278" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#aaa">Most common speciation mode. Geographic isolation NECESSARY but NOT SUFFICIENT — RI must also develop.</text>
</svg>"""


# ---------------------------------------------------------------------------
# Fig 13.9 — Panama Shrimp (Isthmus of Panama, allopatric speciation)
# ---------------------------------------------------------------------------
SVG_FIG_13_9 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 280" width="520" height="280">
  <rect width="520" height="280" fill="#111118" rx="8"/>
  <text x="260" y="22" text-anchor="middle" font-family="Georgia,serif" font-size="13" font-weight="bold" fill="#e8e4d8">Fig 13.9 — Isthmus of Panama: Allopatric Speciation Test</text>
  <!-- Ocean backgrounds -->
  <rect x="15" y="35" width="185" height="175" rx="6" fill="#0d2136"/>
  <rect x="320" y="35" width="185" height="175" rx="6" fill="#0d2136"/>
  <!-- Isthmus bar -->
  <rect x="200" y="35" width="120" height="175" rx="4" fill="#6b4a1e"/>
  <text x="260" y="88" text-anchor="middle" font-family="Georgia,serif" font-size="11" font-weight="bold" fill="#e8c87a">ISTHMUS</text>
  <text x="260" y="103" text-anchor="middle" font-family="Georgia,serif" font-size="11" font-weight="bold" fill="#e8c87a">OF</text>
  <text x="260" y="118" text-anchor="middle" font-family="Georgia,serif" font-size="11" font-weight="bold" fill="#e8c87a">PANAMA</text>
  <text x="260" y="140" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#c8a85a">Formed ~3 mya</text>
  <!-- Ocean labels -->
  <text x="107" y="68" text-anchor="middle" font-family="Georgia,serif" font-size="13" font-weight="bold" fill="#4ea8de">PACIFIC</text>
  <text x="107" y="84" text-anchor="middle" font-family="Georgia,serif" font-size="13" font-weight="bold" fill="#4ea8de">OCEAN</text>
  <text x="413" y="68" text-anchor="middle" font-family="Georgia,serif" font-size="13" font-weight="bold" fill="#60b0f4">ATLANTIC</text>
  <text x="413" y="84" text-anchor="middle" font-family="Georgia,serif" font-size="13" font-weight="bold" fill="#60b0f4">OCEAN</text>
  <!-- Shrimp silhouettes (simplified) -->
  <ellipse cx="90" cy="145" rx="40" ry="14" fill="#4ea8de" opacity="0.7"/>
  <text x="90" y="150" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#111" font-weight="bold">shrimp A</text>
  <ellipse cx="413" cy="145" rx="40" ry="14" fill="#60b0f4" opacity="0.7"/>
  <text x="413" y="150" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#111" font-weight="bold">shrimp B</text>
  <!-- Sister species labels -->
  <text x="90" y="168" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#7dd3fc">Pacific species</text>
  <text x="413" y="168" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#7dd3fc">Atlantic species</text>
  <!-- Phylogeny at bottom showing sister relationship -->
  <text x="260" y="224" text-anchor="middle" font-family="Georgia,serif" font-size="11" font-weight="bold" fill="#aaa">Phylogeny (Knowlton 1993):</text>
  <!-- Simple cladogram lines -->
  <line x1="120" y1="255" x2="120" y2="240" stroke="#aaa" stroke-width="1.5"/>
  <line x1="160" y1="255" x2="160" y2="240" stroke="#aaa" stroke-width="1.5"/>
  <line x1="120" y1="240" x2="160" y2="240" stroke="#aaa" stroke-width="1.5"/>
  <line x1="140" y1="240" x2="140" y2="233" stroke="#aaa" stroke-width="1.5"/>
  <text x="100" y="268" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#4ea8de">Pacific sp.</text>
  <text x="166" y="268" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#60b0f4">Atlantic sp.</text>
  <text x="140" y="228" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#aaa">sister!</text>
  <!-- × for lab test -->
  <line x1="310" y1="248" x2="400" y2="248" stroke="#555" stroke-width="1"/>
  <text x="355" y="244" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#ffc857">Lab mating test: ✗</text>
  <text x="355" y="260" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#aaa">refuse to interbreed</text>
  <text x="355" y="272" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#aaa">→ confirmed RI</text>
</svg>"""


# ---------------------------------------------------------------------------
# Fig 13.10 — Rhagoletis fly host-race emergence timing
# Apple race emerges earlier; hawthorn race emerges later → temporal isolation
# ---------------------------------------------------------------------------
SVG_FIG_13_10 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 280" width="460" height="280">
  <rect width="460" height="280" fill="#111118" rx="8"/>
  <text x="230" y="22" text-anchor="middle" font-family="Georgia,serif" font-size="13" font-weight="bold" fill="#e8e4d8">Fig 13.10 — Rhagoletis Fly Emergence Timing</text>
  <text x="230" y="40" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#aaa">Sympatric host-race divergence via temporal isolation</text>
  <!-- Axes -->
  <line x1="60" y1="210" x2="430" y2="210" stroke="#555" stroke-width="1.5"/>
  <line x1="60" y1="60" x2="60" y2="210" stroke="#555" stroke-width="1.5"/>
  <!-- Axis labels -->
  <text x="245" y="248" text-anchor="middle" font-family="Georgia,serif" font-size="11" fill="#aaa">Month</text>
  <text x="18" y="135" text-anchor="middle" font-family="Georgia,serif" font-size="11" fill="#aaa" transform="rotate(-90,18,135)">Adult emergence</text>
  <!-- X tick labels -->
  <text x="95" y="226" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#aaa">Jul</text>
  <text x="150" y="226" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#aaa">Aug</text>
  <text x="205" y="226" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#aaa">Sep</text>
  <text x="260" y="226" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#aaa">Oct</text>
  <text x="315" y="226" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#aaa">Nov</text>
  <!-- Apple-race bell curve (green, earlier) -->
  <path d="M 65,205 Q 90,200 110,180 Q 130,145 155,95 Q 175,68 200,80 Q 225,95 240,130 Q 255,165 270,190 Q 290,205 320,208 L 430,210" stroke="#22c55e" stroke-width="2.5" fill="none"/>
  <!-- Hawthorn-race bell curve (red/orange, later) -->
  <path d="M 65,208 Q 120,207 150,205 Q 180,200 210,180 Q 240,145 265,95 Q 285,68 310,78 Q 335,92 350,130 Q 365,168 380,192 Q 400,206 430,210" stroke="#e63946" stroke-width="2.5" fill="none"/>
  <!-- Fill under apple curve -->
  <path d="M 65,205 Q 90,200 110,180 Q 130,145 155,95 Q 175,68 200,80 Q 225,95 240,130 Q 255,165 270,190 Q 290,205 320,208 L 430,210 L 65,210 Z" fill="#22c55e" opacity="0.15"/>
  <!-- Fill under hawthorn curve -->
  <path d="M 65,208 Q 120,207 150,205 Q 180,200 210,180 Q 240,145 265,95 Q 285,68 310,78 Q 335,92 350,130 Q 365,168 380,192 Q 400,206 430,210 L 65,210 Z" fill="#e63946" opacity="0.15"/>
  <!-- Offset arrow -->
  <line x1="195" y1="80" x2="305" y2="78" stroke="#ffc857" stroke-width="1.5" marker-end="url(#rharr)" marker-start="url(#rharrl)"/>
  <defs>
    <marker id="rharr" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#ffc857"/></marker>
    <marker id="rharrl" markerWidth="6" markerHeight="6" refX="1" refY="3" orient="auto"><path d="M6,0 L0,3 L6,6 Z" fill="#ffc857"/></marker>
  </defs>
  <text x="250" y="72" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#ffc857">~3–4 week offset</text>
  <!-- Legend -->
  <line x1="75" y1="52" x2="100" y2="52" stroke="#22c55e" stroke-width="2.5"/>
  <text x="110" y="57" font-family="Georgia,serif" font-size="10" fill="#22c55e">Apple-race</text>
  <line x1="185" y1="52" x2="210" y2="52" stroke="#e63946" stroke-width="2.5"/>
  <text x="220" y="57" font-family="Georgia,serif" font-size="10" fill="#e63946">Hawthorn-race</text>
  <!-- Caption -->
  <rect x="60" y="258" width="370" height="16" rx="4" fill="#1e1e28"/>
  <text x="245" y="269" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#aaa">Host-plant fruiting time drives temporal isolation → reproductive barrier within same field</text>
</svg>"""


# ---------------------------------------------------------------------------
# Fig 13.11 — Laupala cricket Hawaii colonization + QTL LOD score graphs
# ---------------------------------------------------------------------------
SVG_FIG_13_11 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 620 360" width="620" height="360">
  <rect width="620" height="360" fill="#111118" rx="8"/>
  <text x="310" y="22" text-anchor="middle" font-family="Georgia,serif" font-size="13" font-weight="bold" fill="#e8e4d8">Fig 13.11 — Laupala Crickets: Sexual Selection Speciation</text>
  <!-- Left panel: Hawaii island map schematic -->
  <text x="130" y="46" text-anchor="middle" font-family="Georgia,serif" font-size="11" fill="#aaa">Hawaii island chain colonization</text>
  <!-- Islands (simplified ovals, west to east = Kauai to Big Island) -->
  <!-- Kauai (oldest, orange = Oahu origin) -->
  <ellipse cx="40" cy="170" rx="26" ry="20" fill="#d97706" opacity="0.85"/>
  <text x="40" y="174" text-anchor="middle" font-family="Georgia,serif" font-size="8" fill="#111">Kauai</text>
  <!-- Oahu -->
  <ellipse cx="100" cy="155" rx="24" ry="18" fill="#d97706" opacity="0.85"/>
  <text x="100" y="159" text-anchor="middle" font-family="Georgia,serif" font-size="8" fill="#111">Oahu</text>
  <!-- Maui -->
  <ellipse cx="160" cy="165" rx="22" ry="17" fill="#7c3aed" opacity="0.85"/>
  <text x="160" y="169" text-anchor="middle" font-family="Georgia,serif" font-size="8" fill="#e8e4d8">Maui</text>
  <!-- Big Island (youngest, red) -->
  <ellipse cx="230" cy="200" rx="36" ry="28" fill="#dc2626" opacity="0.85"/>
  <text x="230" y="204" text-anchor="middle" font-family="Georgia,serif" font-size="8" fill="#e8e4d8">Big Island</text>
  <!-- Colonization arrows -->
  <path d="M 127,155 Q 140,148 142,156" stroke="#d97706" stroke-width="2" fill="none" marker-end="url(#lau_arr_o)"/>
  <path d="M 185,166 Q 200,168 198,178" stroke="#d97706" stroke-width="2" fill="none" marker-end="url(#lau_arr_o)"/>
  <path d="M 108,165 Q 125,190 135,188" stroke="#7c3aed" stroke-width="2" fill="none" marker-end="url(#lau_arr_p)"/>
  <path d="M 180,178 Q 200,198 198,196" stroke="#7c3aed" stroke-width="2" fill="none" marker-end="url(#lau_arr_p)"/>
  <defs>
    <marker id="lau_arr_o" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#d97706"/></marker>
    <marker id="lau_arr_p" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#7c3aed"/></marker>
  </defs>
  <!-- Key -->
  <rect x="15" y="248" width="246" height="80" rx="5" fill="#1a1a22"/>
  <circle cx="30" cy="264" r="7" fill="#d97706"/>
  <text x="42" y="269" font-family="Georgia,serif" font-size="10" fill="#fbbf24">Two Oahu lineages colonized</text>
  <text x="42" y="283" font-family="Georgia,serif" font-size="10" fill="#fbbf24">independently (orange)</text>
  <circle cx="30" cy="298" r="7" fill="#7c3aed"/>
  <text x="42" y="303" font-family="Georgia,serif" font-size="10" fill="#a78bfa">Purple = Maui-origin</text>
  <text x="42" y="317" font-family="Georgia,serif" font-size="10" fill="#f87171">Big Island: 6 spp / 430 kyr</text>
  <!-- Right panel: QTL LOD score graphs -->
  <text x="430" y="46" text-anchor="middle" font-family="Georgia,serif" font-size="11" fill="#aaa">QTL mapping (Shaw &amp; Lesnick 2009)</text>
  <!-- Female preference LOD graph -->
  <rect x="290" y="58" width="316" height="120" rx="5" fill="#151520"/>
  <text x="298" y="74" font-family="Georgia,serif" font-size="10" fill="#e8e4d8">Female preference</text>
  <text x="298" y="86" font-family="Georgia,serif" font-size="9" fill="#aaa">LOD</text>
  <line x1="310" y1="90" x2="310" y2="165" stroke="#555" stroke-width="1"/>
  <line x1="310" y1="165" x2="595" y2="165" stroke="#555" stroke-width="1"/>
  <!-- Significance dashed line at LOD=3.5 -->
  <line x1="310" y1="118" x2="595" y2="118" stroke="#555" stroke-width="1" stroke-dasharray="4,3"/>
  <text x="298" y="121" font-family="Georgia,serif" font-size="8" fill="#aaa">3.5</text>
  <text x="298" y="135" font-family="Georgia,serif" font-size="8" fill="#aaa">2</text>
  <text x="298" y="153" font-family="Georgia,serif" font-size="8" fill="#aaa">0</text>
  <!-- LOD score line (female pref) — flat with one spike near Lp1 end and big spike at Lp7 -->
  <polyline points="315,162 335,160 355,158 365,162 380,160 395,157 405,161 420,158 435,155 450,162 465,158 475,162 490,155 510,115 525,162 540,160 555,158 575,110 590,162" stroke="#4ea8de" stroke-width="1.5" fill="none"/>
  <!-- Male song LOD graph -->
  <rect x="290" y="190" width="316" height="130" rx="5" fill="#151520"/>
  <text x="298" y="206" font-family="Georgia,serif" font-size="10" fill="#e8e4d8">Male song</text>
  <text x="298" y="218" font-family="Georgia,serif" font-size="9" fill="#aaa">LOD</text>
  <line x1="310" y1="222" x2="310" y2="302" stroke="#555" stroke-width="1"/>
  <line x1="310" y1="302" x2="595" y2="302" stroke="#555" stroke-width="1"/>
  <!-- Significance dashed -->
  <line x1="310" y1="262" x2="595" y2="262" stroke="#555" stroke-width="1" stroke-dasharray="4,3"/>
  <text x="292" y="264" font-family="Georgia,serif" font-size="8" fill="#aaa">5</text>
  <text x="292" y="284" font-family="Georgia,serif" font-size="8" fill="#aaa">2</text>
  <!-- LOD line (male song) — big spikes at Lp3 and Lp5 -->
  <polyline points="315,300 335,298 355,290 370,298 390,278 405,295 425,240 445,295 465,250 490,230 510,295 525,298 540,295 560,292 575,295 590,298" stroke="#7c6cf7" stroke-width="1.5" fill="none"/>
  <!-- Chromosome labels -->
  <text x="320" y="315" font-family="Georgia,serif" font-size="8" fill="#aaa">Lp1</text>
  <text x="350" y="315" font-family="Georgia,serif" font-size="8" fill="#aaa">Lp2</text>
  <text x="390" y="315" font-family="Georgia,serif" font-size="8" fill="#aaa">Lp3</text>
  <text x="425" y="315" font-family="Georgia,serif" font-size="8" fill="#aaa">Lp4</text>
  <text x="460" y="315" font-family="Georgia,serif" font-size="8" fill="#aaa">Lp5</text>
  <text x="505" y="315" font-family="Georgia,serif" font-size="8" fill="#aaa">Lp6</text>
  <text x="558" y="315" font-family="Georgia,serif" font-size="8" fill="#aaa">Lp7</text>
  <!-- Key insight -->
  <rect x="290" y="328" width="316" height="26" rx="4" fill="#1e1e28" stroke="#ffc857" stroke-width="1"/>
  <text x="448" y="340" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#ffc857">Same locus → male song AND female preference</text>
  <text x="448" y="350" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#aaa">Co-localized genetics may explain rapid speciation rate</text>
</svg>"""


# ---------------------------------------------------------------------------
# Fig 13.13 — Polar bear / brown bear population history (hourglass)
# ---------------------------------------------------------------------------
SVG_FIG_13_13 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 480" width="420" height="480">
  <rect width="420" height="480" fill="#111118" rx="8"/>
  <text x="210" y="24" text-anchor="middle" font-family="Georgia,serif" font-size="13" font-weight="bold" fill="#e8e4d8">Fig 13.13 — Polar vs Brown Bear Population History</text>
  <text x="210" y="42" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#aaa">Effective population size (Ne) through time — Liu et al. 2014</text>
  <!-- Y axis (time) -->
  <line x1="60" y1="70" x2="60" y2="440" stroke="#555" stroke-width="1.5"/>
  <text x="30" y="258" text-anchor="middle" font-family="Georgia,serif" font-size="11" fill="#aaa" transform="rotate(-90,30,258)">Time (thousands of years ago)</text>
  <!-- Y tick marks and labels -->
  <line x1="55" y1="440" x2="65" y2="440" stroke="#555"/><text x="52" y="444" text-anchor="end" font-family="Georgia,serif" font-size="9" fill="#aaa">0</text>
  <line x1="55" y1="380" x2="65" y2="380" stroke="#555"/><text x="52" y="384" text-anchor="end" font-family="Georgia,serif" font-size="9" fill="#aaa">100</text>
  <line x1="55" y1="320" x2="65" y2="320" stroke="#555"/><text x="52" y="324" text-anchor="end" font-family="Georgia,serif" font-size="9" fill="#aaa">200</text>
  <line x1="55" y1="260" x2="65" y2="260" stroke="#555"/><text x="52" y="264" text-anchor="end" font-family="Georgia,serif" font-size="9" fill="#aaa">300</text>
  <line x1="55" y1="200" x2="65" y2="200" stroke="#555"/><text x="52" y="204" text-anchor="end" font-family="Georgia,serif" font-size="9" fill="#aaa">400</text>
  <line x1="55" y1="140" x2="65" y2="140" stroke="#555"/><text x="52" y="144" text-anchor="end" font-family="Georgia,serif" font-size="9" fill="#aaa">500</text>
  <line x1="55" y1="80" x2="65" y2="80" stroke="#555"/><text x="52" y="84" text-anchor="end" font-family="Georgia,serif" font-size="9" fill="#aaa">600</text>
  <!-- Polar bear column (left, light blue) -->
  <!-- Shape: wide at top (123k), narrow bottleneck (~20k), widens again (~5k bottleneck again), base 68k -->
  <text x="145" y="62" text-anchor="middle" font-family="Georgia,serif" font-size="12" font-weight="bold" fill="#7dd3fc">POLAR BEAR</text>
  <!-- Using path to draw population shape — width proportional to Ne -->
  <!-- Top (600 kya): divergence point, very narrow, y=80 -->
  <!-- 123k yr ago: largest polar pop, y=220 (420-200) -->
  <!-- 20k yr ago: bottleneck, y=388 -->
  <!-- 5k yr ago: bottleneck, y=418 -->
  <!-- present (68k): base, y=440 -->
  <!-- Left side of polar column -->
  <path d="M 145,80 L 100,220 L 108,388 L 105,418 L 90,440 L 145,440 Z" fill="#7dd3fc" opacity="0.35"/>
  <!-- Right side mirror -->
  <path d="M 145,80 L 190,220 L 182,388 L 185,418 L 200,440 L 145,440 Z" fill="#7dd3fc" opacity="0.35"/>
  <!-- Outline -->
  <path d="M 100,220 L 108,388 L 105,418 L 90,440 L 200,440 L 185,418 L 182,388 L 190,220" stroke="#7dd3fc" stroke-width="1.5" fill="none"/>
  <line x1="100" y1="220" x2="190" y2="220" stroke="#7dd3fc" stroke-width="1"/>
  <line x1="108" y1="388" x2="182" y2="388" stroke="#7dd3fc" stroke-width="1"/>
  <!-- Labels for key Ne values -->
  <text x="205" y="224" font-family="Georgia,serif" font-size="10" fill="#7dd3fc">123,000</text>
  <text x="185" y="392" font-family="Georgia,serif" font-size="10" fill="#7dd3fc">20,000</text>
  <text x="185" y="422" font-family="Georgia,serif" font-size="10" fill="#7dd3fc">5,000</text>
  <text x="75" y="454" font-family="Georgia,serif" font-size="9" fill="#7dd3fc">68,000</text>
  <!-- Divergence point arrow -->
  <line x1="145" y1="80" x2="145" y2="70" stroke="#ffc857" stroke-width="1.5"/>
  <text x="145" y="68" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#ffc857">~479 kya divergence</text>
  <!-- Brown bear column (right) -->
  <text x="310" y="62" text-anchor="middle" font-family="Georgia,serif" font-size="12" font-weight="bold" fill="#b45309">BROWN BEAR</text>
  <!-- Brown bear: very wide, stable large pop throughout, base 463k -->
  <path d="M 280,150 L 350,200 L 360,440 L 260,440 L 270,200 Z" fill="#b45309" opacity="0.35"/>
  <path d="M 270,200 L 260,440 L 360,440 L 350,200" stroke="#b45309" stroke-width="1.5" fill="none"/>
  <text x="365" y="444" font-family="Georgia,serif" font-size="10" fill="#b45309">463,000</text>
  <!-- Gene flow arrows between them (after divergence) -->
  <line x1="200" y1="340" x2="260" y2="340" stroke="#ffc857" stroke-width="1.5" marker-end="url(#gf_arr)"/>
  <defs><marker id="gf_arr" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#ffc857"/></marker></defs>
  <text x="230" y="332" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#ffc857">gene flow</text>
  <text x="230" y="354" text-anchor="middle" font-family="Georgia,serif" font-size="8" fill="#ffc857">polar→brown</text>
  <!-- Caption -->
  <rect x="60" y="460" width="300" height="16" rx="4" fill="#1e1e28"/>
  <text x="210" y="471" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#aaa">Speciation ~479–343 kya; gene flow continued one-way after split</text>
</svg>"""


# ---------------------------------------------------------------------------
# Fig 13.14 — Coyne & Orr Drosophila: RI vs genetic distance scatter plot
# ---------------------------------------------------------------------------
SVG_FIG_13_14 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 320" width="500" height="320">
  <rect width="500" height="320" fill="#111118" rx="8"/>
  <text x="250" y="22" text-anchor="middle" font-family="Georgia,serif" font-size="13" font-weight="bold" fill="#e8e4d8">Fig 13.14 — Reproductive Isolation vs Genetic Distance</text>
  <text x="250" y="38" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#aaa">Coyne &amp; Orr 2004 — Drosophila species pairs</text>
  <!-- Axes -->
  <line x1="70" y1="260" x2="470" y2="260" stroke="#555" stroke-width="1.5"/>
  <line x1="70" y1="52" x2="70" y2="260" stroke="#555" stroke-width="1.5"/>
  <!-- X axis labels -->
  <text x="270" y="288" text-anchor="middle" font-family="Georgia,serif" font-size="11" fill="#aaa">Genetic distance (D)</text>
  <text x="70" y="276" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#aaa">0</text>
  <text x="170" y="276" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#aaa">0.5</text>
  <text x="270" y="276" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#aaa">1.0</text>
  <text x="370" y="276" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#aaa">1.5</text>
  <text x="470" y="276" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#aaa">2.0</text>
  <!-- Y axis labels -->
  <text x="18" y="160" text-anchor="middle" font-family="Georgia,serif" font-size="11" fill="#aaa" transform="rotate(-90,18,160)">Reproductive isolation</text>
  <text x="60" y="264" text-anchor="end" font-family="Georgia,serif" font-size="9" fill="#aaa">0</text>
  <text x="60" y="212" text-anchor="end" font-family="Georgia,serif" font-size="9" fill="#aaa">0.2</text>
  <text x="60" y="160" text-anchor="end" font-family="Georgia,serif" font-size="9" fill="#aaa">0.4</text>
  <text x="60" y="108" text-anchor="end" font-family="Georgia,serif" font-size="9" fill="#aaa">0.6</text>
  <text x="60" y="64" text-anchor="end" font-family="Georgia,serif" font-size="9" fill="#aaa">0.8</text>
  <!-- Labels at extremes -->
  <text x="70" y="300" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#aaa">Closely related</text>
  <text x="470" y="300" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#aaa">Distantly related</text>
  <text x="485" y="60" text-anchor="end" font-family="Georgia,serif" font-size="9" fill="#aaa">Complete</text>
  <text x="485" y="71" text-anchor="end" font-family="Georgia,serif" font-size="9" fill="#aaa">isolation</text>
  <text x="485" y="262" text-anchor="end" font-family="Georgia,serif" font-size="9" fill="#aaa">No isolation</text>
  <!-- Dashed line at RI=1 -->
  <line x1="70" y1="56" x2="470" y2="56" stroke="#555" stroke-width="1" stroke-dasharray="5,4"/>
  <!-- Data points — dark red triangles. Scatter: low D = variable RI, high D = near 1 -->
  <!-- Low D zone (0-0.5): variable 0.2-1.0 -->
  <polygon points="75,220 79,228 71,228" fill="#7b1a1a"/>
  <polygon points="85,195 89,203 81,203" fill="#7b1a1a"/>
  <polygon points="95,170 99,178 91,178" fill="#7b1a1a"/>
  <polygon points="105,148 109,156 101,156" fill="#7b1a1a"/>
  <polygon points="115,112 119,120 111,120" fill="#7b1a1a"/>
  <polygon points="125,92 129,100 121,100" fill="#7b1a1a"/>
  <polygon points="130,240 134,248 126,248" fill="#7b1a1a"/>
  <polygon points="140,180 144,188 136,188" fill="#7b1a1a"/>
  <polygon points="150,130 154,138 146,138" fill="#7b1a1a"/>
  <polygon points="155,70 159,78 151,78" fill="#7b1a1a"/>
  <polygon points="160,210 164,218 156,218" fill="#7b1a1a"/>
  <polygon points="170,160 174,168 166,168" fill="#7b1a1a"/>
  <!-- Mid D zone (0.5-1.0): mostly high RI -->
  <polygon points="185,80 189,88 181,88" fill="#7b1a1a"/>
  <polygon points="200,62 204,70 196,70" fill="#7b1a1a"/>
  <polygon points="210,58 214,66 206,66" fill="#7b1a1a"/>
  <polygon points="220,58 224,66 216,66" fill="#7b1a1a"/>
  <polygon points="230,96 234,104 226,104" fill="#7b1a1a"/>
  <polygon points="245,58 249,66 241,66" fill="#7b1a1a"/>
  <polygon points="255,62 259,70 251,70" fill="#7b1a1a"/>
  <polygon points="260,58 264,66 256,66" fill="#7b1a1a"/>
  <polygon points="270,132 274,140 266,140" fill="#7b1a1a"/>
  <!-- High D zone (1.0-2.0): nearly all complete isolation -->
  <polygon points="290,58 294,66 286,66" fill="#7b1a1a"/>
  <polygon points="310,58 314,66 306,66" fill="#7b1a1a"/>
  <polygon points="330,58 334,66 326,66" fill="#7b1a1a"/>
  <polygon points="345,60 349,68 341,68" fill="#7b1a1a"/>
  <polygon points="360,58 364,66 356,66" fill="#7b1a1a"/>
  <polygon points="380,58 384,66 376,66" fill="#7b1a1a"/>
  <polygon points="400,58 404,66 396,66" fill="#7b1a1a"/>
  <polygon points="420,62 424,70 416,70" fill="#7b1a1a"/>
  <polygon points="440,58 444,66 436,66" fill="#7b1a1a"/>
  <polygon points="450,58 454,66 446,66" fill="#7b1a1a"/>
  <polygon points="460,64 464,72 456,72" fill="#7b1a1a"/>
  <!-- Trend line -->
  <path d="M 70,230 Q 170,180 270,70 L 470,58" stroke="#ffc857" stroke-width="1.5" fill="none" opacity="0.6" stroke-dasharray="6,3"/>
  <!-- Caption box -->
  <rect x="70" y="295" width="360" height="18" rx="4" fill="#1e1e28"/>
  <text x="250" y="307" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#ffc857">Prezygotic isolation increases faster than postzygotic as D increases</text>
</svg>"""


# ---------------------------------------------------------------------------
# Fig 13.15 — Allopolyploidy: step-by-step chromosome diagram
# ---------------------------------------------------------------------------
SVG_FIG_13_15 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 560" width="500" height="560">
  <rect width="500" height="560" fill="#111118" rx="8"/>
  <text x="250" y="24" text-anchor="middle" font-family="Georgia,serif" font-size="13" font-weight="bold" fill="#e8e4d8">Fig 13.15 — Allopolyploidy: Instant Speciation</text>
  <!-- Helper: chromosome pair symbol = two parallel bars -->
  <!-- Species A (2n=6): 3 pairs of blue chromosomes -->
  <rect x="80" y="40" width="130" height="90" rx="8" fill="#1a1e2a" stroke="#4ea8de" stroke-width="1.5"/>
  <text x="145" y="56" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#4ea8de">Species A (2n=6)</text>
  <text x="145" y="68" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#aaa">3 chromosome pairs</text>
  <!-- 3 blue chr pairs -->
  <rect x="92" y="74" width="6" height="30" rx="2" fill="#4ea8de"/>
  <rect x="100" y="74" width="6" height="30" rx="2" fill="#4ea8de"/>
  <rect x="115" y="74" width="6" height="30" rx="2" fill="#4ea8de"/>
  <rect x="123" y="74" width="6" height="30" rx="2" fill="#4ea8de"/>
  <rect x="138" y="74" width="6" height="30" rx="2" fill="#4ea8de"/>
  <rect x="146" y="74" width="6" height="30" rx="2" fill="#4ea8de"/>
  <text x="145" y="115" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#aaa">diploid parental</text>
  <!-- Species B (2n=4): 2 pairs of red chromosomes -->
  <rect x="290" y="40" width="130" height="90" rx="8" fill="#2a1a1a" stroke="#e63946" stroke-width="1.5"/>
  <text x="355" y="56" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#e63946">Species B (2n=4)</text>
  <text x="355" y="68" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#aaa">2 chromosome pairs</text>
  <!-- 2 red chr pairs -->
  <rect x="320" y="74" width="6" height="30" rx="2" fill="#e63946"/>
  <rect x="328" y="74" width="6" height="30" rx="2" fill="#e63946"/>
  <rect x="348" y="74" width="6" height="30" rx="2" fill="#e63946"/>
  <rect x="356" y="74" width="6" height="30" rx="2" fill="#e63946"/>
  <text x="355" y="115" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#aaa">diploid parental</text>
  <!-- Arrows down to gametes -->
  <line x1="145" y1="130" x2="145" y2="155" stroke="#555" stroke-width="1.5" marker-end="url(#ap15)"/>
  <line x1="355" y1="130" x2="355" y2="155" stroke="#555" stroke-width="1.5" marker-end="url(#ap15)"/>
  <defs><marker id="ap15" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#555"/></marker></defs>
  <!-- Gametes -->
  <rect x="105" y="155" width="80" height="58" rx="6" fill="#1a1e2a" stroke="#4ea8de" stroke-width="1"/>
  <text x="145" y="170" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#4ea8de">gamete (n=3)</text>
  <rect x="110" y="178" width="6" height="24" rx="2" fill="#4ea8de"/>
  <rect x="125" y="178" width="6" height="24" rx="2" fill="#4ea8de"/>
  <rect x="140" y="178" width="6" height="24" rx="2" fill="#4ea8de"/>
  <rect x="315" y="155" width="80" height="58" rx="6" fill="#2a1a1a" stroke="#e63946" stroke-width="1"/>
  <text x="355" y="170" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#e63946">gamete (n=2)</text>
  <rect x="335" y="178" width="6" height="24" rx="2" fill="#e63946"/>
  <rect x="350" y="178" width="6" height="24" rx="2" fill="#e63946"/>
  <!-- Arrow to hybrid -->
  <line x1="185" y1="184" x2="235" y2="214" stroke="#555" stroke-width="1.5" marker-end="url(#ap15)"/>
  <line x1="315" y1="184" x2="265" y2="214" stroke="#555" stroke-width="1.5" marker-end="url(#ap15)"/>
  <!-- Sterile Hybrid -->
  <rect x="160" y="218" width="180" height="78" rx="8" fill="#201a1a" stroke="#ffc857" stroke-width="2"/>
  <text x="250" y="234" text-anchor="middle" font-family="Georgia,serif" font-size="11" font-weight="bold" fill="#ffc857">Sterile Hybrid (2n=5)</text>
  <text x="250" y="248" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#aaa">chromosomes cannot pair in meiosis</text>
  <!-- 3 blue + 2 red, unpaired -->
  <rect x="175" y="254" width="5" height="26" rx="2" fill="#4ea8de"/>
  <rect x="185" y="254" width="5" height="26" rx="2" fill="#4ea8de"/>
  <rect x="195" y="254" width="5" height="26" rx="2" fill="#4ea8de"/>
  <rect x="210" y="254" width="5" height="26" rx="2" fill="#e63946"/>
  <rect x="220" y="254" width="5" height="26" rx="2" fill="#e63946"/>
  <text x="250" y="285" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#e63946" font-weight="bold">✗ STERILE</text>
  <text x="310" y="268" font-family="Georgia,serif" font-size="8" fill="#aaa">5 unpaired</text>
  <text x="310" y="280" font-family="Georgia,serif" font-size="8" fill="#aaa">chromosomes</text>
  <!-- Arrow down — genome doubling -->
  <line x1="250" y1="296" x2="250" y2="326" stroke="#00c9a7" stroke-width="2" marker-end="url(#ap15g)"/>
  <defs><marker id="ap15g" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#00c9a7"/></marker></defs>
  <rect x="170" y="310" width="160" height="18" rx="4" fill="#0d2620"/>
  <text x="250" y="322" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#00c9a7">Genome doubling event</text>
  <!-- Allotetraploid -->
  <rect x="150" y="332" width="200" height="90" rx="8" fill="#0d2620" stroke="#00c9a7" stroke-width="2"/>
  <text x="250" y="350" text-anchor="middle" font-family="Georgia,serif" font-size="11" font-weight="bold" fill="#00c9a7">Allotetraploid (2n=10)</text>
  <text x="250" y="364" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#aaa">all chromosomes have a homolog</text>
  <!-- 3 blue pairs + 2 red pairs -->
  <rect x="160" y="370" width="5" height="22" rx="2" fill="#4ea8de"/>
  <rect x="168" y="370" width="5" height="22" rx="2" fill="#4ea8de"/>
  <rect x="180" y="370" width="5" height="22" rx="2" fill="#4ea8de"/>
  <rect x="188" y="370" width="5" height="22" rx="2" fill="#4ea8de"/>
  <rect x="200" y="370" width="5" height="22" rx="2" fill="#4ea8de"/>
  <rect x="208" y="370" width="5" height="22" rx="2" fill="#4ea8de"/>
  <rect x="222" y="370" width="5" height="22" rx="2" fill="#e63946"/>
  <rect x="230" y="370" width="5" height="22" rx="2" fill="#e63946"/>
  <rect x="244" y="370" width="5" height="22" rx="2" fill="#e63946"/>
  <rect x="252" y="370" width="5" height="22" rx="2" fill="#e63946"/>
  <text x="250" y="408" text-anchor="middle" font-family="Georgia,serif" font-size="11" fill="#00c9a7" font-weight="bold">✓ FERTILE — NEW SPECIES</text>
  <!-- Arrow down to new species label -->
  <line x1="250" y1="422" x2="250" y2="450" stroke="#00c9a7" stroke-width="1.5" marker-end="url(#ap15g)"/>
  <rect x="110" y="450" width="280" height="40" rx="6" fill="#0d2620" stroke="#00c9a7" stroke-width="1.5"/>
  <text x="250" y="466" text-anchor="middle" font-family="Georgia,serif" font-size="11" fill="#00c9a7">Reproductively isolated from BOTH parents</text>
  <text x="250" y="481" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#aaa">Cross with A or B → odd chromosome number → sterile</text>
  <!-- Caption -->
  <rect x="60" y="500" width="380" height="28" rx="5" fill="#1e1e28" stroke="#ffc857" stroke-width="1"/>
  <text x="250" y="513" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#ffc857">Speciation in potentially ONE generation — most common in plants</text>
  <text x="250" y="525" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#aaa">Possibly half of all ~300,000 flowering plant species originated this way</text>
</svg>"""


# ---------------------------------------------------------------------------
# Fig 13.16 — Tragopogon allopolyploidy (salsify flowers)
# ---------------------------------------------------------------------------
SVG_FIG_13_16 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 240" width="540" height="240">
  <rect width="540" height="240" fill="#111118" rx="8"/>
  <text x="270" y="22" text-anchor="middle" font-family="Georgia,serif" font-size="13" font-weight="bold" fill="#e8e4d8">Fig 13.16 — Tragopogon Allopolyploidy</text>
  <text x="270" y="38" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#aaa">Two new species arose in North America within ~100 years (Soltis &amp; Soltis 2009)</text>
  <!-- T. pratensis (yellow flower, 2n=12) -->
  <circle cx="80" cy="120" r="38" fill="#854d0e" opacity="0.3" stroke="#854d0e" stroke-width="1.5"/>
  <!-- Flower petals simplified -->
  <circle cx="80" cy="120" r="22" fill="#ca8a04" opacity="0.8"/>
  <circle cx="80" cy="120" r="12" fill="#fef08a"/>
  <text x="80" y="167" text-anchor="middle" font-family="Georgia,serif" font-size="10" font-style="italic" fill="#fef08a">T. pratensis</text>
  <text x="80" y="180" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#aaa">2n = 12</text>
  <!-- T. dubius (green spiky, 2n=12) -->
  <circle cx="270" cy="90" r="38" fill="#166534" opacity="0.25" stroke="#166534" stroke-width="1.5"/>
  <circle cx="270" cy="90" r="22" fill="#16a34a" opacity="0.8"/>
  <circle cx="270" cy="90" r="12" fill="#86efac"/>
  <text x="270" y="52" text-anchor="middle" font-family="Georgia,serif" font-size="10" font-style="italic" fill="#86efac">T. dubius</text>
  <text x="270" y="65" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#aaa">2n = 12</text>
  <!-- T. porrifolius (pink/magenta, 2n=12) -->
  <circle cx="460" cy="120" r="38" fill="#831843" opacity="0.25" stroke="#831843" stroke-width="1.5"/>
  <circle cx="460" cy="120" r="22" fill="#be185d" opacity="0.8"/>
  <circle cx="460" cy="120" r="12" fill="#f9a8d4"/>
  <text x="460" y="167" text-anchor="middle" font-family="Georgia,serif" font-size="10" font-style="italic" fill="#f9a8d4">T. porrifolius</text>
  <text x="460" y="180" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#aaa">2n = 12</text>
  <!-- Arrows to hybrids -->
  <line x1="118" y1="115" x2="158" y2="145" stroke="#aaa" stroke-width="1.5" marker-end="url(#tg_arr)"/>
  <line x1="240" y1="108" x2="188" y2="145" stroke="#aaa" stroke-width="1.5" marker-end="url(#tg_arr)"/>
  <line x1="300" y1="108" x2="350" y2="145" stroke="#aaa" stroke-width="1.5" marker-end="url(#tg_arr)"/>
  <line x1="422" y1="116" x2="380" y2="145" stroke="#aaa" stroke-width="1.5" marker-end="url(#tg_arr)"/>
  <defs><marker id="tg_arr" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#aaa"/></marker></defs>
  <!-- T. miscellus (left hybrid, yellow-green, 2n=24) -->
  <circle cx="175" cy="175" r="32" fill="#3a5c0e" opacity="0.25" stroke="#65a30d" stroke-width="1.5"/>
  <circle cx="175" cy="175" r="18" fill="#84cc16" opacity="0.85"/>
  <circle cx="175" cy="175" r="10" fill="#d9f99d"/>
  <text x="175" y="213" text-anchor="middle" font-family="Georgia,serif" font-size="9" font-style="italic" fill="#d9f99d">T. miscellus</text>
  <text x="175" y="225" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#00c9a7">2n = 24 ✓ NEW</text>
  <!-- T. mirus (right hybrid, pink-green, 2n=24) -->
  <circle cx="365" cy="175" r="32" fill="#4a1942" opacity="0.25" stroke="#a21caf" stroke-width="1.5"/>
  <circle cx="365" cy="175" r="18" fill="#a855f7" opacity="0.85"/>
  <circle cx="365" cy="175" r="10" fill="#e9d5ff"/>
  <text x="365" y="213" text-anchor="middle" font-family="Georgia,serif" font-size="9" font-style="italic" fill="#e9d5ff">T. mirus</text>
  <text x="365" y="225" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#00c9a7">2n = 24 ✓ NEW</text>
  <!-- Genus label -->
  <text x="270" y="200" text-anchor="middle" font-family="Georgia,serif" font-size="10" font-weight="bold" font-style="italic" fill="#aaa">Genus: Tragopogon</text>
</svg>"""


# ---------------------------------------------------------------------------
# Fig 13.17 — Astraptes fulgerator: cryptic species via DNA barcoding
# ---------------------------------------------------------------------------
SVG_FIG_13_17 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 380" width="520" height="380">
  <rect width="520" height="380" fill="#111118" rx="8"/>
  <text x="260" y="22" text-anchor="middle" font-family="Georgia,serif" font-size="13" font-weight="bold" fill="#e8e4d8">Fig 13.17 — Astraptes: DNA Barcoding Reveals Cryptic Species</text>
  <text x="260" y="38" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#aaa">Hebert &amp; Janzen 2004 — Costa Rica skipper butterfly "one species" = 10 cryptic species</text>
  <!-- Phylogenetic tree (simplified, left side) -->
  <!-- Trunk -->
  <line x1="75" y1="360" x2="75" y2="58" stroke="#555" stroke-width="2"/>
  <!-- Branch clusters representing the 10 cryptic lineages -->
  <!-- Trigo cluster -->
  <line x1="75" y1="68" x2="140" y2="68" stroke="#555" stroke-width="1.5"/>
  <line x1="140" y1="58" x2="140" y2="78" stroke="#555" stroke-width="1.5"/>
  <text x="145" y="62" font-family="Georgia,serif" font-size="10" fill="#e8e4d8">Trigo</text>
  <text x="145" y="73" font-family="Georgia,serif" font-size="9" fill="#7fb89a">rain &amp; dry forest</text>
  <!-- Dashed separator -->
  <line x1="75" y1="88" x2="480" y2="88" stroke="#555" stroke-width="0.5" stroke-dasharray="3,3" opacity="0.5"/>
  <!-- Celt cluster -->
  <line x1="75" y1="100" x2="130" y2="100" stroke="#555" stroke-width="1.5"/>
  <line x1="130" y1="92" x2="130" y2="108" stroke="#555" stroke-width="1.5"/>
  <text x="135" y="95" font-family="Georgia,serif" font-size="10" fill="#e8e4d8">Celt</text>
  <text x="135" y="107" font-family="Georgia,serif" font-size="9" fill="#7fb89a">rain forest</text>
  <line x1="75" y1="120" x2="130" y2="120" stroke="#555" stroke-width="1.5"/>
  <text x="135" y="124" font-family="Georgia,serif" font-size="10" fill="#aaa">Numt</text>
  <line x1="75" y1="132" x2="480" y2="132" stroke="#555" stroke-width="0.5" stroke-dasharray="3,3" opacity="0.5"/>
  <!-- Sennov cluster -->
  <line x1="75" y1="152" x2="145" y2="152" stroke="#555" stroke-width="1.5"/>
  <text x="150" y="156" font-family="Georgia,serif" font-size="10" fill="#e8e4d8">Sennov</text>
  <text x="150" y="167" font-family="Georgia,serif" font-size="9" fill="#7fb89a">dry forest</text>
  <line x1="75" y1="176" x2="480" y2="176" stroke="#555" stroke-width="0.5" stroke-dasharray="3,3" opacity="0.5"/>
  <!-- Fabov cluster -->
  <line x1="75" y1="196" x2="138" y2="196" stroke="#555" stroke-width="1.5"/>
  <text x="143" y="200" font-family="Georgia,serif" font-size="10" fill="#e8e4d8">Fabov</text>
  <text x="143" y="211" font-family="Georgia,serif" font-size="9" fill="#7fb89a">dry forest</text>
  <line x1="75" y1="220" x2="480" y2="220" stroke="#555" stroke-width="0.5" stroke-dasharray="3,3" opacity="0.5"/>
  <!-- Myst/Hihamp/Ingcup cluster -->
  <line x1="75" y1="238" x2="120" y2="238" stroke="#555" stroke-width="1.5"/>
  <line x1="120" y1="232" x2="120" y2="268" stroke="#555" stroke-width="1.5"/>
  <line x1="120" y1="238" x2="148" y2="238" stroke="#555" stroke-width="1.5"/>
  <text x="153" y="242" font-family="Georgia,serif" font-size="10" fill="#aaa">Myst</text>
  <line x1="120" y1="252" x2="148" y2="252" stroke="#555" stroke-width="1.5"/>
  <text x="153" y="256" font-family="Georgia,serif" font-size="10" fill="#e8e4d8">Hihamp</text>
  <text x="153" y="267" font-family="Georgia,serif" font-size="9" fill="#7fb89a">cloud forest</text>
  <line x1="120" y1="268" x2="148" y2="268" stroke="#555" stroke-width="1.5"/>
  <text x="153" y="272" font-family="Georgia,serif" font-size="10" fill="#e8e4d8">Ingcup</text>
  <line x1="75" y1="284" x2="480" y2="284" stroke="#555" stroke-width="0.5" stroke-dasharray="3,3" opacity="0.5"/>
  <!-- Loncho/Lohamp/Byttner/Yessen cluster -->
  <line x1="75" y1="300" x2="115" y2="300" stroke="#555" stroke-width="1.5"/>
  <line x1="115" y1="292" x2="115" y2="340" stroke="#555" stroke-width="1.5"/>
  <line x1="115" y1="300" x2="143" y2="300" stroke="#555" stroke-width="1.5"/>
  <text x="148" y="304" font-family="Georgia,serif" font-size="10" fill="#e8e4d8">Loncho</text>
  <line x1="115" y1="314" x2="143" y2="314" stroke="#555" stroke-width="1.5"/>
  <text x="148" y="318" font-family="Georgia,serif" font-size="10" fill="#e8e4d8">Lohamp</text>
  <line x1="115" y1="328" x2="143" y2="328" stroke="#555" stroke-width="1.5"/>
  <text x="148" y="332" font-family="Georgia,serif" font-size="10" fill="#e8e4d8">Byttner</text>
  <line x1="115" y1="342" x2="143" y2="342" stroke="#555" stroke-width="1.5"/>
  <text x="148" y="346" font-family="Georgia,serif" font-size="10" fill="#e8e4d8">Yessen</text>
  <!-- Color swatches for caterpillar patterns -->
  <!-- Trigo: yellow+black -->
  <rect x="320" y="56" width="50" height="22" rx="3" fill="#1a1a00"/>
  <rect x="322" y="60" width="8" height="14" rx="1" fill="#f59e0b"/><rect x="333" y="60" width="3" height="14" fill="#111"/><rect x="338" y="60" width="8" height="14" rx="1" fill="#f59e0b"/><rect x="349" y="60" width="3" height="14" fill="#111"/><rect x="355" y="60" width="12" height="14" rx="1" fill="#f59e0b"/>
  <!-- Celt -->
  <rect x="320" y="88" width="50" height="22" rx="3" fill="#1a1a00"/>
  <rect x="322" y="92" width="46" height="14" rx="1" fill="#d97706"/>
  <!-- Sennov -->
  <rect x="320" y="144" width="50" height="22" rx="3" fill="#0a0a0a"/>
  <rect x="322" y="148" width="15" height="14" rx="1" fill="#dc2626"/><rect x="340" y="148" width="30" height="14" rx="1" fill="#e8e4d8"/>
  <!-- Hihamp -->
  <rect x="320" y="244" width="50" height="22" rx="3" fill="#0a0a0a"/>
  <rect x="322" y="248" width="46" height="14" rx="1" fill="#ea580c"/>
  <!-- Key label -->
  <text x="310" y="50" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#aaa">caterpillar pattern →</text>
  <!-- Caption box -->
  <rect x="60" y="356" width="400" height="20" rx="5" fill="#1e1e28" stroke="#7c6cf7" stroke-width="1"/>
  <text x="260" y="368" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#c4b5fd">One named species "A. fulgerator" = 10 cryptic species, each using different host plants</text>
</svg>"""


# ---------------------------------------------------------------------------
# Fig 13.18 — E. coli pan-genome vs core genome
# ---------------------------------------------------------------------------
SVG_FIG_13_18 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 320" width="540" height="320">
  <rect width="540" height="320" fill="#111118" rx="8"/>
  <text x="270" y="22" text-anchor="middle" font-family="Georgia,serif" font-size="13" font-weight="bold" fill="#e8e4d8">Fig 13.18 — E. coli Pan-Genome vs Core Genome</text>
  <!-- Left panel: Venn diagram -->
  <text x="120" y="46" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#aaa">A — Pan-genome concept</text>
  <!-- Outer ellipse (pan-genome border) -->
  <ellipse cx="120" cy="165" rx="108" ry="95" fill="none" stroke="#7c6cf7" stroke-width="1.5" stroke-dasharray="5,3"/>
  <text x="14" y="168" font-family="Georgia,serif" font-size="9" fill="#7c6cf7">Pan-genome</text>
  <!-- Three strain circles -->
  <circle cx="108" cy="142" r="48" fill="#4ea8de" opacity="0.18" stroke="#4ea8de" stroke-width="1"/>
  <circle cx="150" cy="142" r="48" fill="#00c9a7" opacity="0.18" stroke="#00c9a7" stroke-width="1"/>
  <circle cx="130" cy="180" r="48" fill="#ffc857" opacity="0.18" stroke="#ffc857" stroke-width="1"/>
  <text x="88" y="128" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#4ea8de" font-style="italic">E. coli</text>
  <text x="88" y="138" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#4ea8de">strain #1</text>
  <text x="172" y="128" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#00c9a7" font-style="italic">E. coli</text>
  <text x="172" y="138" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#00c9a7">strain #2</text>
  <text x="130" y="220" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#ffc857" font-style="italic">E. coli</text>
  <text x="130" y="230" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#ffc857">strain #3</text>
  <!-- Core genome label (intersection) -->
  <text x="130" y="164" text-anchor="middle" font-family="Georgia,serif" font-size="9" font-weight="bold" fill="#e8e4d8">Core</text>
  <text x="130" y="176" text-anchor="middle" font-family="Georgia,serif" font-size="9" font-weight="bold" fill="#e8e4d8">genome</text>
  <!-- Right panel: cumulative gene count curve -->
  <text x="390" y="46" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#aaa">B — Cumulative gene count as strains added</text>
  <!-- Axes -->
  <line x1="270" y1="280" x2="530" y2="280" stroke="#555" stroke-width="1.5"/>
  <line x1="270" y1="60" x2="270" y2="280" stroke="#555" stroke-width="1.5"/>
  <!-- Y axis labels -->
  <text x="260" y="64" text-anchor="end" font-family="Georgia,serif" font-size="9" fill="#aaa">15,000</text>
  <text x="260" y="128" text-anchor="end" font-family="Georgia,serif" font-size="9" fill="#aaa">10,000</text>
  <text x="260" y="192" text-anchor="end" font-family="Georgia,serif" font-size="9" fill="#aaa">5,000</text>
  <text x="260" y="280" text-anchor="end" font-family="Georgia,serif" font-size="9" fill="#aaa">0</text>
  <!-- X axis label -->
  <text x="400" y="298" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#aaa">Number of E. coli strains sequenced</text>
  <!-- Pan-genome curve (rising, then leveling off) -->
  <path d="M 275,220 Q 295,175 320,145 Q 345,120 370,108 Q 400,96 430,88 Q 460,82 490,78 L 525,76" stroke="#4ea8de" stroke-width="2" fill="none"/>
  <!-- Core genome flat line -->
  <line x1="275" y1="218" x2="525" y2="218" stroke="#e63946" stroke-width="2"/>
  <!-- Labels -->
  <text x="527" y="73" font-family="Georgia,serif" font-size="9" fill="#4ea8de">16,373</text>
  <text x="527" y="84" font-family="Georgia,serif" font-size="9" fill="#4ea8de">(pan)</text>
  <text x="527" y="215" font-family="Georgia,serif" font-size="9" fill="#e63946">3,051</text>
  <text x="527" y="225" font-family="Georgia,serif" font-size="9" fill="#e63946">(core)</text>
  <!-- Arrow labels on curves -->
  <text x="420" y="105" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#4ea8de">Pan-genome (keeps growing)</text>
  <text x="395" y="234" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#e63946">Core genome (stable, ~6% of genes)</text>
  <!-- Caption -->
  <rect x="60" y="296" width="420" height="18" rx="4" fill="#1e1e28" stroke="#ffc857" stroke-width="1"/>
  <text x="270" y="308" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#ffc857">Only ~6% of E. coli genes shared by all strains — rest acquired by HGT from unrelated organisms</text>
</svg>"""


# ---------------------------------------------------------------------------
# Fig 13.19 — Horizontal gene transfer in bacteria (mixing circles)
# ---------------------------------------------------------------------------
SVG_FIG_13_19 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 260" width="560" height="260">
  <rect width="560" height="260" fill="#111118" rx="8"/>
  <text x="280" y="22" text-anchor="middle" font-family="Georgia,serif" font-size="13" font-weight="bold" fill="#e8e4d8">Fig 13.19 — HGT Mixes Bacterial Genomes Across Lineages</text>
  <!-- Left side: "neatly divided by species barriers" -->
  <text x="100" y="44" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#aaa">Without HGT:</text>
  <text x="100" y="57" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#aaa">neat species boundaries</text>
  <!-- 4 colored bacteria groups -->
  <circle cx="55" cy="110" r="32" fill="#dc2626" opacity="0.5" stroke="#dc2626" stroke-width="1.5"/>
  <circle cx="105" cy="110" r="32" fill="#2563eb" opacity="0.5" stroke="#2563eb" stroke-width="1.5"/>
  <circle cx="55" cy="165" r="32" fill="#d97706" opacity="0.5" stroke="#d97706" stroke-width="1.5"/>
  <circle cx="105" cy="165" r="32" fill="#16a34a" opacity="0.5" stroke="#16a34a" stroke-width="1.5"/>
  <!-- DNA circles under each -->
  <circle cx="55" cy="210" r="14" fill="none" stroke="#dc2626" stroke-width="1.5"/>
  <circle cx="105" cy="210" r="14" fill="none" stroke="#2563eb" stroke-width="1.5"/>
  <text x="80" y="237" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#aaa">DNA</text>
  <!-- Arrow to the right -->
  <text x="165" y="148" text-anchor="middle" font-family="Georgia,serif" font-size="16" fill="#ffc857">→</text>
  <text x="165" y="162" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#ffc857">HGT</text>
  <!-- Right side: HGT mixed circles -->
  <text x="380" y="44" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#aaa">With HGT:</text>
  <text x="380" y="57" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#aaa">genes jump across all lineages</text>
  <!-- Mixed circles with arrows between -->
  <circle cx="260" cy="120" r="26" fill="none" stroke="#dc2626" stroke-width="1.5"/>
  <circle cx="320" cy="100" r="26" fill="none" stroke="#2563eb" stroke-width="1.5"/>
  <circle cx="380" cy="120" r="26" fill="none" stroke="#2563eb" stroke-width="1.5"/>
  <circle cx="440" cy="100" r="26" fill="none" stroke="#dc2626" stroke-width="1.5"/>
  <circle cx="280" cy="180" r="26" fill="none" stroke="#d97706" stroke-width="1.5"/>
  <circle cx="340" cy="195" r="26" fill="none" stroke="#16a34a" stroke-width="1.5"/>
  <circle cx="410" cy="178" r="26" fill="none" stroke="#d97706" stroke-width="1.5"/>
  <circle cx="470" cy="160" r="26" fill="none" stroke="#16a34a" stroke-width="1.5"/>
  <!-- HGT arrows between circles -->
  <defs><marker id="hgt_arr" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto"><path d="M0,0 L5,2.5 L0,5 Z" fill="#ffc857" opacity="0.7"/></marker></defs>
  <line x1="283" y1="108" x2="297" y2="104" stroke="#ffc857" stroke-width="1" marker-end="url(#hgt_arr)" opacity="0.7"/>
  <line x1="345" y1="106" x2="358" y2="112" stroke="#ffc857" stroke-width="1" marker-end="url(#hgt_arr)" opacity="0.7"/>
  <line x1="297" y1="130" x2="290" y2="158" stroke="#ffc857" stroke-width="1" marker-end="url(#hgt_arr)" opacity="0.7"/>
  <line x1="320" y1="124" x2="330" y2="170" stroke="#ffc857" stroke-width="1" marker-end="url(#hgt_arr)" opacity="0.7"/>
  <line x1="400" y1="122" x2="415" y2="152" stroke="#ffc857" stroke-width="1" marker-end="url(#hgt_arr)" opacity="0.7"/>
  <line x1="460" y1="120" x2="460" y2="138" stroke="#ffc857" stroke-width="1" marker-end="url(#hgt_arr)" opacity="0.7"/>
  <line x1="365" y1="192" x2="385" y2="183" stroke="#ffc857" stroke-width="1" marker-end="url(#hgt_arr)" opacity="0.7"/>
  <!-- Caption -->
  <rect x="60" y="224" width="440" height="30" rx="5" fill="#1e1e28" stroke="#7c6cf7" stroke-width="1"/>
  <text x="280" y="237" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#c4b5fd">HGT makes microbial species boundaries porous — genes flow across any lineage</text>
  <text x="280" y="249" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#aaa">"Life seems to blur into a jumble of mosaic-like genomes" (Doolittle &amp; Papke 2006)</text>
</svg>"""


# ---------------------------------------------------------------------------
# Fig 13.22 — Bacterial speciation with HGT (two lineages diverging)
# ---------------------------------------------------------------------------
SVG_FIG_13_22 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 240" width="600" height="240">
  <rect width="600" height="240" fill="#111118" rx="8"/>
  <text x="300" y="22" text-anchor="middle" font-family="Georgia,serif" font-size="13" font-weight="bold" fill="#e8e4d8">Fig 13.22 — Bacterial Speciation Model with HGT</text>
  <!-- Time arrow -->
  <line x1="40" y1="50" x2="570" y2="50" stroke="#aaa" stroke-width="1.5" marker-end="url(#time_arr)"/>
  <defs><marker id="time_arr" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#aaa"/></marker></defs>
  <text x="305" y="45" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#aaa">Time →</text>
  <!-- Ecologically associated population (left, blue DNA strands) -->
  <text x="90" y="72" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#93c5fd">Ecologically associated</text>
  <text x="90" y="82" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#93c5fd">populations of microbes</text>
  <!-- DNA strand representation (parallel lines) -->
  <path d="M 40,100 Q 90,95 140,100 Q 90,105 40,100" stroke="#4ea8de" stroke-width="2" fill="#4ea8de" opacity="0.3"/>
  <path d="M 40,115 Q 90,110 140,115 Q 90,120 40,115" stroke="#4ea8de" stroke-width="2" fill="#4ea8de" opacity="0.3"/>
  <path d="M 40,130 Q 90,125 140,130 Q 90,135 40,130" stroke="#4ea8de" stroke-width="2" fill="#4ea8de" opacity="0.3"/>
  <path d="M 40,145 Q 90,140 140,145 Q 90,150 40,145" stroke="#4ea8de" stroke-width="2" fill="#4ea8de" opacity="0.3"/>
  <path d="M 40,160 Q 90,155 140,160 Q 90,165 40,160" stroke="#4ea8de" stroke-width="2" fill="#4ea8de" opacity="0.3"/>
  <!-- HGT arrows within population (blue arrows within) -->
  <line x1="85" y1="100" x2="85" y2="115" stroke="#60a5fa" stroke-width="1.5" stroke-dasharray="2,2"/>
  <line x1="85" y1="115" x2="85" y2="130" stroke="#60a5fa" stroke-width="1.5" stroke-dasharray="2,2"/>
  <line x1="85" y1="130" x2="85" y2="145" stroke="#60a5fa" stroke-width="1.5" stroke-dasharray="2,2"/>
  <!-- Genes from unrelated microbes (yellow curved arrows coming from outside) -->
  <path d="M 80,60 Q 60,78 65,95" stroke="#ffc857" stroke-width="1.5" fill="none" marker-end="url(#hgt_arr2)"/>
  <path d="M 100,60 Q 115,80 110,95" stroke="#ffc857" stroke-width="1.5" fill="none" marker-end="url(#hgt_arr2)"/>
  <defs><marker id="hgt_arr2" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto"><path d="M0,0 L5,2.5 L0,5 Z" fill="#ffc857"/></marker></defs>
  <text x="60" y="58" text-anchor="middle" font-family="Georgia,serif" font-size="8" fill="#ffc857">genes from</text>
  <text x="60" y="67" text-anchor="middle" font-family="Georgia,serif" font-size="8" fill="#ffc857">unrelated microbes</text>
  <!-- Middle transition (divergence begins ~x=200) -->
  <line x1="160" y1="95" x2="200" y2="95" stroke="#555" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="160" y1="165" x2="200" y2="165" stroke="#555" stroke-width="1" stroke-dasharray="3,3"/>
  <!-- After divergence: two separate lineages (top=red, bottom=gold) -->
  <!-- Upper lineage (species 1, red) -->
  <path d="M 200,95 Q 380,90 570,85" stroke="#e63946" stroke-width="3" fill="none" opacity="0.8"/>
  <path d="M 200,105 Q 380,100 570,95" stroke="#e63946" stroke-width="3" fill="none" opacity="0.8"/>
  <!-- Cross-links on upper strand (ladder rungs) -->
  <line x1="260" y1="95" x2="260" y2="105" stroke="#e63946" stroke-width="1.5"/>
  <line x1="320" y1="94" x2="320" y2="104" stroke="#e63946" stroke-width="1.5"/>
  <line x1="380" y1="93" x2="380" y2="103" stroke="#e63946" stroke-width="1.5"/>
  <line x1="440" y1="92" x2="440" y2="102" stroke="#e63946" stroke-width="1.5"/>
  <line x1="500" y1="91" x2="500" y2="101" stroke="#e63946" stroke-width="1.5"/>
  <!-- Lower lineage (species 2, gold) -->
  <path d="M 200,155 Q 380,160 570,165" stroke="#d97706" stroke-width="3" fill="none" opacity="0.8"/>
  <path d="M 200,165 Q 380,170 570,175" stroke="#d97706" stroke-width="3" fill="none" opacity="0.8"/>
  <line x1="260" y1="155" x2="260" y2="165" stroke="#d97706" stroke-width="1.5"/>
  <line x1="320" y1="156" x2="320" y2="166" stroke="#d97706" stroke-width="1.5"/>
  <line x1="380" y1="157" x2="380" y2="167" stroke="#d97706" stroke-width="1.5"/>
  <line x1="440" y1="158" x2="440" y2="168" stroke="#d97706" stroke-width="1.5"/>
  <line x1="500" y1="159" x2="500" y2="169" stroke="#d97706" stroke-width="1.5"/>
  <!-- HGT between the two lineages AFTER speciation (curved arrows) -->
  <path d="M 350,104 Q 355,130 350,154" stroke="#ffc857" stroke-width="1.5" fill="none" marker-end="url(#hgt_arr2)" opacity="0.8"/>
  <path d="M 420,104 Q 415,130 420,154" stroke="#ffc857" stroke-width="1.5" fill="none" marker-end="url(#hgt_arr2)" opacity="0.8"/>
  <!-- Labels -->
  <text x="540" y="82" text-anchor="start" font-family="Georgia,serif" font-size="10" fill="#e63946">Species 1</text>
  <text x="540" y="178" text-anchor="start" font-family="Georgia,serif" font-size="10" fill="#d97706">Species 2</text>
  <text x="330" y="136" text-anchor="middle" font-family="Georgia,serif" font-size="8" fill="#ffc857">HGT after</text>
  <text x="330" y="146" text-anchor="middle" font-family="Georgia,serif" font-size="8" fill="#ffc857">speciation</text>
  <!-- Divergence marker -->
  <line x1="200" y1="80" x2="200" y2="180" stroke="#aaa" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="200" y="195" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#aaa">ecological speciation</text>
  <!-- Caption -->
  <rect x="60" y="208" width="480" height="26" rx="5" fill="#1e1e28" stroke="#7c6cf7" stroke-width="1"/>
  <text x="300" y="220" text-anchor="middle" font-family="Georgia,serif" font-size="10" fill="#c4b5fd">HGT is frequent within ecologically associated populations (Cohan 2006 stable ecotype model)</text>
  <text x="300" y="230" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#aaa">Genes acquired from other lineages drive ecological divergence → eventual speciation</text>
</svg>"""
