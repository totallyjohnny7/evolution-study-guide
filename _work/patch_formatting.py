"""
Patch index_prod.html and index.html with:
1. Rich body text formatter (bullets, numbered lists, caps sub-headers)
2. Exam trap callout box styling for warnings
3. Practice question displayed at bottom of every popup
"""
import sys, os
sys.stdout.reconfigure(encoding='utf-8')

BUILDER = os.path.dirname(os.path.abspath(__file__))
ROOT    = os.path.normpath(os.path.join(BUILDER, '..', 'public'))
FILES   = [os.path.join(ROOT, 'index_prod.html'), os.path.join(ROOT, 'index.html')]

# ─────────────────────────────────────────────────────────────────────────────
# PATCH 1 — Rich body formatter
# Replace the plain-text paragraph renderer with a rich formatter that handles:
#   • bullet lines, numbered steps, ALL CAPS: sub-headers, normal paragraphs
# ─────────────────────────────────────────────────────────────────────────────
P1_OLD = (
    "}else if(s.body.indexOf(String.fromCharCode(10))>=0)"
    "{s.body.split(String.fromCharCode(10)).forEach(function(p)"
    "{if(!p.trim())return;var pe=el('p',{style:'margin-bottom:8px'});"
    "pe.textContent=p;bd.appendChild(pe);});}else{bd.textContent=s.body;}"
    "sec.appendChild(bd);})()"
)

P1_NEW = (
    # fall-through case: use rich formatter for everything
    "}else{(function(){"
    "var NL=String.fromCharCode(10);"
    "var lines=s.body.split(NL);"
    "var ulEl=null;"
    "lines.forEach(function(line){"
      "var t=line.trim();"
      "if(!t){ulEl=null;return;}"
      # Bullet: starts with • or -<space>
      "if(/^[\\u2022\\-]\\s/.test(t)){"
        "if(!ulEl){ulEl=el('ul',{style:'margin:6px 0 10px 0;padding-left:0;list-style:none'});bd.appendChild(ulEl);}"
        "var li=el('li',{style:'display:flex;align-items:flex-start;gap:8px;margin-bottom:5px;color:#c8c4b8;line-height:1.75'});"
        "var dot=el('span',{style:'color:#00c9a7;font-size:10px;flex-shrink:0;margin-top:5px'},'\u25cf');"
        "var sptxt=el('span',{style:'font-size:13.5px'});"
        "sptxt.textContent=t.replace(/^[\\u2022\\-]\\s/,'');"
        "li.appendChild(dot);li.appendChild(sptxt);ulEl.appendChild(li);return;}"
      "ulEl=null;"
      # Numbered step: starts with digit + . or )
      "var nm=t.match(/^(\\d+)[.)] +(.*)/);"
      "if(nm){"
        "var nr=el('div',{style:'display:flex;align-items:flex-start;gap:10px;margin-bottom:7px;color:#c8c4b8;line-height:1.75'});"
        "var nc2=el('div',{style:'min-width:18px;height:18px;background:#00c9a7;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:9px;font-weight:700;color:#0a0a0e;flex-shrink:0;margin-top:3px'});"
        "nc2.textContent=nm[1];"
        "var ntxt=el('span',{style:'font-size:13.5px'});ntxt.textContent=nm[2];"
        "nr.appendChild(nc2);nr.appendChild(ntxt);bd.appendChild(nr);return;}"
      # ALL-CAPS sub-header ending with colon, under 80 chars
      "if(/^[A-Z][A-Z0-9 ()\\/#&+\\-]+:/.test(t)&&t.length<80){"
        "var bk=el('div',{style:'font-size:9.5px;font-weight:700;text-transform:uppercase;letter-spacing:1.5px;color:#6c6880;margin:12px 0 5px;border-top:1px solid rgba(255,255,255,.04);padding-top:8px'});"
        "bk.textContent=t.replace(/:$/,'');bd.appendChild(bk);return;}"
      # Normal paragraph
      "var pe=el('p',{style:'margin-bottom:8px;font-size:13.5px;color:#c8c4b8;line-height:1.85'});"
      "pe.textContent=line;bd.appendChild(pe);"
    "});"
    "}());}sec.appendChild(bd);})()"
)

# ─────────────────────────────────────────────────────────────────────────────
# PATCH 2 — Warnings: styled as exam-trap callout boxes
# ─────────────────────────────────────────────────────────────────────────────
P2_OLD_END   = "});pb.appendChild(wDiv);}if(p.mnemonic)"
P2_SEARCH    = "if(p.warnings&&p.warnings.length){"

P2_NEW_BLOCK = (
    "if(p.warnings&&p.warnings.length){"
      "var wDiv=el('div',{style:'margin-top:14px'});"
      "wDiv.appendChild(el('div',{style:'font-size:9.5px;font-weight:700;text-transform:uppercase;letter-spacing:1.5px;color:#44416a;margin-bottom:8px'},'EXAM TRAPS'));"
      "p.warnings.forEach(function(w){"
        "var wi=el('div',{style:'background:rgba(224,82,82,.06);border-left:3px solid #e05252;border-radius:0 8px 8px 0;padding:10px 14px;margin-bottom:8px;font-size:13px;color:#c8c4b8;line-height:1.75'});"
        "var wIcon=el('span',{style:'color:#e05252;font-weight:700;margin-right:6px'},'\u26a0 ');"
        "wi.appendChild(wIcon);wi.appendChild(document.createTextNode(w));wDiv.appendChild(wi);"
      "});pb.appendChild(wDiv);"
    "}if(p.mnemonic)"
)

# ─────────────────────────────────────────────────────────────────────────────
# PATCH 3 — Practice question at bottom of every node popup
# Insert before: panel.appendChild(pb);ct.appendChild(panel);}function rCards
# ─────────────────────────────────────────────────────────────────────────────
P3_ANCHOR = "panel.appendChild(pb);ct.appendChild(panel);}function rCards"
P3_INSERT  = (
    "if(p.quiz){"
      "var qDiv=el('div',{style:'margin-top:20px;border-top:1px solid rgba(255,255,255,.06);padding-top:16px'});"
      "qDiv.appendChild(el('div',{style:'font-size:9.5px;font-weight:700;text-transform:uppercase;letter-spacing:1.5px;color:#44416a;margin-bottom:10px'},'PRACTICE QUESTION'));"
      "var qBox=el('div',{style:'background:#13131d;border-radius:12px;padding:14px 16px;border:1px solid rgba(255,255,255,.06)'});"
      "var qTxt=el('p',{style:'font-size:13.5px;color:#e8e4d8;line-height:1.75;margin-bottom:12px;font-weight:500'});"
      "qTxt.textContent=p.quiz.question;qBox.appendChild(qTxt);"
      "var qA=el('div',{style:'background:rgba(0,201,167,.07);border-left:3px solid #00c9a7;border-radius:0 8px 8px 0;padding:10px 14px;font-size:13px;color:#7fe8d8;line-height:1.65'});"
      "var qAl=el('span',{style:'font-weight:700;color:#00c9a7;margin-right:6px'},'\u2713 ');"
      "qA.appendChild(qAl);qA.appendChild(document.createTextNode(p.quiz.correct));"
      "qBox.appendChild(qA);qDiv.appendChild(qBox);pb.appendChild(qDiv);"
    "}"
    "panel.appendChild(pb);ct.appendChild(panel);}function rCards"
)

def patch_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    orig_size = len(html)
    results = {}

    # PATCH 1 — body renderer
    if P1_OLD in html:
        html = html.replace(P1_OLD, P1_NEW, 1)
        results['P1_body'] = 'OK'
    else:
        results['P1_body'] = 'FAIL - old string not found'

    # PATCH 2 — warnings callout
    # Find the whole warnings block by locating start + known end marker
    wi_start = html.find(P2_SEARCH)
    wi_end   = html.find(P2_OLD_END, wi_start) if wi_start != -1 else -1
    if wi_start != -1 and wi_end != -1:
        old_block = html[wi_start : wi_end + len(P2_OLD_END)]
        html = html[:wi_start] + P2_NEW_BLOCK + html[wi_start + len(old_block):]
        results['P2_warnings'] = 'OK'
    else:
        results['P2_warnings'] = f'FAIL (wi_start={wi_start}, wi_end={wi_end})'

    # PATCH 3 — practice question
    if P3_ANCHOR in html:
        html = html.replace(P3_ANCHOR, P3_INSERT, 1)
        results['P3_quiz'] = 'OK'
    else:
        results['P3_quiz'] = 'FAIL - anchor not found'

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    results['size'] = f'{orig_size:,} → {len(html):,}'
    return results

for fp in FILES:
    name = os.path.basename(fp)
    res  = patch_file(fp)
    print(f'\n{name}:')
    for k, v in res.items():
        icon = '✓' if v == 'OK' else ('→' if '→' in str(v) else '✗')
        print(f'  {icon} {k}: {v}')
