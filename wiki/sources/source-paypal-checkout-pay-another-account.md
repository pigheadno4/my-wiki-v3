---
title: "PayPal Checkout: Pay Another Account"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-checkout-pay-another-account.md"
tags: [paypal, checkout, payee, marketplace, orders-api, split-payment]
---

## PayPal Checkout: Pay Another Account

Official PayPal guide for routing a payment to a different PayPal account (not the app owner's) by specifying a `payee` in the Create Order request.

Source URL: <https://developer.paypal.com/docs/checkout/standard/customize/pay-another-account/>

Last updated: 2024-04-19

## Key Takeaways

### Default behaviour

By default, funds go to the application owner's PayPal account.

### Override with `payee`

Add a `payee` object inside any `purchase_units[]` entry and specify either:
- `email_address` — the payee's PayPal email
- `merchant_id` — the payee's PayPal merchant ID

```json
"purchase_units": [{
    "amount": { "value": "15.00", "currency_code": "USD" },
    "payee": {
        "email_address": "payee@example.com"
    }
}]
```

### Use cases

Marketplace platforms routing payments to sellers; split checkouts where the platform takes a fee and routes the remainder to a third party.

## Raw Sources

- [[paypal-checkout-pay-another-account]] — verbatim webpage content

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-checkout]] — PayPal Checkout concept page
- [[source-paypal-checkout-customize-overview]] — full customization feature catalog
