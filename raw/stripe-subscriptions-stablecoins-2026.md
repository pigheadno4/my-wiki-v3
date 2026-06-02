<!-- Source URL: https://docs.stripe.com/billing/subscriptions/stablecoins -->
<!-- Fetched: 2026-05-13 -->

# Set up a subscription with stablecoin payments

Learn how to create and charge for a subscription with stablecoins.

Use this guide to set up a _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) that withdraws recurring _stablecoin_ (A cryptocurrency that's pegged to the value of a fiat currency or other asset in order to limit volatility) payments from a customer’s crypto wallet.

# Stripe-hosted page

> This is a Stripe-hosted page for when api-integration is checkout. View the full page at https://docs.stripe.com/billing/subscriptions/stablecoins?api-integration=checkout.

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

Your customer must authorize you to use their crypto wallet for future payments through Stripe.

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

Create a Checkout Session in `subscription` mode to collect the required information. After creating the Checkout Session, redirect your customer to the [URL](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-url) that the response returns.

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
  payment_method_types: ["crypto"],
  mode: "subscription",
});
```

## Confirm the payment is successful

When your customer completes a payment, Stripe redirects them to the URL that you specified in the `success_url` parameter. Typically, this is a page on your website that informs your customer that their payment was successful.

After the payment succeeds, the underlying _PaymentIntent_ (The Payment Intents API tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by regulatory mandates, custom Radar fraud rules, or redirect-based payment methods) status changes from `processing` to `succeeded`.

You can confirm the payment is successful in several ways:

#### Dashboard

Successful payments display in the Dashboard’s [list of payments](https://dashboard.stripe.com/payments). When you click a payment, it takes you to the payment details page. The **Checkout summary** section contains billing information and the list of items purchased, which you can use to manually fulfill the order.
![](assets/stripe-ach-checkout-success.png)

> Stripe can help you keep up with incoming payments by sending you email notifications whenever a customer successfully completes one. Use the Dashboard to [configure email notifications](https://dashboard.stripe.com/settings/user).

#### Webhooks

We send the following Checkout events when the payment status changes:

| Event Name                                                                                                       | Description                                                                           | Next steps                                                          |
| ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| [checkout.session.completed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.completed) | The customer has successfully authorized the payment by submitting the Checkout form. | Wait for the payment to succeed or fail.                            |
| [invoice.paid](https://docs.stripe.com/api/events/types.md#event_types-invoice.paid)                             | The customer’s payment succeeded.                                                     | Fulfill the goods or services that the customer purchased.          |
| [invoice.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-invoice.payment_failed)         | The customer’s payment was declined, or failed for some other reason.                 | Email the customer and request that they attempt the payment again. |

Your webhook code needs to handle all of these Checkout events.

Each Checkout webhook payload includes the [Checkout Session object](https://docs.stripe.com/api/checkout/sessions.md) and invoice webhooks include the [Invoice](https://docs.stripe.com/api/invoices/object.md) object. Both contain information about the _Customer_ (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) and _PaymentIntent_ (The Payment Intents API tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by regulatory mandates, custom Radar fraud rules, or redirect-based payment methods). .

Stripe sends the `checkout.session.completed` webhook to your server before redirecting your customer. Your webhook acknowledgement (any `2xx` status code) triggers the customer’s redirect to the `success_url`. If Stripe doesn’t receive successful acknowledgement within 10 seconds of a successful payment, your customer automatically redirects to the `success_url` page.

We recommend [using webhooks](https://docs.stripe.com/webhooks.md) to confirm the payment has succeeded and fulfill the goods or services the customer purchased. Below is an example webhook endpoint that handles the success or failure of a payment:

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

// Find your endpoint's secret in your Dashboard's webhook settings
const endpointSecret = "whsec_...";

// Using Express
const app = require("express")();

// Use body-parser to retrieve the raw body as a buffer
const bodyParser = require("body-parser");

// Match the raw body to content type application/json
app.post(
  "/webhook",
  bodyParser.raw({ type: "application/json" }),
  (request, response) => {
    const sig = request.headers["stripe-signature"];

    let event;

    try {
      event = stripe.webhooks.constructEvent(request.body, sig, endpointSecret);
    } catch (err) {
      return response.status(400).send(`Webhook Error: ${err.message}`);
    }

    switch (event.type) {
      case "checkout.session.completed": {
        const session = event.data.object;
        const subscriptionId = session.subscription;

        // Find the subscription or save it to your database.
        // invoice.paid may have fired before this so there
        // could already be a subscription.
        findOrCreateSubscription(subscriptionId);

        break;
      }

      case "invoice.paid": {
        const invoice = event.data.object;
        const subscriptionId = invoice.parent.subscription_details.subscription;

        // Find the subscription or save it to your database.
        // checkout.session.completed may not have fired yet
        // so we may need to create the subscription.
        const subscription = findOrCreateSubscription(subscriptionId);

        // Fulfill the purchase
        fulfillOrder(invoice);

        // Record that the subscription has been paid for
        // this payment period. invoice.paid will fire every
        // time there is a payment made for this subscription.
        recordAsPaidForThisPeriod(subscription);

        break;
      }

      case "invoice.payment_failed": {
        const invoice = event.data.object;

        // Send an email to the customer asking them to retry their payment
        emailCustomerAboutFailedPayment(invoice);

        break;
      }
    }

    // Return a response to acknowledge receipt of the event
    response.json({ received: true });
  },
);
```

You can get information about the customer, payment, or subscription by retrieving the `Customer`, `PaymentIntent`, or `Subscription` objects referenced by the `customer`, `payment_intent`, and `subscription` properties in the webhook payload.

### Retrieving line items from webhook

By default, Checkout webhooks don’t return `line_items`. To retrieve the items created with the Checkout Session, make an additional request with the Checkout Session id:

#### curl

```bash
curl https://api.stripe.com/v1/checkout/sessions/{{CHECKOUT_SESSION_ID}}/line_items \
  -u <<YOUR_SECRET_KEY>>:
```

#### Stripe CLI

```bash
stripe get /v1/checkout/sessions/{{CHECKOUT_SESSION_ID}}/line_items
```

### Testing webhooks locally

To test webhooks locally, you can use the [Stripe CLI](https://docs.stripe.com/stripe-cli.md). After you install it, you can forward events to your server:

```bash
stripe listen --forward-to localhost:4242/webhook
Ready! Your webhook signing secret is '{{WEBHOOK_SIGNING_SECRET}}' (^C to quit)
```

Learn more about [setting up webhooks](https://docs.stripe.com/webhooks.md).

#### Third-party plugins

You can use plugins such as [Zapier](https://stripe.com/works-with/zapier) to automate updating your purchase fulfillment systems with information from Stripe payments.

Some examples of automation supported by plugins include:

- Updating spreadsheets used for order tracking in response to successful payments
- Updating inventory management systems in response to successful payments
- Triggering notifications to internal customer service teams using email or chat applications

## Test your integration

Test your crypto payment integration by opening the payment redirect page using your test API keys. You can test a successful payment flow at no cost using [testnet assets](https://docs.stripe.com/billing/subscriptions/stablecoins.md#testnet-assets).

1. In a _sandbox_ (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes), create a new transaction using your chosen integration method, and open its redirect URL.
1. Connect your preferred wallet and payment network.
1. Complete the payment, and validate that you’re redirected to the expected URL.

### Test payments with testnet assets

Most cryptocurrencies offer testnet assets, or tokens that have no monetary value, that you can use to test blockchain transactions. Stripe recommends the MetaMask wallet, Polygon Amoy testnet, and Circle faucet for testing, but you can use your own preferred services.

#### Install a wallet

1. [Download the MetaMask extension](https://metamask.io/download) for your web browser.
1. [Create a new wallet](https://support.metamask.io/start/creating-a-new-wallet/) or [import an existing one](https://support.metamask.io/start/use-an-existing-wallet/).

#### Enable a testnet

1. In your MetaMask wallet, select **Networks** from the main menu.
1. Click **Add custom network**.
1. Enter the following details:
   - **Network name**: `Amoy`
   - **Default RPC URL**: `https://rpc-amoy.polygon.technology/`
   - **Chain ID**: `80002`
   - **Currency symbol**: `POL`
   - **Block explorer URL**: `https://amoy.polygonscan.com/`
1. Click **Save**.

#### Import a token

1. In your MetaMask wallet, under **Tokens**, select **Amoy** from the network dropdown.
1. Click the overflow menu (⋯), and select **Import tokens**.
1. Click **Select a network** > **Amoy**.
1. Under **Token contract address**, paste the Polygon Amoy testnet contract address:
   ```
   0x41E94Eb019C0762f9Bfcf9Fb1E58725BfB0e7582
   ```
   The **Token symbol** field automatically updates with `USDC` and the **Decimals** field with `6`.
1. Click **Next**.
1. Verify that you’re importing the `USDC` token, and then click **Import**.

Your MetaMask wallet now shows **POL** and **USDC** in the tokens list.

When testing refunds, the token sent to your wallet might have a different contract than the one used for payment. We recommend reviewing the [transaction_hash](https://docs.stripe.com/api/refunds/object.md?rds=1#refund_object-destination_details-crypto-reference) of your refund on block explorer, and adding that token’s contract to your wallet. For example, you might see a `0x58277ebcabbe2a6694fbca8daf9e23163dbacf3e` token contract address for Sepolia ETH USDC refunds.

#### Get testnet assets

> To use some testnet faucets, you might need to hold a small amount of mainnet tokens.

1. Open [faucet.circle.com](https://faucet.circle.com/)
1. Click **USDC**.
1. Under **Network**, select **Polygon PoS Amoy**.
1. Under **Send to**, paste your wallet address.
1. Click **Send 20 USDC**.

In addition to USDC for making payments, you need POL to pay transaction costs:

1. Open [faucet.polygon.technology](https://faucet.polygon.technology/).
1. Under **Select Chain & Token**, select **Polygon Amoy** and **POL**.
1. Under **Verify your identity**, click the third-party platform you want to authenticate with, and complete the login process.
1. Under **Enter Wallet Address**, paste your wallet address.
1. Click **Claim**.

Testnet transactions can take a few minutes to complete. Check your wallet to confirm that the USDC and POL has transferred.

### More testnet faucets

Check these faucet services for more testing token options:

- [Paxos USDP](https://faucet.paxos.com/)
- [Devnet SOL](https://faucet.solana.com/)
- [Sepolia ETH](https://faucets.chain.link/sepolia)
- [Amoy POL](https://faucet.polygon.technology/)

# Payment Intents API

> This is a Payment Intents API for when api-integration is paymentintents. View the full page at https://docs.stripe.com/billing/subscriptions/stablecoins?api-integration=paymentintents.

## Create a product and price [Dashboard]

[Products](https://docs.stripe.com/api/products.md) represent the item or service you’re selling. [Prices](https://docs.stripe.com/api/prices.md) define how much and how frequently you charge for a product. This includes how much the product costs, what currency you accept, and whether it’s a one-time or recurring charge. If you only have a few products and prices, create and manage them in the Dashboard.

This guide uses a stock photo service as an example and charges customers a 15 USDC monthly subscription. To model this:

1. Go to the [Products](https://dashboard.stripe.com/products?active=true) page and click **Create product**.
1. Enter a **Name** for the product. You can optionally add a **Description** and upload an image of the product.
1. Select a **Product tax code**. Learn more about [product tax codes](https://docs.stripe.com/tax/tax-codes.md).
1. Select **Recurring**. Then enter **15** for the price and select **USDC** as the currency.
1. Choose whether to **Include tax in price**. You can either use the default value from your [tax settings](https://dashboard.stripe.com/test/settings/tax) or set the value manually. In this example, select **Auto**.
1. Select **Monthly** for the **Billing period**.
1. Click **More pricing options**. Then select **Flat rate** as the pricing model for this example. Learn more about [flat rate](https://docs.stripe.com/products-prices/pricing-models.md#flat-rate) and other [pricing models](https://docs.stripe.com/products-prices/pricing-models.md).
1. Add an internal **Price description** and [Lookup key](https://docs.stripe.com/products-prices/manage-prices.md#lookup-keys) to organize, query, and update specific prices in the future.
1. Click **Next**. Then click **Add product**.

After you create the product and the price, record the price ID so you can use it in subsequent steps. The pricing page displays the ID and it looks similar to this: `price_G0FvDp6vZvdwRZ`.

## Create a subscription [Server-side]

Create a subscription with a price and a customer. Set the [payment_behavior](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-payment_behavior) value to `default_incomplete` so the subscription status remains `incomplete` until the user completes payment. Set the `payment_settings.save_default_payment_method` parameter to `on_subscription` to save the payment method once the subscription is activated.

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
    payment_method_types: ["crypto"],
  },
  expand: ["latest_invoice.payments", "latest_invoice.confirmation_secret"],
});
```

The API response includes the subscription’s first [Invoice](https://docs.stripe.com/api/invoices.md). Use the included PaymentIntent ID in `latest_invoice.payments` to confirm the subscription in the next step.

## Create a PaymentIntent [Server-side]

Call the [Payment Intents API](https://docs.stripe.com/api/payment_intents.md) to initiate payment. Set the value of `payment_intents_id` to the PaymentIntents ID returned by the Subscriptions API in the previous step. Set the value of the `payment_method_types` parameter to `crypto`:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.confirm(":id", {
  payment_method_data: {
    type: "crypto",
  },
  return_url: "https://www.example.com",
  mandate_data: {
    customer_acceptance: {
      type: "online",
      online: {
        ip_address: "127.0.0.0",
        user_agent: "device",
      },
      accepted_at: 1660000000,
    },
  },
});
```

The API response object includes the status `requires_action`, and a redirect URL in [next_action.redirect_to_url.url](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-redirect_to_url-url). Redirect the customer to this URL to complete the subscription payment setup. After they complete the payment flow, they’re redirected back to the [return_url](https://docs.stripe.com/api/payment_intents/create.md#create_setup_intent-return_url) you provided.

## Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

- **Handle events manually in the Dashboard**

  Use the Dashboard to [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments), send email receipts, handle payouts, or retry failed payments.

- **Build a custom webhook**

  [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook) handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- **Integrate a prebuilt app**

  Handle common business events, such as [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

## Test your integration

Test your crypto payment integration by opening the payment redirect page using your test API keys. You can test a successful payment flow at no cost using [testnet assets](https://docs.stripe.com/billing/subscriptions/stablecoins.md#testnet-assets).

1. In a _sandbox_ (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes), create a new transaction using your chosen integration method, and open its redirect URL.
1. Connect your preferred wallet and payment network.
1. Complete the payment, and validate that you’re redirected to the expected URL.

### Test payments with testnet assets

Most cryptocurrencies offer testnet assets, or tokens that have no monetary value, that you can use to test blockchain transactions. Stripe recommends the MetaMask wallet, Polygon Amoy testnet, and Circle faucet for testing, but you can use your own preferred services.

#### Install a wallet

1. [Download the MetaMask extension](https://metamask.io/download) for your web browser.
1. [Create a new wallet](https://support.metamask.io/start/creating-a-new-wallet/) or [import an existing one](https://support.metamask.io/start/use-an-existing-wallet/).

#### Enable a testnet

1. In your MetaMask wallet, select **Networks** from the main menu.
1. Click **Add custom network**.
1. Enter the following details:
   - **Network name**: `Amoy`
   - **Default RPC URL**: `https://rpc-amoy.polygon.technology/`
   - **Chain ID**: `80002`
   - **Currency symbol**: `POL`
   - **Block explorer URL**: `https://amoy.polygonscan.com/`
1. Click **Save**.

#### Import a token

1. In your MetaMask wallet, under **Tokens**, select **Amoy** from the network dropdown.
1. Click the overflow menu (⋯), and select **Import tokens**.
1. Click **Select a network** > **Amoy**.
1. Under **Token contract address**, paste the Polygon Amoy testnet contract address:
   ```
   0x41E94Eb019C0762f9Bfcf9Fb1E58725BfB0e7582
   ```
   The **Token symbol** field automatically updates with `USDC` and the **Decimals** field with `6`.
1. Click **Next**.
1. Verify that you’re importing the `USDC` token, and then click **Import**.

Your MetaMask wallet now shows **POL** and **USDC** in the tokens list.

When testing refunds, the token sent to your wallet might have a different contract than the one used for payment. We recommend reviewing the [transaction_hash](https://docs.stripe.com/api/refunds/object.md?rds=1#refund_object-destination_details-crypto-reference) of your refund on block explorer, and adding that token’s contract to your wallet. For example, you might see a `0x58277ebcabbe2a6694fbca8daf9e23163dbacf3e` token contract address for Sepolia ETH USDC refunds.

#### Get testnet assets

> To use some testnet faucets, you might need to hold a small amount of mainnet tokens.

1. Open [faucet.circle.com](https://faucet.circle.com/)
1. Click **USDC**.
1. Under **Network**, select **Polygon PoS Amoy**.
1. Under **Send to**, paste your wallet address.
1. Click **Send 20 USDC**.

In addition to USDC for making payments, you need POL to pay transaction costs:

1. Open [faucet.polygon.technology](https://faucet.polygon.technology/).
1. Under **Select Chain & Token**, select **Polygon Amoy** and **POL**.
1. Under **Verify your identity**, click the third-party platform you want to authenticate with, and complete the login process.
1. Under **Enter Wallet Address**, paste your wallet address.
1. Click **Claim**.

Testnet transactions can take a few minutes to complete. Check your wallet to confirm that the USDC and POL has transferred.

### More testnet faucets

Check these faucet services for more testing token options:

- [Paxos USDP](https://faucet.paxos.com/)
- [Devnet SOL](https://faucet.solana.com/)
- [Sepolia ETH](https://faucets.chain.link/sepolia)
- [Amoy POL](https://faucet.polygon.technology/)

# Setup Intents API

> This is a Setup Intents API for when api-integration is setupintents. View the full page at https://docs.stripe.com/billing/subscriptions/stablecoins?api-integration=setupintents.

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

## Create a SetupIntent [Server-side]

Create a [SetupIntent](https://docs.stripe.com/api/setup_intents.md) to save a customer’s payment method for future payments. The SetupIntent tracks the steps of this set up process.

Create a SetupIntent on your server with [payment_method_types](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-payment_method_types) set to `crypto` and specify the Customer’s ID and [usage=off_session](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-usage).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  confirm: true,
  return_url: "https://www.example.com",
  usage: "off_session",
  customer: "cus_00000000000000",
  payment_method_data: {
    type: "crypto",
  },
  payment_method_types: ["crypto"],
  mandate_data: {
    customer_acceptance: {
      type: "online",
      online: {
        ip_address: "127.0.0.0",
        user_agent: "device",
      },
    },
  },
});
```

The API response object includes a [payment_method](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-payment_method) ID, and a redirect URL in [next_action.redirect_to_url.url](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-next_action-redirect_to_url-url). Redirect the customer to this URL to complete the subscription payment setup. After they complete the payment flow, they’re redirected back to the URL provided as your [return_url](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-return_url).

## Create a subscription [Server-side]

Create a subscription that has a price and a customer. Set the value of the `default_payment_method` parameter to the `payment_method` ID from the SetupIntent response.

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

Creating subscriptions automatically charges customers due to the pre-set default payment method. After a successful payment, the status in the Stripe Dashboard changes to **Active**. The price that you previously set determines the amount for future billings.

## Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

- **Handle events manually in the Dashboard**

  Use the Dashboard to [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments), send email receipts, handle payouts, or retry failed payments.

- **Build a custom webhook**

  [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook) handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- **Integrate a prebuilt app**

  Handle common business events, such as [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

## Test your integration

Test your crypto payment integration by opening the payment redirect page using your test API keys. You can test a successful payment flow at no cost using [testnet assets](https://docs.stripe.com/billing/subscriptions/stablecoins.md#testnet-assets).

1. In a _sandbox_ (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes), create a new transaction using your chosen integration method, and open its redirect URL.
1. Connect your preferred wallet and payment network.
1. Complete the payment, and validate that you’re redirected to the expected URL.

### Test payments with testnet assets

Most cryptocurrencies offer testnet assets, or tokens that have no monetary value, that you can use to test blockchain transactions. Stripe recommends the MetaMask wallet, Polygon Amoy testnet, and Circle faucet for testing, but you can use your own preferred services.

#### Install a wallet

1. [Download the MetaMask extension](https://metamask.io/download) for your web browser.
1. [Create a new wallet](https://support.metamask.io/start/creating-a-new-wallet/) or [import an existing one](https://support.metamask.io/start/use-an-existing-wallet/).

#### Enable a testnet

1. In your MetaMask wallet, select **Networks** from the main menu.
1. Click **Add custom network**.
1. Enter the following details:
   - **Network name**: `Amoy`
   - **Default RPC URL**: `https://rpc-amoy.polygon.technology/`
   - **Chain ID**: `80002`
   - **Currency symbol**: `POL`
   - **Block explorer URL**: `https://amoy.polygonscan.com/`
1. Click **Save**.

#### Import a token

1. In your MetaMask wallet, under **Tokens**, select **Amoy** from the network dropdown.
1. Click the overflow menu (⋯), and select **Import tokens**.
1. Click **Select a network** > **Amoy**.
1. Under **Token contract address**, paste the Polygon Amoy testnet contract address:
   ```
   0x41E94Eb019C0762f9Bfcf9Fb1E58725BfB0e7582
   ```
   The **Token symbol** field automatically updates with `USDC` and the **Decimals** field with `6`.
1. Click **Next**.
1. Verify that you’re importing the `USDC` token, and then click **Import**.

Your MetaMask wallet now shows **POL** and **USDC** in the tokens list.

When testing refunds, the token sent to your wallet might have a different contract than the one used for payment. We recommend reviewing the [transaction_hash](https://docs.stripe.com/api/refunds/object.md?rds=1#refund_object-destination_details-crypto-reference) of your refund on block explorer, and adding that token’s contract to your wallet. For example, you might see a `0x58277ebcabbe2a6694fbca8daf9e23163dbacf3e` token contract address for Sepolia ETH USDC refunds.

#### Get testnet assets

> To use some testnet faucets, you might need to hold a small amount of mainnet tokens.

1. Open [faucet.circle.com](https://faucet.circle.com/)
1. Click **USDC**.
1. Under **Network**, select **Polygon PoS Amoy**.
1. Under **Send to**, paste your wallet address.
1. Click **Send 20 USDC**.

In addition to USDC for making payments, you need POL to pay transaction costs:

1. Open [faucet.polygon.technology](https://faucet.polygon.technology/).
1. Under **Select Chain & Token**, select **Polygon Amoy** and **POL**.
1. Under **Verify your identity**, click the third-party platform you want to authenticate with, and complete the login process.
1. Under **Enter Wallet Address**, paste your wallet address.
1. Click **Claim**.

Testnet transactions can take a few minutes to complete. Check your wallet to confirm that the USDC and POL has transferred.

### More testnet faucets

Check these faucet services for more testing token options:

- [Paxos USDP](https://faucet.paxos.com/)
- [Devnet SOL](https://faucet.solana.com/)
- [Sepolia ETH](https://faucets.chain.link/sepolia)
- [Amoy POL](https://faucet.polygon.technology/)
