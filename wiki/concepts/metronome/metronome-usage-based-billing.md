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

The documentation landing page routes readers toward billing architecture planning and getting-started material, then highlights contracts, invoicing, and revenue recognition as adjacent areas. It does not establish the detailed sequence connecting those areas.

The credits-and-commits guide supplies one implementation path for hybrid subscription and usage models: recurring credits provide free periodic usage, recurring commits provide paid periodic usage, and each period receives a distinct balance ledger. Uncovered usage remains available for overage billing.

## Pre-processing validation

The Preview Events API provides a concrete validation step between usage-event design and invoice generation. It can calculate draft invoices from proposed events using the customer's current contract, either replacing historical usage for the calculation or merging with it. The preview does not support contracts with SQL billable metrics.

## Platform context

This page describes the Metronome-specific implementation surface. For the cross-provider recurring model, see [[recurring-payments]]. Related platform context is available through [[metronome]] and [[stripe]].

## Open questions

- How usage events are represented, validated, and aggregated.
- Which product, rate-card, customer, and contract objects participate in each pricing pattern.
- How invoice generation and revenue-recognition outputs differ across the four patterns.
- Which capabilities are native to Metronome versus coordinated with Stripe products.

These questions require dedicated sources and are not answered by the landing page.

## Sources

- [[source-metronome-guides-get-started-home]] — documentation landing page and pricing-model routes
- [[source-metronome-api-reference-invoices-preview-events]] — pre-processing draft-invoice calculation from proposed usage events
- [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-create-a-pre-paid-commit]] — recurring free or paid grants, balances, and overage boundary
