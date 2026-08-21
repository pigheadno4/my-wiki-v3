---
title: "Metronome"
type: company
tags: [metronome, stripe, usage-based-billing]
source_count: 112
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

The retained `@metronome/sdk@3.10.0` GitHub baseline adds the exact Node/TypeScript client contract: built-in Web Fetch with no runtime dependencies, typed V1 and V2 resources, two default retries, one-minute per-attempt timeout, async pagination, raw-response access, and webhook verification. It supports Node 20+, browsers, Deno, Bun, edge runtimes, and related server environments but explicitly excludes React Native. The generated package proves client implementation, not account feature enablement or current REST behavior; its stale `api.md` Payments listing conflicts with the removed source resource and the `3.7.0` changelog. [[source-github-metronome-node]]

The `Metronome-Industries/ai` baseline adds Metronome-authored operating instructions for coding and customer-success agents: integration best practices, catalog and contract setup, PLG billing, CSM reviews, and Stripe usage-billing migration. It is workflow and example evidence rather than an SDK or API schema. Its preview-before-write controls and parallel-run migration process are useful, but exact endpoint, enum, numeric-property, and rate claims require canonical verification because the retained skills contain internal and cross-source conflicts. [[source-github-ai]]

The experimental `terraform-provider-metronome@0.1.0-alpha.3` baseline configures a Metronome Go client through base URL, bearer token, and webhook-secret settings, but registers no Terraform resources or data sources. It is not production-ready and cannot be treated as a Metronome infrastructure-management surface at this version. [[source-github-terraform-provider-metronome]]

- Python, Node.js, Ruby, and Go SDKs demonstrate a common event-to-invoice flow.
- Event ingestion uses transaction IDs for deduplication and can associate application identifiers with customers through ingest aliases.
- The bearer-authenticated `POST /v1/ingest` schema accepts one to 100 events. Each requires a nonempty transaction ID, customer ID, event type, and RFC 3339 timestamp; transaction IDs are capped at 128 characters.
- Event design starts from billing and operational requirements, follows the data and cadence available in the source system, and retains contextual properties for future reporting or pricing changes.
- Billable metrics filter and aggregate events; products and rate cards turn those measurements into prices.
- Customer contracts apply the rate card and produce draft invoices that update with usage.
- The architecture guide orders the full flow as usage events, billable-metric quantities, product and rate-card pricing, customer contract terms, and invoice generation. It distinguishes event-time alert evaluation and on-demand API views from cycle-close invoice finalization and downstream delivery.
- The Preview Events API simulates draft-invoice costs from proposed events without processing or billing them. `merge` includes existing billing-period usage, while `replace` ignores existing usage; calculation uses the customer's contract and can reflect tiers, commits and credits, free allotments, and multiple products. Multiple active contracts return separate preview invoices. The guide documents an 8 RPS per-client limit, excludes invoices with SQL billable metrics, and conflicts with the API reference on same-request duplicate transaction IDs.
- High-volume ingestion supports batches of 100 events, with documented infrastructure capacity up to 110,000 events per second and a default 5,000-events-per-second limit. Metronome recommends event sampling, queue and retry controls, and dead-letter queues around the producer pipeline.

The ingest endpoint reference separately advertises support for 100,000 events per second and a 34-day historical and deduplication window. It documents only a `200 Success` response without per-event results or errors, so partial-batch, retry, duplicate-response, and exact cutoff semantics remain unspecified.

The implementation guide adds producer recovery behavior: queue direct-ingest events, retry network and `5xx` failures until `200`, back off exponentially after continued `429` responses, and dead-letter other `4xx` payload failures. It recommends string-valued properties, deterministic heartbeat IDs with duplicate sends, configurable failure-rate tests, and asynchronous Metronome customer creation through ingest-alias matching.

The create-contract API adds package or rate-card selection, commits and credits, pricing overrides, subscriptions, scheduled charges, usage routing, threshold billing, provider configuration, and customer hierarchy. Only customer ID and contract start are unconditionally required at the top level; nested requirements depend on the selected structures.

The implementation workflow layers a worked prepaid commit, quarterly platform charge, monthly usage statements, and AWS Marketplace routing onto a rate card. It also documents usage-invoice consolidation, a beta current-period provider attachment that may differ from marketplace transition timing, tag-scoped discounts, and schedulable multi-contract usage filters.

Customer creation requires a name and can attach up to 2,000 ingest aliases plus billing-provider or revenue-system configuration. The page recommends provisioning the downstream payment or ERP customer first and then selecting the intended customer configuration on the contract. Its narrative returns `customer_id`, while the schema returns `data.id`, and the documented 409 conflict does not identify which request field supplies the conflicting customer ID.

The implementation guide adds that aliases can model enterprise sub-organizations and can retroactively associate earlier usage when attached later. A customer needs a contract before rating begins; customer-level provider configuration alone does not route billing, and its beta archival can immediately stop an active contract's destination.

The contract edit-history API exposes recorded changes made through the UI and contract-changing endpoints, grouping additions, updates, archives, and removals for contract audit work.

The legacy `POST /v1/contracts/amend` endpoint can add commits, credits, rate overrides, scheduled charges, and configuration-gated commercial fields from an inclusive effective time. Metronome directs new clients to `editContract` and removes amendment access after Contract editing is enabled. The legacy schema leaves omission, array mutation, backdating, invoice-state, atomicity, and response-ID semantics unspecified.

Metronome list endpoints use cursor pagination with `limit` and `next_page`. Clients continue until `next_page` is null; the reference recommends 50 records for bulk retrieval and caps a page at 100, but does not state cursor lifetime or result-order guarantees.

Metronome's API-wide status convention classifies `2xx`, `4xx`, and `5xx` responses, uses a JSON `message` envelope for every documented `4XX` error, and distinguishes organization-wide from per-customer rate limits through `X-Metronome-Rate-Limit-Type`. The reference does not publish numeric limits, reset headers, a backoff schedule, or exact partial-creation recovery semantics.

Metronome uses four distinct idempotency mechanisms: event `transaction_id` values, customer ingest aliases, supported resource `uniqueness_key` fields, and POST `Idempotency-Key` headers. Their lifetimes and conflict behavior differ; notably, header results persist for at least 24 hours and can cache HTTP 500 errors, so clients must investigate system state rather than assume that changing a key is always safe.

The enterprise commitment guide shows how prepaid balance access can be scheduled separately from invoicing, how product-tag overrides model negotiated discounts, and how edits differ from transitions. Its examples contain two documented inconsistencies, so the dedicated API schema remains the implementation authority.

The customer-commit API supports enterprise-wide and multi-contract spending pools, although Metronome recommends contract-level commits for standard cases. Its prepaid and postpaid paths have different invoice requirements, and lower numeric priorities consume first.

The dashboard quickstart provides a no-code first-invoice path through billable metrics, products, rate cards, customer contracts, Sandbox-only test events, and draft-invoice verification. It documents immutable billable-metric configuration, a 2,000-property event limit, and a 24-hour grace period before invoice finalization.

Billable metrics can be streaming queries using `COUNT`, `SUM`, `MAX`, or `LATEST`, or SQL queries for calculations such as distinct counts. Presentation and pricing dimensions must be defined in metric group keys before downstream use; high-cardinality keys can increase API latency. New streaming metrics match later events by default, although Metronome can perform an undocumented representative-assisted reflow over retained raw events.

The create-metric endpoint accepts one named metric using either SQL or mutually exclusive standard fields and returns one UUID. Its schema introduces unresolved contradictions around `UNIQUE`, aggregation-key requiredness, empty exclusion lists, and request-body requiredness, and documents no endpoint-specific errors, limits, or recovery behavior.

Products define charge mechanics and invoice presentation but not price ownership. Usage, composite, and subscription prices live on rate cards and can be modified on contracts; fixed-product prices live on contracts. Product edits are effective-dated and can be retroactive, while product type is immutable and requires replacement plus archival when wrong.

Rate cards centralize one-currency standard pricing, effective-dated aliases, scheduled rates, dimensional combinations, and tiers. The guide preserves inconsistencies between singular/plural add-rate paths and enum casing, plus an unresolved tension between “all contracts use rate cards” and the optional create-contract rate-card/package request family.

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

For Indian-card invoices, Metronome documents a Stripe-mandate flow in which the merchant confirms an on-session SetupIntent, waits for the Stripe mandate to become active, and stores its ID in a contract custom field mapped to Stripe `invoice.payment_settings.default_mandate`. Stripe owns mandate creation and lifecycle; Metronome attempts to attach the mapped mandate to invoices but exposes no mandate-management API. Customer action or mandate replacement can therefore remain necessary before payment or a later recharge succeeds.

## Stripe Dashboard app

- The Metronome Stripe App embeds revenue and usage summaries, linked-customer management, and contract creation in the Stripe Dashboard.
- Its contract wizard configures invoice terms, rate-card pricing and overrides, subscription quantities, product entitlement, and credits.
- The app is a management interface; invoice delivery still uses Metronome's native Stripe integration and the customer's Stripe billing-provider configuration.

## Notifications and webhooks

- Webhook categories span thresholds, contract and balance-object lifecycles, invoices, integration failures, marketplace disablement, and payment gating.
- Receivers should acknowledge quickly, process asynchronously, and deduplicate by notification ID because retries can continue for up to two days.
- Authenticity can be established by retrieving authoritative API data or verifying an HMAC-SHA256 signature over the request date and exact body bytes.
- Notifications divide into threshold, system, and offset families. System and offset notifications are stateless scheduled signals; threshold notifications are continuously evaluated, use `OK` and `IN_ALARM` as ongoing states, and have an `EVALUATING` condition before initial evaluation. Thresholds are evaluated at least every three minutes, with firing documented within five minutes after triggering usage is ingested.
- Offset notifications schedule a system-event signal before or after a known date using hour-through-year units. They are prospective rather than backfilled, and the payload timestamp remains the source event time rather than the offset fire time. Before-`commit.segment.start` offsets longer than a recurring commit's one-period child-generation horizon fire only when the future child is created.
- Spend-threshold billing attaches a charge trigger to contract spend and can payment-gate release of the resulting commit. Stripe collection can use an invoice or PaymentIntent; an external gateway instead consumes `payment_gate.external_initiate`, owns collection, and releases or cancels the commit with the workflow ID. The feature limits unpaid-revenue exposure but this guide does not establish application access blocking or a customer-wide hard cap.
- Customer controls use threshold alerts as merchant-consumed action signals. The examples create soft and hard limits with the same `spend_threshold_reached` type, support dimension filters tied to billable-metric group keys, expose a low-remaining-commit alert, and distinguish pre-drawdown usage spend from post-drawdown invoice total. Metronome evaluates and delivers the alert, while the merchant owns the customer UI, messaging, and access blocking; no invoice finalization, payment success, or automatic service-denial guarantee follows from an alarm.

## Security principles

- Access follows least privilege, with explicit grants and field-level controls.
- Service-to-service and actor-to-system communication follows a zero-trust authentication model.
- Metronome states that engineers use daily minted credentials lasting 12 hours rather than long-lived credentials on developer machines.
- Customer API requests use dashboard-created bearer tokens. Tokens inherit the creating user's permissions by default, can be scoped by access level, environment, or endpoint through a Metronome representative, and cannot be viewed in full after creation.

The API-authentication page does not state an expiry duration for customer bearer tokens; the 12-hour lifetime above applies only to Metronome engineer credentials.

Metronome's Postman guide imports the live OpenAPI specification, organizes requests by tags, and uses a collection-scoped bearer-token variable. Its customer request and response are illustrative rather than a complete endpoint schema, and the guide does not pin the OpenAPI version or define token lifecycle controls.

The API quickstart provides the first-connection sequence: create and securely copy a named token, install one of four SDKs, use `METRONOME_BEARER_TOKEN` or a supplied bearer token, and list customers even when the account has none. It does not define token lifecycle policy, SDK versions, general error behavior, or numeric limits.

## Subscription and PayGo lifecycle

- Subscription products carry recurring fees, with quantity-one list prices on rate cards and quantity, proration, collection direction, applicable rates, and credits applied through customer contracts.
- Subscription price changes reach inheriting contracts next period while a contract overwrite retains its price. Upgrades can prorate through renewal transitions; downgrades take effect next period.
- Most cancellations should end the contract, while a later restart creates a new contract. A hybrid subscription cancelled by moving its end date requires its recurring credit to end separately.
- The PayGo example combines usage products, one rate card, a customer contract, a plan-scoped product-tag override, and optional Stripe `send_invoice` delivery. It is illustrative and does not establish application entitlement or automatic card collection.
- Free trials can use either a capped, time-bounded credit with a balance alert or an uncapped time-bounded multiplier-0 override. Access enforcement and customer action remain merchant-owned.

The subscription guides use both `entitlement` and `entitled`, and one lifecycle operation labels a create-contract action while linking to edit-contract. Current API fields and endpoints should be verified.

## Architecture, access, and retrieval additions

- Billing-system planning spans value exchange, reliable usage data, commercial terms, billing-data distribution, and ongoing operations. The planning source is strategic guidance, not evidence of APIs, limits, SLAs, accounting compliance, or recovery guarantees.
- RBAC documents admin, member, and viewer roles, SSO claim mapping with default denial, full access for existing users when SSO is absent, and immutable role selection for newly created tokens. Its relationship to the authentication guide's default inherited permissions remains unresolved.
- `GET /v1/billable-metrics/{billable_metric_id}` retrieves one metric, including archived configuration, while the customer-scoped list endpoint supports cursor pagination, current-plan filtering, and archived inclusion. Their schemas retain `UNIQUE`, SQL discrimination, filter, grouping, and example contradictions.
- A manual Stripe-gated commit edits an existing contract, releases balance after payment success, voids both invoices and creates no commit after failure, and requires a new request for retry. Payment retry and webhook-delivery retry are distinct.
- Public-beta spend trackers sum selected contract spend over a reset period. The documented scope currently counts only commit purchases, filterable by manual versus threshold-recharge source and discounted status. A prepaid-threshold discount can reference a tracker cap and stop discounting new threshold commits until the next billing period; other internal pricing rules remain merchant-owned checks against the contract's returned `accumulated_spend`. The guide does not define usage-event tracking, alert delivery, or the payment states that enter or leave the total.
- Customer balance retrieval has two documented levels: `/getNetBalance` returns one filtered customer aggregate, while `listBalances` exposes individual credit and commit ledgers whose signed entries determine each remaining balance. Values may be fractional even in USD cents, and invoice-deduction timestamps use the usage service-period end rather than establishing invoice finalization or payment time.

## Reporting and data export

- Warehouse exports cover raw events, customers, invoices, contracts, pricing, packages, payments, alerts, and metadata.
- Finalized invoice rows, daily draft snapshots, and invoice-breakdown snapshots have distinct grains and update behavior.
- Exported columns may all appear nullable because of the export methodology, so warehouse types alone do not establish business optionality.
- One export destination spans Production and Sandbox. Selected tables transfer every two hours with four-hour average freshness, while others transfer every 24 hours with 24-hour average freshness.
- Object-storage delivery is append-only and at-least-once, so consumers must resolve repeated primary keys using the most recent row.

## Knowledge status

- Collected documentation pages: 225
- Ingested source summaries: 112
- Raw pages without source summaries: 119

## Sources

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

- [[source-github-ai]] - Metronome-authored agent workflows for integrations, catalog setup, CSM reviews, and Stripe migration
- [[changelog-github-ai]] - commit-qualified Metronome AI skills history
- [[source-github-metronome-node]] - exact `@metronome/sdk@3.10.0` server client, API surface, transport, webhook helper, and evidence boundaries
- [[changelog-github-metronome-node]] - package-qualified Node SDK release history and upgrade ledger
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
- [[source-metronome-api-reference-introduction]] — API directory, stated platform capabilities, SDK routes, and endpoint-domain map
- [[source-metronome-api-reference-postman]] — live OpenAPI import, collection bearer-token setup, and illustrative customer request
- [[source-metronome-api-reference-api-quickstart]] — token creation, four SDK installs, environment configuration, and connectivity test
- [[source-metronome-guides-implement-metronome-core-concepts-send-usage-events]] — producer event representation, queue/retry policy, heartbeat idempotence, and asynchronous customer matching
- [[source-metronome-guides-implement-metronome-core-concepts-create-products-contracts]] — product types, price ownership, creation, effective-dated edits, tags, and group keys
- [[source-metronome-guides-get-started-how-metronome-works]] — ordered event-to-invoice architecture, object responsibilities, and timing boundaries
- [[source-metronome-guides-implement-metronome-core-concepts-provision-contract]] — contract provisioning, charge consolidation, provider attachment, discounts, and usage filters
- [[source-metronome-guides-implement-metronome-core-concepts-create-manage-rate-cards]] — aliases, effective changes, dimensional pricing, and tiers
- [[source-metronome-api-reference-billable-metrics-create-a-billable-metric]] — singular create schema, filters, SQL exclusivity, contradictions, and UUID response
- [[source-metronome-guides-implement-metronome-core-concepts-provision-customer]] — alias hierarchy, retroactive association, rating prerequisite, and provider routing
- [[source-metronome-guides-pricing-packaging-subscription-subscription-overview]] — subscription products, rate-card prices, contracts, and credit scope
- [[source-metronome-guides-pricing-packaging-subscription-define-subscription-pricing]] — per-offering products, seat key, quantity-one prices, and multi-rate setup
- [[source-metronome-guides-pricing-packaging-subscription-manage-subscription-lifecycle]] — inherited pricing, trials, transitions, proration, and cancellation
- [[source-metronome-guides-platform-configuration-role-based-access-rbac]] — roles, SSO claims, default denial, and token role selection
- [[source-metronome-guides-pricing-packaging-billing-model-guides-pay-as-you-go]] — illustrative PayGo packaging, provisioning, overrides, and Stripe delivery
- [[source-metronome-guides-implement-metronome-planning-your-billing-architecture]] — five-lens billing architecture planning framework
- [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-manual-payment-gated-commits]] — Stripe-gated manual commit lifecycle and explicit retry boundary
- [[source-metronome-guides-pricing-packaging-billing-model-guides-create-a-trial]] — capped-credit and zero-multiplier trial patterns
- [[source-metronome-api-reference-billable-metrics-get-a-billable-metric]] — single-metric retrieval and archive visibility
- [[source-metronome-api-reference-billable-metrics-get-billable-metrics-for-a-customer]] — customer-scoped metric discovery, filters, and pagination
- [[source-metronome-guides-customers-billing-overview]] — navigation map for customer lifecycle, customer-facing billing controls, fraud and entitlement themes, and notifications
- [[source-metronome-guides-customers-billing-manage-customers-manage-product-access]] — product-access navigation through contract terms, usage- and payment-based entitlement status, lifecycle guides, trials, and notifications
- [[source-metronome-guides-customers-billing-set-up-notifications-create-and-manage-notifications]] — threshold, system, and offset notification behavior, delivery, scheduling, and states
- [[source-metronome-guides-customers-billing-optimize-customer-experience-india-e-mandates]] — Indian-card Stripe mandate setup, invoice mapping, action-required flow, and lifecycle responsibility
- [[source-metronome-guides-customers-billing-set-up-notifications-offset-notifications]] — relative-time policy, payload timestamp, prospective firing, UI/API setup, and recurring-commit timing caveat
- [[source-metronome-guides-customers-billing-manage-customers-spend-trackers]] — public-beta spend accumulation, commit-purchase scope, threshold-discount caps, retrieval, and merchant enforcement
- [[source-metronome-guides-customers-billing-optimize-customer-experience-set-customer-spend-control]] — contract spend thresholds, immediate updates, Stripe and external payment gates, and enforcement boundaries
- [[source-metronome-guides-customers-billing-optimize-customer-experience-preview-event-cost]] — pre-action cost simulation, contract pricing, preview modes, multi-contract responses, deduplication, and limits
- [[source-metronome-guides-customers-billing-optimize-customer-experience-customer-controls]] — merchant-configured spend, dimension, commit-balance, and invoice-total alerts with access-enforcement boundaries
- [[source-metronome-guides-customers-billing-optimize-customer-experience-get-remaining-balance]] — customer aggregate and per-balance ledger retrieval, signed arithmetic, precision, effective time, and manual adjustments
- [[source-metronome-guides-pricing-packaging-billing-model-guides-guides-home]] — navigation routes for pay-as-you-go, enterprise commits, usage subscriptions, and pre-paid credits
- [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-alerts]] — credit and commit threshold dimensions, custom-field scoping, and downstream action boundary
- [[source-metronome-guides-pricing-packaging-overview]] — pricing-and-packaging navigation across billing models, changes, credits, commits, and examples
- [[source-metronome-guides-platform-configuration-metronome-pricing-model]] — Metronome platform fees, consumption commitment, Events, Billings, and exported-row accounting
- [[source-metronome-guides-implement-metronome-core-concepts-billable-metrics-basic-filters]] — streaming metric filters, property existence, grouped counting, and API representation
- [[source-metronome-guides-pricing-packaging-make-pricing-changes-use-currency-custompricingunits]] — supported currencies, API denomination, custom-unit pricing, balance drawdown, and invoice conversion
- [[source-metronome-guides-events-send-usage-events]] — usage-event fields, direct-ingest retries, heartbeat IDs, customer attribution, and 34-day duplicate suppression
- [[source-metronome-guides-invoices-invoice-optimization-issue-credit-memos]] — future credits, external A/R credit memos, invoice-state corrections, re-billing, and refunds
- [[source-metronome-api-reference-security-get-services]] — authenticated service registry, directional IP usage labels, and allowlisting boundaries
- [[source-metronome-api-reference-alerts-reset-a-threshold-notification]] — threshold-state reset, asynchronous reassessment, empty success response, and retry unknowns
- [[source-metronome-integrations-platform-integrations-workato-connector]] — SDK-like Workato connector setup, API-token connection, example workflows, and per-environment boundary
- [[source-metronome-guides-platform-configuration-audit-logs]] — action attribution, outcomes, request correlation, and audit-evidence limitations
- [[source-metronome-guides-platform-configuration-single-sign-on-sso]] — SAML 2.0 team login, identity-provider access control, retained users, and password cutover
- [[source-metronome-guides-platform-configuration-allowlist]] — service-registry polling, allowlist automation, stale-rule risk, and layered-security boundaries
- [[source-metronome-integrations-platform-integrations-segment]] — Segment destination setup, event-field mappings, transaction-ID default, and conditional actions
- [[source-metronome-integrations-tax-integrations-avalara]] — Avalara through Stripe's third-party tax-app framework, mappings, draft setting, and native Stripe Tax boundary
- [[source-metronome-integrations-tax-integrations-anrok]] — Anrok calculation and compliance modes, Stripe invoice configuration, and provider boundaries
- [[source-metronome-guides-invoices-invoice-optimization-import-existing-invoices]] — contract migration, historical invoice periods, balance effects, preview, and reporting breakdowns
- [[source-metronome-guides-implement-metronome-core-concepts-billable-metrics-sql-editor]] — SQL metric query surface, output fallback, breakdown granularity, and scheduled swaps
- [[source-metronome-guides-implement-metronome-production-checklist]] — go-live checks across ingestion, pricing, provisioning, invoicing, security, webhooks, and exports
- [[source-metronome-plans-shared-endpoints-notifications]] — shared Plan and Contract alert routes, entity-specific parameter boundaries, and Plan alert types
- [[source-metronome-plans-shared-endpoints-invoices]] — shared Plan and Contract invoice operations, adjustments, sub-line items, and tier detail
- [[source-metronome-guides-reporting-insights-financial-reporting-reconcile-data]] — Data Export and API reconciliation patterns across Metronome, Salesforce, and Stripe
- [[source-metronome-api-reference-invoices-void-an-invoice]] — invoice void endpoint, requiredness boundaries, intended uses, and downstream unknowns
- [[source-metronome-guides-reporting-insights-financial-reporting-revenue-recognition]] — revenue-reporting categories, invoice and ledger query model, and accounting ownership boundary
- [[source-metronome-api-reference-notifications-list-system-notification-event-types]] — lifecycle event-type discovery, response taxonomy, and webhook-publication status
- [[source-metronome-api-reference-invoices-regenerate-an-invoice]] — invoice regeneration, recalculation and distribution wording, and identity contradiction
- [[source-metronome-integrations-invoice-integrations-custom-invoice-integrations]] — finalized-invoice export flow, QuickBooks transformation, and integration ownership boundaries
- [[source-metronome-api-reference-invoices-add-a-one-time-charge]] — deprecated Plans one-time charge contract, product restriction, and empty response boundary
- [[source-metronome-guides-reporting-insights-in-app-reporting]] — report generation, beta dashboards, ARR calculations, defaults, and freshness limits
- [[source-metronome-api-reference-custom-fields]] — custom-field purpose, supported object examples, persistence, uniqueness, and invoice-line propagation

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
- [[metronome-packages-and-aliases]] — package cohorts, effective-dated alias transitions, and migration boundaries
- [[metronome-customers-and-contracts]] — customer aliases, commercial terms, and invoice activation
- [[metronome-reporting-and-analytics]] — warehouse exports, snapshot grains, and query cautions
- [[metronome-webhooks]] — notification delivery, reliability, and authenticity
- [[metronome-security-principles]] — platform access, authentication, and credential-lifetime principles
- [[metronome-api-idempotency]] — platform-specific retry keys, conflict behavior, retention, and cached errors
- [[metronome-subscriptions]] — subscription pricing, contract configuration, transitions, and cancellation
- [[metronome-alerts-and-notifications]] — alert-definition semantics and merchant-action boundary
- [[metronome-currencies-and-custom-pricing-units]] — Metronome-specific fiat denomination, custom-unit rate setup, matching-balance drawdown, and invoice conversion
- [[metronome-custom-fields]] — platform-object metadata, external-system mappings, uniqueness, and persistence
