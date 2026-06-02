<!-- Source URL: https://docs.stripe.com/payments/mobile/save-card-without-authentication -->
<!-- Fetched: 2026-04-23 -->

# Save a card without bank authentication

Collect card details in your mobile app and charge your customer at a later time.

# iOS

> This is a iOS for when platform is ios. View the full page at https://docs.stripe.com/payments/mobile/save-card-without-authentication?platform=ios.

​​Stripe allows you to collect card details and charge your customer at a later time. ​​In some regions, banks require a second form of authentication such as entering a code sent to a phone. ​​The extra step decreases conversion if your customer isn’t actively using your website or application because they aren’t available to authenticate the purchase.

​​If you primarily do business in the US and Canada, banks don’t require authentication, so you can follow this simpler integration. This integration will be non-compliant in countries that require authentication for saving cards (for example, India) so building this integration means that expanding to other countries or adding other payment methods will require significant changes. Learn how to [save cards that require authentication](https://docs.stripe.com/payments/save-and-reuse.md).

> #### Compliance
>
> You’re responsible for your compliance with all applicable laws, regulations, and network rules when saving a customer’s payment details. For instance, if you want to save their payment method for future use, such as charging them when they’re not actively using your website or app. Add terms to your website or app that state how you plan to save payment method details and allow customers to opt in. If you want to charge them when they’re offline, make sure your terms include the following:
>
> - The customer’s agreement to your initiating a payment or a series of payments on their behalf for specified transactions.

- The anticipated timing and frequency of payments (for example, if the charges are for scheduled installments, subscription payments, or unscheduled top-ups).
- How you determine the payment amount.
- Your cancellation policy, if the payment method is for a subscription service.
  > Make sure you keep a record of your customer’s written agreement to these terms.

## Set up Stripe [Server-side] [Client-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Set up the iOS and server Stripe SDKs before starting your integration.

### Server-side

This integration requires endpoints on your server that talk to the Stripe API. Use our official libraries:

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

## Collect card details [Client-side]

Start by displaying a payment form to your customer. Collect card details from the customer using [STPPaymentCardTextField](https://stripe.dev/stripe-ios/stripe-payments-ui/Classes/STPPaymentCardTextField.html), a drop-in UI component provided by the SDK that collects the card number, expiration date, CVC, and postal code.
![](assets/stripe-inapp-ios-card-field.mp4)
Pass the card details to [createPaymentMethod](<https://stripe.dev/stripe-ios/stripe-payments/Classes/STPAPIClient.html#/c:@CM@StripePayments@StripeCore@objc(cs)STPAPIClient(im)createPaymentMethodWithPayment:completion:>) to create a _PaymentMethod_ (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs).

#### Swift

```swift
class CheckoutViewController: UIViewController {
    lazy var cardTextField: STPPaymentCardTextField = {
        let cardTextField = STPPaymentCardTextField()
        return cardTextField
    }()

    @objc
    func pay() {
        // Collect card details on the client
        STPAPIClient.shared.createPaymentMethod(with: cardTextField.paymentMethodParams) { [weak self] paymentMethod, error in
            guard let paymentMethod = paymentMethod else {
                // Display the error to the user
                return
            }
            let paymentMethodId = paymentMethod.stripeId
            // Send paymentMethodId to your server for the next steps
        }
    }
}
```

Send the resulting PaymentMethod ID to your server and follow the remaining steps to save the card to a customer and charge the card in the future.

## Save the card [Server-side]

Save the card by attaching the PaymentMethod to a _Customer_ (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments). You can use the Customer object to store other information about your customer, such as shipping details and email address.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create({
  payment_method: "{{PAYMENT_METHOD_ID}}",
});
```

If you have an existing Customer, you can attach the PaymentMethod to that object instead.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethod = await stripe.paymentMethods.attach(
  "{{PAYMENT_METHOD_ID}}",
  {
    customer: "{{CUSTOMER_ID}}",
  },
);
```

At this point, associate the ID of the Customer object and the ID of the PaymentMethod with your own internal representation of a customer, if you have one.

## Charge the saved card [Server-side]

When you’re ready to charge the Customer, look up the PaymentMethod ID to charge. You can do this by either storing the IDs of both in your database, or by using the Customer ID to look up all the Customer’s available PaymentMethods.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethods = await stripe.paymentMethods.list({
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  type: "card",
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethods = await stripe.paymentMethods.list({
  customer: "{{CUSTOMER_ID}}",
  type: "card",
});
```

Use the PaymentMethod ID and the Customer ID to create a new PaymentIntent. Set [error_on_requires_action](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-error_on_requires_action) to true to decline payments that require any actions from your customer, such as two-factor authentication.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "usd",
  payment_method_types: ["card"],
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{PAYMENT_METHOD_ID}}",
  error_on_requires_action: true,
  confirm: true,
});
```

When a payment attempt fails, the request also fails with a 402 HTTP status code and Stripe throws an error. You need to notify your customer to return to your application (for example, by sending an in-app notification) to complete the payment. Check the code of the [Error](https://docs.stripe.com/api/errors/handling.md) raised by the Stripe API library or check the [last_payment_error.decline_code](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-last_payment_error-decline_code) on the PaymentIntent to inspect why the card issuer declined the payment.

## Handle any card errors

Notify your customer that the payment failed and direct them to the payment form you made in step 1 where they can enter new card details. Send that new PaymentMethod ID to your server to [attach](https://docs.stripe.com/api/payment_methods/attach.md) to the Customer object and make the payment again.

Alternatively, you can create a PaymentIntent and save a card in one API call if you already created a Customer.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "usd",
  payment_method_types: ["card"],
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{PAYMENT_METHOD_ID}}",
  error_on_requires_action: true,
  confirm: true,
  setup_future_usage: "on_session",
});
```

Setting [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) to `on_session` indicates to Stripe that you want to save the card for later, without triggering unnecessary authentication.

## Test the integration

Stripe provides [test cards](https://docs.stripe.com/testing.md) you can use in a sandbox to simulate the behavior of different cards. Use these cards with any CVC, postal code, and expiration date in the future.

| Number           | Description                                                                                           |
| ---------------- | ----------------------------------------------------------------------------------------------------- |
| 4242424242424242 | Succeeds and immediately processes the payment.                                                       |
| 4000000000009995 | Always fails with a decline code of `insufficient_funds`.                                             |
| 4000002500003155 | Requires authentication, which in this integration declines with a code of `authentication_required`. |

## Optional: Re-collect a CVC

When creating subsequent payments on a saved card, you might want to re-collect the CVC of the card as an additional fraud measure to verify the user.

Start by creating a PaymentIntent from your server with the amount and currency of the payment, and set [customer](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-customer) to the ID of your Customer. Then, [list](https://docs.stripe.com/api/payment_methods/list.md) the PaymentMethods associated with your Customer to determine which PaymentMethods to show to your user for CVC re-collection.

After re-collecting the customer’s CVC information, create an [STPConfirmCardOptions](https://stripe.dev/stripe-ios/stripe-payments/Classes/STPConfirmCardOptions.html) instance with the customer’s CVC. Use the `STPConfirmCardOptions` instance to configure the `cardOptions` property on an instance of [STPConfirmPaymentMethodOptions](https://stripe.dev/stripe-ios/stripe-payments/Classes/STPConfirmPaymentMethodOptions.html). Finally, confirm the PaymentIntent by creating a [STPPaymentIntentParams](https://stripe.dev/stripe-ios/stripe-payments/Classes/STPPaymentIntentParams.html) instance with the [STPConfirmPaymentMethodOptions](https://stripe.dev/stripe-ios/stripe-payments/Classes/STPConfirmPaymentMethodOptions.html) instance and passing it to [STPPaymentHandler confirmPayment](<https://stripe.dev/stripe-ios/stripe-payments/Classes/STPPaymentHandler.html#/c:@M@StripePayments@objc(cs)STPPaymentHandler(im)confirmPayment:withAuthenticationContext:completion:>).

#### Swift

```swift
import UIKit
import StripePaymentsUI

class CheckoutViewController: UIViewController {
    // ...
    @objc
    func pay() {
        guard let paymentIntentClientSecret = paymentIntentClientSecret,
            let cvc = cvc else {
                return
        }

        let paymentIntentParams = STPPaymentIntentParams(clientSecret: paymentIntentClientSecret)

        let cardOptions = STPConfirmCardOptions()
        cardOptions.cvc = cvc;
        let paymentMethodOptions = STPConfirmPaymentMethodOptions()
        paymentMethodOptions.cardOptions = cardOptions
        paymentIntentParams.paymentMethodOptions = paymentMethodOptions

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
}

extension CheckoutViewController: STPAuthenticationContext {
    func authenticationPresentingViewController() -> UIViewController {
        return self
    }
}
```

A payment might succeed even with a failed CVC check. To prevent this, configure your [Radar rules](https://docs.stripe.com/radar/rules.md#traditional-bank-checks) to block payments when CVC verification fails.

## Upgrade your integration to handle card authentication

This integration **declines cards that require authentication during payment**. If you start seeing many payments in the Dashboard listed as `Failed`, then it’s time to [upgrade your integration](https://docs.stripe.com/payments/payment-intents/upgrade-to-handle-actions.md). Stripe’s global integration handles these payments instead of automatically declining.

# Android

> This is a Android for when platform is android. View the full page at https://docs.stripe.com/payments/mobile/save-card-without-authentication?platform=android.

​​Stripe allows you to collect card details and charge your customer at a later time. ​​In some regions, banks require a second form of authentication such as entering a code sent to a phone. ​​The extra step decreases conversion if your customer isn’t actively using your website or application because they aren’t available to authenticate the purchase.

​​If you primarily do business in the US and Canada, banks don’t require authentication, so you can follow this simpler integration. This integration will be non-compliant in countries that require authentication for saving cards (for example, India) so building this integration means that expanding to other countries or adding other payment methods will require significant changes. Learn how to [save cards that require authentication](https://docs.stripe.com/payments/save-and-reuse.md).

> #### Compliance
>
> You’re responsible for your compliance with all applicable laws, regulations, and network rules when saving a customer’s payment details. For instance, if you want to save their payment method for future use, such as charging them when they’re not actively using your website or app. Add terms to your website or app that state how you plan to save payment method details and allow customers to opt in. If you want to charge them when they’re offline, make sure your terms include the following:
>
> - The customer’s agreement to your initiating a payment or a series of payments on their behalf for specified transactions.

- The anticipated timing and frequency of payments (for example, if the charges are for scheduled installments, subscription payments, or unscheduled top-ups).
- How you determine the payment amount.
- Your cancellation policy, if the payment method is for a subscription service.
  > Make sure you keep a record of your customer’s written agreement to these terms.

## Set up Stripe [Server-side] [Client-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Set up the Android and server Stripe SDKs before starting your integration.

### Server-side

This integration requires endpoints on your server that talk to the Stripe API. Use our official libraries for access to the Stripe API from your server:

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

## Collect card details [Client-side]

When the customer submits the payment form, collect their card details using [CardInputWidget](https://stripe.dev/stripe-android/payments-core/com.stripe.android.view/-card-input-widget/index.html), a drop-in UI component provided by the SDK that collects the card number, expiration date, CVC, and postal code.
![](assets/stripe-inapp-android-card-input.mp4)
Pass the card details to [createPaymentMethod](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-stripe/create-payment-method.html) to create a _PaymentMethod_ (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs).

#### Kotlin

```kotlin
class CheckoutActivity : AppCompatActivity() {
    private lateinit var stripe: Stripe

    private fun pay() {
        val weakActivity = WeakReference<Activity>(this)
        // Collect card details on the client
        val cardInputWidget =
            findViewById<CardInputWidget>(R.id.cardInputWidget)
        val params = cardInputWidget.paymentMethodCreateParams
        if (params == null) {
            return
        }

        // Configure the SDK with your Stripe publishable key so that it can make requests to the Stripe API
        stripe = Stripe(applicationContext, PaymentConfiguration.getInstance(applicationContext).publishableKey)
        lifecycleScope.launch {
            runCatching {
                stripe.createPaymentMethod(params).id
            }.fold(
                onSuccess = { paymentMethodId ->
                    // Send paymentMethodId to your server for the next steps
                },
                onFailure = {
                    // Create PaymentMethod failed, display the error to the user
                }
            )
        }
    }

    private fun pay(paymentMethod: String?, paymentIntent: String?) {
        // ...
    }
}
```

Send the resulting PaymentMethod ID to your server and follow the remaining steps to save the card to a customer and charge the card in the future.

## Save the card [Server-side]

Save the card by attaching the PaymentMethod to a _Customer_ (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments). You can use the Customer object to store other information about your customer, such as shipping details and email address.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create({
  payment_method: "{{PAYMENT_METHOD_ID}}",
});
```

If you have an existing Customer, you can attach the PaymentMethod to that object instead.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethod = await stripe.paymentMethods.attach(
  "{{PAYMENT_METHOD_ID}}",
  {
    customer: "{{CUSTOMER_ID}}",
  },
);
```

At this point, associate the ID of the Customer object and the ID of the PaymentMethod with your own internal representation of a customer, if you have one.

## Charge the saved card [Server-side]

When you’re ready to charge the Customer, look up the PaymentMethod ID to charge. You can do this by either storing the IDs of both in your database, or by using the Customer ID to look up all the Customer’s available PaymentMethods.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethods = await stripe.paymentMethods.list({
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  type: "card",
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethods = await stripe.paymentMethods.list({
  customer: "{{CUSTOMER_ID}}",
  type: "card",
});
```

Use the PaymentMethod ID and the Customer ID to create a new PaymentIntent. Set [error_on_requires_action](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-error_on_requires_action) to true to decline payments that require any actions from your customer, such as two-factor authentication.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "usd",
  payment_method_types: ["card"],
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{PAYMENT_METHOD_ID}}",
  error_on_requires_action: true,
  confirm: true,
});
```

When a payment attempt fails, the request also fails with a 402 HTTP status code and Stripe throws an error. You need to notify your customer to return to your application (for example, by sending an in-app notification) to complete the payment. Check the code of the [Error](https://docs.stripe.com/api/errors/handling.md) raised by the Stripe API library or check the [last_payment_error.decline_code](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-last_payment_error-decline_code) on the PaymentIntent to inspect why the card issuer declined the payment.

## Handle any card errors

Notify your customer that the payment failed and direct them to the payment form you made in step 1 where they can enter new card details. Send that new PaymentMethod ID to your server to [attach](https://docs.stripe.com/api/payment_methods/attach.md) to the Customer object and make the payment again.

Alternatively, you can create a PaymentIntent and save a card in one API call if you already created a Customer.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "usd",
  payment_method_types: ["card"],
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{PAYMENT_METHOD_ID}}",
  error_on_requires_action: true,
  confirm: true,
  setup_future_usage: "on_session",
});
```

Setting [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) to `on_session` indicates to Stripe that you want to save the card for later, without triggering unnecessary authentication.

## Test the integration

Stripe provides [test cards](https://docs.stripe.com/testing.md) you can use in a sandbox to simulate the behavior of different cards. Use these cards with any CVC, postal code, and expiration date in the future.

| Number           | Description                                                                                           |
| ---------------- | ----------------------------------------------------------------------------------------------------- |
| 4242424242424242 | Succeeds and immediately processes the payment.                                                       |
| 4000000000009995 | Always fails with a decline code of `insufficient_funds`.                                             |
| 4000002500003155 | Requires authentication, which in this integration declines with a code of `authentication_required`. |

## Optional: Re-collect a CVC

When creating subsequent payments on a saved card, you might want to re-collect the CVC of the card as an additional fraud measure to verify the user.

Start by creating a PaymentIntent from your server with the amount and currency of the payment, and set [customer](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-customer) to the ID of your Customer. Then, [list](https://docs.stripe.com/api/payment_methods/list.md) the PaymentMethods associated with your Customer to determine which PaymentMethods to show to your user for CVC re-collection.

After re-collecting the customer’s CVC information, create a [PaymentMethodOptionsParams.Card](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-payment-method-options-params/-card/index.html) instance with the customer’s CVC. Confirm the PaymentIntent by creating a [ConfirmPaymentIntentParams](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-confirm-payment-intent-params/index.html) instance with the [PaymentMethodOptionsParams.Card](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-payment-method-options-params/-card/index.html) instance and passing it to [Stripe#confirmPayment()](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-stripe/confirm-payment.html).

#### Kotlin

```kotlin
class CheckoutActivity : AppCompatActivity() {
    private val stripe: Stripe by lazy {
        Stripe(this, "<<YOUR_PUBLISHABLE_KEY>>")
    }

    private fun confirmPaymentIntent(clientSecret: String, cvc: String) {
        val params = ConfirmPaymentIntentParams.createWithPaymentMethodId(
            paymentMethodId = '{{PAYMENT_METHOD_ID}}',
            paymentMethodOptions = PaymentMethodOptionsParams.Card(
                cvc = cvc
            ),
            clientSecret = clientSecret
        )
        stripe.confirmPayment(this, params)
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)
        stripe.onPaymentResult(
            requestCode, data,
            object : ApiResultCallback<PaymentIntentResult> {
                override fun onSuccess(result: PaymentIntentResult) {
                }

                override fun onError(e: Exception) {
                }
            }
        )
    }
}
```

A payment might succeed even with a failed CVC check. To prevent this, configure your [Radar rules](https://docs.stripe.com/radar/rules.md#traditional-bank-checks) to block payments when CVC verification fails.

## Upgrade your integration to handle card authentication

This integration **declines cards that require authentication during payment**. If you start seeing many payments in the Dashboard listed as `Failed`, then it’s time to [upgrade your integration](https://docs.stripe.com/payments/payment-intents/upgrade-to-handle-actions.md). Stripe’s global integration handles these payments instead of automatically declining.

# React Native

> This is a React Native for when platform is react-native. View the full page at https://docs.stripe.com/payments/mobile/save-card-without-authentication?platform=react-native.

​​Stripe allows you to collect card details and charge your customer at a later time. ​​In some regions, banks require a second form of authentication such as entering a code sent to a phone. ​​The extra step decreases conversion if your customer isn’t actively using your website or application because they aren’t available to authenticate the purchase.

​​If you primarily do business in the US and Canada, banks don’t require authentication, so you can follow this simpler integration. This integration will be non-compliant in countries that require authentication for saving cards (for example, India) so building this integration means that expanding to other countries or adding other payment methods will require significant changes. Learn how to [save cards that require authentication](https://docs.stripe.com/payments/save-and-reuse.md).

> #### Compliance
>
> You’re responsible for your compliance with all applicable laws, regulations, and network rules when saving a customer’s payment details. For instance, if you want to save their payment method for future use, such as charging them when they’re not actively using your website or app. Add terms to your website or app that state how you plan to save payment method details and allow customers to opt in. If you want to charge them when they’re offline, make sure your terms include the following:
>
> - The customer’s agreement to your initiating a payment or a series of payments on their behalf for specified transactions.

- The anticipated timing and frequency of payments (for example, if the charges are for scheduled installments, subscription payments, or unscheduled top-ups).
- How you determine the payment amount.
- Your cancellation policy, if the payment method is for a subscription service.
  > Make sure you keep a record of your customer’s written agreement to these terms.

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

## Collect card details [Client-side]

Securely collect card information on the client with `CardField`, a UI component provided by the SDK that collects the card number, expiration date, CVC, and postal code.
![](assets/stripe-inapp-ios-card-field.mp4)
Add the `CardField` component to your payment screen to securely collect card details from your customers. Use the `onCardChange` callback to inspect non-sensitive information about the card, like the brand, and whether the details are complete.

```javascript
import { CardField, useStripe } from "@stripe/stripe-react-native";

function PaymentScreen() {
  // ...
  return (
    <View>
      <CardField
        postalCodeEnabled={true}
        placeholders={{
          number: "4242 4242 4242 4242",
        }}
        cardStyle={{
          backgroundColor: "#FFFFFF",
          textColor: "#000000",
        }}
        style={{
          width: "100%",
          height: 50,
          marginVertical: 30,
        }}
        onCardChange={(cardDetails) => {
          console.log("cardDetails", cardDetails);
        }}
        onFocus={(focusedField) => {
          console.log("focusField", focusedField);
        }}
      />
    </View>
  );
}
```

Run your app and make sure your checkout page shows the `CardField` component. When the customer taps **Pay**, use `createPaymentMethod` to collect the card details and create a _PaymentMethod_ (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs). Send the ID of the PaymentMethod to your server.

```javascript
const pay = () => {
  const { paymentMethod, error } = await createPaymentMethod({
    paymentMethodType: 'Card',
    paymentMethodData: {
      billingDetails: {
        name: 'Jenny Rosen',
      }
    },
  });

  if (error) {
    // Handle error
  } else if (paymentMethod) {
    const paymentMethodId = paymentMethod.id;
    // Send the ID of the PaymentMethod to your server for the next step
    // ...
  }
};
```

## Save the card [Server-side]

Save the card by attaching the PaymentMethod to a _Customer_ (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments). You can use the Customer object to store other information about your customer, such as shipping details and email address.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create({
  payment_method: "{{PAYMENT_METHOD_ID}}",
});
```

If you have an existing Customer, you can attach the PaymentMethod to that object instead.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethod = await stripe.paymentMethods.attach(
  "{{PAYMENT_METHOD_ID}}",
  {
    customer: "{{CUSTOMER_ID}}",
  },
);
```

At this point, associate the ID of the Customer object and the ID of the PaymentMethod with your own internal representation of a customer, if you have one.

## Charge the saved card [Server-side]

When you’re ready to charge the Customer, look up the PaymentMethod ID to charge. You can do this by either storing the IDs of both in your database, or by using the Customer ID to look up all the Customer’s available PaymentMethods.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethods = await stripe.paymentMethods.list({
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  type: "card",
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethods = await stripe.paymentMethods.list({
  customer: "{{CUSTOMER_ID}}",
  type: "card",
});
```

Use the PaymentMethod ID and the Customer ID to create a new PaymentIntent. Set [error_on_requires_action](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-error_on_requires_action) to true to decline payments that require any actions from your customer, such as two-factor authentication.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "usd",
  payment_method_types: ["card"],
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{PAYMENT_METHOD_ID}}",
  error_on_requires_action: true,
  confirm: true,
});
```

When a payment attempt fails, the request also fails with a 402 HTTP status code and Stripe throws an error. You need to notify your customer to return to your application (for example, by sending an in-app notification) to complete the payment. Check the code of the [Error](https://docs.stripe.com/api/errors/handling.md) raised by the Stripe API library or check the [last_payment_error.decline_code](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-last_payment_error-decline_code) on the PaymentIntent to inspect why the card issuer declined the payment.

## Handle any card errors

Notify your customer that the payment failed and direct them to the payment form you made in step 1 where they can enter new card details. Send that new PaymentMethod ID to your server to [attach](https://docs.stripe.com/api/payment_methods/attach.md) to the Customer object and make the payment again.

Alternatively, you can create a PaymentIntent and save a card in one API call if you already created a Customer.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "usd",
  payment_method_types: ["card"],
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{PAYMENT_METHOD_ID}}",
  error_on_requires_action: true,
  confirm: true,
  setup_future_usage: "on_session",
});
```

Setting [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) to `on_session` indicates to Stripe that you want to save the card for later, without triggering unnecessary authentication.

## Test the integration

Stripe provides [test cards](https://docs.stripe.com/testing.md) you can use in a sandbox to simulate the behavior of different cards. Use these cards with any CVC, postal code, and expiration date in the future.

| Number           | Description                                                                                           |
| ---------------- | ----------------------------------------------------------------------------------------------------- |
| 4242424242424242 | Succeeds and immediately processes the payment.                                                       |
| 4000000000009995 | Always fails with a decline code of `insufficient_funds`.                                             |
| 4000002500003155 | Requires authentication, which in this integration declines with a code of `authentication_required`. |

## Optional: Re-collect a CVC

When creating subsequent payments on a saved card, you might want to re-collect the CVC of the card as an additional fraud measure to verify the user.

Start by creating a PaymentIntent on your server with the amount, currency, and your [Customer](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-customer) ID. [List](https://docs.stripe.com/api/payment_methods/list.md) the _PaymentMethods_ (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) associated with your _Customer_ (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) to determine which PaymentMethods to show for CVC re-collection. After re-collecting the customer’s CVC information, call `confirmPayment` method with the customer’s `CVC` and `paymentMethodId`.

```javascript
const pay = async (cvc: string) => {
  const {
    clientSecret,
    paymentMethodId,
  } = await fetchPaymentIntentClientSecret();

  const {error, paymentIntent} = await confirmPayment(clientSecret, {
    paymentMethodType: 'Card',
    paymentMethodData: {
      cvc,
      paymentMethodId,
    },
  });

  if (error) {
    Alert.alert(`Error code: ${error.code}`, error.message);
  } else if (paymentIntent.status === PaymentIntent.Status.Succeeded) {
    Alert.alert('Success', 'The payment was confirmed successfully!');
  } else {
    // Handle other statuses accordingly
  }
};
```

A payment might succeed even with a failed CVC check. To prevent this, configure your [Radar rules](https://docs.stripe.com/radar/rules.md#traditional-bank-checks) to block payments when CVC verification fails.

## Upgrade your integration to handle card authentication

This integration **declines cards that require authentication during payment**. If you start seeing many payments in the Dashboard listed as `Failed`, then it’s time to [upgrade your integration](https://docs.stripe.com/payments/payment-intents/upgrade-to-handle-actions.md). Stripe’s global integration handles these payments instead of automatically declining.
