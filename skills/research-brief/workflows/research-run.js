export const meta = {
  name: 'research-run',
  description: 'Run a research-brief AGENT BRIEF at quick, standard or deep size, or a blind framing preflight',
  whenToUse: 'Dispatching a brief written with the research-brief skill, or checking one blind before dispatch',
  phases: [
    { title: 'Preflight', detail: 'preflight mode only: one blind reader looks for framing leaks' },
    { title: 'Search', detail: 'deep only: one blind search agent per vocabulary angle' },
    { title: 'Review', detail: 'researcher (quick, standard) or synthesis (deep)' },
    { title: 'Critique', detail: 'standard and deep: adversarial critic' },
  ],
}

// args: { mode?: 'run' | 'preflight', brief, protocol, size, angles: [{name, vocabulary}], extra: [string] }
// brief is the AGENT BRIEF text only. ROUTING and DISPATCH (other than extra instructions) must never be passed.
const a = args || {}
if (typeof a.brief !== 'string' || !a.brief.trim()) throw new Error('args.brief (AGENT BRIEF text) is required')
const mode = a.mode || 'run'
if (!['run', 'preflight'].includes(mode)) throw new Error(`unknown mode: ${mode}`)
const extraList = Array.isArray(a.extra) ? a.extra.filter(x => typeof x === 'string' && x.trim()) : []
const extra = extraList.length
  ? `\n\nADDITIONAL INSTRUCTIONS\n${extraList.map(x => `- ${x}`).join('\n')}`
  : ''

const BRIEF = `=== AGENT BRIEF ===\n${a.brief}\n=== END AGENT BRIEF ===`

if (mode === 'preflight') {
  phase('Preflight')
  const PREFLIGHT_SCHEMA = {
    type: 'object',
    properties: {
      inferred_design: { type: 'string', description: 'the research design or claim you think this brief was written to serve, or "cannot tell"' },
      inferred_hoped_answers: {
        type: 'array',
        items: {
          type: 'object',
          properties: {
            direction: { type: 'string' },
            hoped_answer: { type: 'string', description: 'the answer you think the author hopes for, or "cannot tell"' },
            cue: { type: 'string', description: 'the exact wording that gave it away' },
          },
          required: ['direction', 'hoped_answer'],
        },
      },
      loaded_wording: { type: 'array', items: { type: 'string' }, description: 'phrases that lean toward one answer: one-way comparisons, a lone null, novelty-shaped boundaries' },
      one_sided_requests: { type: 'array', items: { type: 'string' }, description: 'evidence, background or cautions requested for one side and not the other' },
      evidence_rules_in_refusal: { type: 'array', items: { type: 'string' }, description: 'out-of-scope text that states a conclusion or discounts a kind of evidence' },
      scope_inconsistencies: { type: 'array', items: { type: 'string' }, description: 'places where scope is defined differently in different sentences' },
      nearest_precedent_risk: { type: 'array', items: { type: 'string' }, description: 'boundaries so narrow that the closest relevant work would fall outside every direction' },
      communities: { type: 'array', items: { type: 'string' }, description: 'research communities and vocabularies you would search to answer this brief' },
    },
    required: ['inferred_design', 'inferred_hoped_answers', 'loaded_wording', 'one_sided_requests',
      'evidence_rules_in_refusal', 'scope_inconsistencies', 'nearest_precedent_risk', 'communities'],
  }
  const report = await agent(
    `You are a BLIND READER checking a research brief before it is sent to research agents. Do not do the research. ` +
    `Research agents will receive exactly the text below and nothing else. The brief is meant to be neutral: it should not ` +
    `reveal what design it serves or what answer its author hopes for. Your job is to find where it fails that.\n\n` +
    `Read it as a sharp, suspicious reader would. Reconstruct, if you can, the design it serves and the answer hoped for in each ` +
    `direction, and quote the wording that gave each away. Then list loaded wording, one-sided requests, out-of-scope text that ` +
    `discounts evidence, scope defined inconsistently, boundaries that would exclude the nearest relevant work, and the research ` +
    `communities you would search. Say "cannot tell" where you genuinely cannot; do not invent a leak.\n\n${BRIEF}${extra}`,
    { label: 'preflight', phase: 'Preflight', schema: PREFLIGHT_SCHEMA },
  )
  if (!report) throw new Error('preflight reader returned nothing')
  return { mode, preflight: report }
}

if (typeof a.protocol !== 'string' || !a.protocol.trim()) throw new Error('args.protocol (researcher-protocol.md text) is required')
const size = a.size || 'standard'
if (!['quick', 'standard', 'deep'].includes(size)) throw new Error(`unknown size: ${size}`)
const angles = Array.isArray(a.angles) ? a.angles : []
if (size === 'deep' && angles.length < 2) throw new Error('deep size needs at least two angles')

const PROTOCOL = `=== RESEARCHER PROTOCOL ===\n${a.protocol}\n=== END RESEARCHER PROTOCOL ===`

const ACCESS = { type: 'string', enum: ['full_text', 'abstract_only', 'secondary'] }

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
          direction: { type: 'string', description: 'which direction (D1, D2, ...) this bears on' },
          claim: { type: 'string' },
          reference: { type: 'string', description: 'complete reference with DOI' },
          access: ACCESS,
          quote_or_figure: { type: 'string' },
          evidence_class: { type: 'string', enum: ['measured', 'derived', 'modelled', 'asserted'] },
          setting: { type: 'string', description: 'system, population, environment, scale, n, measurement type, range of key variable, or "not reported"' },
          standing: { type: 'string', enum: ['replicated', 'contested', 'single_study', 'unclear'] },
          single_source: { type: 'boolean' },
          bounding_or_contrary: { type: 'boolean' },
          nearest_precedent: { type: 'boolean', description: 'meets some but not all of the direction\'s conditions' },
        },
        required: ['claim', 'reference', 'access', 'evidence_class', 'setting'],
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
    answers: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          direction: { type: 'string', description: 'direction label, plus the case if the direction is answered per case' },
          answer: { type: 'string', description: 'what the evidence shows, in the reviewer\'s own words' },
          strength: { type: 'string', description: 'how strong the evidence is, and why' },
          conflicts: { type: 'string', description: 'where the evidence disagrees, or "none found"' },
          not_measured: { type: 'string', description: 'cases or settings with no evidence, or "none"' },
          access_basis: { type: 'string', description: 'how much of the answer rests on full text, abstract only, secondary' },
          single_source_sensitivity: { type: 'string', description: 'would the answer change if one source were removed; name it' },
        },
        required: ['direction', 'answer', 'strength', 'access_basis'],
      },
    },
    review_markdown: { type: 'string', description: 'full review body with in-text markers, access labels and reference list' },
    not_obtained: NOT_OBTAINED,
    search_record: { type: 'string' },
  },
  required: ['title', 'answers', 'review_markdown', 'not_obtained', 'search_record'],
}

const CRITIQUE_SCHEMA = {
  type: 'object',
  properties: {
    answers_supported: { type: 'string', enum: ['yes', 'partial', 'no'] },
    reformulated_answers: {
      type: 'array',
      items: {
        type: 'object',
        properties: { direction: { type: 'string' }, answer: { type: 'string' } },
        required: ['direction', 'answer'],
      },
      description: 'the answers the body supports; repeat the original where supported',
    },
    answers_assessment: { type: 'string' },
    single_source_claims: { type: 'array', items: { type: 'string' } },
    access_errors: { type: 'array', items: { type: 'string' } },
    reference_errors: { type: 'array', items: { type: 'string' } },
    coverage_gaps: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          gap: { type: 'string' },
          setting_or_class: { type: 'string', description: 'the concrete setting, measurement type, population or community missed' },
          direction: { type: 'string' },
        },
        required: ['gap', 'setting_or_class'],
      },
    },
    one_sided_handling: { type: 'array', items: { type: 'string' } },
    merged_cases: { type: 'array', items: { type: 'string' } },
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
  required: ['answers_supported', 'reformulated_answers', 'answers_assessment', 'single_source_claims',
    'access_errors', 'reference_errors', 'coverage_gaps', 'one_sided_handling', 'merged_cases', 'scope_drift', 'expectation_echo'],
}

let sweeps = []
let review

if (size === 'deep') {
  phase('Search')
  const raw = await parallel(angles.map(ang => () => agent(
    `You are a SEARCH AGENT. Follow the Common rules and the Search agent section of the protocol.\n\n` +
    `Your angle: ${ang.name}\nSearch in this community's vocabulary: ${ang.vocabulary || ang.name}\n\n` +
    `${BRIEF}\n\n${PROTOCOL}${extra}\n\nReturn findings for your angle only. Do not write a review or an answer.`,
    { label: `search:${ang.name}`, phase: 'Search', schema: FINDINGS_SCHEMA },
  )))
  const failed = angles.filter((_, i) => !raw[i]).map(x => x.name)
  if (failed.length) log(`search agents returned nothing for: ${failed.join(', ')}`)
  sweeps = raw.map((s, i) => (s ? { angle: angles[i].name, ...s } : null)).filter(Boolean)
  if (!sweeps.length) throw new Error('every search agent failed; nothing to synthesise')

  phase('Review')
  review = await agent(
    `You are the SYNTHESIS AGENT. Follow the Common rules and the Synthesis agent section of the protocol.\n\n` +
    `${BRIEF}\n\n${PROTOCOL}${extra}\n\n` +
    `=== SEARCH FINDINGS (one block per angle; the angles were searched blind to each other) ===\n` +
    `${JSON.stringify(sweeps, null, 1)}\n=== END SEARCH FINDINGS ===`,
    { label: 'synthesis', phase: 'Review', schema: REVIEW_SCHEMA },
  )
} else {
  phase('Review')
  review = await agent(
    `You are the RESEARCHER for this brief. Follow the Common rules, and both the Search agent and Synthesis agent ` +
    `sections of the protocol: search, read, then write the review.\n\n${BRIEF}\n\n${PROTOCOL}${extra}`,
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
    `Verify against the sources themselves, and check references against Crossref.\n\n${BRIEF}\n\n${PROTOCOL}${extra}\n\n` +
    `=== REVIEW UNDER CRITIQUE ===\nAnswers: ${JSON.stringify(review.answers)}\n\n${review.review_markdown}\n\n` +
    `Sources the reviewer did not obtain: ${JSON.stringify(review.not_obtained)}\n=== END REVIEW ===`,
    { label: 'critic', phase: 'Critique', schema: CRITIQUE_SCHEMA },
  )
  if (!critique) log('critic returned nothing: treat the review as uncritiqued')
}

const notObtained = [
  ...sweeps.flatMap(s => s.not_obtained.map(n => ({ ...n, angle: s.angle }))),
  ...review.not_obtained,
]

const accessCounts = { full_text: 0, abstract_only: 0, secondary: 0 }
for (const s of sweeps) for (const f of s.findings) if (f.access in accessCounts) accessCounts[f.access]++

return {
  mode,
  size,
  angles: sweeps.map(s => s.angle),
  sweepCounts: sweeps.map(s => ({ angle: s.angle, findings: s.findings.length, not_obtained: s.not_obtained.length })),
  accessCounts: size === 'deep' ? accessCounts : null,
  notObtained,
  review,
  critique,
}
