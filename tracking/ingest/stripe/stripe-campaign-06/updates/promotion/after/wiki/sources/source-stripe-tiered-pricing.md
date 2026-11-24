---
title: "Stripe — Set Up Tiered Pricing"
type: source
date_ingested: 2026-05-12
date_updated: 2026-11-24
original_format: webpage
canonical_url: "https://docs.stripe.com/subscriptions/pricing-models/tiered-pricing"
raw_files:
  - "stripe-subscriptions-pricing-models-tiered-pricing-2026-11-07.md"
  - "stripe-tiered-pricing-2026.md"
tags: [stripe, subscriptions, tiered, volume, graduated, pricing, tiers]
---

## Summary

Set up recurring tiered Prices whose total depends on a subscription item's quantity or usage. **Volume** applies the reached tier's rate to all units at the end of the period, so crossing a threshold can reduce the total. **Graduated** charges the units in each tier at that tier's rate and adds the charges.

## Volume vs Graduated Math

| Six units at $7 for 1–5, $6.50 for 6–10, $6 for 11+ | Volume | Graduated |
| --- | --- | --- |
| Formula | 6 × $6.50 | 5 × $7 + 1 × $6.50 |
| Total | $39 | $41.50 |

## Dashboard and API Setup

- **Dashboard.** Create a Product and a monthly recurring tiered Price for it. Choose Volume or Graduated, enter tier boundaries and amounts, and save.
- **API.** The examples create a USD Price on an existing Product through `POST /v1/prices` with `billing_scheme=tiered`, a monthly `recurring.interval`, and optional expansion of `tiers`. Set `tiers_mode` to the string `volume` or `graduated`. The font example pairs `up_to` values of 5, 10, and `inf` with `unit_amount` values of 700, 650, and 600 cents.

| Capture | Example format | `recurring.usage_type` in both modes |
| --- | --- | --- |
| 2026-05-12 | Node SDK | `metered` |
| 2026-11-07 | cURL | `licensed` |

The dated examples use different usage types while retaining the same tier calculations. The captures give no general requirement to use either example's usage type. See the raw captures' two **API** subsections for each exact request and [[source-stripe-usage-based-pricing]] for the separate meter setup.

> [!warning] Dashboard editing guidance in the 2026-05-12 and 2026-11-07 tiered guides
> Both tiered setup guides give a Subscription-use cutoff for editing the Product and Price. The 2026-04-20 and 2026-11-07 management guides describe restrictions on an existing Price from the time it is created and give a replacement-Price path to change the amount. See [[source-stripe-products-prices]] for Product and Price edits.

## Flat Amount per Tier

Both modes allow `unit_amount`, `flat_amount`, or both. Each tier needs at least one. The guides' flat-fee example uses `up_to` boundaries of 5, 10, 15, 20, and `inf`. At quantity 12, volume charges all 12 units at $3 plus the reached tier's $30 flat fee ($66). Graduated adds the per-unit and flat charges for the three occupied tiers ($111).

## Zero Quantity

If the first tier defines a flat amount, Stripe charges it even when `quantity=0`. To bill zero when there is no usage, the guide puts the flat rate in the `unit_amount` of an `up_to=1` tier and omits `flat_amount` for that tier.

## Related Pages

- [[stripe-subscriptions]] — Stripe Subscriptions concept
- [[stripe]]
- [[source-stripe-usage-based-pricing]] — usage-based pricing and meter setup

## Raw Sources

- [[raw/stripe-subscriptions-pricing-models-tiered-pricing-2026-11-07|2026-11-07 tiered pricing guide, licensed cURL examples]]
- [[stripe-tiered-pricing-2026]] — 2026-05-12 tiered pricing guide, metered Node examples (186 lines)
