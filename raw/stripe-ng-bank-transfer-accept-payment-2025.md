<!-- Source URL: https://docs.stripe.com/payments/ng-bank-transfer/accept-a-payment -->
<!-- Fetched: 2026-05-08 -->

# Accept a payment through local bank transfers in Nigeria

# Checkout

> This is a Checkout for when payment-ui is checkout. View the full page at https://docs.stripe.com/payments/ng-bank-transfer/accept-a-payment?payment-ui=checkout.

> Stripe can automatically present the relevant payment methods to your customers by evaluating currency, payment method restrictions, and other parameters.
>
> - Follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=checkout&ui=stripe-hosted) guide to build a Checkout integration that uses [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md).

- If you don’t want to use dynamic payment methods, follow the steps below to manually configure the payment methods in your Checkout integration.

Integrating with Naira bank transfer enables Nigerian customers to pay using a local bank transfer.

Stripe’s merchant of record service provider offers a redirect-based payment flow for local bank transfers (also known locally as “Transfers”). When a customer makes a payment, Stripe redirects them to the local merchant of record service provider’s checkout flow to authenticate and authorize the payment. After the customer authorizes the payment, Stripe redirects them back to your site.

## Determine compatibility

**Supported business locations**: US

**Supported currencies**: `ngn`

**Presentment currencies**: `ngn`

**Payment mode**: Yes

**Setup mode**: No

**Subscription mode**: No

[A Checkout Session](https://docs.stripe.com/payments/checkout/how-checkout-works.md#session) must satisfy all of the following conditions to support Nigerian payment methods:

- Express _prices_ (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) for all line items in Nigerian naira (currency code `ngn`).
- The transaction amount must be between 500 NGN and 100,000,000 NGN.

## Accept a Naira bank transfer payment

To enable Naira bank transfer, update your integration to:

- Add `ng_bank_transfer` to the list of `payment_method_types` when you create a [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md).
- Make sure all `line_items` use the `ngn` currency.

#### Stripe-hosted page

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        currency: "ngn",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "ng_bank_transfer"],
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
        currency: "ngn",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "ng_bank_transfer"],
  return_url: "https://example.com/return",
  ui_mode: "embedded_page",
});
```

## Test your integration

When testing your Checkout integration, select **Nigerian payment methods** as the payment method and click **Pay**.

# Direct API

> This is a Direct API for when payment-ui is direct-api. View the full page at https://docs.stripe.com/payments/ng-bank-transfer/accept-a-payment?payment-ui=direct-api.

Integrating with Naira bank transfer enables Nigerian customers to pay using a local bank transfer.

Stripe’s merchant of record service provider offers a redirect-based payment flow for local bank transfers (also known locally as “Transfers”). When a customer makes a payment, Stripe redirects them to the local merchant of record service provider’s checkout flow to authenticate and authorize the payment. After the customer authorizes the payment, Stripe redirects them back to your site.

Use the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md) to accept payments from Nigerian customers using local bank transfer.

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create a PaymentIntent [Server-side]

The [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) object represents an intent to collect a payment from a customer and tracks the payment process. To create a `PaymentIntent` that accepts a payment using Nigerian payment methods, specify:

- The amount to collect
- `ngn` as the currency
- `ng_bank_transfer` in the [payment_method_types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) list. If you maintain a list of payment method types that you pass when creating a `PaymentIntent`, add `ng_bank_transfer` to it.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1000000,
  currency: "ngn",
  payment_method_types: ["ng_bank_transfer"],
  payment_method_data: {
    type: "ng_bank_transfer",
  },
});
```

### Retrieve the client secret

The PaymentIntent includes a _client secret_ (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)) that the client side uses to securely complete the payment process. You can use different approaches to pass the client secret to the client side.

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

## Redirect to local service provider [Client-side]

When a customer clicks to pay with Naira bank transfer, use Stripe.js to submit the payment to Stripe. [Stripe.js](https://docs.stripe.com/payments/elements.md) is the foundational JavaScript library for building payment flows. It automatically handles complexities like the redirect described below, and enables you to extend your integration to other payment methods. Include the Stripe.js script on your checkout page by adding it to the `head` of your HTML file.

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

Use the [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) of the `PaymentIntent` and call `stripe.confirmPayment` to handle the local merchant of record service provider redirect. Add a `return_url` to specify where Stripe redirects the customer after they complete the payment.

```javascript
const form = document.getElementById("payment-form");

form.addEventListener("submit", async function (event) {
  event.preventDefault();

  // Set the clientSecret of the PaymentIntent
  const { error } = await stripe.confirmPayment({
    clientSecret: clientSecret,
    confirmParams: {
      payment_method_data: {
        type: "ng_bank_transfer",
      },
      // Return URL where the customer should be redirected after the authorization
      return_url: `${window.location.href}`,
    },
  });

  if (error) {
    // Inform the customer that there was an error.
    const errorElement = document.getElementById("error-message");
    errorElement.textContent = result.error.message;
  }
});
```

The `return_url` corresponds to a page on your website that displays the result of the payment. You can determine what to display by [verifying the status](https://docs.stripe.com/payments/payment-intents/verifying-status.md#checking-status) of the `PaymentIntent`. To verify the status, the Stripe redirect to the `return_url` includes the following URL query parameters. You can also append your own query parameters to the `return_url`. They persist throughout the redirect process.

| Parameter                      | Description                                                                                                                                   |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_intent`               | The unique identifier for the `PaymentIntent`.                                                                                                |
| `payment_intent_client_secret` | The [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) of the `PaymentIntent` object. |

## Test integration with Naira payment methods

Use your test API keys to test your integration with Naira payment methods by viewing the redirect page. You can test the successful payment case by authenticating the payment on the redirect page. The PaymentIntent transitions from `requires_action` to `succeeded`. To test the case where the customer fails to authenticate, use your test API keys and view the redirect page. On the redirect page, click **Fail test payment**. The PaymentIntent transitions from `requires_action` to `requires_payment_method`.

## Optional: Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

- **Handle events manually in the Dashboard**

  Use the Dashboard to [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments), send email receipts, handle payouts, or retry failed payments.

- **Build a custom webhook**

  [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook) handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- **Integrate a prebuilt app**

  Handle common business events, such as [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.
