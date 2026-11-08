---
title: "Stripe — Migrate Subscriptions Using Stripe APIs"
type: source
date_ingested: 2026-11-08
canonical_url: https://docs.stripe.com/billing/subscriptions/import-subscriptions
original_format: webpage
raw_files:
  - "stripe-billing-subscriptions-import-subscriptions-2026-11-07.md"
  - "stripe-subscriptions-migration-api-2026.md"
tags: [stripe, subscriptions, migration, api, subscription-schedules, legacy-pricing, test-clocks]
---

## Summary

API-based guide for migrating subscriptions from another processor, an in-house system, or an existing Stripe account into Stripe Billing. Prepare customers and prices, map source IDs and billing dates, test in a sandbox, and create Subscription or Subscription Schedule objects. Schedules are recommended for future starts and phase controls; the guide does not establish that any particular migration has run or collected payment.

## Key Patterns

**Prerequisites**: Review migration stages and set up a Stripe Billing integration once. Request a payments-data/PAN import when moving from another processor; this is unnecessary for Stripe-to-Stripe migration. For third-party card data, complete the PAN import before setting default payment methods. These are instructions, not evidence that an import occurred.

**Automatic collection**: Customers the merchant wants to charge automatically need a default payment source; without one, subscription invoices cannot collect payment. Create or retrieve a PaymentMethod, attach it to the Customer if needed, then set `invoice_settings.default_payment_method` on the applicable Customer. An attached method that only lacks default status need not be recreated. This prerequisite was explicit in the 2026-11-07 capture, not in the earlier prerequisite list.

**Legacy pricing (conditional)**: If legacy plans must continue, create a placeholder product such as `Legacy plan` and use `items.price_data` where needed to override the legacy price. The 2026-05-12 Node.js example and the 2026-11-07 curl example illustrate this pattern; it is not a universal migration prerequisite. The newer legacy-price table states a maximum recurring interval of 3 years, 36 months, or 156 weeks; it also says to set only one of `unit_amount` and `unit_amount_decimal`. This is the captured documentation limit, not a validated account or API-version result.

**Identity and mid-cycle continuity**: Map source customer IDs to Stripe Customer IDs and source price IDs to Stripe Price IDs. Align a schedule's `current_phase.start_date`, `billing_cycle_anchor`, and `start_date` with the remaining source term. Preserve relevant third-party metadata and tax IDs or settings as appropriate.

**Subscription creation**: The Subscription API can create subscriptions, while the guide recommends Subscription Schedules for future starts, including monthly subscriptions more than 30 days ahead, and for phase-specific tax, collection, and coupon settings. A future start permits review before production billing; it does not prove that a scheduled subscription has started.

**Sandbox validation**: Run the pricing-model import in a sandbox before live mode. Remap script IDs after wiping sandbox data and when moving to live mode because price IDs differ. Test clocks simulate time progression in the sandbox; this capture does not demonstrate a production billing outcome.

**Existence check**: Listing Subscriptions with a `created` filter checks whether Subscription objects exist. It does not by itself verify source-to-Stripe mapping, schedule start, invoice payment, collectability, or completed reconciliation. The older Node.js `stripe.subscriptions.list({ created: { gt: timestamp } })` and newer curl call express the same narrow check.

> [!warning] Contradiction
> The 2026-05-12 raw guide states a maximum legacy-price interval of 1 year (12 months or 52 weeks), while the 2026-11-07 capture states 3 years (36 months or 156 weeks). Retain the old statement as dated evidence; do not treat either captured table as live account validation. Both captures also label their schedule example as June 1, 2022 at 00:00 UTC (the newer prose says May 31 at 17:00 GMT-7), but both retain `start_date=1654066801`, which resolves to June 1, 2022 at 07:00:01 UTC. The intended example time remains unresolved; preserve the literal timestamp and do not infer changed scheduling behavior from the prose revision.

## Related Pages

- [[stripe-subscriptions]] — concept page
- [[source-stripe-subscriptions-migration-toolkit]] — toolkit (no-code) migration

## Raw Sources

- [[raw/stripe-billing-subscriptions-import-subscriptions-2026-11-07]] — 2026-11-07 guide, including the default-payment-source prerequisite, curl examples, and three-year table (142 lines)
- [[raw/stripe-subscriptions-migration-api-2026]] — 2026-05-12 guide, including the Node.js examples and one-year table (160 lines)
