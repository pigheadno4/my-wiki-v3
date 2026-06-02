<!-- Source URL: https://docs.stripe.com/payments/paynow/accept-a-payment -->
<!-- Fetched: 2026-05-06 -->

# Accept a PayNow payment

Accept online payments with PayNow, a funds transfer service popular in Singapore.

# Checkout

> This is a Checkout for when payment-ui is checkout. View the full page at https://docs.stripe.com/payments/paynow/accept-a-payment?payment-ui=checkout.

> Stripe can automatically present the relevant payment methods to your customers by evaluating currency, payment method restrictions, and other parameters.
>
> - Follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=checkout&ui=stripe-hosted) guide to build a Checkout integration that uses [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md).

- If you don’t want to use dynamic payment methods, follow the steps below to manually configure the payment methods in your Checkout integration.

PayNow is a [single-use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method. Customers pay with PayNow by scanning the QR code that they see during Checkout. Completing the payment redirects customers back to your website.

This guide describes using Paynow in your online checkout flow. For in-person payments with Stripe Terminal, see [Additional payment methods](https://docs.stripe.com/terminal/payments/additional-payment-methods.md).

## Determine compatibility

**Supported business locations**: SG

**Supported currencies**: `sgd`

**Presentment currencies**: `sgd`

**Payment mode**: Yes

**Setup mode**: No

**Subscription mode**: No

A Checkout Session must satisfy all of the following conditions to support PayNow payments:

- *Prices* (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) for all line items must be in the same currency, and must be in `sgd`.
- You can only use one-time line items (PayNow Checkout Sessions don’t support recurring *subscription* (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) plans).

## Accept a payment

> This guide builds on the foundational [accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?integration=checkout) Checkout integration.

This guides you through enabling PayNow and shows the differences between accepting payments using dynamic payment methods and manually configuring payment methods.

### Enable PayNow as a payment method

When creating a new [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md), you need to:

1. Add `paynow` to the list of `payment_method_types`.
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
        currency: "sgd",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "paynow"],
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
        currency: "sgd",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "paynow"],
  return_url: "https://example.com/return",
  ui_mode: "embedded_page",
});
```

### Fulfill your orders

After accepting a payment, learn how to [fulfill orders](https://docs.stripe.com/checkout/fulfillment.md).

## Test your integration

When testing your Checkout integration, select PayNow as the payment method and click the **Generate QR code** button, which creates and renders a QR code.

While testing, you can scan the QR code with a QR code scanning application on your mobile device. The QR code payload contains a URL which brings you to a Stripe-hosted PayNow test payment page where you can either authorize or fail the test payment.

In live mode, you’ll be able to scan the QR code using a preferred banking app or payment app that supports PayNow.

## See also

- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment.md)
- [Customizing Checkout](https://docs.stripe.com/payments/checkout/customization.md)

# Direct API

> This is a Direct API for when payment-ui is direct-api. View the full page at https://docs.stripe.com/payments/paynow/accept-a-payment?payment-ui=direct-api.

PayNow is a [single-use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method. Customers use their preferred app from participating banks and participating non-bank financial institutions to scan the QR code presented to them in the checkout flow and complete the payment.

This guide describes using Paynow in your online checkout flow. For in-person payments with Stripe Terminal, see [Additional payment methods](https://docs.stripe.com/terminal/payments/additional-payment-methods.md).

## Set up Stripe

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create a PaymentIntent [Server-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) is an object that represents your intent to collect payment from a customer and tracks the lifecycle of the payment process through each stage. First, create a PaymentIntent on your server and specify the amount to collect and the currency. If you already have an integration using the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md), add `paynow` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your `PaymentIntent`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["paynow"],
  payment_method_data: {
    type: "paynow",
  },
  amount: 1099,
  currency: "sgd",
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

## Display the PayNow QR Code [Client-side]

In this step, you’ll complete PayNow payments on the client with [Stripe.js](https://docs.stripe.com/payments/elements.md). Include the Stripe.js script on your checkout page by adding it to the `head` of your HTML file.

#### HTML

```html
<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/dahlia/stripe.js"></script>
</head>
```

Create an instance of Stripe.js with the following JavaScript on your checkout page.

#### JavaScript

```js
// Set your publishable key. Remember to change this to your live publishable key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
var stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");
```

Use `stripe.confirmPayNowPayment` to confirm the payment on the client side.

#### JavaScript

```js
var form = document.getElementById("payment-form");

form.addEventListener("submit", function (event) {
  event.preventDefault();

  // Set the clientSecret here you got in Step 2
  stripe.confirmPayNowPayment(clientSecret).then((res) => {
    if (res.paymentIntent.status === "succeeded") {
      // The user scanned the QR code
    } else {
      // The user closed the modal, cancelling payment
    }
  });
});
```

After you call `confirmPayNowPayment`, the webpage displays a QR code. Your customers can scan the QR code and authenticate the payment using their preferred banking app or payment app. You should remain on the page with the QR code until Stripe [fulfills the order](https://docs.stripe.com/payments/paynow/accept-a-payment.md#fulfill-order) and you know the outcome of the payment.

## Fulfill the order [Server-side]

Use a method such as [webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks) to handle order *fulfillment* (Fulfillment is the process of providing the goods or services purchased by a customer, typically after payment is collected), instead of relying on your customer to return to the payment status page. When a customer completes payment, the `PaymentIntent` transitions to `succeeded` and emits the [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event.

## Test your integration

While testing, you can scan the QR code with a QR code scanning application on your mobile device. The QR code payload contains a URL that redirects you to a Stripe-hosted PayNow test payment page where you can either authorize or fail the test payment.

In live mode, you can scan the QR code using an app from participating banks and participating non-bank financial institutions.
