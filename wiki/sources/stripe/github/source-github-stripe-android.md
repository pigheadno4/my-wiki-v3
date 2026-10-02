---
title: "GitHub: stripe/stripe-android"
type: source
date_ingested: 2026-05-13
date_updated: 2026-10-02
original_format: github-repo
raw_files:
  - "github/stripe/stripe-android/snapshots/2026-09-29-a074a95/manifest.json"
  - "github/stripe/stripe-android/snapshots/2026-09-29-d47cf89/manifest.json"
  - "github/stripe/stripe-android/snapshots/2026-09-29-a95cc0e/manifest.json"
  - "github/stripe/stripe-android/snapshots/2026-09-29-f5e7f5c/manifest.json"
  - "github/stripe/stripe-android/snapshots/2026-09-29-c5f31a3/manifest.json"
  - "github/stripe/stripe-android/snapshots/2026-09-29-93ef69a/manifest.json"
  - "github/stripe/stripe-android/snapshots/2026-09-29-a8d0e74/manifest.json"
  - "github/stripe/stripe-android/snapshots/2026-09-29-03dc31c/manifest.json"
  - "github/stripe/stripe-android/snapshots/2026-09-29-f286cb8/manifest.json"
  - "github/stripe/stripe-android/snapshots/2026-07-31-dc874ce/manifest.json"
  - "github-stripe-android.md"
tags: [stripe, android, kotlin, mobile, sdk, payments, payment-sheet, embedded-payment-element, google-pay, connect, identity, financial-connections, crypto-onramp, github-repository]
---

## Overview

`stripe/stripe-android` publishes Stripe's official native Android SDK. This cumulative page preserves the legacy `23.8.0` manual capsule and adds the approved `stripe-android@23.13.1` full baseline at commit `dc874ce7c62dd433664ec4e312efeb9300c21795`.

Repository: <https://github.com/stripe/stripe-android>

## Evidence Boundary

- `23.21.0` uses explicitly approved additive full mode with focused reading for callback/lifecycle architecture and compiled compatibility changes. All 104 prior/current retained hashes match: 52 files per capsule, twelve modified/40 unchanged, 757 classified upstream dispositions. Changed source/context, short files, API blocks and affected prior code reviewed; expanded unchanged full inventory/history mechanically checked. Concrete callback registry/launcher, Embedded credentials processing, consent/terms persistence, card/Bizum/MB WAY routing and Financial Connections error mapping remain excluded. No build/device/payment tests; all older wiki knowledge preserved.
- `23.20.0` is a contained approved delta with focused reading: complete current/prior GooglePayLauncher, changed short files, added API declarations in enclosing context and release/patch content reviewed. Both 52-file capsules match all 104 hashes; eight modified/44 unchanged and 712 classified upstream dispositions. Unchanged inventories/history checked mechanically; Bizum/Alipay routing and GooglePayConfig/repository internals are excluded. No build/device/payment tests.
- `23.19.0` uses explicitly approved additive full mode with focused reading for the revised returning-user Link entry contract. All 104 prior/current retained hashes match; 52 files per capsule, five modified/47 unchanged, 942 classified upstream dispositions. Changed short files, release/patch content and complete prior/current LinkConfiguration blocks read; unchanged expanded full inventory/history checked mechanically. Link detection/rendering, locale resources and race-fix implementation remain excluded; no build/device/payment proof.
- `23.18.0` is an explicitly approved additive full-mode override with focused reading. Both 52-file capsules have matching hashes (104 checks): nine modified/43 unchanged, 954 classified upstream dispositions. Changed implementation, short files, API additions/context and affected prior evidence reviewed; unchanged full-mode inventory/history checked mechanically. PaymentSheet method implementations, autocomplete requests/fallback and Onramp KYC model/request internals remain excluded. No build/device/payment tests; all older knowledge preserved.
- `23.17.1` uses approved additive full mode with focused reading for a removed compiled public generated binding class. All 104 prior/current hashes matched: 52 files per capsule, six modified/46 unchanged; 263 upstream dispositions. Changed short files, release/comparison patch and API class context reviewed; unchanged full-mode inventory/history checked mechanically. Klarna/Wero billing and Link 2FA logout implementations remain excluded. No build/device/payment or session-isolation tests.
- `23.17.0` is an approved additive full-mode override with focused reading for incompatible Identity copy signatures and module-floor changes. All 104 retained hashes matched; 52 files per snapshot, 12 modified/40 unchanged; 762 upstream dispositions. Changed implementation/API context, migration additions, dependency/build declarations and release/patch content reviewed; unchanged raw/history mechanically carried forward. Autocomplete networking, Alipay next-action and guided selfie implementation remain excluded. No Android build/device/payment tests.
- `23.16.0` has an explicitly approved full-mode override with focused reading, not a complete reread of unchanged code. Changed declarations and implementation context, affected prior code, short files, release notes and retained patch were read; unchanged history and expanded full-mode inventories were checked mechanically. Both 52-file capsules have matching hashes (104 checks): ten modified/42 unchanged, 577 upstream dispositions. Autocomplete implementation, downstream Link rendering and Onramp deletion/network internals remain excluded. Earlier baselines and deltas are preserved; no build/device/payment tests.
- The approved `23.15.0` delta uses the standing nine-update focused-reading exception. Changed short files/builds and release/diff content read fully; changed API declarations/enclosing blocks and affected prior declarations read; unchanged history/inventories mechanically checked. Both capsules have 52 files: seven modified, 45 unchanged. All 104 retained hashes matched. All 545 upstream paths have dispositions, not full semantic implementation coverage. Samsung Pay configuration/availability/credential/error internals, FPX list/order and Link funding-source handling are excluded; announcements and signatures are distinguished. No Android build/device/payment tests.
- The approved `23.14.0` delta uses focused reading: changed API declarations in complete enclosing blocks, affected prior declarations, changed short files and release/diff content; unchanged cumulative history and inventories checked mechanically. Both capsules have 52 files: six modified, 46 unchanged, none added/removed. All 104 prior/current retained hashes matched. The packet classifies 337 upstream paths, but excluded paths are not semantically reviewed. Current Link appearance/billing implementation, CryptoOnramp network/request plumbing, Checkout internals and changed Google Pay helpers remain excluded. No Android build, device/payment or eligibility tests.
- The `23.13.1` capsule retains 52 production, public-signature, build, documentation, and example files. Tests, fixtures, screenshot trees, generated docs, CI, and general tooling are excluded by policy.
- This is a bounded public-source capsule, not a full repository mirror. A later query that needs excluded implementation requires an immutable supplement tied to the exact SHA.
- The legacy `23.8.0` evidence is a manually selected 10-file capsule. No automated comparison exists from its SHA to `23.13.1`, so retained baseline findings are not represented as a complete file-by-file diff.
- Public source proves SDK contracts, not merchant eligibility, enabled payment methods, geographic availability, preview access, or server API behavior.
- `PaymentSheetResult.Completed` does not prove that funds moved. Fulfillment remains gated by a successful server-side Stripe payment event.

## Grounding Excerpts

> "We provide powerful and customizable UI elements that can be used out-of-the-box to collect your users' payment details. We also expose the low-level APIs that power those UIs so that you can build fully custom experiences."
>
> `raw/github/stripe/stripe-android/snapshots/2026-07-31-dc874ce/files/README.md:12`

> "This means sensitive data is sent directly to Stripe instead of passing through your server."
>
> `raw/github/stripe/stripe-android/snapshots/2026-07-31-dc874ce/files/README.md:34`

> "The SDK now requires Android 6.0+ (API level 23+)"
>
> `raw/github/stripe/stripe-android/snapshots/2026-07-31-dc874ce/files/MIGRATING.md:3-7`

> "The payment may still be processing at this point; don't assume money has successfully moved."
>
> `raw/github/stripe/stripe-android/snapshots/2026-07-31-dc874ce/files/paymentsheet/src/main/java/com/stripe/android/paymentsheet/PaymentSheetResult.kt:14-20`

> "Fixed an issue where the SDK could fail to correctly reconcile and close out an Alipay payment in test mode."
>
> `raw/github/stripe/stripe-android/releases/stripe-android/23.13.1/2026-07-31/release-notes.md:1-2`

## Package Status

| Package | Latest ingested release | Exact SHA | Evidence status |
| --- | --- | --- | --- |
| `stripe-android` | `23.21.0` | `a074a9500e14932f00ce9cef250a3c63940f9837` | Approved additive full mode with focused reading; all older baselines/deltas retained |

This table reports wiki ingest progress, not the latest release published upstream.

## Architecture

The retained repository evidence separates the Android SDK into these principal layers:

1. `paymentsheet` owns PaymentSheet, FlowController, Embedded Payment Element, configuration, and public result contracts.
2. `payments-core` owns the `Stripe` client, Intent confirmation and next-action handling, Google Pay, PaymentLauncher, models, and public API signatures.
3. Product modules expose Connect embedded components, Financial Connections, Identity, Crypto Onramp, Payment Method Messaging, and card scanning.
4. Example applications demonstrate complete PaymentSheet, custom FlowController, and embedded-element lifecycles with server-created client secrets.

The build includes more modules than the bounded capsule retains. Module names in `settings.gradle` are inventory evidence, not a claim that every module is publicly supported or independently installable.

## Core Payment Surfaces

### PaymentSheet

PaymentSheet is the prebuilt collect-and-confirm UI. The preferred `PaymentSheet.Builder` registers result and optional custom/external/deferred-confirmation callbacks before building for an Activity, Fragment, or Compose host. Direct constructors remain available but are deprecated.

PaymentSheet supports three broad initialization patterns:

- an existing PaymentIntent client secret;
- an existing SetupIntent client secret; or
- `IntentConfiguration`, where a merchant callback creates or confirms the Intent on its server after payment details are collected.

`PaymentSheet.Configuration` controls merchant display, customer credentials, Google Pay, Link, appearance, billing/shipping collection, delayed methods, ordering, wallets, custom methods, and external methods. These options configure the client surface; account and payment-method eligibility still come from Stripe configuration and server-created resources.

### FlowController

FlowController supports merchant-owned checkout composition. The app configures the controller, presents payment options, renders the returned `PaymentOption`, and calls `confirm()` from its own buy button. The retained custom-flow example gets a PaymentIntent client secret from a backend before configuration.

### Embedded Payment Element

`EmbeddedPaymentElement` puts selectable payment UI directly in a Compose layout. Its contract includes configure, current option, clear, state restoration, and confirm operations. Result handling is explicit: `Completed`, `Canceled`, or `Failed`. The retained playground demonstrates both one-step completion and two-step navigation that returns updated element state.

### Direct Intent APIs

The `Stripe` entry point exposes PaymentIntent and SetupIntent confirmation, retrieval, and next-action handling, PaymentMethod creation, Sources, and Tokens. `PaymentLauncher` provides a narrower lifecycle-aware Intent confirmation surface for Activity, Fragment, and Compose.

The direct APIs use publishable keys, connected-account IDs, and client secrets. Secret-key creation of Intents, customers, sessions, and ephemeral credentials remains on the backend.

## `stripe-android@23.14.0` Integration Delta

LinkController private preview gains LinkAppearance with fluent lightColors/darkColors, primaryButton, reduceLinkBranding and style setters. Colors exposes primary, contentOnPrimary and borderSelected; primary-button configuration exposes nullable Float cornerRadiusDp and heightDp; style enumerates AUTOMATIC, ALWAYS_LIGHT and ALWAYS_DARK. Configuration adds appearance and billingDetailsCollectionConfiguration alongside existing identity/payment-method setters. The compiled API proves declarations only, not Kotlin parameter names, defaults, bounds, actual rendering or downstream collection behavior. No incompatible retained signature removal was observed.

CryptoNetwork adds Tempo. Internal CryptoOnramp preview API-version pinning is a release announcement, not independently verified request behavior: serializers, request implementation and current presenter internals are excluded. Do not infer account/network eligibility or promote private preview to general availability.

The cumulative changelog preserves all 4,733 prior lines and inserts eleven lines, including a billingDetailsCollectionConfiguration note under 23.13.1. That older retained API/notes did not contain this addition. Record the upstream retrospective attribution separately from the observed 23.13.1 -> 23.14.0 signature boundary; neither proves the exact first implementation release. README/gradle.properties/VERSION changes only advance the version; no deployment-floor change is established.

### Grounding excerpts

> "`LinkController` now supports appearance customization via `LinkAppearance` (private preview)."
>
> `raw/github/stripe/stripe-android/releases/stripe-android/23.14.0/2026-09-29/release-notes.md` - PaymentSheet bullet

> `public final class com/stripe/android/link/LinkAppearance {`
>
> `raw/github/stripe/stripe-android/snapshots/2026-09-29-f286cb8/files/paymentsheet/api/paymentsheet.api:234`

> `public final fun billingDetailsCollectionConfiguration (Lcom/stripe/android/paymentsheet/PaymentSheet$BillingDetailsCollectionConfiguration;)Lcom/stripe/android/link/LinkController$Configuration;`
>
> `raw/github/stripe/stripe-android/snapshots/2026-09-29-f286cb8/files/paymentsheet/api/paymentsheet.api:290`

> `public static final field Tempo Lcom/stripe/android/crypto/onramp/model/CryptoNetwork;`
>
> `raw/github/stripe/stripe-android/snapshots/2026-09-29-f286cb8/files/crypto-onramp/api/crypto-onramp.api:186`

## `stripe-android@23.15.0` Integration Delta

Crypto Onramp adds SamsungPayConfig constructor overloads, a samsungPayConfig setter, samsungPayIsReadyCallback, PaymentMethodSelection.SamsungPay, SamsungPay payment/display enum cases and Available/Unavailable result types. Unavailable exposes SamsungPayException. The exception exposes reason, optional Integer Samsung Pay error code, underlying error, code/documentation/developer/user messages; reasons distinguish configuration, SDK, readiness, presentation, platform-key, credential, setup, app-update, temporary and general operation failures.

These are compiled declarations, not verified behavior or complete Kotlin call recipes: signatures omit parameter names and generic callback types. Do not infer units/defaults, SDK version constraints, supported card brands, credential serialization or automatic retries. The release requires the merchant app to provide the Samsung Pay SDK. Configuration/availability/request/error implementation is excluded. Collection is not checkout/settlement, and this Onramp API does not establish Samsung Pay support in ordinary PaymentSheet.

Release notes announce LinkController returning an error when no funding sources exist rather than silently falling back to card, and Agrobank/MBSB Bank/Bank of China FPX support with alphabetical ordering. Retained implementation does not verify either finding. Crypto build adds a test Turbine dependency; PaymentSheet build adds Pixel 2/API 33/google_apis managed test-device configuration. These test settings do not raise the merchant minimum Android version or prove test execution. README/VERSION/gradle.properties only bump the release. All 4,744 prior changelog lines survive with nine new release lines.

### Grounding excerpts

> "Integrators must provide the Samsung Pay SDK in their application."
>
> `raw/github/stripe/stripe-android/releases/stripe-android/23.15.0/2026-09-29/release-notes.md` - CryptoOnramp bullet

> `public final class com/stripe/android/crypto/onramp/model/OnrampConfiguration$SamsungPayConfig {`
>
> `raw/github/stripe/stripe-android/snapshots/2026-09-29-03dc31c/files/crypto-onramp/api/crypto-onramp.api:368`

> `public final fun getError ()Lcom/stripe/android/crypto/onramp/exception/SamsungPayException;`
>
> `raw/github/stripe/stripe-android/snapshots/2026-09-29-03dc31c/files/crypto-onramp/api/crypto-onramp.api:673`

## `stripe-android@23.16.0` Additive Full Ingest

### Link Entry-Point Control

`PaymentSheet.LinkConfiguration.Display` adds `WalletButtonHidden`. The retained configuration maps `Automatic` to Link enabled/button shown, `Never` to Link disabled/button hidden, and `WalletButtonHidden` to Link enabled/button hidden. The new value's documentation retains returning-user and inline-signup flows; the analytics value is `wallet_button_hidden`. The public constructor and builder still default to `Automatic`. This proves configuration logic and the documented contract, not every downstream rendering or payment result. Review exhaustive enum switches when upgrading.

```kotlin
val linkConfiguration = PaymentSheet.LinkConfiguration.Builder()
    .display(PaymentSheet.LinkConfiguration.Display.WalletButtonHidden)
    .build()
// Supply this through the existing PaymentSheet configuration integration.
// Hiding the wallet entry is not the same as disabling Link.
```

### Address Defaults and Historical Attribution

Release notes announce inline address autocomplete enabled by default in PaymentSheet, FlowController and AddressElement. Its implementation is excluded, so credential/prerequisite handling, supported locations, fallback behavior and the exact first implementation release are not independently established. The new cumulative changelog repeats the announcement under 23.15.0 as a later annotation, absent from the retained 23.15.0 notes/changelog. Preserve both dated records rather than silently backdating the earlier ingest. Applications should regression-test billing/shipping collection; the announcement does not establish removal of Google Places requirements.

### Authenticated Onramp Wallet Deletion

Experimental `OnrampCoordinator.deleteWalletAddress(walletId: String)` is documented to delete the specified crypto wallet from the current Link account and require an authenticated Link user. The method delegates to `interactor.deleteWalletAddress(walletId)`. Public signatures expose `OnrampDeleteWalletAddressResult.Completed` and `Failed`, with the latter carrying a Throwable. The interactor/request/model implementation is excluded; no claims about authorization enforcement, idempotency, deletion propagation or retries are established. Registered-wallet deletion is not a crypto transfer or Link-account deletion.

### Compatibility and Evidence Limits

README/VERSION/gradle.properties advance to 23.16.0 without changing the documented baseline platform floors. PaymentSheet build adds a testParameterInjector test dependency, not a merchant runtime requirement or proof that tests ran. Compiled inventories add a generated Financial Connections lambda accessor and remove a generated NFC lambda accessor; these are recorded as generated UI artifacts, not promoted as merchant API recipes. All 4,753 prior changelog lines remain, with 16 insertions including the retrospective annotation. Full mode adds this knowledge to existing history; it does not replace earlier versions.

### Grounding excerpts

> "Inline address autocomplete is now enabled by default in PaymentSheet and FlowController."
>
> `raw/github/stripe/stripe-android/releases/stripe-android/23.16.0/2026-09-29/release-notes.md` - PaymentSheet bullet

> "Requires an authenticated Link user."
>
> `raw/github/stripe/stripe-android/snapshots/2026-09-29-a8d0e74/files/crypto-onramp/src/main/java/com/stripe/android/crypto/onramp/OnrampCoordinator.kt` - deleteWalletAddress documentation

> `Display.Never, Display.WalletButtonHidden -> false`
>
> `raw/github/stripe/stripe-android/snapshots/2026-09-29-a8d0e74/files/paymentsheet/src/main/java/com/stripe/android/paymentsheet/PaymentSheet.kt` - shouldShowButton getter

## `stripe-android@23.17.0` Additive Full Ingest

### Keyless Address Autocomplete Migration

The migration guide directs removal of `PaymentSheet.Configuration.Builder.googlePlacesApiKey`, `AddressLauncher.Configuration.Builder.googlePlacesApiKey`, or Google Places key constructor arguments. They are deprecated, not yet removed, and the guide says autocomplete continues without the merchant key, including for integrations that never supplied one. Retained PaymentSheet source adds a deprecation message and keeps the old setter callable; compiled AddressLauncher signatures retain existing overloads and add a shorter overload. Complete AddressLauncher implementation and autocomplete networking are excluded, so detailed provider/request/fallback behavior is not established.

```kotlin
// 23.17.0 migration: remove the old .googlePlacesApiKey(...) call.
val configuration = PaymentSheet.Configuration.Builder(merchantDisplayName)
    .build()
// Keep the rest of the merchant's customer/wallet/billing configuration.
```

The earlier 23.16.0 section records that release's narrower evidence and remains historical. The explicit keyless contract is now supported by the 23.17.0 migration guide; it does not prove the exact first runtime implementation release.

### Identity Styling and Binary Compatibility

`IdentityVerificationSheet.Configuration` adds `@get:ColorInt val brandColor: Int? = null`, documented for native primary-action buttons, alongside brandLogo. `@JvmOverloads` preserves the one-argument constructor. Compiled `copy(Uri)` and `copy$default` are replaced with signatures including nullable Integer, while component2/getBrandColor are added. Optional Kotlin source syntax does not make the old binary copy ABI compatible: recompile dependent artifacts and review Java calls. Rendering implementation is excluded.

```kotlin
val identityConfiguration = IdentityVerificationSheet.Configuration(
    brandLogo = logoUri,
    brandColor = android.graphics.Color.rgb(20, 110, 80),
)
// Existing one-argument construction remains available.
```

### Scoped Platform Floors and Announcements

Both `identity/build.gradle` and `crypto-onramp/build.gradle` set `minSdkVersion 24`. Identity adds MediaPipe Tasks Vision; dependencies.gradle defines version 0.10.35. This is a production module requirement, unlike earlier managed test-device configuration, and must not be generalized to all SDK modules: the top-level README still documents API 23 for the general SDK. Integrators using Identity or Onramp should update their app floor and test the affected flow.

Release notes announce guided 3D selfie capture with left/right poses for supported verification sessions and Alipay SetupIntent support through direct APIs. The selfie capture and Alipay implementation are excluded, so exact eligible session types, capture/permission/failure details and direct confirmation recipes are not proven by this evidence. A generated Express Checkout lambda declaration is not a supported merchant entry-point recipe; generated Identity selfie UI declarations disappear without proving the flow was removed.

### Historical Attribution

The new cumulative changelog inserts the Identity/Onramp API 24 statement under 23.15.0, absent from that older retained build evidence. Record the later attribution separately from the observed 23.16.0 -> 23.17.0 build boundary. All 4,769 prior changelog lines survive with 14 insertions; all prior migration content survives with five inserted lines. Older knowledge is retained rather than replaced.

### Grounding excerpts

> "Address autocomplete continues to work without a Google Places API key, and integrations that did not provide one receive autocomplete automatically."
>
> `raw/github/stripe/stripe-android/snapshots/2026-09-29-93ef69a/files/MIGRATING.md` - Migrating from versions < 23.17.0

> `@get:ColorInt val brandColor: Int? = null`
>
> `raw/github/stripe/stripe-android/snapshots/2026-09-29-93ef69a/files/identity/src/main/java/com/stripe/android/identity/IdentityVerificationSheet.kt` - Configuration

> `minSdkVersion 24`
>
> `raw/github/stripe/stripe-android/snapshots/2026-09-29-93ef69a/files/identity/build.gradle` and `crypto-onramp/build.gradle` - defaultConfig

## `stripe-android@23.17.1` Additive Full Ingest

### Announced Checkout Fixes

The release notes announce three PaymentSheet fixes:

- Klarna billing-address fields update after a country change.
- Wero no longer displays duplicate country fields during full billing-address collection.
- Selecting `Not you?` during Link 2FA fully logs out the previous account, fixing blocked subsequent logins.

These are upstream announcements, not independently verified implementation behavior: changed billing-form and Link logout internals are excluded. Regression-test the affected address/account-switch paths; no additional assumptions about backend sessions, credential invalidation, retries or settlement follow from these notes.

### Generated Binding Compatibility

The compiled PaymentSheet inventory removes `com.stripe.android.paymentsheet.databinding.StripeGooglePayButtonBinding` entirely, including Google Pay layout/button fields, bind/inflate methods and getRoot. A direct caller's old references are no longer represented in the retained public inventory; that concrete source/binary risk justified the approved full-mode override. Do not adopt generated binding classes as merchant integration entry points. This removal is not evidence that Google Pay support was removed: the existing public launcher evidence remains unchanged, and this release's README still lists Google Pay.

Identity's compiled inventory adds `ComposableSingletons$IdentityTopAppBarKt` and its generated lambda accessor; that alone establishes no new merchant-facing feature. README/VERSION/gradle.properties advance to 23.17.1. Prior platform, keyless-address, Identity styling/copy and module-floor findings remain version-qualified. All 4,783 prior changelog lines remain with seven inserted lines; no retrospective edit was found in this comparison.

### Grounding excerpts

> "Fixed an issue where Klarna billing address fields did not update when the country changed."
>
> `raw/github/stripe/stripe-android/releases/stripe-android/23.17.1/2026-09-29/release-notes.md:2`

> "Fixed an issue where Wero displayed duplicate country fields when collecting a full billing address."
>
> `raw/github/stripe/stripe-android/releases/stripe-android/23.17.1/2026-09-29/release-notes.md:3`

> `public final class com/stripe/android/paymentsheet/databinding/StripeGooglePayButtonBinding : androidx/viewbinding/ViewBinding {`
>
> `raw/github/stripe/stripe-android/snapshots/2026-09-29-93ef69a/files/paymentsheet/api/paymentsheet.api:2212` - prior declaration; absent from the current API inventory

## `stripe-android@23.18.0` Additive Full Ingest

### Six PaymentSheet Support Announcements and API Additions

Release notes announce support for SeQura, PAYCO, Korean cards, Naver Pay, Kakao Pay and Scalapay. The compiled payments-core API directly adds `PaymentMethod.Type.Sequra`, `Payco`, `KrCard`, `NaverPay`, `KakaoPay` and `Scalapay`. `PaymentMethodCreateParams` and its Companion expose matching `createSequra`, `createPayco`, `createKrCard`, `createNaverPay`, `createKakaoPay` and `createScalapay` overloads: no arguments, BillingDetails, BillingDetails plus Map, and BillingDetails plus Map plus AllowRedisplay. Companion also exposes synthetic default helpers. No prior payments-core inventory line was removed.

These signatures establish API presence, not default argument values, field requirements, serialized codes or a complete integration recipe. Actual PaymentSheet selection, form generation, redirect/next-action handling and current model serialization are excluded. Merchant enablement, country/currency and recurring/mandate eligibility must not be inferred. Review exhaustive enum switches and test applicable configured payment methods. General BNPL and Korean-method knowledge stays in [[stripe-bnpl]] and [[stripe-korea-payment-methods]] rather than being rewritten from SDK declarations.

### Address Provider and Build Changes

AddressElement release notes now specify Stripe-hosted autocomplete by default. Preserve this provider-specific announcement alongside 23.16.0's default-inline-autocomplete record and 23.17.0's explicit keyless migration. The request/fallback implementation remains excluded; this does not prove the exact first provider-switch release, universal address coverage or fallback behavior.

`dependencies.gradle` changes `com.google.android.gms:play-services-wallet` from 19.5.0 to 20.0.0. It is a dependency declaration, not proof of a changed minimum Android floor or runtime Google Pay behavior. The root build removes a TapToAdd instrumentation-test exclusion; that is test configuration, not a payment feature or evidence of test execution. README/VERSION/gradle.properties advance to 23.18.0; earlier scoped Identity/Onramp API 24 floors remain historical.

### Onramp KYC Types and Identity Restriction

The compiled Onramp inventory adds `IdType` values CanadianSocialInsuranceNumber, ColombianTaxIdentificationNumber, PhilippinesTaxpayerIdentificationNumber and SocialSecurityNumber. `KycInfo` gains getIdType and constructor overloads containing IdType while retaining previous constructors. Signatures alone do not establish parameter names/defaults, identifier format validation, serialization or supported geography: model/request internals remain excluded. See [[stripe-crypto-onramp]].

Identity's retained source adds nullable `Configuration.biometricConsent`, default null, documented to use the default consent header when null. Its getter/setter and nested Parcelable `BiometricConsentConfiguration(hideBrandingHeader: Boolean)` are restricted to LIBRARY_GROUP. This is not a supported general merchant API; excluded rendering code is not independently verified. The property lives outside Configuration's primary constructor, so this source does not place it in the generated data-class copy/equality contract. Existing brandLogo/brandColor construction and prior version-qualified copy-compatibility findings are retained.

### Historical Attribution

All 4,790 prior cumulative changelog lines survive, with sixteen inserted lines. Thirteen introduce 23.18.0; three add an Onramp KYC note under 23.17.1. Those IdType/getIdType declarations and that note were absent from the retained 23.17.1 evidence. Preserve the later upstream attribution separately from the observed 23.17.1 -> 23.18.0 API boundary; neither proves the exact first implementation release. Additive full ingest retains all previous version knowledge.

### Grounding excerpts

> "Added support for SeQura."
>
> `raw/github/stripe/stripe-android/releases/stripe-android/23.18.0/2026-09-29/release-notes.md:2`

> "Use Stripe-hosted address autocomplete by default."
>
> `raw/github/stripe/stripe-android/releases/stripe-android/23.18.0/2026-09-29/release-notes.md:10`

> `public final fun getIdType ()Lcom/stripe/android/crypto/onramp/model/IdType;`
>
> `raw/github/stripe/stripe-android/snapshots/2026-09-29-f5e7f5c/files/crypto-onramp/api/crypto-onramp.api:258`

## `stripe-android@23.19.0` Additive Full Ingest

### Returning-User Link Visibility Contract

The retained `PaymentSheet.LinkConfiguration.Display.WalletButtonHidden` documentation now says Link remains enabled, including automatic verification and inline sign-up, and its button/row is shown when an existing Link user is detected but hidden otherwise. `shouldDisplay` continues to return true for this mode and false for Never; constructor/builder defaults remain Automatic. The earlier internal `shouldShowButton` getter, which returned false for WalletButtonHidden, is removed. Compiled public API inventories are unchanged: this is not an observed public signature break.

> [!warning] Contradiction
> The earlier 23.16.0 through retained 23.18.0 source documented an always-hidden Link button/row. The 23.19.0 source documents conditional visibility for detected existing users. Preserve the older section and code example as historical; do not infer that the enum name guarantees unconditional hiding in 23.19.0. [[stripe-android-sdk]] records the same version distinction.

Detection and downstream rendering implementation remain excluded. The declaration/documentation change does not prove how users are detected, when UI updates, what happens on account switching or whether a specific device shows the button. Regression-test existing-user, new-user and account-switch cases; do not equate enabled Link or SDK completion with successful payment/settlement. [[stripe-link]] holds the native contract separately from web integration behavior.

### Localization, Race Fix and Resource Shrinking

Release notes announce Welsh (United Kingdom), Arabic (Saudi Arabia), and a rare PaymentSheet race-condition fix for a half-visible sheet. README adds Welsh to its localization list but omits Arabic; this is differing documentation coverage, not proof that Arabic is absent from the SDK. Locale resources and presentation/race-fix internals are excluded, so translations, RTL behavior and the actual fix are not independently verified.

Gradle sets `android.r8.optimizedResourceShrinking=true` and updates VERSION_NAME; README/VERSION advance to 23.19.0. This is build-configuration evidence, not a measured app-size improvement, successful release build, changed device floor or verified runtime behavior. All 4,806 prior raw changelog lines survive with nine inserted release lines and no retrospective rewrite in this comparison. Full mode adds the new contract and preserves all older knowledge.

### Grounding excerpts

> "Its button or row is shown when an existing Link user is detected and hidden otherwise."
>
> `raw/github/stripe/stripe-android/snapshots/2026-09-29-a95cc0e/files/paymentsheet/src/main/java/com/stripe/android/paymentsheet/PaymentSheet.kt:3769`

> "Added Arabic (Saudi Arabia) localization."
>
> `raw/github/stripe/stripe-android/releases/stripe-android/23.19.0/2026-09-29/release-notes.md:3`

> "Fixed a rare race condition which could result in the payment sheet being half-visible on screen."
>
> `raw/github/stripe/stripe-android/releases/stripe-android/23.19.0/2026-09-29/release-notes.md:6`

## `stripe-android@23.20.0` Integration Delta

### Bizum and Next-Action Declarations

PaymentSheet release notes announce Bizum support. The compiled payments-core API adds `PaymentMethod.Type.Bizum` and `StripeIntent.NextActionType.AwaitAuthorization`, without removing prior declarations. These are observed enum additions, not proof that every account supports Bizum or that AwaitAuthorization always belongs to Bizum. Model serialization, next-action processing and PaymentSheet forms/routing are excluded. Review exhaustive switches and independently verify merchant enablement and flow prerequisites; no authorization timeout, recurring eligibility or payment/settlement guarantee follows from these signatures.

Release notes also announce fixes for Alipay+ and Alipay SDK redirects. Their changed implementations are excluded, so exact redirect/fallback/callback behavior is not independently verified. Preserve the earlier version-qualified Alipay findings rather than merging distinct fixes.

### Google Pay Repository Configuration

The complete current/prior GooglePayLauncher source shows a new explicit `googlePayConfig = GooglePayConfig(context)` argument in four repository-factory paths: ordinary Activity, library-group-restricted React Native Activity, Fragment and Compose. Existing readiness initialization remains asynchronous through `repository.isReady().first()`; presentation still checks `isReady`, and SetupIntent presentation still requires a currency code. Public launcher signatures are unchanged. This is an internal construction change, not a new merchant call requirement.

GooglePayConfig and DefaultGooglePayRepository implementations are not retained. Do not infer exact publishable-key/connected-account handling, tokenization data, the prior constructor default, or changed readiness outcomes. Regression-test affected wallet paths; no device or payment execution was performed.

Financial Connections adds `testImplementation testLibs.androidx.composeUi`; this is test configuration, not a merchant runtime dependency or new device floor. README/VERSION/gradle.properties advance the release version. PaymentSheet API adds a generated NFC close-button lambda accessor, not a merchant-facing integration feature. All 4,815 prior raw changelog lines survive with eight inserted release lines and no retrospective edits; all older wiki history remains intact.

### Grounding excerpts

> "Added support for Bizum."
>
> `raw/github/stripe/stripe-android/releases/stripe-android/23.20.0/2026-09-29/release-notes.md:5`

> `public static final field AwaitAuthorization Lcom/stripe/android/model/StripeIntent$NextActionType;`
>
> `raw/github/stripe/stripe-android/snapshots/2026-09-29-d47cf89/files/payments-core/api/payments-core.api:3687`

> `googlePayConfig = GooglePayConfig(context),`
>
> `raw/github/stripe/stripe-android/snapshots/2026-09-29-d47cf89/files/payments-core/src/main/java/com/stripe/android/googlepaylauncher/GooglePayLauncher.kt:89` - also at 134, 183 and 423

## `stripe-android@23.21.0` Additive Full Ingest

### Host-Owned PaymentSheet Callback Identity

Activity and Fragment constructors/builders now retrieve StoreViewModel from the host ViewModelProvider. Its getter reuses a SavedStateHandle value or generates a UUID, saves it under PAYMENTSHEET_ID and returns it. The identifier is passed to DefaultPaymentSheetLauncher and used as the PaymentElementCallbackReferences key; the prior source used PAYMENT_SHEET_DEFAULT_CALLBACK_IDENTIFIER. FlowController's callback setter still uses its separate default identifier. Public constructor/builder signatures remain represented in the compiled inventory.

This is host-owned identity, not evidence that every PaymentSheet instance gets an independent key. Multiple sheets under the same owner can retrieve the same ViewModel; do not claim guaranteed isolation, callback redelivery or successful process restoration. The concrete launcher, callback registry and internal Compose helper are excluded. Preserve lifecycle registration and test deferred/custom/external callbacks across recreation, navigation and multiple hosts; no device execution was performed.

Generated public inventories also remove ComposableSingletons$UserAttestationScreenKt and replace the ExpressCheckoutElementContentKt lambda getter (Function4 -> Function5 with a changed generated name), while adding an NFC scanning accessor. Direct references have source/binary compatibility risk; generated classes are not merchant entry points. Their removal is not evidence that user attestation or Express Checkout features were removed.

### Embedded API Configuration Preview

Release notes announce EmbeddedPaymentElement.Configuration.apiConfiguration in public preview for publishable key and Stripe account ID. The compiled builder adds apiConfiguration(ApiConfiguration) and ApiConfigurationPreview. The retained example opts into the preview, fetches checkout data before configure on its optional preview path, skips global PaymentConfiguration.init on that path and supplies ApiConfiguration from the returned publishable key. It keeps the prefetched CreateIntentResult for its existing deferred callback. The default non-preview path still initializes global configuration through checkout.

```kotlin
// Excerpt of the retained preview example; not a complete checkout integration.
@OptIn(ApiConfigurationPreview::class)
fun configureEmbedded(publishableKey: String) =
    EmbeddedPaymentElement.Configuration.Builder("Powdur")
        .apiConfiguration(ApiConfiguration(publishableKey))
        .build()
```

This illustrative excerpt was not compiled or run. The example does not supply a connected-account ID; announcement and API presence do not prove its detailed request behavior. ApiConfiguration implementation and EmbeddedPaymentElement configuration/request internals are excluded. Do not infer automatic credential rotation or tenant isolation.

PaymentSheet source separately adds internal nullable ApiConfiguration.State, initialized to null, a library-group-restricted builder setter, forwarding during build and reconstruction in newBuilder. Its documentation states that omitted configuration uses PaymentConfiguration credentials. This restricted PaymentSheet/FlowController surface is not the publicly announced Embedded preview API; it is not a supported general merchant customization recipe.

### Financial Connections Consent and Error Contracts

FinancialConnectionsSheet adds present(configuration, preCollectedConsent: FinancialConnectionsPreCollectedConsent?). The old present(configuration) remains and delegates with null. Source documentation describes previously merchant-collected consent to link an account; conversion forwards it into internal configuration without changing the retained key/session/account fields. The consent type, legal sufficiency, validation, persistence and server propagation are excluded: do not infer skipped consent UI or universal eligibility.

Compiled CollectBankAccountLauncher adds consent-taking PaymentIntent/SetupIntent overloads plus default helpers, retaining old calls. New abstract interface methods mean custom implementers should recompile/review implementations; signature additions alone are not blanket compatibility proof. The launcher implementation is excluded. Financial Connections also exposes NO_ELIGIBLE_ACCOUNTS. Notes announce preserving no_eligible_accounts instead of unexpected_error in onEvent and suppressing background authorization-session telemetry failures from those callbacks. Error mapping/telemetry implementation is excluded; treat these as announcements, not independently executed results.

### Onramp, Payment Methods and Historical Attribution

Experimental OnrampCoordinator.Presenter adds presentTermsAndConditionsIfNeeded and presentTermsOfServiceIfNeeded. Both require an authenticated Link user by documentation; call the first before checkout and the second during onboarding after authentication. They delegate to the presenter coordinator and use corresponding OnrampCallbacks. Compiled API adds those hooks and OnrampPartnerTermsResult variants Accepted, Cancelled, Failed with Throwable, and NotRequired. Enforcement, persistence, UI, versioned acceptance and retry internals are excluded. See [[stripe-crypto-onramp]]; terms acceptance is not payment completion.

Notes announce MB WAY support and a fix for rejecting valid card numbers in BIN ranges with differing PAN lengths, including some 16-digit UnionPay cards. Compiled payments-core directly adds PaymentMethod.Type.MbWay and StripeIntent.NextActionType.MbWayAwaitAuthorization. Selection/next-action/card-validation implementations are excluded, so eligibility, waiting duration and the exact validation algorithm are not established. Review exhaustive enum switches and test configured methods; don't assume authorization or settlement merely from SDK completion.

The current raw changelog has 4,843 lines versus 4,823 previously: 23 inserted lines and three removed/moved lines. Thirteen introduce 23.21.0; three add an Identity background-color fix under 23.20.0; four add Onramp terms methods under 23.19.0; three place the KYC note under 23.18.0, removing the identical three-line block from 23.17.1. The Identity fix implementation is excluded. README/VERSION/gradle.properties only advance the release; earlier scoped module floors remain intact.

> [!warning] Contradiction
> The 23.18.0 ingest above records the earlier raw changelog's retrospective KYC attribution to 23.17.1. The 23.21.0 raw changelog moves it to 23.18.0 and backdates terms methods to 23.19.0, although retained terms API/source through 23.20.0 lacked them. Keep those prior records and the observed 23.20.0 -> 23.21.0 terms boundary separately; neither label alone proves the exact first implementation release. [[stripe-android-sdk]] and [[stripe-crypto-onramp]] record the same distinction.

### Grounding excerpts

> `savedStateHandle[ID_KEY] = storeId`
>
> `raw/github/stripe/stripe-android/snapshots/2026-09-29-a074a95/files/paymentsheet/src/main/java/com/stripe/android/paymentsheet/PaymentSheet.kt:4587`

> "Call this before checkout."
>
> `raw/github/stripe/stripe-android/snapshots/2026-09-29-a074a95/files/crypto-onramp/src/main/java/com/stripe/android/crypto/onramp/OnrampCoordinator.kt:288`

> `present(configuration = configuration, preCollectedConsent = null)`
>
> `raw/github/stripe/stripe-android/snapshots/2026-09-29-a074a95/files/financial-connections/src/main/java/com/stripe/android/financialconnections/FinancialConnectionsSheet.kt:49`

> `@OptIn(ApiConfigurationPreview::class)`
>
> `raw/github/stripe/stripe-android/snapshots/2026-09-29-a074a95/files/paymentsheet-example/src/main/java/com/stripe/android/paymentsheet/example/playground/embedded/EmbeddedExampleActivity.kt:64`

## Google Pay

`GooglePayLauncher` checks device readiness before it can present. It confirms PaymentIntents or SetupIntents and returns `Completed`, `Canceled`, or `Failed`. SetupIntent use requires a currency code for the Google Pay request even though Stripe's SetupIntent object does not require one.

Configuration includes environment, merchant country/name, email and billing-address collection, existing-method readiness, credit-card acceptance, and selected extra networks. `GooglePayPaymentMethodLauncher` supports PaymentMethod-only collection for custom flows.

## Specialized Product Modules

### Connect

`EmbeddedComponentManager` is initialized with a publishable key and a callback that fetches a server-created client secret. It creates Account Onboarding, Payments, and Payouts components and can update appearance. Activity lifecycle registration is mandatory for every Activity that hosts an embedded component. The cumulative changelog records Payments and Payouts as generally available in `23.12.0`.

### Financial Connections

`FinancialConnectionsSheet` presents bank-account linking and returns session data or token-oriented results. Its launcher must be registered unconditionally during Activity or Fragment initialization. Configuration includes a Financial Connections session client secret, publishable key, and optional connected-account ID.

### Identity

`IdentityVerificationSheet` supports Activity, Fragment, and Compose hosts. Presentation requires a verification-session ID and ephemeral-key secret, both supplied from a merchant backend. Results are `Completed`, `Canceled`, or `Failed`.

### Crypto Onramp

The experimental `OnrampCoordinator` covers Link account discovery and authentication, KYC, compliance identifiers, wallet registration and ownership challenges, payment-method collection, crypto payment-token creation, and checkout. Public source does not imply general merchant access.

### Payment Method Messaging

The public-preview Compose element displays BNPL promotional messaging. Amount and currency are required; locale, country, and Affirm/Afterpay-Clearpay/Klarna selection are optional. Configuration can succeed with content, succeed with `NoContent`, or fail.

### Card Scanning

The retained direct `CardScanSheet` types are library-group restricted. The changelog records Stripe card scanning returning in public preview in `23.6.0` through Stripe UI surfaces. This is distinct from treating the restricted classes as a supported direct merchant API.

## Platform and Migration Requirements

| Requirement | `23.13.1` baseline |
| --- | --- |
| Android | 6.0 / API 23+ |
| `compileSdkVersion` | 36+ |
| Android Gradle Plugin | 8.13.2 |
| Gradle | 9.3.1 |
| Kotlin | 2.3.10 |
| Jetpack Compose | 1.10.x for SDK 23.x |

The v23 migration raises the Android and SDK floors. The v22 migration removes legacy payment methods and token-oriented APIs, 3DS1, old Google Pay launchers, and accidentally public internals while moving public configuration toward builders. The v21 migration removes Basic Integration in favor of Mobile Payment Element.

## Version History

### `stripe-android@23.21.0`

Published 2026-09-28; additive full override with focused reading approved for callback/lifecycle and generated compatibility changes. Adds Embedded preview example, consent/terms contracts and qualified payment/error announcements. Preserves moved/retrospective changelog attribution and all earlier knowledge; see [[changelog-github-stripe-android]].

### `stripe-android@23.20.0`

Published 2026-09-21; approved focused-reading delta adds Bizum/next-action declarations and explicit internal Google Pay configuration, distinguishing Alipay announcements from retained implementation. Older history remains; see [[changelog-github-stripe-android]].

### `stripe-android@23.19.0`

Published 2026-09-15; approved additive full mode with focused reading for revised returning-user Link visibility. Public signatures remain unchanged; conditional UI contract, qualified localization/race-fix announcements and resource-shrinking setting are recorded without replacing earlier history. See [[changelog-github-stripe-android]].

### `stripe-android@23.18.0`

Published 2026-09-08; approved additive full mode with focused reading for six announced PaymentSheet methods and the address provider default. Adds directly observed API/KYC declarations and restricted Identity source contract, with implementation gaps and retrospective attribution kept explicit. Older history remains intact. See [[changelog-github-stripe-android]].

### `stripe-android@23.17.1`

Published 2026-08-31; approved full override with focused reading for generated binding binary removal. Records announcement-qualified Klarna/Wero/Link fixes without replacing prior architecture or history. See [[changelog-github-stripe-android]].

### `stripe-android@23.17.0`

Published 2026-08-24; full override with focused reading approved for Identity binary-copy incompatibility and Identity/Onramp API 24 floors. Adds keyless-autocomplete migration and styling contracts, qualified Alipay/selfie announcements and historical attribution notes. Earlier findings remain queryable. See [[changelog-github-stripe-android]].

### `stripe-android@23.16.0`

Published 2026-08-18; additive full mode approved over the generated delta recommendation because of announced defaults across three UI surfaces. Focused reading preserves unchanged evidence and all older knowledge. Adds Link entry-point control and wallet-deletion contracts; autocomplete remains announcement-qualified. See [[changelog-github-stripe-android]].

### `stripe-android@23.15.0`

Published 2026-08-10; approved focused-reading delta from stripe-android@23.14.0. Adds optional Onramp wallet contracts and clearly qualified release announcements. Older knowledge remains; see [[changelog-github-stripe-android]].

### `stripe-android@23.14.0`

Published 2026-08-03. Approved bounded delta from stripe-android@23.13.1 with focused reading; records additive preview contracts and distinguishes the later historical annotation. Earlier knowledge remains intact. See [[changelog-github-stripe-android]]; this is ingest progress, not a latest-upstream claim.

### `stripe-android@23.13.1`

The exact patch fixes Alipay test-mode reconciliation and closeout. It does not introduce the broader baseline architecture summarized above.

### Accumulated `23.9.0--23.13.0` Context

- `23.9.2` enriches payment/setup confirmation errors with error code, decline code, and error type and expands Crypto Onramp diagnostics.
- `23.10.0--23.11.0` adds Identity manual capture and changes EU Crypto Onramp compliance/attestation contracts.
- `23.12.0` marks Connect Payments and Payouts embedded components generally available and adds a private-preview standalone Link controller.
- `23.13.0` localizes declined-card errors from 3DS2 flows and changes private-preview Link SetupIntent confirmation to an explicit post-selection step.

These milestones come from the retained cumulative changelog, not automated comparisons against every intermediate release.

### Legacy `stripe-android@23.8.0`

The May 2026 manual capsule established PaymentSheet, FlowController, CustomerSheet, Embedded Payment Element, the `Stripe` client, Google Pay, 3DS2 configuration, models, and the platform requirements. Those findings remain queryable and are extended rather than replaced by this baseline.

## Integration Guidance

- Prefer PaymentSheet for a maintained prebuilt checkout, FlowController for merchant-owned confirmation UI, and Embedded Payment Element for inline payment-method UI.
- Create Intents and session credentials on the backend; return only publishable configuration and client secrets to the app.
- Treat `Completed` as completion of the SDK interaction, not settlement evidence; fulfill from successful server-side events.
- Register Activity Result based launchers during the host initialization path, before attempting presentation.
- Verify payment-method, country, currency, connected-account, and preview eligibility independently of public API presence.
- Review `MIGRATING.md` before a major upgrade and regression-test Compose, Google Pay, 3DS, delayed methods, and process recreation.
- For Android digital goods, verify current Google Play and regional billing policy in addition to SDK capability.

## Related

- Company: [[stripe]]
- Concept: [[stripe-android-sdk]]
- Native counterpart: [[source-github-stripe-ios]]
- React Native bridge: [[source-github-stripe-react-native]]
- History: [[changelog-github-stripe-android]]

## Raw Sources

- `raw/github/stripe/stripe-android/snapshots/2026-09-29-a074a95/manifest.json` - exact-SHA 23.21.0 capsule; unchanged expanded inventory hash-checked
- `raw/github/stripe/stripe-android/releases/stripe-android/23.21.0/2026-09-29/manifest.json` - package release/publication identity
- `raw/github/stripe/stripe-android/releases/stripe-android/23.21.0/2026-09-29/release-notes.md` - payment/preview/error announcements
- `tracking/github/repos/stripe/stripe-android/comparisons/stripe-android/23.20.0--23.21.0/comparison.json` - adjacent comparison.md/diff.patch
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-a074a95/files/paymentsheet/src/main/java/com/stripe/android/paymentsheet/PaymentSheet.kt` - affected constructor/builder/configuration/store blocks; prior context at d47cf89
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-a074a95/files/paymentsheet/api/paymentsheet.api` - preview and generated compatibility declarations in enclosing blocks
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-a074a95/files/paymentsheet-example/src/main/java/com/stripe/android/paymentsheet/example/playground/embedded/EmbeddedExampleActivity.kt` - complete current/prior Embedded example
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-a074a95/files/financial-connections/src/main/java/com/stripe/android/financialconnections/FinancialConnectionsSheet.kt` - complete current source and prior affected consent-free path
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-a074a95/files/financial-connections/api/financial-connections.api` - consent/error declarations in enclosing blocks
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-a074a95/files/payments-core/api/payments-core.api` - method/next-action/bank-collection declarations in enclosing blocks
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-a074a95/files/crypto-onramp/src/main/java/com/stripe/android/crypto/onramp/OnrampCoordinator.kt` - complete current source and prior Presenter context
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-a074a95/files/crypto-onramp/api/crypto-onramp.api` - terms hooks/results in enclosing blocks
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-a074a95/files/CHANGELOG.md` - release additions and moved/backdated notes; unchanged history mechanically checked
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-d47cf89/manifest.json` - exact-SHA 23.20.0 capsule; unchanged inventory hash-checked
- `raw/github/stripe/stripe-android/releases/stripe-android/23.20.0/2026-09-29/manifest.json` - package-qualified release/publication
- `raw/github/stripe/stripe-android/releases/stripe-android/23.20.0/2026-09-29/release-notes.md` - Bizum and Alipay redirect announcements
- `tracking/github/repos/stripe/stripe-android/comparisons/stripe-android/23.19.0--23.20.0/comparison.json` - adjacent comparison.md/diff.patch
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-d47cf89/files/payments-core/src/main/java/com/stripe/android/googlepaylauncher/GooglePayLauncher.kt` - complete current/prior launcher read; prior source at a95cc0e
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-d47cf89/files/payments-core/api/payments-core.api` - new enum declarations in enclosing blocks
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-d47cf89/files/financial-connections/build.gradle` - test-only dependency
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-a95cc0e/manifest.json` - exact-SHA 23.19.0 snapshot; unchanged full inventory hash-checked
- `raw/github/stripe/stripe-android/releases/stripe-android/23.19.0/2026-09-29/manifest.json` - package-qualified release/publication
- `raw/github/stripe/stripe-android/releases/stripe-android/23.19.0/2026-09-29/release-notes.md` - announced localization and presentation fix
- `tracking/github/repos/stripe/stripe-android/comparisons/stripe-android/23.18.0--23.19.0/comparison.json` - adjacent comparison.md/diff.patch
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-a95cc0e/files/paymentsheet/src/main/java/com/stripe/android/paymentsheet/PaymentSheet.kt` - complete changed LinkConfiguration block; prior block read from 23.18.0
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-a95cc0e/files/README.md` - localization list and unchanged platform requirements
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-a95cc0e/files/gradle.properties` - resource-shrinking declaration
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-f5e7f5c/manifest.json` - exact-SHA 23.18.0 snapshot; unchanged full inventory hash-checked
- `raw/github/stripe/stripe-android/releases/stripe-android/23.18.0/2026-09-29/manifest.json` - package release identity/publication
- `raw/github/stripe/stripe-android/releases/stripe-android/23.18.0/2026-09-29/release-notes.md` - PaymentSheet methods and AddressElement provider announcements
- `tracking/github/repos/stripe/stripe-android/comparisons/stripe-android/23.17.1--23.18.0/comparison.json` - adjacent comparison.md/diff.patch
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-f5e7f5c/files/payments-core/api/payments-core.api` - new method declarations in retained context
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-f5e7f5c/files/crypto-onramp/api/crypto-onramp.api` - IdType/KycInfo declarations; affected prior block compared
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-f5e7f5c/files/identity/src/main/java/com/stripe/android/identity/IdentityVerificationSheet.kt` - restricted consent-header source contract; prior source read
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-f5e7f5c/files/dependencies.gradle` - Play Services Wallet declaration
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-f5e7f5c/files/build.gradle` - removed test exclusion
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-f5e7f5c/files/CHANGELOG.md` - additions reviewed; unchanged history mechanically preserved
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-c5f31a3/manifest.json` - exact-SHA 23.17.1 snapshot; unchanged evidence hash-checked
- `raw/github/stripe/stripe-android/releases/stripe-android/23.17.1/2026-09-29/manifest.json` - package release identity/publication
- `raw/github/stripe/stripe-android/releases/stripe-android/23.17.1/2026-09-29/release-notes.md` - announced checkout fixes
- `tracking/github/repos/stripe/stripe-android/comparisons/stripe-android/23.17.0--23.17.1/comparison.json` - adjacent comparison.md/diff.patch
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-c5f31a3/files/paymentsheet/api/paymentsheet.api` - removed binding boundary; affected prior declaration read in full
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-c5f31a3/files/identity/api/identity.api` - added generated top-app-bar declaration
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-c5f31a3/files/README.md` - release version and Google Pay listing
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-93ef69a/manifest.json` - 23.17.0 snapshot; unchanged evidence hash-checked
- `raw/github/stripe/stripe-android/releases/stripe-android/23.17.0/2026-09-29/manifest.json` - package release identity/publication
- `raw/github/stripe/stripe-android/releases/stripe-android/23.17.0/2026-09-29/release-notes.md` - migration and capability announcements
- `tracking/github/repos/stripe/stripe-android/comparisons/stripe-android/23.16.0--23.17.0/comparison.json` - adjacent comparison.md/diff.patch
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-93ef69a/files/MIGRATING.md` - new migration section; unchanged history mechanically checked
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-93ef69a/files/identity/src/main/java/com/stripe/android/identity/IdentityVerificationSheet.kt` - configuration/source contract
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-93ef69a/files/identity/api/identity.api` - changed configuration signatures
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-93ef69a/files/identity/build.gradle` - module floor and production dependency
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-93ef69a/files/crypto-onramp/build.gradle` - scoped module floor
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-93ef69a/files/dependencies.gradle` - changed MediaPipe declarations in retained context
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-a8d0e74/manifest.json` - exact-SHA 23.16.0 capsule; unchanged content hash-checked under the exception
- `raw/github/stripe/stripe-android/releases/stripe-android/23.16.0/2026-09-29/manifest.json` - release identity/publication
- `raw/github/stripe/stripe-android/releases/stripe-android/23.16.0/2026-09-29/release-notes.md` - announced defaults and additions
- `tracking/github/repos/stripe/stripe-android/comparisons/stripe-android/23.15.0--23.16.0/comparison.json` - adjacent comparison.md/diff.patch
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-a8d0e74/files/paymentsheet/src/main/java/com/stripe/android/paymentsheet/PaymentSheet.kt` - changed LinkConfiguration context
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-a8d0e74/files/crypto-onramp/src/main/java/com/stripe/android/crypto/onramp/OnrampCoordinator.kt` - wallet-deletion contract/delegation
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-a8d0e74/files/crypto-onramp/api/crypto-onramp.api` - changed result signatures in context
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-a8d0e74/files/README.md` - unchanged platform requirements and updated dependency version
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-03dc31c/manifest.json` - exact-SHA 23.15.0 capsule
- `raw/github/stripe/stripe-android/releases/stripe-android/23.15.0/2026-09-29/manifest.json` - release identity/publication
- `raw/github/stripe/stripe-android/releases/stripe-android/23.15.0/2026-09-29/release-notes.md` - announcements
- `tracking/github/repos/stripe/stripe-android/comparisons/stripe-android/23.14.0--23.15.0/comparison.json` - adjacent comparison.md/diff.patch
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-03dc31c/files/crypto-onramp/api/crypto-onramp.api` - changed Samsung Pay declarations in context
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-03dc31c/files/crypto-onramp/build.gradle` - test dependency
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-03dc31c/files/paymentsheet/build.gradle` - managed test-device configuration
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-f286cb8/manifest.json` - exact-SHA 23.14.0 capsule
- `raw/github/stripe/stripe-android/releases/stripe-android/23.14.0/2026-09-29/manifest.json` - release identity/publication
- `raw/github/stripe/stripe-android/releases/stripe-android/23.14.0/2026-09-29/release-notes.md` - announcements
- `tracking/github/repos/stripe/stripe-android/comparisons/stripe-android/23.13.1--23.14.0/comparison.json` - comparison; adjacent comparison.md and diff.patch
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-f286cb8/files/paymentsheet/api/paymentsheet.api` - changed Link declarations in context
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-f286cb8/files/crypto-onramp/api/crypto-onramp.api` - Tempo enum declaration
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-f286cb8/files/CHANGELOG.md` - release block and later historical annotation
- `raw/github/stripe/stripe-android/snapshots/2026-07-31-dc874ce/manifest.json` - exact-SHA `23.13.1` bounded source capsule
- `raw/github/stripe/stripe-android/releases/stripe-android/23.13.1/2026-07-31/manifest.json` - package-qualified release record
- `raw/github/stripe/stripe-android/releases/stripe-android/23.13.1/2026-07-31/release-notes.md` - exact upstream release note
- `raw/github/stripe/stripe-android/snapshots/2026-07-31-dc874ce/files/README.md` - purpose, security boundary, requirements, installation, and supported surfaces
- `raw/github/stripe/stripe-android/snapshots/2026-07-31-dc874ce/files/MIGRATING.md` - major-version migration requirements
- `raw/github/stripe/stripe-android/snapshots/2026-07-31-dc874ce/files/CHANGELOG.md` - cumulative upstream release history
- `raw/github/stripe/stripe-android/snapshots/2026-07-31-dc874ce/files/paymentsheet/api/paymentsheet.api` - compiled public PaymentSheet signatures
- `raw/github/stripe/stripe-android/snapshots/2026-07-31-dc874ce/files/payments-core/api/payments-core.api` - compiled public payments signatures
- `raw/github/stripe/stripe-android/snapshots/2026-07-31-dc874ce/files/paymentsheet/src/main/java/com/stripe/android/paymentsheet/PaymentSheet.kt` - PaymentSheet and FlowController source contract
- `raw/github/stripe/stripe-android/snapshots/2026-07-31-dc874ce/files/payments-core/src/main/java/com/stripe/android/Stripe.kt` - low-level Stripe client
- `raw/github/stripe/stripe-android/snapshots/2026-07-31-dc874ce/files/payments-core/src/main/java/com/stripe/android/googlepaylauncher/GooglePayLauncher.kt` - Google Pay lifecycle
- `raw/github/stripe/stripe-android/snapshots/2026-07-31-dc874ce/files/paymentsheet-example/src/main/java/com/stripe/android/paymentsheet/example/samples/ui/paymentsheet/complete_flow/CompleteFlowViewModel.kt` - backend-prepared complete-flow example
- `raw/github/stripe/stripe-android/snapshots/2026-07-31-dc874ce/files/paymentsheet-example/src/main/java/com/stripe/android/paymentsheet/example/samples/ui/paymentsheet/custom_flow/CustomFlowActivity.kt` - custom FlowController example
- `raw/github/stripe/stripe-android/snapshots/2026-07-31-dc874ce/files/paymentsheet-example/src/main/java/com/stripe/android/paymentsheet/example/playground/embedded/EmbeddedPlaygroundActivity.kt` - embedded-element lifecycle example
- `raw/github-stripe-android.md` - legacy `23.8.0` capsule pointer
