<!-- Repo: https://github.com/paypal/paypal-android -->
<!-- Commit SHA: 2685f88374fa09c17e5af6f3ea88ba622d940901 -->
<!-- Date reviewed: 2026-04-13 -->
<!-- Detail directory: raw/github-paypal-android/ -->
<!-- Files saved (read directly from these paths):
  raw/github-paypal-android/README.md
  raw/github-paypal-android/MOBILE_CHECKOUT_MIGRATION_GUIDE.md
  raw/github-paypal-android/v2_MIGRATION_GUIDE.md
  raw/github-paypal-android/CHANGELOG.md
  raw/github-paypal-android/CardPayments/src/main/java/com/paypal/android/cardpayments/CardClient.kt
  raw/github-paypal-android/CardPayments/src/main/java/com/paypal/android/cardpayments/CardRequest.kt
  raw/github-paypal-android/CorePayments/src/main/java/com/paypal/android/corepayments/CoreConfig.kt
  raw/github-paypal-android/PayPalWebPayments/src/main/java/com/paypal/android/paypalwebpayments/PayPalWebCheckoutClient.kt
  raw/github-paypal-android/PayPalWebPayments/src/main/java/com/paypal/android/paypalwebpayments/PayPalWebCheckoutRequest.kt
  raw/github-paypal-android/PayPalWebPayments/src/main/java/com/paypal/android/paypalwebpayments/PayPalWebCheckoutFundingSource.kt
  raw/github-paypal-android/FraudProtection/src/main/java/com/paypal/android/fraudprotection/PayPalDataCollector.kt
  raw/github-paypal-android/FraudProtection/src/main/java/com/paypal/android/fraudprotection/PayPalDataCollectorRequest.kt
  raw/github-paypal-android/PaymentButtons/src/main/java/com/paypal/android/paymentbuttons/PayPalButton.kt
  raw/github-paypal-android/Demo/src/main/java/com/paypal/android/ui/approveorder/ApproveOrderViewModel.kt
  raw/github-paypal-android/Demo/src/main/java/com/paypal/android/ui/paypalweb/PayPalWebViewModel.kt
  raw/github-paypal-android/Demo/src/main/java/com/paypal/android/usecase/CreateOrderUseCase.kt
  raw/github-paypal-android/Demo/src/main/java/com/paypal/android/usecase/CompleteOrderUseCase.kt
  raw/github-paypal-android/Demo/src/main/java/com/paypal/android/api/services/SDKSampleServerAPI.kt
-->
<!-- Deep-dive fallback: if a query needs files NOT listed above, re-clone from the repo URL at the commit SHA above, then save any newly discovered files into raw/github-paypal-android/ preserving their repo-relative paths -->

## paypal/paypal-android

PayPal Mobile Android SDK — Kotlin modules for accepting PayPal, card, and Venmo payments in Android apps.

## What each file covers

| File | What to find there |
| ---- | ------------------ |
| `raw/github-paypal-android/README.md` | Module overview, installation, quick-start links |
| `raw/github-paypal-android/MOBILE_CHECKOUT_MIGRATION_GUIDE.md` | Migrating from deprecated PayPalNativePayments → PayPalWebPayments |
| `raw/github-paypal-android/v2_MIGRATION_GUIDE.md` | v1 → v2 API breaking changes and migration steps |
| `raw/github-paypal-android/CHANGELOG.md` | Version history, deprecation notices, breaking changes |
| `raw/github-paypal-android/CardPayments/.../CardClient.kt` | Core card client — `approveOrder()`, all listener callbacks, 3DS launch |
| `raw/github-paypal-android/CardPayments/.../CardRequest.kt` | CardRequest data class — orderID, card, returnUrl, sca fields |
| `raw/github-paypal-android/CorePayments/.../CoreConfig.kt` | Shared config — clientId + Environment enum |
| `raw/github-paypal-android/PayPalWebPayments/.../PayPalWebCheckoutClient.kt` | Web checkout client — `start()`, `finishStart()`, listener callbacks |
| `raw/github-paypal-android/PayPalWebPayments/.../PayPalWebCheckoutRequest.kt` | Request data class — orderID + fundingSource |
| `raw/github-paypal-android/PayPalWebPayments/.../PayPalWebCheckoutFundingSource.kt` | Funding source enum — PAYPAL, PAY_LATER, PAYPAL_CREDIT, VENMO |
| `raw/github-paypal-android/FraudProtection/.../PayPalDataCollector.kt` | Device data collection — `collectDeviceData()` implementation |
| `raw/github-paypal-android/FraudProtection/.../PayPalDataCollectorRequest.kt` | Request data class — hasUserLocationConsent flag |
| `raw/github-paypal-android/PaymentButtons/.../PayPalButton.kt` | PayPalButton composable — color, shape, label, size customization |
| `raw/github-paypal-android/Demo/.../ApproveOrderViewModel.kt` | **Full end-to-end card payment sample** — create order → CardClient → 3DS → capture, with ViewModel + state |
| `raw/github-paypal-android/Demo/.../PayPalWebViewModel.kt` | **Full end-to-end web payment sample** — create order → PayPalWebCheckoutClient → finishStart → capture |
| `raw/github-paypal-android/Demo/.../CreateOrderUseCase.kt` | Server call to create an order — Retrofit/API layer |
| `raw/github-paypal-android/Demo/.../CompleteOrderUseCase.kt` | Server call to capture/authorize an order |
| `raw/github-paypal-android/Demo/.../SDKSampleServerAPI.kt` | All merchant server API endpoints the demo app uses — order, capture, authorize, vault flows |
