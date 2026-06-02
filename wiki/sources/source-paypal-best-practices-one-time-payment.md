---
title: "Pay with PayPal for One-time Payments: Best Practices"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-best-practices-one-time-payment.md"
tags: [paypal, checkout, best-practices, one-time-payment, ux, conversion, button-placement, shipping-callbacks, pay-now, app-switch]
---

## Pay with PayPal for One-time Payments: Best Practices

Official PayPal guide covering UX and integration best practices for one-time payment flows — button placement, shipping callbacks, login optimisation, and the PayPal review page.

Source URL: <https://developer.paypal.com/docs/checkout/standard/best-practices/one-time/>

Last updated: 2025-09-17

## Key Takeaways

### Two button placement contexts

PayPal distinguishes two modes with different rules:

| Context | When | Key rule |
| ------- | ---- | -------- |
| **Upstream** | Cart, PDP — before buyer enters any data | Pass shipping options callback; merchant receives buyer's address from PayPal |
| **Checkout** | After buyer has manually entered shipping info | Pass address in Create Order; set `shipping_preference: SET_PROVIDED_ADDRESS` |

### Upstream placement best practices

- Place PayPal button **before any other checkout flow requiring data entry** (User Agreement requirement)
- Treat PayPal/Venmo equally to other payment methods — no earlier in flow, same logo placement and fees
- Add **Pay Later messaging** near the order total
- Pass `data-page-type` in the JS SDK script tag to help PayPal optimise button behaviour per page type
- **Always integrate shipping options callback** for physical goods, even if only one shipping method is available — without it, PayPal can't show delivery options and buyer must return to the merchant site

### Checkout placement best practices

- Detect PayPal users and **proactively pre-select PayPal** to reduce decision fatigue
- PayPal button click = buyer's **last action** on merchant site
- After PayPal approval → redirect to order success page (no more merchant-side steps)
- Set `shipping_preference: SET_PROVIDED_ADDRESS` to lock the address the buyer already entered

### PayPal login / loading page

- If you have the buyer's email, **pass it in the Create Order call** (via Pass buyer identifier API) to prefill the login page
- Never present PayPal in an **iframe** — must be full height in web view

### PayPal review page (Checkout experience)

- Use **Pay Now** button (not "Continue") so checkout completes inside PayPal — buyer returns to order success page
- Create the order when buyer taps Pay Now (not before)
- Pass **line items and SKU details** in the Create Order request — improves transparency, reduces disputes
- For upstream flows: include all supported shipping options and use shipping callbacks to recalculate cost + taxes based on selected address
- Implement **App Switch** to redirect mobile buyers to the PayPal app for faster authentication

### Pay Now flow (diagram)

See `raw/assets/paypal-best-practices-one-time-pay-now-flow.png` — diagram showing the full Pay Now flow from button click to order success.

### Compliance requirement

> Per PayPal's User Agreement: PayPal and Venmo must be treated equally to other payment methods — same logo placement, payment flow, and fees. PayPal must appear **at least as early** as other payment options; never present another payment method earlier in the flow.

## Images

- `raw/assets/paypal-best-practices-one-time-overview.png` — 4-screen end-to-end one-click checkout flow
- `raw/assets/paypal-best-practices-one-time-placement-cart.png` — cart page button placement example
- `raw/assets/paypal-best-practices-one-time-placement-pdp.png` — product detail page button placement example
- `raw/assets/paypal-best-practices-one-time-checkout-page.png` — merchant checkout page with PayPal button
- `raw/assets/paypal-best-practices-one-time-loading-page.png` — PayPal login/loading page example
- `raw/assets/paypal-best-practices-one-time-paysheet.png` — PayPal review/paysheet page example
- `raw/assets/paypal-best-practices-one-time-pay-now-flow.png` — Pay Now flow diagram

## Raw Sources

- [[paypal-best-practices-one-time-payment]] — verbatim webpage content + downloaded images

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-checkout]] — PayPal Checkout concept page
- [[source-paypal-best-practices-pay-with-paypal]] — parent best practices overview page
- [[source-paypal-checkout-integrate-one-time-payment]] — technical integration guide
