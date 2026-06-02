<!-- Source: Stripe Terminal — Collect card payments while offline (iOS, Android, React Native) -->
<!-- Fetched: 2026-04-24 -->

# Collect card payments while offline

Collect card payments when you have internet connectivity issues.

# iOS

> This is a iOS for when terminal-card-present-integration is terminal and terminal-sdk-platform is ios and reader-type is bluetooth. View the full page at https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments?terminal-card-present-integration=terminal&terminal-sdk-platform=ios&reader-type=bluetooth.

The Terminal SDK allows your application to continue collecting payments using a mobile reader without a network connection.

> When operating offline, payment information is collected at the time of sale, and authorization is only attempted after connectivity is restored and the payment is forwarded. You, as the user, assume all decline and tamper-related risks associated with an offline transaction. If your tampered reader can’t forward payments to Stripe, or the issuer declines the transaction, there’s no way to recover the funds, and you might not receive payment from the customer for goods or services already provided.
>
> To reduce the chances of an issuer decline, you’re encouraged to:
>
> - Reestablish internet connectivity as soon as possible to record the payments to Stripe.

- Restrict transactions if they exceed a certain amount.
- [Fail all offline payments](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#managing-risk) if the SDK has stored a set of transactions whose sum exceeds a certain amount.

## Collect payments while offline

Offline payments follow the same steps as online payments: create, collect, process, and capture the payment. Your device can transition from online to offline at any step in the process.

1. [Enable offline mode](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#enable-offline-mode)
1. [Connect to a reader while offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#connect-while-offline)
1. [Handle offline events](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#handle-offline-events)
1. [Create a PaymentIntent while offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#create-payment-intent)
1. [Collect a payment method](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#collect-payment-method)
1. [Confirm the payment](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#confirm-payment)
1. [Wait for payments to forward](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#wait-for-forward)
1. (Optional) [Capture the payment](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#capture-payment)
1. (Optional) [Examine payments collected offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#examine-offline)

## Enable offline mode

To use offline mode, your application needs to consume version `3.3.0` or later of the Terminal iOS SDK.

Use a [Configuration](https://docs.stripe.com/api/terminal/configuration.md) object or [the Dashboard](https://docs.stripe.com/terminal/fleet/configurations-overview.md?dashboard-or-api=dashboard#update-the-default-configuration-for-the-account) to enable offline mode for the [supported](https://docs.stripe.com/terminal/features/operate-offline/overview.md?reader-type=bluetooth#availability) devices at your `Location`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const configuration = await stripe.terminal.configurations.create({
  offline: {
    enabled: true,
  },
});
```

After you enable offline mode on a `Configuration` object, you can [assign it](https://docs.stripe.com/terminal/fleet/configurations-overview.md?dashboard-or-api=api#create-a-configuration-for-an-individual-location) to a `Location`. You can also enable offline mode by default for all `Locations` by updating the [default](https://docs.stripe.com/terminal/fleet/configurations-overview.md?dashboard-or-api=api#retrieve-the-account-default-configuration) `Configuration` object for your account. Configuration API changes can take several minutes to propagate to your SDK and reader, and require you to disconnect from and reconnect to your reader to take effect.

## Connect to a reader while offline

The SDK stores necessary `Location` information locally after connecting online. On subsequent offline connections, it uses the stored configuration information from that `Location`.

To collect payments with a smart reader while offline, you must have previously connected to any mobile reader of the same type at the same `Location` while online within the last 30 days, and have updated your reader’s software within that time.

If you attempt to connect to a reader while offline without meeting these requirements, the request fails with an error.

| Error                                                                                                             | Resolution                                                                                                                                                                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **The SDK isn’t connected to the internet**                                                                       | Make sure the `Location` you’re using is [configured](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#enable-offline-mode) for offline mode. Otherwise, connect to any reader while online, and then connect to a reader of the same type while offline.                                |
| **The selected reader requires a software update before it can be used to collect payments offline.**             | The reader’s software hasn’t been updated in 30 days or more. Connect to the reader while online to update it.                                                                                                                                                                                                             |
| **The selected reader must be paired online at this location before it can be used to collect payments offline.** | You’re attempting to connect to a reader type that your POS hasn’t previously connected to while online. You must first connect to this reader or any reader of the same type while online. Or, if you want to connect while offline, you can connect to a reader type that your POS previously connected to while online. |

If you reinstall the application or perform any operation that clears the disk storage for the SDK (such as clearing your POS app’s cache in the POS device’s settings) you lose any payments that the SDK has stored and not yet forwarded. Make sure there are no stored payments before you perform any destructive action.

## Handle offline events [Client-side]

- [OfflineDelegate (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Protocols/SCPOfflineDelegate.html)

- [NetworkStatus (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Enums/SCPNetworkStatus.html)

To allow your application to receive updates about the SDK’s network status and the state of forwarded payments, implement the `OfflineDelegate` protocol and pass it to the Terminal SDK. You must set `OfflineDelegate` before collecting payments offline.

#### Swift

```swift

import StripeTerminal

class CustomOfflineDelegate: OfflineDelegate {

    func terminal(_ terminal: Terminal, didChangeOfflineStatus offlineStatus: OfflineStatus) {
        // Check the value of `offlineStatus` and update your UI accordingly. For instance,
        // you can check the SDK's network status at `offlineStatus.sdk.networkStatus`.
        //
        // You can also check the SDK's current offline status using
        // `Terminal.shared.offlineStatus.sdk.networkStatus`.
    }

    func terminal(_ terminal: Terminal, didForwardPaymentIntent intent: PaymentIntent, error: Error?) {
        // The PaymentIntent was successfully forwarded, or an error occurred.
        // Reconcile any local state using the backend-generated `PaymentIntent.stripeId`
        // and the metadata you supplied when creating the PaymentIntent.
        //
        // Note that the `PaymentIntent.stripeId` may still be nil if creating the
        // PaymentIntent in the backend failed.
    }

    func terminal(_ terminal: Terminal, didReportForwardingError error: Error) {
        // A non-specific error occurred while forwarding a PaymentIntent.
        // Check the error message and your integration implementation to
        // troubleshoot.
    }
}
```

#### Swift

```swift
import UIKit
import StripeTerminal

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil) -> Bool {
        Terminal.initWithTokenProvider(APIClient.shared)
        Terminal.shared.offlineDelegate = CustomOfflineDelegate()
        // ...
        return true
    }

    // ...

}
```

## Create a PaymentIntent while offline [Client-side]

- [createPaymentIntent (iOS)](<https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)createPaymentIntent:completion:>)
- [CreateConfiguration (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPCreateConfiguration.html)
- [OfflineDetails (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPOfflineDetails.html)

To support operating offline, use the SDK’s `createPaymentIntent` to create PaymentIntent objects. This allows the SDK to create PaymentIntents while offline and forward them to Stripe after you’ve re-established connectivity.

While operating offline, `PaymentIntent` objects have a null `stripeId`. We recommend adding a custom identifier to the PaymentIntent’s [metadata](https://docs.stripe.com/payments/payment-intents.md#storing-information-in-metadata) to help reconcile `PaymentIntent` objects created offline in your database.

After the `PaymentIntent` has been successfully forwarded to Stripe in [Step 7](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#wait-for-forward), use your custom identifier to reconcile it in the `OfflineDelegate.didForwardPaymentIntent` callback.

#### Swift

```swift

import UIKit
import StripeTerminal

class PaymentViewController: UIViewController {

    // Action for a "Checkout" button
    func checkoutAction() throws {
        // Populate the correct transaction amount from your application.
        let amount = UInt(10_00)

        // Build up parameters for creating a `PaymentIntent`
        let params = try PaymentIntentParametersBuilder(
            amount: amount,
            currency: "sgd"
        ).setMetadata(["offlineId": UUID().uuidString])
        .build()

        Terminal.shared.createPaymentIntent(params) { createResult, createError in
            if let error = createError {
                // Handle errors in your application.
                print("createPaymentIntent failed: \(error)")
            } else if let paymentIntent = createResult {
                print("createPaymentIntent succeeded")// If the `PaymentIntent` was created offline, its `stripeId` field will be nil.
                if let onlineCreatedId = paymentIntent.stripeId {
                    print("created online");
                } else {
                    print("created offline")
                }
            }
        }
    }
}
```

The `Terminal.createPaymentIntent` accepts a `CreateConfiguration` parameter. By default, if you’re operating offline, the Terminal SDK stores all offline payments, then forwards them to Stripe’s backend when connectivity is restored.

To customize this behavior, you can pass in a `CreateConfiguration` object with an `offlineBehavior` attribute set to as `REQUIRE_ONLINE`, `PREFER_ONLINE` or `FORCE_OFFLINE`.

#### Managing risk

Setting `offlineBehavior` to `REQUIRE_ONLINE` fails the current transaction if you’re operating offline. For example, you might want to disallow transactions above a certain amount or disallow all offline transactions if the SDK has stored a set of transactions whose sum exceeds a certain amount.

The SDK exposes two properties to help you manage risk:

1. `Terminal.offlineStatus.sdk.offlinePaymentsCount`
1. `Terminal.offlineStatus.sdk.offlinePaymentAmountsByCurrency`

#### Managing latency while offline

Based on your network connectivity, the Terminal SDK automatically determines whether to collect payments online or offline. However, you might want to operate offline despite having an active network connection (for example, if you need to collect transactions quickly and your network connection is slow). You can pass a `CreateConfiguration` object with `offlineBehavior` set to `FORCE_OFFLINE` to collect the payment offline regardless of connectivity.

Payments collected offline while the Terminal SDK has an active network connection are forwarded in the background.

#### Swift

```swift

import UIKit
import StripeTerminal

class PaymentViewController: UIViewController {

    // Action for a "Checkout" button
    func checkoutAction() throws {
        // ...build up parameters and callback for creating a `PaymentIntent`

        // Your app might want to prevent offline payments for too large an amount.
        // Here, we block the payment if the amount is over 1000 sgd.
        // Otherwise, we allow collecting offline if the network connection is unavailable.let offlineBehavior: SCPOfflineBehavior = {
            if amount > UInt(1_000_00) {
                return .requireOnline
            } else {
                return .preferOnline
            }
        }()

        let createConfiguration = try CreateConfigurationBuilder().setOfflineBehavior(offlineBehavior).build()
        Terminal.shared.createPaymentIntent(params, createConfig: createConfiguration) { createResult, createError in
            // handle success or failure
        }
    }
}
```

## Collect a payment method [Client-side]

- [didRequestReaderInput (iOS)](<https://stripe.dev/stripe-terminal-ios/docs/Protocols/SCPReaderDisplayDelegate.html#/c:objc(pl)SCPReaderDisplayDelegate(im)terminal:didRequestReaderInput:>)

- [CollectPaymentIntentConfiguration (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPCollectPaymentIntentConfiguration.html)

> Payment liability is your responsibility when operating your reader offline. Because magnetic stripe data is easy to spoof, Stripe disallows this option while operating offline. Tapping cards is also not supported in markets where _Strong Customer Authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase) is required.

Collecting payments while offline is similar to [collecting payments while online](https://docs.stripe.com/terminal/payments/collect-card-payment.md#collect-payment). Use the `didRequestReaderInput` method to display the valid card presentment options to the customer.

> Readers don’t support [inspecting payment method details before authorization](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=ios#collect-inspect-payment-method) while offline. Although you can still use the `initWithUpdatePaymentIntent` parameter in `CollectPaymentIntentConfiguration`, the `paymentMethod` field on the PaymentIntent is absent if the SDK is operating offline.

#### Swift

```swift

import UIKit
import StripeTerminal

class PaymentViewController: UIViewController {

    // Action for a "Checkout" button
    func checkoutAction() {
        Terminal.shared.collectPaymentMethod(paymentIntent) { collectResult, collectError in
            if let error = collectError {
                print("collectPaymentMethod failed: \(error)")
            }
            else if let paymentIntent = collectResult {
                print("collectPaymentMethod succeeded")
                // ... Confirm the payment
            }
        }
    }
}
```

## Confirm payment [Client-side]

Confirming payments while offline is similar to [confirming payments while online](https://docs.stripe.com/terminal/payments/collect-card-payment.md#confirm-payment). The primary difference is that your integration must handle offline-specific error cases, such as when the transaction exceeds the Stripe-enforced offline maximum of 10,000 USD or equivalent in your operating currency.

In some cases, the SDK might create a `PaymentIntent` online, but confirm it while offline. When this happens, the `PaymentIntent` might have a non-null `stripeId`. If it was confirmed offline, `offlineDetails` will be defined and populated.

#### Swift

```swift


import UIKit
import StripeTerminal

class PaymentViewController: UIViewController {

    // Action for a "Checkout" button
    func checkoutAction() {

        Terminal.shared.confirmPaymentIntent(paymentIntent) { confirmResult, confirmError in
            if let error = confirmError {
                // Handle offline-specific errors in your application (for example,
                // unsupported payment method).
                print("confirmPaymentIntent failed: \(error)")
            } else if let confirmedPaymentIntent= confirmResult {print("confirmPaymentIntent succeeded")
                if let offlineDetails = paymentIntent.offlineDetails {
                    print("confirmed offline");
                } else {
                    print("confirmed online")
                }
            }
        }
    }
}
```

#### Providing receipts

You might require information about the card used to complete a payment while offline. For example, you might need to generate a receipt for customers who require one at the time of purchase.

If the PaymentIntent is confirmed offline, retrieve its [OfflineCardPresentDetails](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPOfflineCardPresentDetails.html) from the `paymentIntent.offlineDetails.offlineCardPresentDetails` property.

This hash contains a [ReceiptDetails](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPReceiptDetails.html) property you can use to generate a receipt, as well as other card details like the cardholder name and card brand.

The `account_type` and `authorization_response_code` receipt fields are unavailable on PaymentIntents processed offline. [Prebuilt email receipts](https://docs.stripe.com/terminal/features/receipts.md#prebuilt) are only sent after connectivity is restored and the payment is successfully captured.

## Wait for payments to forward [Client-side]

When Internet access is restored, the SDK automatically begins forwarding the stored offline payments.

The SDK attempts to forward payments even if its network status is offline. This means your connection token provider might receive a request to provide a connection token even when the device is offline.

If you power off your POS device too soon, your payments might not be forwarded. You can query `Terminal.offlineStatus.sdk.networkStatus` to make sure your POS is online and can forward payments, and `Terminal.offlineStatus.sdk.offlinePaymentsCount` to check how many payments the Terminal SDK has to be forwarded.

## Capture payment

While offline, you can create PaymentIntents with `captureMethod` set to `automatic`.

After you confirm these PaymentIntents, they have a `Succeeded` status instead of `RequiresCapture`. Stripe automatically captures the payments after you forward them.

If you opt for manual capture, payments that are successfully forwarded and authorized require capture from your backend or application.

- To capture payments from your backend, use [webhooks](https://docs.stripe.com/webhooks.md) to listen for PaymentIntents with a `requires_capture` status.
- To capture payments from your application, wait for your application to receive calls to `OfflineDelegate.didForwardPayment` for each PaymentIntent as the SDK forwards it. A PaymentIntent is ready to capture if its status is `RequiresCapture` and the `offlineDetails` is null or has a `requiresUpload` value of `NO` .

#### Swift

```swift

Terminal.shared.confirmPaymentIntent(paymentIntent) { confirmResult, confirmError in
    if let error = confirmError {
        // Handle offline-specific errors in your application (for example,
        // unsupported payment method).
        print("confirmPaymentIntent failed: \(error)")
    } else if let confirmedPaymentIntent = confirmResult {
        if intent.status == .requiresCapture {if let offlineDetails = confirmedPaymentIntent.offlineDetails(),
               offlineDetails.requiresUpload {
                // Offline payment, wait for `didForwardPaymentIntent` (see snippet below)
            } else {
                // Online payment, can be captured now
            }
        }
        // else, handle other intent.status results here
    }
}
```

Capture an offline payment after the SDK forwards it in your OfflineDelegate’s `didForwardPaymentIntent`:

#### Swift

```swift

import StripeTerminal

class CustomOfflineDelegate: OfflineDelegate {
    // ...
    func terminal(_ terminal: Terminal, didForwardPaymentIntent intent: PaymentIntent, error: Error?) {
        if let error = error {
            // Handle the error appropriate for your application
            return
        }

        if intent.status == .requiresCapture {
            // The intent is ready to be captured.
        } else {
            // Handle the intent.status as appropriate.
        }
    }
    // ...
}
```

## Examine payments collected offline

After authorization, you can use the [PaymentIntents](https://docs.stripe.com/payments/payment-intents.md) API to examine offline details on a payment. Access the [payment method details](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-offline) on the [latest Charge](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-latest_charge) object on a `PaymentIntent` to determine if it was collected offline.

# Android

> This is a Android for when terminal-card-present-integration is terminal and terminal-sdk-platform is android and reader-type is bluetooth. View the full page at https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments?terminal-card-present-integration=terminal&terminal-sdk-platform=android&reader-type=bluetooth.

The Terminal SDK allows your application to continue collecting payments using a mobile reader without a network connection.

> When operating offline, payment information is collected at the time of sale, and authorization is only attempted after connectivity is restored and the payment is forwarded. You, as the user, assume all decline and tamper-related risks associated with an offline transaction. If your tampered reader can’t forward payments to Stripe, or the issuer declines the transaction, there’s no way to recover the funds, and you might not receive payment from the customer for goods or services already provided.
>
> To reduce the chances of an issuer decline, you’re encouraged to:
>
> - Reestablish internet connectivity as soon as possible to record the payments to Stripe.

- Restrict transactions if they exceed a certain amount.
- [Fail all offline payments](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#managing-risk) if the SDK has stored a set of transactions whose sum exceeds a certain amount.

## Collect payments while offline

Offline payments follow the same steps as online payments: create, collect, process, and capture the payment. Your device can transition from online to offline at any step in the process.

1. [Enable offline mode](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#enable-offline-mode)
1. [Connect to a reader while offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#connect-while-offline)
1. [Handle offline events](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#handle-offline-events)
1. [Create a PaymentIntent while offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#create-payment-intent)
1. [Collect a payment method](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#collect-payment-method)
1. [Confirm the payment](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#confirm-payment)
1. [Wait for payments to forward](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#wait-for-forward)
1. (Optional) [Capture the payment](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#capture-payment)
1. (Optional) [Examine payments collected offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#examine-offline)

## Enable offline mode

To use offline mode, your application needs to consume version `3.2.0` or later of the Terminal Android SDK.

Use a [Configuration](https://docs.stripe.com/api/terminal/configuration.md) object or [the Dashboard](https://docs.stripe.com/terminal/fleet/configurations-overview.md?dashboard-or-api=dashboard#update-the-default-configuration-for-the-account) to enable offline mode for the [supported](https://docs.stripe.com/terminal/features/operate-offline/overview.md?reader-type=bluetooth#availability) devices at your `Location`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const configuration = await stripe.terminal.configurations.create({
  offline: {
    enabled: true,
  },
});
```

After you enable offline mode on a `Configuration` object, you can [assign it](https://docs.stripe.com/terminal/fleet/configurations-overview.md?dashboard-or-api=api#create-a-configuration-for-an-individual-location) to a `Location`. You can also enable offline mode by default for all `Locations` by updating the [default](https://docs.stripe.com/terminal/fleet/configurations-overview.md?dashboard-or-api=api#retrieve-the-account-default-configuration) `Configuration` object for your account. Configuration API changes can take several minutes to propagate to your SDK and reader, and require you to disconnect from and reconnect to your reader to take effect.

## Connect to a reader while offline

The SDK stores necessary `Location` information locally after connecting online. On subsequent offline connections, it uses the stored configuration information from that `Location`.

To collect payments with a smart reader while offline, you must have previously connected to any mobile reader of the same type at the same `Location` while online within the last 30 days, and have updated your reader’s software within that time.

If you attempt to connect to a reader while offline without meeting these requirements, the request fails with an error.

| Error                                                                                                             | Resolution                                                                                                                                                                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **The SDK isn’t connected to the internet**                                                                       | Make sure the `Location` you’re using is [configured](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#enable-offline-mode) for offline mode. Otherwise, connect to any reader while online, and then connect to a reader of the same type while offline.                                |
| **The selected reader requires a software update before it can be used to collect payments offline.**             | The reader’s software hasn’t been updated in 30 days or more. Connect to the reader while online to update it.                                                                                                                                                                                                             |
| **The selected reader must be paired online at this location before it can be used to collect payments offline.** | You’re attempting to connect to a reader type that your POS hasn’t previously connected to while online. You must first connect to this reader or any reader of the same type while online. Or, if you want to connect while offline, you can connect to a reader type that your POS previously connected to while online. |

If you reinstall the application or perform any operation that clears the disk storage for the SDK (such as clearing your POS app’s cache in the POS device’s settings) you lose any payments that the SDK has stored and not yet forwarded. Make sure there are no stored payments before you perform any destructive action.

## Handle offline events [Client-side]

- [OfflineListener (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.callable/-offline-listener/index.html)

- [NetworkStatus (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-network-status/index.html)

To allow your application to receive updates about the SDK’s network status and the state of forwarded payments, implement the `OfflineListener` interface and pass it to the Terminal SDK. You must set `OfflineListener` before collecting payments offline.

#### Kotlin

```kotlin
class CustomOfflineListener : OfflineListener {
    override fun onOfflineStatusChange(offlineStatus: OfflineStatus) {
        // Check the value of `offlineStatus` and update your UI accordingly. For instance,
        // you can check the SDK's network status at `offlineStatus.sdk.networkStatus`.
        //
        // You can also check the SDK's current offline status using
        // `Terminal::offlineStatus`.
    }

    override fun onPaymentIntentForwarded(paymentIntent: PaymentIntent, e: TerminalException?) {
        // The PaymentIntent was successfully forwarded, or an error occurred.
        // Reconcile any local state using the backend-generated `PaymentIntent::id`
        // and the metadata you supplied when creating the PaymentIntent.
        //
        // Note that the `PaymentIntent::id` may still be null if creating the
        // PaymentIntent in the backend failed.
    }

    override fun onForwardingFailure(e: TerminalException) {
        // A non-specific error occurred while forwarding a PaymentIntent.
        // Check the error message and your integration implementation to
        // troubleshoot.
    }
}
```

#### Kotlin

```kotlin
Terminal.init(
    context = applicationContext,
    logLevel = LogLevel.VERBOSE,
    tokenProvider = CustomConnectionTokenProvider(),
    listener = CustomTerminalListener(),
    offlineListener = CustomOfflineListener(),
)
```

## Create a PaymentIntent while offline [Client-side]

- [createPaymentIntent (Android)](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/create-payment-intent.html)
- [CreateConfiguration (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-create-configuration/index.html)
- [OfflineDetails (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-offline-details/index.html)

To support operating offline, use the SDK’s `createPaymentIntent` to create PaymentIntent objects. This allows the SDK to create PaymentIntents while offline and forward them to Stripe after you’ve re-established connectivity.

While operating offline, `PaymentIntent` objects have a null `id`. We recommend adding a custom identifier to the PaymentIntent’s [metadata](https://docs.stripe.com/payments/payment-intents.md#storing-information-in-metadata) to help reconcile `PaymentIntent` objects created offline in your database.

After the `PaymentIntent` has been successfully forwarded to Stripe in [Step 7](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#wait-for-forward), use your custom identifier to reconcile it in the `OfflineListener::onPaymentIntentForwarded` callback.

#### Kotlin

```kotlin
private const val TAG = "PaymentActivity"

class PaymentActivity : AppCompatActivity() {
    // Action for a "Checkout" button
    private fun onCheckout(cart: Cart) {
        // Build up parameters for creating a `PaymentIntent`
        val params = PaymentIntentParameters.Builder()
            .setAmount(cart.total)
            .setCurrency(cart.currency).setMetadata(mapOf("unique-id" to UUID.randomUUID().toString()))
            .build()

        val createPaymentCallback: PaymentIntentCallback = object : PaymentIntentCallback {
            override fun onSuccess(paymentIntent: PaymentIntent) {
                Log.d(TAG, "createPaymentIntent succeeded")// If the `PaymentIntent` was created offline, its `id` field will be null.
                if (paymentIntent.id != null) {
                    Log.d(TAG, "created online")
                } else {
                    Log.d(TAG, "created offline")
                }
                // ... Collect a PaymentMethod
            }

            override fun onFailure(e: TerminalException) {
                Log.e(TAG, "createPaymentIntent failed", e)
                // Handle errors in your application.
            }
        }
        Terminal.getInstance().createPaymentIntent(params, createPaymentCallback)
    }
}
```

The `Terminal.createPaymentIntent` accepts a `CreateConfiguration` parameter. By default, if you’re operating offline, the Terminal SDK stores all offline payments, then forwards them to Stripe’s backend when connectivity is restored.

To customize this behavior, you can pass in a `CreateConfiguration` object with an `offlineBehavior` attribute set to as `REQUIRE_ONLINE`, `PREFER_ONLINE` or `FORCE_OFFLINE`.

#### Managing risk

Setting `offlineBehavior` to `REQUIRE_ONLINE` fails the current transaction if you’re operating offline. For example, you might want to disallow transactions above a certain amount or disallow all offline transactions if the SDK has stored a set of transactions whose sum exceeds a certain amount.

The SDK exposes two properties to help you manage risk:

1. `Terminal.offlineStatus.sdk.offlinePaymentsCount`
1. `Terminal.offlineStatus.sdk.offlinePaymentAmountsByCurrency`

#### Managing latency while offline

Based on your network connectivity, the Terminal SDK automatically determines whether to collect payments online or offline. However, you might want to operate offline despite having an active network connection (for example, if you need to collect transactions quickly and your network connection is slow). You can pass a `CreateConfiguration` object with `offlineBehavior` set to `FORCE_OFFLINE` to collect the payment offline regardless of connectivity.

Payments collected offline while the Terminal SDK has an active network connection are forwarded in the background.

#### Kotlin

```kotlin
private const val TAG = "PaymentActivity"

class PaymentActivity : AppCompatActivity() {
    // Action for a "Checkout" button
    private fun onCheckout(cart: Cart) {
        // ...build up parameters and callback for creating a `PaymentIntent`

        // Your app might want to prevent offline payments for too large an amount.
        // Here, we require a network connection if the payment if the amount is over 1000 sgd.
        // Otherwise, we allow collecting offline if the network connection is unavailable.val offlineBehavior = if (cart.total > 1000000) {
            OfflineBehavior.REQUIRE_ONLINE
        } else {
            OfflineBehavior.PREFER_ONLINE
        }
        val createConfig = CreateConfiguration(offlineBehavior)

        Terminal.getInstance().createPaymentIntent(params, createPaymentCallback, createConfig)
    }
}
```

## Collect a payment method [Client-side]

- [onRequestReaderInput (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.callable/-reader-listener/on-request-reader-input.html)

- [CollectPaymentIntentConfiguration (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-collect-payment-intent-configuration/index.html)

> Payment liability is your responsibility when operating your reader offline. Because magnetic stripe data is easy to spoof, Stripe disallows this option while operating offline. Tapping cards is also not supported in markets where _Strong Customer Authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase) is required.

Collecting payments while offline is similar to [collecting payments while online](https://docs.stripe.com/terminal/payments/collect-card-payment.md#collect-payment). Use the `onRequestReaderInput` method to display the valid card presentment options to the customer.

> Readers don’t support [inspecting payment method details before authorization](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=android#collect-inspect-payment-method) while offline. Although you can still set the `updatePaymentIntent` parameter in `CollectPaymentIntentConfiguration`, the `paymentMethod` field on the PaymentIntent is absent if the SDK is operating offline.

#### Kotlin

```kotlin
private const val TAG = "PaymentActivity"

class PaymentActivity : AppCompatActivity() {
    // Action for a "Checkout" button
    private fun onCheckout(cart: Cart) {
        val collectPaymentCallback: PaymentIntentCallback = object : PaymentIntentCallback {
            override fun onSuccess(paymentIntent: PaymentIntent) {
                Log.d(TAG, "collectPaymentMethod succeeded")
                // ... Confirm the payment
            }

            override fun onFailure(e: TerminalException) {
                Log.d(TAG, "collectPaymentMethod failed:", e)
            }
        }
        val collectConfig = CollectPaymentIntentConfiguration.Builder().build()
        Terminal.getInstance().collectPaymentMethod(paymentIntent, collectPaymentCallback, collectConfig)
    }
}
```

## Confirm payment [Client-side]

Confirming payments while offline is similar to [confirming payments while online](https://docs.stripe.com/terminal/payments/collect-card-payment.md#confirm-payment). The primary difference is that your integration must handle offline-specific error cases, such as when the transaction exceeds the Stripe-enforced offline maximum of 10,000 USD or equivalent in your operating currency.

In some cases, the SDK might create a `PaymentIntent` online, but confirm it while offline. When this happens, the `PaymentIntent` might have a non-null `id`. If it was confirmed offline, `offlineDetails` will be defined and populated.

#### Kotlin

```kotlin
private const val TAG = "PaymentActivity"

class PaymentActivity : AppCompatActivity() {
    // Action for a "Checkout" button
    private fun onCheckout(cart: Cart) {
        val confirmPaymentIntentCallback: PaymentIntentCallback = object : PaymentIntentCallback {
            override fun onSuccess(paymentIntent: PaymentIntent) {
                Log.d(TAG, "confirmPaymentIntent succeeded")// If the `PaymentIntent` was confirmed offline, `paymentIntent.offlineDetails` will be defined
                if (paymentIntent.offlineDetails != null) {
                    Log.d(TAG, "confirmed offline")
                } else {
                    Log.d(TAG, "confirmed online")
                }
            }

            override fun onFailure(e: TerminalException) {
                // Handle offline-specific errors in your application (for example,
                // unsupported payment method).
                Log.e(TAG, "confirmPaymentIntent failed:", e)
            }
        }
        Terminal.getInstance().confirmPaymentIntent(paymentIntent, confirmPaymentIntentCallback)
    }
}
```

#### Providing receipts

You might require information about the card used to complete a payment while offline. For example, you might need to generate a receipt for customers who require one at the time of purchase.

If the PaymentIntent is confirmed offline, retrieve its [OfflineCardPresentDetails](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-offline-card-present-details/index.html) from the `paymentIntent.offlineDetails.offlineCardPresentDetails` property.

This hash contains a [ReceiptDetails](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-receipt-details/index.html) property you can use to generate a receipt, as well as other card details like the cardholder name and card brand.

The `account_type` and `authorization_response_code` receipt fields are unavailable on PaymentIntents processed offline. [Prebuilt email receipts](https://docs.stripe.com/terminal/features/receipts.md#prebuilt) are only sent after connectivity is restored and the payment is successfully captured.

## Wait for payments to forward [Client-side]

When Internet access is restored, the SDK automatically begins forwarding the stored offline payments.

The SDK attempts to forward payments even if its network status is offline. This means your connection token provider might receive a request to provide a connection token even when the device is offline.

If you power off your POS device too soon, your payments might not be forwarded. You can query `Terminal.offlineStatus.sdk.networkStatus` to make sure your POS is online and can forward payments, and `Terminal.offlineStatus.sdk.offlinePaymentsCount` to check how many payments the Terminal SDK has to be forwarded.

## Capture payment

While offline, you can create PaymentIntents with `captureMethod` set to `automatic`.

After you confirm these PaymentIntents, they have a `SUCCEEDED` status instead of `REQUIRES_CAPTURE` . Stripe automatically captures the payments after you forward them.

If you opt for manual capture, payments that are successfully forwarded and authorized require capture from your backend or application.

- To capture payments from your backend, use [webhooks](https://docs.stripe.com/webhooks.md) to listen for PaymentIntents with a `requires_capture` status.
- To capture payments from your application, wait for your application to receive calls to `OfflineListener::onPaymentIntentForwarded` for each PaymentIntent as the SDK forwards it. A PaymentIntent is ready to capture if its status is `REQUIRES_CAPTURE` and the `offlineDetails` is null or has a `requiresUpload` value of `false` .

#### Kotlin

```kotlin
private const val TAG = "PaymentActivity"

class PaymentActivity : AppCompatActivity() {
    // Action for a "Checkout" button
    private fun onCheckout(cart: Cart) {
        val callback: PaymentIntentCallback = object : PaymentIntentCallback {
            override fun onSuccess(paymentIntent: PaymentIntent) {
                Log.d(TAG, "confirmPaymentIntent succeeded")
                if (paymentIntent.status == PaymentIntentStatus.REQUIRES_CAPTURE) {val offlineDetails = paymentIntent.offlineDetails
                    if (offlineDetails?.requiresUpload == true) {
                        // Offline payment, wait for `onPaymentIntentForwarded` (see snippet below)
                    } else {
                        // Online payment, can be captured now
                    }
                } else {
                    // Handle other status results here
                }
            }

            override fun onFailure(e: TerminalException) {
                // Handle offline-specific errors in your application (for example,
                // unsupported payment method).
                Log.e(TAG, "confirmPaymentIntent failed:", e)
            }
        }

        Terminal.getInstance().confirmPaymentIntent(paymentIntent, callback)
    }
}
```

Capture an offline payment after the SDK forwards it in your `OfflineListener::onPaymentIntentForwarded`:

#### Kotlin

```kotlin
class CustomOfflineListener : OfflineListener {
    // ...

    override fun onPaymentIntentForwarded(paymentIntent: PaymentIntent, e: TerminalException?) {
        if (e != null) {
            // Handle the error appropriate for your application
        } else if (paymentIntent.status == PaymentIntentStatus.REQUIRES_CAPTURE) {
            // The paymentIntent is ready to be captured
        } else {
            // Handle other status results here
        }
    }

    // ...
}
```

## Examine payments collected offline

After authorization, you can use the [PaymentIntents](https://docs.stripe.com/payments/payment-intents.md) API to examine offline details on a payment. Access the [payment method details](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-offline) on the [latest Charge](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-latest_charge) object on a `PaymentIntent` to determine if it was collected offline.

# React Native

> This is a React Native for when terminal-card-present-integration is terminal and terminal-sdk-platform is react-native and reader-type is bluetooth. View the full page at https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments?terminal-card-present-integration=terminal&terminal-sdk-platform=react-native&reader-type=bluetooth.

The Terminal SDK allows your application to continue collecting payments using a mobile reader without a network connection.

> When operating offline, payment information is collected at the time of sale, and authorization is only attempted after connectivity is restored and the payment is forwarded. You, as the user, assume all decline and tamper-related risks associated with an offline transaction. If your tampered reader can’t forward payments to Stripe, or the issuer declines the transaction, there’s no way to recover the funds, and you might not receive payment from the customer for goods or services already provided.
>
> To reduce the chances of an issuer decline, you’re encouraged to:
>
> - Reestablish internet connectivity as soon as possible to record the payments to Stripe.

- Restrict transactions if they exceed a certain amount.
- [Fail all offline payments](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#managing-risk) if the SDK has stored a set of transactions whose sum exceeds a certain amount.

## Collect payments while offline

Offline payments follow the same steps as online payments: create, collect, process, and capture the payment. Your device can transition from online to offline at any step in the process.

1. [Enable offline mode](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#enable-offline-mode)
1. [Connect to a reader while offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#connect-while-offline)
1. [Handle offline events](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#handle-offline-events)
1. [Create a PaymentIntent while offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#create-payment-intent)
1. [Collect a payment method](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#collect-payment-method)
1. [Confirm the payment](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#confirm-payment)
1. [Wait for payments to forward](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#wait-for-forward)
1. (Optional) [Capture the payment](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#capture-payment)
1. (Optional) [Examine payments collected offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#examine-offline)

## Enable offline mode

Use a [Configuration](https://docs.stripe.com/api/terminal/configuration.md) object or [the Dashboard](https://docs.stripe.com/terminal/fleet/configurations-overview.md?dashboard-or-api=dashboard#update-the-default-configuration-for-the-account) to enable offline mode for the [supported](https://docs.stripe.com/terminal/features/operate-offline/overview.md?reader-type=bluetooth#availability) devices at your `Location`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const configuration = await stripe.terminal.configurations.create({
  offline: {
    enabled: true,
  },
});
```

After you enable offline mode on a `Configuration` object, you can [assign it](https://docs.stripe.com/terminal/fleet/configurations-overview.md?dashboard-or-api=api#create-a-configuration-for-an-individual-location) to a `Location`. You can also enable offline mode by default for all `Locations` by updating the [default](https://docs.stripe.com/terminal/fleet/configurations-overview.md?dashboard-or-api=api#retrieve-the-account-default-configuration) `Configuration` object for your account. Configuration API changes can take several minutes to propagate to your SDK and reader, and require you to disconnect from and reconnect to your reader to take effect.

## Connect to a reader while offline

The SDK stores necessary `Location` information locally after connecting online. On subsequent offline connections, it uses the stored configuration information from that `Location`.

To collect payments with a smart reader while offline, you must have previously connected to any mobile reader of the same type at the same `Location` while online within the last 30 days, and have updated your reader’s software within that time.

If you attempt to connect to a reader while offline without meeting these requirements, the request fails with an error.

| Error                                                                                                             | Resolution                                                                                                                                                                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **The SDK isn’t connected to the internet**                                                                       | Make sure the `Location` you’re using is [configured](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#enable-offline-mode) for offline mode. Otherwise, connect to any reader while online, and then connect to a reader of the same type while offline.                                |
| **The selected reader requires a software update before it can be used to collect payments offline.**             | The reader’s software hasn’t been updated in 30 days or more. Connect to the reader while online to update it.                                                                                                                                                                                                             |
| **The selected reader must be paired online at this location before it can be used to collect payments offline.** | You’re attempting to connect to a reader type that your POS hasn’t previously connected to while online. You must first connect to this reader or any reader of the same type while online. Or, if you want to connect while offline, you can connect to a reader type that your POS previously connected to while online. |

If you reinstall the application or perform any operation that clears the disk storage for the SDK (such as clearing your POS app’s cache in the POS device’s settings) you lose any payments that the SDK has stored and not yet forwarded. Make sure there are no stored payments before you perform any destructive action.

## Handle offline events [Client-side]

- [UserCallbacks (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/index.html#UserCallbacks)

- [OfflineStatus (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/index.html#OfflineStatus)

To allow your application to receive updates about the SDK’s network status and the state of forwarded payments, implement the offline callbacks on the `useStripeTerminal` hook.

```js
const { connectReader, disconnectReader, connectedReader } = useStripeTerminal({
    onDidChangeOfflineStatus(status: OfflineStatus) {
       // Check the value of `offlineStatus` and update your UI accordingly.
       //
       // You can also check the SDK's current offline status calling
       // `getOfflineStatus`.
    },
    onDidForwardingFailure(error) {
       // A non-specific error occurred while forwarding a PaymentIntent.
       // Check the error message and your integration implementation to
       // troubleshoot.
    },
    onDidForwardPaymentIntent(paymentIntent, error) {
       // The PaymentIntent was successfully forwarded, or an error occurred.
       // Reconcile any local state using the backend-generated `paymentIntent.id`
       // and the metadata you supplied when creating the PaymentIntent.
       //
       // Note that the `paymentIntent.id` may still be null if creating the
       // PaymentIntent in the backend failed.
    },
  });
```

## Create a PaymentIntent while offline [Client-side]

- [createPaymentIntent (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#createPaymentIntent)
- [CreatePaymentIntentParams (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/index.html#CreatePaymentIntentParams)
- [OfflineStatus (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/index.html#OfflineStatus)
- [OfflineStatusDetails (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/index.html#OfflineStatusDetails)

To support operating offline, use the SDK’s `createPaymentIntent` to create PaymentIntent objects. This allows the SDK to create PaymentIntents while offline and forward them to Stripe after you’ve re-established connectivity.

While operating offline, `PaymentIntent` objects have a null `id`. We recommend adding a custom identifier to the PaymentIntent’s [metadata](https://docs.stripe.com/payments/payment-intents.md#storing-information-in-metadata) to help reconcile `PaymentIntent` objects created offline in your database.

After the `PaymentIntent` has been successfully forwarded to Stripe in [Step 7](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#wait-for-forward), use your custom identifier to reconcile it in the `onDidForwardPaymentIntent` callback.

```js
const _createPaymentIntent = async (cart) => {
  const { error, paymentIntent } = await createPaymentIntent({
    amount: cart.total,
    currency: cart.currency,
    metadata: {
      "unique-id": UUID().uuidString,
    },
  });
};
```

The `Terminal.createPaymentIntent` accepts a `CreateConfiguration` parameter. By default, if you’re operating offline, the Terminal SDK stores all offline payments, then forwards them to Stripe’s backend when connectivity is restored.

To customize this behavior, you can pass in a `CreateConfiguration` object with an `offlineBehavior` attribute set to as `REQUIRE_ONLINE`, `PREFER_ONLINE` or `FORCE_OFFLINE`.

#### Managing risk

Setting `offlineBehavior` to `REQUIRE_ONLINE` fails the current transaction if you’re operating offline. For example, you might want to disallow transactions above a certain amount or disallow all offline transactions if the SDK has stored a set of transactions whose sum exceeds a certain amount.

The SDK exposes two properties to help you manage risk:

1. `OfflineStatus.sdk.offlinePaymentsCount`
1. `OfflineStatus.sdk.offlinePaymentAmountsByCurrency`

#### Managing latency while offline

Based on your network connectivity, the Terminal SDK automatically determines whether to collect payments online or offline. However, you might want to operate offline despite having an active network connection (for example, if you need to collect transactions quickly and your network connection is slow). You can set `offlineBehavior` to `force_offline` to collect the payment offline regardless of connectivity.

Payments collected offline while the Terminal SDK has an active network connection are forwarded in the background.

```js
const _createPaymentIntent = async (cart) => {
  // Your app might want to prevent offline payments for too large an amount.
  // Here, we require a network connection if the payment if the amount is over 1000 usd.
  // Otherwise, we allow collecting offline if the network connection is unavailable.let offlineBehavior:
  if (cart.total > 1000000) {
    offlineBehavior = "require_online";
  } else {
    offlineBehavior = "prefer_online";
  }

  const { error, paymentIntent } = await createPaymentIntent({
    amount: cart.total,
    currency: cart.currency,
    offlineBehavior,
  });
};
```

## Collect a payment method [Client-side]

- [UserCallbacks (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/index.html#UserCallbacks)

- [CollectPaymentMethodParams (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/index.html#CollectPaymentMethodParams)

> Payment liability is your responsibility when operating your reader offline. Because magnetic stripe data is easy to spoof, Stripe disallows this option while operating offline. Tapping cards is also not supported in markets where _Strong Customer Authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase) is required.

Collecting payments while offline is similar to [collecting payments while online](https://docs.stripe.com/terminal/payments/collect-card-payment.md#collect-payment). Use the method to display the valid card presentment options to the customer.

> [Inspecting payment method details before authorization](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=react-native#collect-inspect-payment-method) isn’t supported while offline. Although you can still set the `updatePaymentIntent` parameter in `CollectConfiguration`, the `paymentMethod` field on the PaymentIntent is absent if the SDK is operating offline.

```js
const _collectPaymentMethod_ = async () => {
  const { paymentIntent, error } = await collectPaymentMethod({
    paymentIntent: paymentIntent,
  });

  if (error) {
    // Handle errors in your application.
  }

  // ... Confirm the payment
};
```

## Confirm payment [Client-side]

Confirming payments while offline is similar to [confirming payments while online](https://docs.stripe.com/terminal/payments/collect-card-payment.md#confirm-payment). The primary difference is that your integration must handle offline-specific error cases, such as when the transaction exceeds the Stripe-enforced offline maximum of 10,000 USD or equivalent in your operating currency.

In some cases, the SDK might create a `PaymentIntent` online, but confirm it while offline. When this happens, the `PaymentIntent` might have a non-null `id`. If it was confirmed offline, `offlineDetails` will be defined and populated.

```js
const _confirmPaymentIntent = async () => {
  const { paymentIntent, error } = await confirmPaymentIntent({
    paymentIntent: paymentIntent,
  });

  if (error) {
    // Handle offline-specific errors in your application (for example,
    // unsupported payment method).
  }
  if (paymentIntent.offlineDetails) {
    console.log("confirmed offline");
  } else {
    console.log("confirmed online");
  }
};
```

#### Providing receipts

You might require information about the card used to complete a payment while offline. For example, you might need to generate a receipt for customers who require one at the time of purchase.

If the PaymentIntent is confirmed offline, retrieve its [OfflineCardPresentDetails](https://stripe.dev/stripe-terminal-react-native/api-reference/index.html#OfflineCardPresentDetails) from the `paymentIntent.offlineDetails.offlineCardPresentDetails` property.

This hash contains a [ReceiptDetails](https://stripe.dev/stripe-terminal-react-native/api-reference/index.html#ReceiptDetails) property you can use to generate a receipt, as well as other card details like the cardholder name and card brand.

The `account_type` and `authorization_response_code` receipt fields are unavailable on PaymentIntents processed offline. [Prebuilt email receipts](https://docs.stripe.com/terminal/features/receipts.md#prebuilt) are only sent after connectivity is restored and the payment is successfully captured.

## Wait for payments to forward [Client-side]

When Internet access is restored, the SDK automatically begins forwarding the stored offline payments.

The SDK attempts to forward payments even if its network status is offline. This means your connection token provider might receive a request to provide a connection token even when the device is offline.

If you power off your POS device too soon, your payments might not be forwarded. You can query `OfflineStatus.sdk.networkStatus` to make sure your POS is online and can forward payments, and `OfflineStatus.sdk.offlinePaymentsCount` to check how many payments the Terminal SDK has to be forwarded.

## Capture payment

While offline, you can create PaymentIntents with `captureMethod` set to `automatic`.

After you confirm these PaymentIntents, they have a `succeeded` status instead of `requiresCapture` . Stripe automatically captures the payments after you forward them.

If you opt for manual capture, payments that are successfully forwarded and authorized require capture from your backend or application.

- To capture payments from your backend, use [webhooks](https://docs.stripe.com/webhooks.md) to listen for PaymentIntents with a `requires_capture` status.
- To capture payments from your application, wait for your application to receive calls to `useStripeTerminal` hook’s `onDidForwardPaymentIntent` for each PaymentIntent as the SDK forwards it. A PaymentIntent is ready to capture if its status is `requiresCapture` and the `OfflineDetails` is null or has a `requiresUpload` value of `false` .

```js
const _confirmPaymentIntent = async () => {
  const { paymentIntent, error } = await confirmPaymentIntent({
    paymentIntent: paymentIntent,
  });

  if (error) {
    // Handle offline-specific errors in your application (for example,
    // unsupported payment method).
  }

  if (paymentIntent.status == "requiresCapture") {
    const offlineDetails = paymentIntent.offlineDetails;
    if (offlineDetails.requiresUpload === true) {
      // Offline payment, wait for `onDidForwardPaymentIntent` (see snippet below)
    } else {
      // Online payment, can be captured now
    }
  } else {
    // handle other paymentIntent.status results here
  }
};
```

Capture an offline payment after the SDK forwards it in `onDidForwardPaymentIntent`:

```js
const { connectReader, disconnectReader, connectedReader } = useStripeTerminal({
  onDidForwardPaymentIntent(paymentIntent, error) {
    if (error) {
      // Handle the error appropriate for your application
    } else if (paymentIntent.status == "requires_capture") {
      // The paymentIntent is ready to be captured
    } else {
      // Handle the paymentIntent.status as appropriate.
    }
  },
});
```

## Examine payments collected offline

After authorization, you can use the [PaymentIntents](https://docs.stripe.com/payments/payment-intents.md) API to examine offline details on a payment. Access the [payment method details](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-offline) on the [latest Charge](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-latest_charge) object on a `PaymentIntent` to determine if it was collected offline.

# iOS

> This is a iOS for when terminal-card-present-integration is terminal and terminal-sdk-platform is ios and reader-type is internet. View the full page at https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments?terminal-card-present-integration=terminal&terminal-sdk-platform=ios&reader-type=internet.

The Terminal SDK allows your application to continue collecting payments using a smart reader without an Internet connection.

If you’re using a separate POS device with a Stripe smart reader, you still need a functioning local network to allow your POS device to communicate with the smart reader. Operating offline with smart readers is for scenarios where your POS and reader can’t communicate with Stripe, such as during an ISP outage. If you need to operate offline without a local network, consider Stripe Terminal’s [mobile readers](https://docs.stripe.com/terminal/mobile-readers.md).

You can also operate offline with an Apps on Devices integration. Since your POS application runs directly on the smart reader, you don’t need a local network to collect payments. However, you still need to be on a local network when your reader first boots up, even if the network doesn’t have access to the Internet.

> When operating offline, payment information is collected at the time of sale, and authorization is only attempted after connectivity is restored and the payment is forwarded. When operating offline with an Internet reader, the reader stores collected payment information. You, as the user, assume all decline and tamper-related risks associated with an offline transaction. If your tampered reader can’t forward payments to Stripe, or the issuer declines the transaction, there’s no way to recover the funds, and you might not receive payment from the customer for goods or services already provided.
>
> To reduce the chances of an issuer decline, you’re encouraged to:
>
> - Reestablish internet connectivity as soon as possible to record the payments to Stripe.

- Restrict transactions if they exceed a certain amount.
- [Fail all offline payments](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#managing-risk) if the SDK has stored a set of transactions whose sum exceeds a certain amount.

## Collect payments while offline

Offline payments follow the same steps as online payments: create, collect, process, and capture the payment. Your device can transition from online to offline at any step in the process.

1. [Enable offline mode](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#enable-offline-mode)
1. [Connect to a reader while offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#connect-while-offline)
1. [Handle offline events](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#handle-offline-events)
1. [Create a PaymentIntent while offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#create-payment-intent)
1. [Collect a payment method](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#collect-payment-method)
1. [Confirm the payment](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#confirm-payment)
1. [Wait for payments to forward](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#wait-for-forward)
1. (Optional) [Capture the payment](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#capture-payment)
1. (Optional) [Examine payments collected offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#examine-offline)

## Enable offline mode

To use offline mode, your application needs to consume version `3.3.0` or later of the Terminal iOS SDK.

Use a [Configuration](https://docs.stripe.com/api/terminal/configuration.md) object or [the Dashboard](https://docs.stripe.com/terminal/fleet/configurations-overview.md?dashboard-or-api=dashboard#update-the-default-configuration-for-the-account) to enable offline mode for the [supported](https://docs.stripe.com/terminal/features/operate-offline/overview.md?reader-type=internet#availability) devices at your `Location`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const configuration = await stripe.terminal.configurations.create({
  offline: {
    enabled: true,
  },
});
```

After you enable offline mode on a `Configuration` object, you can [assign it](https://docs.stripe.com/terminal/fleet/configurations-overview.md?dashboard-or-api=api#create-a-configuration-for-an-individual-location) to a `Location`. You can also enable offline mode by default for all `Locations` by updating the [default](https://docs.stripe.com/terminal/fleet/configurations-overview.md?dashboard-or-api=api#retrieve-the-account-default-configuration) `Configuration` object for your account. Configuration API changes can take several minutes to propagate to your SDK and reader, and require you to disconnect from and reconnect to your reader to take effect.

## Connect to a reader while offline

The reader stores necessary `Location` information locally after connecting online. On subsequent offline connections, it uses the stored configuration information from that `Location`.

To collect payments with a smart reader while offline, you must have previously connected to any mobile reader of the same type at the same `Location` while online within the last 30 days, on the same local network.

The reader stores the `Location` information locally after connecting online, and it derives configuration information from that `Location` while operating offline. Your reader and POS device must be on the same local network used to connect online. You can’t switch networks while offline.

If you attempt to connect to a reader while offline without meeting these requirements, the request fails with an error.

| Error                                                                                                             | Resolution                                                                                                                                                                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **The SDK isn’t connected to the internet**                                                                       | Make sure the `Location` you’re using is [configured](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#enable-offline-mode) for offline mode. Otherwise, connect to any reader while online, and then connect to a reader of the same type while offline.                                |
| **The selected reader requires a software update before it can be used to collect payments offline.**             | The reader’s software hasn’t been updated in 30 days or more. Connect to the reader while online to update it.                                                                                                                                                                                                             |
| **The selected reader must be paired online at this location before it can be used to collect payments offline.** | You’re attempting to connect to a reader type that your POS hasn’t previously connected to while online. You must first connect to this reader or any reader of the same type while online. Or, if you want to connect while offline, you can connect to a reader type that your POS previously connected to while online. |

## Handle offline events [Client-side]

- [OfflineDelegate (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Protocols/SCPOfflineDelegate.html)

To allow your application to receive updates about the SDK’s network status and the state of forwarded payments, implement the `OfflineDelegate` protocol and pass it to the Terminal SDK. You must set `OfflineDelegate` before collecting payments offline.

#### Swift

```swift

import StripeTerminal

class CustomOfflineDelegate: OfflineDelegate {

    func terminal(_ terminal: Terminal, didChangeOfflineStatus offlineStatus: OfflineStatus) {
        // Check the value of `offlineStatus` and update your UI accordingly. For instance,
        // you can check the SDK's network status at `offlineStatus.sdk.networkStatus`.
        //
        // You can also check the SDK's current offline status using
        // `Terminal.shared.offlineStatus.sdk.networkStatus`.
    }

    func terminal(_ terminal: Terminal, didForwardPaymentIntent intent: PaymentIntent, error: Error?) {
        // The PaymentIntent was successfully forwarded, or an error occurred.
        // Reconcile any local state using the backend-generated `PaymentIntent.stripeId`
        // and the metadata you supplied when creating the PaymentIntent.
        //
        // Note that the `PaymentIntent.stripeId` may still be nil if creating the
        // PaymentIntent in the backend failed.
    }

    func terminal(_ terminal: Terminal, didReportForwardingError error: Error) {
        // A non-specific error occurred while forwarding a PaymentIntent.
        // Check the error message and your integration implementation to
        // troubleshoot.
    }
}
```

#### Swift

```swift
import UIKit
import StripeTerminal

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil) -> Bool {
        Terminal.initWithTokenProvider(APIClient.shared)
        Terminal.shared.offlineDelegate = CustomOfflineDelegate()
        // ...
        return true
    }

    // ...

}
```

## Create a PaymentIntent while offline [Client-side]

- [createPaymentIntent (iOS)](<https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)createPaymentIntent:completion:>)
- [CreateConfiguration (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPCreateConfiguration.html)
- [OfflineDetails (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPOfflineDetails.html)

To support operating offline, use the SDK’s `createPaymentIntent` to create PaymentIntent objects. This allows the SDK to create PaymentIntents while offline and forward them to Stripe after you’ve re-established connectivity.

While operating offline, `PaymentIntent` objects have a null `stripeId`. We recommend adding a custom identifier to the PaymentIntent’s [metadata](https://docs.stripe.com/payments/payment-intents.md#storing-information-in-metadata) to help reconcile `PaymentIntent` objects created offline in your database.

You can set up a [webhook](https://docs.stripe.com/webhooks.md) endpoint to receive `PaymentIntent` events when offline payments are forwarded to Stripe, and use your identifier to associate them with a `PaymentIntent` ID.

#### Swift

```swift

import UIKit
import StripeTerminal

class PaymentViewController: UIViewController {

    // Action for a "Checkout" button
    func checkoutAction() throws {
        // Populate the correct transaction amount from your application.
        let amount = UInt(10_00)

        // Build up parameters for creating a `PaymentIntent`
        let params = try PaymentIntentParametersBuilder(
            amount: amount,
            currency: "sgd"
        ).setMetadata(["offlineId": UUID().uuidString])
        .build()

        Terminal.shared.createPaymentIntent(params) { createResult, createError in
            if let error = createError {
                // Handle errors in your application.
                print("createPaymentIntent failed: \(error)")
            } else if let paymentIntent = createResult {
                print("createPaymentIntent succeeded")// If the `PaymentIntent` was created offline, its `stripeId` field will be nil.
                if let onlineCreatedId = paymentIntent.stripeId {
                    print("created online");
                } else {
                    print("created offline")
                }
            }
        }
    }
}
```

The `Terminal.createPaymentIntent` accepts a `CreateConfiguration` parameter. By default, if you’re operating offline, the Terminal SDK stores all offline payments, then forwards them to Stripe’s backend when connectivity is restored.

To customize this behavior, you can pass in a `CreateConfiguration` object with an `offlineBehavior` attribute set to as `REQUIRE_ONLINE`, `PREFER_ONLINE` or `FORCE_OFFLINE`.

#### Managing risk

Setting `offlineBehavior` to `REQUIRE_ONLINE` fails the current transaction if you’re operating offline. For example, you might want to disallow transactions above a certain amount or disallow all offline transactions if the reader has stored a set of transactions whose sum exceeds a certain amount.

The SDK exposes two properties to help you manage risk:

1. `Terminal.offlineStatus.reader.offlinePaymentsCount`
1. `Terminal.offlineStatus.reader.offlinePaymentAmountsByCurrency`

#### Managing latency while offline

Based on your network connectivity, the Terminal SDK automatically determines whether to collect payments online or offline. However, you might want to operate offline despite having an active network connection (for example, if you need to collect transactions quickly and your network connection is slow). You can pass a `CreateConfiguration` object with `offlineBehavior` set to `FORCE_OFFLINE` to collect the payment offline regardless of connectivity.

Payments collected offline while the Terminal reader has an active network connection are forwarded in the background.

#### Swift

```swift

import UIKit
import StripeTerminal

class PaymentViewController: UIViewController {

    // Action for a "Checkout" button
    func checkoutAction() throws {
        // ...build up parameters and callback for creating a `PaymentIntent`

        // Your app might want to prevent offline payments for too large an amount.
        // Here, we block the payment if the amount is over 1000 sgd.
        // Otherwise, we allow collecting offline if the network connection is unavailable.let offlineBehavior: SCPOfflineBehavior = {
            if amount > UInt(1_000_00) {
                return .requireOnline
            } else {
                return .preferOnline
            }
        }()

        let createConfiguration = try CreateConfigurationBuilder().setOfflineBehavior(offlineBehavior).build()
        Terminal.shared.createPaymentIntent(params, createConfig: createConfiguration) { createResult, createError in
            // handle success or failure
        }
    }
}
```

## Collect a payment method [Client-side]

- [CollectPaymentIntentConfiguration (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPCollectPaymentIntentConfiguration.html)

> Payment liability is your responsibility when operating your reader offline. Because magnetic stripe data is easy to spoof, Stripe disallows this option while operating offline. Tapping cards is also not supported in markets where _Strong Customer Authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase) is required.

Collecting payments while offline is similar to [collecting payments while online](https://docs.stripe.com/terminal/payments/collect-card-payment.md#collect-payment). Your smart reader automatically displays the available payment options to the customer.

> Readers don’t support [inspecting payment method details before authorization](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=ios#collect-inspect-payment-method) while offline. Although you can still use the `initWithUpdatePaymentIntent` parameter in `CollectPaymentIntentConfiguration`, the `paymentMethod` field on the PaymentIntent is absent if the SDK is operating offline.

#### Swift

```swift

import UIKit
import StripeTerminal

class PaymentViewController: UIViewController {

    // Action for a "Checkout" button
    func checkoutAction() {
        Terminal.shared.collectPaymentMethod(paymentIntent) { collectResult, collectError in
            if let error = collectError {
                print("collectPaymentMethod failed: \(error)")
            }
            else if let paymentIntent = collectResult {
                print("collectPaymentMethod succeeded")
                // ... Confirm the payment
            }
        }
    }
}
```

## Confirm payment [Client-side]

Confirming payments while offline is similar to [confirming payments while online](https://docs.stripe.com/terminal/payments/collect-card-payment.md#confirm-payment). The primary difference is that your integration must handle offline-specific error cases, such as when the transaction exceeds the Stripe-enforced offline maximum of 10,000 USD or equivalent in your operating currency.

In some cases, the SDK might create a `PaymentIntent` online, but confirm it while offline. When this happens, the `PaymentIntent` might have a non-null `stripeId`. If it was confirmed offline, `offlineDetails` will be defined and populated.

#### Swift

```swift


import UIKit
import StripeTerminal

class PaymentViewController: UIViewController {

    // Action for a "Checkout" button
    func checkoutAction() {

        Terminal.shared.confirmPaymentIntent(paymentIntent) { confirmResult, confirmError in
            if let error = confirmError {
                // Handle offline-specific errors in your application (for example,
                // unsupported payment method).
                print("confirmPaymentIntent failed: \(error)")
            } else if let confirmedPaymentIntent= confirmResult {print("confirmPaymentIntent succeeded")
                if let offlineDetails = paymentIntent.offlineDetails {
                    print("confirmed offline");
                } else {
                    print("confirmed online")
                }
            }
        }
    }
}
```

#### Providing receipts

You might require information about the card used to complete a payment while offline. For example, you might need to generate a receipt for customers who require one at the time of purchase.

If the PaymentIntent is confirmed offline, retrieve its [OfflineCardPresentDetails](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPOfflineCardPresentDetails.html) from the `paymentIntent.offlineDetails.offlineCardPresentDetails` property.

This hash contains a [ReceiptDetails](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPReceiptDetails.html) property you can use to generate a receipt, as well as other card details like the cardholder name and card brand.

The `account_type` and `authorization_response_code` receipt fields are unavailable on PaymentIntents processed offline. [Prebuilt email receipts](https://docs.stripe.com/terminal/features/receipts.md#prebuilt) are only sent after connectivity is restored and the payment is successfully captured.

## Wait for payments to forward [Client-side]

When network connectivity is restored, the reader automatically begins forwarding the stored offline payments.

The reader attempts to forward payments even if its network status is offline. This means your connection token provider might receive a request to provide a connection token even when the device is offline.

If you disconnect or power off your smart reader too soon, your payments might not be forwarded. You can query `Terminal.offlineStatus.reader.networkStatus` to make sure your reader is online and can forward payments, and `Terminal.offlineStatus.reader.offlinePaymentsCount` to check how many payments the reader has to be forwarded.

If your smart reader becomes damaged or otherwise can’t take payments, your stored payments can often still be forwarded. Make sure to connect the smart reader to your POS and re-establish Internet access to allow it to re-connect to Stripe.

## Capture payment

While offline, you can create PaymentIntents with `captureMethod` set to `automatic`.

After you confirm these PaymentIntents, they have a `Succeeded` status instead of `RequiresCapture`. Stripe automatically captures the payments after you forward them.

If you opt for manual capture, payments that are successfully forwarded and authorized require capture from your backend or application.

- To capture payments from your backend, use [webhooks](https://docs.stripe.com/webhooks.md) to listen for PaymentIntents with a `requires_capture` status.
- To capture payments from your application, wait for your application to receive calls to `OfflineDelegate.didForwardPayment` for each PaymentIntent as the reader forwards it. A PaymentIntent is ready to capture if its status is `RequiresCapture` and the `offlineDetails` is null or has a `requiresUpload` value of `NO` .

#### Swift

```swift

Terminal.shared.confirmPaymentIntent(paymentIntent) { confirmResult, confirmError in
    if let error = confirmError {
        // Handle offline-specific errors in your application (for example,
        // unsupported payment method).
        print("confirmPaymentIntent failed: \(error)")
    } else if let confirmedPaymentIntent = confirmResult {
        if intent.status == .requiresCapture {if let offlineDetails = confirmedPaymentIntent.offlineDetails(),
               offlineDetails.requiresUpload {
                // Offline payment, wait for `didForwardPaymentIntent` (see snippet below)
            } else {
                // Online payment, can be captured now
            }
        }
        // else, handle other intent.status results here
    }
}
```

Capture an offline payment after the reader forwards it in your OfflineDelegate’s `didForwardPaymentIntent`:

#### Swift

```swift

import StripeTerminal

class CustomOfflineDelegate: OfflineDelegate {
    // ...
    func terminal(_ terminal: Terminal, didForwardPaymentIntent intent: PaymentIntent, error: Error?) {
        if let error = error {
            // Handle the error appropriate for your application
            return
        }

        if intent.status == .requiresCapture {
            // The intent is ready to be captured.
        } else {
            // Handle the intent.status as appropriate.
        }
    }
    // ...
}
```

## Examine payments collected offline

After authorization, you can use the [PaymentIntents](https://docs.stripe.com/payments/payment-intents.md) API to examine offline details on a payment. Access the [payment method details](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-offline) on the [latest Charge](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-latest_charge) object on a `PaymentIntent` to determine if it was collected offline.

# Android

> This is a Android for when terminal-card-present-integration is terminal and terminal-sdk-platform is android and reader-type is internet. View the full page at https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments?terminal-card-present-integration=terminal&terminal-sdk-platform=android&reader-type=internet.

The Terminal SDK allows your application to continue collecting payments using a smart reader without an Internet connection.

If you’re using a separate POS device with a Stripe smart reader, you still need a functioning local network to allow your POS device to communicate with the smart reader. Operating offline with smart readers is for scenarios where your POS and reader can’t communicate with Stripe, such as during an ISP outage. If you need to operate offline without a local network, consider Stripe Terminal’s [mobile readers](https://docs.stripe.com/terminal/mobile-readers.md).

You can also operate offline with an Apps on Devices integration. Since your POS application runs directly on the smart reader, you don’t need a local network to collect payments. However, you still need to be on a local network when your reader first boots up, even if the network doesn’t have access to the Internet.

> When operating offline, payment information is collected at the time of sale, and authorization is only attempted after connectivity is restored and the payment is forwarded. When operating offline with an Internet reader, the reader stores collected payment information. You, as the user, assume all decline and tamper-related risks associated with an offline transaction. If your tampered reader can’t forward payments to Stripe, or the issuer declines the transaction, there’s no way to recover the funds, and you might not receive payment from the customer for goods or services already provided.
>
> To reduce the chances of an issuer decline, you’re encouraged to:
>
> - Reestablish internet connectivity as soon as possible to record the payments to Stripe.

- Restrict transactions if they exceed a certain amount.
- [Fail all offline payments](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#managing-risk) if the SDK has stored a set of transactions whose sum exceeds a certain amount.

## Collect payments while offline

Offline payments follow the same steps as online payments: create, collect, process, and capture the payment. Your device can transition from online to offline at any step in the process.

1. [Enable offline mode](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#enable-offline-mode)
1. [Connect to a reader while offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#connect-while-offline)
1. [Handle offline events](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#handle-offline-events)
1. [Create a PaymentIntent while offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#create-payment-intent)
1. [Collect a payment method](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#collect-payment-method)
1. [Confirm the payment](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#confirm-payment)
1. [Wait for payments to forward](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#wait-for-forward)
1. (Optional) [Capture the payment](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#capture-payment)
1. (Optional) [Examine payments collected offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#examine-offline)

## Enable offline mode

To use offline mode, your application needs to consume version `3.2.0` or later of the Terminal Android SDK.

Use a [Configuration](https://docs.stripe.com/api/terminal/configuration.md) object or [the Dashboard](https://docs.stripe.com/terminal/fleet/configurations-overview.md?dashboard-or-api=dashboard#update-the-default-configuration-for-the-account) to enable offline mode for the [supported](https://docs.stripe.com/terminal/features/operate-offline/overview.md?reader-type=internet#availability) devices at your `Location`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const configuration = await stripe.terminal.configurations.create({
  offline: {
    enabled: true,
  },
});
```

After you enable offline mode on a `Configuration` object, you can [assign it](https://docs.stripe.com/terminal/fleet/configurations-overview.md?dashboard-or-api=api#create-a-configuration-for-an-individual-location) to a `Location`. You can also enable offline mode by default for all `Locations` by updating the [default](https://docs.stripe.com/terminal/fleet/configurations-overview.md?dashboard-or-api=api#retrieve-the-account-default-configuration) `Configuration` object for your account. Configuration API changes can take several minutes to propagate to your SDK and reader, and require you to disconnect from and reconnect to your reader to take effect.

## Connect to a reader while offline

The reader stores necessary `Location` information locally after connecting online. On subsequent offline connections, it uses the stored configuration information from that `Location`.

To collect payments with a smart reader while offline, you must have previously connected to any mobile reader of the same type at the same `Location` while online within the last 30 days, on the same local network.

The reader stores the `Location` information locally after connecting online, and it derives configuration information from that `Location` while operating offline. Your reader and POS device must be on the same local network used to connect online. You can’t switch networks while offline.

If you attempt to connect to a reader while offline without meeting these requirements, the request fails with an error.

| Error                                                                                                             | Resolution                                                                                                                                                                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **The SDK isn’t connected to the internet**                                                                       | Make sure the `Location` you’re using is [configured](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#enable-offline-mode) for offline mode. Otherwise, connect to any reader while online, and then connect to a reader of the same type while offline.                                |
| **The selected reader requires a software update before it can be used to collect payments offline.**             | The reader’s software hasn’t been updated in 30 days or more. Connect to the reader while online to update it.                                                                                                                                                                                                             |
| **The selected reader must be paired online at this location before it can be used to collect payments offline.** | You’re attempting to connect to a reader type that your POS hasn’t previously connected to while online. You must first connect to this reader or any reader of the same type while online. Or, if you want to connect while offline, you can connect to a reader type that your POS previously connected to while online. |

## Handle offline events [Client-side]

- [OfflineListener (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.callable/-offline-listener/index.html)

To allow your application to receive updates about the SDK’s network status and the state of forwarded payments, implement the `OfflineListener` interface and pass it to the Terminal SDK. You must set `OfflineListener` before collecting payments offline.

#### Kotlin

```kotlin
class CustomOfflineListener : OfflineListener {
    override fun onOfflineStatusChange(offlineStatus: OfflineStatus) {
        // Check the value of `offlineStatus` and update your UI accordingly. For instance,
        // you can check the SDK's network status at `offlineStatus.sdk.networkStatus`.
        //
        // You can also check the SDK's current offline status using
        // `Terminal::offlineStatus`.
    }

    override fun onPaymentIntentForwarded(paymentIntent: PaymentIntent, e: TerminalException?) {
        // The PaymentIntent was successfully forwarded, or an error occurred.
        // Reconcile any local state using the backend-generated `PaymentIntent::id`
        // and the metadata you supplied when creating the PaymentIntent.
        //
        // Note that the `PaymentIntent::id` may still be null if creating the
        // PaymentIntent in the backend failed.
    }

    override fun onForwardingFailure(e: TerminalException) {
        // A non-specific error occurred while forwarding a PaymentIntent.
        // Check the error message and your integration implementation to
        // troubleshoot.
    }
}
```

#### Kotlin

```kotlin
Terminal.init(
    context = applicationContext,
    logLevel = LogLevel.VERBOSE,
    tokenProvider = CustomConnectionTokenProvider(),
    listener = CustomTerminalListener(),
    offlineListener = CustomOfflineListener(),
)
```

## Create a PaymentIntent while offline [Client-side]

- [createPaymentIntent (Android)](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/create-payment-intent.html)
- [CreateConfiguration (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-create-configuration/index.html)
- [OfflineDetails (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-offline-details/index.html)

To support operating offline, use the SDK’s `createPaymentIntent` to create PaymentIntent objects. This allows the SDK to create PaymentIntents while offline and forward them to Stripe after you’ve re-established connectivity.

While operating offline, `PaymentIntent` objects have a null `id`. We recommend adding a custom identifier to the PaymentIntent’s [metadata](https://docs.stripe.com/payments/payment-intents.md#storing-information-in-metadata) to help reconcile `PaymentIntent` objects created offline in your database.

You can set up a [webhook](https://docs.stripe.com/webhooks.md) endpoint to receive `PaymentIntent` events when offline payments are forwarded to Stripe, and use your identifier to associate them with a `PaymentIntent` ID.

#### Kotlin

```kotlin
private const val TAG = "PaymentActivity"

class PaymentActivity : AppCompatActivity() {
    // Action for a "Checkout" button
    private fun onCheckout(cart: Cart) {
        // Build up parameters for creating a `PaymentIntent`
        val params = PaymentIntentParameters.Builder()
            .setAmount(cart.total)
            .setCurrency(cart.currency).setMetadata(mapOf("unique-id" to UUID.randomUUID().toString()))
            .build()

        val createPaymentCallback: PaymentIntentCallback = object : PaymentIntentCallback {
            override fun onSuccess(paymentIntent: PaymentIntent) {
                Log.d(TAG, "createPaymentIntent succeeded")// If the `PaymentIntent` was created offline, its `id` field will be null.
                if (paymentIntent.id != null) {
                    Log.d(TAG, "created online")
                } else {
                    Log.d(TAG, "created offline")
                }
                // ... Collect a PaymentMethod
            }

            override fun onFailure(e: TerminalException) {
                Log.e(TAG, "createPaymentIntent failed", e)
                // Handle errors in your application.
            }
        }
        Terminal.getInstance().createPaymentIntent(params, createPaymentCallback)
    }
}
```

The `Terminal.createPaymentIntent` accepts a `CreateConfiguration` parameter. By default, if you’re operating offline, the Terminal SDK stores all offline payments, then forwards them to Stripe’s backend when connectivity is restored.

To customize this behavior, you can pass in a `CreateConfiguration` object with an `offlineBehavior` attribute set to as `REQUIRE_ONLINE`, `PREFER_ONLINE` or `FORCE_OFFLINE`.

#### Managing risk

Setting `offlineBehavior` to `REQUIRE_ONLINE` fails the current transaction if you’re operating offline. For example, you might want to disallow transactions above a certain amount or disallow all offline transactions if the reader has stored a set of transactions whose sum exceeds a certain amount.

The SDK exposes two properties to help you manage risk:

1. `Terminal.offlineStatus.reader.offlinePaymentsCount`
1. `Terminal.offlineStatus.reader.offlinePaymentAmountsByCurrency`

#### Managing latency while offline

Based on your network connectivity, the Terminal SDK automatically determines whether to collect payments online or offline. However, you might want to operate offline despite having an active network connection (for example, if you need to collect transactions quickly and your network connection is slow). You can pass a `CreateConfiguration` object with `offlineBehavior` set to `FORCE_OFFLINE` to collect the payment offline regardless of connectivity.

Payments collected offline while the Terminal reader has an active network connection are forwarded in the background.

#### Kotlin

```kotlin
private const val TAG = "PaymentActivity"

class PaymentActivity : AppCompatActivity() {
    // Action for a "Checkout" button
    private fun onCheckout(cart: Cart) {
        // ...build up parameters and callback for creating a `PaymentIntent`

        // Your app might want to prevent offline payments for too large an amount.
        // Here, we require a network connection if the payment if the amount is over 1000 sgd.
        // Otherwise, we allow collecting offline if the network connection is unavailable.val offlineBehavior = if (cart.total > 1000000) {
            OfflineBehavior.REQUIRE_ONLINE
        } else {
            OfflineBehavior.PREFER_ONLINE
        }
        val createConfig = CreateConfiguration(offlineBehavior)

        Terminal.getInstance().createPaymentIntent(params, createPaymentCallback, createConfig)
    }
}
```

## Collect a payment method [Client-side]

- [CollectPaymentIntentConfiguration (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-collect-payment-intent-configuration/index.html)

> Payment liability is your responsibility when operating your reader offline. Because magnetic stripe data is easy to spoof, Stripe disallows this option while operating offline. Tapping cards is also not supported in markets where _Strong Customer Authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase) is required.

Collecting payments while offline is similar to [collecting payments while online](https://docs.stripe.com/terminal/payments/collect-card-payment.md#collect-payment). Your smart reader automatically displays the available payment options to the customer.

> Readers don’t support [inspecting payment method details before authorization](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=android#collect-inspect-payment-method) while offline. Although you can still set the `updatePaymentIntent` parameter in `CollectPaymentIntentConfiguration`, the `paymentMethod` field on the PaymentIntent is absent if the SDK is operating offline.

#### Kotlin

```kotlin
private const val TAG = "PaymentActivity"

class PaymentActivity : AppCompatActivity() {
    // Action for a "Checkout" button
    private fun onCheckout(cart: Cart) {
        val collectPaymentCallback: PaymentIntentCallback = object : PaymentIntentCallback {
            override fun onSuccess(paymentIntent: PaymentIntent) {
                Log.d(TAG, "collectPaymentMethod succeeded")
                // ... Confirm the payment
            }

            override fun onFailure(e: TerminalException) {
                Log.d(TAG, "collectPaymentMethod failed:", e)
            }
        }
        val collectConfig = CollectPaymentIntentConfiguration.Builder().build()
        Terminal.getInstance().collectPaymentMethod(paymentIntent, collectPaymentCallback, collectConfig)
    }
}
```

## Confirm payment [Client-side]

Confirming payments while offline is similar to [confirming payments while online](https://docs.stripe.com/terminal/payments/collect-card-payment.md#confirm-payment). The primary difference is that your integration must handle offline-specific error cases, such as when the transaction exceeds the Stripe-enforced offline maximum of 10,000 USD or equivalent in your operating currency.

In some cases, the SDK might create a `PaymentIntent` online, but confirm it while offline. When this happens, the `PaymentIntent` might have a non-null `id`. If it was confirmed offline, `offlineDetails` will be defined and populated.

#### Kotlin

```kotlin
private const val TAG = "PaymentActivity"

class PaymentActivity : AppCompatActivity() {
    // Action for a "Checkout" button
    private fun onCheckout(cart: Cart) {
        val confirmPaymentIntentCallback: PaymentIntentCallback = object : PaymentIntentCallback {
            override fun onSuccess(paymentIntent: PaymentIntent) {
                Log.d(TAG, "confirmPaymentIntent succeeded")// If the `PaymentIntent` was confirmed offline, `paymentIntent.offlineDetails` will be defined
                if (paymentIntent.offlineDetails != null) {
                    Log.d(TAG, "confirmed offline")
                } else {
                    Log.d(TAG, "confirmed online")
                }
            }

            override fun onFailure(e: TerminalException) {
                // Handle offline-specific errors in your application (for example,
                // unsupported payment method).
                Log.e(TAG, "confirmPaymentIntent failed:", e)
            }
        }
        Terminal.getInstance().confirmPaymentIntent(paymentIntent, confirmPaymentIntentCallback)
    }
}
```

#### Providing receipts

You might require information about the card used to complete a payment while offline. For example, you might need to generate a receipt for customers who require one at the time of purchase.

If the PaymentIntent is confirmed offline, retrieve its [OfflineCardPresentDetails](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-offline-card-present-details/index.html) from the `paymentIntent.offlineDetails.offlineCardPresentDetails` property.

This hash contains a [ReceiptDetails](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-receipt-details/index.html) property you can use to generate a receipt, as well as other card details like the cardholder name and card brand.

The `account_type` and `authorization_response_code` receipt fields are unavailable on PaymentIntents processed offline. [Prebuilt email receipts](https://docs.stripe.com/terminal/features/receipts.md#prebuilt) are only sent after connectivity is restored and the payment is successfully captured.

## Wait for payments to forward [Client-side]

When network connectivity is restored, the reader automatically begins forwarding the stored offline payments.

The reader attempts to forward payments even if its network status is offline. This means your connection token provider might receive a request to provide a connection token even when the device is offline.

If you disconnect or power off your smart reader too soon, your payments might not be forwarded. You can query `Terminal.offlineStatus.reader.networkStatus` to make sure your reader is online and can forward payments, and `Terminal.offlineStatus.reader.offlinePaymentsCount` to check how many payments the reader has to be forwarded.

If your smart reader becomes damaged or otherwise can’t take payments, your stored payments can often still be forwarded. Make sure to connect the smart reader to your POS and re-establish Internet access to allow it to re-connect to Stripe.

## Capture payment

While offline, you can create PaymentIntents with `captureMethod` set to `automatic`.

After you confirm these PaymentIntents, they have a `SUCCEEDED` status instead of `REQUIRES_CAPTURE` . Stripe automatically captures the payments after you forward them.

If you opt for manual capture, payments that are successfully forwarded and authorized require capture from your backend or application.

- To capture payments from your backend, use [webhooks](https://docs.stripe.com/webhooks.md) to listen for PaymentIntents with a `requires_capture` status.
- To capture payments from your application, wait for your application to receive calls to `OfflineListener::onPaymentIntentForwarded` for each PaymentIntent as the reader forwards it. A PaymentIntent is ready to capture if its status is `REQUIRES_CAPTURE` and the `offlineDetails` is null or has a `requiresUpload` value of `false` .

#### Kotlin

```kotlin
private const val TAG = "PaymentActivity"

class PaymentActivity : AppCompatActivity() {
    // Action for a "Checkout" button
    private fun onCheckout(cart: Cart) {
        val callback: PaymentIntentCallback = object : PaymentIntentCallback {
            override fun onSuccess(paymentIntent: PaymentIntent) {
                Log.d(TAG, "confirmPaymentIntent succeeded")
                if (paymentIntent.status == PaymentIntentStatus.REQUIRES_CAPTURE) {val offlineDetails = paymentIntent.offlineDetails
                    if (offlineDetails?.requiresUpload == true) {
                        // Offline payment, wait for `onPaymentIntentForwarded` (see snippet below)
                    } else {
                        // Online payment, can be captured now
                    }
                } else {
                    // Handle other status results here
                }
            }

            override fun onFailure(e: TerminalException) {
                // Handle offline-specific errors in your application (for example,
                // unsupported payment method).
                Log.e(TAG, "confirmPaymentIntent failed:", e)
            }
        }

        Terminal.getInstance().confirmPaymentIntent(paymentIntent, callback)
    }
}
```

Capture an offline payment after the reader forwards it in your `OfflineListener::onPaymentIntentForwarded`:

#### Kotlin

```kotlin
class CustomOfflineListener : OfflineListener {
    // ...

    override fun onPaymentIntentForwarded(paymentIntent: PaymentIntent, e: TerminalException?) {
        if (e != null) {
            // Handle the error appropriate for your application
        } else if (paymentIntent.status == PaymentIntentStatus.REQUIRES_CAPTURE) {
            // The paymentIntent is ready to be captured
        } else {
            // Handle other status results here
        }
    }

    // ...
}
```

## Examine payments collected offline

After authorization, you can use the [PaymentIntents](https://docs.stripe.com/payments/payment-intents.md) API to examine offline details on a payment. Access the [payment method details](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-offline) on the [latest Charge](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-latest_charge) object on a `PaymentIntent` to determine if it was collected offline.

# React Native

> This is a React Native for when terminal-card-present-integration is terminal and terminal-sdk-platform is react-native and reader-type is internet. View the full page at https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments?terminal-card-present-integration=terminal&terminal-sdk-platform=react-native&reader-type=internet.

The Terminal SDK allows your application to continue collecting payments using a smart reader without an Internet connection.

If you’re using a separate POS device with a Stripe smart reader, you still need a functioning local network to allow your POS device to communicate with the smart reader. Operating offline with smart readers is for scenarios where your POS and reader can’t communicate with Stripe, such as during an ISP outage. If you need to operate offline without a local network, consider Stripe Terminal’s [mobile readers](https://docs.stripe.com/terminal/mobile-readers.md).

You can also operate offline with an Apps on Devices integration. Since your POS application runs directly on the smart reader, you don’t need a local network to collect payments. However, you still need to be on a local network when your reader first boots up, even if the network doesn’t have access to the Internet.

> When operating offline, payment information is collected at the time of sale, and authorization is only attempted after connectivity is restored and the payment is forwarded. When operating offline with an Internet reader, the reader stores collected payment information. You, as the user, assume all decline and tamper-related risks associated with an offline transaction. If your tampered reader can’t forward payments to Stripe, or the issuer declines the transaction, there’s no way to recover the funds, and you might not receive payment from the customer for goods or services already provided.
>
> To reduce the chances of an issuer decline, you’re encouraged to:
>
> - Reestablish internet connectivity as soon as possible to record the payments to Stripe.

- Restrict transactions if they exceed a certain amount.
- [Fail all offline payments](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#managing-risk) if the SDK has stored a set of transactions whose sum exceeds a certain amount.

## Collect payments while offline

Offline payments follow the same steps as online payments: create, collect, process, and capture the payment. Your device can transition from online to offline at any step in the process.

1. [Enable offline mode](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#enable-offline-mode)
1. [Connect to a reader while offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#connect-while-offline)
1. [Handle offline events](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#handle-offline-events)
1. [Create a PaymentIntent while offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#create-payment-intent)
1. [Collect a payment method](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#collect-payment-method)
1. [Confirm the payment](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#confirm-payment)
1. [Wait for payments to forward](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#wait-for-forward)
1. (Optional) [Capture the payment](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#capture-payment)
1. (Optional) [Examine payments collected offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#examine-offline)

## Enable offline mode

Use a [Configuration](https://docs.stripe.com/api/terminal/configuration.md) object or [the Dashboard](https://docs.stripe.com/terminal/fleet/configurations-overview.md?dashboard-or-api=dashboard#update-the-default-configuration-for-the-account) to enable offline mode for the [supported](https://docs.stripe.com/terminal/features/operate-offline/overview.md?reader-type=internet#availability) devices at your `Location`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const configuration = await stripe.terminal.configurations.create({
  offline: {
    enabled: true,
  },
});
```

After you enable offline mode on a `Configuration` object, you can [assign it](https://docs.stripe.com/terminal/fleet/configurations-overview.md?dashboard-or-api=api#create-a-configuration-for-an-individual-location) to a `Location`. You can also enable offline mode by default for all `Locations` by updating the [default](https://docs.stripe.com/terminal/fleet/configurations-overview.md?dashboard-or-api=api#retrieve-the-account-default-configuration) `Configuration` object for your account. Configuration API changes can take several minutes to propagate to your SDK and reader, and require you to disconnect from and reconnect to your reader to take effect.

## Connect to a reader while offline

The reader stores necessary `Location` information locally after connecting online. On subsequent offline connections, it uses the stored configuration information from that `Location`.

To collect payments with a smart reader while offline, you must have previously connected to any mobile reader of the same type at the same `Location` while online within the last 30 days, on the same local network.

The reader stores the `Location` information locally after connecting online, and it derives configuration information from that `Location` while operating offline. Your reader and POS device must be on the same local network used to connect online. You can’t switch networks while offline.

If you attempt to connect to a reader while offline without meeting these requirements, the request fails with an error.

| Error                                                                                                             | Resolution                                                                                                                                                                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **The SDK isn’t connected to the internet**                                                                       | Make sure the `Location` you’re using is [configured](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#enable-offline-mode) for offline mode. Otherwise, connect to any reader while online, and then connect to a reader of the same type while offline.                                |
| **The selected reader requires a software update before it can be used to collect payments offline.**             | The reader’s software hasn’t been updated in 30 days or more. Connect to the reader while online to update it.                                                                                                                                                                                                             |
| **The selected reader must be paired online at this location before it can be used to collect payments offline.** | You’re attempting to connect to a reader type that your POS hasn’t previously connected to while online. You must first connect to this reader or any reader of the same type while online. Or, if you want to connect while offline, you can connect to a reader type that your POS previously connected to while online. |

## Handle offline events [Client-side]

- [UserCallbacks (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/index.html#UserCallbacks)

To allow your application to receive updates about the SDK’s network status and the state of forwarded payments, implement the offline callbacks on the `useStripeTerminal` hook.

```js
const { connectReader, disconnectReader, connectedReader } = useStripeTerminal({
    onDidChangeOfflineStatus(status: OfflineStatus) {
       // Check the value of `offlineStatus` and update your UI accordingly.
       //
       // You can also check the SDK's current offline status calling
       // `getOfflineStatus`.
    },
    onDidForwardingFailure(error) {
       // A non-specific error occurred while forwarding a PaymentIntent.
       // Check the error message and your integration implementation to
       // troubleshoot.
    },
    onDidForwardPaymentIntent(paymentIntent, error) {
       // The PaymentIntent was successfully forwarded, or an error occurred.
       // Reconcile any local state using the backend-generated `paymentIntent.id`
       // and the metadata you supplied when creating the PaymentIntent.
       //
       // Note that the `paymentIntent.id` may still be null if creating the
       // PaymentIntent in the backend failed.
    },
  });
```

## Create a PaymentIntent while offline [Client-side]

- [createPaymentIntent (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#createPaymentIntent)
- [CreatePaymentIntentParams (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/index.html#CreatePaymentIntentParams)
- [OfflineStatus (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/index.html#OfflineStatus)
- [OfflineStatusDetails (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/index.html#OfflineStatusDetails)

To support operating offline, use the SDK’s `createPaymentIntent` to create PaymentIntent objects. This allows the SDK to create PaymentIntents while offline and forward them to Stripe after you’ve re-established connectivity.

While operating offline, `PaymentIntent` objects have a null `id`. We recommend adding a custom identifier to the PaymentIntent’s [metadata](https://docs.stripe.com/payments/payment-intents.md#storing-information-in-metadata) to help reconcile `PaymentIntent` objects created offline in your database.

You can set up a [webhook](https://docs.stripe.com/webhooks.md) endpoint to receive `PaymentIntent` events when offline payments are forwarded to Stripe, and use your identifier to associate them with a `PaymentIntent` ID.

```js
const _createPaymentIntent = async (cart) => {
  const { error, paymentIntent } = await createPaymentIntent({
    amount: cart.total,
    currency: cart.currency,
    metadata: {
      "unique-id": UUID().uuidString,
    },
  });
};
```

The `Terminal.createPaymentIntent` accepts a `CreateConfiguration` parameter. By default, if you’re operating offline, the Terminal SDK stores all offline payments, then forwards them to Stripe’s backend when connectivity is restored.

To customize this behavior, you can pass in a `CreateConfiguration` object with an `offlineBehavior` attribute set to as `REQUIRE_ONLINE`, `PREFER_ONLINE` or `FORCE_OFFLINE`.

#### Managing risk

Setting `offlineBehavior` to `REQUIRE_ONLINE` fails the current transaction if you’re operating offline. For example, you might want to disallow transactions above a certain amount or disallow all offline transactions if the reader has stored a set of transactions whose sum exceeds a certain amount.

The SDK exposes two properties to help you manage risk:

1. `OfflineStatus.reader.offlinePaymentsCount`
1. `OfflineStatus.reader.offlinePaymentAmountsByCurrency`

#### Managing latency while offline

Based on your network connectivity, the Terminal SDK automatically determines whether to collect payments online or offline. However, you might want to operate offline despite having an active network connection (for example, if you need to collect transactions quickly and your network connection is slow). You can set `offlineBehavior` to `force_offline` to collect the payment offline regardless of connectivity.

Payments collected offline while the Terminal reader has an active network connection are forwarded in the background.

```js
const _createPaymentIntent = async (cart) => {
  // Your app might want to prevent offline payments for too large an amount.
  // Here, we require a network connection if the payment if the amount is over 1000 usd.
  // Otherwise, we allow collecting offline if the network connection is unavailable.let offlineBehavior:
  if (cart.total > 1000000) {
    offlineBehavior = "require_online";
  } else {
    offlineBehavior = "prefer_online";
  }

  const { error, paymentIntent } = await createPaymentIntent({
    amount: cart.total,
    currency: cart.currency,
    offlineBehavior,
  });
};
```

## Collect a payment method [Client-side]

- [CollectPaymentMethodParams (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/index.html#CollectPaymentMethodParams)

> Payment liability is your responsibility when operating your reader offline. Because magnetic stripe data is easy to spoof, Stripe disallows this option while operating offline. Tapping cards is also not supported in markets where _Strong Customer Authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase) is required.

Collecting payments while offline is similar to [collecting payments while online](https://docs.stripe.com/terminal/payments/collect-card-payment.md#collect-payment). Your smart reader automatically displays the available payment options to the customer.

> [Inspecting payment method details before authorization](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=react-native#collect-inspect-payment-method) isn’t supported while offline. Although you can still set the `updatePaymentIntent` parameter in `CollectConfiguration`, the `paymentMethod` field on the PaymentIntent is absent if the SDK is operating offline.

```js
const _collectPaymentMethod_ = async () => {
  const { paymentIntent, error } = await collectPaymentMethod({
    paymentIntent: paymentIntent,
  });

  if (error) {
    // Handle errors in your application.
  }

  // ... Confirm the payment
};
```

## Confirm payment [Client-side]

Confirming payments while offline is similar to [confirming payments while online](https://docs.stripe.com/terminal/payments/collect-card-payment.md#confirm-payment). The primary difference is that your integration must handle offline-specific error cases, such as when the transaction exceeds the Stripe-enforced offline maximum of 10,000 USD or equivalent in your operating currency.

In some cases, the SDK might create a `PaymentIntent` online, but confirm it while offline. When this happens, the `PaymentIntent` might have a non-null `id`. If it was confirmed offline, `offlineDetails` will be defined and populated.

```js
const _confirmPaymentIntent = async () => {
  const { paymentIntent, error } = await confirmPaymentIntent({
    paymentIntent: paymentIntent,
  });

  if (error) {
    // Handle offline-specific errors in your application (for example,
    // unsupported payment method).
  }
  if (paymentIntent.offlineDetails) {
    console.log("confirmed offline");
  } else {
    console.log("confirmed online");
  }
};
```

#### Providing receipts

You might require information about the card used to complete a payment while offline. For example, you might need to generate a receipt for customers who require one at the time of purchase.

If the PaymentIntent is confirmed offline, retrieve its [OfflineCardPresentDetails](https://stripe.dev/stripe-terminal-react-native/api-reference/index.html#OfflineCardPresentDetails) from the `paymentIntent.offlineDetails.offlineCardPresentDetails` property.

This hash contains a [ReceiptDetails](https://stripe.dev/stripe-terminal-react-native/api-reference/index.html#ReceiptDetails) property you can use to generate a receipt, as well as other card details like the cardholder name and card brand.

The `account_type` and `authorization_response_code` receipt fields are unavailable on PaymentIntents processed offline. [Prebuilt email receipts](https://docs.stripe.com/terminal/features/receipts.md#prebuilt) are only sent after connectivity is restored and the payment is successfully captured.

## Wait for payments to forward [Client-side]

When network connectivity is restored, the reader automatically begins forwarding the stored offline payments.

The reader attempts to forward payments even if its network status is offline. This means your connection token provider might receive a request to provide a connection token even when the device is offline.

If you disconnect or power off your smart reader too soon, your payments might not be forwarded. You can query `OfflineStatus.reader.networkStatus` to make sure your reader is online and can forward payments, and `OfflineStatus.reader.offlinePaymentsCount` to check how many payments the reader has to be forwarded.

If your smart reader becomes damaged or otherwise can’t take payments, your stored payments can often still be forwarded. Make sure to connect the smart reader to your POS and re-establish Internet access to allow it to re-connect to Stripe.

## Capture payment

While offline, you can create PaymentIntents with `captureMethod` set to `automatic`.

After you confirm these PaymentIntents, they have a `succeeded` status instead of `requiresCapture` . Stripe automatically captures the payments after you forward them.

If you opt for manual capture, payments that are successfully forwarded and authorized require capture from your backend or application.

- To capture payments from your backend, use [webhooks](https://docs.stripe.com/webhooks.md) to listen for PaymentIntents with a `requires_capture` status.
- To capture payments from your application, wait for your application to receive calls to `useStripeTerminal` hook’s `onDidForwardPaymentIntent` for each PaymentIntent as the reader forwards it. A PaymentIntent is ready to capture if its status is `requiresCapture` and the `OfflineDetails` is null or has a `requiresUpload` value of `false` .

```js
const _confirmPaymentIntent = async () => {
  const { paymentIntent, error } = await confirmPaymentIntent({
    paymentIntent: paymentIntent,
  });

  if (error) {
    // Handle offline-specific errors in your application (for example,
    // unsupported payment method).
  }

  if (paymentIntent.status == "requiresCapture") {
    const offlineDetails = paymentIntent.offlineDetails;
    if (offlineDetails.requiresUpload === true) {
      // Offline payment, wait for `onDidForwardPaymentIntent` (see snippet below)
    } else {
      // Online payment, can be captured now
    }
  } else {
    // handle other paymentIntent.status results here
  }
};
```

Capture an offline payment after the reader forwards it in `onDidForwardPaymentIntent`:

```js
const { connectReader, disconnectReader, connectedReader } = useStripeTerminal({
  onDidForwardPaymentIntent(paymentIntent, error) {
    if (error) {
      // Handle the error appropriate for your application
    } else if (paymentIntent.status == "requires_capture") {
      // The paymentIntent is ready to be captured
    } else {
      // Handle the paymentIntent.status as appropriate.
    }
  },
});
```

## Examine payments collected offline

After authorization, you can use the [PaymentIntents](https://docs.stripe.com/payments/payment-intents.md) API to examine offline details on a payment. Access the [payment method details](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-offline) on the [latest Charge](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-latest_charge) object on a `PaymentIntent` to determine if it was collected offline.

# Java

> This is a Java for when terminal-card-present-integration is terminal and terminal-sdk-platform is java and reader-type is internet. View the full page at https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments?terminal-card-present-integration=terminal&terminal-sdk-platform=java&reader-type=internet.

The Terminal SDK allows your application to continue collecting payments using a smart reader without an Internet connection.

If you’re using a separate POS device with a Stripe smart reader, you still need a functioning local network to allow your POS device to communicate with the smart reader. Operating offline with smart readers is for scenarios where your POS and reader can’t communicate with Stripe, such as during an ISP outage. If you need to operate offline without a local network, consider Stripe Terminal’s [mobile readers](https://docs.stripe.com/terminal/mobile-readers.md).

You can also operate offline with an Apps on Devices integration. Since your POS application runs directly on the smart reader, you don’t need a local network to collect payments. However, you still need to be on a local network when your reader first boots up, even if the network doesn’t have access to the Internet.

> When operating offline, payment information is collected at the time of sale, and authorization is only attempted after connectivity is restored and the payment is forwarded. When operating offline with an Internet reader, the reader stores collected payment information. You, as the user, assume all decline and tamper-related risks associated with an offline transaction. If your tampered reader can’t forward payments to Stripe, or the issuer declines the transaction, there’s no way to recover the funds, and you might not receive payment from the customer for goods or services already provided.
>
> To reduce the chances of an issuer decline, you’re encouraged to:
>
> - Reestablish internet connectivity as soon as possible to record the payments to Stripe.

- Restrict transactions if they exceed a certain amount.
- [Fail all offline payments](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#managing-risk) if the SDK has stored a set of transactions whose sum exceeds a certain amount.

## Collect payments while offline

Offline payments follow the same steps as online payments: create, collect, process, and capture the payment. Your device can transition from online to offline at any step in the process.

1. [Enable offline mode](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#enable-offline-mode)
1. [Connect to a reader while offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#connect-while-offline)
1. [Handle offline events](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#handle-offline-events)
1. [Create a PaymentIntent while offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#create-payment-intent)
1. [Collect a payment method](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#collect-payment-method)
1. [Confirm the payment](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#confirm-payment)
1. [Wait for payments to forward](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#wait-for-forward)
1. (Optional) [Capture the payment](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#capture-payment)
1. (Optional) [Examine payments collected offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#examine-offline)

## Enable offline mode

Use a [Configuration](https://docs.stripe.com/api/terminal/configuration.md) object or [the Dashboard](https://docs.stripe.com/terminal/fleet/configurations-overview.md?dashboard-or-api=dashboard#update-the-default-configuration-for-the-account) to enable offline mode for the [supported](https://docs.stripe.com/terminal/features/operate-offline/overview.md?reader-type=internet#availability) devices at your `Location`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const configuration = await stripe.terminal.configurations.create({
  offline: {
    enabled: true,
  },
});
```

After you enable offline mode on a `Configuration` object, you can [assign it](https://docs.stripe.com/terminal/fleet/configurations-overview.md?dashboard-or-api=api#create-a-configuration-for-an-individual-location) to a `Location`. You can also enable offline mode by default for all `Locations` by updating the [default](https://docs.stripe.com/terminal/fleet/configurations-overview.md?dashboard-or-api=api#retrieve-the-account-default-configuration) `Configuration` object for your account. Configuration API changes can take several minutes to propagate to your SDK and reader, and require you to disconnect from and reconnect to your reader to take effect.

## Connect to a reader while offline

The reader stores necessary `Location` information locally after connecting online. On subsequent offline connections, it uses the stored configuration information from that `Location`.

To collect payments with a smart reader while offline, you must have previously connected to any mobile reader of the same type at the same `Location` while online within the last 30 days, on the same local network.

The reader stores the `Location` information locally after connecting online, and it derives configuration information from that `Location` while operating offline. Your reader and POS device must be on the same local network used to connect online. You can’t switch networks while offline.

If you attempt to connect to a reader while offline without meeting these requirements, the request fails with an error.

| Error                                                                                                             | Resolution                                                                                                                                                                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **The SDK isn’t connected to the internet**                                                                       | Make sure the `Location` you’re using is [configured](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#enable-offline-mode) for offline mode. Otherwise, connect to any reader while online, and then connect to a reader of the same type while offline.                                |
| **The selected reader requires a software update before it can be used to collect payments offline.**             | The reader’s software hasn’t been updated in 30 days or more. Connect to the reader while online to update it.                                                                                                                                                                                                             |
| **The selected reader must be paired online at this location before it can be used to collect payments offline.** | You’re attempting to connect to a reader type that your POS hasn’t previously connected to while online. You must first connect to this reader or any reader of the same type while online. Or, if you want to connect while offline, you can connect to a reader type that your POS previously connected to while online. |

## Handle offline events [Client-side]

- [OfflineListener (Java)](https://stripe.dev/stripe-terminal-java/external/com.stripe.stripeterminal.external.callable/-offline-listener/index.html)

To allow your application to receive updates about the SDK’s network status and the state of forwarded payments, implement the `OfflineListener` interface and pass it to the Terminal SDK. You must set `OfflineListener` before collecting payments offline.

```java
public class CustomOfflineListener implements OfflineListener {
    @Override
    public void onOfflineStatusChange(@NotNull OfflineStatus offlineStatus) {
        // Check the value of `offlineStatus` and update your UI accordingly. For instance,
        // you can check the SDK's network status at `offlineStatus.sdk.networkStatus`.
        //
        // You can also check the SDK's current offline status using
        // `Terminal::offlineStatus`.
    }

    @Override
    public void onPaymentIntentForwarded(@NotNull PaymentIntent paymentIntent, @Nullable TerminalException e) {
        // The PaymentIntent was successfully forwarded, or an error occurred.
        // Reconcile any local state using the backend-generated `PaymentIntent::getId`
        // and the metadata you supplied when creating the PaymentIntent.
        //
        // Note that the `PaymentIntent::getId` may still be null if creating the
        // PaymentIntent in the backend failed.
    }

    @Override
    public void onForwardingFailure(@NotNull TerminalException e) {
        // A non-specific error occurred while forwarding a PaymentIntent.
        // Check the error message and your integration implementation to
        // troubleshoot.
    }
}
```

```java
Terminal.init(
    new CustomConnectionTokenProvider(),
    new CustomTerminalListener(),
    getApplicationInfo(),
    LogLevel.VERBOSE,
    new CustomOfflineListener()
);
```

## Create a PaymentIntent while offline [Client-side]

- [createPaymentIntent (Java)](https://stripe.dev/stripe-terminal-java/core/com.stripe.stripeterminal/-terminal/create-payment-intent.html)
- [CreateConfiguration (Java)](https://stripe.dev/stripe-terminal-java/external/com.stripe.stripeterminal.external.models/-create-configuration/index.html)
- [OfflineDetails (Java)](https://stripe.dev/stripe-terminal-java/external/com.stripe.stripeterminal.external.models/-offline-details/index.html)

To support operating offline, use the SDK’s `createPaymentIntent` to create PaymentIntent objects. This allows the SDK to create PaymentIntents while offline and forward them to Stripe after you’ve re-established connectivity.

While operating offline, `PaymentIntent` objects have a null `id`. We recommend adding a custom identifier to the PaymentIntent’s [metadata](https://docs.stripe.com/payments/payment-intents.md#storing-information-in-metadata) to help reconcile `PaymentIntent` objects created offline in your database.

You can set up a [webhook](https://docs.stripe.com/webhooks.md) endpoint to receive `PaymentIntent` events when offline payments are forwarded to Stripe, and use your identifier to associate them with a `PaymentIntent` ID.

```java
HashMap<String, String> metadata = new HashMap<> ();
metadata.put("unique-id", UUID.randomUUID().toString());

final PaymentIntentParameters params = new PaymentIntentParameters.Builder()
    .setAmount(cart.getTotal())
    .setCurrency(cart.getCurrency()).setMetadata(metadata)
    .build();

final PaymentIntentCallback createPaymentCallback = new PaymentIntentCallback() {
    @Override
    public void onSuccess(@NotNull PaymentIntent paymentIntent) {
        System.out.println("createPaymentIntent succeeded");// If the `PaymentIntent` was created offline, its `id` field will be null.
        if (paymentIntent.getId() != null) {
            System.out.println("created online");
        } else {
            System.out.println("created offline");
        }
        // ... Collect a PaymentMethod
    }

    @Override
    public void onFailure(@NotNull TerminalException e) {
        // Handle errors in your application.
    }
};

Terminal.getInstance().createPaymentIntent(params, null, createPaymentCallback);
```

The `Terminal.createPaymentIntent` accepts a `CreateConfiguration` parameter. By default, if you’re operating offline, the Terminal SDK stores all offline payments, then forwards them to Stripe’s backend when connectivity is restored.

To customize this behavior, you can pass in a `CreateConfiguration` object with an `offlineBehavior` attribute set to as `REQUIRE_ONLINE`, `PREFER_ONLINE` or `FORCE_OFFLINE`.

#### Managing risk

Setting `offlineBehavior` to `REQUIRE_ONLINE` fails the current transaction if you’re operating offline. For example, you might want to disallow transactions above a certain amount or disallow all offline transactions if the reader has stored a set of transactions whose sum exceeds a certain amount.

The SDK exposes two properties to help you manage risk:

1. `Terminal.offlineStatus.reader.offlinePaymentsCount`
1. `Terminal.offlineStatus.reader.offlinePaymentAmountsByCurrency`

#### Managing latency while offline

Based on your network connectivity, the Terminal SDK automatically determines whether to collect payments online or offline. However, you might want to operate offline despite having an active network connection (for example, if you need to collect transactions quickly and your network connection is slow). You can pass a `CreateConfiguration` object with `offlineBehavior` set to `FORCE_OFFLINE` to collect the payment offline regardless of connectivity.

Payments collected offline while the Terminal reader has an active network connection are forwarded in the background.

```java
// Your app might want to prevent offline payments for too large an amount.
// Here, we block the payment if the amount is over 1000 sgd.
// Otherwise, we allow collecting offline if the network connection is unavailable.
OfflineBehavior offlineBehavior
    = cart.getTotal() > 1000000 ? offlineBehavior = OfflineBehavior.REQUIRE_ONLINE : OfflineBehavior.PREFER_ONLINE;

final CreateConfiguration createConfig = new CreateConfiguration(offlineBehavior);

Terminal.getInstance().createPaymentIntent(params, createConfig, createPaymentCallback);
```

## Collect a payment method [Client-side]

- [CollectPaymentIntentConfiguration (Java)](https://stripe.dev/stripe-terminal-java/external/com.stripe.stripeterminal.external.models/-collect-payment-intent-configuration/index.html)

> Payment liability is your responsibility when operating your reader offline. Because magnetic stripe data is easy to spoof, Stripe disallows this option while operating offline. Tapping cards is also not supported in markets where _Strong Customer Authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase) is required.

Collecting payments while offline is similar to [collecting payments while online](https://docs.stripe.com/terminal/payments/collect-card-payment.md#collect-payment). Your smart reader automatically displays the available payment options to the customer.

> [Inspecting payment method details before authorization](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=java#collect-inspect-payment-method) isn’t supported while offline. Although you can still use the `updatePaymentIntent` method in `CollectPaymentIntentConfiguration`, the `paymentMethod` field on the PaymentIntent is absent if the SDK is operating offline.

```java
final PaymentIntentCallback collectPaymentCallback = new PaymentIntentCallback() {
    @Override
    public void onSuccess(@NotNull PaymentIntent paymentIntent) {
        System.out.println("collectPaymentMethod succeeded");
        // ... Confirm the payment
    }

    @Override
    public void onFailure(@NotNull TerminalException e) {
        e.printStackTrace();
    }
};

final CollectPaymentIntentConfiguration collectConfig = new CollectPaymentIntentConfiguration.Builder().build();

Terminal.getInstance().collectPaymentMethod(paymentIntent, collectConfig, collectPaymentCallback);
```

## Confirm payment [Client-side]

Confirming payments while offline is similar to [confirming payments while online](https://docs.stripe.com/terminal/payments/collect-card-payment.md#confirm-payment). The primary difference is that your integration must handle offline-specific error cases, such as when the transaction exceeds the Stripe-enforced offline maximum of 10,000 USD or equivalent in your operating currency.

In some cases, the SDK might create a `PaymentIntent` online, but confirm it while offline. When this happens, the `PaymentIntent` might have a non-null `id`. If it was confirmed offline, `offlineDetails`will be defined and populated.

```java
final PaymentIntentCallback confirmPaymentIntentCallback = new PaymentIntentCallback() {
    @Override
    public void onSuccess(@NotNull PaymentIntent paymentIntent) {
        System.out.println("confirmPaymentIntent succeeded");
        // If the `PaymentIntent` was confirmed offline, `paymentIntent.getOfflineDetails()` will be definedif (paymentIntent.getOfflineDetails() != null) {
            System.out.println("confirmed offline");
        } else {
            System.out.println("confirmed online");
        }
    }

    @Override
    public void onFailure(@NotNull TerminalException e) {
        // Handle offline-specific errors in your application (for example,
        // unsupported payment method).
        e.printStackTrace();
    }
};

Terminal.getInstance().confirmPaymentIntent(paymentIntent, confirmPaymentIntentCallback);
```

#### Providing receipts

You might require information about the card used to complete a payment while offline. For example, you might need to generate a receipt for customers who require one at the time of purchase.

If the PaymentIntent is confirmed offline, retrieve its [OfflineCardPresentDetails](https://stripe.dev/stripe-terminal-java/external/com.stripe.stripeterminal.external.models/-offline-card-present-details/index.html) from the `paymentIntent.offlineDetails.offlineCardPresentDetails` property.

This hash contains a [ReceiptDetails](https://stripe.dev/stripe-terminal-java/external/com.stripe.stripeterminal.external.models/-receipt-details/index.html) property you can use to generate a receipt, as well as other card details like the cardholder name and card brand.

The `account_type` and `authorization_response_code` receipt fields are unavailable on PaymentIntents processed offline. [Prebuilt email receipts](https://docs.stripe.com/terminal/features/receipts.md#prebuilt) are only sent after connectivity is restored and the payment is successfully captured.

## Wait for payments to forward [Client-side]

When network connectivity is restored, the reader automatically begins forwarding the stored offline payments.

The reader attempts to forward payments even if its network status is offline. This means your connection token provider might receive a request to provide a connection token even when the device is offline.

If you disconnect or power off your smart reader too soon, your payments might not be forwarded. You can query `Terminal.offlineStatus.reader.networkStatus` to make sure your reader is online and can forward payments, and `Terminal.offlineStatus.reader.offlinePaymentsCount` to check how many payments the reader has to be forwarded.

If your smart reader becomes damaged or otherwise can’t take payments, your stored payments can often still be forwarded. Make sure to connect the smart reader to your POS and re-establish Internet access to allow it to re-connect to Stripe.

## Capture payment

While offline, you can create PaymentIntents with `captureMethod` set to `automatic`.

After you confirm these PaymentIntents, they have a `SUCCEEDED` status instead of `REQUIRES_CAPTURE` . Stripe automatically captures the payments after you forward them.

If you opt for manual capture, payments that are successfully forwarded and authorized require capture from your backend or application.

- To capture payments from your backend, use [webhooks](https://docs.stripe.com/webhooks.md) to listen for PaymentIntents with a `requires_capture` status.
- To capture payments from your application, wait for your application to receive calls to `OfflineListener.OnPaymentIntentForwarded` for each PaymentIntent as the reader forwards it. A PaymentIntent is ready to capture if its status is `REQUIRES_CAPTURE` and the `offlineDetails` is null or has a `requiresUpload` value of `false` .

```java
final PaymentIntentCallback confirmPaymentIntentCallback = new PaymentIntentCallback() {
    @Override
    public void onSuccess(@NotNull PaymentIntent paymentIntent) {
        System.out.println("confirmPaymentIntent succeeded");
        if (paymentIntent.getStatus() == PaymentIntentStatus.REQUIRES_CAPTURE) {OfflineDetails offlineDetails = paymentIntent.getOfflineDetails();
            if (offlineDetails != null && offlineDetails.getRequiresUpload()) {
                // Offline payment, wait for `onPaymentIntentForwarded` (see snippet below)
            } else {
                // Online payment, can be captured now
            }
        } else {
            // Handle other status results here
        }
    }

    @Override
    public void onFailure(@NotNull TerminalException e) {
        // Handle offline-specific errors in your application (for example,
        // unsupported payment method).
    }
};

Terminal.getInstance().confirmPaymentIntent(paymentIntent, confirmPaymentIntentCallback);
```

Capture an offline payment after the reader forwards it in your `OfflineListener::onPaymentIntentForwarded`:

```java
public class CustomOfflineListener implements OfflineListener {
    // ...
    @Override
    public void onPaymentIntentForwarded(@NotNull PaymentIntent paymentIntent, @Nullable TerminalException e) {
        if (e != null) {
            // Handle the error appropriate for your application
        } else if (paymentIntent.getStatus() == PaymentIntentStatus.REQUIRES_CAPTURE) {
            // The paymentIntent is ready to be captured
        } else {
            // Handle other status results here
        }
    }
    // ...
}
```

## Examine payments collected offline

After authorization, you can use the [PaymentIntents](https://docs.stripe.com/payments/payment-intents.md) API to examine offline details on a payment. Access the [payment method details](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-offline) on the [latest Charge](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-latest_charge) object on a `PaymentIntent` to determine if it was collected offline.

# .NET

> This is a .NET for when terminal-card-present-integration is terminal and terminal-sdk-platform is dotnet and reader-type is internet. View the full page at https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments?terminal-card-present-integration=terminal&terminal-sdk-platform=dotnet&reader-type=internet.

The Terminal SDK allows your application to continue collecting payments using a smart reader without an Internet connection.

If you’re using a separate POS device with a Stripe smart reader, you still need a functioning local network to allow your POS device to communicate with the smart reader. Operating offline with smart readers is for scenarios where your POS and reader can’t communicate with Stripe, such as during an ISP outage. If you need to operate offline without a local network, consider Stripe Terminal’s [mobile readers](https://docs.stripe.com/terminal/mobile-readers.md).

You can also operate offline with an Apps on Devices integration. Since your POS application runs directly on the smart reader, you don’t need a local network to collect payments. However, you still need to be on a local network when your reader first boots up, even if the network doesn’t have access to the Internet.

> When operating offline, payment information is collected at the time of sale, and authorization is only attempted after connectivity is restored and the payment is forwarded. When operating offline with an Internet reader, the reader stores collected payment information. You, as the user, assume all decline and tamper-related risks associated with an offline transaction. If your tampered reader can’t forward payments to Stripe, or the issuer declines the transaction, there’s no way to recover the funds, and you might not receive payment from the customer for goods or services already provided.
>
> To reduce the chances of an issuer decline, you’re encouraged to:
>
> - Reestablish internet connectivity as soon as possible to record the payments to Stripe.

- Restrict transactions if they exceed a certain amount.
- [Fail all offline payments](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#managing-risk) if the SDK has stored a set of transactions whose sum exceeds a certain amount.

## Collect payments while offline

Offline payments follow the same steps as online payments: create, collect, process, and capture the payment. Your device can transition from online to offline at any step in the process.

1. [Enable offline mode](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#enable-offline-mode)
1. [Connect to a reader while offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#connect-while-offline)
1. [Handle offline events](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#handle-offline-events)
1. [Create a PaymentIntent while offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#create-payment-intent)
1. [Collect a payment method](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#collect-payment-method)
1. [Confirm the payment](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#confirm-payment)
1. [Wait for payments to forward](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#wait-for-forward)
1. (Optional) [Capture the payment](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#capture-payment)
1. (Optional) [Examine payments collected offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#examine-offline)

## Enable offline mode

Use a [Configuration](https://docs.stripe.com/api/terminal/configuration.md) object or [the Dashboard](https://docs.stripe.com/terminal/fleet/configurations-overview.md?dashboard-or-api=dashboard#update-the-default-configuration-for-the-account) to enable offline mode for the [supported](https://docs.stripe.com/terminal/features/operate-offline/overview.md?reader-type=internet#availability) devices at your `Location`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const configuration = await stripe.terminal.configurations.create({
  offline: {
    enabled: true,
  },
});
```

After you enable offline mode on a `Configuration` object, you can [assign it](https://docs.stripe.com/terminal/fleet/configurations-overview.md?dashboard-or-api=api#create-a-configuration-for-an-individual-location) to a `Location`. You can also enable offline mode by default for all `Locations` by updating the [default](https://docs.stripe.com/terminal/fleet/configurations-overview.md?dashboard-or-api=api#retrieve-the-account-default-configuration) `Configuration` object for your account. Configuration API changes can take several minutes to propagate to your SDK and reader, and require you to disconnect from and reconnect to your reader to take effect.

## Connect to a reader while offline

The reader stores necessary `Location` information locally after connecting online. On subsequent offline connections, it uses the stored configuration information from that `Location`.

To collect payments with a smart reader while offline, you must have previously connected to any mobile reader of the same type at the same `Location` while online within the last 30 days, on the same local network.

The reader stores the `Location` information locally after connecting online, and it derives configuration information from that `Location` while operating offline. Your reader and POS device must be on the same local network used to connect online. You can’t switch networks while offline.

If you attempt to connect to a reader while offline without meeting these requirements, the request fails with an error.

| Error                                                                                                             | Resolution                                                                                                                                                                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **The SDK isn’t connected to the internet**                                                                       | Make sure the `Location` you’re using is [configured](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#enable-offline-mode) for offline mode. Otherwise, connect to any reader while online, and then connect to a reader of the same type while offline.                                |
| **The selected reader requires a software update before it can be used to collect payments offline.**             | The reader’s software hasn’t been updated in 30 days or more. Connect to the reader while online to update it.                                                                                                                                                                                                             |
| **The selected reader must be paired online at this location before it can be used to collect payments offline.** | You’re attempting to connect to a reader type that your POS hasn’t previously connected to while online. You must first connect to this reader or any reader of the same type while online. Or, if you want to connect while offline, you can connect to a reader type that your POS previously connected to while online. |

## Handle offline events [Client-side]

To allow your application to receive updates about the SDK’s network status and the state of forwarded payments, implement the `IOfflineListener` interface and pass it to the Terminal SDK. You must set `IOfflineListener` before collecting payments offline.

```csharp
using TerminalSdk.Api;

namespace StripeExampleApi;

public class CustomOfflineListener : IOfflineListener
{
    public void OnOfflineStatusChange(OfflineStatus offlineStatus)
    {
        // Check the value of `offlineStatus` and update your UI accordingly. For instance,
        // you can check the reader's network status at `offlineStatus.Reader.NetworkStatus`.
        //
        // You can also check the reader's current offline status using
        // `Terminal.OfflineStatus`.
    }

    public void OnPaymentIntentForwarded(PaymentIntent paymentIntent, TerminalException? e)
    {
        // The PaymentIntent was successfully forwarded, or an error occurred.
        // Reconcile any local state using the backend-generated `paymentIntent.Id`
        // and the metadata you supplied when creating the PaymentIntent.
        //
        // Note that the `PaymentIntent.Id` may still be null if creating the
        // PaymentIntent in the backend failed.
    }

    public void OnForwardingFailure(TerminalException e)
    {
        // A non-specific error occurred while forwarding a PaymentIntent.
        // Check the error message and your integration implementation to
        // troubleshoot.
    }
}
```

```csharp
 Terminal.InitTerminal(
    new CustomConnectionTokenProvider(),
    new CustomTerminalListener(),
    new CustomOfflineListener(),
    new ApplicationInformation.Builder()
        .SetName("Terminal Test Console")
        .SetVersion("0.0.0.1")
        .SetDataDirectory(new DirectoryInfo("C:\\TerminalSDK"))
        .Build()
);
```

## Create a PaymentIntent while offline [Client-side]

To support operating offline, use the SDK’s `CreatePaymentIntentAsync` to create PaymentIntent objects. This allows the SDK to create PaymentIntents while offline and forward them to Stripe after you’ve re-established connectivity.

While operating offline, `PaymentIntent` objects have a null `Id`. We recommend adding a custom identifier to the PaymentIntent’s [Metadata](https://docs.stripe.com/payments/payment-intents.md#storing-information-in-metadata) to help reconcile `PaymentIntent` objects created offline in your database.

You can set up a [webhook](https://docs.stripe.com/webhooks.md) endpoint to receive `PaymentIntent` events when offline payments are forwarded to Stripe, and use your identifier to associate them with a `PaymentIntent` ID.

```csharp
// Build up parameters for creating a `PaymentIntent`
var paymentIntentParameters = new PaymentIntentParameters.Builder()
    .SetAmount(cart.Total)
    .SetCurrency(cart.Currency).SetMetadata(new Dictionary<string, string>() { { "unique-id", Guid.NewGuid().ToString() } })
    .Build();

try
{
    var paymentIntent = await Terminal.Instance.CreatePaymentIntentAsync(paymentIntentParameters, null);
    _logger.LogDebug("CreatePaymentIntentAsync succeeded");// If the `PaymentIntent` was created offline, its `Id` field will be null.
    if (paymentIntent.Id != null) {
        _logger.LogDebug("created online");
    } else {
        _logger.LogDebug("created offline");
    }
    // ... Collect a PaymentMethod
}
catch (TerminalException ex)
{
    _logger.LogError(ex, "CreatePaymentIntentAsync failed");
    // Handle errors in your application.
}
```

The `Terminal.CreatePaymentIntentAsync` accepts a `CreateConfiguration` parameter. By default, if you’re operating offline, the Terminal SDK stores all offline payments, then forwards them to Stripe’s backend when connectivity is restored.

To customize this behavior, you can pass in a `CreateConfiguration` object with an `OfflineBehavior` attribute set to as `RequireOnline`, `PreferOnline` or `ForceOffline`.

#### Managing risk

Setting `OfflineBehavior` to `RequireOnline` fails the current transaction if you’re operating offline. For example, you might want to disallow transactions above a certain amount or disallow all offline transactions if the reader has stored a set of transactions whose sum exceeds a certain amount.

The SDK exposes two properties to help you manage risk:

1. `Terminal.OfflineStatus.Reader.OfflinePaymentsCount`
1. `Terminal.OfflineStatus.Reader.OfflinePaymentAmountsByCurrency`

#### Managing latency while offline

Based on your network connectivity, the Terminal SDK automatically determines whether to collect payments online or offline. However, you might want to operate offline despite having an active network connection (for example, if you need to collect transactions quickly and your network connection is slow). You can pass a `CreateConfiguration` object with `OfflineBehavior` set to `ForceOffline` to collect the payment offline regardless of connectivity.

Payments collected offline while the Terminal reader has an active network connection are forwarded in the background.

```csharp
// Your app might want to prevent offline payments for too large an amount.
// Here, we require a network connection if the payment amount is over 1000 usd.
// Otherwise, we allow collecting offline if the network connection is unavailable.var offlineBehavior = OfflineBehavior.PreferOnline;
if (cart.total > 1000000)
{
    offlineBehavior = OfflineBehavior.RequireOnline;
}

var createConfig = new CreateConfiguration.Builder()
    .SetOfflineBehavior(offlineBehavior)
    .Build();


var paymentIntent = await Terminal.Instance.CreatePaymentIntentAsync(paymentIntentParameters, createConfig);
_logger.LogDebug("CreatePaymentIntentAsync succeeded");
// ...continue transaction
```

## Collect a payment method [Client-side]

> Payment liability is your responsibility when operating your reader offline. Because magnetic stripe data is easy to spoof, Stripe disallows this option while operating offline. Tapping cards is also not supported in markets where _Strong Customer Authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase) is required.

Collecting payments while offline is similar to [collecting payments while online](https://docs.stripe.com/terminal/payments/collect-card-payment.md#collect-payment). Your smart reader automatically displays the available payment options to the customer.

> [Inspecting payment method details before authorization](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=dotnet#collect-inspect-payment-method) isn’t supported while offline. Although you can still use the `SetUpdatePaymentIntent` method in `CollectConfiguration`, the `paymentMethod` field on the PaymentIntent is absent if the SDK is operating offline.

```csharp
try
{
    var collectConfig = new CollectConfiguration.Builder()
        .Build();
    var collectedPaymentIntent = await Terminal.Instance.CollectPaymentMethodAsync(paymentIntent, collectConfig);
    _logger.LogDebug("CollectPaymentMethodAsync succeeded");
    // ... Confirm the payment
}
catch (TerminalException ex)
{
    // Handle errors in your application.
}
```

## Confirm payment [Client-side]

Confirming payments while offline is similar to [confirming payments while online](https://docs.stripe.com/terminal/payments/collect-card-payment.md#confirm-payment). The primary difference is that your integration must handle offline-specific error cases, such as when the transaction exceeds the Stripe-enforced offline maximum of 10,000 USD or equivalent in your operating currency.

In some cases, the SDK might create a `PaymentIntent` online, but confirm it while offline. When this happens, the `PaymentIntent` might have a non-null `Id`. If it was confirmed offline, `OfflineDetails` will be defined and populated.

```csharp
try
{
    var confirmedPaymentIntent = await Terminal.Instance.ConfirmPaymentIntentAsync(collectedPaymentIntent);
}
catch (TerminalException ex)
{
    // Handle offline-specific errors in your application (for example,
    // unsupported payment method).
}
```

#### Providing receipts

You might require information about the card used to complete a payment while offline. For example, you might need to generate a receipt for customers who require one at the time of purchase.

If the PaymentIntent is confirmed offline, retrieve its OfflineCardPresentDetails from the `paymentIntent.OfflineDetails.OfflineCardPresentDetails` property.

This hash contains a ReceiptDetails property you can use to generate a receipt, as well as other card details like the cardholder name and card brand.

The `account_type` and `authorization_response_code` receipt fields are unavailable on PaymentIntents processed offline. [Prebuilt email receipts](https://docs.stripe.com/terminal/features/receipts.md#prebuilt) are only sent after connectivity is restored and the payment is successfully captured.

## Wait for payments to forward [Client-side]

When network connectivity is restored, the reader automatically begins forwarding the stored offline payments.

The reader attempts to forward payments even if its network status is offline. This means your connection token provider might receive a request to provide a connection token even when the device is offline.

If you disconnect or power off your smart reader too soon, your payments might not be forwarded. You can query `Terminal.OfflineStatus.Reader.NetworkStatus` to make sure your reader is online and can forward payments, and `Terminal.OfflineStatus.Reader.OfflinePaymentsCount` to check how many payments the reader has to be forwarded.

If your smart reader becomes damaged or otherwise can’t take payments, your stored payments can often still be forwarded. Make sure to connect the smart reader to your POS and re-establish Internet access to allow it to re-connect to Stripe.

## Capture payment

While offline, you can create PaymentIntents with `CaptureMethod` set to `Automatic` .

After you confirm these PaymentIntents, they have a `Succeeded` status instead of `RequiresCapture`. Stripe automatically captures the payments after you forward them.

If you opt for manual capture, payments that are successfully forwarded and authorized require capture from your backend or application.

- To capture payments from your backend, use [webhooks](https://docs.stripe.com/webhooks.md) to listen for PaymentIntents with a `requires_capture` status.
- To capture payments from your application, wait for your application to receive calls to `OfflineListener.OnPaymentIntentForwarded` for each PaymentIntent as the reader forwards it. A PaymentIntent is ready to capture if its status is `RequiresCapture` and the `OfflineDetails` is null or has a `RequiresUpload` value of `false` .

```csharp
try
{
    var confirmedPaymentIntent = await Terminal.Instance.ConfirmPaymentIntentAsync(collectedPaymentIntent);
    _logger.LogDebug("ConfirmPaymentIntentAsync succeeded");
    if (paymentIntent.status == PaymentIntentStatus.RequiresCapture) {var offlineDetails = paymentIntent.OfflineDetails;
        if (offlineDetails?.RequiresUpload == true) {
            // Offline payment, wait for `OnPaymentIntentForwarded` (see snippet below)
        } else {
            // Online payment, can be captured now
        }
    } else {
        // handle other paymentIntent.Status results here
    }
}
catch (TerminalException ex)
{
    // Handle offline-specific errors in your application (for example,
    // unsupported payment method).
    _logger.LogError(ex, "ConfirmPaymentIntentAsync failed");
}
```

Capture an offline payment after the reader forwards it in your `IOfflineListener.OnPaymentIntentForwarded`:

```csharp
using TerminalSdk.Api;

namespace StripeExampleApi;

public class CustomOfflineListener : IOfflineListener
{
    public void OnPaymentIntentForwarded(PaymentIntent paymentIntent, TerminalException? e)
    {
        if (e != null) {
            // Handle the error appropriate for your application
        } else if (paymentIntent.Status == PaymentIntentStatus.RequiresCapture) {
            // The paymentIntent is ready to be captured
        } else {
            // Handle the paymentIntent.Status as appropriate.
        }
    }

    // ...
}
```

## Examine payments collected offline

After authorization, you can use the [PaymentIntents](https://docs.stripe.com/payments/payment-intents.md) API to examine offline details on a payment. Access the [payment method details](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-offline) on the [latest Charge](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-latest_charge) object on a `PaymentIntent` to determine if it was collected offline.

# iOS

> This is a iOS for when terminal-card-present-integration is terminal and terminal-sdk-platform is ios and reader-type is simulated. View the full page at https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments?terminal-card-present-integration=terminal&terminal-sdk-platform=ios&reader-type=simulated.

The Terminal SDK allows your application to continue collecting payments using a simulated reader without a network connection.

> When operating offline, payment information is collected at the time of sale, and authorization is only attempted after connectivity is restored and the payment is forwarded. You, as the user, assume all decline and tamper-related risks associated with an offline transaction. If your tampered reader can’t forward payments to Stripe, or the issuer declines the transaction, there’s no way to recover the funds, and you might not receive payment from the customer for goods or services already provided.
>
> To reduce the chances of an issuer decline, you’re encouraged to:
>
> - Reestablish internet connectivity as soon as possible to record the payments to Stripe.

- Restrict transactions if they exceed a certain amount.
- [Fail all offline payments](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#managing-risk) if the SDK has stored a set of transactions whose sum exceeds a certain amount.

## Collect payments while offline

Offline payments follow the same steps as online payments: create, collect, process, and capture the payment. Your device can transition from online to offline at any step in the process.

1. [Enable offline mode](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#enable-offline-mode)
1. [Connect to a reader while offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#connect-while-offline)
1. [Handle offline events](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#handle-offline-events)
1. [Create a PaymentIntent while offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#create-payment-intent)
1. [Collect a payment method](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#collect-payment-method)
1. [Confirm the payment](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#confirm-payment)
1. [Wait for payments to forward](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#wait-for-forward)
1. (Optional) [Capture the payment](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#capture-payment)
1. (Optional) [Examine payments collected offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#examine-offline)

## Enable offline mode

To use offline mode, your application needs to consume version `3.3.0` or later of the Terminal iOS SDK.

Configure the simulated reader to enable offline mode.

#### Swift

```
let simulatorConfiguration = Terminal.shared.simulatorConfiguration
simulatorConfiguration.offlineEnabled = true
```

## Connect to a reader while offline

The SDK stores necessary `Location` information locally after connecting online. On subsequent offline connections, it uses the stored configuration information from that `Location`.

To collect payments with a smart reader while offline, you must have previously connected to any mobile reader of the same type at the same `Location` while online within the last 30 days, and have updated your reader’s software within that time.

If you attempt to connect to a reader while offline without meeting these requirements, the request fails with an error.

| Error                                                                                                             | Resolution                                                                                                                                                                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **The SDK isn’t connected to the internet**                                                                       | Make sure you’ve enabled offline mode on the `SimulatorConfiguration` for your simulated reader. Otherwise, connect to any reader while online, and then connect to a reader of the same type while offline.                                                                                                               |
| **The selected reader requires a software update before it can be used to collect payments offline.**             | You’ve set the `SimulateReaderUpdate` value on the SDK’s `SimulatorConfiguration` to `SimulateReaderUpdateRequiredForOffline`. Use a different value to allow offline connection.                                                                                                                                          |
| **The selected reader must be paired online at this location before it can be used to collect payments offline.** | You’re attempting to connect to a reader type that your POS hasn’t previously connected to while online. You must first connect to this reader or any reader of the same type while online. Or, if you want to connect while offline, you can connect to a reader type that your POS previously connected to while online. |

## Handle offline events [Client-side]

- [OfflineDelegate (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Protocols/SCPOfflineDelegate.html)

To allow your application to receive updates about the SDK’s network status and the state of forwarded payments, implement the `OfflineDelegate` protocol and pass it to the Terminal SDK. You must set `OfflineDelegate` before collecting payments offline.

#### Swift

```swift

import StripeTerminal

class CustomOfflineDelegate: OfflineDelegate {

    func terminal(_ terminal: Terminal, didChangeOfflineStatus offlineStatus: OfflineStatus) {
        // Check the value of `offlineStatus` and update your UI accordingly. For instance,
        // you can check the SDK's network status at `offlineStatus.sdk.networkStatus`.
        //
        // You can also check the SDK's current offline status using
        // `Terminal.shared.offlineStatus.sdk.networkStatus`.
    }

    func terminal(_ terminal: Terminal, didForwardPaymentIntent intent: PaymentIntent, error: Error?) {
        // The PaymentIntent was successfully forwarded, or an error occurred.
        // Reconcile any local state using the backend-generated `PaymentIntent.stripeId`
        // and the metadata you supplied when creating the PaymentIntent.
        //
        // Note that the `PaymentIntent.stripeId` may still be nil if creating the
        // PaymentIntent in the backend failed.
    }

    func terminal(_ terminal: Terminal, didReportForwardingError error: Error) {
        // A non-specific error occurred while forwarding a PaymentIntent.
        // Check the error message and your integration implementation to
        // troubleshoot.
    }
}
```

#### Swift

```swift
import UIKit
import StripeTerminal

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil) -> Bool {
        Terminal.initWithTokenProvider(APIClient.shared)
        Terminal.shared.offlineDelegate = CustomOfflineDelegate()
        // ...
        return true
    }

    // ...

}
```

## Create a PaymentIntent while offline [Client-side]

- [createPaymentIntent (iOS)](<https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)createPaymentIntent:completion:>)
- [CreateConfiguration (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPCreateConfiguration.html)
- [OfflineDetails (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPOfflineDetails.html)

To support operating offline, use the SDK’s `createPaymentIntent` to create PaymentIntent objects. This allows the SDK to create PaymentIntents while offline and forward them to Stripe after you’ve re-established connectivity.

While operating offline, `PaymentIntent` objects have a null `stripeId`. We recommend adding a custom identifier to the PaymentIntent’s [metadata](https://docs.stripe.com/payments/payment-intents.md#storing-information-in-metadata) to help reconcile `PaymentIntent` objects created offline in your database.

After the `PaymentIntent` has been successfully forwarded to Stripe in [Step 7](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#wait-for-forward), use your custom identifier to reconcile it in the `OfflineDelegate.didForwardPaymentIntent` callback.

#### Swift

```swift

import UIKit
import StripeTerminal

class PaymentViewController: UIViewController {

    // Action for a "Checkout" button
    func checkoutAction() throws {
        // Populate the correct transaction amount from your application.
        let amount = UInt(10_00)

        // Build up parameters for creating a `PaymentIntent`
        let params = try PaymentIntentParametersBuilder(
            amount: amount,
            currency: "sgd"
        ).setMetadata(["offlineId": UUID().uuidString])
        .build()

        Terminal.shared.createPaymentIntent(params) { createResult, createError in
            if let error = createError {
                // Handle errors in your application.
                print("createPaymentIntent failed: \(error)")
            } else if let paymentIntent = createResult {
                print("createPaymentIntent succeeded")// If the `PaymentIntent` was created offline, its `stripeId` field will be nil.
                if let onlineCreatedId = paymentIntent.stripeId {
                    print("created online");
                } else {
                    print("created offline")
                }
            }
        }
    }
}
```

The `Terminal.createPaymentIntent` accepts a `CreateConfiguration` parameter. By default, if you’re operating offline, the Terminal SDK stores all offline payments, then forwards them to Stripe’s backend when connectivity is restored.

To customize this behavior, you can pass in a `CreateConfiguration` object with an `offlineBehavior` attribute set to as `REQUIRE_ONLINE`, `PREFER_ONLINE` or `FORCE_OFFLINE`.

#### Managing risk

Setting `offlineBehavior` to `REQUIRE_ONLINE` fails the current transaction if you’re operating offline. For example, you might want to disallow transactions above a certain amount or disallow all offline transactions if the SDK has stored a set of transactions whose sum exceeds a certain amount.

The SDK exposes two properties to help you manage risk:

1. `Terminal.offlineStatus.sdk.offlinePaymentsCount`
1. `Terminal.offlineStatus.sdk.offlinePaymentAmountsByCurrency`

#### Managing latency while offline

Based on your network connectivity, the Terminal SDK automatically determines whether to collect payments online or offline. However, you might want to operate offline despite having an active network connection (for example, if you need to collect transactions quickly and your network connection is slow). You can pass a `CreateConfiguration` object with `offlineBehavior` set to `FORCE_OFFLINE` to collect the payment offline regardless of connectivity.

Payments collected offline while the Terminal SDK has an active network connection are forwarded in the background.

#### Swift

```swift

import UIKit
import StripeTerminal

class PaymentViewController: UIViewController {

    // Action for a "Checkout" button
    func checkoutAction() throws {
        // ...build up parameters and callback for creating a `PaymentIntent`

        // Your app might want to prevent offline payments for too large an amount.
        // Here, we block the payment if the amount is over 1000 sgd.
        // Otherwise, we allow collecting offline if the network connection is unavailable.let offlineBehavior: SCPOfflineBehavior = {
            if amount > UInt(1_000_00) {
                return .requireOnline
            } else {
                return .preferOnline
            }
        }()

        let createConfiguration = try CreateConfigurationBuilder().setOfflineBehavior(offlineBehavior).build()
        Terminal.shared.createPaymentIntent(params, createConfig: createConfiguration) { createResult, createError in
            // handle success or failure
        }
    }
}
```

## Collect a payment method [Client-side]

- [CollectPaymentIntentConfiguration (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPCollectPaymentIntentConfiguration.html)

> Payment liability is your responsibility when operating your reader offline. Because magnetic stripe data is easy to spoof, Stripe disallows this option while operating offline. Tapping cards is also not supported in markets where _Strong Customer Authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase) is required.

Collecting payments while offline is similar to [collecting payments while online](https://docs.stripe.com/terminal/payments/collect-card-payment.md#collect-payment). Use the `didRequestReaderInput` method to display the valid card presentment options to the customer.

> Readers don’t support [inspecting payment method details before authorization](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=ios#collect-inspect-payment-method) while offline. Although you can still use the `initWithUpdatePaymentIntent` parameter in `CollectPaymentIntentConfiguration`, the `paymentMethod` field on the PaymentIntent is absent if the SDK is operating offline.

#### Swift

```swift

import UIKit
import StripeTerminal

class PaymentViewController: UIViewController {

    // Action for a "Checkout" button
    func checkoutAction() {
        Terminal.shared.collectPaymentMethod(paymentIntent) { collectResult, collectError in
            if let error = collectError {
                print("collectPaymentMethod failed: \(error)")
            }
            else if let paymentIntent = collectResult {
                print("collectPaymentMethod succeeded")
                // ... Confirm the payment
            }
        }
    }
}
```

## Confirm payment [Client-side]

Confirming payments while offline is similar to [confirming payments while online](https://docs.stripe.com/terminal/payments/collect-card-payment.md#confirm-payment). The primary difference is that your integration must handle offline-specific error cases, such as when the transaction exceeds the Stripe-enforced offline maximum of 10,000 USD or equivalent in your operating currency.

In some cases, the SDK might create a `PaymentIntent` online, but confirm it while offline. When this happens, the `PaymentIntent` might have a non-null `stripeId`. If it was confirmed offline, `offlineDetails` will be defined and populated.

The simulated reader can be configured to use a simulated test card, enabling you to test various offline-specific flows during confirmation. For example, you can:

- Use the simulated Interac test card number to test errors while confirming a `PaymentIntent` offline for payment methods that aren’t supported
- Use a test card number that [results in a declined charge](https://docs.stripe.com/terminal/references/testing.md#test-cards-for-specific-error-cases) to test failures to forward a stored `PaymentIntent`

For a full list of available options, see [Test Stripe Terminal](https://docs.stripe.com/terminal/references/testing.md).

#### Swift

```swift


import UIKit
import StripeTerminal

class PaymentViewController: UIViewController {

    // Action for a "Checkout" button
    func checkoutAction() {

        Terminal.shared.confirmPaymentIntent(paymentIntent) { confirmResult, confirmError in
            if let error = confirmError {
                // Handle offline-specific errors in your application (for example,
                // unsupported payment method).
                print("confirmPaymentIntent failed: \(error)")
            } else if let confirmedPaymentIntent= confirmResult {print("confirmPaymentIntent succeeded")
                if let offlineDetails = paymentIntent.offlineDetails {
                    print("confirmed offline");
                } else {
                    print("confirmed online")
                }
            }
        }
    }
}
```

#### Providing receipts

You might require information about the card used to complete a payment while offline. For example, you might need to generate a receipt for customers who require one at the time of purchase.

If the PaymentIntent is confirmed offline, retrieve its [OfflineCardPresentDetails](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPOfflineCardPresentDetails.html) from the `paymentIntent.offlineDetails.offlineCardPresentDetails` property.

This hash contains a [ReceiptDetails](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPReceiptDetails.html) property you can use to generate a receipt, as well as other card details like the cardholder name and card brand.

The `account_type` and `authorization_response_code` receipt fields are unavailable on PaymentIntents processed offline. [Prebuilt email receipts](https://docs.stripe.com/terminal/features/receipts.md#prebuilt) are only sent after connectivity is restored and the payment is successfully captured.

## Wait for payments to forward [Client-side]

When Internet access is restored, the SDK automatically begins forwarding the stored offline payments.

The SDK attempts to forward payments even if its network status is offline. This means your connection token provider might receive a request to provide a connection token even when the device is offline.

If you power off your POS device too soon, your payments might not be forwarded. You can query `Terminal.offlineStatus.sdk.networkStatus` to make sure your POS is online and can forward payments, and `Terminal.offlineStatus.sdk.offlinePaymentsCount` to check how many payments the Terminal SDK has to be forwarded.

## Capture payment

While offline, you can create PaymentIntents with `captureMethod` set to `automatic`.

After you confirm these PaymentIntents, they have a `Succeeded` status instead of `RequiresCapture`. Stripe automatically captures the payments after you forward them.

If you opt for manual capture, payments that are successfully forwarded and authorized require capture from your backend or application.

- To capture payments from your backend, use [webhooks](https://docs.stripe.com/webhooks.md) to listen for PaymentIntents with a `requires_capture` status.
- To capture payments from your application, wait for your application to receive calls to `OfflineDelegate.didForwardPayment` for each PaymentIntent as the SDK forwards it. A PaymentIntent is ready to capture if its status is `RequiresCapture` and the `offlineDetails` is null or has a `requiresUpload` value of `NO` .

#### Swift

```swift

Terminal.shared.confirmPaymentIntent(paymentIntent) { confirmResult, confirmError in
    if let error = confirmError {
        // Handle offline-specific errors in your application (for example,
        // unsupported payment method).
        print("confirmPaymentIntent failed: \(error)")
    } else if let confirmedPaymentIntent = confirmResult {
        if intent.status == .requiresCapture {if let offlineDetails = confirmedPaymentIntent.offlineDetails(),
               offlineDetails.requiresUpload {
                // Offline payment, wait for `didForwardPaymentIntent` (see snippet below)
            } else {
                // Online payment, can be captured now
            }
        }
        // else, handle other intent.status results here
    }
}
```

Capture an offline payment after the SDK forwards it in your OfflineDelegate’s `didForwardPaymentIntent`:

#### Swift

```swift

import StripeTerminal

class CustomOfflineDelegate: OfflineDelegate {
    // ...
    func terminal(_ terminal: Terminal, didForwardPaymentIntent intent: PaymentIntent, error: Error?) {
        if let error = error {
            // Handle the error appropriate for your application
            return
        }

        if intent.status == .requiresCapture {
            // The intent is ready to be captured.
        } else {
            // Handle the intent.status as appropriate.
        }
    }
    // ...
}
```

## Examine payments collected offline

After authorization, you can use the [PaymentIntents](https://docs.stripe.com/payments/payment-intents.md) API to examine offline details on a payment. Access the [payment method details](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-offline) on the [latest Charge](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-latest_charge) object on a `PaymentIntent` to determine if it was collected offline.

# Android

> This is a Android for when terminal-card-present-integration is terminal and terminal-sdk-platform is android and reader-type is simulated. View the full page at https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments?terminal-card-present-integration=terminal&terminal-sdk-platform=android&reader-type=simulated.

The Terminal SDK allows your application to continue collecting payments using a simulated reader without a network connection.

> When operating offline, payment information is collected at the time of sale, and authorization is only attempted after connectivity is restored and the payment is forwarded. You, as the user, assume all decline and tamper-related risks associated with an offline transaction. If your tampered reader can’t forward payments to Stripe, or the issuer declines the transaction, there’s no way to recover the funds, and you might not receive payment from the customer for goods or services already provided.
>
> To reduce the chances of an issuer decline, you’re encouraged to:
>
> - Reestablish internet connectivity as soon as possible to record the payments to Stripe.

- Restrict transactions if they exceed a certain amount.
- [Fail all offline payments](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#managing-risk) if the SDK has stored a set of transactions whose sum exceeds a certain amount.

## Collect payments while offline

Offline payments follow the same steps as online payments: create, collect, process, and capture the payment. Your device can transition from online to offline at any step in the process.

1. [Enable offline mode](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#enable-offline-mode)
1. [Connect to a reader while offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#connect-while-offline)
1. [Handle offline events](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#handle-offline-events)
1. [Create a PaymentIntent while offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#create-payment-intent)
1. [Collect a payment method](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#collect-payment-method)
1. [Confirm the payment](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#confirm-payment)
1. [Wait for payments to forward](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#wait-for-forward)
1. (Optional) [Capture the payment](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#capture-payment)
1. (Optional) [Examine payments collected offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#examine-offline)

## Enable offline mode

To use offline mode, your application needs to consume version `3.2.0` or later of the Terminal Android SDK.

Configure the simulated reader to enable offline mode.

#### Kotlin

```
val simulatorConfig = SimulatorConfiguration(
    offlineEnabled = true
);

Terminal.getInstance().setSimulatorConfiguration(simulatorConfig);
```

## Connect to a reader while offline

The SDK stores necessary `Location` information locally after connecting online. On subsequent offline connections, it uses the stored configuration information from that `Location`.

To collect payments with a smart reader while offline, you must have previously connected to any mobile reader of the same type at the same `Location` while online within the last 30 days, and have updated your reader’s software within that time.

If you attempt to connect to a reader while offline without meeting these requirements, the request fails with an error.

| Error                                                                                                             | Resolution                                                                                                                                                                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **The SDK isn’t connected to the internet**                                                                       | Make sure you’ve enabled offline mode on the `SimulatorConfiguration` for your simulated reader. Otherwise, connect to any reader while online, and then connect to a reader of the same type while offline.                                                                                                               |
| **The selected reader requires a software update before it can be used to collect payments offline.**             | You’ve set the `SimulateReaderUpdate` value on the SDK’s `SimulatorConfiguration` to `REQUIRED_FOR_OFFLINE`. Use a different value to allow offline connection.                                                                                                                                                            |
| **The selected reader must be paired online at this location before it can be used to collect payments offline.** | You’re attempting to connect to a reader type that your POS hasn’t previously connected to while online. You must first connect to this reader or any reader of the same type while online. Or, if you want to connect while offline, you can connect to a reader type that your POS previously connected to while online. |

## Handle offline events [Client-side]

- [OfflineListener (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.callable/-offline-listener/index.html)

To allow your application to receive updates about the SDK’s network status and the state of forwarded payments, implement the `OfflineListener` interface and pass it to the Terminal SDK. You must set `OfflineListener` before collecting payments offline.

#### Kotlin

```kotlin
class CustomOfflineListener : OfflineListener {
    override fun onOfflineStatusChange(offlineStatus: OfflineStatus) {
        // Check the value of `offlineStatus` and update your UI accordingly. For instance,
        // you can check the SDK's network status at `offlineStatus.sdk.networkStatus`.
        //
        // You can also check the SDK's current offline status using
        // `Terminal::offlineStatus`.
    }

    override fun onPaymentIntentForwarded(paymentIntent: PaymentIntent, e: TerminalException?) {
        // The PaymentIntent was successfully forwarded, or an error occurred.
        // Reconcile any local state using the backend-generated `PaymentIntent::id`
        // and the metadata you supplied when creating the PaymentIntent.
        //
        // Note that the `PaymentIntent::id` may still be null if creating the
        // PaymentIntent in the backend failed.
    }

    override fun onForwardingFailure(e: TerminalException) {
        // A non-specific error occurred while forwarding a PaymentIntent.
        // Check the error message and your integration implementation to
        // troubleshoot.
    }
}
```

#### Kotlin

```kotlin
Terminal.init(
    context = applicationContext,
    logLevel = LogLevel.VERBOSE,
    tokenProvider = CustomConnectionTokenProvider(),
    listener = CustomTerminalListener(),
    offlineListener = CustomOfflineListener(),
)
```

## Create a PaymentIntent while offline [Client-side]

- [createPaymentIntent (Android)](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/create-payment-intent.html)
- [CreateConfiguration (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-create-configuration/index.html)
- [OfflineDetails (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-offline-details/index.html)

To support operating offline, use the SDK’s `createPaymentIntent` to create PaymentIntent objects. This allows the SDK to create PaymentIntents while offline and forward them to Stripe after you’ve re-established connectivity.

While operating offline, `PaymentIntent` objects have a null `id`. We recommend adding a custom identifier to the PaymentIntent’s [metadata](https://docs.stripe.com/payments/payment-intents.md#storing-information-in-metadata) to help reconcile `PaymentIntent` objects created offline in your database.

After the `PaymentIntent` has been successfully forwarded to Stripe in [Step 7](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md#wait-for-forward), use your custom identifier to reconcile it in the `OfflineListener::onPaymentIntentForwarded` callback.

#### Kotlin

```kotlin
private const val TAG = "PaymentActivity"

class PaymentActivity : AppCompatActivity() {
    // Action for a "Checkout" button
    private fun onCheckout(cart: Cart) {
        // Build up parameters for creating a `PaymentIntent`
        val params = PaymentIntentParameters.Builder()
            .setAmount(cart.total)
            .setCurrency(cart.currency).setMetadata(mapOf("unique-id" to UUID.randomUUID().toString()))
            .build()

        val createPaymentCallback: PaymentIntentCallback = object : PaymentIntentCallback {
            override fun onSuccess(paymentIntent: PaymentIntent) {
                Log.d(TAG, "createPaymentIntent succeeded")// If the `PaymentIntent` was created offline, its `id` field will be null.
                if (paymentIntent.id != null) {
                    Log.d(TAG, "created online")
                } else {
                    Log.d(TAG, "created offline")
                }
                // ... Collect a PaymentMethod
            }

            override fun onFailure(e: TerminalException) {
                Log.e(TAG, "createPaymentIntent failed", e)
                // Handle errors in your application.
            }
        }
        Terminal.getInstance().createPaymentIntent(params, createPaymentCallback)
    }
}
```

The `Terminal.createPaymentIntent` accepts a `CreateConfiguration` parameter. By default, if you’re operating offline, the Terminal SDK stores all offline payments, then forwards them to Stripe’s backend when connectivity is restored.

To customize this behavior, you can pass in a `CreateConfiguration` object with an `offlineBehavior` attribute set to as `REQUIRE_ONLINE`, `PREFER_ONLINE` or `FORCE_OFFLINE`.

#### Managing risk

Setting `offlineBehavior` to `REQUIRE_ONLINE` fails the current transaction if you’re operating offline. For example, you might want to disallow transactions above a certain amount or disallow all offline transactions if the SDK has stored a set of transactions whose sum exceeds a certain amount.

The SDK exposes two properties to help you manage risk:

1. `Terminal.offlineStatus.sdk.offlinePaymentsCount`
1. `Terminal.offlineStatus.sdk.offlinePaymentAmountsByCurrency`

#### Managing latency while offline

Based on your network connectivity, the Terminal SDK automatically determines whether to collect payments online or offline. However, you might want to operate offline despite having an active network connection (for example, if you need to collect transactions quickly and your network connection is slow). You can pass a `CreateConfiguration` object with `offlineBehavior` set to `FORCE_OFFLINE` to collect the payment offline regardless of connectivity.

Payments collected offline while the Terminal SDK has an active network connection are forwarded in the background.

#### Kotlin

```kotlin
private const val TAG = "PaymentActivity"

class PaymentActivity : AppCompatActivity() {
    // Action for a "Checkout" button
    private fun onCheckout(cart: Cart) {
        // ...build up parameters and callback for creating a `PaymentIntent`

        // Your app might want to prevent offline payments for too large an amount.
        // Here, we require a network connection if the payment if the amount is over 1000 sgd.
        // Otherwise, we allow collecting offline if the network connection is unavailable.val offlineBehavior = if (cart.total > 1000000) {
            OfflineBehavior.REQUIRE_ONLINE
        } else {
            OfflineBehavior.PREFER_ONLINE
        }
        val createConfig = CreateConfiguration(offlineBehavior)

        Terminal.getInstance().createPaymentIntent(params, createPaymentCallback, createConfig)
    }
}
```

## Collect a payment method [Client-side]

- [CollectPaymentIntentConfiguration (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-collect-payment-intent-configuration/index.html)

> Payment liability is your responsibility when operating your reader offline. Because magnetic stripe data is easy to spoof, Stripe disallows this option while operating offline. Tapping cards is also not supported in markets where _Strong Customer Authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase) is required.

Collecting payments while offline is similar to [collecting payments while online](https://docs.stripe.com/terminal/payments/collect-card-payment.md#collect-payment). Use the `onRequestReaderInput` method to display the valid card presentment options to the customer.

> Readers don’t support [inspecting payment method details before authorization](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=android#collect-inspect-payment-method) while offline. Although you can still set the `updatePaymentIntent` parameter in `CollectPaymentIntentConfiguration`, the `paymentMethod` field on the PaymentIntent is absent if the SDK is operating offline.

#### Kotlin

```kotlin
private const val TAG = "PaymentActivity"

class PaymentActivity : AppCompatActivity() {
    // Action for a "Checkout" button
    private fun onCheckout(cart: Cart) {
        val collectPaymentCallback: PaymentIntentCallback = object : PaymentIntentCallback {
            override fun onSuccess(paymentIntent: PaymentIntent) {
                Log.d(TAG, "collectPaymentMethod succeeded")
                // ... Confirm the payment
            }

            override fun onFailure(e: TerminalException) {
                Log.d(TAG, "collectPaymentMethod failed:", e)
            }
        }
        val collectConfig = CollectPaymentIntentConfiguration.Builder().build()
        Terminal.getInstance().collectPaymentMethod(paymentIntent, collectPaymentCallback, collectConfig)
    }
}
```

## Confirm payment [Client-side]

Confirming payments while offline is similar to [confirming payments while online](https://docs.stripe.com/terminal/payments/collect-card-payment.md#confirm-payment). The primary difference is that your integration must handle offline-specific error cases, such as when the transaction exceeds the Stripe-enforced offline maximum of 10,000 USD or equivalent in your operating currency.

In some cases, the SDK might create a `PaymentIntent` online, but confirm it while offline. When this happens, the `PaymentIntent` might have a non-null `id`. If it was confirmed offline, `offlineDetails` will be defined and populated.

The simulated reader can be configured to use a simulated test card, enabling you to test various offline-specific flows during confirmation. For example, you can:

- Use the simulated Interac test card number to test errors while confirming a `PaymentIntent` offline for payment methods that aren’t supported
- Use a test card number that [results in a declined charge](https://docs.stripe.com/terminal/references/testing.md#test-cards-for-specific-error-cases) to test failures to forward a stored `PaymentIntent`

For a full list of available options, see [Test Stripe Terminal](https://docs.stripe.com/terminal/references/testing.md).

#### Kotlin

```kotlin
private const val TAG = "PaymentActivity"

class PaymentActivity : AppCompatActivity() {
    // Action for a "Checkout" button
    private fun onCheckout(cart: Cart) {
        val confirmPaymentIntentCallback: PaymentIntentCallback = object : PaymentIntentCallback {
            override fun onSuccess(paymentIntent: PaymentIntent) {
                Log.d(TAG, "confirmPaymentIntent succeeded")// If the `PaymentIntent` was confirmed offline, `paymentIntent.offlineDetails` will be defined
                if (paymentIntent.offlineDetails != null) {
                    Log.d(TAG, "confirmed offline")
                } else {
                    Log.d(TAG, "confirmed online")
                }
            }

            override fun onFailure(e: TerminalException) {
                // Handle offline-specific errors in your application (for example,
                // unsupported payment method).
                Log.e(TAG, "confirmPaymentIntent failed:", e)
            }
        }
        Terminal.getInstance().confirmPaymentIntent(paymentIntent, confirmPaymentIntentCallback)
    }
}
```

#### Providing receipts

You might require information about the card used to complete a payment while offline. For example, you might need to generate a receipt for customers who require one at the time of purchase.

If the PaymentIntent is confirmed offline, retrieve its [OfflineCardPresentDetails](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-offline-card-present-details/index.html) from the `paymentIntent.offlineDetails.offlineCardPresentDetails` property.

This hash contains a [ReceiptDetails](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-receipt-details/index.html) property you can use to generate a receipt, as well as other card details like the cardholder name and card brand.

The `account_type` and `authorization_response_code` receipt fields are unavailable on PaymentIntents processed offline. [Prebuilt email receipts](https://docs.stripe.com/terminal/features/receipts.md#prebuilt) are only sent after connectivity is restored and the payment is successfully captured.

## Wait for payments to forward [Client-side]

When Internet access is restored, the SDK automatically begins forwarding the stored offline payments.

The SDK attempts to forward payments even if its network status is offline. This means your connection token provider might receive a request to provide a connection token even when the device is offline.

If you power off your POS device too soon, your payments might not be forwarded. You can query `Terminal.offlineStatus.sdk.networkStatus` to make sure your POS is online and can forward payments, and `Terminal.offlineStatus.sdk.offlinePaymentsCount` to check how many payments the Terminal SDK has to be forwarded.

## Capture payment

While offline, you can create PaymentIntents with `captureMethod` set to `automatic`.

After you confirm these PaymentIntents, they have a `SUCCEEDED` status instead of `REQUIRES_CAPTURE` . Stripe automatically captures the payments after you forward them.

If you opt for manual capture, payments that are successfully forwarded and authorized require capture from your backend or application.

- To capture payments from your backend, use [webhooks](https://docs.stripe.com/webhooks.md) to listen for PaymentIntents with a `requires_capture` status.
- To capture payments from your application, wait for your application to receive calls to `OfflineListener::onPaymentIntentForwarded` for each PaymentIntent as the SDK forwards it. A PaymentIntent is ready to capture if its status is `REQUIRES_CAPTURE` and the `offlineDetails` is null or has a `requiresUpload` value of `false` .

#### Kotlin

```kotlin
private const val TAG = "PaymentActivity"

class PaymentActivity : AppCompatActivity() {
    // Action for a "Checkout" button
    private fun onCheckout(cart: Cart) {
        val callback: PaymentIntentCallback = object : PaymentIntentCallback {
            override fun onSuccess(paymentIntent: PaymentIntent) {
                Log.d(TAG, "confirmPaymentIntent succeeded")
                if (paymentIntent.status == PaymentIntentStatus.REQUIRES_CAPTURE) {val offlineDetails = paymentIntent.offlineDetails
                    if (offlineDetails?.requiresUpload == true) {
                        // Offline payment, wait for `onPaymentIntentForwarded` (see snippet below)
                    } else {
                        // Online payment, can be captured now
                    }
                } else {
                    // Handle other status results here
                }
            }

            override fun onFailure(e: TerminalException) {
                // Handle offline-specific errors in your application (for example,
                // unsupported payment method).
                Log.e(TAG, "confirmPaymentIntent failed:", e)
            }
        }

        Terminal.getInstance().confirmPaymentIntent(paymentIntent, callback)
    }
}
```

Capture an offline payment after the SDK forwards it in your `OfflineListener::onPaymentIntentForwarded`:

#### Kotlin

```kotlin
class CustomOfflineListener : OfflineListener {
    // ...

    override fun onPaymentIntentForwarded(paymentIntent: PaymentIntent, e: TerminalException?) {
        if (e != null) {
            // Handle the error appropriate for your application
        } else if (paymentIntent.status == PaymentIntentStatus.REQUIRES_CAPTURE) {
            // The paymentIntent is ready to be captured
        } else {
            // Handle other status results here
        }
    }

    // ...
}
```

## Examine payments collected offline

After authorization, you can use the [PaymentIntents](https://docs.stripe.com/payments/payment-intents.md) API to examine offline details on a payment. Access the [payment method details](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-offline) on the [latest Charge](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-latest_charge) object on a `PaymentIntent` to determine if it was collected offline.
