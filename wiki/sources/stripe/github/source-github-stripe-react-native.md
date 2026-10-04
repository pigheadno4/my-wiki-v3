---
title: "GitHub: stripe/stripe-react-native"
type: source
date_ingested: 2026-05-13
date_updated: 2026-10-04
original_format: github-repo
raw_files:
  - "github/stripe/stripe-react-native/snapshots/2026-10-04-ce9c1bf/manifest.json"
  - "github/stripe/stripe-react-native/snapshots/2026-10-04-6bbf9d5/manifest.json"
  - "github/stripe/stripe-react-native/snapshots/2026-10-04-fa56337/manifest.json"
  - "github/stripe/stripe-react-native/snapshots/2026-10-04-cc20080/manifest.json"
  - "github/stripe/stripe-react-native/snapshots/2026-10-04-ee6e868/manifest.json"
  - "github/stripe/stripe-react-native/snapshots/2026-09-01-e0a845f/manifest.json"
  - "github/stripe/stripe-react-native/snapshots/2026-09-01-a628bc0/manifest.json"
  - "github/stripe/stripe-react-native/snapshots/2026-09-01-8b1bc13/manifest.json"
  - "github/stripe/stripe-react-native/snapshots/2026-07-30-e752a71/manifest.json"
  - "github-stripe-react-native.md"
tags: [stripe, react-native, mobile, sdk, payments, payment-sheet, embedded-payment-element, connect, link, crypto-onramp, apple-pay, google-pay, github-repository]
---

## Overview

`stripe/stripe-react-native` publishes `@stripe/stripe-react-native`, Stripe's official React Native bridge to its native iOS and Android payment SDKs. This cumulative page preserves the legacy `0.65.1` manual capsule, the approved `0.72.0` baseline and subsequent history through `0.80.0` delta at `ce9c1bf03fff8c022b244c2ac62a89c35ae6fab3`.

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
| `@stripe/stripe-react-native` | `0.80.0` | `ce9c1bf03fff8c022b244c2ac62a89c35ae6fab3` | Delta with approved focused reading; older history retained |

This table reports wiki ingest progress, not the latest version published upstream.

## Architecture and Package Shape

The package exposes CommonJS, ES module, and TypeScript declaration outputs from generated `lib/` paths. The retained source establishes three implementation layers:

1. `src/` owns the public TypeScript hooks, components, functions, types, code-generated native specifications, and Connect wrappers.
2. `android/src/main/` implements the Kotlin bridge over Stripe Android SDK `23.21.0` through `0.80.0`; earlier pins remain in version history.
3. `ios/` implements the Swift and Objective-C bridge over Stripe iOS SDK `26.12.1` through `0.80.0`. New architecture is required from 0.77.0; older old-architecture component evidence is historical.

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
- historical internal Checkout Session declarations (see the corrected private-preview boundary below; these are not an established working integration).

These client APIs consume client secrets and ephemeral configuration created by a merchant backend. They do not replace server-side Intent, CustomerSession, Checkout Session, or Connect-session creation.

### Checkout Private Preview

The Checkout private preview is separate from ordinary Intent-based PaymentSheet. At 0.78.0 imperative creation/session/mutations become partially bridged; 0.79.0 adds the reactive hook and server-update handshake. Payment presentation, confirmation and the embedded view remain unimplemented through 0.79.0. Platform-specific mutation gaps and earlier stubs remain version-qualified below; this is not a complete merchant-ready Checkout integration.

0.80.0 adds inline native `CheckoutPaymentElementView` rendering for an SDK-owned element. Modal `paymentElement.present` and payment `confirm` remain unimplemented. Treat the staged preview implementation history separately from normal PaymentSheet, and do not equate inline rendering with a complete payment flow.

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

Principal components include `StripeProvider`, `CardField`, `CardForm`, `AuBECSDebitForm`, `PlatformPayButton`, `AddressSheet`, `CustomerSheet`, `EmbeddedPaymentElement`, `PaymentMethodMessagingElement`, `AddToWalletButton`, `StripeContainer`, and Connect embedded components. Historical internal `CurrencySelectorElement` source through 0.75.0 was a native placeholder and is removed at 0.76.0; it is not a current supported component.

## Platform requirements

From 0.77.0, enable TurboModules/Fabric on Android, iOS and Expo. The older platform requirements below come from wrapper guidance; resolve actual native SDK minimums for the selected dependency versions rather than treating a wrapper declaration as proof of device compatibility.

| Platform | Minimum |
| --- | --- |
| Android | API 23, `compileSdkVersion` 36, `targetSdkVersion` 36, Kotlin 2.x |
| iOS | Wrapper README/podspec declare 13; this is not proof that the pinned native SDK supports 13. Verify the selected native SDK deployment target. |
| Expo | Use `expo install @stripe/stripe-react-native`; each Expo SDK pins a compatible package version |

If an Android app cannot move to SDK 36, the migration guide directs it to pin a package release based on Stripe Android SDK 22.x or earlier. `CardForm` additionally requires a Material Components theme.

From 0.78.0, React Native >=0.75 defaults to SPM for the native Stripe iOS SDK and requires dynamic frameworks. The wrapper remains a development pod: still run `pod install`. Configure `use_frameworks! :linkage => :dynamic`, or Expo `expo-build-properties` with `ios.useFrameworks: 'dynamic'`. RN <0.75 is deprecated and currently falls back to CocoaPods. Temporary opt-out uses `$StripeDisableSPM = true` or the SDK Expo plugin's `disableSPM: true`; the fallback is deprecated. Preserve `react_native_post_install`; check the app embed phase if dynamic frameworks cannot load. The README directs Identity SDK co-users to opt out until Identity supports SPM.

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

### `@stripe/stripe-react-native@0.80.0` - Delta

**Financial Connections private preview:** `preCollectedConsent` is accepted by account/session collection, bank-account token collection and Intent bank collection on both platforms. Supply the server-created Consent object's ID and Unix-second timestamp captured at affirmative acceptance of the complete Stripe-issued text. Reuse the same timestamp on retries rather than resetting it at launch. Stripe may still show its own consent pane; this does not guarantee consent UI is bypassed or preview access granted.

The bridges map optional consent to native launchers and fail missing/empty ID or nonnumeric timestamp fields within a supplied consent map. Android converts Double to Long; iOS NSNumber to intValue. These are basic shape checks, not comprehensive authenticity, freshness or valid-time enforcement. Omission leaves the ordinary consent path. Session/token collection respects connected-account configuration already present in the bridge.

**Demo flow, patch-only:** The example obtains account holder, issued consent text/locale/expiry and collection session from its demo backend, renders the full text, checks expiry when the buyer presses Agree, captures seconds and launches collection. It clears its overlay before the native sheet and restores the default publishable key when switching back. The configured default merchant lacks preview access. Its custom-secret-in-mobile setup is demo-only and must not be copied into production: keep secret keys on the merchant backend. Server Consent API semantics require separate evidence; demo routes are not public Stripe API endpoints.

**Inline Checkout element:** A WeakMap resolves only SDK-owned elements to controller IDs; unknown objects throw. React starts native height at 1, remounts on controller-ID changes and animates height updates. The iOS UIKit container uses native intrinsic height, permits one mount of an owned element, and detaches on window removal/recycle/destruction. Android Compose measures independent of the React height, obtains a presenter for the current ComponentActivity and releases it when that Activity is destroyed. Controller destruction notifies mounted views to detach on both platforms. Missing native controller/Activity means no attachment; source inspection does not prove all lifecycle recovery cases.

**Remaining limits:** Modal presentation and confirmation still throw; hook/server-update from 0.79.0 and platform-specific mutation gaps persist. Native versions remain Android `23.21.0`/iOS `26.12.1`. No native build, consent authorization or device payment test. Existing knowledge/count retained.

**Grounding:** FinancialConnections.ts:7 states Stripe may still show its consent pane; :16 requires reusing acceptance time on retries; createCheckout.ts:153/:190 retain modal/confirmation stubs; iOS container:35 says one mount only.

### `@stripe/stripe-react-native@0.79.0` - Delta

**Announced updates:** Native pins advance Android `23.20.0 -> 23.21.0`, iOS `26.12.0 -> 26.12.1`. Connect's loading overlay/spinner uses configured background/text colors, with white/black fallback. This changes loading appearance, not merchant-account authorization or payment state.

**Additional Checkout implementation:** `useCheckout` replaces its stub with loading/ready/updating/error/idle lifecycle and native session observation. It destroys controllers on disable/reload/unmount, tracks asynchronous generations, and destroys a late-created stale controller. `getConfiguration` changes do not automatically reload; reload calls the latest function. Initialization errors populate state; explicit reload rejection is retained.

`runServerUpdate` now creates an operation ID, subscribes before starting native work, filters both controller and operation IDs, and invokes the merchant callback once upon native request. It reports callback success/error to native and removes its listener on settlement. Android waits on a deferred completion; iOS waits on a continuation and cancels pending continuations when destroyed. Android scope cancellation also follows destruction. No wrapper callback timeout, backend idempotency or automatic retry is established. Update the session on the merchant backend; the native SDK owns its refresh operation.

**Remaining gaps:** `paymentElement.present` and `confirm` still throw; `CheckoutPaymentElementView` is hash-identical to its stub. iOS email mutation and Android null shipping clearing retain 0.78.0 limits. The hook/handshake implementation is not evidence of complete payment or private-preview access. Android adds MbWayAwaitAuthorization to existing next-action switches; do not infer new merchant enablement. The patch-only SPM helper guards missing TARGET_BUILD_DIR before embedding. Older knowledge/count preserved, no native build or payment test.

**Grounding:** useCheckout.ts:40-41 says changing getConfiguration does not reload automatically; createCheckout.ts:136/:173 retain presentation/confirmation stubs; EmbeddedComponent.tsx:855 sets colorText with black fallback.

### `@stripe/stripe-react-native@0.78.0` - Additive Full Ingest

**SPM migration:** The native Stripe iOS dependency moves to `stripe-ios-spm` with an exact version pin; the React Native wrapper still installs through CocoaPods. The complete new SPM helper is preserved in comparison hunks, outside the standalone capsule. It requires CocoaPods >=1.10 in SPM mode, verifies dynamic linkage/package references/project integrity, conditionally links Onramp, and adds an idempotent app embed/sign phase for dynamic Stripe frameworks. Opting out removes that phase. Expo's `disableSPM` plugin adds/removes its tagged Podfile block. RN <0.75 is deprecated, not immediately hard-rejected by the SPM selector. No install/build was executed.

**Partial Checkout implementation:** `createCheckout` subscribes before native creation, returns observed session/status and stable paymentElement ownership, bridges shipping/promotion/clear operations and destroys its controller/listeners idempotently. Android supports native email updates; iOS explicitly rejects email mutation because its pinned SDK lacks the method. Android null shipping addresses are rejected; iOS delegates the optional address to native. Payment presentation, `runServerUpdate` and `confirm` remain unimplemented, and the hook/view remain hash-identical stubs. Do not infer a complete Checkout flow or preview eligibility from bridge presence.

**Lifecycle/contracts:** JS-generated IDs and per-controller listener filtering replace the old registry/sequence buffer. Android observes session/updating flows and cancels work on destroy/invalidation; iOS observes publishers and checks controller identity after mutation. Session serializers expose status/totals/order items/payment-option details. Item-level amountDetails and adjustableQuantity.enabled replace earlier declared shapes; lastPaymentError, useAutocompleteEndpoints, group amountDetails and item discount are removed. Android payment-option images have a five-second loading timeout and empty-string fallback. These are bounded implementation findings, not cross-platform runtime proof.

**Financial Connections/compatibility:** Adds `no_eligible_accounts` and Android-only `web_browser_unavailable`; Android emits the native error enum's string value. AwaitAuthorization is handled in Android next-action switches, without proving a new method's merchant availability. Native pins advance Android `23.19.0 -> 23.20.0`, iOS `26.11.0 -> 26.12.0`. Older validated knowledge remains intact.

**Grounding:** `MIGRATING.md:7` specifies `use_frameworks! :linkage => :dynamic`; README.md:79 deprecates RN below 0.75; createCheckout.ts:122 is `present: notImplemented,`; iOS StripeSdkImpl+Checkout.swift:91 rejects unsupported email updates.

### `@stripe/stripe-react-native@0.77.0` - Additive Full Ingest

**Architecture migration:** TurboModules/Fabric are now mandatory. Set Android `newArchEnabled=true`, iOS `RCT_NEW_ARCH_ENABLED=1`, and Expo `newArchEnabled: true`. Android build configuration rejects disabled new architecture; the podspec rejects explicit `0` and always installs Core/NewArch. Old iOS view managers and Android legacy codegen sources are removed; Fabric component implementations remain. The event-emitter compatibility layer is for new-architecture RN below 0.80, not restored old-architecture support.

**Android wallet lifecycle:** Google Pay payment-method/token creation moves from AutoResolveHelper/request-code dispatch to `GooglePayRequestLauncher` and the Activity Result API. It re-registers after Activity recreation, destroys request resources after callbacks, and rejects overlapping requests. Successful status with no PaymentData becomes an explicit failure; canceled status remains distinct. PaymentSheet result delivery now waits for a current Activity, with single-run lifecycle cleanup. Retest rotation, background/resume, cancellation and rapid repeated taps; no device test was performed.

**Onramp:** KYC adds optional `idType`: US `social_security_number`, Canada `ca_sin`, Colombia `co_nit`, Philippines `ph_tin`. Documented default and native fallback are SSN; account/region eligibility is not established. The demo resets identifiers when residence changes. Android presenter recreation is announced and visible in changed hunks, but complete Android Onramp implementation remains outside the capsule.

**Checkout scaffolding, not availability:** Both native configuration mappers are added while the public stubs remain hash-identical to 0.76.0. Android uses Session-controlled billing collection, has deferred TODO setters for phone/save opt-in/Google Pay environment and parts of appearance; iOS billing configuration currently maps address only. iOS Apple Pay mapping requires a configured merchant identifier. The mapper contracts do not establish functioning creation, confirmation or rendering.

**Connect:** Internal auth-challenge setter/callback wiring is omitted from public prop types and is explicitly not an authorization boundary. Financial Connections cancellation returns null session/token/error, successful completion without a session yields `UnexpectedError`, and cleanup moves to an idempotent finalizer. These changes come from implementation comparison, not headline notes.

Native pins advance Android `23.17.1 -> 23.19.0`, iOS `26.9.0 -> 26.11.0`. This additive full ingest preserves all older API/history findings. Grounding: `README.md:76` requires new architecture; `src/types/Onramp.ts:250` documents the SSN default; `StripeSdkModule.kt:895` rejects a request already in progress; `src/connect/EmbeddedComponent.tsx:663` reports completion without a session.

### `@stripe/stripe-react-native@0.76.0` - Additive Full Ingest

**Onramp:** `useOnramp().deleteWalletAddress(walletId)` deletes a registered wallet from the authenticated current Link account and resolves an optional error. iOS delegates to the native coordinator; Android result mapping is visible only in comparison hunks. The demo fetches wallet records via its backend, deletes by ID, then removes local entries and resets selected wallet/challenge state when appropriate. Deletion does not transfer cryptocurrency. Backend propagation, idempotency and retry guarantees remain unproven.

**Checkout contract replacement:** The root newly exports `useCheckout`, `createCheckout` and `CheckoutPaymentElementView`; `CheckoutController` owns session, payment element, mutations, confirmation and destruction. `UseOptions` declares `enabled` and `getConfiguration`; creation options require a Session client secret and `returnURL`. The new session model uses `orderSummaryItems`, `totals` and typed lifecycle/payment status, replacing the previous internal session shape. These are declarations, not functioning runtime support at this SHA.

> [!warning] Contradiction
> Earlier source text described Checkout mutations and CurrencySelectorElement as normal payment surfaces. Prior 0.75.0 native Checkout methods already rejected calls as temporarily unavailable, and currency-selector views reported zero height. In 0.76.0 the replacement `useCheckout` explicitly returns error/idle with null session/element and rejects every operation; controller creation and view rendering throw. This corrects the earlier capability inference, not a regression from a proven working Checkout flow. See [[stripe-react-native-sdk]].

The old CurrencySelectorElement/native specification, Checkout bridge methods, `PaymentSheet.CheckoutSetupParams` and Embedded Payment Element Checkout overload are removed. Ordinary Intent-based PaymentSheet and Embedded Payment Element remain separate. Native controller registries generate opaque IDs, advance per-controller event sequence numbers and destroy resources on removal/invalidation; JavaScript event buffering rejects duplicate/out-of-order sequence values. This lifecycle scaffolding does not make Checkout usable.

**Compatibility:** Native dependencies advance Android `23.16.0 -> 23.17.1`, iOS `26.7.0 -> 26.9.0`. The retained migration guide still documents SDK 36 and the older Platform Pay migration. The full ingest adds this broader API/architecture boundary while preserving older knowledge; it used the user's focused-reading exception and hash checks for unchanged evidence, not a full upstream-tree read.

**Grounding:** `src/hooks/useOnramp.tsx:313-314` states "Deletes the given crypto wallet from the current Link account." / "Requires an authenticated Link user."; `src/hooks/useCheckout.ts:5` states "This version of @stripe/stripe-react-native does not include native support for the Checkout private preview."; its line 32 is `status: enabled ? 'error' : 'idle',`. Prior `ios/StripeSdkImpl.swift:41` records temporary Checkout unavailability.

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

- `raw/github/stripe/stripe-react-native/snapshots/2026-10-04-ce9c1bf/manifest.json` - exact-SHA 0.80.0 capsule, 240 retained files
- `raw/github/stripe/stripe-react-native/releases/stripe-react-native/0.80.0/2026-10-04/manifest.json` - release identity
- `raw/github/stripe/stripe-react-native/releases/stripe-react-native/0.80.0/2026-10-04/release-notes.md` - consent private-preview announcement
- `tracking/github/repos/stripe/stripe-react-native/comparisons/stripe-react-native/0.79.0--0.80.0/comparison.json` - comparison identity/dispositions
- `tracking/github/repos/stripe/stripe-react-native/comparisons/stripe-react-native/0.79.0--0.80.0/diff.patch` - changed production/affected prior code, complete new view/spec implementations and demo hunks

- `raw/github/stripe/stripe-react-native/snapshots/2026-10-04-6bbf9d5/manifest.json` - exact-SHA 0.79.0 capsule, 234 retained files
- `raw/github/stripe/stripe-react-native/releases/stripe-react-native/0.79.0/2026-10-04/manifest.json` - release identity
- `raw/github/stripe/stripe-react-native/releases/stripe-react-native/0.79.0/2026-10-04/release-notes.md` - native upgrades and Connect appearance fix
- `tracking/github/repos/stripe/stripe-react-native/comparisons/stripe-react-native/0.78.0--0.79.0/comparison.json` - comparison identity/dispositions
- `tracking/github/repos/stripe/stripe-react-native/comparisons/stripe-react-native/0.78.0--0.79.0/diff.patch` - changed production and affected prior code
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-04-6bbf9d5/files/src/hooks/useCheckout.ts` - complete reactive lifecycle implementation
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-04-6bbf9d5/files/src/checkout/createCheckout.ts` - complete partial controller bridge
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-04-6bbf9d5/files/src/checkout/runServerUpdate.ts` - complete added handshake

- `raw/github/stripe/stripe-react-native/snapshots/2026-10-04-fa56337/manifest.json` - exact-SHA 0.78.0 capsule, 233 retained files
- `raw/github/stripe/stripe-react-native/releases/stripe-react-native/0.78.0/2026-10-04/manifest.json` - release identity
- `raw/github/stripe/stripe-react-native/releases/stripe-react-native/0.78.0/2026-10-04/release-notes.md` - SPM migration and deprecation
- `tracking/github/repos/stripe/stripe-react-native/comparisons/stripe-react-native/0.77.0--0.78.0/comparison.json` - comparison identity/dispositions
- `tracking/github/repos/stripe/stripe-react-native/comparisons/stripe-react-native/0.77.0--0.78.0/diff.patch` - changed production hunks, complete added native controllers/serializers and SPM helper
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-04-fa56337/files/MIGRATING.md` - complete migration guide
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-04-fa56337/files/README.md` - installation and troubleshooting

- `raw/github/stripe/stripe-react-native/snapshots/2026-10-04-cc20080/manifest.json` - exact-SHA 0.77.0 capsule, 233 retained files
- `raw/github/stripe/stripe-react-native/releases/stripe-react-native/0.77.0/2026-10-04/manifest.json` - release identity
- `raw/github/stripe/stripe-react-native/releases/stripe-react-native/0.77.0/2026-10-04/release-notes.md` - architecture/KYC/lifecycle changes
- `tracking/github/repos/stripe/stripe-react-native/comparisons/stripe-react-native/0.76.0--0.77.0/comparison.json` - comparison identity/dispositions
- `tracking/github/repos/stripe/stripe-react-native/comparisons/stripe-react-native/0.76.0--0.77.0/diff.patch` - changed production code and affected prior code, including full added mapper/launcher implementations
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-04-cc20080/files/android/src/main/java/com/reactnativestripesdk/GooglePayRequestLauncher.kt` - complete lifecycle launcher

- `raw/github/stripe/stripe-react-native/snapshots/2026-10-04-ee6e868/manifest.json` - 0.76.0 exact-SHA capsule, 247 retained files
- `raw/github/stripe/stripe-react-native/releases/stripe-react-native/0.76.0/2026-10-04/manifest.json` - package-qualified release identity
- `raw/github/stripe/stripe-react-native/releases/stripe-react-native/0.76.0/2026-10-04/release-notes.md` - wallet deletion announcement
- `tracking/github/repos/stripe/stripe-react-native/comparisons/stripe-react-native/0.75.0--0.76.0/comparison.json` - exact comparison identity and dispositions
- `tracking/github/repos/stripe/stripe-react-native/comparisons/stripe-react-native/0.75.0--0.76.0/diff.patch` - changed code and prior Checkout/Onramp evidence
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-04-ee6e868/files/src/types/Checkout.ts` - complete new preview contract
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-04-ee6e868/files/src/hooks/useCheckout.ts` - complete unimplemented hook
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-04-ee6e868/files/src/checkout/createCheckout.ts` - complete unimplemented creation API
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-04-ee6e868/files/src/components/CheckoutPaymentElementView.tsx` - complete unimplemented view
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-04-ee6e868/files/MIGRATING.md` - retained migration guidance

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
- `raw/github/stripe/stripe-react-native/snapshots/2026-09-01-a628bc0/files/src/connect/NotificationBanner.tsx` — experimental Connect notification banner
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
