<!-- Source URL: https://docs.stripe.com/subscriptions/pricing-models/flat-rate-pricing -->
<!-- Fetched: 2026-05-12 -->

# Set up flat rate pricing

Set up flat rate pricing for your subscriptions.

SaaS businesses often offer their customers a choice of escalating service options. Customers choose a service tier and pay a flat rate for it. For example, imagine a business called [Typographic](https://typographic.io/) that sells a subscription webfont service. They offer three different service levels: Basic, Starter, and Enterprise. They offer a monthly and yearly price for each service level.
![](assets/stripe-subs-pricing-flat-rate.png)

Flat-rate pricing model

In this example, Typographic has three products: `Basic`, `Starter`, and `Enterprise`. Each product has several different prices. The basic level has prices for 10 USD per month and 100 USD per year. Both prices are for the same `Basic` product, so they share the same product description on the customer’s receipt and invoice.

#### Dashboard

First, create the `Basic` product. To learn about all the options for creating a product, see the [prices guide](https://docs.stripe.com/products-prices/manage-prices.md#create-product).

1. Go to [Product catalog](https://dashboard.stripe.com/products).
1. Click **+ Create product**.
1. Enter a **Name** for the product.
1. (Optional) Add a **Description**. The description appears at checkout, on the [customer portal](https://docs.stripe.com/customer-management.md), and in [quotes](https://docs.stripe.com/quotes.md).

Next, create the monthly price for the `Basic` product:

1. Click **More pricing options**.
1. Select **Recurring**.
1. For **Choose your pricing model**, select **Flat rate**.
1. For **Amount**, enter a price amount.
1. For **Billing period**, select **Monthly**.
1. Click **Next** to save the price.

Then, create the yearly price for the `Basic` product:

1. Click **+ Add another price**.
1. Select **Recurring**.
1. For **Choose your pricing model**, select **Flat rate**.
1. For **Amount**, enter a price amount.
1. For **Billing period**, select **Yearly**.
1. Click **Next**.
1. Click **Add product** to save the product and price. You can only edit the product and price until you create a subscription with them.

#### API

1. Create a Product for the `Basic` service level.

   ```node
   // Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
   // Find your keys at https://dashboard.stripe.com/apikeys.
   const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

   const product = await stripe.products.create({
     name: "Basic",
   });
   ```

1. Create the monthly price for the `Basic` product.

   ```node
   // Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
   // Find your keys at https://dashboard.stripe.com/apikeys.
   const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

   const price = await stripe.prices.create({
     product: "{{PRODUCT_ID}}",
     unit_amount: 1000,
     currency: "usd",
     recurring: {
       interval: "month",
     },
   });
   ```

1. Create the yearly price for the `Basic` product.

   ```node
   // Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
   // Find your keys at https://dashboard.stripe.com/apikeys.
   const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

   const price = await stripe.prices.create({
     product: "{{PRODUCT_ID}}",
     unit_amount: 10000,
     currency: "usd",
     recurring: {
       interval: "year",
     },
   });
   ```

Repeat these steps to create the `Starter` and `Enterprise` products and their associated prices. After you create this pricing model, use it to create [subscriptions](https://docs.stripe.com/api/subscriptions.md) for your customers.

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
});
```
