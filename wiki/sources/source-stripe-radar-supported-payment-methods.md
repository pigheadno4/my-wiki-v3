---
title: "Stripe — Supported Payment Methods with Radar"
type: source
date_ingested: 2026-05-10
original_format: webpage
raw_files:
  - "stripe-radar-supported-payment-methods-2026.md"
tags: [stripe, radar, payment-methods, ach, sepa, bnpl, wallets, custom-rules]
---

## Summary

Default Radar protection applies to all payment methods. Custom risk settings (Fraud Teams or Platforms) are fully available for cards, ACH, and SEPA; private preview for others.

## Coverage

| Status | Payment methods |
| --- | --- |
| Default (all users) | All payment methods — blocks high-risk transactions |
| Custom supported (Fraud Teams/Platforms) | Cards (credit/debit/card-backed wallets: Apple Pay, Google Pay), ACH, SEPA |
| Private preview | ACSS, AU BECS, Bacs, NZ BECS, PayTo; BNPL (Affirm, Afterpay, Klarna); Digital wallets (Cash App, PayPal); Stablecoin/crypto wallets |

## Custom Features (Fraud Teams/Platforms)

- Block/allow lists (email, IP, email domain, etc.)
- Custom rules with `:payment_method_type:` attribute to target specific PMs
- Rule backtesting against historical data
- Consolidated Radar analytics across all payment volume

## Example Rule

```
if :payment_method_type: = 'bacs_debit' and :dispute_count_on_ip_weekly: > 3
```

## Related Pages

- [[stripe-radar]] — concept page (updated with PM coverage)
- [[source-stripe-radar-risk-settings]] — risk settings and controls

## Raw Sources

- [[stripe-radar-supported-payment-methods-2026]] — verbatim supported payment methods with Radar
