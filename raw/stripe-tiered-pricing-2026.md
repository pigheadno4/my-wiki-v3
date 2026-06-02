<!-- Source URL: https://docs.stripe.com/subscriptions/pricing-models/tiered-pricing -->
<!-- Fetched: 2026-05-12 -->

# Set up tiered pricing

Set up tiered pricing for your subscriptions.

Prices can represent tiers, allowing the unit cost to change with quantity or usage. Use tiers if you need non-linear pricing when `quantity` or [usage](https://docs.stripe.com/api/billing/meter-event.md) changes. To create [usage-based pricing models](https://docs.stripe.com/subscriptions/pricing-models/usage-based-pricing.md), you can combine tiered pricing with flat rates.

For example, imagine a business called [Typographic](https://typographic.io/) that wants to offer lower rates for customers who use more fonts per month. The following tiered pricing models show two different ways to adjust pricing as usage increases: [volume-based pricing](https://docs.stripe.com/subscriptions/pricing-models/tiered-pricing.md#volume-based-pricing) and [graduated pricing](https://docs.stripe.com/subscriptions/pricing-models/tiered-pricing.md#graduated-pricing). To demonstrate these approaches to tiered pricing, we’ll use the following tiers:

|                 | Number of fonts | Price per tier |
| --------------- | --------------- | -------------- |
| **First tier**  | 1-5             | 7 USD          |
| **Second tier** | 6-10            | 6.5 USD        |
| **Third tier**  | 11+             | 6 USD          |

## Volume-based pricing

With volume-based pricing, the subscription item bills at the tier corresponding to the amount of usage at the end of the period. The entire `quantity` (or `usage`) is multiplied by the unit cost of the tier. Because the tier price applies to the entire `quantity` (or `usage`), the total might decrease when calculating the final cost.

For example, a customer with 5 fonts is charged 35 USD (5 × 7 USD) in November. If they use 6 fonts in December, then Typographic bills all fonts at the `6-10` rate. For December, Typographic charges 39 USD (6 × 6.5 USD).

| Quantity and usage at end of the period | Unit cost | Total monthly cost |
| --------------------------------------- | --------- | ------------------ |
| 1                                       | 7 USD     | 7 USD              |
| 5                                       | 7 USD     | 35 USD             |
| 6                                       | 6.5 USD   | 39 USD             |
| 20                                      | 6 USD     | 120 USD            |
| 25                                      | 6 USD     | 150 USD            |

#### Dashboard

1. Go to the [Product catalog](https://dashboard.stripe.com/products).
1. Click **+ Create product**.
1. Enter a **Name** for the product.
1. (Optional) Add a **Description**. The description appears at checkout, on the [customer portal](https://docs.stripe.com/customer-management.md), and in [quotes](https://docs.stripe.com/quotes.md).

Next, create the monthly price for the product:

1. Click **More pricing options**.
1. Select **Recurring**.
1. For **Choose your pricing model**, select **Tiered pricing** and **Volume**.
1. Under **Price**, create three tiers:
   | | First unit | Last unit | Per unit | Flat rate |
   | ----------- | ---------- | --------- | -------- | --------- |
   | First tier | 1 | 5 | 7 USD | 0 USD |
   | Second tier | 6 | 10 | 6.5 USD | 0 USD |
   | Third tier | 11 | ∞ | 6 USD | 0 USD |
1. For **Billing period**, select **Monthly**.
1. Click **Add product** to save the product and price. You can only edit the product and price until you create a subscription with them.

#### API

Create the tiers to match the example and set the value of `tiers_mode` to `volume`:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const price = await stripe.prices.create({
  nickname: "Font Volume Pricing",
  tiers: [
    {
      unit_amount: 700,
      up_to: 5,
    },
    {
      unit_amount: 650,
      up_to: 10,
    },
    {
      unit_amount: 600,
      up_to: "inf",
    },
  ],
  currency: "usd",
  recurring: {
    interval: "month",
    usage_type: "metered",
  },
  product: "{{PRODUCT_ID}}",
  tiers_mode: "volume",
  billing_scheme: "tiered",
  expand: ["tiers"],
});
```

## Graduated pricing

Graduated pricing charges for the usage in each tier instead of applying a single price for overall usage. The `quantity` is multiplied by the amount for each tier and the totals for each tier are summed together.

For example, 5 fonts result in the same charge as volume-based pricing: 35 USD total at 7 USD per font. This changes as usage exceeds the first tier. Typographic charges a customer with more than 5 fonts 7 USD per font for the first 5 fonts, then 6.5 USD for fonts 6 through 10, and 6 USD for any additional fonts. They charge a customer with 6 fonts 41.5 USD, 35 USD for the first 5 fonts and 6.5 USD for the 6th font.

| Quantity and usage at end of the period | Total for graduated tiered pricing |
| --------------------------------------- | ---------------------------------- |
| 1                                       | 7 USD                              |
| 5                                       | 35 USD                             |
| 6                                       | 41.5 USD                           |
| 20                                      | 127.5 USD                          |
| 25                                      | 157.5 USD                          |

#### Dashboard

1. Go to the [Product catalog](https://dashboard.stripe.com/products).
1. Click **+ Create product**.
1. Enter a **Name** for the product.
1. (Optional) Add a **Description**. The description appears at checkout, on the [customer portal](https://docs.stripe.com/customer-management.md), and in [quotes](https://docs.stripe.com/quotes.md).

Next, create the monthly price for the product:

1. Click **More pricing options**.
1. Select **Recurring**.
1. For **Choose your pricing model**, select **Tiered pricing** and **Graduated**.
1. Under **Price**, create three tiers:
   | | First unit | Last unit | Per unit | Flat rate |
   | ----------- | ---------- | --------- | -------- | --------- |
   | First tier | 1 | 5 | 7 USD | 0 USD |
   | Second tier | 6 | 10 | 6.5 USD | 0 USD |
   | Third tier | 11 | ∞ | 6 USD | 0 USD |
1. For the **Billing period**, select **Monthly**.
1. Click **Add product** to save the product and price. You can only edit the product and price until you create a subscription with them.

#### API

Create the tiers to match the example and set the value of `tiers_mode` to `graduated`:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const price = await stripe.prices.create({
  nickname: "Per-minute pricing",
  tiers: [
    {
      unit_amount: 700,
      up_to: 5,
    },
    {
      unit_amount: 650,
      up_to: 10,
    },
    {
      unit_amount: 600,
      up_to: "inf",
    },
  ],
  currency: "usd",
  recurring: {
    interval: "month",
    usage_type: "metered",
  },
  product: "{{PRODUCT_ID}}",
  tiers_mode: "graduated",
  billing_scheme: "tiered",
  expand: ["tiers"],
});
```

## Add a flat rate

You can specify a flat rate (`flat_amount`) to add to the _invoice_ (Invoices are statements of amounts owed by a customer. They track the status of payments from draft through paid or otherwise finalized. Subscriptions automatically generate invoices, or you can manually create a one-off invoice). This works for both volume and graduated pricing. For example, you can have a flat fee that increases when your customer exceeds certain usage thresholds:

| Tier               | Amount (unit cost)        | Flat rate                   |
| ------------------ | ------------------------- | --------------------------- |
| 1-5 (`up_to=5`)    | 5 USD (`unit_amount=500`) | 10 USD (`flat_amount=1000`) |
| 6-10 (`up_to=10`)  | 4 USD (`unit_amount=400`) | 20 USD (`flat_amount=2000`) |
| 10-15 (`up_to=15`) | 3 USD (`unit_amount=300`) | 30 USD (`flat_amount=3000`) |
| 15-20 (`up_to=20`) | 2 USD (`unit_amount=200`) | 40 USD (`flat_amount=4000`) |
| 20+ (`up_to=inf`)  | 1 USD (`unit_amount=100`) | 50 USD (`flat_amount=5000`) |

#### Volume-based pricing flat rate example

If `quantity` is `12` and `tiers_mode=volume`, the total amount billed is:

12 × 3 USD + 30 USD = 66 USD

#### Graduated pricing flat rate example

If `quantity` is `12` and `tiers_mode=graduated`, the total amount billed is:

(5 × 5 USD + 10 USD) + (5 × 4 USD + 20 USD) + (2 × 3 USD + 30 USD) = 111 USD

A tier can have either a `unit_amount` or a `flat_amount`, or both, but it must have at least one of the two. If `quantity` is `0`, the total amount is 10 USD regardless of the tiered pricing model used. Stripe always bills the first flat rate tier when `quantity=0`. To bill `0` when there’s no usage, set up an `up_to=1` tier with an `unit_amount` equal to the flat rate and omit the `flat_amount`.
