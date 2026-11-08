---
title: "Stripe: How Usage-Based Billing Works"
type: source
date_ingested: 2026-11-08
original_format: webpage
canonical_url: https://docs.stripe.com/billing/subscriptions/usage-based/how-it-works
raw_files:
  - "stripe-billing-subscriptions-usage-based-how-it-works-2026-11-07.md"
  - "stripe-usage-based-billing-how-it-works-2025.md"
tags: [stripe, billing, usage-based, meters, subscriptions, pricing]
---

## Summary

This guide explains **basic usage-based billing with Stripe Billing Meters**: its four-part lifecycle and six core objects. The 2026-11-07 capture adds Stripe's recommendation to use Metronome for a new usage-based integration unless maintaining an existing Billing Meters integration, including when adding usage pricing to a flat-rate subscription. It is a captured product-selection recommendation, not a Meter API deprecation, mandatory migration, or account-eligibility determination. The 2026-05-05 capture described the basic Meter path without that Metronome recommendation.

> [!warning] Contradiction
> The earlier source summary called the Meter API the “new v2 approach,” and the linked concept called it the “current approach.” The November guide instead presents Billing Meters as the **basic** path and recommends Metronome for new integrations. These dated descriptions do not establish that Billing Meters stopped working or that any account is eligible for Metronome.

## Metronome versus basic Billing Meters

In Stripe's November comparison, the basic path sends meter events to Stripe and aggregates usage with Billing Meters for invoicing. Metronome is described as handling event ingestion, real-time metering and rating, and contract management, then passing finalized charges to Stripe for invoicing and payment collection. This describes the component boundary; no merchant invoice or payment outcome was observed.

The same capture attributes live usage and credit-balance visibility, real-time credit burndown, enterprise commits/minimum spend/ramps, and dimensional or composite pricing to Metronome. It says basic billing credits reconcile at invoice time and could be exceeded during a cycle. The page also documents **Meter Event Summaries** for a custom time period, updated asynchronously. Thus its absence-of-live-totals statement concerns real-time visibility, not a prohibition on querying a processed mid-cycle summary. The linked feature comparison is outside this pinned evidence, so these are the page's comparative claims rather than a complete feature matrix or account-specific verification.

## Key details

### Four-component basic lifecycle

1. **Ingestion** — send customer usage to Stripe as meter events.
2. **Product catalog** — create usage-based and recurring prices.
3. **Billing** — subscribe the customer to prices; the documented workflow invoices consumed usage.
4. **Monitoring** — threshold alerts and usage analytics.

The November text diagram connects customer action, meter event and aggregation, price rating, subscription, invoice, and Meter Event Summaries. It illustrates the architecture; it is not evidence of an executed ingest or invoice.

### Six core concepts

| Term | Definition |
| --- | --- |
| **Customer-configured Account or Customer** | Alternative billing identities: a customer-configured Accounts v2 `Account` or a Customers v1 `Customer`. This table does not make their API parameters interchangeable in every operation. |
| **Subscription** | Recurring relationship with customer and one or more prices; governs billing cycles and invoice generation. |
| **Price** | Product-linked configuration of amount and billing frequency, including usage-based charges. |
| **Meter** | Tracks reported usage and specifies an aggregation formula over a billing period. |
| **Meter event** | Reported usage with event name, customer identifier and numeric value; optional timestamp, unique idempotency identifier and segmentation dimensions. |
| **Meter Event Summary** | Aggregated usage for a chosen customer and custom time period; updates asynchronously as events process. |

## Related pages

- [[stripe-usage-based-billing]] — concept page
- [[stripe]] — company page

## Raw Sources

- [[stripe-billing-subscriptions-usage-based-how-it-works-2026-11-07]] — Stripe guide captured 2026-11-07 (74 lines)
- [[stripe-usage-based-billing-how-it-works-2025]] — Stripe guide captured 2026-05-05 (42 lines)
