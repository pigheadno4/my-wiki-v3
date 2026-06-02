---
title: "Stripe Docs — Nigerian payment methods"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-nigeria-payment-methods-2025.md"
tags: [stripe, nigeria, naira, local-payment-methods, merchant-of-record, bank-transfer, wallets]
---

## Summary

Stripe supports Nigerian local payment methods via a merchant of record (MoR) model through a Nigerian partner. No local entity required — US-based Stripe accounts accept NGN with USD settlement.

## Key Facts

- **MoR flow**: customer pays on Stripe checkout → redirected to partner's localized checkout → payment completed there; funds available after 3 days
- **Currency**: NGN only; **business locations**: US only (USD settlement)
- **Payment methods**:
  - Naira cards — one-time + recurring
  - Naira bank transfer — one-time; recurring coming soon
  - Naira wallet — coming soon
- **Recurring**: Yes (Naira cards). **Manual capture**: Yes. **Connect**: Yes
- **Disputes**: Cannot challenge — PSP accepts request → funds removed immediately from Stripe account; must resolve with customer directly
- **Refunds**: Full + partial, 365-day window; up to 7 calendar days to return status for some transactions
- **VAT**: MoR partner remits buyer VAT for Nigerian transactions — include VAT in presentment pricing

## Integration

Dashboard or Payment Intents API. Checkout, Elements, and Payment Links supported.

## Related Pages

- [[stripe-nigeria-payment-methods]] — concept page
- [[stripe-managed-payments]] — broader merchant of record framework
- [[source-stripe-local-payment-methods-by-country]] — hub page linking Nigeria + South Korea guides
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-nigeria-payment-methods-2025]] — verbatim webpage content
