<!-- Source URL: https://docs.stripe.com/payments/naver-pay/set-up-future-payments -->
<!-- Fetched: 2026-05-08 -->

# Set up future payments with Naver Pay

Learn how to save Naver Pay to charge your customers later.

# Checkout

> This is a Checkout for when payment-ui is checkout. View the full page at https://docs.stripe.com/payments/naver-pay/set-up-future-payments?payment-ui=checkout.

Save Naver Pay payment details using [Checkout](https://docs.stripe.com/payments/checkout.md), our fully hosted checkout page.

Learn how to [set up a subscription with Naver Pay](https://docs.stripe.com/billing/subscriptions/naver-pay.md) to create recurring payments after saving a payment method in Checkout.

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Get permission to save Naver Pay as a payment method [Server-side]

You need permission to save your customer’s payment method for future use. Creating an agreement (sometimes called a mandate) up front allows you to save your customer’s payment details and charge them when they’re not actively using your website or app.

Add terms to your website or app that state how you plan to save your customer’s payment method details, and let them opt in. If you plan to charge your customer when they’re offline, make sure that your terms also include the following:

- The customer’s permission for you to initiate a payment or a series of payments on their behalf for specified transactions
- The anticipated frequency (one-time or recurring) and timing of payments
- How you determine the payment amount
- Your cancellation policy (if you’re setting up the payment method for a subscription service)

Make sure that you keep a record of your customer’s written agreement to these terms, and only submit charges in accordance with the agreed terms.

## Create or retrieve a customer [Server-side]

To reuse a Naver Pay payment method for future payments, attach it to an object that represents your customer.

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

## Create a Checkout Session [Server-side]

Your customer must authorize you to use their NICEPAY account for future payments through Stripe Checkout. This allows you to accept future Naver Pay payments. Add a checkout button to your website that calls a server-side endpoint to create a [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md).

```html
<html>
  <head>
    <title>Set up payment</title>
  </head>
  <body>
    <form action="/create-checkout-session" method="POST">
      <button type="submit">Set up payment</button>
    </form>
  </body>
</html>
```

Create a Checkout Session in `setup` mode to collect the required information. After creating the Checkout Session, redirect your customer to the [URL](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-url) in the response.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  mode: "setup",
  payment_method_types: ["card", "naver_pay"],
  success_url: "https://example.com/success",
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  customer: "{{CUSTOMER_ID}}",
  mode: "setup",
  payment_method_types: ["card", "naver_pay"],
  success_url: "https://example.com/success",
});
```

## Test your integration

While testing your Checkout integration, select **Naver Pay** and click **Continue to Naver Pay**. You’ll be redirected to a Stripe-hosted page where you can choose to authorize or fail the payment setup. Learn more about [testing redirect-based payment methods](https://docs.stripe.com/testing.md#redirects).

# Direct API

> This is a Direct API for when payment-ui is direct-api. View the full page at https://docs.stripe.com/payments/naver-pay/set-up-future-payments?payment-ui=direct-api.

You can use the [Setup Intents API](https://docs.stripe.com/payments/setup-intents.md) to collect payment method details in advance, with the final amount or payment date determined later. Use this for:

- Saving payment methods to a wallet to streamline future purchases
- Collecting surcharges after fulfilling a service
- [Starting a free trial for a subscription](https://docs.stripe.com/billing/subscriptions/trials.md)

To collect payment method details and charge the saved payment method immediately, use the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md).

Learn how to [set up a subscription with Naver Pay](https://docs.stripe.com/billing/subscriptions/naver-pay.md) to create recurring payments after saving a payment method in Checkout.

## Create or retrieve a customer [Server-side]

To save a Naver Pay payment method for future payments, attach it to an object that represents your customer.

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

#### Save a payment method with the Setup Intents API

Use the [Setup Intents API](https://docs.stripe.com/payments/setup-intents.md) to collect payment method details in advance and determine the final amount or payment date at a later point. This is useful for:

- Saving payment methods for customers so their later purchases don’t require authentications
- Starting a free trial for a _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis)

## Get permission to save Naver Pay as a payment method [Server-side]

You need permission to save your customer’s payment method for future use. Creating an agreement (sometimes called a mandate) up front allows you to save your customer’s payment details and charge them when they’re not actively using your website or app.

Add terms to your website or app that state how you plan to save your customer’s payment method details, and let them opt in. If you plan to charge your customer when they’re offline, make sure that your terms also include the following:

- The customer’s permission for you to initiate a payment or a series of payments on their behalf for specified transactions
- The anticipated frequency (one-time or recurring) and timing of payments
- How you determine the payment amount
- Your cancellation policy (if you’re setting up the payment method for a subscription service)

Make sure that you keep a record of your customer’s written agreement to these terms, and only submit charges in accordance with the agreed terms.

## Create a SetupIntent and save Naver Pay as a payment method [Server-side]

A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) is an object that represents your intent to set up a customer’s payment method for future payments. The `SetupIntent` tracks the steps of this setup process. Create a `SetupIntent` on your server and set [usage](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-usage) to `off_session` or `on_session`. Add `naver_pay` to the [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) array, and specify the ID of the customer-configured `Account` or `Customer`.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ["naver_pay"],
  payment_method_data: {
    type: "naver_pay",
  },
  usage: "off_session",
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ["naver_pay"],
  payment_method_data: {
    type: "naver_pay",
  },
  usage: "off_session",
  customer: "{{CUSTOMER_ID}}",
});
```

### Retrieve the client secret

The SetupIntent includes a _client secret_ (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)) that the client side uses to securely complete the payment process. You can use different approaches to pass the client secret to the client side.

#### Single-page application

Retrieve the client secret from an endpoint on your server, using the browser’s `fetch` function. This approach is best if your client side is a single-page application, particularly one built with a modern frontend framework like React. Create the server endpoint that serves the client secret:

#### Node.js

```javascript
const express = require("express");
const app = express();

app.get("/secret", async (req, res) => {
  const intent = // ... Fetch or create the SetupIntent
    res.json({ client_secret: intent.client_secret });
});

app.listen(3000, () => {
  console.log("Running on port 3000");
});
```

And then fetch the client secret with JavaScript on the client side:

```javascript
(async () => {
  const response = await fetch("/secret");
  const { client_secret: clientSecret } = await response.json();
  // Render the form using the clientSecret
})();
```

#### Server-side rendering

Pass the client secret to the client from your server. This approach works best if your application generates static content on the server before sending it to the browser.

Add the [client_secret](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-client_secret) in your checkout form. In your server-side code, retrieve the client secret from the SetupIntent:

#### Node.js

```html
<form id="payment-form" data-secret="{{ client_secret }}">
  <div id="payment-element">
    <!-- Elements will create form elements here -->
  </div>

  <button id="submit">Submit</button>
</form>
```

```javascript
const express = require("express");
const expressHandlebars = require("express-handlebars");
const app = express();

app.engine(".hbs", expressHandlebars({ extname: ".hbs" }));
app.set("view engine", ".hbs");
app.set("views", "./views");

app.get("/checkout", async (req, res) => {
  const intent = // ... Fetch or create the SetupIntent
    res.render("checkout", { client_secret: intent.client_secret });
});

app.listen(3000, () => {
  console.log("Running on port 3000");
});
```

Next, save Naver Pay on the client with [Stripe.js](https://docs.stripe.com/payments/elements.md).

Include the Stripe.js script on your checkout page by adding it to the `head` of your HTML file.

```html
<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/dahlia/stripe.js"></script>
</head>
```

When a customer clicks to pay with Naver Pay, use Stripe.js to submit the payment to Stripe. [Stripe.js](https://docs.stripe.com/payments/elements.md) is the foundational JavaScript library for building payment flows. It automatically handles complexities like the redirect described below, and enables you to extend your integration to other payment methods. Include the Stripe.js script on your checkout page by adding it to the `head` of your HTML file.

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
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");
```

Use `stripe.confirmNaverPaySetup` to confirm the SetupIntent on the client-side, with a [return_url](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-return_url) and [mandate_data](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-mandate_data). Use the [return_url](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-return_url) to redirect customers to a specific page after the SetupIntent succeeds.

```javascript
// Redirects away from the client
const { error } = await stripe.confirmNaverPaySetup(
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

## Optional: Handle redirects manually

Stripe.js helps you extend your integration to other payment methods. However, you can manually redirect your customers on your server.

1. Create and _confirm_ (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) a PaymentIntent of type `naver_pay`. By specifying `payment_method_data`, a PaymentMethod is created and immediately used with the PaymentIntent.

You must also provide the URL where your customer is redirected to after they complete their payment in the `return_url` field. You can provide your own query parameters in this URL. These parameters are included in the final URL upon completing the redirect flow.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: "krw",
  payment_method_types: ["naver_pay"],
  payment_method_data: {
    type: "naver_pay",
  },
  return_url: "https://example.com/checkout/complete",
  confirm: true,
});
```

1. Check that the `PaymentIntent` has a status of `requires_action` and the type for `next_action` is `redirect_to_url`.

#### Json

```json
{"status": "requires_action",
  "next_action": {
    "type": "redirect_to_url",
    "redirect_to_url": {
      "url": "https://hooks.stripe.com/...",
      "return_url": "https://example.com/checkout/complete"
    }
  },
  "id": "pi_1G1sgdKi6xqXeNtkldRRE6HT",
  "object": "payment_intent",
  ...
}
```

1. Redirect the customer to the URL provided in the `next_action.redirect_to_url.url` property. This code example is approximate—the redirect method might be different in your web framework.

#### Node.js

```javascript
if (
  paymentIntent.status === "requires_action" &&
  paymentIntent.next_action.type === "redirect_to_url"
) {
  const url = paymentIntent.next_action.redirect_to_url.url;
  res.redirect(url);
}
```

Your customer is redirected to the `return_url` when they complete the payment process. The `payment_intent` and `payment_intent_client_secret` URL query parameters are included along with any of your own query parameters. Stripe recommends setting up a [webhook endpoint](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks) to programmatically confirm the status of a payment.

#### Save a payment method with the Payment Intents API

Use the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md) to collect payment method details at checkout and save a payment method to a customer. This is useful for:

- Saving payment methods for customers so their later purchases don’t require authentications
- Starting a free trial for a _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis)

## Create a PaymentIntent and save a payment method [Server-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) is an object that represents your intent to charge a customer. If you don’t provide a saved payment method with the PaymentIntent request, we create a new payment method and attach it to a customer before confirming the PaymentIntent. Create a `PaymentIntent` on your server as follows:

- Add `naver_pay` to the [payment_method_types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) array.
- Specify the ID of the `Customer` or customer-configured `Account`.
- Set `confirm` to true.
- Set [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) to `off_session`.
- Set the [return_url](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-return_url) to the URL of the page you want to return the customer to after the `PaymentIntent` succeeds.
- If you need to create a mandate, set [mandate_data](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-mandate_data).

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["naver_pay"],
  mandate_data: {
    customer_acceptance: {
      type: "online",
      online: {
        ip_address: "127.0.0.0",
        user_agent: "device",
      },
    },
  },
  return_url: "https://www.stripe.com",
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  setup_future_usage: "off_session",
  amount: 1000,
  currency: "ngn",
  statement_descriptor: "test_statement",
  capture_method: "automatic",
  confirm: true,
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["naver_pay"],
  mandate_data: {
    customer_acceptance: {
      type: "online",
      online: {
        ip_address: "127.0.0.0",
        user_agent: "device",
      },
    },
  },
  return_url: "https://www.stripe.com",
  customer: "{{CUSTOMER_ID}}",
  setup_future_usage: "off_session",
  amount: 1000,
  currency: "ngn",
  statement_descriptor: "test_statement",
  capture_method: "automatic",
  confirm: true,
});
```

The PaymentIntent that returns includes a _client secret_ (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)), which the client-side uses to securely complete the payment instead of passing the entire PaymentIntent object. Pass the client secret to the client-side application to continue with the payment process.

## Create a PaymentIntent using a saved payment method [Server-side]

After you create a [PaymentMethod](https://docs.stripe.com/api/payment_methods.md), you can accept future Naver Pay payments by creating and confirming a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md). When confirming a PaymentIntent, use the same payment method ID from the previous SetupIntent or PaymentIntent object. The `off_session` value must also be set to true if the customer isn’t in a checkout flow for this PaymentIntent.

> Recurring payments must be made with `capture_method: "automatic"`. Manual capture isn’t supported.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["naver_pay"],
  payment_method: "{{PAYMENT_METHOD_ID}}",
  amount: 1000,
  currency: "krw",
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  statement_descriptor: "test_statement",
  capture_method: "automatic",
  confirm: true,
  off_session: true,
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["naver_pay"],
  payment_method: "{{PAYMENT_METHOD_ID}}",
  amount: 1000,
  currency: "krw",
  customer: "{{CUSTOMER_ID}}",
  statement_descriptor: "test_statement",
  capture_method: "automatic",
  confirm: true,
  off_session: true,
});
```

## Detach a reusable payment method

To deactivate a reusable payment method, call [detach PaymentMethod](https://docs.stripe.com/api/payment_methods/detach.md) from your server. Stripe sends both a [mandate.updated](https://docs.stripe.com/api/events/types.md#event_types-mandate.updated) event and a [payment_method.detached](https://docs.stripe.com/api/events/types.md#event_types-payment_method.detached) event. You can subscribe to [webhook](https://docs.stripe.com/webhooks.md) events to get notifications.

## Test your integration

While testing your Checkout integration, select **Naver Pay** and click **Pay**. This redirects you to a Stripe-hosted page where you have the choice to authorize or fail the payment. If you authorize the payment, the PaymentIntent switches from `requires_action` to `succeeded`. Failing the test payment makes the PaymentIntent switch from `requires_action` to `requires_payment_method`. Learn more about how to [test](https://docs.stripe.com/testing.md#redirects) redirect-based payment methods.
