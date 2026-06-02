---
title: "PayPal: Save Payment Method for Future Payments"
type: source
date_ingested: 2026-04-17
original_format: webpage
raw_files:
  - "paypal-save-payment-method.md"
  - "paypal-save-without-purchase-sdk-v6.md"
tags: [paypal, vault, recurring-payments, payment-tokens, orders-api, vault-without-payment]
---

## Summary

Integration guide for saving a customer's PayPal account for future charges without requiring approval each time. Uses the vault feature in **Orders API v2** via `payment_source.paypal.attributes.vault`. Customer approves once; subsequent charges are server-side only using a stored payment token.

## Key takeaways

### 3-step vault flow

**Step 1 — Create order with vault enabled:**

```json
{
  "payment_source": {
    "paypal": {
      "attributes": {
        "vault": {
          "store_in_vault": "ON_SUCCESS",
          "usage_type": "MERCHANT",
          "customer_type": "CONSUMER"
        }
      }
    }
  }
}
```

**Step 2 — After capture, extract and store the token:**

- Token path: `capture.payment_source.paypal.attributes.vault.id`
- Store securely in database linked to the customer

**Step 3 — Future charges (no customer present):**

```json
{
  "payment_source": {
    "token": {
      "id": "<stored_token>",
      "type": "PAYMENT_METHOD_TOKEN"
    }
  }
}
```

## Prerequisites

- Secure database to store payment tokens
- Mechanism to collect and record customer consent

## Use cases

- Subscription renewals
- On-demand services billed after usage
- Automatic bill payments
- One-click purchases for returning customers

## Related pages

- [[paypal-vault]] — PayPal Vault concept page
- [[recurring-payments]] — Generic recurring payments concept
- [[source-paypal-checkout-recurring-payment]] — Earlier vault integration guide (developer.paypal.com)
- [[source-paypal-payments-quickstart]] — Base integration

## Raw Sources

- [[paypal-save-payment-method]] — verbatim save payment method integration guide
- [[paypal-save-without-purchase-sdk-v6]] — VAULT_WITHOUT_PAYMENT flow: clientToken auth, createPayPalSavePaymentSession, setup token → payment token (server-side only), IMMEDIATE vs DEFERRED usage patterns, TypeScript server SDK
