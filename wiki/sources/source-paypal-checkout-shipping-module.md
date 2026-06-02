---
title: "PayPal Checkout: Shipping Module"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-checkout-shipping-module.md"
tags: [paypal, checkout, venmo, shipping, shipping-callbacks, server-side-callbacks, orders-api, shipping-preference, callback-events]
---

## PayPal Checkout: Shipping Module

Official PayPal reference for the shipping module — server-side shipping callbacks for both PayPal and Venmo, shipping preferences, callback request/response schemas, and decline error codes.

Source URL: <https://developer.paypal.com/docs/checkout/standard/customize/shipping-module/>

Last updated: 2026-03-09

## Key Takeaways

### Server-side vs client-side callbacks

**Server-side recommended** over client-side because:
- Client-side (JS SDK) is **incompatible with Venmo**
- Client-side not suitable for native mobile apps

### Three shipping preferences

| `shipping_preference` | Buyer can change address? | Callbacks fire? | Notes |
| --------------------- | ------------------------- | --------------- | ----- |
| `GET_FROM_FILE` (default) | Yes | Yes | Uses wallet address; buyer can change |
| `NO_SHIPPING` | N/A | No | Removes shipping from review page; still returns `phone_number`/`email_address` for digital goods |
| `SET_PROVIDED_ADDRESS` | No | No | Locks to merchant-provided address |

### Two callback events

- `SHIPPING_ADDRESS` — fires on page load + address change. **Recommended sole subscription** — return all options upfront, avoids need for `SHIPPING_OPTIONS` callback.
- `SHIPPING_OPTIONS` — fires when buyer selects/changes a shipping option. Subscribe only if you need to recalculate on option change.

### Callback URL tip

Embed cart identifier in the callback URL (`?cart_id=...&session_id=...`) if you can't associate the shopping cart with the order ID from the callback body alone.

### Initial callback gotcha

The **first callback does NOT include `shipping_option`** — only `shipping_address` and `purchase_units`. Only subsequent callbacks (when buyer changes option) include `shipping_option`.

### Merchant success response — amount consistency rules

All of these must hold or PayPal will reject:
1. `breakdown.shipping.value` = selected shipping option's `amount.value`
2. `amount.value` = sum of all breakdown fields
3. `breakdown.item_total` and `breakdown.tax_total` = Order/Cart values
4. All `currency_code` values must match throughout

### Decline response — supported error codes

| Event | Code | Buyer-facing message |
| ----- | ---- | -------------------- |
| Address | `ADDRESS_ERROR` | Can't ship to this address |
| Address | `COUNTRY_ERROR` | Can't ship to this country |
| Address | `STATE_ERROR` | Can't ship to this state |
| Address | `ZIP_ERROR` | Can't ship to this zip |
| Option | `METHOD_UNAVAILABLE` | Shipping method unavailable |
| Option | `STORE_UNAVAILABLE` | Part of order unavailable at this store |

### Venmo support

Identical integration to PayPal — just swap `payment_source.paypal` → `payment_source.venmo`. Full parity for the shipping module.

## Images

- `raw/assets/paypal-shipping-module-review-page.png` — PayPal and Venmo review pages showing shipping address and options module (1.1MB)

## Raw Sources

- [[paypal-checkout-shipping-module]] — verbatim webpage content + downloaded image

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-checkout]] — PayPal Checkout concept page
- [[source-paypal-checkout-integrate-server-side-shipping]] — earlier source with `orderUpdateCallbackConfig` in context of the integrate guide
- [[source-paypal-checkout-customize-overview]] — full customization feature catalog
- [[source-paypal-best-practices-one-time-payment]] — references shipping callbacks as required for physical goods
