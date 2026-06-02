<!-- Source URL: https://docs.stripe.com/payments/payment-methods/upgrading-to-automatic-payment-methods -->
<!-- Fetched: 2026-05-01 -->

# Manage default payment methods in the Dashboard

Upgrade your API to manage payment methods in the Dashboard by default.

On August 16, 2023, Stripe [updated the selection process](http://stripe.com/blog/dynamic-payment-methods) for default payment methods that apply to PaymentIntents and SetupIntents created with the [/v1/payment_intents](https://docs.stripe.com/api/payment_intents.md) and [/v1/setup_intents](https://docs.stripe.com/api/setup_intents.md) APIs.

In prior versions of the Stripe API, if you didn’t specify a [payment_method_types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) parameter during the creation request, Stripe would default to using the card payment method for both PaymentIntents and SetupIntents.

Moving forward, Stripe applies eligible payment methods that you manage from your [Dashboard](https://dashboard.stripe.com/settings/payment_methods) to your PaymentIntents and SetupIntents by default if you don’t specify the `payment_method_types` parameter in the creation request.

### Payment methods

By default, Stripe enables cards and other common payment methods. You can turn individual payment methods on or off in the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods). In Checkout, Stripe evaluates the currency and any restrictions, then dynamically presents the supported payment methods to the customer.

To see how your payment methods appear to customers, enter a transaction ID or set an order amount and currency in the Dashboard.

You can enable Apple Pay and Google Pay in your [payment methods settings](https://dashboard.stripe.com/settings/payment_methods). By default, Apple Pay is enabled and Google Pay is disabled. However, in some cases Stripe filters them out even when they’re enabled. We filter Google Pay if you [enable automatic tax](https://docs.stripe.com/tax/checkout.md) without collecting a shipping address.

Checkout’s Stripe-hosted pages don’t need integration changes to enable Apple Pay or Google Pay. Stripe handles these payments the same way as other card payments.

## Update your payment flows

Choose from the upgrade path that matches your current Stripe integration:

#### Elements

If your integration uses Card Element or individual payment method Elements, we recommend migrating to the [Payment Element](https://docs.stripe.com/payments/payment-element/migration.md). This single, unified integration allows you to accept over 25 different payment methods.

### Create the PaymentIntent

In this version of the API, specifying the [automatic_payment_methods.enabled](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-automatic_payment_methods-enabled) parameter is optional. If you don’t specify it, Stripe assumes a value of `true`, which enables its functionality by default.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'usd',
});
```

### Client-side confirmations with Stripe.js

If your integration uses Stripe.js to confirm payments with [confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment) or by [payment method](https://docs.stripe.com/js/payment_intents/payment_method), your existing processes remains the same and requires no further changes.

When you confirm payments, we recommend that you provide the [return_url](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-return_url) parameter. This allows you to accept payment methods that [require redirect](https://docs.stripe.com/payments/payment-methods/payment-method-support.md#additional-api-supportability).

#### HTML + JS

```javascript
const form = document.getElementById('payment-form');

form.addEventListener('submit', async (event) => {
  event.preventDefault();
const {error} = await stripe.confirmPayment({
    //`Elements` instance that was used to create the Payment Element
    elements,
    confirmParams: {
      return_url: 'https://example.com/return_url',
    },
  });

  if (error) {
    // This point will only be reached if there is an immediate error when
    // confirming the payment. Show error to your customer (for example, payment
    // details incomplete)
    const messageContainer = document.querySelector('#error-message');
    messageContainer.textContent = error.message;
  } else {
    // Your customer will be redirected to your `return_url`. For some payment
    // methods like iDEAL, your customer will be redirected to an intermediate
    // site first to authorize the payment, then redirected to the `return_url`.
  }
});
```

#### React

```jsx
import React, {useState} from 'react';
import {
  useStripe,
  useElements,
  PaymentElement,
} from '@stripe/react-stripe-js';

const CheckoutForm = () => {
  const stripe = useStripe();
  const elements = useElements();

  const [errorMessage, setErrorMessage] = useState(null);

  const handleSubmit = async (event) => {
    // We don't want to let default form submission happen here,
    // which would refresh the page.
    event.preventDefault();

    if (!stripe || !elements) {
      // Stripe.js hasn't yet loaded.
      // Make sure to disable form submission until Stripe.js has loaded.
      return;
    }
const {error} = await stripe.confirmPayment({
      //`Elements` instance that was used to create the Payment Element
      elements,
      confirmParams: {
        return_url: 'https://example.com/return_url',
      },
    });


    if (error) {
      // This point will only be reached if there is an immediate error when
      // confirming the payment. Show error to your customer (for example, payment
      // details incomplete)
      setErrorMessage(error.message);
    } else {
      // Your customer will be redirected to your `return_url`. For some payment
      // methods like iDEAL, your customer will be redirected to an intermediate
      // site first to authorize the payment, then redirected to the `return_url`.
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <PaymentElement />
      <button disabled={!stripe}>Submit</button>
      {/* Show error message to your customers */}
      {errorMessage && <div>{errorMessage}</div>}
    </form>
  )
};

export default CheckoutForm;
```

### Server-side confirmation

If you use server-side confirmation, you must use the [return_url](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-return_url) parameter in your integration.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'usd',
  confirm: true,
  payment_method: '{{PAYMENTMETHOD_ID}}',
  return_url: 'https://example.com/return_url',
});
```

Alternatively, you can create the PaymentIntent or SetupIntent with the [automatic_payment_methods.allow_redirects](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-automatic_payment_methods-allow_redirects) parameter set to `never`. This disables the `return_url` requirement on confirmation. You can still manage payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods), but the [payment methods that require redirects](https://docs.stripe.com/payments/bank-redirects.md#bank-redirects-api-support) aren’t eligible.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'usd',
  confirm: true,
  payment_method: '{{PAYMENTMETHOD_ID}}',
  automatic_payment_methods: {
    enabled: true,
    allow_redirects: 'never',
  },
});
```

Lastly, you can create the PaymentIntent or SetupIntent with the [payment_method_types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) parameter. This also disables the `return_url` requirement on confirmation. With this option, you can’t manage payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'usd',
  confirm: true,
  payment_method: '{{PAYMENTMETHOD_ID}}',
  payment_method_types: ['card'],
});
```

#### Checkout and Payment Links

If your integration uses Checkout and Payment Links, refer to the [upgrade your API version guide](https://docs.stripe.com/upgrades.md#how-can-i-upgrade-my-api) to upgrade without making changes to your integration code.

#### API

If your integration confirms payments with the [off_session](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-off_session) parameter set to `true`, your existing processes remains the same and requires no further changes.

Otherwise, you must provide the [return_url](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-return_url) parameter in your integration.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'usd',
  confirm: true,
  payment_method: '{{PAYMENTMETHOD_ID}}',
  return_url: 'https://example.com/return_url',
});
```

Alternatively, you can create the PaymentIntent or SetupIntent with the [automatic_payment_methods.allow_redirects](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-automatic_payment_methods-allow_redirects) parameter set to `never`. This also disables the `return_url` requirement on confirmation. You can still manage payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods), but the payment methods that require redirects won’t be eligible.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'usd',
  confirm: true,
  payment_method: '{{PAYMENTMETHOD_ID}}',
  automatic_payment_methods: {
    enabled: true,
    allow_redirects: 'never',
  },
});
```

Lastly, you can create the PaymentIntent or SetupIntent with the [payment_method_types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) parameter. This also disables the `return_url` requirement on confirmation. With this option, you can’t manage payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'usd',
  confirm: true,
  payment_method: '{{PAYMENTMETHOD_ID}}',
  payment_method_types: ['card'],
});
```
