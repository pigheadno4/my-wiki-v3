<!-- Source URL: https://docs.stripe.com/payments/konbini/accept-a-payment -->
<!-- Fetched: 2026-05-07 -->

# Konbini payments

Use the Payment Intents and Payment Methods APIs to accept payments through Konbini, a common way to make payments through convenience stores in Japan.

# Checkout

> This is a Checkout for when payment-ui is checkout. View the full page at https://docs.stripe.com/payments/konbini/accept-a-payment?payment-ui=checkout.

> Stripe can automatically present the relevant payment methods to your customers by evaluating currency, payment method restrictions, and other parameters.
>
> - Follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=checkout&ui=stripe-hosted) guide to build a Checkout integration that uses [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md).

- If you don’t want to use dynamic payment methods, follow the steps below to manually configure the payment methods in your Checkout integration.

Konbini is a [single use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method where customers are required to [take additional steps](https://docs.stripe.com/payments/payment-methods.md#customer-actions) to complete their payment. Customers pay by providing a payment code, confirmation number, and cash payment at Japanese convenience stores. Stripe notifies you when the payment is completed.

## Determine compatibility

**Supported business locations**: JP

**Supported currencies**: `jpy`

**Presentment currencies**: `jpy`

**Payment mode**: Yes

**Setup mode**: No

**Subscription mode**: No

A Checkout Session must satisfy all of the following conditions to support Konbini payments:

- *Prices* (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) for all line items must be in the same currency (JPY).
- You can only use one-time line items (recurring *subscription* (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) plans aren’t supported).

## Accept a payment

> Build an integration to [accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?integration=checkout) with Checkout before using this guide.

This guides you through enabling Konbini and shows the differences between accepting payments using dynamic payment methods and manually configuring payment methods.

### Enable Konbini as a payment method

When creating a new [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md), you need to:

1. Add `konbini` to the list of `payment_method_types`.
1. Make sure all your `line_items` use the `jpy` currency.

#### Stripe-hosted page

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        currency: "jpy",
        product_data: {
          name: "Tシャツ",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "konbini"],
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
        currency: "jpy",
        product_data: {
          name: "Tシャツ",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "konbini"],
  return_url: "https://example.com/return",
  ui_mode: "embedded_page",
});
```

### Additional payment method options

Payment method options can be specified in the [payment method options](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_method_options-konbini) under the `konbini` key.

| Field                | Value                                                                                                                                                                                                                            | Required | Default Value |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ------------- |
| `expires_after_days` | The number of calendar days before a pending Konbini payment expires. Valid values are from 1 to 60 days. See [Expiration](https://docs.stripe.com/payments/konbini/accept-a-payment.md#checkout-additional-options-expiration). | No       | 3             |

#### Expiration

Pending Konbini payments expire right before midnight (23:59:59 JST) on the specified date. For example if `expires_after_days` is set to 2 and the PaymentIntent is confirmed on Monday, the pending Konbini payment will expire on Wednesday at 23:59:59 Japan (UTC+9) time.

#### Stripe-hosted page

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        currency: "jpy",
        product_data: {
          name: "Tシャツ",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_options: {
    konbini: {
      expires_after_days: 7,
    },
  },
  payment_method_types: ["card", "konbini"],
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
        currency: "jpy",
        product_data: {
          name: "Tシャツ",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_options: {
    konbini: {
      expires_after_days: 7,
    },
  },
  payment_method_types: ["card", "konbini"],
  return_url: "https://example.com/return",
  ui_mode: "embedded_page",
});
```

#### Phone number

On the Konbini checkout form, your customers can optionally supply a phone number to use as their confirmation number. This simplifies their payment process at a convenience store where the in-store UI asks for the customer to provide a payment code and their confirmation number. Both are reflected in the payment instructions that Stripe displays after the customer submits their checkout form. If your customer doesn’t provide a phone number, Stripe generates a random confirmation number.

Stripe proactively blocks phone numbers consisting of only zeros.

### Redirect to Stripe hosted voucher page

> Unlike card payments, the customer won’t be redirected to the [success_url](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-success_url) with Konbini payment.

After submitting the Checkout form successfully, the customer is redirected to the `hosted_voucher_url`. The customer can reference the hosted page’s payment instructions for details on how to complete their payment. The page is viewable on desktop and mobile, as well as being printable.

Stripe sends a [payment_intent.requires_action](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.requires_action) event when a Konbini voucher is created successfully. If you need to email your customers the voucher’s payment instructions link, you can locate the `hosted_voucher_url` in [payment_intent.next_action.konbini_display_details](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-konbini_display_details-hosted_voucher_url). Learn more about how to [monitor a PaymentIntent with webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks).

Stripe allows customization of customer-facing UIs on the [Branding Settings](https://dashboard.stripe.com/account/branding) page. The following brand settings can be applied to the voucher:

- **Icon**—your brand image and public business name
- **Accent color**—used as the color of the Copy Number button
- **Brand color**—used as the background color

### Fulfill your orders

Because Konbini is a delayed notification payment method, you need to use a method such as *webhooks* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) to monitor the payment status and handle order *fulfillment* (Fulfillment is the process of providing the goods or services purchased by a customer, typically after payment is collected). Learn more about [setting up webhooks and fulfilling orders](https://docs.stripe.com/checkout/fulfillment.md).

The following events are sent when the payment status changes:

| Event Name                                                                                                       | Description                                                                                          | Next steps |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------- |
| [checkout.session.completed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.completed) | The customer has successfully submitted the Checkout form. Stripe has generated the Konbini voucher. |

You can choose to email the `hosted_voucher_url` to your customer in case they lose the Konbini voucher. | Wait for the customer to pay at a Konbini. |
| [checkout.session.async_payment_succeeded](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.async_payment_succeeded) | The customer has successfully paid the Konbini voucher. The `PaymentIntent` transitions to `succeeded`. | Fulfill the goods or services that the customer purchased. |
| [checkout.session.async_payment_failed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.async_payment_failed) | The Konbini voucher has expired, or the payment has failed for some other reason. The `PaymentIntent` returns to a status of `requires_payment_method`. | Contact the customer through email and request that they place a new order. |

## Test your integration

When testing your Checkout integration, select Konbini as the payment method and click the **Pay** button.

Provide the following values in the Checkout form to test different scenarios. You can either test with a special confirmation number or an email pattern. If both are provided the behavior of the special confirmation number applies.

| Email                       | Confirmation number | Description                                                                                                               |
| --------------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `{any_prefix}@{any_domain}` | `11111111110`       | Simulates a Konbini payment which succeeds after 3 minutes and the `payment_intent.succeeded` webhook arrives after that. |

Example: hanako@test.com |
| `{any_prefix}succeed_immediately@{any_domain}` | `22222222220` | Simulates a Konbini payment which succeeds immediately and the `payment_intent.succeeded` webhook arrives after that.

Example: succeed_immediately@test.com |
| `{any_prefix}expire_immediately@{any_domain}` | `33333333330` | Simulates a Konbini payment which expires immediately and the `payment_intent.payment_failed` webhook arrives after that.

The `expires_at` field in [next_action.konbini_display_details](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-konbini_display_details-expires_at) is set to the current time regardless of what the `expires_after_days` or `expires_at` parameter in [payment method options](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-konbini-expires_after_days) is set to.

Example: expire_immediately@test.com |
| `{any_prefix}expire_with_delay@{any_domain}` | `44444444440` | Simulates a Konbini payment which never succeeds; it expires in 3 minutes and the `payment_intent.payment_failed` webhook arrives after that.

The `expires_at` field in [next_action.konbini_display_details](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-konbini_display_details-expires_at) is set to 3 minutes in the future regardless of what the `expires_after_days` or `expires_at` parameter in [payment method options](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-konbini-expires_after_days) is set to.

Example: expire_with_delay@test.com |
| `{any_prefix}fill_never@{any_domain}` | `55555555550` | Simulates a Konbini payment which never succeeds; it expires according to the `expires_at` field in `next_action.konbini_display_details` per the provided parameters in the [payment method options](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-konbini-expires_after_days) and the `payment_intent.payment_failed` webhook arrives after that.

Example: fill_never@test.com |

To test [confirmation number](https://docs.stripe.com/payments/konbini/accept-a-payment.md#web-confirm-payment-intent-additional-options-confirmation-number) errors you may use the following values:

- `01234567890` simulates a confirmation number rejection.
- `00000000000` results in a validation error.

## Expiration and cancellation

After the time specified by the `expires_at` value in the [next_action.konbini_display_details](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-konbini_display_details-expires_at), the customer can no longer *initiate* the payment process for a pending Konbini payment at a convenience store kiosk. However, if they issued a valid payment slip before the deadline they might be able to *complete* the payment at the cash register after the `expires_at` time.

There is a buffer period to avoid premature payment failures in such an event. The PaymentIntent’s status changes to `requires_payment_method`. At this point, you can cancel or confirm the PaymentIntent with another payment method.

You can also cancel a pending Konbini payment after confirmation and before the time specified by `next_action.konbini_display_details.expires_at`. Updating the PaymentIntent or confirming it with another payment method will also implicitly cancel the existing Konbini payment.

If the customer is currently paying for the Konbini payment at the convenience store, the cancellation request will fail. Cancellation might be re-attempted if the customer abandons the payment attempt and after the payment slip expires.

Note that [temporary payment method availability issues](https://docs.stripe.com/payments/konbini/accept-a-payment.md#web-handling-temporary-availability-issues) also affect (both explicit as well as implicit) cancellation requests.

> When you cancel a pending payment the original payment instructions become invalid. For most use cases we suggest you reach out to your customer to inform them of the cancellation.
>
> When you successfully reconfirm a PaymentIntent in status `requires_action` we create new instructions and a new `hosted_voucher_url`. You need to ensure that your customer is made aware of these.

## Refunds

It’s possible to refund Konbini payments through the [Dashboard](https://dashboard.stripe.com/payments) or [API](https://docs.stripe.com/api.md#create_refund).

To complete a refund sent to the customer’s bank account directly, your customer must provide the bank account details where they would like to receive the funds. Stripe contacts the customer at the email address from the billing details on the payment method and requests these details from them. After we receive the bank details, we process the refund automatically.

The refund’s status transitions as follows:

| Event                                                                          | Refund status     |
| ------------------------------------------------------------------------------ | ----------------- |
| Refund is created                                                              | `requires_action` |
| Customer submits bank account details, and Stripe begins processing the refund | `pending`         |
| Refund is expected to arrive in customer’s bank                                | `succeeded`       |
| Customer’s bank returns the funds back to Stripe                               | `requires_action` |
| Refund is in `requires_action` 45 days after creation                          | `failed`          |
| Refund is canceled from a `requires_action` state                              | `canceled`        |

If the customer’s bank can’t successfully complete the transfer, the funds are returned to Stripe and the refund transitions to `requires_action`. This can happen if the account holder’s name doesn’t match what the recipient bank has on file or if the provided bank account number has a typo. In these cases, Stripe emails the customer to inform them of the failure and to request that they resubmit their bank account details.

If your customer doesn’t provide their bank account details within 45 days, the refund’s status transitions to `failed` and we send the [refund.failed](https://docs.stripe.com/api/events/types.md#event_types-refund.failed) event. This means that Stripe can’t process the refund, and you must [return the funds to your customer outside of Stripe](https://docs.stripe.com/refunds.md#failed-refunds).

The [instructions_email](https://docs.stripe.com/api/refunds/object.md#refund_object-instructions_email) field on the refund is the email that the refund was sent to. While a refund is waiting for a response from the customer, details of the email sent to the customer can also be found under the [next_action.display_details.email_sent](https://docs.stripe.com/api/refunds/object.md#refund_object-next_action-display_details-email_sent) field on the refund.

Each individual refund (including each partial refund) might incur a fee. Contact your point of contact at Stripe to learn more about this.

### Testing Refunds

You can test refund behavior in testmode using the following test bank accounts on the bank account details collection page linked in the email sent to the customer. Bank account details outside of these test bank accounts won’t be accepted.

| Routing   | Account   | Type             |
| --------- | --------- | ---------------- |
| `1100000` | `0001234` | Refund succeeds. |
| `1100000` | `1111113` |

`1111116`

`1111113`

`3333335`

`4444440` | Refund fails. |

#### Testing Refunds Expiry

You can make an API call to simulate the expiry of a testmode refund.

```bash
curl https://api.stripe.com/v1/test_helpers/refunds/{{REFUND_ID}}/expire \
  -X POST \
  -u <<YOUR_SECRET_KEY>>:
```

## See also

- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment.md)
- [Customizing Checkout](https://docs.stripe.com/payments/checkout/customization.md)

# Direct API

> This is a Direct API for when payment-ui is direct-api. View the full page at https://docs.stripe.com/payments/konbini/accept-a-payment?payment-ui=direct-api.

Stripe users in Japan can accept Konbini payments from customers in Japan by using the Payment Intents and Payment Methods APIs. Customers pay by providing a payment code, confirmation number, and cash payment at Japanese convenience stores. Stripe notifies you when the payment is completed.

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/test/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create a PaymentIntent [Server-side]

Stripe uses a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) object to represent your intent to collect payment from a customer, tracking state changes from Konbini PaymentIntent creation to completion.

Create a PaymentIntent on your server with an amount and the `jpy` currency (Konbini doesn’t support other currencies). If you already have an integration using the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md), add `konbini` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your PaymentIntent.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "jpy",
  payment_method_types: ["konbini"],
  payment_method_options: {
    konbini: {
      product_description: "Tシャツ",
      expires_after_days: 3,
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

### Additional payment method options

Payment method options can be specified in the [payment method options](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-konbini) under the `konbini` key.

| Field                 | Value                                                                                                                                                                                                                                                                                                                                                                                                                  | Required | Default Value |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ------------- |
| `expires_after_days`  | The number of calendar days before a pending Konbini payment expires. Valid values are from 1 to 60 days. See [Expiration](https://docs.stripe.com/payments/konbini/accept-a-payment.md#web-additional-options-expiration).                                                                                                                                                                                            | No       | 3             |
| `expires_at`          | A Unix timestamp at which the pending Konbini payment will expire. This expiry date must be more than 30 minutes from the current time and less than 60 days after the setting is applied to the PaymentIntent. See [Expiration](https://docs.stripe.com/payments/konbini/accept-a-payment.md#web-additional-options-expiration).                                                                                      | No       | *unset*       |
| `product_description` | A product descriptor of up to 22 characters, which will appear to customers at the convenience store. Presence of non-Shift JIS ([JIS X 0208:1997](https://en.wikipedia.org/wiki/Shift_JIS)) characters will cause an error to be returned. While not required, we recommend setting this option. Otherwise we fall back to a generic placeholder chosen at our own discretion, for example, お買い上げ商品・サービス. | No       | *placeholder* |

#### Expiration

Pending Konbini payments expire right before midnight (23:59:59 JST) on the specified date. For example if `expires_after_days` is set to 2 and the PaymentIntent is confirmed on Monday, the pending Konbini payment will expire on Wednesday at 23:59:59 Japan (UTC+9) time.

The `expires_at` setting is a Unix timestamp in seconds. If the value is less than 30 minutes from the current time, or the PaymentIntent confirmation happens less than 30 minutes from the expiration time, an error will be returned.

`expires_after_days` and `expires_at` are mutually exclusive. An error will be returned if both are set. Both are also optional, and if neither are set, the expiration time defaults to 3 days after PaymentIntent creation at 23:59 Japan (UTC+9) time.

### Error handling

Requests on PaymentIntents such as creation, updates, and confirmation might fail. You can inspect the `error` value of the API response to determine the reason and in many cases either resubmit the request or correct the error. In particular, if you provide a value for the `confirmation_number` payment method option, you might want to handle specific error codes we return. See [Confirmation numbers](https://docs.stripe.com/payments/konbini/accept-a-payment.md#confirm-payment-intent-additional-options-confirmation-number) for more details.

The payment method might at times become temporarily unavailable due to outages, scheduled maintenance, or your usage patterns. See [Handling temporary availability issues](https://docs.stripe.com/payments/konbini/accept-a-payment.md#web-handling-temporary-availability-issues) for more details.

## Collect payment method details [Client-side]

Create a payment form on your client to collect the required billing details from the customer:

| Field   | Value                                                                                                                                                                                                                            |
| ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`  | The full name of the customer, truncated to a maximum of 20 characters in convenience store UIs and receipts. Non-Shift JIS ([JIS X 0208:1997](https://en.wikipedia.org/wiki/Shift_JIS)) characters will be dropped or replaced. |
| `email` | The full email address of the customer.                                                                                                                                                                                          |

The form example here also collects a phone number, to be used as a customer-provided confirmation number:

```html
<form id="payment-form">
  <div class="form-row">
    <label for="name"> Name </label>
    <input id="name" name="name" required />
  </div>

  <div class="form-row">
    <label for="email"> Email </label>
    <input id="email" name="email" required />
  </div>

  <div class="form-row">
    <label for="phone"> Phone Number </label>
    <input id="phone" name="phone" required />
  </div>

  <!-- Used to display form errors. -->
  <div id="error-message" role="alert"></div>

  <button id="submit-button">Pay with Konbini</button>
</form>
```

## Submit the payment to Stripe [Client-side]

When a customer clicks to pay with Konbini, use Stripe.js to submit the payment to Stripe. [Stripe.js](https://docs.stripe.com/payments/elements.md) is our foundational JavaScript library for building payment flows.

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

Use [stripe.confirmKonbiniPayment](https://docs.stripe.com/js/payment_intents/confirm_konbini_payment) and the [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) of the PaymentIntent object that you created in [Step 2](https://docs.stripe.com/payments/konbini/accept-a-payment.md#web-create-payment-intent) to submit the customer’s billing details.

Upon confirmation, Stripe will automatically open a modal to display the Konbini payment instructions to your customer.

```javascript
const form = document.getElementById("payment-form");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const result = await stripe.confirmKonbiniPayment(
    "{{PAYMENT_INTENT_CLIENT_SECRET}}",
    {
      payment_method: {
        billing_details: {
          name: document.getElementById("name").value,
          email: document.getElementById("email").value,
        },
      },
      payment_method_options: {
        konbini: {
          confirmation_number: document
            .getElementById("phone")
            .value.replace(/\D/g, ""),
        },
      },
    },
  );
  // Stripe.js will open a modal to display the Konbini payment instructions to your customer
  // This async function finishes when the customer closes the modal

  if (result.error) {
    // Display error to your customer
    const errorMsg = document.getElementById("error-message");
    errorMsg.innerText = result.error.message;
  }
});
```

> `stripe.confirmKonbiniPayment` might take several seconds to complete. During that time, disable your form from being resubmitted and show a waiting indicator like a spinner. If you receive an error, show it to the customer, re-enable the form, and hide the waiting indicator.

### Additional payment method options

When confirming a Konbini PaymentIntent, you can specify additional payment method options in the [payment method options](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-payment_method_options-konbini), under the `konbini` key.

| Field                 | Value                                                                                                                                                                                                                                                                                                                                                                                                 | Required | Default value |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ------------- |
| `confirmation_number` | A 10 to 11-digit numeric string. This string is also shown in the payment instructions and can’t consist of only zeroes. If you don’t provide a value for `confirmation_number`, Stripe randomly generates one for you. For more information, see [Confirmation numbers](https://docs.stripe.com/payments/konbini/accept-a-payment.md#confirm-payment-intent-additional-options-confirmation-number). | No       | *unset*       |

#### Confirmation numbers

Your customers will need to refer to the `confirmation_number` when completing their payment. A common suggestion for this value, if you choose to set it or allow your customers to set it, is the customer’s phone number. A `confirmation_number` may also be set during server-side PaymentIntent creation, but more commonly would be set client-side by the customer during PaymentIntent confirmation. It may be updated from the value set during PaymentIntent creation all the way until confirmation.

If a specified `confirmation_number` is too common among all ongoing convenience store transactions it may be rejected at the time of PaymentIntent confirmation. The error code returned in this case would be `payment_intent_konbini_rejected_confirmation_number`, which would only be expected when confirming a PaymentIntent.

Stripe proactively blocks confirmation numbers consisting of only zeros at PaymentIntent creation as well as during update and confirmation. Please ensure on your end that you don’t set this value or allow customers to set it.

### Error handling

Confirming a PaymentIntent client side might also fail. You should inspect the `error` return value to determine why and possibly show the error to the customer or correct the error and try again.

## Optional: Display your own Konbini payment instructions to your customer [Client-side]

We recommend relying on Stripe.js to handle displaying the Konbini payment instructions with `confirmKonbiniPayment`. However, you can also manually display your own payment instructions to your customers.

To manually handle the next action of displaying the Konbini details to your customer, use `handleActions: false` when calling `stripe.confirmKonbiniPayment` in [Step 4](https://docs.stripe.com/payments/konbini/accept-a-payment.md#web-submit-payment).

```javascript
const form = document.getElementById("payment-form");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const result = await stripe.confirmKonbiniPayment(
    "{{PAYMENT_INTENT_CLIENT_SECRET}}",
    {
      payment_method: {
        billing_details: {
          name: document.getElementById("name").value,
          email: document.getElementById("email").value,
        },
      },
      payment_method_options: {
        konbini: {
          confirmation_number: document
            .getElementById("phone")
            .value.replace(/\D/g, ""),
        },
      },
    },
    { handleActions: false },
  );
  // This async function finishes when the PaymentIntent is confirmed

  if (result.error) {
    // Display error to your customer
    var errorMsg = document.getElementById("error-message");
    errorMsg.innerText = result.error.message;
  } else {
    // A Konbini PaymentIntent was successfully created
    var amount = result.paymentIntent.amount;
    var currency = result.paymentIntent.currency;

    var details = result.paymentIntent.next_action.konbini_display_details;
    for (var store in details.stores) {
      // Do something with each store's details
    }
    var expires_at = details.expires_at;
    // Display Konbini details to end customer
  }
});
```

### Presentation

You specify how to present payment instructions to the customer. At minimum, your instructions must contain the following:

- General information relevant to the purchase, such as the product description, amount, and payment expiration date.
- Payment and confirmation codes for each convenience store chain obtained through the PaymentIntent confirmation.
- Instructions to the customer on how to complete the Konbini payment. Example payment instructions are as follows:

### Konbini payment instructions

1. Locate the payment code and confirmation number for the convenience store chain where you plan to pay.
1. At the convenience store, provide the payment code and confirmation number to the payment machine or cashier.
1. After the payment is complete, keep the receipt for your records.
1. Contact us if you have any questions.

## Optional: Submit the payment to Stripe from your server [Server-side]

We recommend relying on Stripe.js to handle Konbini payments client-side with [stripe.confirmKonbiniPayment](https://docs.stripe.com/js/payment_intents/confirm_konbini_payment). Using Stripe.js helps extend your integration to other payment methods. However, you can also manually redirect your customers on your server by following these steps:

- Set `confirm` to `true` when creating your [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) of type `konbini`, or [confirm](https://docs.stripe.com/api/payment_intents/confirm.md) an existing PaymentIntent. You must provide the `payment_method_data.billing_details.name` and `payment_method_data.billing_details.email` properties. You can also optionally set `payment_method_options.konbini.confirmation_number` or other [payment_method_options](https://docs.stripe.com/payments/konbini/accept-a-payment.md#web-additional-options). By specifying `payment_method_data`, we’ll create a *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) and immediately use it with this PaymentIntent.

  ```node
  // Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
  // Find your keys at https://dashboard.stripe.com/apikeys.
  const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

  const paymentIntent = await stripe.paymentIntents.create({
    amount: 1099,
    currency: "jpy",
    confirm: true,
    payment_method_types: ["konbini"],
    payment_method_data: {
      type: "konbini",
      billing_details: {
        name: "Jenny Rosen",
        email: "jenny@example.com",
      },
    },
  });
  ```

  The created `PaymentIntent` has a status of `requires_action` and the type for `next_action` is `konbini_display_details`.

  #### Json

  ```json
  {"status": "requires_action",
    "next_action": {
      "type": "konbini_display_details",
      "konbini_display_details": {
        "expires_at": 1642431599,
        "hosted_voucher_url": "https://payments.stripe.com/konbini/voucher/...",
        "stores": {
          "familymart": {
              "confirmation_number": "12345678901",
              "payment_code": "123456"
          },
          ...
        }
      }
    },
    "id": "pi_1G1sgdKi6xqXeNtkldRRE6HT",
    "object": "payment_intent",
    "amount": 1099,
    "client_secret": "pi_1G1sgdKi6xqXeNtkldRRE6HT_secret_h9B56ObhTN72fQiBAuzcVPb2E",
    "confirmation_method": "automatic",
    "created": 1642126547,
    "currency": "jpy",
    "livemode": true,
    "charges": {
      "data": [],
      "object": "list",
      "has_more": false,
      "url": "/v1/charges?payment_intent=pi_1G1sgdKi6xqXeNtkldRRE6HT"
    },
    "payment_method_options": {
      "konbini": {
        "confirmation_number": null,
        "expires_after_days": null,
        "expires_at": null,
        "product_description": null
      }
    },
    "payment_method_types": [
      "konbini"
    ]
  }
  ```

- Redirect the customer to the URL provided in the `next_action.konbini_display_details.hosted_voucher_url` property. The code example here is approximate. The redirect method might be different in your web framework.

  #### Node.js

  ```javascript
  if (
    paymentIntent.status === "requires_action" &&
    paymentIntent.next_action.type === "konbini_display_details"
  ) {
    const url =
      paymentIntent.next_action.konbini_display_details.hosted_voucher_url;
    res.redirect(url);
  }
  ```

We recommend that you [rely on webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks) to confirm the status of a payment.

## Optional: Customize payment instructions

You can customize what your customers see by using the [Branding Settings](https://dashboard.stripe.com/account/branding) page. If a [customer](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-customer) is linked to the PaymentIntent, the hosted payment instructions use the customer’s preferred language. If not, the customer’s browser language is used.

You can apply the following brand settings to the hosted payment instructions:

- **Icon**—Your brand image and public business name
- **Logo**—Your brand image
- **Accent color**—The color of the Print button
- **Brand color**—The background color

## Optional: Send payment instruction emails

You can enable Konbini payment instruction and reminder emails on the [Email Settings](https://dashboard.stripe.com/settings/emails) page in the Dashboard. After enabling instruction emails, Stripe sends payment instruction emails upon PaymentIntent confirmation. These emails contain the payment code, confirmation number, and other details to make a payment at a convenience store. This includes a link to the hosted payment instructions page.

## Optional: Send reminder emails

You can enable payment reminder emails and configure the maximum amount of reminder emails per PaymentIntent on the [Email Settings](https://dashboard.stripe.com/settings/emails) page in the Dashboard. Stripe sends at most one reminder email per day until a payment succeeds, expires, or is canceled.

> In testing environments, instruction and reminder emails are only sent to email addresses linked to the Stripe account.

## Handle post-payment events [Server-side]

Konbini is a [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method, so funds aren’t immediately available. Customers might not pay for the pending Konbini payment at a convenience store immediately after checking out.

After a pending Konbini Payment completes, Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event for it. Use the Dashboard or build a *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) handler to receive these events and run actions. Examples of actions include sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

When it’s clear that a pending Konbini payment didn’t complete, typically about an hour after its expiration deadline, Stripe sends a [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) event.

| Event                            | Description                                                            | Next steps                                                                                                        |
| -------------------------------- | ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `payment_intent.requires_action` | The pending Konbini payment is created.                                | Optionally, send the customer to the payment instructions page. Wait for the customer to pay the Konbini payment. |
| `payment_intent.succeeded`       | The customer paid for the pending Konbini payment before expiration.   | Fulfill the goods or services that the customer purchased.                                                        |
| `payment_intent.payment_failed`  | The customer didn’t pay the pending Konbini payment before expiration. | Contact the customer using email or push notification to request another payment method.                          |

> While testing, the status of a Konbini PaymentIntent might automatically change based on the parameters sent, such as `email`. You can confirm any updates on the [Dashboard](https://dashboard.stripe.com/test/payments). See [Test the integration](https://docs.stripe.com/payments/konbini/accept-a-payment.md#web-test-integration) for more details.

### Receive events and run business actions

#### Manually

Use the Stripe Dashboard to view all your Stripe payments, send email receipts, handle payouts, or retry failed payments.

- [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments)

#### Custom Code

Build a webhook handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook)

## Test the integration

While testing, set `payment_method.billing_details.email` to the following values when you call [stripe.confirmKonbiniPayment](https://docs.stripe.com/js/payment_intents/confirm_konbini_payment) to test different scenarios. You can either test with a special confirmation number or an email pattern. If both are provided, the behavior of the special confirmation number applies.

| Email                       | Confirmation number | Description                                                                                                               |
| --------------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `{any_prefix}@{any_domain}` | `11111111110`       | Simulates a Konbini payment which succeeds after 3 minutes and the `payment_intent.succeeded` webhook arrives after that. |

Example: hanako@test.com |
| `{any_prefix}succeed_immediately@{any_domain}` | `22222222220` | Simulates a Konbini payment which succeeds immediately and the `payment_intent.succeeded` webhook arrives after that.

Example: succeed_immediately@test.com |
| `{any_prefix}expire_immediately@{any_domain}` | `33333333330` | Simulates a Konbini payment which expires immediately and the `payment_intent.payment_failed` webhook arrives after that.

The `expires_at` field in [next_action.konbini_display_details](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-konbini_display_details-expires_at) is set to the current time regardless of what the `expires_after_days` or `expires_at` parameter in [payment method options](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-konbini-expires_after_days) is set to.

Example: expire_immediately@test.com |
| `{any_prefix}expire_with_delay@{any_domain}` | `44444444440` | Simulates a Konbini payment which never succeeds; it expires in 3 minutes and the `payment_intent.payment_failed` webhook arrives after that.

The `expires_at` field in [next_action.konbini_display_details](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-konbini_display_details-expires_at) is set to 3 minutes in the future regardless of what the `expires_after_days` or `expires_at` parameter in [payment method options](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-konbini-expires_after_days) is set to.

Example: expire_with_delay@test.com |
| `{any_prefix}fill_never@{any_domain}` | `55555555550` | Simulates a Konbini payment which never succeeds; it expires according to the `expires_at` field in `next_action.konbini_display_details` per the provided parameters in the [payment method options](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-konbini-expires_after_days) and the `payment_intent.payment_failed` webhook arrives after that.

Example: fill_never@test.com |

To test [confirmation number](https://docs.stripe.com/payments/konbini/accept-a-payment.md#web-confirm-payment-intent-additional-options-confirmation-number) error handling, you can use the following values for `payment_method_options[confirmation_number]`:

- `01234567890` yields a `payment_intent_konbini_rejected_confirmation_number` error code.
- `00000000000` yields a generic validation error code. You should avoid this error in your integration using pre-validation.

## Expiration and cancellation

After the time specified by the `expires_at` value in the [next_action.konbini_display_details](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-konbini_display_details-expires_at), the customer can no longer *initiate* the payment process for a pending Konbini payment at a convenience store kiosk. However, if they issued a valid payment slip before the deadline they might be able to *complete* the payment at the cash register after the `expires_at` time.

There is a buffer period to avoid premature payment failures in such an event. The PaymentIntent’s status changes to `requires_payment_method`. At this point, you can cancel or confirm the PaymentIntent with another payment method.

You can also cancel a pending Konbini payment after confirmation and before the time specified by `next_action.konbini_display_details.expires_at`. Updating the PaymentIntent or confirming it with another payment method will also implicitly cancel the existing Konbini payment.

If the customer is currently paying for the Konbini payment at the convenience store, the cancellation request will fail. Cancellation might be re-attempted if the customer abandons the payment attempt and after the payment slip expires.

Note that [temporary payment method availability issues](https://docs.stripe.com/payments/konbini/accept-a-payment.md#web-handling-temporary-availability-issues) also affect (both explicit as well as implicit) cancellation requests.

> When you cancel a pending payment the original payment instructions become invalid. For most use cases we suggest you reach out to your customer to inform them of the cancellation.
>
> When you successfully reconfirm a PaymentIntent in status `requires_action` we create new instructions and a new `hosted_voucher_url`. You need to ensure that your customer is made aware of these.

## Handle temporary availability issues

The following error codes indicate temporary issues with the availability of the payment method:

| Code                                 | Description                                                                                                                                                                      | Handling                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_method_rate_limit_exceeded` | Too many requests are being made in quick succession for this payment method, which has stricter limits than our [API-wide rate limits](https://docs.stripe.com/rate-limits.md). | Retrying with backoff generally resolves the situation. However, in case of sustained heavy usage of the payment method (for example, during an ongoing sale on your website) these errors may persist for some amount of requests. In that case, asking your customers to consider choosing a different payment method may be an additional mitigation option. |
| `payment_method_not_available`       | The payment method is experiencing unknown temporary issues that may potentially last for a while (for example, during outages or periods of scheduled maintenance).             | It’s best to invite your users to complete their purchase with a different payment method or try again at a later time.                                                                                                                                                                                                                                         |

> If you anticipate heavy usage in general or for an upcoming event, contact us ahead of time.

## Refunds

It’s possible to refund Konbini payments through the [Dashboard](https://dashboard.stripe.com/payments) or [API](https://docs.stripe.com/api.md#create_refund).

To complete a refund sent to the customer’s bank account directly, your customer must provide the bank account details where they would like to receive the funds. Stripe contacts the customer at the email address from the billing details on the payment method and requests these details from them. After we receive the bank details, we process the refund automatically.

The refund’s status transitions as follows:

| Event                                                                          | Refund status     |
| ------------------------------------------------------------------------------ | ----------------- |
| Refund is created                                                              | `requires_action` |
| Customer submits bank account details, and Stripe begins processing the refund | `pending`         |
| Refund is expected to arrive in customer’s bank                                | `succeeded`       |
| Customer’s bank returns the funds back to Stripe                               | `requires_action` |
| Refund is in `requires_action` 45 days after creation                          | `failed`          |
| Refund is canceled from a `requires_action` state                              | `canceled`        |

If the customer’s bank can’t successfully complete the transfer, the funds are returned to Stripe and the refund transitions to `requires_action`. This can happen if the account holder’s name doesn’t match what the recipient bank has on file or if the provided bank account number has a typo. In these cases, Stripe emails the customer to inform them of the failure and to request that they resubmit their bank account details.

If your customer doesn’t provide their bank account details within 45 days, the refund’s status transitions to `failed` and we send the [refund.failed](https://docs.stripe.com/api/events/types.md#event_types-refund.failed) event. This means that Stripe can’t process the refund, and you must [return the funds to your customer outside of Stripe](https://docs.stripe.com/refunds.md#failed-refunds).

The [instructions_email](https://docs.stripe.com/api/refunds/object.md#refund_object-instructions_email) field on the refund is the email that the refund was sent to. While a refund is waiting for a response from the customer, details of the email sent to the customer can also be found under the [next_action.display_details.email_sent](https://docs.stripe.com/api/refunds/object.md#refund_object-next_action-display_details-email_sent) field on the refund.

Each individual refund (including each partial refund) might incur a fee. Contact your point of contact at Stripe to learn more about this.

### Testing Refunds

You can test refund behavior in testmode using the following test bank accounts on the bank account details collection page linked in the email sent to the customer. Bank account details outside of these test bank accounts won’t be accepted.

| Routing   | Account   | Type             |
| --------- | --------- | ---------------- |
| `1100000` | `0001234` | Refund succeeds. |
| `1100000` | `1111113` |

`1111116`

`1111113`

`3333335`

`4444440` | Refund fails. |

#### Testing Refunds Expiry

You can make an API call to simulate the expiry of a testmode refund.

```bash
curl https://api.stripe.com/v1/test_helpers/refunds/{{REFUND_ID}}/expire \
  -X POST \
  -u <<YOUR_SECRET_KEY>>:
```
