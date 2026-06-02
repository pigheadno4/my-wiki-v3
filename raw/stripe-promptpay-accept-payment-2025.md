<!-- Source URL: https://docs.stripe.com/payments/promptpay/accept-a-payment -->
<!-- Fetched: 2026-05-06 -->

# Accept a PromptPay payment

Accept payments with PromptPay, an instant funds transfer service in Thailand.

# Checkout

> This is a Checkout for when payment-ui is checkout. View the full page at https://docs.stripe.com/payments/promptpay/accept-a-payment?payment-ui=checkout.

> Stripe can automatically present the relevant payment methods to your customers by evaluating currency, payment method restrictions, and other parameters.
>
> - Follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=checkout&ui=stripe-hosted) guide to build a Checkout integration that uses [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md).

- If you don’t want to use dynamic payment methods, follow the steps below to manually configure the payment methods in your Checkout integration.

PromptPay is a [single-use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method where customers pay with PromptPay by scanning the QR code that they see during checkout. Completing the payment redirects customers back to your website.

## Determine compatibility

**Supported business locations**: TH

**Supported currencies**: `thb`

**Presentment currencies**: `thb`

**Payment mode**: Yes

**Setup mode**: No

**Subscription mode**: No

A Checkout Session must satisfy all of the following conditions to support PromptPay payments:

- *Prices* (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) for all line items must be in the same currency. If you have line items in different currencies, create separate Checkout Sessions for each currency.
- You can only use one-time line items (PromptPay Checkout Sessions don’t support recurring *subscription* (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) plans).

## Accept a payment

> This guide builds on the foundational [accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?integration=checkout) Checkout integration.

This guides you through enabling PromptPay and shows the differences between accepting payments using dynamic payment methods and manually configuring payment methods.

### Enable PromptPay as a payment method

When creating a new [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md), you need to:

1. Add `promptpay` to the list of `payment_method_types`.
1. Make sure all your `line_items` use the same currency.

#### Stripe-hosted page

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        currency: "thb",
        product_data: {
          name: "เสื้อยืด",
        },
        unit_amount: 1000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "promptpay"],
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
        currency: "thb",
        product_data: {
          name: "เสื้อยืด",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "promptpay"],
  return_url: "https://example.com/return",
  ui_mode: "embedded_page",
});
```

### Fulfill your orders

After accepting a payment, learn how to [fulfill orders](https://docs.stripe.com/checkout/fulfillment.md).

## Test your integration

When testing your Checkout integration, select PromptPay as the payment method and click the **Generate QR code** button, which creates and renders a QR code.

While testing, you can scan the QR code with a QR code scanning application on your mobile device. The QR code payload contains a URL which brings you to a Stripe-hosted PromptPay test payment page where you can either authorize or fail the test payment.

In live mode, you’ll be able to scan the QR code using a preferred banking app or payment app that supports PromptPay.

## See also

- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment.md)
- [Customizing Checkout](https://docs.stripe.com/payments/checkout/customization.md)

# Direct API

> This is a Direct API for when payment-ui is direct-api. View the full page at https://docs.stripe.com/payments/promptpay/accept-a-payment?payment-ui=direct-api.

> We recommend that you follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md) guide unless you need to use manual server-side confirmation, or your integration requires presenting payment methods separately. If you’ve already integrated with Elements, see the [Payment Element migration guide](https://docs.stripe.com/payments/payment-element/migration.md).

PromptPay is a [single-use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method. Customers use their preferred banking app or payment app to scan the QR code presented to them during checkout. This loads a payment screen where they complete the payment.

## Set up Stripe

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create a PaymentIntent [Server-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) is an object that represents your intent to collect payment from a customer and tracks the lifecycle of the payment process through each stage. First, create a PaymentIntent on your server and specify the amount to collect and the currency. If you already have an integration using the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md), add `promptpay` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your `PaymentIntent`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["promptpay"],
  amount: 10900,
  currency: "thb",
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

Create a payment form on your client to collect the required billing details from the customer:

| Field   | Value                                   |
| ------- | --------------------------------------- |
| `email` | The full email address of the customer. |

```html
<form id="payment-form">
  <div class="form-row">
    <label for="email"> Email </label>
    <input id="email" name="email" required />
  </div>

  <!-- Used to display form errors. -->
  <div id="error-message" role="alert"></div>

  <button id="submit-button">Pay with PromptPay</button>
</form>
```

## Display the PromptPay QR Code [Client-side]

In this step, you’ll complete PromptPay payments on the client with [Stripe.js](https://docs.stripe.com/payments/elements.md). Include the Stripe.js script on your checkout page by adding it to the `head` of your HTML file.

#### HTML

```html
<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/dahlia/stripe.js"></script>
</head>
```

Create an instance of Stripe.js with the following JavaScript snippet on your checkout page.

#### JavaScript

```js
// Set your publishable key. Remember to change this to your live publishable key in production!
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");
```

Use `stripe.confirmPromptPayPayment` to confirm the payment on the client side.

#### JavaScript

```js
const form = document.getElementById("payment-form");

form.addEventListener("submit", function (event) {
  event.preventDefault();

  // Set the clientSecret here you got in Step 2
  stripe
    .confirmPromptPayPayment(clientSecret, {
      payment_method: {
        type: "promptpay",
        billing_details: {
          email: document.getElementById("email").value,
        },
      },
    })
    // Stripe.js will open a modal to display the PromptPay QR Code to your customer
    .then((res) => {
      if (res.paymentIntent.status === "succeeded") {
        // The user scanned the QR code
      } else {
        // The user closed the modal, cancelling payment
      }
    });
});
```

After calling `confirmPromptPayPayment`, a QR code displays on the webpage. Your customers can scan the QR code and authenticate the payment using their preferred banking app or payment app. A few seconds after customers authenticate the payment successfully, the QR code modal closes automatically and you can [fulfill the order](https://docs.stripe.com/payments/promptpay/accept-a-payment.md#fulfill-order).

## Fulfill the order [Server-side]

[Use a method such as webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks) to handle order *fulfillment* (Fulfillment is the process of providing the goods or services purchased by a customer, typically after payment is collected), instead of relying on your customer to return to the payment status page. When a customer completes payment, the `PaymentIntent` transitions to `succeeded` and emits the [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event.

## Test your integration

*Sandboxes* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes) have a **Simulate scan** button that replaces the QR code. The button opens a Stripe-hosted PromptPay test payment page where you can either authorize or fail the test payment.

If you’re not using Stripe.js or another Stripe-hosted solution to display the QR code, scan the QR code with a QR code scanning application on your mobile device. The QR code payload contains a URL that brings you the same PromptPay test payment page.

In live mode, you can scan the QR code using a preferred banking app or payment app that supports PromptPay.
