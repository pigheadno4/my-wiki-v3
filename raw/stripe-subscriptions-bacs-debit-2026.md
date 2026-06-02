<!-- Source URL: https://docs.stripe.com/billing/subscriptions/bacs-debit -->
<!-- Fetched: 2026-05-13 -->

# Set up a subscription with Bacs Direct Debit

Learn how to create and charge for a subscription with Bacs Direct Debit.

Check out the [sample on GitHub](https://github.com/stripe-samples/checkout-single-subscription) or explore the [demo](https://checkout.stripe.dev/checkout).

Use this guide to set up a _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) using [Bacs Direct Debit](https://docs.stripe.com/payments/payment-methods/bacs-debit.md) as a payment method and _Checkout_ (A low-code payment integration that creates a customizable form for collecting payments. You can embed Checkout directly in your website, redirect customers to a Stripe-hosted payment page, or create a customized checkout page with Stripe Elements).

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create recurring products and prices

> The Prices API unifies how one-time purchases and subscriptions are modeled on Stripe. Existing integrations that don’t use the Prices API are still [supported](https://support.stripe.com/questions/prices-api-and-existing-checkout-integrations). However, some Checkout features only support Prices. See the [migration guide](https://docs.stripe.com/payments/checkout/migrating-prices.md) to upgrade to the Prices API.

To use Checkout, you first need to create a _Product_ (Products represent what your business sells—whether that's a good or a service) and a _Price_ (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions). Different physical goods or levels of service must be represented by products. Each product’s pricing is represented by one or more prices.

For example, you can create a software _product_ that has four _prices_: 10 USD/month, 100 USD/year, 9 GBP/month, and 90 GBP/year. This allows you to change and add prices without needing to change the details of your underlying products. You can create a product and price [through the API](https://docs.stripe.com/api/prices.md) or through [the Stripe Dashboard](https://dashboard.stripe.com/products).

If your price is determined at checkout (for example, the customer sets a donation amount) or you prefer not to create prices upfront, you can create [prices inline](https://docs.stripe.com/billing/subscriptions/bacs-debit.md#creating-prices-inline) at Checkout Session creation.

#### Dashboard

Before you start configuring products, make sure you’re in a sandbox. Next, define the goods and services you plan to sell. To create a new product and price:

- Go to the [Products](https://dashboard.stripe.com/products) section in the Dashboard
- Click **Add product**
- Select “Recurring” when setting the price
- Configure the pricing plan

You can define multiple pricing plans with different parameters for each recurring product. Each price has a generated ID that you can use as a reference during the checkout process.

> Products created in a sandbox can be copied to live mode so that you don’t need to re-create them. In the Product detail view in the Dashboard, click **Copy to live mode** on the upper right corner. You can only do this once for each product created in a sandbox. Subsequent updates to the test product aren’t reflected for the live product.

#### API

To create a basic [Product](https://docs.stripe.com/api/products.md) through the API, only the `name` field is required. The product `name`, `description`, and `images` that you supply are displayed to customers on Checkout.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const product = await stripe.products.create({
  name: "Blue banana",
});
```

Next, create a [Price](https://docs.stripe.com/api/prices.md) to define how much and how often to charge for your product. This includes how much the product costs, what currency to use, and its billing interval.

#### Node.js

```javascript
const price = await stripe.prices.create({
  product: "{{PRODUCT_ID}}",
  unit_amount: 1000,
  currency: "gbp",
  recurring: {
    interval: "month",
  },
});
```

This price ID is how you refer to the product when you start the payment process with Checkout.

## Create a Checkout Session [Client-side] [Server-side]

Add a checkout button to your website that calls a server-side endpoint to create a Checkout Session.

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

### Checkout Session parameters

See [Create a Checkout Session](https://docs.stripe.com/api/checkout/sessions/create.md) for a complete list of usable parameters.

Create a Checkout Session with the ID of an existing [Price](https://docs.stripe.com/api/prices.md). Make sure that mode is set to `subscription` and you pass at least one recurring price. You can add one-time prices in addition to recurring prices. After creating the Checkout Session, redirect your customer to the [URL](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-url) returned in the response.

#### Node.js

```javascript
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
  mode: "subscription",
  success_url: "https://example.com/success?session_id={CHECKOUT_SESSION_ID}",
});

// Record the session ID in your system
const session_id = session.id;

// 303 redirect to session.url
```

When your customer successfully completes their payment, they’re redirected to the `success_url`, a page on your website that informs them that their payment was successful. Make the Session ID available on your success page by including the `{CHECKOUT_SESSION_ID}` template variable in the `success_url` as in the above example.

Checkout Sessions expire 24 hours after creation by default.

From the [Dashboard](https://dashboard.stripe.com/settings/payment_methods), enable the payment methods you want to accept from your customers. Checkout supports [several payment methods](https://docs.stripe.com/payments/payment-methods/payment-method-support.md#product-support).

> Don’t rely on the redirect to the `success_url` alone for detecting payment initiation, because:
>
> - Malicious users could directly access the `success_url` without paying and gain access to your goods or services.

- After a successful payment, customers might close their browser tab before they’re redirected to the `success_url`.

## Confirm the payment is successful

When your customer completes a payment, Stripe redirects them to the URL that you specified in the `success_url` parameter. Typically, this is a page on your website that informs your customer that their payment was successful.

However, Bacs Direct Debit is a delayed notification payment method, which means that funds aren’t immediately available. Because of this, delay order _fulfillment_ (Fulfillment is the process of providing the goods or services purchased by a customer, typically after payment is collected) until the funds are available. After the payment succeeds, the underlying _PaymentIntent_ (The Payment Intents API tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by regulatory mandates, custom Radar fraud rules, or redirect-based payment methods) status changes from `processing` to `succeeded`.

You can confirm the payment is successful in several ways:

#### Dashboard

Successful payments display in the Dashboard’s [list of payments](https://dashboard.stripe.com/payments). When you click a payment, it takes you to the payment details page. The **Checkout summary** section contains billing information and the list of items purchased, which you can use to manually fulfill the order.
![](assets/stripe-ach-checkout-success.png)

> Stripe can help you keep up with incoming payments by sending you email notifications whenever a customer successfully completes one. Use the Dashboard to [configure email notifications](https://dashboard.stripe.com/settings/user).

#### Webhooks

We send the following Checkout events when the payment status changes:

| Event Name                                                                                                                                   | Description                                                                                 | Next steps                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| [checkout.session.completed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.completed)                             | The customer has successfully authorized the debit payment by submitting the Checkout form. | Wait for the payment to succeed or fail.                                            |
| [checkout.session.async_payment_succeeded](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.async_payment_succeeded) | The delayed payment method eventually succeeded.                                            | Fulfill the goods or services that the customer purchased.                          |
| [checkout.session.async_payment_failed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.async_payment_failed)       | The delayed payment method eventually failed.                                               | Email the customer and request that they attempt the payment again.                 |
| [invoice.paid](https://docs.stripe.com/api/events/types.md#event_types-invoice.paid)                                                         | The customer’s payment succeeded.                                                           | Fulfill the goods or services that the customer purchased.                          |
| [invoice.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-invoice.payment_failed)                                     | The customer’s payment was declined, or failed for some other reason.                       | Contact the customer through email and request that they attempt the payment again. |

Your webhook code needs to handle all of these Checkout events.

Each Checkout webhook payload includes the [Checkout Session object](https://docs.stripe.com/api/checkout/sessions.md) and invoice webhooks include the [Invoice](https://docs.stripe.com/api/invoices/object.md) object. Both contain information about the customer and _PaymentIntent_ (The Payment Intents API tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by regulatory mandates, custom Radar fraud rules, or redirect-based payment methods).

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

Get information about the customer, payment, or subscription by retrieving the objects referenced by the `customer` or `customer_account`, `payment_intent`, and `subscription` properties in the webhook payload.

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

## Test the integration

There are several [test bank account numbers](https://docs.stripe.com/keys.md#test-live-modes) you can use in a _sandbox_ (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes) to make sure this integration is ready. You can also use the corresponding token to skip manually entering bank account details.

| Sort code  | Account number | Token                                    | Description                                                                                                                                                                                              |
| ---------- | -------------- | ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `10-88-00` | `00012345`     | `pm_bacsDebit_success`                   | The payment succeeds and the Invoice transitions to `paid`.                                                                                                                                              |
| `10-88-00` | `90012345`     | `pm_bacsDebit_successDelayed`            | The payment succeeds after three minutes and the Invoice transitions to `paid`.                                                                                                                          |
| `10-88-00` | `33333335`     | `pm_bacsDebit_debitNotAuthorized`        | The payment fails with a `debit_not_authorized` failure code and the Invoice transitions to `open`. The Mandate becomes `inactive` and the PaymentMethod can’t be used again.                            |
| `10-88-00` | `93333335`     | `pm_bacsDebit_debitNotAuthorizedDelayed` | The payment fails after three minutes with a `debit_not_authorized` failure code and the Invoice transitions to `open`. The Mandate becomes `inactive` and the PaymentMethod can’t be used again.        |
| `10-88-00` | `22222227`     | `pm_bacsDebit_insufficientFunds`         | The payment fails with an `insufficient_funds` failure code and the Invoice transitions to `open`. The Mandate remains `active` and the PaymentMethod can be used again.                                 |
| `10-88-00` | `92222227`     | `pm_bacsDebit_insufficientFundsDelayed`  | The payment fails after three minutes with an `insufficient_funds` failure code and the Invoice transitions to `open`. The Mandate remains `active` and the PaymentMethod can be used again.             |
| `10-88-00` | `55555559`     | `pm_bacsDebit_dispute`                   | The payment succeeds after three minutes and the Invoice transitions to `paid`, but a dispute is immediately created.                                                                                    |
| `10-88-00` | `00033333`     | `pm_bacsDebit_mandateRefused`            | Payment Method creation succeeds, but the Mandate is refused by the customer’s bank and immediately transitions to `inactive`.                                                                           |
| `10-88-00` | `00044444`     | —                                        | The request to set up Bacs Direct Debit fails immediately due to an invalid account number and the customer is prompted to update their information before submitting. Payment details aren’t collected. |

You can test using any of the account numbers provided above. However, because Bacs Direct Debit payments take several days to process, use the test account numbers that operate on a three-minute delay to better simulate the behavior of live payments.

> By default, Stripe automatically sends [emails](https://docs.stripe.com/payments/payment-methods/bacs-debit.md#debit-notifications) to the customer when payment details are initially collected and each time a debit will be made on their account. These notifications aren’t sent in sandboxes.

## Optional: Adding a one-time setup fee [Server-side]

In addition to passing recurring prices, you can add one-time prices in `subscription` mode. These are only on the initial _invoice_ (Invoices are statements of amounts owed by a customer. They track the status of payments from draft through paid or otherwise finalized. Subscriptions automatically generate invoices, or you can manually create a one-off invoice) created by the subscription. This is useful for adding setup fees or other one-time fees associated with a subscription.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  payment_method_types: ["bacs_debit"],

  // or you can take multiple payment methods with
  // payment_method_types: ['card', 'bacs_debit', ...]
  line_items: [
    {
      price: "{{RECURRING_PRICE_ID}}",
      quantity: 1,
    },
    {
      price: "{{ONE_TIME_PRICE_ID}}",
      quantity: 1,
    },
  ],
  mode: "subscription",
  success_url: "https://example.com/success?session_id={CHECKOUT_SESSION_ID}",
});
```

## Optional: Create prices and products inline [Server-side]

In addition to passing in existing price IDs, you can also define your item price at Checkout session creation. First define a [Product](https://docs.stripe.com/api/products.md). Then create a Checkout session using the product ID, by passing it into [price_data](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items-price_data) with the `unit_amount`, `currency`, and `recurring` details:

#### Node.js

```javascript

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({payment_method_types: ['bacs_debit'],

  // or you can take multiple payment methods with
  // payment_method_types: ['card', 'bacs_debit', ...]line_items: [{
    price_data: {
      unit_amount: 5000,
      currency: 'gbp',
      product: '{{PRODUCT_ID}}',
      recurring: {
        interval: 'month'
      },
    },
    quantity: 1
  }],
  mode: 'subscription',
  success_url: 'https://example.com/success?session_id={CHECKOUT_SESSION_ID}'
});
```

If you also need to create products inline, you can do so with [product_data](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items-price_data-product_data):

#### Node.js

```javascript

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({payment_method_types: ['bacs_debit'],

  // or you can take multiple payment methods with
  // payment_method_types: ['card', 'bacs_debit', ...]line_items: [{
    price_data: {
      currency: 'gbp',
      product_data: {
        name: 'T-shirt'
      },
      unit_amount: 2000
    },
    quantity: 1
  }],
  mode: 'subscription',
  success_url: 'https://example.com/success?session_id={CHECKOUT_SESSION_ID}'
});
```

## Optional: Existing customers [Server-side]

#### Accounts v2

If you’ve previously created a customer-configured `Account` object to represent a customer, use the [customer_account](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer_account) argument to pass their `Account` ID when creating a Checkout Session. This ensures that all objects created during the Session are associated with the correct `Account` object.

When you pass an `Account` ID, Stripe also uses the email stored on the `Account` object to prefill the email field on the Checkout page. If the customer changes their email on the Checkout page, it updates on the `Account` object after a successful payment.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  customer_account: "{{CUSTOMER_ACCOUNT_ID}}",
  payment_method_types: ["bacs_debit"],

  // or you can take multiple payment methods with
  // payment_method_types: ['card', 'bacs_debit', ...]
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  mode: "subscription",
  success_url: "https://example.com/success",
});
```

#### Customers v1

If you’ve previously created a _`Customer`_ (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) object to represent a customer, use the [customer](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer) argument to pass their `Customer` ID when creating a Checkout Session. This ensures that all objects created during the Session are associated with the correct `Customer` object.

When you pass a `Customer` ID, Stripe also uses the email stored on the `Customer` object to prefill the email field on the Checkout page. If the customer changes their email on the Checkout page, it will be updated on the `Customer` object after a successful payment.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  customer: "{{CUSTOMER_ID}}",
  payment_method_types: ["bacs_debit"],

  // or you can take multiple payment methods with
  // payment_method_types: ['card', 'bacs_debit', ...]
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  mode: "subscription",
  success_url: "https://example.com/success",
});
```

## Optional: Prefill customer data [Server-side]

If you’ve already collected your customer’s email and want to prefill it in the Checkout Session for them, pass [customer_email](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer_email) when creating a Checkout Session.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  customer_email: "customer@example.com",
  payment_method_types: ["bacs_debit"],

  // or you can take multiple payment methods with
  // payment_method_types: ['card', 'bacs_debit', ...]
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  mode: "subscription",
  success_url: "https://example.com/success",
});
```

## Optional: Handling trials [Server-side]

You can use [trial_end](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-subscription_data-trial_end) or [trial_period_days](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-subscription_data-trial_period_days) on the Checkout session to specify the duration of the trial period. In this example we use `trial_period_days` to create a Checkout session for a subscription with a 30 days trial.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  payment_method_types: ["bacs_debit"],

  // or you can take multiple payment methods with
  // payment_method_types: ['card', 'bacs_debit', ...]
  subscription_data: { trial_period_days: 30 },
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  mode: "subscription",
  success_url: "https://example.com/success?session_id={CHECKOUT_SESSION_ID}",
});
```

Checkout displays the following information automatically for subscriptions with trials:

- Trial period
- Frequency and amount of charges after trial expiration

For more information on compliance requirements, see the [Manage compliance requirements](https://docs.stripe.com/billing/subscriptions/trials/manage-trial-compliance.md) or [support](https://support.stripe.com/questions/2020-visa-trial-subscription-requirement-changes-guide) guides.

## Optional: Tax rates [Server-side]

You can specify [tax rates](https://docs.stripe.com/tax/tax-rates.md) (Sales, VAT, GST, and others) in Checkout Sessions to apply taxes to _subscriptions_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis).

- Use fixed tax rates when you know the exact tax rate to charge your customers before they start the checkout process (for example, you only sell to customers in the UK and always charge 20% VAT).
- With the _Prices_ (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) API, you can use dynamic tax rates when you require more information from your customer (for example, their billing or shipping address) before determining the tax rate to charge. With dynamic tax rates, you create tax rates for different regions (for example, a 20% VAT tax rate for customers in the UK and a 7.25% sales tax rate for customers in California, US) and Stripe attempts to match your customer’s location to one of those tax rates.

#### Fixed tax rates

Set [subscription_data.default_tax_rates](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-subscription_data-default_tax_rates) to apply a default tax rate to a subscription started with Checkout.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  payment_method_types: ["bacs_debit"],

  // or you can take multiple payment methods with
  // payment_method_types: ['card', 'bacs_debit', ...]
  subscription_data: { default_tax_rates: ["{{TAX_RATE_ID}}"] },
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  mode: "subscription",
  success_url: "https://example.com/success",
});
```

You can also specify [line_items.tax_rates](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items-tax_rates) or [subscription_data.items.tax_rates](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-subscription_data-items-tax_rates) to apply tax rates to specific plans or invoice line items.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  payment_method_types: ["bacs_debit"],

  // or you can take multiple payment methods with
  // payment_method_types: ['card', 'bacs_debit', ...]
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
      tax_rates: ["{{TAX_RATE_ID}}"],
    },
  ],
  mode: "subscription",
  success_url: "https://example.com/success",
});
```

#### Dynamic tax rates

Pass an array of [tax rates](https://docs.stripe.com/api/tax_rates/object.md) to [line_items.dynamic_tax_rates](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items-dynamic_tax_rates). Each tax rate must have a [supported](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items-dynamic_tax_rates) `country`, and for the US, a `state`.

This list matches tax rates to your customer’s [shipping address](https://docs.stripe.com/payments/collect-addresses.md), billing address, or country. The shipping address takes precedence over the billing address for determining the tax rate to charge.

If you’re not collecting shipping or billing addresses, your customer’s country (and postal code where applicable) is used to determine the tax rate. If you haven’t passed a tax rate that matches your customer’s shipping address, billing address, or country, no tax rate is applied.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  payment_method_types: ["bacs_debit"],
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
      dynamic_tax_rates: [
        "{{FIRST_TAX_RATE_ID}}",
        "{{SECOND_TAX_RATE_ID}}",
        // additional tax rates
      ],
    },
  ],
  mode: "subscription",
  success_url: "https://example.com/success",
});
```

> [subscription_data.default_tax_rates](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-subscription_data-default_tax_rates) and [line_items.tax_rates](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items-tax_rates) can’t be used in combination with [line_items.dynamic_tax_rates](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items-dynamic_tax_rates).

You can use Stripe’s data exports to populate the periodic reports required for remittance. Visit [Tax reporting and remittance](https://docs.stripe.com/tax/tax-rates.md#remittance) for more information.

## Optional: Adding coupons [Server-side]

You can apply [coupons](https://docs.stripe.com/billing/subscriptions/coupons.md) to subscriptions in a Checkout Session by setting [discounts](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-discounts). This coupon overrides any coupon on the customer. If you’re creating a subscription with an [existing customer](https://docs.stripe.com/billing/subscriptions/bacs-debit.md#handling-existing-customers), any coupon associated with the customer is applied to the subscription’s _invoices_ (Invoices are statements of amounts owed by a customer. They track the status of payments from draft through paid or otherwise finalized. Subscriptions automatically generate invoices, or you can manually create a one-off invoice).

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  payment_method_types: ["bacs_debit"],

  // or you can take multiple payment methods with
  // payment_method_types: ['card', 'bacs_debit', ...]
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  discounts: [{ coupon: "{{COUPON_ID}}" }],
  mode: "subscription",
  success_url: "https://example.com/success",
});
```

### Adding customer-facing promotion codes

You can also enable user-redeemable [Promotion Codes](https://docs.stripe.com/billing/subscriptions/coupons.md#promotion-codes) using the [allow_promotion_codes](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-allow_promotion_codes) parameter in Checkout Sessions. When `allow_promotion_codes` is enabled on a Checkout Session, Checkout includes a promotion code redemption box for your customers to use. Create your [coupons](https://docs.stripe.com/billing/subscriptions/coupons.md) and promotion codes through the Dashboard or API in order for your customers to redeem them in Checkout.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  payment_method_types: ["bacs_debit"],

  // or you can take multiple payment methods with
  // payment_method_types: ['card', 'bacs_debit', ...]
  line_items: [
    {
      price_data: {
        currency: "gbp",
        unit_amount: 2000,
        product: "{{PRODUCT_ID}}",
        recurring: {
          interval: "month",
        },
      },
      quantity: 1,
    },
  ],
  allow_promotion_codes: true,
  mode: "subscription",
  success_url: "https://example.com/success",
});
```

## See also

- [Customize your integration](https://docs.stripe.com/payments/checkout/customization.md)
- [Manage subscriptions with the customer portal](https://docs.stripe.com/billing/subscriptions/build-subscriptions.md?payment-ui=checkout&ui=stripe-hosted)
