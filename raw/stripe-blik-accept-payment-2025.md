<!-- Source URL: https://docs.stripe.com/payments/blik/accept-a-payment -->
<!-- Fetched: 2026-05-03 -->

# BLIK payments

Learn how to accept BLIK, a common payment method in Poland.

# Checkout

> This is a Checkout for when payment-ui is checkout. View the full page at https://docs.stripe.com/payments/blik/accept-a-payment?payment-ui=checkout.

> Stripe can automatically present the relevant payment methods to your customers by evaluating currency, payment method restrictions, and other parameters.
>
> - Follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=checkout&ui=stripe-hosted) guide to build a Checkout integration that uses [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md).

- If you don’t want to use dynamic payment methods, follow the steps below to manually configure the payment methods in your Checkout integration.

BLIK is a [single use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method that requires customers to [authenticate](https://docs.stripe.com/payments/payment-methods.md#customer-actions) their payments. When customers want to pay online using BLIK, they request a six-digit code from their banking application and enter it into the payment collection form.

The bank sends a push notification to your customer’s mobile phone asking to authorize the payment inside their banking application. The BLIK code is valid for 2 minutes; customers have 60 seconds to authorize the payment after starting a payment. After 60 seconds, it times out and they must request a new BLIK code. Customers typically approve BLIK payments in less than 10 seconds.

## Determine compatibility

**Supported business locations**: AT, AU, BE, BG, CA, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GR, HR, HU, IE, IS, IT, LI, LT, LU, LV, MT, NL, NO, PL, PT, RO, SE, SG, SI, SK, US

**Supported currencies**: `pln`

**Presentment currencies**: `pln`

**Payment mode**: Yes

**Setup mode**: Not yet

**Subscription mode**: Not yet

A Checkout Session must satisfy all of the following conditions to support BLIK payments:

- *Prices* (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) for all line items must be expressed in Złoty (currency code `pln`).

## Accept a payment

> This guide builds on the foundational [accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?ui=stripe-hosted) Checkout integration.

This guides you through enabling BLIK and shows the differences between accepting payments using dynamic payment methods and manually configuring payment methods.

### Enable BLIK as a payment method

When creating a new [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md), you need to:

1. Add `blik` to the list of `payment_method_types`.
1. Make sure all your `line_items` use the `pln` currency.

#### Stripe-hosted page

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        currency: "pln",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "blik"],
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
        currency: "pln",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "blik"],
  return_url: "https://example.com/return",
  ui_mode: "embedded_page",
});
```

#### Elements

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        currency: "pln",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "blik"],
  return_url: "https://example.com/return",
  ui_mode: "elements",
});
```

### What customers see

Inside their Banking app, customers see four lines related to each BLIK transaction:

- If you provided a value for [payment_intent_data.description](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_intent_data-description), the first two lines display it (max 70 characters).
- If you provided a value for [payment_intent_data.statement_descriptor](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_intent_data-statement_descriptor) (typically, an order ID), line 3 displays it (max 22 characters).
- The fourth line automatically populates with the URL of your website.

### Fulfill your orders

After accepting a payment, learn how to [fulfill orders](https://docs.stripe.com/checkout/fulfillment.md).

## Test your integration

When testing your Checkout integration, select BLIK as the payment method and click the **Pay** button.

Use a *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes) to test a successful payment by entering any 6-digit code (such as `123456`) in the payment form.

## Handle refunds and disputes

The refund period for BLIK is up to 13 months after the original payment.

Customers can dispute a payment through their bank up to 13 months after the original payment. There’s no appeal process.

Learn more about [BLIK disputes](https://docs.stripe.com/payments/blik.md#disputed-payments).

## Optional: Simulate failures in a sandbox

BLIK payments can fail for different reasons. There are immediate failures (for example, the code is expired or invalid), delayed errors (the bank declines) or timeouts (the customer didn’t respond in time). You can simulate each failure scenarios by passing `email` values matching certain patterns (documented below) when creating the `PaymentIntent`, as part of the [billing details](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_data-billing_details), with any 6-digit as BLIK code.

You can enter the `email` in the contact information section of the Checkout page.

### Immediate Failures

| Failure code                       | Explanation                                                                                                    | Email pattern       |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------- | ------------------- |
| `payment_method_invalid_parameter` | The code passed wasn’t a valid BLIK code.                                                                      | `.*invalid_code@.*` |
| `payment_method_invalid_parameter` | The code passed has expired. BLIK codes expire after 2 minutes, please request another code from the customer. | `.*expired_code@.*` |

### Declines (8 second delay)

| Failure code                      | Explanation                                                                                    | Email pattern             |
| --------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------- |
| `payment_method_provider_decline` | The payment has been declined because the payment limit on this bank account has been reached. | `.*limit_exceeded@.*`     |
| `payment_method_provider_decline` | The bank account has insufficient funds to complete the purchase.                              | `.*insufficient_funds@.*` |
| `payment_method_provider_decline` | The customer declined this payment.                                                            | `.*customer_declined@.*`  |
| `payment_method_provider_decline` | The payment has been declined by the customer’s bank for an unknown reason.                    | `.*bank_declined@.*`      |
| `payment_method_provider_decline` | The payment has been declined for an unknown reason.                                           | `.*blik_declined@.*`      |

### Timeouts (60 second delay)

| Failure code                      | Explanation                                                               | Email pattern           |
| --------------------------------- | ------------------------------------------------------------------------- | ----------------------- |
| `payment_method_provider_timeout` | The customer didn’t approve this payment within the allocated 60 seconds. | `.*customer_timeout@.*` |
| `payment_method_provider_timeout` | The request to the customer’s bank timed out.                             | `.*bank_timeout@.*`     |
| `payment_method_provider_timeout` | The request to the BLIK network timed out.                                | `.*blik_timeout@.*`     |

## See also

- [More about BLIK](https://docs.stripe.com/payments/blik.md)
- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment.md)
- [Customizing Checkout](https://docs.stripe.com/payments/checkout/customization.md)

# Direct API

> This is a Direct API for when payment-ui is direct-api. View the full page at https://docs.stripe.com/payments/blik/accept-a-payment?payment-ui=direct-api.

> We recommend that you follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md) guide unless you need to use manual server-side confirmation, or your integration requires presenting payment methods separately. If you’ve already integrated with Elements, see the [Payment Element migration guide](https://docs.stripe.com/payments/payment-element/migration.md).

BLIK is a [single use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method that requires customers to [authenticate](https://docs.stripe.com/payments/payment-methods.md#customer-actions) their payments. When customers want to pay online using BLIK, they request a six-digit code from their banking application and enter it into the payment collection form.

The bank sends a push notification to your customer’s mobile phone asking to authorize the payment inside their banking application. The BLIK code is valid for 2 minutes; customers have 60 seconds to authorize the payment after starting a payment. After 60 seconds, it times out and they must request a new BLIK code. Customers typically approve BLIK payments in less than 10 seconds.

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create a PaymentIntent [Server-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) is an object that represents your intent to collect a payment from a customer and tracks the lifecycle of the payment process through each stage. First, create a `PaymentIntent` on your server and specify the amount to collect and the `pln` currency, because BLIK only supports `pln`. If you already have an integration using the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md), add `blik` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your `PaymentIntent`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "pln",
  payment_method_types: ["blik"],
  description: "A description of what you're selling",
  statement_descriptor: "ORDER_123",
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

To submit the payment to Stripe, you need to confirm the PaymentIntent with your customer’s 6-digit BLIK code. You can get this code by creating a form on your client to collect the required code from the customer.

#### HTML + JS

```html
<form id="payment-form">
  <div class="form-row">
    <label for="code"> Code </label>
    <input id="code" name="code" required />
  </div>

  <button id="submit-button">Submit</button>

  <!-- Used to display form errors. -->
  <div id="error-message" role="alert"></div>
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

To integrate Stripe.js and (optionally) use Elements components for other payment methods, wrap the root of your React app in an [Elements provider](https://docs.stripe.com/sdks/stripejs-react.md#elements-provider). Call `loadStripe` with your publishable key and pass the returned `Promise` to the `Elements` provider.

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

### Create a form to accept payments

If you intend to use the [useStripe](https://docs.stripe.com/sdks/stripejs-react.md#usestripe-hook) hook to access Stripe.js features, you can create a normal React component.

If you prefer traditional class components over hooks, you can instead use an [ElementsConsumer](https://docs.stripe.com/sdks/stripejs-react.md#elements-consumer).

#### Hooks

```jsx
import React from "react";
import { useStripe } from "@stripe/react-stripe-js";

export default function CheckoutForm() {
  return (
    <form>
      <div className="form-row">
        <label>
          Code
          <input name="code" placeholder="000000" required />
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
  render() {
    const { stripe } = this.props;

    return (
      <form>
        <div className="form-row">
          <label>
            Code
            <input name="code" placeholder="000000" required />
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
      {({ stripe, elements }) => <CheckoutForm stripe={stripe} />}
    </ElementsConsumer>
  );
}
```

## Submit the payment to Stripe [Client-side]

Use the PaymentIntent object from [step 2](https://docs.stripe.com/payments/blik/accept-a-payment.md#web-create-payment-intent) and the 6-digit BLIK code you collected in [step 3](https://docs.stripe.com/payments/blik/accept-a-payment.md#web-collect-payment-method-details) to *confirm* (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) the PaymentIntent; this declares that the customer intends to pay with the specified *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs). After the PaymentIntent is confirmed, it initiates a payment.

Rather than sending the entire PaymentIntent object to the client, use its [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret). This client secret is different from your API keys that authenticate Stripe API requests.

Handle the client secret carefully, because it can complete the charge. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

Also, because the 6-digit BLIK code is only valid for 2 minutes, you can only pass it into the payment method options when confirming the PaymentIntent. In a *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes), any 6-digit code works.

#### HTML + JS

When a customer clicks to pay with Blik, use Stripe.js to submit the payment to Stripe. [Stripe.js](https://docs.stripe.com/payments/elements.md) is the foundational JavaScript library for building payment flows. It automatically handles complexities like the redirect described below, and enables you to extend your integration to other payment methods. Include the Stripe.js script on your checkout page by adding it to the `head` of your HTML file.

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

Use [stripe.confirmBlikPayment](https://docs.stripe.com/js/payment_intents/confirm_blik_payment) to confirm the payment. `confirmBlikPayment` doesn’t return until the confirmation succeeds or fails. If you want to implement your own logic to update payment status, you can disable Stripe.js polling of the API by setting the `handleActions` parameter to `false`.

```javascript
const form = document.getElementById('payment-form');
const codeInput = document.getElementById('code');

form.addEventListener('submit', (event) => {
  event.preventDefault();

  const {error} = await stripe.confirmBlikPayment(
    '{{PAYMENT_INTENT_CLIENT_SECRET}}',
    {
      payment_method: {
        blik: {},
      },
      payment_method_options: {
        blik: {
          code: code.value,
        },
      },
    }
  );
});
```

#### React

When a customer clicks to pay with Blik, use Stripe.js to submit the payment to Stripe. [Stripe.js](https://docs.stripe.com/payments/elements.md) is the foundational JavaScript library for building payment flows. It automatically handles complexities like the redirect described below, and enables you to extend your integration to other payment methods. Include the Stripe.js script on your checkout page by adding it to the `head` of your HTML file.

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

Use [stripe.confirmBlikPayment](https://docs.stripe.com/js/payment_intents/confirm_blik_payment) to confirm the payment. `confirmBlikPayment` doesn’t return until the confirmation succeeds or fails. You can disable the polling of the API by setting the `handleActions` parameter to `false`.

#### Hooks

To call `stripe.confirmBlikPayment` from your payment form component, use the [useStripe](https://docs.stripe.com/sdks/stripejs-react.md#usestripe-hook) hook.

```jsx
import React from "react";
import { useStripe } from "@stripe/react-stripe-js";

export default function CheckoutForm() {
  const stripe = useStripe();

  const handleSubmit = async (event) => {
    // We don't want to let default form submission happen here,
    // which would refresh the page.
    event.preventDefault();

    if (!stripe) {
      // Stripe.js hasn't yet loaded.
      // Make sure to disable form submission until Stripe.js has loaded.
      return;
    }

    // For brevity, this example is using uncontrolled components for
    // the code input. In a real world app you will
    // probably want to use controlled components.
    // https://reactjs.org/docs/uncontrolled-components.html
    // https://reactjs.org/docs/forms.html#controlled-components

    const code = event.target["code"];

    const { error } = await stripe.confirmBlikPayment(
      "{{PAYMENT_INTENT_CLIENT_SECRET}}",
      {
        payment_method: {
          blik: {},
        },
        payment_method_options: {
          blik: {
            code,
          },
        },
      },
    );

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
          Code
          <input name="code" placeholder="000000" required />
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

    const { stripe } = this.props;

    if (!stripe) {
      // Stripe.js hasn't yet loaded.
      // Make  sure to disable form submission until Stripe.js has loaded.
      return;
    }

    // For brevity, this example is using uncontrolled components for
    // the accountholder's name. In a real world app you will
    // probably want to use controlled components.
    // https://reactjs.org/docs/uncontrolled-components.html
    // https://reactjs.org/docs/forms.html#controlled-components

    const code = event.target["code"];

    const { error } = await stripe.confirmBlikPayment(
      "{{PAYMENT_INTENT_CLIENT_SECRET}}",
      {
        payment_method: {
          blik: {},
        },
        payment_method_options: {
          blik: {
            code,
          },
        },
      },
    );

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
            Code
            <input name="code" placeholder="000000" required />
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
      {({ stripe, elements }) => <CheckoutForm stripe={stripe} />}
    </ElementsConsumer>
  );
}
```

After confirming the PaymentIntent with valid parameters, the PaymentIntent’s `status` becomes `requires_action`. The `next_action` has the `blik_authorize` type: this means that the next step is completed by your customer, who has 60 seconds to confirm the payment inside their mobile banking app. We recommend showing a timer or a dialog to your customer to prompt them to authorize the payment within the time.

### What customers see

Inside their Banking app, customers see four lines related to each BLIK transaction:

- If you provided a value for `description` when creating the PaymentIntent, the first two lines display it (max 70 characters).
- If you provided a value for `statement_descriptor` (typically, an order ID), line 3 displays it (max 22 characters).
- The fourth line automatically populates with the URL of your website.

## Fulfill the order [Server-side]

[Use a method such as webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks) to handle order *fulfillment* (Fulfillment is the process of providing the goods or services purchased by a customer, typically after payment is collected). When a customer completes payment, the `PaymentIntent`’s status transitions to `succeeded` and sends the [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event. If a customer doesn’t pay, the `PaymentIntent` sends the [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) webhook event and returns to a status of `requires_payment_method`.

## Optional: Simulate failures in a sandbox

BLIK payments can fail for different reasons. There are immediate failures (for example, the code is expired or invalid), delayed errors (the bank declines) or timeouts (the customer didn’t respond in time). You can simulate each failure scenarios by passing `email` values matching certain patterns (documented below) when creating the `PaymentIntent`, as part of the [billing details](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_data-billing_details), with any 6-digit as BLIK code.

When confirming the `PaymentIntent` server side, a request simulating an invalid BLIK code would look like:

#### curl

```bash
curl https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT_ID}}/confirm \
  -u <<YOUR_SECRET_KEY>>: \
  -d "payment_method_data[type]"="blik" \
  -d "payment_method_options[blik][code]"="{{CODE}}" \
  -d "payment_method_data[billing_details][email]"="invalid_code@example.com"
```

### Immediate Failures

| Failure code                       | Explanation                                                                                                    | Email pattern       |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------- | ------------------- |
| `payment_method_invalid_parameter` | The code passed wasn’t a valid BLIK code.                                                                      | `.*invalid_code@.*` |
| `payment_method_invalid_parameter` | The code passed has expired. BLIK codes expire after 2 minutes, please request another code from the customer. | `.*expired_code@.*` |

### Declines (8 second delay)

| Failure code                      | Explanation                                                                                    | Email pattern             |
| --------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------- |
| `payment_method_provider_decline` | The payment has been declined because the payment limit on this bank account has been reached. | `.*limit_exceeded@.*`     |
| `payment_method_provider_decline` | The bank account has insufficient funds to complete the purchase.                              | `.*insufficient_funds@.*` |
| `payment_method_provider_decline` | The customer declined this payment.                                                            | `.*customer_declined@.*`  |
| `payment_method_provider_decline` | The payment has been declined by the customer’s bank for an unknown reason.                    | `.*bank_declined@.*`      |
| `payment_method_provider_decline` | The payment has been declined for an unknown reason.                                           | `.*blik_declined@.*`      |

### Timeouts (60 second delay)

| Failure code                      | Explanation                                                               | Email pattern           |
| --------------------------------- | ------------------------------------------------------------------------- | ----------------------- |
| `payment_method_provider_timeout` | The customer didn’t approve this payment within the allocated 60 seconds. | `.*customer_timeout@.*` |
| `payment_method_provider_timeout` | The request to the customer’s bank timed out.                             | `.*bank_timeout@.*`     |
| `payment_method_provider_timeout` | The request to the BLIK network timed out.                                | `.*blik_timeout@.*`     |

# iOS

> This is a iOS for when payment-ui is mobile and platform is ios. View the full page at https://docs.stripe.com/payments/blik/accept-a-payment?payment-ui=mobile&platform=ios.

BLIK is a [single use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method that requires customers to [authenticate](https://docs.stripe.com/payments/payment-methods.md#customer-actions) their payments. When customers want to pay online using BLIK, they request a six-digit code from their banking application and enter it into the payment collection form.

The bank sends a push notification to your customer’s mobile phone asking to authorize the payment inside their banking application. The BLIK code is valid for 2 minutes; customers have 60 seconds to authorize the payment after starting a payment. After 60 seconds, it times out and they must request a new BLIK code. Customers typically approve BLIK payments in less than 10 seconds.

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

First, create a `PaymentIntent` on your server and specify the amount to collect and the `pln` currency (BLIK doesn’t support other currencies). Add `blik` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your `PaymentIntent`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "pln",
  payment_method_types: ["blik"],
  description: "A description of what you're selling",
  statement_descriptor: "ORDER_123",
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

In your app, collect the required 6-digit BLIK code from the customer. Create a [STPConfirmBLIKOptions](https://stripe.dev/stripe-ios/stripe-payments/Classes/STPConfirmBLIKOptions.html) with the BLIK code.

#### Swift

```swift
let blikOptions = STPConfirmBLIKOptions(code: "777123")
```

## Submit the payment to Stripe [Client-side]

Retrieve the client secret from the PaymentIntent you created in step 2 and the 6-digit BLIK code you collected in step 3 to call [STPPaymentHandler confirmPayment](<https://stripe.dev/stripe-ios/stripe-payments/Classes/STPPaymentHandler.html#/c:@M@StripePayments@objc(cs)STPPaymentHandler(im)confirmPayment:withAuthenticationContext:completion:>).

#### Swift

```swift
​​let paymentIntentParams = STPPaymentIntentParams(clientSecret: paymentIntentClientSecret)

​​paymentIntentParams.paymentMethodParams = STPPaymentMethodParams(
​​    blik: STPPaymentMethodBLIKParams(),
    billingDetails: nil,
​​    metadata: nil
​​)

let confirmPaymentMethodOptions = STPConfirmPaymentMethodOptions()
confirmPaymentMethodOptions.blikOptions = blikOptions
paymentIntentParams.paymentMethodOptions = confirmPaymentMethodOptions

STPPaymentHandler.shared().confirmPayment(paymentIntentParams, with: self) { (handlerStatus, paymentIntent, error) in
    switch handlerStatus {
    case .succeeded:
        // Show a timer or a dialog to your customer to prompt them to authorize the payment.
        // Poll your server or Stripe API for the PaymentIntent status update

    case .canceled:
        // Payment was canceled

    case .failed:
        // Payment failed

    @unknown default:
        fatalError()
    }
}
```

After confirmation with valid parameters, the status of the PaymentIntent becomes `requires_action` and calls the completion block with succeeded handlerStatus. The `next_action` has the `blik_authorize` type: this means that the next step is completed by your customer, who has 60 seconds to confirm the payment inside their mobile banking app. We recommend:

- Showing a timer or dialog to your customer to prompt them to authorize the payment
- Polling your server or Stripe API for the PaymentIntent status update
- Displaying the payment confirmation to your customer as soon as the PaymentIntent status updates to `succeeded`

## Optional: Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

- **Handle events manually in the Dashboard**

  Use the Dashboard to [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments), send email receipts, handle payouts, or retry failed payments.

- **Build a custom webhook**

  [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook) handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- **Integrate a prebuilt app**

  Handle common business events, such as [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

## Optional: Simulate failures in a sandbox

BLIK payments can fail for different reasons. There are immediate failures (for example, the code is expired or invalid), delayed errors (the bank declines) or timeouts (the customer didn’t respond in time). You can simulate each failure scenarios by passing `email` values matching certain patterns (documented below) when creating the `PaymentIntent`, as part of the [billing details](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_data-billing_details), with any 6-digit as BLIK code.

### Immediate Failures

| Failure code                       | Explanation                                                                                                    | Email pattern       |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------- | ------------------- |
| `payment_method_invalid_parameter` | The code passed wasn’t a valid BLIK code.                                                                      | `.*invalid_code@.*` |
| `payment_method_invalid_parameter` | The code passed has expired. BLIK codes expire after 2 minutes, please request another code from the customer. | `.*expired_code@.*` |

### Declines (8 second delay)

| Failure code                      | Explanation                                                                                    | Email pattern             |
| --------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------- |
| `payment_method_provider_decline` | The payment has been declined because the payment limit on this bank account has been reached. | `.*limit_exceeded@.*`     |
| `payment_method_provider_decline` | The bank account has insufficient funds to complete the purchase.                              | `.*insufficient_funds@.*` |
| `payment_method_provider_decline` | The customer declined this payment.                                                            | `.*customer_declined@.*`  |
| `payment_method_provider_decline` | The payment has been declined by the customer’s bank for an unknown reason.                    | `.*bank_declined@.*`      |
| `payment_method_provider_decline` | The payment has been declined for an unknown reason.                                           | `.*blik_declined@.*`      |

### Timeouts (60 second delay)

| Failure code                      | Explanation                                                               | Email pattern           |
| --------------------------------- | ------------------------------------------------------------------------- | ----------------------- |
| `payment_method_provider_timeout` | The customer didn’t approve this payment within the allocated 60 seconds. | `.*customer_timeout@.*` |
| `payment_method_provider_timeout` | The request to the customer’s bank timed out.                             | `.*bank_timeout@.*`     |
| `payment_method_provider_timeout` | The request to the BLIK network timed out.                                | `.*blik_timeout@.*`     |

# Android

> This is a Android for when payment-ui is mobile and platform is android. View the full page at https://docs.stripe.com/payments/blik/accept-a-payment?payment-ui=mobile&platform=android.

BLIK is a [single use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method that requires customers to [authenticate](https://docs.stripe.com/payments/payment-methods.md#customer-actions) their payments. When customers want to pay online using BLIK, they request a six-digit code from their banking application and enter it into the payment collection form.

The bank sends a push notification to your customer’s mobile phone asking to authorize the payment inside their banking application. The BLIK code is valid for 2 minutes; customers have 60 seconds to authorize the payment after starting a payment. After 60 seconds, it times out and they must request a new BLIK code. Customers typically approve BLIK payments in less than 10 seconds.

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

First, create a `PaymentIntent` on your server and specify the amount to collect and the `pln` currency (BLIK doesn’t support other currencies). Add `blik` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your `PaymentIntent`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "pln",
  payment_method_types: ["blik"],
  description: "A description of what you're selling",
  statement_descriptor: "ORDER_123",
});
```

### Client-side

On the client, request a PaymentIntent from your server and store its client secret.

#### Kotlin

```kotlin
class BlikPaymentActivity: AppCompatActivity() {
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

In your app, collect the required 6-digit BLIK code from the customer. Create a `PaymentMethodOptionsParams` with the BLIK code.

#### Kotlin

```kotlin
val paymentMethodOptionsParams = PaymentMethodOptionsParams.Blik(code = "777123"),
```

## Submit the payment to Stripe [Client-side]

Retrieve the client secret from the PaymentIntent you created in step 2 and the 6-digit BLIK code you collected in step 3 and call [PaymentLauncher confirm](https://stripe.dev/stripe-android/payments-core/com.stripe.android.payments.paymentlauncher/-payment-launcher/index.html#74063765%2FFunctions%2F-1622557690).

#### Kotlin

```kotlin
class BlikPaymentActivity : AppCompatActivity() {
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
                  paymentMethodCreateParams = PaymentMethodCreateParams.createBlik(),
                  clientSecret = paymentIntentClientSecret,
                  paymentMethodOptions = paymentMethodOptionsParams
                )
        paymentLauncher.confirm(confirmParams)
    }

    private fun onPaymentResult(paymentResult: PaymentResult) {
        val message = when (paymentResult) {
            is PaymentResult.Completed -> {
                // Show a timer or a dialog to your customer to prompt them to authorize the payment.
                // Poll your server or Stripe API for the PaymentIntent status update
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

After confirmation with valid parameters, the status of the PaymentIntent becomes `requires_action` and `onPaymentResult` is called with `PaymentResult.Completed`. The `next_action` has the `blik_authorize` type: this means that the next step is completed by your customer, who has 60 seconds to confirm the payment inside their mobile banking app. We recommend:

- Showing a timer or dialog to your customer to prompt them to authorize the payment
- Polling your server or Stripe API for the PaymentIntent status update
- Displaying the payment confirmation to your customer as soon as the PaymentIntent status updates to `succeeded`

## Optional: Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

- **Handle events manually in the Dashboard**

  Use the Dashboard to [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments), send email receipts, handle payouts, or retry failed payments.

- **Build a custom webhook**

  [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook) handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- **Integrate a prebuilt app**

  Handle common business events, such as [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

## Optional: Simulate failures in a sandbox

BLIK payments can fail for different reasons. There are immediate failures (for example, the code is expired or invalid), delayed errors (the bank declines) or timeouts (the customer didn’t respond in time). You can simulate each failure scenarios by passing `email` values matching certain patterns (documented below) when creating the `PaymentIntent`, as part of the [billing details](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_data-billing_details), with any 6-digit as BLIK code.

### Immediate Failures

| Failure code                       | Explanation                                                                                                    | Email pattern       |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------- | ------------------- |
| `payment_method_invalid_parameter` | The code passed wasn’t a valid BLIK code.                                                                      | `.*invalid_code@.*` |
| `payment_method_invalid_parameter` | The code passed has expired. BLIK codes expire after 2 minutes, please request another code from the customer. | `.*expired_code@.*` |

### Declines (8 second delay)

| Failure code                      | Explanation                                                                                    | Email pattern             |
| --------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------- |
| `payment_method_provider_decline` | The payment has been declined because the payment limit on this bank account has been reached. | `.*limit_exceeded@.*`     |
| `payment_method_provider_decline` | The bank account has insufficient funds to complete the purchase.                              | `.*insufficient_funds@.*` |
| `payment_method_provider_decline` | The customer declined this payment.                                                            | `.*customer_declined@.*`  |
| `payment_method_provider_decline` | The payment has been declined by the customer’s bank for an unknown reason.                    | `.*bank_declined@.*`      |
| `payment_method_provider_decline` | The payment has been declined for an unknown reason.                                           | `.*blik_declined@.*`      |

### Timeouts (60 second delay)

| Failure code                      | Explanation                                                               | Email pattern           |
| --------------------------------- | ------------------------------------------------------------------------- | ----------------------- |
| `payment_method_provider_timeout` | The customer didn’t approve this payment within the allocated 60 seconds. | `.*customer_timeout@.*` |
| `payment_method_provider_timeout` | The request to the customer’s bank timed out.                             | `.*bank_timeout@.*`     |
| `payment_method_provider_timeout` | The request to the BLIK network timed out.                                | `.*blik_timeout@.*`     |
