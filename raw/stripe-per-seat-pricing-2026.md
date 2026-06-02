<!-- Source URL: https://docs.stripe.com/subscriptions/pricing-models/per-seat-pricing -->
<!-- Fetched: 2026-05-12 -->

# Set up per-seat pricing

Set up per-seat pricing for your subscriptions.

Per-seat pricing is a linear pricing model where the number of seats (for example, software licenses) maps to the number of units (for example, users). For example, imagine a business called [Typographic](https://typographic.io/) that wants to offer a per-seat plan. Typographic’s customers pick how many seats they’ll use, and Typographic charges based on that amount. In this example, a customer chooses and pays for three seats, which represents access for three of their users.
![](assets/stripe-subs-pricing-per-seat.png)

Per-seat pricing model

To model this scenario, Typographic creates a product with a flat-rate price where each unit represents a user. When Typographic creates a subscription for a customer, the customer specifies the number of users for that subscription.

#### Dashboard

First, create the `Per-seat` product. To learn about all the options for creating a product, see the [prices guide](https://docs.stripe.com/products-prices/manage-prices.md#create-product).

1. Go to [Product catalog](https://dashboard.stripe.com/products).
1. Click **+ Create product**.
1. Enter a **Name** for the product.
1. (Optional) Add a **Description**. The description appears at checkout, on the [customer portal](https://docs.stripe.com/customer-management.md), and in [quotes](https://docs.stripe.com/quotes.md).

Next, create the monthly price for the product:

1. Select **Recurring**.
1. For **Amount**, enter a price amount.
1. For **Billing period**, select **Monthly**.
1. Click **Add product** to save the product and price. You can only edit the product and price until you create a subscription with them.

To create a subscription using that price:

1. Go to the **Billing** > **Subscriptions** page.
1. Click **+ Create subscription**.
1. Find or add a customer.
1. Search for the product you created and select the price you want to use.
1. (Optional) Select **Collect tax automatically** to use Stripe Tax.
1. Click **Start subscription** to start it immediately. To schedule a subscription, switch to the classic editor, and click **Schedule subscription**. To learn more, see [Subscription schedules](https://docs.stripe.com/billing/subscriptions/subscription-schedules.md?dashboard-or-api=dashboard#managing).

#### API

1. Create the `Per-seat` product.

   ```node
   // Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
   // Find your keys at https://dashboard.stripe.com/apikeys.
   const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

   const product = await stripe.products.create({
     name: "Per-seat",
   });
   ```

1. Create a price for the monthly fee.

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

1. When you create the [subscription](https://docs.stripe.com/api/subscriptions.md), specify a `quantity` to charge for the number of seats.

   ```node
   // Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
   // Find your keys at https://dashboard.stripe.com/apikeys.
   const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

   const subscription = await stripe.subscriptions.create({
     customer: "{{CUSTOMER_ID}}",
     items: [
       {
         price: "{{per_seat_price_id}}",
         quantity: 12,
       },
     ],
   });
   ```
