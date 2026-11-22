---
title: "Collect Physical Addresses and Phone Numbers — Mobile"
type: source
date_ingested: 2026-04-22
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/mobile/collect-addresses"
raw_files:
  - "stripe-inapp-collect-addresses-2025.md"
tags: [stripe, mobile, ios, android, react-native, address-element, autocomplete, billing-address, shipping-address, google-places]
---

## Summary

The 2026-04-22 integration guide covers the mobile Address Element across iOS UIKit, iOS SwiftUI, Android and React Native. It shows SDK setup, configuration, address retrieval, optional Payment Element prefill and billing details collection. The 2026-11-07 capture of the same URL introduces address and phone collection and indexes the same four variants. The examples and requirements below come from the April guide.

> See also [[source-stripe-inapp-address-element]] for the overview page, and [[source-stripe-collect-addresses]] for the web variant.

## Platform API Comparison

The April guide calls for a Stripe account and the platform SDK with a client publishable key. Use test keys during development and live keys in production. The April iOS compatibility wording is iOS 13 or above. The Android dependency examples use Stripe Android 23.5.0 and Google Places 2.6.0. The sample Financial Connections dependency serves US bank account payments.

| | iOS UIKit | iOS SwiftUI | Android | React Native |
| --- | --- | --- | --- | --- |
| Component | `AddressViewController` | `AddressElement` (SwiftUI sheet) | `AddressLauncher` | `<AddressSheet>` |
| Config type | `AddressViewController.Configuration` | `AddressElement.Configuration` | `AddressLauncher.Configuration` | Props on component |
| Callback | `AddressViewControllerDelegate` | Bound `$address` state | `AddressLauncherResultCallback` | `onSubmit`/`onError` |
| Result | `AddressViewController.AddressDetails?` | `AddressElement.AddressDetails?` | `AddressLauncherResult.Succeeded`/`.Canceled` | `addressDetails` in `onSubmit` |

## iOS UIKit

The April example makes the phone field required. Stripe says to collect phone numbers only when needed for the transaction. The delegate receives optional address details.

```swift
// 1. Configure
let addressConfiguration = AddressViewController.Configuration(
    additionalFields: .init(phone: .required),
    allowedCountries: ["US", "CA", "GB"],
    title: "Shipping Address"
)

// 2. Retrieve via delegate
extension MyViewController: AddressViewControllerDelegate {
    func addressViewControllerDidFinish(_ vc: AddressViewController, with address: AddressViewController.AddressDetails?) {
        vc.dismiss(animated: true)
        self.addressDetails = address
    }
}

// 3. Present
let addressVC = AddressViewController(configuration: addressConfiguration, delegate: self)
present(UINavigationController(rootViewController: addressVC), animated: true)

// 4. Prefill Payment Element (optional)
configuration.shippingDetails = { [weak self] in self?.addressDetails }
```

## iOS SwiftUI

The bound address value updates when the customer completes or cancels address collection. The April SwiftUI section mentions billing prefill from a shipping address. The concrete shipping-prefill examples are in the UIKit, Android and React Native sections.

```swift
var configuration = AddressElement.Configuration()
configuration.allowedCountries = ["US", "CA", "GB", "AU"]

// Present as sheet; address state variable updates automatically
.sheet(isPresented: $showingAddressElement) {
    AddressElement(address: $collectedAddress, configuration: configuration)
}
```

## Android (Kotlin)

```kotlin
// Must instantiate in onCreate — crashes if later
private lateinit var addressLauncher: AddressLauncher

override fun onCreate(savedInstanceState: Bundle?) {
    addressLauncher = AddressLauncher(this, ::onAddressLauncherResult)
}

private fun onAddressLauncherResult(result: AddressLauncherResult) {
    when (result) {
        is AddressLauncherResult.Succeeded -> shippingDetails = result.address
        is AddressLauncherResult.Canceled -> { /* handle */ }
    }
}

// Present
addressLauncher.present(publishableKey = publishableKey, configuration = addressConfiguration)

// Prefill Payment Element (optional)
PaymentSheet.Configuration.Builder("Merchant").shippingDetails(shippingDetails).build()
```

- Autocomplete requires Google Places SDK dependency + API key
- `AddressLauncher.Configuration.googlePlacesApiKey` — optional field

## React Native

The April example makes the phone field required. Stripe says to collect phone numbers only when needed for the transaction.

```jsx
<AddressSheet
  visible={addressSheetVisible}
  allowedCountries={['US', 'CA', 'GB']}
  additionalFields={{ phoneNumber: 'required' }}
  googlePlacesApiKey={'(optional) YOUR KEY HERE'}
  onSubmit={async (addressDetails) => {
    setAddressSheetVisible(false);
    // use addressDetails
  }}
  onError={(error) => {
    setAddressSheetVisible(false); // must set back to false
  }}
/>

// Prefill Payment Element (optional)
await initPaymentSheet({ defaultShippingDetails: addressDetails });
```

- iOS autocomplete: enabled by default
- Android autocomplete: requires Google Places SDK in `build.gradle` + API key

## Billing Details Collection (All Platforms)

`billingDetailsCollectionConfiguration` controls what's collected in PaymentSheet:
- **Field-specific modes.** Name, email and phone have general collection controls. The examples set name to always and email to never. The address setting uses its own modes. The full-address value shown is `.full` in UIKit and SwiftUI, `BillingDetailsCollectionConfiguration.AddressCollectionMode.Full` in Android and `PaymentSheet.AddressCollectionMode.FULL` in React Native.
- **PaymentMethod billing defaults.** `defaultBillingDetails` prefills the billing fields. `attachDefaultsToPaymentMethod: true` opts into attaching those defaults to the PaymentMethod, including values omitted from the UI. The React Native guide explicitly requires providing any method-required values skipped in the UI as `defaultBillingDetails` and enabling attachment.

## Key Notes

- **Android onCreate rule**: `AddressLauncher` MUST be instantiated in `onCreate` — after will crash
- **Autocomplete**. The April guide says iOS enables it by default, including React Native on iOS. Android, including React Native on Android, needs the Google Places SDK and API key to enable autocomplete. Address collection is available without enabling autocomplete.
- **Dismiss on RN**: must manually set `visible={false}` in both `onSubmit` and `onError`
- **Optional shipping-to-billing prefill**. The April examples populate PaymentSheet `shippingDetails` in UIKit and Android or `defaultShippingDetails` in React Native with the collected address. The payment UI then prefills billing and shows the same-as-shipping checkbox. In those paths, populated shipping details are recorded in `PaymentIntent.shipping` upon confirmation. Address UI completion, autocomplete and populated shipping or billing details establish neither payment success nor address ownership.

## Related Pages

- [[stripe]] — Stripe company profile
- [[stripe-inapp-payments]] — in-app payments concept page
- [[source-stripe-inapp-address-element]] — mobile Address Element overview
- [[stripe-address-element]] — web Address Element concept page

## Raw Sources

- [[raw/stripe-inapp-collect-addresses-2025|Mobile Address Element guide captured 2026-04-22]] — verbatim guide (~768 lines, iOS UIKit + iOS SwiftUI + Android + React Native)

## Related raw API references

- [[raw/stripe-payments-mobile-collect-addresses-2026-11-07|Mobile Address Element collection variant index]] — 2026-11-07 navigation capture for iOS UIKit, iOS SwiftUI, Android and React Native.
