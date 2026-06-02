<!-- Source URL: https://docs.stripe.com/payments/acss-debit/accept-a-payment -->
<!-- Fetched: 2026-05-02 -->

# Accept a Canadian pre-authorized debit payment

Build a custom payment form or use Stripe Checkout to accept payments with pre-authorized debit in Canada.

# Checkout

> This is a Checkout for when payment-ui is checkout. View the full page at https://docs.stripe.com/payments/acss-debit/accept-a-payment?payment-ui=checkout.

Accepting Canadian pre-authorized debit (PAD) payments on your website consists of creating an object to track a payment, collecting payment method information and mandate acknowledgement, submitting the payment to Stripe for processing, and verifying your customer’s bank account.

With Checkout, you can create a Checkout Session with `acss_debit` as a payment method type to track and handle the states of the payment until the payment completes.

> Pre-authorized debit in Canada is a **delayed notification payment method**, which means that funds aren’t immediately available after payment. A payment typically takes **5 business days** to arrive in your account.

## Determine compatibility

**Customer Geography**: Canada

**Supported currencies**: `cad, usd`

**Presentment currencies**: `cad, usd`

**Payment mode**: Yes

**Setup mode**: Yes

**Subscription mode**: [Contact us](mailto:payment-methods-feedback@stripe.com?subject=PADs%20Subscription%20Mode%20User%20Interest)

To support Canadian pre-authorized debit payments, a Checkout Session must satisfy all of the following conditions:

- You can only use one-time line items (*subscriptions* (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) aren’t yet supported in Checkout).
- *Prices* (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) for all line items must be expressed in Canadian or US dollars (currency code `cad` or `usd`).
- Prices for all line items must be in the same currency. If you have line items in different currencies, create separate Checkout Sessions for each currency.

### Presentment currency

Most bank accounts in Canada hold Canadian dollars (CAD), with a small number of accounts in other currencies, including US dollars (USD). It’s possible to accept PAD payments in either CAD or USD, but choosing the correct currency for your customer is important to avoid payment failures.

Unlike many card-based payment methods, you might not be able to successfully debit a CAD account in USD or debit a USD account in CAD. Most often, attempting to do so results in a delayed payment failure that takes up to five business days.

To avoid these failures, it’s safest to take PAD payments in CAD unless you’re confident your customer’s account accepts USD debits.

## Accept a payment

> Build an integration to [accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?integration=checkout) with Checkout before using this guide.

This guides you through enabling Canadian pre-authorized debit and shows the differences between accepting payments using dynamic payment methods and manually configuring payment methods.

### Enable Canadian pre-authorized debit as a payment method

When creating a new [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md), you need to:

1. Add `acss_debit` to the list of `payment_method_types`.
   - If you manage payment methods in the Dashboard, you don’t need to include `payment_method_types` in the Checkout Session because [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md) are enabled by default. However, you still need to include `payment_method_options`.
1. Make sure all your `line_items` use the `cad` currency.
1. Specify additional [payment_method_options](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-acss_debit) parameters to describe your transaction. Learn more below.

Payments must specify a [payment schedule](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_method_options-acss_debit-mandate_options-payment_schedule) for customers to authorize when checking out. See [PAD Mandates](https://docs.stripe.com/payments/acss-debit.md#mandates) for details on how to choose the right mandate options for your business:

| Parameter                                                                   | Value                                                                                                                                                                                                                                      | Required                                                         |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| `payment_method_options[acss_debit][mandate_options][payment_schedule]`     | The mandate payment schedule. Accepted values are `interval`, `sporadic`, or `combined`. See the [PAD Mandates](https://docs.stripe.com/payments/acss-debit.md#mandates) overview to help you select the right schedule for your business. | Yes                                                              |
| `payment_method_options[acss_debit][mandate_options][interval_description]` | Text description of the payment schedule. See the [PAD Mandates](https://docs.stripe.com/payments/acss-debit.md#mandates) overview to help you construct the right interval description for your business.                                 | Required if `payment_schedule` value is `interval` or `combined` |
| `payment_method_options[acss_debit][mandate_options][transaction_type]`     | The type of transactions you’ll use the mandate for, either `personal` (if the transactions are for personal reasons) or `business` (if the transactions are for business reasons).                                                        | Yes                                                              |

### Create a Checkout session

#### Stripe-hosted page

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        currency: 'cad',
        product_data: {
          name: 'T-shirt',
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: 'payment',
  payment_method_options: {
    acss_debit: {
      mandate_options: {
        payment_schedule: 'interval',
        interval_description: 'First day of every month',
        transaction_type: 'personal',
      },
    },
  },
  payment_method_types: ['acss_debit'],
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
        currency: 'cad',
        product_data: {
          name: 'T-shirt',
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: 'payment',
  payment_method_options: {
    acss_debit: {
      mandate_options: {
        payment_schedule: 'interval',
        interval_description: 'First day of every month',
        transaction_type: 'personal',
      },
    },
  },
  payment_method_types: ['acss_debit'],
  return_url: 'https://example.com/return',
  ui_mode: 'embedded_page',
});
```

During the Checkout session, the customer is presented with a UI modal that handles bank account details collection and instant verification with an optional fallback to verification using micro-deposits. In the uncommon case that the customer opts for micro-deposit verification, Stripe automatically sends two small deposits to the provided bank account which take 1-2 business days to appear on the customer’s online bank statement. When the deposits are expected to arrive, the customer receives an email with a link to confirm these amounts and verify the bank account with Stripe. Once completed, the payment begins processing.

### Fulfill your orders

After accepting a payment, learn how to [fulfill orders](https://docs.stripe.com/checkout/fulfillment.md).

## Test your integration

### Receive micro-deposit verification email

To receive the micro-deposit verification email in a *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes):

1. In Checkout, provide an email in the form of `{any_prefix}+test_email@{any_domain}`.
1. Click **Pay**.
1. Click **Agree** in the **Link your bank account to pay** modal.
1. Select **Use micro-deposit verification**.
1. Use one of the following test account numbers.
1. Click **Confirm**.
1. Click **Agree** to accept the **Pre-authorized debit agreement**.

### Test payment method tokens

Use test payment method tokens to test your integration without needing to manually enter bank account details. These tokens bypass the bank account collection and verification steps.

| Token                             | Scenario                                                        |
| --------------------------------- | --------------------------------------------------------------- |
| `pm_acssDebit_success`            | The payment succeeds immediately after the mandate is accepted. |
| `pm_acssDebit_noAccount`          | The payment fails because no account is found.                  |
| `pm_acssDebit_accountClosed`      | The payment fails because the account is closed.                |
| `pm_acssDebit_insufficientFunds`  | The payment fails due to insufficient funds.                    |
| `pm_acssDebit_debitNotAuthorized` | The payment fails because debits aren’t authorized.             |
| `pm_acssDebit_dispute`            | The payment succeeds but triggers a dispute.                    |

### Test account numbers

Stripe provides several test account numbers you can use to make sure your integration for manually-entered bank accounts is ready for production. All test accounts that automatically succeed or fail the payment must be verified using the test micro-deposit amounts below before they can be completed.

| Institution Number | Transit Number | Account Number | Scenario                                                                                                   |
| ------------------ | -------------- | -------------- | ---------------------------------------------------------------------------------------------------------- |
| `000`              | `11000`        | `000123456789` | Succeeds the payment immediately after micro-deposits are verified.                                        |
| `000`              | `11000`        | `900123456789` | Succeeds the payment with a three-minute delay after micro-deposits are verified.                          |
| `000`              | `11000`        | `000222222227` | Fails the payment immediately after micro-deposits are verified.                                           |
| `000`              | `11000`        | `900222222227` | Fails the payment with a three-minute delay after micro-deposits are verified.                             |
| `000`              | `11000`        | `000666666661` | Fails to send verification micro-deposits.                                                                 |
| `000`              | `11000`        | `000777777771` | Fails the payment due to the payment amount causing the account to exceed its weekly payment volume limit. |
| `000`              | `11000`        | `000888888881` | Fails the payment due to the payment amount exceeding the account’s transaction limit.                     |

To mimic successful or failed bank account verifications in a sandbox, use these meaningful amounts for micro-deposits:

| Micro-deposit Values          | Scenario                                                         |
| ----------------------------- | ---------------------------------------------------------------- |
| `32` and `45`                 | Successfully verifies the account.                               |
| `10` and `11`                 | Simulates exceeding the number of allowed verification attempts. |
| Any other number combinations | Fails account verification.                                      |

## Handle refunds and disputes

The refund period for Canadian pre-authorized debit is up to 180 days after the original payment.

Customers can dispute a payment through their bank up to 90 calendar days after the original payment and there is no appeals process.

Learn more about [Canadian pre-authorized debit disputes](https://docs.stripe.com/payments/acss-debit.md#disputed-payments).

## Additional considerations

### Microdeposit verification failure

When a bank account is pending verification with micro-deposits, it’s possible for the customer to fail to verify for two reasons:

- The micro-deposits failed to send to the customer’s bank account (usually indicates a closed/unavailable bank account or incorrect bank account number).
- The customer made three failed verification for the account. Exceeding this limit means the bank account can no longer be verified or reused.
- The customer failed to verify the bank account within 10 days.

If the bank account fails verification for one of these reasons, you can [handle the `checkout.session.async_payment_failed` event](https://docs.stripe.com/api/events/types.md?event_types-invoice.payment_succeeded=#event_types-checkout.session.async_payment_failed) to contact the customer about placing a new order.

## Optional: Instant only verification [Server-side]

By default, Canadian pre-authorized debit payments allow your customers to use instant bank account verification or micro-deposits. You can optionally require instant bank account verification only using the `payment_method_options[acss_debit][verification_method]` parameter when you create the Checkout session.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({
  mode: 'payment',
  customer_account: '{{CUSTOMERACCOUNT_ID}}',
  payment_method_types: ['acss_debit'],
  line_items: [
    {
      price_data: {
        currency: 'cad',
        product_data: {
          name: 'T-shirt',
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  payment_method_options: {
    acss_debit: {
      mandate_options: {
        payment_schedule: 'interval',
        interval_description: 'On November 25, 2021',
        transaction_type: 'personal',
      },
      verification_method: 'instant',
    },
  },
  success_url: 'https://example.com/success',
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({
  mode: 'payment',
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['acss_debit'],
  line_items: [
    {
      price_data: {
        currency: 'cad',
        product_data: {
          name: 'T-shirt',
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  payment_method_options: {
    acss_debit: {
      mandate_options: {
        payment_schedule: 'interval',
        interval_description: 'On November 25, 2021',
        transaction_type: 'personal',
      },
      verification_method: 'instant',
    },
  },
  success_url: 'https://example.com/success',
});
```

## Optional: Micro-deposit only verification [Server-side]

By default, Canadian pre-authorized debit payments allow your customers to use instant bank account verification or micro-deposits. You can optionally require micro-deposit verification only using the `payment_method_options[acss_debit][verification_method]` parameter when you create the Checkout session.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({
  mode: 'payment',
  customer_account: '{{CUSTOMERACCOUNT_ID}}',
  payment_method_types: ['acss_debit'],
  line_items: [
    {
      price_data: {
        currency: 'cad',
        product_data: {
          name: 'T-shirt',
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  payment_method_options: {
    acss_debit: {
      mandate_options: {
        payment_schedule: 'interval',
        interval_description: 'On November 25, 2021',
        transaction_type: 'personal',
      },
      verification_method: 'microdeposits',
    },
  },
  success_url: 'https://example.com/success',
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({
  mode: 'payment',
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['acss_debit'],
  line_items: [
    {
      price_data: {
        currency: 'cad',
        product_data: {
          name: 'T-shirt',
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  payment_method_options: {
    acss_debit: {
      mandate_options: {
        payment_schedule: 'interval',
        interval_description: 'On November 25, 2021',
        transaction_type: 'personal',
      },
      verification_method: 'microdeposits',
    },
  },
  success_url: 'https://example.com/success',
});
```

## Optional: Configure customer debit date [Server-side]

You can control the date that Stripe debits a customer’s bank account using the [target date](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-payment_method_options-acss_debit-target_date). The target date must be at least three days in the future and no more than 15 days from the current date.

The target date schedules money to leave the customer’s account on the target date.

Target dates that meet one of the following criteria delay the debit until the next available business day:

- Target date falls on a weekend, a bank holiday, or other non-business day.
- Target date is fewer than three business days in the future.

This parameter operates on a best-effort basis. Each customer’s bank might process debits on different dates, depending on local bank holidays or other reasons.

> You can’t set the [verification method](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-payment_method_options-acss_debit-verification_method) to `microdeposits` when using a [target date](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-payment_method_options-acss_debit-target_date), as the verification process could take longer than the target date, causing payments to arrive later than expected.

## See also

- [More about pre-authorized debit in Canada](https://docs.stripe.com/payments/acss-debit.md)
- [Managing mandates](https://docs.stripe.com/payments/acss-debit.md#mandates)
- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment.md)
- [Customizing Checkout](https://docs.stripe.com/payments/checkout/customization.md)

# Direct API

> This is a Direct API for when payment-ui is direct-api. View the full page at https://docs.stripe.com/payments/acss-debit/accept-a-payment?payment-ui=direct-api.

Accepting Canadian pre-authorized debit (PAD) payments on your website consists of creating an object to track a payment, collecting payment method information and mandate acknowledgement, submitting the payment to Stripe for processing, and verifying your customer’s bank account.

Stripe uses this payment object, the [Payment Intent](https://docs.stripe.com/payments/payment-intents.md), to track and handle all the states of the payment until the payment completes.

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create or retrieve a customer [Server-side]

To reuse a bank account for future payments, attach it to an object that represents your customer.

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
  include: ["configuration.customer"],
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

## Create a PaymentIntent [Server-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) is an object that represents your intent to collect a payment from a customer and tracks the lifecycle of the payment process through [each stage](https://docs.stripe.com/payments/paymentintents/lifecycle.md).

To use Canadian pre-authorized debits, you must obtain authorization from your customer for one-time and recurring debits using a pre-authorized debit agreement (see [PAD Mandates](https://docs.stripe.com/payments/acss-debit.md#mandates)). The [Mandate](https://docs.stripe.com/api/mandates.md) object records this agreement and authorization.

First, create a `PaymentIntent` on your server and specify the customer, amount to collect, and currency ([usually `cad`](https://docs.stripe.com/payments/acss-debit.md#presentment-currency)). If your integration already uses the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md), add `acss_debit` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your `PaymentIntent`.

If you want to reuse the payment method in the future, provide the [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) parameter with a value of `off_session`.

To define a payment schedule and verification method on the [Mandate](https://docs.stripe.com/api/mandates.md) for this PaymentIntent, also include the following parameters:

| Parameter                                                                   | Value                                                                                                                                                                                                                                      | Required                                                       |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------- |
| `payment_method_options[acss_debit][mandate_options][payment_schedule]`     | The mandate payment schedule. Accepted values are `interval`, `sporadic`, or `combined`. See the [PAD Mandates](https://docs.stripe.com/payments/acss-debit.md#mandates) overview to help you select the right schedule for your business. | Yes                                                            |
| `payment_method_options[acss_debit][mandate_options][interval_description]` | Text description of the interval of payment schedule. See the [PAD Mandates](https://docs.stripe.com/payments/acss-debit.md#mandates) overview to help you construct the right interval description for your business.                     | If `payment_schedule` is specified as `interval` or `combined` |
| `payment_method_options[acss_debit][mandate_options][transaction_type]`     | The type of transactions you’ll use the mandate for, either `personal` (if the transactions are for personal reasons) or `business` (if the transactions are for business reasons).                                                        | Yes                                                            |

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'cad',
  setup_future_usage: 'off_session',
  customer_account: '{{CUSTOMERACCOUNT_ID}}',
  payment_method_types: ['acss_debit'],
  payment_method_options: {
    acss_debit: {
      mandate_options: {
        payment_schedule: 'interval',
        interval_description: 'First day of every month',
        transaction_type: 'personal',
      },
    },
  },
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'cad',
  setup_future_usage: 'off_session',
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['acss_debit'],
  payment_method_options: {
    acss_debit: {
      mandate_options: {
        payment_schedule: 'interval',
        interval_description: 'First day of every month',
        transaction_type: 'personal',
      },
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
const express = require('express');
const app = express();

app.get('/secret', async (req, res) => {
  const intent = // ... Fetch or create the PaymentIntent
    res.json({ client_secret: intent.client_secret });
});

app.listen(3000, () => {
  console.log('Running on port 3000');
});
```

And then fetch the client secret with JavaScript on the client side:

```javascript
(async () => {
  const response = await fetch('/secret');
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
const express = require('express');
const expressHandlebars = require('express-handlebars');
const app = express();

app.engine('.hbs', expressHandlebars({ extname: '.hbs' }));
app.set('view engine', '.hbs');
app.set('views', './views');

app.get('/checkout', async (req, res) => {
  const intent = // ... Fetch or create the PaymentIntent
    res.render('checkout', { client_secret: intent.client_secret });
});

app.listen(3000, () => {
  console.log('Running on port 3000');
});
```

## Collect payment method details and submit [Client-side]

When a customer clicks to pay with Canadian pre-authorized debit, we recommend you use Stripe.js to submit the payment to Stripe. [Stripe.js](https://docs.stripe.com/payments/elements.md) is our foundational JavaScript library for building payment flows. It will automatically handle integration complexities, and enables you to easily extend your integration to other payment methods in the future.

Include the Stripe.js script on your checkout page by adding it to the `head` of your HTML file.

```html
<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/dahlia/stripe.js"></script>
</head>
```

Create an instance of Stripe.js with the following JavaScript on your checkout page.

```javascript
// Set your publishable key. Remember to change this to your live publishable key in production!
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe('<<YOUR_PUBLISHABLE_KEY>>');
```

Rather than sending the entire PaymentIntent object to the client, use its *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)) from the previous step. This is different from your API keys that authenticate Stripe API requests.

The client secret should still be handled carefully because it can complete the charge. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

Use [stripe.confirmAcssDebitPayment](https://docs.stripe.com/js/payment_intents/confirm_acss_debit_payment) to collect bank account details and verification, confirm the mandate, and complete the payment when the user submits the form. Including the customer’s email address and the account holder’s name in the `billing_details` property of the `payment_method` parameter is required to create a PAD payment method.

```javascript
const form = document.getElementById('payment-form');
const accountholderName = document.getElementById('accountholder-name');
const email = document.getElementById('email');
const submitButton = document.getElementById('submit-button');
const clientSecret = submitButton.dataset.secret;

form.addEventListener('submit', async (event) => {
  event.preventDefault();

  const { paymentIntent, error } = await stripe.confirmAcssDebitPayment(
    clientSecret,
    {
      payment_method: {
        billing_details: {
          name: accountholderName.value,
          email: email.value,
        },
      },
    },
  );

  if (error) {
    // Inform the customer that there was an error.
    console.log(error.message);
  } else {
    // Handle next step based on PaymentIntent's status.
    console.log('PaymentIntent ID: ' + paymentIntent.id);
    console.log('PaymentIntent status: ' + paymentIntent.status);
  }
});
```

Stripe.js then loads an on-page modal UI that handles bank account details collection and verification, presents a hosted mandate agreement and collects authorization.

> `stripe.confirmAcssDebitPayment` might take several seconds to complete. During that time, disable your form from being resubmitted and show a waiting indicator like a spinner. If you receive an error, show it to the customer, re-enable the form, and hide the waiting indicator.

If successful, Stripe returns a [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) object, with one of the following possible statuses:

| Status            | Description                                                                    | Next step                                                                                                                                                |
| ----------------- | ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `processing`      | The bank account has been instantly verified or verification wasn’t necessary. | ​​​​​​Step 6: [Confirm the PaymentIntent succeeded](https://docs.stripe.com/payments/acss-debit/accept-a-payment.md#web-confirm-paymentintent-succeeded) |
| `requires_action` | Further action needed to complete bank account verification.                   | Step 5: [Verifying bank accounts with micro-deposits](https://docs.stripe.com/payments/acss-debit/accept-a-payment.md#web-verify-with-microdeposits)     |

After successfully confirming the PaymentIntent, an email confirmation of the mandate and collected bank account details must be sent to your customer. Stripe handles these by default, but you can choose to [send custom notifications](https://docs.stripe.com/payments/acss-debit.md#mandate-and-debit-notification-emails) if you prefer.

> Mandate confirmation emails won’t be sent to the customer’s email address when testing the integration.

If the customer chooses to close the modal without completing the verification flow, Stripe.js returns the following error:

```json
{
  "error": {
    "type": "validation_error",
    "code": "incomplete_payment_details",
    "message": "Please provide complete payment details."
  }
}
```

## Verify bank account with micro-deposits [Client-side]

Not all customers can verify the bank account instantly. This step only applies if your customer has elected to opt out of the instant verification flow in the previous step.

In this case, Stripe automatically sends two micro-deposits to the customer’s bank account. These deposits take 1–2 business days to appear on the customer’s online statement and have statement descriptors that include `ACCTVERIFY`.

The result of the `stripe.confirmAcssDebitPayment` method call in the previous step is a PaymentIntent in the `requires_action` state. The PaymentIntent contains a `next_action` field that contains some useful information for completing the verification.

Stripe notifies your customer at the [billing email](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-billing_details-email) when the deposits are expected to arrive. The email includes a link to a Stripe-hosted verification page where they can confirm the amounts of the deposits and complete verification.

There is a limit of three failed verification attempts. If this limit is exceeded, the bank account can no longer be verified. In addition, there is a timeout for micro-deposit verifications of 10 days. If micro-deposits aren’t verified in that time, the PaymentIntent reverts to requiring new payment method details. Clear messaging about what these micro-deposits are and how you use them can help your customers avoid verification issues.

### Optional: Custom email and verification page

If you choose to send [custom email notifications](https://docs.stripe.com/payments/acss-debit.md#mandate-and-debit-notification-emails), you have to email your customer instead. To do this, you can use the `verify_with_microdeposits[hosted_verification_url]` URL in the `next_action` object to direct your customer to complete the verification process.

If you’re sending custom emails and don’t want to use the Stripe hosted verification page, you can create a form on your site for your customers to relay these amounts to you and verify the bank account using [Stripe.js](https://docs.stripe.com/js/payment_intents/verify_microdeposits_for_payment).

```javascript
stripe.verifyMicrodepositsForPayment(clientSecret, {
  amounts: [32, 45],
});
```

When the bank account is successfully verified, Stripe returns the [PaymentIntent object](https://docs.stripe.com/api/payment_intents/object.md) with a `status` of `processing`, and sends a `payment_intent.processing` *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event.

Verification can fail for several reasons. The failure might happen synchronously as a direct error response, or asynchronously through a `payment_intent.payment_failed` webhook event (shown in the following examples).

#### Synchronous Error

```json
{
  "error": {
    "code": "payment_method_microdeposit_verification_amounts_mismatch",
    "message": "The amounts provided do not match the amounts that were sent to the bank account. You have {attempts_remaining} verification attempts remaining.",
    "type": "invalid_request_error"
  }
}
```

#### Webhook Event

```javascript
{
  "object": {
    "id": "pi_1234",
    "object": "payment_intent",
    "customer": "cus_0246",
    ...
    "last_payment_error": {
      "code": "payment_method_microdeposit_verification_attempts_exceeded",
      "message": "You have exceeded the number of allowed verification attempts."
    },
    ...
    "status": "requires_payment_method"
  }
}
```

| Error Code                                                   | Synchronous or asynchronous                             | Message                                                                                                                                         | Status Change                                                           |
| ------------------------------------------------------------ | ------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `payment_method_microdeposit_failed`                         | Synchronously, or asynchronously through webhook event  | Microdeposits failed. Please check the account, institution and transit numbers provided                                                        | `status` is `requires_payment_method`, and `last_payment_error` is set. |
| `payment_method_microdeposit_verification_amounts_mismatch`  | Synchronously                                           | The amounts provided don’t match the amounts that were sent to the bank account. You have {attempts_remaining} verification attempts remaining. | Unchanged                                                               |
| `payment_method_microdeposit_verification_attempts_exceeded` | Synchronously, and asynchronously through webhook event | Exceeded number of allowed verification attempts                                                                                                | `status` is `requires_payment_method`, and `last_payment_error` is set. |
| `payment_method_microdeposit_verification_timeout`           | Asynchronously through webhook event                    | Microdeposit timeout. Customer hasn’t verified their bank account within the required 10 day period.                                            | `status` is `requires_payment_method`, and `last_payment_error` is set. |

## Confirm the PaymentIntent succeeded [Server-side]

Canadian pre-authorized debits are a [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method. This means that it can take up to five business days to receive notification of the success or failure of a payment after you initiate a debit from your customer’s account.

The PaymentIntent you create initially has a status of `processing`. Successful completion of the payment updates the PaymentIntent status from `processing` to `succeeded`.

The following events are sent when the PaymentIntent status is updated:

| Event                           | Description                                                                                     | Next step                                                                                                                                                                                                                                                                                     |
| ------------------------------- | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_intent.processing`     | The customer’s payment was submitted to Stripe successfully.                                    | Wait for the initiated payment to succeed or fail.                                                                                                                                                                                                                                            |
| `payment_intent.succeeded`      | The customer’s payment succeeded.                                                               | Fulfill the goods or services that the customer purchased.                                                                                                                                                                                                                                    |
| `payment_intent.payment_failed` | The customer’s payment was declined. This can also apply to a failed microdeposit verification. | Contact the customer through email or push notification and request another payment method. If the webhook was sent due to a failed microdeposit verification, the user needs to enter in their bank account details again and a new set of microdeposits will be deposited in their account. |

We recommend using [webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks) to *confirm* (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) the charge has succeeded and to notify the customer that the payment is complete. You can also view events on the [Stripe Dashboard](https://dashboard.stripe.com/test/events).

## Test your integration

### Receive micro-deposit verification email

To receive the micro-deposit verification email in a *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes) after collecting the bank account details and accepting a mandate, provide an email in the `payment_method[billing_details][email]` field in the form of `{any_prefix}+test_email@{any_domain}` when confirming the payment method details.

### Test payment method tokens

Use test payment method tokens to test your integration without needing to manually enter bank account details. These tokens bypass the bank account collection and verification steps.

| Token                             | Scenario                                                        |
| --------------------------------- | --------------------------------------------------------------- |
| `pm_acssDebit_success`            | The payment succeeds immediately after the mandate is accepted. |
| `pm_acssDebit_noAccount`          | The payment fails because no account is found.                  |
| `pm_acssDebit_accountClosed`      | The payment fails because the account is closed.                |
| `pm_acssDebit_insufficientFunds`  | The payment fails due to insufficient funds.                    |
| `pm_acssDebit_debitNotAuthorized` | The payment fails because debits aren’t authorized.             |
| `pm_acssDebit_dispute`            | The payment succeeds but triggers a dispute.                    |

### Test account numbers

Stripe provides several test account numbers you can use to make sure your integration for manually-entered bank accounts is ready for production. All test accounts that automatically succeed or fail the payment must be verified using the test micro-deposit amounts below before they can be completed.

| Institution Number | Transit Number | Account Number | Scenario                                                                                                   |
| ------------------ | -------------- | -------------- | ---------------------------------------------------------------------------------------------------------- |
| `000`              | `11000`        | `000123456789` | Succeeds the payment immediately after micro-deposits are verified.                                        |
| `000`              | `11000`        | `900123456789` | Succeeds the payment with a three-minute delay after micro-deposits are verified.                          |
| `000`              | `11000`        | `000222222227` | Fails the payment immediately after micro-deposits are verified.                                           |
| `000`              | `11000`        | `900222222227` | Fails the payment with a three-minute delay after micro-deposits are verified.                             |
| `000`              | `11000`        | `000666666661` | Fails to send verification micro-deposits.                                                                 |
| `000`              | `11000`        | `000777777771` | Fails the payment due to the payment amount causing the account to exceed its weekly payment volume limit. |
| `000`              | `11000`        | `000888888881` | Fails the payment due to the payment amount exceeding the account’s transaction limit.                     |

To mimic successful or failed bank account verifications in a sandbox, use these meaningful amounts for micro-deposits:

| Micro-deposit Values          | Scenario                                                         |
| ----------------------------- | ---------------------------------------------------------------- |
| `32` and `45`                 | Successfully verifies the account.                               |
| `10` and `11`                 | Simulates exceeding the number of allowed verification attempts. |
| Any other number combinations | Fails account verification.                                      |

## Optional: Instant only verification [Server-side]

By default, Canadian pre-authorized debit payments allow your customers to use instant bank account verification or micro-deposits. You can optionally require instant bank account verification only using the [verification_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-acss_debit-verification_method) parameter when you create the PaymentIntent.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'cad',
  setup_future_usage: 'off_session',
  customer_account: '{{CUSTOMERACCOUNT_ID}}',
  payment_method_types: ['acss_debit'],
  payment_method_options: {
    acss_debit: {
      mandate_options: {
        payment_schedule: 'interval',
        interval_description: 'First day of every month',
        transaction_type: 'personal',
      },
      verification_method: 'instant',
    },
  },
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'cad',
  setup_future_usage: 'off_session',
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['acss_debit'],
  payment_method_options: {
    acss_debit: {
      mandate_options: {
        payment_schedule: 'interval',
        interval_description: 'First day of every month',
        transaction_type: 'personal',
      },
      verification_method: 'instant',
    },
  },
});
```

## Optional: Micro-deposit only verification [Server-side]

By default, Canadian pre-authorized debit payments allow your customers to use instant bank account verification or micro-deposits. You can optionally require micro-deposit verification only using the [verification_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-acss_debit-verification_method) parameter when you create the PaymentIntent.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'cad',
  setup_future_usage: 'off_session',
  customer_account: '{{CUSTOMERACCOUNT_ID}}',
  payment_method_types: ['acss_debit'],
  payment_method_options: {
    acss_debit: {
      mandate_options: {
        payment_schedule: 'interval',
        interval_description: 'First day of every month',
        transaction_type: 'personal',
      },
      verification_method: 'microdeposits',
    },
  },
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'cad',
  setup_future_usage: 'off_session',
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['acss_debit'],
  payment_method_options: {
    acss_debit: {
      mandate_options: {
        payment_schedule: 'interval',
        interval_description: 'First day of every month',
        transaction_type: 'personal',
      },
      verification_method: 'microdeposits',
    },
  },
});
```

## Optional: Configure customer debit date [Server-side]

You can control the date that Stripe debits a customer’s bank account using the [target date](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-payment_method_options-acss_debit-target_date). The target date must be at least three days in the future and no more than 15 days from the current date.

The target date schedules money to leave the customer’s account on the target date. You can [cancel a PaymentIntent](https://docs.stripe.com/api/payment_intents/cancel.md) created with a target date up to three business days before the configured date.

Target dates that meet one of the following criteria delay the debit until next available business day:

- Target date falls on a weekend, a bank holiday, or other non-business day.
- Target date is fewer than three business days in the future.

This parameter operates on a best-effort basis. Each customer’s bank might process debits on different dates, depending on local bank holidays or other reasons.

> You can’t set the [verification method](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-payment_method_options-acss_debit-verification_method) to `microdeposits` when using a [target date](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-payment_method_options-acss_debit-target_date), as the verification process could take longer than the target date, causing payments to arrive later than expected.

## See also

- [Save Canadian pre-authorized debit details for future payments](https://docs.stripe.com/payments/acss-debit/set-up-payment.md)
