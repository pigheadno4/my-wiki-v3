# Metronome Campaign 09 Selection Review

Status: `approved`

Manifest: [manifest.json](manifest.json)

This is the exact Campaign 09 proposal. Selection used only pending-corpus paths, source URL headers, headings, immutable hashes, line counts, and source-target absence. No selected raw body was read in full, no campaign state exists, and ingestion has not started.

## Proposed jobs

| Order | Job | Page shape | Lines | Recommended tier | Routing reason |
| ---: | --- | --- | ---: | --- | --- |
| 1 | `guides-home` | Billing-model navigation | 23 | `standard` | Very short navigation page with no expected fact-bearing concept change. |
| 2 | `credit-commit-alerts` | Credit/commit alert guide | 24 | `strong` | May add a durable alert and credit-balance boundary. |
| 3 | `pricing-packaging-overview` | Pricing navigation overview | 63 | `standard` | Short bounded navigation and catalog page. |
| 4 | `metronome-pricing-model` | Platform pricing model | 88 | `strong` | Separates pricing structure, usage metrics, billing counts, and export behavior. |
| 5 | `billable-metrics-basic-filters` | Streaming metric guide | 106 | `strong` | Filter and aggregation behavior affects an existing shared concept. |
| 6 | `currency-custom-pricing-units` | Currency and unit guide | 115 | `strong` | Financial denomination and custom-unit boundaries require judgment. |
| 7 | `send-usage-events` | Event-ingestion guide | 123 | `strong` | Identity, timestamps, queueing, and retry behavior affect ingestion guarantees. |
| 8 | `issue-credit-memos` | Invoice-correction guide | 135 | `strong` | Future and historical corrections cross invoice and revenue semantics. |
| 9 | `get-services` | Security API schema | 140 | `strong` | Service and authorization schema interpretation requires strong review. |
| 10 | `reset-threshold-notification` | Alert reset API | 187 | `strong` | Longest selected page covers state reset and response-schema boundaries. |

Total selected raw lines: 1,004, about 13% fewer than Campaign 08's 1,155 lines and far below the rejected 3,951-line customer-alert cluster. Two genuinely navigational pages are eligible for Terra; eight semantic or schema-bearing pages use Sol. Every first attempt still receives a distinct Sol full-source review.

## Compact production behavior

- Workers return only fact-bearing concept suggestions, reciprocal source links, and contradictions. Their `company`, `index`, and `log` suggestion arrays stay empty.
- Reviewers may approve suggestions by returning their update-ID strings. Only rejected suggestions require detailed decision objects and reasons.
- The coordinator derives company and provider-index catalog entries, the consolidated campaign log entry, and counts from approved source metadata.
- Approved concept suggestions are grouped by exact target and applied once by the coordinator. There is no default shared-close proposal agent.

## Shared-reduction clusters

- Pricing overview, platform pricing, and custom pricing units share pricing and packaging context.
- Billable-metric filters and usage-event sending share event-to-metric semantics.
- Credit/commit alerts and threshold reset share alert-state context.
- Credit memos remain an invoicing correction topic; Get Services remains a security API topic.

Each worker still handles exactly one complete raw page. Compact review and deterministic catalogs reduce ceremony; they do not combine source units.

## Audit set

The immutable manifest preselects:

1. `guides-home` — the required standard-page sample.
2. `reset-threshold-notification` — the longest and schema-bearing selected page.
3. `send-usage-events` — the ordinary manifest sample with operational semantics.

Any material partial or failure expands the query-quality audit to all ten pages.

## Runtime and acceptance

The coordinator remains the only repository writer. Three dynamic subagent slots are shared by workers and reviewers without a batch barrier. Ready reviews are preferred while one worker remains active if jobs are queued; no reviewer may review its own worker output.

First attempts receive complete-source review. An unchanged-hash retry may use targeted review only for a bounded wording, link, frontmatter, or named-field correction; factual or uncertain changes require complete-source rereview. The coordinator does not perform a default third raw read.

Campaign close runs one touched-page validation, one capsule validation, complete candidate/hash/link/count/duplicate checks, and the fixed three-page query audit. No separate performance framework or extra full-corpus test loop is introduced.

## Approval boundary

Approval of this exact manifest authorizes Campaign 09 initialization and execution. Until explicit approval, no campaign state, worker order, source candidate, shared wiki edit, or ingestion log entry will be created.
