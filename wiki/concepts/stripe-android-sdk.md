---
title: "Stripe Android SDK"
type: concept
category: framework
tags: [stripe, android, kotlin, mobile, sdk, payments, google-pay, payment-sheet, embedded-payment-element, jetpack-compose]
---

## Overview

`stripe-android` is Stripe's official native Android SDK. The approved `23.13.1` baseline provides prebuilt payment UI, lower-level PaymentIntent and SetupIntent APIs, Google Pay, automatic 3DS/SCA handling, and separate modules for Connect, Identity, Financial Connections, Crypto Onramp, BNPL messaging, and card scanning.

The SDK collects sensitive payment details directly for Stripe rather than routing them through the merchant server. Merchant backends still own creation of PaymentIntents, SetupIntents, customer/session credentials, fulfillment decisions, and webhook processing.

## `23.13.1` Baseline Requirements

| Field | Value |
| --- | --- |
| Package | `com.stripe:stripe-android:23.13.1` |
| Release tag | `v23.13.1` |
| Exact commit | `dc874ce7c62dd433664ec4e312efeb9300c21795` |
| Android minimum | Android 6.0 / API 23 |
| Compile SDK | 36+ |
| Android Gradle Plugin | 8.13.2 |
| Gradle | 9.3.1 |
| Kotlin | 2.3.10 |
| Compose compatibility | Compose UI 1.10.x for SDK 23.x |

This table preserves the 23.13.1 baseline requirements. Newer ingested deltas are recorded below and in [[source-github-stripe-android]]; this is not a latest-upstream claim.

## Installation

```gradle
dependencies {
    implementation 'com.stripe:stripe-android:23.13.1'
}
```

Initialize publishable configuration at application startup. A connected-account ID can be included for Connect API requests.

```kotlin
PaymentConfiguration.init(context, publishableKey = "pk_...")
PaymentConfiguration.init(context, publishableKey = "pk_...", stripeAccountId = "acct_...")
```

## Payment UI

### PaymentSheet

PaymentSheet is the maintained prebuilt checkout surface. `PaymentSheet.Builder` is the preferred Activity, Fragment, and Compose construction path; direct constructors are deprecated. It supports:

- PaymentIntent and SetupIntent client-secret flows;
- deferred Intent creation through a merchant callback;
- saved methods through customer configuration;
- Google Pay, Link, delayed methods, custom methods, and external methods subject to account and platform eligibility;
- appearance, billing, shipping, payment-method ordering, and wallet-button configuration; and
- automatic next-action and 3DS handling.

`PaymentSheetResult.Completed` means the customer completed the SDK flow. The payment can still be processing, so fulfillment must wait for a successful server-side payment event.

### FlowController

`PaymentSheet.FlowController` separates method selection from confirmation. The merchant presents payment options, displays the returned `PaymentOption`, and calls `confirm()` from its own pay button.

### Embedded Payment Element

`EmbeddedPaymentElement` places payment-method UI inside a merchant-owned Compose layout. It has explicit configure, selection-state, clear, and confirm operations and returns `Completed`, `Canceled`, or `Failed`. The retained example demonstrates one-step and state-preserving two-step Activity contracts.

## Google Pay

`GooglePayLauncher` confirms PaymentIntents or SetupIntents after an asynchronous readiness callback. `presentForPaymentIntent` and `presentForSetupIntent` are invalid until the device is reported ready. SetupIntent presentation additionally requires an ISO currency code, even though the SetupIntent API itself does not.

`GooglePayPaymentMethodLauncher` is the lower-level option when an integration needs a PaymentMethod without immediately confirming an Intent. Compose integrations use `rememberGooglePayLauncher`.

Wallet API availability does not prove that a specific merchant, country, currency, card network, or payment method is enabled.

## Low-Level APIs

The `Stripe` entry point supports asynchronous and synchronous access to:

- PaymentIntent confirmation, retrieval, and next-action handling;
- SetupIntent confirmation, retrieval, and next-action handling;
- PaymentMethod creation;
- Source creation and retrieval; and
- token creation for supported card, bank, identity, and account parameter types.

`PaymentLauncher` is a lifecycle-aware confirmation and next-action abstraction for Activity, Fragment, and Compose integrations. Both surfaces use publishable keys and client secrets; they do not replace server-side secret-key operations.

## Specialized Modules

| Module | Primary contract | Lifecycle or access note |
| --- | --- | --- |
| `connect` | `EmbeddedComponentManager` creates account-onboarding, Payments, and Payouts components | Requires publishable key plus a callback that fetches a server-created client secret; Payments and Payouts became GA in `23.12.0` |
| `financial-connections` | `FinancialConnectionsSheet` returns linked-account session data or token results | Register the launcher unconditionally during Activity/Fragment initialization |
| `identity` | `IdentityVerificationSheet` presents a verification session | Requires a verification-session ID and ephemeral-key secret created on the server |
| `crypto-onramp` | `OnrampCoordinator` handles Link authentication, KYC, wallet ownership, payment collection, token creation, and checkout | Marked experimental/private-preview evidence; availability is not implied by the public source |
| `payment-method-messaging` | Compose BNPL promotional messaging for Affirm, Afterpay/Clearpay, and Klarna | Public preview; amount and currency are required, and configuration can return `NoContent` |
| `stripecardscan` | Card scan implementation used by Stripe UI surfaces | Direct retained classes are library-group restricted; v23.6 restored card scanning in public preview through Stripe UI |

## Migration Landmarks

- `23.0.0` raises the minimum Android API level to 23 and the compile/target SDK to 36. It also updates Kotlin, Compose, Gradle, and Android dependencies.
- v22 removes legacy token-oriented `CardParams` paths, deprecated Google Pay launchers, 3DS1, and accidentally exposed APIs; builder APIs replace data-class copying for public configuration objects.
- v21 removes Basic Integration in favor of Mobile Payment Element and changes PaymentSheet's default method layout to automatic.
- Current code favors builder and lifecycle-aware launcher APIs over deprecated constructors and launcher factories.

## `23.13.1` Release Note

The exact `23.13.1` release fixes an Alipay test-mode issue where the SDK could fail to reconcile and close out a payment. The broader architecture on this page is baseline evidence from the complete retained capsule and must not be attributed solely to that patch.

## `23.14.0` Delta

The approved focused-reading delta adds private-preview LinkAppearance declarations: light/dark colors, selected border, primary/content colors, primary-button corner radius/height, automatic/light/dark style and reduced branding. LinkController.Configuration gains appearance and billingDetailsCollectionConfiguration setters. API signatures do not establish defaults, validation, rendering or all downstream billing behavior; the current implementation is excluded.

CryptoNetwork exposes Tempo. Release notes announce internal preview API-version pinning, but the request/network implementation is excluded and merchant eligibility is unverified. The later changelog places the billing-collection note under 23.13.1 although the earlier retained snapshot lacked it; preserve that retrospective label separately from this observed signature difference. See [[source-github-stripe-android]] and [[changelog-github-stripe-android]] for subsequent ingested releases. Earlier platform/installation examples remain qualified to 23.13.1. No Android build/device/payment testing.

## `23.15.0` Delta

Crypto Onramp adds optional Samsung Pay configuration, readiness callback, selection/display types, availability results and typed error reasons. The merchant app must supply the Samsung Pay SDK. The retained compiled API does not identify constructor parameter names/defaults or prove readiness/credential mapping, supported SDK versions or ordinary PaymentSheet Samsung Pay support. See [[stripe-crypto-onramp]].

Release notes announce private-preview Link errors for no funding sources instead of silent card fallback, and Agrobank/MBSB/Bank of China FPX additions with alphabetic ordering. Those changed implementations are excluded; they are not device-verified behavior. Build changes add test tooling/managed-device settings, not a new merchant deployment floor. Older knowledge remains intact in [[source-github-stripe-android]] and [[changelog-github-stripe-android]].

## `23.16.0` Additive Full Ingest

`PaymentSheet.LinkConfiguration.Display.WalletButtonHidden` keeps Link enabled while hiding its wallet button/row. The retained configuration returns `shouldDisplay=true` and `shouldShowButton=false`; its documented contract preserves returning-user and inline-signup flows. `Never` is different: it disables Link display. Downstream rendering is outside the capsule, so this is a source contract, not device-tested behavior.

Release notes announce inline address autocomplete enabled by default in PaymentSheet, FlowController and AddressElement. The newer changelog also inserts this announcement under 23.15.0, absent from that earlier retained release evidence. The exact implementation introduction and fallback/eligibility behavior are not established. Test address flows when upgrading; do not infer that Google Places setup or other prerequisites disappeared.

Experimental Crypto Onramp adds authenticated wallet deletion by wallet ID; see [[stripe-crypto-onramp]]. Full mode was explicitly approved with focused reading; unchanged retained evidence was hash-checked and all older knowledge preserved. See [[source-github-stripe-android]] and [[changelog-github-stripe-android]].

## `23.17.0` Additive Full Ingest

The migration guide deprecates Google Places key builder calls and AddressLauncher constructor arguments and directs integrations to remove them: autocomplete continues without a merchant key, including for previously keyless integrations. PaymentSheet source carries that deprecation; autocomplete request/fallback internals remain excluded. This is the 23.17.0 contract, not a silent rewrite of 23.16.0's evidence limits.

Identity and Crypto Onramp build files now declare API 24 minimum. This scoped requirement does not raise every Stripe Android module's floor. Identity Configuration adds nullable `@ColorInt brandColor`, default null, for primary-action-button styling; its one-argument constructor remains, but compiled `copy`/`copy$default` signatures change. Recompile dependent binaries and review Java copy calls. Guided 3D selfie capture and direct-API Alipay SetupIntent support are announced, not implementation-verified in this capsule.

The newer changelog attributes the API 24 change to 23.15.0 retrospectively; earlier retained build files lacked it. Preserve both the later label and observed 23.16.0 -> 23.17.0 build boundary. See [[source-github-stripe-android]], [[changelog-github-stripe-android]] and [[stripe-crypto-onramp]]. No device/build/payment testing.

## `23.17.1` Additive Full Ingest

Release notes announce fixes for Klarna billing fields after a country change, Wero duplicate country fields during full billing-address collection and Link 2FA's `Not you?` account logout. Their implementation is excluded; no runtime, retry or session-isolation guarantees are inferred.

Compiled PaymentSheet API removes the generated public `StripeGooglePayButtonBinding` class, including bind/inflate/root access and fields. Direct references to this class are a source/binary compatibility risk; it is not a supported merchant integration recipe and its removal does not establish removal of Google Pay. Identity adds a generated top-app-bar accessor, not a new merchant API. Earlier keyless-address and scoped Identity/Onramp API 24 findings remain intact. See [[source-github-stripe-android]] and [[changelog-github-stripe-android]].

## `23.18.0` Additive Full Ingest

PaymentSheet release notes announce SeQura, PAYCO, Korean cards, Naver Pay, Kakao Pay and Scalapay support. The compiled payments-core API adds the corresponding `PaymentMethod.Type` values and `PaymentMethodCreateParams` creation overloads. Declarations are directly observed; actual PaymentSheet routing, forms, eligibility and redirect/confirmation behavior remain excluded. Review exhaustive enum handling and test enabled methods rather than assuming every merchant gains access.

AddressElement now announces Stripe-hosted autocomplete by default. This adds provider-specific information to the earlier 23.16.0 default announcement and 23.17.0 keyless migration; it does not replace that history or establish request/fallback behavior. Play Services Wallet advances from 19.5.0 to 20.0.0 in dependency declarations, without proving a changed device floor or runtime Google Pay behavior.

Onramp gains KYC identity-type declarations; see [[stripe-crypto-onramp]]. Identity adds library-group-restricted biometric-consent header configuration, not a supported general merchant customization API. Full mode with focused reading was explicitly approved; unchanged evidence was hash-checked and older knowledge retained. See [[source-github-stripe-android]], [[changelog-github-stripe-android]], [[stripe-bnpl]] and [[stripe-korea-payment-methods]]. No build/device/payment testing.

## `23.19.0` Additive Full Ingest

`WalletButtonHidden` now documents showing Link's button/row when an existing Link user is detected and hiding it otherwise. Link remains enabled, including automatic verification and inline sign-up; `shouldDisplay` still returns true. The old internal `shouldShowButton` getter disappears, but the compiled public inventory is unchanged. Detection/rendering implementation is excluded, so this is a documented contract and observed internal-source change, not device-tested UI behavior.

> [!warning] Contradiction
> The 23.16.0 version-qualified record above describes unconditional button hiding. The retained 23.19.0 contract instead describes conditional returning-user visibility. Preserve both by version; do not carry the old always-hidden assumption into this release. See [[source-github-stripe-android]].

Release notes announce Welsh (United Kingdom), Arabic (Saudi Arabia) and a half-visible PaymentSheet race fix. README lists Welsh but omits Arabic; that omission does not prove Arabic is unsupported. Locale resources/race-fix internals are excluded. Gradle enables optimized resource shrinking without establishing app-size, runtime or deployment-floor effects. Earlier history remains intact in [[source-github-stripe-android]] and [[changelog-github-stripe-android]]. No build/device/payment tests.

## `23.20.0` Delta

PaymentSheet announces Bizum support; compiled payments-core adds `PaymentMethod.Type.Bizum` and `StripeIntent.NextActionType.AwaitAuthorization`. Review exhaustive enum handling. These declarations do not establish Bizum eligibility, required fields, authorization timing or a complete payment recipe: model/PaymentSheet routing internals are excluded. Alipay+ and Alipay SDK redirect fixes are release announcements with excluded implementation.

Current GooglePayLauncher explicitly passes `GooglePayConfig(context)` to its repository in Activity, restricted React Native Activity, Fragment and Compose construction paths. The existing asynchronous readiness gate and SetupIntent currency requirement remain. GooglePayConfig/repository implementations are excluded, so no new key/account/tokenization or readiness outcome is inferred. Financial Connections adds a test-only Compose dependency, not a merchant deployment-floor change. Earlier history remains in [[source-github-stripe-android]] and [[changelog-github-stripe-android]]. No build/device/payment tests.

## `23.21.0` Additive Full Ingest

PaymentSheet Activity/Fragment construction now retrieves a host-owned StoreViewModel, retains a callback identifier in SavedStateHandle and forwards it to the launcher/callback registry instead of using the shared default identifier. This is observed internal wiring, not a guarantee of per-instance isolation or process-restoration correctness; multiple sheets under the same owner can share the ViewModel. Compose helper and concrete launcher/registry implementations are excluded. Regression-test deferred/external callbacks across navigation and recreation.

EmbeddedPaymentElement gains public-preview apiConfiguration, with an opt-in example that prefetches checkout configuration and supplies ApiConfiguration without initializing global PaymentConfiguration on that path. PaymentSheet's similarly named setter is library-group restricted; do not generalize the preview to a supported PaymentSheet/FlowController merchant API. Generated public UI declarations change/remove, so direct references need compatibility review rather than inference that payment features disappeared.

FinancialConnectionsSheet adds nullable preCollectedConsent forwarding while preserving the old one-argument call; compiled bank-account launcher overloads and NO_ELIGIBLE_ACCOUNTS are added. Consent type/validation/network and callback error mapping are excluded. Notes announce MB WAY, mixed-PAN-length card validation and Financial Connections error/telemetry fixes; compiled MbWay/MbWayAwaitAuthorization declarations prove API presence, not eligibility or runtime outcomes. Onramp terms contracts are recorded in [[stripe-crypto-onramp]].

> [!warning] Contradiction
> The newer raw changelog moves the KYC note previously attributed to 23.17.1 into 23.18.0 and retrospectively labels terms methods under 23.19.0. The retained terms signatures/source are first observed across 23.20.0 -> 23.21.0 in this comparison. Preserve earlier evidence and labels rather than silently backdating implementation. See [[source-github-stripe-android]] and [[changelog-github-stripe-android]].

Full mode with focused reading was approved; unchanged inventory/history mechanically checked. Earlier architecture, platform floors and versioned contracts remain intact. No build/device/payment tests.

## `23.22.0` Additive Full Ingest

FlowController Activity/Fragment builders and deprecated creators now retrieve StoreViewModel under FLOW_CONTROLLER_STORE_KEY and pass its SavedStateHandle-backed callback ID to the factory and callback registry. This extends 23.21.0's PaymentSheet change to these FlowController paths. The same owner/key can share a store; this is not per-instance isolation or proof of restored callback delivery. Compose delegates to its unchanged helper. Regression-test deferred/external callbacks across navigation and host recreation.

Compiled API adds GoPay, MoMo and Pix creation/type declarations and DisplayPixDetails. Notes announce GoPay/MoMo PaymentIntent and Pix PaymentIntent/SetupIntent PaymentSheet support. Routing, request fields, mandates and eligibility are excluded; see [[stripe-pix]]. Embedded View more/Edit processing guards and removal of the process-wide HTTP cache are announcements with excluded implementation.

Financial Connections adds financialConnectionsSessionId/component3 declarations. Identity's library-group-restricted biometric-consent source adds a required hideDeclineButton Boolean; the general merchant Configuration constructor remains unchanged. Two generated public primary-button binding classes disappear: review direct references without inferring removal of PaymentSheet functionality. Onramp wallet/contact changes are recorded in [[stripe-crypto-onramp]]. Older knowledge remains in [[source-github-stripe-android]] and [[changelog-github-stripe-android]]. No Android build/device/payment testing.

## `23.23.0` Additive Full Ingest

Notes announce browsable-only intent URL resolution in authentication, invalid-secret errors without echoing the supplied value, and legacy next-action errors instead of uncaught exceptions. Retained Stripe.kt removes local PaymentIntent/SetupIntent.ClientSecret wrappers in four Activity/Fragment next-action methods and forwards the string to paymentController.startAuth. The controller, client-secret models and URL resolver are excluded: error text/redaction, result delivery and security enforcement are not independently verified. Keep client secrets out of app logs regardless of SDK error wording.

Compiled API adds GCash, NgCard, Qris and ShopeePay types/creation overloads; NgCard exposes brand/last4 with Amex, Mastercard, Verve, Visa and Unknown brand declarations. Notes announce one-time Naira card, GCash, and QRIS/ShopeePay PaymentIntent PaymentSheet support. Declarations do not prove eligibility, request fields or runtime routing. Test-header removal, case-insensitive address prefill and incomplete optional-phone rejection are announcements with excluded implementation; absence of a test banner is not evidence of live mode.

Financial Connections forwards the same public key/account/consent fields through internal ApiConfiguration.State without changing merchant configuration signatures. Identity adds library-group-restricted primary/secondary button styles, not general merchant APIs; generated debug/Compose declarations change/remove. Experimental Onramp restores callback registration before constructing presenters; its excluded store implementation and retrospective attribution are detailed in [[stripe-crypto-onramp]]. Production floors are not raised by retained build changes (test/debug tooling and root classpath changes). Older history remains in [[source-github-stripe-android]] and [[changelog-github-stripe-android]]. No build/device/payment testing.

## `23.24.0` Additive Full Ingest

The preview annotation moves from `com.stripe.android.paymentelement.ApiConfigurationPreview` to `com.stripe.android.core.ApiConfigurationPreview`. The old annotation disappears from the retained PaymentSheet API inventory; the Embedded example changes its import and adds explicit opt-ins to its checkout helper and result type. Six retained module build files add the new opt-in. Preview consumers must update imports/compiler opt-ins and recompile; this does not make the API generally available, change the example's server-owned Intent flow, or establish new credential-isolation behavior. The core annotation definition itself is outside this capsule. [[source-github-stripe-android]]

Compiled payments-core adds Mondu, NgBankTransfer, NgUssd and NgWallet types plus corresponding static/Companion creation overloads. Notes announce PaymentIntent PaymentSheet support for all four; declarations do not establish request-field requirements, enabled accounts/currencies, recurring support, next-action behavior or actual payment results. Address country-dropdown autofill and Identity test-mode bundled document/selfie upload are release announcements with excluded implementation. The retained module floors do not change. Experimental Onramp changes are recorded in [[stripe-crypto-onramp]].

> [!warning] Contradiction
> The newer cumulative changelog moves the Identity/Onramp API 24 note from 23.15.0 to 23.17.0 and adds older brandColor/manual-capture/upload/privacy-link notes. Preserve the prior raw/wiki attributions and observed 23.16.0 -> 23.17.0 floor/styling boundary; these retrospective edits are not new 23.24.0 runtime changes or proof of an earlier first implementation. [[source-github-stripe-android]] records the same distinction. The user approved additive full mode with focused reading; all earlier knowledge remains in [[changelog-github-stripe-android]]. No build/device/payment tests were run.

## `23.25.0` Delta

Compiled payments-core adds `PaymentMethod.Type.TouchNGo` and `TrueMoney`, plus static/Companion `createTouchNGo` and `createTrueMoney` overloads. Release notes announce Touch 'n Go PaymentSheet support for payments and setup and TrueMoney PaymentSheet support without an equivalent explicit setup claim. API presence does not establish serialized values, required fields, country/currency or merchant eligibility, recurring capability or a complete integration recipe. Review exhaustive type switches and test enabled methods. [[source-github-stripe-android]]

AddressElement's discard-unsaved-changes confirmation is a release announcement; its UI implementation is excluded. Onramp adds a card-funding display getter, not a new funding/checkout operation; see [[stripe-crypto-onramp]]. Generated Link verification Compose accessors change, but they are not supported merchant entry points. Retained platform requirements and merchant PaymentSheet/FlowController call sites are unchanged.

> [!warning] Contradiction
> The newer raw changelog adds native Link email OTP/MFA support under `23.24.0`, absent from that earlier retained changelog/notes. Preserve that retrospective label and the older immutable evidence rather than call this a new `23.25.0` feature or infer the first implementation release. [[source-github-stripe-android]] records the same distinction. Older version knowledge remains intact; no build/device/payment tests.

## `23.25.1` Delta

Release notes announce a fix for PaymentSheet error messages disappearing after returning from Link. The error-state/return implementation is excluded; this is not proof of new authentication capability, changed payment status or successful device behavior. Regression-test error visibility after Link returns without equating displayed errors or SDK completion with server payment outcomes. [[source-github-stripe-android]]

The retained payments-core build adds `implementation libs.androidx.webkit`. The alias's resolved version is outside the retained catalog, so no exact WebKit version, minimum-device change or security/runtime claim follows. All retained compiled API inventories, launcher/example source and other dependency declarations remain unchanged. All 23.25.0 and older findings remain preserved in [[changelog-github-stripe-android]]. No build/device/payment tests.

## Related

- Source: [[source-github-stripe-android]]
- Changelog: [[changelog-github-stripe-android]]
- Company: [[stripe]]
- Native counterpart: [[stripe-ios-sdk]]
- Cross-platform bridge: [[stripe-react-native-sdk]]
- Supporting concepts: [[stripe-inapp-payments]], [[stripe-payment-intents]], [[stripe-3d-secure]], [[stripe-payment-method-messaging-element]], [[stripe-crypto-onramp]]

## Sources

- `raw/github/stripe/stripe-android/snapshots/2026-07-31-dc874ce/manifest.json` - exact-SHA `23.13.1` source capsule
- `raw/github/stripe/stripe-android/snapshots/2026-07-31-dc874ce/files/README.md` - purpose, capabilities, requirements, installation, and security boundary
- `raw/github/stripe/stripe-android/snapshots/2026-07-31-dc874ce/files/MIGRATING.md` - major-version migration requirements
- `raw/github/stripe/stripe-android/snapshots/2026-07-31-dc874ce/files/paymentsheet/src/main/java/com/stripe/android/paymentsheet/PaymentSheet.kt` - PaymentSheet and FlowController contract
- `raw/github/stripe/stripe-android/snapshots/2026-07-31-dc874ce/files/paymentsheet/src/main/java/com/stripe/android/paymentsheet/PaymentSheetResult.kt` - result and fulfillment semantics
- `raw/github/stripe/stripe-android/snapshots/2026-07-31-dc874ce/files/payments-core/src/main/java/com/stripe/android/Stripe.kt` - low-level client API
- `raw/github/stripe/stripe-android/snapshots/2026-07-31-dc874ce/files/payments-core/src/main/java/com/stripe/android/googlepaylauncher/GooglePayLauncher.kt` - Google Pay lifecycle and result contract
- `raw/github-stripe-android.md` - legacy v23.8.0 capsule pointer
