<!-- Source URL: https://docs.stripe.com/terminal/references/sdk-v3-migration-guide -->
<!-- Fetched: 2026-05-01 -->

# Terminal SDK V3 migration guide

Learn how to migrate to the 3.0.0 of the Stripe Terminal SDK.

The Stripe Terminal iOS and Android SDKs have been updated with a number of breaking changes in APIs and behavior, some of which require that you update your integration with the Stripe Terminal SDK. We regularly make changes in major version updates that might affect the way your integration works or behaves, to improve consistency between our SDKs and to simplify your application logic and integration. This guide walks you through the latest changes to help you upgrade your integration.

> Building a new Stripe Terminal integration? Visit our [Design an integration](https://docs.stripe.com/terminal/designing-integration.md) page to learn how to get started.

## Migrate to version 3.0.0

Here are some things you need to know about the 3.0.0 Stripe Terminal iOS and Android SDKs:

- Support for processing offline payments
  - The offline mode feature is in private preview. To request access, email [stripe-terminal-betas@stripe.com](mailto:stripe-terminal-betas@stripe.com). After we enable the changes in the backend for your account, you must disconnect and reconnect to your reader using the SDK for the updated configuration to take effect.
- Updates to minimum supported platform versions for iOS and Android
- Removal of deprecated features and properties

# iOS

> This is a iOS for when terminal-sdk-platform is ios. View the full page at https://docs.stripe.com/terminal/references/sdk-v3-migration-guide?terminal-sdk-platform=ios.

If your application currently uses an Terminal iOS SDK version prior to 3.0.0, there are a few changes you need to make to upgrade and accept card present payments globally. For a detailed list of the changes from version 2.23.1 to 3.0.0, please reference the [SDK changelog](https://github.com/stripe/stripe-terminal-ios/releases/tag/v3.0.0).

## Update your minimum supported version to iOS 13 or higher

We regularly update the minimum supported version of our SDKs to focus on providing the best experience for our developers.

Existing 2.X versions of the Terminal iOS SDK will continue to support devices running **iOS 11** and higher.

## Update your DiscoveryConfiguration usage to the specific DiscoveryConfiguration implementation

To support configuration for different discovery methods, [SCPDiscoveryConfiguration](https://stripe.dev/stripe-terminal-ios/docs/Protocols/SCPDiscoveryConfiguration.html) is now a protocol that is implemented by several different types. Instead of providing a DiscoveryMethod, there are now individual classes to choose from to search for a specific type of reader:

| Configuration Class                                                                                                                                 | Usage                                                                                                                              |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| [SCPBluetoothScanDiscoveryConfiguration](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPBluetoothScanDiscoveryConfiguration.html)           | Bluetooth-capable readers near this iOS device                                                                                     |
| [SCPBluetoothProximityDiscoveryConfiguration](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPBluetoothProximityDiscoveryConfiguration.html) | A subset of Bluetooth-capable readers near this iOS device                                                                         |
| [SCPInternetDiscoveryConfiguration](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPInternetDiscoveryConfiguration.html)                     | Internet-connected readers registered to this account                                                                              |
| [SCPLocalMobileDiscoveryConfiguration](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPLocalMobileDiscoveryConfiguration.html)               | [Tap to Pay](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay.md?platform=ios) using this iOS device’s NFC reader |

Create the discovery configuration appropriate for your desired discovery method using the provided builder class and provide that to `discoverReaders`. The builder exposes setters for the properties that each configuration supports.

## Update your discoverReaders and connectReader usage

- Canceling `discoverReaders` now calls the completion block with an error with code `SCPErrorCanceled`, just like all other cancelable methods.
- `discoverReaders` is now completed successfully right when `connectReader` is called. If `connectReader` fails, your integration needs to make a new call to `discoverReaders` to resume discovering readers.
- `discoverReaders` is no longer required to be running for `connectReader` to work. You’re now able to call `connectReader` with a previously discovered reader instance or to retry connecting without restarting `discoverReaders`.

## Update your ReconnectionDelegate implementation

`SCPReconnectionDelegate` now provides the instance of the reader that is being reconnected to instead of the Terminal instance. If you implemented this delegate before you need to replace `terminal` in the method names with `reader`.

## Update Parameters and Configuration class usage to use Builders

The input classes like `SCPCollectConfiguration` and `SCPPaymentIntentParameters` are now immutable and have associated builders provided to create them. All builders have a build method that validates the inputs and creates the class it builds.

- In Swift, `build()` throws and should be checked for errors.
- In Objective-C, you provide an `NSError **` out-parameter to receive the error, if any.

```swift
let paymentParams = try PaymentIntentParametersBuilder(amount: 100, currency: "cad")
  .setCaptureMethod(.automatic)
  .build()
```

## Remove any dependency on SCPErrorBusy

`SCPErrorBusy` is removed. In SDK 3.0.0 and later, if you call a Terminal method while another is still in-progress the new calls now queue up. The commands are executed after all previous commands complete. If you were previously tracking state to prevent `SCPErrorBusy`, or were queuing your own commands to work around `SCPErrorBusy`, you can now make use of the command queue to simplify your code. If your application relied on `SCPErrorBusy` to know if a command is running, review your code to see if this could cause problems with queuing too many commands.

## Review support for Offline Payments

`SCPPaymentIntent.stripeId` is null for offline payments. If your integration only supports online payments, the `stripeId` will always be present and no changes are needed beyond checks to satisfy the presence of the ID. See [Collect card payments while offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md?terminal-sdk-platform=ios) for more details on how to process payments offline.

```swift
Terminal.shared.createPaymentIntent(params) { intent, error in
  if let error = error {
    // Placeholder for handling exception
  }
  guard let intentId = intent.stripeId else {
    // PaymentIntent was created offline without an id. See intent.offlineDetails.
    // This is only expected when offline mode is enabled.
  }
}
```

## Update your process calls to confirm

`SCPTerminal.processPayment` is renamed to `SCPTerminal.confirmPaymentIntent` and `SCPTerminal.processRefund` is renamed to `SCPTerminal.confirmRefund`. The parameters for these methods haven’t changed but the error types have also been renamed to `SCPConfirmPaymentIntentError` and `SCPConfirmRefundError` respectively.

## Update your readReusableCard usage to SetupIntents

`SCPTerminal.readReusableCard` is removed. SetupIntents are the recommended path for saving payment methods without charging. SetupIntents follow a similar pattern to PaymentIntents where you create, collect, and then confirm the SetupIntent in the SDK. See [Save payment details for online re-use](https://docs.stripe.com/terminal/features/saving-payment-details/overview.md) for more details.

# Android

> This is a Android for when terminal-sdk-platform is android. View the full page at https://docs.stripe.com/terminal/references/sdk-v3-migration-guide?terminal-sdk-platform=android.

If your application currently uses an Terminal Android SDK version prior to 3.0.0, there are a few changes you need to make to upgrade and accept card present payments globally. For a detailed list of the changes from version 2.23.1 to 3.0.0, please reference the [SDK changelog](https://github.com/stripe/stripe-terminal-android/blob/master/CHANGELOG.md).

## Update your minimum supported version to Android 8 or higher

Future versions of the Terminal Android SDK will only support devices running **Android 8.0 “Oreo” (API 26)** and higher. We regularly update the minimum supported version of our SDKs to focus on providing the best experience for our developers. Note that attempting to override the `minSdkVersion` to decrease the minimum supported API level won’t work due to internal runtime API level validation.

Existing 2.X versions of the Terminal Android SDK will continue to support devices running **Android 5.0 “Lollipop” (API 21)** and higher.

## Update your DiscoveryConfiguration usage

To support configuration for different discovery methods, the [DiscoveryConfiguration](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-discovery-configuration/index.html) class is now an interface that is implemented by several different sealed subclasses. Instead of providing a DiscoveryMethod, there are now individual classes to choose from to search for a specific type of reader:

| Configuration Class                                                                                                                                                                                          | Usage                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| [BluetoothDiscoveryConfiguration](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-discovery-configuration/-bluetooth-discovery-configuration/index.html)      | Bluetooth-capable readers near this Android device                                                                                         |
| [UsbDiscoveryConfiguration](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-discovery-configuration/-usb-discovery-configuration/index.html)                  | Readers connected by USB to this Android device                                                                                            |
| [InternetDiscoveryConfiguration](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-discovery-configuration/-internet-discovery-configuration/index.html)        | Internet-connected readers registered to this account                                                                                      |
| [LocalMobileDiscoveryConfiguration](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-discovery-configuration/-local-mobile-discovery-configuration/index.html) | [Tap to Pay](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay.md?platform=android) using this Android device’s NFC reader |
| [HandoffDiscoveryConfiguration](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-discovery-configuration/-handoff-discovery-configuration/index.html)          | [Apps on Devices](https://docs.stripe.com/terminal/features/apps-on-devices/overview.md) for Stripe SmartPOS Android Devices               |

## Update your reader discovery to perform runtime permission requests

Previously, the SDK would require Location and Bluetooth permissions to be granted to the application at SDK initialization time, when calling `Terminal.initTerminal()`. This was overly strict and would often require integrations that didn’t connect to Bluetooth readers to still grant the Bluetooth permissions to use the SDK. This requirement has now been relaxed so that permissions are now checked at the time of reader discovery, and only the minimal set of permissions are enforced depending on the `DiscoveryConfiguration`.

Location permissions are still always required, but checking if those permissions have been granted is now delayed until reader discovery for any `DiscoveryConfiguration`. Bluetooth permissions are also now checked at the time of reader discovery, but they’re only required when searching for readers with a `BluetoothDiscoveryConfiguration`.

## Review change in reader connection status when installing required updates

When attempting to connect with Bluetooth or USB to a reader that has required updates, those updates must be applied to allow for the connection to be successfully completed. Previously, your integration’s `TerminalListener.onConnectionStatusChange()` callback would be invoked with `CONNECTED` and `TerminalListener.onPaymentStatusChanged()` would be invoked with `READY` as soon as the connection was established. However, if the reader had any required updates that had to be performed, they would be installed while receiving these callbacks, which would delay the reader from accepting any commands until after they completed.

The reader status will now remain `CONNECTING` while installing any required updates. It’s only after those required updates complete successfully that your integration will be notified the reader is now connected and ready for use.

## Review support for Offline Payments

`PaymentIntent.id` is null for offline payments. If your integration only supports online payments, the `id` will always be present and no changes are needed beyond checks to satisfy the presence of the ID. See [Collect card payments while offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md?terminal-sdk-platform=android) for more details on how to process payments offline.

```kotlin
Terminal.getInstance().createPaymentIntent(
    params,
    object : PaymentIntentCallback {
        override fun onSuccess(paymentIntent: PaymentIntent) {
            val intentId = paymentIntent.id ?: run {
                // PaymentIntent was created offline without an id. See intent.offlineDetails.
                // This is only expected when offline mode is enabled.
            }
        }

        override fun onFailure(e: TerminalException) {
            // Placeholder for handling exception
        }
    }
)
```

## Update your process calls to confirm

`Terminal.processPayment()` is renamed to `Terminal.confirmPaymentIntent()` and `Terminal.processRefund()` is renamed to `Terminal.confirmRefund()`. Only the name of the method is changed, the behavior of these methods remains identical.

## Update usage of Parcelable data models to use Serializable methods

If your integration requires reading and writing Terminal SDK data models to a Parcel, you need to update your `writeParcelable()` and `readParcelable()` calls with `writeSerializable()` and `readSerializable()`.

As with `Parcelable` data models, it recommended to not place any `Serializable` data into persistent storage: changes in the underlying implementation of any of the data in a `Serializable` data model between SDK updates, such as adding new fields, can render older data unreadable.

## Update your readReusableCard usage to SetupIntents

`Terminal.readReusableCard()` is removed. SetupIntents are the recommended path for saving payment details without charging. SetupIntents follow a similar pattern to PaymentIntents where you’ll create, collect, and then confirm the SetupIntent in the SDK. See [Save payment details for online payments](https://docs.stripe.com/terminal/features/saving-payment-details/overview.md) for more details.

## Update usage of renamed or removed Deprecated APIs

A number of deprecated classes, fields, and methods have been removed from the SDK. Most of the APIs that have been removed already have replacement fields that can be read from instead.

- `CaptureMethod.getManual()` is removed. Use `CaptureMethod.MANUAL` instead.
- The `CollectConfiguration` constructor is removed. Use `CollectConfiguration.Builder` instead.
- `CollectConfiguration.moto` is no longer mutable.
- `ConnectConfiguration.registerToLocation` is removed and replaced with `ConnectConfiguration.locationId`.
- The `locationId` parameter from the `HandoffConnectionConfiguration` constructor is removed.
- `BluetoothReaderListener` and `UsbReaderListener` have been removed and replaced with `ReaderListener`.
- `EmvBlob` is marked as an internal class.
- `Reader.device` is removed and replaced with `Reader.bluetoothDevice` and `Reader.usbDevice`.
- `Reader.registeredLocation` is removed and replaced with `Reader.location`.
- `TerminalApplicationDelegate.onTrimMemory()` is removed. It’s automatically managed by the SDK.
- `CardDetails.fingerprint` and `CardPresentDetails.fingerprint` have been removed. You’re still able to access the fingerprint using Stripe [server-side SDKs](https://docs.stripe.com/sdks.md#server-side-libraries).
