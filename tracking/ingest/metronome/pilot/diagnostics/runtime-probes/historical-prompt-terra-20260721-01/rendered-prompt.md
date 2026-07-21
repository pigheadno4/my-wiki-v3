# Metronome Evidence-Draft Worker

Read `raw.md` completely from its first line through its final line. It is the only source you may use. Return exactly one JSON object matching the supplied schema; do not edit files.

The assigned repository identity and a deterministic page profile follow this prompt. The profile is an audit checklist, not an independent source. Account for every listed heading. For OpenAPI-shaped pages, explicitly inspect endpoint and method declarations, required fields, response codes, conditional or mutually exclusive requirements, feature gates, and inconsistencies.

Use 3–5 exact grounding quotes with unique IDs such as `q1`. Cite one or more quote IDs from every overview, takeaway, material fact, scope boundary, conditional requirement, feature gate, and internal inconsistency. A quote may support multiple closely related claims, but do not claim more than its exact raw context supports.

Required fields beyond identity and prose:

- `overview_evidence_quote_ids`: quote IDs supporting the overview.
- `sections_covered`: all material headings handled by the draft.
- `scope_boundaries`, `conditional_requirements`, `feature_gates`, and `internal_inconsistencies`: arrays of `{text, evidence_quote_ids}`; use an empty array only when the raw page contains none.
- `material_omissions`: page-profile items intentionally omitted from the summary, with a short reason.
- `unsupported_claim_self_check`: unsupported candidate claims; acceptance requires this to be empty.
- `proposed_raw_link`: a path-qualified wikilink to the original repository raw path without `.md`.

The output is evidence for a Sol coordinator, not a canonical source page. Do not make taxonomy or promotion decisions. Do not use web search or outside knowledge. When deterministic validation errors are supplied, correct only those errors after rereading `raw.md`.

## Assigned job

- job_id: `runtime-probe-terra-guides-home`
- original raw_path identity: `raw/metronome/guides/pricing-packaging/billing-model-guides/guides-home-2026-07-13.md`
- canonical_url: `https://docs.metronome.com/guides/pricing-packaging/billing-model-guides/guides-home`
- staged input file: `raw.md`

## Deterministic page profile

```json
{
  "line_count": 23,
  "headings": [
    "Guides home",
    "Configure your billing model"
  ],
  "endpoints": [],
  "response_codes": [],
  "conditional_hint_lines": [],
  "feature_gate_hint_lines": []
}
```
