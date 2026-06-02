<!-- Source URL: https://docs.stripe.com/payments/managed-payments/set-up -->
<!-- Fetched: 2026-04-23 -->

# Build a Checkout integration with Managed Payments

Learn how to accept a payment using Managed Payments.

> #### Terms of service required
>
> You must accept the [Managed Payments terms of service](https://stripe.com/legal/managed-payments) in the [Dashboard](https://dashboard.stripe.com/settings/managed-payments) before you can use Managed Payments.

Use Managed Payments to accept global payments for digital products. Managed Payments enables Stripe to act as the merchant of record on your behalf. To learn more, see [How Managed Payments works](https://docs.stripe.com/payments/managed-payments/how-it-works.md).

## Before you begin

- Make sure your products meet the [eligibility requirements](https://docs.stripe.com/payments/managed-payments/eligibility.md) for Managed Payments. To process a payment with Managed Payments, all of the products the customer is purchasing must be eligible.
- Activate Managed Payments in your [Dashboard](https://dashboard.stripe.com/settings/managed-payments).
- [Set up your development environment](https://docs.stripe.com/get-started/development-environment.md).
- Use an API version of `2025-03-31.basil` or [later](https://docs.stripe.com/changelog.md).

## Create products and prices

You can accept subscriptions and one-time payments:

#### Subscriptions

Stripe uses [Products](https://docs.stripe.com/api/products.md) to represent the different goods or services you’re selling. For example, if you have multiple subscription tiers, such as Basic and Premium, create a separate product for each tier.

[Prices](https://docs.stripe.com/api/prices.md) represent the amount you charge your customer for a product, and how frequently you charge them. A product can have multiple prices. For example, your Basic subscription could have two prices: 10 USD per month or 100 USD per year. You can also define different currency options for each price, such as 10 USD per month and 15 CAD per month.

Use either the Dashboard or the API to create products and prices for each of the products you sell:

#### Dashboard

### Create a new product and price

To create a new product and assign a price:

1. Navigate to the **Dashboard** > [Product catalog](https://dashboard.stripe.com/test/products).
1. Click **Create product**.
1. Enter the **Product name**, **Description**, and select a **Product tax code**.
   - The tax code you select must be [eligible for Managed Payments](https://docs.stripe.com/payments/managed-payments/eligibility.md#eligible-tax-codes). Eligible tax codes are labeled `Eligible for Managed Payments`.
1. For the price, enter the **Amount** and the **Currency**.
1. Set the **Billing period** based on how frequently you’d like to charge your customer for this subscription.
1. Use the preview pane on the right to see how much tax customers will pay based on their location.
1. Click **Add product**.
1. Repeat these steps for every product you sell.

### Add a price to an existing product

To add another price to an existing product:

1. Open the [Product catalog](https://dashboard.stripe.com/test/products).
1. Click the product you want to add a price to.
1. Click the `+` button in the **Pricing** section.
1. Configure the price as described above.
1. Click **Create price**.

#### API

### Create a new product and price

To create a new product and assign a price:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const product = await stripe.products.create({
  name: "Basic subscription",
  description: "A basic subscription to our service",
  tax_code: "{{TAX_CODE}}",
  default_price_data: {
    unit_amount: 1000,
    currency: "usd",
    recurring: {
      interval: "month",
    },
  },
});
```

The tax code you use must be [eligible for Managed Payments](https://docs.stripe.com/payments/managed-payments/eligibility.md#product-eligibility).

Repeat this step for every product you sell.

### Add a price to an existing product

To add another price to an existing product:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const price = await stripe.prices.create({
  product: "{{BASIC_PRODUCT_ID}}",
  unit_amount: 10000,
  currency: "usd",
  recurring: {
    interval: "year",
  },
});
```

#### One-time payments

Stripe uses [Products](https://docs.stripe.com/api/products.md) to represent the different goods or services you’re selling. For example, if you sell e-books, create a separate product for each e-book.

[Prices](https://docs.stripe.com/api/prices.md) represent the amount you charge your customer for a product. A product can have multiple prices. You can also define different currency options for each price, such as 10 USD and 15 CAD.

Use either the Dashboard or the API to create products and prices for each of the products you sell:

#### Dashboard

### Create a new product and price

To create a new product and assign a price:

1. Navigate to the **Dashboard** > [Product catalog](https://dashboard.stripe.com/test/products).
1. Click **Create product**.
1. Enter the **Product name**, **Description**, and select a **Product tax code**.
   - The tax code you select must be [eligible for Managed Payments](https://docs.stripe.com/payments/managed-payments/eligibility.md#product-eligibility). Eligible tax codes are labeled `Eligible for Managed Payments`.
1. For the price, enter the **Amount** and the **Currency**.
1. Use the preview pane on the right to see how much tax customers will pay based on their location.
1. Click **Add product**.
1. Repeat these steps for every product you sell.

### Add a price to an existing product

To add another price to an existing product:

1. Open the [Product catalog](https://dashboard.stripe.com/test/products).
1. Click the product you want to add a price to.
1. Click the `+` button in the **Pricing** section.
1. Configure the price as described above.
1. Click **Create price**.

#### API

### Create a new product and price

To create a new product and assign a price:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const product = await stripe.products.create({
  name: "Hamlet (e-book)",
  description: "A Shakespearean tragedy",
  tax_code: "{{TAX_CODE}}",
  default_price_data: {
    unit_amount: 1000,
    currency: "usd",
  },
});
```

The tax code you use must be [eligible for Managed Payments](https://docs.stripe.com/payments/managed-payments/eligibility.md#product-eligibility).

Repeat this step for every product you sell.

### Add a price to an existing product

To add another price to an existing product:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const price = await stripe.prices.create({
  product: "{{PRODUCT_ID}}",
  unit_amount: 1000,
  currency: "usd",
});
```

## Build your checkout [Client-side]

[Stripe Checkout](https://docs.stripe.com/payments/checkout.md) allows you to accept payments from your customers through a Stripe-hosted payment page. You’re responsible for redirecting your customer to the payment page, and Stripe redirects your customer back to your site once the payment is complete. To learn more, see [How Checkout works](https://docs.stripe.com/payments/checkout/how-checkout-works.md?payment-ui=stripe-hosted).

To build your checkout, you must add a checkout button and a success page to your site.

#### Subscriptions

### Add a checkout button

Add a checkout button to your website that calls an endpoint on your server. For example:

```html
<html>
  <head>
    <title>Subscribe to our cool new service</title>
  </head>
  <body>
    <!-- Use action="/create-checkout-session.php" if your server is PHP based. -->
    <form action="/create-checkout-session" method="POST">
      <button type="submit">Subscribe</button>
    </form>
  </body>
</html>
```

When your customer clicks this button, they’ll be redirected to the Stripe-hosted payment page.

### Add a success page

Next, create a success page for your customer to see after they successfully check out. Host this success page on your site. For example:

```html
<html>
  <head>
    <title>Thanks for subscribing!</title>
  </head>
  <body>
    <h1>Thanks for subscribing!</h1>
    <p>
      We appreciate your business! If you have any questions, please email us at
      <a href="mailto:orders@example.com">orders@example.com</a>.
    </p>
  </body>
</html>
```

Stripe redirects your customer to this page after they complete an authorized payment.

### Add a cancel page (optional)

You can also create a cancel page for your customer to see if they terminate the checkout process. For example:

```html
<html>
  <head>
    <title>Checkout canceled</title>
  </head>
  <body>
    <p>Not ready to subscribe yet? No problem, we'll be here when you are!</p>
  </body>
</html>
```

Stripe redirects your customer to this page if they click the back button on the payment page.

#### One-time payments

### Add a checkout button

Add a checkout button to your website that calls an endpoint on your server. For example:

```html
<html>
  <head>
    <title>Buy Hamlet</title>
  </head>
  <body>
    <!-- Use action="/create-checkout-session.php" if your server is PHP based. -->
    <form action="/create-checkout-session" method="POST">
      <button type="submit">Purchase</button>
    </form>
  </body>
</html>
```

When your customer clicks this button, they’ll be redirected to the Stripe-hosted payment page.

### Add a success page

Next, create a success page for your customer to see after they successfully check out. Host this success page on your site. For example:

```html
<html>
  <head>
    <title>Thanks for purchasing!</title>
  </head>
  <body>
    <h1>Thanks for purchasing!</h1>
    <p>
      We appreciate your business! If you have any questions, please email us at
      <a href="mailto:orders@example.com">orders@example.com</a>.
    </p>
  </body>
</html>
```

Stripe redirects your customer to this page after they complete an authorized payment.

### Add a cancel page (optional)

You can also create a cancel page for your customer to see if they terminate the checkout process. For example:

```html
<html>
  <head>
    <title>Checkout canceled</title>
  </head>
  <body>
    <p>Not ready to purchase yet? No problem, we'll be here when you are!</p>
  </body>
</html>
```

Stripe redirects your customer to this page if they click the back button on the payment page.

## Set up your server [Server-side]

Stripe uses [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions.md) to represent what your customer sees when they’re redirected to the payment form. You can configure Checkout Sessions with options such as [line items](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items) to charge or currencies to accept.

### Create a Checkout Session

#### Subscriptions

Create a Checkout Session using one of the [prices you created](https://docs.stripe.com/payments/managed-payments/set-up.md#create-product) as a line item. Set the `mode` to `subscription`, and set the `success_url` to the URL of your success page. To enable Managed Payments, set `managed_payments[enabled]` to `true`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  managed_payments: {
    enabled: true,
  },
  mode: "subscription",
  success_url: "https://localhost:4242/success",
});
```

#### One-time payments

Create a Checkout Session using one of the [prices you created](https://docs.stripe.com/payments/managed-payments/set-up.md#create-product) as a line item. Set the `mode` to `payment`, and set the `success_url` to the URLs of your success and cancel pages. To enable Managed Payments, set `managed_payments[enabled]` to `true`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  managed_payments: {
    enabled: true,
  },
  mode: "payment",
  success_url: "https://localhost:4242/success",
});
```

### Create an endpoint

Add an endpoint to your server that creates a [Checkout Session](https://docs.stripe.com/api/checkout/sessions/create.md). The endpoint path must match the `action` attribute of [your checkout button](https://docs.stripe.com/payments/managed-payments/set-up.md#add-a-checkout-button).

After you create a Checkout Session, redirect your customer to the [URL](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-url) returned in the response.

#### Item 1

#### Node.js

```javascript
// This example sets up an endpoint using the Express framework.

const express = require("express");
const app = express();

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

app.post("/create-checkout-session", async (req, res) => {
  const session = await stripe.checkout.sessions.create({
    line_items: [
      {
        price: "{{PRICE_ID}}",
        quantity: 1,
      },
    ],
    mode: "subscription",
    managed_payments: { enabled: true },
    success_url: "http://localhost:4242/success",
  });

  res.redirect(303, session.url);
});

app.listen(4242, () => console.log(`Listening on port ${4242}!`));
```

#### Item 2

#### Node.js

```javascript
// This example sets up an endpoint using the Express framework.

const express = require("express");
const app = express();

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

app.post("/create-checkout-session", async (req, res) => {
  const session = await stripe.checkout.sessions.create({
    line_items: [
      {
        price: "{{PRICE_ID}}",
        quantity: 1,
      },
    ],
    mode: "payment",
    managed_payments: { enabled: true },
    success_url: "http://localhost:4242/success",
  });

  res.redirect(303, session.url);
});

app.listen(4242, () => console.log(`Listening on port ${4242}!`));
```

### Test your endpoint

Confirm your endpoint is accessible by starting your web server (for example, `localhost:4242`) and running the following command:

```bash
curl -X POST -is "http://localhost:4242/create-checkout-session" -d ""
```

The response in your terminal looks like:

```bash
HTTP/1.1 303 See Other
Location: https://checkout.stripe.com/c/pay/cs_test_...
...
```

## Handle post-payment events

Stripe sends a [checkout.session.completed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.completed) event when a customer completes a Checkout Session payment. Use the [Dashboard webhook tool](https://dashboard.stripe.com/webhooks) or follow the [webhook guide](https://docs.stripe.com/webhooks/quickstart.md) to receive and handle these events.

Listen for these events instead of waiting for Stripe to redirect your customer to your success page. Avoid only using your success page to trigger post-checkout actions.

Set up your integration to listen for asynchronous events to properly handle [different types of payment methods](https://stripe.com/payments/payment-methods-guide) that might be delayed. To learn more, see [Fulfill orders for Checkout](https://docs.stripe.com/checkout/fulfillment.md).

Handle the following events when collecting payments with Checkout:

| Event                                                                                                                                        | Description                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| [checkout.session.completed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.completed)                             | Sent when a customer successfully completes a Checkout Session.                            |
| [checkout.session.async_payment_succeeded](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.async_payment_succeeded) | Sent when a payment made with a delayed payment method, such as ACH direct debt, succeeds. |
| [checkout.session.async_payment_failed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.async_payment_failed)       | Sent when a payment made with a delayed payment method, such as ACH direct debt, fails.    |

## Testing

Test that your integration works correctly for your customers.

### Checkout

1. Start your server and go to your checkout page (for example, <http://localhost:4242/checkout.html> from [Build your checkout](https://docs.stripe.com/payments/managed-payments/set-up.md#build-your-checkout)).
1. Click the checkout button to be redirected to the Managed Payments checkout page.
1. On the checkout page, enter different billing addresses to see how Managed Payments calculates tax for customers in different locations.
1. To process the payment, enter your email, phone number, and the test card number `4242 4242 4242 4242` with any CVC and an expiration date in the future.

For additional information, see [Testing](https://docs.stripe.com/testing.md).

### Payment details

#### Item 1

1. After you confirm the test payment, go to the **Dashboard** > [Transactions](https://dashboard.stripe.com/test/payments)
1. Click your test payment to view the payment details. This page shows the:
   - Product that was purchased
   - [Subscription](https://docs.stripe.com/api/subscriptions.md) that was created
   - [Invoice](https://docs.stripe.com/api/invoices.md) that was created
   - Amount of tax calculated and withheld through Managed Payments
   - Statement descriptor that displays on your customer’s statements

> #### Customer authorization
>
> When a customer purchases a subscription through Managed Payments, it only authorizes their payment method to be charged by Managed Payments. Make sure you obtain the appropriate consent from your customer to charge this payment method for any transactions outside of Managed Payments.

#### Item 2

1. After you confirm the test payment, go to the **Dashboard** > [Transactions](https://dashboard.stripe.com/test/payments)
1. Click your test payment to view the payment details. This page shows the:
   - Product that was purchased
   - [Subscription](https://docs.stripe.com/api/subscriptions.md) that was created (if purchased)
   - [Invoice](https://docs.stripe.com/api/invoices.md) that was created
   - Amount of tax calculated and withheld through Managed Payments
   - Statement descriptor that displays on your customer’s statements

#### Preview the receipt

1. Under **Receipt history**, click **View receipt**.
1. Click **Send receipt** to preview the receipt email sent to your customer.

> In sandbox mode, you won’t receive receipt emails automatically after purchase but can manually send them using the instructions above.

### Link

[Link](https://docs.stripe.com/payments/link.md) acts as the merchant of record at checkout and provides subscription management and transaction support on the [Link website](https://link.com).

You can test how Link works during checkout by creating a Link account during an initial Checkout Session. After you create the Link account, attempt another session using the same email address. To authenticate, use the test passcode `000000`.

Test purchases won’t appear in the Link app. You can test the order management tools in the Link app by creating a Link account during a live mode Checkout Session.

## Optional: Configure the tax behavior of your prices

The [tax_behavior](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior.md#tax-behavior) of a price specifies whether tax is added on top of the price you set (`tax_behavior: exclusive`) or included already in the price (`tax_behavior: inclusive`).

Managed Payments uses the [tax behavior specified on your price](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior.md#set-tax-behavior-on-price). If you don’t specify the price’s tax behavior, by default, Managed Payments adds tax on top of the price you set.

To change the default, go to the **Dashboard** > [Tax settings](https://dashboard.stripe.com/settings/tax) and update the **Include tax in prices** setting.

## See also

- [How Managed Payments works](https://docs.stripe.com/payments/managed-payments/how-it-works.md)
- [Update a Checkout integration](https://docs.stripe.com/payments/managed-payments/update-checkout.md)
