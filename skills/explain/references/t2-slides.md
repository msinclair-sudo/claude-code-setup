# Tier 2: stepped slides (reveal.js 6, optional narration)

## Rules
- **One idea per slide, a visual on every slide**, at most 12 words of text on it. A slide of bullets is a page; make it tier 1.
- **Build in the order of the explanation:** a fragment appears when the narration reaches it (signalling, temporal contiguity). Each fragment is a storyboard segment with its `step`.
- **Layouts:** `<div class="x-split">` puts the visual left (60%) and its label right; `<div class="x-visual">` gives one visual the slide. Vary the layout across the deck.
- **No accent lines under titles, no decorative stripes or icons**; colour comes from the data and the one accent.
- **Narration (`--voice`)** is for steps that are mainly pictures. Captions are always on. The reader can pause (P) and step by hand.
- **Never leave overflow:** text that wraps or spills is the commonest slide fault; `x check` measures every step.

## Cheat sheet (verified on reveal.js 6.0.2, 2026-10-20)

- **One self-contained file.** `templates/deck.html` inlines `dist/reveal.css` and `dist/reveal.js` from `$REPORT_HOME/vendor/reveal.js-6.0.2/`. Narration clips sit beside it in `audio/`.
- **Never a bundled reveal theme:** `theme/simple.css` and others `@import` Google Fonts. Style comes from `theme.css(tokens)` only.
- **Steps:** each `<section>` is a slide; `class="fragment"` adds a build step inside it. A step's key is `"h.v.f"` (`f` = -1 before the first fragment), from `Reveal.getIndices()`.
- **Narration:** `window.EXPLAIN_AUDIO = {"1.0.0": {"src": "audio/x.m4a", "text": "..."}}`. `templates/narrate.js` shows the text as a caption on every step (always on), plays the clip after the reader presses Start (browsers block sound before a click), and advances when the clip ends. `P` pauses and resumes; arrow keys step by hand.
- **Clips:** `explainlib.tts.clip(text, out_dir, name)` gives a −16 LUFS AAC `.m4a` and its length; cached by text, voice, speed and model.
- **Offline:** opened from `file://` the deck made no network requests (Playwright logged every request).
- **Stills:** in Playwright, after load call `Reveal.configure({transition: 'none'})`; screenshots taken mid-fade show the previous slide as a ghost. Step with `ArrowRight`, screenshot each step.
- **Handout:** load `deck.html?print-pdf`, wait about 800 ms, `page.pdf(width="1280px", height="720px", print_background=True)`.
- **Reduced motion:** the template turns transitions off under `prefers-reduced-motion`.
- **Fragments with a hash URL:** `fragmentInURL: true` lets a reviewer link a step.
