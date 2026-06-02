<!-- Source URL: https://docs.stripe.com/payments/multicapture -->
<!-- Fetched: 2026-05-11 -->

# Capture a payment multiple times

Capture a PaymentIntent multiple times, up to the authorized amount.

# Stripe-hosted page

> This is a Stripe-hosted page for when platform is web and ui is stripe-hosted. View the full page at https://docs.stripe.com/payments/multicapture?platform=web&ui=stripe-hosted.

Multicapture allows you to [capture a PaymentIntent](https://docs.stripe.com/api/payment_intents/capture.md) created during the confirmation step of a [CheckoutSession](https://docs.stripe.com/api/checkout_sessions.md) multiple times for a single transaction, up to the full [amount of the PaymentIntent](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-amount). You can use it when you have orders with multiple shipments, and want to capture funds as you fulfill parts of the order.

> #### IC+ feature
>
> Multicapture is part of the functionality we offer to users on _IC+ pricing_ (A pricing plan where businesses pay the variable network cost for each transaction plus the Stripe fee rather than a flat rate for all transactions. This pricing model provides more visibility into payments costs). If you’re on blended Stripe pricing and want access to this feature, contact us using the form at [Stripe support](https://support.stripe.com).

## Availability

When using multicapture, be aware of the following restrictions:

- It only supports online card payments
- Use [capture_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-capture_method) set to `manual`. Multicapture requires manual capture so that you can perform multiple partial captures on the PaymentIntent.
- It’s available with Amex, Visa, Discover, Mastercard, Cartes Bancaires, Diners Club, China UnionPay (CUP), and Japan Credit Bureau (JCB)
- [Separate charges and transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md) fund flows using [source_transaction](https://docs.stripe.com/api/transfers/create.md#create_transfer-source_transaction) aren’t supported
- Stripe allows you to capture up to 50 times for a single [PaymentIntent](https://docs.stripe.com/api/payment_intents.md)
- [mode](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-mode) is set to `payment` and [capture_method](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_intent_data-capture_method) is set to `manual` on the [CheckoutSession](https://docs.stripe.com/api/checkout/sessions/.md)

> #### CUP and JCB support
>
> CUP multicapture is only available in the United States. JCB multicapture is only available in the United States, Canada, Australia, and New Zealand.

> #### Automatic capture methods
>
> The API currently accepts `request_multicapture="if_available"` when `capture_method` is set to `automatic` or `automatic_async` without returning an error. In this case, `multicapture.status` on the charge may show `available`, but you can’t perform multiple captures because the PaymentIntent is automatically captured in full. Always set `capture_method` to `manual` when you intend to use multicapture. A future API version may return a validation error for this combination.

## Best practices

When sending separate shipments for one order, proactively notify your end customer with the details of each shipment. Doing so avoids inquiries and chargebacks from customers because of confusion with seeing multiple transactions on their bank statement. Use the following best practices when notifying customers:

- Inform them of the estimated delivery date and transaction amount for each shipment at the time of checkout, before purchase.
- Notify them upon each shipment, along with the transaction amount.
- Disclose your full refund and cancellation policy.

You can use the [custom_text](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-custom_text) field when creating a new [CheckoutSession](https://docs.stripe.com/api/checkout_sessions.md) to display additional text on the checkout page to help meet compliance requirements.

> #### Compliance
>
> You’re responsible for your compliance with all applicable laws, regulations, and network rules when using multicapture. Consult the rules for the card networks that you want to use this feature with to make sure your sales comply with all applicable rules, which vary by network. For example, most card networks restrict multicapture usage to card-not-present transactions for the sale of goods that ship separately. Certain card networks permit multicapture for businesses based on their industry (for example, travel), while some don’t permit multicapture for installment or deposit workflows.
>
> The information provided on this page relating to your compliance with these requirements is for your general guidance, and isn’t legal, tax, accounting, or other professional advice. Consult with a professional if you’re unsure about your obligations.

## Create a Checkout Session

Add a checkout button to your website that calls a server-side endpoint to create a [Checkout Session](https://docs.stripe.com/api/checkout/sessions/create.md).

```html
<html>
  <head>
    <title>Buy cool new product</title>
  </head>
  <body>
    <!-- Use action="/create-checkout-session.php" if your server is PHP based. -->
    <form action="/create-checkout-session" method="POST">
      <button type="submit">Checkout</button>
    </form>
  </body>
</html>
r
```

A Checkout Session is the programmatic representation of what your customer sees when they’re redirected to the payment form. You can configure it with options such as:

- [Line items](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items) to charge
- Currencies to use

You must populate `success_url` with the URL value of a page on your website that Checkout returns your customer to after they complete the payment.

> Checkout Sessions expire 24 hours after creation by default.

After creating a Checkout Session, redirect your customer to the [URL](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-url) returned in the response.

Lastly, set [request_multicapture](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_method_options-card-request_multicapture) as `if_available` to enable the multicapture feature.

#### Node.js

```javascript
// This example sets up an endpoint using the Express framework.

const express = require("express");
const app = express();
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

app.post("/create-checkout-session", async (req, res) => {
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
    payment_intent_data: {
      capture_method: "manual",
    },
    payment_method_options: {
      card: {
        request_multicapture: "if_available",
      },
    },
    mode: "payment",
    success_url: "http://localhost:4242/success",
  });

  res.redirect(303, session.url);
});

app.listen(4242, () => console.log(`Listening on port ${4242}!`));
```

### Payment methods

By default, Stripe enables cards and other common payment methods. You can turn individual payment methods on or off in the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods). In Checkout, Stripe evaluates the currency and any restrictions, then dynamically presents the supported payment methods to the customer.

To see how your payment methods appear to customers, enter a transaction ID or set an order amount and currency in the Dashboard.

You can enable Apple Pay and Google Pay in your [payment methods settings](https://dashboard.stripe.com/settings/payment_methods). By default, Apple Pay is enabled and Google Pay is disabled. However, in some cases Stripe filters them out even when they’re enabled. We filter Google Pay if you [enable automatic tax](https://docs.stripe.com/tax/checkout.md) without collecting a shipping address.

Checkout’s Stripe-hosted pages don’t need integration changes to enable Apple Pay or Google Pay. Stripe handles these payments the same way as other card payments.

## Capture the PaymentIntent

For a PaymentIntent in a [requires_capture state](https://docs.stripe.com/payments/paymentintents/lifecycle.md) where multicapture is `available`, specifying the optional `final_capture` parameter to be `false` tells Stripe not to release the remaining uncaptured funds when calling the capture API. For example, if you confirm a 10 USD payment intent, capturing 7 USD with `final_capture=false` keeps the remaining 3 USD authorized.

```curl
curl https://api.stripe.com/v1/payment_intents/pi_xxx/capture \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount_to_capture=700 \
  -d final_capture=false \
  -d "expand[]=latest_charge"
```

In the PI capture response, the [amount_capturable](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-amount_capturable) and [amount_received](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-amount_received) fields update accordingly.

```json
// PaymentIntent Response
{
  "id": "pi_ANipwO3zNfjeWODtRPIg",
  "object": "payment_intent","amount": 1000,
  "amount_capturable": 300, // 1000 - 700 = 300
  "amount_received": 700,
  // if latest_charge is expanded
  "latest_charge": {
      "id": "ch_xxx",
      "object": "charge","amount": 1000,
      "amount_captured": 700,
      "amount_refunded": 0,
      ...
    }
  ...
}
```

## Final capture

The PaymentIntent remains in a `requires_capture` state until you do one of the following:

- Set `final_capture` to `true`.
- Make a capture without the `final_capture` parameter (because `final_capture` defaults to `true`).
- The authorization window expires.

At this point, Stripe releases any remaining funds and transitions the PaymentIntent to a `succeeded` state.

```curl
curl https://api.stripe.com/v1/payment_intents/pi_xxx/capture \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount_to_capture=200 \
  -d final_capture=true \
  -d "expand[]=latest_charge"
```

In the PI capture response, the [amount_capturable](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-amount_capturable) and [amount_received](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-amount_received) fields will be updated accordingly.

```json
// PaymentIntent Response
{
  "id": "pi_ANipwO3zNfjeWODtRPIg",
  "object": "payment_intent","amount": 1000,
  "amount_capturable": 0, // not 100 due to final_capture=true
  "amount_received": 900, // 700 + 200 = 900
  // if latest_charge is expanded
  "latest_charge": {
      "id": "ch_xxx",
      "object": "charge","amount": 1000,
      "amount_captured": 900,
      "amount_refunded": 0,
      ...
    }
  ...
}
```

Uncaptured PaymentIntents transition to `canceled`, while partially captured PaymentIntents transition to `succeeded`.

## Optional: Release uncaptured funds

If you want to release the uncaptured funds for a partially captured payment, set the amount to 0 and set `final_capture` to `true`.

```curl
curl https://api.stripe.com/v1/payment_intents/pi_xxx/capture \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount_to_capture=0 \
  -d final_capture=true
```

This transitions the PaymentIntent to `succeeded` and releases any uncaptured funds back to the cardholder.

## Test your integration

Use a Stripe test card with any CVC, postal code, and future expiration date to test multicapture payments.

| Number           | Payment Method                                 | Description                                                    |
| ---------------- | ---------------------------------------------- | -------------------------------------------------------------- |
| 4242424242424242 | `pm_card_visa`                                 | Visa test card that supports multicapture.                     |
| 4000002500001001 | `pm_card_visa_cartesBancaires`                 | Cartes Bancaires or Visa test card that supports multicapture. |
| 4000008400000076 | `pm_card_credit_disableEnterpriseCardFeatures` | Visa test card that doesn’t support multicapture.              |

## Refunds

For a PaymentIntent in `requires_capture` state, you can [refund](https://docs.stripe.com/api/refunds.md) any number of times up to the total captured amount minus the total refunded amount, which is the [amount_received](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-amount_received)—[amount_refunded](https://docs.stripe.com/api/charges/object.md#charge_object-amount_refunded). The [charge.refunded](https://docs.stripe.com/api/charges/object.md#charge_object-refunded) field transitions to `true` only when the final capture has been performed and the entire [amount_received](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-amount_received) is refunded.

Stripe doesn’t support _partial refunds_ (A partial refund is any refund in which less than the remaining refundable amount is refunded in a single request. The remaining refundable amount is the payment_intent.amount_received - charge.amount_refunded) with [refund_application_fee=true](https://docs.stripe.com/api/refunds/create.md#create_refund-refund_application_fee) or [reverse_transfer=true](https://docs.stripe.com/api/refunds/create.md#create_refund-reverse_transfer). Instead, you can perform partial fee refunds by manually performing partial fee refunds and transfer reversals using the [application fee refund](https://docs.stripe.com/api/fee_refunds.md) and [transfer reversal](https://docs.stripe.com/api/transfer_reversals.md) endpoints. After using the application fee refund or transfer reversal endpoints, Stripe doesn’t support any further refunds with `refund_application_fee=true` or `reverse_transfer=true` respectively.

## Connect

Multicapture supports all Connect use cases, with the exception of [Separate Charges and Transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md) with the [source_transaction](https://docs.stripe.com/api/transfers/create.md#create_transfer-source_transaction) parameter. The [application_fee_amount](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-application_fee_amount) and [transfer_data[amount]](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-transfer_data-amount) parameters have some additional validations. Consider the following validations when implementing multicapture with Connect:

- Setting `application_fee_amount` or `transfer_data[amount]` on the first capture makes it required for all subsequent captures. Each `application_fee_amount` and `transfer_data[amount]` passed at capture time overrides the values passed in on PaymentIntent creation, confirmation, and update.
- Stripe doesn’t support _partial refunds_ (A partial refund is any refund in which less than the remaining refundable amount is refunded in a single request. The remaining refundable amount is the payment_intent.amount_received - charge.amount_refunded) on multicapture payments with refund_application_fee=true or reverse_transfer=true. You can perform partial fee refunds or transfer reversals using the [application fee refund](https://docs.stripe.com/api/fee_refunds.md) and [transfer reversal](https://docs.stripe.com/api/transfer_reversals.md) endpoints.

## Webhooks

### Charge updated webhooks

We send a [charge.updated](https://docs.stripe.com/api/events/types.md#event_types-charge.updated) webhook each time you capture a payment.

For example, on the first capture of a destination charge multicapture payment with an `application_fee_amount`, we update these fields from empty to non-empty values.

```json
// charge.updated
{
  "data": {
    "id": "ch_xxx",
    "object": "charge",
    "amount": 1000,"balance_transaction": "txn_xxx", // applicable to all charges
    "transfer": "tr_xxx",             // applicable to destination charges only
    "application_fee": "fee_xxx",     // applicable to Connect only
    ...
  },
  "previous_attributes": {"balance_transaction": null, // applicable to all charges
    "transfer": null,            // applicable to destination charges only
    "application_fee": null,     // applicable to Connect only
  }
}
```

### payment_intent.amount_capturable_updated

We send [payment_intent.amount_capturable_updated](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.amount_capturable_updated) on every capture, regardless of `amount_to_capture` and `final_capture` values.

For example, if we capture 1 USD from a PaymentIntent with an amount of 10 USD, the PaymentIntent’s amount_capturable field updates to 9 USD.

```json
// payment_intent.amount_capturable_updated
{
  "data": {
    "id": "pi_xxx",
    "object": "payment_intent",
    "amount": 1000,"amount_capturable": 900 // 1000 - 100 = 900
     ...
  },
  "previous_attributes": {"amount_capturable": 1000
  }
}
```

### Charge captured events

We send a [charge.captured](https://docs.stripe.com/api/events/types.md#event_types-charge.captured) event for final captures or at the end of the authorization window to reverse the authorization of the uncaptured amount. The [captured](https://docs.stripe.com/api/charges/object.md#charge_object-captured) field for a charge only becomes `true` after a final capture or authorization reversal.

For example, if we do a capture with `amount=0` and `final_capture=true`, the [captured](https://docs.stripe.com/api/charges/object.md#charge_object-captured) attribute on the charge changes from false to true.

```json
// charge.captured
{
  "data": {
    "id": "ch_xxx",
    "object": "charge","captured": true
        ...
  },
  "previous_attributes": {"captured": false
  }
}

```

### Refund webhooks

Multicapture refund webhooks are no different than non-multicapture refund webhooks.

During each partial refund, we send a [refund.created](https://docs.stripe.com/api/events/types.md#event_types-refund.created) event. For connected accounts, we also send [application_fee.refunded](https://docs.stripe.com/api/events/types.md#event_types-application_fee.refunded) events when we refund application fees and [transfer.reversed](https://docs.stripe.com/api/events/types.md#event_types-transfer.reversed) events when we reverse transfers.

# Full embedded page

> This is a Full embedded page for when platform is web and ui is embedded-page. View the full page at https://docs.stripe.com/payments/multicapture?platform=web&ui=embedded-page.

Multicapture allows you to [capture a PaymentIntent](https://docs.stripe.com/api/payment_intents/capture.md) created during the confirmation step of a [CheckoutSession](https://docs.stripe.com/api/checkout_sessions.md) multiple times for a single transaction, up to the full [amount of the PaymentIntent](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-amount). You can use it when you have orders with multiple shipments, and want to capture funds as you fulfill parts of the order.

> #### IC+ feature
>
> Multicapture is part of the functionality we offer to users on _IC+ pricing_ (A pricing plan where businesses pay the variable network cost for each transaction plus the Stripe fee rather than a flat rate for all transactions. This pricing model provides more visibility into payments costs). If you’re on blended Stripe pricing and want access to this feature, contact us using the form at [Stripe support](https://support.stripe.com).

## Availability

When using multicapture, be aware of the following restrictions:

- It only supports online card payments
- Use [capture_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-capture_method) set to `manual`. Multicapture requires manual capture so that you can perform multiple partial captures on the PaymentIntent.
- It’s available with Amex, Visa, Discover, Mastercard, Cartes Bancaires, Diners Club, China UnionPay (CUP), and Japan Credit Bureau (JCB)
- [Separate charges and transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md) fund flows using [source_transaction](https://docs.stripe.com/api/transfers/create.md#create_transfer-source_transaction) aren’t supported
- Stripe allows you to capture up to 50 times for a single [PaymentIntent](https://docs.stripe.com/api/payment_intents.md)
- [mode](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-mode) is set to `payment` and [capture_method](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_intent_data-capture_method) is set to `manual` on the [CheckoutSession](https://docs.stripe.com/api/checkout/sessions/.md)

> #### CUP and JCB support
>
> CUP multicapture is only available in the United States. JCB multicapture is only available in the United States, Canada, Australia, and New Zealand.

> #### Automatic capture methods
>
> The API currently accepts `request_multicapture="if_available"` when `capture_method` is set to `automatic` or `automatic_async` without returning an error. In this case, `multicapture.status` on the charge may show `available`, but you can’t perform multiple captures because the PaymentIntent is automatically captured in full. Always set `capture_method` to `manual` when you intend to use multicapture. A future API version may return a validation error for this combination.

## Best practices

When sending separate shipments for one order, proactively notify your end customer with the details of each shipment. Doing so avoids inquiries and chargebacks from customers because of confusion with seeing multiple transactions on their bank statement. Use the following best practices when notifying customers:

- Inform them of the estimated delivery date and transaction amount for each shipment at the time of checkout, before purchase.
- Notify them upon each shipment, along with the transaction amount.
- Disclose your full refund and cancellation policy.

You can use the [custom_text](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-custom_text) field when creating a new [CheckoutSession](https://docs.stripe.com/api/checkout_sessions.md) to display additional text on the checkout page to help meet compliance requirements.

> #### Compliance
>
> You’re responsible for your compliance with all applicable laws, regulations, and network rules when using multicapture. Consult the rules for the card networks that you want to use this feature with to make sure your sales comply with all applicable rules, which vary by network. For example, most card networks restrict multicapture usage to card-not-present transactions for the sale of goods that ship separately. Certain card networks permit multicapture for businesses based on their industry (for example, travel), while some don’t permit multicapture for installment or deposit workflows.
>
> The information provided on this page relating to your compliance with these requirements is for your general guidance, and isn’t legal, tax, accounting, or other professional advice. Consult with a professional if you’re unsure about your obligations.

## Create a Checkout Session

From your server, create a _Checkout Session_ (A Checkout Session represents your customer's session as they pay for one-time purchases or subscriptions through Checkout. After a successful payment, the Checkout Session contains a reference to the Customer, and either the successful PaymentIntent or an active Subscription) and set the [ui_mode](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-ui_mode) to `embedded_page`. You can configure the [Checkout Session](https://docs.stripe.com/api/checkout/sessions/create.md) with [line items](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items) to include, and options such as [currency](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-currency).

To return customers to a custom page that you host on your website, specify that page’s URL in the [return_url](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-return_url) parameter. Include the `{CHECKOUT_SESSION_ID}` template variable in the URL to retrieve the session’s status on the return page. Checkout automatically substitutes the variable with the Checkout Session ID before redirecting.

Read more about [configuring the return page](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=checkout&ui=embedded-page#return-page) and other options for [customizing redirect behavior](https://docs.stripe.com/payments/checkout/custom-success-page.md?payment-ui=embedded-page).

After you create the Checkout Session, use the `client_secret` returned in the response to [mount Checkout](https://docs.stripe.com/payments/multicapture.md#mount-checkout).

To enable the multicapture feature, set [request_multicapture](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_method_options-card-request_multicapture) to `if_available`.

#### Node.js

```javascript
// This example sets up an endpoint using the Express framework.
const express = require("express");
const app = express();

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

app.post("/create-checkout-session", async (req, res) => {
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
    ui_mode: "embedded_page",
    payment_method_options: {
      card: {
        request_multicapture: "if_available",
      },
    },
    return_url:
      "https://example.com/checkout/return?session_id={CHECKOUT_SESSION_ID}",
  });

  res.send({ clientSecret: session.client_secret });
});

app.listen(4242, () => console.log(`Listening on port ${4242}!`));
```

### Payment methods

By default, Stripe enables cards and other common payment methods. You can turn individual payment methods on or off in the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods). In Checkout, Stripe evaluates the currency and any restrictions, then dynamically presents the supported payment methods to the customer.

To see how your payment methods appear to customers, enter a transaction ID or set an order amount and currency in the Dashboard.

You can enable Apple Pay and Google Pay in your [payment methods settings](https://dashboard.stripe.com/settings/payment_methods). By default, Apple Pay is enabled and Google Pay is disabled. However, in some cases Stripe filters them out even when they’re enabled. We filter Google Pay if you [enable automatic tax](https://docs.stripe.com/tax/checkout.md) without collecting a shipping address.

Checkout’s Stripe-hosted pages don’t need integration changes to enable Apple Pay or Google Pay. Stripe handles these payments the same way as other card payments.

## Mount Checkout

#### HTML + JS

Checkout is available as part of [Stripe.js](https://docs.stripe.com/js.md). Include the Stripe.js script on your page by adding it to the head of your HTML file. Next, create an empty DOM node (container) to use for mounting.

```html
<head>
  <script src="https://js.stripe.com/dahlia/stripe.js"></script>
</head>
<body>
  <div id="checkout">
    <!-- Checkout will insert the payment form here -->
  </div>
</body>
```

Initialize Stripe.js with your publishable API key.

Create an asynchronous `fetchClientSecret` function that makes a request to your server to create the Checkout Session and retrieve the client secret. Pass this function into `options` when you create the Checkout instance:

```javascript
// Initialize Stripe.js
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");

initialize();

// Fetch Checkout Session and retrieve the client secret
async function initialize() {
  const fetchClientSecret = async () => {
    const response = await fetch("/create-checkout-session", {
      method: "POST",
    });
    const { clientSecret } = await response.json();
    return clientSecret;
  };

  // Initialize Checkout
  const checkout = await stripe.createEmbeddedCheckoutPage({
    fetchClientSecret,
  });

  // Mount Checkout
  checkout.mount("#checkout");
}
```

#### React

Install [react-stripe-js](https://docs.stripe.com/sdks/stripejs-react.md) and the Stripe.js loader from npm:

```bash
npm install --save @stripe/react-stripe-js @stripe/stripe-js
```

To use the Embedded Checkout component, create an `EmbeddedCheckoutProvider`. Call `loadStripe` with your publishable API key and pass the returned `Promise` to the provider.

Create an asynchronous `fetchClientSecret` function that makes a request to your server to create the Checkout Session and retrieve the client secret. Pass this function into the `options` prop accepted by the provider.

```jsx
import * as React from "react";
import { loadStripe } from "@stripe/stripe-js";
import {
  EmbeddedCheckoutProvider,
  EmbeddedCheckout,
} from "@stripe/react-stripe-js";

// Make sure to call `loadStripe` outside of a component’s render to avoid
// recreating the `Stripe` object on every render.
const stripePromise = loadStripe("pk_test_123");

const App = () => {
  const fetchClientSecret = React.useCallback(() => {
    // Create a Checkout Session
    return fetch("/create-checkout-session", {
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => data.clientSecret);
  }, []);

  const options = { fetchClientSecret };

  return (
    <div id="checkout">
      <EmbeddedCheckoutProvider stripe={stripePromise} options={options}>
        <EmbeddedCheckout />
      </EmbeddedCheckoutProvider>
    </div>
  );
};
```

Checkout renders in an iframe that securely sends payment information to Stripe over an HTTPS connection.

> Avoid placing Checkout within another iframe because some payment methods require redirecting to another page for payment confirmation.

### Customize appearance

Customize Checkout to match the design of your site by setting the background color, button color, border radius, and fonts in your account’s [branding settings](https://dashboard.stripe.com/settings/branding).

By default, Checkout renders with no external padding or margin. We recommend using a container element such as a div to apply your desired margin (for example, 16px on all sides).

## Show a return page

After your customer attempts payment, Stripe redirects them to a return page that you host on your site. When you created the Checkout Session, you specified the URL of the return page in the [return_url](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-return_url) parameter. Read more about other options for [customizing redirect behavior](https://docs.stripe.com/payments/checkout/custom-success-page.md?payment-ui=embedded-page).

When rendering your return page, retrieve the Checkout Session status using the Checkout Session ID in the URL. Handle the result according to the session status as follows:

- `complete`: The payment succeeded. Use the information from the Checkout Session to render a success page.
- `open`: The payment failed or was canceled. Remount Checkout so that your customer can try again.

#### Node.js

```javascript
app.get("/session_status", async (req, res) => {
  const session = await stripe.checkout.sessions.retrieve(req.query.session_id);

  res.send({
    status: session.status,
    payment_status: session.payment_status,
    customer_email: session.customer_details.email,
  });
});
```

```javascript
const session = await fetch(`/session_status?session_id=${session_id}`);
if (session.status == "open") {
  // Remount embedded Checkout
} else if (session.status == "complete") {
  // Show success page
  // Optionally use session.payment_status or session.customer_email
  // to customize the success page
}
```

#### Redirect-based payment methods

During payment, some payment methods redirect the customer to an intermediate page, such as a bank authorization page. When they complete that page, Stripe redirects them to your return page.

Learn more about [redirect-based payment methods and redirect behavior](https://docs.stripe.com/payments/checkout/custom-success-page.md?payment-ui=embedded-page#redirect-based-payment-methods).

## Capture the PaymentIntent

For a PaymentIntent in a [requires_capture state](https://docs.stripe.com/payments/paymentintents/lifecycle.md) where multicapture is `available`, specifying the optional `final_capture` parameter to be `false` tells Stripe not to release the remaining uncaptured funds when calling the capture API. For example, if you confirm a 10 USD payment intent, capturing 7 USD with `final_capture=false` keeps the remaining 3 USD authorized.

```curl
curl https://api.stripe.com/v1/payment_intents/pi_xxx/capture \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount_to_capture=700 \
  -d final_capture=false \
  -d "expand[]=latest_charge"
```

In the PI capture response, the [amount_capturable](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-amount_capturable) and [amount_received](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-amount_received) fields update accordingly.

```json
// PaymentIntent Response
{
  "id": "pi_ANipwO3zNfjeWODtRPIg",
  "object": "payment_intent","amount": 1000,
  "amount_capturable": 300, // 1000 - 700 = 300
  "amount_received": 700,
  // if latest_charge is expanded
  "latest_charge": {
      "id": "ch_xxx",
      "object": "charge","amount": 1000,
      "amount_captured": 700,
      "amount_refunded": 0,
      ...
    }
  ...
}
```

## Final capture

The PaymentIntent remains in a `requires_capture` state until you do one of the following:

- Set `final_capture` to `true`.
- Make a capture without the `final_capture` parameter (because `final_capture` defaults to `true`).
- The authorization window expires.

At this point, Stripe releases any remaining funds and transitions the PaymentIntent to a `succeeded` state.

```curl
curl https://api.stripe.com/v1/payment_intents/pi_xxx/capture \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount_to_capture=200 \
  -d final_capture=true \
  -d "expand[]=latest_charge"
```

In the PI capture response, the [amount_capturable](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-amount_capturable) and [amount_received](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-amount_received) fields will be updated accordingly.

```json
// PaymentIntent Response
{
  "id": "pi_ANipwO3zNfjeWODtRPIg",
  "object": "payment_intent","amount": 1000,
  "amount_capturable": 0, // not 100 due to final_capture=true
  "amount_received": 900, // 700 + 200 = 900
  // if latest_charge is expanded
  "latest_charge": {
      "id": "ch_xxx",
      "object": "charge","amount": 1000,
      "amount_captured": 900,
      "amount_refunded": 0,
      ...
    }
  ...
}
```

Uncaptured PaymentIntents transition to `canceled`, while partially captured PaymentIntents transition to `succeeded`.

## Optional: Release uncaptured funds

If you want to release the uncaptured funds for a partially captured payment, set the amount to 0 and set `final_capture` to `true`.

```curl
curl https://api.stripe.com/v1/payment_intents/pi_xxx/capture \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount_to_capture=0 \
  -d final_capture=true
```

This transitions the PaymentIntent to `succeeded` and releases any uncaptured funds back to the cardholder.

## Test your integration

Use a Stripe test card with any CVC, postal code, and future expiration date to test multicapture payments.

| Number           | Payment Method                                 | Description                                                    |
| ---------------- | ---------------------------------------------- | -------------------------------------------------------------- |
| 4242424242424242 | `pm_card_visa`                                 | Visa test card that supports multicapture.                     |
| 4000002500001001 | `pm_card_visa_cartesBancaires`                 | Cartes Bancaires or Visa test card that supports multicapture. |
| 4000008400000076 | `pm_card_credit_disableEnterpriseCardFeatures` | Visa test card that doesn’t support multicapture.              |

## Refunds

For a PaymentIntent in `requires_capture` state, you can [refund](https://docs.stripe.com/api/refunds.md) any number of times up to the total captured amount minus the total refunded amount, which is the [amount_received](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-amount_received)—[amount_refunded](https://docs.stripe.com/api/charges/object.md#charge_object-amount_refunded). The [charge.refunded](https://docs.stripe.com/api/charges/object.md#charge_object-refunded) field transitions to `true` only when the final capture has been performed and the entire [amount_received](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-amount_received) is refunded.

Stripe doesn’t support _partial refunds_ (A partial refund is any refund in which less than the remaining refundable amount is refunded in a single request. The remaining refundable amount is the payment_intent.amount_received - charge.amount_refunded) with [refund_application_fee=true](https://docs.stripe.com/api/refunds/create.md#create_refund-refund_application_fee) or [reverse_transfer=true](https://docs.stripe.com/api/refunds/create.md#create_refund-reverse_transfer). Instead, you can perform partial fee refunds by manually performing partial fee refunds and transfer reversals using the [application fee refund](https://docs.stripe.com/api/fee_refunds.md) and [transfer reversal](https://docs.stripe.com/api/transfer_reversals.md) endpoints. After using the application fee refund or transfer reversal endpoints, Stripe doesn’t support any further refunds with `refund_application_fee=true` or `reverse_transfer=true` respectively.

## Connect

Multicapture supports all Connect use cases, with the exception of [Separate Charges and Transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md) with the [source_transaction](https://docs.stripe.com/api/transfers/create.md#create_transfer-source_transaction) parameter. The [application_fee_amount](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-application_fee_amount) and [transfer_data[amount]](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-transfer_data-amount) parameters have some additional validations. Consider the following validations when implementing multicapture with Connect:

- Setting `application_fee_amount` or `transfer_data[amount]` on the first capture makes it required for all subsequent captures. Each `application_fee_amount` and `transfer_data[amount]` passed at capture time overrides the values passed in on PaymentIntent creation, confirmation, and update.
- Stripe doesn’t support _partial refunds_ (A partial refund is any refund in which less than the remaining refundable amount is refunded in a single request. The remaining refundable amount is the payment_intent.amount_received - charge.amount_refunded) on multicapture payments with refund_application_fee=true or reverse_transfer=true. You can perform partial fee refunds or transfer reversals using the [application fee refund](https://docs.stripe.com/api/fee_refunds.md) and [transfer reversal](https://docs.stripe.com/api/transfer_reversals.md) endpoints.

## Webhooks

### Charge updated webhooks

We send a [charge.updated](https://docs.stripe.com/api/events/types.md#event_types-charge.updated) webhook each time you capture a payment.

For example, on the first capture of a destination charge multicapture payment with an `application_fee_amount`, we update these fields from empty to non-empty values.

```json
// charge.updated
{
  "data": {
    "id": "ch_xxx",
    "object": "charge",
    "amount": 1000,"balance_transaction": "txn_xxx", // applicable to all charges
    "transfer": "tr_xxx",             // applicable to destination charges only
    "application_fee": "fee_xxx",     // applicable to Connect only
    ...
  },
  "previous_attributes": {"balance_transaction": null, // applicable to all charges
    "transfer": null,            // applicable to destination charges only
    "application_fee": null,     // applicable to Connect only
  }
}
```

### payment_intent.amount_capturable_updated

We send [payment_intent.amount_capturable_updated](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.amount_capturable_updated) on every capture, regardless of `amount_to_capture` and `final_capture` values.

For example, if we capture 1 USD from a PaymentIntent with an amount of 10 USD, the PaymentIntent’s amount_capturable field updates to 9 USD.

```json
// payment_intent.amount_capturable_updated
{
  "data": {
    "id": "pi_xxx",
    "object": "payment_intent",
    "amount": 1000,"amount_capturable": 900 // 1000 - 100 = 900
     ...
  },
  "previous_attributes": {"amount_capturable": 1000
  }
}
```

### Charge captured events

We send a [charge.captured](https://docs.stripe.com/api/events/types.md#event_types-charge.captured) event for final captures or at the end of the authorization window to reverse the authorization of the uncaptured amount. The [captured](https://docs.stripe.com/api/charges/object.md#charge_object-captured) field for a charge only becomes `true` after a final capture or authorization reversal.

For example, if we do a capture with `amount=0` and `final_capture=true`, the [captured](https://docs.stripe.com/api/charges/object.md#charge_object-captured) attribute on the charge changes from false to true.

```json
// charge.captured
{
  "data": {
    "id": "ch_xxx",
    "object": "charge","captured": true
        ...
  },
  "previous_attributes": {"captured": false
  }
}

```

### Refund webhooks

Multicapture refund webhooks are no different than non-multicapture refund webhooks.

During each partial refund, we send a [refund.created](https://docs.stripe.com/api/events/types.md#event_types-refund.created) event. For connected accounts, we also send [application_fee.refunded](https://docs.stripe.com/api/events/types.md#event_types-application_fee.refunded) events when we refund application fees and [transfer.reversed](https://docs.stripe.com/api/events/types.md#event_types-transfer.reversed) events when we reverse transfers.

# Advanced integration

> This is a Advanced integration for when platform is web and ui is elements. View the full page at https://docs.stripe.com/payments/multicapture?platform=web&ui=elements.

Multicapture allows you to [capture a PaymentIntent](https://docs.stripe.com/api/payment_intents/capture.md) multiple times for a single authorization, up to the full [amount of the PaymentIntent](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-amount). You can use it when you have orders with multiple shipments, and want to capture funds as you fulfill parts of the order.

> #### IC+ feature
>
> Multicapture is part of the functionality we offer to users on _IC+ pricing_ (A pricing plan where businesses pay the variable network cost for each transaction plus the Stripe fee rather than a flat rate for all transactions. This pricing model provides more visibility into payments costs). If you’re on blended Stripe pricing and want access to this feature, contact us using the form at [Stripe support](https://support.stripe.com).

## Availability

When using multicapture, be aware of the following restrictions:

- It only supports online card payments
- Use [capture_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-capture_method) set to `manual`. Multicapture requires manual capture so that you can perform multiple partial captures on the PaymentIntent.
- It’s available with Amex, Visa, Discover, Mastercard, Cartes Bancaires, Diners Club, China UnionPay (CUP), and Japan Credit Bureau (JCB)
- [Separate charges and transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md) fund flows using [source_transaction](https://docs.stripe.com/api/transfers/create.md#create_transfer-source_transaction) aren’t supported
- Stripe allows you to capture up to 50 times for a single [PaymentIntent](https://docs.stripe.com/api/payment_intents.md)

> #### CUP and JCB support
>
> CUP multicapture is only available in the United States. JCB multicapture is only available in the United States, Canada, Australia, and New Zealand.

> #### Automatic capture methods
>
> The API currently accepts `request_multicapture="if_available"` when `capture_method` is set to `automatic` or `automatic_async` without returning an error. In this case, `multicapture.status` on the charge may show `available`, but you can’t perform multiple captures because the PaymentIntent is automatically captured in full. Always set `capture_method` to `manual` when you intend to use multicapture. A future API version may return a validation error for this combination.

## Best practices

When sending separate shipments for one order, proactively notify your end customer with the details of each shipment. Doing so avoids inquiries and chargebacks from customers because of confusion with seeing multiple transactions on their bank statement. Use the following best practices when notifying customers:

- Inform them of the estimated delivery date and transaction amount for each shipment at the time of checkout, before purchase.
- Notify them upon each shipment, along with the transaction amount.
- Disclose your full refund and cancellation policy.

> #### Compliance
>
> You’re responsible for your compliance with all applicable laws, regulations, and network rules when using multicapture. Consult the rules for the card networks that you want to use this feature with to make sure your sales comply with all applicable rules, which vary by network. For example, most card networks restrict multicapture usage to card-not-present transactions for the sale of goods that ship separately. Certain card networks permit multicapture for businesses based on their industry (for example, travel), while some don’t permit multicapture for installment or deposit workflows.
>
> The information provided on this page relating to your compliance with these requirements is for your general guidance, and isn’t legal, tax, accounting, or other professional advice. Consult with a professional if you’re unsure about your obligations.

## Create and confirm an uncaptured PaymentIntent

To indicate that you want separate authorization and capture, specify the [capture_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-capture_method) as `manual` when creating the PaymentIntent. To learn more about separate authorization and capture, see [how to place a hold on a payment method](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md).

Use the `if_available` or `never` parameters to request multicapture for this payment.

- `if_available`: The created PaymentIntent will allow multiple captures, if the payment method supports it.

- `never`: The created PaymentIntent won’t allow for multiple captures.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: "usd",
  payment_method_types: ["card"],
  payment_method: "pm_card_visa",
  confirm: true,
  capture_method: "manual",
  expand: ["latest_charge"],
  payment_method_options: {
    card: {
      request_multicapture: "if_available",
    },
  },
});
```

In the response, the `payment_method_details.card.multicapture.status` field on the [latest_charge](https://docs.stripe.com/api/charges/object.md) contains `available` or `unavailable` based on the customer’s payment method.

```json
// PaymentIntent Response
{
  "id": "pi_xxx",
  "object": "payment_intent","amount": 1000,
  "amount_capturable": 1000,
  "amount_received": 0,
  ...
  // if latest_charge is expanded
  "latest_charge": {
      "id": "ch_xxx",
      "object": "charge","amount": 1000,
      "amount_captured": 0,
      "amount_refunded": 0,
      "payment_method_details": {
        "card": {
          "multicapture": {"status": "available" // or "unavailable"
          }
        }
      }
      ...
    }
  ...
}
```

## Capture the PaymentIntent

For a PaymentIntent in a [requires_capture state](https://docs.stripe.com/payments/paymentintents/lifecycle.md) where multicapture is `available`, specifying the optional `final_capture` parameter to be `false` tells Stripe not to release the remaining uncaptured funds when calling the capture API. For example, if you confirm a 10 USD payment intent, capturing 7 USD with `final_capture=false` keeps the remaining 3 USD authorized.

```curl
curl https://api.stripe.com/v1/payment_intents/pi_xxx/capture \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount_to_capture=700 \
  -d final_capture=false \
  -d "expand[]=latest_charge"
```

In the PI capture response, the [amount_capturable](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-amount_capturable) and [amount_received](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-amount_received) fields update accordingly.

```json
// PaymentIntent Response
{
  "id": "pi_ANipwO3zNfjeWODtRPIg",
  "object": "payment_intent","amount": 1000,
  "amount_capturable": 300, // 1000 - 700 = 300
  "amount_received": 700,
  // if latest_charge is expanded
  "latest_charge": {
      "id": "ch_xxx",
      "object": "charge","amount": 1000,
      "amount_captured": 700,
      "amount_refunded": 0,
      ...
    }
  ...
}
```

## Final capture

The PaymentIntent remains in a `requires_capture` state until you do one of the following:

- Set `final_capture` to `true`.
- Make a capture without the `final_capture` parameter (because `final_capture` defaults to `true`).
- The authorization window expires.

At this point, Stripe releases any remaining funds and transitions the PaymentIntent to a `succeeded` state.

```curl
curl https://api.stripe.com/v1/payment_intents/pi_xxx/capture \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount_to_capture=200 \
  -d final_capture=true \
  -d "expand[]=latest_charge"
```

In the PI capture response, the [amount_capturable](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-amount_capturable) and [amount_received](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-amount_received) fields will be updated accordingly.

```json
// PaymentIntent Response
{
  "id": "pi_ANipwO3zNfjeWODtRPIg",
  "object": "payment_intent","amount": 1000,
  "amount_capturable": 0, // not 100 due to final_capture=true
  "amount_received": 900, // 700 + 200 = 900
  // if latest_charge is expanded
  "latest_charge": {
      "id": "ch_xxx",
      "object": "charge","amount": 1000,
      "amount_captured": 900,
      "amount_refunded": 0,
      ...
    }
  ...
}
```

Uncaptured PaymentIntents transition to `canceled`, while partially captured PaymentIntents transition to `succeeded`.

## Optional: Release uncaptured funds

If you want to release the uncaptured funds for a partially captured payment, set the amount to 0 and set `final_capture` to `true`.

```curl
curl https://api.stripe.com/v1/payment_intents/pi_xxx/capture \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount_to_capture=0 \
  -d final_capture=true
```

This transitions the PaymentIntent to `succeeded` and releases any uncaptured funds back to the cardholder.

## Test your integration

Use a Stripe test card with any CVC, postal code, and future expiration date to test multicapture payments.

| Number           | Payment Method                                 | Description                                                    |
| ---------------- | ---------------------------------------------- | -------------------------------------------------------------- |
| 4242424242424242 | `pm_card_visa`                                 | Visa test card that supports multicapture.                     |
| 4000002500001001 | `pm_card_visa_cartesBancaires`                 | Cartes Bancaires or Visa test card that supports multicapture. |
| 4000008400000076 | `pm_card_credit_disableEnterpriseCardFeatures` | Visa test card that doesn’t support multicapture.              |

## Refunds

For a PaymentIntent in `requires_capture` state, you can [refund](https://docs.stripe.com/api/refunds.md) any number of times up to the total captured amount minus the total refunded amount, which is the [amount_received](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-amount_received)—[amount_refunded](https://docs.stripe.com/api/charges/object.md#charge_object-amount_refunded). The [charge.refunded](https://docs.stripe.com/api/charges/object.md#charge_object-refunded) field transitions to `true` only when the final capture has been performed and the entire [amount_received](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-amount_received) is refunded.

Stripe doesn’t support _partial refunds_ (A partial refund is any refund in which less than the remaining refundable amount is refunded in a single request. The remaining refundable amount is the payment_intent.amount_received - charge.amount_refunded) with [refund_application_fee=true](https://docs.stripe.com/api/refunds/create.md#create_refund-refund_application_fee) or [reverse_transfer=true](https://docs.stripe.com/api/refunds/create.md#create_refund-reverse_transfer). Instead, you can perform partial fee refunds by manually performing partial fee refunds and transfer reversals using the [application fee refund](https://docs.stripe.com/api/fee_refunds.md) and [transfer reversal](https://docs.stripe.com/api/transfer_reversals.md) endpoints. After using the application fee refund or transfer reversal endpoints, Stripe doesn’t support any further refunds with `refund_application_fee=true` or `reverse_transfer=true` respectively.

## Connect

Multicapture supports all Connect use cases, with the exception of [Separate Charges and Transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md) with the [source_transaction](https://docs.stripe.com/api/transfers/create.md#create_transfer-source_transaction) parameter. The [application_fee_amount](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-application_fee_amount) and [transfer_data[amount]](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-transfer_data-amount) parameters have some additional validations. Consider the following validations when implementing multicapture with Connect:

- Setting `application_fee_amount` or `transfer_data[amount]` on the first capture makes it required for all subsequent captures. Each `application_fee_amount` and `transfer_data[amount]` passed at capture time overrides the values passed in on PaymentIntent creation, confirmation, and update.
- Stripe doesn’t support _partial refunds_ (A partial refund is any refund in which less than the remaining refundable amount is refunded in a single request. The remaining refundable amount is the payment_intent.amount_received - charge.amount_refunded) on multicapture payments with refund_application_fee=true or reverse_transfer=true. You can perform partial fee refunds or transfer reversals using the [application fee refund](https://docs.stripe.com/api/fee_refunds.md) and [transfer reversal](https://docs.stripe.com/api/transfer_reversals.md) endpoints.

## Webhooks

### Charge updated webhooks

We send a [charge.updated](https://docs.stripe.com/api/events/types.md#event_types-charge.updated) webhook each time you capture a payment.

For example, on the first capture of a destination charge multicapture payment with an `application_fee_amount`, we update these fields from empty to non-empty values.

```json
// charge.updated
{
  "data": {
    "id": "ch_xxx",
    "object": "charge",
    "amount": 1000,"balance_transaction": "txn_xxx", // applicable to all charges
    "transfer": "tr_xxx",             // applicable to destination charges only
    "application_fee": "fee_xxx",     // applicable to Connect only
    ...
  },
  "previous_attributes": {"balance_transaction": null, // applicable to all charges
    "transfer": null,            // applicable to destination charges only
    "application_fee": null,     // applicable to Connect only
  }
}
```

### payment_intent.amount_capturable_updated

We send [payment_intent.amount_capturable_updated](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.amount_capturable_updated) on every capture, regardless of `amount_to_capture` and `final_capture` values.

For example, if we capture 1 USD from a PaymentIntent with an amount of 10 USD, the PaymentIntent’s amount_capturable field updates to 9 USD.

```json
// payment_intent.amount_capturable_updated
{
  "data": {
    "id": "pi_xxx",
    "object": "payment_intent",
    "amount": 1000,"amount_capturable": 900 // 1000 - 100 = 900
     ...
  },
  "previous_attributes": {"amount_capturable": 1000
  }
}
```

### Charge captured events

We send a [charge.captured](https://docs.stripe.com/api/events/types.md#event_types-charge.captured) event for final captures or at the end of the authorization window to reverse the authorization of the uncaptured amount. The [captured](https://docs.stripe.com/api/charges/object.md#charge_object-captured) field for a charge only becomes `true` after a final capture or authorization reversal.

For example, if we do a capture with `amount=0` and `final_capture=true`, the [captured](https://docs.stripe.com/api/charges/object.md#charge_object-captured) attribute on the charge changes from false to true.

```json
// charge.captured
{
  "data": {
    "id": "ch_xxx",
    "object": "charge","captured": true
        ...
  },
  "previous_attributes": {"captured": false
  }
}

```

### Refund webhooks

Multicapture refund webhooks are no different than non-multicapture refund webhooks.

During each partial refund, we send a [refund.created](https://docs.stripe.com/api/events/types.md#event_types-refund.created) event. For connected accounts, we also send [application_fee.refunded](https://docs.stripe.com/api/events/types.md#event_types-application_fee.refunded) events when we refund application fees and [transfer.reversed](https://docs.stripe.com/api/events/types.md#event_types-transfer.reversed) events when we reverse transfers.
