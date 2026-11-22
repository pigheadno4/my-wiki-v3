---
title: "Stripe Orchestration"
type: concept
category: technology
tags: [stripe, orchestration, multi-processor, routing, retries, payment-routing, private-preview]
---

## Overview

Stripe Orchestration (private preview) is a rule-based payment routing layer that lets merchants route card payments across multiple external processors. Stripe acts as the orchestration layer; third-party processors remain the processor of record for routed transactions — their fees and liability terms continue to apply.

## Features

- **Multi-processor routing**: Route via PaymentIntents integration or auto-route from Billing, Checkout, Payment Links, or Dashboard
- **Retry on different processor**: Configure rules to automatically retry failed payments with alternative processors
- **Performance monitoring**: Analyze payment performance across processors
- **Post-transaction flows**: Refunds via Stripe Dashboard/Refunds API; third-party processors manage their own refunds
- **Sandbox rule testing**: Test routing rules before live activation

## Supported Products

Cards only via: Payments, Billing, Dashboard payments.

## Supported Processors and Feature Matrix

Three processors currently supported: **Adyen**, **Braintree**, **Worldpay WPG**.

| Feature | Adyen | Braintree | Worldpay WPG |
| --- | --- | --- | --- |
| Auto/manual capture, refunds, 3DS, statement descriptors, wallets, recurring | ✓ | ✓ | ✓ |
| Network tokens | ✓ | ✓ | ✗ |

Key exceptions: multicapture unsupported; `statement_descriptor_suffix_kanji` unsupported; `statement_descriptor_suffix_kana` Adyen only; 3DS + Apple Pay/Google Pay DPAN unsupported; Google Pay FPAN unsupported on Adyen.

Unsupported feature → HTTP 400 `orchestration_unsupported`.

## Explicitly Not Supported

Non-card payments, Link, Capital, Connect, Terminal, Organizations, Radar (for third-party routed payments), Sigma, disputes, settlement-related activity.

## Rule Conditions (7)

| Condition | Notes |
| --- | --- |
| Amount | Must also specify currency |
| BIN | First 6 or 8 digits of card |
| Card country | Card issuing country |
| Card issuer | Issuing financial institution |
| Card type | credit / debit / prepaid |
| Currency | Presentment currency |
| Metadata | PaymentIntent metadata fields |

Conditions evaluated **left to right**; first match wins. Default action applies if no condition matches. No active rules → payments route to Stripe.

**Rule lifecycle**: Draft → Activate (one active set at a time; activating new auto-deactivates current) → Deactivate. **Cannot edit active rules** — must duplicate, edit draft, then re-activate.

## Cross-Processor Retry Behavior

Configure a retry processor in each rule's Action. Key edge cases:

| Scenario | Behavior |
| --- | --- |
| 3DS fails (auth or post-auth payment failure) on main processor | **No retry** → `payment_intent.payment_failed` |
| Retry processor doesn't support a payment feature (e.g., Connect `on_behalf_of`) | No retry |
| Stripe Radar blocks transaction (main = Stripe) | Treated as decline → **retried on retry processor** |
| Adaptive Acceptance + Stripe is main processor | Stripe may internally retry before cross-processor retry triggers |
| Stripe is retry processor + Adaptive Acceptance enabled | Potentially 2 retries (1 cross-processor + 1 Adaptive Acceptance) |

## API Integration

Enable on PaymentIntent: `payments_orchestration: { enabled: true }`. Routing rules configured in the Dashboard apply.

For Billing, Checkout Sessions, Payment Links, and Dashboard payments (which auto-create PaymentIntents), contact Stripe representative to enable Orchestration.

## New API Objects (Breaking Change)

For payments routed to third-party processors, Stripe creates **Payment Records** and **Payment Attempt Records** instead of Charges:

```js
stripe.paymentRecords.retrieve('{{PAYMENT_RECORD_ID}}')
```

`latest_charge: null` in the PaymentIntent when routed to a third party.

## Reporting and Webhook Changes

**Reporting breaks**:

- No Charges for third-party routed payments → switch to Payment Attempt Records
- No Balance Transactions for third-party volume (funds don't flow through Stripe)

**Webhook changes** for third-party routed payments:

- New `processing` status + `payment_intent.processing` event (useful for inventory holds)
- Then `succeeded` + `payment_intent.succeeded` (no change needed if already handling)

## Integration Limitations

- Setup Intents API: not supported
- Flexible acquiring features: not available on other processors
- 3DS: must provide Acquirer BIN for destination processor
- Dashboard: no balance summary, dispute status, or receipts for third-party; data up to 2 days lag

## Error Prevention Mode

When enabled: if the chosen processor doesn't support a required feature, Stripe auto-falls back. If Stripe also fails, retry processor is not attempted.

## Wallet Payments (Apple Pay / Google Pay)

Supported for routing to all three processors. Key constraint: **saved mobile wallet payment methods require `off_session=true`** during PaymentIntent confirmation. If the customer is present in the checkout flow, cannot reuse a saved wallet PM — must re-prompt using native Apple Pay/Google Pay integrations.

## Relationship to Other Products

- [[stripe-vault-and-forward]]: Forwards card data (PANs) to external processors. Orchestration routes *transactions*; Vault and Forward routes *card data*. Complementary.
- [[stripe-off-session-payments]]: Off-Session Payments API also supports multi-processor routing for recurring payments.

## Sources

- [[source-stripe-orchestration]] — overview: features, supported products, exclusions, processor-of-record rule
- [[source-stripe-orchestration-route-payments]] — implementation: API param, Payment Records, reporting/webhook changes, error prevention
- [[source-stripe-orchestration-rules]] — rule conditions (7), execution order, rule lifecycle
- [[source-stripe-orchestration-retries]] — cross-processor retry edge cases: 3DS, ineligible features, Radar blocks, Adaptive Acceptance
- [[source-stripe-orchestration-feature-support]] — feature matrix (Adyen/Braintree/Worldpay WPG), error code orchestration_unsupported, error protection opt-in
- [[source-stripe-orchestration-wallet-payments]] — Apple Pay/Google Pay routing; off_session=true for saved wallets; re-prompt required if customer present
