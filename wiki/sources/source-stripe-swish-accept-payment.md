---
title: "Stripe: Accept a Swish Payment"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-swish-accept-payment-2025.md"
tags: [stripe, real-time-payments, swish, sweden, sek, checkout, elements, direct-api, ios, android, qr-code]
---

## Summary

Integration guide for Swish via Checkout, Elements, Direct API, iOS, and Android SDK. Direct API requires displaying a legal notice about Stripe as merchant of record. `next_action.swish_handle_redirect_or_display_qr_code` exposes QR code data. 3-minute authorization window.

## Key Details

**Three web integration paths**: Checkout, Elements, Direct API (plus iOS and Android SDK).

**Checkout**: `payment_method_types: ['swish']`, SEK only, Europe business locations. 3-minute window.

**Elements**: standard `stripe.confirmPayment` with `return_url`. Desktop renders inline QR (auto-closes on success). Mobile redirects to Swish app. Desktop QR can be refreshed up to **20 times** before expiry.

**Direct API**:
- PaymentIntent: `payment_method_types: ['swish']`, `payment_method_data: { type: 'swish' }`, optional `payment_method_options.swish.reference` (shown as order reference in Swish app)
- After confirmation: `next_action.swish_handle_redirect_or_display_qr_code` with `hosted_instructions_url`, `qr_code.data`, `qr_code.image_url_png`, `qr_code.image_url_svg`
- Redirect to/embed `hosted_instructions_url` — handles both QR and mobile redirect automatically

**Required legal notice (Direct API only)**: must display "Stripe Technology Europe Limited ('Stripe') has acquired the claim for payment. Therefore your payment will be made to Stripe." (EN/SE/other languages). Checkout and Elements show this automatically.

**3-minute authorization window** — PaymentIntent reverts to `requires_payment_method` on timeout.

**Cancelation**: can cancel before expiry via `PaymentIntents.cancel()`.

**Alternative authorization (invite-only beta)**: customer inputs phone number to open Swish app manually.

**Test scenarios (email-based)**:
- Any email → authorizes after 1 minute
- `*succeed_immediately@*` → succeeds within seconds
- `*expire_immediately@*` → fails within seconds
- `*expire_with_delay@*` → expires after ~3 minutes

## Raw Sources

- [[stripe-swish-accept-payment-2025]] — verbatim webpage content (1,797 lines); fixed `*Prices*` ×1, `*webhook*` ×7, `*client secret*` ×5, `*fulfillment*` ×1, `*confirm*` ×4, `*PaymentMethod*` ×4, `*require*` ×1
