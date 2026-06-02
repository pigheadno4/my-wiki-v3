<!-- Source URL: https://docs.stripe.com/mobile/digital-goods/checkout -->
<!-- Fetched: 2026-04-22 -->

# Accept payments for digital goods on iOS with a prebuilt payment page

Open Stripe Checkout in a browser to sell in-app digital goods or subscriptions.

> [Learn how to build a similar integration that uses Managed Payments](https://docs.stripe.com/payments/managed-payments/set-up-mobile.md), Stripe’s _merchant of record_ (The legal entity responsible for facilitating the sale of products to a customer that handles any applicable regulations and liabilities, including sales taxes. In a Connect integration, it can be the platform or a connected account) solution.

For iOS apps selling digital products, content, and subscriptions in the US, you can redirect customers to an external payment page to accept payments using [Stripe Checkout](https://docs.stripe.com/payments/checkout.md). Use [StoreKit’s Storefront](https://developer.apple.com/documentation/storekit/storefront) property to detect which storefront your app was downloaded from. This guide describes how to accept payments for purchasing credits in your iOS app by redirecting customers to a [Stripe-hosted payment page](https://docs.stripe.com/checkout/quickstart.md).

For Android developers in the US, you can process payments directly in-app with a third party payment processor. To accept payments directly in-app with Stripe, see [In-app payments](https://docs.stripe.com/payments/mobile.md).

This guide only describes the process for iOS developers selling in-app digital goods. Use the [native app payment guide](https://docs.stripe.com/payments/mobile.md) if you sell:

- Physical items
- Goods and services intended for consumption outside your app
- Real-time person-to-person services between two individuals

This guide shows you how to:

- Collect payment information with Checkout.
- Model your credit packages with _Products_ (Products represent what your business sells—whether that's a good or a service), _Prices_ (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions), and _Customers_ (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments).
- Use _Universal Links_ (Use Universal links on iOS and macOS to link directly to in-app content. They're standard HTTPS links, so the same URL works for your website and your app) to redirect directly to your app from Checkout.
- Monitor _webhooks_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) to update your customer’s in-app currency balance.
  ![One-time payment](assets/stripe-inapp-digital-goods-one-time-payment.png)

Link out of app for one-time payments
![Recurring payment](assets/stripe-inapp-digital-goods-recurring-payment.png)

Link out of app for recurring or subscription payments

## How it works

The following diagram shows the full app-to-web payment flow at a high level:
High-level app-to-web checkout flow for in-app purchases (See full diagram at https://docs.stripe.com/mobile/digital-goods/checkout)

## What isn’t covered

This guide demonstrates how to add Stripe Checkout alongside your existing in-app purchase system. It doesn’t cover:

- User authentication. If you don’t have an existing authentication provider, you can use a third-party provider, such as [Sign in with Apple](https://developer.apple.com/sign-in-with-apple/) or [Firebase Authentication](https://firebase.google.com/docs/auth).
- Native in-app purchases. To implement in-app purchases using StoreKit, visit [Apple’s in-app purchase guide](https://developer.apple.com/in-app-purchase/).

## Set up Stripe [Server-side]

First, [register](https://dashboard.stripe.com/register) for a Stripe account.

Then add the Stripe API library to your backend:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

Next, install the Stripe CLI. The CLI provides the [webhook](https://docs.stripe.com/webhooks.md#test-webhook) testing you’ll need, and you can run it to create your products and prices.
For additional install options, see [Get started with the Stripe CLI](https://docs.stripe.com/stripe-cli.md).

## Create products and prices

Create your _products_ (Products represent items your customer can subscribe to with a Subscription. An associated Price object describes the pricing and other terms of the subscription) and their _prices_ (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) in the Dashboard or with the Stripe CLI. You can model digital goods using one-off prices and subscriptions using recurring prices. You can also let your customer pay what they want (for example, to decide how many credits to buy), by selecting **Customers choose what to pay**.

This example uses a single _product_ and _price_ to represent a 100 coin bundle.

#### Dashboard

Navigate to the [Add a product](https://dashboard.stripe.com/test/products/create) page and create the coin bundle. Add a one-time price of 10 USD.

- 100 coins: Bundle of 100 in-app coins
  - Price: Standard model | 10 USD | One time

After you create the price, record the price ID so you can use it in subsequent steps. Price IDs look like this: `price_G0FvDp6vZvdwRZ`.

When you’re ready, use the **Copy to live mode** button at the top right of the page to clone your product from a [testing environment to live mode](https://docs.stripe.com/keys.md#test-live-modes).

#### Stripe CLI

Next create the product objects:

```bash
stripe products create \
  --name="100 coins" \
  --description="Bundle of 100 in-app coins"
```

The Stripe CLI returns the product details, including the product ID.

```json
{
  "id": "prod_H94k5odtwJXMtQ",
  "object": "product",
  "active": true,
  "attributes": [],
  "created": 1587577341,
  "description": "Bundle of 100 in-app coins",
  "images": [],
  "livemode": false,
  "metadata": {},
  "name": "100 coins",
  "statement_descriptor": null,
  "type": "service",
  "unit_label": null,
  "updated": 1587577341
}
```

Use the product ID to create a price. The `unit_amount` number is in cents, so `1000` = 10 USD, for example.

```bash
  stripe prices create \
    -d product=prod_H94k5odtwJXMtQ \
    -d unit_amount=1000 \
    -d currency=usd
```

Record the price ID for each price so you can use them in subsequent steps. They look like this:

```json
{
  "id": "price_1Jh0tjEmNk5jCjFGCkLnNYGO",
  "object": "price",
  "active": true,
  "billing_scheme": "per_unit",
  "created": 1633391323,
  "currency": "usd",
  "livemode": false,
  "lookup_key": null,
  "metadata": {},
  "nickname": null,
  "product": "prod_H94k5odtwJXMtQ",
  "recurring": null,
  "tax_behavior": "unspecified",
  "tiers_mode": null,
  "transform_quantity": null,
  "type": "one_time",
  "unit_amount": 1000,
  "unit_amount_decimal": "1000"
}
```

## Create customers [Server-side]

Each time you create a Checkout session, create a _Customer_ (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) object for your user if one doesn’t already exist.

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

> Make sure to store an association on your server between the user account and the Stripe customer ID. Without a way to associate a customer with a purchase, your customers can’t recover their purchases.
>
> If your app doesn’t have an existing authentication provider, you can use [Sign in with Apple](https://developer.apple.com/sign-in-with-apple/).

You can [save payment method details](https://docs.stripe.com/payments/save-during-payment.md?platform=checkout) to have Checkout automatically attach the payment method to the Customer for future reuse.

## Set up universal links [Client-side] [Server-side]

_Universal links_ (Use Universal links on iOS and macOS to link directly to in-app content. They're standard HTTPS links, so the same URL works for your website and your app) allow Checkout to deep link into your app. To configure a universal link:

1. Add an `apple-app-site-association` file to your domain.
1. Add an Associated Domains entitlement to your app.
1. Add a fallback page for your Checkout redirect URLs.

#### Define the associated domains

Add a file to your domain at **.well-known/apple-app-site-association** to define the URLs your app handles. Prepend your App ID with your Team ID, which you can find on the [Membership page of the Apple Developer Portal](https://developer.apple.com/account).

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

You must serve the file with MIME type `application/json`. Use `curl -I` to confirm the content type.

```bash
curl -I https://example.com/.well-known/apple-app-site-association
```

See Apple’s page on [supporting associated domains](https://developer.apple.com/documentation/xcode/supporting-associated-domains) for more details.

#### Add an Associated Domains entitlement to your app

1. Open the **Signing & Capabilities** pane of your app’s target.
1. Click **+ Capability**, then select **Associated Domains**.
1. Add an entry for `applinks:example.com` to the **Associated Domains** list.

For more information on universal links, see Apple’s [Universal Links for Developers](https://developer.apple.com/ios/universal-links/) page.

Although iOS intercepts links to the URLs defined in your `apple-app-site-association` file, you might encounter situations where the redirect fails to open your app.

Make sure to create a [fallback page](https://docs.stripe.com/payments/checkout/custom-success-page.md?payment-ui=stripe-hosted) at your `success_url`. For example, you can [define a custom URL scheme for your app](https://developer.apple.com/documentation/xcode/defining-a-custom-url-scheme-for-your-app) and use it to link back in case the universal link fails.

## Create a Checkout session [Server-side]

A [Checkout Session](https://docs.stripe.com/api/checkout/sessions/create.md) is the programmatic representation of what your customer sees when they’re redirected to the payment form. Checkout Sessions expire 24 hours after creation. Configure it with:

- The customer ID
- The product ID (either a one time payment or subscription)
- An `origin_context` set to `mobile_app` to opt in to a UI that is optimized for app-to-web purchases.
- A `success_url`, a _universal link_ (Use Universal links on iOS and macOS to link directly to in-app content. They're standard HTTPS links, so the same URL works for your website and your app) to redirect your customer to your app after they complete the payment.

> Create the Checkout Session with `origin_context: "mobile_app"` to opt in to a UI that is optimized for app-to-web purchases.

After creating a Checkout Session, return the [URL](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-url) from the response to your app.

#### One time payment

#### Node.js

```javascript
// This example sets up an endpoint using the Express framework.

const express = require("express");
const app = express();
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

app.post("/create-checkout-session", async (req, res) => {
  // Fetch the Stripe customer ID for the customer associated with this request.
  // This assumes your app has an existing user database, which we'll call `myUserDB`.
  const user = myUserDB.getUserFromToken(req.query.token);
  const customerId = user.stripeCustomerID;

  // The price ID from the previous step
  const priceId = "{{PRICE_ID}}";
  const session = await stripe.checkout.sessions.create({
    line_items: [
      {
        price: priceId,
        quantity: 1,
      },
    ],
    mode: "payment",
    origin_context: "mobile_app",
    customer: customerId,
    success_url: "https://example.com/checkout_redirect/success",
  });

  res.json({ url: session.url });
});

app.post("/login", async (req, res) => {
  // This assumes your app has an existing user database, which we'll call `myUserDB`.
  const token = myUserDB.login(req.body.login_details);
  res.json({ token: token });
});

app.listen(4242, () => console.log(`Listening on port ${4242}!`));
```

#### Subscription

#### Node.js

```javascript
// This example sets up an endpoint using the Express framework.

const express = require("express");
const app = express();
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

app.post("/create-checkout-session", async (req, res) => {
  // Fetch the Stripe customer ID for the customer associated with this request.
  // This assumes your app has an existing user database, which we'll call `myUserDB`.
  const user = myUserDB.getUserFromToken(req.query.token);
  const customerId = user.stripeCustomerID;

  // The price ID from the previous step
  const priceId = "{{SUBSCRIPTION_PRICE_ID}}";

  const session = await stripe.checkout.sessions.create({
    line_items: [
      {
        price: priceId,
        quantity: 1,
      },
    ],
    mode: "subscription",
    origin_context: "mobile_app",
    customer: customerId,
    success_url: "https://example.com/checkout_redirect/success",
  });

  res.json({ url: session.url });
});

app.post("/login", async (req, res) => {
  // This assumes your app has an existing user database, which we'll call `myUserDB`.
  const token = myUserDB.login(req.body.login_details);
  res.json({ token: token });
});

app.listen(4242, () => console.log(`Listening on port ${4242}!`));
```

> [Apple Pay is enabled by default](https://dashboard.stripe.com/settings/checkout) and automatically appears in Checkout when a customer uses a supported device. You can accept additional payment methods by using [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md).

## Open Checkout in Safari [Client-side]

Add a checkout button to your app. This button:

1. Calls your server-side endpoint to create a Checkout session.
1. Returns the Checkout session to the client.
1. Opens the session URL in Safari.

```swift
import Foundation
import SwiftUI
import StoreKit

struct BuyCoinsView: View {
    @EnvironmentObject var myBackend: MyServer
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
                    myBackend.createCheckoutSession { url in
                        UIApplication.shared.open(url, options: [:], completionHandler: nil)
                    }
                } label: {
                    Text("Buy 100 coins")
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

### Fetch the Checkout URL on the client

Use your server endpoint to fetch the checkout session.

```swift
class MyServer: ObservableObject {
  // The cached login token
  var token: String?
func createCheckoutSession(completion: @escaping (URL) -> Void) {
    // Send the login token to the `/create_checkout_session` endpoint
    let request = URLRequest(url: URL(string: "https://example.com/create-checkout-session?token=\(self.token)")!)

    let task = URLSession.shared.dataTask(with: request, completionHandler: { (data, response, error) in
      guard let unwrappedData = data,
            let json = try? JSONSerialization.jsonObject(with: unwrappedData, options: []) as? [String : Any],
            let urlString = json["url"] as? String,
            let url = URL(string: urlString) else {
        // Handle error
        return
      }

      DispatchQueue.main.async {
        // Call the completion block with the Checkout session URL returned from the backend
        completion(url)
      }
    })
    task.resume()
  }

  func login() {
    // Login using the server and set the login token.
    let request = URLRequest(url: URL(string: "https://example.com/login")!)

    let task = URLSession.shared.dataTask(with: request, completionHandler: { (data, response, error) in
      guard let unwrappedData = data,
            let json = try? JSONSerialization.jsonObject(with: unwrappedData, options: []) as? [String : Any],
            let token = json["token"] as? String else {
        // Handle error
        return
      }
      self.token = token
    })
    task.resume()
  }
}
```

## Handle order fulfillment [Server-side]

After the purchase succeeds, Stripe sends you a `checkout.session.completed` _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests). When you receive this event, you can add the coins to the customer on your server.

Checkout redirects your customer to the `success_url` when you [acknowledge you received the event](https://docs.stripe.com/webhooks.md#acknowledge-events-immediately). In scenarios where your endpoint is down or the event isn’t acknowledged properly, Checkout redirects the customer to the `success_url` 10 seconds after a successful payment.

For testing purposes, you can monitor events in the [Dashboard](https://dashboard.stripe.com/events) or using the [Stripe CLI](https://docs.stripe.com/webhooks.md#test-webhook). For production, set up a webhook endpoint and subscribe to appropriate event types. If you don’t know your `STRIPE_WEBHOOK_SECRET` key, click the [webhook](https://dashboard.stripe.com/webhooks) in the Dashboard to view it.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

app.post("/webhook", async (req, res) => {
  let data;
  let eventType;
  // Check if webhook signing is configured.
  const webhookSecret = "{{STRIPE_WEBHOOK_SECRET}}"; // Example: whsec_c7681Dm
  if (webhookSecret) {
    // Retrieve the event by verifying the signature using the raw body and secret.
    let event;
    let signature = req.headers["stripe-signature"];

    try {
      event = stripe.webhooks.constructEvent(
        req.body,
        signature,
        webhookSecret,
      );
    } catch (err) {
      console.log(`⚠️  Webhook signature verification failed.`);
      return res.sendStatus(400);
    }
    // Extract the object from the event.
    data = event.data;
    eventType = event.type;
  } else {
    // Webhook signing is recommended, but if the secret is not configured in `config.js`,
    // retrieve the event data directly from the request body.
    data = req.body.data;
    eventType = req.body.type;
  }

  switch (eventType) {
    case "checkout.session.completed":
      const session = event.data.object;
      // Payment is successful.
      // Update the customer in your database to reflect this purchase.
      const user = myUserDB.userForStripeCustomerID(session.customer);
      user.addCoinsTransaction(100, session.id);
      break;
    default:
    // Unhandled event type
  }

  res.sendStatus(200);
});
```

### Testing

Test your checkout button that redirects your customer to Stripe Checkout.

1. Click the checkout button, which redirects you to the Stripe Checkout payment form.
1. Enter the test number 4242 4242 4242 4242, a three-digit CVC, a future expiration date, and any valid postal code.
1. Tap **Pay**.
1. The `checkout.session.completed` webhook fires, and Stripe notifies your server about the transaction.
1. You’re redirected back to your app.

If your integration isn’t working, see the [additional testing resources](https://docs.stripe.com/mobile/digital-goods/checkout.md#additional-testing-resources) section below.

## Optional: Additional testing resources

There are several test cards you can use to make sure your integration is ready for production. Use them with any CVC, postal code, and future expiration date.

| Number              | Description                                                   |
| ------------------- | ------------------------------------------------------------- |
| 4242 4242 4242 4242 | Succeeds and immediately processes the payment.               |
| 4000 0000 0000 3220 | Complete 3D Secure 2 authentication for a successful payment. |
| 4000 0000 0000 9995 | Always fails with a decline code of `insufficient_funds`.     |

For the full list of test cards see the [testing](https://docs.stripe.com/testing.md) guide.

### Testing universal links

If your universal link doesn’t redirect from Checkout to your app, check the `SharedWebCredentials` logs for errors.

1. Add a debug parameter to the Associated Domains entitlement
   - Open the **Signing & Capabilities** pane of your app’s target.
   - Add the `?mode=developer` flag to the entry for your associated domain. _(Example: `applinks:example.com?mode=developer`)_

1. Set the device to developer mode.
   - Run an app from Xcode on your device to enable the developer menu.
   - On your iPhone, open **Settings**, tap **Developer**, and enable **Associated Domains Development**.

1. Delete and reinstall your app. This causes iOS to re-fetch the apple-app-site-association file.

1. Complete the checkout flow in your app.

1. Checkout redirects you to your app. If it doesn’t, take a sysdiagnose.

1. Simultaneously press the volume up, volume down, and power buttons for 1 second, then release. You’ll feel a short vibration, but you won’t see any visual feedback.

1. Wait 5 minutes, then go to **Settings** > **Privacy** > **Analytics & Improvement** > **Analytics Data**, and scroll to the last sysdiagnose file in the list.

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

## Optional: In-app purchases with Managed Payments

Accept payments with Managed Payments, which can handle many business functions (such as tax and disputes) on your behalf. Learn more about [how to use Managed Payments](https://docs.stripe.com/payments/managed-payments/set-up-mobile.md), Stripe’s merchant of record solution, for in-app purchases.

## See also

- [Add discounts](https://docs.stripe.com/payments/checkout/discounts.md)
- [Collect taxes](https://docs.stripe.com/payments/checkout/taxes.md)
- [Collect tax IDs](https://docs.stripe.com/tax/checkout/tax-ids.md)
- [Customize your branding](https://docs.stripe.com/payments/checkout/customization.md)
- [Customize your success page](https://docs.stripe.com/payments/checkout/custom-success-page.md)
