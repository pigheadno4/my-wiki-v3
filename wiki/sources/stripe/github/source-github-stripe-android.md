---
title: "GitHub: stripe/stripe-android"
type: source
date_ingested: 2026-05-13
date_updated: 2026-07-31
original_format: github-repo
raw_files:
  - "github/stripe/stripe-android/snapshots/2026-07-31-dc874ce/manifest.json"
  - "github-stripe-android.md"
tags: [stripe, android, kotlin, mobile, sdk, payments, payment-sheet, embedded-payment-element, google-pay, connect, identity, financial-connections, crypto-onramp, github-repository]
---

## Overview

`stripe/stripe-android` publishes Stripe's official native Android SDK. This cumulative page preserves the legacy `23.8.0` manual capsule and adds the approved `stripe-android@23.13.1` full baseline at commit `dc874ce7c62dd433664ec4e312efeb9300c21795`.

Repository: <https://github.com/stripe/stripe-android>

## Evidence Boundary

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
| `stripe-android` | `23.13.1` | `dc874ce7c62dd433664ec4e312efeb9300c21795` | Approved full baseline; legacy `23.8.0` retained |

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

