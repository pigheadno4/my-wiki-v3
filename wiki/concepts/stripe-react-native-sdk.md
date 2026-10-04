---
title: "Stripe React Native SDK"
type: concept
category: framework
tags: [stripe, react-native, mobile, sdk, payments, apple-pay, google-pay, payment-sheet, ios, android]
---

## Overview

`@stripe/stripe-react-native` is Stripe's official React Native SDK for building native payment UIs on iOS and Android. It wraps Stripe's native iOS/Android SDKs, provides PCI-compliant card collection (data goes directly to Stripe, not your server), automatic 3DS/SCA handling, and prebuilt UI components including PaymentSheet.

Latest ingested version: **0.80.0**. The cumulative history preserves the legacy `0.65.1` manual capsule and the approved `0.72.0` full baseline.

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

Starting in `0.74.0`, iOS Apple Pay params accept `supportedNetworks` to restrict the networks shown for one payment. This differs from `additionalEnabledNetworks`: the restriction replaces the request's default network set, including additional networks.

```tsx
await confirmPlatformPayPayment(clientSecret, {
  applePay: {
    merchantCountryCode: 'US',
    currencyCode: 'USD',
    supportedNetworks: ['Visa', 'MasterCard'],
    cartItems,
  },
});
```

The values are passed as Apple `PKPaymentNetwork` raw values. Invalid strings are dropped by the retained native mapper, so applications should use Apple-documented network names and test the resulting sheet on iOS.

## Connect implementation boundary

The `0.74.0` snapshot contains an experimental `ConnectNotificationBanner` implementation that reports total and action-required notification counts, sizes itself to its web content, and can open full-screen requirement tasks. It is marked `@experimental` and is not exported by the retained package root or `connect/Components` barrel, so it is implementation evidence rather than a supported root-package integration surface.

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

### 0.80.0 Pre-Collected Consent and Inline Checkout

Financial Connections adds private-preview `preCollectedConsent: { consent, collectedAt }` to session/account collection, bank-account token collection and Intent bank collection. `consent` is the server-created Consent object's ID; `collectedAt` is Unix seconds captured when the buyer affirmatively accepts the complete Stripe-issued consent text, not when the sheet is launched. Reuse that acceptance timestamp on retries. Stripe may still display its own consent pane. Both native bridges map the object and reject missing/empty ID or nonnumeric timestamp fields, but these basic checks do not establish freshness, authenticity, finite/integer correctness or authorization. Native conversion truncates to an integer.

The sample obtains issued text/locale/expiry from a backend, renders it for acceptance, checks expiry and launches token/session collection with the matching merchant key/session. Its account-specific preview configuration is demo-only: **never embed a secret key in a production mobile app**, even though the sample provides a custom-secret configuration path. Backend Consent API details require separately collected server evidence. This feature is not generally available merely because it is typed.

`CheckoutPaymentElementView` now resolves an SDK-owned element through a WeakMap and renders a measured native component rather than throwing. It starts at height 1 and animates height updates. iOS hosts the owned UIKit element and requires one mount; Android hosts Compose, reuses an Activity-scoped presenter and detaches on controller destruction. This is source-level inline rendering support, not device-tested checkout: modal `paymentElement.present` and `confirm` still throw. The 0.79 hook/server-update implementation and earlier platform-specific mutation limits remain. Native pins stay Android `23.21.0`/iOS `26.12.1`. See [[source-github-stripe-react-native]] and [[changelog-github-stripe-react-native]].

### 0.79.0 Reactive Checkout and Server Updates

`useCheckout` now creates/observes a native controller and destroys it on disable, reload and unmount. Changing `getConfiguration` alone does not reload; explicit `reload()` uses its latest function. Generation checks ignore stale asynchronous completions and destroy late-created controllers. Initialization failures appear in hook error state; callers of explicit reload still receive rejection.

`runServerUpdate(async () => { /* update this Checkout Session on your backend */ })` now waits for a native request identified by controller+operation ID, invokes the merchant callback once, then reports success/error to native before completing. The native SDK owns its session-update operation; the wrapper does not establish network idempotency, retry guarantees or a callback timeout. iOS destruction cancels pending continuations; Android cancels the owning coroutine scope. `paymentElement.present`, `confirm` and the embedded view still remain unimplemented, and the previous platform mutation limits remain. This is partial private-preview functionality, not a complete payment UI.

Connect loading indicators now use appearance `colorBackground`/`colorText`, defaulting to white/black. Native pins advance Android `23.21.0`, iOS `26.12.1`; the SPM embed helper exits if TARGET_BUILD_DIR is missing (patch-only evidence). Source: [[source-github-stripe-react-native]]; chronological detail: [[changelog-github-stripe-react-native]].

### 0.78.0 SPM Migration and Partial Checkout Bridge

On React Native >=0.75, native Stripe iOS dependency resolution defaults to Swift Package Manager; the React Native wrapper remains a CocoaPods development pod, so `pod install` is still required. Configure `use_frameworks! :linkage => :dynamic`; Expo uses `expo-build-properties` with `ios.useFrameworks: 'dynamic'`. Keep `react_native_post_install` and verify the app's `[stripe-react-native] Embed SPM Frameworks` phase. The helper pins the native version exactly, conditionally links Onramp, embeds/signs only dynamic Stripe frameworks and checks project integrity. It is preserved as complete added-file patch evidence, not a retained standalone file.

React Native <0.75 is deprecated, not yet rejected by this release's SPM selector: it falls back to CocoaPods. Temporary opt-out is `$StripeDisableSPM = true`, or this SDK's Expo plugin `disableSPM: true`; fallback is deprecated. The README directs Identity SDK co-users to opt out until Identity supports SPM. Native pins become Android `23.20.0` and iOS `26.12.0`.

`createCheckout` now bridges native creation, session observation, shipping updates, promotion-code apply/remove, payment-option clearing and destruction. This is **partial private-preview implementation**, not a working complete payment flow: `paymentElement.present`, `runServerUpdate` and `confirm` remain unimplemented; `useCheckout` and `CheckoutPaymentElementView` remain unchanged stubs. Android email updates delegate natively, whereas iOS explicitly rejects them; Android rejects clearing shipping with a null address. IDs are now JS-generated and events filtered by controller ID; the 0.76/0.77 sequence buffer is removed. Session schema moves amount details to individual items and adds `adjustableQuantity.enabled`; removed preview fields should not be relied upon.

Financial Connections adds `no_eligible_accounts` and Android-only `web_browser_unavailable` event codes; Android serializes the native enum's string value. Source inspection does not prove preview access or successful native builds/payments. See [[source-github-stripe-react-native]] and [[changelog-github-stripe-react-native]].

### 0.77.0 New Architecture Boundary

React Native TurboModules/Fabric are required: Android `newArchEnabled=true`, iOS `RCT_NEW_ARCH_ENABLED=1`, Expo `newArchEnabled: true`. Android build configuration throws when disabled; the podspec rejects explicit `0` and unconditionally includes the new-architecture subspec. Removed iOS old-architecture view managers do not remove the corresponding Fabric payment components. The remaining event-emitter compatibility layer supports new-architecture RN below 0.80, not old architecture.

Android Google Pay payment-method/token creation uses Activity Result registration and re-registration after Activity recreation; overlapping requests return an error. PaymentSheet result delivery waits for an available Activity. Test rotation/backgrounding, cancellation and concurrent taps; source inspection is not device verification.

New Checkout configuration mappers remain scaffolding: the public APIs are still the 0.76.0 unimplemented stubs. Android billing collection belongs to the Checkout Session; the configuration field is iOS-only, and the retained iOS mapper currently maps its address setting only. Several Android fields have TODO setters; do not infer declaration-to-runtime parity. Internal Connect auth-challenge props are deliberately omitted from public types; Financial Connections cancellation produces a null result, missing successful sessions produce an error, and cleanup is idempotent. Native pins: Android `23.19.0`, iOS `26.11.0`. Source: [[source-github-stripe-react-native]].

### 0.76.0 Checkout private-preview replacement

> [!warning] Contradiction
> Earlier cumulative wording listed Checkout mutations and CurrencySelectorElement alongside usable payment APIs. The retained 0.75.0 native bridge already rejected Checkout as temporarily unavailable and rendered currency-selector placeholders at zero height. Those historical declarations are not proof of a working flow. In 0.76.0 the old bridge, currency selector, PaymentSheet Checkout setup type and Embedded Payment Element Checkout overload are removed. Ordinary Intent-based PaymentSheet/Embedded Payment Element remain separate.

The package root now exports `useCheckout`, `createCheckout` and `CheckoutPaymentElementView`, with new private-preview `CheckoutController` types. These are explicitly unimplemented at the 0.76.0 SHA: enabled `useCheckout` returns `error`, disabled returns `idle`, session/element stay null, all hook operations reject, and controller creation/view rendering throw. The new `getConfiguration` contract does not execute in this stub. Do not recommend these as a usable frontend Checkout integration. Native registries and ordered event buffering are scaffolding only. See [[source-github-stripe-react-native]] and [[changelog-github-stripe-react-native]].

0.76.0 also adds authenticated Onramp wallet deletion by wallet ID; see [[stripe-crypto-onramp]]. Native pins become Stripe Android `23.17.1` and Stripe iOS `26.9.0`.

- **v0.29.0**: `useApplePay`, `useGooglePay`, `<ApplePayButton>`, `<GooglePayButton>` removed → use `usePlatformPay` / `<PlatformPayButton>`
- **Android SDK 36**: `compileSdkVersion 36`, `targetSdkVersion 36`, `minSdkVersion 23` required
- **v0.72.0 private-preview Link Controller**: `presentLinkController` selects a payment method but no longer confirms a SetupIntent; call `confirmLinkControllerSetupIntent` explicitly afterward
- **v0.73.0 private-preview Link Controller**: `LinkController.Configuration` adds `billingDetailsCollectionConfiguration` and `appearance`; appearance covers light/dark colors, style, primary-button sizing, and preview-only reduced Link branding
- **v0.73.0 deferred intents on iOS**: PaymentSheet and Embedded Payment Element now read `captureMethod` from `intentConfiguration.mode`, matching the documented nested configuration shape
- **v0.73.0 native wrappers**: delegates to Stripe iOS `26.5.0` and Stripe Android `23.14.0`; Crypto Onramp adds the `tempo` network enum value
- **v0.74.0 Apple Pay**: adds iOS `supportedNetworks` to restrict the card networks offered in the Apple Pay sheet; it overrides defaults and `additionalEnabledNetworks` for that request
- **v0.74.0 native wrappers**: delegates to Stripe iOS `26.6.0` and Stripe Android `23.15.0`; the retained SHA also contains experimental, non-root-exported Connect notification-banner implementation work

- **v0.75.0 Crypto Onramp**: adds Android Samsung Pay configuration, `isSamsungPaySupported()`, and `collectPaymentMethod('SamsungPay', { samsungPay: ... })`. The app must supply Samsung Pay SDK `2.22.00` and a service ID. This does not establish ordinary PaymentSheet Samsung Pay support. See [[stripe-crypto-onramp]].
- **v0.75.0 errors and native wrappers**: adds five wallet-verification `onrampErrorType` variants and advances Stripe Android to `23.16.0` and Stripe iOS to `26.7.0`; retain generic-error fallback handling.

## Evidence boundaries

- The React Native package delegates runtime payment behavior to Stripe's native iOS and Android SDKs.
- Exported APIs do not prove merchant eligibility, preview access, payment-method activation, or country/currency availability.
- Mobile apps still need a backend to create Intents, Customer Sessions, Checkout Sessions, Connect sessions, and other client-secret-bearing objects.

## Sources

- [[source-github-stripe-react-native]] — cumulative GitHub source through v0.80.0; historical baselines and version-qualified implementation boundaries preserved
- [[changelog-github-stripe-react-native]] — package-qualified release history and migration impact
