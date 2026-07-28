---
title: "Metronome"
type: company
tags: [metronome, stripe, usage-based-billing]
source_count: 9
---

## Overview

Metronome is maintained as an independent provider capsule related to [[stripe]]. Its documentation covers usage-based pricing and packaging, an SDK-driven event-to-invoice workflow, and invoicing options spanning Stripe, cloud marketplaces, and ERP workflows.

## Documented billing models

- Pay as you go charges customers in arrears for actual usage.
- Enterprise models can include prepaid or postpaid commitments, negotiated discounts, one-time charges, and renewals.
- Hybrid subscriptions combine recurring revenue with usage-based components.
- Prepaid credit models allow upfront purchases, with auto-recharge or gated access after depletion.

The documentation home is a navigation overview. The SDK walkthrough adds an introductory implementation path, while complete API schemas and lifecycle rules still require dedicated references.

## SDK usage-billing workflow

- Python, Node.js, Ruby, and Go SDKs demonstrate a common event-to-invoice flow.
- Event ingestion uses transaction IDs for deduplication and can associate application identifiers with customers through ingest aliases.
- Event design starts from billing and operational requirements, follows the data and cadence available in the source system, and retains contextual properties for future reporting or pricing changes.
- Billable metrics filter and aggregate events; products and rate cards turn those measurements into prices.
- Customer contracts apply the rate card and produce draft invoices that update with usage.
- The Preview Events API can calculate draft invoices from proposed usage before processing, using either replacement or merged historical-usage semantics.

The create-contract API adds package or rate-card selection, commits and credits, pricing overrides, subscriptions, scheduled charges, usage routing, threshold billing, provider configuration, and customer hierarchy. Only customer ID and contract start are unconditionally required at the top level; nested requirements depend on the selected structures.

The contract edit-history API exposes recorded changes made through the UI and contract-changing endpoints, grouping additions, updates, archives, and removals for contract audit work.

## Invoicing options

- Native Stripe invoicing can use Stripe Tax, dunning, and other Stripe product-suite capabilities.
- Marketplace invoicing automates metering and invoice creation for AWS, Azure, and GCP.
- ERP invoicing includes out-of-the-box and custom integrations for collection, book-closing, and revenue workflows.

## Notifications and webhooks

- Webhook categories span thresholds, contract and balance-object lifecycles, invoices, integration failures, marketplace disablement, and payment gating.
- Receivers should acknowledge quickly, process asynchronously, and deduplicate by notification ID because retries can continue for up to two days.
- Authenticity can be established by retrieving authoritative API data or verifying an HMAC-SHA256 signature over the request date and exact body bytes.

## Reporting and data export

- Warehouse exports cover raw events, customers, invoices, contracts, pricing, packages, payments, alerts, and metadata.
- Finalized invoice rows, daily draft snapshots, and invoice-breakdown snapshots have distinct grains and update behavior.
- Exported columns may all appear nullable because of the export methodology, so warehouse types alone do not establish business optionality.

## Knowledge status

- Collected documentation pages: 225
- Ingested source summaries: 9
- Documentation pages pending ingest: 216

## Sources

- [[source-metronome-guides-get-started-home]] — documentation entry point and four pricing/packaging routes
- [[source-metronome-guides-get-started-developer-sdks]] — SDK setup and introductory event-to-invoice workflow
- [[source-metronome-guides-events-design-usage-events]] — usage-event design principles, cadence tradeoffs, and future metric flexibility
- [[source-metronome-guides-invoices-overview]] — Stripe, marketplace, and ERP invoicing options
- [[source-metronome-guides-reporting-insights-data-export-database-reference]] — warehouse schema families, grains, and query cautions
- [[source-metronome-api-reference-contracts-create-a-contract]] — contract creation request families and conditional rules
- [[source-metronome-api-reference-invoices-preview-events]] — draft-invoice previews from proposed usage events
- [[source-metronome-api-reference-contracts-get-contract-edit-history]] — cross-channel contract edit history and change categories
- [[source-metronome-guides-platform-configuration-setup-webhooks]] — webhook categories, retry behavior, deduplication, and verification

## Related

- [[metronome-index]] — provider catalog and coverage
- [[metronome-log]] — collection and future ingest history
- [[stripe-index]] — related Stripe catalog
- [[metronome-usage-based-billing]] — platform-specific billing concept
- [[metronome-invoicing]] — platform-specific invoicing options
- [[metronome-event-ingestion]] — usage-event contract and deduplication
- [[metronome-billable-metrics]] — event matching, aggregation, and grouping
- [[metronome-products-and-rate-cards]] — product presentation and effective pricing
- [[metronome-customers-and-contracts]] — customer aliases, commercial terms, and invoice activation
- [[metronome-reporting-and-analytics]] — warehouse exports, snapshot grains, and query cautions
- [[metronome-webhooks]] — notification delivery, reliability, and authenticity
