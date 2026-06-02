<!-- Source: Stripe Terminal — Tap to Pay (iPhone + Android) -->
<!-- Fetched: 2026-04-24 -->

# Tap to Pay

Learn how to accept contactless payments on a compatible iPhone or Android device.

Looking for a no-code solution? [Accept payments from the Stripe Dashboard mobile app](https://docs.stripe.com/no-code/in-person.md).

# iPhone

> This is a iPhone for when platform is ios. View the full page at https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay?platform=ios.

Use Tap to Pay on iPhone to accept in-person contactless payments with a [compatible iPhone](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay.md?platform=ios#supported-devices).

Tap to Pay on iPhone includes support for Visa, Mastercard, American Express, and Discover contactless cards, NFC-based mobile wallets, and [QR-based payment methods](https://docs.stripe.com/terminal/payments/additional-payment-methods.md). PIN entry is supported. Additionally, [eftpos](https://docs.stripe.com/terminal/payments/regional.md?integration-country=AU#eftpos-payments) is supported in Australia, [Interac](https://docs.stripe.com/terminal/payments/regional.md?integration-country=CA#interac-payments) is supported in Canada, and [Cartes Bancaires](https://docs.stripe.com/terminal/payments/regional.md?integration-country=FR#cartes-bancaires-payments) is supported in France. Stripe includes Tap to Pay on iPhone in the Terminal iOS SDK and the Terminal React Native SDK, and enables payments directly in your iOS mobile app.

> For platforms, use of Tap to Pay on iPhone is subject to the [Apple Acceptance Platform User Terms and Conditions](https://stripe.com/legal/apple-acceptance-platform).

### Availability

- AT
- AU
- BE
- CA
- CH
- CZ
- DE
- DK
- ES
- FR
- GB
- IE
- IT
- NL
- NZ
- PL
- PT
- SE
- SG
- US

> Tap to Pay on iPhone isn’t available in Puerto Rico.

### Availability in (Public preview)

- BG
- CY
- EE
- FI
- HR
- HU
- JP
- LI
- LT
- LU
- LV
- MT
- MY
- NO
- RO
- SI
- SK

## Get started

#### iOS

Tap to Pay on iPhone introduces an [SCPDiscoveryMethodTapToPay](https://stripe.dev/stripe-terminal-ios/docs/Enums/SCPDiscoveryMethod.html#/c:@E@SCPDiscoveryMethod@SCPDiscoveryMethodTapToPay) discovery option and a [connectReader](<https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)connectReader:delegate:connectionConfig:completion:>) method. Integrate the latest version of the [Terminal iOS SDK](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=ios) to include the latest bug fixes and features. You can view version-specific updates and bug fixes in the [SDK changelog](https://github.com/stripe/stripe-terminal-ios/blob/master/CHANGELOG.md).

Device and minimum SDK version requirements can change due to updated compliance requirements or security vulnerabilities. To make sure your solution is up to date with Tap to Pay requirements, subscribe to [terminal-announce@lists.stripe.com](https://groups.google.com/a/lists.stripe.com/g/terminal-announce).

To enable Tap to Pay in your iOS application:

1. [Request](https://developer.apple.com/documentation/proximityreader/setting-up-the-entitlement-for-tap-to-pay-on-iphone?language=objc) an entitlement.
1. [Set up](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=iOS) the Terminal iOS SDK.
1. [Connect](https://docs.stripe.com/terminal/payments/connect-reader.md?terminal-sdk-platform=ios&reader-type=tap-to-pay) to the Tap to Pay reader.
1. [Collect](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=ios) the payment with the Tap to Pay reader.

### Entitlements and build file

To use Tap to Pay on iPhone to accept payments in your application, you must first [request and configure the Tap to Pay on iPhone development entitlement from your Apple Developer account](https://developer.apple.com/documentation/proximityreader/setting-up-the-entitlement-for-tap-to-pay-on-iphone?language=objc). After you complete internal testing, you must request a distribution entitlement.

After you add the development entitlement file to your app build target, add the following:

| |
| |
| Key | `com.apple.developer.proximity-reader.payment.acceptance` |
| Value type | `boolean` |
| Value | `true` or `1` |

Implementing Tap to Pay on iPhone is a complex process that requires submitting your app to Apple for approval. For detailed instructions, you can download our guide: [ Tap to Pay Guide (PDF)](https://docs.stripecdn.com/fd6123a72c0ea6d22019c125f9a35d855fe859b4e327faeb89a2934091830744.pdf)

#### React Native

Tap to Pay on iPhone introduces a [tapToPay](https://stripe.dev/stripe-terminal-react-native/api-reference/modules/Reader.IOS.html#DiscoveryMethod) discovery option and a [connectReader](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#connectreader-1) method. Integrate the latest version of the [Terminal React Native SDK](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=react-native) to include the latest bug fixes and features. You can view version-specific updates and bug fixes in the [SDK changelog](https://github.com/stripe/stripe-terminal-react-native/blob/master/CHANGELOG.md).

Device and minimum SDK version requirements can change due to updated compliance requirements or security vulnerabilities. To make sure your solution is up to date with Tap to Pay requirements, subscribe to [terminal-announce@lists.stripe.com](https://groups.google.com/a/lists.stripe.com/g/terminal-announce).

To enable Tap to Pay in your application:

1. [Request](https://developer.apple.com/documentation/proximityreader/setting-up-the-entitlement-for-tap-to-pay-on-iphone?language=objc) an entitlement.
1. [Set up](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=react-native) the Terminal iOS SDK.
1. [Connect](https://docs.stripe.com/terminal/payments/connect-reader.md?terminal-sdk-platform=react-native&reader-type=tap-to-pay) to the Tap to Pay reader.
1. [Collect](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=react-native) the payment with the Tap to Pay reader.

### Entitlements and build file

To use Tap to Pay on iPhone to accept payments in your application, you must first [request and configure the Tap to Pay on iPhone development entitlement from your Apple Developer account](https://developer.apple.com/documentation/proximityreader/setting-up-the-entitlement-for-tap-to-pay-on-iphone?language=objc). After you complete internal testing, you must request a distribution entitlement.

After you add the development entitlement file to your app build target, add the following:

| |
| |
| Key | `com.apple.developer.proximity-reader.payment.acceptance` |
| Value type | `boolean` |
| Value | `true` or `1` |

Implementing Tap to Pay on iPhone is a complex process that requires submitting your app to Apple for approval. For detailed instructions, you can download our guide: [ Tap to Pay Guide (PDF)](https://docs.stripecdn.com/fd6123a72c0ea6d22019c125f9a35d855fe859b4e327faeb89a2934091830744.pdf)

## Supported devices

Tap to Pay requires an iPhone XS or later running a one-year or later iOS version. [Apple’s Business Register documentation](https://register-docs.apple.com/tap-to-pay-on-iphone/docs/sdk-and-api-guide#ios-versions-and-deprecation-management) lists supported iOS versions. Advise your users to update to the latest iOS version for the best performance.

> Tap to Pay won’t work on beta releases of iOS.

## Cardholder verification limits and fallback

Some contactless card transactions above [certain amounts](https://support.stripe.com/questions/what-are-the-regional-contactless-limits-for-stripe-terminal-transactions) require additional cardholder verification methods (CVM) such as PIN entry. Tap to Pay on iPhone supports PIN entry for devices running iOS 16.4 or later.

NFC wallet payments (Apple Pay, Google Pay, and Samsung Pay) usually don’t require a PIN. However, in the UK, Canada, and Finland, regional requirements and card issuer policies can affect contactless payments.

In the UK, depending on the issuer, Strong Customer Authentication might require some cards to be inserted into a device. In such cases, if the card isn’t inserted, the payment is declined before the PIN screen appears, with the reason `offline_pin_required`.

In Canada and Finland, many issued cards are offline PIN only, meaning that entering the PIN requires physical contact, such as insertion into a device, which isn’t supported with Tap to Pay.

In these scenarios, we recommend asking the customer to try a different card or collecting payment in a different way. For example, using a Terminal card reader or sending a [Payment Link](https://docs.stripe.com/payment-links.md).

When collecting payment with your mobile device, hold the card to the reader until it reads the chip information. You might need to wait a few seconds after the initial vibration when the card makes contact. In the event of a decline, use another method to collect payment, such as a Terminal card reader. You can only have one active connection to a reader at a time.

To test PIN entry in markets where PIN is accepted, use [physical test cards](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards) with amounts ending in .03. In markets where PIN isn’t accepted, a transaction ending in .03 returns an `online_or_offline_pin_required` error code after the card is tapped, instead of allowing the user to test PIN entry.

## Merchant education

> Apple requires you to present a “How to Tap” instructional overlay when enabling Tap to Pay on iPhone. You must integrate this before submitting your app for review.

Use Apple’s [ProximityReaderDiscovery API](https://developer.apple.com/documentation/proximityreader/proximityreaderdiscovery) to display this overlay directly in your app. No additional dependencies are required because `ProximityReader` is a built-in iOS system framework already linked by the Stripe Terminal SDK.

The API follows a two-step pattern described in [Apple’s documentation](https://developer.apple.com/documentation/proximityreader/proximityreaderdiscovery):

1. Call `content(for:)` to fetch the educational content.
1. Call `presentContent(_:from:)` to display it.

```swift
func showHowToTap(from rootViewController: UIViewController) async throws {
    guard #available(iOS 18.0, *) else {
        // Provide your own fallback merchant education UI for earlier versions
        return
    }
    let discovery = ProximityReaderDiscovery()
    let content = try await discovery.content(for: .payment(.howToTap))

    // Walk the presentedViewController chain to find the topmost view controller
    var topVC = rootViewController
    while let presented = topVC.presentedViewController {
        topVC = presented
    }
    discovery.presentContent(content, from: topVC)
}
```

Keep two integration requirements in mind:

- Wrap the call in a `#available(iOS 18.0, *)` guard and provide a fallback UI for earlier versions.
- Pass the topmost presented view controller at the time of the call. Walk the `presentedViewController` chain from your root view controller to find it, otherwise the call fails.

Apple ensures that the content is up to date and localized for your business’s region. For additional merchant education strategies, including in-product promotion and text or email alerts, see Apple’s [developer marketing guidance](https://developer.apple.com/tap-to-pay/marketing-guidelines/).

## Best practices and promotion guidelines

Follow the guidelines in [Tap to Pay on iPhone](https://developer.apple.com/design/human-interface-guidelines/technologies/tap-to-pay-on-iphone/) to ensure an optimal user experience and successful review process with Apple.

Consider the following:

- Connect to the reader in the background on app startup to reduce wait times when collecting a payment.
- Use [automatic reconnection](https://docs.stripe.com/terminal/payments/connect-reader.md?terminal-sdk-platform=ios&reader-type=tap-to-pay#automatically-attempt-reconnection) to reconnect to the reader when the app comes to the foreground to reduce wait times.
- Launch and promote your Tap to Pay on iPhone marketing campaigns using our messaging templates and design assets following [Apple’s brand guidelines](https://developer.apple.com/tap-to-pay/marketing-guidelines/#editorial-guidelines). Become a [Stripe Partner](https://stripe.com/partners/become-a-partner) to access these assets in the [partner portal](https://portal.stripe.partners/s).

# Android

> This is a Android for when platform is android. View the full page at https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay?platform=android.

Use Tap to Pay on Android to accept in-person contactless payments with [compatible NFC-equipped Android devices](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay.md?platform=android#supported-devices).

Tap to Pay on Android includes support for Visa, Mastercard, American Express, and Discover contactless cards, NFC-based mobile wallets, and [QR-based payment methods](https://docs.stripe.com/terminal/payments/additional-payment-methods.md). PIN entry is supported. Additionally, [eftpos](https://docs.stripe.com/terminal/payments/regional.md?integration-country=AU#eftpos-payments) is supported in Australia, [Interac](https://docs.stripe.com/terminal/payments/regional.md?integration-country=CA#interac-payments) is supported in Canada, and [Cartes Bancaires](https://docs.stripe.com/terminal/payments/regional.md?integration-country=FR#cartes-bancaires-payments) is supported in France. Stripe includes Tap to Pay on Android in the Terminal Android SDK and the Terminal React Native SDK, and enables payments directly in your Android mobile app.

### Availability

- AT
- AU
- BE
- CH
- DE
- DK
- FI
- FR
- GB
- IE
- IT
- MY
- NL
- NZ
- PL
- SE
- SG
- US

### Availability in (Public preview)

- BG
- CA
- CY
- CZ
- EE
- ES
- GI
- HR
- HU
- LI
- LT
- LU
- LV
- MT
- NO
- PT
- RO
- SI
- SK

## Get started

#### Android

Integrate the latest version of the [Terminal Android SDK](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=android) to include the latest bug fixes and features. You can view version-specific updates and bug fixes in the [SDK changelog](https://github.com/stripe/stripe-terminal-android/blob/master/CHANGELOG.md).

Device and minimum SDK version requirements can change due to updated compliance requirements or security vulnerabilities. To make sure your solution is up to date with Tap to Pay requirements, subscribe to [terminal-announce@lists.stripe.com](https://groups.google.com/a/lists.stripe.com/g/terminal-announce).

To enable Tap to Pay in your Android application:

1. [Set up](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=android) the Terminal Android SDK.
1. Replace your existing `stripeterminal` dependencies with the following dependencies:

   #### Kotlin

   ```kotlin
       dependencies {
     implementation("com.stripe:stripeterminal-taptopay:5.4.1")
     implementation("com.stripe:stripeterminal-core:5.4.1")
     // ...
   }
   ```

1. [Connect](https://docs.stripe.com/terminal/payments/connect-reader.md?terminal-sdk-platform=android&reader-type=tap-to-pay) to the Tap to Pay reader.
1. [Collect](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=android) the payment with the Tap to Pay reader.

#### React Native

Integrate the latest version of the [Terminal React Native SDK](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=react-native) to include the latest bug fixes and features.

Device and minimum SDK version requirements can change due to updated compliance requirements or security vulnerabilities. To make sure your solution is up to date with Tap to Pay requirements, subscribe to [terminal-announce@lists.stripe.com](https://groups.google.com/a/lists.stripe.com/g/terminal-announce). To enable Tap to Pay in your application:

1. [Set up](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=react-native) the Terminal React Native SDK.
1. [Connect](https://docs.stripe.com/terminal/payments/connect-reader.md?terminal-sdk-platform=react-native&reader-type=tap-to-pay) to the Tap to Pay reader.
1. [Collect](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=react-native) the payment with the Tap to Pay reader.

## Supported devices

Tap to Pay on Android works with a variety of Android devices, including mobile phones, kiosks, tablets, and handheld devices. You can only discover and connect to devices that meet all of the following criteria:

- Has a functioning, integrated NFC sensor and ARM-based processor
- Isn’t rooted and device bootloader is locked and unchanged
- Runs Android 13 or later
- Has a security update installed from the past 12 months
- Uses Google Mobile Services and has the Google Play Store app installed
- Has a keystore with hardware support for ECDH ([`FEATURE_HARDWARE_KEYSTORE`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_HARDWARE_KEYSTORE) version must be 100 or later)
- Has a stable connection to the internet
- Runs the unmodified manufacturer provided OS
- Has Developer options disabled

Android device emulators aren’t supported by Tap to Pay. The same device requirements are enforced in the simulated and production reader to give developers the most realistic experience during testing.

### Device types

Supported device types include, but aren’t limited to:

| Type of device                                                                    | Manufacturer                                                                      | Models                         |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ------------------------------ |
| Countertop                                                                        | [Sunmi](https://partner.posportal.com/stripe/stripe/catalog/category/view/id/11/) | D3 MINI, V3 MIX                |
| Handheld                                                                          | Honeywell                                                                         | CT32, CT37                     |
| iMin                                                                              | Lark 1                                                                            |
| [Sunmi](https://partner.posportal.com/stripe/stripe/catalog/category/view/id/11/) | L3, V3                                                                            |
| Zebra                                                                             | TC53E                                                                             |
| Kiosk                                                                             | [Sunmi](https://partner.posportal.com/stripe/stripe/catalog/category/view/id/11/) | Flex 3 with Qualcomm 6225 chip |
| Register                                                                          | iMin                                                                              | Falcon 2                       |
| [Sunmi](https://partner.posportal.com/stripe/stripe/catalog/category/view/id/11/) | T3, T3 PRO                                                                        |
| Tablet                                                                            | HMD Global                                                                        | HMD T21                        |
| Samsung Galaxy                                                                    | Tab Active5                                                                       |
| [Sunmi](https://partner.posportal.com/stripe/stripe/catalog/category/view/id/11/) | CPad                                                                              |
| Oukitel                                                                           | RT3 Plus                                                                          |
| Ulefone                                                                           | Armor Pad 4 Ultra                                                                 |

Some manufacturers produce both GMS and non-GMS certified devices. If you’re using a non-GMS certified device, you’ll receive an error stating `ATTESTATION_FAILURE: Device is not Google Mobile Services (GMS) certified` when attempting to connect the device. If this occurs, contact the manufacturer to resolve the issue.

### Mobile phones

Supported mobile phones include, but aren’t limited to:

| Manufacturer   | Models                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Asus           | ROG Phone 7 series, ROG Phone 8 series, ROG Phone 9, Zenfone 10, Zenfone 11 Ultra, Zenfone 12 Ultra, Zenfone 9                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Google         | Pixel 10, Pixel 10 Pro, Pixel 10 Pro Fold, Pixel 10 Pro XL, Pixel 6, Pixel 6 Pro, Pixel 6a, Pixel 7, Pixel 7 Pro, Pixel 7a, Pixel 8, Pixel 8 Pro, Pixel 8a, Pixel 9, Pixel 9 Pro, Pixel 9 Pro Fold, Pixel 9 Pro XL, Pixel 9a, Pixel Fold                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Honor          | 100, 200, 200 Lite, 200 Pro, 200 Smart, 400, 400 Lite, 400 Pro, 400 Smart, 90, 90 Lite, 90 Smart, Magic V2, Magic V3, Magic V5, Magic Vs, Magic4 Pro, Magic5 Pro, Magic6, Magic6 Lite 5G, Magic6 Pro, Magic7 Lite, Magic7 Pro, Magic8 Lite, Magic8 pro, X5c Plus, X6, X6a, X6b, X6c, X7b, X7b 5G, X7c 5G, X7d, X8a, X8b, X9b 5G, X9c, X9c Smart, X9d                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Infinix        | GT 20 Pro, GT 30, GT 30 Pro, HOT 40 Pro, HOT 40i, HOT 50 5G, HOT 50 Pro, HOT 50 Pro+, HOT 60 5G, HOT 60 Pro, HOT 60 Pro+, HOT 60i, NOTE 30, NOTE 30 Pro, NOTE 40, NOTE 40 5G, NOTE 40 Pro, NOTE 40 Pro 5G, NOTE 40 Pro+ 5G, NOTE 50, NOTE 50 Pro, NOTE 50 Pro+ 5G, NOTE 50S 5G, SMART 10 PLUS, ZERO 30, ZERO 40                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Motorola       | ThinkPhone 25 by motorola, ThinkPhone by Motorola, edge (2022), edge 2023, edge 2024, edge 2025, edge 30 ultra, edge 40, edge 40 neo, edge 40 pro, edge 50, edge 50 fusion, edge 50 neo, edge 50 pro, edge 50 ultra, edge 60, edge 60 fusion, edge 60 neo, edge 60 pro, edge 60 stylus, edge 70, edge plus (2022), edge plus 2023, edge plus 5G UW (2022), moto g - 2025, moto g play - 2024, moto g power - 2025, moto g power 5G - 2024, moto g stylus 5G - 2023, moto g stylus 5G - 2024, moto g stylus 5G - 2025, moto g04, moto g04s, moto g05, moto g06, moto g06 power, moto g14, moto g15, moto g35 5G, moto g54 5G, moto g55 5G, moto g56 5G, moto g57 power, moto g64 5G, moto g64y 5G, moto g66j 5G, moto g67 power 5G, moto g72, moto g73 5G, moto g75 5G, moto g85 5G, moto g86 5G, moto g86 power 5G, moto g96 5G, razr 2022, razr 2023, razr 2024, razr 2025, razr 40, razr 40 ultra, razr 50, razr 50 ultra, razr 60, razr 60 ultra, razr plus 2023, razr plus 2024, razr plus 2025, razr ultra 2025 |
| OnePlus        | 10 Pro, 10 Pro 5G, 10R 5G, 10T 5G, 11 5G, 11R 5G, 12, 12R, 13, 13R, 13T, 13s, 15, Ace 5, Ace 6, Nord 3 5G, Nord 4, Nord 5, Nord CE4 Lite 5G, Nord CE5, Nord N30 SE 5G, Oneplus Ace 2 Pro, Open                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Oppo           | A3, A3 Pro 5G/A3 5G/A80 5G, A38, A40/A3/A40m, A40/A40m, A5 5G, A5 Pro, A5 Pro 5G, A5/A5m, A58, A5x, A60, A60 5G, A78, A78 5G, A79 5G, A80 5G, F25 Pro 5G, Find N2 Flip, Find N3, Find N3 Flip, Find N5, Find X5 Pro, Find X6, Find X6 Pro, Find X7 Ultra, Find X8, Find X8 Pro, Find X9, Find X9 Pro, OPPO A38, OPPO A6 Pro 5G, OPPO A60 5G/ A3 5G, OPPO F31 5G, OPPO Reno8 Pro 5G, OPPO Reno8 T, Reno 11, Reno 11 Pro, Reno10 5G, Reno10 Pro+ 5G, Reno11 F 5G, Reno11 F 5G/Reno11 A, Reno12 5G, Reno12 F, Reno12 F 5G, Reno12 F/FS 5G, Reno12 Pro, Reno12 Pro 5G, Reno13 5G, Reno13 F 5G, Reno13 F 5G / Reno13 A, Reno13 Pro 5G, Reno14 5G, Reno14 F 5G, Reno14 F 5G/Reno14 FS 5G, Reno14 Pro 5G, realme C51                                                                                                                                                                                                                                                                                                        |
| Redmi          | 12 5G, 13C 5G, 15, 15 5G, 15C 5G, K50, K60 Pro, K60 Ultra, K70, Note 12, Note 12 Turbo, Note 13, Note 13 5G, Note 13 Pro, Note 13 Pro 5G, Note 13 Pro+ 5G, Note 14, Note 14 5G, Note 14 Pro, Note 14 Pro 5G, Note 14 Pro+, Note 14 Pro+ 5G, Turbo 3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Samsung Galaxy | A04s, A05s, A13, A14, A14 5G, A15, A15 5G, A16, A16 5G, A17, A17 5G, A23 5G, A24, A25 5G, A26 5G, A33 5G, A34 5G, A35 5G, A36 5G, A53 5G, A53 5G UW, A54 5G, A55 5G, A56 5G, F34 5G, F54 5G, Flip7 FE, M13, M14 5G, M15 5G, M33 5G, M34 5G, M35 5G, M36 5G, M53 5G, M56 5G, S22, S22 Ultra, S22+, S23, S23 FE, S23 Ultra, S23+, S24, S24 FE, S24 Ultra, S24+, S25, S25 Edge, S25 FE, S25 Ultra, S25+, Tab Active5, Tab Active5 5G, Tab Active5 Pro, Tab Active5 Pro 5G, Wide8, XCover7, XCover7 Pro, Z Flip4, Z Flip5, Z Flip6, Z Flip7, Z Fold4, Z Fold5, Z Fold6, Z Fold7                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Xiaomi         | 12, 12 Pro, 12T, 12T Pro, 13, 13 Lite, 13 Pro, 13 Ultra, 13T, 13T Pro, 14, 14 Pro, 14 Ultra, 14T, 14T Pro, 15, 15 Ultra, 17 Pro Max, MIX Fold 3, MIX Fold 4                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

## User interface

Tap to Pay on Android includes payment collection screens. When your application is ready to collect a payment, the Stripe Terminal SDK takes over the display to handle the collection process. After you call the [process payment](https://docs.stripe.com/terminal/payments/collect-card-payment.md#process-payment) method, your application continues to run while Tap to Pay displays a full-screen prompt that instructs the cardholder to tap their card or NFC-based mobile wallet. If there’s an error reading the card, a prompt for retry displays. A successful tap returns a success indication and then control returns to your application.

### Device-specific NFC tap zone

When possible, the Tap to Pay on Android SDK automatically moves the tap zone indicator to help the end user understand where the tap zone is located on the device:
![](assets/stripe-terminal-ttpa-onscreen-demo-1.mp4)![](assets/stripe-terminal-ttpa-onscreen-demo-2.mp4)
If the SDK is unable to determine the tap zone position automatically (such as when the tap zone is offscreen), a default variant is used instead:
![](assets/stripe-terminal-ttpa-default-demo.mp4)

### UX configuration

- [TapToPayUxConfiguration (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-tap-to-pay-ux-configuration/index.html)
- [TapToPayUxConfiguration (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/types/TapToPayUxConfiguration.html)

You can override the default tap screen using the Terminal SDK, including colors of the tap UI, error UI, success UI, and the position of the tap zone indicator. Call `setTapToPayUxConfiguration` during your initialization or reader connection process. You can invoke it multiple times to adjust the appearance of the tap screen during the lifetime of your application. This configuration only affects the appearance of the tap screen, not the PIN collection screen.

#### Android

#### Kotlin

```kotlin
val config = TapToPayUxConfiguration.Builder()
    .tapZone(
        TapToPayUxConfiguration.TapZone.Front(0.5f, 0.3f)
    )
    .colors(
        TapToPayUxConfiguration.ColorScheme.Builder()
            .primary(TapToPayUxConfiguration.Color.Value(Color.parseColor("#FF008686")))
            .success(TapToPayUxConfiguration.Color.Default)
            .error(TapToPayUxConfiguration.Color.Resource(android.R.color.holo_red_dark))
            .build()
    )
    .darkMode(
        TapToPayUxConfiguration.DarkMode.DARK
    )
    .build()

Terminal.getInstance().setTapToPayUxConfiguration(config)
```

#### React Native

```js
import {
  useStripeTerminal,
  DarkMode,
} from "@stripe/stripe-terminal-react-native";

const { setTapToPayUxConfiguration } = useStripeTerminal();

const callSetTapToPayUxConfiguration = async () => {
  let tapZone = {
    indicator: "front",
    xBias: 0.5,
    yBias: 0.3,
  };
  let darkMode = DarkMode.DARK;
  let colors = {
    primary: "#FF008686",
    error: "#FFCC0000",
  };
  let config = {
    tapZone: tapZone,
    darkMode: darkMode,
    colors: colors,
  };

  const { error } = await setTapToPayUxConfiguration(config);

  if (error) {
    console.log("setTapToPayUxConfiguration error", error);
    return;
  }

  console.log("setTapToPayUxConfiguration success");
};
```

![](assets/stripe-terminal-ttpa-configuration-demo.mp4)

## Cardholder verification limits and fallback

Some contactless card transactions [above certain amounts](https://support.stripe.com/questions/what-are-the-regional-contactless-limits-for-stripe-terminal-transactions) require additional cardholder verification methods (CVM) such as PIN entry. Tap to Pay on Android supports PIN entry on Terminal Android SDK [4.3.0](https://github.com/stripe/stripe-terminal-android/releases/tag/v4.3.0) or later.

The PIN is collected in two scenarios:

- The transaction amount is above the [cardholder verification method (CVM) limit](https://support.stripe.com/questions/what-are-the-regional-contactless-limits-for-stripe-terminal-transactions). In this case, the PIN is collected before [collectPaymentMethod](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/collect-payment-method.html) returns. Focus returns to your application after the PIN is entered or PIN collection is canceled.
  ![Tap to Pay on Android local PIN flow](assets/stripe-terminal-ttpa-local-pin-flow.png)
- The issuer makes a [Strong Customer Authentication (SCA)](https://stripe.com/guides/strong-customer-authentication) request. In this case, the PIN is collected during [confirmPaymentIntent](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/confirm-payment-intent.html). Focus returns to your application after `confirmPaymentIntent`, unless the issuer makes a PIN request. In that case, PIN collection takes focus again until the PIN is entered or PIN collection is canceled.
  ![Tap to Pay on Android SCA PIN flow](assets/stripe-terminal-ttpa-sca-pin-flow.png)

### PIN error handling

You can only collect a PIN under the following conditions:

- [Developer options](https://developer.android.com/studio/debug/dev-options) are disabled.
- [Accessibility services](https://developer.android.com/guide/topics/ui/accessibility/service) aren’t registered or running.
- [Screen recording](https://support.google.com/android/answer/9075928) isn’t active.
- There are no [screen overlay windows](https://developer.android.com/privacy-and-security/risks/tapjacking)
- You have an active internet connection.

PIN collection also fails if any party attempts to take a screenshot.

If PIN collection fails due to one of these factors, you receive a `TAP_TO_PAY_INSECURE_ENVIRONMENT` error with additional information about the cause of the error. We recommend providing actionable next steps for the user to retry the payment to prompt for a PIN.

### Regional PIN considerations

NFC wallet payments (Apple Pay, Google Pay, and Samsung Pay) usually don’t require a PIN. However, in the UK, Canada, and Finland, regional requirements and card issuer policies can affect contactless payments.

In the UK, depending on the issuer, Strong Customer Authentication might require some cards to be inserted into a device. In such cases, if the card isn’t inserted, the payment is declined before the PIN screen appears, with the reason `offline_pin_required`.

In Canada and Finland, many issued cards are offline PIN only, meaning that entering the PIN requires physical contact, such as insertion into a device, which isn’t supported with Tap to Pay.

In these scenarios, we recommend asking the customer to try a different card or collecting payment in a different way. For example, using a Terminal card reader or sending a [Payment Link](https://docs.stripe.com/payment-links.md).

When collecting payment with your mobile device, hold the card to the reader until it reads the chip information. You might need to wait a few seconds after the initial vibration when the card makes contact. In the event of a decline, use another method to collect payment, such as a Terminal card reader. You can only have one active connection to a reader at a time.

### PIN UX

For security reasons, the PIN pad doesn’t always appear in the center of the screen. It appears in a randomly determined position.
![Tap to Pay on Android PIN collection screen](assets/stripe-terminal-ttpa-pin-screen.png)

An off-center PIN pad is expected behavior

## Best practices and promotion guidelines

Ensure an optimal user experience by considering the following:

- Connect to the reader in the background on app startup to reduce wait times when collecting a payment.
- Use [automatic reconnection](https://docs.stripe.com/terminal/payments/connect-reader.md?terminal-sdk-platform=android&reader-type=tap-to-pay#automatically-attempt-reconnection) to reconnect to the reader when the app comes to the foreground to reduce wait times.
- Provide merchant education to guide your users on how to accept contactless payments on a compatible Android device, including in-product promotion and text or email alerts.
- Launch and promote your Tap to Pay on Android marketing campaigns using our messaging templates and design assets. Become a [Stripe Partner](https://stripe.com/partners/become-a-partner) to access these assets in the [partner portal](https://portal.stripe.partners/s).

## Next steps

- [Set up your integration](https://docs.stripe.com/terminal/payments/setup-integration.md)
- [Connect to a reader](https://docs.stripe.com/terminal/payments/connect-reader.md)
- [Collect a card payment](https://docs.stripe.com/terminal/payments/collect-card-payment.md)
- [Test your integration](https://docs.stripe.com/terminal/references/testing.md)
- [Regional payment methods](https://docs.stripe.com/terminal/payments/regional.md)
