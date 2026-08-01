## What's Changed

This release makes instant payments on Sessions more reliable. 

## Features

* PayByBank is now available as a standalone payment component.
* Apple Pay configuration now supports `merchantCapabilities`.

## Fixes

* On Android, the Twint payment method no longer provides a "store payment field" UI, matching the iOS behavior.
* On Android, Google Pay and instant payments now work reliably during device rotation.
* On Android, the "A payment process is still active" screen cannot be dismissed now via the back button or swipe gestures.
* On iOS, the app no longer crashes when dismissing the embedded CardView.

## Dependencies

* Updated Android SDK to 5.19.0
   * UPI: Added support for the Smart Intent flow, with automatic detection of installed UPI apps on the device.
* Updated iOS SDK to 5.25.1
   * UPI: Added support for the Smart Intent flow, with automatic detection of installed UPI apps on the device.
   * Bizum: Added support for Bizum as an instant payment method.
* Upgraded React Native to 0.85

## Example App

* The "Sessions Component" tab now showcases instant payments.
* The example app now uses the UIScene lifecycle.
* Added a searchable country/currency dropdown.

**Full Changelog**: https://github.com/Adyen/adyen-react-native/compare/2.11.1...2.12.0