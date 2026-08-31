---
title: "Metronome Usage-Based Billing"
type: concept
category: technology
tags: [metronome, usage-based-billing, pricing, invoicing]
---

## Definition

Metronome's documentation presents usage-oriented billing as a pricing and packaging capability that can support charging in arrears, enterprise commitments, recurring subscriptions with usage components, and prepaid credit models. The initial landing-page source identifies these patterns but does not define their implementation APIs or data model.

## Pricing and packaging patterns

[[metronome-token-billing]] is a distinct private-preview managed token-cost-plus-markup workflow. It can create managed AI billing objects from configured markups; non-USD fiat is unsupported, while a USD-to-custom-unit conversion supports custom credit-denominated pricing. Newly released models are added at the default markup, but provider-price refresh for existing models is only described as coming soon. The guide does not establish catalog-update timing, removal or fallback behavior, precision or rounding, provider-cost verification, margin guarantees, reconciliation, or endpoint recovery semantics. [[source-metronome-guides-pricing-packaging-billing-model-guides-token-billing]]

Metronome documents a configured zero-overage usage-pricing pattern: the real usage price applies only while an eligible commit is being consumed, then the product falls back to a zero list rate after exhaustion instead of ordinary nonzero overage pricing. The merchant can place the commit price on the rate card or use a commit-scoped contract override. This pattern does not reject usage submission or enforce product access; merchant systems still own gating and restoration, and the worked configuration does not establish a platform default or a guarantee for other products, balances, events, or configurations.

## Metronome commercial pricing boundary

Metronome's own customer pricing is distinct from the prices merchants configure for their end users. It combines an annual platform fee, excluded from consumption charge categories, with consumption-based charges that begin at production go-live. An order-form Consumption Commitment is a prepaid, non-refundable minimum against those platform-usage charges; unused value expires at the end of the applicable service term. This commercial commitment must not be treated as a Metronome credit or commit object configured for a merchant's customer. [[source-metronome-guides-platform-configuration-metronome-pricing-model]]

| Pattern | Landing-page description |
| --- | --- |
| Pay as you go | Charge customers in arrears for what they use. |
| Enterprise commits | Support prepaid or postpaid commitments, negotiated discounts, one-time charges, and renewals. |
| Subscriptions with usage | Combine recurring revenue with usage-based components. |
| Prepaid credits | Let customers buy credits upfront, with auto-recharge or gated access after depletion. |

## Adjacent billing domains

Metronome's product-access overview says entitlement status is tracked in real time based on usage and payment and tied to contract-defined customer access across packaging models. The navigation page supplies no evaluation algorithm, payment-state authority, latency, consistency, enforcement, or recovery contract; those questions require dedicated billing, contract, notification, and integration sources. [[source-metronome-guides-customers-billing-manage-customers-manage-product-access]]

The documentation landing page routes readers toward billing architecture planning and getting-started material, then highlights contracts, invoicing, and revenue recognition as adjacent areas. The architecture guide establishes the main sequence: applications send usage events; billable metrics calculate quantities; products and rate cards define what is sold and its default price; contracts add customer-specific commercial terms; and invoices apply those inputs. It separates event-time alert evaluation and on-demand API views from invoice finalization at billing-cycle close.

The credits-and-commits guide supplies one implementation path for hybrid subscription and usage models: recurring credits provide free periodic usage, recurring commits provide paid periodic usage, and each period receives a distinct balance ledger. Uncovered usage remains available for overage billing.

The billable-metrics guide fills in the metering layer: usage events are filtered and aggregated into invoice-line quantities, products control invoice presentation, rate cards attach list prices, and contracts can override those rates. Streaming metrics provide `COUNT`, `SUM`, `MAX`, and `LATEST` across the UI, API, Plans, and Contracts, while SQL metrics support calculations such as distinct counts.


The invoice guide adds the usage-invoice lifecycle: a contract's usage-statement schedule sets cadence, the draft invoice updates as usage arrives, and a configurable grace period that defaults to 24 hours accepts late usage and corrections before finalization. Once `FINALIZED`, the invoice is immutable within Metronome even if more usage is reported. Distribution and collection follow contract billing configuration, but the guide does not establish downstream provider acceptance, customer delivery, payment success, settlement, tax completion, or accounting posting. [[source-metronome-guides-implement-metronome-core-concepts-how-invoicing-works]]

For non-monotonically increasing metrics that typically use `LATEST`, Metronome bills the incremental change between consecutive reporting windows, including a negative quantity and customer credit when the reported value decreases. The same guide distinguishes this billed quantity from usage-query output: invoice breakdowns show each window's incremental quantity and cost, while usage endpoints show the absolute latest value in each requested window. With no breakdown, the usage example returns the latest value across the full queried period. Exact endpoint schemas, pagination, ordering, freshness, and consistency remain with the dedicated API references.

The dedicated invoice-breakdown read turns customer invoice data into hourly or daily windows whose line items carry quantities and costs for the specific period. Required timestamp bounds select windows by their own start and end, and optional filtering can remove zero-quantity line items. The endpoint says late usage after invoice finalization is reflected in breakdowns, but it does not define aggregation-specific quantity calculation, event attribution, baselines, correction cutoffs, or whether invoice totals change; retain the separate `LATEST`-metric guide as authority for incremental-versus-absolute quantity semantics. [[source-metronome-api-reference-invoices-list-invoice-breakdowns]]

## Pre-processing validation

The Preview Events API provides a concrete validation step between usage-event design and invoice generation. It can calculate draft invoices from proposed events using the customer's current contract, either replacing historical usage for the calculation or merging with it. The preview does not support contracts with SQL billable metrics.

The cost-preview guide expands the validation use case: the simulation can model tier transitions, commit and credit coverage versus overage, free allotments, and several products using the customer's contract. Merge mode estimates incremental cost against existing billing-period usage, while replace mode tests only the proposed usage. Customers with several active contracts receive separate preview invoice calculations.

Preview does not process or bill the events and is not positioned as per-event real-time validation; the documented limit is 8 RPS per client. The source does not define configuration-snapshot consistency, event-to-contract routing, pricing precedence, balance timing, or compatibility with all contract features, and SQL-based billable metrics are excluded.

## Planning, PayGo, and trial patterns

The billing-architecture guide frames implementation as five connected decisions: define the value exchange, build reliable usage data, choose customer-aligned commercial terms, distribute billing data to its consumers, and operate the system with monitoring and correction paths. This is a planning checklist, not evidence of particular schemas, limits, availability, or service guarantees.

A PayGo example packages arrears-oriented self-service usage through products and a rate card, with an optional recurring fixed fee and optional Stripe invoice route. Its AutoSales prices and customer-acquisition framing are illustrative rather than platform guarantees.

Metronome documents two free-trial packaging patterns: a time-bounded credit grant with a balance alert, and a time-bounded multiplier-0 override for uncapped free usage. In both patterns, usage returns to list-price arrears after the grant or override ends; merchant systems remain responsible for access enforcement and customer action.

The `Metronome-Industries/ai` repository adds an agent-oriented operating layer across these patterns. Its Stripe migration playbook recommends discovery, concept mapping, at least one complete parallel billing cycle, invoice-parity checks, remaining-credit migration, billing-boundary cutover, and rollback planning. These are workflow recommendations at one exact commit, not proof of API shape or universally safe cutover behavior. [[source-github-ai]]

## Platform context

This page describes the Metronome-specific implementation surface. For the cross-provider recurring model, see [[recurring-payments]]. Related platform context is available through [[metronome]] and [[stripe]].

## Open questions

- Which event schemas and validation rules apply before billable-metric matching.
- How customer and contract configuration varies across the four pricing patterns.
- How invoice generation and revenue-recognition outputs differ across the four patterns.
- Which capabilities are native to Metronome versus coordinated with Stripe products.

These remaining questions require dedicated sources and are not fully answered by the landing page or the currently ingested implementation guides.

## Sources

- [[source-metronome-api-reference-usage-get-usage-data-with-paginated-groupings]] - customer and billable-metric usage aggregates by requested windows and exact simple or compound metric groups, with filter, pagination, response-placement, `LATEST` reconciliation, and freshness boundaries

- [[source-metronome-api-reference-invoices-list-invoice-breakdowns]] - customer invoice time windows, required interval bounds, temporal and zero-quantity filters, late-usage updates, and aggregation-semantics boundary
- [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-guarantee-zero-overages]] - configured commit-only real pricing with zero-list-rate fallback after exhaustion, contrasted with ordinary nonzero overage pricing and separated from merchant-owned access enforcement
- [[source-metronome-guides-customers-billing-manage-customers-manage-product-access]] - contract-defined access and usage/payment-driven entitlement-status framing, qualified by navigation-page limits
- [[source-metronome-guides-get-started-api-quickstart]] — programmatic sandbox onboarding order from event schema and billing objects to a draft invoice, including the stale worked timestamp boundary

- [[source-github-ai]] - agent-oriented catalog, PLG, CSM, and Stripe usage-billing migration workflows
- [[source-metronome-guides-pricing-packaging-overview]] — navigation overview identifying pay-as-you-go, subscriptions, enterprise commits, hybrid approaches, pricing changes, and credits-and-commits as the documented pricing-and-packaging areas

- [[source-metronome-guides-get-started-home]] — documentation landing page and pricing-model routes
- [[source-metronome-guides-implement-metronome-core-concepts-create-billable-metrics]] — event aggregation, product and rate-card roles, contract overrides, and metric testing
- [[source-metronome-api-reference-invoices-preview-events]] — pre-processing draft-invoice calculation from proposed usage events
- [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-create-a-pre-paid-commit]] — recurring free or paid grants, balances, and overage boundary
- [[source-metronome-guides-get-started-how-metronome-works]] — ordered event-to-invoice architecture and timing boundaries
- [[source-metronome-guides-implement-metronome-planning-your-billing-architecture]] — five-lens billing-system planning checklist
- [[source-metronome-guides-pricing-packaging-billing-model-guides-pay-as-you-go]] — illustrative PayGo packaging and provisioning path
- [[source-metronome-guides-pricing-packaging-billing-model-guides-create-a-trial]] — capped-credit and zero-multiplier trial patterns
- [[source-metronome-guides-customers-billing-optimize-customer-experience-preview-event-cost]] — contract-aware pre-action pricing, merge/replace modes, multi-contract output, and simulation limits

- [[source-metronome-guides-implement-metronome-core-concepts-how-invoicing-works]] — contract-driven usage-invoice cadence, draft updates, configurable default grace period, finalized immutability, and downstream-outcome boundary

- [[source-metronome-guides-implement-metronome-core-concepts-non-monotonically-increasing-metrics]] - incremental billing for falling `LATEST` values, effective-window pricing, and invoice-breakdown versus absolute usage-query semantics
- [[source-metronome-api-reference-sdks]] — four-language SDK route from usage ingestion through metrics, customers, catalog pricing, contracts, and a draft invoice, qualified by stale August 2024 event payloads and a Go contract/grouping sequence that does not establish the narrated result
