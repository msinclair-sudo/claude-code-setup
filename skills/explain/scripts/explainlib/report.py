"""One report folder:

    <dir>/brief.md         audience, message, sources, delivery
         storyboard.yaml   tier, tier_reason, segments (the plan; lint before building)
         claims.yaml       every number and factual statement, with its source
         tokens.json       colours, fonts, layout concept (copied from templates, then edited)
         src/              what the model writes for this tier (page.md, figures.py, slides.html, scene.py)
         build/            rendered output
         checks/           stills, contact sheets, round-N.json
         static/           publishable fallback (passes static_check)
"""
import os
from dataclasses import dataclass, field
from pathlib import Path

import yaml

SKILL = Path(os.environ.get("EXPLAIN_SKILL", Path(__file__).resolve().parents[2]))
TEMPLATES = SKILL / "templates"
TIERS = {0: "note", 1: "figures", 2: "slides", 3: "interactive", 4: "animation"}


@dataclass
class Report:
    dir: Path
    story: dict = field(default_factory=dict)
    claims: list = field(default_factory=list)
    tokens: dict = field(default_factory=dict)

    @property
    def tier(self) -> int:
        return int(self.story.get("tier", 0))

    @property
    def segments(self) -> list:
        return self.story.get("segments") or []

    def p(self, *parts) -> Path:
        return self.dir.joinpath(*parts)

    def claim(self, cid):
        return next((c for c in self.claims if c.get("id") == cid), None)


def load(d) -> Report:
    d = Path(d).resolve()
    r = Report(d)
    sb, cl, tk = d / "storyboard.yaml", d / "claims.yaml", d / "tokens.json"
    if sb.exists():
        r.story = yaml.safe_load(sb.read_text()) or {}
    if cl.exists():
        r.claims = (yaml.safe_load(cl.read_text()) or {}).get("claims") or []
    if tk.exists():
        from . import theme
        r.tokens = theme.load(tk)
    return r


def words(s) -> int:
    return len(str(s or "").split())
