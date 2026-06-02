<!-- Source URL: https://docs.stripe.com/payments/ng-card/set-up-future-payments -->
<!-- Fetched: 2026-05-08 -->

# Set up future payments with Naira card

Learn how to save Naira card to charge customers later.

# Checkout

> This is a Checkout for when payment-ui is checkout. View the full page at https://docs.stripe.com/payments/ng-card/set-up-future-payments?payment-ui=checkout.

Save Naira card payment details using [Checkout](https://docs.stripe.com/payments/checkout.md), our fully hosted checkout page.

Learn how to [set up a subscription with Naira card](https://docs.stripe.com/billing/subscriptions/ng-card.md) to create recurring payments after saving a payment method in Checkout.

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Access the Stripe API from your application using our official libraries:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Getting permission to save a payment method [Server-side]

You need the customer’s permission to save their payment method for future use. Creating an agreement (sometimes called a mandate) up front allows you to save the customer’s payment details and charge them when they’re not actively using your website or app.

Add terms to your website or app that state how you plan to save the customer’s payment method details, and let them opt in. If you plan to charge the customer when they’re offline, make sure that your terms also include the following:

- The customer’s permission for you to initiate a payment or a series of payments on their behalf for specified transactions
- The anticipated frequency (one-time or recurring) and timing of payments
- How you determine the payment amount
- Your cancellation policy, if you’re setting up the payment method for a subscription service

Make sure that you keep a record of the customer’s written agreement to these terms.

## Create or retrieve a Customer [Server-side]

To save a Naira card payment method for future payments, attach it to a _Customer_ (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments).

Create a [Customer object](https://docs.stripe.com/api/customers.md) when the customer creates an account with your business, and associate the ID of the Customer object with your own internal representation of that customer. Alternatively, you can create a new Customer before saving a payment method for future payments.

Create a new Customer or retrieve an existing Customer to associate with this payment. Include the following code on your server to create a new Customer:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create({
  description: "My First Test Customer (created for API docs)",
});
```

## Create a Checkout Session [Server-side]

The customer must authorize the use of the local merchant of record service provider for future payments.

Add a checkout button to your website that calls a server-side endpoint to create a [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md).

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

Create a Checkout Session in `setup` mode to collect the required information. After creating the Checkout Session, redirect the customer to the [Checkout session URL](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-url) that the response returns.

#### Node.js

```javascript
const session = await stripe.checkout.sessions.create({
  payment_method_types: ["card", "ng_card"],
  mode: "setup",
  customer: customer.id,
  success_url: "https://example.com/success",
});
```

## Test your integration

Select Naira card as the payment method, then click **Continue to Naira card**. Test the setup by authenticating the SetupIntent on the redirect page. If the SetupIntent transitions from `requires_action` to `succeeded`, the setup is correct.

# Direct API

> This is a Direct API for when payment-ui is direct-api. View the full page at https://docs.stripe.com/payments/ng-card/set-up-future-payments?payment-ui=direct-api.

You can use the [Setup Intents API](https://docs.stripe.com/payments/setup-intents.md) to collect payment method details in advance, with the final amount or payment date determined later. Use this to:

- Save payment methods to a wallet to streamline future purchases
- Collect surcharges after fulfilling a service
- [Start a free trial for a subscription](https://docs.stripe.com/billing/subscriptions/trials.md)

To collect payment method details and charge the saved payment method immediately, use the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md).

Learn how to [set up a subscription with Naira card](https://docs.stripe.com/billing/subscriptions/ng-card.md) to create recurring payments after saving a payment method in Checkout.

## Create or retrieve a Customer [Server-side]

To save a Naira card payment method for future payments, you must attach it to a _Customer_ (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments).

Create a Customer object after the customer creates an account on your business. Associating the ID of the Customer object with your own internal representation of a customer enables you to retrieve and use the payment method details that you store later. If the customer hasn’t created an account, you can still create a Customer object and associate it with your internal representation of the customer’s account at a later point.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create({
  description: "My First Test Customer (created for API docs)",
});
```

#### Save a payment method with the Setup Intents API

Use the [Setup Intents API](https://docs.stripe.com/payments/setup-intents.md) to collect payment method details in advance, and determine the final amount later. Use it to:

- Save payment methods for customers so their later purchases don’t require authentications
- Start a free trial for a _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis)

## Create a SetupIntent and save a payment method [Server-side]

A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) is an object that represents your intent to set up a customer’s payment method for future payments. The SetupIntent tracks the steps of this set-up process. Create a SetupIntent on your server with [payment_method_types](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-payment_method_types) set to `ng_card` and specify the Customer’s ID and [usage=off_session](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-usage) or `usage=on_session`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ["ng_card"],
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

Next, confirm the Naira card setup on the client with [Stripe.js](https://docs.stripe.com/payments/elements.md).

Include the Stripe.js script on your checkout page by adding it to the `head` of your HTML file.

```html
<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/dahlia/stripe.js"></script>
</head>
```

When a customer clicks to pay with Naira card, use Stripe.js to submit the payment to Stripe. [Stripe.js](https://docs.stripe.com/payments/elements.md) is the foundational JavaScript library for building payment flows. It automatically handles complexities like the redirect described below, and enables you to extend your integration to other payment methods. Include the Stripe.js script on your checkout page by adding it to the `head` of your HTML file.

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

Use `stripe.confirmNgCardSetup` to confirm the SetupIntent on the client-side, with a [return_url](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-return_url) and [mandate_data](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-mandate_data). Use the [return_url](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-return_url) to redirect customers to a specific page after the SetupIntent succeeds.

```javascript
// Redirects away from the client
const { error } = await stripe.confirmNgCardSetup(
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

## Optional: Handle the Naira card redirect manually

Stripe.js helps you extend your integration to other payment methods. However, you can manually redirect customers on your server.

1. Create and _confirm_ (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) a PaymentIntent of type `ng_card`. By specifying `payment_method_data`, a PaymentMethod is created and immediately used with the PaymentIntent.

You must also provide the URL where the customer is redirected to after they complete their payment in the `return_url` field. You can provide your own query parameters in this URL. These parameters are included in the final URL upon completing the redirect flow.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: "ngn",
  payment_method_types: ["ng_card"],
  payment_method_data: {
    type: "ng_card",
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

Use the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md) to collect payment method details at checkout and save a payment method to a customer. Use this to:

- Save payment methods for customers so their later purchases don’t require authentications
- Start a free trial for a _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis)

## Create a PaymentIntent and save a payment method [Server-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) is an object that represents your intent to charge a customer. If you don’t provide a saved payment method with the PaymentIntent request, we create a new payment method and attach it to a customer before confirming the PaymentIntent. Create a PaymentIntent on your server with [payment_method_types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) set to `ng_card` and specify the Customer’s ID, `confirm=true`, [setup_future_usage=off_session](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) with a [return_url](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-return_url), and an optional [mandate_data](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-mandate_data). Use the [return_url](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-return_url) to redirect customers to a specific page after the PaymentIntent succeeds.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["ng_card"],
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

The PaymentIntent that returns includes a _client secret_ (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)), that the client-side uses to securely complete the payment instead of passing the entire PaymentIntent object. Pass the client secret to the client-side application to continue with the payment process.

## Create a PaymentIntent using a saved payment method [Server-side]

After you create a [PaymentMethod](https://docs.stripe.com/api/payment_methods.md), you can accept future Naira card payments by creating and confirming [PaymentIntents](https://docs.stripe.com/api/payment_intents.md). When confirming a PaymentIntent, use the payment method ID from the previous SetupIntent or PaymentIntent. If the customer isn’t in a checkout flow for the current PaymentIntent, you must also set the `off_session` value to true.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["ng_card"],
  payment_method: "{{PAYMENT_METHOD_ID}}",
  amount: 1000,
  currency: "ngn",
  customer: "{{CUSTOMER_ID}}",
  statement_descriptor: "test_statement",
  capture_method: "automatic",
  confirm: true,
  off_session: true,
});
```

## Detach a reusable payment method

To deactivate a reusable payment method, call [detach PaymentMethod](https://docs.stripe.com/api/payment_methods/detach.md) from your server. Stripe sends both a [mandate.updated](https://docs.stripe.com/api/events/types.md#event_types-mandate.updated) event and a [payment_method.detached](https://docs.stripe.com/api/events/types.md#event_types-payment_method.detached) event. You can subscribe to [webhook](https://docs.stripe.com/webhooks.md) events to get notifications.
