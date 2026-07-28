---
title: "Metronome"
type: company
tags: [metronome, stripe, usage-based-billing]
source_count: 15
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
- High-volume ingestion supports batches of 100 events, with documented infrastructure capacity up to 110,000 events per second and a default 5,000-events-per-second limit. Metronome recommends event sampling, queue and retry controls, and dead-letter queues around the producer pipeline.

The create-contract API adds package or rate-card selection, commits and credits, pricing overrides, subscriptions, scheduled charges, usage routing, threshold billing, provider configuration, and customer hierarchy. Only customer ID and contract start are unconditionally required at the top level; nested requirements depend on the selected structures.

The contract edit-history API exposes recorded changes made through the UI and contract-changing endpoints, grouping additions, updates, archives, and removals for contract audit work.

The enterprise commitment guide shows how prepaid balance access can be scheduled separately from invoicing, how product-tag overrides model negotiated discounts, and how edits differ from transitions. Its examples contain two documented inconsistencies, so the dedicated API schema remains the implementation authority.

The customer-commit API supports enterprise-wide and multi-contract spending pools, although Metronome recommends contract-level commits for standard cases. Its prepaid and postpaid paths have different invoice requirements, and lower numeric priorities consume first.

## Invoicing options

- Native Stripe invoicing can use Stripe Tax, dunning, and other Stripe product-suite capabilities.
- Marketplace invoicing automates metering and invoice creation for AWS, Azure, and GCP.
- ERP invoicing includes out-of-the-box and custom integrations for collection, book-closing, and revenue workflows.

The native Stripe integration routes invoices through customer or contract billing configurations, supports multiple Stripe accounts, and imports Stripe status changes by webhook. Existing finalized invoices are not replayed when a provider is added later, and Stripe representation limits can collapse line items or move true decimal quantities into descriptions.

## Stripe Dashboard app

- The Metronome Stripe App embeds revenue and usage summaries, linked-customer management, and contract creation in the Stripe Dashboard.
- Its contract wizard configures invoice terms, rate-card pricing and overrides, subscription quantities, product entitlement, and credits.
- The app is a management interface; invoice delivery still uses Metronome's native Stripe integration and the customer's Stripe billing-provider configuration.

## Notifications and webhooks

- Webhook categories span thresholds, contract and balance-object lifecycles, invoices, integration failures, marketplace disablement, and payment gating.
- Receivers should acknowledge quickly, process asynchronously, and deduplicate by notification ID because retries can continue for up to two days.
- Authenticity can be established by retrieving authoritative API data or verifying an HMAC-SHA256 signature over the request date and exact body bytes.

## Security principles

- Access follows least privilege, with explicit grants and field-level controls.
- Service-to-service and actor-to-system communication follows a zero-trust authentication model.
- Metronome states that engineers use daily minted credentials lasting 12 hours rather than long-lived credentials on developer machines.

## Reporting and data export

- Warehouse exports cover raw events, customers, invoices, contracts, pricing, packages, payments, alerts, and metadata.
- Finalized invoice rows, daily draft snapshots, and invoice-breakdown snapshots have distinct grains and update behavior.
- Exported columns may all appear nullable because of the export methodology, so warehouse types alone do not establish business optionality.

## Knowledge status

- Collected documentation pages: 225
- Ingested source summaries: 15
- Documentation pages pending ingest: 210

## Sources

- [[source-metronome-guides-get-started-home]] — documentation entry point and four pricing/packaging routes
- [[source-metronome-guides-get-started-developer-sdks]] — SDK setup and introductory event-to-invoice workflow
- [[source-metronome-guides-events-design-usage-events]] — usage-event design principles, cadence tradeoffs, and future metric flexibility
- [[source-metronome-guides-events-high-volume-ingestion]] — throughput, batching, observability, and recovery controls
- [[source-metronome-guides-get-started-stripe-marketplace-app]] — embedded Stripe Dashboard app and contract workflow
- [[source-metronome-guides-pricing-packaging-billing-model-guides-enterprise-commit]] — enterprise commitment schedules, discounts, lifecycle, and example cautions
- [[source-metronome-integrations-invoice-integrations-stripe]] — Stripe invoice routing, configuration, statuses, payment timing, and limits
- [[source-metronome-api-reference-credits-and-commits-create-a-commit]] — customer-level commit creation, invoicing conditions, targeting, and priority
- [[source-metronome-guides-invoices-overview]] — Stripe, marketplace, and ERP invoicing options
- [[source-metronome-guides-reporting-insights-data-export-database-reference]] — warehouse schema families, grains, and query cautions
- [[source-metronome-api-reference-contracts-create-a-contract]] — contract creation request families and conditional rules
- [[source-metronome-api-reference-invoices-preview-events]] — draft-invoice previews from proposed usage events
- [[source-metronome-api-reference-contracts-get-contract-edit-history]] — cross-channel contract edit history and change categories
- [[source-metronome-guides-platform-configuration-setup-webhooks]] — webhook categories, retry behavior, deduplication, and verification
- [[source-metronome-guides-platform-configuration-security-principles]] — least privilege, zero trust, and short-lived credentials

## Related

- [[metronome-index]] — provider catalog and coverage
- [[metronome-log]] — collection and future ingest history
- [[stripe-index]] — related Stripe catalog
- [[metronome-usage-based-billing]] — platform-specific billing concept
- [[metronome-invoicing]] — platform-specific invoicing options
- [[metronome-integrations]] — external-system integration boundaries and workflows
- [[metronome-credits-and-commits]] — commitment schedules, rollover, and contract lifecycle
- [[metronome-event-ingestion]] — usage-event contract and deduplication
- [[metronome-billable-metrics]] — event matching, aggregation, and grouping
- [[metronome-products-and-rate-cards]] — product presentation and effective pricing
- [[metronome-customers-and-contracts]] — customer aliases, commercial terms, and invoice activation
- [[metronome-reporting-and-analytics]] — warehouse exports, snapshot grains, and query cautions
- [[metronome-webhooks]] — notification delivery, reliability, and authenticity
- [[metronome-security-principles]] — platform access, authentication, and credential-lifetime principles
