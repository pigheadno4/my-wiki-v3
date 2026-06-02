<!-- Repo: https://github.com/stripe/stripe-ios -->
<!-- Commit SHA: 9f0729618c754def0d212065a11eaeb7e435dab0 -->
<!-- Date reviewed: 2026-05-13 -->
<!-- Detail directory: raw/github-stripe-ios/ -->
<!-- Files saved (read directly from these paths):
  raw/github-stripe-ios/README.md
  raw/github-stripe-ios/MIGRATING.md
  raw/github-stripe-ios/StripePaymentSheet/README.md
  raw/github-stripe-ios/StripePayments/README.md
  raw/github-stripe-ios/StripeApplePay/README.md
  raw/github-stripe-ios/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheet.swift
  raw/github-stripe-ios/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentElementConfiguration.swift
  raw/github-stripe-ios/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Embedded/EmbeddedPaymentElement.swift
  raw/github-stripe-ios/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/CustomerSheet/CustomerSheet.swift
  raw/github-stripe-ios/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheet+API.swift
  raw/github-stripe-ios/StripeApplePay/StripeApplePay/Source/ApplePayContext/STPApplePayContext.swift
  raw/github-stripe-ios/StripePayments/StripePayments/Source/API Bindings/STPAPIClient+Payments.swift
  raw/github-stripe-ios/StripePayments/StripePayments/Source/PaymentHandler/STPPaymentHandler.swift
-->
<!-- Deep-dive fallback: if a query needs files NOT listed above, re-clone from https://github.com/stripe/stripe-ios at commit 9f0729618c754def0d212065a11eaeb7e435dab0, then save any newly discovered files into raw/github-stripe-ios/ preserving their repo-relative paths -->

## What each file covers

| File | What to find there |
| ---- | ------------------ |
| `raw/github-stripe-ios/README.md` | Features overview, module table (StripePaymentSheet, StripeConnect, StripeIdentity, StripeFinancialConnections), requirements (iOS 13+), IAP limitation, 40+ localizations |
| `raw/github-stripe-ios/MIGRATING.md` | Breaking changes across SDK versions |
| `raw/github-stripe-ios/StripePaymentSheet/README.md` | PaymentSheet module overview, requirements, integration guide links |
| `raw/github-stripe-ios/StripePayments/README.md` | StripePayments low-level API module overview |
| `raw/github-stripe-ios/StripeApplePay/README.md` | StripeApplePay lightweight module for App Clips (iOS 13+) |
| `raw/github-stripe-ios/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheet.swift` | PaymentSheet main class: init with IntentConfiguration or clientSecret, present(from:completion:), PaymentSheetResult enum |
| `raw/github-stripe-ios/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentElementConfiguration.swift` | Shared PaymentElement configuration: appearance, billingDetails, defaultBillingDetails, shippingDetails |
| `raw/github-stripe-ios/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Embedded/EmbeddedPaymentElement.swift` | EmbeddedPaymentElement API: inline (non-sheet) payment UI, delegate, update/confirm flow |
| `raw/github-stripe-ios/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/CustomerSheet/CustomerSheet.swift` | CustomerSheet: saved payment methods management UI, CustomerAdapter protocol, delegate |
| `raw/github-stripe-ios/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheet+API.swift` | PaymentSheet server-side confirm: confirm(PaymentIntent/SetupIntent), IntentConfiguration, confirmHandler callback |
| `raw/github-stripe-ios/StripeApplePay/StripeApplePay/Source/ApplePayContext/STPApplePayContext.swift` | STPApplePayContext: presentApplePay, delegate (didCreatePaymentMethod, didCompleteTransaction), paymentStatus |
| `raw/github-stripe-ios/StripePayments/StripePayments/Source/API Bindings/STPAPIClient+Payments.swift` | STPAPIClient extensions: createPaymentMethod, confirmPaymentIntent, confirmSetupIntent, retrievePaymentIntent/SetupIntent |
| `raw/github-stripe-ios/StripePayments/StripePayments/Source/PaymentHandler/STPPaymentHandler.swift` | STPPaymentHandler: handleNextAction, confirmPayment/SetupIntent with 3DS, STPAuthenticationContext protocol |
