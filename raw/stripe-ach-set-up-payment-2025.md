<!-- Source URL: https://docs.stripe.com/payments/ach-direct-debit/set-up-payment -->
<!-- Fetched: 2026-05-02 -->

# Save details for future payments with ACH Direct Debit

Learn how to save payment method details for future ACH Direct Debit payments.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

# Checkout

> This is a Checkout for when payment-ui is checkout. View the full page at https://docs.stripe.com/payments/ach-direct-debit/set-up-payment?payment-ui=checkout.

You can use Checkout in [setup mode](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-mode) to collect payment method details in advance, with the final amount or payment date determined later. This is useful for:

- Saving payment methods to a wallet to streamline future purchases
- Collecting surcharges after fulfilling a service
- Starting a free trial for a _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis)

> ACH Direct Debit is a [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method, which means that funds aren’t immediately available after payment. A payment typically takes 4 business days to arrive in your account.

## Before you begin

This guide shows you how to extend the foundational [set up future payments](https://docs.stripe.com/payments/save-and-reuse.md?platform=web&ui=stripe-hosted) Checkout integration to add support for ACH Direct Debit payments.

## Create or retrieve a customer [Recommended] [Server-side]

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

#### Accounts v2

Create a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-configuration-customer) object when your user creates an account with your business, or retrieve an existing `Account` associated with this user. Associating the ID of the `Account` object with your own internal representation of a customer enables you to retrieve and use the stored payment method details later. Include an email address on the `Account` to enable Financial Connections’ [return user optimization](https://docs.stripe.com/financial-connections/fundamentals.md#return-user-optimization).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const account = await stripe.v2.core.accounts.create({
  contact_email: "{{CUSTOMER_EMAIL}}",
});
```

#### Customers v1

Create a _Customer_ (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) object when your user creates an account with your business, or retrieve an existing `Customer` associated with this user. Associating the ID of the `Customer` object with your own internal representation of a customer enables you to retrieve and use the stored payment method details later. Include an email address on the `Customer` to enable Financial Connections’ [return user optimization](https://docs.stripe.com/financial-connections/fundamentals.md#return-user-optimization).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customer = await stripe.customers.create({
  email: "{{CUSTOMER_EMAIL}}",
});
```

## Enable ACH Direct Debit as a payment method

When creating a new [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md), you need to:

1. Add `us_bank_account` to the list of `payment_method_types`.
1. Set the `permissions` parameter to include `payment_method`.

#### Stripe-hosted page

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({
  customer: '{{CUSTOMER_ID}}',
  mode: 'setup',
  payment_method_options: {
    us_bank_account: {
      financial_connections: {
        permissions: ['payment_method'],
      },
    },
  },
  payment_method_types: ['card', 'us_bank_account'],
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
    us_bank_account: {
      financial_connections: {
        permissions: ['payment_method'],
      },
    },
  },
  payment_method_types: ['card', 'us_bank_account'],
  return_url: 'https://example.com/return',
  ui_mode: 'embedded_page',
});
```

For more information on Financial Connections fees, see [pricing details](https://stripe.com/financial-connections#pricing).

By default, collecting bank account payment information uses [Financial Connections](https://docs.stripe.com/financial-connections.md) to instantly verify your customer’s account, with a fallback option of manual account number entry and microdeposit verification. See the [Financial Connections docs](https://docs.stripe.com/financial-connections/ach-direct-debit-payments.md) to learn how to configure Financial Connections and access additional account data to optimize your ACH integration. For example, you can use Financial Connections to check an account’s balance before initiating the ACH payment.

> To expand access to additional data after a customer authenticates their account, they must re-link their account with expanded permissions.

During the Checkout session, the customer sees a dialog that gives them the option to use instant verification or provide bank account details for microdeposit verification.

If the customer opts for microdeposit verification, Stripe automatically sends two small deposits to the provided bank account. These deposits can take 1-2 business days to appear on the customer’s online bank statement. When the deposits arrive, the customer receives an email with a link to confirm these amounts and verify the bank account with Stripe. After verification completes, the payment begins processing.

## Test your integration

Learn how to test scenarios with instant verifications using [Financial Connections](https://docs.stripe.com/financial-connections/testing.md#web-how-to-use-test-accounts).

### Send transaction emails in a sandbox

After you collect the bank account details and accept a mandate, send the mandate confirmation and microdeposit verification emails in a _sandbox_ (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes).

If your domain is **{domain}** and your username is **{username}**, use the following email format to send test transaction emails: **{username}+test_email@{domain}**.

For example, if your domain is **example.com** and your username is **info**, use the format **info+test\_email@example.com** for testing ACH Direct Debit payments. This format ensures that emails route correctly. If you don’t include the **+test_email** suffix, we won’t send the email.

> You must [set up your Stripe account](https://docs.stripe.com/get-started/account/set-up.md) before you can trigger these emails while testing.

### Test account numbers

Stripe provides several test account numbers and corresponding tokens you can use to make sure your integration for manually-entered bank accounts is ready for production.

| Account number | Token                                  | Routing number | Behavior                                                                                                                                              |
| -------------- | -------------------------------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `000123456789` | `pm_usBankAccount_success`             | `110000000`    | The payment succeeds.                                                                                                                                 |
| `000111111113` | `pm_usBankAccount_accountClosed`       | `110000000`    | The payment fails because the account is closed.                                                                                                      |
| `000000004954` | `pm_usBankAccount_riskLevelHighest`    | `110000000`    | The payment is blocked by Radar due to a [high risk of fraud](https://docs.stripe.com/radar/risk-evaluation.md#high-risk).                            |
| `000111111116` | `pm_usBankAccount_noAccount`           | `110000000`    | The payment fails because no account is found.                                                                                                        |
| `000222222227` | `pm_usBankAccount_insufficientFunds`   | `110000000`    | The payment fails due to insufficient funds.                                                                                                          |
| `000333333335` | `pm_usBankAccount_debitNotAuthorized`  | `110000000`    | The payment fails because debits aren’t authorized.                                                                                                   |
| `000444444440` | `pm_usBankAccount_invalidCurrency`     | `110000000`    | The payment fails due to invalid currency.                                                                                                            |
| `000666666661` | `pm_usBankAccount_failMicrodeposits`   | `110000000`    | The payment fails to send microdeposits.                                                                                                              |
| `000555555559` | `pm_usBankAccount_dispute`             | `110000000`    | The payment triggers a dispute.                                                                                                                       |
| `000000000009` | `pm_usBankAccount_processing`          | `110000000`    | The payment stays in processing indefinitely. Useful for testing [PaymentIntent cancellation](https://docs.stripe.com/api/payment_intents/cancel.md). |
| `000777777771` | `pm_usBankAccount_weeklyLimitExceeded` | `110000000`    | The payment fails due to payment amount causing the account to exceed its weekly payment volume limit.                                                |
| `000888888885` |                                        | `110000000`    | The payment fails because of a deactivated [tokenized account number](https://docs.stripe.com/financial-connections/tokenized-account-numbers.md).    |

Before test transactions can complete, you need to verify all test accounts that automatically succeed or fail the payment. To do so, use the test microdeposit amounts or descriptor codes below.

### Test microdeposit amounts and descriptor codes

To mimic different scenarios, use these microdeposit amounts _or_ 0.01 descriptor code values.

| Microdeposit values | 0.01 descriptor code values | Scenario                                                         |
| ------------------- | --------------------------- | ---------------------------------------------------------------- |
| `32` and `45`       | SM11AA                      | Simulates verifying the account.                                 |
| `10` and `11`       | SM33CC                      | Simulates exceeding the number of allowed verification attempts. |
| `40` and `41`       | SM44DD                      | Simulates a microdeposit timeout.                                |

### Test settlement behavior

Test transactions settle instantly and are added to your available test balance. This behavior differs from livemode, where transactions can take [multiple days](https://docs.stripe.com/payments/ach-direct-debit/set-up-payment.md#timing) to settle in your available balance.

## Use the payment method

After completing the Checkout Session, you can [collect](https://docs.stripe.com/payments/checkout/save-and-reuse.md?payment-ui=stripe-hosted#retrieve-checkout-session) the [PaymentMethod](https://docs.stripe.com/api/payment_methods.md) ID. You can use these PaymentMethod IDs to initiate future payments without having to prompt the customer for their bank account a second time.

When [creating a PaymentIntent](https://docs.stripe.com/api/payment_intents/create.md), provide the `payment_method` and customer IDs to charge your customer using their saved bank account information.

## Optional: Instant only verification

By default, ACH Direct Debit payments allow your customers to use instant bank account verification or microdeposits. You can optionally require instant bank account verification only, using the `payment_method_options[us_bank_account][verification_method]` parameter when you create the Checkout session.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({
  mode: 'setup',
  customer_account: '{{CUSTOMERACCOUNT_ID}}',
  payment_method_types: ['card', 'us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      verification_method: 'instant',
      financial_connections: {
        permissions: ['payment_method', 'balances'],
      },
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
  payment_method_types: ['card', 'us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      verification_method: 'instant',
      financial_connections: {
        permissions: ['payment_method', 'balances'],
      },
    },
  },
  success_url: 'https://example.com/success',
});
```

## Optional: Access data on a Financial Connections bank account

You can only access Financial Connections data if you request additional [data permissions](https://docs.stripe.com/financial-connections/fundamentals.md#data-permissions) when you create your SetupIntent.

After your customer successfully completes the [Stripe Financial Connections authentication flow](https://docs.stripe.com/financial-connections/fundamentals.md#authentication-flow), the `us_bank_account` PaymentMethod returned includes a [financial_connections_account](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-us_bank_account-financial_connections_account) ID that points to a [Financial Connections Account](https://docs.stripe.com/api/financial_connections/accounts.md). Use this ID to access account data.

> Bank accounts that your customers link through manual entry and microdeposits don’t have a `financial_connections_account` ID on the Payment Method.

To determine the Financial Connections account ID, retrieve the SetupIntent and expand the `payment_method` attribute:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.retrieve("{{SETUPINTENT_ID}}", {
  expand: ["payment_method"],
});
```

```json
{
  "id": "{{SETUP_INTENT_ID}}",
  "object": "setup_intent",
  // ...
  "payment_method": {
    "id": "{{PAYMENT_METHOD_ID}}",
    // ...
    "type": "us_bank_account"
    "us_bank_account": {
      "account_holder_type": "individual",
      "account_type": "checking",
      "bank_name": "TEST BANK","financial_connections_account": "{{FINANCIAL_CONNECTIONS_ACCOUNT_ID}}",
      "fingerprint": "q9qchffggRjlX2tb",
      "last4": "6789",
      "routing_number": "110000000"
    }
  }
  // ...
}

```

If you have access to balances data, we recommend [checking balances](https://docs.stripe.com/financial-connections/balances.md#initiate-balance-refresh) before initiating payments with the collected Payment Method.

Learn more about using additional account data to optimize your ACH integration with [Financial Connections](https://docs.stripe.com/financial-connections/ach-direct-debit-payments.md#optimize).

## Optional: Updating the default payment method

After the `SetupIntent` reaches the `succeeded` state, you can update your customer’s `default_payment_method`.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

if (event.type == "setup_intent.succeeded") {
  const setup_intent = event.data.object;
  const customer_id = setup_intent.customer;
  const payment_method_id = setup_intent.payment_method;

  const customer = await stripe.customers.update(customer_id, {
    invoice_settings: { default_payment_method: payment_method_id },
  });
}
```

# Elements

> This is a Elements for when payment-ui is elements. View the full page at https://docs.stripe.com/payments/ach-direct-debit/set-up-payment?payment-ui=elements.

You can use the [Setup Intents API](https://docs.stripe.com/payments/setup-intents.md) to collect payment method details in advance, with the final amount or payment date determined later. This is useful for:

- Saving payment methods to a wallet to streamline future purchases
- Collecting surcharges after fulfilling a service
- Starting a free trial for a _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis)

> ACH Direct Debit is a [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method, which means that funds aren’t immediately available after payment. A payment typically takes 4 business days to arrive in your account.

## Create or retrieve a customer [Recommended] [Server-side]

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

#### Accounts v2

Create a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-configuration-customer) object when your user creates an account with your business, or retrieve an existing `Account` associated with this user. Associating the ID of the `Account` object with your own internal representation of a customer enables you to retrieve and use the stored payment method details later. Include an email address on the `Account` to enable Financial Connections’ [return user optimization](https://docs.stripe.com/financial-connections/fundamentals.md#return-user-optimization).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const account = await stripe.v2.core.accounts.create({
  contact_email: "{{CUSTOMER_EMAIL}}",
});
```

#### Customers v1

Create a _Customer_ (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) object when your user creates an account with your business, or retrieve an existing `Customer` associated with this user. Associating the ID of the `Customer` object with your own internal representation of a customer enables you to retrieve and use the stored payment method details later. Include an email address on the `Customer` to enable Financial Connections’ [return user optimization](https://docs.stripe.com/financial-connections/fundamentals.md#return-user-optimization).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customer = await stripe.customers.create({
  email: "{{CUSTOMER_EMAIL}}",
});
```

## Create a SetupIntent [Server-side]

A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) is an object that represents your intent to set up a customer’s payment method for future payments. The `SetupIntent` tracks the steps of this set-up process.

Create a SetupIntent on your server with [payment_method_types](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-payment_method_types) set to us_bank_account and specify the Customer’s [id](https://docs.stripe.com/api/customers/object.md#customer_object-id).

For more information on Financial Connections fees, see [pricing details](https://stripe.com/financial-connections#pricing).

By default, collecting bank account payment information uses [Financial Connections](https://docs.stripe.com/financial-connections.md) to instantly verify your customer’s account, with a fallback option of manual account number entry and microdeposit verification. See the [Financial Connections docs](https://docs.stripe.com/financial-connections/ach-direct-debit-payments.md) to learn how to configure Financial Connections and access additional account data to optimize your ACH integration. For example, you can use Financial Connections to check an account’s balance before initiating the ACH payment.

> To expand access to additional data after a customer authenticates their account, they must re-link their account with expanded permissions.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.create({
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      financial_connections: {
        permissions: ['payment_method', 'balances'],
      },
    },
  },
});
```

### Retrieve the client secret

The SetupIntent includes a _client secret_ (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)) that the client side uses to securely complete the payment process. You can use different approaches to pass the client secret to the client side.

#### Single-page application

Retrieve the client secret from an endpoint on your server, using the browser’s `fetch` function. This approach is best if your client side is a single-page application, particularly one built with a modern frontend framework like React. Create the server endpoint that serves the client secret:

#### Node.js

```javascript
const express = require("express");
const app = express();

app.get("/secret", async (req, res) => {
  const intent = // ... Fetch or create the SetupIntent
    res.json({ client_secret: intent.client_secret });
});

app.listen(3000, () => {
  console.log("Running on port 3000");
});
```

And then fetch the client secret with JavaScript on the client side:

```javascript
(async () => {
  const response = await fetch("/secret");
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
const express = require("express");
const expressHandlebars = require("express-handlebars");
const app = express();

app.engine(".hbs", expressHandlebars({ extname: ".hbs" }));
app.set("view engine", ".hbs");
app.set("views", "./views");

app.get("/checkout", async (req, res) => {
  const intent = // ... Fetch or create the SetupIntent
    res.render("checkout", { client_secret: intent.client_secret });
});

app.listen(3000, () => {
  console.log("Running on port 3000");
});
```

## Collect payment method details [Client-side]

When a customer clicks to pay with ACH Direct Debit, we recommend you use Stripe.js to submit the payment to Stripe. [Stripe.js](https://docs.stripe.com/payments/elements.md) is our foundational JavaScript library for building payment flows. It will automatically handle integration complexities, and enables you to easily extend your integration to other payment methods in the future.

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
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");
```

Rather than sending the entire SetupIntent object to the client, use its _client secret_ (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)) from the previous step. This is different from your API keys that authenticate Stripe API requests.

Handle the client secret carefully because it can complete the Payment Method setup process. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

Use [stripe.collectBankAccountForSetup](https://docs.stripe.com/js/setup_intents/collect_bank_account_for_setup) to collect bank account details with [Financial Connections](https://docs.stripe.com/financial-connections.md), create a _PaymentMethod_ (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs), and attach that PaymentMethod to the SetupIntent. Including the account holder’s name in the `billing_details` parameter is required to create an ACH Direct Debit PaymentMethod.

```javascript
// Use the form that already exists on the web page.
const paymentMethodForm = document.getElementById("payment-method-form");
const confirmationForm = document.getElementById("confirmation-form");

paymentMethodForm.addEventListener("submit", (ev) => {
  ev.preventDefault();
  const accountHolderNameField = document.getElementById(
    "account-holder-name-field",
  );
  const emailField = document.getElementById("email-field");

  // Calling this method will open the instant verification dialog.
  stripe
    .collectBankAccountForSetup({
      clientSecret: clientSecret,
      params: {
        payment_method_type: "us_bank_account",
        payment_method_data: {
          billing_details: {
            name: accountHolderNameField.value,
            email: emailField.value,
          },
        },
      },
      expand: ["payment_method"],
    })
    .then(({ setupIntent, error }) => {
      if (error) {
        console.error(error.message);
        // PaymentMethod collection failed for some reason.
      } else if (setupIntent.status === "requires_payment_method") {
        // Customer canceled the hosted verification modal. Present them with other
        // payment method type options.
      } else if (setupIntent.status === "requires_confirmation") {
        // We collected an account - possibly instantly verified, but possibly
        // manually-entered. Display payment method details and mandate text
        // to the customer and confirm the intent once they accept
        // the mandate.
        confirmationForm.show();
      }
    });
});
```

The [Financial Connections authentication flow](https://docs.stripe.com/financial-connections/fundamentals.md#authentication-flow) automatically handles bank account details collection and verification. When your customer completes the authentication flow, the _PaymentMethod_ (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) automatically attaches to the SetupIntent, and creates a [Financial Connections Account](https://docs.stripe.com/api/financial_connections/accounts.md).

> Bank accounts that your customers link through manual entry and microdeposits won’t have access to additional bank account data like balances, ownership, and transactions.

To provide the best user experience on all devices, set the viewport `minimum-scale` for your page to 1 using the viewport `meta` tag.

```html
<meta name="viewport" content="width=device-width, minimum-scale=1" />
```

## Optional: Access data on a Financial Connections bank account [Server-side]

You can only access Financial Connections data if you request additional [data permissions](https://docs.stripe.com/financial-connections/fundamentals.md#data-permissions) when you create your SetupIntent.

After your customer successfully completes the [Stripe Financial Connections authentication flow](https://docs.stripe.com/financial-connections/fundamentals.md#authentication-flow), the `us_bank_account` PaymentMethod returned includes a [financial_connections_account](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-us_bank_account-financial_connections_account) ID that points to a [Financial Connections Account](https://docs.stripe.com/api/financial_connections/accounts.md). Use this ID to access account data.

> Bank accounts that your customers link through manual entry and microdeposits don’t have a `financial_connections_account` ID on the Payment Method.

To determine the Financial Connections account ID, retrieve the SetupIntent and expand the `payment_method` attribute:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.retrieve("{{SETUPINTENT_ID}}", {
  expand: ["payment_method"],
});
```

```json
{
  "id": "{{SETUP_INTENT_ID}}",
  "object": "setup_intent",
  // ...
  "payment_method": {
    "id": "{{PAYMENT_METHOD_ID}}",
    // ...
    "type": "us_bank_account"
    "us_bank_account": {
      "account_holder_type": "individual",
      "account_type": "checking",
      "bank_name": "TEST BANK","financial_connections_account": "{{FINANCIAL_CONNECTIONS_ACCOUNT_ID}}",
      "fingerprint": "q9qchffggRjlX2tb",
      "last4": "6789",
      "routing_number": "110000000"
    }
  }
  // ...
}

```

If you have access to balances data, we recommend [checking balances](https://docs.stripe.com/financial-connections/balances.md#initiate-balance-refresh) before initiating payments with the collected Payment Method.

Learn more about using additional account data to optimize your ACH integration with [Financial Connections](https://docs.stripe.com/financial-connections/ach-direct-debit-payments.md#optimize).

## Collect mandate acknowledgement and submit [Client-side]

Before you can complete the SetupIntent and save the payment method details for the customer, you must obtain authorization for payment by displaying mandate terms for the customer to accept.

To be compliant with Nacha rules, you must obtain authorization from your customer before you can initiate payment by displaying mandate terms for them to accept. For more information on mandates, see [Mandates](https://docs.stripe.com/payments/ach-direct-debit.md#mandates).

When the customer accepts the mandate terms, you must confirm the SetupIntent. Use [stripe.confirmUsBankAccountSetup](https://docs.stripe.com/js/setup_intents/confirm_us_bank_account_setup) to complete the payment when the customer submits the form.

```javascript
confirmationForm.addEventListener("submit", (ev) => {
  ev.preventDefault();
  stripe
    .confirmUsBankAccountSetup(clientSecret)
    .then(({ setupIntent, error }) => {
      if (error) {
        console.error(error.message);
        // The payment failed for some reason.
      } else if (setupIntent.status === "requires_payment_method") {
        // Confirmation failed. Attempt again with a different payment method.
      } else if (setupIntent.status === "succeeded") {
        // Confirmation succeeded! The account is now saved.
        // Display a message to customer.
      } else if (
        setupIntent.next_action?.type === "verify_with_microdeposits"
      ) {
        // The account needs to be verified through microdeposits.
        // Display a message to consumer with next steps (consumer waits for
        // microdeposits, then enters a statement descriptor code on a page sent to them through email).
      }
    });
});
```

> [stripe.confirmUsBankAccountSetup](https://docs.stripe.com/js/setup_intents/confirm_us_bank_account_setup) might take several seconds to complete. During that time, disable resubmittals of your form and show a waiting indicator (for example, a spinner). If you receive an error, show it to the customer, re-enable the form, and hide the waiting indicator.

If successful, Stripe returns a SetupIntent object, with one of the following possible statuses:

| Status            | Description                                                                    | Next Steps                                                                                                                                                |
| ----------------- | ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `succeeded`       | The bank account has been instantly verified or verification wasn’t necessary. | No action needed                                                                                                                                          |
| `requires_action` | Further action needed to complete bank account verification.                   | Step 6: [Verifying bank accounts with microdeposits](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md#web-verify-with-microdeposits) |

After successfully confirming the SetupIntent, an email confirmation of the mandate and collected bank account details must be sent to your customer. Stripe handles these by default, but you can choose to [send custom notifications](https://docs.stripe.com/payments/ach-direct-debit.md#mandate-and-microdeposit-emails) if you prefer.

## Verify bank account with microdeposits [Client-side]

Not all customers can verify the bank account instantly. This step only applies if your customer has elected to opt out of the instant verification flow in the previous step.

In these cases, Stripe sends a `descriptor_code` microdeposit and might fall back to an `amount` microdeposit if any further issues arise with verifying the bank account. These deposits take 1-2 business days to appear on the customer’s online statement.

- **Descriptor code**. Stripe sends a single, 0.01 USD microdeposit to the customer’s bank account with a unique, 6-digit `descriptor_code` that starts with SM. Your customer uses this string to verify their bank account.
- **Amount**. Stripe sends two, non-unique microdeposits to the customer’s bank account, with a statement descriptor that reads `ACCTVERIFY`. Your customer uses the deposit amounts to verify their bank account.

The result of the [stripe.confirmUsBankAccountSetup](https://docs.stripe.com/js/setup_intents/confirm_us_bank_account_setup) method call in the previous step is a SetupIntent in the `requires_action` state. The SetupIntent contains a `next_action` field that contains some useful information for completing the verification.

```javascript
next_action: {
  type: "verify_with_microdeposits",
  verify_with_microdeposits: {
    arrival_date: 1647586800,
    hosted_verification_url: "https://payments.stripe.com/…",
    microdeposit_type: "descriptor_code"
  }
}
```

If you supplied a [billing email](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-billing_details-email), Stripe notifies your customer through this email when the deposits are expected to arrive. The email includes a link to a Stripe-hosted verification page where they can confirm the amounts of the deposits and complete verification.

> Verification attempts have a limit of ten failures for descriptor-based microdeposits and three for amount-based ones. If you exceed this limit, we can no longer verify the bank account. In addition, microdeposit verifications have a timeout of 10 days. If you can’t verify microdeposits in that time, the SetupIntent reverts to requiring new payment method details. Clear messaging about what these microdeposits are and how you use them can help your customers avoid verification issues.

### Optional: Send custom email notifications

Optionally, you can send [custom email notifications](https://docs.stripe.com/payments/ach-direct-debit.md#mandate-and-microdeposit-emails) to your customer. After you set up custom emails, you need to specify how the customer responds to the verification email. To do so, choose _one_ of the following:

- Use the Stripe-hosted verification page. To do this, use the `verify_with_microdeposits[hosted_verification_url]` URL in the [next_action](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-verify_with_microdeposits-hosted_verification_url) object to direct your customer to complete the verification process.

- If you prefer not to use the Stripe-hosted verification page, create a form on your site. Your customers then use this form to relay microdeposit amounts to you and verify the bank account using [Stripe.js](https://docs.stripe.com/js/payment_intents/verify_microdeposits_for_payment).
  - At minimum, set up the form to handle the `descriptor code` parameter, which is a 6-digit string for verification purposes.
  - Stripe also recommends that you set your form to handle the `amounts` parameter, as some banks your customers use might require it.

  Integrations only pass in the `descriptor_code` _or_ `amounts`. To determine which one your integration uses, check the value for `verify_with_microdeposits[microdeposit_type]` in the `next_action` object.

```javascript
stripe.verifyMicrodepositsForSetup(clientSecret, {
  // Provide either a descriptor_code OR amounts, not both
  descriptor_code: `SMT86W`,
  amounts: [32, 45],
});
```

When the bank account is successfully verified, Stripe returns the SetupIntent object with a `status` of `succeeded`, and sends a [setup_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.succeeded) _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event.

Verification can fail for several reasons. The failure might happen synchronously as a direct error response, or asynchronously through a [setup_intent.setup_failed](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.setup_failed) webhook event (shown in the following examples).

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
      "message": "You have exceeded the number of allowed verification attempts.",
    },
    ...
    "status": "requires_payment_method"
  }
}
```

| Error Code                                                   | Synchronous or Asynchronous                            | Message                                                                                                                                         | Status change                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `payment_method_microdeposit_failed`                         | Synchronously, or asynchronously through webhook event | Microdeposits failed. Please check the account, institution and transit numbers provided                                                        | `status` is `requires_payment_method`, and `last_setup_error` is set. |
| `payment_method_microdeposit_verification_amounts_mismatch`  | Synchronously                                          | The amounts provided don’t match the amounts that were sent to the bank account. You have {attempts_remaining} verification attempts remaining. | Unchanged                                                             |
| `payment_method_microdeposit_verification_attempts_exceeded` | Synchronously, or asynchronously through webhook event | Exceeded number of allowed verification attempts                                                                                                | `status` is `requires_payment_method`, and `last_setup_error` is set. |
| `payment_method_microdeposit_verification_timeout`           | Asynchronously through webhook event                   | Microdeposit timeout. Customer hasn’t verified their bank account within the required 10 day period.                                            | `status` is `requires_payment_method`, and `last_setup_error` is set. |

## Test your integration

Learn how to test scenarios with instant verifications using [Financial Connections](https://docs.stripe.com/financial-connections/testing.md#web-how-to-use-test-accounts).

### Send transaction emails in a sandbox

After you collect the bank account details and accept a mandate, send the mandate confirmation and microdeposit verification emails in a _sandbox_ (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes).

If your domain is **{domain}** and your username is **{username}**, use the following email format to send test transaction emails: **{username}+test_email@{domain}**.

For example, if your domain is **example.com** and your username is **info**, use the format **info+test\_email@example.com** for testing ACH Direct Debit payments. This format ensures that emails route correctly. If you don’t include the **+test_email** suffix, we won’t send the email.

> You must [set up your Stripe account](https://docs.stripe.com/get-started/account/set-up.md) before you can trigger these emails while testing.

### Test account numbers

Stripe provides several test account numbers and corresponding tokens you can use to make sure your integration for manually-entered bank accounts is ready for production.

| Account number | Token                                  | Routing number | Behavior                                                                                                                                              |
| -------------- | -------------------------------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `000123456789` | `pm_usBankAccount_success`             | `110000000`    | The payment succeeds.                                                                                                                                 |
| `000111111113` | `pm_usBankAccount_accountClosed`       | `110000000`    | The payment fails because the account is closed.                                                                                                      |
| `000000004954` | `pm_usBankAccount_riskLevelHighest`    | `110000000`    | The payment is blocked by Radar due to a [high risk of fraud](https://docs.stripe.com/radar/risk-evaluation.md#high-risk).                            |
| `000111111116` | `pm_usBankAccount_noAccount`           | `110000000`    | The payment fails because no account is found.                                                                                                        |
| `000222222227` | `pm_usBankAccount_insufficientFunds`   | `110000000`    | The payment fails due to insufficient funds.                                                                                                          |
| `000333333335` | `pm_usBankAccount_debitNotAuthorized`  | `110000000`    | The payment fails because debits aren’t authorized.                                                                                                   |
| `000444444440` | `pm_usBankAccount_invalidCurrency`     | `110000000`    | The payment fails due to invalid currency.                                                                                                            |
| `000666666661` | `pm_usBankAccount_failMicrodeposits`   | `110000000`    | The payment fails to send microdeposits.                                                                                                              |
| `000555555559` | `pm_usBankAccount_dispute`             | `110000000`    | The payment triggers a dispute.                                                                                                                       |
| `000000000009` | `pm_usBankAccount_processing`          | `110000000`    | The payment stays in processing indefinitely. Useful for testing [PaymentIntent cancellation](https://docs.stripe.com/api/payment_intents/cancel.md). |
| `000777777771` | `pm_usBankAccount_weeklyLimitExceeded` | `110000000`    | The payment fails due to payment amount causing the account to exceed its weekly payment volume limit.                                                |
| `000888888885` |                                        | `110000000`    | The payment fails because of a deactivated [tokenized account number](https://docs.stripe.com/financial-connections/tokenized-account-numbers.md).    |

Before test transactions can complete, you need to verify all test accounts that automatically succeed or fail the payment. To do so, use the test microdeposit amounts or descriptor codes below.

### Test microdeposit amounts and descriptor codes

To mimic different scenarios, use these microdeposit amounts _or_ 0.01 descriptor code values.

| Microdeposit values | 0.01 descriptor code values | Scenario                                                         |
| ------------------- | --------------------------- | ---------------------------------------------------------------- |
| `32` and `45`       | SM11AA                      | Simulates verifying the account.                                 |
| `10` and `11`       | SM33CC                      | Simulates exceeding the number of allowed verification attempts. |
| `40` and `41`       | SM44DD                      | Simulates a microdeposit timeout.                                |

### Test settlement behavior

Test transactions settle instantly and are added to your available test balance. This behavior differs from livemode, where transactions can take [multiple days](https://docs.stripe.com/payments/ach-direct-debit/set-up-payment.md#timing) to settle in your available balance.

## Accepting future payments [Server-side]

When the SetupIntent succeeds, it will create a new _PaymentMethod_ (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) attached to a [Customer](https://docs.stripe.com/api/customers.md). These can be used to initiate future payments without having to prompt the customer for their bank account a second time.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const intent = await stripe.paymentIntents.create({
  payment_method_types: ['us_bank_account'],
  payment_method: setup_intent.payment_method,
  customer: setup_intent.customer,
  confirm: true,
  amount: 100,
  currency: 'usd',
});
```

## Optional: Instant only verification [Server-side]

By default, setting up a US bank account payment method allows your customers to use instant bank account verification or microdeposits. You can optionally require instant bank account verification only, using the [verification_method](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-payment_method_options-us_bank_account-verification_method) parameter when you create the SetupIntent.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.create({
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      verification_method: 'instant',
      financial_connections: {
        permissions: ['payment_method', 'balances'],
      },
    },
  },
});
```

This ensures that you don’t need to handle microdeposit verification. However, if instant verification fails, the SetupIntent’s status is `requires_payment_method`, indicating a failure to instantly verify a bank account for your customer.

## Optional: Microdeposit only verification [Server-side]

By default, setting up a US bank account payment method lets your customers use instant bank account verification or microdeposits. You can optionally require microdeposit verification using the [verification_method](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-payment_method_options-us_bank_account-verification_method) parameter when you create the SetupIntent.

> If using a custom payment form, you must build your own UI to collect bank account details. If you disable Stripe microdeposit emails, you must build your own UI for your customer to confirm the microdeposit code or amount.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.create({
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      verification_method: "microdeposits",
    },
  },
});
```

You must then collect your customer’s bank account with your own form and call [stripe.confirmUsBankAccountSetup](https://docs.stripe.com/js/setup_intents/confirm_us_bank_account_setup) with those details to complete the SetupIntent.

```javascript
var form = document.getElementById('payment-form');
var accountholderName = document.getElementById('accountholder-name');
var email = document.getElementById('email');
var accountNumber = document.getElementById('account-number');
var routingNumber = document.getElementById('routing-number');
var accountHolderType= document.getElementById('account-holder-type');

var submitButton = document.getElementById('submit-button');
var clientSecret = submitButton.dataset.secret;

form.addEventListener('submit', function(event) {
  event.preventDefault();

  stripe.confirmUsBankAccountSetup(clientSecret, {
    payment_method: {
      billing_details: {
        name: accountholderName.value,
        email: email.value,
      },
      us_bank_account: {
        account_number: accountNumber.value,
        routing_number: routingNumber.value,
        account_holder_type: accountHolderType.value, // 'individual' or 'company'
      },
    },
  })
  .then({setupIntent, error} => {
    if (error) {
      // Inform the customer that there was an error.
      console.log(error.message);
    } else {
      // Handle next step based on the intent's status.
      console.log("SetupIntent ID: " + setupIntent.id);
      console.log("SetupIntent status: " + setupIntent.status);
    }
  });
});
```

## Optional: Updating the default payment method [Server-side]

After the `SetupIntent` reaches the `succeeded` state, you can update your customer’s `default_payment_method`.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

if (event.type == "setup_intent.succeeded") {
  const setup_intent = event.data.object;
  const customer_id = setup_intent.customer;
  const payment_method_id = setup_intent.payment_method;

  const customer = await stripe.customers.update(customer_id, {
    invoice_settings: { default_payment_method: payment_method_id },
  });
}
```

# iOS

> This is a iOS for when payment-ui is mobile and platform is ios. View the full page at https://docs.stripe.com/payments/ach-direct-debit/set-up-payment?payment-ui=mobile&platform=ios.

You can use the [Setup Intents API](https://docs.stripe.com/payments/setup-intents.md) to collect payment method details in advance, with the final amount or payment date determined later. This is useful for:

- Saving payment methods to a wallet to streamline future purchases
- Collecting surcharges after fulfilling a service
- Starting a free trial for a _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis)

> ACH Direct Debit is a [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method, which means that funds aren’t immediately available after payment. A payment typically takes 4 business days to arrive in your account.

The [iOS SDK](https://github.com/stripe/stripe-ios) is open source, [fully documented](https://stripe.dev/stripe-ios/index.html), and compatible with apps supporting iOS 13 or above.

#### Swift Package Manager

To install the SDK:

1. In Xcode, select **File** > **Add Package Dependencies…** and enter `https://github.com/stripe/stripe-ios-spm` as the repository URL.
1. Select the latest version number from our [releases page](https://github.com/stripe/stripe-ios/releases).
1. Add the **StripePayments** and **StripeFinancialConnections** products to the [target of your app](https://developer.apple.com/documentation/swift_packages/adding_package_dependencies_to_your_app).

#### CocoaPods

1. If you haven’t already, install the latest version of [CocoaPods](https://guides.cocoapods.org/using/getting-started.html).
1. If you don’t have an existing [Podfile](https://guides.cocoapods.org/syntax/podfile.html), run the following command to create one:
   ```bash
   pod init
   ```
1. Add this line to your `Podfile`:
   ```podfile
   pod 'Stripe'
   pod 'StripeFinancialConnections'
   ```
1. Run the following command:
   ```bash
   pod install
   ```
1. Don’t forget to use the `.xcworkspace` file to open your project in Xcode, instead of the `.xcodeproj` file, from here on out.
1. In the future, to update to the latest version of the SDK, run:
   ```bash
   pod update Stripe
   pod update StripeFinancialConnections
   ```

#### Carthage

1. If you haven’t already, install the latest version of [Carthage](https://github.com/Carthage/Carthage#installing-carthage).
1. Add this line to your `Cartfile`:
   ```cartfile
   github "stripe/stripe-ios"
   ```
1. Follow the [Carthage installation instructions](https://github.com/Carthage/Carthage#if-youre-building-for-ios-tvos-or-watchos). Make sure to embed all of the required frameworks listed [here](https://github.com/stripe/stripe-ios#releases).
1. In addition to the required frameworks in the link above, be sure to also include the framework **StripeFinancialConnections**
1. In the future, to update to the latest version of the SDK, run the following command:
   ```bash
   carthage update stripe-ios --platform ios
   ```

#### Manual Framework

1. Head to our [GitHub releases page](https://github.com/stripe/stripe-ios/releases/latest) and download and unzip **Stripe.xcframework.zip**.
1. Drag **Stripe.xcframework** to the **Embedded Binaries** section of the **General** settings in your Xcode project. Make sure to select **Copy items if needed**.
1. Repeat step 2 for **StripeFinancialConnections.xcframework**
1. Repeat step 2 for all required frameworks listed [here](https://github.com/stripe/stripe-ios#releases).
1. In the future, to update to the latest version of our SDK, repeat steps 1–3.

> For details on the latest SDK release and past versions, see the [Releases](https://github.com/stripe/stripe-ios/releases) page on GitHub. To receive notifications when a new release is published, [watch releases for the repository](https://help.github.com/en/articles/watching-and-unwatching-releases-for-a-repository#watching-releases-for-a-repository).

Configure the SDK with your Stripe [publishable key](https://dashboard.stripe.com/test/apikeys) on app start. This enables your app to make requests to the Stripe API.

#### Swift

```swift
import UIKitimportStripeFinancialConnections

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {StripeAPI.defaultPublishableKey = "<<YOUR_PUBLISHABLE_KEY>>"
        // do any other necessary launch configuration
        return true
    }
}
```

> Use your [test keys](https://docs.stripe.com/keys.md#obtain-api-keys) while you test and develop, and your [live mode](https://docs.stripe.com/keys.md#test-live-modes) keys when you publish your app.

## Create or retrieve a customer [Recommended] [Server-side]

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

#### Accounts v2

Create a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-configuration-customer) object when your user creates an account with your business, or retrieve an existing `Account` associated with this user. Associating the ID of the `Account` object with your own internal representation of a customer enables you to retrieve and use the stored payment method details later. Include an email address on the `Account` to enable Financial Connections’ [return user optimization](https://docs.stripe.com/financial-connections/fundamentals.md#return-user-optimization).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const account = await stripe.v2.core.accounts.create({
  contact_email: "{{CUSTOMER_EMAIL}}",
});
```

#### Customers v1

Create a _Customer_ (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) object when your user creates an account with your business, or retrieve an existing `Customer` associated with this user. Associating the ID of the `Customer` object with your own internal representation of a customer enables you to retrieve and use the stored payment method details later. Include an email address on the `Customer` to enable Financial Connections’ [return user optimization](https://docs.stripe.com/financial-connections/fundamentals.md#return-user-optimization).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customer = await stripe.customers.create({
  email: "{{CUSTOMER_EMAIL}}",
});
```

## Create a SetupIntent [Server-side] [Client-side]

A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) is an object that represents your intent to set up a customer’s payment method for future payments. The `SetupIntent` tracks the steps of this set-up process.

### Server-side

Create a SetupIntent on your server with [payment_method_types](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-payment_method_types) set to us_bank_account and specify the Customer’s [id](https://docs.stripe.com/api/customers/object.md#customer_object-id).

For more information on Financial Connections fees, see [pricing details](https://stripe.com/financial-connections#pricing).

By default, collecting bank account payment information uses [Financial Connections](https://docs.stripe.com/financial-connections.md) to instantly verify your customer’s account, with a fallback option of manual account number entry and microdeposit verification. See the [Financial Connections docs](https://docs.stripe.com/financial-connections/ach-direct-debit-payments.md) to learn how to configure Financial Connections and access additional account data to optimize your ACH integration. For example, you can use Financial Connections to check an account’s balance before initiating the ACH payment.

> To expand access to additional data after a customer authenticates their account, they must re-link their account with expanded permissions.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.create({
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      financial_connections: {
        permissions: ['payment_method', 'balances'],
      },
    },
  },
});
```

### Client-side

Included in the returned SetupIntent is a _client secret_ (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)), which the client side uses to securely complete the setup instead of passing the entire SetupIntent object. There are different approaches that you can use to pass the client secret to the client side.

#### Swift

```swift
import UIKit
import StripePayments

class CheckoutViewController: UIViewController {
  var setupIntentClientSecret: String?

  func startCheckout() {
      // Request a SetupIntent from your server and store its client secret
  }
}}
```

## Set up a return URL [Client-side]

The customer might navigate away from your app to authenticate (for example, in Safari or their banking app). To allow them to automatically return to your app after authenticating, [configure a custom URL scheme](https://developer.apple.com/documentation/xcode/defining-a-custom-url-scheme-for-your-app) and set up your app delegate to forward the URL to the SDK. Stripe doesn’t support [universal links](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content).

> Stripe might append additional parameters to the provided return URL. Make sure that return URLs with extra parameters aren’t rejected by your code.

#### SceneDelegate

#### Swift

```swift
// This method handles opening custom URL schemes (for example, "your-app://stripe-redirect")
func scene(_ scene: UIScene, openURLContexts URLContexts: Set<UIOpenURLContext>) {
    guard let url = URLContexts.first?.url else {
        return
    }
    let stripeHandled = StripeAPI.handleURLCallback(with: url)
    if (!stripeHandled) {
        // This was not a Stripe url – handle the URL normally as you would
    }
}

```

#### AppDelegate

#### Swift

```swift
// This method handles opening custom URL schemes (for example, "your-app://stripe-redirect")
func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey: Any] = [:]) -> Bool {
    let stripeHandled = StripeAPI.handleURLCallback(with: url)
    if (stripeHandled) {
        return true
    } else {
        // This was not a Stripe url – handle the URL normally as you would
    }
    return false
}
```

#### SwiftUI

#### Swift

```swift

@main
struct MyApp: App {
  var body: some Scene {
    WindowGroup {
      Text("Hello, world!").onOpenURL { incomingURL in
          let stripeHandled = StripeAPI.handleURLCallback(with: incomingURL)
          if (!stripeHandled) {
            // This was not a Stripe url – handle the URL normally as you would
          }
        }
    }
  }
}
```

## Collect payment method details [Client-side]

ACH Direct Debit requires a customer name and (optional) email for the setupIntent to succeed. In your app, collect the required billing details from the customer:

- Their full name (first and last)
- Their email address

Use the class function `collectUSBankAccountParams` in `STPCollectBankAccountParams` to create your parameters required to call `collectBankAccountForSetup`.

Create an instance of `BankAccountCollector` to call `collectBankAccountForSetup` to collect bank account details, create a _PaymentMethod_ (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs), and attach that PaymentMethod to the SetupIntent. Including the account holder’s name in the `billing_details` parameter is required to create an ACH Direct Debit PaymentMethod.

#### Swift

```swift
// Build params
let collectParams = STPCollectBankAccountParams.collectUSBankAccountParams(with: name, email: email)

// Calling this method will display a modal for collecting bank account information
let bankAccountCollector = STPBankAccountCollector()
bankAccountCollector.collectBankAccountForSetup(clientSecret: clientSecret,
                                                returnURL: "https://your-app-domain.com/stripe-redirect",
                                                params: collectParams,
                                                from: self) { intent, error in
    guard let intent = intent else {
        // handle error
        return
    }
    if case .requiresPaymentMethod = intent.status {
        // Customer canceled the Financial Connections modal. Present them with other
        // payment method type options.
    } else if case .requiresConfirmation = intent.status {
        // We collected an account - possibly instantly verified, but possibly
        // manually-entered. Display payment method details and mandate text
        // to the customer and confirm the intent once they accept
        // the mandate.
    }
}
```

This loads a modal UI that handles bank account details collection and verification. When it completes, the _PaymentMethod_ (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) automatically attaches to the SetupIntent.

## Optional: Access data on a Financial Connections bank account [Server-side]

You can only access Financial Connections data if you request additional [data permissions](https://docs.stripe.com/financial-connections/fundamentals.md#data-permissions) when you create your SetupIntent.

After your customer successfully completes the [Stripe Financial Connections authentication flow](https://docs.stripe.com/financial-connections/fundamentals.md#authentication-flow), the `us_bank_account` PaymentMethod returned includes a [financial_connections_account](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-us_bank_account-financial_connections_account) ID that points to a [Financial Connections Account](https://docs.stripe.com/api/financial_connections/accounts.md). Use this ID to access account data.

> Bank accounts that your customers link through manual entry and microdeposits don’t have a `financial_connections_account` ID on the Payment Method.

To determine the Financial Connections account ID, retrieve the SetupIntent and expand the `payment_method` attribute:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.retrieve("{{SETUPINTENT_ID}}", {
  expand: ["payment_method"],
});
```

```json
{
  "id": "{{SETUP_INTENT_ID}}",
  "object": "setup_intent",
  // ...
  "payment_method": {
    "id": "{{PAYMENT_METHOD_ID}}",
    // ...
    "type": "us_bank_account"
    "us_bank_account": {
      "account_holder_type": "individual",
      "account_type": "checking",
      "bank_name": "TEST BANK","financial_connections_account": "{{FINANCIAL_CONNECTIONS_ACCOUNT_ID}}",
      "fingerprint": "q9qchffggRjlX2tb",
      "last4": "6789",
      "routing_number": "110000000"
    }
  }
  // ...
}

```

If you have access to balances data, we recommend [checking balances](https://docs.stripe.com/financial-connections/balances.md#initiate-balance-refresh) before initiating payments with the collected Payment Method.

Learn more about using additional account data to optimize your ACH integration with [Financial Connections](https://docs.stripe.com/financial-connections/ach-direct-debit-payments.md#optimize).

## Collect mandate acknowledgement and submit [Client-side]

Before you can complete the SetupIntent and save the payment method details for the customer, you must obtain authorization for payment by displaying mandate terms for the customer to accept.

To be compliant with _Nacha_ (Nacha is the governing body that oversees the ACH network) rules, you must obtain authorization from your customer before you can initiate payment by displaying mandate terms for them to accept. For more information on mandates, see [Mandates](https://docs.stripe.com/payments/ach-direct-debit.md#mandates).

When the customer accepts the mandate terms, you must confirm the SetupIntent. Use `confirmSetupIntent` to complete the payment when the customer submits the form.

#### Swift

```swift
let setupIntentParams = STPSetupIntentConfirmParams(clientSecret: clientSecret, paymentMethodType: .USBankAccount)
STPPaymentHandler.shared().confirmSetupIntent(
    setupIntentParams, with: self
) { (status, intent, error) in
    switch status {
    case .failed:
        // Payment failed
    case .canceled:
        // Payment was canceled
    case .succeeded:
        // Payment succeeded
    @unknown default:
        fatalError()
    }
}
```

> `confirmSetupIntent` might take several seconds to complete. During that time, disable resubmittals of your form and show a waiting indicator (for example, a spinner). If you receive an error, show it to the customer, re-enable the form, and hide the waiting indicator.

If successful, Stripe returns a SetupIntent object, with one of the following possible statuses:

| Status            | Description                                                                    | Next Steps                                                                                                                                                |
| ----------------- | ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `succeeded`       | The bank account has been instantly verified or verification wasn’t necessary. | No action needed                                                                                                                                          |
| `requires_action` | Further action needed to complete bank account verification.                   | Step 6: [Verifying bank accounts with microdeposits](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md#ios-verify-with-microdeposits) |

After successfully confirming the SetupIntent, an email confirmation of the mandate and collected bank account details must be sent to your customer. Stripe handles these by default, but you can choose to [send custom notifications](https://docs.stripe.com/payments/ach-direct-debit.md#mandate-and-microdeposit-emails) if you prefer.

## Verify bank account with microdeposits [Client-side]

Not all customers can verify the bank account instantly. This step only applies if your customer has elected to opt out of the instant verification flow in the previous step.

In these cases, Stripe sends a `descriptor_code` microdeposit and might fall back to an `amount` microdeposit if any further issues arise with verifying the bank account. These deposits take 1-2 business days to appear on the customer’s online statement.

- **Descriptor code**. Stripe sends a single, 0.01 USD microdeposit to the customer’s bank account with a unique, 6-digit `descriptor_code` that starts with SM. Your customer uses this string to verify their bank account.
- **Amount**. Stripe sends two, non-unique microdeposits to the customer’s bank account, with a statement descriptor that reads `ACCTVERIFY`. Your customer uses the deposit amounts to verify their bank account.

The result of the `confirmSetupIntent` method call in the previous step is a SetupIntent in the `requires_action` state. The SetupIntent contains a [next_action](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-next_action-verify_with_microdeposits) field that contains some useful information for completing the verification.

If you supplied a [billing email](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-billing_details-email), Stripe notifies your customer through this email when the deposits are expected to arrive. The email includes a link to a Stripe-hosted verification page where they can confirm the amounts of the deposits and complete verification.

> Verification attempts have a limit of ten failures for descriptor-based microdeposits and three for amount-based ones. If you exceed this limit, we can no longer verify the bank account. In addition, microdeposit verifications have a timeout of 10 days. If you can’t verify microdeposits in that time, the PaymentIntent reverts to requiring new payment method details. Clear messaging about what these microdeposits are and how you use them can help your customers avoid verification issues.

### Optional: Send custom email notifications

You can also send [custom email notifications](https://docs.stripe.com/payments/ach-direct-debit.md#mandate-and-microdeposit-emails) to your customer. After you set up custom emails, you need to specify how the customer responds to the verification email. To do so, choose _one_ of the following:

- Use the Stripe-hosted verification page. To do this, use the `verify_with_microdeposits[hosted_verification_url]` URL in the [next_action](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-verify_with_microdeposits-hosted_verification_url) object to direct your customer to complete the verification process.

- If you prefer not to use the Stripe-hosted verification page, create a form in your app. Your customers then use this form to relay microdeposit amounts to you and verify the bank account using the iOS SDK.
  - At minimum, set up the form to handle the `descriptor code` parameter, which is a 6-digit string for verification purposes.
  - Stripe also recommends that you set your form to handle the `amounts` parameter, as some banks your customers use might require it.

  Integrations only pass in the `descriptor_code` _or_ `amounts`. To determine which one your integration uses, check the value for `verify_with_microdeposits[microdeposit_type]` in the `next_action` object.

#### Swift

```swift
// Use if you are using a descriptor code, do not use if you are using amounts
STPAPIClient.shared.verifySetupIntentWithMicrodeposits(clientSecret: clientSecret,
                                                       descriptorCode: descriptorCode,
                                                       completion: { intent, error in
})

// Use if you are using amounts, do not use if you are using descriptor code
STPAPIClient.shared.verifySetupIntentWithMicrodeposits(clientSecret: clientSecret,
                                                       firstAmount: firstAmount,
                                                       secondAmount: secondAmount,
                                                       completion: { intent, error in
})
```

When the bank account is successfully verified, Stripe returns the SetupIntent object with a `status` of `succeeded`.

Verification can fail for several reasons. The failure happens synchronously as a direct error response.

```json
{
  "error": {
    "code": "payment_method_microdeposit_verification_amounts_mismatch",
    "message": "The amounts provided do not match the amounts that were sent to the bank account. You have {attempts_remaining} verification attempts remaining.",
    "type": "invalid_request_error"
  }
}
```

| Error Code                                                   | Message                                                                                                                                         | Status change                                                         |
| ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `payment_method_microdeposit_failed`                         | Microdeposits failed. Please check the account, institution and transit numbers provided.                                                       | `status` is `requires_payment_method`, and `last_setup_error` is set. |
| `payment_method_microdeposit_verification_amounts_mismatch`  | The amounts provided don’t match the amounts that were sent to the bank account. You have {attempts_remaining} verification attempts remaining. | Unchanged                                                             |
| `payment_method_microdeposit_verification_attempts_exceeded` | Exceeded number of allowed verification attempts                                                                                                | `status` is `requires_payment_method`, and `last_setup_error` is set. |

## Test your integration

Learn how to test scenarios with instant verifications using [Financial Connections](https://docs.stripe.com/financial-connections/testing.md#web-how-to-use-test-accounts).

### Send transaction emails in a sandbox

After you collect the bank account details and accept a mandate, send the mandate confirmation and microdeposit verification emails in a _sandbox_ (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes).

If your domain is **{domain}** and your username is **{username}**, use the following email format to send test transaction emails: **{username}+test_email@{domain}**.

For example, if your domain is **example.com** and your username is **info**, use the format **info+test\_email@example.com** for testing ACH Direct Debit payments. This format ensures that emails route correctly. If you don’t include the **+test_email** suffix, we won’t send the email.

> You must [set up your Stripe account](https://docs.stripe.com/get-started/account/set-up.md) before you can trigger these emails while testing.

### Test account numbers

Stripe provides several test account numbers and corresponding tokens you can use to make sure your integration for manually-entered bank accounts is ready for production.

| Account number | Token                                  | Routing number | Behavior                                                                                                                                              |
| -------------- | -------------------------------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `000123456789` | `pm_usBankAccount_success`             | `110000000`    | The payment succeeds.                                                                                                                                 |
| `000111111113` | `pm_usBankAccount_accountClosed`       | `110000000`    | The payment fails because the account is closed.                                                                                                      |
| `000000004954` | `pm_usBankAccount_riskLevelHighest`    | `110000000`    | The payment is blocked by Radar due to a [high risk of fraud](https://docs.stripe.com/radar/risk-evaluation.md#high-risk).                            |
| `000111111116` | `pm_usBankAccount_noAccount`           | `110000000`    | The payment fails because no account is found.                                                                                                        |
| `000222222227` | `pm_usBankAccount_insufficientFunds`   | `110000000`    | The payment fails due to insufficient funds.                                                                                                          |
| `000333333335` | `pm_usBankAccount_debitNotAuthorized`  | `110000000`    | The payment fails because debits aren’t authorized.                                                                                                   |
| `000444444440` | `pm_usBankAccount_invalidCurrency`     | `110000000`    | The payment fails due to invalid currency.                                                                                                            |
| `000666666661` | `pm_usBankAccount_failMicrodeposits`   | `110000000`    | The payment fails to send microdeposits.                                                                                                              |
| `000555555559` | `pm_usBankAccount_dispute`             | `110000000`    | The payment triggers a dispute.                                                                                                                       |
| `000000000009` | `pm_usBankAccount_processing`          | `110000000`    | The payment stays in processing indefinitely. Useful for testing [PaymentIntent cancellation](https://docs.stripe.com/api/payment_intents/cancel.md). |
| `000777777771` | `pm_usBankAccount_weeklyLimitExceeded` | `110000000`    | The payment fails due to payment amount causing the account to exceed its weekly payment volume limit.                                                |
| `000888888885` |                                        | `110000000`    | The payment fails because of a deactivated [tokenized account number](https://docs.stripe.com/financial-connections/tokenized-account-numbers.md).    |

Before test transactions can complete, you need to verify all test accounts that automatically succeed or fail the payment. To do so, use the test microdeposit amounts or descriptor codes below.

### Test microdeposit amounts and descriptor codes

To mimic different scenarios, use these microdeposit amounts _or_ 0.01 descriptor code values.

| Microdeposit values | 0.01 descriptor code values | Scenario                                                         |
| ------------------- | --------------------------- | ---------------------------------------------------------------- |
| `32` and `45`       | SM11AA                      | Simulates verifying the account.                                 |
| `10` and `11`       | SM33CC                      | Simulates exceeding the number of allowed verification attempts. |
| `40` and `41`       | SM44DD                      | Simulates a microdeposit timeout.                                |

### Test settlement behavior

Test transactions settle instantly and are added to your available test balance. This behavior differs from livemode, where transactions can take [multiple days](https://docs.stripe.com/payments/ach-direct-debit/set-up-payment.md#timing) to settle in your available balance.

## Accepting future payments [Server-side]

When the SetupIntent succeeds, it will create a new _PaymentMethod_ (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) attached to a [Customer](https://docs.stripe.com/api/customers.md). These can be used to initiate future payments without having to prompt the customer for their bank account a second time.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const intent = await stripe.paymentIntents.create({
  payment_method_types: ['us_bank_account'],
  payment_method: setup_intent.payment_method,
  customer: setup_intent.customer,
  confirm: true,
  amount: 100,
  currency: 'usd',
});
```

## Optional: Instant only verification [Server-side]

By default, setting up a US bank account payment method allows your customers to use instant bank account verification or microdeposits. You can optionally require instant bank account verification only, using the [verification_method](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-payment_method_options-us_bank_account-verification_method) parameter when you create the SetupIntent.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.create({
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      verification_method: 'instant',
      financial_connections: {
        permissions: ['payment_method', 'balances'],
      },
    },
  },
});
```

This ensures that you don’t need to handle microdeposit verification. However, if instant verification fails, the SetupIntent’s status is `requires_payment_method`, indicating a failure to instantly verify a bank account for your customer.

## Optional: Microdeposit only verification [Server-side]

By default, setting up a US bank account payment method lets your customers use instant bank account verification or microdeposits. You can optionally require microdeposit verification using the [verification_method](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-payment_method_options-us_bank_account-verification_method) parameter when you create the SetupIntent.

> If using a custom payment form, you must build your own UI to collect bank account details. If you disable Stripe microdeposit emails, you must build your own UI for your customer to confirm the microdeposit code or amount.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.create({
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      verification_method: "microdeposits",
    },
  },
});
```

You must then collect your customer’s bank account with your own UI and call [STPPaymentHandler.confirmSetupIntent](<https://stripe.dev/stripe-ios/stripepayments/documentation/stripepayments/stppaymenthandler/confirmsetupintent(_:with:completion:)>) with those details to complete the SetupIntent.

#### Swift

```swift
// Use your own UI to collect your customer's input
let accountholderName = // …
let email = // …
let accountNumber = // …
let routingNumber = // …
let accountType = // …
let accountHolderType = // …

let usBankAccountParams = STPPaymentMethodUSBankAccountParams()
usBankAccountParams.accountNumber = accountNumber
usBankAccountParams.routingNumber = routingNumber
usBankAccountParams.accountType = accountType
usBankAccountParams.accountHolderType = accountHolderType

let billingDetails = STPPaymentMethodBillingDetails()
billingDetails.name = accountholderName
billingDetails.email = email

let paymentMethodParams = STPPaymentMethodParams(usBankAccount: usBankAccountParams,
                                                 billingDetails: billingDetails,
                                                 metadata: nil)

let setupIntentParams = STPSetupIntentConfirmParams(clientSecret: clientSecret)
setupIntentParams.paymentMethodParams = paymentMethodParams
setupIntentParams.returnURL = "https://your-app-domain.com/stripe-redirect"

STPPaymentHandler.shared().confirmSetupIntent(
    setupIntentParams, with: self
) { (status, intent, error) in
    // Handle the result
}
```

## Optional: Updating the default payment method [Server-side]

After the `SetupIntent` reaches the `succeeded` state, you can update your customer’s `default_payment_method`.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

if (event.type == "setup_intent.succeeded") {
  const setup_intent = event.data.object;
  const customer_id = setup_intent.customer;
  const payment_method_id = setup_intent.payment_method;

  const customer = await stripe.customers.update(customer_id, {
    invoice_settings: { default_payment_method: payment_method_id },
  });
}
```

# Android

> This is a Android for when payment-ui is mobile and platform is android. View the full page at https://docs.stripe.com/payments/ach-direct-debit/set-up-payment?payment-ui=mobile&platform=android.

You can use the [Setup Intents API](https://docs.stripe.com/payments/setup-intents.md) to collect payment method details in advance, with the final amount or payment date determined later. This is useful for:

- Saving payment methods to a wallet to streamline future purchases
- Collecting surcharges after fulfilling a service
- Starting a free trial for a _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis)

> ACH Direct Debit is a [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method, which means that funds aren’t immediately available after payment. A payment typically takes 4 business days to arrive in your account.

The [Stripe Android SDK](https://github.com/stripe/stripe-android) is open source and [fully documented](https://stripe.dev/stripe-android/).

To install the SDK, add `stripe-android` and `financial-connections` to the `dependencies` block of your [app/build.gradle](https://developer.android.com/studio/build/dependencies) file:

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

  // Financial Connections SDK
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

## Create or retrieve a customer [Recommended] [Server-side]

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

#### Accounts v2

Create a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-configuration-customer) object when your user creates an account with your business, or retrieve an existing `Account` associated with this user. Associating the ID of the `Account` object with your own internal representation of a customer enables you to retrieve and use the stored payment method details later. Include an email address on the `Account` to enable Financial Connections’ [return user optimization](https://docs.stripe.com/financial-connections/fundamentals.md#return-user-optimization).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const account = await stripe.v2.core.accounts.create({
  contact_email: "{{CUSTOMER_EMAIL}}",
});
```

#### Customers v1

Create a _Customer_ (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) object when your user creates an account with your business, or retrieve an existing `Customer` associated with this user. Associating the ID of the `Customer` object with your own internal representation of a customer enables you to retrieve and use the stored payment method details later. Include an email address on the `Customer` to enable Financial Connections’ [return user optimization](https://docs.stripe.com/financial-connections/fundamentals.md#return-user-optimization).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customer = await stripe.customers.create({
  email: "{{CUSTOMER_EMAIL}}",
});
```

## Create a SetupIntent [Server-side] [Client-side]

A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) is an object that represents your intent to set up a customer’s payment method for future payments. The `SetupIntent` tracks the steps of this set-up process.

### Server-side

Create a SetupIntent on your server with [payment_method_types](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-payment_method_types) set to us_bank_account and specify the Customer’s [id](https://docs.stripe.com/api/customers/object.md#customer_object-id).

For more information on Financial Connections fees, see [pricing details](https://stripe.com/financial-connections#pricing).

By default, collecting bank account payment information uses [Financial Connections](https://docs.stripe.com/financial-connections.md) to instantly verify your customer’s account, with a fallback option of manual account number entry and microdeposit verification. See the [Financial Connections docs](https://docs.stripe.com/financial-connections/ach-direct-debit-payments.md) to learn how to configure Financial Connections and access additional account data to optimize your ACH integration. For example, you can use Financial Connections to check an account’s balance before initiating the ACH payment.

> To expand access to additional data after a customer authenticates their account, they must re-link their account with expanded permissions.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.create({
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      financial_connections: {
        permissions: ['payment_method', 'balances'],
      },
    },
  },
});
```

### Client-side

Included in the returned SetupIntent is a _client secret_ (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)), which is used on the client side to securely complete the setup instead of passing the entire SetupIntent object. There are different approaches that you can use to pass the client secret to the client side.

#### Kotlin

```kotlin
import androidx.appcompat.app.AppCompatActivity

class CheckoutActivity : AppCompatActivity() {
    lateinit var setupIntentClientSecret: String

    fun startCheckout() {
        // Request a SetupIntent from your server and store its client secret
    }
}
```

## Collect payment method details [Client-side]

ACH Direct Debit requires a customer name and (optional) email for the payment to succeed. In your app, collect the required billing details from the customer:

- Their full name (first and last)
- Their email address

Use `CollectBankAccountConfiguration.USBankAccount` to create the parameters required to call `presentWithSetupIntent`.

Initialize a CollectBankAccountLauncher instance inside onCreate of your checkout Activity, passing a method to handle the result. Then proceed to call `presentWithSetupIntent` to collect bank account details, create a _PaymentMethod_ (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs), and attach that PaymentMethod to the SetupIntent.

#### Kotlin

```kotlin
import androidx.appcompat.app.AppCompatActivity

class CheckoutActivity : AppCompatActivity() {
    private lateinit var setupIntentClientSecret: String
    private lateinit var collectBankAccountLauncher: CollectBankAccountLauncher

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // Create collector
        collectBankAccountLauncher = CollectBankAccountLauncher.create(
            this
        ) { result: CollectBankAccountResult ->
            when (result) {
                is CollectBankAccountResult.Completed -> {
                    val intent = result.response.intent
                    if (intent.status === StripeIntent.Status.RequiresPaymentMethod) {
                        // Customer canceled the Financial Connections modal. Present them with other
                        // payment method type options.
                    } else if (intent.status === StripeIntent.Status.RequiresConfirmation) {
                        // We collected an account - possibly instantly verified, but possibly
                        // manually-entered. Display payment method details and mandate text
                        // to the customer and confirm the intent once they accept
                        // the mandate.
                    }
                }
                is CollectBankAccountResult.Cancelled -> {
                    // handle cancellation
                }
                is CollectBankAccountResult.Failed -> {
                    // handle error
                    print("Error: ${result.error}")
                }
            }
        }
    }

    fun startCheckout() {
        // ...

        // Build params
        val collectParams: CollectBankAccountConfiguration =
            CollectBankAccountConfiguration.USBankAccount(
                name,
                email
            )

        // Calling this method will trigger the Financial Connections modal to be displayed
        collectBankAccountLauncher.presentWithSetupIntent(
            publishableKey,
            setupIntentClientSecret,
            collectParams
        )
    }
}
```

This loads a modal UI that handles bank account details collection and verification. When it completes, the _PaymentMethod_ (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) automatically attaches to the SetupIntent.

## Optional: Access data on a Financial Connections bank account [Server-side]

You can only access Financial Connections data if you request additional [data permissions](https://docs.stripe.com/financial-connections/fundamentals.md#data-permissions) when you create your SetupIntent.

After your customer successfully completes the [Stripe Financial Connections authentication flow](https://docs.stripe.com/financial-connections/fundamentals.md#authentication-flow), the `us_bank_account` PaymentMethod returned includes a [financial_connections_account](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-us_bank_account-financial_connections_account) ID that points to a [Financial Connections Account](https://docs.stripe.com/api/financial_connections/accounts.md). Use this ID to access account data.

> Bank accounts that your customers link through manual entry and microdeposits don’t have a `financial_connections_account` ID on the Payment Method.

To determine the Financial Connections account ID, retrieve the SetupIntent and expand the `payment_method` attribute:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.retrieve("{{SETUPINTENT_ID}}", {
  expand: ["payment_method"],
});
```

```json
{
  "id": "{{SETUP_INTENT_ID}}",
  "object": "setup_intent",
  // ...
  "payment_method": {
    "id": "{{PAYMENT_METHOD_ID}}",
    // ...
    "type": "us_bank_account"
    "us_bank_account": {
      "account_holder_type": "individual",
      "account_type": "checking",
      "bank_name": "TEST BANK","financial_connections_account": "{{FINANCIAL_CONNECTIONS_ACCOUNT_ID}}",
      "fingerprint": "q9qchffggRjlX2tb",
      "last4": "6789",
      "routing_number": "110000000"
    }
  }
  // ...
}

```

If you have access to balances data, we recommend [checking balances](https://docs.stripe.com/financial-connections/balances.md#initiate-balance-refresh) before initiating payments with the collected Payment Method.

Learn more about using additional account data to optimize your ACH integration with [Financial Connections](https://docs.stripe.com/financial-connections/ach-direct-debit-payments.md#optimize).

## Collect mandate acknowledgement and submit [Client-side]

Before you can complete the SetupIntent and save the payment method details for the customer, you must obtain authorization for payment by displaying mandate terms for the customer to accept.

To be compliant with _Nacha_ (Nacha is the governing body that oversees the ACH network) rules, you must obtain authorization from your customer before you can initiate payment by displaying mandate terms for them to accept. For more information on mandates, see [Mandates](https://docs.stripe.com/payments/ach-direct-debit.md#mandates).

When the customer accepts the mandate terms, you must confirm the Setup. Use `confirm` to complete the payment when the customer submits the form.

#### Kotlin

```kotlin
class CheckoutActivity : AppCompatActivity() {
    // ...
    private lateinit var setupIntentClientSecret: String
    private val paymentLauncher: PaymentLauncher by lazy {
        val paymentConfiguration = PaymentConfiguration.getInstance(applicationContext)
        PaymentLauncher.Companion.create(
            this,
            paymentConfiguration.publishableKey,
            paymentConfiguration.stripeAccountId,
            ::onPaymentResult
        )
    }

    private fun startCheckout() {
        // ...

        val confirmParams = ConfirmSetupIntentParams.create(
            clientSecret = setupIntentClientSecret,
            paymentMethodType = PaymentMethod.Type.USBankAccount
        )
        paymentLauncher.confirm(confirmParams)
    }

    private fun onPaymentResult(paymentResult: PaymentResult) {
        when (paymentResult) {
            is PaymentResult.Completed -> {
                // show success UI
            }
            is PaymentResult.Canceled -> {
                // handle cancel flow
            }
            is PaymentResult.Failed -> {
                // handle failures
                // (for example, the customer might need to choose a new payment
                // method)
            }
        }
    }
}
```

> `confirm` might take several seconds to complete. During that time, disable resubmittals of your form and show a waiting indicator (for example, a spinner). If you receive an error, show it to the customer, re-enable the form, and hide the waiting indicator.

If successful, Stripe returns a SetupIntent object, with one of the following possible statuses:

| Status            | Description                                                                    | Next Steps                                                                                                                                                    |
| ----------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `succeeded`       | The bank account has been instantly verified or verification wasn’t necessary. | No action needed                                                                                                                                              |
| `requires_action` | Further action needed to complete bank account verification.                   | Step 6: [Verifying bank accounts with microdeposits](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md#android-verify-with-microdeposits) |

After successfully confirming the Setup, an email confirmation of the mandate and collected bank account details must be sent to your customer. Stripe handles these by default, but you can choose to [send custom notifications](https://docs.stripe.com/payments/ach-direct-debit.md#mandate-and-microdeposit-emails) if you prefer.

## Verify bank account with microdeposits [Client-side]

Not all customers can verify the bank account instantly. This step only applies if your customer has elected to opt out of the instant verification flow in the previous step.

In these cases, Stripe sends a `descriptor_code` microdeposit and might fall back to an `amount` microdeposit if any further issues arise with verifying the bank account. These deposits take 1-2 business days to appear on the customer’s online statement.

- **Descriptor code**. Stripe sends a single, 0.01 USD microdeposit to the customer’s bank account with a unique, 6-digit `descriptor_code` that starts with SM. Your customer uses this string to verify their bank account.
- **Amount**. Stripe sends two, non-unique microdeposits to the customer’s bank account, with a statement descriptor that reads `ACCTVERIFY`. Your customer uses the deposit amounts to verify their bank account.

The result of the `confirmSetupIntent` method call in the previous step is a SetupIntent in the `requires_action` state. The SetupIntent contains a [next_action](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-next_action-verify_with_microdeposits) field that contains some useful information for completing the verification.

If you supplied a [billing email](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-billing_details-email), Stripe notifies your customer through this email when the deposits are expected to arrive. The email includes a link to a Stripe-hosted verification page where they can confirm the amounts of the deposits and complete verification.

> Verification attempts have a limit of ten failures for descriptor-based microdeposits and three for amount-based ones. If you exceed this limit, we can no longer verify the bank account. In addition, microdeposit verifications have a timeout of 10 days. If you can’t verify microdeposits in that time, the PaymentIntent reverts to requiring new payment method details. Clear messaging about what these microdeposits are and how you use them can help your customers avoid verification issues.

### Optional: Send custom email notifications

You can also send [custom email notifications](https://docs.stripe.com/payments/ach-direct-debit.md#mandate-and-microdeposit-emails) to your customer. After you set up custom emails, you need to specify how the customer responds to the verification email. To do so, choose _one_ of the following:

- Use the Stripe-hosted verification page. To do this, use the `verify_with_microdeposits[hosted_verification_url]` URL in the [next_action](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-verify_with_microdeposits-hosted_verification_url) object to direct your customer to complete the verification process.

- If you prefer not to use the Stripe-hosted verification page, create a form in your app. Your customers then use this form to relay microdeposit amounts to you and verify the bank account using the Android SDK.
  - At minimum, set up the form to handle the `descriptor code` parameter, which is a 6-digit string for verification purposes.
  - Stripe also recommends that you set your form to handle the `amounts` parameter, as some banks your customers use might require it.

  Integrations only pass in the `descriptor_code` _or_ `amounts`. To determine which one your integration uses, check the value for `verify_with_microdeposits[microdeposit_type]` in the `next_action` object.

#### Kotlin

```kotlin
// Use if you are using a descriptor code, do not use if you are using amounts
fun verifySetupIntentWithMicrodeposits(
    clientSecret: String,
    descriptorCode: String,
    callback: ApiResultCallback<PaymentIntent>
)

// Use if you are using amounts, do not use if you are using descriptor code
fun verifySetupIntentWithMicrodeposits(
    clientSecret: String,
    firstAmount: Int,
    secondAmount: Int,
    callback: ApiResultCallback<PaymentIntent>
)
```

When the bank account is successfully verified, Stripe returns the SetupIntent object with a `status` of `succeeded`.

Verification can fail for several reasons. The failure happens synchronously as a direct error response.

```json
{
  "error": {
    "code": "payment_method_microdeposit_verification_amounts_mismatch",
    "message": "The amounts provided do not match the amounts that were sent to the bank account. You have {attempts_remaining} verification attempts remaining.",
    "type": "invalid_request_error"
  }
}
```

| Error Code                                                   | Message                                                                                                                                         | Status change                                                         |
| ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `payment_method_microdeposit_failed`                         | Microdeposits failed. Please check the account, institution and transit numbers provided.                                                       | `status` is `requires_payment_method`, and `last_setup_error` is set. |
| `payment_method_microdeposit_verification_amounts_mismatch`  | The amounts provided don’t match the amounts that were sent to the bank account. You have {attempts_remaining} verification attempts remaining. | Unchanged                                                             |
| `payment_method_microdeposit_verification_attempts_exceeded` | Exceeded number of allowed verification attempts                                                                                                | `status` is `requires_payment_method`, and `last_setup_error` is set. |

## Test your integration

Learn how to test scenarios with instant verifications using [Financial Connections](https://docs.stripe.com/financial-connections/testing.md#web-how-to-use-test-accounts).

### Send transaction emails in a sandbox

After you collect the bank account details and accept a mandate, send the mandate confirmation and microdeposit verification emails in a _sandbox_ (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes).

If your domain is **{domain}** and your username is **{username}**, use the following email format to send test transaction emails: **{username}+test_email@{domain}**.

For example, if your domain is **example.com** and your username is **info**, use the format **info+test\_email@example.com** for testing ACH Direct Debit payments. This format ensures that emails route correctly. If you don’t include the **+test_email** suffix, we won’t send the email.

> You must [set up your Stripe account](https://docs.stripe.com/get-started/account/set-up.md) before you can trigger these emails while testing.

### Test account numbers

Stripe provides several test account numbers and corresponding tokens you can use to make sure your integration for manually-entered bank accounts is ready for production.

| Account number | Token                                  | Routing number | Behavior                                                                                                                                              |
| -------------- | -------------------------------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `000123456789` | `pm_usBankAccount_success`             | `110000000`    | The payment succeeds.                                                                                                                                 |
| `000111111113` | `pm_usBankAccount_accountClosed`       | `110000000`    | The payment fails because the account is closed.                                                                                                      |
| `000000004954` | `pm_usBankAccount_riskLevelHighest`    | `110000000`    | The payment is blocked by Radar due to a [high risk of fraud](https://docs.stripe.com/radar/risk-evaluation.md#high-risk).                            |
| `000111111116` | `pm_usBankAccount_noAccount`           | `110000000`    | The payment fails because no account is found.                                                                                                        |
| `000222222227` | `pm_usBankAccount_insufficientFunds`   | `110000000`    | The payment fails due to insufficient funds.                                                                                                          |
| `000333333335` | `pm_usBankAccount_debitNotAuthorized`  | `110000000`    | The payment fails because debits aren’t authorized.                                                                                                   |
| `000444444440` | `pm_usBankAccount_invalidCurrency`     | `110000000`    | The payment fails due to invalid currency.                                                                                                            |
| `000666666661` | `pm_usBankAccount_failMicrodeposits`   | `110000000`    | The payment fails to send microdeposits.                                                                                                              |
| `000555555559` | `pm_usBankAccount_dispute`             | `110000000`    | The payment triggers a dispute.                                                                                                                       |
| `000000000009` | `pm_usBankAccount_processing`          | `110000000`    | The payment stays in processing indefinitely. Useful for testing [PaymentIntent cancellation](https://docs.stripe.com/api/payment_intents/cancel.md). |
| `000777777771` | `pm_usBankAccount_weeklyLimitExceeded` | `110000000`    | The payment fails due to payment amount causing the account to exceed its weekly payment volume limit.                                                |
| `000888888885` |                                        | `110000000`    | The payment fails because of a deactivated [tokenized account number](https://docs.stripe.com/financial-connections/tokenized-account-numbers.md).    |

Before test transactions can complete, you need to verify all test accounts that automatically succeed or fail the payment. To do so, use the test microdeposit amounts or descriptor codes below.

### Test microdeposit amounts and descriptor codes

To mimic different scenarios, use these microdeposit amounts _or_ 0.01 descriptor code values.

| Microdeposit values | 0.01 descriptor code values | Scenario                                                         |
| ------------------- | --------------------------- | ---------------------------------------------------------------- |
| `32` and `45`       | SM11AA                      | Simulates verifying the account.                                 |
| `10` and `11`       | SM33CC                      | Simulates exceeding the number of allowed verification attempts. |
| `40` and `41`       | SM44DD                      | Simulates a microdeposit timeout.                                |

### Test settlement behavior

Test transactions settle instantly and are added to your available test balance. This behavior differs from livemode, where transactions can take [multiple days](https://docs.stripe.com/payments/ach-direct-debit/set-up-payment.md#timing) to settle in your available balance.

## Accepting future payments [Server-side]

When the SetupIntent succeeds, it will create a new _PaymentMethod_ (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) attached to a [Customer](https://docs.stripe.com/api/customers.md). These can be used to initiate future payments without having to prompt the customer for their bank account a second time.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const intent = await stripe.paymentIntents.create({
  payment_method_types: ['us_bank_account'],
  payment_method: setup_intent.payment_method,
  customer: setup_intent.customer,
  confirm: true,
  amount: 100,
  currency: 'usd',
});
```

## Optional: Instant only verification [Server-side]

By default, setting up a US bank account payment method allows your customers to use instant bank account verification or microdeposits. You can optionally require instant bank account verification only, using the [verification_method](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-payment_method_options-us_bank_account-verification_method) parameter when you create the SetupIntent.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.create({
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      verification_method: 'instant',
      financial_connections: {
        permissions: ['payment_method', 'balances'],
      },
    },
  },
});
```

This ensures that you don’t need to handle microdeposit verification. However, if instant verification fails, the SetupIntent’s status is `requires_payment_method`, indicating a failure to instantly verify a bank account for your customer.

## Optional: Microdeposit only verification [Server-side]

By default, setting up a US bank account payment method lets your customers use instant bank account verification or microdeposits. You can optionally require microdeposit verification using the [verification_method](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-payment_method_options-us_bank_account-verification_method) parameter when you create the SetupIntent.

> If using a custom payment form, you must build your own UI to collect bank account details. If you disable Stripe microdeposit emails, you must build your own UI for your customer to confirm the microdeposit code or amount.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.create({
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      verification_method: "microdeposits",
    },
  },
});
```

You must then collect your customer’s bank account with your own UI and call [PaymentLauncher.confirm](https://stripe.dev/stripe-android/payments-core/com.stripe.android.payments.paymentlauncher/-payment-launcher/confirm.html) with those details to complete the SetupIntent.

#### Kotlin

```kotlin
class CheckoutActivity : AppCompatActivity() {

    private lateinit var setupIntentClientSecret: String
    private val paymentLauncher: PaymentLauncher = // …

    private fun confirmSetupIntent() {
        // Use your own UI to collect your customer's input
        val accountholderName: String = // …
        val email: String = // …
        val accountNumber: String = // …
        val routingNumber: String = // …
        val accountType: PaymentMethod.USBankAccount.USBankAccountType = // …
        val accountHolderType: PaymentMethod.USBankAccount.USBankAccountHolderType = // …

        val createParams = PaymentMethodCreateParams.create(
            usBankAccount = PaymentMethodCreateParams.USBankAccount(
                accountNumber = accountNumber,
                routingNumber = routingNumber,
                accountType = accountType,
                accountHolderType = accountHolderType,
            ),
            billingDetails = PaymentMethod.BillingDetails(
                name = accountholderName,
                email = email,
            ),
        )

        val confirmParams = ConfirmSetupIntentParams.create(
            paymentMethodCreateParams = createParams,
            clientSecret = setupIntentClientSecret,
        )

        paymentLauncher.confirm(confirmParams)
    }
}
```

## Optional: Updating the default payment method [Server-side]

After the `SetupIntent` reaches the `succeeded` state, you can update your customer’s `default_payment_method`.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

if (event.type == "setup_intent.succeeded") {
  const setup_intent = event.data.object;
  const customer_id = setup_intent.customer;
  const payment_method_id = setup_intent.payment_method;

  const customer = await stripe.customers.update(customer_id, {
    invoice_settings: { default_payment_method: payment_method_id },
  });
}
```

# React Native

> This is a React Native for when payment-ui is mobile and platform is react-native. View the full page at https://docs.stripe.com/payments/ach-direct-debit/set-up-payment?payment-ui=mobile&platform=react-native.

You can use the [Setup Intents API](https://docs.stripe.com/payments/setup-intents.md) to collect payment method details in advance, with the final amount or payment date determined later. This is useful for:

- Saving payment methods to a wallet to streamline future purchases
- Collecting surcharges after fulfilling a service
- Starting a free trial for a _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis)

> ACH Direct Debit is a [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method, which means that funds aren’t immediately available after payment. A payment typically takes 4 business days to arrive in your account.

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

## Create or retrieve a customer [Recommended] [Server-side]

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

#### Accounts v2

Create a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-configuration-customer) object when your user creates an account with your business, or retrieve an existing `Account` associated with this user. Associating the ID of the `Account` object with your own internal representation of a customer enables you to retrieve and use the stored payment method details later. Include an email address on the `Account` to enable Financial Connections’ [return user optimization](https://docs.stripe.com/financial-connections/fundamentals.md#return-user-optimization).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const account = await stripe.v2.core.accounts.create({
  contact_email: "{{CUSTOMER_EMAIL}}",
});
```

#### Customers v1

Create a _Customer_ (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) object when your user creates an account with your business, or retrieve an existing `Customer` associated with this user. Associating the ID of the `Customer` object with your own internal representation of a customer enables you to retrieve and use the stored payment method details later. Include an email address on the `Customer` to enable Financial Connections’ [return user optimization](https://docs.stripe.com/financial-connections/fundamentals.md#return-user-optimization).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customer = await stripe.customers.create({
  email: "{{CUSTOMER_EMAIL}}",
});
```

## Create a SetupIntent [Server-side]

A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) is an object that represents your intent to set up a customer’s payment method for future payments. The `SetupIntent` tracks the steps of this set-up process.

Create a SetupIntent on your server with [payment_method_types](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-payment_method_types) set to `us_bank_account` and specify the Customer’s [id](https://docs.stripe.com/api/customers/object.md#customer_object-id).

### Server-side

Create a SetupIntent on your server with [payment_method_types](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-payment_method_types) set to `us_bank_account` and specify the Customer’s [id](https://docs.stripe.com/api/customers/object.md#customer_object-id).

For more information on Financial Connections fees, see [pricing details](https://stripe.com/financial-connections#pricing).

By default, collecting bank account payment information uses [Financial Connections](https://docs.stripe.com/financial-connections.md) to instantly verify your customer’s account, with a fallback option of manual account number entry and microdeposit verification. See the [Financial Connections docs](https://docs.stripe.com/financial-connections/ach-direct-debit-payments.md) to learn how to configure Financial Connections and access additional account data to optimize your ACH integration. For example, you can use Financial Connections to check an account’s balance before initiating the ACH payment.

> To expand access to additional data after a customer authenticates their account, they must re-link their account with expanded permissions.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.create({
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      financial_connections: {
        permissions: ['payment_method', 'balances'],
      },
    },
  },
});
```

### Client-side

A SetupIntent includes a _client secret_ (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)). You can use the client secret in your React Native app to securely complete the payment process instead of passing back the entire SetupIntent object. In your app, request a SetupIntent from your server and store its client secret.

```javascript
function PaymentScreen() {
  // ...

  const fetchIntentClientSecret = async () => {
    const response = await fetch(`${API_URL}/create-intent`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        // This is an example request body, the parameters you pass are up to you
        customer: "<CUSTOMER_ID>",
      }),
    });
    const { clientSecret } = await response.json();

    return clientSecret;
  };

  return <View>...</View>;
}
```

## Collect payment method details [Client-side]

Rather than sending the entire SetupIntent object to the client, use its _client secret_ (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)) from the previous step. This is different from your API keys that authenticate Stripe API requests.

Handle the client secret carefully because it can complete the charge. Don’t log it, embed it in URLs, or expose it to anyone but the customer

Use [collectBankAccountForSetup](https://docs.stripe.com/js/setup_intents/collect_bank_account_for_setup) to collect bank account details, create a _PaymentMethod_ (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs), and attach that PaymentMethod to the SetupIntent. You must include the account holder’s name in the `billingDetails` parameter to create an ACH Direct Debit PaymentMethod.

```javascript
import { collectBankAccountForSetup } from "@stripe/stripe-react-native";

export default function MyPaymentScreen() {
  const [name, setName] = useState("");

  const handleCollectBankAccountPress = async () => {
    // Fetch the intent client secret from the backend.
    // See `fetchIntentClientSecret()`'s implementation above.
    const { clientSecret } = await fetchIntentClientSecret();

    const { setupIntent, error } = await collectBankAccountForSetup(
      clientSecret,
      {
        paymentMethodType: "USBankAccount",
        paymentMethodData: {
          billingDetails: {
            name: "John Doe",
          },
        },
      },
    );

    if (error) {
      Alert.alert(`Error code: ${error.code}`, error.message);
    } else if (setupIntent) {
      Alert.alert("Setup status:", setupIntent.status);
      if (setupIntent.status === SetupIntents.Status.RequiresConfirmation) {
        // The next step is to call `confirmSetup`
      } else if (setupIntent.status === SetupIntents.Status.RequiresAction) {
        // The next step is to call `verifyMicrodepositsForSetup`
      }
    }
  };

  return (
    <PaymentScreen>
      <TextInput
        placeholder="Name"
        onChange={(value) => setName(value.nativeEvent.text)}
      />
      <Button
        onPress={handleCollectBankAccountPress}
        title="Collect bank account"
      />
    </PaymentScreen>
  );
}
```

This loads a modal UI that handles bank account details collection and verification. When it completes, the _PaymentMethod_ (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) is automatically attached to the SetupIntent.

## Set up a return URL (iOS only) [Client-side]

When a customer exits your app (for example to authenticate in Safari or their banking app), provide a way for them to automatically return to your app. Many payment method types _require_ a return URL. If you don’t provide one, we can’t present payment methods that require a return URL to your users, even if you’ve enabled them.

To provide a return URL:

1. [Register](https://developer.apple.com/documentation/xcode/defining-a-custom-url-scheme-for-your-app#Register-your-URL-scheme) a custom URL. Universal links aren’t supported.
1. [Configure](https://reactnative.dev/docs/linking) your custom URL.
1. Set up your root component to forward the URL to the Stripe SDK as shown below.

> If you’re using Expo, [set your scheme](https://docs.expo.io/guides/linking/#in-a-standalone-app) in the `app.json` file.

```jsx
import { useEffect, useCallback } from 'react';
import { Linking } from 'react-native';
import { useStripe } from '@stripe/stripe-react-native';

export default function MyApp() {
  const { handleURLCallback } = useStripe();

  const handleDeepLink = useCallback(
    async (url: string | null) => {
      if (url) {
        const stripeHandled = await handleURLCallback(url);
        if (stripeHandled) {
          // This was a Stripe URL - you can return or add extra handling here as you see fit
        } else {
          // This was NOT a Stripe URL – handle as you normally would
        }
      }
    },
    [handleURLCallback]
  );

  useEffect(() => {
    const getUrlAsync = async () => {
      const initialUrl = await Linking.getInitialURL();
      handleDeepLink(initialUrl);
    };

    getUrlAsync();

    const deepLinkListener = Linking.addEventListener(
      'url',
      (event: { url: string }) => {
        handleDeepLink(event.url);
      }
    );

    return () => deepLinkListener.remove();
  }, [handleDeepLink]);

  return (
    <View>
      <AwesomeAppComponent />
    </View>
  );
}
```

For more information on native URL schemes, refer to the [Android](https://developer.android.com/training/app-links/deep-linking) and [iOS](https://developer.apple.com/documentation/xcode/allowing_apps_and_websites_to_link_to_your_content/defining_a_custom_url_scheme_for_your_app) docs.

## Optional: Access data on a Financial Connections bank account [Server-side]

You can only access Financial Connections data if you request additional [data permissions](https://docs.stripe.com/financial-connections/fundamentals.md#data-permissions) when you create your SetupIntent.

After your customer successfully completes the [Stripe Financial Connections authentication flow](https://docs.stripe.com/financial-connections/fundamentals.md#authentication-flow), the `us_bank_account` PaymentMethod returned includes a [financial_connections_account](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-us_bank_account-financial_connections_account) ID that points to a [Financial Connections Account](https://docs.stripe.com/api/financial_connections/accounts.md). Use this ID to access account data.

> Bank accounts that your customers link through manual entry and microdeposits don’t have a `financial_connections_account` ID on the Payment Method.

To determine the Financial Connections account ID, retrieve the SetupIntent and expand the `payment_method` attribute:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.retrieve("{{SETUPINTENT_ID}}", {
  expand: ["payment_method"],
});
```

```json
{
  "id": "{{SETUP_INTENT_ID}}",
  "object": "setup_intent",
  // ...
  "payment_method": {
    "id": "{{PAYMENT_METHOD_ID}}",
    // ...
    "type": "us_bank_account"
    "us_bank_account": {
      "account_holder_type": "individual",
      "account_type": "checking",
      "bank_name": "TEST BANK","financial_connections_account": "{{FINANCIAL_CONNECTIONS_ACCOUNT_ID}}",
      "fingerprint": "q9qchffggRjlX2tb",
      "last4": "6789",
      "routing_number": "110000000"
    }
  }
  // ...
}

```

If you have access to balances data, we recommend [checking balances](https://docs.stripe.com/financial-connections/balances.md#initiate-balance-refresh) before initiating payments with the collected Payment Method.

Learn more about using additional account data to optimize your ACH integration with [Financial Connections](https://docs.stripe.com/financial-connections/ach-direct-debit-payments.md#optimize).

## Collect mandate acknowledgement and submit [Client-side]

Before you can complete the SetupIntent and save the payment method details for the customer, you must obtain authorization for payment by displaying mandate terms for the customer to accept.

To comply with Nacha rules, you must obtain authorization from your customer before you can initiate payment by displaying mandate terms for them to accept. For more information on mandates, see [Mandates](https://docs.stripe.com/payments/ach-direct-debit.md#mandates).

When the customer accepts the mandate terms, you must confirm the SetupIntent. Use `confirmSetup` to confirm the intent.

```javascript
import { confirmSetup } from "@stripe/stripe-react-native";

export default function MyPaymentScreen() {
  const [name, setName] = useState("");

  const handleCollectBankAccountPress = async () => {
    // See above
  };

  const handlePayPress = async () => {
    // use the same clientSecret as earlier, see above
    const { error, setupIntent } = await confirmSetup(clientSecret, {
      type: "USBankAccount",
    });

    if (error) {
      Alert.alert(`Error code: ${error.code}`, error.message);
    } else if (setupIntent) {
      if (setupIntent.status === SetupIntents.Status.Processing) {
        // The debit has been successfully submitted and is now processing
      } else if (
        setupIntent.status === SetupIntents.Status.RequiresAction &&
        setupIntent?.nextAction?.type === "verifyWithMicrodeposits"
      ) {
        // The payment must be verified with `verifyMicrodepositsForPayment`
      } else {
        Alert.alert("Payment status:", setupIntent.status);
      }
    }
  };

  return (
    <PaymentScreen>
      <TextInput
        placeholder="Name"
        onChange={(value) => setName(value.nativeEvent.text)}
      />
      <Button
        onPress={handleCollectBankAccountPress}
        title="Collect bank account"
      />
      <Button onPress={handlePayPress} title="Pay" />
    </PaymentScreen>
  );
}
```

If successful, Stripe returns a SetupIntent object, with one of the following possible statuses:

| Status           | Description                                                                    | Next Steps                                                                                                                                                |
| ---------------- | ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Succeeded`      | The bank account has been instantly verified or verification wasn’t necessary. | No action needed                                                                                                                                          |
| `RequiresAction` | Bank account verification requires further action.                             | Step 6: [Verifying bank accounts with microdeposits](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md#web-verify-with-microdeposits) |

After successfully confirming the SetupIntent, an email confirmation of the mandate and collected bank account details must be sent to your customer. Stripe handles these by default, but you can choose to [send custom notifications](https://docs.stripe.com/payments/ach-direct-debit.md#mandate-and-microdeposit-emails) if you prefer.

## Verify bank account with microdeposits [Client-side]

Not all customers can verify their bank account instantly. In these cases, Stripe sends a microdeposit to the bank account. This deposit might take up to 1-2 business days to appear on the customer’s online statement. This deposit takes one of two shapes:

- **Descriptor code**. Stripe sends a single, 0.01 USD microdeposit to the customer’s bank account with a unique, 6-digit `descriptorCode` that starts with SM. Your customer uses this string to verify their bank account.
- **Amount**. Stripe sends two, non-unique microdeposits to the customer’s bank account, with a statement descriptor that reads `ACCTVERIFY`. Your customer uses the deposit amounts to verify their bank account.

If the result of the `confirmSetup` method call in the previous step is a SetupIntent with a `requiresAction` status, the SetupIntent contains a `next_action` field that contains some useful information for completing the verification.

```javascript
nextAction: {
  type: 'verifyWithMicrodeposits';
  redirectUrl: "https://payments.stripe.com/…",
  microdepositType: "descriptor_code";
  arrivalDate: "1647586800";
}
```

If you supplied a [billing email](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-billing_details-email), Stripe uses this email to notify your customer when we expect the deposits to arrive. The email includes a link to a Stripe-hosted verification page where they can confirm the amounts of the deposits and complete verification.

> Verification attempts have a limit of ten failures for descriptor-based microdeposits and three for amount-based ones. If you exceed this limit, we can no longer verify the bank account. In addition, microdeposit verifications have a timeout of 10 days. If you can’t verify microdeposits in that time, the PaymentIntent reverts to requiring new payment method details. Clear messaging about what these microdeposits are and how you use them can help your customers avoid verification issues.

When you know the payment is in the `requiresAction` state and the `nextAction` is of type `verifyWithMicrodeposits`, you can complete verification of a bank account in two ways:

1. Verify the deposits directly in your app by calling `verifyMicrodepositsForSetup` after collecting either the descriptor code or amounts.

```javascript
import { verifyMicrodepositsForSetup } from '@stripe/stripe-react-native';

export default function MyPaymentScreen() {
  const [verificationText, setVerificationText] = useState('');

  return (
    <TextInput
      placeholder="Descriptor code or comma-separated amounts"
      onChange={(value) => setVerificationText(value.nativeEvent.text)} // Validate and store your user's verification input
    />
    <Button
      title="Verify microdeposit"
      onPress={async () => {
        const { paymentIntent, error } =
          await verifyMicrodepositsForSetup(secret, {
            // Provide either the descriptorCode OR amounts, not both
            descriptorCode: verificationText,
            amounts: verificationText,
          });

        if (error) {
          Alert.alert(`Error code: ${error.code}`, error.message);
        } else if (paymentIntent) {
          Alert.alert('Payment status:', paymentIntent.status);
        }
      }}
    />
  );
}
```

1. Use the Stripe-hosted verification page that we automatically provide for you. To do this, use the `nextAction[redirectUrl]` URL in the `nextAction` object (see above) to direct your customer to complete the verification process.

```javascript
const { error, setupIntent } = await confirmSetup(clientSecret, {
  type: "USBankAccount",
});

if (error) {
  Alert.alert(`Error code: ${error.code}`, error.message);
} else if (setupIntent) {
  if (
    setupIntent.status === SetupIntents.Status.RequiresAction &&
    setupIntent?.nextAction?.type === "verifyWithMicrodeposits"
  ) {
    // Open the Stripe-hosted verification page
    Linking.openURL(setupIntent.nextAction.redirectUrl);
  } else {
    Alert.alert("Payment status:", setupIntent.status);
  }
}
```

When the bank account is successfully verified, Stripe returns the SetupIntent object with a `status` of `Succeeded`, and sends a [setup_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.succeeded) _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event.

Verification can fail for several reasons. The failure might happen synchronously as a direct error response, or asynchronously through a [setup_intent.setup_failed](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.setup_failed) webhook event (shown in the following examples).

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
      "message": "You have exceeded the number of allowed verification attempts.",
    },
    ...
    "status": "requires_payment_method"
  }
}
```

| Error Code                                                   | Synchronous or Asynchronous                            | Message                                                                                                                                       | Status change                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `payment_method_microdeposit_failed`                         | Synchronously, or asynchronously through webhook event | Microdeposits failed. Please check the account, institution and transit numbers provided                                                      | `status` is `requires_payment_method`, and `last_setup_error` is set. |
| `payment_method_microdeposit_verification_amounts_mismatch`  | Synchronously                                          | The amounts provided don’t match the amounts that we sent to the bank account. You have {attempts_remaining} verification attempts remaining. | Unchanged                                                             |
| `payment_method_microdeposit_verification_attempts_exceeded` | Synchronously, or asynchronously through webhook event | Exceeded the number of allowed verification attempts                                                                                          | `status` is `requires_payment_method`, and `last_setup_error` is set. |
| `payment_method_microdeposit_verification_timeout`           | Asynchronously through a webhook event                 | Microdeposit timeout. The customer hasn’t verified their bank account within the required 10 day period.                                      | `status` is `requires_payment_method`, and `last_setup_error` is set. |

## Test your integration

Learn how to test scenarios with instant verifications using [Financial Connections](https://docs.stripe.com/financial-connections/testing.md#web-how-to-use-test-accounts).

### Send transaction emails in a sandbox

After you collect the bank account details and accept a mandate, send the mandate confirmation and microdeposit verification emails in a _sandbox_ (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes).

If your domain is **{domain}** and your username is **{username}**, use the following email format to send test transaction emails: **{username}+test_email@{domain}**.

For example, if your domain is **example.com** and your username is **info**, use the format **info+test\_email@example.com** for testing ACH Direct Debit payments. This format ensures that emails route correctly. If you don’t include the **+test_email** suffix, we won’t send the email.

> You must [set up your Stripe account](https://docs.stripe.com/get-started/account/set-up.md) before you can trigger these emails while testing.

### Test account numbers

Stripe provides several test account numbers and corresponding tokens you can use to make sure your integration for manually-entered bank accounts is ready for production.

| Account number | Token                                  | Routing number | Behavior                                                                                                                                              |
| -------------- | -------------------------------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `000123456789` | `pm_usBankAccount_success`             | `110000000`    | The payment succeeds.                                                                                                                                 |
| `000111111113` | `pm_usBankAccount_accountClosed`       | `110000000`    | The payment fails because the account is closed.                                                                                                      |
| `000000004954` | `pm_usBankAccount_riskLevelHighest`    | `110000000`    | The payment is blocked by Radar due to a [high risk of fraud](https://docs.stripe.com/radar/risk-evaluation.md#high-risk).                            |
| `000111111116` | `pm_usBankAccount_noAccount`           | `110000000`    | The payment fails because no account is found.                                                                                                        |
| `000222222227` | `pm_usBankAccount_insufficientFunds`   | `110000000`    | The payment fails due to insufficient funds.                                                                                                          |
| `000333333335` | `pm_usBankAccount_debitNotAuthorized`  | `110000000`    | The payment fails because debits aren’t authorized.                                                                                                   |
| `000444444440` | `pm_usBankAccount_invalidCurrency`     | `110000000`    | The payment fails due to invalid currency.                                                                                                            |
| `000666666661` | `pm_usBankAccount_failMicrodeposits`   | `110000000`    | The payment fails to send microdeposits.                                                                                                              |
| `000555555559` | `pm_usBankAccount_dispute`             | `110000000`    | The payment triggers a dispute.                                                                                                                       |
| `000000000009` | `pm_usBankAccount_processing`          | `110000000`    | The payment stays in processing indefinitely. Useful for testing [PaymentIntent cancellation](https://docs.stripe.com/api/payment_intents/cancel.md). |
| `000777777771` | `pm_usBankAccount_weeklyLimitExceeded` | `110000000`    | The payment fails due to payment amount causing the account to exceed its weekly payment volume limit.                                                |
| `000888888885` |                                        | `110000000`    | The payment fails because of a deactivated [tokenized account number](https://docs.stripe.com/financial-connections/tokenized-account-numbers.md).    |

Before test transactions can complete, you need to verify all test accounts that automatically succeed or fail the payment. To do so, use the test microdeposit amounts or descriptor codes below.

### Test microdeposit amounts and descriptor codes

To mimic different scenarios, use these microdeposit amounts _or_ 0.01 descriptor code values.

| Microdeposit values | 0.01 descriptor code values | Scenario                                                         |
| ------------------- | --------------------------- | ---------------------------------------------------------------- |
| `32` and `45`       | SM11AA                      | Simulates verifying the account.                                 |
| `10` and `11`       | SM33CC                      | Simulates exceeding the number of allowed verification attempts. |
| `40` and `41`       | SM44DD                      | Simulates a microdeposit timeout.                                |

### Test settlement behavior

Test transactions settle instantly and are added to your available test balance. This behavior differs from livemode, where transactions can take [multiple days](https://docs.stripe.com/payments/ach-direct-debit/set-up-payment.md#timing) to settle in your available balance.

## Accepting future payments [Server-side]

When the SetupIntent succeeds, it creates a new _PaymentMethod_ (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) attached to a [Customer](https://docs.stripe.com/api/customers.md). You can use these to initiate future payments without having to prompt the customer for their bank account a second time.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const intent = await stripe.paymentIntents.create({
  payment_method_types: ['us_bank_account'],
  payment_method: setup_intent.payment_method,
  customer: setup_intent.customer,
  confirm: true,
  amount: 100,
  currency: 'usd',
});
```

## Optional: Instant only verification [Server-side]

By default, setting up a US bank account payment method allows your customers to use instant bank account verification or microdeposits. You can optionally require instant bank account verification only, using the [verification_method](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-payment_method_options-us_bank_account-verification_method) parameter when you create the SetupIntent.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.create({
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      verification_method: 'instant',
      financial_connections: {
        permissions: ['payment_method', 'balances'],
      },
    },
  },
});
```

This ensures that you don’t need to handle microdeposit verification. However, if instant verification fails, the SetupIntent’s status is `requires_payment_method`, indicating a failure to instantly verify a bank account for your customer.

## Optional: Microdeposit only verification [Server-side]

By default, setting up a US bank account payment method lets your customers use instant bank account verification or microdeposits. You can optionally require microdeposit verification using the [verification_method](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-payment_method_options-us_bank_account-verification_method) parameter when you create the SetupIntent.

> If using a custom payment form, you must build your own UI to collect bank account details. If you disable Stripe microdeposit emails, you must build your own UI for your customer to confirm the microdeposit code or amount.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.create({
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      verification_method: "microdeposits",
    },
  },
});
```

You must then collect your customer’s bank account with your own UI and call [confirmSetupIntent](https://stripe.dev/stripe-react-native/api-reference/index.html#confirmSetupIntent) with those details to complete the SetupIntent.

```javascript
import {useConfirmSetupIntent} from '@stripe/stripe-react-native';

export default function MySetupScreen() {
  const { confirmSetupIntent, loading } = useConfirmSetupIntent();

  const [accountholderName, setAccountholderName] = useState('');
  const [email, setEmail] = useState('');
  const [accountNumber, setAccountNumber] = useState('');
  const [routingNumber, setRoutingNumber] = useState('');
  const [accountType, setAccountType] = useState(undefined);
  const [accountHolderType, setAccountHolderType] = useState(undefined);

  const handleConfirmPress = async () => {
    const billingDetails: BillingDetails = {
      name: accountholderName,
      email: email,
    };

    const { error, setupIntent } = await confirmSetupIntent(secret, {
      paymentMethodType: 'USBankAccount',
      paymentMethodDatapaymentMethodData: {
        billingDetails,
        accountNumber,
        routingNumber,
        accountType,
        accountHolderType,
      },
    });

    // Handle result or error…
  };

  return (
    <PaymentScreen>
      <TextInput
        placeholder="Accountholder Name"
        onChange={(value) => setAccountholderName(value.nativeEvent.text)}
      />

      // Other fields to capture required values…

      <Button
        onPress={handleCollectBankAccountPress}
        title="Collect bank account"
      />
      <Button onPress={handleConfirmPress} title="Confirm" />
    </PaymentScreen>
  );
}
```

## Optional: Updating the default payment method [Server-side]

After the `SetupIntent` reaches the `succeeded` state, you can update your customer’s `default_payment_method`.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

if (event.type == "setup_intent.succeeded") {
  const setup_intent = event.data.object;
  const customer_id = setup_intent.customer;
  const payment_method_id = setup_intent.payment_method;

  const customer = await stripe.customers.update(customer_id, {
    invoice_settings: { default_payment_method: payment_method_id },
  });
}
```
