<!-- Source URL: https://docs.stripe.com/billing/subscriptions/ideal -->
<!-- Fetched: 2026-05-13 -->

# Set up a subscription with iDEAL and SEPA Direct Debit

Learn how to create and charge a subscription with iDEAL and SEPA Direct Debit.

# Full hosted page

> This is a Full hosted page for when payments-ui-type is stripe-hosted. View the full page at https://docs.stripe.com/billing/subscriptions/ideal?payments-ui-type=stripe-hosted.

iDEAL is a [single use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method that requires customers to [authenticate](https://docs.stripe.com/payments/payment-methods.md#customer-actions) each payment. After your customer authenticates the payment, Stripe saves your customer’s [IBAN](https://en.wikipedia.org/wiki/International_Bank_Account_Number) in a [SEPA Direct Debit](https://docs.stripe.com/payments/sepa-debit.md) payment method. You can then use the SEPA Direct Debit payment method to [accept future payments](https://docs.stripe.com/payments/sepa-debit/accept-a-payment.md).

See the [sample on GitHub](https://github.com/stripe-samples/checkout-single-subscription) or try the [demo](https://checkout.stripe.dev/checkout).

Use this guide to set up a _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) using iDEAL and _Checkout_ (A low-code payment integration that creates a customizable form for collecting payments. You can embed Checkout directly in your website, redirect customers to a Stripe-hosted payment page, or create a customized checkout page with Stripe Elements).

With this integration, Stripe charges the first Subscription payment through iDEAL to collect your customer’s bank details. If you’re offering a free trial, Stripe charges your customer 0.01 EUR through iDEAL to collect their bank details and immediately refunds it.

A [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md) represents the details of your customer’s intent to purchase. You create a Checkout Session when your customer wants to start a subscription. After redirecting your customer to a Checkout Session, Stripe presents a payment form where your customer can complete their purchase. After your customer completes a purchase, they’re redirected back to your site.

## Set up Stripe [Server-side]

Install the Stripe client of your choice:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

Install the Stripe CLI (optional). The CLI provides [webhook testing](https://docs.stripe.com/webhooks.md#test-webhook), and you can run it to create your products and prices.

From the command-line, use an install script or download and extract a versioned archive file for your operating system to install the CLI.

#### homebrew

To install the Stripe CLI with [homebrew](https://brew.sh/), run:

```bash
brew install stripe/stripe-cli/stripe
```

This command fails if you run it on the Linux version of homebrew, but you can use this alternative or follow the instructions on the Linux tab.

```bash
brew install stripe-cli
```

#### apt

> The Debian build for the CLI is available on JFrog at https://packages.stripe.dev, which isn’t a domain owned by Stripe. When you visit this URL, it redirects you to the Jfrog artifactory list.

To install the Stripe CLI on Debian and Ubuntu-based distributions:

1. Add Stripe CLI’s GPG key to the apt sources keyring:

```bash
curl -s https://packages.stripe.dev/api/security/keypair/stripe-cli-gpg/public | gpg --dearmor | sudo tee /usr/share/keyrings/stripe.gpg > /dev/null
```

1. Add CLI’s apt repository to the apt sources list:

```bash
echo "deb [signed-by=/usr/share/keyrings/stripe.gpg] https://packages.stripe.dev/stripe-cli-debian-local stable main" | sudo tee -a /etc/apt/sources.list.d/stripe.list
```

1. Update the package list:

```bash
sudo apt update
```

1. Install the CLI:

```bash
sudo apt install stripe
```

#### yum

> The RPM build for the CLI is available on JFrog at https://packages.stripe.dev, which isn’t a domain owned by Stripe. When you visit this URL, it redirects you to the Jfrog artifactory list.

To install the Stripe CLI on RPM-based distributions:

1. Add CLI’s yum repository to the yum sources list:

```bash
echo -e "[Stripe]\nname=stripe\nbaseurl=https://packages.stripe.dev/stripe-cli-rpm-local/\nenabled=1\ngpgcheck=0" >> /etc/yum.repos.d/stripe.repo
```

1. Install the CLI:

```bash
sudo yum install stripe
```

#### Scoop

To install the Stripe CLI with [Scoop](https://scoop.sh/), run:

```bash
scoop bucket add stripe https://github.com/stripe/scoop-stripe-cli.git
```

```bash
scoop install stripe
```

#### macOS

To install the Stripe CLI on macOS without homebrew:

1. Download the latest `mac-os` tar.gz file of your cpu architecture type from [GitHub](https://github.com/stripe/stripe-cli/releases/latest).
1. Unzip the file: `tar -xvf stripe_[X.X.X]_mac-os_[ARCH_TYPE].tar.gz`.

Optionally, install the binary in a location where you can execute it globally (for example, `/usr/local/bin`).

#### Linux

To install the Stripe CLI on Linux without a package manager:

1. Download the latest `linux` tar.gz file from [GitHub](https://github.com/stripe/stripe-cli/releases/latest).
1. Unzip the file: `tar -xvf stripe_X.X.X_linux_x86_64.tar.gz`.
1. Move `./stripe` to your execution path.

#### Windows

To install the Stripe CLI on Windows without Scoop:

1. Download the latest `windows` zip file from [GitHub](https://github.com/stripe/stripe-cli/releases/latest).
1. Unzip the `stripe_X.X.X_windows_x86_64.zip` file.
1. Add the path to the unzipped `stripe.exe` file to your `Path` environment variable. To learn how to update environment variables, see the [Microsoft PowerShell documentation](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables?view=powershell-7.3#saving-changes-to-environment-variables).

> Windows anti-virus scanners occasionally flag the Stripe CLI as unsafe. This is likely a false positive. For more information, see [issue #692](https://github.com/stripe/stripe-cli/issues/692) in the GitHub repository.

1. Run the unzipped `.exe` file.

#### Docker

The Stripe CLI is also available as a [Docker image](https://hub.docker.com/r/stripe/stripe-cli). To install the latest version, run:

```bash
docker run --rm -it stripe/stripe-cli:latest
```

To run the Stripe CLI, you must also pair it with your Stripe account. Run `stripe login` and follow the prompts. For more information, see the [Stripe CLI documentation page](https://docs.stripe.com/stripe-cli.md).

## Create the pricing model [Dashboard] [Stripe CLI]

[Recurring pricing models](https://docs.stripe.com/products-prices/pricing-models.md) represent the products or services you sell, how much they cost, what currency you accept for payments, and the service period for subscriptions. To build the pricing model, create [products](https://docs.stripe.com/api/products.md) (what you sell) and [prices](https://docs.stripe.com/api/prices.md) (how much and how often to charge for your products).

This example uses flat-rate pricing with two different service-level options: Basic and Premium. For each service-level option, you need to create a product and a recurring price. To add a one-time charge for something like a setup fee, create a third product with a one-time price.

Each product bills at monthly intervals. The price for the Basic product is 5 EUR. The price for the Premium product is 15 EUR. See the [flat rate pricing](https://docs.stripe.com/subscriptions/pricing-models/flat-rate-pricing.md) guide for an example with three tiers.

#### Dashboard

Go to the [Add a product](https://dashboard.stripe.com/test/products/create) page and create two products. Add one price for each product, each with a monthly recurring billing period:

- Premium product: Premium service with extra features
  - Price: Flat rate | 15 EUR

- Basic product: Basic service with minimum features
  - Price: Flat rate | 5 EUR

After you create the prices, record the price IDs so you can use them in other steps. Price IDs look like this: `price_G0FvDp6vZvdwRZ`.

When you’re ready, use the **Copy to live mode** button at the top right of the page to clone your product from [a sandbox to live mode](https://docs.stripe.com/keys.md#test-live-modes).

#### API

You can use the API to create the [Products](https://docs.stripe.com/api/products.md) and [Prices](https://docs.stripe.com/api/prices.md).

Create the Premium product:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const product = await stripe.products.create({
  name: "Billing Guide: Premium Service",
  description: "Premium service with extra features",
});
```

Create the Basic product:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const product = await stripe.products.create({
  name: "Billing Guide: Basic Service",
  description: "Basic service with minimum features",
});
```

Record the product ID for each product. They look like this:

```json
{
  "id": "prod_H94k5odtwJXMtQ",
  "object": "product",
  "active": true,
  "attributes": [],
  "created": 1587577341,
  "description": "Premium service with extra features",
  "images": [],
  "livemode": false,
  "metadata": {},
  "name": "Billing Guide: Premium Service",
  "statement_descriptor": null,
  "type": "service",
  "unit_label": null,
  "updated": 1587577341
}
```

Use the product IDs to create a price for each product. The [unit_amount](https://docs.stripe.com/api/prices/object.md#price_object-unit_amount) number is in cents, so `1500` = 15 EUR, for example.

Create the Premium price:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const price = await stripe.prices.create({
  product: "{{PREMIUM_PRODUCT_ID}}",
  unit_amount: 1500,
  currency: "usd",
  recurring: {
    interval: "month",
  },
});
```

Create the Basic price:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const price = await stripe.prices.create({
  product: "{{BASIC_PRODUCT_ID}}",
  unit_amount: 500,
  currency: "usd",
  recurring: {
    interval: "month",
  },
});
```

Record the price ID for each price so you can use them in subsequent steps. They look like this:

```json
{
  "id": "price_HGd7M3DV3IMXkC",
  "object": "price",
  "product": "prod_HGd6W1VUqqXGvr",
  "type": "recurring",
  "currency": "eur",
  "recurring": {
    "interval": "month",
    "interval_count": 1,
    "trial_period_days": null,
    "usage_type": "licensed"
  },
  "active": true,
  "billing_scheme": "per_unit",
  "created": 1589319695,
  "livemode": false,
  "lookup_key": null,
  "metadata": {},
  "nickname": null,
  "unit_amount": 1500,
  "unit_amount_decimal": "1500",
  "tiers": null,
  "tiers_mode": null,
  "transform_quantity": null
}
```

For other pricing models, see [Billing examples](https://docs.stripe.com/products-prices/pricing-models.md).

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

See [Create a Session](https://docs.stripe.com/api/checkout/sessions/create.md) for a complete list of parameters that you can use.

Create a Session with the ID of an existing _Price_ (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions). Make sure that the mode is set to `subscription` and that you pass at least one recurring price. You can add one-time prices in addition to recurring prices. After creating the Checkout Session, redirect your customer to the [URL](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-url) returned in the response.

When creating a Session, you can specify `payment_method_types` or have Stripe automatically pick payment methods based on your [Dashboard](https://dashboard.stripe.com/settings/payment_methods) settings. If you don’t specify `payment_method_types`, you must turn on iDEAL recurring payments in the [Dashboard](https://dashboard.stripe.com/settings/payment_methods). This enables SEPA Direct Debit for recurring iDEAL payments only, but doesn’t turn on SEPA Direct Debit payments as a stand alone payment method.

#### Listing payment methods manually

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  payment_method_types: ["ideal"],

  // or you can take multiple payment methods with
  // payment_method_types: ['card', 'ideal', ...]
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

#### Manage payment methods from the Dashboard

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

When your customer successfully completes their payment, they’re redirected to the `success_url`, a page on your website that informs the customer that their payment was successful. Make the Session ID available on your success page by including the `{CHECKOUT_SESSION_ID}` template variable in the `success_url` as in the above example.

When your customer clicks on your logo in a Checkout Session without completing a payment, Checkout redirects them back to your website that the customer viewed prior to redirecting to Checkout.

Checkout Sessions expire 24 hours after creation by default.

> Don’t rely on the redirect to the `success_url` alone for detecting payment initiation, because:
>
> - Malicious users could directly access the `success_url` without paying and gain access to your goods or services.

- After a successful payment, customers might close their browser tab before they’re redirected to the `success_url`.

## Confirm the payment is successful

When your customer completes a payment, they’re redirected to the URL that you specified as the `success_url`. This is typically a page on your website that informs your customer that their payment was successful.

Use the Dashboard, a custom _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a third-party plugin to handle post-payment events like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

#### Dashboard

Successful payments appear in the Dashboard’s [list of payments](https://dashboard.stripe.com/payments). When you click a payment, it takes you to the Payment details page. The **Checkout summary** section contains billing information and the list of items purchased, which you can use to manually fulfill the order.
![Checkout summary](assets/stripe-ach-checkout-success.png)

When a customer successfully pays for a recurring service, they’re automatically subscribed. Their subscription is recorded as a new entry in the Dashboard’s [list of subscriptions](https://dashboard.stripe.com/subscriptions).

> Stripe can help you keep up with incoming payments by sending you email notifications whenever a customer successfully completes one. Use the Dashboard to [configure email notifications](https://dashboard.stripe.com/settings/user).

#### Webhooks

[Set up webhooks](https://docs.stripe.com/webhooks.md) to programmatically handle post-payment events. The quickest way to develop and test webhooks locally is with the [Stripe CLI](https://docs.stripe.com/stripe-cli.md). Once you have it installed, you can forward events to your server:

```bash
stripe listen --forward-to localhost:4242/webhook
Ready! Your webhook signing secret is '{{WEBHOOK_SIGNING_SECRET}}' (^C to quit)
```

With a webhook endpoint, your customer is redirected to the `success_url` when you [acknowledged you received the event](https://docs.stripe.com/webhooks.md#acknowledge-events-immediately). In scenarios where your endpoint is down or the event isn’t acknowledged properly, your customer is redirected to the `success_url` 10 seconds after a successful payment.

The following example endpoint demonstrates how to acknowledge and handle events.

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

    // Handle the checkout.session.completed event
    if (event.type === "checkout.session.completed") {
      const session = event.data.object;

      // Fulfill the purchase...
      handleCheckoutSession(session);
    }

    // Return a response to acknowledge receipt of the event
    response.json({ received: true });
  },
);

app.listen(8000, () => console.log("Running on port 8000"));
```

You can use plugins like [Zapier](https://stripe.com/works-with/zapier) to automate updating your purchase fulfillment systems with information from Stripe payments.

Some examples of automation supported by plugins include:

- Updating spreadsheets used for order tracking in response to successful payments
- Updating inventory management systems in response to successful payments
- Triggering notifications to internal customer service teams using email or chat applications

## Test the integration

Using your [test API keys](https://docs.stripe.com/keys.md#test-live-modes), select any bank from the list. After confirming, you’re redirected to a test page with options to authorize or fail the payment.

- Click **Authorize test payment** to test the case when the setup is successful.
- Click **Fail test payment** to test the case when the customer fails to authenticate.

## Optional: Create a trial for your subscription

Free trials allow customers access to your product for a period of time without charging them. Add a trial to your subscription by setting the `subscription_data.trial_period_days` or `subscription_data.trial_end` parameters when [creating the Checkout Session](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-subscription_data). Your customer’s first charge occurs after the trial ends. For example, to add a 7-day free trial to the start of your subscription set `subscription_data.trial_period_days` to `7`.

#### Listing payment methods manually

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  payment_method_types: ["ideal"],

  // or you can take multiple payment methods with
  // payment_method_types: ['card', 'ideal', ...]
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  mode: "subscription",
  success_url: "https://example.com/success?session_id={CHECKOUT_SESSION_ID}",
  subscription_data: { trial_period_days: "7" },
});

// Record the session ID in your system
const session_id = session.id;

// 303 redirect to session.url
```

#### Manage payment methods from the Dashboard

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
  subscription_data: { trial_period_days: "7" },
});

// Record the session ID in your system
const session_id = session.id;

// 303 redirect to session.url
```

## See also

- [Customize your integration](https://docs.stripe.com/payments/checkout/customization.md)
- [Manage subscriptions with the customer portal](https://docs.stripe.com/billing/subscriptions/build-subscriptions.md?payment-ui=checkout&ui=stripe-hosted)

# Direct API

> This is a Direct API for when payments-ui-type is direct-api. View the full page at https://docs.stripe.com/billing/subscriptions/ideal?payments-ui-type=direct-api.

Use this guide to set up a _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) using [iDEAL](https://docs.stripe.com/payments/ideal.md) as a payment method.

iDEAL is a [single-use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method that requires customers to [authenticate](https://docs.stripe.com/payments/payment-methods.md#customer-actions) each payment. With this integration, Stripe charges your customer 0.01 EUR through iDEAL to collect their bank details. After your customer authenticates the payment, Stripe refunds the payment and stores your customer’s [IBAN](https://en.wikipedia.org/wiki/International_Bank_Account_Number) in a [SEPA Direct Debit](https://docs.stripe.com/payments/sepa-debit.md) payment method. You can then use the SEPA Direct Debit [PaymentMethod](https://docs.stripe.com/api/payment_methods.md) to charge for the subscription.

> To use iDEAL to set up SEPA Direct Debit payments, you must activate SEPA Direct Debit in the [Dashboard](https://dashboard.stripe.com/account/payments/settings). You must also comply with the [iDEAL Terms of Service](https://stripe.com/ideal/legal) and [SEPA Direct Debit Terms of Service](https://stripe.com/sepa-direct-debit/legal).

## Create a product and price [Dashboard]

[Products](https://docs.stripe.com/api/products.md) represent the item or service you’re selling. [Prices](https://docs.stripe.com/api/prices.md) define how much and how frequently you charge for a product. This includes how much the product costs, what currency you accept, and whether it’s a one-time or recurring charge. If you only have a few products and prices, create and manage them in the Dashboard.

This guide uses a stock photo service as an example and charges customers a 15 EUR monthly subscription. To model this:

1. Go to the [Products](https://dashboard.stripe.com/products?active=true) page and click **Create product**.
1. Enter a **Name** for the product. You can optionally add a **Description** and upload an image of the product.
1. Select a **Product tax code**. Learn more about [product tax codes](https://docs.stripe.com/tax/tax-codes.md).
1. Select **Recurring**. Then enter **15** for the price and select **EUR** as the currency.
1. Choose whether to **Include tax in price**. You can either use the default value from your [tax settings](https://dashboard.stripe.com/test/settings/tax) or set the value manually. In this example, select **Auto**.
1. Select **Monthly** for the **Billing period**.
1. Click **More pricing options**. Then select **Flat rate** as the pricing model for this example. Learn more about [flat rate](https://docs.stripe.com/products-prices/pricing-models.md#flat-rate) and other [pricing models](https://docs.stripe.com/products-prices/pricing-models.md).
1. Add an internal **Price description** and [Lookup key](https://docs.stripe.com/products-prices/manage-prices.md#lookup-keys) to organize, query, and update specific prices in the future.
1. Click **Next**. Then click **Add product**.

After you create the product and the price, record the price ID so you can use it in subsequent steps. The pricing page displays the ID and it looks similar to this: `price_G0FvDp6vZvdwRZ`.

## Create or retrieve a Customer before setup [Server-side]

To reuse an iDEAL-initiated SEPA Direct Debit payment method for future payments, attach it to a _Customer_ (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments).

Create a Customer object when a customer creates an account on your business. Associate the Customer object ID with your internal representation of a customer to retrieve and use the stored payment method details later. If the customer hasn’t created an account, you can still create a Customer object now and associate it with your internal representation of the customer’s account later.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create();
```

## Create a SetupIntent [Server-side]

Create a `SetupIntent` with the customer’s ID and add `ideal` to the [payment_method_types](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-payment_method_types) array. The `SetupIntent` tracks the steps of the setup process. For iDEAL | Wero, this includes collecting a [SEPA Direct Debit mandate](https://www.europeanpaymentscouncil.eu/what-we-do/sepa-direct-debit/sdd-mandate) from the customer and tracking its validity.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ["ideal"],
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ["ideal"],
  customer: "{{CUSTOMER_ID}}",
});
```

## Collect payment details and confirm [Client-side]

Use the [Payment Element](https://docs.stripe.com/payments/payment-element.md) to collect payment method details and confirm the SetupIntent. The Payment Element handles the customer redirect to iDEAL for authentication.

Collect payment details on the client with the [Payment Element](https://docs.stripe.com/payments/payment-element.md). The Payment Element is a prebuilt UI component that simplifies collecting payment details for a variety of payment methods.

The Payment Element contains an iframe that securely sends payment information to Stripe over an HTTPS connection. Avoid placing the Payment Element within another iframe because some payment methods require redirecting to another page for payment confirmation.

If you choose to use an iframe and want to accept Apple Pay or Google Pay, the iframe must have the [allow](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe#attr-allowpaymentrequest) attribute set to equal `"payment *"`.

The checkout page address must start with `https://` rather than `http://` for your integration to work. You can test your integration without using HTTPS, but remember to [enable it](https://docs.stripe.com/security/guide.md#tls) when you’re ready to accept live payments.

#### HTML + JS

### Set up Stripe.js

The Payment Element is automatically available as a feature of Stripe.js. Include the Stripe.js script on your checkout page by adding it to the `head` of your HTML file. Always load Stripe.js directly from js.stripe.com to remain PCI compliant. Don’t include the script in a bundle or host a copy of it yourself.

```html
<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/dahlia/stripe.js"></script>
</head>
```

Create an instance of Stripe with the following JavaScript on your checkout page:

```javascript
// Set your publishable key: remember to change this to your live publishable key in production
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");
```

### Add the Payment Element to your payment page

The Payment Element needs a place to live on your payment page. Create an empty DOM node (container) with a unique ID in your payment form:

```html
<form id="payment-form">
  <div id="payment-element">
    <!-- Elements will create form elements here -->
  </div>
  <button id="submit">Submit</button>
  <div id="error-message">
    <!-- Display error message to your customers here -->
  </div>
</form>
```

When the previous form loads, create an instance of the Payment Element and mount it to the container DOM node. Pass the [client secret](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-client_secret) from the previous step into `options` when you create the [Elements](https://docs.stripe.com/js/elements_object/create) instance:

```javascript
const options = {
  clientSecret: "{{CLIENT_SECRET}}",
  // Fully customizable with appearance API.
  appearance: {
    /*...*/
  },
};

// Set up Stripe.js and Elements to use in checkout form, passing the client secret obtained in a previous stepconst elements = stripe.elements(options);
// Optional: Autofill user's saved payment methods. If the customer's
// email is known when the page is loaded, you can pass the email
// to the linkAuthenticationElement on mount:
//
//   linkAuthenticationElement.mount("#link-authentication-element",  {
//     defaultValues: {
//       email: 'jenny.rosen@example.com',
//     }
//   })

// Create and mount the Payment Element
const paymentElementOptions = { layout: "accordion" };
const paymentElement = elements.create("payment", paymentElementOptions);
paymentElement.mount("#payment-element");
```

#### React

### Set up Stripe.js

Install [React Stripe.js](https://www.npmjs.com/package/@stripe/react-stripe-js) and the [Stripe.js loader](https://www.npmjs.com/package/@stripe/stripe-js) from the npm public registry:

```bash
npm install --save @stripe/react-stripe-js @stripe/stripe-js
```

### Add and configure the Elements provider to your payment page

To use the Payment Element component, wrap your checkout page component in an [Elements provider](https://docs.stripe.com/sdks/stripejs-react.md#elements-provider). Call `loadStripe` with your publishable key, and pass the returned `Promise` to the `Elements` provider. Also pass the [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) from the previous step as `options` to the `Elements` provider.

```jsx
import React from "react";
import ReactDOM from "react-dom";
import { Elements } from "@stripe/react-stripe-js";
import { loadStripe } from "@stripe/stripe-js";

import SetupForm from "./SetupForm";

// Make sure to call `loadStripe` outside of a component’s render to avoid
// recreating the `Stripe` object on every render.
const stripePromise = loadStripe("<<YOUR_PUBLISHABLE_KEY>>");

function App() {
  const options = {
    // passing the client secret obtained in step 3
    clientSecret: "{{CLIENT_SECRET}}",
    // Fully customizable with appearance API.
    appearance: {
      /*...*/
    },
  };

  return (
    <Elements stripe={stripePromise} options={options}>
      <SetupForm />
    </Elements>
  );
}

ReactDOM.render(<App />, document.getElementById("root"));
```

### Add the Payment Element component

Use the `PaymentElement` component to build your form:

```jsx
import React from "react";
import { PaymentElement } from "@stripe/react-stripe-js";

const SetupForm = () => {
  return (
    <form>
      <PaymentElement />
      <button>Submit</button>
    </form>
  );
};

export default SetupForm;
```

Send the SetupIntent object’s [client secret](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-client_secret) to the client, instead of the entire SetupIntent object. This differs from your API keys that authenticate Stripe API requests. Handle the client secret carefully because it can complete the setup. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

Use [stripe.confirmSetup](https://docs.stripe.com/js/payment_intents/confirm_setup) to complete the SetupIntent using details from the Payment Element. Provide a [return_url](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-return_url) to this function to indicate where Stripe redirects the user after they complete the SetupIntent. Your user is first redirected to their bank for authorization, then redirected to the `return_url`.

#### HTML + JS

```javascript
const form = document.getElementById("payment-form");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const { error } = await stripe.confirmSetup({
    elements,
    confirmParams: {
      return_url: "https://example.com/order/123/complete",
    },
  });

  if (error) {
    const messageContainer = document.querySelector("#error-message");
    messageContainer.textContent = error.message;
  } else {
    // Your customer is redirected to your `return_url`.
  }
});
```

#### React

```jsx
import React, { useState } from "react";
import {
  useStripe,
  useElements,
  PaymentElement,
} from "@stripe/react-stripe-js";

const CheckoutForm = () => {
  const stripe = useStripe();
  const elements = useElements();
  const [errorMessage, setErrorMessage] = useState(null);

  const handleSubmit = async (event) => {
    event.preventDefault();

    if (!stripe || !elements) {
      return;
    }

    const { error } = await stripe.confirmSetup({
      elements,
      confirmParams: {
        return_url: "https://example.com/order/123/complete",
      },
    });

    if (error) {
      setErrorMessage(error.message);
    } else {
      // Your customer is redirected to your `return_url`.
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <PaymentElement />
      <button disabled={!stripe}>Submit</button>
      {errorMessage && <div>{errorMessage}</div>}
    </form>
  );
};

export default CheckoutForm;
```

## Optional: Monitor webhooks [Server-side]

Use a method such as webhooks to confirm the setup was authorized successfully by your customer, instead of relying on your customer to return to the payment status page. When a customer successfully authorizes the setup, the SetupIntent emits the `setup_intent.succeeded` webhook event. If a customer doesn’t successfully authorize the setup, the SetupIntent emits the `setup_intent.setup_failed` webhook event and returns to a status of `requires_payment_method`.

## Create the subscription [Server-side]

After the SetupIntent succeeds, retrieve the generated SEPA Direct Debit payment method. Find the ID of the SEPA Direct Debit payment method by [retrieving](https://docs.stripe.com/api/setup_intents/retrieve.md) the SetupIntent and [expanding](https://docs.stripe.com/api/expanding_objects.md) the `latest_attempt` field, where you’ll find the `generated_sepa_debit` ID inside of `payment_method_details`:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.retrieve("{{SETUP_INTENT_ID}}", {
  expand: ["latest_attempt"],
});
```

Use the `generated_sepa_debit` payment method ID from `latest_attempt.payment_method_details.generated_sepa_debit` to create a [subscription](https://docs.stripe.com/api/subscriptions.md) with the customer and the SEPA Direct Debit payment method ID:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer: "cus_Gk0uVzT2M4xOKD",
  default_payment_method: "pm_1F0c9v2eZvKYlo2CJDeTrB4n",
  items: [
    {
      price: "price_F52b2UdntfQsfR",
    },
  ],
  expand: ["latest_invoice.payment_intent"],
  off_session: true,
});
```

Creating subscriptions automatically charges customers because the [default payment method](https://docs.stripe.com/api/customers/create.md#create_customer-invoice_settings-default_payment_method) is set. After a successful payment, the status in the [Stripe Dashboard](https://dashboard.stripe.com/test/subscriptions) changes to **Active**. The price you created earlier determines subsequent billings.

## Manage the subscription status [Client-side]

When the initial payment succeeds, the status of the subscription is `active` and no further action is needed. When payments fail, the status changes to the **Subscription status** configured in your [automatic collection settings](https://docs.stripe.com/invoicing/automatic-collection.md). Notify the customer after a failure and [charge them using a different payment method](https://docs.stripe.com/billing/subscriptions/overview.md#requires-payment-method).

## Update a subscription [Server-side]

When you update a subscription, you must specify `off_session=true`. Otherwise, any new payment requires a user confirmation. For example, use the following to change the quantity of an item included in the subscription:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer: "cus_Gk0uVzT2M4xOKD",
  default_payment_method: "pm_1F0c9v2eZvKYlo2CJDeTrB4n",
  items: [
    {
      price: "price_F52b2UdntfQsfR",
      quantity: 2,
    },
  ],
  off_session: true,
});
```

## Test the integration

Using your [test API keys](https://docs.stripe.com/keys.md#test-live-modes) to confirm the SetupIntent. After confirming, you’re redirected to a test page with options to authorize or fail the payment method setup.

- Click **Authorize test payment** to test the case when the setup is successful. The SetupIntent transitions from `requires_action` to `succeeded`.
- Click **Fail test payment** to test the case when the customer fails to authenticate. The SetupIntent transitions from `requires_action` to `requires_payment_method`.

### Test your SEPA Direct Debit integration

#### Email

Set `payment_method.billing_details.email` to one of the following values to test the `PaymentIntent` status transitions. You can include your own custom text at the beginning of the email address followed by an underscore. For example, `test_1_generatedSepaDebitIntentsFail@example.com` results in a SEPA Direct Debit PaymentMethod that always fails when used with a `PaymentIntent`.

| Email Address                                                      | Description                                                                                                                       |
| ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| `generatedSepaDebitIntentsSucceed@example.com`                     | The `PaymentIntent` status transitions from `processing` to `succeeded`.                                                          |
| `generatedSepaDebitIntentsSucceedDelayed@example.com`              | The `PaymentIntent` status transitions from `processing` to `succeeded` after at least three minutes.                             |
| `generatedSepaDebitIntentsFail@example.com`                        | The `PaymentIntent` status transitions from `processing` to `requires_payment_method`.                                            |
| `generatedSepaDebitIntentsFailDelayed@example.com`                 | The `PaymentIntent` status transitions from `processing` to `requires_payment_method` after at least three minutes.               |
| `generatedSepaDebitIntentsSucceedDisputed@example.com`             | The `PaymentIntent` status transitions from `processing` to `succeeded`, but a dispute is created immediately.                    |
| `generatedSepaDebitIntentsFailsDueToInsufficientFunds@example.com` | The `PaymentIntent` status transitions from `processing` to `requires_payment_method` with the `insufficient_funds` failure code. |

#### PaymentMethod

Use these PaymentMethods to test that the `PaymentIntent` status transitions. These tokens are useful for automated testing to immediately attach the PaymentMethod to the SetupIntent on the server.

| Payment Method                                                  | Description                                                                                                                       |
| --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `pm_ideal_generatedSepaDebitIntentsSucceed`                     | The `PaymentIntent` status transitions from `processing` to `succeeded`.                                                          |
| `pm_ideal_generatedSepaDebitIntentsSucceedDelayed`              | The `PaymentIntent` status transitions from `processing` to `succeeded` after at least three minutes.                             |
| `pm_ideal_generatedSepaDebitIntentsFail`                        | The `PaymentIntent` status transitions from `processing` to `requires_payment_method`.                                            |
| `pm_ideal_generatedSepaDebitIntentsFailDelayed`                 | The `PaymentIntent` status transitions from `processing` to `requires_payment_method` after at least three minutes.               |
| `pm_ideal_generatedSepaDebitIntentsSucceedDisputed`             | The `PaymentIntent` status transitions from `processing` to `succeeded`, but a dispute is created immediately.                    |
| `pm_ideal_generatedSepaDebitIntentsFailsDueToInsufficientFunds` | The `PaymentIntent` status transitions from `processing` to `requires_payment_method` with the `insufficient_funds` failure code. |

## Optional: Set the billing period

When you create a subscription, it automatically sets the billing cycle by default. For example, if a customer subscribes to a monthly plan on September 7, they’re billed on the 7th of every month after that. Some businesses prefer to set the billing cycle manually so that they can charge their customers at the same time each cycle. The [billing cycle anchor](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-billing_cycle_anchor) argument allows you to do this.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  items: [
    {
      price: "{{PRICE_ID}}",
    },
  ],
  billing_cycle_anchor: 1611008505,
});
```

#### Customers v1

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
  billing_cycle_anchor: 1611008505,
});
```

Setting the billing cycle manually automatically charges the customer a prorated amount for the time between the subscription being created and the billing cycle anchor. If you don’t want to charge customers for this time, you can set the [proration_behavior](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-proration_behavior) argument to `none`. You can also combine the billing cycle anchor with [trial periods](https://docs.stripe.com/billing/subscriptions/ideal.md#trial-periods) to give users free access to your product and then charge them a prorated amount.

## Optional: Subscription trials

Free trials allow customers access to your product for a period of time for free. Using free trials is different from setting [proration_behavior](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-proration_behavior) to `none` because you can customize how long the free period lasts. Pass a timestamp in [trial end](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-trial_end) to set the trial period.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  items: [
    {
      price: "{{PRICE_ID}}",
    },
  ],
  trial_end: 1610403705,
});
```

#### Customers v1

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
  trial_end: 1610403705,
});
```

You can also combine a [billing cycle anchor](https://docs.stripe.com/billing/subscriptions/ideal.md#billing-cycle) with a free trial. For example, say it’s September 15 and you want to give your customer a free trial for seven days and then start the normal billing cycle on October 1. You can set the free trial to end on September 22 and the billing cycle anchor to October 1. This gives the customer a free trial for seven days and then charges a prorated amount for the time between the trial ending and October 1. On October 1, you charge them the normal subscription amount for their first full billing cycle.
