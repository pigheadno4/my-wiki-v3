---
title: "GitHub: braintree/braintree_android"
type: source
date_ingested: 2026-10-04
original_format: github-repo
raw_files:
  - "github/braintree/braintree_android/snapshots/2026-10-04-04b82bb/manifest.json"
  - "github/braintree/braintree_android/snapshots/2026-10-04-2695a48/manifest.json"
  - "github/braintree/braintree_android/snapshots/2026-10-04-438d33a/manifest.json"
  - "github/braintree/braintree_android/snapshots/2026-08-01-51f183a/manifest.json"
tags: [braintree, android, mobile-sdk, paypal, venmo, cards, 3d-secure, github-repository]
---

## Overview

`braintree/braintree_android` contains Braintree's modular native Android SDK. The first retained baseline is package-qualified release `braintree-android@5.30.0` at exact SHA `51f183a48557d0fd00eefa541712df0c4f21ee28`.

Repository: <https://github.com/braintree/braintree_android>

## Evidence Boundary

- This exact-SHA snapshot proves implementation present in `braintree-android@5.30.0`, released on 2026-07-21. It does not prove merchant-account enablement, buyer eligibility, regional availability, or production approval for any payment method.
- Braintree Android is independent from both `paypal/paypal-android` and Braintree's browser repositories. Similar product names do not make their APIs, versions, or release histories interchangeable.
- The capsule retains production source, resources, README, changelog, migration guides and selected build metadata. Demo files, tests, fixtures, generated documentation, CI, and unrelated tooling are outside this configured capsule; do not infer demo behavior from their upstream inventory entries.
- The repository changelog supplies historical migration context. The initial baseline is 5.30.0; subsequent release-specific deltas link their own immutable snapshots and comparisons. No build or payment test was performed.

## Grounding Excerpts

> "This library will help you accept card and alternative payments in your Android app."
>
> `raw/github/braintree/braintree_android/snapshots/2026-08-01-51f183a/files/README.md:6`

> "The Braintree SDK supports Android API 23 and above."
>
> `raw/github/braintree/braintree_android/snapshots/2026-08-01-51f183a/files/README.md:10`

> "If set to true, this enables the Checkout with Vault flow, where the customer will be prompted to consent to a billing agreement during checkout."
>
> `raw/github/braintree/braintree_android/snapshots/2026-08-01-51f183a/files/PayPal/src/main/java/com/braintreepayments/api/paypal/PayPalCheckoutRequest.kt:53-56`

> "Venmo app or mobile browser"
>
> `raw/github/braintree/braintree_android/snapshots/2026-08-01-51f183a/files/Venmo/src/main/java/com/braintreepayments/api/venmo/VenmoClient.kt:153-157`

> "Vaulting will only occur if a client token with a customer ID is being used."
>
> `raw/github/braintree/braintree_android/snapshots/2026-08-01-51f183a/files/Venmo/src/main/java/com/braintreepayments/api/venmo/VenmoRequest.kt:15-21`

## Platform and Integration Model

The SDK supports Android API 23+, requires Java 11, and uses Kotlin 1.9.10. Merchants install only the Gradle modules needed for their checkout. A `BraintreeClient`, created from a tokenization key, client token, or token provider, retrieves merchant configuration and supports authorization for the payment-specific clients.

Payment clients create a payment-authorization request, a launcher presents any browser, wallet, or app-switch experience, and the client tokenizes the successful return into a Braintree payment-method nonce. Redirect-capable modules preserve a pending request and resolve the app-link or deep-link return before tokenization. The nonce is then sent to the merchant's Braintree server integration for processing.

## Modules and Payment Surfaces

The retained source includes:

- Card tokenization plus `CardFields`, a native complete-card form with number, expiration, CVV, validation, and XML support.
- PayPal checkout, PayPal vault, checkout-with-vault, Pay Later or Credit offers, app switch, recurring-billing metadata, and dedicated XML and Compose buttons.
- Venmo single-use and multi-use requests, Venmo app or mobile-browser launch, optional vaulting, address enrichment, and dedicated XML and Compose buttons.
- Google Pay readiness, request creation, wallet-sheet launch, and tokenization to a Braintree card or PayPal nonce.
- Local Payment and SEPA flows, including browser mandate handling where required.
- 3D Secure v2 lookup, challenge, tokenization, and liability-shift results.
- Data Collector device data, American Express rewards-balance lookup, PayPal Messaging, and beta Shopper Insights recommendations.

Module presence is SDK capability evidence. Runtime configuration such as `isPayPalEnabled`, `isVenmoEnabled`, and Google Pay readiness still gates presentation, and none of those checks alone proves that a merchant should be sold or activated for the method.

## PayPal Flows

PayPal is a Braintree payment module with separate request types for checkout and vaulting. `PayPalCheckoutRequest` supports one-time checkout and can set `shouldRequestBillingAgreement` for checkout-with-vault. Both checkout and vault requests can carry recurring-billing details and plan types. These fields describe a billing-agreement request surface; they are not a subscription scheduler or evidence that recurring billing is enabled for a merchant.

`enablePayPalAppSwitch` can request the PayPal app path when the installed app is resolvable. The launcher otherwise uses the browser flow. The SDK returns a Braintree PayPal account nonce rather than a direct PayPal Orders API approval result.

The internal PayPal funding-source enum covers PayPal, Pay Later, and Credit. Venmo is not a PayPal funding-source value in this SDK.

## Venmo Flow and Vault Boundary

Venmo is a dedicated Braintree module. `VenmoClient.createPaymentAuthRequest()` first checks `configuration.isVenmoEnabled`; it then creates a Venmo payment context for launch in the Venmo app or a mobile browser. App links are the preferred return mechanism, with a custom-scheme deep-link fallback.

`VenmoPaymentMethodUsage` distinguishes `SINGLE_USE` and `MULTI_USE`. Automatic vaulting requires all of the following in this retained implementation:

- `shouldVault` is true;
- a client token authorization is used, with the public request documentation specifying a customer ID; and
- payment-method usage is `MULTI_USE`.

Address collection is conditional on enriched customer data being enabled. A visible Venmo button, source module, or recommendation from Shopper Insights therefore must not be treated as proof of merchant or buyer eligibility.

This native Braintree Venmo path must not be conflated with `paypal/paypal-android@2.3.0`, whose retained standalone PayPal SDK source exposes no native Venmo integration.

## Cards, 3D Secure, and Risk

Card tokenization can use the public suspend API or the UIComponents card form. The 3D Secure module performs lookup and optional challenge work against a card nonce and returns liability-shift indicators; the merchant still decides whether to proceed when liability does not shift.

Data Collector uses PayPal's Magnes SDK and accepts user-location consent. Device data is a fraud-input artifact, not proof that a particular fraud product or merchant configuration is active.

## Shopper Insights and Presentation

Shopper Insights is a beta recommendation layer for PayPal and Venmo. Its newer flow creates or updates a customer session and requests payment recommendations. Recommendations can inform ordering or presentation, but they do not override Braintree configuration, merchant eligibility, or buyer eligibility.

The UIComponents module provides XML and Compose PayPal and Venmo buttons. In `5.30.0`, explicit button sizing and `match_parent` behavior are honored. Presentation support remains separate from payment-method activation and transaction processing.

## `5.30.0` Release Findings

The release exposes public Kotlin suspend functions across American Express, Card, Google Pay, Local Payment, PayPal, SEPA, Shopper Insights, 3D Secure, and Venmo. It also updates Android Gradle Plugin to 8.13.2 and compile/target SDK to API 37.

Visa Checkout is no longer supported and its module is removed. Visa-related configuration properties are deprecated for removal in the next major version. The release also corrects PayPal and Venmo button sizing behavior.

These are the exact `5.30.0` findings. Broader v5 architecture, request/launcher migration, and older removals such as PayPal Native Checkout, Samsung Pay, and the UnionPay module are historical context from the cumulative changelog and migration guides.

## `5.31.0` Delta from `5.30.0`

Package `braintree-android@5.31.0`, released 2026-08-03, is retained at SHA `438d33ac42c92ca7489c3fec3b45d088a75a8361`. Six retained files changed; the older baseline above is preserved.

### Automatic Device Context on PayPal Authorization

`PayPalInternalClient.sendRequest` still distinguishes Checkout (`/v1/paypal_hermes/create_payment_resource`) and Vault (`/v1/paypal_hermes/setup_billing_agreement`). It first rechecks an enabled app-switch request against `deviceInspector.isPayPalInstalled()` and `resolvePayPalUseCase()`, then selects the return link. Only when enablePayPalAppSwitch remains true and appLinkParam is non-null does it enrich the shared request body.

The helper uses ActivityManager.MemoryInfo and Build.MODEL to write this nested structure (field placeholders, not captured buyer data):

```json
{
  "app_switch_context": {
    "device_info": {
      "model": "<device model>",
      "memory_available_mb": 123,
      "memory_total_mb": 456
    }
  }
}
```

The numeric values above are illustrative. Actual memory values divide bytes by 1024 squared and convert to integers. An existing app_switch_context is preserved and its device_info field is populated; a missing context object is created. If ActivityManager is unavailable, the helper returns the base request unchanged. Disabled/ineligible app-switch requests and deep-link-only returns do not take this enrichment branch. No merchant-supplied deviceInfo parameter was added to the public request constructor.

The device-info helper does not test hasUserLocationConsent. The existing separate DataCollectorInternalRequest still receives that flag, after the authorization POST, unless riskCorrelationId supplies the correlation ID. This is a code-path distinction, not evidence of lawful processing or permission-policy compliance. Do not copy buyer device data into wiki examples.

PayPal's server response still determines isAppSwitchFlow; sending these fields does not guarantee app launch or eligibility. Nonce tokenization and merchant-server processing remain unchanged.

### Browser Switch and Compatibility Boundary

> [!warning] Contradiction
> 5.31.0 release notes and its changelog report a Browser Switch upgrade to 3.6.0, but the same SHA's unchanged DEPENDENCIES.md lists 3.5.1. BraintreeCore/build.gradle only references libs.browser.switch. The excluded gradle/libs.versions.toml and delegated Browser Switch implementation were not collected, so the resolved dependency version and behavior are not independently verified. Preserve both authorities; see [[braintree-android-sdk]].

Android minimum API 23, Java 11, and compile/target API 37 remain declared. README and v5 migration dependency examples advance to 5.31.0; the v4-to-v5 migration architecture is not newly introduced by this release. Before merchant migration advice, verify actual dependency resolution/builds separately. No runtime or payment proof is claimed.

## `5.32.0` Delta from `5.31.0`

Package `braintree-android@5.32.0`, released 2026-08-27, is retained at SHA `2695a481d8cd56a3d6db379297e6682663d2c94e`. There are 23 changed/new retained files and 367 unchanged files. User-approved focused reading covers changed implementation and affected prior code; inventories and unchanged changelog history were mechanically verified. Earlier version findings remain intact.

### Campaign Association Inputs

`PayPalCheckoutRequest` adds `campaigns: List<PayPalCampaign> = emptyList()`. Each Parcelable campaign has an `id: String`; when the list is nonempty, request serialization writes `paypal_campaigns: [{"id":"<campaign ID>"}]`. An empty list omits the field. This change adds checkout request input, not a new campaign creation API or a campaign property on PayPalVaultRequest.

Beta Shopper Insights v2 adds `CustomerSessionRequest.payPalCampaigns: List<ShopperInsightsCampaign>?`, default null. Its builder omits null/empty lists and serializes campaign ID objects as GraphQL `paypalCampaigns` for create/update customer-session inputs and recommendation generation supplied with a CustomerSessionRequest. Generation using only a session ID does not newly supply campaign objects. No retained code here validates campaign ID eligibility, provisions campaigns or guarantees that a buyer receives an offer.

### Shopper Insights Error Propagation and Expiry

The session parser now inspects a nonempty top-level `errors` array before reading `data`; it throws BraintreeException using the first error's message. The recommendation parser adds the same check. Previously both parsers went directly into `data`, potentially masking a GraphQL error with a JSON lookup failure. Existing API wrappers catch these exceptions as Error, and ShopperInsightsClientV2 maps them to public CustomerSessionResult.Failure or CustomerRecommendationsResult.Failure; coroutine cancellation still propagates. This does not aggregate every GraphQL error. The missing-message fallback can use the whole response body, so callers should not display or log unsanitized upstream error content.

Recommendation queries now select `expiresAt`; CustomerRecommendations exposes it as nullable String with ISO-8601 documentation. The parser safely casts the JSON value to String, so missing/non-string values become null. This adds a staleness signal, not date parsing, automatic refreshing or client-side expiry enforcement in these code paths.

### Venmo Vaulted Identity Fix and Limit

In VenmoAccountNonce.fromJSON's nonce/details branch (rather than the paymentMethodId branch), `externalId` now reads `details.commonId` when that key exists; otherwise it is null. Previously that branch supplied no external ID unless payerInfo later supplied one. The subsequent `payerInfo.externalId` assignment remains and can overwrite commonId, including with an empty string if the payerInfo field is missing. The release fixes one vaulted client-token response shape, not all possible empty-ID cases. Existing shouldVault/client-token authorization behavior in VenmoClient is unchanged.

### Google Pay Constructor and Return-Scheme Documentation

GooglePayLauncher adds a public constructor accepting ActivityResultRegistry, LifecycleOwner, Context and callback. It delegates to the existing registration/payment-data flow and supports Compose-oriented callers without a Fragment or ComponentActivity constructor argument. KDoc requires construction before the lifecycle owner reaches CREATED; launch requires CREATED to have been reached. This is not itself an @Composable UI or a new tokenization/payment flow. No Compose execution was tested.

PayPalClient, VenmoClient and XML/Compose button KDoc clarify that deepLinkFallbackUrlScheme is a bare scheme matching AndroidManifest.xml: alphanumerics, hyphens or periods; no `://`, path, query, fragment or underscore. These changes are comments, not a new runtime scheme validator or newly introduced branded-button integration.

### Build, Documentation and Preserved Gaps

README and migration dependency examples advance to 5.32.0. Android minimum API 23 and compile/target API 37 remain. Dokka output moves into build/dokkaDocs and the reference-doc URL points to /current/; the large excluded generated-doc removal is not payment-API removal evidence. Publication scripts and tests remain outside the capsule. The prior Browser Switch release-note/dependency-document discrepancy is not resolved by this delta. No SDK build, dependency-resolution or payment execution proof is claimed.

## `5.33.0` Delta from `5.32.0`

Package `braintree-android@5.33.0`, released 2026-09-16, is retained at SHA `04b82bbb1cb49e3a5ad44bac920704ba03c99317`. Eight retained files were added and eight modified; 382 are unchanged. User-approved focused reading fully covers changed implementation/docs and affected prior code; large inventories and unchanged cumulative changelog history were mechanically checked. Older version sections remain intact.

### Compose Form and Controller Integration

The UIComponents module adds public `compose.CardFields` and `rememberCardFieldsController(authorization: String, request: Card = Card())`. This is distinct from the existing XML CardFields class in the cardfields package. Compose renders card number, expiration and CVV inputs; the merchant supplies the submit button and observes `controller.isFormValid` as StateFlow<Boolean>.

Integration order:

1. Include the UIComponents module and create a remembered controller with a Braintree client token or tokenization key and optional additional Card data.
2. Render CardFields(controller) and observe isFormValid to enable the merchant-owned submit button.
3. Call controller.submit(callback). The controller copies raw number/CVV and the first two/remainder expiration digits into the optional Card request, preserving other request fields such as cardholder name and postal code.
4. CardClient.tokenize returns CardResult; the controller maps it to CardFieldsResult.Success(nonce) or Failure(error). Send nonce.string to the merchant's server for processing; tokenization is not a completed transaction or 3DS verification.

The README illustrates this sequence but its example ignores its authorization parameter in favor of a placeholder string. Use the actual supplied authorization in a real integration, not the literal documentation placeholder. The retained source was not built or executed.

### Validation, Input and Presentation

The shared CardFieldsViewModel changes its current values from private fields to internal getters with private setters so Compose can initialize/restore its state. Its validation algorithm is otherwise unchanged: valid results propagate immediately, typing suppresses errors into Validating, and blur resolves incomplete/empty values into invalid/required errors. All three fields must be Valid for isFormValid.

Compose sanitizers remove non-digits and reject edits exceeding brand-specific number/CVV lengths or four expiration digits. Expiration formatting pads a single month digit greater than 1 and displays an MM/YY separator without storing that separator. Number formatting likewise inserts display-only gaps. A brand change can truncate existing CVV to the new maximum length. Focus advances on a validation change to Valid while the source field is focused; untouched fields are not immediately marked invalid by their initial unfocused callback.

The form reuses existing validation use cases: card-number length plus Luhn (UnionPay exempt), valid nonexpired month/year and brand-specific CVV lengths. These are client input checks, not authorization or card acceptance guarantees. The new base field renders error/accessibility semantics, floating hints and shared resources; no actual visual/accessibility test was run.

The CVV visual transformation masks digits, briefly revealing a newly typed digit for 1,500 milliseconds. Its hint popup is positioned above the icon using measured anchor bounds. Masking changes display, not the underlying field value.

### Submission and Saved-State Caveats

`CardFieldsController.submit` does not check isFormValid and has no in-flight/duplicate-submit guard. It sends CARD_FIELDS_VALIDATED analytics before tokenization regardless of validity; that event name must not be treated as proof of validation success. Integrations should gate submission and manage their own processing state.

The helper uses `rememberSaveable(stateSaver = TextFieldValue.Saver)` for card number, expiration and CVV; a LaunchedEffect synchronizes restored values into its ViewModel. The controller is remembered by ViewModel, authorization and request, and its presentation-event flag is also saveable. This source structure supports state restoration but does not prove host-specific restoration works or that saved state is encrypted, safe for sensitive data, or cleared. submit has no clearing step. The helper uses the default `viewModel<CardFieldsViewModel>()` without a per-form key; do not assume two forms sharing an owner have independent validation state. Inspect host lifecycle/saved-state behavior before sensitive-data use. No real card data was used or retained by this wiki ingest.

### Compatibility and Evidence Limits

README and migration examples advance to 5.33.0; minimum API 23, Java 11 and compile/target API 37 remain declared. UIComponents/build.gradle adds Compose UI instrumentation/debug test dependencies; tests are excluded and were not run. The upstream version catalog changed outside the capsule, so resolved dependency versions remain unverified. This form does not imply new PayPal, Venmo or Google Pay capabilities, a new vaulting policy or Drop-in compatibility. The 5.31.0 Browser Switch discrepancy remains preserved.

## Related

- [[changelog-github-braintree-android]] - package-qualified Android release ledger
- [[braintree-android-sdk]] - native Android SDK concept
- [[braintree]] - company and knowledge-status page
- [[paypal-android-sdk]] - independently versioned standalone PayPal Android SDK
- [[paypal-braintree-integration]] - Braintree PayPal processing boundary

## Raw Sources

- 5.33.0 snapshot: `raw/github/braintree/braintree_android/snapshots/2026-10-04-04b82bb/manifest.json`
- 5.33.0 release: `raw/github/braintree/braintree_android/releases/braintree-android/5.33.0/2026-10-04/manifest.json` and `raw/github/braintree/braintree_android/releases/braintree-android/5.33.0/2026-10-04/release-notes.md`
- 5.32.0--5.33.0 comparison: `tracking/github/repos/braintree/braintree_android/comparisons/braintree-android/5.32.0--5.33.0/comparison.json`, `tracking/github/repos/braintree/braintree_android/comparisons/braintree-android/5.32.0--5.33.0/comparison.md` and `tracking/github/repos/braintree/braintree_android/comparisons/braintree-android/5.32.0--5.33.0/diff.patch`
- Compose form/sanitization: `raw/github/braintree/braintree_android/snapshots/2026-10-04-04b82bb/files/UIComponents/src/main/java/com/braintreepayments/api/uicomponents/compose/CardFields.kt`
- Controller/tokenization/saved state: `raw/github/braintree/braintree_android/snapshots/2026-10-04-04b82bb/files/UIComponents/src/main/java/com/braintreepayments/api/uicomponents/compose/CardFieldsController.kt`
- Shared validation state: `raw/github/braintree/braintree_android/snapshots/2026-10-04-04b82bb/files/UIComponents/src/main/java/com/braintreepayments/api/uicomponents/cardfields/CardFieldsViewModel.kt` and its prior version at `raw/github/braintree/braintree_android/snapshots/2026-10-04-2695a48/files/UIComponents/src/main/java/com/braintreepayments/api/uicomponents/cardfields/CardFieldsViewModel.kt`
- Validation/formatter dependencies: CardNumberValidationUseCase.kt, ExpirationValidationUseCase.kt, CvvValidationUseCase.kt and ExpirationDateFormatter.kt under `raw/github/braintree/braintree_android/snapshots/2026-10-04-04b82bb/files/UIComponents/src/main/java/com/braintreepayments/api/uicomponents/cardfields/`
- Compose display files: CardCvvField.kt, CardExpirationField.kt, CardNumberField.kt, CardFieldBaseTextInputField.kt, CardFieldsVisualTransformations.kt and CvvHintPopup.kt under `raw/github/braintree/braintree_android/snapshots/2026-10-04-04b82bb/files/UIComponents/src/main/java/com/braintreepayments/api/uicomponents/compose/`
- Resources: `raw/github/braintree/braintree_android/snapshots/2026-10-04-04b82bb/files/UIComponents/src/main/res/values/dimens.xml` and `raw/github/braintree/braintree_android/snapshots/2026-10-04-04b82bb/files/UIComponents/src/main/res/values/strings_card_fields.xml`
- Build/setup/migration: `raw/github/braintree/braintree_android/snapshots/2026-10-04-04b82bb/files/UIComponents/build.gradle`, `raw/github/braintree/braintree_android/snapshots/2026-10-04-04b82bb/files/build.gradle`, `raw/github/braintree/braintree_android/snapshots/2026-10-04-04b82bb/files/README.md` and `raw/github/braintree/braintree_android/snapshots/2026-10-04-04b82bb/files/v5_MIGRATION_GUIDE.md`

- 5.32.0 snapshot: `raw/github/braintree/braintree_android/snapshots/2026-10-04-2695a48/manifest.json`
- 5.32.0 release: `raw/github/braintree/braintree_android/releases/braintree-android/5.32.0/2026-10-04/manifest.json` and `raw/github/braintree/braintree_android/releases/braintree-android/5.32.0/2026-10-04/release-notes.md`
- 5.31.0--5.32.0 comparison: `tracking/github/repos/braintree/braintree_android/comparisons/braintree-android/5.31.0--5.32.0/comparison.json`, `tracking/github/repos/braintree/braintree_android/comparisons/braintree-android/5.31.0--5.32.0/comparison.md` and `tracking/github/repos/braintree/braintree_android/comparisons/braintree-android/5.31.0--5.32.0/diff.patch`
- Checkout campaign model/serialization: `raw/github/braintree/braintree_android/snapshots/2026-10-04-2695a48/files/PayPal/src/main/java/com/braintreepayments/api/paypal/PayPalCampaign.kt` and `raw/github/braintree/braintree_android/snapshots/2026-10-04-2695a48/files/PayPal/src/main/java/com/braintreepayments/api/paypal/PayPalCheckoutRequest.kt`
- Shopper Insights models: `raw/github/braintree/braintree_android/snapshots/2026-10-04-2695a48/files/ShopperInsights/src/main/java/com/braintreepayments/api/shopperinsights/v2/CustomerSessionRequest.kt`, `raw/github/braintree/braintree_android/snapshots/2026-10-04-2695a48/files/ShopperInsights/src/main/java/com/braintreepayments/api/shopperinsights/v2/ShopperInsightsCampaign.kt` and `raw/github/braintree/braintree_android/snapshots/2026-10-04-2695a48/files/ShopperInsights/src/main/java/com/braintreepayments/api/shopperinsights/v2/CustomerRecommendations.kt`
- Session serialization/errors: `raw/github/braintree/braintree_android/snapshots/2026-10-04-2695a48/files/ShopperInsights/src/main/java/com/braintreepayments/api/shopperinsights/v2/internal/CustomerSessionRequestBuilder.kt`, `raw/github/braintree/braintree_android/snapshots/2026-10-04-2695a48/files/ShopperInsights/src/main/java/com/braintreepayments/api/shopperinsights/v2/internal/CreateCustomerSessionApi.kt`, `raw/github/braintree/braintree_android/snapshots/2026-10-04-2695a48/files/ShopperInsights/src/main/java/com/braintreepayments/api/shopperinsights/v2/internal/UpdateCustomerSessionApi.kt` and `raw/github/braintree/braintree_android/snapshots/2026-10-04-2695a48/files/ShopperInsights/src/main/java/com/braintreepayments/api/shopperinsights/v2/internal/ShopperInsightsResponseParser.kt`
- Recommendations and public result mapping: `raw/github/braintree/braintree_android/snapshots/2026-10-04-2695a48/files/ShopperInsights/src/main/java/com/braintreepayments/api/shopperinsights/v2/internal/GenerateCustomerRecommendationsApi.kt` and `raw/github/braintree/braintree_android/snapshots/2026-10-04-2695a48/files/ShopperInsights/src/main/java/com/braintreepayments/api/shopperinsights/v2/ShopperInsightsClientV2.kt`
- Venmo nonce and authorization: `raw/github/braintree/braintree_android/snapshots/2026-10-04-2695a48/files/Venmo/src/main/java/com/braintreepayments/api/venmo/VenmoAccountNonce.kt` and `raw/github/braintree/braintree_android/snapshots/2026-10-04-2695a48/files/Venmo/src/main/java/com/braintreepayments/api/venmo/VenmoClient.kt`
- Google Pay launcher: `raw/github/braintree/braintree_android/snapshots/2026-10-04-2695a48/files/GooglePay/src/main/java/com/braintreepayments/api/googlepay/GooglePayLauncher.kt`
- Return-scheme KDoc: `raw/github/braintree/braintree_android/snapshots/2026-10-04-2695a48/files/PayPal/src/main/java/com/braintreepayments/api/paypal/PayPalClient.kt` and the four XML/Compose PayPalButton.kt/VenmoButton.kt files under `raw/github/braintree/braintree_android/snapshots/2026-10-04-2695a48/files/UIComponents/src/main/java/com/braintreepayments/api/uicomponents/`
- Build/setup/migration: `raw/github/braintree/braintree_android/snapshots/2026-10-04-2695a48/files/build.gradle`, `raw/github/braintree/braintree_android/snapshots/2026-10-04-2695a48/files/README.md` and `raw/github/braintree/braintree_android/snapshots/2026-10-04-2695a48/files/v5_MIGRATION_GUIDE.md`

- 5.31.0 snapshot: `raw/github/braintree/braintree_android/snapshots/2026-10-04-438d33a/manifest.json`
- 5.31.0 release: `raw/github/braintree/braintree_android/releases/braintree-android/5.31.0/2026-10-04/manifest.json` and `raw/github/braintree/braintree_android/releases/braintree-android/5.31.0/2026-10-04/release-notes.md`
- 5.30.0--5.31.0 comparison: `tracking/github/repos/braintree/braintree_android/comparisons/braintree-android/5.30.0--5.31.0/comparison.json` and `tracking/github/repos/braintree/braintree_android/comparisons/braintree-android/5.30.0--5.31.0/diff.patch`
- App-switch device context: `raw/github/braintree/braintree_android/snapshots/2026-10-04-438d33a/files/PayPal/src/main/java/com/braintreepayments/api/paypal/PayPalInternalClient.kt`
- Request field names: `raw/github/braintree/braintree_android/snapshots/2026-10-04-438d33a/files/PayPal/src/main/java/com/braintreepayments/api/paypal/PayPalRequest.kt`
- Release changelog: `raw/github/braintree/braintree_android/snapshots/2026-10-04-438d33a/files/CHANGELOG.md`
- Dependency-document mismatch: `raw/github/braintree/braintree_android/snapshots/2026-10-04-438d33a/files/DEPENDENCIES.md`
- Core dependency alias: `raw/github/braintree/braintree_android/snapshots/2026-10-04-438d33a/files/BraintreeCore/build.gradle`
- Compatibility/build metadata: `raw/github/braintree/braintree_android/snapshots/2026-10-04-438d33a/files/build.gradle`
- Setup and migration: `raw/github/braintree/braintree_android/snapshots/2026-10-04-438d33a/files/README.md` and `raw/github/braintree/braintree_android/snapshots/2026-10-04-438d33a/files/v5_MIGRATION_GUIDE.md`

- Snapshot manifest: `raw/github/braintree/braintree_android/snapshots/2026-08-01-51f183a/manifest.json`
- Release manifest: `raw/github/braintree/braintree_android/releases/braintree-android/5.30.0/2026-08-01/manifest.json`
- Release notes: `raw/github/braintree/braintree_android/releases/braintree-android/5.30.0/2026-08-01/release-notes.md`
- README: `raw/github/braintree/braintree_android/snapshots/2026-08-01-51f183a/files/README.md`
- Repository changelog: `raw/github/braintree/braintree_android/snapshots/2026-08-01-51f183a/files/CHANGELOG.md`
- v5 migration guide: `raw/github/braintree/braintree_android/snapshots/2026-08-01-51f183a/files/v5_MIGRATION_GUIDE.md`
- PayPal source: `raw/github/braintree/braintree_android/snapshots/2026-08-01-51f183a/files/PayPal/`
- Venmo source: `raw/github/braintree/braintree_android/snapshots/2026-08-01-51f183a/files/Venmo/`
- Card UI source: `raw/github/braintree/braintree_android/snapshots/2026-08-01-51f183a/files/UIComponents/`
- 3D Secure source: `raw/github/braintree/braintree_android/snapshots/2026-08-01-51f183a/files/ThreeDSecure/`
