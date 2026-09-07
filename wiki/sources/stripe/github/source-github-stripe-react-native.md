---
title: "GitHub: stripe/stripe-react-native"
type: source
date_ingested: 2026-05-13
date_updated: 2026-09-05
original_format: github-repo
raw_files:
  - "github/stripe/stripe-react-native/snapshots/2026-09-01-e0a845f/manifest.json"
  - "github/stripe/stripe-react-native/snapshots/2026-09-01-a628bc0/manifest.json"
  - "github/stripe/stripe-react-native/snapshots/2026-09-01-8b1bc13/manifest.json"
  - "github/stripe/stripe-react-native/snapshots/2026-07-30-e752a71/manifest.json"
  - "github-stripe-react-native.md"
tags: [stripe, react-native, mobile, sdk, payments, payment-sheet, embedded-payment-element, connect, link, crypto-onramp, apple-pay, google-pay, github-repository]
---

## Overview

`stripe/stripe-react-native` publishes `@stripe/stripe-react-native`, Stripe's official React Native bridge to its native iOS and Android payment SDKs. This cumulative page preserves the legacy `0.65.1` manual capsule, the approved `0.72.0` full baseline, and approved deltas through `0.75.0` at commit `e0a845f40749703480146c9d70721b9007d0516d`.

Repository: <https://github.com/stripe/stripe-react-native>

## Evidence Boundary

- The `0.75.0` capsule retains 252 public, production, configuration, example, and story files. Tests and fixtures are excluded by policy; stories are retained as useful integration evidence. Complete Android Onramp implementation files are outside the capsule; their changed hunks are available in the comparison, which does not replace full-file evidence for a deep runtime query.
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

> "Added `billingDetailsCollectionConfiguration` to `LinkController.Configuration` to control which billing fields are collected in the Link sheet."
>
> `raw/github/stripe/stripe-react-native/releases/stripe-react-native/0.73.0/2026-09-01/release-notes.md:4`

> "Added `appearance` to `LinkController.Configuration` to customize Link UI colors and styling."
>
> `raw/github/stripe/stripe-react-native/releases/stripe-react-native/0.73.0/2026-09-01/release-notes.md:5`

> "Added Tempo network support to Crypto Onramp."
>
> `raw/github/stripe/stripe-react-native/releases/stripe-react-native/0.73.0/2026-09-01/release-notes.md:6`

> "Added `supportedNetworks` to the Apple Pay params, which restricts the card networks offered in the Apple Pay sheet."
>
> `raw/github/stripe/stripe-react-native/releases/stripe-react-native/0.74.0/2026-09-01/release-notes.md:2`

> "Added Crypto Onramp Samsung Pay configuration, availability checks, payment collection, and example integration."
>
> `raw/github/stripe/stripe-react-native/releases/stripe-react-native/0.75.0/2026-09-01/release-notes.md:2`

> "Added typed Crypto Onramp error coverage for wallet ownership verification failures."
>
> `raw/github/stripe/stripe-react-native/releases/stripe-react-native/0.75.0/2026-09-01/release-notes.md:3`

> "The Android application must include Samsung Pay SDK 2.22.00 at runtime."
>
> `raw/github/stripe/stripe-react-native/snapshots/2026-09-01-e0a845f/files/src/types/Onramp.ts:79`

## Package Status

| Package | Latest ingested release | Exact SHA | Evidence status |
| --- | --- | --- | --- |
| `@stripe/stripe-react-native` | `0.75.0` | `e0a845f40749703480146c9d70721b9007d0516d` | Approved deltas over `0.72.0` full baseline; legacy `0.65.1` retained |

This table reports wiki ingest progress, not the latest version published upstream.

## Architecture and Package Shape

The package exposes CommonJS, ES module, and TypeScript declaration outputs from generated `lib/` paths. The retained source establishes three implementation layers:

1. `src/` owns the public TypeScript hooks, components, functions, types, code-generated native specifications, and Connect wrappers.
2. `android/src/main/` implements the Kotlin bridge over Stripe Android SDK `23.16.0`.
3. `ios/` implements the Swift and Objective-C bridge over Stripe iOS SDK `26.7.0`, including old- and new-architecture component views.

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

Release `0.74.0` adds `supportedNetworks` to iOS Apple Pay parameters. Supplying it restricts the request to those `PKPaymentNetwork` raw values and overrides the default set, including `additionalEnabledNetworks`, for that payment. The native bridge drops strings that cannot be mapped, so integrations should use Apple-documented values and verify the rendered sheet on iOS.

### Link Controller

`useLinkController` is a private-preview standalone Link flow with shared loading state:

1. call `initLinkController`;
2. call `presentLinkController` for payment-method selection; and
3. for a SetupIntent, call `confirmLinkControllerSetupIntent` explicitly after successful presentation.

Release `0.72.0` deliberately separates selection from SetupIntent confirmation. Code written against the earlier auto-confirm behavior must add the explicit third step.

Release `0.73.0` adds two private-preview configuration surfaces: `billingDetailsCollectionConfiguration` controls collection modes for name, phone, email, and address, while `appearance` maps light/dark colors, automatic/light/dark style, primary-button corner radius and height, and preview-only reduced Link branding across Android and iOS. These declarations and bridge mappings do not establish private-preview access.

### Connect Embedded Components

The root entrypoint exports `ConnectComponentsProvider`, `loadConnectAndInitialize`, Connect instance/update types, and embedded components. The retained native code and example establish Account Onboarding support; the accumulated changelog also records Payments and Payouts component availability by `0.69.0`.

Connect integrations require an Account Session or equivalent server-created client secret. The component exports do not establish connected-account eligibility or enabled features.

The exact `0.74.0` SHA also contains an experimental Connect notification banner that reports total and action-required notification counts, follows rendered web-content height, opens requirement tasks full-screen, and routes external links through native browser surfaces. It is marked `@experimental` and is not exported from the retained package root or `connect/Components` barrel. This is implementation evidence, not a supported public root-package API or proof of general availability.

### Crypto Onramp

`useOnramp()` coordinates Link authentication, wallet registration and ownership verification, KYC and compliance identifiers, payment-method collection, crypto payment-token creation, and checkout. Collection can use card, bank account, or Platform Pay according to the selected method and platform parameters.

The `0.66.0--0.70.0` history adds EU compliance identifiers, typed errors, wallet-ownership challenge APIs, and Arbitrum. Release `0.73.0` adds `tempo` to the React Native `CryptoNetwork` enum. These are specialized onramp contracts and should not be inferred from ordinary PaymentSheet support or treated as proof of merchant, country, or currency eligibility.

Release `0.75.0` adds Android Samsung Pay to `useOnramp`: supply `samsungPay.serviceId` in configuration, check `isSamsungPaySupported()`, then call `collectPaymentMethod('SamsungPay', { samsungPay: { currencyCode, amount, orderNumber } })`. Optional configuration includes `merchantId`, `merchantName`, and `allowedCardBrands`; omitted/empty brand lists use SDK defaults. Amount is in minor units, and order number is unique per transaction. The app must enable Onramp and include Samsung Pay SDK `2.22.00` itself. The retained iOS availability bridge resolves `false`.

Five new `onrampErrorType` variants distinguish invalid wallet signatures, expired challenges, invalid challenges, missing wallets, and unsupported networks. Their exact names and integration example are in [[stripe-crypto-onramp]]. Generic error handling remains necessary. The wallet-ownership methods themselves predate this release.

Samsung Pay here is an Onramp collection option, not evidence of support in ordinary PaymentSheet. Successful collection still requires crypto payment-token creation and the existing server/session checkout flow. The retained example hardcodes collection amount `100` and session source amount `10.0`; treat it as a flow demonstration and align production amounts with server pricing.

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

### `@stripe/stripe-react-native@0.75.0`

Adds Android Samsung Pay configuration, readiness checks, collection, and example wiring to Crypto Onramp. Adds five wallet-verification error discriminants to TypeScript and iOS mapping (Android mapping changes are visible in the comparison). Native pins advance Android `23.15.0` to `23.16.0` and iOS `26.6.0` to `26.7.0`. Review exhaustive error/payment-display switches and supply Samsung's runtime SDK before enabling the option. No broad checkout architecture replacement is established by this delta.

### `@stripe/stripe-react-native@0.74.0`

This contained delta adds iOS Apple Pay `supportedNetworks`, which restricts the networks offered for a payment request and overrides the default and additionally enabled sets. The native wrappers advance Stripe iOS from `26.5.0` to `26.6.0` and Stripe Android from `23.14.0` to `23.15.0`.

The same exact SHA contains experimental Connect notification-banner and external-link handling. Because the banner is not exported from the retained package root or Connect component barrel, it is recorded as implementation evidence rather than a generally supported integration surface.

### `@stripe/stripe-react-native@0.73.0`

This contained delta updates Stripe iOS from `26.4.1` to `26.5.0` and Stripe Android from `23.13.1` to `23.14.0`. The private-preview Link Controller gains billing-detail collection configuration and cross-platform appearance mapping, and Crypto Onramp exposes the Tempo network.

The retained implementation diff also corrects iOS deferred-intent parsing: PaymentSheet and Embedded Payment Element now read `captureMethod` from the nested `intentConfiguration.mode` object rather than the top-level object. This implementation-backed correction is not listed in the release note, so it is attributed to the exact `0.72.0--0.73.0` comparison rather than generalized beyond the retained bridge code.

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
- On `0.73.0`, pass Link billing collection and appearance under `LinkController.Configuration`; do not assume those private-preview fields are enabled for every account.
- For iOS deferred-intent PaymentSheet or Embedded Payment Element flows, place `captureMethod` inside `intentConfiguration.mode`.
- On `0.74.0`, use Apple-documented `PKPaymentNetwork` raw values in `supportedNetworks` and test the resulting iOS sheet; do not expect `additionalEnabledNetworks` to remain additive when the restriction is supplied.
- Do not build against the retained experimental Connect notification-banner implementation until it is exposed and documented as a supported public API.
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

- `raw/github/stripe/stripe-react-native/snapshots/2026-09-01-e0a845f/manifest.json` — exact-SHA `0.75.0` capsule
- `raw/github/stripe/stripe-react-native/releases/stripe-react-native/0.75.0/2026-09-01/manifest.json` — release identity
- `raw/github/stripe/stripe-react-native/releases/stripe-react-native/0.75.0/2026-09-01/release-notes.md` — release features
- `tracking/github/repos/stripe/stripe-react-native/comparisons/stripe-react-native/0.74.0--0.75.0/comparison.json` — comparison identity
- `tracking/github/repos/stripe/stripe-react-native/comparisons/stripe-react-native/0.74.0--0.75.0/diff.patch` — upstream change hunks including Android setup/bridge changes
- `raw/github/stripe/stripe-react-native/snapshots/2026-09-01-e0a845f/files/src/types/Onramp.ts` — Samsung Pay parameters and typed errors
- `raw/github/stripe/stripe-react-native/snapshots/2026-09-01-e0a845f/files/src/hooks/useOnramp.tsx` — readiness and collection API
- `raw/github/stripe/stripe-react-native/snapshots/2026-09-01-e0a845f/files/ios/OnrampErrors.swift` — error mapping
- `raw/github/stripe/stripe-react-native/snapshots/2026-09-01-e0a845f/files/ios/StripeOnrampSdk.mm` — iOS readiness returns false
- `raw/github/stripe/stripe-react-native/snapshots/2026-09-01-e0a845f/files/example/src/screens/Onramp/CryptoOnrampFlow.tsx` — sample lifecycle and amount boundary

- `raw/github/stripe/stripe-react-native/snapshots/2026-09-01-a628bc0/manifest.json` — exact-SHA `0.74.0` source capsule
- `raw/github/stripe/stripe-react-native/releases/stripe-react-native/0.74.0/2026-09-01/manifest.json` — package-qualified `0.74.0` release record
- `raw/github/stripe/stripe-react-native/releases/stripe-react-native/0.74.0/2026-09-01/release-notes.md` — exact upstream `0.74.0` release note
- `tracking/github/repos/stripe/stripe-react-native/comparisons/stripe-react-native/0.73.0--0.74.0/comparison.json` — exact package comparison manifest
- `tracking/github/repos/stripe/stripe-react-native/comparisons/stripe-react-native/0.73.0--0.74.0/comparison.md` — comparison narrative and evidence disposition
- `tracking/github/repos/stripe/stripe-react-native/comparisons/stripe-react-native/0.73.0--0.74.0/diff.patch` — retained implementation delta
- `raw/github/stripe/stripe-react-native/snapshots/2026-09-01-a628bc0/files/src/types/PlatformPay.ts` — Apple Pay restriction contract
- `raw/github/stripe/stripe-react-native/snapshots/2026-09-01-a628bc0/files/ios/ApplePayUtils.swift` — native payment-network mapping
- `raw/github/stripe/stripe-react-native/snapshots/2026-09-01-a628bc0/files/src/components/NotificationBanner.tsx` — experimental Connect notification banner
- `raw/github/stripe/stripe-react-native/snapshots/2026-09-01-8b1bc13/manifest.json` — exact-SHA `0.73.0` source capsule
- `raw/github/stripe/stripe-react-native/releases/stripe-react-native/0.73.0/2026-09-01/manifest.json` — package-qualified `0.73.0` release record
- `raw/github/stripe/stripe-react-native/releases/stripe-react-native/0.73.0/2026-09-01/release-notes.md` — exact upstream `0.73.0` release note
- `tracking/github/repos/stripe/stripe-react-native/comparisons/stripe-react-native/0.72.0--0.73.0/comparison.json` — exact package comparison manifest
- `tracking/github/repos/stripe/stripe-react-native/comparisons/stripe-react-native/0.72.0--0.73.0/diff.patch` — retained implementation delta
- `raw/github/stripe/stripe-react-native/snapshots/2026-09-01-8b1bc13/files/src/types/LinkController.ts` — private-preview Link configuration contract
- `raw/github/stripe/stripe-react-native/snapshots/2026-09-01-8b1bc13/files/src/types/LinkAppearance.ts` — Link appearance type contract
- `raw/github/stripe/stripe-react-native/snapshots/2026-09-01-8b1bc13/files/src/types/Onramp.ts` — Crypto Onramp network contract including Tempo
- `raw/github/stripe/stripe-react-native/snapshots/2026-09-01-8b1bc13/files/ios/StripeSdkImpl+PaymentSheet.swift` — iOS PaymentSheet configuration bridge
- `raw/github/stripe/stripe-react-native/snapshots/2026-09-01-8b1bc13/files/ios/StripeSdkImpl+Embedded.swift` — iOS Embedded Payment Element configuration bridge
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
