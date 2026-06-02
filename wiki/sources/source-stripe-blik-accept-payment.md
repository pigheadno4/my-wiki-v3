---
title: "Stripe: Accept a BLIK Payment"
type: source
date_ingested: 2026-05-03
original_format: webpage
raw_files:
  - "stripe-blik-accept-payment-2025.md"
tags: [stripe, blik, poland, pln, checkout, elements, ios, android]
---

## Summary

Multi-platform integration guide for accepting BLIK payments: Checkout, Direct API (Elements + React), iOS, and Android. Covers `stripe.confirmBlikPayment()` flow, statement descriptor customization, and all sandbox failure simulation patterns.

## Key Details

### Checkout path

- `payment_method_types: ['blik']`, `pln` only, payment mode only (setup/subscription not yet)
- Supports hosted page, embedded page, and Elements UI modes
- `payment_intent_data.description` (lines 1–2, max 70 chars), `statement_descriptor` (line 3, max 22 chars), website URL (line 4)
- Test: enter any 6-digit code (e.g. `123456`)
- Refund/dispute window: **13 months**

### Direct API path

- `stripe.confirmBlikPayment(clientSecret, { payment_method: { blik: {} }, payment_method_options: { blik: { code } } })`
- **Synchronous** — doesn't return until success or failure (no redirect)
- After confirm: `requires_action` status with `blik_authorize` next_action → customer has 60s in banking app
- Recommend showing countdown timer to customer

### iOS

- `STPConfirmBLIKOptions(code:)` + `STPPaymentHandler.confirmPayment()` → poll for `succeeded` status

### Sandbox failure simulation (email patterns)

**Immediate**: `.*invalid_code@.*`, `.*expired_code@.*`

**Declines (8s delay)**: `.*limit_exceeded@.*`, `.*insufficient_funds@.*`, `.*customer_declined@.*`, `.*bank_declined@.*`, `.*blik_declined@.*`

**Timeouts (60s delay)**: `.*customer_timeout@.*`, `.*bank_timeout@.*`, `.*blik_timeout@.*`

## Raw Sources

- [[stripe-blik-accept-payment-2025]] — verbatim webpage content (1190 lines, Checkout + Direct API + iOS + Android)
