-- Render a Markdown thematic break (`---`, `***`, `___`) as a Word
-- "next page" section break instead of pandoc's default (a dropped/invisible
-- horizontal rule). Pandoc has already distinguished a real thematic break from
-- YAML frontmatter and from setext heading underlines, so acting on the parsed
-- HorizontalRule is safe.
--
-- A paragraph-level <w:sectPr> defines the section that ENDS at that paragraph,
-- so it must carry the page geometry or the preceding pages fall back to Word's
-- locale default (A4 vs Letter). convert.sh extracts pgSz/pgMar from the active
-- reference.docx and passes them in via these env vars; if absent we emit a bare
-- next-page break and let Word supply defaults.
local pgsz  = os.getenv("MDDOCX_PGSZ")  or ""
local pgmar = os.getenv("MDDOCX_PGMAR") or ""

function HorizontalRule()
  return pandoc.RawBlock(
    "openxml",
    "<w:p><w:pPr><w:sectPr>"
      .. "<w:type w:val=\"nextPage\"/>"
      .. pgsz
      .. pgmar
      .. "</w:sectPr></w:pPr></w:p>"
  )
end
