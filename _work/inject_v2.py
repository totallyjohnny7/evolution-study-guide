"""Inject v2 schema into both HTML files.

Performs three surgical splices on each HTML file:

  1. Add v2-* CSS rules into the existing <style> block
  2. Replace the JSON blob inside <script id="sd"> with new data.json
  3. Inject rV2() renderer function and patch rMap to call it when n.v2 exists

Source of truth:  C:/Users/johnn/Desktop/evolution-study-guide/data.json
Targets:          public/index_prod.html  +  public/index.html

Idempotent: re-running just refreshes the splices using the latest data.json
and current rV2 source defined in this file.
"""
import json
import os
import re
import sys
import io

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT  = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA  = os.path.join(ROOT, 'data.json')
HTMLS = [
    os.path.join(ROOT, 'public', 'index_prod.html'),
    os.path.join(ROOT, 'public', 'index.html'),
]

# ---------- 1. CSS to inject (Georgia serif, dark mode, theme #0d1117) -----
V2_CSS = (
    "/*v2-start*/"
    ".v2-meta{padding:.55rem 1.1rem;font-size:.72rem;color:#7d8590;background:#0d1117;letter-spacing:.05em;border-bottom:1px solid #21262d;font-family:Georgia,serif}"
    ".v2-meta-lec{color:#e0a85c;font-weight:700}"
    ".v2-meta-title{color:#e0a85c}"
    ".v2-meta-ch{color:#7d8590}"
    ".v2-meta-slides{color:#7d8590}"
    ".v2-header{padding:1rem 1.2rem .7rem;background:#161b22}"
    ".v2-header h2{margin:0;font-family:Georgia,serif;color:#e6edf3;font-size:1.45rem;line-height:1.25;font-weight:700}"
    ".v2-body{padding:1rem 1.2rem 1.4rem;background:#161b22;font-family:Georgia,serif}"
    ".v2-slot{margin-bottom:1.15rem}"
    ".v2-slot:last-child{margin-bottom:0}"
    ".v2-label{font-size:.68rem;font-weight:700;letter-spacing:.12em;color:#e0a85c;margin-bottom:.45rem;text-transform:uppercase;font-family:Georgia,serif}"
    ".v2-trap-label{color:#f0934f}"
    ".v2-def-text{font-size:1.02rem;line-height:1.55;color:#e6edf3;padding:.65rem .85rem;background:#0d1117;border-left:3px solid #e0a85c;border-radius:0 4px 4px 0}"
    ".v2-terms-grid{display:grid;grid-template-columns:1fr 1fr;gap:.5rem}"
    ".v2-term{padding:.55rem .75rem;border-radius:0 4px 4px 0}"
    ".v2-term-name{font-weight:700;font-size:.86rem;color:#e6edf3;margin-bottom:.2rem;font-family:Georgia,serif}"
    ".v2-term-def{font-size:.78rem;color:#c8d1d9;line-height:1.35;font-family:Georgia,serif}"
    ".v2-mnemonic{padding:.7rem .9rem;background:#0d1117;border-left:3px solid #e0a85c;border-radius:0 4px 4px 0}"
    ".v2-mn-hook{font-style:italic;color:#e0a85c;font-size:1.02rem;font-weight:700;margin-bottom:.4rem;font-family:Georgia,serif}"
    ".v2-mn-exp{color:#c8d1d9;font-size:.88rem;line-height:1.45;font-family:Georgia,serif}"
    ".v2-trap{padding:.7rem .9rem;background:#1f1208;border:1px solid #d4641e;border-radius:4px}"
    ".v2-trap-text{color:#e6edf3;font-size:.88rem;line-height:1.5;font-family:Georgia,serif}"
    ".v2-quiz,.v2-flashcard{padding:.6rem .85rem;background:#0d1117;border-radius:4px;margin-bottom:.5rem;border-left:3px solid #4e6e8e}"
    ".v2-flashcard{border-left-color:#5ec5b8}"
    ".v2-mini-label{font-size:.62rem;font-weight:700;letter-spacing:.1em;color:#7d8590;margin-bottom:.32rem;text-transform:uppercase;font-family:Georgia,serif}"
    ".v2-quiz-text{color:#e6edf3;font-size:.9rem;font-style:italic;font-family:Georgia,serif}"
    ".v2-fc-front{color:#e6edf3;font-size:.9rem;font-weight:700;margin-bottom:.32rem;font-family:Georgia,serif}"
    ".v2-fc-back{color:#c8d1d9;font-size:.85rem;padding-top:.32rem;border-top:1px dashed #30363d;font-family:Georgia,serif}"
    "@media(max-width:600px){.v2-terms-grid{grid-template-columns:1fr}}"
    "/*v2-end*/"
)

# ---------- 2. rV2 renderer source (single line, minified-friendly) --------
# Reads n.v2 + top-level lecture/lectureTitle/chapter/slideRange.
# Uses the existing el() helper and NC color map already defined in the app.
RV2_FN = (
    "function rV2(ct,n){"
    "var v=n.v2;"
    "var nc=NC[n.color]||NC.gray;"
    "var panel=el('div',{className:'popup-panel v2-panel'});"
    # Metadata bar
    "var meta=el('div',{className:'v2-meta'});"
    "meta.appendChild(el('span',{className:'v2-meta-lec'},'LEC '+n.lecture));"
    "meta.appendChild(document.createTextNode(' \\u00b7 '));"
    "meta.appendChild(el('span',{className:'v2-meta-title'},n.lectureTitle));"
    "meta.appendChild(document.createTextNode(' \\u00b7 '));"
    "meta.appendChild(el('span',{className:'v2-meta-ch'},n.chapter));"
    "meta.appendChild(document.createTextNode(' \\u00b7 slides '));"
    "meta.appendChild(el('span',{className:'v2-meta-slides'},n.slideRange));"
    "panel.appendChild(meta);"
    # Header (title)
    "var ph=el('div',{className:'popup-header v2-header',style:{borderLeft:'4px solid '+nc.bdr}});"
    "ph.appendChild(el('h2',{},n.title));"
    "panel.appendChild(ph);"
    # Body
    "var pb=el('div',{className:'popup-body v2-body'});"
    # Slot 1: Definition
    "var def=el('div',{className:'v2-slot'});"
    "def.appendChild(el('div',{className:'v2-label'},'\\u25c6 DEFINITION'));"
    "def.appendChild(el('div',{className:'v2-def-text'},v.definition));"
    "pb.appendChild(def);"
    # Slot 2: Key terms grid
    "var kt=el('div',{className:'v2-slot'});"
    "kt.appendChild(el('div',{className:'v2-label'},'\\u25c6 KEY TERMS'));"
    "var ktg=el('div',{className:'v2-terms-grid'});"
    "v.keyTerms.forEach(function(t){"
        "var col=NC[t.color]||NC.gray;"
        "var card=el('div',{className:'v2-term',style:{borderLeft:'3px solid '+col.bdr,background:col.bg}});"
        "card.appendChild(el('div',{className:'v2-term-name'},t.term));"
        "card.appendChild(el('div',{className:'v2-term-def'},t.def));"
        "ktg.appendChild(card);"
    "});"
    "kt.appendChild(ktg);"
    "pb.appendChild(kt);"
    # Slot 3: Mnemonic
    "var mn=el('div',{className:'v2-slot'});"
    "mn.appendChild(el('div',{className:'v2-label'},'\\u25c6 MNEMONIC'));"
    "var mb=el('div',{className:'v2-mnemonic'});"
    "mb.appendChild(el('div',{className:'v2-mn-hook'},v.mnemonic.hook));"
    "mb.appendChild(el('div',{className:'v2-mn-exp'},v.mnemonic.explanation));"
    "mn.appendChild(mb);"
    "pb.appendChild(mn);"
    # Slot 4: Exam trap
    "var et=el('div',{className:'v2-slot'});"
    "et.appendChild(el('div',{className:'v2-label v2-trap-label'},'\\u25b2 EXAM TRAP'));"
    "var etb=el('div',{className:'v2-trap'});"
    "etb.appendChild(el('div',{className:'v2-trap-text'},v.examTrap));"
    "et.appendChild(etb);"
    "pb.appendChild(et);"
    # Slot 5: Actions (quiz + flashcard)
    "var ac=el('div',{className:'v2-slot'});"
    "ac.appendChild(el('div',{className:'v2-label'},'\\u2713 PRACTICE'));"
    "var qz=el('div',{className:'v2-quiz'});"
    "qz.appendChild(el('div',{className:'v2-mini-label'},'Quiz prompt'));"
    "qz.appendChild(el('div',{className:'v2-quiz-text'},v.actions.quizPrompt));"
    "ac.appendChild(qz);"
    "var fc=el('div',{className:'v2-flashcard'});"
    "fc.appendChild(el('div',{className:'v2-mini-label'},'Flashcard'));"
    "fc.appendChild(el('div',{className:'v2-fc-front'},v.actions.flashcardFront));"
    "fc.appendChild(el('div',{className:'v2-fc-back'},v.actions.flashcardBack));"
    "ac.appendChild(fc);"
    "pb.appendChild(ac);"
    # Mount
    "panel.appendChild(pb);"
    "ct.appendChild(panel);"
    "}"
)

# ---------- splice helpers -----------------------------------------------

def splice_css(html):
    """Insert v2-* CSS rules just before </style>. Idempotent."""
    # Remove any prior v2 CSS block
    html = re.sub(r'/\*v2-start\*/.*?/\*v2-end\*/', '', html, flags=re.DOTALL)
    # Add fresh block before </style>
    return html.replace('</style>', V2_CSS + '</style>', 1)


def splice_json(html, blob):
    """Replace contents of <script id="sd" type="application/json">...</script>."""
    pat = r'(<script id="sd" type="application/json">)(.*?)(</script>)'
    return re.sub(
        pat,
        lambda m: m.group(1) + blob + m.group(3),
        html, count=1, flags=re.DOTALL,
    )


def splice_renderer(html):
    """Inject rV2 function and patch rMap to call it. Idempotent."""
    # Step A: remove any prior rV2 definition (to keep idempotent)
    html = re.sub(r'function rV2\(ct,n\)\{.*?\}\}\}\}\}\}\}\}\}\}\}\}', '', html, flags=re.DOTALL)
    html = re.sub(r'function rV2\(ct,n\)\{.*?ct\.appendChild\(panel\);\}',
                  '', html, flags=re.DOTALL)

    # Step B: inject rV2 immediately before "function rMap("
    if 'function rV2(ct,n)' not in html:
        html = html.replace('function rMap(', RV2_FN + 'function rMap(', 1)

    # Step C: patch rMap to call rV2 when n.v2 exists. Idempotent.
    needle  = "function rMap(ct){var n=D.nodes[S.sel];if(!n){ct.appendChild(el('div',{className:'empty'},'Select a concept from the sidebar'));return;}"
    patched = needle + "if(n.v2){return rV2(ct,n);}"
    if patched not in html:
        html = html.replace(needle, patched, 1)
    return html


# ---------- main ---------------------------------------------------------

def main():
    with open(DATA, 'r', encoding='utf-8') as f:
        data = json.load(f)
    blob = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
    print(f'data.json: {len(blob):,} bytes, {len(data["nodes"])} nodes')

    for path in HTMLS:
        with open(path, 'r', encoding='utf-8') as f:
            html = f.read()
        before = len(html)

        html = splice_css(html)
        html = splice_json(html, blob)
        html = splice_renderer(html)

        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        after = len(html)
        delta = after - before
        sign = '+' if delta >= 0 else ''
        print(f'  {os.path.basename(path)}: {before:,} -> {after:,} bytes ({sign}{delta:,})')

    # Quick sanity: rV2 present, JSON parses, every node has v2
    for path in HTMLS:
        with open(path, 'r', encoding='utf-8') as f:
            html = f.read()
        assert 'function rV2(ct,n)' in html, f'rV2 missing from {path}'
        assert 'if(n.v2){return rV2(ct,n);}' in html, f'rMap patch missing in {path}'
        assert '/*v2-start*/' in html and '/*v2-end*/' in html, f'CSS block missing in {path}'
        m = re.search(r'<script id="sd" type="application/json">(.*?)</script>', html, re.DOTALL)
        assert m, f'JSON blob missing in {path}'
        d = json.loads(m.group(1))
        assert len(d['nodes']) == 57, f'expected 57 nodes in {path}, got {len(d["nodes"])}'
        for n in d['nodes']:
            assert 'v2' in n, f'node {n["id"]} in {path} missing v2'
            assert 'lecture' in n and 'lectureTitle' in n
        print(f'  {os.path.basename(path)}: passed sanity (rV2, JSON parses, 57 nodes, all have v2)')

    print('Done.')


if __name__ == '__main__':
    main()
