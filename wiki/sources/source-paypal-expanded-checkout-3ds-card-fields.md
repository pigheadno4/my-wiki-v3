---
title: "PayPal Expanded Checkout: Integrate 3D Secure using Card Fields"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-expanded-checkout-3ds-card-fields.md"
tags: [paypal, expanded-checkout, 3d-secure, card-fields, javascript-sdk, sca, liability-shift, psd2, europe]
---

## PayPal Expanded Checkout: Integrate 3D Secure using Card Fields

Official integration guide for enabling 3D Secure in the CardFields JS SDK integration.

Source URL: <https://developer.paypal.com/docs/checkout/advanced/customize/3d-secure/sdk/>

Last updated: 2025-05-13

## Key Takeaways

### Standard Checkout does NOT need this

> "If you have a standard checkout integration, you don't need to integrate 3D Secure. PayPal handles 3D secure authentication for standard checkout integrations."

This page applies only to **Expanded Checkout (CardFields)** — not Standard Checkout buttons.

### Integration pattern — `payment_source.card.attributes.verification`

3DS is configured on the **server-side** Create Order call, not in the JS SDK config:

```javascript
payment_source: {
    card: {
        attributes: {
            verification: {
                method: "SCA_ALWAYS"  // or "SCA_WHEN_REQUIRED"
            }
        },
        experience_context: {
            shipping_preference: "NO_SHIPPING",
            return_url: "https://example.com/returnUrl",
            cancel_url: "https://example.com/cancelUrl",
        }
    }
}
```

### `liabilityShift` in `onApprove`

After 3DS authentication, `onApprove` receives `liabilityShift` alongside `orderID`:

```javascript
onApprove: function(data) {
    const { liabilityShift, orderID } = data;
    if (liabilityShift) {
        // liability shifted to card issuer — handle accordingly
    }
}
```

### PSD2 compliance note

European merchants subject to PSD2 must:
1. Include 3D Secure
2. Pass the cardholder's **billing address** as part of transaction processing

### HostedFields uses a different guide

This page is CardFields (JS SDK v5). HostedFields (legacy v1) has a separate integration guide.

## Raw Sources

- [[paypal-expanded-checkout-3ds-card-fields]] — verbatim webpage content

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-expanded-checkout]] — Expanded Checkout concept page
- [[source-paypal-expanded-checkout-3d-secure]] — 3DS eligibility and country/card brand table
- [[source-paypal-expanded-checkout-integrate]] — base integration (also shows SCA_ALWAYS in server.js)
- [[source-paypal-javascript-sdk-reference]] — CardFields API reference
