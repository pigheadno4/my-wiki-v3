<!-- Source URL: https://docs.stripe.com/payments/pix/accept-a-payment -->
<!-- Fetched: 2026-05-06 -->

# Accept a one-time payment

Learn how to accept a Pix one-time payment, a common payment method in Brazil.

# Checkout

> This is a Checkout for when payment-ui is checkout. View the full page at https://docs.stripe.com/payments/pix/accept-a-payment?payment-ui=checkout.

Stripe users can accept Pix payments from customers in Brazil. Customers pay by copying and pasting a Pix string or scanning a QR code directly in their bank apps.

## Determine compatibility

**Supported business locations**: BR, US, EU, CA, GB, AU, SG, CH

**Supported currencies**: `brl`

**Presentment currencies**: `brl`

**Payment mode**: Yes

**Setup mode**: Yes

**Subscription mode**: Yes

A Checkout Session must satisfy all of the following conditions to support Pix payments:

- *Prices* (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) for all line items must be in the `brl` currency.
- You can only use one-time line items for Pix one-time payments. Setup mode and recurring *subscription* (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) plans are supported through [Pix Automático](https://docs.stripe.com/payments/pix/pix-automatico.md).

## Accept a payment

> Build an integration to [accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?integration=checkout) with Checkout before using this guide.

This guides you through enabling Pix and shows the differences between accepting payments using dynamic payment methods and manually configuring payment methods.

### Enable Pix as a payment method

When creating a new [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md), you need to:

1. Add `pix` to the list of `payment_method_types`.
1. Make sure all your `line_items` use the `brl` currency.

#### Stripe-hosted page

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
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
  mode: "payment",
  payment_method_types: ["card", "pix"],
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
        currency: "brl",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "pix"],
  return_url: "https://example.com/return",
  ui_mode: "embedded_page",
});
```

### Additional payment method options

You can set the number of seconds before a pending Pix payment expires by specifying the optional [expires_after_seconds](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_method_options-pix-expires_after_seconds) parameter in the `payment_method_options`. For example, if a customer completes the Checkout Session with `expires_after_seconds` set to `600` on Monday at 14:00, they have until Monday at 14:10 to transfer the funds and complete the payment.

You can set `expires_after_seconds` to a value between 10 seconds and 1209600 seconds (14 days). The default is 14400 seconds (4 hours).

#### Stripe-hosted page

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
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
  mode: "payment",
  payment_method_options: {
    pix: {
      expires_after_seconds: 600,
    },
  },
  payment_method_types: ["card", "pix"],
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
        currency: "brl",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_options: {
    pix: {
      expires_after_seconds: 600,
    },
  },
  payment_method_types: ["card", "pix"],
  return_url: "https://example.com/return",
  ui_mode: "embedded_page",
});
```

### Fulfill your orders

After accepting a payment, learn how to [fulfill orders](https://docs.stripe.com/checkout/fulfillment.md).

## Test your integration

To test your integration:

1. Select Pix.
1. Enter the buyer’s details and tap **Pay**. In a testing environment, you can use `000.000.000-00` as a test tax identifier (CPF or CNPJ).
1. Click **Simulate scan** to open a Stripe-hosted Pix test payment page. From this page, you can either authorize or expire the test payment.

In live mode, the **Pay** button displays a Pix QR code. You need a Brazilian bank account with Pix enabled to complete or cancel this payment flow.

You can also set [payment_method.billing_details.email](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_data-billing_details-email) to the following values to test different scenarios.

| Email                       | Description                                                                                                                                                                                                                                                                                                                                                                                                   |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `{any_prefix}@{any_domain}` | Simulates a Pix that a customer pays after 3 minutes. The [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives after approximately 3 minutes. In production, this webhook arrives immediately after the Pix is paid. |

Stripe ignores the [payment_method_options.pix.expires_at](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-pix-expires_at) and [payment_method_options.pix.expires_after_seconds](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-pix-expires_after_seconds) parameters in this case.

Example: `anything@example.com` |
| `{any_prefix}succeed_immediately@{any_domain}` | Simulates a Pix that your customer pays immediately. The [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) webhook arrives within several seconds. In production, this webhook arrives immediately after the Pix is paid.

Stripe ignores the [payment_method_options.pix.expires_at](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-pix-expires_at) and [payment_method_options.pix.expires_after_seconds](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-pix-expires_after_seconds) parameters in this case.

Example: `succeed_immediately@example.com` |
| `{any_prefix}expire_immediately@{any_domain}` | Simulates a Pix that expires before your customer pays. The [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) webhook arrives within several seconds.

Stripe ignores the [payment_method_options.pix.expires_at](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-pix-expires_at) and [payment_method_options.pix.expires_after_seconds](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-pix-expires_after_seconds) parameters in this case.

Example: `expire_immediately@example.com` |
| `{any_prefix}expire_with_delay@{any_domain}` | Simulates a Pix that expires before your customer pays. The [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) webhook arrives after approximately 3 minutes.

Stripe ignores the [payment_method_options.pix.expires_at](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-pix-expires_at) and [payment_method_options.pix.expires_after_seconds](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-pix-expires_after_seconds) parameters in this case.

Example: `expire_with_delay@example.com` |
| `{any_prefix}fill_never@{any_domain}` | Simulates a Pix that never succeeds. It expires according to the [payment_method_options.pix.expires_at](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-pix-expires_at) or [payment_method_options.pix.expires_after_seconds](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-pix-expires_after_seconds) parameter. The [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) webhook arrives after the simulation completes.

Example: `fill_never@example.com` |

## Optional: Refunds [Server-side]

You can refund Pix payments through the [Dashboard](https://dashboard.stripe.com/test/payments) or [API](https://docs.stripe.com/api.md#create_refund).

## See also

- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment.md)
- [Customizing Checkout](https://docs.stripe.com/payments/checkout/customization.md)

# Elements

> This is a Elements for when payment-ui is elements. View the full page at https://docs.stripe.com/payments/pix/accept-a-payment?payment-ui=elements.

### Pix-specific considerations

- The Brazilian government requires that buyers provide a tax ID (CPF/CNPJ) when completing cross-border transactions. Stripe Elements captures this ID, regardless of whether you’re confirming the PaymentIntent on the client-side or server-side.

- Pix QR codes expire after 4 hours from creation. Customers can’t use an expired Pix QR code to complete a payment. As soon as a Pix QR code expires, Stripe sends a `payment_intent.payment_failed` event.

## Set up Stripe [Server-side]

To get started, [create a Stripe account](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Collect payment details [Client-side]

You’re ready to collect payment details on the client with the Payment Element. The Payment Element is a prebuilt UI component that simplifies collecting payment details for a variety of payment methods.

The Payment Element contains an iframe that securely sends payment information to Stripe over an HTTPS connection. Avoid placing the Payment Element within another iframe because some payment methods require redirecting to another page for payment confirmation.

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

### Add the Payment Element to your checkout page

The Payment Element needs a place on your checkout page. Create an empty DOM node (container) with a unique ID in your payment form:

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

#### Control payment methods from the Dashboard

After the form above loads, create an Elements instance with a `mode`, `amount`, and `currency`. These values determine which payment methods your customer sees. To provide a new payment method in your form, make sure you enable it in the [Dashboard](https://dashboard.stripe.com/settings/payment_methods).

```javascript
const options = {
  mode: "payment",
  amount: 1099,
  currency: "brl",
  // Fully customizable with appearance API.
  appearance: {
    /*...*/
  },
};

// Set up Stripe.js and Elements to use in checkout formconst elements = stripe.elements(options);

// Create and mount the Payment Element
const paymentElementOptions = { layout: "accordion" };
const paymentElement = elements.create("payment", paymentElementOptions);
paymentElement.mount("#payment-element");
```

#### List payment methods manually

To manually list the payment methods you want to be available, add each one to `paymentMethodTypes`.

Then, create an instance of the Payment Element and mount it to the container DOM node.

```javascript
const options = {
  mode: "payment",
  amount: 1099,
  currency: "brl",
  paymentMethodTypes: ["pix"],
  // Fully customizable with appearance API.
  appearance: {
    /*...*/
  },
};

// Set up Stripe.js and Elements to use in checkout formconst elements = stripe.elements(options);

// Create and mount the Payment Element
const paymentElementOptions = { layout: "accordion" };
const paymentElement = elements.create("payment", paymentElementOptions);
paymentElement.mount("#payment-element");
```

#### React

### Set up Stripe.js

Install [React Stripe.js](https://www.npmjs.com/package/@stripe/react-stripe-js) and the [Stripe.js loader](https://www.npmjs.com/package/@stripe/stripe-js) from the npm public registry.

```bash
npm install --save @stripe/react-stripe-js @stripe/stripe-js
```

### Add and configure the Elements provider to your checkout page

To use the Payment Element component, wrap your checkout page component in an [Elements provider](https://docs.stripe.com/sdks/stripejs-react.md#elements-provider). Call `loadStripe` with your publishable key, and pass the returned `Promise` to the `Elements` provider.

#### Control payment methods from the Dashboard

The `Elements` provider also accepts a `mode`, `amount`, and `currency`. These values determine which payment methods your customer sees. To provide a new payment method in your form, make sure you enable it in the [Dashboard](https://dashboard.stripe.com/settings/payment_methods).

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
    mode: "payment",
    amount: 1099,
    currency: "brl",
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

#### List payment methods manually

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
    mode: "payment",
    amount: 1099,
    currency: "brl",
    paymentMethodTypes: ["pix"],
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

Use the `PaymentElement` component to build your form.

```jsx
import React from "react";
import { PaymentElement } from "@stripe/react-stripe-js";

const CheckoutForm = () => {
  return (
    <form>
      <PaymentElement />
      <button>Submit</button>
    </form>
  );
};

export default CheckoutForm;
```

You can customize the Payment Element to match the design of your site by passing the [appearance object](https://docs.stripe.com/elements/appearance-api.md) into `options` when creating the `Elements` provider.

### Collect addresses

By default, the Payment Element only collects the necessary billing address details. Some behavior, such as [calculating tax](https://docs.stripe.com/api/tax/calculations/create.md) or entering shipping details, requires your customer’s full address. You can:

- Use the [Address Element](https://docs.stripe.com/elements/address-element.md) to take advantage of autocomplete and localization features to collect your customer’s full address. This helps ensure the most accurate tax calculation.
- Collect address details using your own custom form.

## Create a PaymentIntent [Server-side]

> #### Run custom business logic immediately before payment confirmation
>
> Navigate to [step 5](https://docs.stripe.com/payments/finalize-payments-on-the-server.md?platform=web&type=payment#submit-payment) in the finalize payments guide to run your custom business logic immediately before payment confirmation. Otherwise, follow the steps below for a simpler integration, which uses `stripe.confirmPayment` on the client to both confirm the payment and handle any next actions.

#### Control payment methods from the Dashboard

When the customer submits your payment form, use a *PaymentIntent* (The Payment Intents API tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by regulatory mandates, custom Radar fraud rules, or redirect-based payment methods) to facilitate the confirmation and payment process. Create a PaymentIntent on your server with an `amount` and `currency`. To prevent malicious customers from choosing their own prices, always decide how much to charge on the server-side (a trusted environment) and not the client.

A `PaymentIntent` includes a *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)). Return this value to your client for Stripe.js to use to securely complete the payment process.

#### Accounts v2

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
const express = require("express");
const app = express();

app.use(express.static("."));

app.post("/create-intent", async (req, res) => {
  const intent = await stripe.paymentIntents.create({
    // To allow saving and retrieving payment methods, provide the customer's Account ID.
    customer_account: "{{CUSTOMER_ACCOUNT_ID}}",
    amount: 1099,
    currency: "brl",
  });
  res.json({ client_secret: intent.client_secret });
});

app.listen(3000, () => {
  console.log("Running on port 3000");
});
```

#### Customers v1

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
const express = require("express");
const app = express();

app.use(express.static("."));

app.post("/create-intent", async (req, res) => {
  const intent = await stripe.paymentIntents.create({
    // To allow saving and retrieving payment methods, provide the Customer ID.
    customer: customer.id,
    amount: 1099,
    currency: "brl",
  });
  res.json({ client_secret: intent.client_secret });
});

app.listen(3000, () => {
  console.log("Running on port 3000");
});
```

#### List payment methods manually

When the customer submits your payment form, use a *PaymentIntent* (The Payment Intents API tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by regulatory mandates, custom Radar fraud rules, or redirect-based payment methods) to facilitate the confirmation and payment process. Create a PaymentIntent on your server with an `amount`, `currency`, and one or more payment methods using `payment_method_types`. To prevent malicious customers from choosing their own prices, always decide how much to charge on the server-side (a trusted environment) and not the client.

Included on a PaymentIntent is a *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)). Return this value to your client for Stripe.js to use to securely complete the payment process.

#### Accounts v2

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
const express = require("express");
const app = express();

app.use(express.static("."));

app.post("/create-intent", async (req, res) => {
  const intent = await stripe.paymentIntents.create({
    // To allow saving and retrieving payment methods, provide the customer's Account ID.
    customer_account: customer_account.id,
    amount: 1099,
    currency: "brl",
    payment_method_types: ["pix"],
  });
  res.json({ client_secret: intent.client_secret });
});

app.listen(3000, () => {
  console.log("Running on port 3000");
});
```

#### Customers v1

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
const express = require("express");
const app = express();

app.use(express.static("."));

app.post("/create-intent", async (req, res) => {
  const intent = await stripe.paymentIntents.create({
    // To allow saving and retrieving payment methods, provide the Customer ID.
    customer: customer.id,
    amount: 1099,
    currency: "brl",
    payment_method_types: ["pix"],
  });
  res.json({ client_secret: intent.client_secret });
});

app.listen(3000, () => {
  console.log("Running on port 3000");
});
```

## Submit the payment to Stripe [Client-side]

Use [stripe.confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment) to complete the payment using details from the Payment Element.

Provide a [return_url](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-return_url) to this function to indicate where Stripe redirects the user after they complete the payment. Your user might be initially redirected to an intermediate site, such as a bank authorization page, before being redirected to the `return_url`. Card payments immediately redirect to the `return_url` when a payment is successful.

If you don’t want to redirect for card payments after payment completion, you can set [redirect](https://docs.stripe.com/js/payment_intents/confirm_payment#confirm_payment_intent-options-redirect) to `if_required`. This only redirects customers that check out with redirect-based payment methods.

#### HTML + JS

```javascript
const form = document.getElementById("payment-form");
const submitBtn = document.getElementById("submit");

const handleError = (error) => {
  const messageContainer = document.querySelector("#error-message");
  messageContainer.textContent = error.message;
  submitBtn.disabled = false;
};

form.addEventListener("submit", async (event) => {
  // We don't want to let default form submission happen here,
  // which would refresh the page.
  event.preventDefault();

  // Prevent multiple form submissions
  if (submitBtn.disabled) {
    return;
  }

  // Disable form submission while loading
  submitBtn.disabled = true;

  // Trigger form validation and wallet collection
  const { error: submitError } = await elements.submit();
  if (submitError) {
    handleError(submitError);
    return;
  }

  // Create the PaymentIntent and obtain clientSecret
  const res = await fetch("/create-intent", {
    method: "POST",
  });

  const { client_secret: clientSecret } = await res.json();

  // Confirm the PaymentIntent using the details collected by the Payment Element
  const { error } = await stripe.confirmPayment({
    elements,
    clientSecret,
    confirmParams: {
      return_url: "https://example.com/order/123/complete",
    },
  });

  if (error) {
    // This point is only reached if there's an immediate error when
    // confirming the payment. Show the error to your customer (for example, payment details incomplete)
    handleError(error);
  } else {
    // Your customer is redirected to your `return_url`. For some payment
    // methods like iDEAL, your customer is redirected to an intermediate
    // site first to authorize the payment, then redirected to the `return_url`.
  }
});
```

#### React

```jsx
import React, { useState } from "react";
import {
  useStripe,
  useElements,
  PaymentElement,
} from "@stripe/react-stripe-js";

export default function CheckoutForm() {
  const stripe = useStripe();
  const elements = useElements();

  const [errorMessage, setErrorMessage] = useState();
  const [loading, setLoading] = useState(false);

  const handleError = (error) => {
    setLoading(false);
    setErrorMessage(error.message);
  };

  const handleSubmit = async (event) => {
    // We don't want to let default form submission happen here,
    // which would refresh the page.
    event.preventDefault();

    if (!stripe) {
      // Stripe.js hasn't yet loaded.
      // Make sure to disable form submission until Stripe.js has loaded.
      return;
    }

    setLoading(true);

    // Trigger form validation and wallet collection
    const { error: submitError } = await elements.submit();
    if (submitError) {
      handleError(submitError);
      return;
    }

    // Create the PaymentIntent and obtain clientSecret
    const res = await fetch("/create-intent", {
      method: "POST",
    });

    const { client_secret: clientSecret } = await res.json();

    // Confirm the PaymentIntent using the details collected by the Payment Element
    const { error } = await stripe.confirmPayment({
      elements,
      clientSecret,
      confirmParams: {
        return_url: "https://example.com/order/123/complete",
      },
    });

    if (error) {
      // This point is only reached if there's an immediate error when
      // confirming the payment. Show the error to your customer (for example, payment details incomplete)
      handleError(error);
    } else {
      // Your customer is redirected to your `return_url`. For some payment
      // methods like iDEAL, your customer is redirected to an intermediate
      // site first to authorize the payment, then redirected to the `return_url`.
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <PaymentElement />
      <button type="submit" disabled={!stripe || loading}>
        Submit Payment
      </button>
      {errorMessage && <div>{errorMessage}</div>}
    </form>
  );
}
```

## Optional: Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

- **Handle events manually in the Dashboard**

  Use the Dashboard to [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments), send email receipts, handle payouts, or retry failed payments.

- **Build a custom webhook**

  [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook) handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- **Integrate a prebuilt app**

  Handle common business events, such as [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

## Test your integration

To test your integration:

1. Select Pix.
1. Enter the buyer’s details and tap **Pay**. In a testing environment, you can use `000.000.000-00` as a test tax identifier (CPF or CNPJ).
1. Click **Simulate scan** to open a Stripe-hosted Pix test payment page. From this page, you can either authorize or expire the test payment.

In live mode, the **Pay** button displays a Pix QR code. You need a Brazilian bank account with Pix enabled to complete or cancel this payment flow.

You can also set [payment_method.billing_details.email](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_data-billing_details-email) to the following values to test different scenarios.

| Email                       | Description                                                                                                                                                                                                                                                                                                                                                                                                   |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `{any_prefix}@{any_domain}` | Simulates a Pix that a customer pays after 3 minutes. The [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives after approximately 3 minutes. In production, this webhook arrives immediately after the Pix is paid. |

Stripe ignores the [payment_method_options.pix.expires_at](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-pix-expires_at) and [payment_method_options.pix.expires_after_seconds](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-pix-expires_after_seconds) parameters in this case.

Example: `anything@example.com` |
| `{any_prefix}succeed_immediately@{any_domain}` | Simulates a Pix that your customer pays immediately. The [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) webhook arrives within several seconds. In production, this webhook arrives immediately after the Pix is paid.

Stripe ignores the [payment_method_options.pix.expires_at](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-pix-expires_at) and [payment_method_options.pix.expires_after_seconds](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-pix-expires_after_seconds) parameters in this case.

Example: `succeed_immediately@example.com` |
| `{any_prefix}expire_immediately@{any_domain}` | Simulates a Pix that expires before your customer pays. The [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) webhook arrives within several seconds.

Stripe ignores the [payment_method_options.pix.expires_at](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-pix-expires_at) and [payment_method_options.pix.expires_after_seconds](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-pix-expires_after_seconds) parameters in this case.

Example: `expire_immediately@example.com` |
| `{any_prefix}expire_with_delay@{any_domain}` | Simulates a Pix that expires before your customer pays. The [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) webhook arrives after approximately 3 minutes.

Stripe ignores the [payment_method_options.pix.expires_at](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-pix-expires_at) and [payment_method_options.pix.expires_after_seconds](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-pix-expires_after_seconds) parameters in this case.

Example: `expire_with_delay@example.com` |
| `{any_prefix}fill_never@{any_domain}` | Simulates a Pix that never succeeds. It expires according to the [payment_method_options.pix.expires_at](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-pix-expires_at) or [payment_method_options.pix.expires_after_seconds](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-pix-expires_after_seconds) parameter. The [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) webhook arrives after the simulation completes.

Example: `fill_never@example.com` |

## Error codes

The following table details common error codes and recommended actions:

| Error code                                                | Recommended action                                                                                                                                                                                                                                                                                                                                                |
| --------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_intent_invalid_currency`                         | Enter a supported currency.                                                                                                                                                                                                                                                                                                                                       |
| `missing_required_parameter`                              | Check the error message for more information about the required parameter.                                                                                                                                                                                                                                                                                        |
| `payment_intent_payment_attempt_failed`                   | This code can appear in the [last_payment_error.code](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-last_payment_error-code) field of a PaymentIntent. Check the error message for a detailed failure reason and suggestion on error handling.                                                                                      |
| `payment_intent_authentication_failure`                   | This code can appear in the [last_payment_error.code](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-last_payment_error-code) field of a PaymentIntent. Check the error message for a detailed failure reason and suggestion on error handling. This error occurs when you manually trigger a failure when testing your integration. |
| `payment_intent_redirect_confirmation_without_return_url` | Provide a `return_url` when confirming a PaymentIntent.                                                                                                                                                                                                                                                                                                           |

# Direct API

> This is a Direct API for when payment-ui is direct-api. View the full page at https://docs.stripe.com/payments/pix/accept-a-payment?payment-ui=direct-api.

Stripe users can accept Pix payments from customers in Brazil. Customers pay by copying and pasting a Pix string or scanning a QR code directly in their bank apps.

## Set up Stripe [Server-side]

To get started, [create a Stripe account](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create a PaymentIntent [Server-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) is an object that represents your intent to collect payment from your customer and tracks the lifecycle of the payment process. Create a `PaymentIntent` on your server and specify the amount to collect and a supported currency. If you have an existing [Payment Intents](https://docs.stripe.com/payments/payment-intents.md) integration, add `pix` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["pix"],
  amount: 1000,
  currency: "brl",
});
```

The `PaymentIntent` includes a *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)). Send the client secret to your client to securely complete the payment process instead of passing the entire `PaymentIntent` object.

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

  <button id="submit-button">Pay with Pix</button>
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

## Test your integration

To test your integration:

1. Select Pix.
1. Enter the buyer’s details and tap **Pay**. In a testing environment, you can use `000.000.000-00` as a test tax identifier (CPF or CNPJ).
1. Click **Simulate scan** to open a Stripe-hosted Pix test payment page. From this page, you can either authorize or expire the test payment.

In live mode, the **Pay** button displays a Pix QR code. You need a Brazilian bank account with Pix enabled to complete or cancel this payment flow.

You can also set [payment_method.billing_details.email](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_data-billing_details-email) to the following values to test different scenarios.

| Email                       | Description                                                                                                                                                                                                                                                                                                                                                                                                   |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `{any_prefix}@{any_domain}` | Simulates a Pix that a customer pays after 3 minutes. The [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) arrives after approximately 3 minutes. In production, this webhook arrives immediately after the Pix is paid. |

Stripe ignores the [payment_method_options.pix.expires_at](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-pix-expires_at) and [payment_method_options.pix.expires_after_seconds](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-pix-expires_after_seconds) parameters in this case.

Example: `anything@example.com` |
| `{any_prefix}succeed_immediately@{any_domain}` | Simulates a Pix that your customer pays immediately. The [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) webhook arrives within several seconds. In production, this webhook arrives immediately after the Pix is paid.

Stripe ignores the [payment_method_options.pix.expires_at](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-pix-expires_at) and [payment_method_options.pix.expires_after_seconds](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-pix-expires_after_seconds) parameters in this case.

Example: `succeed_immediately@example.com` |
| `{any_prefix}expire_immediately@{any_domain}` | Simulates a Pix that expires before your customer pays. The [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) webhook arrives within several seconds.

Stripe ignores the [payment_method_options.pix.expires_at](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-pix-expires_at) and [payment_method_options.pix.expires_after_seconds](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-pix-expires_after_seconds) parameters in this case.

Example: `expire_immediately@example.com` |
| `{any_prefix}expire_with_delay@{any_domain}` | Simulates a Pix that expires before your customer pays. The [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) webhook arrives after approximately 3 minutes.

Stripe ignores the [payment_method_options.pix.expires_at](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-pix-expires_at) and [payment_method_options.pix.expires_after_seconds](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-pix-expires_after_seconds) parameters in this case.

Example: `expire_with_delay@example.com` |
| `{any_prefix}fill_never@{any_domain}` | Simulates a Pix that never succeeds. It expires according to the [payment_method_options.pix.expires_at](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-pix-expires_at) or [payment_method_options.pix.expires_after_seconds](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-pix-expires_after_seconds) parameter. The [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) webhook arrives after the simulation completes.

Example: `fill_never@example.com` |

## Expiration

Pix codes expire after the specified `expires_at` UNIX timestamp. After the Pix expires, confirm the PaymentIntent with another payment method or cancel it. Set expiration parameters in the [payment method options](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-pix) under the `pix` key.

A customer can’t pay a Pix after it expires.

| Field                   | Value                                                                                                                      | Default value                        | Required | Example                                                                                                                                                                                                              |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `expires_after_seconds` | The number of seconds before a pending Pix payment expires. Valid values are from 10 seconds to 259200 seconds (3 days)    | 14400 seconds (4 hours)              | No       | If you confirm a Pix on Monday at 14:00 and you set `expires_after_seconds` to 600, the Pix expires on Monday at 14:10. Note that the start time isn’t when the `PaymentIntent` is created, but when it’s confirmed. |
| `expires_at`            | A Unix timestamp that shows when the pending Pix payment expires. Valid values are from 10 seconds to 3 days in the future | The default is 4 hours in the future | No       | If you create a Pix on Monday at 14:00 and you set `expires_at` to 2 days in the future, the Pix expires on Wednesday at 14:00                                                                                       |

`expires_after_seconds` and `expires_at` are mutually exclusive. An error occurs if both are set. Both are also optional, and if neither is set, the expiration defaults to 4 hours from when the `PaymentIntent` is confirmed.

> The value returned on `expires_at` from the `next_action` response is the same as the input set on [payment_method_options.expires_at](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-pix-expires_at). Although, in real scenarios, the actual expiration timestamp might differ. This doesn’t impact your customer’s experience paying with Pix, but it’s recommended to rely on the [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md?event_types-payment_intent.payment_failed) event to consider if the payment intent has expired.

## Cancellation

You can cancel Pix payments before they expire by [canceling the PaymentIntent](https://docs.stripe.com/api/payment_intents/cancel.md) associated with the Pix payment.
