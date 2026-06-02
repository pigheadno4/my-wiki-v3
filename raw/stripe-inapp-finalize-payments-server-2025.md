<!-- Source URL: https://docs.stripe.com/payments/mobile/finalize-payments-on-the-server -->
<!-- Fetched: 2026-04-22 -->

# Finalize payments on the server

Build an integration where you render the Mobile Payment Element before you create a PaymentIntent or SetupIntent, then confirm the Intent from your server.

# Accept a payment

> This is a Accept a payment for when platform is ios and type is payment. View the full page at https://docs.stripe.com/payments/mobile/finalize-payments-on-the-server?platform=ios&type=payment.

The Payment Element allows you to accept multiple payment methods using a single integration. In this integration, you build a custom payment flow where you render the Payment Element, create the _PaymentIntent_ (The Payment Intents API tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by regulatory mandates, custom Radar fraud rules, or redirect-based payment methods), and confirm the payment on your server.

## Set up Stripe [Server-side] [Client-side]

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
1. Add the **StripePaymentSheet** product to the [target of your app](https://developer.apple.com/documentation/swift_packages/adding_package_dependencies_to_your_app).

#### CocoaPods

1. If you haven’t already, install the latest version of [CocoaPods](https://guides.cocoapods.org/using/getting-started.html).
1. If you don’t have an existing [Podfile](https://guides.cocoapods.org/syntax/podfile.html), run the following command to create one:
   ```bash
   pod init
   ```
1. Add this line to your `Podfile`:
   ```podfile
   pod 'StripePaymentSheet'
   ```
1. Run the following command:
   ```bash
   pod install
   ```
1. Don’t forget to use the `.xcworkspace` file to open your project in Xcode, instead of the `.xcodeproj` file, from here on out.
1. In the future, to update to the latest version of the SDK, run:
   ```bash
   pod update StripePaymentSheet
   ```

#### Carthage

1. If you haven’t already, install the latest version of [Carthage](https://github.com/Carthage/Carthage#installing-carthage).
1. Add this line to your `Cartfile`:
   ```cartfile
   github "stripe/stripe-ios"
   ```
1. Follow the [Carthage installation instructions](https://github.com/Carthage/Carthage#if-youre-building-for-ios-tvos-or-watchos). Make sure to embed all of the required frameworks listed [here](https://github.com/stripe/stripe-ios/tree/master/StripePaymentSheet/README.md#manual-linking).
1. In the future, to update to the latest version of the SDK, run the following command:
   ```bash
   carthage update stripe-ios --platform ios
   ```

#### Manual Framework

1. Head to our [GitHub releases page](https://github.com/stripe/stripe-ios/releases/latest) and download and unzip **Stripe.xcframework.zip**.
1. Drag **StripePaymentSheet.xcframework** to the **Embedded Binaries** section of the **General** settings in your Xcode project. Make sure to select **Copy items if needed**.
1. Repeat step 2 for all required frameworks listed [here](https://github.com/stripe/stripe-ios/tree/master/StripePaymentSheet/README.md#manual-linking).
1. In the future, to update to the latest version of our SDK, repeat steps 1–3.

> For details on the latest SDK release and past versions, see the [Releases](https://github.com/stripe/stripe-ios/releases) page on GitHub. To receive notifications when a new release is published, [watch releases](https://help.github.com/en/articles/watching-and-unwatching-releases-for-a-repository#watching-releases-for-a-repository) for the repository.

You also need to set your [publishable key](https://dashboard.stripe.com/apikeys) so that the SDK can make API calls to Stripe. To get started, you can hardcode the publishable key on the client while you’re integrating, but fetch the publishable key from your server in production.

```swift
// Set your publishable key: remember to change this to your live publishable key in production
// See your keys here: https://dashboard.stripe.com/apikeys
STPAPIClient.shared.publishableKey = "<<YOUR_PUBLISHABLE_KEY>>"
```

## Enable payment methods

View your [payment methods settings](https://dashboard.stripe.com/settings/payment_methods) and enable the payment methods you want to support. You need at least one payment method enabled to create a _PaymentIntent_ (The Payment Intents API tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by regulatory mandates, custom Radar fraud rules, or redirect-based payment methods).

By default, Stripe enables cards and other prevalent payment methods that can help you reach more customers, but we recommend turning on additional payment methods that are relevant for your business and customers. See [Payment method support](https://docs.stripe.com/payments/payment-methods/payment-method-support.md) for product and payment method support, and our [pricing page](https://stripe.com/pricing/local-payment-methods) for fees.

## Set up a return URL [Client-side]

The customer might navigate away from your app to authenticate (for example, in Safari or their banking app). To allow them to automatically return to your app after authenticating, [configure a custom URL scheme](https://developer.apple.com/documentation/xcode/defining-a-custom-url-scheme-for-your-app) and set up your app delegate to forward the URL to the SDK. Stripe doesn’t support [universal links](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content).

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

#### SwiftUI

#### Swift

```swift

@main
struct MyApp: App {
  var body: some Scene {
    WindowGroup {
      Text("Hello, world!").onOpenURL { incomingURL in
          let stripeHandled = StripeAPI.handleURLCallback(with: incomingURL)
          if (!stripeHandled) {
            // This was not a Stripe url – handle the URL normally as you would
          }
        }
    }
  }
}
```

Additionally, set the [returnURL](https://stripe.dev/stripe-ios/stripe-paymentsheet/Classes/PaymentSheet/Configuration.html#/s:6Stripe12PaymentSheetC13ConfigurationV9returnURLSSSgvp) on your [PaymentSheet.Configuration](https://stripe.dev/stripe-ios/stripe-paymentsheet/Classes/PaymentSheet/Configuration.html) object to the URL for your app.

```swift
var configuration = PaymentSheet.Configuration()
configuration.returnURL = "your-app://stripe-redirect"
```

## Collect payment details [Client-side]

We offer two styles of integration. Choose one to continue.

| PaymentSheet                                                                                                                                                       | PaymentSheet.FlowController                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![PaymentSheet](assets/ios-overview.9e0d68d009dc005f73a6f5df69e00458.png)                                                 | ![PaymentSheet.FlowController](assets/ios-multi-step.cd631ea4f1cd8cf3f39b6b9e1e92b6c5.png)                                        |
| Displays a sheet to collect payment details and complete the payment. The sheet contains a \*_Pay_ button with the amount and currency, and completes the payment. | Displays a sheet to collect payment details only. The button in the sheet says **Continue** and returns the customer to your app, where your own button completes payment. |

#### PaymentSheet

### Initialize PaymentSheet

When you’re ready to accept a payment (for example, when a customer taps your checkout button), initialize the PaymentSheet with a `PaymentSheet.Configuration` and a [PaymentSheet.IntentConfiguration](https://github.com/stripe/stripe-ios/blob/master/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheetIntentConfiguration.swift). The [Configuration](https://stripe.dev/stripe-ios/stripepaymentsheet/documentation/stripepaymentsheet/paymentsheet/configuration-swift.struct) object contains the general configuration for the PaymentSheet that typically doesn’t change between payments, such as the `returnURL`. The [IntentConfiguration](https://github.com/stripe/stripe-ios/blob/master/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheetIntentConfiguration.swift) object contains details about the specific payment, such as the amount and currency, and a `confirmationTokenConfirmHandler` callback—for now, leave its implementation empty.

```swift
import StripePaymentSheet

class MyCheckoutVC: UIViewController {
  func didTapCheckoutButton() {let intentConfig = PaymentSheet.IntentConfiguration(mode: .payment(amount: 1099, currency: "USD",)) { [weak self] confirmationToken in
      try await self?.handleConfirmationToken(confirmationToken)
    }
    var configuration = PaymentSheet.Configuration()
    configuration.returnURL = "your-app://stripe-redirect" // Use the return url you set up in the previous step
    let paymentSheet = PaymentSheet(intentConfiguration: intentConfig, configuration: configuration)
  }
func handleConfirmationToken(_ confirmationToken: STPConfirmationToken) async throws -> String {
    // ...explained later
  }
}

```

### Present PaymentSheet

Next, present the PaymentSheet. The `present` method takes a completion block that’s called when the customer finishes paying and dismisses the sheet. Implement the completion block to handle the result (for example, by showing a receipt or confirmation screen in the `.completed` case.)

```swift
class MyCheckoutVC: UIViewController {
  func didTapCheckoutButton() {
    // ...paymentSheet.present(from: self) { result in
      switch result {
        case .completed:
          //Paymentcompleted - show a confirmation screen.
        case .failed(let error):
          print(error)
          // PaymentSheet encountered an unrecoverable error. You can display the error to the user, log it, and so on
        case .canceled:
          // Customer canceled - you should probably do nothing.
      }
    }
  }
}

```

### Confirm the payment

When the customer taps the Pay button in the PaymentSheet, it calls the callback you passed to `PaymentSheet.IntentConfiguration` with an [STPConfirmationToken](https://stripe.dev/stripe-ios/stripepayments/documentation/stripepayments/stpconfirmationtoken) object representing the customer’s payment details and preferences.

Implement this callback to send a request to your server, passing `confirmationToken.stripeId`. Your server creates and confirms a PaymentIntent and returns its client secret.

When the request returns, return your server response’s client secret or throw an error. The PaymentSheet completes any next actions required to complete the PaymentIntent using the client secret or displays the localized error message in its UI (either [errorDescription](https://developer.apple.com/documentation/foundation/localizederror/2946895-errordescription) or [localizedDescription](https://developer.apple.com/documentation/foundation/nserror/1414418-localizeddescription)).

```swift
class MyCheckoutVC: UIViewController {
  // ...
func handleConfirmationToken(_ confirmationToken: STPConfirmationToken) async throws -> String {
    // Make a request to your own server. Pass confirmationToken.stripeId if using server-side confirmation.
    // Return the client secret or throw an error.
    return try await MyAPIClient.shared.createIntent(confirmationTokenId: confirmationToken.stripeId)
  }
}
```

#### PaymentSheet.FlowController

This integration assumes your checkout screen has two buttons—a “**Payment Method**” button that presents the PaymentSheet to collect payment details and a “**Buy**” button that completes the payment.

### Initialize PaymentSheet.FlowController

When your checkout screen loads, initialize `PaymentSheet.FlowController` with a `PaymentSheet.Configuration` and a `PaymentSheet.IntentConfiguration`. The [Configuration](https://stripe.dev/stripe-ios/stripepaymentsheet/documentation/stripepaymentsheet/paymentsheet/configuration-swift.struct) object contains general-purpose configuration for PaymentSheet that usually don’t change between payments, like `returnURL`. The [IntentConfiguration](https://github.com/stripe/stripe-ios/blob/master/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheetIntentConfiguration.swift) object contains details about the specific payment, like the amount and currency, as well as a `confirmationTokenConfirmHandler` callback—for now, leave its implementation empty.

After `PaymentSheet.FlowController` initializes, update your “**Payment Method**” button with its `paymentOption`. This property contains an image and label representing the customer’s initially selected, default payment method.

```swift
class MyCheckoutVC: UIViewController {
 func loadCheckout() {let intentConfig = PaymentSheet.IntentConfiguration(mode: .payment(amount: 1099, currency: "USD",)) { [weak self] confirmationToken in
      try await self?.handleConfirmationToken(confirmationToken)
    }
    var configuration = PaymentSheet.Configuration()
    configuration.returnURL = "your-app://stripe-redirect" // Use the return url you set up in the previous step
    PaymentSheet.FlowController.create(
      intentConfiguration: intentConfig,
      configuration: configuration
    ) { [weak self] result in
      switch result {
        case .failure(let error):
          print(error)
        case .success(let paymentSheetFlowController):
          self?.paymentSheetFlowController = paymentSheetFlowController
          // Update your UI paymentSheetFlowController.paymentOption.image and paymentSheetFlowController.paymentOption.label
      }
    }
  }

  func handleConfirmationToken(_ confirmationToken: STPConfirmationToken) async throws -> String {
    // ...explained later
  }
}
```

### Present the PaymentSheet

When a customer taps your “**Payment Method**” button, call `presentPaymentOptions` to collect payment details. When this completes, update your UI again with the `paymentOption` property.

```swift
paymentSheetFlowController.presentPaymentOptions(from: self) {
  // Update your UI using paymentSheetFlowController.paymentOption
}
```

### (Optional) Update payment details

If the customer performs actions that change the payment details (for example, applying a discount code or editing their cart), update the PaymentSheet.FlowController instance with the new values. This makes sure that our UI shows the correct values (for example, the **Pay** button, the Apple Pay UI), the appropriate payment methods display, and so on. By updating the instance instead of re-initializing the PaymentSheet.FlowController, the payment sheet preserves the customer’s payment details.

Call the `update` method with the updated IntentConfiguration object. While the update is in progress, don’t call `present` or `confirm` on the PaymentSheet.FlowController (for example, disable your “**Buy**” and “**Payment method**” buttons).

When the update completes, update your UI with the `paymentOption` property in case the customer’s previously selected payment method is no longer available. If the update failed, retry it.

```swift
// Create an updated IntentConfiguration
var updatedIntentConfig = oldIntentConfig
updatedIntentConfig.amount = 999
// Disable your "Buy" and "Payment method" buttons and call `update`
paymentSheetFlowController.update(intentConfiguration: updatedIntentConfig) { [weak self] error in
  if error != nil {
    // You must retry - until the update succeeds, the customer can't pay or select a payment method.
    // For example, you can automatically retry the update with an exponential back-off, or present the user with an alert that retries the update.
  } else {
    // Re-enable your "Buy" and "Payment method" buttons
    // Update your UI using paymentSheetFlowController.paymentOption.image and paymentSheetFlowController.paymentOption.label
  }
}
```

### Confirm the payment

When the customer taps your **Buy** button, call [paymentSheetFlowController.confirm](<https://stripe.dev/stripe-ios/stripepaymentsheet/documentation/stripepaymentsheet/paymentsheet/flowcontroller/confirm(from:completion:)>). This calls the `confirmationTokenConfirmHandler` callback you passed to `PaymentSheet.IntentConfiguration` with an [STPConfirmationToken](https://stripe.dev/stripe-ios/stripepayments/documentation/stripepayments/stpconfirmationtoken) object representing the customer’s payment details and preferences.

Implement this callback to send a request to your server, passing `confirmationToken.stripeId`. Your server creates and confirms a PaymentIntent and returns its client secret.

When the request returns, return your server response’s client secret or throw an error. The PaymentSheet completes any next actions required to complete the PaymentIntent using the client secret.

```swift
class MyCheckoutVC: UIViewController {
  // ...func didTapBuyButton() {
    paymentSheetFlowController.confirm(from: self) { paymentResult in
      switch paymentResult {
      case .completed:
        //Paymentcompleted - show a confirmation screen.
      case .failed(let error):
        // PaymentSheet encountered an unrecoverable error. You can display the error to the user, log it, and so on
        print(error)
      case .canceled:
        // Customer canceled - you should probably do nothing.
      }
    }
  }
func handleConfirmationToken(_ confirmationToken: STPConfirmationToken) async throws -> String {
    // Make a request to your own server. Pass confirmationToken.stripeId if using server-side confirmation.
    return try await fetchIntentClientSecret(...)
  }
}
```

The server code is explained in the following step.

## Create and submit the payment to Stripe [Server-side]

On your server, create and confirm a _PaymentIntent_ (The Payment Intents API tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by regulatory mandates, custom Radar fraud rules, or redirect-based payment methods) with an amount and currency. You can manage payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods). Stripe handles the return of eligible payment methods based on factors such as the transaction’s amount, currency, and payment flow. To prevent malicious customers from choosing their own prices, always decide how much to charge on the server-side (a trusted environment) and not the client.

If the call succeeds, return the PaymentIntent _client secret_ (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)). If the call fails, [handle the error](https://docs.stripe.com/error-handling.md) and return an error message with a brief explanation for your customer.

> Verify that all IntentConfiguration properties match your PaymentIntent (for example, `setup_future_usage`, `amount`, and `currency`).

### Handling client side arguments:

- `confirmation_token_id` - You can retrieve the ConfirmationToken object using this ID to perform your own validation or business logic.

#### Accounts v2

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
const express = require("express");
const app = express();

app.set("trust proxy", true);
app.use(express.json());

app.post("/create-confirm-intent", async (req, res) => {
  try {
    var args = {
      amount: 1099,
      currency: "usd",
      automatic_payment_methods: { enabled: true },
      confirm: true,
      confirmation_token: req.body.confirmation_token_id, // the ConfirmationToken ID sent by your client
    };
    const intent = await stripe.paymentIntents.create(args);
    res.json({
      client_secret: intent.client_secret,
    });
  } catch (err) {
    res.status(err.statusCode).json({ error: err.message });
  }
});

app.listen(3000, () => {
  console.log("Running on port 3000");
});
```

#### Customers v1

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
const express = require("express");
const app = express();

app.set("trust proxy", true);
app.use(express.json());

app.post("/create-confirm-intent", async (req, res) => {
  try {
    var args = {
      amount: 1099,
      currency: "usd",
      automatic_payment_methods: { enabled: true },
      confirm: true,
      confirmation_token: req.body.confirmation_token_id, // the ConfirmationToken ID sent by your client
    };
    const intent = await stripe.paymentIntents.create(args);
    res.json({
      client_secret: intent.client_secret,
    });
  } catch (err) {
    res.status(err.statusCode).json({ error: err.message });
  }
});

app.listen(3000, () => {
  console.log("Running on port 3000");
});
```

## Handle post-payment events [Server-side]

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the [Dashboard webhook tool](https://dashboard.stripe.com/webhooks) or follow the [webhook guide](https://docs.stripe.com/webhooks/quickstart.md) to receive these events and run actions, such as sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events is what enables you to accept [different types of payment methods](https://stripe.com/payments/payment-methods-guide) with a single integration.

In addition to handling the `payment_intent.succeeded` event, we recommend handling these other events when collecting payments with the Payment Element:

| Event                                                                                                                           | Description                                                                                                                                                                                                                                                                         | Action                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md?lang=php#event_types-payment_intent.succeeded)           | Sent when a customer successfully completes a payment.                                                                                                                                                                                                                              | Send the customer an order confirmation and _fulfill_ (Fulfillment is the process of providing the goods or services purchased by a customer, typically after payment is collected) their order. |
| [payment_intent.processing](https://docs.stripe.com/api/events/types.md?lang=php#event_types-payment_intent.processing)         | Sent when a customer successfully initiates a payment, but the payment has yet to complete. This event is most commonly sent when the customer initiates a bank debit. It’s followed by either a `payment_intent.succeeded` or `payment_intent.payment_failed` event in the future. | Send the customer an order confirmation that indicates their payment is pending. For digital goods, you might want to fulfill the order before waiting for payment to complete.                  |
| [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md?lang=php#event_types-payment_intent.payment_failed) | Sent when a customer attempts a payment, but the payment fails.                                                                                                                                                                                                                     | If a payment transitions from `processing` to `payment_failed`, offer the customer another attempt to pay.                                                                                       |

## Test the integration

#### Cards

| Card number         | Scenario                                                                                                                                                                                                                                                                                      | How to test                                                                                           |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| 4242424242424242    | The card payment succeeds and doesn’t require authentication.                                                                                                                                                                                                                                 | Fill out the credit card form using the credit card number with any expiration, CVC, and postal code. |
| 4000002500003155    | The card payment requires _authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase). | Fill out the credit card form using the credit card number with any expiration, CVC, and postal code. |
| 4000000000009995    | The card is declined with a decline code like `insufficient_funds`.                                                                                                                                                                                                                           | Fill out the credit card form using the credit card number with any expiration, CVC, and postal code. |
| 6205500000000000004 | The UnionPay card has a variable length of 13-19 digits.                                                                                                                                                                                                                                      | Fill out the credit card form using the credit card number with any expiration, CVC, and postal code. |

#### Bank redirects

| Payment method    | Scenario                                                                                                                                                                                        | How to test                                                                                                                                              |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Bancontact, iDEAL | Your customer fails to authenticate on the redirect page for a redirect-based and immediate notification payment method.                                                                        | Choose any redirect-based payment method, fill out the required details, and confirm the payment. Then click **Fail test payment** on the redirect page. |
| Pay by Bank       | Your customer successfully pays with a redirect-based and [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method.                      | Choose the payment method, fill out the required details, and confirm the payment. Then click **Complete test payment** on the redirect page.            |
| Pay by Bank       | Your customer fails to authenticate on the redirect page for a redirect-based and delayed notification payment method.                                                                          | Choose the payment method, fill out the required details, and confirm the payment. Then click **Fail test payment** on the redirect page.                |
| BLIK              | BLIK payments fail in a variety of ways—immediate failures (for example, the code is expired or invalid), delayed errors (the bank declines) or timeouts (the customer didn’t respond in time). | Use email patterns to [simulate the different failures.](https://docs.stripe.com/payments/blik/accept-a-payment.md#simulate-failures)                    |

#### Bank debits

| Payment method    | Scenario                                                                                          | How to test                                                                                                                                                                                       |
| ----------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SEPA Direct Debit | Your customer successfully pays with SEPA Direct Debit.                                           | Fill out the form using the account number `AT321904300235473204`. The confirmed PaymentIntent initially transitions to processing, then transitions to the succeeded status three minutes later. |
| SEPA Direct Debit | Your customer’s payment intent status transitions from `processing` to `requires_payment_method`. | Fill out the form using the account number `AT861904300235473202`.                                                                                                                                |

See [Testing](https://docs.stripe.com/testing.md) for additional information to test your integration.

## Enable card scanning

To enable card scanning support for iOS, set the `NSCameraUsageDescription` (**Privacy - Camera Usage Description**) in the `Info.plist` of your application, and provide a reason for accessing the camera (for example, “To scan cards”).

## Optional: Enable saved cards [Server-side] [Client-side]

`PaymentSheet` can allow the customer to save their card and can include the customer’s saved cards in available payment methods. The customer must have an associated customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/create.md#v2_create_accounts-configuration-customer) object or a [Customer](https://docs.stripe.com/api/customers/create.md) object on your server. To enable a checkbox that allows the customer to save their card, create a [CustomerSession](https://docs.stripe.com/api/customer_sessions.md), with `payment_method_save` set to `enabled`.

#### Accounts v2

```javascript
const stripe = require("stripe")("sk_test_your_secret_key");

app.post("/mobile-payment-element", async (req, res) => {
  // Use an existing Account ID if this is a returning customer.
  const customer_account = await stripe.v2.core.accounts.create();
  const customerSession = await stripe.customerSessions.create({
    customer_account: customer_account.id,
    components: {
      mobile_payment_element: {
        enabled: true,
        features: {
          payment_method_save: "enabled",
          payment_method_redisplay: "enabled",
          payment_method_remove: "enabled",
        },
      },
    },
  });

  res.json({
    customerSessionClientSecret: customerSession.client_secret,
    customer_account: customer_account.id,
  });
});
```

Next, configure PaymentSheet with the customer’s ID and the CustomerSession client secret.

```swift
@_spi(CustomerSessionBetaAccess) import StripePaymentSheet

var configuration = PaymentSheet.Configuration()
configuration.customer = .init(id: customerAccountId, customerSessionClientSecret: customerSessionClientSecret)

self.paymentSheet = PaymentSheet(..., configuration: configuration)
```

#### Customers v1

```javascript
const stripe = require("stripe")("sk_test_your_secret_key");

app.post("/mobile-payment-element", async (req, res) => {
  // Use an existing Customer ID if this is a returning customer.
  const customer = await stripe.customers.create();
  const customerSession = await stripe.customerSessions.create({
    customer: customer.id,
    components: {
      mobile_payment_element: {
        enabled: true,
        features: {
          payment_method_save: "enabled",
          payment_method_redisplay: "enabled",
          payment_method_remove: "enabled",
        },
      },
    },
  });

  res.json({
    customerSessionClientSecret: customerSession.client_secret,
    customer: customer.id,
  });
});
```

Next, configure PaymentSheet with the customer’s ID and the CustomerSession client secret.

```swift
@_spi(CustomerSessionBetaAccess) import StripePaymentSheet

var configuration = PaymentSheet.Configuration()
configuration.customer = .init(id: customerId, customerSessionClientSecret: customerSessionClientSecret)

self.paymentSheet = PaymentSheet(..., configuration: configuration)
```

## Optional: Allow delayed payment methods [Client-side]

_Delayed payment methods_ (A payment method that can't immediately return payment status when a customer attempts a transaction (for example, ACH debits). Businesses commonly hold an order in a pending state until payment is successful with these payment methods) don’t guarantee that you’ll receive funds from your customer at the end of the checkout either because they take time to settle (for example, US Bank Accounts, SEPA Debit, iDEAL, and Bancontact) or because they require customer action to complete (for example, OXXO, Konbini, and Boleto).

By default, PaymentSheet doesn’t display delayed payment methods. To opt in, set `allowsDelayedPaymentMethods` to true in your `PaymentSheet.Configuration`. This step alone doesn’t activate any specific payment methods; rather, it indicates that your app is able to handle them. For example, although OXXO isn’t supported by PaymentSheet, if it becomes supported and you’ve updated to the latest SDK version, your app will be able to display OXXO as a payment option without additional integration changes.

```swift
var configuration = PaymentSheet.Configuration()
configuration.allowsDelayedPaymentMethods = true

self.paymentSheet = PaymentSheet(..., configuration: configuration)
```

If the customer successfully uses one of these delayed payment methods in PaymentSheet, the payment result returned is `.completed`.

## Optional: Enable Apple Pay

> If your checkout screen has a dedicated **Apple Pay** button, follow the [Apple Pay guide](https://docs.stripe.com/apple-pay.md#present-payment-sheet) and use `ApplePayContext` to collect payment from your **Apple Pay** button. You can use `PaymentSheet` to handle other payment method types.

### Register for an Apple Merchant ID

Obtain an Apple Merchant ID by [registering for a new identifier](https://developer.apple.com/account/resources/identifiers/add/merchant) on the Apple Developer website.

Fill out the form with a description and identifier. Your description is for your own records and you can modify it in the future. Stripe recommends using the name of your app as the identifier (for example, `merchant.com.{{YOUR_APP_NAME}}`).

### Create a new Apple Pay certificate

Create a certificate for your app to encrypt payment data.

Go to the [iOS Certificate Settings](https://dashboard.stripe.com/settings/ios_certificates) in the Dashboard, click **Add new application**, and follow the guide.

Download a Certificate Signing Request (CSR) file to get a secure certificate from Apple that allows you to use Apple Pay.

One CSR file must be used to issue exactly one certificate. If you switch your Apple Merchant ID, you must go to the [iOS Certificate Settings](https://dashboard.stripe.com/settings/ios_certificates) in the Dashboard to obtain a new CSR and certificate.

### Integrate with Xcode

Add the Apple Pay capability to your app. In Xcode, open your project settings, click the **Signing & Capabilities** tab, and add the **Apple Pay** capability. You might be prompted to log in to your developer account at this point. Select the merchant ID you created earlier, and your app is ready to accept Apple Pay.
![](assets/xcode.a701d4c1922d19985e9c614a6f105bf1.png)

Enable the Apple Pay capability in Xcode

### Add Apple Pay

#### One-time payment

To add Apple Pay to PaymentSheet, set [applePay](https://stripe.dev/stripe-ios/stripe-paymentsheet/Classes/PaymentSheet/Configuration.html#/s:6Stripe12PaymentSheetC13ConfigurationV8applePayAC05ApplefD0VSgvp) after initializing `PaymentSheet.Configuration` with your Apple merchant ID and the [country code of your business](https://dashboard.stripe.com/settings/account).

#### iOS (Swift)

```swift
var configuration = PaymentSheet.Configuration()
configuration.applePay = .init(
  merchantId: "merchant.com.your_app_name",
  merchantCountryCode: "US"
)
```

#### Recurring payments

To add Apple Pay to PaymentSheet, set [applePay](https://stripe.dev/stripe-ios/stripe-paymentsheet/Classes/PaymentSheet/Configuration.html#/s:6Stripe12PaymentSheetC13ConfigurationV8applePayAC05ApplefD0VSgvp) after initializing `PaymentSheet.Configuration` with your Apple merchant ID and the [country code of your business](https://dashboard.stripe.com/settings/account).

Per [Apple’s guidelines](https://developer.apple.com/design/human-interface-guidelines/apple-pay#Supporting-subscriptions) for recurring payments, you must also set additional attributes on the `PKPaymentRequest`. Add a handler in [ApplePayConfiguration.paymentRequestHandlers](https://stripe.dev/stripe-ios/stripepaymentsheet/documentation/stripepaymentsheet/paymentsheet/applepayconfiguration/handlers/paymentrequesthandler) to configure the [PKPaymentRequest.paymentSummaryItems](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619231-paymentsummaryitems) with the amount you intend to charge (for example, 9.95 USD a month).

You can also adopt [merchant tokens](https://developer.apple.com/apple-pay/merchant-tokens/) by setting the `recurringPaymentRequest` or `automaticReloadPaymentRequest` properties on the `PKPaymentRequest`.

To learn more about how to use recurring payments with Apple Pay, see [Apple’s PassKit documentation](https://developer.apple.com/documentation/passkit/pkpaymentrequest).

#### iOS (Swift)

```swift
let customHandlers = PaymentSheet.ApplePayConfiguration.Handlers(
    paymentRequestHandler: { request in
        // PKRecurringPaymentSummaryItem is available on iOS 15 or later
        if #available(iOS 15.0, *) {
            let billing = PKRecurringPaymentSummaryItem(label: "My Subscription", amount: NSDecimalNumber(string: "59.99"))

            // Payment starts today
            billing.startDate = Date()

            // Payment ends in one year
            billing.endDate = Date().addingTimeInterval(60 * 60 * 24 * 365)

            // Pay once a month.
            billing.intervalUnit = .month
            billing.intervalCount = 1

            // recurringPaymentRequest is only available on iOS 16 or later
            if #available(iOS 16.0, *) {
                request.recurringPaymentRequest = PKRecurringPaymentRequest(paymentDescription: "Recurring",
                                                                            regularBilling: billing,
                                                                            managementURL: URL(string: "https://my-backend.example.com/customer-portal")!)
                request.recurringPaymentRequest?.billingAgreement = "You'll be billed $59.99 every month for the next 12 months. To cancel at any time, go to Account and click 'Cancel Membership.'"
            }
            request.paymentSummaryItems = [billing]
            request.currencyCode = "USD"
        } else {
            // On older iOS versions, set alternative summary items.
            request.paymentSummaryItems = [PKPaymentSummaryItem(label: "Monthly plan starting July 1, 2022", amount: NSDecimalNumber(string: "59.99"), type: .final)]
        }
        return request
    }
)
var configuration = PaymentSheet.Configuration()
configuration.applePay = .init(merchantId: "merchant.com.your_app_name",
                                merchantCountryCode: "US",
                                customHandlers: customHandlers)
```

### Order tracking

To add [order tracking](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/designing-order-tracking) information in iOS 16 or later, configure an [authorizationResultHandler](https://stripe.dev/stripe-ios/stripepaymentsheet/documentation/stripepaymentsheet/paymentsheet/applepayconfiguration/handlers/authorizationresulthandler) in your `PaymentSheet.ApplePayConfiguration.Handlers`. Stripe calls your implementation after the payment is complete, but before iOS dismisses the Apple Pay sheet.

In your `authorizationResultHandler` implementation, fetch the order details from your server for the completed order. Add the details to the provided [PKPaymentAuthorizationResult](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationresult) and return the modified result.

To learn more about order tracking, see [Apple’s Wallet Orders documentation](https://developer.apple.com/documentation/walletorders).

#### iOS (Swift)

```swift
let customHandlers = PaymentSheet.ApplePayConfiguration.Handlers(
    authorizationResultHandler: { result in
      do {
        // Fetch the order details from your service
        let myOrderDetails = try await MyAPIClient.shared.fetchOrderDetails(orderID: orderID)
        result.orderDetails = PKPaymentOrderDetails(
          orderTypeIdentifier: myOrderDetails.orderTypeIdentifier, // "com.myapp.order"
          orderIdentifier: myOrderDetails.orderIdentifier, // "ABC123-AAAA-1111"
          webServiceURL: myOrderDetails.webServiceURL, // "https://my-backend.example.com/apple-order-tracking-backend"
          authenticationToken: myOrderDetails.authenticationToken) // "abc123"
        // Return your modified PKPaymentAuthorizationResult
        return result
      } catch {
        return PKPaymentAuthorizationResult(status: .failure, errors: [error])
      }
    }
)
var configuration = PaymentSheet.Configuration()
configuration.applePay = .init(merchantId: "merchant.com.your_app_name",
                               merchantCountryCode: "US",
                               customHandlers: customHandlers)
```

## Optional: Customize the sheet

All customization is configured through the [PaymentSheet.Configuration](https://stripe.dev/stripe-ios/stripe-paymentsheet/Classes/PaymentSheet/Configuration.html) object.

### Appearance

Customize colors, fonts, and so on to match the look and feel of your app by using the [appearance API](https://docs.stripe.com/elements/appearance-api/mobile.md?platform=ios).

### Payment method layout

Configure the layout of payment methods in the sheet using [paymentMethodLayout](https://stripe.dev/stripe-ios/stripepaymentsheet/documentation/stripepaymentsheet/paymentsheet/configuration-swift.struct/paymentmethodlayout). You can display them horizontally, vertically, or let Stripe optimize the layout automatically.
![](assets/ios-mpe-payment-method-layouts.9d0513e2fcec5660378ba1824d952054.png)

#### Swift

```swift
var configuration = PaymentSheet.Configuration()
configuration.paymentMethodLayout = .automatic
```

### Collect users addresses

Collect local and international shipping or billing addresses from your customers using the [Address Element](https://docs.stripe.com/elements/address-element.md?platform=ios).

### Merchant display name

Specify a customer-facing business name by setting [merchantDisplayName](https://stripe.dev/stripe-ios/stripe-paymentsheet/Classes/PaymentSheet/Configuration.html#/s:18StripePaymentSheet0bC0C13ConfigurationV19merchantDisplayNameSSvp). By default, this is your app’s name.

#### Swift

```swift
var configuration = PaymentSheet.Configuration()
configuration.merchantDisplayName = "My app, Inc."
```

### Dark mode

`PaymentSheet` automatically adapts to the user’s system-wide appearance settings (light and dark mode). If your app doesn’t support dark mode, you can set [style](https://stripe.dev/stripe-ios/stripe-paymentsheet/Classes/PaymentSheet/Configuration.html#/s:18StripePaymentSheet0bC0C13ConfigurationV5styleAC18UserInterfaceStyleOvp) to `alwaysLight` or `alwaysDark` mode.

```swift
var configuration = PaymentSheet.Configuration()
configuration.style = .alwaysLight
```

### Default billing details

To set default values for billing details collected in the payment sheet, configure the `defaultBillingDetails` property. The `PaymentSheet` pre-populates its fields with the values that you provide.

```swift
var configuration = PaymentSheet.Configuration()
configuration.defaultBillingDetails.address.country = "US"
configuration.defaultBillingDetails.email = "foo@bar.com"
```

### Billing details collection

Use `billingDetailsCollectionConfiguration` to specify how you want to collect billing details in the payment sheet.

You can collect your customer’s name, email, phone number, and address.

If you only want to billing details required by the payment method, set `billingDetailsCollectionConfiguration.attachDefaultsToPaymentMethod` to true. In that case, the `PaymentSheet.Configuration.defaultBillingDetails` are set as the payment method’s [billing details](https://docs.stripe.com/api/payment_methods/object.md?lang=node#payment_method_object-billing_details).

If you want to collect additional billing details that aren’t necessarily required by the payment method, set `billingDetailsCollectionConfiguration.attachDefaultsToPaymentMethod` to false. In that case, the billing details collected through the `PaymentSheet` are set as the payment method’s billing details.

```swift
var configuration = PaymentSheet.Configuration()
configuration.defaultBillingDetails.email = "foo@bar.com"
configuration.billingDetailsCollectionConfiguration.name = .always
configuration.billingDetailsCollectionConfiguration.email = .never
configuration.billingDetailsCollectionConfiguration.address = .full
configuration.billingDetailsCollectionConfiguration.attachDefaultsToPaymentMethod = true
```

> Consult with your legal counsel regarding laws that apply to collecting information. Only collect phone numbers if you need them for the transaction.

## Optional: Enable CVC recollection on confirmation

To re-collect the CVC of a saved card during PaymentIntent confirmation, your integration must collect payment details before creating a PaymentIntent.

### Update the intent configuration

`PaymentSheet.IntentConfiguration` accepts an optional parameter that controls when to re-collect CVC for a saved card.

```swift
let intentConfig = PaymentSheet.IntentConfiguration(
  mode: .payment(amount: 1099, currency: "USD"),
  confirmHandler: { confirmationToken in
    // Handle ConfirmationToken...}, requireCVCRecollection: true)
```

### Update parameters of the intent creation

To re-collect the CVC when confirming payment, include both the `customerId` and `require_cvc_recollection` parameters during the creation of the PaymentIntent.

#### Accounts v2

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
const express = require("express");
const app = express();

app.set("trust proxy", true);
app.use(express.json());

app.post("/create-intent", async (req, res) => {
  try {
    var args = {
      amount: 1099,
      currency: "usd",
      automatic_payment_methods: { enabled: true },
      customer_account: customer_account.id,
      payment_method_options: {
        card: {
          require_cvc_recollection: true,
        },
      },
    };
    const intent = await stripe.paymentIntents.create(args);
    res.json({
      client_secret: intent.client_secret,
    });
  } catch (err) {
    res.status(err.statusCode).json({ error: err.message });
  }
});

app.listen(3000, () => {
  console.log("Running on port 3000");
});
```

#### Customers v1

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
const express = require("express");
const app = express();

app.set("trust proxy", true);
app.use(express.json());

app.post("/create-intent", async (req, res) => {
  try {
    var args = {
      amount: 1099,
      currency: "usd",
      automatic_payment_methods: { enabled: true },
      customer: customer.id,
      payment_method_options: {
        card: {
          require_cvc_recollection: true,
        },
      },
    };
    const intent = await stripe.paymentIntents.create(args);
    res.json({
      client_secret: intent.client_secret,
    });
  } catch (err) {
    res.status(err.statusCode).json({ error: err.message });
  }
});

app.listen(3000, () => {
  console.log("Running on port 3000");
});
```

# Collect and save a payment method

> This is a Collect and save a payment method for when platform is ios and type is setup. View the full page at https://docs.stripe.com/payments/mobile/finalize-payments-on-the-server?platform=ios&type=setup.

A SetupIntent flow allows you to collect payment method details and save them for future payments without creating a charge. In this integration, you build a custom flow where you render the Payment Element, create the _SetupIntent_ (The Setup Intents API lets you build dynamic flows for collecting payment method details for future payments. It tracks the lifecycle of a payment setup flow and can trigger additional authentication steps if required by law or by the payment method), and confirm saving the payment method on your server.

## Set up Stripe [Server-side] [Client-side]

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
1. Add the **StripePaymentSheet** product to the [target of your app](https://developer.apple.com/documentation/swift_packages/adding_package_dependencies_to_your_app).

#### CocoaPods

1. If you haven’t already, install the latest version of [CocoaPods](https://guides.cocoapods.org/using/getting-started.html).
1. If you don’t have an existing [Podfile](https://guides.cocoapods.org/syntax/podfile.html), run the following command to create one:
   ```bash
   pod init
   ```
1. Add this line to your `Podfile`:
   ```podfile
   pod 'StripePaymentSheet'
   ```
1. Run the following command:
   ```bash
   pod install
   ```
1. Don’t forget to use the `.xcworkspace` file to open your project in Xcode, instead of the `.xcodeproj` file, from here on out.
1. In the future, to update to the latest version of the SDK, run:
   ```bash
   pod update StripePaymentSheet
   ```

#### Carthage

1. If you haven’t already, install the latest version of [Carthage](https://github.com/Carthage/Carthage#installing-carthage).
1. Add this line to your `Cartfile`:
   ```cartfile
   github "stripe/stripe-ios"
   ```
1. Follow the [Carthage installation instructions](https://github.com/Carthage/Carthage#if-youre-building-for-ios-tvos-or-watchos). Make sure to embed all of the required frameworks listed [here](https://github.com/stripe/stripe-ios/tree/master/StripePaymentSheet/README.md#manual-linking).
1. In the future, to update to the latest version of the SDK, run the following command:
   ```bash
   carthage update stripe-ios --platform ios
   ```

#### Manual Framework

1. Head to our [GitHub releases page](https://github.com/stripe/stripe-ios/releases/latest) and download and unzip **Stripe.xcframework.zip**.
1. Drag **StripePaymentSheet.xcframework** to the **Embedded Binaries** section of the **General** settings in your Xcode project. Make sure to select **Copy items if needed**.
1. Repeat step 2 for all required frameworks listed [here](https://github.com/stripe/stripe-ios/tree/master/StripePaymentSheet/README.md#manual-linking).
1. In the future, to update to the latest version of our SDK, repeat steps 1–3.

> For details on the latest SDK release and past versions, see the [Releases](https://github.com/stripe/stripe-ios/releases) page on GitHub. To receive notifications when a new release is published, [watch releases](https://help.github.com/en/articles/watching-and-unwatching-releases-for-a-repository#watching-releases-for-a-repository) for the repository.

You also need to set your [publishable key](https://dashboard.stripe.com/apikeys) so that the SDK can make API calls to Stripe. To get started, you can hardcode the publishable key on the client while you’re integrating, but fetch the publishable key from your server in production.

```swift
// Set your publishable key: remember to change this to your live publishable key in production
// See your keys here: https://dashboard.stripe.com/apikeys
STPAPIClient.shared.publishableKey = "<<YOUR_PUBLISHABLE_KEY>>"
```

## Enable payment methods

View your [payment methods settings](https://dashboard.stripe.com/settings/payment_methods) and enable the payment methods you want to support. You need at least one payment method enabled to create a _SetupIntent_ (The Setup Intents API lets you build dynamic flows for collecting payment method details for future payments. It tracks the lifecycle of a payment setup flow and can trigger additional authentication steps if required by law or by the payment method).

By default, Stripe enables cards and other prevalent payment methods that can help you reach more customers, but we recommend turning on additional payment methods that are relevant for your business and customers. See [Payment method support](https://docs.stripe.com/payments/payment-methods/payment-method-support.md) for product and payment method support, and our [pricing page](https://stripe.com/pricing/local-payment-methods) for fees.

## Set up a return URL [Client-side]

The customer might navigate away from your app to authenticate (for example, in Safari or their banking app). To allow them to automatically return to your app after authenticating, [configure a custom URL scheme](https://developer.apple.com/documentation/xcode/defining-a-custom-url-scheme-for-your-app) and set up your app delegate to forward the URL to the SDK. Stripe doesn’t support [universal links](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content).

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

#### SwiftUI

#### Swift

```swift

@main
struct MyApp: App {
  var body: some Scene {
    WindowGroup {
      Text("Hello, world!").onOpenURL { incomingURL in
          let stripeHandled = StripeAPI.handleURLCallback(with: incomingURL)
          if (!stripeHandled) {
            // This was not a Stripe url – handle the URL normally as you would
          }
        }
    }
  }
}
```

Additionally, set the [returnURL](https://stripe.dev/stripe-ios/stripe-paymentsheet/Classes/PaymentSheet/Configuration.html#/s:6Stripe12PaymentSheetC13ConfigurationV9returnURLSSSgvp) on your [PaymentSheet.Configuration](https://stripe.dev/stripe-ios/stripe-paymentsheet/Classes/PaymentSheet/Configuration.html) object to the URL for your app.

```swift
var configuration = PaymentSheet.Configuration()
configuration.returnURL = "your-app://stripe-redirect"
```

## Create a customer [Server-side]

To set up a payment method for future payments, you must attach it to an object that represents your customer. When your customer creates an account or has their first transaction with your business, create either a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/create.md) object with the Accounts v2 API or a [Customer](https://docs.stripe.com/api/customers/create.md) object with the Customers API.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/connect/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const account = await stripe.v2.core.accounts.create({
  configuration: {
    customer: {},
  },
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create();
```

## Collect payment details [Client-side]

We offer two styles of integration. Choose one to continue.

| PaymentSheet                                                                                                                                | PaymentSheet.FlowController                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![PaymentSheet](assets/ios-overview.9e0d68d009dc005f73a6f5df69e00458.png)                          | ![PaymentSheet.FlowController](assets/ios-multi-step.cd631ea4f1cd8cf3f39b6b9e1e92b6c5.png)                                          |
| Displays a sheet to collect payment details and complete the setup. The button in the sheet says **Set up** and sets the payment method up. | Displays a sheet to collect payment details only. The button in the sheet says **Continue** and returns the customer to your app, where your own button completes the setup. |

#### PaymentSheet

### Initialize PaymentSheet

When you’re ready to set up a payment method (for example, when a customer taps your checkout button), initialize the PaymentSheet with a `PaymentSheet.Configuration` and a [PaymentSheet.IntentConfiguration](https://github.com/stripe/stripe-ios/blob/master/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheetIntentConfiguration.swift). The [Configuration](https://stripe.dev/stripe-ios/stripepaymentsheet/documentation/stripepaymentsheet/paymentsheet/configuration-swift.struct) object contains the general configuration for the PaymentSheet that typically doesn’t change between payments, such as the `returnURL`. The [IntentConfiguration](https://github.com/stripe/stripe-ios/blob/master/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheetIntentConfiguration.swift) object contains details about the specific setup, such as the currency, and a `confirmationTokenConfirmHandler` callback—for now, leave its implementation empty.

```swift
import StripePaymentSheet

class MyCheckoutVC: UIViewController {
  func didTapCheckoutButton() {let intentConfig = PaymentSheet.IntentConfiguration(mode: .setup(currency: "USD")) { [weak self] confirmationToken in
      try await self?.handleConfirmationToken(confirmationToken)
    }
    var configuration = PaymentSheet.Configuration()
    configuration.returnURL = "your-app://stripe-redirect" // Use the return url you set up in the previous step
    let paymentSheet = PaymentSheet(intentConfiguration: intentConfig, configuration: configuration)
  }
func handleConfirmationToken(_ confirmationToken: STPConfirmationToken) async throws -> String {
    // ...explained later
  }
}

```

### Present PaymentSheet

Next, present the PaymentSheet. The `present` method takes a completion block that’s called when the customer finishes setting up their payment method and dismisses the sheet. Implement the completion block to handle the result (for example, by showing a confirmation screen in the `.completed` case.)

```swift
class MyCheckoutVC: UIViewController {
  func didTapCheckoutButton() {
    // ...paymentSheet.present(from: self) { result in
      switch result {
        case .completed:
          //Setupcompleted - show a confirmation screen.
        case .failed(let error):
          print(error)
          // PaymentSheet encountered an unrecoverable error. You can display the error to the user, log it, and so on
        case .canceled:
          // Customer canceled - you should probably do nothing.
      }
    }
  }
}

```

### Confirm the payment details

When the customer taps the Setup button in the PaymentSheet, it calls the callback you passed to `PaymentSheet.IntentConfiguration` with an [STPConfirmationToken](https://stripe.dev/stripe-ios/stripepayments/documentation/stripepayments/stpconfirmationtoken) object representing the customer’s payment details and preferences.

Implement this callback to send a request to your server, passing `confirmationToken.stripeId`. Your server creates and confirms a SetupIntent and returns its client secret.

When the request returns, return your server response’s client secret or throw an error. The PaymentSheet completes any next actions required to complete the SetupIntent using the client secret or displays the localized error message in its UI (either [errorDescription](https://developer.apple.com/documentation/foundation/localizederror/2946895-errordescription) or [localizedDescription](https://developer.apple.com/documentation/foundation/nserror/1414418-localizeddescription)).

```swift
class MyCheckoutVC: UIViewController {
  // ...
func handleConfirmationToken(_ confirmationToken: STPConfirmationToken) async throws -> String {
    // Make a request to your own server. Pass confirmationToken.stripeId if using server-side confirmation.
    // Return the client secret or throw an error.
    return try await MyAPIClient.shared.createIntent(confirmationTokenId: confirmationToken.stripeId)
  }
}
```

#### PaymentSheet.FlowController

This integration assumes your checkout screen has two buttons—a “**Payment Method**” button that presents the PaymentSheet to collect payment details and a “**Buy**” button that completes the setup.

### Initialize PaymentSheet.FlowController

When your checkout screen loads, initialize `PaymentSheet.FlowController` with a `PaymentSheet.Configuration` and a `PaymentSheet.IntentConfiguration`. The [Configuration](https://stripe.dev/stripe-ios/stripepaymentsheet/documentation/stripepaymentsheet/paymentsheet/configuration-swift.struct) object contains general-purpose configuration for PaymentSheet that usually don’t change between payments, like `returnURL`. The [IntentConfiguration](https://github.com/stripe/stripe-ios/blob/master/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheetIntentConfiguration.swift) object contains details about the specific setup, like the currency, as well as a `confirmationTokenConfirmHandler` callback—for now, leave its implementation empty.

After `PaymentSheet.FlowController` initializes, update your “**Payment Method**” button with its `paymentOption`. This property contains an image and label representing the customer’s initially selected, default payment method.

```swift
class MyCheckoutVC: UIViewController {
 func loadCheckout() {let intentConfig = PaymentSheet.IntentConfiguration(mode: .setup(currency: "USD")) { [weak self] confirmationToken in
      try await self?.handleConfirmationToken(confirmationToken)
    }
    var configuration = PaymentSheet.Configuration()
    configuration.returnURL = "your-app://stripe-redirect" // Use the return url you set up in the previous step
    PaymentSheet.FlowController.create(
      intentConfiguration: intentConfig,
      configuration: configuration
    ) { [weak self] result in
      switch result {
        case .failure(let error):
          print(error)
        case .success(let paymentSheetFlowController):
          self?.paymentSheetFlowController = paymentSheetFlowController
          // Update your UI paymentSheetFlowController.paymentOption.image and paymentSheetFlowController.paymentOption.label
      }
    }
  }

  func handleConfirmationToken(_ confirmationToken: STPConfirmationToken) async throws -> String {
    // ...explained later
  }
}
```

### Present the PaymentSheet

When a customer taps your “**Payment Method**” button, call `presentPaymentOptions` to collect payment details. When this completes, update your UI again with the `paymentOption` property.

```swift
paymentSheetFlowController.presentPaymentOptions(from: self) {
  // Update your UI using paymentSheetFlowController.paymentOption
}
```

### (Optional) Update payment details

If the customer performs actions that change the payment details (for example, applying a discount code or editing their cart), update the PaymentSheet.FlowController instance with the new values. This makes sure that our UI shows the correct values (for example, the **Pay** button, the Apple Pay UI), the appropriate payment methods display, and so on. By updating the instance instead of re-initializing the PaymentSheet.FlowController, the payment sheet preserves the customer’s payment details.

Call the `update` method with the updated IntentConfiguration object. While the update is in progress, don’t call `present` or `confirm` on the PaymentSheet.FlowController (for example, disable your “**Buy**” and “**Payment method**” buttons).

When the update completes, update your UI with the `paymentOption` property in case the customer’s previously selected payment method is no longer available. If the update failed, retry it.

```swift
// Create an updated IntentConfiguration
var updatedIntentConfig = oldIntentConfig
updatedIntentConfig.amount = 999
// Disable your "Buy" and "Payment method" buttons and call `update`
paymentSheetFlowController.update(intentConfiguration: updatedIntentConfig) { [weak self] error in
  if error != nil {
    // You must retry - until the update succeeds, the customer can't pay or select a payment method.
    // For example, you can automatically retry the update with an exponential back-off, or present the user with an alert that retries the update.
  } else {
    // Re-enable your "Buy" and "Payment method" buttons
    // Update your UI using paymentSheetFlowController.paymentOption.image and paymentSheetFlowController.paymentOption.label
  }
}
```

### Confirm the payment details

When the customer taps your **Buy** button, call [paymentSheetFlowController.confirm](<https://stripe.dev/stripe-ios/stripepaymentsheet/documentation/stripepaymentsheet/paymentsheet/flowcontroller/confirm(from:completion:)>). This calls the `confirmationTokenConfirmHandler` callback you passed to `PaymentSheet.IntentConfiguration` with an [STPConfirmationToken](https://stripe.dev/stripe-ios/stripepayments/documentation/stripepayments/stpconfirmationtoken) object representing the customer’s payment details and preferences.

Implement this callback to send a request to your server, passing `confirmationToken.stripeId`. Your server creates and confirms a SetupIntent and returns its client secret.

When the request returns, return your server response’s client secret or throw an error. The PaymentSheet completes any next actions required to complete the SetupIntent using the client secret.

```swift
class MyCheckoutVC: UIViewController {
  // ...func didTapBuyButton() {
    paymentSheetFlowController.confirm(from: self) { paymentResult in
      switch paymentResult {
      case .completed:
        //Setupcompleted - show a confirmation screen.
      case .failed(let error):
        // PaymentSheet encountered an unrecoverable error. You can display the error to the user, log it, and so on
        print(error)
      case .canceled:
        // Customer canceled - you should probably do nothing.
      }
    }
  }
func handleConfirmationToken(_ confirmationToken: STPConfirmationToken) async throws -> String {
    // Make a request to your own server. Pass confirmationToken.stripeId if using server-side confirmation.
    return try await fetchIntentClientSecret(...)
  }
}
```

The server code is explained in the following step.

## Submit the payment details to Stripe [Server-side]

On your server, create and confirm a _SetupIntent_ (The Setup Intents API lets you build dynamic flows for collecting payment method details for future payments. It tracks the lifecycle of a payment setup flow and can trigger additional authentication steps if required by law or by the payment method). You can manage payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods). Stripe evaluates payment method restrictions and other parameters to determine the list of supported payment methods.

If the call succeeds, return the SetupIntent _client secret_ (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)). If the call fails, [handle the error](https://docs.stripe.com/error-handling.md) and return an error message with a brief explanation for your customer.

> Verify that all IntentConfiguration properties match your SetupIntent (for example, [usage](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-usage)).

### Handling client side arguments:

- `confirmation_token_id` - You can retrieve the ConfirmationToken object using this ID to perform your own validation or business logic.

#### Accounts v2

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
const express = require('express');
const app = express();

app.set('trust proxy', true);
app.use(express.json());

app.post('/create-confirm-intent', async (req, res) => {
  try {
    var args = {
      customer_account: ... // The Account ID you previously created
      automatic_payment_methods: {enabled: true},
      confirm: true,
      confirmation_token: req.body.confirmation_token_id, // the ConfirmationToken ID sent by your client
    };
    const intent = await stripe.setupIntents.create(args);
    res.json({
      client_secret: intent.client_secret,
    });
  } catch (err) {
    res.status(err.statusCode).json({ error: err.message })
  }
});

app.listen(3000, () => {
  console.log('Running on port 3000');
});
```

#### Customers v1

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
const express = require('express');
const app = express();

app.set('trust proxy', true);
app.use(express.json());

app.post('/create-confirm-intent', async (req, res) => {
  try {
    var args = {
      customer: ... // The Customer ID you previously created
      automatic_payment_methods: {enabled: true},
      confirm: true,
      confirmation_token: req.body.confirmation_token_id, // the ConfirmationToken ID sent by your client
    };
    const intent = await stripe.setupIntents.create(args);
    res.json({
      client_secret: intent.client_secret,
    });
  } catch (err) {
    res.status(err.statusCode).json({ error: err.message })
  }
});

app.listen(3000, () => {
  console.log('Running on port 3000');
});
```

## Charge the saved payment method later [Server-side]

> `bancontact` and `ideal` are one-time payment methods by default. When set up for future usage, they generate a `sepa_debit` reusable payment method type so you need to use `sepa_debit` to query for saved payment methods.

> #### Compliance
>
> You’re responsible for your compliance with all applicable laws, regulations, and network rules when saving a customer’s payment details. When rendering past payment methods to your end customer for future purchases, make sure you’re listing payment methods where you’ve collected consent from the customer to save the payment method details for this specific future use. To differentiate between payment methods attached to customers that can and can’t be presented to your end customer as a saved payment method for future purchases, use the [allow_redisplay](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-allow_redisplay) parameter.

To find a payment method to charge, list the payment methods associated with your customer. This example lists cards but you can list any supported [type](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-type).

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/connect/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

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

When you’re ready to charge your customer _off-session_ (A payment is described as off-session if it occurs without the direct involvement of the customer, using previously-collected payment information), use the customer’s ID and the `PaymentMethod` ID to create a `PaymentIntent` with the amount and currency of the payment. Set a few other parameters to make the off-session payment:

- Set [off_session](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-off_session) to `true` to indicate that the customer isn’t in your checkout flow during a payment attempt and can’t fulfill an authentication request made by a partner, such as a card issuer, bank, or other payment institution. If, during your checkout flow, a partner requests authentication, Stripe requests exemptions using customer information from a previous _on-session_ (A payment is described as on-session if it occurs while the customer is actively in your checkout flow and able to authenticate the payment method) transaction. If the conditions for exemption aren’t met, the `PaymentIntent` might throw an error.
- Set the value of the `PaymentIntent`’s [confirm](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-confirm) property to true, which causes confirmation to occur immediately when the `PaymentIntent` is created.
- Set [payment_method](https://docs.stripe.com/api.md#create_payment_intent-payment_method) to the `PaymentMethod`’s ID.
- Depending on how you represent customers in your integration, set either [customer_account](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-customer_account) to the ID of the customer-configured `Account` or [customer](https://docs.stripe.com/api.md#create_payment_intent-customer) to the ID of the `Customer`.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "usd",
  automatic_payment_methods: {
    enabled: true,
  },
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  payment_method: "{{PAYMENT_METHOD_ID}}",
  return_url: "https://example.com/order/123/complete",
  off_session: true,
  confirm: true,
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "usd",
  automatic_payment_methods: {
    enabled: true,
  },
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{PAYMENT_METHOD_ID}}",
  return_url: "https://example.com/order/123/complete",
  off_session: true,
  confirm: true,
});
```

## Test the integration

#### Cards

| Card number         | Scenario                                                                                                                                                                                                                                                                                      | How to test                                                                                           |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| 4242424242424242    | The card payment succeeds and doesn’t require authentication.                                                                                                                                                                                                                                 | Fill out the credit card form using the credit card number with any expiration, CVC, and postal code. |
| 4000002500003155    | The card payment requires _authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase). | Fill out the credit card form using the credit card number with any expiration, CVC, and postal code. |
| 4000000000009995    | The card is declined with a decline code like `insufficient_funds`.                                                                                                                                                                                                                           | Fill out the credit card form using the credit card number with any expiration, CVC, and postal code. |
| 6205500000000000004 | The UnionPay card has a variable length of 13-19 digits.                                                                                                                                                                                                                                      | Fill out the credit card form using the credit card number with any expiration, CVC, and postal code. |

#### Bank redirects

| Payment method    | Scenario                                                                                                                                                                                        | How to test                                                                                                                                              |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Bancontact, iDEAL | Your customer fails to authenticate on the redirect page for a redirect-based and immediate notification payment method.                                                                        | Choose any redirect-based payment method, fill out the required details, and confirm the payment. Then click **Fail test payment** on the redirect page. |
| Pay by Bank       | Your customer successfully pays with a redirect-based and [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method.                      | Choose the payment method, fill out the required details, and confirm the payment. Then click **Complete test payment** on the redirect page.            |
| Pay by Bank       | Your customer fails to authenticate on the redirect page for a redirect-based and delayed notification payment method.                                                                          | Choose the payment method, fill out the required details, and confirm the payment. Then click **Fail test payment** on the redirect page.                |
| BLIK              | BLIK payments fail in a variety of ways—immediate failures (for example, the code is expired or invalid), delayed errors (the bank declines) or timeouts (the customer didn’t respond in time). | Use email patterns to [simulate the different failures.](https://docs.stripe.com/payments/blik/accept-a-payment.md#simulate-failures)                    |

#### Bank debits

| Payment method    | Scenario                                                                                          | How to test                                                                                                                                                                                       |
| ----------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SEPA Direct Debit | Your customer successfully pays with SEPA Direct Debit.                                           | Fill out the form using the account number `AT321904300235473204`. The confirmed PaymentIntent initially transitions to processing, then transitions to the succeeded status three minutes later. |
| SEPA Direct Debit | Your customer’s payment intent status transitions from `processing` to `requires_payment_method`. | Fill out the form using the account number `AT861904300235473202`.                                                                                                                                |

See [Testing](https://docs.stripe.com/testing.md) for additional information to test your integration.

## Enable card scanning

To enable card scanning support for iOS, set the `NSCameraUsageDescription` (**Privacy - Camera Usage Description**) in the `Info.plist` of your application, and provide a reason for accessing the camera (for example, “To scan cards”).

## Optional: Enable saved cards [Server-side] [Client-side]

`PaymentSheet` can allow the customer to save their card and can include the customer’s saved cards in available payment methods. The customer must have an associated customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/create.md#v2_create_accounts-configuration-customer) object or a [Customer](https://docs.stripe.com/api/customers/create.md) object on your server. To enable a checkbox that allows the customer to save their card, create a [CustomerSession](https://docs.stripe.com/api/customer_sessions.md), with `payment_method_save` set to `enabled`.

#### Accounts v2

```javascript
const stripe = require("stripe")("sk_test_your_secret_key");

app.post("/mobile-payment-element", async (req, res) => {
  // Use an existing Account ID if this is a returning customer.
  const customer_account = await stripe.v2.core.accounts.create();
  const customerSession = await stripe.customerSessions.create({
    customer_account: customer_account.id,
    components: {
      mobile_payment_element: {
        enabled: true,
        features: {
          payment_method_save: "enabled",
          payment_method_redisplay: "enabled",
          payment_method_remove: "enabled",
        },
      },
    },
  });

  res.json({
    customerSessionClientSecret: customerSession.client_secret,
    customer_account: customer_account.id,
  });
});
```

Next, configure PaymentSheet with the customer’s ID and the CustomerSession client secret.

```swift
@_spi(CustomerSessionBetaAccess) import StripePaymentSheet

var configuration = PaymentSheet.Configuration()
configuration.customer = .init(id: customerAccountId, customerSessionClientSecret: customerSessionClientSecret)

self.paymentSheet = PaymentSheet(..., configuration: configuration)
```

#### Customers v1

```javascript
const stripe = require("stripe")("sk_test_your_secret_key");

app.post("/mobile-payment-element", async (req, res) => {
  // Use an existing Customer ID if this is a returning customer.
  const customer = await stripe.customers.create();
  const customerSession = await stripe.customerSessions.create({
    customer: customer.id,
    components: {
      mobile_payment_element: {
        enabled: true,
        features: {
          payment_method_save: "enabled",
          payment_method_redisplay: "enabled",
          payment_method_remove: "enabled",
        },
      },
    },
  });

  res.json({
    customerSessionClientSecret: customerSession.client_secret,
    customer: customer.id,
  });
});
```

Next, configure PaymentSheet with the customer’s ID and the CustomerSession client secret.

```swift
@_spi(CustomerSessionBetaAccess) import StripePaymentSheet

var configuration = PaymentSheet.Configuration()
configuration.customer = .init(id: customerId, customerSessionClientSecret: customerSessionClientSecret)

self.paymentSheet = PaymentSheet(..., configuration: configuration)
```

## Optional: Allow delayed payment methods [Client-side]

_Delayed payment methods_ (A payment method that can't immediately return payment status when a customer attempts a transaction (for example, ACH debits). Businesses commonly hold an order in a pending state until payment is successful with these payment methods) don’t guarantee that you’ll receive funds from your customer at the end of the checkout either because they take time to settle (for example, US Bank Accounts, SEPA Debit, iDEAL, and Bancontact) or because they require customer action to complete (for example, OXXO, Konbini, and Boleto).

By default, PaymentSheet doesn’t display delayed payment methods. To opt in, set `allowsDelayedPaymentMethods` to true in your `PaymentSheet.Configuration`. This step alone doesn’t activate any specific payment methods; rather, it indicates that your app is able to handle them. For example, although OXXO isn’t supported by PaymentSheet, if it becomes supported and you’ve updated to the latest SDK version, your app will be able to display OXXO as a payment option without additional integration changes.

```swift
var configuration = PaymentSheet.Configuration()
configuration.allowsDelayedPaymentMethods = true

self.paymentSheet = PaymentSheet(..., configuration: configuration)
```

If the customer successfully uses one of these delayed payment methods in PaymentSheet, the payment result returned is `.completed`.

## Optional: Enable Apple Pay

> If your checkout screen has a dedicated **Apple Pay** button, follow the [Apple Pay guide](https://docs.stripe.com/apple-pay.md#present-payment-sheet) and use `ApplePayContext` to collect payment from your **Apple Pay** button. You can use `PaymentSheet` to handle other payment method types.

### Register for an Apple Merchant ID

Obtain an Apple Merchant ID by [registering for a new identifier](https://developer.apple.com/account/resources/identifiers/add/merchant) on the Apple Developer website.

Fill out the form with a description and identifier. Your description is for your own records and you can modify it in the future. Stripe recommends using the name of your app as the identifier (for example, `merchant.com.{{YOUR_APP_NAME}}`).

### Create a new Apple Pay certificate

Create a certificate for your app to encrypt payment data.

Go to the [iOS Certificate Settings](https://dashboard.stripe.com/settings/ios_certificates) in the Dashboard, click **Add new application**, and follow the guide.

Download a Certificate Signing Request (CSR) file to get a secure certificate from Apple that allows you to use Apple Pay.

One CSR file must be used to issue exactly one certificate. If you switch your Apple Merchant ID, you must go to the [iOS Certificate Settings](https://dashboard.stripe.com/settings/ios_certificates) in the Dashboard to obtain a new CSR and certificate.

### Integrate with Xcode

Add the Apple Pay capability to your app. In Xcode, open your project settings, click the **Signing & Capabilities** tab, and add the **Apple Pay** capability. You might be prompted to log in to your developer account at this point. Select the merchant ID you created earlier, and your app is ready to accept Apple Pay.
![](assets/xcode.a701d4c1922d19985e9c614a6f105bf1.png)

Enable the Apple Pay capability in Xcode

### Add Apple Pay

#### One-time payment

To add Apple Pay to PaymentSheet, set [applePay](https://stripe.dev/stripe-ios/stripe-paymentsheet/Classes/PaymentSheet/Configuration.html#/s:6Stripe12PaymentSheetC13ConfigurationV8applePayAC05ApplefD0VSgvp) after initializing `PaymentSheet.Configuration` with your Apple merchant ID and the [country code of your business](https://dashboard.stripe.com/settings/account).

#### iOS (Swift)

```swift
var configuration = PaymentSheet.Configuration()
configuration.applePay = .init(
  merchantId: "merchant.com.your_app_name",
  merchantCountryCode: "US"
)
```

#### Recurring payments

To add Apple Pay to PaymentSheet, set [applePay](https://stripe.dev/stripe-ios/stripe-paymentsheet/Classes/PaymentSheet/Configuration.html#/s:6Stripe12PaymentSheetC13ConfigurationV8applePayAC05ApplefD0VSgvp) after initializing `PaymentSheet.Configuration` with your Apple merchant ID and the [country code of your business](https://dashboard.stripe.com/settings/account).

Per [Apple’s guidelines](https://developer.apple.com/design/human-interface-guidelines/apple-pay#Supporting-subscriptions) for recurring payments, you must also set additional attributes on the `PKPaymentRequest`. Add a handler in [ApplePayConfiguration.paymentRequestHandlers](https://stripe.dev/stripe-ios/stripepaymentsheet/documentation/stripepaymentsheet/paymentsheet/applepayconfiguration/handlers/paymentrequesthandler) to configure the [PKPaymentRequest.paymentSummaryItems](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619231-paymentsummaryitems) with the amount you intend to charge (for example, 9.95 USD a month).

You can also adopt [merchant tokens](https://developer.apple.com/apple-pay/merchant-tokens/) by setting the `recurringPaymentRequest` or `automaticReloadPaymentRequest` properties on the `PKPaymentRequest`.

To learn more about how to use recurring payments with Apple Pay, see [Apple’s PassKit documentation](https://developer.apple.com/documentation/passkit/pkpaymentrequest).

#### iOS (Swift)

```swift
let customHandlers = PaymentSheet.ApplePayConfiguration.Handlers(
    paymentRequestHandler: { request in
        // PKRecurringPaymentSummaryItem is available on iOS 15 or later
        if #available(iOS 15.0, *) {
            let billing = PKRecurringPaymentSummaryItem(label: "My Subscription", amount: NSDecimalNumber(string: "59.99"))

            // Payment starts today
            billing.startDate = Date()

            // Payment ends in one year
            billing.endDate = Date().addingTimeInterval(60 * 60 * 24 * 365)

            // Pay once a month.
            billing.intervalUnit = .month
            billing.intervalCount = 1

            // recurringPaymentRequest is only available on iOS 16 or later
            if #available(iOS 16.0, *) {
                request.recurringPaymentRequest = PKRecurringPaymentRequest(paymentDescription: "Recurring",
                                                                            regularBilling: billing,
                                                                            managementURL: URL(string: "https://my-backend.example.com/customer-portal")!)
                request.recurringPaymentRequest?.billingAgreement = "You'll be billed $59.99 every month for the next 12 months. To cancel at any time, go to Account and click 'Cancel Membership.'"
            }
            request.paymentSummaryItems = [billing]
            request.currencyCode = "USD"
        } else {
            // On older iOS versions, set alternative summary items.
            request.paymentSummaryItems = [PKPaymentSummaryItem(label: "Monthly plan starting July 1, 2022", amount: NSDecimalNumber(string: "59.99"), type: .final)]
        }
        return request
    }
)
var configuration = PaymentSheet.Configuration()
configuration.applePay = .init(merchantId: "merchant.com.your_app_name",
                                merchantCountryCode: "US",
                                customHandlers: customHandlers)
```

### Order tracking

To add [order tracking](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/designing-order-tracking) information in iOS 16 or later, configure an [authorizationResultHandler](https://stripe.dev/stripe-ios/stripepaymentsheet/documentation/stripepaymentsheet/paymentsheet/applepayconfiguration/handlers/authorizationresulthandler) in your `PaymentSheet.ApplePayConfiguration.Handlers`. Stripe calls your implementation after the payment is complete, but before iOS dismisses the Apple Pay sheet.

In your `authorizationResultHandler` implementation, fetch the order details from your server for the completed order. Add the details to the provided [PKPaymentAuthorizationResult](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationresult) and return the modified result.

To learn more about order tracking, see [Apple’s Wallet Orders documentation](https://developer.apple.com/documentation/walletorders).

#### iOS (Swift)

```swift
let customHandlers = PaymentSheet.ApplePayConfiguration.Handlers(
    authorizationResultHandler: { result in
      do {
        // Fetch the order details from your service
        let myOrderDetails = try await MyAPIClient.shared.fetchOrderDetails(orderID: orderID)
        result.orderDetails = PKPaymentOrderDetails(
          orderTypeIdentifier: myOrderDetails.orderTypeIdentifier, // "com.myapp.order"
          orderIdentifier: myOrderDetails.orderIdentifier, // "ABC123-AAAA-1111"
          webServiceURL: myOrderDetails.webServiceURL, // "https://my-backend.example.com/apple-order-tracking-backend"
          authenticationToken: myOrderDetails.authenticationToken) // "abc123"
        // Return your modified PKPaymentAuthorizationResult
        return result
      } catch {
        return PKPaymentAuthorizationResult(status: .failure, errors: [error])
      }
    }
)
var configuration = PaymentSheet.Configuration()
configuration.applePay = .init(merchantId: "merchant.com.your_app_name",
                               merchantCountryCode: "US",
                               customHandlers: customHandlers)
```

## Optional: Customize the sheet

All customization is configured through the [PaymentSheet.Configuration](https://stripe.dev/stripe-ios/stripe-paymentsheet/Classes/PaymentSheet/Configuration.html) object.

### Appearance

Customize colors, fonts, and so on to match the look and feel of your app by using the [appearance API](https://docs.stripe.com/elements/appearance-api/mobile.md?platform=ios).

### Payment method layout

Configure the layout of payment methods in the sheet using [paymentMethodLayout](https://stripe.dev/stripe-ios/stripepaymentsheet/documentation/stripepaymentsheet/paymentsheet/configuration-swift.struct/paymentmethodlayout). You can display them horizontally, vertically, or let Stripe optimize the layout automatically.
![](assets/ios-mpe-payment-method-layouts.9d0513e2fcec5660378ba1824d952054.png)

#### Swift

```swift
var configuration = PaymentSheet.Configuration()
configuration.paymentMethodLayout = .automatic
```

### Collect users addresses

Collect local and international shipping or billing addresses from your customers using the [Address Element](https://docs.stripe.com/elements/address-element.md?platform=ios).

### Merchant display name

Specify a customer-facing business name by setting [merchantDisplayName](https://stripe.dev/stripe-ios/stripe-paymentsheet/Classes/PaymentSheet/Configuration.html#/s:18StripePaymentSheet0bC0C13ConfigurationV19merchantDisplayNameSSvp). By default, this is your app’s name.

#### Swift

```swift
var configuration = PaymentSheet.Configuration()
configuration.merchantDisplayName = "My app, Inc."
```

### Dark mode

`PaymentSheet` automatically adapts to the user’s system-wide appearance settings (light and dark mode). If your app doesn’t support dark mode, you can set [style](https://stripe.dev/stripe-ios/stripe-paymentsheet/Classes/PaymentSheet/Configuration.html#/s:18StripePaymentSheet0bC0C13ConfigurationV5styleAC18UserInterfaceStyleOvp) to `alwaysLight` or `alwaysDark` mode.

```swift
var configuration = PaymentSheet.Configuration()
configuration.style = .alwaysLight
```

### Default billing details

To set default values for billing details collected in the payment sheet, configure the `defaultBillingDetails` property. The `PaymentSheet` pre-populates its fields with the values that you provide.

```swift
var configuration = PaymentSheet.Configuration()
configuration.defaultBillingDetails.address.country = "US"
configuration.defaultBillingDetails.email = "foo@bar.com"
```

### Billing details collection

Use `billingDetailsCollectionConfiguration` to specify how you want to collect billing details in the payment sheet.

You can collect your customer’s name, email, phone number, and address.

If you only want to billing details required by the payment method, set `billingDetailsCollectionConfiguration.attachDefaultsToPaymentMethod` to true. In that case, the `PaymentSheet.Configuration.defaultBillingDetails` are set as the payment method’s [billing details](https://docs.stripe.com/api/payment_methods/object.md?lang=node#payment_method_object-billing_details).

If you want to collect additional billing details that aren’t necessarily required by the payment method, set `billingDetailsCollectionConfiguration.attachDefaultsToPaymentMethod` to false. In that case, the billing details collected through the `PaymentSheet` are set as the payment method’s billing details.

```swift
var configuration = PaymentSheet.Configuration()
configuration.defaultBillingDetails.email = "foo@bar.com"
configuration.billingDetailsCollectionConfiguration.name = .always
configuration.billingDetailsCollectionConfiguration.email = .never
configuration.billingDetailsCollectionConfiguration.address = .full
configuration.billingDetailsCollectionConfiguration.attachDefaultsToPaymentMethod = true
```

> Consult with your legal counsel regarding laws that apply to collecting information. Only collect phone numbers if you need them for the transaction.

# Accept a payment

> This is a Accept a payment for when platform is android and type is payment. View the full page at https://docs.stripe.com/payments/mobile/finalize-payments-on-the-server?platform=android&type=payment.

The Payment Element allows you to accept multiple payment methods using a single integration. In this integration, you’ll build a custom payment flow where you render the Payment Element, create the _PaymentIntent_ (The Payment Intents API tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by regulatory mandates, custom Radar fraud rules, or redirect-based payment methods), and confirm the payment from your server.

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

You also need to set your [publishable key](https://dashboard.stripe.com/apikeys) so that the SDK can make API calls to Stripe. To get started quickly, you can hardcode this on the client while you’re integrating, but fetch the publishable key from your server in production.

```kotlin
// Set your publishable key: remember to change this to your live publishable key in production
// See your keys here: https://dashboard.stripe.com/apikeys
PaymentConfiguration.init(context, publishableKey = "<<YOUR_PUBLISHABLE_KEY>>")
```

## Enable payment methods

View your [payment methods settings](https://dashboard.stripe.com/settings/payment_methods) and enable the payment methods you want to support. You need at least one payment method enabled to create a _PaymentIntent_ (The Payment Intents API tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by regulatory mandates, custom Radar fraud rules, or redirect-based payment methods).

By default, Stripe enables cards and other prevalent payment methods that can help you reach more customers, but we recommend turning on additional payment methods that are relevant for your business and customers. See [Payment method support](https://docs.stripe.com/payments/payment-methods/payment-method-support.md) for product and payment method support, and our [pricing page](https://stripe.com/pricing/local-payment-methods) for fees.

## Collect payment details [Client-side]

We offer two styles of integration.

| PaymentSheet                                                                                                                                                 | PaymentSheet.FlowController                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ![PaymentSheet](assets/android-overview.471eaf89a760f5b6a757fd96b6bb9b60.png)                                       | ![PaymentSheet.FlowController](assets/android-multi-step.84d8a0a44b1baa596bda491322b6d9fd.png)                                        |
| Displays a sheet to collect payment details and complete the payment. The button label is **Pay** and the amount. Clicking the button completes the payment. | Displays a sheet to only collect payment details. The button label is **Continue**. Clicking it returns the customer to your app, where your own button completes the payment. |

#### PaymentSheet

#### Views (Classic)

### Initialize the PaymentSheet

Initialize the PaymentSheet and pass in a `CreateIntentCallback`. Leave the implementations empty for now.

```kotlin
class MyCheckoutActivity : AppCompatActivity() {
private lateinit var paymentSheet: PaymentSheet

  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    // ...
paymentSheet = PaymentSheet.Builder(::onPaymentSheetResult)
      .createIntentCallback { confirmationToken ->
        TODO() // You'll implement this later
      }
      .build(this)
  }

  fun onPaymentSheetResult(paymentSheetResult: PaymentSheetResult) {
    // You'll implement this later
  }
}

```

### Present the PaymentSheet

Next, present the PaymentSheet by calling `presentWithIntentConfiguration()` and pass in an [IntentConfiguration](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/-intent-configuration/index.html). The `IntentConfiguration` contains details about the specific `PaymentIntent`, such as the amount and currency.

```kotlin
class MyCheckoutActivity : AppCompatActivity() {

  // ...

  private fun handleCheckoutButtonPressed() {val intentConfig = PaymentSheet.IntentConfiguration(mode = PaymentSheet.IntentConfiguration.Mode.Payment(
        amount = 1099,
        currency = "usd",),// Other configuration options...
    )

    paymentSheet.presentWithIntentConfiguration(
      intentConfiguration = intentConfig,
      // Optional configuration - See the "Customize the sheet" section in this guide
      configuration = PaymentSheet.Configuration.Builder(
        merchantDisplayName = "Example Inc.",
      ).build()
    )
  }
}
```

### Confirm the Intent

When your customer taps the **Pay** button in PaymentSheet, it calls the `CreateIntentCallback` you passed above with a [ConfirmationToken](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-confirmation-token/index.html) that represents your customer’s payment details and preferences.

Implement this method to send a request to your server with `confirmationToken.id`. Your server creates and confirms a PaymentIntent and returns its client secret.

When you receive the response, return the response’s client secret or an error. The PaymentSheet performs any actions required to complete the PaymentIntent using the client secret, or displays the error in its UI.

```kotlin
class MyCheckoutActivity : AppCompatActivity() {

  private lateinit var paymentSheet: PaymentSheet

  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    // ...

    paymentSheet = PaymentSheet.Builder(::onPaymentSheetResult)
      .createIntentCallback { confirmationToken ->// Make a request to your server to create aPaymentIntentand return its client secret
        val networkResult = myNetworkClient.createIntent(
          confirmationTokenId = confirmationToken.id,
        )
        if (networkResult.isSuccess) {
            CreateIntentResult.Success(networkResult.clientSecret)
        } else {
            CreateIntentResult.Failure(networkResult.exception)
        }
      }
      .build(this)
  }

  fun onPaymentSheetResult(paymentSheetResult: PaymentSheetResult) {
    // You'll implement this later
  }
}
```

After your customer completes payment, the sheet closes, and PaymentSheet invokes the [PaymentSheetResultCallback](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet-result-callback/index.html) you provide with a [PaymentSheetResult](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet-result/index.html).

```kotlin
class MyCheckoutActivity : AppCompatActivity() {

  // ...

  fun onPaymentSheetResult(paymentSheetResult: PaymentSheetResult) {when(paymentSheetResult) {
      is PaymentSheetResult.Canceled -> {
        // Customer canceled - you should probably do nothing.
      }
      is PaymentSheetResult.Failed -> {
        print("Error: ${paymentSheetResult.error}")
        // PaymentSheet encountered an unrecoverable error. You can display the error to the user, log it, and so on
      }
      is PaymentSheetResult.Completed -> {
        // Display, for example, an order confirmation screen
        print("Completed")
      }
    }
  }
}
```

#### Jetpack Compose

### Initialize the PaymentSheet

Initialize the PaymentSheet using `remember` and pass in `PaymentSheet.Builder`. Leave the implementation of `resultCallback` and `createIntentCallback` empty for now.

```kotlin
import androidx.compose.runtime.*
import com.stripe.android.paymentsheet.PaymentSheet
import com.stripe.android.paymentsheet.rememberPaymentSheet

@Composable
fun CheckoutScreen() {
  val paymentSheet = remember {
    Builder(
      resultCallback = { paymentSheetResult ->
        // You'll implement this later
      }
    ).createIntentCallback { confirmationToken ->
      // You'll implement this later
    }
  }.build()
}
```

### Present the PaymentSheet

Next, present the PaymentSheet by calling `presentWithIntentConfiguration()` and pass an [IntentConfiguration](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/-intent-configuration/index.html). The `IntentConfiguration` contains details about the specific `PaymentIntent`, such as the amount and currency.

```kotlin
@Composable
fun CheckoutScreen() {
    val paymentSheet = remember {
      ...
    }.build()

  Button(
    onClick = {
      val intentConfig = PaymentSheet.IntentConfiguration(
        mode = PaymentSheet.IntentConfiguration.Mode.Payment(
          amount = 1099,
          currency = "usd",
        ),
      )
    }
  ) {
    Text("Checkout")
  }
}
```

### Confirm the Intent

When your customer taps the **Pay** button in the PaymentSheet, it calls `createIntentCallback` with a [ConfirmationToken](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-confirmation-token/index.html) object that represents the customer’s payment details and preferences.

Implement this callback to send a request to your server with `confirmationToken.id`. Your server creates and confirms a PaymentIntent and returns its client secret.

When you receive the response, return the client secret or an error. The PaymentSheet performs any actions required to complete the PaymentIntent using the client secret, or displays the error in its UI.

```kotlin
@Composable
fun CheckoutScreen() {
    val paymentSheet = remember {
      Builder(
        resultCallback = { paymentSheetResult ->
          // You'll implement this later
        }
      ).createIntentCallback { confirmationToken ->
        // Make a request to your server to create a PaymentIntent and return its client secret
        try {
          val response = myNetworkClient.createIntent(
            confirmationTokenId = confirmationToken.id,
          )
          CreateIntentResult.Success(response.clientSecret)
        } catch (e: Exception) {
          CreateIntentResult.Failure(
            cause = e,
            displayMessage = e.message
          )
        }
      }
    }.build()

  Button(
    onClick = {
      val intentConfig = PaymentSheet.IntentConfiguration(
        mode = PaymentSheet.IntentConfiguration.Mode.Payment(
          amount = 1099,
          currency = "usd",
        ),
      )

      paymentSheet.presentWithIntentConfiguration(
        intentConfiguration = intentConfig,
        configuration = PaymentSheet.Configuration.Builder(
          merchantDisplayName = "Example Inc.",
        ).build()
      )
    }
  ) {
    Text("Checkout")
  }
}
```

After your customer completes payment, the sheet closes, and the callback you pass to `PaymentSheet.Builder.resultCallback` is invoked with a [PaymentSheetResult](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet-result/index.html).

```kotlin
@Composable
fun CheckoutScreen() {
  val paymentSheet = remember {
    Builder(
      resultCallback = { paymentSheetResult ->
        when(paymentSheetResult) {
          is PaymentSheetResult.Canceled -> {
            // Customer canceled - you should probably do nothing.
          }
          is PaymentSheetResult.Failed -> {
            println("Error: ${paymentSheetResult.error}")
            // PaymentSheet encountered an unrecoverable error. You can display the error to the user, log it, and so on
          }
          is PaymentSheetResult.Completed -> {
            // Display, for example, an order confirmation screen
            println("Completed")
          }
        }
      }
    ).createIntentCallback { confirmationToken ->
      ... // previously implemented confirm intent code
    }
  }.build()
  ... // other code
}
```

#### PaymentSheet.FlowController

This integration assumes your checkout screen has two buttons: a **Payment Method** button that presents the PaymentSheet to collect payment details, and a **Buy** button that completes the payment.

#### Views (Classic)

### Initialize the PaymentSheet

Initialize the `PaymentSheet.FlowController` and pass in a `CreateIntentCallback`. Leave the implementations empty for now.

```kotlin
class MyCheckoutActivity : AppCompatActivity() {

  private lateinit var flowController: PaymentSheet.FlowController

  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    // ...
flowController = PaymentSheet.FlowController.Builder(
      resultCallback = ::onPaymentSheetResult,
      paymentOptionCallback = ::onPaymentOption
    )
      .createIntentCallback { confirmationToken ->
        TODO() // You'll implement this later
      }
      .build(this)
  }

  fun onPaymentSheetResult(paymentSheetResult: PaymentSheetResult) {
    // Explained later
  }

  fun onPaymentOption(paymentOption: PaymentOption?) {
    // Explained later
  }
}
```

After your checkout screen loads, configure the `PaymentSheet.FlowController` with an [IntentConfiguration](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/-intent-configuration/index.html). The `IntentConfiguration` contains details about the specific `PaymentIntent`, such as the amount and currency.

```kotlin
fun handleCheckoutLoaded(cartTotal: Long, currency: String) {flowController.configureWithIntentConfiguration(
    intentConfiguration = PaymentSheet.IntentConfiguration(mode = PaymentSheet.IntentConfiguration.Mode.Payment(
        amount = cartTotal,
        currency = currency,),),
    // Optional configuration - See the "Customize the sheet" section in this guide
    configuration = PaymentSheet.Configuration.Builder(
      merchantDisplayName = "Example Inc.",
    ).build(),
    callback = { success, error ->
      // If success, the FlowController was initialized correctly.
      // Use flowController.getPaymentOption() to populate your payment
      // method button.
    },
  )
}
```

When `PaymentSheet.FlowController` completes configuration, it invokes your callback. Then, you can populate your **Payment Method** button with `flowController.getPaymentOption()`, which includes an image and a label that represent your customer’s initial payment method selection.

### Present the PaymentSheet

When your customer taps your **Payment Method** button, call `presentPaymentOptions()` to collect payment details. Then, update your UI using the `paymentOption` property.

```kotlin
// ...
  flowController.presentPaymentOptions()
// ...
  fun onPaymentOption(paymentOption: PaymentOption?) {
    if (paymentOption != null) {
      paymentMethodButton.text = paymentOption.label
      paymentMethodButton.setCompoundDrawablesRelativeWithIntrinsicBounds(
        paymentOption.drawableResourceId,
        0,
        0,
        0
      )
    } else {
      paymentMethodButton.text = "Select"
      paymentMethodButton.setCompoundDrawablesRelativeWithIntrinsicBounds(
        null,
        null,
        null,
        null
      )
    }
  }
```

### Update payment details

If the customer changes the payment details (for example, by applying a discount code or editing their cart), update the `PaymentSheet.FlowController` instance to reflect the new values by calling `configureWithIntentConfiguration()` again to reflect the new values. This keeps the values shown in the UI in sync.

> Some payment methods, such as Google Pay, show the amount in the UI. If the customer changes the payment and you don’t update the `EmbeddedPaymentElement`, the UI displays incorrect values.

During configuration, don’t call `presentPaymentOptions()` or `confirm()` on `PaymentSheet.FlowController`. Disable your **Buy** and **Payment method** buttons, then enable them when your `ConfigCallback` runs.

If the update succeeds, use `flowController.getPaymentOption()` to update your UI because the customer’s previously selected payment method might be unavailable. If the update fails, retry it.

```kotlin
fun handleCartChanged(
  newCartTotal: Long,
  currency: String,
) {
  // Disable your "Buy" and "Payment method" buttons
  paymentMethodSelectionButton.isEnabled = false
  payButton.isEnabled = false

  // Update FlowController by configuring it again
  flowController.configureWithIntentConfiguration(
    intentConfiguration = PaymentSheet.IntentConfiguration(
      mode = PaymentSheet.IntentConfiguration.Mode.Payment(
        amount = newCartTotal,
        currency = currency
      ),
    ),
    configuration = PaymentSheet.Configuration.Builder(
        merchantDisplayName = "Example Inc.",
    ).build(),
    callback = { success, error ->
      // If success, the FlowController was updated correctly
      if (success) {
        paymentMethodSelectionButton.isEnabled = true

        val canPay = flowController.getPaymentOption() != null
        payButton.isEnabled = canPay
      } else {
        // You must retry - until the update succeeds, the customer can't pay or select a payment method.
        // For example, you can automatically retry the update with an exponential back-off, or present the user with an alert that retries the update.
      }
    },
  )
}
```

### Confirm the Intent

When your customer taps your **Buy** button, call `confirm()` to call the `CreateIntentCallback` you pass with a [ConfirmationToken](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-confirmation-token/index.html) object that represents your customer’s payment details and preferences.

Implement this method to send a request to your server with `confirmationToken.id`. Your server creates and confirms a PaymentIntent and returns its client secret.

When you receive the response, return the client secret or an error. PaymentSheet performs any actions required to complete the PaymentIntent using the client secret, or displays the error in the UI.

```kotlin
class MyCheckoutActivity : AppCompatActivity() {

  private lateinit var flowController: PaymentSheet.FlowController

  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    // …

    flowController = PaymentSheet.FlowController.Builder(
      resultCallback = ::onPaymentSheetResult,
      paymentOptionCallback = ::onPaymentOption
    )
      .createIntentCallback { confirmationToken ->// Make a request to your server to create aPaymentIntentand return its client secret
        try {
          val response = myNetworkClient.createIntent(
            confirmationTokenId = confirmationToken.id, // only required for server-side confirmation
          )
          CreateIntentResult.Success(response.clientSecret)
        } catch (e: Exception) {
            CreateIntentResult.Failure(
              cause = e,
              displayMessage = e.message
            )
        }
      }
      .build(this)
  }
}
```

After your customer completes the payment, the sheet closes, and the [PaymentSheetResultCallback](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet-result-callback/index.html) is invoked with a [PaymentSheetResult](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet-result/index.html).

```kotlin
class MyCheckoutActivity : AppCompatActivity() {

  // ...

  fun onPaymentSheetResult(paymentSheetResult: PaymentSheetResult) {when(paymentSheetResult) {
      is PaymentSheetResult.Canceled -> {
        // Customer canceled - you should probably do nothing.
      }
      is PaymentSheetResult.Failed -> {
        print("Error: ${paymentSheetResult.error}")
        // PaymentSheet encountered an unrecoverable error. You can display the error to the user, log it, and so on
      }
      is PaymentSheetResult.Completed -> {
        // Display, for example, an order confirmation screen
        print("Completed")
      }
    }
  }
}
```

The following step explains the server code.

#### Jetpack Compose

### Initialize the PaymentSheet.FlowController

Initialize the `PaymentSheet.FlowController` and pass in callbacks to `PaymentSheet.FlowController.Builder`. Leave the implementations empty for now.

```kotlin
import androidx.compose.runtime.*
import com.stripe.android.paymentsheet.PaymentSheet
import com.stripe.android.paymentsheet.PaymentSheet.FlowController.Builder
import com.stripe.android.paymentsheet.PaymentSheetResult
import com.stripe.android.paymentsheet.model.PaymentOption

private fun onPaymentSheetResult(paymentSheetResult: PaymentSheetResult) {
    // You'll implement this later
}

private fun onPaymentOption(paymentOption: PaymentOption?) {
    // You'll implement this later
}

@Composable
fun CheckoutScreen() {
  val flowController = remember{
      Builder(
        resultCallback = ::onPaymentSheetResult,
        paymentOptionCallback = ::onPaymentOption,
      ).createIntentCallback { confirmationToken ->
        // You'll implement this later
      }
  }.build()
}
```

After your checkout screen loads, configure the `PaymentSheet.FlowController` instance with an [IntentConfiguration](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/-intent-configuration/index.html). `IntentConfiguration` contains details about the specific `PaymentIntent`, such as the amount and currency.

```kotlin
@Composable
fun CheckoutScreen() {
  val flowController = remember{
    ...
  }.build()

  LaunchedEffect(Unit) {
    flowController.configureWithIntentConfiguration(
      intentConfiguration = PaymentSheet.IntentConfiguration(
        mode = PaymentSheet.IntentConfiguration.Mode.Payment(
          amount = 1099,
          currency = "usd",
        ),
      ),
      configuration = PaymentSheet.Configuration.Builder(
        merchantDisplayName = "Example Inc.",
      ).build(),
      callback = { success, error ->
        // If success, the FlowController was initialized correctly.
        // Use flowController.getPaymentOption() to populate your payment
        // method button.
      },
    )
  }
}
```

When the `PaymentSheet.FlowController` instance completes configuration, it calls `paymentOptionCallback`. At that point, `paymentOption` contains an image and a label that represent the customer’s initial payment method selection.

### Present the PaymentSheet

When a customer taps the **Payment Method** button, call `presentPaymentOptions()` to collect payment details. After it completes, `paymentOptionCallback` updates `paymentOption`. Then, update your UI.

```kotlin
...
  flowController.presentPaymentOptions()
...

fun onPaymentOption(paymentOption: PaymentOption?) {
  if (paymentOption != null) {
    paymentMethodButton.text = paymentOption.label
    paymentMethodButton.setCompoundDrawablesRelativeWithIntrinsicBounds(
      paymentOption.drawableResourceId,
      0,
      0,
      0
    )
  } else {
    paymentMethodButton.text = "Select"
    paymentMethodButton.setCompoundDrawablesRelativeWithIntrinsicBounds(
      null,
      null,
      null,
      null
    )
  }
}
```

### Update payment details

If the customer changes the payment details (for example, by applying a discount code or editing their cart), update the `PaymentSheet.FlowController` instance to reflect the new values by calling `configureWithIntentConfiguration()` again to reflect the new values. This keeps the values shown in the UI in sync.

> Some payment methods, such as Google Pay, show the amount in the UI. If the customer changes the payment and you don’t update the `PaymentSheet.FlowController`, the UI displays incorrect values.

During configuration, don’t call `presentPaymentOptions()` or `confirm()` on the `PaymentSheet.FlowController`.

If the update succeeds, `paymentOptionCallback` runs with the updated payment option. The selection might change if the customer’s previously selected payment method is no longer available. If the update fails, retry it.

```kotlin
fun updateCart(
  flowController: PaymentSheet.FlowController,
  newAmount: Long,
  onComplete: (Boolean) -> Unit
) {
  flowController.configureWithIntentConfiguration(
    intentConfiguration = PaymentSheet.IntentConfiguration(
      mode = PaymentSheet.IntentConfiguration.Mode.Payment(
        amount = newAmount,
        currency = "usd"
      ),
    ),
    configuration = PaymentSheet.Configuration.Builder(
      merchantDisplayName = "Example Inc.",
    ).build(),
    callback = { success, error ->
      // If success, the FlowController was updated correctly
      if (success) {
        paymentMethodSelectionButton.isEnabled = true

        val canPay = flowController.getPaymentOption() != null
        payButton.isEnabled = canPay
      } else {
        // You must retry - until the update succeeds, the customer can't pay or select a payment method.
        // For example, you can automatically retry the update with an exponential back-off, or present the user with an alert that retries the update.
      }
    },
  )
}
```

### Confirm the Intent

When your customer taps your **Buy** button, call `confirm()`. The PaymentSheet calls the `createIntentCallback` you pass with a [ConfirmationToken](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-confirmation-token/index.html) that represents your customer’s payment details and preferences.

```kotlin
@Composable
fun CheckoutScreen() {
  val flowController = remember{
    Builder(
      resultCallback = ::onPaymentSheetResult,
      paymentOptionCallback = ::onPaymentOption,
    ).createIntentCallback { confirmationToken ->
      // Make a request to your server to create a PaymentIntent and return its client secret
      try {
        val response = myNetworkClient.createIntent(
          confirmationTokenId = confirmationToken.id,
        )
        CreateIntentResult.Success(response.clientSecret)
      } catch (e: Exception) {
        CreateIntentResult.Failure(
          cause = e,
          displayMessage = e.message
        )
      }
    }
  }.build()

// Previous flowcontroller configuration code
  Column {
    // Payment method button...
    Button(
      onClick = {
        flowController.confirm()
      },
      enabled = paymentOption != null
    ) {
      Text("Buy")
    }
  }
}
```

After your customer completes the payment, the sheet closes, and `PaymentSheet.FlowController` invokes the callback you pass to `PaymentSheet.FlowController.Builder.resultCallback` with a [PaymentSheetResult](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet-result/index.html).

```kotlin
private fun onPaymentSheetResult(paymentSheetResult: PaymentSheetResult) {
  when(paymentSheetResult) {
    is PaymentSheetResult.Canceled -> {
      // Customer canceled - you should probably do nothing.
    }
    is PaymentSheetResult.Failed -> {
      println("Error: ${(paymentSheetResult as PaymentSheetResult.Failed).error}")
      // PaymentSheet encountered an unrecoverable error. You can display the error to the user, log it, and so on
    }
    is PaymentSheetResult.Completed -> {
      // Display, for example, an order confirmation screen
      println("Completed")
    }
    null -> {
      // No result yet
    }
  }
}
```

The following step explains the server code.

## Create and submit the payment to Stripe [Server-side]

On your server, create and confirm a _PaymentIntent_ (The Payment Intents API tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by regulatory mandates, custom Radar fraud rules, or redirect-based payment methods) with an amount and currency. You can manage payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods). Stripe handles the return of eligible payment methods based on factors such as the transaction’s amount, currency, and payment flow. To prevent malicious customers from choosing their own prices, always decide how much to charge on the server-side (a trusted environment) and not the client.

If the call succeeds, return the PaymentIntent _client secret_ (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)). If the call fails, [handle the error](https://docs.stripe.com/error-handling.md) and return an error message with a brief explanation for your customer.

> Verify that all IntentConfiguration properties match your PaymentIntent (for example, `setup_future_usage`, `amount`, and `currency`).

### Handling client side arguments:

- `confirmation_token_id` - You can retrieve the ConfirmationToken object using this ID to perform your own validation or business logic.

#### Accounts v2

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
const express = require("express");
const app = express();

app.set("trust proxy", true);
app.use(express.json());

app.post("/create-confirm-intent", async (req, res) => {
  try {
    var args = {
      amount: 1099,
      currency: "usd",
      automatic_payment_methods: { enabled: true },
      confirm: true,
      confirmation_token: req.body.confirmation_token_id, // the ConfirmationToken ID sent by your client
    };
    const intent = await stripe.paymentIntents.create(args);
    res.json({
      client_secret: intent.client_secret,
    });
  } catch (err) {
    res.status(err.statusCode).json({ error: err.message });
  }
});

app.listen(3000, () => {
  console.log("Running on port 3000");
});
```

#### Customers v1

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
const express = require("express");
const app = express();

app.set("trust proxy", true);
app.use(express.json());

app.post("/create-confirm-intent", async (req, res) => {
  try {
    var args = {
      amount: 1099,
      currency: "usd",
      automatic_payment_methods: { enabled: true },
      confirm: true,
      confirmation_token: req.body.confirmation_token_id, // the ConfirmationToken ID sent by your client
    };
    const intent = await stripe.paymentIntents.create(args);
    res.json({
      client_secret: intent.client_secret,
    });
  } catch (err) {
    res.status(err.statusCode).json({ error: err.message });
  }
});

app.listen(3000, () => {
  console.log("Running on port 3000");
});
```

## Handle post-payment events [Server-side]

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the [Dashboard webhook tool](https://dashboard.stripe.com/webhooks) or follow the [webhook guide](https://docs.stripe.com/webhooks/quickstart.md) to receive these events and run actions, such as sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events is what enables you to accept [different types of payment methods](https://stripe.com/payments/payment-methods-guide) with a single integration.

In addition to handling the `payment_intent.succeeded` event, we recommend handling these other events when collecting payments with the Payment Element:

| Event                                                                                                                           | Description                                                                                                                                                                                                                                                                         | Action                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md?lang=php#event_types-payment_intent.succeeded)           | Sent when a customer successfully completes a payment.                                                                                                                                                                                                                              | Send the customer an order confirmation and _fulfill_ (Fulfillment is the process of providing the goods or services purchased by a customer, typically after payment is collected) their order. |
| [payment_intent.processing](https://docs.stripe.com/api/events/types.md?lang=php#event_types-payment_intent.processing)         | Sent when a customer successfully initiates a payment, but the payment has yet to complete. This event is most commonly sent when the customer initiates a bank debit. It’s followed by either a `payment_intent.succeeded` or `payment_intent.payment_failed` event in the future. | Send the customer an order confirmation that indicates their payment is pending. For digital goods, you might want to fulfill the order before waiting for payment to complete.                  |
| [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md?lang=php#event_types-payment_intent.payment_failed) | Sent when a customer attempts a payment, but the payment fails.                                                                                                                                                                                                                     | If a payment transitions from `processing` to `payment_failed`, offer the customer another attempt to pay.                                                                                       |

## Test the integration

#### Cards

| Card number         | Scenario                                                                                                                                                                                                                                                                                      | How to test                                                                                           |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| 4242424242424242    | The card payment succeeds and doesn’t require authentication.                                                                                                                                                                                                                                 | Fill out the credit card form using the credit card number with any expiration, CVC, and postal code. |
| 4000002500003155    | The card payment requires _authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase). | Fill out the credit card form using the credit card number with any expiration, CVC, and postal code. |
| 4000000000009995    | The card is declined with a decline code like `insufficient_funds`.                                                                                                                                                                                                                           | Fill out the credit card form using the credit card number with any expiration, CVC, and postal code. |
| 6205500000000000004 | The UnionPay card has a variable length of 13-19 digits.                                                                                                                                                                                                                                      | Fill out the credit card form using the credit card number with any expiration, CVC, and postal code. |

#### Bank redirects

| Payment method    | Scenario                                                                                                                                                                                        | How to test                                                                                                                                              |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Bancontact, iDEAL | Your customer fails to authenticate on the redirect page for a redirect-based and immediate notification payment method.                                                                        | Choose any redirect-based payment method, fill out the required details, and confirm the payment. Then click **Fail test payment** on the redirect page. |
| Pay by Bank       | Your customer successfully pays with a redirect-based and [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method.                      | Choose the payment method, fill out the required details, and confirm the payment. Then click **Complete test payment** on the redirect page.            |
| Pay by Bank       | Your customer fails to authenticate on the redirect page for a redirect-based and delayed notification payment method.                                                                          | Choose the payment method, fill out the required details, and confirm the payment. Then click **Fail test payment** on the redirect page.                |
| BLIK              | BLIK payments fail in a variety of ways—immediate failures (for example, the code is expired or invalid), delayed errors (the bank declines) or timeouts (the customer didn’t respond in time). | Use email patterns to [simulate the different failures.](https://docs.stripe.com/payments/blik/accept-a-payment.md#simulate-failures)                    |

#### Bank debits

| Payment method    | Scenario                                                                                          | How to test                                                                                                                                                                                       |
| ----------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SEPA Direct Debit | Your customer successfully pays with SEPA Direct Debit.                                           | Fill out the form using the account number `AT321904300235473204`. The confirmed PaymentIntent initially transitions to processing, then transitions to the succeeded status three minutes later. |
| SEPA Direct Debit | Your customer’s payment intent status transitions from `processing` to `requires_payment_method`. | Fill out the form using the account number `AT861904300235473202`.                                                                                                                                |

See [Testing](https://docs.stripe.com/testing.md) for additional information to test your integration.

## Optional: Enable saved cards [Server-side] [Client-side]

`PaymentSheet` can allow the customer to save their card and can include the customer’s saved cards in available payment methods. The customer must have an associated customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/create.md#v2_create_accounts-configuration-customer) object or a [Customer](https://docs.stripe.com/api/customers/create.md) object on your server. To enable a checkbox that allows the customer to save their card, create a [CustomerSession](https://docs.stripe.com/api/customer_sessions.md), with `payment_method_save` set to `enabled`.

#### Accounts v2

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
const express = require("express");
const app = express();

app.set("trust proxy", true);
app.use(express.json());

app.post("/payment-sheet", async (req, res) => {
  // Use an existing Account ID if this is a returning customer.
  const customer_account = await stripe.v2.core.accounts.create();
  const customerSession = await stripe.customerSessions.create({
    customer_account: customer_account.id,
    components: {
      mobile_payment_element: {
        enabled: true,
        features: {
          payment_method_save: "enabled",
          payment_method_redisplay: "enabled",
          payment_method_remove: "enabled",
        },
      },
    },
  });

  res.json({
    customerSessionClientSecret: customerSession.client_secret,
    customer_account: customer_account.id,
  });
});
```

Next, present `PaymentSheet` with the customer’s ID and the `CustomerSession` client secret.

```kotlin
val configuration = PaymentSheet.Configuration.Builder(merchantDisplayName = "Powdur")
  .customer(
      PaymentSheet.CustomerConfiguration.createWithCustomerSession(
          id = customerAccountId,
          clientSecret = customerSessionClientSecret,
      )
  )
  .build()

paymentSheet.presentWithIntentConfiguration(
    intentConfiguration = // ... ,
    configuration = configuration,
)
```

#### Customers v1

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
const express = require("express");
const app = express();

app.set("trust proxy", true);
app.use(express.json());

app.post("/payment-sheet", async (req, res) => {
  // Use an existing Customer ID if this is a returning customer.
  const customer = await stripe.customers.create();
  const customerSession = await stripe.customerSessions.create({
    customer: customer.id,
    components: {
      mobile_payment_element: {
        enabled: true,
        features: {
          payment_method_save: "enabled",
          payment_method_redisplay: "enabled",
          payment_method_remove: "enabled",
        },
      },
    },
  });

  res.json({
    customerSessionClientSecret: customerSession.client_secret,
    customer: customer.id,
  });
});
```

Next, present `PaymentSheet` with the customer’s ID and the `CustomerSession` client secret.

```kotlin
val configuration = PaymentSheet.Configuration.Builder(merchantDisplayName = "Powdur")
  .customer(
      PaymentSheet.CustomerConfiguration.createWithCustomerSession(
          id = customerId,
          clientSecret = customerSessionClientSecret,
      )
  )
  .build()

paymentSheet.presentWithIntentConfiguration(
    intentConfiguration = // ... ,
    configuration = configuration,
)
```

## Optional: Allow delayed payment methods [Client-side]

_Delayed payment methods_ (A payment method that can't immediately return payment status when a customer attempts a transaction (for example, ACH debits). Businesses commonly hold an order in a pending state until payment is successful with these payment methods) don’t guarantee that you’ll receive funds from your customer at the end of checkout, either because they take time to settle (for example, US Bank Accounts, SEPA Debit, iDEAL, Bancontact, and Sofort) or because they require customer action to complete (for example, OXXO, Konbini, and Boleto).

By default, `PaymentSheet` doesn’t display delayed payment methods. To include the delayed payment methods that `PaymentSheet` supports, set `allowsDelayedPaymentMethods` to true in your `PaymentSheet.Configuration`.

```kotlin
val configuration = PaymentSheet.Configuration.Builder(merchantDisplayName = "Powdur")
  .allowsDelayedPaymentMethods(true)
  .build()
```

If the customer successfully uses a delayed payment method in a `PaymentSheet`, the payment result returned is `PaymentSheetResult.Completed`.

## Optional: Enable Google Pay

> If your checkout screen has a dedicated **Google Pay** button, follow the [Google Pay guide](https://docs.stripe.com/google-pay.md?platform=android). You can use Embedded Payment Element to handle other payment method types.

### Set up your integration

To use Google Pay, first enable the Google Pay API by adding the following to the `<application>` tag of your **AndroidManifest.xml**:

```xml
<application>
  ...
  <meta-data
    android:name="com.google.android.gms.wallet.api.enabled"
    android:value="true" />
</application>
```

For more details, see Google Pay’s [Set up Google Pay API](https://developers.google.com/pay/api/android/guides/setup) for Android.

### Add Google Pay

To add Google Pay to your integration, pass a [PaymentSheet.GooglePayConfiguration](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/-google-pay-configuration/index.html) with your Google Pay environment (production or test) and the [country code of your business](https://dashboard.stripe.com/settings/account) when initializing [PaymentSheet.Configuration](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/-configuration/index.html).

#### Kotlin

```kotlin
val googlePayConfiguration = PaymentSheet.GooglePayConfiguration(
  environment = PaymentSheet.GooglePayConfiguration.Environment.Test,
  countryCode = "US",
  currencyCode = "USD" // Required for Setup Intents, optional for Payment Intents
)
val configuration = PaymentSheet.Configuration.Builder(merchantDisplayName = "My merchant name")
  .googlePay(googlePayConfiguration)
  .build()
```

### Test Google Pay

Google allows you to make test payments through their [Test card suite](https://developers.google.com/pay/api/android/guides/resources/test-card-suite). The test suite supports using Stripe [test cards](https://docs.stripe.com/testing.md).

You must test Google Pay using a physical Android device instead of a simulated device, in a country where Google Pay is supported. Log in to a Google account on your test device with a real card saved to Google Wallet.

## Optional: Enable card scanning

To enable card scanning support, [request production access](https://developers.google.com/pay/api/android/guides/test-and-deploy/request-prod-access) to the Google Pay API from the [Google Pay and Wallet Console](https://pay.google.com/business/console?utm_source=devsite&utm_medium=devsite&utm_campaign=devsite).

- If you’ve enabled Google Pay, the card scanning feature is automatically available in our UI on eligible devices. To learn more about eligible devices, see the [Google Pay API constraints](https://developers.google.com/pay/payment-card-recognition/debit-credit-card-recognition)
- **Important:** The card scanning feature only appears in builds signed with the same signing key registered in the [Google Pay & Wallet Console](https://pay.google.com/business/console). Test or debug builds using different signing keys (for example, builds distributed through Firebase App Tester) won’t show the **Scan card** option. To test card scanning in pre-release builds, you must either:
  - Sign your test builds with your production signing key
  - Add your test signing key fingerprint to the Google Pay and Wallet Console

## Optional: Customize the sheet

All customization is configured using the [PaymentSheet.Configuration](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/-configuration/index.html) object.

### Appearance

Customize colors, fonts, and more to match the look and feel of your app by using the [appearance API](https://docs.stripe.com/elements/appearance-api/mobile.md?platform=android).

### Payment method layout

Configure the layout of payment methods in the sheet using [paymentMethodLayout](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/-configuration/-builder/index.html#2123253356%2FFunctions%2F2002900378). You can display them horizontally, vertically, or let Stripe optimize the layout automatically.
![](assets/android-mpe-payment-method-layouts.3bcfe828ceaad1a94e0572a22d91733f.png)

#### Kotlin

```kotlin
PaymentSheet.Configuration.Builder("Example, Inc.")
  .paymentMethodLayout(PaymentSheet.PaymentMethodLayout.Automatic)
  .build()
```

### Collect users addresses

Collect local and international shipping or billing addresses from your customers using the [Address Element](https://docs.stripe.com/elements/address-element.md?platform=android).

### Business display name

Specify a customer-facing business name by setting [merchantDisplayName](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/-configuration/index.html#-191101533%2FProperties%2F2002900378). By default, this is your app’s name.

#### Kotlin

```kotlin
PaymentSheet.Configuration.Builder(
  merchantDisplayName = "My app, Inc."
).build()
```

### Dark mode

By default, `PaymentSheet` automatically adapts to the user’s system-wide appearance settings (light and dark mode). You can change this by setting light or dark mode on your app:

#### Kotlin

```kotlin
// force dark
AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_YES)
// force light
AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_NO)
```

### Default billing details

To set default values for billing details collected in the payment sheet, configure the `defaultBillingDetails` property. The `PaymentSheet` pre-populates its fields with the values that you provide.

#### Kotlin

```kotlin
val address = PaymentSheet.Address(country = "US")
val billingDetails = PaymentSheet.BillingDetails(
  address = address,
  email = "foo@bar.com"
)
val configuration = PaymentSheet.Configuration.Builder(merchantDisplayName = "Merchant, Inc.")
  .defaultBillingDetails(billingDetails)
  .build()
```

### Configure collection of billing details

Use `BillingDetailsCollectionConfiguration` to specify how you want to collect billing details in the PaymentSheet.

You can collect your customer’s name, email, phone number, and address.

If you want to attach default billing details to the PaymentMethod object even when those fields aren’t collected in the UI, set `billingDetailsCollectionConfiguration.attachDefaultsToPaymentMethod` to `true`.

#### Kotlin

```kotlin
val billingDetails = PaymentSheet.BillingDetails(
  email = "foo@bar.com"
)
val billingDetailsCollectionConfiguration = BillingDetailsCollectionConfiguration(
  attachDefaultsToPaymentMethod = true,
  name = BillingDetailsCollectionConfiguration.CollectionMode.Always,
  email = BillingDetailsCollectionConfiguration.CollectionMode.Never,
  address = BillingDetailsCollectionConfiguration.AddressCollectionMode.Full,
)
val configuration = PaymentSheet.Configuration.Builder(merchantDisplayName = "Merchant, Inc.")
  .defaultBillingDetails(billingDetails)
  .billingDetailsCollectionConfiguration(billingDetailsCollectionConfiguration)
  .build()
```

> Consult with your legal counsel regarding laws that apply to collecting information. Only collect phone numbers if you need them for the transaction.

## Optional: Enable CVC recollection on confirmation

To re-collect the CVC of a saved card during PaymentIntent confirmation, your integration must collect payment details before creating a PaymentIntent.

### Update the intent configuration

`PaymentSheet.IntentConfiguration` accepts an optional parameter that controls when to re-collect CVC for a saved card.

```kotlin
val intentConfig = PaymentSheet.IntentConfiguration(
  mode = PaymentSheet.IntentConfiguration.Mode.Payment(
    amount = 1099,
    currency = "usd",
  ),requireCvcRecollection = true,
)
```

### Update parameters of the intent creation

To re-collect the CVC when confirming payment, include both the `customerId` and `require_cvc_recollection` parameters during the creation of the PaymentIntent.

#### Accounts v2

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
const express = require("express");
const app = express();

app.set("trust proxy", true);
app.use(express.json());

app.post("/create-intent", async (req, res) => {
  try {
    var args = {
      amount: 1099,
      currency: "usd",

      automatic_payment_methods: { enabled: true },
      customer_account: customer_account.id,
      payment_method_options: {
        card: {
          require_cvc_recollection: true,
        },
      },
    };
    const intent = await stripe.paymentIntents.create(args);
    res.json({
      client_secret: intent.client_secret,
    });
  } catch (err) {
    res.status(err.statusCode).json({ error: err.message });
  }
});

app.listen(3000, () => {
  console.log("Running on port 3000");
});
```

#### Customers v1

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
const express = require("express");
const app = express();

app.set("trust proxy", true);
app.use(express.json());

app.post("/create-intent", async (req, res) => {
  try {
    var args = {
      amount: 1099,
      currency: "usd",

      automatic_payment_methods: { enabled: true },
      customer: customer.id,
      payment_method_options: {
        card: {
          require_cvc_recollection: true,
        },
      },
    };
    const intent = await stripe.paymentIntents.create(args);
    res.json({
      client_secret: intent.client_secret,
    });
  } catch (err) {
    res.status(err.statusCode).json({ error: err.message });
  }
});

app.listen(3000, () => {
  console.log("Running on port 3000");
});
```

# Collect and save a payment method

> This is a Collect and save a payment method for when platform is android and type is setup. View the full page at https://docs.stripe.com/payments/mobile/finalize-payments-on-the-server?platform=android&type=setup.

A SetupIntent flow allows you to collect payment method details and save them for future payments without creating a charge. In this integration, you build a custom flow where you render the Payment Element, create the _SetupIntent_ (The Setup Intents API lets you build dynamic flows for collecting payment method details for future payments. It tracks the lifecycle of a payment setup flow and can trigger additional authentication steps if required by law or by the payment method), and confirm saving the payment method on your server.

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

You also need to set your [publishable key](https://dashboard.stripe.com/apikeys) so that the SDK can make API calls to Stripe. To get started quickly, you can hardcode this on the client while you’re integrating, but fetch the publishable key from your server in production.

```kotlin
// Set your publishable key: remember to change this to your live publishable key in production
// See your keys here: https://dashboard.stripe.com/apikeys
PaymentConfiguration.init(context, publishableKey = "<<YOUR_PUBLISHABLE_KEY>>")
```

## Enable payment methods

View your [payment methods settings](https://dashboard.stripe.com/settings/payment_methods) and enable the payment methods you want to support. You need at least one payment method enabled to create a _SetupIntent_ (The Setup Intents API lets you build dynamic flows for collecting payment method details for future payments. It tracks the lifecycle of a payment setup flow and can trigger additional authentication steps if required by law or by the payment method).

By default, Stripe enables cards and other prevalent payment methods that can help you reach more customers, but we recommend turning on additional payment methods that are relevant for your business and customers. See [Payment method support](https://docs.stripe.com/payments/payment-methods/payment-method-support.md) for product and payment method support, and our [pricing page](https://stripe.com/pricing/local-payment-methods) for fees.

## Create a Customer [Server-side]

To set up a payment method for future payments, you must attach it to an object that represents your customer. When your customer creates an account or has their first transaction with your business, create either a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/create.md) object with the Accounts v2 API or a [Customer](https://docs.stripe.com/api/customers/create.md) object with the Customers API.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/connect/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create();
```

## Collect payment details [Client-side]

We offer two styles of integration.

| PaymentSheet                                                                                                                 | PaymentSheet.FlowController                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![PaymentSheet](assets/android-overview.471eaf89a760f5b6a757fd96b6bb9b60.png)       | ![PaymentSheet.FlowController](assets/android-multi-step.84d8a0a44b1baa596bda491322b6d9fd.png)                                            |
| Displays a sheet to collect and save payment details. The button label is **Set up**. Clicking it saves the payment details. | Displays a sheet to only collect payment details. The button label is **Continue**. Clicking it returns the customer to your app, where your own button saves the payment details. |

#### PaymentSheet

#### Views (Classic)

### Initialize the PaymentSheet

Initialize the PaymentSheet and pass in a `CreateIntentCallback`. Leave the implementations empty for now.

```kotlin
class MyCheckoutActivity : AppCompatActivity() {
private lateinit var paymentSheet: PaymentSheet

  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    // ...
paymentSheet = PaymentSheet.Builder(::onPaymentSheetResult)
      .createIntentCallback { confirmationToken ->
        TODO() // You'll implement this later
      }
      .build(this)
  }

  fun onPaymentSheetResult(paymentSheetResult: PaymentSheetResult) {
    // You'll implement this later
  }
}

```

### Present the PaymentSheet

Next, present the PaymentSheet by calling `presentWithIntentConfiguration()` and pass in an [IntentConfiguration](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/-intent-configuration/index.html). The `IntentConfiguration` contains details about the specific `SetupIntent`, such as the currency.

```kotlin
class MyCheckoutActivity : AppCompatActivity() {

  // ...

  private fun handleCheckoutButtonPressed() {val intentConfig = PaymentSheet.IntentConfiguration(mode = PaymentSheet.IntentConfiguration.Mode.Setup(
        currency = "usd",
      ),// Other configuration options...
    )

    paymentSheet.presentWithIntentConfiguration(
      intentConfiguration = intentConfig,
      // Optional configuration - See the "Customize the sheet" section in this guide
      configuration = PaymentSheet.Configuration.Builder(
        merchantDisplayName = "Example Inc.",
      ).build()
    )
  }
}
```

### Confirm the Intent

When your customer taps the **Setup** button in PaymentSheet, it calls the `CreateIntentCallback` you passed above with a [ConfirmationToken](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-confirmation-token/index.html) that represents your customer’s payment details and preferences.

Implement this method to send a request to your server with `confirmationToken.id`. Your server creates and confirms a SetupIntent and returns its client secret.

When you receive the response, return the response’s client secret or an error. The PaymentSheet performs any actions required to complete the SetupIntent using the client secret, or displays the error in its UI.

```kotlin
class MyCheckoutActivity : AppCompatActivity() {

  private lateinit var paymentSheet: PaymentSheet

  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    // ...

    paymentSheet = PaymentSheet.Builder(::onPaymentSheetResult)
      .createIntentCallback { confirmationToken ->// Make a request to your server to create aSetupIntentand return its client secret
        val networkResult = myNetworkClient.createIntent(
          confirmationTokenId = confirmationToken.id,
        )
        if (networkResult.isSuccess) {
            CreateIntentResult.Success(networkResult.clientSecret)
        } else {
            CreateIntentResult.Failure(networkResult.exception)
        }
      }
      .build(this)
  }

  fun onPaymentSheetResult(paymentSheetResult: PaymentSheetResult) {
    // You'll implement this later
  }
}
```

After your customer saves a payment method, the sheet closes, and PaymentSheet invokes the [PaymentSheetResultCallback](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet-result-callback/index.html) you provide with a [PaymentSheetResult](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet-result/index.html).

```kotlin
class MyCheckoutActivity : AppCompatActivity() {

  // ...

  fun onPaymentSheetResult(paymentSheetResult: PaymentSheetResult) {when(paymentSheetResult) {
      is PaymentSheetResult.Canceled -> {
        // Customer canceled - you should probably do nothing.
      }
      is PaymentSheetResult.Failed -> {
        print("Error: ${paymentSheetResult.error}")
        // PaymentSheet encountered an unrecoverable error. You can display the error to the user, log it, and so on
      }
      is PaymentSheetResult.Completed -> {
        // Display, for example, an order confirmation screen
        print("Completed")
      }
    }
  }
}
```

#### Jetpack Compose

### Initialize the PaymentSheet

Initialize the PaymentSheet using `remember` and pass in `PaymentSheet.Builder`. Leave the implementation of `resultCallback` and `createIntentCallback` empty for now.

```kotlin
import androidx.compose.runtime.*
import com.stripe.android.paymentsheet.PaymentSheet
import com.stripe.android.paymentsheet.rememberPaymentSheet

@Composable
fun CheckoutScreen() {
  val paymentSheet = remember {
    Builder(
      resultCallback = { paymentSheetResult ->
        // You'll implement this later
      }
    ).createIntentCallback { confirmationToken ->
      // You'll implement this later
    }
  }.build()
}
```

### Present the PaymentSheet

Next, present the PaymentSheet by calling `presentWithIntentConfiguration()` and pass an [IntentConfiguration](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/-intent-configuration/index.html). The `IntentConfiguration` contains details about the specific `SetupIntent`, such as the currency.

```kotlin
@Composable
fun CheckoutScreen() {
    val paymentSheet = remember {
      ...
    }.build()

  Button(
    onClick = {
      val intentConfig = PaymentSheet.IntentConfiguration(
        mode = PaymentSheet.IntentConfiguration.Mode.Setup(
          currency = "usd",
        ),
      )
    }
  ) {
    Text("Checkout")
  }
}
```

### Confirm the Intent

When your customer taps the **Setup** button in the PaymentSheet, it calls `createIntentCallback` with a [ConfirmationToken](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-confirmation-token/index.html) object that represents the customer’s payment details and preferences.

Implement this callback to send a request to your server with `confirmationToken.id`. Your server creates and confirms a SetupIntent and returns its client secret.

When you receive the response, return the client secret or an error. The PaymentSheet performs any actions required to complete the SetupIntent using the client secret, or displays the error in its UI.

```kotlin
@Composable
fun CheckoutScreen() {
    val paymentSheet = remember {
      Builder(
        resultCallback = { paymentSheetResult ->
          // You'll implement this later
        }
      ).createIntentCallback { confirmationToken ->
        // Make a request to your server to create a PaymentIntent and return its client secret
        try {
          val response = myNetworkClient.createIntent(
            confirmationTokenId = confirmationToken.id,
          )
          CreateIntentResult.Success(response.clientSecret)
        } catch (e: Exception) {
          CreateIntentResult.Failure(
            cause = e,
            displayMessage = e.message
          )
        }
      }
    }.build()

  Button(
    onClick = {
      val intentConfig = PaymentSheet.IntentConfiguration(
        mode = PaymentSheet.IntentConfiguration.Mode.Setup(
          currency = "usd",
        ),
      )

      paymentSheet.presentWithIntentConfiguration(
        intentConfiguration = intentConfig,
        configuration = PaymentSheet.Configuration.Builder(
          merchantDisplayName = "Example Inc.",
        ).build()
      )
    }
  ) {
    Text("Checkout")
  }
}
```

After your customer saves a payment method, the sheet closes, and the callback you pass to `PaymentSheet.Builder.resultCallback` is invoked with a [PaymentSheetResult](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet-result/index.html).

```kotlin
@Composable
fun CheckoutScreen() {
  val paymentSheet = remember {
    Builder(
      resultCallback = { paymentSheetResult ->
        when(paymentSheetResult) {
          is PaymentSheetResult.Canceled -> {
            // Customer canceled - you should probably do nothing.
          }
          is PaymentSheetResult.Failed -> {
            println("Error: ${paymentSheetResult.error}")
            // PaymentSheet encountered an unrecoverable error. You can display the error to the user, log it, and so on
          }
          is PaymentSheetResult.Completed -> {
            // Display, for example, an order confirmation screen
            println("Completed")
          }
        }
      }
    ).createIntentCallback { confirmationToken ->
      ... // previously implemented confirm intent code
    }
  }.build()
  ... // other code
}
```

#### PaymentSheet.FlowController

This integration assumes your checkout screen has two buttons: a **Payment Method** button that presents the PaymentSheet to collect payment details, and a **Set up** button that sets up the payment details for future payment usage.

#### Views (Classic)

### Initialize the PaymentSheet

Initialize the `PaymentSheet.FlowController` and pass in a `CreateIntentCallback`. Leave the implementations empty for now.

```kotlin
class MyCheckoutActivity : AppCompatActivity() {

  private lateinit var flowController: PaymentSheet.FlowController

  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    // ...
flowController = PaymentSheet.FlowController.Builder(
      resultCallback = ::onPaymentSheetResult,
      paymentOptionCallback = ::onPaymentOption
    )
      .createIntentCallback { confirmationToken ->
        TODO() // You'll implement this later
      }
      .build(this)
  }

  fun onPaymentSheetResult(paymentSheetResult: PaymentSheetResult) {
    // Explained later
  }

  fun onPaymentOption(paymentOption: PaymentOption?) {
    // Explained later
  }
}
```

After your checkout screen loads, configure the `PaymentSheet.FlowController` with an [IntentConfiguration](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/-intent-configuration/index.html). The `IntentConfiguration` contains details about the specific `SetupIntent`, such as the currency.

```kotlin
fun handleCheckoutLoaded(currency: String) {flowController.configureWithIntentConfiguration(
    intentConfiguration = PaymentSheet.IntentConfiguration(mode = PaymentSheet.IntentConfiguration.Mode.Setup(
        currency = currency,
      ),),
    // Optional configuration - See the "Customize the sheet" section in this guide
    configuration = PaymentSheet.Configuration.Builder(
      merchantDisplayName = "Example Inc.",
    ).build(),
    callback = { success, error ->
      // If success, the FlowController was initialized correctly.
      // Use flowController.getPaymentOption() to populate your payment
      // method button.
    },
  )
}
```

When `PaymentSheet.FlowController` completes configuration, it invokes your callback. Then, you can populate your **Payment Method** button with `flowController.getPaymentOption()`, which includes an image and a label that represent your customer’s initial payment method selection.

### Present the PaymentSheet

When your customer taps your **Payment Method** button, call `presentPaymentOptions()` to collect payment details. Then, update your UI using the `paymentOption` property.

```kotlin
// ...
  flowController.presentPaymentOptions()
// ...
  fun onPaymentOption(paymentOption: PaymentOption?) {
    if (paymentOption != null) {
      paymentMethodButton.text = paymentOption.label
      paymentMethodButton.setCompoundDrawablesRelativeWithIntrinsicBounds(
        paymentOption.drawableResourceId,
        0,
        0,
        0
      )
    } else {
      paymentMethodButton.text = "Select"
      paymentMethodButton.setCompoundDrawablesRelativeWithIntrinsicBounds(
        null,
        null,
        null,
        null
      )
    }
  }
```

### Update payment details

If the customer changes the payment details (for example, by applying a discount code or editing their cart), update the `PaymentSheet.FlowController` instance to reflect the new values by calling `configureWithIntentConfiguration()` again to reflect the new values. This keeps the values shown in the UI in sync.

> Some payment methods, such as Google Pay, show the amount in the UI. If the customer changes the payment and you don’t update the `EmbeddedPaymentElement`, the UI displays incorrect values.

During configuration, don’t call `presentPaymentOptions()` or `confirm()` on `PaymentSheet.FlowController`. Disable your **Buy** and **Payment method** buttons, then enable them when your `ConfigCallback` runs.

If the update succeeds, use `flowController.getPaymentOption()` to update your UI because the customer’s previously selected payment method might be unavailable. If the update fails, retry it.

```kotlin
fun handleCartChanged(
  currency: String,
) {
  // Disable your "Buy" and "Payment method" buttons
  paymentMethodSelectionButton.isEnabled = false
  payButton.isEnabled = false

  // Update FlowController by configuring it again
  flowController.configureWithIntentConfiguration(
    intentConfiguration = PaymentSheet.IntentConfiguration(
      mode = PaymentSheet.IntentConfiguration.Mode.Setup(
        currency = currency,
      ),
    ),
    configuration = PaymentSheet.Configuration.Builder(
        merchantDisplayName = "Example Inc.",
    ).build(),
    callback = { success, error ->
      // If success, the FlowController was updated correctly
      if (success) {
        paymentMethodSelectionButton.isEnabled = true

        val canPay = flowController.getPaymentOption() != null
        payButton.isEnabled = canPay
      } else {
        // You must retry - until the update succeeds, the customer can't pay or select a payment method.
        // For example, you can automatically retry the update with an exponential back-off, or present the user with an alert that retries the update.
      }
    },
  )
}
```

### Confirm the Intent

When your customer taps your **Buy** button, call `confirm()` to call the `CreateIntentCallback` you pass with a [ConfirmationToken](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-confirmation-token/index.html) object that represents your customer’s payment details and preferences.

Implement this method to send a request to your server with `confirmationToken.id`. Your server creates and confirms a SetupIntent and returns its client secret.

When you receive the response, return the client secret or an error. PaymentSheet performs any actions required to complete the SetupIntent using the client secret, or displays the error in the UI.

```kotlin
class MyCheckoutActivity : AppCompatActivity() {

  private lateinit var flowController: PaymentSheet.FlowController

  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    // …

    flowController = PaymentSheet.FlowController.Builder(
      resultCallback = ::onPaymentSheetResult,
      paymentOptionCallback = ::onPaymentOption
    )
      .createIntentCallback { confirmationToken ->// Make a request to your server to create aSetupIntentand return its client secret
        try {
          val response = myNetworkClient.createIntent(
            confirmationTokenId = confirmationToken.id, // only required for server-side confirmation
          )
          CreateIntentResult.Success(response.clientSecret)
        } catch (e: Exception) {
            CreateIntentResult.Failure(
              cause = e,
              displayMessage = e.message
            )
        }
      }
      .build(this)
  }
}
```

After your customer finishes saving their payment method, the sheet closes, and the [PaymentSheetResultCallback](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet-result-callback/index.html) is invoked with a [PaymentSheetResult](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet-result/index.html).

```kotlin
class MyCheckoutActivity : AppCompatActivity() {

  // ...

  fun onPaymentSheetResult(paymentSheetResult: PaymentSheetResult) {when(paymentSheetResult) {
      is PaymentSheetResult.Canceled -> {
        // Customer canceled - you should probably do nothing.
      }
      is PaymentSheetResult.Failed -> {
        print("Error: ${paymentSheetResult.error}")
        // PaymentSheet encountered an unrecoverable error. You can display the error to the user, log it, and so on
      }
      is PaymentSheetResult.Completed -> {
        // Display, for example, an order confirmation screen
        print("Completed")
      }
    }
  }
}
```

The following step explains the server code.

#### Jetpack Compose

### Initialize the PaymentSheet.FlowController

Initialize the `PaymentSheet.FlowController` and pass in callbacks to `PaymentSheet.FlowController.Builder`. Leave the implementations empty for now.

```kotlin
import androidx.compose.runtime.*
import com.stripe.android.paymentsheet.PaymentSheet
import com.stripe.android.paymentsheet.PaymentSheet.FlowController.Builder
import com.stripe.android.paymentsheet.PaymentSheetResult
import com.stripe.android.paymentsheet.model.PaymentOption

private fun onPaymentSheetResult(paymentSheetResult: PaymentSheetResult) {
    // You'll implement this later
}

private fun onPaymentOption(paymentOption: PaymentOption?) {
    // You'll implement this later
}

@Composable
fun CheckoutScreen() {
  val flowController = remember{
      Builder(
        resultCallback = ::onPaymentSheetResult,
        paymentOptionCallback = ::onPaymentOption,
      ).createIntentCallback { confirmationToken ->
        // You'll implement this later
      }
  }.build()
}
```

After your checkout screen loads, configure the `PaymentSheet.FlowController` instance with an [IntentConfiguration](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/-intent-configuration/index.html). `IntentConfiguration` contains details about the specific `SetupIntent`, such as the currency.

```kotlin
@Composable
fun CheckoutScreen() {
  val flowController = remember{
    ...
  }.build()

  LaunchedEffect(Unit) {
    flowController.configureWithIntentConfiguration(
      intentConfiguration = PaymentSheet.IntentConfiguration(
        mode = PaymentSheet.IntentConfiguration.Mode.Setup(
          currency = "usd",
        ),
      ),
      configuration = PaymentSheet.Configuration.Builder(
        merchantDisplayName = "Example Inc.",
      ).build(),
      callback = { success, error ->
        // If success, the FlowController was initialized correctly.
        // Use flowController.getPaymentOption() to populate your payment
        // method button.
      },
    )
  }
}
```

When the `PaymentSheet.FlowController` instance completes configuration, it calls `paymentOptionCallback`. At that point, `paymentOption` contains an image and a label that represent the customer’s initial payment method selection.

### Present the PaymentSheet

When a customer taps the **Payment Method** button, call `presentPaymentOptions()` to collect payment details. After it completes, `paymentOptionCallback` updates `paymentOption`. Then, update your UI.

```kotlin
...
  flowController.presentPaymentOptions()
...

fun onPaymentOption(paymentOption: PaymentOption?) {
  if (paymentOption != null) {
    paymentMethodButton.text = paymentOption.label
    paymentMethodButton.setCompoundDrawablesRelativeWithIntrinsicBounds(
      paymentOption.drawableResourceId,
      0,
      0,
      0
    )
  } else {
    paymentMethodButton.text = "Select"
    paymentMethodButton.setCompoundDrawablesRelativeWithIntrinsicBounds(
      null,
      null,
      null,
      null
    )
  }
}
```

### Update payment details

If the customer changes the payment details (for example, by applying a discount code or editing their cart), update the `PaymentSheet.FlowController` instance to reflect the new values by calling `configureWithIntentConfiguration()` again to reflect the new values. This keeps the values shown in the UI in sync.

> Some payment methods, such as Google Pay, show the amount in the UI. If the customer changes the payment and you don’t update the `PaymentSheet.FlowController`, the UI displays incorrect values.

During configuration, don’t call `presentPaymentOptions()` or `confirm()` on the `PaymentSheet.FlowController`.

If the update succeeds, `paymentOptionCallback` runs with the updated payment option. The selection might change if the customer’s previously selected payment method is no longer available. If the update fails, retry it.

```kotlin
fun updateCart(
  flowController: PaymentSheet.FlowController,
  onComplete: (Boolean) -> Unit
) {
  flowController.configureWithIntentConfiguration(
    intentConfiguration = PaymentSheet.IntentConfiguration(
      mode = PaymentSheet.IntentConfiguration.Mode.Setup(
        currency = "usd",
      ),
    ),
    configuration = PaymentSheet.Configuration.Builder(
      merchantDisplayName = "Example Inc.",
    ).build(),
    callback = { success, error ->
      // If success, the FlowController was updated correctly
      if (success) {
        paymentMethodSelectionButton.isEnabled = true

        val canPay = flowController.getPaymentOption() != null
        payButton.isEnabled = canPay
      } else {
        // You must retry - until the update succeeds, the customer can't pay or select a payment method.
        // For example, you can automatically retry the update with an exponential back-off, or present the user with an alert that retries the update.
      }
    },
  )
}
```

### Confirm the Intent

When your customer taps your **Buy** button, call `confirm()`. The PaymentSheet calls the `createIntentCallback` you pass with a [ConfirmationToken](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-confirmation-token/index.html) that represents your customer’s payment details and preferences.

```kotlin
@Composable
fun CheckoutScreen() {
  val flowController = remember{
    Builder(
      resultCallback = ::onPaymentSheetResult,
      paymentOptionCallback = ::onPaymentOption,
    ).createIntentCallback { confirmationToken ->
      // Make a request to your server to create a SetupIntent and return its client secret
      try {
        val response = myNetworkClient.createIntent(
          confirmationTokenId = confirmationToken.id,
        )
        CreateIntentResult.Success(response.clientSecret)
      } catch (e: Exception) {
        CreateIntentResult.Failure(
          cause = e,
          displayMessage = e.message
        )
      }
    }
  }.build()

// Previous flowcontroller configuration code
  Column {
    // Payment method button...
    Button(
      onClick = {
        flowController.confirm()
      },
      enabled = paymentOption != null
    ) {
      Text("Set up")
    }
  }
}
```

After your customer saves their payment method, the sheet closes, and `PaymentSheet.FlowController` invokes the callback you pass to `PaymentSheet.FlowController.resultCallback` with a [PaymentSheetResult](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet-result/index.html).

```kotlin
private fun onPaymentSheetResult(paymentSheetResult: PaymentSheetResult) {
  when(paymentSheetResult) {
    is PaymentSheetResult.Canceled -> {
      // Customer canceled - you should probably do nothing.
    }
    is PaymentSheetResult.Failed -> {
      println("Error: ${(paymentSheetResult as PaymentSheetResult.Failed).error}")
      // PaymentSheet encountered an unrecoverable error. You can display the error to the user, log it, and so on
    }
    is PaymentSheetResult.Completed -> {
      // Display, for example, an order confirmation screen
      println("Completed")
    }
    null -> {
      // No result yet
    }
  }
}
```

The following step explains the server code.

## Submit the payment details to Stripe [Server-side]

On your server, create and confirm a _SetupIntent_ (The Setup Intents API lets you build dynamic flows for collecting payment method details for future payments. It tracks the lifecycle of a payment setup flow and can trigger additional authentication steps if required by law or by the payment method). You can manage payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods). Stripe evaluates payment method restrictions and other parameters to determine the list of supported payment methods.

If the call succeeds, return the SetupIntent _client secret_ (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)). If the call fails, [handle the error](https://docs.stripe.com/error-handling.md) and return an error message with a brief explanation for your customer.

> Verify that all IntentConfiguration properties match your SetupIntent (for example, [usage](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-usage)).

### Handling client side arguments:

- `confirmation_token_id` - You can retrieve the ConfirmationToken object using this ID to perform your own validation or business logic.

#### Accounts v2

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
const express = require('express');
const app = express();

app.set('trust proxy', true);
app.use(express.json());

app.post('/create-confirm-intent', async (req, res) => {
  try {
    var args = {
      customer_account: ... // The Account ID you previously created
      automatic_payment_methods: {enabled: true},
      confirm: true,
      confirmation_token: req.body.confirmation_token_id, // the ConfirmationToken ID sent by your client
    };
    const intent = await stripe.setupIntents.create(args);
    res.json({
      client_secret: intent.client_secret,
    });
  } catch (err) {
    res.status(err.statusCode).json({ error: err.message })
  }
});

app.listen(3000, () => {
  console.log('Running on port 3000');
});
```

#### Customers v1

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
const express = require('express');
const app = express();

app.set('trust proxy', true);
app.use(express.json());

app.post('/create-confirm-intent', async (req, res) => {
  try {
    var args = {
      customer: ... // The Customer ID you previously created
      automatic_payment_methods: {enabled: true},
      confirm: true,
      confirmation_token: req.body.confirmation_token_id, // the ConfirmationToken ID sent by your client
    };
    const intent = await stripe.setupIntents.create(args);
    res.json({
      client_secret: intent.client_secret,
    });
  } catch (err) {
    res.status(err.statusCode).json({ error: err.message })
  }
});

app.listen(3000, () => {
  console.log('Running on port 3000');
});
```

## Charge the saved payment method later [Server-side]

> `bancontact` and `ideal` are one-time payment methods by default. When set up for future usage, they generate a `sepa_debit` reusable payment method type so you need to use `sepa_debit` to query for saved payment methods.

> #### Compliance
>
> You’re responsible for your compliance with all applicable laws, regulations, and network rules when saving a customer’s payment details. When rendering past payment methods to your end customer for future purchases, make sure you’re listing payment methods where you’ve collected consent from the customer to save the payment method details for this specific future use. To differentiate between payment methods attached to customers that can and can’t be presented to your end customer as a saved payment method for future purchases, use the [allow_redisplay](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-allow_redisplay) parameter.

To find a payment method to charge, list the payment methods associated with your customer. This example lists cards but you can list any supported [type](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-type).

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/connect/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

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

When you’re ready to charge your customer _off-session_ (A payment is described as off-session if it occurs without the direct involvement of the customer, using previously-collected payment information), use the customer’s ID and the `PaymentMethod` ID to create a `PaymentIntent` with the amount and currency of the payment. Set a few other parameters to make the off-session payment:

- Set [off_session](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-off_session) to `true` to indicate that the customer isn’t in your checkout flow during a payment attempt and can’t fulfill an authentication request made by a partner, such as a card issuer, bank, or other payment institution. If, during your checkout flow, a partner requests authentication, Stripe requests exemptions using customer information from a previous _on-session_ (A payment is described as on-session if it occurs while the customer is actively in your checkout flow and able to authenticate the payment method) transaction. If the conditions for exemption aren’t met, the `PaymentIntent` might throw an error.
- Set the value of the `PaymentIntent`’s [confirm](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-confirm) property to true, which causes confirmation to occur immediately when the `PaymentIntent` is created.
- Set [payment_method](https://docs.stripe.com/api.md#create_payment_intent-payment_method) to the `PaymentMethod`’s ID.
- Depending on how you represent customers in your integration, set either [customer_account](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-customer_account) to the ID of the customer-configured `Account` or [customer](https://docs.stripe.com/api.md#create_payment_intent-customer) to the ID of the `Customer`.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "usd",
  automatic_payment_methods: {
    enabled: true,
  },
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  payment_method: "{{PAYMENT_METHOD_ID}}",
  return_url: "https://example.com/order/123/complete",
  off_session: true,
  confirm: true,
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "usd",
  automatic_payment_methods: {
    enabled: true,
  },
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{PAYMENT_METHOD_ID}}",
  return_url: "https://example.com/order/123/complete",
  off_session: true,
  confirm: true,
});
```

## Test the integration

#### Cards

| Card number         | Scenario                                                                                                                                                                                                                                                                                      | How to test                                                                                           |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| 4242424242424242    | The card payment succeeds and doesn’t require authentication.                                                                                                                                                                                                                                 | Fill out the credit card form using the credit card number with any expiration, CVC, and postal code. |
| 4000002500003155    | The card payment requires _authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase). | Fill out the credit card form using the credit card number with any expiration, CVC, and postal code. |
| 4000000000009995    | The card is declined with a decline code like `insufficient_funds`.                                                                                                                                                                                                                           | Fill out the credit card form using the credit card number with any expiration, CVC, and postal code. |
| 6205500000000000004 | The UnionPay card has a variable length of 13-19 digits.                                                                                                                                                                                                                                      | Fill out the credit card form using the credit card number with any expiration, CVC, and postal code. |

#### Bank redirects

| Payment method    | Scenario                                                                                                                                                                                        | How to test                                                                                                                                              |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Bancontact, iDEAL | Your customer fails to authenticate on the redirect page for a redirect-based and immediate notification payment method.                                                                        | Choose any redirect-based payment method, fill out the required details, and confirm the payment. Then click **Fail test payment** on the redirect page. |
| Pay by Bank       | Your customer successfully pays with a redirect-based and [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method.                      | Choose the payment method, fill out the required details, and confirm the payment. Then click **Complete test payment** on the redirect page.            |
| Pay by Bank       | Your customer fails to authenticate on the redirect page for a redirect-based and delayed notification payment method.                                                                          | Choose the payment method, fill out the required details, and confirm the payment. Then click **Fail test payment** on the redirect page.                |
| BLIK              | BLIK payments fail in a variety of ways—immediate failures (for example, the code is expired or invalid), delayed errors (the bank declines) or timeouts (the customer didn’t respond in time). | Use email patterns to [simulate the different failures.](https://docs.stripe.com/payments/blik/accept-a-payment.md#simulate-failures)                    |

#### Bank debits

| Payment method    | Scenario                                                                                          | How to test                                                                                                                                                                                       |
| ----------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SEPA Direct Debit | Your customer successfully pays with SEPA Direct Debit.                                           | Fill out the form using the account number `AT321904300235473204`. The confirmed PaymentIntent initially transitions to processing, then transitions to the succeeded status three minutes later. |
| SEPA Direct Debit | Your customer’s payment intent status transitions from `processing` to `requires_payment_method`. | Fill out the form using the account number `AT861904300235473202`.                                                                                                                                |

See [Testing](https://docs.stripe.com/testing.md) for additional information to test your integration.

## Optional: Enable saved cards [Server-side] [Client-side]

`PaymentSheet` can allow the customer to save their card and can include the customer’s saved cards in available payment methods. The customer must have an associated customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/create.md#v2_create_accounts-configuration-customer) object or a [Customer](https://docs.stripe.com/api/customers/create.md) object on your server. To enable a checkbox that allows the customer to save their card, create a [CustomerSession](https://docs.stripe.com/api/customer_sessions.md), with `payment_method_save` set to `enabled`.

#### Accounts v2

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
const express = require("express");
const app = express();

app.set("trust proxy", true);
app.use(express.json());

app.post("/payment-sheet", async (req, res) => {
  // Use an existing Account ID if this is a returning customer.
  const customer_account = await stripe.v2.core.accounts.create();
  const customerSession = await stripe.customerSessions.create({
    customer_account: customer_account.id,
    components: {
      mobile_payment_element: {
        enabled: true,
        features: {
          payment_method_save: "enabled",
          payment_method_redisplay: "enabled",
          payment_method_remove: "enabled",
        },
      },
    },
  });

  res.json({
    customerSessionClientSecret: customerSession.client_secret,
    customer_account: customer_account.id,
  });
});
```

Next, present `PaymentSheet` with the customer’s ID and the `CustomerSession` client secret.

```kotlin
val configuration = PaymentSheet.Configuration.Builder(merchantDisplayName = "Powdur")
  .customer(
      PaymentSheet.CustomerConfiguration.createWithCustomerSession(
          id = customerAccountId,
          clientSecret = customerSessionClientSecret,
      )
  )
  .build()

paymentSheet.presentWithIntentConfiguration(
    intentConfiguration = // ... ,
    configuration = configuration,
)
```

#### Customers v1

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
const express = require("express");
const app = express();

app.set("trust proxy", true);
app.use(express.json());

app.post("/payment-sheet", async (req, res) => {
  // Use an existing Customer ID if this is a returning customer.
  const customer = await stripe.customers.create();
  const customerSession = await stripe.customerSessions.create({
    customer: customer.id,
    components: {
      mobile_payment_element: {
        enabled: true,
        features: {
          payment_method_save: "enabled",
          payment_method_redisplay: "enabled",
          payment_method_remove: "enabled",
        },
      },
    },
  });

  res.json({
    customerSessionClientSecret: customerSession.client_secret,
    customer: customer.id,
  });
});
```

Next, present `PaymentSheet` with the customer’s ID and the `CustomerSession` client secret.

```kotlin
val configuration = PaymentSheet.Configuration.Builder(merchantDisplayName = "Powdur")
  .customer(
      PaymentSheet.CustomerConfiguration.createWithCustomerSession(
          id = customerId,
          clientSecret = customerSessionClientSecret,
      )
  )
  .build()

paymentSheet.presentWithIntentConfiguration(
    intentConfiguration = // ... ,
    configuration = configuration,
)
```

## Optional: Allow delayed payment methods [Client-side]

_Delayed payment methods_ (A payment method that can't immediately return payment status when a customer attempts a transaction (for example, ACH debits). Businesses commonly hold an order in a pending state until payment is successful with these payment methods) don’t guarantee that you’ll receive funds from your customer at the end of checkout, either because they take time to settle (for example, US Bank Accounts, SEPA Debit, iDEAL, Bancontact, and Sofort) or because they require customer action to complete (for example, OXXO, Konbini, and Boleto).

By default, `PaymentSheet` doesn’t display delayed payment methods. To include the delayed payment methods that `PaymentSheet` supports, set `allowsDelayedPaymentMethods` to true in your `PaymentSheet.Configuration`.

```kotlin
val configuration = PaymentSheet.Configuration.Builder(merchantDisplayName = "Powdur")
  .allowsDelayedPaymentMethods(true)
  .build()
```

If the customer successfully uses a delayed payment method in a `PaymentSheet`, the payment result returned is `PaymentSheetResult.Completed`.

## Optional: Enable Google Pay

> If your checkout screen has a dedicated **Google Pay** button, follow the [Google Pay guide](https://docs.stripe.com/google-pay.md?platform=android). You can use Embedded Payment Element to handle other payment method types.

### Set up your integration

To use Google Pay, first enable the Google Pay API by adding the following to the `<application>` tag of your **AndroidManifest.xml**:

```xml
<application>
  ...
  <meta-data
    android:name="com.google.android.gms.wallet.api.enabled"
    android:value="true" />
</application>
```

For more details, see Google Pay’s [Set up Google Pay API](https://developers.google.com/pay/api/android/guides/setup) for Android.

### Add Google Pay

To add Google Pay to your integration, pass a [PaymentSheet.GooglePayConfiguration](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/-google-pay-configuration/index.html) with your Google Pay environment (production or test) and the [country code of your business](https://dashboard.stripe.com/settings/account) when initializing [PaymentSheet.Configuration](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/-configuration/index.html).

#### Kotlin

```kotlin
val googlePayConfiguration = PaymentSheet.GooglePayConfiguration(
  environment = PaymentSheet.GooglePayConfiguration.Environment.Test,
  countryCode = "US",
  currencyCode = "USD" // Required for Setup Intents, optional for Payment Intents
)
val configuration = PaymentSheet.Configuration.Builder(merchantDisplayName = "My merchant name")
  .googlePay(googlePayConfiguration)
  .build()
```

### Test Google Pay

Google allows you to make test payments through their [Test card suite](https://developers.google.com/pay/api/android/guides/resources/test-card-suite). The test suite supports using Stripe [test cards](https://docs.stripe.com/testing.md).

You must test Google Pay using a physical Android device instead of a simulated device, in a country where Google Pay is supported. Log in to a Google account on your test device with a real card saved to Google Wallet.

## Optional: Enable card scanning

To enable card scanning support, [request production access](https://developers.google.com/pay/api/android/guides/test-and-deploy/request-prod-access) to the Google Pay API from the [Google Pay and Wallet Console](https://pay.google.com/business/console?utm_source=devsite&utm_medium=devsite&utm_campaign=devsite).

- If you’ve enabled Google Pay, the card scanning feature is automatically available in our UI on eligible devices. To learn more about eligible devices, see the [Google Pay API constraints](https://developers.google.com/pay/payment-card-recognition/debit-credit-card-recognition)
- **Important:** The card scanning feature only appears in builds signed with the same signing key registered in the [Google Pay & Wallet Console](https://pay.google.com/business/console). Test or debug builds using different signing keys (for example, builds distributed through Firebase App Tester) won’t show the **Scan card** option. To test card scanning in pre-release builds, you must either:
  - Sign your test builds with your production signing key
  - Add your test signing key fingerprint to the Google Pay and Wallet Console

## Optional: Customize the sheet

All customization is configured using the [PaymentSheet.Configuration](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/-configuration/index.html) object.

### Appearance

Customize colors, fonts, and more to match the look and feel of your app by using the [appearance API](https://docs.stripe.com/elements/appearance-api/mobile.md?platform=android).

### Payment method layout

Configure the layout of payment methods in the sheet using [paymentMethodLayout](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/-configuration/-builder/index.html#2123253356%2FFunctions%2F2002900378). You can display them horizontally, vertically, or let Stripe optimize the layout automatically.
![](assets/android-mpe-payment-method-layouts.3bcfe828ceaad1a94e0572a22d91733f.png)

#### Kotlin

```kotlin
PaymentSheet.Configuration.Builder("Example, Inc.")
  .paymentMethodLayout(PaymentSheet.PaymentMethodLayout.Automatic)
  .build()
```

### Collect users addresses

Collect local and international shipping or billing addresses from your customers using the [Address Element](https://docs.stripe.com/elements/address-element.md?platform=android).

### Business display name

Specify a customer-facing business name by setting [merchantDisplayName](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/-configuration/index.html#-191101533%2FProperties%2F2002900378). By default, this is your app’s name.

#### Kotlin

```kotlin
PaymentSheet.Configuration.Builder(
  merchantDisplayName = "My app, Inc."
).build()
```

### Dark mode

By default, `PaymentSheet` automatically adapts to the user’s system-wide appearance settings (light and dark mode). You can change this by setting light or dark mode on your app:

#### Kotlin

```kotlin
// force dark
AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_YES)
// force light
AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_NO)
```

### Default billing details

To set default values for billing details collected in the payment sheet, configure the `defaultBillingDetails` property. The `PaymentSheet` pre-populates its fields with the values that you provide.

#### Kotlin

```kotlin
val address = PaymentSheet.Address(country = "US")
val billingDetails = PaymentSheet.BillingDetails(
  address = address,
  email = "foo@bar.com"
)
val configuration = PaymentSheet.Configuration.Builder(merchantDisplayName = "Merchant, Inc.")
  .defaultBillingDetails(billingDetails)
  .build()
```

### Configure collection of billing details

Use `BillingDetailsCollectionConfiguration` to specify how you want to collect billing details in the PaymentSheet.

You can collect your customer’s name, email, phone number, and address.

If you want to attach default billing details to the PaymentMethod object even when those fields aren’t collected in the UI, set `billingDetailsCollectionConfiguration.attachDefaultsToPaymentMethod` to `true`.

#### Kotlin

```kotlin
val billingDetails = PaymentSheet.BillingDetails(
  email = "foo@bar.com"
)
val billingDetailsCollectionConfiguration = BillingDetailsCollectionConfiguration(
  attachDefaultsToPaymentMethod = true,
  name = BillingDetailsCollectionConfiguration.CollectionMode.Always,
  email = BillingDetailsCollectionConfiguration.CollectionMode.Never,
  address = BillingDetailsCollectionConfiguration.AddressCollectionMode.Full,
)
val configuration = PaymentSheet.Configuration.Builder(merchantDisplayName = "Merchant, Inc.")
  .defaultBillingDetails(billingDetails)
  .billingDetailsCollectionConfiguration(billingDetailsCollectionConfiguration)
  .build()
```

> Consult with your legal counsel regarding laws that apply to collecting information. Only collect phone numbers if you need them for the transaction.

# Accept a payment

> This is a Accept a payment for when platform is react-native and type is payment. View the full page at https://docs.stripe.com/payments/mobile/finalize-payments-on-the-server?platform=react-native&type=payment.

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

## Enable payment methods

View your [payment methods settings](https://dashboard.stripe.com/settings/payment_methods) and enable the payment methods you want to support. You need at least one payment method enabled to create a _PaymentIntent_ (The Payment Intents API tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by regulatory mandates, custom Radar fraud rules, or redirect-based payment methods).

By default, Stripe enables cards and other prevalent payment methods that can help you reach more customers, but we recommend turning on additional payment methods that are relevant for your business and customers. See [Payment method support](https://docs.stripe.com/payments/payment-methods/payment-method-support.md) for product and payment method support, and our [pricing page](https://stripe.com/pricing/local-payment-methods) for fees.

## Set up a return URL [Client-side]

When a customer exits your app (for example to authenticate in Safari or their banking app), provide a way for them to automatically return to your app. Many payment method types _require_ a return URL. If you don’t provide one, we can’t present payment methods that require a return URL to your users, even if you’ve enabled them.

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

Additionally, set the `returnURL` when you call the `initPaymentSheet` method:

```js
await initPaymentSheet({
  ...
  returnURL: 'your-app://stripe-redirect',
  ...
});
```

For more information on native URL schemes, refer to the [Android](https://developer.android.com/training/app-links/deep-linking) and [iOS](https://developer.apple.com/documentation/xcode/allowing_apps_and_websites_to_link_to_your_content/defining_a_custom_url_scheme_for_your_app) docs.

## Collect payment details [Client-side]

The integration can use the default payment flow or a custom flow.

| Default                                                                                                                                  | Custom flow                                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![PaymentSheet](assets/ios-overview.9e0d68d009dc005f73a6f5df69e00458.png)                       | ![Custom flow](assets/ios-multi-step.cd631ea4f1cd8cf3f39b6b9e1e92b6c5.png)                                                        |
| Displays a sheet to collect payment details and complete the payment. The button in the sheet says **Pay $X** and completes the payment. | Displays a sheet to collect payment details only. The button in the sheet says **Continue** and returns the customer to your app, where your own button completes payment. |

#### Default

### Initialize PaymentSheet

When you’re ready to take a payment, for example, when a customer checks out, initialize the PaymentSheet with an `intentConfiguration`. The `intentConfiguration` object contains details about the specific payment, such as the amount and currency, and a `confirmHandler` callback.

```jsx
import {View, Button} from 'react-native';
import {
  useStripe,
  useEffect,
  IntentCreationCallbackParams
} from '@stripe/stripe-react-native';

export default function CheckoutScreen() {const { initPaymentSheet, presentPaymentSheet } = useStripe();

  const initializePaymentSheet = async () => {
    const { error } = await initPaymentSheet({
      merchantDisplayName: "Example, Inc.",
      intentConfiguration: {mode: {
          amount: 1099,
          currencyCode: 'USD',},confirmHandler: confirmHandler
      }
    });
    if (error) {
      // handle error
    }
  };

  useEffect(() => {
    initializePaymentSheet();
  }, []);

  const confirmHandler = async (
    confirmationToken,
    intentCreationCallback: (params: IntentCreationCallbackParams) => void
  ) => {
    // explained later
  }

  const didTapCheckoutButton = async () => {
    // implement later
  }
  return (
    <View>
      <Button
        title="Checkout"
        onPress={didTapCheckoutButton}
      />
    </View>
  );
}
```

### Present PaymentSheet

Next, present the PaymentSheet. The `presentPaymentSheet` method resolves with a promise when the customer finishes paying, and then the sheet is dismissed.

```jsx
import { PaymentSheetError } from "@stripe/stripe-react-native";
export default function CheckoutScreen() {
  // ...
  const didTapCheckoutButton = async () => {
    const { error } = await presentPaymentSheet();

    if (error) {
      if (error.code === PaymentSheetError.Canceled) {
        // Customer canceled - you should probably do nothing.
      } else {
        // PaymentSheet encountered an unrecoverable error. You can display the error to the user, log it, and so on
      }
    } else {
      //Paymentcompleted - show a confirmation screen.
    }
  };
  // ...
}
```

### Confirm the payment

When the customer taps **Pay** in the PaymentSheet, it calls the callback you passed to `initPaymentSheet` with a ConfirmationToken representing the customer’s payment details and preferences.

Implement this method to send a request to your server, passing `confirmationToken.id`. Your server creates and confirms a PaymentIntent and returns its client secret.

When the request returns, call the `intentCreationCallback` with your server response’s client secret or an error. The PaymentSheet completes any next actions required to complete the PaymentIntent using the client secret or displays the localized error message in its UI.

```jsx
export default function CheckoutScreen() {
  // ...
const confirmHandler = async (
    confirmationToken,
    intentCreationCallback: (params: IntentCreationCallbackParams) => void
  ) => {
    // Make a request to your own server to create aPaymentIntentand return its client secret
    const response = await fetch(`${API_URL}/create-intent`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        confirmation_token_id: confirmationToken.id,
      }),
    });
    // Call the `intentCreationCallback` with your server response's client secret or error
    const { client_secret, error } = await response.json();
    if (client_secret) {
      intentCreationCallback({clientSecret: client_secret});
    } else {
      intentCreationCallback({
        error: {
          localizedMessage: error.localizedMessage || 'An error occurred',
        },
      });
    }
  }
  // ...
}
```

#### Custom flow

This integration assumes that your checkout screen has two buttons: a **Payment Method** button that presents the PaymentSheet to collect payment details, and a **Buy** button that completes the payment.

### Initialize PaymentSheet

When your checkout screen loads, initialize the PaymentSheet with an `intentConfiguration`. The `intentConfiguration` object contains details about the specific payment, such as the amount and currency, and a `confirmHandler` callback.

First, call `initPaymentSheet` and pass `customFlow: true`. `initPaymentSheet` resolves with an initial payment option containing an image and label representing the customer’s payment method. Update your UI with these details.

```jsx
import { useStripe } from '@stripe/stripe-react-native';
import {View, Button} from 'react-native';

export default function CheckoutScreen() {const { initPaymentSheet, presentPaymentSheet } = useStripe();

  const initializePaymentSheet = async () => {
    const { error, paymentOption } = await initPaymentSheet({
      merchantDisplayName: "Example, Inc.",
      customFlow: true,
      intentConfiguration: {mode: {
          amount: 1099,
          currencyCode: 'USD',},confirmHandler: handleConfirmation
      }
    });
    if (error) {
      // handle error
    }
    // Update your UI with paymentOption
  };

  useEffect(() => {
    initializePaymentSheet();
  }, []);

  const confirmHandler = async (
    confirmationToken,
    intentCreationCallback: (params: IntentCreationCallbackParams) => void
  ) => {
    // You'll implement this in the "Confirm the payment" section below
  }
  const didTapCheckoutButton = async () => {
    // You'll implement this in the "Confirm the payment" section below
  }
  return (
    <View>
      <Button
        title="Checkout"
        onPress={didTapCheckoutButton}
      />
    </View>
  );
}
```

### Present PaymentSheet

When a customer taps **Payment Method**, call `presentPaymentSheet` to collect payment details. When this completes, update your UI again with the `paymentOption` property.

```javascript
const { error, paymentOption } = await presentPaymentSheet();
// Update your UI with paymentOption
```

### Confirm the payment

When the customer taps **Buy**, call `confirmPaymentSheetPayment`. It calls the `confirmHandler` callback you passed to `initPaymentSheet` with a ConfirmationToken representing the customer’s payment details and preferences.

Implement this method to send a request to your server, passing `confirmationToken.id`. Your server creates and confirms a PaymentIntent and returns its client secret.

When the request returns, call the `intentCreationCallback` with your server response’s client secret or an error. The PaymentSheet completes any next actions required to complete the PaymentIntent using the client secret or displays the localized error message in its UI.

```jsx
export default function CheckoutScreen() {
  // ...
  const didTapCheckoutButton = async () => {const { error } = await confirmPaymentSheetPayment();

    if (error) {
      // PaymentSheet encountered an unrecoverable error. You can display the error to the user, log it, and so on.
    } else {
      //Paymentcompleted - show a confirmation screen.
    }
  }
const confirmHandler = async (
    confirmationToken,
    intentCreationCallback: (params: IntentCreationCallbackParams) => void
  ) => {
    // Make a request to your own server to create aPaymentIntentand return its client secret.
    const response = await fetch(`${API_URL}/create-intent`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        confirmation_token_id: confirmationToken.id,
      }),
    });
    // Call the `intentCreationCallback` with the client secret or error.
    const { client_secret, error } = await response.json();
    if (client_secret) {
      intentCreationCallback({clientSecret: client_secret});
    } else {
      intentCreationCallback({
        error: {
          localizedMessage: error.localizedMessage || 'An error occurred',
        },
      });
    }
  }
  // ...
}

```

The server code is explained in the following step.

## Create and submit the payment to Stripe [Server-side]

On your server, create and confirm a _PaymentIntent_ (The Payment Intents API tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by regulatory mandates, custom Radar fraud rules, or redirect-based payment methods) with an amount and currency. You can manage payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods). Stripe handles the return of eligible payment methods based on factors such as the transaction’s amount, currency, and payment flow. To prevent malicious customers from choosing their own prices, always decide how much to charge on the server-side (a trusted environment) and not the client.

If the call succeeds, return the PaymentIntent _client secret_ (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)). If the call fails, [handle the error](https://docs.stripe.com/error-handling.md) and return an error message with a brief explanation for your customer.

> Verify that all IntentConfiguration properties match your PaymentIntent (for example, `setup_future_usage`, `amount`, and `currency`).

### Handling client side arguments:

- `confirmation_token_id` - You can retrieve the ConfirmationToken object using this ID to perform your own validation or business logic.

#### Accounts v2

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
const express = require("express");
const app = express();

app.set("trust proxy", true);
app.use(express.json());

app.post("/create-confirm-intent", async (req, res) => {
  try {
    var args = {
      amount: 1099,
      currency: "usd",
      automatic_payment_methods: { enabled: true },
      confirm: true,
      confirmation_token: req.body.confirmation_token_id, // the ConfirmationToken ID sent by your client
    };
    const intent = await stripe.paymentIntents.create(args);
    res.json({
      client_secret: intent.client_secret,
    });
  } catch (err) {
    res.status(err.statusCode).json({ error: err.message });
  }
});

app.listen(3000, () => {
  console.log("Running on port 3000");
});
```

#### Customers v1

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
const express = require("express");
const app = express();

app.set("trust proxy", true);
app.use(express.json());

app.post("/create-confirm-intent", async (req, res) => {
  try {
    var args = {
      amount: 1099,
      currency: "usd",
      automatic_payment_methods: { enabled: true },
      confirm: true,
      confirmation_token: req.body.confirmation_token_id, // the ConfirmationToken ID sent by your client
    };
    const intent = await stripe.paymentIntents.create(args);
    res.json({
      client_secret: intent.client_secret,
    });
  } catch (err) {
    res.status(err.statusCode).json({ error: err.message });
  }
});

app.listen(3000, () => {
  console.log("Running on port 3000");
});
```

## Handle post-payment events [Server-side]

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the [Dashboard webhook tool](https://dashboard.stripe.com/webhooks) or follow the [webhook guide](https://docs.stripe.com/webhooks/quickstart.md) to receive these events and run actions, such as sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events is what enables you to accept [different types of payment methods](https://stripe.com/payments/payment-methods-guide) with a single integration.

In addition to handling the `payment_intent.succeeded` event, we recommend handling these other events when collecting payments with the Payment Element:

| Event                                                                                                                           | Description                                                                                                                                                                                                                                                                         | Action                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md?lang=php#event_types-payment_intent.succeeded)           | Sent when a customer successfully completes a payment.                                                                                                                                                                                                                              | Send the customer an order confirmation and _fulfill_ (Fulfillment is the process of providing the goods or services purchased by a customer, typically after payment is collected) their order. |
| [payment_intent.processing](https://docs.stripe.com/api/events/types.md?lang=php#event_types-payment_intent.processing)         | Sent when a customer successfully initiates a payment, but the payment has yet to complete. This event is most commonly sent when the customer initiates a bank debit. It’s followed by either a `payment_intent.succeeded` or `payment_intent.payment_failed` event in the future. | Send the customer an order confirmation that indicates their payment is pending. For digital goods, you might want to fulfill the order before waiting for payment to complete.                  |
| [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md?lang=php#event_types-payment_intent.payment_failed) | Sent when a customer attempts a payment, but the payment fails.                                                                                                                                                                                                                     | If a payment transitions from `processing` to `payment_failed`, offer the customer another attempt to pay.                                                                                       |

## Test the integration

#### Cards

| Card number         | Scenario                                                                                                                                                                                                                                                                                      | How to test                                                                                           |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| 4242424242424242    | The card payment succeeds and doesn’t require authentication.                                                                                                                                                                                                                                 | Fill out the credit card form using the credit card number with any expiration, CVC, and postal code. |
| 4000002500003155    | The card payment requires _authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase). | Fill out the credit card form using the credit card number with any expiration, CVC, and postal code. |
| 4000000000009995    | The card is declined with a decline code like `insufficient_funds`.                                                                                                                                                                                                                           | Fill out the credit card form using the credit card number with any expiration, CVC, and postal code. |
| 6205500000000000004 | The UnionPay card has a variable length of 13-19 digits.                                                                                                                                                                                                                                      | Fill out the credit card form using the credit card number with any expiration, CVC, and postal code. |

#### Bank redirects

| Payment method    | Scenario                                                                                                                                                                                        | How to test                                                                                                                                              |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Bancontact, iDEAL | Your customer fails to authenticate on the redirect page for a redirect-based and immediate notification payment method.                                                                        | Choose any redirect-based payment method, fill out the required details, and confirm the payment. Then click **Fail test payment** on the redirect page. |
| Pay by Bank       | Your customer successfully pays with a redirect-based and [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method.                      | Choose the payment method, fill out the required details, and confirm the payment. Then click **Complete test payment** on the redirect page.            |
| Pay by Bank       | Your customer fails to authenticate on the redirect page for a redirect-based and delayed notification payment method.                                                                          | Choose the payment method, fill out the required details, and confirm the payment. Then click **Fail test payment** on the redirect page.                |
| BLIK              | BLIK payments fail in a variety of ways—immediate failures (for example, the code is expired or invalid), delayed errors (the bank declines) or timeouts (the customer didn’t respond in time). | Use email patterns to [simulate the different failures.](https://docs.stripe.com/payments/blik/accept-a-payment.md#simulate-failures)                    |

#### Bank debits

| Payment method    | Scenario                                                                                          | How to test                                                                                                                                                                                       |
| ----------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SEPA Direct Debit | Your customer successfully pays with SEPA Direct Debit.                                           | Fill out the form using the account number `AT321904300235473204`. The confirmed PaymentIntent initially transitions to processing, then transitions to the succeeded status three minutes later. |
| SEPA Direct Debit | Your customer’s payment intent status transitions from `processing` to `requires_payment_method`. | Fill out the form using the account number `AT861904300235473202`.                                                                                                                                |

See [Testing](https://docs.stripe.com/testing.md) for additional information to test your integration.

## Enable card scanning

> Enabling card scanning is required for Apple’s iOS app review process. Card scanning is not required for Android’s app review process, but we recommend enabling it.

### iOS

To enable card scanning support for iOS, set the `NSCameraUsageDescription` (**Privacy - Camera Usage Description**) in the `Info.plist` of your application, and provide a reason for accessing the camera (for example, “To scan cards”).

### (Optional) Android

To enable card scanning support, [request production access](https://developers.google.com/pay/api/android/guides/test-and-deploy/request-prod-access) to the Google Pay API from the [Google Pay and Wallet Console](https://pay.google.com/business/console?utm_source=devsite&utm_medium=devsite&utm_campaign=devsite).

- If you’ve enabled Google Pay, the card scanning feature is automatically available in our UI on eligible devices. To learn more about eligible devices, see the [Google Pay API constraints](https://developers.google.com/pay/payment-card-recognition/debit-credit-card-recognition)
- **Important:** The card scanning feature only appears in builds signed with the same signing key registered in the [Google Pay & Wallet Console](https://pay.google.com/business/console). Test or debug builds using different signing keys (for example, builds distributed through Firebase App Tester) won’t show the **Scan card** option. To test card scanning in pre-release builds, you must either:
  - Sign your test builds with your production signing key
  - Add your test signing key fingerprint to the Google Pay and Wallet Console

## Optional: Enable saved cards [Server-side] [Client-side]

`PaymentSheet` can allow the customer to save their card and can include the customer’s saved cards in available payment methods. The customer must have an associated customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/create.md#v2_create_accounts-configuration-customer) object or a [Customer](https://docs.stripe.com/api/customers/create.md) object on your server. To enable a checkbox that allows the customer to save their card, create a [CustomerSession](https://docs.stripe.com/api/customer_sessions.md), with `payment_method_save` set to `enabled`.

#### Accounts v2

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
const express = require("express");
const app = express();

app.set("trust proxy", true);
app.use(express.json());

app.post("/payment-sheet", async (req, res) => {
  // Use an existing Account ID if this is a returning customer.
  const customer_account = await stripe.v2.core.accounts.create();
  const customerSession = await stripe.customerSessions.create({
    customer_account: customer_account.id,
    mobile_payment_element: {
      enabled: true,
      features: {
        payment_method_save: "enabled",
        payment_method_redisplay: "enabled",
        payment_method_remove: "enabled",
      },
    },
  });

  res.json({
    customerSessionClientSecret: customerSession.client_secret,
    customer_account: customer_account.id,
  });
});
```

Next, configure PaymentSheet with the customer’s ID and the CustomerSession client secret.

```jsx
const { error } = await initPaymentSheet({
  merchantDisplayName: "Example, Inc.",
  customerId: customer_account,
  customerSessionClientSecret: customerSessionClientSecret,
  ...
});
```

#### Customers v1

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
const express = require("express");
const app = express();

app.set("trust proxy", true);
app.use(express.json());

app.post("/payment-sheet", async (req, res) => {
  // Use an existing Customer ID if this is a returning customer.
  const customer = await stripe.customers.create();
  const customerSession = await stripe.customerSessions.create({
    customer: customer.id,
    mobile_payment_element: {
      enabled: true,
      features: {
        payment_method_save: "enabled",
        payment_method_redisplay: "enabled",
        payment_method_remove: "enabled",
      },
    },
  });

  res.json({
    customerSessionClientSecret: customerSession.client_secret,
    customer: customer.id,
  });
});
```

Next, configure PaymentSheet with the Customer’s ID and the CustomerSession client secret.

```jsx
const { error } = await initPaymentSheet({
  merchantDisplayName: "Example, Inc.",
  customerId: customer,
  customerSessionClientSecret: customerSessionClientSecret,
  ...
});
```

## Optional: Allow delayed payment methods [Client-side]

_Delayed payment methods_ (A payment method that can't immediately return payment status when a customer attempts a transaction (for example, ACH debits). Businesses commonly hold an order in a pending state until payment is successful with these payment methods) don’t guarantee that you’ll receive funds from your customer at the end of checkout. That’s because they take time to settle (for example, US Bank Accounts, SEPA Debit, iDEAL, Bancontact, and Sofort) or because they require customer action to complete (for example, OXXO, Konbini, and Boleto).

By default, PaymentSheet doesn’t display delayed payment methods. To display them, when you call `initPaymentSheet`, set `allowsDelayedPaymentMethods` to true.

> This setting only enables the display of delayed payment methods—it doesn’t activate them. For example, OXXO isn’t supported by PaymentSheet, so `allowsDelayedPaymentMethods` doesn’t allow PaymentSheet to handle OXXO payment methods. It only allows PaymentSheet to display payment methods of the delayed payment types that PaymentSheet supports. If PaymentSheet adds support for OXXO payment methods in the future, it would display them too.

```jsx
const { error } = await initPaymentSheet({
  merchantDisplayName: "Example, Inc.",
  allowsDelayedPaymentMethods: true,
  ...
});
```

If the customer successfully uses one of these delayed payment methods in PaymentSheet, the payment result returned is `.completed`.

## Optional: Enable Apple Pay

### Register for an Apple Merchant ID

Obtain an Apple Merchant ID by [registering for a new identifier](https://developer.apple.com/account/resources/identifiers/add/merchant) on the Apple Developer website.

Fill out the form with a description and identifier. Your description is for your own records and you can modify it in the future. Stripe recommends using the name of your app as the identifier (for example, `merchant.com.{{YOUR_APP_NAME}}`).

### Create a new Apple Pay certificate

Create a certificate for your app to encrypt payment data.

Go to the [iOS Certificate Settings](https://dashboard.stripe.com/settings/ios_certificates) in the Dashboard, click **Add new application**, and follow the guide.

Download a Certificate Signing Request (CSR) file to get a secure certificate from Apple that allows you to use Apple Pay.

One CSR file must be used to issue exactly one certificate. If you switch your Apple Merchant ID, you must go to the [iOS Certificate Settings](https://dashboard.stripe.com/settings/ios_certificates) in the Dashboard to obtain a new CSR and certificate.

### Integrate with Xcode

Add the Apple Pay capability to your app. In Xcode, open your project settings, click the **Signing & Capabilities** tab, and add the **Apple Pay** capability. You might be prompted to log in to your developer account at this point. Select the merchant ID you created earlier, and your app is ready to accept Apple Pay.
![](assets/xcode.a701d4c1922d19985e9c614a6f105bf1.png)

Enable the Apple Pay capability in Xcode

### Add Apple Pay

#### One-time payment

Pass your merchant ID when you create `StripeProvider`:

```javascript
import { StripeProvider } from "@stripe/stripe-react-native";

function App() {
  return (
    <StripeProvider
      publishableKey="<<YOUR_PUBLISHABLE_KEY>>"
      merchantIdentifier="MERCHANT_ID"
    >
      {/* Your app code here */}
    </StripeProvider>
  );
}
```

When you call `initPaymentSheet`, pass in your [ApplePayParams](https://stripe.dev/stripe-react-native/api-reference/modules/PaymentSheet.html#ApplePayParams):

```javascript
await initPaymentSheet({
  // ...
  applePay: {
    merchantCountryCode: "US",
  },
});
```

#### Recurring payments

When you call `initPaymentSheet`, pass in an [ApplePayParams](https://stripe.dev/stripe-react-native/api-reference/modules/PaymentSheet.html#ApplePayParams) with `merchantCountryCode` set to the country code of your business.

In accordance with [Apple’s guidelines](https://developer.apple.com/design/human-interface-guidelines/apple-pay#Supporting-subscriptions) for recurring payments, you must also set a `cardItems` that includes a [RecurringCartSummaryItem](https://stripe.dev/stripe-react-native/api-reference/modules/ApplePay.html#RecurringCartSummaryItem) with the amount you intend to charge (for example, “59.95 USD a month”).

You can also adopt [merchant tokens](https://developer.apple.com/apple-pay/merchant-tokens/) by setting the `request` with its `type` set to `PaymentRequestType.Recurring`

To learn more about how to use recurring payments with Apple Pay, see [Apple’s PassKit documentation](https://developer.apple.com/documentation/passkit/pkpaymentrequest).

#### iOS (React Native)

```javascript
const initializePaymentSheet = async () => {
  const recurringSummaryItem = {
    label: "My Subscription",
    amount: "59.99",
    paymentType: "Recurring",
    intervalCount: 1,
    intervalUnit: "month",
    // Payment starts today
    startDate: new Date().getTime() / 1000,

    // Payment ends in one year
    endDate: new Date().getTime() / 1000 + 60 * 60 * 24 * 365,
  };

  const { error } = await initPaymentSheet({
    // ...
    applePay: {
      merchantCountryCode: "US",
      cartItems: [recurringSummaryItem],
      request: {
        type: PaymentRequestType.Recurring,
        description: "Recurring",
        managementUrl: "https://my-backend.example.com/customer-portal",
        billing: recurringSummaryItem,
        billingAgreement:
          "You'll be billed $59.99 every month for the next 12 months. To cancel at any time, go to Account and click 'Cancel Membership.'",
      },
    },
  });
};
```

### Order tracking

To add [order tracking](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/designing-order-tracking) information in iOS 16 or later, configure a `setOrderTracking` callback function. Stripe calls your implementation after the payment is complete, but before iOS dismisses the Apple Pay sheet.

In your implementation of `setOrderTracking` callback function, fetch the order details from your server for the completed order, and pass the details to the provided `completion` function.

To learn more about order tracking, see [Apple’s Wallet Orders documentation](https://developer.apple.com/documentation/walletorders).

#### iOS (React Native)

```javascript
await initPaymentSheet({
  // ...
  applePay: {
    // ...
    setOrderTracking: async (complete) => {
      const apiEndpoint =
        Platform.OS === "ios" ?
          "http://localhost:4242"
        : "http://10.0.2.2:4567";
      const response = await fetch(
        `${apiEndpoint}/retrieve-order?orderId=${orderId}`,
        {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        },
      );
      if (response.status === 200) {
        const orderDetails = await response.json();
        // orderDetails should include orderIdentifier, orderTypeIdentifier,
        // authenticationToken and webServiceUrl
        complete(orderDetails);
      }
    },
  },
});
```

## Optional: Enable Google Pay

### Set up your integration

To use Google Pay, first enable the Google Pay API by adding the following to the `<application>` tag of your **AndroidManifest.xml**:

```xml
<application>
  ...
  <meta-data
    android:name="com.google.android.gms.wallet.api.enabled"
    android:value="true" />
</application>
```

For more details, see Google Pay’s [Set up Google Pay API](https://developers.google.com/pay/api/android/guides/setup) for Android.

### Add Google Pay

When you initialize `PaymentSheet`, set `merchantCountryCode` to the country code of your business and set `googlePay` to true.

You can also use the test environment by passing the `testEnv` parameter. You can only test Google Pay on a physical Android device. Follow the [React Native docs](https://reactnative.dev/docs/running-on-device) to test your application on a physical device.

```javascript
const { error, paymentOption } = await initPaymentSheet({
  // ...
  googlePay: {
    merchantCountryCode: "US",
    testEnv: true, // use test environment
  },
});
```

## Optional: Customize the sheet

All customization is configured using `initPaymentSheet`.

### Appearance

Customize colors, fonts, and so on to match the look and feel of your app by using the [appearance API](https://docs.stripe.com/elements/appearance-api/mobile.md?platform=react-native).

### Merchant display name

Specify a customer-facing business name by setting `merchantDisplayName`. By default, this is your app’s name.

```javascript
await initPaymentSheet({
  // ...
  merchantDisplayName: "Example Inc.",
});
```

### Dark mode

By default, `PaymentSheet` automatically adapts to the user’s system-wide appearance settings (light and dark mode). You can change this by setting the `style` property to `alwaysLight` or `alwaysDark` mode on iOS.

```javascript
await initPaymentSheet({
  // ...
  style: "alwaysDark",
});
```

On Android, set light or dark mode on your app:

```
// force dark
AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_YES)
// force light
AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_NO)
```

### Default billing details

To set default values for billing details collected in the PaymentSheet, configure the `defaultBillingDetails` property. The `PaymentSheet` pre-populates its fields with the values that you provide.

```javascript
await initPaymentSheet({
  // ...
  defaultBillingDetails: {
    email: "foo@bar.com",
    address: {
      country: "US",
    },
  },
});
```

### Collect billing details

Use `billingDetailsCollectionConfiguration` to specify how you want to collect billing details in the PaymentSheet.

You can collect your customer’s name, email, phone number, and address.

If you don’t intend to collect the values that the payment method requires, you must do the following:

1. Attach the values that aren’t collected by `PaymentSheet` to the `defaultBillingDetails` property.
1. Set `billingDetailsCollectionConfiguration.attachDefaultsToPaymentMethod` to `true`.

```javascript
await initPaymentSheet({
  // ...
  defaultBillingDetails: {
    email: "foo@bar.com",
  },
  billingDetailsCollectionConfiguration: {
    name: PaymentSheet.CollectionMode.ALWAYS,
    email: PaymentSheet.CollectionMode.NEVER,
    address: PaymentSheet.AddressCollectionMode.FULL,
    attachDefaultsToPaymentMethod: true,
  },
});
```

> Consult with your legal counsel regarding laws that apply to collecting information. Only collect phone numbers if you need them for the transaction.

# Collect and save a payment method

> This is a Collect and save a payment method for when platform is react-native and type is setup. View the full page at https://docs.stripe.com/payments/mobile/finalize-payments-on-the-server?platform=react-native&type=setup.

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

## Enable payment methods

> When used with a SetupIntent, PaymentSheet supports cards and PayPal.

View your [payment methods settings](https://dashboard.stripe.com/settings/payment_methods) and enable the payment methods you want to support. You need at least one payment method enabled to create a _SetupIntent_ (The Setup Intents API lets you build dynamic flows for collecting payment method details for future payments. It tracks the lifecycle of a payment setup flow and can trigger additional authentication steps if required by law or by the payment method).

By default, Stripe enables cards and other prevalent payment methods that can help you reach more customers, but we recommend turning on additional payment methods that are relevant for your business and customers. See [Payment method support](https://docs.stripe.com/payments/payment-methods/payment-method-support.md) for product and payment method support, and our [pricing page](https://stripe.com/pricing/local-payment-methods) for fees.

## Set up a return URL [Client-side]

When a customer exits your app (for example to authenticate in Safari or their banking app), provide a way for them to automatically return to your app. Many payment method types _require_ a return URL. If you don’t provide one, we can’t present payment methods that require a return URL to your users, even if you’ve enabled them.

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

Additionally, set the `returnURL` when you call the `initPaymentSheet` method:

```js
await initPaymentSheet({
  ...
  returnURL: 'your-app://stripe-redirect',
  ...
});
```

For more information on native URL schemes, refer to the [Android](https://developer.android.com/training/app-links/deep-linking) and [iOS](https://developer.apple.com/documentation/xcode/allowing_apps_and_websites_to_link_to_your_content/defining_a_custom_url_scheme_for_your_app) docs.

## Create a Customer [Server-side]

To set up a payment method for future payments, you must attach it to an object that represents your customer. When your customer creates an account or has their first transaction with your business, create either a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/create.md) object with the Accounts v2 API or a [Customer](https://docs.stripe.com/api/customers/create.md) object with the Customers API.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/connect/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create();
```

## Collect payment details [Client-side]

The integration can use the default payment flow or a custom flow.

| Default                                                                                                                                     | Custom flow                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![PaymentSheet](assets/ios-overview.9e0d68d009dc005f73a6f5df69e00458.png)                          | ![Custom flow](assets/ios-multi-step.cd631ea4f1cd8cf3f39b6b9e1e92b6c5.png)                                                          |
| Displays a sheet to collect payment details and complete the setup. The button in the sheet says **Set up** and sets up the payment method. | Displays a sheet to collect payment details only. The button in the sheet says **Continue** and returns the customer to your app, where your own button completes the setup. |

#### Default

### Initialize PaymentSheet

When you’re ready to set up a payment method, initialize the PaymentSheet with an `intentConfiguration`. The `intentConfiguration` object contains details about the specific payment method, such as the currency, and a `confirmHandler` callback.

```jsx
import {View, Button} from 'react-native';
import {
  useStripe,
  useEffect,
  IntentCreationCallbackParams
} from '@stripe/stripe-react-native';

export default function CheckoutScreen() {const { initPaymentSheet, presentPaymentSheet } = useStripe();

  const initializePaymentSheet = async () => {
    const { error } = await initPaymentSheet({
      merchantDisplayName: "Example, Inc.",
      intentConfiguration: {mode: {
          currencyCode: 'USD',
        },confirmHandler: confirmHandler
      }
    });
    if (error) {
      // handle error
    }
  };

  useEffect(() => {
    initializePaymentSheet();
  }, []);

  const confirmHandler = async (
    confirmationToken,
    intentCreationCallback: (params: IntentCreationCallbackParams) => void
  ) => {
    // explained later
  }

  const didTapCheckoutButton = async () => {
    // implement later
  }
  return (
    <View>
      <Button
        title="Checkout"
        onPress={didTapCheckoutButton}
      />
    </View>
  );
}
```

### Present PaymentSheet

Next, present the PaymentSheet. The `presentPaymentSheet` method resolves with a promise when the customer finishes setting up their payment method, and then the sheet is dismissed.

```jsx
import { PaymentSheetError } from "@stripe/stripe-react-native";
export default function CheckoutScreen() {
  // ...
  const didTapCheckoutButton = async () => {
    const { error } = await presentPaymentSheet();

    if (error) {
      if (error.code === PaymentSheetError.Canceled) {
        // Customer canceled - you should probably do nothing.
      } else {
        // PaymentSheet encountered an unrecoverable error. You can display the error to the user, log it, and so on
      }
    } else {
      //Setupcompleted - show a confirmation screen.
    }
  };
  // ...
}
```

### Confirm the payment details

When the customer taps **Set up** in the PaymentSheet, it calls the callback you passed to `initPaymentSheet` with a ConfirmationToken representing the customer’s payment details and preferences.

Implement this method to send a request to your server, passing `confirmationToken.id`. Your server creates and confirms a SetupIntent and returns its client secret.

When the request returns, call the `intentCreationCallback` with your server response’s client secret or an error. The PaymentSheet completes any next actions required to complete the SetupIntent using the client secret or displays the localized error message in its UI.

```jsx
export default function CheckoutScreen() {
  // ...
const confirmHandler = async (
    confirmationToken,
    intentCreationCallback: (params: IntentCreationCallbackParams) => void
  ) => {
    // Make a request to your own server to create aSetupIntentand return its client secret
    const response = await fetch(`${API_URL}/create-intent`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        confirmation_token_id: confirmationToken.id,
      }),
    });
    // Call the `intentCreationCallback` with your server response's client secret or error
    const { client_secret, error } = await response.json();
    if (client_secret) {
      intentCreationCallback({clientSecret: client_secret});
    } else {
      intentCreationCallback({
        error: {
          localizedMessage: error.localizedMessage || 'An error occurred',
        },
      });
    }
  }
  // ...
}
```

#### Custom flow

This integration assumes that your checkout screen has two buttons: a **Payment Method** button that presents the PaymentSheet to collect payment details, and a **Save** button that saves the payment method.

### Initialize PaymentSheet

When your checkout screen loads, initialize the PaymentSheet with an `intentConfiguration`. The `intentConfiguration` object contains details about the specific payment method, such as the currency, and a `confirmHandler` callback.

First, call `initPaymentSheet` and pass `customFlow: true`. `initPaymentSheet` resolves with an initial payment option containing an image and label representing the customer’s payment method. Update your UI with these details.

```jsx
import { useStripe } from '@stripe/stripe-react-native';
import {View, Button} from 'react-native';

export default function CheckoutScreen() {const { initPaymentSheet, presentPaymentSheet } = useStripe();

  const initializePaymentSheet = async () => {
    const { error, paymentOption } = await initPaymentSheet({
      merchantDisplayName: "Example, Inc.",
      customFlow: true,
      intentConfiguration: {mode: {
          currencyCode: 'USD',
        },confirmHandler: handleConfirmation
      }
    });
    if (error) {
      // handle error
    }
    // Update your UI with paymentOption
  };

  useEffect(() => {
    initializePaymentSheet();
  }, []);

  const confirmHandler = async (
    confirmationToken,
    intentCreationCallback: (params: IntentCreationCallbackParams) => void
  ) => {
    // You'll implement this in the "Confirm the payment" section below
  }
  const didTapCheckoutButton = async () => {
    // You'll implement this in the "Confirm the payment" section below
  }
  return (
    <View>
      <Button
        title="Checkout"
        onPress={didTapCheckoutButton}
      />
    </View>
  );
}
```

### Present PaymentSheet

When a customer taps **Payment Method**, call `presentPaymentSheet` to collect payment details. When this completes, update your UI again with the `paymentOption` property.

```javascript
const { error, paymentOption } = await presentPaymentSheet();
// Update your UI with paymentOption
```

### Confirm the payment details

When the customer taps **Save**, call `confirmPaymentSheetPayment`. It calls the `confirmHandler` callback you passed to `initPaymentSheet` with a ConfirmationToken representing the customer’s payment details and preferences.

Implement this method to send a request to your server, passing `confirmationToken.id`. Your server creates and confirms a SetupIntent and returns its client secret.

When the request returns, call the `intentCreationCallback` with your server response’s client secret or an error. The PaymentSheet completes any next actions required to complete the SetupIntent using the client secret or displays the localized error message in its UI.

```jsx
export default function CheckoutScreen() {
  // ...
  const didTapCheckoutButton = async () => {const { error } = await confirmPaymentSheetPayment();

    if (error) {
      // PaymentSheet encountered an unrecoverable error. You can display the error to the user, log it, and so on.
    } else {
      //Setupcompleted - show a confirmation screen.
    }
  }
const confirmHandler = async (
    confirmationToken,
    intentCreationCallback: (params: IntentCreationCallbackParams) => void
  ) => {
    // Make a request to your own server to create aSetupIntentand return its client secret.
    const response = await fetch(`${API_URL}/create-intent`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        confirmation_token_id: confirmationToken.id,
      }),
    });
    // Call the `intentCreationCallback` with the client secret or error.
    const { client_secret, error } = await response.json();
    if (client_secret) {
      intentCreationCallback({clientSecret: client_secret});
    } else {
      intentCreationCallback({
        error: {
          localizedMessage: error.localizedMessage || 'An error occurred',
        },
      });
    }
  }
  // ...
}

```

The server code is explained in the following step.

## Submit the payment details to Stripe [Server-side]

On your server, create and confirm a _SetupIntent_ (The Setup Intents API lets you build dynamic flows for collecting payment method details for future payments. It tracks the lifecycle of a payment setup flow and can trigger additional authentication steps if required by law or by the payment method). You can manage payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods). Stripe evaluates payment method restrictions and other parameters to determine the list of supported payment methods.

If the call succeeds, return the SetupIntent _client secret_ (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)). If the call fails, [handle the error](https://docs.stripe.com/error-handling.md) and return an error message with a brief explanation for your customer.

> Verify that all IntentConfiguration properties match your SetupIntent (for example, [usage](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-usage)).

### Handling client side arguments:

- `confirmation_token_id` - You can retrieve the ConfirmationToken object using this ID to perform your own validation or business logic.

#### Accounts v2

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
const express = require('express');
const app = express();

app.set('trust proxy', true);
app.use(express.json());

app.post('/create-confirm-intent', async (req, res) => {
  try {
    var args = {
      customer_account: ... // The Account ID you previously created
      automatic_payment_methods: {enabled: true},
      confirm: true,
      confirmation_token: req.body.confirmation_token_id, // the ConfirmationToken ID sent by your client
    };
    const intent = await stripe.setupIntents.create(args);
    res.json({
      client_secret: intent.client_secret,
    });
  } catch (err) {
    res.status(err.statusCode).json({ error: err.message })
  }
});

app.listen(3000, () => {
  console.log('Running on port 3000');
});
```

#### Customers v1

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
const express = require('express');
const app = express();

app.set('trust proxy', true);
app.use(express.json());

app.post('/create-confirm-intent', async (req, res) => {
  try {
    var args = {
      customer: ... // The Customer ID you previously created
      automatic_payment_methods: {enabled: true},
      confirm: true,
      confirmation_token: req.body.confirmation_token_id, // the ConfirmationToken ID sent by your client
    };
    const intent = await stripe.setupIntents.create(args);
    res.json({
      client_secret: intent.client_secret,
    });
  } catch (err) {
    res.status(err.statusCode).json({ error: err.message })
  }
});

app.listen(3000, () => {
  console.log('Running on port 3000');
});
```

## Charge the saved payment method later [Server-side]

> When you save a `bancontact` or `ideal` payment method, it generates and saves a `sepa_debit` reusable payment method instead of the original method. To query for the saved method, you need to use `sepa_debit`, not `bancontact` or `ideal`.

> #### Compliance
>
> You’re responsible for your compliance with all applicable laws, regulations, and network rules when saving a customer’s payment details. When rendering past payment methods to your end customer for future purchases, make sure you’re listing payment methods where you’ve collected consent from the customer to save the payment method details for this specific future use. To differentiate between payment methods attached to customers that can and can’t be presented to your end customer as a saved payment method for future purchases, use the [allow_redisplay](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-allow_redisplay) parameter.

To find a payment method to charge, list the payment methods associated with your customer. This example lists cards but you can list any supported [type](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-type).

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/connect/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

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

When you’re ready to charge your customer _off-session_ (A payment is described as off-session if it occurs without the direct involvement of the customer, using previously-collected payment information), use the customer’s ID and the `PaymentMethod` ID to create a `PaymentIntent` with the amount and currency of the payment. Set a few other parameters to make the off-session payment:

- Set [off_session](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-off_session) to `true` to indicate that the customer isn’t in your checkout flow during a payment attempt and can’t fulfill an authentication request made by a partner, such as a card issuer, bank, or other payment institution. If, during your checkout flow, a partner requests authentication, Stripe requests exemptions using customer information from a previous _on-session_ (A payment is described as on-session if it occurs while the customer is actively in your checkout flow and able to authenticate the payment method) transaction. If the conditions for exemption aren’t met, the `PaymentIntent` might throw an error.
- Set the value of the `PaymentIntent`’s [confirm](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-confirm) property to true, which causes confirmation to occur immediately when the `PaymentIntent` is created.
- Set [payment_method](https://docs.stripe.com/api.md#create_payment_intent-payment_method) to the `PaymentMethod`’s ID.
- Depending on how you represent customers in your integration, set either [customer_account](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-customer_account) to the ID of the customer-configured `Account` or [customer](https://docs.stripe.com/api.md#create_payment_intent-customer) to the ID of the `Customer`.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "usd",
  automatic_payment_methods: {
    enabled: true,
  },
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  payment_method: "{{PAYMENT_METHOD_ID}}",
  return_url: "https://example.com/order/123/complete",
  off_session: true,
  confirm: true,
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "usd",
  automatic_payment_methods: {
    enabled: true,
  },
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{PAYMENT_METHOD_ID}}",
  return_url: "https://example.com/order/123/complete",
  off_session: true,
  confirm: true,
});
```

## Test the integration

#### Cards

| Card number         | Scenario                                                                                                                                                                                                                                                                                      | How to test                                                                                           |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| 4242424242424242    | The card payment succeeds and doesn’t require authentication.                                                                                                                                                                                                                                 | Fill out the credit card form using the credit card number with any expiration, CVC, and postal code. |
| 4000002500003155    | The card payment requires _authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase). | Fill out the credit card form using the credit card number with any expiration, CVC, and postal code. |
| 4000000000009995    | The card is declined with a decline code like `insufficient_funds`.                                                                                                                                                                                                                           | Fill out the credit card form using the credit card number with any expiration, CVC, and postal code. |
| 6205500000000000004 | The UnionPay card has a variable length of 13-19 digits.                                                                                                                                                                                                                                      | Fill out the credit card form using the credit card number with any expiration, CVC, and postal code. |

#### Bank redirects

| Payment method    | Scenario                                                                                                                                                                                        | How to test                                                                                                                                              |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Bancontact, iDEAL | Your customer fails to authenticate on the redirect page for a redirect-based and immediate notification payment method.                                                                        | Choose any redirect-based payment method, fill out the required details, and confirm the payment. Then click **Fail test payment** on the redirect page. |
| Pay by Bank       | Your customer successfully pays with a redirect-based and [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method.                      | Choose the payment method, fill out the required details, and confirm the payment. Then click **Complete test payment** on the redirect page.            |
| Pay by Bank       | Your customer fails to authenticate on the redirect page for a redirect-based and delayed notification payment method.                                                                          | Choose the payment method, fill out the required details, and confirm the payment. Then click **Fail test payment** on the redirect page.                |
| BLIK              | BLIK payments fail in a variety of ways—immediate failures (for example, the code is expired or invalid), delayed errors (the bank declines) or timeouts (the customer didn’t respond in time). | Use email patterns to [simulate the different failures.](https://docs.stripe.com/payments/blik/accept-a-payment.md#simulate-failures)                    |

#### Bank debits

| Payment method    | Scenario                                                                                          | How to test                                                                                                                                                                                       |
| ----------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SEPA Direct Debit | Your customer successfully pays with SEPA Direct Debit.                                           | Fill out the form using the account number `AT321904300235473204`. The confirmed PaymentIntent initially transitions to processing, then transitions to the succeeded status three minutes later. |
| SEPA Direct Debit | Your customer’s payment intent status transitions from `processing` to `requires_payment_method`. | Fill out the form using the account number `AT861904300235473202`.                                                                                                                                |

See [Testing](https://docs.stripe.com/testing.md) for additional information to test your integration.

## Enable card scanning

> Enabling card scanning is required for Apple’s iOS app review process. Card scanning is not required for Android’s app review process, but we recommend enabling it.

### iOS

To enable card scanning support for iOS, set the `NSCameraUsageDescription` (**Privacy - Camera Usage Description**) in the `Info.plist` of your application, and provide a reason for accessing the camera (for example, “To scan cards”).

### (Optional) Android

To enable card scanning support, [request production access](https://developers.google.com/pay/api/android/guides/test-and-deploy/request-prod-access) to the Google Pay API from the [Google Pay and Wallet Console](https://pay.google.com/business/console?utm_source=devsite&utm_medium=devsite&utm_campaign=devsite).

- If you’ve enabled Google Pay, the card scanning feature is automatically available in our UI on eligible devices. To learn more about eligible devices, see the [Google Pay API constraints](https://developers.google.com/pay/payment-card-recognition/debit-credit-card-recognition)
- **Important:** The card scanning feature only appears in builds signed with the same signing key registered in the [Google Pay & Wallet Console](https://pay.google.com/business/console). Test or debug builds using different signing keys (for example, builds distributed through Firebase App Tester) won’t show the **Scan card** option. To test card scanning in pre-release builds, you must either:
  - Sign your test builds with your production signing key
  - Add your test signing key fingerprint to the Google Pay and Wallet Console

## Optional: Enable saved cards [Server-side] [Client-side]

`PaymentSheet` can allow the customer to save their card and can include the customer’s saved cards in available payment methods. The customer must have an associated customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/create.md#v2_create_accounts-configuration-customer) object or a [Customer](https://docs.stripe.com/api/customers/create.md) object on your server. To enable a checkbox that allows the customer to save their card, create a [CustomerSession](https://docs.stripe.com/api/customer_sessions.md), with `payment_method_save` set to `enabled`.

#### Accounts v2

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
const express = require("express");
const app = express();

app.set("trust proxy", true);
app.use(express.json());

app.post("/payment-sheet", async (req, res) => {
  // Use an existing Account ID if this is a returning customer.
  const customer_account = await stripe.v2.core.accounts.create();
  const customerSession = await stripe.customerSessions.create({
    customer_account: customer_account.id,
    mobile_payment_element: {
      enabled: true,
      features: {
        payment_method_save: "enabled",
        payment_method_redisplay: "enabled",
        payment_method_remove: "enabled",
      },
    },
  });

  res.json({
    customerSessionClientSecret: customerSession.client_secret,
    customer_account: customer_account.id,
  });
});
```

Next, configure PaymentSheet with the customer’s ID and the CustomerSession client secret.

```jsx
const { error } = await initPaymentSheet({
  merchantDisplayName: "Example, Inc.",
  customerId: customer_account,
  customerSessionClientSecret: customerSessionClientSecret,
  ...
});
```

#### Customers v1

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
const express = require("express");
const app = express();

app.set("trust proxy", true);
app.use(express.json());

app.post("/payment-sheet", async (req, res) => {
  // Use an existing Customer ID if this is a returning customer.
  const customer = await stripe.customers.create();
  const customerSession = await stripe.customerSessions.create({
    customer: customer.id,
    mobile_payment_element: {
      enabled: true,
      features: {
        payment_method_save: "enabled",
        payment_method_redisplay: "enabled",
        payment_method_remove: "enabled",
      },
    },
  });

  res.json({
    customerSessionClientSecret: customerSession.client_secret,
    customer: customer.id,
  });
});
```

Next, configure PaymentSheet with the Customer’s ID and the CustomerSession client secret.

```jsx
const { error } = await initPaymentSheet({
  merchantDisplayName: "Example, Inc.",
  customerId: customer,
  customerSessionClientSecret: customerSessionClientSecret,
  ...
});
```

## Optional: Allow delayed payment methods [Client-side]

_Delayed payment methods_ (A payment method that can't immediately return payment status when a customer attempts a transaction (for example, ACH debits). Businesses commonly hold an order in a pending state until payment is successful with these payment methods) don’t guarantee that you’ll receive funds from your customer at the end of checkout. That’s because they take time to settle (for example, US Bank Accounts, SEPA Debit, iDEAL, Bancontact, and Sofort) or because they require customer action to complete (for example, OXXO, Konbini, and Boleto).

By default, PaymentSheet doesn’t display delayed payment methods. To display them, when you call `initPaymentSheet`, set `allowsDelayedPaymentMethods` to true.

> This setting only enables the display of delayed payment methods—it doesn’t activate them. For example, OXXO isn’t supported by PaymentSheet, so `allowsDelayedPaymentMethods` doesn’t allow PaymentSheet to handle OXXO payment methods. It only allows PaymentSheet to display payment methods of the delayed payment types that PaymentSheet supports. If PaymentSheet adds support for OXXO payment methods in the future, it would display them too.

```jsx
const { error } = await initPaymentSheet({
  merchantDisplayName: "Example, Inc.",
  allowsDelayedPaymentMethods: true,
  ...
});
```

If the customer successfully uses one of these delayed payment methods in PaymentSheet, the payment result returned is `.completed`.

## Optional: Enable Apple Pay

### Register for an Apple Merchant ID

Obtain an Apple Merchant ID by [registering for a new identifier](https://developer.apple.com/account/resources/identifiers/add/merchant) on the Apple Developer website.

Fill out the form with a description and identifier. Your description is for your own records and you can modify it in the future. Stripe recommends using the name of your app as the identifier (for example, `merchant.com.{{YOUR_APP_NAME}}`).

### Create a new Apple Pay certificate

Create a certificate for your app to encrypt payment data.

Go to the [iOS Certificate Settings](https://dashboard.stripe.com/settings/ios_certificates) in the Dashboard, click **Add new application**, and follow the guide.

Download a Certificate Signing Request (CSR) file to get a secure certificate from Apple that allows you to use Apple Pay.

One CSR file must be used to issue exactly one certificate. If you switch your Apple Merchant ID, you must go to the [iOS Certificate Settings](https://dashboard.stripe.com/settings/ios_certificates) in the Dashboard to obtain a new CSR and certificate.

### Integrate with Xcode

Add the Apple Pay capability to your app. In Xcode, open your project settings, click the **Signing & Capabilities** tab, and add the **Apple Pay** capability. You might be prompted to log in to your developer account at this point. Select the merchant ID you created earlier, and your app is ready to accept Apple Pay.
![](assets/xcode.a701d4c1922d19985e9c614a6f105bf1.png)

Enable the Apple Pay capability in Xcode

### Add Apple Pay

#### One-time payment

Pass your merchant ID when you create `StripeProvider`:

```javascript
import { StripeProvider } from "@stripe/stripe-react-native";

function App() {
  return (
    <StripeProvider
      publishableKey="<<YOUR_PUBLISHABLE_KEY>>"
      merchantIdentifier="MERCHANT_ID"
    >
      {/* Your app code here */}
    </StripeProvider>
  );
}
```

When you call `initPaymentSheet`, pass in your [ApplePayParams](https://stripe.dev/stripe-react-native/api-reference/modules/PaymentSheet.html#ApplePayParams):

```javascript
await initPaymentSheet({
  // ...
  applePay: {
    merchantCountryCode: "US",
  },
});
```

#### Recurring payments

When you call `initPaymentSheet`, pass in an [ApplePayParams](https://stripe.dev/stripe-react-native/api-reference/modules/PaymentSheet.html#ApplePayParams) with `merchantCountryCode` set to the country code of your business.

In accordance with [Apple’s guidelines](https://developer.apple.com/design/human-interface-guidelines/apple-pay#Supporting-subscriptions) for recurring payments, you must also set a `cardItems` that includes a [RecurringCartSummaryItem](https://stripe.dev/stripe-react-native/api-reference/modules/ApplePay.html#RecurringCartSummaryItem) with the amount you intend to charge (for example, “59.95 USD a month”).

You can also adopt [merchant tokens](https://developer.apple.com/apple-pay/merchant-tokens/) by setting the `request` with its `type` set to `PaymentRequestType.Recurring`

To learn more about how to use recurring payments with Apple Pay, see [Apple’s PassKit documentation](https://developer.apple.com/documentation/passkit/pkpaymentrequest).

#### iOS (React Native)

```javascript
const initializePaymentSheet = async () => {
  const recurringSummaryItem = {
    label: "My Subscription",
    amount: "59.99",
    paymentType: "Recurring",
    intervalCount: 1,
    intervalUnit: "month",
    // Payment starts today
    startDate: new Date().getTime() / 1000,

    // Payment ends in one year
    endDate: new Date().getTime() / 1000 + 60 * 60 * 24 * 365,
  };

  const { error } = await initPaymentSheet({
    // ...
    applePay: {
      merchantCountryCode: "US",
      cartItems: [recurringSummaryItem],
      request: {
        type: PaymentRequestType.Recurring,
        description: "Recurring",
        managementUrl: "https://my-backend.example.com/customer-portal",
        billing: recurringSummaryItem,
        billingAgreement:
          "You'll be billed $59.99 every month for the next 12 months. To cancel at any time, go to Account and click 'Cancel Membership.'",
      },
    },
  });
};
```

### Order tracking

To add [order tracking](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/designing-order-tracking) information in iOS 16 or later, configure a `setOrderTracking` callback function. Stripe calls your implementation after the payment is complete, but before iOS dismisses the Apple Pay sheet.

In your implementation of `setOrderTracking` callback function, fetch the order details from your server for the completed order, and pass the details to the provided `completion` function.

To learn more about order tracking, see [Apple’s Wallet Orders documentation](https://developer.apple.com/documentation/walletorders).

#### iOS (React Native)

```javascript
await initPaymentSheet({
  // ...
  applePay: {
    // ...
    setOrderTracking: async (complete) => {
      const apiEndpoint =
        Platform.OS === "ios" ?
          "http://localhost:4242"
        : "http://10.0.2.2:4567";
      const response = await fetch(
        `${apiEndpoint}/retrieve-order?orderId=${orderId}`,
        {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        },
      );
      if (response.status === 200) {
        const orderDetails = await response.json();
        // orderDetails should include orderIdentifier, orderTypeIdentifier,
        // authenticationToken and webServiceUrl
        complete(orderDetails);
      }
    },
  },
});
```

## Optional: Enable Google Pay

### Set up your integration

To use Google Pay, first enable the Google Pay API by adding the following to the `<application>` tag of your **AndroidManifest.xml**:

```xml
<application>
  ...
  <meta-data
    android:name="com.google.android.gms.wallet.api.enabled"
    android:value="true" />
</application>
```

For more details, see Google Pay’s [Set up Google Pay API](https://developers.google.com/pay/api/android/guides/setup) for Android.

### Add Google Pay

When you initialize `PaymentSheet`, set `merchantCountryCode` to the country code of your business and set `googlePay` to true.

You can also use the test environment by passing the `testEnv` parameter. You can only test Google Pay on a physical Android device. Follow the [React Native docs](https://reactnative.dev/docs/running-on-device) to test your application on a physical device.

```javascript
const { error, paymentOption } = await initPaymentSheet({
  // ...
  googlePay: {
    merchantCountryCode: "US",
    testEnv: true, // use test environment
  },
});
```

## Optional: Customize the sheet

All customization is configured using `initPaymentSheet`.

### Appearance

Customize colors, fonts, and so on to match the look and feel of your app by using the [appearance API](https://docs.stripe.com/elements/appearance-api/mobile.md?platform=react-native).

### Merchant display name

Specify a customer-facing business name by setting `merchantDisplayName`. By default, this is your app’s name.

```javascript
await initPaymentSheet({
  // ...
  merchantDisplayName: "Example Inc.",
});
```

### Dark mode

By default, `PaymentSheet` automatically adapts to the user’s system-wide appearance settings (light and dark mode). You can change this by setting the `style` property to `alwaysLight` or `alwaysDark` mode on iOS.

```javascript
await initPaymentSheet({
  // ...
  style: "alwaysDark",
});
```

On Android, set light or dark mode on your app:

```
// force dark
AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_YES)
// force light
AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_NO)
```

### Default billing details

To set default values for billing details collected in the PaymentSheet, configure the `defaultBillingDetails` property. The `PaymentSheet` pre-populates its fields with the values that you provide.

```javascript
await initPaymentSheet({
  // ...
  defaultBillingDetails: {
    email: "foo@bar.com",
    address: {
      country: "US",
    },
  },
});
```

### Collect billing details

Use `billingDetailsCollectionConfiguration` to specify how you want to collect billing details in the PaymentSheet.

You can collect your customer’s name, email, phone number, and address.

If you don’t intend to collect the values that the payment method requires, you must do the following:

1. Attach the values that aren’t collected by `PaymentSheet` to the `defaultBillingDetails` property.
1. Set `billingDetailsCollectionConfiguration.attachDefaultsToPaymentMethod` to `true`.

```javascript
await initPaymentSheet({
  // ...
  defaultBillingDetails: {
    email: "foo@bar.com",
  },
  billingDetailsCollectionConfiguration: {
    name: PaymentSheet.CollectionMode.ALWAYS,
    email: PaymentSheet.CollectionMode.NEVER,
    address: PaymentSheet.AddressCollectionMode.FULL,
    attachDefaultsToPaymentMethod: true,
  },
});
```

> Consult with your legal counsel regarding laws that apply to collecting information. Only collect phone numbers if you need them for the transaction.
