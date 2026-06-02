<!-- Source: Stripe Terminal — Collect card payments (all SDK platforms) -->
<!-- Fetched: 2026-04-24 -->

# Collect card payments

Prepare your application and back end to collect card payments using Stripe Terminal.

# Server-driven

> This is a Server-driven for when terminal-sdk-platform is server-driven. View the full page at https://docs.stripe.com/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven.

For BBPOS WisePOS E and Stripe Reader S700/S710, we recommend server-side integration because it uses the Stripe API instead of a Terminal SDK to collect payments.

New to the Payment Intents API? Here are some helpful resources:

- [The Payment Intents API](https://docs.stripe.com/payments/payment-intents.md)
- [The PaymentIntent object](https://docs.stripe.com/api/payment_intents.md)
- [More payment scenarios](https://docs.stripe.com/payments/more-payment-scenarios.md)

Collecting payments with Stripe Terminal requires writing a payment flow in your application. Use the Stripe Terminal SDK to create and update a [PaymentIntent](https://docs.stripe.com/api.md#payment_intents), an object representing a single payment session.

While the core concepts are similar to SDK-based integrations, you follow slightly different steps with the server-driven integration:

1. [Create a PaymentIntent](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=server-driven#create-payment). You can define whether to [automatically](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-capture_method) or [manually](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md) capture your payments.
1. [Process the payment](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=server-driven#process-payment). Authorization on the customer’s card takes place when the reader processes the payment.
1. (Optional) [Capture the PaymentIntent](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=server-driven#capture-payment).

> This integration shape doesn’t support [offline card payments](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md).

## Create a PaymentIntent

- [Create a PaymentIntent](https://docs.stripe.com/api/payment_intents/create.md)

The first step in collecting payments is to start the payment flow. When a customer begins checking out, your backend must create a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) object that represents a new payment session on Stripe. With the server-driven integration, you create the PaymentIntent server-side.

In a sandbox, you can use [test amounts](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards) to simulate different error scenarios. In live mode, the amount of the PaymentIntent displays on the reader for payment.

For Terminal payments, the `payment_method_types` parameter must include `card_present`.

To accept Interac payments in Canada, you must also include `interac_present` in `payment_method_types`. Learn about [regional considerations for Canada](https://docs.stripe.com/terminal/payments/regional.md?integration-country=CA#create-a-paymentintent).

To accept non-card payment methods in supported countries, you must also specify your preferred types in `payment_method_types`. Learn about [additional payment methods](https://docs.stripe.com/terminal/payments/additional-payment-methods.md).

You can control the payment flow as follows:

- To fully control the payment flow for `card_present` payments, set the `capture_method` to `manual`. This allows you to add a reconciliation step before finalizing the payment.
- To authorize and capture payments in one step, set the `capture_method` to `automatic`.

> Don’t recreate a PaymentIntent if a card is declined. Instead, re-use the same PaymentIntent to help [avoid double charges](https://docs.stripe.com/terminal/payments/collect-card-payment.md#avoiding-double-charges).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  currency: "usd",
  payment_method_types: ["card_present"],
  capture_method: "manual",
  amount: 1000,
});
```

## Process the payment

You can process a payment immediately with the card presented by a customer, or instead inspect card details before proceeding to process the payment. For most use cases, we recommend processing immediately, as it’s a simpler integration with less API calls and webhook events. However, if you would like to insert your own business logic before the card is authorized, you can use the two-step collect-and-confirm flow.

#### Process immediately

- [Process a PaymentIntent](https://docs.stripe.com/api/terminal/readers/process_payment_intent.md)

After you create a PaymentIntent, the next step is to process the payment. The reader prompts the customer to insert or tap their card and then authorizes the payment.

To collect payment, make a request to Stripe with the ID of the PaymentIntent you created and the reader you want to use for the transaction.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const reader = await stripe.terminal.readers.processPaymentIntent(
  "{{TERMINALREADER_ID}}",
  {
    payment_intent: "{{PAYMENTINTENT_ID}}",
  },
);
```

Processing the payment happens asynchronously. A cardholder might take a few seconds to get their card from their wallet or pose a question to the operator during payment. When you process a payment, Stripe immediately responds to the request with an HTTP `200` status code as an acknowledgement that the reader received the action. In most cases, the request returns a [reader](https://docs.stripe.com/api/terminal/readers.md) with an `in_progress` status. However, because processing occurs asynchronously, the action status might already reflect the final state (`succeeded` or `failed`) if the payment completes quickly.

Simultaneously, the reader screen switches to a UI that prompts the customer to insert their card. To [verify the reader state](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=server-driven#verify-reader), listen to the `terminal.reader.action_succeeded` webhook or poll the Reader and PaymentIntent status to receive the status of the payment.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const reader = await stripe.terminal.readers.retrieve("{{TERMINALREADER_ID}}");
```

```json
{
  "id": "{{READER_ID}}",
  "object": "terminal.reader",
  ...
  "status": "online",
  "action": {
    "type": "process_payment_intent",
    "process_payment_intent": {
      "payment_intent": "{{PAYMENT_INTENT_ID}}"
    },
    "status": "in_progress",
    "failure_code": null,
    "failure_message": null
  }
}
```

#### Collect, inspect, and confirm

After you create a PaymentIntent, the next step is to process the payment. The reader prompts the customer to insert or tap their card and then creates a PaymentMethod.

### Collect a PaymentMethod

- [Collect a payment method](https://docs.stripe.com/api/terminal/readers/collect_payment_method.md)

To collect payment, make a request to Stripe with the ID of the PaymentIntent you created and the reader you want to use for the transaction.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const reader = await stripe.terminal.readers.collectPaymentMethod(
  "{{TERMINALREADER_ID}}",
  {
    payment_intent: "{{PAYMENTINTENT_ID}}",
  },
);
```

> After payment method collection you must authorize the payment or cancel collection within 30 seconds.

Collecting the payment happens asynchronously. A cardholder might take a few seconds to get their card from their wallet or pose a question to the operator during payment. When you start collecting a payment method, Stripe immediately responds to the request with an HTTP `200` status code and returns a reader with an action status of `in_progress`. Simultaneously, the reader screen switches to a UI that prompts the customer to insert their card.

After the reader collects card data, the PaymentMethod attaches to the server-side PaymentIntent and stores on the Reader object as `action.collect_payment_method.payment_method`. To [verify the reader state](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=server-driven#verify-reader), listen to the `terminal.reader.action_updated` webhook or poll the Reader action status to inspect the PaymentMethod.

At this point, you can access attributes like card brand, funding, and other useful data from the PaymentMethod.

Stripe attempts to detect whether a mobile wallet is used in a transaction as shown in the `wallet.type` attribute. However, the attribute isn’t populated if the card’s issuing bank doesn’t support reader-driven identification of a mobile wallet, so accurate detection isn’t guaranteed. After authorization in the [confirmation](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=server-driven&process=inspect#confirm-the-paymentintent) step, Stripe receives up-to-date information from the networks and updates `wallet.type` reliably.

### Confirm the PaymentIntent

- [Confirm a PaymentIntent](https://docs.stripe.com/api/terminal/readers/confirm_payment_intent.md)

After successfully collecting a PaymentMethod, you can proceed to authorize the payment.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const reader = await stripe.terminal.readers.confirmPaymentIntent(
  "{{TERMINALREADER_ID}}",
  {
    payment_intent: "{{PAYMENTINTENT_ID}}",
  },
);
```

Confirming the PaymentIntent is asynchronous. You can listen to the `terminal.reader.action_succeeded` webhook or poll the Reader and PaymentIntent status to receive the status of the payment.

If you’re using a simulated reader, use the [present_payment_method](https://docs.stripe.com/terminal/references/testing.md#simulated-card-presentment) endpoint to simulate a cardholder tapping or inserting their card on the reader. Use [test cards](https://docs.stripe.com/terminal/references/testing.md#standard-test-cards) to simulate different success or failure scenarios.

## Capture the payment

If you defined `capture_method` as `manual` during PaymentIntent creation in [Step 1](https://docs.stripe.com/terminal/payments/collect-card-payment.md#create-payment), the SDK returns an authorized but not captured PaymentIntent to your application. Learn more about the difference between [authorization and capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md). When your application receives a confirmed PaymentIntent, make sure it notifies your backend to capture the PaymentIntent. To do so, create an endpoint on your backend that accepts a PaymentIntent ID and sends a request to the Stripe API to capture it.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.capture(
  "{{PAYMENTINTENT_ID}}",
);
```

A successful capture call results in a PaymentIntent with a status of `succeeded`.

To make sure the application fee captured is correct for connected accounts, inspect each PaymentIntent and modify the application fee (if needed), before manually capturing the payment.

> You must manually capture `PaymentIntents` within two days or the authorization expires and funds are released to the customer.

### Collect tips (US only)

In the US, eligible users can [collect a tip on the receipt when capturing payments](https://docs.stripe.com/terminal/features/collecting-tips/on-receipt.md).

## Verify the reader state

To make sure the reader completed an action, your application must verify the reader state before initiating a new reader action or continuing to capture the payment. In most cases, this verification allows you to confirm a successful (approved) payment and show any relevant UX to your operator for them to complete the transaction. In other cases, you might need to [handle errors](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=api#handle-errors), including declined payments.

Use one of the following to check the reader status:

- [Listen to webhooks](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=server-driven#webhooks)
- [Poll the Stripe API](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=server-driven#stripe-api)
- [Use the PaymentIntent](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=server-driven#payment-intent)
- [Use the reader object](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=server-driven#reader-object)

#### Listen to webhooks (Recommended)

For maximum resiliency, we recommend your application listens to [webhooks](https://docs.stripe.com/webhooks.md) from Stripe to receive real-time notifications of the reader status. Stripe sends three webhooks to notify your application of a reader’s action status:

| Status                                     | Description                                                                                                                                |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `terminal.reader.action_succeeded`         | Sent when a reader action succeeds, such as when a payment is authorized successfully.                                                     |
| `terminal.reader.action_failed`            | Sent when a reader action fails, such as when a card is declined due to insufficient funds.                                                |
| `terminal.reader.action_updated` (Preview) | Sent when a reader action is updated, such as when a payment method is collected (only triggered for the `collect_payment_method` action). |

To listen for these webhooks, create a [webhook](https://docs.stripe.com/webhooks.md) endpoint. We recommend having a dedicated webhook endpoint for only these events because they’re high priority and in the critical payment path.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const webhookEndpoint = await stripe.webhookEndpoints.create({
  enabled_events: [
    "terminal.reader.action_succeeded",
    "terminal.reader.action_failed",
  ],
  url: "https://example.com/my/webhook/endpoint",
});
```

#### Poll the Stripe API

In case of webhook delivery issues, you can poll the Stripe API by adding a `check status` button to your point-of-sale interface that the operator can invoke, if needed.

#### Use the PaymentIntent

You can retrieve the PaymentIntent that you passed to the reader for processing. When you create a PaymentIntent it has an initial status of `requires_payment_method`. After you successfully collect the payment method, the status updates to `requires_confirmation`. After the payment processes successfully, the status updates to `requires_capture`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.retrieve(
  "{{PAYMENTINTENT_ID}}",
);
```

#### Use the reader object

You can use the [Reader](https://docs.stripe.com/api/terminal/readers/object.md) object, which contains an [action](https://docs.stripe.com/api/terminal/readers/object.md#terminal_reader_object-action) attribute that shows the latest action received by the reader and its status. Your application can [retrieve a Reader](https://docs.stripe.com/api/terminal/readers/retrieve.md) to check if the [status](https://docs.stripe.com/api/terminal/readers/object.md#terminal_reader_object-action-status) of the reader action has changed.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const reader = await stripe.terminal.readers.retrieve("{{TERMINALREADER_ID}}");
```

The Reader object is also returned as the response to the process payment step. The `action` type when processing a payment is `process_payment_intent`.

The `action.status` updates to `succeeded` for a successful payment. This means you can proceed with completing the transaction. Other values for `action.status` include `failed` or `in_progress`.

## Handle errors

The following errors are the most common types your application needs to handle:

- [Avoiding double charges](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=server-driven#avoiding-double-charges)
- [Payment failures](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=server-driven#payment-failures)
- [Payment timeout](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=server-driven#payment-timeout)
- [Payment cancellation](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=server-driven#payment-cancellation)
- [Reader busy](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=server-driven#reader-busy)
- [Reader timeout](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=server-driven#reader-timeout)
- [Reader offline](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=server-driven#reader-offline)
- [Missing webhooks](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=server-driven#missing-webhooks)
- [Delayed webhooks](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=server-driven#delayed-webhooks)

### Avoiding double charges

The PaymentIntent object enables money movement at Stripe—use a single PaymentIntent to represent a transaction.

Re-use the same PaymentIntent after a card is declined (for example, if it has insufficient funds), so your customer can try again with a different card.

If you edit the PaymentIntent, you must call [process_payment_intent](https://docs.stripe.com/api/terminal/readers/process_payment_intent.md) to update the payment information on the reader.

A PaymentIntent must be in the `requires_payment_method` state before Stripe can process it. An authorized, captured, or canceled PaymentIntent can’t be processed by a reader and results in an `intent_invalid_state` error:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const reader = await stripe.terminal.readers.processPaymentIntent(
  "{{TERMINALREADER_ID}}",
  {
    payment_intent: "{{PAYMENTINTENT_ID}}",
  },
);
```

```json
{
  "error": {
    "code": "intent_invalid_state",
    "doc_url": "https://docs.stripe.com/error-codes#intent-invalid-state",
    "message": "Payment intent must be in the requires_payment_method state to be processed by a reader.",
    "type": "invalid_request_error"
  }
}
```

### Payment failures

The most common payment failure is a failed payment authorization (for example, a payment that’s declined by the customer’s bank due to insufficient funds).

When a payment authorization fails, Stripe sends the `terminal.reader.action_failed` webhook. Check the [action.failure_code](https://docs.stripe.com/api/terminal/readers/object.md#terminal_reader_object-action-failure_code) and [action.failure_message](https://docs.stripe.com/api/terminal/readers/object.md#terminal_reader_object-action-failure_message) attributes to know why a payment is declined:

```json
{
  "id": "{{READER_ID}}",
  "object": "terminal.reader","action": {
    "failure_code": "card_declined",
    "failure_message": "Your card has insufficient funds.",
    "process_payment_intent": {
      "payment_intent": "{{PAYMENT_INTENT_ID}}"
    },
    "status": "failed",
    "type": "process_payment_intent"
  },
  ...
}
```

In the case of a declined card, prompt the customer for an alternative form of payment. Use the same PaymentIntent in another request to the [process_payment_intent](https://docs.stripe.com/api/terminal/readers/object.md#terminal_reader_object-action-process_payment_intent) endpoint. If you create a new PaymentIntent, you must [cancel](https://docs.stripe.com/api/payment_intents/cancel.md) the failed PaymentIntent to prevent double charges.

For card read errors (for example, an error reading the chip), the reader automatically prompts the customer to retry without any notification to your application. If multiple retries fail, you can prompt for another payment method by making another [process_payment_intent](https://docs.stripe.com/api/terminal/readers/object.md#terminal_reader_object-action-process_payment_intent) request.

### Payment timeout

A reader with unreliable internet connectivity can fail to process a payment because of a networking request timeout when authorizing the card. The reader shows a processing screen for several seconds, followed by a failure screen, and you receive a `terminal.reader.action_failed` webhook with a `failure_code` of `connection_error`:

```json
{
  "id": "{{READER_ID}}",
  "object": "terminal.reader","action": {
    "failure_code": "connection_error",
    "failure_message": "Could not connect to Stripe.",
    "process_payment_intent": {
      "payment_intent": "{{PAYMENT_INTENT_ID}}"
    },
    "status": "failed",
    "type": "process_payment_intent"
  },
  ...
}
```

The payment confirmation request might have been processed by Stripe’s backend systems, but the reader might have disconnected before receiving the response from Stripe. When receiving a webhook with this failure code, fetch the PaymentIntent `status` to verify if the payment is successfully authorized.

Make sure your network meets our [network requirements](https://docs.stripe.com/terminal/network-requirements.md) to minimize timeouts.

### Payment cancellation

#### Programmatic cancellation

You might need to cancel an in-flight payment. For example, if a customer adds items to their purchase after your integration has already initiated payment collection on the reader. Use the [cancel_action](https://docs.stripe.com/api/terminal/readers/object.md#terminal_reader_object-action-cancel_action) endpoint to reset the reader:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const reader = await stripe.terminal.readers.cancelAction(
  "{{TERMINALREADER_ID}}",
);
```

> You can’t cancel a reader action in the middle of a payment authorization. If a customer has already presented their card to pay on the reader, you must wait for processing to complete. An authorization normally takes a few seconds to complete. Calling [cancel_action](https://docs.stripe.com/api/terminal/readers/object.md#terminal_reader_object-action-cancel_action) during an authorization results in a `terminal_reader_busy` error.

#### Customer-initiated cancellation

Users can set the value of `enable_customer_cancellation` on these endpoints:

- [process_payment_intent](https://docs.stripe.com/api/terminal/readers/process_payment_intent.md)
- [process_setup_intent](https://docs.stripe.com/api/terminal/readers/process_setup_intent.md)
- [collect_payment_method](https://docs.stripe.com/api/terminal/readers/collect_payment_method.md)
- [refund_payment](https://docs.stripe.com/api/terminal/readers/refund_payment.md)

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const reader = await stripe.terminal.readers.processPaymentIntent(
  "{{TERMINALREADER_ID}}",
  {
    payment_intent: "{{PAYMENTINTENT_ID}}",
    process_config: {
      enable_customer_cancellation: true,
    },
  },
);
```

When set to true, smart reader users see a cancel button.
![Payment collection screen with customer cancellation button](assets/stripe-terminal-customer-cancellation.png)

Payment collection with cancellation enabled

Tapping the cancel button cancels the active transaction. Stripe sends a `terminal.reader.action_failed` webhook with a failure_code of `customer_canceled`.

```json
{
  "action": {
    "failure_code": "customer_canceled",
    "failure_message": "This action could not be completed due to an error on the card reader.",
    "process_payment_intent": {
      "payment_intent": "{{PAYMENT_INTENT_ID}}",
      "process_config": {
        "enable_customer_cancellation": true
      }
    },
    "status": "failed",
    "type": "process_payment_intent"
  }
}
```

### Reader busy

A reader can process only one payment at a time. While it’s processing a payment, attempting a new payment fails with a `terminal_reader_busy` error:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const reader = await stripe.terminal.readers.processPaymentIntent(
  "{{TERMINALREADER_ID}}",
  {
    payment_intent: "{{PAYMENTINTENT_ID}}",
  },
);
```

```json
{
  "error": {
    "code": "terminal_reader_busy",
    "doc_url": "https://docs.stripe.com/error-codes#terminal-reader-timeout",
    "message": "Reader is currently busy processing another request. Please reference the integration guide at https://stripe.com/docs/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven#handle-errors for details on how to handle this error.",
    "type": "invalid_request_error"
  }
}
```

Payments that have not begun processing can be replaced with a new payment.

A reader also rejects an API request if it’s busy performing updates, changing settings or if a card is inserted from the previous transaction.

### Reader timeout

On rare occasions, a reader might fail to respond to an API request on time because of temporary networking issues. If this happens, you receive a `terminal_reader_timeout` error code:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const reader = await stripe.terminal.readers.processPaymentIntent(
  "{{TERMINALREADER_ID}}",
  {
    payment_intent: "{{PAYMENTINTENT_ID}}",
  },
);
```

```json
{
  "error": {
    "code": "terminal_reader_timeout",
    "doc_url": "https://docs.stripe.com/error-codes#terminal-reader-timeout",
    "message": "There was a timeout when sending this command to the reader. Please reference the integration guide at https://stripe.com/docs/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven#handle-errors for details on how to handle this error.",
    "type": "invalid_request_error"
  }
}
```

In this case, we recommend you retry the API request. Make sure your network meets our [network requirements](https://docs.stripe.com/terminal/network-requirements.md) to minimize timeouts.

On rare occasions, a `terminal_reader_timeout` error code is a false negative. In this scenario, you receive a `terminal_reader_timeout` error from the API as described above, but the reader has actually received the command successfully. False negatives happen when Stripe sends a message to the reader, but doesn’t receive an acknowledgement back from the reader due to temporary networking failures.

### Reader offline

A location losing its internet connection might result in interrupted communication between the reader and Stripe. In this case, a reader is unresponsive to events initiated from your point-of-sale application and backend infrastructure.

A reader that consistently fails to respond to API requests is most likely powered off (for example, the power cord is disconnected or it’s out of battery) or not correctly connected to the internet.

A reader is considered offline if Stripe hasn’t received any signal from that reader in the past 2 minutes. Attempting to call API methods on a reader that’s offline results in a `terminal_reader_offline` error code:

```json
{
  "error": {
    "code": "terminal_reader_offline",
    "doc_url": "https://docs.stripe.com/error-codes#terminal-reader-offline",
    "message": "Reader is currently offline, please ensure the reader is powered on and connected to the internet before retrying your request. Reference the integration guide at https://docs.stripe.com/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven#reader-offline for details on how to handle this error.",
    "type": "invalid_request_error"
  }
}
```

Refer to our [network requirements](https://docs.stripe.com/terminal/network-requirements.md) to make sure a reader is correctly connected to the internet.

### Missing webhooks

When a reader disconnects in the middle of a payment, it can’t update its action status in the API. In this scenario, the reader shows an error screen after a card is presented. However, the Reader object in the API doesn’t update to reflect the failure on the device, and you also don’t get reader action webhooks. A reader might be left with an action status of `in_progress` when this happens, and a cashier has to intervene by calling the [cancel_action](https://docs.stripe.com/api/terminal/readers/object.md#terminal_reader_object-action-cancel_action) endpoint to reset the reader state.

### Delayed webhooks

On rare occasions, if Stripe is having an outage, reader action webhooks might be late. You can query the status of the Reader or the PaymentIntent objects to know what their latest state is.

## Webhook events

| Webhook                            | Description                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `terminal.reader.action_succeeded` | Sent when an asynchronous action succeeds. Sent for actions that need card presentment, such as `process_payment_intent`, `confirm_payment_intent`, `process_setup_intent`, and `refund_payment`.                                                                                                                                                                                                              |
| `terminal.reader.action_failed`    | Sent when an asynchronous action fails. Sent for actions that need card presentment such as `process_payment_intent`, `process_setup_intent`, `refund_payment`. No webhook is sent for the `set_reader_display` and `cancel_action` actions. Your integration must [handle these errors](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=server-driven#handle-errors). |
| `terminal.reader.action_updated`   | Sent when an asynchronous action is updated. Sent for actions such as `collect_payment_method`.                                                                                                                                                                                                                                                                                                                |

# JavaScript

> This is a JavaScript for when terminal-sdk-platform is js. View the full page at https://docs.stripe.com/terminal/payments/collect-card-payment?terminal-sdk-platform=js.

> #### Recommendation for smart readers
>
> For smart readers, such as the [BBPOS WisePOS E reader](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepos-e.md), [Stripe Reader S700/S710](https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710.md), and [Verifone readers](https://docs.stripe.com/terminal/payments/setup-reader/verifone.md), we recommend using the [server-driven integration](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=server-driven) instead of the JavaScript SDK.
>
> The JavaScript SDK requires your POS and reader on the same local network with working local DNS. The server-driven integration uses the Stripe API instead, which can be simpler in complex network environments. See our [platform comparison](https://docs.stripe.com/terminal/payments/setup-reader.md#sdk) to help you choose the best platform for your needs.

New to the Payment Intents API? Here are some helpful resources:

- [The Payment Intents API](https://docs.stripe.com/payments/payment-intents.md)
- [The PaymentIntent object](https://docs.stripe.com/api/payment_intents.md)
- [More payment scenarios](https://docs.stripe.com/payments/more-payment-scenarios.md)

Collecting payments with Stripe Terminal requires writing a payment flow in your application. Use the Stripe Terminal SDK to create and update a [PaymentIntent](https://docs.stripe.com/api.md#payment_intents), an object representing a single payment session.

Designed to be robust to failures, the Terminal integration splits the payment process into several steps, each of which can be retried safely:

1. [Create a PaymentIntent](https://docs.stripe.com/terminal/payments/collect-card-payment.md#create-payment).
1. [Collect a payment method](https://docs.stripe.com/terminal/payments/collect-card-payment.md#collect-payment). You can define whether to [automatically](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-capture_method) or [manually](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md) capture your payments.
1. [Process the payment](https://docs.stripe.com/terminal/payments/collect-card-payment.md#confirm-payment). Authorization on the customer’s card takes place when the SDK processes the payment.
1. (Optional) [Capture the payment](https://docs.stripe.com/terminal/payments/collect-card-payment.md#capture-payment)

> This integration shape doesn’t support [offline card payments](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md).

## Create a PaymentIntent [Server-side]

The first step when collecting payments is to start the payment flow. When a customer begins checking out, your application must create a `PaymentIntent` object. This represents a new payment session on Stripe.

Use [test amounts](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards) to try producing different results. An amount ending in `00` results in an approved payment.

> #### Don't recreate PaymentIntents for declined cards
>
> Don’t recreate a PaymentIntent if a card is declined. Instead, reuse the same PaymentIntent to help [avoid double charges](https://docs.stripe.com/terminal/payments/collect-card-payment.md#avoiding-double-charges).

The following example shows how to create a `PaymentIntent` on your server:

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const intent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: "sgd",
  payment_method_types: ["card_present"],
  capture_method: "manual",
});
```

For Terminal payments, the `payment_method_types` parameter must include `card_present`.

You can control the payment flow as follows:

- To fully control the payment flow for `card_present` payments, set the `capture_method` to `manual`. This allows you to add a reconciliation step before finalizing the payment.
- To authorize and capture payments in one step, set the `capture_method` to `automatic`.

To accept Interac payments in Canada, you must also include `interac_present` in `payment_method_types`. For more details, visit our [Canada documentation](https://docs.stripe.com/terminal/payments/regional.md?integration-country=CA).

The `PaymentIntent` contains a [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret), a key that’s unique to the individual `PaymentIntent`. To use the client secret, you must obtain it from the `PaymentIntent` on your server and [pass it to the client side](https://docs.stripe.com/payments/payment-intents.md#passing-to-client).

#### Node.js

```javascript
const express = require("express");
const app = express();

app.post("/create_payment_intent", async (req, res) => {
  const intent = // ... Fetch or create the PaymentIntent
    res.json({ client_secret: intent.client_secret });
});

app.listen(3000, () => {
  console.log("Running on port 3000");
});
```

Use the client secret as a parameter when calling [collectPaymentMethod](https://docs.stripe.com/terminal/references/api/js-sdk.md#collect-payment-method).

The `client_secret` is all you need in your client-side application to proceed to payment method collection.

## Collect a payment method [Client-side]

- [collectPaymentMethod (JavaScript)](https://docs.stripe.com/terminal/references/api/js-sdk.md#collect-payment-method)

After you’ve created a `PaymentIntent`, the next step is to collect a payment method with the SDK.

To collect a payment method, your app needs to be connected to a reader. The connected reader waits for a card to be presented after your app calls `collectPaymentMethod`.

```javascript
async () => {
  // clientSecret is the client_secret from the PaymentIntent you created in Step 1.
  const result = await terminal.collectPaymentMethod(clientSecret);
  if (result.error) {
    // Placeholder for handling result.error
  } else {
    // Placeholder for processing result.paymentIntent
  }
};
```

This method collects encrypted payment method data using the connected card reader, and associates the encrypted data with the local `PaymentIntent`.

### Optionally inspect payment method details

- [collectPaymentMethod config_override (JavaScript)](https://docs.stripe.com/terminal/references/api/js-sdk.md#collect-payment-method)

For advanced use cases, you can examine the payment method details of the presented card and perform your own business logic prior to authorization.

Use the `update_payment_intent` parameter to attach a `PaymentMethod` to the server-side `PaymentIntent`. This data is returned in the `collectPaymentMethod` response.

```javascript
async () => {
  // clientSecret is the client_secret from the PaymentIntent you created in Step 1.
  const result = await terminal.collectPaymentMethod(clientSecret, {
    config_override: {
      update_payment_intent: true,
    },
  });
  if (result.error) {
    // Placeholder for handling result.error
  } else {
    const pm = result.paymentIntent.payment_method;
    const card = pm?.card_present ?? pm?.interac_present;

    // Placeholder for business logic on card before processing result.paymentIntent
  }
};
```

This method attaches the collected encrypted payment method data with an update to the `PaymentIntent` object. It doesn’t requires authorization until you [process the payment](https://docs.stripe.com/terminal/payments/collect-card-payment.md#confirm-payment). This advanced use case isn’t supported on the Verifone P400.

After payment method collection you must authorize the payment or cancel collection within 30 seconds.

If the SDK is [operating offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md), the `paymentMethod` field isn’t present in the `PaymentIntent` object.

You can access attributes like card brand, funding, and other useful data at this point.

Stripe attempts to detect whether a mobile wallet is used in a transaction as shown in the `wallet.type` attribute. However, the attribute isn’t populated if the card’s issuing bank doesn’t support reader-driven identification of a mobile wallet, so accurate detection isn’t guaranteed. After authorization in the [confirmation](https://docs.stripe.com/terminal/payments/collect-card-payment.md#confirm-payment) step, Stripe receives up-to-date information from the networks and updates `wallet.type` reliably

### Cancel collection

#### Programmatic cancellation

You can cancel collecting a payment method by calling [cancelCollectPaymentMethod](https://docs.stripe.com/terminal/references/api/js-sdk.md#cancel-collect-payment-method) in the JavaScript SDK.

#### Customer-initiated cancellation

- [enable_customer_cancellation (JavaScript)](https://docs.stripe.com/terminal/references/api/js-sdk.md#collect-payment-method)

When you set `enable_customer_cancellation` to true for a transaction, smart reader users see a cancel button.

Tapping the cancel button cancels the active transaction.

```javascript
terminal.collectPaymentMethod(clientSecret, {
  config_override: { enable_customer_cancellation: true },
});
```

### Handle events

> The JavaScript SDK only supports the Verifone P400, BBPOS WisePOS E, and Stripe Reader S700/S710, which have a built-in display. Your application doesn’t need to display events from the payment method collection process to users, because the reader displays them. To clear the payment method on a transaction, the cashier can press the cancel (❌) key.

## Confirm the payment [Client-side]

- [processPayment (JavaScript)](https://docs.stripe.com/terminal/references/api/js-sdk.md#process-payment)

After successfully collecting a payment method from the customer, the next step is to process the payment with the SDK. When you’re ready to proceed with the payment, call `processPayment` with the updated `PaymentIntent` from [Step 2](https://docs.stripe.com/terminal/payments/collect-card-payment.md#collect-payment).

- For manual capture of payments, a successful `processPayment` call results in a `PaymentIntent` with a status of `requires_capture`.
- For automatic capture of payments, the `PaymentIntent` transitions to a `succeeded` state.

Always confirm PaymentIntents using the Terminal SDK on the client side. Server-side confirmation bypasses critical interactions, such as PIN prompts, and can result in transaction failures.

```javascript
async () => {
  const result = await terminal.processPayment(paymentIntent);
  if (result.error) {
    // Placeholder for handling result.error
  } else if (result.paymentIntent) {
    // Placeholder for notifying your backend to capture result.paymentIntent.id
  }
};
```

You must manually capture a PaymentIntent within 2 days or the authorization expires and funds are released to the customer.

### Handle failures

- [Error codes (JavaScript)](https://docs.stripe.com/terminal/references/api/js-sdk.md#error-codes)

When processing a payment fails, the SDK returns an error that includes the updated `PaymentIntent`. Your application needs to inspect the `PaymentIntent` to decide how to deal with the error.

| PaymentIntent Status      | Meaning                                                     | Resolution                                                                                                                                      |
| ------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `requires_payment_method` | Payment method declined                                     | Try collecting a different payment method by calling `collectPaymentMethod` again with the same `PaymentIntent`.                                |
| `requires_confirmation`   | Temporary connectivity problem                              | Call `processPayment` again with the same `PaymentIntent` to retry the request.                                                                 |
| `PaymentIntent` is `nil`  | Request to Stripe timed out, unknown `PaymentIntent` status | Retry processing the original `PaymentIntent`. Don’t create a new one, because that might result in multiple authorizations for the cardholder. |

If you encounter multiple, consecutive timeouts, there might be a problem with your connectivity. Make sure that your app can communicate with the internet.

### Avoiding double charges

The `PaymentIntent` object enables money movement at Stripe—use a single `PaymentIntent` to represent a transaction.

Re-use the same `PaymentIntent` after a card is declined (for example, if it has insufficient funds), so your customer can try again with a different card.

If you edit the `PaymentIntent`, you must call `collectPaymentMethod` to update the payment information on the reader.

A `PaymentIntent` must be in the `requires_payment_method` state before Stripe can process it. An authorized, captured, or canceled `PaymentIntent` can’t be processed by a reader.

## Capture the payment [Server-side]

If you defined `capture_method` as `manual` during `PaymentIntent` creation in [Step 1](https://docs.stripe.com/terminal/payments/collect-card-payment.md#create-payment), the SDK returns an authorized but not captured `PaymentIntent` to your application. Learn more about the difference between [authorization and capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md).

When your app receives a confirmed `PaymentIntent` from the SDK, make sure it notifies your backend to capture the payment. Create an endpoint on your backend that accepts a `PaymentIntent` ID and sends a request to the Stripe API to capture it:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.capture(
  "{{PAYMENT_INTENT_ID}}",
);
```

A successful `capture` call results in a `PaymentIntent` with a status of `succeeded`.

To make sure the application fee captured is correct for connected accounts, inspect each `PaymentIntent` and modify the application fee, if needed, before manually capturing the payment.

### Reconcile payments

To monitor the payments activity of your business, you might want to reconcile PaymentIntents with your internal orders system on your server at the end of a day’s activity.

A `PaymentIntent` that retains a `requires_capture` status might represent two things:

**Unnecessary authorization on your customer’s card statement**

- Cause: User abandons your app’s checkout flow in the middle of a transaction
- Solution: If the uncaptured `PaymentIntent` isn’t associated with a completed order on your server, you can [cancel](https://docs.stripe.com/api/payment_intents/cancel.md) it. You can’t use a canceled `PaymentIntent` to perform charges.

**Incomplete collection of funds from a customer**

- Cause: Failure of the request from your app notifying your backend to capture the payment
- Solution: If the uncaptured `PaymentIntent` is associated with a completed order on your server, and no other payment has been taken for the order (for example, a cash payment), you can [capture](https://docs.stripe.com/api/payment_intents/capture.md) it.

### Collect tips (US only)

In the US, eligible users can [collect a tip on the receipt when capturing payments](https://docs.stripe.com/terminal/features/collecting-tips/on-receipt.md).

# iOS

> This is a iOS for when terminal-sdk-platform is ios. View the full page at https://docs.stripe.com/terminal/payments/collect-card-payment?terminal-sdk-platform=ios.

New to the Payment Intents API? Here are some helpful resources:

- [The Payment Intents API](https://docs.stripe.com/payments/payment-intents.md)
- [The PaymentIntent object](https://docs.stripe.com/api/payment_intents.md)
- [More payment scenarios](https://docs.stripe.com/payments/more-payment-scenarios.md)

Collecting payments with Stripe Terminal requires writing a payment flow in your application. Use the Stripe Terminal SDK to create and update a [PaymentIntent](https://docs.stripe.com/api.md#payment_intents), an object representing a single payment session.

Designed to be robust to failures, the Terminal integration splits the payment process into several steps, each of which can be retried safely:

1. [Create a PaymentIntent](https://docs.stripe.com/terminal/payments/collect-card-payment.md#create-payment).
1. [Process the payment](https://docs.stripe.com/terminal/payments/collect-card-payment.md#process-payment). Authorization on the customer’s card takes place when the SDK processes the payment.
1. (Optional) [Capture the payment](https://docs.stripe.com/terminal/payments/collect-card-payment.md#capture-payment)

## Create a PaymentIntent [Client-side] [Server-side]

The first step when collecting payments is to start the payment flow. When a customer begins checking out, your application must create a `PaymentIntent` object. This represents a new payment session on Stripe.

- [createPaymentIntent (iOS)](<https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)createPaymentIntent:completion:>)

You can create a `PaymentIntent` on the client or server.

Use [test amounts](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards) to try producing different results. An amount ending in `00` results in an approved payment.

> #### Don't recreate PaymentIntents for declined cards
>
> Don’t recreate a PaymentIntent if a card is declined. Instead, re-use the same PaymentIntent to help [avoid double charges](https://docs.stripe.com/terminal/payments/collect-card-payment.md#avoiding-double-charges).

### Client-side

Create a `PaymentIntent` from your client:

> If your app is connected to the Verifone P400, you can’t create a PaymentIntent from the iOS SDK. Instead, you must [create the PaymentIntent server-side](https://docs.stripe.com/terminal/payments/collect-card-payment.md#create-server-side), and retrieve the PaymentIntent in your app using the `Terminal.retrievePaymentIntent` method in the SDK.

#### Swift

```swift
import UIKit
import StripeTerminal

class PaymentViewController: UIViewController {

    // ...

    // Action for a "Checkout" button
    func checkoutAction() throws {
        let params = try PaymentIntentParametersBuilder(amount: 1000, currency: "sgd").build()
        Terminal.shared.createPaymentIntent(params) { createResult, createError in
            if let error = createError {
                print("createPaymentIntent failed: \(error)")
            } else if let paymentIntent = createResult {
                print("createPaymentIntent succeeded")
                // ...
            }

        }
    }

    // ...
}
```

### Server-side

You can create the `PaymentIntent` on your server if the information required to start a payment isn’t readily available in your app.

The following example shows how to create a `PaymentIntent` on your server:

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const intent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: "sgd",
  payment_method_types: ["card_present"],
  capture_method: "manual",
});
```

For Terminal payments, the `payment_method_types` parameter must include `card_present`.

You can control the payment flow as follows:

- To fully control the payment flow for `card_present` payments, set the `capture_method` to `manual`. This allows you to add a reconciliation step before finalizing the payment.
- To authorize and capture payments in one step, set the `capture_method` to `automatic`.

To accept payments in Australia, you need to set `capture_method` to `automatic` or `manual_preferred`. For more details, visit our [Australia documentation](https://docs.stripe.com/terminal/payments/regional.md?integration-country=AU). To accept Interac payments in Canada, you must also include `interac_present` in `payment_method_types`. For more details, visit our [Canada documentation](https://docs.stripe.com/terminal/payments/regional.md?integration-country=CA).

The `PaymentIntent` contains a [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret), a key that’s unique to the individual `PaymentIntent`. To use the client secret, you must obtain it from the `PaymentIntent` on your server and [pass it to the client side](https://docs.stripe.com/payments/payment-intents.md#passing-to-client).

#### Node.js

```javascript
const express = require("express");
const app = express();

app.post("/create_payment_intent", async (req, res) => {
  const intent = // ... Fetch or create the PaymentIntent
    res.json({ client_secret: intent.client_secret });
});

app.listen(3000, () => {
  console.log("Running on port 3000");
});
```

- [retrievePaymentIntent (iOS)](<https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)retrievePaymentIntent:completion:>)

To retrieve a `PaymentIntent`, use the client secret to call `retrievePaymentIntent`.

After you retrieve the `PaymentIntent`, use it to call `processPaymentIntent`.

#### Swift

```swift
func checkoutButtonAction() {
    // ... Fetch the client secret from your backend
    Terminal.shared.retrievePaymentIntent(clientSecret: clientSecret) { retrieveResult, retrieveError in
        if let error = retrieveError {
            print("retrievePaymentIntent failed: \(error)")
        }
        else if let paymentIntent = retrieveResult {
            print("retrievePaymentIntent succeeded: \(paymentIntent)")
            // ...
        }
    }
}
```

## Process the payment [Client-side]

You can process a payment immediately with the card presented by a customer, or instead inspect card details before proceeding to process the payment. For most use cases, we recommend processing immediately, because it’s a simpler integration with fewer API calls. However, if you want to insert your own business logic before authorizing the card, use the two-step collect-and-confirm flow.

#### Process immediately

After you create a PaymentIntent, the next step is to process the payment. The reader prompts the customer to insert or tap their card and then attempts to authorize the payment.

- [processPaymentIntent (iOS)](<https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)processPaymentIntent:delegate:completion:>)

While processing a payment, cardholder might take a few seconds to get their card from their wallet or pose a question to the operator during payment.

#### Swift

```swift


// Action for a "Checkout" button
func checkoutAction() throws {
  let params = try PaymentIntentParametersBuilder(amount: 1000, currency: "sgd").build()
  Terminal.shared.createPaymentIntent(params) { createResult, createError in
      if let error = createError {
          print("createPaymentIntent failed: \(error)")
      } else if let paymentIntent = createResult {
          print("createPaymentIntent succeeded")
          self.processCancelable = Terminal.shared.processPaymentIntent(paymentIntent, collectConfig: nil, confirmConfig: nil) { processResult, processError in
              if let error = processError {
                  print("processPaymentIntent failed: \(error)")
              } else if let processedPaymentIntent = processResult {
                  print("processPaymentIntent succeeded")
                  // Notify your backend to capture the PaymentIntent
                  if let stripeId = processedPaymentIntent.stripeId {
                      APIClient.shared.capturePaymentIntent(stripeId) { captureError in
                          if let error = captureError {
                              print("capturePaymentIntent failed: \(error)")
                          } else {
                              print("capturePaymentIntent succeeded")
                          }
                      }
                  } else {
                      print("Payment processed offline");
                  }
              }
          }
      }
  }
}
```

### Cancel collection

#### Programmatic cancellation

- [Cancelable (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPCancelable.html)

You can cancel processing a PaymentIntent using the `Cancelable` object returned by the iOS SDK.

#### Customer-initiated cancellation

- [setCustomerCancellation (iOS)](<https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPCollectPaymentIntentConfigurationBuilder.html#/c:objc(cs)SCPCollectPaymentIntentConfigurationBuilder(im)setCustomerCancellation>)
- [CustomerCancellation (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Enums/SCPCustomerCancellation.html)

Smart readers show customers a cancel button by default. You can disable this by setting `customerCancellation` to `.disableIfAvailable`.

Tapping the cancel button cancels the active transaction.

#### Swift

```swift
let collectConfig = try CollectPaymentIntentConfigurationBuilder()
    .setCustomerCancellation(.disableIfAvailable) // turn OFF the cancel button, ON by default
    .build()
Terminal.shared.collectPaymentMethod(paymentIntent: paymentIntent, collectConfig: collectConfig) {
    intentWithPaymentMethod, attachError in
}
```

### Handle events

- [ReaderDisplayDelegate (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Protocols/SCPReaderDisplayDelegate.html)

When collecting a payment method using a reader such as the [Stripe M2](https://docs.stripe.com/terminal/readers/stripe-m2.md), without a built-in display, your app must be able to display events from the payment method collection process to users. These events help users successfully collect payments (for example, retrying a card, trying a different card, or using a different read method).

When a transaction begins, the SDK passes a `ReaderInputOptions` value to your app’s reader display handler, denoting the acceptable types of input (for example, `Swipe`, `Insert`, or `Tap`). In your app’s checkout UI, prompt the user to present a card using one of these options.

During the transaction, the SDK might request your app to display additional prompts (for example, `Retry Card`) to your user by passing a `ReaderDisplayMessage` value to your app’s reader display handler. Make sure your checkout UI displays these messages to the user.

#### Swift

```swift
 // MARK: MobileReaderDelegate - only needed for Bluetooth readers, this is the delegate set during connectReader

 func reader(_ reader: Reader, didRequestReaderInput inputOptions: ReaderInputOptions = []) {
     readerMessageLabel.text = Terminal.stringFromReaderInputOptions(inputOptions)
 }

 func reader(_ reader: Reader, didRequestReaderDisplayMessage displayMessage: ReaderDisplayMessage) {
     readerMessageLabel.text = Terminal.stringFromReaderDisplayMessage(displayMessage)
 }
```

### Collect payments with Tap to Pay on iPhone

When your application is ready to collect a payment, the Stripe Terminal iOS SDK takes over the display to handle the collection process. After calling the [process payment](https://docs.stripe.com/terminal/payments/collect-card-payment.md#process-payment) method, your application remains running, but the iPhone displays a full-screen prompt to the cardholder, instructing them to present their card or NFC-based mobile wallet. If there’s an error reading the card, a prompt for retry displays. A successful presentation returns a success indication, and then control returns to your application.
![Tap to Pay on iPhone payment collection](assets/stripe-terminal-ttpoi-payment-collection.png)

Payment collection

- For manual capture of payments, a successful `processPaymentIntent` call results in a `PaymentIntent` with a status of `requires_capture`.
- For automatic capture of payments, the `PaymentIntent` transitions to a `succeeded` state.

You must manually capture a PaymentIntent within 2 days or the authorization expires and funds are released to the customer.

### Handle failures

- [ConfirmPaymentIntentError (iOS)](<https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPConfirmPaymentIntentError.html#/c:objc(cs)SCPConfirmPaymentIntentError(py)paymentIntent>)

When processing a payment fails, the SDK returns an error that includes the updated `PaymentIntent` if it was declined by stripe. Your application needs to inspect the `PaymentIntent` to decide how to deal with the error.

| PaymentIntent status      | Meaning                                                     | Resolution                                                                                                                                      |
| ------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `requires_payment_method` | Payment method declined                                     | Try collecting a different payment method by calling `processPaymentIntent` again with the same `PaymentIntent`.                                |
| `requires_confirmation`   | Temporary connectivity problem                              | Call `processPaymentIntent` again with the same `PaymentIntent` to retry the request.                                                           |
| `PaymentIntent` is `nil`  | Request to Stripe timed out, unknown `PaymentIntent` status | Retry processing the original `PaymentIntent`. Don’t create a new one, because that might result in multiple authorizations for the cardholder. |

If you encounter multiple, consecutive timeouts, there might be a problem with your connectivity. Make sure that your app can communicate with the internet.

### Avoid double charges

The `PaymentIntent` object enables money movement at Stripe—use a single `PaymentIntent` to represent a transaction.

Re-use the same `PaymentIntent` after a card is declined (for example, if it has insufficient funds), so your customer can try again with a different card.

If you edit the `PaymentIntent`, you must call `processPaymentIntent` to update the payment information on the reader.

A `PaymentIntent` must be in the `requires_payment_method` state before Stripe can process it. An authorized, captured, or canceled `PaymentIntent` can’t be processed by a reader.

#### Collect, inspect, and confirm

After you create a PaymentIntent, the next step is to process the payment. The reader prompts the customer to insert or tap their card and then creates a PaymentMethod.

## Collect a PaymentMethod

- [collectPaymentMethod (iOS)](<https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)collectPaymentMethod:delegate:completion:>)

After you’ve created a `PaymentIntent`, the next step is to collect a payment method with the SDK.

To collect a payment method, your app needs to be connected to a reader. The connected reader waits for a card to be presented after your app calls `collectPaymentMethod`.

#### Swift

```swift


import UIKit
import StripeTerminal

class PaymentViewController: UIViewController, ReaderDisplayDelegate {


    // Label for displaying messages from the card reader
    let readerMessageLabel = UILabel(frame: .zero)
    var collectCancelable: Cancelable? = nil

    // ...

    // Action for a "Checkout" button
    func checkoutAction() throws {
        let params = try PaymentIntentParametersBuilder(amount: 1000, currency: "sgd").build()
        Terminal.shared.createPaymentIntent(params) { createResult, createError in
            if let error = createError {
                print("createPaymentIntent failed: \(error)")
            }
            else if let paymentIntent = createResult {
                print("createPaymentIntent succeeded")
                self.collectCancelable = Terminal.shared.collectPaymentMethod(paymentIntent) { collectResult, collectError in
                    if let error = collectError {
                        print("collectPaymentMethod failed: \(error)")
                    }
                    else if let paymentIntent = collectResult {
                        print("collectPaymentMethod succeeded")
                        // ... Confirm the payment
                    }
                }
            }

        }
    }
 }

 // MARK: MobileReaderDelegate - only needed for mobile readers, this is the delegate set during connectReader

 func reader(_ reader: Reader, didRequestReaderInput inputOptions: ReaderInputOptions = []) {
     readerMessageLabel.text = Terminal.stringFromReaderInputOptions(inputOptions)
 }

 func reader(_ reader: Reader, didRequestReaderDisplayMessage displayMessage: ReaderDisplayMessage) {
     readerMessageLabel.text = Terminal.stringFromReaderDisplayMessage(displayMessage)
 }
 // MARK: ReaderDisplayDelegate

 func terminal(_ terminal: Terminal, didRequestReaderInput inputOptions: ReaderInputOptions = []) {
     readerMessageLabel.text = Terminal.stringFromReaderInputOptions(inputOptions)
 }

 func terminal(_ terminal: Terminal, didRequestReaderDisplayMessage displayMessage: ReaderDisplayMessage) {
     readerMessageLabel.text = Terminal.stringFromReaderDisplayMessage(displayMessage)
 }
```

This method collects encrypted payment method data using the connected card reader, and associates the encrypted data with the local `PaymentIntent`.

### Optionally inspect payment method details

- [CollectPaymentIntentConfiguration (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPCollectPaymentIntentConfiguration.html)
- [CardPresentDetails (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPCardPresentDetails.html)

For advanced use cases, you can examine the payment method details of the presented card and perform your own business logic prior to authorization.

Use the `setUpdatePaymentIntent` setter in `CollectPaymentIntentConfigurationBuilder` to attach a `PaymentMethod` to the server-side `PaymentIntent`. This data is returned in the `collectPaymentMethod` response.

#### Swift

```swift


class PaymentViewController: UIViewController, ReaderDisplayDelegate {
    // ...

    // Action for a "Checkout" button
    func checkoutAction() throws {
        let params = try PaymentIntentParametersBuilder(amount: 1000, currency: "sgd").build()
        Terminal.shared.createPaymentIntent(params) { createResult, createError in
            if let error = createError {
                print("createPaymentIntent failed: \(error)")
            }
            else if let paymentIntent = createResult {
                print("createPaymentIntent succeeded")
                let collectConfig = try CollectPaymentIntentConfigurationBuilder().setUpdatePaymentIntent(true).build()
                self.collectCancelable = Terminal.shared.collectPaymentMethod(paymentIntent: paymentIntent, collectConfig: collectConfig) {
                  collectResult, collectError in
                    if let error = collectError {
                        print("collectPaymentMethod failed: \(error)")
                    }
                    else if let paymentIntent = collectResult {
                        print("collectPaymentMethod succeeded")
                        if let paymentMethod = paymentIntent.paymentMethod,
                            let card = paymentMethod.cardPresent ?? paymentMethod.interacPresent {

                            // ... Perform business logic on card
                        }

                        // ... Confirm the payment
                    }
                }
            }

        }
    }
 }
```

This method attaches the collected encrypted payment method data with an update to the `PaymentIntent` object. It doesn’t require authorization until you confirm the payment. This advanced use case isn’t supported on the Verifone P400.

After payment method collection, you must authorize or cancel the payment within 30 seconds.

If the SDK is [operating offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md), the `paymentMethod` field isn’t present in the `PaymentIntent` object.

You can access attributes like card brand, funding, and other useful data at this point.

Stripe attempts to detect whether a mobile wallet is used in a transaction as shown in the `wallet.type` attribute. However, the attribute isn’t populated if the card’s issuing bank doesn’t support reader-driven identification of a mobile wallet, so accurate detection isn’t guaranteed. After authorization and when you [process the payment](https://docs.stripe.com/terminal/payments/collect-card-payment.md#process-payment), Stripe receives up-to-date information from the networks and updates `wallet.type`.

### Cancel collection

#### Programmatic cancellation

- [Cancelable (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPCancelable.html)

You can cancel collecting a payment method using the `Cancelable` object returned by the iOS SDK.

#### Customer-initiated cancellation

- [setCustomerCancellation (iOS)](<https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPCollectPaymentIntentConfigurationBuilder.html#/c:objc(cs)SCPCollectPaymentIntentConfigurationBuilder(im)setCustomerCancellation>)
- [CustomerCancellation (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Enums/SCPCustomerCancellation.html)

Smart readers show customers a cancel button by default. You can disable this by setting `customerCancellation` to `.disableIfAvailable`.

Tapping the cancel button cancels the active transaction.

#### Swift

```swift
let collectConfig = try CollectPaymentIntentConfigurationBuilder()
    .setCustomerCancellation(.disableIfAvailable) // turn OFF the cancel button, ON by default
    .build()
Terminal.shared.collectPaymentMethod(paymentIntent: paymentIntent, collectConfig: collectConfig) {
    intentWithPaymentMethod, attachError in
}
```

### Handle events

- [ReaderDisplayDelegate (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Protocols/SCPReaderDisplayDelegate.html)

When collecting a payment method using a reader such as the [Stripe M2](https://docs.stripe.com/terminal/readers/stripe-m2.md), without a built-in display, your app must be able to display events from the payment method collection process to users. These events help users successfully collect payments (for example, retrying a card, trying a different card, or using a different read method).

When a transaction begins, the SDK passes a `ReaderInputOptions` value to your app’s reader display handler, denoting the acceptable types of input (for example, `Swipe`, `Insert`, or `Tap`). In your app’s checkout UI, prompt the user to present a card using one of these options.

During the transaction, the SDK might request your app to display additional prompts (for example, `Retry Card`) to your user by passing a `ReaderDisplayMessage` value to your app’s reader display handler. Make sure your checkout UI displays these messages to the user.

#### Swift

```swift
 // MARK: MobileReaderDelegate - only needed for Bluetooth readers, this is the delegate set during connectReader

 func reader(_ reader: Reader, didRequestReaderInput inputOptions: ReaderInputOptions = []) {
     readerMessageLabel.text = Terminal.stringFromReaderInputOptions(inputOptions)
 }

 func reader(_ reader: Reader, didRequestReaderDisplayMessage displayMessage: ReaderDisplayMessage) {
     readerMessageLabel.text = Terminal.stringFromReaderDisplayMessage(displayMessage)
 }
```

### Collect payments with Tap to Pay on iPhone

When your application is ready to collect a payment, the Stripe Terminal iOS SDK takes over the display to handle the collection process. After calling the [process payment](https://docs.stripe.com/terminal/payments/collect-card-payment.md#process-payment) method, your application remains running, but the iPhone displays a full-screen prompt to the cardholder, instructing them to present their card or NFC-based mobile wallet. If there’s an error reading the card, a prompt for retry displays. A successful presentation returns a success indication, and then control returns to your application.
![Tap to Pay on iPhone payment collection](assets/stripe-terminal-ttpoi-payment-collection.png)

Payment collection

## Confirm the PaymentIntent

- [confirmPaymentIntent (iOS)](<https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)confirmPaymentIntent:completion:>)

After successfully collecting a payment method from the customer, the next step is to confirm the payment with the SDK. When you’re ready to proceed with the payment, call `confirmPaymentIntent` with the updated `PaymentIntent` from the [previous step](https://docs.stripe.com/terminal/payments/collect-card-payment.md#collect-inspect-payment-method).

- For manual capture of payments, a successful `confirmPaymentIntent` call results in a `PaymentIntent` with a status of `requires_capture`.
- For automatic capture of payments, the `PaymentIntent` transitions to a `succeeded` state.

Always confirm PaymentIntents using the Terminal SDK on the client. Server-side confirmation bypasses critical interactions, such as PIN prompts, and might result in transaction failures.

#### Swift

```swift


// Action for a "Checkout" button
func checkoutAction() throws {
  let params = try PaymentIntentParametersBuilder(amount: 1000, currency: "sgd").build()
  Terminal.shared.createPaymentIntent(params) { createResult, createError in
      if let error = createError {
          print("createPaymentIntent failed: \(error)")
      } else if let paymentIntent = createResult {
          print("createPaymentIntent succeeded")
          self.collectCancelable = Terminal.shared.collectPaymentMethod(paymentIntent) { collectResult, collectError in
              if let error = collectError {
                  print("collectPaymentMethod failed: \(error)")
              } else if let collectPaymentMethodPaymentIntent = collectResult {
                  print("collectPaymentMethod succeeded")
                  // ... Confirm the payment
                  self.confirmCancelable = Terminal.shared.confirmPaymentIntent(collectPaymentMethodPaymentIntent) { confirmResult, confirmError in
                      if let error = confirmError {
                          print("confirmPaymentIntent failed: \(error)")
                      } else if let confirmedPaymentIntent = confirmResult {
                          print("confirmPaymentIntent succeeded")
                          // Notify your backend to capture the PaymentIntent
                          if let stripeId = confirmedPaymentIntent.stripeId {
                              APIClient.shared.capturePaymentIntent(stripeId) { captureError in
                                  if let error = captureError {
                                      print("capture failed: \(error)")
                                  } else {
                                      print("capture succeeded")
                                  }
                              }
                          } else {
                              print("Payment collected offline");
                          }
                      }
                  }
              }
          }
      }
  }
```

You must manually capture a PaymentIntent within 2 days or the authorization expires and funds are released to the customer.

### Handle failures

- [ConfirmPaymentIntentError (iOS)](<https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPConfirmPaymentIntentError.html#/c:objc(cs)SCPConfirmPaymentIntentError(py)paymentIntent>)

When confirming a payment fails, the SDK returns an error that includes the updated `PaymentIntent`. Your application needs to inspect the `PaymentIntent` to decide how to deal with the error.

| PaymentIntent Status      | Meaning                                                     | Resolution                                                                                                                                      |
| ------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `requires_payment_method` | Payment method declined                                     | Try collecting a different payment method by calling `collectPaymentMethod` again with the same `PaymentIntent`.                                |
| `requires_confirmation`   | Temporary connectivity problem                              | Call `confirmPaymentIntent` again with the same `PaymentIntent` to retry the request.                                                           |
| `PaymentIntent` is `nil`  | Request to Stripe timed out, unknown `PaymentIntent` status | Retry confirming the original `PaymentIntent`. Don’t create a new one, because that might result in multiple authorizations for the cardholder. |

If you encounter multiple, consecutive timeouts, there might be a problem with your connectivity. Make sure that your app can communicate with the internet.

### Avoid double charges

The `PaymentIntent` object enables money movement at Stripe—use a single `PaymentIntent` to represent a transaction.

Re-use the same `PaymentIntent` after a card is declined (for example, if it has insufficient funds), so your customer can try again with a different card.

If you edit the `PaymentIntent`, you must call `collectPaymentMethod` to update the payment information on the reader.

A `PaymentIntent` must be in the `requires_payment_method` state before Stripe can confirm it. An authorized, captured, or canceled `PaymentIntent` can’t be confirmed by a reader.

## Capture the payment [Server-side]

If you defined `capture_method` as `manual` during `PaymentIntent` creation in [Step 1](https://docs.stripe.com/terminal/payments/collect-card-payment.md#create-payment), the SDK returns an authorized but not captured `PaymentIntent` to your application. Learn more about the difference between [authorization and capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md).

When your app receives a confirmed `PaymentIntent` from the SDK, make sure it notifies your backend to capture the payment. Create an endpoint on your backend that accepts a `PaymentIntent` ID and sends a request to the Stripe API to capture it:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.capture(
  "{{PAYMENT_INTENT_ID}}",
);
```

A successful `capture` call results in a `PaymentIntent` with a status of `succeeded`.

To make sure the application fee captured is correct for connected accounts, inspect each `PaymentIntent` and modify the application fee, if needed, before manually capturing the payment.

### Reconcile payments

To monitor the payments activity of your business, you might want to reconcile PaymentIntents with your internal orders system on your server at the end of a day’s activity.

A `PaymentIntent` that retains a `requires_capture` status might represent two things:

**Unnecessary authorization on your customer’s card statement**

- Cause: User abandons your app’s checkout flow in the middle of a transaction
- Solution: If the uncaptured `PaymentIntent` isn’t associated with a completed order on your server, you can [cancel](https://docs.stripe.com/api/payment_intents/cancel.md) it. You can’t use a canceled `PaymentIntent` to perform charges.

**Incomplete collection of funds from a customer**

- Cause: Failure of the request from your app notifying your backend to capture the payment
- Solution: If the uncaptured `PaymentIntent` is associated with a completed order on your server, and no other payment has been taken for the order (for example, a cash payment), you can [capture](https://docs.stripe.com/api/payment_intents/capture.md) it.

### Collect tips (US only)

In the US, eligible users can [collect a tip on the receipt when capturing payments](https://docs.stripe.com/terminal/features/collecting-tips/on-receipt.md).

# Android

> This is a Android for when terminal-sdk-platform is android. View the full page at https://docs.stripe.com/terminal/payments/collect-card-payment?terminal-sdk-platform=android.

New to the Payment Intents API? Here are some helpful resources:

- [The Payment Intents API](https://docs.stripe.com/payments/payment-intents.md)
- [The PaymentIntent object](https://docs.stripe.com/api/payment_intents.md)
- [More payment scenarios](https://docs.stripe.com/payments/more-payment-scenarios.md)

Collecting payments with Stripe Terminal requires writing a payment flow in your application. Use the Stripe Terminal SDK to create and update a [PaymentIntent](https://docs.stripe.com/api.md#payment_intents), an object representing a single payment session.

Designed to be robust to failures, the Terminal integration splits the payment process into several steps, each of which can be retried safely:

1. [Create a PaymentIntent](https://docs.stripe.com/terminal/payments/collect-card-payment.md#create-payment).
1. [Process the payment](https://docs.stripe.com/terminal/payments/collect-card-payment.md#process-payment). Authorization on the customer’s card takes place when the SDK processes the payment.
1. (Optional) [Capture the payment](https://docs.stripe.com/terminal/payments/collect-card-payment.md#capture-payment)

## Create a PaymentIntent [Client-side] [Server-side]

The first step when collecting payments is to start the payment flow. When a customer begins checking out, your application must create a `PaymentIntent` object. This represents a new payment session on Stripe.

- [createPaymentIntent (Android)](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/create-payment-intent.html)

You can create a `PaymentIntent` on the client or server.

Use [test amounts](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards) to try producing different results. An amount ending in `00` results in an approved payment.

> #### Don't recreate PaymentIntents for declined cards
>
> Don’t recreate a PaymentIntent if a card is declined. Instead, re-use the same PaymentIntent to help [avoid double charges](https://docs.stripe.com/terminal/payments/collect-card-payment.md#avoiding-double-charges).

### Client-side

Create a `PaymentIntent` from your client:

> If your app is connected to the Verifone P400, you can’t create a PaymentIntent from the Android SDK. Instead, you must [create the PaymentIntent server-side](https://docs.stripe.com/terminal/payments/collect-card-payment.md#create-server-side), and retrieve the PaymentIntent in your app using the `Terminal.retrievePaymentIntent` method in the SDK.

#### Kotlin

```kotlin
val params = PaymentIntentParameters.Builder()
    .setAmount(1000)
    .setCurrency("sgd")
    .build()
Terminal.getInstance().createPaymentIntent(
    params,
    object : PaymentIntentCallback {
        override fun onSuccess(paymentIntent: PaymentIntent) {
            // Placeholder for handling successful operation
        }

        override fun onFailure(e: TerminalException) {
            // Placeholder for handling exception
        }
    }
)
```

### Server-side

You can create the `PaymentIntent` on your server if the information required to start a payment isn’t readily available in your app.

The following example shows how to create a `PaymentIntent` on your server:

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const intent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: "sgd",
  payment_method_types: ["card_present"],
  capture_method: "manual",
});
```

For Terminal payments, the `payment_method_types` parameter must include `card_present`.

You can control the payment flow as follows:

- To fully control the payment flow for `card_present` payments, set the `capture_method` to `manual`. This allows you to add a reconciliation step before finalizing the payment.
- To authorize and capture payments in one step, set the `capture_method` to `automatic`.

To accept payments in Australia, you need to set `capture_method` to `automatic` or `manual_preferred`. For more details, visit our [Australia documentation](https://docs.stripe.com/terminal/payments/regional.md?integration-country=AU). To accept Interac payments in Canada, you must also include `interac_present` in `payment_method_types`. For more details, visit our [Canada documentation](https://docs.stripe.com/terminal/payments/regional.md?integration-country=CA).

The `PaymentIntent` contains a [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret), a key that’s unique to the individual `PaymentIntent`. To use the client secret, you must obtain it from the `PaymentIntent` on your server and [pass it to the client side](https://docs.stripe.com/payments/payment-intents.md#passing-to-client).

#### Node.js

```javascript
const express = require("express");
const app = express();

app.post("/create_payment_intent", async (req, res) => {
  const intent = // ... Fetch or create the PaymentIntent
    res.json({ client_secret: intent.client_secret });
});

app.listen(3000, () => {
  console.log("Running on port 3000");
});
```

- [retrievePaymentIntent (Android)](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/retrieve-payment-intent.html)

To retrieve a `PaymentIntent`, use the client secret to call `retrievePaymentIntent`.

After you retrieve the `PaymentIntent`, use it to call `processPaymentIntent`.

#### Kotlin

```kotlin
Terminal.getInstance().retrievePaymentIntent(
    clientSecret,
    object : PaymentIntentCallback {
        override fun onSuccess(paymentIntent: PaymentIntent) {
            // Placeholder for handling successful operation
        }

        override fun onFailure(e: TerminalException) {
            // Placeholder for handling exception
        }
    }
)
```

## Process the payment [Client-side]

You can process a payment immediately with the card presented by a customer, or instead inspect card details before proceeding to process the payment. For most use cases, we recommend processing immediately, because it’s a simpler integration with fewer API calls. However, if you want to insert your own business logic before authorizing the card, use the two-step collect-and-confirm flow.

#### Process immediately

After you create a PaymentIntent, the next step is to process the payment. The reader prompts the customer to insert or tap their card and then attempts to authorize the payment.

- [processPaymentIntent (Android)](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/process-payment-intent.html)

While processing a payment, cardholder might take a few seconds to get their card from their wallet or pose a question to the operator during payment.

#### Kotlin

```kotlin
val cancelable = Terminal.getInstance().processPaymentIntent(
    paymentIntent = paymentIntent,
    collectConfig = CollectPaymentIntentConfiguration.Builder().build(),
    confirmConfig = ConfirmPaymentIntentConfiguration.Builder().build(),
    callback = object : PaymentIntentCallback {
        override fun onSuccess(paymentIntent: PaymentIntent) {
            println("processPaymentIntent succeeded")
            // Notify your backend to capture the PaymentIntent
            if (paymentIntent.id != null) {
                ApiClient.capturePaymentIntent(paymentIntent.id) { error ->
                    if (error != null) {
                        println("capturePaymentIntent failed: $error")
                    } else {
                        println("capturePaymentIntent succeeded")
                    }
                }
            } else {
                println("Payment collected offline")
            }
        }

        override fun onFailure(e: TerminalException) {
            println("processPaymentIntent failed: $e")
        }
    }
)
```

### Cancel collection

#### Programmatic cancellation

- [Cancelable (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.callable/-cancelable/index.html)

You can cancel processing a PaymentIntent using the `Cancelable` object returned by the Android SDK.

#### Customer-initiated cancellation

- [setCustomerCancellation (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-collect-payment-intent-configuration/-builder/set-customer-cancellation.html)
- [Customer Cancellation (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-customer-cancellation/index.html)

Smart readers show customers a cancel button by default. You can disable this by setting `customerCancellation` to `DISABLE_IF_AVAILABLE`.

Tapping the cancel button cancels the active transaction.

#### Kotlin

```kotlin
Terminal.getInstance().collectPaymentMethod(
    paymentIntent,
    object : PaymentIntentCallback {
        override fun onSuccess(paymentIntent: PaymentIntent) {
            // Placeholder for handling successful operation
        }

        override fun onFailure(e: TerminalException) {
            // Placeholder for handling exception
        }
    },CollectPaymentIntentConfiguration.Builder()
        .setCustomerCancellation(CustomerCancellation.DISABLE_IF_AVAILABLE) // turn OFF the cancel button, ON by default
        .build(),
)
```

### Handle events

- [MobileReaderListener (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.callable/-mobile-reader-listener/index.html)

When collecting a payment method using a reader such as the [Stripe M2](https://docs.stripe.com/terminal/readers/stripe-m2.md), without a built-in display, your app must be able to display events from the payment method collection process to users. These events help users successfully collect payments (for example, retrying a card, trying a different card, or using a different read method).

When a transaction begins, the SDK passes a `ReaderInputOptions` value to your app’s reader display handler, denoting the acceptable types of input (for example, `Swipe`, `Insert`, or `Tap`). In your app’s checkout UI, prompt the user to present a card using one of these options.

During the transaction, the SDK might request your app to display additional prompts (for example, `Retry Card`) to your user by passing a `ReaderDisplayMessage` value to your app’s reader display handler. Make sure your checkout UI displays these messages to the user.

#### Kotlin

```kotlin
class ReaderActivity : AppCompatActivity(), MobileReaderListener {
    // ...

    override fun onRequestReaderInput(options: ReaderInputOptions) {
        Toast.makeText(activity, options.toString(), Toast.LENGTH_SHORT).show()
    }

    override fun onRequestReaderDisplayMessage(message: ReaderDisplayMessage) {
        Toast.makeText(activity, message.toString(), Toast.LENGTH_SHORT).show()
    }

    // ...
}
```

### Collect payments with Tap to Pay on Android

When your application is ready to collect a payment, the Stripe Terminal Android SDK takes over the display to handle the collection process. After calling the [process payment](https://docs.stripe.com/terminal/payments/collect-card-payment.md#process-payment) method, your application remains running. The Android device displays a full-screen prompt to the cardholder, instructing them to present their card or NFC-based mobile wallet. If there’s an error reading the card, a prompt for retry displays. A successful presentation returns a success indication, and then control returns to your application.
![Tap to Pay on Android payment collection](assets/stripe-terminal-ttpa-payment-collection.png)

Payment collection

- For manual capture of payments, a successful `processPaymentIntent` call results in a `PaymentIntent` with a status of `requires_capture`.
- For automatic capture of payments, the `PaymentIntent` transitions to a `succeeded` state.

You must manually capture a PaymentIntent within 2 days or the authorization expires and funds are released to the customer.

### Handle failures

- [TerminalException (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-terminal-exception/index.html)

When processing a payment fails, the SDK returns an error that includes the updated `PaymentIntent` if it was declined by stripe. Your application needs to inspect the `PaymentIntent` to decide how to deal with the error.

| PaymentIntent status      | Meaning                                                     | Resolution                                                                                                                                      |
| ------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `requires_payment_method` | Payment method declined                                     | Try collecting a different payment method by calling `processPaymentIntent` again with the same `PaymentIntent`.                                |
| `requires_confirmation`   | Temporary connectivity problem                              | Call `processPaymentIntent` again with the same `PaymentIntent` to retry the request.                                                           |
| `PaymentIntent` is `nil`  | Request to Stripe timed out, unknown `PaymentIntent` status | Retry processing the original `PaymentIntent`. Don’t create a new one, because that might result in multiple authorizations for the cardholder. |

If you encounter multiple, consecutive timeouts, there might be a problem with your connectivity. Make sure that your app can communicate with the internet.

### Avoid double charges

The `PaymentIntent` object enables money movement at Stripe—use a single `PaymentIntent` to represent a transaction.

Re-use the same `PaymentIntent` after a card is declined (for example, if it has insufficient funds), so your customer can try again with a different card.

If you edit the `PaymentIntent`, you must call `processPaymentIntent` to update the payment information on the reader.

A `PaymentIntent` must be in the `requires_payment_method` state before Stripe can process it. An authorized, captured, or canceled `PaymentIntent` can’t be processed by a reader.

#### Collect, inspect, and confirm

After you create a PaymentIntent, the next step is to process the payment. The reader prompts the customer to insert or tap their card and then creates a PaymentMethod.

## Collect a PaymentMethod

- [collectPaymentMethod (Android)](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/collect-payment-method.html)

After you’ve created a `PaymentIntent`, the next step is to collect a payment method with the SDK.

To collect a payment method, your app needs to be connected to a reader. The connected reader waits for a card to be presented after your app calls `collectPaymentMethod`.

#### Kotlin

```kotlin
val cancelable = Terminal.getInstance().collectPaymentMethod(
    paymentIntent,
    object : PaymentIntentCallback {
        override fun onSuccess(paymentIntent: PaymentIntent) {
            // Placeholder for handling successful operation
        }

        override fun onFailure(e: TerminalException) {
            // Placeholder for handling exception
        }
    }
)
```

This method collects encrypted payment method data using the connected card reader, and associates the encrypted data with the local `PaymentIntent`.

### Optionally inspect payment method details

- [CollectPaymentIntentConfiguration (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-collect-payment-intent-configuration/index.html)
- [CardPresentDetails (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-card-present-details/index.html)

For advanced use cases, you can examine the payment method details of the presented card and perform your own business logic prior to authorization.

Use the `updatePaymentIntent` parameter in `CollectPaymentIntentConfiguration` to attach a `PaymentMethod` to the server-side `PaymentIntent`. This data is returned in the `collectPaymentMethod` response.

#### Kotlin

```kotlin
val collectConfig = CollectPaymentIntentConfiguration.Builder()
    .updatePaymentIntent(true)
    .build()

val cancelable = Terminal.getInstance().collectPaymentMethod(paymentIntent,
    object : PaymentIntentCallback {
        override fun onSuccess(paymentIntent: PaymentIntent) {
            val pm = paymentIntent.paymentMethod
            val card = pm?.cardPresentDetails ?: pm?.interacPresentDetails

            // Placeholder for business logic on card before confirming paymentIntent
        }

        override fun onFailure(e: TerminalException) {
            // Placeholder for handling exception
        }
    }
)
```

This method attaches the collected encrypted payment method data with an update to the `PaymentIntent` object. It doesn’t require authorization until you confirm the payment. This advanced use case isn’t supported on the Verifone P400.

After payment method collection, you must authorize or cancel the payment within 30 seconds.

If the SDK is [operating offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md), the `paymentMethod` field isn’t present in the `PaymentIntent` object.

You can access attributes like card brand, funding, and other useful data at this point.

Stripe attempts to detect whether a mobile wallet is used in a transaction as shown in the `wallet.type` attribute. However, the attribute isn’t populated if the card’s issuing bank doesn’t support reader-driven identification of a mobile wallet, so accurate detection isn’t guaranteed. After authorization and when you [process the payment](https://docs.stripe.com/terminal/payments/collect-card-payment.md#process-payment), Stripe receives up-to-date information from the networks and updates `wallet.type`.

### Cancel collection

#### Programmatic cancellation

- [Cancelable (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.callable/-cancelable/index.html)

You can cancel collecting a payment method using the `Cancelable` object returned by the Android SDK.

#### Customer-initiated cancellation

- [setCustomerCancellation (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-collect-payment-intent-configuration/-builder/set-customer-cancellation.html)
- [Customer Cancellation (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-customer-cancellation/index.html)

Smart readers show customers a cancel button by default. You can disable this by setting `customerCancellation` to `DISABLE_IF_AVAILABLE`.

Tapping the cancel button cancels the active transaction.

#### Kotlin

```kotlin
Terminal.getInstance().collectPaymentMethod(
    paymentIntent,
    object : PaymentIntentCallback {
        override fun onSuccess(paymentIntent: PaymentIntent) {
            // Placeholder for handling successful operation
        }

        override fun onFailure(e: TerminalException) {
            // Placeholder for handling exception
        }
    },CollectPaymentIntentConfiguration.Builder()
        .setCustomerCancellation(CustomerCancellation.DISABLE_IF_AVAILABLE) // turn OFF the cancel button, ON by default
        .build(),
)
```

### Handle events

- [MobileReaderListener (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.callable/-mobile-reader-listener/index.html)

When collecting a payment method using a reader such as the [Stripe M2](https://docs.stripe.com/terminal/readers/stripe-m2.md), without a built-in display, your app must be able to display events from the payment method collection process to users. These events help users successfully collect payments (for example, retrying a card, trying a different card, or using a different read method).

When a transaction begins, the SDK passes a `ReaderInputOptions` value to your app’s reader display handler, denoting the acceptable types of input (for example, `Swipe`, `Insert`, or `Tap`). In your app’s checkout UI, prompt the user to present a card using one of these options.

During the transaction, the SDK might request your app to display additional prompts (for example, `Retry Card`) to your user by passing a `ReaderDisplayMessage` value to your app’s reader display handler. Make sure your checkout UI displays these messages to the user.

#### Kotlin

```kotlin
class ReaderActivity : AppCompatActivity(), MobileReaderListener {
    // ...

    override fun onRequestReaderInput(options: ReaderInputOptions) {
        Toast.makeText(activity, options.toString(), Toast.LENGTH_SHORT).show()
    }

    override fun onRequestReaderDisplayMessage(message: ReaderDisplayMessage) {
        Toast.makeText(activity, message.toString(), Toast.LENGTH_SHORT).show()
    }

    // ...
}
```

### Collect payments with Tap to Pay on Android

When your application is ready to collect a payment, the Stripe Terminal Android SDK takes over the display to handle the collection process. After calling the [process payment](https://docs.stripe.com/terminal/payments/collect-card-payment.md#process-payment) method, your application remains running. The Android device displays a full-screen prompt to the cardholder, instructing them to present their card or NFC-based mobile wallet. If there’s an error reading the card, a prompt for retry displays. A successful presentation returns a success indication, and then control returns to your application.
![Tap to Pay on Android payment collection](assets/stripe-terminal-ttpa-payment-collection.png)

Payment collection

## Confirm the PaymentIntent

- [confirmPaymentIntent (Android)](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/confirm-payment-intent.html)

After successfully collecting a payment method from the customer, the next step is to confirm the payment with the SDK. When you’re ready to proceed with the payment, call `confirmPaymentIntent` with the updated `PaymentIntent` from the [previous step](https://docs.stripe.com/terminal/payments/collect-card-payment.md#collect-inspect-payment-method).

- For manual capture of payments, a successful `confirmPaymentIntent` call results in a `PaymentIntent` with a status of `requires_capture`.
- For automatic capture of payments, the `PaymentIntent` transitions to a `succeeded` state.

Always confirm PaymentIntents using the Terminal SDK on the client. Server-side confirmation bypasses critical interactions, such as PIN prompts, and might result in transaction failures.

#### Kotlin

```kotlin
val cancelable = Terminal.getInstance().confirmPaymentIntent(
    paymentIntent,
    object : PaymentIntentCallback {
        override fun onSuccess(paymentIntent: PaymentIntent) {
            // Placeholder handling successful operation
        }

        override fun onFailure(e: TerminalException) {
            // Placeholder for handling exception
        }
    }
)
```

You must manually capture a PaymentIntent within 2 days or the authorization expires and funds are released to the customer.

### Handle failures

- [TerminalException (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-terminal-exception/index.html)

When confirming a payment fails, the SDK returns an error that includes the updated `PaymentIntent`. Your application needs to inspect the `PaymentIntent` to decide how to deal with the error.

| PaymentIntent Status      | Meaning                                                     | Resolution                                                                                                                                      |
| ------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `requires_payment_method` | Payment method declined                                     | Try collecting a different payment method by calling `collectPaymentMethod` again with the same `PaymentIntent`.                                |
| `requires_confirmation`   | Temporary connectivity problem                              | Call `confirmPaymentIntent` again with the same `PaymentIntent` to retry the request.                                                           |
| `PaymentIntent` is `nil`  | Request to Stripe timed out, unknown `PaymentIntent` status | Retry confirming the original `PaymentIntent`. Don’t create a new one, because that might result in multiple authorizations for the cardholder. |

If you encounter multiple, consecutive timeouts, there might be a problem with your connectivity. Make sure that your app can communicate with the internet.

### Avoid double charges

The `PaymentIntent` object enables money movement at Stripe—use a single `PaymentIntent` to represent a transaction.

Re-use the same `PaymentIntent` after a card is declined (for example, if it has insufficient funds), so your customer can try again with a different card.

If you edit the `PaymentIntent`, you must call `collectPaymentMethod` to update the payment information on the reader.

A `PaymentIntent` must be in the `requires_payment_method` state before Stripe can confirm it. An authorized, captured, or canceled `PaymentIntent` can’t be confirmed by a reader.

## Capture the payment [Server-side]

If you defined `capture_method` as `manual` during `PaymentIntent` creation in [Step 1](https://docs.stripe.com/terminal/payments/collect-card-payment.md#create-payment), the SDK returns an authorized but not captured `PaymentIntent` to your application. Learn more about the difference between [authorization and capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md).

When your app receives a confirmed `PaymentIntent` from the SDK, make sure it notifies your backend to capture the payment. Create an endpoint on your backend that accepts a `PaymentIntent` ID and sends a request to the Stripe API to capture it:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.capture(
  "{{PAYMENT_INTENT_ID}}",
);
```

A successful `capture` call results in a `PaymentIntent` with a status of `succeeded`.

To make sure the application fee captured is correct for connected accounts, inspect each `PaymentIntent` and modify the application fee, if needed, before manually capturing the payment.

### Reconcile payments

To monitor the payments activity of your business, you might want to reconcile PaymentIntents with your internal orders system on your server at the end of a day’s activity.

A `PaymentIntent` that retains a `requires_capture` status might represent two things:

**Unnecessary authorization on your customer’s card statement**

- Cause: User abandons your app’s checkout flow in the middle of a transaction
- Solution: If the uncaptured `PaymentIntent` isn’t associated with a completed order on your server, you can [cancel](https://docs.stripe.com/api/payment_intents/cancel.md) it. You can’t use a canceled `PaymentIntent` to perform charges.

**Incomplete collection of funds from a customer**

- Cause: Failure of the request from your app notifying your backend to capture the payment
- Solution: If the uncaptured `PaymentIntent` is associated with a completed order on your server, and no other payment has been taken for the order (for example, a cash payment), you can [capture](https://docs.stripe.com/api/payment_intents/capture.md) it.

### Collect tips (US only)

In the US, eligible users can [collect a tip on the receipt when capturing payments](https://docs.stripe.com/terminal/features/collecting-tips/on-receipt.md).

# React Native

> This is a React Native for when terminal-sdk-platform is react-native. View the full page at https://docs.stripe.com/terminal/payments/collect-card-payment?terminal-sdk-platform=react-native.

New to the Payment Intents API? Here are some helpful resources:

- [The Payment Intents API](https://docs.stripe.com/payments/payment-intents.md)
- [The PaymentIntent object](https://docs.stripe.com/api/payment_intents.md)
- [More payment scenarios](https://docs.stripe.com/payments/more-payment-scenarios.md)

Collecting payments with Stripe Terminal requires writing a payment flow in your application. Use the Stripe Terminal SDK to create and update a [PaymentIntent](https://docs.stripe.com/api.md#payment_intents), an object representing a single payment session.

Designed to be robust to failures, the Terminal integration splits the payment process into several steps, each of which can be retried safely:

1. [Create a PaymentIntent](https://docs.stripe.com/terminal/payments/collect-card-payment.md#create-payment).
1. [Process the payment](https://docs.stripe.com/terminal/payments/collect-card-payment.md#process-payment). Authorization on the customer’s card takes place when the SDK processes the payment.
1. (Optional) [Capture the payment](https://docs.stripe.com/terminal/payments/collect-card-payment.md#capture-payment)

## Create a PaymentIntent [Client-side] [Server-side]

The first step when collecting payments is to start the payment flow. When a customer begins checking out, your application must create a `PaymentIntent` object. This represents a new payment session on Stripe.

- [createPaymentIntent (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#createPaymentIntent)

You can create a `PaymentIntent` on the client or server.

Use [test amounts](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards) to try producing different results. An amount ending in `00` results in an approved payment.

> #### Don't recreate PaymentIntents for declined cards
>
> Don’t recreate a PaymentIntent if a card is declined. Instead, re-use the same PaymentIntent to help [avoid double charges](https://docs.stripe.com/terminal/payments/collect-card-payment.md#avoiding-double-charges).

### Client-side

Create a `PaymentIntent` from your client:

> If your app is connected to the Verifone P400, you can’t create a PaymentIntent from the React Native SDK. Instead, you must [create the PaymentIntent server-side](https://docs.stripe.com/terminal/payments/collect-card-payment.md#create-server-side), and retrieve the PaymentIntent in your app using the `retrievePaymentIntent` method in the SDK.

```js
const { error, paymentIntent } = await createPaymentIntent({
  amount: 1000,
  currency: "sgd",
});
```

### Server-side

You can create the `PaymentIntent` on your server if the information required to start a payment isn’t readily available in your app.

The following example shows how to create a `PaymentIntent` on your server:

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const intent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: "sgd",
  payment_method_types: ["card_present"],
  capture_method: "manual",
});
```

For Terminal payments, the `payment_method_types` parameter must include `card_present`.

You can control the payment flow as follows:

- To fully control the payment flow for `card_present` payments, set the `capture_method` to `manual`. This allows you to add a reconciliation step before finalizing the payment.
- To authorize and capture payments in one step, set the `capture_method` to `automatic`.

To accept payments in Australia, you need to set `capture_method` to `automatic` or `manual_preferred`. For more details, visit our [Australia documentation](https://docs.stripe.com/terminal/payments/regional.md?integration-country=AU). To accept Interac payments in Canada, you must also include `interac_present` in `payment_method_types`. For more details, visit our [Canada documentation](https://docs.stripe.com/terminal/payments/regional.md?integration-country=CA).

The `PaymentIntent` contains a [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret), a key that’s unique to the individual `PaymentIntent`. To use the client secret, you must obtain it from the `PaymentIntent` on your server and [pass it to the client side](https://docs.stripe.com/payments/payment-intents.md#passing-to-client).

#### Node.js

```javascript
const express = require("express");
const app = express();

app.post("/create_payment_intent", async (req, res) => {
  const intent = // ... Fetch or create the PaymentIntent
    res.json({ client_secret: intent.client_secret });
});

app.listen(3000, () => {
  console.log("Running on port 3000");
});
```

- [retrievePaymentIntent (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#retrievePaymentIntent)

To retrieve a `PaymentIntent`, use the client secret to call `retrievePaymentIntent`.

After you retrieve the `PaymentIntent`, use it to call `processPaymentIntent`.

```js
const { paymentIntent, error } = await retrievePaymentIntent(clientSecret);

if (error) {
  // Placeholder for handling exception
  return;
}

// Placeholder for collecting payment method
```

## Process the payment [Client-side]

You can process a payment immediately with the card presented by a customer, or instead inspect card details before proceeding to process the payment. For most use cases, we recommend processing immediately, because it’s a simpler integration with fewer API calls. However, if you want to insert your own business logic before authorizing the card, use the two-step collect-and-confirm flow.

#### Process immediately

After you create a PaymentIntent, the next step is to process the payment. The reader prompts the customer to insert or tap their card and then attempts to authorize the payment.

- [processPaymentIntent (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#processpaymentintent)

While processing a payment, cardholder might take a few seconds to get their card from their wallet or pose a question to the operator during payment.

```js
const { paymentIntent, error } = await processPaymentIntent({
  paymentIntent: paymentIntent,
});

if (error) {
  // Placeholder for handling exception
  return;
}

// Notify your backend to capture the PaymentIntent
```

### Cancel collection

#### Programmatic cancellation

- [cancelProcessPaymentIntent (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#cancelprocesspaymentintent)

You can cancel processing a PaymentIntent by calling `cancelProcessPaymentIntent` in the React Native SDK.

#### Customer-initiated cancellation

- [customerCancellation (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/types/CustomerCancellation.html)

Smart readers show customers a cancel button by default. You can disable this by setting `customerCancellation` to `'disableIfAvailable'`.

Tapping the cancel button cancels the active transaction.

```js
const { paymentIntent, error } = await collectPaymentMethod({
  paymentIntent: paymentIntent,
  customerCancellation: "disableIfAvailable",
});

if (error) {
  // Placeholder for handling exception
}

// Placeholder for processing PaymentIntent
```

### Handle events

- [UserCallbacks (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/index.html#UserCallbacks)

When collecting a payment method using a reader such as the [Stripe M2](https://docs.stripe.com/terminal/readers/stripe-m2.md), without a built-in display, your app must be able to display events from the payment method collection process to users. These events help users successfully collect payments (for example, retrying a card, trying a different card, or using a different read method).

When a transaction begins, the SDK passes a `ReaderInputOptions` value to your app’s reader display handler, denoting the acceptable types of input (for example, `Swipe`, `Insert`, or `Tap`). In your app’s checkout UI, prompt the user to present a card using one of these options.

During the transaction, the SDK might request your app to display additional prompts (for example, `Retry Card`) to your user by passing a `ReaderDisplayMessage` value to your app’s reader display handler. Make sure your checkout UI displays these messages to the user.

```js
useStripeTerminal({
  onDidRequestReaderInput: (options) => {
    // Placeholder for updating your app's checkout UI
    Alert.alert(options.join("/"));
  },
  onDidRequestReaderDisplayMessage: (message) => {
    Alert.alert(message);
  },
});
```

- For manual capture of payments, a successful `processPaymentIntent` call results in a `PaymentIntent` with a status of `requires_capture`.
- For automatic capture of payments, the `PaymentIntent` transitions to a `succeeded` state.

You must manually capture a PaymentIntent within 2 days or the authorization expires and funds are released to the customer.

### Handle failures

- [StripeError (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeError.html)

When processing a payment fails, the SDK returns an error that includes the updated `PaymentIntent` if it was declined by stripe. Your application needs to inspect the `PaymentIntent` to decide how to deal with the error.

| PaymentIntent status      | Meaning                                                     | Resolution                                                                                                                                      |
| ------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `requires_payment_method` | Payment method declined                                     | Try collecting a different payment method by calling `processPaymentIntent` again with the same `PaymentIntent`.                                |
| `requires_confirmation`   | Temporary connectivity problem                              | Call `processPaymentIntent` again with the same `PaymentIntent` to retry the request.                                                           |
| `PaymentIntent` is `nil`  | Request to Stripe timed out, unknown `PaymentIntent` status | Retry processing the original `PaymentIntent`. Don’t create a new one, because that might result in multiple authorizations for the cardholder. |

If you encounter multiple, consecutive timeouts, there might be a problem with your connectivity. Make sure that your app can communicate with the internet.

### Avoid double charges

The `PaymentIntent` object enables money movement at Stripe—use a single `PaymentIntent` to represent a transaction.

Re-use the same `PaymentIntent` after a card is declined (for example, if it has insufficient funds), so your customer can try again with a different card.

If you edit the `PaymentIntent`, you must call `processPaymentIntent` to update the payment information on the reader.

A `PaymentIntent` must be in the `requires_payment_method` state before Stripe can process it. An authorized, captured, or canceled `PaymentIntent` can’t be processed by a reader.

#### Collect, inspect, and confirm

After you create a PaymentIntent, the next step is to process the payment. The reader prompts the customer to insert or tap their card and then creates a PaymentMethod.

## Collect a PaymentMethod

- [collectPaymentMethod (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#collectpaymentmethod)

After you’ve created a `PaymentIntent`, the next step is to collect a payment method with the SDK.

To collect a payment method, your app needs to be connected to a reader. The connected reader waits for a card to be presented after your app calls `collectPaymentMethod`.

```js
const { paymentIntent, error } = await collectPaymentMethod({
  paymentIntent: paymentIntent,
});

if (error) {
  // Placeholder for handling exception
}

// Placeholder for processing PaymentIntent
```

This method collects encrypted payment method data using the connected card reader, and associates the encrypted data with the local `PaymentIntent`.

### Optionally inspect payment method details

- [CollectPaymentMethodParams (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/types/CollectPaymentMethodParams.html)
- [CardPresentDetails (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/types/CardPresentDetails.html)

For advanced use cases, you can examine the payment method details of the presented card and perform your own business logic prior to authorization.

Use the `updatePaymentIntent` parameter to attach a `PaymentMethod` to the server-side `PaymentIntent`. This data is returned in the `collectPaymentMethod` response.

```js
const { paymentIntent, error } = await collectPaymentMethod({
  paymentIntent: paymentIntent,
  updatePaymentIntent: true,
});

if (error) {
  // Placeholder for handling exception
}

// Placeholder for processing PaymentIntent
```

This method attaches the collected encrypted payment method data with an update to the `PaymentIntent` object. It doesn’t require authorization until you confirm the payment. This advanced use case isn’t supported on the Verifone P400.

After payment method collection, you must authorize or cancel the payment within 30 seconds.

If the SDK is [operating offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md), the `paymentMethod` field isn’t present in the `PaymentIntent` object.

You can access attributes like card brand, funding, and other useful data at this point.

Stripe attempts to detect whether a mobile wallet is used in a transaction as shown in the `wallet.type` attribute. However, the attribute isn’t populated if the card’s issuing bank doesn’t support reader-driven identification of a mobile wallet, so accurate detection isn’t guaranteed. After authorization and when you [process the payment](https://docs.stripe.com/terminal/payments/collect-card-payment.md#process-payment), Stripe receives up-to-date information from the networks and updates `wallet.type`.

### Cancel collection

#### Programmatic cancellation

- [cancelCollectPaymentMethod (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#cancelcollectpaymentmethod)

You can cancel payment method collection by calling [cancelCollectPaymentMethod](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#cancelcollectpaymentmethod) in the React Native SDK.

#### Customer-initiated cancellation

- [customerCancellation (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/types/CustomerCancellation.html)

Smart readers show customers a cancel button by default. You can disable this by setting `customerCancellation` to `'disableIfAvailable'`.

Tapping the cancel button cancels the active transaction.

```js
const { paymentIntent, error } = await collectPaymentMethod({
  paymentIntent: paymentIntent,
  customerCancellation: "disableIfAvailable",
});

if (error) {
  // Placeholder for handling exception
}

// Placeholder for processing PaymentIntent
```

### Handle events

- [UserCallbacks (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/index.html#UserCallbacks)

When collecting a payment method using a reader such as the [Stripe M2](https://docs.stripe.com/terminal/readers/stripe-m2.md), without a built-in display, your app must be able to display events from the payment method collection process to users. These events help users successfully collect payments (for example, retrying a card, trying a different card, or using a different read method).

When a transaction begins, the SDK passes a `ReaderInputOptions` value to your app’s reader display handler, denoting the acceptable types of input (for example, `Swipe`, `Insert`, or `Tap`). In your app’s checkout UI, prompt the user to present a card using one of these options.

During the transaction, the SDK might request your app to display additional prompts (for example, `Retry Card`) to your user by passing a `ReaderDisplayMessage` value to your app’s reader display handler. Make sure your checkout UI displays these messages to the user.

```js
useStripeTerminal({
  onDidRequestReaderInput: (options) => {
    // Placeholder for updating your app's checkout UI
    Alert.alert(options.join("/"));
  },
  onDidRequestReaderDisplayMessage: (message) => {
    Alert.alert(message);
  },
});
```

## Confirm the PaymentIntent

- [confirmPaymentIntent (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#confirmpaymentintent)

After successfully collecting a payment method from the customer, the next step is to confirm the payment with the SDK. When you’re ready to proceed with the payment, call `confirmPaymentIntent` with the updated `PaymentIntent` from the [previous step](https://docs.stripe.com/terminal/payments/collect-card-payment.md#collect-inspect-payment-method).

- For manual capture of payments, a successful `confirmPaymentIntent` call results in a `PaymentIntent` with a status of `requires_capture`.
- For automatic capture of payments, the `PaymentIntent` transitions to a `succeeded` state.

Always confirm PaymentIntents using the Terminal SDK on the client. Server-side confirmation bypasses critical interactions, such as PIN prompts, and might result in transaction failures.

```js
const { paymentIntent, error } = await confirmPaymentIntent({
  paymentIntent: paymentIntent,
});

if (error) {
  // Placeholder for handling exception
  return;
}

// Placeholder for notifying your backend to capture paymentIntent.id
```

You must manually capture a PaymentIntent within 2 days or the authorization expires and funds are released to the customer.

### Handle failures

- [StripeError (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeError.html)

When confirming a payment fails, the SDK returns an error that includes the updated `PaymentIntent`. Your application needs to inspect the `PaymentIntent` to decide how to deal with the error.

| PaymentIntent Status      | Meaning                                                     | Resolution                                                                                                                                      |
| ------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `requires_payment_method` | Payment method declined                                     | Try collecting a different payment method by calling `collectPaymentMethod` again with the same `PaymentIntent`.                                |
| `requires_confirmation`   | Temporary connectivity problem                              | Call `confirmPaymentIntent` again with the same `PaymentIntent` to retry the request.                                                           |
| `PaymentIntent` is `nil`  | Request to Stripe timed out, unknown `PaymentIntent` status | Retry confirming the original `PaymentIntent`. Don’t create a new one, because that might result in multiple authorizations for the cardholder. |

If you encounter multiple, consecutive timeouts, there might be a problem with your connectivity. Make sure that your app can communicate with the internet.

### Avoid double charges

The `PaymentIntent` object enables money movement at Stripe—use a single `PaymentIntent` to represent a transaction.

Re-use the same `PaymentIntent` after a card is declined (for example, if it has insufficient funds), so your customer can try again with a different card.

If you edit the `PaymentIntent`, you must call `collectPaymentMethod` to update the payment information on the reader.

A `PaymentIntent` must be in the `requires_payment_method` state before Stripe can confirm it. An authorized, captured, or canceled `PaymentIntent` can’t be confirmed by a reader.

## Capture the payment [Server-side]

If you defined `capture_method` as `manual` during `PaymentIntent` creation in [Step 1](https://docs.stripe.com/terminal/payments/collect-card-payment.md#create-payment), the SDK returns an authorized but not captured `PaymentIntent` to your application. Learn more about the difference between [authorization and capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md).

When your app receives a confirmed `PaymentIntent` from the SDK, make sure it notifies your backend to capture the payment. Create an endpoint on your backend that accepts a `PaymentIntent` ID and sends a request to the Stripe API to capture it:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.capture(
  "{{PAYMENT_INTENT_ID}}",
);
```

A successful `capture` call results in a `PaymentIntent` with a status of `succeeded`.

To make sure the application fee captured is correct for connected accounts, inspect each `PaymentIntent` and modify the application fee, if needed, before manually capturing the payment.

### Reconcile payments

To monitor the payments activity of your business, you might want to reconcile PaymentIntents with your internal orders system on your server at the end of a day’s activity.

A `PaymentIntent` that retains a `requires_capture` status might represent two things:

**Unnecessary authorization on your customer’s card statement**

- Cause: User abandons your app’s checkout flow in the middle of a transaction
- Solution: If the uncaptured `PaymentIntent` isn’t associated with a completed order on your server, you can [cancel](https://docs.stripe.com/api/payment_intents/cancel.md) it. You can’t use a canceled `PaymentIntent` to perform charges.

**Incomplete collection of funds from a customer**

- Cause: Failure of the request from your app notifying your backend to capture the payment
- Solution: If the uncaptured `PaymentIntent` is associated with a completed order on your server, and no other payment has been taken for the order (for example, a cash payment), you can [capture](https://docs.stripe.com/api/payment_intents/capture.md) it.

### Collect tips (US only)

In the US, eligible users can [collect a tip on the receipt when capturing payments](https://docs.stripe.com/terminal/features/collecting-tips/on-receipt.md).
