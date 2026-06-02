<!-- Source URL: https://docs.stripe.com/payments/grabpay/accept-a-payment -->
<!-- Fetched: 2026-05-07 -->

# Accept a GrabPay payment

Learn how to accept GrabPay, a common payment method in Southeast Asia.

> *Subscriptions* (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) and using GrabPay for future payments aren’t currently supported. Reach out to [Stripe support](https://support.stripe.com/contact) for any support queries on these features.

# Checkout

> This is a Checkout for when payment-ui is checkout. View the full page at https://docs.stripe.com/payments/grabpay/accept-a-payment?payment-ui=checkout.

> Stripe can automatically present the relevant payment methods to your customers by evaluating currency, payment method restrictions, and other parameters.
>
> - Follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=checkout&ui=stripe-hosted) guide to build a Checkout integration that uses [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md).

- If you don’t want to use dynamic payment methods, follow the steps below to manually configure the payment methods in your Checkout integration.

GrabPay is a [single-use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method. Customers pay with GrabPay by redirecting from your website to GrabPay to authorize the payment. After that, they will automatically be redirected back to your website. You’ll get [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) on whether the payment succeeded or failed.

Assets such as logos and payment buttons are provided in the [branding guidelines](https://docs.stripe.com/payments/grabpay.md#branding-guidelines) section.

## Determine compatibility

A Checkout Session must satisfy all of the following conditions to support GrabPay payments:

- *Prices* (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) for all line items must be in the same currency. If you have line items in different currencies, create separate Checkout Sessions for each currency.
- You can only use one-time line items (recurring *subscription* (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) plans aren’t supported).
- The `sgd` currency is supported for businesses based in Singapore.
- The `myr` currency is supported for businesses based in Malaysia.

## Accept a payment

> This guide builds on the foundational [accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?integration=checkout) Checkout integration.

This guides you through enabling GrabPay and shows the differences between accepting payments using dynamic payment methods and manually configuring payment methods.

### Enable GrabPay as a payment method

When creating a new [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md), you need to:

1. Add `grabpay` to the list of `payment_method_types`.
1. Make sure all your `line_items` use the same currency.

#### Stripe-hosted page

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        currency: "sgd",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "grabpay"],
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
        currency: "sgd",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "grabpay"],
  return_url: "https://example.com/return",
  ui_mode: "embedded_page",
});
```

### Fulfill your orders

After accepting a payment, learn how to [fulfill orders](https://docs.stripe.com/checkout/fulfillment.md).

## Test your integration

When testing your Checkout integration, select GrabPay as the payment method and click the **Pay** button.

## See also

- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment.md)
- [Customizing Checkout](https://docs.stripe.com/payments/checkout/customization.md)

# iOS

> This is a iOS for when payment-ui is mobile and platform is ios. View the full page at https://docs.stripe.com/payments/grabpay/accept-a-payment?payment-ui=mobile&platform=ios.

GrabPay is a [single-use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method. Customers pay with GrabPay by redirecting from your app to GrabPay, authorizing the payment, then returning to your app where you get [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) on whether the payment succeeded or failed.

> Learn more about [activating GrabPay in the Dashboard](https://support.stripe.com/questions/grabpay-availability-and-getting-started).

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

Create a `PaymentIntent` on your server and specify the `amount` to collect and `sgd` or `myr` as the currency. There is no minimum charge amount for GrabPay so the payment amount can be as low as 1. If you have an existing [Payment Intents](https://docs.stripe.com/payments/payment-intents.md) integration, add `grabpay` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["grabpay"],
  amount: 1099,
  currency: "sgd",
});
```

### Client-side

On the client, request a PaymentIntent from your server and store its *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)).

#### Swift

```swift
class CheckoutViewController: UIViewController {
    var paymentIntentClientSecret: String?

    func startCheckout() {
        // Request a PaymentIntent from your server and store its client secret
    }
}
```

## Redirect to the GrabPay Wallet [Client-side]

Follow the [branding guidelines](https://d37ugbyn3rpeym.cloudfront.net/docs/files/GrabPay_Online_Partners_Brand_Guidelines.pdf) and use the [GrabPay assets](https://d37ugbyn3rpeym.cloudfront.net/docs/files/GrabPay-Branding-Guidelines-with-Logos-and-Artworks.zip) when building your checkout page. The iOS SDK presents a webview in your app to complete the GrabPay payment. When authentication is finished, the webview can automatically dismiss itself instead of having your customer close it. To enable this behavior, configure a [custom URL scheme](https://developer.apple.com/documentation/xcode/allowing_apps_and_websites_to_link_to_your_content/defining_a_custom_url_scheme_for_your_app) or [universal link](https://developer.apple.com/documentation/xcode/allowing_apps_and_websites_to_link_to_your_content) and set up your app delegate to forward the URL to the SDK.

#### SceneDelegate

#### Swift

```swift
// This method handles opening custom URL schemes (for example, "your-app://stripe-redirect")
func scene(_ scene: UIScene, openURLContexts URLContexts: Set<UIOpenURLContext>) {
    guard let url = URLContexts.first?.url else {
        return
    }
    let stripeHandled = StripeAPI.handleURLCallback(with: url)
    if (!stripeHandled) {
        // This was not a Stripe url – handle the URL normally as you would
    }
}

```

#### AppDelegate

#### Swift

```swift
// This method handles opening custom URL schemes (for example, "your-app://stripe-redirect")
func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey: Any] = [:]) -> Bool {
    let stripeHandled = StripeAPI.handleURLCallback(with: url)
    if (stripeHandled) {
        return true
    } else {
        // This was not a Stripe url – handle the URL normally as you would
    }
    return false
}
```

When the customer chooses to pay with GrabPay, complete the payment by calling [STPPaymentHandler confirmPayment](<https://stripe.dev/stripe-ios/stripe-payments/Classes/STPPaymentHandler.html#/c:@M@StripePayments@objc(cs)STPPaymentHandler(im)confirmPayment:withAuthenticationContext:completion:>). This presents a webview where the customer completes payment on the GrabPay website.

#### Swift

```swift
class CheckoutViewController: UIViewController, STPAuthenticationContext {
    func pay() {
        let clientSecret = ... // The client secret of the PaymentIntent created in step 2
        let grabPayParams = STPPaymentMethodGrabPayParams()
        let paymentMethodParams = STPPaymentMethodParams(grabPay: grabPayParams, billingDetails: nil, metadata: nil)
        let paymentIntentParams = STPPaymentIntentParams(clientSecret: clientSecret)
        paymentIntentParams.paymentMethodParams = paymentMethodParams
        paymentIntentParams.returnURL = "your-app://link"

        STPPaymentHandler.shared().confirmPayment(paymentIntentParams,
                                                  with: self)
        { (handlerStatus, paymentIntent, error) in
            switch handlerStatus {
            case .succeeded:
                // Payment succeeded
                // ...
            case .canceled:
                // Payment canceled
                // ...

            case .failed:
                // Payment failed
                // ...

            @unknown default:
                fatalError()
            }
        }
    }

    func authenticationPresentingViewController() -> UIViewController {
        return self
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

## Supported currencies

Stripe users in Malaysia and Singapore can accept GrabPay payments from customers in Malaysia and Singapore respectively. Review the supported currencies and GrabPay transaction limits below:

| Country        | Customer country                               | Supported currency | Transaction limits                                                                                                         |
| -------------- | ---------------------------------------------- | ------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| Singapore (SG) | [Singapore (SG)](https://www.grab.com/sg/pay/) | SGD                | [GrabPay SG](https://help.grab.com/passenger/en-sg/360023805451)                                                           |
| Malaysia (MY)  | [Malaysia (MY)](https://www.grab.com/my/pay/)  | MYR                | [GrabPay MY](https://help.grab.com/passenger/en-my/360023805451-What-are-my-GrabPay-Wallet-balance-and-transaction-limits) |

# Android

> This is a Android for when payment-ui is mobile and platform is android. View the full page at https://docs.stripe.com/payments/grabpay/accept-a-payment?payment-ui=mobile&platform=android.

GrabPay is a [single-use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method. Customers pay with GrabPay by redirecting from your app to GrabPay, authorizing the payment, then returning to your app where you get [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) on whether the payment succeeded or failed.

> Learn more about [activating GrabPay in the Dashboard](https://support.stripe.com/questions/grabpay-availability-and-getting-started).

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

## Create a PaymentIntent [Server-side] [Client-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) represents your intent to collect payment from a customer and tracks the lifecycle of the payment process.

### Server-side

Create a `PaymentIntent` on your server and specify the `amount` to collect and `sgd` or `myr` as the currency. There is no minimum charge amount for GrabPay so the payment amount can be as low as 1. If you have an existing [Payment Intents](https://docs.stripe.com/payments/payment-intents.md) integration, add `grabpay` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["grabpay"],
  amount: 1099,
  currency: "sgd",
});
```

### Client-side

On the client, request a PaymentIntent from your server and store its client secret.

#### Kotlin

```kotlin
class GrabPayActivity : AppCompatActivity() {
    private lateinit var paymentIntentClientSecret: String

    override fun onCreate(savedInstanceState: Bundle?) {
        // ...
        fetchPaymentIntent()
    }

  private fun fetchPaymentIntent() {
      // Request a PaymentIntent from your server and store its client secret
  }
}
```

## Collect billing details [Client-side]

Follow the [branding guidelines](https://d37ugbyn3rpeym.cloudfront.net/docs/files/GrabPay_Online_Partners_Brand_Guidelines.pdf) and use the [GrabPay assets](https://d37ugbyn3rpeym.cloudfront.net/docs/files/GrabPay-Branding-Guidelines-with-Logos-and-Artworks.zip) when building your checkout page. In your app, collect your customer’s full name and create a [PaymentMethodCreateParams](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-payment-method-create-params/index.html) with these details.

#### Kotlin

```kotlin
private fun startCheckout() {
    // ...

    val billingDetails = PaymentMethod.BillingDetails(name = "Jenny Rosen")
    val paymentMethodCreateParams = PaymentMethodCreateParams.createGrabPay(billingDetails)
}
```

## Submit the payment to Stripe [Client-side]

Retrieve the client secret from the PaymentIntent you created and call [PaymentLauncher confirm](https://stripe.dev/stripe-android/payments-core/com.stripe.android.payments.paymentlauncher/-payment-launcher/index.html#74063765%2FFunctions%2F-1622557690). This presents a webview where the customer can complete the payment. Afterwards, onPaymentResult is called with the result of the payment.

#### Kotlin

```kotlin
class GrabPayPaymentActivity : AppCompatActivity() {
    // ...
    private lateinit var paymentIntentClientSecret: String
    private val paymentLauncher: PaymentLauncher by lazy {
        PaymentLauncher.Companion.create(
            this,
            PaymentConfiguration.getInstance(applicationContext).publishableKey
            PaymentConfiguration.getInstance(applicationContext).stripeAccountId
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
        val message = when (paymentResult) {
            is PaymentResult.Completed -> {
                "Completed!"
            }
            is PaymentResult.Canceled -> {
                "Canceled!"
            }
            is PaymentResult.Failed -> {
                // This string comes from the PaymentIntent's error message.
                // See here: https://stripe.com/docs/api/payment_intents/object#payment_intent_object-last_payment_error-message
                "Failed: " + paymentResult.throwable.message
            }
            // do something with message
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

## Supported currencies

Stripe users in Malaysia and Singapore can accept GrabPay payments from customers in Malaysia and Singapore respectively. Review the supported currencies and GrabPay transaction limits below:

| Country        | Customer country                               | Supported currency | Transaction limits                                                                                                         |
| -------------- | ---------------------------------------------- | ------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| Singapore (SG) | [Singapore (SG)](https://www.grab.com/sg/pay/) | SGD                | [GrabPay SG](https://help.grab.com/passenger/en-sg/360023805451)                                                           |
| Malaysia (MY)  | [Malaysia (MY)](https://www.grab.com/my/pay/)  | MYR                | [GrabPay MY](https://help.grab.com/passenger/en-my/360023805451-What-are-my-GrabPay-Wallet-balance-and-transaction-limits) |

# React Native

> This is a React Native for when payment-ui is mobile and platform is react-native. View the full page at https://docs.stripe.com/payments/grabpay/accept-a-payment?payment-ui=mobile&platform=react-native.

GrabPay is a [single-use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method. Customers pay with GrabPay by redirecting from your app to GrabPay, authorizing the payment, then returning to your app where you get [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) on whether the payment succeeded or failed.

> Learn more about [activating GrabPay in the Dashboard](https://support.stripe.com/questions/grabpay-availability-and-getting-started).

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

## Create a PaymentIntent [Server-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) represents your intent to collect payment from a customer and tracks the lifecycle of the payment process.

### Server-side

Create a `PaymentIntent` on your server and specify the `amount` to collect and `sgd` or `myr` as the currency. There is no minimum charge amount for GrabPay so the payment amount can be as low as 1. If you have an existing [Payment Intents](https://docs.stripe.com/payments/payment-intents.md) integration, add `grabpay` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["grabpay"],
  amount: 1099,
  currency: "sgd",
});
```

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
      currency: "sgd",
      payment_method_types: ["grabpay"],
    }),
  });
  const { clientSecret, error } = await response.json();

  return { clientSecret, error };
};
```

## Collect billing details [Client-side]

Follow the [branding guidelines](https://d37ugbyn3rpeym.cloudfront.net/docs/files/GrabPay_Online_Partners_Brand_Guidelines.pdf) and use the [GrabPay assets](https://d37ugbyn3rpeym.cloudfront.net/docs/files/GrabPay-Branding-Guidelines-with-Logos-and-Artworks.zip) when building your checkout page. In your app, collect your customer’s full name.

```javascript
export default function GrabPayPaymentScreen() {
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

## Redirect to the GrabPay wallet [Client-side]

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

## Submit the payment to Stripe [Client-side]

Retrieve the client secret from the PaymentIntent you created and call `confirmPayment`. This presents a webview where the customer can authenticate the payment on GrabPay’s website or app. Afterwards, the promise resolves with the result of the payment.

```javascript
export default function GrabPayPaymentScreen() {
  const [name, setName] = useState();

  const handlePayPress = async () => {
    const billingDetails: PaymentMethodCreateParams.BillingDetails = {
      name,
    };
  };

  const { error, paymentIntent } = await confirmPayment(clientSecret, {
    paymentMethodType: 'GrabPay',
    paymentMethodData: {
      billingDetails
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
        placeholder="Name"
        onChange={(value) => setName(value.nativeEvent.text)}
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

## Supported currencies

Stripe users in Malaysia and Singapore can accept GrabPay payments from customers in Malaysia and Singapore respectively. Review the supported currencies and GrabPay transaction limits below:

| Country        | Customer country                               | Supported currency | Transaction limits                                                                                                         |
| -------------- | ---------------------------------------------- | ------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| Singapore (SG) | [Singapore (SG)](https://www.grab.com/sg/pay/) | SGD                | [GrabPay SG](https://help.grab.com/passenger/en-sg/360023805451)                                                           |
| Malaysia (MY)  | [Malaysia (MY)](https://www.grab.com/my/pay/)  | MYR                | [GrabPay MY](https://help.grab.com/passenger/en-my/360023805451-What-are-my-GrabPay-Wallet-balance-and-transaction-limits) |

# Direct API

> This is a Direct API for when payment-ui is direct-api. View the full page at https://docs.stripe.com/payments/grabpay/accept-a-payment?payment-ui=direct-api.

GrabPay is a [single-use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method. Customers pay with GrabPay by redirecting from your app to GrabPay, authorizing the payment, then returning to your app where you get [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) on whether the payment succeeded or failed.

> Learn more about [activating GrabPay in the Dashboard](https://support.stripe.com/questions/grabpay-availability-and-getting-started).

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

Create a `PaymentIntent` on your server and specify the `amount` to collect and `sgd` or `myr` as the currency. There is no minimum charge amount for GrabPay so the payment amount can be as low as 1. If you have an existing [Payment Intents](https://docs.stripe.com/payments/payment-intents.md) integration, add `grabpay` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["grabpay"],
  amount: 1099,
  currency: "sgd",
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

## Submit the payment to Stripe [Client-side]

When a customer clicks to pay with GrabPay, use Stripe.js to submit the payment to Stripe. [Stripe.js](https://docs.stripe.com/payments/elements.md) is the foundational JavaScript library for building payment flows. It automatically handles complexities like the redirect described below, and enables you to extend your integration to other payment methods. Include the Stripe.js script on your checkout page by adding it to the `head` of your HTML file.

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

To create a payment on the client side, add a [Pay with GrabPay button](https://docs.stripe.com/payments/grabpay.md#branding-guidelines) and use `stripe.confirmGrabPayPayment` to handle the redirect away from your page and to complete the payment.

```html
<button type="button" id="grabpay-button">Pay with GrabPay</button>
<div id="error-message"></div>
```

```javascript
const button = document.getElementById("grabpay-button");

button.addEventListener("click", async function () {
  // By this point, the PaymentIntent should have already been created
  // Pass the clientSecret of the PaymentIntent to confirmGrabPayPayment

  stripe.confirmGrabPayPayment(clientSecret, {
    // Return URL where the customer should be redirected after the authorization
    return_url: "https://example.com/checkout/complete",
  });
});
```

Pass the [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) of the `PaymentIntent` object that you created in Step 2 to `stripe.confirmGrabPayPayment`.

Additionally, add a `return_url` to this function to indicate where Stripe should redirect the user after they complete the payment on Grab’s website.

When your customer submits a payment, Stripe redirects them to the `return_url` and includes the following URL query parameters. The return page can use them to get the status of the PaymentIntent so it can display the payment status to the customer.

When you specify the `return_url`, you can also append your own query parameters for use on the return page.

| Parameter                      | Description                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_intent`               | The unique identifier for the `PaymentIntent`.                                                                                                                                                                                                                                                                                                             |
| `payment_intent_client_secret` | The [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) of the `PaymentIntent` object. For subscription integrations, this client_secret is also exposed on the `Invoice` object through [`confirmation_secret`](https://docs.stripe.com/api/invoices/object.md#invoice_object-confirmation_secret) |

When the customer is redirected back to your site, you can use the `payment_intent_client_secret` to query for the PaymentIntent and display the transaction status to your customer.

```html
<h2>Payment result</h2>
<div class="payment-result"></div>

<script>
  // Check if we're returning from a redirect.
  const url = new URL(window.location.href);
  const paymentIntentClientSecret = url.searchParams.get(
    "paymentIntentClientSecret",
  );
  if (paymentIntentClientSecret) {
    stripe
      .retrievePaymentIntent(paymentIntentClientSecret)
      .then(function (result) {
        const paymentIntent = result.paymentIntent;
        document.querySelector(".payment-result").textContent =
          paymentIntent.status;
      });
  }
</script>
```

## Test your integration

When testing, the client side redirect brings you to a Stripe-hosted GrabPay test payment page where you can either authorize or fail the test payment.

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

## Optional: Handle the GrabPay redirect manually

We recommend relying on Stripe.js to handle GrabPay redirects and payments with `confirmGrabPayPayment`. However, you can also manually redirect your customers by:

1. Providing the URL where your customers will be redirected after they complete their payment.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.confirm(
  "{{PAYMENT_INTENT_ID}}",
  {
    return_url: "https://example.com/checkout/complete",
    payment_method_data: {
      type: "grabpay",
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
  "payment_method_types": ["grabpay"],
  "id": "pi_1G1sgdKi6xqXeNtkldRRE6HT",
  "object": "payment_intent",
  "amount": 1099,
  "confirmation_method": "automatic",
  "created": 1579259303,
  "currency": "sgd",
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

## Supported currencies

Stripe users in Malaysia and Singapore can accept GrabPay payments from customers in Malaysia and Singapore respectively. Review the supported currencies and GrabPay transaction limits below:

| Country        | Customer country                               | Supported currency | Transaction limits                                                                                                         |
| -------------- | ---------------------------------------------- | ------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| Singapore (SG) | [Singapore (SG)](https://www.grab.com/sg/pay/) | SGD                | [GrabPay SG](https://help.grab.com/passenger/en-sg/360023805451)                                                           |
| Malaysia (MY)  | [Malaysia (MY)](https://www.grab.com/my/pay/)  | MYR                | [GrabPay MY](https://help.grab.com/passenger/en-my/360023805451-What-are-my-GrabPay-Wallet-balance-and-transaction-limits) |
