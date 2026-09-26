export const meta = {
  name: 'research-run',
  description: 'Run a research-brief AGENT BRIEF at quick, standard or deep size',
  whenToUse: 'Dispatching a brief written with the research-brief skill',
  phases: [
    { title: 'Search', detail: 'deep only: one blind search agent per vocabulary angle' },
    { title: 'Review', detail: 'researcher (quick, standard) or synthesis (deep)' },
    { title: 'Critique', detail: 'standard and deep: adversarial critic' },
  ],
}

// args: { brief, protocol, size, angles: [{name, vocabulary}], extra: [string], verdictOptions: [string] }
// brief is the AGENT BRIEF text only. ROUTING and DISPATCH must never be passed.
const a = args || {}
if (typeof a.brief !== 'string' || !a.brief.trim()) throw new Error('args.brief (AGENT BRIEF text) is required')
if (typeof a.protocol !== 'string' || !a.protocol.trim()) throw new Error('args.protocol (researcher-protocol.md text) is required')
const size = a.size || 'standard'
if (!['quick', 'standard', 'deep'].includes(size)) throw new Error(`unknown size: ${size}`)
const angles = Array.isArray(a.angles) ? a.angles : []
if (size === 'deep' && angles.length < 2) throw new Error('deep size needs at least two angles')
const extra = Array.isArray(a.extra) && a.extra.length
  ? `\n\nADDITIONAL INSTRUCTIONS\n${a.extra.map(x => `- ${x}`).join('\n')}`
  : ''
const options = Array.isArray(a.verdictOptions) && a.verdictOptions.length
  ? `\n\nChoose each verdict from exactly these options, one verdict per part:\n${a.verdictOptions.map(x => `- ${x}`).join('\n')}`
  : ''

const BRIEF = `=== AGENT BRIEF ===\n${a.brief}\n=== END AGENT BRIEF ===`
const PROTOCOL = `=== RESEARCHER PROTOCOL ===\n${a.protocol}\n=== END RESEARCHER PROTOCOL ===`

const NOT_OBTAINED = {
  type: 'array',
  items: {
    type: 'object',
    properties: {
      reference: { type: 'string' },
      routes_tried: { type: 'string' },
      why_relevant: { type: 'string' },
    },
    required: ['reference', 'routes_tried'],
  },
}

const FINDINGS_SCHEMA = {
  type: 'object',
  properties: {
    findings: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          claim: { type: 'string' },
          reference: { type: 'string', description: 'complete reference with DOI' },
          quote_or_figure: { type: 'string' },
          evidence_class: { type: 'string', enum: ['measured', 'inferred', 'modelled', 'asserted'] },
          system: { type: 'string', enum: ['natural', 'engineered', 'not_applicable'] },
          regime: { type: 'string', description: 'organism group, environment, scale, n, range of key variable, or "not reported"' },
          single_source: { type: 'boolean' },
          bounding_or_negative: { type: 'boolean' },
        },
        required: ['claim', 'reference', 'evidence_class', 'system', 'regime'],
      },
    },
    not_obtained: NOT_OBTAINED,
    search_record: { type: 'string' },
  },
  required: ['findings', 'not_obtained', 'search_record'],
}

const REVIEW_SCHEMA = {
  type: 'object',
  properties: {
    title: { type: 'string' },
    verdicts: {
      type: 'array',
      items: {
        type: 'object',
        properties: { part: { type: 'string' }, verdict: { type: 'string' } },
        required: ['part', 'verdict'],
      },
    },
    review_markdown: { type: 'string', description: 'full review body with in-text markers and reference list' },
    not_obtained: NOT_OBTAINED,
    search_record: { type: 'string' },
  },
  required: ['title', 'verdicts', 'review_markdown', 'not_obtained', 'search_record'],
}

const CRITIQUE_SCHEMA = {
  type: 'object',
  properties: {
    verdict_supported: { type: 'string', enum: ['yes', 'partial', 'no'] },
    reformulated_verdict: { type: 'string', description: 'the verdict the body supports; repeat the original if supported' },
    verdict_assessment: { type: 'string' },
    single_source_claims: { type: 'array', items: { type: 'string' } },
    abstract_only_claims: { type: 'array', items: { type: 'string' } },
    reference_errors: { type: 'array', items: { type: 'string' } },
    coverage_gaps: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          gap: { type: 'string' },
          setting_or_class: { type: 'string', description: 'the concrete setting, class, group or community missed' },
          brief_bullet: { type: 'string' },
        },
        required: ['gap', 'setting_or_class'],
      },
    },
    scope_drift: { type: 'array', items: { type: 'string' } },
    expectation_echo: {
      type: 'object',
      properties: {
        brief_states_expectation: { type: 'boolean' },
        brief_wording: { type: 'string' },
        review_repeats_it: { type: 'boolean' },
        independent_support: { type: 'string' },
      },
      required: ['brief_states_expectation', 'review_repeats_it'],
    },
  },
  required: ['verdict_supported', 'reformulated_verdict', 'verdict_assessment', 'single_source_claims',
    'abstract_only_claims', 'reference_errors', 'coverage_gaps', 'scope_drift', 'expectation_echo'],
}

let sweeps = []
let review

if (size === 'deep') {
  phase('Search')
  const raw = await parallel(angles.map(ang => () => agent(
    `You are a SEARCH AGENT. Follow the Common rules and the Search agent section of the protocol.\n\n` +
    `Your angle: ${ang.name}\nSearch in this community's vocabulary: ${ang.vocabulary || ang.name}\n\n` +
    `${BRIEF}\n\n${PROTOCOL}${extra}\n\nReturn findings for your angle only. Do not write a review or a verdict.`,
    { label: `search:${ang.name}`, phase: 'Search', schema: FINDINGS_SCHEMA },
  )))
  const failed = angles.filter((_, i) => !raw[i]).map(x => x.name)
  if (failed.length) log(`search agents returned nothing for: ${failed.join(', ')}`)
  sweeps = raw.map((s, i) => (s ? { angle: angles[i].name, ...s } : null)).filter(Boolean)
  if (!sweeps.length) throw new Error('every search agent failed; nothing to synthesise')

  phase('Review')
  review = await agent(
    `You are the SYNTHESIS AGENT. Follow the Common rules and the Synthesis agent section of the protocol.\n\n` +
    `${BRIEF}\n\n${PROTOCOL}${extra}${options}\n\n` +
    `=== SEARCH FINDINGS (one block per angle; the angles were searched blind to each other) ===\n` +
    `${JSON.stringify(sweeps, null, 1)}\n=== END SEARCH FINDINGS ===`,
    { label: 'synthesis', phase: 'Review', schema: REVIEW_SCHEMA },
  )
} else {
  phase('Review')
  review = await agent(
    `You are the RESEARCHER for this brief. Follow the Common rules, and both the Search agent and Synthesis agent ` +
    `sections of the protocol: search, read in full, then write the review.\n\n${BRIEF}\n\n${PROTOCOL}${extra}${options}`,
    { label: 'researcher', phase: 'Review', schema: REVIEW_SCHEMA },
  )
}
if (!review) throw new Error('review stage returned nothing')

let critique = null
if (size === 'quick') {
  log('quick size: no critic ran. Do not cite this review until it has been critiqued.')
} else {
  phase('Critique')
  critique = await agent(
    `You are the CRITIC. Follow the Common rules and the Critic section of the protocol. ` +
    `Verify against the sources themselves, and check references against Crossref.\n\n${BRIEF}\n\n${PROTOCOL}\n\n` +
    `=== REVIEW UNDER CRITIQUE ===\nVerdicts: ${JSON.stringify(review.verdicts)}\n\n${review.review_markdown}\n\n` +
    `Sources the reviewer did not obtain: ${JSON.stringify(review.not_obtained)}\n=== END REVIEW ===`,
    { label: 'critic', phase: 'Critique', schema: CRITIQUE_SCHEMA },
  )
  if (!critique) log('critic returned nothing: treat the review as uncritiqued')
}

const notObtained = [
  ...sweeps.flatMap(s => s.not_obtained.map(n => ({ ...n, angle: s.angle }))),
  ...review.not_obtained,
]

return {
  size,
  angles: sweeps.map(s => s.angle),
  sweepCounts: sweeps.map(s => ({ angle: s.angle, findings: s.findings.length, not_obtained: s.not_obtained.length })),
  notObtained,
  review,
  critique,
}
