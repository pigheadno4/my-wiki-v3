<!-- Source URL: https://docs.stripe.com/payments/cash-app-pay/set-up-payment -->
<!-- Fetched: 2026-05-07 -->

# Set up future Cash App Pay payments

Learn how to save Cash App Pay details and charge your customers later.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

This guide covers how to save a Cash App Pay payment details using [Checkout](https://docs.stripe.com/payments/checkout.md), our fully hosted checkout page.

To create recurring payments after saving a payment method in Checkout, see [Set up a subscription with Cash App Pay](https://docs.stripe.com/billing/subscriptions/cash-app-pay.md) for more details.

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create or retrieve a Customer [Server-side]

To reuse a Cash App Pay payment method for future payments, attach it to a *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments).

Create a [Customer object](https://docs.stripe.com/api/customers.md) when your customer creates an account with your business, and associate the ID of the Customer object with your own internal representation of a customer. Alternatively, you can create a new Customer later, right before saving a payment method for future payments.

Create a new Customer or retrieve an existing Customer to associate with this payment. Include the following code on your server to create a new Customer.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create({
  description: "My First Test Customer (created for API docs)",
});
```

## Create a Checkout Session [Server-side]

Your customer must authorize you to use their Cash App account for future payments through Stripe Checkout. This allows you to accept Cash App payments. Add a checkout button to your website that calls a server-side endpoint to create a [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md).

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

Create a Checkout Session in `setup` mode to collect the required information. After creating the Checkout Session, redirect your customer to the [URL](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-url) returned in the response.

#### Node.js

```javascript
const session = await stripe.checkout.sessions.create({
  payment_method_types: ["card", "cashapp"],
  mode: "setup",
  customer: customer.id,
  success_url: "https://example.com/success",
});
```

## Test your integration [Server-side]

#### Mobile web app testing

To test your integration, choose Cash App Pay as the payment method and tap **Pay**. While testing, this redirects you to a test payment page where you can approve or decline the payment.

In live mode, tapping **Pay** redirects you to the Cash App mobile application—you don’t have the option to approve or decline the payment within Cash App. The payment is automatically approved after the redirect.

#### Desktop web app testing

To test your integration, scan the QR code with a QR code scanning application on your mobile device. While testing, the QR code payload contains a URL that redirects you to a test payment page where you can approve or decline the test payment.

In live mode, scanning the QR code redirects you to the Cash App mobile application—you don’t have the option to approve or decline the payment within Cash App. The payment is automatically approved after you scan the QR code.

# Direct API

> This is a Direct API for when payment-ui is direct-api. View the full page at https://docs.stripe.com/payments/cash-app-pay/set-up-payment?payment-ui=direct-api.

You can use the [Setup Intents API](https://docs.stripe.com/payments/setup-intents.md) to collect payment method details in advance, and determine the final amount or payment date later. Use it to:

- Save payment methods to a wallet to streamline future purchases
- Collect surcharges after fulfilling a service
- [Start a free trial for a subscription](https://docs.stripe.com/billing/subscriptions/trials.md)

To collect payment method details and charge the saved payment method immediately, use the Payment Intents API.

To create recurring payments after saving a payment method in Checkout, see [Set up a subscription with Cash App Pay](https://docs.stripe.com/billing/subscriptions/cash-app-pay.md) for more details.

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create or retrieve a Customer [Server-side]

To save a Cash App Pay payment method for future payments, you must attach it to a *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments).

Create a Customer object when your customer creates an account with your business. Associate the ID of the Customer object with your own internal representation of a customer. Alternatively, you can create the Customer object before you save a payment method for future payments.

Include the following code on your server to create a new Customer.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create({
  description: "My First Test Customer (created for API docs)",
});
```

## Present authorization terms on your payment form [Client-side]

Save your customer’s Cash App Pay credentials([$Cashtag](https://cash.app/help/us/en-us/3123-cashtags)) to charge their account for future, *off-session* (A payment is described as off-session if it occurs without the direct involvement of the customer, using previously-collected payment information) payments. Your custom payment form must present a written notice of authorization before confirming the [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) or [SetupIntent](https://docs.stripe.com/api/setup_intents.md).

The authorization terms only need to be displayed the first time you save a customer’s $Cashtag.

We recommend that you use the following text for your custom payment form:

> By continuing, you authorize Rocket Rides to debit your Cash App account for this payment and future payments in accordance with Rocket Rides's terms, until this authorization is revoked. You can change this anytime in your Cash App Settings.

#### Save a payment method with the Setup Intents API

Use the [Setup Intents API](https://docs.stripe.com/payments/setup-intents.md) to collect payment method details in advance and determine the final amount or payment date at a later point. This is useful for:

- Saving payment methods for customers so their later purchases don’t require authentications
- Starting a free trial for a *subscription* (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis)

## Create a SetupIntent and save a payment method [Server-side]

A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) is an object that represents your intent to set up a customer’s payment method for future payments. The SetupIntent tracks the steps of this set-up process. Create a SetupIntent on your server with [payment_method_types](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-payment_method_types) set to `cashapp` and specify the Customer’s ID and [usage=off_session](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-usage) or `usage=on_session`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ["cashapp"],
  payment_method_data: {
    type: "cashapp",
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

Next, you save Cash App Pay on the client with [Stripe.js](https://docs.stripe.com/payments/elements.md).

Include the Stripe.js script on your checkout page by adding it to the `head` of your HTML file.

```html
<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/dahlia/stripe.js"></script>
</head>
```

Create an instance of Stripe.js with the following JavaScript on your checkout page:

```javascript
// Set your publishable key. Remember to change this to your live publishable key in production!
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");
```

Use `stripe.confirmCashappSetup` to confirm the setupIntent on the client side, with a [return_url](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-return_url) and an optional [mandate_data](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-mandate_data). Use the [return_url](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-return_url) to redirect customers to a specific page after the SetupIntent succeeds.

```javascript
const form = document.getElementById("setup-form");

form.addEventListener("submit", function (event) {
  event.preventDefault();

  // Set the clientSecret here
  stripe.confirmCashappSetup(clientSecret, {
    payment_method: {
      type: "cashapp",
    },
    return_url: "https://www.example.com/checkout/done",
  });
});
```

Customers can authenticate Cash App Pay with mobile or desktop apps. After calling `confirmCashappSetup`, the client the customer uses determines the authentication method such as redirect for mobile or QR code for desktop. The authentication response also includes a payment method ID that you need to use in the next step to make a PaymentIntent.

#### Mobile application authentication

After calling `confirmCashappSetup`, Stripe redirects your customers to Cash App for authorization. After they authorize the payment, Stripe sends them to the Setup Intent’s `return_url`. Stripe adds `setup_intent`, `setup_intent_client_secret`, `redirect_pm_type`, and `redirect_status` as URL query parameters, along with any existing query parameters in the `return_url`.

An authentication session expires after 10 minutes, and the SetupIntent’s status transitions back to `require_payment_method`. After the status transitions, the customer sees an authorization error and must restart the process.

#### Desktop web app authentication

After calling `confirmCashappSetup`, a QR code displays on the webpage. Your customers can scan the QR code using either their mobile device’s camera or the Cash App mobile application to finish authorization session. A few seconds after authentication successfully, the QR code modal closes automatically.

An authentication session expires after 10 minutes. You can refresh the QR code up to 20 times before the SetupIntent’s status transitions back to `require_payment_method`. After the status transitions, the customer sees an authorization error and must restart the process.

## Optional: Handle redirect and authentication manually

We recommend using Stripe.js to handle redirects and authentication with `confirmCashappSetup`. However, you can also handle redirects and authentication manually on your server.

Specify `handleActions: false` in the `confirmCashappSetup` call.

```javascript
const form = document.getElementById("payment-form");

form.addEventListener("submit", function (event) {
  event.preventDefault();

  // Set the clientSecret here you got in Step 2
  stripe
    .confirmCashappSetup(
      clientSecret,
      {
        payment_method: {
          type: "cashapp",
        },
        return_url: "https://www.example.com/checkout/done",
      },
      {
        handleActions: false,
      },
    )
    .then((result) => {
      if (result.error) {
        // Display error to your customer.
      } else if (result.paymentIntent.status === "requires_action") {
        const nextAction =
          result.setupIntent.next_action
            .cashapp_handle_redirect_or_display_qr_code;
        const expiresAt = nextAction.qr_code.expires_at;
        if (IS_MOBILE) {
          // This URL redirects the customer to Cash App to approve or decline the payment.
          const mobileAuthUrl = nextAction.mobile_auth_url;
        } else if (IS_DESKTOP) {
          // Render the QR code and display it to the customer using the below image source.
          const imageUrlSvg = nextAction.qr_code.image_url_svg;
          const imageUrlPng = nextAction.qr_code.image_url_png;
        }
      }
    });
});
```

The SetupIntent response includes the status `requires_action`, which means your users must perform another action to complete saving the payment method.

#### Mobile application authentication

If a customer is saving a Cash App Pay payment method on a mobile device:

1. Redirect the customer to the URL set as the `next_action.cashapp_handle_redirect_or_display_qr_code.mobile_auth_url` property from the SetupIntent response. This redirects the customer to Cash App, where they can finish the authentication session.
1. The `mobile_auth_url` expires after 30 seconds. If the customer isn’t redirected to `mobile_auth_url` before expiration, call [stripe.retrieveSetupIntent](https://docs.stripe.com/js/setup_intents/retrieve_setup_intent) to get a new `mobile_auth_url`.

#### Desktop web app authentication

If a customer is saving a Cash App Pay payment method on a desktop web app:

1. Redirect the customer to the URL set as the `next_action.cashapp_handle_redirect_or_display_qr_code.hosted_instructions_url` property from the SetupIntent response.
1. The customer scans the QR code rendered on this page using either their mobile device’s camera or the Cash App mobile application to finish the authentication session.

After a successful in-app authentication, Cash App redirects customers to the `return_url` you set in the request to complete checkout, and the SetupIntent automatically moves to a `succeeded` state. The SetupIntent response also includes a payment method ID that you can reuse with future PaymentIntents.

#### Save a payment method with the Payment Intents API

Use the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md) to collect payment method details at checkout and save a payment method to a customer. This is useful for:

- Saving payment methods for customers so their later purchases don’t require authentications
- Starting a free trial for a *subscription* (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis)

## Create a PaymentIntent and save a payment method [Server-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) is an object that represents your intent to charge a customer. If you don’t provide a saved payment method with the PaymentIntent request, a new payment method gets created and attached to a customer before confirming the PaymentIntent. Create a PaymentIntent on your server with [payment_method_types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) set to `cashapp` and specify the Customer’s ID, `confirm=true`, [setup_future_usage=off_session](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) (or `on_session`) with a [return_url](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-return_url) and an optional [mandate_data](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-mandate_data). Use the [return_url](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-return_url) to redirect customers to a specific page after the PaymentIntent succeeds.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["cashapp"],
  payment_method_data: {
    type: "cashapp",
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

The returned PaymentIntent includes a *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)), which the client-side uses to securely complete the payment instead of passing the entire PaymentIntent object. Pass the client secret to the client-side application to continue with the payment process.

The PaymentIntent response includes the status `requires_action`, which requires your users to perform another action to complete the PaymentIntent. Use the `next_action.cashapp_handle_redirect_or_display_qr_code.hosted_instructions_url` object from the same PaymentIntent response to redirect your customers to a page to help them open the Cash App mobile application to finish the authentication session. After a successful in-app authentication, Cash App redirects customers to the `return_url` you set in the request, the payment gets confirmed, and the PaymentIntent automatically moves to a `succeeded` state. The PaymentIntent response also includes a payment method ID that you can re-use with future PaymentIntents.

## Create a PaymentIntent using a saved payment method [Server-side]

After you create a [PaymentMethod](https://docs.stripe.com/api/payment_methods.md), you can accept future Cash App Pay payments by creating and confirming a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md). When confirming a PaymentIntent, use the same payment method ID from the previous SetupIntent or PaymentIntent object. The `off_session` value must also be set to true if the customer isn’t in a checkout flow for this PaymentIntent.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["cashapp"],
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

## Handle reusable payment method revocation

There are two ways to revoke a reusable payment method:

- A customer can deactivate a reusable payment method in the Cash App mobile application. In this case, Stripe sends a [mandate.updated](https://docs.stripe.com/api/events/types.md#event_types-mandate.updated) event. Subscribe to [webhook](https://docs.stripe.com/webhooks.md) events, and call [detach PaymentMethod](https://docs.stripe.com/api/payment_methods/detach.md) to deactivate it.
- A customer can also deactivate a reusable payment method on your UI, if supported. In this case, your server can call [detach PaymentMethod](https://docs.stripe.com/api/payment_methods/detach.md) to deactivate it.

In both cases, after you call the [detach PaymentMethod](https://docs.stripe.com/api/payment_methods/detach.md), a [payment_method.detached](https://docs.stripe.com/api/events/types.md#event_types-payment_method.detached) event is sent to you.

# iOS

> This is a iOS for when payment-ui is mobile and platform is ios. View the full page at https://docs.stripe.com/payments/cash-app-pay/set-up-payment?payment-ui=mobile&platform=ios.

You can use the [Setup Intents API](https://docs.stripe.com/payments/setup-intents.md) to collect payment method details in advance, and determine the final amount or payment date later. Use it to:

- Save payment methods to a wallet to streamline future purchases
- Collect surcharges after fulfilling a service
- [Start a free trial for a subscription](https://docs.stripe.com/billing/subscriptions/trials.md)

This guide covers how to first save payment method details using the Setup Intents API, and how to use the Payment Intents API to charge the saved payment method later.

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

## Create or retrieve a Customer [Server-side]

To save a Cash App Pay payment method for future payments, you must attach it to a *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments).

Create a Customer object when your customer creates an account with your business. Associate the ID of the Customer object with your own internal representation of a customer. Alternatively, you can create the Customer object before you save a payment method for future payments.

Include the following code on your server to create a new Customer.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create({
  description: "My First Test Customer (created for API docs)",
});
```

## Create a SetupIntent [Server-side]

A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) is an object that represents your intent to set up a customer’s payment method for future payments. The SetupIntent tracks the steps of this set-up process. Create a SetupIntent on your server with [payment_method_types](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-payment_method_types) set to `cashapp` and specify the Customer’s ID and [usage=off_session](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-usage) or `usage=on_session`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ["cashapp"],
  payment_method_data: {
    type: "cashapp",
  },
  usage: "off_session",
  customer: "{{CUSTOMER_ID}}",
});
```

## Present authorization terms on your payment form [Client-side]

Save your customer’s Cash App Pay credentials([$Cashtag](https://cash.app/help/us/en-us/3123-cashtags)) to charge their account for future, *off-session* (A payment is described as off-session if it occurs without the direct involvement of the customer, using previously-collected payment information) payments. Your custom payment form must present a written notice of authorization before confirming the [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) or [SetupIntent](https://docs.stripe.com/api/setup_intents.md).

The authorization terms only need to be displayed the first time you save a customer’s $Cashtag.

We recommend that you use the following text for your custom payment form:

> By continuing, you authorize Rocket Rides to debit your Cash App account for this payment and future payments in accordance with Rocket Rides's terms, until this authorization is revoked. You can change this anytime in your Cash App Settings.

## Collect payment method details [Client-side]

#### Swift

```swift
// Cash App Pay does not require additional parameters so we only need to pass the initialized
// STPPaymentMethodCashAppParams instance to STPPaymentMethodParams
let cashApp = STPPaymentMethodCashAppParams()
let paymentMethodParams = STPPaymentMethodParams(cashApp: cashApp, billingDetails: nil, metadata: nil)
```

## Submit the payment to Stripe [Client-side]

Retrieve the client secret from the SetupIntent you created and call [STPPaymentHandler confirmSetupIntent](<https://stripe.dev/stripe-ios/stripe-payments/Classes/STPPaymentHandler.html#/c:objc(cs)STPPaymentHandler(im)confirmSetupIntent:withAuthenticationContext:completion:>). This presents a webview where the customer can complete the payment in Cash App. Afterwards, the completion block is called with the result of the payment.

#### Swift

```swift
let setupIntentParams = STPSetupIntentConfirmParams(clientSecret: setupIntentClientSecret)
setupIntentParams.paymentMethodParams = paymentMethodParams
setupIntentParams.returnURL = "payments-example://stripe-redirect"

STPPaymentHandler.shared().confirmSetupIntent(withParams: setupIntentParams, authenticationContext: self) { (handlerStatus, setupIntent, error) in
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

After you create a [PaymentMethod](https://docs.stripe.com/api/payment_methods.md), you can accept future Cash App Pay payments by creating and confirming a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md). When confirming a PaymentIntent, use the same payment method ID from the previous SetupIntent or PaymentIntent object. The `off_session` value must also be set to true if the customer isn’t in a checkout flow for this PaymentIntent.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["cashapp"],
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

## Handle reusable payment method revocation

There are two ways to revoke a reusable payment method:

- A customer can deactivate a reusable payment method in the Cash App mobile application. In this case, Stripe sends a [mandate.updated](https://docs.stripe.com/api/events/types.md#event_types-mandate.updated) event. Subscribe to [webhook](https://docs.stripe.com/webhooks.md) events, and call [detach PaymentMethod](https://docs.stripe.com/api/payment_methods/detach.md) to deactivate it.
- A customer can also deactivate a reusable payment method on your UI, if supported. In this case, your server can call [detach PaymentMethod](https://docs.stripe.com/api/payment_methods/detach.md) to deactivate it.

In both cases, after you call the [detach PaymentMethod](https://docs.stripe.com/api/payment_methods/detach.md), a [payment_method.detached](https://docs.stripe.com/api/events/types.md#event_types-payment_method.detached) event is sent to you.

# Android

> This is a Android for when payment-ui is mobile and platform is android. View the full page at https://docs.stripe.com/payments/cash-app-pay/set-up-payment?payment-ui=mobile&platform=android.
> Available in: US
> You can use the [Setup Intents API](https://docs.stripe.com/payments/setup-intents.md) or the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md) to save Cash App Pay details for future payments.

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

## Create or retrieve a Customer [Server-side]

To save a Cash App Pay payment method for future payments, you must attach it to a *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments).

Create a Customer object when your customer creates an account with your business. Associate the ID of the Customer object with your own internal representation of a customer. Alternatively, you can create the Customer object before you save a payment method for future payments.

Include the following code on your server to create a new Customer.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create({
  description: "My First Test Customer (created for API docs)",
});
```

## Create a SetupIntent [Server-side]

A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) is an object that represents your intent to set up a customer’s payment method for future payments. The SetupIntent tracks the steps of this set-up process. Create a SetupIntent on your server with [payment_method_types](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-payment_method_types) set to `cashapp` and specify the Customer’s ID and [usage=off_session](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-usage) or `usage=on_session`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ["cashapp"],
  payment_method_data: {
    type: "cashapp",
  },
  usage: "off_session",
  customer: "{{CUSTOMER_ID}}",
});
```

## Present authorization terms on your payment form [Client-side]

Save your customer’s Cash App Pay credentials([$Cashtag](https://cash.app/help/us/en-us/3123-cashtags)) to charge their account for future, *off-session* (A payment is described as off-session if it occurs without the direct involvement of the customer, using previously-collected payment information) payments. Your custom payment form must present a written notice of authorization before confirming the [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) or [SetupIntent](https://docs.stripe.com/api/setup_intents.md).

The authorization terms only need to be displayed the first time you save a customer’s $Cashtag.

We recommend that you use the following text for your custom payment form:

> By continuing, you authorize Rocket Rides to debit your Cash App account for this payment and future payments in accordance with Rocket Rides's terms, until this authorization is revoked. You can change this anytime in your Cash App Settings.

## Submit the payment method details to Stripe [Client-side]

Retrieve the client secret from the SetupIntent you created and call [PaymentLauncher confirm](https://stripe.dev/stripe-android/payments-core/com.stripe.android.payments.paymentlauncher/-payment-launcher/confirm.html). This presents a webview where the customer can complete the setup with Cash App Pay. Upon completion, the provided `PaymentResultCallback` is called with the result of the payment.

#### Kotlin

```kotlin
class CashAppPaySetupActivity : AppCompatActivity() {

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

        val cashAppPayParams = PaymentMethodCreateParams.createCashAppPay()

        val confirmParams = ConfirmSetupIntentParams.create(
            paymentMethodCreateParams = cashAppPayParams,
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

After you create a [PaymentMethod](https://docs.stripe.com/api/payment_methods.md), you can accept future Cash App Pay payments by creating and confirming a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md). When confirming a PaymentIntent, use the same payment method ID from the previous SetupIntent or PaymentIntent object. The `off_session` value must also be set to true if the customer isn’t in a checkout flow for this PaymentIntent.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["cashapp"],
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

## Handle reusable payment method revocation

There are two ways to revoke a reusable payment method:

- A customer can deactivate a reusable payment method in the Cash App mobile application. In this case, Stripe sends a [mandate.updated](https://docs.stripe.com/api/events/types.md#event_types-mandate.updated) event. Subscribe to [webhook](https://docs.stripe.com/webhooks.md) events, and call [detach PaymentMethod](https://docs.stripe.com/api/payment_methods/detach.md) to deactivate it.
- A customer can also deactivate a reusable payment method on your UI, if supported. In this case, your server can call [detach PaymentMethod](https://docs.stripe.com/api/payment_methods/detach.md) to deactivate it.

In both cases, after you call the [detach PaymentMethod](https://docs.stripe.com/api/payment_methods/detach.md), a [payment_method.detached](https://docs.stripe.com/api/events/types.md#event_types-payment_method.detached) event is sent to you.
