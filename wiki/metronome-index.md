# Metronome Index

> Canonical router for the Metronome provider capsule. Collection is complete; the controlled ingest pilot is underway.

## Company

- [[metronome]] — company and platform page

## Coverage

| State | Count |
| --- | ---: |
| English canonical documentation pages collected | 225 |
| OpenAPI artifacts collected | 2 |
| Source summaries ingested | 4 |
| Documentation pages pending ingest | 221 |
| Collection failures | 0 |

Operational evidence:

- [Current collection status](../tracking/collections/metronome/collection-status.md)
- [2026-07-13 collection manifest](../tracking/collections/metronome/runs/2026-07-13T100930-manifest.md)

## Sources

- [[source-metronome-guides-get-started-home]] — documentation entry point, getting-started routes, and four pricing/packaging models
- [[source-metronome-guides-get-started-developer-sdks]] — SDK installation and an introductory event-to-invoice implementation path
- [[source-metronome-guides-invoices-overview]] — Stripe, marketplace, and ERP invoicing options
- [[source-metronome-guides-reporting-insights-data-export-database-reference]] — warehouse schema navigation, snapshot grains, and query cautions

## Concepts

- [[metronome-usage-based-billing]] — pay as you go, enterprise commitments, subscriptions with usage, and prepaid credits
- [[metronome-invoicing]] — native Stripe, marketplace, and ERP invoicing paths
- [[metronome-event-ingestion]] — usage-event fields, limits, idempotency, and matching boundary
- [[metronome-billable-metrics]] — filters, aggregation operations, grouping, and creation-time behavior
- [[metronome-products-and-rate-cards]] — product presentation, quantity conversion, and effective rates
- [[metronome-customers-and-contracts]] — ingest aliases, commercial terms, and draft-invoice activation
- [[metronome-reporting-and-analytics]] — exported table families, row grains, and nullability/version cautions

## Planned concept taxonomy

Additional concept pages will be created only when grounded source summaries are ingested:

- `metronome-credits-and-commits.md`
- `metronome-alerts-and-notifications.md`
- `metronome-integrations.md`

## Related platforms

- [[stripe]] — owner and related billing platform
- [[stripe-index]] — Stripe-specific knowledge catalog

## Operations

- [[metronome-log]] — collection and future ingest history
- [Pilot benchmark and receipts](../tracking/ingest/metronome/pilot/)
