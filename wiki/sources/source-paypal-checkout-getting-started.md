---
title: "PayPal Checkout: Getting Started"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-checkout-getting-started.md"
tags: [paypal, checkout, javascript-sdk, orders-api, integration, sandbox]
---

## PayPal Checkout: Getting Started

Official PayPal developer documentation for integrating PayPal Checkout — the standard flow for accepting PayPal, Venmo, debit, and credit card payments on a website.

Source URL: <https://developer.paypal.com/docs/checkout/standard/integrate/>

## Key Takeaways

- **PayPal JS SDK** renders all payment buttons (PayPal, Venmo, Debit/Credit Card) and launches the checkout pop-up. Accessed globally via `window.paypal`.
- **Two-step server flow**: merchant server creates an order via `POST /v2/checkout/orders`, returns the Order ID to the SDK, then captures via `POST /v2/checkout/orders/{orderID}/capture` after buyer approval.
- **Key SDK callbacks**:
  - `createOrder` — triggered on button click; calls merchant server to create the order
  - `onShippingAddressChange` / `onShippingOptionsChange` — allow dynamic shipping recalculation
  - `onApprove` — triggered after buyer approves; merchant server captures the order
- **PayPal Checkout pop-up** shows the buyer their default shipping address and the default shipping option set in the initial Orders API call. Buyer can change address and payment method before confirming.
- **Button placement**: PayPal recommends showing PayPal/Pay Later buttons on product detail pages, cart pages, and checkout pages — not just at final checkout.
- **Server SDK**: `@paypal/paypal-server-sdk@1.0.0` for Node.js (also Java, PHP, Python, Ruby, .Net). Wraps the PayPal REST API.
- **Auth**: Client ID + Client Secret (from Developer Dashboard). Access token authenticates REST API calls.
- **Sandbox**: Full sandbox environment available; create personal or business sandbox accounts from the Developer Dashboard.

## Checkout Sequence (detailed)

1. Merchant page loads → `<script>` tag fetches PayPal JS SDK
2. SDK renders PayPal button on page
3. Buyer clicks button → SDK opens checkout browser pop-up, calls `createOrder` callback
4. Merchant server calls `POST /v2/checkout/orders` → PayPal returns Order ID
5. Order ID passed back to SDK → SDK launches full checkout browser pop-up
6. Buyer logs in (username + password); `onShippingAddressChange` / `onShippingOptionsChange` fire
7. Buyer completes checkout → PayPal sends "Order Approved"
8. `onApprove` callback fires → merchant server calls `POST /v2/checkout/orders/{orderID}/capture`
9. PayPal returns OK → merchant marks order as captured, checkout complete

See sequence diagram in `raw/assets/paypal-checkout-workflow-sequence-diagram.png`.

## Optimal Button Placement (from UI screenshots)

PayPal recommends surfacing buttons at three points in the purchase journey:

| Page | What the buyer can do |
| ------ | ---------------------- |
| Product details | Buy directly from the product page |
| Cart | Buy directly from the cart page |
| Checkout | Complete payment with PayPal Checkout |

See `raw/assets/paypal-optimal-payment-methods-ui.png` for the UI example.

## Node.js Setup (quick reference)

```bash
npm install @paypal/paypal-server-sdk@1.0.0 dotenv express body-parser
```

Key `package.json` requirements:

- `"type": "module"` — required for ES module support
- `nodemon` recommended for dev server restarts

Environment variables: `PAYPAL_CLIENT_ID`, `PAYPAL_CLIENT_SECRET`

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-checkout]] — PayPal Checkout concept page
- [[javascript-sdk]] — PayPal JS SDK concept
- [[orders-api]] — PayPal Orders REST API

## Images

- `raw/assets/paypal-checkout-workflow-sequence-diagram.png` — sequence diagram showing the full integration flow across Buyer, Merchant Server, Merchant Page, PayPal JS SDK, PayPal Checkout, and PayPal Orders API actors
- `raw/assets/paypal-optimal-payment-methods-ui.png` — mobile UI mockup showing PayPal button placement on product detail, cart, and checkout pages

## Raw Sources

- [[paypal-checkout-getting-started]] — verbatim webpage content + image references
