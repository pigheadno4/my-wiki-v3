---
title: "Metronome Collection and Ingest Log"
type: log
tags: [metronome, usage-based-billing, operations]
---

Newest entries appear first. Detailed collection evidence remains under `tracking/collections/metronome/`; ingest evidence remains under `tracking/ingest/metronome/`.

## 2026-08-27 — Metronome Campaign 24 larger confirmation promoted

- Result: eight approved source pages from complete raw-page reads across twelve Sol worker attempts and twelve independent full Sol reviews; four pages passed attempt 1 and four passed attempt 2, with no targeted review, failure, or rejection.
- Sources: [[source-metronome-api-reference-contracts-get-the-rate-schedule-for-a-contract]], [[source-metronome-api-reference-credit-grants-list-credit-ledger-entries]], [[source-metronome-api-reference-contracts-update-invoice-issue-date]], [[source-metronome-api-reference-security-get-audit-logs]], [[source-metronome-integrations-marketplace-integrations-gcp]], [[source-metronome-guides-get-started-api-quickstart]], [[source-metronome-guides-customers-billing-set-up-notifications-system-notifications]], and [[source-metronome-guides-pricing-packaging-subscription-manage-seats]].
- Minimum Sufficient Source result: all eight sources retain query-critical facts, material contradictions and unknowns, primary concept routes, coverage maps, and exact immutable raw links without reproducing complete schemas or walkthroughs.
- Retry findings: the credit ledger required explicit entry-versus-ledger ordering and a positive-deduction amount contradiction; audit logs required the narrative-versus-OpenAPI `next_page` placement conflict; API Quickstart required replacement of stale worked timestamps; Manage Seats required API-wide POST idempotency and corrected nested requiredness.
- Concepts: updated subscriptions, credits and commits, alerts and notifications, API idempotency, customers and contracts, invoicing, reporting and analytics, security, integrations, event ingestion, currencies, usage billing, billable metrics, products and rate cards, packages and aliases, and webhooks; no new concept page was required.
- Coverage after promotion: 225 collected documentation pages, 145 source summaries, and 86 raw pages without source summaries.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-24/monitor.md), [quality audit](../tracking/ingest/metronome/metronome-campaign-24/quality-audit.md), and [retrospective](../tracking/ingest/metronome/metronome-campaign-24/retrospective.md).

## 2026-08-26 — Metronome Campaign 23 Minimum Sufficient Source pilot promoted

- Result: five approved source pages from complete raw-page reads, each accepted on attempt 1 after an independent complete-source Sol review; no worker retry, targeted review, failure, or rejection was required.
- Sources: [[source-metronome-api-reference-contracts-get-a-contract-v2]], [[source-metronome-api-reference-invoices-list-invoices]], [[source-metronome-api-reference-credit-grants-void-a-credit-grant]], [[source-metronome-guides-implement-metronome-core-concepts-packages-overview]], and [[source-metronome-integrations-marketplace-integrations-azure]].
- Minimum Sufficient Source finding: concise query routers retained material decisions, contradictions, authority boundaries, primary concept routes, raw coverage maps, and exact raw deep-dive links without copying complete schemas or setup procedures.
- Concepts: updated customers and contracts, credits and commits, API idempotency, invoicing, reporting and analytics, packages and aliases, products and rate cards, custom fields, integrations, event ingestion, and currencies and custom pricing units; no new concept page was required.
- Boundaries retained: contract balance history remains ambiguous; invoice default ordering conflicts across the page; the legacy grant void does not establish downstream or atomic effects; package aliases do not imply existing-contract rewrites; Azure setup and metering do not prove acceptance, payment, settlement, tax, refund, or reconciliation, and its provider-change wording conflicts with the dedicated transition authority.
- Coverage after promotion: 225 collected documentation pages, 137 source summaries, and 94 raw pages without source summaries.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-23/monitor.md), [quality audit](../tracking/ingest/metronome/metronome-campaign-23/quality-audit.md), and [retrospective](../tracking/ingest/metronome/metronome-campaign-23/retrospective.md).

## 2026-08-25 — Metronome Campaign 22 archetype v2 pilot promoted

- Result: five approved source pages from complete raw-page reads across eleven worker attempts and eleven independent reviews; final attempts were 2, 3, 2, 2, and 2, with no coordinator content repair.
- Sources: [[source-metronome-api-reference-products-get-a-product]], [[source-metronome-api-reference-products-list-products]], [[source-metronome-api-reference-customers-archive-a-customer]], [[source-metronome-guides-implement-metronome-core-concepts-non-monotonically-increasing-metrics]], and [[source-metronome-integrations-platform-integrations-sfdc-integration]].
- Archetype v2 checks: claim-to-evidence closure, authority separation, and concept-impact sweep made reviewer defect attribution explicit, but no page passed attempt 1 and `list-products` required a third attempt.
- Concepts: updated products and rate cards, billable metrics, custom fields, integrations, API idempotency, customers and contracts, invoicing, alerts and notifications, usage-based billing, credits and commits, reporting and analytics, event ingestion, and currencies and custom pricing units; no new concept page was required.
- Boundaries retained: `PRO_SERVICE` conflicts with the four-type guide; product state and update identifier formats differ; customer archival does not define downstream invoice or notification completion; the non-monotonic worked example conflicts with its full-period recommendation; Salesforce synchronization does not prove completeness, financial reconciliation, or downstream outcomes.
- Campaign outcome: final content quality reached reviewer approval, but the pilot failed its throughput gate before promotion: zero of five attempt-1 approvals, five full semantic retry cycles, one targeted retry, and one page reaching attempt 3. Archetype v2 should remain campaign-local evidence rather than a production speed rule.
- Coverage after promotion: 225 collected documentation pages, 132 source summaries, and 99 raw pages without source summaries.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-22/monitor.md); quality audit and retrospective are recorded in the same campaign folder after closure.

## 2026-08-24 — Metronome Campaign 21 archetype pilot promoted

- Result: five approved source pages from complete raw-page reads across thirteen worker attempts and thirteen independent reviews; final attempts were 3, 2, 2, 3, and 3, with no coordinator content repair.
- Sources: [[source-metronome-api-reference-invoices-get-an-invoice]], [[source-metronome-api-reference-customers-list-customers]], [[source-metronome-api-reference-customers-update-a-customer-name]], [[source-metronome-guides-implement-metronome-core-concepts-how-invoicing-works]], and [[source-metronome-integrations-marketplace-integrations-aws]].
- Archetypes: API Read, API List / Schema, API Mutation, Concept / Guide, and Integration Guide. The playbook made reviewer attention and defect attribution more consistent, but zero of five pages passed attempt 1, so it did not meet the throughput gate.
- Concepts: updated customers and contracts, event ingestion, custom fields, invoicing, API idempotency, credits and commits, currencies, integrations, products and rate cards, usage-based billing, billable metrics, and security; no new concept page was required.
- Boundaries retained: invoice response examples do not settle cross-source status terminology; customer listing does not prove cursor consistency or alias lifecycle; immediate name propagation leaves finalized and downstream artifacts undefined; native invoice examples conflict with some documented fields; AWS Marketplace setup does not prove provider acceptance, payment, settlement, tax, or reconciliation.
- Independent query audit: the fixed three-page sample passed 9/9 factual, boundary or contradiction, and exact raw deep-dive queries. All five hashes, approved-candidate equality, backlinks, catalog entries, and reciprocal concept links passed, so no expansion was required.
- Campaign outcome: final content quality passed, but zero of five pages passed attempt 1, four full semantic retry cycles were required, and time to final reviewer approval was about 44 minutes. The archetype playbook improved review focus and defect attribution but failed its throughput gate.
- Coverage after promotion: 225 collected documentation pages, 127 source summaries, and 104 raw pages without source summaries.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-21/monitor.md), [quality audit](../tracking/ingest/metronome/metronome-campaign-21/quality-audit.md), and [retrospective](../tracking/ingest/metronome/metronome-campaign-21/retrospective.md).

## 2026-08-23 — Metronome Campaign 20 completed

- Result: five approved API-reference source pages from complete raw-page reads across twelve worker attempts and twelve independent reviews; final attempts were 2, 2, 3, 3, and 2, with no coordinator content repair.
- Sources: [[source-metronome-api-reference-customers-get-a-customer]], [[source-metronome-api-reference-billable-metrics-list-all-billable-metrics]], [[source-metronome-api-reference-credits-and-commits-list-balances]], [[source-metronome-api-reference-credits-and-commits-create-a-credit]], and [[source-metronome-api-reference-settings-set-up-account-level-billing-provider]].
- Concepts: updated billable metrics, custom fields, customers and contracts, event ingestion, integrations, invoicing, API idempotency, security, credits and commits, products and rate cards, and currencies and custom pricing units; no new concept page was required.
- Boundaries retained: customer detail is separate from billing configuration; metric examples conflict with their aggregation-key rule; detailed balances differ from global pagination and ledger conventions; credit selector and exclusion semantics remain source-bounded; account-level provider setup does not prove customer attachment, downstream readiness, invoice delivery, payment, or reconciliation.
- Independent query audit: the fixed three-page sample passed 9/9 factual, boundary or contradiction, and exact raw deep-dive queries. All five hashes, canonical candidate equality, backlinks, company/index entries, and reviewer-approved concept blocks passed, so no expansion was required.
- Campaign outcome: content quality passed, but zero of five pages passed on attempt 1 and elapsed time was 3,464 seconds. The Campaign 19 preflight reminders did not meet the throughput gate, so an 8–10 page expansion is not approved.
- Coverage after promotion: 225 collected documentation pages, 122 source summaries, and 109 raw pages without source summaries.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-20/monitor.md), [quality audit](../tracking/ingest/metronome/metronome-campaign-20/quality-audit.md), and [retrospective](../tracking/ingest/metronome/metronome-campaign-20/retrospective.md).

## 2026-08-21 — Metronome Campaign 19 completed

- Result: five approved API-reference source pages from complete raw-page reads. Four pages needed one retry; three corrections used unchanged-hash targeted review, while `disable-trueup-for-commit` and `search-events` received full semantic rereviews.
- Sources: [[source-metronome-api-reference-settings-list-account-level-billing-providers]], [[source-metronome-api-reference-credits-and-commits-disable-trueup-for-commit]], [[source-metronome-api-reference-contracts-get-subscription-quantity-history]], [[source-metronome-api-reference-contracts-archive-a-contract]], and [[source-metronome-api-reference-usage-search-events]].
- Concepts: updated integrations, credits and commits, invoicing, subscriptions, customers and contracts, event ingestion, and billable metrics; no new concept page was required.
- Boundaries retained: account delivery-method IDs are not proven interchangeable with customer or contract selectors; true-up suppression does not prove balance, obligation, or downstream effects; quantity history excludes future scheduled changes; archive request-wrapper requiredness and downstream atomicity remain undefined; keyed search replay is not evidence of later ingest or matching state.
- Campaign outcome: all five pages passed final independent review, but none passed on attempt 1, so this representative-complexity campaign did not meet the planned first-pass efficiency gate.
- Coverage after promotion: 225 collected documentation pages, 117 source summaries, and 114 raw pages without source summaries.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-19/monitor.md), [quality audit](../tracking/ingest/metronome/metronome-campaign-19/quality-audit.md), and [retrospective](../tracking/ingest/metronome/metronome-campaign-19/retrospective.md).

## 2026-08-21 — Metronome Campaign 18 completed

- Result: five approved API-reference source pages from complete raw-page reads and five independent Sol reviews; all passed on attempt 1 with no retry or coordinator content repair.
- Sources: [[source-metronome-api-reference-settings-list-pricing-units]], [[source-metronome-api-reference-rate-cards-archive-a-rate-card]], [[source-metronome-api-reference-plans-list-plans]], [[source-metronome-api-reference-credits-and-commits-release-external-payment-gate-threshold-commit]], and [[source-metronome-api-reference-invoices-get-an-invoice-pdf]].
- Concepts: updated currencies and custom pricing units, products and rate cards, customers and contracts, spend-threshold billing, credits and commits, webhooks, and invoicing; no new concept page was required.
- Boundaries retained: pricing-unit fields and non-USD denomination remain incomplete; rate-card restoration and existing-contract preservation mechanics are unspecified; Plans-to-Contracts migration lacks a field or identity mapping; external payment-gate retry, ordering, and propagation are undefined; PDF media metadata does not prove legal officiality, compliance, retention, or rendering stability.
- Independent query audit: the immutable three-page sample passed 9/9 queries; all five raw hashes, canonical candidate equality, backlinks, company/index entries, and 7/7 fact-bearing reciprocal concept targets passed, so no expansion was required.
- Coverage after promotion: 225 collected documentation pages, 112 source summaries, and 119 raw pages without source summaries.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-18/monitor.md) and [quality audit](../tracking/ingest/metronome/metronome-campaign-18/quality-audit.md).

## 2026-08-20 — Metronome Campaign 17 completed

- Result: five approved source pages from complete raw-page reads. Pricing-change evidence used one unchanged-hash targeted review; data-export cookbook, edit-contract, and revenue-recognition corrections received full independent rereviews.
- Sources: [[source-metronome-guides-pricing-packaging-make-pricing-changes-make-a-pricing-change]], [[source-metronome-guides-pricing-packaging-make-pricing-changes-edit-or-override-a-contract]], [[source-metronome-guides-reporting-insights-data-export-cookbook]], [[source-metronome-guides-pricing-packaging-make-pricing-changes-edit-contract]], and [[source-metronome-guides-reporting-insights-financial-reporting-revenue-recognition-examples]].
- Concepts: created [[metronome-packages-and-aliases]] and updated products and rate cards, customers and contracts, credits and commits, invoicing, and reporting and analytics.
- Boundaries retained: package examples do not prove future-rate scheduling; override examples do not document an existing-contract edit route; cookbook SQL requires environment, grain, deduplication, effective-time, and currency care; edit endpoint and timestamp terminology conflicts across guides; revenue examples contain amount, identifier, field-name, and classification conflicts and are not accounting policy.
- Independent query audit: the fixed sample found one missing reciprocal link from [[payment-reconciliation-reporting]] to the revenue examples. One bounded coordinator repair added that source-only link; the same auditor verified it and the required expansion passed all five pages and 15/15 queries.
- Coverage after promotion: 225 collected documentation pages, 107 source summaries, and 124 raw pages without source summaries.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-17/monitor.md) and [quality audit](../tracking/ingest/metronome/metronome-campaign-17/quality-audit.md).

## 2026-08-19 — Metronome Campaign 16 completed

- Result: five approved source pages from complete raw-page reads across nine worker attempts and nine independent reviews; one correction used unchanged-hash targeted review and three material corrections received another full review. All workers and reviewers used Sol.
- Sources:
  - [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-prioritization-rules]] — rollover and ordinary credit/commit ordering, tie-breakers, and invoice-line priority
  - [[source-metronome-guides-pricing-packaging-billing-model-guides-prepaid-credits]] — prepaid-credit packaging, merchant-owned entitlement, Stripe payment gate, and example contradictions
  - [[source-metronome-guides-pricing-packaging-subscription-provision-your-customer]] — subscription contract fields, invoice placement, and pooled or individual seat credits
  - [[source-metronome-guides-reporting-insights-gtm-reporting-get-commit-and-usage-analytics]] — commit pacing and burn analysis with export-grain and deduplication cautions
  - [[source-metronome-guides-pricing-packaging-billing-model-guides-model-hierarchical-customer-relationships]] — parent-child contracts, shared commits, consolidated invoicing, reporting, and hierarchy limits
- Concepts: updated alerts, credits and commits, currencies, customers and contracts, invoicing, reporting, and subscriptions; no new concept page was required.
- Boundaries retained: rollover precedence qualifies the general prepaid-before-postpaid rule; prepaid entitlement remains merchant-owned; subscription seat-field spelling conflicts across guides; analytics SQL does not establish a coherent export table family; hierarchy amounts conflict with the USD-cent convention; hierarchy billing is Stripe-only in this guide; consolidation failure and hierarchy lifecycle semantics remain undocumented.
- Independent query audit: the initial fixed sample found one missing standard-subscription usage boundary. One bounded coordinator repair restored the raw's included-versus-separate-arrears distinction, the same auditor rechecked it, and the required expansion then passed 5/5 pages and 15/15 queries.
- Coverage after promotion: 225 collected documentation pages, 102 source summaries, and 129 raw pages without source summaries.
- Evidence: [campaign monitor](../tracking/ingest/metronome/metronome-campaign-16/monitor.md) and [quality audit](../tracking/ingest/metronome/metronome-campaign-16/quality-audit.md).

## 2026-08-15 — GitHub full ingest: `terraform-provider-metronome@0.1.0-alpha.3`

- Full-ingested work item `github-462a1c4b707deb10c6aa` at exact SHA `f06da6d6afee448e9fe9bad77d213cf6159d11f8` after complete serial review of the 37-path packet.
- Added [[source-github-terraform-provider-metronome]] and [[changelog-github-terraform-provider-metronome]] for provider maturity, configuration, generation dependencies, prerelease history, and future comparison routing.
- Preserved the decisive implementation boundary: this experimental release constructs a client but registers no Terraform resources and no data sources, so it cannot be represented as a production Metronome management integration.
- Kept generic serializer, validator, permission-description, and data-source changelog entries scoped to provider machinery rather than treating them as Metronome product capabilities.
- Coverage after promotion: 225 collected documentation pages, 97 source summaries, and 134 documentation raw pages without source summaries.

## 2026-08-15 — GitHub full ingest: `Metronome-Industries/ai` `main@59193aa`

- Full-ingested work item `github-5b78ff7871557dec5f21` at exact SHA `59193aabd9c43cca32f320d6f68f5d63d04034d4` after complete serial review of the 44-path packet and all 39 retained repository files.
- Added [[source-github-ai]] and [[changelog-github-ai]] for integration best practices, catalog and contract setup, PLG billing, CSM reviews, and Stripe usage-billing migration.
- Preserved the instruction-repository boundary: skills and dogfood scenarios are agent workflow evidence, not runtime SDK, API-schema, product-eligibility, or production-test evidence.
- Recorded conflicts around numeric event properties, `SUBSCRIPTION` versus `FLAT` rate representation, endpoint naming, and Stripe line-item consequences instead of selecting one example as canonical.
- Coverage after promotion: 225 collected documentation pages, 95 source summaries, and 134 documentation raw pages without source summaries.

## 2026-08-12 — GitHub full ingest: `@metronome/sdk@3.10.0`

- Full-ingested work item `github-f8e02889b5caf0809fc7` at exact SHA `f8ac11210fbca9616a220e82ea82ac1d340ea2df` after complete review of the 103-path Node/TypeScript SDK capsule.
- Added [[source-github-metronome-node]] and [[changelog-github-metronome-node]] for package/runtime behavior, transport and retry defaults, generated V1/V2 resources, usage ingestion, contracts, pricing, billing providers, and webhook verification.
- Recorded `3.10.0` additions for rate-card conversions, commit cost basis, and customer-commit applicability, plus the removed transition field and retained major-version migration boundaries.
- Preserved the evidence conflict where `api.md` lists removed Payments methods while the exact source tree omits that resource and the `3.7.0` changelog records its removal.
- Coverage after promotion: 225 collected documentation pages, 93 source summaries, and 134 documentation raw pages without source summaries.

## 2026-08-02 — Metronome Campaign 12 selective-ingest pilot completed

- Result: promoted the independently approved [[source-metronome-api-reference-custom-fields]] overview byte-identically and created [[metronome-custom-fields]] from overview evidence only.
- Classification: the create-key raw-reference audit returned `source_required`, and both delete-key semantic-triage reads returned `source_required`; the final verdict is `revise_routing_rule`, so cross-provider rollout is not authorized.
- Query quality: all three fixed queries passed. The overview question routed to the canonical overview source, while the create-key schema and delete-key consequence questions used their supplied prior-complete-read raw evidence without rereading either raw body.
- Read boundary: the pilot used five complete reads and no retry reads. The list-key, set-values, and delete-fields raw bodies were not read; their links remain navigation-only references and do not support endpoint facts.
- Coverage after promotion: 225 collected documentation pages, 91 source summaries, and 134 raw pages without source summaries.
- Evidence: [quality audit](../tracking/ingest/metronome/metronome-campaign-12/quality-audit.md) and [monitor](../tracking/ingest/metronome/metronome-campaign-12/monitor.md).

## 2026-08-01 — Metronome Campaign 11 completed

- Result: ten approved source pages from complete raw pages across sixteen worker attempts and sixteen independent reviews; four corrections required full rereview, two used unchanged-hash targeted review, and no job was rejected. All workers and reviewers used Sol.
- Sources:
  - [[source-metronome-plans-shared-endpoints-notifications]] — shared Plan and Contract alert routes, entity-specific parameter boundaries, and Plan alert types (raw SHA-256 `6df588128566f8fc0ae1f979da31313ce2e73fec83e3fc7781f795f871d5605c`)
  - [[source-metronome-plans-shared-endpoints-invoices]] — shared Plan and Contract invoice operations, adjustments, sub-line items, and tier detail (raw SHA-256 `8a61a8f4729d60da2071fe385a9888c3423a687e48c7164968f03fbda94e69aa`)
  - [[source-metronome-guides-reporting-insights-financial-reporting-reconcile-data]] — Data Export and API reconciliation patterns across Metronome, Salesforce, and Stripe (raw SHA-256 `4b1ea7a4112883d7d3ece76485a3e2f6b13fb34aef301cb7c4221ed4255c2ab2`)
  - [[source-metronome-api-reference-invoices-void-an-invoice]] — invoice void endpoint, OpenAPI requiredness, intended uses, and downstream unknowns (raw SHA-256 `640e3ff5d2ecb18704a5e328f51be80c314e3d2e8747483549ce798fa46cac49`)
  - [[source-metronome-guides-reporting-insights-financial-reporting-revenue-recognition]] — revenue categories, invoice and ledger query model, and downstream accounting ownership (raw SHA-256 `3af1b4a46ea87650dab7709269d6e7e10d89195ab7fbf5f37888b3c2740a132b`)
  - [[source-metronome-api-reference-notifications-list-system-notification-event-types]] — lifecycle event-type discovery, response taxonomy, and webhook-publication status (raw SHA-256 `92e8e204c0584f61d984df6bc80064ecd4cfbb1a84168b2a3b5fc4c098f88925`)
  - [[source-metronome-api-reference-invoices-regenerate-an-invoice]] — regeneration, recalculation and distribution wording, and invoice-ID contradiction (raw SHA-256 `3b72f09da3d09b82ff40ce731776e67728d8f26b4b238000f75c08f4d896052e`)
  - [[source-metronome-integrations-invoice-integrations-custom-invoice-integrations]] — finalized-invoice export, QuickBooks transformation, and integration ownership boundaries (raw SHA-256 `072923acb1509ae155263bafdae861c2c1cdcc17f4ceec282c3501309c1e71a9`)
  - [[source-metronome-api-reference-invoices-add-a-one-time-charge]] — deprecated Plans one-time charge contract, product restriction, and empty response boundary (raw SHA-256 `10c9181c948df1ca0705647683a8851d33caf2ad19a03d47bca190cdf75cd918`)
  - [[source-metronome-guides-reporting-insights-in-app-reporting]] — report generation, beta dashboards, ARR calculations, defaults, and freshness limits (raw SHA-256 `2b0aacc8bcf12478480762506a6484347b6bf4015a63077af03c3b6e37c5d886`)
- Concepts: updated alerts and notifications, credits and commits, integrations, invoicing, products and rate cards, reporting and analytics, webhooks, and generic payment-reconciliation reporting; no new concept page was required.
- Boundaries retained: shared route labels are not complete versioned API contracts; Metronome invoice voiding and regeneration do not prove downstream payment or accounting effects; regenerated-invoice ID examples conflict with the prose; revenue-recognition guidance remains a merchant-owned reporting model rather than accounting advice; report, dashboard, Data Export, and API freshness semantics remain separate; finalized-invoice comparison is not proof of payment or settlement.
- Independent audit: the immutable sample passed 3/3 pages and 9/9 queries with no expansion. Its initial close check found stale body-level company counts; one bounded coordinator repair changed 80/145 to 90/135 and a scoped mechanical recheck passed without repeating the semantic audit.
- Operational note: the final worker order was marked running before its native dispatch was issued; the coordinator detected and dispatched the existing attempt without creating a duplicate. This delayed wall-clock completion but caused no content, state, or write conflict.
- Routing finding: all-Sol workers did not reduce the six-review correction count relative to Campaign 10; two Campaign 11 corrections were mechanical and used targeted review, while four required full rereview.
- Coverage after promotion: 225 collected documentation pages, 90 ingested source summaries, and 135 pending pages.

## 2026-08-01 — Metronome Campaign 10 completed

- Result: ten approved source pages from complete raw pages across sixteen worker/reviewer attempts; six full reviews requested semantic corrections, no targeted-review shortcut was used, and no job was rejected. The immutable three-page audit passed 3/3 pages and 9/9 future-query tests, so no expanded audit was required.
- Sources:
  - [[source-metronome-integrations-platform-integrations-workato-connector]] — SDK-like Workato connector setup, API-token connection, example workflows, and per-environment boundary (raw SHA-256 `12b7d512419d74b31334bb091e1462ce41a164cfd5fff855b075fd960f9ce499`)
  - [[source-metronome-guides-platform-configuration-audit-logs]] — action attribution, outcomes, request correlation, and audit-evidence limitations (raw SHA-256 `98cfb48e35f0c94a32eac2e577bf8123f1a7a614010fa2c6b837cf358ebd012a`)
  - [[source-metronome-guides-platform-configuration-single-sign-on-sso]] — SAML 2.0 team login, identity-provider access control, retained users, and password cutover (raw SHA-256 `35facd1f2b955251b2fa3468eecc6eaddf2689abce75fa3f5f54c83fdeade837`)
  - [[source-metronome-guides-platform-configuration-allowlist]] — registry polling, allowlist automation, stale-rule risk, and layered-security boundaries (raw SHA-256 `29bed40bf7af74ba13e224024839a8d527c3f5e5eb58ed64b566cbf8f87b5e46`)
  - [[source-metronome-integrations-platform-integrations-segment]] — Segment destination setup, event-field mappings, transaction-ID default, and conditional actions (raw SHA-256 `e40b344b8ac5ff29c4875474fba52fcd55eac53613ecae7a3c7c6c96289f6048`)
  - [[source-metronome-integrations-tax-integrations-avalara]] — Avalara through Stripe's third-party tax-app framework, mappings, draft setting, and native Stripe Tax boundary (raw SHA-256 `669af4d8d1bd834e66ef476bc757315c1771076659d5058b5caa1826468e6e73`)
  - [[source-metronome-integrations-tax-integrations-anrok]] — Anrok calculation and compliance modes, Stripe invoice configuration, and provider boundaries (raw SHA-256 `efc6f41253304c312756134c96025738dc1b5c9871945b3a5fffb6b9cf54f4bc`)
  - [[source-metronome-guides-invoices-invoice-optimization-import-existing-invoices]] — contract migration, historical invoice periods, calculated balance effects, preview, and reporting breakdowns (raw SHA-256 `957691618bac7d40ab232998265c5722da477dd7d07495ec1814c6074272d3a5`)
  - [[source-metronome-guides-implement-metronome-core-concepts-billable-metrics-sql-editor]] — SQL query surface, output fallback, breakdown granularity, and scheduled metric swaps (raw SHA-256 `edc85071e55d41fcd4f39b9112d38c742d31e52f42a28058d5f25cfcf59fed4f`)
  - [[source-metronome-guides-implement-metronome-production-checklist]] — bounded readiness checks across ingestion, pricing, provisioning, invoices, controls, webhooks, and exports (raw SHA-256 `b65117c3c1f7847ad97e02d3b3bea9dd5b11dbd7cc45fc8e1cbef9f7733e7e9a`)
- Concepts: updated billable metrics, credits and commits, customers and contracts, event ingestion, integrations, invoicing, reporting, security, webhooks, and Stripe Tax; no new concept page was required.
- Boundaries retained: Workato examples do not prove complete endpoint coverage; audit visibility is not authorization or tamper-proof evidence; allowlisting is a layered control rather than authentication; Segment adapter requirements do not replace the direct-ingest schema; Avalara and Anrok third-party tax modes remain distinct from native Stripe Tax; historical import is not reduced to either migration-only or an undocumented correction workflow; SQL SUM outcomes stay example-scoped; production-checklist recommendations are not guarantees.
- Coverage after promotion: 225 collected documentation pages, 80 ingested source summaries, and 145 pending pages.

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
