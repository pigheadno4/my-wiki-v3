---
title: "Stripe: Accept a Pix One-Time Payment"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-pix-accept-payment-2025.md"
tags: [stripe, real-time-payments, pix, brazil, brl, checkout, elements, direct-api, tax-id, cpf, cnpj]
---

## Summary

Integration guide for Pix one-time payments via Checkout, Elements (PaymentIntents), and Direct API. Notable: Checkout supports setup and subscription modes (via Pix Automático). Tax ID (CPF/CNPJ) required by Brazilian law. Configurable QR expiry via `expires_after_seconds`.

## Key Details

**Three integration paths**: Checkout, Elements (PaymentIntents), Direct API.

**Checkout**: `payment_method_types: ['pix']`, BRL only. Setup mode and Subscription mode both supported (redirect to Pix Automático for recurring).

**`expires_after_seconds`** (Checkout and Direct API): configurable QR/Pix string expiry. Range: 10 seconds to 1,209,600 seconds (14 days). Default: 14,400 seconds (4 hours). Set in `payment_method_options.pix`.

**Tax ID required**: Brazilian government requires CPF (individual) or CNPJ (business) for cross-border transactions.
- Elements: captures automatically
- Direct API: must collect explicitly via form field (`billing_details.tax_id`)

**Test data**:
- Test CPF: `000.000.000-00`
- Test email scenarios (set `billing_details.email`):
  - Any email → pays after 3 minutes
  - `*succeed_immediately@*` → pays immediately
  - `*expire_immediately@*` → `payment_intent.payment_failed` within seconds
  - `*expire_with_delay@*` → `payment_intent.payment_failed` after 3 minutes
  - `*fill_never@*` → expires per `expires_at`/`expires_after_seconds`

**Error codes**: `payment_intent_invalid_currency`, `missing_required_parameter`, `payment_intent_payment_attempt_failed`, `payment_intent_authentication_failure`, `payment_intent_redirect_confirmation_without_return_url`.

## Raw Sources

- [[stripe-pix-accept-payment-2025]] — verbatim webpage content (1,179 lines); fixed `*Prices*` ×1, `*subscription*` ×1, `*webhook*` ×4, `*PaymentIntent*` ×2, `*client secret*` ×4
