<!-- Source: Stripe — Stripe Web Elements overview -->
<!-- Fetched: 2026-04-21 -->
<!-- URL: https://docs.stripe.com/payments/elements -->

<!-- Diagram (inline attachment, cannot be downloaded):
     Shows Checkout Sessions API → Customer, Shipping, Taxes, Discounts and coupons, Payment
     Payment Intents API → Payment (dashed line, lower-level)
     Key insight: Checkout Sessions API manages more checkout concerns; Payment Intents API handles only the payment step
-->

# Stripe Web Elements

Create your own checkout flows with prebuilt UI components.

Stripe Elements is a set of prebuilt UI components for building your web checkout flow. It's available as a feature of Stripe.js, our foundational JavaScript library for building payment flows. Stripe.js tokenizes sensitive payment details within an Element without ever having them touch your server.

## Features

- **Global payment methods**: Access to over 100 global payment methods, including wallets like Apple Pay.
- **Link**: Help your customers check out faster by letting them select a saved payment method at checkout instead of entering payment information.
- **Saved payment methods**: Save, reuse, and manage cards and bank accounts with built-in features.
- **Compliance**: Stripe provides a globally compliant interface and handles requirements for displaying mandates and consent notices to buyers.
- **Up-to-date forms**: Localized forms with built-in error handling. Stripe keeps each payment method provider's requirements up to date.
- **Address collection**: Collect full or partial billing addresses with any payment method.
- **Appearance customization**: Customize the look and feel of Elements to match the design of your site.
- **Other features**: Additional features like CVC recollection and control over which card brands you accept.

## Available Elements

### Payment Element
Accept a payment with one or multiple payment methods securely, including cards.

### Express Checkout Element
Display popular Wallets like Apple Pay, Google Pay, and PayPal.

### Link Authentication Element
Link auto-fills your customers' payment and shipping details to reduce friction and deliver an easy and secure checkout experience.

### Address Element
Collect address information and display Link saved addresses.

### Payment Method Messaging Element
Automatically inform customers about available Buy now, Pay later plans.

### Currency Selector Element
*(Checkout Sessions API only)*
Let customers pay in their local currency with Adaptive Pricing.

### Tax ID Element
Collect business tax IDs for invoices and VAT refunds.

## Compatible APIs

Stripe offers two core payments APIs compatible with Elements. **Stripe recommends the Checkout Sessions API for most integrations.**

### Checkout Sessions API (Recommended)

Use the Checkout Sessions API to build your checkout flow. Checkout Sessions covers similar use cases as Payment Intents, including:
- Basic payments using `price_data`
- Full checkout with line items, tax, discounts, shipping, subscriptions
- Adaptive Pricing (only available with Checkout Sessions)

→ Build a checkout page with the Checkout Sessions API.

### Payment Intents API

The Payment Intents API is a lower-level API that models only the payment step. You pass in a final amount and build all checkout logic yourself, including tax calculation, discounts, shipping, subscriptions, and currency conversion.

Use Payment Intents only if you want to deeply own your checkout state and build these features yourself.

→ Build a custom integration from scratch with the Payment Intents API.

## API Comparison (from diagram)

| Checkout concern | Checkout Sessions API | Payment Intents API |
| --- | --- | --- |
| Customer management | ✓ | — (build yourself) |
| Shipping | ✓ | — (build yourself) |
| Taxes | ✓ | — (build yourself) |
| Discounts and coupons | ✓ | — (build yourself) |
| Payment | ✓ | ✓ (core feature) |
| Adaptive Pricing | ✓ | — |
