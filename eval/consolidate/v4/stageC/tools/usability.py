"""Stage C usability re-test (heldout/criteria.md): sealed key, writer folders by blind name, collection, the owner's
blank sheets. The key is written by script and never printed.

    python3 usability.py key                 -> usability/ab-key.sealed.md (seed 20261042)
    python3 usability.py folders <k>         writer folders for topic T<k>, named by piece (T<k>-<n><L>), each holding
                                             only its input: the result note(s) (raw) or writers-view.md (view)
    python3 usability.py collect <k>         piece.md and notes.md from each folder -> usability/pieces/
    python3 usability.py sheets              the owner's packet -> <vault>/temp/stage-C/
"""
import random
import re
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
S = HERE.parent
U = S / "usability"
VAULT = Path("/mnt/a/Obsidian Vault/Michael.md")
WORK = Path("/home/rabbit/.claude/jobs/8eb2ff87/tmp/buildC/U")
SEED = 20261042
KEY = U / "ab-key.sealed.md"
sys.path.insert(0, str(HERE.parents[4] / "skills" / "consolidate" / "scripts"))


def topics():
    """[(k, ID, result-note path)] from topics.md."""
    t = (U / "topics.md").read_text(encoding="utf-8")
    return [(int(k), i, p) for k, i, p in re.findall(r"## T(\d): .*?\n\n- Chosen: \*\*(C-[A-Z]+)\*\*, category \d: `(.+?)`",
                                                     t, re.S)]


def pieces():
    for k, _, _ in topics():
        for n in (1, 2):
            for L in "AB":
                yield f"T{k}-{n}{L}"


def cmd_key():
    if KEY.exists():
        sys.exit("the key exists; it is written once")
    rng = random.Random(SEED)
    L = [f"# Sealed key (seed {SEED}). Do not open until the owner has graded all 12 pieces.\n",
         "| Piece | Input |", "|---|---|"]
    for k, _, _ in topics():
        for n in (1, 2):
            raw_is_a = rng.random() < 0.5
            L.append(f"| T{k}-{n}A | {'raw' if raw_is_a else 'view'} {n} |")
            L.append(f"| T{k}-{n}B | {'view' if raw_is_a else 'raw'} {n} |")
    KEY.write_text("\n".join(L) + "\n", encoding="utf-8")
    print("key written (not shown)")


def _key():
    return dict(re.findall(r"\| (T\d-\d[AB]) \| (raw|view) \d \|", KEY.read_text(encoding="utf-8")))


def cmd_folders(k):
    import kn
    k = int(k)
    (_, nid, raw), = [t for t in topics() if t[0] == k]
    rel = (S / "heldout" / nid / "vault-path.txt").read_text(encoding="utf-8").strip()
    view = U / f"T{k}.view.md"
    kn.view(VAULT / rel, view)
    key = _key()
    for p in [p for p in pieces() if p.startswith(f"T{k}-")]:
        d = WORK / p
        d.mkdir(parents=True, exist_ok=False)
        if key[p] == "raw":
            for part in raw.split(" + "):
                shutil.copy(VAULT / part, d / Path(part).name)
        else:
            shutil.copy(view, d / "writers-view.md")
    print(f"T{k}: 4 writer folders under {WORK}")


def cmd_collect(k):
    out = U / "pieces"
    out.mkdir(exist_ok=True)
    for p in [p for p in pieces() if p.startswith(f"T{k}-")]:
        shutil.copy(WORK / p / "piece.md", out / f"{p}.md")
        shutil.copy(WORK / p / "notes.md", out / f"{p}.notes.md")
        print(p, len((out / f"{p}.md").read_text(encoding="utf-8").split()), "words")


SHEET = """Piece: {p} (topic: {topic})

A1 Accuracy            _ /3
A2 Calibration         _ /3
A3 Access phrasing     _ /3
A4 Absences qualified  _ /3
A5 Opposing evidence   _ /3
A6 Scope and breadth   _ /3
A7 Attribution         _ /3
A8 Depth and coverage  _ /3
A9 Stands alone        _ /3
A10 Usefulness         _ /3
Total                  _ /30

B1 Reference list      Yes / Partly / No
B2 Tables for numbers  Yes / Partly / No
B3 Cognitive load      Yes / Partly / No
B4 Prose quality       Yes / Partly / No
B5 Ambiguity flagged   Yes / Partly / No

Errors (quote each sentence):
-

Notes:
"""

PAIR = """Pair: {topic}, writer {n} (pieces {k}-{n}A and {k}-{n}B)
Preferred: A / B / no preference
Confidence: low / medium / high
Why (one or two sentences):
"""


def cmd_sheets():
    names = dict(re.findall(r"^\| (T\d) \| (.+?) \|$", (U / "protocol.md").read_text(encoding="utf-8"), re.M))
    out = VAULT / "temp" / "stage-C"
    out.mkdir(parents=True, exist_ok=False)
    for p in pieces():
        shutil.copy(U / "pieces" / f"{p}.md", out / f"{p}.md")
        (out / f"{p}.sheet.md").write_text(SHEET.format(p=p, topic=names[p[:2]]), encoding="utf-8")
    for k, _, _ in topics():
        for n in (1, 2):
            (out / f"T{k}-pair{n}.sheet.md").write_text(PAIR.format(topic=names[f"T{k}"], n=n, k=f"T{k}"),
                                                        encoding="utf-8")
    shutil.copy(U / "marking-scheme.md", out / "marking-scheme.md")
    print(f"{len(list(out.iterdir()))} files -> {out}")


if __name__ == "__main__":
    a = sys.argv[1:]
    {"key": cmd_key, "folders": lambda: cmd_folders(a[1]), "collect": lambda: cmd_collect(a[1]),
     "sheets": cmd_sheets}[a[0]]()
