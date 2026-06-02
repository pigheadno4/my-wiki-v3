<!-- Source URL: https://docs.stripe.com/payments/bancontact/accept-a-payment -->
<!-- Fetched: 2026-05-03 -->

# Accept a Bancontact payment

Learn how to accept Bancontact, a common payment method in Belgium.

# Checkout

> This is a Checkout for when payment-ui is checkout. View the full page at https://docs.stripe.com/payments/bancontact/accept-a-payment?payment-ui=checkout.

> Stripe can automatically present the relevant payment methods to your customers by evaluating currency, payment method restrictions, and other parameters.
>
> - Follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=checkout&ui=stripe-hosted) guide to build a Checkout integration that uses [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md).

- If you don’t want to use dynamic payment methods, follow the steps below to manually configure the payment methods in your Checkout integration.

Bancontact is a [single use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method where customers are required to [authenticate](https://docs.stripe.com/payments/payment-methods.md#customer-actions) their payment. *Customers* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) pay with Bancontact by redirecting from your website, authorizing the payment, then returning to your website where you get [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) on whether the payment succeeded or failed.

> Your use of Bancontact must be in accordance with our [Bancontact Terms of Service](https://stripe.com/bancontact/legal).

## Determine compatibility

**Supported business locations**: Europe, US, CA, NZ, SG, HK, JP, AU, MX

**Supported currencies**: `eur`

**Presentment currencies**: `eur`

**Payment mode**: Yes

**Setup mode**: Yes

**Subscription mode**: Yes

A Checkout Session must satisfy all of the following conditions to support Bancontact payments:

- *Prices* (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) for all line items must be expressed in Euro (currency code `eur`).

## Accept a payment

> Build an integration to [accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?integration=checkout) with Checkout before using this guide.

This guides you through enabling Bancontact and shows the differences between accepting payments using dynamic payment methods and manually configuring payment methods.

### Enable Bancontact as a payment method

When creating a new [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md), you need to:

1. Add `bancontact` to the list of `payment_method_types`.
1. Make sure all your `line_items` use the `eur` currency.

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
  payment_method_types: ["card", "bancontact"],
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
  payment_method_types: ["card", "bancontact"],
  return_url: "https://example.com/return",
  ui_mode: "embedded_page",
});
```

### Fulfill your orders

After accepting a payment, learn how to [fulfill orders](https://docs.stripe.com/checkout/fulfillment.md).

## Test your integration

There are no special test numbers required for Bancontact.

When testing your Checkout integration, select Bancontact as the payment method and click the **Pay** button.

## Handle refunds and disputes

The refund period for Bancontact is up to 180 days after the original payment.

There is no dispute process—customers authenticate with their bank.

## See also

- [More about Bancontact](https://docs.stripe.com/payments/bancontact.md)
- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment.md)
- [Customizing Checkout](https://docs.stripe.com/payments/checkout/customization.md)

# Direct API

> This is a Direct API for when payment-ui is direct-api. View the full page at https://docs.stripe.com/payments/bancontact/accept-a-payment?payment-ui=direct-api.

Bancontact is a [single use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method where customers are required to [authenticate](https://docs.stripe.com/payments/payment-methods.md#customer-actions) their payment. *Customers* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) pay with Bancontact by redirecting from your app, authenticating the payment, then returning to your app where you get [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) on whether the payment succeeded or failed.

> Your use of Bancontact must be in accordance with the [Bancontact Terms of Service](https://stripe.com/bancontact/legal).

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

Create a `PaymentIntent` on your server and specify the amount to collect and the `eur` currency (Bancontact doesn’t support other currencies). If you have an existing [Payment Intents](https://docs.stripe.com/payments/payment-intents.md) integration, add `bancontact` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  payment_method_types: ["bancontact"],
});
```

The default language of the Bancontact authorization page is English (`en`). You can match the preferred language of your customer by setting `preferred_language` to `fr`, `nl`, or `de`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  payment_method_types: ["bancontact"],
  payment_method_options: {
    bancontact: {
      preferred_language: "fr",
    },
  },
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

#### HTML + JS

Create a payment form on your client to collect the required billing details from the customer:

| Field  | Value                                           |
| ------ | ----------------------------------------------- |
| `name` | The full name (first and last) of the customer. |

```html
<form id="payment-form">
  <div class="form-row">
    <label for="name"> Name </label>
    <input id="name" name="name" required />
  </div>

  <!-- Used to display form errors. -->
  <div id="error-message" role="alert"></div>

  <button id="submit-button">Pay with Bancontact</button>
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

## Submit the payment to Stripe [Client-side]

Create a payment on the client side with the [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) of the `PaymentIntent`. The client secret is different from your API keys that authenticate Stripe API requests. It should be handled carefully because it can complete the charge. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

#### HTML + JS

When a customer clicks to pay with Bancontact, use Stripe.js to submit the payment to Stripe. [Stripe.js](https://docs.stripe.com/payments/elements.md) is the foundational JavaScript library for building payment flows. It automatically handles complexities like the redirect described below, and enables you to extend your integration to other payment methods. Include the Stripe.js script on your checkout page by adding it to the `head` of your HTML file.

```html
<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/dahlia/stripe.js"></script>
</head>
```

Create an instance of Stripe.js with the following JavaScript on your checkout page.

```javascript
// Set your publishable key. Remember to change this to your live publishable key in production!
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");
```

Call [stripe.confirmBancontactPayment](https://docs.stripe.com/js/payment_intents/confirm_bancontact_payment) to redirect your customer to Bancontact’s website or app to complete the payment. Include a `return_url` to redirect your customer after they complete the payment. You must also provide the customer’s full name in `billing_details`.

```javascript
var stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");

// Redirects away from the client
const { error } = await stripe.confirmBancontactPayment(
  "{{PAYMENT_INTENT_CLIENT_SECRET}}",
  {
    payment_method: {
      billing_details: {
        name: "Jenny Rosen",
      },
    },
    return_url: "https://example.com/checkout/complete",
  },
);

if (error) {
  // Inform the customer that there was an error.
}
```

#### React

Use [stripe.confirmBancontactPayment](https://docs.stripe.com/js/payment_intents/confirm_bancontact_payment) to handle the redirect away from your page and to complete the payment. Add a [return_url](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-return_url) to this function to indicate where Stripe should redirect the user after they complete the payment on their bank’s website or mobile application.

To call `stripe.confirmBancontactPayment` from your payment form component, use the [useStripe](https://docs.stripe.com/sdks/stripejs-react.md#usestripe-hook) and [useElements](https://docs.stripe.com/sdks/stripejs-react.md#useelements-hook) hooks.

If you prefer traditional class components over hooks, you can instead use an [ElementsConsumer](https://docs.stripe.com/sdks/stripejs-react.md#elements-consumer).

#### Hooks

```jsx
import React from "react";
import { useStripe, useElements } from "@stripe/react-stripe-js";

export default function CheckoutForm() {
  const stripe = useStripe();
  const elements = useElements();

  const handleSubmit = async (event) => {
    // We don't want to let default form submission happen here,
    // which would refresh the page.
    event.preventDefault();

    if (!stripe || !elements) {
      // Stripe.js hasn't yet loaded.
      // Make sure to disable form submission until Stripe.js has loaded.
      return;
    }

    // For brevity, this example is using uncontrolled components for
    // the accountholder's name. In a real world app you will
    // probably want to use controlled components.
    // https://reactjs.org/docs/uncontrolled-components.html
    // https://reactjs.org/docs/forms.html#controlled-components

    const accountholderName = event.target["accountholder-name"];

    const { error } = await stripe.confirmBancontactPayment("{CLIENT_SECRET}", {
      payment_method: {
        billing_details: {
          name: accountholderName.value,
        },
      },
      return_url: "https://example.com/checkout/complete",
    });

    if (error) {
      // Show error to your customer.
      console.log(error.message);
    }

    // Otherwise the customer will be redirected away from your
    // page to complete the payment with their bank.
  };

  return (
    <form onSubmit={handleSubmit}>
      <div className="form-row">
        <label>
          Name
          <input name="accountholder-name" placeholder="Jenny Rosen" required />
        </label>
      </div>
      <button type="submit" disabled={!stripe}>
        Submit Payment
      </button>
    </form>
  );
}
```

#### Class Components

```jsx
import React from "react";
import { ElementsConsumer } from "@stripe/react-stripe-js";

class CheckoutForm extends React.Component {
  handleSubmit = async (event) => {
    // We don't want to let default form submission happen here,
    // which would refresh the page.
    event.preventDefault();

    const { stripe, elements } = this.props;

    if (!stripe || !elements) {
      // Stripe.js hasn't yet loaded.
      // Make  sure to disable form submission until Stripe.js has loaded.
      return;
    }

    // For brevity, this example is using uncontrolled components for
    // the accountholder's name. In a real world app you will
    // probably want to use controlled components.
    // https://reactjs.org/docs/uncontrolled-components.html
    // https://reactjs.org/docs/forms.html#controlled-components

    const accountholderName = event.target["accountholder-name"];

    const { error } = await stripe.confirmBancontactPayment("{CLIENT_SECRET}", {
      payment_method: {
        billing_details: {
          name: accountholderName.value,
        },
      },
      return_url: "https://example.com/checkout/complete",
    });

    if (error) {
      // Show error to your customer.
      console.log(error.message);
    }

    // Otherwise the customer will be redirected away from your
    // page to complete the payment with their bank.
  };

  render() {
    const { stripe } = this.props;

    return (
      <form onSubmit={this.handleSubmit}>
        <div className="form-row">
          <label>
            Name
            <input
              name="accountholder-name"
              placeholder="Jenny Rosen"
              required
            />
          </label>
        </div>
        <button type="submit" disabled={!stripe}>
          Submit Payment
        </button>
      </form>
    );
  }
}

export default function InjectedCheckoutForm() {
  return (
    <ElementsConsumer>
      {({ stripe, elements }) => (
        <CheckoutForm stripe={stripe} elements={elements} />
      )}
    </ElementsConsumer>
  );
}
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

### Bank account details

You can find details about the bank account the customer used to complete the payment on the resulting charge under [payment_method_details](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-bancontact).

#### Json

```json
{
  "charges": {
    "data": [
      {
        "payment_method_details": {
          "bancontact": {
            "bank_code": "VAPE",
            "bank_name": "VAN DE PUT & CO",
            "bics": "VAPEBE22",
            "iban_last4": "7061",
            "preferred_language": "en",
            "verified_name": "Jenny Rosen"
          },
          "type": "bancontact"
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
        "type": "bancontact",
        "usage": "single_use"
      }
    ],
    "object": "list",
    "has_more": false,
    "url": "/v1/charges?payment_intent=pi_1G1sgdKi6xqXeNtkldRRE6HT"
  },
  "payment_method_options": {
    "bancontact": {
      "preferred_language": "en"
    }
  },
  "payment_method_types": ["bancontact"],
  "id": "pi_1G1sgdKi6xqXeNtkldRRE6HT",
  "object": "payment_intent",
  "amount": 1099,
  "client_secret": "pi_1G1sgdKi6xqXeNtkldRRE6HT_secret_h9B56ObhTN72fQiBAuzcVPb2E",
  "confirmation_method": "automatic",
  "created": 1579259303,
  "currency": "eur",
  "livemode": true,
  "next_action": null
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

## Optional: Handle the Bancontact redirect manually

We recommend relying on Stripe.js to handle Bancontact redirects and payments client-side with `confirmBancontactPayment`. Using Stripe.js helps extend your integration to other payment methods. However, you can also manually redirect your customers on your server by following these steps:

1. Create and *confirm* (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) a PaymentIntent of type `bancontact`. You must provide the `payment_method_data.billing_details.name` property, which you should collect from your customer. Note that, by specifying `payment_method_data`, a PaymentMethod is created and immediately used with this PaymentIntent.

   You must also provide the URL where your customer is redirected to after they complete their payment in the `return_url` field. You can optionally provide your own query parameters in this URL. These parameters will be included in the final URL upon completing the redirect flow.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const intent = await stripe.paymentIntents.create({
  confirm: true,
  amount: 1099,
  currency: "eur",
  payment_method_types: ["bancontact"],
  payment_method_data: {
    type: "bancontact",
    billing_details: {
      name: "Jenny Rosen",
    },
  },
  return_url: "https://example.com/checkout/complete",
});
```

1. Check that the `PaymentIntent` has a status of `requires_action` and the type for `next_action` is `redirect_to_url`.

#### Json

```json
{"status": "requires_action",
  "next_action": {
    "type": "redirect_to_url",
    "redirect_to_url": {
      "url": "https://hooks.stripe.com/...",
      "return_url": "https://example.com/checkout/complete"
    }
  },
  "id": "pi_1G1sgdKi6xqXeNtkldRRE6HT",
  "object": "payment_intent",
  ...
}
```

1. Redirect the customer to the URL provided in the `next_action.redirect_to_url.url` property. This code example is approximate—the redirect method might be different in your web framework.

#### Node.js

```javascript
if (
  paymentIntent.status === "requires_action" &&
  paymentIntent.next_action.type === "redirect_to_url"
) {
  const url = paymentIntent.next_action.redirect_to_url.url;
  res.redirect(url);
}
```

Your customer is redirected to the `return_url` when they complete the payment process. The `payment_intent` and `payment_intent_client_secret` URL query parameters are included along with any of your own query parameters. Stripe recommends setting up a [webhook endpoint](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks) to programmatically confirm the status of a payment.

# iOS

> This is a iOS for when payment-ui is mobile and platform is ios. View the full page at https://docs.stripe.com/payments/bancontact/accept-a-payment?payment-ui=mobile&platform=ios.

> We recommend that you follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md) guide unless you need to use manual server-side confirmation, or your integration requires presenting payment methods separately. If you’ve already integrated with Elements, see the [Payment Element migration guide](https://docs.stripe.com/payments/payment-element/migration.md).

Bancontact is a [single use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method where customers are required to [authenticate](https://docs.stripe.com/payments/payment-methods.md#customer-actions) their payment. *Customers* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) pay with Bancontact by redirecting from your app, authenticating the payment, then returning to your app where you get [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) on whether the payment succeeded or failed.

> Your use of Bancontact must be in accordance with the [Bancontact Terms of Service](https://stripe.com/bancontact/legal).

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

A [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) is an object that represents your intent to collect payment from a customer and tracks the lifecycle of the payment process through each stage.

### Server-side

Create a `PaymentIntent` on your server and specify the amount to collect and the `eur` currency (Bancontact doesn’t support other currencies). If you have an existing [Payment Intents](https://docs.stripe.com/payments/payment-intents.md) integration, add `bancontact` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  payment_method_types: ["bancontact"],
});
```

The default language of the Bancontact authorization page is English (`en`). You can match the preferred language of your customer by setting `preferred_language` to `fr`, `nl`, or `de`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  payment_method_types: ["bancontact"],
  payment_method_options: {
    bancontact: {
      preferred_language: "fr",
    },
  },
});
```

### Client-side

On the client, request a PaymentIntent from your server and store its client secret.

#### Swift

```swift
class CheckoutViewController: UIViewController {
    var paymentIntentClientSecret: String?

    func startCheckout() {
        // Request a PaymentIntent from your server and store its client secret
    }
}
```

## Collect payment method details [Client-side]

In your app, collect the required billing details (first and last name) from the customer. Create a [STPPaymentIntentParams](https://stripe.dev/stripe-ios/stripe-payments/Classes/STPPaymentIntentParams.html) with the billing details.

#### Swift

```swift
let bancontactParams = STPPaymentMethodBancontactParams()

let billingDetails = STPPaymentMethodBillingDetails()
billingDetails.name = "Jane Doe"
```

## Submit the payment to Stripe [Client-side]

Retrieve the client secret from the PaymentIntent you created in step 2 and call [STPPaymentHandler confirmPayment](<https://stripe.dev/stripe-ios/stripe-payments/Classes/STPPaymentHandler.html#/c:@M@StripePayments@objc(cs)STPPaymentHandler(im)confirmPayment:withAuthenticationContext:completion:>). This presents a webview where the customer can complete the payment. Upon completion, the completion block is called with the result of the payment.

#### Swift

```swift
let paymentIntentParams = STPPaymentIntentParams(clientSecret: paymentIntentClientSecret)
paymentIntentParams.paymentMethodParams = STPPaymentMethodParams(
    bancontact: bancontactParams,
    billingDetails: billingDetails,
    metadata: nil
)

STPPaymentHandler.shared().confirmPayment(paymentIntentParams, with: self) { (handlerStatus, paymentIntent, error) in
    switch handlerStatus {
    case .succeeded:
        // Payment succeeded

    case .canceled:
        // Payment was canceled

    case .failed:
        // Payment failed

    @unknown default:
        fatalError()
    }
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

# Android

> This is a Android for when payment-ui is mobile and platform is android. View the full page at https://docs.stripe.com/payments/bancontact/accept-a-payment?payment-ui=mobile&platform=android.

> We recommend that you follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md) guide unless you need to use manual server-side confirmation, or your integration requires presenting payment methods separately. If you’ve already integrated with Elements, see the [Payment Element migration guide](https://docs.stripe.com/payments/payment-element/migration.md).

Bancontact is a [single use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method where customers are required to [authenticate](https://docs.stripe.com/payments/payment-methods.md#customer-actions) their payment. *Customers* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) pay with Bancontact by redirecting from your app, authenticating the payment, then returning to your app where you get [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) on whether the payment succeeded or failed.

> Your use of Bancontact must be in accordance with the [Bancontact Terms of Service](https://stripe.com/bancontact/legal).

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

## Create a PaymentIntent [Server-side] [Client-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) is an object that represents your intent to collect payment from a customer and tracks the lifecycle of the payment process through each stage.

### Server-side

Create a `PaymentIntent` on your server and specify the amount to collect and the `eur` currency (Bancontact doesn’t support other currencies). If you have an existing [Payment Intents](https://docs.stripe.com/payments/payment-intents.md) integration, add `bancontact` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  payment_method_types: ["bancontact"],
});
```

The default language of the Bancontact authorization page is English (`en`). You can match the preferred language of your customer by setting `preferred_language` to `fr`, `nl`, or `de`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  payment_method_types: ["bancontact"],
  payment_method_options: {
    bancontact: {
      preferred_language: "fr",
    },
  },
});
```

### Client-side

On the client, request a PaymentIntent from your server and store its client secret.

#### Kotlin

```kotlin
class BancontactPaymentActivity: AppCompatActivity() {
    private lateinit var paymentIntentClientSecret: String

    override fun onCreate(savedInstanceState: Bundle?) {
        // ...
        startCheckout()
    }


    private fun startCheckout() {
        // Request a PaymentIntent from your server and store its client secret
    }
}
```

## Collect payment method details [Client-side]

In your app, collect the required billing details (first and last name) from the customer. Create a `PaymentMethodCreateParams` with the billing details.

#### Kotlin

```kotlin
val billingDetails = PaymentMethod.BillingDetails(name = "Jenny Rosen")
val paymentMethodCreateParams = PaymentMethodCreateParams.createBancontact(billingDetails)
```

## Submit the payment to Stripe [Client-side]

Retrieve the client secret from the PaymentIntent you created in step 2 and call [PaymentLauncher confirm](https://stripe.dev/stripe-android/payments-core/com.stripe.android.payments.paymentlauncher/-payment-launcher/index.html#74063765%2FFunctions%2F-1622557690). This presents a webview where the customer can complete the payment. Upon completion, `onPaymentResult` is called with the result of the payment.

#### Kotlin

```kotlin
class BancontactPaymentActivity : AppCompatActivity() {
    // ...
    private lateinit var paymentIntentClientSecret: String
    private val paymentLauncher: PaymentLauncher by lazy {
        PaymentLauncher.Companion.create(
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
                  paymentMethodCreateParams = paymentMethodCreateParams,
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
                // See here: https://stripe.com/docs/api/payment_intents/object#payment_intent_object-last_payment_error-message
                "Failed: " + paymentResult.throwable.message
            }
        }
    }
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

# React Native

> This is a React Native for when payment-ui is mobile and platform is react-native. View the full page at https://docs.stripe.com/payments/bancontact/accept-a-payment?payment-ui=mobile&platform=react-native.

> We recommend that you follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md) guide unless you need to use manual server-side confirmation, or your integration requires presenting payment methods separately. If you’ve already integrated with Elements, see the [Payment Element migration guide](https://docs.stripe.com/payments/payment-element/migration.md).

Bancontact is a [single use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method where customers are required to [authenticate](https://docs.stripe.com/payments/payment-methods.md#customer-actions) their payment. *Customers* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) pay with Bancontact by redirecting from your app, authenticating the payment, then returning to your app where you get [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) on whether the payment succeeded or failed.

> Your use of Bancontact must be in accordance with the [Bancontact Terms of Service](https://stripe.com/bancontact/legal).

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

## Create a PaymentIntent [Server-side] [Client-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) is an object that represents your intent to collect payment from a customer and tracks the lifecycle of the payment process through each stage.

### Server-side

Create a `PaymentIntent` on your server and specify the amount to collect and the `eur` currency (Bancontact doesn’t support other currencies). If you have an existing [Payment Intents](https://docs.stripe.com/payments/payment-intents.md) integration, add `bancontact` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  payment_method_types: ["bancontact"],
});
```

The default language of the Bancontact authorization page is English (`en`). You can match the preferred language of your customer by setting `preferred_language` to `fr`, `nl`, or `de`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  payment_method_types: ["bancontact"],
  payment_method_options: {
    bancontact: {
      preferred_language: "fr",
    },
  },
});
```

### Client-side

On the client, request a PaymentIntent from your server and store its client secret.

```javascript
const fetchPaymentIntentClientSecret = async () => {
  const response = await fetch(`${API_URL}/create-payment-intent`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      email,
      currency: "eur",
      payment_method_types: ["bancontact"],
    }),
  });
  const { clientSecret, error } = await response.json();

  return { clientSecret, error };
};
```

## Collect payment method details [Client-side]

In your app, collect your customer’s full name and email address.

```javascript
export default function BancontactPaymentScreen() {
  const [name, setName] = useState();
  const [email, setEmail] = useState();

  const handlePayPress = async () => {
    // ...
  };

  return (
    <Screen>
      <TextInput
        placeholder="Name"
        onChange={(value) => setName(value.nativeEvent.text)}
      />
      <TextInput
        placeholder="E-mail"
        onChange={(value) => setEmail(value.nativeEvent.text)}
      />
    </Screen>
  );
}
```

## Submit the payment to Stripe [Client-side]

Retrieve the client secret from the PaymentIntent you created and call `confirmPayment`. This presents a webview where the customer can complete the payment on the Bancontact website or app. Afterwards, the promise resolves with the result of the payment.

```javascript
export default function BancontactPaymentScreen() {
  const [name, setName] = useState();
  const [email, setEmail] = useState();

  const handlePayPress = async () => {
    const billingDetails: PaymentMethodCreateParams.BillingDetails = {
      name,
      email,
    };
  };

  const { error, paymentIntent } = await confirmPayment(clientSecret, {
    paymentMethodType: 'Bancontact',
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

  return (
    <Screen>
      <TextInput
        placeholder="Name"
        onChange={(value) => setName(value.nativeEvent.text)}
      />
      <TextInput
        placeholder="E-mail"
        onChange={(value) => setEmail(value.nativeEvent.text)}
      />
    </Screen>
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
