<!-- Source URL: https://docs.stripe.com/payments/nz-bank-account/accept-a-payment -->
<!-- Fetched: 2026-05-03 -->

# Accept a New Zealand BECS Direct Debit payment

Build a custom payment form to accept payments with New Zealand bank account debits.

Accepting New Zealand BECS Direct Debit payments on your website consists of creating an object to track a payment, collecting payment method information and mandate acknowledgement, and submitting the payment to Stripe for processing.

Stripe uses a payment object, the [Payment Intent](https://docs.stripe.com/payments/payment-intents.md), to track and handle all the states of the payment until the payment completes.

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
  include: ['configuration.customer'],
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customer = await stripe.customers.create({
  name: 'Jenny Rosen',
  email: 'jenny.rosen@example.com',
});
```

## Create a PaymentIntent [Server-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) is an object that represents your intent to collect payment from a customer and tracks the lifecycle of the payment process through each stage.

First, create a `PaymentIntent` on your server and specify the amount to collect and the `nzd` currency. Add `nz_bank_account` to the [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) array, and specify the ID of the customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-id) or [Customer](https://docs.stripe.com/api/customers/object.md#customer_object-id).

If you want to save the generated *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) to the customer for future use, also set [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) to `off_session`.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ['nz_bank_account'],
  customer_account: '{{CUSTOMERACCOUNT_ID}}',
  amount: 1099,
  currency: 'nzd',
  setup_future_usage: 'off_session',
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ['nz_bank_account'],
  customer: '{{CUSTOMER_ID}}',
  amount: 1099,
  currency: 'nzd',
  setup_future_usage: 'off_session',
});
```

Included in the returned PaymentIntent is a [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret), which the client side uses to securely complete the payment process instead of passing the entire PaymentIntent object. You can use different approaches to pass the client secret to the client side.

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
  console.log("Running on port 3000");
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
  console.log("Running on port 3000");
});
```

## Collect payment method details and mandate acknowledgement [Client-side]

### Set up Stripe Elements

Include the Stripe.js script on your checkout page by adding it to the `head` of your HTML file. Always load Stripe.js directly from js.stripe.com. Don’t include the script in a bundle or host a copy of it yourself.

```html
<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/dahlia/stripe.js"></script>
</head>
```

Create an instance of the [Stripe object](https://docs.stripe.com/js.md#stripe-function) by providing your publishable [API key](https://docs.stripe.com/keys.md):

```javascript
// Set your publishable key: remember to change this to your live publishable key in production
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");
```

### Add the Payment Element to your checkout page

On your checkout page, create an empty DOM node with a unique ID for the [Payment Element](https://docs.stripe.com/payments/payment-element.md) to render into.

```html
<form id="payment-form">
  <h3>Payment</h3>
  <div id="payment-element"></div>

  <button id="submit">Submit</button>
</form>
```

When the form above finishes loading, create a new Elements group, passing the [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) from [the previous step](https://docs.stripe.com/payments/nz-bank-account/accept-a-payment.md#web-create-intent) as configuration. You can also pass in the [appearance option](https://docs.stripe.com/elements/appearance-api.md), customizing the Elements to match the design of your site.

Then, create an instance of the Payment Element and mount it to its corresponding DOM node:

```javascript
// Customize the appearance of Elements using the Appearance API.
const appearance = {
  /* ... */
};

// Create an elements group from the Stripe instance, passing the clientSecret (obtained in step 2) and appearance (optional).
const elements = stripe.elements({ clientSecret, appearance });

// Create Payment Element instance.
const paymentElement = elements.create('payment');

// Mount the Payment Element to its corresponding DOM node.
paymentElement.mount("#payment-element");
```

The Payment Element renders a dynamic form that allows your customer to pick a payment method type. The form automatically collects all necessary payments details for the payment method type that they select. For New Zealand BECS Diret Debit payments, that includes the customer’s name, email address, and bank account number.

### Mandate acknowledgement

The Payment Element also displays the New Zealand BECS Direct Debit Service Terms and Conditions to your customer and collects their agreement with those terms. You’re not required to do anything else.

If you don’t use the Payment Element, you must separately display these terms and conditions to your customer and confirm their acceptance.

> By providing your bank account details and confirming this payment, you authorise Stripe New Zealand Limited (authorisation code 3143978), to debit your account with the amounts of direct debits payable to Rocket Rides (“we”, “us” or “Merchant”) in accordance with this authority.
>
> You agree that this authority is subject to:
>
> - your bank’s terms and conditions that relate to your account, and

- the [Direct Debit Service Terms and Conditions](https://stripe.com/nz/legal/nzbecs-customer-dd-service-terms)
  > You certify that you’re either the sole account holder on the bank account listed above or that you’re an authorised signatory on, and have authority to operate, this bank account severally.
  >
  > We’ll send you an email confirmation no later than 5 business days after your confirmation of this Direct Debit Authority.

If we request you to do so, you must promptly provide Stripe with a record of the mandates.

## Optional: Customize the appearance [Client-side]

Now that you’ve added these Elements to your page, you can customize everything about their appearance to make them fit with the design of the rest of your page:
![](assets/stripe-elements-appearance-example.png)

[Read about the Appearance API](https://docs.stripe.com/elements/appearance-api.md)

## Submit the payment to Stripe [Client-side]

Use [stripe.confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment) to collect bank account details, create a *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs), and attach that PaymentMethod to the PaymentIntent.

For some other payment method types, your customer might be first redirected to an intermediate site, like a bank authorization page, before being redirected to the `return_url`. Provide a [return_url](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-return_url) to this function to indicate where Stripe should redirect the customer after they complete the payment.

Since New Zealand BECS Direct Debits don’t require a redirect, you can also set [redirect](https://docs.stripe.com/js/payment_intents/confirm_payment#confirm_payment_intent-options-redirect) to `if_required` in place of providing a `return_url`. A `return_url` will only be required if you add another redirect-based payment method later.

```javascript
confirmationForm.addEventListener('submit', (ev) => {
  ev.preventDefault();
  stripe
    .confirmPayment({ elements, redirect: 'if_required' })
    .then(({ paymentIntent, error }) => {
      if (error) {
        console.error(error.message);
        // The confirmation failed for some reason.
      } else if (paymentIntent.status === 'requires_payment_method') {
        // Confirmation failed. Attempt again with a different payment method.
      } else if (paymentIntent.status === 'processing') {
        // Confirmation succeeded! The account will be debited.
        // Display a message to the customer.
      }
    });
});
```

If successful, Stripe returns a PaymentIntent object with the status `processing`. See the next step for information on how to confirm success of the PaymentIntent.

### Customer notification emails

You must send an email confirmation of the mandate and collected bank account details to your customer after successfully confirming the PaymentIntent.

In addition, for every payment collected, including this one, you must send your customer an email notification of the debit date and amount at latest on the day the debit takes place.

Stripe handles sending these emails for you by default, but you can choose to [send custom notifications](https://docs.stripe.com/payments/nz-bank-account.md#mandate-confirmation-and-debit-notification-emails).

## Confirm the PaymentIntent succeeded [Server-side]

New Zealand BECS Direct Debit are a [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method. In addition, they require notifying your customer of any debit from their bank account, at latest, on the date of the debit.

Notification of success or failure of the PaymentIntent comes within 3 business days thereafter. When the payment succeeds, the PaymentIntent status changes from `processing` to `succeeded`.

The following events are sent when the PaymentIntent status changes:

| Event                           | Description                                                  | Next Step                                                                           |
| ------------------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------------- |
| `payment_intent.processing`     | The customer successfully submitted their payment to Stripe. | Wait for the initiated payment to succeed or fail.                                  |
| `payment_intent.succeeded`      | The customer’s payment succeeded.                            | Fulfill the goods or services that were purchased.                                  |
| `payment_intent.payment_failed` | The customer’s payment was declined.                         | Send the customer an email or push notification and request another payment method. |

We recommend using [webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks) to *confirm* (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) the charge succeeds and to notify the customer that the payment is complete. You can also view events on the [Stripe Dashboard](https://dashboard.stripe.com/events).

## Accepting future payments [Server-side]

If you set [setup_future_usage](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-setup_future_usage) to `off_session`, then after the `PaymentIntent` succeeds, the generated `PaymentMethod` is attached to the object that represents the customer. You can use it to initiate future payments without having to prompt the customer for their bank account.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ['nz_bank_account'],
  customer: '{{CUSTOMER_ID}}',
  payment_method: "{{PAYMENTMETHOD_ID}}",
  confirm: true,
  amount: 100,
  currency: 'nzd',
  off_session: true,
});
```

## Test your integration

### Test account numbers

In a *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes), you can use the following parameters to simulate specific errors.

#### Account numbers

Test your form using bank code `11`, branch code `0000`, and one of the following account number and suffix combinations.

| Account number | Suffix | Description                                                                                                                                                            |
| -------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `0000000`      | `010`  | The PaymentIntent status transitions from `processing` to `succeeded`. The mandate status remains `active`.                                                            |
| `2222222`      | `027`  | The PaymentIntent status transitions from `processing` to `requires_payment_method` with a `insufficient_funds` failure code. The mandate status remains `active`.     |
| `8888888`      | `000`  | The PaymentIntent status transitions from `processing` to `requires_payment_method` with a `refer_to_customer` failure code. The mandate status remains `active`.      |
| `1111111`      | `016`  | The PaymentIntent status transitions from `processing` to `requires_payment_method` with a `no_account` failure code. The mandate status becomes `inactive`.           |
| `5555555`      | `059`  | The PaymentIntent status transitions from `processing` to `requires_payment_method` with a `debit_not_authorized` failure code. The mandate status becomes `inactive`. |
| `9999999`      | `000`  | The PaymentIntent status transitions to `processing` and remains there. To transition it further, use an API request as described below.                               |

#### PaymentMethods

Pass these tokens in the `payment_method` parameter while creating or confirming a PaymentIntent.

| Payment Method                        | Description                                                                                                                                                            |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `pm_nzBankAccount_success`            | The PaymentIntent status transitions from `processing` to `succeeded`. The mandate status remains `active`.                                                            |
| `pm_nzBankAccount_insufficientFunds`  | The PaymentIntent status transitions from `processing` to `requires_payment_method` with a `insufficient_funds` failure code. The mandate status remains `active`.     |
| `pm_nzBankAccount_referToCustomer`    | The PaymentIntent status transitions from `processing` to `requires_payment_method` with a `refer_to_customer` failure code. The mandate status remains `active`.      |
| `pm_nzBankAccount_noAccount`          | The PaymentIntent status transitions from `processing` to `requires_payment_method` with an `no_account` failure code. The mandate status becomes `inactive`.          |
| `pm_nzBankAccount_debitNotAuthorized` | The PaymentIntent status transitions from `processing` to `requires_payment_method` with a `debit_not_authorized` failure code. The mandate status becomes `inactive`. |
| `pm_nzBankAccount_processing`         | The PaymentIntent status transitions to `processing` and remains there. To transition it further, use an API request as described below.                               |

## Optional: Configure customer debit date

You can control the date that Stripe debits a customer’s bank account using the [target date](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-payment_method_options-nz_bank_account-target_date). The target date must be at least three days in the future and no more than 15 days from the current date.

The target date schedules money to leave the customer’s account on the target date. You can [cancel a PaymentIntent](https://docs.stripe.com/api/payment_intents/cancel.md) created with a target date up to three business days before the configured date.

Target dates that meet one of the following criteria delay the debit until next available business day:

- Target date falls on a weekend, a bank holiday, or other non-business day.
- Target date is fewer than three business days in the future.

This parameter operates on a best-effort basis. Each customer’s bank might process debits on different dates, depending on local bank holidays or other reasons.
