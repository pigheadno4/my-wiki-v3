<!-- Source URL: https://docs.stripe.com/billing/subscriptions/ach-debit -->
<!-- Fetched: 2026-05-13 -->

# Set up a subscription with ACH Direct Debit

Learn how to create and charge for a subscription with US bank account.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

Use this guide to set up a _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) using [ACH Direct Debit](https://docs.stripe.com/payments/ach-direct-debit.md).

# Advanced integration

> This is a Advanced integration for when platform is web and payment-ui is elements. View the full page at https://docs.stripe.com/billing/subscriptions/ach-debit?platform=web&payment-ui=elements.

> If you’re a new user, use the [Payment Element](https://docs.stripe.com/payments/payment-element.md) instead of using Stripe Elements as described in this guide. The Payment Element provides a low-code integration path with built-in conversion optimizations. For instructions, see [Build a subscription](https://docs.stripe.com/billing/subscriptions/build-subscriptions.md?payment-ui=elements).

## Create a product and price [Dashboard]

[Products](https://docs.stripe.com/api/products.md) represent the item or service you’re selling. [Prices](https://docs.stripe.com/api/prices.md) define how much and how frequently you charge for a product. This includes how much the product costs, what currency you accept, and whether it’s a one-time or recurring charge. If you only have a few products and prices, create and manage them in the Dashboard.

This guide uses a stock photo service as an example and charges customers a 15 USD monthly subscription. To model this:

1. Go to the [Products](https://dashboard.stripe.com/products?active=true) page and click **Create product**.
1. Enter a **Name** for the product. You can optionally add a **Description** and upload an image of the product.
1. Select a **Product tax code**. Learn more about [product tax codes](https://docs.stripe.com/tax/tax-codes.md).
1. Select **Recurring**. Then enter **15** for the price and select **USD** as the currency.
1. Choose whether to **Include tax in price**. You can either use the default value from your [tax settings](https://dashboard.stripe.com/test/settings/tax) or set the value manually. In this example, select **Auto**.
1. Select **Monthly** for the **Billing period**.
1. Click **More pricing options**. Then select **Flat rate** as the pricing model for this example. Learn more about [flat rate](https://docs.stripe.com/products-prices/pricing-models.md#flat-rate) and other [pricing models](https://docs.stripe.com/products-prices/pricing-models.md).
1. Add an internal **Price description** and [Lookup key](https://docs.stripe.com/products-prices/manage-prices.md#lookup-keys) to organize, query, and update specific prices in the future.
1. Click **Next**. Then click **Add product**.

After you create the product and the price, record the price ID so you can use it in subsequent steps. The pricing page displays the ID and it looks similar to this: `price_G0FvDp6vZvdwRZ`.

## Create the subscription [Server-side]

> To create a _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) with a free trial period, see [Subscription trials](https://docs.stripe.com/billing/subscriptions/ach-debit.md#trial-periods).

Create a [subscription](https://docs.stripe.com/api/subscriptions.md) with the price and customer with status `incomplete` by providing the [payment_behavior](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-payment_behavior) parameter with the value of `default_incomplete`.

#### Accounts v2

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer_account: customer_account.id,
  items: [
    {
      price: "price_FSDjyHWis0QVwl",
    },
  ],
  payment_behavior: "default_incomplete",
  payment_settings: {
    payment_method_types: ["us_bank_account"],
  },
  expand: ["latest_invoice.payments", "latest_invoice.confirmation_secret"],
});

const client_secret =
  subscription.latest_invoice.confirmation_secret.client_secret;
```

#### Customers v1

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer: customer.id,
  items: [
    {
      price: "price_FSDjyHWis0QVwl",
    },
  ],
  payment_behavior: "default_incomplete",
  payment_settings: {
    payment_method_types: ["us_bank_account"],
  },
  expand: ["latest_invoice.payments", "latest_invoice.confirmation_secret"],
});

const client_secret =
  subscription.latest_invoice.confirmation_secret.client_secret;
```

The response includes the _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis)’s first [Invoice](https://docs.stripe.com/api/invoices.md). This contains the invoice’s payments, which includes a default PaymentIntent that Stripe generated for this invoice and the confirmation secret which you can use on the client side to securely complete the payment process instead of passing the entire PaymentIntent object. Return the `latest_invoice.confirmation_secret.client_secret` to the front end to complete payment.

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

## Collect mandate acknowledgement and submit [Client-side]

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

If the customer completes instant verification, the subscription automatically becomes `active`. Otherwise, see [Verify bank account with microdeposits](https://docs.stripe.com/billing/subscriptions/ach-debit.md#verify-with-microdeposits) to learn how to handle microdeposit verification while the subscription remains `incomplete`.

## Verify bank account with microdeposits [Client-side]

> Customers have 10 days to successfully verify microdeposits for a subscription, instead of the 23 hours normally given in the [subscription lifecycle](https://docs.stripe.com/billing/subscriptions/overview.md#subscription-lifecycle). However, this expiration can’t be later than the [billing cycle date](https://docs.stripe.com/billing/subscriptions/ach-debit.md#billing-cycle).

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

## Set the default payment method [Server]

You now have an active _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) belonging to a customer with a payment method, but this payment method isn’t automatically used for future payments. To automatically bill this payment method in the future, use a _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) consumer to listen to the `invoice.payment_succeeded` event for new subscriptions and set the default payment method.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

if (event.type == "invoice.payment_succeeded") {
  const invoice = event.data.object;
  if (invoice.billing_reason == "subscription_create") {
    const subscription_id = invoice.parent.subscription_details.subscription;

    // This example assumes you're using the default PaymentIntent that Stripe generated for the invoice
    const invoice_payments = await stripe.invoicePayments.list({
      invoice: invoice.id,
    });
    const payment_intent_id = invoice_payments.data[0].payment.payment_intent;

    // Retrieve the payment intent used to pay the subscription
    const payment_intent =
      await stripe.paymentIntents.retrieve(payment_intent_id);

    const subscription = await stripe.subscriptions.update(subscription_id, {
      default_payment_method: payment_intent.payment_method,
    });
  }
}
```

## Manage subscription status [Client-side]

Assuming the initial payment succeeds, the state of the subscription is `active` and requires no further action. When payments fail, the status changes to the **Subscription status** configured in your [automatic collection settings](https://docs.stripe.com/invoicing/automatic-collection.md). Notify the customer upon failure and [charge them with a different payment method](https://docs.stripe.com/billing/subscriptions/overview.md#requires-payment-method).

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

Test transactions settle instantly and are added to your available test balance. This behavior differs from livemode, where transactions can take [multiple days](https://docs.stripe.com/billing/subscriptions/ach-debit.md#timing) to settle in your available balance.

## Optional: Setting the billing cycle

When you create a subscription, it automatically sets the billing cycle by default. For example, if a customer subscribes to a monthly plan on September 7, they’re billed on the 7th of every month after that. Some businesses prefer to set the billing cycle manually so that they can charge their customers at the same time each cycle. The [billing cycle anchor](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-billing_cycle_anchor) argument allows you to do this.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  items: [
    {
      price: "{{PRICE_ID}}",
    },
  ],
  billing_cycle_anchor: 1611008505,
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer: "{{CUSTOMER_ID}}",
  items: [
    {
      price: "{{PRICE_ID}}",
    },
  ],
  billing_cycle_anchor: 1611008505,
});
```

Setting the billing cycle manually automatically charges the customer a prorated amount for the time between the subscription being created and the billing cycle anchor. If you don’t want to charge customers for this time, you can set the [proration_behavior](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-proration_behavior) argument to `none`. You can also combine the billing cycle anchor with [trial periods](https://docs.stripe.com/billing/subscriptions/ach-debit.md#trial-periods) to give users free access to your product and then charge them a prorated amount.

## Optional: Subscription trials

Free trials allow customers access to your product for a period of time without charging them. To set a trial period, pass a timestamp in [trial_end](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-trial_end) .

> Using free trials is different from setting [proration_behavior](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-proration_behavior) to `none` because you can customize how long the free period lasts.

When you start a subscription with a trial period using the [payment_behavior](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-payment_behavior) value `default_incomplete`, Stripe returns a `pending_setup_intent` value in the Subscription object. Read the docs to learn more about the [SetupIntent](https://docs.stripe.com/api/setup_intents.md) object.

#### Accounts v2

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer_account: "acct_4fdAW5ftNQow1a",
  items: [
    {
      price: "price_CBb6IXqvTLXp3f",
    },
  ],
  payment_behavior: "default_incomplete",
  payment_settings: {
    payment_method_types: ["us_bank_account"],
  },
  trial_end: 1610403705,
  expand: ["pending_setup_intent"],
});

const intent = subscription.pending_setup_intent;
```

#### Customers v1

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer: "cus_4fdAW5ftNQow1a",
  items: [
    {
      price: "price_CBb6IXqvTLXp3f",
    },
  ],
  payment_behavior: "default_incomplete",
  payment_settings: {
    payment_method_types: ["us_bank_account"],
  },
  trial_end: 1610403705,
  expand: ["pending_setup_intent"],
});

const intent = subscription.pending_setup_intent;
```

Return the `client_secret` from the subscription’s `pending_setup_intent` to the frontend to complete the setup. This step is required to successfully initiate a charge for the first billing cycle.

Follow the instructions in [Collect payment method details](https://docs.stripe.com/billing/subscriptions/ach-debit.md#collect-payment-details), [Collect mandate acknowledgement and submit](https://docs.stripe.com/billing/subscriptions/ach-debit.md#collect-mandate-and-submit), and [Verify bank account with microdeposits](https://docs.stripe.com/billing/subscriptions/ach-debit.md#verify-with-microdeposits), with two differences:

- Use `stripe.collectBankAccountForSetup` instead of `stripe.collectBankAccountForPayment`.
- Use `stripe.confirmUsBankAccountSetup` instead of `stripe.confirmUsBankAccountPayment`.

If your customer chooses microdeposit verification, use `stripe.verifyMicrodepositsForSetup` instead of `stripe.verifyMicrodepositsForPayment`.

The SetupIntent immediately transitions to `succeeded` status upon verification, and Stripe automatically sets the subscription’s `default_payment_method` to the newly created _PaymentMethod_ (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs).

You can also combine a [billing cycle anchor](https://docs.stripe.com/billing/subscriptions/ach-debit.md#billing-cycle) with a free trial. For example, on September 15 you want to give your customer a free trial for seven days and then start the normal billing cycle on October 1. You can set the free trial to end on September 22 and the billing cycle anchor to October 1. This gives the customer a free trial for seven days and then charges a prorated amount for the time between the trial ending and October 1. On October 1, you charge them the normal subscription amount for their first full billing cycle.

## Optional: Saving payment method details for future use

You can save your customer’s US bank account details for automatic use with _invoices_ (Invoices are statements of amounts owed by a customer. They track the status of payments from draft through paid or otherwise finalized. Subscriptions automatically generate invoices, or you can manually create a one-off invoice), subscriptions, or subscription schedules that you create later. To do this, use a [SetupIntent](https://docs.stripe.com/api/setup_intents.md) object, which represents your intent to save a customer’s payment method for future payments.

Follow the instructions for [Saving US bank account details for future payments](https://docs.stripe.com/payments/ach-direct-debit/set-up-payment.md).

After the `SetupIntent` reaches the `succeeded` state, update your customer’s `default_payment_method`.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

if (event.type == "setup_intent.succeeded") {
  const setup_intent = event.data.object;
  const customer_id = setup_intent.customer;
  const payment_method_id = setup_intent.payment_method;

  const customer = await stripe.customers.update(customer_id, {
    invoice_settings: { default_payment_method: payment_method_id },
  });
}
```

# Full hosted page

> This is a Full hosted page for when platform is web and payment-ui is stripe-hosted. View the full page at https://docs.stripe.com/billing/subscriptions/ach-debit?platform=web&payment-ui=stripe-hosted.

If your Stripe Checkout integration allows customers to create subscriptions in a [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md), you can add a US bank account as a payment method.

A [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md) represents the details of a customer’s intent to purchase. Create a Checkout Session when a customer wants to start a subscription. After redirecting a customer to a Checkout Session, Stripe presents a payment form where they can complete their purchase. After they complete a purchase, Stripe redirects them back to your site.

After you complete the integration, you can extend it to:

- [Add multiple prices](https://docs.stripe.com/products-prices/how-products-and-prices-work.md#multiple-prices)
- [Create variable pricing](https://docs.stripe.com/products-prices/how-products-and-prices-work.md#variable-pricing)
- [Handle existing customers](https://docs.stripe.com/payments/existing-customers.md?platform=web&ui=stripe-hosted)
- [Handle trials](https://docs.stripe.com/billing/subscriptions/trials.md)
- [Collect taxes](https://docs.stripe.com/billing/taxes/collect-taxes.md?tax-calculation=tax-rates)
- [Create billing coupons](https://docs.stripe.com/billing/subscriptions/coupons.md)

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create the pricing model [Dashboard] [Stripe CLI]

[Recurring pricing models](https://docs.stripe.com/products-prices/pricing-models.md) represent the products or services you sell, how much they cost, what currency you accept for payments, and the service period for subscriptions. To build the pricing model, create [products](https://docs.stripe.com/api/products.md) (what you sell) and [prices](https://docs.stripe.com/api/prices.md) (how much and how often to charge for your products).

This example uses flat-rate pricing with two different service-level options: Basic and Premium. For each service-level option, you need to create a product and a recurring price. To add a one-time charge for something like a setup fee, create a third product with a one-time price.

Each product bills at monthly intervals. The price for the Basic product is 5 USD. The price for the Premium product is 15 USD. See the [flat rate pricing](https://docs.stripe.com/subscriptions/pricing-models/flat-rate-pricing.md) guide for an example with three tiers.

#### Dashboard

Go to the [Add a product](https://dashboard.stripe.com/test/products/create) page and create two products. Add one price for each product, each with a monthly recurring billing period:

- Premium product: Premium service with extra features
  - Price: Flat rate | 15 USD

- Basic product: Basic service with minimum features
  - Price: Flat rate | 5 USD

After you create the prices, record the price IDs so you can use them in other steps. Price IDs look like this: `price_G0FvDp6vZvdwRZ`.

When you’re ready, use the **Copy to live mode** button at the top right of the page to clone your product from [a sandbox to live mode](https://docs.stripe.com/keys.md#test-live-modes).

#### API

You can use the API to create the [Products](https://docs.stripe.com/api/products.md) and [Prices](https://docs.stripe.com/api/prices.md).

Create the Premium product:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const product = await stripe.products.create({
  name: "Billing Guide: Premium Service",
  description: "Premium service with extra features",
});
```

Create the Basic product:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const product = await stripe.products.create({
  name: "Billing Guide: Basic Service",
  description: "Basic service with minimum features",
});
```

Record the product ID for each product. They look like this:

```json
{
  "id": "prod_H94k5odtwJXMtQ",
  "object": "product",
  "active": true,
  "attributes": [],
  "created": 1587577341,
  "description": "Premium service with extra features",
  "images": [],
  "livemode": false,
  "metadata": {},
  "name": "Billing Guide: Premium Service",
  "statement_descriptor": null,
  "type": "service",
  "unit_label": null,
  "updated": 1587577341
}
```

Use the product IDs to create a price for each product. The [unit_amount](https://docs.stripe.com/api/prices/object.md#price_object-unit_amount) number is in cents, so `1500` = 15 USD, for example.

Create the Premium price:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const price = await stripe.prices.create({
  product: "{{PREMIUM_PRODUCT_ID}}",
  unit_amount: 1500,
  currency: "usd",
  recurring: {
    interval: "month",
  },
});
```

Create the Basic price:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const price = await stripe.prices.create({
  product: "{{BASIC_PRODUCT_ID}}",
  unit_amount: 500,
  currency: "usd",
  recurring: {
    interval: "month",
  },
});
```

Record the price ID for each price so you can use them in subsequent steps. They look like this:

```json
{
  "id": "price_HGd7M3DV3IMXkC",
  "object": "price",
  "product": "prod_HGd6W1VUqqXGvr",
  "type": "recurring",
  "currency": "usd",
  "recurring": {
    "interval": "month",
    "interval_count": 1,
    "trial_period_days": null,
    "usage_type": "licensed"
  },
  "active": true,
  "billing_scheme": "per_unit",
  "created": 1589319695,
  "livemode": false,
  "lookup_key": null,
  "metadata": {},
  "nickname": null,
  "unit_amount": 1500,
  "unit_amount_decimal": "1500",
  "tiers": null,
  "tiers_mode": null,
  "transform_quantity": null
}
```

See examples of other [pricing models](https://docs.stripe.com/products-prices/pricing-models.md).

## Create a Checkout Session [Client-side] [Server-side]

Add a checkout button to your website that calls a server-side endpoint to create a Checkout Session.

```html
<html>
  <head>
    <title>Checkout</title>
  </head>
  <body>
    <form action="/create-checkout-session" method="POST">
      <button type="submit">Checkout</button>
    </form>
  </body>
</html>
```

### Checkout Session parameters

For a complete list of all the parameters you can use, see [Create a Session](https://docs.stripe.com/api/checkout/sessions/create.md).

Create a Checkout Session with the ID of an existing [Price](https://docs.stripe.com/api/prices.md). Make sure that the mode is set to `subscription` and you pass at least one recurring price. You can add one-time prices in addition to recurring prices. After creating the Checkout Session, redirect your customer to the [URL](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-url) returned in the response.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  payment_method_types: ["us_bank_account"],

  // or you can take multiple payment methods with
  // payment_method_types: ['card', 'us_bank_account', ...]
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  mode: "subscription",
  success_url: "https://example.com/success?session_id={CHECKOUT_SESSION_ID}",
});

// Record the session ID in your system
const session_id = session.id;

// 303 redirect to session.url
```

When your customer successfully completes their payment, they’re redirected to the `success_url`, a page on your website that informs them that their payment was successful. Make the Session ID available on your success page by including the `{CHECKOUT_SESSION_ID}` template variable in the `success_url` as in the above example.

Checkout Sessions expire 24 hours after creation by default.

> Don’t rely on the redirect to the `success_url` alone for detecting payment initiation, because:
>
> - Malicious users could directly access the `success_url` without paying and gain access to your goods or services.

- After a successful payment, customers might close their browser tab before they’re redirected to the `success_url`.

## Confirm the payment is successful

When your customer completes a payment, Stripe redirects them to the URL that you specified in the `success_url` parameter. Typically, this is a page on your website that informs your customer that their payment was successful.

However, US bank account debit is a delayed notification payment method, which means that funds aren’t immediately available. Because of this, delay order _fulfillment_ (Fulfillment is the process of providing the goods or services purchased by a customer, typically after payment is collected) until the funds are available. After the payment succeeds, the underlying _PaymentIntent_ (The Payment Intents API tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by regulatory mandates, custom Radar fraud rules, or redirect-based payment methods) status changes from `processing` to `succeeded`.

A US bank account debit payment typically takes four days to make the funds available.

You can confirm the payment is successful in several ways:

#### Dashboard

Successful payments display in the Dashboard’s [list of payments](https://dashboard.stripe.com/payments). When you click a payment, it takes you to the payment details page. The **Checkout summary** section contains billing information and the list of items purchased, which you can use to manually fulfill the order.
![](assets/stripe-ach-checkout-success.png)

> Stripe can help you keep up with incoming payments by sending you email notifications whenever a customer successfully completes one. Use the Dashboard to [configure email notifications](https://dashboard.stripe.com/settings/user).

#### Webhooks

We send the following Checkout events when the payment status changes:

| Event Name                                                                                                                                   | Description                                                                                 | Next steps                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| [checkout.session.completed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.completed)                             | The customer has successfully authorized the debit payment by submitting the Checkout form. | Wait for the payment to succeed or fail.                                            |
| [checkout.session.async_payment_succeeded](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.async_payment_succeeded) | The delayed payment method eventually succeeded.                                            | Fulfill the goods or services that the customer purchased.                          |
| [checkout.session.async_payment_failed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.async_payment_failed)       | The delayed payment method eventually failed.                                               | Email the customer and request that they attempt the payment again.                 |
| [invoice.paid](https://docs.stripe.com/api/events/types.md#event_types-invoice.paid)                                                         | The customer’s payment succeeded.                                                           | Fulfill the goods or services that the customer purchased.                          |
| [invoice.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-invoice.payment_failed)                                     | The customer’s payment was declined, or failed for some other reason.                       | Contact the customer through email and request that they attempt the payment again. |

Your webhook code needs to handle all of these Checkout events.

Each Checkout webhook payload includes the [Checkout Session object](https://docs.stripe.com/api/checkout/sessions.md) and invoice webhooks include the [Invoice](https://docs.stripe.com/api/invoices/object.md) object. Both contain information about the customer and _PaymentIntent_ (The Payment Intents API tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by regulatory mandates, custom Radar fraud rules, or redirect-based payment methods).

Stripe sends the `checkout.session.completed` webhook to your server before redirecting your customer. Your webhook acknowledgement (any `2xx` status code) triggers the customer’s redirect to the `success_url`. If Stripe doesn’t receive successful acknowledgement within 10 seconds of a successful payment, your customer automatically redirects to the `success_url` page.

On your `success_url` page, show a success message to your customer, and let them know that fulfillment of the order will take up to four days as the US bank account debit payment method isn’t instant.

We recommend [using webhooks](https://docs.stripe.com/webhooks.md) to confirm the payment has succeeded and fulfill the goods or services the customer purchased. Below is an example webhook endpoint that handles the success or failure of a payment:

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

// Find your endpoint's secret in your Dashboard's webhook settings
const endpointSecret = "whsec_...";

// Using Express
const app = require("express")();

// Use body-parser to retrieve the raw body as a buffer
const bodyParser = require("body-parser");

// Match the raw body to content type application/json
app.post(
  "/webhook",
  bodyParser.raw({ type: "application/json" }),
  (request, response) => {
    const sig = request.headers["stripe-signature"];

    let event;

    try {
      event = stripe.webhooks.constructEvent(request.body, sig, endpointSecret);
    } catch (err) {
      return response.status(400).send(`Webhook Error: ${err.message}`);
    }

    switch (event.type) {
      case "checkout.session.completed": {
        const session = event.data.object;
        const subscriptionId = session.subscription;

        // Find the subscription or save it to your database.
        // invoice.paid may have fired before this so there
        // could already be a subscription.
        findOrCreateSubscription(subscriptionId);

        break;
      }

      case "invoice.paid": {
        const invoice = event.data.object;
        const subscriptionId = invoice.parent.subscription_details.subscription;

        // Find the subscription or save it to your database.
        // checkout.session.completed may not have fired yet
        // so we may need to create the subscription.
        const subscription = findOrCreateSubscription(subscriptionId);

        // Fulfill the purchase
        fulfillOrder(invoice);

        // Record that the subscription has been paid for
        // this payment period. invoice.paid will fire every
        // time there is a payment made for this subscription.
        recordAsPaidForThisPeriod(subscription);

        break;
      }

      case "invoice.payment_failed": {
        const invoice = event.data.object;

        // Send an email to the customer asking them to retry their payment
        emailCustomerAboutFailedPayment(invoice);

        break;
      }
    }

    // Return a response to acknowledge receipt of the event
    response.json({ received: true });
  },
);
```

Get information about the customer, payment, or subscription by retrieving the objects referenced by the `customer` or `customer_account`, `payment_intent`, and `subscription` properties in the webhook payload.

### Retrieving line items from webhook

By default, Checkout webhooks don’t return `line_items`. To retrieve the items created with the Checkout Session, make an additional request with the Checkout Session id:

#### curl

```bash
curl https://api.stripe.com/v1/checkout/sessions/{{CHECKOUT_SESSION_ID}}/line_items \
  -u <<YOUR_SECRET_KEY>>:
```

#### Stripe CLI

```bash
stripe get /v1/checkout/sessions/{{CHECKOUT_SESSION_ID}}/line_items
```

### Testing webhooks locally

To test webhooks locally, you can use the [Stripe CLI](https://docs.stripe.com/stripe-cli.md). After you install it, you can forward events to your server:

```bash
stripe listen --forward-to localhost:4242/webhook
Ready! Your webhook signing secret is '{{WEBHOOK_SIGNING_SECRET}}' (^C to quit)
```

Learn more about [setting up webhooks](https://docs.stripe.com/webhooks.md).

#### Third-party plugins

You can use plugins such as [Zapier](https://stripe.com/works-with/zapier) to automate updating your purchase fulfillment systems with information from Stripe payments.

Some examples of automation supported by plugins include:

- Updating spreadsheets used for order tracking in response to successful payments
- Updating inventory management systems in response to successful payments
- Triggering notifications to internal customer service teams using email or chat applications

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

Test transactions settle instantly and are added to your available test balance. This behavior differs from livemode, where transactions can take [multiple days](https://docs.stripe.com/billing/subscriptions/ach-debit.md#timing) to settle in your available balance.

## Additional considerations

### Microdeposit verification failure

When a bank account is pending verification with microdeposits, the customer can fail to verify for three reasons:

- The microdeposits failed to send to the customer’s bank account (this usually indicates a closed or unavailable bank account or incorrect bank account number).
- The customer made 10 failed verification attempts for the account. Exceeding this limit means the bank account can no longer be verified or reused.
- The customer failed to verify the bank account within 10 days.

If the bank account fails verification for one of these reasons, you can [handle the `checkout.session.async_payment_failed` event](https://docs.stripe.com/api/events/types.md?event_types-invoice.payment_succeeded=#event_types-checkout.session.async_payment_failed) to contact the customer about placing a new order.

## Optional: Instant only verification

By default, ACH Direct Debit payments allow your customers to use instant bank account verification or microdeposits. You can optionally require instant bank account verification only, using the `payment_method_options[us_bank_account][verification_method]` parameter when you create the Checkout session.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  mode: "subscription",
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  payment_method_types: ["card", "us_bank_account"],
  payment_method_options: {
    us_bank_account: {
      verification_method: "instant",
      financial_connections: {
        permissions: ["payment_method"],
      },
    },
  },
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  success_url: "https://example.com/success",
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  mode: "subscription",
  customer: "{{CUSTOMER_ID}}",
  payment_method_types: ["card", "us_bank_account"],
  payment_method_options: {
    us_bank_account: {
      verification_method: "instant",
      financial_connections: {
        permissions: ["payment_method"],
      },
    },
  },
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  success_url: "https://example.com/success",
});
```

## See also

- [Customize your integration](https://docs.stripe.com/payments/checkout/customization.md)
- [Manage subscriptions with the customer portal](https://docs.stripe.com/billing/subscriptions/build-subscriptions.md?payment-ui=checkout&ui=stripe-hosted)
