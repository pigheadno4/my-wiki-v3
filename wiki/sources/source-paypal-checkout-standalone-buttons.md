---
title: "PayPal Checkout: Standalone Payment Buttons"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-checkout-standalone-buttons.md"
tags: [paypal, checkout, standalone-buttons, funding-eligibility, venmo, pay-later, marks, javascript-sdk]
---

## PayPal Checkout: Standalone Payment Buttons

Official PayPal guide for rendering individual payment method buttons in separate locations on a page, using `paypal.getFundingSources()` and `button.isEligible()` for smart eligibility.

Source URL: <https://developer.paypal.com/docs/checkout/standard/customize/standalone-buttons/>

Last updated: 2025-05-09

## Key Takeaways

### When to use

Default PayPal Checkout renders all eligible buttons in one container. Use standalone buttons to:
- Show buttons in different parts of the page
- Show buttons alongside radio button groups
- Show only a specific subset of payment methods

### Required `components` in script tag

| Use case | Components param |
| -------- | ---------------- |
| Standalone / subset | `buttons,funding-eligibility` |
| Radio buttons with Marks | `buttons,funding-eligibility,marks` |

Without `funding-eligibility`, `paypal.getFundingSources()` and `button.isEligible()` are unavailable.

### Eligibility check pattern

Always check `button.isEligible()` before rendering — the SDK handles payer eligibility (e.g. Venmo only for US users):

```javascript
var button = paypal.Buttons({ fundingSource: fundingSource });
if (button.isEligible()) {
    button.render('#container');
}
```

### Four implementation patterns

| Pattern | When to use |
| ------- | ----------- |
| `getFundingSources()` loop | All eligible buttons in one spot |
| Manual `FUNDING_SOURCES` array | Specific subset of methods |
| Marks + radio buttons | When buttons accompany radio selectors |
| Multiple `render()` targets | PayPal + Venmo in different page sections |

### Pay Later + Credit note (US/UK)

Show **both** `PAYLATER` and `CREDIT` when enabling either — PayPal renders whichever the buyer is eligible for. Don't show only one.

### Sandbox limitation

Venmo is **not supported in the sandbox** — only testable in production.

### UK regulatory note

PayPal Credit button requires authorization as a credit broker + a credit agreement with PayPal (UK regulated activity).

## Raw Sources

- [[paypal-checkout-standalone-buttons]] — verbatim webpage content

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-checkout]] — PayPal Checkout concept page
- [[source-paypal-checkout-display-payment-methods]] — related: radio button toggle with Marks (referenced from this page)
- [[source-paypal-checkout-display-funding-source]] — related: fundingSource enum values
- [[source-paypal-checkout-customize-overview]] — full customization feature catalog
