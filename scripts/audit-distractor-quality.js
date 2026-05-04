/* Spot-check distractors for accidental correctness or token overlap with the right answer.
   1) Heavy overlap with correct answer (>50% token overlap) — risky paraphrase
   2) Internal contradictions
   3) Length anomalies — distractor much longer/shorter than the rest

   Output: a markdown report flagging each suspect distractor.
*/
const fs = require('fs');
const path = require('path');
const ROOT = path.resolve(__dirname, '..');
const data = JSON.parse(fs.readFileSync(path.join(ROOT, 'public/data/practice-exams.json'), 'utf8'));

function flagsFor(qStem, correctText, distractorText, allLengths) {
  const flags = [];
  const distLower = String(distractorText).toLowerCase();
  const correctLower = String(correctText).toLowerCase();

  // 1) Heavy overlap with correct answer (>50% token overlap on 4+ char tokens)
  const tokens = (s) => new Set(String(s).toLowerCase().match(/\b[a-z]{4,}\b/g) || []);
  const c = tokens(correctText), d = tokens(distractorText);
  const inter = [...c].filter(t => d.has(t));
  const overlap = c.size > 0 ? inter.length / c.size : 0;
  if (overlap > 0.55) flags.push(`OVERLAP: distractor shares ${(overlap*100).toFixed(0)}% of correct-answer tokens (${inter.slice(0,5).join(', ')})`);

  // 2) Length anomaly (>1.7× the median of all 5 choices)
  const median = [...allLengths].sort((a,b) => a-b)[Math.floor(allLengths.length/2)];
  const ratio = String(distractorText).length / Math.max(1, median);
  if (ratio > 1.7) flags.push(`LENGTH-ANOMALY: distractor is ${ratio.toFixed(1)}× the median choice length`);
  if (ratio < 0.4 && median > 30) flags.push(`LENGTH-ANOMALY: distractor is only ${ratio.toFixed(1)}× the median (suspiciously short)`);

  // 3) Internal contradictions on common evolution motifs
  if (/no selection/i.test(distLower) && /(adaptive|fitness advantage|selective pressure)/i.test(distLower))
    flags.push('CONTRADICTION: claims no selection AND mentions selection');
  if (/no drift/i.test(distLower) && /(stochastic|random change|allele.*lost by chance)/i.test(distLower))
    flags.push('CONTRADICTION: claims no drift AND mentions stochastic loss');

  return flags;
}

const allFlags = [];
let totalDistractors = 0;
for (const exam of data.exams) {
  for (const q of exam.mc) {
    const correctIdx = q.ans.charCodeAt(0) - 65;
    const correct = q.choices[correctIdx];
    const allLengths = q.choices.map(c => String(c).length);
    q.choices.forEach((c, i) => {
      if (i === correctIdx) return;
      totalDistractors++;
      const flags = flagsFor(q.q, correct, c, allLengths);
      if (flags.length) {
        allFlags.push({ exam: exam.id, qNum: q.n, qStem: String(q.q).slice(0, 100), distractor: c, correct, flags });
      }
    });
  }
}

console.log(`Total distractors: ${totalDistractors}`);
console.log(`Flagged for review: ${allFlags.length}\n`);

if (allFlags.length === 0) {
  console.log('✓ No risky distractors found.');
} else {
  for (const f of allFlags) {
    console.log(`### ${f.exam} Q${f.qNum}`);
    console.log(`Stem: ${f.qStem}`);
    console.log(`Distractor: "${f.distractor}"`);
    console.log(`Correct:    "${f.correct}"`);
    f.flags.forEach(x => console.log('  FLAG: ' + x));
    console.log();
  }
}

const lines = ['# Distractor Quality Audit', '', `Total distractors: ${totalDistractors} · Flagged: ${allFlags.length}`, ''];
for (const f of allFlags) {
  lines.push(`### ${f.exam} Q${f.qNum}`);
  lines.push(`**Q:** ${f.qStem}`);
  lines.push(`**Distractor:** ${f.distractor}`);
  lines.push(`**Correct:**   ${f.correct}`);
  f.flags.forEach(x => lines.push('- ' + x));
  lines.push('');
}
if (allFlags.length === 0) lines.push('**✓ No risky distractors found.**');
fs.writeFileSync(path.join(ROOT, 'distractor-quality-audit.md'), lines.join('\n'), 'utf8');
console.log('Wrote distractor-quality-audit.md');
process.exit(allFlags.length > 8 ? 1 : 0);
