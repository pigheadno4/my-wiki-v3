<!-- Source URL: https://docs.stripe.com/payment-links/shipping -->
<!-- Fetched: 2026-04-20 -->

# Charge for shipping

Create different shipping rates for your customers.

Shipping rates let you display various shipping options—like standard, express, and overnight—with more accurate delivery estimates. Charge your customer for shipping using different Stripe products, some of which require coding. Before you create a shipping rate, learn how to [collect billing and shipping addresses](https://docs.stripe.com/payment-links/customize.md).

> #### Third-party plugins
>
> If you’re using a third-party application with Stripe (for example, [Thrivecart](https://support.thrivecart.com/help/setting-your-physical-fulfilment-shipping-options/) or [Shopify](https://help.shopify.com/en/manual/shipping/setting-up-and-managing-your-shipping/setting-up-shipping-rates)) and want to adjust the shipping rate, visit the docs for that service.

#### Dashboard

1. Create a [payment link](https://dashboard.stripe.com/test/payment-links/create) and select **Collect customers’ addresses** with the **Billing and shipping addresses** option.
1. Select the countries you ship to.
1. Click **Add shipping rates** to select an existing shipping rate or add a new one. You can only use shipping rates with one-time prices on payment links.
   ![Add shipping rate to payment link](assets/create-payment-link-with-shipping-rate.299819920f996e92c28c393f7a9d91cc.png)

Add a new shipping rate for a payment link in the Dashboard

#### API

[Create a shipping rate](https://docs.stripe.com/api/shipping_rates.md), which at a minimum, requires the `type` and `display_name` parameters. The following code sample uses both of these parameters along with `fixed_amount` and `deliver_estimate` to create a shipping rate:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const shippingRate = await stripe.shippingRates.create({
  display_name: "Ground shipping",
  type: "fixed_amount",
  fixed_amount: {
    amount: 500,
    currency: "usd",
  },
  delivery_estimate: {
    minimum: {
      unit: "business_day",
      value: 5,
    },
    maximum: {
      unit: "business_day",
      value: 7,
    },
  },
});
```

Create a payment link and [collect a billing and shipping address](https://docs.stripe.com/payments/collect-addresses.md?payment-ui=payment-links). Add shipping rates to the payment link using the [shipping_options](https://docs.stripe.com/api/payment-link/object.md#payment_link_object-shipping_options) parameter. You can only use shipping rates with one time prices on payment links.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentLink = await stripe.paymentLinks.create({
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  billing_address_collection: "required",
  shipping_address_collection: {
    allowed_countries: ["US"],
  },
  shipping_options: [
    {
      shipping_rate: "{{SHIPPINGRATE_ID}}",
    },
  ],
});
```
