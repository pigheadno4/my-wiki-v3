<!-- Repo: https://github.com/paypal/paypal-messages-android -->
<!-- Commit SHA: 1d2238c9e5ec3564ad5d8060c474e008ab7bf779 -->
<!-- Date reviewed: 2026-04-14 -->
<!-- Detail directory: raw/github-paypal-messages-android/ -->
<!-- Files saved (read directly from these paths):
  raw/github-paypal-messages-android/README.md
  raw/github-paypal-messages-android/library/src/main/java/com/paypal/messages/config/message/PayPalMessageConfig.kt
  raw/github-paypal-messages-android/library/src/main/java/com/paypal/messages/config/message/PayPalMessageData.kt
  raw/github-paypal-messages-android/library/src/main/java/com/paypal/messages/config/message/PayPalMessageStyle.kt
  raw/github-paypal-messages-android/library/src/main/java/com/paypal/messages/config/message/PayPalMessageViewStateCallbacks.kt
  raw/github-paypal-messages-android/library/src/main/java/com/paypal/messages/config/message/PayPalMessageEventsCallbacks.kt
  raw/github-paypal-messages-android/library/src/main/java/com/paypal/messages/config/PayPalMessageOfferType.kt
  raw/github-paypal-messages-android/library/src/main/java/com/paypal/messages/config/PayPalMessagePageType.kt
  raw/github-paypal-messages-android/library/src/main/java/com/paypal/messages/config/message/style/PayPalMessageColor.kt
  raw/github-paypal-messages-android/library/src/main/java/com/paypal/messages/config/message/style/PayPalMessageLogoType.kt
  raw/github-paypal-messages-android/library/src/main/java/com/paypal/messages/config/message/style/PayPalMessageAlignment.kt
  raw/github-paypal-messages-android/library/src/main/java/com/paypal/messages/config/modal/ModalEvents.kt
  raw/github-paypal-messages-android/library/src/main/java/com/paypal/messages/PayPalComposableMessage.kt
-->
<!-- Deep-dive fallback: if a query needs files NOT listed above, re-clone from https://github.com/paypal/paypal-messages-android at commit SHA 1d2238c9e5ec3564ad5d8060c474e008ab7bf779, then save any newly discovered files into raw/github-paypal-messages-android/ preserving their repo-relative paths -->

## What each file covers

| File | What to find there |
| ---- | ------------------ |
| `raw/github-paypal-messages-android/README.md` | Overview, availability status (development/sandbox), Android SDK 23+, Maven Central distribution, build steps, Gradle tasks |
| `raw/github-paypal-messages-android/library/src/main/java/com/paypal/messages/config/message/PayPalMessageConfig.kt` | `PayPalMessageConfig` data class — data/style/viewStateCallbacks/eventsCallbacks; `setGlobalAnalytics(integrationName, integrationVersion)` |
| `raw/github-paypal-messages-android/library/src/main/java/com/paypal/messages/config/message/PayPalMessageData.kt` | `PayPalMessageData` — clientID, merchantID, partnerAttributionID, amount, buyerCountry, offerType, pageType, language, locale, environment |
| `raw/github-paypal-messages-android/library/src/main/java/com/paypal/messages/config/message/PayPalMessageStyle.kt` | `PayPalMessageStyle` — color, logoType, textAlignment (note: field is `textAlignment` not `textAlign`) |
| `raw/github-paypal-messages-android/library/src/main/java/com/paypal/messages/config/message/PayPalMessageViewStateCallbacks.kt` | `PayPalMessageViewStateCallbacks` — onLoading/onSuccess/onError lambdas |
| `raw/github-paypal-messages-android/library/src/main/java/com/paypal/messages/config/message/PayPalMessageEventsCallbacks.kt` | `PayPalMessageEventsCallbacks` — onClick/onApply lambdas |
| `raw/github-paypal-messages-android/library/src/main/java/com/paypal/messages/config/PayPalMessageOfferType.kt` | Offer type enum — PAY_LATER_SHORT_TERM(0)/PAY_LATER_LONG_TERM(1)/PAY_LATER_PAY_IN_1(2)/PAYPAL_CREDIT_NO_INTEREST(3); int-indexed via `invoke(attributeIndex)` |
| `raw/github-paypal-messages-android/library/src/main/java/com/paypal/messages/config/PayPalMessagePageType.kt` | Page type enum — CART(0)/CHECKOUT(1)/HOME(2)/MINI_CART(3)/PRODUCT_DETAILS(4)/PRODUCT_LISTING(5)/SEARCH_RESULTS(6); int-indexed |
| `raw/github-paypal-messages-android/library/src/main/java/com/paypal/messages/config/message/style/PayPalMessageColor.kt` | Color enum — BLACK/WHITE/MONOCHROME/GRAYSCALE with colorResId; `@SerializedName` for JSON |
| `raw/github-paypal-messages-android/library/src/main/java/com/paypal/messages/config/message/style/PayPalMessageLogoType.kt` | Logo type enum — PRIMARY/ALTERNATIVE/INLINE/NONE with `@SerializedName` |
| `raw/github-paypal-messages-android/library/src/main/java/com/paypal/messages/config/message/style/PayPalMessageAlignment.kt` | Alignment enum — LEFT/CENTER/RIGHT with `@SerializedName` |
| `raw/github-paypal-messages-android/library/src/main/java/com/paypal/messages/config/modal/ModalEvents.kt` | `ModalEvents` — onClick/onApply/onLoading/onSuccess/onError/onCalculate/onShow/onClose lambdas |
| `raw/github-paypal-messages-android/library/src/main/java/com/paypal/messages/PayPalComposableMessage.kt` | `PayPalComposableMessage` Jetpack Compose composable — wraps `PayPalMessageView` via `AndroidView`; accepts clientId/amount/buyerCountry/offerType/environment + all callbacks |
