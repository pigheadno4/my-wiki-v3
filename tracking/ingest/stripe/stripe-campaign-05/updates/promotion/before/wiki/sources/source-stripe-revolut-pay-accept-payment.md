---
title: "Stripe: Accept a Payment with Revolut Pay"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-revolut-pay-accept-payment-2025.md"
tags: [stripe, wallets, revolut-pay, checkout, elements, direct-api, ios, android, react-native, redirect, qr-code, manual-capture]
---

## Summary

Multi-platform integration guide for accepting Revolut Pay payments. Covers Checkout, Elements, Direct API, iOS, Android, and React Native. Revolut Pay is a reusable redirect-based payment method with both mobile redirect and desktop QR code authentication flows.

## Key Details

**6 platforms**: Checkout, Elements, Direct API, iOS, Android, React Native.

**Reusable payment method** — supports recurring/subscriptions in Checkout.

**Authentication modes**:
- **Mobile**: customer redirected to Revolut app → approve/decline → redirect back. 1-hour session expiry.
- **Desktop**: QR code shown on page → scan with camera or Revolut app → auto-closes after auth. Refreshable up to **20×**. 1-hour session expiry.

**Failed payments**: Revolut detaches PaymentMethod and transitions PI to `requires_payment_method` on decline or 1-hour timeout.

**Manual capture**: `capture_method: 'manual'`; 7-day capture window; auto-cancels if not captured.

**Testing**: sandbox shows approve/decline page. Live mode — **auto-approves** after redirect (mobile) or QR scan (desktop); no approve/decline option.

**Error codes** (4): `payment_intent_invalid_currency`, `missing_required_parameter`, `payment_intent_payment_attempt_failed`, `payment_intent_redirect_confirmation_without_return_url`.

## Raw Sources

- [[stripe-revolut-pay-accept-payment-2025]] — verbatim multi-platform guide (1,869 lines); 15 italic fixes; 1 CDN PNG downloaded (stripe-revolut-pay-checkout-visible.png)
