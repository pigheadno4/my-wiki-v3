---
title: "Alternative Payment Methods (APM) Overview"
type: source
date_ingested: 2026-04-14
original_format: webpage
raw_files:
  - "paypal-apm-overview.md"
tags: [paypal, apm, apple-pay, google-pay, ideal, bancontact, blik, eps, multibanco, mybank, pay-upon-invoice, przelewy24, trustly, bank-redirect, local-payment-methods]
---

## Overview

Overview of PayPal's alternative payment methods (APMs) — non-card, non-PayPal-wallet payment options including bank redirects, digital wallets, vouchers, and deferred payment.

Source URL: <https://developer.paypal.com/docs/checkout/apm/>

Last updated: 2025-07-30

## Key Takeaways

### Available APMs (as of July 2025)

| Payment method | Type | Flow | Countries | Currencies | Min | Refunds |
| --- | --- | --- | --- | --- | --- | --- |
| Apple Pay | push | direct | Multi-country | Multi-currency | 1 USD | ≤180 days |
| Google Pay | push | direct | Multi-country | Multi-currency | 1 USD | ≤180 days |
| Bancontact | bank redirect | redirect | Belgium | EUR | 1 EUR | ≤180 days |
| BLIK | bank redirect | redirect | Poland | PLN | 1 PLN | ≤180 days |
| eps | bank redirect | redirect | Austria | EUR | 1 EUR | ≤180 days |
| iDEAL | bank redirect | redirect | Netherlands | EUR | 0.01 EUR | ≤180 days |
| MyBank | bank redirect | redirect | Italy | EUR | N/A | ≤180 days |
| Przelewy24 | bank redirect | redirect | Poland | PLN, EUR | 1 PLN | ≤180 days |
| Trustly | bank redirect | redirect | AT,DE,DK,EE,ES,FI,GB,LT,LV,NL,NO,SE | EUR,DKK,SEK,GBP,NOK | 0.01 EUR | ≤365 days |
| Multibanco | voucher | redirect | Portugal | EUR | N/A | N/A |
| Pay upon Invoice | deferred payment | direct | Germany | EUR | 5 EUR | ≤180 days |

### Payment type taxonomy

- **Push**: payer-initiated from a digital wallet (Apple Pay, Google Pay) — `direct` flow, no redirect
- **Bank redirect**: payer redirected to their bank's interface to authorize — all the European bank APMs
- **Voucher**: payer receives a reference number to pay at a bank/ATM (Multibanco)
- **Deferred payment**: pay after delivery (Pay upon Invoice, Germany only)

### Notable details

- **Trustly** has the longest refund window: up to **365 days** (vs 180 for all others)
- **Multibanco**: no minimum amount, **no refunds supported**
- **Pay upon Invoice**: Germany/EUR only, 5 EUR minimum, `direct` flow
- **Przelewy24**: supports both PLN and EUR
- **iDEAL**: very low minimum (0.01 EUR)

### Sunset notices

- **giropay**: sunset June 30, 2024 — no longer supported
- **Sofort**: sunset April 18, 2024 — no longer supported

### Privacy disclosure requirement

Merchants must inform payers that PayPal processes the payment. Two approved options:
1. At-checkout text linking to PayPal Privacy Statement
2. Privacy notice (shown before payment) describing PayPal's data processing role

## Raw Sources

- [[paypal-apm-overview]] — verbatim overview page with full APM table

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[source-paypal-save-applepay-js-sdk]] — Apple Pay vault integration detail
