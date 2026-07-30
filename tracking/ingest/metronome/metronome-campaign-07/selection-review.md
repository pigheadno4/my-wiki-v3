# Metronome Campaign 07 Selection Review

Status: `proposed`

Manifest: [manifest.json](manifest.json)

This is an exact proposal for the approved parallel-review design. Selection uses raw-path metadata, immutable hashes, canonical URL headers, line counts, and current capsule-pending status. It is not raw ingestion: no selected raw body has been read in full, and heading or metadata selection does not constitute full raw ingestion.

## Proposed jobs

| Order | Job | Page shape | Lines | Recommended tier | Routing reason |
| ---: | --- | --- | ---: | --- | --- |
| 1 | `subscription-overview` | Subscription data-model guide | 57 | `standard` | Short subscription data-model guide establishing the shared subscription concept target. |
| 2 | `define-subscription-pricing` | Subscription pricing guide | 59 | `standard` | Focused product and rate-card setup guidance with bounded seat pricing context. |
| 3 | `manage-subscription-lifecycle` | Subscription lifecycle guide | 73 | `standard` | Compact operational guide for trials, pricing changes, upgrades, downgrades, and cancellation. |
| 4 | `role-based-access-rbac` | Access-control guide | 65 | `standard` | Short self-contained role and token assignment guide extending the existing security concept. |
| 5 | `pay-as-you-go` | Commercial-model guide | 187 | `standard` | Representative medium commercial-model guide grounded in existing billing objects. |
| 6 | `planning-billing-architecture` | Cross-object architecture guide | 110 | `strong` | Cross-object architecture guidance spanning value exchange, data, commercial model, and system design. |
| 7 | `manual-payment-gated-commits` | Payment-gated commit guide | 89 | `strong` | Payment outcome, Stripe mapping, webhook, and retry boundaries require careful treatment. |
| 8 | `create-a-trial` | Trial configuration guide | 294 | `strong` | Credit-based and uncapped trial paths join contracts, alerts, usage, and time-bound overrides. |
| 9 | `get-a-billable-metric` | Billable-metric API | 318 | `strong` | OpenAPI response schema covers archival matching, aggregation groups, custom fields, and SQL metric boundaries. |
| 10 | `get-billable-metrics-for-customer` | Customer billable-metrics API | 384 | `strong` | Largest selected schema-heavy API covering customer scope, pagination, plan-status filtering, and archived metrics. |

Total selected raw lines: 1,636. Routing balance: five `standard` jobs and five `strong` jobs.

The total is deliberately comparable with Campaign 06: 1,636 lines here versus 1,641 lines there, with the same five-standard/five-strong balance. The scale therefore tests the approved review architecture rather than changing both workload size and workflow at once.

## Shared-reduction clusters

- Three subscription guides share a subscription concept target.
- `create-a-trial` and `manual-payment-gated-commits` both touch credit, commit, alert, usage, and lifecycle boundaries.
- The two billable-metric APIs share schema and metric-concept context.

Candidates remain one raw source per job. Once individual reviewer approvals exist, the coordinator groups and reduces durable shared-file suggestions by target; it does not combine raw pages into a batch source summary.

## Audit set

The immutable manifest records these three distinct audit jobs before execution:

1. `subscription-overview` — the required standard-page sample.
2. `get-billable-metrics-for-customer` — the longest selected and schema-heaviest page.
3. `pay-as-you-go` — the ordinary manifest sample.

The independent auditor reads each complete raw/source pair and asks one core, one boundary, and one trap question. Any material partial or fail expands the audit to every campaign page.

## Runtime allocation and ownership

The coordinator uses the coordinator role plus three current subagent slots. `standard` workers map to GPT-5.6 Terra and `strong` workers to GPT-5.6 Sol. Every candidate receives a distinct, fresh GPT-5.6 Sol reviewer; reviewer and worker identities must differ.

Configured worker concurrency is the portable ceiling of five, review concurrency is three, and the current host remains bounded by `total_subagent_slots=3`. While jobs remain queued, the shared-slot policy preserves one worker and therefore allows at most two simultaneous reviews; after the worker queue is empty, all three slots may review. Dynamic refill has no batch barrier: ready reviews receive available capacity under that policy, then queued workers fill what remains. The coordinator is the only repository writer and does not default to a third raw read; it rereads only the approved-design exceptions (dispute, uncertain review, unresolved retry risk, manifest-designated high risk, or final audit sample).

## Deterministic checks and acceptance gates

Before initialization, the proposal must mechanically confirm selected raw-file existence and non-symlink status, SHA-256 values, canonical URLs after terminal `.md` normalization, current pending state, unique absent source targets, exact line total, routing balance, and the three valid selected audit IDs. A temporary-root initialization must also preserve `review_concurrency=3` and the ordered audit set without creating repository campaign state.

During execution, worker handoff checks raw SHA-256, canonical URL, exact result keys, and three to five byte-matching quotes. Reviewer handoff checks a complete raw read, factual and boundary completeness, contradiction and unknown preservation, raw/source/related-link intent, and shared-file suggestion completeness. Campaign close validates all promoted sources, touched concepts and company page, every campaign raw link and manifest hash, company/index/log/links/counts, and the Metronome capsule; the full unit suite runs only when campaign code, rules, or validators changed.

Campaign 07 can validate the approved workflow only if every promoted page has a distinct worker and Sol reviewer, workers and reviewers make no repository writes, coordinator rereads stay within declared exceptions, shared-file reduction is applied once except for a verified repair, campaign-wide deterministic checks pass, the three-page audit has no material expansion finding, elapsed time and coordinator repair work improve over Campaign 06, and the sampled query audit has no quality regression.

## Explicit stop

Initialization and dispatch require user approval of this exact proposal. This proposal creates neither campaign state nor jobs, events, monitors, attempts, candidates, source pages, or canonical wiki changes.
