-- headings.lua — cooperate with reference.docx's automatic heading numbering,
-- and map the title and abstract onto the template's own styles.
--
-- The template binds Heading1–Heading9 to a multilevel list (numId 18), so Word
-- supplies "1", "1.1", "1.1.1" itself. A section number typed into the Markdown
-- therefore prints twice ("1 1 Background"). This filter:
--
--   * strips a leading manual number ("1 ", "2.1 ", "3.1.1 ") from a heading and
--     lets Word number it;
--   * leaves a heading that carried no manual number visually unnumbered, by
--     emitting it with list numbering switched off (numId 0). The document's
--     deliberate mix — numbered sections, unnumbered subheadings, self-labelled
--     appendices and References — therefore survives unchanged;
--   * maps the first level-1 heading to the template's Title style;
--   * maps an "Abstract" heading and the body that follows it to the template's
--     Abstract Title / Abstract styles.
--
-- custom-style values are Word style *names* (not styleIds): pandoc resolves
-- them against the reference doc by name, and inventing a new name would create
-- a new style instead of reusing the template's.

local utils = pandoc.utils

-- "1", "2.1", "3.1.1", "10" — a manual section number, not a word like "16S"
local function leading_number(inlines)
  if #inlines >= 2
    and inlines[1].t == "Str"
    and inlines[2].t == "Space"
    and inlines[1].text:match("^%d[%d%.]*$")
  then
    local rest = {}
    for i = 3, #inlines do rest[#rest + 1] = inlines[i] end
    return true, pandoc.Inlines(rest)
  end
  return false, inlines
end

local function esc(s)
  return (s:gsub("&", "&amp;"):gsub("<", "&lt;"):gsub(">", "&gt;"))
end

-- a HeadingN paragraph with list numbering explicitly switched off. numId 0 is
-- OOXML's "no numbering", which overrides the numPr inherited from the style.
local function unnumbered_heading(level, text)
  return pandoc.RawBlock("openxml",
    '<w:p><w:pPr><w:pStyle w:val="Heading' .. level .. '"/>'
      .. '<w:numPr><w:ilvl w:val="0"/><w:numId w:val="0"/></w:numPr>'
      .. '</w:pPr><w:r><w:t xml:space="preserve">' .. esc(text) .. '</w:t></w:r></w:p>')
end

local function styled(name, blocks)
  return pandoc.Div(blocks, pandoc.Attr("", {}, { ["custom-style"] = name }))
end

function Pandoc(doc)
  local blocks, out = doc.blocks, pandoc.Blocks({})
  local title_done = false
  local i = 1

  while i <= #blocks do
    local b = blocks[i]

    if b.t == "Header" then
      local numbered, content = leading_number(b.content)
      local text = utils.stringify(content)

      if b.level == 1 and not title_done then
        -- the document title: Title style, outside the numbered outline
        title_done = true
        out:insert(styled("Title", pandoc.Blocks({ pandoc.Para(content) })))

      elseif b.level == 1 and text:lower() == "abstract" then
        out:insert(styled("Abstract Title", pandoc.Blocks({ pandoc.Para(content) })))
        -- everything up to the next heading is the abstract body
        local body, j = pandoc.Blocks({}), i + 1
        while j <= #blocks and blocks[j].t ~= "Header" do
          body:insert(blocks[j])
          j = j + 1
        end
        if #body > 0 then out:insert(styled("Abstract", body)) end
        i = j - 1

      elseif numbered then
        b.content = content
        out:insert(b)

      else
        out:insert(unnumbered_heading(b.level, text))
      end
    else
      out:insert(b)
    end

    i = i + 1
  end

  doc.blocks = out
  return doc
end
