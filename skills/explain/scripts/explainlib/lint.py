"""Storyboard and claims lint: the plan must hold before anything is built.

Caps are heuristics drawn from the evidence (references/design-rules.md):
on-screen text <= 12 words (coherence, redundancy), narration <= 35 words per
segment and about 20 per sentence (long transient narration loses the modality gain),
animation <= 10 min in chapters, pauses included (references/narration.md).
"""
import re

from .report import TIERS, words

ONSCREEN_MAX, LABEL_MAX, NARRATION_MAX = 16, 4, 35   # onscreen: labels separated by ';'
ANIM_MINUTES_MAX, WPM, SENTENCE_MAX = 10, 155, 22
CELL = re.compile(r"^[A-F][1-4]$")
STEP = re.compile(r"^\d+\.\d+\.-?\d+$")
KINDS = {"quoted", "derived", "illustrative"}
ROLES = ("setting", "mechanism", "problem", "distil", "resolution", "limits")


def lint(r) -> list:
    """[(level, message)] with level 'error' or 'warn'."""
    out = []
    err = lambda m: out.append(("error", m))
    warn = lambda m: out.append(("warn", m))
    s = r.story
    if not s:
        return [("error", "storyboard.yaml missing or empty")]
    for k in ("title", "message", "audience", "delivery", "tier"):
        if not s.get(k) and s.get(k) != 0:
            err(f"storyboard: '{k}' is required")
    if s.get("tier") not in TIERS:
        err(f"storyboard: tier must be one of {sorted(TIERS)}")
        return out
    t = int(s["tier"])
    if t > 0 and not str(s.get("tier_reason") or "").strip():
        err(f"storyboard: tier {t} needs tier_reason (why the tier below would not carry the message)")
    if s.get("delivery") not in ("read", "presented"):
        err("storyboard: delivery is 'read' (self-paced) or 'presented' (system-paced)")
    if t == 4 and s.get("delivery") == "read":
        err("tier 4 animates for a system-paced, narrated presentation; for self-paced reading use tier 1 or 3")
    if words(s.get("message")) > 30:
        warn("storyboard: message is over 30 words; it should be one sentence a reader can repeat")

    claim_ids = {c.get("id") for c in r.claims}
    for c in r.claims:
        cid = c.get("id") or "?"
        if not c.get("text"):
            err(f"claims {cid}: 'text' (as shown or spoken) is required")
        if not c.get("source"):
            err(f"claims {cid}: 'source' is required (file:line, DOI, or the query that produced it)")
        if c.get("kind") not in KINDS:
            err(f"claims {cid}: kind is one of {sorted(KINDS)}")

    segs = r.segments
    if t >= 2 and not segs:
        err("storyboard: segments are required from tier 2 up")
    from .tts import PACING, pause_for
    for k, v in (s.get("pacing") or {}).items():
        if k not in PACING or not isinstance(v, (int, float)) or not 0 <= v <= 6:
            err(f"storyboard: pacing.{k} = {v}; keys are {', '.join(PACING)}, in seconds (0 to 6)")
    pacing = {**PACING, **(s.get("pacing") or {})}
    for g in segs:
        v = g.get("pause_after")
        if v is not None and (not isinstance(v, (int, float)) or not 0 <= v <= 6):
            err(f"segment {g.get('id')}: pause_after is seconds, 0 to 6")
    roles = [g.get("role") for g in segs]
    for g in segs:
        if g.get("role") and g["role"] not in ROLES:
            err(f"segment {g.get('id')}: role is one of {', '.join(ROLES)}")
    if t >= 2 and segs and roles[0] != "setting":
        warn("storyboard: the first segment should set the scene (role: setting): what the system is and "
             "how it was measured, before the problem")
    ids, steps, narr_words = set(), set(), 0
    for i, g in enumerate(segs):
        sid = g.get("id") or f"#{i + 1}"
        if sid in ids:
            err(f"segment {sid}: duplicate id")
        ids.add(sid)
        if not g.get("visual"):
            err(f"segment {sid}: 'visual' says what is drawn")
        if words(g.get("onscreen")) > ONSCREEN_MAX:
            err(f"segment {sid}: on-screen text is {words(g.get('onscreen'))} words; at most {ONSCREEN_MAX}")
        for lab in str(g.get("onscreen") or "").split(";"):
            nw = sum(1 for w in lab.split() if re.search(r"[A-Za-z]", w))   # numbers and arrows are not words to read
            if nw > LABEL_MAX:   # a sentence on screen is the narration read off a slide
                (err if t == 4 else warn)(f"segment {sid}: on-screen label '{lab.strip()}' is {nw} words; "
                                          f"labels name things in at most {LABEL_MAX} words, the voice says the rest")
        n = words(g.get("narration"))
        narr_words += n
        if n > NARRATION_MAX:
            err(f"segment {sid}: narration is {n} words; at most {NARRATION_MAX} (split the segment)")
        for sent in re.split(r"(?<=[.!?])\s+", (g.get("narration") or "").strip()):
            if words(sent) > SENTENCE_MAX:
                warn(f"segment {sid}: a {words(sent)}-word sentence; keep spoken sentences to about 20 words")
        on = re.sub(r"[^a-z0-9 ]", "", str(g.get("onscreen") or "").lower()).strip()
        if on and len(on.split()) >= 4 and on in re.sub(r"[^a-z0-9 ]", "", str(g.get("narration") or "").lower()):
            warn(f"segment {sid}: on-screen text repeats the narration word for word; show key words, reworded")
        for cid in g.get("claims") or []:
            if cid not in claim_ids:
                err(f"segment {sid}: claim '{cid}' is not in claims.yaml")
        if t == 2:
            st = str(g.get("step") or "")
            if not STEP.match(st):
                err(f"segment {sid}: tier 2 needs step 'h.v.f' (f = -1 before any fragment)")
            elif st in steps:
                err(f"segment {sid}: step {st} used twice")
            steps.add(st)
            if s.get("voice") and not g.get("narration"):
                warn(f"segment {sid}: no narration on a narrated deck; the step will be silent")
        if t == 4:
            if not g.get("scene"):
                err(f"segment {sid}: tier 4 needs 'scene' (the Manim class that plays it)")
            if not g.get("narration"):
                err(f"segment {sid}: tier 4 segments are narrated")
            for name, cell in (g.get("anchors") or {}).items():
                if not CELL.match(str(cell)):
                    err(f"segment {sid}: anchor {name}={cell}; cells are A1..F4 (6 columns, 4 rows)")
            if not g.get("verify"):
                warn(f"segment {sid}: no 'verify' list; overlap and hold checks will be all it gets")
            sync = g.get("sync")
            if not sync:
                warn(f"segment {sid}: no 'sync'; declare each event the narration names (id: a phrase from "
                     "the narration) so the render can check it starts when the phrase is spoken")
            elif not isinstance(sync, dict):
                err(f"segment {sid}: sync is a mapping, event id: phrase from the narration")
            else:
                from .timing import find
                from .tts import sentences
                for name, phrase in sync.items():
                    try:
                        find(sentences(g.get("narration") or ""), str(phrase))
                    except ValueError as e:
                        err(f"segment {sid}: sync {name}: {e} (and stays inside one sentence)")
    if t == 3:
        n = int(s.get("controls", 0) or 0)
        if n > 2:
            err(f"storyboard: {n} controls; at most 2 (few readers touch any)")
        if not s.get("default_view"):
            err("storyboard: tier 3 needs 'default_view': what the page shows before anyone touches it")
    if t == 4:
        chapters = {}
        for g in segs:
            chapters.setdefault(g.get("scene"), []).append(g)
        quiet = sum(pause_for(g, pacing, chapter_end=g is gs[-1]) for gs in chapters.values() for g in gs)
        minutes = narr_words / WPM + quiet / 60
        tol = s.get("sync_tolerance")
        if tol is not None and (not isinstance(tol, (int, float)) or not 0.1 <= tol <= 2):
            err(f"storyboard: sync_tolerance = {tol}; seconds, 0.1 to 2 (default 0.5)")
        cap = float(s.get("max_minutes") or ANIM_MINUTES_MAX)
        if cap > ANIM_MINUTES_MAX and not str(s.get("length_reason") or "").strip():
            err(f"storyboard: max_minutes {cap:g} is over {ANIM_MINUTES_MAX}; say why in length_reason")
        if minutes > cap:
            err(f"narration and pauses come to about {minutes:.1f} min; at most {cap:g} (cut, or split the video)")
        for sc, gs in chapters.items():
            if len(gs) >= 3 and not any(g.get("role") == "distil" for g in gs):
                warn(f"chapter {sc}: {len(gs)} segments and no distil line; restate the idea before moving on")
        for sc, gs in list(chapters.items())[1:]:
            if not str(gs[0].get("question") or "").strip():
                warn(f"chapter {sc}: its first segment {gs[0].get('id')} has no 'question': the question the last chapter "
                     "left the viewer with, which this one answers (say it, or set it up, in the narration)")
    return out
