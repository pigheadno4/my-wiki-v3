---
title: "GitHub: paypal/paypal-messages-ios"
type: source
date_ingested: 2026-04-14
original_format: github-repo
raw_files:
  - "github-paypal-messages-ios.md"
tags: [paypal, pay-later, ios, swift, sdk, messaging, bnpl, mobile]
---

## Overview

[paypal/paypal-messages-ios](https://github.com/paypal/paypal-messages-ios) is the PayPal iOS SDK Messages Module — a standalone Swift package that renders Pay Later and PayPal Credit promotional messages within iOS apps. Version 1.2.0, MIT license.

Recommended integration path: via the [PayPal iOS SDK](https://github.com/paypal/paypal-ios) umbrella SDK. Can also be used standalone.

**Requirements:** iOS 14.0+, Xcode 14.3+, Swift 5.8+

**Package managers:** CocoaPods, Swift Package Manager (binary XCFramework), Carthage

**UI frameworks:** UIKit and SwiftUI both supported

## Key Takeaways

### Core API: `PayPalMessageConfig`

Config is composed of two objects:

**`PayPalMessageData`** — business/data parameters:

| Property | Type | Notes |
| --- | --- | --- |
| `clientID` | `String` | Required — from PayPal Developer Dashboard |
| `environment` | `Environment` | `.sandbox` or `.live` |
| `amount` | `Double?` | Price in cents for the current context |
| `pageType` | `PayPalMessagePageType?` | Screen location (home, cart, checkout, etc.) |
| `offerType` | `PayPalMessageOfferType?` | Preferred offer to display |
| `buyerCountry` | `String?` | Cross-border — requires PayPal approval |
| `language` | `String?` | e.g. `"fr-CA"`, `"en-US"` |
| `locale` | `String?` | e.g. `"fr_CA"`, `"en_US"` |
| `merchantID` | `String?` | Partner integrations only |
| `partnerAttributionID` | `String?` | Partner BN Code — partner integrations only |

Two inits: **standard** (clientID + environment) and **partner** (adds merchantID + partnerAttributionID).

**`PayPalMessageStyle`** — visual parameters:

| Property | Type | Values |
| --- | --- | --- |
| `logoType` | `PayPalMessageLogoType` | `inline`, `primary`, `alternative`, `none` |
| `color` | `PayPalMessageColor` | `black`, `white`, `monochrome`, `grayscale` |
| `textAlign` | `PayPalMessageTextAlign` | `left`, `center`, `right` |

### Offer Types

| Enum case | Raw value | Meaning |
| --- | --- | --- |
| `.payLaterShortTerm` | `PAY_LATER_SHORT_TERM` | Pay in 4 |
| `.payLaterLongTerm` | `PAY_LATER_LONG_TERM` | Pay Monthly |
| `.payLaterPayIn1` | `PAY_LATER_PAY_IN_1` | Deferred single payment |
| `.payPalCreditNoInterest` | `PAYPAL_CREDIT_NO_INTEREST` | PayPal Credit |

### Page Types

`home`, `product-listing`, `product-details`, `cart`, `mini-cart`, `checkout`, `search-results`

### Delegates

**`PayPalMessageViewStateDelegate`** — rendering lifecycle:
- `onLoading(_:)` — fetch started
- `onSuccess(_:)` — message rendered
- `onError(_:error:)` — fetch/render failed; `error.paypalDebugId` available

**`PayPalMessageViewEventDelegate`** — user interactions:
- `onClick(_:)` — message tapped (modal opens)
- `onApply(_:)` — user began PayPal Credit application

**`PayPalMessageModalEventDelegate`** — modal interactions:
- `onClick(_:data:)` — link tapped within modal; `data.linkName`, `data.linkSrc`
- `onCalculate(_:data:)` — payment calculator submitted; `data.value`
- `onShow(_:)` / `onClose(_:)` — modal visibility

### Integration Pattern (UIKit)

```swift
let config = PayPalMessageConfig(
    data: PayPalMessageData(
        clientID: "YOUR_CLIENT_ID",
        environment: .sandbox,
        amount: 100.00,
        pageType: .cart,
        offerType: .payLaterShortTerm
    ),
    style: PayPalMessageStyle(
        logoType: .inline,
        color: .black,
        textAlign: .left
    )
)

let messageView = PayPalMessageView(
    config: config,
    stateDelegate: self,
    eventDelegate: self
)
```

### Integration Pattern (SwiftUI)

```swift
PayPalMessageView.Representable(
    config: messageConfig,
    stateDelegate: stateDelegate,
    eventDelegate: eventDelegate
)
```

### `setConfig` / `getConfig`

`PayPalMessageView` exposes `setConfig(_:)` and `getConfig()` instead of direct property access. Calling `setConfig` with a new config triggers a full refetch. Changing individual proxy properties (e.g. `amount`, `offerType`) updates without refetch. When changing multiple properties, prefer `setConfig` to avoid locking during in-progress updates.

### Analytics

```swift
PayPalMessageConfig.setGlobalAnalytics(
    integrationName: "YourApp",
    integrationVersion: "1.0.0"
)
```

Call once at startup for partner/wrapper integrations.

### Distribution

- **SPM**: binary XCFramework at `v1.2.0` — checksum `819604d7...`
- **CocoaPods**: `pod 'PayPalMessages', '~> 1.2.0'`
- **Carthage**: `Carthage/PayPalMessages.json`

## Raw Sources

- [[github-paypal-messages-ios]] — stub file with file list and "What each file covers" table; detail in `raw/github-paypal-messages-ios/`

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-pay-later]] — Pay Later products surfaced via this messaging SDK
- [[paypal-ios-sdk]] — umbrella iOS SDK (recommended integration path)
