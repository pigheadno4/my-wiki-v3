---
title: "Stripe React Native SDK"
type: concept
category: framework
tags: [stripe, react-native, mobile, sdk, payments, apple-pay, google-pay, payment-sheet, ios, android]
---

## Overview

`@stripe/stripe-react-native` is Stripe's official React Native SDK for building native payment UIs on iOS and Android. It wraps Stripe's native iOS/Android SDKs, provides PCI-compliant card collection (data goes directly to Stripe, not your server), automatic 3DS/SCA handling, and prebuilt UI components including PaymentSheet.

Latest ingested version: **0.84.0**. The cumulative history preserves the legacy `0.65.1` manual capsule and the approved `0.72.0` full baseline.

## Platform requirements

At `0.84.0`, React Native >=0.75 and the new architecture are required. Native Stripe iOS dependency resolution must use SPM with dynamic frameworks; remove the old `disableSPM: true` / `$StripeDisableSPM = true` opt-outs, which now error. The React Native wrapper remains a development pod, so `pod install` and `react_native_post_install` are still needed. Expo precompiled-module users additionally need Expo >=58.0.19 according to this release's migration guide; this is not a blanket minimum for every Expo app. Native pins: Android 23.25.1 / iOS 26.15.1. Historical fallback guidance below applies only to older versions.

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

### 0.84.0 Mandatory SPM and Internal Checkout Boundary

The package root stops exporting `useCheckout`, `createCheckout`, `CheckoutPaymentElementView` and `CheckoutCurrencySelectorElementView`; the types barrel also stops exporting Checkout types. Their files remain marked `@internal` private preview. Do not apply the older root-import examples unchanged or recommend deep internal imports as a supported migration. Ordinary Intent-based PaymentSheet is not removed.

Internal preview changes include shipping-form/button appearance mapping and iOS `applePay.display: 'never'`, which returns no Apple Pay configuration before checking merchant ID. Omitted/automatic display still requires that ID when Apple Pay configuration is supplied. The mandate-text default comment changes to true, but both wrappers still set it only when supplied; the comment alone does not date a native behavior change.

Android PaymentSheet and custom FlowController rebuild when the registered callback kind changes between direct secret, deferred PaymentMethod and ConfirmationToken modes. This fixes stale registration in the inspected code, not proven concurrency safety. Connect Android external navigation now follows configured browser presentation regardless of navigation type, and CSV detection recognizes Stripe's S3 export host. The broader pathname heuristic remains, so this is not a strict host-allowlist change. See [[source-github-stripe-react-native]] and [[changelog-github-stripe-react-native]] for exact-SHA evidence and the separately collected SPM helper. All previous release knowledge remains below.

### 0.83.0 Shipping Element and Checkout Type Migration

Private-preview Checkout adds optional `shippingAddressElement: {}` configuration, with title/button-title overrides, and a nullable controller/hook handle. Its `present()` requests native presentation and resolves immediately, not after dismissal or address selection. Observe the session's shipping address separately. Android requires a resumed Activity and registers shipping results when recreating its shared presenter; iOS retains the configured element and requires a visible presenter. These bridge paths do not prove backend acceptance, preview access or payment success.

Checkout types move under `Checkout.PaymentElementConfiguration` and `Checkout.CurrencySelectorElementConfiguration` namespaces. Checkout-only billing collection configuration and Apple Pay `merchantCountryCode` are removed; ordinary PaymentSheet/Platform Pay configuration remains separate. Payment-option serializers now forward optional `sublabel`; Android selector colors honor explicit light/dark style and reports updating before potentially slow icon serialization. None proves automatic theme refresh or universal lifecycle recovery.

AddressSheet deprecates Android `googlePlacesApiKey` but retains/forwards the prop; keyless autocomplete is announced, with native address-launcher internals outside this capsule. Connect initialization double-stringifies configuration and installs a read-only injected JSON accessor to handle quotes, backslashes and backticks; this is not a general security-hardening guarantee. PlatformPayButton now documents an explicit height; its rendering implementation is unchanged. README adds iOS host-localization guidance.

Native pins advance to Android `23.24.0`/iOS `26.15.0`, not iOS 26.15.1. Android preferred networks are set only when supplied across PaymentSheet, Embedded and CustomerSheet, preserving native defaults rather than synthesizing them. Older history remains in [[source-github-stripe-react-native]] and [[changelog-github-stripe-react-native]]. No SDK/device/payment testing.

### 0.82.0 Currency Selector and Preview Compatibility

Private-preview Checkout adds `CheckoutCurrencySelectorElementView` and a nullable controller/hook `currencySelectorElement`. Supply `currencySelectorElement: {}` in creation configuration to enable it when Adaptive Pricing is available; render only the SDK-owned non-null element. The wrapper derives availability during controller creation, not a universal merchant capability. React follows native height; iOS permits one mount and detaches on removal/destruction, while Android uses an Activity-scoped presenter. This is distinct from the removed pre-0.76 placeholder.

`CheckoutPaymentElementView` no longer accepts/forwards ordinary ViewProps or caller style: place layout/accessibility wrappers outside it. Checkout-specific `GooglePayConfiguration.testEnv` and `savePaymentMethodOptInBehavior`/its type are removed; ordinary PaymentSheet and Platform Pay test-environment options are separate. iOS previously mapped save opt-in; Android's old declarations had deferred setters, not demonstrated parity. Android now maps Checkout default phone, font, shapes and embedded-row appearance. Theme-aware Android payment-option icons use `loadIcon(isSystemDarkTheme)` with the existing timeout/fallback.

The iOS bridge now calls `updateEmail(email)` and Android forwards nullable shipping addresses, closing the two earlier bridge limitations. Native pins advance to Android `23.23.0`/iOS `26.14.0`, not the later independently ingested native releases. Android lifecycle callbacks are registered through the Application and unregistered on module invalidation, addressing the announced JS-reload/Activity-recreation issue. Font validation accepts underscores; Gradle excludes the private TapAndPay transitive dependency for optional compile-only provisioning, while the R8 warning suppression is comparison-hunk evidence only. No native build, device or payment test establishes recovery in every lifecycle case.

Onramp adds optional `countryHint`, contact-prefill fields `email`/`phone`/`rawPhone`, and Samsung `collectContactInformation`; see [[stripe-crypto-onramp]]. Contact prefill is not KYC submission, and rawPhone is not registration-ready E.164. The later raw changelog attributes the contact additions to 0.81.0, but the retained bridge comparison observes them in 0.81.0 -> 0.82.0. Preserve that distinction and all older behavior in [[source-github-stripe-react-native]] and [[changelog-github-stripe-react-native]].

### 0.81.0 Checkout and Lifecycle Bridges

Private-preview Checkout now bridges `paymentElement.present()` and `confirm()` on both platforms instead of throwing the earlier not-implemented error. Presentation resolves after requesting the sheet, not after dismissal or selection. Observe the controller/hook session for the selection; confirm only the selected payment option while ready. Confirmation preserves completed/canceled/failed outcomes and paid/unpaid/noPaymentRequired status. Bridge invocation errors reject separately. Completion is not proof of paid funds; fulfill from authoritative server state/events.

Android requires a resumed, non-finishing ComponentActivity; iOS requires a visible, non-dismissing presenter. Per-controller overlapping confirmations are rejected. Destruction cancels pending bridge work; no wrapper timeout, backend idempotency or process-restoration guarantee is established. Android's completed-result serializer requires a complete native session or rejects. Android inline layout adds child remeasurement and height-event/prop wiring. iOS email updates and Android null shipping-address clearing remain unsupported.

> [!warning] Contradiction
> The version-qualified 0.80.0 record below correctly says modal presentation/confirmation still throw. At 0.81.0 those stubs are replaced by native bridge calls. Preserve the old record but do not apply its unsupported-call conclusion to this release. This is source-level private-preview support, not general availability or device-tested payment.

CustomerSession credentials gain request-ID correlation, provider-error responses and cancellation/invalidation on sheet replacement or module teardown. The public provider still returns customerId/clientSecret; the SDK adds the request ID internally. SetupIntent-secret callbacks retain their older single-slot handling, and a provider that never settles has no demonstrated request timeout. IDs are correlation, not customer authorization or comprehensive tenant isolation.

Android PaymentSheet configuration invalidates cached sheet/controller objects when the host Activity changes; presentation/results use a host-owned PromiseViewModel. It stores one mutable Promise and does not clear it on resolve, so do not infer per-instance/concurrent-call isolation or exactly-once delivery. Reconfigure for the current host and test recreation/navigation; this is not an automatic recovery guarantee for every presentation path.

ConfirmationToken.setupFutureUsage on Android maps to OnSession/OffSession/None instead of API snake-case values; Blank/absent maps to null. FinancialConnectionsEvent requires financialConnectionsSessionId in TypeScript, forwarded by both native mappers; update typed fixtures. Notes announce emission once the ID exists, but the wrapper does not independently enforce native event timing. Android DisplayPixDetails is explicitly unhandled by the generic next-action mapper (returns null); the enum does not create a direct JS Pix integration recipe.

Native pins advance to Android 23.22.0/iOS 26.13.0, not Android 23.23.0. New-architecture/SPM requirements remain. Additive full ingest with focused reading preserves older knowledge; native SDK internals, changed unretained examples and tests remain outside full-file evidence. See [[source-github-stripe-react-native]], [[changelog-github-stripe-react-native]] and [[stripe-checkout]]. No native build/device/payment tests.

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

- [[source-github-stripe-react-native]] — cumulative GitHub source through v0.82.0; private-preview currency selector, compatibility/mutation changes and Onramp prefill; older knowledge preserved
- [[changelog-github-stripe-react-native]] — package-qualified release history and migration impact
