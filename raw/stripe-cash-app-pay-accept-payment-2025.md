<!-- Source URL: https://docs.stripe.com/payments/cash-app-pay/accept-a-payment -->
<!-- Fetched: 2026-05-07 -->

# Cash App Pay payments

Add support for Cash App Pay to your integration.

> Stripe can automatically present the relevant payment methods to your customers by evaluating currency, payment method restrictions, and other parameters.
>
> - Follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=checkout&ui=stripe-hosted) guide to build a Checkout integration that uses [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md).

- If you don’t want to use dynamic payment methods, follow the steps below to manually configure the payment methods in your Checkout integration.

This guides you through enabling Cash App Pay on [Checkout](https://docs.stripe.com/payments/checkout.md), our hosted checkout form, and shows the differences between accepting a card payment and a Cash App Pay payment.

## Determine compatibility

**Supported business locations**: US

**Supported currencies**: `usd`

**Presentment currencies**: `usd`

**Payment mode**: Yes

**Setup mode**: Yes

**Subscription mode**: Yes

A Checkout Session must satisfy all of the following conditions to support Cash App Pay payments:

- *Prices* (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) for all line items must be expressed in USD.

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

### Enable Cash App Pay as a payment method

When creating a new [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md), you need to:

1. Add `cashapp` to the list of `payment_method_types`.
1. Make sure all your `line_items` use the `usd` currency.

#### Stripe-hosted page

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        currency: "usd",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "cashapp"],
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
        currency: "usd",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "cashapp"],
  return_url: "https://example.com/return",
  ui_mode: "embedded_page",
});
```

### Fulfill your orders

After accepting a payment, learn how to [fulfill orders](https://docs.stripe.com/checkout/fulfillment.md).

## Test your integration

#### Mobile web app testing

To test your integration, choose Cash App Pay as the payment method and tap **Pay**. While testing, this redirects you to a test payment page where you can approve or decline the payment.

In live mode, tapping **Pay** redirects you to the Cash App mobile application—you don’t have the option to approve or decline the payment within Cash App. The payment is automatically approved after the redirect.

#### Desktop web app testing

To test your integration, scan the QR code with a QR code scanning application on your mobile device. While testing, the QR code payload contains a URL that redirects you to a test payment page where you can approve or decline the test payment.

In live mode, scanning the QR code redirects you to the Cash App mobile application—you don’t have the option to approve or decline the payment within Cash App. The payment is automatically approved after you scan the QR code.

## See also

- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment.md)
- [Customizing Checkout](https://docs.stripe.com/payments/checkout/customization.md)

# Checkout Sessions API

> This is a Checkout Sessions API for when payment-ui is elements and api-integration is checkout. View the full page at https://docs.stripe.com/payments/cash-app-pay/accept-a-payment?payment-ui=elements&api-integration=checkout.

To determine which API meets your business needs, see the [comparison guide](https://docs.stripe.com/payments/checkout-sessions-and-payment-intents-comparison.md).

Use the [Payment Element](https://docs.stripe.com/payments/payment-element.md) to embed a custom Stripe payment form in your website or application and offer payment methods to customers. For advanced configurations and customizations, refer to the [Accept a Payment](https://docs.stripe.com/payments/accept-a-payment.md) integration guide.

## Determine compatibility

**Supported business locations**: US

**Supported currencies**: `usd`

**Presentment currencies**: `usd`

**Payment mode**: Yes

**Setup mode**: Yes

**Subscription mode**: Yes

A Checkout Session must satisfy all of the following conditions to support Cash App Pay payments:

- *Prices* (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) for all line items must be expressed in USD.

## Set up the server [Server-side]

Use the official Stripe libraries to access the API from your application.

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create a Checkout Session [Server-side]

Add an endpoint on your server that creates a [Checkout Session](https://docs.stripe.com/api/checkout/sessions/create.md) and returns its [client secret](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-client_secret) to your front end. A Checkout Session represents your customer’s session as they pay for one-time purchases or subscriptions. Checkout Sessions expire 24 hours after creation.

We recommend using [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md) to dynamically display the most relevant eligible payment methods to each customer to maximize conversion. You can also [manually list payment methods](https://docs.stripe.com/payments/payment-methods/integration-options.md#listing-payment-methods-manually), which disables dynamic payment methods.

#### Manage payment methods from the Dashboard

#### TypeScript

```javascript
import express, {Express} from 'express';

const app: Express = express();

app.post('/create-checkout-session', async (req: Express.Request, res: Express.Response) => {
  const session = await stripe.checkout.sessions.create({
    line_items: [
      {
        price_data: {
          currency: 'usd',
          product_data: {
            name: 'T-shirt',
          },
          unit_amount: 1099,
        },
        quantity: 1,
      },
    ],
    mode: 'payment',
    ui_mode: 'elements',
    return_url: 'https://example.com/return?session_id={CHECKOUT_SESSION_ID}'
  });

  res.json({checkoutSessionClientSecret: session.client_secret});
});

app.listen(3000, () => {
  console.log('Running on port 3000');
});
```

#### Manually list payment methods

#### TypeScript

```javascript
import express, {Express} from 'express';

const app: Express = express();

app.post('/create-checkout-session', async (req: Express.Request, res: Express.Response) => {
  const session = await stripe.checkout.sessions.create({
    line_items: [
      {
        price_data: {
          currency: 'usd',
          product_data: {
            name: 'T-shirt',
          },
          unit_amount: 1099,
        },
        quantity: 1,
      },
    ],
    mode: 'payment',
    ui_mode: 'elements',
    payment_method_types: ['cashapp'],
    return_url: 'https://example.com/return?session_id={CHECKOUT_SESSION_ID}'
  });

  res.json({checkoutSessionClientSecret: session.client_secret});
});

app.listen(3000, () => {
  console.log('Running on port 3000');
});
```

## Set up the front end [Client-side]

#### HTML + JS

Include the Stripe.js script on your checkout page by adding it to the `head` of your HTML file. Always load Stripe.js directly from js.stripe.com to remain PCI compliant. Don’t include the script in a bundle or host a copy of it yourself.

Make sure you’re on the latest Stripe.js version by including the following script tag `<script src=“https://js.stripe.com/dahlia/stripe.js”></script>`. Learn more about [Stripe.js versioning](https://docs.stripe.com/sdks/stripejs-versioning.md).

```html
<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/dahlia/stripe.js"></script>
</head>
```

> Stripe provides an npm package that you can use to load Stripe.js as a module. See the [project on GitHub](https://github.com/stripe/stripe-js). Version [7.0.0](https://www.npmjs.com/package/%40stripe/stripe-js/v/7.0.0) or later is required.

Initialize stripe.js.

```js
// Set your publishable key: remember to change this to your live publishable key in production
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");
```

#### React

Install [React Stripe.js](https://www.npmjs.com/package/@stripe/react-stripe-js) and the [Stripe.js loader](https://www.npmjs.com/package/@stripe/stripe-js) from the npm public registry. You need at least version 5.0.0 for React Stripe.js and version 8.0.0 for the Stripe.js loader.

```bash
npm install --save @stripe/react-stripe-js@^5.0.0 @stripe/stripe-js@^8.0.0
```

Initialize a `stripe` instance on your front end with your publishable key.

```javascript
import { loadStripe } from "@stripe/stripe-js";
const stripe = loadStripe("<<YOUR_PUBLISHABLE_KEY>>");
```

## Initialize Checkout [Client-side]

#### HTML + JS

Call [initCheckoutElementsSdk](https://docs.stripe.com/js/custom_checkout/init), passing in `clientSecret`.

`initCheckoutElementsSdk` returns a [Checkout](https://docs.stripe.com/js/custom_checkout) object that contains data from the Checkout Session and methods to update it.

Read the `total` and `lineItems` from [actions.getSession()](https://docs.stripe.com/js/custom_checkout/session), and display them in your UI. This lets you turn on new features with minimal code changes. For example, adding [manual currency prices](https://docs.stripe.com/payments/custom/localize-prices/manual-currency-prices.md) requires no UI changes if you display the `total`.

```html
<div id="checkout-container"></div>
```

```javascript
const clientSecret = fetch("/create-checkout-session", { method: "POST" })
  .then((response) => response.json())
  .then((json) => json.client_secret);

const checkout = stripe.initCheckoutElementsSdk({ clientSecret });
const loadActionsResult = await checkout.loadActions();

if (loadActionsResult.type === "success") {
  const session = loadActionsResult.actions.getSession();
  const checkoutContainer = document.getElementById("checkout-container");

  checkoutContainer.append(JSON.stringify(session.lineItems, null, 2));
  checkoutContainer.append(document.createElement("br"));
  checkoutContainer.append(`Total: ${session.total.total.amount}`);
}
```

#### React

Wrap your application with the [CheckoutElementsProvider](https://docs.stripe.com/js/react_stripe_js/checkout/checkout_provider) component, passing in `clientSecret` and the `stripe` instance.

```jsx
import React from "react";
import { CheckoutElementsProvider } from "@stripe/react-stripe-js/checkout";
import CheckoutForm from "./CheckoutForm";

const clientSecret = fetch("/create-checkout-session", { method: "POST" })
  .then((response) => response.json())
  .then((json) => json.client_secret);

const App = () => {
  return (
    <CheckoutElementsProvider stripe={stripe} options={{ clientSecret }}>
      <CheckoutForm />
    </CheckoutElementsProvider>
  );
};

export default App;
```

Access the [Checkout](https://docs.stripe.com/js/custom_checkout) object in your checkout form component by using the `useCheckoutElements()` hook. The `Checkout` object contains data from the Checkout Session and methods to update it.

Read the `total` and `lineItems` from the `Checkout` object, and display them in your UI. This lets you enable features with minimal code changes. For example, adding [manual currency prices](https://docs.stripe.com/payments/custom/localize-prices/manual-currency-prices.md) requires no UI changes if you display the `total`.

```jsx
import React from "react";
import { useCheckoutElements } from "@stripe/react-stripe-js/checkout";

const CheckoutForm = () => {
  const checkoutState = useCheckoutElements();

  if (checkoutState.type === "loading") {
    return <div>Loading...</div>;
  }

  if (checkoutState.type === "error") {
    return <div>Error: {checkoutState.error.message}</div>;
  }

  return (
    <form>
      {JSON.stringify(checkoutState.checkout.lineItems, null, 2)}
      {/* A formatted total amount */}
      Total: {checkoutState.checkout.total.total.amount}
    </form>
  );
};
```

## Collect customer email [Client-side]

#### HTML + JS

You must provide a valid customer email when completing a Checkout Session.

These instructions create an email input and use [updateEmail](https://docs.stripe.com/js/custom_checkout/update_email) from the `Checkout` object.

Alternatively, you can:

- Pass in [customer_email](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer_email), [customer_account](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer_account) (for customers represented as customer-configured `Account` objects), or [customer](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer) (for customers represented as `Customer` objects) when creating the Checkout Session. Stripe validates emails provided this way.
- Pass in an email you already validated on [checkout.confirm](https://docs.stripe.com/js/custom_checkout/confirm).

```html
<input type="text" id="email" />
<div id="email-errors"></div>
```

```javascript
const checkout = stripe.initCheckoutElementsSdk({ clientSecret });
const loadActionsResult = await checkout.loadActions();

if (loadActionsResult.type === "success") {
  const { actions } = loadActionsResult;
  const emailInput = document.getElementById("email");
  const emailErrors = document.getElementById("email-errors");

  emailInput.addEventListener("input", () => {
    // Clear any validation errors
    emailErrors.textContent = "";
  });

  emailInput.addEventListener("blur", () => {
    const newEmail = emailInput.value;
    actions.updateEmail(newEmail).then((result) => {
      if (result.error) {
        emailErrors.textContent = result.error.message;
      }
    });
  });
}
```

#### React

You must provide a valid customer email when completing a Checkout Session.

These instructions create an email input and use [updateEmail](https://docs.stripe.com/js/react_stripe_js/checkout/update_email) from the `Checkout` object.

Alternatively, you can:

- Pass in [customer_email](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer_email), [customer_account](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer_account) (for customers represented as customer-configured `Account` objects), or [customer](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer) (for customers represented as `Customer` objects) when creating the Checkout Session. Stripe validates emails provided this way.
- Pass in an email you already validated on [confirm](https://docs.stripe.com/js/react_stripe_js/checkout/confirm).

```jsx
import React from "react";
import { useCheckoutElements } from "@stripe/react-stripe-js/checkout";

const EmailInput = () => {
  const checkoutState = useCheckoutElements();
  const [email, setEmail] = React.useState("");
  const [error, setError] = React.useState(null);

  if (checkoutState.type === "loading") {
    return <div>Loading...</div>;
  } else if (checkoutState.type === "error") {
    return <div>Error: {checkoutState.error.message}</div>;
  }

  const handleBlur = () => {
    checkoutState.checkout.updateEmail(email).then((result) => {
      if (result.type === "error") {
        setError(result.error);
      }
    });
  };

  const handleChange = (e) => {
    setError(null);
    setEmail(e.target.value);
  };

  return (
    <div>
      <label htmlFor="checkout-form-email">Email</label>
      <input
        id="checkout-form-email"
        type="email"
        value={email}
        onChange={handleChange}
        onBlur={handleBlur}
      />
      {error && <div>{error.message}</div>}
    </div>
  );
};

export default EmailInput;
```

## Collect payment details [Client-side]

Collect payment details on the client with the [Payment Element](https://docs.stripe.com/payments/payment-element.md). The Payment Element is a prebuilt UI component that simplifies collecting payment details for a variety of payment methods.

The Payment Element contains an iframe that securely sends payment information to Stripe over an HTTPS connection. Avoid placing the Payment Element within another iframe because some payment methods require redirecting to another page for payment confirmation.

If you choose to use an iframe and want to accept Apple Pay or Google Pay, the iframe must have the [allow](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe#attr-allowpaymentrequest) attribute set to equal `"payment *"`.

The checkout page address must start with `https://` rather than `http://` for your integration to work. You can test your integration without using HTTPS, but remember to [enable it](https://docs.stripe.com/security/guide.md#tls) when you’re ready to accept live payments.

#### HTML + JS

First, create a container DOM element to mount the [Payment Element](https://docs.stripe.com/payments/payment-element.md). Then create an instance of the `Payment Element` using [checkout.createPaymentElement](https://docs.stripe.com/js/custom_checkout/create_payment_element) and mount it by calling [element.mount](https://docs.stripe.com/js/element/mount), providing either a CSS selector or the container DOM element.

```html
<div id="payment-element"></div>
```

```javascript
const paymentElement = checkout.createPaymentElement();
paymentElement.mount("#payment-element");
```

See the [Stripe.js docs](https://docs.stripe.com/js/custom_checkout/create_payment_element#custom_checkout_create_payment_element-options) to view the supported options.

You can [customize the appearance](https://docs.stripe.com/payments/checkout/customization/appearance.md) of all Elements by passing [elementsOptions.appearance](https://docs.stripe.com/js/custom_checkout/init#custom_checkout_init-options-elementsOptions-appearance) when initializing Checkout on the front end.

#### React

Mount the [Payment Element](https://docs.stripe.com/payments/payment-element.md) component within the [CheckoutElementsProvider](https://docs.stripe.com/js/react_stripe_js/checkout/checkout_provider).

```jsx
import React from "react";
import {
  PaymentElement,
  useCheckoutElements,
} from "@stripe/react-stripe-js/checkout";

const CheckoutForm = () => {
  const checkoutState = useCheckoutElements();

  if (checkoutState.type === "loading") {
    return <div>Loading...</div>;
  }

  if (checkoutState.type === "error") {
    return <div>Error: {checkoutState.error.message}</div>;
  }

  return (
    <form>
      {JSON.stringify(checkoutState.checkout.lineItems, null, 2)}
      {/* A formatted total amount */}
      Total: {checkoutState.checkout.total.total.amount}
      <PaymentElement options={{ layout: "accordion" }} />
    </form>
  );
};

export default CheckoutForm;
```

See the [Stripe.js docs](https://docs.stripe.com/js/custom_checkout/create_payment_element#custom_checkout_create_payment_element-options) to view the supported options.

You can [customize the appearance](https://docs.stripe.com/payments/checkout/customization/appearance.md) of all Elements by passing [elementsOptions.appearance](https://docs.stripe.com/js/react_stripe_js/checkout/checkout_provider#react_checkout_provider-options-elementsOptions-appearance) to the [CheckoutElementsProvider](https://docs.stripe.com/js/react_stripe_js/checkout/checkout_provider).

## Submit the payment [Client-side]

#### HTML + JS

Render a **Pay** button that calls [confirm](https://docs.stripe.com/js/custom_checkout/confirm) from the `Checkout` instance to submit the payment.

```html
<button id="pay-button">Pay</button>
<div id="confirm-errors"></div>
```

```js
const checkout = stripe.initCheckoutElementsSdk({ clientSecret });

checkout.on("change", (session) => {
  document.getElementById("pay-button").disabled = !session.canConfirm;
});

const loadActionsResult = await checkout.loadActions();

if (loadActionsResult.type === "success") {
  const { actions } = loadActionsResult;
  const button = document.getElementById("pay-button");
  const errors = document.getElementById("confirm-errors");
  button.addEventListener("click", () => {
    // Clear any validation errors
    errors.textContent = "";

    actions.confirm().then((result) => {
      if (result.type === "error") {
        errors.textContent = result.error.message;
      }
    });
  });
}
```

#### React

Render a **Pay** button that calls [confirm](https://docs.stripe.com/js/custom_checkout/confirm) from [useCheckoutElements](https://docs.stripe.com/js/react_stripe_js/checkout/use_checkout_elements) to submit the payment.

```jsx
import React from "react";
import { useCheckoutElements } from "@stripe/react-stripe-js/checkout";

const PayButton = () => {
  const checkoutState = useCheckoutElements();
  const [loading, setLoading] = React.useState(false);
  const [error, setError] = React.useState(null);

  if (checkoutState.type !== "success") {
    return null;
  }

  const handleClick = () => {
    setLoading(true);
    checkoutState.checkout.confirm().then((result) => {
      if (result.type === "error") {
        setError(result.error);
      }
      setLoading(false);
    });
  };

  return (
    <div>
      <button
        disabled={!checkoutState.checkout.canConfirm || loading}
        onClick={handleClick}
      >
        Pay
      </button>
      {error && <div>{error.message}</div>}
    </div>
  );
};

export default PayButton;
```

## Test your integration

#### Mobile web app testing

To test your integration, choose Cash App Pay as the payment method and tap **Pay**. While testing, this redirects you to a test payment page where you can approve or decline the payment.

In live mode, tapping **Pay** redirects you to the Cash App mobile application—you don’t have the option to approve or decline the payment within Cash App. The payment is automatically approved after the redirect.

#### Desktop web app testing

To test your integration, scan the QR code with a QR code scanning application on your mobile device. While testing, the QR code payload contains a URL that redirects you to a test payment page where you can approve or decline the test payment.

In live mode, scanning the QR code redirects you to the Cash App mobile application—you don’t have the option to approve or decline the payment within Cash App. The payment is automatically approved after you scan the QR code.

# Payment Intents API

> This is a Payment Intents API for when payment-ui is elements and api-integration is paymentintents. View the full page at https://docs.stripe.com/payments/cash-app-pay/accept-a-payment?payment-ui=elements&api-integration=paymentintents.

This guide shows you how to embed a custom Stripe payment form in your website or application using the [Payment Element](https://docs.stripe.com/payments/payment-element.md). The Payment Element allows you to support Cash App Pay and other payment methods automatically. For advanced configurations and customizations, refer to the [Accept a Payment](https://docs.stripe.com/payments/accept-a-payment.md) integration guide.

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

Create a PaymentIntent on your server with an amount and currency. You can manage payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods). Stripe handles the return of eligible payment methods based on factors such as the transaction’s amount, currency, and payment flow. Before creating the Payment Intent, make sure to turn **Cash App Pay** on in the [payment methods settings](https://dashboard.stripe.com/settings/payment_methods) page.

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
  amount: 1099,
  currency: "usd",
  payment_method_types: ["cashapp"],
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

Customers can authenticate Cash App Pay transactions with mobile or desktop apps. The client the customer is using determines the authentication method after calling `confirmPayment`.

#### Mobile app authentication

After calling `confirmPayment`, the customers are redirected to Cash App to approve or decline the payment. After the customers authorize the payment, they’re redirected to the Payment Intent’s `return_url`. Stripe adds `payment_intent`, `payment_intent_client_secret`, `redirect_pm_type`, and `redirect_status` as URL query parameters (along with any existing query parameters in the `return_url`).

An authentication session expires after 60 minutes, and the PaymentIntent’s status transitions back to `require_payment_method`. After the status transitions, the customer sees a payment error and must restart the payment process.

#### Desktop web app authentication

After calling confirmPayment, a QR code displays on the webpage. Your customers can scan the QR code using either their mobile device’s camera or the Cash App mobile app and authenticate the payment using Cash App Pay. A few seconds after customers authenticate the payment successfully, the QR code modal closes automatically and you can fulfill the order. Stripe redirects to the `return_url` when payment is complete. If you don’t want to redirect after payment on web, pass `redirect: if_required` to the Payment Element.

An authentication session expires after 60 minutes. You can refresh the QR code up to 20 times before the PaymentIntent’s status transitions back to `require_payment_method`. After the status transitions, the customer sees a payment error and must restart the payment process.

## Optional: Separate authorization and capture

You can separate authorization and capture to create a charge now, but capture funds later. Stripe cancels the PaymentIntent and sends a [payment_intent.canceled](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.canceled) event if the payment isn’t captured during the 7-day window.

If you know that you can’t capture the payment, we recommend [canceling the PaymentIntent](https://docs.stripe.com/refunds.md#cancel-payment) instead of waiting for the 7-day window to elapse.

### 1. Tell Stripe to authorize only

To indicate that you want separate authorization and capture, set [capture_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-capture_method) to `manual` when creating the PaymentIntent. This parameter instructs Stripe to only authorize the amount on the customer’s Cash App Pay account.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 6000,
  confirm: true,
  currency: "usd",
  payment_method_types: ["cashapp"],
  payment_method_data: {
    type: "cashapp",
  },
  capture_method: "manual",
  return_url: "https://www.example.com/checkout/done",
});
```

### 2. Capture the funds

After the authorization succeeds, the PaymentIntent [status](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-status) transitions to `requires_capture`. To capture the authorized funds, make a PaymentIntent [capture](https://docs.stripe.com/api/payment_intents/capture.md) request.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.capture(
  "{PAYMENT_INTENT_ID}",
);
```

The total authorized amount is captured by default. You can also specify `amount_to_capture` which can be less or equal to the total.

### (Optional) Cancel the authorization

If you need to cancel an authorization, you can [cancel the PaymentIntent](https://docs.stripe.com/api/payment_intents/cancel.md).

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

#### Mobile web app testing

To test your integration, choose Cash App Pay as the payment method and tap **Pay**. While testing, this redirects you to a test payment page where you can approve or decline the payment.

In live mode, tapping **Pay** redirects you to the Cash App mobile application—you don’t have the option to approve or decline the payment within Cash App. The payment is automatically approved after the redirect.

#### Desktop web app testing

To test your integration, scan the QR code with a QR code scanning application on your mobile device. While testing, the QR code payload contains a URL that redirects you to a test payment page where you can approve or decline the test payment.

In live mode, scanning the QR code redirects you to the Cash App mobile application—you don’t have the option to approve or decline the payment within Cash App. The payment is automatically approved after you scan the QR code.

## Failed payments

Cash App Pay uses multiple data points to decide when to decline a transaction (for example, their AI model detected high consumer fraud risk for the transaction, or the consumer has revoked your permission to charge them in Cash App).

In these cases, the [PaymentMethod](https://docs.stripe.com/api/payment_methods/object.md) is detached and the [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) object’s status automatically transitions to `requires_payment_method`.

Other than a payment being declined, for a Cash App Pay [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) with a status of `requires_action`, customers must complete the payment within 10 minutes after they’re redirected to Cash App. If no action is taken after 10 minutes, the [PaymentMethod](https://docs.stripe.com/api/payment_methods/object.md) is detached and the [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) object’s status automatically transitions to `requires_payment_method`.

When this happens, the Payment Element renders error messages and instructs your customer to retry using a different payment method.

## Error codes

The following table details common error codes and recommended actions:

| Error Code                                                | Recommended Action                                                                                                                                                                                                                                                           |
| --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_intent_invalid_currency`                         | Enter the appropriate currency. Cash App Pay only supports `usd`.                                                                                                                                                                                                            |
| `missing_required_parameter`                              | Check the error message for more information about the required parameter.                                                                                                                                                                                                   |
| `payment_intent_payment_attempt_failed`                   | This code can appear in the [last_payment_error.code](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-last_payment_error-code) field of a PaymentIntent. Check the error message for a detailed failure reason and suggestion on error handling. |
| `payment_intent_redirect_confirmation_without_return_url` | Provide a `return_url` when confirming a PaymentIntent with Cash App Pay.                                                                                                                                                                                                    |

# Direct API

> This is a Direct API for when payment-ui is direct-api. View the full page at https://docs.stripe.com/payments/cash-app-pay/accept-a-payment?payment-ui=direct-api.

We recommend that you implement the [Elements](https://docs.stripe.com/payments/cash-app-pay/accept-a-payment.md?payment-ui=elements) integration. An Elements integration allows you to add Cash App Pay and other payment methods with significantly less effort than a Direct API integration. Accepting Cash App Pay using a Direct API integration consists of:

- Creating a [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) object to track a payment.
- Submitting the payment to Stripe for processing.
- Authenticating the payment (through a mobile application redirect or QR code).
- Handling post-payment events to redirect the customer after an order succeeds or fails.

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create a PaymentIntent [Server-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) is an object that represents your intent to collect payment from a customer and tracks the lifecycle of the payment process through each stage.

To create a `PaymentIntent` on your server:

- Specify the amount to collect and the currency.
- Add `cashapp` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your `PaymentIntent`. Make sure Cash App Pay is enabled in the [Dashboard](https://dashboard.stripe.com/settings/payment_methods).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 6000,
  currency: "usd",
  payment_method_types: ["cashapp"],
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

## Submit the payment to Stripe and authenticate transactions client-side

In this step, you’ll complete Cash App Pay payments on the client with [Stripe.js](https://docs.stripe.com/payments/elements.md). To authenticate a transaction, you must redirect the customer to Cash App.

Include the Stripe.js script on your checkout page by adding it to the `head` of your HTML file.

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

Use `stripe.confirmCashappPayment` to confirm the PaymentIntent on the client side.

```javascript
const form = document.getElementById("payment-form");

form.addEventListener("submit", function (event) {
  event.preventDefault();

  // Pass the clientSecret obtained from the server in step 2 as the first argument
  stripe.confirmCashappPayment(clientSecret, {
    payment_method: {
      type: "cashapp",
    },
    return_url: "https://www.example.com/checkout/done",
  });
});
```

> `confirmCashappPayment` only redirects mobile browsers to your `return_url`, it doesn’t redirect desktop browsers. You can manually redirect customers using desktop browsers to your return URL after the returned promise resolves.

Customers can authenticate Cash App Pay transactions with mobile or desktop apps. The client the customer is using determines the authentication method after calling `confirmCashappPayment`.

#### Mobile application authentication

After calling `confirmCashappPayment`, the customers are redirected to Cash App to approve or decline the payment. After the customers authorize the payment, they’re redirected to the Payment Intent’s `return_url`. Stripe adds `payment_intent`, `payment_intent_client_secret`, `redirect_pm_type`, and `redirect_status` as URL query parameters (along with any existing query parameters in the `return_url`).

An authentication session expires after 60 minutes, and the PaymentIntent’s status transitions back to `require_payment_method`. After the status transitions, the customer sees a payment error and must restart the payment process.

#### Desktop web app authentication

After calling `confirmCashappPayment`, a QR code displays on the webpage. Your customers can scan the QR code using either their mobile device’s camera or the Cash App mobile application and authenticate the payment. A few seconds after customers authenticate the payment successfully, the QR code modal closes automatically and you can fulfill the order.

An authentication session expires after 60 minutes. You can refresh the QR code up to 20 times before the PaymentIntent’s status transitions back to `require_payment_method`. After the status transitions, the customer sees a payment error and must restart the payment process.

## Optional: Handle redirect and authentication manually

We recommend using Stripe.js to handle redirects and authentication with `confirmCashappPayment`. However, you can also handle redirects and authentication manually on your server.

Specify `handleActions: false` in the `confirmCashappPayment` call.

```javascript
const form = document.getElementById("payment-form");

form.addEventListener("submit", function (event) {
  event.preventDefault();

  // Set the clientSecret here you got in Step 2
  stripe
    .confirmCashappPayment(
      clientSecret,
      {
        payment_method_data: {
          type: "cashapp",
        },
        return_url: "https://www.example.com/checkout/done",
      },
      {
        handleActions: false,
      },
    )
    .then((result) => {
      if (result.error) {
        // Display error to your customer.
      } else if (result.paymentIntent.status === "requires_action") {
        const nextAction =
          result.paymentIntent.next_action
            .cashapp_handle_redirect_or_display_qr_code;
        const expiresAt = nextAction.qr_code.expires_at;
        if (IS_MOBILE) {
          // This URL redirects the customer to Cash App to approve or decline the payment.
          const mobileAuthUrl = nextAction.mobile_auth_url;
        } else if (IS_DESKTOP) {
          // Render the QR code and display it to the customer using the below image source.
          const imageUrlSvg = nextAction.qr_code.image_url_svg;
          const imageUrlPng = nextAction.qr_code.image_url_png;
        }
      }
    });
});
```

#### Mobile application authentication

If a customer is paying with Cash App Pay on a mobile device:

1. Redirect the customer to the URL set as the `result.paymentIntent.next_action.cashapp_handle_redirect_or_display_qr_code.mobile_auth_url` property. This redirects the customer to Cash App to approve or decline the payment.

1. After the customer authorizes the payment, they’re redirected to the Payment Intent’s `return_url`. Stripe adds `payment_intent`, `payment_intent_client_secret`, `redirect_pm_type`, and `redirect_status` as URL query parameters (along with any existing query parameters in the `return_url`).

1. The `mobile_auth_url` expires after 30 seconds. In case the customer isn’t redirected to `mobile_auth_url` before expiration, call [stripe.retrievePaymentIntent](https://docs.stripe.com/js/payment_intents/retrieve_payment_intent) to get a new `mobile_auth_url`.

#### Desktop web app authentication

If a customer is paying with Cash App Pay from a desktop web app:

1. Render the QR code and display it to the customer. Use `result.paymentIntent.next_action.cashapp_handle_redirect_or_display_qr_code.qr_code.image_url_png` or `image_url_svg` as an image source. For example:

   ```html
   <img
     src="${result.paymentIntent.next_action.cashapp_handle_redirect_or_display_qr_code.qr_code.image_url_png}"
   />
   ```

1. The customer can scan the QR code using either their mobile device’s camera or the Cash App mobile application. They can then authenticate the payment.

1. Make the customer wait on the QR code page until Stripe fulfills the order and you know the outcome of the payment. Stripe sends the outcome in a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) or a [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) webhook. You can either consume these payment intent webhooks server-side and return the results to the client (for example, with a persistent connection using web-socket) or implement client-side polling on your webpage to periodically fetch the status of the [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md).

1. The QR code expires after 30 seconds. On expiration, call [stripe.retrievePaymentIntent](https://docs.stripe.com/js/payment_intents/retrieve_payment_intent) to get a new QR code from `result.paymentIntent.next_action.cashapp_handle_redirect_or_display_qr_code.qr_code`.

An authentication session expires after 60 minutes. You can refresh the QR code up to 20 times before the PaymentIntent’s status transitions back to `require_payment_method`. After the status transitions, the customer sees a payment error and must restart the payment process.

## Optional: Separate authorization and capture

You can separate authorization and capture to create a charge now, but capture funds later. Stripe cancels the PaymentIntent and sends a [payment_intent.canceled](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.canceled) event if the payment isn’t captured during the 7-day window.

If you know that you can’t capture the payment, we recommend [canceling the PaymentIntent](https://docs.stripe.com/refunds.md#cancel-payment) instead of waiting for the 7-day window to elapse.

### 1. Tell Stripe to authorize only

To indicate that you want separate authorization and capture, set [capture_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-capture_method) to `manual` when creating the PaymentIntent. This parameter instructs Stripe to only authorize the amount on the customer’s Cash App Pay account.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 6000,
  confirm: true,
  currency: "usd",
  payment_method_types: ["cashapp"],
  payment_method_data: {
    type: "cashapp",
  },
  capture_method: "manual",
  return_url: "https://www.example.com/checkout/done",
});
```

### 2. Capture the funds

After the authorization succeeds, the PaymentIntent [status](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-status) transitions to `requires_capture`. To capture the authorized funds, make a PaymentIntent [capture](https://docs.stripe.com/api/payment_intents/capture.md) request.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.capture(
  "{PAYMENT_INTENT_ID}",
);
```

The total authorized amount is captured by default. You can also specify `amount_to_capture` which can be less or equal to the total.

### (Optional) Cancel the authorization

If you need to cancel an authorization, you can [cancel the PaymentIntent](https://docs.stripe.com/api/payment_intents/cancel.md).

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

#### Mobile web app testing

To test your integration, choose Cash App Pay as the payment method and tap **Pay**. While testing, this redirects you to a test payment page where you can approve or decline the payment.

In live mode, tapping **Pay** redirects you to the Cash App mobile application—you don’t have the option to approve or decline the payment within Cash App. The payment is automatically approved after the redirect.

#### Desktop web app testing

To test your integration, scan the QR code with a QR code scanning application on your mobile device. While testing, the QR code payload contains a URL that redirects you to a test payment page where you can approve or decline the test payment.

In live mode, scanning the QR code redirects you to the Cash App mobile application—you don’t have the option to approve or decline the payment within Cash App. The payment is automatically approved after you scan the QR code.

## Failed payments

Cash App Pay uses multiple data points to decide when to decline a transaction (for example, their AI model detected high consumer fraud risk for the transaction, or the consumer has revoked your permission to charge them in Cash App).

In these cases, the [PaymentMethod](https://docs.stripe.com/api/payment_methods/object.md) is detached and the [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) object’s status automatically transitions to `requires_payment_method`.

Other than a payment being declined, for a Cash App Pay [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) with a status of `requires_action`, customers must complete the payment within 10 minutes after they’re redirected to Cash App. If no action is taken after 10 minutes, the [PaymentMethod](https://docs.stripe.com/api/payment_methods/object.md) is detached and the [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) object’s status automatically transitions to `requires_payment_method`.

When this happens, the Payment Element renders error messages and instructs your customer to retry using a different payment method.

## Error codes

The following table details common error codes and recommended actions:

| Error Code                                                | Recommended Action                                                                                                                                                                                                                                                           |
| --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_intent_invalid_currency`                         | Enter the appropriate currency. Cash App Pay only supports `usd`.                                                                                                                                                                                                            |
| `missing_required_parameter`                              | Check the error message for more information about the required parameter.                                                                                                                                                                                                   |
| `payment_intent_payment_attempt_failed`                   | This code can appear in the [last_payment_error.code](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-last_payment_error-code) field of a PaymentIntent. Check the error message for a detailed failure reason and suggestion on error handling. |
| `payment_intent_redirect_confirmation_without_return_url` | Provide a `return_url` when confirming a PaymentIntent with Cash App Pay.                                                                                                                                                                                                    |

# iOS

> This is a iOS for when payment-ui is mobile and platform is ios. View the full page at https://docs.stripe.com/payments/cash-app-pay/accept-a-payment?payment-ui=mobile&platform=ios.

We recommend you use the [Mobile Payment Element](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=mobile&platform=ios), an embeddable payment form, to add Cash App Pay and other payment methods to your integration with the least amount of effort.

This guide covers how to accept Cash App Pay from your native mobile application using your own custom payment form.

If you’re accepting Cash App Pay from your native mobile application, your customers are redirected to the Cash App mobile application for authentication. The purchase is completed in the Cash App mobile application, and the customer is redirected back to your native mobile application.

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

- Specify the amount to collect and the currency.
- Add `cashapp` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your `PaymentIntent`. Make sure Cash App Pay is enabled in the [Dashboard](https://dashboard.stripe.com/settings/payment_methods).
- Set `payment_method_data[type]` to `cashapp` to create a *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) and immediately use it with this PaymentIntent.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 6000,
  currency: "usd",
  payment_method_types: ["cashapp"],
  payment_method_data: {
    type: "cashapp",
  },
  return_url: "payments-example://stripe-redirect",
});
```

The returned PaymentIntent includes a *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)), that you’ll use to *confirm* (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) the PaymentIntent. Send the client secret back to the client so you can use it in the next step.

### Client-side

On the client, request a PaymentIntent from your server and store its *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)).

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

When a customer taps to pay with Cash App Pay, confirm the `PaymentIntent` to complete the payment. Configure an `STPPaymentIntentParams` object with the `PaymentIntent` [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret).

The client secret is different from your API keys that authenticate Stripe API requests. Handle it carefully, as it can complete the charge. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

### Set up a return URL

The iOS SDK presents a webview in your app to complete the Cash App Pay payment. When authentication is finished, the webview can automatically dismiss itself instead of having your customer close it. To enable this behavior, configure a custom URL scheme or universal link and set up your app delegate to forward the URL to the SDK.

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

// This method handles opening universal link URLs (for example, "https://example.com/stripe_ios_callback")
func application(_ application: UIApplication, continue userActivity: NSUserActivity, restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
    if userActivity.activityType == NSUserActivityTypeBrowsingWeb {
        if let url = userActivity.webpageURL {
            let stripeHandled = StripeAPI.handleURLCallback(with: url)
            if (stripeHandled) {
                return true
            } else {
                // This was not a Stripe url – handle the URL normally as you would
            }
        }
    }
    return false
}
```

Pass the URL as the `return_url` when you confirm the PaymentIntent. After webview-based authentication finishes, Stripe redirects the user to the `return_url`.

### Confirm Cash App Pay payment

Complete the payment by calling `STPPaymentHandler confirmPayment`. This presents a webview where the customer can complete the payment with Cash App Pay. Upon completion, the completion block is called with the result of the payment.

#### Swift

```swift
let paymentIntentParams = STPPaymentIntentParams(clientSecret: paymentIntentClientSecret)

// Cash App Pay doesn't require additional parameters so we only need to pass the initialized
// STPPaymentMethodCashAppParams instance to STPPaymentMethodParams
let cashApp = STPPaymentMethodCashAppParams()
let paymentMethodParams = STPPaymentMethodParams(cashApp: cashApp, billingDetails: nil, metadata: nil)

paymentIntentParams.paymentMethodParams = paymentMethodParams
paymentIntentParams.returnURL = "payments-example://stripe-redirect"

STPPaymentHandler.shared().confirmPayment(paymentIntentParams,
                                          with: self)
{ (handlerStatus, paymentIntent, error) in
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

## Optional: Separate authorization and capture

You can separate authorization and capture to create a charge now, but capture funds later. Stripe cancels the PaymentIntent and sends a [payment_intent.canceled](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.canceled) event if the payment isn’t captured during the 7-day window.

If you know that you can’t capture the payment, we recommend [canceling the PaymentIntent](https://docs.stripe.com/refunds.md#cancel-payment) instead of waiting for the 7-day window to elapse.

### 1. Tell Stripe to authorize only

To indicate that you want separate authorization and capture, set [capture_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-capture_method) to `manual` when creating the PaymentIntent. This parameter instructs Stripe to only authorize the amount on the customer’s Cash App Pay account.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 6000,
  confirm: true,
  currency: "usd",
  payment_method_types: ["cashapp"],
  payment_method_data: {
    type: "cashapp",
  },
  capture_method: "manual",
  return_url: "https://www.example.com/checkout/done",
});
```

### 2. Capture the funds

After the authorization succeeds, the PaymentIntent [status](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-status) transitions to `requires_capture`. To capture the authorized funds, make a PaymentIntent [capture](https://docs.stripe.com/api/payment_intents/capture.md) request.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.capture(
  "{PAYMENT_INTENT_ID}",
);
```

The total authorized amount is captured by default. You can also specify `amount_to_capture` which can be less or equal to the total.

### (Optional) Cancel the authorization

If you need to cancel an authorization, you can [cancel the PaymentIntent](https://docs.stripe.com/api/payment_intents/cancel.md).

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

Test your Cash App Pay integration with your test API keys by viewing the redirect page. You can test the successful payment case by authenticating the payment on the redirect page. The [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) transitions from `requires_action` to `succeeded`.

To test the case where the user fails to authenticate, use your test API keys and view the redirect page. On the redirect page, click **Fail test payment**. The [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) transitions from `requires_action` to `requires_payment_method`.

For test manual capture PaymentIntents, the uncaptured [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) auto-expires 7 days after successful authorization.

In live mode, tapping **Pay** redirects you to the Cash App mobile application—you don’t have the option to approve or decline the payment within Cash App. The payment is automatically approved after the redirect.

## Failed payments

Cash App Pay uses multiple data points to decide when to decline a transaction (for example, their AI model detected high consumer fraud risk for the transaction, or the consumer has revoked your permission to charge them in Cash App).

In these cases, the [PaymentMethod](https://docs.stripe.com/api/payment_methods/object.md) is detached and the [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) object’s status automatically transitions to `requires_payment_method`.

Other than a payment being declined, for a Cash App Pay [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) with a status of `requires_action`, customers must complete the payment within 10 minutes after they’re redirected to Cash App. If no action is taken after 10 minutes, the [PaymentMethod](https://docs.stripe.com/api/payment_methods/object.md) is detached and the [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) object’s status automatically transitions to `requires_payment_method`.

When this happens, the Payment Element renders error messages and instructs your customer to retry using a different payment method.

## Error codes

The following table details common error codes and recommended actions:

| Error Code                                                | Recommended Action                                                                                                                                                                                                                                                           |
| --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_intent_invalid_currency`                         | Enter the appropriate currency. Cash App Pay only supports `usd`.                                                                                                                                                                                                            |
| `missing_required_parameter`                              | Check the error message for more information about the required parameter.                                                                                                                                                                                                   |
| `payment_intent_payment_attempt_failed`                   | This code can appear in the [last_payment_error.code](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-last_payment_error-code) field of a PaymentIntent. Check the error message for a detailed failure reason and suggestion on error handling. |
| `payment_intent_redirect_confirmation_without_return_url` | Provide a `return_url` when confirming a PaymentIntent with Cash App Pay.                                                                                                                                                                                                    |

# Android

> This is a Android for when payment-ui is mobile and platform is android. View the full page at https://docs.stripe.com/payments/cash-app-pay/accept-a-payment?payment-ui=mobile&platform=android.

We recommend you use the [Mobile Payment Element](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=mobile&platform=android), an embeddable payment form, to add Cash App Pay and other payment methods to your integration with the least amount of effort.

This guide covers how to accept Cash App Pay from your native mobile application using your own custom payment form.

If you’re accepting Cash App Pay from your native mobile application, your customers are redirected to the Cash App mobile application for authentication. The purchase is completed in the Cash App mobile application, and the customer is redirected back to your native mobile application.

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

- Specify the amount to collect and the currency.
- Add `cashapp` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your `PaymentIntent`. Make sure Cash App Pay is enabled in the [Dashboard](https://dashboard.stripe.com/settings/payment_methods).
- Set `payment_method_data[type]` to `cashapp` to create a *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) and immediately use it with this PaymentIntent.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 6000,
  currency: "usd",
  payment_method_types: ["cashapp"],
  payment_method_data: {
    type: "cashapp",
  },
  return_url: "payments-example://stripe-redirect",
});
```

The returned PaymentIntent includes a *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)), that you’ll use to *confirm* (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) the PaymentIntent. Send the client secret back to the client so you can use it in the next step.

### Client-side

On the client, request a PaymentIntent from your server and store its *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)).

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

When a customer taps to pay with Cash App Pay, confirm the `PaymentIntent` to complete the payment. Configure a `ConfirmPaymentIntentParams` object with the `PaymentIntent` [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret).

The client secret is different from your API keys that authenticate Stripe API requests. Handle it carefully, as it can complete the charge. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

### Confirm Cash App Pay payment

Complete the payment by calling [PaymentLauncher confirm](https://stripe.dev/stripe-android/payments-core/com.stripe.android.payments.paymentlauncher/-payment-launcher/confirm.html). This presents a webview where the customer can complete the payment with Cash App Pay. Upon completion, the provided `PaymentResultCallback` is called with the result of the payment.

#### Kotlin

```kotlin
class CheckoutActivity : AppCompatActivity() {

    // ...

    private val paymentLauncher: PaymentLauncher by lazy {
        val paymentConfiguration = PaymentConfiguration.getInstance(applicationContext)
        PaymentLauncher.create(
            activity = this,
            publishableKey = paymentConfiguration.publishableKey,
            stripeAccountId = paymentConfiguration.stripeAccountId,
            callback = ::onPaymentResult,
        )
    }

    // …

    private fun startCheckout() {
        // ...

        val cashAppPayParams = PaymentMethodCreateParams.createCashAppPay()

        val confirmParams = ConfirmPaymentIntentParams
            .createWithPaymentMethodCreateParams(
                paymentMethodCreateParams = cashAppPayParams,
                clientSecret = paymentIntentClientSecret,
                // Add a mandate ID or MandateDataParams if you
                // want to set this up for future use…
            )

        paymentLauncher.confirm(confirmParams)
    }

    private fun onPaymentResult(paymentResult: PaymentResult) {
        // Handle the payment result…
    }
}
```

## Optional: Separate authorization and capture

You can separate authorization and capture to create a charge now, but capture funds later. Stripe cancels the PaymentIntent and sends a [payment_intent.canceled](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.canceled) event if the payment isn’t captured during the 7-day window.

If you know that you can’t capture the payment, we recommend [canceling the PaymentIntent](https://docs.stripe.com/refunds.md#cancel-payment) instead of waiting for the 7-day window to elapse.

### 1. Tell Stripe to authorize only

To indicate that you want separate authorization and capture, set [capture_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-capture_method) to `manual` when creating the PaymentIntent. This parameter instructs Stripe to only authorize the amount on the customer’s Cash App Pay account.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 6000,
  confirm: true,
  currency: "usd",
  payment_method_types: ["cashapp"],
  payment_method_data: {
    type: "cashapp",
  },
  capture_method: "manual",
  return_url: "https://www.example.com/checkout/done",
});
```

### 2. Capture the funds

After the authorization succeeds, the PaymentIntent [status](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-status) transitions to `requires_capture`. To capture the authorized funds, make a PaymentIntent [capture](https://docs.stripe.com/api/payment_intents/capture.md) request.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.capture(
  "{PAYMENT_INTENT_ID}",
);
```

The total authorized amount is captured by default. You can also specify `amount_to_capture` which can be less or equal to the total.

### (Optional) Cancel the authorization

If you need to cancel an authorization, you can [cancel the PaymentIntent](https://docs.stripe.com/api/payment_intents/cancel.md).

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

Test your Cash App Pay integration with your test API keys by viewing the redirect page. You can test the successful payment case by authenticating the payment on the redirect page. The [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) transitions from `requires_action` to `succeeded`.

To test the case where the user fails to authenticate, use your test API keys and view the redirect page. On the redirect page, click **Fail test payment**. The [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) transitions from `requires_action` to `requires_payment_method`.

For test manual capture PaymentIntents, the uncaptured [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) auto-expires 7 days after successful authorization.

There are some differences between how *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes) and live mode payments work. For example, in live mode, tapping **Pay** redirects you to the Cash App mobile application. Within Cash App, you don’t have the option to approve or decline the payment within Cash App. The payment is automatically approved after the redirect.

## Failed payments

Cash App Pay uses multiple data points to decide when to decline a transaction (for example, their AI model detected high consumer fraud risk for the transaction, or the consumer has revoked your permission to charge them in Cash App).

In these cases, the [PaymentMethod](https://docs.stripe.com/api/payment_methods/object.md) is detached and the [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) object’s status automatically transitions to `requires_payment_method`.

Other than a payment being declined, for a Cash App Pay [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) with a status of `requires_action`, customers must complete the payment within 10 minutes after they’re redirected to Cash App. If no action is taken after 10 minutes, the [PaymentMethod](https://docs.stripe.com/api/payment_methods/object.md) is detached and the [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) object’s status automatically transitions to `requires_payment_method`.

When this happens, the Payment Element renders error messages and instructs your customer to retry using a different payment method.

## Error codes

The following table details common error codes and recommended actions:

| Error Code                                                | Recommended Action                                                                                                                                                                                                                                                           |
| --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_intent_invalid_currency`                         | Enter the appropriate currency. Cash App Pay only supports `usd`.                                                                                                                                                                                                            |
| `missing_required_parameter`                              | Check the error message for more information about the required parameter.                                                                                                                                                                                                   |
| `payment_intent_payment_attempt_failed`                   | This code can appear in the [last_payment_error.code](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-last_payment_error-code) field of a PaymentIntent. Check the error message for a detailed failure reason and suggestion on error handling. |
| `payment_intent_redirect_confirmation_without_return_url` | Provide a `return_url` when confirming a PaymentIntent with Cash App Pay.                                                                                                                                                                                                    |

# React Native

> This is a React Native for when payment-ui is mobile and platform is react-native. View the full page at https://docs.stripe.com/payments/cash-app-pay/accept-a-payment?payment-ui=mobile&platform=react-native.

Cash App Pay is a payment method available to all Cash App customers for single use and recurring payments to businesses. Cash App Pay uses the customer’s stored balance or linked debit card to fund the payment. The customer can confirm the payment in one of two ways:

- During checkout from a mobile device, your site redirects customers to the Cash App mobile application for authentication. The payment is authenticated during the redirect. No additional action is needed in the Cash App mobile application to complete the purchase. The customer is then redirected back to your site.
- During checkout from a desktop web application, the customer scans a QR code with their mobile device to authenticate the transaction.

Customers can also authorize the use of Cash App Pay for future, on-file payments.

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

- Specify the amount to collect and the currency.
- Add `cashapp` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your `PaymentIntent`. Make sure Cash App Pay is enabled in the [Dashboard](https://dashboard.stripe.com/settings/payment_methods).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 6000,
  currency: "usd",
  payment_method_types: ["cashapp"],
  return_url: "payments-example://stripe-redirect",
});
```

The returned PaymentIntent includes a *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)), that you’ll use to *confirm* (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) the PaymentIntent. Send the client secret back to the client so you can use it in the next step.

### Client-side

On the client, request a PaymentIntent from your server and store its *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)):

```javascript
function PaymentScreen() {
  const fetchPaymentIntentClientSecret = async () => {
    const response = await fetch(`${API_URL}/create-payment-intent`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        currency: "usd",
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

## Confirm Cash App Pay payment [Client-side]

When a customer taps to pay with CashApp, complete the payment by calling [confirmPayment](https://stripe.dev/stripe-react-native/api-reference/index.html#confirmPayment). This presents a webview where the customer can complete the payment with CashApp. Upon completion, the promise resolves with an object containing either a `paymentIntent` field, or an `error` field if an error occurred with the payment.

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
      paymentMethodType: "CashApp",
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

## Optional: Separate authorization and capture

You can separate authorization and capture to create a charge now, but capture funds later. Stripe cancels the PaymentIntent and sends a [payment_intent.canceled](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.canceled) event if the payment isn’t captured during the 7-day window.

If you know that you can’t capture the payment, we recommend [canceling the PaymentIntent](https://docs.stripe.com/refunds.md#cancel-payment) instead of waiting for the 7-day window to elapse.

### 1. Tell Stripe to authorize only

To indicate that you want separate authorization and capture, set [capture_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-capture_method) to `manual` when creating the PaymentIntent. This parameter instructs Stripe to only authorize the amount on the customer’s Cash App Pay account.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 6000,
  confirm: true,
  currency: "usd",
  payment_method_types: ["cashapp"],
  payment_method_data: {
    type: "cashapp",
  },
  capture_method: "manual",
  return_url: "https://www.example.com/checkout/done",
});
```

### 2. Capture the funds

After the authorization succeeds, the PaymentIntent [status](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-status) transitions to `requires_capture`. To capture the authorized funds, make a PaymentIntent [capture](https://docs.stripe.com/api/payment_intents/capture.md) request.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.capture(
  "{PAYMENT_INTENT_ID}",
);
```

The total authorized amount is captured by default. You can also specify `amount_to_capture` which can be less or equal to the total.

### (Optional) Cancel the authorization

If you need to cancel an authorization, you can [cancel the PaymentIntent](https://docs.stripe.com/api/payment_intents/cancel.md).

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

Test your Cash App Pay integration with your test API keys by viewing the redirect page. You can test the successful payment case by authenticating the payment on the redirect page. The [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) transitions from `requires_action` to `succeeded`.

To test the case where the user fails to authenticate, use your test API keys and view the redirect page. On the redirect page, click **Fail test payment**. The [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) transitions from `requires_action` to `requires_payment_method`.

For test [manual capture](https://docs.stripe.com/payments/cash-app-pay/accept-a-payment.md#manual-capture) PaymentIntents, the uncaptured PaymentIntent auto-expires 60 minutes after successful authorization.

In live mode, confirming the [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) redirects you to Cash App. As a best practice, test it in live mode with a real Cash App account before releasing it to your customers. In live mode, you don’t have the option to approve or decline the payment within Cash App. The payment is automatically approved after your customers are redirected to Cash App.

## Failed payments

Cash App Pay uses multiple data points to decide when to decline a transaction (for example, their AI model detected high consumer fraud risk for the transaction, or the consumer has revoked your permission to charge them in Cash App).

In these cases, the [PaymentMethod](https://docs.stripe.com/api/payment_methods/object.md) is detached and the [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) object’s status automatically transitions to `requires_payment_method`.

Other than a payment being declined, for a Cash App Pay [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) with a status of `requires_action`, customers must complete the payment within 10 minutes after they’re redirected to Cash App. If no action is taken after 10 minutes, the [PaymentMethod](https://docs.stripe.com/api/payment_methods/object.md) is detached and the [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) object’s status automatically transitions to `requires_payment_method`.

When this happens, the Payment Element renders error messages and instructs your customer to retry using a different payment method.

## Error codes

The following table details common error codes and recommended actions:

| Error Code                                                | Recommended Action                                                                                                                                                                                                                                                           |
| --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_intent_invalid_currency`                         | Enter the appropriate currency. Cash App Pay only supports `usd`.                                                                                                                                                                                                            |
| `missing_required_parameter`                              | Check the error message for more information about the required parameter.                                                                                                                                                                                                   |
| `payment_intent_payment_attempt_failed`                   | This code can appear in the [last_payment_error.code](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-last_payment_error-code) field of a PaymentIntent. Check the error message for a detailed failure reason and suggestion on error handling. |
| `payment_intent_redirect_confirmation_without_return_url` | Provide a `return_url` when confirming a PaymentIntent with Cash App Pay.                                                                                                                                                                                                    |
