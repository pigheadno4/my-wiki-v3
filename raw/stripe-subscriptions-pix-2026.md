<!-- Source URL: https://docs.stripe.com/billing/subscriptions/pix -->
<!-- Fetched: 2026-05-13 -->

# Set up a subscription with Pix

Learn how to create and charge for a subscription with Pix.

Use this guide to set up a _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) using [Pix](https://docs.stripe.com/payments/pix.md) as a payment method. Pix subscriptions use [Pix Automático](https://docs.stripe.com/payments/pix/pix-automatico.md) to create a customer-authorized mandate for automatic recurring charges.

# Stripe-hosted page

> This is a Stripe-hosted page for when api-integration is checkout. View the full page at https://docs.stripe.com/billing/subscriptions/pix?api-integration=checkout.

You can use the [Checkout API](https://docs.stripe.com/api/checkout/sessions.md) to create and confirm a subscription with a prebuilt checkout page.

## Create a product and price [Dashboard]

[Products](https://docs.stripe.com/api/products.md) represent the item or service you’re selling. [Prices](https://docs.stripe.com/api/prices.md) define how much and how frequently you charge for a product. This includes how much the product costs, what currency you accept, and whether it’s a one-time or recurring charge. If you only have a few products and prices, create and manage them in the Dashboard.

This guide uses a stock photo service as an example and charges customers a 20 BRL monthly subscription. To model this:

1. Go to the [Products](https://dashboard.stripe.com/products?active=true) page and click **Create product**.
1. Enter a **Name** for the product. You can optionally add a **Description** and upload an image of the product.
1. Select a **Product tax code**. Learn more about [product tax codes](https://docs.stripe.com/tax/tax-codes.md).
1. Select **Recurring**. Then enter **20** for the price and select **BRL** as the currency.
1. Choose whether to **Include tax in price**. You can either use the default value from your [tax settings](https://dashboard.stripe.com/test/settings/tax) or set the value manually. In this example, select **Auto**.
1. Select **Monthly** for the **Billing period**.
1. Click **More pricing options**. Then select **Flat rate** as the pricing model for this example. Learn more about [flat rate](https://docs.stripe.com/products-prices/pricing-models.md#flat-rate) and other [pricing models](https://docs.stripe.com/products-prices/pricing-models.md).
1. Add an internal **Price description** and [Lookup key](https://docs.stripe.com/products-prices/manage-prices.md#lookup-keys) to organize, query, and update specific prices in the future.
1. Click **Next**. Then click **Add product**.

After you create the product and the price, record the price ID so you can use it in subsequent steps. The pricing page displays the ID and it looks similar to this: `price_G0FvDp6vZvdwRZ`.

## Create a Checkout Session [Server-side]

Your customer must authorize a Pix Automático mandate for the subscription through Stripe Checkout.

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

Create a Checkout Session in `subscription` mode with [Pix Automático mandate options](https://docs.stripe.com/payments/pix/pix-automatico.md#pix-automtico-customization). After creating the Checkout Session, redirect your customer to the [URL](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-url) returned in the response.

> If you want to encourage users to upgrade to a higher subscription plan without coming back on session, you can pass a higher amount in `payment_method_options.pix.mandate_options.amount`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  success_url: "https://example.com/success",
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  payment_method_types: ["pix"],
  payment_method_options: {
    pix: {
      mandate_options: {
        amount: 2000,
        payment_schedule: "monthly",
      },
    },
  },
  mode: "subscription",
});
```

After the customer authorizes the mandate in their banking app, the subscription activates and subsequent invoices charge automatically.

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
| `{any_prefix}expire_immediately@{any_domain}` | Simulates a Pix that expires immediately. The [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) or [setup_intent.setup_failed](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.setup_failed) _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives within several seconds. No active mandate is created. |

Example: `expire_immediately@test.com` |
| `{any_prefix}expire_with_delay@{any_domain}` | Simulates a Pix that expires after 3 minutes. The [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) or [setup_intent.setup_failed](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.setup_failed) _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives after about 3 minutes. No active mandate is created.

Example: `expire_with_delay@test.com` |
| `{any_prefix}succeed_mandate_expire_payments_immediately@{any_domain}` | Simulates a Pix that a customer pays immediately. The [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) or [setup_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.succeeded) _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives within several seconds. An active mandate is created. Recurring payments with the same payment method expire immediately. The [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives within several seconds.

Example: `succeed_mandate_expire_payments_immediately@test.com` |
| `{any_prefix}succeed_mandate_expire_payments_with_delay@{any_domain}` | Simulates a Pix that a customer pays after 3 minutes. The [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) or [setup_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.succeeded) _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives within several seconds. An active mandate is created. Recurring payments with the same payment method expire after 3 minutes. The [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives after about 3 minutes.

Example: `succeed_mandate_expire_payments_with_delay@test.com` |
| `{any_prefix}succeed_immediately@{any_domain}` | Simulates a Pix that a customer pays immediately. The [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) or [setup_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.succeeded) _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives within several seconds. An active mandate is created. Any recurring payments with the same payment method succeed immediately. The [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives within several seconds.

Example: `succeed_immediately@test.com` |
| `{any_prefix}@{any_domain}` | Simulates a Pix that a customer pays after 3 minutes. The [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) or [setup_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.succeeded) _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives after approximately 3 minutes. An active mandate is created. Any recurring payments with the same payment method succeed after 3 minutes. The [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives after approximately 3 minutes.

Example: `anything@test.com` |

# Setup Intents API

> This is a Setup Intents API for when api-integration is setupintents. View the full page at https://docs.stripe.com/billing/subscriptions/pix?api-integration=setupintents.

Create and confirm a subscription using two API calls. The [first API call](https://docs.stripe.com/billing/subscriptions/pix.md#create-setup-intent) uses the [Setup Intents API](https://docs.stripe.com/api/setup_intents.md) to set Pix as a payment method and create a mandate. The [second API call](https://docs.stripe.com/billing/subscriptions/pix.md#create-subscription) sends customer, product, and payment method information to the [Subscriptions API](https://docs.stripe.com/api/subscriptions.md) to create a Subscription and confirm a payment in one call.

## Create a product and price [Dashboard]

[Products](https://docs.stripe.com/api/products.md) represent the item or service you’re selling. [Prices](https://docs.stripe.com/api/prices.md) define how much and how frequently you charge for a product. This includes how much the product costs, what currency you accept, and whether it’s a one-time or recurring charge. If you only have a few products and prices, create and manage them in the Dashboard.

This guide uses a stock photo service as an example and charges customers a 20 BRL monthly subscription. To model this:

1. Go to the [Products](https://dashboard.stripe.com/products?active=true) page and click **Create product**.
1. Enter a **Name** for the product. You can optionally add a **Description** and upload an image of the product.
1. Select a **Product tax code**. Learn more about [product tax codes](https://docs.stripe.com/tax/tax-codes.md).
1. Select **Recurring**. Then enter **20** for the price and select **BRL** as the currency.
1. Choose whether to **Include tax in price**. You can either use the default value from your [tax settings](https://dashboard.stripe.com/test/settings/tax) or set the value manually. In this example, select **Auto**.
1. Select **Monthly** for the **Billing period**.
1. Click **More pricing options**. Then select **Flat rate** as the pricing model for this example. Learn more about [flat rate](https://docs.stripe.com/products-prices/pricing-models.md#flat-rate) and other [pricing models](https://docs.stripe.com/products-prices/pricing-models.md).
1. Add an internal **Price description** and [Lookup key](https://docs.stripe.com/products-prices/manage-prices.md#lookup-keys) to organize, query, and update specific prices in the future.
1. Click **Next**. Then click **Add product**.

After you create the product and the price, record the price ID so you can use it in subsequent steps. The pricing page displays the ID and it looks similar to this: `price_G0FvDp6vZvdwRZ`.

## Create or retrieve a customer [Server-side]

To save a Pix payment method for future payments, attach it to an object that represents your customer.

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

Use the [Setup Intents API](https://docs.stripe.com/payments/setup-intents.md) to collect Pix payment method details without making an initial payment.

A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) is an object that represents your intent to set up a customer’s payment method for future payments. The SetupIntent tracks the steps of this set-up process.

Create a SetupIntent on your server with [payment_method_types](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-payment_method_types) set to `pix`, specify the customer’s ID, and provide the Pix Automático [mandate options](https://docs.stripe.com/payments/pix/pix-automatico.md#pix-automtico-customization). Mandate options dictate how the payment method can be saved for future payments.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ["pix"],
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  payment_method_options: {
    pix: {
      mandate_options: {
        amount: 2000,
        payment_schedule: "monthly",
      },
    },
  },
});
```

#### Customers v1

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
        amount: 2000,
        payment_schedule: "monthly",
      },
    },
  },
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

## Optional: Display the Pix QR Code yourself [Client-side]

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

## Create a subscription [Server-side]

Create a subscription that has a price and customer. Set the value of the `default_payment_method` parameter to the PaymentMethod ID from the SetupIntent response.

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
  default_payment_method: "{{PAYMENT_METHOD_ID}}",
  payment_settings: {
    payment_method_types: ["pix"],
  },
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
  default_payment_method: "{{PAYMENT_METHOD_ID}}",
  payment_settings: {
    payment_method_types: ["pix"],
  },
});
```

Creating the subscription automatically charges the customer because of the pre-set default payment method. After a successful payment, the status in the Stripe Dashboard changes to Active. The price that you previously set up determines the amount for future billings.

> To create a _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) with a free trial period, see [Subscription trials](https://docs.stripe.com/billing/subscriptions/trials.md).

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
| `{any_prefix}expire_immediately@{any_domain}` | Simulates a Pix that expires immediately. The [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) or [setup_intent.setup_failed](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.setup_failed) _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives within several seconds. No active mandate is created. |

Example: `expire_immediately@test.com` |
| `{any_prefix}expire_with_delay@{any_domain}` | Simulates a Pix that expires after 3 minutes. The [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) or [setup_intent.setup_failed](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.setup_failed) _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives after about 3 minutes. No active mandate is created.

Example: `expire_with_delay@test.com` |
| `{any_prefix}succeed_mandate_expire_payments_immediately@{any_domain}` | Simulates a Pix that a customer pays immediately. The [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) or [setup_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.succeeded) _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives within several seconds. An active mandate is created. Recurring payments with the same payment method expire immediately. The [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives within several seconds.

Example: `succeed_mandate_expire_payments_immediately@test.com` |
| `{any_prefix}succeed_mandate_expire_payments_with_delay@{any_domain}` | Simulates a Pix that a customer pays after 3 minutes. The [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) or [setup_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.succeeded) _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives within several seconds. An active mandate is created. Recurring payments with the same payment method expire after 3 minutes. The [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives after about 3 minutes.

Example: `succeed_mandate_expire_payments_with_delay@test.com` |
| `{any_prefix}succeed_immediately@{any_domain}` | Simulates a Pix that a customer pays immediately. The [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) or [setup_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.succeeded) _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives within several seconds. An active mandate is created. Any recurring payments with the same payment method succeed immediately. The [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives within several seconds.

Example: `succeed_immediately@test.com` |
| `{any_prefix}@{any_domain}` | Simulates a Pix that a customer pays after 3 minutes. The [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) or [setup_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.succeeded) _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives after approximately 3 minutes. An active mandate is created. Any recurring payments with the same payment method succeed after 3 minutes. The [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives after approximately 3 minutes.

Example: `anything@test.com` |

# Subscriptions API

> This is a Subscriptions API for when api-integration is subscription. View the full page at https://docs.stripe.com/billing/subscriptions/pix?api-integration=subscription.

Create and confirm a Subscription using two API calls. The [first API call](https://docs.stripe.com/billing/subscriptions/pix.md#pi-create-subscription) sends customer and product information to the [Subscriptions API](https://docs.stripe.com/api/subscriptions.md) to create a Subscription and PaymentIntent in one call. The response includes a PaymentIntent ID that you must use to [confirm a payment](https://docs.stripe.com/billing/subscriptions/pix.md#display-qr-code-stripe).

## Create a product and price [Dashboard]

[Products](https://docs.stripe.com/api/products.md) represent the item or service you’re selling. [Prices](https://docs.stripe.com/api/prices.md) define how much and how frequently you charge for a product. This includes how much the product costs, what currency you accept, and whether it’s a one-time or recurring charge. If you only have a few products and prices, create and manage them in the Dashboard.

This guide uses a stock photo service as an example and charges customers a 20 BRL monthly subscription. To model this:

1. Go to the [Products](https://dashboard.stripe.com/products?active=true) page and click **Create product**.
1. Enter a **Name** for the product. You can optionally add a **Description** and upload an image of the product.
1. Select a **Product tax code**. Learn more about [product tax codes](https://docs.stripe.com/tax/tax-codes.md).
1. Select **Recurring**. Then enter **20** for the price and select **BRL** as the currency.
1. Choose whether to **Include tax in price**. You can either use the default value from your [tax settings](https://dashboard.stripe.com/test/settings/tax) or set the value manually. In this example, select **Auto**.
1. Select **Monthly** for the **Billing period**.
1. Click **More pricing options**. Then select **Flat rate** as the pricing model for this example. Learn more about [flat rate](https://docs.stripe.com/products-prices/pricing-models.md#flat-rate) and other [pricing models](https://docs.stripe.com/products-prices/pricing-models.md).
1. Add an internal **Price description** and [Lookup key](https://docs.stripe.com/products-prices/manage-prices.md#lookup-keys) to organize, query, and update specific prices in the future.
1. Click **Next**. Then click **Add product**.

After you create the product and the price, record the price ID so you can use it in subsequent steps. The pricing page displays the ID and it looks similar to this: `price_G0FvDp6vZvdwRZ`.

## Create or retrieve a customer [Server-side]

To save a Pix payment method for future payments, attach it to an object that represents your customer.

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

## Create a subscription [Server-side]

Create a [subscription](https://docs.stripe.com/api/subscriptions.md) that has a price and customer with status of `incomplete` by providing the [payment_behavior](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-payment_behavior) parameter with a value of `default_incomplete`. Set the `payment_settings.save_default_payment_method=on_subscription` parameter to save a payment method when a subscription is activated.

Optionally, provide the [Pix Automático mandate options](https://docs.stripe.com/payments/pix/pix-automatico.md#pix-automtico-customization).

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  payment_behavior: "default_incomplete",
  items: [
    {
      price: "{{PRICE_ID}}",
    },
  ],
  payment_settings: {
    save_default_payment_method: "on_subscription",
    payment_method_types: ["pix"],
    payment_method_options: {
      pix: {
        mandate_options: {
          amount: 2000,
        },
      },
    },
  },
  expand: ["latest_invoice.payments", "latest_invoice.confirmation_secret"],
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer: "{{CUSTOMER_ID}}",
  payment_behavior: "default_incomplete",
  items: [
    {
      price: "{{PRICE_ID}}",
    },
  ],
  payment_settings: {
    save_default_payment_method: "on_subscription",
    payment_method_types: ["pix"],
    payment_method_options: {
      pix: {
        mandate_options: {
          amount: 2000,
        },
      },
    },
  },
  expand: ["latest_invoice.payments", "latest_invoice.confirmation_secret"],
});
```

The response includes the _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis)’s first [Invoice](https://docs.stripe.com/api/invoices.md). This contains the invoice’s payments, which includes a default PaymentIntent that Stripe generated for this invoice and the confirmation secret which you can use on the client side to securely complete the payment process instead of passing the entire PaymentIntent object. Return the `latest_invoice.confirmation_secret.client_secret` to the front end to complete payment.

Get the PaymentIntent ID that you must use to confirm a payment from `latest_invoice.payments`.

> To create a _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) with a free trial period, see [Subscription trials](https://docs.stripe.com/billing/subscriptions/trials.md).

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

After the customer authorizes the mandate in their banking app, the payment gets confirmed and the `PaymentIntent` moves to a `succeeded` state.

After a successful payment, the subscription becomes active and saves the payment method as the default payment method.

## Optional: Display the Pix QR Code yourself [Client-side]

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
| `{any_prefix}expire_immediately@{any_domain}` | Simulates a Pix that expires immediately. The [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) or [setup_intent.setup_failed](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.setup_failed) _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives within several seconds. No active mandate is created. |

Example: `expire_immediately@test.com` |
| `{any_prefix}expire_with_delay@{any_domain}` | Simulates a Pix that expires after 3 minutes. The [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) or [setup_intent.setup_failed](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.setup_failed) _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives after about 3 minutes. No active mandate is created.

Example: `expire_with_delay@test.com` |
| `{any_prefix}succeed_mandate_expire_payments_immediately@{any_domain}` | Simulates a Pix that a customer pays immediately. The [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) or [setup_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.succeeded) _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives within several seconds. An active mandate is created. Recurring payments with the same payment method expire immediately. The [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives within several seconds.

Example: `succeed_mandate_expire_payments_immediately@test.com` |
| `{any_prefix}succeed_mandate_expire_payments_with_delay@{any_domain}` | Simulates a Pix that a customer pays after 3 minutes. The [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) or [setup_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.succeeded) _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives within several seconds. An active mandate is created. Recurring payments with the same payment method expire after 3 minutes. The [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives after about 3 minutes.

Example: `succeed_mandate_expire_payments_with_delay@test.com` |
| `{any_prefix}succeed_immediately@{any_domain}` | Simulates a Pix that a customer pays immediately. The [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) or [setup_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.succeeded) _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives within several seconds. An active mandate is created. Any recurring payments with the same payment method succeed immediately. The [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives within several seconds.

Example: `succeed_immediately@test.com` |
| `{any_prefix}@{any_domain}` | Simulates a Pix that a customer pays after 3 minutes. The [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) or [setup_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.succeeded) _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives after approximately 3 minutes. An active mandate is created. Any recurring payments with the same payment method succeed after 3 minutes. The [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives after approximately 3 minutes.

Example: `anything@test.com` |

## Optional: Change the pricing of an existing subscription

You can [update the pricing of an existing subscription](https://docs.stripe.com/api/subscriptions/update.md).

If the new total amount in the subscription is greater than the amount in the mandate, the recurring payments might fail and trigger a [payment failed](https://docs.stripe.com/billing/subscriptions/webhooks.md#payment-failures) webhook event. These payments might fail because customers have the option to set a limit, but Stripe doesn’t have any visibility into this limit. The status of the subscription might change depending on your [subscription configuration](https://docs.stripe.com/billing/subscriptions/overview.md#subscription-statuses).

You have several options for handling these scenarios:

- You can ask your customer to increase the mandate amount in their banking app.
- You can update the mandate options with the new amount using the [Update Subscription](https://docs.stripe.com/api/subscriptions/update.md) API and create a [Customer Portal](https://docs.stripe.com/api/customer_portal/sessions/create.md) session for your customer to update their Pix payment method.
- You can update the mandate options with the new amount using the [Update Subscription](https://docs.stripe.com/api/subscriptions/update.md) API and create a [Checkout Session](https://docs.stripe.com/api/checkout/sessions/create.md) in `setup` mode (without an initial payment) or in `payment` mode with [payment_method_options.pix.setup_future_usage](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_method_options-pix-setup_future_usage)=`off_session` (with an initial payment) to create a new mandate with a new payment method, and [update the payment method of the subscription](https://docs.stripe.com/payments/checkout/subscriptions/update-payment-details.md#set-default-payment-method).
- You can cancel and re-create the subscription.

## Optional: Change the billing cycle of an existing subscription

You can [update the billing cycle of an existing subscription](https://docs.stripe.com/api/subscriptions/update.md).

If the payment schedule in the mandate options is more restrictive than the new interval of the subscription (for example, if the mandate’s `payment_schedule=monthly` and the new `interval=weekly`), the recurring payments fail and you receive a [payment failed](https://docs.stripe.com/billing/subscriptions/webhooks.md#payment-failures) webhook event. The status of the subscription might change depending on your [subscription configuration](https://docs.stripe.com/billing/subscriptions/overview.md#subscription-statuses).

You have several options for handling these scenarios:

- You can update the mandate options with the new interval using the [Update Subscription](https://docs.stripe.com/api/subscriptions/update.md) API and create a [Customer Portal](https://docs.stripe.com/api/customer_portal/sessions/create.md) session for your customer to update their Pix payment method.
- You can update the mandate options with the new interval using the [Update Subscription](https://docs.stripe.com/api/subscriptions/update.md) API and create a [Checkout Session](https://docs.stripe.com/api/checkout/sessions/create.md) in `setup` mode (without an initial payment) or in `payment` mode with [payment_method_options.pix.setup_future_usage](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_method_options-pix-setup_future_usage)=`off_session` (with an initial payment) to create a new mandate with a new payment method, and [update the payment method of the subscription](https://docs.stripe.com/payments/checkout/subscriptions/update-payment-details.md#set-default-payment-method).
- You can cancel and re-create the subscription.

## Optional: Handle payment failures

If a recurring payment fails and the reason is not related to the pricing or the billing cycle change scenarios described above, Stripe retries the payment as described in the [Retries](https://docs.stripe.com/payments/pix/pix-automatico.md#retries) section.

If the payment fails after exhausting all of the retries, you can do one of the following:

- Create a one-time payment for your customer to pay the invoice for the subscription.
- Create a [Customer Portal](https://docs.stripe.com/api/customer_portal/sessions/create.md) session for your customer to pay the invoice or update their payment method.

## Optional: Handle add-on purchases after subscription creation

Due to scheme restrictions, you can only charge a Pix payment method once per cycle specified in [payment_method_options.pix.mandate_options.payment_schedule](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_method_options-pix-mandate_options-payment_schedule). If your users can buy add-ons after the subscription creation, you have the following options depending on your use case:

- If you don’t require an immediate payment and you only want to update the subscription for future payments, you can update the existing subscription using the [Update Subscription](https://docs.stripe.com/api/subscriptions/update.md) API. The restrictions mentioned in [Change the pricing of an existing subscription](https://docs.stripe.com/billing/subscriptions/pix.md#change-pricing-of-subscription) still apply. If the mandate restrictions mentioned in that section aren’t respected, your recurring payments might fail.
- If you require an immediate payment, you can create a one-time payment by creating a Checkout Session in `payment` mode and bringing your user back on-session. Separately, if you also want to update the subscription for future payments, you can use the [Update Subscription](https://docs.stripe.com/api/subscriptions/update.md) API.
