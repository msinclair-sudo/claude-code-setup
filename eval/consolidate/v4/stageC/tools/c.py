"""Stage C, held-out builds: the frozen stage B procedure (two checkers per 60-entry packet, a fault from either
counted; one fresh re-checker per round), rooted at stageC/heldout/<ID>/. A thin wrapper over stageB/tools/rebuild.py.

    python3 c.py prep <ID> <vault-relative knowledge note>   as-built.md, vault-path.txt, packets/ (hints), verdicts-a|b/
    python3 c.py first <ID>                                  -> first-pass.md, fixes-1.md
    python3 c.py repack <ID> <n>                             -> recheck-<n>/ for the entries in fixes-<n>.md
    python3 c.py recheck <ID> <n>                            after recheck-<n>/verdicts.md -> fixes-<n+1>.md if any
    python3 c.py final <ID>                                  -> final.md
    python3 c.py measures <ID> [<ID> ...]                    near-copy and real-setting shares of claims (v4 only)
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
B = HERE.parents[1] / "stageB" / "tools"
sys.path.insert(0, str(B))
import notestats  # noqa: E402
import rebuild  # noqa: E402

ROOT = HERE.parent / "heldout"


def d(nid):
    return ROOT / nid


def rel(nid):
    return (d(nid) / "vault-path.txt").read_text(encoding="utf-8").strip()


def prep(nid, path):
    for sub in ("verdicts-a", "verdicts-b"):
        (d(nid) / sub).mkdir(parents=True, exist_ok=True)
    src = rebuild.VAULT / path
    (d(nid) / "as-built.md").write_bytes(src.read_bytes())
    (d(nid) / "vault-path.txt").write_text(path + "\n", encoding="utf-8")
    rebuild.kn().packets(src, d(nid) / "packets", with_hints=True)


def repack(nid, n):
    ids = [ln.split(":", 1)[0] for ln in (d(nid) / f"fixes-{n}.md").read_text(encoding="utf-8").splitlines()
           if rebuild.LINE.match(ln)]
    rebuild.kn().packets(rebuild.VAULT / rel(nid), d(nid) / f"recheck-{n}", only=set(ids), with_hints=True)


def final(nid):
    (d(nid) / "final.md").write_bytes((rebuild.VAULT / rel(nid)).read_bytes())
    print(f"{nid}: final.md saved")


def measures(ids):
    print("| Note | Claims | With a real setting | Near-copies |\n|---|---|---|---|")
    for nid in ids:
        s = notestats.stats(notestats.load(d(nid) / "as-built.md", notestats.kn4))
        print(f"| {nid} | {s['claims']} | {s['setting']} ({s['setting'] / s['claims']:.0%}) | "
              f"{s['near']} ({s['near'] / s['claims']:.0%}) |")


if __name__ == "__main__":
    a = sys.argv[1:]
    {"prep": lambda: prep(a[1], a[2]), "first": lambda: rebuild.cmd_first(d(a[1])),
     "repack": lambda: repack(a[1], a[2]), "recheck": lambda: rebuild.cmd_recheck(d(a[1]), a[2]),
     "final": lambda: final(a[1]), "measures": lambda: measures(a[1:])}[a[0]]()
