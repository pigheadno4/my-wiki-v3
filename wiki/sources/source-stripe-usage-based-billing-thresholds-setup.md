---
title: "Stripe: Set Up Thresholds"
type: source
date_ingested: 2026-05-05
original_format: webpage
raw_files:
  - "stripe-usage-based-billing-thresholds-setup-2025.md"
tags: [stripe, billing, usage-based, thresholds, invoicing, tiered-pricing]
---

## Summary

Implementation guide for billing thresholds: monetary (subscription-level) and usage (item-level) thresholds, billing cycle anchor reset, how tiers behave across threshold invoices, and the negative line item edge case with volume tiers.

## Key Details

**Monetary threshold** — set on a subscription:
- `billing_thresholds[amount_gte]=10000` (smallest currency unit; min 50 units)
- `billing_thresholds[reset_billing_cycle_anchor]=false|true`
- Configurable via Dashboard or API

**Usage threshold** — set on a subscription item:
- `billing_thresholds[usage_gte]=2000`
- **API only** — Dashboard not supported

**Billing cycle anchor behavior**: by default unchanged at threshold (subscription resets at natural period end). Set `reset_billing_cycle_anchor=true` to reset the cycle when the threshold is reached.

**Tiers across threshold invoices**: tiers are maintained across threshold invoices — they only reset at end of billing period. To reset tiers at threshold, must set `reset_billing_cycle_anchor=true`.

**Volume tiers + thresholds = negative line items**: volume tiers reprice *all* usage when a tier boundary is crossed. If a threshold invoice was already issued at the higher tier rate, the next invoice may include a negative "amount previously billed" line item to correct for the lower rate. Excess credit goes to customer balance for future invoices.

**Threshold invoices don't include grace period usage** — only usage accrued up to the invoice creation moment.

## Raw Sources

- [[stripe-usage-based-billing-thresholds-setup-2025]] — verbatim webpage content (112 lines); fixed 4× `_italic_` → `*italic*`
