<!-- Source URL: https://docs.stripe.com/payments/au-becs-debit/accept-a-payment -->
<!-- Fetched: 2026-05-02 -->

# Accept an Australia BECS Direct Debit payment

Learn to accept Australia BECS Direct Debit payments.

# Checkout

> This is a Checkout for when payment-ui is checkout. View the full page at https://docs.stripe.com/payments/au-becs-debit/accept-a-payment?payment-ui=checkout.

> Stripe can automatically present the relevant payment methods to your customers by evaluating currency, payment method restrictions, and other parameters.
>
> - Follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=checkout&ui=stripe-hosted) guide to build a Checkout integration that uses [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md).

- If you don’t want to use dynamic payment methods, follow the steps below to manually configure the payment methods in your Checkout integration.

Stripe users in Australia can use [Checkout](https://docs.stripe.com/payments/checkout.md) in payment mode to accept Australia BECS Direct Debit payments.

A [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md) represents the details of your customer’s intent to purchase. You create a Checkout Session when your customer wants to pay for something. After redirecting your customer to a Checkout Session, Stripe presents a payment form where your customer can complete their purchase. When your customer has completed a purchase, they’re redirected back to your site.

## Determine compatibility

**Customer Geography**: Australia

**Supported currencies**: `aud`

**Presentment currencies**: `aud`

**Payment mode**: Yes

**Setup mode**: Yes

**Subscription mode**: Yes

To support BECS Direct Debit payments in Checkout, *Prices* (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) for all line items must be expressed in Australian dollars (currency code `aud`).

## Accept a payment

> Build an integration to [accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?integration=checkout) with Checkout before using this guide.

Use this guide to learn how to enable BECS Direct Debit—it shows the differences between accepting payments using dynamic payment methods and manually configuring payment methods.

### Enable BECS Direct Debit as a payment method

When creating a new [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md), you need to:

1. Add `au_becs_debit` to the list of `payment_method_types`
1. Make sure all your `line_items` use the `aud` currency

#### Stripe-hosted page

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        currency: 'aud',
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: 'payment',
  payment_method_types: ['card', 'au_becs_debit'],
  success_url: 'https://example.com/success',
});
```

#### Full embedded page

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        currency: 'aud',
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: 'payment',
  payment_method_types: ['card', 'au_becs_debit'],
  return_url: 'https://example.com/return',
  ui_mode: 'embedded_page',
});
```

### Fulfill your orders

After accepting a payment, learn how to [fulfill orders](https://docs.stripe.com/checkout/fulfillment.md).

## Test your integration

> You’ll want to use the [BECS Direct Debit test numbers](https://docs.stripe.com/payments/au-becs-debit/accept-a-payment.md#test-integration) when testing your Checkout integration with BECS Direct Debit.

There are several test numbers you can use to make sure your integration is ready for production.

| BSB Number | Account number | Token                                    | Description                                                                                                                                                                                   |
| ---------- | -------------- | ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `000000`   | `000123456`    | `pm_auBecsDebit_success`                 | The PaymentIntent status transitions from `processing` to `succeeded`. The mandate status remains `active`.                                                                                   |
| `000000`   | `900123456`    | `pm_auBecsDebit_successDelayed`          | The PaymentIntent status transitions from `processing` to `succeeded` (with a three-minute delay). The mandate status remains `active`.                                                       |
| `000000`   | `111111113`    | `pm_auBecsDebit_accountClosed`           | The PaymentIntent status transitions from `processing` to `requires_payment_method` with an `account_closed` failure code. The mandate status becomes `inactive`.                             |
| `000000`   | `111111116`    | `pm_auBecsDebit_noAccount`               | The PaymentIntent status transitions from `processing` to `requires_payment_method` with a `no_account` failure code. The mandate status becomes `inactive`.                                  |
| `000000`   | `222222227`    | `pm_auBecsDebit_referToCustomer`         | The PaymentIntent status transitions from `processing` to `requires_payment_method` with a `refer_to_customer` failure code. The mandate status remains `active`.                             |
| `000000`   | `922222227`    | `pm_auBecsDebit_referToCustomerDelayed`  | The PaymentIntent status transitions from `processing` to `requires_payment_method` with a `refer_to_customer` failure code (with a three-minute delay). The mandate status remains `active`. |
| `000000`   | `333333335`    | `pm_auBecsDebit_debitNotAuthorized`      | The PaymentIntent status transitions from `processing` to `requires_payment_method` with a `debit_not_authorized` failure code. The mandate status becomes `inactive`.                        |
| `000000`   | `666666660`    | `pm_auBecsDebit_dispute`                 | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                                                                  |
| `000000`   | `343434343`    | `pm_auBecsDebit_exceedsWeeklyLimit`      | The PaymentIntent fails with a `charge_exceeds_source_limit` error due to the payment amount causing the account to exceed its weekly payment volume limit.                                   |
| `000000`   | `121212121`    | `pm_auBecsDebit_exceedsTransactionLimit` | The PaymentIntent fails with a `charge_exceeds_transaction_limit` error due to the payment amount exceeding the account’s transaction volume limit.                                           |

## Handle refunds and disputes

The refund period for BECS Direct Debit is up to 90 days after the original payment.

Customers can dispute a payment through their bank up to 7 years after the original payment and there is no appeals process.

Learn more about [BECS Direct Debit disputes](https://docs.stripe.com/payments/au-becs-debit.md).

## Optional: Configure customer debit date

You can control the date that Stripe debits a customer’s bank account using the [target date](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-payment_method_options-au_becs_debit-target_date). The target date must be at least three days in the future and no more than 15 days from the current date.

The target date schedules money to leave the customer’s account on the target date.

Target dates that meet one of the following criteria delay the debit until the next available business day:

- Target date falls on a weekend, a bank holiday, or other non-business day.
- Target date is fewer than three business days in the future.

This parameter operates on a best-effort basis. Each customer’s bank might process debits on different dates, depending on local bank holidays or other reasons.

## See also

- [Managing mandates](https://docs.stripe.com/payments/au-becs-debit.md#mandates)
- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment.md)
- [Customizing Checkout](https://docs.stripe.com/payments/checkout/customization.md)
- [Save BECS Direct Debit details for future payments](https://docs.stripe.com/payments/au-becs-debit/set-up-payment.md)
- [Connect payments](https://docs.stripe.com/connect/charges.md)

# Checkout Sessions API

> This is a Checkout Sessions API for when payment-ui is elements and api-integration is checkout. View the full page at https://docs.stripe.com/payments/au-becs-debit/accept-a-payment?payment-ui=elements&api-integration=checkout.

To determine which API meets your business needs, see the [comparison guide](https://docs.stripe.com/payments/checkout-sessions-and-payment-intents-comparison.md).

Use the [Payment Element](https://docs.stripe.com/payments/payment-element.md) to embed a custom Stripe payment form in your website or application and offer payment methods to customers. For advanced configurations and customizations, refer to the [Accept a Payment](https://docs.stripe.com/payments/accept-a-payment.md) integration guide.

## Determine compatibility

**Customer Geography**: Australia

**Supported currencies**: `aud`

**Presentment currencies**: `aud`

**Payment mode**: Yes

**Setup mode**: Yes

**Subscription mode**: Yes

A Checkout Session must satisfy all of the following conditions to support Australia BECS Direct Debit payments:

- *Prices* (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) for all line items must be expressed in Australian dollars (currency code `aud`).

## Set up the server [Server-side]

Use the official Stripe libraries to access the API from your application.

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create or retrieve a customer [Server-side]

To reuse a BECS Direct Debit account for future payments, attach it to an object that represents your customer.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

Create a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/create.md#v2_create_accounts-configuration-customer) or [Customer](https://docs.stripe.com/api/customers/create.md) when your customer creates an account with your business, or when saving a payment method. Associate the object’s ID with your own internal representation of a customer.

Create a new customer or retrieve an existing one to associate with this payment.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const account = await stripe.v2.core.accounts.create({
  contact_email: 'jenny.rosen@example.com',
  display_name: 'Jenny Rosen',
  configuration: {
    customer: {},
  },
  include: ['configuration.customer'],
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customer = await stripe.customers.create({
  name: "Jenny Rosen",
  email: 'jenny.rosen@example.com',
});
```

## Create a Checkout Session [Server-side]

Add an endpoint on your server that creates a [Checkout Session](https://docs.stripe.com/api/checkout/sessions/create.md) and returns its [client secret](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-client_secret) to your front end. A Checkout Session represents your customer’s session as they pay for one-time purchases or subscriptions. Checkout Sessions expire 24 hours after creation.

We recommend using [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md) to dynamically display the most relevant eligible payment methods to each customer to maximize conversion. You can also [manually list payment methods](https://docs.stripe.com/payments/payment-methods/integration-options.md#listing-payment-methods-manually), which disables dynamic payment methods.

#### Manage payment methods from the Dashboard

#### TypeScript

```javascript
import express, {Express} from 'express';

const app: Express = express();

app.post('/create-checkout-session', async (req: Express.Request, res: Express.Response) => {
  const session = await stripe.checkout.sessions.create({
    line_items: [
      {
        price_data: {
          currency: 'aud',
          product_data: {
            name: 'T-shirt',
          },
          unit_amount: 1099,
        },
        quantity: 1,
      },
    ],
    mode: 'payment',
    ui_mode: 'elements',
    return_url: 'https://example.com/return?session_id={CHECKOUT_SESSION_ID}'
  });

  res.json({checkoutSessionClientSecret: session.client_secret});
});

app.listen(3000, () => {
  console.log('Running on port 3000');
});
```

#### Manually list payment methods

#### TypeScript

```javascript
import express, {Express} from 'express';

const app: Express = express();

app.post('/create-checkout-session', async (req: Express.Request, res: Express.Response) => {
  const session = await stripe.checkout.sessions.create({
    line_items: [
      {
        price_data: {
          currency: 'aud',
          product_data: {
            name: 'T-shirt',
          },
          unit_amount: 1099,
        },
        quantity: 1,
      },
    ],
    mode: 'payment',
    ui_mode: 'elements',
    payment_method_types: ['au_becs_debit'],
    return_url: 'https://example.com/return?session_id={CHECKOUT_SESSION_ID}'
  });

  res.json({checkoutSessionClientSecret: session.client_secret});
});

app.listen(3000, () => {
  console.log('Running on port 3000');
});
```

## Set up the front end [Client-side]

#### HTML + JS

Include the Stripe.js script on your checkout page by adding it to the `head` of your HTML file. Always load Stripe.js directly from js.stripe.com to remain PCI compliant. Don’t include the script in a bundle or host a copy of it yourself.

Make sure you’re on the latest Stripe.js version by including the following script tag `<script src=“https://js.stripe.com/dahlia/stripe.js”></script>`. Learn more about [Stripe.js versioning](https://docs.stripe.com/sdks/stripejs-versioning.md).

```html
<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/dahlia/stripe.js"></script>
</head>
```

> Stripe provides an npm package that you can use to load Stripe.js as a module. See the [project on GitHub](https://github.com/stripe/stripe-js). Version [7.0.0](https://www.npmjs.com/package/%40stripe/stripe-js/v/7.0.0) or later is required.

Initialize stripe.js.

```js
// Set your publishable key: remember to change this to your live publishable key in production
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");
```

#### React

Install [React Stripe.js](https://www.npmjs.com/package/@stripe/react-stripe-js) and the [Stripe.js loader](https://www.npmjs.com/package/@stripe/stripe-js) from the npm public registry. You need at least version 5.0.0 for React Stripe.js and version 8.0.0 for the Stripe.js loader.

```bash
npm install --save @stripe/react-stripe-js@^5.0.0 @stripe/stripe-js@^8.0.0
```

Initialize a `stripe` instance on your front end with your publishable key.

```javascript
import { loadStripe } from "@stripe/stripe-js";
const stripe = loadStripe("<<YOUR_PUBLISHABLE_KEY>>");
```

## Initialize Checkout [Client-side]

#### HTML + JS

Call [initCheckoutElementsSdk](https://docs.stripe.com/js/custom_checkout/init), passing in `clientSecret`.

`initCheckoutElementsSdk` returns a [Checkout](https://docs.stripe.com/js/custom_checkout) object that contains data from the Checkout Session and methods to update it.

Read the `total` and `lineItems` from [actions.getSession()](https://docs.stripe.com/js/custom_checkout/session), and display them in your UI. This lets you turn on new features with minimal code changes. For example, adding [manual currency prices](https://docs.stripe.com/payments/custom/localize-prices/manual-currency-prices.md) requires no UI changes if you display the `total`.

```html
<div id="checkout-container"></div>
```

```javascript
const clientSecret = fetch('/create-checkout-session', { method: 'POST' })
  .then((response) => response.json())
  .then((json) => json.client_secret);

const checkout = stripe.initCheckoutElementsSdk({ clientSecret });
const loadActionsResult = await checkout.loadActions();

if (loadActionsResult.type === 'success') {
  const session = loadActionsResult.actions.getSession();
  const checkoutContainer = document.getElementById('checkout-container');

  checkoutContainer.append(JSON.stringify(session.lineItems, null, 2));
  checkoutContainer.append(document.createElement('br'));
  checkoutContainer.append(`Total: ${session.total.total.amount}`);
}
```

#### React

Wrap your application with the [CheckoutElementsProvider](https://docs.stripe.com/js/react_stripe_js/checkout/checkout_provider) component, passing in `clientSecret` and the `stripe` instance.

```jsx
import React from "react";
import { CheckoutElementsProvider } from "@stripe/react-stripe-js/checkout";
import CheckoutForm from "./CheckoutForm";

const clientSecret = fetch('/create-checkout-session', { method: 'POST' })
  .then((response) => response.json())
  .then((json) => json.client_secret);

const App = () => {
  return (
    <CheckoutElementsProvider stripe={stripe} options={{ clientSecret }}>
      <CheckoutForm />
    </CheckoutElementsProvider>
  );
};

export default App;
```

Access the [Checkout](https://docs.stripe.com/js/custom_checkout) object in your checkout form component by using the `useCheckoutElements()` hook. The `Checkout` object contains data from the Checkout Session and methods to update it.

Read the `total` and `lineItems` from the `Checkout` object, and display them in your UI. This lets you enable features with minimal code changes. For example, adding [manual currency prices](https://docs.stripe.com/payments/custom/localize-prices/manual-currency-prices.md) requires no UI changes if you display the `total`.

```jsx
import React from "react";
import { useCheckoutElements } from "@stripe/react-stripe-js/checkout";

const CheckoutForm = () => {
  const checkoutState = useCheckoutElements();

  if (checkoutState.type === 'loading') {
    return <div>Loading...</div>;
  }

  if (checkoutState.type === 'error') {
    return <div>Error: {checkoutState.error.message}</div>;
  }

  return (
    <form>
      {JSON.stringify(checkoutState.checkout.lineItems, null, 2)}
      {/* A formatted total amount */}
      Total: {checkoutState.checkout.total.total.amount}
    </form>
  );
};
```

## Collect customer email [Client-side]

#### HTML + JS

You must provide a valid customer email when completing a Checkout Session.

These instructions create an email input and use [updateEmail](https://docs.stripe.com/js/custom_checkout/update_email) from the `Checkout` object.

Alternatively, you can:

- Pass in [customer_email](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer_email), [customer_account](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer_account) (for customers represented as customer-configured `Account` objects), or [customer](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer) (for customers represented as `Customer` objects) when creating the Checkout Session. Stripe validates emails provided this way.
- Pass in an email you already validated on [checkout.confirm](https://docs.stripe.com/js/custom_checkout/confirm).

```html
<input type="text" id="email" />
<div id="email-errors"></div>
```

```javascript
const checkout = stripe.initCheckoutElementsSdk({ clientSecret });
const loadActionsResult = await checkout.loadActions();

if (loadActionsResult.type === 'success') {
  const { actions } = loadActionsResult;
  const emailInput = document.getElementById('email');
  const emailErrors = document.getElementById('email-errors');

  emailInput.addEventListener('input', () => {
    // Clear any validation errors
    emailErrors.textContent = "";
  });

  emailInput.addEventListener('blur', () => {
    const newEmail = emailInput.value;
    actions.updateEmail(newEmail).then((result) => {
      if (result.error) {
        emailErrors.textContent = result.error.message;
      }
    });
  });
}
```

#### React

You must provide a valid customer email when completing a Checkout Session.

These instructions create an email input and use [updateEmail](https://docs.stripe.com/js/react_stripe_js/checkout/update_email) from the `Checkout` object.

Alternatively, you can:

- Pass in [customer_email](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer_email), [customer_account](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer_account) (for customers represented as customer-configured `Account` objects), or [customer](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer) (for customers represented as `Customer` objects) when creating the Checkout Session. Stripe validates emails provided this way.
- Pass in an email you already validated on [confirm](https://docs.stripe.com/js/react_stripe_js/checkout/confirm).

```jsx
import React from "react";
import { useCheckoutElements } from "@stripe/react-stripe-js/checkout";

const EmailInput = () => {
  const checkoutState = useCheckoutElements();
  const [email, setEmail] = React.useState("");
  const [error, setError] = React.useState(null);

  if (checkoutState.type === 'loading') {
    return <div>Loading...</div>;
  } else if (checkoutState.type === 'error') {
    return <div>Error: {checkoutState.error.message}</div>;
  }

  const handleBlur = () => {
    checkoutState.checkout.updateEmail(email).then((result) => {
      if (result.type === 'error') {
        setError(result.error);
      }
    });
  };

  const handleChange = (e) => {
    setError(null);
    setEmail(e.target.value);
  };

  return (
    <div>
      <label htmlFor="checkout-form-email">Email</label>
      <input
        id="checkout-form-email"
        type="email"
        value={email}
        onChange={handleChange}
        onBlur={handleBlur}
      />
      {error && <div>{error.message}</div>}
    </div>
  );
};

export default EmailInput;
```

## Collect payment details [Client-side]

Collect payment details on the client with the [Payment Element](https://docs.stripe.com/payments/payment-element.md). The Payment Element is a prebuilt UI component that simplifies collecting payment details for a variety of payment methods.

The Payment Element contains an iframe that securely sends payment information to Stripe over an HTTPS connection. Avoid placing the Payment Element within another iframe because some payment methods require redirecting to another page for payment confirmation.

If you choose to use an iframe and want to accept Apple Pay or Google Pay, the iframe must have the [allow](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe#attr-allowpaymentrequest) attribute set to equal `"payment *"`.

The checkout page address must start with `https://` rather than `http://` for your integration to work. You can test your integration without using HTTPS, but remember to [enable it](https://docs.stripe.com/security/guide.md#tls) when you’re ready to accept live payments.

#### HTML + JS

First, create a container DOM element to mount the [Payment Element](https://docs.stripe.com/payments/payment-element.md). Then create an instance of the `Payment Element` using [checkout.createPaymentElement](https://docs.stripe.com/js/custom_checkout/create_payment_element) and mount it by calling [element.mount](https://docs.stripe.com/js/element/mount), providing either a CSS selector or the container DOM element.

```html
<div id="payment-element"></div>
```

```javascript
const paymentElement = checkout.createPaymentElement();
paymentElement.mount("#payment-element");
```

See the [Stripe.js docs](https://docs.stripe.com/js/custom_checkout/create_payment_element#custom_checkout_create_payment_element-options) to view the supported options.

You can [customize the appearance](https://docs.stripe.com/payments/checkout/customization/appearance.md) of all Elements by passing [elementsOptions.appearance](https://docs.stripe.com/js/custom_checkout/init#custom_checkout_init-options-elementsOptions-appearance) when initializing Checkout on the front end.

#### React

Mount the [Payment Element](https://docs.stripe.com/payments/payment-element.md) component within the [CheckoutElementsProvider](https://docs.stripe.com/js/react_stripe_js/checkout/checkout_provider).

```jsx
import React from "react";
import {
  PaymentElement,
  useCheckoutElements,
} from "@stripe/react-stripe-js/checkout";

const CheckoutForm = () => {
  const checkoutState = useCheckoutElements();

  if (checkoutState.type === 'loading') {
    return <div>Loading...</div>;
  }

  if (checkoutState.type === 'error') {
    return <div>Error: {checkoutState.error.message}</div>;
  }

  return (
    <form>
      {JSON.stringify(checkoutState.checkout.lineItems, null, 2)}
      {/* A formatted total amount */}
      Total: {checkoutState.checkout.total.total.amount}
      <PaymentElement options={{ layout: 'accordion' }} />
    </form>
  );
};

export default CheckoutForm;
```

See the [Stripe.js docs](https://docs.stripe.com/js/custom_checkout/create_payment_element#custom_checkout_create_payment_element-options) to view the supported options.

You can [customize the appearance](https://docs.stripe.com/payments/checkout/customization/appearance.md) of all Elements by passing [elementsOptions.appearance](https://docs.stripe.com/js/react_stripe_js/checkout/checkout_provider#react_checkout_provider-options-elementsOptions-appearance) to the [CheckoutElementsProvider](https://docs.stripe.com/js/react_stripe_js/checkout/checkout_provider).

## Submit the payment [Client-side]

#### HTML + JS

Render a **Pay** button that calls [confirm](https://docs.stripe.com/js/custom_checkout/confirm) from the `Checkout` instance to submit the payment.

```html
<button id="pay-button">Pay</button>
<div id="confirm-errors"></div>
```

```js
const checkout = stripe.initCheckoutElementsSdk({ clientSecret });

checkout.on('change', (session) => {
  document.getElementById('pay-button').disabled = !session.canConfirm;
});

const loadActionsResult = await checkout.loadActions();

if (loadActionsResult.type === 'success') {
  const { actions } = loadActionsResult;
  const button = document.getElementById('pay-button');
  const errors = document.getElementById('confirm-errors');
  button.addEventListener('click', () => {
    // Clear any validation errors
    errors.textContent = "";

    actions.confirm().then((result) => {
      if (result.type === 'error') {
        errors.textContent = result.error.message;
      }
    });
  });
}
```

#### React

Render a **Pay** button that calls [confirm](https://docs.stripe.com/js/custom_checkout/confirm) from [useCheckoutElements](https://docs.stripe.com/js/react_stripe_js/checkout/use_checkout_elements) to submit the payment.

```jsx
import React from "react";
import { useCheckoutElements } from "@stripe/react-stripe-js/checkout";

const PayButton = () => {
  const checkoutState = useCheckoutElements();
  const [loading, setLoading] = React.useState(false);
  const [error, setError] = React.useState(null);

  if (checkoutState.type !== 'success') {
    return null;
  }

  const handleClick = () => {
    setLoading(true);
    checkoutState.checkout.confirm().then((result) => {
      if (result.type === 'error') {
        setError(result.error);
      }
      setLoading(false);
    });
  };

  return (
    <div>
      <button
        disabled={!checkoutState.checkout.canConfirm || loading}
        onClick={handleClick}
      >
        Pay
      </button>
      {error && <div>{error.message}</div>}
    </div>
  );
};

export default PayButton;
```

## Test your integration

You can test your form using the test BSB number `000000` and one of the test account numbers below when going through your checkout flow, or use the corresponding token to skip manually entering bank account details.

| BSB Number | Account number | Token                                    | Description                                                                                                                                                                                   |
| ---------- | -------------- | ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `000000`   | `000123456`    | `pm_auBecsDebit_success`                 | The PaymentIntent status transitions from `processing` to `succeeded`. The mandate status remains `active`.                                                                                   |
| `000000`   | `900123456`    | `pm_auBecsDebit_successDelayed`          | The PaymentIntent status transitions from `processing` to `succeeded` (with a three-minute delay). The mandate status remains `active`.                                                       |
| `000000`   | `111111113`    | `pm_auBecsDebit_accountClosed`           | The PaymentIntent status transitions from `processing` to `requires_payment_method` with an `account_closed` failure code. The mandate status becomes `inactive`.                             |
| `000000`   | `111111116`    | `pm_auBecsDebit_noAccount`               | The PaymentIntent status transitions from `processing` to `requires_payment_method` with a `no_account` failure code. The mandate status becomes `inactive`.                                  |
| `000000`   | `222222227`    | `pm_auBecsDebit_referToCustomer`         | The PaymentIntent status transitions from `processing` to `requires_payment_method` with a `refer_to_customer` failure code. The mandate status remains `active`.                             |
| `000000`   | `922222227`    | `pm_auBecsDebit_referToCustomerDelayed`  | The PaymentIntent status transitions from `processing` to `requires_payment_method` with a `refer_to_customer` failure code (with a three-minute delay). The mandate status remains `active`. |
| `000000`   | `333333335`    | `pm_auBecsDebit_debitNotAuthorized`      | The PaymentIntent status transitions from `processing` to `requires_payment_method` with a `debit_not_authorized` failure code. The mandate status becomes `inactive`.                        |
| `000000`   | `666666660`    | `pm_auBecsDebit_dispute`                 | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                                                                  |
| `000000`   | `343434343`    | `pm_auBecsDebit_exceedsWeeklyLimit`      | The PaymentIntent fails with a `charge_exceeds_source_limit` error due to the payment amount causing the account to exceed its weekly payment volume limit.                                   |
| `000000`   | `121212121`    | `pm_auBecsDebit_exceedsTransactionLimit` | The PaymentIntent fails with a `charge_exceeds_transaction_limit` error due to the payment amount exceeding the account’s transaction volume limit.                                           |

Using test account numbers triggers *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) events. In a *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes), Checkout Sessions complete immediately, and as a result, the respective `checkout.session.completed` and `checkout.session.async_payment_failed` events trigger immediately as well. In live mode, the webhooks get triggered with the same delays as those of their related Checkout Session successes and failures.

## Optional: Configure customer debit date

You can control the date that Stripe debits a customer’s bank account using the [target date](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-payment_method_options-au_becs_debit-target_date). The target date must be at least three days in the future and no more than 15 days from the current date.

The target date schedules money to leave the customer’s account on the target date.

Target dates that meet one of the following criteria delay the debit until the next available business day:

- Target date falls on a weekend, a bank holiday, or other non-business day.
- Target date is fewer than three business days in the future.

This parameter operates on a best-effort basis. Each customer’s bank might process debits on different dates, depending on local bank holidays or other reasons.

# iOS

> This is a iOS for when payment-ui is mobile and platform is ios. View the full page at https://docs.stripe.com/payments/au-becs-debit/accept-a-payment?payment-ui=mobile&platform=ios.

> We recommend that you follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md) guide unless you need to use manual server-side confirmation, or your integration requires presenting payment methods separately. If you’ve already integrated with Elements, see the [Payment Element migration guide](https://docs.stripe.com/payments/payment-element/migration.md).

Check out the [BECS Direct Debit sample](https://docs.stripe.com/payments/au-becs-debit.md#payment-flow) or see the [code on GitHub](https://github.com/stripe-samples/au-becs-debit-payment).

Use [STPAUBECSFormView](https://stripe.dev/stripe-ios/stripe-payments-ui/Classes/STPAUBECSDebitFormView.html), Stripe’s prebuilt BECS payment details collection UI, to create a payment form that securely collects bank details without handling sensitive customer data. Accepting BECS Direct Debit payments in your app consists of:

- Creating an object to track a payment
- ​​Collecting payment method information and mandate acknowledgement
- Submitting the payment to Stripe for processing

Stripe users in Australia can use the [STPAUBECSFormView](https://stripe.dev/stripe-ios/stripe-payments-ui/Classes/STPAUBECSDebitFormView.html) and a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) to accept BECS Direct Debit payments from customers with an Australian bank account.

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

## Collect payment method details and mandate acknowledgment [Client-side]

You can securely collect BECS Debit payment information with [STPAUBECSFormView](https://stripe.dev/stripe-ios/stripe-payments-ui/Classes/STPAUBECSDebitFormView.html), a drop-in UI component provided by the SDK. `STPAUBECSFormView​` provides a UI for customers to enter their name, email, BSB number, and account number—in addition to displaying the [BECS Direct Debit Terms](https://stripe.com/au-becs/legal).

Create an instance of `STPAUBECSFormView​` configured with your company name and set up a delegate for the SDK to notify after the customer enters the required details to create an instance of `STPPaymentMethodParams`​. You can also customize `STPAUBECSFormView​` to match the look and feel of your app by providing values to `STPAUBECSFormView​'s` public properties.

#### Swift

```swift
import UIKit
import StripePaymentsUI

class CheckoutViewController: UIViewController {

    private var becsFormView = STPAUBECSDebitFormView(companyName: "Example Company Inc.")
    private let payButton = UIButton()

    private var paymentIntentClientSecret: String?

    override func viewDidLoad() {
        super.viewDidLoad()

        view.backgroundColor = .secondarySystemBackground

        payButton.layer.cornerRadius = 5
        payButton.contentEdgeInsets = UIEdgeInsets(top: 4, left: 8, bottom: 4, right: 8)
        payButton.backgroundColor = .systemGray3
        payButton.titleLabel?.font = UIFont.systemFont(ofSize: 18)
        payButton.setTitle("Accept Mandate and Pay", for: .normal)
        payButton.addTarget(self, action: #selector(pay), for: .touchUpInside)
        payButton.isEnabled = false
        payButton.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(payButton)

        becsFormView.becsDebitFormDelegate = self
        becsFormView.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(becsFormView)

        NSLayoutConstraint.activate([
                   becsFormView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
                   view.trailingAnchor.constraint(equalTo: becsFormView.trailingAnchor),

                   becsFormView.topAnchor.constraint(equalToSystemSpacingBelow: view.safeAreaLayoutGuide.topAnchor, multiplier: 2),

                   payButton.centerXAnchor.constraint(equalTo: view.centerXAnchor),
                   payButton.topAnchor.constraint(equalToSystemSpacingBelow: becsFormView.bottomAnchor, multiplier: 2),
               ])
    }

    @objc
    func pay() {
        // ...
    }

}

extension CheckoutViewController: STPAUBECSDebitFormViewDelegate {
    func auBECSDebitForm(_ form: STPAUBECSDebitFormView, didChangeToStateComplete complete: Bool) {
        payButton.isEnabled = complete
        payButton.backgroundColor = complete ? .systemBlue : .systemGray3
    }
}
```

## Create a PaymentIntent [Server-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) is an object that represents your intent to collect a payment. The `PaymentIntent` tracks the lifecycle of the payment process through [each stage](https://docs.stripe.com/payments/paymentintents/lifecycle.md). First, create a PaymentIntent on your server and specify the amount to collect and the `aud` currency (BECS Direct Debit doesn’t support other currencies). If you already have an integration using the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md), add `au_becs_debit` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your `PaymentIntent`.

To save the BECS Direct Debit account for reuse, set the [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) parameter to `off_session`. BECS Direct Debit only accepts an `off_session` value for this parameter.

#### Accounts v2

#### Node.js

```javascript
// Using Express
const express = require('express');
const app = express();
app.use(express.json());
const { resolve } = require('path');

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'aud',
  setup_future_usage: 'off_session',
  customer_account: customer_account.id,
  payment_method_types: ['au_becs_debit'],
});
const clientSecret = paymentIntent.client_secret;
// Pass the client secret to the client
```

#### Customers v1

#### Node.js

```javascript
// Using Express
const express = require('express');
const app = express();
app.use(express.json());
const { resolve } = require('path');

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'aud',
  setup_future_usage: 'off_session',
  customer: customer.id,
  payment_method_types: ['au_becs_debit'],
});
const clientSecret = paymentIntent.client_secret;
// Pass the client secret to the client
```

When you create a `PaymentIntent`, Stripe generates its [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) property. Pass the client secret to the client side.

> Use the client secret to charge the customer the amount specified on the PaymentIntent. Don’t log it, embed it in URLs, or expose it to anyone other than your customer.

## Submit the payment to Stripe [Client-side]

When the customer taps the Pay button, confirm the `PaymentIntent` to complete the payment.

First, assemble a [STPPaymentIntentParams](https://stripe.dev/stripe-ios/stripe-payments/Classes/STPPaymentIntentParams.html) object with:

1. The [STPAUBECSFormView’s](https://stripe.dev/stripe-ios/stripe-payments-ui/Classes/STPAUBECSDebitFormView.html) `paymentMethodParams` property
1. The `PaymentIntent` client secret from your server

Rather than sending the entire `PaymentIntent` object to the client, use its [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) from [step 3](https://docs.stripe.com/payments/au-becs-debit/accept-a-payment.md#ios-create-payment-intent). This is different from your API keys that authenticate Stripe API requests.

Next, complete the payment by calling the [STPPaymentHandler confirmPayment](<https://stripe.dev/stripe-ios/stripe-payments/Classes/STPPaymentHandler.html#/c:@M@StripePayments@objc(cs)STPPaymentHandler(im)confirmPayment:withAuthenticationContext:completion:>) method.

#### Swift

```swift
import UIKit
import StripePaymentsUI

class CheckoutViewController: UIViewController {
    // ...
    @objc
    func pay() {
        guard let paymentIntentClientSecret = paymentIntentClientSecret,
            let paymentMethodParams = becsFormView.paymentMethodParams else {
                return;
        }

        let paymentIntentParams = STPPaymentIntentParams(clientSecret: paymentIntentClientSecret)

        paymentIntentParams.paymentMethodParams = paymentMethodParams

        STPPaymentHandler.shared().confirmPayment(paymentIntentParams,
                                                  with: self)
        { (handlerStatus, paymentIntent, error) in
            switch handlerStatus {
            case .succeeded:
                // Payment succeeded
                // ...

            case .canceled:
                // Payment canceled
                // ...

            case .failed:
                // Payment failed
                // ...

            @unknown default:
                fatalError()
            }
        }
    }
}

extension CheckoutViewController: STPAuthenticationContext {
    func authenticationPresentingViewController() -> UIViewController {
        return self
    }
}
```

After confirming the `PaymentIntent​`, share the [mandate URL](https://docs.stripe.com/api/mandates/object.md#mandate_object-payment_method_details-au_becs_debit-url) from the [Mandate object](https://docs.stripe.com/api/mandates.md) with your customer. We also recommend including the following details when you confirm their mandate has been established:

- An explicit confirmation message that indicates a Direct Debit arrangement has been set up
- The business name that will appear on the customer’s bank statement whenever their account gets debited
- The payment amount and schedule (if applicable)
- A link to the generated DDR mandate URL

You can access the `Mandate​` object’s ID from `the payment_method_details​` on the [latest_charge](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-latest_charge) of the `PaymentIntent` by [retrieving it](https://docs.stripe.com/api/payment_intents/retrieve.md).

Users on API version [2022-08-01](https://docs.stripe.com/upgrades.md#2022-08-01) or older:

​​You can access the `Mandate​` object’s ID from `the payment_method_details​` on the [charge object](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-charges-data) of the `PaymentIntent` (included with the `payment_intent.processing​` event sent after confirmation) or [retrieve it](https://docs.stripe.com/api/payment_intents/retrieve.md).

## Confirm the PaymentIntent succeeded [Server-side]

BECS Direct Debit is a [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method, which means that funds aren’t immediately available. A BECS Direct Debit PaymentIntent typically remains in a processing state for 2 business days after submission to the BECS network. This submission happens once per day. Once the payment succeeds, the associated `PaymentIntent` status updates from `processing` to `succeeded`.

The following events are sent when the `PaymentIntent` status is updated:

| Event                           | Description                                                  | Next steps                                                                                  |
| ------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| `payment_intent.processing`     | The customer’s payment was submitted to Stripe successfully. | Wait for the initiated payment to succeed or fail.                                          |
| `payment_intent.succeeded`      | The customer’s payment succeeded.                            | Fulfill the goods or services that were purchased.                                          |
| `payment_intent.payment_failed` | The customer’s payment was declined.                         | Contact the customer through email or push notification and request another payment method. |

Because [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) and [customer](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-customer) were set, the *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) will be attached to the *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) object when the payment enters the `processing` state. This attachment happens regardless of whether payment eventually succeeds or fails.

When a Direct Debit attempt fails, Stripe sends a `payment_intent.payment_failed` event containing a `PaymentIntent` object. The `last_payment_error` attribute on the `PaymentIntent` contains a `code` and `message` describing details of the failure.

The failures can be transient or final for the mandate associated with the failed `PaymentIntent`. In case of a final failure, Stripe revokes the mandate to prevent additional failure costs. When this happens, and you need your customer to pay, it’s your responsibility to contact your customer to establish a new mandate by [re-collecting the bank account information](https://docs.stripe.com/payments/au-becs-debit/set-up-payment.md).

For the following failure codes returned, Stripe updates the mandate status as follows:

| Failure Code           | Description                                                                                                                     | Mandate Status |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| `debit_not_authorized` | There’s a permanent failure due to a restriction or block to debit the account and you should contact your customer.            | `inactive`     |
| `account_closed`       | There’s a permanent failure because the account has been closed and you should contact your customer.                           | `inactive`     |
| `no_account`           | There’s a permanent failure because there’s no account for the provided bank information and you should contact your customer.  | `inactive`     |
| `refer_to_customer`    | There’s a transient failure (for example, insufficient funds) and you can re-attempt to debit without collecting a new mandate. | `active`       |

We recommend [using webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks) to confirm the charge succeeds or fails, and to notify the customer whether mandate establishment and payment are complete or if they require additional attention.

## Test the integration

You can test your form using the test BSB number `000000` and one of the test account numbers below with your [STPPaymentHandler confirmPayment](<https://stripe.dev/stripe-ios/stripe-payments/Classes/STPPaymentHandler.html#/c:@M@StripePayments@objc(cs)STPPaymentHandler(im)confirmPayment:withAuthenticationContext:completion:>) method call.

| BSB Number | Account number | Token                                    | Description                                                                                                                                                                                   |
| ---------- | -------------- | ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `000000`   | `000123456`    | `pm_auBecsDebit_success`                 | The PaymentIntent status transitions from `processing` to `succeeded`. The mandate status remains `active`.                                                                                   |
| `000000`   | `900123456`    | `pm_auBecsDebit_successDelayed`          | The PaymentIntent status transitions from `processing` to `succeeded` (with a three-minute delay). The mandate status remains `active`.                                                       |
| `000000`   | `111111113`    | `pm_auBecsDebit_accountClosed`           | The PaymentIntent status transitions from `processing` to `requires_payment_method` with an `account_closed` failure code. The mandate status becomes `inactive`.                             |
| `000000`   | `111111116`    | `pm_auBecsDebit_noAccount`               | The PaymentIntent status transitions from `processing` to `requires_payment_method` with a `no_account` failure code. The mandate status becomes `inactive`.                                  |
| `000000`   | `222222227`    | `pm_auBecsDebit_referToCustomer`         | The PaymentIntent status transitions from `processing` to `requires_payment_method` with a `refer_to_customer` failure code. The mandate status remains `active`.                             |
| `000000`   | `922222227`    | `pm_auBecsDebit_referToCustomerDelayed`  | The PaymentIntent status transitions from `processing` to `requires_payment_method` with a `refer_to_customer` failure code (with a three-minute delay). The mandate status remains `active`. |
| `000000`   | `333333335`    | `pm_auBecsDebit_debitNotAuthorized`      | The PaymentIntent status transitions from `processing` to `requires_payment_method` with a `debit_not_authorized` failure code. The mandate status becomes `inactive`.                        |
| `000000`   | `666666660`    | `pm_auBecsDebit_dispute`                 | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                                                                  |
| `000000`   | `343434343`    | `pm_auBecsDebit_exceedsWeeklyLimit`      | The PaymentIntent fails with a `charge_exceeds_source_limit` error due to the payment amount causing the account to exceed its weekly payment volume limit.                                   |
| `000000`   | `121212121`    | `pm_auBecsDebit_exceedsTransactionLimit` | The PaymentIntent fails with a `charge_exceeds_transaction_limit` error due to the payment amount exceeding the account’s transaction volume limit.                                           |

*Webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) events are triggered when using test account numbers. In a *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes), PaymentIntents succeed and fail immediately, and as a result, the respective `payment_intent.succeeded` and `payment_intent.payment_failed` events trigger immediately as well. In live mode, the webhooks get triggered with the same delays as those of their related PaymentIntent successes and failures.

## See also

- [Save Australia BECS Direct Debit details for future payments](https://docs.stripe.com/payments/au-becs-debit/set-up-payment.md)
- [Connect payments](https://docs.stripe.com/connect/charges.md)

# Android

> This is a Android for when payment-ui is mobile and platform is android. View the full page at https://docs.stripe.com/payments/au-becs-debit/accept-a-payment?payment-ui=mobile&platform=android.

> We recommend that you follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md) guide unless you need to use manual server-side confirmation, or your integration requires presenting payment methods separately. If you’ve already integrated with Elements, see the [Payment Element migration guide](https://docs.stripe.com/payments/payment-element/migration.md).

Check out the [BECS Direct Debit sample](https://docs.stripe.com/payments/au-becs-debit.md#payment-flow) or see the [code on GitHub](https://github.com/stripe-samples/au-becs-debit-payment).

Use [BecsDebitWidget](https://stripe.dev/stripe-android/payments-core/com.stripe.android.view/-becs-debit-widget/index.html), Stripe’s prebuilt BECS payment details collection UI, to create a payment form that securely collects bank details without handling sensitive customer data. Accepting BECS Direct Debit payments in your app consists of:

- Creating an object to track a payment
- ​​Collecting payment method information and mandate acknowledgement
- Submitting the payment to Stripe for processing

Stripe users in Australia can use the [BecsDebitWidget](https://stripe.dev/stripe-android/payments-core/com.stripe.android.view/-becs-debit-widget/index.html) and a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) to accept BECS Direct Debit payments from customers with an Australian bank account.

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
  implementation("com.stripe:stripe-android:23.5.0")
  // Include the financial connections SDK to support US bank account as a payment method
  implementation("com.stripe:financial-connections:23.5.0")
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

## Collect payment method details and mandate acknowledgment [Client-side]

You can securely collect BECS Debit payment information with [BecsDebitWidget](https://stripe.dev/stripe-android/payments-core/com.stripe.android.view/-becs-debit-widget/index.html), a drop-in UI component provided by the SDK. `BecsDebitWidget` provides a UI for customers to enter their name, email, BSB number, and account number. It also displays the [BECS Direct Debit Terms](https://stripe.com/au-becs/legal).

### Add BecsDebitWidget to your layout

Add `BecsDebitWidget` to your layout and configure the `app:companyName` attribute with your company name.

```xml
  <?xml version="1.0" encoding="utf-8"?>
  <LinearLayout
      xmlns:android="http://schemas.android.com/apk/res/android"
      xmlns:app="http://schemas.android.com/apk/res-auto"
      android:layout_width="match_parent"
      android:layout_height="match_parent"
      android:orientation="vertical">

      <!-- app:companyName is a required attribute -->
      <com.stripe.android.view.BecsDebitWidget
          android:id="@+id/becs_debit_widget"
          android:layout_width="match_parent"
          android:layout_height="wrap_content"
          app:companyName="@string/company_name" />

      <Button
          android:id="@+id/pay_button"
          android:layout_width="300dp"
          android:layout_height="wrap_content"
          android:layout_gravity="center_horizontal"
          android:enabled="false"
          android:text="@string/pay_with_becs_debit" />

  </LinearLayout>
```

#### Style the BecsDebitWidget

The `BecsDebitWidget` can be further customized by adding the following styles to your application’s `styles.xml`.

```xml
<?xml version="1.0" encoding="utf-8"?>

<!-- Optionally customize the widget's EditText fields -->
<style name="Stripe.BecsDebitWidget.EditText"
    parent="Stripe.Base.BecsDebitWidget.EditText">
    <!-- Add custom styles here -->
</style>

<!-- Optionally customize the mandate -->
<style name="Stripe.BecsDebitWidget.MandateAcceptanceTextView"
    parent="Stripe.Base.BecsDebitWidget.MandateAcceptanceTextView">
    <!-- Add custom styles here -->
</style>

```

### Configure your Activity

Set a [BecsDebitWidget.ValidParamsCallback](https://stripe.dev/stripe-android/payments-core/com.stripe.android.view/-becs-debit-widget/-valid-params-callback/index.html) instance on [BecsDebitWidget#validParamsCallback](https://stripe.dev/stripe-android/payments-core/com.stripe.android.view/-becs-debit-widget/index.html#com.stripe.android.view/BecsDebitWidget/validParamsCallback/#/PointingToDeclaration/) to be notified after the customer enters the required details to create an instance of `PaymentMethodCreateParams`​.

#### Kotlin

```kotlin
class CheckoutActivity : Activity() {
    private val stripe: Stripe by lazy {
        Stripe(this, PaymentConfiguration.getInstance(this).publishableKey)
    }

    private lateinit var becsDebitWidget: BecsDebitWidget
    private lateinit var paymentIntentClientSecret: String

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.checkout_activity)

        becsDebitWidget = findViewById(R.id.becs_debit_widget)
        val payButton = findViewById<Button>(R.id.pay_button)

        becsDebitWidget.validParamsCallback =
            object : BecsDebitWidget.ValidParamsCallback {
                override fun onInputChanged(isValid: Boolean) {
                    // enable payButton if the customer's input is valid
                    payButton.isEnabled = isValid
                }
            }

        payButton.setOnClickListener {
            onPayClicked(paymentIntentClientSecret)
        }

        createPaymentIntent()
    }

    private fun createPaymentIntent() {
        // Create a PaymentIntent on your backend and return the client_secret to
        // this Activity. Set paymentIntentClientSecret to the client_secret.
    }
}
```

## Create a PaymentIntent [Server-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) is an object that represents your intent to collect a payment. The `PaymentIntent` tracks the lifecycle of the payment process through [each stage](https://docs.stripe.com/payments/paymentintents/lifecycle.md). First, create a PaymentIntent on your server and specify the amount to collect and the `aud` currency (BECS Direct Debit doesn’t support other currencies). If you already have an integration using the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md), add `au_becs_debit` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your `PaymentIntent`.

To save the BECS Direct Debit account for reuse, set the [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) parameter to `off_session`. BECS Direct Debit only accepts an `off_session` value for this parameter.

#### Accounts v2

#### Node.js

```javascript
// Using Express
const express = require('express');
const app = express();
app.use(express.json());
const { resolve } = require('path');

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'aud',
  setup_future_usage: 'off_session',
  customer_account: customer_account.id,
  payment_method_types: ['au_becs_debit'],
});
const clientSecret = paymentIntent.client_secret;
// Pass the client secret to the client
```

#### Customers v1

#### Node.js

```javascript
// Using Express
const express = require('express');
const app = express();
app.use(express.json());
const { resolve } = require('path');

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'aud',
  setup_future_usage: 'off_session',
  customer: customer.id,
  payment_method_types: ['au_becs_debit'],
});
const clientSecret = paymentIntent.client_secret;
// Pass the client secret to the client
```

When you create a `PaymentIntent`, Stripe generates its [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) property. Pass the client secret to the client side.

> Use the client secret to charge the customer the amount specified on the PaymentIntent. Don’t log it, embed it in URLs, or expose it to anyone other than your customer.

## Submit the payment to Stripe [Client-side]

When the customer taps the Pay button, confirm the `PaymentIntent` to complete the payment.

First, assemble a [ConfirmPaymentIntentParams](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-confirm-payment-intent-params/index.html) object with:

1. The [BecsDebitWidget#params](https://stripe.dev/stripe-android/payments-core/com.stripe.android.view/-becs-debit-widget/index.html#com.stripe.android.view/BecsDebitWidget/params/#/PointingToDeclaration/) property
1. The `PaymentIntent` client secret from your server

Rather than sending the entire `PaymentIntent` object to the client, use its [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) from [step 3](https://docs.stripe.com/payments/au-becs-debit/accept-a-payment.md#android-create-payment-intent). This is different from your API keys that authenticate Stripe API requests.

Next, complete the payment by calling the [PaymentLauncher confirm](https://stripe.dev/stripe-android/payments-core/com.stripe.android.payments.paymentlauncher/-payment-launcher/index.html#74063765%2FFunctions%2F-1622557690) method.

#### Kotlin

```kotlin
class CheckoutActivity : Activity() {
    // ...
    private val paymentLauncher: PaymentLauncher by lazy {
        PaymentLauncher.Companion.create(
            this,
            PaymentConfiguration.getInstance(applicationContext)publishableKey,
            PaymentConfiguration.getInstance(applicationContext).stripeAccountId,
            ::onPaymentResult
        )
    }

    fun onPayClicked(paymentIntentClientSecret: String) {
        becsDebitWidget.params?.let { params ->
            paymentLauncher.confirm(
                ConfirmSetupIntentParams.create(
                    paymentMethodCreateParams = params,
                    clientSecret = setupIntentClientSecret
                )
            )
        }
    }

    private fun onPaymentResult(paymentResult: PaymentResult) {
        when (paymentResult) {
            is PaymentResult.Completed -> {
                // PaymentIntent confirmation succeeded
            }
            is PaymentResult.Canceled -> {
                // PaymentIntent confirmation canceled
            }
            is PaymentResult.Failed -> {
                // PaymentIntent confirmation failed see here for message:
                // ((PaymentResult.Failed) paymentResult).getThrowable().getMessage();
            }
        }
    }
}
```

After confirming the `PaymentIntent​`, share the [mandate URL](https://docs.stripe.com/api/mandates/object.md#mandate_object-payment_method_details-au_becs_debit-url) from the [Mandate object](https://docs.stripe.com/api/mandates.md) with your customer. We also recommend including the following details when you confirm their mandate has been established:

- An explicit confirmation message that indicates a Direct Debit arrangement has been set up
- The business name that will appear on the customer’s bank statement whenever their account gets debited
- The payment amount and schedule (if applicable)
- A link to the generated DDR mandate URL

You can access the `Mandate` ID from `the payment_method_details​` on the [latest_charge](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-latest_charge) of the `PaymentIntent` by [retrieving it](https://docs.stripe.com/api/payment_intents/retrieve.md).

Users on API version [2022-08-01](https://docs.stripe.com/upgrades.md#2022-08-01) or older:

​​You can access the `Mandate​` object’s ID from `the payment_method_details​` on the [charge object](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-charges-data) of the `PaymentIntent` (included with the `payment_intent.processing​` event sent after confirmation) or you can [retrieve it](https://docs.stripe.com/api/payment_intents/retrieve.md).

## Confirm the PaymentIntent succeeded [Server-side]

BECS Direct Debit is a [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method, which means that funds aren’t immediately available. A BECS Direct Debit PaymentIntent typically remains in a processing state for 2 business days after submission to the BECS network. This submission happens once per day. Once the payment succeeds, the associated `PaymentIntent` status updates from `processing` to `succeeded`.

The following events are sent when the `PaymentIntent` status is updated:

| Event                           | Description                                                  | Next steps                                                                                  |
| ------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| `payment_intent.processing`     | The customer’s payment was submitted to Stripe successfully. | Wait for the initiated payment to succeed or fail.                                          |
| `payment_intent.succeeded`      | The customer’s payment succeeded.                            | Fulfill the goods or services that were purchased.                                          |
| `payment_intent.payment_failed` | The customer’s payment was declined.                         | Contact the customer through email or push notification and request another payment method. |

Because [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) and [customer](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-customer) were set, the *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) will be attached to the *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) object when the payment enters the `processing` state. This attachment happens regardless of whether payment eventually succeeds or fails.

When a Direct Debit attempt fails, Stripe sends a `payment_intent.payment_failed` event containing a `PaymentIntent` object. The `last_payment_error` attribute on the `PaymentIntent` contains a `code` and `message` describing details of the failure.

The failures can be transient or final for the mandate associated with the failed `PaymentIntent`. In case of a final failure, Stripe revokes the mandate to prevent additional failure costs. When this happens, and you need your customer to pay, it’s your responsibility to contact your customer to establish a new mandate by [re-collecting the bank account information](https://docs.stripe.com/payments/au-becs-debit/set-up-payment.md).

For the following failure codes returned, Stripe updates the mandate status as follows:

| Failure Code           | Description                                                                                                                     | Mandate Status |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| `debit_not_authorized` | There’s a permanent failure due to a restriction or block to debit the account and you should contact your customer.            | `inactive`     |
| `account_closed`       | There’s a permanent failure because the account has been closed and you should contact your customer.                           | `inactive`     |
| `no_account`           | There’s a permanent failure because there’s no account for the provided bank information and you should contact your customer.  | `inactive`     |
| `refer_to_customer`    | There’s a transient failure (for example, insufficient funds) and you can re-attempt to debit without collecting a new mandate. | `active`       |

We recommend [using webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks) to confirm the charge succeeds or fails, and to notify the customer whether mandate establishment and payment are complete or if they require additional attention.

## Test the integration

You can test your form using the test BSB number `000000` and one of the test account numbers below with your [Stripe#confirmPayment()](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-stripe/confirm-payment.html) method call.

| BSB Number | Account number | Token                                    | Description                                                                                                                                                                                   |
| ---------- | -------------- | ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `000000`   | `000123456`    | `pm_auBecsDebit_success`                 | The PaymentIntent status transitions from `processing` to `succeeded`. The mandate status remains `active`.                                                                                   |
| `000000`   | `900123456`    | `pm_auBecsDebit_successDelayed`          | The PaymentIntent status transitions from `processing` to `succeeded` (with a three-minute delay). The mandate status remains `active`.                                                       |
| `000000`   | `111111113`    | `pm_auBecsDebit_accountClosed`           | The PaymentIntent status transitions from `processing` to `requires_payment_method` with an `account_closed` failure code. The mandate status becomes `inactive`.                             |
| `000000`   | `111111116`    | `pm_auBecsDebit_noAccount`               | The PaymentIntent status transitions from `processing` to `requires_payment_method` with a `no_account` failure code. The mandate status becomes `inactive`.                                  |
| `000000`   | `222222227`    | `pm_auBecsDebit_referToCustomer`         | The PaymentIntent status transitions from `processing` to `requires_payment_method` with a `refer_to_customer` failure code. The mandate status remains `active`.                             |
| `000000`   | `922222227`    | `pm_auBecsDebit_referToCustomerDelayed`  | The PaymentIntent status transitions from `processing` to `requires_payment_method` with a `refer_to_customer` failure code (with a three-minute delay). The mandate status remains `active`. |
| `000000`   | `333333335`    | `pm_auBecsDebit_debitNotAuthorized`      | The PaymentIntent status transitions from `processing` to `requires_payment_method` with a `debit_not_authorized` failure code. The mandate status becomes `inactive`.                        |
| `000000`   | `666666660`    | `pm_auBecsDebit_dispute`                 | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                                                                  |
| `000000`   | `343434343`    | `pm_auBecsDebit_exceedsWeeklyLimit`      | The PaymentIntent fails with a `charge_exceeds_source_limit` error due to the payment amount causing the account to exceed its weekly payment volume limit.                                   |
| `000000`   | `121212121`    | `pm_auBecsDebit_exceedsTransactionLimit` | The PaymentIntent fails with a `charge_exceeds_transaction_limit` error due to the payment amount exceeding the account’s transaction volume limit.                                           |

*Webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) events are triggered when using test account numbers. In a *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes), PaymentIntents succeed and fail immediately, and as a result, the respective `payment_intent.succeeded` and `payment_intent.payment_failed` events trigger immediately as well. In live mode, the webhooks get triggered with the same delays as those of their related PaymentIntent successes and failures.

## See also

- [Save Australia BECS Direct Debit details for future payments](https://docs.stripe.com/payments/au-becs-debit/set-up-payment.md)
- [Connect payments](https://docs.stripe.com/connect/charges.md)

# React Native

> This is a React Native for when payment-ui is mobile and platform is react-native. View the full page at https://docs.stripe.com/payments/au-becs-debit/accept-a-payment?payment-ui=mobile&platform=react-native.

> We recommend that you follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md) guide unless you need to use manual server-side confirmation, or your integration requires presenting payment methods separately. If you’ve already integrated with Elements, see the [Payment Element migration guide](https://docs.stripe.com/payments/payment-element/migration.md).

Use `AuBECSDebitForm`, Stripe’s prebuilt BECS payment details collection UI, to create a payment form that securely collects bank details without handling sensitive customer data. Accepting BECS Direct Debit payments in your app consists of:

- Creating an object to track a payment
- ​​Collecting payment method information and mandate acknowledgement
- Submitting the payment to Stripe for processing

Stripe users in Australia can use the `AuBECSDebitForm` and a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) to accept BECS Direct Debit payments from customers with an Australian bank account.

## Set up Stripe [Server-side] [Client-side]

### Server-side

This integration requires endpoints on your server that talk to the Stripe API. Use our official libraries for access to the Stripe API from your server:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

### Client-side

The [React Native SDK](https://github.com/stripe/stripe-react-native) is open source and fully documented. Internally, it uses the [native iOS](https://github.com/stripe/stripe-ios) and [Android](https://github.com/stripe/stripe-android) SDKs. To install Stripe’s React Native SDK, run one of the following commands in your project’s directory (depending on which package manager you use):

#### yarn

```bash
yarn add @stripe/stripe-react-native
```

#### npm

```bash
npm install @stripe/stripe-react-native
```

Next, install some other necessary dependencies:

- For iOS, go to the **ios** directory and run `pod install` to ensure that you also install the required native dependencies.
- For Android, there are no more dependencies to install.

> We recommend following the [official TypeScript guide](https://reactnative.dev/docs/typescript#adding-typescript-to-an-existing-project) to add TypeScript support.

### Stripe initialization

To initialize Stripe in your React Native app, either wrap your payment screen with the `StripeProvider` component, or use the `initStripe` initialization method. Only the API [publishable key](https://docs.stripe.com/keys.md#obtain-api-keys) in `publishableKey` is required. The following example shows how to initialize Stripe using the `StripeProvider` component.

```jsx
import { useState, useEffect } from "react";
import { StripeProvider } from "@stripe/stripe-react-native";

function App() {
  const [publishableKey, setPublishableKey] = useState("");

  const fetchPublishableKey = async () => {
    const key = await fetchKey(); // fetch key from your server here
    setPublishableKey(key);
  };

  useEffect(() => {
    fetchPublishableKey();
  }, []);

  return (
    <StripeProvider
      publishableKey={publishableKey}
      merchantIdentifier="merchant.identifier" // required for Apple Pay
      urlScheme="your-url-scheme" // required for 3D Secure and bank redirects
    >
      {/* Your app code here */}
    </StripeProvider>
  );
}
```

> Use your API [test keys](https://docs.stripe.com/keys.md#obtain-api-keys) while you test and develop, and your [live mode](https://docs.stripe.com/keys.md#test-live-modes) keys when you publish your app.

## Collect payment method details and mandate acknowledgment [Client-side]

You can securely collect Australia BECS Direct Debit payment information with `AuBECSDebitForm` component, a drop-in UI component provided by the SDK. `AuBECSDebitForm` provides a UI for customers to enter their name, email, BSB number, and account number in addition to displaying the [Australia BECS Direct Debit Terms](https://stripe.com/au-becs/legal).

Add an `AuBECSDebitForm` component to the screen with your company name as a prop. You can also customize `AuBECSDebitForm` to match the look and feel of your app by providing the `formStyle` prop. Collect form details with the `onComplete` prop when confirming the payment.

```javascript
function PaymentScreen() {
  const [formDetails, setFormDetails] = useState<
    AuBECSDebitFormComponent.FormDetails
  >();

  return (
    <View>
      <AuBECSDebitForm
        onComplete={(value) => setFormDetails(value)}
        companyName="Example Company Inc."
        formStyle={{
          textColor: '#000000',
          fontSize: 22,
          placeholderColor: '#999999',
        }}
      />
      <Button title="Pay" variant="primary" onPress={handlePayPress} />
    </View>
  );
}
```

## Create a PaymentIntent [Server-side]

### Server-side

A [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) is an object that represents your intent to collect a payment. The `PaymentIntent` tracks the lifecycle of the payment process through [each stage](https://docs.stripe.com/payments/paymentintents/lifecycle.md). First, create a PaymentIntent on your server and specify the amount to collect and the `aud` currency (BECS Direct Debit doesn’t support other currencies). If you already have an integration using the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md), add `au_becs_debit` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your `PaymentIntent`.

To save the BECS Direct Debit account for reuse, set the [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) parameter to `off_session`. BECS Direct Debit only accepts an `off_session` value for this parameter.

#### Accounts v2

#### Node.js

```javascript
// Using Express
const express = require('express');
const app = express();
app.use(express.json());
const { resolve } = require('path');

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'aud',
  setup_future_usage: 'off_session',
  customer_account: customer_account.id,
  payment_method_types: ['au_becs_debit'],
});
const clientSecret = paymentIntent.client_secret;
// Pass the client secret to the client
```

#### Customers v1

#### Node.js

```javascript
// Using Express
const express = require('express');
const app = express();
app.use(express.json());
const { resolve } = require('path');

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'aud',
  setup_future_usage: 'off_session',
  customer: customer.id,
  payment_method_types: ['au_becs_debit'],
});
const clientSecret = paymentIntent.client_secret;
// Pass the client secret to the client
```

When you create a `PaymentIntent`, Stripe generates its [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) property. Pass the client secret to the client side.

> Use the client secret to charge the customer the amount specified on the PaymentIntent. Don’t log it, embed it in URLs, or expose it to anyone other than your customer.

### Client-side

On the client, request a PaymentIntent from your server and store its *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)).

```javascript
const fetchPaymentIntentClientSecret = async () => {
  const response = await fetch(`${API_URL}/create-payment-intent`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      currency: 'aud',
      payment_method_types: ['au_becs_debit'],
    }),
  });
  const { clientSecret, error } = await response.json();

  return { clientSecret, error };
};
```

## Submit the payment to Stripe [Client-side]

Retrieve the client secret from the PaymentIntent you created and call `confirmPayment`. This presents a webview where the customer can complete the payment on their bank’s website or app. Afterwards, the promise resolves with the result of the payment.

```javascript
function PaymentScreen() {
  const { confirmPayment, loading } = useConfirmPayment();

  const [formDetails, setFormDetails] = useState<
    AuBECSDebitFormComponent.FormDetails
  >();

  const handlePayPress = async () => {
    const { error, paymentIntent } = await confirmPayment(clientSecret, {
      paymentMethodType: 'AuBecsDebit',
      paymentMethodData: {
        formDetails,
      }
    });

    if (error) {
      Alert.alert(`Error code: ${error.code}`, error.message);
      console.log('Payment confirmation error', error.message);
    } else if (paymentIntent) {
      if (paymentIntent.status === PaymentIntents.Status.Processing) {
        Alert.alert(
          'Processing',
          `The debit has been successfully submitted and is now processing.`
        );
      } else if (paymentIntent.status === PaymentIntents.Status.Succeeded) {
        Alert.alert(
          'Success',
          `The payment was confirmed successfully! currency: ${paymentIntent.currency}`
        );
      } else {
        Alert.alert('Payment status:', paymentIntent.status);
      }
    }
  };

  return (
    <View>
      <AuBECSDebitForm
        onComplete={(value) => setFormDetails(value)}
        companyName="Example Company Inc."
        formStyle={{
          textColor: '#000000',
          fontSize: 22,
          placeholderColor: '#999999',
        }}
      />
      <Button title="Pay" variant="primary" onPress={handlePayPress} />
    </View>
  );
}
```

## Confirm the PaymentIntent succeeded [Server-side]

BECS Direct Debit is a [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method, which means that funds aren’t immediately available. A BECS Direct Debit PaymentIntent typically remains in a processing state for 2 business days after submission to the BECS network. This submission happens once per day. Once the payment succeeds, the associated `PaymentIntent` status updates from `processing` to `succeeded`.

The following events are sent when the `PaymentIntent` status is updated:

| Event                           | Description                                                  | Next steps                                                                                  |
| ------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| `payment_intent.processing`     | The customer’s payment was submitted to Stripe successfully. | Wait for the initiated payment to succeed or fail.                                          |
| `payment_intent.succeeded`      | The customer’s payment succeeded.                            | Fulfill the goods or services that were purchased.                                          |
| `payment_intent.payment_failed` | The customer’s payment was declined.                         | Contact the customer through email or push notification and request another payment method. |

Because [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) and [customer](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-customer) were set, the *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) will be attached to the *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) object when the payment enters the `processing` state. This attachment happens regardless of whether payment eventually succeeds or fails.

When a Direct Debit attempt fails, Stripe sends a `payment_intent.payment_failed` event containing a `PaymentIntent` object. The `last_payment_error` attribute on the `PaymentIntent` contains a `code` and `message` describing details of the failure.

The failures can be transient or final for the mandate associated with the failed `PaymentIntent`. In case of a final failure, Stripe revokes the mandate to prevent additional failure costs. When this happens, and you need your customer to pay, it’s your responsibility to contact your customer to establish a new mandate by [re-collecting the bank account information](https://docs.stripe.com/payments/au-becs-debit/set-up-payment.md).

For the following failure codes returned, Stripe updates the mandate status as follows:

| Failure Code           | Description                                                                                                                     | Mandate Status |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| `debit_not_authorized` | There’s a permanent failure due to a restriction or block to debit the account and you should contact your customer.            | `inactive`     |
| `account_closed`       | There’s a permanent failure because the account has been closed and you should contact your customer.                           | `inactive`     |
| `no_account`           | There’s a permanent failure because there’s no account for the provided bank information and you should contact your customer.  | `inactive`     |
| `refer_to_customer`    | There’s a transient failure (for example, insufficient funds) and you can re-attempt to debit without collecting a new mandate. | `active`       |

We recommend [using webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks) to confirm the charge succeeds or fails, and to notify the customer whether mandate establishment and payment are complete or if they require additional attention.

## Test the integration

Test your form using the test BSB number `000000` and one of the test account numbers below when you call `confirmPayment`.

| BSB Number | Account number | Token                                    | Description                                                                                                                                                                                   |
| ---------- | -------------- | ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `000000`   | `000123456`    | `pm_auBecsDebit_success`                 | The PaymentIntent status transitions from `processing` to `succeeded`. The mandate status remains `active`.                                                                                   |
| `000000`   | `900123456`    | `pm_auBecsDebit_successDelayed`          | The PaymentIntent status transitions from `processing` to `succeeded` (with a three-minute delay). The mandate status remains `active`.                                                       |
| `000000`   | `111111113`    | `pm_auBecsDebit_accountClosed`           | The PaymentIntent status transitions from `processing` to `requires_payment_method` with an `account_closed` failure code. The mandate status becomes `inactive`.                             |
| `000000`   | `111111116`    | `pm_auBecsDebit_noAccount`               | The PaymentIntent status transitions from `processing` to `requires_payment_method` with a `no_account` failure code. The mandate status becomes `inactive`.                                  |
| `000000`   | `222222227`    | `pm_auBecsDebit_referToCustomer`         | The PaymentIntent status transitions from `processing` to `requires_payment_method` with a `refer_to_customer` failure code. The mandate status remains `active`.                             |
| `000000`   | `922222227`    | `pm_auBecsDebit_referToCustomerDelayed`  | The PaymentIntent status transitions from `processing` to `requires_payment_method` with a `refer_to_customer` failure code (with a three-minute delay). The mandate status remains `active`. |
| `000000`   | `333333335`    | `pm_auBecsDebit_debitNotAuthorized`      | The PaymentIntent status transitions from `processing` to `requires_payment_method` with a `debit_not_authorized` failure code. The mandate status becomes `inactive`.                        |
| `000000`   | `666666660`    | `pm_auBecsDebit_dispute`                 | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                                                                  |
| `000000`   | `343434343`    | `pm_auBecsDebit_exceedsWeeklyLimit`      | The PaymentIntent fails with a `charge_exceeds_source_limit` error due to the payment amount causing the account to exceed its weekly payment volume limit.                                   |
| `000000`   | `121212121`    | `pm_auBecsDebit_exceedsTransactionLimit` | The PaymentIntent fails with a `charge_exceeds_transaction_limit` error due to the payment amount exceeding the account’s transaction volume limit.                                           |

*Webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) events are triggered when using test account numbers. In a *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes), PaymentIntents succeed and fail immediately, and as a result, the respective `payment_intent.succeeded` and `payment_intent.payment_failed` events trigger immediately as well. In live mode, the webhooks get triggered with the same delays as those of their related PaymentIntent successes and failures.

## See also

- [Save Australia BECS Direct Debit details for future payments](https://docs.stripe.com/payments/au-becs-debit/set-up-payment.md)
- [Connect payments](https://docs.stripe.com/connect/charges.md)

# Payment Intents API

> This is a Payment Intents API for when payment-ui is elements and api-integration is paymentintents. View the full page at https://docs.stripe.com/payments/au-becs-debit/accept-a-payment?payment-ui=elements&api-integration=paymentintents.

To determine which API meets your business needs, see the [comparison guide](https://docs.stripe.com/payments/checkout-sessions-and-payment-intents-comparison.md).

Use the [Payment Element](https://docs.stripe.com/payments/payment-element.md) to embed a custom Stripe payment form in your website or application and offer payment methods to customers. For advanced configurations and customizations, refer to the [Accept a Payment](https://docs.stripe.com/payments/accept-a-payment.md) integration guide.

## Set up Stripe [Server-side]

To get started, [create a Stripe account](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create or retrieve a customer [Server-side]

To reuse a BECS Direct Debit account for future payments, attach it to an object that represents your customer.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

Create a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/create.md#v2_create_accounts-configuration-customer) or [Customer](https://docs.stripe.com/api/customers/create.md) when your customer creates an account with your business, or when saving a payment method. Associate the object’s ID with your own internal representation of a customer.

Create a new customer or retrieve an existing one to associate with this payment.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const account = await stripe.v2.core.accounts.create({
  contact_email: 'jenny.rosen@example.com',
  display_name: 'Jenny Rosen',
  configuration: {
    customer: {},
  },
  include: ['configuration.customer'],
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customer = await stripe.customers.create({
  name: "Jenny Rosen",
  email: 'jenny.rosen@example.com',
});
```

## Collect payment details [Client-side]

You’re ready to collect payment details on the client with the Payment Element. The Payment Element is a prebuilt UI component that simplifies collecting payment details for a variety of payment methods.

The Payment Element contains an iframe that securely sends payment information to Stripe over an HTTPS connection. Avoid placing the Payment Element within another iframe because some payment methods require redirecting to another page for payment confirmation.

The checkout page address must start with `https://` rather than `http://` for your integration to work. You can test your integration without using HTTPS, but remember to [enable it](https://docs.stripe.com/security/guide.md#tls) when you’re ready to accept live payments.

#### HTML + JS

### Set up Stripe.js

The Payment Element is automatically available as a feature of Stripe.js. Include the Stripe.js script on your checkout page by adding it to the `head` of your HTML file. Always load Stripe.js directly from js.stripe.com to remain PCI compliant. Don’t include the script in a bundle or host a copy of it yourself.

```html
<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/dahlia/stripe.js"></script>
</head>
```

Create an instance of Stripe with the following JavaScript on your checkout page:

```javascript
// Set your publishable key: remember to change this to your live publishable key in production
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");
```

### Add the Payment Element to your checkout page

The Payment Element needs a place on your checkout page. Create an empty DOM node (container) with a unique ID in your payment form:

```html
<form id="payment-form">
  <div id="payment-element">
    <!-- Elements will create form elements here -->
  </div>
  <button id="submit">Submit</button>
  <div id="error-message">
    <!-- Display error message to your customers here -->
  </div>
</form>
```

#### Control payment methods from the Dashboard

After the form above loads, create an Elements instance with a `mode`, `amount`, and `currency`. These values determine which payment methods your customer sees. To provide a new payment method in your form, make sure you enable it in the [Dashboard](https://dashboard.stripe.com/settings/payment_methods).

```javascript
const options = {
  mode: 'payment',
  amount: 1099,
  currency: 'aud',
  // Fully customizable with appearance API.
  appearance: {
    /*...*/
  },
};

// Set up Stripe.js and Elements to use in checkout formconst elements = stripe.elements(options);

// Create and mount the Payment Element
const paymentElementOptions = { layout: 'accordion' };
const paymentElement = elements.create('payment', paymentElementOptions);
paymentElement.mount("#payment-element");
```

#### List payment methods manually

To manually list the payment methods you want to be available, add each one to `paymentMethodTypes`.

Then, create an instance of the Payment Element and mount it to the container DOM node.

```javascript
const options = {
  mode: 'payment',
  amount: 1099,
  currency: 'aud',
  paymentMethodTypes: ['au_becs_debit'],
  // Fully customizable with appearance API.
  appearance: {
    /*...*/
  },
};

// Set up Stripe.js and Elements to use in checkout formconst elements = stripe.elements(options);

// Create and mount the Payment Element
const paymentElementOptions = { layout: 'accordion' };
const paymentElement = elements.create('payment', paymentElementOptions);
paymentElement.mount("#payment-element");
```

#### React

### Set up Stripe.js

Install [React Stripe.js](https://www.npmjs.com/package/@stripe/react-stripe-js) and the [Stripe.js loader](https://www.npmjs.com/package/@stripe/stripe-js) from the npm public registry.

```bash
npm install --save @stripe/react-stripe-js @stripe/stripe-js
```

### Add and configure the Elements provider to your checkout page

To use the Payment Element component, wrap your checkout page component in an [Elements provider](https://docs.stripe.com/sdks/stripejs-react.md#elements-provider). Call `loadStripe` with your publishable key, and pass the returned `Promise` to the `Elements` provider.

#### Control payment methods from the Dashboard

The `Elements` provider also accepts a `mode`, `amount`, and `currency`. These values determine which payment methods your customer sees. To provide a new payment method in your form, make sure you enable it in the [Dashboard](https://dashboard.stripe.com/settings/payment_methods).

```jsx
import React from "react";
import ReactDOM from "react-dom";
import { Elements } from "@stripe/react-stripe-js";
import { loadStripe } from "@stripe/stripe-js";

import CheckoutForm from "./CheckoutForm";

// Make sure to call `loadStripe` outside of a component’s render to avoid
// recreating the `Stripe` object on every render.
const stripePromise = loadStripe("<<YOUR_PUBLISHABLE_KEY>>");

function App() {
  const options = {
    mode: 'payment',
    amount: 1099,
    currency: 'aud',
    // Fully customizable with appearance API.
    appearance: {
      /*...*/
    },
  };

  return (
    <Elements stripe={stripePromise} options={options}>
      <CheckoutForm />
    </Elements>
  );
}

ReactDOM.render(<App />, document.getElementById("root"));
```

#### List payment methods manually

```jsx
import React from "react";
import ReactDOM from "react-dom";
import { Elements } from "@stripe/react-stripe-js";
import { loadStripe } from "@stripe/stripe-js";

import CheckoutForm from "./CheckoutForm";

// Make sure to call `loadStripe` outside of a component’s render to avoid
// recreating the `Stripe` object on every render.
const stripePromise = loadStripe("<<YOUR_PUBLISHABLE_KEY>>");

function App() {
  const options = {
    mode: 'payment',
    amount: 1099,
    currency: 'aud',
    paymentMethodTypes: ['au_becs_debit'],
    // Fully customizable with appearance API.
    appearance: {
      /*...*/
    },
  };

  return (
    <Elements stripe={stripePromise} options={options}>
      <CheckoutForm />
    </Elements>
  );
}

ReactDOM.render(<App />, document.getElementById("root"));
```

### Add the Payment Element component

Use the `PaymentElement` component to build your form.

```jsx
import React from "react";
import { PaymentElement } from "@stripe/react-stripe-js";

const CheckoutForm = () => {
  return (
    <form>
      <PaymentElement />
      <button>Submit</button>
    </form>
  );
};

export default CheckoutForm;
```

You can customize the Payment Element to match the design of your site by passing the [appearance object](https://docs.stripe.com/elements/appearance-api.md) into `options` when creating the `Elements` provider.

### Collect addresses

By default, the Payment Element only collects the necessary billing address details. Some behavior, such as [calculating tax](https://docs.stripe.com/api/tax/calculations/create.md) or entering shipping details, requires your customer’s full address. You can:

- Use the [Address Element](https://docs.stripe.com/elements/address-element.md) to take advantage of autocomplete and localization features to collect your customer’s full address. This helps ensure the most accurate tax calculation.
- Collect address details using your own custom form.

## Create a PaymentIntent [Server-side]

> #### Run custom business logic immediately before payment confirmation
>
> Navigate to [step 5](https://docs.stripe.com/payments/finalize-payments-on-the-server.md?platform=web&type=payment#submit-payment) in the finalize payments guide to run your custom business logic immediately before payment confirmation. Otherwise, follow the steps below for a simpler integration, which uses `stripe.confirmPayment` on the client to both confirm the payment and handle any next actions.

#### Control payment methods from the Dashboard

When the customer submits your payment form, use a _PaymentIntent_ (The Payment Intents API tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by regulatory mandates, custom Radar fraud rules, or redirect-based payment methods) to facilitate the confirmation and payment process. Create a PaymentIntent on your server with an `amount` and `currency`. To prevent malicious customers from choosing their own prices, always decide how much to charge on the server-side (a trusted environment) and not the client.

A `PaymentIntent` includes a *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)). Return this value to your client for Stripe.js to use to securely complete the payment process.

#### Accounts v2

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');
const express = require('express');
const app = express();

app.use(express.static("."));

app.post("/create-intent", async (req, res) => {
  const intent = await stripe.paymentIntents.create({
    // To allow saving and retrieving payment methods, provide the customer's Account ID.
    customer_account: "{{CUSTOMER_ACCOUNT_ID}}",
    amount: 1099,
    currency: 'aud',
    setup_future_usage: 'off_session',
  });
  res.json({ client_secret: intent.client_secret });
});

app.listen(3000, () => {
  console.log("Running on port 3000");
});
```

#### Customers v1

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');
const express = require('express');
const app = express();

app.use(express.static("."));

app.post("/create-intent", async (req, res) => {
  const intent = await stripe.paymentIntents.create({
    // To allow saving and retrieving payment methods, provide the Customer ID.
    customer: customer.id,
    amount: 1099,
    currency: 'aud',
    setup_future_usage: 'off_session',
  });
  res.json({ client_secret: intent.client_secret });
});

app.listen(3000, () => {
  console.log("Running on port 3000");
});
```

#### List payment methods manually

When the customer submits your payment form, use a _PaymentIntent_ (The Payment Intents API tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by regulatory mandates, custom Radar fraud rules, or redirect-based payment methods) to facilitate the confirmation and payment process. Create a PaymentIntent on your server with an `amount`, `currency`, and one or more payment methods using `payment_method_types`. To prevent malicious customers from choosing their own prices, always decide how much to charge on the server-side (a trusted environment) and not the client.

Included on a PaymentIntent is a *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)). Return this value to your client for Stripe.js to use to securely complete the payment process.

#### Accounts v2

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');
const express = require('express');
const app = express();

app.use(express.static("."));

app.post("/create-intent", async (req, res) => {
  const intent = await stripe.paymentIntents.create({
    // To allow saving and retrieving payment methods, provide the customer's Account ID.
    customer_account: customer_account.id,
    amount: 1099,
    currency: 'aud',
    setup_future_usage: 'off_session',
    payment_method_types: ['au_becs_debit'],
  });
  res.json({ client_secret: intent.client_secret });
});

app.listen(3000, () => {
  console.log("Running on port 3000");
});
```

#### Customers v1

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');
const express = require('express');
const app = express();

app.use(express.static("."));

app.post("/create-intent", async (req, res) => {
  const intent = await stripe.paymentIntents.create({
    // To allow saving and retrieving payment methods, provide the Customer ID.
    customer: customer.id,
    amount: 1099,
    currency: 'aud',
    setup_future_usage: 'off_session',
    payment_method_types: ['au_becs_debit'],
  });
  res.json({ client_secret: intent.client_secret });
});

app.listen(3000, () => {
  console.log("Running on port 3000");
});
```

## Submit the payment to Stripe [Client-side]

Use [stripe.confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment) to complete the payment using details from the Payment Element.

Provide a [return_url](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-return_url) to this function to indicate where Stripe redirects the user after they complete the payment. Your user might be initially redirected to an intermediate site, such as a bank authorization page, before being redirected to the `return_url`. Card payments immediately redirect to the `return_url` when a payment is successful.

If you don’t want to redirect for card payments after payment completion, you can set [redirect](https://docs.stripe.com/js/payment_intents/confirm_payment#confirm_payment_intent-options-redirect) to `if_required`. This only redirects customers that check out with redirect-based payment methods.

#### HTML + JS

```javascript
const form = document.getElementById('payment-form');
const submitBtn = document.getElementById("submit");

const handleError = (error) => {
  const messageContainer = document.querySelector("#error-message");
  messageContainer.textContent = error.message;
  submitBtn.disabled = false;
};

form.addEventListener("submit", async (event) => {
  // We don't want to let default form submission happen here,
  // which would refresh the page.
  event.preventDefault();

  // Prevent multiple form submissions
  if (submitBtn.disabled) {
    return;
  }

  // Disable form submission while loading
  submitBtn.disabled = true;

  // Trigger form validation and wallet collection
  const { error: submitError } = await elements.submit();
  if (submitError) {
    handleError(submitError);
    return;
  }

  // Create the PaymentIntent and obtain clientSecret
  const res = await fetch("/create-intent", {
    method: 'POST',
  });

  const { client_secret: clientSecret } = await res.json();

  // Confirm the PaymentIntent using the details collected by the Payment Element
  const { error } = await stripe.confirmPayment({
    elements,
    clientSecret,
    confirmParams: {
      return_url: "https://example.com/order/123/complete",
    },
  });

  if (error) {
    // This point is only reached if there's an immediate error when
    // confirming the payment. Show the error to your customer (for example, payment details incomplete)
    handleError(error);
  } else {
    // Your customer is redirected to your `return_url`. For some payment
    // methods like iDEAL, your customer is redirected to an intermediate
    // site first to authorize the payment, then redirected to the `return_url`.
  }
});
```

#### React

```jsx
import React, { useState } from "react";
import {
  useStripe,
  useElements,
  PaymentElement,
} from "@stripe/react-stripe-js";

export default function CheckoutForm() {
  const stripe = useStripe();
  const elements = useElements();

  const [errorMessage, setErrorMessage] = useState();
  const [loading, setLoading] = useState(false);

  const handleError = (error) => {
    setLoading(false);
    setErrorMessage(error.message);
  };

  const handleSubmit = async (event) => {
    // We don't want to let default form submission happen here,
    // which would refresh the page.
    event.preventDefault();

    if (!stripe) {
      // Stripe.js hasn't yet loaded.
      // Make sure to disable form submission until Stripe.js has loaded.
      return;
    }

    setLoading(true);

    // Trigger form validation and wallet collection
    const { error: submitError } = await elements.submit();
    if (submitError) {
      handleError(submitError);
      return;
    }

    // Create the PaymentIntent and obtain clientSecret
    const res = await fetch("/create-intent", {
      method: 'POST',
    });

    const { client_secret: clientSecret } = await res.json();

    // Confirm the PaymentIntent using the details collected by the Payment Element
    const { error } = await stripe.confirmPayment({
      elements,
      clientSecret,
      confirmParams: {
        return_url: "https://example.com/order/123/complete",
      },
    });

    if (error) {
      // This point is only reached if there's an immediate error when
      // confirming the payment. Show the error to your customer (for example, payment details incomplete)
      handleError(error);
    } else {
      // Your customer is redirected to your `return_url`. For some payment
      // methods like iDEAL, your customer is redirected to an intermediate
      // site first to authorize the payment, then redirected to the `return_url`.
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <PaymentElement />
      <button type="submit" disabled={!stripe || loading}>
        Submit Payment
      </button>
      {errorMessage && <div>{errorMessage}</div>}
    </form>
  );
}
```

## Confirm the PaymentIntent succeeded [Server-side]

BECS Direct Debit is a [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method, which means that funds aren’t immediately available. A BECS Direct Debit PaymentIntent typically remains in a processing state for 2 business days after submission to the BECS network. This submission happens once per day. Once the payment succeeds, the associated `PaymentIntent` status updates from `processing` to `succeeded`.

The following events are sent when the `PaymentIntent` status is updated:

| Event                           | Description                                                  | Next steps                                                                                  |
| ------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| `payment_intent.processing`     | The customer’s payment was submitted to Stripe successfully. | Wait for the initiated payment to succeed or fail.                                          |
| `payment_intent.succeeded`      | The customer’s payment succeeded.                            | Fulfill the goods or services that were purchased.                                          |
| `payment_intent.payment_failed` | The customer’s payment was declined.                         | Contact the customer through email or push notification and request another payment method. |

Because [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) and [customer](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-customer) were set, the *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) will be attached to the *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) object when the payment enters the `processing` state. This attachment happens regardless of whether payment eventually succeeds or fails.

When a Direct Debit attempt fails, Stripe sends a `payment_intent.payment_failed` event containing a `PaymentIntent` object. The `last_payment_error` attribute on the `PaymentIntent` contains a `code` and `message` describing details of the failure.

The failures can be transient or final for the mandate associated with the failed `PaymentIntent`. In case of a final failure, Stripe revokes the mandate to prevent additional failure costs. When this happens, and you need your customer to pay, it’s your responsibility to contact your customer to establish a new mandate by [re-collecting the bank account information](https://docs.stripe.com/payments/au-becs-debit/set-up-payment.md).

For the following failure codes returned, Stripe updates the mandate status as follows:

| Failure Code           | Description                                                                                                                     | Mandate Status |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| `debit_not_authorized` | There’s a permanent failure due to a restriction or block to debit the account and you should contact your customer.            | `inactive`     |
| `account_closed`       | There’s a permanent failure because the account has been closed and you should contact your customer.                           | `inactive`     |
| `no_account`           | There’s a permanent failure because there’s no account for the provided bank information and you should contact your customer.  | `inactive`     |
| `refer_to_customer`    | There’s a transient failure (for example, insufficient funds) and you can re-attempt to debit without collecting a new mandate. | `active`       |

We recommend [using webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks) to confirm the charge succeeds or fails, and to notify the customer whether mandate establishment and payment are complete or if they require additional attention.

## Test your integration

You can test your form using the test BSB number `000000` and one of the test account numbers below when going through your checkout flow, or use the corresponding token to skip manually entering bank account details.

| BSB Number | Account number | Token                                    | Description                                                                                                                                                                                   |
| ---------- | -------------- | ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `000000`   | `000123456`    | `pm_auBecsDebit_success`                 | The PaymentIntent status transitions from `processing` to `succeeded`. The mandate status remains `active`.                                                                                   |
| `000000`   | `900123456`    | `pm_auBecsDebit_successDelayed`          | The PaymentIntent status transitions from `processing` to `succeeded` (with a three-minute delay). The mandate status remains `active`.                                                       |
| `000000`   | `111111113`    | `pm_auBecsDebit_accountClosed`           | The PaymentIntent status transitions from `processing` to `requires_payment_method` with an `account_closed` failure code. The mandate status becomes `inactive`.                             |
| `000000`   | `111111116`    | `pm_auBecsDebit_noAccount`               | The PaymentIntent status transitions from `processing` to `requires_payment_method` with a `no_account` failure code. The mandate status becomes `inactive`.                                  |
| `000000`   | `222222227`    | `pm_auBecsDebit_referToCustomer`         | The PaymentIntent status transitions from `processing` to `requires_payment_method` with a `refer_to_customer` failure code. The mandate status remains `active`.                             |
| `000000`   | `922222227`    | `pm_auBecsDebit_referToCustomerDelayed`  | The PaymentIntent status transitions from `processing` to `requires_payment_method` with a `refer_to_customer` failure code (with a three-minute delay). The mandate status remains `active`. |
| `000000`   | `333333335`    | `pm_auBecsDebit_debitNotAuthorized`      | The PaymentIntent status transitions from `processing` to `requires_payment_method` with a `debit_not_authorized` failure code. The mandate status becomes `inactive`.                        |
| `000000`   | `666666660`    | `pm_auBecsDebit_dispute`                 | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                                                                  |
| `000000`   | `343434343`    | `pm_auBecsDebit_exceedsWeeklyLimit`      | The PaymentIntent fails with a `charge_exceeds_source_limit` error due to the payment amount causing the account to exceed its weekly payment volume limit.                                   |
| `000000`   | `121212121`    | `pm_auBecsDebit_exceedsTransactionLimit` | The PaymentIntent fails with a `charge_exceeds_transaction_limit` error due to the payment amount exceeding the account’s transaction volume limit.                                           |

Using test account numbers triggers *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) events. In a *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes), PaymentIntents succeed and fail immediately, and as a result, the respective `payment_intent.succeeded` and `payment_intent.payment_failed` events trigger immediately as well. In live mode, the webhooks get triggered with the same delays as those of their related PaymentIntent successes and failures.

## Optional: Configure customer debit date

You can control the date that Stripe debits a customer’s bank account using the [target date](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-payment_method_options-au_becs_debit-target_date). The target date must be at least three days in the future and no more than 15 days from the current date.

The target date schedules money to leave the customer’s account on the target date. You can [cancel a PaymentIntent](https://docs.stripe.com/api/payment_intents/cancel.md) created with a target date up to three business days before the configured date.

Target dates that meet one of the following criteria delay the debit until next available business day:

- Target date falls on a weekend, a bank holiday, or other non-business day.
- Target date is fewer than three business days in the future.

This parameter operates on a best-effort basis. Each customer’s bank might process debits on different dates, depending on local bank holidays or other reasons.

## See also

- [Save Australia BECS Direct Debit details for future payments](https://docs.stripe.com/payments/au-becs-debit/set-up-payment.md)
- [Connect payments](https://docs.stripe.com/connect/charges.md)
