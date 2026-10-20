// Narration for a reveal.js deck: one clip per step (slide or fragment).
// window.EXPLAIN_AUDIO maps "h.v.f" (f = -1 before any fragment) to {src, text}.
// Captions always show. Sound starts only after the reader presses Start
// (browsers block it before), then each clip advances the deck when it ends
// (system-paced). P pauses or resumes; arrow keys still step by hand.
(function () {
  var map = window.EXPLAIN_AUDIO || {};
  var cap = document.getElementById('x-caption');
  var overlay = document.getElementById('x-start');
  var audio = new Audio();
  var auto = false;

  function key() {
    var i = Reveal.getIndices();
    return i.h + '.' + (i.v || 0) + '.' + (i.f === undefined ? -1 : i.f);
  }
  function step() {
    var e = map[key()];
    audio.pause();
    cap.textContent = e ? e.text : '';
    if (e && auto) { audio.src = e.src; audio.play().catch(function () {}); }
  }
  audio.addEventListener('ended', function () {
    if (!auto) return;
    if (Reveal.isLastSlide() && !Reveal.availableFragments().next) return;
    setTimeout(function () { Reveal.next(); }, 700);
  });
  if (overlay) {
    overlay.querySelector('button').addEventListener('click', function () {
      auto = true; overlay.remove(); step();
    });
  }
  document.addEventListener('keydown', function (ev) {
    if (ev.key === 'p' || ev.key === 'P') {
      auto = !auto;
      if (auto) step(); else audio.pause();
    }
  });
  Reveal.on('ready', step);
  Reveal.on('slidechanged', step);
  Reveal.on('fragmentshown', step);
  Reveal.on('fragmenthidden', step);
})();
