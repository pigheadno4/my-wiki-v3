<!-- Source URL: https://docs.stripe.com/payments/mobile/without-card-authentication -->
<!-- Fetched: 2026-04-23 -->

# Card payments without bank authentication

Build a simpler mobile integration with regional limitations.

# iOS

> This is a iOS for when platform is ios. View the full page at https://docs.stripe.com/payments/mobile/without-card-authentication?platform=ios.

This integration supports businesses accepting only US and Canadian cards. It’s simpler to build, but doesn’t scale to support a global customer base.

### How this integration works

Banks in regions such as Europe and India often require two-factor authentication to confirm a purchase. If you primarily do business in the US and Canada, ignoring _card authentication_ (A bank might require the customer to authenticate a card payment before processing. Implementation varies by bank but commonly consists of a customer entering in a security code sent to their phone) can simplify your integration, as banks rarely request it in these regions.

When a bank requires authentication, this basic integration immediately declines the payment (similar to a card decline), instead of handling authentication to complete the payment asynchronously. The benefit is that the payment succeeds or declines immediately and payment confirmation happens on the server, so you can handle immediate post-payment actions without a _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests).

### How it compares to the global integration

| Feature                                                              | This Integration | Global Integration |
| -------------------------------------------------------------------- | ---------------- | ------------------ |
| Custom payment form                                                  | ✔                | ✔                  |
| Sensitive data never touches your server                             | ✔                | ✔                  |
| Works for your US and Canada customers                               | ✔                | ✔                  |
| Declines payments with incorrect card details or no funds            | ✔                | ✔                  |
| Declines payments with bank authentication requests                  | ✔                |                    |
| Works for your global customers                                      |                  | ✔                  |
| Automatically handles card payments that require bank authentication |                  | ✔                  |
| Webhooks recommended for post-payment tasks                          |                  | ✔                  |
| Easily scales to other payment methods (for example, bank debits)    |                  | ✔                  |

Growing or global businesses should use Stripe’s [global integration](https://docs.stripe.com/payments/accept-a-payment.md) to support bank requests for two-factor authentication and allow customers to pay with more payment methods.

## Install the Stripe iOS SDK [Client-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

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

Securely collect card information on the client with [STPPaymentCardTextField](https://stripe.dev/stripe-ios/stripe-payments-ui/Classes/STPPaymentCardTextField.html), a drop-in UI component provided by the SDK that collects the card number, expiration date, CVC, and postal code.
![](assets/stripe-inapp-ios-card-field.mp4)
Create an instance of the card component and a **Pay** button with the following code:

#### Swift

```swift
import UIKit
import StripePaymentsUI

class CheckoutViewController: UIViewController {

    lazy var cardTextField: STPPaymentCardTextField = {
        let cardTextField = STPPaymentCardTextField()
        return cardTextField
    }()
    lazy var payButton: UIButton = {
        let button = UIButton(type: .custom)
        button.layer.cornerRadius = 5
        button.backgroundColor = .systemBlue
        button.titleLabel?.font = UIFont.systemFont(ofSize: 22)
        button.setTitle("Pay", for: .normal)
        button.addTarget(self, action: #selector(pay), for: .touchUpInside)
        return button
    }()

    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .white
        let stackView = UIStackView(arrangedSubviews: [cardTextField, payButton])
        stackView.axis = .vertical
        stackView.spacing = 20
        stackView.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(stackView)
        NSLayoutConstraint.activate([
            stackView.leftAnchor.constraint(equalToSystemSpacingAfter: view.leftAnchor, multiplier: 2),
            view.rightAnchor.constraint(equalToSystemSpacingAfter: stackView.rightAnchor, multiplier: 2),
            stackView.topAnchor.constraint(equalToSystemSpacingBelow: view.safeAreaLayoutGuide.topAnchor, multiplier: 2),
        ])
    }

    @objc
    func pay() {
        // ...
    }
}
```

Run your app and make sure your checkout page shows the card component. When the customer taps **Pay**, call [createPaymentMethod](<https://stripe.dev/stripe-ios/stripe-payments/Classes/STPAPIClient.html#/c:@CM@StripePayments@StripeCore@objc(cs)STPAPIClient(im)createPaymentMethodWithPayment:completion:>) to collect the card details and create a [PaymentMethod](https://docs.stripe.com/api/payment_methods.md). Send the ID of the PaymentMethod to your server.

#### Swift

```swift
func pay() {
    // Create a PaymentMethod with the card text field's card details
    STPAPIClient.shared.createPaymentMethod(with: cardTextField.paymentMethodParams) { (paymentMethod, error) in
        guard let paymentMethod = paymentMethod else {
            // Display the error to the customer
            return
        }
        let paymentMethodID = paymentMethod.stripeId
        // Send paymentMethodID to your server for the next step
    }
}
```

## Make a payment [Server-side]

Set up an endpoint on your server to receive the request from the client. Use the official libraries for access to the Stripe API from your server:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

Stripe uses a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) object to represent your intent to collect payment from a customer, tracking charge attempts and payment state changes throughout the process.

Create an HTTP endpoint to respond to the request from step 2. In that endpoint, you should decide how much to charge the customer. To create a payment, create a PaymentIntent using the PaymentMethod ID from step 2 with the following parameters:

Always decide how much to charge on the server, a trusted environment, as opposed to the client. This prevents malicious customers from being able to choose their own prices.

#### Node.js

```javascript
// Using Express
const express = require("express");
const app = express();
app.use(express.json());
const { resolve } = require("path");

app.get("/", (req, res) => {
  // Display checkout page
  const path = resolve("./index.html");
  res.sendFile(path);
});

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

// Endpoint for when `/pay` is called from client
app.post("/pay", async (request, response) => {
  try {
    // Create the PaymentIntent
    let intent = await stripe.paymentIntents.create({
      amount: 1099,
      currency: "usd",
      payment_method: request.body.payment_method_id,

      // A PaymentIntent can be confirmed some time after creation,
      // but here we want to confirm (collect payment) immediately.
      confirm: true,

      // If the payment requires any follow-up actions from the
      // customer, like two-factor authentication, Stripe will error
      // and you will need to prompt them for a new payment method.>
      error_on_requires_action: true,
    });
    return generateResponse(response, intent);
  } catch (e) {
    if (e.type === "StripeCardError") {
      // Display error on client
      return response.send({ error: e.message });
    } else {
      // Something else happened
      return response.status(500).send({ error: e.type });
    }
  }
});

function generateResponse(response, intent) {
  if (intent.status === "succeeded") {
    // Handle post-payment fulfillment
    return response.send({ success: true });
  } else {
    // Any other status would be unexpected, so error
    return response
      .status(500)
      .send({ error: "Unexpected status " + intent.status });
  }
}

app.listen(4242, () => console.log(`Node server listening on port ${4242}!`));
```

> If you set [error_on_requires_action](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-error_on_requires_action) to `true` when confirming a payment, Stripe automatically fails the payment if it requires two-factor authentication from the user.

#### Payment Intents API response

When you make a payment with the API, the response includes a status of the PaymentIntent. If the payment was successful, it will have a status of `succeeded`.

```json
{
  "id": "pi_0FdpcX589O8KAxCGR6tGNyWj",
  "object": "payment_intent",
  "amount": 1099,
  "charges": {
    "object": "list",
    "data": [
      {
        "id": "ch_GA9w4aF29fYajT",
        "object": "charge",
        "amount": 1099,
        "refunded": false,
        "status": "succeeded"
      }
    ]
  },
  "client_secret": "pi_0FdpcX589O8KAxCGR6tGNyWj_secret_e00tjcVrSv2tjjufYqPNZBKZc",
  "currency": "usd",
  "last_payment_error": null,
  "status": "succeeded"
}
```

If the payment is declined, the response includes the error code and error message. Here’s an example of a payment that failed because two-factor authentication was required for the card.

```json
{
  "error": {
    "code": "authentication_required",
    "decline_code": "authentication_not_handled",
    "doc_url": "https://docs.stripe.com/error-codes#authentication-required",
    "message": "This payment required an authentication action to complete, but `error_on_requires_action` was set. When you're ready, you can upgrade your integration to handle actions at https://stripe.com/docs/payments/payment-intents/upgrade-to-handle-actions.",
    "payment_intent": {
      "id": "pi_1G8JtxDpqHItWkFAnB32FhtI",
      "object": "payment_intent",
      "amount": 1099,
      "status": "requires_payment_method",
      "last_payment_error": {
        "code": "authentication_required",
        "decline_code": "authentication_not_handled",
        "doc_url": "https://docs.stripe.com/error-codes#authentication-required",
        "message": "This payment required an authentication action to complete, but `error_on_requires_action` was set. When you're ready, you can upgrade your integration to handle actions at https://stripe.com/docs/payments/payment-intents/upgrade-to-handle-actions.",
        "type": "card_error"
      }
    },
    "type": "card_error"
  }
}
```

## Test the integration

There are several test cards you can use in a testing environment to make sure this integration is ready. Use them with any CVC, postal code, and future expiration date.

| Number           | Description                                                                                                       |
| ---------------- | ----------------------------------------------------------------------------------------------------------------- |
| 4242424242424242 | Succeeds and immediately processes the payment.                                                                   |
| 4000000000009995 | Always fails with a decline code of `insufficient_funds`.                                                         |
| 4000002500003155 | Requires authentication, which in this integration will fail with a decline code of `authentication_not_handled`. |

See the full list of [test cards](https://docs.stripe.com/testing.md).

## Upgrade your integration to handle card authentication

Congratulations! You completed a payments integration for basic card payments. Note that this integration **declines cards that require authentication during payment**.

If you start seeing payments in the Dashboard listed as `Failed`, then it’s time to [upgrade your integration](https://docs.stripe.com/payments/payment-intents/upgrade-to-handle-actions.md). Stripe’s global integration handles these payments instead of automatically declining them.

# Android

> This is a Android for when platform is android. View the full page at https://docs.stripe.com/payments/mobile/without-card-authentication?platform=android.

This integration supports businesses accepting only US and Canadian cards. It’s simpler to build, but doesn’t scale to support a global customer base.

### How this integration works

Banks in regions such as Europe and India often require two-factor authentication to confirm a purchase. If you primarily do business in the US and Canada, ignoring _card authentication_ (A bank might require the customer to authenticate a card payment before processing. Implementation varies by bank but commonly consists of a customer entering in a security code sent to their phone) can simplify your integration, as banks rarely request it in these regions.

When a bank requires authentication, this basic integration immediately declines the payment (similar to a card decline), instead of handling authentication to complete the payment asynchronously. The benefit is that the payment succeeds or declines immediately and payment confirmation happens on the server, so you can handle immediate post-payment actions without a _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests).

### How it compares to the global integration

| Feature                                                              | This Integration | Global Integration |
| -------------------------------------------------------------------- | ---------------- | ------------------ |
| Custom payment form                                                  | ✔                | ✔                  |
| Sensitive data never touches your server                             | ✔                | ✔                  |
| Works for your US and Canada customers                               | ✔                | ✔                  |
| Declines payments with incorrect card details or no funds            | ✔                | ✔                  |
| Declines payments with bank authentication requests                  | ✔                |                    |
| Works for your global customers                                      |                  | ✔                  |
| Automatically handles card payments that require bank authentication |                  | ✔                  |
| Webhooks recommended for post-payment tasks                          |                  | ✔                  |
| Easily scales to other payment methods (for example, bank debits)    |                  | ✔                  |

Growing or global businesses should use Stripe’s [global integration](https://docs.stripe.com/payments/accept-a-payment.md) to support bank requests for two-factor authentication and allow customers to pay with more payment methods.

## Install the Stripe Android SDK [Client-side]

Next, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

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

Securely collect card information on the client with [CardInputWidget](https://stripe.dev/stripe-android/payments-core/com.stripe.android.view/-card-input-widget/index.html), a drop-in UI component provided by the SDK that collects the card number, expiration date, CVC, and postal code.
![](assets/stripe-inapp-android-card-input.mp4)
Create an instance of the card component and a **Pay** button by adding the following to your checkout page’s layout:

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout
        xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:tools="http://schemas.android.com/tools"
        xmlns:app="http://schemas.android.com/apk/res-auto"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        app:layout_behavior="@string/appbar_scrolling_view_behavior"
        tools:showIn="@layout/activity_checkout"
        tools:context=".CheckoutActivity">

    <!--  ...  -->

    <com.stripe.android.view.CardInputWidget
            android:id="@+id/cardInputWidget"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_marginLeft="20dp"
            android:layout_marginRight="20dp"/>

    <Button
            android:text="Pay"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:id="@+id/payButton"
            android:layout_marginTop="20dp"
            app:layout_constraintTop_toBottomOf="@+id/cardInputWidget"
            app:layout_constraintStart_toStartOf="@+id/cardInputWidget"
            app:layout_constraintEnd_toEndOf="@+id/cardInputWidget"/>

      <!--  ...  -->

</androidx.constraintlayout.widget.ConstraintLayout>
```

When the customer taps **Pay**, call [Stripe#createPaymentMethod()](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-stripe/create-payment-method.html) in Java or [Stripe#createPaymentMethod()](https://stripe.dev/stripe-android/payments-core/com.stripe.android/create-payment-method.html) in Kotlin to collect the card details and create a [PaymentMethod](https://docs.stripe.com/api/payment_methods.md). Send the ID of the PaymentMethod to your server.

#### Kotlin

```kotlin
cardInputWidget.paymentMethodCreateParams?.let { paymentMethodParams ->
    lifecycleScope.launch {
        runCatching {
            stripe.createPaymentMethod(paymentMethodParams).id
        }.fold(
            onSuccess = { // paymentMethodId
                // Send the ID of the PaymentMethod to your server.
            },
            onFailure = {
                // Display the error to the customer.
            }
        )
    }
}
```

## Make a payment [Server-side]

Set up an endpoint on your server to receive the request from the client. Use the official libraries for access to the Stripe API from your server:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

Stripe uses a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) object to represent your intent to collect payment from a customer, tracking charge attempts and payment state changes throughout the process.

Create an HTTP endpoint to respond to the request from step 2. In that endpoint, you should decide how much to charge the customer. To create a payment, create a PaymentIntent using the PaymentMethod ID from step 2 with the following parameters:

Always decide how much to charge on the server, a trusted environment, as opposed to the client. This prevents malicious customers from being able to choose their own prices.

#### Node.js

```javascript
// Using Express
const express = require("express");
const app = express();
app.use(express.json());
const { resolve } = require("path");

app.get("/", (req, res) => {
  // Display checkout page
  const path = resolve("./index.html");
  res.sendFile(path);
});

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

// Endpoint for when `/pay` is called from client
app.post("/pay", async (request, response) => {
  try {
    // Create the PaymentIntent
    let intent = await stripe.paymentIntents.create({
      amount: 1099,
      currency: "usd",
      payment_method: request.body.payment_method_id,

      // A PaymentIntent can be confirmed some time after creation,
      // but here we want to confirm (collect payment) immediately.
      confirm: true,

      // If the payment requires any follow-up actions from the
      // customer, like two-factor authentication, Stripe will error
      // and you will need to prompt them for a new payment method.>
      error_on_requires_action: true,
    });
    return generateResponse(response, intent);
  } catch (e) {
    if (e.type === "StripeCardError") {
      // Display error on client
      return response.send({ error: e.message });
    } else {
      // Something else happened
      return response.status(500).send({ error: e.type });
    }
  }
});

function generateResponse(response, intent) {
  if (intent.status === "succeeded") {
    // Handle post-payment fulfillment
    return response.send({ success: true });
  } else {
    // Any other status would be unexpected, so error
    return response
      .status(500)
      .send({ error: "Unexpected status " + intent.status });
  }
}

app.listen(4242, () => console.log(`Node server listening on port ${4242}!`));
```

> If you set [error_on_requires_action](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-error_on_requires_action) to `true` when confirming a payment, Stripe automatically fails the payment if it requires two-factor authentication from the user.

#### Payment Intents API response

When you make a payment with the API, the response includes a status of the PaymentIntent. If the payment was successful, it will have a status of `succeeded`.

```json
{
  "id": "pi_0FdpcX589O8KAxCGR6tGNyWj",
  "object": "payment_intent",
  "amount": 1099,
  "charges": {
    "object": "list",
    "data": [
      {
        "id": "ch_GA9w4aF29fYajT",
        "object": "charge",
        "amount": 1099,
        "refunded": false,
        "status": "succeeded"
      }
    ]
  },
  "client_secret": "pi_0FdpcX589O8KAxCGR6tGNyWj_secret_e00tjcVrSv2tjjufYqPNZBKZc",
  "currency": "usd",
  "last_payment_error": null,
  "status": "succeeded"
}
```

If the payment is declined, the response includes the error code and error message. Here’s an example of a payment that failed because two-factor authentication was required for the card.

```json
{
  "error": {
    "code": "authentication_required",
    "decline_code": "authentication_not_handled",
    "doc_url": "https://docs.stripe.com/error-codes#authentication-required",
    "message": "This payment required an authentication action to complete, but `error_on_requires_action` was set. When you're ready, you can upgrade your integration to handle actions at https://stripe.com/docs/payments/payment-intents/upgrade-to-handle-actions.",
    "payment_intent": {
      "id": "pi_1G8JtxDpqHItWkFAnB32FhtI",
      "object": "payment_intent",
      "amount": 1099,
      "status": "requires_payment_method",
      "last_payment_error": {
        "code": "authentication_required",
        "decline_code": "authentication_not_handled",
        "doc_url": "https://docs.stripe.com/error-codes#authentication-required",
        "message": "This payment required an authentication action to complete, but `error_on_requires_action` was set. When you're ready, you can upgrade your integration to handle actions at https://stripe.com/docs/payments/payment-intents/upgrade-to-handle-actions.",
        "type": "card_error"
      }
    },
    "type": "card_error"
  }
}
```

## Test the integration

There are several test cards you can use in a testing environment to make sure this integration is ready. Use them with any CVC, postal code, and future expiration date.

| Number           | Description                                                                                                       |
| ---------------- | ----------------------------------------------------------------------------------------------------------------- |
| 4242424242424242 | Succeeds and immediately processes the payment.                                                                   |
| 4000000000009995 | Always fails with a decline code of `insufficient_funds`.                                                         |
| 4000002500003155 | Requires authentication, which in this integration will fail with a decline code of `authentication_not_handled`. |

See the full list of [test cards](https://docs.stripe.com/testing.md).

## Upgrade your integration to handle card authentication

Congratulations! You completed a payments integration for basic card payments. Note that this integration **declines cards that require authentication during payment**.

If you start seeing payments in the Dashboard listed as `Failed`, then it’s time to [upgrade your integration](https://docs.stripe.com/payments/payment-intents/upgrade-to-handle-actions.md). Stripe’s global integration handles these payments instead of automatically declining them.

# React Native

> This is a React Native for when platform is react-native. View the full page at https://docs.stripe.com/payments/mobile/without-card-authentication?platform=react-native.

This integration supports businesses accepting only US and Canadian cards. It’s simpler to build, but doesn’t scale to support a global customer base.

### How this integration works

Banks in regions such as Europe and India often require two-factor authentication to confirm a purchase. If you primarily do business in the US and Canada, ignoring _card authentication_ (A bank might require the customer to authenticate a card payment before processing. Implementation varies by bank but commonly consists of a customer entering in a security code sent to their phone) can simplify your integration, as banks rarely request it in these regions.

When a bank requires authentication, this basic integration immediately declines the payment (similar to a card decline), instead of handling authentication to complete the payment asynchronously. The benefit is that the payment succeeds or declines immediately and payment confirmation happens on the server, so you can handle immediate post-payment actions without a _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests).

### How it compares to the global integration

| Feature                                                              | This Integration | Global Integration |
| -------------------------------------------------------------------- | ---------------- | ------------------ |
| Custom payment form                                                  | ✔                | ✔                  |
| Sensitive data never touches your server                             | ✔                | ✔                  |
| Works for your US and Canada customers                               | ✔                | ✔                  |
| Declines payments with incorrect card details or no funds            | ✔                | ✔                  |
| Declines payments with bank authentication requests                  | ✔                |                    |
| Works for your global customers                                      |                  | ✔                  |
| Automatically handles card payments that require bank authentication |                  | ✔                  |
| Webhooks recommended for post-payment tasks                          |                  | ✔                  |
| Easily scales to other payment methods (for example, bank debits)    |                  | ✔                  |

Growing or global businesses should use Stripe’s [global integration](https://docs.stripe.com/payments/accept-a-payment.md) to support bank requests for two-factor authentication and allow customers to pay with more payment methods.

## Install the React Native SDK [Client-side]

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

Run your app, and make sure your checkout page shows the `CardField` component. When the customer taps **Pay**, use `createPaymentMethod` to collect the card details and create a [PaymentMethod](https://docs.stripe.com/api/payment_methods.md). Send the ID of the PaymentMethod to your server.

```javascript
const pay = async () => {
  const { paymentMethod, error } = await createPaymentMethod({
    paymentMethodType: "Card",
    paymentMethodData: {
      billingDetails: {
        name: "Jenny Rosen",
      },
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

## Make a payment [Server-side]

Set up an endpoint on your server to receive the request from the client. Use the official libraries for access to the Stripe API from your server:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

Stripe uses a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) object to represent your intent to collect payment from a customer, tracking charge attempts and payment state changes throughout the process.

Create an HTTP endpoint to respond to the request from step 2. In that endpoint, you should decide how much to charge the customer. To create a payment, create a PaymentIntent using the PaymentMethod ID from step 2 with the following parameters:

Always decide how much to charge on the server, a trusted environment, as opposed to the client. This prevents malicious customers from being able to choose their own prices.

#### Node.js

```javascript
// Using Express
const express = require("express");
const app = express();
app.use(express.json());
const { resolve } = require("path");

app.get("/", (req, res) => {
  // Display checkout page
  const path = resolve("./index.html");
  res.sendFile(path);
});

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

// Endpoint for when `/pay` is called from client
app.post("/pay", async (request, response) => {
  try {
    // Create the PaymentIntent
    let intent = await stripe.paymentIntents.create({
      amount: 1099,
      currency: "usd",
      payment_method: request.body.payment_method_id,

      // A PaymentIntent can be confirmed some time after creation,
      // but here we want to confirm (collect payment) immediately.
      confirm: true,

      // If the payment requires any follow-up actions from the
      // customer, like two-factor authentication, Stripe will error
      // and you will need to prompt them for a new payment method.>
      error_on_requires_action: true,
    });
    return generateResponse(response, intent);
  } catch (e) {
    if (e.type === "StripeCardError") {
      // Display error on client
      return response.send({ error: e.message });
    } else {
      // Something else happened
      return response.status(500).send({ error: e.type });
    }
  }
});

function generateResponse(response, intent) {
  if (intent.status === "succeeded") {
    // Handle post-payment fulfillment
    return response.send({ success: true });
  } else {
    // Any other status would be unexpected, so error
    return response
      .status(500)
      .send({ error: "Unexpected status " + intent.status });
  }
}

app.listen(4242, () => console.log(`Node server listening on port ${4242}!`));
```

> If you set [error_on_requires_action](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-error_on_requires_action) to `true` when confirming a payment, Stripe automatically fails the payment if it requires two-factor authentication from the user.

#### Payment Intents API response

When you make a payment with the API, the response includes a status of the PaymentIntent. If the payment was successful, it will have a status of `succeeded`.

```json
{
  "id": "pi_0FdpcX589O8KAxCGR6tGNyWj",
  "object": "payment_intent",
  "amount": 1099,
  "charges": {
    "object": "list",
    "data": [
      {
        "id": "ch_GA9w4aF29fYajT",
        "object": "charge",
        "amount": 1099,
        "refunded": false,
        "status": "succeeded"
      }
    ]
  },
  "client_secret": "pi_0FdpcX589O8KAxCGR6tGNyWj_secret_e00tjcVrSv2tjjufYqPNZBKZc",
  "currency": "usd",
  "last_payment_error": null,
  "status": "succeeded"
}
```

If the payment is declined, the response includes the error code and error message. Here’s an example of a payment that failed because two-factor authentication was required for the card.

```json
{
  "error": {
    "code": "authentication_required",
    "decline_code": "authentication_not_handled",
    "doc_url": "https://docs.stripe.com/error-codes#authentication-required",
    "message": "This payment required an authentication action to complete, but `error_on_requires_action` was set. When you're ready, you can upgrade your integration to handle actions at https://stripe.com/docs/payments/payment-intents/upgrade-to-handle-actions.",
    "payment_intent": {
      "id": "pi_1G8JtxDpqHItWkFAnB32FhtI",
      "object": "payment_intent",
      "amount": 1099,
      "status": "requires_payment_method",
      "last_payment_error": {
        "code": "authentication_required",
        "decline_code": "authentication_not_handled",
        "doc_url": "https://docs.stripe.com/error-codes#authentication-required",
        "message": "This payment required an authentication action to complete, but `error_on_requires_action` was set. When you're ready, you can upgrade your integration to handle actions at https://stripe.com/docs/payments/payment-intents/upgrade-to-handle-actions.",
        "type": "card_error"
      }
    },
    "type": "card_error"
  }
}
```

## Test the integration

There are several test cards you can use in a testing environment to make sure this integration is ready. Use them with any CVC, postal code, and future expiration date.

| Number           | Description                                                                                                       |
| ---------------- | ----------------------------------------------------------------------------------------------------------------- |
| 4242424242424242 | Succeeds and immediately processes the payment.                                                                   |
| 4000000000009995 | Always fails with a decline code of `insufficient_funds`.                                                         |
| 4000002500003155 | Requires authentication, which in this integration will fail with a decline code of `authentication_not_handled`. |

See the full list of [test cards](https://docs.stripe.com/testing.md).

## Upgrade your integration to handle card authentication

Congratulations! You completed a payments integration for basic card payments. Note that this integration **declines cards that require authentication during payment**.

If you start seeing payments in the Dashboard listed as `Failed`, then it’s time to [upgrade your integration](https://docs.stripe.com/payments/payment-intents/upgrade-to-handle-actions.md). Stripe’s global integration handles these payments instead of automatically declining them.
