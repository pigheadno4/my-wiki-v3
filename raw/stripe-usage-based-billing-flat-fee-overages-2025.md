<!-- Source URL: https://docs.stripe.com/billing/subscriptions/usage-based-v1/use-cases/flat-fee-and-overages -->
<!-- Fetched: 2026-05-05 -->

# Set up a flat fee and overages pricing model

Charge customers a flat rate with the option to pay for additional usage in arrears.

Flat fee with overages combines predictable billing with the flexibility to scale. Customers pay a set recurring fee for a base package, and any usage beyond that limit is billed separately. This model works well if you want steady, reliable revenue while still giving customers room to grow. The base fee covers core value, while overages ensure that heavy users pay in proportion to what they consume. For example, if you run a video hosting platform, you might include 1,000 monthly video streams in a 200 USD flat fee. If a customer streams more than that, each additional stream is billed as an overage. At the end of the month, Stripe sends an invoice that combines the flat fee with any usage above the included limit, automatically charging the customer’s payment method on file or prompting them to add one.

## What you’ll build

In this example, Hypernian charges customers for access to their LLM services by using a [fixed fee and overages](https://docs.stripe.com/subscriptions/pricing-models/usage-based-pricing.md#fixed-fee-overage) pricing model, with the following rates:

| License  | Fee     |
| -------- | ------- |
| Per user | 100 USD |

| Usage  | Fee      |
| ------ | -------- |
| 0-1000 | 0 USD    |
| 1000+  | 0.04 USD |

To implement this model, you create a meter to record the usage, products and prices to represent your service, a customer, and a customer subscription.

## Create a meter

Meters specify how to aggregate meter events over a billing period. Meter events represent all actions that customers take in your system (for example, API requests). Meters attach to prices and form the basis of what’s billed.

For the Hypernian example, meter events are the number of tokens a customer uses in a query. The meter is the sum of tokens over a month.

You can use the Stripe Dashboard or API to configure a meter. To use the API with the Stripe CLI to create a meter, [get started with the Stripe CLI](https://docs.stripe.com/stripe-cli.md).

#### Dashboard

1. On the [Meters](https://dashboard.stripe.com/test/meters) page, click **Create meter**.
1. In the meter editor:
   - For **Meter name**, enter the name of the meter to display and for organization purposes. For the Hypernian example, enter “Hypernian tokens.”
   - For **Event name**, enter the name to display in meter events when reporting usage to Stripe. For the Hypernian example, enter “hypernian_tokens.”
   - Set the **Aggregation method** in the dropdown:
     - For the Hypernian example, select **Sum**. This will *sum the values* reported (in this example, number of tokens a customer uses) to determine the usage to bill for.
     - Choose **Count** to bill based on the *number* of events reported.
     - Choose **Last** to bill based on the *last value* reported.
     - Use the preview pane to set example usage events and verify the aggregation method.
   - Click **Create meter**.

#### API

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const meter = await stripe.billing.meters.create({
  display_name: "Hypernian tokens",
  event_name: "hypernian_tokens",
  default_aggregation: {
    formula: "sum",
  },
  customer_mapping: {
    event_payload_key: "stripe_customer_id",
    type: "by_id",
  },
  value_settings: {
    event_payload_key: "value",
  },
});
```

## Create a pricing model

Use the Stripe Dashboard or API to create a [pricing model](https://docs.stripe.com/products-prices/pricing-models.md) that includes your [Products](https://docs.stripe.com/api/products.md) and their pricing options. [Prices](https://docs.stripe.com/api/prices.md) define the unit cost, currency, and billing period.

For the Hypernian example, you create a product with a metered price of 0.04 USD per hundred units, billed at a monthly interval. Use the meter that you created in the previous step.

#### Dashboard

1. On the [Product catalog](https://dashboard.stripe.com/products?active=true) page, click **Create product**.
1. On the **Add a product** page, do the following:
   1. For **Name**, enter the name of your product. For the Hypernian example, enter `Hypernian usage`.
   1. (Optional) For **Description**, add a description that appears in [Checkout](https://docs.stripe.com/payments/checkout.md), in the [customer portal](https://docs.stripe.com/customer-management.md) and in [quotes](https://docs.stripe.com/quotes.md).
   1. Select **Recurring**.
   1. Under **Billing period**, select **More pricing options**.
1. On the **Add price** page, do the following:
   1. Under **Choose your pricing model**, select **Usage-based**.
   1. Choose your pricing structure:
      - For the Hypernian example, select **Per Tier and Graduated**.
      - In the first row of the grid, set **First unit** to 0, **Last unit** to 1,000, **Per unit** to 0 USD, and **Flat fee** to 0 USD.
      - In the second row of the grid, set **First unit** to 1,001, **Last unit** to ∞, **Per unit** to 0.04 USD, and **Flat fee** to 0 USD.
      - After you create the first product, create another product to charge customers the 100 USD fee at the beginning of the month. A customer’s second invoice contains their usage fees from the previous month and their license fee for the upcoming month.
      - (Optional) To bill customers the initial license fee at the end of the month, update the first row of the grid to set the **Flat fee** to 100 USD.
   1. Under **Meter**, select the meter you created previously. For the Hypernian example, select **Hypernian tokens** from the dropdown.
   1. Select the **Billing period**. For the Hypernian example, select **Monthly**.
   1. Click **Next**.
   1. Click **Add Product**.

#### API

Locate your meter ID on the meter details page.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const product = await stripe.products.create({
  description: "Usage fees for Hypernian",
  name: "Hypernian Usage",
});
```

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const price = await stripe.prices.create({
  product: "{{PRODUCT_ID}}",
  currency: "usd",
  billing_scheme: "tiered",
  recurring: {
    interval: "month",
    interval_count: 1,
    usage_type: "metered",
    meter: "{{METER_ID}}",
  },
  tiers: [
    {
      flat_amount_decimal: Decimal.from("0"),
      unit_amount_decimal: Decimal.from("0"),
      up_to: 1000,
    },
    {
      flat_amount_decimal: Decimal.from("0"),
      unit_amount_decimal: Decimal.from("4"),
      up_to: "inf",
    },
  ],
  tiers_mode: "graduated",
});
```

Next, create the 100 USD monthly fee.

#### Dashboard

1. On the [Product catalog](https://dashboard.stripe.com/products?active=true) page, click **Create product**.
1. On the **Add a product** page, do the following:
   - For **Name**, enter the name of your product. For the Hypernian example, enter `Hypernian license fee`.
   - (Optional) For **Description**, add a description that appears in [Checkout](https://docs.stripe.com/payments/checkout.md), in the [customer portal](https://docs.stripe.com/customer-management.md) and in [quotes](https://docs.stripe.com/quotes.md).
   - Select **Recurring**.
   - Under **Billing period**, select **More pricing options**.
1. On the **Add price** page, do the following:
   - Select *Recurring*.
   - For **Amount**, enter *100 USD*.
   - For **Currency**, select **USD**.
   - For **Billing Period**, select **Monthly**.
   - Click **Next**.
   - Click **Add Product**.

#### API

Create a product and price for the license fee.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const product = await stripe.products.create({
  description: "License fee for Hypernian",
  name: "Hypernian License fee",
});
```

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const price = await stripe.prices.create({
  billing_scheme: "per_unit",
  currency: "usd",
  product: "{{PRODUCT_ID}}",
  recurring: {
    interval: "month",
    interval_count: 1,
    usage_type: "licensed",
  },
  unit_amount_decimal: Decimal.from("10000"),
});
```

## Create a customer

If your integration uses [customer-configured Accounts](https://docs.stripe.com/api/v2/core/accounts/create.md#v2_create_accounts-configuration-customer), replace `Customer` and event references in the code examples with the equivalent Accounts v2 API references. For more information, see [Represent customers with Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md).

Next, create a *customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments).

#### Dashboard

1. On the [Customers](https://dashboard.stripe.com/test/customers) page, click **Add customer**.
1. On the **Create customer** page, do the following:
   - For **Name**, enter the name of your customer. For the Hypernian example, enter `John Doe`.
   - (Optional) Add an email address and description for your customer.
   - Click **Add customer**.

#### API

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create({
  name: "John Doe",
});
```

## Create a subscription

[Subscriptions](https://docs.stripe.com/api/subscriptions.md) allow you to charge recurring amounts by associating a customer with a specific price.

Use the Stripe Dashboard or API to create a subscription that includes your customer, product, and usage-based price.

For the Hypernian example, you create a subscription for the Hypernian usage product and Hypernian license fee product.

> You can associate a single metered price with one or more subscriptions.
>
> When you create a `billing_mode=flexible` subscription, Stripe excludes metered line items from the first invoice since no prior usage exists to bill. Stripe creates an invoice only if the subscription is backdated with previously accrued usage or if pending invoice items exist. When you create a `billing_mode=classic` subscription, Stripe generates a zero monetary value invoice line item for each metered subscription item.

#### Dashboard

1. On the [Subscriptions](https://dashboard.stripe.com/test/subscriptions) page, click **Create test subscription**.
1. On the **Create a test subscription** page, do the following:
   - Under **Customer**, select the name of your customer. For the Hypernian example, select **John Doe**.
   - Under **Product**, select your price. For the Hypernian example, select the price under **Hypernian usage** and **Hypernian license fee**.
   - (Optional) Modify the subscription details and settings as needed.
   - Click **Create test subscription**.

#### API

Locate your customer ID on the customer details page.

You can locate your price ID on the product details page. Under **Pricing**, click the overflow menu (⋯), and then select **Copy price ID** for **Hypernian license** and **Hypernian usage**.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer: "{{CUSTOMER_ID}}",
  items: [
    {
      price: "{{PRICE_ID_for_hypernian_license}}",
    },
    {
      price: "{{PRICE_ID_for_hypernian_usage}}",
    },
  ],
});
```

## Send a test meter event

Use [Meter Events](https://docs.stripe.com/api/billing/meter-event.md) to [record customer usage](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage.md) for your meter. At the end of the billing period, Stripe bills the reported usage.

You can test your usage-based billing by sending a meter event through the Stripe Dashboard or API. When using the API, specify the customer ID and value for the `payload`.

After you send meter events, you can view usage details for your meter on the [Meters](https://dashboard.stripe.com/test/meters) page in the Dashboard.

#### Dashboard

1. On the [Meters](https://dashboard.stripe.com/test/meters) page, select the meter name. For the Hypernian example, select **Hypernian tokens**.
1. On the meter page, click **Add usage** > **Manually input usage**.
1. On the **Add usage** page, do the following:
   - Select your customer from the **Customer** dropdown.
   - For **Value**, enter a sample value. For the Hypernian example, enter `3000`.
   - Click **Submit**.

#### API

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const meterEvent = await stripe.billing.meterEvents.create({
  event_name: "hypernian_tokens",
  payload: {
    stripe_customer_id: "{{CUSTOMER_ID}}",
    value: "3000",
  },
});
```

## Create a preview invoice

[Create a preview invoice](https://docs.stripe.com/api/invoices/create_preview.md) to see a preview of a customer’s invoice that includes details such as the meter price and usage quantity.

#### Dashboard

1. On the [Subscriptions](https://dashboard.stripe.com/test/subscriptions) page, select a subscription. For the Hypernian example, select the subscription for **Jenny Rosen**.

1. On the subscription details page, scroll down to the **Upcoming invoice** section. The preview invoice shows the subscription amount to bill the customer on the specified date.

1. Click **View full invoice** to see complete details for the upcoming invoice, including:
   - Customer
   - Billing method
   - Creation date
   - Connected subscription
   - Subscription details (usage quantity and meter price)
   - Amount due

   Because Stripe processes meter events asynchronously, upcoming invoices might not immediately reflect recently received meter events.

#### API

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const invoice = await stripe.invoices.createPreview({
  subscription: "{{SUBSCRIPTION_ID}}",
});
```

## Optional: Retrieve usage for a custom time period

Use the [Meter Event Summary](https://docs.stripe.com/api/billing/meter-event-summary.md) to retrieve total usage for a custom time period. The meter event summary returns a customer’s aggregated usage for a period, based on the aggregation formula defined by the meter.

In the Hypernian example, the meter event summary returns the sum of tokens for a specific customer, meter, and time window.

Because Stripe processes meter events asynchronously, meter event summaries might not immediately reflect recently received meter events.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const meterEventSummaries = await stripe.billing.meters.listEventSummaries(
  "{{METER_ID}}",
  {
    customer: "{{CUSTOMER_ID}}",
    start_time: 1717249380,
    end_time: 1717249440,
  },
);
```
