---
title: "PayPal iOS: In-app Purchases Flow (Lower Processing Fee)"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-ios-in-app-purchases.md"
tags: [paypal, ios, mobile, in-app-purchases, apple, external-payment, digital-goods, subscriptions, payment-link, no-code]
---

## PayPal iOS: In-app Purchases Flow (Lower Processing Fee)

Brief overview page explaining the Apple external payment entitlement flow — where apps redirect to a browser for payment processing to achieve lower processing fees than Apple's in-app purchase system.

Source URL: <https://developer.paypal.com/docs/checkout/advanced/ios/in-app-purchases/>

Last updated: 2025-05-22

## Key Takeaways

### Why this exists

In certain countries (notably the US after Epic v. Apple ruling), Apple allows iOS apps to redirect to an external website for payment processing. This enables merchants to use PayPal instead of Apple's in-app purchase system, which carries lower processing fees.

### Three recommended integration options

| Option | Complexity | What it is |
| ------ | ---------- | ----------- |
| **Payment Link** | Lowest | No-code: create a PayPal Payment Link for digital goods/subscriptions |
| **Payment Buttons** | Medium | No-code: PayPal buttons on a custom web form for in-app purchases |
| **Custom Checkout** | Highest | Direct Orders v2 API — redirect to a PayPal-hosted payment page |

### Key framing

This flow is **browser-redirect based** — the buyer leaves the app, pays on the web, then returns. This is different from the in-app card fields integration (`CardPayments` module) which keeps the buyer in the app.

The No-Code options (Payment Link, Payment Buttons) are sufficient for most digital goods / subscription use cases and require no SDK integration.

## Images

- `raw/assets/paypal-ios-iap-payment-link-icon.png` — icon for Payment Link option
- `raw/assets/paypal-ios-iap-payment-buttons-icon.png` — icon for Payment Buttons option
- `raw/assets/paypal-ios-iap-custom-checkout-icon.png` — icon for Custom Checkout option

## Raw Sources

- [[paypal-ios-in-app-purchases]] — verbatim webpage content + downloaded images

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[source-paypal-ios-card-payments]] — in-app card payments (stays in app — different from this browser-redirect flow)
- [[source-paypal-expanded-checkout-integrate]] — Custom Checkout uses Orders v2 API (same as option 3 here)
