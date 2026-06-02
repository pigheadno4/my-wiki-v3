<!-- Source URL: https://docs.stripe.com/billing/subscriptions/bank-transfers -->
<!-- Fetched: 2026-05-13 -->

# Set up a subscription with bank transfers

Learn how to create and charge for a subscription with bank transfers.

Use this guide to set up a _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) using [bank transfers](https://docs.stripe.com/payments/bank-transfers.md) as a payment method.

## Create a product and price [Dashboard] [Server-side]

_Products_ (Products represent what your business sells—whether that's a good or a service) and _Prices_ (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) are core resources for Subscriptions. [Create a product and a recurring price](https://docs.stripe.com/products-prices/manage-prices.md#create-product). Save the price ID—you’ll need it later in this guide.

## Create or retrieve a customer [Server-side]

To start, create a customer (either a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-configuration-customer) object or a [Customer](https://docs.stripe.com/api/customers/object.md) object) with a valid email address, if one doesn’t already exist. The valid email address ensures that the customer can receive invoices you send to them.

#### Accounts v2

Funds from bank transfers are held in the customer’s [cash balance](https://docs.stripe.com/payments/customer-balance.md), so you have to associate a customer with each bank transfer subscription. To manage the cash balance for a customer-configured `Account`, use the Customers API endpoint with the Account ID as the path parameter, for example `v1/customers/acct_xxxxx/cash_balances`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const account = await stripe.v2.core.accounts.create({
  contact_email: "jenny.rosen@example.com",
  display_name: "Jenny Rosen",
  configuration: {
    customer: {},
  },
  include: ["configuration.customer"],
});
```

#### Customers v1

Funds from bank transfers are held in the customer’s [cash balance](https://docs.stripe.com/payments/customer-balance.md), so you have to associate a [Customer](https://docs.stripe.com/api/customers.md) object with each bank transfer subscription.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create({
  name: "Jenny Rosen",
  email: "jenny.rosen@example.com",
});
```

## Create the subscription [Server-side]

[Create](https://docs.stripe.com/api/subscriptions/create.md) the subscription using the customer ID and price ID from the previous steps.

- Set [collection_method](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-collection_method) to `send_invoice`.
- Set [days_until_due](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-days_until_due) to configure how many days the customer has to pay the _invoice_ (Invoices are statements of amounts owed by a customer. They track the status of payments from draft through paid or otherwise finalized. Subscriptions automatically generate invoices, or you can manually create a one-off invoice).

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer_account: "{{CUSTOMER_ACCOUNT_ID}}",
  items: [
    {
      price: "{{PRICE_ID}}",
    },
  ],
  collection_method: "send_invoice",
  days_until_due: 30,
  payment_settings: {
    payment_method_types: ["customer_balance"],
  },
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
  collection_method: "send_invoice",
  days_until_due: 30,
  payment_settings: {
    payment_method_types: ["customer_balance"],
  },
});
```

An invoice is sent to the customer when the Subscription is due. The invoice is marked as paid if the customer has enough funds in their [cash balance](https://docs.stripe.com/payments/customer-balance.md). Otherwise, it contains the necessary information needed for the customer to push funds from their bank account. This invoice also has a link to the [Hosted Invoice Page](https://docs.stripe.com/invoicing/hosted-invoice-page.md). Subsequent invoices use the price you created in the first step.

Learn more about [bank transfer invoices](https://docs.stripe.com/invoicing/bank-transfer.md).

## Optional: Create a subscription schedule [Server-side]

To schedule changes to this subscription, [create](https://docs.stripe.com/api/subscription_schedules/create.md) a [subscription schedule](https://docs.stripe.com/billing/subscriptions/subscription-schedules.md).

Set [from_subscription](https://docs.stripe.com/api/subscription_schedules/create.md#create_subscription_schedule-from_subscription) to the subscription ID from the previous step.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscriptionSchedule = await stripe.subscriptionSchedules.create({
  from_subscription: "{{SUBSCRIPTION_ID}}",
});
```

## Test your integration

Use the Stripe Dashboard or CLI to simulate an [inbound transfer of funds](https://docs.stripe.com/payments/bank-transfers/accept-a-payment.md#test-your-integration).

As soon as you receive a fund, Stripe performs [automatic](https://docs.stripe.com/invoicing/bank-transfer.md#automatic-transfer-reconciliation) or [manual](https://docs.stripe.com/invoicing/bank-transfer.md#manual-reconciliation) reconciliation of the invoice.
