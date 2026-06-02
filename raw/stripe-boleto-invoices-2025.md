<!-- Source URL: https://docs.stripe.com/payments/boleto/set-up-invoices -->
<!-- Fetched: 2026-05-07 -->

# Use Boleto with invoices

Learn how to use Boleto with invoices.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

Learn how to set up [Boleto](https://docs.stripe.com/payments/boleto.md) as a *payment method* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs). Boleto is a voucher with a generated number that *Customers* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) can obtain from an ATM, a bank, an online bank portal, or an authorized agency.

## Enable Boleto emails

Before you start your integration, go to **Manage payments that require confirmation** in your [Subscriptions and emails settings](https://dashboard.stripe.com/settings/billing/automatic) and enable **Send a Stripe-hosted link for customers to confirm their payments when required**.

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

Create a customer for every new user or business you want to bill. When you create a new customer, set up a [minimal customer profile](https://docs.stripe.com/payments/boleto/set-up-invoices.md#customer-profile) to help generate more useful invoices, and enable Smart Retries (if you’re an [Invoicing Plus](https://stripe.com/invoicing/pricing) user). After you set up your customer, you can issue one-off invoices or create *subscriptions* (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis).

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

## Create and send an invoice

To create and send an invoice, complete these steps:

#### Dashboard

1. In the Dashboard, go to the [Invoices overview page](https://dashboard.stripe.com/invoices), then click **Create Invoice** to open the [invoice editor](https://dashboard.stripe.com/invoices/create). Whenever you exit the invoice editor, Stripe saves a draft. To delete a draft invoice, click the overflow menu (⋯) next to an invoice on the [Invoices page](https://dashboard.stripe.com/invoices).

1. Choose an existing customer by entering their name.

1. Select your product under **Items**, and enter the **Quantity**. Stripe automatically populates the product’s price based on what you selected when you first created the product.

1. (Optional) Click **Item options** if you need to add a tax rate, coupon, or supply date. You can also use the Dashboard to create a [tax rate](https://dashboard.stripe.com/tax-rates) or [coupon](https://dashboard.stripe.com/coupons/create).

1. (Optional) Use the **Memo** box to provide more information to your customer. You can edit the memo on an invoice by clicking **Edit memo** on its details page.

1. Select the following invoice delivery option, depending on whether you want to send the invoice or charge your customer automatically:

   > If you want to automatically charge your customer using Boleto, go to the [Customers page](https://dashboard.stripe.com/customers), click the customer, and select **Add Boleto** under Payment methods.
   - **Automatically charge a payment method on file**: Immediately charges the invoice amount to the payment method that you have on file for the customer. (Select **Boleto** as the payment option.)

   - **Email invoice with link**: Enables Stripe to send an email with a payment page and an invoice PDF. (Select **Boleto** and **card** as the payment options.)

1. (Optional) To schedule this invoice to [finalize automatically](https://docs.stripe.com/invoicing/scheduled-finalization.md) at some date in the future, select **Schedule send date**. Or, depending on what you selected in the previous step, **Schedule charge date** or **Schedule finalization date**.

1. (Optional) Expand **Advanced options**, and add [custom fields](https://docs.stripe.com/invoicing/customize.md#custom-fields). You can also choose whether you want item prices to **Include inclusive tax** or **Exclude tax**. To learn more, see [Net prices and taxes](https://docs.stripe.com/invoicing/taxes.md#net-price-taxes). Expand **Advanced options**, and add [custom fields](https://docs.stripe.com/invoicing/customize.md#custom-fields).

1. Click **Review invoice**, deciding whether you want to include additional emails or continue editing. Send the invoice.

If you automatically charge your customer, they still need to pay the Boleto for the payment to succeed (despite the finalization of the invoice.) Stripe sends your customer an email with a link that they can visit to complete their Boleto payment.
![](https://d37ugbyn3rpeym.cloudfront.net/videos/invoice-editor-net-price-supply-date.mp4)

#### API

### Create an invoice

If you need to invoice a customer, create an invoice item by passing the customer ID, currency, and price. You can then create an invoice for your customer, which automatically adds the invoice item.

To simplify the example, we’ve set `auto_advance` to `true`. This means that Stripe automatically finalizes the invoice after a few hours, which makes the invoice ready for payment. Stripe doesn’t send emails in a *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes), but you can verify that Stripe created the invoice by checking the [Invoices page](https://dashboard.stripe.com/test/invoices) in the Dashboard. The **Invoices** page shows a **Scheduled** status next to the invoice until it’s automatically finalized.

Before you finalize the invoice, decide how you want the customer to pay by using the [collection_method](https://docs.stripe.com/api/invoices/object.md#invoice_object-collection_method) parameter. You can send an email to your customer (`send_invoice`) or charge them automatically (`charge_automatically`). If you use `send_invoice`, provide the [days_until_due](https://docs.stripe.com/api/invoices/create.md#create_invoice-days_until_due) parameter so that Stripe can mark an invoice as past due. When you send an invoice, Stripe emails the invoice to the customer with payment instructions.

> The maximum number of invoice items is 250. Creating an invoice adds up to 250 pending invoice items with the remainder to be added on the next invoice. To see your customer’s pending invoice items, see the **Customer details** page or set the [pending](https://docs.stripe.com/api/invoiceitems/list.md#list_invoiceitems-pending) attribute to `true` when you use the API to list all of the invoice items.

#### Email an invoice

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const invoiceItem = await stripe.invoiceItems.create({
  customer: "{{CUSTOMER_ID}}",
  pricing: {
    price: "{{PRICE_ID}}",
  },
});
```

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const invoice = await stripe.invoices.create({
  customer: "{{CUSTOMER_ID}}",
  collection_method: "send_invoice",
  payment_settings: {
    payment_method_types: ["card", "boleto"],
  },
  days_until_due: 3,
});
```

If you set `auto_advance` to `false`, you can continue to modify the invoice until you [finalize](https://docs.stripe.com/invoicing/integration/workflow-transitions.md) it. To finalize a draft invoice, use the Dashboard, send it to the customer, or pay it. You can also use the [Finalize an invoice](https://docs.stripe.com/api/invoices/finalize.md) API:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const invoice = await stripe.invoices.finalizeInvoice("{{INVOICE_ID}}");
```

You can [void](https://docs.stripe.com/invoicing/overview.md#void) an invoice if it was created in error. You can also mark an invoice as [uncollectible](https://docs.stripe.com/invoicing/overview.md#uncollectible).

#### Automatically charge your customer

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const invoiceItem = await stripe.invoiceItems.create({
  customer: "{{CUSTOMER_ID}}",
  pricing: {
    price: "{{PRICE_ID}}",
  },
});
```

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const invoice = await stripe.invoices.create({
  customer: "{{CUSTOMER_ID}}",
  collection_method: "charge_automatically",
  auto_advance: true,
});
```

If you set `auto_advance` to `false`, you can continue to modify the invoice until you [finalize](https://docs.stripe.com/invoicing/integration/workflow-transitions.md) it. To finalize a draft invoice, use the Dashboard, send it to the customer, or pay it. You can also use the [Finalize an invoice](https://docs.stripe.com/api/invoices/finalize.md) API:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const invoice = await stripe.invoices.finalizeInvoice("{{INVOICE_ID}}");
```

If you created the invoice in error, [void](https://docs.stripe.com/invoicing/overview.md#void) it. You can also mark an invoice as [uncollectible](https://docs.stripe.com/invoicing/overview.md#uncollectible).

### Send an invoice

Send the invoice to the email address associated with the customer. Stripe finalizes the invoice as soon as you send it. Many jurisdictions consider finalized invoices a legal document making certain fields unalterable. If you send invoices that have already been paid, there’s no reference to the payment in the email.

> When you send invoices that have already been paid, the email doesn’t reference the payment. Stripe sends invoices to the email address associated with the customer.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const invoice = await stripe.invoices.sendInvoice("{{INVOICE_ID}}");
```

## See also

- [How Invoicing works](https://docs.stripe.com/invoicing/overview.md)
