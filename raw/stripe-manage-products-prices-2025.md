<!-- Source URL: https://docs.stripe.com/products-prices/manage-prices -->
<!-- Fetched: 2026-04-20 -->

# Manage products and prices

Learn how to manage products and prices.

You can create and update products and prices in the Dashboard or through the API.

Some advanced use cases, such as [creating variable prices](https://docs.stripe.com/products-prices/how-products-and-prices-work.md#variable-pricing), require you to use the API. Use the API if you have a large number of products and prices or if you’re [building a custom integration](https://docs.stripe.com/billing/subscriptions/build-subscriptions.md?payment-ui=elements) with Elements.

- Use the [Dashboard](https://dashboard.stripe.com/test/products) to create and manage products and prices if you want to avoid writing code or if you only have a few products and prices. Set up your _pricing model_ (The pricing model consists of the products or services you sell, how much they cost, what currency you accept for payments, and the service period to charge (for subscriptions). To build the pricing model, you use Products—what you sell—and Prices—how much and how often to charge for your products) in a sandbox and click the **Copy to live mode** button on the product details page.
- Use the [API](https://docs.stripe.com/api.md) or the [Stripe CLI](https://docs.stripe.com/stripe-cli.md) to create and manage products and prices. The API is a direct method that you use for production implementations. The Stripe CLI is a developer tool that helps you build, test, and manage your integration with Stripe directly from your terminal.

The following API steps illustrate an example of a software-as-a-service platform that charges a monthly subscription fee, along with a one-time setup fee.

## Create a product

#### Dashboard

### Create a product and price

#### Create a product

To create a product in the Dashboard:

1. Go to **More** > **Product catalog**.
1. Click **+Add product**.
1. Enter the **Name** of your product.
1. (Optional) Add a **Description**. The description appears at checkout, on the [customer portal](https://docs.stripe.com/customer-management.md), and in [quotes](https://docs.stripe.com/quotes.md).
1. (Optional) Add an **Image** of your product. Use a JPEG, PNG, or WEBP file that’s smaller than 2MB. The image appears at checkout.
1. (Optional) If you’re using [Stripe Tax](https://docs.stripe.com/tax.md), select a **Tax code** for your product. See [tax codes](https://docs.stripe.com/tax/tax-codes.md) for more information about the appropriate category for your product.
1. (Optional) Enter a **Statement descriptor**. This descriptor overrides any account descriptors for recurring payments. Choose something that your customers would recognize on a bank statement.
1. (Optional) Enter a **Unit label**. This describes how you sell your product. For example, if you charge by the seat, enter “seat” so the line item includes “per seat” for the price. Unit labels appear at checkout, and in invoices, receipts, and the _customer portal_ (The customer portal is a secure, Stripe-hosted page that lets your customers manage their subscriptions and billing details).

#### Create a price for the product

To save a product in the Dashboard, you must also add at least one price. The product editor shows the flat-rate pricing model by default. You can create multiple prices or use a different pricing model with the **Advanced pricing options**.

1. Select a **Pricing model**. For more details about recurring pricing models, read the [pricing model guide](https://docs.stripe.com/products-prices/pricing-models.md).
   - **Flat-rate pricing**: Charge the same price for each unit. If you use this option, select **One time** or **Recurring**.
   - **Package pricing**: Charge by the package, or group of units, such as charging 25 USD for every 5 units. Purchases are rounded up by default, so a customer buying 8 units pays 50 USD.
   - **Graduated pricing**: Use pricing tiers that might result in a different price for some units in an order. For example, you might charge 10 USD per unit for the first 100 units and then 5 USD per unit for the next 50. If you use this option, select the currency for the price and fill in the tier table.
   - **Volume pricing**: Charge the same price for each unit based on the total number of units sold. For example, you might charge 10 USD per unit for 50 units, and 7 USD per unit for 100 units. If you use this option, select the currency for the price and fill in the tier table.

   - **Customer chooses price**: Let the payer decide on the amount to pay for your product, service, or cause. **Customer chooses price** is only compatible with Checkout and Payment Links.

   - **Usage-based pricing**: Charge your customers based on how much of your service they use during the billing period.

1. (Optional) If you’re selling in multiple currencies, click **Add another currency** to set how much to charge in each currency.

1. Select a **Billing period** for recurring prices. You can add a custom period if none of the drop-down options are what you want.

1. Select whether to **Include tax in price**. Learn more about [taxes and subscriptions](https://docs.stripe.com/billing/taxes/collect-taxes.md).

1. (Optional) Enter a **Price description**. Customers don’t see this description.

1. (Optional) Click **Advanced pricing options** if you want to create multiple prices for your product.
1. Click **Add product** to save the product and price. You can [edit both](https://docs.stripe.com/products-prices/manage-prices.md#edit-product) later.

#### API

To create a single product and price:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const product = await stripe.products.create({
  name: "Basic Dashboard",
  default_price_data: {
    unit_amount: 1000,
    currency: "usd",
    recurring: {
      interval: "month",
    },
  },
  expand: ["default_price"],
});
```

When customers first sign up for this service, they’re also charged a setup fee.

To create the fee as a product and price, make the same request using a different product name and price data:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const product = await stripe.products.create({
  name: "Starter Setup",
  default_price_data: {
    unit_amount: 2000,
    currency: "usd",
  },
  expand: ["default_price"],
});
```

## Edit a product

#### Dashboard

To modify a product in the Dashboard:

1. Go to **More** > **Product catalog**.
1. Find the product you want to modify, click the overflow menu (⋯), then click **Edit product**.
1. Make your changes to the product.
1. Click **Save product**.

You can also edit products from within the product information page by clicking the overflow menu (⋯) or **Edit**.

#### API

To modify a product through the API:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const product = await stripe.products.update("id", {
  name: "Updated Product",
});
```

## Archive a product

If you want to disable a product so that it can’t be added to new invoices or subscriptions, you can archive it. If you archive a product, any existing subscriptions that use the product remain active until they’re canceled and any existing payment links that use the product are deactivated. You can’t delete products that have an associated price, but you can archive them.

#### Dashboard

To archive a product:

1. Go to **More** > **Product catalog**.
1. Find the product you want to modify, click the overflow menu (⋯), then click **Archive product**.

To unarchive a product:

1. Go to the **Archived** tab on the **Product catalog**\>**Overview** page.
1. Find the product you want to modify, click the overflow menu (⋯), then click **Unarchive product**.

You can also unarchive a product from the product information page.

#### API

To archive a product (that is, to indicate that it’s not available for purchase) through the API, change the [active](https://docs.stripe.com/api/products/update.md#update_product-active) parameter to `false`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const product = await stripe.products.create({
  active: false,
  name: "My product",
});
```

To unarchive a product (that is, to indicate that it’s available for purchase) through the API, change the [active](https://docs.stripe.com/api/products/update.md#update_product-active) parameter to `true`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const product = await stripe.products.update("id", {
  active: true,
});
```

## Delete a product

You can only delete products that have no prices associated with them. Alternatively, you can [archive a product](https://docs.stripe.com/products-prices/manage-prices.md#archive-product).

#### Dashboard

If a product has a price associated with it, you have to [delete](https://docs.stripe.com/products-prices/manage-prices.md#delete-price) or [archive](https://docs.stripe.com/products-prices/manage-prices.md#archive-price) the price before you can delete the product. Stripe keeps a record of the price and product for historical transactions.

To permanently delete a product:

1. Go to **More** > **Product catalog**.
1. Find the product you want to modify, click the overflow menu (⋯), then click **Delete product**.

#### API

To permanently delete a product through the API, use [delete product](https://docs.stripe.com/api/products/delete.md).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const deleted = await stripe.products.del("{{PRODUCT_ID}}");
```

## Create a price

You can create single or multiple prices for a product. For example, you might have a “starter” level offered at 10 USD per month, 100 USD per year, or 9 EUR as a one-time purchase.

> After you create a price, you can only update its `metadata`, `nickname`, and `active` fields.

#### Dashboard

To create a price in the Dashboard, you have to [create a product](https://docs.stripe.com/products-prices/manage-prices.md#create-product) first. Then you can create a price:

1. Select a **Pricing model**. For more details about recurring pricing models, read the [pricing model guide](https://docs.stripe.com/products-prices/pricing-models.md).
   - **Flat-rate pricing**: Charge the same price for each unit. If you use this option, select **One time** or **Recurring**.
   - **Package pricing**: Charge by the package, or group of units, such as charging 25 USD for every 5 units. Purchases are rounded up by default, so a customer buying 8 units pays 50 USD.
   - **Graduated pricing**: Use pricing tiers that might result in a different price for some units in an order. For example, you might charge 10 USD per unit for the first 100 units and then 5 USD per unit for the next 50. If you use this option, select the currency for the price and fill in the tier table.
   - **Volume pricing**: Charge the same price for each unit based on the total number of units sold. For example, you might charge 10 USD per unit for 50 units, and 7 USD per unit for 100 units. If you use this option, select the currency for the price and fill in the tier table.

   - **Customer chooses price**: Let the payer decide on the amount to pay for your product, service, or cause. **Customer chooses price** is only compatible with Checkout and Payment Links.

   - **Usage-based pricing**: Charge your customers based on how much of your service they use during the billing period.

1. (Optional) If you’re selling in multiple currencies, click **Add another currency** to set how much to charge in each currency.

1. Select a **Billing period** for recurring prices. You can add a custom period if none of the drop-down options are what you want.

1. Select whether to **Include tax in price**. Learn more about [taxes and subscriptions](https://docs.stripe.com/billing/taxes/collect-taxes.md).

1. (Optional) Enter a **Price description**. Customers don’t see this description.

1. Click **Create price** to save the price. You can [edit the price](https://docs.stripe.com/products-prices/manage-prices.md#edit-price) later.

#### API

To create prices through the API, use [create price](https://docs.stripe.com/api/prices/create.md).

In this example, the service charges 10 USD per month for a “starter” service level.

The `unit_amount` parameter uses the lowest unit of the currency specified for the price. In this case, the lowest unit is cents: 10 USD is 1,000 cents, which means their price `unit_amount` is `1000`.

To create the price and assign it to the product, pass the product ID, unit amount, currency, and interval:

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

The setup fee for new customers is 20 USD. Because this charge is separate from the subscription and you only charge it one time, you don’t need to pass the `interval`:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const price = await stripe.prices.create({
  product: "{{PRODUCT_ID}}",
  unit_amount: 2000,
  currency: "usd",
});
```

### Set a default price

A product’s default price is the most common price you want to present to customers. For example, a product could have multiple prices for seasonal sales, but the default is the regular (non-sale) price. If you create a product in the [Dashboard](https://dashboard.stripe.com/products), then this initial price is set as the default price. The default price must be an [active](https://docs.stripe.com/api/prices/object.md#price_object-active) price.

#### Dashboard

To change your product’s default price in the Dashboard:

1. Go to **More** > **Product catalog**.
1. Find the product you want to modify, click the overflow menu (⋯), then click **Edit product**.
1. Under the **Price information** section, find the price you want to set as the new default price, then click **Set as default price**.
1. Click **Save product**.

To create a new price and make it the new default price in the Dashboard:

1. Go to **More** > **Product catalog**.
1. Find the product you want to modify and click it to open the product information page.
1. In the **Pricing** section, click the **Add another price** button.
1. Enter your pricing details and select **Set as default price**. Read more about the fields available when you [create a price](https://docs.stripe.com/products-prices/manage-prices.md#create-price).
1. Click **Add price**.

#### API

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const product = await stripe.products.update("{{PRODUCT_ID}}", {
  default_price: "{{PRICE_ID}}",
});
```

### Create an inline price

To create an [inline price](https://docs.stripe.com/products-prices/how-products-and-prices-work.md#inline-pricing), pass in `price_data` instead of a `price.id` when you create a one-time payment or subscription. For example, to subscribe a customer to a monthly subscription with an inline price:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer: "{{CUSTOMER_ID}}",
  items: [
    {
      price_data: {
        unit_amount: 5000,
        currency: "usd",
        product: "{{PRODUCT_ID}}",
        recurring: {
          interval: "month",
        },
      },
    },
  ],
});
```

This creates a monthly recurring price of 50 USD for the basic service offering. You can’t update or reuse inline prices after you create them. By default, prices created with `price_data` are effectively archived (they’re marked as `active=false`). You can also use `price_data` with [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions.md), [Payment Links](https://docs.stripe.com/api/payment-link.md), [Invoice Items](https://docs.stripe.com/api/invoiceitems.md), and [Subscription Schedules](https://docs.stripe.com/api/subscription_schedules.md).

### Create multi-currency prices

You can create [multi-currency Prices](https://docs.stripe.com/products-prices/how-products-and-prices-work.md#multiple-currencies) in the [API](https://docs.stripe.com/api/prices/create.md) or the Dashboard.

#### Dashboard

To create a multi-currency Price through the Dashboard:

1. Go to the [Product catalog](https://dashboard.stripe.com/test/products) and select a product.
1. Click **Edit product**.
1. Click **+ Add another price** to create a new price. The default currency is the first currency on your Price. All your Prices must have the same default currency.
1. To add a new currency option to your price, click **+ Add a price by currency**. Search and select from the list of supported currencies.
   - Stripe suggests an exchange rate based on currency values at 12:00 PM EST, but you can pick your own. For currencies that are subject to larger fluctuations, we recommend adding more of a buffer.
1. To save the new price, click **Next** > **Update product**.

#### API

The [currency](https://docs.stripe.com/api/prices/create.md#create_price-currency) parameter sets the default currency for your price. All your prices must have the same default currency. The [currency_options](https://docs.stripe.com/api/prices/create.md#create_price-currency_options) parameter sets which other currencies the price supports.

This code snippet shows how to create a price that supports `usd` (US dollar) as the default currency, and also `eur` (euro) and `jpy` (Japanese yen).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const price = await stripe.prices.create({
  unit_amount: 1000,
  currency: "usd",
  product: "{{PRODUCT_ID}}",
  currency_options: {
    eur: {
      unit_amount: 9000,
    },
    jpy: {
      unit_amount: 12000,
    },
  },
});
```

[Coupons](https://docs.stripe.com/billing/subscriptions/coupons.md#coupons), [promotion codes](https://docs.stripe.com/billing/subscriptions/coupons.md#promotion-codes), and [shipping rates](https://docs.stripe.com/payments/during-payment/charge-shipping.md) also support multi-currency in a similar way to prices.

#### Render multi-currency prices

To show your customer the price in their currency, you can retrieve the multi-currency price and view its [currency_options.<currency>.unit_amount](https://docs.stripe.com/api/prices/object.md#price_object-currency_options-unit_amount) field. The API response won’t include `currency_options` by default. To include it in the response, [expand](https://docs.stripe.com/api/expanding_objects.md) the `currency_options` field:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const price = await stripe.prices.retrieve("{{PRICE_ID}}", {
  expand: ["currency_options"],
});
```

> To improve latency and avoid problems with rate-limiting, cache the price instead of re-fetching it every time a customer visits your site.

#### Use multi-currency prices

Each purchase uses one of the multi-currency Price’s supported currencies, depending on how you use the Price in your integration.

#### Stripe Checkout

Checkout automatically determines the customer’s local currency from their IP address, as long as the price supports that currency. If the customer’s local currency isn’t supported, Checkout uses the default currency for the price.

If a Checkout Session uses multiple prices, coupons, promotion codes, or shipping rates, then they must all support the customer’s local currency, or else Checkout uses the default currency. They must all have the same default currency, or else Stripe returns an error when you create the Checkout Session.

Alternatively, you can use the [currency](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-currency) parameter to explicitly tell Checkout which currency to use.

Learn more about defining [manual currency prices](https://docs.stripe.com/payments/checkout/localize-prices/manual-currency-prices.md) in Checkout.

#### Payment Links

Payment Links automatically determine the customer’s local currency from their IP address, as long as the price supports that currency. If the customer’s local currency isn’t supported, the payment link uses the default currency for the price.

If you have multiple prices in the payment link, they must all support the customer’s local currency, or else the payment link uses the default currency. All the prices must have the same default currency, or else Stripe returns an error when you create the payment link.

Alternatively, you can use the [currency](https://docs.stripe.com/api/payment-link/create.md#create_payment_link-currency) parameter to explicitly tell the payment link which currency to use.

#### Subscriptions

You can create subscriptions several different ways. The way to use multi-currency prices depends on how you create subscriptions:

- If you’re creating subscriptions with Stripe Checkout, Checkout automatically determines the customer’s local currency from their IP address, as long the price supports that currency. If the customer’s local currency isn’t supported, Checkout uses the default currency for the price. If you use multiple prices, coupons, promotion codes, or shipping rates in a single Checkout Session, then they must all support the customer’s local currency, and they must all have the same default currency.

- If you’re creating subscriptions with Stripe Elements, use the [currency](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-currency) parameter to tell the subscription which currency to use for the price. (If you omit the `currency` parameter, then the Subscription uses the default currency for the price.)

- [Subscription schedules](https://docs.stripe.com/billing/subscriptions/subscription-schedules.md) also support multi-currency prices. To create a subscription schedule with a multi-currency price, use the [phases.currency](https://docs.stripe.com/api/subscription_schedules/create.md#create_subscription_schedule-phases-currency) parameter to tell the schedule which of the currencies for the price to use. (If you omit the `phases.currency` parameter, then the schedule and the subscription managed by the schedule use the default currency for the price.)

#### Quotes

Quotes don’t support multi-currency Prices. If you create a quote with a multi-currency price, the quote always uses the default currency for the price.

#### Invoices

When you create an invoice item, use the [currency](https://docs.stripe.com/api/invoiceitems/create.md#create_invoiceitem-currency) parameter to tell the invoice item which of the currencies to use for the multi-currency price.

You must explicitly pass the `currency` parameter even if it’s the same as the customer’s default currency. If you omit the `currency` parameter, multi-currency prices won’t work.

#### Migrate from single-currency prices to multi-currency

If you have an existing single-currency price, you can retroactively add multiple currencies to it in the Dashboard.

If you use Checkout or Payment Links, then multi-currency prices take effect automatically. If Stripe detects that the price supports the customer’s local currency, then it automatically uses that currency. If you use multiple prices, coupons, promotion codes, or shipping rates in a single purchase, then they must all support the customer’s local currency, and they must all have the same default currency.

If you create subscriptions directly, the multi-currency prices don’t take effect until you pass the `currency` parameter. If you don’t pass the `currency` parameter, the subscription always uses the default currency for the price.

### Lookup keys

Most businesses display pricing information on their website. If these prices are hard-coded and you want to change them, the process is often manual and requires you to deploy new code. To better manage these scenarios, you can use the [lookup_key](https://docs.stripe.com/api/prices/create.md#create_price-lookup_key) attribute on the [Price object](https://docs.stripe.com/api/prices/object.md#price_object). This key allows you to:

- Render different prices in your frontend.
- Use the rendered price to bill customers.

You can pass a `lookup_key` when you create a price:

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
  lookup_key: "standard_monthly",
});
```

Instead of hard-coding text like **10 USD per month** on your pricing page and using a price ID on your backend, you can query for the price using the `standard_monthly` key and then render that in your frontend:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const prices = await stripe.prices.list({
  lookup_keys: ["standard_monthly"],
});
```

> To improve performance, you might want to add a caching layer to only reload the price occasionally.

When a customer clicks your subscribe or pay button, you pass the price from the `GET` request above into the Subscriptions API.

Now that you can render different prices, if you decide that you want to start charging new users 20 USD per month rather than 10 USD per month, you only need to create a new price and transfer the lookup key to that new price using [transfer_lookup_key=true](https://docs.stripe.com/api/prices/create.md#create_price-transfer_lookup_key):

#### Rounding

Rounding occurs on the line item level of your _invoices_ (Invoices are statements of amounts owed by a customer. They track the status of payments from draft through paid or otherwise finalized. Subscriptions automatically generate invoices, or you can manually create a one-off invoice). For example, if you create a price with `unit_amount_decimal = 0.05` and a monthly subscription for that [price] with `quantity = 30`, rounding occurs after multiplying the quantity by the decimal amount. In this case, the calculated amount for the line item would be `0.05 * 30 = 1.5`, which rounds up to 2 cents. If you have multiple line items, each is rounded up before summing up the total amount for the invoice. This ensures that customers are still charged an integer minor unit amount, as decimal amounts only apply for pricing.

Exclusive taxes are added to each line item amount, depending on the tax rate. If you enable [automatic taxes](https://docs.stripe.com/tax/invoicing.md), exclusive taxes are applied and rounded on the total of the invoice, including invoice level discounts. If you use manual taxes on either the line item level or the invoice level, you can choose how to apply rounding. Use the [invoice settings](https://dashboard.stripe.com/settings/billing/invoice) page in the Dashboard to apply and round taxes for each line item, or apply and round taxes on the invoice subtotal.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const price = await stripe.prices.create({
  product: "{{PRODUCT_ID}}",
  unit_amount: 2000,
  currency: "usd",
  recurring: {
    interval: "month",
  },
  lookup_key: "standard_monthly",
  transfer_lookup_key: true,
});
```

## Edit a price

Multiple properties can be updated on a price, either in the Dashboard or the API. For example, you can change whether the price is active, or modify its metadata.

Note that you can’t change a price’s amount in the API. Instead, we recommend creating a new price for the new amount, switch to the new price’s ID, then update the old price to be inactive.

#### Dashboard

To modify a price in the Dashboard:

1. Go to **More** > **Product catalog**.
1. Find the product for the price you want to modify, and click it
1. Find the price you want to modify, click the overflow menu (⋯), then click **Edit price**.
1. Make your changes to the price. You can add another price at this point.
1. Click **Save**.

#### API

To edit a price through the API, use [update price](https://docs.stripe.com/api/prices/update.md) and specify the parameter you want to change. If you don’t specify a parameter, it remains unchanged.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const price = await stripe.prices.update("id", {
  lookup_key: "MY_LOOKUP_KEY",
});
```

## Archive a price

If you want to disable a price so that it can’t be added to new invoices or subscriptions, you can archive it. If you archive a price, any existing subscriptions that use the price remain active until they’re canceled and any existing payment links that use the product are deactivated.

#### Dashboard

To archive a price through the Dashboard:

1. Go to **More** > **Product catalog**.
1. Find the product you want to modify, click the overflow menu (⋯).
1. On the product information page, find the price you want to modify, then click the overflow menu (⋯) next to it and click **Archive price**.

To unarchive a price:

1. Go to **More** > **Product catalog**.
1. Find the product you want to modify, click the overflow menu (⋯).
1. On the product information page, find the price you want to modify, then click the overflow menu (⋯) next to it and click **Unarchive price**.

#### API

To use the API to archive a price (that is, to indicate that it can’t be used for new purchases), change the [active](https://docs.stripe.com/api/prices/update.md#update_price-active) parameter to `false`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const price = await stripe.prices.update("id", {
  lookup_key: "MY_LOOKUP_KEY",
  active: false,
});
```

To use the API to unarchive a price (that is, to indicate that it can be used for new purchases), change the [active](https://docs.stripe.com/api/prices/update.md#update_price-active) parameter to `true`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const price = await stripe.prices.update("id", {
  lookup_key: "MY_LOOKUP_KEY",
  active: true,
});
```

## Delete a price

You can only delete prices that you’ve never used. Otherwise, you can [archive them](https://docs.stripe.com/products-prices/manage-prices.md#archive-price).

#### Dashboard

To permanently delete a price in the Dashboard:

1. Go to **More** > **Product catalog**.
1. Find the product you want to modify, click the overflow menu (⋯).
1. On the product information page, find the price you want to modify, then click the overflow menu (⋯) next to it and click **Delete price**.

#### API

You can’t delete a price through the API. You can [archive](https://docs.stripe.com/products-prices/manage-prices.md#archive-price) a price to mark it as `active=false`, which indicates that it’s not available for purchase.

## Display pricing information

After creating products and prices, you can embed a [pricing table](https://docs.stripe.com/payments/checkout/pricing-table.md) on your website to display pricing information to your customers. When customers choose a subscription option, they’re taken directly to checkout. Configure, customize, and update directly in the [Dashboard](https://dashboard.stripe.com/test/pricing-tables) without writing any code.

## Import products and prices

If you have a very large product catalog, use the [Products](https://docs.stripe.com/api/products.md) API to import your catalog programmatically. If you’re importing your product catalog to Stripe, you can use anything as your starting data source, like a product management system or CSV file.

Use the [Products](https://docs.stripe.com/api/products.md) API to create a product in Stripe for each product in your system. To map products in your system to products in Stripe, assign each product that you import a unique [id](https://docs.stripe.com/api/products/create.md#create_product-id). For each product, use the [Prices](https://docs.stripe.com/api/prices.md) API to make a corresponding price. Make sure to store the `id` of the newly created price. You need to pass this `id` when you [use the products and prices](https://docs.stripe.com/products-prices/manage-prices.md#use-products-and-prices-in-your-integration) in your integration.

Confirm the import by checking the [Dashboard](https://dashboard.stripe.com/products) or using the API to [list all products](https://docs.stripe.com/api/products/list.md).

### Delete imported prices

During development, you might need to run this script multiple times for testing. If you use the same Product ID, you’ll see an error stating that a Product with that ID already exists. If you haven’t used the Product yet, you can delete it using the Stripe Dashboard:

1. Go to the Products [Dashboard](https://dashboard.stripe.com/products) and find your Product.

1. In the **Pricing** section, click the overflow menu (⋯ Overflow menu) next to the Price and select **Delete Price**.

1. Click the overflow menu (⋯ Overflow menu) at the top of the page, and select **Delete Product**.

### Synchronize products and prices

You might need to run through an import multiple times. You can create a script to test the import and, if you want to, synch your original data source with Stripe. To make your script idempotent and resilient to errors, you can safely try to create the product first, then update it if the product already exists.

To keep your product catalog synchronized with Stripe, use webhooks or other mechanisms to trigger product updates in Stripe. To [update a product](https://docs.stripe.com/api/products/update.md) programmatically, use the following pattern.

First, find the existing price associated with the product with [list all prices](https://docs.stripe.com/api/prices/list.md) API to make sure the price still matches your data source. Each product should have exactly one active price.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const prices = await stripe.prices.list({
  product: "{{PRODUCT_ID}}",
  active: true,
});
```

Next, check whether the decimal amount of the price has changed. The `unit_amount_decimal` [field](https://docs.stripe.com/api/prices/object.md#price_object-unit_amount_decimal) displays the unit amount in cents.

If the amount doesn’t match, you have to create a new price. When you [create a new price](https://docs.stripe.com/api/prices/create.md), specify the `product` ID of the original product, the `currency`, and the updated `unit_amount` price.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const price = await stripe.prices.create({
  product: "{{PRODUCT_ID}}",
  unit_amount: 2000,
  currency: "usd",
});
```

[Update the old price](https://docs.stripe.com/api/prices/update.md) to mark it as `active=false`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const price = await stripe.prices.update("{{PRICE_ID}}", {
  active: false,
});
```

## Use products and prices in your integration

You can use products and prices across several different Stripe integration paths.

#### Stripe Checkout

Specify the Price ID when you create a Checkout Session.

- If you’re using one-time prices, see [how to create a Checkout Session](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=checkout&ui=stripe-hosted#redirect-customers) when accepting a payment.

- If you’re creating Subscriptions, see [how to create a Checkout Session](https://docs.stripe.com/billing/subscriptions/build-subscriptions.md?payment-ui=checkout&ui=stripe-hosted#create-session) when building a subscription integration.

#### Payment Links

If you’re using Payment Links, the next step is to select a product to [create a payment link](https://docs.stripe.com/payment-links/create.md).

#### Subscriptions

If you’re creating Subscriptions with Stripe Checkout, specify the Price ID when you create a [Checkout Session](https://docs.stripe.com/billing/subscriptions/build-subscriptions.md?payment-ui=checkout&ui=stripe-hosted#create-session).

If you’re creating Subscriptions with Stripe Elements, specify the Price ID when you [create a subscription](https://docs.stripe.com/billing/subscriptions/build-subscriptions.md?payment-ui=elements&api-integration=checkout#create-session).

#### Quotes

If you’re using Quotes, the next step is to select a product when you [create a quote if you’re using the Dashboard](https://docs.stripe.com/quotes/create.md?testing-method=without-code).

If you’re writing code for your Quotes integration, specify the `price.id` when you [create the quote](https://docs.stripe.com/quotes/create.md?testing-method=with-code#create-quote-code).

#### Invoices

If you’re using Invoices, the next step is to select a product when you create an invoice with the [Dashboard](https://docs.stripe.com/invoicing/dashboard.md#create-invoice). If you’re using the [API](https://docs.stripe.com/invoicing/integration.md#create-invoice-code), specify the `price.id`.

## Testing

You can copy products from a testing environment to live mode so that you don’t need to recreate them. Prices associated with the product are also copied over. In the product details page in the Dashboard, click **Copy to live mode** in the upper right corner.

You can only copy test products to live mode once. If you make updates to the test product after the copy, the live product won’t reflect the changes.
