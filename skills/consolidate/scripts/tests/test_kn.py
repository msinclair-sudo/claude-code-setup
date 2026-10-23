"""Tests for kn.py on a synthetic vault: python3 scripts/tests/test_kn.py"""
import json
import re
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


def knowledge(inputs, concepts, extra="", table=None, oos="", gaps=""):
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
{gaps}

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
        self.assertEqual([x["text"] for x in inv2 if x["id"][0] not in "BR"],
                         ["Lime is not scarce at current rates.",
                                                     "Energy cost is small."])

    SECOND = ("- **gap.1** The verdict's figures were never checked by a second reader.\n"
              "  blocks: none · origin: no critique ran · search: not stated")

    def _plain(self, concepts, oos="- LIME:A-001..002: test", gaps=SECOND):
        row = "| LIME | [[plain]] | no (the note says none ran) | none found | no | no | fallback |"
        return knowledge("  - LIME: R/plain.md", concepts, table=row, oos=oos, gaps=gaps)

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
        ids = [x["id"] for x in inv if x["id"][0] not in "BR"]
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
        refs = [x for x in inv if "Kim, A." in x["text"]]                  # the reference list: R addresses only
        self.assertTrue(refs and all(x["id"].startswith("R-") for x in refs))

    def test_from_none_critic_basis_rating_and_body_addresses(self):
        base = "### lime: Lime\nneeds: none\n- **lime.1** Rates vary from 1 to 5 t per hectare.\n" \
               "  conf: not stated · class: not stated · holds: h · src: leeTitleWords2019 · trail: LIME §1 · from: {f}"
        code, out = self.lint(self._plain(base.format(f="none (body)")))
        self.assertIn("from: none", out)
        _, inv = kn.detect(self.v / "R" / "plain.md", "LIME")
        b = next(x["id"] for x in inv if x["text"].startswith("Rates vary"))
        code, out = self.lint(self._plain(base.format(f=f"LIME:{b}")))
        self.assertEqual(code, 0, out)
        b2 = next(x["id"] for x in inv if x["text"].startswith("One agent"))
        rated = base.format(f=f"LIME:{b}").replace("holds: h", 'holds: h · rating: "One agent"')
        code, out = self.lint(self._plain(rated))
        self.assertIn("not in this entry's from text", out)       # in the note, but not in what the checker sees
        rated = rated.replace(f"from: LIME:{b}", f"from: LIME:{b}, LIME:{b2}")
        code, out = self.lint(self._plain(rated))
        self.assertEqual(code, 0, out)
        code, out = self.lint(self._plain(rated.replace('"One agent"', '"Strong"')))
        self.assertIn('rating "Strong" is not in any input note', out)
        crit = base.format(f=f"LIME:{b}").replace("conf: not stated", "conf: single (critic: C-009)")
        code, out = self.lint(self._plain(crit))
        self.assertIn("basis LIME:C-009 is not in the inventory", out)

    def test_bullet_label_covers_bullet_and_repeats_get_addresses(self):
        note = ("# R\n\n## Body\n\n"
                "- Copy number varies by taxon. It ranges from 1 to 15 (Ray 2015) [FT; meas; repl].\n"
                "- One finding (Kay 2021) [FT; meas; single]. Another finding (Lee 2019) [AB; meas; single].\n\n"
                + " ".join(f"Finding {i} holds here (Lee 2019) [FT; meas; single]." for i in range(8))
                + "\n\n*Strength:* Moderate here.\n\n## More\n\n*Strength:* Moderate here.\n")
        (self.v / "R" / "b.md").write_text(note)
        _, inv = kn.detect(self.v / "R" / "b.md", "BB")
        texts = [x["text"] for x in inv if x["id"].startswith("I-")]
        self.assertIn("- Copy number varies by taxon. It ranges from 1 to 15 (Ray 2015) [FT; meas; repl].", texts)
        self.assertIn("Another finding (Lee 2019) [AB; meas; single].", texts)   # two labels: each its own
        self.assertEqual(len(texts), 11)
        strength = [x for x in inv if x["text"] == "*Strength:* Moderate here."]
        self.assertEqual([x["id"][0] for x in strength], ["B", "B"])
        self.assertEqual([x["where"] for x in strength], ["Body", "More"])

    def test_limit_src_correction_trail_comma_and_table_words(self):
        f, inv = kn.detect(self.v / "R" / "lab.md")
        ids = [x["id"] for x in inv if x["id"][0] not in "BR"]
        row = "| AB-01 | [[lab]] | yes | labelled (access; class; standing) | yes (11 of 11 labels) | no | exact |"
        c = ("### copy: Copy number\nneeds: none\n- **copy.1** Genomes carry 1 to 15 copies.\n"
             "  conf: single (critic: C-002) · class: meas (marker) · holds: genomes · "
             'src: rayGenomesCopies2015 (FT; meas; single; critic: C-002 was "FT; meas; repl") · '
             "trail: AB-01 §1. Copy, §2. More · from: AB-01:I-0002 · limit: access (critic: C-001)")
        oos = "- " + ", ".join(f"AB-01:{i}" for i in ids if i != "I-0002") + ": test"
        code, out = self.lint(knowledge("  - AB-01: R/lab.md", c, table=row, oos=oos))
        self.assertEqual(code, 0, out)
        for bad, msg in ((c.replace("critic: C-002 was", "critic: C-077 was"), "src names critic C-077"),
                         (c.replace('was "FT; meas; repl"', 'was "AB; meas; repl"'), "src says the note's label was"),
                         (c.replace("limit: access (critic: C-001)", "limit: weak"), "limit 'weak'"),
                         (c.replace("conf: single (critic: C-002)", 'conf: single (note: "Genomes carry")'),
                          "no word the format's table counts")):
            code, out = self.lint(knowledge("  - AB-01: R/lab.md", bad, table=row, oos=oos))
            self.assertIn(msg, out)

    def test_packets_only_and_spotcheck(self):
        c = "".join(f"- **lime.{n}** Lime is not scarce.\n  conf: not stated · class: not stated · holds: h · "
                    f"src: leeTitleWords2019 · trail: LIME §Verdict · from: LIME:A-00{1 + n % 2}\n" for n in range(1, 6))
        p = self.v / "K.md"
        p.write_text(self._plain("### lime: Lime\nneeds: none\n" + c, oos=""))
        kn.lint(p)
        kn.packets(p, self.v / "pk", only={"lime.2", "lime.4"})
        txt = (self.v / "pk" / "packet-01.md").read_text()
        self.assertEqual(re.findall(r"^## (\S+)", txt, re.M), ["lime.2", "lime.4"])
        kn.spotcheck(p, self.v / "s.md", n=3, seed=7)
        s = (self.v / "s.md").read_text()
        self.assertIn("random.Random(7)", s)
        self.assertEqual(len(re.findall(r"^## \d+\. lime\.\d", s, re.M)), 3)
        self.assertIn("`holds`:", s)                       # the fault kinds come from checker.md
        self.assertIn("trail links: [[R/plain#Verdict]]", s)

    def test_writer_view(self):
        (self.v / "R" / "brief.md").write_text("#### AB-01: copy number\n\n> [!abstract] AGENT BRIEF\n"
                                              "> **Directions:**\n> - **D1.** How much PCR bias does copy number "
                                              "explain?\n\n> [!note] ROUTING\n> - **D2.** project only\n")
        f, inv = kn.detect(self.v / "R" / "lab.md")
        ids = [x["id"] for x in inv if x["id"][0] not in "BR"]
        row = "| AB-01 | [[lab]] | yes | labelled (access; class; standing) | yes (11 of 11 labels) | no | exact |"
        c = ("### copy: Copy number\nneeds: none\n- **copy.1** Genomes carry 1 to 15 copies.\n"
             "  conf: repl (marker) · class: meas (marker) · holds: genomes · src: rayGenomesCopies2015 (repl) · "
             "trail: AB-01 §1. Copy · from: AB-01:I-0002\n"
             "- **copy.2** Correction worsened fit in ten mocks.\n"
             "  conf: single (marker) · class: meas (marker) · holds: ten mocks · src: leeTitleWords2019 · "
             'trail: AB-01 §1. Copy · from: AB-01:I-0003 · rating: "worsened fit" (critic: C-002: rests on one dataset)')
        dns = ('- **dns.1** "Copy number explains about 60% of PCR bias."\n'
               "  why: The critic says copy number explains part of the bias, in one mock only. · instead: copy.1 · "
               "from: AB-01:C-001")
        gaps = ("- **gap.1** Copy number in soil.\n  blocks: copy · origin: critic coverage gap · "
                "search: not searched (critic: C-001) · from: AB-01:C-001")
        oos = "- " + ", ".join(f"AB-01:{i}" for i in ids if i not in ("I-0002", "I-0003", "C-001")) + ": test"
        p = self.v / "K.md"
        p.write_text(knowledge("  - AB-01: R/lab.md", c, extra=dns, table=row, oos=oos, gaps=gaps))
        self.assertEqual(kn.lint(p), 0)
        kn.view(p, self.v / "W.md")
        w = (self.v / "W.md").read_text()
        self.assertIn("**D1. How much PCR bias does copy number explain?**", w)
        self.assertNotIn("project only", w)                       # ROUTING never reaches the view
        self.assertIn("*Answer, as the research gave it; a second reader reviewed it and left it as given.*", w)
        self.assertIn("Copy number explains about 60% of PCR bias (Lee 2019).", w)   # label stripped
        # everything with epistemic weight is content: who, setting, class in words, standing, rating and ruling
        self.assertIn("- Genomes carry 1 to 15 copies. (Ray 2015)\n  Holds for: genomes.\n"
                      "  Evidence: measured; replicated.", w)
        self.assertIn('rated "worsened fit" by the research; a second reader disputes this: rests on one dataset', w)
        self.assertIn('- Do not write: "Copy number explains about 60% of PCR bias."\n  Why: The critic says', w)
        self.assertIn("  Say instead: Genomes carry 1 to 15 copies. (Ray 2015)", w)
        self.assertIn("- Copy number in soil.\n  Not searched for.", w)
        self.assertIn("## References\n\n- Lee, A. (2019). A title. J.\n- Ray, B. (2015). Genomes. J.", w)
        for prov in ("rayGenomesCopies2015", "trail:", "AB-01:I-0002", "C-001", "§"):      # only navigation goes
            self.assertNotIn(prov, w)

    def test_hints_go_to_checker_packets_only(self):
        c = ("### lime: Lime\nneeds: none\n- **lime.1** Lime is not scarce at current Ethiopian rates of 7 t.\n"
             "  conf: not stated · class: not stated · holds: Oregon coastal soils · src: leeTitleWords2019 · "
             "trail: LIME §Verdict · from: LIME:A-001\n"
             "- **lime.2** Energy cost is small.\n  conf: not stated · class: not stated · holds: current rates · "
             "src: leeTitleWords2019 · trail: LIME §Verdict · from: LIME:A-002")
        p = self.v / "K.md"
        p.write_text(self._plain(c, oos=""))
        r = subprocess.run([sys.executable, str(KN), "lint", str(p)], capture_output=True, text=True)
        self.assertNotIn("Not found in the cited text", r.stdout)            # lint never prints hints
        kn.packets(p, self.v / "plain-pk")
        self.assertNotIn("Not found in the cited text", (self.v / "plain-pk" / "packet-01.md").read_text())
        subprocess.run([sys.executable, str(KN), "packets", "--hints", str(p), str(self.v / "pk")], check=True,
                       capture_output=True)
        txt = (self.v / "pk" / "packet-01.md").read_text()
        one, two = txt.split("## lime.2")
        self.assertIn(f"{kn.HINT_LINE}: 7; Ethiopian; holds: oregon; holds: coastal; holds: soils", one)
        self.assertNotIn(kn.HINT_LINE, two)                                  # everything found: no line
        self.assertIn("where to look, not what is wrong", (KN.parents[1] / "references" / "checker.md").read_text())

    def test_detection_misses_fail_loudly(self):
        # a title that starts like a references heading is not one: the body still gets addresses
        note = ("# Sources of functional covariation\n\n## Findings\n\nCovariation is strong in soils. "
                "It is weak in water.\n\n## References\n\n1. Lee, A. (2019). A title. J 1: 1.\n")
        (self.v / "R" / "src.md").write_text(note)
        f, inv = kn.detect(self.v / "R" / "src.md", "SRC")
        self.assertEqual(f["body addresses"], 2)
        self.assertEqual([x["id"][0] for x in inv if "Lee, A." in x["text"]], ["R"])
        # answers under 'Provisional verdicts' and 'Assessment' are answers
        for head in ("## Provisional verdicts (single-pass)", "## Assessment: redundancy holds in soil"):
            (self.v / "R" / "pv.md").write_text(f"# Scout\n\n## Findings\n\nA thing was found.\n\n{head}\n\n"
                                                "Integrate several taxonomies.\n")
            f, inv = kn.detect(self.v / "R" / "pv.md", "PV")
            self.assertTrue(f["omission check"].startswith("fallback"), (head, f))
            self.assertIn("Integrate several taxonomies.", [x["text"] for x in inv if x["id"].startswith("A-")])
        # nothing detected: lint fails unless the answer sections are declared
        (self.v / "R" / "free.md").write_text("# Review\n\n## Sub-claim 1\n\nPangenomes vary.\n\n"
                                              "## Where it lands\n\nThe premise holds in soil.\n")
        c = ("### pan: Pangenome\nneeds: none\n- **pan.1** Pangenomes vary.\n  conf: not stated · class: not stated · "
             "holds: h · src: leeTitleWords2019 · trail: FREE §Sub-claim · from: FREE:B-0001")
        row = "| FREE | [[free]] | no | none found | no | no | not run |"
        k = knowledge("  - FREE: R/free.md", c, table=row, gaps=self.SECOND)
        code, out = self.lint(k)
        self.assertIn("omission check cannot run", out)
        declared = k.replace("built: 2026-10-21", "answers:\n  - FREE: §Where it lands\nbuilt: 2026-10-21")
        declared = declared.replace("| not run |", "| fallback |").replace(
            "## Out of scope\n", "## Out of scope\n- FREE:A-001: test\n")
        code, out = self.lint(declared)
        self.assertNotIn("cannot run", out)
        self.assertIn("omission FREE: fallback, 1/1", out)
        # a section of refuted claims is not a second reader
        (self.v / "R" / "ref.md").write_text("# H\n\n## Verdict\n\nIt works.\n\n## Refuted (killed in verification)\n\n"
                                             "- It always works: killed 3-0.\n")
        f, _ = kn.detect(self.v / "R" / "ref.md", "REF")
        self.assertEqual(f["critique"], "refutations only")
        # an uncritiqued note without the second-reader gap fails
        code, out = self.lint(self._plain("### lime: Lime\nneeds: none\n- **lime.1** Lime is not scarce at current "
                                          "rates.\n  conf: not stated · class: not stated · holds: current rates · "
                                          "src: leeTitleWords2019 · trail: LIME §Verdict · from: LIME:A-001..002",
                                          oos="", gaps=""))
        self.assertIn("never checked by a second reader", out)

    def test_splitter_search_status_rating_and_years(self):
        self.assertEqual(kn.sentences("Shown by J. Smith in 2020. Then Supp. Fig. 3 shows it."),
                         ["Shown by J. Smith in 2020.", "Then Supp. Fig. 3 shows it."])
        base = ("### lime: Lime\nneeds: none\n- **lime.1** No study measured lime supply.\n"
                '  conf: not stated · class: search (note: "Lime is not scarce") · holds: h · src: leeTitleWords2019 · '
                "trail: LIME §Verdict · from: LIME:A-001..002{x}")
        code, out = self.lint(self._plain(base.format(x=""), oos=""))
        self.assertIn("class search needs its search status", out)
        code, out = self.lint(self._plain(base.format(x=" · search: searched, not found"), oos=""))
        self.assertIn("needs its basis", out)
        code, out = self.lint(self._plain(base.format(x=' · search: searched, not found (note: "Lime is not scarce")'),
                                          oos=""))
        self.assertEqual(code, 0, out)
        code, out = self.lint(self._plain(base.format(x=" · search: not stated · contrary: one-sided"), oos=""))
        self.assertIn("one-sided rests on the critic", out)
        code, out = self.lint(self._plain(base.format(x=' · search: not stated · rating: "Energy cost" '
                                                         "(critic: C-009: weak)"), oos=""))
        self.assertIn("rating basis LIME:C-009 is not in the inventory", out)


if __name__ == "__main__":
    unittest.main(verbosity=1)
