---
title: "Save PayPal with the Payment Method Tokens API"
type: source
date_ingested: 2026-04-14
original_format: webpage
raw_files:
  - "paypal-save-paypal-payment-tokens-api.md"
tags: [paypal, vault, payment-tokens, setup-token, purchase-later, billing-agreements, orders-api, webhooks]
---

## Overview

Server-side integration for saving PayPal Wallets without a purchase using the Payment Method Tokens API directly. No client SDK involved. Requires **billing agreement / reference transaction approval** from account manager.

Source URL: <https://developer.paypal.com/docs/checkout/save-payment-methods/purchase-later/payment-tokens-api/paypal/>

Last updated: 2025-08-25

## Key Takeaways

### Prerequisites

- Approved and configured for billing agreements / reference transactions — contact account manager
- No SAQ D required (unlike card Payment Method Tokens API)

### Availability

35 countries — same as all other PayPal Wallet vault integrations.

### Flow

1. Server: `POST /v3/vault/setup-tokens` with `payment_source.paypal` → `PAYER_ACTION_REQUIRED`
2. Payer follows `approve` HATEOAS link (PayPal-hosted approval flow for billing agreement)
3. Server: `POST /v3/vault/payment-tokens` with approved setup token → payment token + `customer.id`
4. Store both; use `vault_id` in Orders API for future charges

### Setup token request — richest PayPal payload documented

```json
{
  "payment_source": {
    "paypal": {
      "description": "Description for PayPal to be shown to PayPal payer",
      "shipping": { ... },
      "permit_multiple_payment_tokens": false,
      "usage_pattern": "IMMEDIATE",
      "usage_type": "MERCHANT",
      "customer_type": "CONSUMER",
      "experience_context": {
        "shipping_preference": "SET_PROVIDED_ADDRESS",
        "payment_method_preference": "IMMEDIATE_PAYMENT_REQUIRED",
        "brand_name": "EXAMPLE INC",
        "locale": "en-US",
        "return_url": "https://example.com/returnUrl",
        "cancel_url": "https://example.com/cancelUrl"
      }
    }
  }
}
```

New fields not seen in other PayPal vault guides:
- `shipping_preference: SET_PROVIDED_ADDRESS`
- `payment_method_preference: IMMEDIATE_PAYMENT_REQUIRED`
- `description` (payer-visible)

**Setup token expires after 3 days** — explicitly documented here.

**Merchant Customer ID**: optional field in setup/payment token requests to map PayPal customer ID to merchant's internal system.

### `usage_type: MERCHANT` — consistent with during-purchase

Unlike mobile purchase-later guides which use `PLATFORM`, this server-side guide uses `MERCHANT` — same as during-purchase flows.

### Subsequent payment (payer present)

```json
{
  "payment_source": {
    "paypal": {
      "vault_id": "jwgvx42"
    }
  }
}
```

### Off-session charge (payer not present)

1. `GET /v3/vault/payment-tokens?customer_id=CUSTOMER-ID`
2. Create order with `payment_source.paypal.vault_id` + `PayPal-Client-Metadata-Id` header

Note: `PayPal-Client-Metadata-Id` header appears only in the off-session order request — not in payer-present flow.

### Webhooks

Same 3 events as all other vault guides:
- `VAULT.PAYMENT-TOKEN.CREATED` — Cards and PayPal
- `VAULT.PAYMENT-TOKEN.DELETED` — Cards and PayPal
- `VAULT.PAYMENT-TOKEN.DELETION-INITIATED` — PayPal only

## Raw Sources

- [[paypal-save-paypal-payment-tokens-api]] — verbatim integration guide

## Relevant Wiki Pages

- [[paypal-vault]] — Vault concept: setup token → payment token flow
- [[source-paypal-save-cards-payment-tokens-api]] — Cards equivalent (SAQ D, 3 verification modes)
- [[source-paypal-save-paypal-orders-api]] — Orders API PayPal vault during purchase (also requires reference transaction approval)
