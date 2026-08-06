# Metronome Campaign 10 Selection Review

Status: `approved`

Manifest: [manifest.json](manifest.json)

This is the exact Campaign 10 proposal. Selection used only pending-corpus paths, source URL headers, headings, immutable hashes, line counts, and source-target absence. No selected raw body was read in full, no campaign state exists, and ingestion has not started.

## Proposed jobs

| Order | Job | Page shape | Lines | Recommended tier | Routing reason |
| ---: | --- | --- | ---: | --- | --- |
| 1 | `workato-connector` | Thin connector setup | 28 | `standard` | Isolated setup page with no expected fact-bearing shared-concept change. |
| 2 | `audit-logs-guide` | Audit-log guide | 55 | `strong` | Audit visibility and actor-action evidence affect security boundaries. |
| 3 | `single-sign-on-sso` | SSO guide | 41 | `strong` | Identity-provider and user-management behavior require precise access boundaries. |
| 4 | `allowlist-guide` | Network allowlist guide | 43 | `strong` | Must remain consistent with the already-ingested service-registry source. |
| 5 | `segment-integration` | Event integration | 78 | `strong` | Field mapping affects customer attribution and ingestion semantics. |
| 6 | `avalara-integration` | Tax integration | 85 | `strong` | Tax-code mapping and invoice-setting ownership cross system boundaries. |
| 7 | `anrok-integration` | Tax integration | 105 | `strong` | Metronome, Anrok, and Stripe product mapping requires responsibility separation. |
| 8 | `import-existing-invoices` | Historical invoice guide | 143 | `strong` | Historical import affects contract and reporting state outside ordinary event processing. |
| 9 | `billable-metrics-sql-editor` | SQL metric guide | 154 | `strong` | SQL functions, aggregation, and scheduled changes extend a shared concept. |
| 10 | `production-checklist` | Production readiness guide | 189 | `strong` | Longest page spans metering, pricing, invoicing, security, and webhook boundaries. |

Total selected raw lines: 921, about 8% fewer than Campaign 09's 1,004 lines. One genuinely thin isolated page is eligible for Terra; nine semantic pages use Sol. Every first attempt still receives a distinct Sol full-source review.

## Compact production behavior

- Workers return only fact-bearing concept suggestions, reciprocal source links, and contradictions. Their `company`, `index`, and `log` suggestion arrays stay empty.
- Reviewers may approve suggestions by update-ID string. Only rejected suggestions require detailed decision objects and reasons.
- The coordinator derives company and provider-index catalog entries, the consolidated campaign log entry, and counts from approved source metadata.
- Approved concept suggestions are grouped by exact target and applied once. There is no shared-close proposal agent or extra full-corpus review.

## Shared-reduction clusters

- Audit logs, SSO, allowlisting, and the production checklist share security and operational-readiness context.
- Segment and Workato share platform-integration context; only Segment is expected to change event-ingestion semantics.
- Anrok and Avalara share tax-integration and invoice-setting context.
- SQL metrics extend billable-metric semantics; historical invoice import extends invoicing and reporting boundaries.

Each worker still handles one complete raw page. No candidate combines sources.

## Audit set

The immutable manifest preselects:

1. `workato-connector` — the required standard-page sample.
2. `production-checklist` — the longest, cross-domain selected page.
3. `segment-integration` — an ordinary operational integration sample.

Any material partial or failure expands the audit to all ten pages.

## Runtime and acceptance

The coordinator remains the only repository writer. Three dynamic subagent slots are shared without a batch barrier. Ready reviews are preferred while one worker remains active if jobs are queued, and no reviewer may review its own worker output.

First attempts receive complete-source review. Unchanged-hash, bounded formatting or named-field corrections may use targeted review; factual or uncertain changes receive complete-source rereview. Campaign close runs one touched-page validation, one capsule validation, complete hash/link/count/duplicate checks, and the fixed three-page query audit.

No workflow change, worktree layer, performance framework, shared-close agent, coordinator full-source reread, or extra testing tier is introduced.

## Approval boundary

Approval of this exact manifest authorizes Campaign 10 initialization and execution. Until explicit approval, no campaign state, worker order, source candidate, shared wiki edit, or ingestion log entry will be created.
