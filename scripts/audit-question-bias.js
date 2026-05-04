/* Analyze the 4 evolution practice exams for common multiple-choice biases:
   - Answer letter distribution (A/B/C/D/E share)
   - Correct-answer length bias (mean chars: correct vs distractor)
   - "Position bias" — index of correct choice (0=A, 1=B, ...)
   - NOT/EXCEPT/FALSE question clustering
   - Number-of-choices consistency

   Targets:
   - Letter clustering ≤ 23% (no single letter > ~7 of 30)
   - Length ratio 1.0–1.4× (correct shouldn't be obviously longer)
*/
const fs = require('fs');
const path = require('path');
const ROOT = path.resolve(__dirname, '..');
const PE = JSON.parse(fs.readFileSync(path.join(ROOT, 'public/data/practice-exams.json'), 'utf8'));

function adaptPractice(exam) {
  return exam.mc.map(q => ({
    num: q.n, stem: q.q, ans: q.ans,
    choices: q.choices.map((c, i) => ({ letter: String.fromCharCode(65 + i), text: c })),
  }));
}

function analyze(label, mc) {
  const letters = { A: 0, B: 0, C: 0, D: 0, E: 0 };
  const choiceCounts = {};
  let notCount = 0, notRightLetters = {};
  let allLens = [], correctLens = [], distractorLens = [];
  for (const q of mc) {
    const ans = q.ans;
    if (!ans) continue;
    letters[ans] = (letters[ans] || 0) + 1;
    const cn = q.choices.length;
    choiceCounts[cn] = (choiceCounts[cn] || 0) + 1;
    if (/\b(NOT|EXCEPT|FALSE)\b/.test(q.stem || q.q || '')) {
      notCount++;
      notRightLetters[ans] = (notRightLetters[ans] || 0) + 1;
    }
    for (const c of q.choices) {
      const len = (c.text || c).length;
      allLens.push(len);
      if (c.letter === ans) correctLens.push(len);
      else distractorLens.push(len);
    }
  }
  const tot = mc.length;
  const pct = n => ((n / tot) * 100).toFixed(0) + '%';
  const mean = arr => arr.length ? Math.round(arr.reduce((a, b) => a + b, 0) / arr.length) : 0;
  return {
    n: tot,
    letterDist: Object.entries(letters).map(([k, v]) => `${k}=${v} (${pct(v)})`).join(' '),
    maxLetterPct: Math.max(...Object.values(letters)) / tot,
    choiceCounts,
    notQuestions: notCount,
    notRightLetters,
    meanCorrectLen: mean(correctLens),
    meanDistractorLen: mean(distractorLens),
    lenRatio: ((mean(correctLens) / mean(distractorLens)) || 0),
  };
}

const reports = [];
for (const exam of PE.exams) {
  reports.push({ label: `PRACTICE · ${exam.id}`, stats: analyze(exam.id, adaptPractice(exam)) });
}

console.log('='.repeat(80));
console.log('QUESTION BIAS AUDIT — multiple-choice only');
console.log('='.repeat(80));
let overallPass = true;
for (const r of reports) {
  console.log('\n' + r.label);
  console.log('  N questions:        ', r.stats.n);
  console.log('  Letter dist:        ', r.stats.letterDist);
  console.log('  Choices/Q:          ', JSON.stringify(r.stats.choiceCounts));
  console.log('  NOT/EXCEPT Qs:      ', r.stats.notQuestions, ' answers:', JSON.stringify(r.stats.notRightLetters));
  console.log('  Mean correct len:   ', r.stats.meanCorrectLen, 'chars');
  console.log('  Mean distractor len:', r.stats.meanDistractorLen, 'chars');
  console.log('  Len ratio:          ', r.stats.lenRatio.toFixed(2), '(want 1.0–1.4)');
  const letterFlag = r.stats.maxLetterPct > 0.30 ? ' ❌ FAIL' : (r.stats.maxLetterPct > 0.23 ? ' ⚠️  warn' : ' ✓');
  const lenFlag = r.stats.lenRatio > 1.4 ? ' ❌ FAIL' : (r.stats.lenRatio > 1.3 ? ' ⚠️  warn' : ' ✓');
  console.log('  Letter clustering:   max', (r.stats.maxLetterPct*100).toFixed(0) + '%' + letterFlag);
  console.log('  Length ratio:       ', lenFlag);
  if (r.stats.maxLetterPct > 0.30 || r.stats.lenRatio > 1.4) overallPass = false;
}

console.log('\n' + '='.repeat(80));
console.log(overallPass ? '✓ All variations pass bias thresholds' : '❌ One or more variations fail — debias before deploy');
console.log('='.repeat(80));

// Write a markdown report
const mdLines = ['# Question Bias Audit', '', '| Variation | N | Letter dist | NOT Qs | Correct len | Distractor len | Ratio |', '|---|---|---|---|---|---|---|'];
for (const r of reports) {
  mdLines.push(`| ${r.label} | ${r.stats.n} | ${r.stats.letterDist} | ${r.stats.notQuestions} | ${r.stats.meanCorrectLen} | ${r.stats.meanDistractorLen} | ${r.stats.lenRatio.toFixed(2)} |`);
}
mdLines.push('');
mdLines.push(overallPass ? '**✓ All variations pass bias thresholds**' : '**❌ One or more variations fail bias thresholds — debias required**');
fs.writeFileSync(path.join(ROOT, 'question-bias-audit.md'), mdLines.join('\n'), 'utf8');
console.log('\nWrote question-bias-audit.md');

process.exit(overallPass ? 0 : 1);
