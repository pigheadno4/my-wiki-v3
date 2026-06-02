<!-- Source URL: https://docs.stripe.com/payments/checkout-sessions -->
<!-- Fetched: 2026-04-19 -->

# The Checkout Sessions API

Build a Stripe payments integration with built-in support using the Checkout Sessions API.

Use the [Checkout Sessions API](https://docs.stripe.com/api/checkout/sessions.md) to build a payments integration with built-in support for [tax calculation](https://docs.stripe.com/payments/checkout/taxes.md), [discounts](https://docs.stripe.com/payments/checkout/promotions.md), [subscriptions](https://docs.stripe.com/payments/subscriptions.md), [shipping](https://docs.stripe.com/payments/during-payment/charge-shipping.md), and [currency conversion](https://docs.stripe.com/payments/currencies/localize-prices/adaptive-pricing.md#exchange-rate). Stripe recommends this API for most payments integrations because it handles complex checkout tasks for you, enables features such as [Adaptive Pricing](https://docs.stripe.com/payments/currencies/localize-prices/adaptive-pricing.md), and reduces the amount of custom code you need to write and maintain.

The Checkout Sessions API serves as the backend for multiple [Stripe payment UIs](https://docs.stripe.com/payments/online-payments.md#payment-uis):

- [Stripe-hosted page](https://docs.stripe.com/payments/checkout.md): Redirect customers to a Stripe-hosted payment page.
- [Embedded form](https://docs.stripe.com/checkout/embedded/quickstart.md): Embed a Stripe payment form directly on your site.
- [Custom payment flow](https://docs.stripe.com/payments/quickstart-checkout-sessions.md): Build a fully custom checkout page using [Stripe Elements](https://docs.stripe.com/payments/elements.md), including the [Payment Element](https://docs.stripe.com/payments/payment-element.md).

To get started, see the [Checkout Sessions quickstart](https://docs.stripe.com/payments/quickstart-checkout-sessions.md). It walks through creating a `Checkout Session` on the server, using its `client_secret` with Stripe Elements on the client.

## A prebuilt, extensible checkout

The Checkout Sessions API manages the full checkout lifecycle for you. Some of the advantages of using the Checkout Sessions API include:

| Feature                           | Description                                                                                                                                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Built-in checkout features        | Tax calculation, discounts, shipping, subscriptions, and [Adaptive Pricing](https://docs.stripe.com/payments/currencies/localize-prices/adaptive-pricing.md) are available without additional API integrations. |
| Automatic authentication handling | Stripe manages [3D Secure](https://docs.stripe.com/payments/3d-secure.md) authentication, and other required customer actions.                                                                                  |
| Flexible payment UIs              | Use a Stripe-hosted page, an embedded form, or fully custom [Stripe Elements](https://docs.stripe.com/payments/elements.md) to match your brand.                                                                |
| Managed checkout state            | Stripe tracks the session state, including expiration and status, so you don’t have to.                                                                                                                         |
| No double charges                 | The API prevents duplicate charges by tracking the session lifecycle.                                                                                                                                           |

The Checkout Sessions API covers similar payment scenarios as the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md), but the Checkout Sessions API requires significantly less code. Use the Payment Intents API if you need to control every aspect of the checkout state or if you plan to build discount, tax, subscription, and currency conversion logic yourself. To determine which is right for your integration, [compare the two](https://docs.stripe.com/payments/checkout-sessions-and-payment-intents-comparison.md).

## Checkout lifecycle

The Checkout Sessions API manages the full checkout lifecycle for you, with the lifecycle varying depending on the [payment UI you use](https://docs.stripe.com/payments/checkout/how-checkout-works.md).

### Store information in metadata

Stripe supports adding [metadata](https://docs.stripe.com/api.md#metadata) to most requests, including requests to the Checkout Sessions API. Use metadata to associate your own identifiers (such as order IDs) with Stripe sessions. Metadata is visible in the Dashboard and available in reports, to help you reconcile payments.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  mode: "payment",
  ui_mode: "custom",
  return_url: "https://example.com/return",
  metadata: {
    order_id: "6735",
  },
});
```

Don’t store sensitive information (such as personally identifiable information or card details) as metadata.

## See also

- [How Checkout works](https://docs.stripe.com/payments/checkout/how-checkout-works.md)
- [Build a checkout page with the Checkout Sessions API](https://docs.stripe.com/payments/quickstart-checkout-sessions.md)
- [Migrate from Payment Intents to Checkout Sessions](https://docs.stripe.com/payments/payment-element/migration-ewcs.md)
