"""Tests for kn.py on a synthetic vault: python3 scripts/tests/test_kn.py"""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

KN = Path(__file__).resolve().parents[1] / "kn.py"
sys.path.insert(0, str(KN.parent))
import kn  # noqa: E402

LABELLED = """---
tags: [research, result]
---
> [!abstract] Note Role
> **Contains**: The returned literature review for AB-01 of [[brief]].

> [!danger] Critic: answers partly supported
> - **D1**: Copy number explains part of PCR bias in one mock only.
> - The review calls the ordering strong; it rests on one dataset.

> [!quote] Answers as delivered
> **D1**: Copy number explains about 60% of PCR bias (Lee 2019) [FT; model; single].

# Review

## 1. Copy number

Genomes carry 1 to 15 copies (Ray 2015) [FT; meas; repl]. Correction worsened fit in ten mocks (Kay 2021) [FT; meas; single].

## 2. More

""" + " ".join(f"Finding number {i} was seen once (Lee 2019) [FT; meas; single]." for i in range(8)) + """

## References

Lee 2019. Lee, A. (2019). A title. J 1: 1. https://doi.org/10.1/a [FT]
"""

PLAIN = """# A review

> [!warning] No adversarial pass was run
> One agent, no critic.

## 1. Findings

Rates vary from 1 to 5 t per hectare [1]. Supply is not limited [2].

## Verdict

Lime is not scarce at current rates. Energy cost is small.

## References

1. Smith, A. (2020). Lime. J 2: 3.
"""


def knowledge(inputs, concepts, extra="", table=None, oos=""):
    rows = table or ""
    return f"""---
type: knowledge
title: Test
inputs:
{inputs}
built: 2026-10-21
status: draft
---
# Test

## Inputs
| id | note | critique | citations | standing labels | run record | omission check |
|---|---|---|---|---|---|---|
{rows}

## Concepts
{concepts}

## Do not say
{extra}

## Gaps

## Out of scope
{oos}

## Sources
```bibtex
@article{{leeTitleWords2019, author = {{Lee, A.}}, title = {{A title}}, journal = {{J}}, year = {{2019}}, note = {{access: full_text}}}}
@article{{rayGenomesCopies2015, author = {{Ray, B.}}, title = {{Genomes}}, journal = {{J}}, year = {{2015}}, note = {{access: full_text}}}}
```
"""


class KnTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.v = Path(self.tmp.name)
        (self.v / ".obsidian").mkdir()
        (self.v / "R").mkdir()
        (self.v / "R" / "lab.md").write_text(LABELLED)
        (self.v / "R" / "plain.md").write_text(PLAIN)

    def tearDown(self):
        self.tmp.cleanup()

    def lint(self, text):
        p = self.v / "K.md"
        p.write_text(text)
        r = subprocess.run([sys.executable, str(KN), "lint", str(p)], capture_output=True, text=True)
        return r.returncode, r.stdout + r.stderr

    def test_detect_paths(self):
        f, inv = kn.detect(self.v / "R" / "lab.md")
        self.assertEqual(f["id"], "AB-01")
        self.assertTrue(f["citations"].startswith("labelled"))
        self.assertTrue(f["omission check"].startswith("exact"))
        self.assertEqual(sum(1 for x in inv if x["id"].startswith("I-")), 11)   # ten body, one answer
        f2, inv2 = kn.detect(self.v / "R" / "plain.md", "LIME")
        self.assertEqual(f2["critique"], "no (the note says none ran)")
        self.assertEqual(f2["citations"], "none found")   # two citations: too few to name a style
        self.assertTrue(f2["omission check"].startswith("fallback"))
        self.assertEqual([x["text"] for x in inv2 if not x["id"].startswith("B-")],
                         ["Lime is not scarce at current rates.",
                                                     "Energy cost is small."])

    def _plain(self, concepts, oos="- LIME:A-001..002: test"):
        row = "| LIME | [[plain]] | no (the note says none ran) | none found | no | no | fallback |"
        return knowledge("  - LIME: R/plain.md", concepts, table=row, oos=oos)

    def test_not_stated_passes_and_inferred_fails(self):
        ok = "### lime: Lime\nneeds: none\n- **lime.1** Lime is not scarce at current rates.\n" \
             "  conf: not stated · class: not stated · holds: current rates · src: leeTitleWords2019 · " \
             "trail: LIME §Verdict · from: LIME:A-001..002"
        code, out = self.lint(self._plain(ok, oos=""))
        self.assertEqual(code, 0, out)
        bad = ok.replace("conf: not stated", "conf: repl")
        code, out = self.lint(self._plain(bad, oos=""))
        self.assertIn("needs its basis", out)
        quoted = ok.replace("conf: not stated", 'conf: repl (note: "replicated widely")')
        code, out = self.lint(self._plain(quoted, oos=""))
        self.assertIn("not in any input note", out)

    def test_groups_for_mutual_needs(self):
        claim = "- **{c}.1** X.\n  conf: not stated · class: not stated · holds: h · src: leeTitleWords2019 · " \
                "trail: LIME §1 · from: LIME:A-00{n}"
        mutual = ("### a: A\nneeds: b\ngroup: ab\n" + claim.format(c="a", n=1) +
                  "\n### b: B\nneeds: a\ngroup: ab\n" + claim.format(c="b", n=2))
        code, out = self.lint(self._plain(mutual, oos=""))
        self.assertEqual(code, 0, out)
        code, out = self.lint(self._plain(mutual.replace("group: ab\n", ""), oos=""))
        self.assertIn("depend on each other", out)
        order = ("### b: B\nneeds: a\n" + claim.format(c="b", n=2) + "\n### a: A\nneeds: none\n" +
                 claim.format(c="a", n=1))
        code, out = self.lint(self._plain(order, oos=""))
        self.assertIn("valid ordering", out)

    def test_omission_and_inputs_table(self):
        c = "### lime: Lime\nneeds: none\n- **lime.1** Lime is not scarce.\n  conf: not stated · class: not stated · " \
            "holds: h · src: leeTitleWords2019 · trail: LIME §Verdict · from: LIME:A-001"
        code, out = self.lint(self._plain(c, oos=""))
        self.assertIn("1 of 2 items not accounted for: A-002", out)
        wrong = knowledge("  - LIME: R/plain.md", c, table="| LIME | [[plain]] | yes | none found | no | no | exact |",
                          oos="- LIME:A-002: test")
        code, out = self.lint(wrong)
        self.assertIn("critique is 'yes'", out)
        self.assertIn("omission check is 'exact'", out)

    def test_labelled_marker_basis_and_index(self):
        f, inv = kn.detect(self.v / "R" / "lab.md")
        ids = [x["id"] for x in inv if not x["id"].startswith("B-")]
        row = ("| AB-01 | [[lab]] | yes | labelled (access; class; standing) | yes (11 of 11 labels) | no | exact |")
        c = ("### copy: Copy number\nneeds: none\n- **copy.1** Genomes carry 1 to 15 copies.\n"
             "  conf: repl (marker) · class: meas (marker) · holds: genomes · src: rayGenomesCopies2015 (repl) · "
             "trail: AB-01 §1. Copy · from: AB-01:I-0002")
        oos = "- " + ", ".join(f"AB-01:{i}" for i in ids if i != "I-0002") + ": test"
        code, out = self.lint(knowledge("  - AB-01: R/lab.md", c, table=row, oos=oos))
        self.assertEqual(code, 0, out)
        idx = json.loads((self.v / "K.index.json").read_text())
        self.assertEqual(idx["entries"][0]["trail_links"], ["[[R/lab#1. Copy number]]"])
        self.assertEqual(idx["checks"]["omission"]["AB-01"]["accounted"], len(ids))


    def test_label_forms_verdict_callout_and_abbreviations(self):
        note = ("# R\n\n> [!quote] Verdict\n> Lime is cheap at St. Luce farms in most years.\n\n## Body\n\n"
                + " ".join(f"Finding {i} holds widely here [Kim2012; FT; measured; SINGLE SOURCE]." for i in range(10))
                + "\n\n## Reference list\n\nKim2012. Kim, A. (2012). T. J 1: 1. [FT]\n")
        (self.v / "R" / "h2.md").write_text(note)
        f, inv = kn.detect(self.v / "R" / "h2.md", "H2")
        self.assertTrue(f["citations"].startswith("labelled"), f)
        self.assertEqual(f["answers section"], "yes")
        self.assertIn("Lime is cheap at St. Luce farms in most years.", [x["text"] for x in inv])
        self.assertEqual(sum(1 for x in inv if x["id"].startswith("I-")), 10)
        self.assertFalse(any("Kim, A." in x["text"] for x in inv))      # the reference list is not inventoried

    def test_from_none_critic_basis_rating_and_body_addresses(self):
        base = "### lime: Lime\nneeds: none\n- **lime.1** Rates vary from 1 to 5 t per hectare.\n" \
               "  conf: not stated · class: not stated · holds: h · src: leeTitleWords2019 · trail: LIME §1 · from: {f}"
        code, out = self.lint(self._plain(base.format(f="none (body)")))
        self.assertIn("from: none", out)
        _, inv = kn.detect(self.v / "R" / "plain.md", "LIME")
        b = next(x["id"] for x in inv if x["text"].startswith("Rates vary"))
        code, out = self.lint(self._plain(base.format(f=f"LIME:{b}")))
        self.assertEqual(code, 0, out)
        rated = base.format(f=f"LIME:{b}").replace("holds: h", 'holds: h · rating: "One agent"')
        code, out = self.lint(self._plain(rated))
        self.assertEqual(code, 0, out)
        code, out = self.lint(self._plain(rated.replace('"One agent"', '"Strong"')))
        self.assertIn('rating "Strong" is not in any input note', out)
        crit = base.format(f=f"LIME:{b}").replace("conf: not stated", "conf: single (critic: C-009)")
        code, out = self.lint(self._plain(crit))
        self.assertIn("basis LIME:C-009 is not in the inventory", out)


if __name__ == "__main__":
    unittest.main(verbosity=1)
