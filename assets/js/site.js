/* O.J. Ekoja & Co. — site behaviour: header, mobile menu, hero slider, scroll animations, forms. */
(function () {
  'use strict';
  var root = document.documentElement;

  // Header shadow on scroll
  var header = document.querySelector('.site-header');
  function onScroll() { if (header) header.classList.toggle('scrolled', window.scrollY > 10); }
  window.addEventListener('scroll', onScroll, { passive: true }); onScroll();

  // Mobile menu
  var toggle = document.querySelector('.menu-toggle');
  if (toggle) {
    toggle.addEventListener('click', function () {
      var open = document.body.classList.toggle('menu-open');
      toggle.setAttribute('aria-expanded', open);
    });
    document.querySelectorAll('.nav a').forEach(function (a) {
      a.addEventListener('click', function () { document.body.classList.remove('menu-open'); toggle.setAttribute('aria-expanded', false); });
    });
    window.addEventListener('resize', function () { if (window.innerWidth > 991) document.body.classList.remove('menu-open'); });
  }

  // Hero slider. Each slide's photo is assembled from a 5x5 grid of tiles that fly in and
  // come together (as on the reference's slider), then the headline letters gather into place.
  var hero = document.querySelector('.hero');
  if (hero) {
    var slides = Array.prototype.slice.call(hero.querySelectorAll('.slide'));
    var current = -1, timer = null, busy = false, DELAY = 7500;
    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // Split each headline into letters so they can converge individually.
    slides.forEach(function (s) {
      var h = s.querySelector('.letters');
      if (!h) return;
      var text = h.textContent, i = 0;
      h.setAttribute('aria-label', text);
      h.textContent = '';
      text.split(' ').forEach(function (word, w) {
        var wspan = document.createElement('span');
        wspan.className = 'word'; wspan.setAttribute('aria-hidden', 'true');
        word.split('').forEach(function (ch) {
          var c = document.createElement('span');
          c.className = 'ch'; c.textContent = ch;
          c.style.setProperty('--x', Math.round((Math.random() - 0.5) * 220) + 'px');
          c.style.setProperty('--y', Math.round((Math.random() - 0.5) * 160) + 'px');
          c.style.setProperty('--r', Math.round((Math.random() - 0.5) * 70) + 'deg');
          c.style.setProperty('--d', (0.05 + i++ * 0.045).toFixed(3) + 's');
          wspan.appendChild(c);
        });
        if (w) h.appendChild(document.createTextNode(' '));
        h.appendChild(wspan);
      });
    });

    // Load each slide photo; remember its size so tiles can match the 'cover' crop exactly.
    function loadPhoto(bg) {
      return new Promise(function (resolve) {
        var src = bg.getAttribute('data-photo');
        if (!src) return resolve(false);
        var img = new Image();
        img.onload = function () {
          bg.style.backgroundImage = 'url(' + src + ')';
          bg.dataset.w = img.naturalWidth; bg.dataset.h = img.naturalHeight;
          bg.classList.add('has-photo');
          var art = bg.parentNode.querySelector('.slide-art'); if (art) art.style.display = 'none';
          resolve(true);
        };
        img.onerror = function () { resolve(false); };
        img.src = src;
      });
    }
    var loaded = slides.map(function (s) { var bg = s.querySelector('.slide-bg'); return bg ? loadPhoto(bg) : Promise.resolve(false); });

    function assemble(slide, done) {
      var bg = slide.querySelector('.slide-bg');
      if (reduce || !bg.classList.contains('has-photo')) return done();
      var W = hero.clientWidth, H = hero.clientHeight;
      var cs = getComputedStyle(bg), overlay = getComputedStyle(bg, '::after').backgroundImage;
      var iw = +bg.dataset.w, ih = +bg.dataset.h, k = Math.max(W / iw, H / ih), sw = iw * k, sh = ih * k;
      var pos = cs.backgroundPosition.split(' ');
      var px = parseFloat(pos[0]) / 100, py = parseFloat(pos[1] || '50%') / 100;
      var ox = (W - sw) * px, oy = (H - sh) * py;
      var COLS = 5, ROWS = 5, tw = W / COLS, th = H / ROWS, longest = 0;
      var layer = document.createElement('div');
      layer.className = 'tiles';
      for (var r = 0; r < ROWS; r++) {
        for (var c = 0; c < COLS; c++) {
          var t = document.createElement('div'), x = c * tw, y = r * th;
          t.style.cssText = 'left:' + x + 'px;top:' + y + 'px;width:' + Math.ceil(tw + 1) + 'px;height:' + Math.ceil(th + 1) + 'px;' +
            'background-image:' + overlay + ',' + cs.backgroundImage + ';' +
            'background-size:' + W + 'px ' + H + 'px,' + sw + 'px ' + sh + 'px;' +
            'background-position:' + (-x) + 'px ' + (-y) + 'px,' + (ox - x) + 'px ' + (oy - y) + 'px';
          layer.appendChild(t);
          // Tiles start pushed outwards from the centre and converge to their place.
          var dx = (c - (COLS - 1) / 2) * 90 + (Math.random() - 0.5) * 60;
          var dy = (r - (ROWS - 1) / 2) * 70 + (Math.random() - 0.5) * 60;
          var delay = Math.random() * 500, dur = 900;
          longest = Math.max(longest, delay + dur);
          t.animate([
            { opacity: 0, transform: 'translate(' + dx + 'px,' + dy + 'px) scale(.35) rotate(' + ((Math.random() - 0.5) * 30) + 'deg)' },
            { opacity: 1, transform: 'none' }
          ], { duration: dur, delay: delay, easing: 'cubic-bezier(.2,.7,.2,1)', fill: 'both' });
        }
      }
      hero.appendChild(layer);
      setTimeout(function () { done(); requestAnimationFrame(function () { layer.remove(); }); }, longest + 40);
    }

    function go(n) {
      if (busy) return;
      n = (n + slides.length) % slides.length;
      if (n === current) return;
      busy = true;
      var prev = current >= 0 ? slides[current] : null;
      var next = slides[n];
      current = n;
      if (prev) { prev.classList.remove('is-active'); prev.classList.add('is-leaving'); prev.setAttribute('aria-hidden', 'true'); }
      loaded[n].then(function () {
        assemble(next, function () {
          next.classList.add('is-active'); next.removeAttribute('aria-hidden');
          if (prev) prev.classList.remove('is-leaving');
          busy = false;
        });
      });
    }
    function restart() { clearInterval(timer); if (!reduce && slides.length > 1) timer = setInterval(function () { go(current + 1); }, DELAY); }
    hero.querySelector('.prev').addEventListener('click', function () { go(current - 1); restart(); });
    hero.querySelector('.next').addEventListener('click', function () { go(current + 1); restart(); });
    hero.addEventListener('mouseenter', function () { clearInterval(timer); });
    hero.addEventListener('mouseleave', restart);
    document.addEventListener('visibilitychange', function () { document.hidden ? clearInterval(timer) : restart(); });
    var x0 = null;
    hero.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
    hero.addEventListener('touchend', function (e) {
      if (x0 === null) return; var dx = e.changedTouches[0].clientX - x0; x0 = null;
      if (Math.abs(dx) > 50) { go(current + (dx < 0 ? 1 : -1)); restart(); }
    });
    slides.forEach(function (s) { s.setAttribute('aria-hidden', 'true'); });
    go(0);
    restart();
  }

  // Scroll animations: [data-anim] fades up when it enters the viewport.
  // Siblings marked data-stagger on the parent get 0.2s steps (as on the reference).
  document.querySelectorAll('[data-stagger]').forEach(function (group) {
    var step = parseFloat(group.getAttribute('data-stagger')) || 0.2;
    Array.prototype.forEach.call(group.children, function (el, i) {
      if (!el.hasAttribute('data-anim')) el.setAttribute('data-anim', '');
      el.style.setProperty('--delay', (i % 4) * step + 's');
    });
  });
  var pending = Array.prototype.slice.call(document.querySelectorAll('[data-anim]'));
  var ticking = false;
  function reveal() {
    ticking = false;
    var limit = window.innerHeight * 0.9;
    pending = pending.filter(function (el) {
      var r = el.getBoundingClientRect();
      if (r.top < limit && r.bottom > 0) {
        el.classList.add('in');
        el.addEventListener('transitionend', function () { el.classList.add('done'); }, { once: true });
        return false;
      }
      return true;
    });
  }
  function queue() { if (!ticking) { ticking = true; requestAnimationFrame(reveal); } }
  window.addEventListener('scroll', queue, { passive: true });
  window.addEventListener('resize', queue);
  window.addEventListener('load', queue);
  reveal();

  // Forms: no server, so messages open in the visitor's email app or WhatsApp.
  var EMAIL = 'ojekojaandco@gmail.com', WHATSAPP = '2347050308648';
  function collect(form) {
    var lines = [];
    form.querySelectorAll('input, select, textarea').forEach(function (f) {
      if (f.name && f.value.trim()) lines.push((f.getAttribute('data-label') || f.name) + ': ' + f.value.trim());
    });
    return lines.join('\n');
  }
  document.querySelectorAll('form[data-send]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      var via = (e.submitter && e.submitter.value) || form.getAttribute('data-send');
      var text = collect(form);
      if (via === 'whatsapp') {
        window.open('https://wa.me/' + WHATSAPP + '?text=' + encodeURIComponent(text), '_blank', 'noopener');
      } else {
        var subject = form.getAttribute('data-subject') || 'Website enquiry';
        window.location.href = 'mailto:' + EMAIL + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(text);
      }
    });
  });

  var yr = document.getElementById('year'); if (yr) yr.textContent = new Date().getFullYear();
  root.classList.add('js-ready');
})();
