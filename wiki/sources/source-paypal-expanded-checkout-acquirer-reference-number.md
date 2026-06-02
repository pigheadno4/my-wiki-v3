---
title: "PayPal Expanded Checkout: Acquirer Reference Number (ARN)"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-expanded-checkout-acquirer-reference-number.md"
tags: [paypal, expanded-checkout, arn, acquirer-reference-number, refund, capture, orders-api, payments-api, tracking]
---

## PayPal Expanded Checkout: Acquirer Reference Number (ARN)

Guide for retrieving the ARN — a unique transaction identifier assigned by the acquiring bank, useful for tracing refunds when a customer's card has changed.

Source URL: <https://developer.paypal.com/docs/checkout/advanced/customize/acquirer-reference-number/>

Last updated: 2025-05-09

## Key Takeaways

### What the ARN is for

- Assigned after a card transaction is processed
- Lets card brands, issuers, and processors trace the transaction
- Customers use it to confirm refunds were processed
- Critical when a card is lost/stolen/closed: helps the bank route the refund correctly

### Availability

US, UK, Canada, Australia, EU — credit/debit cards including digital wallets.

Requires Expanded Checkout integration (not Standard Checkout).

### ARN is not immediate

> "After you capture a payment or refund a transaction, the ARN is available after a few days."

Don't try to retrieve it immediately after capture/refund.

### Three endpoints and ARN location

| Endpoint | ARN field path |
| -------- | -------------- |
| `GET /v2/checkout/orders/{id}?fields=payment_source` | `purchase_units[].payments.captures[].network_transaction_reference.acquirer_reference_number` |
| `GET /v2/checkout/orders/{id}?fields=payment_source` (refund) | `purchase_units[].payments.refunds[].acquirer_reference_number` |
| `GET /v2/payments/captures/{id}` | `network_transaction_reference.acquirer_reference_number` |
| `GET /v2/payments/refunds/{id}` | `acquirer_reference_number` (top level) |

Note: ARN path differs between captures (nested under `network_transaction_reference`) and refunds (top-level field).

## Raw Sources

- [[paypal-expanded-checkout-acquirer-reference-number]] — verbatim webpage content with full sample responses

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-expanded-checkout]] — Expanded Checkout concept page
- [[source-paypal-expanded-checkout-customize-overview]] — full customization catalog
- [[source-paypal-checkout-authorize-and-capture]] — capture flow context
