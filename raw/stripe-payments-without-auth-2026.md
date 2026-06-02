<!-- Source URL: https://docs.stripe.com/payments/without-card-authentication -->
<!-- Fetched: 2026-05-11 -->

# Card payments without bank authentication

Build a simpler integration with regional limitations.

This integration supports businesses accepting only US and Canadian cards. It’s simpler to build, but doesn’t scale to support a global customer base.

### How this integration works

Banks in regions such as Europe and India often require two-factor authentication to confirm a purchase. If you primarily do business in the US and Canada, ignoring _card authentication_ (A bank might require the customer to authenticate a card payment before processing. Implementation varies by bank but commonly consists of a customer entering in a security code sent to their phone) can simplify your integration, as banks rarely request it in these regions.

When a bank requires authentication, this basic integration immediately declines the payment (similar to a card decline), instead of handling authentication to complete the payment asynchronously. The benefit is that the payment succeeds or declines immediately and payment confirmation happens on the server, so you can handle immediate post-payment actions without a _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests).

### How it compares to the global integration

| Feature                                                              | This Integration | Global Integration |
| -------------------------------------------------------------------- | ---------------- | ------------------ |
| Custom payment form                                                  | ✔                | ✔                  |
| Sensitive data never touches your server                             | ✔                | ✔                  |
| Works for your US and Canada customers                               | ✔                | ✔                  |
| Declines payments with incorrect card details or no funds            | ✔                | ✔                  |
| Declines payments with bank authentication requests                  | ✔                |                    |
| Works for your global customers                                      |                  | ✔                  |
| Automatically handles card payments that require bank authentication |                  | ✔                  |
| Webhooks recommended for post-payment tasks                          |                  | ✔                  |
| Easily scales to other payment methods (for example, bank debits)    |                  | ✔                  |

Growing or global businesses should use Stripe’s [global integration](https://docs.stripe.com/payments/accept-a-payment.md) to support bank requests for two-factor authentication and allow customers to pay with more payment methods.
Payment flow you're integrating (See full diagram at https://docs.stripe.com/payments/without-card-authentication)

## Build a checkout form [Client-side]

[Elements](https://docs.stripe.com/payments/elements.md), part of Stripe.js, provides drop-in UI components for collecting card information from customers. Stripe hosts them and places them into your payment form as an iframe so your customer’s card details never touch your code.

#### HTML + JS

First, include the [Stripe.js](https://docs.stripe.com/js.md) script in the head of every page on your site.

```html
<script src="https://js.stripe.com/dahlia/stripe.js"></script>
```

Including the script on every page of your site lets you take advantage of the Stripe [advanced fraud functionality](https://docs.stripe.com/radar.md) and ability to detect anomalous browsing behavior.

### Security requirements

This script must always load directly from **js.stripe.com** to remain [PCI compliant](https://docs.stripe.com/security/guide.md). You can’t include the script in a bundle or host a copy of it yourself.

When you use Elements, all payment information is submitted over a secure HTTPS connection.

The address of the page that contains Elements must also start with **https://** rather than **http://**. For more information about getting SSL certificates and integrating them with your server to enable a secure HTTPS connection, see the [security](https://docs.stripe.com/security.md) documentation.

### Add Elements to your page

Next, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Create empty DOM elements (containers) with unique IDs within your payment form.

```html
<form id="payment-form">
  <div id="card-element"><!-- placeholder for Elements --></div>
  <button id="card-button">Submit Payment</button>
  <p id="payment-result">
    <!-- we'll pass the response from the server here -->
  </p>
</form>
```

Create an instance of the [Stripe object](https://docs.stripe.com/js.md#stripe-function), providing your publishable [API key](https://docs.stripe.com/keys.md) as the first parameter. Afterwards, create an instance of the [Elements object](https://docs.stripe.com/js.md#stripe-elements) and use it to [mount](https://docs.stripe.com/js.md#element-mount) a Card element in the empty DOM element container on the page.

```javascript
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");

const elements = stripe.elements();
const cardElement = elements.create("card");
cardElement.mount("#card-element");
```

Use [stripe.createPaymentMethod](https://docs.stripe.com/js/payment_methods/create_payment_method) on your client to collect the card details and create a [PaymentMethod](https://docs.stripe.com/api/payment_methods.md) when the customer submits the payment form. Send the ID of the PaymentMethod to your server.

```javascript
const form = document.getElementById("payment-form");

var resultContainer = document.getElementById("payment-result");

// cardElement is defined in the previous step
cardElement.on("change", function (event) {
  if (event.error) {
    resultContainer.textContent = event.error.message;
  } else {
    resultContainer.textContent = "";
  }
});

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  resultContainer.textContent = "";
  const result = await stripe.createPaymentMethod({
    type: "card",
    card: cardElement,
  });
  handlePaymentMethodResult(result);
});

const handlePaymentMethodResult = async ({ paymentMethod, error }) => {
  if (error) {
    // An error happened when collecting card details, show error in payment form
    resultContainer.textContent = error.message;
  } else {
    // Send paymentMethod.id to your server (see Step 3)
    const response = await fetch("/pay", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ payment_method_id: paymentMethod.id }),
    });

    const responseJson = await response.json();

    handleServerResponse(responseJson);
  }
};

const handleServerResponse = async (responseJson) => {
  if (responseJson.error) {
    // An error happened when charging the card, show it in the payment form
    resultContainer.textContent = responseJson.error;
  } else {
    // Show a success message
    resultContainer.textContent = "Success!";
  }
};
```

#### React

First, install [Stripe.js](https://github.com/stripe/stripe-js) and [React Stripe.js](https://docs.stripe.com/sdks/stripejs-react.md).

```bash
npm install --save @stripe/stripe-js @stripe/react-stripe-js
```

> This guide assumes that you already have a basic working knowledge of React and that you already set up a React project. If you’re new to React, we recommend that you read the React [Getting Started](https://reactjs.org/docs/getting-started.html) guide before continuing.
>
> If you’re looking for a quick way to try out React Stripe.js without needing to build a new project, start with this [demo in CodeSandbox](https://codesandbox.io/s/react-stripe-official-q1loc?fontsize=14&hidenavigation=1&theme=dark).

### Security requirements

When you use Elements, all payment information is submitted over a secure HTTPS connection.

The address of the page that contains Elements must also start with **https://** rather than **http://**. For more information about getting SSL certificates and integrating them with your server to enable a secure HTTPS connection, see the [security](https://docs.stripe.com/security.md) documentation.

### Load Stripe.js and add Elements to your page

To use Elements, wrap the root of your React app in an [Elements](https://docs.stripe.com/sdks/stripejs-react.md#elements-provider) provider. Call [loadStripe](https://github.com/stripe/stripe-js#loadstripe) with your publishable key and pass the returned `Promise` to the `Elements` provider.

Import and call `loadStripe` at the root of your React app to take advantage of the Stripe [advanced fraud functionality](https://docs.stripe.com/radar.md) and its ability to detect anomalous browsing behavior.

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
  return (
    <Elements stripe={stripePromise}>
      <CheckoutForm />
    </Elements>
  );
}

ReactDOM.render(<App />, document.getElementById("root"));
```

### Create a PaymentMethod

Use the `CardElement` and [stripe.createPaymentMethod](https://docs.stripe.com/js/payment_methods/create_payment_method) on your client to collect the card details and create a [PaymentMethod](https://docs.stripe.com/api/payment_methods.md) when the customer submits the payment form. Send the ID of the PaymentMethod to your server.

To call `stripe.createPaymentMethod` from your payment form component, use the [useStripe](https://docs.stripe.com/sdks/stripejs-react.md#usestripe-hook) and [useElements](https://docs.stripe.com/sdks/stripejs-react.md#useelements-hook) hooks. If you prefer traditional class components over hooks, you can instead use an [ElementsConsumer](https://docs.stripe.com/sdks/stripejs-react.md#elements-consumer).

#### Hooks

```jsx
import React from "react";
import { useStripe, useElements, CardElement } from "@stripe/react-stripe-js";

export default function CheckoutForm() {
  const stripe = useStripe();
  const elements = useElements();

  const handleSubmit = async (event) => {
    // We don't want to let default form submission happen here,
    // which would refresh the page.
    event.preventDefault();
    const result = await stripe.createPaymentMethod({
      type: "card",
      card: elements.getElement(CardElement),
      billing_details: {
        // Include any additional collected billing details.
        name: "Jenny Rosen",
      },
    });

    handlePaymentMethodResult(result);
  };

  const handlePaymentMethodResult = async (result) => {
    if (result.error) {
      // An error happened when collecting card details,
      // show `result.error.message` in the payment form.
    } else {
      // Otherwise send paymentMethod.id to your server (see Step 3)
      const response = await fetch("/pay", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          payment_method_id: result.paymentMethod.id,
        }),
      });

      const serverResponse = await response.json();

      handleServerResponse(serverResponse);
    }
  };

  const handleServerResponse = (serverResponse) => {
    if (serverResponse.error) {
      // An error happened when charging the card,
      // show the error in the payment form.
    } else {
      // Show a success message
    }
  };

  const handleCardChange = (event) => {
    if (event.error) {
      // Show `event.error.message` in the payment form.
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <CardElement onChange={handleCardChange} />
      <button type="submit" disabled={!stripe}>
        Submit Payment
      </button>
    </form>
  );
}
```

## Set up Stripe [Server-side]

Use an official library to make requests to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Make a payment [Server-side]

Set up an endpoint on your server to receive the request from the client.

Stripe uses a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) object to represent your intent to collect payment from a customer, tracking charge attempts and payment state changes throughout the process.

Always decide how much to charge on the server, a trusted environment, as opposed to the client. This prevents malicious customers from being able to choose their own prices.

Create an HTTP endpoint to respond to the AJAX request from step 1. In that endpoint, and decide how much to charge the customer. To create a payment, create a PaymentIntent using the _PaymentMethod_ (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) ID from step 1 with the following code:

#### Node.js

```javascript
// Using Express
const express = require("express");
const app = express();
app.use(express.json());
const { resolve } = require("path");

app.get("/", (req, res) => {
  // Display checkout page
  const path = resolve("./index.html");
  res.sendFile(path);
});

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

// Endpoint for when `/pay` is called from client
app.post("/pay", async (request, response) => {
  try {
    // Create the PaymentIntent
    let intent = await stripe.paymentIntents.create({
      amount: 1099,
      currency: "usd",
      payment_method: request.body.payment_method_id,

      // A PaymentIntent can be confirmed some time after creation,
      // but here we want to confirm (collect payment) immediately.
      confirm: true,

      // If the payment requires any follow-up actions from the
      // customer, like two-factor authentication, Stripe will error
      // and you will need to prompt them for a new payment method.>
      error_on_requires_action: true,
    });
    return generateResponse(response, intent);
  } catch (e) {
    if (e.type === "StripeCardError") {
      // Display error on client
      return response.send({ error: e.message });
    } else {
      // Something else happened
      return response.status(500).send({ error: e.type });
    }
  }
});

function generateResponse(response, intent) {
  if (intent.status === "succeeded") {
    // Handle post-payment fulfillment
    return response.send({ success: true });
  } else {
    // Any other status would be unexpected, so error
    return response
      .status(500)
      .send({ error: "Unexpected status " + intent.status });
  }
}

app.listen(4242, () => console.log(`Node server listening on port ${4242}!`));
```

> If you set [error_on_requires_action](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-error_on_requires_action) to `true` when confirming a payment, Stripe automatically fails the payment if it requires two-factor authentication from the user.

#### Payment Intents API response

When you make a payment with the API, the response includes a status of the PaymentIntent. If the payment was successful, it will have a status of `succeeded`.

```json
{
  "id": "pi_0FdpcX589O8KAxCGR6tGNyWj",
  "object": "payment_intent",
  "amount": 1099,
  "charges": {
    "object": "list",
    "data": [
      {
        "id": "ch_GA9w4aF29fYajT",
        "object": "charge",
        "amount": 1099,
        "refunded": false,
        "status": "succeeded"
      }
    ]
  },
  "client_secret": "pi_0FdpcX589O8KAxCGR6tGNyWj_secret_e00tjcVrSv2tjjufYqPNZBKZc",
  "currency": "usd",
  "last_payment_error": null,
  "status": "succeeded"
}
```

If the payment is declined, the response includes the error code and error message. Here’s an example of a payment that failed because two-factor authentication was required for the card.

```json
{
  "error": {
    "code": "authentication_required",
    "decline_code": "authentication_not_handled",
    "doc_url": "https://docs.stripe.com/error-codes#authentication-required",
    "message": "This payment required an authentication action to complete, but `error_on_requires_action` was set. When you're ready, you can upgrade your integration to handle actions at https://stripe.com/docs/payments/payment-intents/upgrade-to-handle-actions.",
    "payment_intent": {
      "id": "pi_1G8JtxDpqHItWkFAnB32FhtI",
      "object": "payment_intent",
      "amount": 1099,
      "status": "requires_payment_method",
      "last_payment_error": {
        "code": "authentication_required",
        "decline_code": "authentication_not_handled",
        "doc_url": "https://docs.stripe.com/error-codes#authentication-required",
        "message": "This payment required an authentication action to complete, but `error_on_requires_action` was set. When you're ready, you can upgrade your integration to handle actions at https://stripe.com/docs/payments/payment-intents/upgrade-to-handle-actions.",
        "type": "card_error"
      }
    },
    "type": "card_error"
  }
}
```

## Test the integration

Stripe provides several test cards you can use in a _sandbox_ (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes) to make sure this integration is ready. Use them with any CVC, postal code, and future expiration date.

| Number           | Description                                                                                                       |
| ---------------- | ----------------------------------------------------------------------------------------------------------------- |
| 4242424242424242 | Succeeds and immediately processes the payment.                                                                   |
| 4000000000009995 | Always fails with a decline code of `insufficient_funds`.                                                         |
| 4000002500003155 | Requires authentication, which in this integration will fail with a decline code of `authentication_not_handled`. |

See the full list of [test cards](https://docs.stripe.com/testing.md).

## Upgrade your integration to handle card authentication

Your payments integration for basic card payments is now complete. This integration **declines cards that require authentication during payment**.

If you start seeing payments in the Dashboard listed as `Failed`, then you need to [upgrade your integration](https://docs.stripe.com/payments/payment-intents/upgrade-to-handle-actions.md). The Stripe global integration handles these payments instead of automatically declining them.
