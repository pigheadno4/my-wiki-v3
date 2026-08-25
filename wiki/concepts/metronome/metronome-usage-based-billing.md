---
title: "Metronome Usage-Based Billing"
type: concept
category: technology
tags: [metronome, usage-based-billing, pricing, invoicing]
---

## Definition

Metronome's documentation presents usage-oriented billing as a pricing and packaging capability that can support charging in arrears, enterprise commitments, recurring subscriptions with usage components, and prepaid credit models. The initial landing-page source identifies these patterns but does not define their implementation APIs or data model.

## Pricing and packaging patterns

## Metronome commercial pricing boundary

Metronome's own customer pricing is distinct from the prices merchants configure for their end users. It combines an annual platform fee, excluded from consumption charge categories, with consumption-based charges that begin at production go-live. An order-form Consumption Commitment is a prepaid, non-refundable minimum against those platform-usage charges; unused value expires at the end of the applicable service term. This commercial commitment must not be treated as a Metronome credit or commit object configured for a merchant's customer. [[source-metronome-guides-platform-configuration-metronome-pricing-model]]

| Pattern | Landing-page description |
| --- | --- |
| Pay as you go | Charge customers in arrears for what they use. |
| Enterprise commits | Support prepaid or postpaid commitments, negotiated discounts, one-time charges, and renewals. |
| Subscriptions with usage | Combine recurring revenue with usage-based components. |
| Prepaid credits | Let customers buy credits upfront, with auto-recharge or gated access after depletion. |

## Adjacent billing domains

The documentation landing page routes readers toward billing architecture planning and getting-started material, then highlights contracts, invoicing, and revenue recognition as adjacent areas. The architecture guide establishes the main sequence: applications send usage events; billable metrics calculate quantities; products and rate cards define what is sold and its default price; contracts add customer-specific commercial terms; and invoices apply those inputs. It separates event-time alert evaluation and on-demand API views from invoice finalization at billing-cycle close.

The credits-and-commits guide supplies one implementation path for hybrid subscription and usage models: recurring credits provide free periodic usage, recurring commits provide paid periodic usage, and each period receives a distinct balance ledger. Uncovered usage remains available for overage billing.

The billable-metrics guide fills in the metering layer: usage events are filtered and aggregated into invoice-line quantities, products control invoice presentation, rate cards attach list prices, and contracts can override those rates. Streaming metrics provide `COUNT`, `SUM`, `MAX`, and `LATEST` across the UI, API, Plans, and Contracts, while SQL metrics support calculations such as distinct counts.


The invoice guide adds the usage-invoice lifecycle: a contract's usage-statement schedule sets cadence, the draft invoice updates as usage arrives, and a configurable grace period that defaults to 24 hours accepts late usage and corrections before finalization. Once `FINALIZED`, the invoice is immutable within Metronome even if more usage is reported. Distribution and collection follow contract billing configuration, but the guide does not establish downstream provider acceptance, customer delivery, payment success, settlement, tax completion, or accounting posting. [[source-metronome-guides-implement-metronome-core-concepts-how-invoicing-works]]

For non-monotonically increasing metrics that typically use `LATEST`, Metronome bills the incremental change between consecutive reporting windows, including a negative quantity and customer credit when the reported value decreases. The same guide distinguishes this billed quantity from usage-query output: invoice breakdowns show each window's incremental quantity and cost, while usage endpoints show the absolute latest value in each requested window. With no breakdown, the usage example returns the latest value across the full queried period. Exact endpoint schemas, pagination, ordering, freshness, and consistency remain with the dedicated API references.


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
