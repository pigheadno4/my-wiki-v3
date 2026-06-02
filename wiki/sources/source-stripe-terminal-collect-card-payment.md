---
title: "Stripe Terminal: Collect Card Payments (All Platforms)"
type: source
date_ingested: 2026-04-24
original_format: webpage
raw_files:
  - "stripe-terminal-collect-card-payment-2025.md"
tags: [stripe, terminal, in-person, paymentintents, card-present, collect, capture, server-driven, javascript, ios, android, react-native]
---

## Stripe Terminal: Collect Card Payments (All Platforms)

Payment collection guide for all 5 Terminal SDK platforms: Server-driven, JavaScript, iOS, Android, React Native.

## Key Takeaways

### Universal payment flow

1. Create PaymentIntent (`card_present` in `payment_method_types`)
2. Collect payment method (reader prompts cardholder)
3. Process/Confirm payment (authorization)
4. (Optional) Capture

### Critical rules

- **Don't recreate PaymentIntent on decline** — reuse the same PI; create a new one only if you cancel the failed one first (to avoid double charges)
- **PaymentIntent must be in `requires_payment_method` state** to be processable; authorized/captured/canceled PI → `intent_invalid_state` error
- **Manual capture deadline: 2 days** — authorization expires and funds released after 2 days
- **After collect, must authorize or cancel within 30 seconds**
- **Don't recreate PI after timeout** — `terminal_reader_timeout` may be a false negative (reader received command but no ack); retry the same PI

### Server-driven specifics

- Two flow options:
  1. **Process immediately**: `processPaymentIntent` → verify via webhook or poll
  2. **Collect-inspect-confirm**: `collectPaymentMethod` → inspect PaymentMethod → `confirmPaymentIntent`
- **Verify reader state**: listen to `terminal.reader.action_succeeded`/`action_failed`/`action_updated` webhooks (recommended) or poll Reader/PI
- **Reader offline threshold**: Stripe considers a reader offline if no signal received for **2 minutes**
- **Cannot cancel during active authorization**: `cancel_action` during authorization → `terminal_reader_busy` error; must wait for processing to complete
- **Customer cancellation**: `enable_customer_cancellation: true` on `processPaymentIntent`; sends `terminal.reader.action_failed` with `failure_code: customer_canceled`
- **Missing webhooks**: reader disconnect during payment can leave action stuck at `in_progress`; cashier must call `cancel_action` to reset

### Server-driven error codes

| Error code | Cause | Resolution |
| --- | --- | --- |
| `intent_invalid_state` | PI not in `requires_payment_intent` | Reuse or cancel the PI |
| `terminal_reader_busy` | Reader processing another action | Wait; don't retry immediately |
| `terminal_reader_timeout` | Reader didn't acknowledge (may be false negative) | Retry with same PI; check network |
| `terminal_reader_offline` | No signal from reader for 2 minutes | Check power and network |
| `connection_error` | Reader networking timeout during authorization | Fetch PI status; may already be authorized |
| `card_declined` | Card declined | Prompt alternate payment; retry same PI |
| `customer_canceled` | Cardholder tapped cancel button | Normal flow; prompt retry |

### JavaScript SDK specifics

- **Always confirm client-side** — server-side confirmation bypasses PIN prompts → transaction failures
- Error handling after `processPayment` failure:

| PI Status | Meaning | Resolution |
| --- | --- | --- |
| `requires_payment_method` | Card declined | Retry `collectPaymentMethod` with same PI |
| `requires_confirmation` | Connectivity issue | Retry `processPayment` with same PI |
| PI is nil | Request timed out, unknown status | Retry original PI — do NOT create new one |

### iOS/Android/React Native specifics

- Flow: `createPaymentIntent` (server) → `collectPaymentMethod` (client) → `processPayment` (client) → capture (server)
- `collectPaymentMethod` returns updated PI with encrypted payment method data
- `processPayment` returns PI with status `requires_capture` (manual) or `succeeded` (automatic)

### Tips collection (US only)

Can collect tips on receipt when capturing payments.

## Relevant Wiki Pages

- [[stripe]] — Stripe company overview
- [[stripe-terminal]] — Stripe Terminal concept page

## Raw Sources

- [[stripe-terminal-collect-card-payment-2025]] — verbatim payment collection guide (2304 lines; all 5 platforms)
