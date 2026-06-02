---
title: "GitHub: paypal/paypal-messages-android"
type: source
date_ingested: 2026-04-14
original_format: github-repo
raw_files:
  - "github-paypal-messages-android.md"
tags: [paypal, pay-later, android, kotlin, sdk, messaging, bnpl, mobile, jetpack-compose]
---

## Overview

[paypal/paypal-messages-android](https://github.com/paypal/paypal-messages-android) is the PayPal Android Messages Library — a Kotlin component library for rendering Pay Later and PayPal Credit promotional messages in Android apps. Version 1.3.0, MIT license.

> [!info] Availability status
> The README notes the library is still in active development and recommends using it in **sandbox only** until an official general availability release. No GA date is specified in the README.

**Requirements:** Android SDK 23+, targets SDK 34

**Distribution:** Maven Central (published via GitHub Actions)

**UI frameworks:** XML Views (`PayPalMessageView` extends `FrameLayout`) and Jetpack Compose (`PayPalComposableMessage`)

## Key Takeaways

### Core API: `PayPalMessageConfig`

Config is a Kotlin data class composed of four objects:

**`PayPalMessageData`** — business/data parameters:

| Property | Type | Notes |
| --- | --- | --- |
| `clientID` | `String` | Required |
| `environment` | `PayPalEnvironment` | Default: `SANDBOX` |
| `amount` | `Double?` | Price for the current context |
| `pageType` | `PayPalMessagePageType?` | Screen location |
| `offerType` | `PayPalMessageOfferType?` | Preferred offer |
| `buyerCountry` | `String?` | Cross-border — requires PayPal approval |
| `language` | `PayPalLanguage?` | Typed enum (not raw string like iOS) |
| `locale` | `PayPalLocale?` | Typed enum (not raw string like iOS) |
| `merchantID` | `String?` | Partner integrations only |
| `partnerAttributionID` | `String?` | Partner BN Code |

**`PayPalMessageStyle`** — visual parameters:

| Property | Type | Values |
| --- | --- | --- |
| `color` | `PayPalMessageColor` | `BLACK`, `WHITE`, `MONOCHROME`, `GRAYSCALE` |
| `logoType` | `PayPalMessageLogoType` | `PRIMARY`, `ALTERNATIVE`, `INLINE`, `NONE` |
| `textAlignment` | `PayPalMessageAlignment` | `LEFT`, `CENTER`, `RIGHT` |

> [!info] Field name difference vs iOS
> Android uses `textAlignment` (in `PayPalMessageStyle`); iOS uses `textAlign` (in `PayPalMessageStyle`). Android's field is also named `PayPalMessageAlignment` vs iOS's `PayPalMessageTextAlign`.

**`PayPalMessageViewStateCallbacks`** — rendering lifecycle:

```kotlin
PayPalMessageViewStateCallbacks(
    onLoading = { /* fetch started */ },
    onSuccess = { /* message rendered */ },
    onError = { error -> /* PayPalErrors.Base */ }
)
```

**`PayPalMessageEventsCallbacks`** — user interactions:

```kotlin
PayPalMessageEventsCallbacks(
    onClick = { /* message tapped */ },
    onApply = { /* user began application */ }
)
```

### Offer Types

| Enum value | Index | Meaning |
| --- | --- | --- |
| `PAY_LATER_SHORT_TERM` | 0 | Pay in 4 |
| `PAY_LATER_LONG_TERM` | 1 | Pay Monthly |
| `PAY_LATER_PAY_IN_1` | 2 | Deferred single payment |
| `PAYPAL_CREDIT_NO_INTEREST` | 3 | PayPal Credit |

Enums are int-indexed (via `invoke(attributeIndex: Int)`) for XML attribute binding — a pattern not present in the iOS SDK.

### Page Types

`CART`, `CHECKOUT`, `HOME`, `MINI_CART`, `PRODUCT_DETAILS`, `PRODUCT_LISTING`, `SEARCH_RESULTS`

### Modal Events

`ModalEvents` has more callbacks than the iOS modal delegates: `onClick`, `onApply`, `onLoading`, `onSuccess`, `onError`, `onCalculate`, `onShow`, `onClose`.

### Integration Pattern (XML View)

```kotlin
val config = PayPalMessageConfig(
    data = PayPalMessageData(
        clientID = "YOUR_CLIENT_ID",
        environment = PayPalEnvironment.SANDBOX,
        amount = 100.0,
        pageType = PayPalMessagePageType.CART,
        offerType = PayPalMessageOfferType.PAY_LATER_SHORT_TERM,
    ),
    style = PayPalMessageStyle(
        color = PayPalMessageColor.BLACK,
        logoType = PayPalMessageLogoType.PRIMARY,
        textAlignment = PayPalMessageAlignment.LEFT,
    ),
    viewStateCallbacks = PayPalMessageViewStateCallbacks(
        onLoading = { },
        onSuccess = { },
        onError = { error -> },
    ),
    eventsCallbacks = PayPalMessageEventsCallbacks(
        onClick = { },
        onApply = { },
    ),
)
messageView.setConfig(config)
```

### Integration Pattern (Jetpack Compose)

```kotlin
PayPalComposableMessage(
    clientId = "YOUR_CLIENT_ID",
    amount = 100.0,
    buyerCountry = "US",
    offerType = PayPalMessageOfferType.PAY_LATER_SHORT_TERM.name,
    environment = PayPalEnvironment.SANDBOX,
    onLoading = { },
    onSuccess = { },
    onError = { error -> },
    onClick = { },
    onApply = { },
)
```

> [!info] Compose compatibility note
> The README notes potential compatibility issues between Kotlin 1.8.22 and the Compose compiler. If issues arise, use `PayPalMessageView` wrapped in `AndroidView` instead.

### Analytics

```kotlin
PayPalMessageConfig.setGlobalAnalytics(
    integrationName = "YourApp",
    integrationVersion = "1.0.0"
)
```

### Distribution

Maven Central: `com.paypal.messages:paypal-messages-android:1.3.0`

Build locally: `./gradlew assemble` → `library/build/outputs/aar/library-release.aar`

## Android vs iOS — key differences

| Aspect | Android | iOS |
| --- | --- | --- |
| View class | `PayPalMessageView` extends `FrameLayout` | `PayPalMessageView` extends `UIControl` |
| Compose support | `PayPalComposableMessage` composable | `PayPalMessageView.Representable` (UIViewRepresentable) |
| Callbacks | Separate `ViewStateCallbacks` + `EventsCallbacks` data classes | Protocol delegates (`PayPalMessageViewStateDelegate`, `PayPalMessageViewEventDelegate`) |
| Style field name | `textAlignment` (`PayPalMessageAlignment`) | `textAlign` (`PayPalMessageTextAlign`) |
| language/locale types | Typed `PayPalLanguage`/`PayPalLocale` enums | Raw `String?` |
| Enum indexing | Int-indexed via `invoke(attributeIndex)` for XML | No int indexing — Swift enums by case name |
| Availability | Still in development / sandbox recommended | v1.2.0 generally available |

## Raw Sources

- [[github-paypal-messages-android]] — stub file with file list and "What each file covers" table; detail in `raw/github-paypal-messages-android/`

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-pay-later]] — Pay Later products surfaced via this messaging SDK
- [[paypal-android-sdk]] — umbrella Android SDK
- [[source-github-paypal-messages-ios]] — iOS counterpart for comparison
