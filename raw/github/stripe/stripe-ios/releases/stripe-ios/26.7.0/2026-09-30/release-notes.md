## 26.7.0 2026-08-17
### PaymentSheet
* [Added] StripePaymentSheet now depends on `StripeFinancialConnectionsLite` to support lightweight bank payment flows. If you use StripePaymentSheet with Carthage or by manually embedding the .xcframeworks, [you must also embed StripeFinancialConnectionsLite.xcframework](https://github.com/stripe/stripe-ios/blob/master/MIGRATING.md#migrating-from-versions--2670) in your app. No action is required for CocoaPods or Swift Package Manager users.
* [Changed] Address autocomplete results sourced from internal service.
* [Added] Added `PaymentSheet.LinkConfiguration.Display.walletButtonHidden`, which keeps Link enabled but hides its button from the payment element UI.

### AddressElement
* [Changed] Address autocomplete results sourced from internal service.

