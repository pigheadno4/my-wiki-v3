---
title: "PayPal JavaScript SDK: Performance Optimization"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-javascript-sdk-performance.md"
tags: [paypal, javascript-sdk, performance, async-loading, render, pre-caching, spa, module]
---

## PayPal JavaScript SDK: Performance Optimization

Official PayPal guide for optimising SDK load time and button render speed — covering instant vs delayed render patterns, pre-caching, and module loading.

Source URL: <https://developer.paypal.com/sdk/js/performance/>

Last updated: 2025-12-17

## Key Takeaways

### Why self-hosting is not allowed

PayPal explicitly forbids bundling or self-hosting the SDK. The dynamic bundling from paypal.com is core to performance: the script is customised per client ID and buyer (only necessary code loaded), shared between parent page, iframe, and popup window via browser cache, and gets instant security/conversion updates.

### Two render patterns

| Scenario | Approach |
| -------- | -------- |
| Buttons shown immediately on page load | Synchronous script tag **before** container; call `render()` immediately after container |
| Buttons shown on user action / route change | Async script tag in `<head>`; call `render()` on the triggering event |

### Pre-caching trick (high impact)

Load the SDK async on a **preceding page** (landing page, product page) before the buyer reaches checkout. The browser caches it so checkout page load is near-instant:

```html
<!-- On a pre-checkout page -->
<script src="https://www.paypal.com/sdk/js?client-id=CLIENT_ID" async></script>
```

### Hidden container pattern (delayed render)

Render the button into a hidden container immediately on page load, then show it on user action. Eliminates the render delay at click time:

```javascript
document.querySelector('#paypal-button-container').style.display = 'none';
paypal.Buttons().render('#paypal-button-container');
// later:
document.querySelector('#paypal-button-container').style.display = 'block';
```

### Module loading (`paypal-js` / `react-paypal-js`)

- `@paypal/paypal-js` — async load + promise interface; best for front-end build tool setups
- `@paypal/react-paypal-js` — React-specific; ships `PayPalButtons`, `PayPalMarks`, `PayPalMessages` components

Both packages handle async loading best practices automatically.

## Raw Sources

- [[paypal-javascript-sdk-performance]] — verbatim webpage content

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[source-paypal-javascript-sdk-overview]] — SDK component overview
- [[source-paypal-javascript-sdk-configuration]] — script tag configuration reference
- [[source-paypal-checkout-single-page-app]] — SPA integration (uses `defer` for delayed render)
