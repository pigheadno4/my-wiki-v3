# Metronome Index

> Canonical router for the Metronome provider capsule. Collection is complete; canonical ingest proceeds one source at a time.

## Company

- [[metronome]] — company and platform page

## Coverage

| State | Count |
| --- | ---: |
| English canonical documentation pages collected | 225 |
| OpenAPI artifacts collected | 2 |
| Source summaries ingested | 15 |
| Documentation pages pending ingest | 210 |
| Collection failures | 0 |

Operational evidence:

- [Current collection status](../tracking/collections/metronome/collection-status.md)
- [2026-07-13 collection manifest](../tracking/collections/metronome/runs/2026-07-13T100930-manifest.md)

## Sources

- [[source-metronome-guides-get-started-home]] — documentation entry point, getting-started routes, and four pricing/packaging models
- [[source-metronome-guides-get-started-developer-sdks]] — SDK installation and an introductory event-to-invoice implementation path
- [[source-metronome-guides-events-design-usage-events]] — event-design principles, cadence tradeoffs, contextual properties, and future-only metric changes
- [[source-metronome-guides-events-high-volume-ingestion]] — throughput limits, batching, pipeline observability, and recovery
- [[source-metronome-guides-get-started-stripe-marketplace-app]] — Stripe Dashboard app, customer management, and contract creation
- [[source-metronome-guides-pricing-packaging-billing-model-guides-enterprise-commit]] — enterprise commitment schedules, tag-scoped discounts, lifecycle, and example cautions
- [[source-metronome-integrations-invoice-integrations-stripe]] — Stripe account routing, invoice settings, status synchronization, payment timing, and limits
- [[source-metronome-api-reference-credits-and-commits-create-a-commit]] — customer-level commit requirements, schedules, scope, priority, and response boundary
- [[source-metronome-guides-invoices-overview]] — Stripe, marketplace, and ERP invoicing options
- [[source-metronome-guides-reporting-insights-data-export-database-reference]] — warehouse schema navigation, snapshot grains, and query cautions
- [[source-metronome-api-reference-contracts-create-a-contract]] — create endpoint, nested request families, conditional requirements, and response boundary
- [[source-metronome-api-reference-invoices-preview-events]] — request modes, event constraints, deduplication, and draft-invoice response
- [[source-metronome-api-reference-contracts-get-contract-edit-history]] — audit scope, edit-operation groups, and response constraints
- [[source-metronome-guides-platform-configuration-setup-webhooks]] — event families, retry and duplicate handling, signature verification, and Slack delivery
- [[source-metronome-guides-platform-configuration-security-principles]] — least privilege, zero-trust communication, and short-lived credentials

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

## Planned concept taxonomy

Additional concept pages will be created only when grounded source summaries are ingested:

- `metronome-alerts-and-notifications.md`

## Related platforms

- [[stripe]] — owner and related billing platform
- [[stripe-index]] — Stripe-specific knowledge catalog

## Operations

- [[metronome-log]] — collection and future ingest history
- [Pilot benchmark and receipts](../tracking/ingest/metronome/pilot/)
