<!-- Source URL: https://docs.stripe.com/payments/ideal/save-during-payment -->
<!-- Fetched: 2026-05-03 -->

# Save bank details during an iDEAL | Wero payment

Learn how to save your customer's IBAN bank details from an iDEAL | Wero payment.

> We recommend that you follow the [Save payment details during payment](https://docs.stripe.com/payments/save-during-payment.md) guide. If you’ve already integrated with Elements, see the [Payment Element migration guide](https://docs.stripe.com/payments/payment-element/migration.md).

See [accepting SEPA Direct Debit payments](https://docs.stripe.com/payments/sepa-debit/accept-a-payment.md) to integrate without iDEAL | Wero.

iDEAL | Wero (formerly iDEAL) is a popular [single use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method in the Netherlands where customers are required to [authenticate](https://docs.stripe.com/payments/payment-methods.md#customer-actions) their payment. *Customers* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) pay with iDEAL | Wero by redirecting to a webview, authorizing the payment, then returning to your app where you get [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) on whether the payment succeeded or failed.

You can also use iDEAL | Wero to save your customer’s [IBAN](https://en.wikipedia.org/wiki/International_Bank_Account_Number) bank details into a [SEPA Direct Debit](https://docs.stripe.com/payments/sepa-debit.md) *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs). You can then use the SEPA Direct Debit PaymentMethod to [accept payments](https://docs.stripe.com/payments/sepa-debit/accept-a-payment.md) or [set up a subscription](https://docs.stripe.com/billing/subscriptions/sepa-debit.md). This reduces friction for your customer as they don’t have to enter their IBAN again. You also receive their verified name and validated IBAN.

> To use iDEAL | Wero to set up SEPA Direct Debit payments, you must activate SEPA Direct Debit in the [Dashboard](https://dashboard.stripe.com/account/payments/settings). You must also comply with the [iDEAL Terms of Service](https://stripe.com/ideal/legal) and [SEPA Direct Debit Terms of Service](https://stripe.com/sepa-direct-debit/legal).

# Elements

> This is a Elements for when payment-ui is elements. View the full page at https://docs.stripe.com/payments/ideal/save-during-payment?payment-ui=elements.

Accepting iDEAL | Wero payments consists of creating a [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) object to track a payment, collecting payment method details and mandate acknowledgement, and submitting the payment to Stripe for processing. Stripe uses the PaymentIntent to track and handle all the states of the payment until the payment completes. Use the ID of the SEPA Direct Debit *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) collected from your initial iDEAL | Wero PaymentIntent to create future payments.

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create a Customer [Server-side]

Create a *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) when they create an account with your business and associate it with your internal representation of their account. This enables you to retrieve and use their saved payment method details later.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create();
```

## Create a PaymentIntent [Server-side]

Create a `PaymentIntent` on your server and specify the `amount` to collect, the `eur` currency, the customer ID, and `off_session` as an argument for [setup future usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage). There is no minimum charge amount and iDEAL | Wero doesn’t support other currencies. If you have an existing [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md) integration, add `ideal` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  payment_method_types: ["ideal"],
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

## Charge the SEPA Direct Debit PaymentMethod later

When you need to charge your customer again, create a new PaymentIntent. Find the ID of the SEPA Direct Debit payment method by [retrieving](https://docs.stripe.com/api/payment_intents/retrieve.md) the previous PaymentIntent and [expanding](https://docs.stripe.com/api/expanding_objects.md) the `latest_charge` field where you’ll find the `generated_sepa_debit` ID inside of `payment_method_details`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.retrieve(
  "{{PAYMENT_INTENT_ID}}",
  {
    expand: ["latest_charge"],
  },
);
```

The SEPA Direct Debit payment method ID is the `generated_sepa_debit` ID under [payment_method_details](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-ideal) in the response.

#### Json

```json
{
  "latest_charge": {
    "payment_method_details": {
      "ideal": {
        "bank": "ing",
        "bic": "INGBNL2A",
        "iban_last4": "****",
        "generated_sepa_debit": "pm_1GrddXGf98efjktuBIi3ag7aJQ",
        "verified_name": "JENNY ROSEN"
      },
      "type": "ideal"
    }
  },
  "payment_method_options": {
    "ideal": {}
  },
  "payment_method_types": ["ideal"],
  "id": "pi_1G1sgdKi6xqXeNtkldRRE6HT",
  "object": "payment_intent",
  "amount": 1099,
  "client_secret": "pi_1G1sgdKi6xqXeNtkldRRE6HT_secret_h9B56ObhTN72fQiBAuzcVPb2E",
  "confirmation_method": "automatic",
  "created": 1579259303,
  "currency": "eur",
  "customer": "cus_f0Us034jfkXcl0CJQ",
  "livemode": true,
  "next_action": null
}
```

Create a `PaymentIntent` with the SEPA Direct Debit ID and the customer’s ID.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["sepa_debit"],
  amount: 1099,
  currency: "eur",
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  payment_method: "{{SEPA_DEBIT_PAYMENT_METHOD_ID}}",
  confirm: true,
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["sepa_debit"],
  amount: 1099,
  currency: "eur",
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{SEPA_DEBIT_PAYMENT_METHOD_ID}}",
  confirm: true,
});
```

## Test your integration

Use your [test API keys](https://docs.stripe.com/keys.md#test-live-modes) to confirm the PaymentIntent. After confirming, you’re redirected to a test page with options to authorize or fail the payment.

- Click **Authorize test payment** to test the case when the payment is successful. The PaymentIntent transitions from `requires_action` to `succeeded`.
- Click **Fail test payment** to test the case when the customer fails to authenticate. The PaymentIntent transitions from `requires_action` to `requires_payment_method`.

### Test your SEPA Direct Debit integration

#### Email

Set `payment_method.billing_details.email` to one of the following values to test the `PaymentIntent` status transitions. You can include your own custom text at the beginning of the email address followed by an underscore. For example, `test_1_generatedSepaDebitIntentsFail@example.com` results in a SEPA Direct Debit PaymentMethod that always fails when used with a `PaymentIntent`.

| Email Address                                                      | Description                                                                                                                       |
| ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| `generatedSepaDebitIntentsSucceed@example.com`                     | The `PaymentIntent` status transitions from `processing` to `succeeded`.                                                          |
| `generatedSepaDebitIntentsSucceedDelayed@example.com`              | The `PaymentIntent` status transitions from `processing` to `succeeded` after at least three minutes.                             |
| `generatedSepaDebitIntentsFail@example.com`                        | The `PaymentIntent` status transitions from `processing` to `requires_payment_method`.                                            |
| `generatedSepaDebitIntentsFailDelayed@example.com`                 | The `PaymentIntent` status transitions from `processing` to `requires_payment_method` after at least three minutes.               |
| `generatedSepaDebitIntentsSucceedDisputed@example.com`             | The `PaymentIntent` status transitions from `processing` to `succeeded`, but a dispute is created immediately.                    |
| `generatedSepaDebitIntentsFailsDueToInsufficientFunds@example.com` | The `PaymentIntent` status transitions from `processing` to `requires_payment_method` with the `insufficient_funds` failure code. |

#### PaymentMethod

Use these PaymentMethods to test that the `PaymentIntent` status transitions. These tokens are useful for automated testing to immediately attach the PaymentMethod to the PaymentIntent on the server.

| Payment Method                                                  | Description                                                                                                                       |
| --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `pm_ideal_generatedSepaDebitIntentsSucceed`                     | The `PaymentIntent` status transitions from `processing` to `succeeded`.                                                          |
| `pm_ideal_generatedSepaDebitIntentsSucceedDelayed`              | The `PaymentIntent` status transitions from `processing` to `succeeded` after at least three minutes.                             |
| `pm_ideal_generatedSepaDebitIntentsFail`                        | The `PaymentIntent` status transitions from `processing` to `requires_payment_method`.                                            |
| `pm_ideal_generatedSepaDebitIntentsFailDelayed`                 | The `PaymentIntent` status transitions from `processing` to `requires_payment_method` after at least three minutes.               |
| `pm_ideal_generatedSepaDebitIntentsSucceedDisputed`             | The `PaymentIntent` status transitions from `processing` to `succeeded`, but a dispute is created immediately.                    |
| `pm_ideal_generatedSepaDebitIntentsFailsDueToInsufficientFunds` | The `PaymentIntent` status transitions from `processing` to `requires_payment_method` with the `insufficient_funds` failure code. |

## Optional: Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

### Receive events and run business actions

There are a few options for receiving and running business actions.

#### Manually

Use the Stripe Dashboard to view all your Stripe payments, send email receipts, handle payouts, or retry failed payments.

- [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments)

#### Custom code

Build a webhook handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook)

#### Prebuilt apps

Handle common business events, like [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

## Optional: Handle the iDEAL | Wero redirect manually

We recommend relying on Stripe.js to handle iDEAL | Wero redirects and payments with `confirmIdealPayment`. However, you can also complete the payment on your server and manually redirect your customer.

1. After [collecting payment method details](https://docs.stripe.com/payments/ideal/save-during-payment.md#web-collect-payment-method-details), call [stripe.createPaymentMethod](https://docs.stripe.com/js/payment_methods/create_payment_method) to create a *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs):
   ```javascript
   const paymentMethod = await stripe.createPaymentMethod({
     type: "ideal",
     billing_details: {
       name: accountholderName.value,
     },
   });
   ```
1. On your server, [confirm](https://docs.stripe.com/api/payment_intents/confirm.md) the PaymentIntent with the PaymentMethod ID and provide a [return_url](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-return_url) to redirect your customer after they complete the payment.

   ```node
   // Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
   // Find your keys at https://dashboard.stripe.com/apikeys.
   const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

   const paymentIntent = await stripe.paymentIntents.confirm(
     "{{PAYMENT_INTENT_ID}}",
     {
       payment_method: "{{PAYMENTMETHOD_ID}}",
       return_url: "https://example.com/checkout/complete",
     },
   );
   ```

   Confirming the `PaymentIntent` has a status of `requires_action` with a `next_action` of `redirect_to_url`.

   #### Json

   ```json
   {
     "next_action": {
       "type": "redirect_to_url",
       "redirect_to_url": {
         "url": "https://hooks.stripe.com/...",
         "return_url": "https://example.com/checkout/complete"
       }
     },
     "charges": {
       "data": [
         {
           "payment_method_details": {
             "ideal": {
               "bank": "ing",
               "bic": "INGBNL2A",
               "iban_last4": "****",
               "verified_name": "JENNY ROSEN"
             },
             "type": "ideal"
           },
           "id": "src_16xhynE8WzK49JbAs9M21jaR",
           "object": "source",
           "amount": 1099,
           "client_secret": "src_client_secret_UfwvW2WHpZ0s3QEn9g5x7waU",
           "created": 1445277809,
           "currency": "eur",
           "flow": "redirect",
           "livemode": true,
           "statement_descriptor": null,
           "status": "pending",
           "type": "ideal",
           "usage": "single_use"
         }
       ],
       "object": "list",
       "has_more": false,
       "url": "/v1/charges?payment_intent=pi_1G1sgdKi6xqXeNtkldRRE6HT"
     },
     "payment_method_options": {
       "ideal": {}
     },
     "payment_method_types": ["ideal"],
     "id": "pi_1G1sgdKi6xqXeNtkldRRE6HT",
     "object": "payment_intent",
     "amount": 1099,
     "client_secret": "pi_1G1sgdKi6xqXeNtkldRRE6HT_secret_h9B56ObhTN72fQiBAuzcVPb2E",
     "confirmation_method": "automatic",
     "created": 1579259303,
     "currency": "eur",
     "livemode": true
   }
   ```

1. Redirect your customer to the URL provided in the `next_action` property so they can authenticate and complete the payment.
   ```javascript
   const action = intent.next_action;
   if (action && action.type === "redirect_to_url") {
     window.location = action.redirect_to_url.url;
   }
   ```
   Your customer is redirected to the `return_url` after they complete the payment. The URL includes `payment_intent` and `payment_intent_client_secret` query parameters and you can also append your own query parameters, as described above.

# iOS

> This is a iOS for when payment-ui is mobile and platform is ios. View the full page at https://docs.stripe.com/payments/ideal/save-during-payment?payment-ui=mobile&platform=ios.

Accepting iDEAL | Wero payments consists of creating a [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) object to track a payment, collecting payment method details and mandate acknowledgement, and submitting the payment to Stripe for processing. Stripe uses the PaymentIntent to track and handle all the states of the payment until the payment completes. Use the ID of the SEPA Direct Debit *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) collected from your initial iDEAL | Wero PaymentIntent to create future payments.

## Set up Stripe [Server-side] [Client-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

### Server-side

This integration requires endpoints on your server that talk to the Stripe API. Use the official libraries for access to the Stripe API from your server:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

### Client-side

The [Stripe iOS SDK](https://github.com/stripe/stripe-ios) is open source, [fully documented](https://stripe.dev/stripe-ios/index.html), and compatible with apps supporting iOS 13 or above.

#### Swift Package Manager

To install the SDK, follow these steps:

1. In Xcode, select **File** > **Add Package Dependencies…** and enter `https://github.com/stripe/stripe-ios-spm` as the repository URL.
1. Select the latest version number from our [releases page](https://github.com/stripe/stripe-ios/releases).
1. Add the **StripePaymentsUI** product to the [target of your app](https://developer.apple.com/documentation/swift_packages/adding_package_dependencies_to_your_app).

#### CocoaPods

1. If you haven’t already, install the latest version of [CocoaPods](https://guides.cocoapods.org/using/getting-started.html).
1. If you don’t have an existing [Podfile](https://guides.cocoapods.org/syntax/podfile.html), run the following command to create one:
   ```bash
   pod init
   ```
1. Add this line to your `Podfile`:
   ```podfile
   pod 'StripePaymentsUI'
   ```
1. Run the following command:
   ```bash
   pod install
   ```
1. Don’t forget to use the `.xcworkspace` file to open your project in Xcode, instead of the `.xcodeproj` file, from here on out.
1. In the future, to update to the latest version of the SDK, run:
   ```bash
   pod update StripePaymentsUI
   ```

#### Carthage

1. If you haven’t already, install the latest version of [Carthage](https://github.com/Carthage/Carthage#installing-carthage).
1. Add this line to your `Cartfile`:
   ```cartfile
   github "stripe/stripe-ios"
   ```
1. Follow the [Carthage installation instructions](https://github.com/Carthage/Carthage#if-youre-building-for-ios-tvos-or-watchos). Make sure to embed all of the required frameworks listed [here](https://github.com/stripe/stripe-ios/tree/master/StripePaymentsUI/README.md#manual-linking).
1. In the future, to update to the latest version of the SDK, run the following command:
   ```bash
   carthage update stripe-ios --platform ios
   ```

#### Manual Framework

1. Head to our [GitHub releases page](https://github.com/stripe/stripe-ios/releases/latest) and download and unzip **Stripe.xcframework.zip**.
1. Drag **StripePaymentsUI.xcframework** to the **Embedded Binaries** section of the **General** settings in your Xcode project. Make sure to select **Copy items if needed**.
1. Repeat step 2 for all required frameworks listed [here](https://github.com/stripe/stripe-ios/tree/master/StripePaymentsUI/README.md#manual-linking).
1. In the future, to update to the latest version of our SDK, repeat steps 1–3.

> For details on the latest SDK release and past versions, see the [Releases](https://github.com/stripe/stripe-ios/releases) page on GitHub. To receive notifications when a new release is published, [watch releases](https://help.github.com/en/articles/watching-and-unwatching-releases-for-a-repository#watching-releases-for-a-repository) for the repository.

Configure the SDK with your Stripe [publishable key](https://dashboard.stripe.com/test/apikeys) on app start. This enables your app to make requests to the Stripe API.

#### Swift

```swift
import UIKitimportStripePaymentsUI

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {StripeAPI.defaultPublishableKey = "<<YOUR_PUBLISHABLE_KEY>>"
        // do any other necessary launch configuration
        return true
    }
}
```

> Use your [test keys](https://docs.stripe.com/keys.md#obtain-api-keys) while you test and develop, and your [live mode](https://docs.stripe.com/keys.md#test-live-modes) keys when you publish your app.

## Create a Customer [Server-side]

Create a *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) when they create an account with your business and associate it with your internal representation of their account. This enables you to retrieve and use their saved payment method details later.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create();
```

## Create a PaymentIntent [Server-side]

Create a `PaymentIntent` on your server and specify the `amount` to collect, the `eur` currency, the customer ID, and `off_session` as an argument for [setup future usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage). There is no minimum charge amount and iDEAL | Wero doesn’t support other currencies. If you have an existing [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md) integration, add `ideal` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  payment_method_types: ["ideal"],
  customer: "{{CUSTOMER_ID}}",
  setup_future_usage: "off_session",
});
```

The PaymentIntent includes the payment method ID and a *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)), which is used on the client side to securely complete the payment process instead of passing the entire PaymentIntent object.

## Collect payment method details and mandate acknowledgement [Client-side]

In your app, collect your customer’s full name and email address. Create an [STPPaymentMethodParams](https://stripe.dev/stripe-ios/stripe-payments/Classes/STPPaymentMethodParams.html) object with these details.

#### Swift

```swift
let billingDetails = STPPaymentMethodBillingDetails()
billingDetails.name = "Jane Doe"
billingDetails.email = "jane.doe@example.com"

let paymentMethodParams = STPPaymentMethodParams(billingDetails: billingDetails,
                                                 metadata: nil)
```

​​To process SEPA Direct Debit payments, you must collect a mandate agreement from your customer. Display the following standard authorization text for your customer to implicitly sign the mandate.

Replace *Rocket Rides* with your company name.

#### de

Durch Angabe Ihrer Zahlungsinformationen und der Bestätigung der vorliegenden Zahlung ermächtigen Sie (A) und Stripe, unseren Zahlungsdienstleister, Ihrem Kreditinstitut Anweisungen zur Belastung Ihres Kontos zu erteilen, und (B) Ihr Kreditinstitut, Ihr Konto gemäß diesen Anweisungen zu belasten. Im Rahmen Ihrer Rechte haben Sie, entsprechend den Vertragsbedingungen mit Ihrem Kreditinstitut, Anspruch auf eine Rückerstattung von Ihrem Kreditinstitut. Eine Rückerstattung muss innerhalb von 8 Wochen ab dem Tag, an dem Ihr Konto belastet wurde, geltend gemacht werden. Eine Erläuterung Ihrer Rechte können Sie von Ihrem Kreditinstitut anfordern. Sie erklären sich einverstanden, Benachrichtigungen über künftige Belastungen bis spätestens 2 Tage vor dem Buchungsdatum zu erhalten.

#### en

By providing your payment information and confirming this payment, you authorise (A) and Stripe, our payment service provider, to send instructions to your bank to debit your account and (B) your bank to debit your account in accordance with those instructions. As part of your rights, you’re entitled to a refund from your bank under the terms and conditions of your agreement with your bank. A refund must be claimed within 8 weeks starting from the date on which your account was debited. Your rights are explained in a statement that you can obtain from your bank. You agree to receive notifications for future debits up to 2 days before they occur.

#### es

Al proporcionar sus datos de pago y confirmar este pago, usted autoriza a (A) y Stripe, nuestro proveedor de servicios de pago, a enviar instrucciones a su banco para realizar un débito en su cuenta y (B) a su banco a realizar un cargo en su cuenta de conformidad con dichas instrucciones. Como parte de sus derechos, usted tiene derecho a un reembolso de su banco conforme a los términos y condiciones del contrato con su banco. El reembolso debe reclamarse en un plazo de 8 semanas a partir de la fecha en la que se haya efectuado el cargo en su cuenta. Sus derechos se explican en un extracto que puede obtener en su banco. Usted acepta recibir notificaciones de futuros débitos hasta 2 días antes de que se produzcan.

#### fi

Antamalla maksutiedot ja vahvistamalla tämän maksun, valtuutat (A) ja Stripen, maksupalveluntarjoajamme, lähettämään ohjeet pankille tilisi veloittamiseksi ja (B) pankkisi veloittamaan tiliäsi kyseisten ohjeiden mukaisesti. Oikeuksiesi mukaisesti olet oikeutettu maksun palautukseen pankilta, kuten heidän kanssaan tekemässäsi sopimuksessa ja sen ehdoissa on kuvattu. Maksun palautus on lunastettava 8 viikon aikana alkaen päivästä, jolloin tiliäsi veloitettiin. Oikeutesi on selitetty pankilta saatavissa olevassa lausunnossa. Hyväksyt vastaanottamaan ilmoituksia tulevista veloituksista jopa kaksi päivää ennen niiden tapahtumista.

#### fr

En fournissant vos informations de paiement et en confirmant ce paiement, vous autorisez (A) et Stripe, notre prestataire de services de paiement et/ou PPRO, son prestataire de services local, à envoyer des instructions à votre banque pour débiter votre compte et (B) votre banque à débiter votre compte conformément à ces instructions. Vous avez, entre autres, le droit de vous faire rembourser par votre banque selon les modalités et conditions du contrat conclu avec votre banque. La demande de remboursement doit être soumise dans un délai de 8 semaines à compter de la date à laquelle votre compte a été débité. Vos droits sont expliqués dans une déclaration disponible auprès de votre banque. Vous acceptez de recevoir des notifications des débits à venir dans les 2 jours précédant leur réalisation.

#### it

Fornendo i dati di pagamento e confermando il pagamento, l’utente autorizza (A) e Stripe, il fornitore del servizio di pagamento locale, a inviare alla sua banca le istruzioni per eseguire addebiti sul suo conto e (B) la sua banca a effettuare addebiti conformemente a tali istruzioni. L’utente, fra le altre cose, ha diritto a un rimborso dalla banca, in base a termini e condizioni dell’accordo sottoscritto con l’istituto. Il rimborso va richiesto entro otto settimane dalla data dell’addebito sul conto. I diritti dell’utente sono illustrati in una comunicazione riepilogativa che è possibile richiedere alla banca. L’utente accetta di ricevere notifiche per i futuri addebiti fino a due giorni prima che vengano effettuati.

#### nl

Door je betaalgegevens door te geven en deze betaling te bevestigen, geef je (A) en Stripe, onze betaaldienst, toestemming om instructies naar je bank te verzenden om het bedrag van je rekening af te schrijven, en (B) geef je je bank toestemming om het bedrag van je rekening af te schrijven conform deze aanwijzingen. Als onderdeel van je rechten kom je in aanmerking voor een terugbetaling van je bank conform de voorwaarden van je overeenkomst met de bank. Je moet terugbetalingen binnen acht weken claimen vanaf de datum waarop het bedrag is afgeschreven van je rekening. Je rechten worden toegelicht in een overzicht dat je bij de bank kunt opvragen. Je gaat ermee akkoord meldingen te ontvangen voor toekomstige afschrijvingen tot twee dagen voordat deze plaatsvinden.

​​Setting up a payment method or confirming a PaymentIntent creates the accepted mandate. As the customer has implicitly signed the mandate, you must communicate these terms in your form or through email.

## Submit the payment to Stripe [Client-side]

Retrieve the client secret from the PaymentIntent you created in step 3 and call [STPPaymentHandler confirmPayment](<https://stripe.dev/stripe-ios/stripe-payments/Classes/STPPaymentHandler.html#/c:@M@StripePayments@objc(cs)STPPaymentHandler(im)confirmPayment:withAuthenticationContext:completion:>). This presents a webview where the customer can complete the payment on their bank’s website or app. Afterwards, the completion block is called with the result of the payment.

#### Swift

```swift
let paymentIntentParams = STPPaymentIntentParams(clientSecret: paymentIntentClientSecret)
paymentIntentParams.paymentMethodParams = paymentMethodParams

STPPaymentHandler.shared().confirmPayment(paymentIntentParams, with: self) { (handlerStatus, paymentIntent, error) in
    switch handlerStatus {
    case .succeeded:
        // Payment succeeded

    case .canceled:
        // Payment was cancelled

    case .failed:
        // Payment failed

    @unknown default:
        fatalError()
    }
}
```

## Charge the SEPA Direct Debit PaymentMethod later

When you need to charge your customer again, create a new PaymentIntent. Find the ID of the SEPA Direct Debit payment method by [retrieving](https://docs.stripe.com/api/payment_intents/retrieve.md) the previous PaymentIntent and [expanding](https://docs.stripe.com/api/expanding_objects.md) the `latest_charge` field where you’ll find the `generated_sepa_debit` ID inside of `payment_method_details`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.retrieve(
  "{{PAYMENT_INTENT_ID}}",
  {
    expand: ["latest_charge"],
  },
);
```

The SEPA Direct Debit payment method ID is the `generated_sepa_debit` ID under [payment_method_details](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-ideal) in the response.

#### Json

```json
{
  "latest_charge": {
    "payment_method_details": {
      "ideal": {
        "bank": "ing",
        "bic": "INGBNL2A",
        "iban_last4": "****",
        "generated_sepa_debit": "pm_1GrddXGf98efjktuBIi3ag7aJQ",
        "verified_name": "JENNY ROSEN"
      },
      "type": "ideal"
    }
  },
  "payment_method_options": {
    "ideal": {}
  },
  "payment_method_types": ["ideal"],
  "id": "pi_1G1sgdKi6xqXeNtkldRRE6HT",
  "object": "payment_intent",
  "amount": 1099,
  "client_secret": "pi_1G1sgdKi6xqXeNtkldRRE6HT_secret_h9B56ObhTN72fQiBAuzcVPb2E",
  "confirmation_method": "automatic",
  "created": 1579259303,
  "currency": "eur",
  "customer": "cus_f0Us034jfkXcl0CJQ",
  "livemode": true,
  "next_action": null
}
```

Create a `PaymentIntent` with the SEPA Direct Debit ID and the customer’s ID.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["sepa_debit"],
  amount: 1099,
  currency: "eur",
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  payment_method: "{{SEPA_DEBIT_PAYMENT_METHOD_ID}}",
  confirm: true,
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["sepa_debit"],
  amount: 1099,
  currency: "eur",
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{SEPA_DEBIT_PAYMENT_METHOD_ID}}",
  confirm: true,
});
```

## Test your integration

Use your [test API keys](https://docs.stripe.com/keys.md#test-live-modes) to confirm the PaymentIntent. After confirming, you’re redirected to a test page with options to authorize or fail the payment.

- Click **Authorize test payment** to test the case when the payment is successful. The PaymentIntent transitions from `requires_action` to `succeeded`.
- Click **Fail test payment** to test the case when the customer fails to authenticate. The PaymentIntent transitions from `requires_action` to `requires_payment_method`.

### Test your SEPA Direct Debit integration

#### Email

Set `payment_method.billing_details.email` to one of the following values to test the `PaymentIntent` status transitions. You can include your own custom text at the beginning of the email address followed by an underscore. For example, `test_1_generatedSepaDebitIntentsFail@example.com` results in a SEPA Direct Debit PaymentMethod that always fails when used with a `PaymentIntent`.

| Email Address                                                      | Description                                                                                                                       |
| ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| `generatedSepaDebitIntentsSucceed@example.com`                     | The `PaymentIntent` status transitions from `processing` to `succeeded`.                                                          |
| `generatedSepaDebitIntentsSucceedDelayed@example.com`              | The `PaymentIntent` status transitions from `processing` to `succeeded` after at least three minutes.                             |
| `generatedSepaDebitIntentsFail@example.com`                        | The `PaymentIntent` status transitions from `processing` to `requires_payment_method`.                                            |
| `generatedSepaDebitIntentsFailDelayed@example.com`                 | The `PaymentIntent` status transitions from `processing` to `requires_payment_method` after at least three minutes.               |
| `generatedSepaDebitIntentsSucceedDisputed@example.com`             | The `PaymentIntent` status transitions from `processing` to `succeeded`, but a dispute is created immediately.                    |
| `generatedSepaDebitIntentsFailsDueToInsufficientFunds@example.com` | The `PaymentIntent` status transitions from `processing` to `requires_payment_method` with the `insufficient_funds` failure code. |

#### PaymentMethod

Use these PaymentMethods to test that the `PaymentIntent` status transitions. These tokens are useful for automated testing to immediately attach the PaymentMethod to the PaymentIntent on the server.

| Payment Method                                                  | Description                                                                                                                       |
| --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `pm_ideal_generatedSepaDebitIntentsSucceed`                     | The `PaymentIntent` status transitions from `processing` to `succeeded`.                                                          |
| `pm_ideal_generatedSepaDebitIntentsSucceedDelayed`              | The `PaymentIntent` status transitions from `processing` to `succeeded` after at least three minutes.                             |
| `pm_ideal_generatedSepaDebitIntentsFail`                        | The `PaymentIntent` status transitions from `processing` to `requires_payment_method`.                                            |
| `pm_ideal_generatedSepaDebitIntentsFailDelayed`                 | The `PaymentIntent` status transitions from `processing` to `requires_payment_method` after at least three minutes.               |
| `pm_ideal_generatedSepaDebitIntentsSucceedDisputed`             | The `PaymentIntent` status transitions from `processing` to `succeeded`, but a dispute is created immediately.                    |
| `pm_ideal_generatedSepaDebitIntentsFailsDueToInsufficientFunds` | The `PaymentIntent` status transitions from `processing` to `requires_payment_method` with the `insufficient_funds` failure code. |

## Optional: Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

### Receive events and run business actions

There are a few options for receiving and running business actions.

#### Manually

Use the Stripe Dashboard to view all your Stripe payments, send email receipts, handle payouts, or retry failed payments.

- [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments)

#### Custom code

Build a webhook handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook)

#### Prebuilt apps

Handle common business events, like [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

# Android

> This is a Android for when payment-ui is mobile and platform is android. View the full page at https://docs.stripe.com/payments/ideal/save-during-payment?payment-ui=mobile&platform=android.

Accepting iDEAL | Wero payments consists of creating a [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) object to track a payment, collecting payment method details and mandate acknowledgement, and submitting the payment to Stripe for processing. Stripe uses the PaymentIntent to track and handle all the states of the payment until the payment completes. Use the ID of the SEPA Direct Debit *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) collected from your initial iDEAL | Wero PaymentIntent to create future payments.

## Set up Stripe [Server-side] [Client-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

### Server-side

This integration requires endpoints on your server that talk to the Stripe API. Use the official libraries for access to the Stripe API from your server:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

### Client-side

The [Stripe Android SDK](https://github.com/stripe/stripe-android) is open source and [fully documented](https://stripe.dev/stripe-android/).

To install the SDK, add `stripe-android` to the `dependencies` block of your [app/build.gradle](https://developer.android.com/studio/build/dependencies) file:

#### Kotlin

```kotlin
plugins {
    id("com.android.application")
}

android { ... }

dependencies {
  // ...

  // Stripe Android SDK
  implementation("com.stripe:stripe-android:23.5.0")
  // Include the financial connections SDK to support US bank account as a payment method
  implementation("com.stripe:financial-connections:23.5.0")
}
```

> For details on the latest SDK release and past versions, see the [Releases](https://github.com/stripe/stripe-android/releases) page on GitHub. To receive notifications when a new release is published, [watch releases for the repository](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/configuring-notifications#configuring-your-watch-settings-for-an-individual-repository).

Configure the SDK with your Stripe [publishable key](https://dashboard.stripe.com/apikeys) so that it can make requests to the Stripe API, such as in your `Application` subclass:

#### Kotlin

```kotlin
import com.stripe.android.PaymentConfiguration

class MyApp : Application() {
    override fun onCreate() {
        super.onCreate()
        PaymentConfiguration.init(
            applicationContext,
            "<<YOUR_PUBLISHABLE_KEY>>"
        )
    }
}
```

> Use your [test keys](https://docs.stripe.com/keys.md#obtain-api-keys) while you test and develop, and your [live mode](https://docs.stripe.com/keys.md#test-live-modes) keys when you publish your app.

Stripe samples also use [OkHttp](https://github.com/square/okhttp) and [GSON](https://github.com/google/gson) to make HTTP requests to a server.

## Create a Customer [Server-side]

Create a *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) when they create an account with your business and associate it with your internal representation of their account. This enables you to retrieve and use their saved payment method details later.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create();
```

## Create a PaymentIntent [Server-side]

Create a `PaymentIntent` on your server and specify the `amount` to collect, the `eur` currency, the customer ID, and `off_session` as an argument for [setup future usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage). There is no minimum charge amount and iDEAL | Wero doesn’t support other currencies. If you have an existing [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md) integration, add `ideal` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  payment_method_types: ["ideal"],
  customer: "{{CUSTOMER_ID}}",
  setup_future_usage: "off_session",
});
```

The PaymentIntent includes the payment method ID and a *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)), which is used on the client side to securely complete the payment process instead of passing the entire PaymentIntent object.

## Collect payment method details and mandate acknowledgement [Client-side]

In your app, collect your customer’s full name and email address. Create a [PaymentMethodCreateParams](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-payment-method-create-params/index.html) object with these details.

#### Kotlin

```kotlin
val billingDetails = PaymentMethod.BillingDetails(name = "Jenny Rosen", email = "jenny.rosen@example.com")
val ideal = PaymentMethodCreateParams.Ideal(null)
val paymentMethodCreateParams = PaymentMethodCreateParams.create(ideal, billingDetails)
```

​​To process SEPA Direct Debit payments, you must collect a mandate agreement from your customer. Display the following standard authorization text for your customer to implicitly sign the mandate.

Replace *Rocket Rides* with your company name.

#### de

Durch Angabe Ihrer Zahlungsinformationen und der Bestätigung der vorliegenden Zahlung ermächtigen Sie (A) und Stripe, unseren Zahlungsdienstleister, Ihrem Kreditinstitut Anweisungen zur Belastung Ihres Kontos zu erteilen, und (B) Ihr Kreditinstitut, Ihr Konto gemäß diesen Anweisungen zu belasten. Im Rahmen Ihrer Rechte haben Sie, entsprechend den Vertragsbedingungen mit Ihrem Kreditinstitut, Anspruch auf eine Rückerstattung von Ihrem Kreditinstitut. Eine Rückerstattung muss innerhalb von 8 Wochen ab dem Tag, an dem Ihr Konto belastet wurde, geltend gemacht werden. Eine Erläuterung Ihrer Rechte können Sie von Ihrem Kreditinstitut anfordern. Sie erklären sich einverstanden, Benachrichtigungen über künftige Belastungen bis spätestens 2 Tage vor dem Buchungsdatum zu erhalten.

#### en

By providing your payment information and confirming this payment, you authorise (A) and Stripe, our payment service provider, to send instructions to your bank to debit your account and (B) your bank to debit your account in accordance with those instructions. As part of your rights, you’re entitled to a refund from your bank under the terms and conditions of your agreement with your bank. A refund must be claimed within 8 weeks starting from the date on which your account was debited. Your rights are explained in a statement that you can obtain from your bank. You agree to receive notifications for future debits up to 2 days before they occur.

#### es

Al proporcionar sus datos de pago y confirmar este pago, usted autoriza a (A) y Stripe, nuestro proveedor de servicios de pago, a enviar instrucciones a su banco para realizar un débito en su cuenta y (B) a su banco a realizar un cargo en su cuenta de conformidad con dichas instrucciones. Como parte de sus derechos, usted tiene derecho a un reembolso de su banco conforme a los términos y condiciones del contrato con su banco. El reembolso debe reclamarse en un plazo de 8 semanas a partir de la fecha en la que se haya efectuado el cargo en su cuenta. Sus derechos se explican en un extracto que puede obtener en su banco. Usted acepta recibir notificaciones de futuros débitos hasta 2 días antes de que se produzcan.

#### fi

Antamalla maksutiedot ja vahvistamalla tämän maksun, valtuutat (A) ja Stripen, maksupalveluntarjoajamme, lähettämään ohjeet pankille tilisi veloittamiseksi ja (B) pankkisi veloittamaan tiliäsi kyseisten ohjeiden mukaisesti. Oikeuksiesi mukaisesti olet oikeutettu maksun palautukseen pankilta, kuten heidän kanssaan tekemässäsi sopimuksessa ja sen ehdoissa on kuvattu. Maksun palautus on lunastettava 8 viikon aikana alkaen päivästä, jolloin tiliäsi veloitettiin. Oikeutesi on selitetty pankilta saatavissa olevassa lausunnossa. Hyväksyt vastaanottamaan ilmoituksia tulevista veloituksista jopa kaksi päivää ennen niiden tapahtumista.

#### fr

En fournissant vos informations de paiement et en confirmant ce paiement, vous autorisez (A) et Stripe, notre prestataire de services de paiement et/ou PPRO, son prestataire de services local, à envoyer des instructions à votre banque pour débiter votre compte et (B) votre banque à débiter votre compte conformément à ces instructions. Vous avez, entre autres, le droit de vous faire rembourser par votre banque selon les modalités et conditions du contrat conclu avec votre banque. La demande de remboursement doit être soumise dans un délai de 8 semaines à compter de la date à laquelle votre compte a été débité. Vos droits sont expliqués dans une déclaration disponible auprès de votre banque. Vous acceptez de recevoir des notifications des débits à venir dans les 2 jours précédant leur réalisation.

#### it

Fornendo i dati di pagamento e confermando il pagamento, l’utente autorizza (A) e Stripe, il fornitore del servizio di pagamento locale, a inviare alla sua banca le istruzioni per eseguire addebiti sul suo conto e (B) la sua banca a effettuare addebiti conformemente a tali istruzioni. L’utente, fra le altre cose, ha diritto a un rimborso dalla banca, in base a termini e condizioni dell’accordo sottoscritto con l’istituto. Il rimborso va richiesto entro otto settimane dalla data dell’addebito sul conto. I diritti dell’utente sono illustrati in una comunicazione riepilogativa che è possibile richiedere alla banca. L’utente accetta di ricevere notifiche per i futuri addebiti fino a due giorni prima che vengano effettuati.

#### nl

Door je betaalgegevens door te geven en deze betaling te bevestigen, geef je (A) en Stripe, onze betaaldienst, toestemming om instructies naar je bank te verzenden om het bedrag van je rekening af te schrijven, en (B) geef je je bank toestemming om het bedrag van je rekening af te schrijven conform deze aanwijzingen. Als onderdeel van je rechten kom je in aanmerking voor een terugbetaling van je bank conform de voorwaarden van je overeenkomst met de bank. Je moet terugbetalingen binnen acht weken claimen vanaf de datum waarop het bedrag is afgeschreven van je rekening. Je rechten worden toegelicht in een overzicht dat je bij de bank kunt opvragen. Je gaat ermee akkoord meldingen te ontvangen voor toekomstige afschrijvingen tot twee dagen voordat deze plaatsvinden.

​​Setting up a payment method or confirming a PaymentIntent creates the accepted mandate. As the customer has implicitly signed the mandate, you must communicate these terms in your form or through email.

## Submit the payment to Stripe [Client-side]

Retrieve the client secret from the PaymentIntent you created in step 3 and call the [stripe confirmPayment](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-stripe/index.html#com.stripe.android/Stripe/confirmPayment/#android.app.Activity#com.stripe.android.model.ConfirmPaymentIntentParams#kotlin.String?/PointingToDeclaration/) method. This presents a webview where the customer can complete the payment on their bank’s website or app. Afterwards, `onActivityResult` is called with the result of the payment.

#### Kotlin

```kotlin
class IdealPaymentActivity : AppCompatActivity() {
    // ...
    private lateinit var paymentIntentClientSecret: String
    private val stripe: Stripe by lazy {
        Stripe(
            applicationContext,
            PaymentConfiguration.getInstance(applicationContext).publishableKey
        )
    }

    private fun startCheckout() {
        // ...

        val confirmParams = ConfirmPaymentIntentParams
                .createWithPaymentMethodCreateParams(
                  paymentMethodCreateParams = paymentMethodCreateParams,
                  clientSecret = paymentIntentClientSecret
                )
        stripe.confirmPayment(this, confirmParams)
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)

        // Handle the result of stripe.confirmPayment
        if (stripe.isPaymentResult(requestCode, data)) {
            lifecycleScope.launch {
                runCatching {
                    stripe.getPaymentIntentResult(requestCode, data!!).intent
                }.fold(
                    onSuccess = { paymentIntent ->
                        val status = paymentIntent.status
                        when (status) {
                            StripeIntent.Status.Succeeded -> {
                                // Payment succeeded
                            }
                            else -> {
                                // Payment failed/canceled
                            }
                        }
                    },
                    onFailure = {
                        // Payment failed
                    }
                )
            }
        }
    }
}
```

## Charge the SEPA Direct Debit PaymentMethod later

When you need to charge your customer again, create a new PaymentIntent. Find the ID of the SEPA Direct Debit payment method by [retrieving](https://docs.stripe.com/api/payment_intents/retrieve.md) the previous PaymentIntent and [expanding](https://docs.stripe.com/api/expanding_objects.md) the `latest_charge` field where you’ll find the `generated_sepa_debit` ID inside of `payment_method_details`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.retrieve(
  "{{PAYMENT_INTENT_ID}}",
  {
    expand: ["latest_charge"],
  },
);
```

The SEPA Direct Debit payment method ID is the `generated_sepa_debit` ID under [payment_method_details](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-ideal) in the response.

#### Json

```json
{
  "latest_charge": {
    "payment_method_details": {
      "ideal": {
        "bank": "ing",
        "bic": "INGBNL2A",
        "iban_last4": "****",
        "generated_sepa_debit": "pm_1GrddXGf98efjktuBIi3ag7aJQ",
        "verified_name": "JENNY ROSEN"
      },
      "type": "ideal"
    }
  },
  "payment_method_options": {
    "ideal": {}
  },
  "payment_method_types": ["ideal"],
  "id": "pi_1G1sgdKi6xqXeNtkldRRE6HT",
  "object": "payment_intent",
  "amount": 1099,
  "client_secret": "pi_1G1sgdKi6xqXeNtkldRRE6HT_secret_h9B56ObhTN72fQiBAuzcVPb2E",
  "confirmation_method": "automatic",
  "created": 1579259303,
  "currency": "eur",
  "customer": "cus_f0Us034jfkXcl0CJQ",
  "livemode": true,
  "next_action": null
}
```

Create a `PaymentIntent` with the SEPA Direct Debit ID and the customer’s ID.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["sepa_debit"],
  amount: 1099,
  currency: "eur",
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  payment_method: "{{SEPA_DEBIT_PAYMENT_METHOD_ID}}",
  confirm: true,
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["sepa_debit"],
  amount: 1099,
  currency: "eur",
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{SEPA_DEBIT_PAYMENT_METHOD_ID}}",
  confirm: true,
});
```

## Test your integration

Use your [test API keys](https://docs.stripe.com/keys.md#test-live-modes) to confirm the PaymentIntent. After confirming, you’re redirected to a test page with options to authorize or fail the payment.

- Click **Authorize test payment** to test the case when the payment is successful. The PaymentIntent transitions from `requires_action` to `succeeded`.
- Click **Fail test payment** to test the case when the customer fails to authenticate. The PaymentIntent transitions from `requires_action` to `requires_payment_method`.

### Test your SEPA Direct Debit integration

#### Email

Set `payment_method.billing_details.email` to one of the following values to test the `PaymentIntent` status transitions. You can include your own custom text at the beginning of the email address followed by an underscore. For example, `test_1_generatedSepaDebitIntentsFail@example.com` results in a SEPA Direct Debit PaymentMethod that always fails when used with a `PaymentIntent`.

| Email Address                                                      | Description                                                                                                                       |
| ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| `generatedSepaDebitIntentsSucceed@example.com`                     | The `PaymentIntent` status transitions from `processing` to `succeeded`.                                                          |
| `generatedSepaDebitIntentsSucceedDelayed@example.com`              | The `PaymentIntent` status transitions from `processing` to `succeeded` after at least three minutes.                             |
| `generatedSepaDebitIntentsFail@example.com`                        | The `PaymentIntent` status transitions from `processing` to `requires_payment_method`.                                            |
| `generatedSepaDebitIntentsFailDelayed@example.com`                 | The `PaymentIntent` status transitions from `processing` to `requires_payment_method` after at least three minutes.               |
| `generatedSepaDebitIntentsSucceedDisputed@example.com`             | The `PaymentIntent` status transitions from `processing` to `succeeded`, but a dispute is created immediately.                    |
| `generatedSepaDebitIntentsFailsDueToInsufficientFunds@example.com` | The `PaymentIntent` status transitions from `processing` to `requires_payment_method` with the `insufficient_funds` failure code. |

#### PaymentMethod

Use these PaymentMethods to test that the `PaymentIntent` status transitions. These tokens are useful for automated testing to immediately attach the PaymentMethod to the PaymentIntent on the server.

| Payment Method                                                  | Description                                                                                                                       |
| --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `pm_ideal_generatedSepaDebitIntentsSucceed`                     | The `PaymentIntent` status transitions from `processing` to `succeeded`.                                                          |
| `pm_ideal_generatedSepaDebitIntentsSucceedDelayed`              | The `PaymentIntent` status transitions from `processing` to `succeeded` after at least three minutes.                             |
| `pm_ideal_generatedSepaDebitIntentsFail`                        | The `PaymentIntent` status transitions from `processing` to `requires_payment_method`.                                            |
| `pm_ideal_generatedSepaDebitIntentsFailDelayed`                 | The `PaymentIntent` status transitions from `processing` to `requires_payment_method` after at least three minutes.               |
| `pm_ideal_generatedSepaDebitIntentsSucceedDisputed`             | The `PaymentIntent` status transitions from `processing` to `succeeded`, but a dispute is created immediately.                    |
| `pm_ideal_generatedSepaDebitIntentsFailsDueToInsufficientFunds` | The `PaymentIntent` status transitions from `processing` to `requires_payment_method` with the `insufficient_funds` failure code. |

## Optional: Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

### Receive events and run business actions

There are a few options for receiving and running business actions.

#### Manually

Use the Stripe Dashboard to view all your Stripe payments, send email receipts, handle payouts, or retry failed payments.

- [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments)

#### Custom code

Build a webhook handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook)

#### Prebuilt apps

Handle common business events, like [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

# React Native

> This is a React Native for when payment-ui is mobile and platform is react-native. View the full page at https://docs.stripe.com/payments/ideal/save-during-payment?payment-ui=mobile&platform=react-native.

Accepting iDEAL | Wero payments consists of creating a [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) object to track a payment, collecting payment method details and mandate acknowledgement, and submitting the payment to Stripe for processing. Stripe uses the PaymentIntent to track and handle all the states of the payment until the payment completes. Use the ID of the SEPA Direct Debit *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) collected from your initial iDEAL | Wero PaymentIntent to create future payments.

## Set up Stripe [Server-side] [Client-side]

### Server-side

This integration requires endpoints on your server that talk to the Stripe API. Use our official libraries for access to the Stripe API from your server:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

### Client-side

The [React Native SDK](https://github.com/stripe/stripe-react-native) is open source and fully documented. Internally, it uses the [native iOS](https://github.com/stripe/stripe-ios) and [Android](https://github.com/stripe/stripe-android) SDKs. To install Stripe’s React Native SDK, run one of the following commands in your project’s directory (depending on which package manager you use):

#### yarn

```bash
yarn add @stripe/stripe-react-native
```

#### npm

```bash
npm install @stripe/stripe-react-native
```

Next, install some other necessary dependencies:

- For iOS, go to the **ios** directory and run `pod install` to ensure that you also install the required native dependencies.
- For Android, there are no more dependencies to install.

> We recommend following the [official TypeScript guide](https://reactnative.dev/docs/typescript#adding-typescript-to-an-existing-project) to add TypeScript support.

### Stripe initialization

To initialize Stripe in your React Native app, either wrap your payment screen with the `StripeProvider` component, or use the `initStripe` initialization method. Only the API [publishable key](https://docs.stripe.com/keys.md#obtain-api-keys) in `publishableKey` is required. The following example shows how to initialize Stripe using the `StripeProvider` component.

```jsx
import { useState, useEffect } from "react";
import { StripeProvider } from "@stripe/stripe-react-native";

function App() {
  const [publishableKey, setPublishableKey] = useState("");

  const fetchPublishableKey = async () => {
    const key = await fetchKey(); // fetch key from your server here
    setPublishableKey(key);
  };

  useEffect(() => {
    fetchPublishableKey();
  }, []);

  return (
    <StripeProvider
      publishableKey={publishableKey}
      merchantIdentifier="merchant.identifier" // required for Apple Pay
      urlScheme="your-url-scheme" // required for 3D Secure and bank redirects
    >
      {/* Your app code here */}
    </StripeProvider>
  );
}
```

> Use your API [test keys](https://docs.stripe.com/keys.md#obtain-api-keys) while you test and develop, and your [live mode](https://docs.stripe.com/keys.md#test-live-modes) keys when you publish your app.

## Create a Customer [Server-side]

Create a *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) when they create an account with your business and associate it with your internal representation of their account. This enables you to retrieve and use their saved payment method details later.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create();
```

## Create a PaymentIntent [Server-side]

Create a `PaymentIntent` on your server and specify the `amount` to collect, the `eur` currency, the customer ID, and `off_session` as an argument for [setup future usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage). There is no minimum charge amount and iDEAL | Wero doesn’t support other currencies. If you have an existing [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md) integration, add `ideal` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  payment_method_types: ["ideal"],
  customer: "{{CUSTOMER_ID}}",
  setup_future_usage: "off_session",
});
```

The PaymentIntent includes the payment method ID and a *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)), which is used on the client side to securely complete the payment process instead of passing the entire PaymentIntent object.

## Collect payment method details and mandate acknowledgement [Client-side]

In your app, collect your customer’s full name and email address.

```javascript
export default function IdealPaymentScreen() {
  const [name, setName] = useState();
  const [email, setEmai] = useState();

  const handlePayPress = async () => {
    // ...
  };

  return (
    <Screen>
      <TextInput
        placeholder="Email"
        onChange={(value) => setEmail(value.nativeEvent.text)}
      />
      <TextInput
        placeholder="Name"
        onChange={(value) => setName(value.nativeEvent.text)}
      />
    </Screen>
  );
}
```

​​To process SEPA Direct Debit payments, you must collect a mandate agreement from your customer. Display the following standard authorization text for your customer to implicitly sign the mandate.

Replace *Rocket Rides* with your company name.

#### de

Durch Angabe Ihrer Zahlungsinformationen und der Bestätigung der vorliegenden Zahlung ermächtigen Sie (A) und Stripe, unseren Zahlungsdienstleister, Ihrem Kreditinstitut Anweisungen zur Belastung Ihres Kontos zu erteilen, und (B) Ihr Kreditinstitut, Ihr Konto gemäß diesen Anweisungen zu belasten. Im Rahmen Ihrer Rechte haben Sie, entsprechend den Vertragsbedingungen mit Ihrem Kreditinstitut, Anspruch auf eine Rückerstattung von Ihrem Kreditinstitut. Eine Rückerstattung muss innerhalb von 8 Wochen ab dem Tag, an dem Ihr Konto belastet wurde, geltend gemacht werden. Eine Erläuterung Ihrer Rechte können Sie von Ihrem Kreditinstitut anfordern. Sie erklären sich einverstanden, Benachrichtigungen über künftige Belastungen bis spätestens 2 Tage vor dem Buchungsdatum zu erhalten.

#### en

By providing your payment information and confirming this payment, you authorise (A) and Stripe, our payment service provider, to send instructions to your bank to debit your account and (B) your bank to debit your account in accordance with those instructions. As part of your rights, you’re entitled to a refund from your bank under the terms and conditions of your agreement with your bank. A refund must be claimed within 8 weeks starting from the date on which your account was debited. Your rights are explained in a statement that you can obtain from your bank. You agree to receive notifications for future debits up to 2 days before they occur.

#### es

Al proporcionar sus datos de pago y confirmar este pago, usted autoriza a (A) y Stripe, nuestro proveedor de servicios de pago, a enviar instrucciones a su banco para realizar un débito en su cuenta y (B) a su banco a realizar un cargo en su cuenta de conformidad con dichas instrucciones. Como parte de sus derechos, usted tiene derecho a un reembolso de su banco conforme a los términos y condiciones del contrato con su banco. El reembolso debe reclamarse en un plazo de 8 semanas a partir de la fecha en la que se haya efectuado el cargo en su cuenta. Sus derechos se explican en un extracto que puede obtener en su banco. Usted acepta recibir notificaciones de futuros débitos hasta 2 días antes de que se produzcan.

#### fi

Antamalla maksutiedot ja vahvistamalla tämän maksun, valtuutat (A) ja Stripen, maksupalveluntarjoajamme, lähettämään ohjeet pankille tilisi veloittamiseksi ja (B) pankkisi veloittamaan tiliäsi kyseisten ohjeiden mukaisesti. Oikeuksiesi mukaisesti olet oikeutettu maksun palautukseen pankilta, kuten heidän kanssaan tekemässäsi sopimuksessa ja sen ehdoissa on kuvattu. Maksun palautus on lunastettava 8 viikon aikana alkaen päivästä, jolloin tiliäsi veloitettiin. Oikeutesi on selitetty pankilta saatavissa olevassa lausunnossa. Hyväksyt vastaanottamaan ilmoituksia tulevista veloituksista jopa kaksi päivää ennen niiden tapahtumista.

#### fr

En fournissant vos informations de paiement et en confirmant ce paiement, vous autorisez (A) et Stripe, notre prestataire de services de paiement et/ou PPRO, son prestataire de services local, à envoyer des instructions à votre banque pour débiter votre compte et (B) votre banque à débiter votre compte conformément à ces instructions. Vous avez, entre autres, le droit de vous faire rembourser par votre banque selon les modalités et conditions du contrat conclu avec votre banque. La demande de remboursement doit être soumise dans un délai de 8 semaines à compter de la date à laquelle votre compte a été débité. Vos droits sont expliqués dans une déclaration disponible auprès de votre banque. Vous acceptez de recevoir des notifications des débits à venir dans les 2 jours précédant leur réalisation.

#### it

Fornendo i dati di pagamento e confermando il pagamento, l’utente autorizza (A) e Stripe, il fornitore del servizio di pagamento locale, a inviare alla sua banca le istruzioni per eseguire addebiti sul suo conto e (B) la sua banca a effettuare addebiti conformemente a tali istruzioni. L’utente, fra le altre cose, ha diritto a un rimborso dalla banca, in base a termini e condizioni dell’accordo sottoscritto con l’istituto. Il rimborso va richiesto entro otto settimane dalla data dell’addebito sul conto. I diritti dell’utente sono illustrati in una comunicazione riepilogativa che è possibile richiedere alla banca. L’utente accetta di ricevere notifiche per i futuri addebiti fino a due giorni prima che vengano effettuati.

#### nl

Door je betaalgegevens door te geven en deze betaling te bevestigen, geef je (A) en Stripe, onze betaaldienst, toestemming om instructies naar je bank te verzenden om het bedrag van je rekening af te schrijven, en (B) geef je je bank toestemming om het bedrag van je rekening af te schrijven conform deze aanwijzingen. Als onderdeel van je rechten kom je in aanmerking voor een terugbetaling van je bank conform de voorwaarden van je overeenkomst met de bank. Je moet terugbetalingen binnen acht weken claimen vanaf de datum waarop het bedrag is afgeschreven van je rekening. Je rechten worden toegelicht in een overzicht dat je bij de bank kunt opvragen. Je gaat ermee akkoord meldingen te ontvangen voor toekomstige afschrijvingen tot twee dagen voordat deze plaatsvinden.

​​Setting up a payment method or confirming a PaymentIntent creates the accepted mandate. As the customer has implicitly signed the mandate, you must communicate these terms in your form or through email.

## Submit the payment to Stripe [Client-side]

Retrieve the client secret from the PaymentIntent you created and call `confirmPayment`. This presents a webview where the customer can complete the payment on their bank’s website or app. Afterwards, the promise resolves with the result of the payment.

```javascript
export default function IdealPaymentScreen() {
  const [name, setName] = useState();
  const [email, setEmai] = useState();

  const handlePayPress = async () => {
    const billingDetails: PaymentMethodCreateParams.BillingDetails = {
      name: 'Jenny Rosen',
      email: 'jenny.rosen@example.com',
    };
  };

  const { error, paymentIntent } = await confirmPayment(clientSecret, {
    paymentMethodType: 'Ideal',
    paymentMethodData: {
      billingDetails,
    }
  });

  if (error) {
    Alert.alert(`Error code: ${error.code}`, error.message);
  } else if (paymentIntent) {
    Alert.alert(
      'Success',
      `The payment was confirmed successfully! currency: ${paymentIntent.currency}`
    );
  }

    return <Screen>{/* ... */}</Screen>;
}
```

## Charge the SEPA Direct Debit PaymentMethod later

When you need to charge your customer again, create a new PaymentIntent. Find the ID of the SEPA Direct Debit payment method by [retrieving](https://docs.stripe.com/api/payment_intents/retrieve.md) the previous PaymentIntent and [expanding](https://docs.stripe.com/api/expanding_objects.md) the `latest_charge` field where you’ll find the `generated_sepa_debit` ID inside of `payment_method_details`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.retrieve(
  "{{PAYMENT_INTENT_ID}}",
  {
    expand: ["latest_charge"],
  },
);
```

The SEPA Direct Debit payment method ID is the `generated_sepa_debit` ID under [payment_method_details](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-ideal) in the response.

#### Json

```json
{
  "latest_charge": {
    "payment_method_details": {
      "ideal": {
        "bank": "ing",
        "bic": "INGBNL2A",
        "iban_last4": "****",
        "generated_sepa_debit": "pm_1GrddXGf98efjktuBIi3ag7aJQ",
        "verified_name": "JENNY ROSEN"
      },
      "type": "ideal"
    }
  },
  "payment_method_options": {
    "ideal": {}
  },
  "payment_method_types": ["ideal"],
  "id": "pi_1G1sgdKi6xqXeNtkldRRE6HT",
  "object": "payment_intent",
  "amount": 1099,
  "client_secret": "pi_1G1sgdKi6xqXeNtkldRRE6HT_secret_h9B56ObhTN72fQiBAuzcVPb2E",
  "confirmation_method": "automatic",
  "created": 1579259303,
  "currency": "eur",
  "customer": "cus_f0Us034jfkXcl0CJQ",
  "livemode": true,
  "next_action": null
}
```

Create a `PaymentIntent` with the SEPA Direct Debit ID and the customer’s ID.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["sepa_debit"],
  amount: 1099,
  currency: "eur",
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  payment_method: "{{SEPA_DEBIT_PAYMENT_METHOD_ID}}",
  confirm: true,
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["sepa_debit"],
  amount: 1099,
  currency: "eur",
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{SEPA_DEBIT_PAYMENT_METHOD_ID}}",
  confirm: true,
});
```

## Test your integration

Use your [test API keys](https://docs.stripe.com/keys.md#test-live-modes) to confirm the PaymentIntent. After confirming, you’re redirected to a test page with options to authorize or fail the payment.

- Click **Authorize test payment** to test the case when the payment is successful. The PaymentIntent transitions from `requires_action` to `succeeded`.
- Click **Fail test payment** to test the case when the customer fails to authenticate. The PaymentIntent transitions from `requires_action` to `requires_payment_method`.

### Test your SEPA Direct Debit integration

#### Email

Set `payment_method.billing_details.email` to one of the following values to test the `PaymentIntent` status transitions. You can include your own custom text at the beginning of the email address followed by an underscore. For example, `test_1_generatedSepaDebitIntentsFail@example.com` results in a SEPA Direct Debit PaymentMethod that always fails when used with a `PaymentIntent`.

| Email Address                                                      | Description                                                                                                                       |
| ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| `generatedSepaDebitIntentsSucceed@example.com`                     | The `PaymentIntent` status transitions from `processing` to `succeeded`.                                                          |
| `generatedSepaDebitIntentsSucceedDelayed@example.com`              | The `PaymentIntent` status transitions from `processing` to `succeeded` after at least three minutes.                             |
| `generatedSepaDebitIntentsFail@example.com`                        | The `PaymentIntent` status transitions from `processing` to `requires_payment_method`.                                            |
| `generatedSepaDebitIntentsFailDelayed@example.com`                 | The `PaymentIntent` status transitions from `processing` to `requires_payment_method` after at least three minutes.               |
| `generatedSepaDebitIntentsSucceedDisputed@example.com`             | The `PaymentIntent` status transitions from `processing` to `succeeded`, but a dispute is created immediately.                    |
| `generatedSepaDebitIntentsFailsDueToInsufficientFunds@example.com` | The `PaymentIntent` status transitions from `processing` to `requires_payment_method` with the `insufficient_funds` failure code. |

#### PaymentMethod

Use these PaymentMethods to test that the `PaymentIntent` status transitions. These tokens are useful for automated testing to immediately attach the PaymentMethod to the PaymentIntent on the server.

| Payment Method                                                  | Description                                                                                                                       |
| --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `pm_ideal_generatedSepaDebitIntentsSucceed`                     | The `PaymentIntent` status transitions from `processing` to `succeeded`.                                                          |
| `pm_ideal_generatedSepaDebitIntentsSucceedDelayed`              | The `PaymentIntent` status transitions from `processing` to `succeeded` after at least three minutes.                             |
| `pm_ideal_generatedSepaDebitIntentsFail`                        | The `PaymentIntent` status transitions from `processing` to `requires_payment_method`.                                            |
| `pm_ideal_generatedSepaDebitIntentsFailDelayed`                 | The `PaymentIntent` status transitions from `processing` to `requires_payment_method` after at least three minutes.               |
| `pm_ideal_generatedSepaDebitIntentsSucceedDisputed`             | The `PaymentIntent` status transitions from `processing` to `succeeded`, but a dispute is created immediately.                    |
| `pm_ideal_generatedSepaDebitIntentsFailsDueToInsufficientFunds` | The `PaymentIntent` status transitions from `processing` to `requires_payment_method` with the `insufficient_funds` failure code. |

## Optional: Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

### Receive events and run business actions

There are a few options for receiving and running business actions.

#### Manually

Use the Stripe Dashboard to view all your Stripe payments, send email receipts, handle payouts, or retry failed payments.

- [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments)

#### Custom code

Build a webhook handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook)

#### Prebuilt apps

Handle common business events, like [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

## Optional: Handle deep linking

When a customer exits your app (for example to authenticate in Safari or their banking app), provide a way for them to automatically return to your app. Many payment method types *require* a return URL. If you don’t provide one, we can’t present payment methods that require a return URL to your users, even if you’ve enabled them.

To provide a return URL:

1. [Register](https://developer.apple.com/documentation/xcode/defining-a-custom-url-scheme-for-your-app#Register-your-URL-scheme) a custom URL. Universal links aren’t supported.
1. [Configure](https://reactnative.dev/docs/linking) your custom URL.
1. Set up your root component to forward the URL to the Stripe SDK as shown below.

> If you’re using Expo, [set your scheme](https://docs.expo.io/guides/linking/#in-a-standalone-app) in the `app.json` file.

```jsx
import { useEffect, useCallback } from 'react';
import { Linking } from 'react-native';
import { useStripe } from '@stripe/stripe-react-native';

export default function MyApp() {
  const { handleURLCallback } = useStripe();

  const handleDeepLink = useCallback(
    async (url: string | null) => {
      if (url) {
        const stripeHandled = await handleURLCallback(url);
        if (stripeHandled) {
          // This was a Stripe URL - you can return or add extra handling here as you see fit
        } else {
          // This was NOT a Stripe URL – handle as you normally would
        }
      }
    },
    [handleURLCallback]
  );

  useEffect(() => {
    const getUrlAsync = async () => {
      const initialUrl = await Linking.getInitialURL();
      handleDeepLink(initialUrl);
    };

    getUrlAsync();

    const deepLinkListener = Linking.addEventListener(
      'url',
      (event: { url: string }) => {
        handleDeepLink(event.url);
      }
    );

    return () => deepLinkListener.remove();
  }, [handleDeepLink]);

  return (
    <View>
      <AwesomeAppComponent />
    </View>
  );
}
```

For more information on native URL schemes, refer to the [Android](https://developer.android.com/training/app-links/deep-linking) and [iOS](https://developer.apple.com/documentation/xcode/allowing_apps_and_websites_to_link_to_your_content/defining_a_custom_url_scheme_for_your_app) docs.

## See also

- [Accept a SEPA Direct Debit payment](https://docs.stripe.com/payments/sepa-debit/accept-a-payment.md)
- [Set up a subscription with SEPA Direct Debit in the EU](https://docs.stripe.com/billing/subscriptions/sepa-debit.md)
