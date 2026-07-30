---
title: "Stripe React Native SDK"
type: concept
category: framework
tags: [stripe, react-native, mobile, sdk, payments, apple-pay, google-pay, payment-sheet, ios, android]
---

## Overview

`@stripe/stripe-react-native` is Stripe's official React Native SDK for building native payment UIs on iOS and Android. It wraps Stripe's native iOS/Android SDKs, provides PCI-compliant card collection (data goes directly to Stripe, not your server), automatic 3DS/SCA handling, and prebuilt UI components including PaymentSheet.

Latest ingested version: **0.72.0**. The cumulative history preserves the legacy `0.65.1` manual capsule.

## Platform requirements

| Platform | Minimum |
|---|---|
| Android | API 23 (Android 6.0), `compileSdkVersion` 36, `targetSdkVersion` 36, Kotlin 2.x |
| Expo | `expo install @stripe/stripe-react-native` (version-pinned per Expo SDK) |

## Important limitation

**Must use App Store / Play Store IAP APIs** for: subscriptions, in-game currency, premium content unlocks, full-version upgrades. Stripe SDK only for physical goods, services, and other non-IAP scenarios.

## Initialization

```tsx
// Wrap your app (component pattern)
<StripeProvider publishableKey="pk_..." merchantIdentifier="merchant.com.app">
  <App />
</StripeProvider>

// Or imperatively (class components, early init)
await initStripe({ publishableKey: 'pk_...', merchantIdentifier: 'merchant.com.app' })
```

Expo: configure via plugin in `app.json` (`merchantIdentifier`, `enableGooglePay`).

## Core hooks

| Hook | Key methods |
|---|---|
| `useStripe()` | All payment functions as memoized callbacks |
| `usePaymentSheet()` | `initPaymentSheet`, `presentPaymentSheet`, `confirmPaymentSheetPayment` |
| `usePlatformPay()` | `isPlatformPaySupported`, `confirmPlatformPayPayment`, `createPlatformPayPaymentMethod`, `updatePlatformPaySheet`, `dismissPlatformPay` |
| `useConfirmPayment()` | Confirm a PaymentIntent |
| `useConfirmSetupIntent()` | Confirm a SetupIntent |
| `useFinancialConnectionsSheet()` | Bank account collection (ACH) |
| `useOnramp()` | Crypto onramp |
| `useLinkController()` | Private-preview Link selection plus explicit SetupIntent confirmation |

## Core components

| Component | Notes |
|---|---|
| `<StripeProvider>` | SDK init wrapper |
| `<CardField>` | Inline card input (number/expiry/CVC) |
| `<CardForm>` | Full card form; requires Material Components theme on Android |
| `<PlatformPayButton>` | Unified Apple Pay / Google Pay button |
| `<AddressSheet>` | Address collection |
| `<CustomerSheet>` | Saved payment methods UI |
| `<EmbeddedPaymentElement>` | Embeddable payment-method UI for merchant-owned layouts |
| `<PaymentMethodMessagingElement>` | BNPL messaging (Klarna, Afterpay, etc.) |
| Connect embedded components | Account onboarding, payments, and payouts surfaces |

## PaymentSheet

Prebuilt payment UI covering the full checkout flow. Supports: Card, Apple Pay, Google Pay, SEPA, Bancontact, Billie, iDEAL, EPS, P24, Afterpay/Clearpay, Klarna, Giropay, ACH. Includes card scanning on iOS and Android.

```tsx
const { initPaymentSheet, presentPaymentSheet } = usePaymentSheet();

// 1. Init (server creates PaymentIntent, returns clientSecret)
await initPaymentSheet({ paymentIntentClientSecret: secret, merchantDisplayName: 'My Shop' });

// 2. Present
const { error } = await presentPaymentSheet();
```

## Apple Pay / Google Pay

Use `usePlatformPay()` — the legacy `useApplePay` / `useGooglePay` hooks were removed in v0.29.0.

```tsx
const { isPlatformPaySupported, confirmPlatformPayPayment } = usePlatformPay();
const supported = await isPlatformPaySupported({ googlePay: { testEnv: true } });
```

## Key imperative functions

- `createPaymentMethod(params)` — tokenize card or bank details
- `confirmPayment(clientSecret, params)` — confirm a PaymentIntent (handles 3DS automatically)
- `confirmSetupIntent(clientSecret, params)` — confirm a SetupIntent
- `handleNextAction(clientSecret)` — handle 3DS or other redirect actions
- `collectBankAccountForPayment/Setup` — ACH bank collection
- `verifyMicrodepositsForPayment/Setup` — microdeposit verification
- `createRadarSession()` — Radar fraud signals
- `canAddCardToWallet(params)` — check Apple/Google wallet eligibility

## Migration notes

- **v0.29.0**: `useApplePay`, `useGooglePay`, `<ApplePayButton>`, `<GooglePayButton>` removed → use `usePlatformPay` / `<PlatformPayButton>`
- **Android SDK 36**: `compileSdkVersion 36`, `targetSdkVersion 36`, `minSdkVersion 23` required
- **v0.72.0 private-preview Link Controller**: `presentLinkController` selects a payment method but no longer confirms a SetupIntent; call `confirmLinkControllerSetupIntent` explicitly afterward

## Evidence boundaries

- The React Native package delegates runtime payment behavior to Stripe's native iOS and Android SDKs.
- Exported APIs do not prove merchant eligibility, preview access, payment-method activation, or country/currency availability.
- Mobile apps still need a backend to create Intents, Customer Sessions, Checkout Sessions, Connect sessions, and other client-secret-bearing objects.

## Sources

- [[source-github-stripe-react-native]] — cumulative GitHub source: legacy v0.65.1 plus approved v0.72.0 full baseline
- [[changelog-github-stripe-react-native]] — package-qualified release history and migration impact
