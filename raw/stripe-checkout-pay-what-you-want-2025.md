<!-- Source: Stripe Checkout — Let customers decide what to pay -->
<!-- Fetched: 2026-04-20 -->

# Let customers decide what to pay

Accept tips and donations, or sell pay-what-you-want products and services.

# Hosted page

> This is a Hosted page for when payment-ui is stripe-hosted. View the full page at https://docs.stripe.com/payments/checkout/pay-what-you-want?payment-ui=stripe-hosted.

If you maintain your product catalog outside of Stripe, you might want to use [inline pricing](https://docs.stripe.com/products-prices/how-products-and-prices-work.md#inline-pricing). With inline pricing, you set inline prices for products or services when you create a Checkout Session.

You can also use inline pricing to collect donations. However, unlike pay-what-you-want pricing, you can’t reuse or update inline prices, and they’re only available through the API.

You can use this feature to collect a tip for a service provided, accept donations for a cause, or give your customers the option to pay what they want for your product or service. Go to Stripe Support to learn more about Stripe’s [requirements for accepting tips or donations](https://support.stripe.com/questions/requirements-for-accepting-tips-or-donations).

Pay-what-you-want payments have the following limitations:

- You can’t add any other line items and the quantity can only be 1.
- You can’t use promotion codes or discounts with them.
- They don’t support recurring payments or optional items.
  ![Custom amounts](assets/stripe-checkout-custom-amount.png)

## Set up your product catalog

Stripe Checkout uses _Products_ (Products represent what your business sells—whether that's a good or a service) and _Prices_ (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) to structure pay-what-you-want payments. In the following example, a nonprofit is selling tickets to a fundraising dinner and wants to allow their customers to pay what they want for their tickets.

#### Dashboard

To create a pay-what-you-want model on Stripe through the Dashboard, complete these steps:

1. Create the `Fundraising dinner` product.
   1. Go to **More** > **Product catalog**.
   1. Click **+Add product**.
   1. Enter the **Name** of the product (`Fundraising dinner`).
   1. (Optional) Add a **Description**. The customer sees the description at checkout.

1. Create the price for the `Fundraising dinner` product:
   1. Click **More pricing options** at the bottom.
   1. Select **One-off**.
   1. Select **Customer chooses price** in the **Choose your pricing model** dropdown.
   1. (Optional) Add a suggested price.
   1. (Optional) Specify limits that the customer can input.
   1. Click **Next** and **Add product**.

#### API

To create a pay-what-you-want pricing model on Stripe through the [Products](https://docs.stripe.com/api/products.md) and [Prices](https://docs.stripe.com/api/prices.md) APIs:

1. Create the `Fundraising dinner` product.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const product = await stripe.products.create({
  name: "Fundraising dinner",
});
```

1. Create a price for the customer input. You can optionally specify a `preset` price, which is the initial amount on the payment page that your customer can update. You can also set a `minimum` and `maximum` bound for the price.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const price = await stripe.prices.create({
  currency: "usd",
  custom_unit_amount: {
    enabled: true,
  },
  product: "{{PRODUCT_ID}}",
});
```

## Create a Checkout Session

To enable customers to change the amount on the payment page, use the price ID when you create a Checkout Session. If you select **Customer chooses price** as your pricing model, you can’t add any other line items and the quantity can only be 1.

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
  mode: "payment",
  success_url: "https://example.com/success",
});
```

# Embedded page

> This is a Embedded page for when payment-ui is embedded-form. View the full page at https://docs.stripe.com/payments/checkout/pay-what-you-want?payment-ui=embedded-form.

If you maintain your product catalog outside of Stripe, you might want to use [inline pricing](https://docs.stripe.com/products-prices/how-products-and-prices-work.md#inline-pricing). With inline pricing, you set inline prices for products or services when you create a Checkout Session.

You can also use inline pricing to collect donations. However, unlike pay-what-you-want pricing, you can’t reuse or update inline prices, and they’re only available through the API.

You can use this feature to collect a tip for a service provided, accept donations for a cause, or give your customers the option to pay what they want for your product or service. Go to Stripe Support to learn more about Stripe’s [requirements for accepting tips or donations](https://support.stripe.com/questions/requirements-for-accepting-tips-or-donations).

Pay-what-you-want payments have the following limitations:

- You can’t add any other line items and the quantity can only be 1.
- You can’t use promotion codes or discounts with them.
- They don’t support recurring payments or optional items.
  ![Custom amounts](assets/stripe-checkout-custom-amount.png)

## Set up your product catalog

Stripe Checkout uses _Products_ (Products represent what your business sells—whether that's a good or a service) and _Prices_ (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) to structure pay-what-you-want payments. In the following example, a charity is selling tickets to a fundraising dinner and wants to allow donors to pay what they want for their tickets.

#### Dashboard

To create a pay-what-you-want model on Stripe through the Dashboard, complete these steps:

1. Create the `Fundraising dinner` product.
   1. Go to **More** > **Product catalog**.
   1. Click **+Add product**.
   1. Enter the **Name** of the product (`Fundraising dinner`).
   1. (Optional) Add a **Description**. The customer sees the description at checkout.

1. Create the price for the `Fundraising dinner` product:
   1. Click **More pricing options** at the bottom.
   1. Select **One-off**.
   1. Select **Customer chooses price** in the **Choose your pricing model** dropdown.
   1. (Optional) Add a suggested price.
   1. (Optional) Specify limits that the customer can input.
   1. Click **Next** and **Add product**.

#### API

To create a pay-what-you-want pricing model on Stripe through the [Products](https://docs.stripe.com/api/products.md) and [Prices](https://docs.stripe.com/api/prices.md) APIs:

1. Create the `Fundraising dinner` product.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const product = await stripe.products.create({
  name: "Fundraising dinner",
});
```

1. Create a price for the customer input. You can optionally specify a `preset` price, which is the initial amount on the payment page that your customer can update. You can also set a `minimum` and `maximum` bound for the price.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const price = await stripe.prices.create({
  currency: "usd",
  custom_unit_amount: {
    enabled: true,
  },
  product: "{{PRODUCT_ID}}",
});
```

## Create a Checkout Session

To enable customers to change the amount on the payment page, use the price ID when you create a Checkout Session. If you select **Customer chooses price** as your pricing model, you can’t add any other line items and the quantity can only be 1.

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
  mode: "payment",
  ui_mode: "embedded_page",
  return_url:
    "https://example.com/checkout/return?session_id={CHECKOUT_SESSION_ID}",
});
```
