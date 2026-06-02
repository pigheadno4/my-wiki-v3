<!-- Source URL: https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment -->
<!-- Fetched: 2026-05-02 -->

# Accept an ACH Direct Debit payment

Build a custom payment form or use Stripe Checkout to accept payments with ACH Direct Debit.

# Checkout

> This is a Checkout for when payment-ui is checkout. View the full page at https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment?payment-ui=checkout.

> Stripe can automatically present the relevant payment methods to your customers by evaluating currency, payment method restrictions, and other parameters.
>
> - Follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=checkout&ui=stripe-hosted) guide to build a Checkout integration that uses [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md).

- If you don’t want to use dynamic payment methods, follow the steps below to manually configure the payment methods in your Checkout integration.

Stripe users in the US can use Checkout in payment mode to accept ACH Direct Debit payments.

A Checkout Session represents the details of your customer’s intent to purchase. You create a Session when your customer wants to pay for something. After redirecting your customer to a Checkout Session, Stripe presents a payment form where your customer can complete their purchase. After your customer completes a purchase, they redirect back to your site.

With Checkout, you can create a Checkout Session with `us_bank_account` as a payment method type to track and handle the states of the payment until the payment completes.

> ACH Direct Debit is a [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method, which means that funds aren’t immediately available after payment. A payment typically takes 4 business days to arrive in your account.

## Determine compatibility

**Supported business locations**: US

**Supported currencies**: `usd`

**Presentment currencies**: `usd`

**Payment mode**: Yes

**Setup mode**: Yes

**Subscription mode**: Yes

To support ACH Direct Debit payments, make sure you express _Prices_ (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) for all line items in US dollars (currency code `usd`).

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
  contact_email: '{{CUSTOMER_EMAIL}}',
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

## Accept a payment

> Build an integration to [accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?integration=checkout) with Checkout before using this guide.

This guides you through enabling ACH Direct Debit and shows the differences between accepting payments using dynamic payment methods and manually configuring payment methods.

### Enable ACH Direct Debit as a payment method

When creating a new [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md), you need to:

1. Add `us_bank_account` to the list of `payment_method_types`.
1. Make sure all your `line_items` use the `usd` currency.

#### Stripe-hosted page

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({
  customer_account: '{{CUSTOMERACCOUNT_ID}}',
  line_items: [
    {
      price_data: {
        currency: 'usd',
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: 'payment',
  payment_method_types: ['card', 'us_bank_account'],
  success_url: 'https://example.com/success',
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({
  customer: '{{CUSTOMER_ID}}',
  line_items: [
    {
      price_data: {
        currency: 'usd',
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: 'payment',
  payment_method_types: ['card', 'us_bank_account'],
  success_url: 'https://example.com/success',
});
```

#### Full embedded page

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({
  customer_account: '{{CUSTOMERACCOUNT_ID}}',
  line_items: [
    {
      price_data: {
        currency: 'usd',
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: 'payment',
  payment_method_types: ['card', 'us_bank_account'],
  return_url: 'https://example.com/return',
  ui_mode: 'embedded_page',
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({
  customer: '{{CUSTOMER_ID}}',
  line_items: [
    {
      price_data: {
        currency: 'usd',
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: 'payment',
  payment_method_types: ['card', 'us_bank_account'],
  return_url: 'https://example.com/return',
  ui_mode: 'embedded_page',
});
```

For more information on Financial Connections fees, see [pricing details](https://stripe.com/financial-connections#pricing).

By default, collecting bank account payment information uses [Financial Connections](https://docs.stripe.com/financial-connections.md) to instantly verify your customer’s account, with a fallback option of manual account number entry and microdeposit verification. See the [Financial Connections docs](https://docs.stripe.com/financial-connections/ach-direct-debit-payments.md) to learn how to configure Financial Connections and access additional account data to optimize your ACH integration. For example, you can use Financial Connections to check an account’s balance before initiating the ACH payment.

> To expand access to additional data after a customer authenticates their account, they must re-link their account with expanded permissions.

If the customer opts for microdeposit verification instead of Financial Connections, Stripe automatically sends two small deposits to the provided bank account. These deposits can take 1-2 business days to appear on the customer’s online bank statement. When the deposits are expected to arrive, the customer receives an email with a link to confirm these amounts and verify the bank account with Stripe. After verification is complete, the payment begins processing.

We recommend including the [payment_intent_data.setup_future_usage](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-setup_future_usage) parameter with a value of `off_session` when creating a payment mode Session for ACH Direct Debit so you can [save payment method details](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=checkout&ui=stripe-hosted#save-payment-method-details).

### Fulfill your orders

After accepting a payment, learn how to [fulfill orders](https://docs.stripe.com/checkout/fulfillment.md).

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

Test transactions settle instantly and are added to your available test balance. This behavior differs from livemode, where transactions can take [multiple days](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md#timing) to settle in your available balance.

## Additional considerations

### Microdeposit verification failure

When a bank account is pending verification with microdeposits, the customer can fail to verify for three reasons:

- The microdeposits failed to send to the customer’s bank account (this usually indicates a closed or unavailable bank account or incorrect bank account number).
- The customer made 10 failed verification attempts for the account. Exceeding this limit means the bank account can no longer be verified or reused.
- The customer failed to verify the bank account within 10 days.

If the bank account fails verification for one of these reasons, you can [handle the `checkout.session.async_payment_failed` event](https://docs.stripe.com/api/events/types.md?event_types-invoice.payment_succeeded=#event_types-checkout.session.async_payment_failed) to contact the customer about placing a new order.

## Optional: Instant only verification

By default, ACH Direct Debit payments allow your customers to use instant bank account verification or microdeposits. You can optionally require instant bank account verification using the `payment_method_options[us_bank_account][verification_method]` parameter when you create the Checkout Session.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({
  mode: 'payment',
  customer_account: '{{CUSTOMERACCOUNT_ID}}',
  payment_method_types: ['card', 'us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      verification_method: 'instant',
      financial_connections: {
        permissions: ['payment_method'],
      },
    },
  },
  line_items: [
    {
      price_data: {
        currency: 'usd',
        unit_amount: 2000,
        product_data: {
          name: "T-shirt",
        },
      },
      quantity: 1,
    },
  ],
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
  payment_method_types: ['card', 'us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      verification_method: 'instant',
      financial_connections: {
        permissions: ['payment_method'],
      },
    },
  },
  line_items: [
    {
      price_data: {
        currency: 'usd',
        unit_amount: 2000,
        product_data: {
          name: "T-shirt",
        },
      },
      quantity: 1,
    },
  ],
  success_url: 'https://example.com/success',
});
```

## Optional: Access data on a Financial Connections bank account

You can only access Financial Connections data if you request additional [data permissions](https://docs.stripe.com/financial-connections/fundamentals.md#data-permissions) when you create your PaymentIntent .

After your customer successfully completes the Checkout flow, the `us_bank_account` PaymentMethod returned includes a [financial_connections_account](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-us_bank_account-financial_connections_account) ID that points to a [Financial Connections Account](https://docs.stripe.com/api/financial_connections/accounts.md). Use this ID to access account data.

> Bank accounts that your customers link through manual entry and microdeposits don’t have a `financial_connections_account` ID on the Payment Method.

To determine the Financial Connections account ID, retrieve the Checkout Session and expand the `payment_intent.payment_method` attribute:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.retrieve(
  "{{CHECKOUTSESSION_ID}}",
  {
    expand: ["payment_intent.payment_method"],
  },
);
```

```json
{
  "id": "{{CHECKOUT_SESSION_ID}}",
  "object": "checkout.session",
  // ...
  "payment_intent": {
    "id": "{{PAYMENT_INTENT_ID}}",
    "object": "payment_intent",
    // ...
    "payment_method": {
      "id": "{{PAYMENT_METHOD_ID}}",
      // ...
      "type": "us_bank_account",
      "us_bank_account": {
        "account_holder_type": "individual",
        "account_type": "checking",
        "bank_name": "TEST BANK",
        "financial_connections_account": "{{FINANCIAL_CONNECTIONS_ACCOUNT_ID}}",
        "fingerprint": "q9qchffggRjlX2tb",
        "last4": "6789",
        "routing_number": "110000000"
      }
    }
    // ...
  }
}
```

Learn more about using additional account data to optimize your ACH integration with [Financial Connections](https://docs.stripe.com/financial-connections/ach-direct-debit-payments.md#optimize).

## Optional: Resolve disputes [Server-side]

Customers can generally [dispute an ACH Direct Debit payment](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md#resolving-disputes) through their bank for up to 60 calendar days after a debit on a personal account, or up to 2 business days for a business account. In rare instances, a customer might be able to successfully dispute a debit payment outside these standard dispute timelines.

When a customer disputes a payment, Stripe sends a [charge.dispute.closed](https://docs.stripe.com/api/events/types.md#event_types-charge.dispute.closed) webhook event, and the PaymentMethod authorization is revoked.

In rare situations, Stripe might receive an ACH failure from the bank after a PaymentIntent has transitioned to `succeeded`. If this happens, Stripe creates a dispute with a `reason` of:

- `insufficient_funds`
- `incorrect_account_details`
- `bank_can't_process`

Stripe charges a failure fee in this situation.

Future payments reusing this PaymentMethod return the following error:

```javascript
{
  "error": {
    "message": "This PaymentIntent requires a mandate, but no existing mandate was found. Collect mandate acceptance from the customer and try again, providing acceptance data in the mandate_data parameter.",
    "payment_intent": {
      ...
    }
    "type": "invalid_request_error"
  }
}
```

This error contains a PaymentIntent in the `requires_confirmation` state. To continue with the payment, you must:

1. Resolve the dispute with the customer to ensure future payments won’t be disputed.
1. Confirm authorization from your customer again.

To confirm authorization for the payment, you can [collect mandate acknowledgement from your customer online with Stripe.js](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md?platform=web#web-collect-mandate-and-submit) or confirm authorization with your customer offline using the Stripe API.

> If a customer disputes more than one payment from the same bank account, Stripe blocks their bank account. Contact [Stripe Support](https://support.stripe.com/?contact=true) for further resolution.

```curl
curl https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT_ID}}/confirm \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "mandate_data[customer_acceptance][type]=offline"
```

## Optional: Payment Reference

The payment reference number is a bank-generated value that allows the bank account owner to use their bank to locate funds. When the payment succeeds, Stripe provides the payment reference number in the Dashboard and inside the [Charge object](https://docs.stripe.com/api/charges/object.md).

| Charge State | Payment Reference Value                  |
| ------------ | ---------------------------------------- |
| Pending      | Unavailable                              |
| Failed       | Unavailable                              |
| Succeeded    | Available (for example, 091000015001234) |

In addition, when you receive the `charge.succeeded` webhook, view the content of `payment_method_details` to locate the [payment_reference](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-us_bank_account-payment_reference).

The following example event shows the rendering of a successful ACH payment with a payment reference number.

#### charge-succeeded

```json
{
  "id": "{{EVENT_ID}}",
  "object": "event",
  // omitted some fields in the example
  "type": "charge.succeeded",
  "data": {
    "object": {
      "id": "{{PAYMENT_ID}}",
      "object": "charge",
      //...
      "paid": true,
      "payment_intent": "{{PAYMENT_INTENT_ID}}",
      "payment_method": "{{PAYMENT_METHOD_ID}}",
      "payment_method_details": {
        "type": "us_bank_account",
        "us_bank_account": {
          "account_holder_type": "individual",
          "account_type": "checking",
          "bank_name": "TEST BANK",
          "fingerprint": "Ih3foEnRvLXShyfB",
          "last4": "1000",
          "payment_reference": "091000015001234",
          "routing_number": "110000000"
        }
      }
      // ...
    }
  }
}
```

View the contents of the `destination_details` to locate the [refund reference](https://docs.stripe.com/api/refunds/object.md#refund_object-destination_details-us_bank_transfer-reference) associated with the refunded ACH payments.

The following example event shows the rendering of a successful ACH refund with a refund reference number. Learn more about [refunds](https://docs.stripe.com/refunds.md).

#### charge-refund-updated

```json
{
  "id": "{{EVENT_ID}}",
  "object": "event",
  "type": "charge.refund.updated",
  "data": {
    "object": {
      "id": "{{REFUND_ID}}",
      "object": "refund",
      //...
      "payment_intent": "{{PAYMENT_INTENT_ID}}",
      "destination_details": {
        "type": "us_bank_transfer",
        "us_bank_transfer": {
          "reference": "091000015001111",
          "reference_status": "available"
        }
      }
      // ...
    }
  }
}
```

## Optional: Configure customer debit date [Server-side]

You can control the date that Stripe debits a customer’s bank account using the [target date](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-payment_method_options-us_bank_account-target_date). The target date must be at least three days in the future and no more than 15 days from the current date.

The target date schedules money to leave the customer’s account on the target date.

Target dates that meet one of the following criteria delay the debit until the next available business day:

- Target date falls on a weekend, a bank holiday, or other non-business day.
- Target date is fewer than three business days in the future.

This parameter operates on a best-effort basis. Each customer’s bank might process debits on different dates, depending on local bank holidays or other reasons.

> You can’t set the [verification method](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-payment_method_options-us_bank_account-verification_method) to `microdeposits` when using a [target date](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-payment_method_options-us_bank_account-target_date), as the verification process could take longer than the target date, causing payments to arrive later than expected.

## See also

- [Save ACH Direct Debit pre-authorized debit details for future payments](https://docs.stripe.com/payments/ach-direct-debit/set-up-payment.md)

# Checkout Sessions API

> This is a Checkout Sessions API for when payment-ui is elements and api-integration is checkout. View the full page at https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment?payment-ui=elements&api-integration=checkout.

To determine which API meets your business needs, see the [comparison guide](https://docs.stripe.com/payments/checkout-sessions-and-payment-intents-comparison.md).

Use the [Payment Element](https://docs.stripe.com/payments/payment-element.md) to embed a custom Stripe payment form in your website or application and offer payment methods to customers. For advanced configurations and customizations, refer to the [Accept a Payment](https://docs.stripe.com/payments/accept-a-payment.md) integration guide.

Before you use ACH direct debit in your Payment Element integration, learn about the following ACH direct debit considerations:

- Learn about [mandate collection](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md#mandate-collection).
- Choose how you [verify bank accounts](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md#bank-verification).

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

### Mandate collection

When accepting ACH payments, you need to understand mandates.

Unless you use a direct API integration, Stripe handles mandate collection and storage for your business to make sure that regulatory requirements are met. When a customer accepts the mandate during the payment process, Stripe automatically stores this information and it becomes available for you to access from your Dashboard.

## Set up the server [Server-side]

Use the official Stripe libraries to access the API from your application.

#### Node.js

```bash
# Install with npm
npm install stripe --save
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
          currency: 'usd',
          product_data: {
            name: 'T-shirt',
          },
          unit_amount: 2000,
        },
        quantity: 1,
      },
    ],
    mode: 'payment',ui_mode: 'elements',
    // The URL of your payment completion page
    return_url: 'https://example.com/return?session_id={CHECKOUT_SESSION_ID}'
  });

  res.json({checkoutSessionClientSecret: session.client_secret});
});

app.listen(3000, () => {
  console.log('Running on port 3000');
});
```

#### Manually list payment methods

To manually list a payment method, specify it in [payment_method_types](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_method_types) when you create a [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md). If you have `line_items` in different currencies, you need to create separate Checkout Sessions.

#### TypeScript

```javascript
import express, {Express} from 'express';

const app: Express = express();

app.post('/create-checkout-session', async (req: Express.Request, res: Express.Response) => {
  const session = await stripe.checkout.sessions.create({
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
    mode: 'payment',
    ui_mode: 'elements',
    payment_method_types: ['us_bank_account'],
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

Ensure you’re on the latest Stripe.js version by including the following script tag `<script src=“https://js.stripe.com/dahlia/stripe.js”></script>`. Learn more about [Stripe.js versioning](https://docs.stripe.com/sdks/stripejs-versioning.md).

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
const clientSecret = fetch("/create-checkout-session", { method: "POST" })
  .then((response) => response.json())
  .then((json) => json.client_secret);

const checkout = stripe.initCheckoutElementsSdk({ clientSecret });
const loadActionsResult = await checkout.loadActions();

if (loadActionsResult.type === "success") {
  const session = loadActionsResult.actions.getSession();
  const checkoutContainer = document.getElementById("checkout-container");

  checkoutContainer.append(JSON.stringify(session.lineItems, null, 2));
  checkoutContainer.append(document.createElement("br"));
  checkoutContainer.append(`Total: ${session.total.total.amount}`);
}
```

#### React

Wrap your application with the [CheckoutElementsProvider](https://docs.stripe.com/js/react_stripe_js/checkout/checkout_provider) component, passing in `clientSecret` and the `stripe` instance.

```jsx
import React from "react";
import { CheckoutElementsProvider } from "@stripe/react-stripe-js/checkout";
import CheckoutForm from "./CheckoutForm";

const clientSecret = fetch("/create-checkout-session", { method: "POST" })
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

  if (checkoutState.type === "loading") {
    return <div>Loading...</div>;
  }

  if (checkoutState.type === "error") {
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

if (loadActionsResult.type === "success") {
  const { actions } = loadActionsResult;
  const emailInput = document.getElementById("email");
  const emailErrors = document.getElementById("email-errors");

  emailInput.addEventListener("input", () => {
    // Clear any validation errors
    emailErrors.textContent = "";
  });

  emailInput.addEventListener("blur", () => {
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

  if (checkoutState.type === "loading") {
    return <div>Loading...</div>;
  } else if (checkoutState.type === "error") {
    return <div>Error: {checkoutState.error.message}</div>;
  }

  const handleBlur = () => {
    checkoutState.checkout.updateEmail(email).then((result) => {
      if (result.type === "error") {
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

  if (checkoutState.type === "loading") {
    return <div>Loading...</div>;
  }

  if (checkoutState.type === "error") {
    return <div>Error: {checkoutState.error.message}</div>;
  }

  return (
    <form>
      {JSON.stringify(checkoutState.checkout.lineItems, null, 2)}
      {/* A formatted total amount */}
      Total: {checkoutState.checkout.total.total.amount}
      <PaymentElement options={{ layout: "accordion" }} />
    </form>
  );
};

export default CheckoutForm;
```

See the [Stripe.js docs](https://docs.stripe.com/js/custom_checkout/create_payment_element#custom_checkout_create_payment_element-options) to view the supported options.

You can [customize the appearance](https://docs.stripe.com/payments/checkout/customization/appearance.md) of all Elements by passing [elementsOptions.appearance](https://docs.stripe.com/js/react_stripe_js/checkout/checkout_provider#react_checkout_provider-options-elementsOptions-appearance) to the [CheckoutElementsProvider](https://docs.stripe.com/js/react_stripe_js/checkout/checkout_provider).

## Verify bank accounts

#### Item 1

For information on Financial Connections fees, see [pricing details](https://stripe.com/financial-connections#pricing).

Bank account verification uses automatic verification to collect payment information through [Financial Connections](https://docs.stripe.com/financial-connections.md) by default. No changes are required to use it. You can change your verification method by setting `payment_method_options[us_bank_account][verification_method]` when creating the Checkout Session to `instant` to make all users verify their bank accounts with Financial Connections. To learn how to configure Financial Connections and access additional account data, such as checking an account’s balance before initiating a payment, see the [Financial Connections](https://docs.stripe.com/financial-connections.md).

#### Automatic (default)

By default, collecting bank account payment information uses [Financial Connections](https://docs.stripe.com/financial-connections.md) to instantly verify your customer’s account. If instant verification isn’t possible, it falls back to manual account number entry and microdeposit verification.

> To expand access to additional data after a customer authenticates their account, the customer needs to re-link their account with expanded permissions. This authentication occurs one time per customer, and the permission it grants is reusable.

**Microdeposit verification**Not all customers can verify their bank account instantly. This section only applies if your customer has elected to opt out of the instant verification flow in the previous step. In these cases, Stripe sends 1-2 microdeposits to a customer’s bank account for verification instead. These deposits take 1-2 business days to appear on the customer’s online statement.

There are two types of microdeposits:

- **Descriptor code** (default): Stripe sends a 0.01 USD microdeposit to the customer’s bank account with a unique 6-digit `descriptor_code` that starts with SM. Your customer uses this code to verify their bank account.
- **Amount**: Stripe sends two, non-unique microdeposits to the customer’s bank account, with a statement descriptor that reads `ACCTVERIFY`. Your customer uses the deposit amounts to verify their bank account.

**Microdeposit verification failure**When a bank account is pending verification with microdeposits, verification can fail in several ways:

- The microdeposits fail to arrive in the customer’s bank account (this usually indicates a closed or unavailable bank account or incorrect bank account number).
- The customer exceeds the limit of verification attempts for the account. Exceeding this limit means the bank account can no longer be verified or reused.
- The customer didn’t complete verification within 10 days.

#### Instant

You can enforce all of your customers to verify their bank accounts with Financial Connections by using instant verification.

To use instant verification, set the `payment_method_options[us_bank_account][verification_method]` parameter to `instant` when you create a Checkout Session.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({
  customer_account: '{{CUSTOMERACCOUNT_ID}}',
  line_items: [
    {
      price_data: {
        currency: 'usd',
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: 'payment',
  ui_mode: 'elements',
  payment_method_options: {
    us_bank_account: {
      verification_method: 'instant',
      financial_connections: {
        permissions: ['payment_method'],
      },
    },
  },
  return_url: 'https://example.com/return?session_id={CHECKOUT_SESSION_ID}',
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({
  customer: '{{CUSTOMER_ID}}',
  line_items: [
    {
      price_data: {
        currency: 'usd',
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: 'payment',
  ui_mode: 'elements',
  payment_method_options: {
    us_bank_account: {
      verification_method: 'instant',
      financial_connections: {
        permissions: ['payment_method'],
      },
    },
  },
  return_url: 'https://example.com/return?session_id={CHECKOUT_SESSION_ID}',
});
```

On the client side, the Payment Element created through `checkout.createPaymentElement()` automatically uses the verification method configured in the Checkout Session. No additional configuration is needed.

#### Item 2

For information on Financial Connections fees, see [pricing details](https://stripe.com/financial-connections#pricing).

Bank account verification uses automatic verification to collect payment information through [Financial Connections](https://docs.stripe.com/financial-connections.md) by default. No changes are required to use it. You can change your verification method by setting `payment_method_options[us_bank_account][verification_method]` when creating the Checkout Session to `instant` to make all users verify their bank accounts with Financial Connections. To learn how to configure Financial Connections and access additional account data, such as checking an account’s balance before initiating a payment, see the [Financial Connections](https://docs.stripe.com/financial-connections.md).

#### Automatic (default)

By default, collecting bank account payment information uses [Financial Connections](https://docs.stripe.com/financial-connections.md) to instantly verify your customer’s account. If instant verification isn’t possible, it falls back to manual account number entry and microdeposit verification.

> To expand access to additional data after a customer authenticates their account, the customer needs to re-link their account with expanded permissions. This authentication occurs one time per customer, and the permission it grants is reusable.

**Microdeposit verification**Not all customers can verify their bank account instantly. This section only applies if your customer has elected to opt out of the instant verification flow in the previous step. In these cases, Stripe sends 1-2 microdeposits to a customer’s bank account for verification instead. These deposits take 1-2 business days to appear on the customer’s online statement.

There are two types of microdeposits:

- **Descriptor code** (default): Stripe sends a 0.01 USD microdeposit to the customer’s bank account with a unique 6-digit `descriptor_code` that starts with SM. Your customer uses this code to verify their bank account.
- **Amount**: Stripe sends two, non-unique microdeposits to the customer’s bank account, with a statement descriptor that reads `ACCTVERIFY`. Your customer uses the deposit amounts to verify their bank account.

**Microdeposit verification failure**When a bank account is pending verification with microdeposits, verification can fail in several ways:

- The microdeposits fail to arrive in the customer’s bank account (this usually indicates a closed or unavailable bank account or incorrect bank account number).
- The customer exceeds the limit of verification attempts for the account. Exceeding this limit means the bank account can no longer be verified or reused.
- The customer didn’t complete verification within 10 days.

#### Instant

You can enforce all of your customers to verify their bank accounts with Financial Connections by using instant verification.

To use instant verification, set the `payment_method_options[us_bank_account][verification_method]` parameter to `instant` when you create a Checkout Session.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({
  customer_account: '{{CUSTOMERACCOUNT_ID}}',
  line_items: [
    {
      price_data: {
        currency: 'usd',
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: 'payment',
  ui_mode: 'elements',
  payment_method_types: ['card', 'us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      verification_method: 'instant',
      financial_connections: {
        permissions: ['payment_method'],
      },
    },
  },
  return_url: 'https://example.com/return?session_id={CHECKOUT_SESSION_ID}',
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({
  customer: '{{CUSTOMER_ID}}',
  line_items: [
    {
      price_data: {
        currency: 'usd',
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: 'payment',
  ui_mode: 'elements',
  payment_method_types: ['card', 'us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      verification_method: 'instant',
      financial_connections: {
        permissions: ['payment_method'],
      },
    },
  },
  return_url: 'https://example.com/return?session_id={CHECKOUT_SESSION_ID}',
});
```

On the client side, the Payment Element created through `checkout.createPaymentElement()` automatically uses the verification method configured in the Checkout Session. No additional configuration is needed.

## Submit the payment [Client-side]

#### HTML + JS

Render a **Pay** button that calls [confirm](https://docs.stripe.com/js/custom_checkout/confirm) from the `Checkout` instance to submit the payment.

```html
<button id="pay-button">Pay</button>
<div id="confirm-errors"></div>
```

```js
const checkout = stripe.initCheckoutElementsSdk({ clientSecret });

checkout.on("change", (session) => {
  document.getElementById("pay-button").disabled = !session.canConfirm;
});

const loadActionsResult = await checkout.loadActions();

if (loadActionsResult.type === "success") {
  const { actions } = loadActionsResult;
  const button = document.getElementById("pay-button");
  const errors = document.getElementById("confirm-errors");
  button.addEventListener("click", () => {
    // Clear any validation errors
    errors.textContent = "";

    actions.confirm().then((result) => {
      if (result.type === "error") {
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

  if (checkoutState.type !== "success") {
    return null;
  }

  const handleClick = () => {
    setLoading(true);
    checkoutState.checkout.confirm().then((result) => {
      if (result.type === "error") {
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

## Handle post-payment events

Stripe sends a [checkout.session.async_payment_succeeded](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.async_payment_succeeded) event when the payment completes. Use the Dashboard, a custom _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

- **Handle events manually in the Dashboard**

  Use the Dashboard to [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments), send email receipts, handle payouts, or retry failed payments.

- **Build a custom webhook**

  [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook) handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- **Integrate a prebuilt app**

  Handle common business events, such as [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

## Test your integration

Learn how to test scenarios with instant verifications using [Financial Connections](https://docs.stripe.com/financial-connections/testing.md#web-how-to-use-test-accounts).

### Send transaction emails in a sandbox

After you collect the bank account details and accept a mandate, send the mandate confirmation and microdeposit verification emails in a _sandbox_ (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes).

If your domain is **{domain}** and your username is **{username}**, use the following email format to send test transaction emails: **{username}+test_email@{domain}**.

For example, if your domain is **example.com** and your username is **info**, use the format **info+test\_email@example.com** for testing ACH Direct Debit payments. This format ensures that emails route correctly. If you don’t include the **+test_email** suffix, we won’t send the email.

> You must [set up your Stripe account](https://docs.stripe.com/get-started/account/set-up.md) before you can trigger these emails while testing.

### Test account numbers

Stripe provides several test account numbers and corresponding tokens you can use to make sure your integration for manually-entered bank accounts is ready for production.

| Account number | Token                                  | Routing number | Behavior                                                                                                                                                 |
| -------------- | -------------------------------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `000123456789` | `pm_usBankAccount_success`             | `110000000`    | The payment succeeds.                                                                                                                                    |
| `000111111113` | `pm_usBankAccount_accountClosed`       | `110000000`    | The payment fails because the account is closed.                                                                                                         |
| `000000004954` | `pm_usBankAccount_riskLevelHighest`    | `110000000`    | The payment is blocked by Radar due to a [high risk of fraud](https://docs.stripe.com/radar/risk-evaluation.md#high-risk).                               |
| `000111111116` | `pm_usBankAccount_noAccount`           | `110000000`    | The payment fails because no account is found.                                                                                                           |
| `000222222227` | `pm_usBankAccount_insufficientFunds`   | `110000000`    | The payment fails due to insufficient funds.                                                                                                             |
| `000333333335` | `pm_usBankAccount_debitNotAuthorized`  | `110000000`    | The payment fails because debits aren’t authorized.                                                                                                      |
| `000444444440` | `pm_usBankAccount_invalidCurrency`     | `110000000`    | The payment fails due to invalid currency.                                                                                                               |
| `000666666661` | `pm_usBankAccount_failMicrodeposits`   | `110000000`    | The payment fails to send microdeposits.                                                                                                                 |
| `000555555559` | `pm_usBankAccount_dispute`             | `110000000`    | The payment triggers a dispute.                                                                                                                          |
| `000000000009` | `pm_usBankAccount_processing`          | `110000000`    | The payment stays in processing indefinitely. Useful for testing [Checkout Session expiration](https://docs.stripe.com/api/checkout/sessions/expire.md). |
| `000777777771` | `pm_usBankAccount_weeklyLimitExceeded` | `110000000`    | The payment fails due to payment amount causing the account to exceed its weekly payment volume limit.                                                   |
| `000888888885` |                                        | `110000000`    | The payment fails because of a deactivated [tokenized account number](https://docs.stripe.com/financial-connections/tokenized-account-numbers.md).       |

Before test transactions can complete, you need to verify all test accounts that automatically succeed or fail the payment. To do so, use the test microdeposit amounts or descriptor codes below.

### Test microdeposit amounts and descriptor codes

To mimic different scenarios, use these microdeposit amounts _or_ 0.01 descriptor code values.

| Microdeposit values | 0.01 descriptor code values | Scenario                                                         |
| ------------------- | --------------------------- | ---------------------------------------------------------------- |
| `32` and `45`       | SM11AA                      | Simulates verifying the account.                                 |
| `10` and `11`       | SM33CC                      | Simulates exceeding the number of allowed verification attempts. |
| `40` and `41`       | SM44DD                      | Simulates a microdeposit timeout.                                |

### Test settlement behavior

Test transactions settle instantly and are added to your available test balance. This behavior differs from livemode, where transactions can take [multiple days](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md#timing) to settle in your available balance.

## Optional: Access data on a Financial Connections bank account

You can only access Financial Connections data if you request additional [data permissions](https://docs.stripe.com/financial-connections/fundamentals.md#data-permissions) when you create your PaymentIntent .

After your customer successfully completes the Checkout flow, the `us_bank_account` PaymentMethod returned includes a [financial_connections_account](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-us_bank_account-financial_connections_account) ID that points to a [Financial Connections Account](https://docs.stripe.com/api/financial_connections/accounts.md). Use this ID to access account data.

> Bank accounts that your customers link through manual entry and microdeposits don’t have a `financial_connections_account` ID on the Payment Method.

To determine the Financial Connections account ID, retrieve the Checkout Session and expand the `payment_intent.payment_method` attribute:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.retrieve(
  "{{CHECKOUTSESSION_ID}}",
  {
    expand: ["payment_intent.payment_method"],
  },
);
```

```json
{
  "id": "{{CHECKOUT_SESSION_ID}}",
  "object": "checkout.session",
  // ...
  "payment_intent": {
    "id": "{{PAYMENT_INTENT_ID}}",
    "object": "payment_intent",
    // ...
    "payment_method": {
      "id": "{{PAYMENT_METHOD_ID}}",
      // ...
      "type": "us_bank_account",
      "us_bank_account": {
        "account_holder_type": "individual",
        "account_type": "checking",
        "bank_name": "TEST BANK",
        "financial_connections_account": "{{FINANCIAL_CONNECTIONS_ACCOUNT_ID}}",
        "fingerprint": "q9qchffggRjlX2tb",
        "last4": "6789",
        "routing_number": "110000000"
      }
    }
    // ...
  }
}
```

Learn more about using additional account data to optimize your ACH integration with [Financial Connections](https://docs.stripe.com/financial-connections/ach-direct-debit-payments.md#optimize).

## Optional: Resolve disputes [Server-side]

Customers can generally [dispute an ACH Direct Debit payment](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md#resolving-disputes) through their bank for up to 60 calendar days after a debit on a personal account, or up to 2 business days for a business account. In rare instances, a customer might be able to successfully dispute a debit payment outside these standard dispute timelines.

When a customer disputes a payment, Stripe sends a [charge.dispute.closed](https://docs.stripe.com/api/events/types.md#event_types-charge.dispute.closed) webhook event, and the PaymentMethod authorization is revoked.

In rare situations, Stripe might receive an ACH failure from the bank after a PaymentIntent has transitioned to `succeeded`. If this happens, Stripe creates a dispute with a `reason` of:

- `insufficient_funds`
- `incorrect_account_details`
- `bank_can't_process`

Stripe charges a failure fee in this situation.

Future payments reusing this PaymentMethod return the following error:

```javascript
{
  "error": {
    "message": "This PaymentIntent requires a mandate, but no existing mandate was found. Collect mandate acceptance from the customer and try again, providing acceptance data in the mandate_data parameter.",
    "payment_intent": {
      ...
    }
    "type": "invalid_request_error"
  }
}
```

This error contains a PaymentIntent in the `requires_confirmation` state. To continue with the payment, you must:

1. Resolve the dispute with the customer to ensure future payments won’t be disputed.
1. Confirm authorization from your customer again.

To confirm authorization for the payment, you can [collect mandate acknowledgement from your customer online with Stripe.js](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md?platform=web#web-collect-mandate-and-submit) or confirm authorization with your customer offline using the Stripe API.

> If a customer disputes more than one payment from the same bank account, Stripe blocks their bank account. Contact [Stripe Support](https://support.stripe.com/?contact=true) for further resolution.

```curl
curl https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT_ID}}/confirm \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "mandate_data[customer_acceptance][type]=offline"
```

## Optional: Payment Reference

The payment reference number is a bank-generated value that allows the bank account owner to use their bank to locate funds. When the payment succeeds, Stripe provides the payment reference number in the Dashboard and inside the [Charge object](https://docs.stripe.com/api/charges/object.md).

| Charge State | Payment Reference Value                  |
| ------------ | ---------------------------------------- |
| Pending      | Unavailable                              |
| Failed       | Unavailable                              |
| Succeeded    | Available (for example, 091000015001234) |

In addition, when you receive the `charge.succeeded` webhook, view the content of `payment_method_details` to locate the [payment_reference](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-us_bank_account-payment_reference).

The following example event shows the rendering of a successful ACH payment with a payment reference number.

#### charge-succeeded

```json
{
  "id": "{{EVENT_ID}}",
  "object": "event",
  // omitted some fields in the example
  "type": "charge.succeeded",
  "data": {
    "object": {
      "id": "{{PAYMENT_ID}}",
      "object": "charge",
      //...
      "paid": true,
      "payment_intent": "{{PAYMENT_INTENT_ID}}",
      "payment_method": "{{PAYMENT_METHOD_ID}}",
      "payment_method_details": {
        "type": "us_bank_account",
        "us_bank_account": {
          "account_holder_type": "individual",
          "account_type": "checking",
          "bank_name": "TEST BANK",
          "fingerprint": "Ih3foEnRvLXShyfB",
          "last4": "1000",
          "payment_reference": "091000015001234",
          "routing_number": "110000000"
        }
      }
      // ...
    }
  }
}
```

View the contents of the `destination_details` to locate the [refund reference](https://docs.stripe.com/api/refunds/object.md#refund_object-destination_details-us_bank_transfer-reference) associated with the refunded ACH payments.

The following example event shows the rendering of a successful ACH refund with a refund reference number. Learn more about [refunds](https://docs.stripe.com/refunds.md).

#### charge-refund-updated

```json
{
  "id": "{{EVENT_ID}}",
  "object": "event",
  "type": "charge.refund.updated",
  "data": {
    "object": {
      "id": "{{REFUND_ID}}",
      "object": "refund",
      //...
      "payment_intent": "{{PAYMENT_INTENT_ID}}",
      "destination_details": {
        "type": "us_bank_transfer",
        "us_bank_transfer": {
          "reference": "091000015001111",
          "reference_status": "available"
        }
      }
      // ...
    }
  }
}
```

## Optional: Configure customer debit date [Server-side]

You can control the date that Stripe debits a customer’s bank account using the [target date](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-payment_method_options-us_bank_account-target_date). The target date must be at least three days in the future and no more than 15 days from the current date.

The target date schedules money to leave the customer’s account on the target date.

Target dates that meet one of the following criteria delay the debit until the next available business day:

- Target date falls on a weekend, a bank holiday, or other non-business day.
- Target date is fewer than three business days in the future.

This parameter operates on a best-effort basis. Each customer’s bank might process debits on different dates, depending on local bank holidays or other reasons.

> You can’t set the [verification method](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-payment_method_options-us_bank_account-verification_method) to `microdeposits` when using a [target date](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-payment_method_options-us_bank_account-target_date), as the verification process could take longer than the target date, causing payments to arrive later than expected.

# Payment Intents API

> This is a Payment Intents API for when payment-ui is elements and api-integration is paymentintents. View the full page at https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment?payment-ui=elements&api-integration=paymentintents.

To determine which API meets your business needs, see the [comparison guide](https://docs.stripe.com/payments/checkout-sessions-and-payment-intents-comparison.md).

Use the [Payment Element](https://docs.stripe.com/payments/payment-element.md) to embed a custom Stripe payment form in your website or application and offer payment methods to customers. For advanced configurations and customizations, refer to the [Accept a Payment](https://docs.stripe.com/payments/accept-a-payment.md) integration guide.

Before you use ACH direct debit in your Payment Element integration, learn about the following ACH direct debit-specific considerations:

- Learn about [mandate collection](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md#mandate-collection).
- Choose how you [verify bank accounts](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md#bank-verification).

### Mandate collection

When accepting ACH payments, you need to understand mandates.

Unless you use a direct API integration, Stripe handles mandate collection and storage for your business to make sure that regulatory requirements are met. When a customer accepts the mandate during the payment process, Stripe automatically stores this information and it becomes available for you to access from your Dashboard.

## Set up Stripe [Server-side]

To get started, [create a Stripe account](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Collect payment details [Client-side]

Use the Payment Element to collect payment details on the client. The Payment Element is a prebuilt UI component that simplifies collecting payment details for various payment methods.

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

To add the Payment Element to your checkout page, create an empty DOM node (container) with a unique ID in your payment form:

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

You can manage payment methods from the Dashboard or manually list the payment methods you want to be available when you create the [Payment Element](https://docs.stripe.com/js/elements_object/create_without_intent).

#### Manage payment methods from the Dashboard

```javascript
const options = {
  mode: 'payment',
  amount: 1099,
  currency: 'usd',
  // Fully customizable with appearance API.
  appearance: {
    /*...*/
  },
};

// Set up Stripe.js and Elements to use in checkout formconst elements = stripe.elements(options);

// Create and mount the Payment Element
const paymentElementOptions = { layout: "accordion" };
const paymentElement = elements.create("payment", paymentElementOptions);
paymentElement.mount("#payment-element");
```

#### Manually list payment methods

To manually list payment methods, add each one to the `PaymentMethodTypes` attribute in `options` when you create the [Payment Element](https://docs.stripe.com/js/elements_object/create_without_intent).

```javascript
const options = {
  mode: 'payment',
  amount: 1099,
  currency: 'usd',
  paymentMethodTypes: ["us_bank_account"],
  // Fully customizable with appearance API.
  appearance: {
    /*...*/
  },
};

// Set up Stripe.js and Elements to use in checkout formconst elements = stripe.elements(options);

// Create and mount the Payment Element
const paymentElementOptions = { layout: "accordion" };
const paymentElement = elements.create("payment", paymentElementOptions);
paymentElement.mount("#payment-element");
```

#### React

### Set up Stripe.js

Install React Stripe.js and the Stripe.js loader from the [npm public registry](https://www.npmjs.com/package/@stripe/react-stripe-js).

```bash
npm install --save @stripe/react-stripe-js @stripe/stripe-js
```

### Add and configure the Elements provider to your checkout page

To use the Payment Element component, wrap your checkout page component in an [Elements provider](https://docs.stripe.com/sdks/stripejs-react.md#elements-provider). Call `loadStripe` with your publishable key, and pass the returned `Promise` to the `Elements` provider.

You can manage payment methods from the Dashboard or manually list the payment methods you want to be available when you create the [Payment Element](https://docs.stripe.com/js/elements_object/create_without_intent).

#### Manage payment methods from the Dashboard

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
    currency: 'usd',
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

#### Manually list payment methods

To manually list payment methods, add each one to the `payment_method_types` attribute when you create the [Payment Element](https://docs.stripe.com/js/elements_object/create_without_intent).

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
    currency: 'usd',
    paymentMethodTypes: ["us_bank_account"],
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

## Verify bank accounts

#### Item 1

For information on Financial Connections fees, see [pricing details](https://stripe.com/financial-connections#pricing).

Bank account verification uses automatic verification to collect payment information through [Financial Connections](https://docs.stripe.com/financial-connections.md) by default. No changes are required to use it. You can change your [verification_method](https://docs.stripe.com/js/elements_object/create_without_intent#stripe_elements_no_intent-options-paymentMethodOptions-us_bank_account-verification_method) to `instant` to make all users verify their bank accounts with Financial Connections. To learn how to configure Financial Connections and access additional account data, such as checking an account’s balance before initiating a payment, see the [Financial Connections](https://docs.stripe.com/financial-connections.md).

#### Automatic (default)

By default, collecting bank account payment information uses [Financial Connections](https://docs.stripe.com/financial-connections.md) to instantly verify your customer’s account. If instant verification isn’t possible, it falls back to manual account number entry and microdeposit verification.

> To expand access to additional data after a customer authenticates their account, the customer needs to re-link their account with expanded permissions. This authentication occurs one time per customer, and the permission it grants is reusable.

**Microdeposit verification**Not all customers can verify their bank account instantly. This section only applies if your customer has elected to opt out of the instant verification flow in the previous step. In these cases, Stripe sends 1-2 microdeposits to a customer’s bank account for verification instead. These deposits take 1-2 business days to appear on the customer’s online statement.

There are two types of microdeposits:

- **Descriptor code** (default): Stripe sends a 0.01 USD microdeposit to the customer’s bank account with a unique 6-digit `descriptor_code` that starts with SM. Your customer uses this code to verify their bank account.
- **Amount**: Stripe sends two, non-unique microdeposits to the customer’s bank account, with a statement descriptor that reads `ACCTVERIFY`. Your customer uses the deposit amounts to verify their bank account.

**Microdeposit verification failure**When a bank account is pending verification with microdeposits, verification can fail in several ways:

- The microdeposits fail to arrive in the customer’s bank account (this usually indicates a closed or unavailable bank account or incorrect bank account number).
- The customer exceeds the limit of verification attempts for the account. Exceeding this limit means the bank account can no longer be verified or reused.
- The customer didn’t complete verification within 10 days.

#### Instant

You can enforce all of your customers to verify their bank accounts with Financial Connections by using instant verification.

To use instant verification, set the [verification_method](https://docs.stripe.com/js/elements_object/create_without_intent#stripe_elements_no_intent-options-paymentMethodOptions-us_bank_account-verification_method) parameter to `instant` when you create a [Payment Element](https://docs.stripe.com/js/elements_object/create_without_intent).

#### HTML + JS

```js
const options = {
  mode: 'payment',
  amount: 1099,
  currency: 'usd',paymentMethodOptions: {
    us_bank_account: {
      verification_method: "instant"
    }
  }
  appearance: {/*...*/},
};

// Set up Stripe.js and Elements to use in checkout form
const elements = stripe.elements(options);

// Create and mount the Payment Element
const paymentElement = elements.create('payment');
paymentElement.mount('#payment-element');
```

#### React

```jsx
import React from 'react';
import ReactDOM from 'react-dom';
import {Elements} from '@stripe/react-stripe-js';
import {loadStripe} from '@stripe/stripe-js';

import CheckoutForm from './CheckoutForm';

// Make sure to call `loadStripe` outside of a component’s render to avoid
// recreating the `Stripe` object on every render.
const stripePromise = loadStripe('<<YOUR_PUBLISHABLE_KEY>>');

function App() {
  const options = {
    mode: 'payment',
    amount: 1099,
    currency: 'usd',paymentMethodOptions: {
      us_bank_account: {
        verification_method: "instant"
      }
    }
    // Fully customizable with appearance API.
    appearance: {/*...*/},
  };

  return (
    <Elements stripe={stripePromise} options={options}>
      <CheckoutForm />
    </Elements>
  );
};

ReactDOM.render(<App />, document.getElementById('root'));
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

#### Item 2

For information on Financial Connections fees, see [pricing details](https://stripe.com/financial-connections#pricing).

Bank account verification uses automatic verification to collect payment information through [Financial Connections](https://docs.stripe.com/financial-connections.md) by default. No changes are required to use it. You can change your [verification_method](https://docs.stripe.com/js/elements_object/create_without_intent#stripe_elements_no_intent-options-paymentMethodOptions-us_bank_account-verification_method) to `instant` to make all users verify their bank accounts with Financial Connections. To learn how to configure Financial Connections and access additional account data, such as checking an account’s balance before initiating a payment, see the [Financial Connections](https://docs.stripe.com/financial-connections.md).

#### Automatic (default)

By default, collecting bank account payment information uses [Financial Connections](https://docs.stripe.com/financial-connections.md) to instantly verify your customer’s account. If instant verification isn’t possible, it falls back to manual account number entry and microdeposit verification.

> To expand access to additional data after a customer authenticates their account, the customer needs to re-link their account with expanded permissions. This authentication occurs one time per customer, and the permission it grants is reusable.

**Microdeposit verification**Not all customers can verify their bank account instantly. This section only applies if your customer has elected to opt out of the instant verification flow in the previous step. In these cases, Stripe sends 1-2 microdeposits to a customer’s bank account for verification instead. These deposits take 1-2 business days to appear on the customer’s online statement.

There are two types of microdeposits:

- **Descriptor code** (default): Stripe sends a 0.01 USD microdeposit to the customer’s bank account with a unique 6-digit `descriptor_code` that starts with SM. Your customer uses this code to verify their bank account.
- **Amount**: Stripe sends two, non-unique microdeposits to the customer’s bank account, with a statement descriptor that reads `ACCTVERIFY`. Your customer uses the deposit amounts to verify their bank account.

**Microdeposit verification failure**When a bank account is pending verification with microdeposits, verification can fail in several ways:

- The microdeposits fail to arrive in the customer’s bank account (this usually indicates a closed or unavailable bank account or incorrect bank account number).
- The customer exceeds the limit of verification attempts for the account. Exceeding this limit means the bank account can no longer be verified or reused.
- The customer didn’t complete verification within 10 days.

#### Instant

You can enforce all of your customers to verify their bank accounts with Financial Connections by using instant verification.

To use instant verification, set the [verification_method](https://docs.stripe.com/js/elements_object/create_without_intent#stripe_elements_no_intent-options-paymentMethodOptions-us_bank_account-verification_method) parameter to `instant` when you create a [Payment Element](https://docs.stripe.com/js/elements_object/create_without_intent).

#### HTML + JS

```js
const options = {
  mode: 'payment',
  amount: 1099,
  payment_method_types: ['card', 'us_bank_account'],
  currency: 'usd',paymentMethodOptions: {
    us_bank_account: {
      verification_method: "instant"
    }
  }
  appearance: {/*...*/},
};

// Set up Stripe.js and Elements to use in checkout form
const elements = stripe.elements(options);

// Create and mount the Payment Element
const paymentElement = elements.create('payment');
paymentElement.mount('#payment-element');
```

#### React

```jsx
import React from 'react';
import ReactDOM from 'react-dom';
import {Elements} from '@stripe/react-stripe-js';
import {loadStripe} from '@stripe/stripe-js';

import CheckoutForm from './CheckoutForm';

// Make sure to call `loadStripe` outside of a component’s render to avoid
// recreating the `Stripe` object on every render.
const stripePromise = loadStripe('<<YOUR_PUBLISHABLE_KEY>>');

function App() {
  const options = {
    mode: 'payment',
    amount: 1099,
    currency: 'usd',
    payment_method_types: `us_bank_account`,paymentMethodOptions: {
      us_bank_account: {
        verification_method: "instant"
      }
    }
    // Fully customizable with appearance API.
    appearance: {/*...*/},
  };

  return (
    <Elements stripe={stripePromise} options={options}>
      <CheckoutForm />
    </Elements>
  );
};

ReactDOM.render(<App />, document.getElementById('root'));
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

## Create a PaymentIntent [Server-side]

> #### Run custom business logic immediately before payment confirmation
>
> Navigate to [step 5](https://docs.stripe.com/payments/finalize-payments-on-the-server.md?platform=web&type=payment#submit-payment) in the finalize payments guide to run your custom business logic immediately before payment confirmation. Otherwise, follow the steps below for a simpler integration, which uses `stripe.confirmPayment` on the client to both confirm the payment and handle any next actions.

#### Control payment methods from the Dashboard

When the customer submits your payment form, use a _PaymentIntent_ (The Payment Intents API tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by regulatory mandates, custom Radar fraud rules, or redirect-based payment methods) to facilitate the confirmation and payment process. Create a PaymentIntent on your server with an `amount` and `currency`. To prevent malicious customers from choosing their own prices, always decide how much to charge on the server-side (a trusted environment) and not the client.

A `PaymentIntent` includes a _client secret_ (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)). Return this value to your client for Stripe.js to use to securely complete the payment process.

#### Accounts v2

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');
const express = require("express");
const app = express();

app.use(express.static("."));

app.post("/create-intent", async (req, res) => {
  const intent = await stripe.paymentIntents.create({
    // To allow saving and retrieving payment methods, provide the customer's Account ID.
    customer_account: "{{CUSTOMER_ACCOUNT_ID}}",
    amount: 1099,
    currency: 'usd',
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
const express = require("express");
const app = express();

app.use(express.static("."));

app.post("/create-intent", async (req, res) => {
  const intent = await stripe.paymentIntents.create({
    // To allow saving and retrieving payment methods, provide the Customer ID.
    customer: customer.id,
    amount: 1099,
    currency: 'usd',
  });
  res.json({ client_secret: intent.client_secret });
});

app.listen(3000, () => {
  console.log("Running on port 3000");
});
```

#### List payment methods manually

When the customer submits your payment form, use a _PaymentIntent_ (The Payment Intents API tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by regulatory mandates, custom Radar fraud rules, or redirect-based payment methods) to facilitate the confirmation and payment process. Create a PaymentIntent on your server with an `amount`, `currency`, and one or more payment methods using `payment_method_types`. To prevent malicious customers from choosing their own prices, always decide how much to charge on the server-side (a trusted environment) and not the client.

Included on a PaymentIntent is a _client secret_ (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)). Return this value to your client for Stripe.js to use to securely complete the payment process.

#### Accounts v2

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');
const express = require("express");
const app = express();

app.use(express.static("."));

app.post("/create-intent", async (req, res) => {
  const intent = await stripe.paymentIntents.create({
    // To allow saving and retrieving payment methods, provide the customer's Account ID.
    customer_account: customer_account.id,
    amount: 1099,
    currency: 'usd',
    payment_method_types: ['us_bank_account'],
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
const express = require("express");
const app = express();

app.use(express.static("."));

app.post("/create-intent", async (req, res) => {
  const intent = await stripe.paymentIntents.create({
    // To allow saving and retrieving payment methods, provide the Customer ID.
    customer: customer.id,
    amount: 1099,
    currency: 'usd',
    payment_method_types: ['us_bank_account'],
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
const form = document.getElementById("payment-form");
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
    method: "POST",
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
      method: "POST",
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

## Optional: Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

- **Handle events manually in the Dashboard**

  Use the Dashboard to [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments), send email receipts, handle payouts, or retry failed payments.

- **Build a custom webhook**

  [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook) handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- **Integrate a prebuilt app**

  Handle common business events, such as [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

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

Test transactions settle instantly and are added to your available test balance. This behavior differs from livemode, where transactions can take [multiple days](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md#timing) to settle in your available balance.

## Error codes

The following table details common error codes and recommended actions:

| Error code                                                | Recommended action                                                                                                                                                                                                                                                                                                                                                |
| --------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_intent_invalid_currency`                         | Enter a supported currency.                                                                                                                                                                                                                                                                                                                                       |
| `missing_required_parameter`                              | Check the error message for more information about the required parameter.                                                                                                                                                                                                                                                                                        |
| `payment_intent_payment_attempt_failed`                   | This code can appear in the [last_payment_error.code](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-last_payment_error-code) field of a PaymentIntent. Check the error message for a detailed failure reason and suggestion on error handling.                                                                                      |
| `payment_intent_authentication_failure`                   | This code can appear in the [last_payment_error.code](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-last_payment_error-code) field of a PaymentIntent. Check the error message for a detailed failure reason and suggestion on error handling. This error occurs when you manually trigger a failure when testing your integration. |
| `payment_intent_redirect_confirmation_without_return_url` | Provide a `return_url` when confirming a PaymentIntent.                                                                                                                                                                                                                                                                                                           |

## Optional: Access data on a Financial Connections bank account

For more information on Financial Connections fees, see [pricing details](https://stripe.com/financial-connections#pricing).

You can only access [Financial Connections](https://docs.stripe.com/financial-connections.md) data if you request additional [data permissions](https://docs.stripe.com/financial-connections/fundamentals.md#data-permissions) when you create your Payment Intent.

After your customer successfully completes the [Stripe Financial Connections authentication flow](https://docs.stripe.com/financial-connections/fundamentals.md#authentication-flow), the `us_bank_account` PaymentMethod returned includes a [financial_connections_account](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-us_bank_account-financial_connections_account) ID that points to a [Financial Connections Account](https://docs.stripe.com/api/financial_connections/accounts.md). Use this ID to access account data.

> Bank accounts that your customers link through manual entry and microdeposits don’t have a `financial_connections_account` ID on the payment method.

To determine the Financial Connections account ID, retrieve the Payment Intent and expand the `payment_intent.payment_method` attribute:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.retrieve(
  "{{PAYMENTINTENT_ID}}",
  {
    expand: ["payment_method"],
  },
);
```

```json
{
  "payment_intent": {
    "id": "{{PAYMENT_INTENT_ID}}",
    "object": "payment_intent",
    // ...
    "payment_method": {
      "id": "{{PAYMENT_METHOD_ID}}",
      // ...
      "type": "us_bank_account",
      "us_bank_account": {
        "account_holder_type": "individual",
        "account_type": "checking",
        "bank_name": "TEST BANK",
        "financial_connections_account": "{{FINANCIAL_CONNECTIONS_ACCOUNT_ID}}",
        "fingerprint": "q9qchffggRjlX2tb",
        "last4": "6789",
        "routing_number": "110000000"
      }
    }
    // ...
  }
}
```

## Optional: Resolve disputes [Server-side]

Customers can generally [dispute an ACH Direct Debit payment](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md#resolving-disputes) through their bank for up to 60 calendar days after a debit on a personal account, or up to 2 business days for a business account. In rare instances, a customer might be able to successfully dispute a debit payment outside these standard dispute timelines.

When a customer disputes a payment, Stripe sends a [charge.dispute.closed](https://docs.stripe.com/api/events/types.md#event_types-charge.dispute.closed) webhook event, and the PaymentMethod authorization is revoked.

In rare situations, Stripe might receive an ACH failure from the bank after a PaymentIntent has transitioned to `succeeded`. If this happens, Stripe creates a dispute with a `reason` of:

- `insufficient_funds`
- `incorrect_account_details`
- `bank_can't_process`

Stripe charges a failure fee in this situation.

Future payments reusing this PaymentMethod return the following error:

```javascript
{
  "error": {
    "message": "This PaymentIntent requires a mandate, but no existing mandate was found. Collect mandate acceptance from the customer and try again, providing acceptance data in the mandate_data parameter.",
    "payment_intent": {
      ...
    }
    "type": "invalid_request_error"
  }
}
```

This error contains a PaymentIntent in the `requires_confirmation` state. To continue with the payment, you must:

1. Resolve the dispute with the customer to ensure future payments won’t be disputed.
1. Confirm authorization from your customer again.

To confirm authorization for the payment, you can [collect mandate acknowledgement from your customer online with Stripe.js](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md?platform=web#web-collect-mandate-and-submit) or confirm authorization with your customer offline using the Stripe API.

> If a customer disputes more than one payment from the same bank account, Stripe blocks their bank account. Contact [Stripe Support](https://support.stripe.com/?contact=true) for further resolution.

```curl
curl https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT_ID}}/confirm \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "mandate_data[customer_acceptance][type]=offline"
```

## Optional: Payment Reference

The payment reference number is a bank-generated value that allows the bank account owner to use their bank to locate funds. When the payment succeeds, Stripe provides the payment reference number in the Dashboard and inside the [Charge object](https://docs.stripe.com/api/charges/object.md).

| Charge State | Payment Reference Value                  |
| ------------ | ---------------------------------------- |
| Pending      | Unavailable                              |
| Failed       | Unavailable                              |
| Succeeded    | Available (for example, 091000015001234) |

In addition, when you receive the `charge.succeeded` webhook, view the content of `payment_method_details` to locate the [payment_reference](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-us_bank_account-payment_reference).

The following example event shows the rendering of a successful ACH payment with a payment reference number.

#### charge-succeeded

```json
{
  "id": "{{EVENT_ID}}",
  "object": "event",
  // omitted some fields in the example
  "type": "charge.succeeded",
  "data": {
    "object": {
      "id": "{{PAYMENT_ID}}",
      "object": "charge",
      //...
      "paid": true,
      "payment_intent": "{{PAYMENT_INTENT_ID}}",
      "payment_method": "{{PAYMENT_METHOD_ID}}",
      "payment_method_details": {
        "type": "us_bank_account",
        "us_bank_account": {
          "account_holder_type": "individual",
          "account_type": "checking",
          "bank_name": "TEST BANK",
          "fingerprint": "Ih3foEnRvLXShyfB",
          "last4": "1000",
          "payment_reference": "091000015001234",
          "routing_number": "110000000"
        }
      }
      // ...
    }
  }
}
```

View the contents of the `destination_details` to locate the [refund reference](https://docs.stripe.com/api/refunds/object.md#refund_object-destination_details-us_bank_transfer-reference) associated with the refunded ACH payments.

The following example event shows the rendering of a successful ACH refund with a refund reference number. Learn more about [refunds](https://docs.stripe.com/refunds.md).

#### charge-refund-updated

```json
{
  "id": "{{EVENT_ID}}",
  "object": "event",
  "type": "charge.refund.updated",
  "data": {
    "object": {
      "id": "{{REFUND_ID}}",
      "object": "refund",
      //...
      "payment_intent": "{{PAYMENT_INTENT_ID}}",
      "destination_details": {
        "type": "us_bank_transfer",
        "us_bank_transfer": {
          "reference": "091000015001111",
          "reference_status": "available"
        }
      }
      // ...
    }
  }
}
```

## Optional: Configure customer debit date [Server-side]

You can control the date that Stripe debits a customer’s bank account using the [target date](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-payment_method_options-us_bank_account-target_date). The target date must be at least three days in the future and no more than 15 days from the current date.

The target date schedules money to leave the customer’s account on the target date. You can [cancel a PaymentIntent](https://docs.stripe.com/api/payment_intents/cancel.md) created with a target date up to three business days before the configured date.

Target dates that meet one of the following criteria delay the debit until next available business day:

- Target date falls on a weekend, a bank holiday, or other non-business day.
- Target date is fewer than three business days in the future.

This parameter operates on a best-effort basis. Each customer’s bank might process debits on different dates, depending on local bank holidays or other reasons.

> You can’t set the [verification method](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-payment_method_options-us_bank_account-verification_method) to `microdeposits` when using a [target date](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-payment_method_options-us_bank_account-target_date), as the verification process could take longer than the target date, causing payments to arrive later than expected.

# Direct API

> This is a Direct API for when payment-ui is direct-api. View the full page at https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment?payment-ui=direct-api.

Accepting ACH Direct Debit payments on your website consists of:

- Creating an object to track a payment
- Collecting payment method information with instant verifications enabled by [Stripe Financial Connections](https://docs.stripe.com/financial-connections.md)
- Submitting the payment to Stripe for processing
- Verifying your customer’s bank account

ACH Direct Debit is a [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method, which means that funds aren’t immediately available after payment. A payment typically takes 4 business days to arrive in your account.

Stripe uses the payment object, the [Payment Intent](https://docs.stripe.com/payments/payment-intents.md), to track and handle all the states of the payment until the payment completes.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

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
  contact_email: '{{CUSTOMER_EMAIL}}',
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

## Create a PaymentIntent [Server-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) is an object that represents your intent to collect payment from a customer and tracks the lifecycle of the payment process through each stage.

Create a PaymentIntent on your server and specify the amount to collect and the `usd` currency. If you already have an integration using the Payment Intents API, add `us_bank_account` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your PaymentIntent. Specify the customer’s ID.

If you want to reuse the payment method in the future, provide the [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) parameter with the value of `off_session`.

For more information on Financial Connections fees, see [pricing details](https://stripe.com/financial-connections#pricing).

By default, collecting bank account payment information uses [Financial Connections](https://docs.stripe.com/financial-connections.md) to instantly verify your customer’s account, with a fallback option of manual account number entry and microdeposit verification. See the [Financial Connections docs](https://docs.stripe.com/financial-connections/ach-direct-debit-payments.md) to learn how to configure Financial Connections and access additional account data to optimize your ACH integration. For example, you can use Financial Connections to check an account’s balance before initiating the ACH payment.

> To expand access to additional data after a customer authenticates their account, they must re-link their account with expanded permissions.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'usd',
  setup_future_usage: "off_session",
  customer_account: '{{CUSTOMERACCOUNT_ID}}',
  payment_method_types: ['us_bank_account'],
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'usd',
  setup_future_usage: "off_session",
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['us_bank_account'],
});
```

### Retrieve the client secret

The PaymentIntent includes a _client secret_ (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)) that the client side uses to securely complete the payment process. You can use different approaches to pass the client secret to the client side.

#### Single-page application

Retrieve the client secret from an endpoint on your server, using the browser’s `fetch` function. This approach is best if your client side is a single-page application, particularly one built with a modern frontend framework like React. Create the server endpoint that serves the client secret:

#### Node.js

```javascript
const express = require("express");
const app = express();

app.get("/secret", async (req, res) => {
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
  const response = await fetch("/secret");
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
const express = require("express");
const expressHandlebars = require("express-handlebars");
const app = express();

app.engine(".hbs", expressHandlebars({ extname: ".hbs" }));
app.set("view engine", ".hbs");
app.set("views", "./views");

app.get("/checkout", async (req, res) => {
  const intent = // ... Fetch or create the PaymentIntent
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

Rather than sending the entire PaymentIntent object to the client, use its _client secret_ (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)) from the previous step. This is different from your API keys that authenticate Stripe API requests.

Handle the client secret carefully because it can complete the charge. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

Use [stripe.collectBankAccountForPayment](https://docs.stripe.com/js/payment_intents/collect_bank_account_for_payment) to collect bank account details with [Financial Connections](https://docs.stripe.com/financial-connections.md), create a _PaymentMethod_ (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs), and attach that PaymentMethod to the PaymentIntent. Including the account holder’s name in the `billing_details` parameter is required to create an ACH Direct Debit PaymentMethod.

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
    .collectBankAccountForPayment({
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
    .then(({ paymentIntent, error }) => {
      if (error) {
        console.error(error.message);
        // PaymentMethod collection failed for some reason.
      } else if (paymentIntent.status === "requires_payment_method") {
        // Customer canceled the hosted verification modal. Present them with other
        // payment method type options.
      } else if (paymentIntent.status === "requires_confirmation") {
        // We collected an account - possibly instantly verified, but possibly
        // manually-entered. Display payment method details and mandate text
        // to the customer and confirm the intent once they accept
        // the mandate.
        confirmationForm.show();
      }
    });
});
```

The [Financial Connections authentication flow](https://docs.stripe.com/financial-connections/fundamentals.md#authentication-flow) automatically handles bank account details collection and verification. When your customer completes the authentication flow, the _PaymentMethod_ (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) automatically attaches to the PaymentIntent, and creates a [Financial Connections Account](https://docs.stripe.com/api/financial_connections/accounts.md).

> Bank accounts that your customers link through manual entry and microdeposits won’t have access to additional bank account data like balances, ownership, and transactions.

To provide the best user experience on all devices, set the viewport `minimum-scale` for your page to 1 using the viewport `meta` tag.

```html
<meta name="viewport" content="width=device-width, minimum-scale=1" />
```

## Optional: Access data on a Financial Connections bank account [Server-side]

You can only access Financial Connections data if you request additional [data permissions](https://docs.stripe.com/financial-connections/fundamentals.md#data-permissions) when you create your PaymentIntent .

After your customer successfully completes the [Stripe Financial Connections authentication flow](https://docs.stripe.com/financial-connections/fundamentals.md#authentication-flow), the `us_bank_account` PaymentMethod returned includes a [financial_connections_account](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-us_bank_account-financial_connections_account) ID that points to a [Financial Connections Account](https://docs.stripe.com/api/financial_connections/accounts.md). Use this ID to access account data.

> Bank accounts that your customers link through manual entry and microdeposits don’t have a `financial_connections_account` ID on the Payment Method.

To determine the Financial Connections account ID, retrieve the PaymentIntent and expand the `payment_method` attribute:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.retrieve(
  "{{PAYMENTINTENT_ID}}",
  {
    expand: ["payment_method"],
  },
);
```

```json
{
  "id": "{{PAYMENT_INTENT_ID}}",
  "object": "payment_intent",
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

If you opted to receive `balances` permissions, we recommend checking a balance at this stage to verify sufficient funds before confirming a payment.

Learn more about using additional account data to optimize your ACH integration with [Financial Connections](https://docs.stripe.com/financial-connections/ach-direct-debit-payments.md#optimize).

## Collect mandate acknowledgement and submit the payment [Client-side]

Before you can initiate the payment, you must obtain authorization from your customer by displaying mandate terms for them to accept.

To be compliant with Nacha rules, you must obtain authorization from your customer before you can initiate payment by displaying mandate terms for them to accept. For more information on mandates, see [Mandates](https://docs.stripe.com/payments/ach-direct-debit.md#mandates).

When the customer accepts the mandate terms, you must confirm the PaymentIntent. Use [stripe.confirmUsBankAccountPayment](https://docs.stripe.com/js/payment_intents/confirm_us_bank_account_payment) to complete the payment when the customer submits the form.

```javascript
confirmationForm.addEventListener("submit", (ev) => {
  ev.preventDefault();
  stripe
    .confirmUsBankAccountPayment(clientSecret)
    .then(({ paymentIntent, error }) => {
      if (error) {
        console.error(error.message);
        // The payment failed for some reason.
      } else if (paymentIntent.status === "requires_payment_method") {
        // Confirmation failed. Attempt again with a different payment method.
      } else if (paymentIntent.status === "processing") {
        // Confirmation succeeded! The account will be debited.
        // Display a message to customer.
      } else if (
        paymentIntent.next_action?.type === "verify_with_microdeposits"
      ) {
        // The account needs to be verified through microdeposits.
        // Display a message to consumer with next steps (consumer waits for
        // microdeposits, then enters a statement descriptor code on a page sent to them through email).
      }
    });
});
```

> [stripe.confirmUsBankAccountPayment](https://docs.stripe.com/js/payment_intents/confirm_us_bank_account_payment) might take several seconds to complete. During that time, disable resubmittals of your form and show a waiting indicator (for example, a spinner). If you receive an error, show it to the customer, re-enable the form, and hide the waiting indicator.

If successful, Stripe returns a PaymentIntent object, with one of the following possible statuses:

| Status            | Description                                                              | Next Steps                                                                                                                                                |
| ----------------- | ------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `requires_action` | Further action is needed to complete bank account verification.          | Step 6: [Verifying bank accounts with microdeposits](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md#web-verify-with-microdeposits) |
| `processing`      | The bank account was instantly verified or verification isn’t necessary. | Step 7: [Confirm the PaymentIntent succeeded](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md#web-confirm-paymentintent-succeeded)  |

After successfully confirming the PaymentIntent, an email confirmation of the mandate and collected bank account details must be sent to your customer. Stripe handles these by default, but you can choose to [send custom notifications](https://docs.stripe.com/payments/ach-direct-debit.md#mandate-and-microdeposit-emails) if you prefer.

## Verify bank account with microdeposits [Client-side]

Not all customers can verify the bank account instantly. This step only applies if your customer has elected to opt out of the instant verification flow in the previous step.

In these cases, Stripe sends a `descriptor_code` microdeposit and might fall back to an `amount` microdeposit if any further issues arise with verifying the bank account. These deposits take 1-2 business days to appear on the customer’s online statement.

- **Descriptor code**. Stripe sends a single, 0.01 USD microdeposit to the customer’s bank account with a unique, 6-digit `descriptor_code` that starts with SM. Your customer uses this string to verify their bank account.
- **Amount**. Stripe sends two, non-unique microdeposits to the customer’s bank account, with a statement descriptor that reads `ACCTVERIFY`. Your customer uses the deposit amounts to verify their bank account.

The result of the [stripe.confirmUsBankAccountPayment](https://docs.stripe.com/js/payment_intents/confirm_us_bank_account_payment) method call in the previous step is a PaymentIntent in the `requires_action` state. The PaymentIntent contains a `next_action` field that contains some useful information for completing the verification.

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

> Verification attempts have a limit of ten failures for descriptor-based microdeposits and three for amount-based ones. If you exceed this limit, we can no longer verify the bank account. In addition, microdeposit verifications have a timeout of 10 days. If you can’t verify microdeposits in that time, the PaymentIntent reverts to requiring new payment method details. Clear messaging about what these microdeposits are and how you use them can help your customers avoid verification issues.

### Optional: Send custom email notifications

Optionally, you can send [custom email notifications](https://docs.stripe.com/payments/ach-direct-debit.md#mandate-and-microdeposit-emails) to your customer. After you set up custom emails, you need to specify how the customer responds to the verification email. To do so, choose _one_ of the following:

- Use the Stripe-hosted verification page. To do this, use the `verify_with_microdeposits[hosted_verification_url]` URL in the [next_action](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-verify_with_microdeposits-hosted_verification_url) object to direct your customer to complete the verification process.

- If you prefer not to use the Stripe-hosted verification page, create a form on your site. Your customers then use this form to relay microdeposit amounts to you and verify the bank account using [Stripe.js](https://docs.stripe.com/js/payment_intents/verify_microdeposits_for_payment).
  - At minimum, set up the form to handle the `descriptor code` parameter, which is a 6-digit string for verification purposes.
  - Stripe also recommends that you set your form to handle the `amounts` parameter, as some banks your customers use might require it.

  Integrations only pass in the `descriptor_code` _or_ `amounts`. To determine which one your integration uses, check the value for `verify_with_microdeposits[microdeposit_type]` in the `next_action` object.

```javascript
stripe.verifyMicrodepositsForPayment(clientSecret, {
  // Provide either a descriptor_code OR amounts, not both
  descriptor_code: "SMT86W",
  amounts: [32, 45],
});
```

When the bank account is successfully verified, Stripe returns the PaymentIntent object with a `status` of `processing`, and sends a [payment_intent.processing](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.processing) _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event.

Verification can fail for several reasons. The failure might happen synchronously as a direct error response, or asynchronously through a [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.failed) webhook event (shown in the following examples).

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
      "message": "You have exceeded the number of allowed verification attempts.",
    },
    ...
    "status": "requires_payment_method"
  }
}
```

| Error Code                                                   | Synchronous or Asynchronous                            | Message                                                                                                                                         | Status change                                                           |
| ------------------------------------------------------------ | ------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `payment_method_microdeposit_failed`                         | Synchronously, or asynchronously through webhook event | Microdeposits failed. Please check the account, institution and transit numbers provided                                                        | `status` is `requires_payment_method`, and `last_payment_error` is set. |
| `payment_method_microdeposit_verification_amounts_mismatch`  | Synchronously                                          | The amounts provided don’t match the amounts that were sent to the bank account. You have {attempts_remaining} verification attempts remaining. | Unchanged                                                               |
| `payment_method_microdeposit_verification_attempts_exceeded` | Synchronously, or asynchronously through webhook event | Exceeded number of allowed verification attempts                                                                                                | `status` is `requires_payment_method`, and `last_payment_error` is set. |
| `payment_method_microdeposit_verification_timeout`           | Asynchronously through webhook event                   | Microdeposit timeout. Customer hasn’t verified their bank account within the required 10 day period.                                            | `status` is `requires_payment_method`, and `last_payment_error` is set. |

## Confirm the PaymentIntent succeeded [Server-side]

ACH Direct Debit is a [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method. This means that it can take up to four business days to receive notification of the success or failure of a payment after you initiate a debit from your customer’s account.

The PaymentIntent you create initially has a status of `processing`. After the payment has succeeded, the PaymentIntent status is updated from `processing` to `succeeded`.

We recommend using [webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks) to _confirm_ (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) the charge has succeeded and to notify the customer that the payment is complete. You can also view events on the [Stripe Dashboard](https://dashboard.stripe.com/events).

#### PaymentIntent events

The following events are sent when the PaymentIntent status is updated:

| Event                           | Description                                                                                     | Next Step                                                                                                                                                                                                                                                                                     |
| ------------------------------- | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_intent.processing`     | The customer’s payment was submitted to Stripe successfully.                                    | Wait for the initiated payment to succeed or fail.                                                                                                                                                                                                                                            |
| `payment_intent.succeeded`      | The customer’s payment succeeded.                                                               | Fulfill the goods or services that were purchased.                                                                                                                                                                                                                                            |
| `payment_intent.payment_failed` | The customer’s payment was declined. This can also apply to a failed microdeposit verification. | Contact the customer through email or push notification and request another payment method. If the webhook was sent due to a failed microdeposit verification, the user needs to enter in their bank account details again and a new set of microdeposits will be deposited in their account. |

#### Charge events

You may also use additional Charge webhooks to track the payment’s status. Upon receiving the `charge.updated` webhook, the payment is no longer cancellable.

The following events are sent when the Charge status is updated:

| Event              | Description                                                                                                                                     | Next Step                                                                         |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `charge.pending`   | The customer’s payment was created successfully.                                                                                                | Wait for the initiated payment to be processed.                                   |
| `charge.updated`   | The customer’s payment was updated. It can be emitted when a new balance transaction was created, a charge description or metadata got updated. | Wait for the initiated payment to succeed or fail.                                |
| `charge.succeeded` | The customer’s payment succeeded and the funds are available in your balance.                                                                   | Fulfill the goods or services that were purchased.                                |
| `charge.failed`    | The customer’s payment failed.                                                                                                                  | Check the charge’s failure_code and failure_message to determine further actions. |

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

Test transactions settle instantly and are added to your available test balance. This behavior differs from livemode, where transactions can take [multiple days](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md#timing) to settle in your available balance.

## Optional: Instant only verification [Server-side]

By default, US bank account payments allows your customers to use instant bank account verification or microdeposits. You can optionally require instant bank account verification only, using the [verification_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-us_bank_account-verification_method) parameter when you create the PaymentIntent.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'usd',
  setup_future_usage: "off_session",
  customer_account: '{{CUSTOMERACCOUNT_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      verification_method: 'instant',
      financial_connections: {
        permissions: ["payment_method", "balances"],
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
  currency: 'usd',
  setup_future_usage: "off_session",
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      verification_method: 'instant',
      financial_connections: {
        permissions: ["payment_method", "balances"],
      },
    },
  },
});
```

This ensures that you don’t need to handle microdeposit verification. However, if instant verification fails, the PaymentIntent’s status is `requires_payment_method`, indicating a failure to instantly verify a bank account for your customer.

## Optional: Microdeposit only verification [Server-side]

By default, US bank account payments allow your customers to use instant bank account verification or microdeposits. You can optionally require microdeposit verification only using the [verification_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-us_bank_account-verification_method) parameter when you create the PaymentIntent.

> If using a custom payment form, you must build your own UI to collect bank account details. If you disable Stripe microdeposit emails, you must build your own UI for your customer to confirm the microdeposit code or amount.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'usd',
  setup_future_usage: "off_session",
  customer_account: '{{CUSTOMERACCOUNT_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      verification_method: "microdeposits",
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
  currency: 'usd',
  setup_future_usage: "off_session",
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      verification_method: "microdeposits",
    },
  },
});
```

You must then collect your customer’s bank account with your own form and call [stripe.confirmUsBankAccountPayment](https://docs.stripe.com/js/payment_intents/confirm_us_bank_account_payment) with those details to complete the PaymentIntent.

```javascript
var form = document.getElementById("payment-form");
var accountholderName = document.getElementById("accountholder-name");
var email = document.getElementById("email");
var accountNumber = document.getElementById("account-number");
var routingNumber = document.getElementById("routing-number");
var accountHolderType = document.getElementById("account-holder-type");

var submitButton = document.getElementById("submit-button");
var clientSecret = submitButton.dataset.secret;

form.addEventListener("submit", function (event) {
  event.preventDefault();

  stripe
    .confirmUsBankAccountPayment(clientSecret, {
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
    .then(({ paymentIntent, error }) => {
      if (error) {
        // Inform the customer that there was an error.
        console.log(error.message);
      } else {
        // Handle next step based on the intent's status.
        console.log("PaymentIntent ID: " + paymentIntent.id);
        console.log("PaymentIntent status: " + paymentIntent.status);
      }
    });
});
```

## Optional: Resolve disputes [Server-side]

Customers can generally [dispute an ACH Direct Debit payment](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md#resolving-disputes) through their bank for up to 60 calendar days after a debit on a personal account, or up to 2 business days for a business account. In rare instances, a customer might be able to successfully dispute a debit payment outside these standard dispute timelines.

When a customer disputes a payment, Stripe sends a [charge.dispute.closed](https://docs.stripe.com/api/events/types.md#event_types-charge.dispute.closed) webhook event, and the PaymentMethod authorization is revoked.

In rare situations, Stripe might receive an ACH failure from the bank after a PaymentIntent has transitioned to `succeeded`. If this happens, Stripe creates a dispute with a `reason` of:

- `insufficient_funds`
- `incorrect_account_details`
- `bank_can't_process`

Stripe charges a failure fee in this situation.

Future payments reusing this PaymentMethod return the following error:

```javascript
{
  "error": {
    "message": "This PaymentIntent requires a mandate, but no existing mandate was found. Collect mandate acceptance from the customer and try again, providing acceptance data in the mandate_data parameter.",
    "payment_intent": {
      ...
    }
    "type": "invalid_request_error"
  }
}
```

This error contains a PaymentIntent in the `requires_confirmation` state. To continue with the payment, you must:

1. Resolve the dispute with the customer to ensure future payments won’t be disputed.
1. Confirm authorization from your customer again.

To confirm authorization for the payment, you can [collect mandate acknowledgement from your customer online with Stripe.js](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md?platform=web#web-collect-mandate-and-submit) or confirm authorization with your customer offline using the Stripe API.

> If a customer disputes more than one payment from the same bank account, Stripe blocks their bank account. Contact [Stripe Support](https://support.stripe.com/?contact=true) for further resolution.

```curl
curl https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT_ID}}/confirm \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "mandate_data[customer_acceptance][type]=offline"
```

## Optional: Payment Reference

The payment reference number is a bank-generated value that allows the bank account owner to use their bank to locate funds. When the payment succeeds, Stripe provides the payment reference number in the Dashboard and inside the [Charge object](https://docs.stripe.com/api/charges/object.md).

| Charge State | Payment Reference Value                  |
| ------------ | ---------------------------------------- |
| Pending      | Unavailable                              |
| Failed       | Unavailable                              |
| Succeeded    | Available (for example, 091000015001234) |

In addition, when you receive the `charge.succeeded` webhook, view the content of `payment_method_details` to locate the [payment_reference](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-us_bank_account-payment_reference).

The following example event shows the rendering of a successful ACH payment with a payment reference number.

#### charge-succeeded

```json
{
  "id": "{{EVENT_ID}}",
  "object": "event",
  // omitted some fields in the example
  "type": "charge.succeeded",
  "data": {
    "object": {
      "id": "{{PAYMENT_ID}}",
      "object": "charge",
      //...
      "paid": true,
      "payment_intent": "{{PAYMENT_INTENT_ID}}",
      "payment_method": "{{PAYMENT_METHOD_ID}}",
      "payment_method_details": {
        "type": "us_bank_account",
        "us_bank_account": {
          "account_holder_type": "individual",
          "account_type": "checking",
          "bank_name": "TEST BANK",
          "fingerprint": "Ih3foEnRvLXShyfB",
          "last4": "1000",
          "payment_reference": "091000015001234",
          "routing_number": "110000000"
        }
      }
      // ...
    }
  }
}
```

View the contents of the `destination_details` to locate the [refund reference](https://docs.stripe.com/api/refunds/object.md#refund_object-destination_details-us_bank_transfer-reference) associated with the refunded ACH payments.

The following example event shows the rendering of a successful ACH refund with a refund reference number. Learn more about [refunds](https://docs.stripe.com/refunds.md).

#### charge-refund-updated

```json
{
  "id": "{{EVENT_ID}}",
  "object": "event",
  "type": "charge.refund.updated",
  "data": {
    "object": {
      "id": "{{REFUND_ID}}",
      "object": "refund",
      //...
      "payment_intent": "{{PAYMENT_INTENT_ID}}",
      "destination_details": {
        "type": "us_bank_transfer",
        "us_bank_transfer": {
          "reference": "091000015001111",
          "reference_status": "available"
        }
      }
      // ...
    }
  }
}
```

## Optional: Configure customer debit date [Server-side]

You can control the date that Stripe debits a customer’s bank account using the [target date](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-payment_method_options-us_bank_account-target_date). The target date must be at least three days in the future and no more than 15 days from the current date.

The target date schedules money to leave the customer’s account on the target date. You can [cancel a PaymentIntent](https://docs.stripe.com/api/payment_intents/cancel.md) created with a target date up to three business days before the configured date.

Target dates that meet one of the following criteria delay the debit until next available business day:

- Target date falls on a weekend, a bank holiday, or other non-business day.
- Target date is fewer than three business days in the future.

This parameter operates on a best-effort basis. Each customer’s bank might process debits on different dates, depending on local bank holidays or other reasons.

## See also

- [Save ACH Direct Debit pre-authorized debit details for future payments](https://docs.stripe.com/payments/ach-direct-debit/set-up-payment.md)

# iOS

> This is a iOS for when payment-ui is mobile and platform is ios. View the full page at https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment?payment-ui=mobile&platform=ios.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

Accepting ACH Direct Debit payments in your app consists of:

- Creating an object to track a payment
- Collecting payment method information with instant verifications enabled by [Stripe Financial Connections](https://docs.stripe.com/financial-connections.md)
- Submitting the payment to Stripe for processing
- Verifying your customer’s bank account

> ACH Direct Debit is a [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method, which means that funds aren’t immediately available after payment. A payment typically takes 4 business days to arrive in your account.

Stripe uses the payment object, the [Payment Intent](https://docs.stripe.com/payments/payment-intents.md), to track and handle all the states of the payment until the payment completes.

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

With Stripe, you can instantly verify a customer’s bank account. If you want to retrieve additional data on an account, [sign up for data access](https://dashboard.stripe.com/financial-connections/application) with [Stripe Financial Connections](https://docs.stripe.com/financial-connections.md).

Stripe Financial Connections lets your customers securely share their financial data by linking their financial accounts to your business. Use Financial Connections to access customer-permissioned financial data such as tokenized account and routing numbers, balance data, ownership details, and transaction data.

Access to this data helps you perform actions like check balances before initiating a payment to reduce the chance of a failed payment because of insufficient funds.

Financial Connections enables your users to connect their accounts in fewer steps with Link, allowing them to save and reuse their bank account details across Stripe businesses.

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
  contact_email: '{{CUSTOMER_EMAIL}}',
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

## Create a PaymentIntent [Server-side] [Client-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) is an object that represents your intent to collect payment from a customer and tracks the lifecycle of the payment process through each stage.

### Server-side

First, create a PaymentIntent on your server and specify the amount to collect and the `usd` currency. If you already have an integration using the Payment Intents API, add `us_bank_account` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your PaymentIntent. Optionally, specify the [id](https://docs.stripe.com/api/customers/object.md#customer_object-id) of the Customer.

If you want to reuse the payment method in the future, provide the [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) parameter with the value of `off_session`.

For more information on Financial Connections fees, see [pricing details](https://stripe.com/financial-connections#pricing).

By default, collecting bank account payment information uses [Financial Connections](https://docs.stripe.com/financial-connections.md) to instantly verify your customer’s account, with a fallback option of manual account number entry and microdeposit verification. See the [Financial Connections docs](https://docs.stripe.com/financial-connections/ach-direct-debit-payments.md) to learn how to configure Financial Connections and access additional account data to optimize your ACH integration. For example, you can use Financial Connections to check an account’s balance before initiating the ACH payment.

> To expand access to additional data after a customer authenticates their account, they must re-link their account with expanded permissions.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'usd',
  setup_future_usage: "off_session",
  customer_account: '{{CUSTOMERACCOUNT_ID}}',
  payment_method_types: ['us_bank_account'],
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'usd',
  setup_future_usage: "off_session",
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['us_bank_account'],
});
```

### Client-side

Included in the returned PaymentIntent is a _client secret_ (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)), which the client side can use to securely complete the payment process instead of passing the entire PaymentIntent object. On the client, request a PaymentIntent from your server and store its client secret.

#### Swift

```swift
import UIKit
import StripePayments

class CheckoutViewController: UIViewController {
  var paymentIntentClientSecret: String?

  func startCheckout() {
      // Request a PaymentIntent from your server and store its client secret
  }
}
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

ACH Direct Debit requires a customer name and (optional) email for the payment to succeed. In your app, collect the required billing details from the customer:

- Their full name (first and last)
- Their email address

Use the class function `collectUSBankAccountParams` in `STPCollectBankAccountParams` to create your parameters required to call `collectBankAccountForPayment`. Including the account holder’s name in the `billing_details` parameter is required to create an ACH Direct Debit PaymentMethod.

Create an instance of `STPBankAccountCollector` to call `collectBankAccountForPayment` to collect bank account details, create a _PaymentMethod_ (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs), and attach that PaymentMethod to the PaymentIntent.

#### Swift

```swift
// Build params
let collectParams = STPCollectBankAccountParams.collectUSBankAccountParams(with: name, email: email)

// (optional) Configure the style
let style: STPBankAccountCollectorUserInterfaceStyle = .alwaysLight
let bankAccountCollector = STPBankAccountCollector(style: style)

// Calling this method will display a modal for collecting bank account information
bankAccountCollector.collectBankAccountForPayment(clientSecret: clientSecret,
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

This loads a modal UI that handles bank account details collection and verification. When it completes, the _PaymentMethod_ (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) automatically attaches to the PaymentIntent.

## Optional: Access data on a Financial Connections bank account [Server-side]

You can only access Financial Connections data if you request additional [data permissions](https://docs.stripe.com/financial-connections/fundamentals.md#data-permissions) when you create your PaymentIntent .

After your customer successfully completes the [Stripe Financial Connections authentication flow](https://docs.stripe.com/financial-connections/fundamentals.md#authentication-flow), the `us_bank_account` PaymentMethod returned includes a [financial_connections_account](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-us_bank_account-financial_connections_account) ID that points to a [Financial Connections Account](https://docs.stripe.com/api/financial_connections/accounts.md). Use this ID to access account data.

> Bank accounts that your customers link through manual entry and microdeposits don’t have a `financial_connections_account` ID on the Payment Method.

To determine the Financial Connections account ID, retrieve the PaymentIntent and expand the `payment_method` attribute:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.retrieve(
  "{{PAYMENTINTENT_ID}}",
  {
    expand: ["payment_method"],
  },
);
```

```json
{
  "id": "{{PAYMENT_INTENT_ID}}",
  "object": "payment_intent",
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

If you opted to receive `balances` permissions, we recommend checking a balance at this stage to verify sufficient funds before confirming a payment.

Learn more about using additional account data to optimize your ACH integration with [Financial Connections](https://docs.stripe.com/financial-connections/ach-direct-debit-payments.md#optimize).

## Collect mandate acknowledgement and submit the payment [Client-side]

Before you can initiate the payment, you must obtain authorization from your customer by displaying mandate terms for them to accept.

To be compliant with _Nacha_ (Nacha is the governing body that oversees the ACH network) rules, you must obtain authorization from your customer before you can initiate payment by displaying mandate terms for them to accept. For more information on mandates, see [Mandates](https://docs.stripe.com/payments/ach-direct-debit.md#mandates).

When the customer accepts the mandate terms, you must confirm the PaymentIntent. Use `confirmPayment` to complete the payment when the customer submits the form.

#### Swift

```swift
let paymentIntentParams = STPPaymentIntentParams(clientSecret: clientSecret,
                                            paymentMethodType: .USBankAccount)

STPPaymentHandler.shared().confirmPayment(
    paymentIntentParams, with: self
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

> `confirmPayment` might take several seconds to complete. During that time, disable resubmittals of your form and show a waiting indicator (for example, a spinner). If you receive an error, show it to the customer, re-enable the form, and hide the waiting indicator.

If successful, Stripe returns a PaymentIntent object, with one of the following possible statuses:

| Status            | Description                                                              | Next Steps                                                                                                                                                |
| ----------------- | ------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `requires_action` | Further action is needed to complete bank account verification.          | Step 6: [Verifying bank accounts with microdeposits](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md#ios-verify-with-microdeposits) |
| `processing`      | The bank account was instantly verified or verification isn’t necessary. | Step 7: [Confirm the PaymentIntent succeeded](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md#ios-confirm-paymentintent-succeeded)  |

After successfully confirming the PaymentIntent, an email confirmation of the mandate and collected bank account details must be sent to your customer. Stripe handles these by default, but you can choose to [send custom notifications](https://docs.stripe.com/payments/ach-direct-debit.md#mandate-and-microdeposit-emails) if you prefer.

## Verify bank account with micro-deposits [Client-side]

Not all customers can verify the bank account instantly. This step only applies if your customer has elected to opt out of the instant verification flow in the previous step.

In these cases, Stripe sends a `descriptor_code` microdeposit and might fall back to an `amount` microdeposit if any further issues arise with verifying the bank account. These deposits take 1-2 business days to appear on the customer’s online statement.

- **Descriptor code**. Stripe sends a single, 0.01 USD microdeposit to the customer’s bank account with a unique, 6-digit `descriptor_code` that starts with SM. Your customer uses this string to verify their bank account.
- **Amount**. Stripe sends two, non-unique microdeposits to the customer’s bank account, with a statement descriptor that reads `ACCTVERIFY`. Your customer uses the deposit amounts to verify their bank account.

The result of the `confirmPayment` method call in the previous step is a PaymentIntent in the `requires_action` state. The PaymentIntent contains a [next_action](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-verify_with_microdeposits) field that contains some useful information for completing the verification.

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
STPAPIClient.shared.verifyPaymentIntentWithMicrodeposits(clientSecret: clientSecret,
                                                         descriptorCode: descriptorCode,
                                                         completion: { intent, error in
})

// Use if you are using amounts, do not use if you are using descriptor code
STPAPIClient.shared.verifyPaymentIntentWithMicrodeposits(clientSecret: clientSecret,
                                                         firstAmount: firstAmount,
                                                         secondAmount: secondAmount,
                                                         completion: { intent, error in
})
```

When the bank account is successfully verified, Stripe returns the PaymentIntent object with a `status` of `processing`.

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

| Error Code                                                   | Message                                                                                                                                         | Status change                                                           |
| ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `payment_method_microdeposit_failed`                         | Microdeposits failed. Please check the account, institution and transit numbers provided.                                                       | `status` is `requires_payment_method`, and `last_payment_error` is set. |
| `payment_method_microdeposit_verification_amounts_mismatch`  | The amounts provided don’t match the amounts that were sent to the bank account. You have {attempts_remaining} verification attempts remaining. | Unchanged                                                               |
| `payment_method_microdeposit_verification_attempts_exceeded` | Exceeded number of allowed verification attempts                                                                                                | `status` is `requires_payment_method`, and `last_payment_error` is set. |

## Confirm the PaymentIntent succeeded [Server-side]

ACH Direct Debit is a [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method. This means that it can take up to four business days to receive notification of the success or failure of a payment after you initiate a debit from your customer’s account.

The PaymentIntent you create initially has a status of `processing`. After the payment has succeeded, the PaymentIntent status is updated from `processing` to `succeeded`.

We recommend using [webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks) to _confirm_ (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) the charge has succeeded and to notify the customer that the payment is complete. You can also view events on the [Stripe Dashboard](https://dashboard.stripe.com/events).

#### PaymentIntent events

The following events are sent when the PaymentIntent status is updated:

| Event                           | Description                                                                                     | Next Step                                                                                                                                                                                                                                                                                     |
| ------------------------------- | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_intent.processing`     | The customer’s payment was submitted to Stripe successfully.                                    | Wait for the initiated payment to succeed or fail.                                                                                                                                                                                                                                            |
| `payment_intent.succeeded`      | The customer’s payment succeeded.                                                               | Fulfill the goods or services that were purchased.                                                                                                                                                                                                                                            |
| `payment_intent.payment_failed` | The customer’s payment was declined. This can also apply to a failed microdeposit verification. | Contact the customer through email or push notification and request another payment method. If the webhook was sent due to a failed microdeposit verification, the user needs to enter in their bank account details again and a new set of microdeposits will be deposited in their account. |

#### Charge events

You may also use additional Charge webhooks to track the payment’s status. Upon receiving the `charge.updated` webhook, the payment is no longer cancellable.

The following events are sent when the Charge status is updated:

| Event              | Description                                                                                                                                     | Next Step                                                                         |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `charge.pending`   | The customer’s payment was created successfully.                                                                                                | Wait for the initiated payment to be processed.                                   |
| `charge.updated`   | The customer’s payment was updated. It can be emitted when a new balance transaction was created, a charge description or metadata got updated. | Wait for the initiated payment to succeed or fail.                                |
| `charge.succeeded` | The customer’s payment succeeded and the funds are available in your balance.                                                                   | Fulfill the goods or services that were purchased.                                |
| `charge.failed`    | The customer’s payment failed.                                                                                                                  | Check the charge’s failure_code and failure_message to determine further actions. |

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

Test transactions settle instantly and are added to your available test balance. This behavior differs from livemode, where transactions can take [multiple days](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md#timing) to settle in your available balance.

## Optional: Instant only verification [Server-side]

By default, US bank account payments allows your customers to use instant bank account verification or microdeposits. You can optionally require instant bank account verification only, using the [verification_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-us_bank_account-verification_method) parameter when you create the PaymentIntent.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'usd',
  setup_future_usage: "off_session",
  customer_account: '{{CUSTOMERACCOUNT_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      verification_method: 'instant',
      financial_connections: {
        permissions: ["payment_method", "balances"],
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
  currency: 'usd',
  setup_future_usage: "off_session",
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      verification_method: 'instant',
      financial_connections: {
        permissions: ["payment_method", "balances"],
      },
    },
  },
});
```

This ensures that you don’t need to handle microdeposit verification. However, if instant verification fails, the PaymentIntent’s status is `requires_payment_method`, indicating a failure to instantly verify a bank account for your customer.

## Optional: Microdeposit only verification [Server-side]

By default, US bank account payments allow your customers to use instant bank account verification or microdeposits. You can optionally require microdeposit verification only using the [verification_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-us_bank_account-verification_method) parameter when you create the PaymentIntent.

> If using a custom payment form, you must build your own UI to collect bank account details. If you disable Stripe microdeposit emails, you must build your own UI for your customer to confirm the microdeposit code or amount.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'usd',
  setup_future_usage: "off_session",
  customer_account: '{{CUSTOMERACCOUNT_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      verification_method: "microdeposits",
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
  currency: 'usd',
  setup_future_usage: "off_session",
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      verification_method: "microdeposits",
    },
  },
});
```

You must then collect your customer’s bank account with your own form and call [stripe.confirmUsBankAccountPayment](https://docs.stripe.com/js/payment_intents/confirm_us_bank_account_payment) with those details to complete the PaymentIntent.

```javascript
var form = document.getElementById("payment-form");
var accountholderName = document.getElementById("accountholder-name");
var email = document.getElementById("email");
var accountNumber = document.getElementById("account-number");
var routingNumber = document.getElementById("routing-number");
var accountHolderType = document.getElementById("account-holder-type");

var submitButton = document.getElementById("submit-button");
var clientSecret = submitButton.dataset.secret;

form.addEventListener("submit", function (event) {
  event.preventDefault();

  stripe
    .confirmUsBankAccountPayment(clientSecret, {
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
    .then(({ paymentIntent, error }) => {
      if (error) {
        // Inform the customer that there was an error.
        console.log(error.message);
      } else {
        // Handle next step based on the intent's status.
        console.log("PaymentIntent ID: " + paymentIntent.id);
        console.log("PaymentIntent status: " + paymentIntent.status);
      }
    });
});
```

## Optional: Payment Reference

The payment reference number is a bank-generated value that allows the bank account owner to use their bank to locate funds. When the payment succeeds, Stripe provides the payment reference number in the Dashboard and inside the [Charge object](https://docs.stripe.com/api/charges/object.md).

| Charge State | Payment Reference Value                  |
| ------------ | ---------------------------------------- |
| Pending      | Unavailable                              |
| Failed       | Unavailable                              |
| Succeeded    | Available (for example, 091000015001234) |

In addition, when you receive the `charge.succeeded` webhook, view the content of `payment_method_details` to locate the [payment_reference](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-us_bank_account-payment_reference).

The following example event shows the rendering of a successful ACH payment with a payment reference number.

#### charge-succeeded

```json
{
  "id": "{{EVENT_ID}}",
  "object": "event",
  // omitted some fields in the example
  "type": "charge.succeeded",
  "data": {
    "object": {
      "id": "{{PAYMENT_ID}}",
      "object": "charge",
      //...
      "paid": true,
      "payment_intent": "{{PAYMENT_INTENT_ID}}",
      "payment_method": "{{PAYMENT_METHOD_ID}}",
      "payment_method_details": {
        "type": "us_bank_account",
        "us_bank_account": {
          "account_holder_type": "individual",
          "account_type": "checking",
          "bank_name": "TEST BANK",
          "fingerprint": "Ih3foEnRvLXShyfB",
          "last4": "1000",
          "payment_reference": "091000015001234",
          "routing_number": "110000000"
        }
      }
      // ...
    }
  }
}
```

View the contents of the `destination_details` to locate the [refund reference](https://docs.stripe.com/api/refunds/object.md#refund_object-destination_details-us_bank_transfer-reference) associated with the refunded ACH payments.

The following example event shows the rendering of a successful ACH refund with a refund reference number. Learn more about [refunds](https://docs.stripe.com/refunds.md).

#### charge-refund-updated

```json
{
  "id": "{{EVENT_ID}}",
  "object": "event",
  "type": "charge.refund.updated",
  "data": {
    "object": {
      "id": "{{REFUND_ID}}",
      "object": "refund",
      //...
      "payment_intent": "{{PAYMENT_INTENT_ID}}",
      "destination_details": {
        "type": "us_bank_transfer",
        "us_bank_transfer": {
          "reference": "091000015001111",
          "reference_status": "available"
        }
      }
      // ...
    }
  }
}
```

## See also

- [Save ACH Direct Debit pre-authorized debit details for future payments](https://docs.stripe.com/payments/ach-direct-debit/set-up-payment.md)

# Android

> This is a Android for when payment-ui is mobile and platform is android. View the full page at https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment?payment-ui=mobile&platform=android.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

Accepting ACH Direct Debit payments in your app consists of:

- Creating an object to track a payment
- Collecting payment method information with instant verifications enabled by [Stripe Financial Connections](https://docs.stripe.com/financial-connections.md)
- Submitting the payment to Stripe for processing
- Verifying your customer’s bank account

> ACH Direct Debit is a [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method, which means that funds aren’t immediately available after payment. A payment typically takes 4 business days to arrive in your account.

Stripe uses the payment object, the [Payment Intent](https://docs.stripe.com/payments/payment-intents.md), to track and handle all the states of the payment until the payment completes.

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
  contact_email: '{{CUSTOMER_EMAIL}}',
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

## Create a PaymentIntent [Server-side] [Client-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) is an object that represents your intent to collect payment from a customer and tracks the lifecycle of the payment process through each stage.

### Server-side

First, create a PaymentIntent on your server and specify the amount to collect and the `usd` currency. If you already have an integration using the Payment Intents API, add `us_bank_account` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your PaymentIntent. Optionally, specify the [id](https://docs.stripe.com/api/customers/object.md#customer_object-id) of the Customer.

If you want to reuse the payment method in the future, provide the [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) parameter with the value of `off_session`.

For more information on Financial Connections fees, see [pricing details](https://stripe.com/financial-connections#pricing).

By default, collecting bank account payment information uses [Financial Connections](https://docs.stripe.com/financial-connections.md) to instantly verify your customer’s account, with a fallback option of manual account number entry and microdeposit verification. See the [Financial Connections docs](https://docs.stripe.com/financial-connections/ach-direct-debit-payments.md) to learn how to configure Financial Connections and access additional account data to optimize your ACH integration. For example, you can use Financial Connections to check an account’s balance before initiating the ACH payment.

> To expand access to additional data after a customer authenticates their account, they must re-link their account with expanded permissions.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'usd',
  setup_future_usage: "off_session",
  customer_account: '{{CUSTOMERACCOUNT_ID}}',
  payment_method_types: ['us_bank_account'],
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'usd',
  setup_future_usage: "off_session",
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['us_bank_account'],
});
```

### Client-side

Included in the returned PaymentIntent is a _client secret_ (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)), which the client side can use to securely complete the payment process instead of passing the entire PaymentIntent object. On the client, request a PaymentIntent from your server and use the client secret for subsequent API calls.

#### Kotlin

```kotlin
import androidx.appcompat.app.AppCompatActivity

class CheckoutActivity : AppCompatActivity() {
    private lateinit var paymentIntentClientSecret: String

    fun startCheckout() {
        // Request a PaymentIntent from your server and store its client secret
    }
}
```

## Collect payment method details [Client-side]

ACH Direct Debit requires a customer name and (optional) email for the payment to succeed. In your app, collect the required billing details from the customer:

- Their full name (first and last)
- Their email address

Use `CollectBankAccountConfiguration.USBankAccount` to create the parameters required to call `presentWithPaymentIntent`.

Initialize a `CollectBankAccountLauncher` instance inside onCreate of your checkout Activity, passing a method to handle the result. Then proceed to call `presentWithPaymentIntent` to collect bank account details, create a _PaymentMethod_ (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs), and attach that PaymentMethod to the PaymentIntent.

#### Kotlin

```kotlin
import androidx.appcompat.app.AppCompatActivity

class CheckoutActivity : AppCompatActivity() {
    private lateinit var paymentIntentClientSecret: String
    private lateinit var collectBankAccountLauncher CollectBankAccountLauncher

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
        val configuration: CollectBankAccountConfiguration =
            CollectBankAccountConfiguration.USBankAccount(
                name,
                email
            )

        // Calling this method will trigger the Financial Connections modal to be displayed
        collectBankAccountLauncher.presentWithPaymentIntent(
            publishableKey,
            paymentIntentClientSecret,
            collectParams
        )
    }
}
```

This loads a modal UI that handles bank account details collection and verification. When it completes, the _PaymentMethod_ (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) automatically attaches to the PaymentIntent.

## Optional: Customize the sheet [Client-side]

### Dark mode

By default, `CollectBankAccountLauncher` automatically adapts to the user’s system-wide appearance settings (light and dark mode). You can change this by setting light or dark mode on your app:

#### Kotlin

```kotlin
// force dark
AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_YES)
// force light
AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_NO)
```

## Optional: Access data on a Financial Connections bank account [Server-side]

You can only access Financial Connections data if you request additional [data permissions](https://docs.stripe.com/financial-connections/fundamentals.md#data-permissions) when you create your PaymentIntent .

After your customer successfully completes the [Stripe Financial Connections authentication flow](https://docs.stripe.com/financial-connections/fundamentals.md#authentication-flow), the `us_bank_account` PaymentMethod returned includes a [financial_connections_account](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-us_bank_account-financial_connections_account) ID that points to a [Financial Connections Account](https://docs.stripe.com/api/financial_connections/accounts.md). Use this ID to access account data.

> Bank accounts that your customers link through manual entry and microdeposits don’t have a `financial_connections_account` ID on the Payment Method.

To determine the Financial Connections account ID, retrieve the PaymentIntent and expand the `payment_method` attribute:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.retrieve(
  "{{PAYMENTINTENT_ID}}",
  {
    expand: ["payment_method"],
  },
);
```

```json
{
  "id": "{{PAYMENT_INTENT_ID}}",
  "object": "payment_intent",
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

If you opted to receive `balances` permissions, we recommend checking a balance at this stage to verify sufficient funds before confirming a payment.

Learn more about using additional account data to optimize your ACH integration with [Financial Connections](https://docs.stripe.com/financial-connections/ach-direct-debit-payments.md#optimize).

## Collect mandate acknowledgement and submit the payment [Client-side]

Before you can initiate the payment, you must obtain authorization from your customer by displaying mandate terms for them to accept.

To be compliant with _Nacha_ (Nacha is the governing body that oversees the ACH network) rules, you must obtain authorization from your customer before you can initiate payment by displaying mandate terms for them to accept. For more information on mandates, see [Mandates](https://docs.stripe.com/payments/ach-direct-debit.md#mandates).

When the customer accepts the mandate terms, you must confirm the Payment. Use `confirm` to complete the payment when the customer submits the form.

#### Kotlin

```kotlin
class CheckoutActivity : AppCompatActivity() {
    // ...
    private lateinit var paymentIntentClientSecret: String
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

        val confirmParams = ConfirmPaymentIntentParams.create(
            clientSecret = paymentIntentClientSecret,
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

If successful, Stripe returns a PaymentIntent object, with one of the following possible statuses:

| Status            | Description                                                              | Next Steps                                                                                                                                                    |
| ----------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `requires_action` | Further action is needed to complete bank account verification.          | Step 5: [Verifying bank accounts with microdeposits](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md#android-verify-with-microdeposits) |
| `processing`      | The bank account was instantly verified or verification isn’t necessary. | Step 6: [Confirm the PaymentIntent succeeded](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md#android-confirm-paymentintent-succeeded)  |

After successfully confirming the Payment, an email confirmation of the mandate and collected bank account details must be sent to your customer. Stripe handles these by default, but you can choose to [send custom notifications](https://docs.stripe.com/payments/ach-direct-debit.md#mandate-and-microdeposit-emails) if you prefer.

## Verify bank account with micro-deposits [Client-side]

Not all customers can verify the bank account instantly. This step only applies if your customer has elected to opt out of the instant verification flow in the previous step.

In these cases, Stripe sends a `descriptor_code` microdeposit and might fall back to an `amount` microdeposit if any further issues arise with verifying the bank account. These deposits take 1-2 business days to appear on the customer’s online statement.

- **Descriptor code**. Stripe sends a single, 0.01 USD microdeposit to the customer’s bank account with a unique, 6-digit `descriptor_code` that starts with SM. Your customer uses this string to verify their bank account.
- **Amount**. Stripe sends two, non-unique microdeposits to the customer’s bank account, with a statement descriptor that reads `ACCTVERIFY`. Your customer uses the deposit amounts to verify their bank account.

The result of the `confirmPayment` method call in the previous step is a PaymentIntent in the `requires_action` state. The PaymentIntent contains a [next_action](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-verify_with_microdeposits) field that contains some useful information for completing the verification.

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
fun verifyPaymentIntentWithMicrodeposits(
    clientSecret: String,
    descriptorCode: String,
    callback: ApiResultCallback<PaymentIntent>
)

// Use if you are using amounts, do not use if you are using descriptor code
fun verifyPaymentIntentWithMicrodeposits(
    clientSecret: String,
    firstAmount: Int,
    secondAmount: Int,
    callback: ApiResultCallback<PaymentIntent>
)
```

When the bank account is successfully verified, Stripe returns the PaymentIntent object with a `status` of `processing`.

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

| Error Code                                                   | Message                                                                                                                                         | Status change                                                           |
| ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `payment_method_microdeposit_failed`                         | Microdeposits failed. Please check the account, institution and transit numbers provided.                                                       | `status` is `requires_payment_method`, and `last_payment_error` is set. |
| `payment_method_microdeposit_verification_amounts_mismatch`  | The amounts provided don’t match the amounts that were sent to the bank account. You have {attempts_remaining} verification attempts remaining. | Unchanged                                                               |
| `payment_method_microdeposit_verification_attempts_exceeded` | Exceeded number of allowed verification attempts                                                                                                | `status` is `requires_payment_method`, and `last_payment_error` is set. |

## Confirm the PaymentIntent succeeded [Server-side]

ACH Direct Debit is a [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method. This means that it can take up to four business days to receive notification of the success or failure of a payment after you initiate a debit from your customer’s account.

The PaymentIntent you create initially has a status of `processing`. After the payment has succeeded, the PaymentIntent status is updated from `processing` to `succeeded`.

We recommend using [webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks) to _confirm_ (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) the charge has succeeded and to notify the customer that the payment is complete. You can also view events on the [Stripe Dashboard](https://dashboard.stripe.com/events).

#### PaymentIntent events

The following events are sent when the PaymentIntent status is updated:

| Event                           | Description                                                                                     | Next Step                                                                                                                                                                                                                                                                                     |
| ------------------------------- | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_intent.processing`     | The customer’s payment was submitted to Stripe successfully.                                    | Wait for the initiated payment to succeed or fail.                                                                                                                                                                                                                                            |
| `payment_intent.succeeded`      | The customer’s payment succeeded.                                                               | Fulfill the goods or services that were purchased.                                                                                                                                                                                                                                            |
| `payment_intent.payment_failed` | The customer’s payment was declined. This can also apply to a failed microdeposit verification. | Contact the customer through email or push notification and request another payment method. If the webhook was sent due to a failed microdeposit verification, the user needs to enter in their bank account details again and a new set of microdeposits will be deposited in their account. |

#### Charge events

You may also use additional Charge webhooks to track the payment’s status. Upon receiving the `charge.updated` webhook, the payment is no longer cancellable.

The following events are sent when the Charge status is updated:

| Event              | Description                                                                                                                                     | Next Step                                                                         |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `charge.pending`   | The customer’s payment was created successfully.                                                                                                | Wait for the initiated payment to be processed.                                   |
| `charge.updated`   | The customer’s payment was updated. It can be emitted when a new balance transaction was created, a charge description or metadata got updated. | Wait for the initiated payment to succeed or fail.                                |
| `charge.succeeded` | The customer’s payment succeeded and the funds are available in your balance.                                                                   | Fulfill the goods or services that were purchased.                                |
| `charge.failed`    | The customer’s payment failed.                                                                                                                  | Check the charge’s failure_code and failure_message to determine further actions. |

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

Test transactions settle instantly and are added to your available test balance. This behavior differs from livemode, where transactions can take [multiple days](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md#timing) to settle in your available balance.

## Optional: Instant only verification [Server-side]

By default, US bank account payments allows your customers to use instant bank account verification or microdeposits. You can optionally require instant bank account verification only, using the [verification_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-us_bank_account-verification_method) parameter when you create the PaymentIntent.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'usd',
  setup_future_usage: "off_session",
  customer_account: '{{CUSTOMERACCOUNT_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      verification_method: 'instant',
      financial_connections: {
        permissions: ["payment_method", "balances"],
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
  currency: 'usd',
  setup_future_usage: "off_session",
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      verification_method: 'instant',
      financial_connections: {
        permissions: ["payment_method", "balances"],
      },
    },
  },
});
```

This ensures that you don’t need to handle microdeposit verification. However, if instant verification fails, the PaymentIntent’s status is `requires_payment_method`, indicating a failure to instantly verify a bank account for your customer.

## Optional: Microdeposit only verification [Server-side]

By default, US bank account payments allow your customers to use instant bank account verification or microdeposits. You can optionally require microdeposit verification only using the [verification_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-us_bank_account-verification_method) parameter when you create the PaymentIntent.

> If using a custom payment form, you must build your own UI to collect bank account details. If you disable Stripe microdeposit emails, you must build your own UI for your customer to confirm the microdeposit code or amount.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'usd',
  setup_future_usage: "off_session",
  customer_account: '{{CUSTOMERACCOUNT_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      verification_method: "microdeposits",
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
  currency: 'usd',
  setup_future_usage: "off_session",
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      verification_method: "microdeposits",
    },
  },
});
```

You must then collect your customer’s bank account with your own form and call [stripe.confirmUsBankAccountPayment](https://docs.stripe.com/js/payment_intents/confirm_us_bank_account_payment) with those details to complete the PaymentIntent.

```javascript
var form = document.getElementById("payment-form");
var accountholderName = document.getElementById("accountholder-name");
var email = document.getElementById("email");
var accountNumber = document.getElementById("account-number");
var routingNumber = document.getElementById("routing-number");
var accountHolderType = document.getElementById("account-holder-type");

var submitButton = document.getElementById("submit-button");
var clientSecret = submitButton.dataset.secret;

form.addEventListener("submit", function (event) {
  event.preventDefault();

  stripe
    .confirmUsBankAccountPayment(clientSecret, {
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
    .then(({ paymentIntent, error }) => {
      if (error) {
        // Inform the customer that there was an error.
        console.log(error.message);
      } else {
        // Handle next step based on the intent's status.
        console.log("PaymentIntent ID: " + paymentIntent.id);
        console.log("PaymentIntent status: " + paymentIntent.status);
      }
    });
});
```

## Optional: Payment Reference

The payment reference number is a bank-generated value that allows the bank account owner to use their bank to locate funds. When the payment succeeds, Stripe provides the payment reference number in the Dashboard and inside the [Charge object](https://docs.stripe.com/api/charges/object.md).

| Charge State | Payment Reference Value                  |
| ------------ | ---------------------------------------- |
| Pending      | Unavailable                              |
| Failed       | Unavailable                              |
| Succeeded    | Available (for example, 091000015001234) |

In addition, when you receive the `charge.succeeded` webhook, view the content of `payment_method_details` to locate the [payment_reference](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-us_bank_account-payment_reference).

The following example event shows the rendering of a successful ACH payment with a payment reference number.

#### charge-succeeded

```json
{
  "id": "{{EVENT_ID}}",
  "object": "event",
  // omitted some fields in the example
  "type": "charge.succeeded",
  "data": {
    "object": {
      "id": "{{PAYMENT_ID}}",
      "object": "charge",
      //...
      "paid": true,
      "payment_intent": "{{PAYMENT_INTENT_ID}}",
      "payment_method": "{{PAYMENT_METHOD_ID}}",
      "payment_method_details": {
        "type": "us_bank_account",
        "us_bank_account": {
          "account_holder_type": "individual",
          "account_type": "checking",
          "bank_name": "TEST BANK",
          "fingerprint": "Ih3foEnRvLXShyfB",
          "last4": "1000",
          "payment_reference": "091000015001234",
          "routing_number": "110000000"
        }
      }
      // ...
    }
  }
}
```

View the contents of the `destination_details` to locate the [refund reference](https://docs.stripe.com/api/refunds/object.md#refund_object-destination_details-us_bank_transfer-reference) associated with the refunded ACH payments.

The following example event shows the rendering of a successful ACH refund with a refund reference number. Learn more about [refunds](https://docs.stripe.com/refunds.md).

#### charge-refund-updated

```json
{
  "id": "{{EVENT_ID}}",
  "object": "event",
  "type": "charge.refund.updated",
  "data": {
    "object": {
      "id": "{{REFUND_ID}}",
      "object": "refund",
      //...
      "payment_intent": "{{PAYMENT_INTENT_ID}}",
      "destination_details": {
        "type": "us_bank_transfer",
        "us_bank_transfer": {
          "reference": "091000015001111",
          "reference_status": "available"
        }
      }
      // ...
    }
  }
}
```

## See also

- [Save ACH Direct Debit pre-authorized debit details for future payments](https://docs.stripe.com/payments/ach-direct-debit/set-up-payment.md)

# React Native

> This is a React Native for when payment-ui is mobile and platform is react-native. View the full page at https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment?payment-ui=mobile&platform=react-native.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

Accepting ACH Direct Debit payments in your app consists of:

- Creating an object to track a payment
- Collecting payment method information
- Submitting the payment to Stripe for processing
- Verifying your customer’s bank account

Stripe uses a [Payment Intent](https://docs.stripe.com/payments/payment-intents.md) to track and handle all the states of the payment until the payment completes.

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

With Stripe, you can instantly verify a customer’s bank account. If you want to retrieve additional data on an account, [sign up for data access](https://dashboard.stripe.com/financial-connections/application) with [Stripe Financial Connections](https://docs.stripe.com/financial-connections.md).

Stripe Financial Connections lets your customers securely share their financial data by linking their financial accounts to your business. Use Financial Connections to access customer-permissioned financial data such as tokenized account and routing numbers, balance data, ownership details, and transaction data.

Access to this data helps you perform actions like check balances before initiating a payment to reduce the chance of a failed payment because of insufficient funds.

Financial Connections enables your users to connect their accounts in fewer steps with Link, allowing them to save and reuse their bank account details across Stripe businesses.

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
  contact_email: '{{CUSTOMER_EMAIL}}',
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

## Create a PaymentIntent [Server-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) is an object that represents your intent to collect payment from a customer and tracks the lifecycle of the payment process through each stage.

### Server-side

First, create a PaymentIntent on your server and specify the amount to collect and `usd` as the currency. If you already have an integration using the Payment Intents API, add `us_bank_account` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your PaymentIntent. Specify the [id](https://docs.stripe.com/api/customers/object.md#customer_object-id) of the Customer.

If you want to reuse the payment method in the future, provide the [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) parameter with the value of `off_session`.

For more information on Financial Connections fees, see [pricing details](https://stripe.com/financial-connections#pricing).

By default, collecting bank account payment information uses [Financial Connections](https://docs.stripe.com/financial-connections.md) to instantly verify your customer’s account, with a fallback option of manual account number entry and microdeposit verification. See the [Financial Connections docs](https://docs.stripe.com/financial-connections/ach-direct-debit-payments.md) to learn how to configure Financial Connections and access additional account data to optimize your ACH integration. For example, you can use Financial Connections to check an account’s balance before initiating the ACH payment.

> To expand access to additional data after a customer authenticates their account, they must re-link their account with expanded permissions.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'usd',
  setup_future_usage: "off_session",
  customer_account: '{{CUSTOMERACCOUNT_ID}}',
  payment_method_types: ['us_bank_account'],
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'usd',
  setup_future_usage: "off_session",
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['us_bank_account'],
});
```

### Client-side

A PaymentIntent includes a _client secret_ (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)). You can use the client secret in your React Native app to securely complete the payment process instead of passing back the entire PaymentIntent object. In your app, request a PaymentIntent from your server and store its client secret.

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
        product: "<PRODUCT_ID>",
      }),
    });
    const { clientSecret } = await response.json();

    return clientSecret;
  };

  return <View>...</View>;
}
```

## Collect payment method details [Client-side]

Rather than sending the entire PaymentIntent object to the client, use its _client secret_ (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)) from the previous step. This is different from your API keys that authenticate Stripe API requests.

Handle the client secret carefully because it can complete the charge. Don’t log it, embed it in URLs, or expose it to anyone but the customer

Use [collectBankAccountForPayment](https://docs.stripe.com/js/payment_intents/collect_bank_account_for_payment) to collect bank account details, create a _PaymentMethod_ (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs), and attach that PaymentMethod to the PaymentIntent. You must include the account holder’s name in the `billingDetails` parameter to create an ACH Direct Debit PaymentMethod.

```javascript
import { collectBankAccountForPayment } from "@stripe/stripe-react-native";

export default function MyPaymentScreen() {
  const [name, setName] = useState("");

  const handleCollectBankAccountPress = async () => {
    // Fetch the intent client secret from the backend.
    // See `fetchIntentClientSecret()`'s implementation above.
    const { clientSecret } = await fetchIntentClientSecret();

    const { paymentIntent, error } = await collectBankAccountForPayment(
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
    } else if (paymentIntent) {
      Alert.alert("Payment status:", paymentIntent.status);
      if (paymentIntent.status === PaymentIntents.Status.RequiresConfirmation) {
        // The next step is to call `confirmPayment`
      } else if (
        paymentIntent.status === PaymentIntents.Status.RequiresAction
      ) {
        // The next step is to call `verifyMicrodepositsForPayment`
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

This loads a modal UI that handles bank account details collection and verification. When it completes, the _PaymentMethod_ (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) is automatically attached to the PaymentIntent.

## Optional: Customize the bank account collector [Client-side]

### Dark mode

By default, the bank account collector automatically switches between light and dark mode compatible colors based on device settings. If your app doesn’t support dark or light mode, you can set `style` to `alwaysLight` or `alwaysDark`, respectively.

```javascript
const { session, error } = await collectBankAccountForPayment(clientSecret, {
  style: "alwaysLight",
});
```

To achieve an always light or always dark appearance in your Android app, make use of Android’s `AppCompatDelegate`. Our UI automatically respects this setting.

#### Kotlin

```kotlin
// force dark
AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_YES)
// force light
AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_NO)
```

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

You can only access Financial Connections data if you request additional [data permissions](https://docs.stripe.com/financial-connections/fundamentals.md#data-permissions) when you create your PaymentIntent .

After your customer successfully completes the [Stripe Financial Connections authentication flow](https://docs.stripe.com/financial-connections/fundamentals.md#authentication-flow), the `us_bank_account` PaymentMethod returned includes a [financial_connections_account](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-us_bank_account-financial_connections_account) ID that points to a [Financial Connections Account](https://docs.stripe.com/api/financial_connections/accounts.md). Use this ID to access account data.

> Bank accounts that your customers link through manual entry and microdeposits don’t have a `financial_connections_account` ID on the Payment Method.

To determine the Financial Connections account ID, retrieve the PaymentIntent and expand the `payment_method` attribute:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.retrieve(
  "{{PAYMENTINTENT_ID}}",
  {
    expand: ["payment_method"],
  },
);
```

```json
{
  "id": "{{PAYMENT_INTENT_ID}}",
  "object": "payment_intent",
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

If you opted to receive `balances` permissions, we recommend checking a balance at this stage to verify sufficient funds before confirming a payment.

Learn more about using additional account data to optimize your ACH integration with [Financial Connections](https://docs.stripe.com/financial-connections/ach-direct-debit-payments.md#optimize).

## Collect mandate acknowledgement and submit the payment [Client-side]

Before you can initiate the payment, you must obtain authorization from your customer by displaying mandate terms for them to accept.

To comply with Nacha rules, you must obtain authorization from your customer before you can initiate payment by displaying mandate terms for them to accept. For more information on mandates, see [Mandates](https://docs.stripe.com/payments/ach-direct-debit.md#mandates).

When the customer accepts the mandate terms, you must confirm the PaymentIntent. Use `confirmPayment` to confirm the intent.

```javascript
import { confirmPayment } from "@stripe/stripe-react-native";

export default function MyPaymentScreen() {
  const [name, setName] = useState("");

  const handleCollectBankAccountPress = async () => {
    // See above
  };

  const handlePayPress = async () => {
    // use the same clientSecret as earlier, see above
    const { error, paymentIntent } = await confirmPayment(clientSecret, {
      paymentMethodType: "USBankAccount",
    });

    if (error) {
      Alert.alert(`Error code: ${error.code}`, error.message);
    } else if (paymentIntent) {
      if (paymentIntent.status === PaymentIntents.Status.Processing) {
        // The debit has been successfully submitted and is now processing
      } else if (
        paymentIntent.status === PaymentIntents.Status.RequiresAction &&
        paymentIntent?.nextAction?.type === "verifyWithMicrodeposits"
      ) {
        // The payment must be verified with `verifyMicrodepositsForPayment`
      } else {
        Alert.alert("Payment status:", paymentIntent.status);
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

If successful, Stripe returns a PaymentIntent object, with one of the following possible statuses:

| Status           | Description                                                              | Next Steps                                                                                                                                                                               |
| ---------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `RequiresAction` | Bank account verification requires further action.                       | Step 6: [Verifying bank accounts with microdeposits](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md?platform=react-native#react-native-verify-with-microdeposits) |
| `Processing`     | The bank account was instantly verified or verification isn’t necessary. | Step 7: [Confirm the PaymentIntent succeeded](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md?platform=react-native#confirm-paymentintent-succeeded)               |

After successfully confirming the PaymentIntent, an email confirmation of the mandate and collected bank account details must be sent to your customer. Stripe handles these by default, but you can choose to [send custom notifications](https://docs.stripe.com/payments/ach-direct-debit.md#mandate-and-microdeposit-emails) if you prefer.

## Verify bank account with microdeposits [Client-side]

Not all customers can verify their bank account instantly. In these cases, Stripe sends a microdeposit to the bank account. This deposit might take up to 1-2 business days to appear on the customer’s online statement. This deposit takes one of two shapes:

- **Descriptor code**. Stripe sends a single, 0.01 USD microdeposit to the customer’s bank account with a unique, 6-digit `descriptorCode` that starts with SM. Your customer uses this string to verify their bank account.
- **Amount**. Stripe sends two, non-unique microdeposits to the customer’s bank account, with a statement descriptor that reads `ACCTVERIFY`. Your customer uses the deposit amounts to verify their bank account.

If the result of the `confirmPayment` method call in the previous step is a PaymentIntent with a `requiresAction` status, the PaymentIntent contains a `nextAction` field that contains some useful information for completing the verification.

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

1. Verify the deposits directly in your app by calling `verifyMicrodepositsForPayment` after collecting either the descriptor code or amounts.

```javascript
import { verifyMicrodepositsForPayment } from '@stripe/stripe-react-native';

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
          await verifyMicrodepositsForPayment(secret, {
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
const { error, paymentIntent } = await confirmPayment(clientSecret, {
  paymentMethodType: "USBankAccount",
});

if (error) {
  Alert.alert(`Error code: ${error.code}`, error.message);
} else if (paymentIntent) {
  if (
    paymentIntent.status === PaymentIntents.Status.RequiresAction &&
    paymentIntent?.nextAction?.type === "verifyWithMicrodeposits"
  ) {
    // Open the Stripe-hosted verification page
    Linking.openURL(paymentIntent.nextAction.redirectUrl);
  }
}
```

When the bank account is successfully verified, Stripe returns the PaymentIntent object with a `status` of `Processing`, and sends a [payment_intent.processing](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.processing) _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event.

Verification can fail for several reasons. The failure might happen synchronously as a direct error response, or asynchronously through a [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.failed) webhook event (shown in the following examples).

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
      "message": "You have exceeded the number of allowed verification attempts.",
    },
    ...
    "status": "requires_payment_method"
  }
}
```

| Error Code                                                   | Synchronous or Asynchronous                            | Message                                                                                                                                       | Status change                                                           |
| ------------------------------------------------------------ | ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `payment_method_microdeposit_failed`                         | Synchronously, or asynchronously through webhook event | Microdeposits failed. Please check the account, institution and transit numbers provided                                                      | `status` is `requires_payment_method`, and `last_payment_error` is set. |
| `payment_method_microdeposit_verification_amounts_mismatch`  | Synchronously                                          | The amounts provided don’t match the amounts that we sent to the bank account. You have {attempts_remaining} verification attempts remaining. | Unchanged                                                               |
| `payment_method_microdeposit_verification_attempts_exceeded` | Synchronously, or asynchronously through webhook event | Exceeded the number of allowed verification attempts                                                                                          | `status` is `requires_payment_method`, and `last_payment_error` is set. |
| `payment_method_microdeposit_verification_timeout`           | Asynchronously through a webhook event                 | Microdeposit timeout. The customer hasn’t verified their bank account within the required 10 day period.                                      | `status` is `requires_payment_method`, and `last_payment_error` is set. |

## Confirm the PaymentIntent succeeded [Server-side]

ACH Direct Debit is a [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method. This means that it can take up to four business days to receive notification of the success or failure of a payment after you initiate a debit from your customer’s account.

The PaymentIntent you create initially has a status of `processing`. After the payment has succeeded, the PaymentIntent status is updated from `processing` to `succeeded`.

We recommend using [webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks) to _confirm_ (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) the charge has succeeded and to notify the customer that the payment is complete. You can also view events on the [Stripe Dashboard](https://dashboard.stripe.com/events).

#### PaymentIntent events

The following events are sent when the PaymentIntent status is updated:

| Event                           | Description                                                                                     | Next Step                                                                                                                                                                                                                                                                                     |
| ------------------------------- | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_intent.processing`     | The customer’s payment was submitted to Stripe successfully.                                    | Wait for the initiated payment to succeed or fail.                                                                                                                                                                                                                                            |
| `payment_intent.succeeded`      | The customer’s payment succeeded.                                                               | Fulfill the goods or services that were purchased.                                                                                                                                                                                                                                            |
| `payment_intent.payment_failed` | The customer’s payment was declined. This can also apply to a failed microdeposit verification. | Contact the customer through email or push notification and request another payment method. If the webhook was sent due to a failed microdeposit verification, the user needs to enter in their bank account details again and a new set of microdeposits will be deposited in their account. |

#### Charge events

You may also use additional Charge webhooks to track the payment’s status. Upon receiving the `charge.updated` webhook, the payment is no longer cancellable.

The following events are sent when the Charge status is updated:

| Event              | Description                                                                                                                                     | Next Step                                                                         |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `charge.pending`   | The customer’s payment was created successfully.                                                                                                | Wait for the initiated payment to be processed.                                   |
| `charge.updated`   | The customer’s payment was updated. It can be emitted when a new balance transaction was created, a charge description or metadata got updated. | Wait for the initiated payment to succeed or fail.                                |
| `charge.succeeded` | The customer’s payment succeeded and the funds are available in your balance.                                                                   | Fulfill the goods or services that were purchased.                                |
| `charge.failed`    | The customer’s payment failed.                                                                                                                  | Check the charge’s failure_code and failure_message to determine further actions. |

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

Test transactions settle instantly and are added to your available test balance. This behavior differs from livemode, where transactions can take [multiple days](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md#timing) to settle in your available balance.

## Optional: Instant only verification [Server-side]

By default, US bank account payments allows your customers to use instant bank account verification or microdeposits. You can optionally require instant bank account verification only, using the [verification_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-us_bank_account-verification_method) parameter when you create the PaymentIntent.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'usd',
  setup_future_usage: "off_session",
  customer_account: '{{CUSTOMERACCOUNT_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      verification_method: 'instant',
      financial_connections: {
        permissions: ["payment_method", "balances"],
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
  currency: 'usd',
  setup_future_usage: "off_session",
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      verification_method: 'instant',
      financial_connections: {
        permissions: ["payment_method", "balances"],
      },
    },
  },
});
```

This ensures that you don’t need to handle microdeposit verification. However, if instant verification fails, the PaymentIntent’s status is `requires_payment_method`, indicating a failure to instantly verify a bank account for your customer.

## Optional: Microdeposit only verification [Server-side]

By default, US bank account payments allow your customers to use instant bank account verification or microdeposits. You can optionally require microdeposit verification only using the [verification_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-us_bank_account-verification_method) parameter when you create the PaymentIntent.

> If you use a custom payment form, you must build your own UI to collect bank account details. If you disable Stripe microdeposit emails, you must build your own UI for your customer to confirm the microdeposit code or amount.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'usd',
  setup_future_usage: "off_session",
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      verification_method: "microdeposits",
    },
  },
});
```

## Optional: Payment Reference

The payment reference number is a bank-generated value that allows the bank account owner to use their bank to locate funds. When the payment succeeds, Stripe provides the payment reference number in the Dashboard and inside the [Charge object](https://docs.stripe.com/api/charges/object.md).

| Charge State | Payment Reference Value                  |
| ------------ | ---------------------------------------- |
| Pending      | Unavailable                              |
| Failed       | Unavailable                              |
| Succeeded    | Available (for example, 091000015001234) |

In addition, when you receive the `charge.succeeded` webhook, view the content of `payment_method_details` to locate the [payment_reference](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-us_bank_account-payment_reference).

The following example event shows the rendering of a successful ACH payment with a payment reference number.

#### charge-succeeded

```json
{
  "id": "{{EVENT_ID}}",
  "object": "event",
  // omitted some fields in the example
  "type": "charge.succeeded",
  "data": {
    "object": {
      "id": "{{PAYMENT_ID}}",
      "object": "charge",
      //...
      "paid": true,
      "payment_intent": "{{PAYMENT_INTENT_ID}}",
      "payment_method": "{{PAYMENT_METHOD_ID}}",
      "payment_method_details": {
        "type": "us_bank_account",
        "us_bank_account": {
          "account_holder_type": "individual",
          "account_type": "checking",
          "bank_name": "TEST BANK",
          "fingerprint": "Ih3foEnRvLXShyfB",
          "last4": "1000",
          "payment_reference": "091000015001234",
          "routing_number": "110000000"
        }
      }
      // ...
    }
  }
}
```

View the contents of the `destination_details` to locate the [refund reference](https://docs.stripe.com/api/refunds/object.md#refund_object-destination_details-us_bank_transfer-reference) associated with the refunded ACH payments.

The following example event shows the rendering of a successful ACH refund with a refund reference number. Learn more about [refunds](https://docs.stripe.com/refunds.md).

#### charge-refund-updated

```json
{
  "id": "{{EVENT_ID}}",
  "object": "event",
  "type": "charge.refund.updated",
  "data": {
    "object": {
      "id": "{{REFUND_ID}}",
      "object": "refund",
      //...
      "payment_intent": "{{PAYMENT_INTENT_ID}}",
      "destination_details": {
        "type": "us_bank_transfer",
        "us_bank_transfer": {
          "reference": "091000015001111",
          "reference_status": "available"
        }
      }
      // ...
    }
  }
}
```

# Webview

> This is a Webview for when payment-ui is mobile and platform is webview. View the full page at https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment?payment-ui=mobile&platform=webview.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

> We recommend that you follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md) guide unless you need to use manual server-side confirmation, or your integration requires presenting payment methods separately. If you’ve already integrated with Elements, see the [Payment Element migration guide](https://docs.stripe.com/payments/payment-element/migration.md).

Accepting ACH Direct Debit payments in your app’s webview consists of:

- Creating an object to track a payment
- Handling potential OAuth redirects from the webview
- Collecting payment method information
- Submitting the payment to Stripe for processing
- Verifying your customer’s bank account

> ACH Direct Debit is a [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method, which means that funds aren’t immediately available after payment. A payment typically takes 4 business days to arrive in your account.

Stripe uses the payment object, the [Payment Intent](https://docs.stripe.com/payments/payment-intents.md), to track and handle all the states of the payment until the payment completes.

Before beginning, make sure that you have access to the ACH Direct Debit payment method beta. If you haven’t already been gated into the beta, reach out to your account manager to request access.

## Overview [Client-side]

To embed Financial Connections within a WebView, begin with one of our example WebView applications:

- [Android Webview](https://github.com/stripe/stripe-android/blob/master/financial-connections-example/src/main/java/com/stripe/android/financialconnections/example/FinancialConnectionsWebviewExampleActivity.kt)
- [iOS WKWebview](https://github.com/stripe/stripe-ios/blob/master/Example/FinancialConnections%20Example/FinancialConnections%20Example/WebViewViewController.swift)

These sample applications are fully functional (on both simulators and physical devices) and contain all necessary code to set up Financial Connections and handle events delivered to your application through HTTP redirect urls.

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

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
  contact_email: '{{CUSTOMER_EMAIL}}',
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

## Create a PaymentIntent [Server-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) is an object that represents your intent to collect payment from a customer and tracks the lifecycle of the payment process through each stage.

Create a PaymentIntent on your server:

1. Specify the amount to collect and `usd` as the currency.
1. Add `us_bank_account` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types).
1. Specify the [ID](https://docs.stripe.com/api/customers/object.md#customer_object-id) of the Customer.
1. Set the [data `permissions`](https://docs.stripe.com/financial-connections/fundamentals.md#data-permissions) parameter to include `payment_method`, as well as any other permissions required to fulfill your use case.
1. Set a `return_url` parameter, which you can use to redirect your customer back to your native app if they log into their bank with OAuth in the native browser.
   | iOS | Android |
   | --------------------------------------------------- | ----------------------------------------------------- |
   | The return_url needs to be an https universal link. | The return_url needs to be an https Android App Link. |
1. If you want to reuse the payment method in the future, provide the [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) parameter with the value of `off_session`.

The following code example demonstrates how to create a WebView-optimized [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) including the `payment_method` permission request:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'usd',
  setup_future_usage: "off_session",
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      financial_connections: {
        permissions: ['payment_method'],
        return_url: "https://stripe.com",
      },
    },
  },
});
```

### Retrieve the client secret

The PaymentIntent includes a _client secret_ (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)) that the client side uses to securely complete the payment process. You can use different approaches to pass the client secret to the client side.

#### Single-page application

Retrieve the client secret from an endpoint on your server, using the browser’s `fetch` function. This approach is best if your client side is a single-page application, particularly one built with a modern frontend framework like React. Create the server endpoint that serves the client secret:

#### Node.js

```javascript
const express = require("express");
const app = express();

app.get("/secret", async (req, res) => {
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
  const response = await fetch("/secret");
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
const express = require("express");
const expressHandlebars = require("express-handlebars");
const app = express();

app.engine(".hbs", expressHandlebars({ extname: ".hbs" }));
app.set("view engine", ".hbs");
app.set("views", "./views");

app.get("/checkout", async (req, res) => {
  const intent = // ... Fetch or create the PaymentIntent
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

Rather than sending the entire PaymentIntent object to the client, use its _client secret_ (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)) from the previous step. This is different from your API keys that authenticate Stripe API requests.

Handle the client secret carefully because it can complete the charge. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

Use [stripe.collectBankAccountForPayment](https://docs.stripe.com/js/payment_intents/collect_bank_account_for_payment) to collect bank account details with [Financial Connections](https://docs.stripe.com/financial-connections.md), create a _PaymentMethod_ (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs), and attach that PaymentMethod to the PaymentIntent. Including the account holder’s name in the `billing_details` parameter is required to create an ACH Direct Debit PaymentMethod.

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
    .collectBankAccountForPayment({
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
    .then(({ paymentIntent, error }) => {
      if (error) {
        console.error(error.message);
        // PaymentMethod collection failed for some reason.
      } else if (paymentIntent.status === "requires_payment_method") {
        // Customer canceled the hosted verification modal. Present them with other
        // payment method type options.
      } else if (paymentIntent.status === "requires_confirmation") {
        // We collected an account - possibly instantly verified, but possibly
        // manually-entered. Display payment method details and mandate text
        // to the customer and confirm the intent once they accept
        // the mandate.
        confirmationForm.show();
      }
    });
});
```

The [Financial Connections authentication flow](https://docs.stripe.com/financial-connections/fundamentals.md#authentication-flow) automatically handles bank account details collection and verification. When your customer completes the authentication flow, the _PaymentMethod_ (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) automatically attaches to the PaymentIntent, and creates a [Financial Connections Account](https://docs.stripe.com/api/financial_connections/accounts.md).

> Bank accounts that your customers link through manual entry and microdeposits won’t have access to additional bank account data like balances, ownership, and transactions.

To provide the best user experience on all devices, set the viewport `minimum-scale` for your page to 1 using the viewport `meta` tag.

```html
<meta name="viewport" content="width=device-width, minimum-scale=1" />
```

### Handle OAuth redirects on your mobile app

In addition to including Stripe.js on your webview-embedded page, your app might need to handle redirecting your customer to their native mobile browser for OAuth login.

> Beginning January 1, 2024, all webview-based integrations need to properly handle secure institution authentication and app redirects, or it will impact your Financial Connections authorization flow. Refer to the iOS or Android instructions above.

#### Android

On Android your app must register an [intent filter](https://developer.android.com/guide/components/intents-filters) for the previously set `return_url` in your manifest.

Read more about [handling links on Android](https://developer.android.com/training/app-links).

```xml
<activity
    android:name="...">

    <intent-filter>
        <action android:name="android.intent.action.VIEW" />
        <category android:name="android.intent.category.DEFAULT" />
        <category android:name="android.intent.category.BROWSABLE" />

        <!-- Data structure to listen for "https://stripe.com" URL -->
        <data android:scheme="http" />
        <data android:scheme="https" />

        <data android:host="stripe.com" />
    </intent-filter>
</activity>
```

Register a [WebViewClient](https://developer.android.com/reference/android/webkit/WebViewClient) on your WebView. You can override `shouldOverrideUrlLoading` to open OAuth login pages on a Custom Tab / secure browser instance:

```kotlin
val webViewClient = object : WebViewClient() {
  override fun shouldOverrideUrlLoading(
      view: WebView,
      webResourceRequest: WebResourceRequest
  ): Boolean {
      val url = webResourceRequest.url.toString()
      CustomTabsIntent.Builder().build().launchUrl(view.context, Uri.parse(url))
      return true
  }
}
// ...

// register the web view client on your WebView
myWebView.webViewClient = webViewClient
```

#### iOS

On iOS, your app must be equipped to handle the WebView’s attempt to open an OAuth window. This process involves attempting to open the URL in a bank app or, if unsupported, in a secure browser instance.

When the `WKWebView` intercepts a new window request, first attempt to open the URL as a universal link. Universal links allow banking apps installed on the user’s device to directly handle their associated URLs to simplify the authentication process. This method enhances user security and convenience by leveraging the existing, trusted apps already on the device.

If opening the URL as a universal link isn’t successful—either because no supporting bank app is installed or the link isn’t recognized—the app needs to fall back to using `ASWebAuthenticationSession`. This session facilitates the authentication flow within a secure, in-app browser that ensures the safe handling of sensitive information. `ASWebAuthenticationSession` mimics the native browser, allowing users to authenticate without leaving the app.

```swift
class ViewController: UIViewController {
  private var webAuthenticationSession: ASWebAuthenticationSession?

  override func viewDidLoad() {
      super.viewDidLoad()

      // Initialize and configure your WKWebView
      let webView = WKWebView(frame: .zero, configuration: WKWebViewConfiguration())

      // Load your website URL
      webView.load(URLRequest(url: URL(string: "https://yourwebsite.com")!))

      // Add the web view to the view
      view.addSubview(webView)

      // Important: Assign a `uiDelegate` to handle redirects
      webView.uiDelegate = self
  }
}

extension ViewController: WKUIDelegate {
  func webView(
      _ webView: WKWebView,
      createWebViewWith configuration: WKWebViewConfiguration,
      for navigationAction: WKNavigationAction,
      windowFeatures: WKWindowFeatures
  ) -> WKWebView? {
      // Check if the link is attempting to open in a new window.
      // This is typically the case for a banking partner's authentication flow.
      let isAttemptingToOpenLinkInNewWindow = navigationAction.targetFrame?.isMainFrame != true

      if isAttemptingToOpenLinkInNewWindow, let url = navigationAction.request.url {
          // Attempt to open the URL as a universal link.
          // Universal links allow apps on the device to handle specific URLs directly.
          UIApplication.shared.open(
              url,
              options: [.universalLinksOnly: true],
              completionHandler: { [weak self] success in
                  guard let self else { return }
                  if success {
                      // App-to-app flow:
                      // The URL was successfully opened in a banking application that supports universal links.
                      print("Successfully opened the authentication URL in a bank app: \(url)")
                  } else {
                      // Fallback for when no compatible bank app is found:
                      // Create an `ASWebAuthenticationSession` to handle the authentication in a secure in-app browser
                      self.launchInSecureBrowser(url: url)
                  }
              })
      }
      return nil
  }

  private func launchInSecureBrowser(url: URL) {
    let redirectURL = URL(string: "https://yourwebsite.com")!
    let webAuthenticationSession = ASWebAuthenticationSession(
        url: url,
        callbackURLScheme: redirectURL.scheme,
        completionHandler: { redirectURL, error in
            if let error {
                if
                    (error as NSError).domain == ASWebAuthenticationSessionErrorDomain,
                    (error as NSError).code == ASWebAuthenticationSessionError.canceledLogin.rawValue
                {
                    print("User manually closed the browser by pressing 'Cancel' at the top-left corner.")
                } else {
                    print("Received an error from ASWebAuthenticationSession: \(error)")
                }
            } else {
                // IMPORTANT NOTE:
                // The browser will automatically close when
                // the `callbackURLScheme` is called.
                print("Received a redirect URL: \(redirectURL?.absoluteString ?? "null")")
            }
        }
    )
    // Store the session reference to prevent premature deallocation
    self.webAuthenticationSession = webAuthenticationSession

    // Set the presentation context provider to handle the browser's UI presentation
    webAuthenticationSession.presentationContextProvider = self

    // Use an ephemeral session to enhance privacy
    // This also disables the initial Apple alert about signing in to another app
    webAuthenticationSession.prefersEphemeralWebBrowserSession = true

    // Initiate the authentication session
    webAuthenticationSession.start()
  }
}
```

After your customer logs into their institution and authorizes access to their accounts, Stripe redirects to the `return_url` to return to your app. After returning to the app, your customer can resume and complete the bank account detail collection process.

## Collect mandate acknowledgement and submit the payment [Client-side]

Before you can initiate the payment, you must obtain authorization from your customer by displaying mandate terms for them to accept.

To be compliant with Nacha rules, you must obtain authorization from your customer before you can initiate payment by displaying mandate terms for them to accept. For more information on mandates, see [Mandates](https://docs.stripe.com/payments/ach-direct-debit.md#mandates).

When the customer accepts the mandate terms, you must confirm the PaymentIntent. Use [stripe.confirmUsBankAccountPayment](https://docs.stripe.com/js/payment_intents/confirm_us_bank_account_payment) to complete the payment when the customer submits the form.

```javascript
confirmationForm.addEventListener("submit", (ev) => {
  ev.preventDefault();
  stripe
    .confirmUsBankAccountPayment(clientSecret)
    .then(({ paymentIntent, error }) => {
      if (error) {
        console.error(error.message);
        // The payment failed for some reason.
      } else if (paymentIntent.status === "requires_payment_method") {
        // Confirmation failed. Attempt again with a different payment method.
      } else if (paymentIntent.status === "processing") {
        // Confirmation succeeded! The account will be debited.
        // Display a message to customer.
      } else if (
        paymentIntent.next_action?.type === "verify_with_microdeposits"
      ) {
        // The account needs to be verified through microdeposits.
        // Display a message to consumer with next steps (consumer waits for
        // microdeposits, then enters a statement descriptor code on a page sent to them through email).
      }
    });
});
```

> [stripe.confirmUsBankAccountPayment](https://docs.stripe.com/js/payment_intents/confirm_us_bank_account_payment) might take several seconds to complete. During that time, disable resubmittals of your form and show a waiting indicator (for example, a spinner). If you receive an error, show it to the customer, re-enable the form, and hide the waiting indicator.

If successful, Stripe returns a PaymentIntent object, with one of the following possible statuses:

| Status            | Description                                                              | Next Steps                                                                                                                                                |
| ----------------- | ------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `requires_action` | Further action is needed to complete bank account verification.          | Step 6: [Verifying bank accounts with microdeposits](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md#web-verify-with-microdeposits) |
| `processing`      | The bank account was instantly verified or verification isn’t necessary. | Step 7: [Confirm the PaymentIntent succeeded](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md#web-confirm-paymentintent-succeeded)  |

After successfully confirming the PaymentIntent, an email confirmation of the mandate and collected bank account details must be sent to your customer. Stripe handles these by default, but you can choose to [send custom notifications](https://docs.stripe.com/payments/ach-direct-debit.md#mandate-and-microdeposit-emails) if you prefer.

## Verify bank account with microdeposits [Client-side]

Not all customers can verify the bank account instantly. This step only applies if your customer has elected to opt out of the instant verification flow in the previous step.

In these cases, Stripe sends a `descriptor_code` microdeposit and might fall back to an `amount` microdeposit if any further issues arise with verifying the bank account. These deposits take 1-2 business days to appear on the customer’s online statement.

- **Descriptor code**. Stripe sends a single, 0.01 USD microdeposit to the customer’s bank account with a unique, 6-digit `descriptor_code` that starts with SM. Your customer uses this string to verify their bank account.
- **Amount**. Stripe sends two, non-unique microdeposits to the customer’s bank account, with a statement descriptor that reads `ACCTVERIFY`. Your customer uses the deposit amounts to verify their bank account.

The result of the [stripe.confirmUsBankAccountPayment](https://docs.stripe.com/js/payment_intents/confirm_us_bank_account_payment) method call in the previous step is a PaymentIntent in the `requires_action` state. The PaymentIntent contains a `next_action` field that contains some useful information for completing the verification.

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

> Verification attempts have a limit of ten failures for descriptor-based microdeposits and three for amount-based ones. If you exceed this limit, we can no longer verify the bank account. In addition, microdeposit verifications have a timeout of 10 days. If you can’t verify microdeposits in that time, the PaymentIntent reverts to requiring new payment method details. Clear messaging about what these microdeposits are and how you use them can help your customers avoid verification issues.

### Optional: Send custom email notifications

Optionally, you can send [custom email notifications](https://docs.stripe.com/payments/ach-direct-debit.md#mandate-and-microdeposit-emails) to your customer. After you set up custom emails, you need to specify how the customer responds to the verification email. To do so, choose _one_ of the following:

- Use the Stripe-hosted verification page. To do this, use the `verify_with_microdeposits[hosted_verification_url]` URL in the [next_action](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-verify_with_microdeposits-hosted_verification_url) object to direct your customer to complete the verification process.

- If you prefer not to use the Stripe-hosted verification page, create a form on your site. Your customers then use this form to relay microdeposit amounts to you and verify the bank account using [Stripe.js](https://docs.stripe.com/js/payment_intents/verify_microdeposits_for_payment).
  - At minimum, set up the form to handle the `descriptor code` parameter, which is a 6-digit string for verification purposes.
  - Stripe also recommends that you set your form to handle the `amounts` parameter, as some banks your customers use might require it.

  Integrations only pass in the `descriptor_code` _or_ `amounts`. To determine which one your integration uses, check the value for `verify_with_microdeposits[microdeposit_type]` in the `next_action` object.

```javascript
stripe.verifyMicrodepositsForPayment(clientSecret, {
  // Provide either a descriptor_code OR amounts, not both
  descriptor_code: "SMT86W",
  amounts: [32, 45],
});
```

When the bank account is successfully verified, Stripe returns the PaymentIntent object with a `status` of `processing`, and sends a [payment_intent.processing](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.processing) _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event.

Verification can fail for several reasons. The failure might happen synchronously as a direct error response, or asynchronously through a [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.failed) webhook event (shown in the following examples).

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
      "message": "You have exceeded the number of allowed verification attempts.",
    },
    ...
    "status": "requires_payment_method"
  }
}
```

| Error Code                                                   | Synchronous or Asynchronous                            | Message                                                                                                                                         | Status change                                                           |
| ------------------------------------------------------------ | ------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `payment_method_microdeposit_failed`                         | Synchronously, or asynchronously through webhook event | Microdeposits failed. Please check the account, institution and transit numbers provided                                                        | `status` is `requires_payment_method`, and `last_payment_error` is set. |
| `payment_method_microdeposit_verification_amounts_mismatch`  | Synchronously                                          | The amounts provided don’t match the amounts that were sent to the bank account. You have {attempts_remaining} verification attempts remaining. | Unchanged                                                               |
| `payment_method_microdeposit_verification_attempts_exceeded` | Synchronously, or asynchronously through webhook event | Exceeded number of allowed verification attempts                                                                                                | `status` is `requires_payment_method`, and `last_payment_error` is set. |
| `payment_method_microdeposit_verification_timeout`           | Asynchronously through webhook event                   | Microdeposit timeout. Customer hasn’t verified their bank account within the required 10 day period.                                            | `status` is `requires_payment_method`, and `last_payment_error` is set. |

## Confirm the PaymentIntent succeeded [Server-side]

ACH Direct Debit is a [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method. This means that it can take up to four business days to receive notification of the success or failure of a payment after you initiate a debit from your customer’s account.

The PaymentIntent you create initially has a status of `processing`. After the payment has succeeded, the PaymentIntent status is updated from `processing` to `succeeded`.

We recommend using [webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks) to _confirm_ (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) the charge has succeeded and to notify the customer that the payment is complete. You can also view events on the [Stripe Dashboard](https://dashboard.stripe.com/events).

#### PaymentIntent events

The following events are sent when the PaymentIntent status is updated:

| Event                           | Description                                                                                     | Next Step                                                                                                                                                                                                                                                                                     |
| ------------------------------- | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_intent.processing`     | The customer’s payment was submitted to Stripe successfully.                                    | Wait for the initiated payment to succeed or fail.                                                                                                                                                                                                                                            |
| `payment_intent.succeeded`      | The customer’s payment succeeded.                                                               | Fulfill the goods or services that were purchased.                                                                                                                                                                                                                                            |
| `payment_intent.payment_failed` | The customer’s payment was declined. This can also apply to a failed microdeposit verification. | Contact the customer through email or push notification and request another payment method. If the webhook was sent due to a failed microdeposit verification, the user needs to enter in their bank account details again and a new set of microdeposits will be deposited in their account. |

#### Charge events

You may also use additional Charge webhooks to track the payment’s status. Upon receiving the `charge.updated` webhook, the payment is no longer cancellable.

The following events are sent when the Charge status is updated:

| Event              | Description                                                                                                                                     | Next Step                                                                         |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `charge.pending`   | The customer’s payment was created successfully.                                                                                                | Wait for the initiated payment to be processed.                                   |
| `charge.updated`   | The customer’s payment was updated. It can be emitted when a new balance transaction was created, a charge description or metadata got updated. | Wait for the initiated payment to succeed or fail.                                |
| `charge.succeeded` | The customer’s payment succeeded and the funds are available in your balance.                                                                   | Fulfill the goods or services that were purchased.                                |
| `charge.failed`    | The customer’s payment failed.                                                                                                                  | Check the charge’s failure_code and failure_message to determine further actions. |

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

Test transactions settle instantly and are added to your available test balance. This behavior differs from livemode, where transactions can take [multiple days](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md#timing) to settle in your available balance.

## Optional: Instant only verification [Server-side]

By default, US bank account payments allows your customers to use instant bank account verification or microdeposits. You can optionally require instant bank account verification only, using the [verification_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-us_bank_account-verification_method) parameter when you create the PaymentIntent.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'usd',
  setup_future_usage: "off_session",
  customer_account: '{{CUSTOMERACCOUNT_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      verification_method: 'instant',
      financial_connections: {
        permissions: ["payment_method", "balances"],
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
  currency: 'usd',
  setup_future_usage: "off_session",
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      verification_method: 'instant',
      financial_connections: {
        permissions: ["payment_method", "balances"],
      },
    },
  },
});
```

This ensures that you don’t need to handle microdeposit verification. However, if instant verification fails, the PaymentIntent’s status is `requires_payment_method`, indicating a failure to instantly verify a bank account for your customer.

## Optional: Microdeposit only verification [Server-side]

By default, US bank account payments allow your customers to use instant bank account verification or microdeposits. You can optionally require microdeposit verification only using the [verification_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-us_bank_account-verification_method) parameter when you create the PaymentIntent.

> If using a custom payment form, you must build your own UI to collect bank account details. If you disable Stripe microdeposit emails, you must build your own UI for your customer to confirm the microdeposit code or amount.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'usd',
  setup_future_usage: "off_session",
  customer_account: '{{CUSTOMERACCOUNT_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      verification_method: "microdeposits",
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
  currency: 'usd',
  setup_future_usage: "off_session",
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      verification_method: "microdeposits",
    },
  },
});
```

You must then collect your customer’s bank account with your own form and call [stripe.confirmUsBankAccountPayment](https://docs.stripe.com/js/payment_intents/confirm_us_bank_account_payment) with those details to complete the PaymentIntent.

```javascript
var form = document.getElementById("payment-form");
var accountholderName = document.getElementById("accountholder-name");
var email = document.getElementById("email");
var accountNumber = document.getElementById("account-number");
var routingNumber = document.getElementById("routing-number");
var accountHolderType = document.getElementById("account-holder-type");

var submitButton = document.getElementById("submit-button");
var clientSecret = submitButton.dataset.secret;

form.addEventListener("submit", function (event) {
  event.preventDefault();

  stripe
    .confirmUsBankAccountPayment(clientSecret, {
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
    .then(({ paymentIntent, error }) => {
      if (error) {
        // Inform the customer that there was an error.
        console.log(error.message);
      } else {
        // Handle next step based on the intent's status.
        console.log("PaymentIntent ID: " + paymentIntent.id);
        console.log("PaymentIntent status: " + paymentIntent.status);
      }
    });
});
```

## Optional: Retrieve balance information on a Financial Connections bank account

To help prevent payment failures due to insufficient funds, we recommend that you check a customer’s balance before initiating a payment. With your user’s permission, you can use Financial Connections to [access account balances](https://docs.stripe.com/financial-connections/balances.md).

## Optional: Payment Reference

The payment reference number is a bank-generated value that allows the bank account owner to use their bank to locate funds. When the payment succeeds, Stripe provides the payment reference number in the Dashboard and inside the [Charge object](https://docs.stripe.com/api/charges/object.md).

| Charge State | Payment Reference Value                  |
| ------------ | ---------------------------------------- |
| Pending      | Unavailable                              |
| Failed       | Unavailable                              |
| Succeeded    | Available (for example, 091000015001234) |

In addition, when you receive the `charge.succeeded` webhook, view the content of `payment_method_details` to locate the [payment_reference](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-us_bank_account-payment_reference).

The following example event shows the rendering of a successful ACH payment with a payment reference number.

#### charge-succeeded

```json
{
  "id": "{{EVENT_ID}}",
  "object": "event",
  // omitted some fields in the example
  "type": "charge.succeeded",
  "data": {
    "object": {
      "id": "{{PAYMENT_ID}}",
      "object": "charge",
      //...
      "paid": true,
      "payment_intent": "{{PAYMENT_INTENT_ID}}",
      "payment_method": "{{PAYMENT_METHOD_ID}}",
      "payment_method_details": {
        "type": "us_bank_account",
        "us_bank_account": {
          "account_holder_type": "individual",
          "account_type": "checking",
          "bank_name": "TEST BANK",
          "fingerprint": "Ih3foEnRvLXShyfB",
          "last4": "1000",
          "payment_reference": "091000015001234",
          "routing_number": "110000000"
        }
      }
      // ...
    }
  }
}
```

View the contents of the `destination_details` to locate the [refund reference](https://docs.stripe.com/api/refunds/object.md#refund_object-destination_details-us_bank_transfer-reference) associated with the refunded ACH payments.

The following example event shows the rendering of a successful ACH refund with a refund reference number. Learn more about [refunds](https://docs.stripe.com/refunds.md).

#### charge-refund-updated

```json
{
  "id": "{{EVENT_ID}}",
  "object": "event",
  "type": "charge.refund.updated",
  "data": {
    "object": {
      "id": "{{REFUND_ID}}",
      "object": "refund",
      //...
      "payment_intent": "{{PAYMENT_INTENT_ID}}",
      "destination_details": {
        "type": "us_bank_transfer",
        "us_bank_transfer": {
          "reference": "091000015001111",
          "reference_status": "available"
        }
      }
      // ...
    }
  }
}
```

## See also

- [Save ACH Direct Debit pre-authorized debit details for future payments](https://docs.stripe.com/payments/ach-direct-debit/set-up-payment.md)
