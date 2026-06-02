---
title: "Save Apple Pay with the JavaScript SDK"
type: source
date_ingested: 2026-04-14
original_format: webpage
raw_files:
  - "paypal-save-applepay-js-sdk.md"
tags: [paypal, apple-pay, vault, save-payment-methods, recurring-payments, orders-api, webhook, platform]
---

## Overview

Integration guide for saving Apple Pay as a payment method during purchase via the PayPal JavaScript SDK and Orders v2 API, enabling merchants to make recurring payments without the payer being present.

Source URL: <https://developer.paypal.com/docs/checkout/save-payment-methods/during-purchase/js-sdk/applepay/>

Last updated: 2025-11-27

## Key Takeaways

### Critical Apple Pay vault limitation

> [!warning] Apple Pay cannot be used for returning buyer checkout
> Per Apple guidelines, **Apple Pay cannot be shown as a saved payment option for returning buyers at checkout**. Vaulted Apple Pay is for **merchant-initiated recurring charges only** — not for buyer-selected one-click checkout.

### How it works

1. Payer opts in to save Apple Pay during checkout
2. PayPal creates a customer record after first successful transaction, encrypts and stores the payment method
3. PayPal generates a `customer.id` — merchant must store this for future use
4. Merchant uses `vault_id` for subsequent merchant-initiated recurring charges (payer not present)

### Key API fields for saving

**First-time save** (no existing customer):
```json
"payment_source": {
  "apple_pay": {
    "stored_credential": {
      "payment_initiator": "CUSTOMER",
      "payment_type": "RECURRING"
    },
    "attributes": {
      "vault": { "store_in_vault": "ON_SUCCESS" }
    }
  }
}
```

**Returning payer** (link to existing `customer.id`):
```json
"attributes": {
  "customer": { "id": "PayPal-generated customer id" },
  "vault": { "store_in_vault": "ON_SUCCESS" }
}
```

**Merchant-initiated recurring** (payer not present):
```json
"payment_source": {
  "apple_pay": {
    "stored_credential": {
      "payment_initiator": "MERCHANT",
      "payment_type": "RECURRING",
      "usage": "SUBSEQUENT"
    },
    "vault_id": "nkq2y9g"
  }
}
```

### vault.status: APPROVED vs VAULTED

The Orders API responds immediately after capture — vaulting may not be complete yet:

| Status | Meaning | `vault_id` available? |
| --- | --- | --- |
| `VAULTED` | Payment method saved | Yes |
| `APPROVED` | Approved to be saved, saving in progress | No — subscribe to webhook |

If `APPROVED` is returned, subscribe to `VAULT.PAYMENT-TOKEN.CREATED` webhook to receive the `vault_id` asynchronously. The `resource.id` in the webhook payload is the vault ID; `resource.customer.id` is the PayPal-generated customer ID.

### JS SDK limitation

> [!info]
> The JavaScript SDK has **no direct support to show saved payments**. Merchants must build their own UI using the Payment Method Tokens v3 API to list saved methods.

### Platform considerations

- `PayPal-Partner-Attribution-Id` header: pass partner BN code for reporting/tracking
- `PayPal-Auth-Assertion` header: assign saved payment ownership to merchant (not platform)

### Go live — manual Apple Pay onboarding required

1. Account Settings → Payment Method → Enable Apple Pay → Get Started
2. Submit Profile collection details
3. Status flow: "under review" → Denied / Need more information / **Success**

Approval may be instant or require manual review.

### Delete a saved token

```curl
DELETE https://api-m.sandbox.paypal.com/v3/vault/payment-tokens/{vault_id}
```

## Raw Sources

- [[paypal-save-applepay-js-sdk]] — full integration guide with all curl/JSON request+response samples, webhook payload, platform headers, go-live onboarding steps

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-vault]] — Vault concept: token types, APPROVED vs VAULTED status pattern
- [[paypal-expanded-checkout]] — Expanded Checkout approval required for card/APM vaulting
- [[source-paypal-save-payment-methods]] — Save payment methods overview and integration path table
