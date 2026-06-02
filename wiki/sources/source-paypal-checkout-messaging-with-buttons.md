---
title: "PayPal Checkout: Messaging with Buttons"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-checkout-messaging-with-buttons.md"
tags: [paypal, checkout, messaging, pay-later, buttons, javascript-sdk, conversion, us-only]
---

## PayPal Checkout: Messaging with Buttons

Official PayPal guide for embedding Pay Later and promotional messaging directly into the PayPal Buttons component.

Source URL: <https://developer.paypal.com/docs/checkout/standard/customize/messaging-with-buttons/>

Last updated: 2024-12-16

## Key Takeaways

### Availability

US merchants and US customers only. Requires Pay Later eligibility to show Pay Later offers; other PayPal value propositions still display if ineligible.

### Integration — `message` option on `Buttons`

```javascript
const buttons = paypal.Buttons({
  message: {
    amount: 100,   // current cart/product total
    align: 'center',
    color: 'black',
  }
});
```

- `message.amount` should match the current cart/product total for the strongest offer
- `message.amount` is **independent** of the captured order total — changing it does not affect what gets charged

### Message position adapts to button layout

| Layout | Message position |
| ------ | ---------------- |
| Vertical stack | Top (above buttons) — moved up to make room for card button text |
| Horizontal stack | Inline with buttons |
| Standalone PayPal | Adjacent (non-Pay Later messaging) |
| Standalone Pay Later | Adjacent (Pay Later messaging) |

### Dynamic amount update — `updateProps`

When cart total changes, update messaging without re-rendering:

```javascript
buttons.updateProps({
  message: { amount: 200, align: 'center', color: 'black' }
});
```

> **Gotcha**: `updateProps` must include **all** previously set `message` options — omitted options reset to defaults.

## Images

- `raw/assets/paypal-messaging-header-horizontal.png` — horizontal layout header example
- `raw/assets/paypal-messaging-vertical-stack.png` — vertical stack with Pay Later messaging
- `raw/assets/paypal-messaging-horizontal-stack.png` — horizontal stack with Pay Later messaging
- `raw/assets/paypal-messaging-standalone-paypal.png` — standalone PayPal button with messaging
- `raw/assets/paypal-messaging-standalone-paylater.png` — standalone Pay Later button with messaging

## Raw Sources

- [[paypal-checkout-messaging-with-buttons]] — verbatim webpage content + downloaded images

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-checkout]] — PayPal Checkout concept page
- [[source-paypal-checkout-customize-overview]] — full customization feature catalog
- [[source-paypal-checkout-display-funding-source]] — related: Pay Later as a fundingSource value
