---
title: "Stripe Terminal: Additional Payment Methods (QR Code)"
type: source
date_ingested: 2026-04-24
original_format: webpage
raw_files:
  - "stripe-terminal-additional-payment-methods-2025.md"
tags: [stripe, terminal, in-person, wechat-pay, affirm, paynow, qr-code, payment-methods, capture]
---

## Stripe Terminal: Additional Payment Methods (QR Code)

Guide for accepting WeChat Pay, Affirm, and PayNow via QR code on Terminal smart readers.

## Key Takeaways

### Supported methods and readers

- **Methods**: WeChat Pay (not in Japan), Affirm, PayNow
- **Readers**: Smart readers + Tap to Pay on Android — QR displayed on reader screen
- **Tap to Pay on iPhone**: app must handle QR display itself
- **Simulated reader NOT supported** — physical reader required for QR payment testing
- **No offline support** — active network required for all QR transactions

### Capture support

| Method | Manual capture |
| --- | --- |
| `card_present` | ✓ |
| `affirm` | ✓ |
| `wechat_pay` | ✗ (automatic only) |
| `paynow` | ✗ (automatic only) |

**Hybrid pattern** (broadest compatibility): `capture_method: automatic` + `payment_method_options.card_present.capture_method: manual`

### QR payment flow

1. Create PI with non-card method types in `payment_method_types`
2. Process PI → reader shows QR code
3. Customer scans QR → completes payment on their device
4. Reader updates (usually within seconds); PI moves to final state
5. Listen to `payment_intent.succeeded`/`payment_intent.payment_failed` webhooks

**QR payments are asynchronous** — PI stays in `requires_action` after customer scans. Stripe sends `terminal.reader.action_succeeded` webhook when payment completes.

### Affirm: `return_url` required

Affirm needs a `return_url` to redirect after authentication/cancellation. If not provided, customer sees Stripe's generic landing page.

### Free reader while QR pending

If QR takes too long (customer switched to app): call `cancel_action` to reset the reader. PI stays in `requires_action`; customer can still complete; reconcile via `payment_intent.succeeded`/`payment_intent.payment_failed` webhooks.

### US restriction

When deploying readers with **only** non-card payment methods in the US: **cart display not supported** at this time.

### Testing

Scan QR code with mobile phone in sandbox → URL goes to Stripe-hosted test payment page (or Affirm sandbox if enrolled; use SSN last 4: `0000` or `5678` for Affirm testing).

## Relevant Wiki Pages

- [[stripe]] — Stripe company overview
- [[stripe-terminal]] — Stripe Terminal concept page

## Raw Sources

- [[stripe-terminal-additional-payment-methods-2025]] — verbatim additional payment methods guide (921 lines; all 5 platforms)
