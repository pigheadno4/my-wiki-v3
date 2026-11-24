## 26.16.0 2026-11-02
### PaymentSheet
* [Added] The Link auth flow now natively supports email OTP and multi-factor authentication (MFA) enabled accounts.
* [Added] Added `returnURL` to `LinkConfiguration`, allowing `LinkController` users to let customers authenticate in their banking app and then return to the merchant's app. Without a `returnURL`, bank authentication happens in a secure webview presented in the merchant's app (private preview).
* [Fixed] Fixed a horizontal layout bug that caused the sheet to freeze when the bottom form insets were less than the bottom safe area.
* [Fixed] Fixed an issue introduced in 26.14.0 where customers couldn't interact with 3D Secure authentication challenges shown in the native Link sheet.

### Identity
* [Added] Added support for 3D face capture in StripeIdentity.
* [Fixed] Fixed release archives failing to link MediaPipe for x86_64 simulators. Prebuilt `StripeIdentity` and `StripeCryptoOnramp` frameworks support arm64 simulators only; other SDK frameworks retain arm64 and x86_64 simulator support. Swift Package Manager integrations with the `Identity` trait enabled also require arm64 simulators.
* [Added] Added the `Identity` package trait for Swift Package Manager. It links MediaPipe from [stripe/identity-ios-mediapipe](https://github.com/stripe/identity-ios-mediapipe), which StripeIdentity uses for 3D face capture. To enable it, check `Identity` in the **Traits** menu for `stripe-ios-spm` under your project's **Package Dependencies** (Xcode 26.4 or later), or add `traits: [.defaults, "Identity"]` to the `stripe-ios-spm` dependency in your `Package.swift`. Without the trait, StripeIdentity works as before. CocoaPods installs include MediaPipe through the `StripeMediaPipe` pod.

