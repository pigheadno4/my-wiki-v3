---
title: "Adyen Google Pay Android Component migration to 5.9.x"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/google-pay/android-component/migrate"
raw_files:
  - "adyen/docs/payment-methods/google-pay/android-component/migrate/2026-09-15.md"
tags: [adyen, google-pay, android, component, migration]
---

## Overview

This [[adyen]] Android Google Pay Component guide describes an **optional** migration from earlier 5.x.x versions to **5.9.x**. It says 5.9.0 introduced a simplified integration that omits the deprecated `onActivityResult` path and can include the Google Pay button. It is a historical migration guide, not a statement that 5.9.x is the current SDK or a universal prerequisite for Google Pay. [[adyen-android-sdk]]

## Key takeaways

- **Activity result removal:** Add `AdyenComponentView` to the layout and attach `googlePayComponent` with `lifecycleOwner`, or use the shown Jetpack Compose `AdyenComponent(googlePayComponent)`. The guide then says activity-result-related code can be cleaned up and gives `onActivityResult`/`handleActivityResult` removal as an example. See raw lines 27–60.
- **Button choice:** If the app keeps its own Google Pay button, replace `googlePayComponent.startGooglePayScreen(…)` with `googlePayComponent.submit()`. To show the button inside `AdyenComponentView`, remove the app's button and configure `setSubmitButtonVisible(true)`; `setGooglePayButtonStyling(…)` is optional. The page says the `com.google.pay.button:compose-pay-button` dependency can then be removed. These are alternative UI paths within this migration, not a requirement to adopt the embedded button. See raw lines 62–83.
- **Availability handling:** The guide says a separate `GooglePayComponent.PROVIDER.isAvailable(…)` call is no longer needed because `GooglePayComponent` checks on initialization; unavailability is reported as `GooglePayUnavailableException` in `onError`. This is SDK behavior asserted for the migration path, not proof that a device or merchant is eligible. See raw lines 85–89.

## Detail locators

- Version and optional migration scope: raw lines 15–25.
- View/Compose examples and deprecated callback cleanup: raw lines 27–60.
- Button configuration and dependency note: raw lines 62–83.
- Availability check and error callback: raw lines 85–89.

## Related

- [[adyen-android-sdk]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-google-pay-android-component]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/google-pay/android-component/migrate/2026-09-15|Adyen Android Google Pay 5.9.x migration guide]]
