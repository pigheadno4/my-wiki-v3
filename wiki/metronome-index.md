# Metronome Index

> Canonical router for the Metronome provider capsule. Collection is complete; canonical ingest proceeds one source at a time.

## Company

- [[metronome]] — company and platform page

## Coverage

| State | Count |
| --- | ---: |
| English canonical documentation pages collected | 226 |
| OpenAPI artifacts collected | 2 |
| Source summaries ingested | 157 |
| Raw snapshots without source summaries | 135 |
| Collection failures | 0 |

Operational evidence:

- [Current collection status](../tracking/collections/metronome/collection-status.md)
- [2026-07-13 collection manifest](../tracking/collections/metronome/runs/2026-07-13T100930-manifest.md)

## Sources

- [[source-metronome-guides-reporting-insights-financial-reporting-asc-606-revenue-recognition]] — ASC 606 product mapping, reporting and reconciliation inputs, timing tensions, examples, and accounting-authority limits
- [[source-metronome-api-reference-alerts-create-a-threshold-notification]] — customer threshold configuration, schema boundaries, evaluation and response conflicts, and distinct Plan alert surface
- [[source-metronome-api-reference-customers-set-billing-provider-configurations-for-a-customer]] — customer provider-configuration creation, routing layers, Stripe suppression rules, and lifecycle unknowns
- [[source-metronome-api-reference-custom-fields-create-a-custom-field-key]] — key allowlisting, entity-applicability tension, uniqueness, downstream invoice use, and response limits
- [[source-metronome-api-reference-custom-fields-delete-a-custom-field-key]] — key removal, managed-entity scope, existing-value inaccessibility, and propagation limits

- [[source-metronome-api-reference-products-get-a-product]] — single-product state and update history, composite configuration, group keys, custom fields, and integration boundaries
- [[source-metronome-api-reference-products-list-products]] — paginated catalog retrieval, archive filtering, complete-version-history claim, product schemas, and contradictions
- [[source-metronome-api-reference-customers-archive-a-customer]] — irreversible customer archival, contract and invoice effects, alias reservation, and notification suppression
- [[source-metronome-guides-implement-metronome-core-concepts-non-monotonically-increasing-metrics]] — incremental non-monotonic billing, negative quantities, effective periods, credit ordering, and reporting boundaries
- [[source-metronome-integrations-platform-integrations-sfdc-integration]] — outbound Salesforce synchronization, setup layers, daily cadence, object mappings, and completeness limits

- [[source-metronome-api-reference-invoices-get-an-invoice]] — single-invoice retrieval, state, line items, applied balances, hierarchy, and integration-status boundaries
- [[source-metronome-api-reference-customers-list-customers]] — account customer filters, pagination, identity, aliases, custom fields, and archive visibility
- [[source-metronome-api-reference-customers-update-a-customer-name]] — customer display-name mutation, truncation, propagation claim, retry, and lifecycle boundaries
- [[source-metronome-guides-implement-metronome-core-concepts-how-invoicing-works]] — native invoice generation, types, lifecycle, calculation, and presentation model
- [[source-metronome-integrations-marketplace-integrations-aws]] — AWS Marketplace listing, IAM delegation, customer mapping, metering, and external-provider boundaries

- [[source-metronome-api-reference-customers-get-a-customer]] — customer identity, ingest aliases, custom fields, archival state, and billing-configuration boundary
- [[source-metronome-api-reference-billable-metrics-list-all-billable-metrics]] — billable-metric discovery, configuration schema, archive filtering, pagination, and documented contradictions
- [[source-metronome-api-reference-credits-and-commits-list-balances]] — detailed customer balances, endpoint-specific pagination, archive visibility, ledgers, and denomination boundaries
- [[source-metronome-api-reference-credits-and-commits-create-a-credit]] — customer-level credit creation, access schedules, applicability selectors, priority, and idempotency boundaries
- [[source-metronome-api-reference-settings-set-up-account-level-billing-provider]] — account-level marketplace provider setup, credential boundaries, identifier layers, and readiness limits

- [[source-metronome-api-reference-settings-list-account-level-billing-providers]] — account-level billing-provider delivery methods, pagination, configuration exposure, and identifier boundaries
- [[source-metronome-api-reference-credits-and-commits-disable-trueup-for-commit]] — postpaid true-up invoice suppression, API-wide idempotency, and lifecycle unknowns
- [[source-metronome-api-reference-contracts-get-subscription-quantity-history]] — historical subscription quantities and prices with the future-change boundary
- [[source-metronome-api-reference-contracts-archive-a-contract]] — permanent archival, invoice disposition, balance expiration entries, and historical visibility
- [[source-metronome-api-reference-usage-search-events]] — sampled 34-day event search, matched-customer and metric diagnostics, keyed replay, and completeness limits

- [[source-metronome-api-reference-settings-list-pricing-units]] — pricing-unit enumeration, USD cents identifier, pagination, and response-schema boundaries
- [[source-metronome-api-reference-rate-cards-archive-a-rate-card]] — permanent new-contract disablement and preservation of existing-contract pricing
- [[source-metronome-api-reference-plans-list-plans]] — deprecated Plans listing schema and Contracts migration boundary
- [[source-metronome-api-reference-credits-and-commits-release-external-payment-gate-threshold-commit]] — external payment outcome correlation and pending-commit release or cancellation
- [[source-metronome-api-reference-invoices-get-an-invoice-pdf]] — PDF retrieval, required identifiers, response-media, and generic not-found boundaries

- [[source-metronome-guides-pricing-packaging-make-pricing-changes-make-a-pricing-change]] — package-based cohort pricing changes, alias transitions, and worked-example contradictions
- [[source-metronome-guides-pricing-packaging-make-pricing-changes-edit-or-override-a-contract]] — contract override models, dimensional targeting, precedence, and create-only boundary
- [[source-metronome-guides-reporting-insights-data-export-cookbook]] — example export queries and their environment, grain, deduplication, effective-time, and currency boundaries
- [[source-metronome-guides-pricing-packaging-make-pricing-changes-edit-contract]] — contract edit lifecycle, effective history, audit surfaces, and invoice-state guards
- [[source-metronome-guides-reporting-insights-financial-reporting-revenue-recognition-examples]] — illustrative revenue scenarios with amount, key, classification, and accounting-authority boundaries

- [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-prioritization-rules]] - rollover and ordinary credit/commit ordering, tie-breakers, and invoice-line priority
- [[source-metronome-guides-pricing-packaging-billing-model-guides-prepaid-credits]] - prepaid-credit packaging, merchant-owned entitlement, Stripe payment gate, and example contradictions
- [[source-metronome-guides-pricing-packaging-subscription-provision-your-customer]] - subscription contract fields, invoice placement, and pooled or individual seat credits
- [[source-metronome-guides-reporting-insights-gtm-reporting-get-commit-and-usage-analytics]] - commit pacing and burn analysis with export-grain and deduplication cautions
- [[source-metronome-guides-pricing-packaging-billing-model-guides-model-hierarchical-customer-relationships]] - parent-child contracts, shared commits, consolidated invoicing, reporting, and hierarchy limits

- [[source-github-ai]] - Metronome-authored AI skills for integration, catalog and contract setup, PLG billing, CSM reviews, and Stripe migration
- [[changelog-github-ai]] - commit-qualified Metronome AI skills history and future comparison rule
- [[source-github-metronome-node]] - `@metronome/sdk@3.10.0` server client, runtime, transport, generated API surface, and webhook helper
- [[changelog-github-metronome-node]] - package-qualified Node SDK release and upgrade history
- [[source-github-terraform-provider-metronome]] - experimental `0.1.0-alpha.3` provider configuration and empty resource/data-source surface
- [[changelog-github-terraform-provider-metronome]] - package-qualified Terraform provider prerelease history and future comparison rule
- [[source-metronome-guides-get-started-home]] — documentation entry point, getting-started routes, and four pricing/packaging models
- [[source-metronome-guides-get-started-developer-sdks]] — SDK installation and an introductory event-to-invoice implementation path
- [[source-metronome-guides-events-design-usage-events]] — event-design principles, cadence tradeoffs, contextual properties, and future-only metric changes
- [[source-metronome-guides-events-high-volume-ingestion]] — throughput limits, batching, pipeline observability, and recovery
- [[source-metronome-api-reference-usage-ingest-events]] — authenticated endpoint schema, idempotency window, response gaps, and advertised capacity
- [[source-metronome-guides-get-started-stripe-marketplace-app]] — Stripe Dashboard app, customer management, and contract creation
- [[source-metronome-guides-get-started-metronome-dashboard-quickstart]] — dashboard first-invoice workflow, immutable metric choices, and Sandbox testing
- [[source-metronome-guides-pricing-packaging-billing-model-guides-enterprise-commit]] — enterprise commitment schedules, tag-scoped discounts, lifecycle, and example cautions
- [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-create-a-pre-paid-commit]] — free credits, prepaid/postpaid commits, recurring grants, transitions, and line-item drawdown
- [[source-metronome-guides-customers-billing-optimize-customer-experience-prepaid-balance-thresholds]] — automatic recharge, balance filtering, custom pricing units, and payment-gate recovery
- [[source-metronome-guides-customers-billing-manage-customers-schedule-billing-provider-change]] — provider transition matrix, invoice routing, schedule limits, and timing cautions
- [[source-metronome-integrations-invoice-integrations-stripe]] — Stripe account routing, invoice settings, status synchronization, payment timing, and limits
- [[source-metronome-integrations-tax-integrations-stripe-tax]] — Stripe Tax prerequisites, product mapping, invoice finalization, and threshold override
- [[source-metronome-api-reference-credits-and-commits-create-a-commit]] — customer-level commit requirements, schedules, scope, priority, and response boundary
- [[source-metronome-api-reference-credits-and-commits-edit-a-commit]] — targeted commit mutation, schedule operations, invoice-state limits, and schema cautions
- [[source-metronome-guides-invoices-overview]] — Stripe, marketplace, and ERP invoicing options
- [[source-metronome-guides-reporting-insights-data-export-database-reference]] — warehouse schema navigation, snapshot grains, and query cautions
- [[source-metronome-guides-reporting-insights-data-export-overview]] — destination scope, transfer cadence, freshness, and append-only object-storage delivery
- [[source-metronome-api-reference-contracts-create-a-contract]] — create endpoint, nested request families, conditional requirements, and response boundary
- [[source-metronome-api-reference-invoices-preview-events]] — request modes, event constraints, deduplication, and draft-invoice response
- [[source-metronome-api-reference-contracts-get-contract-edit-history]] — audit scope, edit-operation groups, and response constraints
- [[source-metronome-api-reference-pagination]] — cursor parameters, completion signal, limit guidance, and undocumented ordering
- [[source-metronome-api-reference-status-codes]] — HTTP response categories, JSON error envelope, rate-limit scopes, and retry boundaries
- [[source-metronome-api-reference-idempotency]] — event, customer, resource, and POST idempotency mechanisms and lifetimes
- [[source-metronome-guides-implement-metronome-core-concepts-create-billable-metrics]] — metric roles, aggregations, group-key constraints, reflow, and testing
- [[source-metronome-api-reference-customers-create-a-customer]] — provisioning, aliases, downstream configuration, and response boundaries
- [[source-metronome-api-reference-contracts-amend-a-contract]] — legacy amendment lifecycle, nested schedules, overrides, and schema gaps
- [[source-metronome-guides-platform-configuration-setup-webhooks]] — event families, retry and duplicate handling, signature verification, and Slack delivery
- [[source-metronome-guides-platform-configuration-security-principles]] — least privilege, zero-trust communication, and short-lived credentials
- [[source-metronome-api-reference-authentication]] — bearer-token creation, SDK configuration, permission scopes, and archival
- [[source-metronome-api-reference-introduction]] — API directory, stated platform capabilities, SDK routes, and endpoint-domain map
- [[source-metronome-api-reference-postman]] — live OpenAPI import, collection bearer-token setup, and illustrative customer request
- [[source-metronome-api-reference-api-quickstart]] — token creation, four SDK installs, environment configuration, and connectivity test
- [[source-metronome-guides-implement-metronome-core-concepts-send-usage-events]] — producer event representation, queue/retry policy, heartbeat idempotence, and asynchronous customer matching
- [[source-metronome-guides-implement-metronome-core-concepts-create-products-contracts]] — product types, price ownership, creation, effective-dated edits, tags, and group keys
- [[source-metronome-guides-get-started-how-metronome-works]] — ordered event-to-invoice architecture, object responsibilities, and timing boundaries
- [[source-metronome-guides-implement-metronome-core-concepts-provision-contract]] — contract provisioning, charge consolidation, provider attachment, discounts, and usage filters
- [[source-metronome-guides-implement-metronome-core-concepts-create-manage-rate-cards]] — aliases, effective changes, dimensional pricing, and tiers
- [[source-metronome-api-reference-billable-metrics-create-a-billable-metric]] — create schema, filters, SQL exclusivity, contradictions, and UUID response
- [[source-metronome-guides-implement-metronome-core-concepts-provision-customer]] — alias hierarchy, retroactive association, rating prerequisite, and provider routing
- [[source-metronome-guides-pricing-packaging-subscription-subscription-overview]] — subscription products, quantity-one prices, contracts, and credit scope
- [[source-metronome-guides-pricing-packaging-subscription-define-subscription-pricing]] — per-offering products, seat key, list pricing, and multi-rate setup
- [[source-metronome-guides-pricing-packaging-subscription-manage-subscription-lifecycle]] — price propagation, trials, transitions, proration, and cancellation
- [[source-metronome-guides-platform-configuration-role-based-access-rbac]] — built-in roles, SSO claims, default denial, and token role assignment
- [[source-metronome-guides-pricing-packaging-billing-model-guides-pay-as-you-go]] — illustrative PayGo packaging, provisioning, plan tags, and Stripe delivery
- [[source-metronome-guides-implement-metronome-planning-your-billing-architecture]] — five-lens architecture planning for data, terms, distribution, and operations
- [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-manual-payment-gated-commits]] — existing-contract Stripe gate, payment outcomes, and manual retry
- [[source-metronome-guides-pricing-packaging-billing-model-guides-create-a-trial]] — capped-credit and uncapped zero-multiplier trial patterns
- [[source-metronome-api-reference-billable-metrics-get-a-billable-metric]] — single-metric schema, matching, aggregation, grouping, and archive state
- [[source-metronome-api-reference-billable-metrics-get-billable-metrics-for-a-customer]] — customer metric listing, pagination, filters, and schema defects
- [[source-metronome-guides-customers-billing-overview]] — Customers & Billing navigation across lifecycle management, dashboards and spend controls, fraud and entitlement themes, and alerts
- [[source-metronome-guides-customers-billing-manage-customers-manage-product-access]] — product-access navigation overview spanning customer provisioning, contract lifecycle, temporary trials, and entitlement-state notifications
- [[source-metronome-guides-customers-billing-set-up-notifications-create-and-manage-notifications]] — notification families, webhook delivery, evaluation timing, and threshold states
- [[source-metronome-guides-customers-billing-optimize-customer-experience-india-e-mandates]] — Indian-card Stripe mandate setup, threshold and recurring configuration, invoice mapping, and responsibility boundaries
- [[source-metronome-guides-customers-billing-set-up-notifications-offset-notifications]] — relative-time offsets, payload semantics, prospective behavior, setup paths, and recurring-commit caveat
- [[source-metronome-guides-customers-billing-manage-customers-spend-trackers]] — public-beta commit-purchase accumulation, threshold-discount caps, contract retrieval, and enforcement boundaries
- [[source-metronome-guides-customers-billing-optimize-customer-experience-set-customer-spend-control]] — contract spend thresholds, incremental billing, configuration updates, and Stripe/external payment gates
- [[source-metronome-guides-customers-billing-optimize-customer-experience-preview-event-cost]] — contract-aware event-cost simulation, preview modes, multi-contract draft output, deduplication conflict, and limits
- [[source-metronome-guides-customers-billing-optimize-customer-experience-customer-controls]] — customer-defined spend, grouped-dimension, commit-balance, and invoice-total alerts with merchant enforcement
- [[source-metronome-guides-customers-billing-optimize-customer-experience-get-remaining-balance]] — aggregate and ledger balance retrieval, signed calculation, precision, timestamps, and manual adjustments
- [[source-metronome-guides-pricing-packaging-billing-model-guides-guides-home]] — billing-model navigation for pay-as-you-go, enterprise commits, usage subscriptions, and pre-paid credits
- [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-alerts]] — balance, percentage, and days-remaining notifications with custom-field filtering and action boundaries
- [[source-metronome-guides-pricing-packaging-overview]] — pricing-and-packaging navigation across billing models, pricing changes, credits, commits, and examples
- [[source-metronome-guides-platform-configuration-metronome-pricing-model]] — platform fee and consumption accounting for accepted events, generated billings, and exported rows
- [[source-metronome-guides-implement-metronome-core-concepts-billable-metrics-basic-filters]] — Basic Filters matching, property requirements, grouped `COUNT`, and streaming aggregation boundary
- [[source-metronome-guides-pricing-packaging-make-pricing-changes-use-currency-custompricingunits]] — fiat denomination, custom-unit rate setup, balance drawdown, and residual invoice conversion
- [[source-metronome-guides-events-send-usage-events]] — required event fields, customer attribution, retry policy, heartbeat IDs, and duplicate-suppression scope
- [[source-metronome-guides-invoices-invoice-optimization-issue-credit-memos]] — future-credit versus A/R memo boundary, invoice-state corrections, re-billing, and refund ownership
- [[source-metronome-api-reference-security-get-services]] — bearer-authenticated service registry, IP direction labels, schema, and notice boundary
- [[source-metronome-api-reference-alerts-reset-a-threshold-notification]] — customer-alert reset, asynchronous reassessment, empty `200`, and idempotency unknowns
- [[source-metronome-integrations-platform-integrations-workato-connector]] — Workato connector installation, API-token connection, example workflows, and environment isolation
- [[source-metronome-guides-platform-configuration-audit-logs]] — action attribution, outcome visibility, request correlation, and audit-evidence boundaries
- [[source-metronome-guides-platform-configuration-single-sign-on-sso]] — SAML team login, identity-provider access removal, retained metadata, and password-login cutover
- [[source-metronome-guides-platform-configuration-allowlist]] — registry polling, network-rule automation, stale-allowlist risk, and notice wording
- [[source-metronome-integrations-platform-integrations-segment]] — Segment source/token setup, explicit event mappings, default message ID, and conditional actions
- [[source-metronome-integrations-tax-integrations-avalara]] — Avalara tax-app workflow, metadata mapping, draft requirement, and native Stripe Tax distinction
- [[source-metronome-integrations-tax-integrations-anrok]] — Anrok tax calculation and compliance modes with Stripe invoice configuration
- [[source-metronome-guides-invoices-invoice-optimization-import-existing-invoices]] — historical contract/invoice migration, calculated totals, balance effects, preview, and breakdowns
- [[source-metronome-guides-implement-metronome-core-concepts-billable-metrics-sql-editor]] — SQL inputs and functions, output-column fallback, granularity, and scheduled metric swaps
- [[source-metronome-guides-implement-metronome-production-checklist]] — bounded production-readiness checks for usage, pricing, contracts, invoices, controls, and operations
- [[source-metronome-plans-shared-endpoints-notifications]] — shared Plan and Contract alert routes, entity-specific parameter boundaries, and Plan alert types
- [[source-metronome-plans-shared-endpoints-invoices]] — shared Plan and Contract invoice operations, adjustments, sub-line items, and tier detail
- [[source-metronome-guides-reporting-insights-financial-reporting-reconcile-data]] — Data Export and API reconciliation patterns across Metronome, Salesforce, and Stripe
- [[source-metronome-api-reference-invoices-void-an-invoice]] — invoice void endpoint, requiredness boundaries, intended uses, and downstream unknowns
- [[source-metronome-guides-reporting-insights-financial-reporting-revenue-recognition]] — revenue-reporting categories, invoice and ledger query model, and accounting ownership boundary
- [[source-metronome-api-reference-notifications-list-system-notification-event-types]] — lifecycle event-type discovery, response taxonomy, and webhook-publication status
- [[source-metronome-api-reference-invoices-regenerate-an-invoice]] — invoice regeneration, recalculation and distribution, refreshed distinct-ID examples, and remaining lineage and retry boundaries
- [[source-metronome-integrations-invoice-integrations-custom-invoice-integrations]] — finalized-invoice export flow, QuickBooks transformation, and integration ownership boundaries
- [[source-metronome-api-reference-invoices-add-a-one-time-charge]] — deprecated Plans one-time charge contract, product restriction, and empty response boundary
- [[source-metronome-guides-reporting-insights-in-app-reporting]] — report generation, beta dashboards, ARR calculations, defaults, and freshness limits
- [[source-metronome-api-reference-custom-fields]] — custom-field purpose, supported object examples, persistence, uniqueness, and invoice-line propagation

- [[source-metronome-api-reference-contracts-get-a-contract-v2]] — contract-state read, historical configuration, optional balance and ledger detail, and incomplete embedded collections
- [[source-metronome-api-reference-invoices-list-invoices]] — customer invoice collection, filters, pagination, mutable drafts, and ordering contradiction
- [[source-metronome-api-reference-credit-grants-void-a-credit-grant]] — legacy Plans grant void mutation, invoice option, uniqueness release, and recovery limits
- [[source-metronome-guides-implement-metronome-core-concepts-packages-overview]] — reusable package terms, contract provisioning, aliases, immutable versions, and propagation boundaries
- [[source-metronome-integrations-marketplace-integrations-azure]] — Azure offer and identity layers, metering, corrections, late-event window, currency, and lifecycle ownership
- [[source-metronome-api-reference-contracts-get-the-rate-schedule-for-a-contract]] — contract rate-schedule retrieval, effective-time and selector scope, returned pricing surfaces, and unknown precedence
- [[source-metronome-api-reference-credit-grants-list-credit-ledger-entries]] — deprecated Plans credit-ledger listing, ordering boundaries, amount-sign contradiction, pagination, and incomplete history
- [[source-metronome-api-reference-contracts-update-invoice-issue-date]] — draft invoice issue-date mutation, schedule separation, lifecycle boundaries, and idempotent retry context
- [[source-metronome-api-reference-security-get-audit-logs]] — account audit retrieval, time and resource filters, continuous cursor polling, attribution gaps, and response-shape contradiction
- [[source-metronome-integrations-marketplace-integrations-gcp]] — GCP Marketplace setup, identity mapping, USD-cent metering, correction limits, and merchant-owned outcomes
- [[source-metronome-guides-get-started-api-quickstart]] — programmatic sandbox onboarding, event-to-invoice flow, stale timestamps, diagnostics, and integration limits
- [[source-metronome-guides-customers-billing-set-up-notifications-system-notifications]] — lifecycle policy catalog, payload-family distinction, account-wide webhook scope, and prospective enablement
- [[source-metronome-guides-pricing-packaging-subscription-manage-seats]] — aggregate and identity-bearing seat lifecycle, configuration-dependent billing, seat alerts, history, and retry risk

- [[source-metronome-api-reference-contracts-edit-a-contract]] — contract mutation scope, invoice and grant lifecycle, threshold charges, idempotency conflict, and provider-boundary contradiction
- [[source-metronome-api-reference-credits-and-commits-list-seat-balances]] — seat balance identity, filtering, detail expansions, pagination, completeness, and reconciliation limits
- [[source-metronome-integrations-invoice-integrations-netsuite]] — Public Beta NetSuite billing and revenue-system modes, identity mappings, sync diagnostics, recovery, and external authority limits
- [[source-metronome-api-reference-alerts-get-a-threshold-notification]] — customer threshold current-state lookup, archived behavior, targeted scope, timestamp conflict, and replay freshness boundary
- [[source-metronome-api-reference-plans-get-plan-details]] — deprecated Plan retrieval, legacy price and credit-grant configuration, custom fields, and Contracts migration boundary
- [[source-metronome-api-reference-sdks]] — Python, Node.js, Ruby, and Go usage-billing route with retry, chronology, grouping, and authority boundaries
- [[source-metronome-guides-pricing-packaging-billing-model-guides-token-billing]] — private-preview managed token pricing, custom-unit and package flow, event mapping, and model-update boundaries

## Concepts

- [[metronome-usage-based-billing]] — pay as you go, enterprise commitments, subscriptions with usage, and prepaid credits
- [[metronome-token-billing]] — private-preview managed LLM token-cost-plus-markup workflow
- [[metronome-invoicing]] — native Stripe, marketplace, and ERP invoicing paths
- [[metronome-integrations]] — external-system integration boundaries and workflows
- [[metronome-credits-and-commits]] — commitment access and invoice schedules, rollover, and lifecycle boundaries
- [[metronome-event-ingestion]] — usage-event fields, limits, idempotency, design choices, and matching boundary
- [[metronome-billable-metrics]] — filters, aggregation operations, contextual grouping, and creation-time behavior
- [[metronome-products-and-rate-cards]] — product presentation, quantity conversion, and effective rates
- [[metronome-packages-and-aliases]] — package cohorts, effective-dated alias transitions, and migration boundaries
- [[metronome-customers-and-contracts]] — ingest aliases, commercial terms, and draft-invoice activation
- [[metronome-reporting-and-analytics]] — exported table families, row grains, and nullability/version cautions
- [[metronome-webhooks]] — notification delivery, deduplication, API verification, and HMAC authenticity
- [[metronome-security-principles]] — explicit access grants, authenticated communication, and credential lifetime
- [[metronome-api-idempotency]] — key selection, conflict behavior, retention windows, and cached-error handling
- [[metronome-subscriptions]] — subscription pricing, contract configuration, transitions, and cancellation
- [[metronome-alerts-and-notifications]] — alert definitions, trial-balance triggers, and merchant action boundary
- [[metronome-spend-trackers]] — public-beta commit-purchase accumulators, threshold-discount integration, retrieval, and billing-state unknowns
- [[metronome-spend-threshold-billing]] — contract-level incremental collection with optional commit-release payment gating, distinct from product-access enforcement and a customer-wide cross-contract cap
- [[metronome-currencies-and-custom-pricing-units]] — supported fiat currencies, Metronome-specific API denomination, custom-unit rates, balance drawdown, and invoice conversion
- [[metronome-custom-fields]] — platform-object metadata, external-system mappings, uniqueness, and persistence

## Related platforms

- [[stripe]] — owner and related billing platform
- [[stripe-index]] — Stripe-specific knowledge catalog

## Operations

- [[metronome-log]] — collection and future ingest history
- [Pilot benchmark and receipts](../tracking/ingest/metronome/pilot/)
