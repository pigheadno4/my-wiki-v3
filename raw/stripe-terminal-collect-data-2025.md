<!-- Source URL: https://docs.stripe.com/terminal/features/collect-data -->
<!-- Fetched: 2026-05-01 -->

# Collect swiped data

Use Terminal for collecting non-PCI data with the reader hardware interfaces.

> Request access to the Collect data private preview by sending an email to [terminal-collect-data@stripe.com](mailto:terminal-collect-data@stripe.com) with the following information:
>
> - Use case

- Terminal device and integration type
- Magstripe data format
- Provider, if using a third-party card provider

Use the Terminal SDK and the reader’s hardware interfaces (such as the magnetic stripe reader) to read non-PCI payment methods such as gift cards. This feature isn’t available offline.

After swiping the card, Stripe provides a tokenized data object. Use the token to securely retrieve the cleartext track data on your back end.

The Terminal reader only reads and stores cleartext magstripe data that follows these formats:

- The card data is available on track 2 only.
- The card data uses only the [ISO/IEC-7813](https://en.wikipedia.org/wiki/ISO/IEC_7813) track 2 start sentinel `;` and end sentinel `?`, without the separator character.
- The card data consists of only numeric digits.

[Contact the Terminal team](mailto:terminal-collect-data@stripe.com) with your card format and BIN ranges if your card numbers don’t match one of these approved formats.

Collecting swiped data is available on:

- [Stripe Reader S700/S710](https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710.md), [BBPOS WisePOS E](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e.md), [Stripe M2](https://docs.stripe.com/terminal/readers/stripe-m2.md), and [BBPOS Chipper2X BT](https://docs.stripe.com/terminal/readers/bbpos-chipper2xbt.md)

# iOS

> This is a iOS for when terminal-sdk-platform is ios. View the full page at https://docs.stripe.com/terminal/features/collect-data?terminal-sdk-platform=ios.

## Collect data

- [collectData (iOS)](<https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)collectData:completion:>)

Use `Terminal.collectData()` to prompt your point-of-sale application to collect data. Specify the type of data you want to receive in the configuration passed to the function, such as `.magstripe`. After a customer swipes a card, the SDK returns a token that represents the data or an error if the swipe fails. Use this token in your integration to refer to the data.

> On supported readers, the ability for customers to cancel transactions is now _enabled by default_. To disable customer cancellation on smart readers, set `customerCancellation` to `.disableIfAvailable`.

#### Swift

```swift
import UIKit
import StripeTerminal

class PaymentViewController: UIViewController {
    func readGiftCard() throws {
        let config = try CollectDataConfigurationBuilder()
            .setCollectDataType(.magstripe)
            .build()
        self.cancelable = Terminal.shared.collectData(config) { collectedData, collectError in
            if let error = collectError {
                // Handle read errors
                print("Collect data failed: \(error)")
            } else if let data = collectedData, let stripeId = data.stripeId {
                print("Received collected data token: \(stripeId)")
            }
        }
    }
}
```

## Fetch collected data

When you need to perform operations such as redeeming a gift card, [fetch the cleartext data](https://docs.stripe.com/api/terminal/reader-collected_data.md) from your backend using the collected data token. The collected data is stored on Stripe’s servers for 24 hours.

```curl
curl https://api.stripe.com/v1/terminal/reader_collected_data/tmrcd_xxxxxxxx \
  -u "<<YOUR_SECRET_KEY>>:"
```

> Stripe doesn’t perform and isn’t responsible for the authentication of collected data or the authorization of transactions using collected data. Stripe isn’t liable for any illegal conduct or fraud by any third party associated with the collected data.

# Android

> This is a Android for when terminal-sdk-platform is android. View the full page at https://docs.stripe.com/terminal/features/collect-data?terminal-sdk-platform=android.

## Collect data

- [collectData (Android)](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/collect-data.html)

Use `Terminal.collectData()` to prompt your point-of-sale application to collect data. Specify the type of data you want to receive in the configuration passed to the function, such as `MAGSTRIPE`. After a customer swipes a card, the SDK returns a token that represents the data or an error if the swipe fails. Use this token in your integration to refer to the data.

> On supported readers, the ability for customers to cancel transactions is now _enabled by default_. To disable customer cancellation on smart readers, set `customerCancellation` to `DISABLE_IF_AVAILABLE`.

#### Kotlin

```kotlin
val config = CollectDataConfiguration.Builder()
    .setType(CollectDataType.MAGSTRIPE)
    .build()
val cancelable = Terminal.getInstance().collectData(
    config,
    callback = object : CollectedDataCallback {
        override fun onSuccess(collectedData: CollectedData) {
            // Placeholder for handling successful operation
        }

        override fun onFailure(e: TerminalException) {
            // Placeholder for handling exception
        }
    }
)
```

## Fetch collected data

When you need to perform operations such as redeeming a gift card, [fetch the cleartext data](https://docs.stripe.com/api/terminal/reader-collected_data.md) from your backend using the collected data token. The collected data is stored on Stripe’s servers for 24 hours.

```curl
curl https://api.stripe.com/v1/terminal/reader_collected_data/tmrcd_xxxxxxxx \
  -u "<<YOUR_SECRET_KEY>>:"
```

> Stripe doesn’t perform and isn’t responsible for the authentication of collected data or the authorization of transactions using collected data. Stripe isn’t liable for any illegal conduct or fraud by any third party associated with the collected data.

# React Native

> This is a React Native for when terminal-sdk-platform is react-native. View the full page at https://docs.stripe.com/terminal/features/collect-data?terminal-sdk-platform=react-native.

## Collect data

- [collectData (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#collectdata)

Use `collectData()` to prompt your point-of-sale application to collect data. Specify the type of data you want to receive in the configuration passed to the function, such as `MAGSTRIPE`. After a customer swipes a card, the SDK returns a token that represents the data or an error if the swipe fails. Use this token in your integration to refer to the data.

```javascript
import { CollectDataType } from '@stripe/stripe-terminal-react-native';

const readGiftCard = async () => {
  try {
    let collectDataType = CollectDataType.MAGSTRIPE;

    const { collectedData, error } = await collectData({
      collectDataType: collectDataType,
      customerCancellation: 'disableIfAvailable',
    });

    if (error) {
      // Handle read errors
      console.error('Collect data failed:', error);
    } else if (collectedData?.stripeId) {
      console.log('Received collected data token:', collectedData.stripeId);
    }
  } catch (e) {
    // Handle any unexpected errors
    console.error('Error collecting data:', e);
  }
};
```

## Fetch collected data

When you need to perform operations such as redeeming a gift card, [fetch the cleartext data](https://docs.stripe.com/api/terminal/reader-collected_data.md) from your backend using the collected data token. The collected data is stored on Stripe’s servers for 24 hours.

```curl
curl https://api.stripe.com/v1/terminal/reader_collected_data/tmrcd_xxxxxxxx \
  -u "<<YOUR_SECRET_KEY>>:"
```

> Stripe doesn’t perform and isn’t responsible for the authentication of collected data or the authorization of transactions using collected data. Stripe isn’t liable for any illegal conduct or fraud by any third party associated with the collected data.
