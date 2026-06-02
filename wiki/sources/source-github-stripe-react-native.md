---
title: "GitHub: stripe/stripe-react-native"
type: source
date_ingested: 2026-05-13
original_format: github-repo
raw_files:
  - "github-stripe-react-native.md"
tags: [stripe, react-native, mobile, sdk, payments, apple-pay, google-pay, payment-sheet]
---

## Summary

Official Stripe React Native SDK (`@stripe/stripe-react-native`, v0.65.1). Provides native payment UI components, hooks, and functions for building payment flows in React Native apps on iOS and Android. Wraps Stripe's native iOS and Android SDKs.

## Key features

- **PaymentSheet**: prebuilt payment UI for mobile. Accepts cards, Apple Pay, Google Pay, SEPA, Bancontact, Billie, iDEAL, EPS, P24, Afterpay/Clearpay, Klarna, Giropay, ACH. Card scanning on iOS and Android.
- **PCI compliance**: sensitive card data sent directly to Stripe, never through your server.
- **SCA / 3DS**: automatic 3D Secure authentication when required.
- **Apple Pay / Google Pay**: via `usePlatformPay()` hook (unified API; legacy `useApplePay`/`useGooglePay` removed in v0.29.0).
- **Financial Connections**: bank account collection and verification.
- **Radar**: `createRadarSession()` for fraud signals.
- **Connect**: `ConnectComponentsProvider` + embedded Connect components.
- **Crypto onramp**: `useOnramp()` hook.

## Platform requirements

| Platform | Minimum |
|---|---|
| Android | API 23 (Android 6.0), `compileSdkVersion` 36, Kotlin 2.x |
| iOS | Configured via `.podspec` |
| Expo | Use `expo install @stripe/stripe-react-native` (version-pinned) |

## Initialization

Two patterns:

```tsx
// Component-based
<StripeProvider publishableKey="pk_..." merchantIdentifier="merchant.com.app">
  {children}
</StripeProvider>

// Imperative (for class components or early init)
await initStripe({ publishableKey: 'pk_...', merchantIdentifier: 'merchant.com.app' })
```

Expo: add plugin to `app.json` with `merchantIdentifier` and `enableGooglePay`.

## Core hooks

| Hook | Purpose |
|---|---|
| `useStripe()` | All imperative functions as memoized callbacks |
| `usePaymentSheet()` | `initPaymentSheet`, `presentPaymentSheet`, `confirmPaymentSheetPayment` |
| `usePlatformPay()` | Apple Pay / Google Pay: `isPlatformPaySupported`, `confirmPlatformPayPayment`, `createPlatformPayPaymentMethod`, `updatePlatformPaySheet` |
| `useConfirmPayment()` | Confirm a PaymentIntent |
| `useConfirmSetupIntent()` | Confirm a SetupIntent |
| `useFinancialConnectionsSheet()` | Bank account collection |
| `useOnramp()` | Crypto onramp |

## Core components

| Component | Purpose |
|---|---|
| `<StripeProvider>` | SDK initialization wrapper |
| `<CardField>` | Inline card number/expiry/CVC input |
| `<CardForm>` | Full card form (requires Material Components theme on Android) |
| `<PlatformPayButton>` | Apple Pay / Google Pay button |
| `<AddressSheet>` | Address collection |
| `<CustomerSheet>` | Saved payment methods management |
| `<PaymentMethodMessagingElement>` | BNPL messaging (Klarna, Afterpay, etc.) |

## Key imperative functions (via `useStripe` or direct import)

- `createPaymentMethod(params, options)` — create a PaymentMethod from card/bank details
- `confirmPayment(clientSecret, params)` — confirm a PaymentIntent
- `confirmSetupIntent(clientSecret, params)` — confirm a SetupIntent
- `initPaymentSheet(params)` — initialize PaymentSheet
- `presentPaymentSheet()` — show PaymentSheet UI
- `handleNextAction(clientSecret)` — handle 3DS or other next actions
- `collectBankAccountForPayment/Setup` — ACH bank account collection
- `verifyMicrodepositsForPayment/Setup` — microdeposit verification
- `createRadarSession()` — Fraud signals
- `canAddCardToWallet(params)` — check wallet eligibility

## Important limitation

**In-app purchases** (subscriptions, in-game currency, premium content, app unlocking): must use Apple App Store / Google Play in-app purchase APIs, not this SDK. Stripe SDK for all other payment scenarios.

## Migration notes

- **v0.29.0**: removed legacy `useApplePay`, `useGooglePay`, `<ApplePayButton>`, `<GooglePayButton>` — use `usePlatformPay` instead.
- **Android SDK 36**: `compileSdkVersion 36`, `targetSdkVersion 36`, `minSdkVersion 23` now required.

## Related pages

- [[stripe-react-native-sdk]] — concept page
- [[stripe]] — company page
- [[stripe-node-sdk]] — Node.js SDK (server-side counterpart)

## Raw Sources

- [[github-stripe-react-native]] — stub file with key file index
