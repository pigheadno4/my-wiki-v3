<!-- Source URL: https://docs.stripe.com/payments/amazon-pay/set-up-future-payments -->
<!-- Fetched: 2026-05-07 -->

# Set up future Amazon Pay payments

Learn how to save Amazon Pay details and charge your customers later.

# Checkout

> This is a Checkout for when payment-ui is checkout. View the full page at https://docs.stripe.com/payments/amazon-pay/set-up-future-payments?payment-ui=checkout.

This guide describes how to save Amazon Pay payment details using [Checkout](https://docs.stripe.com/payments/checkout.md), our fully hosted checkout page.

Learn how to [set up a subscription with Amazon Pay](https://docs.stripe.com/billing/subscriptions/amazon-pay.md) to create recurring payments after saving a payment method in Checkout.

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Getting permission to save a payment method [Server-side]

If you save your customer’s payment method for future use, you need permission. Creating an agreement (sometimes called a mandate) up front allows you to save your customer’s payment details and charge them when they’re not actively using your website or app.

Add terms to your website or app that state how you plan to save your customer’s payment method details, and let them opt in. If you plan to charge your customer when they’re offline, make sure that your terms also include the following:

- The customer’s permission for you to initiate a payment or a series of payments on their behalf for specified transactions
- The anticipated frequency (that is, one-time or recurring) and timing of payments
- How you determine the payment amount
- Your cancellation policy, if you’re setting up the payment method for a subscription service

Make sure that you keep a record of your customer’s written agreement to these terms.

## Create or retrieve a customer [Server-side]

To reuse an Amazon Pay payment method for future payments, attach it to an object that represents your customer.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

Create a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/create.md#v2_create_accounts-configuration-customer) or [Customer](https://docs.stripe.com/api/customers/create.md) when your customer creates an account with your business, or when saving a payment method. Associate the object’s ID with your own internal representation of a customer.

Create a new customer or retrieve an existing one to associate with this payment.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const account = await stripe.v2.core.accounts.create({
  contact_email: "jenny.rosen@example.com",
  display_name: "Jenny Rosen",
  configuration: {
    customer: {},
  },
  include: ["configuration.customer"],
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create({
  name: "Jenny Rosen",
  email: "jenny.rosen@example.com",
});
```

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

Create a Checkout Session in `setup` mode to collect the required information. After creating the Checkout Session, redirect your customer to the [URL](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-url) that the response returns.

#### Node.js

```javascript
const session = await stripe.checkout.sessions.create({
  payment_method_types: ["card", "amazon_pay"],
  mode: "setup",
  customer: customer.id,
  success_url: "https://example.com/success",
});
```

## Test your integration

Select Amazon Pay as the payment method, then click **Continue to Amazon Pay**. You can test the successful setup case by authenticating the SetupIntent on the redirect page. The SetupIntent transitions from requires_action to succeeded.

# Direct API

> This is a Direct API for when payment-ui is direct-api. View the full page at https://docs.stripe.com/payments/amazon-pay/set-up-future-payments?payment-ui=direct-api.

You can use the [Setup Intents API](https://docs.stripe.com/payments/setup-intents.md) to collect payment method details in advance, with the final amount or payment date determined later. Use this for:

- Saving payment methods to a wallet to streamline future purchases
- Collecting surcharges after fulfilling a service
- [Starting a free trial for a subscription](https://docs.stripe.com/billing/subscriptions/trials.md)

To collect payment method details and charge the saved payment method immediately, use the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md).

Learn how to [set up a subscription with Amazon Pay](https://docs.stripe.com/billing/subscriptions/amazon-pay.md) to create recurring payments after saving a payment method in Checkout.

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Getting permission to save a payment method [Server-side]

If you save your customer’s payment method for future use, you need permission. Creating an agreement (sometimes called a mandate) up front allows you to save your customer’s payment details, and charge them when they’re not actively using your website or app.

Add terms to your website or app that state how you plan to save your customer’s payment method details, and let your customer opt in. If you plan to charge them when they’re offline, make sure that your terms also cover the following:

- The customer’s permission for you to initiate a payment or a series of payments on their behalf for specified transactions
- The anticipated frequency (that is, one-time or recurring) and timing of payments
- How you determine the payment amount
- Your cancellation policy, if you’re setting the payment method up for a subscription service

Make sure that you keep a record of your customer’s written agreement to these terms.

## Create or retrieve a customer [Server-side]

To save an Amazon Pay payment method for future payments, attach it to an object that represents your customer.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

Create a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/create.md#v2_create_accounts-configuration-customer) or [Customer](https://docs.stripe.com/api/customers/create.md) when your customer creates an account with your business, or when saving a payment method. Associate the object’s ID with your own internal representation of a customer.

Create a new customer or retrieve an existing one to associate with this payment.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const account = await stripe.v2.core.accounts.create({
  contact_email: "jenny.rosen@example.com",
  display_name: "Jenny Rosen",
  configuration: {
    customer: {},
  },
  include: ["configuration.customer"],
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create({
  name: "Jenny Rosen",
  email: "jenny.rosen@example.com",
});
```

## Present authorization terms on your payment form [Client-side]

Save your customer’s Amazon Pay credentials to charge their account for future *off-session* (A payment is described as off-session if it occurs without the direct involvement of the customer, using previously-collected payment information) payments. Your custom payment form must present a written notice of authorization before confirming the [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) or [SetupIntent](https://docs.stripe.com/api/setup_intents.md).

You only need to display the authorization after the first time you save your customer’s Amazon Pay credentials.

We recommend that you use the following text for your custom payment form:

> By continuing, you authorize Rocket Rides to debit your Amazon Pay account for this payment and future payments in accordance with Rocket Rides's terms, until this authorization is revoked.

#### Save a payment method with the Setup Intents API

Use the [Setup Intents API](https://docs.stripe.com/payments/setup-intents.md) to collect payment method details in advance and determine the final amount or payment date at a later point. Use it for:

- Saving payment methods for customers so their later purchases don’t require authentication
- Starting a free trial for a *subscription* (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis)

## Create a SetupIntent and save a payment method [Server-side]

A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) is an object that represents your intent to set up a customer’s payment method for future payments. Create a `SetupIntent` with the customer’s ID, add `amazon_pay` to the [payment_method_types](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-payment_method_types) array, and set [usage](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-usage) to `off_session` or `on_session`. The `SetupIntent` tracks the steps of the setup process.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ["amazon_pay"],
  payment_method_data: {
    type: "amazon_pay",
  },
  usage: "off_session",
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ["amazon_pay"],
  payment_method_data: {
    type: "amazon_pay",
  },
  usage: "off_session",
  customer: "{{CUSTOMER_ID}}",
});
```

### Retrieve the client secret

The SetupIntent includes a *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)) that the client side uses to securely complete the payment process. You can use different approaches to pass the client secret to the client side.

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

Next, you save Amazon Pay on the client with [Stripe.js](https://docs.stripe.com/payments/elements.md).

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

## Optional: Handle the Amazon Pay redirect manually

Stripe.js helps you extend your integration to other payment methods. However, you can manually redirect your customers on your server.

1. Create and *confirm* (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) a PaymentIntent of type `amazon_pay`. By specifying `payment_method_data`, a PaymentMethod is created and immediately used with the PaymentIntent.

You must also provide the URL where your customer is redirected to after they complete their payment in the `return_url` field. You can provide your own query parameters in this URL. These parameters are included in the final URL upon completing the redirect flow.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: "usd",
  payment_method_types: ["amazon_pay"],
  payment_method_data: {
    type: "amazon_pay",
  },
  return_url: "https://example.com/checkout/complete",
  confirm: true,
});
```

1. Check that the `PaymentIntent` has a status of `requires_action` and the type for `next_action` is `redirect_to_url`.

#### Json

```json
{"status": "requires_action",
  "next_action": {
    "type": "redirect_to_url",
    "redirect_to_url": {
      "url": "https://hooks.stripe.com/...",
      "return_url": "https://example.com/checkout/complete"
    }
  },
  "id": "pi_1G1sgdKi6xqXeNtkldRRE6HT",
  "object": "payment_intent",
  ...
}
```

1. Redirect the customer to the URL provided in the `next_action.redirect_to_url.url` property. This code example is approximate—the redirect method might be different in your web framework.

#### Node.js

```javascript
if (
  paymentIntent.status === "requires_action" &&
  paymentIntent.next_action.type === "redirect_to_url"
) {
  const url = paymentIntent.next_action.redirect_to_url.url;
  res.redirect(url);
}
```

Your customer is redirected to the `return_url` when they complete the payment process. The `payment_intent` and `payment_intent_client_secret` URL query parameters are included along with any of your own query parameters. Stripe recommends setting up a [webhook endpoint](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks) to programmatically confirm the status of a payment.

#### Save a payment method with the Payment Intents API

Use the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md) to collect payment method details at checkout and save a payment method to a customer. Use this for:

- Saving payment methods for customers so their later purchases don’t require authentications
- Starting a free trial for a *subscription* (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis)

## Create a PaymentIntent and save a payment method [Server-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) is an object that represents your intent to charge a customer. If you don’t provide a saved payment method with the `PaymentIntent` request, we create a new payment method and attach it to a customer before confirming the `PaymentIntent`.

Create a `PaymentIntent` on your server as follows:

- Add `amazon_pay` to the [payment_method_types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) array.
- Specify the ID of the `Customer` or customer-configured `Account`.
- Set `confirm` to true.
- Set [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) to `off_session`.
- Set the [return_url](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-return_url) to the URL of the page you want to return the customer to after the `PaymentIntent` succeeds.
- If you need to create a mandate, set [mandate_data](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-mandate_data).

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["amazon_pay"],
  payment_method_data: {
    type: "amazon_pay",
  },
  mandate_data: {
    customer_acceptance: {
      type: "online",
      online: {
        ip_address: "127.0.0.0",
        user_agent: "device",
      },
    },
  },
  return_url: "https://www.stripe.com",
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  setup_future_usage: "off_session",
  amount: 1000,
  currency: "usd",
  statement_descriptor: "test_statement",
  capture_method: "automatic",
  confirm: true,
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["amazon_pay"],
  payment_method_data: {
    type: "amazon_pay",
  },
  mandate_data: {
    customer_acceptance: {
      type: "online",
      online: {
        ip_address: "127.0.0.0",
        user_agent: "device",
      },
    },
  },
  return_url: "https://www.stripe.com",
  customer: "{{CUSTOMER_ID}}",
  setup_future_usage: "off_session",
  amount: 1000,
  currency: "usd",
  statement_descriptor: "test_statement",
  capture_method: "automatic",
  confirm: true,
});
```

The returned `PaymentIntent` includes a *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)), which the client side uses to securely complete the payment without needing the `PaymentIntent` object. Pass the client secret to the client-side application to continue with the payment process.

## Create a PaymentIntent using a saved payment method [Server-side]

After you create a [PaymentMethod](https://docs.stripe.com/api/payment_methods.md), you can accept future Amazon Pay payments by creating and confirming a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md). When confirming a PaymentIntent, use the same payment method ID from the previous SetupIntent or PaymentIntent object. The `off_session` value must also be set to true if the customer isn’t in a checkout flow for this PaymentIntent.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["amazon_pay"],
  payment_method: "{{PAYMENTMETHOD_ID}}",
  amount: 1000,
  currency: "usd",
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  statement_descriptor: "test_statement",
  capture_method: "automatic",
  confirm: true,
  off_session: true,
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["amazon_pay"],
  payment_method: "{{PAYMENT_METHOD_ID}}",
  amount: 1000,
  currency: "usd",
  customer: "{{CUSTOMER_ID}}",
  statement_descriptor: "test_statement",
  capture_method: "automatic",
  confirm: true,
  off_session: true,
});
```

## Optional: Detach reusable payment method

To deactivate a reusable payment method, your server can call the [detach PaymentMethod](https://docs.stripe.com/api/payment_methods/detach.md) API. Stripe sends both a [mandate.updated](https://docs.stripe.com/api/events/types.md#event_types-mandate.updated) event and a [payment_method.detached](https://docs.stripe.com/api/events/types.md#event_types-payment_method.detached) event. You can subscribe to [webhook](https://docs.stripe.com/webhooks.md) events to get notifications.

# iOS

> This is a iOS for when payment-ui is mobile and platform is ios. View the full page at https://docs.stripe.com/payments/amazon-pay/set-up-future-payments?payment-ui=mobile&platform=ios.

You can use the [Setup Intents API](https://docs.stripe.com/payments/setup-intents.md) to gather payment method details ahead of time, allowing you to determine the final amount or payment date later. This API is useful for the following scenarios:

- Saving payment methods to a wallet to streamline future purchases.
- Collecting surcharges after providing a service.
- [Initiating a free trial for a subscription](https://docs.stripe.com/billing/subscriptions/trials.md).

If you need to collect payment method details and charge the saved payment method immediately, use the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md) instead.

## Set up Stripe [Server-side] [Client-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

### Server-side

This integration requires endpoints on your server that talk to the Stripe API. Use the official libraries for access to the Stripe API from your server:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

### Client-side

The [Stripe iOS SDK](https://github.com/stripe/stripe-ios) is open source, [fully documented](https://stripe.dev/stripe-ios/index.html), and compatible with apps supporting iOS 13 or above.

#### Swift Package Manager

To install the SDK, follow these steps:

1. In Xcode, select **File** > **Add Package Dependencies…** and enter `https://github.com/stripe/stripe-ios-spm` as the repository URL.
1. Select the latest version number from our [releases page](https://github.com/stripe/stripe-ios/releases).
1. Add the **StripePaymentsUI** product to the [target of your app](https://developer.apple.com/documentation/swift_packages/adding_package_dependencies_to_your_app).

#### CocoaPods

1. If you haven’t already, install the latest version of [CocoaPods](https://guides.cocoapods.org/using/getting-started.html).
1. If you don’t have an existing [Podfile](https://guides.cocoapods.org/syntax/podfile.html), run the following command to create one:
   ```bash
   pod init
   ```
1. Add this line to your `Podfile`:
   ```podfile
   pod 'StripePaymentsUI'
   ```
1. Run the following command:
   ```bash
   pod install
   ```
1. Don’t forget to use the `.xcworkspace` file to open your project in Xcode, instead of the `.xcodeproj` file, from here on out.
1. In the future, to update to the latest version of the SDK, run:
   ```bash
   pod update StripePaymentsUI
   ```

#### Carthage

1. If you haven’t already, install the latest version of [Carthage](https://github.com/Carthage/Carthage#installing-carthage).
1. Add this line to your `Cartfile`:
   ```cartfile
   github "stripe/stripe-ios"
   ```
1. Follow the [Carthage installation instructions](https://github.com/Carthage/Carthage#if-youre-building-for-ios-tvos-or-watchos). Make sure to embed all of the required frameworks listed [here](https://github.com/stripe/stripe-ios/tree/master/StripePaymentsUI/README.md#manual-linking).
1. In the future, to update to the latest version of the SDK, run the following command:
   ```bash
   carthage update stripe-ios --platform ios
   ```

#### Manual Framework

1. Head to our [GitHub releases page](https://github.com/stripe/stripe-ios/releases/latest) and download and unzip **Stripe.xcframework.zip**.
1. Drag **StripePaymentsUI.xcframework** to the **Embedded Binaries** section of the **General** settings in your Xcode project. Make sure to select **Copy items if needed**.
1. Repeat step 2 for all required frameworks listed [here](https://github.com/stripe/stripe-ios/tree/master/StripePaymentsUI/README.md#manual-linking).
1. In the future, to update to the latest version of our SDK, repeat steps 1–3.

> For details on the latest SDK release and past versions, see the [Releases](https://github.com/stripe/stripe-ios/releases) page on GitHub. To receive notifications when a new release is published, [watch releases](https://help.github.com/en/articles/watching-and-unwatching-releases-for-a-repository#watching-releases-for-a-repository) for the repository.

Configure the SDK with your Stripe [publishable key](https://dashboard.stripe.com/test/apikeys) on app start. This enables your app to make requests to the Stripe API.

#### Swift

```swift
import UIKitimportStripePaymentsUI

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {StripeAPI.defaultPublishableKey = "<<YOUR_PUBLISHABLE_KEY>>"
        // do any other necessary launch configuration
        return true
    }
}
```

> Use your [test keys](https://docs.stripe.com/keys.md#obtain-api-keys) while you test and develop, and your [live mode](https://docs.stripe.com/keys.md#test-live-modes) keys when you publish your app.

## Get permission to save a payment method [Server-side]

If you save your customer’s payment method for future use, you need permission. Creating an agreement (sometimes called a mandate) up front allows you to save your customer’s payment details, and charge them when they’re not actively using your website or app.

Add terms to your website or app that state how you plan to save your customer’s payment method details, and let your customer opt in. If you plan to charge them when they’re offline, make sure that your terms also cover the following:

- The customer’s permission for you to initiate a payment or a series of payments on their behalf for specified transactions.
- The anticipated frequency (that is, one-time or recurring) and timing of payments.
- How you determine the payment amount.
- Your cancellation policy, if you’re setting the payment method up for a subscription service.

Make sure that you keep a record of your customer’s written agreement to these terms.

## Create or retrieve a customer [Server-side]

To save an Amazon Pay payment method for future payments, attach it to an object that represents your customer.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

Create a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/create.md#v2_create_accounts-configuration-customer) or [Customer](https://docs.stripe.com/api/customers/create.md) when your customer creates an account with your business, or when saving a payment method. Associate the object’s ID with your own internal representation of a customer.

Create a new customer or retrieve an existing one to associate with this payment.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const account = await stripe.v2.core.accounts.create({
  contact_email: "jenny.rosen@example.com",
  display_name: "Jenny Rosen",
  configuration: {
    customer: {},
  },
  include: ["configuration.customer"],
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create({
  name: "Jenny Rosen",
  email: "jenny.rosen@example.com",
});
```

## Present authorization terms on your payment form [Client-side]

Save your customer’s Amazon Pay credentials to charge their account for future *off-session* (A payment is described as off-session if it occurs without the direct involvement of the customer, using previously-collected payment information) payments. Your custom payment form must present a written notice of authorization before confirming the [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) or [SetupIntent](https://docs.stripe.com/api/setup_intents.md). You only need to display the authorization after the first time you save your customer’s Amazon Pay credentials.

We recommend that you use the following text for your custom payment form:

> By continuing, you authorize Rocket Rides to debit your Amazon Pay account for this payment and future payments in accordance with Rocket Rides's terms, until this authorization is revoked.

## Collect payment method details [Client-side]

#### Swift

```swift
// Amazon Pay does not require additional parameters so we only need to pass the initialized
// STPPaymentMethodAmazonPayParams instance to STPPaymentMethodParams
let amazonPay = STPPaymentMethodAmazonPayParams()
let paymentMethodParams = STPPaymentMethodParams(amazonPay: amazonPay, billingDetails: nil, metadata: nil)
```

## Submit the payment to Stripe [Client-side]

Retrieve the client secret from the SetupIntent you created and call [STPPaymentHandler confirmSetupIntent](<https://stripe.dev/stripe-ios/stripe-payments/Classes/STPPaymentHandler.html#/c:objc(cs)STPPaymentHandler(im)confirmSetupIntent:withAuthenticationContext:completion:>). This presents a webview where the customer can complete the payment with Amazon Pay. Afterwards, the completion block is called with the result of the payment.

#### Swift

```swift
let setupIntentParams = STPSetupIntentConfirmParams(clientSecret: setupIntentClientSecret)
setupIntentParams.paymentMethodParams = paymentMethodParams
setupIntentParams.returnURL = "payments-example://stripe-redirect"

STPPaymentHandler.shared().confirmSetupIntent(setupIntentParams, with: self) { (handlerStatus, setupIntent, error) in
    switch handlerStatus {
    case .succeeded:
        // Setup succeeded

    case .canceled:
        // Setup was canceled

    case .failed:
        // Setup failed

    @unknown default:
        fatalError()
    }
}
```

## Create a PaymentIntent using a saved payment method [Server-side]

After you create a [PaymentMethod](https://docs.stripe.com/api/payment_methods.md), you can accept future Amazon Pay payments by creating and confirming a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md). When confirming a `PaymentIntent`, use the ID of the `PaymentMethod` you created. If the customer isn’t in a checkout flow for this `PaymentIntent`, set `off_session` to true.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["amazon_pay"],
  payment_method: "{{PAYMENTMETHOD_ID}}",
  amount: 1000,
  currency: "usd",
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  statement_descriptor: "test_statement",
  capture_method: "automatic",
  confirm: true,
  off_session: true,
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["amazon_pay"],
  payment_method: "{{PAYMENT_METHOD_ID}}",
  amount: 1000,
  currency: "usd",
  customer: "{{CUSTOMER_ID}}",
  statement_descriptor: "test_statement",
  capture_method: "automatic",
  confirm: true,
  off_session: true,
});
```

## Detach a reusable payment method

To deactivate a reusable payment method, you can use the Stripe API to call the [detach PaymentMethod](https://docs.stripe.com/api/payment_methods/detach.md) endpoint from your server. This detaches the payment method from the customer’s account.

When you detach a payment method, Stripe sends two events:

- [mandate.updated](https://docs.stripe.com/api/events/types.md#event_types-mandate.updated): This event indicates that the mandate associated with the payment method has been updated.

- [payment_method.detached](https://docs.stripe.com/api/events/types.md#event_types-payment_method.detached): This event indicates that the payment method has been detached from the customer’s account.

To receive notifications about these events, you can subscribe to [webhook](https://docs.stripe.com/webhooks.md) events. For more details on how to revoke a reusable payment method, see [detach PaymentMethod](https://docs.stripe.com/api/payment_methods/detach.md) documentation.

# Android

> This is a Android for when payment-ui is mobile and platform is android. View the full page at https://docs.stripe.com/payments/amazon-pay/set-up-future-payments?payment-ui=mobile&platform=android.

You can use the [Setup Intents API](https://docs.stripe.com/payments/setup-intents.md) to gather payment method details ahead of time, allowing you to determine the final amount or payment date later. This API is useful for the following scenarios:

- Saving payment methods to a wallet to streamline future purchases.
- Collecting surcharges after providing a service.
- [Initiating a free trial for a subscription](https://docs.stripe.com/billing/subscriptions/trials.md).

If you need to collect payment method details and charge the saved payment method immediately, use the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md).

## Set up Stripe [Server-side] [Client-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

### Server-side

This integration requires endpoints on your server that talk to the Stripe API. Use the official libraries for access to the Stripe API from your server:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

### Client-side

The [Stripe Android SDK](https://github.com/stripe/stripe-android) is open source and [fully documented](https://stripe.dev/stripe-android/).

To install the SDK, add `stripe-android` to the `dependencies` block of your [app/build.gradle](https://developer.android.com/studio/build/dependencies) file:

#### Kotlin

```kotlin
plugins {
    id("com.android.application")
}

android { ... }

dependencies {
  // ...

  // Stripe Android SDK
  implementation("com.stripe:stripe-android:23.7.0")
  // Include the financial connections SDK to support US bank account as a payment method
  implementation("com.stripe:financial-connections:23.7.0")
}
```

> For details on the latest SDK release and past versions, see the [Releases](https://github.com/stripe/stripe-android/releases) page on GitHub. To receive notifications when a new release is published, [watch releases for the repository](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/configuring-notifications#configuring-your-watch-settings-for-an-individual-repository).

Configure the SDK with your Stripe [publishable key](https://dashboard.stripe.com/apikeys) so that it can make requests to the Stripe API, such as in your `Application` subclass:

#### Kotlin

```kotlin
import com.stripe.android.PaymentConfiguration

class MyApp : Application() {
    override fun onCreate() {
        super.onCreate()
        PaymentConfiguration.init(
            applicationContext,
            "<<YOUR_PUBLISHABLE_KEY>>"
        )
    }
}
```

> Use your [test keys](https://docs.stripe.com/keys.md#obtain-api-keys) while you test and develop, and your [live mode](https://docs.stripe.com/keys.md#test-live-modes) keys when you publish your app.

Stripe samples also use [OkHttp](https://github.com/square/okhttp) and [GSON](https://github.com/google/gson) to make HTTP requests to a server.

## Create or retrieve a customer [Server-side]

To save an Amazon Pay payment method for future payments, attach it to an object that represents your customer.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

Create a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/create.md#v2_create_accounts-configuration-customer) or [Customer](https://docs.stripe.com/api/customers/create.md) when your customer creates an account with your business, or when saving a payment method. Associate the object’s ID with your own internal representation of a customer.

Create a new customer or retrieve an existing one to associate with this payment.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const account = await stripe.v2.core.accounts.create({
  contact_email: "jenny.rosen@example.com",
  display_name: "Jenny Rosen",
  configuration: {
    customer: {},
  },
  include: ["configuration.customer"],
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create({
  name: "Jenny Rosen",
  email: "jenny.rosen@example.com",
});
```

## Create a SetupIntent [Server-side]

A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) represents your intention to set up a customer’s payment method for future payments. It tracks the steps of this setup process.

To create a `SetupIntent` on your server, follow these steps:

1. Set [payment_method_types](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-payment_method_types) to `amazon_pay`.
1. Specify the ID of the `Customer` or customer-configured `Account`.
1. Set [usage](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-usage) to `off_session` or `on_session`.
1. Include the following code on your server:

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ["amazon_pay"],
  payment_method_data: {
    type: "amazon_pay",
  },
  usage: "off_session",
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ["amazon_pay"],
  payment_method_data: {
    type: "amazon_pay",
  },
  usage: "off_session",
  customer: "{{CUSTOMER_ID}}",
});
```

## Present authorization terms on your payment form [Client-side]

When saving your customer’s Amazon Pay credentials to charge their account for future *off-session* (A payment is described as off-session if it occurs without the direct involvement of the customer, using previously-collected payment information) payments, it’s important to present a written notice of authorization on your payment form before confirming the [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) or [SetupIntent](https://docs.stripe.com/api/setup_intents.md).

The authorization terms only need to be displayed the first time you save a customer’s credentials.

We recommend using the following text for your custom payment form:

> By continuing, you authorize Rocket Rides to debit your Amazon account for this payment and future payments in accordance with Rocket Rides's terms, until this authorization is revoked. You can change this anytime in your Amazon Settings.

Make sure that you replace Rocket Rides with the actual business name of your entity.

## Submit the payment method details to Stripe [Client-side]

To submit the payment method details to Stripe, follow these steps:

1. Retrieve the client secret from the SetupIntent that you created.

1. Call `PaymentLauncher.confirm()` with the client secret. This redirects the customer to Amazon, where they can complete the setup process.

1. After the customer completes the setup process, the `PaymentResultCallback` that you provided is called with the result of the payment.

To learn more, see [PaymentLauncher confirm](https://stripe.dev/stripe-android/payments-core/com.stripe.android.payments.paymentlauncher/-payment-launcher/confirm.html).

#### Kotlin

```kotlin
class AmazonPaySetupActivity : AppCompatActivity() {

    // ...

    private val paymentLauncher: PaymentLauncher by lazy {
        val paymentConfiguration = PaymentConfiguration.getInstance(applicationContext)
        PaymentLauncher.create(
            activity = this,
            publishableKey = paymentConfiguration.publishableKey,
            stripeAccountId = paymentConfiguration.stripeAccountId,
            callback = ::onPaymentResult,
        )
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        // …
        startCheckout()
    }

    private fun startCheckout() {
        // Create a SetupIntent on your backend and return the client_secret here
        val setupIntentClientSecret = // …

        val amazonPayParams = PaymentMethodCreateParams.createAmazonPay()

        val confirmParams = ConfirmSetupIntentParams.create(
            paymentMethodCreateParams = amazonPayParams,
            clientSecret = setupIntentClientSecret,
            // Add a mandate ID or MandateDataParams…
        )

        paymentLauncher.confirm(confirmParams)
    }

    private fun onPaymentResult(paymentResult: PaymentResult) {
        // Handle the setup result…
    }
}
```

## Create a PaymentIntent using a saved payment method [Server-side]

To accept future Amazon Pay payments, you can create and confirm a PaymentIntent after creating a PaymentMethod. Follow these steps:

1. Create a [PaymentMethod](https://docs.stripe.com/api/payment_methods.md) for the customer.

1. When confirming the `PaymentIntent`, use the ID of the `PaymentMethod` you created.

1. If the customer isn’t in a checkout flow for this `PaymentIntent`, set `off_session` to true.

Following these steps will allow you to accept future Amazon Pay payments using the saved payment method.

For more detailed instructions on creating and confirming a `PaymentIntent` with a saved payment method, see [The Payment Intents API](https://docs.stripe.com/payments/payment-intents.md).

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["amazon_pay"],
  payment_method: "{{PAYMENTMETHOD_ID}}",
  amount: 1000,
  currency: "usd",
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  statement_descriptor: "test_statement",
  capture_method: "automatic",
  confirm: true,
  off_session: true,
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["amazon_pay"],
  payment_method: "{{PAYMENTMETHOD_ID}}",
  amount: 1000,
  currency: "usd",
  customer: "{{CUSTOMER_ID}}",
  statement_descriptor: "test_statement",
  capture_method: "automatic",
  confirm: true,
  off_session: true,
});
```

## Detach a reusable payment method

To deactivate a reusable payment method, you can use the Stripe API to call the [detach PaymentMethod](https://docs.stripe.com/api/payment_methods/detach.md) endpoint from your server. This detaches the payment method from the customer’s account.

When you detach a payment method, Stripe sends two events:

- [mandate.updated](https://docs.stripe.com/api/events/types.md#event_types-mandate.updated): This event indicates that the mandate associated with the payment method has been updated.

- [payment_method.detached](https://docs.stripe.com/api/events/types.md#event_types-payment_method.detached): This event indicates that the payment method has been detached from the customer’s account.

To receive notifications about these events, you can subscribe to [webhook](https://docs.stripe.com/webhooks.md) events.

For more details on how to revoke a reusable payment method, see [detach PaymentMethod](https://docs.stripe.com/api/payment_methods/detach.md).
