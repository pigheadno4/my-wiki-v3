---
title: "PayPal Checkout: Validate User Input"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-checkout-validate-user-input.md"
tags: [paypal, checkout, validation, oninit, onclick, actions-disable, actions-reject, javascript-sdk]
---

## PayPal Checkout: Validate User Input

Official PayPal guide for validating form input before initiating checkout — using `onInit`/`onClick` for synchronous validation and a Promise-returning `onClick` for asynchronous validation. One of PayPal's two recommended starting customizations.

Source URL: <https://developer.paypal.com/docs/checkout/standard/customize/validate-user-input/>

Last updated: 2025-05-14

## Key Takeaways

### Two validation modes

| Mode | When to use | Mechanism |
| ---- | ----------- | --------- |
| **Synchronous** | Preferred — form state known client-side | `onInit` + `actions.disable()`/`enable()` + `onClick` |
| **Asynchronous** | Server-side or async validation only | `onClick` returns a Promise → `actions.reject()`/`resolve()` |

### Synchronous pattern — `onInit` + `onClick`

- `onInit`: fires when button renders → call `actions.disable()` immediately; attach event listeners to form fields to call `actions.enable()`/`disable()` based on validity
- `onClick`: show validation error message if form is invalid

This pattern gives the best UX: button is visually disabled until the form is valid, and the buyer sees inline error feedback.

### Asynchronous pattern — Promise from `onClick`

- `onClick` returns a `fetch()` Promise
- On validation failure: show error + return `actions.reject()` → blocks PayPal from opening
- On validation pass: return `actions.resolve()` → PayPal proceeds

> **Avoid async when sync suffices** — async validation adds latency and degrades UX.

### Ideal validation order

1. Complete validation **before rendering buttons** (best UX)
2. Synchronous validation on click (`onInit` + `onClick`) — second choice
3. Asynchronous validation on click — only when server-side validation required

## Raw Sources

- [[paypal-checkout-validate-user-input]] — verbatim webpage content

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-checkout]] — PayPal Checkout concept page
- [[source-paypal-checkout-customize-overview]] — full customization feature catalog (recommends this as starting point alongside show-cancellation-page)
- [[source-paypal-checkout-show-cancellation-page]] — the other recommended starting customization
