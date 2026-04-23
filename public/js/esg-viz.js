/* ESG Interactive Visualizations — Exam 1 & 2 diagrams
 * window.ESG_VIZ.init(el) walks the element, finds [data-viz], runs handler.
 * Each handler is idempotent (guard via el.dataset.vizInit === '1').
 */
(function(){
  'use strict';

  var handlers = {};

  function reg(name, fn){ handlers[name] = fn; }
  function q(el, sel){ return el.querySelector(sel); }
  function qa(el, sel){ return Array.prototype.slice.call(el.querySelectorAll(sel)); }

  // Normal distribution helper (unscaled Gaussian)
  function gauss(x, mu, sig){ var z=(x-mu)/sig; return Math.exp(-0.5*z*z); }

  // Build an SVG path for a curve y(x) on a grid
  function curvePath(xs, ys, xmap, ymap){
    var d=''; for (var i=0;i<xs.length;i++){ d += (i?'L':'M') + xmap(xs[i]) + ',' + ymap(ys[i]); } return d;
  }

  // ───────────────────────────────────────────────────────────────
  // 1. Selection types (stabilizing / directional / disruptive)
  // ───────────────────────────────────────────────────────────────
  reg('selection-types', function(root){
    var btns = qa(root, '[data-mode]');
    var before = q(root, '#sel-before');
    var after = q(root, '#sel-after');
    var caption = q(root, '#sel-caption');
    var W=320, H=120, PAD=20;

    var modes = {
      stabilizing: {
        before: function(x){ return gauss(x, 0, 1.4); },
        after:  function(x){ return gauss(x, 0, 0.65) * 1.0; },
        label: 'Stabilizing — extremes culled, mean unchanged, variance ↓'
      },
      directional: {
        before: function(x){ return gauss(x, 0, 1.2); },
        after:  function(x){ return gauss(x, 1.0, 1.0); },
        label: 'Directional — mean shifts toward favored extreme'
      },
      disruptive: {
        before: function(x){ return gauss(x, 0, 1.3); },
        after:  function(x){ return (gauss(x, -1.2, 0.6) + gauss(x, 1.2, 0.6))*0.5; },
        label: 'Disruptive — intermediates culled, variance ↑, bimodal'
      }
    };

    function build(mode){
      var xs=[], n=80;
      for (var i=0;i<=n;i++) xs.push(-3 + 6*i/n);
      function xmap(x){ return PAD + (W-2*PAD) * (x+3)/6; }
      function ymap(y){ return H - PAD - (H-2*PAD) * y; }
      var ybs = xs.map(mode.before);
      var yas = xs.map(mode.after);
      var maxY = Math.max.apply(null, ybs.concat(yas));
      ybs = ybs.map(function(y){ return y/maxY; });
      yas = yas.map(function(y){ return y/maxY; });
      var pb = curvePath(xs, ybs, xmap, ymap) + ' L '+xmap(3)+','+ymap(0)+' L '+xmap(-3)+','+ymap(0)+' Z';
      var pa = curvePath(xs, yas, xmap, ymap) + ' L '+xmap(3)+','+ymap(0)+' L '+xmap(-3)+','+ymap(0)+' Z';
      before.setAttribute('d', pb);
      after.setAttribute('d', pa);
      caption.textContent = mode.label;
    }

    btns.forEach(function(b){
      b.addEventListener('click', function(){
        btns.forEach(function(x){ x.classList.remove('on'); });
        b.classList.add('on');
        build(modes[b.dataset.mode]);
      });
    });
    build(modes.stabilizing);
    if (btns[0]) btns[0].classList.add('on');
  });

  // ───────────────────────────────────────────────────────────────
  // 2. Breeder's Equation R = h² × S (parent-offspring regression)
  // ───────────────────────────────────────────────────────────────
  reg('breeders-eq', function(root){
    var h2slider = q(root, '[data-range=h2]');
    var h2val = q(root, '[data-val=h2]');
    var sval = q(root, '[data-val=S]');
    var rval = q(root, '[data-val=R]');
    var regLine = q(root, '#be-line');
    var points = qa(root, '.be-pt');
    var meanOff = q(root, '#be-meanoff');
    var selArrow = q(root, '#be-sel-arrow');
    var W=300, H=200, PAD=34;
    var mu=50, sd=10, S=10; // selection differential fixed at +10

    function regress(h2){
      // center at (mu,mu). Slope = h2. Offspring mean of breeders = mu + h2*S
      var xs=[], ys=[];
      // Deterministic jitter for reproducibility
      var seed=42;
      function rnd(){ seed = (seed*9301 + 49297) % 233280; return seed/233280; }
      for (var i=0;i<30;i++){
        var x = mu + (rnd()-0.5)*sd*4;
        var noise = (rnd()-0.5)*sd*2*(1-h2);
        var y = mu + h2*(x-mu) + noise;
        xs.push(x); ys.push(y);
      }
      return {xs:xs, ys:ys};
    }

    function xmap(x){ return PAD + (W-2*PAD)*(x-20)/60; }
    function ymap(y){ return H - PAD - (H-2*PAD)*(y-20)/60; }

    function render(h2){
      var d = regress(h2);
      points.forEach(function(pt, i){
        if (i < d.xs.length){
          pt.setAttribute('cx', xmap(d.xs[i]));
          pt.setAttribute('cy', ymap(d.ys[i]));
          pt.setAttribute('opacity', 0.75);
        } else {
          pt.setAttribute('opacity', 0);
        }
      });
      // Regression line through (mu, mu) with slope h2
      var x0 = 20, x1 = 80;
      var y0 = mu + h2*(x0-mu);
      var y1 = mu + h2*(x1-mu);
      regLine.setAttribute('x1', xmap(x0)); regLine.setAttribute('y1', ymap(y0));
      regLine.setAttribute('x2', xmap(x1)); regLine.setAttribute('y2', ymap(y1));
      // Mean offspring of breeders (breeders chosen at mu+S)
      var R = h2 * S;
      meanOff.setAttribute('cx', xmap(mu+S));
      meanOff.setAttribute('cy', ymap(mu+R));
      selArrow.setAttribute('y1', ymap(mu));
      selArrow.setAttribute('y2', ymap(mu+R));
      selArrow.setAttribute('x1', xmap(mu+S));
      selArrow.setAttribute('x2', xmap(mu+S));

      h2val.textContent = h2.toFixed(2);
      sval.textContent = '+' + S;
      rval.textContent = (R>=0?'+':'') + R.toFixed(1);
    }

    if (h2slider){
      h2slider.addEventListener('input', function(){ render(parseFloat(h2slider.value)); });
      render(parseFloat(h2slider.value || 0.5));
    }
  });

  // ───────────────────────────────────────────────────────────────
  // 3. Genetic drift simulation (Wright-Fisher)
  // ───────────────────────────────────────────────────────────────
  reg('drift-sim', function(root){
    var run = q(root, '[data-action=run]');
    var reset = q(root, '[data-action=reset]');
    var Nslider = q(root, '[data-range=N]');
    var Nval = q(root, '[data-val=N]');
    var svg = q(root, 'svg');
    var plot = q(root, '#drift-plot');
    var W=320, H=160, PAD=28;
    var lines = [];

    function clear(){
      while (plot.firstChild) plot.removeChild(plot.firstChild);
      lines = [];
    }
    function addLine(color){
      var p = document.createElementNS('http://www.w3.org/2000/svg','path');
      p.setAttribute('fill','none'); p.setAttribute('stroke', color); p.setAttribute('stroke-width', 1.4);
      p.setAttribute('opacity', 0.7);
      plot.appendChild(p);
      lines.push({el:p, pts:[]});
      return lines[lines.length-1];
    }
    function xmap(t){ return PAD + (W-2*PAD)*t/100; }
    function ymap(p){ return H - PAD - (H-2*PAD)*p; }

    function sim(N, nlines){
      clear();
      var colors = ['#f5c542','#7cc4ff','#34d399','#f87171','#b197fc','#fbbf24'];
      for (var k=0;k<nlines;k++){
        var L = addLine(colors[k % colors.length]);
        var p = 0.5;
        L.pts.push([0,p]);
        for (var t=1;t<=100;t++){
          // Binomial sampling: count of A alleles among 2N draws
          var count=0;
          for (var i=0;i<2*N;i++){ if (Math.random() < p) count++; }
          p = count/(2*N);
          L.pts.push([t,p]);
        }
        var d=''; L.pts.forEach(function(pt,i){ d += (i?'L':'M') + xmap(pt[0]) + ',' + ymap(pt[1]); });
        L.el.setAttribute('d', d);
      }
    }

    if (Nslider){
      Nslider.addEventListener('input', function(){ Nval.textContent = Nslider.value; });
      Nval.textContent = Nslider.value;
    }
    if (run) run.addEventListener('click', function(){ sim(parseInt(Nslider.value,10), 6); });
    if (reset) reset.addEventListener('click', clear);
    sim(20, 6);
  });

  // ───────────────────────────────────────────────────────────────
  // 4. Hardy-Weinberg interactive
  // ───────────────────────────────────────────────────────────────
  reg('hwe', function(root){
    var pslider = q(root, '[data-range=p]');
    var pval = q(root, '[data-val=p]');
    var qval = q(root, '[data-val=q]');
    var aaVal = q(root, '[data-val=AA]');
    var AaVal = q(root, '[data-val=Aa]');
    var aaHom = q(root, '[data-val=aa]');
    var barAA = q(root, '#hwe-AA');
    var barAa = q(root, '#hwe-Aa');
    var baraa = q(root, '#hwe-aa');
    var BW = 240, BH = 160, BP = 28;

    function render(p){
      var qv = 1-p;
      var pAA = p*p, pAa = 2*p*qv, paa = qv*qv;
      var base = BH - BP;
      var hAA = pAA * (BH - 2*BP);
      var hAa = pAa * (BH - 2*BP);
      var haa = paa * (BH - 2*BP);
      barAA.setAttribute('height', hAA); barAA.setAttribute('y', base - hAA);
      barAa.setAttribute('height', hAa); barAa.setAttribute('y', base - hAa);
      baraa.setAttribute('height', haa); baraa.setAttribute('y', base - haa);
      pval.textContent = p.toFixed(2);
      qval.textContent = qv.toFixed(2);
      aaVal.textContent = pAA.toFixed(3);
      AaVal.textContent = pAa.toFixed(3);
      aaHom.textContent = paa.toFixed(3);
    }
    if (pslider){
      pslider.addEventListener('input', function(){ render(parseFloat(pslider.value)); });
      render(parseFloat(pslider.value || 0.5));
    }
  });

  // ───────────────────────────────────────────────────────────────
  // 5. Allele dose response: dominant / recessive / additive
  // ───────────────────────────────────────────────────────────────
  reg('allele-dose', function(root){
    var btns = qa(root, '[data-dose]');
    var line = q(root, '#dose-line');
    var dots = qa(root, '.dose-pt');
    var caption = q(root, '#dose-caption');
    var W=280, H=160, PAD=36;
    // x: 0 (aa), 1 (Aa), 2 (AA); y: phenotype 0-10
    function xmap(x){ return PAD + (W-2*PAD)*x/2; }
    function ymap(y){ return H - PAD - (H-2*PAD)*y/10; }
    var modes = {
      dominant:  { y:[0,10,10], label:'Dominant — one copy of A gives full phenotype (Aa ≈ AA)' },
      recessive: { y:[0, 0,10], label:'Recessive — needs two copies to express (aa-like until AA)' },
      additive:  { y:[0, 5,10], label:'Additive — each copy adds equal increment; Aa midpoint' }
    };
    function apply(mode){
      var pts = modes[mode].y;
      var d = 'M '+xmap(0)+','+ymap(pts[0])+' L '+xmap(1)+','+ymap(pts[1])+' L '+xmap(2)+','+ymap(pts[2]);
      line.setAttribute('d', d);
      dots.forEach(function(dot, i){
        dot.setAttribute('cx', xmap(i));
        dot.setAttribute('cy', ymap(pts[i]));
      });
      caption.textContent = modes[mode].label;
    }
    btns.forEach(function(b){
      b.addEventListener('click', function(){
        btns.forEach(function(x){ x.classList.remove('on'); });
        b.classList.add('on');
        apply(b.dataset.dose);
      });
    });
    apply('additive');
    btns.forEach(function(b){ if (b.dataset.dose === 'additive') b.classList.add('on'); });
  });

  // ───────────────────────────────────────────────────────────────
  // 6. Reaction norms: flat / parallel / G×E
  // ───────────────────────────────────────────────────────────────
  reg('reaction-norms', function(root){
    var btns = qa(root, '[data-rn]');
    var g1 = q(root, '#rn-g1');
    var g2 = q(root, '#rn-g2');
    var caption = q(root, '#rn-caption');
    var W=280, H=160, PAD=30;
    function xmap(x){ return PAD + (W-2*PAD)*x; }
    function ymap(y){ return H - PAD - (H-2*PAD)*y; }
    var modes = {
      flat:     { a:[0.5,0.5], b:[0.7,0.7], label:'Flat — no plasticity; phenotype constant across environments' },
      parallel: { a:[0.2,0.9], b:[0.4,0.7], label:'Parallel slopes — plasticity without G×E (same response, different means)' },
      'gxe':    { a:[0.2,0.9], b:[0.9,0.2], label:'G×E crossing — genotypes rank-reverse; no universal best' }
    };
    function apply(mode){
      var m = modes[mode];
      g1.setAttribute('d', 'M '+xmap(0)+','+ymap(m.a[0])+' L '+xmap(1)+','+ymap(m.a[1]));
      g2.setAttribute('d', 'M '+xmap(0)+','+ymap(m.b[0])+' L '+xmap(1)+','+ymap(m.b[1]));
      caption.textContent = m.label;
    }
    btns.forEach(function(b){
      b.addEventListener('click', function(){
        btns.forEach(function(x){ x.classList.remove('on'); });
        b.classList.add('on');
        apply(b.dataset.rn);
      });
    });
    apply('flat');
    btns.forEach(function(b){ if (b.dataset.rn === 'flat') b.classList.add('on'); });
  });

  // ───────────────────────────────────────────────────────────────
  // 7. Aging curves — antagonistic pleiotropy vs mutation accumulation
  // ───────────────────────────────────────────────────────────────
  reg('aging-curves', function(root){
    var btns = qa(root, '[data-aging]');
    var curveFit = q(root, '#aging-fit');
    var curveSel = q(root, '#aging-sel');
    var caption = q(root, '#aging-caption');
    var W=300, H=170, PAD=36;
    function xmap(a){ return PAD + (W-2*PAD)*a/80; }
    function ymap(v){ return H - PAD - (H-2*PAD)*v; }
    function build(ages, fitness, selection){
      var df = ''; ages.forEach(function(a,i){ df += (i?'L':'M') + xmap(a) + ',' + ymap(fitness[i]); });
      var ds = ''; ages.forEach(function(a,i){ ds += (i?'L':'M') + xmap(a) + ',' + ymap(selection[i]); });
      curveFit.setAttribute('d', df);
      curveSel.setAttribute('d', ds);
    }
    var ages = []; for (var i=0;i<=80;i+=4) ages.push(i);
    var modes = {
      'mutation-accum': {
        fitness: ages.map(function(a){ return Math.max(0, 1 - Math.pow(a/70,3)); }),
        selection: ages.map(function(a){ return Math.max(0.02, Math.exp(-a/18)); }),
        label: 'Mutation Accumulation: selection strength collapses with age → late-acting deleterious alleles drift to fixation'
      },
      'antag-pleio': {
        fitness: ages.map(function(a){ return a<25 ? 1 + 0.15*Math.sin(a/8) : Math.max(0, 1.0 - Math.pow((a-20)/60,2.2)); }),
        selection: ages.map(function(a){ return Math.max(0.02, Math.exp(-a/18)); }),
        label: 'Antagonistic Pleiotropy: SAME allele boosts early fitness but harms late — net positive selection despite late cost'
      }
    };
    function apply(mode){ var m = modes[mode]; build(ages, m.fitness, m.selection); caption.textContent = m.label; }
    btns.forEach(function(b){
      b.addEventListener('click', function(){
        btns.forEach(function(x){ x.classList.remove('on'); });
        b.classList.add('on');
        apply(b.dataset.aging);
      });
    });
    apply('mutation-accum');
    btns.forEach(function(b){ if (b.dataset.aging === 'mutation-accum') b.classList.add('on'); });
  });

  // ───────────────────────────────────────────────────────────────
  // 8. Bateman gradient
  // ───────────────────────────────────────────────────────────────
  reg('bateman', function(root){
    // Static slopes — nothing dynamic required, pure CSS hover is enough.
    // Hook retained to mark initialized.
  });

  // ───────────────────────────────────────────────────────────────
  // 9. Hamilton's rule calculator
  // ───────────────────────────────────────────────────────────────
  reg('hamilton', function(root){
    var rSlider = q(root, '[data-range=r]');
    var bSlider = q(root, '[data-range=B]');
    var cSlider = q(root, '[data-range=C]');
    var rVal = q(root, '[data-val=r]');
    var bVal = q(root, '[data-val=B]');
    var cVal = q(root, '[data-val=C]');
    var rbVal = q(root, '[data-val=rB]');
    var verdict = q(root, '[data-val=verdict]');
    var verdictLine = q(root, '#ham-verdict');
    function update(){
      var r = parseFloat(rSlider.value);
      var B = parseFloat(bSlider.value);
      var C = parseFloat(cSlider.value);
      rVal.textContent = r.toFixed(2);
      bVal.textContent = B.toFixed(1);
      cVal.textContent = C.toFixed(1);
      var rB = r*B;
      rbVal.textContent = rB.toFixed(2);
      var pass = rB > C;
      verdict.textContent = pass ? 'rB > C ✓ altruism favored' : 'rB ≤ C ✗ altruism NOT favored';
      verdict.style.color = pass ? 'var(--green)' : 'var(--red)';
      if (verdictLine){
        verdictLine.setAttribute('fill', pass ? 'rgba(52,211,153,.12)' : 'rgba(248,113,113,.10)');
        verdictLine.setAttribute('stroke', pass ? 'var(--green)' : 'var(--red)');
      }
    }
    [rSlider,bSlider,cSlider].forEach(function(s){ if (s) s.addEventListener('input', update); });
    update();
  });

  // ───────────────────────────────────────────────────────────────
  // 10. Twofold cost of sex
  // ───────────────────────────────────────────────────────────────
  reg('twofold-cost', function(root){
    var step = q(root, '[data-action=step]');
    var resetBtn = q(root, '[data-action=reset]');
    var genVal = q(root, '[data-val=gen]');
    var sexVal = q(root, '[data-val=sex]');
    var asexVal = q(root, '[data-val=asex]');
    var barSex = q(root, '#tc-sex-bar');
    var barAsex = q(root, '#tc-asex-bar');
    var labelS = q(root, '#tc-sex-label');
    var labelA = q(root, '#tc-asex-label');
    var state = { g:0, s:10, a:1 };
    var BH = 120, BP = 10;
    function render(){
      genVal.textContent = state.g;
      sexVal.textContent = state.s;
      asexVal.textContent = state.a;
      var max = Math.max(state.s, state.a);
      var hS = (state.s/max) * (BH - 2*BP);
      var hA = (state.a/max) * (BH - 2*BP);
      barSex.setAttribute('height', hS);
      barSex.setAttribute('y', BH - BP - hS);
      barAsex.setAttribute('height', hA);
      barAsex.setAttribute('y', BH - BP - hA);
      labelS.setAttribute('y', BH - BP - hS - 6);
      labelA.setAttribute('y', BH - BP - hA - 6);
      labelS.textContent = state.s;
      labelA.textContent = state.a;
    }
    function advance(){
      // Sexual: half female, each female 2 offspring → same count
      // Asexual: everyone produces 2 offspring → doubles
      state.g++;
      state.s = state.s;  // flat under twofold cost baseline
      state.a = state.a * 2;
      render();
    }
    if (step) step.addEventListener('click', advance);
    if (resetBtn) resetBtn.addEventListener('click', function(){ state = { g:0, s:10, a:1 }; render(); });
    render();
  });

  // ───────────────────────────────────────────────────────────────
  // Dispatcher
  // ───────────────────────────────────────────────────────────────
  function initOne(el){
    if (el.dataset.vizInit === '1') return;
    var name = el.getAttribute('data-viz');
    if (!name) return;
    var fn = handlers[name];
    if (!fn) return;
    fn(el);
    el.dataset.vizInit = '1';
  }

  window.ESG_VIZ = {
    init: function(scope){
      // If scope itself has data-viz, init it; otherwise walk descendants.
      if (!scope) scope = document;
      if (scope.getAttribute && scope.getAttribute('data-viz')){ initOne(scope); return; }
      qa(scope, '[data-viz]').forEach(initOne);
    },
    register: reg
  };
})();
