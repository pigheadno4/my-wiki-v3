<!-- Source URL: https://docs.stripe.com/payments/acss-debit/set-up-payment -->
<!-- Fetched: 2026-05-02 -->

# Save details for future payments with pre-authorized debit in Canada

Save payment method details for future Canadian pre-authorized debit payments.

# Checkout

> This is a Checkout for when payment-ui is checkout. View the full page at https://docs.stripe.com/payments/acss-debit/set-up-payment?payment-ui=checkout.

You can use the [Setup Intents API](https://docs.stripe.com/payments/setup-intents.md) to collect payment method details in advance, with the final amount or payment date determined later. This is useful for:

- Saving payment methods to a wallet to streamline future purchases
- Collecting surcharges after fulfilling a service
- Starting a free trial for a subscription

> Pre-authorized debit in Canada is a **delayed notification payment method**, which means that funds aren’t immediately available after payment. A payment typically takes **5 business days** to arrive in your account.

Most bank accounts in Canada hold Canadian dollars (CAD), with a small number of accounts in other currencies, including US dollars (USD). It’s possible to accept PAD payments in either CAD or USD, but choosing the correct currency for your customer is important to avoid payment failures.

Unlike many card-based payment methods, you might not be able to successfully debit a CAD account in USD or debit a USD account in CAD. Most often, attempting to do so results in a delayed payment failure that takes up to five business days.

To avoid these failures, it’s safest to set up PAD bank accounts in CAD unless you’re confident your customer’s account accepts USD debits.

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create or retrieve a Customer [Server-side]

To reuse a bank account for future payments, it must be attached to a [Customer](https://docs.stripe.com/api/customers.md).

Create a Customer object when your customer creates an account with your business. Associating the ID of the Customer object with your own internal representation of a customer lets you retrieve and use the stored payment method details later. If your customer hasn’t created an account, you can still create a Customer object now and associate it with your internal representation of the customer’s account later.

Create a new Customer or retrieve an existing Customer to associate with these payment details. Include the following code on your server to create a new Customer.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customer = await stripe.customers.create();
```

## Set up future payments

> This guide builds on the foundational [set up future payments](https://docs.stripe.com/payments/save-and-reuse.md) Checkout integration.

Use this guide to learn how to enable Canadian Pre-Authorized Debits (PADs)—it shows the differences between setting up future payments using dynamic payment methods and manually configuring payment methods and using PADs.

### Enable Canadian pre-authorized debit as a payment method

When creating a new [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md), you need to:

1. Add `acss_debit` to the list of `payment_method_types`.
1. Specify additional [payment_method_options](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-payment_method_options-acss_debit) parameters to describe your transaction. Learn more below.

Payments must specify a [payment schedule](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_method_options-acss_debit-mandate_options-payment_schedule) for customers to authorize when checking out. See [PAD Mandates](https://docs.stripe.com/payments/acss-debit.md#mandates) for details on how to choose the right mandate options for your business:

| Parameter                                                                   | Value                                                                                                                                                                                                                                      | Required                                                         |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| `payment_method_options[acss_debit][currency]`                              | Currency to use for future payments with this payment method. Must match the customer’s bank account currency. Accepted values are `cad` or `usd`.                                                                                         | Yes                                                              |
| `payment_method_options[acss_debit][mandate_options][payment_schedule]`     | The mandate payment schedule. Accepted values are `interval`, `sporadic`, or `combined`. See the [PAD Mandates](https://docs.stripe.com/payments/acss-debit.md#mandates) overview to help you select the right schedule for your business. | Yes                                                              |
| `payment_method_options[acss_debit][mandate_options][interval_description]` | Text description of the payment schedule. See the [PAD Mandates](https://docs.stripe.com/payments/acss-debit.md#mandates) overview to help you construct the right interval description for your business.                                 | Required if `payment_schedule` value is `interval` or `combined` |
| `payment_method_options[acss_debit][mandate_options][transaction_type]`     | The type of transactions you’ll use the mandate for, either `personal` (if the transactions are for personal reasons) or `business` (if the transactions are for business reasons).                                                        | Yes                                                              |
| `payment_method_options[acss_debit][mandate_options][default_for]`          | An array of mandate purposes. For more information, see the [PAD mandates](https://docs.stripe.com/payments/acss-debit.md#mandates) overview to choose the right default purpose for your business.                                        | No                                                               |

### Create a Checkout session

#### Stripe-hosted page

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({
  customer: '{{CUSTOMER_ID}}',
  mode: 'setup',
  payment_method_options: {
    acss_debit: {
      currency: 'cad',
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
  customer: '{{CUSTOMER_ID}}',
  mode: 'setup',
  payment_method_options: {
    acss_debit: {
      currency: 'cad',
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

During the Checkout session, the customer is presented with a UI modal that handles bank account details collection and instant verification with an optional fallback to verification using microdeposits. If the customer opts for microdeposit verification, Stripe automatically sends two small deposits to the provided bank account which take 1-2 business days to appear on the customer’s online bank statement. When the deposits are expected to arrive, the customer receives an email with a link to *confirm* (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) these amounts and verify the bank account with Stripe. After verification is completed, the payment method is ready to be used for future payments.

## Test your integration

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

## Use the payment method [Server-side]

After completing the Checkout Session, you can [collect](https://docs.stripe.com/payments/checkout/save-and-reuse.md?payment-ui=stripe-hosted#retrieve-checkout-session) the [PaymentMethod](https://docs.stripe.com/api/payment_methods.md) ID and a [Mandate](https://docs.stripe.com/api/mandates.md) ID. You can use these to initiate future payments without having to prompt the customer for their bank account a second time.

> Future pre-authorized debit payments must be charged according to the terms of the existing mandate. Debiting at any time that doesn’t meet the terms of the mandate could be cause for a payment dispute.

When you’re ready to charge your customer off-session, provide the `payment_method`, `customer`, and `mandate` IDs when [creating a PaymentIntent](https://docs.stripe.com/api/payment_intents/create.md).

If you haven’t captured the SetupIntent ID yet, look up the PaymentMethod and Mandate to charge by [listing](https://docs.stripe.com/api/setup_intents/list.md) the SetupIntents associated with your customer:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntents = await stripe.setupIntents.list({
  customer: '{{CUSTOMER_ID}}',
});
```

### Reuse a payment method with an existing authorized mandate

When you have the PaymentMethod and Mandate IDs from the applicable SetupIntent, create a PaymentIntent with the amount and currency of the payment. Set a few other parameters to make the *off-session payment* (A payment is described as off-session if it occurs without the direct involvement of the customer, using previously-collected payment information):

- Set the value of the PaymentIntent’s [confirm](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-confirm) property to `true`, which causes confirmation to occur immediately when the PaymentIntent is created.
- Set [payment_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method) to the ID of the PaymentMethod, [mandate](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-mandate) to the ID of the Mandate, and [customer](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-customer) to the ID of the Customer.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ['acss_debit'],
  payment_method: '{{PAYMENTMETHOD_ID}}',
  customer: '{{CUSTOMER_ID}}',
  mandate: '{{MANDATE_ID}}',
  confirm: true,
  amount: 100,
  currency: 'cad',
});
```

When reusing an existing mandate with the new PaymentIntent, a debit notification email must be sent at that time. Stripe handles this for you by default, unless you choose to [send custom notifications](https://docs.stripe.com/payments/acss-debit.md#mandate-and-debit-notification-emails).

## Optional: Instant only verification [Server-side]

By default, Canadian pre-authorized debit payments allow your customers to use instant bank account verification or micro-deposits. You can optionally require instant bank account verification only using the `payment_method_options[acss_debit][verification_method]` parameter when you create the Checkout session.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({
  mode: 'setup',
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  payment_method_types: ['acss_debit'],
  payment_method_options: {
    acss_debit: {
      currency: 'cad',
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
  mode: 'setup',
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['acss_debit'],
  payment_method_options: {
    acss_debit: {
      currency: 'cad',
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
  mode: 'setup',
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  payment_method_types: ['acss_debit'],
  payment_method_options: {
    acss_debit: {
      currency: 'cad',
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
  mode: 'setup',
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['acss_debit'],
  payment_method_options: {
    acss_debit: {
      currency: 'cad',
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

# Direct API

> This is a Direct API for when payment-ui is direct-api. View the full page at https://docs.stripe.com/payments/acss-debit/set-up-payment?payment-ui=direct-api.

You can use the [Setup Intents API](https://docs.stripe.com/payments/setup-intents.md) to collect payment method details in advance, with the final amount or payment date determined later. This is useful for:

- Saving payment methods to a wallet to streamline future purchases
- Collecting surcharges after fulfilling a service
- Starting a free trial for a *subscription* (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis)

Most bank accounts in Canada hold Canadian dollars (CAD), with a small number of accounts in other currencies, including US dollars (USD). It’s possible to accept PAD payments in either CAD or USD, but choosing the correct currency for your customer is important to avoid payment failures.

Unlike many card-based payment methods, you might not be able to successfully debit a CAD account in USD or debit a USD account in CAD. Most often, attempting to do so results in a delayed payment failure that takes up to five business days.

To avoid these failures, it’s safest to set up PAD bank accounts in CAD unless you’re confident your customer’s account accepts USD debits.

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create or retrieve a Customer [Server-side]

To reuse a bank account for future payments, it must be attached to a *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments).

You should create a Customer object when your customer creates an account with your business. Associating the ID of the Customer object with your own internal representation of a customer enables you to retrieve and use the stored payment method details later. If your customer hasn’t created an account, you can still create a Customer object now and associate it with your internal representation of the customer’s account later.

Create a new Customer or retrieve an existing Customer to associate with these payment details. Include the following code on your server to create a new Customer.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customer = await stripe.customers.create();
```

## Create a SetupIntent [Server-side]

A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) is an object that represents your intent to set up a customer’s payment method for future payments. The `SetupIntent` tracks the steps of this set-up process.

To use Canadian pre-authorized debits, you must obtain authorization from your customer for one-time and recurring debits using a pre-authorized debit agreement (see [PAD Mandates](https://docs.stripe.com/payments/acss-debit.md#mandates)). The [Mandate](https://docs.stripe.com/api/mandates.md) object records this agreement and authorization.

Create a SetupIntent on your server with [payment_method_types](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-payment_method_types) set to `acss_debit` and specify the Customer’s [id](https://docs.stripe.com/api/customers/object.md#customer_object-id). To define a payment schedule on the [Mandate](https://docs.stripe.com/api/mandates.md) for this SetupIntent, also include the following parameters:

| Parameter                                                                   | Value                                                                                                                                                                                                                                      | Required                                                    |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------- |
| `payment_method_options[acss_debit][currency]`                              | Currency to use for future payments with this payment method. Must match the customer’s bank account currency. Accepted values are `cad` or `usd`.                                                                                         | Yes                                                         |
| `payment_method_options[acss_debit][mandate_options][payment_schedule]`     | The mandate payment schedule. Accepted values are `interval`, `sporadic`, or `combined`. See the [PAD Mandates](https://docs.stripe.com/payments/acss-debit.md#mandates) overview to help you select the right schedule for your business. | Yes                                                         |
| `payment_method_options[acss_debit][mandate_options][interval_description]` | Text description of the interval of payment schedule. See the [PAD Mandates](https://docs.stripe.com/payments/acss-debit.md#mandates) overview to help you construct the right interval description for your business.                     | If `payment_schedule` specified as `interval` or `combined` |
| `payment_method_options[acss_debit][mandate_options][transaction_type]`     | The type of transactions you’ll use the mandate for, either `personal` (if the transactions are for personal reasons) or `business` (if the transactions are for business reasons).                                                        | Yes                                                         |
| `payment_method_options[acss_debit][mandate_options][default_for]`          | An array of mandate purposes. For more information, see the [PAD mandates](https://docs.stripe.com/payments/acss-debit.md#mandates) overview to choose the right default purpose for your business.                                        | No                                                          |

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ['acss_debit'],
  customer: '{{CUSTOMER_ID}}',
  payment_method_options: {
    acss_debit: {
      currency: 'cad',
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

The SetupIntent includes a *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)) that the client side uses to securely complete the payment process. You can use different approaches to pass the client secret to the client side.

#### Single-page application

Retrieve the client secret from an endpoint on your server, using the browser’s `fetch` function. This approach is best if your client side is a single-page application, particularly one built with a modern frontend framework like React. Create the server endpoint that serves the client secret:

#### Node.js

```javascript
const express = require('express');
const app = express();

app.get('/secret', async (req, res) => {
  const intent = // ... Fetch or create the SetupIntent
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

Add the [client_secret](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-client_secret) in your checkout form. In your server-side code, retrieve the client secret from the SetupIntent:

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
  const intent = // ... Fetch or create the SetupIntent
    res.render('checkout', { client_secret: intent.client_secret });
});

app.listen(3000, () => {
  console.log('Running on port 3000');
});
```

## Collect payment method details and mandate acknowledgement [Client-side]

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

Use [stripe.confirmAcssDebitSetup](https://docs.stripe.com/js/setup_intents/confirm_acss_debit_setup) to collect bank account details and verification, confirm the mandate, and complete the setup when the user submits the form. Including the customer’s email address and the account holder’s name in the `billing_details` property of the `payment_method` parameter is required to create a PAD payment method.

```javascript
const form = document.getElementById('payment-form');
const accountholderName = document.getElementById('accountholder-name');
const email = document.getElementById('email');
const submitButton = document.getElementById('submit-button');
const clientSecret = submitButton.dataset.secret;

form.addEventListener('submit', async (event) => {
  event.preventDefault();

  const { setupIntent, error } = await stripe.confirmAcssDebitSetup(
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
    // Handle next step based on SetupIntent's status.
    console.log('SetupIntent ID: ' + setupIntent.id);
    console.log('SetupIntent status: ' + setupIntent.status);
  }
});
```

Stripe.js then loads an on-page modal UI that handles bank account details collection and verification, presents a hosted mandate agreement and collects authorization.

> `stripe.confirmAcssDebitSetup` might take several seconds to complete. During that time, disable your form from being resubmitted and show a waiting indicator like a spinner. If you receive an error, show it to the customer, re-enable the form, and hide the waiting indicator.

If successful, Stripe returns a [SetupIntent](https://docs.stripe.com/api/setup_intents/object.md) object, with one of the following possible statuses:

| Status            | Description                                                                    | Next step                                                                                                                                          |
| ----------------- | ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `succeeded`       | The bank account has been instantly verified or verification wasn’t necessary. | No action needed                                                                                                                                   |
| `requires_action` | Further action needed to complete bank account verification.                   | Step 5: [Verifying bank accounts with micro-deposits](https://docs.stripe.com/payments/acss-debit/set-up-payment.md#web-verify-with-microdeposits) |

After successfully confirming the SetupIntent, an email confirmation of the mandate and collected bank account details must be sent to your customer. Stripe handles these by default, but you can choose to [send custom notifications](https://docs.stripe.com/payments/acss-debit.md#mandate-and-debit-notification-emails) if you prefer.

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

The result of the `stripe.confirmAcssDebitSetup` method call is a SetupIntent in the `requires_action` state. The SetupIntent contains a `next_action` field that contains some useful information for completing the verification.

Stripe notifies your customer at the [billing email](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-billing_details-email) when the deposits are expected to arrive. The email includes a link to a Stripe-hosted verification page where they can confirm the amounts of the deposits and complete verification.

There is a limit of three failed verification attempts. If this limit is exceeded, the bank account can no longer be verified. In addition, there is a timeout for micro-deposit verifications of 10 days. If micro-deposits aren’t verified in that time, the PaymentIntent reverts to requiring new payment method details. Clear messaging about what these micro-deposits are and how you use them can help your customers avoid verification issues.

### Optional: Custom email and verification page

If you choose to send [custom email notifications](https://docs.stripe.com/payments/acss-debit.md#mandate-and-debit-notification-emails), you have to email your customer instead. To do this, you can use the `verify_with_microdeposits[hosted_verification_url]` URL in the `next_action` object to direct your customer to complete the verification process.

If you’re sending custom emails and don’t want to use the Stripe hosted verification page, you can create a form on your site for your customers to relay these amounts to you and verify the bank account using [Stripe.js](https://docs.stripe.com/js/payment_intents/verify_microdeposits_for_payment).

```javascript
stripe.verifyMicrodepositsForSetup(clientSecret, {
  amounts: [32, 45],
});
```

When the bank account is successfully verified, Stripe returns the [SetupIntent object](https://docs.stripe.com/api/setup_intents/object.md), with a `status` of `succeeded`, and sends a `setup_intent.succeeded` webhook event.

Verification can fail for several reasons. The failure might happen synchronously as a direct error response, or asynchronously through a `setup_intent.payment_failed` webhook event (shown in the following examples).

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
    "id": "seti_1234",
    "object": "setup_intent",
    "customer": "cus_0246",
    ...
    "last_setup_error": {
      "code": "payment_method_microdeposit_verification_attempts_exceeded",
      "message": "You have exceeded the number of allowed verification attempts."
    },
    ...
    "status": "requires_payment_method"
  }
}
```

| Error Code                                                   | Synchronous or asynchronous                             | Message                                                                                                                                         | Status Change                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `payment_method_microdeposit_failed`                         | Synchronously, or asynchronously through webhook event  | Microdeposits failed. Please check the account, institution and transit numbers provided                                                        | `status` is `requires_payment_method`, and `last_setup_error` is set. |
| `payment_method_microdeposit_verification_amounts_mismatch`  | Synchronously                                           | The amounts provided don’t match the amounts that were sent to the bank account. You have {attempts_remaining} verification attempts remaining. | Unchanged                                                             |
| `payment_method_microdeposit_verification_attempts_exceeded` | Synchronously, and asynchronously through webhook event | Exceeded number of allowed verification attempts                                                                                                | `status` is `requires_payment_method`, and `last_setup_error` is set. |
| `payment_method_microdeposit_verification_timeout`           | Asynchronously through webhook event                    | Microdeposit timeout. Customer hasn’t verified their bank account within the required 10 day period.                                            | `status` is `requires_payment_method`, and `last_setup_error` is set. |

## Test your integration

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

## Optional: Accept future payments [Server-side]

After completing the SetupIntent, you have a new *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) object and a [mandate](https://docs.stripe.com/api/mandates.md) object. You can use the objects to initiate future payments without having to prompt the customer for their bank account a second time.

> Future pre-authorized debit payments must be charged according to the terms of the existing mandate. Debiting at any time that doesn’t meet the terms of the mandate can cause a payment dispute.

When you’re ready to charge your customer off-session, use the customer, PaymentMethod, and mandate IDs to create a PaymentIntent.

If you haven’t captured the SetupIntent ID yet, look up the PaymentMethod and Mandate to charge by [listing](https://docs.stripe.com/api/setup_intents/list.md) the SetupIntents associated with your customer:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntents = await stripe.setupIntents.list({
  customer: '{{CUSTOMER_ID}}',
});
```

### Reuse a payment method with an existing authorized mandate

When you have the PaymentMethod and Mandate IDs from the applicable SetupIntent, create a PaymentIntent with the amount and currency of the payment. Set a few other parameters to make the *off-session payment* (A payment is described as off-session if it occurs without the direct involvement of the customer, using previously-collected payment information):

- Set the value of the PaymentIntent’s [confirm](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-confirm) property to `true`, which causes confirmation to occur immediately when the PaymentIntent is created.
- Set [payment_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method) to the ID of the PaymentMethod, [mandate](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-mandate) to the ID of the Mandate, and [customer](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-customer) to the ID of the Customer.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ['acss_debit'],
  payment_method: '{{PAYMENTMETHOD_ID}}',
  customer: '{{CUSTOMER_ID}}',
  mandate: '{{MANDATE_ID}}',
  confirm: true,
  amount: 100,
  currency: 'cad',
});
```

When reusing an existing mandate with the new PaymentIntent, a debit notification email must be sent at that time. Stripe handles this for you by default, unless you choose to [send custom notifications](https://docs.stripe.com/payments/acss-debit.md#mandate-and-debit-notification-emails).

### Reuse a payment method with a new mandate

If you need to collect a debit from a customer using different terms, but want to avoid requiring them to enter their bank account info again, you can still reuse the existing PaymentMethod and get your customer’s authorization for a new mandate. To do so, follow the instructions for [creating a new PaymentIntent](https://docs.stripe.com/payments/acss-debit/accept-a-payment.md#web-create-payment-intent) or [creating a new SetupIntent](https://docs.stripe.com/payments/acss-debit/set-up-payment.md#web-create-setup-intent), with the following changes:

- Include the additional parameter `payment_method` with the ID for the existing PaymentMethod as its value when creating the new PaymentIntent or SetupIntent.
- Omit the `payment_method` and `acss_debit` data in the payment method details submit step when calling `stripe.confirmAcssDebitPayment` or `stripe.confirmAcssDebitSetup`.

> Verification isn’t required for PaymentIntents and SetupIntents created with a reused PaymentMethod and a new Mandate, but you must send a new mandate confirmation email, and charges will be delayed for three days.

## Optional: Instant only verification [Server-side]

By default, Canadian pre-authorized debit payments allow your customers to use instant bank account verification or micro-deposits. You can optionally require instant bank account verification only using the [verification_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-acss_debit-verification_method) parameter when you create the PaymentIntent.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ['acss_debit'],
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  payment_method_options: {
    acss_debit: {
      currency: 'cad',
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

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ['acss_debit'],
  customer: '{{CUSTOMER_ID}}',
  payment_method_options: {
    acss_debit: {
      currency: 'cad',
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

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ['acss_debit'],
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  payment_method_options: {
    acss_debit: {
      currency: 'cad',
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

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ['acss_debit'],
  customer: '{{CUSTOMER_ID}}',
  payment_method_options: {
    acss_debit: {
      currency: 'cad',
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

## See also

- [Accept a Canadian pre-authorized debit payment](https://docs.stripe.com/payments/acss-debit/accept-a-payment.md)
