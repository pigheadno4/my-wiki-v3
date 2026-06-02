<!-- Source URL: https://docs.stripe.com/payments/boleto/set-up-subscription -->
<!-- Fetched: 2026-05-07 -->

# Use Boleto with subscriptions

Learn how to use Boleto with subscriptions.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

Learn how to set up [Boleto](https://docs.stripe.com/payments/boleto.md) as a *payment method* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs). Boleto is a voucher with a generated number that *Customers* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) can obtain from an ATM, a bank, an online bank portal, or an authorized agency.

## Enable Boleto

Before you start your integration, go to **Manage payments that require confirmation** in your [Subscriptions and emails settings](https://dashboard.stripe.com/settings/billing/automatic) and enable **Send a Stripe-hosted link for customers to confirm their payments when required**.

Go to your [Payment methods settings](https://dashboard.stripe.com/settings/payment_methods) and enable Boleto as a payment method. You can click **Configure** to set the voucher expiration delay.

## Decide the collection method

You can set the collection method in the Dashboard or [API](https://docs.stripe.com/api/invoices/create.md#create_invoice-collection_method). For invoices, you can choose to either send an invoice or charge your customer automatically. If you’re using the API, the `send_invoice` and `charge_automatically` values determine the collection method.

|                                                                                                                                                                                                                                                                                                                                     | Send invoice                                                                                                                                                                                                                                                                                    | Charge automatically                                                                                                                                                                                    |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| When to use                                                                                                                                                                                                                                                                                                                         | - Your customer hasn’t defined their preferred payment method to pay invoices or subscriptions. In this case, you want to give them the option to use either a credit card or Boleto.                                                                                                           |
| - You’re missing important customer information required to use Boleto (full name, address, and tax ID).                                                                                                                                                                                                                            | - Your customer already chose to pay for their invoices or subscriptions using boletos.                                                                                                                                                                                                         |
| - You have the customer information needed to create an invoice that uses Boleto (full name, address, and tax ID).                                                                                                                                                                                                                  |
| Customer experience                                                                                                                                                                                                                                                                                                                 | - Your customer needs to reenter their personal information details (full name, address, and tax ID) every time you send a new invoice, or for each new subscription service period. This collection method doesn’t take into account the default payment method associated with that customer. | - Your customer has Boleto set up as their default payment method. Your customer receives an email with a Boleto voucher every time you send them an invoice, or there’s a subscription service period. |
| Expiration and due dates                                                                                                                                                                                                                                                                                                            | - The invoice must contain a due date.                                                                                                                                                                                                                                                          |
| - Stripe creates the boleto—regardless of the invoice due date—as soon as your customer enters the needed details. Because boletos have their own expiration date (the default is 3 days), the invoice due date and the boleto expiration date won’t necessarily match. The boleto might expire before or after the invoice is due. | - The invoice doesn’t have a due date.                                                                                                                                                                                                                                                          |
| - Stripe creates the boleto when the merchant creates the invoice with a selected expiration date (the default is 3 days).                                                                                                                                                                                                          |

## Create a customer

Create a customer for every new user or business you want to bill. When you create a new customer, set up a [minimal customer profile](https://docs.stripe.com/payments/boleto/set-up-subscription.md#customer-profile) to help generate more useful invoices, and enable Smart Retries (if you’re an [Invoicing Plus](https://stripe.com/invoicing/pricing) user). After you set up your customer, you can issue one-off invoices or create *subscriptions* (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis).

> Before you create a new customer, make sure that the customer doesn’t already exist in the Dashboard. Creating multiple customer entries for the same customer can cause you problems later on, such as when you need to reconcile transaction history or coordinate saved payment methods.

#### Dashboard

You can create and manage customers on the [Customers page](https://dashboard.stripe.com/customers) when you don’t want to use code to create a customer, or if you want to manually bill a customer with a one-off invoice. You can also create a customer in the Dashboard during invoice creation.

### Create a customer

When you create a new customer, you can set their account and billing information, such as **Email**, **Name**, and **Country**. You can also set a customer’s preferred language, currency, and other important details.

To create a customer, complete these steps:

1. Verify that the customer doesn’t already exist.

1. Click **Add customer**, or press **N**, on the **Customers** page.

1. At a minimum, enter your customer’s **Name** and **Account email**.

1. Click **Add customer** in the dialog.

### Edit a customer

To edit a customer’s profile, complete these steps:

1. Find the customer you want to modify and click the name on the **Customers** page.

1. In the account information page, select **Actions** > **Edit information**.

1. Make your changes to the customer profile.

1. Click **Update customer**.

### Delete a customer

To delete a customer, complete these steps:

1. Find the customer you want to delete on the **Customers** page.

1. Click the checkbox next to your customer’s name followed by **Delete**. You can also click into the customer’s details page and select **Actions** > **Delete customer**.

#### API

Before you create a new customer, verify that the customer doesn’t already exist. For example, pass an email address to the [list all customers](https://docs.stripe.com/api/customers/list.md) API.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customers = await stripe.customers.list({
  email: "{EMAIL_ADDRESS}",
});
```

Learn how to create a new customer that uses the Boleto payment method. See [create a customer](https://docs.stripe.com/api/customers/create.md) for complete details.

#### Email an invoice

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create({
  email: "joao@exemplo.com",
  description: "My first test customer",
});
```

#### Automatically charge your customer

### Set up the customer

To create a customer with a `name`, `email`, and `description`, add this code:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create({
  name: "João da Silva",
  email: "joao@exemplo.com",
  description: "My first test customer",
});
```

### Create the Boleto payment method

To create the Boleto payment method, add this code:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethod = await stripe.paymentMethods.create({
  type: "boleto",
  boleto: {
    tax_id: "000.000.000-00",
  },
  billing_details: {
    name: "João da Silva",
    email: "joao@exemplo.com",
    address: {
      line1: "1234 Av. Paulista",
      city: "São Paulo",
      state: "SP",
      postal_code: "01310-000",
      country: "BR",
    },
  },
});
```

### Attach that boleto payment method to a customer

To attach the Boleto payment method to your customer, add this code:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethod = await stripe.paymentMethods.attach(
  "{{PAYMENT_METHOD_ID}}",
  {
    customer: "{{CUSTOMER_ID}}",
  },
);
```

### Set default payment method to that customer

To make Boleto the default payment method for your customer, add this code:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.update("{{CUSTOMER_ID}}", {
  invoice_settings: {
    default_payment_method: "{{PAYMENT_ID}}",
  },
});
```

## Create a product and price

Define all your business and product offerings in one place. *Products* (Products represent what your business sells—whether that's a good or a service) define what you sell and *Prices* (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) track how much and how often to charge. This is a core entity within Stripe that works with *subscriptions* (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis), *invoices* (Invoices are statements of amounts owed by a customer. They track the status of payments from draft through paid or otherwise finalized. Subscriptions automatically generate invoices, or you can manually create a one-off invoice), and [Checkout](https://docs.stripe.com/payments/checkout.md).

Prices enable these use cases:

- A software provider that charges a one-time setup fee whenever a user creates a new subscription.
- An e-commerce store that sends a recurring box of goods for 10 USD per month and wants to allow customers to purchase one-time add-ons.
- A professional services firm that can now create a standard list of services and choose from that list per invoice instead of typing out each line item by hand.
- A non-profit organization that allows donors to define a custom recurring donation amount per customer.

You can manage your product catalog with products and prices. Products define what you sell and prices track how much and how often to charge. Manage your products and their prices in the Dashboard or through the API.

#### Dashboard

If you used the Dashboard in a *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes) to set up your business, you can copy each of your products over to live mode by using **Copy to live mode** in the [Product catalog page](https://dashboard.stripe.com/products). Use our official libraries to access the Stripe API from your application.

1. Navigate to the **Product catalog** page, and click **Add product**.

1. Select whether you want to create a **One-time product**, or a **Recurring one-time product**.

1. Give your product a name, and assign it a price.

#### API

Learn how to create [Products](https://docs.stripe.com/api/products.md) and [Prices](https://docs.stripe.com/api/prices.md).

> For a complete guide on how to get started using the [Stripe CLI](https://docs.stripe.com/stripe-cli.md) or API, see the [Invoicing end-to-end integration guide](https://docs.stripe.com/invoicing/integration.md).

### Create a product

To create a product, enter its name:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const product = await stripe.products.create({
  name: "Gold Special",
});
```

### Create a price

[Prices](https://docs.stripe.com/api.md#prices) define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the billing interval (when the price is for a subscription). Like products, if you only have a few prices, it’s preferable to manage them in the Dashboard. Use the unit amount to express prices in the lowest unit of the currency—in this case, cents (10 USD is 1,000 cents, so the unit amount is 1000).

As an alternative, if you don’t need to create a price for your product, you can use the [amount](https://docs.stripe.com/api/invoiceitems/create.md#create_invoiceitem-amount) parameter during invoice item creation.

To create a price and assign it to the product, pass the product ID, unit amount, and currency. In the following example, the price for the “Gold Special” product is 10 USD:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const price = await stripe.prices.create({
  product: "{{PRODUCT_ID}}",
  unit_amount: 1000,
  currency: "usd",
});
```

> #### Localized pricing
>
> When you [create invoice items](https://docs.stripe.com/api/invoiceitems/create.md) or charges with the API, Stripe processes the amount and currency you explicitly provide. The localized price isn’t automatically calculated, and you’re responsible for passing the correct amount and currency for your customer’s region. We recommend using the [pricing.price](https://docs.stripe.com/api/invoiceitems/create.md#create_invoiceitem-pricing-price) parameter to pass the price ID.

## Create a subscription

You can create and update subscriptions from the Dashboard or the API. Use the API if you have a large number of subscriptions to manage, or if you want to manage them programmatically.

> See our integration guide to learn how to [build a complete subscription integration](https://docs.stripe.com/billing/subscriptions/build-subscriptions.md).

#### Dashboard

### Create a subscription

To create a subscription:

1. Go to the **Payments** > **Subscriptions** page.

1. Click **+Create subscription**.

1. Find or add a customer.

1. Enter the pricing and product information, which allows you to add multiple products, a coupon, or trial to the subscription.

In the **Advanced** options section, you can optionally create [thresholds for metered usage](https://docs.stripe.com/products-prices/pricing-models.md#usage-based-pricing) or add [customized invoice](https://docs.stripe.com/invoicing/customize.md) fields. When you’re finished, click **Schedule subscription** or **Start subscription**. When scheduling a subscription you can start it immediately, the next month, or customize it. You can end the subscription immediately, after a number of cycles, or customize a date.

### Edit a subscription

To edit a subscription:

1. Go to the **Payments** > **Subscriptions** page.

1. Find the subscription you want to modify, click the overflow menu (⋯), then click **Update subscription**. You can also click the ✏ edit icon next to the subscription name. From this menu, you can also:
   - **Cancel the subscription**: Select a date to cancel the subscription immediately, at the end of the current period, or on a custom date. You can also select the option to refund the last payment for this subscription and create a [credit note](https://docs.stripe.com/invoicing/dashboard/credit-notes.md) for your records.

   - **Pause payment collection**: Select the duration of the pause (indefinite or ending on a custom date) and how invoices should behave during the pause.

   - **Share payment update link**: Generate a link the customer can use to [update the subscription payment method](https://docs.stripe.com/billing/subscriptions/payment-methods-setting.md#update-payment-method).

1. Make your changes to the subscription.

1. Click **Update subscription**.

### Delete a subscription

You can’t delete a subscription object, but you can cancel it or pause payment collection. See [editing a subscription](https://docs.stripe.com/payments/boleto/set-up-subscription.md#edit-subscription) for those details.

#### API

### Create a subscription

When you create a [subscription](https://docs.stripe.com/api/subscriptions.md), you can email the invoices to the customer, or automatically charge the customer every cycle.

#### Email an invoice

To create a subscription and email your customer an invoice every period, enter the following code:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer: "{{CUSTOMER_ID}}",
  items: [
    {
      price: "{{RECURRING_PRICE_ID}}",
    },
  ],
  collection_method: "send_invoice",
  payment_behavior: "default_incomplete",
  payment_settings: {
    payment_method_types: ["card", "boleto"],
  },
  days_until_due: 3,
});
```

#### Automatically charge your customer

To create a subscription and automatically charge your customer every period, enter the following code:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer: "{{CUSTOMER_ID}}",
  items: [
    {
      price: "{{RECURRING_PRICE_ID}}",
    },
  ],
  collection_method: "charge_automatically",
  payment_behavior: "default_incomplete",
  off_session: true,
});
```

### Use Checkout Sessions

You can also create a subscription using [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions.md). Stripe sends your customer a previously generated Boleto to their email address in each subscription cycle.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  mode: "subscription",
  customer: "{{CUSTOMER_ID}}",
  line_items: [
    {
      price: "{{RECURRING_PRICE_ID}}",
      quantity: 1,
    },
  ],
  payment_method_options: {
    boleto: {
      expires_after_days: 3,
    },
  },
  success_url: "https://example.com/success",
});
```

### Use subscription schedules

Some customers want to schedule their subscription to start in the future or only sign up for a year of service at a time. [Subscription schedules](https://docs.stripe.com/api/subscription_schedules.md) allow you to configure phases with a recurring price to start in the future or configure them to end on a specific date. If you want to bundle one-time purchases with the beginning of a phase, you can do so by using `add_invoice_items` on a phase:

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const schedule = await stripe.subscriptionSchedules.create({
  customer: "{{CUSTOMER_ID}}",
  start_date: "1780272000",
  phases: [
    {
      items: [
        {
          price: "{{RECURRING_PRICE_ID}}",
        },
      ],
      add_invoice_items: [
        {
          price: "{{PRICE_ID}}",
        },
      ],
    },
  ],
});
```

This schedules a 10 USD per month subscription to begin in the future and its first invoice will include a one-time fee of 20 USD.

If you configure `add_invoice_items` on future phases, invoice items won’t be generated until that phase begins. If you set `add_invoice_items` on the current phase, invoice items are generated immediately.

## See also

- [How Subscriptions work](https://docs.stripe.com/billing/subscriptions/overview.md)
