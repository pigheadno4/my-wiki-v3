<!-- Source URL: https://docs.stripe.com/payments/p24/accept-a-payment -->
<!-- Fetched: 2026-05-03 -->

# Accept a Przelewy24 payment

Learn how to accept Przelewy24 (P24), a popular payment method in Poland.

# Checkout

> This is a Checkout for when payment-ui is checkout. View the full page at https://docs.stripe.com/payments/p24/accept-a-payment?payment-ui=checkout.

> Stripe can automatically present the relevant payment methods to your customers by evaluating currency, payment method restrictions, and other parameters.
>
> - Follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=checkout&ui=stripe-hosted) guide to build a Checkout integration that uses [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md).

- If you don’t want to use dynamic payment methods, follow the steps below to manually configure the payment methods in your Checkout integration.

[Przelewy24](https://www.przelewy24.pl) is a [single-use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method where customers are required to [authenticate](https://docs.stripe.com/payments/payment-methods.md#customer-actions) their payment. Customers pay with Przelewy24 by redirecting from your website, authorizing the payment, then returning to your website where you get [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) on whether the payment succeeded or failed.

## Determine compatibility

**Supported business locations**: Europe, US, CA, NZ, SG, HK, JP, AU, MX

**Supported currencies**: `eur, pln`

**Presentment currencies**: `eur, pln`

**Payment mode**: Yes

**Setup mode**: No

**Subscription mode**: No

A Checkout Session must satisfy all of the following conditions to support Przelewy24 payments:

- *Prices* (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) for all line items must be in the same currency. If you have line items in different currencies, create separate Checkout Sessions for each currency.
- You can only use one-time line items (recurring *subscription* (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) plans aren’t supported).

## Accept a payment

> This guide builds on the foundational [accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?ui=stripe-hosted) Checkout integration.

This guides you through enabling Przelewy24 and shows the differences between accepting payments using dynamic payment methods and manually configuring payment methods.

### Enable Przelewy24 as a payment method

When creating a new [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md), you need to:

1. Add `p24` to the list of `payment_method_types`.
1. Make sure all your `line_items` use the `eur` currency.

#### Stripe-hosted page

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        currency: "eur",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "p24"],
  success_url: "https://example.com/success",
});
```

#### Full embedded page

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        currency: "eur",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "p24"],
  return_url: "https://example.com/return",
  ui_mode: "embedded_page",
});
```

### Fulfill your orders

After accepting a payment, learn how to [fulfill orders](https://docs.stripe.com/checkout/fulfillment.md).

## Test your integration

When testing your Checkout integration, select Przelewy24 as the payment method and click the **Pay** button.

## Handle refunds and disputes

The refund period for Przelewy24 is up to 180 days after the original payment.

There is no dispute process—customers authenticate with their bank.

## See also

- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment.md)
- [Customizing Checkout](https://docs.stripe.com/payments/checkout/customization.md)

# iOS

> This is a iOS for when payment-ui is mobile and platform is ios. View the full page at https://docs.stripe.com/payments/p24/accept-a-payment?payment-ui=mobile&platform=ios.

> We recommend that you follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md) guide unless you need to use manual server-side confirmation, or your integration requires presenting payment methods separately. If you’ve already integrated with Elements, see the [Payment Element migration guide](https://docs.stripe.com/payments/payment-element/migration.md).

[Przelewy24](https://www.przelewy24.pl) is a [single-use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method where customers are required to [authenticate](https://docs.stripe.com/payments/payment-methods.md#customer-actions) their payment. Customers pay with Przelewy24 by redirecting from your website, authorizing the payment, then returning to your website where you get [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) on whether the payment succeeded or failed.

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

## Create a PaymentIntent [Server-side] [Client-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) represents your intent to collect payment from a customer and tracks the lifecycle of the payment process.

### Server-side

Create a `PaymentIntent` on your server and specify the `amount` to collect, and `eur` or `pln` as the currency. If you have an existing [Payment Intents](https://docs.stripe.com/payments/payment-intents.md) integration, add `p24` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "pln",
  payment_method_types: ["p24"],
});
```

Instead of passing the entire PaymentIntent object to your app, return its *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)). The PaymentIntent’s client secret is a unique key that lets you *confirm* (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) the payment and update payment details on the client, without allowing manipulation of sensitive information, like the payment amount.

### Client-side

On the client, request a PaymentIntent from your server and store its client secret.

#### Swift

```swift
class CheckoutViewController: UIViewController {
    var paymentIntentClientSecret: String?

    func startCheckout() {
        // Request a PaymentIntent from your server and store its client secret
    }
}
```

### Statement descriptors with Przelewy24

You can set a [custom statement descriptor](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-statement_descriptor) before confirming the PaymentIntent. For Przelewy24, the statement descriptor is limited to 14 characters. It’s visible on your customer’s bank records within the payment’s description, with the format `/OPT/X/////P24-XXX-XXX-XXX {statement_descriptor}`, where `/OPT/X/////P24-XXX-XXX-XXX` is a unique reference for the payment generated by Przelewy24.

## Collect payment method details [Client-side]

In your app, collect your customer’s email address. Create a [STPPaymentIntentParams](https://stripe.dev/stripe-ios/stripe-payments/Classes/STPPaymentIntentParams.html) with the billing details.

#### Swift

```swift
let przelewy24Params = STPPaymentMethodPrzelewy24Params()

let billingDetails = STPPaymentMethodBillingDetails()
billingDetails.email = "email@email.com"
```

## Submit the payment to Stripe [Client-side]

Retrieve the client secret from the PaymentIntent you created and call [STPPaymentHandler confirmPayment](<https://stripe.dev/stripe-ios/stripe-payments/Classes/STPPaymentHandler.html#/c:@M@StripePayments@objc(cs)STPPaymentHandler(im)confirmPayment:withAuthenticationContext:completion:>). This presents a webview where the customer can complete the payment. Upon completion, the completion block is called with the result of the payment.

#### Swift

```swift
let paymentIntentParams = STPPaymentIntentParams(clientSecret: paymentIntentClientSecret)

paymentIntentParams.paymentMethodParams = STPPaymentMethodParams(
    przelewy24: przelewy24Params,
    billingDetails: billingDetails,
    metadata: nil
)

STPPaymentHandler.shared().confirmPayment(paymentIntentParams, with: self) { (handlerStatus, paymentIntent, error) in
    switch handlerStatus {
    case .succeeded:
        // Payment succeeded

    case .canceled:
        // Payment was canceled

    case .failed:
        // Payment failed

    @unknown default:
        fatalError()
    }
}
```

## Optional: Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

### Receive events and run business actions

There are a few options for receiving and running business actions.

#### Manually

Use the Stripe Dashboard to view all your Stripe payments, send email receipts, handle payouts, or retry failed payments.

- [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments)

#### Custom code

Build a webhook handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook)

#### Prebuilt apps

Handle common business events, like [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

# Android

> This is a Android for when payment-ui is mobile and platform is android. View the full page at https://docs.stripe.com/payments/p24/accept-a-payment?payment-ui=mobile&platform=android.

> We recommend that you follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md) guide unless you need to use manual server-side confirmation, or your integration requires presenting payment methods separately. If you’ve already integrated with Elements, see the [Payment Element migration guide](https://docs.stripe.com/payments/payment-element/migration.md).

[Przelewy24](https://www.przelewy24.pl) is a [single-use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method where customers are required to [authenticate](https://docs.stripe.com/payments/payment-methods.md#customer-actions) their payment. Customers pay with Przelewy24 by redirecting from your website, authorizing the payment, then returning to your website where you get [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) on whether the payment succeeded or failed.

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
  implementation("com.stripe:stripe-android:23.5.0")
  // Include the financial connections SDK to support US bank account as a payment method
  implementation("com.stripe:financial-connections:23.5.0")
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

## Create a PaymentIntent [Server-side] [Client-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) represents your intent to collect payment from a customer and tracks the lifecycle of the payment process.

### Server-side

Create a `PaymentIntent` on your server and specify the `amount` to collect, and `eur` or `pln` as the currency. If you have an existing [Payment Intents](https://docs.stripe.com/payments/payment-intents.md) integration, add `p24` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "pln",
  payment_method_types: ["p24"],
});
```

Instead of passing the entire PaymentIntent object to your app, return its *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)). The PaymentIntent’s client secret is a unique key that lets you *confirm* (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) the payment and update payment details on the client, without allowing manipulation of sensitive information, like the payment amount.

### Client-side

On the client, request a PaymentIntent from your server and store its client secret.

#### Kotlin

```kotlin
class P24PaymentActivity: AppCompatActivity() {
    private lateinit var paymentIntentClientSecret: String

    override fun onCreate(savedInstanceState: Bundle?) {
        // ...
        startCheckout()
    }


    private fun startCheckout() {
        // Request a PaymentIntent from your server and store its client secret
    }
}
```

### Statement descriptors with Przelewy24

You can set a [custom statement descriptor](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-statement_descriptor) before confirming the PaymentIntent. For Przelewy24, the statement descriptor is limited to 14 characters. It’s visible on your customer’s bank records within the payment’s description, with the format `/OPT/X/////P24-XXX-XXX-XXX {statement_descriptor}`, where `/OPT/X/////P24-XXX-XXX-XXX` is a unique reference for the payment generated by Przelewy24.

## Collect payment method details [Client-side]

In your app, collect your customer’s email address. Create a `PaymentMethodCreateParams` with the billing details.

#### Kotlin

```kotlin
val billingDetails = PaymentMethod.BillingDetails(email = "email@email.com")
val paymentMethodCreateParams = PaymentMethodCreateParams.createP24(billingDetails)
```

## Submit the payment to Stripe [Client-side]

Retrieve the client secret from the PaymentIntent you created and call [PaymentLauncher confirm](https://stripe.dev/stripe-android/payments-core/com.stripe.android.payments.paymentlauncher/-payment-launcher/index.html#74063765%2FFunctions%2F-1622557690). This presents a webview where the customer can complete the payment. Upon completion, `onPaymentResult` is called with the result of the payment.

#### Kotlin

```kotlin
class P24PaymentActivity : AppCompatActivity() {
    // ...
    private lateinit var paymentIntentClientSecret: String
    private val paymentLauncher: PaymentLauncher by lazy {
        val paymentConfiguration = PaymentConfiguration.getInstance(applicationContext)
        PaymentLauncher.Companion.create(
            this,
            paymentConfiguration.publishableKey,
            paymentConfiguration.stripeAccountId,
            ::onPaymentResult
        )
    }

    private fun startCheckout() {
        // ...

        val confirmParams = ConfirmPaymentIntentParams
                .createWithPaymentMethodCreateParams(
                  paymentMethodCreateParams = paymentMethodCreateParams,
                  clientSecret = paymentIntentClientSecret
                )
        paymentLauncher.confirm(confirmParams)
    }

    private fun onPaymentResult(paymentResult: PaymentResult) {
        when (paymentResult) {
            is PaymentResult.Completed -> {
                // show success UI
            }
            is PaymentResult.Canceled -> {
                // handle cancel flow
            }
            is PaymentResult.Failed -> {
                // handle failures
                // (for example, the customer may need to choose a new payment
                // method)
            }
        }
    }
}
```

## Optional: Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

### Receive events and run business actions

There are a few options for receiving and running business actions.

#### Manually

Use the Stripe Dashboard to view all your Stripe payments, send email receipts, handle payouts, or retry failed payments.

- [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments)

#### Custom code

Build a webhook handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook)

#### Prebuilt apps

Handle common business events, like [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

# React Native

> This is a React Native for when payment-ui is mobile and platform is react-native. View the full page at https://docs.stripe.com/payments/p24/accept-a-payment?payment-ui=mobile&platform=react-native.

> We recommend that you follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md) guide unless you need to use manual server-side confirmation, or your integration requires presenting payment methods separately. If you’ve already integrated with Elements, see the [Payment Element migration guide](https://docs.stripe.com/payments/payment-element/migration.md).

[Przelewy24](https://www.przelewy24.pl) is a [single-use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method where customers are required to [authenticate](https://docs.stripe.com/payments/payment-methods.md#customer-actions) their payment. Customers pay with Przelewy24 by redirecting from your website, authorizing the payment, then returning to your website where you get [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) on whether the payment succeeded or failed.

## Set up Stripe [Server-side] [Client-side]

### Server-side

This integration requires endpoints on your server that talk to the Stripe API. Use our official libraries for access to the Stripe API from your server:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

### Client-side

The [React Native SDK](https://github.com/stripe/stripe-react-native) is open source and fully documented. Internally, it uses the [native iOS](https://github.com/stripe/stripe-ios) and [Android](https://github.com/stripe/stripe-android) SDKs. To install Stripe’s React Native SDK, run one of the following commands in your project’s directory (depending on which package manager you use):

#### yarn

```bash
yarn add @stripe/stripe-react-native
```

#### npm

```bash
npm install @stripe/stripe-react-native
```

Next, install some other necessary dependencies:

- For iOS, go to the **ios** directory and run `pod install` to ensure that you also install the required native dependencies.
- For Android, there are no more dependencies to install.

> We recommend following the [official TypeScript guide](https://reactnative.dev/docs/typescript#adding-typescript-to-an-existing-project) to add TypeScript support.

### Stripe initialization

To initialize Stripe in your React Native app, either wrap your payment screen with the `StripeProvider` component, or use the `initStripe` initialization method. Only the API [publishable key](https://docs.stripe.com/keys.md#obtain-api-keys) in `publishableKey` is required. The following example shows how to initialize Stripe using the `StripeProvider` component.

```jsx
import { useState, useEffect } from "react";
import { StripeProvider } from "@stripe/stripe-react-native";

function App() {
  const [publishableKey, setPublishableKey] = useState("");

  const fetchPublishableKey = async () => {
    const key = await fetchKey(); // fetch key from your server here
    setPublishableKey(key);
  };

  useEffect(() => {
    fetchPublishableKey();
  }, []);

  return (
    <StripeProvider
      publishableKey={publishableKey}
      merchantIdentifier="merchant.identifier" // required for Apple Pay
      urlScheme="your-url-scheme" // required for 3D Secure and bank redirects
    >
      {/* Your app code here */}
    </StripeProvider>
  );
}
```

> Use your API [test keys](https://docs.stripe.com/keys.md#obtain-api-keys) while you test and develop, and your [live mode](https://docs.stripe.com/keys.md#test-live-modes) keys when you publish your app.

## Create a PaymentIntent [Server-side] [Client-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) represents your intent to collect payment from a customer and tracks the lifecycle of the payment process.

### Server-side

Create a `PaymentIntent` on your server and specify the `amount` to collect, and `eur` or `pln` as the currency. If you have an existing [Payment Intents](https://docs.stripe.com/payments/payment-intents.md) integration, add `p24` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "pln",
  payment_method_types: ["p24"],
});
```

Instead of passing the entire PaymentIntent object to your app, return its *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)). The PaymentIntent’s client secret is a unique key that lets you *confirm* (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) the payment and update payment details on the client, without allowing manipulation of sensitive information, like the payment amount.

### Client-side

On the client, request a PaymentIntent from your server and store its client secret.

```javascript
const fetchPaymentIntentClientSecret = async () => {
  const response = await fetch(`${API_URL}/create-payment-intent`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      email,
      currency: "pln",
      payment_method_types: ["p24"],
    }),
  });
  const { clientSecret, error } = await response.json();

  return { clientSecret, error };
};
```

### Statement descriptors with Przelewy24

You can set a [custom statement descriptor](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-statement_descriptor) before confirming the PaymentIntent. For Przelewy24, the statement descriptor is limited to 14 characters. It’s visible on your customer’s bank records within the payment’s description, with the format `/OPT/X/////P24-XXX-XXX-XXX {statement_descriptor}`, where `/OPT/X/////P24-XXX-XXX-XXX` is a unique reference for the payment generated by Przelewy24.

## Collect payment method details [Client-side]

In your app, collect your customer’s email address.

```javascript
export default function P24PaymentScreen() {
  const [email, setEmail] = useState();

  const handlePayPress = async () => {
    // ...
  };

  return (
    <Screen>
      <TextInput
        placeholder="E-mail"
        onChange={(value) => setEmail(value.nativeEvent.text)}
      />
    </Screen>
  );
}
```

## Submit the payment to Stripe [Client-side]

Retrieve the client secret from the PaymentIntent you created and call `confirmPayment`. This presents a webview where the customer can complete the payment on their bank’s website or app. Afterwards, the promise resolves with the result of the payment.

```javascript
export default function P24PaymentScreen() {
  const [email, setEmail] = useState();

  const handlePayPress = async () => {
    const billingDetails: PaymentMethodCreateParams.BillingDetails = {
      email,
    };
  };

  const { error, paymentIntent } = await confirmPayment(clientSecret, {
    paymentMethodType: 'P24',
    paymentMethodData: {
      billingDetails,
    }
  });

  if (error) {
    Alert.alert(`Error code: ${error.code}`, error.message);
  } else if (paymentIntent) {
    Alert.alert(
      'Success',
      `The payment was confirmed successfully! currency: ${paymentIntent.currency}`
    );
  }

  return (
    <Screen>
      <TextInput
        placeholder="E-mail"
        onChange={(value) => setEmail(value.nativeEvent.text)}
      />
    </Screen>
  );
}
```

## Optional: Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

### Receive events and run business actions

There are a few options for receiving and running business actions.

#### Manually

Use the Stripe Dashboard to view all your Stripe payments, send email receipts, handle payouts, or retry failed payments.

- [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments)

#### Custom code

Build a webhook handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook)

#### Prebuilt apps

Handle common business events, like [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

## Optional: Handle deep linking

When a customer exits your app (for example to authenticate in Safari or their banking app), provide a way for them to automatically return to your app. Many payment method types *require* a return URL. If you don’t provide one, we can’t present payment methods that require a return URL to your users, even if you’ve enabled them.

To provide a return URL:

1. [Register](https://developer.apple.com/documentation/xcode/defining-a-custom-url-scheme-for-your-app#Register-your-URL-scheme) a custom URL. Universal links aren’t supported.
1. [Configure](https://reactnative.dev/docs/linking) your custom URL.
1. Set up your root component to forward the URL to the Stripe SDK as shown below.

> If you’re using Expo, [set your scheme](https://docs.expo.io/guides/linking/#in-a-standalone-app) in the `app.json` file.

```jsx
import { useEffect, useCallback } from 'react';
import { Linking } from 'react-native';
import { useStripe } from '@stripe/stripe-react-native';

export default function MyApp() {
  const { handleURLCallback } = useStripe();

  const handleDeepLink = useCallback(
    async (url: string | null) => {
      if (url) {
        const stripeHandled = await handleURLCallback(url);
        if (stripeHandled) {
          // This was a Stripe URL - you can return or add extra handling here as you see fit
        } else {
          // This was NOT a Stripe URL – handle as you normally would
        }
      }
    },
    [handleURLCallback]
  );

  useEffect(() => {
    const getUrlAsync = async () => {
      const initialUrl = await Linking.getInitialURL();
      handleDeepLink(initialUrl);
    };

    getUrlAsync();

    const deepLinkListener = Linking.addEventListener(
      'url',
      (event: { url: string }) => {
        handleDeepLink(event.url);
      }
    );

    return () => deepLinkListener.remove();
  }, [handleDeepLink]);

  return (
    <View>
      <AwesomeAppComponent />
    </View>
  );
}
```

For more information on native URL schemes, refer to the [Android](https://developer.android.com/training/app-links/deep-linking) and [iOS](https://developer.apple.com/documentation/xcode/allowing_apps_and_websites_to_link_to_your_content/defining_a_custom_url_scheme_for_your_app) docs.

# Elements

> This is a Elements for when payment-ui is elements. View the full page at https://docs.stripe.com/payments/p24/accept-a-payment?payment-ui=elements.

> The content of this section refers to a *Legacy* (Technology that's no longer recommended) product. You should use the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md) guide for the most recent integration path instead. While Stripe still supports this product, this support might end if the product is deprecated.

[Przelewy24](https://www.przelewy24.pl) is a [single-use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method where customers are required to [authenticate](https://docs.stripe.com/payments/payment-methods.md#customer-actions) their payment. Customers pay with Przelewy24 by redirecting from your website, authorizing the payment, then returning to your website where you get [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) on whether the payment succeeded or failed.

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create a PaymentIntent [Server-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) represents your intent to collect payment from a customer and tracks the lifecycle of the payment process.

Create a `PaymentIntent` on your server and specify the `amount` to collect, and `eur` or `pln` as the currency. If you have an existing [Payment Intents](https://docs.stripe.com/payments/payment-intents.md) integration, add `p24` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "pln",
  payment_method_types: ["p24"],
});
```

Instead of passing the entire PaymentIntent object to your app, return its *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)). The PaymentIntent’s client secret is a unique key that lets you *confirm* (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) the payment and update payment details on the client, without allowing manipulation of sensitive information, like the payment amount.

### Statement descriptors with Przelewy24

You can set a [custom statement descriptor](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-statement_descriptor) before confirming the PaymentIntent. For Przelewy24, the statement descriptor is limited to 14 characters. It’s visible on your customer’s bank records within the payment’s description, with the format `/OPT/X/////P24-XXX-XXX-XXX {statement_descriptor}`, where `/OPT/X/////P24-XXX-XXX-XXX` is a unique reference for the payment generated by Przelewy24.

## Collect payment method details [Client-side]

Collect payment information on the client with [Stripe Elements](https://docs.stripe.com/payments/elements.md). Elements is a set of prebuilt UI components for collecting payment details.

A Stripe Element contains an iframe that securely sends the payment information to Stripe over an HTTPS connection. The checkout page address must also start with https:// rather than http:// for your integration to work.

You can test your integration without using HTTPS. [Enable it](https://docs.stripe.com/security/guide.md#tls) when you’re ready to accept live payments.

### Set up Stripe Elements

#### HTML + JS

Stripe Elements is automatically available as a feature of Stripe.js. Include the Stripe.js script on your payment page by adding it to the `head` of your HTML file. Always load Stripe.js directly from js.stripe.com to remain PCI compliant. Don’t include the script in a bundle or host a copy of it yourself.

```html
<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/dahlia/stripe.js"></script>
</head>
```

Create an instance of Elements with the following JavaScript on your checkout page:

```javascript
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");
const elements = stripe.elements();
```

### Add and configure an p24Bank Element

> This doc refers to a *Legacy* (Technology that's no longer recommended) feature that’s no longer available in the latest version of Stripe.js. We recommend you use the [Payment Element](https://docs.stripe.com/payments/payment-element.md), a UI component for the web that accepts 40+ payment methods, validates input, and handles errors.

Elements needs a place to live in your payment form. Create empty DOM nodes (containers) with unique IDs in your payment form and then pass those IDs to Elements.

#### HTML

```html
<form id="payment-form">
  <div class="form-row">
    <label for="accountholder-name"> Name </label>
    <input id="accountholder-name" name="accountholder-name" />
  </div>
  <div class="form-row">
    <label for="accountholder-email"> Email </label>
    <input id="accountholder-email" name="accountholder-email" />
  </div>

  <div class="form-row">
    <!--
      Using a label with a for attribute that matches the ID of the
      Element container enables the Element to automatically gain focus
      when the customer clicks on the label.
    --><label for="p24-bank-element"> P24 Bank </label>
    <div id="p24-bank-element">
      <!-- A Stripe Element will be inserted here. -->
    </div>
  </div>

  <button>Submit Payment</button>

  <!-- Used to display form errors. -->
  <div id="error-message" role="alert"></div>
</form>
```

When the form above has loaded, [create an instance](https://docs.stripe.com/js/elements_object/create_element?type=p24Bank) of an `p24Bank` Element and mount it to the Element container created above:

```javascript
const options = {
  // Custom styling can be passed to options when creating an Element
  style: {
    base: {
      padding: "10px 12px",
      color: "#32325d",
      fontSize: "16px",
      "::placeholder": {
        color: "#aab7c4",
      },
    },
  },
};

// Create an instance of the p24Bank Element
const p24Bank = elements.create("p24Bank", options);

// Add an instance of the p24Bank Element into
// the `p24-bank-element` <div>
p24Bank.mount("#p24-bank-element");
```

Elements are completely customizable. You can [style Elements](https://docs.stripe.com/js/elements_object/create_element?type=p24Bank#elements_create-options) to match the look and feel of your site, providing a seamless checkout experience for your customers. It’s also possible to style various input states (for example, when the Element has focus).

#### React

#### npm

Install [React Stripe.js](https://www.npmjs.com/package/@stripe/react-stripe-js) and the [Stripe.js loader](https://www.npmjs.com/package/@stripe/stripe-js) from the npm public registry.

```bash
npm install --save @stripe/react-stripe-js @stripe/stripe-js
```

#### umd

We also provide a UMD build for sites that don’t use npm or modules.

Include the Stripe.js script, which exports a global `Stripe` function, and the UMD build of React Stripe.js, which exports a global `ReactStripe` object. Always load the Stripe.js script directly from **js.stripe.com** to remain PCI compliant. Don’t include the script in a bundle or host a copy of it yourself.

```html
<!-- Stripe.js -->
<script src="https://js.stripe.com/dahlia/stripe.js"></script>

<!-- React Stripe.js development build -->
<script src="https://unpkg.com/@stripe/react-stripe-js@latest/dist/react-stripe.umd.js"></script>

<!-- When you are ready to deploy your site to production, remove the
      above development script, and include the following production build. -->
<script src="https://unpkg.com/@stripe/react-stripe-js@latest/dist/react-stripe.umd.min.js"></script>
```

> The [demo in CodeSandbox](https://codesandbox.io/s/react-stripe-official-q1loc?fontsize=14&hidenavigation=1&theme=dark) lets you try out React Stripe.js without having to create a new project.

### Add Stripe.js and Elements to your page

To use Element components, wrap your checkout page component in an [Elements provider](https://docs.stripe.com/sdks/stripejs-react.md#elements-provider). Call `loadStripe` with your publishable key and pass the returned `Promise` to the `Elements` provider.

```jsx
import React from "react";
import ReactDOM from "react-dom";
import { Elements } from "@stripe/react-stripe-js";
import { loadStripe } from "@stripe/stripe-js";

import CheckoutForm from "./CheckoutForm";

// Make sure to call `loadStripe` outside of a component's render to avoid
// recreating the `Stripe` object on every render.
const stripePromise = loadStripe("<<YOUR_PUBLISHABLE_KEY>>");

function App() {
  return (
    <Elements stripe={stripePromise}>
      <CheckoutForm />
    </Elements>
  );
}

ReactDOM.render(<App />, document.getElementById("root"));
```

### Add and configure an P24BankElement component

Use the `P24BankElement` to allow your customer to select their preferred bank.

#### JSX

```jsx
/**
 * Use the CSS tab above to style your Element's container.
 */
import React from "react";
import { P24BankElement } from "@stripe/react-stripe-js";
import "./P24BankSectionStyles.css";

const P24_ELEMENT_OPTIONS = {
  // Custom styling can be passed to options when creating an Element
  style: {
    base: {
      padding: "10px 12px",
      color: "#32325d",
      fontSize: "16px",
      "::placeholder": {
        color: "#aab7c4",
      },
    },
  },
};

function P24BankSection() {
  return (
    <label>
      P24 Bank
      <P24BankElement options={P24_ELEMENT_OPTIONS} />
    </label>
  );
}

export default P24BankSection;
```

Elements are completely customizable. You can [style Elements](https://docs.stripe.com/js/elements_object/create_element?type=p24Bank#elements_create-options) to match the look and feel of your site, providing a seamless checkout experience for your customers. It’s also possible to style various input states (for example, when the Element has focus).

## Submit the payment to Stripe [Client-side]

Rather than sending the entire PaymentIntent object to the client, use its [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret). This is different from your API keys that authenticate Stripe API requests. The client secret should be handled carefully because it can complete the charge. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

#### HTML + JS

Use [stripe.confirmP24Payment](https://docs.stripe.com/js/payment_intents/confirm_p24_payment) to handle the redirect away from your page and to complete the payment. Add a [return_url](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-return_url) to this function to indicate where Stripe should redirect the user after they complete the payment on their bank’s website or mobile application.

```javascript
const form = document.getElementById('payment-form');
const accountholderName = document.getElementById('accountholder-name');
const accountholderEmail = document.getElementById('accountholder-email');

form.addEventListener('submit', (event) => {
  event.preventDefault();

  // Redirects away from the client
  const {error} = await stripe.confirmP24Payment(
    '{{PAYMENT_INTENT_CLIENT_SECRET}}',
    {
      payment_method: {
        p24: p24Bank,
        billing_details: {
          name: accountholderName.value,
          email: accountholderEmail.value,
        },
      },
      payment_method_options: {
        p24: {
          // To be able to pass the `tos_shown_and_accepted` parameter, you must
          // ensure that the P24 regulations and information obligation consent
          // text is clearly visible to the customer. See
          // stripe.com/docs/payments/p24/accept-a-payment#requirements
          // for directions.
          tos_shown_and_accepted: true,
        }
      },
      return_url: 'https://example.com/checkout/complete',
    }
  );
});
```

#### React

Use [stripe.confirmP24Payment](https://docs.stripe.com/js/payment_intents/confirm_p24_payment) to handle the redirect away from your page and to complete the payment. Add a [return_url](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-return_url) to this function to indicate where Stripe should redirect the user after they complete the payment on their bank’s website or mobile application.

To call `stripe.confirmP24Payment` from your payment form component, use the [useStripe](https://docs.stripe.com/sdks/stripejs-react.md#usestripe-hook) and [useElements](https://docs.stripe.com/sdks/stripejs-react.md#useelements-hook) hooks.

If you prefer traditional class components over hooks, you can instead use an [ElementsConsumer](https://docs.stripe.com/sdks/stripejs-react.md#elements-consumer).

#### Hooks

```jsx
import React from "react";
import {
  useStripe,
  useElements,
  P24BankElement,
} from "@stripe/react-stripe-js";

import P24BankSection from "./P24BankSection";

export default function CheckoutForm() {
  const stripe = useStripe();
  const elements = useElements();

  const handleSubmit = async (event) => {
    // We don't want to let default form submission happen here,
    // which would refresh the page.
    event.preventDefault();
    if (!stripe || !elements) {
      // Stripe.js hasn't yet loaded.
      // Make sure to disable form submission until Stripe.js has loaded.
      return;
    }

    const p24Bank = elements.getElement(P24BankElement);

    // For brevity, this example is using uncontrolled components for
    // the accountholder's name. In a real world app you will
    // probably want to use controlled components.
    // https://reactjs.org/docs/uncontrolled-components.html
    // https://reactjs.org/docs/forms.html#controlled-components
    const accountholderName = event.target["accountholder-name"];
    const { error } = await stripe.confirmP24Payment("{CLIENT_SECRET}", {
      payment_method: {
        p24: p24Bank,
        billing_details: {
          name: accountholderName.value,
        },
      },
      payment_method_options: {
        p24: {
          // To be able to pass the `tos_shown_and_accepted` parameter, you must
          // ensure that the P24 regulations and information obligation consent
          // text is clearly in the view of the customer. See
          // stripe.com/docs/payments/p24/accept-a-payment#requirements
          // for directions.
          tos_shown_and_accepted: true,
        },
      },
      return_url: "https://example.com/checkout/complete",
    });

    if (error) {
      // Show error to your customer.
      console.log(error.message);
    }

    // Otherwise the customer will be redirected away from your
    // page to complete the payment with their bank.
  };

  return (
    <form onSubmit={handleSubmit}>
      <div className="form-row">
        <label>
          Name
          <input
            name="accountholder-name"
            placeholder="Jenny Rosen"
            required
            autocomplete
          />
        </label>
      </div>
      <div className="form-row">
        <P24BankSection />
      </div>
      <button type="submit" disabled={!stripe}>
        Submit Payment
      </button>
    </form>
  );
}
```

#### Class Components

```jsx
import React from "react";
import { ElementsConsumer, P24BankElement } from "@stripe/react-stripe-js";

import P24BankSection from "./P24BankSection";

class CheckoutForm extends React.Component {
  handleSubmit = async (event) => {
    // We don't want to let default form submission happen here,
    // which would refresh the page.
    event.preventDefault();
    const { stripe, elements } = this.props;
    if (!stripe || !elements) {
      // Stripe.js hasn't yet loaded.
      // Make  sure to disable form submission until Stripe.js has loaded.
      return;
    }

    const p24Bank = elements.getElement(P24BankElement);

    // For brevity, this example is using uncontrolled components for
    // the accountholder's name. In a real world app you will
    // probably want to use controlled components.
    // https://reactjs.org/docs/uncontrolled-components.html
    // https://reactjs.org/docs/forms.html#controlled-components

    const accountholderName = event.target["accountholder-name"];
    const { error } = await stripe.confirmP24Payment("{CLIENT_SECRET}", {
      payment_method: {
        p24: p24Bank,
        billing_details: {
          name: accountholderName.value,
        },
      },
      return_url: "https://example.com/checkout/complete",
    });

    if (error) {
      // Show error to your customer.
      console.log(error.message);
    }

    // Otherwise the customer will be redirected away from your
    // page to complete the payment with their bank.
  };

  render() {
    const { stripe } = this.props;

    return (
      <form onSubmit={this.handleSubmit}>
        <div className="form-row">
          <label>
            Name
            <input
              name="accountholder-name"
              placeholder="Jenny Rosen"
              required
            />
          </label>
        </div>
        <div className="form-row">
          <P24BankSection />
        </div>
        <button type="submit" disabled={!stripe}>
          Submit Payment
        </button>
      </form>
    );
  }
}

export default function InjectedCheckoutForm() {
  return (
    <ElementsConsumer>
      {({ stripe, elements }) => (
        <CheckoutForm stripe={stripe} elements={elements} />
      )}
    </ElementsConsumer>
  );
}
```

When your customer submits a payment, Stripe redirects them to the `return_url` and includes the following URL query parameters. The return page can use them to get the status of the PaymentIntent so it can display the payment status to the customer.

When you specify the `return_url`, you can also append your own query parameters for use on the return page.

| Parameter                      | Description                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_intent`               | The unique identifier for the `PaymentIntent`.                                                                                                                                                                                                                                                                                                             |
| `payment_intent_client_secret` | The [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) of the `PaymentIntent` object. For subscription integrations, this client_secret is also exposed on the `Invoice` object through [`confirmation_secret`](https://docs.stripe.com/api/invoices/object.md#invoice_object-confirmation_secret) |

When the customer is redirected back to your site, you can use the `payment_intent_client_secret` to query for the PaymentIntent and display the transaction status to your customer.

You can find details about the bank account the customer used to complete the payment on the resulting Charge under the [payment_method_details](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-p24) property.

#### Json

```json
{
  "charges": {
    "data": [
      {
        "payment_method_details": {
          "p24": {
            "bank": "inteligo",
            "reference": "P24 123-456-789",
            "verified_name": "JENNY ROSEN"
          },
          "type": "p24"
        },
        "id": "src_16xhynE8WzK49JbAs9M21jaR",
        "object": "source",
        "amount": 1099,
        "client_secret": "src_client_secret_UfwvW2WHpZ0s3QEn9g5x7waU",
        "created": 1445277809,
        "currency": "eur",
        "flow": "redirect",
        "livemode": true,
        "statement_descriptor": null,
        "status": "pending",
        "type": "p24",
        "usage": "single_use"
      }
    ],
    "object": "list",
    "has_more": false,
    "url": "/v1/charges?payment_intent=pi_1G1sgdKi6xqXeNtkldRRE6HT"
  },
  "payment_method_options": {
    "p24": {}
  },
  "payment_method_types": ["p24"],
  "id": "pi_1G1sgdKi6xqXeNtkldRRE6HT",
  "object": "payment_intent",
  "amount": 1099,
  "client_secret": "pi_1G1sgdKi6xqXeNtkldRRE6HT_secret_h9B56ObhTN72fQiBAuzcVPb2E",
  "confirmation_method": "automatic",
  "created": 1579259303,
  "currency": "eur",
  "livemode": true,
  "next_action": null
}
```

## Test your integration

Select any bank in the P24 bank list with your test API keys. After confirming the payment, you’re redirected to a test page with options to succeed or fail the payment. You can test the successful payment case by authenticating the payment on the redirect page. The PaymentIntent will transition from `requires_action` to `succeeded`.

To test the case where the user fails to authenticate, select any bank with your test API keys. On the redirect page, click **Fail test payment**. Your PaymentIntent will transition from `requires_action` to `requires_payment_method`.

## Optional: Handle post-payment events [Server-side]

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

### Receive events and run business actions

There are a few options for receiving and running business actions.

#### Manually

Use the Stripe Dashboard to view all your Stripe payments, send email receipts, handle payouts, or retry failed payments.

- [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments)

#### Custom code

Build a webhook handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook)

#### Prebuilt apps

Handle common business events, like [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

## Optional: Handle P24 Bank Element changes [Client-side]

The P24 Bank Element outputs the customer’s selected bank as it changes. To perform additional logic with the bank value (for example, requiring the field for form validation), you can listen to the change event:

#### HTML + JS

```javascript
p24Bank.on("change", (event) => {
  const bank = event.value;
  // Perform any additional logic here...
});
```

#### React

```jsx
<P24BankElement onChange={(event) => {
  const bank = event.value;
  // Perform any additional logic here...
}}>
```

The change event contains other parameters that can help to build a richer user experience. Refer to the [Stripe.js reference](https://docs.stripe.com/js/element/events/on_change?type=p24BankElement#element_on_change-handler) for more detail.

## Optional: Handle P24 redirect manually [Server-side]

We recommend relying on Stripe.js to handle P24 redirects and payments with `confirmP24Payment`. However, you can also manually redirect your customers by:

1. Providing the URL where your customers will be redirected after they complete their payment.
1. Optionally providing the customer’s bank, where they will be redirected to authorize the payment. You can find the list of available banks under the [Bank values](https://docs.stripe.com/payments/p24/accept-a-payment.md#bank-values) section.
1. Optionally specify that the customer has seen and consented to the P24 regulations and information obligation terms. Follow the guidelines provided under the [Requirements](https://docs.stripe.com/payments/p24/accept-a-payment.md#requirements) section to *confirm* (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) that your implementation meets the requirements.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.confirm(
  "{{PAYMENT_INTENT_ID}}",
  {
    return_url: "https://example.com/checkout/complete",
    payment_method_data: {
      type: "p24",
      p24: {
        bank: "inteligo",
      },
    },
    payment_method_options: {
      p24: {
        // To be able to pass the `tos_shown_and_accepted` parameter, you must
        // ensure that the P24 regulations and information obligation consent
        // text is clearly visible to the customer. See the section on Requirements
        // for guidance.
        tos_shown_and_accepted: true,
      },
    },
  },
);
```

1. Confirming the `PaymentIntent` has a status of `requires_action`. The type for the `next_action` will be `redirect_to_url`.

#### Json

```json
{
  "next_action": {
    "type": "redirect_to_url",
    "redirect_to_url": {
      "url": "https://hooks.stripe.com/...",
      "return_url": "https://example.com/checkout/complete"
    }
  },
  "charges": {
    "data": [
      {
        "payment_method_details": {
          "p24": {
            "bank": "inteligo",
            "reference": "P24 123-456-789",
            "verified_name": "JENNY ROSEN"
          },
          "type": "p24"
        },
        "id": "src_16xhynE8WzK49JbAs9M21jaR",
        "object": "source",
        "amount": 1099,
        "client_secret": "src_client_secret_UfwvW2WHpZ0s3QEn9g5x7waU",
        "created": 1445277809,
        "currency": "eur",
        "flow": "redirect",
        "livemode": true,
        "statement_descriptor": null,
        "status": "pending",
        "type": "p24",
        "usage": "single_use"
      }
    ],
    "object": "list",
    "has_more": false,
    "url": "/v1/charges?payment_intent=pi_1G1sgdKi6xqXeNtkldRRE6HT"
  },
  "payment_method_options": {
    "p24": {}
  },
  "payment_method_types": ["p24"],
  "id": "pi_1G1sgdKi6xqXeNtkldRRE6HT",
  "object": "payment_intent",
  "amount": 1099,
  "client_secret": "pi_1G1sgdKi6xqXeNtkldRRE6HT_secret_h9B56ObhTN72fQiBAuzcVPb2E",
  "confirmation_method": "automatic",
  "created": 1579259303,
  "currency": "eur",
  "livemode": true
}
```

1. Redirecting the customer to the URL provided in the `next_action` property.

```javascript
const action = intent.next_action;
if (action && action.type === "redirect_to_url") {
  window.location = action.redirect_to_url.url;
}
```

When the customer finishes the payment process, they’re sent to the `return_url` destination. The `payment_intent` and `payment_intent_client_secret` URL query parameters are included and you can pass through your own query parameters, as described above.

## Optional: Store the customer's bank preference [Client-side]

You can’t reuse P24 _PaymentMethods_ (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) or save them to customers. You must create a new P24 PaymentMethod each time your customer selects this method of payment in your checkout, using the P24 Bank Element. To track your customer’s bank preference, store their bank value in your own database or use the `metadata` property on the _Customer_ (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) object.

You can prefill the P24 Bank Element with the customer’s bank preference when creating the Element:

#### HTML + JS

```javascript
const options = {
  // Include the bank name along with any custom stylingvalue: 'inteligo',
  style: {
    base: {
      padding: "10px 12px",
      color: "#32325d",
      fontSize: "16px",
      "::placeholder": {
        color: "#aab7c4",
      },
    },
  },
};

// Create an instance of the Element
const p24Bank = elements.create("p24Bank", options);

// Mount the Element
p24Bank.mount("#p24-bank-element");
```

#### React

```jsx
const P24_ELEMENT_OPTIONS = {
  // Include the bank name along with any custom stylingvalue: 'inteligo',
  style: {
    base: {
      padding: '10px 12px',
      color: '#32325d',
      fontSize: '16px',
      '::placeholder': {
        color: '#aab7c4'
      },
    },
  },
}

<P24BankElement options={P24_ELEMENT_OPTIONS} />
```

## Przelewy24 requirements

Przelewy24 requires customers to agree to their Terms of Service to successfully authorize the transaction. This means that the customer will first be redirected to a Przelewy24 page where they can accept these terms. To skip the intermediate page, you’re required to present the Przelewy24 terms on your website, and collect consent on their behalf. When you’ve done that, you’ll be able to set the `p24[tos_shown_and_accepted]` payment method option.

| Requirement                                                                         | Details                                                                                 |
| ----------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Present a hyperlinked Przelewy24 Terms of Service standard wording with hyperlinks. | The following text should be clearly visible to the customer, with hyperlinks included: |

- **Standard wording in Polish (hyperlinked)**: Oświadczam, że zapoznałem się z [regulaminem](https://www.przelewy24.pl/regulamin) i [obowiązkiem informacyjnym](https://www.przelewy24.pl/obowiazekinformacyjny) serwisu Przelewy24.
- **Standard wording in English (hyperlinked)**: I declare that I have familiarized myself with the [regulations](https://www.przelewy24.pl/regulamin) and [information obligation](https://www.przelewy24.pl/obowiazekinformacyjny) of the Przelewy24 service. |

## Bank values

| Bank name                     | Value                |
| ----------------------------- | -------------------- |
| Alior Bank                    | alior_bank           |
| Bank Millennium               | bank_millennium      |
| Bank Nowy BFG S.A.            | bank_nowy_bfg_sa     |
| Bank Pekao                    | bank_pekao_sa        |
| Bank Pocztowy                 | etransfer_pocztowy24 |
| Banki Spółdzielcze            | banki_spbdzielcze    |
| BLIK                          | blik                 |
| BNP Paribas                   | bnp_paribas          |
| BOŚ (Bank Ochrony Środowiska) | boz                  |
| Citi Handlowy                 | citi_handlowy        |
| Credit Agricole               | credit_agricole      |
| ING Bank Śląski               | ing                  |
| Inteligo                      | inteligo             |
| mBank                         | mbank_mtransfer      |
| Nest Bank                     | nest_przelew         |
| PKO Bank Polski               | pbac_z_ipko          |
| Plus Bank                     | plus_bank            |
| Santander Bank Polska         | santander_przelew24  |
| Toyota Bank                   | toyota_bank          |
| VeloBank                      | velobank             |
| Volkswagen Bank               | volkswagen_bank      |
