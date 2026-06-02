<!-- Source URL: https://docs.stripe.com/payments/payment-intents/asynchronous-capture -->
<!-- Fetched: 2026-04-19 -->

# Asynchronous capture

Use Asynchronous Capture to enable faster PaymentIntent confirmations.

Asynchronous capture reduces the latency of PaymentIntent confirmations by making the capture operation take place in the background. After making the capture request, your integration receives a successful response, and Stripe completes payment capture in the backend. To use these faster PaymentIntent captures, set the `capture_method=automatic_async` parameter when confirming a PaymentIntent.

## Opt in to asynchronous capture

To upgrade your existing integration and add support for asynchronous capture, use `automatic_async` as the capture method when creating a PaymentIntent. Specifying the `capture_method=automatic_async` parameter is optional because Stripe enables its functionality by default in the latest version of the API.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 2000,
  currency: "usd",
  payment_method_types: ["card"],
  payment_method: "pm_card_visa",
  confirm: true,
  capture_method: "automatic_async",
});
```

You might need to make additional changes when you opt into asynchronous capture since the API response and some webhooks have different behavior than with other capture methods.

For all payments, the [balance_transaction](https://docs.stripe.com/api/balance_transactions.md) is `null` on the following objects. For Connect payments, the [transfer](https://docs.stripe.com/api/charges/object.md#charge_object-transfer) and [application_fee](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-application_fee_amount) are also `null` on the following objects:

- attached [Charge](https://docs.stripe.com/api/charges/object.md) object of the API response
- [charge.succeeded](https://docs.stripe.com/api/events/types.md#event_types-charge.succeeded) webhook
- [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) webhook

Modified Charge object on the [charge.succeeded](https://docs.stripe.com/api/events/types.md#event_types-charge.succeeded) webhook:

```json
# Charge Object
{
    "id": "ch_123",
    "object": "charge",
    "amount_captured": 1000, # the capture has happened
    "application_fee_amount": 100,
    "captured": true,"balance_transaction": null,  # object might not be created yet, might be shown as nil.
    "transfer": null,             # object might not be created yet, might be shown as nil.
    "application_fee": null,      # object might not be created yet, might be shown as nil.
    ...
}
```

Modified API response and [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) webhook: (different based on [API version](https://docs.stripe.com/upgrades.md))

#### API version 2022-11-15 or later

```json
# PaymentIntent Object
{
  "id": "pi_123",
  "object": "payment_intent",
  "capture_method": "automatic_async",
  "status": "succeeded","latest_charge": "ch_**" # if expanded, this is the Modified Charge object above
}
```

## Listen to webhooks to get notified when additional data is available

> Our SLA for the charge.updated webhook is 1 hour after the successful PaymentIntent confirmation.

You can listen to webhooks to check the status of objects that are initially `null` when using asynchronous capture.

- To get the [balance_transaction](https://docs.stripe.com/api/balance_transactions.md), subscribe to the [charge.updated](https://docs.stripe.com/api/events/types.md#event_types-charge.created) webhook event.
- To get the [application_fee](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-application_fee_amount), subscribe to the [application_fee.created](https://docs.stripe.com/api/events/types.md#event_types-application_fee.created) webhook event.
- To get the [transfer](https://docs.stripe.com/api/charges/object.md#charge_object-transfer), subscribe to the [transfer.created](https://docs.stripe.com/api/events/types.md#event_types-transfer.created) webhook events.

Webhooks for Asynchronous Capture

```json
# charge.updated events
{
  "data": {
    "id": "ch_123",
    "object": "charge",
    "amount": 100,"balance_transaction": "txn_123", # applicable to all charges.
    "transfer": "tr_123",         # applicable to destination charge only.
    "application_fee": "fee_123", # applicable to destination charge only.
    ...
  },
  previous_attributes: {
   "balance_transaction": null, # applicable to all charges.
   "transfer": null,          # applicable to destination charge only.
   "application_fee": null,   # applicable to destination charge only.
  }
}
```

```json
# transfer.created events
{
  "data": {
    "id": "tr_123",
    "object": "transfer",
    "amount": 1000,
    ...
  }
}
```

```json
# application_fee.created events
{
  "data": {
    "id": "fee_123",
    "object": "application_fee",
    "amount": 100,
    ...
  }
}
```
