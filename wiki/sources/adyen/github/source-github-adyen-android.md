---
title: "GitHub: Adyen/adyen-android"
type: source
date_ingested: 2026-08-01
date_updated: 2026-11-07
original_format: github-repo
raw_files:
  - "github/adyen/adyen-android/snapshots/2026-11-07-73df655/manifest.json"
  - "github/adyen/adyen-android/snapshots/2026-11-07-405b582/manifest.json"
  - "github/adyen/adyen-android/supplements/2026-11-07-405b582-93095740/manifest.json"
  - "github/adyen/adyen-android/snapshots/2026-08-01-5314fad/manifest.json"
tags: [adyen, android, kotlin, mobile-sdk, drop-in, components, sessions, jetpack-compose, github-repository]
---

## Overview

`Adyen/adyen-android` contains Adyen's modular native Android checkout SDK. It provides a prebuilt Drop-in, individual payment Components, Session orchestration, follow-up actions, card encryption, Jetpack Compose adapters, and integrations for local payment methods and delegated wallet or authentication SDKs. This cumulative page begins with package-qualified release `adyen-android@5.20.0` at exact SHA `5314fad1389a8def9d8e3377f27f7405e303faba`.

Repository: <https://github.com/Adyen/adyen-android>

Latest ingested package evidence is `adyen-android@5.22.0`, released 2026-10-30 and ingested 2026-11-07. The full additive sections below retain all `5.20.0` architecture and behavior plus the `5.21.0` release (2026-10-27, ingested 2026-11-07) as historical evidence rather than replacing them.

## Evidence boundary

- The snapshot proves retained implementation at `adyen-android@5.20.0`, released on 2026-07-30. It does not establish current product eligibility, merchant enablement, regional availability, or device support.
- Payment-method models and Components are client integration surfaces. The merchant backend or Session response remains authoritative for available methods and transaction results.
- The capsule retains the complete selected source set, including example and story-equivalent integration material, while excluding tests and generated or binary artifacts by policy.
- Adyen 3DS2, Google Pay, Cash App Pay, Twint, and WeChat Pay behavior is partly delegated to separately versioned dependencies. This page records the Android SDK's adapter boundary, not each dependency's complete runtime.

## Grounding excerpts

> "Adyen Android allows you to accept in-app payments by providing you with the building blocks you need to create a checkout experience."
>
> `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/README.md:9`

> "Drop-in is our pre-built checkout UI for accepting payments. You only need to integrate through your backend with the /sessions API endpoint"
>
> `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/drop-in/src/main/java/com/adyen/checkout/dropin/DropIn.kt:31-36`

> "The rest of the /payments call request data should be filled in, on your server, according to your needs."
>
> `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/components-core/src/main/java/com/adyen/checkout/components/core/PaymentComponentData.kt:21-25`

> "You only need to integrate with the /sessions endpoint to create a session and the component will automatically handle the rest of the payment flow."
>
> `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/components-compose/src/main/java/com/adyen/checkout/components/compose/ComposeExtensions.kt:124-126`

> "Supported API levels" with Compile SDK Version 36 and Target SDK Version 36.
>
> `raw/github/adyen/adyen-android/releases/adyen-android/5.20.0/2026-08-01/release-notes.md:1-6`

## Platform, distribution, and lifecycle

The retained README marks 5.x active, 4.x inactive with deprecation in June 2026 and end-of-life in June 2027, and 3.x end-of-life. Version `5.20.0` uses minimum Android API 21, compile and target SDK 36, Java toolchain 11, and Kotlin 1.9.25.

Artifacts are distributed through Maven Central. Merchants can import View-based `drop-in` and payment-method modules or Compose-oriented `drop-in-compose` and `components-compose` adapters. ProGuard and R8 rules are embedded in the published artifacts.

## Integration modes and server boundary

Drop-in is the prebuilt checkout route. With Sessions, the merchant backend creates a Session and the SDK handles the remaining client flow. The advanced route begins with `/paymentMethods` and delegates `/payments` and `/payments/details` to merchant callbacks. Drop-in must be registered through the Activity Result API before starting a payment.

Individual Components expose typed state and shopper input. `PaymentComponentData` includes payment-method details, amount, order, storage choice, shopper reference, installments, and billing data that the SDK can infer; the merchant server must complete and submit the rest of the payment request in an advanced integration.

## Sessions

`CheckoutSessionProvider` initializes a checkout Session from a server-created session ID and session data. The internal Session service supports setup, payments, payment details, balance checks, order creation and cancellation, payment-method refresh, and stored-token disabling.

A merchant can take over Session payments or details calls. Once a call is taken over, the corresponding callbacks become the merchant's responsibility; missing callback implementations fail rather than silently returning to SDK ownership. This allows selective server control but requires a consistent ownership boundary.

## Drop-in, storage, and partial payments

Drop-in separates stored, regular, gift-card, and already-paid methods, filters unavailable Components, and routes follow-up actions. It can remove supported stored methods and preserve partial-payment state.

Sessions can check gift-card balances, create or cancel orders, refresh payment methods against a remaining amount, and continue an order after partial payment. These client capabilities do not replace server-side order reconciliation or final transaction verification.

## Components and Compose

The repository separates shared Component models and lifecycle from method-specific modules. Compose adapters retain lifecycle and saved-state owners, create one Component per lifecycle by default, and accept a key when multiple instances are needed. `AdyenComponent` hosts the existing Component view in Compose. Drop-in Compose wraps the same Activity Result contracts as View-based Drop-in instead of introducing a separate checkout engine.

Payment-method modules include cards, ACH, Bacs, Blik, Boleto, issuer-list banking, Pay by Bank, PayTo, SEPA, UPI, gift cards, Google Pay, Cash App Pay, Twint, WeChat Pay, and other local methods. A module's presence proves an adapter exists, not that the method is enabled for a particular merchant.

## Cards and encryption

The Card Component supports six- and eight-digit BIN callbacks, card-brand lookup, dual-brand selection, card scanning, holder name, billing address and address lookup, storage choice, installments, country-specific fields, and stored-card security-code policies. The selected co-badged brand is submitted with the payment data, while debit funding sources suppress installments in the retained implementation.

Card fields and generic sensitive fields are encrypted with an Adyen public key before submission. Client-side encryption narrows raw-detail exposure but does not replace server-side payment creation, result verification, compliance controls, or fulfillment logic.

## Actions and delegated SDKs

The action layer dispatches redirect, 3DS2 fingerprint and challenge, generic SDK, await, QR-code, and voucher actions. The 3DS2 adapter coordinates token validation, fingerprint submission, challenge results, and app-return handling while delegating its underlying runtime to `com.adyen.threeds:adyen-3ds2@2.2.27`.

Google Pay delegates to Google Play Services Wallet `19.4.0`, Cash App Pay to Pay Kit `2.5.0`, Twint to its Android SDK `8.0.0`, and WeChat Pay to Tencent's SDK `6.8.0`. Claims about those runtimes require their own evidence histories.

## Analytics

Drop-in and Component analytics are enabled by default from the 5.x line. `AnalyticsLevel.NONE` suppresses event analytics, while the implementation retains an initial setup request used to obtain a checkout-attempt identifier. Merchants should evaluate this behavior against their telemetry, consent, and privacy requirements.

## `5.20.0` release finding

The exact release documents one change: compile and target SDK support moved to API 36. Android consumers should verify their build toolchain and application compatibility when adopting the release. No API migration or breaking behavioral change is documented in the retained release note.

Broader Drop-in, Session, Component, card, action, wallet, analytics, and payment-method findings above describe accumulated behavior present at the exact SHA, not changes introduced solely by `5.20.0`.

## `adyen-android@5.21.0` full additive findings

From `5.20.0` to `5.21.0`, exact SHA `405b582a7b2060aceac756eae7b6bd3757e0c084`. The selected capsule has 1,199 files: 65 modified and 1,134 unchanged. User approved full mode despite the script's contained-minor delta recommendation because the broad build migration merits full migration treatment. Focused reading and mechanical verification of unchanged evidence were explicitly approved; this is not a full upstream-tree read. The five supplemental build files belong to this exact SHA.

### Checkout fixes

- **Save-card switch after address lookup:** `CardView.updateInputFields` now restores the switch from the output state:

  ```kotlin
  binding.switchStorePaymentMethod.isChecked = outputData.shouldStorePaymentMethod
  ```

  Located at `card/src/main/java/com/adyen/checkout/card/internal/ui/view/CardView.kt:756` in the current snapshot. Release notes identify the visible fix as preventing the store-payment-details switch from resetting on return from address lookup. This does not by itself store a payment token or change backend/consent responsibilities.
- **Native redirect failure reporting:** `DefaultRedirectDelegate.handleNativeRedirect` protects request submission and response serialization with `runSuspendCatching`. Success emits details; failure tracks a serialization/network error and invokes `emitError`, preserving CheckoutException or wrapping another failure in `ComponentException("Native redirect request failed.", e)`. The unchanged helper rethrows CancellationException. This closes the previously narrower HttpException/serialization handling path, not all app crash paths; no automatic retry is introduced.
- The example Card Activity and BACS dialog switch back handling to `OnBackPressedDispatcher`, preserving the Component's first chance to handle back navigation. Other retained Kotlin changes are lint suppression, whitespace and comment cleanup, not demonstrated new public callback contracts.

### Build migration and delegated dependencies

| Evidence | `5.20.0` | `5.21.0` | Qualification |
| --- | --- | --- | --- |
| Adyen 3DS2 pin | `2.2.27` | `2.2.28` | Adapter dependency only; dependency runtime not audited here |
| Kotlin catalog | `1.9.25` | `2.3.21` | Repository build definition, not a universal consumer minimum |
| Android Gradle Plugin | `8.8.1` | `9.4.1` | Repository build definition |
| Android Java source/target | `11` | `11` | Explicit in the exact-SHA supplemental Java convention |
| Catalog JVM target | Prior shared Java setting `11` | `17` | Plain Kotlin JVM tooling/convention build; not universal Android-library bytecode 17 |
| Compile/min SDK catalog | `36` / `21` | `36` / `21` | Retained configuration, not merchant/device eligibility |
| Example-app Retrofit | `2.11.0` | `3.0.0` | Not evidence of an SDK-core transport migration |

The version catalog also updates AndroidX, Compose, Coroutines and Material. Module build files adopt `checkout.android.library`; settings includes `build-logic`. Supplemental plugin registration maps these aliases to the retained implementations. The Java convention explicitly says `compileOptions.sourceCompatibility = JavaVersion.VERSION_11` and sets targetCompatibility to 11, while `jvmToolchain(jvmTarget.majorVersion.toInt())` applies to plain Kotlin JVM projects. The convention build separately uses catalog target 17. The wrapper file records `gradle-9.8.0-bin.zip`; it is not a requirement for every consuming application to copy that wrapper or proof that the build ran successfully.

The supplemental Android library convention sets `com.adyen.checkout` group, compile/min SDK, consumer ProGuard and checkout-version BuildConfig settings. Its conditional AGP 9/binary-compatibility-validator workaround registers API build/check/dump tasks for non-ignored projects and filters generated Compose `ComposableSingletons` content. These are configured tasks, not passing compatibility tests, and generated API dump changes outside the capsule are not independently established authored API removals.

**Migration action:** test the consuming application's dependency/build compatibility, save-card choice through address lookup and redirect failure callbacks. Independently validate the delegated 3DS2 runtime if its internal changes matter. This ingest ran no Gradle build, Android/device, certificate-rejection or payment tests. Earlier `5.20.0` integration and runtime descriptions remain version-qualified history.

## `adyen-android@5.22.0` full additive findings

From `5.21.0` to `5.22.0`, exact SHA `73df6558fa5868a2c14449ac2e0c6379fc349798`. Three of 1,199 retained files change; 1,196 remain hash-identical. This is an approved full security ingest with focused reading, not an assertion that the small changed-file count makes security impact bounded. All `5.20.0` and `5.21.0` knowledge above remains, and the five-file supplement stays attributed to its exact `5.21.0` SHA.

### Security claim and source evidence

Adyen's release notes state that Drop-in and Components block eight compromised eMudhra intermediate CA certificates on Android devices without Google Play services, and that devices with Play services had already received Google's automatic update. The retained version catalog raises both OkHttp and its logging pin from `4.12.0` to `4.12.1`. SDK-core HttpClientFactory and the existing DefaultImageLoader instantiate OkHttp clients.

**Evidence limit:** The certificate-blocking claim comes from the upstream release note. This capsule does not contain the upgraded dependency's blocklist implementation, an independently verified eight-certificate inventory or a device rejection test. No CVE, comprehensive TLS guarantee, live rollout, or universal safety claim is inferred from the version pin alone.

### Image saving and bitmap ownership

`ImageSaver.saveImageFromUrl` no longer downloads through URL.openStream/BufferedInputStream and BitmapFactory.decodeStream. It checks URL syntax, then calls the existing shared image loader through a new `loadBitmap` helper:

```kotlin
context.imageLoader.load(
    url = imageUrl,
    onSuccess = { bitmap -> bitmapResult = Result.success(bitmap) },
    onError = { error -> bitmapResult = Result.failure(error) },
)
```

`ImageLoadingExtensions` makes the Context.imageLoader accessor internal rather than private, allowing this reuse. The loader caches by URL and uses OkHttp; callback errors or protected load failures now become `CheckoutException("Failed to load image", error)`, distinct from the initial `CheckoutException("Malformed URL")` check.

The shared `saveImageFromBitmap` helper no longer recycles every input bitmap. Recycling now happens after saving in `saveImageFromView`, which created that bitmap. Consequently, the URL-saving route does not recycle a loader-provided cached bitmap via the old shared helper. This is an ownership-path change, not proof of leak-free cleanup or cancellation safety on every path. Existing MediaStore/legacy permission-saving paths remain; this is not a new merchant payment API.

**Migration action:** prioritize reviewing the upstream security release and the application's resolved dependency graph; regression-test image download/save, malformed URL, HTTP failure and cached-image reuse, including target device populations. No Gradle build, Android/device, certificate-rejection or payment test was run during ingestion. The earlier build-migration distinctions remain documented at `5.21.0`, not re-proven by a mismatched-SHA supplement.

## Related

- [[changelog-github-adyen-android]] - package-qualified release ledger
- [[adyen-android-sdk]] - native Android SDK concept
- [[source-github-adyen-ios]] - independently versioned native iOS SDK
- [[source-github-adyen-web]] - independently versioned browser SDK
- [[co-badged-cards]] - cross-provider network-choice concept
- [[adyen]] - company and knowledge-status page

## Raw sources

- `5.22.0` snapshot: `raw/github/adyen/adyen-android/snapshots/2026-11-07-73df655/manifest.json`
- `5.22.0` release: `raw/github/adyen/adyen-android/releases/adyen-android/5.22.0/2026-11-07/manifest.json` and `raw/github/adyen/adyen-android/releases/adyen-android/5.22.0/2026-11-07/release-notes.md`
- `5.21.0` -> `5.22.0` comparison: `tracking/github/repos/adyen/adyen-android/comparisons/adyen-android/5.21.0--5.22.0/comparison.json`, `tracking/github/repos/adyen/adyen-android/comparisons/adyen-android/5.21.0--5.22.0/comparison.md` and `tracking/github/repos/adyen/adyen-android/comparisons/adyen-android/5.21.0--5.22.0/diff.patch`
- `5.22.0` catalog: `raw/github/adyen/adyen-android/snapshots/2026-11-07-73df655/files/gradle/libs.versions.toml`
- `5.22.0` image changes: `raw/github/adyen/adyen-android/snapshots/2026-11-07-73df655/files/ui-core/src/main/java/com/adyen/checkout/ui/core/internal/util/ImageSaver.kt` and `raw/github/adyen/adyen-android/snapshots/2026-11-07-73df655/files/ui-core/src/main/java/com/adyen/checkout/ui/core/internal/ui/ImageLoadingExtensions.kt`
- `5.22.0` retained dependency boundaries: `raw/github/adyen/adyen-android/snapshots/2026-11-07-73df655/files/checkout-core/src/main/java/com/adyen/checkout/core/internal/ui/ImageLoader.kt` and `raw/github/adyen/adyen-android/snapshots/2026-11-07-73df655/files/checkout-core/src/main/java/com/adyen/checkout/core/internal/data/api/HttpClientFactory.kt`
- `5.21.0` snapshot: `raw/github/adyen/adyen-android/snapshots/2026-11-07-405b582/manifest.json`
- `5.21.0` release: `raw/github/adyen/adyen-android/releases/adyen-android/5.21.0/2026-11-07/manifest.json` and `raw/github/adyen/adyen-android/releases/adyen-android/5.21.0/2026-11-07/release-notes.md`
- `5.20.0` -> `5.21.0` comparison: `tracking/github/repos/adyen/adyen-android/comparisons/adyen-android/5.20.0--5.21.0/comparison.json`, `tracking/github/repos/adyen/adyen-android/comparisons/adyen-android/5.20.0--5.21.0/comparison.md` and `tracking/github/repos/adyen/adyen-android/comparisons/adyen-android/5.20.0--5.21.0/diff.patch`
- `5.21.0` card fix: `raw/github/adyen/adyen-android/snapshots/2026-11-07-405b582/files/card/src/main/java/com/adyen/checkout/card/internal/ui/view/CardView.kt`
- Redirect and cancellation boundary: `raw/github/adyen/adyen-android/snapshots/2026-11-07-405b582/files/redirect/src/main/java/com/adyen/checkout/redirect/internal/ui/DefaultRedirectDelegate.kt` and `raw/github/adyen/adyen-android/snapshots/2026-11-07-405b582/files/checkout-core/src/main/java/com/adyen/checkout/core/internal/util/ResultExt.kt`
- `5.21.0` catalog/example build: `raw/github/adyen/adyen-android/snapshots/2026-11-07-405b582/files/gradle/libs.versions.toml` and `raw/github/adyen/adyen-android/snapshots/2026-11-07-405b582/files/example-app/build.gradle`
- Exact-SHA build supplement: `raw/github/adyen/adyen-android/supplements/2026-11-07-405b582-93095740/manifest.json`; attached through `tracking/github/repos/adyen/adyen-android/evidence-attachments/github-7ed8658609166ae83227/attachment.json`
- Supplemental build files: `raw/github/adyen/adyen-android/supplements/2026-11-07-405b582-93095740/files/build-logic/convention/build.gradle.kts`, `raw/github/adyen/adyen-android/supplements/2026-11-07-405b582-93095740/files/build-logic/convention/src/main/kotlin/CheckoutAndroidLibraryPlugin.kt`, `raw/github/adyen/adyen-android/supplements/2026-11-07-405b582-93095740/files/build-logic/convention/src/main/kotlin/JavaConventionPlugin.kt`, `raw/github/adyen/adyen-android/supplements/2026-11-07-405b582-93095740/files/build-logic/convention/src/main/kotlin/com/adyen/checkout/ProjectExtensions.kt` and `raw/github/adyen/adyen-android/supplements/2026-11-07-405b582-93095740/files/gradle/wrapper/gradle-wrapper.properties`
- Snapshot manifest: `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/manifest.json`
- Release manifest: `raw/github/adyen/adyen-android/releases/adyen-android/5.20.0/2026-08-01/manifest.json`
- Release notes: `raw/github/adyen/adyen-android/releases/adyen-android/5.20.0/2026-08-01/release-notes.md`
- README: `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/README.md`
- Build metadata: `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/build.gradle` and `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/gradle/libs.versions.toml`
- Session: `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/sessions-core/`
- Drop-in: `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/drop-in/` and `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/drop-in-compose/`
- Components: `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/components-core/` and `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/components-compose/`
- Cards and encryption: `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/card/` and `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/cse/`
- Actions: `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/action-core/`, `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/3ds2/`, and method-specific action modules
- Example integration: `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/example-app/`
