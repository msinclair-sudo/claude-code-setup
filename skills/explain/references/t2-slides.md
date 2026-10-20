# Tier 2: stepped slides (reveal.js 6, optional narration)

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
