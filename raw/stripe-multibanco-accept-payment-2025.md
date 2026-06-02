<!-- Source URL: https://docs.stripe.com/payments/multibanco/accept-a-payment -->
<!-- Fetched: 2026-05-07 -->

# Accept a Multibanco payment

Learn how to accept the Multibanco payment method.

# Checkout

> This is a Checkout for when payment-ui is checkout. View the full page at https://docs.stripe.com/payments/multibanco/accept-a-payment?payment-ui=checkout.

> Stripe can automatically present the relevant payment methods to your customers by evaluating currency, payment method restrictions, and other parameters.
>
> - Follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=checkout&ui=stripe-hosted) guide to build a Checkout integration that uses [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md).

- If you don’t want to use dynamic payment methods, follow the steps below to manually configure the payment methods in your Checkout integration.

Multibanco is a voucher-based payment method in Portugal. If your business is based in Europe or the United States, you can accept Multibanco payments from customers in Portugal using [Stripe Checkout](https://docs.stripe.com/payments/checkout.md).

To complete a transaction, customers receive a voucher that includes a Multibanco entity and reference numbers. Customers use these voucher details to make a payment outside your checkout flow through online banking or from an ATM.

Payment confirmation might be delayed by several days due to the initiation of a bank transfer when a customer pays for a Multibanco voucher. Bank transfers can encounter delays, particularly over weekends, contributing to the delay in payment confirmation.

## Determine compatibility

**Supported business locations**: Europe, US

**Supported currencies**: `eur`

**Presentment currencies**: `eur`

**Payment mode**: Yes

**Setup mode**: No

**Subscription mode**: No

A Checkout Session must satisfy all of the following conditions to support Multibanco:

- *Prices* (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) for all line items must be in the same currency (EUR).
- You can only use one-time line items (recurring *subscription* (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) plans aren’t supported).

## Accept a payment

> Build an integration to [accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?integration=checkout) with Checkout before using this guide.

This guides you through enabling Multibanco and shows the differences between accepting payments using dynamic payment methods and manually configuring payment methods.

### Enable Multibanco as a payment method

When creating a new [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md), you need to:

1. Add `multibanco` to the list of `payment_method_types`.
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
  payment_method_types: ["card", "multibanco"],
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
  payment_method_types: ["card", "multibanco"],
  return_url: "https://example.com/return",
  ui_mode: "embedded_page",
});
```

### Redirect to Stripe-hosted voucher page

> Unlike card payments, the customer won’t be redirected to the [success_url](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-success_url) with a Multibanco payment.

After submitting the Checkout form successfully, the customer is redirected to the `hosted_voucher_url`. The customer can reference the hosted page’s payment instructions for details on how to complete their payment. You can view the page on both desktop and mobile platforms, and it’s also printable.

Stripe sends a [payment_intent.requires_action](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.requires_action) event when a Multibanco voucher is created successfully. If you need to send an email with the voucher’s payment instructions link, locate the PaymentIntent at `data.object` on the `requires_action` event, and extract the `hosted_voucher_url` at [next_action.multibanco_display_details.hosted_voucher_url](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-multibanco_display_details-hosted_voucher_url) on the PaymentIntent.

### Fulfill your orders

Because Multibanco is a [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method, you need to use a method such as *webhooks* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) to monitor the payment status and handle order *fulfillment* (Fulfillment is the process of providing the goods or services purchased by a customer, typically after payment is collected). Learn more about [setting up webhooks and fulfilling orders](https://docs.stripe.com/checkout/fulfillment.md).

The following events are sent when the payment status changes:

| Event name                                                                                                                                   | Description                                                                                                                                                | Next steps                                                             |
| -------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| [checkout.session.completed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.completed)                             | The customer has successfully submitted the Checkout form. Stripe has generated a Multibanco voucher.                                                      | Wait for the customer to pay the Multibanco voucher.                   |
| [checkout.session.async_payment_succeeded](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.async_payment_succeeded) | The customer has successfully paid the Multibanco voucher. The `PaymentIntent` transitions to `succeeded`.                                                 | Fulfill the goods or services that the customer purchased.             |
| [checkout.session.async_payment_failed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.async_payment_failed)       | The Multibanco voucher has expired, or the payment has failed for some other reason. The `PaymentIntent` returns to a status of `requires_payment_method`. | Contact the customer by email and request that they place a new order. |

## Optional: Send automated payment instruction emails

You can enable Multibanco payment instruction emails on the [Email Settings](https://dashboard.stripe.com/settings/emails) page in the Dashboard. After you enable it, Stripe automatically sends payment instruction emails upon PaymentIntent confirmation. The emails contain the Multibanco voucher instructions and a link to the Stripe-hosted voucher page.

> In testing environments, instruction emails are only sent to email addresses linked to the Stripe account.

## Optional: Customize voucher appearance

Customize your customer-facing UIs in the [Branding Settings](https://dashboard.stripe.com/account/branding) page.

You can apply the following Branding settings to the Stripe-hosted voucher page:

- **Icon**: Your brand image and public business name
- **Logo**: Your brand image
- **Accent color**: The color of the Print button
- **Brand color**: The background color

## Test your integration

When testing your Checkout integration, select Multibanco as the payment method, then click **Pay**. Provide the following email patterns in the Checkout form to test different scenarios:

| Email                       | Description                                                                                                                |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `{any_prefix}@{any_domain}` | Simulates a Multibanco voucher that a customer pays. The `payment_intent.succeeded` webhook arrives after about 3 minutes. |

Example: jenny@example.com |
| `{any_prefix}succeed_immediately@{any_domain}` | Simulates a Multibanco voucher that a customer pays immediately. The `payment_intent.succeeded` webhook arrives within several seconds.

Example: succeed_immediately@example.com |
| `{any_prefix}expire_immediately@{any_domain}` | Simulates a Multibanco voucher that expires immediately. The `payment_intent.payment_failed` webhook arrives within several seconds.

Example: expire_immediately@example.com |
| `{any_prefix}expire_with_delay@{any_domain}` | Simulates a Multibanco voucher that expires before a customer pays. The `payment_intent.payment_failed` webhook arrives after about 3 minutes.

Example: expire_with_delay@example.com |
| `{any_prefix}fill_never@{any_domain}` | Simulates a Multibanco voucher that never succeeds. The `payment_intent.payment_failed` webhook arrives after 11 days, which mimics behavior in live mode. Learn about Multibanco [expiration](https://docs.stripe.com/payments/multibanco/accept-a-payment.md#expiration).

Example: fill_never@example.com |

## Expiration

Multibanco vouchers expire at the `expires_at` UNIX timestamp in [next_action.multibanco_display_details.expires_at](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-multibanco_display_details-expires_at), which is 7 days after you create the voucher. Customers can’t pay a Multibanco voucher after it expires. After expiration, the PaymentIntent’s status transitions from `requires_action` to `processing`, and Stripe sends a [payment_intent.processing](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.processing) event.

The PaymentIntent remains in the `processing` status for a maximum buffer period of 4 days to allow for potential completed payment notification delays caused by bank-transfer delays. If the Multibanco payment doesn’t complete within the buffer period, the PaymentIntent’s status transitions to `requires_payment_method` and Stripe sends a [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) event. If you receive the customer’s funds after the buffer period, Stripe automatically initiates a refund process for the mispaid amount.

## Cancelation

You can cancel Multibanco vouchers using [Cancel a PaymentIntent](https://docs.stripe.com/api/payment_intents/cancel.md). After cancelation, Stripe sends a [payment_intent.canceled](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.canceled) event.

If a customer’s funds are received for a canceled Multibanco voucher, Stripe automatically initiates a refund process for the mispaid amount.

> Canceling a pending payment invalidates the original voucher instructions. When you cancel a pending Multibanco payment, inform your customer.
>
> When you successfully reconfirm a PaymentIntent in status `requires_action`, Stripe creates new voucher instructions and a new `hosted_voucher_url`. You must provide them to your customer.

## Refunds

Learn about Multibanco [refunds](https://docs.stripe.com/payments/multibanco.md#refunds).

## See also

- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment.md)
- [Customizing Checkout](https://docs.stripe.com/payments/checkout/customization.md)

# Direct API

> This is a Direct API for when payment-ui is direct-api. View the full page at https://docs.stripe.com/payments/multibanco/accept-a-payment?payment-ui=direct-api.

> We recommend that you follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md) guide unless you need to use manual server-side confirmation, or your integration requires presenting payment methods separately. If you’ve already integrated with Elements, see the [Payment Element migration guide](https://docs.stripe.com/payments/payment-element/migration.md).

Multibanco is a voucher-based payment method in Portugal. If your business is based in Europe or the United States, you can accept Multibanco payments from customers in Portugal using the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md).

To complete a transaction, customers receive a voucher that includes a Multibanco entity and reference numbers. Customers use these voucher details to make a payment outside your checkout flow through online banking or from an ATM.

Payment confirmation might be delayed by several days due to the initiation of a bank transfer when a customer pays for a Multibanco voucher. Bank transfers can encounter delays, particularly over weekends, contributing to the delay in payment confirmation.

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

To access the Stripe API from your application, use our official libraries:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create a PaymentIntent [Server-side]

Stripe uses a [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) object to represent your intent to collect payment from a customer, tracking state changes from Multibanco voucher creation to payment completion.

Create a PaymentIntent on your server with an amount and the `eur` currency (Multibanco doesn’t support other currencies). If you already have an integration using the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md), add `multibanco` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your PaymentIntent.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  payment_method_types: ["multibanco"],
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

  <button id="submit-button">Pay with Multibanco</button>
</form>
```

## Submit the payment to Stripe [Client-side]

When a customer clicks to pay with Multibanco, use Stripe.js to submit the payment to Stripe. [Stripe.js](https://docs.stripe.com/payments/elements.md) is our foundational JavaScript library for building payment flows.

Include the Stripe.js script on your checkout page by adding it to the `head` of your HTML file.

```html
<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/dahlia/stripe.js"></script>
</head>
```

Create an instance of Stripe.js with the following JavaScript on your checkout page.

```javascript
// Set your publishable key. Remember to switch to your live publishable key in production!
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");
```

Submit the customer’s billing details by calling by calling [stripe.confirmMultibancoPayment](https://docs.stripe.com/js/payment_intents/confirm_multibanco_payment) with the [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) of the PaymentIntent object that you created.

After confirmation, Stripe automatically opens a modal to display the Multibanco voucher to your customer.

```javascript
const form = document.getElementById("payment-form");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const result = await stripe.confirmMultibancoPayment(
    "{{PAYMENT_INTENT_CLIENT_SECRET}}",
    {
      payment_method: {
        billing_details: {
          email: document.getElementById("email").value,
        },
      },
    },
  );
  // Stripe.js will open a modal to display the Multibanco voucher to your customer
  // This async function finishes when the customer closes the modal

  if (result.error) {
    // Display error to your customer
    const errorMsg = document.getElementById("error-message");
    errorMsg.innerText = result.error.message;
  }
});
```

> `stripe.confirmMultibancoPayment` might take several seconds to complete. During that time, disable your form from being resubmitted and show a waiting indicator, such as a spinner. If you receive an error, display it to the customer, re-enable the form, and hide the waiting indicator.

When a Multibanco voucher is created successfully, the value of the returned PaymentIntent’s `status` property is `requires_action`. Check the status of a PaymentIntent in the [Dashboard](https://dashboard.stripe.com/test/payments) or by inspecting the status property on the object. If the Multibanco voucher wasn’t created successfully, inspect the returned `error` to determine the cause (for example, an invalid email format).

Stripe sends a [payment_intent.requires_action](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.requires_action) event when a Multibanco voucher is created successfully. If you need to send an email with the voucher’s payment instructions link, you can locate the `hosted_voucher_url` at [payment_intent.next_action.multibanco_display_details.hosted_voucher_url](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-multibanco_display_details-hosted_voucher_url).

## Optional: Submit the payment to Stripe from your server [Server-side]

We recommend relying on Stripe.js to handle Multibanco payments client-side with [stripe.confirmMultibancoPayment](https://docs.stripe.com/js/payment_intents/confirm_multibanco_payment). Using Stripe.js extends your integration to other payment methods. However, you can also manually redirect your customers on your server:

- Set `confirm` to `true` when creating your [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) of type `multibanco`, or [confirm](https://docs.stripe.com/api/payment_intents/confirm.md) an existing PaymentIntent. You must provide the `payment_method_data.billing_details.email` property. After you specify `payment_method_data`, we create a *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) and immediately use it with this PaymentIntent.

  ```node
  // Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
  // Find your keys at https://dashboard.stripe.com/apikeys.
  const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

  const paymentIntent = await stripe.paymentIntents.create({
    amount: 1099,
    currency: "eur",
    confirm: true,
    payment_method_types: ["multibanco"],
    payment_method_data: {
      type: "multibanco",
      billing_details: {
        email: "jenny@example.com",
      },
    },
  });
  ```

  This PaymentIntent has a status of `requires_action` and the type for `next_action` is `multibanco_display_details`.

  #### Json

  ```json
  {
    "status": "requires_action",
    "next_action": {
      "multibanco_display_details": {
        "entity": "12345",
        "expires_at": 1712922993,
        "hosted_voucher_url": "https://payments.stripe.com/multibanco/voucher/...",
        "reference": "123456789"
      },
      "type": "multibanco_display_details"
    },
    "id": "pi_1G1sgdKi6xqXeNtkldRRE6HT",
    "object": "payment_intent",
    "amount": 1099,
    "client_secret": "pi_1G1sgdKi6xqXeNtkldRRE6HT_secret_h9B56ObhTN72fQiBAuzcVPb2E",
    "confirmation_method": "automatic",
    "created": 1712922950,
    "currency": "eur",
    "livemode": true,
    "payment_method_options": {
      "multibanco": {}
    },
    "payment_method_types": ["multibanco"]
  }
  ```

- Redirect the customer to the URL provided in the `next_action.multibanco_display_details.hosted_voucher_url` property. The following example is approximate. The redirect method might different in your web framework.

  #### Node.js

  ```javascript
  if (
    paymentIntent.status === "requires_action" &&
    paymentIntent.next_action.type === "multibanco_display_details"
  ) {
    const url =
      paymentIntent.next_action.multibanco_display_details.hosted_voucher_url;
    res.redirect(url);
  }
  ```

We recommend that you [rely on webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks) to confirm the status of a payment.

## Optional: Display the Multibanco details to your customer [Client-side]

We recommend relying on Stripe.js to handle displaying the Multibanco voucher with `confirmMultibancoPayment`. However, you can also manually display the voucher to your customers.

You can specify `handleActions: false` when calling `stripe.confirmMultibancoPayment` during payment submission to Stripe to indicate that you plan to handle the next action to display the Multibanco details to your customer.

```javascript
const form = document.getElementById("payment-form");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const result = await stripe.confirmMultibancoPayment(
    "{{PAYMENT_INTENT_CLIENT_SECRET}}",
    {
      payment_method: {
        billing_details: {
          email: document.getElementById("email").value,
        },
      },
    },
    { handleActions: false },
  );

  if (result.error) {
    // Display error to your customer
    const errorMsg = document.getElementById("error-message");
    errorMsg.innerText = result.error.message;
  } else {
    // A Multibanco voucher was successfully created
    const amount = result.paymentIntent.amount;
    const currency = result.paymentIntent.currency;

    const details = result.paymentIntent.next_action.multibanco_display_details;
    const entity = details.entity;
    const reference = details.reference;
    const expires_at = details.expires_at;

    // Handle the next action by displaying the Multibanco details to your customer

    // You can also use the generated hosted voucher page
    const hosted_voucher_url =
      result.paymentIntent.next_action.multibanco_display_details
        .hosted_voucher_url;
  }
});
```

### Presentation

Include, at minimum, the following:

| Detail           | Description                                                                                                                                                                                                                                                                              |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Entity number    | Locate the entity number on the PaymentIntent in [next_action.multibanco_display_details.entity](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-multibanco_display_details-entity).                                                             |
| Reference number | Locate the reference number on the PaymentIntent in [next_action.multibanco_display_details.reference](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-multibanco_display_details-reference).                                                    |
| Expiry date      | Locate the UNIX timestamp that indicates when the Multibanco voucher expires on the PaymentIntent in [next_action.multibanco_display_details.expires_at](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-multibanco_display_details-expires_at). |
| Amount           | The voucher amount.                                                                                                                                                                                                                                                                      |
| Currency         | EUR.                                                                                                                                                                                                                                                                                     |

### Customer payment instructions

1. In your online bank account or from an ATM, choose **Payment and other services**.
1. Click **Payments of services/shopping**.
1. Enter the entity number, reference number, and amount.

## Optional: Send automated payment instruction emails

You can enable Multibanco payment instruction emails on the [Email Settings](https://dashboard.stripe.com/settings/emails) page in the Dashboard. After you enable it, Stripe automatically sends payment instruction emails upon PaymentIntent confirmation. The emails contain the Multibanco voucher instructions and a link to the Stripe-hosted voucher page.

> In testing environments, instruction emails are only sent to email addresses linked to the Stripe account.

## Optional: Customize voucher appearance

Customize your customer-facing UIs in the [Branding Settings](https://dashboard.stripe.com/account/branding) page.

You can apply the following Branding settings to the Stripe-hosted voucher page:

- **Icon**: Your brand image and public business name
- **Logo**: Your brand image
- **Accent color**: The color of the Print button
- **Brand color**: The background color

## Handle post-payment events [Server-side]

Multibanco is a [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method. A customer pays for a Multibanco voucher outside your checkout flow through online banking or from an ATM.

After a Multibanco payment completes, Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event. Use the Dashboard or build a *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) handler to receive these events and run actions, such as sending an order confirmation email to your customer, logging the sale in a database, or initiating a shipping workflow.

Learn about Multibanco [expiration](https://docs.stripe.com/payments/multibanco/accept-a-payment.md#expiration).

| Event                            | Description                                                | Next steps                                                                                  |
| -------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `payment_intent.requires_action` | The Multibanco voucher is created successfully.            | Wait for the customer to pay for the Multibanco voucher.                                    |
| `payment_intent.processing`      | The customer can no longer pay for the Multibanco voucher. | Wait for the initiated payment to succeed or fail.                                          |
| `payment_intent.succeeded`       | The customer paid for the Multibanco voucher.              | Fulfill the goods or services that the customer purchased.                                  |
| `payment_intent.payment_failed`  | The customer didn’t pay for the Multibanco voucher.        | Contact the customer through email or push notification and request another payment method. |

### Receive events and run business actions

#### Manually

Use the Stripe Dashboard to view all your Stripe payments, send email receipts, handle payouts, or retry failed payments.

View your [test payments in the Dashboard](https://dashboard.stripe.com/test/payments).

#### Custom Code

Build a webhook handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

Learn how to [build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook).

## Test the integration

In a *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes), set `payment_method.billing_details.email` to the following values when you call [stripe.confirmMultibancoPayment](https://docs.stripe.com/js/payment_intents/confirm_multibanco_payment) to test different scenarios.

| Email                       | Description                                                                                                                |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `{any_prefix}@{any_domain}` | Simulates a Multibanco voucher that a customer pays. The `payment_intent.succeeded` webhook arrives after about 3 minutes. |

Example: jenny@example.com |
| `{any_prefix}succeed_immediately@{any_domain}` | Simulates a Multibanco voucher that a customer pays immediately. The `payment_intent.succeeded` webhook arrives within several seconds.

Example: succeed_immediately@example.com |
| `{any_prefix}expire_immediately@{any_domain}` | Simulates a Multibanco voucher that expires immediately. The `payment_intent.payment_failed` webhook arrives within several seconds.

Example: expire_immediately@example.com |
| `{any_prefix}expire_with_delay@{any_domain}` | Simulates a Multibanco voucher that expires before a customer pays. The `payment_intent.payment_failed` webhook arrives after about 3 minutes.

Example: expire_with_delay@example.com |
| `{any_prefix}fill_never@{any_domain}` | Simulates a Multibanco voucher that never succeeds. The `payment_intent.payment_failed` webhook arrives after 11 days, which mimics behavior in live mode. Learn about Multibanco [expiration](https://docs.stripe.com/payments/multibanco/accept-a-payment.md#expiration).

Example: fill_never@example.com |

## Expiration

Multibanco vouchers expire at the `expires_at` UNIX timestamp in [next_action.multibanco_display_details.expires_at](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-multibanco_display_details-expires_at), which is 7 days after you create the voucher. Customers can’t pay a Multibanco voucher after it expires. After expiration, the PaymentIntent’s status transitions from `requires_action` to `processing`, and Stripe sends a [payment_intent.processing](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.processing) event.

The PaymentIntent remains in the `processing` status for a maximum buffer period of 4 days to allow for potential completed payment notification delays caused by bank-transfer delays. If the Multibanco payment doesn’t complete within the buffer period, the PaymentIntent’s status transitions to `requires_payment_method` and Stripe sends a [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) event. If you receive the customer’s funds after the buffer period, Stripe automatically initiates a refund process for the mispaid amount.

## Cancelation

You can cancel Multibanco vouchers using [Cancel a PaymentIntent](https://docs.stripe.com/api/payment_intents/cancel.md). After cancelation, Stripe sends a [payment_intent.canceled](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.canceled) event.

If a customer’s funds are received for a canceled Multibanco voucher, Stripe automatically initiates a refund process for the mispaid amount.

> Canceling a pending payment invalidates the original voucher instructions. When you cancel a pending Multibanco payment, inform your customer.
>
> When you successfully reconfirm a PaymentIntent in status `requires_action`, Stripe creates new voucher instructions and a new `hosted_voucher_url`. You must provide them to your customer.

## Refunds

Learn about Multibanco [refunds](https://docs.stripe.com/payments/multibanco.md#refunds).

# iOS

> This is a iOS for when payment-ui is mobile and platform is ios. View the full page at https://docs.stripe.com/payments/multibanco/accept-a-payment?payment-ui=mobile&platform=ios.

> We recommend that you follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md) guide unless you need to use manual server-side confirmation, or your integration requires presenting payment methods separately. If you’ve already integrated with Elements, see the [Payment Element migration guide](https://docs.stripe.com/payments/payment-element/migration.md).

Multibanco is a voucher-based payment method in Portugal. If your business is based in Europe or the United States, you can accept Multibanco payments from customers in Portugal using the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md).

To complete a transaction, customers receive a voucher that includes a Multibanco entity and reference numbers. Customers use these voucher details to make a payment outside your checkout flow through online banking or from an ATM.

Payment confirmation might be delayed by several days due to the initiation of a bank transfer when a customer pays for a Multibanco voucher. Bank transfers can encounter delays, particularly over weekends, contributing to the delay in payment confirmation.

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

Stripe uses a [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) object to represent your intent to collect payment from a customer, tracking state changes from Multibanco voucher creation to payment completion.

### Server-side

Create a PaymentIntent on your server with an amount and the `eur` currency (Multibanco doesn’t support other currencies). If you already have an integration using the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md), add `multibanco` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your PaymentIntent.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  payment_method_types: ["multibanco"],
});
```

The returned PaymentIntent includes a *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)), that you’ll use to *confirm* (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) the PaymentIntent. Send the client secret back to the client so you can use it in the next step.

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

## Collect payment method details [Client-side]

In your app, collect the following required billing details from the customer. Create a [STPPaymentIntentParams](https://stripe.dev/stripe-ios/stripe-payments/Classes/STPPaymentIntentParams.html) with the billing details.

| Field   | Value                                   |
| ------- | --------------------------------------- |
| `email` | The full email address of the customer. |

#### Swift

```swift
let billingDetails = STPPaymentMethodBillingDetails()
billingDetails.email = "jenny@example.com"
```

## Submit the payment to Stripe [Client-side]

Submit the customer’s billing details by calling [STPPaymentHandler confirmPayment](<https://stripe.dev/stripe-ios/stripe-payments/Classes/STPPaymentHandler.html#/c:@M@StripePayments@objc(cs)STPPaymentHandler(im)confirmPayment:withAuthenticationContext:completion:>) with the [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) of the PaymentIntent object that you created. This presents a webview to display the Multibanco voucher. Afterwards, the completion block is called with the result of the payment.

#### Swift

```swift
let paymentIntentParams = STPPaymentIntentParams(clientSecret: paymentIntentClientSecret)
let multibancoParams = STPPaymentMethodMultibancoParams();
paymentIntentParams.paymentMethodParams = STPPaymentMethodParams(
    multibanco: multibancoParams,
    billingDetails: billingDetails,
    metadata: nil
)

STPPaymentHandler.shared().confirmPayment(paymentIntentParams, with: self) { (handlerStatus, paymentIntent, error) in
    switch handlerStatus {
    case .succeeded:
        // The Multibanco voucher was displayed successfully. The customer can now pay the Multibanco voucher
    case .canceled:
        // Handle cancelation
    case .failed:
        // Handle failure
    @unknown default:
        fatalError()
    }
}
```

Stripe sends a [payment_intent.requires_action](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.requires_action) event when a Multibanco voucher is created successfully. If you need to send an email with the voucher’s payment instructions link, you can locate the `hosted_voucher_url` at [payment_intent.next_action.multibanco_display_details.hosted_voucher_url](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-multibanco_display_details-hosted_voucher_url).

## Optional: Send automated payment instruction emails

You can enable Multibanco payment instruction emails on the [Email Settings](https://dashboard.stripe.com/settings/emails) page in the Dashboard. After you enable it, Stripe automatically sends payment instruction emails upon PaymentIntent confirmation. The emails contain the Multibanco voucher instructions and a link to the Stripe-hosted voucher page.

> In testing environments, instruction emails are only sent to email addresses linked to the Stripe account.

## Optional: Customize voucher appearance

Customize your customer-facing UIs in the [Branding Settings](https://dashboard.stripe.com/account/branding) page.

You can apply the following Branding settings to the Stripe-hosted voucher page:

- **Icon**: Your brand image and public business name
- **Logo**: Your brand image
- **Accent color**: The color of the Print button
- **Brand color**: The background color

## Handle post-payment events [Server-side]

Multibanco is a [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method. A customer pays for a Multibanco voucher outside your checkout flow through online banking or from an ATM.

After a Multibanco payment completes, Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event. Use the Dashboard or build a *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) handler to receive these events and run actions, such as sending an order confirmation email to your customer, logging the sale in a database, or initiating a shipping workflow.

Learn about Multibanco [expiration](https://docs.stripe.com/payments/multibanco/accept-a-payment.md#expiration).

| Event                            | Description                                                | Next steps                                                                                  |
| -------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `payment_intent.requires_action` | The Multibanco voucher is created successfully.            | Wait for the customer to pay for the Multibanco voucher.                                    |
| `payment_intent.processing`      | The customer can no longer pay for the Multibanco voucher. | Wait for the initiated payment to succeed or fail.                                          |
| `payment_intent.succeeded`       | The customer paid for the Multibanco voucher.              | Fulfill the goods or services that the customer purchased.                                  |
| `payment_intent.payment_failed`  | The customer didn’t pay for the Multibanco voucher.        | Contact the customer through email or push notification and request another payment method. |

### Receive events and run business actions

#### Manually

Use the Stripe Dashboard to view all your Stripe payments, send email receipts, handle payouts, or retry failed payments.

View your [test payments in the Dashboard](https://dashboard.stripe.com/test/payments).

#### Custom Code

Build a webhook handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

Learn how to [build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook).

## Test the integration

In a *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes), set [STPPaymentMethodBillingDetails email](<https://stripe.dev/stripe-ios/stripe-payments/Classes/STPPaymentMethodBillingDetails.html#/c:@M@StripePayments@objc(cs)STPPaymentMethodBillingDetails(py)email>) to the following values when you call [STPPaymentHandler confirmPayment](<https://stripe.dev/stripe-ios/stripe-payments/Classes/STPPaymentHandler.html#/c:@M@StripePayments@objc(cs)STPPaymentHandler(im)confirmPayment:withAuthenticationContext:completion:>) to test different scenarios.

| Email                       | Description                                                                                                                |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `{any_prefix}@{any_domain}` | Simulates a Multibanco voucher that a customer pays. The `payment_intent.succeeded` webhook arrives after about 3 minutes. |

Example: jenny@example.com |
| `{any_prefix}succeed_immediately@{any_domain}` | Simulates a Multibanco voucher that a customer pays immediately. The `payment_intent.succeeded` webhook arrives within several seconds.

Example: succeed_immediately@example.com |
| `{any_prefix}expire_immediately@{any_domain}` | Simulates a Multibanco voucher that expires immediately. The `payment_intent.payment_failed` webhook arrives within several seconds.

Example: expire_immediately@example.com |
| `{any_prefix}expire_with_delay@{any_domain}` | Simulates a Multibanco voucher that expires before a customer pays. The `payment_intent.payment_failed` webhook arrives after about 3 minutes.

Example: expire_with_delay@example.com |
| `{any_prefix}fill_never@{any_domain}` | Simulates a Multibanco voucher that never succeeds. The `payment_intent.payment_failed` webhook arrives after 11 days, which mimics behavior in live mode. Learn about Multibanco [expiration](https://docs.stripe.com/payments/multibanco/accept-a-payment.md#expiration).

Example: fill_never@example.com |

## Expiration

Multibanco vouchers expire at the `expires_at` UNIX timestamp in [next_action.multibanco_display_details.expires_at](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-multibanco_display_details-expires_at), which is 7 days after you create the voucher. Customers can’t pay a Multibanco voucher after it expires. After expiration, the PaymentIntent’s status transitions from `requires_action` to `processing`, and Stripe sends a [payment_intent.processing](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.processing) event.

The PaymentIntent remains in the `processing` status for a maximum buffer period of 4 days to allow for potential completed payment notification delays caused by bank-transfer delays. If the Multibanco payment doesn’t complete within the buffer period, the PaymentIntent’s status transitions to `requires_payment_method` and Stripe sends a [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) event. If you receive the customer’s funds after the buffer period, Stripe automatically initiates a refund process for the mispaid amount.

## Cancelation

You can cancel Multibanco vouchers using [Cancel a PaymentIntent](https://docs.stripe.com/api/payment_intents/cancel.md). After cancelation, Stripe sends a [payment_intent.canceled](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.canceled) event.

If a customer’s funds are received for a canceled Multibanco voucher, Stripe automatically initiates a refund process for the mispaid amount.

> Canceling a pending payment invalidates the original voucher instructions. When you cancel a pending Multibanco payment, inform your customer.
>
> When you successfully reconfirm a PaymentIntent in status `requires_action`, Stripe creates new voucher instructions and a new `hosted_voucher_url`. You must provide them to your customer.

## Refunds

Learn about Multibanco [refunds](https://docs.stripe.com/payments/multibanco.md#refunds).

# Android

> This is a Android for when payment-ui is mobile and platform is android. View the full page at https://docs.stripe.com/payments/multibanco/accept-a-payment?payment-ui=mobile&platform=android.

> We recommend that you follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md) guide unless you need to use manual server-side confirmation, or your integration requires presenting payment methods separately. If you’ve already integrated with Elements, see the [Payment Element migration guide](https://docs.stripe.com/payments/payment-element/migration.md).

Multibanco is a voucher-based payment method in Portugal. If your business is based in Europe or the United States, you can accept Multibanco payments from customers in Portugal using the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md).

To complete a transaction, customers receive a voucher that includes a Multibanco entity and reference numbers. Customers use these voucher details to make a payment outside your checkout flow through online banking or from an ATM.

Payment confirmation might be delayed by several days due to the initiation of a bank transfer when a customer pays for a Multibanco voucher. Bank transfers can encounter delays, particularly over weekends, contributing to the delay in payment confirmation.

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

Stripe uses a [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) object to represent your intent to collect payment from a customer, tracking state changes from Multibanco voucher creation to payment completion.

### Server-side

Create a PaymentIntent on your server with an amount and the `eur` currency (Multibanco doesn’t support other currencies). If you already have an integration using the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md), add `multibanco` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your PaymentIntent.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  payment_method_types: ["multibanco"],
});
```

The returned PaymentIntent includes a *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)), that you’ll use to *confirm* (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) the PaymentIntent. Send the client secret back to the client so you can use it in the next step.

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

## Collect payment method details [Client-side]

In your app, collect the following required billing details from the customer. Create a [PaymentMethodCreateParams](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-payment-method-create-params/index.html) with the billing details.

| Field   | Value                                   |
| ------- | --------------------------------------- |
| `email` | The full email address of the customer. |

#### Kotlin

```kotlin
val billingDetails = PaymentMethod.BillingDetails(email = "jenny@example.com")
val paymentMethodCreateParams = PaymentMethodCreateParams.createMultibanco(billingDetails)
```

## Submit the payment to Stripe [Client-side]

Submit the customer’s billing details by calling [PaymentLauncher confirm](https://stripe.dev/stripe-android/payments-core/com.stripe.android.payments.paymentlauncher/-payment-launcher/index.html#74063765%2FFunctions%2F-1622557690) with the [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) of the PaymentIntent object that you created. This presents a webview to display the Multibanco voucher. Afterwards, `onPaymentResult` is called with the result of the payment.

#### Kotlin

```kotlin
class MultibancoActivity : AppCompatActivity() {
    // ...
    private lateinit var paymentIntentClientSecret: String
    private val paymentLauncher: PaymentLauncher by lazy {
        val paymentConfiguration = PaymentConfiguration.getInstance(applicationContext)
        PaymentLauncher.Companion.create(
            this,
            paymentConfiguration.publishableKey,
            paymentConfiguration.stripeAccountId,
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
        when (paymentResult) {
            is PaymentResult.Completed -> {
                // The Multibanco voucher was displayed successfully. The customer can now pay the Multibanco voucher
            }
            is PaymentResult.Canceled -> {
                // Handle cancelation
            }
            is PaymentResult.Failed -> {
                // Handle failure
            }
        }
    }
}
```

Stripe sends a [payment_intent.requires_action](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.requires_action) event when a Multibanco voucher is created successfully. If you need to send an email with the voucher’s payment instructions link, you can locate the `hosted_voucher_url` at [payment_intent.next_action.multibanco_display_details.hosted_voucher_url](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-multibanco_display_details-hosted_voucher_url).

## Optional: Send automated payment instruction emails

You can enable Multibanco payment instruction emails on the [Email Settings](https://dashboard.stripe.com/settings/emails) page in the Dashboard. After you enable it, Stripe automatically sends payment instruction emails upon PaymentIntent confirmation. The emails contain the Multibanco voucher instructions and a link to the Stripe-hosted voucher page.

> In testing environments, instruction emails are only sent to email addresses linked to the Stripe account.

## Optional: Customize voucher appearance

Customize your customer-facing UIs in the [Branding Settings](https://dashboard.stripe.com/account/branding) page.

You can apply the following Branding settings to the Stripe-hosted voucher page:

- **Icon**: Your brand image and public business name
- **Logo**: Your brand image
- **Accent color**: The color of the Print button
- **Brand color**: The background color

## Handle post-payment events [Server-side]

Multibanco is a [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method. A customer pays for a Multibanco voucher outside your checkout flow through online banking or from an ATM.

After a Multibanco payment completes, Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event. Use the Dashboard or build a *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) handler to receive these events and run actions, such as sending an order confirmation email to your customer, logging the sale in a database, or initiating a shipping workflow.

Learn about Multibanco [expiration](https://docs.stripe.com/payments/multibanco/accept-a-payment.md#expiration).

| Event                            | Description                                                | Next steps                                                                                  |
| -------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `payment_intent.requires_action` | The Multibanco voucher is created successfully.            | Wait for the customer to pay for the Multibanco voucher.                                    |
| `payment_intent.processing`      | The customer can no longer pay for the Multibanco voucher. | Wait for the initiated payment to succeed or fail.                                          |
| `payment_intent.succeeded`       | The customer paid for the Multibanco voucher.              | Fulfill the goods or services that the customer purchased.                                  |
| `payment_intent.payment_failed`  | The customer didn’t pay for the Multibanco voucher.        | Contact the customer through email or push notification and request another payment method. |

### Receive events and run business actions

#### Manually

Use the Stripe Dashboard to view all your Stripe payments, send email receipts, handle payouts, or retry failed payments.

View your [test payments in the Dashboard](https://dashboard.stripe.com/test/payments).

#### Custom Code

Build a webhook handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

Learn how to [build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook).

## Test the integration

In a *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes), set [PaymentMethod.BillingDetails#email](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-payment-method/-billing-details/index.html) to the following values when you call [Stripe\# confirmPayment()](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-stripe/confirm-payment.html) to test different scenarios.

| Email                       | Description                                                                                                                |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `{any_prefix}@{any_domain}` | Simulates a Multibanco voucher that a customer pays. The `payment_intent.succeeded` webhook arrives after about 3 minutes. |

Example: jenny@example.com |
| `{any_prefix}succeed_immediately@{any_domain}` | Simulates a Multibanco voucher that a customer pays immediately. The `payment_intent.succeeded` webhook arrives within several seconds.

Example: succeed_immediately@example.com |
| `{any_prefix}expire_immediately@{any_domain}` | Simulates a Multibanco voucher that expires immediately. The `payment_intent.payment_failed` webhook arrives within several seconds.

Example: expire_immediately@example.com |
| `{any_prefix}expire_with_delay@{any_domain}` | Simulates a Multibanco voucher that expires before a customer pays. The `payment_intent.payment_failed` webhook arrives after about 3 minutes.

Example: expire_with_delay@example.com |
| `{any_prefix}fill_never@{any_domain}` | Simulates a Multibanco voucher that never succeeds. The `payment_intent.payment_failed` webhook arrives after 11 days, which mimics behavior in live mode. Learn about Multibanco [expiration](https://docs.stripe.com/payments/multibanco/accept-a-payment.md#expiration).

Example: fill_never@example.com |

## Expiration

Multibanco vouchers expire at the `expires_at` UNIX timestamp in [next_action.multibanco_display_details.expires_at](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-multibanco_display_details-expires_at), which is 7 days after you create the voucher. Customers can’t pay a Multibanco voucher after it expires. After expiration, the PaymentIntent’s status transitions from `requires_action` to `processing`, and Stripe sends a [payment_intent.processing](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.processing) event.

The PaymentIntent remains in the `processing` status for a maximum buffer period of 4 days to allow for potential completed payment notification delays caused by bank-transfer delays. If the Multibanco payment doesn’t complete within the buffer period, the PaymentIntent’s status transitions to `requires_payment_method` and Stripe sends a [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) event. If you receive the customer’s funds after the buffer period, Stripe automatically initiates a refund process for the mispaid amount.

## Cancelation

You can cancel Multibanco vouchers using [Cancel a PaymentIntent](https://docs.stripe.com/api/payment_intents/cancel.md). After cancelation, Stripe sends a [payment_intent.canceled](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.canceled) event.

If a customer’s funds are received for a canceled Multibanco voucher, Stripe automatically initiates a refund process for the mispaid amount.

> Canceling a pending payment invalidates the original voucher instructions. When you cancel a pending Multibanco payment, inform your customer.
>
> When you successfully reconfirm a PaymentIntent in status `requires_action`, Stripe creates new voucher instructions and a new `hosted_voucher_url`. You must provide them to your customer.

## Refunds

Learn about Multibanco [refunds](https://docs.stripe.com/payments/multibanco.md#refunds).
