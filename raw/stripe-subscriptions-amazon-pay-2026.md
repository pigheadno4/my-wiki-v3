<!-- Source URL: https://docs.stripe.com/billing/subscriptions/amazon-pay -->
<!-- Fetched: 2026-05-13 -->

# Set up a subscription with Amazon Pay

Learn how to create and charge for a subscription with Amazon Pay.

Use this guide to set up a _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) using [Amazon Pay](https://docs.stripe.com/payments/amazon-pay.md) as a payment method.

# Setup Intents API

> This is a Setup Intents API for when api-integration is setupintents. View the full page at https://docs.stripe.com/billing/subscriptions/amazon-pay?api-integration=setupintents.

Create and confirm a subscription using two API calls. The [first API call](https://docs.stripe.com/billing/subscriptions/amazon-pay.md#create-setup-intent) uses the [Setup Intents API](https://docs.stripe.com/api/setup_intents.md) to set Amazon Pay as a payment method. The [second API call](https://docs.stripe.com/billing/subscriptions/amazon-pay.md#create-subscription) sends customer, product, and payment method information to the [Subscriptions API](https://docs.stripe.com/api/subscriptions.md) to create a Subscription and confirm a payment in one call.

## Create a product and price [Dashboard]

[Products](https://docs.stripe.com/api/products.md) represent the item or service you’re selling. [Prices](https://docs.stripe.com/api/prices.md) define how much and how frequently you charge for a product. This includes how much the product costs, what currency you accept, and whether it’s a one-time or recurring charge. If you only have a few products and prices, create and manage them in the Dashboard.

This guide uses a stock photo service as an example and charges customers a 15 USD monthly subscription. To model this:

1. Go to the [Products](https://dashboard.stripe.com/products?active=true) page and click **Create product**.
1. Enter a **Name** for the product. You can optionally add a **Description** and upload an image of the product.
1. Select a **Product tax code**. Learn more about [product tax codes](https://docs.stripe.com/tax/tax-codes.md).
1. Select **Recurring**. Then enter **15** for the price and select **USD** as the currency.
1. Choose whether to **Include tax in price**. You can either use the default value from your [tax settings](https://dashboard.stripe.com/test/settings/tax) or set the value manually. In this example, select **Auto**.
1. Select **Monthly** for the **Billing period**.
1. Click **More pricing options**. Then select **Flat rate** as the pricing model for this example. Learn more about [flat rate](https://docs.stripe.com/products-prices/pricing-models.md#flat-rate) and other [pricing models](https://docs.stripe.com/products-prices/pricing-models.md).
1. Add an internal **Price description** and [Lookup key](https://docs.stripe.com/products-prices/manage-prices.md#lookup-keys) to organize, query, and update specific prices in the future.
1. Click **Next**. Then click **Add product**.

After you create the product and the price, record the price ID so you can use it in subsequent steps. The pricing page displays the ID and it looks similar to this: `price_G0FvDp6vZvdwRZ`.

## Create or retrieve a Customer [Server-side]

To save an Amazon Pay payment method for future payments, you must attach it to a _Customer_ (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments).

Create a `Customer` object after your customer creates an account on your business. Associating the ID of the `Customer` object with your own internal representation of a customer enables you to retrieve and use the payment method details that you store later. If your customer hasn’t created an account, you can still create a `Customer` object and associate it with your internal representation of their account at a later point.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create({
  description: "My First Test Customer (created for API docs)",
});
```

## Create a SetupIntent [Server-side]

Create a [SetupIntent](https://docs.stripe.com/api/setup_intents.md) to save a customer’s payment method for future payments. A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) is an object that represents your intent to set up a customer’s payment method for future payments. The SetupIntent tracks the steps of this set up process.

Create a SetupIntent on your server with [payment_method_types](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-payment_method_types) set to `amazon_pay` and specify the Customer’s ID and [usage=off_session](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-usage) or `usage=on_session`.

```curl
curl https://api.stripe.com/v1/setup_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d confirm=true \
  --data-urlencode "return_url=https://www.stripe.com" \
  -d usage=off_session \
  -d customer=cus_ODQluYFNl44ODI \
  -d "payment_method_data[type]=amazon_pay" \
  -d "payment_method_types[]=amazon_pay" \
  -d "mandate_data[customer_acceptance][type]=online" \
  -d "mandate_data[customer_acceptance][online][ip_address]=127.0.0.0" \
  -d "mandate_data[customer_acceptance][online][user_agent]=device"
```

The SetupIntent object contains a `client_secret`, which is a unique key that you must pass to Stripe.js on the client side to redirect your buyer to Amazon Pay and authorize the mandate.

### Retrieve the client secret

The SetupIntent includes a _client secret_ (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)) that the client side uses to securely complete the payment process. You can use different approaches to pass the client secret to the client side.

#### Single-page application

Retrieve the client secret from an endpoint on your server, using the browser’s `fetch` function. This approach is best if your client side is a single-page application, particularly one built with a modern frontend framework like React. Create the server endpoint that serves the client secret:

#### Node.js

```javascript
const express = require("express");
const app = express();

app.get("/secret", async (req, res) => {
  const intent = // ... Fetch or create the SetupIntent
    res.json({ client_secret: intent.client_secret });
});

app.listen(3000, () => {
  console.log("Running on port 3000");
});
```

And then fetch the client secret with JavaScript on the client side:

```javascript
(async () => {
  const response = await fetch("/secret");
  const { client_secret: clientSecret } = await response.json();
  // Render the form using the clientSecret
})();
```

#### Server-side rendering

Pass the client secret to the client from your server. This approach works best if your application generates static content on the server before sending it to the browser.

Add the [client_secret](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-client_secret) in your checkout form. In your server-side code, retrieve the client secret from the SetupIntent:

#### Node.js

```html
<form id="payment-form" data-secret="{{ client_secret }}">
  <div id="payment-element">
    <!-- Elements will create form elements here -->
  </div>

  <button id="submit">Submit</button>
</form>
```

```javascript
const express = require("express");
const expressHandlebars = require("express-handlebars");
const app = express();

app.engine(".hbs", expressHandlebars({ extname: ".hbs" }));
app.set("view engine", ".hbs");
app.set("views", "./views");

app.get("/checkout", async (req, res) => {
  const intent = // ... Fetch or create the SetupIntent
    res.render("checkout", { client_secret: intent.client_secret });
});

app.listen(3000, () => {
  console.log("Running on port 3000");
});
```

Next, save Amazon Pay on the client with [Stripe.js](https://docs.stripe.com/payments/elements.md).

Include the Stripe.js script on your checkout page by adding it to the `head` of your HTML file.

```html
<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/dahlia/stripe.js"></script>
</head>
```

When a customer clicks to pay with Amazon Pay, use Stripe.js to submit the payment to Stripe. [Stripe.js](https://docs.stripe.com/payments/elements.md) is the foundational JavaScript library for building payment flows. It automatically handles complexities like the redirect described below, and enables you to extend your integration to other payment methods. Include the Stripe.js script on your checkout page by adding it to the `head` of your HTML file.

```html
<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/dahlia/stripe.js"></script>
</head>
```

Create an instance of Stripe.js with the following JavaScript on your checkout page.

```javascript
// Set your publishable key. Remember to change this to your live publishable key in production!
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");
```

Use `stripe.confirmAmazonPaySetup` to confirm the setupIntent on the client side, with a [return_url](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-return_url) and [mandate_data](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-mandate_data). Use the [return_url](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-return_url) to redirect customers to a specific page after the SetupIntent succeeds.

```javascript
// Redirects away from the client
const { error } = await stripe.confirmAmazonPaySetup(
  "{{SETUP_INTENT_CLIENT_SECRET}}",
  {
    return_url: "https://example.com/setup/complete",
    mandate_data: {
      customer_acceptance: {
        type: "online",
        online: {
          infer_from_client: true,
        },
      },
    },
  },
);

if (error) {
  // Inform the customer that there was an error.
}
```

## Create a subscription [Server-side]

Create a subscription that has a price and a customer. Set the value of the `default_payment_method` parameter to the PaymentMethod ID from the SetupIntent response.

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
  off_session: true,
});
```

Creating subscriptions automatically charges customers due to the pre-set default payment method. After a successful payment, the status in the Stripe Dashboard changes to **Active**. The price that you previously set up determines the amount for future billings. Learn how to [create a subscription with a free trial period](https://docs.stripe.com/billing/subscriptions/trials.md).

# Payment Intents API

> This is a Payment Intents API for when api-integration is subscription. View the full page at https://docs.stripe.com/billing/subscriptions/amazon-pay?api-integration=subscription.

Create and confirm a Subscription using two API calls. The [first API call](https://docs.stripe.com/billing/subscriptions/amazon-pay.md#pi-create-subscription) sends customer and product information to the [Subscriptions API](https://docs.stripe.com/api/subscriptions.md) to create a Subscription and PaymentIntent in one call. The response includes a PaymentIntent ID that you must use in a [Payment Intents API](https://docs.stripe.com/api/payment_intents.md) call to [confirm a payment](https://docs.stripe.com/billing/subscriptions/amazon-pay.md#pi-confirm-payment).

## Create a product and price [Dashboard]

[Products](https://docs.stripe.com/api/products.md) represent the item or service you’re selling. [Prices](https://docs.stripe.com/api/prices.md) define how much and how frequently you charge for a product. This includes how much the product costs, what currency you accept, and whether it’s a one-time or recurring charge. If you only have a few products and prices, create and manage them in the Dashboard.

This guide uses a stock photo service as an example and charges customers a 15 USD monthly subscription. To model this:

1. Go to the [Products](https://dashboard.stripe.com/products?active=true) page and click **Create product**.
1. Enter a **Name** for the product. You can optionally add a **Description** and upload an image of the product.
1. Select a **Product tax code**. Learn more about [product tax codes](https://docs.stripe.com/tax/tax-codes.md).
1. Select **Recurring**. Then enter **15** for the price and select **USD** as the currency.
1. Choose whether to **Include tax in price**. You can either use the default value from your [tax settings](https://dashboard.stripe.com/test/settings/tax) or set the value manually. In this example, select **Auto**.
1. Select **Monthly** for the **Billing period**.
1. Click **More pricing options**. Then select **Flat rate** as the pricing model for this example. Learn more about [flat rate](https://docs.stripe.com/products-prices/pricing-models.md#flat-rate) and other [pricing models](https://docs.stripe.com/products-prices/pricing-models.md).
1. Add an internal **Price description** and [Lookup key](https://docs.stripe.com/products-prices/manage-prices.md#lookup-keys) to organize, query, and update specific prices in the future.
1. Click **Next**. Then click **Add product**.

After you create the product and the price, record the price ID so you can use it in subsequent steps. The pricing page displays the ID and it looks similar to this: `price_G0FvDp6vZvdwRZ`.

## Create a subscription [Server-side]

Create a [subscription](https://docs.stripe.com/api/subscriptions.md) that has a price and a customer with the `incomplete` status by providing the [payment_behavior](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-payment_behavior) parameter with a value of `default_incomplete`. Set the `payment_settings.save_default_payment_method=on_subscription` parameter to save a payment method when a subscription is activated.

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
    payment_method_types: ["amazon_pay", "card"],
  },
  expand: ["latest_invoice.payments", "latest_invoice.confirmation_secret"],
});
```

The response includes the _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis)’s first [Invoice](https://docs.stripe.com/api/invoices.md). This contains the invoice’s payments, which includes a default PaymentIntent that Stripe generated for this invoice and the confirmation secret which you can use on the client side to securely complete the payment process instead of passing the entire PaymentIntent object. Get the PaymentIntent ID that you must use to confirm a payment from `latest_invoice.payments`. Return the `latest_invoice.confirmation_secret.client_secret` to the front end to complete payment. Learn how to [create a subscription with a free trial period](https://docs.stripe.com/billing/subscriptions/trials.md).

## Confirm a payment [Server-side]

Confirm a payment with [PaymentIntents](https://docs.stripe.com/api/payment_intents.md) using the PaymentIntent ID from the Subscriptions response. And then add the PaymentIntent ID to the URL path and set the value of the `payment_method_types` parameter to `amazon_pay`:

```curl
curl https://api.stripe.com/v1/payment_intents/:id/confirm \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "payment_method_data[type]=amazon_pay" \
  --data-urlencode "return_url=https://www.stripe.com" \
  -d "mandate_data[customer_acceptance][type]=online" \
  -d "mandate_data[customer_acceptance][online][ip_address]=127.0.0.0" \
  -d "mandate_data[customer_acceptance][online][user_agent]=device" \
  -d "mandate_data[customer_acceptance][accepted_at]=1660000000"
```

The PaymentIntent response includes the status `requires_action`, which indicates that your users must authenticate with Amazon Pay to complete the PaymentIntent. After a successful payment, the subscription becomes active and saves the payment method as the default payment method.

# Stripe-hosted page

> This is a Stripe-hosted page for when api-integration is checkout. View the full page at https://docs.stripe.com/billing/subscriptions/amazon-pay?api-integration=checkout.

You can use the [Checkout API](https://docs.stripe.com/api/checkout/sessions.md) to create and confirm a subscription with a prebuilt checkout page.

## Create a product and price [Dashboard]

[Products](https://docs.stripe.com/api/products.md) represent the item or service you’re selling. [Prices](https://docs.stripe.com/api/prices.md) define how much and how frequently you charge for a product. This includes how much the product costs, what currency you accept, and whether it’s a one-time or recurring charge. If you only have a few products and prices, create and manage them in the Dashboard.

This guide uses a stock photo service as an example and charges customers a 15 USD monthly subscription. To model this:

1. Go to the [Products](https://dashboard.stripe.com/products?active=true) page and click **Create product**.
1. Enter a **Name** for the product. You can optionally add a **Description** and upload an image of the product.
1. Select a **Product tax code**. Learn more about [product tax codes](https://docs.stripe.com/tax/tax-codes.md).
1. Select **Recurring**. Then enter **15** for the price and select **USD** as the currency.
1. Choose whether to **Include tax in price**. You can either use the default value from your [tax settings](https://dashboard.stripe.com/test/settings/tax) or set the value manually. In this example, select **Auto**.
1. Select **Monthly** for the **Billing period**.
1. Click **More pricing options**. Then select **Flat rate** as the pricing model for this example. Learn more about [flat rate](https://docs.stripe.com/products-prices/pricing-models.md#flat-rate) and other [pricing models](https://docs.stripe.com/products-prices/pricing-models.md).
1. Add an internal **Price description** and [Lookup key](https://docs.stripe.com/products-prices/manage-prices.md#lookup-keys) to organize, query, and update specific prices in the future.
1. Click **Next**. Then click **Add product**.

After you create the product and the price, record the price ID so you can use it in subsequent steps. The pricing page displays the ID and it looks similar to this: `price_G0FvDp6vZvdwRZ`.

## Create a Checkout Session [Server-side]

Your customer must authorize you to use their Amazon account for future payments through Stripe Checkout. This allows you to accept Amazon payments. Add a checkout button to your website that calls a server-side endpoint to create a [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md).

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

Create a Checkout Session in `subscription` mode to collect the required information. After creating the Checkout Session, redirect your customer to the [URL](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-url) that the response returns.

```curl
curl https://api.stripe.com/v1/checkout/sessions \
  -u "<<YOUR_SECRET_KEY>>:" \
  --data-urlencode "success_url=https://example.com/success" \
  -d "line_items[0][price]={{RECURRING_PRICE_ID}}" \
  -d "line_items[0][quantity]=1" \
  -d "payment_method_types[0]=card" \
  -d "payment_method_types[1]=amazon_pay" \
  -d mode=subscription
```

## Test your integration [Server-side]

Select Amazon Pay as the payment method and tap Subscribe. You can test the successful payment case by authenticating the payment on the redirect page. The PaymentIntent transitions from `requires_action` to `succeeded`.
