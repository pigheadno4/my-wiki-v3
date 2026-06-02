<!-- Source URL: https://docs.stripe.com/payments/ach-direct-debit/nacha-compliance -->
<!-- Fetched: 2026-05-02 -->

# Nacha compliance for online consumer purchases

Learn how to classify ACH Direct Debit transactions.

Effective March 20, 2026, the National Automated Clearing House Association (Nacha) requires you to label e-commerce purchases made through ACH debits by including `PURCHASE` in the Company Entry Description.

An ACH debit transaction qualifies as an e-commerce purchase when it meets both of the following conditions:

- A consumer authorizes it for the online purchase of physical or digital goods.
- It uses the [SEC](https://docs.stripe.com/payments/ach-direct-debit/sec-codes.md) code `WEB` or `TEL`.

This requirement doesn’t apply to purchases of services, donations, or bill payments.

## Implementation guidance

Configure how Stripe classifies your ACH debit transactions in either of the following ways:

- **Stripe Dashboard setting**: Configure your classification setting in the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods). Choose between automatically classifying transactions, classifying all transactions as goods, or not classifying any transactions as goods.
- **API configuration**: If you use the Payment Intents API, control classification per transaction through the `transaction_purpose` field. For details, see the [API documentation](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-us_bank_account).

## Stripe Dashboard setting

Stripe provides a Stripe Dashboard setting to configure how your ACH Direct Debit transactions are classified.

### Classification option

- **Automatically classify transactions**: Stripe determines whether each transaction represents a purchase of goods based on available signals such as business information and transaction details.
- **Classify all transactions as goods**: Use this option if you exclusively sell physical or digital products. Stripe classifies all your ACH transactions as purchases of goods.
- **Don’t classify any transactions as goods**: Use this option if you provide services, accept donations, or collect bill payments instead of selling goods.

### Configure Nacha classification

For ACH Direct Debit:

1. Go to **Settings** > **Payment methods** > **ACH Direct Debit**.
1. Locate **ACH classification**.
1. Select a classification option.

### Configure Nacha classification for Connect platforms

If you use Connect, configure the same options in your payment method settings. When you configure your ACH classification setting in the Stripe Dashboard, that setting applies to direct charges on your platform account and to [destination charges](https://docs.stripe.com/connect/destination-charges.md) and [separate charges and transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md) that don’t set `on_behalf_of`.

To configure settings for direct charges on your Connect accounts or charges with the `on_behalf_of` parameter in the Dashboard:

1. Go to **Settings** > **Connect** > **Payment methods**.
1. In **ACH Direct Debit**, click **Configure Nacha classification**.
1. Select a classification option.

## Configure Nacha classification through the API

Use `transaction_purpose` in `payment_method_options.us_bank_account` on the [Payment Intents](https://docs.stripe.com/api/payment_intents.md) API for transaction-level classification.

To classify an individual transaction as an e-commerce purchase, set `transaction_purpose` to `goods`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 100,
  currency: 'usd',
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_data: {
    type: 'us_bank_account',
    us_bank_account: {
      account_number: '000123456789',
      routing_number: '110000000',
      account_type: 'checking',
      account_holder_type: 'individual',
    },
    billing_details: {
      name: '{{CUSTOMER_NAME}}',
    },
  },
  payment_method_options: {
    us_bank_account: {
      verification_method: 'microdeposits',
      transaction_purpose: 'goods',
    },
  },
});
```

Transactions with this `transaction_purpose` include `PURCHASE` in the company entry description.

To classify a transaction as a purchase of services or as something other than goods, set `transaction_purpose` to `services` or `other`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 100,
  currency: 'usd',
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_data: {
    type: 'us_bank_account',
    us_bank_account: {
      account_number: '000123456789',
      routing_number: '110000000',
      account_type: 'checking',
      account_holder_type: 'individual',
    },
    billing_details: {
      name: '{{CUSTOMER_NAME}}',
    },
  },
  payment_method_options: {
    us_bank_account: {
      verification_method: 'microdeposits',
      transaction_purpose: 'services',
    },
  },
});
```

Transactions with either `transaction_purpose` don’t include `PURCHASE` in the company entry description.

This field is optional. If you don’t provide a value, Stripe uses your **ACH classification** setting in the Stripe Dashboard. If you don’t configure a Stripe Dashboard setting, Stripe classifies transactions automatically based on available signals such as business information and transaction details.

For more information, see the [API documentation](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-us_bank_account).
