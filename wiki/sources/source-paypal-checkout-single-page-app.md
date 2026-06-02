---
title: "PayPal Checkout: Single-Page Applications"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-checkout-single-page-app.md"
tags: [paypal, checkout, spa, react, vue, angular, javascript-sdk, framework-driver]
---

## PayPal Checkout: Single-Page Applications

Official PayPal guide for integrating PayPal Checkout into React, Vue, Angular (1.x), and Angular 2 / TypeScript SPAs using the `paypal.Buttons.driver()` API.

Source URL: <https://developer.paypal.com/docs/checkout/standard/customize/single-page-app/>

Last updated: 2025-05-09

## Key Takeaways

### Script tag: `defer` for SPAs

Use `defer` when buttons render after a route change or user interaction:

```html
<script defer src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID"></script>
```

Without `defer`, use the standard synchronous tag (for immediate render on page load). Choosing incorrectly causes `paypal is not defined` errors in SPA route transitions.

### Framework driver API

```javascript
paypal.Buttons.driver(framework, adapterObject)
```

| Framework | Call |
| --------- | ---- |
| React | `paypal.Buttons.driver("react", { React, ReactDOM })` |
| Angular 1.x | `paypal.Buttons.driver("angular", window.angular)` |
| Angular 2 | `paypal.Buttons.driver("angular2", ng.core)` |
| Vue | `paypal.Buttons.driver("vue", window.Vue)` |

### React: component vs functional

Both class-based and functional components are supported. The functional approach uses `computed` callbacks; the class approach uses `this.createOrder` / `this.onApprove` bound methods. The `createOrder` and `onApprove` logic is identical to the vanilla integration — just wired through JSX props.

### Vue: `style-object` naming gotcha

In Vue, pass button style as `:style-object` (or `:styleObject`) — **not** `:style` — to avoid conflict with Vue's reserved `style` prop. Passing `:style` will silently fail or cause unexpected behaviour.

### Vue: shipping callbacks included

The Vue sample includes `onShippingAddressChange` and `onShippingOptionsChange` as computed props, with example rejection logic (`COUNTRY_ERROR`, `STORE_UNAVAILABLE`). This is the only framework sample to show shipping callbacks.

### Partner headers

All framework samples include `PayPal-Partner-Attribution-Id` (BN code) and `PayPal-Auth-Assertion` headers in the `createOrder` fetch — these are partner/platform tracking headers not present in the basic integration guide.

## Raw Sources

- [[paypal-checkout-single-page-app]] — verbatim webpage content with full framework code samples

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-checkout]] — PayPal Checkout concept page
- [[source-paypal-checkout-customize-overview]] — full customization feature catalog
- [[source-paypal-checkout-integrate-one-time-payment]] — base integration this extends
