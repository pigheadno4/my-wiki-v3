<!-- Source URL: https://docs.stripe.com/payments/mobile/payment-method-settings-sheet -->
<!-- Fetched: 2026-04-22 -->

# Manage payment methods in settings

Use the Payment Method Settings Sheet to let your customers manage their payment methods in your app settings page.

> The Payment Method Settings Sheet is intended for use on an app settings page. For checkout and payments, use the [In-app Payments](https://docs.stripe.com/payments/mobile.md), which also has built-in support for saving and displaying payment methods and supports more payment methods than the Payment Method Settings Sheet.

> In code, this component is referenced as `CustomerSheet` for historical reasons. Throughout the documentation, when you see `CustomerSheet` in code examples, this refers to the Payment Method Settings Sheet.

The Payment Method Settings Sheet is a prebuilt UI component that lets your customers manage their saved payment methods. You can use the Payment Method Settings Sheet UI outside of a checkout flow, and the appearance and styling is customizable to match the appearance and aesthetic of your app. Customers can add and remove payment methods, which get saved to the customer object, and set their default payment method stored locally on the device. Use both the In-app Payments and the Payment Method Settings Sheet to provide customers a consistent end-to-end solution for saved payment methods.
![Screenshot of Payment Method Settings Sheet presenting multiple saved payment methods in an iOS app.](assets/stripe-inapp-customer-sheet-landing.png)

The [CustomerSession](https://docs.stripe.com/api/customer_sessions.md) object grants the SDK temporary access to the Customer and provides additional configuration options. These configuration options allow you to customize the behavior of CustomerSheet. A complete list of features exposed on the CustomerSession are in our [API docs](https://docs.stripe.com/api/customer_sessions/create.md#create_customer_session-components).

## Set up Stripe

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

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

Configure the SDK with your Stripe [publishable key](https://dashboard.stripe.com/test/apikeys) on app start. This enables your app to make requests to the Stripe API.

#### Swift

```swift
import UIKitimportStripePaymentSheet

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {StripeAPI.defaultPublishableKey = "<<YOUR_PUBLISHABLE_KEY>>"
        // do any other necessary launch configuration
        return true
    }
}
```

> Use your [test keys](https://docs.stripe.com/keys.md#obtain-api-keys) while you test and develop, and your [live mode](https://docs.stripe.com/keys.md#test-live-modes) keys when you publish your app.

## Enable payment methods

View your [payment methods settings](https://dashboard.stripe.com/settings/payment_methods) and enable the payment methods you want to support. You need at least one payment method enabled to create a _SetupIntent_ (The Setup Intents API lets you build dynamic flows for collecting payment method details for future payments. It tracks the lifecycle of a payment setup flow and can trigger additional authentication steps if required by law or by the payment method).

By default, Stripe enables cards and other prevalent payment methods that can help you reach more customers, but we recommend turning on additional payment methods that are relevant for your business and customers. See [Payment method support](https://docs.stripe.com/payments/payment-methods/payment-method-support.md) for product and payment method support, and our [pricing page](https://stripe.com/pricing/local-payment-methods) for fees.

> CustomerSheet only supports cards, US bank accounts, and SEPA Direct Debit.

## Add Customer endpoints [Server-side]

If your integration uses [customer-configured Accounts](https://docs.stripe.com/api/v2/core/accounts/create.md#v2_create_accounts-configuration-customer), replace `Customer` and event references in the code examples with the equivalent Accounts v2 API references. For more information, see [Represent customers with Account objects](https://docs.stripe.com/connect/use-accounts-as-customers.md).

Create two endpoints on your server: one for fetching a CustomerSession client secret, and one to create a [SetupIntent](https://docs.stripe.com/api/setup_intents.md) for saving a new payment method to the [Customer](https://docs.stripe.com/api/customers.md).

1. Create an endpoint to return a [Customer](https://docs.stripe.com/api/customers.md) ID and a [CustomerSession](https://docs.stripe.com/api/customer_sessions.md) client secret.

#### Node.js

```javascript
app.post("/customer", async (req, res) => {
  // Use an existing Customer ID if this is a returning customer.
  const customer = await stripe.customers.create();

  const customerSession = await stripe.customerSessions.create({
    customer: customer.id,
    components: {
      customer_sheet: {
        enabled: true,
        features: {
          payment_method_remove: "enabled",
        },
      },
    },
  });

  res.json({
    customer: customer.id,
    customerSessionClientSecret: customerSession.client_secret,
  });
});
```

> Integrations with legacy customer ephemeral keys results in saved payment methods having an `allow_redisplay` value of `unspecified`. To display these payment methods in addition to payment methods saved while using Customer Sessions, set `payment_method_allow_redisplay_filters` to `["unspecified", "always"]`. For more information, see [CustomerSessions](https://docs.stripe.com/api/customer_sessions.md).

1. Create an endpoint to return a [SetupIntent](https://docs.stripe.com/api/setup_intents.md) configured with the [Customer](https://docs.stripe.com/api/customers.md) ID.

#### Node.js

```javascript
app.post('/create-setup-intent', async (req, res) => {
  // Use existing Customer
  const customer = {{EXISTING_CUSTOMER}}
  const setupIntent = await stripe.setupIntents.create({
    customer: customer.id,
  });
  res.json({
    setupIntent: setupIntent.client_secret
  })
});
```

If you only plan to use the payment method for future payments when your customer is present during the checkout flow, set the [usage](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-usage) parameter to _on_session_ (A payment is described as on-session if it occurs while the customer is actively in your checkout flow and able to authenticate the payment method) to improve authorization rates.

## Configure the sheet

Next, configure the Payment Method Settings Sheet using the `CustomerSheet` class with an `IntentConfiguration`, `CustomerSessionClientSecretProvider` and a [CustomerSheet.Configuration](https://stripe.dev/stripe-ios/stripepaymentsheet/documentation/stripepaymentsheet/customersheet/configuration/).

```swift
var configuration = CustomerSheet.Configuration()

// Configure settings for the CustomerSheet here. For example:
configuration.headerTextForSelectionScreen = "Manage your payment method"

let intentConfiguration = CustomerSheet.IntentConfiguration(setupIntentClientSecretProvider: {
  let json = try await myBackend.createSetupIntent()
  return json["setupIntentClientSecret"]!
})

let customerSheet = CustomerSheet(
      configuration: configuration,
      intentConfiguration: intentConfiguration,
      customerSessionClientSecretProvider: {
        let json = try await myBackend.createCustomerSessionClientSecret()
        return .init(customerId: json["customerId"]!, clientSecret: json["customerSessionClientSecret"]!)
      })
```

## Present the sheet

#### UIKit

Present the Payment Method Settings Sheet using `CustomerSheet`. When the customer dismisses the sheet, the `CustomerSheet` calls the completion block with a `CustomerSheet.SheetResult`.

#### iOS (Swift)

```swift
import StripePaymentSheet

customerSheet.present(from: self, completion: { result in
  switch result {
  case .canceled(let paymentOption), .selected(let paymentOption):
    // Configure your UI based on the payment option
    self.paymentLabel.text = paymentOption?.displayData().label ?? "None"

    // Optional: Send the selected payment method ID to your backend for advanced use cases
    // like charging a customer when not present in your app
    if let paymentOption = paymentOption {
      switch paymentOption {
      case .paymentMethod(let paymentMethod, let paymentOptionDisplayData):
        MyBackend.setDefaultPaymentMethod(paymentMethod.stripeId)
      case .applePay(paymentOptionDisplayData: let paymentOptionDisplayData):
        MyBackend.setDefaultPaymentMethodIsApplePay()
      }
    }
  case .error(let error):
    // Show the error in your UI
  }
})
```

- If the customer selects a payment method, the result is `.selected(PaymentOptionSelection?)`. The associated value is the selected [PaymentOptionSelection](https://stripe.dev/stripe-ios/stripepaymentsheet/documentation/stripepaymentsheet/customersheet/paymentoptionselection), or `nil` if the user deleted the previously-selected payment method. You can find the full payment method details in the PaymentOptionSelection’s `paymentMethod` associated value.
- If the user cancels the sheet, the result is `.canceled`. The associated value is the original payment method selected prior to opening the customer sheet, as long as that payment method is still available.
- If an error occurs, the result is `.error(Error)`.

Learn more about how to [enable Apple Pay](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=mobile&platform=ios#ios-apple-pay).

#### SwiftUI

Create an `ObservableObject` model for your screen presenting the Payment Method Settings Sheet. This model maintains an instance to the [CustomerSheet](https://stripe.dev/stripe-ios/stripepaymentsheet/documentation/stripepaymentsheet/customersheet).

```swift
import StripePaymentSheet
import SwiftUI

class YourAccountViewModel: ObservableObject {
  var customerSheet: CustomerSheet
}
```

Use the `.customerSheet` ViewModifier to present the Payment Method Settings Sheet.

```swift
struct YourAccountView: View {
    @State private var showingCustomerSheet = false
    @ObservedObject var model = YourAccountViewModel()
    var body: some View {
        VStack {
            Button(action: {
                showingCustomerSheet = true
            }) {
                Text("Present Customer Sheet")
            }.customerSheet(
                isPresented: $showingCustomerSheet,
                customerSheet: model.customerSheet,
                onCompletion: model.onCompletion)
        }
    }
}
```

Add a `customerSheetResult` to store the result of presenting the Payment Method Settings Sheet in your `ObservableObject`.

```swift
class YourAccountViewModel: ObservableObject {
  var customerSheet: CustomerSheet
@Published var customerSheetResult: CustomerSheet.CustomerSheetResult?

  func onCompletion(result: CustomerSheet.CustomerSheetResult) {
    self.customerSheetResult = result
  }
}
```

Use the `customerSheetResult` to render the selected payment method in your UI:

```swift
struct YourAccountView: View {
    @State private var showingCustomerSheet = false
    @ObservedObject var model = MyBackendCustomerSheetModel()
    var body: some View {
        VStack {
            Button(action: {
                showingCustomerSheet = true
            }) {
                Text("Present Customer Sheet")
            }.customerSheet(
                isPresented: $showingCustomerSheet,
                customerSheet: model.customerSheet,
                onCompletion: model.onCompletion)if let customerSheetResult = model.customerSheetResult {
                ExampleCustomerSheetPaymentMethodView(customerSheetResult: customerSheetResult)
            }
        }
    }
}
```

- If the customer selects a payment method, the result is `.selected(PaymentOptionSelection?)`. The associated value is the selected [PaymentOptionSelection](https://stripe.dev/stripe-ios/stripepaymentsheet/documentation/stripepaymentsheet/customersheet/paymentoptionselection), or `nil` if the user deleted the previously-selected payment method. You can find the full payment method details in the PaymentOptionSelection’s `paymentMethod` associated value.
- If the user cancels the sheet, the result is `.canceled`. The selected payment method didn’t change.
- If an error occurs, the result is `.error(Error)`.

Learn more about how to [enable Apple Pay](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=mobile&platform=ios#ios-apple-pay).

## Optional: Enable ACH payments

To enable ACH debit payments:

1. Include `StripeFinancialConnections` as a dependency for your app.
1. Enable US Bank Account as a payment method in the settings section of the [Dashboard](https://dashboard.stripe.com/settings/payment_methods).

## Optional: Fetch the selected payment method

To fetch the default payment method without presenting the Payment Method Settings Sheet, call `retrievePaymentOptionSelection()` on the `CustomerSheet`.

```swift
let paymentMethodOption = try await customerSheet.retrievePaymentOptionSelection()

// Configure your UI based on the payment option
self.paymentLabel.text = paymentMethodOption?.displayData().label ?? "None"

// Send the selected payment method ID to your backend
switch paymentMethodOption {
case .paymentMethod(paymentMethod: let paymentMethod, paymentOptionDisplayData: let paymentOptionDisplayData):
    try await MyBackend.setDefaultPaymentMethod(paymentMethod.stripeId)
case .applePay(paymentOptionDisplayData: let paymentOptionDisplayData):
    try await MyBackend.setDefaultPaymentMethodIsApplePay()
}
```

## Optional: Customize the sheet

### Appearance

Customize the colors, fonts, and other appearance attributes to match the look and feel of your app by using the [appearance API](https://docs.stripe.com/elements/appearance-api/mobile.md?platform=ios).

> `fetchPaymentMethods` can filter out saved payment methods from being shown, but won’t impact the type of payment methods that are addable.

### Default billing details

To set default values for billing details collected in the payment sheet, configure the `defaultBillingDetails` property. The `CustomerSheet` pre-populates its fields with the values that you provide.

```swift
var configuration = CustomerSheet.Configuration()
configuration.defaultBillingDetails.address.country = "US"
configuration.defaultBillingDetails.email = "foo@bar.com"
```

### Billing details collection

Use `billingDetailsCollectionConfiguration` to specify how you want to collect billing details in the payment sheet.

You can collect your customer’s name, email, phone number, and address.

To attach values that aren’t collected by `CustomerSheet`, add them to the `defaultBillingDetails` property and set `billingDetailsCollectionConfiguration.attachDefaultsToPaymentMethod` to `true`. Make sure that you complete this step if you don’t plan to collect values required by the payment method.

```swift
var configuration = CustomerSheet.Configuration()
configuration.defaultBillingDetails.email = "foo@bar.com"
configuration.billingDetailsCollectionConfiguration.name = .always
configuration.billingDetailsCollectionConfiguration.email = .never
configuration.billingDetailsCollectionConfiguration.address = .full
configuration.billingDetailsCollectionConfiguration.attachDefaultsToPaymentMethod = true
```

> Consult with your legal team regarding laws that apply to collecting information. Only collect phone numbers if you need them for the transaction.

> The Payment Method Settings Sheet is intended for use on an app settings page. For checkout and payments, use the [In-app Payments](https://docs.stripe.com/payments/mobile.md), which also has built-in support for saving and displaying payment methods and supports more payment methods than the Payment Method Settings Sheet.

> In code, this component is referenced as `CustomerSheet` for historical reasons. Throughout the documentation, when you see `CustomerSheet` in code examples, this refers to the Payment Method Settings Sheet.

The Payment Method Settings Sheet is a prebuilt UI component that lets your customers manage their saved payment methods. You can use the Payment Method Settings Sheet UI outside of a checkout flow, and the appearance and styling is customizable to match the appearance and aesthetic of your app. Customers can add and remove payment methods, which get saved to the customer object, and set their default payment method stored locally on the device. Use both the In-app Payments and the Payment Method Settings Sheet to provide customers a consistent end-to-end solution for saved payment methods.
![Screenshot of Payment Method Settings Sheet presenting multiple saved payment methods in an Android app.](assets/stripe-inapp-customer-sheet-landing.png)

The [CustomerSession](https://docs.stripe.com/api/customer_sessions.md) object grants the SDK temporary access to the Customer and provides additional configuration options. These configuration options allow you to customize the behavior of `CustomerSheet`. A complete list of features exposed on the `CustomerSession` are in our [API docs](https://docs.stripe.com/api/customer_sessions/create.md#create_customer_session-components).

## Set up Stripe

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

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

## Enable payment methods

View your [payment methods settings](https://dashboard.stripe.com/settings/payment_methods) and enable the payment methods you want to support. You need at least one payment method enabled to create a _SetupIntent_ (The Setup Intents API lets you build dynamic flows for collecting payment method details for future payments. It tracks the lifecycle of a payment setup flow and can trigger additional authentication steps if required by law or by the payment method).

By default, Stripe enables cards and other prevalent payment methods that can help you reach more customers, but we recommend turning on additional payment methods that are relevant for your business and customers. See [Payment method support](https://docs.stripe.com/payments/payment-methods/payment-method-support.md) for product and payment method support, and our [pricing page](https://stripe.com/pricing/local-payment-methods) for fees.

> At this time, Payment Method Settings Sheet only supports cards and US bank accounts.

## Add Customer endpoints [Server-side]

If your integration uses [customer-configured Accounts](https://docs.stripe.com/api/v2/core/accounts/create.md#v2_create_accounts-configuration-customer), replace `Customer` and event references in the code examples with the equivalent Accounts v2 API references. For more information, see [Represent customers with Account objects](https://docs.stripe.com/connect/use-accounts-as-customers.md).

Create two endpoints on your server: one for fetching a CustomerSession client secret, and one to create a [SetupIntent](https://docs.stripe.com/api/setup_intents.md) for saving a new payment method to the [Customer](https://docs.stripe.com/api/customers.md).

1. Create an endpoint to return a [Customer](https://docs.stripe.com/api/customers.md) ID and a [CustomerSession](https://docs.stripe.com/api/customer_sessions.md) client secret.

#### Node.js

```javascript
app.post("/customer", async (req, res) => {
  // Use an existing Customer ID if this is a returning customer.
  const customer = await stripe.customers.create();

  const customerSession = await stripe.customerSessions.create({
    customer: customer.id,
    components: {
      customer_sheet: {
        enabled: true,
        features: {
          payment_method_remove: "enabled",
        },
      },
    },
  });

  res.json({
    customer: customer.id,
    customerSessionClientSecret: customerSession.client_secret,
  });
});
```

> Integrations with legacy customer ephemeral keys results in saved payment methods having an `allow_redisplay` value of `unspecified`. To display these payment methods in addition to payment methods saved while using Customer Sessions, set `payment_method_allow_redisplay_filters` to `["unspecified", "always"]`. For more information, see [CustomerSessions](https://docs.stripe.com/api/customer_sessions.md).

1. Create an endpoint to return a [SetupIntent](https://docs.stripe.com/api/setup_intents.md) configured with the [Customer](https://docs.stripe.com/api/customers.md) ID.

#### Node.js

```javascript
app.post('/create-setup-intent', async (req, res) => {
  // Use existing Customer
  const customer = {{EXISTING_CUSTOMER}}
  const setupIntent = await stripe.setupIntents.create({
    customer: customer.id,
  });
  res.json({
    setupIntent: setupIntent.client_secret
  })
});
```

If you only plan to use the payment method for future payments when your customer is present during the checkout flow, set the [usage](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-usage) parameter to _on_session_ (A payment is described as on-session if it occurs while the customer is actively in your checkout flow and able to authenticate the payment method) to improve authorization rates.

## Create a Customer session provider [Client-side]

A `CustomerSessionProvider` enables a `CustomerSheet` to communicate with Stripe using [CustomerSession](https://docs.stripe.com/api/customer_sessions.md) objects. On the client, create a `CustomerSessionProvider` that can create a `CustomerSession` client secret and a `SetupIntent` client secret from your server.

```kotlin
import com.stripe.android.customersheet.CustomerSheet
import com.stripe.android.customersheet.ExperimentalCustomerSheetApi

@OptIn(ExperimentalCustomerSheetApi::class)
class MyCustomerSessionProvider : CustomerSheet.CustomerSessionProvider() {
    val myBackend = // ....

    override suspend fun providesCustomerSessionClientSecret(): Result<CustomerSheet.CustomerSessionClientSecret> {
        return myBackend.getCustomerSessionClientSecret().fold(
            onSuccess = { response ->
                Result.success(
                    CustomerSessionClientSecret.create(
                        customerId = response.customerId,
                        clientSecret = response.customerSessionClientSecret,
                    )
                )
            },
            onFailure = { exception ->
                Result.failure(exception)
            }
        )
    }

    override suspend fun provideSetupIntentClientSecret(customerId: String): Result<String> {
        return myBackend.getSetupIntentClientSecret(customerId).fold(
            onSuccess = { response ->
                Result.success(response.setupIntentClientSecret)
            },
            onFailure = { exception ->
                Result.failure(exception)
            }
        )
    }
}
```

```kotlin
import android.app.Application
import androidx.lifecycle.AndroidViewModel

class CheckoutViewModel(
    application: Application
) : AndroidViewModel(application) {
    val customerSessionProvider = MyCustomerSessionProvider()
}
```

## Configure the sheet

Next, initialize the Payment Method Settings Sheet using the `CustomerSheet` class with your `CustomerSessionProvider` then call `configure` with a [CustomerSheet.Configuration](https://github.com/stripe/stripe-android/blob/master/paymentsheet/src/main/java/com/stripe/android/customersheet/CustomerSheet.kt). Always call `configure` before calling `present` and `retrievePaymentOptionSelection`.

```kotlin
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.viewModels
import com.stripe.android.customersheet.CustomerSheet
import com.stripe.android.customersheet.ExperimentalCustomerSheetApi
import com.stripe.android.customersheet.rememberCustomerSheet

@OptIn(ExperimentalCustomerSheetApi::class)
class CheckoutActivity : ComponentActivity() {
    private val viewModel by viewModels<CheckoutViewModel>()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val configuration = CustomerSheet.Configuration.builder(merchantDisplayName = "{{YOUR BUSINESS NAME}}")
            .build()

        setContent {
            val customerSheet = rememberCustomerSheet(
                customerSessionProvider = viewModel.customerSessionProvider,
                callback = viewModel::handleResult // Implemented in next step
            )

            LaunchedEffect(customerSheet) {
                customerSheet.configure(configuration = configuration)
            }
        }
    }
}
```

## Present the sheet

Present the Payment Method Settings Sheet using `CustomerSheet`. When the customer dismisses the sheet, the `CustomerSheet` calls the completion block with a `CustomerSheetResult`.

```kotlin
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.viewModelsimport androidx.compose.foundation.Image
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.material.Text
import androidx.compose.material.TextButton
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.stripe.android.customersheet.CustomerSheet
import com.stripe.android.customersheet.ExperimentalCustomerSheetApi
import com.stripe.android.customersheet.rememberCustomerSheetimport com.stripe.android.uicore.image.rememberDrawablePainter

@OptIn(ExperimentalCustomerSheetApi::class)
class CheckoutActivity : ComponentActivity() {private val viewModel by viewModels<CheckoutViewModel>()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val configuration = CustomerSheet.Configuration.builder(merchantDisplayName = "{{YOUR BUSINESS NAME}}")
            .headerTextForSelectionScreen("Manage your payment method")
            .build()

        setContent {
            val customerSheet = rememberCustomerSheet(
                customerSessionProvider = viewModel.customerSessionProvider,
                callback = viewModel::handleResult
            )

            LaunchedEffect(customerSheet) {
                customerSheet.configure(configuration = configuration)viewModel.handleResult(customerSheet.retrievePaymentOptionSelection())
            }val paymentOption by viewModel.paymentOption.collectAsState()

            Row(
                modifier = Modifier.fillMaxWidth(),
                verticalAlignment = Alignment.CenterVertically,
                horizontalArrangement = Arrangement.SpaceBetween,
            ) {
                val icon = paymentOption?.icon()

                if (icon != null) {
                    Image(
                        painter = rememberDrawablePainter(
                            drawable = icon
                        ),
                        contentDescription = "Payment Method Icon",
                        modifier = Modifier.height(32.dp)
                    )
                }
                TextButton(
                    onClick = {
                        customerSheet.present()
                    }
                ) {
                    Text(
                        text = paymentOption?.label ?: "Select"
                    )
                }
            }
        }
    }
}
```

```kotlin
import android.app.Application
import androidx.lifecycle.AndroidViewModel
import com.stripe.android.customersheet.ExperimentalCustomerSheetApiimport com.stripe.android.paymentsheet.model.PaymentOption
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.update

@OptIn(ExperimentalCustomerSheetApi::class)
class CheckoutViewModel(
    application: Application
) : AndroidViewModel(application) {
    val customerSessionProvider = // ...
private val _paymentOption = MutableStateFlow<PaymentOption?>(null)
    val paymentOption: StateFlow<PaymentOption?> = _paymentOption

    fun handleResult(result: CustomerSheetResult) {
        when (result) {
            is CustomerSheetResult.Selected -> {
                // Configure your UI based on the payment option
                _paymentOption.update {
                    result.selection?.paymentOption
                }
            }
            is CustomerSheetResult.Canceled -> {
                // Configure your UI based on the payment option
                _paymentOption.update {
                    result.selection?.paymentOption
                }
            }
            is CustomerSheetResult.Failed -> {
                // Show the error in your UI
            }
        }
    }
}
```

- If the customer selects a payment method, the result is `CustomerSheetResult.Selected`. The associated value is the selected `PaymentOptionSelection`, or null if the user deleted the previously-selected payment method. The full payment method details are available in the `PaymentOptionSelection`’s `paymentMethod` value.
- If the customer cancels the sheet, the result is `CustomerSheetResult.Canceled`. The associated value is the customer’s original `PaymentOptionSelection`, or null if the customer hasn’t selected a payment method before or has deleted the originally selected payment method.
- If an error occurs, the result is `CustomerSheetResult.Failed`.

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

To add Google Pay to your integration, pass `true` to [googlePayEnabled](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.customersheet/-customer-sheet/-configuration/-builder/google-pay-enabled.html) when initializing [CustomerSheet.Configuration](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.customersheet/-customer-sheet/-configuration/index.html) with [CustomerSheet.Configuration.Builder](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.customersheet/-customer-sheet/-configuration/-builder/index.html).

#### Kotlin

```kotlin
val configuration = CustomerSheet.Configuration.Builder()
  .googlePayEnabled(true)
  .build()
```

## Optional: Enable ACH payments

To enable ACH debit payments include Financial Connections as a dependency for your app.

The [Stripe Android SDK](https://github.com/stripe/stripe-android) is open source and [fully documented](https://stripe.dev/stripe-android/).

To install the SDK, add `financial-connections` to the `dependencies` block of your [app/build.gradle](https://developer.android.com/studio/build/dependencies) file:

#### Kotlin

```kotlin
plugins {
    id("com.android.application")
}

android { ... }

dependencies {
  // ...

  // Financial Connections Android SDK
  implementation("com.stripe:financial-connections:23.5.0")
}
```

> For details on the latest SDK release and past versions, see the [Releases](https://github.com/stripe/stripe-android/releases) page on GitHub. To receive notifications when a new release is published, [watch releases for the repository](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/configuring-notifications#configuring-your-watch-settings-for-an-individual-repository).

## Optional: Fetch the selected payment method

To fetch the default payment method without presenting the Payment Method Settings Sheet, call `retrievePaymentOptionSelection()` on `CustomerSheet`.

```kotlin
class CheckoutActivity : ComponentActivity() {
    private val viewModel by viewModels<CheckoutViewModel>()
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val configuration = ...
        setContent {
            val customerSheet = ...

            LaunchedEffect(Unit) {
                customerSheet.configure(configuration = configuration)
                val result = customerSheet.retrievePaymentOptionSelection()
                viewModel.handleResult(result)
            }

            ...
        }
    }
}
```

## Optional: Customize the sheet

### Appearance

Customize the colors, fonts, and other appearance attributes to match the look and feel of your app by using the [appearance API](https://docs.stripe.com/elements/appearance-api/mobile.md?platform=android).

> `retrievePaymentMethods` can filter out saved payment methods from being shown, but won’t impact the type of payment methods that are addable.

### Default billing details

To set default values for billing details collected in the customer sheet, configure the [defaultBillingDetails](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.customersheet/-customer-sheet/-configuration/-builder/index.html#-1446247975%2FFunctions%2F2002900378) property. The `CustomerSheet` pre-populates its fields with the values that you provide.

```kotlin
val configuration = CustomerSheet.Configuration.Builder()
    .defaultBillingDetails(
       PaymentSheet.BillingDetails(
         address = PaymentSheet.Address(
           country = "US"
         ),
         email = "foo@bar.com"
      )
    )
    .build()
```

### Billing details collection

Use [billingDetailsCollectionConfiguration](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.customersheet/-customer-sheet/-configuration/-builder/index.html#1512634376%2FFunctions%2F2002900378) to specify how you want to collect billing details in the payment sheet.

You can collect your customer’s name, email, phone number, and address.

To attach values that aren’t collected by `CustomerSheet`, add them to the [defaultBillingDetails](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.customersheet/-customer-sheet/-configuration/-builder/index.html#-1446247975%2FFunctions%2F2002900378) property and set `billingDetailsCollectionConfiguration.attachDefaultsToPaymentMethod` to `true`. Make sure that you complete this step if you don’t plan to collect values required by the payment method.

```kotlin
val configuration = CustomerSheet.Configuration.Builder()
    .defaultBillingDetails(
       PaymentSheet.BillingDetails(
           email = "foo@bar.com"
       )
    )
    .billingDetailsCollectionConfiguration(
        PaymentSheet.BillingDetailsCollectionConfiguration(
            name = PaymentSheet.BillingDetailsCollectionConfiguration.AddressCollectionMode.Always,
            email = PaymentSheet.BillingDetailsCollectionConfiguration.AddressCollectionMode.Never,
            address = PaymentSheet.BillingDetailsCollectionConfiguration.AddressCollectionMode.Full,
            attachDefaultsToPaymentMethod = true,
        )
    )
    .build()
```

> Consult with your legal team regarding laws that apply to you collecting information. Only collect phone numbers if you need them for the transaction.

> The Payment Method Settings Sheet is intended for use on an app settings page. For checkout and payments, use the [In-app Payments](https://docs.stripe.com/payments/mobile.md), which also has built-in support for saving and displaying payment methods and supports more payment methods than the Payment Method Settings Sheet.

> In code, this component is referenced as `CustomerSheet` for historical reasons. Throughout the documentation, when you see `CustomerSheet` in code examples, this refers to the Payment Method Settings Sheet.

The Payment Method Settings Sheet is a prebuilt UI component that lets your customers manage their saved payment methods. You can use the Payment Method Settings Sheet UI outside of a checkout flow, and the appearance and styling is customizable to match the appearance and aesthetic of your app. Customers can add and remove payment methods, which get saved to the customer object, and set their default payment method stored locally on the device. Use both the In-app Payments and the Payment Method Settings Sheet to provide customers a consistent end-to-end solution for saved payment methods.
![Screenshot of Payment Method Settings Sheet presenting multiple saved payment methods in an iOS app.](assets/stripe-inapp-customer-sheet-landing.png)

## Set up Stripe

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

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

View your [payment methods settings](https://dashboard.stripe.com/settings/payment_methods) and enable the payment methods you want to support. You need at least one payment method enabled to create a _SetupIntent_ (The Setup Intents API lets you build dynamic flows for collecting payment method details for future payments. It tracks the lifecycle of a payment setup flow and can trigger additional authentication steps if required by law or by the payment method).

By default, Stripe enables cards and other prevalent payment methods that can help you reach more customers, but we recommend turning on additional payment methods that are relevant for your business and customers. See [Payment method support](https://docs.stripe.com/payments/payment-methods/payment-method-support.md) for product and payment method support, and our [pricing page](https://stripe.com/pricing/local-payment-methods) for fees.

> CustomerSheet only supports cards and US bank accounts.

## Add Customer endpoints [Server-side]

If your integration uses [customer-configured Accounts](https://docs.stripe.com/api/v2/core/accounts/create.md#v2_create_accounts-configuration-customer), replace `Customer` and event references in the code examples with the equivalent Accounts v2 API references. For more information, see [Represent customers with Account objects](https://docs.stripe.com/connect/use-accounts-as-customers.md).

Create two endpoints on your server: one for fetching a CustomerSession client secret, and one to create a [SetupIntent](https://docs.stripe.com/api/setup_intents.md) for saving a new payment method to the [Customer](https://docs.stripe.com/api/customers.md).

1. Create an endpoint to return a [Customer](https://docs.stripe.com/api/customers.md) ID and a [CustomerSession](https://docs.stripe.com/api/customer_sessions.md) client secret.

#### Node.js

```javascript
app.post("/customer", async (req, res) => {
  // Use an existing Customer ID if this is a returning customer.
  const customer = await stripe.customers.create();

  const customerSession = await stripe.customerSessions.create({
    customer: customer.id,
    components: {
      customer_sheet: {
        enabled: true,
        features: {
          payment_method_remove: "enabled",
        },
      },
    },
  });

  res.json({
    customer: customer.id,
    customerSessionClientSecret: customerSession.client_secret,
  });
});
```

> Integrations with legacy customer ephemeral keys results in saved payment methods having an `allow_redisplay` value of `unspecified`. To display these payment methods in addition to payment methods saved while using Customer Sessions, set `payment_method_allow_redisplay_filters` to `["unspecified", "always"]`. For more information, see [CustomerSessions](https://docs.stripe.com/api/customer_sessions.md).

1. Create an endpoint to return a [SetupIntent](https://docs.stripe.com/api/setup_intents.md) configured with the [Customer](https://docs.stripe.com/api/customers.md) ID.

#### Node.js

```javascript
app.post('/create-setup-intent', async (req, res) => {
  // Use existing Customer
  const customer = {{EXISTING_CUSTOMER}}
  const setupIntent = await stripe.setupIntents.create({
    customer: customer.id,
  });
  res.json({
    setupIntent: setupIntent.client_secret
  })
});
```

If you only plan to use the payment method for future payments when your customer is present during the checkout flow, set the [usage](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-usage) parameter to _on_session_ (A payment is described as on-session if it occurs while the customer is actively in your checkout flow and able to authenticate the payment method) to improve authorization rates.

## Initialize the sheet

Create a `ClientSecretProvider` object that implements two methods. `CustomerSheet` needs it to communicate with Stripe using `CustomerSession` objects and the endpoints you created earlier.

```jsx
import {ClientSecretProvider, CustomerSessionClientSecret} from '@stripe/stripe-react-native';

const clientSecretProvider: ClientSecretProvider = {
  // Must return an object with customerId and clientSecret
  async provideCustomerSessionClientSecret(): Promise<CustomerSessionClientSecret> {
    const result = await MyBackend.createCustomerSession();
    return {
      customerId: result.customer,
      clientSecret: result.customerSessionClientSecret,
    };
  },

  // Must return a string
  async provideSetupIntentClientSecret(): Promise<string> {
    const result = await MyBackend.createSetupIntent();
    return result.setupIntent;
  }
};
```

Next, configure the Payment Method Settings Sheet using the `CustomerSheet` class, by providing your desired settings to `CustomerSheet.initialize`.

```jsx
import { CustomerSheet } from "@stripe/stripe-react-native";

const { error } = await CustomerSheet.initialize({
  // You must provide intentConfiguration and clientSecretProvider
  intentConfiguration: {
    paymentMethodTypes: ["card"],
  },
  clientSecretProvider: clientSecretProvider,
  headerTextForSelectionScreen: "Manage your payment method",
  returnURL: "my-return-url://",
});
```

## Present the sheet

#### Functional

Present the Payment Method Settings Sheet using `CustomerSheet`. When the customer dismisses the sheet, the promise resolves with a `CustomerSheetResult`.

#### Using functions directly

```jsx
import { CustomerSheet } from "@stripe/stripe-react-native";

const { error, paymentOption, paymentMethod } = await CustomerSheet.present();
if (error) {
  if (error.code === CustomerSheetError.Canceled) {
    // Customer dismissed the sheet without changing their payment option
  } else {
    // Show the error in your UI
  }
} else {
  if (paymentOption) {
    // Configure your UI based on the payment option
    MyBackend.setDefaultPaymentMethod(paymentMethod.id);
  }
  if (paymentMethod) {
    console.log(JSON.stringify(paymentMethod, null, 2));
  }
}
```

- If the customer selects a payment method, the result contains a `paymentOption`. The associated value is the selected [PaymentOption](https://stripe.dev/stripe-react-native/api-reference/interfaces/PaymentSheet.PaymentOption.html), or `nil` if the user deleted the previously-selected payment method. You can find the full payment method details in the `paymentMethod` field.
- If the user cancels the sheet, the result contains an `error` with the `error.code === CustomerSheetError.Canceled`. The selected payment method doesn’t change.
- If an error occurs, the details are included in `error`.

Learn more about how to [enable Apple Pay](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=mobile&platform=ios#ios-apple-pay).

#### Component

Create a state variable to control presentation of the Payment Method Settings Sheet (`CustomerSheet`).

```jsx
import {CustomerSheet, ClientSecretProvider, CustomerSessionClientSecret} from '@stripe/stripe-react-native';

export default function MyScreen() {
  const [customerSheetVisible, setCustomerSheetVisible] = React.useState(false);

  const clientSecretProvider: ClientSecretProvider = {
    async provideCustomerSessionClientSecret(): Promise<CustomerSessionClientSecret> {
      const result = await MyBackend.createCustomerSession();
      return {
        customerId: result.customer,
        clientSecret: result.customerSessionClientSecret,
      };
    },
    async provideSetupIntentClientSecret(): Promise<string> {
      const result = await MyBackend.createSetupIntent();
      return result.setupIntent;
    }
  };

  return (
    <YourPaymentScreen>
      <Button
        title="Manage payment methods"
        onPress={() => {
          setCustomerSheetVisible(true);
        }}
      />
    </YourPaymentScreen>
  );
}
```

Add the `CustomerSheet.Component` to your view hierarchy.

```jsx
import { CustomerSheet } from '@stripe/stripe-react-native';

export default function MyScreen() {
  const [customerSheetVisible, setCustomerSheetVisible] = React.useState(false);

  const clientSecretProvider = /* defined above */;

  return (
    <YourPaymentScreen>
      <Button
        title="Manage payment methods"
        onPress={() => {
          setCustomerSheetVisible(true);
        }}
      />
      <CustomerSheet.Component
        visible={customerSheetVisible}
        intentConfiguration={{
          paymentMethodTypes: ['card'],
        }}
        clientSecretProvider={clientSecretProvider}
        headerTextForSelectionScreen={'Manage your payment method'}
        returnURL={'my-return-url://'}
        onResult={() => {/* SEE BELOW */}}
      />
    </YourPaymentScreen>
  )
}
```

Use the `onResult` callback to render the selected payment method in your UI:

```jsx
import {CustomerSheet} from '@stripe/stripe-react-native';

export default function MyScreen() {
  const [customerSheetVisible, setCustomerSheetVisible] = React.useState(false);

  const clientSecretProvider = /* defined above */;

  return (
    <YourPaymentScreen>
      <Button
        title="Manage payment methods"
        onPress={() => {
          setCustomerSheetVisible(true);
        }}
      />
      <CustomerSheet.Component
        visible={customerSheetVisible}
        intentConfiguration={{
          paymentMethodTypes: ['card'],
        }}
        clientSecretProvider={clientSecretProvider}
        headerTextForSelectionScreen={'Manage your payment method'}
        returnURL={'my-return-url://'}
        onResult={({error, paymentOption, paymentMethod}) => {
          setCustomerSheetVisible(false);
          if (error) {
            if (error.code === CustomerSheetError.Canceled) {
              // Customer dismissed the sheet without changing their payment option
            } else {
              // Show the error in your UI
            }
            return;
          }

          if (paymentOption) {
            // Configure your UI based on the payment option
            MyBackend.setDefaultPaymentMethod(paymentMethod.id);
          }
          if (paymentMethod) {
            console.log(JSON.stringify(paymentMethod, null, 2));
          }
        }}
      />
    </YourPaymentScreen>
  );
}
```

- If the customer selects a payment method, the result contains a `paymentOption`. The associated value is the selected [PaymentOption](https://stripe.dev/stripe-react-native/api-reference/interfaces/PaymentSheet.PaymentOption.html), or `nil` if the user deleted the previously-selected payment method. You can find the full payment method details in the `paymentMethod` field.
- If the user cancels the sheet, the result contains an `error` with the `error.code === CustomerSheetError.Canceled`. The selected payment method doesn’t change.
- If an error occurs, the details are included in `error`.

Learn more about how to [enable Apple Pay](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=mobile&platform=ios#ios-apple-pay).

## Optional: Enable ACH payments

To enable ACH debit payments, enable `US Bank Account` as a payment method in the settings section of the [Dashboard](https://dashboard.stripe.com/settings/payment_methods).

## Optional: Fetch the selected payment method

To fetch the default payment method without presenting the Payment Method Settings Sheet, call `CustomerSheet.retrievePaymentOptionSelection()` after initializing the sheet.

```jsx
// Call CustomerSheet.initialize()
...
const {
  error,
  paymentOption,
  paymentMethod,
} = await CustomerSheet.retrievePaymentOptionSelection();
```

## Optional: Customize the sheet

### Appearance

Customize the colors, fonts, and other appearance attributes to match the look and feel of your app by using the [appearance API](https://docs.stripe.com/elements/appearance-api/mobile.md?platform=react-native).

### Default billing details

To set default values for billing details collected in the Payment Method Settings Sheet, configure the `defaultBillingDetails` property. The Payment Method Settings Sheet pre-populates its fields with the values that you provide.

```jsx
await CustomerSheet.initialize({
  // ...
  defaultBillingDetails: {
    email: "foo@bar.com",
    address: {
      country: "US",
    },
  },
});
```

### Billing details collection

Use `billingDetailsCollectionConfiguration` to specify how you want to collect billing details in the Payment Method Settings Sheet.

You can collect your customer’s name, email, phone number, and address.

If you don’t intend to collect the values that the payment method requires, you must do the following:

1. Attach the values that aren’t collected by the Payment Method Settings Sheet to the `defaultBillingDetails` property.
1. Set `billingDetailsCollectionConfiguration.attachDefaultsToPaymentMethod` to `true`.

```jsx
await CustomerSheet.initialize({
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

> Consult with your legal counsel regarding laws that apply to collecting information. Only collect a phone number if you need it for a transaction.
