---
title: "Stripe Express Checkout Element"
type: source
date_ingested: 2026-04-21
original_format: webpage
raw_files:
  - "stripe-express-checkout-element-2025.md"
tags: [stripe, elements, express-checkout, apple-pay, google-pay, paypal, link, klarna, amazon-pay, one-click-payments, wallet]
---

## Summary

The Express Checkout Element is a Stripe UI component that renders multiple one-click payment buttons — Link, Apple Pay, Google Pay, PayPal, Klarna, and Amazon Pay — in a single integration. Buttons are dynamically sorted by customer location/relevance. New payment methods can be added from the Dashboard without frontend code changes.

## Key Takeaways

- **Supported payment methods**: Link, Apple Pay, Google Pay, PayPal, Klarna, Amazon Pay
- **Dynamic sorting**: Stripe sorts buttons by relevance to the customer's location automatically
- **No frontend changes needed** to add new payment methods once integrated
- **Reuses existing Elements instance** — compatible with Payment Element in the same Elements group

## Payment Method Availability

Methods only appear when:
- Active in the Stripe Dashboard
- Browser and currency are supported
- Customer has the method set up (e.g., Google Pay configured on their device)
- Domain is registered in Stripe (both test and live mode)

Finland and Sweden regulations require debit payment methods to appear before credit methods.

## Browser Support Matrix

|                    | Apple Pay | Google Pay | Link | PayPal | Amazon Pay | Klarna |
| ------------------ | --------- | ---------- | ---- | ------ | ---------- | ------ |
| Chrome             | ✓ (macOS only, `always`) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Edge               | ✓ (macOS only, `always`) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Firefox            | ❌ | ✓ (`always`) | ❌ | ✓ | ✓ | ❌ |
| Safari             | ✓ | ✓ (`always`) | ✓ | ✓ | ✓ | ✓ |
| Chrome on iOS 16+  | ✓ | ✓ (`always`) | ✓ | ✓ | ✓ | ✓ |
| Chrome on Android  | ❌ | ✓ | ✓ | ✓ | ✓ | ✓ |

Notes: Apple Pay on desktop Chromium requires `paymentMethods.applePay: 'always'`. Google Pay on Firefox/Safari requires `paymentMethods.googlePay: 'always'`. Limited support in in-app webviews.

## Customization

### Layout
Default grid layout; configurable via `layout` option (max columns, max rows, overflow menu behavior).

### Button Types (`buttonType`)
Each wallet supports different call-to-action text:
- **Apple Pay**: `plain`, `buy`, `checkout`, `subscribe`, `donate`, `book`, `order`, and more (14 types)
- **Google Pay**: `plain`, `buy`, `checkout`, `pay`, `subscribe`, `donate`, `book`, `order`
- **PayPal**: `paypal`, `checkout`, `buynow`, `pay`
- **Klarna**: `continue`, `pay`
- **Link / Amazon Pay**: single type each

### Button Themes (`buttonTheme`)
- **Apple Pay**: `black`, `white`, `white-outline`
- **Google Pay**: `black`, `white`
- **PayPal**: `gold`, `blue`, `silver`, `white`, `black`
- **Klarna**: multiple (auto-selected from Appearance API theme)
- Appearance API `theme` drives automatic compatible theme selection per wallet

### Appearance Limits
Only these are customizable: button height (`buttonHeight`), border radius (via Appearance API variables), button themes. Logos and brand colors are wallet-controlled.

## Controlling Payment Methods

- Activate/deactivate from Dashboard
- `paymentMethodOrder` — override Stripe's relevance-based ordering
- `paymentMethods.applePay / googlePay: 'never'` — hide a method
- `paymentMethods.applePay / googlePay: 'always'` — show even if not set up (still blocked on unsupported platforms/currencies)

## Ready Event

The `ready` event fires with `availablePaymentMethods` when the element determines which wallets are available. Use it to:
- Show a fallback payment UI (e.g., Payment Element) if no wallets are available
- Hide the Express Checkout container until a wallet is confirmed

```js
expressCheckoutElement.on("ready", ({ availablePaymentMethods }) => {
  if (!availablePaymentMethods) showFallbackPaymentUI();
});
```

React equivalent uses `onReady` prop on `<ExpressCheckoutElement>`.

## Related Pages

- [[stripe-express-checkout-element]] — concept page
- [[stripe-elements]] — parent Elements framework
- [[stripe]] — company page
- [[stripe-checkout]] — alternative full-checkout approach

## Raw Sources

- [[stripe-express-checkout-element-2025]] — verbatim Stripe docs webpage
