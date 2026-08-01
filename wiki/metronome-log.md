---
title: "Metronome Collection and Ingest Log"
type: log
tags: [metronome, usage-based-billing, operations]
---

Newest entries appear first. Detailed collection evidence remains under `tracking/collections/metronome/`; ingest evidence remains under `tracking/ingest/metronome/`.

## 2026-08-01 — Metronome Campaign 09 completed

- Result: ten approved source pages from complete raw pages across thirteen worker/reviewer attempts; three reviews requested bounded corrections, no job was rejected, and one coordinator formatting repair prevented a JSON array from being interpreted as a wikilink. The immutable three-page audit passed 3/3 pages and 9/9 future-query tests, so no expanded audit was required.
- Sources:
  - [[source-metronome-guides-pricing-packaging-billing-model-guides-guides-home]] — billing-model navigation for pay-as-you-go, enterprise commits, usage subscriptions, and pre-paid credits (raw SHA-256 `c0e56629644cd181e7deb54cb6af94c7c806298739c131d34468f18d45ac49dc`)
  - [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-alerts]] — credit and commit threshold dimensions, custom-field filtering, and action boundaries (raw SHA-256 `d814acd9f7edd119e1c1a5dc305dd20b8b1c75304249fe9a5de0ed4a6c2af2ac`)
  - [[source-metronome-guides-pricing-packaging-overview]] — pricing-and-packaging navigation across billing models, changes, credits, commits, and examples (raw SHA-256 `54ccfe03556452023711ff149fad16153f31ed289ff0233a76a17f69c7e6afaf`)
  - [[source-metronome-guides-platform-configuration-metronome-pricing-model]] — platform fee and consumption accounting for accepted events, generated billings, and exported rows (raw SHA-256 `a2fa7ab4ec7a6da68ec7dd8bd7f2205228e388f82a29d6b3c9ce446c1fd46008`)
  - [[source-metronome-guides-implement-metronome-core-concepts-billable-metrics-basic-filters]] — Basic Filters matching, property requirements, grouped counting, and streaming aggregation boundaries (raw SHA-256 `d934d873c509b5962de5ef14414c4919ec279c9142edccf507a4ae1907e5a89f`)
  - [[source-metronome-guides-pricing-packaging-make-pricing-changes-use-currency-custompricingunits]] — fiat denomination, custom-unit rates, balance drawdown, and residual invoice conversion (raw SHA-256 `be3d1ee69264848cf3d8869d3ca7b1f61767378abfe17b266362e21bed3623fe`)
  - [[source-metronome-guides-events-send-usage-events]] — event fields, customer attribution, retry policy, heartbeat IDs, and duplicate-suppression scope (raw SHA-256 `5fdd07cf1b27bb098d4facfe48a50a3043623e2476475d20d0a3965b0f4fba56`)
  - [[source-metronome-guides-invoices-invoice-optimization-issue-credit-memos]] — future credits, external A/R memos, invoice-state corrections, re-billing, and refund ownership (raw SHA-256 `e21b6730a2334f3f4665dba5b0488e5790d5dba5e6bbaede6fee06a6aa7a608f`)
  - [[source-metronome-api-reference-security-get-services]] — bearer-authenticated service registry, IP direction labels, schema, and notice boundary (raw SHA-256 `ed652135505abf971cbed018ce28264543434c7828f64bbd26c648c99ad1a5fa`)
  - [[source-metronome-api-reference-alerts-reset-a-threshold-notification]] — threshold reset, asynchronous reassessment, empty success response, and idempotency unknowns (raw SHA-256 `c25a9c284ee921af560595ff488771555905e4db2e067e311b7931bd59b9735a`)
- Concepts: created [[metronome-currencies-and-custom-pricing-units]]; updated alerts, API idempotency, billable metrics, credits and commits, customer contracts, event ingestion, invoicing, products and rate cards, reporting, security, and usage-based-billing boundaries.
- Boundaries retained: navigation pages do not prove implementation semantics; Metronome's own platform-pricing terms are distinct from merchant-configured end-user pricing; non-USD denomination follows the documented Metronome encoding rather than inferred ISO minor-unit scaling; finalized-invoice correction and beyond-34-day routes remain explicitly ambiguous; event transaction IDs are not treated as permanent global uniqueness.
- Coverage after promotion: 225 collected documentation pages, 70 ingested source summaries, and 155 pending pages.

## 2026-07-31 — Metronome Campaign 08 completed

- Result: ten approved source candidates from complete raw pages, including four bounded targeted retries with unchanged raw hashes; no job was rejected. The immutable three-page query audit passed 3/3 pages and 9/9 future-query tests, so no expanded audit was required.
- Sources:
  - [[source-metronome-guides-customers-billing-overview]] — Customers & Billing navigation across lifecycle management, dashboards and spend controls, fraud and entitlement themes, and alerts (raw SHA-256 `c122107b4e1533e19f297582807a032d0b2447a15e964d2fc0ccee817caa3cdc`)
  - [[source-metronome-guides-customers-billing-manage-customers-manage-product-access]] — product-access navigation overview spanning customer provisioning, contract lifecycle, temporary trials, and entitlement-state notifications (raw SHA-256 `42bee2588c3e27fc0e984e047bb87578da11180a3cc9eeaf3b9dcf49907ce1a1`)
  - [[source-metronome-guides-customers-billing-set-up-notifications-create-and-manage-notifications]] — notification families, webhook delivery, evaluation timing, and threshold states (raw SHA-256 `7c0125db5f4ab812a70d96d8d79b5a32942a1b05b0419820fea001b11ae57d5a`)
  - [[source-metronome-guides-customers-billing-optimize-customer-experience-india-e-mandates]] — Indian-card Stripe mandate setup, threshold and recurring configuration, invoice mapping, and responsibility boundaries (raw SHA-256 `a143201d70f01039a6a13cfc9ab4be02270bd632ce56d9fcf84ea94c9389d8f5`)
  - [[source-metronome-guides-customers-billing-set-up-notifications-offset-notifications]] — relative-time offsets, payload semantics, prospective behavior, setup paths, and recurring-commit caveat (raw SHA-256 `3d638b97de733aa9366dafb8b2fdc265294b5d33a96431ea9530e6c4cda819a7`)
  - [[source-metronome-guides-customers-billing-manage-customers-spend-trackers]] — public-beta commit-purchase accumulation, threshold-discount caps, contract retrieval, and enforcement boundaries (raw SHA-256 `8327257a20bcb8b0989cd2024d03e5a9bc1e47136d10416b44c9f38a553d47eb`)
  - [[source-metronome-guides-customers-billing-optimize-customer-experience-set-customer-spend-control]] — contract spend thresholds, incremental billing, configuration updates, and Stripe/external payment gates (raw SHA-256 `6ce6ff23625a045cf60d50be5fc0beface0da6f47017f44f991e31ee8520489e`)
  - [[source-metronome-guides-customers-billing-optimize-customer-experience-preview-event-cost]] — contract-aware event-cost simulation, preview modes, multi-contract draft output, deduplication conflict, and limits (raw SHA-256 `b27a060efe5d9d1a8507e143fa468a4e5890dd028bb0ccb902c8053c9d26a7d3`)
  - [[source-metronome-guides-customers-billing-optimize-customer-experience-customer-controls]] — customer-defined spend, grouped-dimension, commit-balance, and invoice-total alerts with merchant enforcement (raw SHA-256 `9a2128829a46fce304d3b48229d4f71a8fc7c9f6888f4c5a2e523b638fd58685`)
  - [[source-metronome-guides-customers-billing-optimize-customer-experience-get-remaining-balance]] — aggregate and ledger balance retrieval, signed calculation, precision, timestamps, and manual adjustments (raw SHA-256 `2f427835858daeeb9f71ff4ce25b53a08d0b62ea9d2dc3edba5cf6f182351bae`)
- Concepts: created [[metronome-spend-trackers]] and [[metronome-spend-threshold-billing]]; updated alerts, billable metrics, credits and commits, customer contracts, event ingestion, integrations, invoicing, usage billing, webhooks, and Stripe saved-payment-method boundaries.
- Boundaries retained: navigation pages do not prove implementation semantics; alerts and spend controls do not automatically enforce merchant access; preview results are not processed usage or finalized invoices; mandate attachment is not payment success; spend trackers remain Public Beta.
- Coverage after promotion: 225 collected documentation pages, 60 ingested source summaries, and 165 pending pages.

## 2026-07-30 — Metronome Campaign 07 completed

- Result: ten approved jobs, sixteen worker/reviewer attempts, zero failed jobs, and zero rejected jobs; coverage is 225 raw / 50 ingested / 175 pending.
- Routing: five standard jobs used Terra workers and five strong jobs used Sol workers; every candidate received a distinct fresh Sol full-source review. Strong workers passed first review on 4/5 pages, while standard workers passed first review on 1/5 pages.
- Dynamic scheduling: three shared sub-agent slots used review-first refill with one worker reserved only when queued work remained and no worker was active; no batch barrier or per-agent worktree was used.
- Promotion: created [[metronome-subscriptions]] and [[metronome-alerts-and-notifications]], updated eleven existing Metronome concepts, and promoted the ten approved sources with exact canonical URLs and path-qualified raw backlinks.
- Sources: [[source-metronome-guides-pricing-packaging-subscription-subscription-overview]], [[source-metronome-guides-pricing-packaging-subscription-define-subscription-pricing]], [[source-metronome-guides-pricing-packaging-subscription-manage-subscription-lifecycle]], [[source-metronome-guides-platform-configuration-role-based-access-rbac]], [[source-metronome-guides-pricing-packaging-billing-model-guides-pay-as-you-go]], [[source-metronome-guides-implement-metronome-planning-your-billing-architecture]], [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-manual-payment-gated-commits]], [[source-metronome-guides-pricing-packaging-billing-model-guides-create-a-trial]], [[source-metronome-api-reference-billable-metrics-get-a-billable-metric]], and [[source-metronome-api-reference-billable-metrics-get-billable-metrics-for-a-customer]].
- Verification: ten manifest hashes, promoted-candidate byte equality, canonical/raw links, company/index entries, and required fact backlinks pass; targeted validation passes for all 25 frontmatter-bearing touched pages, and the capsule reports 225 raw / 50 sources / 175 pending.
- Independent query audit: the three immutable manifest samples passed 9/9 queries with 0 partial and 0 fail; no expansion to all ten pages was required.
- Pilot issues retained for follow-up: an initial temporary status-literal prompt error was blocked before campaign mutation; one worker identity label did not match its authoritative job name although the correct raw/order was processed; and one coordinator backlink omission was found and repaired before audit. The journal lacks timestamps, so no measured elapsed-time improvement is claimed.
- Evidence: [selection and result](../tracking/ingest/metronome/metronome-campaign-07/selection-review.md), [quality audit](../tracking/ingest/metronome/metronome-campaign-07/quality-audit.md), [monitor](../tracking/ingest/metronome/metronome-campaign-07/monitor.md), and [event journal](../tracking/ingest/metronome/metronome-campaign-07/events.jsonl).

## 2026-07-30 — Metronome Campaign 06 completed

- Result: ten approved jobs, one retained failed attempt, one successful retry, and zero rejected jobs; coverage is 225 raw / 40 ingested / 185 pending.
- Routing and scheduling: five Terra standard candidates and five Sol strong candidates, with at most three workers active and immediate refill rather than batch barriers.
- Independent query audit: initial 29 pass / 1 partial / 0 fail; after restoring one customer-creation recommendation, final 30 pass / 0 partial / 0 fail.
- Verification: all manifest hashes match, ten sources pass targeted validation, capsule counts reconcile, and the full 548-test suite passed.
- Graduation: Campaign content passes, but reduced testing and parallel review remain disabled because `provision-customer` attempt 1 failed the zero-malformed-first-attempt criterion.
- Link policy: company and provider index remain exhaustive; concept backlinks are required for durable factual contribution, not navigation-only symmetry.
- Evidence: [selection and result](../tracking/ingest/metronome/metronome-campaign-06/selection-review.md), [quality audit](../tracking/ingest/metronome/metronome-campaign-06/quality-audit.md), [monitor](../tracking/ingest/metronome/metronome-campaign-06/monitor.md), and [event journal](../tracking/ingest/metronome/metronome-campaign-06/events.jsonl).

## 2026-07-30 — Canonical ingest: Provision a Customer

- Ingested: [[source-metronome-guides-implement-metronome-core-concepts-provision-customer]] from the complete 124-line guide.
- Concept audit updated contracts, integrations, and invoicing with alias hierarchy, retroactive association, contract-required rating, customer-versus-contract provider assignment, and beta archival behavior.
- Terra attempt 1 failed deterministic quote validation; its receipt remains in the campaign journal. A fresh Terra worker produced a byte-for-byte verified attempt 2, which then passed serial full-raw Sol review.
- Full customer schema, alias limits, errors, idempotency, non-AWS provider fields, and invoice lifecycle remain delegated to dedicated sources.
- Coverage after finalization: 40 source summaries ingested and 185 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-06/monitor.md), [failed attempt](../tracking/ingest/metronome/metronome-campaign-06/attempts/provision-customer/attempt-1/failure.json), and [approved attempt](../tracking/ingest/metronome/metronome-campaign-06/attempts/provision-customer/attempt-2/receipt.json).

## 2026-07-30 — Canonical ingest: Create a Billable Metric API

- Ingested: [[source-metronome-api-reference-billable-metrics-create-a-billable-metric]] from the complete 342-line endpoint reference.
- Concept audit updated [[metronome-billable-metrics]] with SQL exclusivity, all-filter matching, enum spellings, aggregation-key constraints, nested group keys, and response shape.
- Sol review preserved contradictions around `UNIQUE`, aggregation-key requiredness, empty `not_in_values`, and an optional request body whose payload requires `name`.
- Errors, limits, retry, idempotency, SQL output rules, group-key limits, and batch semantics remain undocumented.
- Campaign 06: the strong-tier Sol candidate passed fixed-schema validation on attempt 1 before serial full-raw Sol review.
- Coverage after finalization: 39 source summaries ingested and 186 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-06/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-06/attempts/create-a-billable-metric/attempt-1/receipt.json).

## 2026-07-30 — Canonical ingest: Create and Manage Rate Cards

- Ingested: [[source-metronome-guides-implement-metronome-core-concepts-create-manage-rate-cards]] from the complete 264-line guide.
- Concept audit updated products and rate cards, billable metrics, and contracts with creation fields, aliases, one-currency scope, scheduled rates, dimensional relationships, tier boundaries, and provisioning effects.
- Sol review preserved the `/addRates` versus `/addRate` and `"FLAT"` versus `"tiered"` inconsistencies, plus the tension between “all contracts use rate cards” and the optional create-contract card/package family.
- Alias overlap, rate overlap, fallback, removal, currency changes, limits, grandfathering, and invoice recalculation remain undocumented.
- Campaign 06: the strong-tier Sol candidate passed fixed-schema validation on attempt 1 before serial full-raw Sol review.
- Coverage after finalization: 38 source summaries ingested and 187 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-06/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-06/attempts/create-manage-rate-cards/attempt-1/receipt.json).

## 2026-07-30 — Canonical ingest: Provision a Customer Contract

- Ingested: [[source-metronome-guides-implement-metronome-core-concepts-provision-contract]] from the complete 213-line implementation guide.
- Concept audit updated contracts, products and rate cards, credits and commits, invoicing, and billable metrics with prerequisites, charge schedules, consolidation, provider attachment, tag discounts, and usage-filter constraints.
- Sol review retained the prerequisite-versus-later-attachment tension and the possible conflict between current-period marketplace attachment and next-period-only marketplace transitions.
- Undocumented amount denomination, nested validation, override precedence, filter overlap/no-match behavior, backdating, errors, and retry semantics remain explicit.
- Campaign 06: the strong-tier Sol candidate passed fixed-schema validation on attempt 1 before serial full-raw Sol review.
- Coverage after finalization: 37 source summaries ingested and 188 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-06/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-06/attempts/provision-contract/attempt-1/receipt.json).

## 2026-07-30 — Canonical ingest: How Metronome Works

- Ingested: [[source-metronome-guides-get-started-how-metronome-works]] from the complete 163-line architecture guide.
- Concept audit: updated usage billing, event ingestion, billable metrics, products and rate cards, contracts, invoicing, webhooks, and integrations with the ordered object model and timing boundaries.
- Sol review retained the one-event-to-many-metrics relationship; shared-price versus customer-term separation; what/how/where contract framing; and the distinction among event-time evaluation, API visibility, and cycle-close finalization.
- Broad claims about no-code evolution, automatic pricing propagation, support for any commercial model, and real-time behavior remain non-guaranteed; precedence, grandfathering, latency, lifecycle, and downstream-delivery semantics remain undocumented.
- Campaign 06: the strong-tier Sol candidate passed fixed-schema validation on attempt 1 before serial full-raw Sol review.
- Coverage after finalization: 36 source summaries ingested and 189 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-06/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-06/attempts/how-metronome-works/attempt-1/receipt.json).

## 2026-07-30 — Canonical ingest: Create Products

- Ingested: [[source-metronome-guides-implement-metronome-core-concepts-create-products-contracts]] from the complete 119-line product guide.
- Concept audit: updated [[metronome-products-and-rate-cards]], [[metronome-billable-metrics]], and [[metronome-customers-and-contracts]] first with product types, price ownership, metric cardinality, effective-dated edits, and narrow contract boundaries.
- Sol review retained immutable product type, replacement/archive handling, retroactive editing, tag roles, dimensional and presentation group keys, the near-one-thousand-value latency caution, and undocumented recalculation and invoice-state effects.
- Campaign 06: the strong-tier Sol candidate passed fixed-schema validation on attempt 1 before serial full-raw Sol review.
- Coverage after finalization: 35 source summaries ingested and 190 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-06/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-06/attempts/create-products-contracts/attempt-1/receipt.json).

## 2026-07-30 — Canonical ingest: Send Usage Events

- Ingested: [[source-metronome-guides-implement-metronome-core-concepts-send-usage-events]] from the complete 118-line implementation guide.
- Concept audit: updated [[metronome-event-ingestion]], [[metronome-api-idempotency]], [[metronome-billable-metrics]], and [[metronome-customers-and-contracts]] first with property representation, status-specific retry, heartbeat, SQL-aggregation, event-change, and asynchronous customer boundaries.
- Sol review retained the required producer fields, RFC 3339 and future-time rule, reliable-queue/DLQ sequence, 20% resilience-test recommendation, deterministic heartbeat example, and all undocumented endpoint and duplicate-response semantics.
- Campaign 06: the standard-tier Terra candidate passed fixed-schema validation on attempt 1 before serial full-raw Sol review.
- Coverage after finalization: 34 source summaries ingested and 191 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-06/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-06/attempts/send-usage-events/attempt-1/receipt.json).

## 2026-07-30 — Canonical ingest: API Quickstart

- Ingested: [[source-metronome-api-reference-api-quickstart]] from the complete 148-line onboarding guide.
- Concept audit: updated [[metronome-security-principles]] first with the secure-copy and environment-variable evidence while preserving the undocumented customer-token lifecycle boundary.
- Sol review retained four exact SDK installation/configuration routes, empty-list connectivity behavior, the API-key versus bearer-token terminology boundary, and the absence of SDK version, numeric-limit, and general error semantics.
- Link reconciliation added reciprocal references from the authentication and SDK walkthrough sources.
- Campaign 06: the standard-tier Terra candidate passed fixed-schema validation on attempt 1 before serial full-raw Sol review.
- Coverage after finalization: 33 source summaries ingested and 192 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-06/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-06/attempts/api-quickstart/attempt-1/receipt.json).

## 2026-07-30 — Canonical ingest: Use Postman with Metronome

- Ingested: [[source-metronome-api-reference-postman]] from the complete 79-line setup guide.
- Concept audit: no new concept or concept update was warranted for this thin developer-tool guide.
- Sol review retained the live OpenAPI import URL, Tags organization, collection-scoped bearer-token variable, illustrative customer exchange, and undocumented OpenAPI version and token-lifecycle boundaries; it removed an unnecessary operational recommendation from the candidate.
- Campaign 06: the standard-tier Terra candidate passed fixed-schema validation on attempt 1 before serial full-raw Sol review.
- Coverage after finalization: 32 source summaries ingested and 193 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-06/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-06/attempts/postman/attempt-1/receipt.json).

## 2026-07-30 — Canonical ingest: API Reference Introduction

- Ingested: [[source-metronome-api-reference-introduction]] from the complete 71-line API directory page.
- Concept audit: no concept edit or new concept was warranted because the page only routes existing platform domains and adds no new implementation behavior.
- Sol review retained the named API-wide capabilities, four SDK repositories, ten endpoint domains, and the boundary that the page contains no endpoint schemas, limits, authentication rules, or lifecycle semantics.
- Campaign 06: the standard-tier Terra candidate passed fixed-schema validation on attempt 1 before serial full-raw Sol review.
- Coverage after finalization: 31 source summaries ingested and 194 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-06/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-06/attempts/api-introduction/attempt-1/receipt.json).

## 2026-07-30 — Metronome Campaign 05 query-quality audit

- Method: an independent Sol reviewer asked one core, one boundary, and one trap question per Campaign 05 source, answered from the source alone, and checked the answer against each complete raw page; Sol then independently adjudicated every finding.
- Initial result: 10 pass, 4 partial, and 1 fail across 15 tests.
- Bounded repairs: documented Alerts-only uniqueness-key release, streaming-aggregation availability surfaces, Create a Customer bearer authentication and HTTP `200`, commit invoice suppression, the required multiplier on every tiered-override tier, and the missing usage-based-billing concept backlink/update.
- Final result: 15 pass, 0 partial, and 0 fail; all 41 audited wikilinks resolve, provider counts remain 225 raw / 30 ingested / 195 pending, and no scheduler, schema, or validator change was introduced.
- Scale decision: retain the current three-worker ceiling and serial strong-model review for the next campaign; do not relax review because the long nested OpenAPI page produced the only material omission.
- Evidence: [Campaign 05 quality audit](../tracking/ingest/metronome/metronome-campaign-05/quality-audit.md).

## 2026-07-30 — Metronome Campaign 05 completed

- Result: all five jobs were approved on attempt 1; no worker result failed deterministic validation, no retry was needed, and no job was rejected.
- Routing: two standard jobs used native GPT-5.6 Terra and three strong jobs used native GPT-5.6 Sol; at most three native workers ran concurrently while Sol performed serial full-raw review.
- Preflight evaluation: canonical URL, exact top-level-key, and quote-field failures fell from five in Campaign 04 to zero in Campaign 05 across 1,790 raw lines, including one 1,133-line endpoint.
- Content-review boundary: Sol still added material concept, contradiction, request/response, selector, lifecycle, and unknown-semantics coverage, so deterministic compliance does not replace full review.
- Output: five source summaries, one new platform concept, grounded updates to existing concepts and company state, and reciprocal source links.
- Coverage after campaign: 30 source summaries ingested and 195 documentation pages pending.
- Evidence: [campaign selection and result](../tracking/ingest/metronome/metronome-campaign-05/selection-review.md), [campaign monitor](../tracking/ingest/metronome/metronome-campaign-05/monitor.md), and [event journal](../tracking/ingest/metronome/metronome-campaign-05/events.jsonl).

## 2026-07-30 — Canonical ingest: Amend a Contract API

- Ingested: [[source-metronome-api-reference-contracts-amend-a-contract]] from the complete 1,133-line legacy API reference.
- Concept audit: updated [[metronome-customers-and-contracts]], [[metronome-credits-and-commits]], and [[metronome-products-and-rate-cards]] before canonical source creation; no endpoint-specific concept or comparison page was warranted.
- Sol review retained the `editContract` migration/removal boundary, inclusive amendment timing, nested schedule and override validation, configuration gates, prose-versus-required-list gaps, credit applicability ambiguity, and undocumented mutation, invoice, atomicity, and response-ID semantics.
- Cross-source review linked the API-wide idempotency guarantee while preserving the absence of defined cached-error behavior for a partially applied multi-object amendment.
- Link reconciliation added reciprocal references from create-contract, edit-history, targeted commit-edit, and idempotency sources.
- Campaign 05: the 1,133-line strong-tier Sol candidate passed the new canonical-URL, fixed-key, and quote-field preflight plus deterministic validation on attempt 1 before serial full-raw Sol review.
- Coverage after finalization: 30 source summaries ingested and 195 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-05/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-05/attempts/amend-a-contract/attempt-1/receipt.json).

## 2026-07-30 — Canonical ingest: Create a Customer API

- Ingested: [[source-metronome-api-reference-customers-create-a-customer]] from the complete 393-line API reference.
- Concept audit: updated [[metronome-customers-and-contracts]], [[metronome-event-ingestion]], and [[metronome-integrations]] before canonical source creation; no endpoint-specific concept or comparison page was warranted.
- Sol review retained the required name and truncation behavior, 2,000 alias limit and deprecation, provider/delivery/tax/revenue boundaries, optional request-body ambiguity, and `customer_id` versus `data.id` response mismatch.
- Link reconciliation added reciprocal references from the idempotency, create-contract, and Stripe-integration sources.
- Campaign 05: the strong-tier Sol candidate passed the new canonical-URL, fixed-key, and quote-field preflight plus deterministic validation on attempt 1 before serial full-raw Sol review.
- Coverage after finalization: 29 source summaries ingested and 196 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-05/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-05/attempts/create-a-customer/attempt-1/receipt.json).

## 2026-07-30 — Canonical ingest: create billable metrics

- Ingested: [[source-metronome-guides-implement-metronome-core-concepts-create-billable-metrics]] from the complete 130-line guide.
- Concept audit: updated [[metronome-billable-metrics]], [[metronome-event-ingestion]], and [[metronome-products-and-rate-cards]] before canonical source creation; no new concept or comparison page was warranted.
- Sol review retained all four streaming aggregations, SQL distinct-count guidance, compound group-key and filter prerequisites, the near-one-thousand-value latency caution, the ingest/search test, and missing reflow guarantees.
- Contradiction review reconciled the event-design guide's categorical non-retroactivity wording with this guide's representative-assisted reflow exception and added reciprocal source links.
- Campaign 05: the strong-tier Sol candidate passed the new canonical-URL, fixed-key, and quote-field preflight plus deterministic validation on attempt 1 before serial full-raw Sol review.
- Coverage after finalization: 28 source summaries ingested and 197 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-05/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-05/attempts/create-billable-metrics/attempt-1/receipt.json).

## 2026-07-30 — Canonical ingest: API idempotency

- Ingested: [[source-metronome-api-reference-idempotency]] from the complete 86-line API convention page.
- Concept audit: created [[metronome-api-idempotency]] and updated [[metronome-event-ingestion]] and [[metronome-customers-and-contracts]] before canonical source creation; no comparison page was warranted.
- Sol review retained the four mechanism scopes, ingest-alias move-before-reuse rule, 34-day event and at-least-24-hour request-cache windows, HTTP 409 conflicts, cached HTTP 500 behavior, and the cross-page retry-guidance tension.
- Link reconciliation added reciprocal references from the status-code, ingest-events, and create-contract sources.
- Campaign 05: the standard-tier Terra candidate passed the new canonical-URL, fixed-key, and quote-field preflight plus deterministic validation on attempt 1 before serial full-raw Sol review.
- Coverage after finalization: 27 source summaries ingested and 198 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-05/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-05/attempts/idempotency/attempt-1/receipt.json).

## 2026-07-30 — Canonical ingest: API status codes

- Ingested: [[source-metronome-api-reference-status-codes]] from the complete 48-line API convention page.
- Concept audit: no existing concept needed material changes and no standalone concept or comparison page was warranted for this thin API-wide convention.
- Sol review retained the `4XX` JSON `message` envelope, `409` idempotency warning, `429` client-versus-customer rate-limit scope, `5XX` partial-creation warning, and the undocumented numeric-limit, reset-header, and backoff boundaries.
- Campaign 05: the standard-tier Terra candidate passed the new canonical-URL, fixed-key, and quote-field preflight plus deterministic validation on attempt 1 before serial full-raw Sol review.
- Coverage after finalization: 26 source summaries ingested and 199 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-05/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-05/attempts/status-codes/attempt-1/receipt.json).

## 2026-07-29 — Metronome Campaign 04 completed

- Result: all five jobs were approved; 5 failed attempts were retained, retried within the three-attempt limit, and no job was rejected.
- Routing: two standard jobs used native GPT-5.6 Terra and three strong jobs used native GPT-5.6 Sol; Sol performed serial full-raw review and canonical promotion for every job.
- Deterministic gates rejected three `.md` fetch URLs used as canonical URLs, one malformed fixed-schema result, and one result with missing quote locations before review.
- Output: five source summaries plus grounded company, concept, reciprocal-source-link, index, and log updates.
- Coverage after campaign: 25 source summaries ingested and 200 documentation pages pending.
- Evaluation: content-complexity routing remained useful, but fixed-schema compliance was not model-tier-specific; keep the existing validator and exact preflight assertions without adding a classifier.
- Evidence: [campaign selection and result](../tracking/ingest/metronome/metronome-campaign-04/selection-review.md), [campaign monitor](../tracking/ingest/metronome/metronome-campaign-04/monitor.md), and [event journal](../tracking/ingest/metronome/metronome-campaign-04/events.jsonl).

## 2026-07-29 — Canonical ingest: scheduled billing-provider changes

- Ingested: [[source-metronome-guides-customers-billing-manage-customers-schedule-billing-provider-change]] from the complete 137-line guide.
- Concept audit: updated [[metronome-customers-and-contracts]], [[metronome-invoicing]], [[metronome-integrations]], and [[metronome-credits-and-commits]] before canonical source creation; no new concept or comparison page was warranted.
- Sol review preserved the service-period start-versus-end timing conflict, the `issued~at` label, invalid JSON in both request examples, external-provider readiness gaps, and the exactly-once finalized-invoice boundary.
- Link reconciliation added reciprocal references from the Stripe invoice integration, prepaid-threshold guide, and contract edit-history source.
- Campaign 04: attempt 1 failed fixed-schema validation, attempt 2 failed quote-location validation, and attempt 3 passed deterministic validation before serial Sol review.
- Coverage after finalization: 25 source summaries ingested and 200 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-04/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-04/attempts/schedule-billing-provider-change/attempt-3/receipt.json).

## 2026-07-29 — Canonical ingest: Ingest Events API

- Ingested: [[source-metronome-api-reference-usage-ingest-events]] from the complete 293-line API reference.
- Concept audit: updated [[metronome-event-ingestion]] and [[metronome-billable-metrics]] before canonical source creation; no new concept or comparison page was warranted.
- Sol review retained the one-to-100-event schema, four required fields, 128-character transaction ID limit, 34-day backdate and deduplication window, and the missing response, partial-batch, retry, duplicate, future-time, and cutoff semantics.
- Throughput boundary: the endpoint's 100,000-events-per-second support statement remains distinct from the high-volume guide's 110,000 infrastructure-capacity and 5,000 default-account-limit figures.
- Campaign 04: attempt 1 was rejected because the candidate used the `.md` fetch URL as canonical; attempt 2 corrected the canonical URL and passed deterministic validation before serial Sol review.
- Coverage after finalization: 24 source summaries ingested and 201 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-04/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-04/attempts/ingest-events/attempt-2/receipt.json).

## 2026-07-29 — Canonical ingest: API pagination

- Ingested: [[source-metronome-api-reference-pagination]] from the complete 61-line API guide.
- Concept audit: no existing concept needed material changes and no standalone concept or comparison page was warranted for this thin API-wide convention.
- Sol review retained the `limit` and `next_page` traversal contract, the recommended 1/50 values and 100 cap, and the undocumented ordering, cursor-lifetime, retry, and endpoint-variation boundaries.
- Campaign 04: attempt 1 was rejected because the candidate used the `.md` fetch URL as canonical; attempt 2 corrected the canonical URL and passed deterministic validation before serial Sol review.
- Coverage after finalization: 23 source summaries ingested and 202 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-04/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-04/attempts/pagination/attempt-2/receipt.json).

## 2026-07-29 — Canonical ingest: API authentication

- Ingested: [[source-metronome-api-reference-authentication]] from the complete 112-line API guide.
- Concept audit: updated [[metronome-security-principles]] before canonical source creation; no new concept or comparison page was warranted.
- Sol review preserved the distinction between customer bearer tokens with an undocumented expiry and the separate 12-hour engineer credential lifecycle.
- Campaign 04: attempt 1 was rejected because the candidate used the `.md` fetch URL as canonical; attempt 2 corrected the canonical URL and passed deterministic validation before serial Sol review.
- Coverage after finalization: 22 source summaries ingested and 203 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-04/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-04/attempts/authentication/attempt-2/receipt.json).

## 2026-07-29 — Canonical ingest: prepaid balance thresholds

- Ingested: [[source-metronome-guides-customers-billing-optimize-customer-experience-prepaid-balance-thresholds]] from the complete 269-line guide.
- Concept audit: updated [[metronome-credits-and-commits]], [[metronome-customers-and-contracts]], [[metronome-invoicing]], [[metronome-products-and-rate-cards]], [[metronome-webhooks]], and [[metronome-integrations]] before canonical source creation; no new concept or comparison page was warranted.
- Sol review preserved the source's threshold equality, minimum-field naming, and discount-fraction ambiguities, plus its undocumented concurrency and duplicate-recharge behavior.
- Campaign 04: the strong-tier candidate passed deterministic validation on attempt 1 and then underwent a complete serial Sol reread and promotion review.
- Coverage after finalization: 21 source summaries ingested and 204 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-04/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-04/attempts/prepaid-balance-thresholds/attempt-1/receipt.json).

## 2026-07-29 — Metronome Campaign 03 completed

- Result: five of five jobs were approved on attempt 1; no job failed, retried, or was rejected.
- Routing: two standard jobs used native GPT-5.6 Terra and three strong jobs used native GPT-5.6 Sol; Sol performed serial full-raw review and canonical promotion for every job.
- Output: five source summaries and grounded updates to existing company and concept pages; no duplicate concept or comparison page was created.
- Quality: preserved the prepaid-guide contradictions, edit-API unknowns, Stripe Tax mapping ambiguity, and explicit missing-information boundaries.
- Coverage after campaign: 20 source summaries ingested and 205 documentation pages pending.
- Evaluation boundary: routing worked for this sample, but full Sol rereads mean the pilot does not establish lower reviewer-token volume.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-03/monitor.md), [selection and result summary](../tracking/ingest/metronome/metronome-campaign-03/selection-review.md), and [event journal](../tracking/ingest/metronome/metronome-campaign-03/events.jsonl).

## 2026-07-29 — Canonical ingest: Stripe Tax integration

- Ingested: [[source-metronome-integrations-tax-integrations-stripe-tax]] from the complete 184-line guide.
- Concept audit: updated [[stripe-tax]], [[metronome-invoicing]], [[metronome-integrations]], [[metronome-products-and-rate-cards]], and [[metronome-credits-and-commits]]; no duplicate tax concept or comparison page was warranted.
- Sol review retained the Metronome/Stripe responsibility boundary, address and tax-code prerequisites, many-to-one product mapping, finalization timing, threshold override, and the `Product` versus `ContractProduct` and all-tax-provider scope cautions.
- Campaign 03 routing: the strong-tier Sol worker candidate passed deterministic validation and serial full-raw Sol coordinator review on attempt 1.
- Coverage after finalization: 20 source summaries ingested and 205 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-03/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-03/attempts/stripe-tax/attempt-1/receipt.json).

## 2026-07-29 — Canonical ingest: Edit a Commit API

- Ingested: [[source-metronome-api-reference-credits-and-commits-edit-a-commit]] from the complete 457-line API reference.
- Concept audit: updated [[metronome-credits-and-commits]], [[metronome-customers-and-contracts]], [[metronome-invoicing]], and [[metronome-products-and-rate-cards]]; no endpoint-specific concept or comparison page was warranted.
- Sol review retained schedule add/update/remove requirements, finalized and voided invoice restrictions, selector exclusivity, hierarchy variants, and the undocumented response-ID, `product_id`, proration, error, and null/omission boundaries.
- Campaign 03 routing: the strong-tier Sol worker candidate passed deterministic validation and serial full-raw Sol coordinator review on attempt 1.
- Coverage after finalization: 19 source summaries ingested and 206 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-03/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-03/attempts/edit-a-commit/attempt-1/receipt.json).

## 2026-07-29 — Canonical ingest: credits and commits guide

- Ingested: [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-create-a-pre-paid-commit]] from the complete 459-line guide.
- Concept audit: updated [[metronome-credits-and-commits]], [[metronome-customers-and-contracts]], [[metronome-products-and-rate-cards]], [[metronome-invoicing]], and [[metronome-usage-based-billing]]; no duplicate concept or comparison page was warranted.
- Sol review preserved contradictions in the guide's prepaid amount, recurring-example JSON, signup/upgrade dates, and `rollover_fraction` representation, with a reciprocal warning on the create-contract API source.
- Campaign 03 routing: the strong-tier Sol worker candidate passed deterministic validation and serial full-raw Sol coordinator review on attempt 1.
- Coverage after finalization: 18 source summaries ingested and 207 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-03/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-03/attempts/create-pre-paid-commit/attempt-1/receipt.json).

## 2026-07-29 — Canonical ingest: dashboard first-invoice quickstart

- Ingested: [[source-metronome-guides-get-started-metronome-dashboard-quickstart]] from the complete 248-line dashboard guide.
- Concept audit: updated the existing event-ingestion, billable-metric, product/rate-card, customer/contract, invoicing, and webhook concepts; no dashboard-only concept or comparison page was warranted.
- Sol review retained the 2,000-property limit, immutable metric settings, group-key dependencies, Sandbox-only test-event rules, 34-day timestamp window, and invoice/provider boundary.
- Campaign 03 routing: the standard-tier Terra candidate passed deterministic validation and serial full-raw Sol review on attempt 1.
- Coverage after finalization: 17 source summaries ingested and 208 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-03/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-03/attempts/metronome-dashboard-quickstart/attempt-1/receipt.json).

## 2026-07-29 — Canonical ingest: data export overview

- Ingested: [[source-metronome-guides-reporting-insights-data-export-overview]] from the complete 134-line guide.
- Concept audit: updated [[metronome-reporting-and-analytics]] with destination scope, delivery cadence, freshness, and append-only object-storage semantics; no duplicate concept or comparison page was warranted.
- Sol review confirmed the one-destination boundary, table-specific timing, at-least-once deduplication responsibility, and the absence of a stated retention period.
- Campaign 03 routing: the standard-tier Terra candidate passed deterministic validation and serial full-raw Sol review on attempt 1.
- Coverage after finalization: 16 source summaries ingested and 209 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-03/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-03/attempts/data-export-overview/attempt-1/receipt.json).

## 2026-07-29 — Campaign 02 query-quality audit

- Scope: an independent reviewer checked all five source pages against all 1,442 raw lines using 15 core, boundary, and trap questions.
- Initial result: 13 pass, 1 partial, and 1 fail. The hard failure omitted the contract-level multi-account `billing_provider_configuration_id` and lookup route; the soft partial omitted the equivalent 6.6-million-events-per-minute throughput figure.
- Resolution: Sol repaired the source and related concepts. Final result: 15 pass, 0 partial, and 0 fail.
- Architecture boundary: no new coordinator machinery, schema, retry behavior, or parallel-ingest abstraction was added.
- Evidence: [Campaign 02 quality audit](../tracking/ingest/metronome/metronome-campaign-02/quality-audit.md).

## 2026-07-28 — Metronome Campaign 02 completed

- Result: five of five jobs were approved on attempt 1; no job failed, retried, or was rejected.
- Execution: three native GPT-5.6 Terra workers produced bounded candidates and suggestions, while Sol performed serial full-raw review, concept audit, canonical promotion, shared-file reconciliation, and final approval.
- Output: five source summaries, two new concepts, and grounded updates to four existing concepts.
- Coverage after campaign: 15 source summaries ingested and 210 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-02/monitor.md), [selection and result summary](../tracking/ingest/metronome/metronome-campaign-02/selection-review.md), and [event journal](../tracking/ingest/metronome/metronome-campaign-02/events.jsonl).

## 2026-07-28 — Canonical ingest: Create a commit API

- Ingested: [[source-metronome-api-reference-credits-and-commits-create-a-commit]] from the complete 605-line API reference.
- Concept audit: updated [[metronome-credits-and-commits]]; no endpoint-specific concept or comparison page was warranted.
- Sol review retained conditional prepaid/postpaid invoice rules, cross-contract scope, targeting semantics, priority ties, gated fields, and the generic recurring-schedule versus postpaid single-item ambiguity.
- Terra/Sol campaign: attempt 1 passed deterministic candidate validation and serial Sol review after bounded canonical repair.
- Coverage after finalization: 15 source summaries ingested and 210 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-02/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-02/attempts/create-commit/attempt-1/receipt.json).

## 2026-07-28 — Canonical ingest: Stripe invoice integration

- Ingested: [[source-metronome-integrations-invoice-integrations-stripe]] from the complete 331-line guide.
- Concept audit: updated [[metronome-invoicing]] and [[metronome-integrations]]; no new concept or cross-provider comparison page was warranted.
- Sol review restored multi-account routing, non-retroactive activation, payment-gated product mapping, account-level setting boundaries, Stripe-side payment timing, and representation limits omitted by the worker draft.
- Terra/Sol campaign: attempt 1 passed deterministic candidate validation and serial Sol review after canonical repair.
- Coverage after finalization: 14 source summaries ingested and 211 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-02/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-02/attempts/stripe-invoice-integration/attempt-1/receipt.json).

## 2026-07-28 — Canonical ingest: enterprise commitment model

- Ingested: [[source-metronome-guides-pricing-packaging-billing-model-guides-enterprise-commit]] from the complete 267-line guide.
- Concept audit: created [[metronome-credits-and-commits]] and updated [[metronome-products-and-rate-cards]] and [[metronome-customers-and-contracts]]; no comparison page was warranted.
- Sol review preserved two source-document inconsistencies: `product` versus the API reference's `product_id`, and an upsell described as a commitment but implemented as a scheduled charge.
- Terra/Sol campaign: attempt 1 passed deterministic candidate validation and serial Sol review after canonical repair.
- Coverage after finalization: 13 source summaries ingested and 212 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-02/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-02/attempts/enterprise-commit/attempt-1/receipt.json).

## 2026-07-28 — Canonical ingest: Metronome Stripe App

- Ingested: [[source-metronome-guides-get-started-stripe-marketplace-app]] from the complete 154-line guide.
- Concept audit: created [[metronome-integrations]] and updated [[metronome-customers-and-contracts]]; no comparison page was warranted.
- Terra/Sol campaign: attempt 1 passed deterministic candidate validation and serial Sol review.
- Coverage after finalization: 12 source summaries ingested and 213 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-02/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-02/attempts/stripe-marketplace-app/attempt-1/receipt.json).

## 2026-07-28 — Canonical ingest: usage events at scale

- Ingested: [[source-metronome-guides-events-high-volume-ingestion]] from the complete 85-line guide.
- Concept audit: updated [[metronome-event-ingestion]] with throughput, batching, observability, and recovery boundaries; no new concept or comparison page was warranted.
- Terra/Sol campaign: attempt 1 passed deterministic candidate validation and serial Sol review.
- Coverage after finalization: 11 source summaries ingested and 214 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-02/monitor.md) and [attempt receipt](../tracking/ingest/metronome/metronome-campaign-02/attempts/high-volume-ingestion/attempt-1/receipt.json).

## 2026-07-28 — Minimum promotion pilot closed

- Result: all five jobs were approved and promoted; no job failed or was rejected.
- Boundary correction: future campaign jobs retain their canonical URL, and the coordinator now rejects candidate pages that omit or change it or use a filename-only raw backlink.
- Scope: this closes `metronome-minimum-pilot-01`; it does not authorize bulk ingest or bypass serial Sol review.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-minimum-pilot-01/monitor.md) and [event journal](../tracking/ingest/metronome/metronome-minimum-pilot-01/events.jsonl).

## 2026-07-28 — Canonical ingest: security principles

- Ingested: [[source-metronome-guides-platform-configuration-security-principles]] from the complete 29-line guide.
- Concept audit: created [[metronome-security-principles]] before canonical source promotion; no comparison page was warranted.
- Terra/Sol dry run: attempt 1 reached `review_approved`; canonical promotion retained the four grounded security claims and added the required canonical URL and path-qualified raw backlink.
- Coverage after finalization: 10 source summaries ingested and 215 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-minimum-pilot-01/monitor.md) and [approved attempt receipt](../tracking/ingest/metronome/metronome-minimum-pilot-01/attempts/security-principles/attempt-1/receipt.json).

## 2026-07-28 — Canonical ingest: setup webhooks

- Ingested: [[source-metronome-guides-platform-configuration-setup-webhooks]] from the complete 870-line guide.
- Concept audit: created [[metronome-webhooks]] before canonical source promotion; no comparison page was warranted.
- Terra/Sol dry run: attempt 1 reached `review_approved`; canonical promotion retained the grounded delivery and verification rules and added the required canonical URL and path-qualified raw backlink.
- Coverage after finalization: 9 source summaries ingested and 216 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-minimum-pilot-01/monitor.md) and [approved attempt receipt](../tracking/ingest/metronome/metronome-minimum-pilot-01/attempts/setup-webhooks/attempt-1/receipt.json).

## 2026-07-28 — Canonical ingest: Get Contract Edit History API

- Ingested: [[source-metronome-api-reference-contracts-get-contract-edit-history]] from the complete 2,672-line API reference.
- Concept audit: updated [[metronome-customers-and-contracts]]; no endpoint-specific concept or comparison page was warranted.
- Terra/Sol dry run: attempt 1 reached `review_approved`; canonical promotion retained the grounded audit scope and added the required canonical URL and path-qualified raw backlink.
- Coverage after finalization: 8 source summaries ingested and 217 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-minimum-pilot-01/monitor.md) and [approved attempt receipt](../tracking/ingest/metronome/metronome-minimum-pilot-01/attempts/get-contract-edit-history/attempt-1/receipt.json).

## 2026-07-28 — Canonical ingest: Preview Events API

- Ingested: [[source-metronome-api-reference-invoices-preview-events]] from the complete 1,020-line API reference.
- Concept audit: updated [[metronome-event-ingestion]], [[metronome-invoicing]], and [[metronome-usage-based-billing]]; no new concept or comparison page was warranted.
- Terra/Sol dry run: attempt 1 reached `review_approved`; canonical promotion retained the grounded API constraints and added the required canonical URL and path-qualified raw backlink.
- Coverage after finalization: 7 source summaries ingested and 218 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-minimum-pilot-01/monitor.md) and [approved attempt receipt](../tracking/ingest/metronome/metronome-minimum-pilot-01/attempts/preview-events/attempt-1/receipt.json).

## 2026-07-28 — Canonical ingest: design usage events

- Ingested: [[source-metronome-guides-events-design-usage-events]] from the complete 88-line guide.
- Concept audit: updated [[metronome-event-ingestion]] and [[metronome-billable-metrics]]; no new concept or comparison page was warranted.
- Terra/Sol dry run: attempt 1 was returned because its log suggestion targeted `wiki/log.md`; attempt 2 corrected the destination to `wiki/metronome-log.md` and passed serial Sol review.
- Coverage after finalization: 6 source summaries ingested and 219 documentation pages pending.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-minimum-pilot-01/monitor.md) and [approved attempt receipt](../tracking/ingest/metronome/metronome-minimum-pilot-01/attempts/design-usage-events/attempt-2/receipt.json).

## 2026-07-14 — Luna/Sol five-page pilot concluded

- Decision: `scale_with_changes`; Luna is approved only as a constrained draft/evidence worker, with Sol remaining mandatory for concepts, contradictions, shared state, promotion, and final approval.
- Results: 5 accepted cases, 7 Luna attempts, 23 recorded Sol repairs, 59 coordinator repair minutes, and 4 production sources added.
- Independent review: agreed with `scale_with_changes`, found retry-regression and evidence/accounting gaps, and identified two additional SDK example inconsistencies now preserved on the canonical source.
- Coverage remains: 5 source summaries ingested and 220 documentation pages pending.
- Report: [Metronome GPT-5.6 Luna five-page pilot](../tracking/ingest/metronome/pilot/luna-sol-five-page-pilot-report.md).

## 2026-07-14 — Luna/Sol pilot: create-contract API

- Ingested: [[source-metronome-api-reference-contracts-create-a-contract]] from the complete 4,561-line endpoint reference.
- Concept audit: updated [[metronome-customers-and-contracts]] before promoting the canonical source; no endpoint-specific concept was created.
- Luna result: passed on attempt 1 with four exact quotes and a correct raw deep-dive link.
- Sol review: added package-mode restrictions, account/feature-gated field boundaries, conditional subscription quantity rules, immutable charge-consolidation behavior, and the `409` versus listed-response caveat.
- Coverage after finalization: 5 source summaries ingested and 220 documentation pages pending.
- Evidence: [worker run](../tracking/ingest/metronome/pilot/runs/pilot-create-contract-luna/) and [final receipt](../tracking/ingest/metronome/pilot/receipts/pilot-create-contract-luna-final.json).

## 2026-07-14 — Luna/Sol pilot: data-export database reference

- Ingested: [[source-metronome-guides-reporting-insights-data-export-database-reference]] from the complete 1,600-line schema reference.
- Concept audit: created [[metronome-reporting-and-analytics]] before promoting the canonical source.
- Luna result: passed on attempt 1 with four exact quotes and a correct raw deep-dive link.
- Sol review: elevated the all-columns-nullable warning, added row-grain and time/version navigation, clarified the commits-table scope, and narrowed the Private Beta wording to the note's actual invoicing statement.
- Coverage after finalization: 4 source summaries ingested and 221 documentation pages pending.
- Evidence: [worker run](../tracking/ingest/metronome/pilot/runs/pilot-database-reference-luna/) and [final receipt](../tracking/ingest/metronome/pilot/receipts/pilot-database-reference-luna-final.json).

## 2026-07-14 — Luna/Sol pilot: developer SDK walkthrough

- Ingested: [[source-metronome-guides-get-started-developer-sdks]] from the complete 944-line guide.
- Concept audit: created [[metronome-event-ingestion]], [[metronome-billable-metrics]], [[metronome-products-and-rate-cards]], and [[metronome-customers-and-contracts]] from the planned taxonomy; no separate SDK concept was warranted.
- Luna result: passed on attempt 1 with five exact quotes and a correct raw deep-dive link.
- Sol review: restored the 34-day event window, the future-event metric boundary, pricing/effective-period rules, and two language-example caveats; no external platform contradiction was found.
- Coverage after finalization: 3 source summaries ingested and 222 documentation pages pending.
- Evidence: [worker run](../tracking/ingest/metronome/pilot/runs/pilot-developer-sdks-luna/) and [final receipt](../tracking/ingest/metronome/pilot/receipts/pilot-developer-sdks-luna-final.json).

## 2026-07-14 — Luna/Sol pilot: invoicing overview

- Ingested: [[source-metronome-guides-invoices-overview]] from the complete 31-line overview.
- Concept: created [[metronome-invoicing]] after the mandatory concept audit.
- Luna result: attempt 1 failed exact-line grounding after using unsupported invoice-state content; attempt 2 passed with five exact quotes.
- Sol review: consolidated four proposed sub-concepts into one planned invoicing concept and tightened the ASC 606 wording; no contradiction was found.
- Coverage after finalization: 2 source summaries ingested and 223 documentation pages pending.
- Evidence: [worker run](../tracking/ingest/metronome/pilot/runs/pilot-invoices-overview-luna/) and [final receipt](../tracking/ingest/metronome/pilot/receipts/pilot-invoices-overview-luna-final.json).

## 2026-07-14 — Strong-model baseline ingest

- Ingested: [[source-metronome-guides-get-started-home]] from the complete 140-line documentation landing page.
- Concept: created [[metronome-usage-based-billing]] after the mandatory concept audit.
- Worker role: `strong_baseline`; worker commit `e9a90d0` touched only its leased source and concept files.
- Coverage after finalization: 1 source summary ingested and 224 documentation pages pending.
- Validation: exact grounding quotes, write ownership, focused wiki validation, capsule reconciliation, and the full test suite passed.
- Receipt: [pilot-home-baseline.json](../tracking/ingest/metronome/pilot/receipts/pilot-home-baseline.json).

## 2026-07-13 — Initial English documentation collection

- Collected corpus: 225 English canonical documentation pages and 2 OpenAPI artifacts.
- Result: 222 new items, 5 unchanged smoke-test items, and 0 failures.
- Discovery reconciliation: 208 pages in both discovery sources and 17 additional English sitemap-only pages.
- Ingest status: not started; all 225 documentation pages remain pending.
- Evidence: [collection status](../tracking/collections/metronome/collection-status.md), [run manifest](../tracking/collections/metronome/runs/2026-07-13T100930-manifest.md), and [detailed JSONL run record](../tracking/collections/metronome/runs/2026-07-13T100930.jsonl).

## Related

- [[metronome-index]]
- [[metronome]]
