---
title: "Metronome"
type: company
tags: [metronome, stripe, usage-based-billing]
source_count: 30
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
- The bearer-authenticated `POST /v1/ingest` schema accepts one to 100 events. Each requires a nonempty transaction ID, customer ID, event type, and RFC 3339 timestamp; transaction IDs are capped at 128 characters.
- Event design starts from billing and operational requirements, follows the data and cadence available in the source system, and retains contextual properties for future reporting or pricing changes.
- Billable metrics filter and aggregate events; products and rate cards turn those measurements into prices.
- Customer contracts apply the rate card and produce draft invoices that update with usage.
- The Preview Events API can calculate draft invoices from proposed usage before processing, using either replacement or merged historical-usage semantics.
- High-volume ingestion supports batches of 100 events, with documented infrastructure capacity up to 110,000 events per second and a default 5,000-events-per-second limit. Metronome recommends event sampling, queue and retry controls, and dead-letter queues around the producer pipeline.

The ingest endpoint reference separately advertises support for 100,000 events per second and a 34-day historical and deduplication window. It documents only a `200 Success` response without per-event results or errors, so partial-batch, retry, duplicate-response, and exact cutoff semantics remain unspecified.

The create-contract API adds package or rate-card selection, commits and credits, pricing overrides, subscriptions, scheduled charges, usage routing, threshold billing, provider configuration, and customer hierarchy. Only customer ID and contract start are unconditionally required at the top level; nested requirements depend on the selected structures.

Customer creation requires a name and can attach up to 2,000 ingest aliases plus billing-provider or revenue-system configuration. The page recommends provisioning the downstream payment or ERP customer first and then selecting the intended customer configuration on the contract. Its narrative returns `customer_id`, while the schema returns `data.id`, and the documented 409 conflict does not identify which request field supplies the conflicting customer ID.

The contract edit-history API exposes recorded changes made through the UI and contract-changing endpoints, grouping additions, updates, archives, and removals for contract audit work.

The legacy `POST /v1/contracts/amend` endpoint can add commits, credits, rate overrides, scheduled charges, and configuration-gated commercial fields from an inclusive effective time. Metronome directs new clients to `editContract` and removes amendment access after Contract editing is enabled. The legacy schema leaves omission, array mutation, backdating, invoice-state, atomicity, and response-ID semantics unspecified.

Metronome list endpoints use cursor pagination with `limit` and `next_page`. Clients continue until `next_page` is null; the reference recommends 50 records for bulk retrieval and caps a page at 100, but does not state cursor lifetime or result-order guarantees.

Metronome's API-wide status convention classifies `2xx`, `4xx`, and `5xx` responses, uses a JSON `message` envelope for every documented `4XX` error, and distinguishes organization-wide from per-customer rate limits through `X-Metronome-Rate-Limit-Type`. The reference does not publish numeric limits, reset headers, a backoff schedule, or exact partial-creation recovery semantics.

Metronome uses four distinct idempotency mechanisms: event `transaction_id` values, customer ingest aliases, supported resource `uniqueness_key` fields, and POST `Idempotency-Key` headers. Their lifetimes and conflict behavior differ; notably, header results persist for at least 24 hours and can cache HTTP 500 errors, so clients must investigate system state rather than assume that changing a key is always safe.

The enterprise commitment guide shows how prepaid balance access can be scheduled separately from invoicing, how product-tag overrides model negotiated discounts, and how edits differ from transitions. Its examples contain two documented inconsistencies, so the dedicated API schema remains the implementation authority.

The customer-commit API supports enterprise-wide and multi-contract spending pools, although Metronome recommends contract-level commits for standard cases. Its prepaid and postpaid paths have different invoice requirements, and lower numeric priorities consume first.

The dashboard quickstart provides a no-code first-invoice path through billable metrics, products, rate cards, customer contracts, Sandbox-only test events, and draft-invoice verification. It documents immutable billable-metric configuration, a 2,000-property event limit, and a 24-hour grace period before invoice finalization.

Billable metrics can be streaming queries using `COUNT`, `SUM`, `MAX`, or `LATEST`, or SQL queries for calculations such as distinct counts. Presentation and pricing dimensions must be defined in metric group keys before downstream use; high-cardinality keys can increase API latency. New streaming metrics match later events by default, although Metronome can perform an undocumented representative-assisted reflow over retained raw events.

The credits-and-commits guide adds recurring grant ledgers, priority and line-item drawdown, renewal-transition behavior, and separately configurable access and invoice schedules. Its worked payloads contain amount, syntax, date, and rollover-fraction inconsistencies, so the dedicated API references remain the implementation authority.

The targeted commit-edit API changes one existing contract- or customer-level commit, including schedule items, applicability, invoicing contract, rate type, priority, and hierarchy access. Draft invoices reflect changes immediately, while finalized and voided invoice associations constrain schedule updates and removals.

Prepaid balance thresholds can automatically restore contract value in fiat or a custom pricing unit. The flow supports Stripe or an external payment gate, immediately reevaluates changed configurations, and disables auto recharge after a failed gated payment until the merchant re-enables it. The guide leaves threshold equality and discount-fraction semantics ambiguous.

## Invoicing options

- Native Stripe invoicing can use Stripe Tax, dunning, and other Stripe product-suite capabilities.
- Marketplace invoicing automates metering and invoice creation for AWS, Azure, and GCP.
- ERP invoicing includes out-of-the-box and custom integrations for collection, book-closing, and revenue workflows.

The native Stripe integration routes invoices through customer or contract billing configurations, supports multiple Stripe accounts, and imports Stripe status changes by webhook. Existing finalized invoices are not replayed when a provider is added later, and Stripe representation limits can collapse line items or move true decimal quantities into descriptions.

Existing contracts can schedule invoice delivery changes among Stripe, NetSuite, and AWS, Azure, or GCP Marketplace. Marketplace-involved transitions begin next period and require threshold billing to be removed; current-period Stripe or NetSuite corrections can reroute only draft invoices. The provider-selection timing text and both request examples contain documentation defects preserved in the source summary.

Stripe Tax can calculate tax when Stripe finalizes a Metronome-created invoice. The setup depends on linked customers with addresses, Stripe product tax codes, and a Metronome `stripe_product_id` mapping; threshold and payment-gated flows require explicit API tax configuration.

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
- Customer API requests use dashboard-created bearer tokens. Tokens inherit the creating user's permissions by default, can be scoped by access level, environment, or endpoint through a Metronome representative, and cannot be viewed in full after creation.

The API-authentication page does not state an expiry duration for customer bearer tokens; the 12-hour lifetime above applies only to Metronome engineer credentials.

## Reporting and data export

- Warehouse exports cover raw events, customers, invoices, contracts, pricing, packages, payments, alerts, and metadata.
- Finalized invoice rows, daily draft snapshots, and invoice-breakdown snapshots have distinct grains and update behavior.
- Exported columns may all appear nullable because of the export methodology, so warehouse types alone do not establish business optionality.
- One export destination spans Production and Sandbox. Selected tables transfer every two hours with four-hour average freshness, while others transfer every 24 hours with 24-hour average freshness.
- Object-storage delivery is append-only and at-least-once, so consumers must resolve repeated primary keys using the most recent row.

## Knowledge status

- Collected documentation pages: 225
- Ingested source summaries: 30
- Documentation pages pending ingest: 195

## Sources

- [[source-metronome-guides-get-started-home]] — documentation entry point and four pricing/packaging routes
- [[source-metronome-guides-get-started-developer-sdks]] — SDK setup and introductory event-to-invoice workflow
- [[source-metronome-guides-events-design-usage-events]] — usage-event design principles, cadence tradeoffs, and future metric flexibility
- [[source-metronome-guides-events-high-volume-ingestion]] — throughput, batching, observability, and recovery controls
- [[source-metronome-api-reference-usage-ingest-events]] — ingest endpoint schema, idempotency window, matching, response gaps, and advertised capacity
- [[source-metronome-guides-get-started-stripe-marketplace-app]] — embedded Stripe Dashboard app and contract workflow
- [[source-metronome-guides-get-started-metronome-dashboard-quickstart]] — dashboard first-invoice workflow and Sandbox testing boundary
- [[source-metronome-guides-pricing-packaging-billing-model-guides-enterprise-commit]] — enterprise commitment schedules, discounts, lifecycle, and example cautions
- [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-create-a-pre-paid-commit]] — free credits, prepaid and postpaid commits, recurring grants, and drawdown
- [[source-metronome-guides-customers-billing-optimize-customer-experience-prepaid-balance-thresholds]] — automatic recharge, custom-unit balances, payment gating, and failure recovery
- [[source-metronome-integrations-invoice-integrations-stripe]] — Stripe invoice routing, configuration, statuses, payment timing, and limits
- [[source-metronome-guides-customers-billing-manage-customers-schedule-billing-provider-change]] — scheduled Stripe, NetSuite, and marketplace transitions
- [[source-metronome-integrations-tax-integrations-stripe-tax]] — Stripe Tax responsibility, product mapping, finalization, and threshold configuration
- [[source-metronome-api-reference-credits-and-commits-create-a-commit]] — customer-level commit creation, invoicing conditions, targeting, and priority
- [[source-metronome-api-reference-credits-and-commits-edit-a-commit]] — targeted commit fields, schedule operations, invoice-state constraints, and schema boundaries
- [[source-metronome-guides-invoices-overview]] — Stripe, marketplace, and ERP invoicing options
- [[source-metronome-guides-reporting-insights-data-export-database-reference]] — warehouse schema families, grains, and query cautions
- [[source-metronome-guides-reporting-insights-data-export-overview]] — destination scope, delivery cadence, freshness, and object-storage semantics
- [[source-metronome-api-reference-contracts-create-a-contract]] — contract creation request families and conditional rules
- [[source-metronome-api-reference-invoices-preview-events]] — draft-invoice previews from proposed usage events
- [[source-metronome-api-reference-contracts-get-contract-edit-history]] — cross-channel contract edit history and change categories
- [[source-metronome-api-reference-pagination]] — list-endpoint cursor traversal, limit guidance, and undocumented cursor boundaries
- [[source-metronome-api-reference-status-codes]] — HTTP response categories, error envelope, rate-limit scopes, and recovery boundaries
- [[source-metronome-api-reference-idempotency]] — transaction IDs, aliases, uniqueness keys, request caching, and retry lifetimes
- [[source-metronome-guides-implement-metronome-core-concepts-create-billable-metrics]] — streaming and SQL metrics, group keys, assisted reflow, and matching tests
- [[source-metronome-api-reference-customers-create-a-customer]] — aliases, downstream configurations, provisioning sequence, and response caveats
- [[source-metronome-api-reference-contracts-amend-a-contract]] — retiring amendment lifecycle, nested mutation schema, and validation gaps
- [[source-metronome-guides-platform-configuration-setup-webhooks]] — webhook categories, retry behavior, deduplication, and verification
- [[source-metronome-guides-platform-configuration-security-principles]] — least privilege, zero trust, and short-lived credentials
- [[source-metronome-api-reference-authentication]] — customer bearer-token creation, SDK use, permissions, and archival

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
- [[metronome-api-idempotency]] — platform-specific retry keys, conflict behavior, retention, and cached errors
