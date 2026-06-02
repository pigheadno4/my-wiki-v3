<!-- Source URL: https://docs.stripe.com/payments/zip/accept-a-payment -->
<!-- Fetched: 2026-05-06 -->

# Accept a Zip payment

Learn how to accept Zip, a popular buy now, pay later payment method in Australia and the US.

# Checkout

> This is a Checkout for when payment-ui is checkout. View the full page at https://docs.stripe.com/payments/zip/accept-a-payment?payment-ui=checkout.

> Stripe can automatically present the relevant payment methods to your customers by evaluating currency, payment method restrictions, and other parameters.
>
> - Follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=checkout&ui=stripe-hosted) guide to build a Checkout integration that uses [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md).

- If you don’t want to use dynamic payment methods, follow the steps below to manually configure the payment methods in your Checkout integration.

Zip is a buy now, pay later payment method that allows customers to split purchases over a series of payments.

Customers authenticate a payment on Zip website and there is immediate notification about the success or failure of a payment.

## Determine compatibility

**Supported business locations**: AU, US

**Supported currencies**: `aud, usd`

**Presentment currencies**: `aud, usd`

**Payment mode**: Yes

**Setup mode**: No

**Subscription mode**: No

A Checkout Session must satisfy all of the following conditions to support Zip payments:

- *Prices* (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) for all line items must be expressed in Australian Dollar (currency code `aud`) or United States Dollar (currency code `usd`).

## Accept a Zip payment

> Build an integration to [accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?integration=checkout) with Checkout before using this guide.

This guides you through enabling Zip and shows the differences between accepting payments using dynamic payment methods and manually configuring payment methods.

### Enable Zip as a payment method

When creating a new [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md), you need to:

1. Add `zip` to the list of `payment_method_types`
1. Make sure all your `line_items` use the `aud` or `usd` currency.

#### Stripe-hosted page

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        currency: "aud",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "zip"],
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
        currency: "aud",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "zip"],
  return_url: "https://example.com/return",
  ui_mode: "embedded_page",
});
```

### Fulfill your orders

After accepting a payment, learn how to [fulfill orders](https://docs.stripe.com/checkout/fulfillment.md).

## Test your integration

When testing your Checkout integration, select Zip as the payment method and click **Pay**.

## Handle refunds and disputes

Learn more about Zip [disputes](https://docs.stripe.com/payments/zip.md#disputes-and-fraud) and [refunds](https://docs.stripe.com/payments/zip.md#refunds).

## See also

- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment.md)
- [Customizing Checkout](https://docs.stripe.com/payments/checkout/customization.md)

# Direct API

> This is a Direct API for when payment-ui is direct-api. View the full page at https://docs.stripe.com/payments/zip/accept-a-payment?payment-ui=direct-api.

> The content of this section refers to a *Legacy* (Technology that's no longer recommended) product. You should use the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md) guide for the most recent integration path instead. While Stripe still supports this product, this support might end if the product is deprecated.

Zip is a buy now, pay later payment method that allows customers to split purchases over a series of payments.

Customers authenticate a payment on Zip website and there is immediate notification about the success or failure of a payment.

Stripe users in Australia and the US can use the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md)—a single integration path for creating payments using any supported method—to accept [Zip](https://zip.co/au) payments.

Accepting Zip payments on your website consists of:

- Creating an object to track a payment
- Submitting the payment to Stripe for processing
- Handling the Zip redirect and relevant webhook events

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create a PaymentIntent [Server-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) is an object that represents your intent to collect a payment from a customer and tracks the lifecycle of the payment process through each stage. First, create a `PaymentIntent` on your server and specify the amount to collect and `aud` as the currency. If you already have an integration using the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md), add `zip` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your `PaymentIntent`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 2020,
  currency: "aud",
  payment_method_types: ["zip"],
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

## Collect payment method details and submit [Client-side]

When a customer clicks to pay with Zip, use Stripe.js to submit the payment to Stripe. [Stripe.js](https://docs.stripe.com/payments/elements.md) is the foundational JavaScript library for building payment flows. It automatically handles complexities like the redirect described below, and enables you to extend your integration to other payment methods. Include the Stripe.js script on your checkout page by adding it to the `head` of your HTML file.

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

Rather than sending the entire PaymentIntent object to the client, use its client secret from step 1. This is different from your API keys that authenticate Stripe API requests.

Handle the client secret carefully, because it can complete the charge. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

**Confirm the PaymentIntent**

Use [stripe.confirmZipPayment](https://docs.stripe.com/js/payment_intents/confirm_zip_payment) to handle the redirect away from your page and to complete the payment. You must also pass a [return_url](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-return_url) to this function to indicate where Stripe redirects the user after they complete the payment on Zip website.

On Zip’s payments page, the customer selects the payment options available to them. See the overview page for more details.

```javascript
// Redirects away from the client
stripe
  .confirmZipPayment("{{PAYMENT_INTENT_CLIENT_SECRET}}", {
    payment_method: {
      // Billing details is optional.
      billing_details: {
        name: "Jenny Rosen",
        email: "jenny@example.com",
      },
    },
    // Return URL where the customer should be redirected after the authorization.
    return_url: "https://example.com/checkout/complete",
  })
  .then(function (result) {
    if (result.error) {
      // Inform the customer that there was an error.
      console.log(result.error.message);
    }
  });
```

When your customer submits a payment, Stripe redirects them to the `return_url` and includes the following URL query parameters. The return page can use them to get the status of the PaymentIntent so it can display the payment status to the customer.

When you specify the `return_url`, you can also append your own query parameters for use on the return page.

| Parameter                      | Description                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_intent`               | The unique identifier for the `PaymentIntent`.                                                                                                                                                                                                                                                                                                             |
| `payment_intent_client_secret` | The [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) of the `PaymentIntent` object. For subscription integrations, this client_secret is also exposed on the `Invoice` object through [`confirmation_secret`](https://docs.stripe.com/api/invoices/object.md#invoice_object-confirmation_secret) |

When the customer is redirected back to your site, you can use the `payment_intent_client_secret` to query for the PaymentIntent and display the transaction status to your customer.

## Test Zip integration

Test your Zip integration with your test API keys by viewing the redirect page. You can test the successful payment case by authenticating the payment on the redirect page. The PaymentIntent transitions from `requires_action` to `succeeded`. To test the case where the user fails to authenticate, use your test API keys and view the redirect page. On the redirect page, click **Fail test payment**. The PaymentIntent transitions from `requires_action` to `requires_payment_method`.

## Optional: Handle the Zip redirect manually

We recommend relying on Stripe.js to handle Zip redirects and payments client-side with `confirmZipPayment`. Using Stripe.js allows you to extend your integration to other payment methods. However, you can also manually redirect your customers on your server by following these steps:

- Create and confirm a [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) of type `zip`. By specifying `payment_method_data`, we create a *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) and immediately use it with this PaymentIntent.

  You must also provide the redirect URL for your customer after they complete their payment in the `return_url` field. You can provide your own query parameters in this URL. These parameters are included in the final URL upon completing the redirect flow.

  ```node
  // Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
  // Find your keys at https://dashboard.stripe.com/apikeys.
  const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

  const paymentIntent = await stripe.paymentIntents.create({
    amount: 2021,
    currency: "aud",
    payment_method_types: ["zip"],
    confirm: true,
    payment_method_data: {
      type: "zip",
    },
    return_url: "https://example.com/checkout/complete",
  });
  ```

  The created `PaymentIntent` has a status of `requires_action` and the type for `next_action` is `redirect_to_url`.

  ```json
  {
    "status": "requires_action",
    "next_action": {
      "type": "redirect_to_url",
      "redirect_to_url": {
        "url": "https://hooks.stripe.com/...",
        "return_url": "https://example.com/checkout/complete"
      }
    },
    "id": "pi_xxx",
    "object": "payment_intent",
    "amount": 2020,
    "client_secret": "pi_xxx_secret_xxx",
    "confirm": "true",
    "confirmation_method": "automatic",
    "created": 1579259303,
    "currency": "aud",
    "livemode": true,
    "charges": {
      "data": [],
      "object": "list",
      "has_more": false,
      "url": "/v1/charges?payment_intent=pi_xxx"
    },
    "payment_method_types": ["zip"]
  }
  ```

- Redirect the customer to the URL provided in the `next_action.redirect_to_url.url` property. The code example here is approximate—the redirect method might be different in your web framework.

  When the customer finishes the payment process, we sent them to the `return_url` configured in step 1. The `payment_intent` and `payment_intent_client_secret` URL query parameters are included. If `return_url` already included query parameters, they’ll be preserved too.

  We recommend that you [rely on webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks) to confirm the status of a payment.

## Optional: Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

- **Handle events manually in the Dashboard**

  Use the Dashboard to [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments), send email receipts, handle payouts, or retry failed payments.

- **Build a custom webhook**

  [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook) handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- **Integrate a prebuilt app**

  Handle common business events, such as [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.
