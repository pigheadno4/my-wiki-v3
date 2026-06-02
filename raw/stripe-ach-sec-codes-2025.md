<!-- Source URL: https://docs.stripe.com/payments/ach-direct-debit/sec-codes -->
<!-- Fetched: 2026-05-02 -->

# Overview of ACH SEC codes

Learn about different types of customer authorizations for ACH Direct Debit.

A Standard Entry Class (SEC) code is a three letter code that describes how a customer or business authorized an ACH transaction. SEC codes are defined and maintained by [Nacha](https://www.nacha.org/newrules), the governing body for the ACH network.

Businesses must make sure that the correct code is used when initiating debit transactions to make sure they comply with ACH Direct Debit rules and appropriate authorization evidence in the event of a dispute. The business is responsible under the ACH Direct Debit rules for indicating the appropriate SEC code for each ACH transaction.

Stripe currently supports four types of SEC codes for ACH Debits. If you don’t specify a mandate collection method, Stripe defaults to using WEB for consumer bank accounts and CCD for business bank accounts.

The mandate requirements under ACH Direct Debit rules and applicable law vary based on the type of mandate collected. The information on this page relating to your compliance with ACH mandate requirements is for your general guidance, and isn’t legal advice. If you’re unsure of the applicable mandate requirements, consult with a professional about your obligations.

## WEB (Internet Initiated or Mobile Entry)

This code is used to initiate entries to a consumer’s account when the internet or a mobile device is used to initiate the transaction. WEB is the default unless you indicate otherwise. Refunds processed for WEB transactions use the PPD SEC code.

## CCD (Corporate Credit or Debit Entry)

This code is used to facilitate business-to-business payments and is applied to charges to all PaymentMethods that have `account_holder_type=company`, regardless of the authorization type.

## PPD (Prearranged Payment and Deposit)

This code is used to initiate entries to a consumer’s account, based on standing or single-entry authorization from that customer in writing. Your customer’s authorization must be in writing and signed or otherwise authenticated (that is, confirm the customer’s identity and agreement such as using a phone for a previously provided written authorization). Authorizations need to include information required for [online mandates](https://docs.stripe.com/payments/ach-direct-debit.md#mandates-for-online-custom-payment-forms) and you must provide a copy of the authorization to your customer.

To initiate a PPD debit, you must create a mandate with offline customer acceptance. You can do so by confirming a PaymentIntent or a SetupIntent with offline customer acceptance and providing a `collection_method=paper` mandate option as shown below:

#### PaymentIntent

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
        accepted_at: 1647448692,
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

#### SetupIntent

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.confirm(
  '{{SETUPINTENT_ID}}',
  {
    mandate_data: {
      customer_acceptance: {
        type: 'offline',
        accepted_at: 1647448692,
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

## TEL (Telephone-Initiated Entry) (Beta)

This code is used to initiate debit transactions to a consumer’s account when authorization is given over the telephone. TEL debits are currently in private beta. Contact Stripe Support if you initiate bank debits to consumer accounts over the telephone.

### Requirements for Telephone-initiated payments

If your business accepts ACH payments over the telephone, Stripe supports single TEL ACH debit transactions. Don’t use a TEL entry where a standing authorization is in place or to support a recurring transaction. TEL entries have their own Nacha requirements that you need to meet prior to accepting and processing these payments.

#### Existing relationship

You can only use a TEL entry if:

- You and the customer have an existing relationship, which means that:
  - You and the customer have a written agreement in place for the provision of goods or services; or
  - Your customer has purchased goods or services from you within the past 2 years; or
- You don’t have an existing relationship with the customer, but the customer initiated the telephone call to you.

Your customer’s pre-existing relationship with one of your affiliates isn’t sufficient to be an existing relationship between you and your customer.

#### Verifications

You must establish and implement commercially reasonable procedures to verify the identity of the customer (for example, name, address, and telephone number). Additionally, you must establish and implement commercially reasonable procedures to verify that the routing numbers provided by your customers are valid.

#### Authorization requirements

Your customer’s explicit oral authorization is needed prior to you initiating a debit entry to their account. Authorizations need to include information required for [online mandates](https://docs.stripe.com/payments/ach-direct-debit.md#mandates-for-online-custom-payment-forms), along with a telephone number available to your customer for inquiries.

In addition, you must capture authorization by either an audio recording of the customer’s oral authorization (in accordance with applicable state law regarding the recording of calls) or providing written notice to the customer of their authorization *before* the first debit of their bank account.

To confirm your payment, I understand that you, {{customer’s name}} authorize {{business name}} to debit you on {{debit date}} for the amount of {{amount}} for {{service provided}}. The account information you’ve provided me is as follows: Bank Name: {{bank name}}. Bank ABA Routing Number: {{routing number}}. Bank Account Type: {{checking/savings}}. Bank Account Number: {{account number}}. Is this information correct? As of today’s date, {{date}}, this debit authorization is valid and will remain in effect until you, {{customer name}}, notify {{business name}} of its cancellation by calling {{customer support phone number}}

For single TEL entries, if you provide a written notice instead of audio recording the authorization, you should indicate how you’ll provide that notice (for example, emails and mailed letters).
