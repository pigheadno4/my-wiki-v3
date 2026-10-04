# Braintree C35 selection

Status: ACTIVE — exact manifest approved; execution started 2026-10-04T05:32:25Z. C34 committed and pushed at 1c48fa10442c7dc0faaf0905ad11acef4ae6363d; remote main independently verified. C35 commit/push is not authorized.

## Scope and preflight

Twenty previously unowned canonical website raws: ten Wells IC articles and ten Wells Flat articles. Selection is metadata-only; no product claims inferred from unread raw. Hashes, canonical URLs and absent source targets are pinned in manifest.json. Primary volume: 2216 lines (C34: 1682); differing content and volume prevent a concurrency-only timing comparison.

Baseline 352 = 335 website + 17 GitHub. Twenty approvals would yield 372 = 355 website + 17 GitHub. No collection, refresh, GitHub ingestion or historical source migration.

## Roles and rolling capacity

Ten shared child slots excluding coordinator, bounded by actual capacity. The session exposes eleven total slots; C34 confirmed ten simultaneous children. Workers, reviewers and auditors share this pool, not ten slots each. Sol medium workers; different Sol high initial reviewers; existing review-first allocation and worker reserve, correction priority, maximum three attempts. Refill eligible slots immediately, without a batch barrier. Coordinator alone writes canonical/shared/state files.

Every worker fully reads its raw; every initial candidate receives independent full review. Targeted retry requires unchanged evidence and a bounded correction; broad uncertainty requires full review. Coordinator does not add a default third full raw read. No new scheduler, registry, role, worktree or validation layer.

## Pinned queue

| Position | Job | Lines | Raw |
| --- | --- | ---: | --- |
| 1 | `articles-wells-flat-chargebacks-retrievals-prearbs` | 239 | `raw/braintree/articles/wells-flat/chargebacks-retrievals-prearbs-2026-09-16.md` |
| 2 | `articles-wells-ic-chargebacks-retrievals-prearbs` | 210 | `raw/braintree/articles/wells-ic/chargebacks-retrievals-prearbs-2026-09-16.md` |
| 3 | `articles-wells-ic-statements-reconciliation` | 202 | `raw/braintree/articles/wells-ic/statements-reconciliation-2026-09-16.md` |
| 4 | `articles-wells-flat-statements-reconciliation` | 193 | `raw/braintree/articles/wells-flat/statements-reconciliation-2026-09-16.md` |
| 5 | `articles-wells-flat-braintree-marketplace-statements-reconciliation` | 161 | `raw/braintree/articles/wells-flat/braintree-marketplace-statements-reconciliation-2026-09-16.md` |
| 6 | `articles-wells-ic-braintree-marketplace-statements-reconciliation` | 157 | `raw/braintree/articles/wells-ic/braintree-marketplace-statements-reconciliation-2026-09-16.md` |
| 7 | `articles-wells-ic-transactions-descriptors` | 125 | `raw/braintree/articles/wells-ic/transactions/descriptors-2026-09-16.md` |
| 8 | `articles-wells-flat-transactions-descriptors` | 121 | `raw/braintree/articles/wells-flat/transactions/descriptors-2026-09-16.md` |
| 9 | `articles-wells-flat-transactions-accepted-payment-methods` | 96 | `raw/braintree/articles/wells-flat/transactions/accepted-payment-methods-2026-09-16.md` |
| 10 | `articles-wells-ic-transactions-accepted-payment-methods` | 96 | `raw/braintree/articles/wells-ic/transactions/accepted-payment-methods-2026-09-16.md` |
| 11 | `articles-wells-ic-pricing-fees` | 80 | `raw/braintree/articles/wells-ic/pricing-fees-2026-09-16.md` |
| 12 | `articles-wells-flat-pricing-fees` | 78 | `raw/braintree/articles/wells-flat/pricing-fees-2026-09-16.md` |
| 13 | `articles-wells-flat-change-your-bank-account` | 76 | `raw/braintree/articles/wells-flat/change-your-bank-account-2026-09-16.md` |
| 14 | `articles-wells-ic-change-your-bank-account` | 76 | `raw/braintree/articles/wells-ic/change-your-bank-account-2026-09-16.md` |
| 15 | `articles-wells-flat-transactions-settlement-funding-timeline` | 75 | `raw/braintree/articles/wells-flat/transactions/settlement-funding-timeline-2026-09-16.md` |
| 16 | `articles-wells-ic-transactions-settlement-funding-timeline` | 75 | `raw/braintree/articles/wells-ic/transactions/settlement-funding-timeline-2026-09-16.md` |
| 17 | `articles-wells-ic-transactions-level-2-and-3-processing` | 60 | `raw/braintree/articles/wells-ic/transactions/level-2-and-3-processing-2026-09-16.md` |
| 18 | `articles-wells-flat-pre-dispute-programs` | 50 | `raw/braintree/articles/wells-flat/pre-dispute-programs-2026-09-16.md` |
| 19 | `articles-wells-flat-overview` | 23 | `raw/braintree/articles/wells-flat/overview-2026-09-16.md` |
| 20 | `articles-wells-ic-overview` | 23 | `raw/braintree/articles/wells-ic/overview-2026-09-16.md` |

## Fixed query allocation

Five dispatch-order groups, four pages/eight questions each, forty total. Dispatch each group when its four approved canonical routes exist; auditors use the same rolling pool.

- A: `articles-wells-flat-chargebacks-retrievals-prearbs`; `articles-wells-ic-chargebacks-retrievals-prearbs`; `articles-wells-ic-statements-reconciliation`; `articles-wells-flat-statements-reconciliation`
- B: `articles-wells-flat-braintree-marketplace-statements-reconciliation`; `articles-wells-ic-braintree-marketplace-statements-reconciliation`; `articles-wells-ic-transactions-descriptors`; `articles-wells-flat-transactions-descriptors`
- C: `articles-wells-flat-transactions-accepted-payment-methods`; `articles-wells-ic-transactions-accepted-payment-methods`; `articles-wells-ic-pricing-fees`; `articles-wells-flat-pricing-fees`
- D: `articles-wells-flat-change-your-bank-account`; `articles-wells-ic-change-your-bank-account`; `articles-wells-flat-transactions-settlement-funding-timeline`; `articles-wells-ic-transactions-settlement-funding-timeline`
- E: `articles-wells-ic-transactions-level-2-and-3-processing`; `articles-wells-flat-pre-dispute-programs`; `articles-wells-flat-overview`; `articles-wells-ic-overview`

For EACH exact named page:
1. Locate root index → Braintree index → relevant concept → source → pinned raw. What exact processor/account/pricing-model scope is documented?
2. What is the page's central purpose or action, with consequential prerequisites, warnings and limitations? Where are the detailed instructions or values in raw?

Auditors read CLAUDE.md, rules/query-and-synthesis.md and selected evidence fully. Verify hashes, subject/condition/action, reciprocal routes and any discovered relevant conflicts. Record one explicit route and two concise supported answers per page with locators and PASS/FAIL; shared gap checks and extra reads once per report. Do not copy routine inventories or repeat generic caveats. Sparse pages do not justify invented detail. Material retrieval failures block successful close and require appropriate expanded checks. Preserve original failure evidence and distinguish analysis end from report handoff.

## Short delegated scope notes

Workers/reviewers use rules/ingest-roles.md, trusted order and these notes. Start index → Braintree index → relevant concept and inspect its pertinent section. New hubs require a genuine topic gap, one assigned proposal owner and a reviewed route supplied to later jobs.

These are Braintree-owned captured Wells IC/Wells Flat articles, not independent current Wells Fargo policy. Preserve exact processor/account/pricing, region and availability qualifications found in the raw. Never transfer fees, funding schedules, statement rules, descriptors or dispute behavior between the two variants. Marketplace statements and ordinary merchant statements must remain distinguishable. Funding schedules do not prove individual deposits. A documented Control Panel procedure does not prove an API route is unavailable.

Sources are retrieval entries, not replacement specifications. Retain central meaning and consequential warnings; route routine procedures/tables to verified raw locations. Quotes have exact locators; navigation labels need no per-label quote. Fully read evidence belongs in raw_files and Raw Sources; unread references remain separate. Reverse raw lookup derives from raw_files; never edit raw. Immutable storage establishes provenance, not upstream correctness or current support.

## Two small approved optimizations

- During the existing catalog update, ensure EVERY source's main concept is reachable from the Braintree index, including generic concepts such as payment-reconciliation-reporting. Check reciprocal source/concept/raw routes in the existing close step. No extra registry or validation round.
- Prefer shorter purpose-fit source and query prose: avoid repeated qualifications and unneeded schema/fee inventories; keep material conditions and warnings. No hard word cap, evidence-read waiver or reviewer waiver. Shorten redundant reporting, not required verification.

## Promotion, close and timing

Persist trusted orders and dispatch immediately; fill eligible free slots before promotion/report prose. Serial promotion applies individually approved concept updates followed by exact accepted candidate bytes. Aggregate company/index/log/count once. One close checks equality, hashes, ownership, exact approved updates, factual/navigation/reciprocal links, catalog uniqueness and counts; one touched typed-page validation. No repeated documentation-only full unit suite.

Use existing UTC milestones for dispatch, worker/review, catalog work, query analysis/handoff and close, plus first-pass/retry/word counts; no new monitoring fields or machinery. C34's unrelated GitHub unit-suite failure remains unresolved and outside scope. Preparation does not authorize execution or commit/push of these draft files.
