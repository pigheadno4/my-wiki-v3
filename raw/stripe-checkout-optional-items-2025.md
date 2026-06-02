<!-- Source: Stripe Checkout — Configure optional items -->
<!-- Fetched: 2026-04-20 -->

# Configure optional items

Enable customers to purchase complementary products at checkout by using optional items.

# Hosted page

> This is a Hosted page for when payment-ui is stripe-hosted. View the full page at https://docs.stripe.com/payments/checkout/optional-items?payment-ui=stripe-hosted.
> ![](https://docs.stripecdn.com/84b8dfc6dd8a1b5c8d1375a930b8c2d38f48d151fb004cbdd88f048e25a79ff5.mp4)
> Configuring optional items on a _Checkout Session_ (A Checkout Session represents your customer's session as they pay for one-time purchases or subscriptions through Checkout. After a successful payment, the Checkout Session contains a reference to the Customer, and either the successful PaymentIntent or an active Subscription) allows customers to add multiple optional products to their order during checkout. This can increase your average order value and revenue. For example, if you’re selling a subscription service, you might also want to offer optional add-ons to customers during checkout like a one-time setup fee and recurring priority support plan.

## Create a Checkout Session with optional items

When creating a Checkout Session, you configure `optional_items` in the same way you configure `line_items`, specifying a `price` and `quantity` for each optional item you want to offer to the customer. You can offer up to 10 optional items on a single Checkout Session.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  optional_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
});
```

## Allow customers to adjust quantity

You can also allow customers to adjust the quantity of optional items after adding them to their order by specifying `adjustable_quantity`, the same way you do for line items.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  optional_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
      adjustable_quantity: {
        enabled: true,
        minimum: 0,
        maximum: 10,
      },
    },
  ],
});
```

Customers can always remove optional items from their order, even if you specify a `quantity` or `adjustable_quantity.minimum` greater than 0.

## Limitations

- Supports at most 10 optional items.
- Doesn’t support recurring optional items if a line item has a subscription upsell configured.
- Doesn’t support optional items using custom amounts or using optional items when a line item is using custom amounts.
- Not supported in `setup` mode.
- Doesn’t support recurring optional items in `payment` mode.
- The billing interval of any recurring optional items (monthly, yearly, etc) must match the interval of the recurring line items.
- [Cross-sells](https://docs.stripe.com/payments/checkout/cross-sells.md) configured in the Product catalog won’t appear on Checkout Sessions created with optional items.

### Add a product-associated optional item

Use [cross-sells](https://docs.stripe.com/payments/checkout/cross-sells.md) to specify complementary products that you always want recommended as optional items at checkout. When you configure a cross-sell associated with a product, the optional item appears across all eligible Checkout Sessions with that product. Cross-sells won’t appear if you specify additional optional items on a payment link.

To configure a cross-sell:

1. On the [Product catalog](https://dashboard.stripe.com/test/products) page, select your product.
1. On the product details page, under **Cross-sells**, find the product you want to cross-sell.

After you configure a cross-sell, the Checkout Sessions that contain your designated product automatically add the cross-sell as an optional item.
![](https://docs.stripecdn.com/73a4baa89ea5ac0e30a39cd03f33b21e35979759cdc9293b680695226a5b7dbe.mp4)

# Embedded page

> This is a Embedded page for when payment-ui is embedded-form. View the full page at https://docs.stripe.com/payments/checkout/optional-items?payment-ui=embedded-form.
> ![](https://docs.stripecdn.com/84b8dfc6dd8a1b5c8d1375a930b8c2d38f48d151fb004cbdd88f048e25a79ff5.mp4)
> Configuring optional items on a _Checkout Session_ (A Checkout Session represents your customer's session as they pay for one-time purchases or subscriptions through Checkout. After a successful payment, the Checkout Session contains a reference to the Customer, and either the successful PaymentIntent or an active Subscription) allows customers to add multiple optional products to their order during checkout. This can increase your average order value and revenue. For example, if you’re selling a subscription service, you might also want to offer optional add-ons to customers during checkout like a one-time setup fee and recurring priority support plan.

## Create a Checkout Session with optional items

When creating a Checkout Session, you configure `optional_items` in the same way you configure `line_items`, specifying a `price` and `quantity` for each optional item you want to offer to the customer. You can offer up to 10 optional items on a single Checkout Session.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  optional_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
});
```

## Allow customers to adjust quantity

You can also allow customers to adjust the quantity of optional items after adding them to their order by specifying `adjustable_quantity`, the same way you do for line items.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  optional_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
      adjustable_quantity: {
        enabled: true,
        minimum: 0,
        maximum: 10,
      },
    },
  ],
});
```

Customers can always remove optional items from their order, even if you specify a `quantity` or `adjustable_quantity.minimum` greater than 0.

## Limitations

- Supports at most 10 optional items.
- Doesn’t support recurring optional items if a line item has a subscription upsell configured.
- Doesn’t support optional items using custom amounts or using optional items when a line item is using custom amounts.
- Not supported in `setup` mode.
- Doesn’t support recurring optional items in `payment` mode.
- The billing interval of any recurring optional items (monthly, yearly, etc) must match the interval of the recurring line items.
- [Cross-sells](https://docs.stripe.com/payments/checkout/cross-sells.md) configured in the Product catalog won’t appear on Checkout Sessions created with optional items.

### Add a product-associated optional item

Use [cross-sells](https://docs.stripe.com/payments/checkout/cross-sells.md) to specify complementary products that you always want recommended as optional items at checkout. When you configure a cross-sell associated with a product, the optional item appears across all eligible Checkout Sessions with that product. Cross-sells won’t appear if you specify additional optional items on a payment link.

To configure a cross-sell:

1. On the [Product catalog](https://dashboard.stripe.com/test/products) page, select your product.
1. On the product details page, under **Cross-sells**, find the product you want to cross-sell.

After you configure a cross-sell, the Checkout Sessions that contain your designated product automatically add the cross-sell as an optional item.
![](https://docs.stripecdn.com/73a4baa89ea5ac0e30a39cd03f33b21e35979759cdc9293b680695226a5b7dbe.mp4)
