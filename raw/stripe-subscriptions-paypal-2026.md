<!-- Source URL: https://docs.stripe.com/billing/subscriptions/paypal -->
<!-- Fetched: 2026-05-13 -->

# Set up a subscription with PayPal

Learn how to create and charge for a subscription with PayPal.

# Stripe-hosted page

> This is a Stripe-hosted page for when payments-ui-type is stripe-hosted. View the full page at https://docs.stripe.com/billing/subscriptions/paypal?payments-ui-type=stripe-hosted.

Check out the [sample on GitHub](https://github.com/stripe-samples/checkout-single-subscription) or explore the [demo](https://checkout.stripe.dev/checkout).

Use this guide to set up a _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) using [PayPal](https://docs.stripe.com/payments/paypal.md) and _Checkout_ (A low-code payment integration that creates a customizable form for collecting payments. You can embed Checkout directly in your website, redirect customers to a Stripe-hosted payment page, or create a customized checkout page with Stripe Elements).

A [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md) represents the details of a customer’s intent to purchase. Create a Checkout Session when a customer wants to start a subscription. After redirecting a customer to a Checkout Session, Stripe presents a payment form where they can complete their purchase. After they complete a purchase, Stripe redirects them back to your site.

> #### Enable PayPal recurring payments
>
> Stripe automatically enables recurring payments for most users when they [activate PayPal payments](https://docs.stripe.com/payments/paypal/activate.md) in the Stripe Dashboard. However, due to PayPal’s policies and regional restrictions, you might need to manually [enable](https://docs.stripe.com/payments/paypal/set-up-future-payments.md#enable-recurring-payments) PayPal recurring payments in the Dashboard.

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create recurring products and prices

> The Prices API unifies how one-time purchases and subscriptions are modeled on Stripe. Existing integrations that don’t use the Prices API are still [supported](https://support.stripe.com/questions/prices-api-and-existing-checkout-integrations). However, some Checkout features only support Prices. See the [migration guide](https://docs.stripe.com/payments/checkout/migrating-prices.md) to upgrade to the Prices API.

To use Checkout, you first need to create a _Product_ (Products represent what your business sells—whether that's a good or a service) and a _Price_ (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions). Different physical goods or levels of service must be represented by products. Each product’s pricing is represented by one or more prices.

For example, you can create a software _product_ that has four _prices_: 10 USD/month, 100 USD/year, 9 eur/month, and 90 eur/year. This allows you to change and add prices without needing to change the details of your underlying products. You can either create a product and price [through the API](https://docs.stripe.com/api/prices.md) or through [the Stripe Dashboard](https://dashboard.stripe.com/products).

If your price is determined at checkout (for example, the customer sets a donation amount) or you prefer not to create prices upfront, you can create [prices inline](https://docs.stripe.com/billing/subscriptions/paypal.md#creating-prices-inline) at Checkout Session creation.

#### Dashboard

Before you start configuring products, make sure you’re in a sandbox. Next, define the goods and services you plan to sell. To create a new product and price:

- Go to the [Products](https://dashboard.stripe.com/products) section in the Dashboard
- Click **Add product**
- Select “Recurring” when setting the price
- Configure the pricing plan

You can define multiple pricing plans with different parameters for each recurring product. Each price has a generated ID that you can use as a reference during the checkout process.

> Products created in a sandbox can be copied to live mode so that you don’t need to re-create them. In the Product detail view in the Dashboard, click **Copy to live mode** on the upper right corner. You can only do this once for each product created in a sandbox. Subsequent updates to the test product aren’t reflected for the live product.

#### API

To create a basic [Product](https://docs.stripe.com/api/products.md) through the API, only the `name` field is required. The product `name`, `description`, and `images` that you supply are displayed to customers on Checkout.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const product = await stripe.products.create({
  name: "Blue banana",
});
```

Next, create a [Price](https://docs.stripe.com/api/prices.md) to define how much and how often to charge for your product. This includes how much the product costs, what currency to use, and its billing interval.

#### Node.js

```javascript
const price = await stripe.prices.create({
  product: "{{PRODUCT_ID}}",
  unit_amount: 1000,
  currency: "eur",
  recurring: {
    interval: "month",
  },
});
```

This price ID is how you refer to the product when you start the payment process with Checkout.

## Create a Checkout Session [Client-side] [Server-side]

Add a checkout button to your website that calls a server-side endpoint to create a Checkout Session.

```html
<html>
  <head>
    <title>Checkout</title>
  </head>
  <body>
    <form action="/create-checkout-session" method="POST">
      <button type="submit">Checkout</button>
    </form>
  </body>
</html>
```

### Checkout Session parameters

See [Create a Checkout Session](https://docs.stripe.com/api/checkout/sessions/create.md) for a complete list of parameters that you can use.

Create a Checkout Session with the ID of an existing [Price](https://docs.stripe.com/api/prices.md). Make sure that mode is set to `subscription` and you pass at least one recurring price. You can add one-time prices in addition to recurring prices. After creating the Checkout Session, redirect your customer to the [URL](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-url) returned in the response.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  payment_method_types: ["paypal"],

  // or you can take multiple payment methods with
  // payment_method_types: ['card', 'paypal', ...]
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  mode: "subscription",
  success_url: "https://example.com/success?session_id={CHECKOUT_SESSION_ID}",
});

// Record the session ID in your system
const session_id = session.id;

// 303 redirect to session.url
```

When your customer successfully completes their payment, they’re redirected to the `success_url`, a page on your website that informs the customer that their payment was successful. Make the Session ID available on your success page by including the `{CHECKOUT_SESSION_ID}` template variable in the `success_url` as in the above example.

Checkout Sessions expire 24 hours after creation by default.

> Don’t rely on the redirect to the `success_url` alone for detecting payment initiation, because:
>
> - Malicious users could directly access the `success_url` without paying and gain access to your goods or services.

- After a successful payment, customers might close their browser tab before they’re redirected to the `success_url`.

## Confirm the payment is successful

> When a buyer successfully confirms a subscription on Stripe with PayPal, they receive a receipt from Stripe as well as from PayPal.

When your customer completes a payment, they’re redirected to the URL that you specified as the `success_url`. This is typically a page on your website that informs your customer that their payment was successful.

Use the Dashboard, a custom _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a third-party plugin to handle post-payment events like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

#### Dashboard

Successful payments appear in the Dashboard’s [list of payments](https://dashboard.stripe.com/payments). When you click a payment, it takes you to the Payment details page. The **Checkout summary** section contains billing information and the list of items purchased, which you can use to manually fulfill the order.
![Checkout summary](assets/stripe-ach-checkout-success.png)

> Stripe can help you keep up with incoming payments by sending you email notifications whenever a customer successfully completes one. Use the Dashboard to [configure email notifications](https://dashboard.stripe.com/settings/user).

#### Webhooks

[Set up webhooks](https://docs.stripe.com/webhooks.md) to programmatically handle post-payment events. The quickest way to develop and test webhooks locally is with the [Stripe CLI](https://docs.stripe.com/stripe-cli.md). Once you have it installed, you can forward events to your server:

```bash
stripe listen --forward-to localhost:4242/webhook
Ready! Your webhook signing secret is '{{WEBHOOK_SIGNING_SECRET}}' (^C to quit)
```

With a webhook endpoint, your customer is redirected to the `success_url` when you [acknowledged you received the event](https://docs.stripe.com/webhooks.md#acknowledge-events-immediately). In scenarios where your endpoint is down or the event isn’t acknowledged properly, your customer is redirected to the `success_url` 10 seconds after a successful payment.

The following example endpoint demonstrates how to acknowledge and handle events.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

// Find your endpoint's secret in your Dashboard's webhook settings
const endpointSecret = "whsec_...";

// Using Express
const app = require("express")();

// Use body-parser to retrieve the raw body as a buffer
const bodyParser = require("body-parser");

// Match the raw body to content type application/json
app.post(
  "/webhook",
  bodyParser.raw({ type: "application/json" }),
  (request, response) => {
    const sig = request.headers["stripe-signature"];

    let event;

    try {
      event = stripe.webhooks.constructEvent(request.body, sig, endpointSecret);
    } catch (err) {
      return response.status(400).send(`Webhook Error: ${err.message}`);
    }

    // Handle the checkout.session.completed event
    if (event.type === "checkout.session.completed") {
      const session = event.data.object;

      // Fulfill the purchase...
      handleCheckoutSession(session);
    }

    // Return a response to acknowledge receipt of the event
    response.json({ received: true });
  },
);

app.listen(8000, () => console.log("Running on port 8000"));
```

You can use plugins like [Zapier](https://stripe.com/works-with/zapier) to automate updating your purchase fulfillment systems with information from Stripe payments.

Some examples of automation supported by plugins include:

- Updating spreadsheets used for order tracking in response to successful payments
- Updating inventory management systems in response to successful payments
- Triggering notifications to internal customer service teams using email or chat applications

## Test the integration

Test your PayPal integration with your [test API keys](https://docs.stripe.com/keys.md#test-live-modes) by viewing the redirect page. You can test the successful payment case by authenticating the payment on the redirect page. The PaymentIntent will transition from `requires_action` to `succeeded`.

To test the case where the user fails to authenticate, use your test API keys and view the redirect page. On the redirect page, click **Fail test payment**. The PaymentIntent will transition from `requires_action` to `requires_payment_method`.

## Optional: Adding a one-time setup fee [Server-side]

In addition to passing recurring prices, you can add one-time prices in `subscription` mode. These are only on the initial _invoice_ (Invoices are statements of amounts owed by a customer. They track the status of payments from draft through paid or otherwise finalized. Subscriptions automatically generate invoices, or you can manually create a one-off invoice) created by the subscription. This is useful for adding setup fees or other one-time fees associated with a subscription.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  payment_method_types: ["paypal"],

  // or you can take multiple payment methods with
  // payment_method_types: ['card', 'paypal', ...]
  line_items: [
    {
      price: "{{RECURRING_PRICE_ID}}",
      quantity: 1,
    },
    {
      price: "{{ONE_TIME_PRICE_ID}}",
      quantity: 1,
    },
  ],
  mode: "subscription",
  success_url: "https://example.com/success?session_id={CHECKOUT_SESSION_ID}",
});
```

## Optional: Create prices and products inline [Server-side]

In addition to passing in existing price IDs, you can also define your item price at Checkout session creation. First define a [Product](https://docs.stripe.com/api/products.md). Then create a Checkout session using the product ID, by passing it into [price_data](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items-price_data) with the `unit_amount`, `currency`, and `recurring` details:

#### Node.js

```javascript

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({payment_method_types: ['paypal'],

  // or you can take multiple payment methods with
  // payment_method_types: ['card', 'paypal', ...]line_items: [{
    price_data: {
      unit_amount: 5000,
      currency: 'eur',
      product: '{{PRODUCT_ID}}',
      recurring: {
        interval: 'month'
      },
    },
    quantity: 1
  }],
  mode: 'subscription',
  success_url: 'https://example.com/success?session_id={CHECKOUT_SESSION_ID}'
});
```

If you also need to create products inline, you can do so with [product_data](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items-price_data-product_data):

#### Node.js

```javascript

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({payment_method_types: ['paypal'],

  // or you can take multiple payment methods with
  // payment_method_types: ['card', 'paypal', ...]line_items: [{
    price_data: {
      currency: 'eur',
      product_data: {
        name: 'T-shirt'
      },
      unit_amount: 2000
    },
    quantity: 1
  }],
  mode: 'subscription',
  success_url: 'https://example.com/success?session_id={CHECKOUT_SESSION_ID}'
});
```

## Optional: Existing customers [Server-side]

#### Accounts v2

If you’ve previously created a customer-configured `Account` object to represent a customer, use the [customer_account](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer_account) argument to pass their `Account` ID when creating a Checkout Session. This ensures that all objects created during the Session are associated with the correct `Account` object.

When you pass an `Account` ID, Stripe also uses the email stored on the `Account` object to prefill the email field on the Checkout page. If the customer changes their email on the Checkout page, it updates on the `Account` object after a successful payment.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  customer_account: "{{CUSTOMER_ACCOUNT_ID}}",
  payment_method_types: ["paypal"],

  // or you can take multiple payment methods with
  // payment_method_types: ['card', 'paypal', ...]
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  mode: "subscription",
  success_url: "https://example.com/success",
});
```

#### Customers v1

If you’ve previously created a _`Customer`_ (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) object to represent a customer, use the [customer](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer) argument to pass their `Customer` ID when creating a Checkout Session. This ensures that all objects created during the Session are associated with the correct `Customer` object.

When you pass a `Customer` ID, Stripe also uses the email stored on the `Customer` object to prefill the email field on the Checkout page. If the customer changes their email on the Checkout page, it will be updated on the `Customer` object after a successful payment.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  customer: "{{CUSTOMER_ID}}",
  payment_method_types: ["paypal"],

  // or you can take multiple payment methods with
  // payment_method_types: ['card', 'paypal', ...]
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  mode: "subscription",
  success_url: "https://example.com/success",
});
```

## Optional: Prefill customer data [Server-side]

If you’ve already collected your customer’s email and want to prefill it in the Checkout Session for them, pass [customer_email](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer_email) when creating a Checkout Session.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  customer_email: "customer@example.com",
  payment_method_types: ["paypal"],

  // or you can take multiple payment methods with
  // payment_method_types: ['card', 'paypal', ...]
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  mode: "subscription",
  success_url: "https://example.com/success",
});
```

## Optional: Handling trials [Server-side]

You can use [trial_end](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-subscription_data-trial_end) or [trial_period_days](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-subscription_data-trial_period_days) on the Checkout session to specify the duration of the trial period. In this example we use `trial_period_days` to create a Checkout session for a subscription with a 30 days trial.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  payment_method_types: ["paypal"],

  // or you can take multiple payment methods with
  // payment_method_types: ['card', 'paypal', ...]
  subscription_data: { trial_period_days: 30 },
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  mode: "subscription",
  success_url: "https://example.com/success?session_id={CHECKOUT_SESSION_ID}",
});
```

Checkout displays the following information automatically for subscriptions with trials:

- Trial period
- Frequency and amount of charges after trial expiration

For more information on compliance requirements, see the [Manage compliance requirements](https://docs.stripe.com/billing/subscriptions/trials/manage-trial-compliance.md) or [support](https://support.stripe.com/questions/2020-visa-trial-subscription-requirement-changes-guide) guides.

## Optional: Tax rates [Server-side]

You can specify [tax rates](https://docs.stripe.com/tax/tax-rates.md) (Sales, VAT, GST, and others) in Checkout Sessions to apply taxes to _subscriptions_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis).

- Use fixed tax rates when you know the exact tax rate to charge your customers before they start the checkout process (for example, you only sell to customers in the UK and always charge 20% VAT).
- With the _Prices_ (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) API, you can use dynamic tax rates when you require more information from your customer (for example, their billing or shipping address) before determining the tax rate to charge. With dynamic tax rates, you create tax rates for different regions (for example, a 20% VAT tax rate for customers in the UK and a 7.25% sales tax rate for customers in California, US) and Stripe attempts to match your customer’s location to one of those tax rates.

#### Fixed tax rates

Set [subscription_data.default_tax_rates](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-subscription_data-default_tax_rates) to apply a default tax rate to a subscription started with Checkout.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  payment_method_types: ["paypal"],

  // or you can take multiple payment methods with
  // payment_method_types: ['card', 'paypal', ...]
  subscription_data: { default_tax_rates: ["{{TAX_RATE_ID}}"] },
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  mode: "subscription",
  success_url: "https://example.com/success",
});
```

You can also specify [line_items.tax_rates](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items-tax_rates) or [subscription_data.items.tax_rates](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-subscription_data-items-tax_rates) to apply tax rates to specific plans or invoice line items.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  payment_method_types: ["paypal"],

  // or you can take multiple payment methods with
  // payment_method_types: ['card', 'paypal', ...]
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
      tax_rates: ["{{TAX_RATE_ID}}"],
    },
  ],
  mode: "subscription",
  success_url: "https://example.com/success",
});
```

#### Dynamic tax rates

Pass an array of [tax rates](https://docs.stripe.com/api/tax_rates/object.md) to [line_items.dynamic_tax_rates](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items-dynamic_tax_rates). Each tax rate must have a [supported](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items-dynamic_tax_rates) `country`, and for the US, a `state`.

This list matches tax rates to your customer’s [shipping address](https://docs.stripe.com/payments/collect-addresses.md), billing address, or country. The shipping address takes precedence over the billing address for determining the tax rate to charge.

If you’re not collecting shipping or billing addresses, your customer’s country (and postal code where applicable) is used to determine the tax rate. If you haven’t passed a tax rate that matches your customer’s shipping address, billing address, or country, no tax rate is applied.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  payment_method_types: ["paypal"],
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
      dynamic_tax_rates: [
        "{{FIRST_TAX_RATE_ID}}",
        "{{SECOND_TAX_RATE_ID}}",
        // additional tax rates
      ],
    },
  ],
  mode: "subscription",
  success_url: "https://example.com/success",
});
```

> [subscription_data.default_tax_rates](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-subscription_data-default_tax_rates) and [line_items.tax_rates](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items-tax_rates) can’t be used in combination with [line_items.dynamic_tax_rates](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items-dynamic_tax_rates).

You can use Stripe’s data exports to populate the periodic reports required for remittance. Visit [Tax reporting and remittance](https://docs.stripe.com/tax/tax-rates.md#remittance) for more information.

## Optional: Adding coupons [Server-side]

You can apply [coupons](https://docs.stripe.com/billing/subscriptions/coupons.md) to subscriptions in a Checkout Session by setting [discounts](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-discounts). This coupon overrides any coupon on the customer. If you’re creating a subscription with an [existing customer](https://docs.stripe.com/billing/subscriptions/paypal.md#handling-existing-customers), any coupon associated with the customer is applied to the subscription’s _invoices_ (Invoices are statements of amounts owed by a customer. They track the status of payments from draft through paid or otherwise finalized. Subscriptions automatically generate invoices, or you can manually create a one-off invoice).

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  payment_method_types: ["paypal"],

  // or you can take multiple payment methods with
  // payment_method_types: ['card', 'paypal', ...]
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  discounts: [{ coupon: "{{COUPON_ID}}" }],
  mode: "subscription",
  success_url: "https://example.com/success",
});
```

### Adding customer-facing promotion codes

You can also enable user-redeemable [Promotion Codes](https://docs.stripe.com/billing/subscriptions/coupons.md#promotion-codes) using the [allow_promotion_codes](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-allow_promotion_codes) parameter in Checkout Sessions. When `allow_promotion_codes` is enabled on a Checkout Session, Checkout includes a promotion code redemption box for your customers to use. Create your [coupons](https://docs.stripe.com/billing/subscriptions/coupons.md) and promotion codes through the Dashboard or API in order for your customers to redeem them in Checkout.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  payment_method_types: ["paypal"],

  // or you can take multiple payment methods with
  // payment_method_types: ['card', 'paypal', ...]
  line_items: [
    {
      price_data: {
        currency: "eur",
        unit_amount: 2000,
        product: "{{PRODUCT_ID}}",
        recurring: {
          interval: "month",
        },
      },
      quantity: 1,
    },
  ],
  allow_promotion_codes: true,
  mode: "subscription",
  success_url: "https://example.com/success",
});
```

## See also

- [Customize your integration](https://docs.stripe.com/payments/checkout/customization.md)
- [Manage subscriptions with the customer portal](https://docs.stripe.com/billing/subscriptions/build-subscriptions.md?payment-ui=checkout&ui=stripe-hosted)

# Direct API

> This is a Direct API for when payments-ui-type is direct-api. View the full page at https://docs.stripe.com/billing/subscriptions/paypal?payments-ui-type=direct-api.

Use this guide to set up a _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) using [PayPal](https://docs.stripe.com/payments/paypal.md) as a payment method.

## Before you begin

- To accept PayPal subscriptions on Stripe, you must [enable PayPal recurring payments in the Dashboard](https://docs.stripe.com/payments/paypal/set-up-future-payments.md?platform=web#enable-recurring-payments).
- This feature is only available to specific business locations. [Review the business locations to confirm eligibility](https://docs.stripe.com/payments/paypal.md).

## Create a product and price [Dashboard]

[Products](https://docs.stripe.com/api/products.md) represent the item or service you’re selling. [Prices](https://docs.stripe.com/api/prices.md) define how much and how frequently you charge for a product. This includes how much the product costs, what currency you accept, and whether it’s a one-time or recurring charge. If you only have a few products and prices, create and manage them in the Dashboard.

This guide uses a stock photo service as an example and charges customers a 15 EUR monthly subscription. To model this:

1. Go to the [Products](https://dashboard.stripe.com/products?active=true) page and click **Create product**.
1. Enter a **Name** for the product. You can optionally add a **Description** and upload an image of the product.
1. Select a **Product tax code**. Learn more about [product tax codes](https://docs.stripe.com/tax/tax-codes.md).
1. Select **Recurring**. Then enter **15** for the price and select **EUR** as the currency.
1. Choose whether to **Include tax in price**. You can either use the default value from your [tax settings](https://dashboard.stripe.com/test/settings/tax) or set the value manually. In this example, select **Auto**.
1. Select **Monthly** for the **Billing period**.
1. Click **More pricing options**. Then select **Flat rate** as the pricing model for this example. Learn more about [flat rate](https://docs.stripe.com/products-prices/pricing-models.md#flat-rate) and other [pricing models](https://docs.stripe.com/products-prices/pricing-models.md).
1. Add an internal **Price description** and [Lookup key](https://docs.stripe.com/products-prices/manage-prices.md#lookup-keys) to organize, query, and update specific prices in the future.
1. Click **Next**. Then click **Add product**.

After you create the product and the price, record the price ID so you can use it in subsequent steps. The pricing page displays the ID and it looks similar to this: `price_G0FvDp6vZvdwRZ`.

## Create or retrieve a customer before setup [Server-side]

To reuse a PayPal payment method for future payments, attach it to an object that represents your customer.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

Create a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/create.md#v2_create_accounts-configuration-customer) or [Customer](https://docs.stripe.com/api/customers/create.md) when your customer creates an account with your business, or when saving a payment method. Associate the object’s ID with your own internal representation of a customer.

Create a new customer or retrieve an existing one to associate with this payment.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const account = await stripe.v2.core.accounts.create({
  contact_email: "jenny.rosen@example.com",
  display_name: "Jenny Rosen",
  configuration: {
    customer: {},
  },
  include: ["configuration.customer"],
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create({
  name: "Jenny Rosen",
  email: "jenny.rosen@example.com",
});
```

## Create a SetupIntent [Server-side]

A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) is an object that represents your intent and tracks the steps to set up your customer’s payment method for future payments.

Create a [SetupIntent](https://docs.stripe.com/api/setup_intents.md) on your server with [payment_method_types](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-payment_method_types) set to `paypal` and specify the ID of the customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-id) or [Customer](https://docs.stripe.com/api/customers/object.md#customer_object-id).

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  payment_method_types: ["paypal"],
  payment_method_data: {
    type: "paypal",
  },
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  customer: "{{CUSTOMER_ID}}",
  payment_method_types: ["paypal"],
  payment_method_data: {
    type: "paypal",
  },
});
```

The SetupIntent object contains a [client_secret](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-client_secret), a unique key that you need to pass to Stripe on the client side to redirect your buyer to PayPal and authorize the mandate.

## Redirect your customer [Client-side]

When a customer attempts to set up their PayPal account for future payments, we recommend you use [Stripe.js](https://docs.stripe.com/js.md) to confirm the SetupIntent. Stripe.js is our foundational JavaScript library for building payment flows. It will automatically handle complexities like the redirect described below, and enables you to easily extend your integration to other payment methods in the future.

Include the Stripe.js script on your checkout page by adding it to the head of your HTML file.

```html
<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/dahlia/stripe.js"></script>
</head>
```

Create an instance of Stripe.js with the following JavaScript on your checkout page.

```javascript
// Set your publishable key. Remember to change this to your live publishable key in production!
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>", {});
```

To confirm the setup on the client side, pass the client secret of the SetupIntent object that you created in Step 3.

The client secret is different from your API keys that authenticate Stripe API requests. It should still be handled carefully because it can complete the charge. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

### Confirm PayPal Setup

To authorize you to use their PayPal account for future payments, your customer will be redirected to a PayPal billing agreement page, which they will need to approve before being redirected back to your website. Use [stripe.confirmPayPalSetup](https://docs.stripe.com/js/setup_intents/confirm_paypal_setup) to handle the redirect away from your page and to complete the setup. Add a `return_url` to this function to indicate where Stripe should redirect the user to after they approve the billing agreement on PayPal’s website.

```javascript
// Redirects away from the client
const { error } = await stripe.confirmPayPalSetup(
  "{{SETUP_INTENT_CLIENT_SECRET}}",
  {
    return_url: "https://example.com/setup/complete",
    mandate_data: {
      customer_acceptance: {
        type: "online",
        online: {
          infer_from_client: true,
        },
      },
    },
  },
);

if (error) {
  // Inform the customer that there was an error.
}
```

You can find the Payment Method payer ID and Billing Agreement ID on the resulting [Mandate](https://docs.stripe.com/api/mandates/.md) under the [payment_method_details](https://docs.stripe.com/api/mandates/object.md#mandate_object-payment_method_details-paypal) property. You can also find the buyer’s email and payer ID in the [paypal](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-paypal) property on the [PaymentMethod](https://docs.stripe.com/api/payment_methods.md).

| Field                  | Value                                                                                                                                         |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `payer_email`          | The email address of the payer on their PayPal account.                                                                                       |
| `payer_id`             | A unique ID of the payer’s PayPal account.                                                                                                    |
| `billing_agreement_id` | The PayPal Billing Agreement ID (BAID). This is an ID generated by PayPal which represents the mandate between the business and the customer. |

## Monitor webhooks [Server-side]

Use a method such as [webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks) to confirm the billing agreement was authorized successfully by your customer, instead of relying on your customer to return to the payment status page. When a customer successfully authorizes the billing agreement, the SetupIntent emits the [setup_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.succeeded) _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event. If a customer doesn’t successfully authorize the billing agreement, the SetupIntent will emit the [setup_intent.setup_failed](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.setup_failed) webhook event and returns to a status of `requires_payment_method`. When a customer revokes the billing agreement from their PayPal account, the [mandate.updated](https://docs.stripe.com/api/events/types.md#event_types-mandate.updated) is emitted.

## Create the subscription [Server-side]

Create a [subscription](https://docs.stripe.com/api/subscriptions.md) with the price and customer:

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  default_payment_method: "pm_1F0c9v2eZvKYlo2CJDeTrB4n",
  items: [
    {
      price: "price_F52b2UdntfQsfR",
    },
  ],
  expand: ["latest_invoice.confirmation_secret"],
  off_session: true,
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer: "{{CUSTOMER_ID}}",
  default_payment_method: "pm_1F0c9v2eZvKYlo2CJDeTrB4n",
  items: [
    {
      price: "price_F52b2UdntfQsfR",
    },
  ],
  expand: ["latest_invoice.confirmation_secret"],
  off_session: true,
});
```

Creating subscriptions automatically charges customers because the [default payment method](https://docs.stripe.com/api/customers/create.md#create_customer-invoice_settings-default_payment_method) is set. After a successful payment, the status in the [Stripe Dashboard](https://dashboard.stripe.com/test/subscriptions) changes to **Active**. The price you created earlier determines subsequent billings.

## Manage subscription status [Client-side]

When the initial payment succeeds, the status of the subscription is `active` and no further action is needed. When payments fail, the status is changed to the **Subscription status** configured in your [automatic collection settings](https://docs.stripe.com/invoicing/automatic-collection.md). Notify the customer after a failure and [charge them with a different payment method](https://docs.stripe.com/billing/subscriptions/overview.md#requires-payment-method).

## Update a subscription [Server-side]

When you update a subscription, you need to specify `off_session=true`. Otherwise, any new payment requires a user redirection to PayPal for confirmation. For example, if you want to change the quantity of an item included in the subscription you can use:

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  default_payment_method: "pm_1F0c9v2eZvKYlo2CJDeTrB4n",
  items: [
    {
      price: "price_F52b2UdntfQsfR",
      quantity: 2,
    },
  ],
  off_session: true,
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer: "{{CUSTOMER_ID}}",
  default_payment_method: "pm_1F0c9v2eZvKYlo2CJDeTrB4n",
  items: [
    {
      price: "price_F52b2UdntfQsfR",
      quantity: 2,
    },
  ],
  off_session: true,
});
```

## Test the integration

Test your PayPal integration with your [test API keys](https://docs.stripe.com/keys.md#test-live-modes) by viewing the redirect page. You can test the successful payment case by authenticating the payment on the redirect page. The PaymentIntent will transition from `requires_action` to `succeeded`.

To test the case where the user fails to authenticate, use your test API keys and view the redirect page. On the redirect page, click **Fail test payment**. The PaymentIntent will transition from `requires_action` to `requires_payment_method`.

## Optional: Set the billing period

When you create a subscription, it automatically sets the billing cycle by default. For example, if a customer subscribes to a monthly plan on September 7, they’re billed on the 7th of every month after that. Some businesses prefer to set the billing cycle manually so that they can charge their customers at the same time each cycle. The [billing cycle anchor](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-billing_cycle_anchor) argument allows you to do this.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  items: [
    {
      price: "{{PRICE_ID}}",
    },
  ],
  billing_cycle_anchor: 1611008505,
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer: "{{CUSTOMER_ID}}",
  items: [
    {
      price: "{{PRICE_ID}}",
    },
  ],
  billing_cycle_anchor: 1611008505,
});
```

Setting the billing cycle manually automatically charges the customer a prorated amount for the time between the subscription being created and the billing cycle anchor. If you don’t want to charge customers for this time, you can set the [proration_behavior](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-proration_behavior) argument to `none`. You can also combine the billing cycle anchor with [trial periods](https://docs.stripe.com/billing/subscriptions/paypal.md#trial-periods) to give users free access to your product and then charge them a prorated amount.

## Optional: Subscription trials

Free trials allow customers access to your product for a period of time for free. Using free trials is different from setting [proration_behavior](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-proration_behavior) to `none` because you can customize how long the free period lasts. Pass a timestamp in [trial end](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-trial_end) to set the trial period.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  items: [
    {
      price: "{{PRICE_ID}}",
    },
  ],
  trial_end: 1610403705,
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer: "{{CUSTOMER_ID}}",
  items: [
    {
      price: "{{PRICE_ID}}",
    },
  ],
  trial_end: 1610403705,
});
```

You can also combine a [billing cycle anchor](https://docs.stripe.com/billing/subscriptions/paypal.md#billing-cycle) with a free trial. For example, say it’s September 15 and you want to give your customer a free trial for seven days and then start the normal billing cycle on October 1. You can set the free trial to end on September 22 and the billing cycle anchor to October 1. This gives the customer a free trial for seven days and then charges a prorated amount for the time between the trial ending and October 1. On October 1, you charge them the normal subscription amount for their first full billing cycle.

## Optional: Remove a saved PayPal account

You can use the [detach](https://docs.stripe.com/api/payment_methods/detach.md) API to remove a customer’s saved PayPal account as a payment method. When you detach a PayPal payment method, it revokes the [mandate](https://docs.stripe.com/api/mandates.md) and also calls the PayPal API to cancel the associated PayPal billing agreement.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethod = await stripe.paymentMethods.detach(
  "{{PAYMENT_METHOD_ID}}",
);
```
