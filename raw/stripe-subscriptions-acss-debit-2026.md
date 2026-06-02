<!-- Source URL: https://docs.stripe.com/billing/subscriptions/acss-debit -->
<!-- Fetched: 2026-05-13 -->

# Set up a subscription with pre-authorized debit in Canada

Learn how to create and charge for a subscription with Canadian pre-authorized debits.

> Subscription mode in [Checkout](https://docs.stripe.com/payments/checkout.md) isn’t yet supported. To learn about early access when this feature is available, [contact us](mailto:payment-methods-feedback@stripe.com?subject=PADs%20Subscription%20Mode%20User%20Interest) to join the waitlist.

## Create a product and price [Dashboard]

[Products](https://docs.stripe.com/api/products.md) represent the item or service you’re selling. [Prices](https://docs.stripe.com/api/prices.md) define how much and how frequently you charge for a product. This includes how much the product costs, what currency you accept, and whether it’s a one-time or recurring charge. If you only have a few products and prices, create and manage them in the Dashboard.

This guide uses a stock photo service as an example and charges customers a 15 CAD monthly subscription. To model this:

1. Go to the [Products](https://dashboard.stripe.com/products?active=true) page and click **Create product**.
1. Enter a **Name** for the product. You can optionally add a **Description** and upload an image of the product.
1. Select a **Product tax code**. Learn more about [product tax codes](https://docs.stripe.com/tax/tax-codes.md).
1. Select **Recurring**. Then enter **15** for the price and select **CAD** as the currency.
1. Choose whether to **Include tax in price**. You can either use the default value from your [tax settings](https://dashboard.stripe.com/test/settings/tax) or set the value manually. In this example, select **Auto**.
1. Select **Monthly** for the **Billing period**.
1. Click **More pricing options**. Then select **Flat rate** as the pricing model for this example. Learn more about [flat rate](https://docs.stripe.com/products-prices/pricing-models.md#flat-rate) and other [pricing models](https://docs.stripe.com/products-prices/pricing-models.md).
1. Add an internal **Price description** and [Lookup key](https://docs.stripe.com/products-prices/manage-prices.md#lookup-keys) to organize, query, and update specific prices in the future.
1. Click **Next**. Then click **Add product**.

After you create the product and the price, record the price ID so you can use it in subsequent steps. The pricing page displays the ID and it looks similar to this: `price_G0FvDp6vZvdwRZ`.

## Create the subscription [Server-side]

> To create a subscription with a free trial period, see [Subscription trials](https://docs.stripe.com/billing/subscriptions/acss-debit.md#trial-periods).

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
    payment_method_types: ["acss_debit"],
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
    payment_method_types: ["acss_debit"],
  },
  expand: ["latest_invoice.payments", "latest_invoice.confirmation_secret"],
});

const client_secret =
  subscription.latest_invoice.confirmation_secret.client_secret;
```

The response includes the _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis)’s first [Invoice](https://docs.stripe.com/api/invoices.md). This contains the invoice’s payments, which includes a default PaymentIntent that Stripe generated for this invoice and the confirmation secret which you can use on the client side to securely complete the payment process instead of passing the entire PaymentIntent object. Return the `latest_invoice.confirmation_secret.client_secret` to the front end to complete payment.

## Collect payment method details and mandate acknowledgment [Client-side]

To use Canadian pre-authorized debits, you must obtain authorization from your customer for one-time and recurring debits using a pre-authorized debit agreement (see [PAD Mandates](https://docs.stripe.com/payments/acss-debit.md#mandates)). The [Mandate](https://docs.stripe.com/api/mandates.md) object records this agreement and authorization.

Stripe automatically configures subscription and _invoice_ (Invoices are statements of amounts owed by a customer. They track the status of payments from draft through paid or otherwise finalized. Subscriptions automatically generate invoices, or you can manually create a one-off invoice) mandates for you. The customer only needs to acknowledge the mandate terms once, subsequent subscription charges will succeed without further intervention.

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
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");
```

Rather than sending the entire PaymentIntent object to the client, use its _client secret_ (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)) from the previous step. This is different from your API keys that authenticate Stripe API requests.

The client secret should still be handled carefully because it can complete the charge. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

Use [stripe.confirmAcssDebitPayment](https://docs.stripe.com/js/payment_intents/confirm_acss_debit_payment) to collect bank account details and verification, confirm the mandate, and complete the payment when the user submits the form. Including the customer’s email address and the account holder’s name in the `billing_details` property of the `payment_method` parameter is required to create a PAD payment method.

```javascript
const form = document.getElementById("payment-form");
const accountholderName = document.getElementById("accountholder-name");
const email = document.getElementById("email");
const submitButton = document.getElementById("submit-button");
const clientSecret = submitButton.dataset.secret;

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const { paymentIntent, error } = await stripe.confirmAcssDebitPayment(
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
    // Handle next step based on PaymentIntent's status.
    console.log("PaymentIntent ID: " + paymentIntent.id);
    console.log("PaymentIntent status: " + paymentIntent.status);
  }
});
```

Stripe.js then loads an on-page modal UI that handles bank account details collection and verification, presents a hosted mandate agreement and collects authorization.

> `stripe.confirmAcssDebitPayment` might take several seconds to complete. During that time, disable your form from being resubmitted and show a waiting indicator like a spinner. If you receive an error, show it to the customer, re-enable the form, and hide the waiting indicator.

If the customer completes instant verification, the subscription automatically becomes `active`. Otherwise, consult the following section to handle micro-deposit verification while the subscription remains `incomplete`.

## Verify bank account with micro-deposits [Client-side]

> Customers have 10 days to successfully verify micro-deposits for a subscription, instead of the 23 hours normally given in the [subscription lifecycle](https://docs.stripe.com/billing/subscriptions/overview.md#subscription-lifecycle). However, this expiration can’t be later than the [billing period date](https://docs.stripe.com/billing/subscriptions/acss-debit.md#billing-cycle).

Not all customers can verify the bank account instantly. This step only applies if your customer has elected to opt out of the instant verification flow in the previous step.

In this case, Stripe automatically sends two micro-deposits to the customer’s bank account. These deposits take 1–2 business days to appear on the customer’s online statement and have statement descriptors that include `ACCTVERIFY`.

The result of the `stripe.confirmAcssDebitPayment` method call in the previous step is a PaymentIntent in the `requires_action` state. The PaymentIntent contains a `next_action` field that contains some useful information for completing the verification.

Stripe notifies your customer at the [billing email](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-billing_details-email) when the deposits are expected to arrive. The email includes a link to a Stripe-hosted verification page where they can confirm the amounts of the deposits and complete verification.

There is a limit of three failed verification attempts. If this limit is exceeded, the bank account can no longer be verified. In addition, there is a timeout for micro-deposit verifications of 10 days. If micro-deposits aren’t verified in that time, the PaymentIntent reverts to requiring new payment method details. Clear messaging about what these micro-deposits are and how you use them can help your customers avoid verification issues.

### Optional: Custom email and verification page

If you choose to send [custom email notifications](https://docs.stripe.com/payments/acss-debit.md#mandate-and-debit-notification-emails), you have to email your customer instead. To do this, you can use the `verify_with_microdeposits[hosted_verification_url]` URL in the `next_action` object to direct your customer to complete the verification process.

If you’re sending custom emails and don’t want to use the Stripe hosted verification page, you can create a form on your site for your customers to relay these amounts to you and verify the bank account using [Stripe.js](https://docs.stripe.com/js/payment_intents/verify_microdeposits_for_payment).

```javascript
stripe.verifyMicrodepositsForPayment(clientSecret, {
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

When the initial payment succeeds, the status of the subscription is `active` and requires no further action. When payments fail, the status changes to the **Subscription status** configured in your [automatic collection settings](https://docs.stripe.com/invoicing/automatic-collection.md). Notify the customer after a failure and [charge them with a different payment method](https://docs.stripe.com/billing/subscriptions/overview.md#requires-payment-method).

> Canadian pre-authorized debit payments are never automatically retried, even if you have a [retry schedule](https://docs.stripe.com/invoicing/automatic-collection.md) configured for other payment methods.

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

## Optional: Setting the billing period

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

Setting the billing cycle manually automatically charges the customer a prorated amount for the time between the subscription being created and the billing cycle anchor. If you don’t want to charge customers for this time, you can set the [proration_behavior](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-proration_behavior) argument to `none`. You can also combine the billing cycle anchor with [trial periods](https://docs.stripe.com/billing/subscriptions/acss-debit.md#trial-periods) to give users free access to your product and then charge them a prorated amount.

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
    payment_method_types: ["acss_debit"],
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
    payment_method_types: ["acss_debit"],
  },
  trial_end: 1610403705,
  expand: ["pending_setup_intent"],
});

const intent = subscription.pending_setup_intent;
```

Return the `client_secret` from the subscription’s `pending_setup_intent` to the frontend to complete the setup. This step is required to successfully initiate a charge for the first billing cycle.

Follow the instructions in [Collect payment method details and mandate acknowledgment](https://docs.stripe.com/billing/subscriptions/acss-debit.md#collect-payment-and-mandate) and [Verify bank account with micro-deposits](https://docs.stripe.com/billing/subscriptions/acss-debit.md#verify-with-microdeposits), but use `stripe.confirmAcssDebitSetup` instead of `stripe.confirmAcssDebitPayment`. If your customer chooses micro-deposit verification, use `stripe.verifyMicrodepositsForSetup` instead of `stripe.verifyMicrodepositsForPayment`.

The SetupIntent immediately transitions to `succeeded` status upon verification, and Stripe automatically sets the subscription’s `default_payment_method` to the newly created _PaymentMethod_ (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs).

You can also combine a [billing cycle anchor](https://docs.stripe.com/billing/subscriptions/acss-debit.md#billing-cycle) with a free trial. For example, on September 15 you want to give your customer a free trial for seven days and then start the normal billing period on October 1. You can set the free trial to end on September 22 and the billing cycle anchor to October 1. This gives the customer a free trial for seven days and then charges a prorated amount for the time between the trial ending and October 1. On October 1, you charge them the normal subscription amount for their first full billing period.

## Optional: Saving payment method details for future use

You might also want to save your customer’s Canadian pre-authorized debit payment method for automatic use with invoices, subscriptions, or subscription schedules that you create later.

You can do this using a [SetupIntent](https://docs.stripe.com/api/setup_intents.md) object, which represents your intent to save a customer’s payment method for future payments. The `SetupIntent` tracks the steps of this set-up process.

Follow the instructions for [Saving details for future payments with pre-authorized debit in Canada](https://docs.stripe.com/payments/acss-debit/set-up-payment.md), but provide a different set of `mandate_options` to collect authorization for subscriptions and invoices.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ["acss_debit"],
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  payment_method_options: {
    acss_debit: {
      currency: "cad",
      mandate_options: {
        default_for: ["invoice", "subscription"],
      },
    },
  },
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ["acss_debit"],
  customer: "{{CUSTOMER_ID}}",
  payment_method_options: {
    acss_debit: {
      currency: "cad",
      mandate_options: {
        default_for: ["invoice", "subscription"],
      },
    },
  },
});
```

After the `SetupIntent` reaches the `succeeded` state, update your customer’s default payment method in either [configuration.customer.billing.default_payment_method](https://docs.stripe.com/api/v2/core/accounts/update.md#v2_update_accounts-response-configuration-customer-billing-default_payment_method) (for customer-configured `Account` objects) or [invoice_settings.default_payment_method](https://docs.stripe.com/api/customers/update.md#update_customer-invoice_settings-default_payment_method) (for `Customer` objects).

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
