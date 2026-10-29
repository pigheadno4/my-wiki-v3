**Breaking changes**

* [Removed] iOS: The `disableSPM` Expo option and `$StripeDisableSPM = true` Podfile flag are no longer supported because the Stripe iOS SDK no longer supports CocoaPods resolution. Remove these options and use dynamic frameworks with Swift Package Manager. See the [migration guide](MIGRATING.md#ios-swift-package-manager-dependency-resolution-and-dynamic-linking).
* [Removed] Support for React Native versions below 0.75. React Native 0.75 or later is now required.

**Fixes**

* [Fixed] Android: Connect external links now use the configured browser presentation regardless of navigation type.
* [Fixed] Connect CSV exports now open the native share sheet again for exports served from Stripe's export storage.