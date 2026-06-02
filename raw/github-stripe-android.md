<!-- Repo: https://github.com/stripe/stripe-android -->
<!-- Commit SHA: c7f4742a0d964f8616563a0fef7ce66eceeb4e02 -->
<!-- Date reviewed: 2026-05-13 -->
<!-- Detail directory: raw/github-stripe-android/ -->
<!-- Files saved (read directly from these paths):
  raw/github-stripe-android/README.md
  raw/github-stripe-android/MIGRATING.md
  raw/github-stripe-android/paymentsheet/src/main/java/com/stripe/android/paymentsheet/PaymentSheet.kt
  raw/github-stripe-android/payments-core/src/main/java/com/stripe/android/Stripe.kt
  raw/github-stripe-android/payments-core/src/main/java/com/stripe/android/PaymentConfiguration.kt
  raw/github-stripe-android/paymentsheet/src/main/java/com/stripe/android/customersheet/CustomerSheet.kt
  raw/github-stripe-android/payments-core/src/main/java/com/stripe/android/googlepaylauncher/GooglePayLauncher.kt
  raw/github-stripe-android/payments-core/src/main/java/com/stripe/android/model/PaymentMethod.kt
  raw/github-stripe-android/payments-core/src/main/java/com/stripe/android/model/ConfirmPaymentIntentParams.kt
  raw/github-stripe-android/payments-core/src/main/java/com/stripe/android/PaymentAuthConfig.kt
-->
<!-- Deep-dive fallback: if a query needs files NOT listed above, re-clone from https://github.com/stripe/stripe-android at commit c7f4742a0d964f8616563a0fef7ce66eceeb4e02, then save any newly discovered files into raw/github-stripe-android/ preserving their repo-relative paths -->

## What each file covers

| File | What to find there |
| ---- | ------------------ |
| `raw/github-stripe-android/README.md` | Features overview, Gradle installation, requirements (Android 6+/API 23, compileSdk 36, Kotlin 2.x, Jetpack Compose compat table), 40+ localizations, IAP note |
| `raw/github-stripe-android/MIGRATING.md` | Breaking changes across SDK versions |
| `raw/github-stripe-android/paymentsheet/src/main/java/com/stripe/android/paymentsheet/PaymentSheet.kt` | PaymentSheet main class: Configuration (appearance, billing, customer, Google Pay, return URL), IntentConfiguration, FlowController, result types, Compose integration |
| `raw/github-stripe-android/payments-core/src/main/java/com/stripe/android/Stripe.kt` | Core `Stripe` API client: createPaymentMethod, confirmPaymentIntent, confirmSetupIntent, retrievePaymentIntent/SetupIntent, handleNextActionForPayment |
| `raw/github-stripe-android/payments-core/src/main/java/com/stripe/android/PaymentConfiguration.kt` | SDK init config: publishableKey, stripeAccountId; `PaymentConfiguration.init()` entry point |
| `raw/github-stripe-android/paymentsheet/src/main/java/com/stripe/android/customersheet/CustomerSheet.kt` | CustomerSheet: saved payment methods management UI, CustomerAdapter, Configuration, Compose/Activity integration |
| `raw/github-stripe-android/payments-core/src/main/java/com/stripe/android/googlepaylauncher/GooglePayLauncher.kt` | GooglePayLauncher: Config (merchantName, billingAddressConfig, environment), result types, Activity/Compose integration |
| `raw/github-stripe-android/payments-core/src/main/java/com/stripe/android/model/PaymentMethod.kt` | PaymentMethod data model: type enum, Card/BankAccount/BillingDetails nested types |
| `raw/github-stripe-android/payments-core/src/main/java/com/stripe/android/model/ConfirmPaymentIntentParams.kt` | ConfirmPaymentIntentParams: all confirm options (paymentMethodId, paymentMethodData, returnUrl, mandateData, setupFutureUsage) |
| `raw/github-stripe-android/payments-core/src/main/java/com/stripe/android/PaymentAuthConfig.kt` | PaymentAuthConfig: 3DS2 UI customization (button, label, navigation bar, text field, footer, selection styles) |
