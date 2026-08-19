# Metronome Campaign 16 Selection Review

- Status: **completed — 5/5 approved and promoted**
- Purpose: first small production-shaped campaign after Campaign 15. It uses
  the established independent semantic gate rather than testing another model
  or reviewer-removal hypothesis.
- Scheduler mode: `dry_run` keeps workers and reviewers repository-read-only;
  canonical promotion is a coordinator close action after terminal reviews and
  the approved-page validation gate.
- Selection method: metadata only — raw path, source URL, first heading, line
  count, SHA-256, prior-manifest membership, and source-target existence. No raw
  body was read completely during selection.
- Selection: five ordinary guide pages with no prior campaign membership and no
  canonical source page. API/schema-heavy pages are excluded.
- Models: Sol-medium worker and a different Sol-high reviewer for every page.
- Runtime: one coordinator plus at most three repository-read-only native agents
  in a dynamic pool; completed work immediately releases its slot.

| # | Job | Lines | Role |
| ---: | --- | ---: | --- |
| 1 | `prioritization-rules` | 265 | standard guide and fixed audit sample |
| 2 | `prepaid-credits` | 277 | billing-model guide |
| 3 | `provision-your-customer` | 301 | subscription guide and fixed audit sample |
| 4 | `get-commit-and-usage-analytics` | 413 | reporting guide |
| 5 | `model-hierarchical-customer-relationships` | 554 | longest page and fixed audit sample |

## Per-page gate

Each worker reads exactly one complete raw page, extracts three to five
verbatim quotes, and returns one isolated source candidate plus only
fact-bearing concept, reciprocal-link, and contradiction signals. Company,
index, and log suggestion arrays remain empty.

A different Sol reviewer reads the complete raw page and checks source facts,
important omissions, contradictions, unknowns, quote grounding, the raw
backlink, and the semantic completeness of concept signals. The reviewer does
not polish final shared-page prose or inspect mechanical company, index, and log
entries.

An unchanged-hash correction limited to evidence, links, frontmatter,
formatting, wording, or an already identified field may use targeted diff
review by the same reviewer. A factual error, important omission, or renewed
interpretation requires a complete review. A page rejected after its bounded
attempt policy remains terminal evidence and does not block unrelated approved
pages.

## Coordinator close

Only reviewer-approved jobs are eligible for promotion. The coordinator does
not perform a default third full-source read. It groups approved concept signals
by exact target, applies each affected concept once before its corresponding
sources, writes approved sources, verifies reciprocal links and contradictions,
then derives company, provider-index, and provider-log entries mechanically.

Rejected-job candidates and suggestions are never promoted. Approved jobs do
not require every other manifest job to pass. After the terminal job set is
known, the coordinator runs one campaign-close validation covering all promoted
sources and touched concepts, then provider counts, links, duplicates, raw
hashes, and capsule consistency once.

## Authorization boundary

Approval of this exact manifest authorizes initialization, complete reads of
only these five raw pages, independent per-page review, and coordinator
promotion of reviewer-approved jobs after the stated close gates pass. It does
not authorize API/schema-heavy pages, repair or promotion of Campaign 15,
another model comparison, bulk ingestion, or cross-PSP rollout.

## Outcome

- Five pages were approved and promoted across nine worker attempts, eight full reviews, and one targeted review.
- The fixed three-page query audit initially found one material omission in `provision-your-customer`. One bounded coordinator repair restored the raw's standard-subscription included-versus-separate-arrears boundary.
- The same independent auditor rechecked that repair and expanded the audit to all five pages. Final result: 5/5 pages and 15/15 queries passed, with no material open defect.
- Campaign-close validation passed for all touched Metronome pages and the provider capsule. The repository-wide validator still reports 16 unrelated pre-existing PayPal and Stripe issues.
- Final coverage: 225 collected documentation pages, 102 source summaries, and 129 raw pages without source summaries.
- Evidence: [monitor](monitor.md) and [quality audit](quality-audit.md).
