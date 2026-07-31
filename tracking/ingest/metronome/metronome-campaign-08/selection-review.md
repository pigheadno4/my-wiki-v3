# Metronome Campaign 08 Selection Review

Status: `approved`

Manifest: [manifest.json](manifest.json)

This is the exact Campaign 08 proposal. Selection used only raw paths, source URL headers, immutable hashes, line counts, current capsule-pending status, and source-target absence. No selected raw body was read in full, and ingestion has not started.

## Proposed jobs

| Order | Job | Page shape | Lines | Recommended tier | Routing reason |
| ---: | --- | --- | ---: | --- | --- |
| 1 | `overview` | Customer-billing overview | 66 | `strong` | Cross-object overview spanning contracts, invoices, alerts, balances, and reporting. |
| 2 | `manage-product-access` | Product-access guide | 53 | `standard` | Short isolated guide suitable for the limited templated Terra route. |
| 3 | `create-and-manage-notifications` | Notification setup guide | 77 | `strong` | May update shared alert and webhook concepts. |
| 4 | `india-e-mandates` | Regional payment guide | 81 | `strong` | Recurring-payment rules and Stripe boundaries need strong review. |
| 5 | `offset-notifications` | Notification timing guide | 86 | `strong` | Date-relative lifecycle semantics may affect shared concepts. |
| 6 | `spend-trackers` | Spend-monitoring guide | 118 | `strong` | Joins customer usage, alerts, and billing state. |
| 7 | `set-customer-spend-control` | Spend-control guide | 123 | `strong` | Enforcement, alerts, and billing boundaries require judgment. |
| 8 | `preview-event-cost` | Cost-preview guide | 173 | `strong` | Crosses event ingestion, pricing, and contract behavior. |
| 9 | `customer-controls` | Cross-feature controls guide | 185 | `strong` | Spans dashboards, alerts, access, balances, and spend limits. |
| 10 | `get-remaining-balance` | Balance calculation guide | 193 | `strong` | Longest selected page with financial calculation and API interpretation. |

Total selected raw lines: 1,155. Campaign 07 contained 1,636 lines, so this retains ten independent jobs while reducing selected input volume by about 29%. Nine jobs default to Sol workers; only the genuinely short, isolated product-access page is eligible for Terra. Every first attempt still requires a distinct Sol full-source reviewer.

## Shared-reduction clusters

- The overview and customer-controls pages route broad customer-experience relationships.
- Notification setup and offset notifications share alert, lifecycle, and webhook targets.
- Spend trackers, spend control, remaining balance, and cost preview share customer, usage, pricing, and balance targets.

Each worker still processes exactly one raw file. Shared suggestions are grouped only after individual reviewer approval, and the coordinator writes each shared target once.

## Audit set

The immutable manifest preselects:

1. `manage-product-access` — the required standard-page sample.
2. `get-remaining-balance` — the longest selected page and the financial/API interpretation sample.
3. `spend-trackers` — the ordinary manifest sample.

Any material partial or failure expands the query-quality audit to all ten pages.

## Runtime and acceptance

The coordinator remains the sole repository writer. Three dynamic subagent slots are shared by workers and reviewers without a batch barrier. A completed slot is immediately reused, ready reviews are preferred while one worker remains active when jobs are queued, and no reviewer may review its own worker output.

Campaign 08 uses simplified production mode: one full-source review for every first attempt; unchanged-hash targeted retry review only for bounded link, frontmatter, wording, or named-field repairs; full rereview for factual, uncertain, or broader corrections. The coordinator does not perform a default third full-source read.

Campaign close runs one touched-page validation, one capsule validation, complete hash/link/count/duplicate checks, and the fixed three-page query audit. It records only `started_at` and `completed_at`; no additional performance-monitoring system is introduced.

## Approval boundary

Approval of this exact manifest authorizes Campaign 08 initialization and execution. Until that explicit approval, no campaign state, worker order, source candidate, shared wiki edit, or ingestion log entry may be created.
