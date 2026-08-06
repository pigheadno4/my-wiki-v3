# Metronome Campaign 11 Selection Review

Status: `approved`

Manifest: [manifest.json](manifest.json)

This is the exact Campaign 11 proposal. Selection used only pending-corpus paths, titles, immutable hashes, line counts, canonical URLs, and source-target absence. No selected raw body was read in full, campaign state has not been initialized, and ingestion has not started.

## Proposed jobs

| Order | Job | Page shape | Lines | Worker | Routing reason |
| ---: | --- | --- | ---: | --- | --- |
| 1 | `plans-shared-notifications` | Short shared-endpoint page | 36 | Sol | Standard audit sample under the approved all-Sol policy. |
| 2 | `plans-shared-invoices` | Shared invoice endpoint page | 86 | Sol | May contribute invoice context. |
| 3 | `reconcile-data` | Financial reconciliation guide | 111 | Sol | Requires financial-reporting boundaries; ordinary audit sample. |
| 4 | `void-an-invoice` | Invoice API endpoint | 141 | Sol | Requires precise invoice-state treatment. |
| 5 | `revenue-recognition` | Financial reporting guide | 149 | Sol | Requires careful revenue-recognition boundaries. |
| 6 | `list-system-notification-event-types` | Notification API endpoint | 154 | Sol | May affect notification and webhook concepts. |
| 7 | `regenerate-an-invoice` | Invoice API endpoint | 166 | Sol | Requires precise state and side-effect treatment. |
| 8 | `custom-invoice-integrations` | Integration guide | 168 | Sol | Cross-system invoice ownership requires semantic review. |
| 9 | `add-one-time-charge` | Invoice API endpoint | 174 | Sol | May affect invoicing and pricing semantics. |
| 10 | `in-app-reporting` | Reporting guide | 177 | Sol | Longest selected page and heavy audit sample. |

Total selected raw lines: 1,362. This is higher than Campaign 10's 921 lines, but the selected pages are short and concentrated around invoicing, reporting, and notifications. All workers use Sol; Terra is not eligible for any job.

## Existing production behavior

- Three dynamic subagent slots are shared by workers and reviewers without a batch barrier.
- Each worker reads exactly one complete raw page and writes only isolated temporary artifacts.
- Every first attempt receives independent full-source Sol review by another agent.
- Factual or uncertain corrections receive complete-source rereview; only bounded unchanged-hash mechanical corrections may use targeted review.
- The coordinator alone promotes approved sources and applies reviewer-approved concept updates grouped by target.
- Campaign close runs the existing touched-page validation, capsule validation, hash/link/count/duplicate checks, and fixed three-page query audit once.

No new workflow layer, worktree, performance framework, test tier, or coordinator full-source reread is introduced.

## Audit set

1. `plans-shared-notifications` — short standard-page sample.
2. `in-app-reporting` — longest selected page.
3. `reconcile-data` — ordinary financial-reporting sample.

Any material partial or failure expands the audit to all ten pages.

## Approval boundary

Approval of this exact manifest authorizes Campaign 11 initialization and execution. Until explicit approval, no campaign state, worker order, source candidate, canonical wiki edit, or ingest log entry will be created.
