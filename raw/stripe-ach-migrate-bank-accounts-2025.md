<!-- Source URL: https://docs.stripe.com/payments/ach-direct-debit/migrating-from-charges -->
<!-- Fetched: 2026-05-02 -->

# Migrate existing bank accounts

Learn how to migrate existing bank accounts to the Payment Intents API or Checkout Sessions API.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

Stripe is removing support for [ACH Direct Debit](https://docs.stripe.com/ach-deprecated.md) using [legacy integrations](https://docs.stripe.com/payments/ach-direct-debit/migrating-from-charges.md#identify-legacy-payments).

If you create legacy ACH Direct Debit payments, you must migrate to the [Payment Intents API](https://docs.stripe.com/api/payment_intents.md) or [Checkout Sessions API](https://docs.stripe.com/api/checkout/sessions.md).

If you previously collected customer payment details with Stripe using the [Tokens API](https://docs.stripe.com/ach-deprecated.md), you can continue using the saved `BankAccount` as a _PaymentMethod_ (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs).

You can only use customer [bank accounts](https://docs.stripe.com/api/customer_bank_accounts.md) with the [Payment Intents API](https://docs.stripe.com/api/payment_intents.md) or [Checkout Sessions API](https://docs.stripe.com/payments/quickstart-checkout-sessions.md) after you meet the following requirements:

- **Checkout Sessions API:** The customer’s bank account has been verified.

- **Payment Intents API:** The customer’s bank account has been verified, and an [active mandate](https://docs.stripe.com/payments/ach-direct-debit/migrating-from-charges.md#mandate-acknowledgement) exists for that bank account.

You don’t need to re-verify Bank Accounts that are already verified to use them with Payment Intents or Checkout Sessions.

# Checkout Sessions API

> This is a Checkout Sessions API for when integration-path is checkout. View the full page at https://docs.stripe.com/payments/ach-direct-debit/migrating-from-charges?integration-path=checkout.

## Use Checkout Sessions

To display previously saved and verified bank accounts in Checkout, you need to:

- Create a Checkout Session with a `customer` parameter
- Set the filters to `['unspecified', 'always']`
- Specify `us_bank_account` in `payment_method_types`

When these requirements are met, Checkout automatically finds and displays all saved, verified bank accounts associated with that customer, eliminating the need to recollect payment details.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({
  mode: 'payment',
  ui_mode: 'elements',
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['us_bank_account'],
  line_items: [
    {
      price_data: {
        currency: 'usd',
        product_data: {
          name: 'T-shirt',
        },
        unit_amount: 1099,
      },
      quantity: 1,
    },
  ],
  saved_payment_method_options: {
    allow_redisplay_filters: ['unspecified', 'always'],
  },
  return_url: 'YOUR_DOMAIN/complete?session_id={CHECKOUT_SESSION_ID}',
});
```

If the `customer` has an email attached, the customer’s email is prefilled in the [Session](https://docs.stripe.com/js/custom_checkout/session_object) and can’t be modified. You must check for an email and render your email input field accordingly.

#### React

```javascript
const { checkout } = useCheckoutElements();
const currentEmail = checkout.email;

if (currentEmail) {
  return <input value={currentEmail} readOnly />;
}
```

#### HTML/JavaScript

```javascript
const emailInput = document.getElementById('email');
const loadActionsResult = await checkout.loadActions();
const session = loadActionsResult.actions.getSession();
const currentEmail = session.email;

if (currentEmail) {
  emailInput.value = currentEmail;
  emailInput.readOnly = true;
  emailInput.classList.add('read-only');
}
```

# Payment Intents API

> This is a Payment Intents API for when integration-path is payment-intent. View the full page at https://docs.stripe.com/payments/ach-direct-debit/migrating-from-charges?integration-path=payment-intent.

## Collect mandate acknowledgement

Confirming a PaymentIntent or SetupIntent requires having your customer authorize a [mandate](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-mandate_data) to debit the account. Learn more about [SEC codes](https://docs.stripe.com/payments/ach-direct-debit/sec-codes.md) to understand which authorization type is right for your business.

In some cases, you might have pre-authorization from your customer from an earlier purchase or Setup Intent that you can use to create an _off-session_ (A payment is described as off-session if it occurs without the direct involvement of the customer, using previously-collected payment information) payment. For example:

- If you previously collected an online mandate from the customer, you can use both the IP address and user agent information to create a `mandate` object. If you didn’t retain your customer’s IP address or user agent information, you can provide placeholder data. If you provide placeholder data, we recommend selecting any value you can easily identify in the future.
- If you previously collected payment and mandate information offline, you can create a [PPD mandate](https://docs.stripe.com/payments/ach-direct-debit/sec-codes.md#ppd-sec-code).

Authorization is only required the first time you use a `BankAccount` object with the Payment Intents or Setup Intents API. After that, you can use the `BankAccount` object as a PaymentMethod to [accept future payments](https://docs.stripe.com/payments/ach-direct-debit/set-up-payment.md#web-future-payments).

You can create and confirm a Setup Intent to create a `mandate` without the need to charge a customer:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.create({
  customer: '{{CUSTOMER_ID}}',
  payment_method: '{{BANKACCOUNT_ID}}',
  payment_method_types: ['us_bank_account'],
  mandate_data: {
    customer_acceptance: {
      type: 'offline',
      accepted_at: 123456789,
    },
  },
  confirm: true,
});
```

You can also provide mandate data when confirming a Payment Intent:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.confirm(
  '{{PAYMENTINTENT_ID}}',
  {
    mandate_data: {
      customer_acceptance: {
        type: 'offline',
        accepted_at: 123456789,
      },
    },
    payment_method_options: {
      us_bank_account: {
        mandate_options: {
          collection_method: 'paper',
        },
      },
    },
  }
);
```

## Create a PaymentIntent with a Bank Account

You can use a saved `BankAccount` as a _PaymentMethod_ (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) when creating a PaymentIntent, which eliminates the need to recollect payment details. Make sure that you also [update your integration](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md) to begin creating PaymentMethods rather than Bank Accounts instead.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  customer: '{{CUSTOMER_ID}}',
  payment_method: '{{BANKACCOUNT_ID}}',
  payment_method_types: ['us_bank_account'],
  amount: 1099,
  currency: 'usd',
});
```

Similarly, you can use a saved BankAccount as a PaymentMethod when creating a SetupIntent.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.create({
  customer: '{{CUSTOMER_ID}}',
  payment_method: '{{BANKACCOUNT_ID}}',
  payment_method_types: ['us_bank_account'],
});
```

## Retrieve a BankAccount as a PaymentMethod

You can retrieve saved BankAccounts through the [Payment Methods API](https://docs.stripe.com/api/payment_methods.md):

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentMethod =
  await stripe.paymentMethods.retrieve('{{BANKACCOUNT_ID}}');
```

When using a BankAccount as a PaymentMethod, no new objects are created. The Payment Methods API simply provides a different view of the same underlying object.

#### PaymentMethod View

```json
{
  "id": "ba_1IsleZ2eZvKYlo2CI3To1g72",
  "object": "payment_method",
  "billing_details": {
    "address": {
      "city": null,
      "country": null,
      "line1": null,
      "line2": null,
      "postal_code": null,
      "state": null
    },
    "email": null,
    "name": "Jenny Rosen",
    "phone": null
  },
  "us_bank_account": {
    "last4": "6789",
    "routing_number": "110000000",
    "fingerprint": "1JWtPxqbdX5Gamtc",
    "account_holder_type": "individual",
    "bank_name": "STRIPE TEST BANK"
  },
  "created": 123456789,
  "customer": "cus_CY5bH92D99f4mn",
  "livemode": false,
  "metadata": {},
  "type": "us_bank_account"
}
```

#### BankAccount View

```json
{
  "id": "ba_1IsleZ2eZvKYlo2CI3To1g72",
  "object": "bank_account",
  "account_holder_name": "Jenny Rosen",
  "account_holder_type": "individual",
  "bank_name": "STRIPE TEST BANK",
  "country": "US",
  "currency": "usd",
  "customer": "cus_CY5bH92D99f4mn",
  "fingerprint": "1JWtPxqbdX5Gamtc",
  "last4": "6789",
  "metadata": {},
  "routing_number": "110000000",
  "status": "verified"
}
```

## Invoices

After you collect mandate acknowledgment, to continue using [Invoicing](https://docs.stripe.com/invoicing.md) you must either update your customer’s default payment method or set the `default_payment_method` parameter.

To update a customer’s default payment method:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customer = await stripe.customers.update('{{CUSTOMER_ID}}', {
  invoice_settings: {
    default_payment_method: '{{BANKACCOUNT_ID}}',
  },
});
```

To create an invoice with a bank account as a payment method:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const invoice = await stripe.invoices.create({
  customer: '{{CUSTOMER_ID}}',
  default_payment_method: '{{BANKACCOUNT_ID}}',
});
```

## Subscriptions

After you collect mandate acknowledgment, to continue using [Subscriptions](https://docs.stripe.com/subscriptions.md), you must either update your customer’s default payment method or set the `default_payment_method` parameter.

To update a customer’s default payment method:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customer = await stripe.customers.update('{{CUSTOMER_ID}}', {
  invoice_settings: {
    default_payment_method: '{{BANKACCOUNT_ID}}',
  },
});
```

To create an subscription with a bank account as a payment method:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const subscription = await stripe.subscriptions.create({
  customer: '{{CUSTOMER_ID}}',
  default_payment_method: '{{BANKACCOUNT_ID}}',
  items: [
    {
      price: 'price_1MowQULkdIwHu7ixraBm864M',
    },
  ],
});
```

## Identify Legacy ACH Payments

On a [Charge](https://docs.stripe.com/api/charges/object.md) object, the `payment_method_details.type` property is `ach_debit` for the legacy integration and `us_bank_account` for the newer integration.

A legacy ACH payment is created when a legacy `BankAccount` is the payment [source](https://docs.stripe.com/api/charges/object.md#charge_object-source). This happens when:

- You call the [Create Charge API](https://docs.stripe.com/api/charges/create.md).
- A [Subscription](https://docs.stripe.com/billing/subscriptions/overview.md) or [Invoice](https://docs.stripe.com/invoicing/overview.md) charges a customer whose `default_source` is a legacy BankAccount, and no `default_payment_method` is set on the customer, subscription, or invoice.
- You call the PaymentIntent API with a `payment_method_type` of `ach_debit`.
