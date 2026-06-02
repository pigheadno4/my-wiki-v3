---
title: "Stripe: Nacha Compliance for Online Consumer Purchases"
type: source
date_ingested: 2026-05-02
original_format: webpage
raw_files:
  - "stripe-ach-nacha-compliance-2025.md"
tags: [stripe, ach, us-bank-account, nacha, compliance, sec-codes, web, tel, transaction-purpose]
---

## Summary

Effective March 20, 2026, Nacha requires businesses to include `PURCHASE` in the Company Entry Description for qualifying ACH e-commerce transactions. Stripe provides both a Dashboard setting and a per-transaction API field to comply.

## Key Details

**Qualifying transaction**: consumer-authorized online purchase of physical or digital goods using WEB or TEL SEC code. Excludes services, donations, and bill payments.

**Dashboard configuration** (global): Settings > Payment methods > ACH Direct Debit > ACH classification. Three options:
- **Automatically classify** — Stripe infers from business and transaction signals (default fallback)
- **Classify all as goods** — for businesses that exclusively sell physical/digital products
- **Don't classify any as goods** — for services, donations, or bill payments

**API configuration** (per-transaction): `payment_method_options.us_bank_account.transaction_purpose` on PaymentIntent:
- `goods` — adds `PURCHASE` to company entry description
- `services` / `other` — no `PURCHASE` label
- Omitted — falls back to Dashboard setting, then auto-classify

**Connect**: Platform Dashboard setting covers direct charges + destination charges + separate charges without `on_behalf_of`. Connected account settings configured separately under Settings > Connect > Payment methods.

## Raw Sources

- [[stripe-ach-nacha-compliance-2025]] — verbatim webpage content
