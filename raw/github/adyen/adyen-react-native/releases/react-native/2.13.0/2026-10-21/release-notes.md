## What's Changed

### Features
* **Android:** Added support for providing Google Pay merchant info.
* The SDK version is now configured directly from JavaScript.

### Changed
* The SDK now targets Android API 36.

### Fixes
* **iOS:** Ensured the embedded `CardView` correctly ignores the safe area.
* Fixed an issue where `findSubview` didn't search the entire view tree.
* Exported the `ApplePayAuthorizationResult` type to resolve a missing export issue.

### Example app
* Moved `onDisableStoredPaymentMethod` to `AdvancedCheckout`.

### SDK Updates

| Name | New version |
| --- | --- |
| Android Drop-in/Components | 5.20.0 |
| iOS Drop-in/Components | 5.26.0 |

**Updated Android SDK to 5.20.0**
* UPI: Added support for the Smart Intent flow, with automatic detection of installed UPI apps on the device.
* UI: Redesigned the UI for co-badged cards, allowing shoppers to select their preferred brand directly inside the card field for certain brands.
* Accessibility: Drop-in accessibility services now correctly announce headings.
* Fix: The primary button can now be selected via keyboard input when using an external hardware keyboard.
* Fix: Prevented a crash in Drop-in when a shopper selects a stored payment method and a regular payment method simultaneously.

**Updated iOS SDK to 5.26.0**
* iPhone Duo Support: Improved the layout of both the Drop-in and Components specifically for iPhone Duo.
* Accessibility: Improved accessibility by updating the default inactive text-input title and underline colors.
* **Deprecation Notice:** This is the last release available through CocoaPods. Moving forward, the iOS SDK will be distributed exclusively through Swift Package Manager (SPM) and Carthage.

## New Contributors
* @mohamedmaged made their first contribution in https://github.com/Adyen/adyen-react-native/pull/1231
* @Nawal00 made their first contribution in https://github.com/Adyen/adyen-react-native/pull/1227

**Full Changelog**: https://github.com/Adyen/adyen-react-native/compare/2.12.0...2.13.0