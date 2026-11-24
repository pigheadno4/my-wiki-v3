---
title: "Stripe: Accept a Payment with Satispay"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-satispay-accept-payment-2025.md"
tags: [stripe, wallets, satispay, integration, checkout, elements, direct-api, ios, android, manual-capture, accounts-v2]
---

## Summary

Multi-platform guide to accepting Satispay payments through Stripe. Covers Checkout, Checkout Sessions API, Payment Intents API, Direct API, iOS, and Android. Payment mode only — no setup or subscription mode.

## Key Details

**EUR only**, European business locations. Single-use, redirect-based payment method with immediate confirmation.

**4 web integration paths + 2 mobile**:
1. **Checkout** — hosted UI, add `satispay` to `payment_method_types`, all line items same currency
2. **Checkout Sessions API** — embedded Payment Element via `ui_mode: 'elements'`, returns `client_secret`
3. **Payment Intents API** — standard Payment Element + `stripe.confirmPayment()` with `return_url`
4. **Direct API** — server-side `stripe.confirmSatispayPayment()` with `return_url` + `payment_method_data: { type: 'satispay' }`
5. **iOS** — `STPPaymentMethodSatispayParams` + `STPPaymentHandler.confirmPayment()`, custom URL scheme required
6. **Android** — `PaymentMethodCreateParams.createSatispay()` + `PaymentLauncher.confirm()`, custom URL scheme required

**Accounts v2**: use `customer_account` instead of `customer` on PaymentIntent creation.

**Manual capture**: `capture_method: 'manual'` → status `requires_capture` → `paymentIntents.capture()`. 7-day capture window. Cancel if you won't capture. Partial capture supported (`amount_to_capture`).

**Testing**: sandbox shows approve/decline test page. Live mode redirects directly to Satispay — no approve/decline option.

## Error Codes

| Error code | Action |
| --- | --- |
| `payment_intent_invalid_currency` | Enter a supported currency |
| `missing_required_parameter` | Check error message for details |
| `payment_intent_payment_attempt_failed` | Check `last_payment_error.code` for failure reason |
| `payment_intent_authentication_failure` | Check `last_payment_error.code`; occurs on manual test failure |
| `payment_intent_redirect_confirmation_without_return_url` | Provide a `return_url` when confirming |

## Raw Sources

- [[stripe-satispay-accept-payment-2025]] — verbatim multi-platform guide (1,887 lines); 16 italic fixes, 1 CDN image downloaded
