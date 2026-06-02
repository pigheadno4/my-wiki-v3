<!-- Source URL: https://docs.stripe.com/products-prices/how-products-and-prices-work -->
<!-- Fetched: 2026-04-20 -->

# How products and prices work

Learn how products and prices in Stripe model your business.

Products and prices are core resources for many Stripe integrations. Products define what your business offers, whether that’s goods or services. Prices define how much and how often to charge for products.

You can create products and prices in Stripe or [import](https://docs.stripe.com/products-prices/manage-prices.md#import-products-prices) them into Stripe through the [API](https://docs.stripe.com/api/products.md). After you create products and prices, you can use them with [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions/create.md), [Payment Links](https://docs.stripe.com/payment-links.md), [Invoices](https://docs.stripe.com/invoicing.md), [Quotes](https://docs.stripe.com/quotes/create.md), or a custom integration to create [Subscriptions](https://docs.stripe.com/billing.md).

## Products

Products describe the specific goods or services you offer to your customers. Use cases include:

- **E-commerce**: If you sell clothes online, you can create a separate product for each size and color combination of shirts, for example.
- **SaaS platform**: You could offer basic and premium pricing tiers, where basic and premium are separate products.
- **Donation platform**: You accept donations for several different causes, and each cause is a different product.

### Product IDs

Each product has a unique ID. Unlike most Stripe resources, you can choose the ID of the product yourself. We recommend choosing an ID that makes it easy to integrate Stripe with other systems you use. For example, if you’re selling physical goods, you can use the internal ID from your own systems.

### Product names

When you create a product in Stripe, you have to provide a name. You can optionally add other attributes, like a description or image. If you’re using [Stripe Tax](https://docs.stripe.com/tax.md), you can also define a [tax code](https://docs.stripe.com/tax/tax-codes.md) for each product, such as pet grooming, e-books, or SaaS. Stripe Tax uses the tax code to automatically calculate and collect sales taxes during purchase.

## Prices

In Stripe, prices include additional information, such as tax behavior, volume tiers, and recurrence intervals for subscriptions. You don’t need to create new prices for each purchase–if you’re selling a product for one price, you only need to create one price. You can also make this price the [default price](https://docs.stripe.com/products-prices/manage-prices.md#default-price) for the product.

### One-time and recurring payments

Prices can either be one-time or recurring. Subscriptions use recurring prices to charge the customer at an interval, such as “once a month.” If you sell the same service at several different intervals, it’s best to create multiple recurring prices for the same product. Learn more about [pricing models](https://docs.stripe.com/products-prices/pricing-models.md#flat-rate).

### Variable pricing

You can use two types of variable pricing:

- **Inline pricing**: You define the price for your customer when you create a subscription, invoice, Checkout Session, or Payment Link.
- **Pay-what-you-want pricing**: The customer fills in the price they pay, such as with a tip or donation. Recurring payments don’t support this type of variable pricing. See how to [let customers decide what to pay](https://docs.stripe.com/payments/checkout/pay-what-you-want.md) for single payments.

#### Inline pricing

In some cases, you might want to use a custom price that hasn’t been preconfigured. For example, you might want to use inline prices when you manage your product catalog outside of Stripe. You can only create inline prices through the API.

### Multiple currencies

A single Price can support multiple currencies. This helps you manage localized pricing when selling internationally. For example, if you sell a product in the US for 10 USD, in Europe for 9 EUR, and in Japan for 1300 JPY, the same `Price` object can cover all three currencies. Each purchase uses one of the supported currencies for the price, depending on how you use the price in your integration. Learn more about [multi-currency prices](https://docs.stripe.com/products-prices/manage-prices.md#create-multi-currency-prices).

### Multiple prices

Products can use multiple prices to define different pricing options. The prices share the product description, and it looks the same on the customer’s receipt and invoice—only the pricing differs. Because a product can have multiple prices associated with it, you need to specify which price to use when creating Checkout Sessions, Payment Links, invoices, quotes, or subscriptions.

### Unit amount

Most prices define a fixed `unit_amount`, but you can also configure the price to function with different tiers or usage-based models. Learn more about [tiered pricing](https://docs.stripe.com/products-prices/pricing-models.md#tiered-pricing) and [usage-based pricing](https://docs.stripe.com/products-prices/pricing-models.md#usage-based-pricing).

### Tax behavior

If you use Stripe Tax, you can specify the `tax_behavior` for the price to determine whether the tax is already included in the amount, or if it needs to be added. Learn more about [tax behavior](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior.md#tax-behavior).

## Working with products and prices

### Create or import products and prices

The quickest way to get started with products and prices is to create them through the [Stripe Dashboard](https://dashboard.stripe.com/products).

If you have a large product catalog that you manage using a spreadsheet or other software, you might prefer to import the product catalog programmatically using the [Products](https://docs.stripe.com/api/products.md) and [Prices](https://docs.stripe.com/api/prices.md) API. Learn more about [import products and prices](https://docs.stripe.com/products-prices/manage-prices.md#import-products-prices).

If you need to charge an amount of money that’s different for each transaction (for example, a user-selected donation amount), you can create the product, but not create a price. Instead, you can use the `price_data` parameter when creating Checkout Sessions, Payment Links, or Subscriptions to set the particular price.

This method generates `Price` and `Product` objects that are relevant for the specific Checkout Session, Payment Link, or Subscription. While the `Price` objects are temporary and not visible in the Dashboard, the associated `Product` objects aren’t always temporary. For example, `Price` objects created with `price_data` don’t appear in product searches or lists in the Dashboard. You can still view these objects directly by constructing a specific URL in the Dashboard, but they won’t show up in the main catalog.

### Use products and prices

#### Stripe Checkout

When creating a Checkout Session, specify the price `id` for each line item. The Checkout Session uses the price to compute the order total. It also retrieves the product associated with the price, then uses the product’s name and image to render the payment page.

#### Payment Links

Use the Dashboard to create a Payment Link based on a price. The Payment Link uses the price to compute the order total. It also retrieves the product associated with the price. The product’s name and image are used to render the payment page.

#### Subscriptions

When creating a Subscription, specify the price `id`. The price must be recurring. The [recurrence interval](https://docs.stripe.com/api/prices/object.md#price_object-recurring-interval) for the price defines the subscription’s billing period, and the amount for the price defines how much the subscription charges in each billing period. You can add more than one price to the same subscription as long as they have the same recurrence interval.

#### Quotes

When creating a Quote, specify the price `id`. Quotes model the cost of either a one-off invoice or subscription. When a customer accepts the quote, ​​Stripe automatically creates all relevant invoices and subscriptions.

#### Invoices

When creating an invoice, specify the price `id` for each line item. The invoice uses the price to compute the invoice total. It also retrieves the product associated with the price and uses `product.name` when rendering the invoice as a web page or PDF.

## Manage existing products and prices

You can update product details through the Dashboard or API. For example, you might change the description of a product, or add new product images to use on the [Checkout](https://docs.stripe.com/payments/checkout.md) page.

If you’re no longer selling a product, you can archive both it and the price through the Dashboard by clicking the **Archive** button, or through the API by setting `active` to `false`. We store the archived product and price information indefinitely to maintain records of past transactions.

In general, you can’t delete products or prices, you can only archive them. In certain cases, you can use the Dashboard to delete a price that has never been used, or to delete a product that doesn’t have any prices set.

To change the price of a product, create a new price for the new amount, then archive the existing price by setting `active` to `false`. Instead of changing the `unit_amount` on the existing price, you need to create a new price to make sure that we keep the existing price as an immutable record of past transactions.

You can set a [default price](https://docs.stripe.com/products-prices/manage-prices.md#default-price) on a product to specify the most common price to present to customers. You can change the default price to another price later, such as if you increase the price of your product.

## Understand product and price compatibility

Not all features of products and prices are compatible with all Stripe APIs. Consult the following table for compatibility information.

| Feature                                                      | Checkout    | Payment Links  | Quotes         | Subscriptions  | Invoices       |
| ------------------------------------------------------------ | ----------- | -------------- | -------------- | -------------- | -------------- |
| Product images                                               | ✓ Supported | ✓ Supported    | (Ignored\*)    | (Ignored\*)    | (Ignored\*)    |
| Product descriptions                                         | ✓ Supported | ✓ Supported    | ✓ Supported    | (Ignored\*)    | (Ignored\*)    |
| Product tax codes                                            | ✓ Supported | ✓ Supported    | ✓ Supported    | ✓ Supported    | ✓ Supported    |
| Product statement descriptor                                 | ✓ Supported | ✓ Supported    | (Ignored\*)    | ✓ Supported    | ✓ Supported    |
| Recurring prices                                             | ✓ Supported | ✓ Supported    | ✓ Supported    | ✓ Supported    | ✓ Supported    |
| Multi-currency prices                                        | ✓ Supported | ✓ Supported    | (Ignored\*)    | ✓ Supported    | (Ignored\*)    |
| Tiered prices                                                | ✓ Supported | (Disallowed\*) | ✓ Supported    | ✓ Supported    | ✓ Supported    |
| Decimal amounts (for example, charging half-a-cent per unit) | ✓ Supported | (Disallowed\*) | ✓ Supported    | ✓ Supported    | ✓ Supported    |
| Usage-based prices                                           | ✓ Supported | (Disallowed\*) | ✓ Supported    | ✓ Supported    | ✓ Supported    |
| Customer chooses price                                       | ✓ Supported | ✓ Supported    | (Disallowed\*) | (Disallowed\*) | (Disallowed\*) |

Entries marked as (Disallowed) indicate that if a product or price uses this feature, you can’t use that product or price with this Stripe API.

Entries marked as (Ignored) indicate that the feature has no effect with this Stripe API, but you can still use the product or price as usual.

## Understand limitations

We don’t limit the number of customers, coupons, products, prices, or most other objects that you can create in your Stripe account.

When using recurring prices with Subscriptions:

- If you don’t use [flexible billing mode](https://docs.stripe.com/billing/subscriptions/billing-mode.md) to support [mixed interval subscriptions](https://docs.stripe.com/billing/subscriptions/mixed-interval.md), then all prices on a Subscription must have the same [recurring.interval](https://docs.stripe.com/api/prices/create.md#create_price-recurring-interval) and [recurring.interval_count](https://docs.stripe.com/api/prices/create.md#create_price-recurring-interval_count)
- The maximum interval time period of a price is 3 years

## See also

- [Add product images](https://docs.stripe.com/payments/checkout/customization/product-images.md)
