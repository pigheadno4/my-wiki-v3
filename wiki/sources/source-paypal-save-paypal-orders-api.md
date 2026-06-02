---
title: "Save PayPal with the Orders API"
type: source
date_ingested: 2026-04-14
original_format: webpage
raw_files:
  - "paypal-save-paypal-orders-api.md"
tags: [paypal, vault, orders-api, save-payment-methods, payment-tokens, reference-transactions, webhooks]
---

## Overview

Integration guide for saving PayPal Wallets during purchase using the Orders API directly (no client SDK). Targets merchants who are PCI compliant or have opted out of a PayPal client-side SDK.

Source URL: <https://developer.paypal.com/docs/checkout/save-payment-methods/during-purchase/orders-api/paypal/>

Last updated: 2025-05-13

## Key Takeaways

### When to use this path

- PCI compliant and capturing/passing card info directly
- Opted out of a client-side PayPal JS SDK
- **Reference transaction approval required** — must contact account manager; not self-serve

### Availability

35 countries — same as all other PayPal Wallet vault integrations. No Venmo support.

### Flow (two-step — unlike cards Orders API)

1. Create order → response: `status: PAYER_ACTION_REQUIRED`
2. Return order `id` to client → redirect payer to `approve` link
3. Payer approves PayPal Wallet vault
4. Server captures/authorizes → response contains `vault.id` + `customer.id`

### Create Order payload

```json
{
  "intent": "CAPTURE",
  "payment_source": {
    "paypal": {
      "attributes": {
        "vault": {
          "store_in_vault": "ON_SUCCESS",
          "usage_type": "MERCHANT"
        }
      },
      "experience_context": {
        "return_url": "https://example.com/returnUrl",
        "cancel_url": "https://example.com/cancelUrl"
      }
    }
  }
}
```

Key differences from JS SDK PayPal vault payload:
- `experience_context` with `return_url`/`cancel_url` required (JS SDK uses `data-user-id-token` instead)
- `customer_type` field absent (JS SDK includes `customer_type: CONSUMER`)

### Vault webhooks (unique to this page)

| Webhook | Trigger | Payment methods |
| --- | --- | --- |
| `VAULT.PAYMENT-TOKEN.CREATED` | Payment token created | Cards and PayPal |
| `VAULT.PAYMENT-TOKEN.DELETED` | Payment token deleted | Cards and PayPal |
| `VAULT.PAYMENT-TOKEN.DELETION-INITIATED` | Delete request submitted to Payment Method Tokens API | PayPal only |

`VAULT.PAYMENT-TOKEN.DELETION-INITIATED` is documented only on this page — not mentioned in other vault guides.

### APPROVED vs VAULTED

Same pattern as all other integrations — subscribe to `VAULT.PAYMENT-TOKEN.CREATED` webhook if `vault.status: APPROVED`.

> [!info] Doc typo
> The capture response sample uses `"id" = "ROaPMoZUaV"` (with `=` instead of `:`). Same typo appears in the cards Orders API guide — likely a copy-paste error in PayPal's docs.

## Raw Sources

- [[paypal-save-paypal-orders-api]] — verbatim integration guide

## Relevant Wiki Pages

- [[paypal-vault]] — Vault concept: token types, APPROVED/VAULTED, webhook
- [[source-paypal-save-cards-orders-api]] — Cards Orders API equivalent (SAQ D, single-step capture)
- [[source-paypal-save-paypal-js-sdk]] — JS SDK equivalent for PayPal Wallet vault
