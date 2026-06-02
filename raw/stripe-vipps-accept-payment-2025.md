<!-- Source URL: https://docs.stripe.com/payments/vipps/accept-a-payment -->
<!-- Fetched: 2026-05-08 -->

# Vipps payments

Learn how to accept Vipps, a common payment method in Norway.

# Checkout

> This is a Checkout for when payment-ui is checkout. View the full page at https://docs.stripe.com/payments/vipps/accept-a-payment?payment-ui=checkout.

Vipps is a [single-use](https://docs.stripe.com/payments/payment-methods.md#usage) card wallet payment method used in Norway. It allows your customer to [authenticate and approve](https://docs.stripe.com/payments/payment-methods.md#customer-actions) payments using the Vipps app.

When your customer pays with Vipps, Stripe performs a card transaction using the card data we receive from Vipps. The processing of the card transaction is invisible to your integration, and Stripe [immediately notifies you](https://docs.stripe.com/payments/payment-methods.md#payment-notification) whether the payment succeeded or failed.

> Stripe can automatically present the relevant payment methods to your customers by evaluating currency, payment method restrictions, and other parameters.
>
> - Follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=checkout&ui=stripe-hosted) guide to build a Checkout integration that uses [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md).

- If you don’t want to use dynamic payment methods, follow the steps below to manually configure the payment methods in your Checkout integration.

Use this guide to enable Vipps on [Checkout](https://docs.stripe.com/payments/checkout.md), our hosted checkout form, and learn the differences between accepting payments using dynamic payment methods and manually configuring payment methods.

## Determine compatibility

**Supported business locations**: EEA, GB

**Supported currencies**: `nok`

**Presentment currencies**: `nok`

**Payment mode**: Yes

**Setup mode**: No

**Subscription mode**: No

A Checkout Session must satisfy all of the following conditions to support Vipps payments:

- _Prices_ (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) for all line items must be expressed in Norwegian Krona (currency code `NOK`).

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries to access the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Accept a payment

> This guide builds on the foundational [accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?integration=checkout) Checkout integration.

### Enable Vipps as a payment method

When creating a new [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md), you need to:

1. Provide the `vipps_preview=v1` preview header with your [API version](https://docs.stripe.com/sdks/set-version.md) on requests.
1. Add `vipps` to the list of `payment_method_types`.
1. Make sure all your `line_items` use the `nok` currency.

#### Stripe-hosted page

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>", {
  // @ts-ignore overrides the pinned API version
  apiVersion: "2026-04-22.preview; vipps_preview=v1",
});

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        currency: "nok",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "vipps"],
  success_url: "https://example.com/success",
});
```

#### Full embedded page

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>", {
  // @ts-ignore overrides the pinned API version
  apiVersion: "2026-04-22.preview; vipps_preview=v1",
});

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        currency: "nok",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "vipps"],
  return_url: "https://example.com/return",
  ui_mode: "embedded_page",
});
```

### Fulfill your orders

After accepting a payment, learn how to [fulfill orders](https://docs.stripe.com/checkout/fulfillment.md).

## Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

- **Handle events manually in the Dashboard**

  Use the Dashboard to [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments), send email receipts, handle payouts, or retry failed payments.

- **Build a custom webhook**

  [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook) handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- **Integrate a prebuilt app**

  Handle common business events, such as [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

## Test the integration

To test your integration in a testing environment, it redirects you to a test payment page where you can approve or decline the test payment.

In live mode, enter the phone number linked to Vipps to send a push notification to your Vipps mobile application. You can approve or decline the payment in the Vipps mobile application.

## Authorize a payment and then capture later

Vipps supports [separate authorization and capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md) with a 7-day hold period. Stripe cancels the PaymentIntent and sends a [payment_intent.canceled](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.canceled) event if the payment isn’t captured during the 7-day window.

### Tell Stripe to authorize only

To indicate that you want separate authorization and capture, set [capture_method](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_intent_data-capture_method) to `manual` when creating the Checkout Session. This parameter instructs Stripe to only authorize the amount on the customer’s card linked to Vipps.

#### Stripe-hosted page

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>", {
  // @ts-ignore overrides the pinned API version
  apiVersion: "2026-04-22.preview; vipps_preview=v1",
});

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        currency: "nok",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_intent_data: {
    capture_method: "manual",
  },
  payment_method_types: ["card", "vipps"],
  success_url: "https://example.com/success.html",
});
```

#### Full embedded page

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>", {
  // @ts-ignore overrides the pinned API version
  apiVersion: "2026-04-22.preview; vipps_preview=v1",
});

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        currency: "nok",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_intent_data: {
    capture_method: "manual",
  },
  payment_method_types: ["card", "vipps"],
  return_url: "https://example.com/return",
  ui_mode: "embedded_page",
});
```

After the authorization is successful, Stripe sends a [payment_intent.amount_capturable_updated](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.amount_capturable_updated) event. See [Events](https://docs.stripe.com/api/events.md) to learn more.

### Capture the funds

After the authorization succeeds, the PaymentIntent’s [status](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-status) transitions to `requires_capture` and you can [capture](https://docs.stripe.com/api/payment_intents/capture.md) the authorized funds. Stripe only support manual captures of the full amount.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.capture(
  "{{PAYMENTINTENT_ID}}",
  {
    amount_to_capture: 2000,
  },
);
```

## Optional: Cancellation

You can cancel Vipps payments before they expire by [canceling the PaymentIntent](https://docs.stripe.com/api/payment_intents/cancel.md) associated with the Vipps payment.

## Failed payments

Vipps transactions can fail if the underlying card transaction is declined. Learn more about [card declines](https://docs.stripe.com/declines/card.md). In this case, the PaymentMethod detaches and the PaymentIntent’s status automatically transitions to `requires_payment_method`.

When the PaymentIntent’s status is `requires_action`, your customer must authenticate the payment within 5 minutes. If no action is taken after 5 minutes, the PaymentMethod detaches and the PaymentIntent’s status automatically transitions to `requires_payment_method`.

## Refunds and disputes

Stripe performs a card transaction using standard card rails as part of a Vipps transaction. [Refunds](https://docs.stripe.com/refunds.md) and [disputes](https://docs.stripe.com/disputes/how-disputes-work.md) are subject to the Visa and Mastercard network rules.

## See also

- [More about Vipps](https://docs.stripe.com/payments/vipps.md)
- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment.md)
- [Customize Checkout](https://docs.stripe.com/payments/checkout/customization.md)

# Elements

> This is a Elements for when payment-ui is elements. View the full page at https://docs.stripe.com/payments/vipps/accept-a-payment?payment-ui=elements.

Vipps is a [single-use](https://docs.stripe.com/payments/payment-methods.md#usage) card wallet payment method used in Norway. It allows your customer to [authenticate and approve](https://docs.stripe.com/payments/payment-methods.md#customer-actions) payments using the Vipps app.

When your customer pays with Vipps, Stripe performs a card transaction using the card data we receive from Vipps. The processing of the card transaction is invisible to your integration, and Stripe [immediately notifies you](https://docs.stripe.com/payments/payment-methods.md#payment-notification) whether the payment succeeded or failed.

This guide shows you how to embed a custom Stripe payment form in your website or application using the [Payment Element](https://docs.stripe.com/payments/payment-element.md). The Payment Element allows you to support Vipps and other payment methods automatically. For advanced configurations and customizations, refer to the [Accept a Payment](https://docs.stripe.com/payments/accept-a-payment.md) integration guide.

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create a PaymentIntent [Server-side]

Stripe uses a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) object to represent your intent to collect payment from a customer, tracking charge attempts and payment state changes throughout the process.

Manually specify payment methods by listing them using the `payment_method_types` attribute.

Create a PaymentIntent on your server with an amount, currency, and a list of payment methods. Always decide how much to charge on the server side, a trusted environment, as opposed to the client. This prevents malicious customers from being able to choose their own prices.

To enable Vipps payments when creating a PaymentIntent, you need to include the `vipps_preview=v1` preview header in your API requests.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>", {
  // @ts-ignore overrides the pinned API version
  apiVersion: "2026-04-22.preview; vipps_preview=v1",
});

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: "nok",
  payment_method_types: ["vipps"],
});
```

### Retrieve the client secret

The PaymentIntent includes a _client secret_ (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)) that the client side uses to securely complete the payment process. You can use different approaches to pass the client secret to the client side.

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

## Collect payment details [Client-side]

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
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>", {
  betas: "vipps_pm_beta_1",
  apiVersion: (vipps_preview = v1),
});
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
const stripePromise = loadStripe("<<YOUR_PUBLISHABLE_KEY>>", {
  betas: "vipps_pm_beta_1",
  apiVersion: (vipps_preview = v1),
});

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

## Submit the payment to Stripe [Client-side]

Use [stripe.confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment) to complete the payment using details from the Payment Element. Provide a [return_url](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-return_url) to this function to indicate where Stripe should redirect the user after they complete the payment. Your user may be first redirected to an intermediate site, like a bank authorization page, before being redirected to the `return_url`. Card payments immediately redirect to the `return_url` when a payment is successful.

#### HTML + JS

```javascript
const form = document.getElementById("payment-form");

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const { error } = await stripe.confirmPayment({
    //`Elements` instance that was used to create the Payment Element
    elements,
    confirmParams: {
      return_url: "https://example.com/order/123/complete",
    },
  });

  if (error) {
    // This point will only be reached if there is an immediate error when
    // confirming the payment. Show error to your customer (for example, payment
    // details incomplete)
    const messageContainer = document.querySelector("#error-message");
    messageContainer.textContent = error.message;
  } else {
    // Your customer will be redirected to your `return_url`. For some payment
    // methods like iDEAL, your customer will be redirected to an intermediate
    // site first to authorize the payment, then redirected to the `return_url`.
  }
});
```

#### React

To call [stripe.confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment) from your payment form component, use the [useStripe](https://docs.stripe.com/sdks/stripejs-react.md#usestripe-hook) and [useElements](https://docs.stripe.com/sdks/stripejs-react.md#useelements-hook) hooks.

If you prefer traditional class components over hooks, you can instead use an [ElementsConsumer](https://docs.stripe.com/sdks/stripejs-react.md#elements-consumer).

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

  const [errorMessage, setErrorMessage] = useState(null);

  const handleSubmit = async (event) => {
    // We don't want to let default form submission happen here,
    // which would refresh the page.
    event.preventDefault();

    if (!stripe || !elements) {
      // Stripe.js hasn't yet loaded.
      // Make sure to disable form submission until Stripe.js has loaded.
      return;
    }
    const { error } = await stripe.confirmPayment({
      //`Elements` instance that was used to create the Payment Element
      elements,
      confirmParams: {
        return_url: "https://example.com/order/123/complete",
      },
    });

    if (error) {
      // This point will only be reached if there is an immediate error when
      // confirming the payment. Show error to your customer (for example, payment
      // details incomplete)
      setErrorMessage(error.message);
    } else {
      // Your customer will be redirected to your `return_url`. For some payment
      // methods like iDEAL, your customer will be redirected to an intermediate
      // site first to authorize the payment, then redirected to the `return_url`.
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <PaymentElement />
      <button disabled={!stripe}>Submit</button>
      {/* Show error message to your customers */}
      {errorMessage && <div>{errorMessage}</div>}
    </form>
  );
};

export default CheckoutForm;
```

Make sure the `return_url` corresponds to a page on your website that provides the status of the payment. When Stripe redirects the customer to the `return_url`, we provide the following URL query parameters:

| Parameter                      | Description                                                                                                                                   |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_intent`               | The unique identifier for the `PaymentIntent`.                                                                                                |
| `payment_intent_client_secret` | The [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) of the `PaymentIntent` object. |

> If you have tooling that tracks the customer’s browser session, you might need to add the `stripe.com` domain to the referrer exclude list. Redirects cause some tools to create new sessions, which prevents you from tracking the complete session.

Use one of the query parameters to retrieve the PaymentIntent. Inspect the [status of the PaymentIntent](https://docs.stripe.com/payments/paymentintents/lifecycle.md) to decide what to show your customers. You can also append your own query parameters when providing the `return_url`, which persist through the redirect process.

#### HTML + JS

```javascript
// Initialize Stripe.js using your publishable key
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");

// Retrieve the "payment_intent_client_secret" query parameter appended to
// your return_url by Stripe.js
const clientSecret = new URLSearchParams(window.location.search).get(
  "payment_intent_client_secret",
);

// Retrieve the PaymentIntent
stripe.retrievePaymentIntent(clientSecret).then(({ paymentIntent }) => {
  const message = document.querySelector("#message");

  // Inspect the PaymentIntent `status` to indicate the status of the payment
  // to your customer.
  //
  // Some payment methods will [immediately succeed or fail][0] upon
  // confirmation, while others will first enter a `processing` state.
  //
  // [0]: https://stripe.com/docs/payments/payment-methods#payment-notification
  switch (paymentIntent.status) {
    case "succeeded":
      message.innerText = "Success! Payment received.";
      break;

    case "processing":
      message.innerText =
        "Payment processing. We'll update you when payment is received.";
      break;

    case "requires_payment_method":
      message.innerText = "Payment failed. Please try another payment method.";
      // Redirect your user back to your payment page to attempt collecting
      // payment again
      break;

    default:
      message.innerText = "Something went wrong.";
      break;
  }
});
```

#### React

```jsx
import React, { useState, useEffect } from "react";
import { useStripe } from "@stripe/react-stripe-js";

const PaymentStatus = () => {
  const stripe = useStripe();
  const [message, setMessage] = useState(null);

  useEffect(() => {
    if (!stripe) {
      return;
    }

    // Retrieve the "payment_intent_client_secret" query parameter appended to
    // your return_url by Stripe.js
    const clientSecret = new URLSearchParams(window.location.search).get(
      "payment_intent_client_secret",
    );

    // Retrieve the PaymentIntent
    stripe.retrievePaymentIntent(clientSecret).then(({ paymentIntent }) => {
      // Inspect the PaymentIntent `status` to indicate the status of the payment
      // to your customer.
      //
      // Some payment methods will [immediately succeed or fail][0] upon
      // confirmation, while others will first enter a `processing` state.
      //
      // [0]: https://stripe.com/docs/payments/payment-methods#payment-notification
      switch (paymentIntent.status) {
        case "succeeded":
          setMessage("Success! Payment received.");
          break;

        case "processing":
          setMessage(
            "Payment processing. We'll update you when payment is received.",
          );
          break;

        case "requires_payment_method":
          // Redirect your user back to your payment page to attempt collecting
          // payment again
          setMessage("Payment failed. Please try another payment method.");
          break;

        default:
          setMessage("Something went wrong.");
          break;
      }
    });
  }, [stripe]);

  return message;
};

export default PaymentStatus;
```

## Redirect and authenticate transactions

Customers can authenticate Vipps transactions with mobile or desktop apps. The client that the customer uses determines the authentication method after calling `confirmPayment`.

#### Mobile app authentication

After you call `confirmPayment`, Stripe redirects your customers to Vipps to approve or decline the payment. After your customers authorize the payment, the page redirects them to the Payment Intent’s `return_url`. Stripe adds `payment_intent`, `payment_intent_client_secret`, `redirect_pm_type`, and `redirect_status` as URL query parameters (along with any existing query parameters in the `return_url`).

An authentication session expires after 5 minutes, and the PaymentIntent’s status transitions back to `require_payment_method`. After the status transitions, your customer sees a payment error and must restart the payment process.

#### Desktop web app authentication

After you call `confirmPayment`, Stripe redirects your customers to a Vipps-hosted page where they can input the phone number associated with their Vipps account. This sends a push notification to their Vipps app for payment authentication. After your customer successfully authenticates the payment, the page redirects them back to the `return_url`. If you prefer not to redirect customers on the web after payment, pass `redirect: if_required` to the Payment Element.

An authentication session expires after 5 minutes, and the PaymentIntent’s status transitions back to `require_payment_method`. After the status transitions, your customer sees a payment error and must restart the payment process.

## Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

- **Handle events manually in the Dashboard**

  Use the Dashboard to [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments), send email receipts, handle payouts, or retry failed payments.

- **Build a custom webhook**

  [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook) handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- **Integrate a prebuilt app**

  Handle common business events, such as [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

## Test the integration

#### Mobile web app testing

To test your integration, choose Vipps as the payment method and tap **Pay**. In a testing environment, it redirects you to a test payment page where you can approve or decline the payment.

In live mode, tapping **Pay** redirects you to the Vipps mobile application, where you can approve or decline the payment.

#### Desktop web app testing

To test your integration in a testing environment, it redirects you to a test payment page where you can approve or decline the test payment.

In live mode, enter the phone number linked to Vipps to send a push notification to your Vipps mobile application. You can approve or decline the payment in the Vipps mobile application.

## Optional: Authorize a payment and then capture later

Vipps supports [separate authorization and capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md) with a 7-day hold period. Stripe cancels the PaymentIntent and sends a [payment_intent.canceled](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.canceled) event if the payment isn’t captured during the 7-day window.

### Tell Stripe to authorize only

To indicate that you want separate authorization and capture, set [capture_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-capture_method) to `manual` when creating the PaymentIntent. This parameter instructs Stripe to only authorize the amount on the customer’s card linked to Vipps.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>", {
  // @ts-ignore overrides the pinned API version
  apiVersion: "2026-04-22.preview; vipps_preview=v1",
});

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "dkk",
  capture_method: "manual",
  payment_method_types: ["vipps"],
  payment_method_data: {
    type: "vipps",
  },
});
```

After the authorization is successful, Stripe sends a [payment_intent.amount_capturable_updated](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.amount_capturable_updated) event. See [Events](https://docs.stripe.com/api/events.md) to learn more.

### Capture the funds

After the authorization succeeds, the PaymentIntent’s [status](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-status) transitions to `requires_capture` and you can [capture](https://docs.stripe.com/api/payment_intents/capture.md) the authorized funds. Stripe only support manual captures of the full amount.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>", {
  // @ts-ignore overrides the pinned API version
  apiVersion: "2026-04-22.preview; vipps_preview=v1",
});

const paymentIntent = await stripe.paymentIntents.capture(
  "{{PAYMENTINTENT_ID}}",
  {
    amount_to_capture: 1099,
  },
);
```

## Optional: Cancellation

You can cancel Vipps payments before they expire by [canceling the PaymentIntent](https://docs.stripe.com/api/payment_intents/cancel.md) associated with the Vipps payment.

## Failed payments

Vipps transactions can fail if the underlying card transaction is declined. Learn more about [card declines](https://docs.stripe.com/declines/card.md). In this case, the PaymentMethod detaches and the PaymentIntent’s status automatically transitions to `requires_payment_method`.

When the PaymentIntent’s status is `requires_action`, your customer must authenticate the payment within 5 minutes. If no action is taken after 5 minutes, the PaymentMethod detaches and the PaymentIntent’s status automatically transitions to `requires_payment_method`.

## Refunds and disputes

Stripe performs a card transaction using standard card rails as part of a Vipps transaction. [Refunds](https://docs.stripe.com/refunds.md) and [disputes](https://docs.stripe.com/disputes/how-disputes-work.md) are subject to the Visa and Mastercard network rules.

# Direct API

> This is a Direct API for when payment-ui is direct-api. View the full page at https://docs.stripe.com/payments/vipps/accept-a-payment?payment-ui=direct-api.

Vipps is a [single-use](https://docs.stripe.com/payments/payment-methods.md#usage) card wallet payment method used in Norway. It allows your customer to [authenticate and approve](https://docs.stripe.com/payments/payment-methods.md#customer-actions) payments using the Vipps app.

When your customer pays with Vipps, Stripe performs a card transaction using the card data we receive from Vipps. The processing of the card transaction is invisible to your integration, and Stripe [immediately notifies you](https://docs.stripe.com/payments/payment-methods.md#payment-notification) whether the payment succeeded or failed.

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries to access the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create a PaymentIntent [Server-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) is an object that represents your intent to collect a payment from a customer and tracks the lifecycle of the payment process through each stage. Create a `PaymentIntent` on your server and specify the amount to collect and a supported currency (`nok`). If you already have an integration using the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md), add `vipps` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types). Make sure you include the `vipps_preview=v1` header in your API requests to enable Vipps.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>", {
  // @ts-ignore overrides the pinned API version
  apiVersion: "2026-04-22.preview; vipps_preview=v1",
});

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "nok",
  payment_method_types: ["vipps"],
  payment_method_data: {
    type: "vipps",
  },
});
```

### Example response

```json
{
  "id": "pi_12345",
  "amount": 1099,
  "client_secret": "pi_12345_secret_abcdef",
  "currency": "nok",
  "payment_method": "pm_12345",
  "payment_method_types": ["vipps"],
  "status": "requires_confirmation"
}
```

### Retrieve the client secret

The PaymentIntent includes a _client secret_ (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)) that the client side uses to securely complete the payment process. You can use different approaches to pass the client secret to the client side.

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

## Confirm the PaymentIntent

Use the PaymentIntent [ID](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-id) from [step 2](https://docs.stripe.com/payments/vipps/accept-a-payment.md#create-payment-intent) to _confirm_ (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) the PaymentIntent. This declares that the customer intends to pay with the specified _PaymentMethod_ (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs). Stripe initiates a payment after confirming the PaymentIntent. The [return_url](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-return_url) indicates where Stripe redirects the customer after they complete the payment.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.confirm(
  "{{PAYMENTINTENT_ID}}",
  {
    return_url: "https://example.com/checkout/complete",
  },
);
```

### Example response

```json
{
  "id": "pi_12345",
  "amount": 1099,
  "currency": "nok",
  "payment_method": "pm_12345",
  "next_action": {
    "redirect_to_url": {
      "return_url": "https://example.com/checkout/complete",
      "url": "https://pm-redirects.stripe.com/authorize/acct_123/pa_nonce_abc"
    },
    "type": "redirect_to_url"
  },
  "payment_method_types": ["vipps"],
  "status": "requires_action"
}
```

To authorize the payment, redirect your customer to the URL in the [next_action[redirect_to_url][url]](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-redirect_to_url-url) field.

- On desktop, the URL opens a Vipps landing page where the customer can enter their phone number, which identifies their Vipps account. They can then use the Vipps smartphone app to proceed with payment authorization.
- On mobile devices, the URL opens the Vipps application directly (if present) or directs to the Vipps landing page, similar to the desktop process.

Your customer has 5 minutes to open the redirect URL and authorize the payment in the Vipps app. If the underlying card charge fails, your customer can choose a different card and retry in the Vipps app. If the payment isn’t authorized within 5 minutes, the payment fails and the PaymentIntent’s status transitions to `requires_payment_method`.

## Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

- **Handle events manually in the Dashboard**

  Use the Dashboard to [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments), send email receipts, handle payouts, or retry failed payments.

- **Build a custom webhook**

  [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook) handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- **Integrate a prebuilt app**

  Handle common business events, such as [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

## Test the integration

Using your [test API keys](https://docs.stripe.com/keys.md#test-live-modes), create a PaymentIntent. After confirming the PaymentIntent, follow the `next_action` redirect URL to a test page with options to authorize or fail the payment.

- Click **Authorize test payment** to test the case when the payment is successful. The PaymentIntent transitions from `requires_action` to `succeeded`.
- Click **Fail test payment** to test the case when the customer fails to authenticate. The PaymentIntent transitions from `requires_action` to `requires_payment_method`.

## Optional: Authorize a payment and then capture later

Vipps supports [separate authorization and capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md) with a 7-day hold period. Stripe cancels the PaymentIntent and sends a [payment_intent.canceled](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.canceled) event if the payment isn’t captured during the 7-day window.

### Tell Stripe to authorize only

To indicate that you want separate authorization and capture, set [capture_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-capture_method) to `manual` when creating the PaymentIntent. This parameter instructs Stripe to only authorize the amount on the customer’s card linked to Vipps.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>", {
  // @ts-ignore overrides the pinned API version
  apiVersion: "2026-04-22.preview; vipps_preview=v1",
});

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "dkk",
  capture_method: "manual",
  payment_method_types: ["vipps"],
  payment_method_data: {
    type: "vipps",
  },
});
```

After the authorization is successful, Stripe sends a [payment_intent.amount_capturable_updated](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.amount_capturable_updated) event. See [Events](https://docs.stripe.com/api/events.md) to learn more.

### Capture the funds

After the authorization succeeds, the PaymentIntent’s [status](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-status) transitions to `requires_capture` and you can [capture](https://docs.stripe.com/api/payment_intents/capture.md) the authorized funds. Stripe only support manual captures of the full amount.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>", {
  // @ts-ignore overrides the pinned API version
  apiVersion: "2026-04-22.preview; vipps_preview=v1",
});

const paymentIntent = await stripe.paymentIntents.capture(
  "{{PAYMENTINTENT_ID}}",
  {
    amount_to_capture: 1099,
  },
);
```

## Optional: Cancellation

You can cancel Vipps payments before they expire by [canceling the PaymentIntent](https://docs.stripe.com/api/payment_intents/cancel.md) associated with the Vipps payment.

## Failed payments

Vipps transactions can fail if the underlying card transaction is declined. Learn more about [card declines](https://docs.stripe.com/declines/card.md). In this case, the PaymentMethod detaches and the PaymentIntent’s status automatically transitions to `requires_payment_method`.

When the PaymentIntent’s status is `requires_action`, your customer must authenticate the payment within 5 minutes. If no action is taken after 5 minutes, the PaymentMethod detaches and the PaymentIntent’s status automatically transitions to `requires_payment_method`.

## Refunds and disputes

Stripe performs a card transaction using standard card rails as part of a Vipps transaction. [Refunds](https://docs.stripe.com/refunds.md) and [disputes](https://docs.stripe.com/disputes/how-disputes-work.md) are subject to the Visa and Mastercard network rules.
