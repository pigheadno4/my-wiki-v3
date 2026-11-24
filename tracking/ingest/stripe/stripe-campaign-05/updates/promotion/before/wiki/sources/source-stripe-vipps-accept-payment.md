---
title: "Stripe: Accept a Payment with Vipps"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-vipps-accept-payment-2025.md"
tags: [stripe, wallets, vipps, norway, nok, integration, checkout, elements, direct-api, manual-capture, private-preview]
---

## Summary

Multi-platform guide to accepting Vipps payments through Stripe. Covers Checkout (Stripe-hosted + embedded), Elements (Payment Element with HTML+JS and React), and Direct API. Private preview — requires `vipps_preview=v1` header.

## Key Details

**NOK only**, EEA + GB business locations. Single-use card wallet with immediate confirmation. Payment mode only — no setup or subscription mode.

**Private preview requirements**:
- All API requests: `apiVersion: '2026-04-22.preview; vipps_preview=v1'`
- Elements (Stripe.js): `betas: 'vipps_pm_beta_1'` + `apiVersion: vipps_preview=v1`

**3 integration paths**:
1. **Checkout** — Stripe-hosted page or full embedded page (`ui_mode: 'embedded_page'`). Add `vipps` to `payment_method_types`, all line items in NOK
2. **Elements** — Payment Element with PaymentIntent. `stripe.confirmPayment()` with `return_url`. HTML+JS and React examples
3. **Direct API** — Create PaymentIntent with `payment_method_types: ['vipps']` + `payment_method_data: { type: 'vipps' }` → confirm → `next_action.redirect_to_url`

**Two authentication flows**:
- **Mobile**: redirect directly to Vipps app for approval
- **Desktop**: Vipps landing page → enter phone number → push notification to Vipps app

**5-minute authentication window**: if customer doesn't authorize within 5 minutes, PaymentMethod detaches and PaymentIntent transitions to `requires_payment_method`.

**Card retry**: if underlying card transaction is declined, customer can choose a different card in the Vipps app and retry.

**Manual capture**: `capture_method: 'manual'`, 7-day hold period. **Full amount only** — no partial capture. `payment_intent.amount_capturable_updated` event on successful authorization.

**Cancellation**: cancel PaymentIntent before expiry via API.

**Refunds/disputes**: subject to Visa and Mastercard network rules (card rails underneath).

**Testing**: sandbox shows approve/decline test page. Direct API: follow `next_action` redirect URL → authorize or fail. Live mode: phone number → push notification → approve/decline in Vipps app.

## Raw Sources

- [[stripe-vipps-accept-payment-2025]] — verbatim multi-platform guide (1,123 lines); 7 italic fixes
