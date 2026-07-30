---
title: "Metronome Usage-Based Billing"
type: concept
category: technology
tags: [metronome, usage-based-billing, pricing, invoicing]
---

## Definition

Metronome's documentation presents usage-oriented billing as a pricing and packaging capability that can support charging in arrears, enterprise commitments, recurring subscriptions with usage components, and prepaid credit models. The initial landing-page source identifies these patterns but does not define their implementation APIs or data model.

## Pricing and packaging patterns

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

## Pre-processing validation

The Preview Events API provides a concrete validation step between usage-event design and invoice generation. It can calculate draft invoices from proposed events using the customer's current contract, either replacing historical usage for the calculation or merging with it. The preview does not support contracts with SQL billable metrics.

## Planning, PayGo, and trial patterns

The billing-architecture guide frames implementation as five connected decisions: define the value exchange, build reliable usage data, choose customer-aligned commercial terms, distribute billing data to its consumers, and operate the system with monitoring and correction paths. This is a planning checklist, not evidence of particular schemas, limits, availability, or service guarantees.

A PayGo example packages arrears-oriented self-service usage through products and a rate card, with an optional recurring fixed fee and optional Stripe invoice route. Its AutoSales prices and customer-acquisition framing are illustrative rather than platform guarantees.

Metronome documents two free-trial packaging patterns: a time-bounded credit grant with a balance alert, and a time-bounded multiplier-0 override for uncapped free usage. In both patterns, usage returns to list-price arrears after the grant or override ends; merchant systems remain responsible for access enforcement and customer action.

## Platform context

This page describes the Metronome-specific implementation surface. For the cross-provider recurring model, see [[recurring-payments]]. Related platform context is available through [[metronome]] and [[stripe]].

## Open questions

- Which event schemas and validation rules apply before billable-metric matching.
- How customer and contract configuration varies across the four pricing patterns.
- How invoice generation and revenue-recognition outputs differ across the four patterns.
- Which capabilities are native to Metronome versus coordinated with Stripe products.

These remaining questions require dedicated sources and are not fully answered by the landing page or the currently ingested implementation guides.

## Sources

- [[source-metronome-guides-get-started-home]] — documentation landing page and pricing-model routes
- [[source-metronome-guides-implement-metronome-core-concepts-create-billable-metrics]] — event aggregation, product and rate-card roles, contract overrides, and metric testing
- [[source-metronome-api-reference-invoices-preview-events]] — pre-processing draft-invoice calculation from proposed usage events
- [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-create-a-pre-paid-commit]] — recurring free or paid grants, balances, and overage boundary
- [[source-metronome-guides-get-started-how-metronome-works]] — ordered event-to-invoice architecture and timing boundaries
- [[source-metronome-guides-implement-metronome-planning-your-billing-architecture]] — five-lens billing-system planning checklist
- [[source-metronome-guides-pricing-packaging-billing-model-guides-pay-as-you-go]] — illustrative PayGo packaging and provisioning path
- [[source-metronome-guides-pricing-packaging-billing-model-guides-create-a-trial]] — capped-credit and zero-multiplier trial patterns
