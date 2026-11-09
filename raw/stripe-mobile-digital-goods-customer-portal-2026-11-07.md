<!-- Source URL: https://docs.stripe.com/mobile/digital-goods/customer-portal -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Provide subscription management on iOS with a customer portal page

Set up a customer portal and open it in a browser from your app.

For digital products and content, including subscriptions, sold in the United States or European Economic Area (EEA), your app can accept Apple Pay by redirecting to an external payment page.

This guide describes how to configure a [customer portal](https://docs.stripe.com/customer-management.md) for subscription management and redirect your customers to it from your app.
![One-time payment](https://b.stripecdn.com/docs-statics-srv/assets/subscriptions_hero.647ac1dba5270dbf75e15c456c6bcf0d.png)

Link out of app to manage subscriptions and payment methods

## What you’ll build 

> This guide only describes subscription management. If you’re setting up subscription purchases, see [Accept payments for digital goods on iOS with a prebuilt payment page](https://docs.stripe.com/mobile/digital-goods/checkout.md).

This guide shows you how to:

- Set up a customer portal page that customers can use to manage subscriptions
- Use *universal links* (Use Universal links on iOS and macOS to link directly to in-app content. They're standard HTTPS links, so the same URL works for your website and your app) to redirect users back to your app from the customer portal
- Monitor *webhooks* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) to update your customer’s subscription status

## What isn’t covered 

This guide demonstrates how to set up a Stripe [customer portal](https://docs.stripe.com/customer-management.md) and link to it from your app. It doesn’t cover:

- **Subscription purchases**: To use Stripe Checkout to sell in-app goods and subscriptions, see [Accept payments for digital goods on iOS with a prebuilt payment page](https://docs.stripe.com/mobile/digital-goods/checkout.md).
- **User authentication**: If you don’t have an existing authentication provider, you can use a third-party provider, such as [Sign in with Apple](https://developer.apple.com/sign-in-with-apple/) or [Firebase Authentication](https://firebase.google.com/docs/auth).
- **Native in-app purchases**: To implement in-app purchases using StoreKit, visit [Apple’s in-app purchase guide](https://developer.apple.com/in-app-purchase/).

## Configure the portal

First, you need to [register for a Stripe account](https://dashboard.stripe.com/register/).

Before you integrate the customer portal, use the Dashboard to choose which actions customers can take. Configure the portal separately for *sandboxes* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes) and live mode based on your product and price catalog.

> If you use the customer portal with Stripe Connect, configure it for your platform, not a connected account.

To use different portal settings for different groups of customers, or to manage configurations for connected accounts as a *Connect* (Connect is Stripe's solution for multi-party businesses, such as marketplace or software platforms, to route payments between sellers, customers, and other recipients) platform, [create portal configurations with the API](https://docs.stripe.com/api/customer_portal/configurations/create.md):

```curl
curl https://api.stripe.com/v1/billing_portal/configurations \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "features[invoice_history][enabled]=true"
```

### Set a product catalog 

If customers can upgrade, downgrade, or change subscription quantities, you must configure a product catalog. Specify the products and prices they can switch to and the subscription items whose quantities they can change. To learn more, see [Create a product](https://docs.stripe.com/products-prices/manage-prices.md#create-product).

You don’t need to configure a product catalog if you use the customer portal only for invoicing.

The portal displays the following attributes of your product catalog:

- **Product name and description**: Editable attributes in the Dashboard and API.
- **Quantity restrictions per product**: Editable attributes in the Dashboard.
- **Price amount, currency, and billing interval**: Fixed attributes. You can only set them when you create them in the Dashboard and API.

### Enable tax ID collection 

If you use [Stripe Tax](https://docs.stripe.com/tax.md) to automatically collect taxes for subscriptions or invoices, you can let customers set and update their tax IDs in the customer portal. Stripe Billing adds the tax IDs to the customers’ *invoices* (Invoices are statements of amounts owed by a customer. They track the status of payments from draft through paid or otherwise finalized. Subscriptions automatically generate invoices, or you can manually create a one-off invoice). To allow customers to set their tax IDs, go to the [Customer portal settings](https://dashboard.stripe.com/settings/billing/portal) and toggle on **Tax ID**. For more information, see how customer tax IDs work with [subscriptions](https://docs.stripe.com/billing/customer/tax-ids.md) and [invoices](https://docs.stripe.com/invoicing/taxes/account-tax-ids.md).

To learn more, see [Set up Stripe Tax](https://docs.stripe.com/tax/set-up.md) and [Collect taxes for recurring payments](https://docs.stripe.com/billing/taxes/collect-taxes.md).

### Preview and test 

While you configure the portal, click **Preview** to open a read-only view and see how customers can manage their subscriptions and billing details.

After you save your settings, test the portal with a sandbox customer:

1. In the Dashboard, open the customer’s details page.
2. Click **Actions**.
3. Click **Open customer portal**.

You can preview and test the portal only in a sandbox, and you need Dashboard edit permissions. If these options aren’t available, confirm that you’re viewing a sandbox, saved the configuration in that sandbox, and have the required permissions.

## Set up Stripe [Server-side]

### Server-side 

#### Ruby

```bash
# Available as a gem
sudo gem install stripe
```

```ruby
# If you use bundler, you can add this line to your Gemfile
gem 'stripe'
```

Next, install the Stripe CLI. The CLI provides the [webhook](https://docs.stripe.com/webhooks.md#test-webhook) testing that you need.

Install the Stripe CLI with [npm](https://www.npmjs.com/):

```bash
npm install -g @stripe/cli@latest
```

After installation, log in to your Stripe account:

```bash
stripe login
```

After you install the CLI, you can also install [agent tooling](https://docs.stripe.com/cli/agent/setup), or set up [autocompletion](https://docs.stripe.com/cli/completion).

> For more installation options for Windows, macOS, Linux, and Docker, see the [Stripe CLI readme](https://github.com/stripe/stripe-cli#installation) on GitHub.

### Client-side 

The [Stripe iOS SDK](https://github.com/stripe/stripe-ios) is open source, [fully documented](https://stripe.dev/stripe-ios/index.html), and compatible with apps supporting iOS 13 or above.

#### Swift Package Manager

To install the SDK, follow these steps:

1. In Xcode, select **File** > **Add Package Dependencies…** and enter `https://github.com/stripe/stripe-ios-spm` as the repository URL.
2. Select the latest version number from our [releases page](https://github.com/stripe/stripe-ios/releases).
3. Add the **StripePaymentSheet** product to the [target of your app](https://developer.apple.com/documentation/swift_packages/adding_package_dependencies_to_your_app).

#### Carthage

1. If you haven’t already, install the latest version of [Carthage](https://github.com/Carthage/Carthage#installing-carthage).
2. Add this line to your `Cartfile`:
   ```cartfile
   github "stripe/stripe-ios"
   ```
3. Follow the [Carthage installation instructions](https://github.com/Carthage/Carthage#if-youre-building-for-ios-tvos-or-watchos). Make sure to embed all of the required frameworks listed [here](https://github.com/stripe/stripe-ios/tree/master/StripePaymentSheet/README.md#manual-linking).
4. In the future, to update to the latest version of the SDK, run the following command:
   ```bash
   carthage update stripe-ios --platform ios
   ```

#### Manual Framework

1. Head to our [GitHub releases page](https://github.com/stripe/stripe-ios/releases/latest) and download and unzip **Stripe.xcframework.zip**.
2. Drag **StripePaymentSheet.xcframework** to the **Embedded Binaries** section of the **General** settings in your Xcode project. Make sure to select **Copy items if needed**.
3. Repeat step 2 for all required frameworks listed [here](https://github.com/stripe/stripe-ios/tree/master/StripePaymentSheet/README.md#manual-linking).
4. In the future, to update to the latest version of our SDK, repeat steps 1–3.

> For details on the latest SDK release and past versions, see the [Releases](https://github.com/stripe/stripe-ios/releases) page on GitHub. To receive notifications when a new release is published, [watch releases](https://help.github.com/en/articles/watching-and-unwatching-releases-for-a-repository#watching-releases-for-a-repository) for the repository.

You also need to set your [publishable key](https://dashboard.stripe.com/apikeys) so that the SDK can make API calls to Stripe. To get started quickly, you can hardcode this on the client while you’re integrating, but fetch the publishable key from your server in production.

```swift
// Set your publishable key: remember to change this to your live publishable key in production
// See your keys here: https://dashboard.stripe.com/apikeys
STPAPIClient.shared.publishableKey = "<<YOUR_PUBLISHABLE_KEY>>"
```

## Create a portal session [Server-side]

When a customer wants to make changes to their subscription, generate a URL for the portal page using their Stripe customer ID through the portal session API.

#### Node.js

```javascript

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

app.get('/customer_portal_url', async (req, res) => {

  // Replace this with your actual customer lookup logic
  const customerId = 'cus_...'; // Get this from your database

  const billingSession = await stripe.billingPortal.sessions.create({
    customer: customerId,
    return_url: 'https://example.com/portal_redirect',
  });

  res.json({
    url: billingSession.url
  });
})

```

## Set up universal links [Client-side] [Server-side]

*Universal links* (Use Universal links on iOS and macOS to link directly to in-app content. They're standard HTTPS links, so the same URL works for your website and your app) allow the customer portal to deep link into your app. To configure a universal link:

1. Add an `apple-app-site-association` file to your domain.
2. Add an Associated Domains entitlement to your app.
3. Add a fallback page for your portal redirect URLs.

#### Define the associated domains

Add a file to your domain at **.well-known/apple-app-site-association** to define the URLs your app handles. Prepend your App ID with your Team ID, which you can find on the [Membership page of the Apple Developer Portal](https://developer.apple.com/account).

```json

{
  "applinks": {

      "apps": [],
      "details": [
           {
             "appIDs": [ "A28BC3DEF9.com.example.MyApp1",
                         "A28BC3DEF9.com.example.MyApp1-Debug" ],
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
2. Click **+ Capability**, then select **Associated Domains**.
3. Add an entry for `applinks:example.com` to the **Associated Domains** list.

For more information on universal links, see Apple’s [Universal Links for Developers](https://developer.apple.com/ios/universal-links/) page.

Although iOS intercepts links to the URLs defined in your `apple-app-site-association` file, you might encounter situations where the redirect fails to open your app.

Make sure to create a fallback page at your `return_url`. For example, you can [define a custom URL scheme for your app](https://developer.apple.com/documentation/xcode/defining-a-custom-url-scheme-for-your-app) and use it to link back in case the universal link fails.

## Open the customer portal in Safari [Client-side]

Add a button to open the customer portal in your app. This button:

1. Calls your server-side endpoint to create a portal session.
2. Returns the portal page URL to the client.
3. Opens the URL in Safari.

```swift
import Foundation
import SwiftUI
import StoreKit

struct SubscriptionManagementView: View {

    @EnvironmentObject var myBackend: MyServer

    var body: some View {
        // Check if payments are blocked by Parental Controls on this device.
        if !SKPaymentQueue.canMakePayments() {
            Text("Payments are disabled on this device.")
        } else {
            Button {
                myBackend.createCustomerPortalSession { url in
                    UIApplication.shared.open(url, options: [:], completionHandler: nil)
                }
            } label: {
                Text("Manage subscriptions")
            }.onOpenURL { url in
                // Handle the universal link from the customer portal.
                // Implement any necessary behavior, such as refreshing the customer's subscription status.
            }
        }
    }
}
```

## Handle changes to customer subscription status [Server-side]

When customers make changes to their subscription status through the customer portal, Stripe sends you *webhooks* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), such as `customer.subscription.created`, `customer.subscription.deleted`, and `customer.subscription.updated`. For a full list of events and information about them, see [Using webhooks with subscriptions](https://docs.stripe.com/billing/subscriptions/webhooks.md). Make sure you handle all events necessary to accurately monitor the statuses of the subscriptions you’ve configured.

For testing purposes, you can monitor events in the [Dashboard](https://dashboard.stripe.com/events) or using the [Stripe CLI](https://docs.stripe.com/webhooks.md#test-webhook). For production, set up a webhook endpoint and subscribe to appropriate event types. If you don’t know your `STRIPE_WEBHOOK_SECRET` key, click the [webhook](https://dashboard.stripe.com/webhooks) link in the Dashboard to view it.

#### Node.js

```javascript
const express = require('express');
const app = express();
// Set your Stripe API key. Don't put any keys in code.
// See https://docs.stripe.com/keys-best-practices.
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY)

app.post('/webhook', async (req, res) => {
  let data;
  let eventType;
  // Check if webhook signing is configured.
  const webhookSecret = "{{STRIPE_WEBHOOK_SECRET}}" // Example: whsec_c7681Dm
  if (webhookSecret) {
    // Retrieve the event by verifying the signature using the raw body and secret.
    let event;
    let signature = req.headers["stripe-signature"];

    try {
      event = stripe.webhooks.constructEvent(
        req.body,
        signature,
        webhookSecret
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
    case 'customer.subscription.created': {
      const subscription = event.data.object;
      const customerId = subscription.customer;
      myUserDB.setUserSubscriptionIsActive(customerId, true);
      break;
    }
    case 'customer.subscription.deleted': {
      const subscription = event.data.object;
      const customerId = subscription.customer;
      myUserDB.setUserSubscriptionIsActive(customerId, false);
      break;
    }
    // Add other relevant event types as needed
  }

  res.sendStatus(200); // Acknowledge receipt of the webhook
})
```

## Optional: Deep link to specific pages

You might want to further customize workflows between your own app and Stripe. Customer portal deep links allow you to link directly to a page with the specified action to complete, and to customize the redirect behavior after the customer completes the action. Learn more about using [customer portal deep links](https://docs.stripe.com/customer-management/portal-deep-links.md).

## See also

- [Customer self-service with a customer portal](https://docs.stripe.com/customer-management.md)
- [Subscription lifecycle](https://docs.stripe.com/billing/subscriptions/overview.md#subscription-lifecycle)
- [Testing subscriptions](https://docs.stripe.com/billing/testing.md)
