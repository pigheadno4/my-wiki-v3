<!-- Repo: https://github.com/paypal/paypal-ios -->
<!-- Commit SHA: 600a97a5f69ea6f44db3cf2f8b631276fd0152d8 -->
<!-- Date reviewed: 2026-04-13 -->
<!-- Detail directory: raw/github-paypal-ios/ -->
<!-- Files saved (read directly from these paths):
  raw/github-paypal-ios/README.md
  raw/github-paypal-ios/v2_MIGRATION_GUIDE.md
  raw/github-paypal-ios/CHANGELOG.md
  raw/github-paypal-ios/Sources/CardPayments/CardClient.swift
  raw/github-paypal-ios/Sources/CardPayments/Models/CardRequest.swift
  raw/github-paypal-ios/Sources/CardPayments/Models/Card.swift
  raw/github-paypal-ios/Sources/CardPayments/Models/SCA.swift
  raw/github-paypal-ios/Sources/CorePayments/CoreConfig.swift
  raw/github-paypal-ios/Sources/PayPalWebPayments/PayPalWebCheckoutClient.swift
  raw/github-paypal-ios/Sources/PayPalWebPayments/PayPalWebCheckoutRequest.swift
  raw/github-paypal-ios/Sources/PayPalWebPayments/PayPalWebCheckoutFundingSource.swift
  raw/github-paypal-ios/Sources/FraudProtection/PayPalDataCollector.swift
  raw/github-paypal-ios/Sources/PaymentButtons/PayPalButton.swift
  raw/github-paypal-ios/Sources/PaymentButtons/PaymentButton.swift
  raw/github-paypal-ios/Demo/Demo/CardPayments/CardPaymentViewModel/CardPaymentViewModel.swift
  raw/github-paypal-ios/Demo/Demo/PayPalWebPayments/PayPalWebViewModel/PayPalWebViewModel.swift
  raw/github-paypal-ios/Demo/Demo/Networking/DemoMerchantAPI.swift
-->
<!-- Deep-dive fallback: if a query needs files NOT listed above, re-clone from the repo URL at the commit SHA above, then save any newly discovered files into raw/github-paypal-ios/ preserving their repo-relative paths -->

## paypal/paypal-ios

PayPal Mobile iOS SDK — Swift modules for card, PayPal web, fraud protection, and payment button integrations.

## What each file covers

| File | What to find there |
| ---- | ------------------ |
| `raw/github-paypal-ios/README.md` | Module overview, SPM/CocoaPods installation, quick links |
| `raw/github-paypal-ios/v2_MIGRATION_GUIDE.md` | v1 → v2 breaking changes and migration steps |
| `raw/github-paypal-ios/CHANGELOG.md` | Version history, deprecations, breaking changes |
| `raw/github-paypal-ios/Sources/CardPayments/CardClient.swift` | Core card client — `CardClient(config:)`, `approveOrder()`, `vault()`, `CardDelegate` protocol |
| `raw/github-paypal-ios/Sources/CardPayments/Models/CardRequest.swift` | CardRequest struct — orderID, card, returnURL, sca fields |
| `raw/github-paypal-ios/Sources/CardPayments/Models/Card.swift` | Card struct — all card + billing address fields |
| `raw/github-paypal-ios/Sources/CardPayments/Models/SCA.swift` | SCA enum — `.scaWhenRequired` (default) / `.scaAlways` |
| `raw/github-paypal-ios/Sources/CorePayments/CoreConfig.swift` | CoreConfig struct — clientID + Environment enum |
| `raw/github-paypal-ios/Sources/PayPalWebPayments/PayPalWebCheckoutClient.swift` | Web checkout client — `start()`, `PayPalWebCheckoutDelegate`, vault support |
| `raw/github-paypal-ios/Sources/PayPalWebPayments/PayPalWebCheckoutRequest.swift` | Request struct — orderID + fundingSource |
| `raw/github-paypal-ios/Sources/PayPalWebPayments/PayPalWebCheckoutFundingSource.swift` | Funding source enum — `.paypal`, `.paylater` (rename pending), `.paypalCredit` |
| `raw/github-paypal-ios/Sources/FraudProtection/PayPalDataCollector.swift` | Device data collection — `collectDeviceData()`, no location consent flag |
| `raw/github-paypal-ios/Sources/PaymentButtons/PayPalButton.swift` | PayPalButton — UIKit + SwiftUI `Representable` wrapper |
| `raw/github-paypal-ios/Sources/PaymentButtons/PaymentButton.swift` | Base button — color, shape, label, size customization options |
| `raw/github-paypal-ios/Demo/Demo/CardPayments/CardPaymentViewModel/CardPaymentViewModel.swift` | **Full card payment end-to-end sample** — create order → approveOrder → CardDelegate → capture |
| `raw/github-paypal-ios/Demo/Demo/PayPalWebPayments/PayPalWebViewModel/PayPalWebViewModel.swift` | **Full web payment end-to-end sample** — create order → start() → delegate → capture |
| `raw/github-paypal-ios/Demo/Demo/Networking/DemoMerchantAPI.swift` | All merchant server API endpoint calls — order, capture, authorize, vault flows |
