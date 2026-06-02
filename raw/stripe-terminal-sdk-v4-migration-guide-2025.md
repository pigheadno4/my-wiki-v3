<!-- Source URL: https://docs.stripe.com/terminal/references/sdk-v4-migration-guide -->
<!-- Fetched: 2026-05-01 -->

# Terminal SDK V4 migration guide

Learn how to migrate to version 4.0.0 of the Stripe Terminal SDK.

The Stripe Terminal iOS and Android SDKs have been updated with a number of breaking changes in APIs and behavior, some of which require you to update your integration with the Stripe Terminal SDK. To improve consistency between our SDKs and to simplify your application logic and integration, we regularly make changes in major version updates that might affect the way your integration works or behaves. This guide explains the latest changes to help you upgrade your integration.

> If you’re building a new Stripe Terminal integration, see [Design an integration](https://docs.stripe.com/terminal/designing-integration.md) learn how to get started.

## Migrate to version 4.0.0

Here’s what you need to know about the 4.0.0 Stripe Terminal iOS and Android SDKs:

- [Save payment details after payment globally](https://docs.stripe.com/terminal/features/saving-payment-details/save-after-payment.md)
  - Users can now save payment details after payment outside of the US by updating the customer consent collection process for saving payment details on point-of-sale devices.
- Support for [Mail order and telephone order](https://docs.stripe.com/terminal/features/mail-telephone-orders/overview.md) (MOTO) payments on smart readers (Preview)
  - This feature is in preview. To request access, email [stripe-terminal-betas@stripe.com](mailto:stripe-terminal-betas@stripe.com).
- Updates to the minimum supported iOS platform version
- Enables [reader auto-reconnect on unexpected disconnects](https://docs.stripe.com/terminal/payments/connect-reader.md?terminal-sdk-platform=ios&reader-type=tap-to-pay#automatically-attempt-reconnection) by default for mobile and Tap to Pay readers
- Consolidates reader connection functionality and disconnect callbacks for all reader types

# iOS

> This is a iOS for when terminal-sdk-platform is ios. View the full page at https://docs.stripe.com/terminal/references/sdk-v4-migration-guide?terminal-sdk-platform=ios.

If your application currently uses an Terminal iOS SDK version earlier than 4.0.0, you need to make a few changes to upgrade and accept card present payments globally. For a detailed list of the changes from version 3.9.1 to 4.0.0, see the [SDK changelog](https://github.com/stripe/stripe-terminal-ios/blob/master/CHANGELOG.md).

## Update your minimum supported version to iOS 14 or higher

We regularly update the minimum supported version of our SDKs to streamline our developer support efforts.

Existing 3.X versions of the Terminal iOS SDK continue to support devices running _iOS 13_ and later.

## Update saving cards after PaymentIntents integration

If you [save a payment method after a successful in-person PaymentIntent](https://docs.stripe.com/terminal/features/saving-payment-details/save-after-payment.md), you need to make the following updates to your integration:

- When creating Terminal PaymentIntents, pass the [setup_future_usage](<https://stripe.dev/stripe-terminal-ios/docs/4.0.0/Classes/SCPPaymentIntent.html#/c:objc(cs)SCPPaymentIntent(py)setupFutureUsage>) parameter, which informs Stripe that you want to make future payments with the same card.

- You also need to pass [allow_redisplay](<https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPCollectConfiguration.html#/c:objc(cs)SCPCollectConfiguration(py)allowRedisplay>) as `always` or `limited` in `SCPCollectConfiguration`. Pass `always` if you want the customer’s saved card to be presented to them in all future checkout flows, and `limited` if they can only use it in the context of the initially scoped use, such as a subscription.

  Learn more about [saving payment details after a payment](https://docs.stripe.com/terminal/features/saving-payment-details/save-after-payment.md).

## Update saving cards without payment with SetupIntents integration

To ensure a consistent integration pattern between SetupIntents and PaymentIntents, and in-person and online transactions, in `SCPTerminal`’s `collectSetupIntentPaymentMethod`, we removed the `customerConsentCollected` parameter that was previously required on all SetupIntent transactions, and replaced it with the `allowRedisplay` parameter.

Learn more about [saving directly without charging](https://docs.stripe.com/terminal/features/saving-payment-details/save-directly.md).

## Update your discoverReaders usage

- We added a new enum value, `discovering`, to [SCPConnectionStatus](https://stripe.dev/stripe-terminal-ios/docs/Enums/SCPConnectionStatus.html) to represent when reader discovery is running. Make sure your integration can handle this new state and provide relevant information to your customers.

- We improved the handling of multiple simultaneous reader discover operations. Previously, calling [discoverReaders](<https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)discoverReaders:delegate:completion:>) multiple times would queue the operations. Now, when a new [discoverReaders](<https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)discoverReaders:delegate:completion:>) is called while an existing one is already in progress, the SDK cancels the ongoing operation and returns a [SCPErrorCanceledDueToIntegrationError](https://stripe.dev/stripe-terminal-ios/docs/Errors.html#/c:@SCPErrorNewDiscoveryRequested) error. The new discoverReaders operation then starts immediately.

- Discovering smart and Tap to Pay readers now calls the `discoverReaders` completion block when the operation ends. This change reflects the reality that reader discovery for these reader types isn’t a long-running operation.

- We fixed a bug that strongly held a reference to the [SCPDiscoveryDelegate](https://stripe.dev/stripe-terminal-ios/docs/Protocols/SCPDiscoveryDelegate.html) in the SDK. Make sure your application is holding a strong reference to your delegate to receive the discovery events.

## Update your reader connection usage

- To ensure a consistent integration pattern across reader discovery and connection, we consolidated all previous reader connection methods (`connectBluetoothReader`, `connectInternetReader`, `connectLocalMobileReader`) into [connectReader](<https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)connectReader:delegate:connectionConfig:completion:>). The exact connection type is still determined by the passed in connection configuration.

- For mobile readers and Tap to Pay readers, the `ReaderDelegate` parameter has been removed from the `connectReader` method and instead moved into the `connectionConfig`, replacing `SCPReconnectionDelegate`. Consistent with other reader types, smart readers `InternetConnectionConfiguration` now also expects an `InternetReaderDelegate` to be passed in, which alerts your integration of events, including when a reader disconnects.

| Reader Type   | Connection Configuration            | Reader Delegate                                                                                                                   |
| ------------- | ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Mobile Reader | SCPBluetoothConnectionConfiguration | [SCPMobileReaderDelegate](https://stripe.dev/stripe-terminal-ios/docs/4.0.0/Protocols/SCPMobileReaderDelegate.html)               |
| Smart Reader  | SCPInternetConnectionConfiguration  | [SCPInternetReaderDelegate](<https://stripe.dev/stripe-terminal-ios/docs/4.0.0/Reader.html#/c:objc(pl)SCPInternetReaderDelegate>) |
| Tap to Pay    | SCPTapToPayConnectionConfiguration  | [SCPTapToPayReaderDelegate](https://stripe.dev/stripe-terminal-ios/docs/4.0.0/Protocols/SCPTapToPayReaderDelegate.html)           |

### Before

#### Swift

```swift
// Call `connectBluetoothReader` with the selected reader and a connection config
// to register to a location as set by your app.
let connectionConfig: BluetoothConnectionConfiguration
do {
    connectionConfig = try BluetoothConnectionConfigurationBuilder(locationId: ""{{LOCATION_ID}}"").build()
} catch {
    // Handle the error building the connection configuration
    return
}
Terminal.shared.connectBluetoothReader(selectedReader, delegate: readerDelegate, connectionConfig: connectionConfig) { reader, error in
    if let reader = reader {
        print("Successfully connected to reader: \(reader)")
    } else if let error = error {
        print("connectBluetoothReader failed: \(error)")
    }
}
```

### After

#### Swift

```swift
// Call `connectReader` with the selected reader and a connection config
// to register to a location as set by your app.
let connectionConfig: BluetoothConnectionConfiguration
do {
    connectionConfig = try BluetoothConnectionConfigurationBuilder(delegate: yourMobileReaderDelegate, locationId: ""{{LOCATION_ID}}"")
    .build()
} catch {
    // Handle the error building the connection configuration
    return
}
Terminal.shared.connectReader(selectedReader, connectionConfig: connectionConfig) { reader, error in
    if let reader = reader {
        print("Successfully connected to reader: \(reader)")
    } else if let error = error {
        print("connectReader failed: \(error)")
    }
}
```

For more details, refer our documentation about [connecting to a reader](https://docs.stripe.com/terminal/payments/connect-reader.md?terminal-sdk-platform=ios&reader-type=bluetooth#connect-reader).

## Auto reconnection is now enabled by default for mobile and Tap to Pay readers

- To increase the resiliency of your Terminal integration with mobile and Tap to Pay readers, we enabled [auto reconnection](https://docs.stripe.com/terminal/payments/connect-reader.md?terminal-sdk-platform=ios&reader-type=bluetooth#handle-disconnects) by default when a reader unexpectedly disconnects.

- We recommend displaying notifications in your app to inform the users about the reader status throughout the reconnection process. To handle reader reconnection methods, we removed the `SCPReconnectionDelegate`. Its responsibilities have been integrated into the respective ReaderDelegates. Use `MobileReaderDelegate` for mobile readers, and `TapToPayReaderDelegate` for Tap to Pay readers to handle reconnection events.

- If you implemented your own reader reconnection logic and want to maintain this behavior, you can turn off auto reconnection by setting [setAutoReconnectOnUnexpectedDisconnect](<https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPBluetoothConnectionConfigurationBuilder.html#/c:objc(cs)SCPBluetoothConnectionConfigurationBuilder(im)setAutoReconnectOnUnexpectedDisconnect:>) to `false`.

### Before

#### Swift

```swift
import StripeTerminal

extension ReaderViewController: ReconnectionDelegate {
    // MARK: ReconnectionDelegate
    func terminal(_ terminal: Terminal, didStartReaderReconnect cancelable: Cancelable) {
        // 1. Notified at the start of a reconnection attempt
        // Use cancelable to stop reconnection at any time
    }

    func terminalDidSucceedReaderReconnect(_ terminal: Terminal) {
        // 2. Notified when reader reconnection succeeds
        // App is now connected
    }
    func terminalDidFailReaderReconnect(_ terminal: Terminal) {
        // 3. Notified when reader reconnection fails
        // App is now disconnected
    }
}
```

### After

#### Swift

```swift
import StripeTerminal

extension ReaderViewController: MobileReaderDelegate {
    // MARK: MobileReaderDelegate

    func reader(_ reader: Reader, didStartReconnect cancelable: Cancelable, disconnectReason: DisconnectReason) {
        // 1. Notified at the start of a reconnection attempt
        // Use cancelable to stop reconnection at any time
    }

    func readerDidSucceedReconnect(_ reader: Reader) {
        // 2. Notified when reader reconnection succeeds
        // App is now connected
    }
    func readerDidFailReconnect(_ reader: Reader) {
        // 3. Notified when reader reconnection fails
        // App is now disconnected
    }
}
```

For more details and code snippets, see [automatically attempting to reconnect](https://docs.stripe.com/terminal/payments/connect-reader.md?terminal-sdk-platform=ios&reader-type=tap-to-pay#automatically-attempt-reconnection).

## Update your reader disconnect handling

- To be informed when a reader disconnects, we consolidated the reader disconnect callbacks for all reader types by removing `terminal:didReportUnexpectedReaderDisconnect:` from the `SCPTerminalDelegate`. Use `reader:didDisconnect:` as part of the ReaderDelegates to be notified when a reader disconnects. For mobile readers, the [SCPDisconnectReason](https://stripe.dev/stripe-terminal-ios/docs/Enums/SCPDisconnectReason.html) can help identify the reason for the disconnection.

With auto-reconnection enabled, both [`-readerDidFailReconnect:`](<https://stripe.dev/stripe-terminal-ios/docs/4.0.0/Protocols/SCPReaderDelegate.html#/c:objc(pl)SCPReaderDelegate(im)readerDidFailReconnect:>) and [`reader:didDisconnect:`](<https://stripe.dev/stripe-terminal-ios/docs/4.0.0/Protocols/SCPReaderDelegate.html#/c:objc(pl)SCPReaderDelegate(im)reader:didDisconnect:>) methods are called if the SDK fails to reconnect to the reader and it becomes disconnected.

### Before

#### Swift

```swift
import StripeTerminal

class ReaderViewController: UIViewController, TerminalDelegate {
    override func viewDidLoad() {
        super.viewDidLoad()
        Terminal.shared.delegate = self
    }

    // ...
    // MARK: TerminalDelegate
    func terminal(_ terminal: Terminal, didReportUnexpectedReaderDisconnect reader: Reader) {
        // Consider displaying a UI to notify the user and start rediscovering readers
    }
}
```

### After

#### Swift

```swift
import StripeTerminal

class ReaderViewController: UIViewController, MobileReaderDelegate {
    override func viewDidLoad() {
        super.viewDidLoad()
        // Set the reader delegate when connecting to a reader
    }

    // ...



    func reader(_ reader: Reader, didDisconnect reason: DisconnectReason) {
        // Consider displaying a UI to notify the user and start rediscovering readers
    }
}
```

For more details, refer to our documentation about [handling disconnects manually](https://docs.stripe.com/terminal/payments/connect-reader.md?terminal-sdk-platform=ios&reader-type=tap-to-pay#handle-the-disconnect-manually).

## Update your payment acceptance integration

- You can now cancel `confirmPaymentIntent` using the returned `Cancelable` object. You can use this for QR code payments, which have an asynchronous confirmation process. Similarly, `confirmSetupIntent` and `confirmRefund` are also now cancelable.
- We improved type safety and consistency between the mobile SDKs by updating the way `paymentMethodTypes` are specified in `SCPPaymentIntentParameters` and `SCPSetupIntentParameters`. Previously, this parameter was represented as an array of strings (for example, [“card_present”]). It now uses enum values from `SCPPaymentMethodType`.
- To improve the cancellation flow for PaymentIntents and SetupIntents, calling `Terminal::cancelPaymentIntent` or `Terminal::cancelSetupIntent` now also cancels any ongoing payment processing. You no longer need to cancel payment operations such as `.collectPaymentMethod` separately before canceling the PaymentIntent.
- `SCPSetupIntent.stripeId` is now nullable to be consistent with `SCPPaymentIntent.stripeId`. Although the `stripeId` value will continue to exist, make sure your code safely handles the case where `SCPSetupIntent.stripeId` might be `null` to avoid compiler errors.

## Update usage for renaming and deprecation

- [`BluetoothReaderDelegate`](https://stripe.dev/stripe-terminal-ios/3.9.0/Protocols/SCPBluetoothReaderDelegate.html) has been renamed to [`MobileReaderDelegate`](https://stripe.dev/stripe-terminal-ios/Protocols/SCPMobileReaderDelegate.html).
- In `SCPReaderSoftwareUpdate,` we renamed `SCPUpdateTimeEstimate` to `SCPUpdateDurationEstimate` and `estimatedUpdateTime` to `durationEstimate` to better represent their intent.
- In `SCPOfflineDetails`, which represents payment details available when a payment is created or confirmed while offline, we renamed the time that the offline payment happened from `collectedAt` to `storedAt`, aligning with the naming conventions in the Terminal Android SDK.
- We renamed “local mobile” and “apple built in” to “Tap To Pay” in all SDK function names and error codes.

# Android

> This is a Android for when terminal-sdk-platform is android. View the full page at https://docs.stripe.com/terminal/references/sdk-v4-migration-guide?terminal-sdk-platform=android.

If your application currently uses an Terminal Android SDK version prior to 4.0.0, there are some changes you need to make to upgrade and accept card present payments globally. For a detailed list of the changes from version 3.10.0 to 4.0.0, see the [SDK changelog](https://github.com/stripe/stripe-terminal-android/blob/master/CHANGELOG.md).

## Update your saving cards after PaymentIntents integration

If you [save a payment method after a successful in-person PaymentIntent](https://docs.stripe.com/terminal/features/saving-payment-details/save-after-payment.md), you need to make the following updates to your integration:

- When creating Terminal PaymentIntents, pass the [setup_future_usage](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-payment-intent/index.html#-745150436%2FProperties%2F-1219334616) parameter, which informs Stripe that you want to make future payments with the same card.
- You also need to pass [allow_redisplay](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-collect-configuration/index.html#-74877977%2FProperties%2F-1219334616) as `ALWAYS` or `LIMITED` in `CollectConfiguration`. Pass `ALWAYS` if you want to present the customer’s saved card to them in all future checkout flows, and `LIMITED` if they can only use it in the context of the initially scoped use, such as a subscription.

Learn more about [saving cards after a payment](https://docs.stripe.com/terminal/features/saving-payment-details/save-after-payment.md).

## Update your saving cards without payment with SetupIntents integration

To ensure a consistent integration pattern between SetupIntents and PaymentIntents, as well as in-person and online transactions, in `Terminal`’s [`collectSetupIntentPaymentMethod`](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/index.html#915185703%2FFunctions%2F-1814817128), we removed the `customerConsentCollected` parameter previously required on all SetupIntent transactions, and replaced it with the `allowRedisplay` parameter.

Learn more about [saving directly without charging](https://docs.stripe.com/terminal/features/saving-payment-details/save-directly.md).

## Update your discoverReaders usage

- We added a new enum value, `DISCOVERING`, to [ConnectionStatus](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-connection-status/index.html) to represent when reader discovery is running. Make sure your integration can handle this new state and provide relevant information to your customers.

- We improved the handling of multiple simultaneous reader discover operations. Previously, calling [Terminal::discoverReaders](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/index.html#-307737612%2FFunctions%2F-1814817128) multiple times would queue the operations, which we learned was undesirable. Now when a new `Terminal::discoverReaders` is called while an existing one is already in progress, the SDK cancels the ongoing operation and returns a [CANCELED_DUE_TO_INTEGRATION_ERROR](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-terminal-error-code/-c-a-n-c-e-l-e-d_-d-u-e_-t-o_-i-n-t-e-g-r-a-t-i-o-n_-e-r-r-o-r/index.html) error. The new discoverReaders operation then starts immediately.

- Discovering smart and Tap to Pay readers now calls the `Terminal::discoverReaders` completion callback when the operation ends. This change reflects the reality that reader discovery for these reader types isn’t a long-running operation.

## Update your reader connection usage

- To ensure a consistent integration pattern across reader discovery and connection, we consolidated all reader connection methods (`connectBluetoothReader`, `connectUsbReader`, `connectInternetReader`, `connectLocalMobileReader`, `connectHandoffReader`) into [Terminal::connectReader](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/index.html#1656325082%2FFunctions%2F-1814817128). The specific connection type is still determined by the provided connection configuration.
- For mobile readers, the `readerListener` parameter has been removed from the old `connectBluetoothReader`, `connectUsbReader` methods and moved into the respective `ConnectionConfiguration` object, replacing `ReaderReconnectionListener`. For Tap to Pay readers, the `TapToPayConnectionConfiguration` now takes in an `TapToPayReaderListener` parameter, replacing `ReaderReconnectionListener`.
- Consistent with other reader types, smart readers’s `InternetConnectionConfiguration` now also expects an [`InternetReaderListener`](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.callable/-internet-reader-listener/index.html) to be passed in, which alerts your integration of events including reader disconnects.
- For [Apps on devices](https://docs.stripe.com/terminal/features/apps-on-devices/overview.md#pos-stripe-device) in handoff mode, [`HandoffReaderListener`](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.callable/-handoff-reader-listener/index.html) has been removed from the old `connectHandoffReader` method as a parameter, and moved into the `HandoffConnectionConfiguration` object.

| Reader Type     | Connection Configuration           | Reader Listener                                                                                                                                                  |
| --------------- | ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mobile Reader   | `BluetoothConnectionConfiguration` | [MobileReaderListener](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.callable/-mobile-reader-listener/index.html)       |
| Smart Reader    | `InternetConnectionConfiguration`  | [InternetReaderListener](https://stripe.dev/stripe-terminal-android/com.stripe.stripeterminal.external.callable/-internet-reader-listener/index.html)            |
| Tap to Pay      | `TapToPayConnectionConfiguration`  | [TapToPayReaderListener](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.callable/-tap-to-pay-reader-listener/index.html) |
| Apps on Devices | `HandoffConnectionConfiguration`   | [HandoffReaderListener](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.callable/-handoff-reader-listener/index.html)     |

### Before

#### Kotlin

```kotlin
val connectionConfig = ConnectionConfiguration.BluetoothConnectionConfiguration(
    ""{{LOCATION_ID}}""
)
Terminal.getInstance().connectBluetoothReader(
    selectedReader,
    connectionConfig,
    readerListener,
    object : ReaderCallback {
        override fun onSuccess(reader: Reader) {
            // Placeholder for handling successful operation
        }
        override fun onFailure(e: TerminalException) {
            // Placeholder for handling exception
        }
    }
)
```

### After

#### Kotlin

```kotlin
// Implement your MobileReaderListener
val mobileReaderListener = yourMobileReaderListener
val autoReconnectOnUnexpectedDisconnect = true

val connectionConfig = BluetoothConnectionConfiguration(
    ""{{LOCATION_ID}}"",
    autoReconnectOnUnexpectedDisconnect,
    mobileReaderListener
)

Terminal.getInstance().connectReader(
    selectedReader,
    connectionConfig,
    object : ReaderCallback {
        override fun onSuccess(reader: Reader) {
            // Placeholder for handling successful operation
        }

        override fun onFailure(e: TerminalException) {
            // Placeholder for handling exception
        }
    }
)
```

For more details, see [connecting to a reader](https://docs.stripe.com/terminal/payments/connect-reader.md?terminal-sdk-platform=android&reader-type=bluetooth#connect-reader).

## Auto reconnection is now enabled by default for mobile and Tap to Pay readers

- To increase the resiliency of your Terminal integration with mobile and Tap to Pay readers, we enabled [auto reconnection](https://docs.stripe.com/terminal/payments/connect-reader.md?terminal-sdk-platform=android&reader-type=bluetooth#handle-disconnects) by default when the reader unexpectedly disconnects.
- We recommend displaying notifications in your app to inform the users about the reader status throughout the reconnection process. To handle reader reconnection methods, the `ReaderReconnectionListener` has been inherited by the respective ReaderListeners. Use `MobileReaderListener` for mobile readers, and `TapToPayReaderListener` for Tap to Pay readers to handle reconnection events.
- We removed the `ReaderReconnectionListener` parameter from the connection configurations: `LocalMobileConnectionConfiguration`, `BluetoothConnectionConfiguration`, and `UsbConnectionConfiguration`, and replaced by the appropriate `ReaderListener`.

If you implemented your own reader reconnection logic and want to maintain this behavior, you can turn off auto reconnection by setting [autoReconnectOnUnexpectedDisconnect](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-connection-configuration/-bluetooth-connection-configuration/index.html#1748469061%2FProperties%2F-1219334616) to `false`.

### Before

#### Kotlin

```kotlin
class CustomReaderReconnectionListener : ReaderReconnectionListener {
    override fun onReaderReconnectStarted(reader: Reader, cancelReconnect: Cancelable, reason: DisconnectReason) {
        // 1. Notified at the start of a reconnection attempt
        // Use cancelable to stop reconnection at any time
    }

    override fun onReaderReconnectSucceeded(reader: Reader) {
        // 2. Notified when reader reconnection succeeds
        // App is now connected
    }

    override fun onReaderReconnectFailed(reader: Reader) {
        // 3. Notified when reader reconnection fails
        // App is now disconnected
    }
}
```

### After

#### Kotlin

```kotlin
class CustomMobileReaderListener : MobileReaderListener {
    // ...

    override fun onReaderReconnectStarted(reader: Reader, cancelReconnect: Cancelable, reason: DisconnectReason) {
        // 1. Notified at the start of a reconnection attempt
        // Use cancelable to stop reconnection at any time
    }

    override fun onReaderReconnectSucceeded(reader: Reader) {
        // 2. Notified when reader reconnection succeeds
        // App is now connected
    }

    override fun onReaderReconnectFailed(reader: Reader) {
        // 3. Notified when reader reconnection fails
        // App is now disconnected
    }

    // ...
}
```

For more details, see [automatically attempting to reconnect](https://docs.stripe.com/terminal/payments/connect-reader.md?terminal-sdk-platform=android&reader-type=tap-to-pay#automatically-attempt-reconnection).

## Update your reader disconnect handling

- To be informed when a reader disconnects, we consolidated the reader disconnect callbacks for all reader types by removing `TerminalListener::onUnexpectedReaderDisconnect`. Going forward, implement `onDisconnect` on any of the following listeners to be informed of their corresponding reader disconnects: `InternetReaderListener`, `MobileReaderListener`, `TapToPayReaderListener`, or `HandoffReaderListener`. For mobile readers, the [`DisconnectReason`](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-disconnect-reason/index.html) can help identify the reason for the disconnection.

When auto-reconnect is enabled, both `onDisconnect` and [`onReaderReconnectFailed`](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.callable/-reader-reconnection-listener/on-reader-reconnect-failed.html) methods are called if the SDK fails to reconnect to the reader and it becomes disconnected.

### Before

#### Kotlin

```kotlin
class ReaderActivity : AppCompatActivity(), TerminalListener {
    // ...
    Terminal.getInstance().setTerminalListener(this)
    // ...
    override fun onUnexpectedReaderDisconnect(reader: Reader) {
        // Consider displaying a UI to notify the user and start rediscovering readers
    }
    // ...
}
```

### After

#### Kotlin

```kotlin
class ReaderActivity : AppCompatActivity(), MobileReaderListener {
    // ...

    override fun onDisconnect(reason: DisconnectReason) {
        // Consider displaying a UI to notify the user and start rediscovering readers
    }

    // ...
}
```

For more details, see [handling disconnects manually](https://docs.stripe.com/terminal/payments/connect-reader.md?terminal-sdk-platform=android&reader-type=tap-to-pay#handle-the-disconnect-manually).

## Update your payment acceptance integration

- You can now cancel `Terminal::confirmPaymentIntent` using the returned `Cancelable` object. You can use this for QR code payments, which have an asynchronous confirmation process. Similarly, `Terminal::confirmSetupIntent` and `Terminal::confirmRefund` are now cancelable as well.
- To improve the cancellation flow for PaymentIntents and SetupIntents, calling `Terminal::cancelPaymentIntent` or `Terminal::cancelSetupIntent` now also cancels any ongoing payment processing. You no longer need to cancel payment operations such as `Terminal::collectPaymentMethod` separately before canceling the PaymentIntent.
- `SetupIntent.id` is now nullable to be consistent with `PaymentIntent.id`. Although the `id` value is still present, make sure your code safely handles the case where `SetupIntent.id` might be `null` to avoid compiler error.

## Update error handling

- We moved `TerminalException.TerminalErrorCode` to a standalone enum, `TerminalErrorCode`. Make sure to update the import statements and Terminal error code definition to maintain functionality.
- We added a new Terminal error code `TerminalErrorCode.GENERIC_READER_ERROR`, which can happen when the SDK is out of date, and can’t recognize the error returned by back the smart reader. To remediate this error, update your Terminal SDK.
- For Tap to Pay on Android, `Terminal::collectPaymentMethod` and `Terminal::collectSetupIntentPaymentMethod` now time out after 60 seconds for Tap to Pay on Android transactions. A `TerminalException` is raised with the error code `TerminalErrorCode.CARD_READ_TIMED_OUT`.
- For Tap to Pay on Android, when PIN collection is requested for a payment, a `TerminalException` is raised with the error code `FEATURE_NOT_ENABLED_ON_ACCOUNT` instead of `DECLINED_BY_STRIPE_API` with an `ONLINE_OR_OFFLINE_PIN_REQUIRED` `ApiError`.

## Update usage for renaming and refactoring

- `ReaderListener` has been renamed to [`MobileReaderListener`](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.callable/-mobile-reader-listener/index.html).
- We renamed the `allowedPaymentMethodTypes` parameter to `paymentMethodTypes` in the `PaymentIntentParameters.Builder` and `SetupIntentParameter.Builder` constructors.
- In `ReaderSoftwareUpdate,` we renamed `UpdateTimeEstimate` to `UpdateDurationEstimate` and `estimatedUpdateTime` to `durationEstimate` to better represent their intent.
- We converted `java.util.Date` references to timestamps in milliseconds for the following fields: `ReaderSoftwareUpdate::requiredAt`, `OfflineDetails::storedAt` and `OfflineSetupIntentDetails::storedAt`. Make sure your application interprets these timestamps correctly.
- Fields on the `Location` object are no longer mutable.

## Update your Tap to Pay on Android integration

- The Maven coordinates for the Tap to Pay on Android feature have changed to `com.stripe:stripeterminal-taptopay:4.0.0`. Update your build dependencies to point to the new artifact name. The old one will no longer be updated.
- We renamed all `LocalMobile` function and field names to `TapToPay`. For example, `LocalMobileDiscoveryConfiguration` has been renamed to `TapToPayDiscoveryConfiguration`.
- `TapToPayConnectionConfiguration` now takes a `TapToPayReaderListener` parameter. This listener inherits events from both `ReaderReconnectionListener` and `ReaderDisconnectionListener`, providing a unified mechanism for handling reader events.
- We renamed the background application process used for collecting Tap to Pay transactions to use your application’s id, suffixed with `:stripetaptopay`.
