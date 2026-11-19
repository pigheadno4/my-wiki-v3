---
title: "Stripe: Accept a Payment with Bizum"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-bizum-accept-payment-2025.md"
tags: [stripe, real-time-payments, bizum, spain, eur, checkout, payment-intents, mobile, ios, android]
---

## Summary

Integration guide for Bizum across four paths: Checkout (hosted), Checkout Sessions API (Elements), PaymentIntents API, and Direct API. Covers web and mobile (iOS/Android). Direct API requires explicitly collecting the customer's Bizum-registered phone number.

## Key Details

**Four integration paths**:
- **Checkout**: `payment_method_types: ['bizum']`, EUR only, €0.50–€5,000 — no redirect required, Stripe.js polls
- **Checkout Sessions API**: standard Elements path with `currency: 'eur'`
- **PaymentIntents API**: standard `payment_method_types: ['bizum']` path
- **Direct API**: must collect Bizum-registered phone number from customer and pass as `billing_details[phone]` to `stripe.confirmPayment`; Stripe.js polls for result (no redirect)

**Mobile SDKs**: iOS (Swift via StripePaymentsUI) and Android (Compose) both supported. Use `automatic_payment_methods` or explicit `payment_method_types: ['bizum']`.

**Test phone numbers** (status transitions ~5 seconds after confirmation):

| Phone number | Outcome |
| --- | --- |
| `+34600000002` | Decline — `payment_method_provider_decline` |
| Any other | Success → `succeeded` |

**Error codes**: `payment_intent_invalid_currency`, `missing_required_parameter`, `payment_intent_payment_attempt_failed`, `payment_intent_authentication_failure`, `payment_intent_redirect_confirmation_without_return_url`.

**Note**: "Determine compatibility" fields (Customer Geography, Supported currencies, Payment/Setup/Subscription mode) are blank in the source page — template not filled in.

## Raw Sources

- [[stripe-bizum-accept-payment-2025]] — verbatim webpage content (1,858 lines); fixed `*Prices*` ×2, `*PaymentIntent*` ×2, `*client secret*` ×6, `*webhook*` ×4
