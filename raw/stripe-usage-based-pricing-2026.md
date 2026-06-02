<!-- Source URL: https://docs.stripe.com/subscriptions/pricing-models/usage-based-pricing -->
<!-- Fetched: 2026-05-12 -->

# Set up usage-based pricing models

Set up usage-based pricing models for your subscriptions.

Usage-based pricing enables you to charge based on a customer’s usage of your product or service. Usage-based pricing includes models such as:

- [Fixed fee and overage](https://docs.stripe.com/subscriptions/pricing-models/usage-based-pricing.md#fixed-fee-overage)
- [Pay as you go](https://docs.stripe.com/subscriptions/pricing-models/usage-based-pricing.md#pay-as-you-go)
- [Credit burndown](https://docs.stripe.com/subscriptions/pricing-models/usage-based-pricing.md#credit-burndown)

## Fixed fee and overage

Use the fixed fee and overage model to charge a flat rate per month for your service at the beginning of the period. The flat rate has some included usage entitlement, and any additional usage (overage) charges at the end of the period.

You can use the Stripe Dashboard or API to set this up with two prices within the same product. For example, imagine an AI business called Hypernian introduces an advanced model called Hypernian Pro. Priced at 200 USD per month, this model includes 100,000 tokens. They charge any usage above the included tokens at an additional rate of 0.001 USD per token.

#### Dashboard

1. On the [Product catalog](https://dashboard.stripe.com/test/products) page, click **Create product**.

1. On the **Add a product** page, do the following:
   - For **Name**, enter the name of your product. For the Hypernian example, enter “Hypernian.”
   - (Optional) For **Description**, add a description that appears at checkout in the [customer portal](https://docs.stripe.com/customer-management.md) and in [quotes](https://docs.stripe.com/quotes.md).
   - Under **Billing period**, select **More pricing options**.

1. On the **Add price** page, do the following:
   - Under **Choose your pricing model**, select **Flat rate**.
   - Under **Price**, set the **Amount** to 200 USD.
   - Click **Next**

1. To add a second recurring price to the product, click **Add another price** on the **Add a product** page.

1. On the **Add price** page, do the following:
   - Under **Choose your pricing model**, select **Usage-based**, **Per tier**, and **Graduated**.

   - Under **Price**, create two graduated pricing tiers:

|                 | First unit | Last unit | Per unit  | Flat rate |
| --------------- | ---------- | --------- | --------- | --------- |
| **First tier**  | 0          | 100,000   | 0 USD     | 0 USD     |
| **Second tier** | 100,001    | ∞         | 0.001 USD | 0 USD     |

1. Under **Meter**, create a new meter to record usage. For the Hypernian example, use the meter name “hypernian_api_tokens.”

1. Click **Next**.

1. Click **Add product**. When you create subscriptions, specify both prices.

#### API

First, create your [product](https://docs.stripe.com/api/products.md). For the Hypernian example, use the name `Hypernian tokens`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const product = await stripe.products.create({
  name: "Hypernian tokens",
});
```

Next, add a flat rate [price](https://docs.stripe.com/api/prices.md) to the product with a licensed rate of 200 USD.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const price = await stripe.prices.create({
  product: "{{PRODUCT_ID}}",
  currency: "usd",
  unit_amount: 20000,
  billing_scheme: "per_unit",
  recurring: {
    usage_type: "licensed",
    interval: "month",
  },
});
```

Then, add a metered price to the product with a graduated rate with two tiers.

For the first tier, specify 0 to 100,000 units at 0 USD per unit. For the second tier, specify 0.001 USD per unit. The first tier has a price of 0 USD because the flat rate includes the first 100,000 units.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const price = await stripe.prices.create({
  product: "{{PRODUCT_ID}}",
  currency: "usd",
  billing_scheme: "tiered",
  recurring: {
    usage_type: "metered",
    interval: "month",
    meter: "{{METER_ID}}",
  },
  tiers_mode: "graduated",
  tiers: [
    {
      up_to: 100000,
      unit_amount_decimal: Decimal.from("0"),
    },
    {
      up_to: "inf",
      unit_amount_decimal: Decimal.from("0.1"),
    },
  ],
});
```

Finally, specify both price IDs when you [create a subscription](https://docs.stripe.com/billing/subscriptions/usage-based/implementation-guide.md#create-subscription).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer: "{{CUSTOMER_ID}}",
  items: [
    {
      price: "{{FLAT_MONTHLY_FEE_PRICE_ID}}",
      quantity: 1,
    },
    {
      price: "{{METERED_USAGE_PRICE_ID}}",
    },
  ],
});
```

## Pay as you go

The pay as you go model (also called “in arrears billing”) lets you track usage incurred over a determined period, then charge the customer at the end of the period.

You can use any of the following pricing strategies:

- **Per unit**: Charge the same amount for each unit.
- **Per package**: Charge an amount for a package or bundle of units or usage.
- **Volume-based pricing**: Charge the subscription item at the tier that corresponds to the usage amount at the end of the period.
- **Graduated pricing**: Charge for the usage in each tier instead of applying a single price to all usage.

This model might cause customers to accumulate significant usage, and affect their payment method status at the end of the month.

## Credit burndown

The credit burndown model lets you collect prepayment for usage-based products and services. Customers can use [billing credits](https://docs.stripe.com/billing/subscriptions/usage-based/billing-credits.md) to pay an initial amount, and then apply their billing credits as they use the product.

For example, Hypernian wants to sell a large enterprise contract to an existing self-serve customer for their new Hypernian Model. The customer commits to pay 100000 USD up front for Hypernian, so they can get 120000 USD of billing credit usage to use within 1 year.

#### Dashboard

#### Collect prepayment from a customer

1. On the [Invoices](https://dashboard.stripe.com/invoices) page, click **Create invoice**.
1. Select your customer from the **Customer** dropdown.
1. Select the correct currency from the **Currency** dropdown.
1. Under **Items**, select **Add a new line item**.
1. Under **Item details**, do the following:
   - For **Item**, enter “Hypernian Credits.”
   - For **Price**, enter “100,000.”
   - Click **Save**.
1. Click **Send invoice**.

After your customer pays the invoice, you can grant them billing credits.

#### Grant billing credits to a customer

1. On the [Customers](https://dashboard.stripe.com/test/customers) page, select the customer name.
1. On the customer page, under **Credit grants**, click the plus (**+**) symbol.
1. On the **New credit grant** page, do the following:
   - For **Name**, enter a name for your credit grant.
   - For **Amount**, specify the amount of the credit grant. For the Hypernian example, enter “120,000.”
   - Under **Expiry date**, specify the date, if any, when the credits expire. For the Hypernian example, select **Specific date** and set a date 12 months from now.
   - Click **Create grant**.

#### API

First, create an invoice.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const invoice = await stripe.invoices.create({
  description: "Hypernian Credits",
  customer: "{{CUSTOMER_ID}}",
  collection_method: "charge_automatically",
});
```

Next, add the billing credits to the invoice.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const invoiceItem = await stripe.invoiceItems.create({
  customer: "{{CUSTOMER_ID}}",
  currency: "usd",
  unit_amount_decimal: Decimal.from("10000000"),
  invoice: "{{INVOICE_ID}}",
});
```

Then, finalize the invoice.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const invoice = await stripe.invoices.finalizeInvoice("{{INVOICE_ID}}", {
  auto_advance: true,
});
```

After your customer pays the invoice, you can grant them billing credits.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const creditGrant = await stripe.billing.creditGrants.create({
  customer: "{{CUSTOMER_ID}}",
  category: "paid",
  amount: {
    type: "monetary",
    monetary: {
      value: 12000000,
      currency: "usd",
    },
  },
  applicability_config: {
    scope: {
      price_type: "metered",
    },
  },
  expires_at: 1759341179,
});
```
