---
title: "PayPal: Troubleshoot Common Integration Issues"
type: source
date_ingested: 2026-04-17
original_format: webpage
raw_files:
  - "paypal-troubleshoot.md"
tags: [paypal, javascript-sdk, troubleshooting, sdk-v6, multipage]
---

## Summary

Troubleshooting guide for common PayPal JS SDK v6 integration issues. Covers basic setup errors and a detailed section on multipage/modular app scoping problems.

## Basic errors

| Error | Cause | Fix |
| --- | --- | --- |
| Button doesn't appear | Client ID mismatch between HTML and `.env` | Match credentials; sandbox for dev, production for live |
| 404 Page Not Found | `index.html` not in `public/` folder | Move file to `public/` |
| Invalid Client | Sandbox/production credential mix | Ensure both client ID and secret are from the same environment |

## Multipage / modular app issues

All caused by the same root issue: `window.paypalSdkInstance` not accessible where needed.

### Fix 1 — Expose instance globally in `onLoad()`

```js
async function onLoad() {
  const sdkInstance = await window.paypal.createInstance({...});
  window.paypalSdkInstance = sdkInstance;           // expose globally
  window.dispatchEvent(new CustomEvent('paypalReady', {
    detail: { instance: sdkInstance }
  }));
}
```

### Fix 2 — Include SDK script on every page with buttons

```html
<script async src="https://www.sandbox.paypal.com/web-sdk/v6/core" onload="onLoad()"></script>
<script src="/js/paypal-init.js"></script>
```

For SPAs: ensure `window.paypalSdkInstance` persists across route changes.

### Fix 3 — Race condition: waiting pattern

Don't access `window.paypalSdkInstance` directly in page scripts — use:

```js
function initButtonWhenReady(containerId) {
  if (window.paypalSdkInstance) {
    initPayPalButton(containerId);          // already loaded
  } else {
    window.addEventListener('paypalReady', () => {
      initPayPalButton(containerId);        // wait for event
    }, { once: true });
  }
}
```

### Debugging checklist

```js
console.log('SDK loaded:', !!window.paypal);
console.log('Instance ready:', !!window.paypalSdkInstance);
```

- `window.paypal` false → SDK script not loading on this page
- `window.paypalSdkInstance` false → `onLoad()` not running or missing the global assignment

## Related pages

- [[source-paypal-payments-quickstart]] — Base integration this troubleshoot guide covers
- [[paypal-checkout]] — PayPal Checkout concept page

## Raw Sources

- [[paypal-troubleshoot]] — verbatim troubleshoot guide
