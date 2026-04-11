"""Inject v3 schema + new tab + patched renderers into both HTML files.

This script does five surgical operations on each HTML file (idempotent):

  1. Re-splice v2 CSS block (extended with transcript, sheet, svg styles)
  2. Re-splice the JSON blob inside <script id="sd"> with the latest data.json
  3. Re-inject rV2() (now renders SVG + collapsible transcript inline)
  4. Inject rSheet() (new comprehensive single-scroll sheet view)
  5. Patch render() to add Sheet tab + dispatch
  6. Patch initC() to load 228 flashcards (4 per node × 57)
  7. Patch initQ() to load 228 quiz questions (4 per node × 57)
  8. Patch rVis() mkCard() to render v2.svg (when present)

Source of truth:  data.json
Targets:          public/index_prod.html  +  public/index.html

Re-runnable: each splice removes the prior version before adding the new one.
"""
import json
import os
import re
import sys
import io

if sys.platform == 'win32' and __name__ == '__main__':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT  = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA  = os.path.join(ROOT, 'data.json')
HTMLS = [
    os.path.join(ROOT, 'public', 'index_prod.html'),
    os.path.join(ROOT, 'public', 'index.html'),
]

# ---------- 1. CSS (v3 — extends v2) -------------------------------------
V3_CSS = (
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
    # v3 additions
    ".v2-svg-wrap{padding:1rem 1.2rem;background:#0d1117;border-top:1px solid #21262d}"
    ".v2-svg-wrap svg{max-width:100%;height:auto;display:block}"
    ".v2-transcript{margin:0;padding:.6rem 1.2rem 1.2rem;background:#0d1117;border-top:1px solid #21262d;font-family:Georgia,serif}"
    ".v2-transcript summary{cursor:pointer;color:#e0a85c;font-size:.78rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;list-style:none;padding:.45rem 0;outline:none}"
    ".v2-transcript summary::-webkit-details-marker{display:none}"
    ".v2-transcript[open] summary{margin-bottom:.55rem}"
    ".v2-trans-slide{padding:.55rem .75rem;margin-bottom:.5rem;background:#161b22;border-left:3px solid #4e6e8e;border-radius:0 4px 4px 0}"
    ".v2-trans-n{font-size:.74rem;font-weight:700;color:#e0a85c;margin-bottom:.3rem;font-family:Georgia,serif}"
    ".v2-trans-main{font-size:.82rem;color:#e6edf3;line-height:1.5;margin-bottom:.3rem;font-family:Georgia,serif;white-space:pre-wrap}"
    ".v2-trans-notes{font-size:.74rem;color:#8b949e;line-height:1.45;font-family:Georgia,serif;font-style:italic;padding-top:.3rem;border-top:1px dashed #30363d;white-space:pre-wrap}"
    # Visual tab SVG holder
    ".vis-svg{padding:.8rem;margin:.6rem 0;background:#0d1117;border-radius:6px}"
    ".vis-svg svg{max-width:100%;height:auto;display:block}"
    # Sheet tab styles
    ".sheet-wrap{padding:1rem 1.2rem;background:#161b22;font-family:Georgia,serif;max-width:980px;margin:0 auto}"
    ".sheet-intro{font-size:.85rem;color:#8b949e;margin-bottom:1.2rem;padding:.7rem .9rem;background:#0d1117;border-left:3px solid #e0a85c;border-radius:0 4px 4px 0}"
    ".sheet-lec-header{font-size:1.05rem;font-weight:700;color:#e0a85c;letter-spacing:.05em;text-transform:uppercase;margin:1.4rem 0 .7rem;padding-bottom:.4rem;border-bottom:1px solid #30363d;font-family:Georgia,serif}"
    ".sheet-lec-header:first-child{margin-top:0}"
    ".sheet-row{padding:.9rem 1rem;margin-bottom:.7rem;background:#0d1117;border-left:4px solid #e0a85c;border-radius:0 6px 6px 0;cursor:pointer;transition:background .15s}"
    ".sheet-row:hover{background:#161b22}"
    ".sheet-row-title{font-size:1rem;font-weight:700;color:#e6edf3;margin-bottom:.3rem;font-family:Georgia,serif}"
    ".sheet-row-meta{font-size:.7rem;color:#7d8590;letter-spacing:.05em;text-transform:uppercase;margin-bottom:.45rem;font-family:Georgia,serif}"
    ".sheet-row-def{font-size:.85rem;color:#c8d1d9;line-height:1.5;margin-bottom:.5rem;font-family:Georgia,serif}"
    ".sheet-row-terms{display:flex;flex-wrap:wrap;gap:.35rem;margin-top:.4rem}"
    ".sheet-pill{font-size:.7rem;padding:.2rem .5rem;background:#161b22;color:#c8d1d9;border-radius:3px;border-left:2px solid #7d8590;font-family:Georgia,serif}"
    "@media(max-width:600px){.v2-terms-grid{grid-template-columns:1fr}.sheet-wrap{padding:.7rem .8rem}}"
    "/*v2-end*/"
)

# ---------- 2. rV2 (extends with SVG + transcript) -----------------------
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
    # Header
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
    "panel.appendChild(pb);"
    # NEW Slot 6: SVG diagram
    "if(v.svg){"
        "var sv=el('div',{className:'v2-svg-wrap'});"
        "sv.innerHTML=v.svg;"
        "panel.appendChild(sv);"
    "}"
    # NEW Slot 7: Transcript (collapsible <details>)
    "if(v.transcript&&v.transcript.length){"
        "var dt=document.createElement('details');"
        "dt.className='v2-transcript';"
        "var sm=document.createElement('summary');"
        "sm.textContent='\\u25b8 LECTURE TRANSCRIPT ('+v.transcript.length+' slides)';"
        "dt.appendChild(sm);"
        "v.transcript.forEach(function(s){"
            "var row=el('div',{className:'v2-trans-slide'});"
            "row.appendChild(el('div',{className:'v2-trans-n'},'Slide '+s.n+(s.title?(': '+s.title):'')));"
            "if(s.main){row.appendChild(el('div',{className:'v2-trans-main'},s.main));}"
            "if(s.notes){row.appendChild(el('div',{className:'v2-trans-notes'},s.notes));}"
            "dt.appendChild(row);"
        "});"
        "panel.appendChild(dt);"
    "}"
    "ct.appendChild(panel);"
    "}"
)

# ---------- 3. rSheet — new tab renderer ---------------------------------
RSHEET_FN = (
    "function rSheet(ct){"
    "var wrap=el('div',{className:'sheet-wrap'});"
    "wrap.appendChild(el('div',{className:'sheet-intro'},'All 57 concepts grouped by lecture. Click any concept to open it in the Map tab. Use Ctrl+F to search.'));"
    "var byLec={};"
    "D.nodes.forEach(function(n,i){"
        "var lec=n.lecture||0;"
        "if(!byLec[lec]){byLec[lec]={title:n.lectureTitle||'',items:[]};}"
        "byLec[lec].items.push({n:n,i:i});"
    "});"
    "Object.keys(byLec).sort(function(a,b){return (+a)-(+b);}).forEach(function(lk){"
        "var grp=byLec[lk];"
        "wrap.appendChild(el('div',{className:'sheet-lec-header'},'Lec '+lk+'  \\u00b7  '+grp.title));"
        "grp.items.forEach(function(item){"
            "var n=item.n;var idx=item.i;"
            "var nc=NC[n.color]||NC.gray;"
            "var row=el('div',{className:'sheet-row',style:{borderLeftColor:nc.bdr},onClick:function(){S.sel=idx;S.mode='map';render();window.scrollTo(0,0);}});"
            "row.appendChild(el('div',{className:'sheet-row-meta'},n.chapter+'  \\u00b7  slides '+n.slideRange));"
            "row.appendChild(el('div',{className:'sheet-row-title'},n.title));"
            "if(n.v2&&n.v2.definition){"
                "row.appendChild(el('div',{className:'sheet-row-def'},n.v2.definition));"
            "}"
            "if(n.v2&&n.v2.keyTerms){"
                "var pills=el('div',{className:'sheet-row-terms'});"
                "n.v2.keyTerms.forEach(function(t){"
                    "var col=NC[t.color]||NC.gray;"
                    "pills.appendChild(el('span',{className:'sheet-pill',style:{borderLeftColor:col.bdr}},t.term));"
                "});"
                "row.appendChild(pills);"
            "}"
            "wrap.appendChild(row);"
        "});"
    "});"
    "ct.appendChild(wrap);"
    "}"
)

# ---------- 4. initC patch — load 228 flashcards across all nodes --------
INIT_C_OLD = "function initC(){var ns=D.nodes.filter(function(n){return n.flashcard&&n.flashcard.front;});S.cDk=shuf(ns);S.cI=0;S.cF=false;S.cR=[];}"
INIT_C_NEW = (
    "function initC(){"
    "var cards=[];"
    "D.nodes.forEach(function(n){"
        "var fcs=(n.v2&&n.v2.flashcards&&n.v2.flashcards.length)?n.v2.flashcards:(n.flashcard?[n.flashcard]:[]);"
        "fcs.forEach(function(c,i){"
            "cards.push({"
                "color:n.color,"
                "title:n.title+(fcs.length>1?(' ('+(i+1)+'/'+fcs.length+')'):''),"
                "flashcard:{front:c.front,back:c.back}"
            "});"
        "});"
    "});"
    "S.cDk=shuf(cards);S.cI=0;S.cF=false;S.cR=[];"
    "}"
)

# ---------- 5. initQ patch — load 228 quiz questions across all nodes ----
INIT_Q_OLD = "function initQ(){var ns=D.nodes.filter(function(n){return n.quiz&&n.quiz.question;});S.qDk=shuf(ns);S.qI=0;S.qA=false;S.qS=null;S.qSc=0;if(S.qDk.length){S.qO=shuf([S.qDk[0].quiz.correct].concat(S.qDk[0].quiz.distractors));}}"
INIT_Q_NEW = (
    "function initQ(){"
    "var qs=[];"
    "D.nodes.forEach(function(n){"
        "var quizes=(n.v2&&n.v2.quiz&&n.v2.quiz.length)?n.v2.quiz:(n.quiz?[n.quiz]:[]);"
        "quizes.forEach(function(q,i){"
            "qs.push({"
                "color:n.color,"
                "title:n.title+(quizes.length>1?(' ('+(i+1)+'/'+quizes.length+')'):''),"
                "quiz:{question:q.question,correct:q.correct,distractors:q.distractors,rationale:q.rationale||''},"
                "popup:n.popup||{}"
            "});"
        "});"
    "});"
    "S.qDk=shuf(qs);S.qI=0;S.qA=false;S.qS=null;S.qSc=0;"
    "if(S.qDk.length){S.qO=shuf([S.qDk[0].quiz.correct].concat(S.qDk[0].quiz.distractors));}"
    "}"
)

# ---------- 6. rVis mkCard patch — render v2.svg if present --------------
RVIS_OLD_PIECE = "vc.appendChild(el('div',{className:'vis-type-badge'},v.type.toUpperCase()));vc.appendChild(el('div',{className:'vis-title'},n.title));"
RVIS_NEW_PIECE = (
    "vc.appendChild(el('div',{className:'vis-type-badge'},v.type.toUpperCase()));"
    "vc.appendChild(el('div',{className:'vis-title'},n.title));"
    "if(n.v2&&n.v2.svg&&!dim){"
        "var sw=el('div',{className:'vis-svg'});"
        "sw.innerHTML=n.v2.svg;"
        "vc.appendChild(sw);"
    "}"
)

# ---------- 7. render() patch — add Sheet tab + dispatch -----------------
RENDER_TABS_OLD = "[['map','\\ud83d\\uddfa','Map'],['cards','\\ud83d\\udcd7','Cards'],['quiz','\\u270f\\ufe0f','Quiz'],['visuals','\\ud83d\\udd37','Visual']]"
RENDER_TABS_NEW = "[['map','\\ud83d\\uddfa','Map'],['cards','\\ud83d\\udcd7','Cards'],['quiz','\\u270f\\ufe0f','Quiz'],['visuals','\\ud83d\\udd37','Visual'],['sheet','\\ud83d\\udcc4','Sheet']]"
RENDER_DISPATCH_OLD = "if(S.mode==='map')rMap(ct);else if(S.mode==='cards')rCards(ct);else if(S.mode==='quiz')rQuiz(ct);else rVis(ct);"
RENDER_DISPATCH_NEW = "if(S.mode==='map')rMap(ct);else if(S.mode==='cards')rCards(ct);else if(S.mode==='quiz')rQuiz(ct);else if(S.mode==='sheet')rSheet(ct);else rVis(ct);"


# ---------- splice helpers -----------------------------------------------

def splice_css(html):
    html = re.sub(r'/\*v2-start\*/.*?/\*v2-end\*/', '', html, flags=re.DOTALL)
    return html.replace('</style>', V3_CSS + '</style>', 1)


def splice_json(html, blob):
    pat = r'(<script id="sd" type="application/json">)(.*?)(</script>)'
    return re.sub(
        pat,
        lambda m: m.group(1) + blob + m.group(3),
        html, count=1, flags=re.DOTALL,
    )


def splice_rv2(html):
    """Remove any prior rV2, then inject fresh just before rMap."""
    # Remove old rV2 (more permissive — match up to ct.appendChild(panel);})
    html = re.sub(
        r'function rV2\(ct,n\)\{.*?ct\.appendChild\(panel\);\}',
        '', html, flags=re.DOTALL
    )
    # Also remove the v3 form which appends the transcript details after panel
    # (try once more in case a previous v3 inject left a different shape)
    html = re.sub(
        r'function rV2\(ct,n\)\{var v=n\.v2;var nc=NC\[n\.color\]\|\|NC\.gray;.*?\}\}\}\}',
        '', html, flags=re.DOTALL
    )
    if 'function rV2(ct,n)' not in html:
        html = html.replace('function rMap(', RV2_FN + 'function rMap(', 1)
    # Patch rMap dispatch to call rV2 when n.v2 exists
    needle  = "function rMap(ct){var n=D.nodes[S.sel];if(!n){ct.appendChild(el('div',{className:'empty'},'Select a concept from the sidebar'));return;}"
    patched = needle + "if(n.v2){return rV2(ct,n);}"
    if patched not in html:
        html = html.replace(needle, patched, 1)
    return html


def splice_rsheet(html):
    """Remove any prior rSheet then inject fresh."""
    html = re.sub(
        r'function rSheet\(ct\)\{.*?ct\.appendChild\(wrap\);\}',
        '', html, flags=re.DOTALL
    )
    if 'function rSheet(ct)' not in html:
        # Place rSheet right before rV2 (which is right before rMap)
        if RV2_FN[:30] in html:
            html = html.replace(RV2_FN[:30], RSHEET_FN + RV2_FN[:30], 1)
        else:
            html = html.replace('function rMap(', RSHEET_FN + 'function rMap(', 1)
    return html


def splice_initc(html):
    if INIT_C_NEW in html:
        return html
    if INIT_C_OLD in html:
        return html.replace(INIT_C_OLD, INIT_C_NEW, 1)
    # Already patched with a different new version — match by leading signature
    html = re.sub(
        r'function initC\(\)\{[^}]*S\.cDk[^}]*?S\.cR=\[\];?\}',
        INIT_C_NEW, html, count=1, flags=re.DOTALL
    )
    if INIT_C_NEW not in html:
        # Last-ditch: replace entire function body via bracket scan
        idx = html.find('function initC(')
        if idx >= 0:
            depth = 0; end = -1
            for i, c in enumerate(html[idx:], start=idx):
                if c == '{': depth += 1
                elif c == '}':
                    depth -= 1
                    if depth == 0:
                        end = i + 1
                        break
            if end > 0:
                html = html[:idx] + INIT_C_NEW + html[end:]
    return html


def splice_initq(html):
    if INIT_Q_NEW in html:
        return html
    if INIT_Q_OLD in html:
        return html.replace(INIT_Q_OLD, INIT_Q_NEW, 1)
    # Bracket-scan fallback
    idx = html.find('function initQ(')
    if idx >= 0:
        depth = 0; end = -1
        for i, c in enumerate(html[idx:], start=idx):
            if c == '{': depth += 1
            elif c == '}':
                depth -= 1
                if depth == 0:
                    end = i + 1
                    break
        if end > 0:
            html = html[:idx] + INIT_Q_NEW + html[end:]
    return html


def splice_rvis(html):
    """Insert SVG block into mkCard."""
    if RVIS_NEW_PIECE in html:
        return html
    if RVIS_OLD_PIECE in html:
        return html.replace(RVIS_OLD_PIECE, RVIS_NEW_PIECE, 1)
    return html


def splice_render(html):
    if RENDER_TABS_NEW not in html and RENDER_TABS_OLD in html:
        html = html.replace(RENDER_TABS_OLD, RENDER_TABS_NEW, 1)
    if RENDER_DISPATCH_NEW not in html and RENDER_DISPATCH_OLD in html:
        html = html.replace(RENDER_DISPATCH_OLD, RENDER_DISPATCH_NEW, 1)
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
        html = splice_rv2(html)
        html = splice_rsheet(html)
        html = splice_initc(html)
        html = splice_initq(html)
        html = splice_rvis(html)
        html = splice_render(html)

        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        after = len(html)
        delta = after - before
        sign = '+' if delta >= 0 else ''
        print(f'  {os.path.basename(path)}: {before:,} -> {after:,} bytes ({sign}{delta:,})')

    # Sanity checks
    print('\nSanity checks:')
    for path in HTMLS:
        with open(path, 'r', encoding='utf-8') as f:
            html = f.read()
        bn = os.path.basename(path)
        checks = [
            ('rV2 fn',       'function rV2(ct,n){'),
            ('rSheet fn',    'function rSheet(ct){'),
            ('rV2 dispatch', 'if(n.v2){return rV2(ct,n);}'),
            ('Sheet tab',    "['sheet'"),
            ('Sheet dispatch', "S.mode==='sheet'"),
            ('initC v3',     'D.nodes.forEach(function(n){var fcs='),
            ('initQ v3',     'D.nodes.forEach(function(n){var quizes='),
            ('rVis svg',     "if(n.v2&&n.v2.svg&&!dim){"),
            ('CSS v2-start', '/*v2-start*/'),
            ('CSS sheet',    '.sheet-wrap'),
        ]
        for name, sig in checks:
            ok = sig in html
            print(f'  {bn}  {"OK" if ok else "FAIL"}  {name}')
            if not ok:
                print(f'      missing: {sig[:80]}')
        m = re.search(r'<script id="sd" type="application/json">(.*?)</script>', html, re.DOTALL)
        if m:
            d = json.loads(m.group(1))
            assert len(d['nodes']) == 57, f'expected 57 nodes, got {len(d["nodes"])}'
            n0 = d['nodes'][0]
            assert 'v2' in n0 and 'svg' in n0['v2'], 'missing v2.svg'
            assert 'flashcards' in n0['v2'] and len(n0['v2']['flashcards']) == 4
            assert 'quiz' in n0['v2'] and len(n0['v2']['quiz']) == 4
            print(f'  {bn}  OK  JSON has 57 nodes, v2.svg/flashcards/quiz arrays')
        print()

    print('Done.')


if __name__ == '__main__':
    main()
