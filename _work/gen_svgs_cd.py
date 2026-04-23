#!/usr/bin/env python3
"""Groups C (speciation) + D (biogeography) SVGs."""
import os, sys
sys.stdout.reconfigure(encoding='utf-8')
OUT = "C:/Users/johnn/Desktop/School/Evolution_EVOL4230/evolution-study-guide/public/img/fc"
os.makedirs(OUT, exist_ok=True)
VB = 'viewBox="0 0 240 150" width="240" height="150" xmlns="http://www.w3.org/2000/svg"'
BG = '<rect width="240" height="150" fill="#0a1220"/>'
FT = 'font-family="system-ui,Segoe UI,sans-serif"'
def W(name, body):
    with open(os.path.join(OUT, f"svg_{name}.svg"), 'w', encoding='utf-8') as f:
        f.write(f'<svg {VB}>{BG}{body}</svg>')
def T(text, y=14):
    return f'<text x="120" y="{y}" text-anchor="middle" fill="#fbbf24" font-size="11" font-weight="700" {FT}>{text}</text>'
def S(text, y=26, color="#94a3b8"):
    return f'<text x="120" y="{y}" text-anchor="middle" fill="{color}" font-size="9" {FT}>{text}</text>'

# GROUP C — SPECIATION
W("bsc", T("BIOLOGICAL SPECIES CONCEPT") + S('"Can they produce fertile offspring?"') + f'''
<circle cx="55" cy="70" r="14" fill="#1e3a5f" stroke="#60a5fa"/>
<circle cx="85" cy="70" r="14" fill="#1e3a5f" stroke="#60a5fa"/>
<path d="M70 85 Q70 95 70 100" stroke="#22c55e" stroke-width="2" fill="none"/>
<circle cx="70" cy="108" r="8" fill="#22c55e"/>
<text x="70" y="112" text-anchor="middle" fill="#fff" font-size="9" font-weight="700" {FT}>✓</text>
<text x="70" y="135" text-anchor="middle" fill="#86efac" font-size="8" font-weight="700" {FT}>SAME species</text>
<circle cx="155" cy="70" r="14" fill="#1e3a5f" stroke="#60a5fa"/>
<circle cx="195" cy="70" r="14" fill="#7f1d1d" stroke="#ef4444"/>
<line x1="170" y1="70" x2="180" y2="70" stroke="#ef4444" stroke-width="2" stroke-dasharray="2,2"/>
<line x1="172" y1="64" x2="180" y2="76" stroke="#ef4444" stroke-width="2"/>
<line x1="172" y1="76" x2="180" y2="64" stroke="#ef4444" stroke-width="2"/>
<text x="175" y="108" text-anchor="middle" fill="#ef4444" font-size="9" font-weight="700" {FT}>✗</text>
<text x="175" y="135" text-anchor="middle" fill="#fca5a5" font-size="8" font-weight="700" {FT}>DIFFERENT species</text>
''')

W("speciation_3step", T("3-STEP SPECIATION") + f'''
<circle cx="40" cy="70" r="10" fill="#60a5fa" opacity="0.7"/>
<circle cx="55" cy="70" r="10" fill="#60a5fa" opacity="0.7"/>
<path d="M40 70 L55 70" stroke="#22c55e" stroke-width="2"/>
<text x="47" y="100" text-anchor="middle" fill="#86efac" font-size="7" {FT}>gene flow</text>
<text x="47" y="112" text-anchor="middle" fill="#94a3b8" font-size="7" {FT}>1. One pop</text>
<text x="77" y="75" fill="#fbbf24" font-size="16" {FT}>→</text>
<circle cx="105" cy="60" r="10" fill="#60a5fa" opacity="0.7"/>
<circle cx="135" cy="80" r="10" fill="#a78bfa" opacity="0.7"/>
<rect x="117" y="45" width="4" height="50" fill="#7f1d1d"/>
<text x="120" y="112" text-anchor="middle" fill="#94a3b8" font-size="7" {FT}>2. Barrier</text>
<text x="157" y="75" fill="#fbbf24" font-size="16" {FT}>→</text>
<circle cx="185" cy="60" r="10" fill="#60a5fa"/>
<circle cx="210" cy="80" r="10" fill="#a78bfa"/>
<line x1="196" y1="65" x2="203" y2="78" stroke="#ef4444" stroke-width="2" stroke-dasharray="2,2"/>
<text x="197" y="112" text-anchor="middle" fill="#ef4444" font-size="7" {FT}>3. Isolation</text>
<text x="120" y="135" text-anchor="middle" fill="#fbbf24" font-size="8" font-weight="700" {FT}>Barrier → divergence → reproductive isolation</text>
''')

W("prezygotic", T("PREZYGOTIC BARRIERS") + S("Block BEFORE fertilization") + f'''
<rect x="20" y="34" width="200" height="16" fill="#161b22" stroke="#60a5fa" rx="2"/>
<text x="30" y="45" fill="#93c5fd" font-size="8" font-weight="700" {FT}>• Habitat</text>
<text x="110" y="45" fill="#94a3b8" font-size="7" {FT}>different environments</text>
<rect x="20" y="52" width="200" height="16" fill="#161b22" stroke="#60a5fa" rx="2"/>
<text x="30" y="63" fill="#93c5fd" font-size="8" font-weight="700" {FT}>• Temporal</text>
<text x="110" y="63" fill="#94a3b8" font-size="7" {FT}>different timing</text>
<rect x="20" y="70" width="200" height="16" fill="#161b22" stroke="#60a5fa" rx="2"/>
<text x="30" y="81" fill="#93c5fd" font-size="8" font-weight="700" {FT}>• Behavioral</text>
<text x="110" y="81" fill="#94a3b8" font-size="7" {FT}>different signals/calls</text>
<rect x="20" y="88" width="200" height="16" fill="#161b22" stroke="#60a5fa" rx="2"/>
<text x="30" y="99" fill="#93c5fd" font-size="8" font-weight="700" {FT}>• Mechanical</text>
<text x="110" y="99" fill="#94a3b8" font-size="7" {FT}>incompatible anatomy</text>
<rect x="20" y="106" width="200" height="16" fill="#161b22" stroke="#60a5fa" rx="2"/>
<text x="30" y="117" fill="#93c5fd" font-size="8" font-weight="700" {FT}>• Gametic</text>
<text x="110" y="117" fill="#94a3b8" font-size="7" {FT}>sperm/egg mismatch</text>
<text x="120" y="140" text-anchor="middle" fill="#fbbf24" font-size="8" font-weight="700" {FT}>Strongest & evolved first</text>
''')

W("postzygotic", T("POSTZYGOTIC BARRIERS") + S("After fertilization — hybrid fails") + f'''
<circle cx="55" cy="55" r="10" fill="#60a5fa" opacity="0.7"/>
<circle cx="85" cy="55" r="10" fill="#a78bfa" opacity="0.7"/>
<line x1="70" y1="67" x2="70" y2="77" stroke="#fbbf24" stroke-width="2"/>
<polygon points="70,77 66,70 74,70" fill="#fbbf24"/>
<circle cx="70" cy="92" r="8" fill="#57534e"/>
<line x1="62" y1="84" x2="78" y2="100" stroke="#ef4444" stroke-width="2"/>
<line x1="62" y1="100" x2="78" y2="84" stroke="#ef4444" stroke-width="2"/>
<text x="70" y="120" text-anchor="middle" fill="#fca5a5" font-size="8" font-weight="700" {FT}>Inviability</text>
<text x="70" y="132" text-anchor="middle" fill="#94a3b8" font-size="7" {FT}>embryo dies</text>
<circle cx="170" cy="55" r="10" fill="#60a5fa"/>
<circle cx="200" cy="55" r="10" fill="#a78bfa"/>
<polygon points="185,75 181,68 189,68" fill="#fbbf24"/>
<line x1="185" y1="67" x2="185" y2="77" stroke="#fbbf24" stroke-width="2"/>
<circle cx="185" cy="92" r="9" fill="#d97706"/>
<text x="185" y="96" text-anchor="middle" fill="#fff" font-size="9" {FT}>🐴</text>
<line x1="185" y1="103" x2="185" y2="113" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="2,2"/>
<text x="185" y="120" text-anchor="middle" fill="#fca5a5" font-size="8" font-weight="700" {FT}>Sterility</text>
<text x="185" y="132" text-anchor="middle" fill="#94a3b8" font-size="7" {FT}>mule = sterile</text>
''')

W("mule_sterility", T("MULE STERILITY") + f'''
<ellipse cx="50" cy="55" rx="28" ry="18" fill="#57534e" stroke="#a8a29e"/>
<text x="50" y="59" text-anchor="middle" fill="#fff" font-size="9" font-weight="700" {FT}>Horse</text>
<text x="50" y="85" text-anchor="middle" fill="#fbbf24" font-size="8" font-weight="700" {FT}>2n = 64</text>
<text x="95" y="60" fill="#94a3b8" font-size="16" {FT}>×</text>
<ellipse cx="140" cy="55" rx="28" ry="18" fill="#78716c" stroke="#a8a29e"/>
<text x="140" y="59" text-anchor="middle" fill="#fff" font-size="9" font-weight="700" {FT}>Donkey</text>
<text x="140" y="85" text-anchor="middle" fill="#fbbf24" font-size="8" font-weight="700" {FT}>2n = 62</text>
<text x="183" y="60" fill="#94a3b8" font-size="16" {FT}>=</text>
<ellipse cx="215" cy="55" rx="22" ry="15" fill="#92400e" stroke="#d97706"/>
<text x="215" y="59" text-anchor="middle" fill="#fff" font-size="8" font-weight="700" {FT}>Mule</text>
<text x="215" y="85" text-anchor="middle" fill="#ef4444" font-size="8" font-weight="700" {FT}>2n = 63</text>
<rect x="40" y="100" width="180" height="30" fill="#1a0a0a" stroke="#7f1d1d" rx="3"/>
<text x="130" y="113" text-anchor="middle" fill="#f87171" font-size="8" font-weight="700" {FT}>ODD chromosome → meiosis fails</text>
<text x="130" y="125" text-anchor="middle" fill="#fca5a5" font-size="8" {FT}>→ STERILE (hybrid sterility, not inviability)</text>
''')

W("allopatric", T("ALLOPATRIC SPECIATION") + S("Geographic barrier splits population") + f'''
<ellipse cx="60" cy="75" rx="30" ry="20" fill="#1e3a5f" stroke="#60a5fa"/>
<text x="60" y="79" text-anchor="middle" fill="#93c5fd" font-size="8" font-weight="700" {FT}>Pop A</text>
<rect x="105" y="40" width="30" height="70" fill="#57534e" opacity="0.8"/>
<polygon points="105,40 120,28 135,40" fill="#57534e"/>
<text x="120" y="145" text-anchor="middle" fill="#a8a29e" font-size="7" {FT}>mountain</text>
<ellipse cx="180" cy="75" rx="30" ry="20" fill="#14532d" stroke="#22c55e"/>
<text x="180" y="79" text-anchor="middle" fill="#86efac" font-size="8" font-weight="700" {FT}>Pop B</text>
<path d="M40 105 Q120 125 200 105" stroke="#fbbf24" stroke-width="1" stroke-dasharray="3,2" fill="none"/>
<text x="120" y="130" text-anchor="middle" fill="#fbbf24" font-size="8" {FT}>no gene flow</text>
''')

W("sympatric", T("SYMPATRIC SPECIATION") + S("Same place · diverge by resource") + f'''
<rect x="25" y="38" width="190" height="70" fill="#0f172a" rx="5" stroke="#475569"/>
<text x="120" y="50" text-anchor="middle" fill="#94a3b8" font-size="8" {FT}>Same habitat</text>
<circle cx="65" cy="75" r="8" fill="#16a34a"/>
<text x="65" y="95" text-anchor="middle" fill="#86efac" font-size="7" {FT}>Hawthorn</text>
<circle cx="175" cy="75" r="8" fill="#d97706"/>
<text x="175" y="95" text-anchor="middle" fill="#fde68a" font-size="7" {FT}>Apple</text>
<circle cx="80" cy="78" r="3" fill="#60a5fa"/>
<circle cx="88" cy="72" r="3" fill="#60a5fa"/>
<circle cx="160" cy="78" r="3" fill="#a78bfa"/>
<circle cx="152" cy="72" r="3" fill="#a78bfa"/>
<text x="120" y="125" text-anchor="middle" fill="#fbbf24" font-size="8" font-weight="700" {FT}>Rhagoletis pomonella (apple maggot fly)</text>
<text x="120" y="140" text-anchor="middle" fill="#94a3b8" font-size="7" {FT}>Host shift → reproductive isolation w/o geography</text>
''')

W("reinforcement", T("REINFORCEMENT") + f'''
<ellipse cx="60" cy="60" rx="22" ry="14" fill="#1e3a5f" stroke="#60a5fa"/>
<text x="60" y="63" text-anchor="middle" fill="#93c5fd" font-size="7" {FT}>Pop A</text>
<ellipse cx="180" cy="60" rx="22" ry="14" fill="#14532d" stroke="#22c55e"/>
<text x="180" y="63" text-anchor="middle" fill="#86efac" font-size="7" {FT}>Pop B</text>
<ellipse cx="120" cy="60" rx="20" ry="12" fill="#7c3aed" opacity="0.3" stroke="#a78bfa"/>
<text x="120" y="63" text-anchor="middle" fill="#c4b5fd" font-size="7" {FT}>hybrids</text>
<line x1="110" y1="75" x2="110" y2="90" stroke="#ef4444" stroke-width="2"/>
<line x1="130" y1="75" x2="130" y2="90" stroke="#ef4444" stroke-width="2"/>
<text x="120" y="102" text-anchor="middle" fill="#ef4444" font-size="7" font-weight="700" {FT}>low fitness → selection</text>
<text x="120" y="120" text-anchor="middle" fill="#fbbf24" font-size="8" font-weight="700" {FT}>Prezygotic barriers strengthen</text>
<text x="120" y="133" text-anchor="middle" fill="#94a3b8" font-size="7" {FT}>"Spellcheck gets stricter after bad hybrids"</text>
''')

W("bdm", T("DOBZHANSKY-MULLER INCOMPATIBILITY") + f'''
<rect x="15" y="35" width="90" height="85" fill="#101620" stroke="#60a5fa" rx="3"/>
<text x="60" y="48" text-anchor="middle" fill="#93c5fd" font-size="8" font-weight="700" {FT}>Pop A genome</text>
<circle cx="40" cy="68" r="7" fill="#60a5fa"/><text x="40" y="72" text-anchor="middle" fill="#fff" font-size="8" {FT}>A</text>
<circle cx="80" cy="68" r="7" fill="#60a5fa"/><text x="80" y="72" text-anchor="middle" fill="#fff" font-size="8" {FT}>b</text>
<path d="M48 68 L72 68" stroke="#22c55e" stroke-width="2"/>
<text x="60" y="110" text-anchor="middle" fill="#86efac" font-size="7" {FT}>OK ✓</text>
<rect x="135" y="35" width="90" height="85" fill="#101620" stroke="#a78bfa" rx="3"/>
<text x="180" y="48" text-anchor="middle" fill="#c4b5fd" font-size="8" font-weight="700" {FT}>Pop B genome</text>
<circle cx="160" cy="68" r="7" fill="#a78bfa"/><text x="160" y="72" text-anchor="middle" fill="#fff" font-size="8" {FT}>a</text>
<circle cx="200" cy="68" r="7" fill="#a78bfa"/><text x="200" y="72" text-anchor="middle" fill="#fff" font-size="8" {FT}>B</text>
<path d="M168 68 L192 68" stroke="#22c55e" stroke-width="2"/>
<text x="180" y="110" text-anchor="middle" fill="#86efac" font-size="7" {FT}>OK ✓</text>
<rect x="80" y="128" width="80" height="18" fill="#3b1515" stroke="#ef4444"/>
<text x="120" y="140" text-anchor="middle" fill="#fca5a5" font-size="8" font-weight="700" {FT}>Hybrid A+B → INCOMPATIBLE</text>
''')

W("allopolyploidy", T("ALLOPOLYPLOIDY — instant speciation") + f'''
<rect x="15" y="30" width="48" height="14" fill="#60a5fa" rx="1"/>
<rect x="15" y="46" width="48" height="14" fill="#60a5fa" rx="1"/>
<text x="39" y="75" text-anchor="middle" fill="#93c5fd" font-size="8" {FT}>Sp A 2n=4</text>
<text x="72" y="48" fill="#94a3b8" font-size="12" {FT}>×</text>
<rect x="85" y="30" width="48" height="14" fill="#a78bfa" rx="1"/>
<rect x="85" y="46" width="48" height="14" fill="#a78bfa" rx="1"/>
<text x="109" y="75" text-anchor="middle" fill="#c4b5fd" font-size="8" {FT}>Sp B 2n=4</text>
<text x="142" y="48" fill="#fbbf24" font-size="14" {FT}>→</text>
<rect x="160" y="30" width="24" height="10" fill="#60a5fa" rx="1"/>
<rect x="160" y="44" width="24" height="10" fill="#a78bfa" rx="1"/>
<text x="172" y="70" text-anchor="middle" fill="#ef4444" font-size="7" {FT}>hybrid</text>
<text x="172" y="80" text-anchor="middle" fill="#fca5a5" font-size="6" {FT}>sterile</text>
<text x="192" y="50" fill="#fbbf24" font-size="10" {FT}>→×2</text>
<rect x="208" y="25" width="22" height="8" fill="#60a5fa" rx="1"/>
<rect x="208" y="35" width="22" height="8" fill="#60a5fa" rx="1"/>
<rect x="208" y="45" width="22" height="8" fill="#a78bfa" rx="1"/>
<rect x="208" y="55" width="22" height="8" fill="#a78bfa" rx="1"/>
<text x="219" y="80" text-anchor="middle" fill="#22c55e" font-size="7" {FT}>2n=8</text>
<text x="120" y="105" text-anchor="middle" fill="#22c55e" font-size="9" font-weight="700" {FT}>NEW FERTILE SPECIES</text>
<text x="120" y="120" text-anchor="middle" fill="#94a3b8" font-size="8" {FT}>Chromosome doubling → instant isolation</text>
<text x="120" y="135" text-anchor="middle" fill="#64748b" font-size="7" {FT}>Bread wheat (hexaploid) formed this way</text>
''')

W("peripatric", T("PERIPATRIC SPECIATION") + S("Small peripheral founder + drift") + f'''
<ellipse cx="80" cy="80" rx="55" ry="35" fill="#1e3a5f" stroke="#60a5fa"/>
<text x="80" y="82" text-anchor="middle" fill="#93c5fd" font-size="9" font-weight="700" {FT}>Mainland</text>
<text x="80" y="95" text-anchor="middle" fill="#93c5fd" font-size="7" {FT}>large population</text>
<path d="M135 70 Q160 65 180 75" stroke="#fbbf24" stroke-width="1.5" fill="none" stroke-dasharray="2,2"/>
<polygon points="180,75 175,72 176,78" fill="#fbbf24"/>
<circle cx="195" cy="80" r="15" fill="#14532d" stroke="#22c55e"/>
<text x="195" y="82" text-anchor="middle" fill="#86efac" font-size="7" font-weight="700" {FT}>Founder</text>
<text x="195" y="105" text-anchor="middle" fill="#86efac" font-size="7" {FT}>(few)</text>
<text x="120" y="130" text-anchor="middle" fill="#fbbf24" font-size="8" font-weight="700" {FT}>Founder effect + drift → rapid divergence</text>
<text x="120" y="143" text-anchor="middle" fill="#94a3b8" font-size="7" {FT}>Hawaiian Laupala: 13 spp in <5 Myr</text>
''')

W("hybrid_zone", T("HYBRID ZONE") + f'''
<rect x="15" y="50" width="210" height="50" fill="#0f172a"/>
<ellipse cx="60" cy="75" rx="40" ry="22" fill="#1e3a5f" opacity="0.8"/>
<ellipse cx="180" cy="75" rx="40" ry="22" fill="#14532d" opacity="0.8"/>
<ellipse cx="120" cy="75" rx="25" ry="15" fill="#7c3aed" opacity="0.6"/>
<text x="60" y="78" text-anchor="middle" fill="#93c5fd" font-size="9" font-weight="700" {FT}>Species A</text>
<text x="180" y="78" text-anchor="middle" fill="#86efac" font-size="9" font-weight="700" {FT}>Species B</text>
<text x="120" y="78" text-anchor="middle" fill="#c4b5fd" font-size="8" font-weight="700" {FT}>hybrids</text>
<text x="120" y="120" text-anchor="middle" fill="#94a3b8" font-size="8" {FT}>Contact zone with intermediate phenotypes</text>
<text x="120" y="135" text-anchor="middle" fill="#64748b" font-size="8" {FT}>Stable zones persist if hybrids ≈ fit</text>
''')

W("character_displacement", T("CHARACTER DISPLACEMENT") + f'''
<text x="60" y="38" text-anchor="middle" fill="#94a3b8" font-size="8" font-weight="700" {FT}>BEFORE</text>
<path d="M20 75 Q50 45 60 45 Q80 45 100 75" fill="none" stroke="#60a5fa" stroke-width="2"/>
<path d="M25 75 Q55 55 65 55 Q85 55 105 75" fill="none" stroke="#a78bfa" stroke-width="2"/>
<text x="60" y="88" text-anchor="middle" fill="#94a3b8" font-size="7" {FT}>overlapping</text>
<text x="180" y="38" text-anchor="middle" fill="#22c55e" font-size="8" font-weight="700" {FT}>AFTER (sympatry)</text>
<path d="M130 75 Q145 45 155 45 Q170 45 180 75" fill="none" stroke="#60a5fa" stroke-width="2"/>
<path d="M170 75 Q185 55 205 55 Q220 55 230 75" fill="none" stroke="#a78bfa" stroke-width="2"/>
<text x="180" y="88" text-anchor="middle" fill="#86efac" font-size="7" {FT}>diverged!</text>
<line x1="15" y1="95" x2="225" y2="95" stroke="#334155"/>
<text x="120" y="110" text-anchor="middle" fill="#fbbf24" font-size="8" font-weight="700" {FT}>Competition in sympatry → divergence</text>
<text x="120" y="125" text-anchor="middle" fill="#94a3b8" font-size="7" {FT}>Darwin finch beak example</text>
<text x="120" y="140" text-anchor="middle" fill="#64748b" font-size="7" {FT}>X-axis: trait value (e.g., beak depth)</text>
''')

W("tempo_evolution", T("TEMPO: GRADUALISM vs PUNCTUATED EQ") + f'''
<text x="60" y="38" text-anchor="middle" fill="#60a5fa" font-size="9" font-weight="700" {FT}>Gradualism</text>
<line x1="20" y1="120" x2="100" y2="120" stroke="#334155"/>
<line x1="20" y1="45" x2="20" y2="120" stroke="#334155"/>
<polyline points="20,115 35,105 50,85 65,65 80,55 95,50" stroke="#60a5fa" stroke-width="2" fill="none"/>
<text x="60" y="135" text-anchor="middle" fill="#94a3b8" font-size="7" {FT}>smooth continuous</text>
<text x="180" y="38" text-anchor="middle" fill="#a78bfa" font-size="9" font-weight="700" {FT}>Punctuated Eq</text>
<line x1="140" y1="120" x2="220" y2="120" stroke="#334155"/>
<line x1="140" y1="45" x2="140" y2="120" stroke="#334155"/>
<polyline points="140,115 165,115 165,75 190,75 190,50 215,50" stroke="#a78bfa" stroke-width="2" fill="none"/>
<text x="180" y="135" text-anchor="middle" fill="#94a3b8" font-size="7" {FT}>stasis + jumps</text>
<text x="120" y="148" text-anchor="middle" fill="#64748b" font-size="7" {FT}>Same endpoints · different tempo</text>
''')

W("parapatric", T("PARAPATRIC SPECIATION") + f'''
<defs><linearGradient id="grad1"><stop offset="0%" stop-color="#60a5fa"/><stop offset="100%" stop-color="#22c55e"/></linearGradient></defs>
<rect x="20" y="50" width="200" height="40" fill="url(#grad1)"/>
<text x="40" y="75" text-anchor="middle" fill="#fff" font-size="8" font-weight="700" {FT}>Pop A</text>
<text x="200" y="75" text-anchor="middle" fill="#000" font-size="8" font-weight="700" {FT}>Pop B</text>
<text x="120" y="75" text-anchor="middle" fill="#fde68a" font-size="7" {FT}>gradient</text>
<text x="120" y="105" text-anchor="middle" fill="#fbbf24" font-size="8" font-weight="700" {FT}>Adjacent · clinal variation</text>
<text x="120" y="120" text-anchor="middle" fill="#94a3b8" font-size="7" {FT}>Strong selection along gradient</text>
<text x="120" y="134" text-anchor="middle" fill="#64748b" font-size="7" {FT}>No full geographic barrier</text>
''')

W("temporal_isolation", T("TEMPORAL ISOLATION") + f'''
<rect x="20" y="40" width="200" height="65" fill="#0f172a" stroke="#334155" rx="3"/>
<text x="30" y="55" fill="#94a3b8" font-size="7" font-weight="700" {FT}>J F M A M J J A S O N D</text>
<rect x="48" y="65" width="35" height="10" fill="#60a5fa"/>
<text x="65" y="73" text-anchor="middle" fill="#fff" font-size="7" {FT}>Species 1</text>
<rect x="145" y="85" width="50" height="10" fill="#22c55e"/>
<text x="170" y="93" text-anchor="middle" fill="#fff" font-size="7" {FT}>Species 2</text>
<text x="120" y="125" text-anchor="middle" fill="#fbbf24" font-size="8" font-weight="700" {FT}>No breeding-season overlap</text>
<text x="120" y="140" text-anchor="middle" fill="#94a3b8" font-size="7" {FT}>E.g., cicadas 13-yr vs 17-yr cycles</text>
''')

W("gametic_incompatibility", T("GAMETIC INCOMPATIBILITY") + f'''
<circle cx="65" cy="75" r="28" fill="#7c2d12" stroke="#ea580c"/>
<text x="65" y="78" text-anchor="middle" fill="#fed7aa" font-size="8" font-weight="700" {FT}>EGG</text>
<polygon points="45,60 50,55 48,50 40,48 42,55" fill="#fbbf24"/>
<polygon points="90,55 95,50 93,45 85,43 87,50" fill="#fbbf24"/>
<polygon points="45,90 50,95 48,100 40,102 42,95" fill="#fbbf24"/>
<ellipse cx="160" cy="75" rx="20" ry="6" fill="#22c55e"/>
<circle cx="145" cy="75" r="8" fill="#22c55e"/>
<polygon points="143,69 140,65 138,70 140,75" fill="#ef4444"/>
<line x1="135" y1="75" x2="115" y2="75" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="2,2"/>
<text x="165" y="55" fill="#86efac" font-size="7" {FT}>sperm</text>
<text x="165" y="100" fill="#ef4444" font-size="7" font-weight="700" {FT}>won't bind!</text>
<text x="120" y="125" text-anchor="middle" fill="#fbbf24" font-size="8" font-weight="700" {FT}>Species-specific surface proteins</text>
<text x="120" y="140" text-anchor="middle" fill="#94a3b8" font-size="7" {FT}>Molecular lock-and-key mismatch</text>
''')

# GROUP D — BIOGEOGRAPHY
W("continental_drift", T("CONTINENTAL DRIFT") + f'''
<circle cx="45" cy="55" r="18" fill="#92400e"/>
<text x="45" y="58" text-anchor="middle" fill="#fff" font-size="7" font-weight="700" {FT}>Pangaea</text>
<text x="45" y="85" text-anchor="middle" fill="#94a3b8" font-size="7" {FT}>300 mya</text>
<path d="M75 55 L95 55" stroke="#fbbf24" stroke-width="1.5"/>
<polygon points="95,55 91,51 91,59" fill="#fbbf24"/>
<ellipse cx="115" cy="48" rx="12" ry="8" fill="#d97706"/>
<text x="115" y="50" text-anchor="middle" fill="#fff" font-size="6" {FT}>N</text>
<ellipse cx="115" cy="65" rx="12" ry="8" fill="#a16207"/>
<text x="115" y="67" text-anchor="middle" fill="#fff" font-size="6" {FT}>S</text>
<text x="115" y="85" text-anchor="middle" fill="#94a3b8" font-size="7" {FT}>200 mya</text>
<path d="M135 55 L155 55" stroke="#fbbf24" stroke-width="1.5"/>
<polygon points="155,55 151,51 151,59" fill="#fbbf24"/>
<g>
<ellipse cx="175" cy="45" rx="7" ry="5" fill="#d97706"/>
<ellipse cx="190" cy="42" rx="6" ry="4" fill="#ca8a04"/>
<ellipse cx="215" cy="48" rx="8" ry="5" fill="#059669"/>
<ellipse cx="180" cy="62" rx="6" ry="4" fill="#a16207"/>
<ellipse cx="200" cy="68" rx="7" ry="4" fill="#0891b2"/>
<ellipse cx="215" cy="70" rx="5" ry="3" fill="#d97706"/>
</g>
<text x="195" y="85" text-anchor="middle" fill="#94a3b8" font-size="7" {FT}>today</text>
<text x="120" y="110" text-anchor="middle" fill="#fbbf24" font-size="8" font-weight="700" {FT}>Pangaea → Gondwana + Laurasia → now</text>
<text x="120" y="125" text-anchor="middle" fill="#94a3b8" font-size="7" {FT}>Explains marsupial south / placental north</text>
<text x="120" y="140" text-anchor="middle" fill="#64748b" font-size="7" {FT}>Wegener 1912 · confirmed by plate tectonics</text>
''')

W("vicariance", T("VICARIANCE") + S("Land moves · organisms stay") + f'''
<ellipse cx="120" cy="75" rx="90" ry="25" fill="#14532d" stroke="#22c55e"/>
<circle cx="70" cy="75" r="5" fill="#fbbf24"/>
<circle cx="90" cy="75" r="5" fill="#fbbf24"/>
<circle cx="150" cy="75" r="5" fill="#fbbf24"/>
<circle cx="170" cy="75" r="5" fill="#fbbf24"/>
<line x1="118" y1="45" x2="118" y2="105" stroke="#7f1d1d" stroke-width="3" stroke-dasharray="3,2"/>
<polygon points="118,50 114,55 122,55" fill="#7f1d1d"/>
<polygon points="118,100 114,95 122,95" fill="#7f1d1d"/>
<text x="125" y="40" fill="#ef4444" font-size="8" font-weight="700" {FT}>Barrier forms</text>
<text x="85" y="120" text-anchor="middle" fill="#86efac" font-size="8" {FT}>Same pop</text>
<text x="160" y="120" text-anchor="middle" fill="#86efac" font-size="8" {FT}>Same pop</text>
<text x="120" y="135" text-anchor="middle" fill="#fbbf24" font-size="8" font-weight="700" {FT}>Barrier forms AROUND stationary organisms</text>
<text x="120" y="147" text-anchor="middle" fill="#64748b" font-size="7" {FT}>"Land moves, organisms stay"</text>
''')

W("dispersal_bio", T("DISPERSAL BIOGEOGRAPHY") + S("Organisms move · land stays") + f'''
<ellipse cx="55" cy="80" rx="30" ry="20" fill="#14532d" stroke="#22c55e"/>
<text x="55" y="84" text-anchor="middle" fill="#86efac" font-size="8" font-weight="700" {FT}>Source</text>
<path d="M50 65 Q50 55 60 52 Q65 55 63 65 Z" fill="#fbbf24" stroke="#ca8a04"/>
<rect x="95" y="75" width="50" height="15" fill="#1e40af" opacity="0.6"/>
<text x="120" y="86" text-anchor="middle" fill="#93c5fd" font-size="7" {FT}>water barrier</text>
<path d="M85 62 Q120 50 155 70" stroke="#fbbf24" stroke-width="1.5" fill="none" stroke-dasharray="3,2"/>
<polygon points="155,70 151,66 150,73" fill="#fbbf24"/>
<ellipse cx="185" cy="80" rx="28" ry="18" fill="#1e3a5f" stroke="#60a5fa"/>
<text x="185" y="84" text-anchor="middle" fill="#93c5fd" font-size="8" font-weight="700" {FT}>New habitat</text>
<path d="M180 70 Q180 62 188 60 Q192 62 190 70 Z" fill="#fbbf24"/>
<text x="120" y="120" text-anchor="middle" fill="#fbbf24" font-size="8" font-weight="700" {FT}>Organism crosses existing barrier</text>
<text x="120" y="135" text-anchor="middle" fill="#94a3b8" font-size="7" {FT}>Founds new population → diverges</text>
''')

W("island_biogeography", T("ISLAND BIOGEOGRAPHY") + S("Equilibrium = immigration = extinction") + f'''
<line x1="30" y1="40" x2="30" y2="120" stroke="#475569"/>
<line x1="30" y1="120" x2="220" y2="120" stroke="#475569"/>
<text x="15" y="45" fill="#94a3b8" font-size="7" {FT}>rate</text>
<text x="220" y="135" fill="#94a3b8" font-size="7" {FT}>species</text>
<polyline points="30,45 80,70 130,85 180,95 215,100" stroke="#22c55e" stroke-width="2" fill="none"/>
<text x="40" y="58" fill="#86efac" font-size="8" font-weight="700" {FT}>immigration</text>
<polyline points="30,115 80,100 130,85 180,70 215,55" stroke="#ef4444" stroke-width="2" fill="none"/>
<text x="180" y="68" fill="#fca5a5" font-size="8" font-weight="700" {FT}>extinction</text>
<circle cx="130" cy="85" r="5" fill="#fbbf24"/>
<line x1="130" y1="90" x2="130" y2="120" stroke="#fbbf24" stroke-width="1" stroke-dasharray="2,2"/>
<text x="130" y="135" text-anchor="middle" fill="#fbbf24" font-size="8" font-weight="700" {FT}>S* equilibrium</text>
<text x="120" y="148" text-anchor="middle" fill="#64748b" font-size="7" {FT}>MacArthur & Wilson 1967</text>
''')

W("adaptive_radiation", T("ADAPTIVE RADIATION") + f'''
<circle cx="120" cy="125" r="8" fill="#fbbf24"/>
<text x="120" y="140" text-anchor="middle" fill="#fbbf24" font-size="7" {FT}>ancestor</text>
<g stroke="#22c55e" stroke-width="2" fill="none">
<line x1="120" y1="120" x2="35" y2="60"/>
<line x1="120" y1="120" x2="70" y2="40"/>
<line x1="120" y1="120" x2="100" y2="35"/>
<line x1="120" y1="120" x2="140" y2="35"/>
<line x1="120" y1="120" x2="170" y2="40"/>
<line x1="120" y1="120" x2="205" y2="60"/>
</g>
<path d="M30 55 Q32 52 38 55 Q40 60 35 62 Z" fill="#86efac"/>
<text x="33" y="72" text-anchor="middle" fill="#86efac" font-size="6" {FT}>seed</text>
<path d="M65 35 Q70 32 75 40 Q72 45 65 42 Z" fill="#86efac"/>
<text x="70" y="52" text-anchor="middle" fill="#86efac" font-size="6" {FT}>insect</text>
<path d="M95 30 Q100 28 103 35 Q101 38 95 36 Z" fill="#86efac"/>
<text x="99" y="48" text-anchor="middle" fill="#86efac" font-size="6" {FT}>cactus</text>
<path d="M137 30 Q142 26 145 33 Q144 38 138 36 Z" fill="#86efac"/>
<text x="141" y="48" text-anchor="middle" fill="#86efac" font-size="6" {FT}>nectar</text>
<path d="M167 35 Q173 33 175 40 Q172 44 167 43 Z" fill="#86efac"/>
<text x="171" y="52" text-anchor="middle" fill="#86efac" font-size="6" {FT}>warbler</text>
<path d="M202 55 Q208 52 210 60 Q206 63 202 62 Z" fill="#86efac"/>
<text x="206" y="72" text-anchor="middle" fill="#86efac" font-size="6" {FT}>fruit</text>
<text x="120" y="108" text-anchor="middle" fill="#fbbf24" font-size="8" font-weight="700" {FT}>One ancestor → many niches</text>
''')

W("wallace_line", T("WALLACE LINE") + f'''
<rect x="15" y="35" width="100" height="90" fill="#14532d" opacity="0.5"/>
<text x="65" y="55" text-anchor="middle" fill="#86efac" font-size="9" font-weight="700" {FT}>Asia</text>
<text x="65" y="75" text-anchor="middle" fill="#86efac" font-size="8" {FT}>🐅 Tigers</text>
<text x="65" y="88" text-anchor="middle" fill="#86efac" font-size="8" {FT}>🐒 Monkeys</text>
<text x="65" y="101" text-anchor="middle" fill="#86efac" font-size="8" {FT}>🐘 Elephants</text>
<text x="65" y="115" text-anchor="middle" fill="#86efac" font-size="7" {FT}>placentals</text>
<line x1="118" y1="30" x2="118" y2="130" stroke="#ef4444" stroke-width="3" stroke-dasharray="4,3"/>
<text x="118" y="22" text-anchor="middle" fill="#ef4444" font-size="9" font-weight="700" {FT}>WALLACE</text>
<text x="118" y="142" text-anchor="middle" fill="#ef4444" font-size="8" font-weight="700" {FT}>Bali ↔ Lombok</text>
<rect x="125" y="35" width="100" height="90" fill="#92400e" opacity="0.5"/>
<text x="175" y="55" text-anchor="middle" fill="#fde68a" font-size="9" font-weight="700" {FT}>Australia</text>
<text x="175" y="75" text-anchor="middle" fill="#fde68a" font-size="8" {FT}>🦘 Kangaroos</text>
<text x="175" y="88" text-anchor="middle" fill="#fde68a" font-size="8" {FT}>🐨 Koalas</text>
<text x="175" y="101" text-anchor="middle" fill="#fde68a" font-size="8" {FT}>🦜 Cockatoos</text>
<text x="175" y="115" text-anchor="middle" fill="#fde68a" font-size="7" {FT}>marsupials</text>
''')

W("species_area", T("SPECIES-AREA RELATIONSHIP") + S("S = c·A^z (power law)") + f'''
<line x1="30" y1="40" x2="30" y2="125" stroke="#475569"/>
<line x1="30" y1="125" x2="220" y2="125" stroke="#475569"/>
<text x="15" y="45" fill="#94a3b8" font-size="7" {FT}>log S</text>
<text x="215" y="140" fill="#94a3b8" font-size="7" {FT}>log A</text>
<polyline points="30,115 70,95 120,70 170,50 210,35" stroke="#fbbf24" stroke-width="2.5" fill="none"/>
<circle cx="70" cy="95" r="3" fill="#fbbf24"/>
<circle cx="120" cy="70" r="3" fill="#fbbf24"/>
<circle cx="170" cy="50" r="3" fill="#fbbf24"/>
<text x="120" y="148" text-anchor="middle" fill="#64748b" font-size="7" {FT}>Doubling area ≈ doubles species</text>
''')

W("standing_diversity", T("STANDING DIVERSITY EQUATION") + f'''
<rect x="20" y="40" width="200" height="50" fill="#111" stroke="#334155" rx="4"/>
<text x="120" y="62" text-anchor="middle" fill="#fbbf24" font-size="14" font-weight="700" {FT}>D₂ = D₁ + O − E</text>
<text x="120" y="80" text-anchor="middle" fill="#94a3b8" font-size="8" {FT}>future = current + originations − extinctions</text>
<rect x="20" y="100" width="60" height="35" fill="#1e3a5f" stroke="#60a5fa" rx="3"/>
<text x="50" y="115" text-anchor="middle" fill="#93c5fd" font-size="8" font-weight="700" {FT}>D₁ current</text>
<text x="50" y="127" text-anchor="middle" fill="#94a3b8" font-size="7" {FT}>baseline</text>
<rect x="90" y="100" width="60" height="35" fill="#14532d" stroke="#22c55e" rx="3"/>
<text x="120" y="115" text-anchor="middle" fill="#86efac" font-size="8" font-weight="700" {FT}>+ O spec.</text>
<text x="120" y="127" text-anchor="middle" fill="#94a3b8" font-size="7" {FT}>new species</text>
<rect x="160" y="100" width="60" height="35" fill="#3b1515" stroke="#ef4444" rx="3"/>
<text x="190" y="115" text-anchor="middle" fill="#fca5a5" font-size="8" font-weight="700" {FT}>− E ext.</text>
<text x="190" y="127" text-anchor="middle" fill="#94a3b8" font-size="7" {FT}>lost species</text>
''')

W("big5", T("BIG 5 MASS EXTINCTIONS") + f'''
<line x1="20" y1="120" x2="225" y2="120" stroke="#475569"/>
<line x1="20" y1="35" x2="20" y2="120" stroke="#475569"/>
<polyline points="20,110 40,105 55,60 70,100 90,105 110,70 135,105 155,30 175,100 195,50 220,105" stroke="#ef4444" stroke-width="1.5" fill="none"/>
<rect x="52" y="60" width="6" height="60" fill="#ef4444"/>
<text x="55" y="50" text-anchor="middle" fill="#fca5a5" font-size="6" font-weight="700" {FT}>86%</text>
<text x="55" y="135" text-anchor="middle" fill="#fca5a5" font-size="6" {FT}>Ord</text>
<rect x="107" y="70" width="6" height="50" fill="#ef4444"/>
<text x="110" y="62" text-anchor="middle" fill="#fca5a5" font-size="6" {FT}>75%</text>
<text x="110" y="135" text-anchor="middle" fill="#fca5a5" font-size="6" {FT}>Dev</text>
<rect x="152" y="30" width="6" height="90" fill="#dc2626"/>
<text x="155" y="25" text-anchor="middle" fill="#fbbf24" font-size="7" font-weight="700" {FT}>96%★</text>
<text x="155" y="135" text-anchor="middle" fill="#fbbf24" font-size="6" font-weight="700" {FT}>Perm</text>
<rect x="172" y="70" width="6" height="50" fill="#ef4444"/>
<text x="175" y="62" text-anchor="middle" fill="#fca5a5" font-size="6" {FT}>80%</text>
<text x="175" y="135" text-anchor="middle" fill="#fca5a5" font-size="6" {FT}>Tri</text>
<rect x="192" y="50" width="6" height="70" fill="#ef4444"/>
<text x="195" y="44" text-anchor="middle" fill="#fca5a5" font-size="6" {FT}>76%</text>
<text x="195" y="135" text-anchor="middle" fill="#fca5a5" font-size="6" {FT}>K-Pg</text>
''')

W("metapopulation", T("METAPOPULATION DYNAMICS") + f'''
<circle cx="55" cy="60" r="15" fill="#22c55e"/>
<circle cx="105" cy="45" r="12" fill="#64748b"/>
<circle cx="155" cy="65" r="14" fill="#22c55e"/>
<circle cx="195" cy="55" r="10" fill="#22c55e"/>
<circle cx="75" cy="100" r="12" fill="#64748b"/>
<circle cx="130" cy="110" r="14" fill="#22c55e"/>
<circle cx="185" cy="105" r="11" fill="#22c55e"/>
<line x1="65" y1="65" x2="95" y2="52" stroke="#fbbf24" stroke-width="1" stroke-dasharray="2,2"/>
<line x1="115" y1="50" x2="145" y2="60" stroke="#fbbf24" stroke-width="1" stroke-dasharray="2,2"/>
<line x1="165" y1="68" x2="188" y2="60" stroke="#fbbf24" stroke-width="1" stroke-dasharray="2,2"/>
<line x1="60" y1="72" x2="70" y2="90" stroke="#fbbf24" stroke-width="1" stroke-dasharray="2,2"/>
<line x1="85" y1="100" x2="115" y2="108" stroke="#fbbf24" stroke-width="1" stroke-dasharray="2,2"/>
<line x1="145" y1="108" x2="175" y2="105" stroke="#fbbf24" stroke-width="1" stroke-dasharray="2,2"/>
<circle cx="215" cy="30" r="4" fill="#22c55e"/>
<text x="222" y="33" fill="#86efac" font-size="7" {FT}>occupied</text>
<circle cx="215" cy="43" r="4" fill="#64748b"/>
<text x="222" y="46" fill="#94a3b8" font-size="7" {FT}>empty</text>
<text x="120" y="135" text-anchor="middle" fill="#fbbf24" font-size="8" font-weight="700" {FT}>Patches turn over · system persists</text>
<text x="120" y="147" text-anchor="middle" fill="#64748b" font-size="7" {FT}>Migration rescues empty patches</text>
''')

W("gondwana_laurasia", T("GONDWANA vs LAURASIA") + f'''
<rect x="15" y="35" width="210" height="50" fill="#1e3a5f" opacity="0.5"/>
<text x="120" y="48" text-anchor="middle" fill="#93c5fd" font-size="9" font-weight="700" {FT}>LAURASIA (North)</text>
<text x="50" y="65" fill="#86efac" font-size="7" {FT}>🐎 Placental mammals</text>
<text x="50" y="76" fill="#86efac" font-size="7" {FT}>🌲 Conifers</text>
<text x="160" y="65" fill="#86efac" font-size="7" {FT}>🐻 Ursids</text>
<text x="160" y="76" fill="#86efac" font-size="7" {FT}>🦊 Canids</text>
<rect x="15" y="87" width="210" height="50" fill="#92400e" opacity="0.5"/>
<text x="120" y="100" text-anchor="middle" fill="#fde68a" font-size="9" font-weight="700" {FT}>GONDWANA (South)</text>
<text x="30" y="115" fill="#fbbf24" font-size="7" {FT}>🦘 Marsupials</text>
<text x="30" y="126" fill="#fbbf24" font-size="7" {FT}>🦥 Sloths</text>
<text x="140" y="115" fill="#fbbf24" font-size="7" {FT}>🦆 Ratites</text>
<text x="140" y="126" fill="#fbbf24" font-size="7" {FT}>🌴 Proteaceae</text>
''')

W("vicariance_vs_dispersal", T("VICARIANCE vs DISPERSAL") + f'''
<rect x="10" y="30" width="108" height="110" fill="#0f172a" stroke="#60a5fa" rx="3"/>
<text x="64" y="44" text-anchor="middle" fill="#60a5fa" font-size="8" font-weight="700" {FT}>VICARIANCE</text>
<ellipse cx="40" cy="75" rx="20" ry="12" fill="#14532d"/>
<ellipse cx="88" cy="75" rx="20" ry="12" fill="#14532d"/>
<line x1="62" y1="55" x2="62" y2="95" stroke="#ef4444" stroke-width="2" stroke-dasharray="3,2"/>
<circle cx="40" cy="75" r="3" fill="#fbbf24"/>
<circle cx="88" cy="75" r="3" fill="#fbbf24"/>
<text x="64" y="112" text-anchor="middle" fill="#94a3b8" font-size="7" font-weight="700" {FT}>Land moves</text>
<text x="64" y="123" text-anchor="middle" fill="#94a3b8" font-size="7" {FT}>Organisms stay</text>
<rect x="122" y="30" width="108" height="110" fill="#0f172a" stroke="#22c55e" rx="3"/>
<text x="176" y="44" text-anchor="middle" fill="#22c55e" font-size="8" font-weight="700" {FT}>DISPERSAL</text>
<ellipse cx="145" cy="75" rx="15" ry="10" fill="#14532d"/>
<rect x="165" y="65" width="20" height="20" fill="#1e40af" opacity="0.6"/>
<ellipse cx="210" cy="75" rx="15" ry="10" fill="#14532d"/>
<path d="M155 65 Q175 55 200 70" stroke="#fbbf24" stroke-width="1.5" fill="none" stroke-dasharray="2,2"/>
<polygon points="200,70 196,66 196,74" fill="#fbbf24"/>
<circle cx="205" cy="73" r="3" fill="#fbbf24"/>
<text x="176" y="112" text-anchor="middle" fill="#94a3b8" font-size="7" font-weight="700" {FT}>Organisms move</text>
<text x="176" y="123" text-anchor="middle" fill="#94a3b8" font-size="7" {FT}>Land stays</text>
''')

W("endemism", T("ENDEMISM") + S('"Found ONLY here"') + f'''
<ellipse cx="120" cy="85" rx="70" ry="40" fill="#14532d" stroke="#22c55e"/>
<text x="120" y="52" text-anchor="middle" fill="#86efac" font-size="9" font-weight="700" {FT}>Island</text>
<circle cx="90" cy="78" r="5" fill="#fbbf24"/>
<circle cx="110" cy="90" r="5" fill="#fbbf24"/>
<circle cx="135" cy="80" r="5" fill="#fbbf24"/>
<circle cx="150" cy="95" r="5" fill="#fbbf24"/>
<circle cx="105" cy="105" r="5" fill="#fbbf24"/>
<text x="120" y="135" text-anchor="middle" fill="#fbbf24" font-size="8" font-weight="700" {FT}>★ Species found nowhere else on Earth</text>
<text x="120" y="146" text-anchor="middle" fill="#94a3b8" font-size="7" {FT}>Islands · mountaintops · isolated habitats</text>
''')

W("taxon_cycle", T("TAXON CYCLE") + f'''
<circle cx="120" cy="80" r="55" fill="none" stroke="#475569" stroke-width="1.5" stroke-dasharray="3,2"/>
<circle cx="120" cy="25" r="12" fill="#22c55e"/>
<text x="120" y="28" text-anchor="middle" fill="#fff" font-size="7" {FT}>1. Coloni</text>
<circle cx="175" cy="80" r="12" fill="#60a5fa"/>
<text x="175" y="83" text-anchor="middle" fill="#fff" font-size="7" {FT}>2. Expand</text>
<circle cx="120" cy="135" r="12" fill="#d97706"/>
<text x="120" y="138" text-anchor="middle" fill="#fff" font-size="7" {FT}>3. Contract</text>
<circle cx="65" cy="80" r="12" fill="#ef4444"/>
<text x="65" y="83" text-anchor="middle" fill="#fff" font-size="7" {FT}>4. Extinct</text>
<polygon points="150,55 148,52 144,54" fill="#475569"/>
<polygon points="150,105 146,108 148,111" fill="#475569"/>
<polygon points="90,105 92,108 95,106" fill="#475569"/>
<polygon points="90,55 94,52 95,55" fill="#475569"/>
''')

W("great_american_interchange", T("GREAT AMERICAN INTERCHANGE") + f'''
<ellipse cx="65" cy="55" rx="22" ry="18" fill="#2563eb"/>
<text x="65" y="58" text-anchor="middle" fill="#fff" font-size="8" font-weight="700" {FT}>N.America</text>
<rect x="82" y="70" width="16" height="25" fill="#0891b2"/>
<text x="120" y="85" text-anchor="middle" fill="#fbbf24" font-size="7" font-weight="700" {FT}>Panama</text>
<text x="120" y="95" text-anchor="middle" fill="#fbbf24" font-size="7" {FT}>~3 mya</text>
<rect x="92" y="85" width="16" height="25" fill="#0891b2"/>
<rect x="82" y="100" width="16" height="25" fill="#0891b2"/>
<ellipse cx="65" cy="120" rx="22" ry="18" fill="#d97706"/>
<text x="65" y="123" text-anchor="middle" fill="#fff" font-size="8" font-weight="700" {FT}>S.America</text>
<path d="M75 68 Q80 95 75 105" stroke="#22c55e" stroke-width="2" fill="none" stroke-dasharray="3,2"/>
<polygon points="75,105 71,101 71,108" fill="#22c55e"/>
<text x="105" y="75" fill="#86efac" font-size="6" font-weight="700" {FT}>cats→</text>
<path d="M95 108 Q90 85 95 72" stroke="#a78bfa" stroke-width="2" fill="none" stroke-dasharray="3,2"/>
<polygon points="95,72 99,76 99,69" fill="#a78bfa"/>
<text x="100" y="112" fill="#c4b5fd" font-size="6" font-weight="700" {FT}>opossums←</text>
<text x="165" y="75" fill="#94a3b8" font-size="8" {FT}>Land bridge</text>
<text x="165" y="88" fill="#94a3b8" font-size="8" {FT}>closed →</text>
<text x="165" y="101" fill="#94a3b8" font-size="8" {FT}>biotic</text>
<text x="165" y="114" fill="#94a3b8" font-size="8" {FT}>mixing</text>
''')

W("darwin_finches", T("DARWIN'S FINCHES") + S("Galápagos adaptive radiation") + f'''
<circle cx="120" cy="125" r="6" fill="#fbbf24"/>
<text x="120" y="140" text-anchor="middle" fill="#fbbf24" font-size="7" {FT}>ancestor</text>
<g stroke="#86efac" stroke-width="1" fill="none">
<line x1="120" y1="122" x2="35" y2="70"/>
<line x1="120" y1="122" x2="65" y2="50"/>
<line x1="120" y1="122" x2="100" y2="42"/>
<line x1="120" y1="122" x2="140" y2="42"/>
<line x1="120" y1="122" x2="175" y2="50"/>
<line x1="120" y1="122" x2="205" y2="70"/>
</g>
<circle cx="30" cy="65" r="5" fill="#57534e"/>
<polygon points="25,65 15,68 25,68" fill="#fbbf24"/>
<text x="30" y="82" text-anchor="middle" fill="#86efac" font-size="6" {FT}>seed crusher</text>
<circle cx="60" cy="45" r="5" fill="#57534e"/>
<polygon points="55,45 48,48 55,48" fill="#fbbf24"/>
<text x="60" y="62" text-anchor="middle" fill="#86efac" font-size="6" {FT}>medium seed</text>
<circle cx="95" cy="37" r="5" fill="#57534e"/>
<polygon points="90,37 84,40 90,38" fill="#fbbf24"/>
<text x="95" y="54" text-anchor="middle" fill="#86efac" font-size="6" {FT}>insect</text>
<circle cx="140" cy="37" r="5" fill="#57534e"/>
<polygon points="145,37 153,38 146,40" fill="#fbbf24"/>
<text x="140" y="54" text-anchor="middle" fill="#86efac" font-size="6" {FT}>cactus</text>
<circle cx="175" cy="45" r="5" fill="#57534e"/>
<polygon points="180,45 188,47 180,48" fill="#fbbf24"/>
<text x="175" y="62" text-anchor="middle" fill="#86efac" font-size="6" {FT}>nectar</text>
<circle cx="208" cy="65" r="5" fill="#57534e"/>
<polygon points="213,65 220,66 213,68" fill="#fbbf24"/>
<text x="208" y="82" text-anchor="middle" fill="#86efac" font-size="6" {FT}>warbler</text>
<text x="120" y="110" text-anchor="middle" fill="#fbbf24" font-size="7" font-weight="700" {FT}>Different beaks · different foods</text>
''')

W("cichlid_radiation", T("EAST AFRICAN CICHLIDS") + f'''
<ellipse cx="60" cy="55" rx="22" ry="12" fill="#1e40af"/>
<text x="60" y="58" text-anchor="middle" fill="#bfdbfe" font-size="7" font-weight="700" {FT}>Tanganyika</text>
<text x="60" y="80" text-anchor="middle" fill="#94a3b8" font-size="6" {FT}>~250 spp</text>
<ellipse cx="135" cy="55" rx="22" ry="12" fill="#1e40af"/>
<text x="135" y="58" text-anchor="middle" fill="#bfdbfe" font-size="7" font-weight="700" {FT}>Victoria</text>
<text x="135" y="80" text-anchor="middle" fill="#94a3b8" font-size="6" {FT}>~500 spp</text>
<ellipse cx="205" cy="55" rx="22" ry="12" fill="#1e40af"/>
<text x="205" y="58" text-anchor="middle" fill="#bfdbfe" font-size="7" font-weight="700" {FT}>Malawi</text>
<text x="205" y="80" text-anchor="middle" fill="#94a3b8" font-size="6" {FT}>~1000 spp</text>
<g>
<ellipse cx="45" cy="100" rx="10" ry="3" fill="#fbbf24"/>
<ellipse cx="70" cy="105" rx="10" ry="3" fill="#22c55e"/>
<ellipse cx="125" cy="100" rx="10" ry="3" fill="#a78bfa"/>
<ellipse cx="150" cy="105" rx="10" ry="3" fill="#ef4444"/>
<ellipse cx="195" cy="100" rx="10" ry="3" fill="#60a5fa"/>
<ellipse cx="220" cy="105" rx="10" ry="3" fill="#d97706"/>
</g>
<text x="120" y="125" text-anchor="middle" fill="#fbbf24" font-size="8" font-weight="700" {FT}>Parallel radiations in 3 lakes</text>
<text x="120" y="140" text-anchor="middle" fill="#94a3b8" font-size="7" {FT}>Lakes act like islands</text>
''')

W("sloss_debate", T("SLOSS: Single Large Or Several Small?") + f'''
<rect x="20" y="45" width="80" height="55" fill="#14532d" stroke="#22c55e" rx="3"/>
<text x="60" y="78" text-anchor="middle" fill="#86efac" font-size="8" font-weight="700" {FT}>SINGLE LARGE</text>
<text x="60" y="115" text-anchor="middle" fill="#94a3b8" font-size="7" {FT}>More species/area</text>
<text x="60" y="125" text-anchor="middle" fill="#94a3b8" font-size="7" {FT}>Area-sensitive spp</text>
<text x="108" y="80" fill="#fbbf24" font-size="12" font-weight="700" {FT}>vs</text>
<g stroke="#22c55e" fill="#14532d">
<rect x="130" y="45" width="20" height="18" rx="2"/>
<rect x="155" y="45" width="20" height="18" rx="2"/>
<rect x="180" y="45" width="20" height="18" rx="2"/>
<rect x="205" y="45" width="20" height="18" rx="2"/>
<rect x="130" y="72" width="20" height="18" rx="2"/>
<rect x="155" y="72" width="20" height="18" rx="2"/>
<rect x="180" y="72" width="20" height="18" rx="2"/>
<rect x="205" y="72" width="20" height="18" rx="2"/>
</g>
<text x="177" y="115" text-anchor="middle" fill="#94a3b8" font-size="7" {FT}>SEVERAL SMALL</text>
<text x="177" y="127" text-anchor="middle" fill="#94a3b8" font-size="7" {FT}>Risk spread · β diversity</text>
<text x="120" y="145" text-anchor="middle" fill="#64748b" font-size="7" {FT}>Context-dependent — not one-size-fits-all</text>
''')

W("area_phylogeny", T("AREA PHYLOGENY") + f'''
<text x="60" y="32" text-anchor="middle" fill="#86efac" font-size="8" font-weight="700" {FT}>Organism tree</text>
<line x1="20" y1="80" x2="45" y2="80" stroke="#22c55e" stroke-width="2"/>
<line x1="45" y1="80" x2="45" y2="55" stroke="#22c55e" stroke-width="2"/>
<line x1="45" y1="80" x2="45" y2="105" stroke="#22c55e" stroke-width="2"/>
<line x1="45" y1="55" x2="100" y2="45" stroke="#22c55e" stroke-width="2"/>
<line x1="45" y1="55" x2="100" y2="65" stroke="#22c55e" stroke-width="2"/>
<line x1="45" y1="105" x2="100" y2="105" stroke="#22c55e" stroke-width="2"/>
<text x="105" y="48" fill="#86efac" font-size="8" {FT}>A</text>
<text x="105" y="68" fill="#86efac" font-size="8" {FT}>B</text>
<text x="105" y="108" fill="#86efac" font-size="8" {FT}>C</text>
<text x="180" y="32" text-anchor="middle" fill="#fbbf24" font-size="8" font-weight="700" {FT}>Area tree</text>
<line x1="140" y1="80" x2="165" y2="80" stroke="#fbbf24" stroke-width="2"/>
<line x1="165" y1="80" x2="165" y2="55" stroke="#fbbf24" stroke-width="2"/>
<line x1="165" y1="80" x2="165" y2="105" stroke="#fbbf24" stroke-width="2"/>
<line x1="165" y1="55" x2="220" y2="45" stroke="#fbbf24" stroke-width="2"/>
<line x1="165" y1="55" x2="220" y2="65" stroke="#fbbf24" stroke-width="2"/>
<line x1="165" y1="105" x2="220" y2="105" stroke="#fbbf24" stroke-width="2"/>
<text x="225" y="48" fill="#fde68a" font-size="8" {FT}>Area X</text>
<text x="225" y="68" fill="#fde68a" font-size="8" {FT}>Area Y</text>
<text x="225" y="108" fill="#fde68a" font-size="8" {FT}>Area Z</text>
<text x="120" y="130" text-anchor="middle" fill="#22c55e" font-size="8" font-weight="700" {FT}>Matching topologies → vicariance</text>
<text x="120" y="143" text-anchor="middle" fill="#94a3b8" font-size="7" {FT}>Test by tree congruence</text>
''')

print(f"Groups C+D done. Total SVGs: {len([f for f in os.listdir(OUT) if f.startswith('svg_')])}")
