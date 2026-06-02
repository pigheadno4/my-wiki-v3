<!-- Source URL: https://docs.stripe.com/payments/pix/save-payment-details -->
<!-- Fetched: 2026-05-06 -->

# Save payment details with Pix

Learn how to save Pix payment details and charge your customers later.

Save a customer’s Pix account for future payments. Saving Pix payment details for recurring use requires [Pix Automático](https://docs.stripe.com/payments/pix/pix-automatico.md), which creates a customer-authorized mandate. Your recurring payments might fail if the [mandate options](https://docs.stripe.com/payments/pix/pix-automatico.md#pix-automtico-customization) are violated.

If you use [Stripe Billing](https://docs.stripe.com/billing.md), you can [set up a subscription with Pix](https://docs.stripe.com/billing/subscriptions/pix.md) instead.

This guide covers how to save Pix payment details using [Checkout](https://docs.stripe.com/payments/checkout.md), Stripe’s fully hosted checkout page.

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create or retrieve a customer [Server-side]

To save a Pix payment method for future payments, you must attach it to an object that represents your customer. This can be either a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-configuration-customer) object or a [Customer](https://docs.stripe.com/api/customers/object.md) object.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

Create an object to represent your customer when they create an account with your business, or before you save a payment method for future payments. Associate this object’s ID with your own internal representation of the customer.

Create a new Customer or retrieve an existing Customer to associate with this payment. Include the following code on your server to create a new Customer.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create({
  description: "My First Test Customer (created for API docs)",
});
```

## Create a Checkout Session [Server-side]

Your customer must authorize a Pix Automático mandate for future payments through Stripe Checkout. This allows you to charge their Pix account on a recurring basis.

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

#### Save without charging

Create a Checkout Session in `setup` mode to collect Pix payment details without charging the customer. After creating the Checkout Session, redirect your customer to the [URL](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-url) returned in the response.

Mandate options dictate how the payment method can be saved for future payments. Learn more about the available [Pix Automático customization](https://docs.stripe.com/payments/pix/pix-automatico.md#pix-automtico-customization) parameters.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  mode: "setup",
  payment_method_types: ["pix"],
  currency: "brl",
  customer: "{{CUSTOMER_ID}}",
  payment_method_options: {
    pix: {
      mandate_options: {
        amount: 40000,
        payment_schedule: "monthly",
      },
    },
  },
  success_url: "https://example.com/success",
  cancel_url: "https://example.com/cancel",
});
```

After the customer completes the Checkout Session and authorizes the mandate in their banking app, the resulting `SetupIntent` has a `status` of `succeeded` and the `PaymentMethod` is attached to the Customer.

#### Save while charging

Create a Checkout Session in `payment` mode with [payment_method_options.pix.setup_future_usage](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_method_options-pix-setup_future_usage) set to `off_session` to charge the customer and save their payment details for future use. After creating the Checkout Session, redirect your customer to the [URL](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-url) returned in the response.

Mandate options dictate how the payment method can be saved for future payments. Learn more about the available [Pix Automático customization](https://docs.stripe.com/payments/pix/pix-automatico.md#pix-automtico-customization) parameters.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  mode: "payment",
  payment_method_types: ["pix"],
  currency: "brl",
  customer: "{{CUSTOMER_ID}}",
  line_items: [
    {
      price_data: {
        currency: "brl",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  payment_method_options: {
    pix: {
      setup_future_usage: "off_session",
      mandate_options: {
        amount: 2000,
        payment_schedule: "monthly",
      },
    },
  },
  success_url: "https://example.com/success",
  cancel_url: "https://example.com/cancel",
});
```

After the customer pays and authorizes the mandate in their banking app, the payment completes and the `PaymentMethod` is saved and attached to the Customer for future charges.

## Charge the saved payment method [Server-side]

After collecting and saving payment details, create a `PaymentIntent` to charge the customer using the saved payment method.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 2000,
  currency: "brl",
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{PAYMENT_METHOD_ID}}",
  off_session: true,
  confirm: true,
});
```

## Handle reusable payment method revocation [Server-side]

A customer can revoke a Pix mandate in their banking app. In this case, Stripe sends you a [mandate.updated](https://docs.stripe.com/api/events/types.md#event_types-mandate.updated) event. To handle this, subscribe to [webhook](https://docs.stripe.com/webhooks.md) events, and bring your customer back on-session to create a new mandate.

## Test your integration

To test your integration:

1. Select Pix.
1. Enter the buyer’s details and tap **Pay**. In a testing environment, you can use `000.000.000-00` as a test tax identifier (CPF or CNPJ).
1. Click **Simulate scan** to open a Stripe-hosted Pix test payment page. From this page, you can either authorize or expire the test payment.

In live mode, the **Pay** button displays a Pix QR code. You need a Brazilian bank account with Pix enabled to complete or cancel this payment flow.

You can also set [payment_method.billing_details.email](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_data-billing_details-email) to the following values to test different scenarios.

| Email                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `{any_prefix}expire_immediately@{any_domain}` | Simulates a Pix that expires immediately. The [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) or [setup_intent.setup_failed](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.setup_failed) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives within several seconds. No active mandate is created. |

Example: `expire_immediately@test.com` |
| `{any_prefix}expire_with_delay@{any_domain}` | Simulates a Pix that expires after 3 minutes. The [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) or [setup_intent.setup_failed](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.setup_failed) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives after about 3 minutes. No active mandate is created.

Example: `expire_with_delay@test.com` |
| `{any_prefix}succeed_mandate_expire_payments_immediately@{any_domain}` | Simulates a Pix that a customer pays immediately. The [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) or [setup_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.succeeded) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives within several seconds. An active mandate is created. Recurring payments with the same payment method expire immediately. The [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives within several seconds.

Example: `succeed_mandate_expire_payments_immediately@test.com` |
| `{any_prefix}succeed_mandate_expire_payments_with_delay@{any_domain}` | Simulates a Pix that a customer pays after 3 minutes. The [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) or [setup_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.succeeded) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives within several seconds. An active mandate is created. Recurring payments with the same payment method expire after 3 minutes. The [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives after about 3 minutes.

Example: `succeed_mandate_expire_payments_with_delay@test.com` |
| `{any_prefix}succeed_immediately@{any_domain}` | Simulates a Pix that a customer pays immediately. The [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) or [setup_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.succeeded) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives within several seconds. An active mandate is created. Any recurring payments with the same payment method succeed immediately. The [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives within several seconds.

Example: `succeed_immediately@test.com` |
| `{any_prefix}@{any_domain}` | Simulates a Pix that a customer pays after 3 minutes. The [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) or [setup_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.succeeded) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives after approximately 3 minutes. An active mandate is created. Any recurring payments with the same payment method succeed after 3 minutes. The [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives after approximately 3 minutes.

Example: `anything@test.com` |

# Direct API

> This is a Direct API for when payment-ui is direct-api. View the full page at https://docs.stripe.com/payments/pix/save-payment-details?payment-ui=direct-api.

If you want to create a customized payments UI, use the [Payment Intents API](https://docs.stripe.com/api/payment_intents.md) with [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) to charge your customer immediately or the [Setup Intents API](https://docs.stripe.com/api/setup_intents.md) to charge your customer later.

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create or retrieve a Customer [Server-side]

To save a Pix payment method for future payments, you must attach it to an object that represents your customer. This can be either a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-configuration-customer) object or a [Customer](https://docs.stripe.com/api/customers/object.md) object.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

Create an object to represent your customer when they create an account with your business, or before you save a payment method for future payments. Associate this object’s ID with your own internal representation of the customer.

Include the following code on your server to create a new Customer.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create({
  description: "My First Test Customer (created for API docs)",
});
```

## Create a PaymentIntent or SetupIntent [Server-side]

#### SetupIntent

Use the [Setup Intents API](https://docs.stripe.com/payments/setup-intents.md) to collect Pix payment method details without making an initial payment. This is useful for:

- Saving payment methods for customers so their later purchases don’t require on-session authorization
- Starting a free trial for a *subscription* (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis)

A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) is an object that represents your intent to set up a customer’s payment method for future payments. The SetupIntent tracks the steps of this set-up process.

Create a SetupIntent on your server with [payment_method_types](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-payment_method_types) set to `pix`, specify the customer’s ID, and provide the Pix Automático mandate options. Mandate options dictate how the payment method can be saved for future payments. Learn more about the available [Pix Automático customization](https://docs.stripe.com/payments/pix/pix-automatico.md#pix-automtico-customization) parameters.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ["pix"],
  customer: "{{CUSTOMER_ID}}",
  payment_method_options: {
    pix: {
      mandate_options: {
        amount: 40000,
        payment_schedule: "monthly",
      },
    },
  },
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

#### PaymentIntent

Use the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md) to collect Pix payment details and charge the customer immediately while saving the payment method for future use. This is useful for:

- Saving payment methods during the first purchase
- Enabling future off-session recurring charges

Create a PaymentIntent on your server with [payment_method_types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) set to `pix`, specify the customer’s ID, and set [setup_future_usage=off_session](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) to save the payment method for future charges. Provide the Pix Automático mandate options. Mandate options dictate how the payment method can be saved for future payments. Learn more about the available [Pix Automático customization](https://docs.stripe.com/payments/pix/pix-automatico.md#pix-automtico-customization) parameters.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["pix"],
  amount: 1000,
  currency: "brl",
  customer: "{{CUSTOMER_ID}}",
  setup_future_usage: "off_session",
  payment_method_options: {
    pix: {
      mandate_options: {
        amount: 1000,
        payment_schedule: "monthly",
      },
    },
  },
});
```

### Retrieve the client secret

The PaymentIntent includes a *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)) that the client side uses to securely complete the payment process. You can use different approaches to pass the client secret to the client side.

#### Single-page application

Retrieve the client secret from an endpoint on your server, using the browser’s `fetch` function. This approach is best if your client side is a single-page application, particularly one built with a modern frontend framework like React. Create the server endpoint that serves the client secret:

#### Node.js

```javascript
const express = require("express");
const app = express();

app.get("/secret", async (req, res) => {
  const intent = // ... Fetch or create the PaymentIntent
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

Add the [client_secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) in your checkout form. In your server-side code, retrieve the client secret from the PaymentIntent:

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
  const intent = // ... Fetch or create the PaymentIntent
    res.render("checkout", { client_secret: intent.client_secret });
});

app.listen(3000, () => {
  console.log("Running on port 3000");
});
```

## Collect payment method details [Client-side]

#### HTML + JS

Create a payment form on your client to collect the required billing details from the customer:

| Field    | Value                                                                                                                                                                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`   | The customer’s full name.                                                                                                                                                                                                                       |
| `email`  | The customer’s email address.                                                                                                                                                                                                                   |
| `tax_id` | The customer’s tax identifier: a CPF if the customer is an individual, or a CNPJ if the customer is a business. The Brazilian government requires that buyers provide a tax identifier (CPF or CNPJ) when completing cross-border transactions. |

```html
<form id="payment-form">
  <div class="form-row">
    <label for="name">Full Name:</label>
    <input id="name" name="name" required />
  </div>
  <div class="form-row">
    <label for="email">Email:</label>
    <input id="email" name="email" required />
  </div>
  <div class="form-row">
    <label for="tax-id">CPF or CNPJ:</label>
    <input id="tax-id" name="tax-id" required />
  </div>

  <!-- Used to display form errors. -->
  <div id="error-message" role="alert"></div>

  <button id="submit-button">Save payment details</button>
</form>
```

#### React

#### npm

Install [React Stripe.js](https://www.npmjs.com/package/@stripe/react-stripe-js) and the [Stripe.js loader](https://www.npmjs.com/package/@stripe/stripe-js) from the npm public registry.

```bash
npm install --save @stripe/react-stripe-js @stripe/stripe-js
```

#### umd

We also provide a UMD build for sites that don’t use npm or modules.

Include the Stripe.js script, which exports a global `Stripe` function, and the UMD build of React Stripe.js, which exports a global `ReactStripe` object. Always load the Stripe.js script directly from **js.stripe.com** to remain PCI compliant. Don’t include the script in a bundle or host a copy of it yourself.

```html
<!-- Stripe.js -->
<script src="https://js.stripe.com/dahlia/stripe.js"></script>

<!-- React Stripe.js development build -->
<script src="https://unpkg.com/@stripe/react-stripe-js@latest/dist/react-stripe.umd.js"></script>

<!-- When you are ready to deploy your site to production, remove the
      above development script, and include the following production build. -->
<script src="https://unpkg.com/@stripe/react-stripe-js@latest/dist/react-stripe.umd.min.js"></script>
```

> The [demo in CodeSandbox](https://codesandbox.io/s/react-stripe-official-q1loc?fontsize=14&hidenavigation=1&theme=dark) lets you try out React Stripe.js without having to create a new project.

### Add Stripe.js and Elements to your page

To use Element components, wrap your checkout page component in an [Elements provider](https://docs.stripe.com/sdks/stripejs-react.md#elements-provider). Call `loadStripe` with your publishable key and pass the returned `Promise` to the `Elements` provider.

```jsx
import React from "react";
import ReactDOM from "react-dom";
import { Elements } from "@stripe/react-stripe-js";
import { loadStripe } from "@stripe/stripe-js";

import CheckoutForm from "./CheckoutForm";

// Make sure to call `loadStripe` outside of a component's render to avoid
// recreating the `Stripe` object on every render.
const stripePromise = loadStripe("<<YOUR_PUBLISHABLE_KEY>>");

function App() {
  return (
    <Elements stripe={stripePromise}>
      <CheckoutForm />
    </Elements>
  );
}

ReactDOM.render(<App />, document.getElementById("root"));
```

## Display the Pix QR Code with Stripe [Client-side]

#### SetupIntent

Include the Stripe.js script on your checkout page by adding it to the `head` of your HTML file.

```html
<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/dahlia/stripe.js"></script>
</head>
```

Create an instance of Stripe.js with the following JavaScript on your checkout page:

```javascript
var stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");
```

Call [stripe.confirmPixSetup](https://docs.stripe.com/js/setup_intents/confirm_pix_setup) to confirm the SetupIntent on the client side. Include a `return_url` to redirect your customer after they authorize the mandate.

```javascript
const form = document.getElementById("payment-form");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const { error } = await stripe.confirmPixSetup(
    "{{SETUP_INTENT_CLIENT_SECRET}}",
    {
      payment_method: {
        billing_details: {
          name: document.getElementById("name").value,
          email: document.getElementById("email").value,
          tax_id: document.getElementById("tax-id").value,
        },
      },
      return_url: "https://example.com/checkout/complete",
    },
  );

  if (error) {
    // Inform the customer that there was an error.
  }
});
```

### Handling the redirect

The following URL query parameters are provided when Stripe redirects the customer to the `return_url`.

| Parameter                    | Description                                                                                                                             |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `setup_intent`               | The unique identifier for the `SetupIntent`.                                                                                            |
| `setup_intent_client_secret` | The [client secret](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-client_secret) of the `SetupIntent` object. |

You can also append your own query parameters when providing the `return_url`. They persist throughout the redirect process. The `return_url` should correspond to a page on your website that provides the status of the setup. Verify the status of the `SetupIntent` when rendering the return page by using the `retrieveSetupIntent` function from Stripe.js and passing in the `setup_intent_client_secret`.

```javascript
(async () => {
  const url = new URL(window.location);
  const clientSecret = url.searchParams.get("setup_intent_client_secret");

  const { setupIntent, error } = await stripe.retrieveSetupIntent(clientSecret);
  if (error) {
    // Handle error
  } else if (setupIntent && setupIntent.status === "succeeded") {
    // Handle successful setup
  }
})();
```

After the customer authorizes the mandate in their banking app, the SetupIntent moves to a `succeeded` state and the PaymentMethod is attached to the Customer.

#### PaymentIntent

Include the Stripe.js script on your checkout page by adding it to the `head` of your HTML file.

```html
<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/dahlia/stripe.js"></script>
</head>
```

Create an instance of Stripe.js with the following JavaScript on your checkout page:

```javascript
var stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");
```

Call [stripe.confirmPixPayment](https://docs.stripe.com/js/payment_intents/confirm_pix_payment) to render the QR code that allows your customer to complete their payment. Include a `return_url` to redirect your customer after they complete the payment.

```javascript
const form = document.getElementById("payment-form");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const { error } = await stripe.confirmPixPayment(
    "{{PAYMENT_INTENT_CLIENT_SECRET}}",
    {
      payment_method: {
        billing_details: {
          name: document.getElementById("name").value,
          email: document.getElementById("email").value,
          tax_id: document.getElementById("tax-id").value,
        },
      },
      return_url: "https://example.com/checkout/complete",
    },
  );

  if (error) {
    // Inform the customer that there was an error.
  }
});
```

### Handling the redirect

The following URL query parameters are provided when Stripe redirects the customer to the `return_url`.

| Parameter                      | Description                                                                                                                                   |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_intent`               | The unique identifier for the `PaymentIntent`.                                                                                                |
| `payment_intent_client_secret` | The [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) of the `PaymentIntent` object. |

You can also append your own query parameters when providing the `return_url`. They persist throughout the redirect process. The `return_url` should correspond to a page on your website that provides the status of the payment. You should verify the status of the `PaymentIntent` when rendering the return page. You can do so by using the `retrievePaymentIntent` function from Stripe.js and passing in the `payment_intent_client_secret`.

```javascript
(async () => {
  const url = new URL(window.location);
  const clientSecret = url.searchParams.get("payment_intent_client_secret");

  const { paymentIntent, error } =
    await stripe.retrievePaymentIntent(clientSecret);
  if (error) {
    // Handle error
  } else if (paymentIntent && paymentIntent.status === "succeeded") {
    // Handle successful payment
  }
})();
```

After the customer pays and authorizes the mandate in their banking app, the PaymentIntent moves to a `succeeded` state. The PaymentMethod is saved and attached to the Customer for future charges.

## Optional: Display the Pix QR Code yourself [Client-side]

#### SetupIntent

We recommend using Stripe.js to display the Pix details with `confirmPixSetup`. However, you can also manually display the Pix string or QR code to your customers.

Specify `handleActions: false` when calling `stripe.confirmPixSetup` to manually handle the next action to display the Pix details to your customer.

```javascript
var form = document.getElementById("payment-form");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const result = await stripe.confirmPixSetup(
    "{{SETUP_INTENT_CLIENT_SECRET}}",
    {
      // payment method details omitted for brevity
    },
    {
      handleActions: false,
    },
  );

  if (result.error) {
    // Display error to your customer
    const errorMsg = document.getElementById("error-message");
    errorMsg.innerText = result.error.message;
  } else {
    // Pix details were successfully created
    const details = result.setupIntent.next_action.pix_display_qr_code;
    // Pix string, also known as Pix “copy and paste”
    const emvString = details.data;
    // SVG image Pix QR code
    const imageUrlSvg = details.image_url_svg;
    // PNG image Pix QR code
    const imageUrlPng = details.image_url_png;
    // Pix expiration date as a unix timestamp
    const expires_at = details.expires_at;
    // Handle the next action by displaying the Pix details to your customer
    // You can also use the generated hosted instructions
    const hosted_instructions_url = details.hosted_instructions_url;
  }
});
```

We suggest you display the following:

| Detail               | Description                                                                                                                                                                                                                                                                             |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pix string           | Display the Pix string for your customers to copy it to their clipboard using the SetupIntent’s [setup_intent.next_action.pix_display_qr_code.data](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-next_action-pix_display_qr_code-data) string.               |
| QR code as SVG image | Display the Pix QR code for your customers to scan with their phone using the SetupIntent’s [setup_intent.next_action.pix_display_qr_code.image_url_svg](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-next_action-pix_display_qr_code-image_url_svg) string. |
| QR code as PNG image | Display the Pix QR code for your customers to scan with their phone using the SetupIntent’s [setup_intent.next_action.pix_display_qr_code.image_url_png](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-next_action-pix_display_qr_code-image_url_png) string. |
| Expiry date          | Display the Pix expiration date. Use [setup_intent.next_action.pix_display_qr_code.expires_at](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-next_action-pix_display_qr_code-expires_at) to see the expiration date.                                          |

You can also redirect customers to the Stripe-hosted instructions page, which is similar to the modal opened by `confirmPixSetup`. Use [setup_intent.next_action.pix_display_qr_code.hosted_instructions_url](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-next_action-pix_display_qr_code-hosted_instructions_url) to find the Stripe-hosted instructions page URL on the SetupIntent object.

#### PaymentIntent

We recommend using Stripe.js to display the Pix details with `confirmPixPayment`. However, you can also manually display the Pix string or QR code to your customers.

Specify `handleActions: false` when calling `stripe.confirmPixPayment` to manually handle the next action to display the Pix details to your customer.

```javascript
var form = document.getElementById("payment-form");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const result = await stripe.confirmPixPayment(
    "{{PAYMENT_INTENT_CLIENT_SECRET}}",
    {
      // payment method details omitted for brevity
    },
    {
      handleActions: false,
    },
  );

  if (result.error) {
    // Display error to your customer
    const errorMsg = document.getElementById("error-message");
    errorMsg.innerText = result.error.message;
  } else {
    // Pix details were successfully created
    const amount = result.paymentIntent.amount;
    const currency = result.paymentIntent.currency;
    const details = result.paymentIntent.next_action.pix_display_qr_code;
    // Pix string, also known as Pix “copy and paste”
    const emvString = details.data;
    // SVG image Pix QR code
    const imageUrlSvg = details.image_url_svg;
    // PNG image Pix QR code
    const imageUrlPng = details.image_url_png;
    // Pix expiration date as a unix timestamp
    const expires_at = details.expires_at;
    // Handle the next action by displaying the Pix details to your customer
    // You can also use the generated hosted instructions
    const hosted_instructions_url = details.hosted_instructions_url;
  }
});
```

We suggest you display the following:

| Detail               | Description                                                                                                                                                                                                                                                                                     |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pix string           | Display the Pix string for your customers to copy it to their clipboard using the PaymentIntent’s [payment_intent.next_action.pix_display_qr_code.data](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-pix_display_qr_code-data) string.               |
| QR code as SVG image | Display the Pix QR code for your customers to scan with their phone using the PaymentIntent’s [payment_intent.next_action.pix_display_qr_code.image_url_svg](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-pix_display_qr_code-image_url_svg) string. |
| QR code as PNG image | Display the Pix QR code for your customers to scan with their phone using the PaymentIntent’s [payment_intent.next_action.pix_display_qr_code.image_url_png](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-pix_display_qr_code-image_url_png) string. |
| Expiry date          | Display the Pix expiration date. Use [payment_intent.next_action.pix_display_qr_code.expires_at](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-pix_display_qr_code-expires_at) to see the expiration date.                                            |

You can also redirect customers to the Stripe-hosted instructions page, which is similar to the modal opened by `confirmPixPayment`. Use [payment_intent.next_action.pix_display_qr_code.hosted_instructions_url](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-pix_display_qr_code-hosted_instructions_url) to find the Stripe-hosted instructions page URL on the PaymentIntent object.

## Charge a saved payment method [Server-side]

After you save a Pix [PaymentMethod](https://docs.stripe.com/api/payment_methods.md), you can accept future payments by creating and confirming a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md). Use the same payment method ID from the previous SetupIntent or PaymentIntent object. Set `off_session` to `true` if the customer isn’t in a checkout flow for this PaymentIntent.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["pix"],
  payment_method: "{{PAYMENT_METHOD_ID}}",
  amount: 1000,
  currency: "brl",
  customer: "{{CUSTOMER_ID}}",
  confirm: true,
  off_session: true,
});
```

## Handle reusable payment method revocation [Server-side]

A customer can revoke a Pix mandate in their banking app. In this case, Stripe sends you a [mandate.updated](https://docs.stripe.com/api/events/types.md#event_types-mandate.updated) event. To handle this, subscribe to [webhook](https://docs.stripe.com/webhooks.md) events, and bring your customer back on-session to create a new mandate.

## Test your integration

To test your integration:

1. Select Pix.
1. Enter the buyer’s details and tap **Pay**. In a testing environment, you can use `000.000.000-00` as a test tax identifier (CPF or CNPJ).
1. Click **Simulate scan** to open a Stripe-hosted Pix test payment page. From this page, you can either authorize or expire the test payment.

In live mode, the **Pay** button displays a Pix QR code. You need a Brazilian bank account with Pix enabled to complete or cancel this payment flow.

You can also set [payment_method.billing_details.email](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_data-billing_details-email) to the following values to test different scenarios.

| Email                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `{any_prefix}expire_immediately@{any_domain}` | Simulates a Pix that expires immediately. The [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) or [setup_intent.setup_failed](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.setup_failed) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives within several seconds. No active mandate is created. |

Example: `expire_immediately@test.com` |
| `{any_prefix}expire_with_delay@{any_domain}` | Simulates a Pix that expires after 3 minutes. The [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) or [setup_intent.setup_failed](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.setup_failed) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives after about 3 minutes. No active mandate is created.

Example: `expire_with_delay@test.com` |
| `{any_prefix}succeed_mandate_expire_payments_immediately@{any_domain}` | Simulates a Pix that a customer pays immediately. The [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) or [setup_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.succeeded) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives within several seconds. An active mandate is created. Recurring payments with the same payment method expire immediately. The [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives within several seconds.

Example: `succeed_mandate_expire_payments_immediately@test.com` |
| `{any_prefix}succeed_mandate_expire_payments_with_delay@{any_domain}` | Simulates a Pix that a customer pays after 3 minutes. The [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) or [setup_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.succeeded) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives within several seconds. An active mandate is created. Recurring payments with the same payment method expire after 3 minutes. The [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives after about 3 minutes.

Example: `succeed_mandate_expire_payments_with_delay@test.com` |
| `{any_prefix}succeed_immediately@{any_domain}` | Simulates a Pix that a customer pays immediately. The [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) or [setup_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.succeeded) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives within several seconds. An active mandate is created. Any recurring payments with the same payment method succeed immediately. The [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives within several seconds.

Example: `succeed_immediately@test.com` |
| `{any_prefix}@{any_domain}` | Simulates a Pix that a customer pays after 3 minutes. The [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) or [setup_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.succeeded) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives after approximately 3 minutes. An active mandate is created. Any recurring payments with the same payment method succeed after 3 minutes. The [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives after approximately 3 minutes.

Example: `anything@test.com` |

## Optional: Handle payment failures

If the failure isn’t related to a mandate violation, Stripe [retries the payment](https://docs.stripe.com/payments/pix/pix-automatico.md#retries).

If the payment fails after exhausting all of the retries, you can bring your customer back on-session to create a new payment.

## Optional: Handle add-on purchases after mandate creation

Due to scheme restrictions, you can only charge a Pix payment method once per cycle specified in `payment_method_options.pix.mandate_options.payment_schedule`. If your users can buy add-ons after the mandate creation, you can bring your customer back on-session to create a new payment.
