<!-- Source URL: https://docs.stripe.com/payments/twint/save-during-payment -->
<!-- Fetched: 2026-05-03 -->

# Save payment details during a TWINT payment

Learn how to save your customer’s payment details from a TWINT payment.

# Checkout

> This is a Checkout for when payment-ui is checkout. View the full page at https://docs.stripe.com/payments/twint/save-during-payment?payment-ui=checkout.

You can use [Stripe-hosted Checkout](https://docs.stripe.com/checkout/quickstart.md) to collect payment method details and charge the saved payment method immediately.

Alternatively, you can [set up future TWINT payments](https://docs.stripe.com/payments/twint/set-up-future-payments.md) to collect TWINT payment method details in advance, and determine the final amount or payment date later.

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create or retrieve a customer [Server-side]

To reuse a TWINT payment method for future payments, attach it to an object that represents your customer.

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

Your customer must authorize you to use their TWINT account for future payments through Stripe Checkout. This allows you to accept TWINT payments. Add a checkout button to your website that calls a server-side endpoint to create a [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md).

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

A Checkout Session is the programmatic representation of what your customer sees when they’re redirected to the payment form.

1. Create a Checkout Session in [payment mode](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-mode).
1. Add `twint` to the list of [payment_method_types](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_method_types).
1. List [line_items](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items) to charge. Make sure all `line_items` use the `chf` currency.
1. Specify the customer’s ID.
1. Configure [payment_intent_data.setup_future_usage](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_intent_data-setup_future_usage) to indicate that you want to set up the payment method for future usage.

After creating the Checkout Session, redirect your customer to the [URL](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-url) returned in the response.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  mode: "payment",
  payment_method_types: ["twint"],
  line_items: [
    {
      price_data: {
        currency: "chf",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 1099,
      },
      quantity: 1,
    },
  ],
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  payment_intent_data: {
    setup_future_usage: "off_session",
  },
  success_url: "https://example.com/success?session_id={CHECKOUT_SESSION_ID}",
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  mode: "payment",
  payment_method_types: ["twint"],
  line_items: [
    {
      price_data: {
        currency: "chf",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 1099,
      },
      quantity: 1,
    },
  ],
  customer: "{{CUSTOMER_ID}}",
  payment_intent_data: {
    setup_future_usage: "off_session",
  },
  success_url: "https://example.com/success?session_id={CHECKOUT_SESSION_ID}",
});
```

When your customer provides their payment method details, Stripe redirects them to the `success_url`, a page on your website that informs them that their payment was successful. Make the Session ID available on your success page by including the `{CHECKOUT_SESSION_ID}` template variable in the `success_url` as in the above example.

> Don’t rely on the redirect to the `success_url` alone for detecting payment initiation, because:
>
> - Malicious users could directly access the `success_url` without paying and gain access to your goods or services.

- After a successful payment, customers might close their browser tab before they’re redirected to the `success_url`.

## Retrieve the payment method [Server-side]

After a customer submits their payment details, retrieve the [PaymentMethod](https://docs.stripe.com/payments/payment-methods.md) object. A PaymentMethod stores customer TWINT account information for future payments. You can retrieve the PaymentMethod synchronously using the `success_url` or asynchronously using *webhooks* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests).

Determine whether to retrieve the *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) synchronously or asynchronously, based on your dropff tolerance. Customers might not always reach the `success_url` after a successful payment, for example, if they close their browser tab before the redirect occurs. You can use webhooks to prevent your integration from experiencing this type of dropoff.

#### Webhooks

Handle `checkout.session.completed` webhooks, which contain a Session object. Learn more about [setting up webhooks](https://docs.stripe.com/webhooks.md). The following example is a `checkout.session.completed` response.

```json
{
  "id": "evt_1Ep24XHssDVaQm2PpwS19Yt0",
  "object": "event",
  "api_version": "2019-03-14",
  "created": 1561420781,
  "data": {
    "object": {
      "id": "cs_test_MlZAaTXUMHjWZ7DcXjusJnDU4MxPalbtL5eYrmS2GKxqscDtpJq8QM0k",
      "object": "checkout.session",
      "billing_address_collection": null,
      "client_reference_id": null,
      "customer": null,
      "customer_email": null,
      "display_items": [],
      "mode": "payment",
      "payment_intent": "pi_3MtwBwLkdIwHu7ix28a3tqPa",
      "submit_type": null,
      "subscription": null,
      "success_url": "https://example.com/success"
    }
  },
  "livemode": false,
  "pending_webhooks": 1,
  "request": {
    "id": null,
    "idempotency_key": null
  },
  "type": "checkout.session.completed"
}
```

Note the value of the `payment_intent` key, which is the ID for the PaymentIntent created with the Checkout Session. A [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) is an object that represents your intent to collect a payment from a customer and tracks the payment process. [Retrieve](https://docs.stripe.com/api/payment_intents/retrieve.md) the PaymentIntent object with the ID. The returned object contains a `payment_method` ID that you can charge future payments with.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.retrieve(
  "pi_3MtwBwLkdIwHu7ix28a3tqPa",
);
```

#### Success URL

Obtain the `session_id` from the URL when a user redirects back to your site and [retrieve](https://docs.stripe.com/api/checkout/sessions/retrieve.md) the Session object.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.retrieve("{{SESSION_ID}}", {
  expand: ["payment_intent"],
});
```

Make sure the `session_id` is available from the URL by including the `session_id={CHECKOUT_SESSION_ID}` template variable in the `success_url` when creating the Checkout Session.

Note the PaymentIntent created during the Checkout Session. A [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) is an object that represents your intent to collect a payment from a customer and tracks the payment process. The returned object contains the `payment_method` ID.

## Monitor webhooks [Server-side]

Use a method such as [webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks) to confirm that the customer authorized the mandate. Don’t rely on your customer to return to the payment status page.

When a customer successfully authorizes the mandate, Stripe emits a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event and the PaymentIntent’s status transitions to `succeeded`. Store the resulting [payment_method](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-payment_method) ID to make payments using the saved payment method later.

If a customer doesn’t successfully authorize the mandate, Stripe emits a [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) webhook event and the PaymentIntent’s status updates to `requires_payment_method`.

## Charge a saved TWINT payment method [Server-side]

When you’re ready to charge your customer, use the customer’s ID and the *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) ID to create a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md).

To find a `twint` instrument to charge, [list](https://docs.stripe.com/api/payment_methods/list.md) the payment methods associated with your customer.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethods = await stripe.paymentMethods.list({
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  type: "twint",
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethods = await stripe.paymentMethods.list({
  customer: "{{CUSTOMER_ID}}",
  type: "twint",
});
```

When you have the customer and `PaymentMethod` IDs, create and confirm a `PaymentIntent` with the amount and currency of the payment. To charge your customer *off session* (A payment is described as off-session if it occurs without the direct involvement of the customer, using previously-collected payment information), set [off_session](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-off_session) to true. That indicates that the customer isn’t in your checkout flow during this payment attempt.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "chf",
  payment_method_types: ["twint"],
  payment_method: "{{PAYMENT_METHOD_ID}}",
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  off_session: true,
  confirm: true,
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "chf",
  payment_method_types: ["twint"],
  payment_method: "{{PAYMENT_METHOD_ID}}",
  customer: "{{CUSTOMER_ID}}",
  off_session: true,
  confirm: true,
});
```

> The `return_url` parameter isn’t required when using a TWINT payment method that was previously set up with a SetupIntent or a PaymentIntent with `setup_future_usage`. It’s required for all other cases.

## Test your integration

When testing your payment integration with your test API keys, select TWINT as the payment method and click **Pay**. If you successfully complete authorization on the redirect page, the PaymentIntent transitions from `requires_action` to `succeeded`. If you decline the authorization on this page, the PaymentIntent transitions from `requires_action` to `requires_payment_method`.

## See also

- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment.md)
- [Customize Checkout](https://docs.stripe.com/payments/checkout/customization.md)

# Elements

> This is a Elements for when payment-ui is elements. View the full page at https://docs.stripe.com/payments/twint/save-during-payment?payment-ui=elements.

You can use the [Payment Element](https://docs.stripe.com/payments/payment-element.md), a prebuilt UI component, to collect TWINT payment method details and charge the saved payment method immediately.

Alternatively, you can [set up future TWINT payments](https://docs.stripe.com/payments/twint/set-up-future-payments.md) to collect TWINT payment method details in advance, and determine the final amount or payment date later.

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create or retrieve a customer [Server-side]

To reuse a TWINT payment method for future payments, attach it to an object that represents your customer.

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

## Create a PaymentIntent [Server-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) is an object that represents your intent to collect a payment from a customer and tracks the payment process.

1. Create a `PaymentIntent` on your server with `twint` added to the list of [payment_method_types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types).
1. Specify the customer’s ID.
1. Configure [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) to indicate that you want to set up the payment method for future usage.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "chf",
  payment_method_types: ["twint"],
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  setup_future_usage: "off_session",
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "chf",
  payment_method_types: ["twint"],
  customer: "{{CUSTOMER_ID}}",
  setup_future_usage: "off_session",
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

## Collect payment method details and submit the payment [Client-side]

Collect payment details on the client with the [Payment Element](https://docs.stripe.com/payments/payment-element.md). The Payment Element is a prebuilt UI component that simplifies collecting payment details for a variety of payment methods.

The Payment Element contains an iframe that securely sends payment information to Stripe over an HTTPS connection. Avoid placing the Payment Element within another iframe because some payment methods require redirecting to another page for payment confirmation.

If you choose to use an iframe and want to accept Apple Pay or Google Pay, the iframe must have the [allow](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe#attr-allowpaymentrequest) attribute set to equal `"payment *"`.

The checkout page address must start with `https://` rather than `http://` for your integration to work. You can test your integration without using HTTPS, but remember to [enable it](https://docs.stripe.com/security/guide.md#tls) when you’re ready to accept live payments.

#### HTML + JS

### Set up Stripe.js

The Payment Element is automatically available as a feature of Stripe.js. Include the Stripe.js script on your checkout page by adding it to the `head` of your HTML file. Always load Stripe.js directly from js.stripe.com to remain PCI compliant. Don’t include the script in a bundle or host a copy of it yourself.

```html
<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/dahlia/stripe.js"></script>
</head>
```

Create an instance of Stripe with the following JavaScript on your checkout page:

```javascript
// Set your publishable key: remember to change this to your live publishable key in production
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");
```

### Add the Payment Element to your payment page

The Payment Element needs a place to live on your payment page. Create an empty DOM node (container) with a unique ID in your payment form:

```html
<form id="payment-form">
  <div id="payment-element">
    <!-- Elements will create form elements here -->
  </div>
  <button id="submit">Submit</button>
  <div id="error-message">
    <!-- Display error message to your customers here -->
  </div>
</form>
```

When the previous form loads, create an instance of the Payment Element and mount it to the container DOM node. Pass the [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) from the previous step into `options` when you create the [Elements](https://docs.stripe.com/js/elements_object/create) instance:

Handle the client secret carefully because it can complete the charge. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

```javascript
const options = {
  clientSecret: "{{CLIENT_SECRET}}",
  // Fully customizable with appearance API.
  appearance: {
    /*...*/
  },
};

// Set up Stripe.js and Elements to use in checkout form, passing the client secret obtained in a previous stepconst elements = stripe.elements(options);
// Optional: Autofill user's saved payment methods. If the customer's
// email is known when the page is loaded, you can pass the email
// to the linkAuthenticationElement on mount:
//
//   linkAuthenticationElement.mount("#link-authentication-element",  {
//     defaultValues: {
//       email: 'jenny.rosen@example.com',
//     }
//   })

// Create and mount the Payment Element
const paymentElementOptions = { layout: "accordion" };
const paymentElement = elements.create("payment", paymentElementOptions);
paymentElement.mount("#payment-element");
```

#### React

### Set up Stripe.js

Install [React Stripe.js](https://www.npmjs.com/package/@stripe/react-stripe-js) and the [Stripe.js loader](https://www.npmjs.com/package/@stripe/stripe-js) from the npm public registry:

```bash
npm install --save @stripe/react-stripe-js @stripe/stripe-js
```

### Add and configure the Elements provider to your payment page

To use the Payment Element component, wrap your checkout page component in an [Elements provider](https://docs.stripe.com/sdks/stripejs-react.md#elements-provider). Call `loadStripe` with your publishable key, and pass the returned `Promise` to the `Elements` provider. Also pass the [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) from the previous step as `options` to the `Elements` provider.

```jsx
import React from "react";
import ReactDOM from "react-dom";
import { Elements } from "@stripe/react-stripe-js";
import { loadStripe } from "@stripe/stripe-js";

import CheckoutForm from "./CheckoutForm";

// Make sure to call `loadStripe` outside of a component’s render to avoid
// recreating the `Stripe` object on every render.
const stripePromise = loadStripe("<<YOUR_PUBLISHABLE_KEY>>");

function App() {
  const options = {
    // passing the client secret obtained in step 3
    clientSecret: "{{CLIENT_SECRET}}",
    // Fully customizable with appearance API.
    appearance: {
      /*...*/
    },
  };

  return (
    <Elements stripe={stripePromise} options={options}>
      <CheckoutForm />
    </Elements>
  );
}

ReactDOM.render(<App />, document.getElementById("root"));
```

### Add the Payment Element component

Use the `PaymentElement` component to build your form:

```jsx
import React from 'react';
import {PaymentElement} from '@stripe/react-stripe-js';

const CheckoutForm = () => {
  return (
    <form>
      // Optional: Autofill user's saved payment methods. If the customer's
      // email is known when the page is loaded, you can pass the email
      // to the linkAuthenticationElement
      //
      // <LinkAuthenticationElement id="link-authentication-element"
        // Prefill the email field like so:
        // options={{defaultValues: {email: 'foo@bar.com'}}}
      // /><PaymentElement />
      <button>Submit</button>
    </form>
  );
};

export default CheckoutForm;
```

Use [stripe.confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment) to complete the payment using details from the Payment Element. This redirects the customer from your page to the TWINT-hosted payment page. Specify a [return_url](https://docs.stripe.com/js/payment_intents/confirm_payment#confirm_payment_intent-options-confirmParams-return_url) to indicate where Stripe can redirect the user after they complete the payment.

> `stripe.confirmPayment` might take time to complete while waiting for customers to complete the payment. During that time, you can disable your form from being resubmitted, and display a waiting indicator like a spinner. If you receive an error result, make sure to show the error to the customer, re-enable the form, and hide the waiting indicator.

#### HTML + JS

```javascript
const form = document.getElementById("payment-form");

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const { error, paymentIntent } = await stripe.confirmPayment({
    // `Elements` instance used to create the Payment Element
    elements,
    confirmParams: {
      return_url: "https://example.com/checkout/complete",
    },
  });

  const message = document.querySelector("#message");
  if (error) {
    // This point is reached only if there's an immediate error when
    // confirming the PaymentIntent. Show the error to your customer
    message.innerText = error.message;
  } else {
    // This executes if the confirm request is successful, or if the
    // payment fails asynchronously
    switch (paymentIntent.status) {
      case "succeeded":
        message.innerText = "Success! Payment received.";
        break;

      case "requires_payment_method":
        message.innerText =
          "Payment failed. Please try another payment method.";
        // Redirect your customer back to your payment page to attempt collecting
        // payment details again
        break;

      default:
        message.innerText = "Something went wrong.";
        break;
    }
  }
});
```

#### React

To call [stripe.confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment) from your payment form component, use the [useStripe](https://docs.stripe.com/sdks/stripejs-react.md#usestripe-hook) and [useElements](https://docs.stripe.com/sdks/stripejs-react.md#useelements-hook) hooks.

If you prefer using traditional class components instead of hooks, you can use an [ElementsConsumer](https://docs.stripe.com/sdks/stripejs-react.md#elements-consumer) instead.

```jsx
import React, { useState } from "react";
import {
  useStripe,
  useElements,
  PaymentElement,
} from "@stripe/react-stripe-js";

const CheckoutForm = () => {
  const stripe = useStripe();
  const elements = useElements();

  const [message, setMessage] = useState(null);

  const handleSubmit = async (event) => {
    // We don't want to let default form submission happen here,
    // which would refresh the page
    event.preventDefault();

    if (!stripe || !elements) {
      // Stripe.js hasn't yet loaded.
      // Make sure to disable form submission until Stripe.js has loaded
      return;
    }
    const { error, paymentIntent } = await stripe.confirmPayment({
      // `Elements` instance used to create the Payment Element
      elements,
      confirmParams: {
        return_url: "https://example.com/checkout/complete",
      },
    });

    if (error) {
      // This point is reached only if there's an immediate error when
      // confirming the PaymentIntent. Show the error to your customer
      setMessage(error.message);
    } else {
      // This executes if the confirm request is successful, or if the
      // payment fails asynchronously
      switch (paymentIntent.status) {
        case "succeeded":
          setMessage("Success! Payment received.");
          break;

        case "requires_payment_method":
          setMessage("Payment failed. Please try another payment method.");
          // Redirect your customer back to your payment page to attempt collecting
          // payment details again
          break;

        default:
          setMessage("Something went wrong.");
          break;
      }
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <PaymentElement />
      <button disabled={!stripe}>Submit</button>
      {/* Show message to your customers */}
      {message && <div>{message}</div>}
    </form>
  );
};

export default CheckoutForm;
```

## Monitor webhooks [Server-side]

Use a method such as [webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks) to confirm that the customer authorized the mandate. Don’t rely on your customer to return to the payment status page.

When a customer successfully authorizes the mandate, Stripe emits a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event and the PaymentIntent’s status transitions to `succeeded`. Store the resulting [payment_method](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-payment_method) ID to make payments using the saved payment method later.

If a customer doesn’t successfully authorize the mandate, Stripe emits a [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) webhook event and the PaymentIntent’s status updates to `requires_payment_method`.

## Charge a saved TWINT payment method [Server-side]

When you’re ready to charge your customer, use the customer’s ID and the *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) ID to create a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md).

To find a `twint` instrument to charge, [list](https://docs.stripe.com/api/payment_methods/list.md) the payment methods associated with your customer.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethods = await stripe.paymentMethods.list({
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  type: "twint",
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethods = await stripe.paymentMethods.list({
  customer: "{{CUSTOMER_ID}}",
  type: "twint",
});
```

When you have the customer and `PaymentMethod` IDs, create and confirm a `PaymentIntent` with the amount and currency of the payment. To charge your customer *off session* (A payment is described as off-session if it occurs without the direct involvement of the customer, using previously-collected payment information), set [off_session](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-off_session) to true. That indicates that the customer isn’t in your checkout flow during this payment attempt.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "chf",
  payment_method_types: ["twint"],
  payment_method: "{{PAYMENT_METHOD_ID}}",
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  off_session: true,
  confirm: true,
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "chf",
  payment_method_types: ["twint"],
  payment_method: "{{PAYMENT_METHOD_ID}}",
  customer: "{{CUSTOMER_ID}}",
  off_session: true,
  confirm: true,
});
```

> The `return_url` parameter isn’t required when using a TWINT payment method that was previously set up with a SetupIntent or a PaymentIntent with `setup_future_usage`. It’s required for all other cases.

## Test your integration

When testing your payment integration with your test API keys, select TWINT as the payment method and click **Pay**. If you successfully complete authorization on the redirect page, the PaymentIntent transitions from `requires_action` to `succeeded`. If you decline the authorization on this page, the PaymentIntent transitions from `requires_action` to `requires_payment_method`.

# Direct API

> This is a Direct API for when payment-ui is direct-api. View the full page at https://docs.stripe.com/payments/twint/save-during-payment?payment-ui=direct-api.

You can use the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md) with [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) to collect TWINT payment method details and charge the saved payment method immediately.

Alternatively, you can [set up future TWINT payments](https://docs.stripe.com/payments/twint/set-up-future-payments.md) to collect TWINT payment method details in advance, and determine the final amount or payment date later.

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create or retrieve a customer [Server-side]

To reuse a TWINT payment method for future payments, attach it to an object that represents your customer.

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

## Create a PaymentIntent [Server-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) is an object that represents your intent to collect a payment from a customer and tracks the payment process.

1. Create a PaymentIntent on your server with `twint` added to the list of [payment_method_types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types).
1. Specify the customer’s ID.
1. Configure [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) to indicate that you want to set up the payment method for future usage.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "chf",
  payment_method_types: ["twint"],
  payment_method_data: {
    type: "twint",
  },
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  setup_future_usage: "off_session",
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "chf",
  payment_method_types: ["twint"],
  payment_method_data: {
    type: "twint",
  },
  customer: "{{CUSTOMER_ID}}",
  setup_future_usage: "off_session",
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

## Collect payment method details and submit the payment [Client-side]

Use [Stripe.js](https://docs.stripe.com/js.md) to confirm the PaymentIntent. Stripe.js is our foundational JavaScript library for building payment flows. It automatically manages complexities, such as redirects, and allows you to integrate with other payment methods.

To include Stripe.js on your checkout page, add the script to the `head` section of your HTML file.

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

To confirm the setup on the client side, pass the client secret of the PaymentIntent. The client secret is different from your API keys that authenticate Stripe API requests. Handle it carefully because it can complete the setup. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

Use [stripe.confirmTwintPayment](https://docs.stripe.com/js/payment_intents/confirm_twint_payment) to handle the redirect from your page to the TWINT-hosted payment page. Specify a [return_url](https://docs.stripe.com/js/payment_intents/confirm_payment#confirm_payment_intent-options-confirmParams-return_url) to indicate where Stripe can redirect the user after they complete the payment.

> `stripe.confirmTwintPayment` might take time to complete while waiting for customers to complete the payment. During that time, you can disable your form from being resubmitted, and display a waiting indicator like a spinner. If you receive an error result, make sure to show the error to the customer, re-enable the form, and hide the waiting indicator.

```javascript
// Redirects away from the client
const { error, paymentIntent } = await stripe.confirmTwintPayment(
  "{{PAYMENT_INTENT_CLIENT_SECRET}}",
  {
    return_url: "https://example.com/checkout/complete",
  },
);

if (error) {
  // Inform the customer that there was an error
}
```

## Optional: Confirm and redirect manually [Server-side]

We recommend using [Stripe.js](https://docs.stripe.com/js.md) to handle TWINT redirects and authorizations on the client side. Using the native SDK allows you to extend your integration to other payment methods. Otherwise, you can manually redirect your customers on your server using the following steps:

1. *Confirm* (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) the PaymentIntent at creation time by including `confirm: true`.
1. Provide [mandate_data](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-mandate_data).
1. Use the [return_url](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-return_url) to indicate where Stripe can redirect the user after they complete the setup.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "chf",
  payment_method_types: ["twint"],
  payment_method_data: {
    type: "twint",
  },
  customer: "{{CUSTOMER_ID}}",
  setup_future_usage: "off_session",
  mandate_data: {
    customer_acceptance: {
      type: "online",
      online: {
        ip_address: "{{IP_ADDRESS}}",
        user_agent: "{{USER_AGENT}}",
      },
    },
  },
  return_url: "https://example.com/checkout/complete",
  confirm: true,
});
```

The PaymentIntent has a `requires_action` status and a `next_action` of `redirect_to_url` type. To authorize the use of their TWINT account for future payments, redirect the customer to the TWINT-hosted setup page provided in the `next_action.redirect_to_url.url` property. After the customer completes the process, Stripe redirects them back to the `return_url` you specify.

## Monitor webhooks [Server-side]

Use a method such as [webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks) to confirm that the customer authorized the mandate. Don’t rely on your customer to return to the payment status page.

When a customer successfully authorizes the mandate, Stripe emits a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event and the PaymentIntent’s status transitions to `succeeded`. Store the resulting [payment_method](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-payment_method) ID to make payments using the saved payment method later.

If a customer doesn’t successfully authorize the mandate, Stripe emits a [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) webhook event and the PaymentIntent’s status updates to `requires_payment_method`.

## Charge a saved TWINT payment method [Server-side]

When you’re ready to charge your customer, use the customer’s ID and the *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) ID to create a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md).

To find a `twint` instrument to charge, [list](https://docs.stripe.com/api/payment_methods/list.md) the payment methods associated with your customer.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethods = await stripe.paymentMethods.list({
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  type: "twint",
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethods = await stripe.paymentMethods.list({
  customer: "{{CUSTOMER_ID}}",
  type: "twint",
});
```

When you have the customer and `PaymentMethod` IDs, create and confirm a `PaymentIntent` with the amount and currency of the payment. To charge your customer *off session* (A payment is described as off-session if it occurs without the direct involvement of the customer, using previously-collected payment information), set [off_session](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-off_session) to true. That indicates that the customer isn’t in your checkout flow during this payment attempt.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "chf",
  payment_method_types: ["twint"],
  payment_method: "{{PAYMENT_METHOD_ID}}",
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  off_session: true,
  confirm: true,
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "chf",
  payment_method_types: ["twint"],
  payment_method: "{{PAYMENT_METHOD_ID}}",
  customer: "{{CUSTOMER_ID}}",
  off_session: true,
  confirm: true,
});
```

> The `return_url` parameter isn’t required when using a TWINT payment method that was previously set up with a SetupIntent or a PaymentIntent with `setup_future_usage`. It’s required for all other cases.

## Test your integration

Test your TWINT integration with your test API keys by viewing the PaymentIntent’s redirect page. If you successfully complete authorization on this page, the PaymentIntent transitions from `requires_action` to `succeeded`. If you decline the authorization on this page, the PaymentIntent transitions from `requires_action` to `requires_payment_method`.

To reproduce common live mode payment scenarios when charging a saved TWINT payment method, set [payment_method_data.billing_details.email](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-payment_method_data-billing_details-email) to the following values when you confirm the initial PaymentIntent. If you don’t specify `payment_method_data.billing_details.email`, or if the specified email doesn’t match any of the following values, the payment succeeds by default and the [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) webhook arrives within several seconds.

| Email                              | Description                                                                                                                                                                                                                                                                                                                                        |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `{any_prefix}decline@{any_domain}` | Simulates a TWINT payment with a mandate that fails because of a generic decline. The [payment_intent.failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.failed) webhook arrives within several seconds. Stripe returns the `payment_method_provider_decline` error code and a `partner_generic_decline` decline code. |

Example: decline@example.com |
| `{any_prefix}revoke@{any_domain}` | Simulates a TWINT payment with a mandate that fails because of a mandate revocation. The [payment_intent.failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.failed) webhook arrives within several seconds. Stripe returns the `payment_intent_mandate_revoked` error code and a `partner_generic_decline` decline code.

Example: revoke@example.com |
