"""Surgical inject: flatten data + minimal function patches + CSS.

Patches applied to clean v2 baseline (git 54d1a8e) of public/index.html:

  1. Embed flattened data.json (the JSON <script id="sd"> block).
  2. Replace initC      ->  reads v2.flashcards array (4 cards/node).
  3. Replace rV2        ->  adds SVG slot, structured transcript renderer
                            with parseT() helper (numbered lists, bullet
                            lists, term/def lists, paragraphs).
  4. Patch render()      ->  preserves scroll position across re-renders
                            via requestAnimationFrame.
  5. Append CSS for new classes (.v2-svg-wrap, .v2-trans-*).
"""
import sys
import io
import re
import json

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


# -----------------------------------------------------------------------------
# 1. NEW initC  (replaces the 155-char legacy initC exactly)
# -----------------------------------------------------------------------------

INIT_C_OLD = (
    "function initC(){var n=D.nodes[S.sel];"
    "if(n&&n.flashcard&&n.flashcard.front){"
    "S.cDk=[n];S.cI=0;S.cF=false;S.cR=[];"
    "}else{S.cDk=[];S.cI=0;S.cF=false;S.cR=[];}}"
)

INIT_C_NEW = (
    "function initC(){"
    "var n=D.nodes[S.sel];"
    "S.cDk=[];S.cI=0;S.cF=false;S.cR=[];"
    "if(!n)return;"
    "var fcs=n.v2&&n.v2.flashcards;"
    "if(fcs&&fcs.length){"
    "fcs.forEach(function(fc){"
    "S.cDk.push({title:n.title,color:n.color,popup:n.popup,flashcard:fc});"
    "});"
    "}else if(n.flashcard&&n.flashcard.front){"
    "S.cDk=[n];"
    "}"
    "}"
)


# -----------------------------------------------------------------------------
# 2. SCROLL PRESERVATION patch on render()
#
# The layout uses display:flex with .ct { overflow-y:auto } — the *window*
# never scrolls, the scroll lives entirely inside .ct (and .sb for sidebar).
# window.scrollY is always 0, so the old patch was a no-op.
#
# Correct fix: capture $A.querySelector('.ct').scrollTop and
# $A.querySelector('.sb').scrollTop BEFORE the innerHTML wipe, then restore
# them to the NEW .ct and .sb elements after the synchronous DOM rebuild.
# requestAnimationFrame fires after all synchronous JS completes (render()
# has fully rebuilt the DOM) but before the browser repaints — perfect timing.
# -----------------------------------------------------------------------------

SCROLL_OLD = "function render(){$A.innerHTML='';"
SCROLL_NEW = (
    "function render(){"
    "var __ctEl=$A.querySelector('.ct');"
    "var __sbEl=$A.querySelector('.sb');"
    "var __cty=__ctEl?__ctEl.scrollTop:0;"
    "var __sby=__sbEl?__sbEl.scrollTop:0;"
    "if(typeof requestAnimationFrame==='function'){"
    "requestAnimationFrame(function(){"
    "var nc=$A.querySelector('.ct');if(nc)nc.scrollTop=__cty;"
    "var ns=$A.querySelector('.sb');if(ns)ns.scrollTop=__sby;"
    "});"
    "}else{"
    "setTimeout(function(){"
    "var nc=$A.querySelector('.ct');if(nc)nc.scrollTop=__cty;"
    "var ns=$A.querySelector('.sb');if(ns)ns.scrollTop=__sby;"
    "},0);"
    "}"
    "$A.innerHTML='';"
)


# -----------------------------------------------------------------------------
# 3. NEW rV2 with structured transcript renderer
# -----------------------------------------------------------------------------

RV2_OLD = (
    'function rV2(ct,n){var v=n.v2;var nc=NC[n.color]||NC.gray;'
    "var panel=el('div',{className:'popup-panel v2-panel'});"
    "var meta=el('div',{className:'v2-meta'});"
    "meta.appendChild(el('span',{className:'v2-meta-lec'},'LEC '+n.lecture));"
    "meta.appendChild(document.createTextNode(' \\u00b7 '));"
    "meta.appendChild(el('span',{className:'v2-meta-title'},n.lectureTitle));"
    "meta.appendChild(document.createTextNode(' \\u00b7 '));"
    "meta.appendChild(el('span',{className:'v2-meta-ch'},n.chapter));"
    "meta.appendChild(document.createTextNode(' \\u00b7 slides '));"
    "meta.appendChild(el('span',{className:'v2-meta-slides'},n.slideRange));"
    "panel.appendChild(meta);"
    "var ph=el('div',{className:'popup-header v2-header',"
    "style:{borderLeft:'4px solid '+nc.bdr}});"
    "ph.appendChild(el('h2',{},n.title));"
    "panel.appendChild(ph);"
    "var pb=el('div',{className:'popup-body v2-body'});"
    "var def=el('div',{className:'v2-slot'});"
    "def.appendChild(el('div',{className:'v2-label'},'\\u25c6 DEFINITION'));"
    "def.appendChild(el('div',{className:'v2-def-text'},v.definition));"
    "pb.appendChild(def);"
    "var kt=el('div',{className:'v2-slot'});"
    "kt.appendChild(el('div',{className:'v2-label'},'\\u25c6 KEY TERMS'));"
    "var ktg=el('div',{className:'v2-terms-grid'});"
    "v.keyTerms.forEach(function(t){"
    "var col=NC[t.color]||NC.gray;"
    "var card=el('div',{className:'v2-term',"
    "style:{borderLeft:'3px solid '+col.bdr,background:col.bg}});"
    "card.appendChild(el('div',{className:'v2-term-name'},t.term));"
    "card.appendChild(el('div',{className:'v2-term-def'},t.def));"
    "ktg.appendChild(card);});"
    "kt.appendChild(ktg);pb.appendChild(kt);"
    "var mn=el('div',{className:'v2-slot'});"
    "mn.appendChild(el('div',{className:'v2-label'},'\\u25c6 MNEMONIC'));"
    "var mb=el('div',{className:'v2-mnemonic'});"
    "mb.appendChild(el('div',{className:'v2-mn-hook'},v.mnemonic.hook));"
    "mb.appendChild(el('div',{className:'v2-mn-exp'},v.mnemonic.explanation));"
    "mn.appendChild(mb);pb.appendChild(mn);"
    "var et=el('div',{className:'v2-slot'});"
    "et.appendChild(el('div',{className:'v2-label v2-trap-label'},'\\u25b2 EXAM TRAP'));"
    "var etb=el('div',{className:'v2-trap'});"
    "etb.appendChild(el('div',{className:'v2-trap-text'},v.examTrap));"
    "et.appendChild(etb);pb.appendChild(et);"
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
    "ac.appendChild(fc);pb.appendChild(ac);"
    "panel.appendChild(pb);ct.appendChild(panel);}"
)


# -- parseT() helper, embedded inside the new rV2 ----------------------------

PARSE_T = (
    # Parses raw transcript text into a list of DOM nodes (paragraphs,
    # ordered lists, bullet lists, definition lists). Strips a duplicated
    # title at the very top of the body if present.
    "function parseT(txt,slTitle){"
    "if(!txt)return[];"
    "if(slTitle){"
    "var fl=txt.split('\\n')[0].trim();"
    "if(fl===slTitle.trim()){"
    "txt=txt.split('\\n').slice(1).join('\\n').replace(/^\\s+/,'');"
    "}"
    "}"
    "var blocks=txt.split(/\\n\\s*\\n/);"
    "var out=[];"
    "blocks.forEach(function(b){"
    "var lines=b.split('\\n').map(function(l){return l.trim();})"
    ".filter(function(l){return l.length;});"
    "if(!lines.length)return;"
    # Numbered list (every line starts with N.)
    "if(lines.length>=2&&lines.every(function(l){return /^\\d+\\.[ \\t]/.test(l);})){"
    "var ol=el('ol',{className:'v2-trans-ol'});"
    "lines.forEach(function(l){"
    "ol.appendChild(el('li',{},l.replace(/^\\d+\\.[ \\t]+/,'')));"
    "});"
    "out.push(ol);return;"
    "}"
    # Bullet list (every line starts with - or * or bullet)
    "if(lines.length>=2&&lines.every(function(l){return /^[-*\\u2022][ \\t]/.test(l);})){"
    "var ul=el('ul',{className:'v2-trans-ul'});"
    "lines.forEach(function(l){"
    "ul.appendChild(el('li',{},l.replace(/^[-*\\u2022][ \\t]+/,'')));"
    "});"
    "out.push(ul);return;"
    "}"
    # Definition pattern: at least half the lines have " - " or " \u2013 "
    "var dlMatches=lines.filter(function(l){return /\\s[\\u2013\\u2014-]\\s/.test(l)&&l.length<200;}).length;"
    "if(lines.length>=2&&dlMatches>=Math.ceil(lines.length/2)){"
    "var dl=el('dl',{className:'v2-trans-dl'});"
    "lines.forEach(function(l){"
    "var m=l.match(/^([^\\u2013\\u2014-]+)[\\u2013\\u2014-]\\s*(.+)$/);"
    "if(m&&m[1].trim().length<=60){"
    "dl.appendChild(el('dt',{},m[1].trim()));"
    "dl.appendChild(el('dd',{},m[2].trim()));"
    "}else{"
    "dl.appendChild(el('dd',{className:'v2-trans-dd-plain'},l));"
    "}"
    "});"
    "out.push(dl);return;"
    "}"
    # Default: paragraph
    "out.push(el('p',{className:'v2-trans-p'},lines.join(' ')));"
    "});"
    "return out;"
    "}"
)


RV2_NEW = (
    'function rV2(ct,n){var v=n.v2;var nc=NC[n.color]||NC.gray;'
    + PARSE_T +
    # --- preamble: panel + meta + header ---
    "var panel=el('div',{className:'popup-panel v2-panel'});"
    "var meta=el('div',{className:'v2-meta'});"
    "meta.appendChild(el('span',{className:'v2-meta-lec'},'LEC '+n.lecture));"
    "meta.appendChild(document.createTextNode(' \\u00b7 '));"
    "meta.appendChild(el('span',{className:'v2-meta-title'},n.lectureTitle));"
    "meta.appendChild(document.createTextNode(' \\u00b7 '));"
    "meta.appendChild(el('span',{className:'v2-meta-ch'},n.chapter));"
    "meta.appendChild(document.createTextNode(' \\u00b7 slides '));"
    "meta.appendChild(el('span',{className:'v2-meta-slides'},n.slideRange));"
    "panel.appendChild(meta);"
    "var ph=el('div',{className:'popup-header v2-header',"
    "style:{borderLeft:'4px solid '+nc.bdr}});"
    "ph.appendChild(el('h2',{},n.title));"
    "panel.appendChild(ph);"
    "var pb=el('div',{className:'popup-body v2-body'});"
    # --- definition ---
    "var def=el('div',{className:'v2-slot'});"
    "def.appendChild(el('div',{className:'v2-label'},'\\u25c6 DEFINITION'));"
    "def.appendChild(el('div',{className:'v2-def-text'},v.definition));"
    "pb.appendChild(def);"
    # --- key terms ---
    "var kt=el('div',{className:'v2-slot'});"
    "kt.appendChild(el('div',{className:'v2-label'},'\\u25c6 KEY TERMS'));"
    "var ktg=el('div',{className:'v2-terms-grid'});"
    "v.keyTerms.forEach(function(t){"
    "var col=NC[t.color]||NC.gray;"
    "var card=el('div',{className:'v2-term',"
    "style:{borderLeft:'3px solid '+col.bdr,background:col.bg}});"
    "card.appendChild(el('div',{className:'v2-term-name'},t.term));"
    "card.appendChild(el('div',{className:'v2-term-def'},t.def));"
    "ktg.appendChild(card);});"
    "kt.appendChild(ktg);pb.appendChild(kt);"
    # --- SVG visual slot ---
    "if(v.svg){"
    "var vs=el('div',{className:'v2-slot'});"
    "vs.appendChild(el('div',{className:'v2-label'},'\\u25c6 VISUAL DIAGRAM'));"
    "var svgWrap=el('div',{className:'v2-svg-wrap'});"
    "svgWrap.innerHTML=v.svg;"
    "var svgEl=svgWrap.querySelector('svg');"
    "if(svgEl){svgEl.style.maxWidth='100%';svgEl.style.height='auto';}"
    "vs.appendChild(svgWrap);"
    "pb.appendChild(vs);"
    "}"
    # --- mnemonic ---
    "var mn=el('div',{className:'v2-slot'});"
    "mn.appendChild(el('div',{className:'v2-label'},'\\u25c6 MNEMONIC'));"
    "var mb=el('div',{className:'v2-mnemonic'});"
    "mb.appendChild(el('div',{className:'v2-mn-hook'},v.mnemonic.hook));"
    "mb.appendChild(el('div',{className:'v2-mn-exp'},v.mnemonic.explanation));"
    "mn.appendChild(mb);pb.appendChild(mn);"
    # --- exam trap ---
    "var et=el('div',{className:'v2-slot'});"
    "et.appendChild(el('div',{className:'v2-label v2-trap-label'},'\\u25b2 EXAM TRAP'));"
    "var etb=el('div',{className:'v2-trap'});"
    "etb.appendChild(el('div',{className:'v2-trap-text'},v.examTrap));"
    "et.appendChild(etb);pb.appendChild(et);"
    # --- practice actions ---
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
    "ac.appendChild(fc);pb.appendChild(ac);"
    # --- structured transcript slot (collapsible) ---
    "if(v.transcript&&v.transcript.length){"
    "var tr=el('div',{className:'v2-slot'});"
    "tr.appendChild(el('div',{className:'v2-label'},"
    "'\\u25c6 LECTURE TRANSCRIPT ('+v.transcript.length+' slides)'));"
    "var det=document.createElement('details');"
    "det.className='v2-trans-details';"
    "var sum=document.createElement('summary');"
    "sum.className='v2-trans-sum';"
    "sum.textContent='Show transcript';"
    "det.appendChild(sum);"
    "v.transcript.forEach(function(sl){"
    "var sd=el('div',{className:'v2-trans-slide'});"
    "var stitle=el('div',{className:'v2-trans-title'},"
    "'Slide '+sl.n+(sl.title?': '+sl.title:''));"
    "sd.appendChild(stitle);"
    "if(sl.main){"
    "var mainBox=el('div',{className:'v2-trans-main'});"
    "parseT(sl.main,sl.title).forEach(function(node){"
    "mainBox.appendChild(node);"
    "});"
    "sd.appendChild(mainBox);"
    "}"
    "if(sl.notes){"
    "var notesBox=el('div',{className:'v2-trans-notes'});"
    "var nlbl=el('div',{className:'v2-trans-notes-label'},'Speaker notes');"
    "notesBox.appendChild(nlbl);"
    "parseT(sl.notes,sl.title).forEach(function(node){"
    "notesBox.appendChild(node);"
    "});"
    "sd.appendChild(notesBox);"
    "}"
    "det.appendChild(sd);"
    "});"
    "tr.appendChild(det);"
    "pb.appendChild(tr);"
    "}"
    # --- epilogue ---
    "panel.appendChild(pb);ct.appendChild(panel);}"
)


# -----------------------------------------------------------------------------
# 4. NEW CSS for visual + structured transcript slots
# -----------------------------------------------------------------------------

NEW_CSS = """
.v2-svg-wrap{background:#0d1117;border:1px solid #30363d;border-radius:10px;
padding:18px;margin-top:8px;text-align:center;max-width:100%;overflow-x:auto;}
.v2-svg-wrap svg{max-width:100%;height:auto;display:block;margin:0 auto;}
.v2-trans-details{background:#13131d;border:1px solid #30363d;border-radius:10px;
padding:0;margin-top:8px;}
.v2-trans-sum{cursor:pointer;padding:14px 18px;font-size:13px;font-weight:600;
color:#d4a826;user-select:none;list-style:none;}
.v2-trans-sum::-webkit-details-marker{display:none;}
.v2-trans-sum::before{content:'\u25b6 ';display:inline-block;
transition:transform .2s;margin-right:6px;}
.v2-trans-details[open] .v2-trans-sum::before{transform:rotate(90deg);}
.v2-trans-slide{border-top:1px solid #262634;padding:18px 22px;}
.v2-trans-slide:last-child{border-radius:0 0 10px 10px;}
.v2-trans-title{font-size:11px;font-weight:700;text-transform:uppercase;
letter-spacing:1.5px;color:#d4a826;margin-bottom:10px;
padding-bottom:6px;border-bottom:1px solid #262634;}
.v2-trans-main{font-size:14px;line-height:1.7;color:#d4d0c0;}
.v2-trans-main p,.v2-trans-notes p{margin:0 0 10px 0;}
.v2-trans-main p:last-child,.v2-trans-notes p:last-child{margin-bottom:0;}
.v2-trans-main ol,.v2-trans-notes ol,
.v2-trans-main ul,.v2-trans-notes ul{
margin:6px 0 12px 0;padding-left:22px;}
.v2-trans-main ol li,.v2-trans-notes ol li,
.v2-trans-main ul li,.v2-trans-notes ul li{
margin-bottom:6px;line-height:1.6;}
.v2-trans-main ol li::marker,.v2-trans-notes ol li::marker{
color:#d4a826;font-weight:700;}
.v2-trans-main ul li::marker,.v2-trans-notes ul li::marker{
color:#d4a826;}
.v2-trans-dl{margin:6px 0 12px 0;display:grid;grid-template-columns:auto 1fr;
gap:6px 14px;align-items:baseline;}
.v2-trans-dl dt{font-weight:700;color:#7de2d1;font-size:13px;
white-space:nowrap;}
.v2-trans-dl dd{margin:0;font-size:13.5px;line-height:1.6;color:#d4d0c0;}
.v2-trans-dd-plain{grid-column:1 / -1;color:#d4d0c0;}
.v2-trans-notes{margin-top:14px;padding-top:14px;
border-top:1px dashed #30363d;font-size:13px;line-height:1.65;
color:#9aa0a8;font-style:italic;}
.v2-trans-notes-label{font-style:normal;font-size:10px;font-weight:700;
text-transform:uppercase;letter-spacing:1.5px;color:#6e7681;
margin-bottom:8px;}
.v2-trans-notes .v2-trans-dl dt{color:#9d7ec5;}
"""


# -----------------------------------------------------------------------------
# Brace sanity check
# -----------------------------------------------------------------------------

def js_brace_balance(s):
    """Count braces ignoring string literals."""
    depth = 0
    in_str = False
    sc = None
    bs = False
    for c in s:
        if bs:
            bs = False
            continue
        if in_str:
            if c == '\\':
                bs = True
                continue
            if c == sc:
                in_str = False
        else:
            if c in "'\"`":
                in_str = True
                sc = c
            elif c == '{':
                depth += 1
            elif c == '}':
                depth -= 1
    return depth


# Self-check
assert js_brace_balance(INIT_C_OLD) == 0, f'INIT_C_OLD imbalanced: {js_brace_balance(INIT_C_OLD)}'
assert js_brace_balance(INIT_C_NEW) == 0, f'INIT_C_NEW imbalanced: {js_brace_balance(INIT_C_NEW)}'
assert js_brace_balance(RV2_OLD) == 0, f'RV2_OLD imbalanced: {js_brace_balance(RV2_OLD)}'
assert js_brace_balance(RV2_NEW) == 0, f'RV2_NEW imbalanced: {js_brace_balance(RV2_NEW)}'
assert js_brace_balance(PARSE_T) == 0, f'PARSE_T imbalanced: {js_brace_balance(PARSE_T)}'


# -----------------------------------------------------------------------------
# Patch functions
# -----------------------------------------------------------------------------

def patch_html(html, data_json_str):
    """Apply all patches to an HTML string."""
    errors = []

    # 1. Replace the JSON data block
    pat = re.compile(
        r'(<script id="sd" type="application/json">)(.*?)(</script>)',
        re.DOTALL
    )
    m = pat.search(html)
    if not m:
        errors.append('JSON block not found')
    else:
        html = pat.sub(
            lambda _: m.group(1) + data_json_str + m.group(3),
            html, count=1
        )

    # 2. Replace initC
    if INIT_C_OLD not in html:
        errors.append(f'INIT_C_OLD ({len(INIT_C_OLD)} chars) not found')
    else:
        html = html.replace(INIT_C_OLD, INIT_C_NEW, 1)

    # 3. Patch render() for scroll preservation
    if SCROLL_OLD not in html:
        errors.append(f'SCROLL_OLD ({len(SCROLL_OLD)} chars) not found')
    else:
        html = html.replace(SCROLL_OLD, SCROLL_NEW, 1)

    # 4. Replace rV2
    if RV2_OLD not in html:
        errors.append(f'RV2_OLD ({len(RV2_OLD)} chars) not found')
    else:
        html = html.replace(RV2_OLD, RV2_NEW, 1)

    # 5. Append CSS before </style>
    if '</style>' not in html:
        errors.append('</style> not found')
    else:
        html = html.replace('</style>', NEW_CSS + '</style>', 1)

    return html, errors


def main():
    # Restore clean v2 baseline of index.html from git (idempotent)
    import subprocess
    subprocess.run(
        ['git', 'checkout', '54d1a8e', '--', 'public/index.html'],
        check=True, capture_output=True
    )

    with open('data.json', 'r', encoding='utf-8') as f:
        data = f.read()
    json.loads(data)
    print(f'data.json: {len(data)/1024:.1f} KB loaded')
    print()
    print(f'INIT_C_OLD len: {len(INIT_C_OLD)}')
    print(f'INIT_C_NEW len: {len(INIT_C_NEW)}')
    print(f'SCROLL_OLD len: {len(SCROLL_OLD)}')
    print(f'SCROLL_NEW len: {len(SCROLL_NEW)}')
    print(f'RV2_OLD    len: {len(RV2_OLD)}')
    print(f'RV2_NEW    len: {len(RV2_NEW)} (incl PARSE_T={len(PARSE_T)})')
    print()

    html_path = 'public/index.html'
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    before_len = len(html)
    new_html, errors = patch_html(html, data)
    if errors:
        print(f'{html_path} ERRORS:')
        for e in errors:
            print(f'  - {e}')
        sys.exit(1)
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f'{html_path}: {before_len} -> {len(new_html)} ({len(new_html)-before_len:+} chars)')

    prod_path = 'public/index_prod.html'
    with open(prod_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f'{prod_path}: mirrored ({len(new_html)} chars)')

    # Verify brace balance across the entire main script
    m = re.search(
        r'<script(?![^>]*src)(?![^>]*application/json)[^>]*>(.*?)</script>',
        new_html, re.DOTALL
    )
    if m:
        js = m.group(1)
        bal = js_brace_balance(js)
        marker = 'OK' if bal == 0 else 'FAIL'
        print(f'Main script brace balance: {bal} [{marker}]')
        if bal != 0:
            sys.exit(2)


if __name__ == '__main__':
    main()
