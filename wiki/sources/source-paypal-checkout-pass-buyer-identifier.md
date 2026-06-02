---
title: "PayPal Checkout: Pass Buyer Identifier"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-checkout-pass-buyer-identifier.md"
tags: [paypal, checkout, buyer-identifier, email, prefill, login, orders-api, experience-context]
---

## PayPal Checkout: Pass Buyer Identifier

Official PayPal guide for passing a buyer's email address in the Create Order request to prefill the PayPal login page and streamline authentication.

Source URL: <https://developer.paypal.com/docs/checkout/standard/customize/pass-buyer-identifier/>

Last updated: 2025-02-16

## Key Takeaways

### What it does

Passing `payment_source.paypal.email_address` in Create Order causes PayPal to pre-populate the buyer's login page with that email — fewer keystrokes, faster authentication, higher conversion.

### Implementation

One field addition to the standard Create Order request body:

```json
"payment_source": {
    "paypal": {
        "email_address": "customer@example.com",
        "experience_context": { ... }
    }
}
```

No other changes required.

### When to use

- Merchant site already collected the buyer's email (e.g. account login, checkout form)
- Recurring payments setup — pass email at setup token creation too
- Recommended in best practices guides for both one-time and recurring flows

## Raw Sources

- [[paypal-checkout-pass-buyer-identifier]] — verbatim webpage content

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-checkout]] — PayPal Checkout concept page
- [[source-paypal-checkout-customize-overview]] — full customization feature catalog
- [[source-paypal-best-practices-one-time-payment]] — references this as a recommended optimisation
- [[source-paypal-best-practices-recurring-payment]] — also recommends passing email at order creation
