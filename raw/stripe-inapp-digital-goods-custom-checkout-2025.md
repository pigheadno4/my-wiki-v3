<!-- Source URL: https://docs.stripe.com/mobile/digital-goods/custom-checkout -->
<!-- Fetched: 2026-04-22 -->

# Accept payments for digital goods on iOS with your own checkout page

Open your own checkout to sell in-app digital goods and subscriptions using Payment Element.

For digital products, content, and subscriptions sold in the United States or European Economic Area (EEA), your iOS app can accept Apple Pay using [Elements](https://docs.stripe.com/payments/elements.md).

If you have a limited number of products and prices, you can instead use [Payment Links](https://docs.stripe.com/mobile/digital-goods/payment-links.md).

In other regions, your app can’t accept Apple Pay for digital products, content, or subscriptions.

This guide describes how to sell a subscription in your app using Elements to redirect your customers to your own checkout page.

If you already have your own checkout page that uses Elements, you can skip to the [Set up universal links step](https://docs.stripe.com/mobile/digital-goods/custom-checkout.md#universal-links).

> If your business is new to Stripe, processes a high volume of payments, and has advanced integration needs, [contact our sales team](https://stripe.com/contact/sales)

## What you’ll build

If your integration uses [customer-configured Accounts](https://docs.stripe.com/api/v2/core/accounts/create.md#v2_create_accounts-configuration-customer), replace `Customer` and event references in the code examples with the equivalent Accounts v2 API references. For more information, see [Represent customers with Account objects](https://docs.stripe.com/connect/use-accounts-as-customers.md).

This guide shows you how to:

- Collect payment information with your own checkout page using [Elements](https://docs.stripe.com/payments/elements.md).

- Model your subscriptions with _Products_ (Products represent what your business sells—whether that's a good or a service), _Prices_ (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions), and _Customers_ (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments).

- Use _universal links_ (Use Universal links on iOS and macOS to link directly to in-app content. They're standard HTTPS links, so the same URL works for your website and your app) to redirect directly to your app from Checkout.

- Monitor _webhooks_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) to update your customer’s in-app subscriptions.

This guide only describes the process for selling in-app digital goods. If you sell any of the following, use the [native iOS payment guide](https://docs.stripe.com/payments/mobile.md) instead:

- Physical items
- Goods and services intended for consumption outside your app
- Real-time person-to-person services

## Set up Stripe [Server-side]

First, [register](https://dashboard.stripe.com/register) for a Stripe account.

Then add the Stripe API library to your backend:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

Next, install the Stripe CLI. The CLI provides the required [webhook](https://docs.stripe.com/webhooks.md#test-webhook) testing, and you can run it to create your products and prices.
For additional install options, see [Get started with the Stripe CLI](https://docs.stripe.com/stripe-cli.md).

## Create products and prices

Create your products and their prices in the Dashboard or with the Stripe CLI. This example uses a product and price to represent a subscription product with a 9.99 USD monthly price.

1. Navigate to the [Add a product](https://dashboard.stripe.com/test/products/create) page and create a subscription product with a 9.99 USD monthly price.

1. After you create the price, record the price ID so you can use it in subsequent steps. Price IDs look like this: `price_G0FvDp6vZvdwRZ`.

1. Next, click **Copy to live mode** to clone your product from a [testing environment to live mode](https://docs.stripe.com/keys.md#test-live-modes).

## Create customers [Server-side]

Each time your customer goes to your checkout page, create a Customer object for your customer if one doesn’t already exist.

Your server needs to handle:

- Customer creation (if a matching Stripe Customer doesn’t exist yet).
- Subscription creation in an `incomplete` state.
- Returning the PaymentIntent client secret to the front end.
- Webhook handling so you can update your customer’s subscription status in your own database.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

// This assumes your app has an existing user database, which we'll call `myUserDB`.
const user = myUserDB.getUser("jennyrosen");

if (!user.stripeCustomerID) {
  const customer = await stripe.customers.create({
    name: user.name,
    email: user.email,
  });

  // Set the user's Stripe Customer ID for later retrieval.
  user.stripeCustomerID = customer.id;
}
```

> Store an association on your server between the user account and the Stripe customer ID. Without a way to associate a customer with a purchase, your customers can’t recover their purchases.
>
> If the customer changes their email on the checkout page, the Customer object updates with the new email.

## Create a Subscription [Server-side]

When creating a subscription to use the Payment Element, you typically pass `payment_behavior: 'default_incomplete'`. This tells Stripe to create a subscription in `incomplete` status and generate a Payment Intent for the initial payment.

> Store the `subscription.id` in your database to manage future subscription events such as cancellation, upgrades, and downgrades.

#### Node.js

```javascript
// This example sets up an endpoint using the Express framework.

const express = require("express");
const app = express();
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

app.post("/create-subscription", async (req, res) => {
  const { priceId, customerId } = req.body;

  // Create the subscription
  // setting payment_behavior to "default_incomplete" ensures we get a Payment Intent
  // that we can confirm on the client using the Payment Element
  const subscription = await stripe.subscriptions.create({
    customer: customerId,
    items: [{ price: priceId }],
    payment_behavior: "default_incomplete",
    expand: ["latest_invoice.payment_intent"],
  });

  // Make sure you associate the subscription ID with the user in your database!
  myUserDB.addUserSubscription("jennyrosen", subscription.id);

  // Get the Payment Intent client secret
  const paymentIntent = subscription.latest_invoice.payment_intent;
  const clientSecret = paymentIntent.client_secret;

  return res.json({
    subscriptionId: subscription.id,
    clientSecret: clientSecret,
  });
});

app.post("/login", async (req, res) => {
  // This assumes your app has an existing user database, which we'll call `myUserDB`.
  const token = myUserDB.login(req.body.login_details);
  res.json({ token: token });
});

app.listen(4242, () => console.log(`Listening on port ${4242}!`));
```

> Apple Pay is [enabled by default](https://dashboard.stripe.com/settings/payment_methods) and automatically appears in the Payment Element when a customer uses a supported device and has saved at least one card in the Wallet app. You can accept additional payment methods using the `payment_method_types` property. See [payment methods overview](https://docs.stripe.com/payments/payment-methods/overview.md) for more details.

## Set up universal links

Universal links allow your checkout page to deeply link into your app. To configure a universal link:

- Add an `apple-app-site-association` file to your domain.
- Add an Associated Domains entitlement to your app.
- Add a fallback page for your checkout redirect URLs.

#### Define the associated domains

Add a file to your domain at `.well-known/apple-app-site-association` to define the URLs that your app handles. Prepend your App ID with your Team ID, which you can find on the [Membership page of the Apple Developer Portal](https://developer.apple.com/account).

```json
{
  "applinks": {
    "apps": [],
    "details": [
      {
        "appIDs": [
          "A28BC3DEF9.com.example.MyApp1",
          "A28BC3DEF9.com.example.MyApp1-Debug"
        ],
        "components": [
          {
            "/": "/checkout_redirect*",
            "comment": "Matches any URL whose path starts with /checkout_redirect"
          }
        ]
      }
    ]
  }
}
```

You must serve the file with MIME type `application/json`. Use `curl -I` to confirm the content type:

```bash
curl -I https://example.com/.well-known/apple-app-site-association
```

See Apple’s page on [supporting associated domains](https://developer.apple.com/documentation/xcode/supporting-associated-domains) for more details.

#### Add an Associated Domains entitlement to your app

1. Open the **Signing & Capabilities** pane of your app’s target.
1. Click **+ Capability**, then select **Associated Domains**.
1. Add an entry for `applinks:example.com` to the Associated Domains list.

For more information on universal links, see Apple’s [universal links](https://developer.apple.com/ios/universal-links/) documentation.

Although iOS intercepts links to the URLs defined in your `apple-app-site-association` file, you might encounter situations where the redirect fails to open your app.

Create a [fallback page](https://docs.stripe.com/payments/checkout/custom-success-page.md) at your `success` and `cancel` URLs. For example, you can have a `/checkout_redirect/success` page and a `/checkout_redirect/cancel` page.

## Open Checkout in Safari [Client-side]

Add a checkout button to your app. This button opens your custom checkout page in Safari.

```swift
import Foundation
import SwiftUI
import StoreKit

struct BuySubscriptionsView: View {
   @EnvironmentObject var myBackend: MyBackend
   @State var paymentComplete = false


   var body: some View {
       // Check if payments are blocked by Parental Controls on this device.
       if !SKPaymentQueue.canMakePayments() {
           Text("Payments are disabled on this device.")
       } else {
           if paymentComplete {
               Text("Payment complete!")
           } else {
               Button {
                   UIApplication.shared.open("https://example.com/checkout", options: [:], completionHandler: nil)
               } label: {
                   Text("Subscribe")
               }.onOpenURL { url in
                   // Handle the universal link from Checkout.
                   if url.absoluteString.contains("success") {
                       // The payment was completed. Show a success
                       // page and fetch the latest customer entitlements
                       // from your server.
                       paymentComplete = true
                   }
               }
           }
       }
   }
}
```

## Redirect back to your app [Server-side]

With Elements, make sure you [redirect](https://docs.stripe.com/js/payment_intents/confirm_payment#confirm_payment_intent-options-confirmParams-return_url) users back to your app (using the registered universal link) on a successful payment confirmation.

```javascript
stripe
  .confirmPayment({
    elements,
    confirmParams: {
      // Return URL where the customer should be redirected after the PaymentIntent is confirmed.
      return_url: "https://example.com/checkout_redirect/success",
    },
  })
  .then(function (result) {
    if (result.error) {
      // Inform the customer that there was an error.
    }
  });
```

## Handle order fulfillment [Server-side]

When the user completes the initial payment or when subsequent recurring payments occur, Stripe sends events such as:

- `invoice.payment_succeeded`
- `customer.subscription.updated`
- `invoice.payment_failed`

Listen for these events in your webhook endpoint. For example:

#### Node.js

```javascript
app.post("/webhook", express.raw({ type: "application/json" }), (req, res) => {
  const sig = req.headers["stripe-signature"];
  let event;

  try {
    event = stripe.webhooks.constructEvent(
      req.body,
      sig,
      process.env.STRIPE_WEBHOOK_SECRET,
    );
  } catch (err) {
    console.error("Webhook signature verification failed.", err.message);
    return res.sendStatus(400);
  }

  switch (event.type) {
    case "invoice.payment_succeeded": {
      const invoice = event.data.object;
      // Mark subscription as active in your database
      // For example, invoice.subscription -> "sub_abc123"
      console.log("Payment succeeded");
      break;
    }
    case "invoice.payment_failed": {
      const invoice = event.data.object;
      console.log(
        "Payment failed - notify the user to update their payment methods",
      );
      break;
    }
    case "customer.subscription.updated": {
      const subscription = event.data.object;
      // For example, handle pause, cancellation, or other changes
      console.log(`Subscription updated: ${subscription.id}`);
      break;
    }
    default:
      console.log(`Unhandled event type ${event.type}`);
  }
  res.json({ received: true });
});
```

To test your integration, you can monitor events in the [Dashboard](https://dashboard.stripe.com/events) or using the [Stripe CLI](https://docs.stripe.com/webhooks.md#test-webhook). When developing in production, set up a webhook endpoint and subscribe to appropriate event types. If you don’t know your `STRIPE_WEBHOOK_SECRET` key, click the [webhook](https://dashboard.stripe.com/webhooks) in the Dashboard to view it.

### Testing

To test your that your checkout button works, do the following:

1. Click the checkout button, which redirects you to your checkout with Stripe’s Payment Element.
1. Enter the test number 4242 4242 4242 4242, a three-digit CVC, a future expiration date, and any valid postal code.
1. Tap **Pay**.
1. The `invoice.payment_succeeded` webhook fires, and Stripe notifies your server about the transaction.
1. You’re redirected back to your app.

If your integration isn’t working, see [additional testing resources](https://docs.stripe.com/mobile/digital-goods/custom-checkout.md#additional-testing-resources).

## Optional: Additional testing resources

There are several test cards you can use to make sure your integration is ready for production. Use them with any CVC, postal code, and future expiration date.

| Number              | Description                                                   |
| ------------------- | ------------------------------------------------------------- |
| 4242 4242 4242 4242 | Succeeds and immediately processes the payment.               |
| 4000 0000 0000 3220 | Complete 3D Secure 2 authentication for a successful payment. |
| 4000 0000 0000 9995 | Always fails with a decline code of `insufficient_funds`.     |

For the full list of test cards see the [testing](https://docs.stripe.com/testing.md) guide.

### Test universal links

If your universal link doesn’t redirect from your checkout page to your app, check the `SharedWebCredentials` logs for errors.

1. Add a debug parameter to the Associated Domains entitlement
   1. Open the **Signing & Capabilities** pane of your app’s target.
   1. Add the `?mode=developer` flag to the entry for your associated domain. _(Example: `applinks:example.com?mode=developer`)_

1. Set the device to developer mode.
   1. Run an app from Xcode on your device to enable the developer menu.
   1. On your iPhone, open **Settings**, tap **Developer**, and enable **Associated Domains Development**.

1. Delete and reinstall your app. This causes iOS to re-fetch the apple-app-site-association file.

1. Complete the checkout flow in your app.

1. Checkout redirects you to your app. If it doesn’t, take a sysdiagnose.

1. Simultaneously press the volume up, volume down, and power buttons for 1 second, then release. You’ll feel a short vibration, but you won’t see any visual feedback.

1. Wait 5 minutes, then go to **Settings > Privacy > Analytics & Improvement > Analytics Data**, and scroll to the last sysdiagnose file in the list.

1. Tap the share button to AirDrop the file to your computer.

1. Open the sysdiagnose archive, then open `swcutil_show.txt`

1. Search this file for your app’s ID. You’ll see a section with debugging information for your app, including an error if available.

```
Service:              applinks
App ID:               Y28TH9SHX7.com.stripe.FruitStore
App Version:          1.0
App PI:               <LSPersistentIdentifier 0x115e1a390> { v = 0, t = 0x8, u = 0xc98, db = E335D78F-D49E-4F19-A150-F657E50DEDAE, {length = 8, bytes = 0x980c000000000000} }
Domain:               example.com?mode=developer
User Approval:        unspecified
Site/Fmwk Approval:   unspecified
Flags:                developer
Last Checked:         2021-09-23 18:16:58 +0000
Next Check:           2021-09-23 21:21:34 +0000
Error:                Error Domain=NSCocoaErrorDomain Code=3840 "JSON text did not start with array or object and option to allow fragments not set. around line 1, column 0." UserInfo={NSDebugDescription=JSON text did not start with array or object and option to allow fragments not set. around line 1, column 0., NSJSONSerializationErrorIndex=0}
Retries:              1
```

## See also

- [Add discounts](https://docs.stripe.com/payments/checkout/discounts.md)
- [Collect taxes](https://docs.stripe.com/payments/checkout/taxes.md)
- [Collect tax IDs](https://docs.stripe.com/tax/checkout/tax-ids.md)
- [Customize your branding](https://docs.stripe.com/payments/checkout/customization.md)
- [Customize your success page](https://docs.stripe.com/payments/checkout/custom-success-page.md)
