---
title: "GitHub: stripe/stripe-react-native"
type: source
date_ingested: 2026-05-13
date_updated: 2026-07-30
original_format: github-repo
raw_files:
  - "github/stripe/stripe-react-native/snapshots/2026-07-30-e752a71/manifest.json"
  - "github-stripe-react-native.md"
tags: [stripe, react-native, mobile, sdk, payments, payment-sheet, embedded-payment-element, connect, link, crypto-onramp, apple-pay, google-pay, github-repository]
---

## Overview

`stripe/stripe-react-native` publishes `@stripe/stripe-react-native`, Stripe's official React Native bridge to its native iOS and Android payment SDKs. This cumulative page preserves the legacy `0.65.1` manual capsule and adds the approved `@stripe/stripe-react-native@0.72.0` full baseline at commit `e752a71aec30a0ed88e605345cff3ad74053b623`.

Repository: <https://github.com/stripe/stripe-react-native>

## Evidence Boundary

- The `0.72.0` capsule retains 250 public, production, configuration, example, and story files. Tests and fixtures are excluded by policy; stories are retained as useful integration evidence.
- The TypeScript API delegates payment behavior to native Stripe iOS and Android SDKs through React Native bridges. An exported type or component does not independently prove merchant eligibility, payment-method availability, preview access, or native-runtime behavior.
- The collector first retained `0.72.0`. The older `0.65.1` evidence is a 14-file manual capsule, so this page preserves its findings without claiming an automated, exhaustive `0.65.1--0.72.0` diff.
- The package's current peer ranges are broad (`expo >=46.0.9`; React, React Native, and React Native WebView `*`). Applications still need to follow the platform and Expo compatibility requirements documented for their selected release.
- `useLinkController` is explicitly private preview. Its public source surface is evidence of an available SDK contract, not general production access.

## Grounding Excerpts

> "The Stripe React Native SDK allows you to build delightful payment experiences in your native Android and iOS apps using React Native."
>
> `raw/github/stripe/stripe-react-native/snapshots/2026-07-30-e752a71/files/README.md:1-6`

> "This means the sensitive data is sent directly to Stripe instead of passing through your server."
>
> `raw/github/stripe/stripe-react-native/snapshots/2026-07-30-e752a71/files/README.md:14-16`

> "If you're selling digital products or services within your app ... you must use the app store's in-app purchase APIs."
>
> `raw/github/stripe/stripe-react-native/snapshots/2026-07-30-e752a71/files/README.md:31-33`

> "This API is in private preview and may change without notice."
>
> `raw/github/stripe/stripe-react-native/snapshots/2026-07-30-e752a71/files/src/hooks/useLinkController.tsx:9-17`

> "SetupIntent confirmation is now a separate step."
>
> `raw/github/stripe/stripe-react-native/releases/stripe-react-native/0.72.0/2026-07-30/release-notes.md:1-4`

## Package Status

| Package | Latest ingested release | Exact SHA | Evidence status |
| --- | --- | --- | --- |
| `@stripe/stripe-react-native` | `0.72.0` | `e752a71aec30a0ed88e605345cff3ad74053b623` | Approved full baseline; legacy `0.65.1` retained |

This table reports wiki ingest progress, not the latest version published upstream.

## Architecture and Package Shape

The package exposes CommonJS, ES module, and TypeScript declaration outputs from generated `lib/` paths. The retained source establishes three implementation layers:

1. `src/` owns the public TypeScript hooks, components, functions, types, code-generated native specifications, and Connect wrappers.
2. `android/src/main/` implements the Kotlin bridge over Stripe Android SDK `23.13.1`.
3. `ios/` implements the Swift and Objective-C bridge over Stripe iOS SDK `26.4.1`, including old- and new-architecture component views.

The Android and iOS modules map native result objects and errors back into stable React Native return shapes. Native implementation remains authoritative when TypeScript declarations and platform behavior diverge.

## Core Payment Surfaces

### PaymentSheet and Embedded Payment Element

PaymentSheet is the primary prebuilt checkout UI. It supports cards, Apple Pay, Google Pay, saved payment methods, local methods, and automatic native 3DS handling. The API supports PaymentIntent, SetupIntent, and deferred-intent initialization, followed by presentation or explicit confirmation.

`EmbeddedPaymentElement` provides an embeddable payment-method UI with update, confirm, and height/state events rather than a modal sheet. Its native implementations and retained story cover configuration updates and merchant-owned layout.

`CustomerSheet` manages saved payment methods. Its adapter and CustomerSession-provider bridges show that customer data retrieval and mutation cross the JavaScript/native boundary and require the corresponding server-created customer credentials.

### Direct Intent and Bank APIs

The imperative and hook surfaces include:

- `confirmPayment`, `confirmSetupIntent`, and `handleNextAction`;
- PaymentMethod and Token creation;
- Financial Connections collection for PaymentIntents and SetupIntents;
- microdeposit verification;
- `createRadarSession`;
- card-wallet eligibility and push-provisioning operations; and
- Checkout Session state and line-item/shipping updates through `useCheckout`.

These client APIs consume client secrets and ephemeral configuration created by a merchant backend. They do not replace server-side Intent, CustomerSession, Checkout Session, or Connect-session creation.

### Platform Pay

`usePlatformPay()` and `PlatformPayButton` provide the unified Apple Pay and Google Pay surface. The legacy platform-specific hooks and buttons were removed in `0.29.0`. Expo applications must configure `merchantIdentifier` for Apple Pay and `enableGooglePay` as needed.

Wallet support remains platform- and configuration-dependent. A wallet API export is not proof that a specific payment method, country, currency, or merchant account is enabled.

### Link Controller

`useLinkController` is a private-preview standalone Link flow with shared loading state:

1. call `initLinkController`;
2. call `presentLinkController` for payment-method selection; and
3. for a SetupIntent, call `confirmLinkControllerSetupIntent` explicitly after successful presentation.

Release `0.72.0` deliberately separates selection from SetupIntent confirmation. Code written against the earlier auto-confirm behavior must add the explicit third step.

### Connect Embedded Components

The root entrypoint exports `ConnectComponentsProvider`, `loadConnectAndInitialize`, Connect instance/update types, and embedded components. The retained native code and example establish Account Onboarding support; the accumulated changelog also records Payments and Payouts component availability by `0.69.0`.

Connect integrations require an Account Session or equivalent server-created client secret. The component exports do not establish connected-account eligibility or enabled features.

### Crypto Onramp

`useOnramp()` coordinates Link authentication, wallet registration and ownership verification, KYC and compliance identifiers, payment-method collection, crypto payment-token creation, and checkout. Collection can use card, bank account, or Platform Pay according to the selected method and platform parameters.

The `0.66.0--0.70.0` history adds EU compliance identifiers, typed errors, wallet-ownership challenge APIs, and Arbitrum. These are specialized onramp contracts and should not be inferred from ordinary PaymentSheet support.

## Components and Hooks

The root package exports these principal hooks:

| Hook | Responsibility |
| --- | --- |
| `useStripe()` | Memoized access to the broad imperative SDK surface |
| `usePaymentSheet()` | Initialize, present, and confirm PaymentSheet |
| `usePlatformPay()` | Apple Pay and Google Pay support, confirmation, payment-method creation, updates, and dismissal |
| `useConfirmPayment()` / `useConfirmSetupIntent()` | Intent confirmation |
| `useFinancialConnectionsSheet()` | Bank-account collection |
| `useOnramp()` | Crypto onramp coordinator |
| `useLinkController()` | Private-preview standalone Link selection and SetupIntent confirmation |

Principal components include `StripeProvider`, `CardField`, `CardForm`, `AuBECSDebitForm`, `PlatformPayButton`, `AddressSheet`, `CustomerSheet`, `EmbeddedPaymentElement`, `PaymentMethodMessagingElement`, `CurrencySelectorElement`, `AddToWalletButton`, `StripeContainer`, and Connect embedded components.

## Platform requirements

| Platform | Minimum |
| --- | --- |
| Android | API 23, `compileSdkVersion` 36, `targetSdkVersion` 36, Kotlin 2.x |
| iOS | iOS 13 or later for current releases |
| Expo | Use `expo install @stripe/stripe-react-native`; each Expo SDK pins a compatible package version |

If an Android app cannot move to SDK 36, the migration guide directs it to pin a package release based on Stripe Android SDK 22.x or earlier. `CardForm` additionally requires a Material Components theme.

## Initialization

```tsx
<StripeProvider publishableKey="pk_..." merchantIdentifier="merchant.com.app">
  {children}
</StripeProvider>

await initStripe({ publishableKey: 'pk_...', merchantIdentifier: 'merchant.com.app' })
```

## Important limitation

For digital goods and services sold inside the app, including subscriptions, in-game currency, premium content, and app unlocking, the repository directs developers to Apple or Google in-app purchase APIs. This Stripe SDK is for scenarios allowed under the applicable app-store rules.

## Version History

### `@stripe/stripe-react-native@0.72.0`

The exact release updates Stripe iOS from `26.3.0` to `26.4.1`, Stripe Android from `23.12.0` to `23.13.1`, and changes private-preview Link Controller SetupIntent handling from automatic confirmation during presentation to an explicit post-selection confirmation call.

The full baseline also establishes the broader current package architecture and API surface. Those baseline findings must not be attributed solely to the `0.72.0` patch note.

### Accumulated `0.66.0--0.71.0` Milestones

- `0.66.0--0.70.0`: expanded crypto onramp compliance, typed errors, wallet ownership, network support, and payment collection.
- `0.68.0`: changed push-provisioning contracts and added wearable-related support.
- `0.69.0`: recorded Connect Account Onboarding, Payments, and Payouts embedded components as generally available, while standalone Link Controller remained private preview.
- `0.71.0`: added Pay by Bank to direct PaymentIntent and SetupIntent confirmation.

These milestones are synthesized from the retained cumulative changelog. They are not an automated file-by-file comparison against the old manual capsule.

### Legacy `@stripe/stripe-react-native@0.65.1`

The May 2026 manual capsule established PaymentSheet, Platform Pay, CardField/CardForm, AddressSheet, CustomerSheet, Payment Method Messaging, Financial Connections, Radar, Connect, crypto onramp, the app-store purchase boundary, and the Android SDK 36 migration requirement. The `0.72.0` ingest adds to this history rather than replacing it.

## Integration Guidance

- Prefer PaymentSheet for a maintained prebuilt checkout and Embedded Payment Element when the payment-method UI must live inside a merchant-owned layout.
- Keep Intent and session creation on the backend; pass only publishable configuration and client secrets to the mobile app.
- Use `usePlatformPay` rather than removed Apple Pay and Google Pay hooks.
- Treat Link Controller as private preview and implement the explicit `confirmLinkControllerSetupIntent` step for `0.72.0`.
- Verify Expo, React Native, native SDK, Android SDK, and iOS deployment compatibility before upgrading.
- Re-test both platforms when the React Native package changes because a patch can update delegated native SDKs without changing the JavaScript integration shape.
- Confirm app-store payment policy for digital goods before choosing Stripe mobile payment APIs.

## Related

- Company: [[stripe]]
- Concept: [[stripe-react-native-sdk]]
- Native dependencies: [[source-github-stripe-ios]], [[source-github-stripe-android]]
- Server-side counterpart: [[stripe-node-sdk]]
- History: [[changelog-github-stripe-react-native]]

## Raw Sources

- `raw/github/stripe/stripe-react-native/snapshots/2026-07-30-e752a71/manifest.json` — exact-SHA `0.72.0` source capsule
- `raw/github/stripe/stripe-react-native/releases/stripe-react-native/0.72.0/2026-07-30/manifest.json` — package-qualified release record
- `raw/github/stripe/stripe-react-native/releases/stripe-react-native/0.72.0/2026-07-30/release-notes.md` — exact upstream release note
- `raw/github/stripe/stripe-react-native/snapshots/2026-07-30-e752a71/files/README.md` — purpose, capabilities, installation, platform requirements, and app-store boundary
- `raw/github/stripe/stripe-react-native/snapshots/2026-07-30-e752a71/files/package.json` — package entrypoints, version, and peer ranges
- `raw/github/stripe/stripe-react-native/snapshots/2026-07-30-e752a71/files/src/index.tsx` — public TypeScript exports
- `raw/github/stripe/stripe-react-native/snapshots/2026-07-30-e752a71/files/src/functions.ts` — imperative bridge API
- `raw/github/stripe/stripe-react-native/snapshots/2026-07-30-e752a71/files/src/hooks/useLinkController.tsx` — private-preview Link workflow
- `raw/github/stripe/stripe-react-native/snapshots/2026-07-30-e752a71/files/src/hooks/useOnramp.tsx` — crypto onramp coordinator
- `raw/github/stripe/stripe-react-native/snapshots/2026-07-30-e752a71/files/android/src/main/java/com/reactnativestripesdk/StripeSdkModule.kt` — Android native bridge
- `raw/github/stripe/stripe-react-native/snapshots/2026-07-30-e752a71/files/ios/StripeSdkImpl.swift` — iOS native bridge
- `raw/github/stripe/stripe-react-native/snapshots/2026-07-30-e752a71/files/CHANGELOG.md` — cumulative upstream package history
- `raw/github-stripe-react-native.md` — legacy `0.65.1` manual capsule pointer
