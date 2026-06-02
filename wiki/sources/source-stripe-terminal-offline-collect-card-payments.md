---
title: "Stripe Terminal: Collect Card Payments While Offline"
type: source
date_ingested: 2026-04-24
original_format: webpage
raw_files:
  - "stripe-terminal-offline-collect-card-payments-2025.md"
tags: [stripe, terminal, in-person, offline, ios, android, react-native, java, dotnet, paymentintents, capture]
---

## Stripe Terminal: Collect Card Payments While Offline

Detailed integration guide for offline payment collection across iOS, Android, React Native, Java, and .NET.

## Key Takeaways

### Risk disclosure

Offline payments: authorization happens AFTER connectivity restored. Merchant assumes all decline and tamper risks. No way to recover funds if reader is tampered or issuer declines.

### Minimum SDK versions

- iOS: `3.3.0`
- Android: `3.2.0`

### Prerequisites to connect offline

1. Enable offline mode via `Configuration` object (API or Dashboard) per Location — takes minutes to propagate + requires reader reconnect
2. Must have connected to same reader type at same Location **within last 30 days** while online
3. Reader software must have been updated within last 30 days

### Critical: clearing app cache loses stored payments

If you clear app cache or disk storage before offline payments are forwarded, those payments are **permanently lost**. Check `offlinePaymentsCount` before any destructive operation.

### Offline PaymentIntent behavior

- `stripeId`/`id` is **null** while offline — add custom `metadata` identifier for reconciliation
- After forwarding, use `didForwardPaymentIntent`/`onPaymentIntentForwarded` callback to reconcile via custom metadata
- `offlineDetails` populated only for PaymentIntents confirmed offline

### offlineBehavior options

| Value | Behavior |
| --- | --- |
| `PREFER_ONLINE` (default) | Offline if no network, online if available |
| `REQUIRE_ONLINE` | Fail if offline — use for high-amount risk management |
| `FORCE_OFFLINE` | Always offline; forwarded in background when network restored |

Risk management: `offlinePaymentsCount` + `offlinePaymentAmountsByCurrency` properties on `Terminal.offlineStatus.sdk`

### Stripe-enforced offline maximum

**10,000 USD** (or equivalent in operating currency) per transaction

### Offline receipts

- Access `paymentIntent.offlineDetails.offlineCardPresentDetails` for card details
- `account_type` and `authorization_response_code` **unavailable** for offline payments
- Prebuilt email receipts only sent after connectivity restored AND payment captured

### Manual capture for offline payments

Wait for `didForwardPaymentIntent`/`onPaymentIntentForwarded` callback. Capture only if:
- Status = `requiresCapture`/`REQUIRES_CAPTURE`  
- `offlineDetails.requiresUpload = false` (null `offlineDetails` also means capturable now)

## Relevant Wiki Pages

- [[stripe]] — Stripe company overview
- [[stripe-terminal]] — Stripe Terminal concept page

## Raw Sources

- [[stripe-terminal-offline-collect-card-payments-2025]] — verbatim offline payment collection guide (3434 lines; iOS, Android, React Native, Java, .NET)
