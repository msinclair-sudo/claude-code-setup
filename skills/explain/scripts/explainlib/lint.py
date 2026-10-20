"""Storyboard and claims lint: the plan must hold before anything is built.

Caps are heuristics drawn from the evidence (references/design-rules.md):
on-screen text <= 12 words (coherence, redundancy), narration <= 35 words per
segment (long transient narration loses the modality gain), animation <= 6 min.
"""
import re

from .report import TIERS, words

ONSCREEN_MAX, NARRATION_MAX = 12, 35
ANIM_MINUTES_MAX, WPM = 6, 155
CELL = re.compile(r"^[A-F][1-4]$")
STEP = re.compile(r"^\d+\.\d+\.-?\d+$")
KINDS = {"quoted", "derived", "illustrative"}


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
        n = words(g.get("narration"))
        narr_words += n
        if n > NARRATION_MAX:
            err(f"segment {sid}: narration is {n} words; at most {NARRATION_MAX} (split the segment)")
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
    if t == 3:
        n = int(s.get("controls", 0) or 0)
        if n > 2:
            err(f"storyboard: {n} controls; at most 2 (few readers touch any)")
        if not s.get("default_view"):
            err("storyboard: tier 3 needs 'default_view': what the page shows before anyone touches it")
    if t == 4 and narr_words / WPM > ANIM_MINUTES_MAX:
        err(f"narration is about {narr_words / WPM:.1f} min; at most {ANIM_MINUTES_MAX} (split into chapters)")
    return out
