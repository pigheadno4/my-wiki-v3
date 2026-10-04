# Braintree C34 selection

Status: COMPLETE — exact manifest approved and executed on 2026-10-04. Runtime 2026-10-04T04:48:48Z to 2026-10-04T05:21:52Z (33m04s); twenty sources approved, forty final queries passed after one navigation-edge repair, thirty typed pages validated. C33 is committed/pushed at 637a110526037d5fd34cda33276c7164c6437b84; C34 remains uncommitted and unpushed.

Preparation verification: twenty hashes, unique canonical URLs and absent targets passed; existing runtime accepts review_concurrency 10. Full unit discovery did not pass: it stopped in the unrelated GitHub secret-scanning test (`test_release_notes_are_secret_scanned_before_publication`) because `SecretFindingsBlocked` rejects traceback assignment under Python 3.12. No GitHub code was changed or repaired here; do not report the full suite as passing. C33's targeted close checks passed before its commit.

## Scope and preflight

Twenty previously unowned canonical website raws: seven Chase processor articles, seven Adyen processor articles, and six account/refund/security guides. Metadata-only selection; no product facts inferred from unread raw. Exact hashes, URLs and absent source targets are pinned. Baseline 332 = 315 website + 17 GitHub; all twenty approved would yield 352 = 335 website + 17 GitHub. No collection, refresh or GitHub ingestion.

Primary volume 1682 lines, versus C33 3937. Longest first, ties by job ID. Different content and volume mean elapsed time is not a controlled concurrency comparison.

## Capacity and roles

Requested pool: ten child agents excluding coordinator. Workers, reviewers and auditors share this pool; worker_concurrency/review_concurrency are per-role ceilings, not additive pools. The session capacity declaration now exposes eleven total slots including coordinator, permitting ten children. Ten-child simultaneous dispatch has not yet been exercised; honor actual capacity and report any runtime limit rather than silently running a different concurrency experiment.

Sol medium workers; different Sol high initial reviewers; existing review-first allocation and worker reserve, targeted correction priority, at most three attempts. A completed agent immediately frees its active-work slot for eligible review or work; no batch barrier. Coordinator alone writes canonical/shared/state files. No new scheduler, registry, role, worktree or validation layer.

## Pinned queue

| Position | Job | Lines | Raw |
| --- | --- | ---: | --- |
| 1 | `articles-guides-at-most-once` | 204 | `raw/braintree/articles/guides/at-most-once-2026-09-16.md` |
| 2 | `articles-guides-refund-authorizations` | 193 | `raw/braintree/articles/guides/refund-authorizations-2026-09-16.md` |
| 3 | `articles-guides-account-updater` | 174 | `raw/braintree/articles/guides/account-updater-2026-09-16.md` |
| 4 | `articles-adyen-reconciliation` | 137 | `raw/braintree/articles/adyen/reconciliation-2026-09-16.md` |
| 5 | `articles-guides-account-information` | 130 | `raw/braintree/articles/guides/account-information-2026-09-16.md` |
| 6 | `articles-chase-transactions-descriptors` | 112 | `raw/braintree/articles/chase/transactions/descriptors-2026-09-16.md` |
| 7 | `articles-adyen-transactions-descriptors` | 96 | `raw/braintree/articles/adyen/transactions/descriptors-2026-09-16.md` |
| 8 | `articles-chase-transactions-accepted-payment-methods` | 83 | `raw/braintree/articles/chase/transactions/accepted-payment-methods-2026-09-16.md` |
| 9 | `articles-adyen-pricing-fees` | 78 | `raw/braintree/articles/adyen/pricing-fees-2026-09-16.md` |
| 10 | `articles-adyen-change-your-bank-account` | 60 | `raw/braintree/articles/adyen/change-your-bank-account-2026-09-16.md` |
| 11 | `articles-chase-pricing-fees` | 60 | `raw/braintree/articles/chase/pricing-fees-2026-09-16.md` |
| 12 | `articles-risk-and-security-allowlisting` | 60 | `raw/braintree/articles/risk-and-security/allowlisting-2026-09-16.md` |
| 13 | `articles-risk-and-security-overview` | 58 | `raw/braintree/articles/risk-and-security/overview-2026-09-16.md` |
| 14 | `articles-chase-change-your-bank-account` | 52 | `raw/braintree/articles/chase/change-your-bank-account-2026-09-16.md` |
| 15 | `articles-chase-transactions-settlement-funding-timeline` | 48 | `raw/braintree/articles/chase/transactions/settlement-funding-timeline-2026-09-16.md` |
| 16 | `articles-adyen-transactions-accepted-payment-methods` | 36 | `raw/braintree/articles/adyen/transactions/accepted-payment-methods-2026-09-16.md` |
| 17 | `articles-adyen-overview` | 27 | `raw/braintree/articles/adyen/overview-2026-09-16.md` |
| 18 | `articles-chase-overview` | 27 | `raw/braintree/articles/chase/overview-2026-09-16.md` |
| 19 | `articles-chase-reporting-reconciliation` | 24 | `raw/braintree/articles/chase/reporting-reconciliation-2026-09-16.md` |
| 20 | `articles-adyen-transactions-settlement-funding-timeline` | 23 | `raw/braintree/articles/adyen/transactions/settlement-funding-timeline-2026-09-16.md` |

## Fixed query allocation

Five dispatch-order groups, four pages and eight questions each, forty total. Dispatch a group only when its four approved canonical routes exist; auditors share the same rolling pool.

- A: `articles-guides-at-most-once`; `articles-guides-refund-authorizations`; `articles-guides-account-updater`; `articles-adyen-reconciliation`
- B: `articles-guides-account-information`; `articles-chase-transactions-descriptors`; `articles-adyen-transactions-descriptors`; `articles-chase-transactions-accepted-payment-methods`
- C: `articles-adyen-pricing-fees`; `articles-adyen-change-your-bank-account`; `articles-chase-pricing-fees`; `articles-risk-and-security-allowlisting`
- D: `articles-risk-and-security-overview`; `articles-chase-change-your-bank-account`; `articles-chase-transactions-settlement-funding-timeline`; `articles-adyen-transactions-accepted-payment-methods`
- E: `articles-adyen-overview`; `articles-chase-overview`; `articles-chase-reporting-reconciliation`; `articles-adyen-transactions-settlement-funding-timeline`

For EACH exact named page, ask:
1. Where does root index → Braintree index → relevant concept → source → pinned raw locate this page's specific processor/account/operation, and which region, pricing model or scope qualifications does the raw actually document?
2. What is this page's central action or commercial/operational responsibility, with its material prerequisites, warnings and limitations? Where are its documented detailed values or instructions located? Do not invent specifics absent from a sparse page or import them from another processor.

Auditors read CLAUDE.md, rules/query-and-synthesis.md and selected evidence fully, verify hashes and object/action identity, and record direct answers with exact locators and PASS/FAIL. Read additional authority for discovered relevant conflicts or answers needing it. One route per page, two concise answers; record shared gap sweep, extra reads and reciprocal checks once. Any material retrieval failure blocks successful close and expands coverage as required. No repeated stylistic polishing; distinguish analysis end from handoff time.

## Short delegated scope notes

Use rules/ingest-roles.md, trusted order and these notes. Start index → Braintree index → relevant existing concept. Audit the main concept's pertinent section; do not force all pages onto one hub or create processor concepts from metadata. If a genuine new hub is needed, coordinator assigns one proposal owner and supplies the reviewed route to later jobs. Never reject an earlier approved page merely because a new route appears later.

These Adyen/Chase articles are Braintree-owned documentation, not independent current Adyen/Chase authority, and not the C33 Orchestration integration guides. Preserve documented regional, merchant, processor, account and pricing scope. Never transfer fees, payment-method availability, descriptors, funding timelines or bank-change procedures between processors or regions. Funding schedule is not proof of an individual deposit. Check subject/condition/action for retained claims.

Sources are accurate retrieval entries, not replacement specifications. Retain central meaning and consequential warnings; route routine tables/parameters/procedures to verified raw locations. Do not add absence inventories or repeated generic caveats. Quotes need exact verified locations; navigation labels need no per-label quote. Fully read factual evidence belongs in raw_files and Raw Sources; unread navigation stays separate. Raw immutability establishes provenance, not upstream correctness/current support. Reverse raw lookup derives from raw_files; never edit raw.

## Promotion and close

Persist trusted orders and immediately dispatch; fill eligible free slots before promotion/report prose. Each initial candidate receives independent full review. Use targeted retry only for bounded impact with unchanged evidence and prior findings; full review for broad uncertainty. Coordinator does not perform a default third full raw read.

Serial promotion: approved concept updates precede exact accepted candidate bytes; aggregate company/index/log/count once. One close checks equality, hashes, ownership, approved updates, factual/navigation and reciprocal links, unique catalogs/counts and touched typed pages. No documentation-only repeated unit suite. Track existing UTC milestones, first-pass/retry counts and words without new fields. Preparation authorizes neither execution nor commit/push of these draft files.
