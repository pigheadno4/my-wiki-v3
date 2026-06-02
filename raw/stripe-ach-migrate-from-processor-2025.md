<!-- Source URL: https://docs.stripe.com/payments/ach-direct-debit/migrating-bank-accounts -->
<!-- Fetched: 2026-05-02 -->

# Migrating from another processor

Migrate verified bank accounts from another payment processor with the Payment Methods API.

If you’ve verified bank accounts that you’ve used to process ACH Direct Debit payments on another processor, you can migrate them to Stripe to begin accepting payments.

You and Stripe both share responsibility for maintaining proof of authorization to debit, as well as verification of the bank account.

## Request a data migration with Stripe

Stripe works with you and your current payment processor to migrate data into your Stripe account. After the import completes, Stripe provides you with a CSV or JSON Mapping File to help you match the old customer IDs to the imported Stripe object IDs.

To request this option, submit an [intake form](https://support.stripe.com/contact/email?topic=migrations) and select the ACH payment type.

## Manually migrate bank accounts from another payment processor

If you choose to migrate yourself, Stripe temporarily allows you to bypass bank account verification. To request this temporary capability, contact [Stripe support](https://support.stripe.com/contact) and include details about how your business:

- Collects authorization from customers
- Verifies customer bank accounts

After Stripe enables this option, process each bank account and create a [SetupIntent](https://docs.stripe.com/api/setup_intents.md) for each account:

1. Create a new customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-configuration-customer) or [Customer](https://docs.stripe.com/api/customers.md), or retrieve an existing one to associate with this bank account.
1. Create and _confirm_ (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) a `SetupIntent` with your saved bank account details and the date of your customer’s original authorization to debit the account.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ['us_bank_account'],
  customer_account: '{{CUSTOMERACCOUNT_ID}}',
  confirm: true,
  payment_method_options: {
    us_bank_account: {
      verification_method: 'skip',
    },
  },
  payment_method_data: {
    type: 'us_bank_account',
    billing_details: {
      name: '{{ACCOUNT_HOLDER_NAME}}',
    },
    us_bank_account: {
      routing_number: '{{ROUTING_NUMBER}}',
      account_number: '{{ACCOUNT_NUMBER}}',
      account_holder_type: 'individual',
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
  payment_method_types: ['us_bank_account'],
  customer: '{{CUSTOMER_ID}}',
  confirm: true,
  payment_method_options: {
    us_bank_account: {
      verification_method: 'skip',
    },
  },
  payment_method_data: {
    type: 'us_bank_account',
    billing_details: {
      name: '{{ACCOUNT_HOLDER_NAME}}',
    },
    us_bank_account: {
      routing_number: '{{ROUTING_NUMBER}}',
      account_number: '{{ACCOUNT_NUMBER}}',
      account_holder_type: 'individual',
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

1. Retrieve and store the [PaymentMethod ID](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-payment_method) from the response to use for [future payments](https://docs.stripe.com/payments/ach-direct-debit/set-up-payment.md#web-future-payments). You can also retrieve it by [listing](https://docs.stripe.com/api/payment_methods/list.md) all PaymentMethods for the customer.
