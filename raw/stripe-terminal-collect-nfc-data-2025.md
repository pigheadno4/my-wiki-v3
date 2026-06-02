<!-- Source URL: https://docs.stripe.com/terminal/features/collect-nfc-data -->
<!-- Fetched: 2026-05-01 -->

# Collect tapped data for NFC instruments

Use Terminal for data collection of NFC instruments with the reader hardware interfaces.

> Request access to the Collect data private preview by sending an email to [terminal-collect-data@stripe.com](mailto:terminal-collect-data@stripe.com). Provide your use case, Terminal device, and integration type.

Use the Terminal SDK and the reader’s contactless interface to read the unique identifier (UID) of NFC instruments, such as cards or wristbands. This feature is available offline.

After tapping your NFC instrument, Stripe provides a collected data object with the NFC UID, or an error if one occurred.

> #### Warning
>
> You can’t use this feature to collect card payments. Follow [these instructions](https://docs.stripe.com/terminal/payments/collect-card-payment.md) to collect payments using Stripe Terminal.

Collecting tapped data for NFC instruments is available on:

- [Stripe Reader S700/S710](https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710.md) and [Stripe M2](https://docs.stripe.com/terminal/readers/stripe-m2.md)

# iOS

> This is a iOS for when terminal-sdk-platform is ios. View the full page at https://docs.stripe.com/terminal/features/collect-nfc-data?terminal-sdk-platform=ios.

## Collect data

- [collectData (iOS)](<https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)collectData:completion:>)

Use `Terminal.collectData()` to prompt for data collection from your point-of-sale application. Specify the type of collected data you want to receive, such as `.nfcUid`, in a configuration passed to the function. After a customer taps an NFC instrument, the SDK collects a data object with the NFC UID or returns an error if the read is unsuccessful.

> On supported readers, the ability for customers to cancel transactions is now _enabled by default_. To disable customer cancellation on smart readers, set `customerCancellation` to `.disableIfAvailable`.

#### Swift

```swift
import UIKit
import StripeTerminal

class PaymentViewController: UIViewController {
    func readNfcUid() throws {
        let config = try CollectDataConfigurationBuilder().setCollectDataType(.nfcUid).build()
        self.cancelable = Terminal.shared.collectData(config) { collectedData, collectError in
            if let error = collectError {
                // Placeholder for handling exceptions
            } else if let nfcUid = collectedData?.nfcUid {
                // Placeholder for receiving NFC UID
                print("NFC UID is: \(nfcUid)")
            }
        }
    }
}
```

# Android

> This is a Android for when terminal-sdk-platform is android. View the full page at https://docs.stripe.com/terminal/features/collect-nfc-data?terminal-sdk-platform=android.

## Collect data

- [collectData (Android)](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/collect-data.html)

Use `Terminal.collectData()` to prompt for data collection from your point-of-sale application. Specify the type of collected data you want to receive, such as `NFC_UID`, in a configuration passed to the function. After a customer taps an NFC instrument, the SDK collects a data object with the NFC UID or returns an error if the read is unsuccessful.

> On supported readers, the ability for customers to cancel transactions is now _enabled by default_. To disable customer cancellation on smart readers, set `customerCancellation` to `DISABLE_IF_AVAILABLE`.

#### Kotlin

```kotlin
val config = CollectDataConfiguration.Builder()
    .setType(CollectDataType.NFC_UID)
    .build()
val cancelable = Terminal.getInstance().collectData(config,
    object : CollectedDataCallback {
        override fun onSuccess(collectedData: CollectedData) {
            // Placeholder for receiving NFC UID
            collectedData.nfcUid?.let {
                print("NFC UID is $it")
            }
        }

        override fun onFailure(exception: TerminalException) {
            // Placeholder for handling exception
        }
    }
)
```

# React Native

> This is a React Native for when terminal-sdk-platform is react-native. View the full page at https://docs.stripe.com/terminal/features/collect-nfc-data?terminal-sdk-platform=react-native.

## Collect data

- [collectData (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#collectdata)

Use `collectData()` to prompt for data collection from your point-of-sale application. Specify the type of collected data you want to receive, such as `NFC_UID`, in a configuration passed to the function. After a customer taps an NFC instrument, the SDK collects a data object with the NFC UID or returns an error if the read is unsuccessful.

```javascript
import { CollectDataType } from '@stripe/stripe-terminal-react-native';

const readNfcUid = async () => {
  try {
    let collectDataType = CollectDataType.NFC_UID;

    const { collectedData, error } = await collectData({
      collectDataType: collectDataType,
      customerCancellation: 'disableIfAvailable',
    });

    if (error) {
      // Placeholder for handling exceptions
      console.error('Collect data failed:', error);
    } else if (collectedData?.nfcUid) {
      // Placeholder for receiving NFC UID
      console.log('NFC UID is:', collectedData.nfcUid);
    }
  } catch (e) {
    // Handle any unexpected errors
    console.error('Error collecting NFC data:', e);
  }
};
```
