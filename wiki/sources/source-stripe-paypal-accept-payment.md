---
title: "Stripe: Accept a PayPal Payment"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-paypal-accept-payment-2025.md"
tags: [stripe, wallets, paypal, checkout, direct-api, ios, android, react-native, redirect, manual-capture, preferred-locale, statement-descriptor]
---

## Summary

Multi-platform integration guide for accepting PayPal payments via Stripe. Covers Checkout, Direct API, iOS, Android, and React Native. PayPal is a redirect-based payment method for European merchants processing through Stripe infrastructure.

## Key Details

**Business locations**: Europe, GB, EEA. **Currencies**: EUR, GBP, USD, CHF, CZK, DKK, NOK, PLN, SEK, AUD, CAD, HKD, NZD, SGD (14 currencies).

**Checkout**: Supports payment + setup + subscription modes. All line items must share the same currency. Checkout auto-selects button vs standard payment method listing for conversion optimization.

**Authorization windows**:

- **Settlement to Stripe**: 10-day auth window; Stripe auto-reauthorizes for another 10 days (20 days total max). If reauth fails, expires after original 10 days.
- **Settlement to PayPal**: 3-day auth window; extends to 3 more days. Up to 10-day "honor period" available via PayPal support contact.

**Manual capture**: `capture_method: 'manual'` on PaymentIntent.

**Preferred locale**: `payment_method_options.paypal.preferred_locale` — 21 locales (cs-CZ, da-DK, de-AT, de-DE, de-LU, el-GR, en-GB, en-US, es-ES, fi-FI, fr-BE, fr-FR, fr-LU, hu-HU, it-IT, nl-BE, nl-NL, pl-PL, pt-PT, sk-SK, sv-SE).

**Statement descriptor**: `PAYPAL *BUSINESS_NAME` set by PayPal; `statement_descriptor` field appended up to 22-char total cap.

**Payer details** in `charge.payment_method_details.paypal`: `payer_email`, `payer_name`, `payer_id`, `transaction_id`.

**Settlement to PayPal**: balance transaction amount = 0 in Stripe; funds go directly to PayPal balance. Fees still recorded.

**Async payment methods**: disabled by default (synchronous only). Enabling requires contacting Stripe support.

**Test email patterns** (4 scenarios): `.*payee_account_restricted@.*`, `.*transaction_refused@.*`, `.*instrument_declined@.*`, `.*authorization_expired@.*`.

**Error codes** (7): `country_code_invalid`, `incorrect_address`, `payment_method_not_available`, `payment_method_provider_decline`, `payment_method_provider_timeout`, `payment_method_unactivated`, `payment_method_unexpected_state`.

## Integration by Platform

**Checkout**: Add `paypal` to `payment_method_types`. Supports stripe-hosted and embedded_page UI modes.

**Direct API**: `stripe.confirmPayPalPayment(clientSecret, { return_url })`. Handle redirect via `payment_intent` + `payment_intent_client_secret` query params on return. Manual server-side redirect: create+confirm PaymentIntent with `payment_method_data: { type: 'paypal' }` + `confirm: true` → redirect to `next_action.redirect_to_url.url`.

**iOS**: `STPPaymentMethodPayPalParams` → `STPPaymentMethodParams(payPal:...)` → `STPPaymentHandler.shared().confirmPayment()`. Webview return URL via custom URL scheme or universal link (`StripeAPI.handleURLCallback()`).

**Android**: `confirmPayPalPayment()` via `PaymentLauncher`. PaymentSheet also supported.

**React Native**: `stripe.confirmPayPalPayment(clientSecret, { returnUrl })`.

## Raw Sources

- [[stripe-paypal-accept-payment-2025]] — verbatim multi-platform guide (1,609 lines); 14 italic fixes
