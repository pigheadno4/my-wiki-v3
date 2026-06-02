---
title: "Stripe — Orchestration: Route Payments to Multiple Processors"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-orchestration-route-payments-2026.md"
tags: [stripe, orchestration, multi-processor, routing, payment-record, webhooks, private-preview]
---

## Summary

Implementation guide for Stripe Orchestration. Covers Dashboard rule setup, PaymentIntent API integration, Payment Record objects (replacing Charges for third-party routed payments), reporting/webhook changes, and error prevention behavior.

## API Integration

Add `payments_orchestration: { enabled: true }` to PaymentIntent creation. Routing rules configured in Dashboard apply automatically.

Auto-routing (no API change needed) for Billing, Checkout Sessions, Payment Links, Dashboard payments — contact Stripe representative to configure.

## New API Objects

For payments routed to third-party processors, Stripe creates:
- **Payment Record** (`payment_record`): execution history; retrieve via `stripe.paymentRecords.retrieve(id)`
- **Payment Attempt Record** (`payment_attempt_record`): per-attempt detail

`latest_charge: null` in the PaymentIntent when routed to third-party.

## Reporting Changes Required

Two breaking changes for third-party routed payments:
1. **No Charges** created → must switch to Payment Attempt Records for reporting/reconciliation
2. **No Balance Transactions** → funds don't flow through Stripe account; systems that assume always-present Balance Transactions will break

## Webhook Changes

New PaymentIntent status flow for third-party routed payments:
1. `processing` → `payment_intent.processing` event (useful for inventory holds)
2. `succeeded` → `payment_intent.succeeded` event (no change needed if already handling this)

## Limitations

- No Setup Intents API support
- No flexible acquiring features on other processors
- 3DS requires Acquirer BIN from the destination processor
- Dashboard: no balance summary, dispute status, or receipts for third-party payments; data lag up to 2 days

## Error Prevention Mode

When enabled: if the chosen processor doesn't support a required feature, Stripe auto-falls back to processing on Stripe. If Stripe also fails, the retry processor is not attempted.

## Related Pages

- [[stripe-orchestration]] — concept page (updated with implementation details)
- [[source-stripe-orchestration]] — overview source

## Raw Sources

- [[stripe-orchestration-route-payments-2026]] — verbatim implementation guide (175 lines)
