<!-- Source URL: https://docs.stripe.com/payments/upi/set-up-future-payments -->
<!-- Fetched: 2026-05-06 -->

# Set up future UPI payments

Learn how to save UPI details and charge your customers later.

# Checkout

> This is a Checkout for when payment-ui is checkout. View the full page at https://docs.stripe.com/payments/upi/set-up-future-payments?payment-ui=checkout.

This guide covers how to save UPI payment details using [Checkout](https://docs.stripe.com/payments/checkout.md), our fully hosted checkout page.

You need permission to save your customer’s payment method for future use. Creating an agreement (sometimes called a mandate) up front allows you to save your customer’s payment details, and potentially charge your customer when they’re not actively using your website or app. Learn more about [how e-mandates work in India](https://docs.stripe.com/payments/upi/upi-autopay.md).

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create or retrieve a customer [Server-side]

To reuse a UPI payment method for future payments, attach it to an object that represents your customer.

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

Your customer must authorize you to use UPI for future payments through Stripe Checkout. This lets you accept UPI payments. Add a checkout button to your website that calls a server-side endpoint to create a [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md).

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

Create a Checkout Session in `setup` mode to collect the required information. After creating the Checkout Session, redirect your customer to the [URL](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-url) that the response returns.

#### Node.js

```javascript
const session = await stripe.checkout.sessions.create({
  payment_method_types: ["card", "upi"],
  mode: "setup",
  customer: customer.id,
  success_url: "https://example.com/success",
});
```

## Test your integration

Select UPI as the payment method, then click **Pay with UPI**. If you’re using a mobile device, you’ll be automatically redirected to a test page where you can approve the purchase. Otherwise, you’ll see a QR code, and when you scan it you’ll be redirected to the same test page.

# Direct API

> This is a Direct API for when payment-ui is direct-api. View the full page at https://docs.stripe.com/payments/upi/set-up-future-payments?payment-ui=direct-api.

You can use the [Setup Intents API](https://docs.stripe.com/payments/setup-intents.md) to collect payment method details in advance, with the final amount or payment date determined later. Use this for:

- Saving payment methods to a wallet to streamline future purchases
- Collecting surcharges after fulfilling a service
- [Starting a free trial for a subscription](https://docs.stripe.com/billing/subscriptions/trials.md)

To collect payment method details and charge the saved payment method immediately, use the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md).

Any on-session UPI payment, where you’re actively in your checkout flow, redirects you to the UPI app for confirmation, even if you’re using a saved payment method.

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create or retrieve a customer [Server-side]

To save a UPI payment method for future payments, you must attach it to an object that represents your customer.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

Create a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/create.md#v2_create_accounts-configuration-customer) or [Customer](https://docs.stripe.com/api/customers/create.md) after your customer creates an account on your business. Associating the object’s ID with your own internal representation of a customer enables you to retrieve and use the payment method details that you store later. If your customer hasn’t created an account, you can still create a customer-configured `Account` or `Customer` and associate it with your internal representation of the customer’s account at a later point.

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

## Present authorization terms on your payment form [Client-side]

If you save your customer’s payment method for future use, you need permission. Creating an agreement (sometimes called a mandate) up front allows you to save your customer’s payment details, and potentially charge your customer when they’re not actively using your website or app. [Read more about how e-mandates work in India here](https://docs.stripe.com/payments/upi/upi-autopay.md)

#### Save a payment method with the Setup Intents API

Use the [Setup Intents API](https://docs.stripe.com/payments/setup-intents.md) to collect payment method details in advance and determine the final amount or payment date at a later point. This is useful for:

- Saving payment methods for customers so their later purchases don’t require authentications
- Starting a free trial for a *subscription* (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis)

## Create a SetupIntent and save a payment method [Server-side]

A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) is an object that represents your intent to set up a customer’s payment method for future payments. The SetupIntent tracks the steps of this set-up process. Create a `SetupIntent` on your server with `upi` in the [payment_method_types](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-payment_method_types) array and specify the customer’s ID and [usage=off_session](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-usage) or `usage=on_session`.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ["upi"],
  payment_method_data: {
    type: "upi",
    billing_details: {
      name: "Example name",
      address: {
        line1: "Main Street 123",
        line2: "Apartment 42",
        city: "Bengaluru",
        state: "KA",
        postal_code: "560103",
        country: "IN",
      },
    },
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
  payment_method_types: ["upi"],
  payment_method_data: {
    type: "upi",
    billing_details: {
      name: "Example name",
      address: {
        line1: "Main Street 123",
        line2: "Apartment 42",
        city: "Bengaluru",
        state: "KA",
        postal_code: "560103",
        country: "IN",
      },
    },
  },
  usage: "off_session",
  customer: "{{CUSTOMER_ID}}",
});
```

### Retrieve the client secret

The SetupIntent includes a *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)) that the client side uses to securely complete the payment process. You can use different approaches to pass the client secret to the client side.

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

Next, you save UPI on the client with [Stripe.js](https://docs.stripe.com/payments/elements.md).

Include the Stripe.js script on your checkout page by adding it to the `head` of your HTML file.

```html
<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/dahlia/stripe.js"></script>
</head>
```

Create an instance of Stripe.js with the following JavaScript on your checkout page:

```javascript
// Set your publishable key. Remember to change this to your live publishable key in production!
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");
```

Use `stripe.confirmUpiSetup` to confirm the setupIntent on the client side, with a [return_url](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-return_url) and [mandate_data](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-mandate_data). Use the [return_url](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-return_url) to redirect customers to a specific page after the SetupIntent succeeds.

```javascript
// Redirects away from the client
const { error } = await stripe.confirmUpiSetup(
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

#### Save a payment method with the Payment Intents API

Use the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md) to collect payment method details at checkout and save a payment method to a customer. This is useful for:

- Saving payment methods for customers so their later purchases don’t require authentication
- Starting a free trial for a *subscription* (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis)

## Create a PaymentIntent and save a payment method [Server-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) is an object that represents your intent to charge a customer. If you don’t provide a saved payment method with the PaymentIntent request, we create a new payment method and attach it to a customer before confirming the PaymentIntent. Create a `PaymentIntent` on your server with `upi` in the [payment_method_types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) array and specify the customer’s ID, `confirm=true`, [setup_future_usage=off_session](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) with a [return_url](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-return_url), and an optional [mandate_data](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-mandate_data). Use the [return_url](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-return_url) to redirect customers to a specific page after the `PaymentIntent` succeeds.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["upi"],
  payment_method_data: {
    type: "upi",
    billing_details: {
      name: "Example name",
      address: {
        line1: "Main Street 123",
        line2: "Apartment 42",
        city: "Bengaluru",
        state: "KA",
        postal_code: "560103",
        country: "IN",
      },
    },
  },
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
  amount: 10000,
  currency: "inr",
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
  payment_method_types: ["upi"],
  payment_method_data: {
    type: "upi",
    billing_details: {
      name: "Example name",
      address: {
        line1: "Main Street 123",
        line2: "Apartment 42",
        city: "Bengaluru",
        state: "KA",
        postal_code: "560103",
        country: "IN",
      },
    },
  },
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
  amount: 10000,
  currency: "inr",
  statement_descriptor: "test_statement",
  capture_method: "automatic",
  confirm: true,
});
```

The PaymentIntent that returns includes a *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)), which the client-side uses to securely complete the payment instead of passing the entire PaymentIntent object. Pass the client secret to the client-side application to continue with the payment process.

## Create a PaymentIntent using a saved payment method [Server-side]

After you create a [PaymentMethod](https://docs.stripe.com/api/payment_methods.md), you can accept future UPI payments by creating and confirming a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md). When confirming a PaymentIntent, use the same payment method ID from the previous SetupIntent or PaymentIntent object. The `off_session` value must also be set to true if the customer isn’t in a checkout flow for this PaymentIntent.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["upi"],
  payment_method: "{{PAYMENT_METHOD_ID}}",
  amount: 10000,
  currency: "inr",
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
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
  payment_method_types: ["upi"],
  payment_method: "{{PAYMENT_METHOD_ID}}",
  amount: 10000,
  currency: "inr",
  customer: "{{CUSTOMER_ID}}",
  capture_method: "automatic",
  confirm: true,
  off_session: true,
});
```

## Optional: Handle the UPI flow manually

Stripe.js helps you extend your integration to other payment methods. However, you can manually handle the next action.

1. Create and *confirm* (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) a PaymentIntent of type `upi`. By specifying `payment_method_data`, a PaymentMethod is created and immediately used with the PaymentIntent.

You must also provide the URL where your customer is redirected to after they complete their payment in the `return_url` field. You can provide your own query parameters in this URL. These parameters are included in the final URL upon completing the redirect flow.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 10000,
  currency: "inr",
  payment_method_types: ["upi"],
  payment_method_data: {
    type: "upi",
    billing_details: {
      name: "Example name",
      address: {
        line1: "Main Street 123",
        line2: "Apartment 42",
        city: "Bengaluru",
        state: "KA",
        postal_code: "560103",
        country: "IN",
      },
    },
  },
  return_url: "https://example.com/checkout/complete",
  confirm: true,
});
```

1. Check that the payment intent has a status of `requires_action` and the type for `next_action` is `upi_handle_redirect_or_display_qr_code`

#### Json

```json
{"status": "requires_action",
  "next_action": {
    "type": "upi_handle_redirect_or_display_qr_code",
    "upi_handle_redirect_or_display_qr_code": {
      "hosted_instructions_url": "https://payments.stripe.com/upi/instructions/xxx",
      "qrcode": {
        "image_url_png": "https://qr.stripe.com/test_xxxxxx.png",
        "image_url_svg": "https://qr.stripe.com/test_xxxxxx.svg",
        "expires_at": 1741165397
      }
    }
  },
  "id": "pi_1G1sgdKi6xqXeNtkldRRE6HT",
  "object": "payment_intent",
  ...
}
```

1. Redirect the customer to the URL provided in the `next_action.upi_handle_redirect_or_display_qr_code.hosted_instructions_url` property.

Alternatively, you can render the QR code yourself using the images in the fields `next_action.upi_handle_redirect_or_display_qr_code.image_url_png` or `next_action.upi_handle_redirect_or_display_qr_code.image_url_svg`.

## Detach a reusable payment method

To deactivate a reusable payment method, your server can call [detach PaymentMethod](https://docs.stripe.com/api/payment_methods/detach.md) API. Stripe sends both a [mandate.updated](https://docs.stripe.com/api/events/types.md#event_types-mandate.updated) event and a [payment_method.detached](https://docs.stripe.com/api/events/types.md#event_types-payment_method.detached) event. You can subscribe to [webhook](https://docs.stripe.com/webhooks.md) events to get notifications.
