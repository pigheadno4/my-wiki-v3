<!-- Source URL: https://docs.stripe.com/payments/paypal/import-saved-payment-methods -->
<!-- Fetched: 2026-05-07 -->

# Import saved PayPal payment methods

Learn how to import saved payment methods from PayPal.

You can import PayPal billing agreements created outside of Stripe and reuse them through the Stripe integration.

## Before you begin

Follow the instructions in [Set up future PayPal payments](https://docs.stripe.com/payments/paypal/set-up-future-payments.md#enable-recurring-payments) to enable recurring payments.

## Import PayPal billing agreements to Stripe [Server-side]

You can use the [billing_agreement_id](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-payment_method_options-paypal-billing_agreement_id) parameter of a [Setup Intent](https://docs.stripe.com/api/setup_intents.md) to import an active PayPal billing agreement to Stripe. The resulting [PaymentMethod](https://docs.stripe.com/payments/payment-methods.md#payment-method-object) allows you to charge your existing customer’s PayPal account without the customer needing to reauthorize the billing agreement. This guide shows the steps you need to follow.

PayPal will only send cancellation webhooks for billing agreements created through Stripe.

## Create a Customer [Server-side]

Create a Customer object when your customer creates an account on your business. Associating the ID of the Customer object with your own internal representation of a customer lets you retrieve and use the stored payment method details later. If your customer hasn’t created an account, you can still create a Customer object now and associate it with your internal representation of the customer’s account later.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create();
```

## Attach a payment method [Server-side]

After you create a customer, attach a payment method by creating a Setup Intent.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ["paypal"],
  payment_method_data: {
    type: "paypal",
  },
  payment_method_options: {
    paypal: {
      billing_agreement_id: "B-1234556789",
    },
  },
  return_url: "https://example.com",
  confirm: true,
  usage: "off_session",
  mandate_data: {
    customer_acceptance: {
      type: "offline",
    },
  },
  customer: "cus_XXX",
});
```

## Use your saved payment method [Server-side]

Follow the instructions in [Set up future PayPal payments](https://docs.stripe.com/payments/paypal/set-up-future-payments.md?web-or-mobile=web&payment-ui=stripe-hosted#charge-later) to use this payment method to charge your customers.
