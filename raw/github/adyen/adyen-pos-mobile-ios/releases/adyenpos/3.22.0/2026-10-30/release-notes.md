> [!IMPORTANT]
> **SDK NYC1 PIN support expires on 13 April 2027**

## New

* The SDK now supports Catalan, Croatian, Czech, Estonian, Icelandic, Japanese, Latvian, Lithuanian, Romanian and Russian. See [Change the language](https://docs.adyen.com/point-of-sale/mobile-ios/manage#change-the-language).

## Improved

* The SDK now uses the device's operating system language as a fallback. If the app language is not supported, the SDK shows the device language before falling back to English.

* Close buttons now have a consistent appearance across the transaction flow, card reader pairing, and device management screens on iOS 26.

## Fixed:

* We fixed an issue where labels in the device management UI and on the present card screen did not use the primary language.
We fixed an issue where the payment UI briefly showed the app language before switching to the primary language.

- Built with Xcode 26.3