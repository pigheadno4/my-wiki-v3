<!-- Source: Stripe Checkout — Build a subscriptions integration with Checkout -->
<!-- Fetched: 2026-04-20 -->

# Build a subscriptions integration with Checkout

Create and manage subscriptions to accept recurring payments with Checkout.

# Hosted page

> This is a Hosted page for when payment-ui is stripe-hosted. View the full page at https://docs.stripe.com/payments/checkout/build-subscriptions?payment-ui=stripe-hosted.

# Hosted page

> This is a Hosted page for when platform is web and ui is stripe-hosted. View the full page at https://docs.stripe.com/payments/checkout/build-subscriptions?platform=web&ui=stripe-hosted.

#### Integration effort

Complexity: 2/5

#### UI customization

Limited customization

- 20 preset fonts
- 3 preset border radius
- Custom background and border color
- Custom logo

#### Integration type

Use prebuilt hosted pages to collect payments and manage your _subscriptions_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis).

[Try it out](https://checkout.stripe.dev/)

## What you’ll build

This guide describes how to sell fixed-price monthly subscriptions using [Stripe Checkout](https://docs.stripe.com/payments/checkout.md).

This guide shows you how to:

- Model your business by building a product catalog.
- Add a Checkout session to your site, including a button and success and cancellation pages.
- Monitor subscription events and provision access to your service.
- Set up the [customer portal](https://docs.stripe.com/customer-management.md).
- Add a customer portal session to your site, including a button and redirect.
- Let customers manage their subscription through the portal.
- Learn how to use [flexible billing mode](https://docs.stripe.com/billing/subscriptions/billing-mode.md) to access enhanced billing behavior and additional features.

If you aren’t ready to code an integration, you can set up basic subscriptions [manually in the Dashboard](https://docs.stripe.com/no-code/subscriptions.md) or use [Payment Links](https://docs.stripe.com/payment-links.md) to set up subscriptions without writing any code.

Learn more about [designing an integration](https://docs.stripe.com/billing/subscriptions/design-an-integration.md) to understand the decisions and required resources for a full integration.

After you complete the integration, you can extend it to:

- Display [taxes](https://docs.stripe.com/payments/checkout/taxes.md)
- Apply [discounts](https://docs.stripe.com/billing/subscriptions/coupons.md#using-coupons-in-checkout)
- Offer customers a [free trial period](https://docs.stripe.com/billing/subscriptions/trials.md)
- Add [payment methods](https://docs.stripe.com/payments/payment-methods/integration-options.md)
- Integrate the [hosted invoice page](https://docs.stripe.com/invoicing/hosted-invoice-page.md)
- Use Checkout in [setup mode](https://docs.stripe.com/payments/save-and-reuse.md)
- Set up [usage-based billing](https://docs.stripe.com/products-prices/pricing-models.md#usage-based-pricing), [pricing tiers](https://docs.stripe.com/products-prices/pricing-models.md#tiered-pricing), and [usage-based pricing](https://docs.stripe.com/products-prices/pricing-models.md#usage-based-pricing)
- Manage [prorations](https://docs.stripe.com/billing/subscriptions/prorations.md)
- Allow customers to [subscribe to multiple products](https://docs.stripe.com/billing/subscriptions/quantities.md#multiple-product-sub)
- Integrate [entitlements](https://docs.stripe.com/billing/entitlements.md) to manage access to your product’s features

## Set up Stripe

Install the Stripe client of your choice:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

Optionally, install the Stripe CLI. The CLI provides [webhook](https://docs.stripe.com/webhooks.md#test-webhook) testing, and you can run it to create your products and prices.
For additional install options, see [Get started with the Stripe CLI](https://docs.stripe.com/stripe-cli.md).

## Create the pricing model [Dashboard or Stripe CLI]

[Recurring pricing models](https://docs.stripe.com/products-prices/pricing-models.md) represent the products or services you sell, how much they cost, what currency you accept for payments, and the service period for subscriptions. To build the pricing model, create [products](https://docs.stripe.com/api/products.md) (what you sell) and [prices](https://docs.stripe.com/api/prices.md) (how much and how often to charge for your products).

This example uses flat-rate pricing with two different service-level options: Basic and Premium. For each service-level option, you need to create a product and a recurring price. To add a one-time charge for something like a setup fee, create a third product with a one-time price.

Each product bills at monthly intervals. The price for the Basic product is 5 USD. The price for the Premium product is 15 USD. See the [flat rate pricing](https://docs.stripe.com/subscriptions/pricing-models/flat-rate-pricing.md) guide for an example with three tiers.

#### Dashboard

Go to the [Add a product](https://dashboard.stripe.com/test/products/create) page and create two products. Add one price for each product, each with a monthly recurring billing period:

- Premium product: Premium service with extra features
  - Price: Flat rate | 15 USD

- Basic product: Basic service with minimum features
  - Price: Flat rate | 5 USD

After you create the prices, record the price IDs so you can use them in other steps. Price IDs look like this: `price_G0FvDp6vZvdwRZ`.

When you’re ready, use the **Copy to live mode** button at the top right of the page to clone your product from [a sandbox to live mode](https://docs.stripe.com/keys.md#test-live-modes).

#### API

You can use the API to create the [Products](https://docs.stripe.com/api/products.md) and [Prices](https://docs.stripe.com/api/prices.md).

Create the Premium product:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const product = await stripe.products.create({
  name: "Billing Guide: Premium Service",
  description: "Premium service with extra features",
});
```

Create the Basic product:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const product = await stripe.products.create({
  name: "Billing Guide: Basic Service",
  description: "Basic service with minimum features",
});
```

Record the product ID for each product. They look like this:

```json
{
  "id": "prod_H94k5odtwJXMtQ",
  "object": "product",
  "active": true,
  "attributes": [],
  "created": 1587577341,
  "description": "Premium service with extra features",
  "images": [],
  "livemode": false,
  "metadata": {},
  "name": "Billing Guide: Premium Service",
  "statement_descriptor": null,
  "type": "service",
  "unit_label": null,
  "updated": 1587577341
}
```

Use the product IDs to create a price for each product. The [unit_amount](https://docs.stripe.com/api/prices/object.md#price_object-unit_amount) number is in cents, so `1500` = 15 USD, for example.

Create the Premium price:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const price = await stripe.prices.create({
  product: "{{PREMIUM_PRODUCT_ID}}",
  unit_amount: 1500,
  currency: "usd",
  recurring: {
    interval: "month",
  },
});
```

Create the Basic price:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const price = await stripe.prices.create({
  product: "{{BASIC_PRODUCT_ID}}",
  unit_amount: 500,
  currency: "usd",
  recurring: {
    interval: "month",
  },
});
```

Record the price ID for each price so you can use them in subsequent steps. They look like this:

```json
{
  "id": "price_HGd7M3DV3IMXkC",
  "object": "price",
  "product": "prod_HGd6W1VUqqXGvr",
  "type": "recurring",
  "currency": "usd",
  "recurring": {
    "interval": "month",
    "interval_count": 1,
    "trial_period_days": null,
    "usage_type": "licensed"
  },
  "active": true,
  "billing_scheme": "per_unit",
  "created": 1589319695,
  "livemode": false,
  "lookup_key": null,
  "metadata": {},
  "nickname": null,
  "unit_amount": 1500,
  "unit_amount_decimal": "1500",
  "tiers": null,
  "tiers_mode": null,
  "transform_quantity": null
}
```

If you offer multiple billing periods, use Checkout to [upsell](https://docs.stripe.com/payments/checkout/upsells.md) customers on longer billing periods and collect more revenue upfront.

For other pricing models, see [Billing examples](https://docs.stripe.com/products-prices/pricing-models.md).

## Create a Checkout Session [Client and Server]

Add a checkout button to your website that calls a server-side endpoint to create a Checkout Session.

```html
<html>
  <head>
    <title>Checkout</title>
  </head>
  <body>
    <form action="/create-checkout-session" method="POST">
      <!-- Note: If using PHP set the action to /create-checkout-session.php -->

      <input type="hidden" name="priceId" value="price_G0FvDp6vZvdwRZ" />
      <button type="submit">Checkout</button>
    </form>
  </body>
</html>
```

On the backend of your application, define an endpoint that [creates the session](https://docs.stripe.com/api/checkout/sessions/create.md) for your frontend to call. You need these values:

- The price ID of the subscription the customer is signing up for (your frontend passes this value)
- Your `success_url`, which is a page on your website that Checkout returns your customer to after they complete the payment

You can optionally:

- Configure a [billing cycle anchor](https://docs.stripe.com/billing/subscriptions/billing-cycle.md) to your subscription in this call.
- Use [custom text](https://docs.stripe.com/payments/checkout/custom-components.md?platform=web&payment-ui=stripe-hosted#customize-text) to include your subscription and cancellation terms, and a link to where your customers can update or cancel their subscription. We recommend configuring [email reminders and notifications](https://docs.stripe.com/invoicing/send-email.md#email-configuration) for your subscribers.

If you created a one-time price in [step 2](https://docs.stripe.com/billing/subscriptions/build-subscriptions.md#create-pricing-model), pass that price ID as well. After creating a Checkout Session, redirect your customer to the [URL](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-url) returned in the response.

You can enable more accurate and predictable subscription behavior when you create a Checkout Session by setting the [billing mode](https://docs.stripe.com/billing/subscriptions/billing-mode.md) type to `flexible`. You must use the Stripe API version [2025-06-30.basil](https://docs.stripe.com/changelog/basil.md#2025-06-30.basil) or later.

> You can use [lookup_keys](https://docs.stripe.com/products-prices/manage-prices.md#lookup-keys) to fetch prices rather than price IDs. For an example, see the [sample application](https://github.com/stripe-samples/subscription-use-cases/tree/main/fixed-price-subscriptions).

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

// The price ID passed from the client
//   const {priceId} = req.body;
const priceId = "{{PRICE_ID}}";

const session = await stripe.checkout.sessions.create({
  mode: "subscription",
  line_items: [
    {
      price: priceId,
      // For usage-based billing, don't pass quantity
      quantity: 1,
    },
  ],
  // {CHECKOUT_SESSION_ID} is a string literal; do not change it!
  // the actual Session ID is returned in the query parameter when your customer
  // is redirected to the success page.
  success_url:
    "https://example.com/success.html?session_id={CHECKOUT_SESSION_ID}",
  subscription_data: {
    billing_mode: { type: "flexible" },
  },
});

// Redirect to the URL returned on the Checkout Session.
// With express, you can redirect with:
//   res.redirect(303, session.url);
```

This example customizes the `success_url` by appending the session ID. Learn more about [customizing your success page](https://docs.stripe.com/payments/checkout/custom-success-page.md).

From your [Dashboard](https://dashboard.stripe.com/settings/payment_methods), enable the payment methods you want to accept from your customers. Checkout supports [several payment methods](https://docs.stripe.com/payments/payment-methods/payment-method-support.md#product-support).

## Provision and monitor subscriptions [Server]

After the subscription signup succeeds, the customer returns to your website at the `success_url`, which initiates a `checkout.session.completed` _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests). When you receive a `checkout.session.completed` event, use [entitlements](https://docs.stripe.com/billing/entitlements.md) to provision the subscription. Continue to provision each month (if billing monthly) as you receive `invoice.paid` events. If you receive an `invoice.payment_failed` event, notify your customer and send them to the customer portal to update their payment method.

To determine the next step for your system’s logic, check the event type and parse the payload of each [event object](https://docs.stripe.com/api/events/object.md), such as `invoice.paid`. Store the `subscription.id` and `customer.id` event objects in your database for verification.

For testing purposes, you can monitor events in the [Events tab](https://dashboard.stripe.com/workbench/events) of [Workbench](https://docs.stripe.com/workbench.md). For production, set up a webhook endpoint and subscribe to appropriate event types. If you don’t know your `STRIPE_WEBHOOK_SECRET` key, go to the destination details view of the [Webhooks tab](https://dashboard.stripe.com/workbench/webhooks) in Workbench to view it.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

app.post("/webhook", async (req, res) => {
  let data;
  let eventType;
  // Check if webhook signing is configured.
  const webhookSecret = "{{STRIPE_WEBHOOK_SECRET}}"; // Example: whsec_c7681Dm
  if (webhookSecret) {
    // Retrieve the event by verifying the signature using the raw body and secret.
    let event;
    let signature = req.headers["stripe-signature"];

    try {
      event = stripe.webhooks.constructEvent(
        req.body,
        signature,
        webhookSecret,
      );
    } catch (err) {
      console.log(`⚠️  Webhook signature verification failed.`);
      return res.sendStatus(400);
    }
    // Extract the object from the event.
    data = event.data;
    eventType = event.type;
  } else {
    // Webhook signing is recommended, but if the secret is not configured in `config.js`,
    // retrieve the event data directly from the request body.
    data = req.body.data;
    eventType = req.body.type;
  }

  switch (eventType) {
    case "checkout.session.completed":
      // Payment is successful and the subscription is created.
      // You should provision the subscription and save the customer ID to your database.
      break;
    case "invoice.paid":
      // Continue to provision the subscription as payments continue to be made.
      // Store the status in your database and check when a user accesses your service.
      // This approach helps you avoid hitting rate limits.
      break;
    case "invoice.payment_failed":
      // The payment failed or the customer doesn't have a valid payment method.
      // The subscription becomes past_due. Notify your customer and send them to the
      // customer portal to update their payment information.
      break;
    default:
    // Unhandled event type
  }

  res.sendStatus(200);
});
```

The minimum event types to monitor:

| Event name                   | Description                                                                                        |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| `checkout.session.completed` | Sent when a customer successfully completes the Checkout Session, informing you of a new purchase. |
| `invoice.paid`               | Sent each billing period when a payment succeeds.                                                  |
| `invoice.payment_failed`     | Sent each billing period if there’s an issue with your customer’s payment method.                  |

For even more events to monitor, see [Subscription webhooks](https://docs.stripe.com/billing/subscriptions/webhooks.md).

## Configure the customer portal [Dashboard]

The [customer portal](https://docs.stripe.com/customer-management.md) lets your customers directly manage their existing subscriptions and invoices.

Use the [Dashboard](https://dashboard.stripe.com/test/settings/billing/portal) to configure the portal. At a minimum, make sure to [configure the portal](https://docs.stripe.com/customer-management.md) so that customers can update their payment methods.

## Create a portal session [Server]

Define an endpoint that [creates the customer portal session](https://docs.stripe.com/api/customer_portal/sessions/create.md) for your frontend to call. The `CUSTOMER_ID` refers to the customer ID created by a Checkout Session that you saved while processing the `checkout.session.completed` event. You can also set a default redirect link for the portal in the Dashboard.

Pass an optional `return_url` value for the page on your site to redirect your customer to after they finish managing their subscription:

#### Accounts v2

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

// This is the url to which the customer will be redirected when they're done
// managing their billing with the portal.
const returnUrl = "{{DOMAIN_URL}}"; // Example: http://example.com
const customerAccountId = "{{CUSTOMER_ACCOUNT_ID}}"; // Example: acct_GBV60HKsE0mb5v

const portalSession = await stripe.billingPortal.sessions.create({
  customer_account: customerAccountId,
  return_url: returnUrl,
});

// Redirect to the URL for the session
//   res.redirect(303, portalSession.url);
```

#### Customers v1

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

// This is the url to which the customer will be redirected when they're done
// managing their billing with the portal.
const returnUrl = "{{DOMAIN_URL}}"; // Example: http://example.com
const customerId = "{{CUSTOMER_ID}}"; // Example: cus_GBV60HKsE0mb5v

const portalSession = await stripe.billingPortal.sessions.create({
  customer: customerId,
  return_url: returnUrl,
});

// Redirect to the URL for the session
//   res.redirect(303, portalSession.url);
```

## Send customers to the customer portal [Client]

On your frontend, add a button to the page at the `success_url` that provides a link to the customer portal:

```html
<html>
  <head>
    <title>Manage Billing</title>
  </head>
  <body>
    <form action="/customer-portal" method="POST">
      <!-- Note: If using PHP set the action to /customer-portal.php -->
      <button type="submit">Manage Billing</button>
    </form>
  </body>
</html>
```

After exiting the customer portal, the customer returns to your website at the `return_url`. Continue to [monitor events](https://docs.stripe.com/billing/subscriptions/webhooks.md) to track the status of the customer’s subscription.

If you configure the customer portal to allow actions such as canceling a subscription, [monitor additional events](https://docs.stripe.com/customer-management/integrate-customer-portal.md#webhooks).

## Test your integration

### Test payment methods

Use the following table to test different payment methods and scenarios.

| Payment method    | Scenario                                                                                                                                                                                                                                                                                      | How to test                                                                                                                                                                                                 |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| BECS Direct Debit | Your customer successfully pays with BECS Direct Debit.                                                                                                                                                                                                                                       | Fill out the form using the account number `900123456` and BSB `000000`. The confirmed PaymentIntent initially transitions to `processing`, then transitions to the `succeeded` status three minutes later. |
| BECS Direct Debit | Your customer’s payment fails with an `account_closed` error code.                                                                                                                                                                                                                            | Fill out the form using the account number `111111113` and BSB `000000`.                                                                                                                                    |
| Credit card       | The card payment succeeds and doesn’t require authentication.                                                                                                                                                                                                                                 | Fill out the credit card form using the credit card number `4242 4242 4242 4242` with any expiration, CVC, and postal code.                                                                                 |
| Credit card       | The card payment requires _authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase). | Fill out the credit card form using the credit card number `4000 0025 0000 3155` with any expiration, CVC, and postal code.                                                                                 |
| Credit card       | The card is declined with a decline code like `insufficient_funds`.                                                                                                                                                                                                                           | Fill out the credit card form using the credit card number `4000 0000 0000 9995` with any expiration, CVC, and postal code.                                                                                 |
| SEPA Direct Debit | Your customer successfully pays with SEPA Direct Debit.                                                                                                                                                                                                                                       | Fill out the form using the account number `AT321904300235473204`. The confirmed PaymentIntent initially transitions to processing, then transitions to the succeeded status three minutes later.           |
| SEPA Direct Debit | Your customer’s PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                                                                                                                                              | Fill out the form using the account number `AT861904300235473202`.                                                                                                                                          |

### Monitor events

Set up webhooks to listen to subscription change events, such as upgrades and cancellations. You can view [subscription webhook events](https://docs.stripe.com/billing/subscriptions/webhooks.md) in the [Dashboard](https://dashboard.stripe.com/test/events) or with the [Stripe CLI](https://docs.stripe.com/webhooks.md#test-webhook).

Learn more about [testing your Billing integration](https://docs.stripe.com/billing/testing.md).

## See also

- [Offer customers a free trial period](https://docs.stripe.com/billing/subscriptions/trials.md)
- [Apply discounts](https://docs.stripe.com/billing/subscriptions/coupons.md#using-coupons-in-checkout)
- [Manage prorations](https://docs.stripe.com/billing/subscriptions/prorations.md)
- [Integrate entitlements to manage access to your product’s features](https://docs.stripe.com/billing/entitlements.md)

# Embedded page

> This is a Embedded page for when payment-ui is embedded-form. View the full page at https://docs.stripe.com/payments/checkout/build-subscriptions?payment-ui=embedded-form.

# Embedded page

> This is a Embedded page for when platform is web and ui is embedded-form. View the full page at https://docs.stripe.com/payments/checkout/build-subscriptions?platform=web&ui=embedded-form.

#### Integration effort

Complexity: 2/5

#### UI customization

Customize the appearance.

#### Integration type

Use prebuilt embedded forms to collect payments and manage _subscriptions_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis).

## Set up the server

### Set up Stripe

Install the Stripe client of your choice:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

### Create a product and price

[Recurring pricing models](https://docs.stripe.com/products-prices/pricing-models.md) represent the products or services you sell, how much they cost, what currency you accept for payments, and the service period for subscriptions. To build the pricing model, create [products](https://docs.stripe.com/api/products.md) (what you sell) and [prices](https://docs.stripe.com/api/prices.md) (how much and how often to charge for your products).

This example uses flat-rate pricing with two different service-level options: Basic and Premium. For each service-level option, you need to create a product and a recurring price. To add a one-time charge for something like a setup fee, create a third product with a one-time price.

Each product bills at monthly intervals. The price for the Basic product is 5 USD. The price for the Premium product is 15 USD. See the [flat rate pricing](https://docs.stripe.com/subscriptions/pricing-models/flat-rate-pricing.md) guide for an example with three tiers.

#### Dashboard

Go to the [Add a product](https://dashboard.stripe.com/test/products/create) page and create two products. Add one price for each product, each with a monthly recurring billing period:

- Premium product: Premium service with extra features
  - Price: Flat rate | 15 USD

- Basic product: Basic service with minimum features
  - Price: Flat rate | 5 USD

After you create the prices, record the price IDs so you can use them in other steps. Price IDs look like this: `price_G0FvDp6vZvdwRZ`.

When you’re ready, use the **Copy to live mode** button at the top right of the page to clone your product from [a sandbox to live mode](https://docs.stripe.com/keys.md#test-live-modes).

#### API

You can use the API to create the [Products](https://docs.stripe.com/api/products.md) and [Prices](https://docs.stripe.com/api/prices.md).

Create the Premium product:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const product = await stripe.products.create({
  name: "Billing Guide: Premium Service",
  description: "Premium service with extra features",
});
```

Create the Basic product:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const product = await stripe.products.create({
  name: "Billing Guide: Basic Service",
  description: "Basic service with minimum features",
});
```

Record the product ID for each product. They look like this:

```json
{
  "id": "prod_H94k5odtwJXMtQ",
  "object": "product",
  "active": true,
  "attributes": [],
  "created": 1587577341,
  "description": "Premium service with extra features",
  "images": [],
  "livemode": false,
  "metadata": {},
  "name": "Billing Guide: Premium Service",
  "statement_descriptor": null,
  "type": "service",
  "unit_label": null,
  "updated": 1587577341
}
```

Use the product IDs to create a price for each product. The [unit_amount](https://docs.stripe.com/api/prices/object.md#price_object-unit_amount) number is in cents, so `1500` = 15 USD, for example.

Create the Premium price:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const price = await stripe.prices.create({
  product: "{{PREMIUM_PRODUCT_ID}}",
  unit_amount: 1500,
  currency: "usd",
  recurring: {
    interval: "month",
  },
});
```

Create the Basic price:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const price = await stripe.prices.create({
  product: "{{BASIC_PRODUCT_ID}}",
  unit_amount: 500,
  currency: "usd",
  recurring: {
    interval: "month",
  },
});
```

Record the price ID for each price so you can use them in subsequent steps. They look like this:

```json
{
  "id": "price_HGd7M3DV3IMXkC",
  "object": "price",
  "product": "prod_HGd6W1VUqqXGvr",
  "type": "recurring",
  "currency": "usd",
  "recurring": {
    "interval": "month",
    "interval_count": 1,
    "trial_period_days": null,
    "usage_type": "licensed"
  },
  "active": true,
  "billing_scheme": "per_unit",
  "created": 1589319695,
  "livemode": false,
  "lookup_key": null,
  "metadata": {},
  "nickname": null,
  "unit_amount": 1500,
  "unit_amount_decimal": "1500",
  "tiers": null,
  "tiers_mode": null,
  "transform_quantity": null
}
```

If you offer multiple billing periods, use Checkout to [upsell](https://docs.stripe.com/payments/checkout/upsells.md) customers on longer billing periods and collect more revenue upfront.

For other pricing models, see [Billing examples](https://docs.stripe.com/products-prices/pricing-models.md).

### Create a Checkout Session

Add an endpoint on your server that creates a _Checkout Session_ (A Checkout Session represents your customer's session as they pay for one-time purchases or subscriptions through Checkout. After a successful payment, the Checkout Session contains a reference to the Customer, and either the successful PaymentIntent or an active Subscription).

When you create the [Checkout Session](https://docs.stripe.com/api/checkout/sessions/create.md), pass the following parameters:

- To use the embedded_page payment form, set [ui_mode](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-ui_mode) to `embedded`.
- To create subscriptions when your customer checks out, set [mode](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-mode) to `subscription`.
- To define the page your customer returns to after completing or attempting payment, specify a [return_url](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-return_url). Include the `{CHECKOUT_SESSION_ID}` template variable in the URL. Checkout replaces the variable with the Checkout Session ID before redirecting your customer. You create and host the return page on your website.
- To include your subscription and cancellation terms, and a link to where your customers can update or cancel their subscription, optionally use [custom text](https://docs.stripe.com/payments/checkout/custom-components.md?ui=embedded-form#customize-payment-method-reuse-agreement-and-subscription-terms). We recommend configuring [email reminders and notifications](https://docs.stripe.com/invoicing/send-email.md#email-configuration) for your subscribers.

To mount Checkout, use the Checkout Session’s `client_secret` returned in the response.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  mode: "subscription",
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  ui_mode: "embedded_page",
  return_url:
    "https://example.com/checkout/return?session_id={CHECKOUT_SESSION_ID}",
});
```

## Build your subscription page [Client]

### Mount Checkout

#### HTML + JS

#### Load Stripe.js

Use _Stripe.js_ (Use Stripe.js’ APIs to tokenize customer information, collect sensitive card data, and accept payments with browser payment APIs) to remain _PCI compliant_ (Any party involved in processing, transmitting, or storing credit card data must comply with the rules specified in the Payment Card Industry (PCI) Data Security Standards. PCI compliance is a shared responsibility and applies to both Stripe and your business) by ensuring that payment details are sent directly to Stripe without hitting your server. Always load Stripe.js from js.stripe.com to remain compliant. Don’t include the script in a bundle or host it yourself.

#### Define the payment form

To securely collect the customer’s information, create an empty placeholder `div`. Stripe inserts an iframe into the `div`.

Checkout is available as part of [Stripe.js](https://docs.stripe.com/js.md). Include the Stripe.js script on your page by adding it to the head of your HTML file. Next, create an empty DOM node (container) to use for mounting.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Accept a payment</title>
    <meta name="description" content="A demo of a payment on Stripe" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="stylesheet" href="style.css" />
    <!-- Add the Stripe.js script here -->
    <script src="https://js.stripe.com/dahlia/stripe.js"></script>
    <script src="checkout.js" defer></script>
  </head>
  <body>
    <!-- Display a payment form -->
    <div id="checkout">
      <!-- Checkout inserts the payment form here -->
    </div>
  </body>
</html>
```

#### Initialize Stripe.js

Initialize Stripe.js with your publishable API key.

#### Fetch a Checkout Session client secret

Create an asynchronous `fetchClientSecret` function that makes a request to your server to [create a Checkout Session](https://docs.stripe.com/api/checkout/sessions/create.md) and retrieve the client secret.

#### Initialize Checkout

Initialize Checkout with your `fetchClientSecret` function and mount it to the placeholder `<div>` in your payment form. Checkout is rendered in an iframe that securely sends payment information to Stripe over an HTTPS connection.

Avoid placing Checkout within another iframe because some payment methods require redirecting to another page for payment confirmation.

```javascript
// Initialize Stripe.js
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");

initialize();

// Fetch Checkout Session and retrieve the client secret
async function initialize() {
  const fetchClientSecret = async () => {
    const response = await fetch("/create-checkout-session", {
      method: "POST",
    });
    const { clientSecret } = await response.json();
    return clientSecret;
  };

  // Initialize Checkout
  const checkout = await stripe.createEmbeddedCheckoutPage({
    fetchClientSecret,
  });

  // Mount Checkout
  checkout.mount("#checkout");
}
```

#### React

#### Add Stripe to your React app

Install [React Stripe.js](https://docs.stripe.com/sdks/stripejs-react.md) to stay PCI compliant by ensuring that payment details go directly to Stripe and never reach your server.

```bash
npm install --save @stripe/react-stripe-js @stripe/stripe-js
```

#### Load Stripe.js

To configure the Stripe library, call `loadStripe()` with your Stripe publishable API key. Create an `EmbeddedCheckoutProvider`. Pass the returned `Promise` to the provider.

#### Fetch a Checkout Session client secret

Create an asynchronous `fetchClientSecret` function that makes a request to your server to [create a Checkout Session](https://docs.stripe.com/api/checkout/sessions/create.md) and retrieve the client secret.

#### Initialize Checkout

To allow the child components to access the Stripe service through the embedded Checkout consumer, pass the resulting promise from `loadStripe` and the `fetchClientSecret` function as an `option` to the embedded Checkout provider.

```jsx
import * as React from "react";
import { loadStripe } from "@stripe/stripe-js";
import {
  EmbeddedCheckoutProvider,
  EmbeddedCheckout,
} from "@stripe/react-stripe-js";

// Make sure to call `loadStripe` outside of a component's render to avoid
// recreating the `Stripe` object on every render.
const stripePromise = loadStripe("pk_test_123", {});

const App = ({ fetchClientSecret }) => {
  const options = { fetchClientSecret };

  return (
    <EmbeddedCheckoutProvider stripe={stripePromise} options={options}>
      <EmbeddedCheckout />
    </EmbeddedCheckoutProvider>
  );
};
```

## Show a return page

After your customer attempts payment, Stripe redirects them to a return page that you host on your site. When you created the Checkout Session, you specified the URL of the return page in the [return_url](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-return_url) parameter.

> During payment, some payment methods redirect the customer to an intermediate page, such as a bank authorization page. When the customer completes that page, Stripe redirects them to your return page.

#### Create an endpoint to retrieve a Checkout Session

Add an endpoint to retrieve a Checkout Session status with the Checkout Session ID in the URL.

#### Retrieve a Checkout Session

To use details for the Checkout Session, immediately make a request to the endpoint on your server to [retrieve the Checkout Session](https://docs.stripe.com/api/checkout/sessions/retrieve.md) status using the Checkout Session ID in the URL as soon as your return page loads.

#### Handle the session

Handle the result based on the session status:

- `complete`: The payment succeeded. Use the information from the Checkout Session to render a success page.
- `open`: The payment failed or was canceled. Remount Checkout so that your customer can try again.

```js
// Retrieve a Checkout Session
// Use the session ID
initialize();

async function initialize() {
  const queryString = window.location.search;
  const urlParams = new URLSearchParams(queryString);
  const sessionId = urlParams.get("session_id");
  const response = await fetch(`/session-status?session_id=${sessionId}`);
  const session = await response.json();
  // Handle the session according to its status
  if (session.status == "open") {
    // Remount embedded Checkout
    window.location.replace("http://localhost:4242/checkout.html");
  } else if (session.status == "complete") {
    document.getElementById("success").classList.remove("hidden");
    document.getElementById("customer-email").textContent =
      session.customer_email;
    // Show success page
    // Optionally use session.payment_status or session.customer_email
    // to customize the success page
  }
}
```

#### Accounts v2

```javascript
// Add an endpoint to fetch the Checkout Session status
app.get("/session_status", async (req, res) => {
  const session = await stripe.checkout.sessions.retrieve(req.query.session_id);
  const customer_account = await stripe.v2.core.accounts(
    session.customer_account,
  );

  res.send({
    status: session.status,
    payment_status: session.payment_status,
    customer_email: customer_account.contact_email,
  });
});
```

#### Customers v1

```javascript
// Add an endpoint to fetch the Checkout Session status
app.get("/session_status", async (req, res) => {
  const session = await stripe.checkout.sessions.retrieve(req.query.session_id);
  const customer = await stripe.customers.retrieve(session.customer);

  res.send({
    status: session.status,
    payment_status: session.payment_status,
    customer_email: customer.email,
  });
});
```

## Optional: Configure the customer portal

You can set up the _customer portal_ (The customer portal is a secure, Stripe-hosted page that lets your customers manage their subscriptions and billing details) to let your customers directly manage their existing subscriptions and invoices.

You can configure the portal in the Dashboard. To reduce churn, you can configure the portal to allow customers to update their payment methods in the case of failed payments.

To help customers find it, add a button on your website to redirect to the customer portal to allow customers to manage their subscription. Clicking this button redirects your customer to the Stripe-hosted customer portal page.

Learn more about the [customer portal](https://docs.stripe.com/customer-management.md) and other customer management options.

#### Create a portal session

To add a customer portal, define an endpoint that [creates the customer portal session](https://docs.stripe.com/api/customer_portal/sessions/create.md) for your front end to call. Include the ID of the customer created by the Checkout Session that you saved while processing the `checkout.session.completed` webhook. You can also set a default redirect link for the portal in the Dashboard.

Pass an optional `return_url` value for the page on your site to redirect your customer to after they finish managing their subscription:

#### Accounts v2

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

// This is the url to which the customer will be redirected when they're done
// managing their billing with the portal.
const returnUrl = "{{DOMAIN_URL}}"; // Example: http://example.com
const customerAccountId = "{{CUSTOMER_ACCOUNT_ID}}"; // Example: acct_GBV60HKsE0mb5v

const portalSession = await stripe.billingPortal.sessions.create({
  customer_account: customerAccountId,
  return_url: returnUrl,
});

// Redirect to the URL for the session
//   res.redirect(303, portalSession.url);
```

#### Customers v1

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

// This is the url to which the customer will be redirected when they're done
// managing their billing with the portal.
const returnUrl = "{{DOMAIN_URL}}"; // Example: http://example.com
const customerId = "{{CUSTOMER_ID}}"; // Example: cus_GBV60HKsE0mb5v

const portalSession = await stripe.billingPortal.sessions.create({
  customer: customerId,
  return_url: returnUrl,
});

// Redirect to the URL for the session
//   res.redirect(303, portalSession.url);
```

#### Send customers to the customer portal

On your front end, add a button to the page at the `success_url` that provides a link to the customer portal:

```html
<html>
  <head>
    <title>Manage Billing</title>
  </head>
  <body>
    <form action="/customer-portal" method="POST">
      <!-- Note: If using PHP set the action to /customer-portal.php -->
      <button type="submit">Manage Billing</button>
    </form>
  </body>
</html>
```

After exiting the customer portal, the customer returns to your website at the `return_url`. Continue to [monitor events](https://docs.stripe.com/billing/subscriptions/webhooks.md) to track the status of the customer’s subscription.

If you configure the customer portal to allow actions such as canceling a subscription, make sure to monitor [additional events](https://docs.stripe.com/customer-management/integrate-customer-portal.md#webhooks).

## Provision access

When the subscription is active, give your user access to your service. To do this, listen to the `customer.subscription.created`, `customer.subscription.updated`, and `customer.subscription.deleted` events. These events pass a `Subscription` object that contains a `status` field indicating whether the subscription is active, past due, or canceled. See the [subscription lifecycle](https://docs.stripe.com/billing/subscriptions/overview.md#subscription-lifecycle) for a complete list of statuses. To manage access to your product’s feature, learn about [integrating entitlements](https://docs.stripe.com/billing/entitlements.md).

In your webhook handler:

1. Verify the subscription status. If it’s `active`, your user has paid for your product.
1. Check the product that your customer subscribed to, and grant them access to your service. Checking the product instead of the price allows you to change the pricing or billing period, as needed.
1. Store the `product.id`, `subscription.id`, and `subscription.status` in your database, along with either the `customer_account.id` or the `customer.id` you already saved. Check this record when determining which features to enable for the user in your application.

The subscription status might change at any point during its lifetime, even if your application doesn’t directly make any calls to Stripe. For example, a renewal might fail because of an expired credit card, which puts the subscription in a past due status. Or, if you implement the [customer portal](https://docs.stripe.com/customer-management.md), a user might cancel their subscription without directly visiting your application. Implementing your handler correctly keeps your application status in sync with Stripe.

## Test your integration

### Test payment methods

Use the following table to test different payment methods and scenarios.

| Payment method    | Scenario                                                                                                                                                                                                                                                                                      | How to test                                                                                                                                                                                                 |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| BECS Direct Debit | Your customer successfully pays with BECS Direct Debit.                                                                                                                                                                                                                                       | Fill out the form using the account number `900123456` and BSB `000000`. The confirmed PaymentIntent initially transitions to `processing`, then transitions to the `succeeded` status three minutes later. |
| BECS Direct Debit | Your customer’s payment fails with an `account_closed` error code.                                                                                                                                                                                                                            | Fill out the form using the account number `111111113` and BSB `000000`.                                                                                                                                    |
| Credit card       | The card payment succeeds and doesn’t require authentication.                                                                                                                                                                                                                                 | Fill out the credit card form using the credit card number `4242 4242 4242 4242` with any expiration, CVC, and postal code.                                                                                 |
| Credit card       | The card payment requires _authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase). | Fill out the credit card form using the credit card number `4000 0025 0000 3155` with any expiration, CVC, and postal code.                                                                                 |
| Credit card       | The card is declined with a decline code like `insufficient_funds`.                                                                                                                                                                                                                           | Fill out the credit card form using the credit card number `4000 0000 0000 9995` with any expiration, CVC, and postal code.                                                                                 |
| SEPA Direct Debit | Your customer successfully pays with SEPA Direct Debit.                                                                                                                                                                                                                                       | Fill out the form using the account number `AT321904300235473204`. The confirmed PaymentIntent initially transitions to processing, then transitions to the succeeded status three minutes later.           |
| SEPA Direct Debit | Your customer’s PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                                                                                                                                              | Fill out the form using the account number `AT861904300235473202`.                                                                                                                                          |

### Monitor events

Set up webhooks to listen to subscription change events, such as upgrades and cancellations. You can view [subscription webhook events](https://docs.stripe.com/billing/subscriptions/webhooks.md) in the [Dashboard](https://dashboard.stripe.com/test/events) or with the [Stripe CLI](https://docs.stripe.com/webhooks.md#test-webhook).

Learn more about [testing your Billing integration](https://docs.stripe.com/billing/testing.md).
