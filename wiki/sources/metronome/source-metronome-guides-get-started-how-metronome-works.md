---
title: "How Metronome Works"
type: source
date_ingested: 2026-07-30
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/get-started/how-metronome-works"
raw_files:
  - "metronome/guides/get-started/how-metronome-works-2026-07-13.md"
tags: [metronome, usage-based-billing, usage-events, billable-metrics, products, rate-cards, contracts, invoicing]
---

## Overview

This architecture guide explains Metronome's event-to-invoice model by expanding the familiar **Price × Quantity = Charge** formula with a third element: the customer's **Commercial Model**. It assigns distinct responsibilities to usage events, billable metrics, products, rate cards, contracts, and invoices, then shows the order in which those objects contribute to billing. The page is a conceptual map rather than an API or lifecycle specification.

## Key takeaways

- **Quantity** starts with application-defined usage events. Billable metrics filter and aggregate those events into invoice quantities; one event can contribute to multiple metrics.
- **Price** is split between products and rate cards. Products identify what is sold and control invoice presentation, while rate cards define default per-unit prices for usage products over stated start and end dates.
- **Commercial terms** live in the customer contract. A contract connects the customer to pricing and can inherit base rates, override pricing, control product access, configure commitments, credits, or subscription fees, and set billing-cycle timing.
- Invoice calculation follows an explicit order: receive usage for the billing period, calculate quantities through billable metrics, apply contract pricing and any base-rate-card overrides, then generate the customer-facing invoice.
- Metronome describes three different timing surfaces: event-time alert and threshold evaluation, on-demand API-backed dashboard views, and invoice finalization and delivery at billing-cycle close. These surfaces should not be treated as the same invoice state.

## Object model and boundaries

### Quantity: usage events and billable metrics

Usage events are raw records of measurable customer activity, such as API calls, storage consumption, logins, or other interactions. The application chooses its event schema and sends events through Metronome's API; this page does not impose a predefined event structure.

Billable metrics sit downstream from events. They define what to measure by filtering events and how to measure it by aggregating them into billable units. The page states that one usage event can feed multiple billable metrics. It does not define metric-matching precedence, aggregation operations, deduplication behavior, or controls against unintentionally charging the same event through multiple products.

The guide presents the event/metric separation as an organizational boundary: engineering can keep emitting activity data while a business team changes the metering configuration. The page claims this can avoid application instrumentation changes, but it does not define which metric edits are allowed, whether changes affect earlier events, or when changed metrics take effect.

### Price: products and rate cards

Products represent the SKUs sold to customers and appear as invoice line items. The page names usage-based, fixed, and subscription charges as supported product types. Product configuration can control displayed quantities, rounding or conversion, product tags, and whether charges are consolidated or itemized by selected dimensions. Those controls affect customer-facing presentation rather than replacing the upstream event and metric definitions.

Rate cards define default pricing for usage products across the customer base. Each rate specifies what to charge per unit and carries start and end dates, enabling scheduled changes, promotions, or gradual price increases or decreases. The source does not define date-boundary inclusivity, rate versioning, or how fixed and subscription product prices are represented.

Metronome describes rate cards as the layer that separates reusable pricing from customer-specific commercial models. It says product additions and pricing updates automatically flow to commercial models, including subscriptions, consumption-based billing, and enterprise agreements. Contracts can also contain custom per-unit pricing or percentage discounts, but this page does not specify precedence among base rates, date-effective rate changes, and contract overrides, or whether existing customers can be grandfathered. The statement that many customers use one rate card is an observed practice in the guide, not a platform limit or guarantee.

### Commercial model: contracts

The contract binds a customer to the commercial arrangement and answers three questions:

1. **What** the customer agreed to pay for: products and rates.
2. **How** the customer agreed to pay: arrears, commitments, credits, or subscriptions.
3. **Where** charges should be sent: payment systems or marketplaces.

Contract configuration can inherit rate-card prices, apply percentage or per-unit overrides, enable or disable products, configure commitments, credits, or subscription fees, and determine invoice frequency and timing. This preserves a boundary between shared catalog pricing and terms negotiated for one customer.

The guide lists pay-as-you-go billing in arrears, prepaid credits, subscriptions with overage, enterprise minimum-spend commitments with discounts, and hybrids of those structures. After contract activation, Metronome says it begins generating usage statements according to the contract: credits draw down as usage occurs, pay-as-you-go customers are charged at period end, and commitments compare actual usage with committed amounts. Contract elements are described as programmable by API for self-serve, pricing-page, and enterprise quote-to-cash workflows, but this page supplies no request schema, validation rules, effective-time semantics, amendment behavior, or contract-state lifecycle.

### Invoice generation

The page gives the following processing order:

1. Receive usage-event data for the billing period.
2. Process the data through the applicable billable metrics to calculate quantities.
3. Apply pricing from the customer contract, including its overrides from the base rate card.
4. Generate an invoice that communicates the resulting charges.

It then distinguishes three timing contexts:

- **With incoming usage**, Metronome evaluates customer alerts and thresholds and can send webhooks when spending limits are reached or credits are depleted.
- **On demand through APIs**, Metronome can power current dashboards in end-user applications.
- **At billing-cycle close**, a customer invoice is finalized and sent to a selected downstream system, with month-end or quarter-end given as examples.

The first two contexts describe evaluation and visibility, not necessarily a finalized invoice. The guide does not identify the specific on-demand APIs, define freshness or latency, explain draft-invoice behavior, specify alert or webhook delivery guarantees, or document invoice finalization, delivery, payment collection, retries, and failure states. Payment systems and marketplaces are named as destinations in the contract model, but their configuration and responsibility boundaries are outside this page.

## Scope, cautions, and unknowns

> [!info] Conceptual scope
> This source provides object roles and their processing order. It states no numeric event, metric, product, rate-card, contract, API, alert, webhook, or invoice limits, and it is not an implementation schema.

The source contains no explicit warning callout or direct internal contradiction. Its claims that metering can evolve without code changes, pricing updates flow to all commercial models, contracts can support any commercial model, and one rate card can serve many models are broad architectural or promotional statements. They do not establish guarantees about mutation support, compatibility, rollout timing, grandfathering, override precedence, or operational availability.

The phrase "real-time with usage" is bounded here to alert and threshold evaluation when events arrive. "On-demand via API" is bounded to dashboard-oriented retrieval, and invoice finalization occurs separately at billing-cycle close. The page does not define whether all APIs refresh invoice calculations, what "real-time" latency means, or how these surfaces interact with draft and finalized invoice states.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-usage-based-billing]], [[metronome-event-ingestion]], [[metronome-billable-metrics]], [[metronome-products-and-rate-cards]], [[metronome-customers-and-contracts]], [[metronome-credits-and-commits]], [[metronome-invoicing]], [[metronome-webhooks]], [[metronome-integrations]]
- Related sources: [[source-metronome-guides-get-started-developer-sdks]], [[source-metronome-guides-implement-metronome-core-concepts-create-billable-metrics]], [[source-metronome-guides-get-started-metronome-dashboard-quickstart]], [[source-metronome-guides-invoices-overview]]

## Raw Sources

- [[raw/metronome/guides/get-started/how-metronome-works-2026-07-13|2026-07-13 snapshot — cross-object usage-to-invoice architecture]]
