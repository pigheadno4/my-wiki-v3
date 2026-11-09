---
title: "Stripe: Set Up a Credit-Based Pricing Model"
type: source
date_ingested: 2026-05-05
original_format: webpage
raw_files:
  - "stripe-usage-based-billing-credits-2025.md"
tags: [stripe, billing, usage-based, meters, subscriptions, pricing, credits, credit-grants]
---

## Summary

End-to-end guide for credit-based pricing: pre-purchase monetary credits applied across multiple metered products. Credits burn down at end of billing period (not real-time). Introduces the Credit Grant, Credit Balance Summary, and Credit Balance Transaction APIs.

## Key Details

### How credits differ from flat fee+overages

Credits apply **indiscriminately across all meters** — a customer buys $10 of credits and can spend it on any mix of metered products. Flat fee+overages sets specific limits per product. Use credits when you want cross-product flexibility; use flat fee+overages when you need per-product caps.

### Two-meter, two-product setup

- Two meters: input tokens (`hypernian_input_tokens`) + output tokens (`hypernian_output_tokens`)
- Two `per_unit` metered prices: input at `Decimal.from('3')` ($0.03), output at `Decimal.from('5')` ($0.05)
- Subscription includes both prices in `items[]`

### Credit Grant API

```
stripe.billing.creditGrants.create({
  customer: CUSTOMER_ID,
  name: 'Credit grant',
  applicability_config: { scope: { price_type: 'metered' } },
  category: 'paid',
  amount: { type: 'monetary', monetary: { value: 1000, currency: 'usd' } },
})
```

- `value: 1000` = $10.00 (cents)
- `category: 'paid'` (as opposed to promotional)
- Only applies to meter-price subscription line items — Usage Records API not supported
- Optional: scoped to specific prices via `Eligibility`; priority configurable

### Burn timing

**Credits burn at end of billing period** (when invoice is created). Advanced UBB (private preview) burns in real time — sign up at advanced-ubb-private-preview@stripe.com.

### Credit balance APIs

- **Summary**: `stripe.billing.creditBalanceSummary.retrieve({ customer, filter: { type: 'applicability_scope', applicability_scope: { price_type: 'metered' } } })`
- **Transactions**: `stripe.billing.creditBalanceTransactions.list({ customer, credit_grant })`

### Funding flow (optional)

Create invoice → add invoice item (`invoiceItems.create`) → finalize (`invoices.finalizeInvoice`) → listen for `invoice.paid` webhook → grant credits

### Meter dimensions (optional)

Meters support dimensions for analytics segmentation (e.g., LLM model, token type, region, event type).

## Raw Sources

- [[stripe-usage-based-billing-credits-2025]] — verbatim webpage content (502 lines, two-meter end-to-end with credit grant, balance, and funding APIs)
