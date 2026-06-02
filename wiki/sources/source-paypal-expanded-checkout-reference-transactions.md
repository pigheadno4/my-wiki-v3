---
title: "PayPal Expanded Checkout: Initiate Future Transactions (Reference Transactions)"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-expanded-checkout-reference-transactions.md"
tags: [paypal, expanded-checkout, reference-transactions, website-payments-pro, orders-api, paypal-transaction-id, pnref, payflow, future-payments]
---

## PayPal Expanded Checkout: Initiate Future Transactions (Reference Transactions)

Integration guide for reference transactions — using a buyer's previous PayPal transaction ID to initiate future charges without buyer re-authentication. Available to Website Payments Pro merchants only.

Source URL: <https://developer.paypal.com/docs/checkout/advanced/customize/reference-transactions/>

Last updated: 2025-08-11

## Key Takeaways

### What it is

A reference transaction uses a buyer's original transaction ID (from a prior purchase) as the `payment_source` to create and capture future orders — no buyer re-authentication needed. Requires an established contract with the payer.

> **Important:** Reference transactions are available only to **Website Payments Pro** merchants using Expanded Checkout. Not available to standard merchants.

### Two token types

| Type | When to use |
| ---- | ----------- |
| `PAYPAL_TRANSACTION_ID` | Previous transaction was processed through PayPal Orders/REST API |
| `PNREF` | Previous transaction was processed through Payflow (NVP/SOAP legacy integration) |

Both types are passed identically via `payment_source.token`:

```json
"payment_source": {
  "token": {
    "id": "67N9717781765035V",
    "type": "PAYPAL_TRANSACTION_ID"
  }
}
```

### 3-step flow

1. **Create order** — `POST /v2/checkout/orders` with `intent: CAPTURE` → get `ORDER-ID`
2. **Authorize** — `POST /v2/checkout/orders/{ORDER-ID}/authorize` with `payment_source.token` (previous TX ID)
3. **Capture** — `POST /v2/checkout/orders/{ORDER-ID}/capture` with same `payment_source.token`

Note: Can also do authorize-only (change `intent` to `AUTHORIZE`) and capture separately.

### Idempotency on capture

Pass `PayPal-Request-ID` header on the capture call — prevents duplicate captures if the network call is disrupted.

### NVP/SOAP alternative

For merchants on legacy NVP/SOAP integrations, reference transactions can also be obtained via the `DoReferenceTransaction` API (not Orders v2).

### Contrast with third-party network tokens

Third-party network token processing (`payment_source.card.network_token`) explicitly **does not support** reference or future transactions. Reference transactions use `payment_source.token` with a prior PayPal TX ID — a completely different mechanism.

## Raw Sources

- [[paypal-expanded-checkout-reference-transactions]] — verbatim webpage content with create/authorize/capture curl samples for both PAYPAL_TRANSACTION_ID and PNREF

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-expanded-checkout]] — Expanded Checkout concept page
- [[paypal-vault]] — vault/payment tokens (alternative stored credential approach for non-WPP merchants)
- [[source-paypal-expanded-checkout-3rd-party-token-processing]] — third-party network tokens (explicitly excludes reference transactions)
- [[source-paypal-expanded-checkout-sca-payment-indicators]] — stored_credential (related: merchant-initiated charges)
