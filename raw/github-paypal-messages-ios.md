<!-- Repo: https://github.com/paypal/paypal-messages-ios -->
<!-- Commit SHA: 432d6b832714b2615106c3f2a748ac61654d8bbd -->
<!-- Date reviewed: 2026-04-14 -->
<!-- Detail directory: raw/github-paypal-messages-ios/ -->
<!-- Files saved (read directly from these paths):
  raw/github-paypal-messages-ios/README.md
  raw/github-paypal-messages-ios/Package.swift
  raw/github-paypal-messages-ios/PayPalMessages.podspec
  raw/github-paypal-messages-ios/Sources/PayPalMessages/Config/PayPalMessageConfig.swift
  raw/github-paypal-messages-ios/Sources/PayPalMessages/Delegates/PayPalMessageDelegates.swift
  raw/github-paypal-messages-ios/Sources/PayPalMessages/Delegates/PayPalMessageModalDelegates.swift
  raw/github-paypal-messages-ios/Sources/PayPalMessages/Enums/PayPalMessageOfferType.swift
  raw/github-paypal-messages-ios/Sources/PayPalMessages/Enums/PayPalMessagePageType.swift
  raw/github-paypal-messages-ios/Sources/PayPalMessages/Enums/PayPalMessageColor.swift
  raw/github-paypal-messages-ios/Sources/PayPalMessages/Enums/PayPalMessageLogoType.swift
  raw/github-paypal-messages-ios/Sources/PayPalMessages/Enums/PayPalMessageTextAlign.swift
  raw/github-paypal-messages-ios/Sources/PayPalMessages/PayPalMessageView.swift
  raw/github-paypal-messages-ios/Demo/Demo/SwiftUIContentView.swift
-->
<!-- Deep-dive fallback: if a query needs files NOT listed above, re-clone from https://github.com/paypal/paypal-messages-ios at commit SHA 432d6b832714b2615106c3f2a748ac61654d8bbd, then save any newly discovered files into raw/github-paypal-messages-ios/ preserving their repo-relative paths -->

## What each file covers

| File | What to find there |
| ---- | ------------------ |
| `raw/github-paypal-messages-ios/README.md` | Overview, requirements (iOS 14+, Xcode 14.3+, Swift 5.8+), package manager support (SPM/CocoaPods/Carthage), UIKit/SwiftUI support, demo setup |
| `raw/github-paypal-messages-ios/Package.swift` | SPM distribution definition, version 1.2.0, binary XCFramework target with checksum |
| `raw/github-paypal-messages-ios/PayPalMessages.podspec` | CocoaPods spec — version, platform, source_files pattern, resource_bundle |
| `raw/github-paypal-messages-ios/Sources/PayPalMessages/Config/PayPalMessageConfig.swift` | `PayPalMessageData` (clientID, merchantID, partnerAttributionID, environment, amount, pageType, offerType, buyerCountry, language, locale), `PayPalMessageStyle` (logoType, color, textAlign), `PayPalMessageConfig`, standard vs partner integration inits, `setGlobalAnalytics` |
| `raw/github-paypal-messages-ios/Sources/PayPalMessages/Delegates/PayPalMessageDelegates.swift` | `PayPalMessageViewStateDelegate` (onLoading/onSuccess/onError), `PayPalMessageViewEventDelegate` (onClick/onApply) |
| `raw/github-paypal-messages-ios/Sources/PayPalMessages/Delegates/PayPalMessageModalDelegates.swift` | `PayPalMessageModalStateDelegate`, `PayPalMessageModalEventDelegate` (onClick/onCalculate/onShow/onClose), `PayPalMessageModalClickData`, `PayPalMessageModalCalculateData` |
| `raw/github-paypal-messages-ios/Sources/PayPalMessages/Enums/PayPalMessageOfferType.swift` | Offer type enum: PAY_LATER_SHORT_TERM, PAY_LATER_LONG_TERM, PAY_LATER_PAY_IN_1, PAYPAL_CREDIT_NO_INTEREST; response-only GENERIC case |
| `raw/github-paypal-messages-ios/Sources/PayPalMessages/Enums/PayPalMessagePageType.swift` | Page location enum: home, product-listing, product-details, cart, mini-cart, checkout, search-results |
| `raw/github-paypal-messages-ios/Sources/PayPalMessages/Enums/PayPalMessageColor.swift` | Color enum: black, white, monochrome, grayscale |
| `raw/github-paypal-messages-ios/Sources/PayPalMessages/Enums/PayPalMessageLogoType.swift` | Logo type enum: inline, primary, alternative, none (bold text) |
| `raw/github-paypal-messages-ios/Sources/PayPalMessages/Enums/PayPalMessageTextAlign.swift` | Text alignment enum: left, center, right |
| `raw/github-paypal-messages-ios/Sources/PayPalMessages/PayPalMessageView.swift` | `PayPalMessageView` UIControl — all proxy properties, `setConfig`/`getConfig`, SwiftUI `Representable`, accessibility, highlight animation |
| `raw/github-paypal-messages-ios/Demo/Demo/SwiftUIContentView.swift` | Full SwiftUI integration example — all config params wired to UI controls, state/event delegate implementations, debounce pattern |
