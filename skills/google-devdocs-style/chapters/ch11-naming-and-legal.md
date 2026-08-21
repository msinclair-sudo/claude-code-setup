# Chapter 11: Naming, Trademarks, and Legal Safety

**Source pages**: product-names, trademarks, examples

## Core Idea
Names carry legal weight. Follow each owner's official capitalization exactly, never bend a trademark into a noun or verb, and never publish a real domain, address, or person's name in an example.

## Frameworks Introduced

- **Follow official capitalization**: Google product names are title case (every word capitalized except prepositions like *of*/*on* and articles like *a*/*the*), but the governing rule is always the owner's official form.
  - How: For third-party or open source terms, match the project's own documentation — in a Kubernetes context, "A Job creates one or more Pods" follows Kubernetes' conventions.
  - Exception: match a UI label when you're referring to that label.
  - Lowercase-initial names stay lowercase even at the start of a sentence — but it's better to rewrite so the sentence doesn't begin there.

- **Trademarks are modifiers, never nouns or verbs**: Always use a trademarked term to modify a noun.
  - How: "use a Chromebook notebook computer," not "use a Chromebook."
  - Never form a possessive or plural from a trademark, and never alter it: not "Chromebook's features," not "google 'notebook computers'" as a verb.
  - Follow whatever usage guidelines the mark's owner publishes.

- **Reserved examples only**: Never use real domain names, email addresses, people's names, project names, phone numbers, or credit card numbers.
  - How: Use IANA-reserved `example.com`, `example.org`, `example.net`; or a Google-owned documentation domain (`altostrat.com`, `examplepetstore.com`, `example-pet-store.com`, `myownpersonaldomain.com`, `my-own-personal-domain.com`, `cymbalgroup.com`). For internationalized domains, use an IDN Test TLD.
  - Alternative: use placeholders like `USER_ID` or `EMAIL_ADDRESS` (Ch 6).

## Key Concepts
- **Title case (init-capped)**: Every word capitalized except prepositions and articles.
- **PII**: Personally identifiable information — domain names, email addresses, phone numbers, names, project names, credit card numbers. Keep all of it out of examples.
- **Punycode**: The ASCII encoding for non-ASCII hostnames — `http://مثال.إختبار` encodes as `xn--kgbechtv`.

## Reference Tables

| Recommended | Not recommended | Rule |
|---|---|---|
| use a Chromebook notebook computer | use a Chromebook | Trademark must modify a noun |
| Chromebook computers rely on an internet connection | Chromebook's features rely on… | No possessive from a trademark |
| search for "notebook computers" | google "notebook computers" | No trademark as a verb |
| example.com, altostrat.com | acme-real-company.com | Reserved domains only |

## Worked Example

Product-name capitalization tracks the owner, not a house style — so two correct sentences can look inconsistent side by side:

- **In a Kubernetes context**: "A Job creates one or more Pods." — capitalized because Kubernetes' own documentation capitalizes these resource types.
- **In a Google Cloud context**: "The Cloud Scheduler job publishes a message to a Pub/Sub topic at one-minute intervals." — *job* is lowercase here because it's a common noun, while *Cloud Scheduler* and *Pub/Sub* are product names.

The apparent inconsistency is correct: each term follows its own owner's convention. This is also why Ch 4 forbids relying on capitalization to convey meaning — a reader can't be expected to infer that capital-J *Job* is a distinct concept from lowercase *job*.

## Key Takeaways
1. Match each product's official capitalization; title case is Google's default, not a universal rule.
2. Never start a sentence with a lowercase-initial product name — rewrite instead.
3. Trademarks modify nouns; they're never nouns, verbs, possessives, or plurals.
4. Follow the trademark owner's published usage guidelines.
5. Use only reserved example domains, never real ones.
6. Keep all PII out of examples and screenshots.

## Connects To
- **Ch 4 (Grammar and Usage)**: capitalization rules and the ban on meaning-by-capitalization.
- **Ch 6 (Code Documentation)**: placeholders are the alternative to fictitious example values.
- **Ch 10 (UI and Visuals)**: the same PII prohibition governs screenshots.
- **Ch 7 (Numbers and Data)**: reserved example phone numbers follow this principle.
