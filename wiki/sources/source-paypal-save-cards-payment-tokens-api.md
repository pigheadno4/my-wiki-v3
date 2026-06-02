---
title: "Save Cards with the Payment Method Tokens API"
type: source
date_ingested: 2026-04-14
original_format: webpage
raw_files:
  - "paypal-save-cards-payment-tokens-api.md"
tags: [paypal, vault, card-payments, payment-tokens, setup-token, purchase-later, pci-dss, 3d-secure, smart-authorization, avs, cvv, orders-api]
---

## Overview

Server-side integration for saving credit/debit cards without a purchase using the Payment Method Tokens API directly. Raw card data passed in the setup token request — requires **PCI SAQ D compliance**. No client SDK involved.

Source URL: <https://developer.paypal.com/docs/checkout/save-payment-methods/purchase-later/payment-tokens-api/cards/>

Last updated: 2025-08-25

## Key Takeaways

### When to use

Save cards for later charging without a purchase. Common use: free trial → charge after expiry. PCI SAQ D required (raw card number + expiry in API request).

### Availability

35 countries — same as all other card vault integrations.

### Three setup token verification modes

| Mode | `verification_method` | Setup token status | What happens |
| --- | --- | --- | --- |
| No verification | (none) | `APPROVED` | Format check only; no auth |
| Smart authorization | `SCA_WHEN_REQUIRED` | `APPROVED` | Zero-value auth (or minimal hold if unsupported); returns `VERIFIED` + AVS/CVV codes |
| 3D Secure | `SCA_WHEN_REQUIRED` or `SCA_ALWAYS` | `PAYER_ACTION_REQUIRED` | Payer redirected to approve → GET setup token → `APPROVED` with `three_d_secure` block |

### Setup token request (card with billing address)

```json
{
  "payment_source": {
    "card": {
      "number": "4111111111111111",
      "expiry": "2027-02",
      "name": "Firstname Lastname",
      "billing_address": { ... },
      "verification_method": "SCA_WHEN_REQUIRED",
      "experience_context": {
        "brand_name": "YourBrandName",
        "locale": "en-US",
        "return_url": "https://example.com/returnUrl",
        "cancel_url": "https://example.com/cancelUrl"
      }
    }
  }
}
```

Note: `experience_context` with `brand_name`/`locale` on a card setup token — unusual (typically used for PayPal payment sources).

### Smart authorization detail

- Zero-value auth where supported by issuing bank
- If not supported: minimal amount authorization — **not automatically voided**, creates temporary hold
- Returns `verification_status: VERIFIED` + AVS/CVV codes in response

### 3D Secure detail

- `PAYER_ACTION_REQUIRED` → payer follows `approve` HATEOAS link
- After approval: GET `setup-tokens/{id}` → returns `APPROVED` with full `three_d_secure` block:
  - `eci_flag`, `enrolled`, `pares_status`, `three_ds_version`, `authentication_type`, `three_ds_server_transaction_id`
- Failed AVS/CVV doesn't prevent vault — issuing bank may still authorize; `eci_flag` indicates 3DS completion

### Returning payer

Pass `customer.id` in setup token request to link additional cards to an existing customer.

### Subsequent payment (payer present)

```json
{
  "payment_source": {
    "card": {
      "vault_id": "dnbbj3g"
    }
  }
}
```

### Off-session charge (payer not present)

1. `GET /v3/vault/payment-tokens?customer_id=CUSTOMER-ID` → retrieve token
2. Create order with `payment_source.card.vault_id`

### AVS test codes (sandbox — set Address Line 1)

| Address Line 1 | AVS Code | Visa | MC | Amex | Discover |
| --- | --- | --- | --- | --- | --- |
| AVS_A_971 | A | Yes | Yes | Yes | Yes |
| AVS_N_984 | N | Yes | Yes | Yes | Yes |
| AVS_Y_995 | Y | Yes | Yes | Yes | Yes |
| AVS_Z_996 | Z | Yes | Yes | Yes | Yes |
| (21 total codes — see raw file for complete table) | | | | | |

### CVV test codes (sandbox)

| CVV | Response | Meaning |
| --- | --- | --- |
| 115 | M | Match |
| 116 | N | No Match |
| 120 | P | Not Processed |
| 123 | S | Should be on card but not provided |
| 125 | U | Unknown/Issuer not participating |
| 130 | X | Provider did not respond (default) |

### Webhooks

Same 3 events as Orders API PayPal vault guide:
- `VAULT.PAYMENT-TOKEN.CREATED` — Cards and PayPal
- `VAULT.PAYMENT-TOKEN.DELETED` — Cards and PayPal
- `VAULT.PAYMENT-TOKEN.DELETION-INITIATED` — PayPal only

### Next steps

- RTAU (real-time account updater) — keep saved cards current

## Raw Sources

- [[paypal-save-cards-payment-tokens-api]] — verbatim integration guide with full AVS/CVV tables and 3DS response objects

## Relevant Wiki Pages

- [[paypal-vault]] — Vault concept: setup token → payment token flow
- [[source-paypal-save-cards-purchase-later-js-sdk]] — JS SDK equivalent (SAQ A, CardFields)
- [[source-paypal-save-cards-orders-api]] — Orders API card vault during purchase (also SAQ D)
- [[source-paypal-3ds-test-scenarios]] — 3D Secure test cards for sandbox testing
