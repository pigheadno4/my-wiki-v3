---
title: "PayPal JavaScript SDK: Best Practices (CSP & COOP)"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-javascript-sdk-best-practices.md"
tags: [paypal, javascript-sdk, security, csp, coop, nonce, content-security-policy, xss]
---

## PayPal JavaScript SDK: Best Practices (CSP & COOP)

Official PayPal guide for the two security headers required/recommended when integrating the JS SDK: Content Security Policy (CSP) and Cross-Origin-Opener-Policy (COOP).

Source URL: <https://developer.paypal.com/sdk/js/best-practices/>

Last updated: 2026-02-04

## Key Takeaways

### Required CSP domains

All three must be whitelisted across `child-src`, `connect-src`, `frame-src`, `img-src`, `script-src`, and `style-src`:

- `*.paypal.com`
- `*.paypalobjects.com`
- `*.venmo.com`

Also: `data:` must be allowed in `img-src`.

### Two CSP approaches

| Approach | Security | Complexity |
| -------- | -------- | ---------- |
| `'unsafe-inline'` | Lower | Simpler — no nonce generation needed |
| Nonce | Higher | Requires server-generated nonce per request |

### Nonce integration

When using nonce, pass it in **two places**:
1. The `<script>` tag: `nonce="YOUR_NONCE"`
2. The `data-csp-nonce` attribute: `data-csp-nonce="YOUR_NONCE"`

For React/ES module loading, use `dataCspNonce: "YOUR_NONCE"` in the options object passed to `PayPalScriptProvider` or `loadScript()`.

### COOP header

**Required value**: `Cross-Origin-Opener-Policy: same-origin-allow-popups`

Do not use `same-origin` alone — the `allow-popups` suffix is essential because the PayPal Checkout flow opens in a popup window that must communicate with the parent page.

## Raw Sources

- [[paypal-javascript-sdk-best-practices]] — verbatim webpage content

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[source-paypal-javascript-sdk-configuration]] — `data-csp-nonce` script parameter documented here
- [[source-paypal-javascript-sdk-overview]] — SDK component overview
