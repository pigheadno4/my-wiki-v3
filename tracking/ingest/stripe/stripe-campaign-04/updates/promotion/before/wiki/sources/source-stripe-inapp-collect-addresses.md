---
title: "Collect Physical Addresses and Phone Numbers — Mobile"
type: source
date_ingested: 2026-04-22
original_format: webpage
raw_files:
  - "stripe-inapp-collect-addresses-2025.md"
tags: [stripe, mobile, ios, android, react-native, address-element, autocomplete, billing-address, shipping-address, google-places]
---

## Summary

Full integration guide for the mobile Address Element across iOS UIKit, iOS SwiftUI, Android, and React Native. Covers SDK setup, configuration, address retrieval, Payment Element prefill, and billing details collection customization.

> See also [[source-stripe-inapp-address-element]] for the overview page, and [[source-stripe-collect-addresses]] for the web variant.

## Platform API Comparison

| | iOS UIKit | iOS SwiftUI | Android | React Native |
| --- | --- | --- | --- | --- |
| Component | `AddressViewController` | `AddressElement` (SwiftUI sheet) | `AddressLauncher` | `<AddressSheet>` |
| Config type | `AddressViewController.Configuration` | `AddressElement.Configuration` | `AddressLauncher.Configuration` | Props on component |
| Callback | `AddressViewControllerDelegate` | Bound `$address` state | `AddressLauncherResultCallback` | `onSubmit`/`onError` |
| Result | `AddressViewController.AddressDetails?` | `AddressElement.AddressDetails?` | `AddressLauncherResult.Succeeded`/`.Canceled` | `addressDetails` in `onSubmit` |

## iOS UIKit

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
- `name`, `email`, `phone`, `address` — each can be `always`/`never`/`if_required`
- `attachDefaultsToPaymentMethod` — if `true`, `defaultBillingDetails` attach to PM even when not shown in UI

## Key Notes

- **Android onCreate rule**: `AddressLauncher` MUST be instantiated in `onCreate` — after will crash
- **Autocomplete on Android/RN**: requires Google Places SDK + API key (not automatic)
- **Dismiss on RN**: must manually set `visible={false}` in both `onSubmit` and `onError`
- **Shipping → billing prefill**: setting `shippingDetails` on PaymentSheet auto-shows "Billing same as shipping" checkbox and populates PaymentIntent `shipping` field

## Related Pages

- [[stripe-inapp-payments]] — in-app payments concept page
- [[source-stripe-inapp-address-element]] — mobile Address Element overview
- [[stripe-address-element]] — web Address Element concept page

## Raw Sources

- [[stripe-inapp-collect-addresses-2025]] — verbatim guide (~768 lines, iOS UIKit + iOS SwiftUI + Android + React Native)
