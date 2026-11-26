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

  // Hero slider: crossfade + zoom, arrows, dots, swipe, autoplay (paused on hover / hidden tab)
  // Optional hero photos: shown only if the image file exists, otherwise the drawn background stays.
  document.querySelectorAll('.slide-bg[data-photo]').forEach(function (bg) {
    var img = new Image();
    img.onload = function () { bg.style.backgroundImage = 'url(' + bg.getAttribute('data-photo') + ')'; bg.classList.add('has-photo'); var a = bg.parentNode.querySelector('.slide-art'); if (a) a.style.display = 'none'; };
    img.src = bg.getAttribute('data-photo');
  });
  var hero = document.querySelector('.hero');
  if (hero) {
    var slides = hero.querySelectorAll('.slide');
    var dotsWrap = hero.querySelector('.hero-dots');
    var current = 0, timer = null, DELAY = 6000;
    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    slides.forEach(function (_, i) {
      var b = document.createElement('button');
      b.type = 'button'; b.setAttribute('aria-label', 'Show slide ' + (i + 1));
      b.addEventListener('click', function () { go(i); restart(); });
      dotsWrap.appendChild(b);
    });
    var dots = dotsWrap.querySelectorAll('button');
    function go(n) {
      slides[current].classList.remove('is-active'); slides[current].setAttribute('aria-hidden', 'true');
      dots[current].classList.remove('is-active');
      current = (n + slides.length) % slides.length;
      slides[current].classList.add('is-active'); slides[current].removeAttribute('aria-hidden');
      dots[current].classList.add('is-active');
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
    slides.forEach(function (s, i) { if (i) s.setAttribute('aria-hidden', 'true'); });
    slides[0].classList.add('is-active'); dots[0].classList.add('is-active');
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
