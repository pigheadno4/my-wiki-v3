<!-- Source URL: https://docs.stripe.com/payments/mobile/set-up-future-payments -->
<!-- Fetched: 2026-04-22 -->

# Set up future payments

Learn how to save payment details in your mobile app and charge your customers later.

# iOS

> This is a iOS for when platform is ios and mobile-ui is payment-element. View the full page at https://docs.stripe.com/payments/mobile/set-up-future-payments?platform=ios&mobile-ui=payment-element.

The [Setup Intents API](https://docs.stripe.com/api/setup_intents.md) lets you save a customer’s payment details without an initial payment. This is helpful if you want to onboard customers now, set them up for payments, and charge them in the future—when they’re offline.

Use this integration to set up recurring payments or to create one-time payments with a final amount determined later, often after the customer receives your service.

> #### Card-present transactions
>
> Card-present transactions, such as collecting card details through Stripe Terminal, use a different process for saving the payment method. For details, see [the Terminal documentation](https://docs.stripe.com/terminal/features/saving-payment-details/save-directly.md).

## Compliance

You’re responsible for your compliance with all applicable laws, regulations, and network rules when saving a customer’s payment details. These requirements generally apply if you want to save your customer’s payment method for future use, such as displaying a customer’s payment method to them in the checkout flow for a future purchase or charging them when they’re not actively using your website or app. Add terms to your website or app that state how you plan to save payment method details and allow customers to opt in.

When you save a payment method, you can only use it for the specific usage you’ve included in your terms. To charge a payment method when a customer is offline and save it as an option for future purchases, make sure that you explicitly collect consent from the customer for this specific use. For example, include a “Save my payment method for future use” checkbox to collect consent.

To charge them when they’re offline, make sure your terms include the following:

- The customer’s agreement to your initiating a payment or a series of payments on their behalf for specified transactions.
- The anticipated timing and frequency of payments (for example, if the charges are for scheduled installments, subscription payments, or unscheduled top-ups).
- How you determine the payment amount.
- Your cancellation policy, if the payment method is for a subscription service.

Make sure you keep a record of your customer’s written agreement to these terms.

> If you need to use manual server-side confirmation or your integration requires presenting payment methods separately, see our [alternative guide](https://docs.stripe.com/payments/save-and-reuse-cards-only.md).
> ![](assets/ios-overview.9e0d68d009dc005f73a6f5df69e00458.png)

Integrate Stripe’s prebuilt payment UI into the checkout of your iOS app with the [PaymentSheet](https://stripe.dev/stripe-ios/stripe-paymentsheet/Classes/PaymentSheet.html) class. See our sample integration [on GitHub](https://github.com/stripe/stripe-ios/tree/master/Example/PaymentSheet%20Example).

## Set up Stripe [Server-side] [Client-side]

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

## Add an endpoint [Server-side]

> The mobile Payment Element only supports SetupIntents with cards, Bancontact, iDEAL, Link, SEPA Direct Debit, Sofort, and US bank accounts.

If your integration uses [customer-configured Accounts](https://docs.stripe.com/api/v2/core/accounts/create.md#v2_create_accounts-configuration-customer), replace `Customer` and event references in the code examples with the equivalent Accounts v2 API references. For more information, see [Represent customers with Account objects](https://docs.stripe.com/connect/use-accounts-as-customers.md).

This integration uses three Stripe API objects:

1. A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) is an object that represents your intent to set up a customer’s payment method for future payments. The payment methods shown to customers during the checkout process are also included on the SetupIntent. You can let Stripe automatically pull payment methods from your Dashboard settings or you can list them manually.

1. A _Customer_ (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments). To set up a payment method for future payments, it must be attached to a Customer. Create a Customer object when your customer creates an account with your business. If your customer is making a payment as a guest, you can create a Customer object before payment and associate it with your own internal representation of the customer’s account later.

1. A Customer Ephemeral Key (optional). Information on the Customer object is sensitive, and can’t be retrieved directly from an app. An Ephemeral Key grants the SDK temporary access to the Customer.

For security reasons, your app can’t create these objects. Instead, add an endpoint on your server that:

1. Retrieves the Customer, or creates a new one.
1. Creates an Ephemeral Key for the Customer.
1. Creates a SetupIntent with the Customer ID.
1. Returns the SetupIntent’s [client secret](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-client_secret), the Ephemeral Key’s `secret`, the Customer’s [ID](https://docs.stripe.com/api/customers/object.md#customer_object-id), and your [publishable key](https://dashboard.stripe.com/apikeys) to your app.

The payment methods shown to customers during the checkout process are also included on the SetupIntent. You can let Stripe automatically pull payment methods from your Dashboard settings or you can list them manually.

#### Manage payment methods from the Dashboard

You can manage payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods). Stripe handles the return of eligible payment methods based on factors such as the transaction’s amount, currency, and payment flow.

#### Accounts v2

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
// This example sets up an endpoint using the Express framework.

app.post("/payment-sheet", async (req, res) => {
  // Use an existing Account ID if this is a returning customer.
  const customerAccount = await stripe.v2.core.accounts.create({
    configuration: { customer: {} },
  });
  const ephemeralKey = await stripe.ephemeralKeys.create(
    { customer_account: customerAccount.id },
    {
      apiVersion: "2026-03-25.dahlia",
    },
  );
  const setupIntent = await stripe.setupIntents.create({
    customer_account: customerAccount.id,

    automatic_payment_methods: {
      enabled: true,
    },
  });
  res.json({
    setupIntent: setupIntent.client_secret,
    ephemeralKey: ephemeralKey.secret,
    customer_account: customerAccount.id,
    publishableKey: "<<YOUR_PUBLISHABLE_KEY>>",
  });
});
```

#### Customers v1

#### Node.js

```javascript

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');
// This example sets up an endpoint using the Express framework.

app.post('/payment-sheet', async (req, res) => {
  // Use an existing Customer ID if this is a returning customer.
  const customer = await stripe.customers.create(stripeAccount:'{{CONNECTED_ACCOUNT_ID}}');
  const ephemeralKey = await stripe.ephemeralKeys.create(
    {customer: customer.id},
    {
      stripeAccount: '{{CONNECTED_ACCOUNT_ID}}',
      apiVersion: '2026-03-25.dahlia'
    }
  );
  const setupIntent = await stripe.setupIntents.create({
    customer: customer.id,

    automatic_payment_methods: {
      enabled: true,
    },
  });
  res.json({
    setupIntent: setupIntent.client_secret,
    ephemeralKey: ephemeralKey.secret,
    customer: customer.id,
    publishableKey: '<<YOUR_PUBLISHABLE_KEY>>'
  })
});
```

#### Listing payment methods manually

> You can fork and deploy an implementation of this endpoint on [CodeSandbox](https://codesandbox.io/p/devbox/suspicious-lalande-l325w6) for testing.

#### Accounts v2

#### Node.js

```javascript
// This example sets up an endpoint using the Express framework.

app.post("/payment-sheet", async (req, res) => {
  // Use an existing Account ID if this is a returning customer.
  const customerAccount = await stripe.v2.core.accounts.create({
    configuration: { customer: {} },
  });
  const ephemeralKey = await stripe.ephemeralKeys.create(
    { customer_account: customerAccount.id },
    {
      apiVersion: "2026-03-25.dahlia",
    },
  );
  const setupIntent = await stripe.setupIntents.create({
    customer_account: customerAccount.id,
  });
  res.json({
    setupIntent: setupIntent.client_secret,
    ephemeralKey: ephemeralKey.secret,
    customer_account: customerAccount.id,
    publishableKey: "<<YOUR_PUBLISHABLE_KEY>>",
  });
});
```

#### Customers v1

#### Node.js

```javascript

// This example sets up an endpoint using the Express framework.

app.post('/payment-sheet', async (req, res) => {
  // Use an existing Customer ID if this is a returning customer.
  const customer = await stripe.customers.create(stripeAccount:'{{CONNECTED_ACCOUNT_ID}}');
  const ephemeralKey = await stripe.ephemeralKeys.create(
    {customer: customer.id},
    {
      stripeAccount: '{{CONNECTED_ACCOUNT_ID}}',
      apiVersion: '2026-03-25.dahlia'
    }
  );
  const setupIntent = await stripe.setupIntents.create({
    customer: customer.id,
  });
  res.json({
    setupIntent: setupIntent.client_secret,
    ephemeralKey: ephemeralKey.secret,
    customer: customer.id,
    publishableKey: '<<YOUR_PUBLISHABLE_KEY>>'
  })
});
```

## Collect payment details [Client-side]

To display the mobile Payment Element on your checkout page, you must add a checkout button that displays Stripe’s UI.

#### UIKit

In your app’s checkout screen, fetch the SetupIntent client secret, CustomerSession client secret, Customer ID, and publishable key from the endpoint you created in the previous step. Use `STPAPIClient.shared` to set your publishable key and initialize the [PaymentSheet](https://stripe.dev/stripe-ios/stripe-paymentsheet/Classes/PaymentSheet.html).

#### iOS (Swift)

```swift
import UIKit@_spi(CustomerSessionBetaAccess) import StripePaymentSheet

class CheckoutViewController: UIViewController {
  @IBOutlet weak var checkoutButton: UIButton!
  var paymentSheet: PaymentSheet?
  let backendCheckoutUrl = URL(string: "Your backend endpoint/payment-sheet")! // Your backend endpoint

  override func viewDidLoad() {
    super.viewDidLoad()

    checkoutButton.addTarget(self, action: #selector(didTapCheckoutButton), for: .touchUpInside)
    checkoutButton.isEnabled = false

    // MARK: Fetch the SetupIntent client secret, CustomerSession client secret, Customer ID, and publishable key
    var request = URLRequest(url: backendCheckoutUrl)
    request.httpMethod = "POST"
    let task = URLSession.shared.dataTask(with: request, completionHandler: { [weak self] (data, response, error) in
      guard let data = data,
            let json = try? JSONSerialization.jsonObject(with: data, options: []) as? [String : Any],
            let customerId = json["customer"] as? String,
            let customerSessionClientSecret = json["customerSessionClientSecret"] as? String,
            let setupIntentClientSecret = json["setupIntent"] as? String,
            let publishableKey = json["publishableKey"] as? String,
            let self = self else {
        // Handle error
        return
      }
STPAPIClient.shared.publishableKey = publishableKey// MARK: Create a PaymentSheet instance
      var configuration = PaymentSheet.Configuration()
      configuration.merchantDisplayName = "Example, Inc."
      configuration.customer = .init(id: customerId, customerSessionClientSecret: customerSessionClientSecret)
      // Set `allowsDelayedPaymentMethods` to true if your business handles
      // delayed notification payment methods like US bank accounts.
      configuration.allowsDelayedPaymentMethods = true
      self.paymentSheet = PaymentSheet(setupIntentClientSecret:setupIntentClientSecret, configuration: configuration)

      DispatchQueue.main.async {
        self.checkoutButton.isEnabled = true
      }
    })
    task.resume()
  }

}
```

When the customer taps the **Checkout** button, call `present` to present the PaymentSheet. After the customer completes the payment, Stripe dismisses the PaymentSheet and calls the completion block with [PaymentSheetResult](https://stripe.dev/stripe-ios/stripe-paymentsheet/Enums/PaymentSheetResult.html).

#### iOS (Swift)

```swift
@objc
func didTapCheckoutButton() {
  // MARK: Start the checkout process
  paymentSheet?.present(from: self) { paymentResult in
    // MARK: Handle the payment result
    switch paymentResult {
    case .completed:
      print("Your order is confirmed")
    case .canceled:
      print("Canceled!")
    case .failed(let error):
      print("Payment failed: \(error)")
    }
  }
}
```

#### SwiftUI

Create an `ObservableObject` model for your checkout screen. This model publishes a [PaymentSheet](https://stripe.dev/stripe-ios/stripe-paymentsheet/Classes/PaymentSheet.html) and a [PaymentSheetResult](https://stripe.dev/stripe-ios/stripe-paymentsheet/Enums/PaymentSheetResult.html).

```swift
import StripePaymentSheet
import SwiftUI

class CheckoutViewModel: ObservableObject {
  let backendCheckoutUrl = URL(string: "Your backend endpoint/payment-sheet")! // Your backend endpoint
  @Published var paymentSheet: PaymentSheet?
  @Published var paymentResult: PaymentSheetResult?
}
```

Fetch the SetupIntent client secret, CustomerSession client secret, Customer ID, and publishable key from the endpoint you created in the previous step. Use `STPAPIClient.shared` to set your publishable key and initialize the [PaymentSheet](https://stripe.dev/stripe-ios/stripe-paymentsheet/Classes/PaymentSheet.html).

```swift
@_spi(CustomerSessionBetaAccess) import StripePaymentSheet
import SwiftUI

class CheckoutViewModel: ObservableObject {
  let backendCheckoutUrl = URL(string: "Your backend endpoint/payment-sheet")! // Your backend endpoint
  @Published var paymentSheet: PaymentSheet?
  @Published var paymentResult: PaymentSheetResult?
func preparePaymentSheet() {
    // MARK: Fetch theSetupIntent and Customer information from the backend
    var request = URLRequest(url: backendCheckoutUrl)
    request.httpMethod = "POST"
    let task = URLSession.shared.dataTask(with: request, completionHandler: { [weak self] (data, response, error) in
      guard let data = data,
            let json = try? JSONSerialization.jsonObject(with: data, options: []) as? [String : Any],
            let customerId = json["customer"] as? String,
            let customerSessionClientSecret = json["customerSessionClientSecret"] as? String,
            letsetupIntentClientSecret = json["setupIntent"] as? String,
            let publishableKey = json["publishableKey"] as? String,
            let self = self else {
        // Handle error
        return
      }

      STPAPIClient.shared.publishableKey = publishableKey// MARK: Create a PaymentSheet instance
      var configuration = PaymentSheet.Configuration()
      configuration.merchantDisplayName = "Example, Inc."
      configuration.customer = .init(id: customerId, customerSessionClientSecret: customerSessionClientSecret)
      // Set `allowsDelayedPaymentMethods` to true if your business handles
      // delayed notification payment methods like US bank accounts.
      configuration.allowsDelayedPaymentMethods = true

      DispatchQueue.main.async {
        self.paymentSheet = PaymentSheet(setupIntentClientSecret:setupIntentClientSecret, configuration: configuration)
      }
    })
    task.resume()
  }
}
struct CheckoutView: View {
  @ObservedObject var model = CheckoutViewModel()

  var body: some View {
    VStack {
      if model.paymentSheet != nil {
        Text("Ready to pay.")
      } else {
        Text("Loading…")
      }
    }.onAppear { model.preparePaymentSheet() }
  }
}
```

Add a [PaymentSheet.PaymentButton](https://stripe.dev/stripe-ios/stripe-paymentsheet/Classes/PaymentSheet/PaymentButton.html) to your `View`. This behaves similarly to a SwiftUI `Button`, which allows you to customize it by adding a `View`. When you tap the button, it displays the PaymentSheet. After you complete the payment, Stripe dismisses the PaymentSheet and calls the `onCompletion` handler with a [PaymentSheetResult](https://stripe.dev/stripe-ios/stripe-paymentsheet/Enums/PaymentSheetResult.html) object.

```swift
@_spi(CustomerSessionBetaAccess) import StripePaymentSheet
import SwiftUI

class CheckoutViewModel: ObservableObject {
  let backendCheckoutUrl = URL(string: "Your backend endpoint/payment-sheet")! // Your backend endpoint
  @Published var paymentSheet: PaymentSheet?
  @Published var paymentResult: PaymentSheetResult?

  func preparePaymentSheet() {
    // MARK: Fetch the SetupIntent and Customer information from the backend
    var request = URLRequest(url: backendCheckoutUrl)
    request.httpMethod = "POST"
    let task = URLSession.shared.dataTask(with: request, completionHandler: { [weak self] (data, response, error) in
      guard let data = data,
            let json = try? JSONSerialization.jsonObject(with: data, options: []) as? [String : Any],
            let customerId = json["customer"] as? String,
            let customerSessionClientSecret = json["customerSessionClientSecret"] as? String,
            let setupIntentClientSecret = json["setupIntent"] as? String,
            let publishableKey = json["publishableKey"] as? String,
            let self = self else {
        // Handle error
        return
      }

      STPAPIClient.shared.publishableKey = publishableKey
      // MARK: Create a PaymentSheet instance
      var configuration = PaymentSheet.Configuration()
      configuration.merchantDisplayName = "Example, Inc."
      configuration.customer = .init(id: customerId, customerSessionClientSecret: customerSessionClientSecret)
      // Set `allowsDelayedPaymentMethods` to true if your business can handle payment methods
      // that complete payment after a delay, like SEPA Debit and Sofort.
      configuration.allowsDelayedPaymentMethods = true

      DispatchQueue.main.async {
        self.paymentSheet = PaymentSheet(setupIntentClientSecret: setupIntentClientSecret, configuration: configuration)
      }
    })
    task.resume()
  }
func onPaymentCompletion(result: PaymentSheetResult) {
    self.paymentResult = result
  }
}

struct CheckoutView: View {
  @ObservedObject var model = CheckoutViewModel()

  var body: some View {
    VStack {if let paymentSheet = model.paymentSheet {
        PaymentSheet.PaymentButton(
          paymentSheet: paymentSheet,
          onCompletion: model.onPaymentCompletion
        ) {
          Text("Buy")
        }
      } else {
        Text("Loading…")
      }if let result = model.paymentResult {
        switch result {
        case .completed:
          Text("Payment complete")
        case .failed(let error):
          Text("Payment failed: \(error.localizedDescription)")
        case .canceled:
          Text("Payment canceled.")
        }
      }
    }.onAppear { model.preparePaymentSheet() }
  }
}
```

If `PaymentSheetResult` is `.completed`, inform the user (for example, by displaying an order confirmation screen).

Setting `allowsDelayedPaymentMethods` to true allows [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment methods like US bank accounts. For these payment methods, the final payment status isn’t known when the `PaymentSheet` completes, and instead succeeds or fails later. If you support these types of payment methods, inform the customer their order is confirmed and only fulfill their order (for example, ship their product) when the payment is successful.

## Set up a return URL [Server-side]

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

## Charge the saved payment method later [Server-side]

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

| Payment method | Scenario                                                                                                                                                                                                                                                                                                        | How to test                                                                                                                 |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Credit card    | The card setup succeeds and doesn’t require _authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase). | Fill out the credit card form using the credit card number `4242 4242 4242 4242` with any expiration, CVC, and postal code. |
| Credit card    | The card requires authentication for the initial setup, then succeeds for subsequent payments.                                                                                                                                                                                                                  | Fill out the credit card form using the credit card number `4000 0025 0000 3155` with any expiration, CVC, and postal code. |
| Credit card    | The card requires authentication for the initial setup and also requires authentication for subsequent payments.                                                                                                                                                                                                | Fill out the credit card form using the credit card number `4000 0027 6000 3184` with any expiration, CVC, and postal code. |
| Credit card    | The card is declined during setup.                                                                                                                                                                                                                                                                              | Fill out the credit card form using the credit card number `4000 0000 0000 9995` with any expiration, CVC, and postal code. |

## Optional: Enable Apple Pay

> If your checkout screen has a dedicated **Apple Pay button**, follow the [Apple Pay guide](https://docs.stripe.com/apple-pay.md#present-payment-sheet) and use `ApplePayContext` to collect payment from your Apple Pay button. You can use `PaymentSheet` to handle other payment method types.

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

## Enable card scanning

To enable card scanning support for iOS, set the `NSCameraUsageDescription` (**Privacy - Camera Usage Description**) in the `Info.plist` of your application, and provide a reason for accessing the camera (for example, “To scan cards”).

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

## Optional: Complete payment in your UI

You can present the Payment Sheet to only collect payment method details and then later call a `confirm` method to complete payment in your app’s UI. This is useful if you have a custom buy button or require additional steps after you collect payment details.
![](assets/ios-multi-step.cd631ea4f1cd8cf3f39b6b9e1e92b6c5.png)

Complete the payment in your app’s UI

#### UIKit

The following steps walk you through how to complete payment in your app’s UI. See our sample integration out on [GitHub](https://github.com/stripe/stripe-ios/blob/master/Example/PaymentSheet%20Example/PaymentSheet%20Example/ExampleCustomCheckoutViewController.swift).

1. First, initialize [PaymentSheet.FlowController](https://stripe.dev/stripe-ios/stripepaymentsheet/documentation/stripepaymentsheet/paymentsheet/flowcontroller) instead of `PaymentSheet` and update your UI with its `paymentOption` property. This property contains an image and label representing the customer’s initially selected, default payment method.

```swift
PaymentSheet.FlowController.create(paymentIntentClientSecret: paymentIntentClientSecret, configuration: configuration) { [weak self] result in
  switch result {
  case .failure(let error):
    print(error)
  case .success(let paymentSheetFlowController):
    self?.paymentSheetFlowController = paymentSheetFlowController
    // Update your UI using paymentSheetFlowController.paymentOption
  }
}
```

1. Next, call `presentPaymentOptions` to collect payment details. When completed, update your UI again with the `paymentOption` property.

```swift
paymentSheetFlowController.presentPaymentOptions(from: self) {
  // Update your UI using paymentSheetFlowController.paymentOption
}
```

1. Finally, call `confirm`.

```swift
paymentSheetFlowController.confirm(from: self) { paymentResult in
  // MARK: Handle the payment result
  switch paymentResult {
  case .completed:
    print("Payment complete!")
  case .canceled:
    print("Canceled!")
  case .failed(let error):
    print(error)
  }
}
```

#### SwiftUI

The following steps walk you through how to complete payment in your app’s UI. See our sample integration out on [GitHub](https://github.com/stripe/stripe-ios/blob/master/Example/PaymentSheet%20Example/PaymentSheet%20Example/ExampleSwiftUICustomPaymentFlow.swift).

1. First, initialize [PaymentSheet.FlowController](https://stripe.dev/stripe-ios/stripepaymentsheet/documentation/stripepaymentsheet/paymentsheet/flowcontroller) instead of `PaymentSheet`. Its `paymentOption` property contains an image and label representing the customer’s currently selected payment method, which you can use in your UI.

```swift
PaymentSheet.FlowController.create(paymentIntentClientSecret: paymentIntentClientSecret, configuration: configuration) { [weak self] result in
  switch result {
  case .failure(let error):
    print(error)
  case .success(let paymentSheetFlowController):
    self?.paymentSheetFlowController = paymentSheetFlowController
    // Use the paymentSheetFlowController.paymentOption properties in your UI
    myPaymentMethodLabel = paymentSheetFlowController.paymentOption?.label ?? "Select a payment method"
    myPaymentMethodImage = paymentSheetFlowController.paymentOption?.image ?? UIImage(systemName: "square.and.pencil")!
  }
}
```

1. Use [PaymentSheet.FlowController.PaymentOptionsButton](https://stripe.dev/stripe-ios/stripepaymentsheet/documentation/stripepaymentsheet/paymentsheet/flowcontroller/paymentoptionsbutton) to wrap the button that presents the sheet to collect payment details. When `PaymentSheet.FlowController` calls the `onSheetDismissed` argument, the `paymentOption` for the `PaymentSheet.FlowController` instance reflects the currently selected payment method.

```swift
PaymentSheet.FlowController.PaymentOptionsButton(
  paymentSheetFlowController: paymentSheetFlowController,
  onSheetDismissed: {
    myPaymentMethodLabel = paymentSheetFlowController.paymentOption?.label ?? "Select a payment method"
    myPaymentMethodImage = paymentSheetFlowController.paymentOption?.image ?? UIImage(systemName: "square.and.pencil")!
  },
  content: {
    /* An example button */
    HStack {
      Text(myPaymentMethodLabel)
      Image(uiImage: myPaymentMethodImage)
    }
  }
)
```

1. Use [PaymentSheet.FlowController.PaymentOptionsButton](https://stripe.dev/stripe-ios/stripepaymentsheet/documentation/stripepaymentsheet/paymentsheet/flowcontroller/paymentoptionsbutton) to wrap the button that confirms the payment.

```swift
PaymentSheet.FlowController.ConfirmButton(
  paymentSheetFlowController: paymentSheetFlowController,
  onCompletion: { result in
    // MARK: Handle the payment result
    switch result {
    case .completed:
      print("Payment complete!")
    case .canceled:
      print("Canceled!")
    case .failed(let error):
      print(error)
    }
  },
  content: {
    /* An example button */
    Text("Pay")
  }
)
```

# Android

> This is a Android for when platform is android and mobile-ui is payment-element. View the full page at https://docs.stripe.com/payments/mobile/set-up-future-payments?platform=android&mobile-ui=payment-element.

The [Setup Intents API](https://docs.stripe.com/api/setup_intents.md) lets you save a customer’s payment details without an initial payment. This is helpful if you want to onboard customers now, set them up for payments, and charge them in the future—when they’re offline.

Use this integration to set up recurring payments or to create one-time payments with a final amount determined later, often after the customer receives your service.

> #### Card-present transactions
>
> Card-present transactions, such as collecting card details through Stripe Terminal, use a different process for saving the payment method. For details, see [the Terminal documentation](https://docs.stripe.com/terminal/features/saving-payment-details/save-directly.md).

## Compliance

You’re responsible for your compliance with all applicable laws, regulations, and network rules when saving a customer’s payment details. These requirements generally apply if you want to save your customer’s payment method for future use, such as displaying a customer’s payment method to them in the checkout flow for a future purchase or charging them when they’re not actively using your website or app. Add terms to your website or app that state how you plan to save payment method details and allow customers to opt in.

When you save a payment method, you can only use it for the specific usage you’ve included in your terms. To charge a payment method when a customer is offline and save it as an option for future purchases, make sure that you explicitly collect consent from the customer for this specific use. For example, include a “Save my payment method for future use” checkbox to collect consent.

To charge them when they’re offline, make sure your terms include the following:

- The customer’s agreement to your initiating a payment or a series of payments on their behalf for specified transactions.
- The anticipated timing and frequency of payments (for example, if the charges are for scheduled installments, subscription payments, or unscheduled top-ups).
- How you determine the payment amount.
- Your cancellation policy, if the payment method is for a subscription service.

Make sure you keep a record of your customer’s written agreement to these terms.

> If you need to use manual server-side confirmation or your integration requires presenting payment methods separately, see our [alternative guide](https://docs.stripe.com/payments/save-and-reuse-cards-only.md).
> ![](assets/android-overview.471eaf89a760f5b6a757fd96b6bb9b60.png)

Integrate Stripe’s prebuilt payment UI into the checkout of your Android app with the [PaymentSheet](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/index.html) class.

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

## Add an endpoint [Server-side]

> The mobile Payment Element only supports SetupIntents with cards, Link, and US bank accounts.

If your integration uses [customer-configured Accounts](https://docs.stripe.com/api/v2/core/accounts/create.md#v2_create_accounts-configuration-customer), replace `Customer` and event references in the code examples with the equivalent Accounts v2 API references. For more information, see [Represent customers with Account objects](https://docs.stripe.com/connect/use-accounts-as-customers.md).

This integration uses three Stripe API objects:

1. A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) is an object that represents your intent to set up a customer’s payment method for future payments. The payment methods shown to customers during the checkout process are also included on the SetupIntent. You can let Stripe automatically pull payment methods from your Dashboard settings or you can list them manually.

1. A _Customer_ (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments). To set up a payment method for future payments, it must be attached to a Customer. Create a Customer object when your customer creates an account with your business. If your customer is making a payment as a guest, you can create a Customer object before payment and associate it with your own internal representation of the customer’s account later.

1. A Customer Ephemeral Key (optional). Information on the Customer object is sensitive, and can’t be retrieved directly from an app. An Ephemeral Key grants the SDK temporary access to the Customer.

For security reasons, your app can’t create these objects. Instead, add an endpoint on your server that:

1. Retrieves the Customer, or creates a new one.
1. Creates an Ephemeral Key for the Customer.
1. Creates a SetupIntent with the Customer ID.
1. Returns the SetupIntent’s [client secret](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-client_secret), the Ephemeral Key’s `secret`, the Customer’s [ID](https://docs.stripe.com/api/customers/object.md#customer_object-id), and your [publishable key](https://dashboard.stripe.com/apikeys) to your app.

The payment methods shown to customers during the checkout process are also included on the SetupIntent. You can let Stripe automatically pull payment methods from your Dashboard settings or you can list them manually.

#### Manage payment methods from the Dashboard

You can manage payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods). Stripe handles the return of eligible payment methods based on factors such as the transaction’s amount, currency, and payment flow.

#### Accounts v2

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
// This example sets up an endpoint using the Express framework.

app.post("/payment-sheet", async (req, res) => {
  // Use an existing Account ID if this is a returning customer.
  const customerAccount = await stripe.v2.core.accounts.create({
    configuration: { customer: {} },
  });
  const ephemeralKey = await stripe.ephemeralKeys.create(
    { customer_account: customerAccount.id },
    {
      apiVersion: "2026-03-25.dahlia",
    },
  );
  const setupIntent = await stripe.setupIntents.create({
    customer_account: customerAccount.id,

    automatic_payment_methods: {
      enabled: true,
    },
  });
  res.json({
    setupIntent: setupIntent.client_secret,
    ephemeralKey: ephemeralKey.secret,
    customer_account: customerAccount.id,
    publishableKey: "<<YOUR_PUBLISHABLE_KEY>>",
  });
});
```

#### Customers v1

#### Node.js

```javascript

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');
// This example sets up an endpoint using the Express framework.

app.post('/payment-sheet', async (req, res) => {
  // Use an existing Customer ID if this is a returning customer.
  const customer = await stripe.customers.create(stripeAccount:'{{CONNECTED_ACCOUNT_ID}}');
  const ephemeralKey = await stripe.ephemeralKeys.create(
    {customer: customer.id},
    {
      stripeAccount: '{{CONNECTED_ACCOUNT_ID}}',
      apiVersion: '2026-03-25.dahlia'
    }
  );
  const setupIntent = await stripe.setupIntents.create({
    customer: customer.id,

    automatic_payment_methods: {
      enabled: true,
    },
  });
  res.json({
    setupIntent: setupIntent.client_secret,
    ephemeralKey: ephemeralKey.secret,
    customer: customer.id,
    publishableKey: '<<YOUR_PUBLISHABLE_KEY>>'
  })
});
```

#### Listing payment methods manually

> You can fork and deploy an implementation of this endpoint on [CodeSandbox](https://codesandbox.io/p/devbox/suspicious-lalande-l325w6) for testing.

#### Accounts v2

#### Node.js

```javascript
// This example sets up an endpoint using the Express framework.

app.post("/payment-sheet", async (req, res) => {
  // Use an existing Account ID if this is a returning customer.
  const customerAccount = await stripe.v2.core.accounts.create({
    configuration: { customer: {} },
  });
  const ephemeralKey = await stripe.ephemeralKeys.create(
    { customer_account: customerAccount.id },
    {
      apiVersion: "2026-03-25.dahlia",
    },
  );
  const setupIntent = await stripe.setupIntents.create({
    customer_account: customerAccount.id,
  });
  res.json({
    setupIntent: setupIntent.client_secret,
    ephemeralKey: ephemeralKey.secret,
    customer_account: customerAccount.id,
    publishableKey: "<<YOUR_PUBLISHABLE_KEY>>",
  });
});
```

#### Customers v1

#### Node.js

```javascript

// This example sets up an endpoint using the Express framework.

app.post('/payment-sheet', async (req, res) => {
  // Use an existing Customer ID if this is a returning customer.
  const customer = await stripe.customers.create(stripeAccount:'{{CONNECTED_ACCOUNT_ID}}');
  const ephemeralKey = await stripe.ephemeralKeys.create(
    {customer: customer.id},
    {
      stripeAccount: '{{CONNECTED_ACCOUNT_ID}}',
      apiVersion: '2026-03-25.dahlia'
    }
  );
  const setupIntent = await stripe.setupIntents.create({
    customer: customer.id,
  });
  res.json({
    setupIntent: setupIntent.client_secret,
    ephemeralKey: ephemeralKey.secret,
    customer: customer.id,
    publishableKey: '<<YOUR_PUBLISHABLE_KEY>>'
  })
});
```

## Collect payment details [Client-side]

Before displaying the mobile Payment Element, your checkout page should include a checkout button to present Stripe’s UI.

#### Jetpack Compose

[Initialize](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/-builder/index.html) a `PaymentSheet` instance inside `onCreate` of your checkout Activity, passing a method to handle the result.

```kotlin
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import com.stripe.android.paymentsheet.PaymentSheet
import com.stripe.android.paymentsheet.PaymentSheetResult

@Composable
fun App() {
  val paymentSheet = remember { PaymentSheet.Builder(::onPaymentSheetResult) }.build()
}

private fun onPaymentSheetResult(paymentSheetResult: PaymentSheetResult) {
  // implemented in the next steps
}
```

Next, fetch the SetupIntent client secret, Customer Session client secret, Customer ID, and publishable key from the endpoint you created in the previous step. Set the publishable key using `PaymentConfiguration` and store the others for use when you present the PaymentSheet.

```kotlin
import androidx.compose.runtime.Composable
import androidx.compose.runtime.rememberimport androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.compose.ui.platform.LocalContext
import com.stripe.android.PaymentConfiguration
import com.stripe.android.paymentsheet.PaymentSheet
import com.stripe.android.paymentsheet.PaymentSheetResult

@Composable
fun App() {
  val paymentSheet = remember { PaymentSheet.Builder(::onPaymentSheetResult) }.build()val context = LocalContext.current
  var customerConfig by remember { mutableStateOf<PaymentSheet.CustomerConfiguration?>(null) }
  varsetupIntentClientSecret by remember { mutableStateOf<String?>(null) }

  LaunchedEffect(context) {
    // Make a request to your own server and retrieve payment configurations
    val networkResult = ...
    if (networkResult.isSuccess) {setupIntentClientSecret = networkResult.setupIntent
        customerConfig = PaymentSheet.CustomerConfiguration.createWithCustomerSession(
          id = networkResult.customer,
          clientSecret = networkResult.customerSessionClientSecret
        )PaymentConfiguration.init(context, networkResult.publishableKey)}
  }
}

private fun onPaymentSheetResult(paymentSheetResult: PaymentSheetResult) {
  // implemented in the next steps
}
```

Present the PaymentSheet by calling [presentWithSetupIntent()](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/index.html#-2013366375%2FFunctions%2F2002900378). After the customer completes setting up their payment method for future use, the sheet dismisses and the [PaymentSheetResultCallback](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet-result-callback/index.html) is called with a [PaymentSheetResult](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet-result/index.html).

```kotlin
import androidx.compose.material.Button
import androidx.compose.material.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.platform.LocalContext
import com.stripe.android.PaymentConfiguration
import com.stripe.android.paymentsheet.PaymentSheet
import com.stripe.android.paymentsheet.PaymentSheetResult

@Composable
fun App() {
  val paymentSheet = remember { PaymentSheet.Builder(::onPaymentSheetResult) }.build()
  val context = LocalContext.current
  var customerConfig by remember { mutableStateOf<PaymentSheet.CustomerConfiguration?>(null) }
  var setupIntentClientSecret by remember { mutableStateOf<String?>(null) }

  LaunchedEffect(context) {
    // Make a request to your own server and retrieve payment configurations
    val networkResult = ...
    if (networkResult.isSuccess) {
        setupIntentClientSecret = networkResult.setupIntent
        customerConfig = PaymentSheet.CustomerConfiguration.createWithCustomerSession(
          id = networkResult.customer,
          clientSecret = networkResult.customerSessionClientSecret
        )
        PaymentConfiguration.init(context, networkResult.publishableKey)
    }
  }Button(
    onClick = {
      val currentConfig = customerConfig
      val currentClientSecret =setupIntentClientSecret

      if (currentConfig != null && currentClientSecret != null) {
        presentPaymentSheet(paymentSheet, currentConfig, currentClientSecret)
      }
    }
  ) {
    Text("Checkout")
  }
}private fun presentPaymentSheet(
  paymentSheet: PaymentSheet,
  customerConfig: PaymentSheet.CustomerConfiguration,setupIntentClientSecret: String
) {
  paymentSheet.presentWithSetupIntent(setupIntentClientSecret,
    PaymentSheet.Configuration.Builder(merchantDisplayName = "My merchant name")
      .customer(customerConfig)
      // Set `allowsDelayedPaymentMethods` to true if your business handles
      // delayed notification payment methods like US bank accounts.
      .allowsDelayedPaymentMethods(true)
      .build()
  )
}
private fun onPaymentSheetResult(paymentSheetResult: PaymentSheetResult) {when(paymentSheetResult) {
    is PaymentSheetResult.Canceled -> {
      print("Canceled")
    }
    is PaymentSheetResult.Failed -> {
      print("Error: ${paymentSheetResult.error}")
    }
    is PaymentSheetResult.Completed -> {
      // Display for example, an order confirmation screen
      print("Completed")
    }
  }
}
```

#### Views (Classic)

[Initialize](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/index.html#-394860221%2FConstructors%2F2002900378) a `PaymentSheet` instance inside `onCreate` of your checkout Activity, passing a method to handle the result.

#### Kotlin

```kotlin
import com.stripe.android.paymentsheet.PaymentSheet

class CheckoutActivity : AppCompatActivity() {
  lateinit var paymentSheet: PaymentSheet

  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    paymentSheet = PaymentSheet.Builder(::onPaymentSheetResult).build(this)
  }

  fun onPaymentSheetResult(paymentSheetResult: PaymentSheetResult) {
    // implemented in the next steps
  }
}
```

Next, fetch the SetupIntent client secret, Customer Session client secret, Customer ID, and publishable key from the endpoint you created in the previous step. Set the publishable key using `PaymentConfiguration` and store the others for use when you present the PaymentSheet.

#### Kotlin

```kotlin
import com.stripe.android.paymentsheet.PaymentSheet

class CheckoutActivity : AppCompatActivity() {
  lateinit var paymentSheet: PaymentSheetlateinit var customerConfig: PaymentSheet.CustomerConfiguration
  lateinit varsetupIntentClientSecret: String

  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    paymentSheet = PaymentSheet.Builder(::onPaymentSheetResult).build(this)lifecycleScope.launch {
      // Make a request to your own server and retrieve payment configurations
      val networkResult = MyBackend.getPaymentConfig()
      if (networkResult.isSuccess) {setupIntentClientSecret = networkResult.setupIntent
        customerConfig = PaymentSheet.CustomerConfiguration.createWithCustomerSession(
          id = networkResult.customer,
          clientSecret = networkResult.customerSessionClientSecret
        )PaymentConfiguration.init(context, networkResult.publishableKey)}
    }
  }

  fun onPaymentSheetResult(paymentSheetResult: PaymentSheetResult) {
    // implemented in the next steps
  }
}
```

Present the PaymentSheet by calling [presentWithSetupIntent()](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/index.html#-2013366375%2FFunctions%2F2002900378). After the customer completes setting up their payment method for future use, the sheet dismisses and the [PaymentSheetResultCallback](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet-result-callback/index.html) is called with a [PaymentSheetResult](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet-result/index.html).

#### Kotlin

```kotlin
// ...
class CheckoutActivity : AppCompatActivity() {
  lateinit var paymentSheet: PaymentSheet
  lateinit var customerConfig: PaymentSheet.CustomerConfiguration
  lateinit var setupIntentClientSecret: String
  // ...fun presentPaymentSheet() {
    paymentSheet.presentWithSetupIntent(setupIntentClientSecret,
      PaymentSheet.Configuration.Builder(merchantDisplayName = "My merchant name")
        .customer(customerConfig)
        // Set `allowsDelayedPaymentMethods` to true if your business handles
        // delayed notification payment methods like US bank accounts.
        .allowsDelayedPaymentMethods(true)
        .build()
    )
  }

  fun onPaymentSheetResult(paymentSheetResult: PaymentSheetResult) {when(paymentSheetResult) {
      is PaymentSheetResult.Canceled -> {
        print("Canceled")
      }
      is PaymentSheetResult.Failed -> {
        print("Error: ${paymentSheetResult.error}")
      }
      is PaymentSheetResult.Completed -> {
        // Display for example, an order confirmation screen
        print("Completed")
      }
    }
  }
}
```

Setting `allowsDelayedPaymentMethods` to true allows [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment methods like US bank accounts. For these payment methods, the final payment status isn’t known when the `PaymentSheet` completes, and instead succeeds or fails later. If you support these types of payment methods, inform the customer their order is confirmed and only fulfill their order (for example, ship their product) when the payment is successful.

## Charge the saved payment method later [Server-side]

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

| Payment method | Scenario                                                                                                                                                                                                                                                                                                        | How to test                                                                                                                 |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Credit card    | The card setup succeeds and doesn’t require _authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase). | Fill out the credit card form using the credit card number `4242 4242 4242 4242` with any expiration, CVC, and postal code. |
| Credit card    | The card requires authentication for the initial setup, then succeeds for subsequent payments.                                                                                                                                                                                                                  | Fill out the credit card form using the credit card number `4000 0025 0000 3155` with any expiration, CVC, and postal code. |
| Credit card    | The card requires authentication for the initial setup and also requires authentication for subsequent payments.                                                                                                                                                                                                | Fill out the credit card form using the credit card number `4000 0027 6000 3184` with any expiration, CVC, and postal code. |
| Credit card    | The card is declined during setup.                                                                                                                                                                                                                                                                              | Fill out the credit card form using the credit card number `4000 0000 0000 9995` with any expiration, CVC, and postal code. |

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

## Optional: Complete payment in your UI

You can present Payment Sheet to only collect payment method details and complete the payment back in your app’s UI. This is useful if you have a custom buy button or require additional steps after payment details are collected.
![](assets/android-multi-step.84d8a0a44b1baa596bda491322b6d9fd.png)

> A sample integration is [available on our GitHub](https://github.com/stripe/stripe-android/blob/master/paymentsheet-example/src/main/java/com/stripe/android/paymentsheet/example/samples/ui/paymentsheet/custom_flow/CustomFlowActivity.kt).

1. First, initialize [PaymentSheet.FlowController](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/-flow-controller/index.html) instead of `PaymentSheet` using one of the [Builder](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/-flow-controller/-builder/index.html) methods.

#### Android (Kotlin)

```kotlin
class CheckoutActivity : AppCompatActivity() {
  private lateinit var flowController: PaymentSheet.FlowController

  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)

    val flowController = PaymentSheet.FlowController.Builder(
      resultCallback = ::onPaymentSheetResult,
      paymentOptionResultCallback = ::onPaymentOption,
    ).build(this)
  }
}
```

1. Next, call `configureWithPaymentIntent` with the Stripe object keys fetched from your backend and update your UI in the callback using [getPaymentOption()](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/-flow-controller/index.html#-2091462043%2FFunctions%2F2002900378). This contains an image and label representing the customer’s currently selected payment method.

#### Android (Kotlin)

```kotlin
flowController.configureWithPaymentIntent(
  paymentIntentClientSecret = paymentIntentClientSecret,
  configuration = PaymentSheet.Configuration.Builder("Example, Inc.")
    .customer(PaymentSheet.CustomerConfiguration(
      id = customerId,
      ephemeralKeySecret = ephemeralKeySecret
    ))
    .build()
) { isReady, error ->
  if (isReady) {
    // Update your UI using `flowController.getPaymentOption()`
  } else {
    // handle FlowController configuration failure
  }
}
```

1. Next, call [presentPaymentOptions](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/-flow-controller/index.html#449924733%2FFunctions%2F2002900378) to collect payment details. When the customer finishes, the sheet is dismissed and calls the [paymentOptionCallback](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-option-callback/index.html) passed earlier in `create`. Implement this method to update your UI with the returned `paymentOption`.

#### Android (Kotlin)

```kotlin
// ...
  flowController.presentPaymentOptions()
// ...
  private fun onPaymentOption(paymentOptionResult: PaymentOptionResult) {
    val paymentOption = paymentOptionResult.paymentOption
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

1. Finally, call [confirm](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/-flow-controller/index.html#-479056656%2FFunctions%2F2002900378) to complete the payment. When the customer finishes, the sheet is dismissed and calls the [paymentResultCallback](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet-result-callback/index.html#237248767%2FFunctions%2F2002900378) passed earlier in `create`.

#### Android (Kotlin)

```kotlin
  // ...
    flowController.confirmPayment()
  // ...

  private fun onPaymentSheetResult(
    paymentSheetResult: PaymentSheetResult
  ) {
    when (paymentSheetResult) {
      is PaymentSheetResult.Canceled -> {
        // Payment canceled
      }
      is PaymentSheetResult.Failed -> {
        // Payment Failed. See logcat for details or inspect paymentSheetResult.error
      }
      is PaymentSheetResult.Completed -> {
        // Payment Complete
      }
    }
  }
```

# React Native

> This is a React Native for when platform is react-native and mobile-ui is payment-element. View the full page at https://docs.stripe.com/payments/mobile/set-up-future-payments?platform=react-native&mobile-ui=payment-element.

The [Setup Intents API](https://docs.stripe.com/api/setup_intents.md) lets you save a customer’s payment details without an initial payment. This is helpful if you want to onboard customers now, set them up for payments, and charge them in the future—when they’re offline.

Use this integration to set up recurring payments or to create one-time payments with a final amount determined later, often after the customer receives your service.

> #### Card-present transactions
>
> Card-present transactions, such as collecting card details through Stripe Terminal, use a different process for saving the payment method. For details, see [the Terminal documentation](https://docs.stripe.com/terminal/features/saving-payment-details/save-directly.md).

## Compliance

You’re responsible for your compliance with all applicable laws, regulations, and network rules when saving a customer’s payment details. These requirements generally apply if you want to save your customer’s payment method for future use, such as displaying a customer’s payment method to them in the checkout flow for a future purchase or charging them when they’re not actively using your website or app. Add terms to your website or app that state how you plan to save payment method details and allow customers to opt in.

When you save a payment method, you can only use it for the specific usage you’ve included in your terms. To charge a payment method when a customer is offline and save it as an option for future purchases, make sure that you explicitly collect consent from the customer for this specific use. For example, include a “Save my payment method for future use” checkbox to collect consent.

To charge them when they’re offline, make sure your terms include the following:

- The customer’s agreement to your initiating a payment or a series of payments on their behalf for specified transactions.
- The anticipated timing and frequency of payments (for example, if the charges are for scheduled installments, subscription payments, or unscheduled top-ups).
- How you determine the payment amount.
- Your cancellation policy, if the payment method is for a subscription service.

Make sure you keep a record of your customer’s written agreement to these terms.

> If you need to use manual server-side confirmation or your integration requires presenting payment methods separately, see our [alternative guide](https://docs.stripe.com/payments/save-and-reuse-cards-only.md).
> ![](assets/ios-overview.9e0d68d009dc005f73a6f5df69e00458.png)

This integration combines all of the steps required to pay, including collecting payment details and confirming the payment, into a single sheet that displays on top of your app.

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

## Add an endpoint [Server-side]

> The mobile Payment Element only supports SetupIntents with cards, Link, and US bank accounts.

If your integration uses [customer-configured Accounts](https://docs.stripe.com/api/v2/core/accounts/create.md#v2_create_accounts-configuration-customer), replace `Customer` and event references in the code examples with the equivalent Accounts v2 API references. For more information, see [Represent customers with Account objects](https://docs.stripe.com/connect/use-accounts-as-customers.md).

This integration uses three Stripe API objects:

1. A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) is an object that represents your intent to set up a customer’s payment method for future payments. The payment methods shown to customers during the checkout process are also included on the SetupIntent. You can let Stripe automatically pull payment methods from your Dashboard settings or you can list them manually.

1. A _Customer_ (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments). To set up a payment method for future payments, it must be attached to a Customer. Create a Customer object when your customer creates an account with your business. If your customer is making a payment as a guest, you can create a Customer object before payment and associate it with your own internal representation of the customer’s account later.

1. A Customer Ephemeral Key (optional). Information on the Customer object is sensitive, and can’t be retrieved directly from an app. An Ephemeral Key grants the SDK temporary access to the Customer.

For security reasons, your app can’t create these objects. Instead, add an endpoint on your server that:

1. Retrieves the Customer, or creates a new one.
1. Creates an Ephemeral Key for the Customer.
1. Creates a SetupIntent with the Customer ID.
1. Returns the SetupIntent’s [client secret](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-client_secret), the Ephemeral Key’s `secret`, the Customer’s [ID](https://docs.stripe.com/api/customers/object.md#customer_object-id), and your [publishable key](https://dashboard.stripe.com/apikeys) to your app.

The payment methods shown to customers during the checkout process are also included on the SetupIntent. You can let Stripe automatically pull payment methods from your Dashboard settings or you can list them manually.

#### Manage payment methods from the Dashboard

You can manage payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods). Stripe handles the return of eligible payment methods based on factors such as the transaction’s amount, currency, and payment flow.

#### Accounts v2

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
// This example sets up an endpoint using the Express framework.

app.post("/payment-sheet", async (req, res) => {
  // Use an existing Account ID if this is a returning customer.
  const customerAccount = await stripe.v2.core.accounts.create({
    configuration: { customer: {} },
  });
  const ephemeralKey = await stripe.ephemeralKeys.create(
    { customer_account: customerAccount.id },
    {
      apiVersion: "2026-03-25.dahlia",
    },
  );
  const setupIntent = await stripe.setupIntents.create({
    customer_account: customerAccount.id,

    automatic_payment_methods: {
      enabled: true,
    },
  });
  res.json({
    setupIntent: setupIntent.client_secret,
    ephemeralKey: ephemeralKey.secret,
    customer_account: customerAccount.id,
    publishableKey: "<<YOUR_PUBLISHABLE_KEY>>",
  });
});
```

#### Customers v1

#### Node.js

```javascript

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');
// This example sets up an endpoint using the Express framework.

app.post('/payment-sheet', async (req, res) => {
  // Use an existing Customer ID if this is a returning customer.
  const customer = await stripe.customers.create(stripeAccount:'{{CONNECTED_ACCOUNT_ID}}');
  const ephemeralKey = await stripe.ephemeralKeys.create(
    {customer: customer.id},
    {
      stripeAccount: '{{CONNECTED_ACCOUNT_ID}}',
      apiVersion: '2026-03-25.dahlia'
    }
  );
  const setupIntent = await stripe.setupIntents.create({
    customer: customer.id,

    automatic_payment_methods: {
      enabled: true,
    },
  });
  res.json({
    setupIntent: setupIntent.client_secret,
    ephemeralKey: ephemeralKey.secret,
    customer: customer.id,
    publishableKey: '<<YOUR_PUBLISHABLE_KEY>>'
  })
});
```

#### Listing payment methods manually

> You can fork and deploy an implementation of this endpoint on [CodeSandbox](https://codesandbox.io/p/devbox/suspicious-lalande-l325w6) for testing.

#### Accounts v2

#### Node.js

```javascript
// This example sets up an endpoint using the Express framework.

app.post("/payment-sheet", async (req, res) => {
  // Use an existing Account ID if this is a returning customer.
  const customerAccount = await stripe.v2.core.accounts.create({
    configuration: { customer: {} },
  });
  const ephemeralKey = await stripe.ephemeralKeys.create(
    { customer_account: customerAccount.id },
    {
      apiVersion: "2026-03-25.dahlia",
    },
  );
  const setupIntent = await stripe.setupIntents.create({
    customer_account: customerAccount.id,
  });
  res.json({
    setupIntent: setupIntent.client_secret,
    ephemeralKey: ephemeralKey.secret,
    customer_account: customerAccount.id,
    publishableKey: "<<YOUR_PUBLISHABLE_KEY>>",
  });
});
```

#### Customers v1

#### Node.js

```javascript

// This example sets up an endpoint using the Express framework.

app.post('/payment-sheet', async (req, res) => {
  // Use an existing Customer ID if this is a returning customer.
  const customer = await stripe.customers.create(stripeAccount:'{{CONNECTED_ACCOUNT_ID}}');
  const ephemeralKey = await stripe.ephemeralKeys.create(
    {customer: customer.id},
    {
      stripeAccount: '{{CONNECTED_ACCOUNT_ID}}',
      apiVersion: '2026-03-25.dahlia'
    }
  );
  const setupIntent = await stripe.setupIntents.create({
    customer: customer.id,
  });
  res.json({
    setupIntent: setupIntent.client_secret,
    ephemeralKey: ephemeralKey.secret,
    customer: customer.id,
    publishableKey: '<<YOUR_PUBLISHABLE_KEY>>'
  })
});
```

## Collect payment details [Client-side]

This guide assumes your checkout has a **Set up** button. In the checkout of your app, make a network request to the backend endpoint you created in the previous step and call `initPaymentSheet` from the `useStripe` hook. To reduce loading time, make this request early, like when the screen loads.

```javascript
export default function CheckoutScreen() {
  const { initPaymentSheet, presentPaymentSheet } = useStripe();
  const [loading, setLoading] = useState(false);

  const fetchPaymentSheetParams = async () => {
    const response = await fetch(`${API_URL}/payment-sheet`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
    });
    const { setupIntent, ephemeralKey, customer } = await response.json();

    return {
      setupIntent,
      ephemeralKey,
      customer,
    };
  };

  const initializePaymentSheet = async () => {
    const { setupIntent, ephemeralKey, customer } =
      await fetchPaymentSheetParams();

    const { error } = await initPaymentSheet({
      merchantDisplayName: "Example, Inc.",
      customerId: customer,
      customerEphemeralKeySecret: ephemeralKey,
      setupIntentClientSecret: setupIntent,
    });
    if (!error) {
      setLoading(true);
    }
  };

  const openPaymentSheet = async () => {
    // see below
  };

  useEffect(() => {
    initializePaymentSheet();
  }, []);

  return (
    <Screen>
      <Button
        variant="primary"
        disabled={!loading}
        title="Set up"
        onPress={openPaymentSheet}
      />
    </Screen>
  );
}
```

When your customer taps the **Set up** button, call `presentPaymentSheet()` to open the sheet. After the customer completes setting up their payment method for future use, the sheet is dismissed and the promise resolves with an optional `StripeError<PaymentSheetError>`.

```javascript
export default function CheckoutScreen() {
  // continued from above

  const openPaymentSheet = async () => {
    const { error } = await presentPaymentSheet();

    if (error) {
      Alert.alert(`Error code: ${error.code}`, error.message);
    } else {
      Alert.alert(
        "Success",
        "Your payment method is successfully set up for future payments!",
      );
    }
  };

  return (
    <Screen>
      <Button
        variant="primary"
        disabled={!loading}
        title="Set up"
        onPress={openPaymentSheet}
      />
    </Screen>
  );
}
```

## Set up a return URL (iOS only) [Client-side]

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

## Charge the saved payment method later [Server-side]

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

| Payment method | Scenario                                                                                                                                                                                                                                                                                                        | How to test                                                                                                                 |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Credit card    | The card setup succeeds and doesn’t require _authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase). | Fill out the credit card form using the credit card number `4242 4242 4242 4242` with any expiration, CVC, and postal code. |
| Credit card    | The card requires authentication for the initial setup, then succeeds for subsequent payments.                                                                                                                                                                                                                  | Fill out the credit card form using the credit card number `4000 0025 0000 3155` with any expiration, CVC, and postal code. |
| Credit card    | The card requires authentication for the initial setup and also requires authentication for subsequent payments.                                                                                                                                                                                                | Fill out the credit card form using the credit card number `4000 0027 6000 3184` with any expiration, CVC, and postal code. |
| Credit card    | The card is declined during setup.                                                                                                                                                                                                                                                                              | Fill out the credit card form using the credit card number `4000 0000 0000 9995` with any expiration, CVC, and postal code. |

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

When you initialize `PaymentSheet`, set `merchantCountryCode` to the country code of your business, set `currencyCode`, and set `googlePay` to true.

You can also use the test environment by passing the `testEnv` parameter. You can only test Google Pay on a physical Android device. Follow the [React Native docs](https://reactnative.dev/docs/running-on-device) to test your application on a physical device.

```javascript
const { error, paymentOption } = await initPaymentSheet({
  // ...
  googlePay: {
    merchantCountryCode: "US",
    currencyCode: "USD", // currency must be specified for setup mode
    testEnv: true, // use test environment
  },
});
```

## Enable card scanning [Client-side]

> Enabling card scanning is required for Apple’s iOS app review process. Card scanning is not required for Android’s app review process, but we recommend enabling it.

### iOS

To enable card scanning support for iOS, set the `NSCameraUsageDescription` (**Privacy - Camera Usage Description**) in the `Info.plist` of your application, and provide a reason for accessing the camera (for example, “To scan cards”).

### (Optional) Android

To enable card scanning support, [request production access](https://developers.google.com/pay/api/android/guides/test-and-deploy/request-prod-access) to the Google Pay API from the [Google Pay and Wallet Console](https://pay.google.com/business/console?utm_source=devsite&utm_medium=devsite&utm_campaign=devsite).

- If you’ve enabled Google Pay, the card scanning feature is automatically available in our UI on eligible devices. To learn more about eligible devices, see the [Google Pay API constraints](https://developers.google.com/pay/payment-card-recognition/debit-credit-card-recognition)
- **Important:** The card scanning feature only appears in builds signed with the same signing key registered in the [Google Pay & Wallet Console](https://pay.google.com/business/console). Test or debug builds using different signing keys (for example, builds distributed through Firebase App Tester) won’t show the **Scan card** option. To test card scanning in pre-release builds, you must either:
  - Sign your test builds with your production signing key
  - Add your test signing key fingerprint to the Google Pay and Wallet Console

## Optional: Customize the sheet [Client-side]

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

## Optional: Complete payment in your UI

You can present Payment Sheet to only collect payment method details and then later call a `confirm` method to complete payment in your app’s UI. This is useful if you have a custom buy button or require additional steps after payment details are collected.
![](assets/react-native-multi-step.84d8a0a44b1baa596bda491322b6d9fd.png)

> A sample integration is [available on our GitHub](https://github.com/stripe/stripe-react-native/blob/master/example/src/screens/PaymentsUICustomScreen.tsx).

1. First, call `initPaymentSheet` and pass `customFlow: true`. `initPaymentSheet` resolves with an initial payment option containing an image and label representing the customer’s payment method. Update your UI with these details.

```javascript
const { initPaymentSheet, presentPaymentSheet, confirmPaymentSheetPayment } =
  useStripe();

const { error, paymentOption } = await initPaymentSheet({
  customerId: customer,
  customerEphemeralKeySecret: ephemeralKey,
  paymentIntentClientSecret: paymentIntent,
  customFlow: true,
  merchantDisplayName: "Example Inc.",
});
// Update your UI with paymentOption
```

1. Use `presentPaymentSheet` to collect payment details. When the customer finishes, the sheet dismisses itself and resolves the promise. Update your UI with the selected payment method details.

```javascript
const { error, paymentOption } = await presentPaymentSheet();
```

1. Use `confirmPaymentSheetPayment` to confirm the payment. This resolves with the result of the payment.

```javascript
const { error } = await confirmPaymentSheetPayment();

if (error) {
  Alert.alert(`Error code: ${error.code}`, error.message);
} else {
  Alert.alert("Success", "Your order is confirmed!");
}
```
