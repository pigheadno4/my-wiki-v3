<!-- Source URL: https://docs.stripe.com/payments/nz-bank-account/migrate-from-another-processor -->
<!-- Fetched: 2026-05-03 -->

# Migrate from another processor

Migrate bank accounts from another payment processor with the Payment Methods API.

The Direct Debit Authority is the mandate that the customer gives to authorize the debit of the customer’s account. Before you migrate, make sure that you retain a copy of the Direct Debit Authority for each customer that you plan to migrate. Stripe might require you to provide copies of the Authorities, and you must do so promptly. Keep in mind that you continue to be responsible for any disputes opened before the migration.

## Migration notification

Inform your customers about the migration before it happens. You must include the following information:

- The name of your new processor: Stripe New Zealand Limited (direct debit authority code: `3143978`)
- The date when the transfer occurs (that is, when the migration will complete and when Stripe will start processing the direct debit payments)
- Your customer support contact details

Tell your customers that no further action is required from them, unless they choose to cancel the mandate.

## First debit notification

Inform your customers after you successfully process the first payment post-migration. You must send this notification in addition to the automatic notification that Stripe sends after successfully importing your customer bank account details.

## Stripe notifications

Stripe automatically notifies your customers after successfully importing your customer bank account details. See [mandate confirmation emails](https://docs.stripe.com/payments/nz-bank-account.md#mandate-confirmation-emails) for more information.

In addition, Stripe also notifies your customers on each of the new payments post-migration. See [pre-debit notification emails](https://docs.stripe.com/payments/nz-bank-account.md#pre-debit-notification-emails) for more information.

If you’ve turned off automatic notifications by Stripe, you must notify your customers. Specific requirements apply for these requirements, see [mandate confirmation emails](https://docs.stripe.com/payments/nz-bank-account.md#mandate-confirmation-emails) and [pre-debit notification emails](https://docs.stripe.com/payments/nz-bank-account.md#pre-debit-notification-emails) for more information.

## Manually migrate bank accounts from another payment processor

For each of your customers and bank accounts, create a [SetupIntent](https://docs.stripe.com/api/setup_intents.md):

1. Create a new object to represent your customer (either a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/object.md) or a [Customer](https://docs.stripe.com/api/customers.md)) or retrieve an existing one to associate with this bank account.
1. Create and *confirm* (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) a SetupIntent with your saved bank account details and the date of your customer’s original authorization to debit the account. You must include `billing_details.email` and `billing_details.name` because Stripe automatically sends mandate confirmation and pre-debit notification emails to customers.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.create({
  customer_account: '{{CUSTOMERACCOUNT_ID}}',
  confirm: true,
  payment_method_data: {
    type: 'nz_bank_account',
    nz_bank_account: {
      bank_code: '{{BANK_CODE}}',
      branch_code: '{{BRANCH_CODE}}',
      account_number: '{{ACCOUNT_NUMBER}}',
      suffix: '{{SUFFIX}}',
    },
    billing_details: {
      email: '{{CUSTOMER_EMAIL}}',
      name: '{{CUSTOMER_NAME}}',
    },
  },
  mandate_data: {
    customer_acceptance: {
      type: 'offline',
      accepted_at: 1692821946,
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
  customer: '{{CUSTOMER_ID}}',
  confirm: true,
  payment_method_data: {
    type: 'nz_bank_account',
    nz_bank_account: {
      bank_code: '{{BANK_CODE}}',
      branch_code: '{{BRANCH_CODE}}',
      account_number: '{{ACCOUNT_NUMBER}}',
      suffix: '{{SUFFIX}}',
    },
    billing_details: {
      email: '{{CUSTOMER_EMAIL}}',
      name: '{{CUSTOMER_NAME}}',
    },
  },
  mandate_data: {
    customer_acceptance: {
      type: 'offline',
      accepted_at: 1692821946,
    },
  },
});
```

1. Retrieve and store the [PaymentMethod ID](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-payment_method) from the response to use for [future payments](https://docs.stripe.com/payments/nz-bank-account/accept-a-payment.md). You can also retrieve it by [listing](https://docs.stripe.com/api/payment_methods/list.md) all PaymentMethods for the customer.
