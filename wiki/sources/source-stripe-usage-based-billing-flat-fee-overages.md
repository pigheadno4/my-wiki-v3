---
title: "Stripe: Set Up a Flat Fee and Overages Pricing Model"
type: source
date_ingested: 2026-11-08
canonical_url: https://docs.stripe.com/billing/subscriptions/usage-based-v1/use-cases/flat-fee-and-overages
original_format: webpage
raw_files:
  - "stripe-billing-subscriptions-usage-based-v1-use-cases-flat-fee-and-overages-2026-11-07.md"
  - "stripe-usage-based-billing-flat-fee-overages-2025.md"
tags: [stripe, billing, usage-based, meters, subscriptions, pricing, flat-fee, tiered]
---

## Summary

End-to-end Hypernian example for a flat fee plus overages: a sum meter, graduated metered price with the first 1,000 units included, separate $100 monthly licensed price, and both prices on one subscription. The captured guide creates a Billing Meter, links it through `recurring.meter`, and submits meter events, despite `usage-based-v1` in its URL. This is a documented example, not a verified invoice or payment run.

## Key Details

### Two-product approach

**Product 1 — metered usage (overages):**
- `billing_scheme: 'tiered'`, `tiers_mode: 'graduated'`, `usage_type: 'metered'`
- Tiers: first 1,000 units at zero, then an API `unit_amount_decimal=4` in USD minor units; the Dashboard example says 0.04 USD per unit above 1,000. Both captures also contain contradictory prose saying 0.04 USD per hundred units, so the intended unit basis needs confirmation before implementation.
- References the sum meter via `recurring.meter`. The November curl example creates it at `/v1/billing/meters` and reports events at `/v1/billing/meter_events`.
- The May Node example used `Decimal.from()` for tier monetary values; the November curl example sends numeric form values. The Node syntax is example-specific, not a universal requirement.

**Product 2 — license fee (flat):**
- `billing_scheme: 'per_unit'`, `usage_type: 'licensed'`, `unit_amount_decimal=10000` for the $100 USD monthly example.
- No meter — standard recurring flat price. The May Node example expresses the amount as `Decimal.from('10000')`.

**Subscription:** Two items carry the licensed and usage price IDs. The November guide shows `customer_account` for a customer-configured Account and `customer` for a Customer object. The Accounts v2 API is generally available for Connect users and in public preview for other Stripe users; preview participants need a preview version. This is capture-specific eligibility guidance, not evidence that a particular account is enabled. The meter-event sample still uses `CUSTOMER_ID`, so it does not demonstrate an Account v2 event payload end to end.

### Invoice timing

In the guide's two-product example, the license fee is charged at the beginning of the month and the second invoice combines prior-month usage fees with the upcoming license fee. Under `billing_mode=flexible`, the first invoice excludes metered lines without prior usage; classic mode shows zero-value metered lines. The guide's separate statement that an invoice is created only for backdated usage or pending invoice items is ambiguous for a subscription that also has an upfront licensed price. Do not apply it as a blanket no-first-invoice rule for the mixed-price example. No invoice creation or payment was executed in this capture. Meter events and summaries process asynchronously.

### Alternative single-product approach

Set a $100 flat amount on the first graduated tier row to place the initial flat fee at period end alongside usage, instead of using the separate licensed-price example with an upfront fee.

> [!warning] Contradiction
> Both the May and November captures say 0.04 USD per hundred units in pricing prose, while their Dashboard tier examples say 0.04 USD per unit and their API tier amount is `unit_amount_decimal=4` for USD. The captures do not establish a resolved rate by live execution.

## Related

- [[stripe]] — company and payments platform context.
- [[stripe-usage-based-billing]] — usage-based billing concept and pricing model context.

## Raw Sources

- [[raw/stripe-billing-subscriptions-usage-based-v1-use-cases-flat-fee-and-overages-2026-11-07]] — November 7, 2026 capture with curl examples and Accounts v2/Customers v1 paths.
- [[raw/stripe-usage-based-billing-flat-fee-overages-2025]] — historical May capture with Node SDK examples and the same rate wording conflict.
