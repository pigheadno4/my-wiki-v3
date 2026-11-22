---
title: "Stripe In-App Payments"
type: concept
category: technology
tags: [stripe, mobile, ios, android, react-native, payment-sheet, flow-controller, payment-element, setup-future-usage]
---

## Definition

Stripe's In-App Payments SDK enables customized payment flows for iOS, Android, and React Native apps. Unlike web integrations, mobile offers three distinct UI options and tight OS integration (Apple Pay, Google Pay).

## Three UI Options

| UI | Code | Payment display | Confirm control |
| --- | --- | --- | --- |
| **Payment Sheet** | Low | Sheet | Stripe handles |
| **Flow Controller** | Moderate | Sheet | You control |
| **Payment Element** | Moderate | Embeddable view | App checkout by default. April 2026 iOS and Android guides also describe optional in-sheet confirmation. |

**Payment Sheet** is recommended for most use cases. The single prebuilt sheet handles display, collection and confirmation and supports more than 50 appearance customizations. In the November 2026 guide, native Payment Sheet accepts only `Customer` objects when a Stripe customer identity is supplied. Customer-configured Accounts are unsupported in this route. The retained iOS 26.11.0 and React Native 0.84.0 SDK declarations make customer configuration optional within those snapshots. The April iOS Embedded Payment Element save-during-payment guide separately documents the server-side Account-or-Customer path. See [[source-stripe-inapp-payment-sheet]] and [[source-stripe-inapp-save-during-payment]].

**Flow Controller** splits selection (sheet) from confirmation (your UI) — useful for "confirm on next screen" flows.

**Payment Element** embeds payment method selection in your app. Three layout options include radio buttons, checkmarks and floating buttons. Wallets such as Apple Pay and Link are shown inline where eligible. The overview describes merchant-controlled confirmation as the standard pattern. The dated native iOS embedded guide defaults to **Continue** in the details sheet and supports optional in-sheet confirmation with `formSheetAction`. See [[source-stripe-inapp-accept-payment-embedded]].

## Three API Patterns

### 1. PaymentIntent — Charge Now

A PaymentIntent targets a charge during checkout. The save checkbox depends on the UI’s configuration, such as `payment_method_save` for the embedded card flow. A delayed method can return client `.completed` while payment is pending. Use server-side payment events to distinguish processing, success and failure. See [[source-stripe-inapp-accept-payment-embedded]].

Supports: single-use and reusable payment methods.

### 2. SetupIntent — Save Without Charging

Collect and save a PM for future use, no charge now.

Supports: reusable PMs only (no BNPLs, no one-time methods).

Use cases: free trial onboarding, crowdfunding setup, utility/service pre-auth.

### 3. PaymentIntent + `setup_future_usage` — Charge + Save

Use a PaymentIntent with `setup_future_usage` to attempt payment and save an eligible method for future use. Top-level future use excludes one-time methods such as most BNPLs. The April mobile Payment Element pay-and-save guide limits this flow to cards and US bank accounts. In the April 23 mobile card flow with a Customer, `setup_future_usage` expresses intended reuse and attaches the resulting PaymentMethod after confirmation and any required customer actions. Use `on_session` for future payments with the customer present, as shown in the combined example, or `off_session` for intended reuse that can occur while they are absent. See [[source-stripe-inapp-save-card-without-auth]].

The examples below show generic server-side settings. In the standard April 2026 embedded pay-and-save flow, the server’s global `setup_future_usage` matches the client `IntentConfiguration`. The separate embedded per-method SDK preview leaves both `setup_future_usage` and `payment_method_options[X][setup_future_usage]` unset on the server PaymentIntent so the SDK can supply the settings. See [[source-stripe-inapp-accept-payment-embedded#Saving Payment Methods and Consent]].

```yaml
# Save all PMs (disables one-time methods like most BNPLs)
setup_future_usage: 'off_session'

# Mix one-time and reusable — save only specific PMs
payment_method_options:
  card:
    setup_future_usage: 'off_session'
```

## Saved Payment Methods

Supported: **card**, **US Bank Account**, **SEPA Debit**

The April and November 2026 native Payment Sheet guides describe automatic saving-consent UI. The merchant remains responsible for applicable rules, terms and purpose-specific consent, as scoped in the separate April iOS Payment Element save guide. CustomerSessions API controls:

- Show/hide save consent checkbox
- Show/hide saved PMs in UI
- Allow or prevent PM removal
- Prevent removal of last saved PM

Stripe provides configurable consent and redisplay controls. The April 2026 mobile guides assign the merchant responsibility for compliance with applicable laws, regulations and network rules when saving payment details. Explain the intended use in the terms, obtain explicit consent for that use, and retain the written agreement. CustomerSession features control the saved-method UI. Use `allow_redisplay` to distinguish methods that can be shown for future purchases, with consent for that specific use. In the April 22 mobile Payment Element save-during-payment guide, `setup_future_usage` is limited to cards and US bank accounts. See [[source-stripe-inapp-accept-payment-embedded#Saving Payment Methods and Consent]], [[source-stripe-inapp-finalize-payments-server]] and [[source-stripe-inapp-save-during-payment]].

## Payment Sheet Detail

- **Layout** — the April 2026 guide writes `.automatic`, `.vertical` and `horizontal`. The November guide describes automatic layout (Stripe selects), vertical or horizontal in plain language.
- **Appearance API**: colors, fonts, borders, shadows — 50+ aspects
- **Billing details** — name, email, phone and full or partial billing address are configurable. The November 2026 Payment Sheet guide adds Stripe-provided autocomplete for full addresses in supported countries, subject to the Google Maps Platform Acceptable Use Policy.
- **CVC recollection**: optional for saved card payments
- **Card brand filtering**. April PaymentSheet guidance describes client-side filtering of the card form, Apple Pay on iOS and React Native, and Google Pay on Android. Retained SDK declarations exclude Link from this filter. Server Intent confirmation and the EmbeddedPaymentElement configuration are separate. See [[source-stripe-inapp-filter-card-brands]] for version and wallet wording qualifications, including the separate embedded Android wording.

## Key Facts

- The April and November overviews list 40+ dynamically displayed methods alongside eligible saved methods and a separate 100+ catalog figure, including wallets and custom methods. Available methods depend on the checkout.
- Fraud protection included
- SDK: iOS, Android, React Native
- The overview’s wallet-domain footnote links to web Elements and embeddable Checkout. Native iOS Apple Pay uses Apple Merchant ID, certificate and Xcode configuration. Native Android Google Pay uses Android API and SDK configuration. See [[source-stripe-inapp-save-during-payment]].
- The April and November 2026 US-scoped overview says iOS digital-goods apps **can** redirect to an external Stripe Checkout page and Android apps **can** process directly in-app with a third-party processor such as Stripe; it lists Payment Links separately. The Checkout guide's US iOS route checks the StoreKit storefront and device purchasing before opening Safari. These captures do not make hosted Checkout the sole iOS route, establish that Android has no other restrictions, or prove current App Store or merchant eligibility. See [[source-stripe-inapp-ios-android-purchases]] and [[source-stripe-inapp-digital-goods-checkout]].
- Separate dated iOS app-to-web guides describe Stripe-hosted Checkout, hosted Payment Links for a limited catalog, and a merchant-owned Elements web checkout opened in Safari with Universal Link return. The custom guide does not describe native in-app iOS Elements. The US/EEA Apple Pay statements in the Payment Links and custom Elements guides are dated guide scope, not fresh platform-policy determinations. See [[source-stripe-inapp-digital-goods-payment-links]] and [[source-stripe-inapp-digital-goods-custom-checkout]].

## Key Players

- [[stripe]] — the sole provider of this SDK

## Sources

- [[source-stripe-inapp-payments-overview]] — April and November 2026 native overview. The November tap-to-add private preview has separate Payment Sheet and Payment Element routes for compatible NFC Android devices, with access-request and versioned SetupIntent details.
- [[source-stripe-inapp-payment-sheet]] — April and November 2026 Payment Sheet guides for layout, appearance, saved methods, customer identity and billing address collection. The linked Tap to Add guide describes the separate request-access Android NFC private preview.
- [[source-stripe-inapp-appearance-api]] — Mobile Appearance API: fonts (family + sizeScaleFactor), colors (categories), shapes, primary button; dark mode patterns per platform
- [[source-stripe-inapp-save-during-payment]] — 2026-04-22 mobile PaymentIntent save guide with purpose-specific merchant consent, dated platform example discrepancies, and delayed payment outcomes. The 2026-11-07 capture is a Payment Sheet variant index.
- [[source-stripe-inapp-finalize-payments-server]] — April 2026 deferred PaymentIntent and SetupIntent guide with ConfirmationToken, platform-specific FlowController reconfiguration, and server outcome handling. November 2026 variant navigation index.
- [[source-stripe-inapp-filter-card-brands]] — April 2026 client-side PaymentSheet filter for iOS, Android, and React Native, including Discover Global Network, dated wallet scope, Link exclusion in retained SDKs, and a November variant index
- [[source-stripe-inapp-accept-payment-embedded]] — April 2026 embedded integration by platform and intent, plus November variant navigation. See the [[source-stripe-inapp-accept-payment-embedded#Mandate Display|Swift mandate flag conflict]], [[source-stripe-inapp-accept-payment-embedded#iOS Authentication Returns|native iOS SDK custom-scheme return]] and [[source-stripe-inapp-accept-payment-embedded#Saving Payment Methods and Consent|embedded per-method preview and merchant consent]].
- [[source-stripe-inapp-embedded-appearance-api]] — Embedded Appearance API: selectedBorderWidth, 4 row styles (flatWithDisclosure requires immediateAction), per-style separator/color options
- [[source-stripe-inapp-custom-payment-methods]] — April 2026 PaymentSheet custom methods and their iOS, Android and React Native handler examples. Includes Android FlowController cancellation on exit without confirmation, billing details opt-in and version-scoped optional payment reporting. November supplies platform navigation.
- [[source-stripe-inapp-embedded-custom-payment-methods]] — April 2026 mobile EmbeddedPaymentElement guide for iOS, Android and React Native, with separate handler APIs and external payment reporting. `EmbeddedPaymentElementResult` is the Swift embedded signature. The November capture indexes the variants.
- [[source-stripe-inapp-embedded-filter-card-brands]] — April 2026 Embedded card-brand guide and November platform index. In StripePaymentSheet 26.11.0 the separate Embedded configuration uses aliases to the PaymentSheet brand type. The iOS setting filters Apple Pay’s request networks on the client. React Native 0.84.0 scopes Apple Pay to iOS and Google Pay to Android. Both retained SDKs exclude Link filtering. Android Google Pay setup alone leaves actual Embedded network filtering unverified.
- [[source-stripe-inapp-address-element]] — April 2026 overview of 236 regional address formats (including RTL), autocomplete, saved-address prefill and Appearance API. It names Payment Sheet and Payment Element on iOS, and Payment Element and Link on Android and React Native. The November capture links three overview variants. See [[source-stripe-inapp-collect-addresses]] for each platform’s collection and prefill configuration.
- [[source-stripe-inapp-collect-addresses]] — Mobile Address Element integration: iOS UIKit (AddressViewController), iOS SwiftUI (AddressElement sheet), Android (AddressLauncher, onCreate required, Google Places), React Native (AddressSheet, manual dismiss), billing details collection config
- [[source-stripe-inapp-payment-method-messaging-element]] — April 2026 localized mobile BNPL messaging for iOS and Android, November iOS/Android/React Native navigation, and separately versioned React Native public preview. Messaging content leaves approval and payment state open.
- [[source-stripe-inapp-display-bnpl-messaging]] — April 2026 mobile preview examples for UIKit, SwiftUI, and Android. `noContent` describes absence of displayable content for that configuration. November adds React Native variant navigation. See the guide for the separately versioned iOS installation and React Native SDK qualifications.
- [[source-stripe-inapp-ios-android-purchases]] — April/November 2026 US-scoped navigation overview: conditional iOS external Checkout example, separate Payment Links acceptance path, Android direct in-app example, and customer portal for subscription management; it neither makes Checkout exclusive nor establishes current storefront, policy, or merchant eligibility
- [[source-stripe-inapp-digital-goods-checkout]] — captured US iOS app-to-web Checkout route: Accounts v2 `customer_account` (qualified availability) or Customers v1 `customer`, Universal Links and Safari; server grants credits from verified webhooks only after paid status or asynchronous success, not the return URL alone
- [[source-stripe-inapp-digital-goods-payment-links]] — April/November 2026 iOS guide: Dashboard-created hosted link needs no app endpoint for creation; production fulfillment calls for a trusted webhook receiver, Universal Link return, and qualified US/EEA Apple Pay scope. URL-supplied reference IDs and email prefill aid reconciliation but do not authenticate a user or prove entitlement
- [[source-stripe-inapp-digital-goods-custom-checkout]] — April/November 2026 iOS guide: merchant-owned Elements web checkout in Safari, Universal Link return, separate Accounts v2 `customer_account` and Customers v1 `customer` subscription examples, and webhook-driven access rather than return-URL or subscription-creation proof
- [[source-stripe-inapp-digital-goods-customer-portal]] — iOS subscription **management**: server-created portal session using a Stripe Customer ID, Safari and Universal Link return, subscription-status webhooks; for Connect configure the portal on the platform, while the platform may use the API to manage configurations for connected accounts or customer groups (2026-04-22 and 2026-11-07 captures)
- [[source-stripe-inapp-customer-sheet]] — Payment Method Settings Sheet (CustomerSheet): app settings page PM management, CustomerSession + SetupIntent endpoints, iOS UIKit/SwiftUI/Android/RN, cards+US bank+SEPA (iOS only)
- [[source-stripe-inapp-migrate-confirmation-tokens]] — April 2026 migration for existing mobile PaymentMethod integrations, with SDK-specific token callbacks, collected or configured token fields, optional saved-card CVC recollection, and client versus server initial confirmation. The server can return the Intent's client secret for SDK next actions. November's base is a platform index.
- [[source-stripe-inapp-without-card-auth]] — April 2026 basic card integration for businesses accepting only US and Canadian cards. The server immediately attempts to confirm the PaymentIntent and uses its `succeeded` response for immediate fulfillment. Issuer authentication requests fail in this path. November supplies platform navigation.
- [[source-stripe-inapp-save-card-without-auth]] — 2026-04-23 guide to mobile card saving and later charging for merchants doing business primarily in the US and Canada, with authentication limits and optional CVC re-collection. The November capture is platform navigation.
- [[source-stripe-inapp-upgrade-to-handle-actions]] — April 2026 manual-confirm card authentication migration. The guide points to repeated Dashboard failures like the issuer-authentication example or the API diagnostic `requires_action_not_handled`. A first attempt can succeed. When action is required, reconfirm the same Intent from `requires_confirmation` within the guide’s one-hour window and fulfill on server `succeeded`. The November 2026 capture links platform variants. The source dates the sandbox mismatch, React Native `handleCardAction` removal (replacement verified in 0.84.0), iOS 26.11.0 Objective-C selector deprecation, and Android 23.25.1 `ComponentActivity` and `Fragment` overloads.
- [[source-stripe-managed-payments-mobile]] — April and November 2026 iOS app-to-web Managed Payments guide for eligible digital goods in some countries. Uses the app user's mapped Stripe Customer in `customer`, Safari, and a Universal Link return. Grant entitlements from verified, paid server outcomes, independently of the return.
