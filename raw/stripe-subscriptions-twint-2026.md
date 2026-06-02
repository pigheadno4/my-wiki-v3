<!-- Source URL: https://docs.stripe.com/billing/subscriptions/twint -->
<!-- Fetched: 2026-05-13 -->

# Set up a subscription with TWINT

Learn how to create and charge for a subscription with TWINT.

Use this guide to set up a _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) using [TWINT](https://docs.stripe.com/payments/twint.md) as a payment method.

# Stripe-hosted page

> This is a Stripe-hosted page for when api-integration is checkout. View the full page at https://docs.stripe.com/billing/subscriptions/twint?api-integration=checkout.

You can use the [Checkout API](https://docs.stripe.com/api/checkout/sessions.md) to create and confirm a subscription with a prebuilt checkout page.

## Create a product and price [Dashboard]

[Products](https://docs.stripe.com/api/products.md) represent the item or service you’re selling. [Prices](https://docs.stripe.com/api/prices.md) define how much and how frequently you charge for a product. This includes how much the product costs, what currency you accept, and whether it’s a one-time or recurring charge. If you only have a few products and prices, create and manage them in the Dashboard.

This guide uses a stock photo service as an example and charges customers a 15 CHF monthly subscription. To model this:

1. Go to the [Products](https://dashboard.stripe.com/products?active=true) page and click **Create product**.
1. Enter a **Name** for the product. You can optionally add a **Description** and upload an image of the product.
1. Select a **Product tax code**. Learn more about [product tax codes](https://docs.stripe.com/tax/tax-codes.md).
1. Select **Recurring**. Then enter **15** for the price and select **CHF** as the currency.
1. Choose whether to **Include tax in price**. You can either use the default value from your [tax settings](https://dashboard.stripe.com/test/settings/tax) or set the value manually. In this example, select **Auto**.
1. Select **Monthly** for the **Billing period**.
1. Click **More pricing options**. Then select **Flat rate** as the pricing model for this example. Learn more about [flat rate](https://docs.stripe.com/products-prices/pricing-models.md#flat-rate) and other [pricing models](https://docs.stripe.com/products-prices/pricing-models.md).
1. Add an internal **Price description** and [Lookup key](https://docs.stripe.com/products-prices/manage-prices.md#lookup-keys) to organize, query, and update specific prices in the future.
1. Click **Next**. Then click **Add product**.

After you create the product and the price, record the price ID so you can use it in subsequent steps. The pricing page displays the ID and it looks similar to this: `price_G0FvDp6vZvdwRZ`.

## Create a Checkout Session [Server-side]

Your customer must authorize you to use their TWINT account for future payments through Stripe Checkout. This allows you to accept TWINT payments.

Add a checkout button to your website that calls a server-side endpoint to create a [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md).

```html
<html>
  <head>
    <title>Checkout</title>
  </head>
  <body>
    <form action="/create-checkout-session" method="POST">
      <button type="submit">Checkout</button>
    </form>
  </body>
</html>
```

Create a Checkout Session in `subscription` mode to collect the required information. After creating the Checkout Session, redirect your customer to the [URL](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-url) returned in the response.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  success_url: "https://example.com/success",
  line_items: [
    {
      price: "{{RECURRING_PRICE_ID}}",
      quantity: 1,
    },
  ],
  payment_method_types: ["card", "twint"],
  mode: "subscription",
});
```

## Test your integration [Server-side]

Test your TWINT integration with your test API keys by viewing the redirect page. If you authorize the mandate on the redirect page, the SetupIntent transitions from `requires_action` to `succeeded`. If you decline the mandate on the redirect page, the SetupIntent transitions from `requires_action` to `requires_payment_method`.

# Setup Intents API

> This is a Setup Intents API for when api-integration is setupintents. View the full page at https://docs.stripe.com/billing/subscriptions/twint?api-integration=setupintents.

Create and confirm a subscription using two API calls. The [first API call](https://docs.stripe.com/billing/subscriptions/twint.md#create-setup-intent) uses the [Setup Intents API](https://docs.stripe.com/api/setup_intents.md) to set TWINT as a payment method. The [second API call](https://docs.stripe.com/billing/subscriptions/twint.md#create-subscription) sends customer, product, and payment method information to the [Subscriptions API](https://docs.stripe.com/api/subscriptions.md) to create a Subscription and confirm a payment in one call.

## Create a product and price [Dashboard]

[Products](https://docs.stripe.com/api/products.md) represent the item or service you’re selling. [Prices](https://docs.stripe.com/api/prices.md) define how much and how frequently you charge for a product. This includes how much the product costs, what currency you accept, and whether it’s a one-time or recurring charge. If you only have a few products and prices, create and manage them in the Dashboard.

This guide uses a stock photo service as an example and charges customers a 15 CHF monthly subscription. To model this:

1. Go to the [Products](https://dashboard.stripe.com/products?active=true) page and click **Create product**.
1. Enter a **Name** for the product. You can optionally add a **Description** and upload an image of the product.
1. Select a **Product tax code**. Learn more about [product tax codes](https://docs.stripe.com/tax/tax-codes.md).
1. Select **Recurring**. Then enter **15** for the price and select **CHF** as the currency.
1. Choose whether to **Include tax in price**. You can either use the default value from your [tax settings](https://dashboard.stripe.com/test/settings/tax) or set the value manually. In this example, select **Auto**.
1. Select **Monthly** for the **Billing period**.
1. Click **More pricing options**. Then select **Flat rate** as the pricing model for this example. Learn more about [flat rate](https://docs.stripe.com/products-prices/pricing-models.md#flat-rate) and other [pricing models](https://docs.stripe.com/products-prices/pricing-models.md).
1. Add an internal **Price description** and [Lookup key](https://docs.stripe.com/products-prices/manage-prices.md#lookup-keys) to organize, query, and update specific prices in the future.
1. Click **Next**. Then click **Add product**.

After you create the product and the price, record the price ID so you can use it in subsequent steps. The pricing page displays the ID and it looks similar to this: `price_G0FvDp6vZvdwRZ`.

## Create a SetupIntent [Server-side]

Create a [SetupIntent](https://docs.stripe.com/api/setup_intents.md) to save a customer’s payment method for future payments. The `SetupIntent` tracks the steps of this setup process.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  confirm: true,
  return_url: "https://www.stripe.com",
  usage: "off_session",
  payment_method_data: {
    type: "twint",
  },
  payment_method_types: ["twint"],
  mandate_data: {
    customer_acceptance: {
      type: "online",
      online: {
        ip_address: "127.0.0.1",
        user_agent: "device",
      },
    },
  },
});
```

The returned SetupIntent includes a _client secret_ (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)), which the client side uses to securely complete the setup instead of passing the entire SetupIntent object. You can use different approaches to [pass the client secret to the client side](https://docs.stripe.com/payments/payment-intents.md#passing-to-client).

The SetupIntent response also includes a payment method ID that you need to use in the next step to confirm a PaymentIntent.

The SetupIntent response includes the status `requires_action`, which means your users must perform another action to complete the SetupIntent. Use the `next_action.redirect_to_url.url` object from the SetupIntent response to redirect your users to a TWINT-hosted page that displays the QR code.

To authenticate users, follow the instructions to [confirm SetupIntent and save a payment method](https://docs.stripe.com/payments/twint/set-up-future-payments.md?ui=direct-api). After they authenticate, the TWINT-hosted page redirects users to the `return_url` on their mobile device, and the SetupIntent moves to a `succeeded` state.

## Create a subscription [Server-side]

Create a subscription that has a price and customer. Set the value of the `default_payment_method` parameter to the PaymentMethod ID from the SetupIntent response.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer: "{{CUSTOMER_ID}}",
  items: [
    {
      price: "{{PRICE_ID}}",
    },
  ],
  default_payment_method: "{{PAYMENT_METHOD_ID}}",
});
```

Included in the response is the subscription’s first [PaymentIntent](https://docs.stripe.com/payments/payment-intents.md), containing the _client secret_ (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)), which you use on the client side to securely complete the payment process instead of passing the entire PaymentIntent object. Return the `client_secret` to the frontend to complete payment.

> To create a _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) with a free trial period, see [Subscription trials](https://docs.stripe.com/billing/subscriptions/trials.md).

# Subscriptions API

> This is a Subscriptions API for when api-integration is subscription. View the full page at https://docs.stripe.com/billing/subscriptions/twint?api-integration=subscription.

Create and confirm a Subscription using two API calls. The [first API call](https://docs.stripe.com/billing/subscriptions/twint.md#pi-create-subscription) sends customer and product information to the [Subscriptions API](https://docs.stripe.com/api/subscriptions.md) to create a Subscription and PaymentIntent in one call. The response includes a PaymentIntent ID that you must use in a [Payment Intents API](https://docs.stripe.com/api/payment_intents.md) call to [confirm a payment](https://docs.stripe.com/billing/subscriptions/twint.md#pi-confirm-payment).

## Create a product and price [Dashboard]

[Products](https://docs.stripe.com/api/products.md) represent the item or service you’re selling. [Prices](https://docs.stripe.com/api/prices.md) define how much and how frequently you charge for a product. This includes how much the product costs, what currency you accept, and whether it’s a one-time or recurring charge. If you only have a few products and prices, create and manage them in the Dashboard.

This guide uses a stock photo service as an example and charges customers a 15 CHF monthly subscription. To model this:

1. Go to the [Products](https://dashboard.stripe.com/products?active=true) page and click **Create product**.
1. Enter a **Name** for the product. You can optionally add a **Description** and upload an image of the product.
1. Select a **Product tax code**. Learn more about [product tax codes](https://docs.stripe.com/tax/tax-codes.md).
1. Select **Recurring**. Then enter **15** for the price and select **CHF** as the currency.
1. Choose whether to **Include tax in price**. You can either use the default value from your [tax settings](https://dashboard.stripe.com/test/settings/tax) or set the value manually. In this example, select **Auto**.
1. Select **Monthly** for the **Billing period**.
1. Click **More pricing options**. Then select **Flat rate** as the pricing model for this example. Learn more about [flat rate](https://docs.stripe.com/products-prices/pricing-models.md#flat-rate) and other [pricing models](https://docs.stripe.com/products-prices/pricing-models.md).
1. Add an internal **Price description** and [Lookup key](https://docs.stripe.com/products-prices/manage-prices.md#lookup-keys) to organize, query, and update specific prices in the future.
1. Click **Next**. Then click **Add product**.

After you create the product and the price, record the price ID so you can use it in subsequent steps. The pricing page displays the ID and it looks similar to this: `price_G0FvDp6vZvdwRZ`.

## Create a subscription [Server-side]

Create a [subscription](https://docs.stripe.com/api/subscriptions.md) that has a price and customer with status of `incomplete` by providing the [payment_behavior](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-payment_behavior) parameter with a value of `default_incomplete`. Set the `payment_settings.save_default_payment_method=on_subscription` parameter to save a payment method when a subscription is activated.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer: "{{CUSTOMER_ID}}",
  payment_behavior: "default_incomplete",
  items: [
    {
      price: "{{PRICE_ID}}",
    },
  ],
  payment_settings: {
    save_default_payment_method: "on_subscription",
  },
  expand: ["latest_invoice.payments", "latest_invoice.confirmation_secret"],
});
```

The response includes the _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis)’s first [Invoice](https://docs.stripe.com/api/invoices.md). This contains the invoice’s payments, which includes a default PaymentIntent that Stripe generated for this invoice and the confirmation secret which you can use on the client side to securely complete the payment process instead of passing the entire PaymentIntent object. Return the `latest_invoice.confirmation_secret.client_secret` to the front end to complete payment.

Get the PaymentIntent ID that you must use to confirm a payment from `latest_invoice.payments`.

> To create a _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) with a free trial period, see [Subscription trials](https://docs.stripe.com/billing/subscriptions/trials.md).

## Confirm a payment [Server-side]

Confirm a payment with [PaymentIntents](https://docs.stripe.com/api/payment_intents.md) using the PaymentIntent ID from the Subscriptions response.

Add the PaymentIntent ID to the URL path and set the value of the `payment_method_types` parameter to `twint`.

```curl
curl https://api.stripe.com/v1/payment_intents/:id/confirm \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "payment_method_data[type]=twint" \
  --data-urlencode "return_url=https://www.stripe.com" \
  -d "mandate_data[customer_acceptance][type]=online" \
  -d "mandate_data[customer_acceptance][online][ip_address]=127.0.0.0" \
  -d "mandate_data[customer_acceptance][online][user_agent]=device" \
  -d "mandate_data[customer_acceptance][accepted_at]=1660000000"
```

The PaymentIntent response includes the status `requires_action`, which means your users must perform another action to complete the PaymentIntent. Use the `next_action.redirect_to_url.url` object from the PaymentIntent response to redirect your users to a TWINT hosted page that displays the QR code.

To authenticate users, follow the instructions for [redirect and authenticate transactions](https://docs.stripe.com/payments/twint/accept-a-payment.md?platform=web&ui=direct-api#handle-redirect). After they authenticate, the TWINT hosted page redirects users to the `return_url` on their mobile device, and the PaymentIntent moves to a `succeeded` state.

After a successful payment, the subscription becomes active and saves the payment method as the default payment method.
