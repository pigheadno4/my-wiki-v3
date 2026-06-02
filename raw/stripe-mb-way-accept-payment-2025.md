<!-- Source URL: https://docs.stripe.com/payments/mb-way/accept-a-payment -->
<!-- Fetched: 2026-05-07 -->

# MB WAY payments

Learn how to accept the MB WAY payment method.

MB WAY is a digital wallet payment method in Portugal. When paying with MB WAY, customers initiate payments using their phone number, and [authenticate and approve](https://docs.stripe.com/payments/payment-methods.md#customer-actions) them using their MB WAY app.

You get [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) of whether the payment succeeded or failed.

> MB WAY supports international phone numbers, but the majority of customers use a Portuguese phone number starting with +351. You can test your integration in a *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes) using [test phone numbers](https://docs.stripe.com/payments/mb-way/accept-a-payment.md#web-test-integration).

# Checkout

> This is a Checkout for when payment-ui is checkout. View the full page at https://docs.stripe.com/payments/mb-way/accept-a-payment?payment-ui=checkout.

> Stripe can automatically present the relevant payment methods to your customers by evaluating currency, payment method restrictions, and other parameters.
>
> - Follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=checkout&ui=stripe-hosted) guide to build a Checkout integration that uses [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md).

- If you don’t want to use dynamic payment methods, follow the steps below to manually configure the payment methods in your Checkout integration.

## Determine compatibility

**Supported business locations**: Europe, US, CA, NZ, SG, HK, JP, AU, MX

**Supported currencies**: `eur`

**Presentment currencies**: `eur`

**Payment mode**: Yes

**Setup mode**: No

**Subscription mode**: No

A Checkout Session must satisfy all of the following conditions to support MB WAY:

- You must express *Prices* (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) for all line items in Euros (currency code `eur`).

## Accept a MB WAY payment

> Build an integration to [accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?integration=checkout) with Checkout before using this guide.

Enable MB WAY by making the following updates to your integration.

When creating a [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md), you must:

- Add `mb_way` to the list of `payment_method_types`.
- Make sure all `line_items` use the `eur` currency.

#### Stripe-hosted page

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        currency: "eur",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "mb_way"],
  success_url: "https://example.com/success",
});
```

#### Full embedded page

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        currency: "eur",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "mb_way"],
  return_url: "https://example.com/return",
  ui_mode: "embedded_page",
});
```

### Fulfill your orders

After accepting a payment, learn how to [fulfill orders](https://docs.stripe.com/checkout/fulfillment.md).

## Handle refunds

Learn more about [MB WAY refunds](https://docs.stripe.com/payments/mb-way.md#refunds).

## Test your integration

Test your MB WAY integration by using the following test phone numbers. Each set of details reproduces a common live mode scenario.

| Phone number           | Description                                                                                                                                                                   |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `+351911111112`        | The PaymentIntent status transitions from `requires_action` to `succeeded` after approximately 30 seconds.                                                                    |
| `+351911111113`        | The PaymentIntent status transitions from `requires_action` to `requires_payment_method` immediately. Stripe returns the `payment_method_not_available` error code.           |
| `+351911111114`        | The PaymentIntent status transitions from `requires_action` to `requires_payment_method` immediately. Stripe returns the `payment_method_provider_decline` error code.        |
| `+351911111115`        | The PaymentIntent status transitions from `requires_action` to `requires_payment_method` immediately. Stripe returns the `payment_intent_payment_attempt_expired` error code. |
| `+351911111116`        | The PaymentIntent status transitions from `requires_action` to `requires_payment_method` immediately. Stripe returns the `payment_method_customer_decline` error code.        |
| Any other phone number | The PaymentIntent status immediately transitions from `requires_action` to `succeeded`.                                                                                       |

## See also

- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment.md)
- [Customizing checkout](https://docs.stripe.com/payments/checkout/customization.md)

# Elements

> This is a Elements for when payment-ui is elements. View the full page at https://docs.stripe.com/payments/mb-way/accept-a-payment?payment-ui=elements.

## Set up Stripe [Server-side]

First, [create a Stripe account](https://dashboard.stripe.com/register) or [sign in](https://dashboard.stripe.com/login).

Use our official libraries to access the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create a PaymentIntent [Server-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) is an object that represents your intent to collect a payment from a customer and tracks the payment process. To create a `PaymentIntent` that accepts a MB WAY payment method, specify the amount to collect, `eur` as the currency, and `mb_way` in the [payment_method_types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) list. If you maintain a list of payment method types that you pass when creating a `PaymentIntent`, add `mb_way` to it.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: "eur",
  payment_method_types: ["mb_way"],
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
  betas: "mb_way_pm_beta_1",
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
  betas: "mb_way_pm_beta_1",
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

Use [stripe.confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment) to complete the payment using details from the Payment Element. This sends an authorization request to the buyer.

> `stripe.confirmPayment` might take several seconds to complete while waiting for customers to authorize the payment. During that time, disable your form from being resubmitted and show a waiting indicator like a spinner. If you receive an error, show it to the customer, re-enable the form, and hide the waiting indicator.

#### HTML + JS

```javascript
const form = document.getElementById("payment-form");

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const { error, paymentIntent } = await stripe.confirmPayment({
    //`Elements` instance that was used to create the Payment Element
    elements,
    redirect: "if_required",
  });

  const message = document.querySelector("#message");
  if (error) {
    // This point will only be reached if there is an immediate error when
    // confirming the payment. Show error to your customer (for example, payment
    // details incomplete)
    message.innerText = error.message;
  } else {
    // This will execute if the confirm request is successful, or if the
    // payment fails asynchronously.
    switch (paymentIntent.status) {
      case "succeeded":
        message.innerText = "Success! Payment received.";
        break;

      case "requires_payment_method":
        message.innerText =
          "Payment failed. Please try another payment method.";
        // Redirect your user back to your payment page to attempt collecting
        // payment again
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

If you prefer traditional class components over hooks, you can use an [ElementsConsumer](https://docs.stripe.com/sdks/stripejs-react.md#elements-consumer) instead.

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
    // which would refresh the page.
    event.preventDefault();

    if (!stripe || !elements) {
      // Stripe.js hasn't yet loaded.
      // Make sure to disable form submission until Stripe.js has loaded.
      return;
    }
    const { error, paymentIntent } = await stripe.confirmPayment({
      //`Elements` instance that was used to create the Payment Element
      elements,
      redirect: "if_required",
    });

    if (error) {
      // This point will only be reached if there is an immediate error when
      // confirming the payment. Show error to your customer (for example, payment
      // details incomplete)
      setMessage(error.message);
    } else {
      // This will execute if the confirm request is successful, or if the
      // payment fails asynchronously.
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
          setMessage("Payment failed. Please try another payment method.");
          // Redirect your user back to your payment page to attempt collecting
          // payment again
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

## Test your integration

Test your MB WAY integration by using the following test phone numbers. Each set of details reproduces a common live mode scenario.

| Phone number           | Description                                                                                                                                                                   |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `+351911111112`        | The PaymentIntent status transitions from `requires_action` to `succeeded` after approximately 30 seconds.                                                                    |
| `+351911111113`        | The PaymentIntent status transitions from `requires_action` to `requires_payment_method` immediately. Stripe returns the `payment_method_not_available` error code.           |
| `+351911111114`        | The PaymentIntent status transitions from `requires_action` to `requires_payment_method` immediately. Stripe returns the `payment_method_provider_decline` error code.        |
| `+351911111115`        | The PaymentIntent status transitions from `requires_action` to `requires_payment_method` immediately. Stripe returns the `payment_intent_payment_attempt_expired` error code. |
| `+351911111116`        | The PaymentIntent status transitions from `requires_action` to `requires_payment_method` immediately. Stripe returns the `payment_method_customer_decline` error code.        |
| Any other phone number | The PaymentIntent status immediately transitions from `requires_action` to `succeeded`.                                                                                       |

## Optional: Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

- **Handle events manually in the Dashboard**

  Use the Dashboard to [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments), send email receipts, handle payouts, or retry failed payments.

- **Build a custom webhook**

  [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook) handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- **Integrate a prebuilt app**

  Handle common business events, such as [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

# Direct API

> This is a Direct API for when payment-ui is direct-api. View the full page at https://docs.stripe.com/payments/mb-way/accept-a-payment?payment-ui=direct-api.

## Set up Stripe [Server-side]

First, [create a Stripe account](https://dashboard.stripe.com/register) or [sign in](https://dashboard.stripe.com/login).

Use our official libraries to access the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create a PaymentIntent [Server-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) is an object that represents your intent to collect a payment from a customer and tracks the payment process. To create a `PaymentIntent` that accepts a MB WAY payment method, specify the amount to collect, `eur` as the currency, and `mb_way` in the [payment_method_types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) list. If you maintain a list of payment method types that you pass when creating a `PaymentIntent`, add `mb_way` to it.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: "eur",
  payment_method_types: ["mb_way"],
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

When you confirm the payment, pass the client secret.

> Handle the client secret carefully, because it allows access to the PaymentIntent. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

Use `stripe.confirmMbWayPayment` to initiate the payment authorization with your customer.

The customer receives a notification about the payment request, and authorizes or declines the request in their MB WAY app.

```javascript
// Inititates the payment request notification to the customer
stripe
  .confirmMbWayPayment("{{PAYMENT_INTENT_CLIENT_SECRET}}", {
    payment_method: {
      billing_details: {
        // Phone number is required for all MB WAY payment
        phone: "+351911111111",
      },
    },
  })
  .then(function (result) {
    if (result.error) {
      // Inform the customer that there was an error.
      console.log(result.error.message);
    }
  });
```

By default, Stripe.js polls for updates to the PaymentIntent. The promise returned by `confirmMbWayPayment` resolves when the PaymentIntent reaches the `succeeded` state, or when the payment fails and the PaymentIntent returns to the `requires_payment_method` state. See the [PaymentIntent lifecycle](https://docs.stripe.com/payments/paymentintents/lifecycle.md) for details on how these transitions happen.

To poll yourself, disable automatic polling by setting `handleActions: false`:

```javascript
stripe.confirmMbWayPayment(
  '{{PAYMENT_INTENT_CLIENT_SECRET}}',
  {
    payment_method: {
      billing_details: {
        phone: '+351911111111'
      }
    }
  }
  { handleActions: false } // <---- Like this
)
```

In this case, call the [PaymentIntents API](https://docs.stripe.com/api/payment_intents/retrieve.md) to fetch status of the PaymentIntent yourself.

## Test your integration

Test your MB WAY integration by using the following test phone numbers. Each set of details reproduces a common live mode scenario.

| Phone number           | Description                                                                                                                                                                   |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `+351911111112`        | The PaymentIntent status transitions from `requires_action` to `succeeded` after approximately 30 seconds.                                                                    |
| `+351911111113`        | The PaymentIntent status transitions from `requires_action` to `requires_payment_method` immediately. Stripe returns the `payment_method_not_available` error code.           |
| `+351911111114`        | The PaymentIntent status transitions from `requires_action` to `requires_payment_method` immediately. Stripe returns the `payment_method_provider_decline` error code.        |
| `+351911111115`        | The PaymentIntent status transitions from `requires_action` to `requires_payment_method` immediately. Stripe returns the `payment_intent_payment_attempt_expired` error code. |
| `+351911111116`        | The PaymentIntent status transitions from `requires_action` to `requires_payment_method` immediately. Stripe returns the `payment_method_customer_decline` error code.        |
| Any other phone number | The PaymentIntent status immediately transitions from `requires_action` to `succeeded`.                                                                                       |

## Optional: Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

- **Handle events manually in the Dashboard**

  Use the Dashboard to [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments), send email receipts, handle payouts, or retry failed payments.

- **Build a custom webhook**

  [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook) handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- **Integrate a prebuilt app**

  Handle common business events, such as [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.
