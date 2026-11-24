---
title: "Stripe: Accept a Payment with PayPay"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-paypay-accept-payment-2025.md"
tags: [stripe, wallets, paypay, japan, jpy, checkout, elements, direct-api, ios, android, redirect]
---

## Summary

Multi-platform integration guide for accepting PayPay payments. Covers Checkout, Checkout Sessions API (Elements), Payment Intents API (Elements), Direct API, iOS, and Android. Payment mode only — no setup/subscription.

## Key Details

**6 platforms**: Checkout, Checkout Sessions API, Payment Intents API, Direct API, iOS, Android.

**Payment mode only** — setup/subscription mode not supported across all platforms.

**Redirect-based**: customers redirected to PayPay to authenticate, then returned to `return_url`.

**Testing**: sandbox shows approve/decline test page; **live mode redirects directly to PayPay** with no approve/decline option (same pattern as Cash App Pay live mode).

**Accounts v2 API**: use `customer_account` instead of `customer` on PaymentIntent.

**Error codes** (5):

| Error code | Issue |
| --- | --- |
| `payment_intent_invalid_currency` | Unsupported currency |
| `missing_required_parameter` | Required parameter missing |
| `payment_intent_payment_attempt_failed` | Detailed failure in error message |
| `payment_intent_authentication_failure` | Auth failure (also triggered by manual test decline) |
| `payment_intent_redirect_confirmation_without_return_url` | `return_url` missing |

## Raw Sources

- [[stripe-paypay-accept-payment-2025]] — verbatim multi-platform guide (1,838 lines); 16 italic fixes (_Prices_ ×2, _client secret_ ×6, _webhook_ ×2, _PaymentIntent_ ×4, _sandbox_ ×2)
