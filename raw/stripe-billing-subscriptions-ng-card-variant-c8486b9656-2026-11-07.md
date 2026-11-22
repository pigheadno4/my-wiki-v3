<!-- Source URL: https://docs.stripe.com/billing/subscriptions/ng-card?api-integration=setupintents -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Set up a subscription with Nigerian cards

Learn how to create and charge a subscription with Nigerian cards.

Set up a *subscription* (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) using [Naira card](https://docs.stripe.com/payments/ng-card/accept-a-payment.md) as a payment method.

# SetupIntents API


Create and confirm a Subscription using two API calls. The [first API call](https://docs.stripe.com/billing/subscriptions/ng-card.md#create-setup-intent) sends customer and product information to the [Subscriptions API](https://docs.stripe.com/api/subscriptions.md) to create a Subscription and PaymentIntent in one call. The response includes a PaymentIntent ID that you must use in a [Payment Intents API](https://docs.stripe.com/api/payment_intents.md) call to confirm a payment.

## Create a product and price [Dashboard]

[Products](https://docs.stripe.com/api/products.md) represent the item or service you’re selling. [Prices](https://docs.stripe.com/api/prices.md) define how much and how frequently you charge for a product. This includes how much the product costs, what currency you accept, and whether it’s a one-time or recurring charge. If you only have a few products and prices, create and manage them in the Dashboard.

This guide uses a stock photo service as an example and charges customers a 100,000 NGN monthly subscription. To model this:

1. Go to the [Products](https://dashboard.stripe.com/products?active=true) page and click **Create product**.
2. Enter a **Name** for the product. You can optionally add a **Description** and upload an image of the product.
3. Select a **Product tax code**. Learn more about [product tax codes](https://docs.stripe.com/tax/tax-codes.md).
4. Select **Recurring**. Then enter **100,000** for the price and select **NGN** as the currency.
5. Choose whether to **Include tax in price**. You can either use the default value from your [tax settings](https://dashboard.stripe.com/test/settings/tax) or set the value manually. In this example, select **Auto**.
6. Select **Monthly** for the **Billing period**.
7. Click **More pricing options**. Then select **Flat rate** as the pricing model for this example. Learn more about [flat rate](https://docs.stripe.com/products-prices/pricing-models.md#flat-rate) and other [pricing models](https://docs.stripe.com/products-prices/pricing-models.md).
8. Add an internal **Price description** and [Lookup key](https://docs.stripe.com/products-prices/manage-prices.md#lookup-keys) to organize, query, and update specific prices in the future.
9. Click **Next**. Then click **Add product**.

After you create the product and the price, record the price ID so you can use it in subsequent steps. The pricing page displays the ID and it looks similar to this: `price_G0FvDp6vZvdwRZ`.

> You must convert your prices to NGN to use the payment method.

## Create a SetupIntent [Server-side]

Create a [SetupIntent](https://docs.stripe.com/api/setup_intents.md) to save a customer’s payment method for future payments. The `SetupIntent` tracks the steps of this setup process.

```curl
curl https://api.stripe.com/v1/setup_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d confirm=true \
  --data-urlencode "return_url=https://www.stripe.com" \
  -d usage=off_session \
  -d "customer={{CUSTOMER_ID}}" \
  -d "payment_method_data[type]=ng_card" \
  -d "automatic_payment_methods[enabled]=true" \
  -d "mandate_data[customer_acceptance][type]=online" \
  -d "mandate_data[customer_acceptance][online][ip_address]=127.0.0.0" \
  -d "mandate_data[customer_acceptance][online][user_agent]=device"
```

The SetupIntent object contains a unique `client_secret`. Pass it to Stripe.js on the client side to redirect your customer to our local processor’s checkout page and authorize the mandate.

## Create a subscription [Server-side]

Create a subscription that has a price and a customer. Set the value of the `default_payment_method` parameter to the PaymentMethod ID from the SetupIntent response.

```curl
curl https://api.stripe.com/v1/subscriptions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d customer={{CUSTOMER_ID}} \
  -d "items[0][price]={{PRICE_ID}}" \
  -d default_payment_method={{PAYMENT_METHOD_ID}} \
  -d off_session=true
```

Creating subscriptions automatically charges customers based on the preset default payment method. After a successful payment, the status in the Stripe Dashboard changes to `Active`. The price that you previously set determines the amount for future billings. Learn how to [create a subscription with a free trial period](https://docs.stripe.com/billing/subscriptions/trials/free-trials.md).

## Confirm a payment [Server-side]

Confirm a payment with [PaymentIntents](https://docs.stripe.com/api/payment_intents.md) using the PaymentIntent ID from the Subscriptions response. Add the PaymentIntent ID to the URL path:

```curl
curl https://api.stripe.com/v1/payment_intents/:id/confirm \
  -u "<<YOUR_SECRET_KEY>>:" \
  --data-urlencode "return_url=https://www.stripe.com" \
  -d "payment_method_data[]=type" \
  -d "payment_method_data[]=ng_card"
```

The PaymentIntent response includes the status `requires_action`. This status indicates that the customer must complete the payment with the payment method they selected to complete the PaymentIntent. After a successful payment, the subscription becomes active and saves the payment method as the default payment method.

