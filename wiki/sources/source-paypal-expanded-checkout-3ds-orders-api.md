---
title: "PayPal Expanded Checkout: 3D Secure via Orders API"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-expanded-checkout-3ds-orders-api.md"
tags: [paypal, expanded-checkout, 3d-secure, orders-api, sca, liability-shift, hateoas, payer-action, psd2, contingency]
---

## PayPal Expanded Checkout: 3D Secure via Orders API

Server-side (Orders API) approach to 3D Secure — distinct from the JS SDK CardFields approach. Used for direct API integrations without the JS SDK.

Source URL: <https://developer.paypal.com/docs/checkout/advanced/customize/3d-secure/api/>

Last updated: 2025-05-12

## Key Takeaways

### Orders API vs CardFields 3DS — two separate flows

| Approach | Where 3DS config goes | Authentication trigger |
| -------- | --------------------- | ---------------------- |
| **CardFields (JS SDK)** | `payment_source.card.attributes.verification` in `createOrder` | SDK handles pop-up/redirect |
| **Orders API (this page)** | `payment_source.card.attributes.verification` on authorize/capture call | Merchant redirects buyer to `payer-action` HATEOAS link |

### `SCA_WHEN_REQUIRED` is the default

If neither `SCA_ALWAYS` nor `SCA_WHEN_REQUIRED` is passed, `SCA_WHEN_REQUIRED` is used automatically.

### HATEOAS-driven flow

1. Call authorize or capture with card + `verification.method`
2. Receive HTTP 422 (multi-step) or 3DS contingency in create order (single-step)
3. Redirect buyer to `"rel": "payer-action"` link from response, appending `redirect_uri`
4. Buyer completes 3DS with their bank
5. Call `GET /v2/checkout/orders/{id}?fields=payment_source` to check `authentication_result`
6. Re-call authorize/capture with **empty payload** to complete transaction

### Authentication result structure

```json
"authentication_result": {
    "liability_shift": "POSSIBLE",
    "three_d_secure": {
        "enrollment_status": "Y",
        "authentication_status": "Y"
    }
}
```

### Step result codes

| Request type | HTTP result |
| ------------ | ----------- |
| Single-step (3DS contingency in create order) | 201 Created |
| Multi-step (3DS contingency in authorize/capture) | 422 Unprocessable Entity |
| Confirm order (after 3DS resolved) | 200 OK |

### Empty payload for final capture/authorize

After 3DS is resolved, the final authorize or capture call uses an **empty payload** — the verification is already associated with the order.

### PSD2 requirement

European merchants must pass the cardholder's `billing_address` in the card object alongside the verification method.

## Raw Sources

- [[paypal-expanded-checkout-3ds-orders-api]] — verbatim webpage content

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-expanded-checkout]] — Expanded Checkout concept page
- [[source-paypal-expanded-checkout-3d-secure]] — 3DS eligibility and country table
- [[source-paypal-expanded-checkout-3ds-card-fields]] — CardFields (JS SDK) approach to 3DS
- [[source-paypal-checkout-authorize-and-capture]] — authorize/capture flow context
