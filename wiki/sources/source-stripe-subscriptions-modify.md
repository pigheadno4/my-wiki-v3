---
title: "Stripe Subscriptions — Modify Subscriptions"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-subscriptions-modify-2026.md"
tags: [stripe, billing, subscriptions, prorations, pending-updates, modify]
---

## Summary

Hub page covering how to change existing subscriptions without canceling and recreating them. Key contribution: the billing-related vs non-billing updates distinction, and how discount changes interact with prorations in the same API call.

## Billing impacts

Two categories of subscription changes:

- **Billing-related updates** — create prorations and can generate invoices: changing prices, quantities, billing periods, adding or removing subscription items.
- **Non-billing updates** — apply immediately with no prorations: metadata, payment methods, tax settings, discount-only changes.

### Configuration updates

Metadata and payment method updates don't generate invoices even with `proration_behavior=always_invoice` because they don't change the amount owed for the current billing period.

### Discount-only changes

Updating coupons or promotion codes alone doesn't create proration invoice items — the new discount applies to the next invoice only.

**Mixed call behavior**: if you combine a discount change with a proration-triggering update (e.g. quantity change) in the same API call, Stripe calculates the proration using the **updated discount state**.

## Pending updates

For changes that automatically trigger a new invoice, use [pending updates](https://docs.stripe.com/billing/subscriptions/pending-updates.md) so that changes only apply if the new invoice is successfully paid.

## Use cases covered by sub-guides

| Topic | What it covers |
|---|---|
| Change billing period | Adjust billing date |
| Change prices | Upgrade / downgrade |
| Cancel | Manually cancel subscriptions |
| Pause payment | Temporarily stop collecting payments |
| Apply discounts | Coupons and promotion codes |
| Trial periods | Delay payments |
| Quantities | Multiple quantities of a product |
| Taxes | Stripe Billing + Stripe Tax |
| Payment methods | Allow/restrict payment methods per subscription |
| Prorations | Handle prorations for modified subscriptions |

## Related pages

- [[stripe-subscriptions]] — concept page
- [[stripe-subscriptions-coupons]] — discount / coupon behavior
- [[stripe]] — company page

## Raw Sources

- [[stripe-subscriptions-modify-2026]] — verbatim Stripe docs webpage
