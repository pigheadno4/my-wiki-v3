# Metronome Index

> Canonical router for the Metronome provider capsule. Collection is complete; canonical ingest proceeds one source at a time.

## Company

- [[metronome]] — company and platform page

## Coverage

| State | Count |
| --- | ---: |
| English canonical documentation pages collected | 225 |
| OpenAPI artifacts collected | 2 |
| Source summaries ingested | 40 |
| Documentation pages pending ingest | 185 |
| Collection failures | 0 |

Operational evidence:

- [Current collection status](../tracking/collections/metronome/collection-status.md)
- [2026-07-13 collection manifest](../tracking/collections/metronome/runs/2026-07-13T100930-manifest.md)

## Sources

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

## Concepts

- [[metronome-usage-based-billing]] — pay as you go, enterprise commitments, subscriptions with usage, and prepaid credits
- [[metronome-invoicing]] — native Stripe, marketplace, and ERP invoicing paths
- [[metronome-integrations]] — external-system integration boundaries and workflows
- [[metronome-credits-and-commits]] — commitment access and invoice schedules, rollover, and lifecycle boundaries
- [[metronome-event-ingestion]] — usage-event fields, limits, idempotency, design choices, and matching boundary
- [[metronome-billable-metrics]] — filters, aggregation operations, contextual grouping, and creation-time behavior
- [[metronome-products-and-rate-cards]] — product presentation, quantity conversion, and effective rates
- [[metronome-customers-and-contracts]] — ingest aliases, commercial terms, and draft-invoice activation
- [[metronome-reporting-and-analytics]] — exported table families, row grains, and nullability/version cautions
- [[metronome-webhooks]] — notification delivery, deduplication, API verification, and HMAC authenticity
- [[metronome-security-principles]] — explicit access grants, authenticated communication, and credential lifetime
- [[metronome-api-idempotency]] — key selection, conflict behavior, retention windows, and cached-error handling

## Planned concept taxonomy

Additional concept pages will be created only when grounded source summaries are ingested:

- `metronome-alerts-and-notifications.md`

## Related platforms

- [[stripe]] — owner and related billing platform
- [[stripe-index]] — Stripe-specific knowledge catalog

## Operations

- [[metronome-log]] — collection and future ingest history
- [Pilot benchmark and receipts](../tracking/ingest/metronome/pilot/)
