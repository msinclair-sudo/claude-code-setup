#!/usr/bin/env python3
"""Post-process a pandoc-generated .docx to match the reference document.

Two fixes pandoc cannot make itself:

**Tables.** Pandoc always writes its own `Table` style and styles cell
paragraphs `Compact`, and it ignores a `custom-style` attribute on a Table
element, so a Lua filter cannot redirect it. The template carries the intended
look on its own example table, so that table is read and copied onto every table
in the output: its table style, its `tblLook` (which decides whether the style's
firstRow/firstCol conditional formatting actually renders), and its cell
paragraph style. If the reference doc contains no table, tables are left alone.

Column widths are NOT touched. Pandoc computes them from the Markdown column
widths, which is a better fit for an arbitrary table than the template's single
worked example.

**Unreferenced media.** Pandoc copies `word/media/*` out of the reference doc
wholesale but rebuilds `document.xml.rels` from the document it just wrote, so an
image used only by the template arrives as a bare part nothing points at:
invisible in Word, but still counted in the file size.

Usage: postprocess.py OUTPUT.docx REFERENCE.docx
"""

import os
import re
import sys
import zipfile

TBL_RE = re.compile(r"<w:tbl>.*?</w:tbl>", re.S)
STYLE_RE = re.compile(r'<w:tblStyle w:val="([^"]+)"\s*/>')
LOOK_RE = re.compile(r"<w:tblLook\b[^>]*/>")
PSTYLE_RE = re.compile(r'<w:pStyle w:val="([^"]+)"\s*/>')


def table_spec(reference):
    """Read the intended table look from the reference doc's own table."""
    with zipfile.ZipFile(reference) as z:
        try:
            doc = z.read("word/document.xml").decode("utf-8", "replace")
        except KeyError:
            return None
    match = TBL_RE.search(doc)
    if not match:
        return None
    table = match.group(0)
    style = STYLE_RE.search(table)
    look = LOOK_RE.search(table)
    first_para = re.search(r"<w:p\b.*?</w:p>", table, re.S)
    cell_style = "Normal"
    if first_para:
        found = PSTYLE_RE.search(first_para.group(0))
        if found:
            cell_style = found.group(1)
    if not style:
        return None
    return {
        "style": style.group(1),
        "look": look.group(0) if look else None,
        "cell": cell_style,
    }


def restyle_tables(doc, spec):
    """Apply the reference table's style, tblLook and cell style to every table.

    Markdown cannot produce a nested table, so a non-greedy <w:tbl> scan is safe.
    """
    changed = [0]

    def fix(match):
        table = match.group(0)
        before = table
        table = STYLE_RE.sub(
            '<w:tblStyle w:val="%s"/>' % spec["style"], table, count=1)
        if spec["look"]:
            table = LOOK_RE.sub(lambda _: spec["look"], table, count=1)
        # cell paragraphs: pandoc writes Compact, the template wants its own
        table = PSTYLE_RE.sub(
            lambda m: '<w:pStyle w:val="%s"/>' % spec["cell"]
            if m.group(1) == "Compact" else m.group(0),
            table)
        if table != before:
            changed[0] += 1
        return table

    return TBL_RE.sub(fix, doc), changed[0]


def orphan_media(names, read):
    referenced = set()
    for name in names:
        if name.endswith(".rels"):
            for m in re.finditer(r'Target="(?:\.\./)?(media/[^"]+)"',
                                 read(name).decode("utf-8", "replace")):
                referenced.add("word/" + m.group(1))
    return [n for n in names
            if n.startswith("word/media/") and n not in referenced]


def main():
    if len(sys.argv) != 3:
        sys.exit("usage: postprocess.py OUTPUT.docx REFERENCE.docx")
    path, reference = sys.argv[1], sys.argv[2]
    spec = table_spec(reference)

    with zipfile.ZipFile(path) as z:
        items = [(i, z.read(i.filename)) for i in z.infolist()]
        names = [i.filename for i, _ in items]
        drop = set(orphan_media(names, lambda n: dict(
            (i.filename, d) for i, d in items)[n]))

    tables = 0
    rebuilt = []
    for info, data in items:
        if info.filename in drop:
            continue
        if info.filename == "word/document.xml" and spec:
            doc = data.decode("utf-8", "replace")
            doc, tables = restyle_tables(doc, spec)
            data = doc.encode("utf-8")
        rebuilt.append((info, data))

    if not drop and not tables:
        return

    tmp = path + ".tmp"
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zo:
        for info, data in rebuilt:
            zo.writestr(info, data)
    os.replace(tmp, path)

    if tables:
        print("Styled %d table(s) as %s with %s cell text."
              % (tables, spec["style"], spec["cell"]))
    if drop:
        print("Dropped %d unreferenced media part(s) inherited from the template."
              % len(drop))


if __name__ == "__main__":
    main()
