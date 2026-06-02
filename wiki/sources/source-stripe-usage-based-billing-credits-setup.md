---
title: "Stripe: Set Up Billing Credits"
type: source
date_ingested: 2026-05-05
original_format: webpage
raw_files:
  - "stripe-usage-based-billing-credits-setup-2025.md"
tags: [stripe, billing, usage-based, credits, credit-grants, invoicing]
---

## Summary

End-to-end implementation guide for billing credits: creating credit grants (Dashboard + API), applying credits to invoices, retrieving balance summaries, listing transactions, and optionally funding credits via a one-off invoice.

## Key Details

**Prerequisites**: meter + metered price + subscription must exist before creating credit grants. Credits only apply to meter-price subscription line items (not Usage Records API).

**Create a credit grant** — `stripe.billing.creditGrants.create({ customer, name, applicability_config: { scope: { price_type: 'metered' } }, category: 'paid', amount: { type: 'monetary', monetary: { value: 1000, currency: 'usd' } } })`

**Price-level scoping** (specific metered item): pass `applicability_config.scope.billable_items[0].id = BILLABLE_ITEM_ID` to restrict the credit grant to a single price rather than all metered prices.

**Credits applied automatically** at invoice finalization. Visible on invoice as "Credit grant applied" under Subtotal.

**Retrieve balance**: `stripe.billing.creditBalanceSummary.retrieve({ customer, filter: { type: 'applicability_scope', applicability_scope: { price_type: 'metered' } } })`

**List transactions**: `stripe.billing.creditBalanceTransactions.list({ customer, credit_grant })`

**Funding flow** (optional — collect payment then grant):
1. `stripe.invoices.create({ customer, description: 'credit purchase', collection_method: 'charge_automatically' })`
2. `stripe.invoiceItems.create({ customer, unit_amount_decimal: Decimal.from('1000'), currency: 'usd', invoice })`
3. `stripe.invoices.finalizeInvoice(INVOICE_ID, { auto_advance: true })`
4. Listen for `invoice.paid` webhook → then call `creditGrants.create`

## Raw Sources

- [[stripe-usage-based-billing-credits-setup-2025]] — verbatim webpage content (193 lines)
