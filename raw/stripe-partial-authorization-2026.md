<!-- Source URL: https://docs.stripe.com/payments/partial-authorization -->
<!-- Fetched: 2026-05-11 -->

# Partial authorization

Learn how to allow partial payments for card transactions.

Use partial authorizations to request approval for a portion of the originally requested amount for a card transaction when the available balance is insufficient to cover the full amount. This allows your customers to use the available balance on their card (such as a debit card), then use an alternative payment method to pay the remaining balance.

## Before you begin

First, decide how you want to handle the portion of the originally requested amount that isn’t covered by the partial authorization. You can create a separate PaymentIntent for another form of payment, cancel the entire PaymentIntent, or capture only up to the partially authorized amount. Make sure to clearly communicate with your customer about how you’re proceeding with the transaction and any potential impact on them.

> #### Compliance
>
> You’re responsible for your compliance with all applicable laws, regulations, and network rules when using partial authorization. Consult the rules for the card networks that you want to use this feature with to make sure your sales comply with all applicable rules, which vary by network. For example, as of May 2024, American Express restricts usage of the feature to only debit and prepaid and doesn’t permit its use with recurring or cross-border transactions, while Visa requires you to use the feature across card types. The information provided on this page relating to your compliance with these requirements is for your general guidance, and isn’t legal, tax, accounting, or other professional advice. Consult with a professional if you’re unsure about your obligations.

## Availability

> #### IC+ feature
>
> You can access partial authorizations on _IC+ pricing_ (A pricing plan where businesses pay the variable network cost for each transaction plus the Stripe fee rather than a flat rate for all transactions. This pricing model provides more visibility into payments costs). Contact your sales representative or [support](https://support.stripe.com/) to enable this feature.

Partial authorizations have the following restrictions:

- You can only use partial authorizations for online card payments.

- Only Visa, Mastercard, Discover, and Amex support partial authorizations.
- The issuer and card type determine whether they’re supported.
- Due to network restrictions, you can’t capture more than the authorized amount using [overcapture](https://docs.stripe.com/payments/overcapture.md) if a transaction amount has been partially authorized.
- If you process charges on behalf of your Connect account using a [transfer_amount](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-transfer_data-amount), Stripe limits it to the partially authorized amount when the `transfer_amount` is greater than the partially authorized amount.
- Stripe enforces a [minimum charge](https://docs.stripe.com/currencies.md#minimum-and-maximum-charge-amounts) amount on partially authorized charges, declining any PaymentIntent that falls short.

## Use manual capture to create and confirm PaymentIntents

To enable partial authorization for specific PaymentIntents, set `if_available` to the [request_partial_authorization](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-payment_method_options-card-request_partial_authorization) parameter.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 10000,
  currency: "usd",
  payment_method: "pm_card_debit_partialAuthorization",
  payment_method_types: ["card"],
  payment_method_options: {
    card: {
      request_partial_authorization: "if_available",
    },
  },
  capture_method: "manual",
  confirm: true,
  expand: ["latest_charge"],
});
```

### Verify partial authorization status

Review the [payment_method_details](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details) field on the [latest_charge](https://docs.stripe.com/api/charges/object.md) in the PaymentIntent confirmation response to determine whether the networks applied partial authorization for the payment:

- [partial_authorization.status](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-partial_authorization-status): Displays one of the following authorization statuses: `partially_authorized`, `fully_authorized`, `declined`, or `not_requested`.
- [amount_requested](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-amount_requested): Confirms your originally specified request amount.
- [amount_authorized](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-amount_authorized): Determines the authorized amount.

The example response below shows that the transaction is partially authorized for 70 USD, which is less than the originally requested 100 USD.

```json
{
  "id": "pi_foo","amount": 7000,
  "amount_capturable": 7000,
  "amount_received": 0,
  "capture_method": "manual",
  ...
  // if latest_charge is expanded
  "latest_charge": {
    "id": "ch_foo",
    "object": "charge",
    "amount": 7000,
    "captured": false,
    "payment_method_details": {
      "card": {
        "amount_authorized": 7000,"amount_requested": 10000,
        "partial_authorization": {
          "status": "partially_authorized",
        }
      }
    }
  },
  ...
  "status": "requires_capture"
}
```

If the card issuer declines the authorization, this response returns a [card_declined](https://docs.stripe.com/error-codes.md#card-declined) error.

### Capture the partially authorized PaymentIntent

You can capture an authorized PaymentIntent up to the [amount](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-amount) (or [amount_capturable](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-amount_capturable)) that’s returned in the confirmation response.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.capture("pi_foo");
```

A successful capture returns the [PaymentIntent object](https://docs.stripe.com/api/payment_intents/object.md) with updated fields:

```json
{
  "id": "pi_foo","amount": 7000,
  "amount_capturable": 0,
  "amount_received": 7000,
  "capture_method": "manual",
  "latest_charge": "ch_foo",
  ...
  "status": "succeeded",
}
```

## Optional: Use auto-capture to confirm and capture a PaymentIntent

We recommend using partial authorization with manual capture because it allows you to evaluate the partially authorized amount and decide whether to proceed with the capture. However, you can also use partial authorization with auto-capture. If you decide to use this option, proceed with caution; it’s possible that you might capture an insufficient amount.

You can enable partial authorization with auto-capture functionality by setting:

- [request_partial_authorization](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-payment_method_options-card-request_partial_authorization) to `if_available`
- [capture method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-capture_method) to `automatic` (or leave it blank)

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 10000,
  currency: "usd",
  payment_method: "pm_card_debit_partialAuthorization",
  payment_method_types: ["card"],
  payment_method_options: {
    card: {
      request_partial_authorization: "if_available",
    },
  },
  confirm: true,
  expand: ["latest_charge"],
});
```

In the auto-capture flow, your transaction is automatically captured even if it’s partially authorized. The following example response indicates that the transaction is partially authorized and captured for 70 USD, less than the full 100 USD requested.

```json
{
  "id": "pi_foo","amount": 7000,
  "amount_capturable": 0,
  "amount_received": 7000,
  "capture_method": "automatic",
  ...
  // if latest_charge is expanded
  "latest_charge": {
    "id": "ch_foo",
    "object": "charge",
    "amount": 7000,
    "amount_captured": 7000,
    "captured": true,
    "payment_method_details": {
      "card": {
        "amount_authorized": 7000,"amount_requested": 10000,
        "partial_authorization": {
          "status": "partially_authorized",
        }
      }
    }
  },
  ...
  "status": "succeeded"
}
```

## Optional: Increment with partial authorization

You can request partial authorization in the PaymentIntent increment authorization call to get approval for a portion of the requested increment amount when the available balance isn’t enough to cover the full amount.

### Create and confirm a PaymentIntent

Create and confirm a PaymentIntent with incremental authorization enabled using the [request_incremental_authorization](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-payment_method_options-card-request_incremental_authorization) parameter. This enables the incremental authorization feature on the PaymentIntent. See [incremental authorization](https://docs.stripe.com/payments/incremental-authorization.md) to learn more.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 10000,
  currency: "usd",
  payment_method: "pm_card_debit_partialIncrement",
  payment_method_types: ["card"],
  payment_method_options: {
    card: {
      request_incremental_authorization: "if_available",
    },
  },
  capture_method: "manual",
  confirm: true,
  expand: ["latest_charge"],
});
```

The following example response shows that the transaction is fully authorized for 100 USD:

```json
{
  "id": "pi_foo","amount": 10000,
  "amount_capturable": 10000,
  "amount_received": 0,
  "capture_method": "manual",
  ...
  // if latest_charge is expanded
  "latest_charge": {
    "id": "ch_foo",
    "object": "charge",
    "amount": 10000,
    "captured": false,
    "payment_method_details": {
      "card": {
        "amount_authorized": 10000,"amount_requested": 10000,
        "partial_authorization": {
          "status": "not_requested",
        },
        "incremental_authorization": {
          "status": "available"
        }
      }
    }
  },
  ...
  "status": "requires_capture"
}
```

### Enable partial authorization on increment

To enable partial authorization on increments, set [request_partial_authorization](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-payment_method_options-card-request_partial_authorization) to `if_available`:

By default, Stripe retains the opt-in parameter for [request_partial_authorization](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-payment_method_options-card-request_partial_authorization) that you pass during PaymentIntent confirmation for increments. To disable partial authorizations for increments on a PaymentIntent that has opted for partial authorization, set `payment_method_options[card][request_partial_authorization]` to `never`.

The example requests attempts to increment the PaymentIntent amount to 150 USD from 100 USD, but it’s partially authorized to 135 USD.

```bash
curl https://api.stripe.com/v1/payment_intents/pi_foo/increment_authorization \
  -u <<YOUR_SECRET_KEY>>: \
  -d "amount"=15000 \
  -d "payment_method_options[card][request_partial_authorization]"="if_available" \
  -d "expand[]"="latest_charge"
```

The example response below shows the most recent [Charge](https://docs.stripe.com/api/charge/object.md) object associated with the partially authorized [PaymentIntent object](https://docs.stripe.com/api/payment_intents/object.md):

```json
{
  "id": "pi_foo","amount": 13500,
  "amount_capturable": 13500,
  "amount_received": 0,
  "capture_method": "manual",
  ...
  // if latest_charge is expanded
  "latest_charge": {
    "id": "ch_foo",
    "object": "charge",
    "amount": 13500,
    "captured": false,
    "payment_method_details": {
      "card": {
        "amount_authorized": 13500,"amount_requested": 15000,
        "partial_authorization": {
          "status": "partially_authorized",
        }
      }
    }
  },
  ...
  "status": "requires_capture"
}
```

## Test your integration

To trigger a partial authorization while testing, use the partial authorization Stripe test card with any CVC, postal code, and future expiration date. Make sure to set [request_partial_authorization](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-payment_method_options-card-request_partial_authorization) to `if_available` to trigger partial authorization with the test card.

| Test card number | Payment method                       | Description                                                                                                                                                                                                                                                                                      |
| ---------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 4000058400000071 | `pm_card_debit_partialAuthorization` | This card authorizes 70% of the amount specified in the confirmation request rounded down to the nearest unit (for example, cents) with partial authorization requested. Otherwise, it declines it with an insufficient funds error code.                                                        |
| 4000058400000816 | `pm_card_debit_partialIncrement`     | This card fully authorizes the initial authorization. For subsequent increments, this card authorizes 70% of the amount specified in the increment request rounded down to the nearest unit (for example, cents) with partial authorization requested. Otherwise, it returns insufficient funds. |
