<!-- Source URL: https://docs.stripe.com/payments/ideal/accept-a-payment -->
<!-- Fetched: 2026-05-03 -->

# Accept an iDEAL | Wero payment

Learn how to accept iDEAL | Wero, a common payment method in the Netherlands.

# Checkout

> This is a Checkout for when payment-ui is checkout. View the full page at https://docs.stripe.com/payments/ideal/accept-a-payment?payment-ui=checkout.

> Stripe can automatically present the relevant payment methods to your customers by evaluating currency, payment method restrictions, and other parameters.
>
> - Follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=checkout&ui=stripe-hosted) guide to build a Checkout integration that uses [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md).

- If you don’t want to use dynamic payment methods, follow the steps below to manually configure the payment methods in your Checkout integration.

iDEAL | Wero (formerly iDEAL) is a [single use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method where customers are required to [authenticate](https://docs.stripe.com/payments/payment-methods.md#customer-actions) their payment. *Customers* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) pay with iDEAL | Wero by redirecting from your website, authorizing the payment, then returning to your website where you get [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) on whether the payment succeeded or failed.

> To accept iDEAL | Wero, you must comply with our [iDEAL Terms of Service](https://stripe.com/ideal/legal).

## Determine compatibility

**Supported business locations**: Europe, US, CA, NZ, SG, HK, JP, AU, MX

**Supported currencies**: `eur`

**Presentment currencies**: `eur`

**Payment mode**: Yes

**Setup mode**: Yes

**Subscription mode**: Yes

A Checkout Session must satisfy all of the following conditions to support iDEAL | Wero payments:

- *Prices* (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) for all line items must be expressed in Euro (currency code `eur`).

## Accept a payment

> This guide builds on the foundational [accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?ui=stripe-hosted) Checkout integration.

This guides you through enabling iDEAL | Wero and shows the differences between accepting payments using dynamic payment methods and manually configuring payment methods.

### Enable iDEAL | Wero as a payment method

When creating a new [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md), you need to:

1. Add `ideal` to the list of `payment_method_types`.
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
  payment_method_types: ["card", "ideal"],
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
  payment_method_types: ["card", "ideal"],
  return_url: "https://example.com/return",
  ui_mode: "embedded_page",
});
```

### Fulfill your orders

After accepting a payment, learn how to [fulfill orders](https://docs.stripe.com/checkout/fulfillment.md).

## Test your integration

When testing your Checkout integration, select iDEAL | Wero as the payment method and click the **Pay** button.

## Handle refunds and disputes

The refund period for iDEAL | Wero is up to 180 days after the original payment.

There is no dispute process—customers authenticate with their bank.

## See also

- [More about iDEAL | Wero](https://docs.stripe.com/payments/ideal.md)
- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment.md)
- [Customizing Checkout](https://docs.stripe.com/payments/checkout/customization.md)

# iOS

> This is a iOS for when payment-ui is mobile and platform is ios. View the full page at https://docs.stripe.com/payments/ideal/accept-a-payment?payment-ui=mobile&platform=ios.

> We recommend that you follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md) guide unless you need to use manual server-side confirmation, or your integration requires presenting payment methods separately. If you’ve already integrated with Elements, see the [Payment Element migration guide](https://docs.stripe.com/payments/payment-element/migration.md).

Accepting iDEAL | Wero in your app consists of displaying a webview that sends your customer to their bank’s online portal to authorize the payment. Your customer then returns to your app and you’re [immediately notified](https://docs.stripe.com/payments/payment-methods.md#payment-notification) about whether the payment succeeded or failed.

> To accept iDEAL | Wero, you must comply with our [iDEAL Terms of Service](https://stripe.com/ideal/legal).

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

A [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) is an object that represents your intent to collect payment from a customer and tracks the lifecycle of the payment process through each stage.

### Server-side

First, create a `PaymentIntent` on your server and specify the amount to collect and the `eur` currency (iDEAL | Wero doesn’t support other currencies). iDEAL | Wero doesn’t have a minimum charge amount, so the payment `amount` value can be as low as 1. If you already have an integration using the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md), add `ideal` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your `PaymentIntent`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  payment_method_types: ["ideal"],
});
```

Instead of passing the entire PaymentIntent object to your app, you only need to return its *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)). The PaymentIntent’s client secret is a unique key that lets you *confirm* (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) the payment and update payment details on the client, without allowing manipulation of sensitive information, like payment amount.

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

## Collect payment method details [Client-side]

In your app, collect your customer’s full name. Create an [STPPaymentIntentParams](https://stripe.dev/stripe-ios/stripe-payments/Classes/STPPaymentIntentParams.html) object with this detail.

#### Swift

```swift
let billingDetails = STPPaymentMethodBillingDetails()
billingDetails.name = "Jane Doe"
```

## Submit the payment to Stripe [Client-side]

Retrieve the client secret from the PaymentIntent you created in step 2 and call [STPPaymentHandler confirmPayment](<https://stripe.dev/stripe-ios/stripe-payments/Classes/STPPaymentHandler.html#/c:@M@StripePayments@objc(cs)STPPaymentHandler(im)confirmPayment:withAuthenticationContext:completion:>). This presents a webview where the customer can complete the payment on their bank’s website or app, which calls the completion block with the result of the payment.

#### Swift

```swift
let paymentIntentParams = STPPaymentIntentParams(clientSecret: paymentIntentClientSecret)
paymentIntentParams.paymentMethodParams = STPPaymentMethodParams(billingDetails: billingDetails,
                                                                 metadata: nil)

STPPaymentHandler.shared().confirmPayment(paymentIntentParams, with: self) { (handlerStatus, paymentIntent, error) in
    switch handlerStatus {
    case .succeeded:
        // Payment succeeded

    case .canceled:
        // Payment was cancelled

    case .failed:
        // Payment failed

    @unknown default:
        fatalError()
    }
}
```

## Test your integration

Use your [test API keys](https://docs.stripe.com/keys.md#test-live-modes) to confirm the PaymentIntent. After confirming, you’re redirected to a test page with options to authorize or fail the payment.

- Click **Authorize test payment** to test the case when the payment is successful. The PaymentIntent transitions from `requires_action` to `succeeded`.
- Click **Fail test payment** to test the case when the customer fails to authenticate. The PaymentIntent transitions from `requires_action` to `requires_payment_method`.

## Optional: Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

- **Handle events manually in the Dashboard**

  Use the Dashboard to [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments), send email receipts, handle payouts, or retry failed payments.

- **Build a custom webhook**

  [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook) handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- **Integrate a prebuilt app**

  Handle common business events, such as [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

## Bank reference

| Bank name               | Value          |
| ----------------------- | -------------- |
| ABN AMRO                | `abn_amro`     |
| ASN Bank                | `asn_bank`     |
| Bunq                    | `bunq`         |
| ING                     | `ing`          |
| Knab                    | `knab`         |
| N26                     | `n26`          |
| Nationale-Nederlanden   | `nn`           |
| Rabobank                | `rabobank`     |
| Revolut                 | `revolut`      |
| RegioBank               | `regiobank`    |
| SNS Bank (De Volksbank) | `sns_bank`     |
| Triodos Bank            | `triodos_bank` |
| Van Lanschot            | `van_lanschot` |
| Yoursafe                | `yoursafe`     |

# Android

> This is a Android for when payment-ui is mobile and platform is android. View the full page at https://docs.stripe.com/payments/ideal/accept-a-payment?payment-ui=mobile&platform=android.

> We recommend that you follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md) guide unless you need to use manual server-side confirmation, or your integration requires presenting payment methods separately. If you’ve already integrated with Elements, see the [Payment Element migration guide](https://docs.stripe.com/payments/payment-element/migration.md).

Accepting iDEAL | Wero in your app consists of displaying a webview that sends your customer to their bank’s online portal to authorize the payment. Your customer then returns to your app and you’re [immediately notified](https://docs.stripe.com/payments/payment-methods.md#payment-notification) about whether the payment succeeded or failed.

> To accept iDEAL | Wero, you must comply with our [iDEAL Terms of Service](https://stripe.com/ideal/legal).

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

A [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) is an object that represents your intent to collect payment from a customer and tracks the lifecycle of the payment process through each stage.

### Server-side

First, create a `PaymentIntent` on your server and specify the amount to collect and the `eur` currency (iDEAL | Wero doesn’t support other currencies). iDEAL | Wero doesn’t have a minimum charge amount, so the payment `amount` value can be as low as 1. If you already have an integration using the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md), add `ideal` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your `PaymentIntent`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  payment_method_types: ["ideal"],
});
```

Instead of passing the entire PaymentIntent object to your app, you only need to return its *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)). The PaymentIntent’s client secret is a unique key that lets you *confirm* (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) the payment and update payment details on the client, without allowing manipulation of sensitive information, like payment amount.

### Client-side

On the client, request a PaymentIntent from your server and store its client secret.

#### Kotlin

```kotlin
class CheckoutActivity: AppCompatActivity() {
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

## Collect payment method details [Client-side]

In your app, collect your customer’s full name. Create a [PaymentMethodCreateParams](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-payment-method-create-params/index.html) object with this detail.

#### Kotlin

```kotlin
val paymentMethodCreateParams = PaymentMethodCreateParams.create(
  ideal = PaymentMethodCreateParams.Ideal(null),
  billingDetails = PaymentMethod.BillingDetails(
    name = "Jane Doe"
  )
)
```

## Submit the payment to Stripe [Client-side]

Retrieve the client secret from the PaymentIntent you created and call [PaymentLauncher confirm](https://stripe.dev/stripe-android/payments-core/com.stripe.android.payments.paymentlauncher/-payment-launcher/index.html#74063765%2FFunctions%2F-1622557690). This presents a webview where the customer can complete the payment on their bank’s website or app, which calls the completion block with the result of the payment.

#### Kotlin

```kotlin
class CheckoutActivity : AppCompatActivity() {
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

## Test your integration

Use your [test API keys](https://docs.stripe.com/keys.md#test-live-modes) to confirm the PaymentIntent. After confirming, you’re redirected to a test page with options to authorize or fail the payment.

- Click **Authorize test payment** to test the case when the payment is successful. The PaymentIntent transitions from `requires_action` to `succeeded`.
- Click **Fail test payment** to test the case when the customer fails to authenticate. The PaymentIntent transitions from `requires_action` to `requires_payment_method`.

## Optional: Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

- **Handle events manually in the Dashboard**

  Use the Dashboard to [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments), send email receipts, handle payouts, or retry failed payments.

- **Build a custom webhook**

  [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook) handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- **Integrate a prebuilt app**

  Handle common business events, such as [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

## Bank reference

| Bank name               | Value          |
| ----------------------- | -------------- |
| ABN AMRO                | `abn_amro`     |
| ASN Bank                | `asn_bank`     |
| Bunq                    | `bunq`         |
| ING                     | `ing`          |
| Knab                    | `knab`         |
| N26                     | `n26`          |
| Nationale-Nederlanden   | `nn`           |
| Rabobank                | `rabobank`     |
| Revolut                 | `revolut`      |
| RegioBank               | `regiobank`    |
| SNS Bank (De Volksbank) | `sns_bank`     |
| Triodos Bank            | `triodos_bank` |
| Van Lanschot            | `van_lanschot` |
| Yoursafe                | `yoursafe`     |

# React Native

> This is a React Native for when payment-ui is mobile and platform is react-native. View the full page at https://docs.stripe.com/payments/ideal/accept-a-payment?payment-ui=mobile&platform=react-native.

> We recommend that you follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md) guide unless you need to use manual server-side confirmation, or your integration requires presenting payment methods separately. If you’ve already integrated with Elements, see the [Payment Element migration guide](https://docs.stripe.com/payments/payment-element/migration.md).

Accepting iDEAL | Wero in your app consists of displaying a webview that sends your customer to their bank’s online portal to authorize the payment. Your customer then returns to your app and you’re [immediately notified](https://docs.stripe.com/payments/payment-methods.md#payment-notification) about whether the payment succeeded or failed.

> To accept iDEAL | Wero, you must comply with our [iDEAL Terms of Service](https://stripe.com/ideal/legal).

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

A [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) is an object that represents your intent to collect payment from a customer and tracks the lifecycle of the payment process through each stage.

### Server-side

First, create a `PaymentIntent` on your server and specify the amount to collect and the `eur` currency (iDEAL | Wero doesn’t support other currencies). iDEAL | Wero doesn’t have a minimum charge amount, so the payment `amount` value can be as low as 1. If you already have an integration using the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md), add `ideal` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your `PaymentIntent`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  payment_method_types: ["ideal"],
});
```

Instead of passing the entire PaymentIntent object to your app, return its *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)). The PaymentIntent’s client secret is a unique key that lets you *confirm* (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) the payment and update payment details on the client, without allowing manipulation of sensitive information, like payment amount.

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
      currency: "eur",
      payment_method_types: ["ideal"],
    }),
  });
  const { clientSecret, error } = await response.json();

  return { clientSecret, error };
};
```

## Collect payment method details [Client-side]

In your app, collect your customer’s full name.

```javascript
export default function IdealPaymentScreen() {
  const [name, setName] = useState();

  const handlePayPress = async () => {
    // ...
  };

  return (
    <Screen>
      <TextInput
        placeholder="Name"
        onChange={(value) => setName(value.nativeEvent.text)}
      />
    </Screen>
  );
}
```

## Submit the payment to Stripe [Client-side]

Retrieve the client secret from the PaymentIntent you created and call `confirmPayment`. This presents a webview where the customer can complete the payment on their bank’s website or app. Afterwards, the promise resolves with the result of the payment.

```javascript
export default function IdealPaymentScreen() {
  const [name, setName] = useState();

  const handlePayPress = async () => {
    const { clientSecret } = await fetchPaymentIntentClientSecret();

    const { error, paymentIntent } = await confirmPayment(clientSecret, {
      paymentMethodType: "Ideal",
      paymentMethodData: {
        billingDetails: {
          name,
        },
      },
    });

    if (error) {
      Alert.alert(`Error code: ${error.code}`, error.message);
    } else if (paymentIntent) {
      Alert.alert(
        "Success",
        `The payment was confirmed successfully! currency: ${paymentIntent.currency}`,
      );
    }
  };

  return <Screen>{/* ... */}</Screen>;
}
```

## Test your integration

Use your [test API keys](https://docs.stripe.com/keys.md#test-live-modes) to confirm the PaymentIntent. After confirming, you’re redirected to a test page with options to authorize or fail the payment.

- Click **Authorize test payment** to test the case when the payment is successful. The PaymentIntent transitions from `requires_action` to `succeeded`.
- Click **Fail test payment** to test the case when the customer fails to authenticate. The PaymentIntent transitions from `requires_action` to `requires_payment_method`.

## Optional: Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

- **Handle events manually in the Dashboard**

  Use the Dashboard to [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments), send email receipts, handle payouts, or retry failed payments.

- **Build a custom webhook**

  [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook) handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- **Integrate a prebuilt app**

  Handle common business events, such as [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

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

## Bank reference

| Bank name               | Value          |
| ----------------------- | -------------- |
| ABN AMRO                | `abn_amro`     |
| ASN Bank                | `asn_bank`     |
| Bunq                    | `bunq`         |
| ING                     | `ing`          |
| Knab                    | `knab`         |
| N26                     | `n26`          |
| Nationale-Nederlanden   | `nn`           |
| Rabobank                | `rabobank`     |
| Revolut                 | `revolut`      |
| RegioBank               | `regiobank`    |
| SNS Bank (De Volksbank) | `sns_bank`     |
| Triodos Bank            | `triodos_bank` |
| Van Lanschot            | `van_lanschot` |
| Yoursafe                | `yoursafe`     |

# Elements

> This is a Elements for when payment-ui is elements. View the full page at https://docs.stripe.com/payments/ideal/accept-a-payment?payment-ui=elements.

iDEAL | Wero is a [single use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method where customers are required to [authenticate](https://docs.stripe.com/payments/payment-methods.md#customer-actions) their payment. *Customers* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) pay with iDEAL | Wero by redirecting from your website, authorizing the payment, then returning to your website where you get [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) on whether the payment succeeded or failed.

Use the [Payment Element](https://docs.stripe.com/payments/payment-element.md) to embed a custom Stripe payment form in your website or application. The Payment Element allows you to support iDEAL | Wero and other payment methods automatically. For advanced configurations and customizations, refer to the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md) integration guide.

> To accept iDEAL | Wero, you must comply with our [iDEAL Terms of Service](https://stripe.com/ideal/legal).

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create a PaymentIntent [Server-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) is an object that represents your intent to collect payment from a customer and tracks the lifecycle of the payment process through each stage. First, create a `PaymentIntent` on your server and specify the amount to collect and the `eur` currency (iDEAL | Wero doesn’t support other currencies). iDEAL | Wero has no minimum charge amount, so the payment `amount` value can be as low as 1. If you already have an integration using the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md), add `ideal` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your `PaymentIntent`.

#### Manage payment methods from the Dashboard

Create a PaymentIntent on your server with an amount and currency. In the latest version of the API, specifying the `automatic_payment_methods` parameter is optional because Stripe enables its functionality by default. You can manage payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods). Stripe determines eligible payment methods based on factors such as the transaction’s amount, currency, and payment flow. Make sure **iDEAL | Wero** is turned on in the [payment methods settings](https://dashboard.stripe.com/settings/payment_methods) page.

Always decide how much to charge on the server side, a trusted environment, as opposed to the client. This prevents malicious customers from being able to choose their own prices.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  automatic_payment_methods: {
    enabled: true,
  },
});
```

#### List payment methods manually

If you don’t want to use the Dashboard or want to manually specify payment methods, you can list them using the `payment_method_types` attribute.

Create a PaymentIntent on your server with an amount, currency, and a list of payment methods. Always decide how much to charge on the server side, a trusted environment, as opposed to the client. This prevents malicious customers from being able to choose their own prices.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  payment_method_types: ["ideal"],
});
```

### Retrieve the client secret

The PaymentIntent includes a *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)) that the client side uses to securely complete the payment process. You can use different approaches to pass the client secret to the client side.

#### Single-page application

Retrieve the client secret from an endpoint on your server, using the browser’s `fetch` function. This approach is best if your client side is a single-page application, particularly one built with a modern frontend framework like React. Create the server endpoint that serves the client secret:

#### Node.js

```javascript
const express = require("express");
const app = express();

app.get("/secret", async (req, res) => {
  const intent = // ... Fetch or create the PaymentIntent
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

Add the [client_secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) in your checkout form. In your server-side code, retrieve the client secret from the PaymentIntent:

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
  const intent = // ... Fetch or create the PaymentIntent
    res.render("checkout", { client_secret: intent.client_secret });
});

app.listen(3000, () => {
  console.log("Running on port 3000");
});
```

## Collect payment method details [Client-side]

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

When the previous form loads, create an instance of the Payment Element and mount it to the container DOM node. Pass the [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) from the previous step into `options` when you create the [Elements](https://docs.stripe.com/js/elements_object/create) instance:

Handle the client secret carefully because it can complete the charge. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

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

import CheckoutForm from "./CheckoutForm";

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
      <CheckoutForm />
    </Elements>
  );
}

ReactDOM.render(<App />, document.getElementById("root"));
```

### Add the Payment Element component

Use the `PaymentElement` component to build your form:

```jsx
import React from 'react';
import {PaymentElement} from '@stripe/react-stripe-js';

const CheckoutForm = () => {
  return (
    <form>
      // Optional: Autofill user's saved payment methods. If the customer's
      // email is known when the page is loaded, you can pass the email
      // to the linkAuthenticationElement
      //
      // <LinkAuthenticationElement id="link-authentication-element"
        // Prefill the email field like so:
        // options={{defaultValues: {email: 'foo@bar.com'}}}
      // /><PaymentElement />
      <button>Submit</button>
    </form>
  );
};

export default CheckoutForm;
```

## Submit the payment to Stripe [Client-side]

Use [stripe.confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment) to complete the payment using details from the Payment Element. Provide a [return_url](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-return_url) to this function to indicate where Stripe should redirect the user after they complete the payment. Your user may be first redirected to an intermediate site, like a bank authorization page, before being redirected to the `return_url`. Card payments immediately redirect to the `return_url` when a payment is successful.

#### HTML + JS

```javascript
const form = document.getElementById("payment-form");

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const { error } = await stripe.confirmPayment({
    //`Elements` instance that was used to create the Payment Element
    elements,
    confirmParams: {
      return_url: "https://example.com/order/123/complete",
    },
  });

  if (error) {
    // This point will only be reached if there is an immediate error when
    // confirming the payment. Show error to your customer (for example, payment
    // details incomplete)
    const messageContainer = document.querySelector("#error-message");
    messageContainer.textContent = error.message;
  } else {
    // Your customer will be redirected to your `return_url`. For some payment
    // methods like iDEAL, your customer will be redirected to an intermediate
    // site first to authorize the payment, then redirected to the `return_url`.
  }
});
```

#### React

To call [stripe.confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment) from your payment form component, use the [useStripe](https://docs.stripe.com/sdks/stripejs-react.md#usestripe-hook) and [useElements](https://docs.stripe.com/sdks/stripejs-react.md#useelements-hook) hooks.

If you prefer traditional class components over hooks, you can instead use an [ElementsConsumer](https://docs.stripe.com/sdks/stripejs-react.md#elements-consumer).

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
    // We don't want to let default form submission happen here,
    // which would refresh the page.
    event.preventDefault();

    if (!stripe || !elements) {
      // Stripe.js hasn't yet loaded.
      // Make sure to disable form submission until Stripe.js has loaded.
      return;
    }
    const { error } = await stripe.confirmPayment({
      //`Elements` instance that was used to create the Payment Element
      elements,
      confirmParams: {
        return_url: "https://example.com/order/123/complete",
      },
    });

    if (error) {
      // This point will only be reached if there is an immediate error when
      // confirming the payment. Show error to your customer (for example, payment
      // details incomplete)
      setErrorMessage(error.message);
    } else {
      // Your customer will be redirected to your `return_url`. For some payment
      // methods like iDEAL, your customer will be redirected to an intermediate
      // site first to authorize the payment, then redirected to the `return_url`.
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <PaymentElement />
      <button disabled={!stripe}>Submit</button>
      {/* Show error message to your customers */}
      {errorMessage && <div>{errorMessage}</div>}
    </form>
  );
};

export default CheckoutForm;
```

Make sure the `return_url` corresponds to a page on your website that provides the status of the payment. When Stripe redirects the customer to the `return_url`, we provide the following URL query parameters:

| Parameter                      | Description                                                                                                                                   |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_intent`               | The unique identifier for the `PaymentIntent`.                                                                                                |
| `payment_intent_client_secret` | The [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) of the `PaymentIntent` object. |

> If you have tooling that tracks the customer’s browser session, you might need to add the `stripe.com` domain to the referrer exclude list. Redirects cause some tools to create new sessions, which prevents you from tracking the complete session.

Use one of the query parameters to retrieve the PaymentIntent. Inspect the [status of the PaymentIntent](https://docs.stripe.com/payments/paymentintents/lifecycle.md) to decide what to show your customers. You can also append your own query parameters when providing the `return_url`, which persist through the redirect process.

#### HTML + JS

```javascript
// Initialize Stripe.js using your publishable key
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");

// Retrieve the "payment_intent_client_secret" query parameter appended to
// your return_url by Stripe.js
const clientSecret = new URLSearchParams(window.location.search).get(
  "payment_intent_client_secret",
);

// Retrieve the PaymentIntent
stripe.retrievePaymentIntent(clientSecret).then(({ paymentIntent }) => {
  const message = document.querySelector("#message");

  // Inspect the PaymentIntent `status` to indicate the status of the payment
  // to your customer.
  //
  // Some payment methods will [immediately succeed or fail][0] upon
  // confirmation, while others will first enter a `processing` state.
  //
  // [0]: https://stripe.com/docs/payments/payment-methods#payment-notification
  switch (paymentIntent.status) {
    case "succeeded":
      message.innerText = "Success! Payment received.";
      break;

    case "processing":
      message.innerText =
        "Payment processing. We'll update you when payment is received.";
      break;

    case "requires_payment_method":
      message.innerText = "Payment failed. Please try another payment method.";
      // Redirect your user back to your payment page to attempt collecting
      // payment again
      break;

    default:
      message.innerText = "Something went wrong.";
      break;
  }
});
```

#### React

```jsx
import React, { useState, useEffect } from "react";
import { useStripe } from "@stripe/react-stripe-js";

const PaymentStatus = () => {
  const stripe = useStripe();
  const [message, setMessage] = useState(null);

  useEffect(() => {
    if (!stripe) {
      return;
    }

    // Retrieve the "payment_intent_client_secret" query parameter appended to
    // your return_url by Stripe.js
    const clientSecret = new URLSearchParams(window.location.search).get(
      "payment_intent_client_secret",
    );

    // Retrieve the PaymentIntent
    stripe.retrievePaymentIntent(clientSecret).then(({ paymentIntent }) => {
      // Inspect the PaymentIntent `status` to indicate the status of the payment
      // to your customer.
      //
      // Some payment methods will [immediately succeed or fail][0] upon
      // confirmation, while others will first enter a `processing` state.
      //
      // [0]: https://stripe.com/docs/payments/payment-methods#payment-notification
      switch (paymentIntent.status) {
        case "succeeded":
          setMessage("Success! Payment received.");
          break;

        case "processing":
          setMessage(
            "Payment processing. We'll update you when payment is received.",
          );
          break;

        case "requires_payment_method":
          // Redirect your user back to your payment page to attempt collecting
          // payment again
          setMessage("Payment failed. Please try another payment method.");
          break;

        default:
          setMessage("Something went wrong.");
          break;
      }
    });
  }, [stripe]);

  return message;
};

export default PaymentStatus;
```

## Test your integration

Use your [test API keys](https://docs.stripe.com/keys.md#test-live-modes) to confirm the PaymentIntent. After confirming, you’re redirected to a test page with options to authorize or fail the payment.

- Click **Authorize test payment** to test the case when the payment is successful. The PaymentIntent transitions from `requires_action` to `succeeded`.
- Click **Fail test payment** to test the case when the customer fails to authenticate. The PaymentIntent transitions from `requires_action` to `requires_payment_method`.

## Optional: Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

- **Handle events manually in the Dashboard**

  Use the Dashboard to [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments), send email receipts, handle payouts, or retry failed payments.

- **Build a custom webhook**

  [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook) handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- **Integrate a prebuilt app**

  Handle common business events, such as [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

## Optional: Handle the iDEAL | Wero redirect manually

We recommend relying on Stripe.js to handle iDEAL | Wero redirects and payments with `confirmIdealPayment`. However, you can also complete the payment on your server and manually redirect your customer.

1. After [collecting payment method details](https://docs.stripe.com/payments/ideal/accept-a-payment.md#web-collect-payment-method-details), call [stripe.createPaymentMethod](https://docs.stripe.com/js/payment_methods/create_payment_method) to create a *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs):
   ```javascript
   const paymentMethod = await stripe.createPaymentMethod({
     type: "ideal",
     billing_details: {
       name: accountholderName.value,
     },
   });
   ```
1. On your server, [confirm](https://docs.stripe.com/api/payment_intents/confirm.md) the PaymentIntent with the PaymentMethod ID and provide a [return_url](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-return_url) to redirect your customer after they complete the payment.

   ```node
   // Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
   // Find your keys at https://dashboard.stripe.com/apikeys.
   const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

   const paymentIntent = await stripe.paymentIntents.confirm(
     "{{PAYMENT_INTENT_ID}}",
     {
       payment_method: "{{PAYMENTMETHOD_ID}}",
       return_url: "https://example.com/checkout/complete",
     },
   );
   ```

   Confirming the `PaymentIntent` has a status of `requires_action` with a `next_action` of `redirect_to_url`.

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
             "ideal": {
               "bank": "ing",
               "bic": "INGBNL2A",
               "iban_last4": "****",
               "verified_name": "JENNY ROSEN"
             },
             "type": "ideal"
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
           "type": "ideal",
           "usage": "single_use"
         }
       ],
       "object": "list",
       "has_more": false,
       "url": "/v1/charges?payment_intent=pi_1G1sgdKi6xqXeNtkldRRE6HT"
     },
     "payment_method_options": {
       "ideal": {}
     },
     "payment_method_types": ["ideal"],
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

1. Redirect your customer to the URL provided in the `next_action` property so they can authenticate and complete the payment.
   ```javascript
   const action = intent.next_action;
   if (action && action.type === "redirect_to_url") {
     window.location = action.redirect_to_url.url;
   }
   ```
   Your customer is redirected to the `return_url` after they complete the payment. The URL includes `payment_intent` and `payment_intent_client_secret` query parameters and you can also append your own query parameters, as described above.

## Bank reference

| Bank name               | Value          |
| ----------------------- | -------------- |
| ABN AMRO                | `abn_amro`     |
| ASN Bank                | `asn_bank`     |
| Bunq                    | `bunq`         |
| ING                     | `ing`          |
| Knab                    | `knab`         |
| N26                     | `n26`          |
| Nationale-Nederlanden   | `nn`           |
| Rabobank                | `rabobank`     |
| Revolut                 | `revolut`      |
| RegioBank               | `regiobank`    |
| SNS Bank (De Volksbank) | `sns_bank`     |
| Triodos Bank            | `triodos_bank` |
| Van Lanschot            | `van_lanschot` |
| Yoursafe                | `yoursafe`     |
