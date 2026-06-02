---
title: "PayPal Checkout: Display Funding Source Used"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-checkout-display-funding-source.md"
tags: [paypal, checkout, funding-source, venmo, pay-later, confirmation-page, onclick, javascript-sdk]
---

## PayPal Checkout: Display Funding Source Used

Official PayPal guide for surfacing the buyer's chosen payment method on confirmation pages and notifications using the JS SDK `onClick` handler.

Source URL: <https://developer.paypal.com/docs/checkout/standard/customize/display-funding-source/>

Last updated: 2025-05-13

## Key Takeaways

### The problem

If a buyer pays with Venmo (not PayPal), but your confirmation page says "You paid with PayPal" — that's confusing and can hurt conversion. This feature ensures the correct brand is shown.

### Implementation

One-liner in `onClick` — capture `data.fundingSource` before the checkout flow starts:

```javascript
paypal.Buttons({
    onClick: (data) => {
        fundingSource = data.fundingSource; // e.g. "venmo"
    }
})
```

Use this value to update confirmation pages, emails, and notifications with the correct payment method name/logo.

### Supported `fundingSource` values

| Value | Payment method |
| ----- | -------------- |
| `paypal.FUNDING.PAYPAL` | PayPal |
| `paypal.FUNDING.CARD` | Credit or debit card |
| `paypal.FUNDING.PAYLATER` | Pay Later — US/UK; Pay in 4 (AU); 4X PayPal (FR); Paga en 3 plazos (ES); Paga in 3 rate (IT); Später Bezahlen (DE) |
| `paypal.FUNDING.CREDIT` | PayPal Credit |
| `paypal.FUNDING.VENMO` | Venmo |

### Pay Later localisation

`PAYLATER` covers multiple branded products by market — not a single global product name. Merchants targeting international buyers should map `PAYLATER` to the market-appropriate label.

## Raw Sources

- [[paypal-checkout-display-funding-source]] — verbatim webpage content

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-checkout]] — PayPal Checkout concept page
- [[source-paypal-checkout-customize-overview]] — full customization feature catalog
