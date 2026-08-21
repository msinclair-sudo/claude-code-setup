# Chapter 7: Numbers and Data

**Source pages**: numbers, dates-times, units-of-measure, mathematical-notation, phone-numbers

## Core Idea
Numeric formatting exists to eliminate ambiguity for a global audience and to keep values from breaking across lines. Most rules here reduce to two habits: spell out small numbers, and bind a number to its unit with a nonbreaking space.

## Frameworks Introduced

- **Spell out or use numerals**: Spell out zero through nine and any number that starts a sentence; use numerals from 10 up.
  - Refinement: If a sentence-initial number reads awkwardly spelled out, rearrange the sentence so the number isn't first.
  - Ordinals are always spelled out — *first*, *fifth*, *twelfth*, *forty-third* — never *1st* or *43rd*.

- **Nonbreaking space between value and unit**: Write `64&nbsp;GB`, never `64 GB` (breakable) and never `64GB` (closed up).
  - Exceptions — no space at all: currency (`$10`, `£25`), percent (`65%`), and degrees of an angle (`180°`).
  - Temperature is a hybrid: nonbreaking space between the number and the degree symbol, then no space between `&deg;` and the scale letter (F or C).
  - Attributive compounds hyphenate normally: *a 128-bit system*.

- **Unambiguous dates and times**: Spell out month and weekday names in full; the goal is that no reader has to guess a date order.
  - Times: 12-hour clock by default — switch to 24-hour only when the UI, command, or code sample uses it, and then use it consistently across the page. Capitalize AM/PM with one space before it (`3:45 PM`). Drop `:00` from round hours (`3 PM`). *Noon* and *midnight* are acceptable.
  - Time ranges use hyphens with no surrounding spaces (`5-10 minutes ago`).
  - Time zones: avoid unless necessary. When required, prefer telling the reader it's local ("10 AM your local time") or match the UI's timestamp format. Spell out the region and append the UTC/GMT offset parenthetically — "US and Canadian Pacific Standard Time (UTC-8)". Never abbreviate a time zone name. If an event's time doesn't shift for daylight saving, name the specific zone without a UTC reference.

- **Reserved example phone numbers**: Never publish a real number. Use the US range reserved for examples and fiction: 800-555-0100 through 800-555-0199.
  - Formatting: separate parts with a nonbreaking hyphen (`&#8209;`) in both HTML and Markdown so the number can't wrap.

## Key Concepts
- **Nonbreaking space (`&nbsp;`)**: Keeps a number and its unit on the same line.
- **Nonbreaking hyphen (`&#8209;`)**: Same purpose for hyphenated strings like phone numbers.
- **NANP**: North American Numbering Plan — the region whose numbers follow the area-code format.

## Reference Tables

**Mathematical symbols** — prefer HTML entities over keyboard characters:

| Symbol | Markup | Meaning |
|---|---|---|
| + / = | keyboard | Plus, equals |
| − | `&minus;` | Minus (not a hyphen) |
| × | `&times;` | Multiplication |
| ≠ | `&ne;` | Not equal to |
| ± | `&plusmn;` | Plus-minus |
| ∓ | `&mnplus;` | Minus-plus |
| < / > | `&lt;` / `&gt;` | Less / greater than |
| ≈ | `&asymp;` | Approximately equal |
| ≉ | `&nap;` | Not approximately equal |

Multiplication notes: the dot operator (`&#8729;`) or asterisk operator (`&#42;`) may be used to match a UI. Never use a plain asterisk (`*`) for multiplication in text. Omitting the sign entirely is fine when unambiguous — write *ab* rather than *a* × *b*. Italicize mathematical variables (Ch 5).

Entity-based notation also serves assistive technology and renders more reliably than keyboard substitutes. If a third-party tool handles complex math, follow that tool's markup guidance instead.

## Worked Example

Unit spacing, showing why each rejected form fails:

| Recommended | Not recommended | Problem |
|---|---|---|
| `64&nbsp;GB` | `64 GB` | Ordinary space lets "64" and "GB" split across lines |
| `25&nbsp;mm` | `64GB` | No separation at all |
| a 128-bit system | a 128 bit system | Attributive compound needs the hyphen |
| $10, 65%, 180° | $ 10, 65 %, 180 ° | Currency, percent, and angle take no space |

A phone number formatted so it can never wrap mid-number:

```
415&#8209;555&#8209;0132
```

Renders as 415‑555‑0132, and the identical markup works in both HTML and Markdown.

## Key Takeaways
1. Spell out zero through nine, all ordinals, and any sentence-initial number.
2. Bind number to unit with `&nbsp;` — except currency, percent, and angle degrees, which close up.
3. Spell month and weekday names in full.
4. Default to the 12-hour clock; follow the interface when it uses 24-hour, and stay consistent page-wide.
5. Avoid time zones; when unavoidable, spell out the region and give the UTC offset.
6. Use HTML entities for math symbols; never an asterisk for multiplication.
7. Example phone numbers come from the reserved 800-555-01xx range.

## Connects To
- **Ch 3 (Punctuation)**: hyphens in ranges and compounds; slashes are banned in dates.
- **Ch 8 (Accessibility and Inclusion)**: unambiguous dates and entity-based math both serve global and assistive-technology readers.
- **Ch 4 (Grammar and Usage)**: abbreviation rules govern when to spell out unit names.
- **Ch 11 (Naming and Legal)**: reserved example domains follow the same principle as reserved phone numbers.
