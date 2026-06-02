<!-- Source URL: https://docs.stripe.com/payments/alipay/accept-a-payment -->
<!-- Fetched: 2026-05-07 -->

# Accept an Alipay payment

Learn how to accept Alipay payments, a digital wallet popular with customers from China.

# Checkout

> This is a Checkout for when payment-ui is checkout. View the full page at https://docs.stripe.com/payments/alipay/accept-a-payment?payment-ui=checkout.

> Stripe can automatically present the relevant payment methods to your customers by evaluating currency, payment method restrictions, and other parameters.
>
> - Follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=checkout&ui=stripe-hosted) guide to build a Checkout integration that uses [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md).

- If you don’t want to use dynamic payment methods, follow the steps below to manually configure the payment methods in your Checkout integration.

Alipay is a [single-use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method where customers are required to [authenticate](https://docs.stripe.com/payments/payment-methods.md#customer-actions) their payment. Customers pay by redirecting from your website or app, authorize the payment through Alipay, then return to your website or app where you get [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) on whether the payment succeeded or failed.

## Determine Compatibility

**Customer Geography**: China

**Supported currencies**: `aud, cad, eur, gbp, hkd, jpy, nzd, sgd, usd, myr`

**Presentment currencies**: `aud, cad, cny, eur, gbp, hkd, jpy, nzd, sgd, usd, myr`

**Payment mode**: Yes

**Setup mode**: No

**Subscription mode**: No

To support Alipay payments, a Checkout Session must satisfy all of the following conditions:

- *Prices* (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) for all line items must be in the same currency.
  - If you have line items in different currencies, create separate Checkout Sessions for each currency.
- You can only use one-time line items.

Recurring *subscription* (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) plans aren’t supported.

## Accept a payment

> Build an integration to [accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?integration=checkout) with Checkout before using this guide.

This guides you through enabling Alipay and shows the differences between accepting payments using dynamic payment methods and manually configuring payment methods.

### Enable Alipay as a payment method

When creating a new [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md), you need to:

1. Add `alipay` to the list of `payment_method_types`.
1. Make sure all `line_items` use the same currency.

#### Stripe-hosted page

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        currency: "hkd",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "alipay"],
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
        currency: "hkd",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "alipay"],
  return_url: "https://example.com/return",
  ui_mode: "embedded_page",
});
```

### Fulfill your orders

After accepting a payment, learn how to [fulfill orders](https://docs.stripe.com/checkout/fulfillment.md).

## Test your integration

When testing your Checkout integration, select Alipay as the payment method and click the **Pay** button.

## Handle refunds and disputes

The refund period for Alipay is up to 90 days after the original payment.

Alipay has no dispute process—customers authenticate with their Alipay account.

## See also

- [More about Alipay](https://docs.stripe.com/payments/alipay.md)
- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment.md)
- [Customizing Checkout](https://docs.stripe.com/payments/checkout/customization.md)

# iOS

> This is a iOS for when payment-ui is mobile and platform is ios. View the full page at https://docs.stripe.com/payments/alipay/accept-a-payment?payment-ui=mobile&platform=ios.

Alipay is a [single-use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method where customers are required to [authenticate](https://docs.stripe.com/payments/payment-methods.md#customer-actions) their payment. Customers pay by redirecting from your website or app, authorize the payment through Alipay, then return to your website or app where you get [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) on whether the payment succeeded or failed.

## Set up Stripe [Client-side] [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

### Server-side

This integration requires endpoints on your server that talk to the Stripe API. Use our official libraries for access to the Stripe API from your server:

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

## Create a PaymentIntent [Server-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) is an object that represents your intent to collect payment from your customer and tracks the lifecycle of the payment process. Create a `PaymentIntent` on your server and specify the amount to collect and a [supported currency](https://docs.stripe.com/payments/alipay.md#supported-currencies). If you have an existing [Payment Intents](https://docs.stripe.com/payments/payment-intents.md) integration, add `alipay` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["alipay"],
  amount: 1099,
  currency: "hkd",
});
```

## Redirect to the Alipay Wallet [Client-side]

[Register a custom URL scheme for your app](https://developer.apple.com/documentation/xcode/defining-a-custom-url-scheme-for-your-app) by going to the Info tab of your app target settings.
![Setting up a custom URL scheme in Xcode](assets/stripe-alipay-ios-custom-url-scheme.png)

The Alipay app opens this URL to return to your app after the customer completes the payment. Forward the URL to the Stripe SDK in your `UISceneDelegate` or `UIApplicationDelegate`:

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

When the customer taps to pay with Alipay, confirm the PaymentIntent using [STPPaymentHandler confirmPayment](<https://stripe.dev/stripe-ios/stripe-payments/Classes/STPPaymentHandler.html#/c:@M@StripePayments@objc(cs)STPPaymentHandler(im)confirmPayment:withAuthenticationContext:completion:>). This launches the Alipay app or displays a webview if the Alipay app isn’t installed.

#### Swift

```swift
import UIKit
import StripePayments

class CheckoutViewController: UIViewController {
    // ...
    func pay() {
        let clientSecret = ... // The client secret of the PaymentIntent
        let paymentIntentParams = STPPaymentIntentParams(clientSecret: clientSecret)
        paymentIntentParams.paymentMethodParams = STPPaymentMethodParams(alipay: STPPaymentMethodAlipayParams(), billingDetails: nil, metadata: nil)
        paymentIntentParams.paymentMethodOptions = STPConfirmPaymentMethodOptions()
        paymentIntentParams.paymentMethodOptions?.alipayOptions = STPConfirmAlipayOptions()
        paymentIntentParams.returnURL = "{{URL SCHEME}}://safepay/" // Replace {{URL SCHEME}} with your own custom URL scheme.

        STPPaymentHandler.shared().confirmPayment(paymentIntentParams, with: self) { (status, intent, error) in
            switch status {
                case .canceled:
                    // Payment was canceled
                case .failed:
                    // Payment failed
                case .succeeded:
                    // Payment was successful
                @unknown default:
                    fatalError()
            }
        }
    }
}

extension CheckoutViewController: STPAuthenticationContext {
    func authenticationPresentingViewController() -> UIViewController {
        return self
    }
}
```

Alipay opens the return URL with `safepay/` as the host. For example, if your custom URL scheme is `myapp`, your return URL must be `myapp://safepay/`.

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

Your account must have a bank account for one of the following currencies. You can create Alipay payments in the currencies that map to your country. The default local currency for Alipay is `cny` and customers also see their purchase amount in `cny`.

| Currency | Country                                                                                                                                                                                                                                              |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cny`    | Any country                                                                                                                                                                                                                                          |
| `aud`    | Australia                                                                                                                                                                                                                                            |
| `cad`    | Canada                                                                                                                                                                                                                                               |
| `eur`    | Austria, Belgium, Bulgaria, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Greece, Ireland, Italy, Latvia, Lithuania, Luxembourg, Malta, Netherlands, Norway, Portugal, Romania, Slovakia, Slovenia, Spain, Sweden, Switzerland |
| `gbp`    | United Kingdom                                                                                                                                                                                                                                       |
| `hkd`    | Hong Kong                                                                                                                                                                                                                                            |
| `jpy`    | Japan                                                                                                                                                                                                                                                |
| `myr`    | Malaysia                                                                                                                                                                                                                                             |
| `nzd`    | New Zealand                                                                                                                                                                                                                                          |
| `sgd`    | Singapore                                                                                                                                                                                                                                            |
| `usd`    | United States                                                                                                                                                                                                                                        |

If you have a bank account in another currency and want to create an Alipay payment in that currency, you can [contact support](https://support.stripe.com/email). We provide support for additional currencies on a case-by-case basis.

# Android

> This is a Android for when payment-ui is mobile and platform is android. View the full page at https://docs.stripe.com/payments/alipay/accept-a-payment?payment-ui=mobile&platform=android.

Alipay is a [single-use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method where customers are required to [authenticate](https://docs.stripe.com/payments/payment-methods.md#customer-actions) their payment. Customers pay by redirecting from your website or app, authorize the payment through Alipay, then return to your website or app where you get [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) on whether the payment succeeded or failed.

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

## Integrate the Alipay SDK [Client-side]

For in-app payments using Alipay’s app-to-app redirect flow, you must integrate the [Alipay SDK](https://global.alipay.com/docs/ac/app/download). If you don’t want to integrate the Alipay SDK, the Stripe SDK uses a WebView to redirect customers to Alipay. Integrating the Alipay SDK provides a more seamless experience for your customers, but increases the overall size of your app. See [Use a WebView](https://docs.stripe.com/payments/alipay/accept-a-payment.md#android-use-webview) for more details.

After unzipping the archive, add `alipaySdk-{version}.aar` to the `libs` directory of your app. Add the `libs` folder to your project’s dependency repository list:

```groovy
allprojects {
  repositories {
    flatDir {
      dirs 'libs'
    }
  }
}
```

Add the dependency to your app:

```groovy
dependencies {
  // ...

  // Replace {version} with the version number of the Alipay SDK that you downloaded above
  implementation(name:"alipaySdk-{version}", ext:"aar")
}
```

## Create a PaymentIntent [Server-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) is an object that represents your intent to collect payment from your customer and tracks the lifecycle of the payment process. Create a `PaymentIntent` on your server and specify the amount to collect and a [supported currency](https://docs.stripe.com/payments/alipay.md#supported-currencies). If you have an existing [Payment Intents](https://docs.stripe.com/payments/payment-intents.md) integration, add `alipay` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["alipay"],
  amount: 1099,
  currency: "hkd",
});
```

## Redirect to the Alipay Wallet [Client-side]

Request a PaymentIntent from your server and store its client secret.

#### Kotlin

```kotlin
class AlipayActivity : AppCompatActivity() {
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

When the customer taps to pay with Alipay, confirm the PaymentIntent using Stripe `confirmAlipayPayment`. You must supply an AlipayAuthenticator to pass data from the Stripe SDK to the Alipay SDK. The authenticator calls the Alipay `payV2` method with the supplied data string. The Alipay SDK opens the Alipay app (if installed) or shows its own UI and communicates the result back to the Stripe SDK automatically.

> The Alipay Android SDK doesn’t support test payments. To fully test this integration, use [live mode](https://docs.stripe.com/keys.md#test-live-modes).

#### Kotlin

```kotlin
import com.alipay.sdk.app.PayTask

class AlipayActivity : AppCompatActivity() {
    // ...
    private lateinit var paymentIntentClientSecret: String
    private val stripe: Stripe by lazy {
        Stripe(
            applicationContext,
            PaymentConfiguration.getInstance(applicationContext).publishableKey
        )
    }

    // Call this function when the customer taps "Pay with Alipay"
    private fun startCheckout() {
        // ...
        lifecycleScope.launch {
            runCatching {
                stripe.confirmAlipayPayment(
                    ConfirmPaymentIntentParams.createAlipay(paymentIntentClientSecret),
                    { data -> PayTask(this@AlipayActivity).payV2(data, true) }
                )
            }.fold(
                onSuccess = { result ->
                    val paymentIntent = result.intent
                    val status = paymentIntent.status
                    when (status) {
                        StripeIntent.Status.Succeeded -> {
                            // Payment succeeded
                        }
                        StripeIntent.Status.RequiresAction -> {
                            // Customer didn't complete the payment
                            // You can try to confirm this Payment Intent again
                        }
                        else -> {
                            // Payment failed/canceled
                        }
                    }
                },
                onFailure = {
                    // Payment failed
                }
            )
        }
    }
}
```

## Optional: Use a WebView [Client-side]

If you don’t want to integrate the Alipay SDK, the Stripe SDK can redirect the customer to an Alipay WebView when you call `confirmPayment`. The Alipay website opens the Alipay app (if installed) or allows the customer to complete the payment on the web.

#### Kotlin

```kotlin
class AlipayActivity : AppCompatActivity() {
    // ...
    private lateinit var paymentIntentClientSecret: String
    private val stripe: Stripe by lazy {
        Stripe(
          applicationContext,
          PaymentConfiguration.getInstance(applicationContext).publishableKey
        )
    }

    // Call this method when the customer taps "Pay with Alipay"
    private fun startCheckout() {
        // ...

        val confirmParams = ConfirmPaymentIntentParams.createAlipay(paymentIntentClientSecret)
        stripe.confirmPayment(this, confirmParams)
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)

        // Handle the result of stripe.confirmPayment
        stripe.onPaymentResult(requestCode, data, object : ApiResultCallback<PaymentIntentResult> {
            override fun onSuccess(result: PaymentIntentResult) {
                val paymentIntent = result.intent
                val status = paymentIntent.status
                when (status) {
                    StripeIntent.Status.Succeeded -> {
                        // Payment succeeded
                    }
                    StripeIntent.Status.RequiresAction -> {
                        // Customer didn't complete the payment
                        // You can try to confirm this Payment Intent again
                    }
                    else -> {
                        // Payment failed/canceled
                    }
                }
            }

            override fun onError(e: Exception) {
                // Payment failed
            }
        })
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

Your account must have a bank account for one of the following currencies. You can create Alipay payments in the currencies that map to your country. The default local currency for Alipay is `cny` and customers also see their purchase amount in `cny`.

| Currency | Country                                                                                                                                                                                                                                              |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cny`    | Any country                                                                                                                                                                                                                                          |
| `aud`    | Australia                                                                                                                                                                                                                                            |
| `cad`    | Canada                                                                                                                                                                                                                                               |
| `eur`    | Austria, Belgium, Bulgaria, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Greece, Ireland, Italy, Latvia, Lithuania, Luxembourg, Malta, Netherlands, Norway, Portugal, Romania, Slovakia, Slovenia, Spain, Sweden, Switzerland |
| `gbp`    | United Kingdom                                                                                                                                                                                                                                       |
| `hkd`    | Hong Kong                                                                                                                                                                                                                                            |
| `jpy`    | Japan                                                                                                                                                                                                                                                |
| `myr`    | Malaysia                                                                                                                                                                                                                                             |
| `nzd`    | New Zealand                                                                                                                                                                                                                                          |
| `sgd`    | Singapore                                                                                                                                                                                                                                            |
| `usd`    | United States                                                                                                                                                                                                                                        |

If you have a bank account in another currency and want to create an Alipay payment in that currency, you can [contact support](https://support.stripe.com/email). We provide support for additional currencies on a case-by-case basis.

# React Native

> This is a React Native for when payment-ui is mobile and platform is react-native. View the full page at https://docs.stripe.com/payments/alipay/accept-a-payment?payment-ui=mobile&platform=react-native.

Alipay is a [single-use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method where customers are required to [authenticate](https://docs.stripe.com/payments/payment-methods.md#customer-actions) their payment. Customers pay by redirecting from your website or app, authorize the payment through Alipay, then return to your website or app where you get [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) on whether the payment succeeded or failed.

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

A [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) is an object that represents your intent to collect payment from your customer and tracks the lifecycle of the payment process. Create a `PaymentIntent` on your server and specify the amount to collect and a [supported currency](https://docs.stripe.com/payments/alipay.md#supported-currencies). If you have an existing [Payment Intents](https://docs.stripe.com/payments/payment-intents.md) integration, add `alipay` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["alipay"],
  amount: 1099,
  currency: "hkd",
});
```

## Redirect to the Alipay wallet [Client-side]

The Stripe React Native SDK specifies `safepay/` as the return URL host for bank redirect and digital wallet payment methods. After the customer completes their payment with Alipay, they’re redirected to `myapp://safepay/`, where `myapp` is your custom URL scheme.

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

## Confirm the payment [Client-side]

When the customer taps to pay with Alipay, call `confirmPayment` to present a webview where they can complete the payment.

```javascript
export default function AlipayPaymentScreen() {
  const [email, setEmail] = useState("");
  const { confirmPayment, loading } = useConfirmPayment();

  const handlePayPress = async () => {
    const { clientSecret } = await fetchPaymentIntentClientSecret();

    const { error, paymentIntent } = await confirmPayment(clientSecret, {
      paymentMethodType: "Alipay",
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

  return (
    <Screen>
      <TextInput
        placeholder="E-mail"
        keyboardType="email-address"
        onChange={(value) => setEmail(value.nativeEvent.text)}
      />
      <Button
        variant="primary"
        onPress={handlePayPress}
        title="Pay"
        loading={loading}
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

Your account must have a bank account for one of the following currencies. You can create Alipay payments in the currencies that map to your country. The default local currency for Alipay is `cny` and customers also see their purchase amount in `cny`.

| Currency | Country                                                                                                                                                                                                                                              |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cny`    | Any country                                                                                                                                                                                                                                          |
| `aud`    | Australia                                                                                                                                                                                                                                            |
| `cad`    | Canada                                                                                                                                                                                                                                               |
| `eur`    | Austria, Belgium, Bulgaria, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Greece, Ireland, Italy, Latvia, Lithuania, Luxembourg, Malta, Netherlands, Norway, Portugal, Romania, Slovakia, Slovenia, Spain, Sweden, Switzerland |
| `gbp`    | United Kingdom                                                                                                                                                                                                                                       |
| `hkd`    | Hong Kong                                                                                                                                                                                                                                            |
| `jpy`    | Japan                                                                                                                                                                                                                                                |
| `myr`    | Malaysia                                                                                                                                                                                                                                             |
| `nzd`    | New Zealand                                                                                                                                                                                                                                          |
| `sgd`    | Singapore                                                                                                                                                                                                                                            |
| `usd`    | United States                                                                                                                                                                                                                                        |

If you have a bank account in another currency and want to create an Alipay payment in that currency, you can [contact support](https://support.stripe.com/email). We provide support for additional currencies on a case-by-case basis.

# Direct API

> This is a Direct API for when payment-ui is direct-api. View the full page at https://docs.stripe.com/payments/alipay/accept-a-payment?payment-ui=direct-api.

Alipay is a [single-use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method where customers are required to [authenticate](https://docs.stripe.com/payments/payment-methods.md#customer-actions) their payment. Customers pay by redirecting from your website or app, authorize the payment through Alipay, then return to your website or app where you get [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) on whether the payment succeeded or failed.

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create a PaymentIntent [Server-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) is an object that represents your intent to collect payment from your customer and tracks the lifecycle of the payment process. Create a `PaymentIntent` on your server and specify the amount to collect and a [supported currency](https://docs.stripe.com/payments/alipay.md#supported-currencies). If you have an existing [Payment Intents](https://docs.stripe.com/payments/payment-intents.md) integration, add `alipay` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["alipay"],
  amount: 1099,
  currency: "hkd",
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

## Redirect to the Alipay Wallet [Client-side]

When a customer clicks to pay with Alipay, use Stripe.js to submit the payment to Stripe. [Stripe.js](https://docs.stripe.com/payments/elements.md) is the foundational JavaScript library for building payment flows. It automatically handles complexities like the redirect described below, and enables you to extend your integration to other payment methods. Include the Stripe.js script on your checkout page by adding it to the `head` of your HTML file.

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

Use the [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) of the `PaymentIntent` and call `stripe.confirmAlipayPayment` to handle the Alipay redirect. Add a `return_url` to determine where Stripe redirects the customer after they complete the payment.

```javascript
const form = document.getElementById("payment-form");

form.addEventListener("submit", async function (event) {
  event.preventDefault();

  // Set the clientSecret of the PaymentIntent
  const { error } = await stripe.confirmAlipayPayment(clientSecret, {
    // Return URL where the customer should be redirected after the authorization
    return_url: `${window.location.href}`,
  });

  if (error) {
    // Inform the customer that there was an error.
    const errorElement = document.getElementById("error-message");
    errorElement.textContent = error.message;
  }
});
```

The `return_url` corresponds to a page on your website that displays the result of the payment. You can determine what to display by [verifying the status](https://docs.stripe.com/payments/payment-intents/verifying-status.md#checking-status) of the `PaymentIntent`. To verify the status, the Stripe redirect to the `return_url` includes the following URL query parameters. You can also append your own query parameters to the `return_url`. They persist throughout the redirect process.

| Parameter                      | Description                                                                                                                                   |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_intent`               | The unique identifier for the `PaymentIntent`.                                                                                                |
| `payment_intent_client_secret` | The [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) of the `PaymentIntent` object. |

## Optional: Handle the redirect manually [Server-side]

The best way to handle redirects is to use Stripe.js with `confirmAlipayPayment`. If you need to manually redirect your customers:

1. Provide the URL to redirect your customers to after they complete their payment.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.confirm(
  "pi_1DRuHnHgsMRlo4MtwuIAUe6u",
  {
    payment_method: "pm_1EnPf7AfTbPYpBIFLxIc8SD9",
    return_url: "https://shop.example.com/crtA6B28E1",
  },
);
```

1. Confirm the `PaymentIntent` has a status of `requires_action`. The type for the `next_action` will be `alipay_handle_redirect`.

```json
"next_action": {
  "type": "alipay_handle_redirect",
  "alipay_handle_redirect": {
    "url": "https://hooks.stripe.com/...",
    "return_url": "https://example.com/checkout/complete"
  }
}
```

1. Redirect the customer to the URL provided in the `next_action` property.

When the customer finishes the payment process, they’re sent to the `return_url` destination. The `payment_intent` and `payment_intent_client_secret` URL query parameters are included and you can pass through your own query parameters, as described above.

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

Your account must have a bank account for one of the following currencies. You can create Alipay payments in the currencies that map to your country. The default local currency for Alipay is `cny` and customers also see their purchase amount in `cny`.

| Currency | Country                                                                                                                                                                                                                                              |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cny`    | Any country                                                                                                                                                                                                                                          |
| `aud`    | Australia                                                                                                                                                                                                                                            |
| `cad`    | Canada                                                                                                                                                                                                                                               |
| `eur`    | Austria, Belgium, Bulgaria, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Greece, Ireland, Italy, Latvia, Lithuania, Luxembourg, Malta, Netherlands, Norway, Portugal, Romania, Slovakia, Slovenia, Spain, Sweden, Switzerland |
| `gbp`    | United Kingdom                                                                                                                                                                                                                                       |
| `hkd`    | Hong Kong                                                                                                                                                                                                                                            |
| `jpy`    | Japan                                                                                                                                                                                                                                                |
| `myr`    | Malaysia                                                                                                                                                                                                                                             |
| `nzd`    | New Zealand                                                                                                                                                                                                                                          |
| `sgd`    | Singapore                                                                                                                                                                                                                                            |
| `usd`    | United States                                                                                                                                                                                                                                        |

If you have a bank account in another currency and want to create an Alipay payment in that currency, you can [contact support](https://support.stripe.com/email). We provide support for additional currencies on a case-by-case basis.
