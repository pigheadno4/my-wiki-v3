<!-- Source URL: https://docs.stripe.com/payments/flexible-features-migration -->
<!-- Fetched: 2026-05-11 -->

# Migrate to the latest flexible payment scenarios

Adapt your beta advanced payment scenarios to the general release.

Stripe now supports several flexible payment scenarios for non-card-present transactions. If you’ve already integrated the private beta version of any of these features, this guide provides details to upgrade to the general release. For new integrations, use the following guides for the features that interest you:

- [Increment an Authorization](https://docs.stripe.com/payments/incremental-authorization.md)
- [Capture more than the Authorized Amount](https://docs.stripe.com/payments/overcapture.md)
- [Place an Extended Hold on an Online Card Payment](https://docs.stripe.com/payments/extended-authorization.md)
- [Capture a Payment Multiple Times](https://docs.stripe.com/payments/multicapture.md)

We’ve incorporated the following feedback-driven improvements to these features:

- Detailed control over the features at the _PaymentIntent_ (API object that represents your intent to collect payment from a customer, tracking charge attempts and payment state changes throughout the process) level.
- Clearer expectations regarding feature availability and usage after a _confirmation_ (Confirming a PaymentIntent indicates that the customer intends to pay with the current or provided payment method. Upon confirmation, the PaymentIntent attempts to initiate a payment) phase.

Each of the flexible payment features has different requirements from its private beta integration. Choose the feature you need to upgrade and refer to the note at the top for changes and requirements specific to that feature.

# Incremental authorization

> This is a Incremental authorization for when flex-payment-features is incremental-auth. View the full page at https://docs.stripe.com/payments/flexible-features-migration?flex-payment-features=incremental-auth.

> #### Changes from beta
>
> The first step of this integration is now mandatory.

## Request incremental authorization

Your _PaymentIntent_ (API object that represents your intent to collect payment from a customer, tracking charge attempts and payment state changes throughout the process) must include a request for incremental authorization before confirmation.

> This formerly optional step is now mandatory.

### Before

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: "usd",
  payment_method_types: ["card"],
  payment_method: "pm_card_debit_incrementalAuthAuthorized",
  confirm: true,
  capture_method: "manual",
  expand: ["latest_charge"],
  payment_method_options: {
    card: {
      request_incremental_authorization_support: true,
    },
  },
});
```

### After

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: "usd",
  payment_method_types: ["card"],
  payment_method: "pm_card_debit_incrementalAuthAuthorized",
  confirm: true,
  capture_method: "manual",
  expand: ["latest_charge"],
  payment_method_options: {
    card: {
      request_incremental_authorization: "if_available",
    },
  },
});
```

The response now returns the status of the incremental authorization request in the `payment_method_details.card.incremental_authorization.status` property of the [latest_charge](https://docs.stripe.com/api/charges/object.md). The status values is `available` or `unavailable` depending on the customer’s payment method.

### Before

```json
// PaymentIntent Response
{
  "id": "pi_ANipwO3zNfjeWODtRPIg",
  "object": "payment_intent",
  "amount": 1000,
  "amount_capturable": 1000,
  "amount_received": 0,
  ...
  // if latest_charge is expanded
  {
    "latest_charge": {
        "amount": 1000,
        "payment_method_details": {
          "card": {"incremental_authorization_supported": true // or false
          }
        }
        ...
      }
  }
}
```

### After

```json
// PaymentIntent Response
{
  "id": "pi_ANipwO3zNfjeWODtRPIg",
  "object": "payment_intent",
  "amount": 1000,
  "amount_capturable": 1000,
  "amount_received": 0,
  ...
  // if latest_charge is expanded
  {
    "latest_charge": {
        "amount": 1000,
        "payment_method_details": {
          "card": {
            "incremental_authorization": {"status": "available" // or "unavailable"
            }
          }
        }
        ...
      }
  }
}
```

## Incrementally modify the authorized amount

**No changes have been made to this step in comparison to the beta version.**

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.incrementAuthorization(
  "pi_ANipwO3zNfjeWODtRPIg",
  {
    amount: 1500,
  },
);
```

# Overcapture

> This is a Overcapture for when flex-payment-features is overcapture. View the full page at https://docs.stripe.com/payments/flexible-features-migration?flex-payment-features=overcapture.

> #### Changes from beta
>
> The first step of this integration didn’t previously exist, but is now mandatory.

## Request overcapture

Your _PaymentIntent_ (API object that represents your intent to collect payment from a customer, tracking charge attempts and payment state changes throughout the process) must include a request for overcapture before confirmation. The private beta integration for overcapture didn’t include this step because the request parameter didn’t exist.

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
      request_overcapture: "if_available",
    },
  },
});
```

The response returns the status of the overcapture request in the `payment_method_details.card.overcapture.status` property of the [latest_charge](https://docs.stripe.com/api/charges/object.md). The status values is `available` or `unavailable` depending on the customer’s payment method.

```json
// PaymentIntent Response
{
  "id": "pi_ANipwO3zNfjeWODtRPIg",
  "object": "payment_intent",
  "amount": 1000,
  "amount_capturable": 1000,
  "amount_received": 0,
  ...
  // if latest_charge is expanded
  {
    "latest_charge": {
        "amount": 1000,
        "payment_method_details": {
          "card": {
            "overcapture": {"status": "available", // or "unavailable"
                "maximum_amount_capturable": 1200
            }
          }
        }
        ...
      }
  }
}
```

## Capture more than the authorized amount

To capture more than the currently authorized amount on a _PaymentIntent_ (API object that represents your intent to collect payment from a customer, tracking charge attempts and payment state changes throughout the process), use the [capture](https://docs.stripe.com/api/payment_intents/capture.md) endpoint and provide an [amount_to_capture](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-amount_to_capture) up to the [maximum_amount_capturable](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-overcapture).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.capture(
  "pi_ANipwO3zNfjeWODtRPIg",
  {
    amount_to_capture: 1200,
  },
);
```

# Extended authorization

> This is a Extended authorization for when flex-payment-features is extended-auth. View the full page at https://docs.stripe.com/payments/flexible-features-migration?flex-payment-features=extended-auth.

> #### Changes from beta
>
> The first step of this integration didn’t previously exist, but is now mandatory.

## Request extended authorization

Your _PaymentIntent_ (API object that represents your intent to collect payment from a customer, tracking charge attempts and payment state changes throughout the process) must include a request for extended authorization before confirmation. The private beta integration for extended authorization didn’t include this step because the request parameter didn’t exist.

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
      request_extended_authorization: "if_available",
    },
  },
});
```

The response returns the status of the extended authorization request in the `payment_method_details.card.extended_authorization.status` property of the [latest_charge](https://docs.stripe.com/api/charges/object.md). The status values is `available` or `unavailable` depending on the customer’s payment method.

```json
// PaymentIntent Response
{
  "id": "pi_ANipwO3zNfjeWODtRPIg",
  "object": "payment_intent",
  "amount": 1000,
  "amount_capturable": 1000,
  "amount_received": 0,
  ...
  // if latest_charge is expanded
  {
    "latest_charge": {
        "amount": 1000,
        "payment_method_details": {
          "card": {// The field is now always available, even when not using extended authorization
            "capture_before": 1679090539,
            // The response contains information on whether the capture window was extended.
            "extended_authorization": {"status": "enabled", // or "disabled"
            }
          }
        }
        ...
      }
  }
}
```

## Capture the authorization

**No changes have been made to this step compared to the beta version.**

Perform a capture before the date given in the [`capture_before` field](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-capture_before).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.capture(
  "pi_ANipwO3zNfjeWODtRPIg",
  {
    amount_to_capture: 1000,
  },
);
```

# Multicapture

> This is a Multicapture for when flex-payment-features is multicapture. View the full page at https://docs.stripe.com/payments/flexible-features-migration?flex-payment-features=multicapture.

> #### Changes from beta
>
> Migrating from the beta to the generally available version requires several changes impacting all four of the following steps.

## Request multicapture

Your _PaymentIntent_ (API object that represents your intent to collect payment from a customer, tracking charge attempts and payment state changes throughout the process) must include a request for multicapture before confirmation. The private beta integration for multicapture didn’t include this step because the request parameter didn’t exist.

Request access to the feature in the generally available version by passing the `multicapture_migrate_to_ga_from_beta` value in the [Stripe-Version](https://docs.stripe.com/sdks/set-version.md) header before confirming the _PaymentIntent_ (API object that represents your intent to collect payment from a customer, tracking charge attempts and payment state changes throughout the process).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>", {
  // @ts-ignore overrides the pinned API version
  apiVersion: "2026-04-22.preview; multicapture_migrate_to_ga_from_beta",
});

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

The response returns the status of the multicapture request in the `payment_method_details.card.multicapture.status` property of the [latest_charge](https://docs.stripe.com/api/charges/object.md). The status valus is `available` or `unavailable` depending on the customer’s payment method.

```json
// PaymentIntent Response
{
  "id": "pi_ANipwO3zNfjeWODtRPIg",
  "object": "payment_intent","amount": 1000,
  "amount_capturable": 1000,
  "amount_received": 0,
  ...
  // if latest_charge is expanded
  "latest_charge": {"amount": 1000,
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

## Partially capture the authorized amount multiple times

Similar to the beta version, the optional `final_capture` parameter allows you to capture the _PaymentIntent_ (API object that represents your intent to collect payment from a customer, tracking charge attempts and payment state changes throughout the process) multiple times as long as it remains in a [requires_capture state](https://docs.stripe.com/payments/paymentintents/lifecycle.md).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>", {
  // @ts-ignore overrides the pinned API version
  apiVersion: "2026-04-22.preview; multicapture_migrate_to_ga_from_beta",
});

const paymentIntent = await stripe.paymentIntents.capture(
  "pi_ANipwO3zNfjeWODtRPIg",
  {
    amount_to_capture: 700,
    final_capture: false,
    expand: ["latest_charge"],
  },
);
```

```json
// PaymentIntent Response
{
  "id": "pi_ANipwO3zNfjeWODtRPIg",
  "object": "payment_intent","amount": 1000,
  "amount_capturable": 300, // 1000 - 700 = 300
  "amount_received": 700,
  "status": "requires_capture",
  // if latest_charge is expanded
  "latest_charge": {"amount": 1000,
      "amount_captured": 700,
      "amount_refunded": 0,
      ...
    }
  ...
}
```

> In the generally available version, attempting to capture the full remaining amount with the `final_capture` parameter set to `false` returns a 400 error.

### Before

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.capture(
  "pi_ANipwO3zNfjeWODtRPIg",
  {
    amount_to_capture: 300,
    final_capture: false,
    expand: ["latest_charge"],
  },
);
```

```json
// PaymentIntent Response
{
  "id": "pi_ANipwO3zNfjeWODtRPIg",
  "object": "payment_intent","amount": 1000,
  "amount_capturable": 0, // 1000 - 700 - 300 = 0
  "amount_received": 1000,
  "status": "succeeded",
  // if latest_charge is expanded
  "latest_charge": {"amount": 1000,
      "amount_captured": 1000,
      "amount_refunded": 0,
      ...
    }
  ...
}
```

### After

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.capture(
  "pi_ANipwO3zNfjeWODtRPIg",
  {
    amount_to_capture: 300,
    final_capture: false,
    expand: ["latest_charge"],
  },
);
```

```json
// HTTP 400
{
  "message": "can't set final_capture as false when fully capturing a payment intent.",
  "type": "invalid_request_error"
}
```

## Webhooks

Multicapture event generation differs from the beta version, but the content of the events is unchanged.

| Behavior                  | Before                                                                                                  | After                                                                                                   |
| ------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| On each non-final capture | Stripe sends [charge.captured](https://docs.stripe.com/api/events/types.md#event_types-charge.captured) | Stripe sends [charge.updated](https://docs.stripe.com/api/events/types.md#event_types-charge.updated)   |
| On the final capture      | Stripe sends [charge.captured](https://docs.stripe.com/api/events/types.md#event_types-charge.captured) | Stripe sends [charge.captured](https://docs.stripe.com/api/events/types.md#event_types-charge.captured) |

## Refund

In the generally available version, no [refund](https://docs.stripe.com/api/refunds/object.md) is created to represent uncaptured funds for any _PaymentIntent_ (API object that represents your intent to collect payment from a customer, tracking charge attempts and payment state changes throughout the process) where the user passes in `final_capture=true`.

## Choose how to capture more than initially authorized amount

Two of the flexible payment features allow you to capture an amount larger than initially authorized:

- Over capture up to a certain limit ([Capture more than the authorized amount on a payment](https://docs.stripe.com/payments/overcapture.md))
- Increment the existing authorization and then capture the newly authorized amount ([Increment an authorization](https://docs.stripe.com/payments/incremental-authorization.md))

The example below showcases how these features can complement each other in the generally available version.

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
      request_incremental_authorization: "if_available",
      request_overcapture: "if_available",
    },
  },
});
```

```json
// PaymentIntent Response
{
  "object": "payment_intent",
  "amount": 1000,
  ...
  // if latest_charge is expanded
  {
    "latest_charge": {
      "payment_method_details": {
        "card": {
          "incremental_authorization": {"status": "available" // or "unavailable"
          },
          "overcapture": {"status": "available", // or "unavailable"
              "maximum_amount_capturable": 1200
          }
        }
      }
      ...
    }
  }
}
```

Upon _confirmation_ (Confirming a PaymentIntent indicates that the customer intends to pay with the current or provided payment method. Upon confirmation, the PaymentIntent attempts to initiate a payment) of the PaymentIntent, if both features are available, you have options on the next steps to capture a larger amount than initially authorized:

1. Overcapture if the desired amount is equal or below the `maximum_amount_capturable`.
1. Perform an incremental authorization to the desired amount, then capture.
