"""Stage C frame (heldout/criteria.md): every result note's detected features and word count, metadata only.
Exclusions come from existing records: the v3 frame's exclusions, v3's drawn held-out notes, the writing set-aside.

    python3 frame.py        -> stageC/heldout/frame.tsv; prints counts only
"""
import csv
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
EVAL = HERE.parents[2]                      # eval/consolidate
sys.path.insert(0, str(HERE.parents[4] / "skills" / "consolidate" / "scripts"))
import kn  # noqa: E402  (frozen v4)

V = Path("/mnt/a/Obsidian Vault/Michael.md")
DIRS = ["Apps/Research/Results", "PhD/Proposal/Research/Results", "PhD/biblion/research/results",
        "Topics/Biology/Research/Results"]
SIZE = re.compile(r"\b(quick|standard|deep)\b(?:[- ](?:run|size|research))|\bsize\b\W{0,4}(quick|standard|deep)|"
                  r"(three-agent|two-agent|single-agent|one agent|deep-research harness|harness)", re.I)


def exclusions():
    out = {}
    for r in csv.DictReader(open(EVAL / "heldout" / "frame.tsv", encoding="utf-8", newline=""), delimiter="\t"):
        if r["excluded"].strip():
            out[r["path"]] = f"v3 frame: {r['excluded'].strip()}"
    for p in re.findall(r"\*\*DRAWN\*\* (.+?\.md)", (EVAL / "heldout" / "draw.md").read_text(encoding="utf-8")):
        for part in p.split(" + "):
            out[part] = "v3 held-out"
    for p in re.findall(r"^- (.+?\.md) \(\d+ words\)", (EVAL / "writing-setaside" / "setaside.md")
                        .read_text(encoding="utf-8"), re.M):
        for part in p.split(" + "):
            out[part] = "writing set-aside"
    return out


def main():
    ex = exclusions()
    rows = []
    for d in DIRS:
        for p in sorted((V / d).rglob("*.md")):
            rel = str(p.relative_to(V))
            full = p.read_text(encoding="utf-8", errors="replace")
            f, _ = kn.detect(p)
            m = SIZE.search(full[:6000])
            size = (m.group(1) or m.group(2) or m.group(3)).lower() if m else ""
            rows.append({"path": rel, "id": f["id"] or "", "words": len(full.split()), "critique": f["critique"],
                         "citations": f["citations"], "labels": f["standing labels"], "answers": f["answers section"],
                         "run": f["run record"], "size_hint": size, "excluded": ex.get(rel, "")})
    out = HERE.parent / "heldout" / "frame.tsv"
    with open(out, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]), delimiter="\t")
        w.writeheader()
        w.writerows(rows)
    missing = sorted(set(ex) - {r["path"] for r in rows})
    by = {k: sum(r["excluded"].startswith(k) for r in rows) for k in ("v3 frame", "v3 held-out", "writing set-aside")}
    print(f"{len(rows)} notes; excluded {sum(bool(r['excluded']) for r in rows)} "
          f"({', '.join(f'{k} {n}' for k, n in by.items())}); eligible {sum(not r['excluded'] for r in rows)}")
    if missing:
        print(f"excluded paths not found in the vault: {missing}")


if __name__ == "__main__":
    main()
