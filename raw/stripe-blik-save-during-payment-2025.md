<!-- Source URL: https://docs.stripe.com/payments/blik/save-during-payment -->
<!-- Fetched: 2026-05-03 -->

# Save BLIK details during a payment

Save your customer's BLIK payment method while processing a payment for future recurring use.

You can save a customer’s BLIK payment method while processing a payment. This allows you to charge the customer later for recurring payments without requiring them to enter a new BLIK code. When you save BLIK during a payment, the customer approves both the payment and the mandate authorization in their banking app.

Before collecting the BLIK code, present the mandate terms to the customer, including the price, charge cycle, end date, and a link to your terms and conditions. The customer must understand and agree to the recurring terms before proceeding.

> Not all Polish banks support BLIK recurring payments. If a customer’s bank doesn’t support it, the payment fails with a `recurring_not_supported_by_bank` decline code.

# Checkout

> This is a Checkout for when payment-ui is checkout. View the full page at https://docs.stripe.com/payments/blik/save-during-payment?payment-ui=checkout.

## Create a Checkout Session [Server-side]

Create a [Checkout Session](https://docs.stripe.com/api/checkout/sessions/create.md) in `payment` mode with `setup_future_usage` set to `off_session`. This tells Stripe to save the BLIK payment method for future off-session use after the payment completes.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  mode: "payment",
  payment_method_types: ["blik"],
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  payment_intent_data: {
    setup_future_usage: "off_session",
  },
  customer: "{{CUSTOMER_ID}}",
  success_url: "https://example.com/success",
});
```

After the customer completes the Checkout Session, a reusable BLIK PaymentMethod is attached to the Customer. The customer approves both the payment and the mandate authorization in their banking app.

## Charge the saved BLIK PaymentMethod later [Server-side]

After you save a BLIK payment method, you can use it to charge the customer off-session without making them enter a new BLIK code.

Create a [PaymentIntent](https://docs.stripe.com/api/payment_intents/create.md) with `off_session` set to `true` and the saved PaymentMethod and Customer IDs.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "pln",
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{PAYMENTMETHOD_ID}}",
  payment_method_types: ["blik"],
  off_session: true,
  confirm: true,
});
```

After confirming the PaymentIntent, it initiates a payment. The `next_action` has the `blik_authorize` type, which means that the next step is completed by the customer’s bank, who validates the payment against the terms of the original mandate. We recommend showing a timer or a dialog to your customer and polling your server or the Stripe API for the PaymentIntent status update.

> You must listen for webhooks to determine the final payment status. Use the `payment_intent.succeeded` and `payment_intent.payment_failed` events to handle the outcome.

### Limitations

- **Currency**: Only `pln` is supported.
- **Maximum amount**: Each off-session recurring payment can’t exceed 2000 PLN.

### Handling failures

If the customer’s bank declines the payment, the PaymentIntent transitions to `requires_payment_method`. To resolve a failed off-session payment, you can bring the customer back on session and collect a new payment method, or retry the payment if the failure was transient.

## Simulate failures in a sandbox

In addition to the [one-time payment test patterns](https://docs.stripe.com/payments/blik/accept-a-payment.md#simulate-failures), you can simulate recurring-specific scenarios by passing `email` values matching the patterns below when creating the `SetupIntent` or `PaymentIntent`, as part of the [billing details](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_data-billing_details).

### Mandate setup failures (immediate)

| Failure code                      | Explanation                                                  | Email pattern                  |
| --------------------------------- | ------------------------------------------------------------ | ------------------------------ |
| `payment_method_provider_decline` | The customer’s bank doesn’t support BLIK recurring payments. | `.*recurring_not_supported@.*` |

### Mandate setup failures (8 second delay)

| Failure code                      | Explanation                                                           | Email pattern         |
| --------------------------------- | --------------------------------------------------------------------- | --------------------- |
| `payment_method_provider_decline` | The customer rejected the mandate authorization in their banking app. | `.*alias_declined@.*` |

### Mandate setup failures (60 second delay)

| Event produced                          | Explanation                                                          | Email pattern        |
| --------------------------------------- | -------------------------------------------------------------------- | -------------------- |
| `mandate.updated` (pending to inactive) | The customer didn’t complete the mandate setup in their banking app. | `.*setup_timeout@.*` |

### Mandate lifecycle events (6 minute delay)

These patterns simulate events that occur after a mandate has been successfully set up.

| Event produced                         | Explanation                                                           | Email pattern             |
| -------------------------------------- | --------------------------------------------------------------------- | ------------------------- |
| `mandate.updated` (active to inactive) | The customer removed the saved payment method from their banking app. | `.*alias_unregistered@.*` |
| `mandate.updated` (active to inactive) | The mandate reached its expiration date.                              | `.*alias_expired@.*`      |

### Off-session payment failures (immediate)

These patterns affect off-session payments made with a saved BLIK payment method.

| Failure code                      | Explanation                                                                       | Email pattern             |
| --------------------------------- | --------------------------------------------------------------------------------- | ------------------------- |
| `payment_method_provider_decline` | The mandate setup succeeds, but all subsequent off-session payments are declined. | `.*recurring_declined@.*` |

# Elements

> This is a Elements for when payment-ui is elements. View the full page at https://docs.stripe.com/payments/blik/save-during-payment?payment-ui=elements.

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create or retrieve a Customer [Server-side]

To reuse a BLIK payment method for future payments, you must attach it to a [Customer](https://docs.stripe.com/api/customers.md).

Create a `Customer` object when your customer creates an account with your business. Associating the ID of the `Customer` object with your own internal representation of a customer enables you to retrieve and use the stored payment method details later.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create();
```

## Create a PaymentIntent [Server-side]

Create a [PaymentIntent](https://docs.stripe.com/api/payment_intents/create.md) with the amount, `pln` currency, the Customer ID, and `setup_future_usage` set to `off_session`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "pln",
  customer: "{{CUSTOMER_ID}}",
  payment_method_types: ["blik"],
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

## Collect payment method details [Client-side]

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

> `stripe.confirmPayment` may take several seconds to complete. During that time, disable your form from being resubmitted and show a waiting indicator like a spinner. If you receive an error, show it to the customer, re-enable the form, and hide the waiting indicator. If the customer must perform additional steps to complete the payment, such as authentication, Stripe.js walks them through that process.

If the payment succeeded, the card is saved to the Customer object. This is reflected on the *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs)’s [customer](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-customer) field. At this point, associate the ID of the *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) object with your own internal representation of a customer, if you have one. Now you can use the stored PaymentMethod object to collect payments from your customer in the future without prompting them for their payment details again.

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

After confirming with valid parameters, the PaymentIntent’s status becomes `requires_action`. The `next_action` has the `blik_authorize` type. The customer has 60 seconds to approve both the payment and the mandate authorization in their banking app.

## Optional: Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

- **Handle events manually in the Dashboard**

  Use the Dashboard to [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments), send email receipts, handle payouts, or retry failed payments.

- **Build a custom webhook**

  [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook) handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- **Integrate a prebuilt app**

  Handle common business events, such as [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

## Charge the saved BLIK PaymentMethod later [Server-side]

After you save a BLIK payment method, you can use it to charge the customer off-session without making them enter a new BLIK code.

Create a [PaymentIntent](https://docs.stripe.com/api/payment_intents/create.md) with `off_session` set to `true` and the saved PaymentMethod and Customer IDs.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "pln",
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{PAYMENTMETHOD_ID}}",
  payment_method_types: ["blik"],
  off_session: true,
  confirm: true,
});
```

After confirming the PaymentIntent, it initiates a payment. The `next_action` has the `blik_authorize` type, which means that the next step is completed by the customer’s bank, who validates the payment against the terms of the original mandate. We recommend showing a timer or a dialog to your customer and polling your server or the Stripe API for the PaymentIntent status update.

> You must listen for webhooks to determine the final payment status. Use the `payment_intent.succeeded` and `payment_intent.payment_failed` events to handle the outcome.

### Limitations

- **Currency**: Only `pln` is supported.
- **Maximum amount**: Each off-session recurring payment can’t exceed 2000 PLN.

### Handling failures

If the customer’s bank declines the payment, the PaymentIntent transitions to `requires_payment_method`. To resolve a failed off-session payment, you can bring the customer back on session and collect a new payment method, or retry the payment if the failure was transient.

## Simulate failures in a sandbox

In addition to the [one-time payment test patterns](https://docs.stripe.com/payments/blik/accept-a-payment.md#simulate-failures), you can simulate recurring-specific scenarios by passing `email` values matching the patterns below when creating the `SetupIntent` or `PaymentIntent`, as part of the [billing details](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_data-billing_details).

### Mandate setup failures (immediate)

| Failure code                      | Explanation                                                  | Email pattern                  |
| --------------------------------- | ------------------------------------------------------------ | ------------------------------ |
| `payment_method_provider_decline` | The customer’s bank doesn’t support BLIK recurring payments. | `.*recurring_not_supported@.*` |

### Mandate setup failures (8 second delay)

| Failure code                      | Explanation                                                           | Email pattern         |
| --------------------------------- | --------------------------------------------------------------------- | --------------------- |
| `payment_method_provider_decline` | The customer rejected the mandate authorization in their banking app. | `.*alias_declined@.*` |

### Mandate setup failures (60 second delay)

| Event produced                          | Explanation                                                          | Email pattern        |
| --------------------------------------- | -------------------------------------------------------------------- | -------------------- |
| `mandate.updated` (pending to inactive) | The customer didn’t complete the mandate setup in their banking app. | `.*setup_timeout@.*` |

### Mandate lifecycle events (6 minute delay)

These patterns simulate events that occur after a mandate has been successfully set up.

| Event produced                         | Explanation                                                           | Email pattern             |
| -------------------------------------- | --------------------------------------------------------------------- | ------------------------- |
| `mandate.updated` (active to inactive) | The customer removed the saved payment method from their banking app. | `.*alias_unregistered@.*` |
| `mandate.updated` (active to inactive) | The mandate reached its expiration date.                              | `.*alias_expired@.*`      |

### Off-session payment failures (immediate)

These patterns affect off-session payments made with a saved BLIK payment method.

| Failure code                      | Explanation                                                                       | Email pattern             |
| --------------------------------- | --------------------------------------------------------------------------------- | ------------------------- |
| `payment_method_provider_decline` | The mandate setup succeeds, but all subsequent off-session payments are declined. | `.*recurring_declined@.*` |

# Direct API

> This is a Direct API for when payment-ui is direct-api. View the full page at https://docs.stripe.com/payments/blik/save-during-payment?payment-ui=direct-api.

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create or retrieve a Customer [Server-side]

To reuse a BLIK payment method for future payments, you must attach it to a [Customer](https://docs.stripe.com/api/customers.md).

Create a `Customer` object when your customer creates an account with your business. Associating the ID of the `Customer` object with your own internal representation of a customer enables you to retrieve and use the stored payment method details later.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create();
```

## Create a PaymentIntent [Server-side]

Create a [PaymentIntent](https://docs.stripe.com/api/payment_intents/create.md) with the amount, `pln` currency, the Customer ID, `setup_future_usage` set to `off_session`, and the BLIK code.

You must provide `mandate_data` with `customer_acceptance` set to `online`, including the customer’s `ip_address` and `user_agent`. This is required by the BLIK scheme for recurring mandates.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "pln",
  customer: "{{CUSTOMER_ID}}",
  payment_method_types: ["blik"],
  setup_future_usage: "off_session",
  payment_method_data: {
    type: "blik",
    billing_details: {
      email: "buyer@example.com",
    },
  },
  payment_method_options: {
    blik: {
      code: "123456",
    },
  },
  mandate_data: {
    customer_acceptance: {
      type: "online",
      online: {
        ip_address: "{{CUSTOMER_IP_ADDRESS}}",
        user_agent: "{{CUSTOMER_USER_AGENT}}",
      },
    },
  },
  confirm: true,
});
```

The response includes `status: requires_action` with a `next_action` of type `blik_authorize`:

```json
{
  "id": "pi_xxx",
  "status": "requires_action",
  "next_action": {
    "type": "blik_authorize",
    "blik_authorize": {}
  }
}
```

## Handle the next action [Client-side]

Prompt the customer to open their banking app and approve the operation. The customer has 60 seconds to confirm both the payment and the mandate authorization in their banking app.

Listen for the following webhooks to determine the outcome:

- `payment_intent.succeeded`: The payment and mandate were both approved
- `payment_intent.payment_failed`: The payment or mandate was declined
- `mandate.updated`: The mandate status has changed

## Optional: Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

- **Handle events manually in the Dashboard**

  Use the Dashboard to [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments), send email receipts, handle payouts, or retry failed payments.

- **Build a custom webhook**

  [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook) handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- **Integrate a prebuilt app**

  Handle common business events, such as [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

## Charge the saved BLIK PaymentMethod later [Server-side]

After you save a BLIK payment method, you can use it to charge the customer off-session without making them enter a new BLIK code.

Create a [PaymentIntent](https://docs.stripe.com/api/payment_intents/create.md) with `off_session` set to `true` and the saved PaymentMethod and Customer IDs.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "pln",
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{PAYMENTMETHOD_ID}}",
  payment_method_types: ["blik"],
  off_session: true,
  confirm: true,
});
```

After confirming the PaymentIntent, it initiates a payment. The `next_action` has the `blik_authorize` type, which means that the next step is completed by the customer’s bank, who validates the payment against the terms of the original mandate. We recommend showing a timer or a dialog to your customer and polling your server or the Stripe API for the PaymentIntent status update.

> You must listen for webhooks to determine the final payment status. Use the `payment_intent.succeeded` and `payment_intent.payment_failed` events to handle the outcome.

### Limitations

- **Currency**: Only `pln` is supported.
- **Maximum amount**: Each off-session recurring payment can’t exceed 2000 PLN.

### Handling failures

If the customer’s bank declines the payment, the PaymentIntent transitions to `requires_payment_method`. To resolve a failed off-session payment, you can bring the customer back on session and collect a new payment method, or retry the payment if the failure was transient.

## Simulate failures in a sandbox

In addition to the [one-time payment test patterns](https://docs.stripe.com/payments/blik/accept-a-payment.md#simulate-failures), you can simulate recurring-specific scenarios by passing `email` values matching the patterns below when creating the `SetupIntent` or `PaymentIntent`, as part of the [billing details](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_data-billing_details).

### Mandate setup failures (immediate)

| Failure code                      | Explanation                                                  | Email pattern                  |
| --------------------------------- | ------------------------------------------------------------ | ------------------------------ |
| `payment_method_provider_decline` | The customer’s bank doesn’t support BLIK recurring payments. | `.*recurring_not_supported@.*` |

### Mandate setup failures (8 second delay)

| Failure code                      | Explanation                                                           | Email pattern         |
| --------------------------------- | --------------------------------------------------------------------- | --------------------- |
| `payment_method_provider_decline` | The customer rejected the mandate authorization in their banking app. | `.*alias_declined@.*` |

### Mandate setup failures (60 second delay)

| Event produced                          | Explanation                                                          | Email pattern        |
| --------------------------------------- | -------------------------------------------------------------------- | -------------------- |
| `mandate.updated` (pending to inactive) | The customer didn’t complete the mandate setup in their banking app. | `.*setup_timeout@.*` |

### Mandate lifecycle events (6 minute delay)

These patterns simulate events that occur after a mandate has been successfully set up.

| Event produced                         | Explanation                                                           | Email pattern             |
| -------------------------------------- | --------------------------------------------------------------------- | ------------------------- |
| `mandate.updated` (active to inactive) | The customer removed the saved payment method from their banking app. | `.*alias_unregistered@.*` |
| `mandate.updated` (active to inactive) | The mandate reached its expiration date.                              | `.*alias_expired@.*`      |

### Off-session payment failures (immediate)

These patterns affect off-session payments made with a saved BLIK payment method.

| Failure code                      | Explanation                                                                       | Email pattern             |
| --------------------------------- | --------------------------------------------------------------------------------- | ------------------------- |
| `payment_method_provider_decline` | The mandate setup succeeds, but all subsequent off-session payments are declined. | `.*recurring_declined@.*` |
