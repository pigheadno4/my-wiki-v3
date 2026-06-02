<!-- Source URL: https://docs.stripe.com/payments/mobile/display-bnpl-messaging -->
<!-- Fetched: 2026-04-22 -->

# Display BNPL Messaging

Automatically explain buy now, pay later payment options.

# iOS (UIKit)

> This is a iOS (UIKit) for when payment-ui is mobile and platform is ios. View the full page at https://docs.stripe.com/payments/mobile/display-bnpl-messaging?payment-ui=mobile&platform=ios.

To display promotional messaging for buy now, pay later payment options, use the [Payment Method Messaging Element](https://docs.stripe.com/payments/mobile/payment-method-messaging-element.md).

## Set up Stripe [Server-side] [Client-side]

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

## Initialize the Payment Method Messaging Element

Call `create` to instantiate the Payment Method Messaging Element with a `PaymentMethodMessagingElement.Configuration`. The Configuration object contains details about the potential purchase and how information about it should be displayed. After PaymentMethodMessagingElement has successfully initialized, put its view into your UI.

#### Swift

```swift
@_spi(PaymentMethodMessagingElementPreview) import StripePaymentSheet

class MyViewController: UIViewController {

    private var amount = 1000 // $10.00
    private var currency = "USD"

    private var paymentMethodMessagingElementView: UIView?

    func addPaymentMethodMessagingElement() {
        Task { @MainActor in
            // Create configuration object
            let configuration = PaymentMethodMessagingElement.Configuration(
                amount: amount,
                currency: currency,
            )

            // Create PaymentMethodMessagingElement
            switch await PaymentMethodMessagingElement.create(configuration: configuration) {
            case .success(let element):
                let elementView = element.view
                self.view.addSubview(elementView)
                self.paymentMethodMessagingElementView = elementView
                // Set up constraints for elementView
                NSLayoutConstraint.activate([(
                    // ..
                )])
            case .noContent:
                // No element is available to display with this configuration
                // You may want to adapt your UI accordingly
                // ...
            case .failed(let error):
                // An unrecoverable error has occurred while attempting to load the element
                // You may want to log the error or take other action
                // ...
            }
        }
    }

    override func viewDidLoad() {
        super.viewDidLoad()

        // Set up the remainder of your page
        // ...

        addPaymentMethodMessagingElement()
    }
}
```

## Optional: Update the element

If the customer performs an action that changes the configuration (for example, selecting a different product variant), initialize a new `PaymentMethodMessagingElement` instance to reflect the new information.

#### Swift

```swift
class MyViewController: UIViewController {

    // ...

    func updatePaymentMethodMessagingElement() {
        paymentMethodMessagingElementView?.removeFromSuperview()
        addPaymentMethodMessagingElement()
    }
}

```

## Optional: Customize the element

Customization options are available through the `PaymentMethodMessagingElement.Configuration` and `PaymentMethodMessagingElement.Appearance` objects.

#### Swift

```swift
// Configure appearance
let appearance = PaymentMethodMessagingElement.Appearance(
    style: .flat,
    font: .boldSystemFont(ofSize: 12),
    textColor: .black,
    infoIconColor: .blue
)

// Create configuration object
let configuration = PaymentMethodMessagingElement.Configuration(
    amount: 1000, // $10.00
    currency: "USD",
    locale: "en_GB", // Defaults to device locale but can be explicitly set
    countryCode: "US", // Defaults to customer IP address but can be explicitly set
    paymentMethodTypes: [.affirm, .klarna], // Defaults to dynamic payment methods from the Dashboard, but can be explicitly set
    appearance: appearance
)

```

# iOS (SwiftUI)

> This is a iOS (SwiftUI) for when payment-ui is mobile and platform is plugins. View the full page at https://docs.stripe.com/payments/mobile/display-bnpl-messaging?payment-ui=mobile&platform=plugins.

To display promotional messaging for buy now, pay later payment options, use the [Payment Method Messaging Element](https://docs.stripe.com/payments/mobile/payment-method-messaging-element.md).

## Set up Stripe [Server-side] [Client-side]

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

## Add the Payment Method Messaging Element to your View and pass your configuration

Add the `PaymentMethodMessagingElement.View` to your view hierarchy and pass in a `PaymentMethodMessagingElement.Configuration`. The Configuration object contains details about the potential purchase and how information should be displayed. If your configuration might change while the element is displayed (for example, if the customer selects a different product variant), use a `@State` property for the configuration or compute it using `@State` properties so that SwiftUI propagates the changes to the element and it reloads automatically.

#### Swift

```swift
@_spi(PaymentMethodMessagingElementPreview) import StripePaymentSheet

struct MyView: View {

    private var configuration: PaymentMethodMessagingElement.Configuration {
        .init(amount: price, currency: "usd")
    }
    @State private var price: Int = 1000 // $10.00

    var body: some View {
        // ...
        PaymentMethodMessagingElement.View(configuration)
        // ...
    }
}

```

## Optional: Display a placeholder

To display a placeholder, other content, or to take action depending on the result of the element’s load, pass in a `ViewBuilder` describing what to display depending on the element’s current `phase`.

#### Swift

```swift
@_spi(PaymentMethodMessagingElementPreview) import StripePaymentSheet

struct MyView: View {

    private var configuration: PaymentMethodMessagingElement.Configuration {
        .init(amount: price, currency: "usd")
    }
    @State private var price: Int = 1000 // $10.00

    var body: some View {
        // ...
        PaymentMethodMessagingElement.View(configuration) { phase in
            switch phase {
            case .loaded(let view):
                // Add the view to your view hierarchy.
                view
            case .loading:
                // The element is still loading. Display a loading state.
                // ...
                MyLoadingView()
            case .noContent:
                // No element is available to display with this configuration.
                // For example, the amount is less than the minimum for available payment methods.
                // ...
            case .failed(let error):
                // An unrecoverable error has occurred while attempting to load the element.
                // You may want to log the error or take other action.
                // ...
            }
        }
        // ...
    }
}
```

## Optional: Manually load the element

To directly call and manage the loading of the element, such as when using MVVM-style architecture, call `create` to instantiate the Payment Method Messaging Element with a `PaymentMethodMessagingElement.Configuration`. If loading is successful, the `PaymentMethodMessagingElement` will contain a `viewData` property that can be passed to the `PaymentMethodMessagingElement.View` for immediate display.

#### Swift

```swift
@_spi(PaymentMethodMessagingElementPreview) import StripePaymentSheet

struct MyView: View {

    @StateObject private var viewModel: MyViewModel

    var body: some View {
        // Define the rest of your view
        // ...

        // Display the PaymentMethodMessagingElement if available
        if let viewData = viewModel.pmmeViewData {
            PaymentMethodMessagingElement.View(viewData)
        }

        // ...
    }
}

class MyViewModel: ObservableObject {

    @Published var pmmeViewData: PaymentMethodMessagingElement.ViewData?

    // Call this whenever you load the rest of your view, such as in `.onAppear`
    func loadPaymentMethodMessagingElement() {
        Task { @MainActor in
            // Create configuration object
            let configuration = PaymentMethodMessagingElement.Configuration(
                amount: 1000, // $10.00
                currency: "USD"
            )

            // Create PaymentMethodMessagingElement
            switch await PaymentMethodMessagingElement.create(configuration: configuration) {
            case .success(let element):
                self.pmmeViewData = element.viewData
            case .noContent:
                // No element is available to display with this configuration
                // For example, the amount is less than the minimum for available payment methods
                // ...
            case .failed(let error):
                // An unrecoverable occurred while attempting to load the element
                // You might want to log the error or take other action
                // ...
            }
        }
    }
}
```

## Optional: Customize the element

Customization options are available through the `PaymentMethodMessagingElement.Configuration` and `PaymentMethodMessagingElement.Appearance` objects.

#### Swift

```swift
// Configure appearance
let appearance = PaymentMethodMessagingElement.Appearance(
    style: .flat,
    font: .boldSystemFont(ofSize: 12),
    textColor: .black,
    infoIconColor: .blue
)

// Create configuration object
let configuration = PaymentMethodMessagingElement.Configuration(
    amount: 1000, // $10.00
    currency: "USD",
    locale: "en_GB", // Defaults to device locale but can be explicitly set
    countryCode: "US", // Defaults to customer IP address but can be explicitly set
    paymentMethodTypes: [.affirm, .klarna], // Defaults to dynamic payment methods from the Dashboard, but can be explicitly set
    appearance: appearance
)

```

# Android

> This is a Android for when payment-ui is mobile and platform is android. View the full page at https://docs.stripe.com/payments/mobile/display-bnpl-messaging?payment-ui=mobile&platform=android.

To display promotional messaging for buy now, pay later payment options, use the [Payment Method Messaging Element](https://docs.stripe.com/payments/mobile/payment-method-messaging-element.md).

## Set up Stripe [Server-side] [Client-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

The [Stripe Android SDK](https://github.com/stripe/stripe-android) is open source and [fully documented](https://stripe.dev/stripe-android/).

To install the SDK, add `payment-method-messaging` to the `dependencies` block of your [app/build.gradle](https://developer.android.com/studio/build/dependencies) file:

#### Kotlin

```kotlin
plugins {
    id("com.android.application")
}

android { ... }

dependencies {
  // ...

  // Payment Method Messaging Element Android SDK
  implementation("com.stripe:payment-method-messaging:23.5.0")
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

## Configure the Payment Method Messaging Element

Initialize the `PaymentMethodMessagingElement` by calling `create` and passing the application context. Configure the element by calling `configure`. `configure` returns a `PaymentMethodMessagingElement.Result` to indicate if there’s content to display or if the call succeeded. The Configuration object contains details about the potential purchase and how information about it should be displayed.

#### Kotlin

```kotlin
@OptIn(PaymentMethodMessagingElementPreview::class)
class MyViewModel(
    application: Application,
) : AndroidViewModel(application) {

    val paymentMethodMessagingElement = PaymentMethodMessagingElement.create(getApplication())

    fun configurePaymentMethodMessagingElement() {
        viewModelScope.launch {
            val result = paymentMethodMessagingElement.configure(
                configuration = PaymentMethodMessagingElement.Configuration()
                    .amount(10000L)
                    .currency("usd")
            )

            when (result) {
                is PaymentMethodMessagingElement.ConfigureResult.Succeeded -> {
                    // Handle success
                }
                is PaymentMethodMessagingElement.ConfigureResult.NoContent -> {
                    // Handle no content available
                }
                is PaymentMethodMessagingElement.ConfigureResult.Failed -> {
                    // Handle failure
                }
            }
        }
    }
}
```

## Display the Payment Method Messaging Element

On your Activity, display the content by calling `PaymentMethodMessagingElement.Content`. The composable automatically updates the content if you call `configure` with different params.

#### Kotlin

```kotlin
@OptIn(PaymentMethodMessagingElementPreview::class)
class MyActivity: AppCompateActivity() {

    override fun onCreate(savedInstanceState: Bundle?, persistentState: PersistableBundle?) {
        super.onCreate(savedInstanceState, persistentState)

        setContent {
            // Define the rest of your UI
            viewModel.paymentMethodMessagingElement.Content()
        }
    }
}

```

## Optional: Customize the element

Customize the configuration with `PaymentMethodMessagingElement.Configuration`.

#### Kotlin

```kotlin
@OptIn(PaymentMethodMessagingElementPreview::class)
class MyViewModel(
    application: Application,
) : AndroidViewModel(application) {

    val paymentMethodMessagingElement = PaymentMethodMessagingElement.create(getApplication())

    fun configurePaymentMethodMessagingElement() {
        viewModelScope.launch {
            val configuration = PaymentMethodMessagingElement.Configuration()
                 .amount(10000L)
                 .currency("usd")
                 .locale("en_GB") // Defaults to device locale but can be explicitly set
                 .countryCode("US")  // Defaults to customer IP address but can be explicitly set
                 .paymentMethodTypes(listOf(PaymentMethod.Type.Klarna, PaymentMethod.Type.Affirm)) // Defaults to dynamic payment methods from the Dashboard, but can be explicitly set
            val result = paymentMethodMessagingElement.configure(configuration)
        }
    }
}
```

Customize the appearance with `PaymentMethodMessagingElement.Appearance`.

#### Kotlin

```kotlin
@OptIn(PaymentMethodMessagingElementPreview::class)
class MyActivity: AppCompateActivity() {

    override fun onCreate(savedInstanceState: Bundle?, persistentState: PersistableBundle?) {
        super.onCreate(savedInstanceState, persistentState)

        setContent {
            // Define the rest of your UI
            val font = PaymentMethodMessagingElement.Font()
                .fontFamily(R.font.custom_font)
                .fontWeight(FontWeight.Bold)
                .fontSizeSp(20f)
                .letterSpacingSp(4f)

            val colors = PaymentMethodMessagingElement.Colors()
                 .textColor(getResources().getColor(R.color.text_color))
                 .infoIconColor(getResources().getColor(R.color.icon_color))

            val appearance = PaymentMethodMessagingElement.Appearance()
                 .font(font)
                 .theme(PaymentMethodMessagingElement.Theme.DARK)
                 .colors(colors)
            viewModel.paymentMethodMessagingElement.Content(appearance.build())
        }
    }
}
```
