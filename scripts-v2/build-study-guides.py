"""Generate per-exam editable study guides from public/content/lecture-guides.js.

One-shot generator: re-run any time lecture-guides.js changes.
Reads:  public/content/lecture-guides.js, public/data/evol4230.json
Writes: public/study-guide-exam1.html, exam2.html, exam3.html, study-guide.html (cumulative)

The output HTML carries the full Word-doc-style toolbar (autosave, find/replace,
fonts, highlights, paragraph borders, configurable shortcuts, etc.) and seeds
its content from lecture-guides.js so each exam page opens with a useful first
draft the user can edit. All edits autosave to localStorage with an exam-specific
storage key so guides do not collide.
"""
from __future__ import annotations

import json
import re
import textwrap
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUBLIC = ROOT / "public"
LECTURE_GUIDES_JS = PUBLIC / "content" / "lecture-guides.js"
EVOL_JSON = PUBLIC / "data" / "evol4230.json"


def load_lecture_guides() -> dict:
    """Strip the leading `window.MANUAL_LECTURE_GUIDES = ` and parse the JSON object."""
    raw = LECTURE_GUIDES_JS.read_text(encoding="utf-8")
    # Find the opening brace after the assignment
    m = re.search(r"window\.MANUAL_LECTURE_GUIDES\s*=\s*", raw)
    if not m:
        raise RuntimeError("Could not find MANUAL_LECTURE_GUIDES assignment in lecture-guides.js")
    after = raw[m.end():]
    # Strip a trailing semicolon and any trailing comment lines after the closing brace
    # Walk braces to find the matching close
    depth = 0
    end = -1
    in_string = False
    str_ch = ""
    for i, ch in enumerate(after):
        if in_string:
            if ch == "\\":
                # next char is escaped — skip the next iteration
                continue
            if ch == str_ch:
                in_string = False
            continue
        if ch in ('"', "'"):
            in_string = True
            str_ch = ch
            continue
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                end = i + 1
                break
    if end == -1:
        raise RuntimeError("Could not find end of MANUAL_LECTURE_GUIDES object")
    return json.loads(after[:end])


def load_meta() -> dict:
    return json.loads(EVOL_JSON.read_text(encoding="utf-8"))


def render_section(letter: str, sec: dict) -> str:
    """Render one section (A/B/C…) of a lecture as <h3> + paragraphs."""
    parts: list[str] = []
    title = escape(sec.get("title", ""))
    parts.append(f'<h3>§{letter} — {title}</h3>')
    overview = sec.get("overview", "").strip()
    if overview:
        parts.append(f'<p class="overview">{escape(overview)}</p>')
    key_points = sec.get("key_points") or []
    if key_points:
        parts.append('<p class="q">Key points</p>')
        parts.append('<ul class="a">')
        for kp in key_points:
            parts.append(f'<li>{escape(kp)}</li>')
        parts.append('</ul>')
    key_terms = sec.get("key_terms") or []
    if key_terms:
        parts.append('<p class="q">Key terms</p>')
        parts.append('<ul class="a">')
        for kt in key_terms:
            term = escape(kt.get("term", ""))
            df = escape(kt.get("def", ""))
            parts.append(f'<li><b>{term}</b> — {df}</li>')
        parts.append('</ul>')
    traps = sec.get("exam_traps") or []
    if traps:
        parts.append('<div class="callout"><b>Exam traps</b><ul style="margin-top:4px">')
        for t in traps:
            parts.append(f'<li>{escape(t)}</li>')
        parts.append('</ul></div>')
    return "\n".join(parts)


def render_lecture(lid: str, lect: dict, chapter: str | None) -> str:
    title = escape(lect.get("title", lid))
    subtitle = f' <span style="color:#7a7158;font-size:11pt;">({escape(chapter)})</span>' if chapter else ""
    parts: list[str] = [f'<h2>{lid} · {title}{subtitle}</h2>']
    intro = (lect.get("intro") or "").strip()
    if intro:
        parts.append(f'<p class="intro">{escape(intro)}</p>')
    for sec in lect.get("sections") or []:
        letter = sec.get("letter", "")
        parts.append(render_section(letter, sec))
    return "\n\n".join(parts)


def build_body(exam_id, exam_title: str, lectures: list[str], guides: dict, meta: dict) -> str:
    chapter_by_lid = {l["id"]: l.get("chapter") for l in meta["lectures"]}
    title_by_lid = {l["id"]: l.get("title") for l in meta["lectures"]}
    parts: list[str] = []
    parts.append(f'<h1>{escape(exam_title)} Study Guide</h1>')
    chips = " · ".join(lectures)
    parts.append(
        f'<p class="meta">BIOL 4230 · Evolution · {escape(exam_title)} '
        f'— Final exam Mon May 4, 2026 · 5–7 PM · Dr. Travis Robbins<br/>'
        f'Lectures: {escape(chips)}</p>'
    )
    parts.append('<p class="intro">This guide is fully editable — type anywhere, format with the toolbar, and your edits autosave to this browser. Reset restores the seeded content. Print to PDF (8.5×11 portrait) anytime.</p>')
    for lid in lectures:
        lect = guides.get(lid)
        if not lect:
            parts.append(f'<h2>{lid} <span style="color:#a3290e;font-size:11pt">(no seed content yet — start typing)</span></h2><p class="a">&nbsp;</p>')
            continue
        parts.append(render_lecture(lid, lect, chapter_by_lid.get(lid)))
    return "\n\n".join(parts)


HTML_TEMPLATE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{{TITLE}} — BIOL 4230 Evolution</title>
<style>
  :root{
    --bg:#0c0e12; --paper:#fdfaf2; --ink:#1a1814; --muted:#5b554b;
    --rule:#d8d2c5; --accent:#c89b2e; --accent-bg:#fff4e2;
    --shadow: 0 8px 24px rgba(0,0,0,0.35);
  }
  *{box-sizing:border-box}
  html,body{margin:0;padding:0;background:var(--bg);color:var(--ink);font-family:"Times New Roman", Times, serif;}
  /* Toolbar */
  .tb{position:sticky;top:0;z-index:50;background:#16161b;color:#e6dfd0;border-bottom:1px solid #22262f;padding:6px 12px;display:flex;flex-direction:column;gap:5px;font-family:"Inter",system-ui,-apple-system,Segoe UI,Roboto,sans-serif;font-size:12.5px;box-shadow:var(--shadow)}
  .tb-row{display:flex;flex-wrap:wrap;gap:6px;align-items:center}
  .tb .grp{display:inline-flex;gap:3px;align-items:center;border:1px solid #22262f;border-radius:6px;padding:2px 4px;background:#0c0e12}
  .tb button, .tb select, .tb input[type=color]{
    background:#14171d;border:1px solid transparent;border-radius:4px;padding:3px 6px;font-size:12.5px;cursor:pointer;color:#e6dfd0
  }
  .tb button:hover{background:#22262f}
  .tb button:active{background:var(--accent);color:#0c0e12}
  .tb select{padding:3px 5px;max-width:160px;background:#14171d;color:#e6dfd0}
  .tb input[type=color]{width:24px;height:22px;padding:0;border:1px solid #22262f}
  .tb .spacer{flex:1}
  .tb .save-status{font-size:11.5px;color:#a59a83;min-width:140px;text-align:right;padding:0 6px}
  .tb .save-status b{color:#5fa871}
  .tb .save-status.dirty b{color:var(--accent)}
  .tb-btn-wide{padding:3px 9px;font-weight:600}
  .tb a.back-link{color:var(--accent);text-decoration:none;font-weight:600;padding:3px 8px;font-size:12.5px}
  .tb a.back-link:hover{text-decoration:underline}
  .doc blockquote{border-left:3px solid var(--accent);background:#fff7e8;margin:6px 0 6px 8px;padding:4px 12px;color:#3a2e15;font-style:italic}
  .doc pre{font-family:Consolas,Menlo,Monaco,monospace;background:#fffaf0;border:1px solid var(--rule);border-radius:4px;padding:6px 10px;margin:6px 0;font-size:10.5pt;white-space:pre-wrap}
  .doc .pb-all{border:1px solid #555;padding:4px 8px;border-radius:3px}
  .doc .pb-top{border-top:1px solid #555;padding-top:3px}
  .doc .pb-bottom{border-bottom:1px solid #555;padding-bottom:3px}
  .doc .pb-left{border-left:3px solid #555;padding-left:8px}
  .doc .pb-right{border-right:3px solid #555;padding-right:8px}
  .doc .find-hit{background:#ffe17a;outline:1px solid #d6a01a}
  .doc .find-hit-current{background:#ff9b1a;outline:2px solid #b04200;color:#fff}
  /* Find bar */
  .findbar{position:sticky;top:80px;z-index:49;background:#fffaf0;border-bottom:1px solid var(--rule);padding:6px 12px;display:flex;gap:6px;align-items:center;flex-wrap:wrap;box-shadow:0 4px 12px rgba(0,0,0,0.06);font-family:"Inter",system-ui,sans-serif;font-size:13px}
  .findbar input[type=text]{padding:5px 8px;border:1px solid var(--rule);border-radius:4px;font-size:13px;min-width:180px}
  .findbar button{padding:5px 10px;border:1px solid var(--rule);background:#fff;border-radius:4px;cursor:pointer;font-size:12.5px}
  .findbar button:hover{background:#f1ead9}
  /* Page wrapper */
  .pageWrap{padding:24px 0;display:flex;flex-direction:column;align-items:center;gap:16px}
  .doc{
    width:8.5in; min-height:11in; background:var(--paper); padding:0.55in 0.7in;
    box-shadow:var(--shadow); border:1px solid var(--rule);
    font-size:11pt; line-height:1.32;
  }
  .doc:focus{outline:none}
  .doc h1{font-size:16pt;text-align:center;margin:0 0 2px;font-family:"Fraunces",Georgia,serif}
  .doc h2{font-size:13pt;border-bottom:1.2pt solid var(--ink);padding-bottom:2px;margin:14px 0 6px;clear:both;font-family:"Fraunces",Georgia,serif;color:#3a2e15}
  .doc h3{font-size:11.5pt;margin:8px 0 3px;color:#3a2e15;text-decoration:underline}
  .doc h4{font-size:11pt;margin:6px 0 1px;font-style:italic}
  .doc p{margin:2px 0 4px}
  .doc p.intro{margin:4px 0 8px;font-style:italic;color:#3a2e15}
  .doc p.overview{margin:3px 0 6px;color:#1a1814}
  .doc .meta{text-align:center;color:var(--muted);font-size:10pt;margin-bottom:8px}
  .doc ul{margin:2px 0 6px 18px;padding:0}
  .doc li{margin:1px 0}
  .doc .q{font-weight:700;margin-top:6px;color:#3a2e15}
  .doc .a{font-weight:400}
  .doc figure{
    width:1.7in; margin:2px 8px 4px 8px; float:right; clear:right;
    text-align:center; page-break-inside:avoid; break-inside:avoid;
    font-size:8.5pt;
  }
  .doc figure img{max-width:100%;height:auto;max-height:1.6in;object-fit:contain;border:1px solid var(--rule);border-radius:3px;display:block;margin:0 auto}
  .doc figcaption{font-size:8pt;color:var(--muted);margin-top:1px;font-style:italic;line-height:1.18}
  .doc h2, .doc h3, .doc table, .doc .pagebreak{clear:both}
  .doc table{margin-top:6px;border-collapse:collapse;width:100%;font-size:10.5pt}
  .doc th,.doc td{border:0.5pt solid #888;padding:4px 6px;vertical-align:top}
  .doc th{background:#f1ead9;text-align:left}
  .doc .twocol{display:grid;grid-template-columns:1fr 1fr;gap:10px}
  .doc .threecol{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px}
  .doc .pathway{font-family:Consolas,Menlo,Monaco,monospace;font-size:10.5pt;background:#fffaf0;border-left:3px solid var(--accent);padding:6px 10px;margin:6px 0}
  .doc .callout{border-left:3px solid var(--accent);background:#fff7e8;padding:6px 10px;margin:8px 0;font-size:10.5pt;color:#3a2e15}
  .pagebreak{page-break-after:always;break-after:page;height:0}
  .modal{display:none;position:fixed;inset:0;background:rgba(0,0,0,0.55);z-index:200;align-items:center;justify-content:center;padding:20px;font-family:system-ui,sans-serif}
  .modal.show{display:flex}
  .modal-card{background:#fff;border-radius:10px;max-width:1000px;width:100%;max-height:90vh;overflow:auto;padding:14px;color:#111}
  .modal-card h3{margin:0 0 8px;font-family:system-ui}
  /* Print */
  @page{size:letter portrait;margin:0.45in}
  @media print{
    body{background:#fff}
    .tb,.modal,.pageWrap,.findbar{padding:0;background:#fff;color:#111}
    .tb,.findbar{display:none !important}
    .doc{width:auto;min-height:0;box-shadow:none;border:none;padding:0;font-size:10.5pt;line-height:1.28}
    .doc figure{width:1.5in;font-size:8pt}
    .doc figure img{max-height:1.4in}
    .doc figcaption{font-size:7.5pt}
    .doc h1{font-size:15pt}
    .doc h2{font-size:12.5pt;margin:10px 0 4px}
    .doc h3{font-size:11pt;margin:6px 0 2px}
    .pagebreak{page-break-after:always}
    figure{page-break-inside:avoid}
    h2,h3{page-break-after:avoid}
    .no-print{display:none !important}
  }
</style>
</head>
<body>

<div class="tb no-print" id="toolbar">

  <!-- Row 1 -->
  <div class="tb-row">
    <a class="back-link" href="guides.html">← Guides</a>
    <a class="back-link" href="index.html">EVOLution</a>
    <div class="grp" title="Paragraph style">
      <select id="styleSelect" title="Paragraph style">
        <option value="P">Normal</option>
        <option value="H1">Title</option>
        <option value="H2">Heading 1</option>
        <option value="H3">Heading 2</option>
        <option value="H4">Heading 3</option>
        <option value="BLOCKQUOTE">Quote</option>
        <option value="PRE">Code block</option>
      </select>
    </div>
    <div class="grp">
      <select id="fontFamily" title="Font family">
        <option value="Times New Roman, Times, serif" selected>Times New Roman</option>
        <option value="Georgia, serif">Georgia</option>
        <option value="Garamond, serif">Garamond</option>
        <option value="Cambria, serif">Cambria</option>
        <option value="Arial, Helvetica, sans-serif">Arial</option>
        <option value="Calibri, sans-serif">Calibri</option>
        <option value="Verdana, sans-serif">Verdana</option>
        <option value="Tahoma, sans-serif">Tahoma</option>
        <option value="Trebuchet MS, sans-serif">Trebuchet MS</option>
        <option value="Courier New, monospace">Courier New</option>
        <option value="Consolas, monospace">Consolas</option>
      </select>
      <select id="fontSize" title="Font size (pt)">
        <option value="1">8 pt</option>
        <option value="2">10 pt</option>
        <option value="3" selected>12 pt</option>
        <option value="4">14 pt</option>
        <option value="5">18 pt</option>
        <option value="6">24 pt</option>
        <option value="7">36 pt</option>
      </select>
    </div>
    <div class="grp">
      <button onclick="cmd('bold')" title="Bold (Ctrl+B)"><b>B</b></button>
      <button onclick="cmd('italic')" title="Italic (Ctrl+I)"><i>I</i></button>
      <button onclick="cmd('underline')" title="Underline (Ctrl+U)"><u>U</u></button>
      <button onclick="cmd('strikeThrough')" title="Strikethrough"><s>S</s></button>
      <button onclick="cmd('superscript')" title="Superscript (Ctrl+Shift+=)">x<sup>2</sup></button>
      <button onclick="cmd('subscript')" title="Subscript (Ctrl+=)">x<sub>2</sub></button>
      <button onclick="changeCase()" title="Change case — UPPER · lower · Title · Sentence">Aa▾</button>
    </div>
    <div class="grp">
      <input type="color" id="fgColor" title="Text color" value="#111111" />
      <input type="color" id="bgColor" title="Highlight color (text background)" value="#fff36b" />
      <button onclick="unhighlight()" title="Remove highlight from selected text (Ctrl+Shift+H toggles)">⌫H</button>
      <input type="color" id="paraShade" title="Paragraph shading (block background)" value="#f1ead9" />
    </div>
    <div class="grp">
      <button onclick="cmd('undo')" title="Undo (Ctrl+Z)">↶</button>
      <button onclick="cmd('redo')" title="Redo (Ctrl+Y)">↷</button>
      <button onclick="cmd('removeFormat')" title="Clear formatting">⌫f</button>
    </div>
    <div class="spacer"></div>
    <div class="save-status" id="saveStatus" title="Edits autosave to this browser only">Loaded</div>
  </div>

  <!-- Row 2 -->
  <div class="tb-row">
    <div class="grp">
      <button onclick="cmd('insertUnorderedList')" title="Bullet list">•≡</button>
      <button onclick="cmd('insertOrderedList')" title="Numbered list">1.</button>
      <select id="listStyleSelect" title="Multilevel / list style">
        <option value="">List style…</option>
        <optgroup label="Unordered">
          <option value="ul:disc">• disc</option>
          <option value="ul:circle">○ circle</option>
          <option value="ul:square">▪ square</option>
        </optgroup>
        <optgroup label="Ordered">
          <option value="ol:decimal">1. 2. 3.</option>
          <option value="ol:lower-alpha">a. b. c.</option>
          <option value="ol:upper-alpha">A. B. C.</option>
          <option value="ol:lower-roman">i. ii. iii.</option>
          <option value="ol:upper-roman">I. II. III.</option>
        </optgroup>
      </select>
      <button onclick="cmd('outdent')" title="Decrease indent (Shift+Tab)">⇤</button>
      <button onclick="cmd('indent')" title="Increase indent (Tab)">⇥</button>
    </div>
    <div class="grp">
      <button onclick="cmd('justifyLeft')" title="Align left">⯇</button>
      <button onclick="cmd('justifyCenter')" title="Align center">≡</button>
      <button onclick="cmd('justifyRight')" title="Align right">⯈</button>
      <button onclick="cmd('justifyFull')" title="Justify">☰</button>
    </div>
    <div class="grp">
      <select id="lineSpacing" title="Line spacing">
        <option value="">Spacing…</option>
        <option value="1.0">1.0</option>
        <option value="1.15">1.15</option>
        <option value="1.32">1.32 (default)</option>
        <option value="1.5">1.5</option>
        <option value="2.0">2.0</option>
        <option value="2.5">2.5</option>
        <option value="3.0">3.0</option>
      </select>
      <select id="borderSelect" title="Paragraph border">
        <option value="">Border…</option>
        <option value="none">No border</option>
        <option value="all">Box (all sides)</option>
        <option value="top">Top only</option>
        <option value="bottom">Bottom only</option>
        <option value="left">Left only</option>
        <option value="right">Right only</option>
      </select>
      <button onclick="applyShade()" title="Apply selected shading color to paragraph(s)">Shade</button>
    </div>
    <div class="grp">
      <button onclick="openFind()" title="Find (Ctrl+F)">🔍 Find</button>
      <button onclick="openReplace()" title="Find &amp; Replace (Ctrl+H)">⇄ Replace</button>
      <button onclick="cmd('selectAll')" title="Select all (Ctrl+A)">Select All</button>
    </div>
    <div class="grp">
      <select id="jumpTo" title="Jump to a section">
        <option value="">Jump to…</option>
      </select>
    </div>
    <div class="grp">
      <button onclick="document.getElementById('imgFile').click()" title="Insert image from your computer">📷 Image</button>
      <input type="file" id="imgFile" accept="image/*" style="display:none" onchange="insertImageFromFile(event)" />
      <button onclick="insertHorizontalRule()" title="Horizontal rule">―</button>
      <button onclick="insertPageBreak()" title="Insert page break (for print)">⤓ break</button>
    </div>
    <div class="spacer"></div>
    <div class="grp">
      <button onclick="openShortcuts()" title="Edit keyboard shortcuts">⌨ Shortcuts</button>
      <button onclick="window.print()" title="Print or save as PDF (8.5×11 portrait)" class="tb-btn-wide">Print / PDF</button>
      <button onclick="downloadHTML()" title="Save the current document as a standalone .html file">⤓ .html</button>
      <button onclick="resetDoc()" title="Restore the original seeded answers (your edits will be lost)" style="color:#c89b2e">Reset</button>
    </div>
  </div>
</div>

<!-- ===== Shortcuts Settings Modal ===== -->
<div class="modal" id="shortcutsModal" onclick="if(event.target===this) closeShortcuts()">
  <div class="modal-card" style="max-width:560px">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
      <h3 style="margin:0">Keyboard shortcuts</h3>
      <button onclick="closeShortcuts()" style="font-size:14px;padding:5px 10px;border:1px solid #ccc;border-radius:4px;background:#fff;cursor:pointer">Close</button>
    </div>
    <p style="font-size:12.5px;color:#5b554b;margin:0 0 8px">Click a key combo to rebind. Then press the new combo (any of Ctrl/Alt/Shift + a key). Settings are saved to this browser.</p>
    <table id="shortcutsTable" style="width:100%;font-family:system-ui,sans-serif;font-size:13px;border-collapse:collapse"></table>
    <div style="margin-top:10px;display:flex;gap:6px;justify-content:flex-end">
      <button onclick="resetShortcuts()" style="padding:6px 12px;border:1px solid var(--rule);background:#fff;border-radius:4px;cursor:pointer;color:#a3290e">Reset to defaults</button>
    </div>
  </div>
</div>

<div class="pageWrap">
<div class="doc" id="doc" contenteditable="true" spellcheck="false">

{{BODY}}

</div><!-- /doc -->
</div><!-- /pageWrap -->

<!-- ===== Find / Replace Bar ===== -->
<div class="findbar no-print" id="findbar" style="display:none">
  <input type="text" id="findInput" placeholder="Find" autocomplete="off" />
  <input type="text" id="replaceInput" placeholder="Replace with…" autocomplete="off" />
  <button onclick="findNext()" title="Next match (Enter)">↓ Next</button>
  <button onclick="findPrev()" title="Previous match (Shift+Enter)">↑ Prev</button>
  <button onclick="replaceOne()" title="Replace current match">Replace</button>
  <button onclick="replaceAll()" title="Replace all matches">Replace All</button>
  <span id="findCount" style="color:#5b554b;font-size:12px;margin-left:6px"></span>
  <button onclick="closeFind()" title="Close (Esc)" style="margin-left:auto;color:#a3290e">Close</button>
</div>

<script>
(function(){
  'use strict';
  window.addEventListener('error', e => { console.warn('[study-guide] caught:', e.message); });

  const doc = document.getElementById('doc');
  const status = document.getElementById('saveStatus');
  const STORAGE_KEY = '{{STORAGE_KEY}}';
  const SHORTCUT_KEY = '{{STORAGE_KEY}}_shortcuts_v1';
  const PRISTINE_HTML = doc.innerHTML;

  try{
    const saved = localStorage.getItem(STORAGE_KEY);
    if(saved){ doc.innerHTML = saved; status.innerHTML = 'Loaded from <b>local save</b>'; }
    else { status.innerHTML = 'Loaded — <b>fresh copy</b>'; }
  }catch(e){ console.warn('localStorage unavailable', e); status.innerHTML = '<span style="color:#c34">localStorage off</span>'; }

  let saveTimer = null;
  function markDirty(){
    status.classList.add('dirty');
    status.innerHTML = 'Editing…';
    if(saveTimer) clearTimeout(saveTimer);
    saveTimer = setTimeout(scheduleSave, 1200);
  }
  function scheduleSave(){
    if('requestIdleCallback' in window){
      requestIdleCallback(saveNow, {timeout: 1500});
    } else {
      setTimeout(saveNow, 0);
    }
  }
  function saveNow(){
    try{
      localStorage.setItem(STORAGE_KEY, doc.innerHTML);
      status.classList.remove('dirty');
      const t = new Date().toLocaleTimeString();
      status.innerHTML = 'Saved <b>'+t+'</b>';
    }catch(e){
      status.innerHTML = '<span style="color:#c34">Save failed</span> — '+e.message;
    }
  }
  doc.addEventListener('input', markDirty);
  doc.addEventListener('paste', () => setTimeout(markDirty, 30));
  window.addEventListener('beforeunload', saveNow);

  function cmd(name, value){
    try{
      document.execCommand(name, false, value || null);
      doc.focus();
      markDirty();
    }catch(e){ console.warn('[study-guide] cmd '+name+' failed:', e); }
  }
  document.getElementById('fontFamily').addEventListener('change', e => { restoreSelection(); cmd('fontName', e.target.value); });
  document.getElementById('fontSize').addEventListener('change', e => { restoreSelection(); cmd('fontSize', e.target.value); });
  document.getElementById('fgColor').addEventListener('change', e => { restoreSelection(); cmd('foreColor', e.target.value); });
  document.getElementById('bgColor').addEventListener('change', e => { restoreSelection(); cmd('hiliteColor', e.target.value); });

  function insertHorizontalRule(){ cmd('insertHorizontalRule'); }
  function insertPageBreak(){
    document.execCommand('insertHTML', false, '<div class="pagebreak"></div>');
    markDirty();
  }

  function insertImageFromFile(ev){
    const f = ev.target.files[0]; if(!f) return;
    const r = new FileReader();
    r.onload = e => {
      doc.focus();
      document.execCommand('insertHTML', false, '<figure><img src="'+e.target.result+'" alt="user image"/><figcaption>User-inserted image</figcaption></figure>');
      markDirty();
    };
    r.readAsDataURL(f);
    ev.target.value = '';
  }

  function resetDoc(){
    if(!confirm('Reset to the seeded content? Your edits will be lost.')) return;
    doc.innerHTML = PRISTINE_HTML;
    saveNow();
  }

  function downloadHTML(){
    const html = '<!doctype html><html><head><meta charset="utf-8"><title>{{TITLE}} — BIOL 4230</title><style>'+
      'body{font-family:"Times New Roman",serif;max-width:7in;margin:0.5in auto;line-height:1.45}'+
      'h1{text-align:center}h2{border-bottom:1.5pt solid #000;padding-bottom:3px}h3{text-decoration:underline}'+
      'figure{text-align:center;margin:8px auto}figure img{max-width:100%;border:1px solid #888}'+
      'figcaption{font-size:10pt;color:#555;font-style:italic}'+
      'table{border-collapse:collapse;width:100%;font-size:10.5pt}'+
      'th,td{border:0.5pt solid #888;padding:4px 6px;vertical-align:top}'+
      '.q{font-weight:700}.a{font-weight:400}'+
      '.callout{border-left:3px solid #c89b2e;background:#fff7e8;padding:6px 10px;margin:8px 0}'+
      '.pagebreak{page-break-after:always}'+
      '@page{size:letter portrait;margin:0.5in}'+
      '</style></head><body>' + doc.innerHTML + '</body></html>';
    const blob = new Blob([html], {type:'text/html'});
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url; a.download = '{{DOWNLOAD_NAME}}.html';
    document.body.appendChild(a); a.click(); a.remove();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  }

  function applyBlockStyle(){
    const el = document.getElementById('styleSelect');
    if(!el) return;
    const tag = el.value;
    if(!tag) return;
    try{
      document.execCommand('formatBlock', false, '<' + tag + '>');
      doc.focus();
      markDirty();
    }catch(e){ console.warn('formatBlock failed', e); }
    el.selectedIndex = 0;
  }

  function getSelectedBlocks(){
    const sel = window.getSelection();
    if(!sel || sel.rangeCount === 0) return [];
    const range = sel.getRangeAt(0);
    const blocks = new Set();
    function climb(node){
      while(node && node !== doc){
        if(node.nodeType === 1){
          const d = getComputedStyle(node).display;
          if(d === 'block' || d === 'list-item' || /^(P|H[1-6]|LI|BLOCKQUOTE|PRE|FIGURE|TABLE|TR|TD|TH|DIV)$/.test(node.tagName)){
            blocks.add(node); return;
          }
        }
        node = node.parentNode;
      }
    }
    climb(range.startContainer);
    climb(range.endContainer);
    const it = document.createTreeWalker(doc, NodeFilter.SHOW_ELEMENT, {
      acceptNode: n => range.intersectsNode(n) ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_SKIP
    });
    let n;
    while((n = it.nextNode())){
      const d = getComputedStyle(n).display;
      if(d === 'block' || d === 'list-item') blocks.add(n);
    }
    return Array.from(blocks);
  }

  function changeCase(){
    const choice = prompt('Change case to:\n  1) UPPERCASE\n  2) lowercase\n  3) Title Case\n  4) Sentence case\nEnter 1, 2, 3, or 4:');
    const sel = window.getSelection();
    if(!sel || sel.isCollapsed){ alert('Select some text first.'); return; }
    const text = sel.toString();
    let out = text;
    if(choice === '1') out = text.toUpperCase();
    else if(choice === '2') out = text.toLowerCase();
    else if(choice === '3') out = text.toLowerCase().replace(/\b([a-z])/g, (m, c) => c.toUpperCase());
    else if(choice === '4'){
      out = text.toLowerCase().replace(/(^|[.!?]\s+)([a-z])/g, (m, p, c) => p + c.toUpperCase());
    } else return;
    document.execCommand('insertText', false, out);
    markDirty();
  }

  function applyLineSpacing(){
    const el = document.getElementById('lineSpacing');
    if(!el || !el.value) return;
    const v = el.value;
    getSelectedBlocks().forEach(b => { b.style.lineHeight = v; });
    el.selectedIndex = 0;
    markDirty();
  }

  function colorsEqual(a, b){
    if(!a || !b) return false;
    const ma = ('' + a).match(/\d+/g);
    const mb = ('' + b).match(/\d+/g);
    if(!ma || !mb) return false;
    return ma.slice(0,3).join(',') === mb.slice(0,3).join(',');
  }
  function hexToRgb(hex){
    const m = hex.replace('#','');
    return 'rgb(' + parseInt(m.slice(0,2),16) + ', ' + parseInt(m.slice(2,4),16) + ', ' + parseInt(m.slice(4,6),16) + ')';
  }
  function applyShade(){
    const c = document.getElementById('paraShade').value;
    const target = hexToRgb(c);
    const blocks = getSelectedBlocks();
    if(!blocks.length) return;
    const allHave = blocks.every(b => colorsEqual(b.style.backgroundColor, target));
    blocks.forEach(b => {
      if(allHave){
        b.style.backgroundColor = '';
        if(!/pb-/.test(b.className)) b.style.padding = '';
      } else {
        b.style.backgroundColor = c;
        if(!b.style.padding) b.style.padding = '4px 8px';
      }
    });
    markDirty();
  }

  function applyBorder(){
    const el = document.getElementById('borderSelect');
    if(!el || !el.value) return;
    const which = el.value;
    const blocks = getSelectedBlocks();
    el.selectedIndex = 0;
    if(!blocks.length) return;
    if(which === 'none'){
      blocks.forEach(b => b.classList.remove('pb-all','pb-top','pb-bottom','pb-left','pb-right'));
    } else {
      const cls = 'pb-' + which;
      const allHave = blocks.every(b => b.classList.contains(cls));
      blocks.forEach(b => {
        if(allHave){
          b.classList.remove(cls);
        } else {
          b.classList.remove('pb-all','pb-top','pb-bottom','pb-left','pb-right');
          b.classList.add(cls);
        }
      });
    }
    markDirty();
  }

  function applyListStyle(){
    const el = document.getElementById('listStyleSelect');
    if(!el || !el.value) return;
    const [tag, style] = el.value.split(':');
    const cmdName = tag === 'ol' ? 'insertOrderedList' : 'insertUnorderedList';
    document.execCommand(cmdName, false, null);
    const sel = window.getSelection();
    if(sel && sel.rangeCount){
      let n = sel.getRangeAt(0).startContainer;
      while(n && n !== doc){
        if(n.nodeType === 1 && /^(UL|OL)$/.test(n.tagName)){ n.style.listStyleType = style; break; }
        n = n.parentNode;
      }
    }
    el.selectedIndex = 0;
    markDirty();
  }

  /* FIND / REPLACE */
  let findHits = [];
  let findIndex = -1;
  function clearFindHits(){
    doc.querySelectorAll('.find-hit, .find-hit-current').forEach(el => {
      const parent = el.parentNode;
      while(el.firstChild) parent.insertBefore(el.firstChild, el);
      parent.removeChild(el);
      parent.normalize();
    });
    findHits = []; findIndex = -1;
    const cnt = document.getElementById('findCount'); if(cnt) cnt.textContent = '';
  }
  function highlightAll(query){
    clearFindHits();
    if(!query) return;
    const re = new RegExp(query.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'gi');
    const walker = document.createTreeWalker(doc, NodeFilter.SHOW_TEXT, {
      acceptNode: n => n.parentElement && n.parentElement.closest('.find-hit') ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT
    });
    const targets = [];
    let n;
    while((n = walker.nextNode())){ if(re.test(n.nodeValue)){ re.lastIndex = 0; targets.push(n); } }
    targets.forEach(node => {
      const text = node.nodeValue;
      const frag = document.createDocumentFragment();
      let last = 0;
      let m;
      const re2 = new RegExp(query.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'gi');
      while((m = re2.exec(text))){
        if(m.index > last) frag.appendChild(document.createTextNode(text.slice(last, m.index)));
        const span = document.createElement('span');
        span.className = 'find-hit';
        span.textContent = m[0];
        frag.appendChild(span);
        findHits.push(span);
        last = m.index + m[0].length;
        if(m[0].length === 0) re2.lastIndex++;
      }
      if(last < text.length) frag.appendChild(document.createTextNode(text.slice(last)));
      node.parentNode.replaceChild(frag, node);
    });
    const cnt = document.getElementById('findCount');
    if(cnt) cnt.textContent = findHits.length ? (findHits.length + ' match' + (findHits.length === 1 ? '' : 'es')) : 'No matches';
    if(findHits.length){ findIndex = 0; markCurrent(); }
  }
  function markCurrent(){
    findHits.forEach((h, i) => h.className = (i === findIndex ? 'find-hit-current' : 'find-hit'));
    if(findHits[findIndex]) findHits[findIndex].scrollIntoView({block:'center', behavior:'smooth'});
    const cnt = document.getElementById('findCount');
    if(cnt && findHits.length) cnt.textContent = (findIndex+1) + ' / ' + findHits.length;
  }
  function findNext(){ if(!findHits.length) return; findIndex = (findIndex+1) % findHits.length; markCurrent(); }
  function findPrev(){ if(!findHits.length) return; findIndex = (findIndex-1+findHits.length) % findHits.length; markCurrent(); }
  function replaceOne(){
    const r = document.getElementById('replaceInput').value;
    if(findIndex < 0 || !findHits[findIndex]) return;
    const hit = findHits[findIndex];
    const txt = document.createTextNode(r);
    hit.parentNode.replaceChild(txt, hit);
    findHits.splice(findIndex, 1);
    if(findIndex >= findHits.length) findIndex = 0;
    markCurrent();
    markDirty();
  }
  function replaceAll(){
    const r = document.getElementById('replaceInput').value;
    if(!findHits.length) return;
    findHits.forEach(h => { h.parentNode.replaceChild(document.createTextNode(r), h); });
    const n = findHits.length;
    findHits = []; findIndex = -1;
    const cnt = document.getElementById('findCount'); if(cnt) cnt.textContent = 'Replaced ' + n;
    markDirty();
  }
  function openFind(){
    document.getElementById('findbar').style.display = 'flex';
    const i = document.getElementById('findInput'); i.focus(); i.select();
  }
  function openReplace(){ openFind(); document.getElementById('replaceInput').focus(); }
  function closeFind(){ clearFindHits(); document.getElementById('findbar').style.display = 'none'; doc.focus(); }

  /* JUMP-TO TOC */
  function buildJumpTo(){
    const sel = document.getElementById('jumpTo');
    if(!sel) return;
    sel.innerHTML = '<option value="">Jump to…</option>';
    const heads = doc.querySelectorAll('h1, h2, h3');
    let i = 0;
    heads.forEach(h => {
      if(!h.id) h.id = 'sec-' + (i++);
      const indent = h.tagName === 'H1' ? '' : (h.tagName === 'H2' ? '— ' : '  · ');
      const o = document.createElement('option');
      o.value = h.id;
      o.textContent = indent + (h.textContent || '').trim().slice(0, 60);
      sel.appendChild(o);
    });
  }
  buildJumpTo();
  let tocTimer = null;
  doc.addEventListener('input', () => { clearTimeout(tocTimer); tocTimer = setTimeout(buildJumpTo, 1500); });

  /* TOOLBAR WIRING */
  document.querySelectorAll('.tb button, .findbar button').forEach(btn => {
    btn.addEventListener('mousedown', e => e.preventDefault());
  });

  let savedRange = null;
  function saveSelection(){
    try{
      const sel = window.getSelection();
      if(sel && sel.rangeCount){
        const r = sel.getRangeAt(0);
        if(doc.contains(r.commonAncestorContainer)) savedRange = r.cloneRange();
      }
    }catch(e){}
  }
  function restoreSelection(){
    if(!savedRange) return;
    try{
      const sel = window.getSelection();
      sel.removeAllRanges();
      sel.addRange(savedRange);
    }catch(e){}
  }
  doc.addEventListener('mouseup', saveSelection);
  doc.addEventListener('keyup', saveSelection);
  document.querySelectorAll('.tb select, .tb input[type=color]').forEach(el => {
    el.addEventListener('mousedown', saveSelection);
    el.addEventListener('focus', saveSelection);
  });
  function wrapWithRestore(handler){ return function(e){ restoreSelection(); handler(e); }; }

  document.getElementById('styleSelect').addEventListener('change', wrapWithRestore(applyBlockStyle));
  document.getElementById('lineSpacing').addEventListener('change', wrapWithRestore(applyLineSpacing));
  document.getElementById('borderSelect').addEventListener('change', wrapWithRestore(applyBorder));
  document.getElementById('listStyleSelect').addEventListener('change', wrapWithRestore(applyListStyle));
  document.getElementById('jumpTo').addEventListener('change', e => {
    const id = e.target.value;
    if(!id) return;
    const target = document.getElementById(id);
    if(target){ target.scrollIntoView({behavior:'smooth', block:'start'}); }
    e.target.selectedIndex = 0;
  });
  document.getElementById('findInput').addEventListener('input', e => highlightAll(e.target.value));
  document.getElementById('findInput').addEventListener('keydown', e => {
    if(e.key === 'Enter'){ e.preventDefault(); e.shiftKey ? findPrev() : findNext(); }
    if(e.key === 'Escape'){ closeFind(); }
  });
  document.getElementById('replaceInput').addEventListener('keydown', e => {
    if(e.key === 'Escape') closeFind();
  });

  /* HIGHLIGHT toggle */
  function selectionHasHighlight(){
    try{
      const v = document.queryCommandValue('hiliteColor') || document.queryCommandValue('backColor');
      if(!v) return false;
      const trimmed = ('' + v).trim();
      if(!trimmed || trimmed === 'transparent' || /rgba?\(\s*0\s*,\s*0\s*,\s*0\s*,\s*0\s*\)/.test(trimmed)) return false;
      const m = trimmed.match(/rgba?\((\d+)\s*,\s*(\d+)\s*,\s*(\d+)/);
      if(m && +m[1] >= 250 && +m[2] >= 250 && +m[3] >= 250) return false;
      return true;
    }catch(e){ return false; }
  }
  function unhighlight(){
    try{
      document.execCommand('hiliteColor', false, 'transparent');
      const sel = window.getSelection();
      if(sel && sel.rangeCount){
        const range = sel.getRangeAt(0);
        const it = document.createTreeWalker(doc, NodeFilter.SHOW_ELEMENT, {
          acceptNode: n => range.intersectsNode(n) ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_SKIP
        });
        let n;
        while((n = it.nextNode())){
          if(n.style && n.style.backgroundColor) n.style.backgroundColor = '';
        }
      }
      doc.focus();
      markDirty();
    }catch(e){ console.warn('unhighlight failed', e); }
  }
  function toggleHighlight(){
    if(selectionHasHighlight()){
      unhighlight();
    } else {
      const c = document.getElementById('bgColor').value;
      cmd('hiliteColor', c);
    }
  }

  /* CONFIGURABLE SHORTCUTS */
  const ACTIONS = [
    {id:'save',          label:'Save now',                        def:'ctrl+s',         run: () => saveNow()},
    {id:'find',          label:'Find',                            def:'ctrl+f',         run: () => openFind()},
    {id:'replace',       label:'Find & Replace',                  def:'ctrl+h',         run: () => openReplace()},
    {id:'highlight',     label:'Toggle highlight on selection',   def:'ctrl+shift+h',   run: () => toggleHighlight()},
    {id:'unhighlight',   label:'Remove highlight',                def:'ctrl+shift+u',   run: () => unhighlight()},
    {id:'bold',          label:'Bold',                            def:'ctrl+b',         run: () => cmd('bold')},
    {id:'italic',        label:'Italic',                          def:'ctrl+i',         run: () => cmd('italic')},
    {id:'underline',     label:'Underline',                       def:'ctrl+u',         run: () => cmd('underline')},
    {id:'strike',        label:'Strikethrough',                   def:'',               run: () => cmd('strikeThrough')},
    {id:'super',         label:'Superscript',                     def:'ctrl+shift+=',   run: () => cmd('superscript')},
    {id:'sub',           label:'Subscript',                       def:'ctrl+=',         run: () => cmd('subscript')},
    {id:'selectAll',     label:'Select all (in document)',        def:'ctrl+a',         run: () => {
        const range = document.createRange(); range.selectNodeContents(doc);
        const sel = window.getSelection(); sel.removeAllRanges(); sel.addRange(range);
    }},
    {id:'indent',        label:'Increase indent',                 def:'tab',            run: () => { document.execCommand('indent'); markDirty(); }},
    {id:'outdent',       label:'Decrease indent',                 def:'shift+tab',      run: () => { document.execCommand('outdent'); markDirty(); }},
    {id:'undo',          label:'Undo',                            def:'ctrl+z',         run: () => cmd('undo')},
    {id:'redo',          label:'Redo',                            def:'ctrl+y',         run: () => cmd('redo')}
  ];
  let bindings = {};
  function loadShortcuts(){
    try{
      const saved = JSON.parse(localStorage.getItem(SHORTCUT_KEY) || '{}');
      bindings = {};
      ACTIONS.forEach(a => { bindings[a.id] = saved[a.id] != null ? saved[a.id] : a.def; });
    }catch(e){ bindings = Object.fromEntries(ACTIONS.map(a => [a.id, a.def])); }
  }
  function saveShortcuts(){
    try{ localStorage.setItem(SHORTCUT_KEY, JSON.stringify(bindings)); }catch(e){ console.warn('save shortcuts failed', e); }
  }
  function resetShortcuts(){
    if(!confirm('Reset all shortcuts to defaults?')) return;
    bindings = {};
    ACTIONS.forEach(a => { bindings[a.id] = a.def; });
    saveShortcuts();
    renderShortcuts();
  }
  function comboFromEvent(e){
    if(e.key === 'Tab'){
      return (e.shiftKey ? 'shift+' : '') + 'tab';
    }
    if(e.key === 'Escape' || e.key === 'Control' || e.key === 'Shift' || e.key === 'Alt' || e.key === 'Meta') return null;
    const parts = [];
    if(e.ctrlKey || e.metaKey) parts.push('ctrl');
    if(e.altKey) parts.push('alt');
    if(e.shiftKey) parts.push('shift');
    parts.push(e.key.toLowerCase());
    return parts.join('+');
  }
  loadShortcuts();

  function openShortcuts(){
    document.getElementById('shortcutsModal').classList.add('show');
    renderShortcuts();
  }
  function closeShortcuts(){
    document.getElementById('shortcutsModal').classList.remove('show');
  }
  function renderShortcuts(){
    const tbl = document.getElementById('shortcutsTable');
    tbl.innerHTML = '<tr style="background:#f1ead9"><th style="text-align:left;padding:6px 8px;border-bottom:1px solid #ccc">Action</th><th style="text-align:left;padding:6px 8px;border-bottom:1px solid #ccc">Shortcut</th><th style="border-bottom:1px solid #ccc"></th></tr>';
    ACTIONS.forEach(a => {
      const tr = document.createElement('tr');
      tr.innerHTML =
        '<td style="padding:5px 8px;border-bottom:1px solid #eee">'+a.label+'</td>' +
        '<td style="padding:5px 8px;border-bottom:1px solid #eee"><button data-act="'+a.id+'" class="kb-btn" style="font-family:Consolas,monospace;padding:3px 8px;border:1px solid #ccc;border-radius:4px;background:#fff;cursor:pointer;min-width:130px;text-align:left">'+(bindings[a.id] || '— click to set —')+'</button></td>' +
        '<td style="padding:5px 4px;border-bottom:1px solid #eee"><button data-clear="'+a.id+'" style="font-size:11px;padding:3px 6px;border:1px solid #ccc;border-radius:3px;background:#fff;cursor:pointer">clear</button></td>';
      tbl.appendChild(tr);
    });
    tbl.querySelectorAll('.kb-btn').forEach(btn => {
      btn.onclick = () => {
        btn.textContent = '… press a key combo …';
        btn.style.background = '#fff4e2';
        const handler = (ev) => {
          ev.preventDefault();
          const combo = comboFromEvent(ev);
          if(combo == null) return;
          const conflict = Object.entries(bindings).find(([k,v]) => v === combo && k !== btn.dataset.act);
          if(conflict){
            const ok = confirm('That combo is already bound to "'+ACTIONS.find(a=>a.id===conflict[0]).label+'". Reassign anyway?');
            if(!ok){ btn.textContent = bindings[btn.dataset.act] || '— click to set —'; btn.style.background='#fff'; window.removeEventListener('keydown', handler, true); return; }
            bindings[conflict[0]] = '';
          }
          bindings[btn.dataset.act] = combo;
          saveShortcuts();
          window.removeEventListener('keydown', handler, true);
          renderShortcuts();
        };
        window.addEventListener('keydown', handler, true);
      };
    });
    tbl.querySelectorAll('button[data-clear]').forEach(btn => {
      btn.onclick = () => { bindings[btn.dataset.clear] = ''; saveShortcuts(); renderShortcuts(); };
    });
  }

  document.addEventListener('keydown', e => {
    if(document.getElementById('shortcutsModal').classList.contains('show')) return;
    const combo = comboFromEvent(e);
    if(!combo) return;
    for(const a of ACTIONS){
      if(bindings[a.id] && bindings[a.id] === combo){
        if((a.id === 'indent' || a.id === 'outdent') && !doc.contains(document.activeElement)) return;
        if(a.id === 'selectAll' && !doc.contains(document.activeElement)) return;
        e.preventDefault();
        try{ a.run(); }catch(err){ console.warn('shortcut '+a.id+' failed:', err); }
        return;
      }
    }
  });

  /* PUBLIC */
  window.cmd = cmd;
  window.changeCase = changeCase;
  window.applyShade = applyShade;
  window.unhighlight = unhighlight;
  window.toggleHighlight = toggleHighlight;
  window.openShortcuts = openShortcuts;
  window.closeShortcuts = closeShortcuts;
  window.resetShortcuts = resetShortcuts;
  window.insertHorizontalRule = insertHorizontalRule;
  window.insertPageBreak = insertPageBreak;
  window.insertImageFromFile = insertImageFromFile;
  window.openFind = openFind;
  window.openReplace = openReplace;
  window.closeFind = closeFind;
  window.findNext = findNext;
  window.findPrev = findPrev;
  window.replaceOne = replaceOne;
  window.replaceAll = replaceAll;
  window.resetDoc = resetDoc;
  window.downloadHTML = downloadHTML;
})();
</script>
</body>
</html>
"""


def render(template: str, *, title: str, body: str, storage_key: str, download_name: str) -> str:
    return (
        template
        .replace("{{TITLE}}", title)
        .replace("{{BODY}}", body)
        .replace("{{STORAGE_KEY}}", storage_key)
        .replace("{{DOWNLOAD_NAME}}", download_name)
    )


def main():
    guides = load_lecture_guides()
    meta = load_meta()
    exams = {e["id"]: e for e in meta["exams"]}

    targets = [
        (1, exams[1]["lectures"], "Exam 1 · Mechanisms / Pop Gen", "study-guide-exam1.html", "evol4230_exam1_studyguide_v1", "Exam1_StudyGuide_BIOL4230"),
        (2, exams[2]["lectures"], "Exam 2 · Adaptations / Sex / Social", "study-guide-exam2.html", "evol4230_exam2_studyguide_v1", "Exam2_StudyGuide_BIOL4230"),
        (3, exams[3]["lectures"], "Exam 3 · Phylogeny / Speciation / Humans", "study-guide-exam3.html", "evol4230_exam3_studyguide_v1", "Exam3_StudyGuide_BIOL4230"),
        ("final", exams[0]["lectures"], "Cumulative Final · All units", "study-guide.html", "evol4230_final_studyguide_v1", "Final_StudyGuide_BIOL4230"),
    ]

    for exam_id, lectures, exam_title, filename, storage_key, download_name in targets:
        body = build_body(exam_id, exam_title, lectures, guides, meta)
        html = render(HTML_TEMPLATE, title=exam_title, body=body, storage_key=storage_key, download_name=download_name)
        out = PUBLIC / filename
        out.write_text(html, encoding="utf-8")
        print(f"wrote {out.relative_to(ROOT)} ({len(lectures)} lectures, {len(html):,} bytes)")


if __name__ == "__main__":
    main()
