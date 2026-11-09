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
| **Payment Element** | Moderate | Embeddable view | You control |

**Payment Sheet** is recommended for most use cases — single prebuilt sheet handles display, collection, and confirmation. Supports 50+ appearance customizations.

**Flow Controller** splits selection (sheet) from confirmation (your UI) — useful for "confirm on next screen" flows.

**Payment Element** embeds payment method selection anywhere in your app — most flexible, most code. Three layout options: radio buttons, checkmarks, floating buttons. Wallets (Apple Pay, Link) shown inline as options (not in a separate section).

## Three API Patterns

### 1. PaymentIntent — Charge Now

Collect payment and charge immediately. Stripe auto-shows "Save my info" checkbox.

Supports: single-use and reusable payment methods.

### 2. SetupIntent — Save Without Charging

Collect and save a PM for future use, no charge now.

Supports: reusable PMs only (no BNPLs, no one-time methods).

Use cases: free trial onboarding, crowdfunding setup, utility/service pre-auth.

### 3. PaymentIntent + `setup_future_usage` — Charge + Save

Charge now AND save the PM for future.

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

CustomerSessions API controls:

- Show/hide save consent checkbox
- Show/hide saved PMs in UI
- Allow or prevent PM removal
- Prevent removal of last saved PM

Consent collection is automatic — handles global compliance requirements.

## Payment Sheet Detail

- **Layout**: `.automatic` (Stripe picks), `.vertical`, or `.horizontal`
- **Appearance API**: colors, fonts, borders, shadows — 50+ aspects
- **Address collection**: name, email, phone, full billing address — configurable per transaction
- **CVC recollection**: optional for saved card payments
- **Card brand filtering**: restrict which card brands you accept

## Key Facts

- 100+ payment methods including Apple Pay, Google Pay, Link, Amazon Pay, custom PMs
- Fraud protection included
- SDK: iOS, Android, React Native
- Wallet PMs (Apple Pay, Google Pay) require domain registration
- Android US apps can process in-app payments for digital goods; iOS digital goods require app-to-web flow (Stripe Checkout)

## Key Players

- [[stripe]] — the sole provider of this SDK

## Sources

- [[source-stripe-inapp-payments-overview]] — primary reference: UI options, API patterns, saved PM controls, features table
- [[source-stripe-inapp-payment-sheet]] — Payment Sheet detail: layout, Appearance API, wallets, address collection, CVC recollection, card brand filtering
- [[source-stripe-inapp-appearance-api]] — Mobile Appearance API: fonts (family + sizeScaleFactor), colors (categories), shapes, primary button; dark mode patterns per platform
- [[source-stripe-inapp-finalize-payments-server]] — Server confirmation: ConfirmationToken flow, FlowController update() retry, Apple Pay setup, mobile_payment_element CustomerSession
- [[source-stripe-inapp-filter-card-brands]] — Card brand filtering: allowed/disallowed, 4 brands (discover=entire Global Network inc. JCB/UnionPay/Elo), filters card form + Apple Pay/Google Pay
- [[source-stripe-inapp-accept-payment-embedded]] — EmbeddedPaymentElement integration: UIScrollView required, height delegate, update(), formSheetAction=confirm, mandate display, clearPaymentOption
- [[source-stripe-inapp-embedded-appearance-api]] — Embedded Appearance API: selectedBorderWidth, 4 row styles (flatWithDisclosure requires immediateAction), per-style separator/color options
- [[source-stripe-inapp-custom-payment-methods]] — PaymentSheet/FlowController CPMs: iOS/Android/RN handlers, billing details opt-in, FlowController cancel requirement, payment recording
- [[source-stripe-inapp-embedded-custom-payment-methods]] — EmbeddedPaymentElement CPMs: EmbeddedPaymentElementResult (not PaymentSheetResult), same cpmt_ IDs and paymentMethodOrder, platform handler differences
- [[source-stripe-inapp-embedded-filter-card-brands]] — EmbeddedPaymentElement card brand filtering: EmbeddedPaymentElement.Configuration.CardBrandAcceptance.BrandCategory (iOS), same discover network, API diff table vs PaymentSheet
- [[source-stripe-inapp-address-element]] — Mobile Address Element overview: 236 regional formats, RTL support, autocomplete, prefill, Appearance API, Payment Sheet + Payment Element integration
- [[source-stripe-inapp-collect-addresses]] — Mobile Address Element integration: iOS UIKit (AddressViewController), iOS SwiftUI (AddressElement sheet), Android (AddressLauncher, onCreate required, Google Places), React Native (AddressSheet, manual dismiss), billing details collection config
- [[source-stripe-inapp-payment-method-messaging-element]] — Mobile BNPL messaging overview: iOS + Android, auto-determines plans + localized messaging
- [[source-stripe-inapp-display-bnpl-messaging]] — Mobile BNPL messaging integration (beta): iOS UIKit async create/noContent/failed, SwiftUI phase builder + MVVM, Android separate dependency + Content() composable, configuration/appearance options
- [[source-stripe-inapp-ios-android-purchases]] — Platform rules: iOS digital goods must redirect to Stripe Checkout; Android can go fully in-app; 3 acceptance paths + customer portal
- [[source-stripe-inapp-digital-goods-checkout]] — iOS digital goods app-to-web: origin_context=mobile_app, Universal Links setup, SKPaymentQueue.canMakePayments() gate, open in Safari, checkout.session.completed fulfillment
- [[source-stripe-inapp-digital-goods-payment-links]] — iOS digital goods via Payment Links (no server): Apple Pay US+EEA only, prefilled_email/client_reference_id URL params, success URL set in Dashboard
- [[source-stripe-inapp-digital-goods-custom-checkout]] — iOS digital goods via Elements (own checkout page): subscription default_incomplete pattern, invoice.payment_succeeded webhook, expand latest_invoice.payment_intent
- [[source-stripe-inapp-digital-goods-customer-portal]] — iOS subscription management: billingPortal.sessions.create, open in Safari, customer.subscription.* webhooks, Connect = platform only
- [[source-stripe-inapp-customer-sheet]] — Payment Method Settings Sheet (CustomerSheet): app settings page PM management, CustomerSession + SetupIntent endpoints, iOS UIKit/SwiftUI/Android/RN, cards+US bank+SEPA (iOS only)
- [[source-stripe-inapp-migrate-confirmation-tokens]] — PaymentMethod → ConfirmationToken migration: auto handles shipping/mandate/return_url, enables server-side CVC recollection, client vs server confirmation modes
- [[source-stripe-inapp-without-card-auth]] — Legacy simple integration (US/Canada only): error_on_requires_action=true, STPPaymentCardTextField/CardInputWidget/CardField, synchronous decline, no webhooks
- [[source-stripe-inapp-save-card-without-auth]] — Legacy save-card (US/Canada only): attach PM to Customer, charge later with error_on_requires_action, setup_future_usage=on_session, CVC re-collection patterns
- [[source-stripe-inapp-upgrade-to-handle-actions]] — Upgrade legacy integration to handle 2FA: remove error_on_requires_action, add confirmation_method=manual + use_stripe_sdk, two-round-trip pattern, 1-hour re-confirm window
- [[source-stripe-managed-payments-mobile]] — iOS digital goods with Managed Payments as MoR: managed_payments.enabled + origin_context=mobile_app, Stripe handles tax/fraud/disputes, Universal Links return
