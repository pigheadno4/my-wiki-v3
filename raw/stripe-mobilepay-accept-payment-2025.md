<!-- Source URL: https://docs.stripe.com/payments/mobilepay/accept-a-payment -->
<!-- Fetched: 2026-05-07 -->

# MobilePay payments

Learn how to accept MobilePay, a popular payment method in Denmark and Finland.

# Checkout

> This is a Checkout for when payment-ui is checkout. View the full page at https://docs.stripe.com/payments/mobilepay/accept-a-payment?payment-ui=checkout.

MobilePay is a [single-use](https://docs.stripe.com/payments/payment-methods.md#usage) card wallet payment method used in Denmark and Finland. It allows your customer to [authenticate and approve](https://docs.stripe.com/payments/payment-methods.md#customer-actions) payments using the MobilePay app.

When your customer pays with MobilePay, Stripe performs a card transaction using the card data we receive from MobilePay. The processing of the card transaction is invisible to your integration, and Stripe [immediately notifies you](https://docs.stripe.com/payments/payment-methods.md#payment-notification) whether the payment succeeded or failed.

> Stripe can automatically present the relevant payment methods to your customers by evaluating currency, payment method restrictions, and other parameters.
>
> - Follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=checkout&ui=stripe-hosted) guide to build a Checkout integration that uses [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md).

- If you don’t want to use dynamic payment methods, follow the steps below to manually configure the payment methods in your Checkout integration.

Use this guide to enable MobilePay on [Checkout](https://docs.stripe.com/payments/checkout.md), our hosted checkout form, and learn the differences between accepting payments using dynamic payment methods and manually configuring payment methods.

## Determine compatibility

**Supported business locations**: EEA

**Supported currencies**: `eur, dkk, sek, nok`

**Presentment currencies**: `eur, dkk, sek, nok`

**Payment mode**: Yes

**Setup mode**: No

**Subscription mode**: No

A Checkout Session must satisfy all of the following conditions to support MobilePay payments:

- *Prices* (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) for all line items must be expressed in Euro, Danish Krona, Swedish Krona or Norwegian Krona (currency codes `eur`, `dkk`, `sek` or `nok`).

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Accept a payment

> This guide builds on the foundational [accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?integration=checkout) Checkout integration.

### Enable MobilePay as a payment method

When creating a new [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md), you need to:

1. Add `mobilepay` to the list of `payment_method_types`.
1. Make sure all your `line_items` use the `eur`, `dkk`, `sek` or `nok` currency.

#### Stripe-hosted page

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        currency: "dkk",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "mobilepay"],
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
        currency: "dkk",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "mobilepay"],
  return_url: "https://example.com/return",
  ui_mode: "embedded_page",
});
```

### Fulfill your orders

After accepting a payment, learn how to [fulfill orders](https://docs.stripe.com/checkout/fulfillment.md).

## Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

- **Handle events manually in the Dashboard**

  Use the Dashboard to [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments), send email receipts, handle payouts, or retry failed payments.

- **Build a custom webhook**

  [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook) handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- **Integrate a prebuilt app**

  Handle common business events, such as [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

## Test the integration

#### Mobile web app testing

To test your integration, choose MobilePay as the payment method and tap **Pay**. In a testing environment, this redirects you to a test payment page where you can approve or decline the payment.

In live mode, tapping **Pay** redirects you to the MobilePay mobile application, where you can approve or decline the payment.

#### Desktop web app testing

To test your integration in a testing environment, this redirects you to a test payment page where you can approve or decline the test payment.

In live mode, enter the phone number linked to MobilePay to send a push notification to your MobilePay mobile application. You can approve or decline the payment in the MobilePay mobile application.

## Optional: Authorize a payment and then capture later

MobilePay supports [separate authorization and capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md).

### Tell Stripe to authorize only

To indicate that you want separate authorization and capture, set [capture_method](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_intent_data-capture_method) to `manual` when creating the Checkout Session. This parameter instructs Stripe to only authorize the amount on the customer’s card linked to MobilePay.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  mode: "payment",
  payment_method_types: ["card", "mobilepay"],
  line_items: [
    {
      price_data: {
        currency: "dkk",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  payment_intent_data: {
    capture_method: "manual",
  },
  success_url: "https://example.com/success.html",
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

You can cancel MobilePay payments before they expire by [canceling the PaymentIntent](https://docs.stripe.com/api/payment_intents/cancel.md) associated with the MobilePay payment.

## Failed payments

MobilePay transactions can fail if the underlying card transaction is declined. Learn more about [card declines](https://docs.stripe.com/declines/card.md). In this case, the PaymentMethod is detached and the PaymentIntent’s status automatically transitions to `requires_payment_method`.

When the PaymentIntent’s status is `requires_action`, your customer must authenticate the payment within 5 minutes. If no action is taken after 5 minutes, the PaymentMethod detaches and the PaymentIntent’s status automatically transitions to `requires_payment_method`.

## Refunds and disputes

Stripe performs a card transaction using standard card rails as part of a MobilePay transaction. [Refunds](https://docs.stripe.com/refunds.md) and [disputes](https://docs.stripe.com/disputes/how-disputes-work.md) are subject to the Visa and Mastercard network rules.

## See also

- [More about MobilePay](https://docs.stripe.com/payments/mobilepay.md)
- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment.md)
- [Customize Checkout](https://docs.stripe.com/payments/checkout/customization.md)

# Elements

> This is a Elements for when payment-ui is elements. View the full page at https://docs.stripe.com/payments/mobilepay/accept-a-payment?payment-ui=elements.

MobilePay is a [single-use](https://docs.stripe.com/payments/payment-methods.md#usage) card wallet payment method used in Denmark and Finland. It allows your customer to [authenticate and approve](https://docs.stripe.com/payments/payment-methods.md#customer-actions) payments using the MobilePay app.

When your customer pays with MobilePay, Stripe performs a card transaction using the card data we receive from MobilePay. The processing of the card transaction is invisible to your integration, and Stripe [immediately notifies you](https://docs.stripe.com/payments/payment-methods.md#payment-notification) whether the payment succeeded or failed.

This guide shows you how to embed a custom Stripe payment form in your website or application using the [Payment Element](https://docs.stripe.com/payments/payment-element.md). The Payment Element allows you to support MobilePay and other payment methods automatically. For advanced configurations and customizations, refer to the [Accept a Payment](https://docs.stripe.com/payments/accept-a-payment.md) integration guide.

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

#### Manage payment methods from the Dashboard

Create a PaymentIntent on your server with an amount and currency. You can manage payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods). Stripe handles the return of eligible payment methods based on factors such as the transaction’s amount, currency, and payment flow. Before creating the Payment Intent, make sure to turn **MobilePay** on in the [payment methods settings](https://dashboard.stripe.com/settings/payment_methods) page.

Always decide how much to charge on the server side, a trusted environment, as opposed to the client. This prevents malicious customers from being able to choose their own prices.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "usd",
  automatic_payment_methods: {
    enabled: true,
  },
});
```

#### List payment methods manually

If you don’t want to use the Dashboard or want to manually specify payment methods, you can list them using the `payment_method_types` attribute.

Create a PaymentIntent on your server with an amount, currency, and a list of payment methods. Always decide how much to charge on the server side, a trusted environment, as opposed to the client. This prevents malicious customers from being able to choose their own prices.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: "eur",
  payment_method_types: ["mobilepay"],
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

Customers can authenticate MobilePay transactions with mobile or desktop apps. The client that the customer uses determines the authentication method after calling `confirmPayment`.

#### Mobile app authentication

After you call `confirmPayment`, Stripe redirects your customers to MobilePay to approve or decline the payment. After your customers authorize the payment, the page redirects them to the Payment Intent’s `return_url`. Stripe adds `payment_intent`, `payment_intent_client_secret`, `redirect_pm_type`, and `redirect_status` as URL query parameters (along with any existing query parameters in the `return_url`).

An authentication session expires after 5 minutes, and the PaymentIntent’s status transitions back to `require_payment_method`. After the status transitions, your customer sees a payment error and must restart the payment process.

#### Desktop web app authentication

After you call `confirmPayment`, Stripe redirects your customers to a MobilePay-hosted page where they can input the phone number associated with their MobilePay account. This sends a push notification to their MobilePay app for payment authentication. After your customer successfully authenticates the payment, the page redirect them back to the `return_url`. If you prefer not to redirect customers on the web after payment, pass `redirect: if_required` to the Payment Element.

An authentication session expires after 5 minutes, and the PaymentIntent’s status transitions back to `require_payment_method`. After the status transitions, your customer sees a payment error and must restart the payment process.

## Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

- **Handle events manually in the Dashboard**

  Use the Dashboard to [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments), send email receipts, handle payouts, or retry failed payments.

- **Build a custom webhook**

  [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook) handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- **Integrate a prebuilt app**

  Handle common business events, such as [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

## Test the integration

#### Mobile web app testing

To test your integration, choose MobilePay as the payment method and tap **Pay**. In a testing environment, this redirects you to a test payment page where you can approve or decline the payment.

In live mode, tapping **Pay** redirects you to the MobilePay mobile application, where you can approve or decline the payment.

#### Desktop web app testing

To test your integration in a testing environment, it redirects you to a test payment page where you can approve or decline the test payment.

In live mode, enter the phone number linked to MobilePay to send a push notification to your MobilePay mobile application. You can approve or decline the payment in the MobilePay mobile application.

## Optional: Authorize a payment and then capture later

MobilePay supports [separate authorization and capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md).

### Tell Stripe to authorize only

To indicate that you want separate authorization and capture, set [capture_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-capture_method) to `manual` when creating the PaymentIntent. This parameter instructs Stripe to only authorize the amount on the customer’s card linked to MobilePay.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "dkk",
  capture_method: "manual",
  payment_method_types: ["mobilepay"],
  payment_method_data: {
    type: "mobilepay",
  },
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
    amount_to_capture: 1099,
  },
);
```

## Optional: Cancellation

You can cancel MobilePay payments before they expire by [canceling the PaymentIntent](https://docs.stripe.com/api/payment_intents/cancel.md) associated with the MobilePay payment.

## Failed payments

MobilePay transactions can fail if the underlying card transaction is declined. Learn more about [card declines](https://docs.stripe.com/declines/card.md). In this case, the PaymentMethod is detached and the PaymentIntent’s status automatically transitions to `requires_payment_method`.

When the PaymentIntent’s status is `requires_action`, your customer must authenticate the payment within 5 minutes. If no action is taken after 5 minutes, the PaymentMethod detaches and the PaymentIntent’s status automatically transitions to `requires_payment_method`.

## Refunds and disputes

Stripe performs a card transaction using standard card rails as part of a MobilePay transaction. [Refunds](https://docs.stripe.com/refunds.md) and [disputes](https://docs.stripe.com/disputes/how-disputes-work.md) are subject to the Visa and Mastercard network rules.

# Direct API

> This is a Direct API for when payment-ui is direct-api. View the full page at https://docs.stripe.com/payments/mobilepay/accept-a-payment?payment-ui=direct-api.

MobilePay is a [single-use](https://docs.stripe.com/payments/payment-methods.md#usage) card wallet payment method used in Denmark and Finland. It allows your customer to [authenticate and approve](https://docs.stripe.com/payments/payment-methods.md#customer-actions) payments using the MobilePay app.

When your customer pays with MobilePay, Stripe performs a card transaction using the card data we receive from MobilePay. The processing of the card transaction is invisible to your integration, and Stripe [immediately notifies you](https://docs.stripe.com/payments/payment-methods.md#payment-notification) whether the payment succeeded or failed.

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create a PaymentIntent [Server-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) is an object that represents your intent to collect a payment from a customer and tracks the lifecycle of the payment process through each stage. Create a `PaymentIntent` on your server and specify the amount to collect and a supported currency (`eur`, `dkk`, `sek`, or `nok`). If you already have an integration using the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md), add `mobilepay` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "dkk",
  payment_method_types: ["mobilepay"],
  payment_method_data: {
    type: "mobilepay",
  },
});
```

### Example response

```json
{
  "id": "pi_12345",
  "amount": 1099,
  "client_secret": "pi_12345_secret_abcdef",
  "currency": "dkk",
  "payment_method": "pm_12345",
  "payment_method_types": ["mobilepay"],
  "status": "requires_confirmation"
}
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

## Confirm the PaymentIntent

Use the PaymentIntent [ID](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-id) from [step 2](https://docs.stripe.com/payments/mobilepay/accept-a-payment.md#create-payment-intent) to *confirm* (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) the PaymentIntent. This declares that the customer intends to pay with the specified *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs). Stripe initiates a payment after confirming the PaymentIntent. The [return_url](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-return_url) indicates where Stripe redirects the customer after they complete the payment.

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
  "currency": "dkk",
  "payment_method": "pm_12345",
  "next_action": {
    "redirect_to_url": {
      "return_url": "https://example.com/checkout/complete",
      "url": "https://pm-redirects.stripe.com/authorize/acct_123/pa_nonce_abc"
    },
    "type": "redirect_to_url"
  },
  "payment_method_types": ["mobilepay"],
  "status": "requires_action"
}
```

To authorize the payment, redirect your customer to the URL in the [next_action[redirect_to_url][url]](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-redirect_to_url-url) field.

- On desktop, the URL opens a MobilePay landing page where the customer can enter their phone number, which identifies their MobilePay account. They can then use the MobilePay smartphone app to proceed with payment authorization.
- On mobile devices, the URL opens the MobilePay application directly (if present) or directs to the MobilePay landing page, similar to the desktop process.

Your customer has 5 minutes to open the redirect URL and authorize the payment in the MobilePay app. If the underlying card charge fails, your customer can choose a different card and retry in the MobilePay app. If the payment isn’t authorized within 5 minutes, the payment fails and the PaymentIntent’s status transitions to `requires_payment_method`.

## Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

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

MobilePay supports [separate authorization and capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md).

### Tell Stripe to authorize only

To indicate that you want separate authorization and capture, set [capture_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-capture_method) to `manual` when creating the PaymentIntent. This parameter instructs Stripe to only authorize the amount on the customer’s card linked to MobilePay.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "dkk",
  capture_method: "manual",
  payment_method_types: ["mobilepay"],
  payment_method_data: {
    type: "mobilepay",
  },
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
    amount_to_capture: 1099,
  },
);
```

## Optional: Cancellation

You can cancel MobilePay payments before they expire by [canceling the PaymentIntent](https://docs.stripe.com/api/payment_intents/cancel.md) associated with the MobilePay payment.

## Failed payments

MobilePay transactions can fail if the underlying card transaction is declined. Learn more about [card declines](https://docs.stripe.com/declines/card.md). In this case, the PaymentMethod is detached and the PaymentIntent’s status automatically transitions to `requires_payment_method`.

When the PaymentIntent’s status is `requires_action`, your customer must authenticate the payment within 5 minutes. If no action is taken after 5 minutes, the PaymentMethod detaches and the PaymentIntent’s status automatically transitions to `requires_payment_method`.

## Refunds and disputes

Stripe performs a card transaction using standard card rails as part of a MobilePay transaction. [Refunds](https://docs.stripe.com/refunds.md) and [disputes](https://docs.stripe.com/disputes/how-disputes-work.md) are subject to the Visa and Mastercard network rules.

# iOS

> This is a iOS for when payment-ui is mobile and platform is ios. View the full page at https://docs.stripe.com/payments/mobilepay/accept-a-payment?payment-ui=mobile&platform=ios.

MobilePay is a [single-use](https://docs.stripe.com/payments/payment-methods.md#usage) card wallet payment method used in Denmark and Finland. It allows your customer to [authenticate and approve](https://docs.stripe.com/payments/payment-methods.md#customer-actions) payments using the MobilePay app.

When your customer pays with MobilePay, Stripe performs a card transaction using the card data we receive from MobilePay. The processing of the card transaction is invisible to your integration, and Stripe [immediately notifies you](https://docs.stripe.com/payments/payment-methods.md#payment-notification) whether the payment succeeded or failed.

Stripe recommends using the [Mobile Payment Element](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=mobile&platform=ios), an embeddable payment form, to add MobilePay and other payment methods to your integration with the least amount of effort.

This guide covers how to accept MobilePay from your native mobile application using your own custom payment form. Your native mobile application redirects your customer to the MobilePay mobile application to complete the payment. Completing the purchase requires no additional action in the MobilePay mobile application.

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

## Create a PaymentIntent [Server-side] [Client-side]

### Server-side

A [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) is an object that represents your intent to collect payment from a customer and tracks the lifecycle of the payment process through each stage.

To create and confirm a `PaymentIntent` on your server:

- Specify the amount to collect and a supported currency (`eur`, `dkk`, `sek`, or `nok`).
- Add `mobilepay` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your `PaymentIntent`. Make sure that you enable MobilePay in the [Dashboard](https://dashboard.stripe.com/settings/payment_methods).
- Set `payment_method_data[type]` to `mobilepay` to create a *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) and immediately use it with this PaymentIntent.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "dkk",
  payment_method_types: ["mobilepay"],
  payment_method_data: {
    type: "mobilepay",
  },
  return_url: "payments-example://stripe-redirect",
});
```

The PaymentIntent includes a *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)). Send the client secret to the client to *confirm* (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) the PaymentIntent in the next step.

### Client-side

On the client, request a PaymentIntent from your server and store its client secret.

#### Swift

```swift
class CheckoutViewController: UIViewController {
    var paymentIntentClientSecret: String?

    // ...continued from previous step

    override func viewDidLoad() {
        // ...continued from previous step
        startCheckout()
    }

    func startCheckout() {
        // Request a PaymentIntent from your server and store its client secret
        // Click View full sample to see a complete implementation
    }
}
```

## Submit the payment to Stripe [Client-side]

When a customer taps to pay with MobilePay, confirm the `PaymentIntent` to complete the payment. Configure an `STPPaymentIntentParams` object with the `PaymentIntent` [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret).

The client secret is different from your API keys that authenticate Stripe API requests. Handle it carefully because it can complete the charge. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

### Set up a return URL

The customer might navigate away from your app to authenticate (for example, in Safari or their banking app). To allow them to automatically return to your app after authenticating, [configure a custom URL scheme](https://developer.apple.com/documentation/xcode/defining-a-custom-url-scheme-for-your-app) and set up your app delegate to forward the URL to the SDK. Stripe doesn’t support [universal links](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content).

#### SceneDelegate

#### Swift

```swift
// This method handles opening custom URL schemes (for example, "your-app://stripe-redirect")
func scene(_ scene: UIScene, openURLContexts URLContexts: Set<UIOpenURLContext>) {
    guard let url = URLContexts.first?.url else {
        return
    }
    let stripeHandled = StripeAPI.handleURLCallback(with: url)
    if (!stripeHandled) {
        // This was not a Stripe url – handle the URL normally as you would
    }
}

```

#### AppDelegate

#### Swift

```swift
// This method handles opening custom URL schemes (for example, "your-app://stripe-redirect")
func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey: Any] = [:]) -> Bool {
    let stripeHandled = StripeAPI.handleURLCallback(with: url)
    if (stripeHandled) {
        return true
    } else {
        // This was not a Stripe url – handle the URL normally as you would
    }
    return false
}
```

#### SwiftUI

#### Swift

```swift

@main
struct MyApp: App {
  var body: some Scene {
    WindowGroup {
      Text("Hello, world!").onOpenURL { incomingURL in
          let stripeHandled = StripeAPI.handleURLCallback(with: incomingURL)
          if (!stripeHandled) {
            // This was not a Stripe url – handle the URL normally as you would
          }
        }
    }
  }
}
```

### Confirm the payment

Use the PaymentIntent client secret from [step 2](https://docs.stripe.com/payments/mobilepay/accept-a-payment.md#create-payment-intent) to confirm the PaymentIntent using [STPPaymentHandler.shared.confirmPayment()](<https://stripe.dev/stripe-ios/stripepayments/documentation/stripepayments/stppaymenthandler/confirmpayment(_:with:completion:)>). This opens the MobilePay application directly (if present) or a webview showing the MobilePay landing page. After the customer authorizes the payment, the completion block contains the status of the payment.

#### Swift

```swift
let paymentIntentParams = STPPaymentIntentParams(clientSecret: paymentIntentClientSecret)
paymentIntentParams.paymentMethodParams = STPPaymentMethodParams(
  mobilePay: STPPaymentMethodMobilePayParams(),
  billingDetails: nil,
  metadata: nil
)
paymentIntentParams.returnURL = "your-app://stripe-redirect" // Set returnURL to your app's return URL that you set up in the previous step

STPPaymentHandler.shared().confirmPayment(paymentIntentParams, with: self) { (handlerStatus, paymentIntent, error) in
    switch handlerStatus {
    case .succeeded:
        // Payment succeeded
        // ...

    case .canceled:
        // Payment canceled
        // ...

    case .failed:
        // Payment failed
        // ...

    @unknown default:
        fatalError()
    }
}
```

Your customer has 5 minutes to authorize the payment in the MobilePay app. If the underlying card charge fails, your customer can choose a different card and retry in the MobilePay app.

## Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

- **Handle events manually in the Dashboard**

  Use the Dashboard to [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments), send email receipts, handle payouts, or retry failed payments.

- **Build a custom webhook**

  [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook) handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- **Integrate a prebuilt app**

  Handle common business events, such as [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

## Test the integration

Use your [test API keys](https://docs.stripe.com/keys.md#test-live-modes) to create a PaymentIntent. After confirming the PaymentIntent, follow the `next_action` redirect URL to a test page with options to authorize or fail the payment.

- Click **Authorize test payment** to test the case when the payment is successful. The PaymentIntent’s [status](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-status) transitions from `requires_action` to `succeeded`.
- Click **Fail test payment** to test the case when the customer fails to authenticate. The PaymentIntent’s [status](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-status) transitions from `requires_action` to `requires_payment_method`.

## Optional: Cancellation

You can cancel MobilePay payments before they expire by [canceling the PaymentIntent](https://docs.stripe.com/api/payment_intents/cancel.md) associated with the MobilePay payment.

## Failed payments

MobilePay transactions can fail if the underlying card transaction is declined. Learn more about [card declines](https://docs.stripe.com/declines/card.md). In this case, the PaymentMethod is detached and the PaymentIntent’s status automatically transitions to `requires_payment_method`.

When the PaymentIntent’s status is `requires_action`, your customer must authenticate the payment within 5 minutes. If no action is taken after 5 minutes, the PaymentMethod detaches and the PaymentIntent’s status automatically transitions to `requires_payment_method`.

## Refunds and disputes

Stripe performs a card transaction using standard card rails as part of a MobilePay transaction. [Refunds](https://docs.stripe.com/refunds.md) and [disputes](https://docs.stripe.com/disputes/how-disputes-work.md) are subject to the Visa and Mastercard network rules.

# Android

> This is a Android for when payment-ui is mobile and platform is android. View the full page at https://docs.stripe.com/payments/mobilepay/accept-a-payment?payment-ui=mobile&platform=android.

MobilePay is a [single-use](https://docs.stripe.com/payments/payment-methods.md#usage) card wallet payment method used in Denmark and Finland. It allows your customer to [authenticate and approve](https://docs.stripe.com/payments/payment-methods.md#customer-actions) payments using the MobilePay app.

When your customer pays with MobilePay, Stripe performs a card transaction using the card data we receive from MobilePay. The processing of the card transaction is invisible to your integration, and Stripe [immediately notifies you](https://docs.stripe.com/payments/payment-methods.md#payment-notification) whether the payment succeeded or failed.

Stripe recommends using the [Mobile Payment Element](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=mobile&platform=android), an embeddable payment form, to add MobilePay and other payment methods to your integration with the least amount of effort.

This guide covers how to accept MobilePay from your native mobile application using your own custom payment form. Your native mobile application redirects your customer to the MobilePay mobile application to complete the payment. Completing the purchase requires no additional action in the MobilePay mobile application.

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
  implementation("com.stripe:stripe-android:23.7.0")
  // Include the financial connections SDK to support US bank account as a payment method
  implementation("com.stripe:financial-connections:23.7.0")
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

## Create a PaymentIntent [Server-side] [Client-side]

### Server-side

A [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) is an object that represents your intent to collect payment from a customer and tracks the lifecycle of the payment process through each stage.

To create and confirm a `PaymentIntent` on your server:

- Specify the amount to collect and a supported currency (`eur`, `dkk`, `sek`, or `nok`).
- Add `mobilepay` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types). Make sure that you enable MobilePay in the [Dashboard](https://dashboard.stripe.com/settings/payment_methods).
- Set `payment_method_data[type]` to `mobilepay` to create a *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) and immediately use it with this PaymentIntent.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "dkk",
  payment_method_types: ["mobilepay"],
  payment_method_data: {
    type: "mobilepay",
  },
});
```

The PaymentIntent includes a *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)). Send the client secret to the client to *confirm* (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) the PaymentIntent in the next step.

### Client-side

On the client, request a PaymentIntent from your server and store its client secret.

#### Kotlin

```kotlin
class CheckoutActivity : AppCompatActivity() {

  private lateinit var paymentIntentClientSecret: String

  override fun onCreate(savedInstanceState: Bundle?) {
      super.onCreate(savedInstanceState)
      // ...
      startCheckout()
  }

  private fun startCheckout() {
      // Request a PaymentIntent from your server and store its client secret in paymentIntentClientSecret
      // Click View full sample to see a complete implementation
  }
}
```

## Submit the payment to Stripe [Client-side]

When a customer taps to pay with MobilePay, confirm the `PaymentIntent` to complete the payment. Configure a `ConfirmPaymentIntentParams` object with the `PaymentIntent` [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret).

The client secret is different from your API keys that authenticate Stripe API requests. Handle it carefully because it can complete the charge. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

### Confirm the payment

Use the PaymentIntent client secret from [step 2](https://docs.stripe.com/payments/mobilepay/accept-a-payment.md#create-payment-intent) to confirm the PaymentIntent using [PaymentLauncher confirm](https://stripe.dev/stripe-android/payments-core/com.stripe.android.payments.paymentlauncher/-payment-launcher/index.html#74063765%2FFunctions%2F-1622557690). This opens the MobilePay application directly (if present) or a webview showing the MobilePay landing page. After the customer authorizes the payment, `onPaymentResult` contains the status of the payment.

#### Kotlin

```kotlin
class CheckoutActivity : AppCompatActivity() {
    // ...
    private lateinit var paymentIntentClientSecret: String
    private val paymentLauncher: PaymentLauncher by lazy {
        PaymentLauncher.create(
            this,
            PaymentConfiguration.getInstance(applicationContext).publishableKey,
            PaymentConfiguration.getInstance(applicationContext).stripeAccountId,
            ::onPaymentResult
        )
    }

    private fun startCheckout() {
        // ...

        val confirmParams = ConfirmPaymentIntentParams
            .createWithPaymentMethodCreateParams(
                paymentMethodCreateParams = PaymentMethodCreateParams.createMobilePay(),
                clientSecret = paymentIntentClientSecret
            )
        paymentLauncher.confirm(confirmParams)
    }

    private fun onPaymentResult(paymentResult: PaymentResult) {
        val message = when (paymentResult) {
            is PaymentResult.Completed -> {
                "Completed!"
            }
            is PaymentResult.Canceled -> {
                "Canceled!"
            }
            is PaymentResult.Failed -> {
                // This string comes from the PaymentIntent's error message.
                // See: https://docs.stripe.com/api/payment_intents/object#payment_intent_object-last_payment_error-message
                "Failed: " + paymentResult.throwable.message
            }
        }
    }
}
```

Your customer has 5 minutes to authorize the payment in the MobilePay app. If the underlying card charge fails, your customer can choose a different card and retry in the MobilePay app.

## Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

- **Handle events manually in the Dashboard**

  Use the Dashboard to [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments), send email receipts, handle payouts, or retry failed payments.

- **Build a custom webhook**

  [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook) handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- **Integrate a prebuilt app**

  Handle common business events, such as [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

## Test the integration

Use your [test API keys](https://docs.stripe.com/keys.md#test-live-modes) to create a PaymentIntent. After confirming the PaymentIntent, follow the `next_action` redirect URL to a test page with options to authorize or fail the payment.

- Click **Authorize test payment** to test the case when the payment is successful. The PaymentIntent’s [status](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-status) transitions from `requires_action` to `succeeded`.
- Click **Fail test payment** to test the case when the customer fails to authenticate. The PaymentIntent’s [status](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-status) transitions from `requires_action` to `requires_payment_method`.

## Optional: Cancellation

You can cancel MobilePay payments before they expire by [canceling the PaymentIntent](https://docs.stripe.com/api/payment_intents/cancel.md) associated with the MobilePay payment.

## Failed payments

MobilePay transactions can fail if the underlying card transaction is declined. Learn more about [card declines](https://docs.stripe.com/declines/card.md). In this case, the PaymentMethod is detached and the PaymentIntent’s status automatically transitions to `requires_payment_method`.

When the PaymentIntent’s status is `requires_action`, your customer must authenticate the payment within 5 minutes. If no action is taken after 5 minutes, the PaymentMethod detaches and the PaymentIntent’s status automatically transitions to `requires_payment_method`.

## Refunds and disputes

Stripe performs a card transaction using standard card rails as part of a MobilePay transaction. [Refunds](https://docs.stripe.com/refunds.md) and [disputes](https://docs.stripe.com/disputes/how-disputes-work.md) are subject to the Visa and Mastercard network rules.

# React Native

> This is a React Native for when payment-ui is mobile and platform is react-native. View the full page at https://docs.stripe.com/payments/mobilepay/accept-a-payment?payment-ui=mobile&platform=react-native.

MobilePay is a [single-use](https://docs.stripe.com/payments/payment-methods.md#usage) card wallet payment method used in Denmark and Finland. It allows your customer to [authenticate and approve](https://docs.stripe.com/payments/payment-methods.md#customer-actions) payments using the MobilePay app.

When your customer pays with MobilePay, Stripe performs a card transaction using the card data we receive from MobilePay. The processing of the card transaction is invisible to your integration, and Stripe [immediately notifies you](https://docs.stripe.com/payments/payment-methods.md#payment-notification) whether the payment succeeded or failed.

Stripe recommends using the [Mobile Payment Element](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=mobile&platform=react-native), an embeddable payment form, to add MobilePay and other payment methods to your integration with the least amount of effort.

This guide covers how to accept MobilePay from your native mobile application using your own custom payment form. Your native mobile application redirects your customer to a webview to complete the payment on MobilePay.

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

## Create a PaymentIntent [Server-side] [Client-side]

### Server-side

A [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) is an object that represents your intent to collect payment from a customer and tracks the lifecycle of the payment process through each stage.

To create and confirm a `PaymentIntent` on your server:

- Specify the amount to collect and a supported currency (`eur`, `dkk`, `sek`, or `nok`).
- Add `mobilepay` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types). Make sure that you enable MobilePay in the [Dashboard](https://dashboard.stripe.com/settings/payment_methods).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "dkk",
  payment_method_types: ["mobilepay"],
  return_url: "payments-example://stripe-redirect",
});
```

The PaymentIntent includes a *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)). Send the client secret to the client to *confirm* (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) the PaymentIntent in the next step.

### Client-side

On the client, request a PaymentIntent from your server and store its client secret:

```javascript
function PaymentScreen() {
  const fetchPaymentIntentClientSecret = async () => {
    const response = await fetch(`${API_URL}/create-payment-intent`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        currency: "dkk",
      }),
    });
    const { clientSecret } = await response.json();

    return clientSecret;
  };

  const handlePayPress = async () => {
    // See below
  };

  return (
    <View>
      <Button onPress={handlePayPress} title="Pay" />
    </View>
  );
}
```

The client secret is different from your API keys that authenticate Stripe API requests. Handle it carefully because it can complete the charge. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

## Set up a return URL (iOS only) [Client-side]

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

## Confirm MobilePay payment [Client-side]

When the customer taps to pay with MobilePay, complete the payment by calling [confirmPayment](https://stripe.dev/stripe-react-native/api-reference/index.html#confirmPayment). This presents a webview where the customer can authorize the payment in the MobilePay application. After the customer authorizes the payment, the promise resolves with an object containing either a `paymentIntent` field, or an `error` field if an error occurred with the payment.

```javascript
import { useConfirmPayment } from "@stripe/stripe-react-native";

function PaymentScreen() {
  const { confirmPayment, loading } = useConfirmPayment();

  const fetchPaymentIntentClientSecret = async () => {
    // See above
  };

  const handlePayPress = async () => {
    // Fetch the client secret from the backend.
    const clientSecret = await fetchPaymentIntentClientSecret();

    const { error, paymentIntent } = await confirmPayment(clientSecret, {
      paymentMethodType: "MobilePay",
    });

    if (error) {
      console.log("Payment confirmation error: ", error);
    } else if (paymentIntent) {
      console.log("Successfully confirmed payment: ", paymentIntent);
    }
  };

  return (
    <View>
      <Button onPress={handlePayPress} title="Pay" disabled={loading} />
    </View>
  );
}
```

Your customer has 5 minutes to authorize the payment in the MobilePay app. If the underlying card charge fails, your customer can choose a different card and retry in the MobilePay app.

## Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

- **Handle events manually in the Dashboard**

  Use the Dashboard to [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments), send email receipts, handle payouts, or retry failed payments.

- **Build a custom webhook**

  [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook) handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- **Integrate a prebuilt app**

  Handle common business events, such as [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

## Test the integration

Use your [test API keys](https://docs.stripe.com/keys.md#test-live-modes) to create a PaymentIntent. After confirming the PaymentIntent, follow the `next_action` redirect URL to a test page with options to authorize or fail the payment.

- Click **Authorize test payment** to test the case when the payment is successful. The PaymentIntent’s [status](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-status) transitions from `requires_action` to `succeeded`.
- Click **Fail test payment** to test the case when the customer fails to authenticate. The PaymentIntent’s [status](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-status) transitions from `requires_action` to `requires_payment_method`.

## Optional: Cancellation

You can cancel MobilePay payments before they expire by [canceling the PaymentIntent](https://docs.stripe.com/api/payment_intents/cancel.md) associated with the MobilePay payment.

## Failed payments

MobilePay transactions can fail if the underlying card transaction is declined. Learn more about [card declines](https://docs.stripe.com/declines/card.md). In this case, the PaymentMethod is detached and the PaymentIntent’s status automatically transitions to `requires_payment_method`.

When the PaymentIntent’s status is `requires_action`, your customer must authenticate the payment within 5 minutes. If no action is taken after 5 minutes, the PaymentMethod detaches and the PaymentIntent’s status automatically transitions to `requires_payment_method`.

## Refunds and disputes

Stripe performs a card transaction using standard card rails as part of a MobilePay transaction. [Refunds](https://docs.stripe.com/refunds.md) and [disputes](https://docs.stripe.com/disputes/how-disputes-work.md) are subject to the Visa and Mastercard network rules.
