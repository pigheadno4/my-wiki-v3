---
title: "Stripe"
type: company
tags: [stripe, payment-gateway, payment-intents, checkout, subscriptions, elements, webhooks, payment-links]
source_count: 666
---

## Stripe

Stripe is a global payments infrastructure company providing APIs and SDKs for accepting payments, managing subscriptions, invoicing, and financial automation. It competes directly with PayPal in the payment processing space but targets developers with a code-first integration model.

## Key Products

### Checkout Sessions API (Recommended)

Stripe's recommended API for most payment integrations. Manages the full checkout lifecycle with built-in tax, discounts, shipping, subscriptions, and Adaptive Pricing. Requires significantly less code than Payment Intents.

**3 UI modes**: Stripe-hosted page (redirect), Embedded form, Custom (`ui_mode: "custom"` with Stripe Elements).

Use Payment Intents instead only if you need full checkout state control or plan to build discount/tax/subscription/currency logic yourself.

See [[source-stripe-checkout-sessions]].

### Payment Intents API

The API tour illustrates a PaymentIntent tracking the intent to collect a payment through a simplified flow. It is not a claim that every Stripe payment path uses the same object or that the diagram exhausts its transitions. See [[source-stripe-api-tour]].

The dated API tour says a failed payment **can** be retried by confirming the same PaymentIntent, **usually** with new payment details. It does not make this an unconditional retry obligation or guarantee success. See [[source-stripe-api-tour]].

**Full lifecycle**: `requires_payment_method` → `requires_confirmation` → `requires_action` (3DS) → `processing` → `succeeded`; or `requires_capture` (auth+capture flow).

> [!info] Stripe recommends **Checkout Sessions over Payment Intents** for most integrations — same use cases, less code. Adaptive Pricing only available with Checkout Sessions.

### PaymentMethod

API object representing stored payment credentials (card, bank, wallet). Can be saved for future charges via the SetupIntents API.

### Charge

The dated API tour says **in most cases** confirmation creates a Charge representing a particular attempt to move money; that attempt can succeed or fail. Its simplified diagram is not an exhaustive lifecycle contract. See [[source-stripe-api-tour]].

### Stripe Elements

Drop-in UI components for custom integrations. Enables custom-built checkout flows while Stripe handles PCI compliance and UI rendering.

The `@stripe/stripe-js` npm package is the web loader and TypeScript declaration layer for Stripe.js, not a self-hosted runtime. The retained history covers v8.11.0 on `clover`, the v9.12.1 transition to `dahlia`, and approved deltas through v9.16.0, while preserving standard and deferred `/pure` entrypoints and server-side `null` behavior. V9.13.0 adds Checkout Form promotion-code display control and makes wallet visibility creation-only; v9.14.0 adds updateable wallet contact requirements, embedded Custom Payment Method rendering, a beta Express Checkout CPM surface, and an Embedded Checkout dynamic-shipping deprecation; v9.15.0 adds typed ConfirmationToken metadata and an Elements `buttonBoxShadow` appearance variable. V9.16.0 adds beta Link Signup declarations and Checkout tiered/package pricing response types; typed line-item mocks need new required-but-nullable fields. This does not prove beta eligibility, React exports, or hosted-runtime behavior. See [[source-github-stripe-js]].

`@stripe/react-stripe-js` is the separate React binding layer. Its retained history through `6.10.0` provides standard Elements, provider-specific Checkout Elements and beta Checkout Form hooks, Embedded Checkout, SSR-safe initialization, and typed component lifecycle. Version `6.8.1` makes Checkout Sessions plus `ui_mode: 'elements'` the recommended path for most new custom React checkout pages and modernizes demos to typed TSX and Storybook 10; `6.8.2` adds readiness, submission, error, client-secret, and server-response checks. Those patches preserve the 6.8.x peer range `>=9.5.0 <10.0.0`. Version `6.9.0` raises the Stripe JS minimum to `>=9.10.0 <10.0.0` without changing retained runtime APIs; CI adds minimum-peer checks. Version `6.10.0` adds beta Link Signup wrappers for standard Elements and Checkout Elements, explicitly excluding Checkout Form, and raises the peer floor to `>=9.16.0 <10.0.0`. These separately collected React exports do not independently prove runtime rollout or merchant eligibility. See [[source-github-react-stripe-js]].

`@stripe/stripe-react-native` is the mobile bridge to Stripe's native iOS and Android SDKs. The cumulative source preserves the legacy `0.65.1` capsule, the approved `0.72.0` baseline, and deltas through `0.75.0`. Version `0.72.0` made Link SetupIntent confirmation an explicit post-selection step; `0.73.0` adds private-preview Link configuration, Tempo typing, and corrected nested iOS deferred-capture parsing; `0.74.0` adds per-request iOS Apple Pay network restriction and wraps Stripe Android `23.15.0` plus Stripe iOS `26.6.0`. Its Connect notification banner remains experimental and non-root-exported. See [[source-github-stripe-react-native]] and [[changelog-github-stripe-react-native]]. Version `0.75.0` adds Android Samsung Pay for Crypto Onramp, five wallet-verification error types, and native pins Android `23.16.0`/iOS `26.7.0`; Samsung's SDK must be supplied by the app.

React Native `0.76.0` adds authenticated Onramp wallet deletion and advances native pins to Android `23.17.1`/iOS `26.9.0`. Its newly exported Checkout private-preview controller/hook/view are explicitly unimplemented. Earlier 0.75.0 native Checkout was already unavailable; the replacement is not evidence of a usable mobile Checkout flow. Ordinary Intent-based PaymentSheet remains separate. See [[source-github-stripe-react-native]] and [[stripe-react-native-sdk]].

React Native `0.77.0` requires new architecture, migrates Android Google Pay creation to Activity Result handling, adds KYC ID types, and pins Android `23.19.0`/iOS `26.11.0`. Checkout mapper scaffolding does not change the unimplemented public-API boundary. Older versions remain queryable in [[changelog-github-stripe-react-native]].

React Native `0.78.0` defaults native iOS dependency resolution to SPM on RN >=0.75 and requires dynamic frameworks; the wrapper still needs `pod install`. CocoaPods fallback and older RN are deprecated. Checkout controller creation/mutations gain partial native wiring, but presentation/confirmation/server-update and the hook/view remain unimplemented. Native pins: Android `23.20.0`/iOS `26.12.0`. See [[stripe-react-native-sdk]] for migration and platform-specific gaps.

React Native `0.79.0` pins Android `23.21.0`/iOS `26.12.1`, fixes Connect loading appearance and implements the reactive Checkout hook/server-update callback. Presentation, confirmation and the embedded view remain unimplemented; this is partial preview support, not an end-to-end payment flow. See [[source-github-stripe-react-native]].

React Native `0.80.0` adds Financial Connections pre-collected consent in private preview and inline Checkout element rendering. Consent uses a server-issued ID and the buyer's original affirmative-acceptance timestamp in seconds; Stripe may still show consent UI. Inline rendering does not enable the still-unimplemented modal presentation/payment confirmation. Native versions remain Android `23.21.0`/iOS `26.12.1`. See [[stripe-react-native-sdk]] and [[changelog-github-stripe-react-native]].

React Native `0.81.0` adds native private-preview Checkout presentation/confirmation bridges on both platforms, replacing the prior stubs. Presentation resolves after request, not dismissal/selection; confirmation preserves payment status and is not paid-funds proof. CustomerSession request correlation/error handling and Android host/PromiseViewModel wiring address announced crash/loading/presentation fixes without proving every lifecycle case. Financial Connections adds session IDs; Android ConfirmationToken FutureUsage casing/null mapping is corrected. Native pins: Android `23.22.0`, iOS `26.13.0`. Preview access and platform mutation gaps remain; see [[stripe-react-native-sdk]], [[stripe-checkout]] and [[source-github-stripe-react-native]].

React Native `0.82.0` adds a nullable private-preview Checkout Currency Selector when configured and Adaptive Pricing is available. Payment Element generic view props and Checkout-only testEnv/save-opt-in options are removed; iOS email and Android null-shipping updates now bridge natively. Android adds theme-aware icons/default-phone/appearance mapping and lifecycle/font/build fixes. Onramp gains country hint/contact-prefill contracts with contacts distinct from KYC submission; the later raw note's retrospective 0.81.0 attribution is preserved separately from the observed 0.81.0 -> 0.82.0 bridge boundary. Native pins are Android `23.23.0`/iOS `26.14.0`, not the newer native releases. All earlier knowledge remains; source inspection is not device/payment or merchant-access proof. See [[stripe-react-native-sdk]], [[stripe-crypto-onramp]], [[source-github-stripe-react-native]] and [[changelog-github-stripe-react-native]].

`stripe-android` is the native Android SDK behind Stripe's prebuilt and low-level mobile payment surfaces. The cumulative source preserves the legacy `23.8.0` capsule and adds the approved `23.13.1` baseline: builder-first PaymentSheet, FlowController, Embedded Payment Element, direct Intent APIs, Google Pay, and specialized Connect, Identity, Financial Connections, Crypto Onramp, messaging, and card-scan modules. A completed SDK result can still represent a processing payment, so fulfillment remains webhook-gated. See [[source-github-stripe-android]] and [[changelog-github-stripe-android]].

The approved additive `stripe-android@23.24.0` baseline moves the preview ApiConfigurationPreview import to com.stripe.android.core, adds Mondu/Naira bank-transfer/USSD/Wallet declarations with announced PaymentIntent PaymentSheet support, and exposes a library-restricted Onramp KYC delegate. Wallet labels, country autofill and Identity test-mode uploads remain announcement-qualified; eligibility and excluded runtime behavior are not inferred. Earlier platform floors/history and retrospective changelog labels remain preserved in [[source-github-stripe-android]], [[changelog-github-stripe-android]] and [[stripe-android-sdk]].

`stripe-ios` is the native Swift SDK behind Stripe's prebuilt and low-level iOS payment surfaces. The cumulative source preserves the legacy `25.14.0` capsule and adds the approved `26.4.1` baseline: PaymentSheet, FlowController, Embedded Payment Element, CustomerSheet, Apple Pay, low-level Intent and 3DS APIs, and specialized Connect, Identity, Financial Connections, Issuing, and alpha Crypto Onramp modules. The `26.5.0` delta adds private-preview Link billing/appearance configuration and retained selection, presentation, and internal Checkout confirmation changes; alpha Tempo registration is release-note-only evidence. Version 26 requires iOS 15+, and a completed SDK result can still represent a processing payment, so fulfillment remains event-gated. See [[source-github-stripe-ios]] and [[changelog-github-stripe-ios]].

`stripe-terminal-ios` is the separate native SDK for card-present checkout and reader control. The retained `StripeTerminal@5.8.0` baseline covers backend-issued ConnectionTokens, reader discovery and connection, Tap to Pay, split and combined payment/SetupIntent flows, in-person refunds, offline forwarding, reader updates, QR methods, and the v5 iOS 15 migration boundary. Manual capture and authoritative reconciliation remain backend responsibilities. The additive `5.8.1` delta records Stripe's offline Tap to Pay/onBehalfOf parameter-preservation fix; proprietary binary behavior is not independently verified. The additive `6.0.0` major requires iOS 16, announces SPM-only future updates (including older-major patches), defaults SDK-side creation to automatic-async capture, and migrates consent configuration, card/Intent models and reader delegates. Refund/MSI/Swish previews remain access-gated; both v5 and v6 branch histories are retained. See [[source-github-stripe-terminal-ios]] and [[changelog-github-stripe-terminal-ios]].

The `stripe-ios@26.6.0` additive baseline adds MB WAY/Bizum PaymentSheet support, private-preview Link error propagation, and alpha wallet deletion. Expanded native Checkout SPI evidence exposes unfinished confirmation-result mapping and wallet/UI actions; it is not a production integration recommendation. Older native SDK history remains in [[source-github-stripe-ios]] and [[changelog-github-stripe-ios]].

The `26.7.0` delta adds PaymentSheet's Financial Connections Lite dependency (manual/Carthage embedding required), Link button hiding without disabling Link, autocomplete flag changes and typed Vipps support. Eligibility remains unverified; its outer Checkout code is excluded, so the unfinished finding above remains specific to 26.6.0.

The `26.8.0` additive baseline retains CheckoutController SPI confirmation-result mapping through a bounded supplement, without proving full Apple Pay behavior or general availability. It also adds FPX banks, preserves decline text after 3DS, and exposes private-preview Link permissions and low-level Alipay/Klarna options. Earlier history remains intact in [[source-github-stripe-ios]] and [[changelog-github-stripe-ios]].

The `26.9.0` additive baseline adds five payment-method API bindings and broader Checkout SPI polling, result and creation-visibility changes. Polling timeout and client completion are not settlement proof. Current Apple Pay and delegated API internals remain explicit evidence gaps. See [[source-github-stripe-ios]] and [[changelog-github-stripe-ios]]; older versions remain queryable.

The `26.10.0` delta records announced PaymentSheet support for Naver Pay, Korean cards, PAYCO and SeQura, plus Arabic localization. Retained code changes PaymentIntent-only mandate inference and adds scoped branding, Identity and rendering behavior. Excluded implementation and merchant eligibility remain explicit limits in [[source-github-stripe-ios]] and [[changelog-github-stripe-ios]].

The `26.11.0` additive baseline adds Scalapay bindings/support announcements and Checkout SPI no-method/missing-Intent confirmation changes. A timeout can still yield SDK completion with an open session; this is not payment proof. Revised Link visibility documentation and the retrospective Kakao Pay note remain version-qualified in [[source-github-stripe-ios]] and [[changelog-github-stripe-ios]].

The `26.13.0` iOS delta adds MoMo/GoPay/ShopeePay bindings and announced PaymentIntent support, with MoMo processing distinct from the other two in client completion. FlowController preserves Checkout updater plumbing; alpha CryptoOnramp adds pre-auth Apple Pay collection, merchant-of-record hint/cache handling and delegated additional KYC. Announced Apple Pay/card-brand/currency fixes and excluded internals remain explicitly qualified; older history is retained in [[source-github-stripe-ios]] and [[changelog-github-stripe-ios]].

The `26.14.0` iOS additive baseline adds nine payment-method bindings/support announcements, shared-container presentation, structured display labels and alpha Apple Pay KYC-region revalidation with explicit recollection recovery. New-method processing is not client success; account eligibility, concrete presentation internals and the announced redirect-crash repair remain bounded evidence. Older native history stays in [[source-github-stripe-ios]] and [[changelog-github-stripe-ios]].

The `26.15.0` iOS additive baseline records the plural alpha KYC method/result rename, wallet funding-label forwarding, native Identity test-mode placeholder uploads and flow-stable presentation plumbing. The deferred preparation path drops one saved-method Radar helper while ordinary Radar session APIs remain; image substitution does not mean all camera/PII handling stops. Historical attribution and excluded/runtime boundaries remain in [[source-github-stripe-ios]] and [[changelog-github-stripe-ios]].

The `26.15.1` iOS additive baseline removes CocoaPods support after its final 26.15.0 release; future updates require SPM or manually linked XCFrameworks. Existing apps do not automatically stop working. It also announces a React Native initialization fix for slow Apple Pay checks and records internal Checkout request/SEPA/challenge and SPI lifecycle changes. Those implementation findings are not public Checkout integration guarantees; all earlier history and evidence limits remain in [[source-github-stripe-ios]] and [[changelog-github-stripe-ios]].

React Native `0.83.0` adds opt-in private-preview Checkout shipping-address UI and incompatible preview type changes, plus Connect initialization serialization repair and Android keyless-autocomplete deprecation guidance. Presentation resolves before selection/dismissal; native pins are Android 23.24.0/iOS 26.15.0. Ordinary PaymentSheet remains separate and earlier history is preserved in [[source-github-stripe-react-native]] and [[changelog-github-stripe-react-native]].

React Native `0.84.0` requires RN >=0.75 and native iOS SPM/dynamic frameworks; legacy SPM opt-outs now error, while the wrapper still needs pod install. It removes public root/type-barrel Checkout preview exports but retains internal implementation, adds internal shipping appearance/Apple Pay hide configuration, repairs Android PaymentSheet callback-kind switching and Connect navigation/CSV export routing. Native pins: Android 23.25.1/iOS 26.15.1. The exact-SHA SPM helper is separately retained; this is not a new public Checkout integration or runtime verification. Earlier versions remain in [[source-github-stripe-react-native]].

### AI Developer and Token-Billing Tooling

At the August `1953b6c` baseline, the `stripe/ai` repository supplies independently versioned LLM token-billing packages, a local bridge to Stripe's remote MCP server, TypeScript and Python agent toolkits, provider-specific agent skills/plugins, and integration benchmarks. At that SHA, token billing is private preview, the Stripe AI SDK proxy does not support tool calling, native token-meter delivery is fire-and-forget, and the agent toolkits require remote MCP availability.

At the November `1bb4869` baseline, the repository focuses on active skills, provider plugins, and benchmarks. It directs agent integrations to hosted Stripe MCP and deprecates the local MCP bridge, both old toolkits, and both LLM token-billing packages without further updates. See [[source-github-ai]] and [[changelog-github-ai]] for the exact-SHA evidence and retained history.

### Operational Data Synchronization

`stripe/sync-engine` is an experimental Stripe-to-Postgres synchronization framework with OpenAPI-driven discovery, resumable backfill, event and webhook live paths, account-qualified records, PostgreSQL projection, and Temporal orchestration. The retained baseline is exact default-branch commit `93321ab`, not a tagged `0.2.5` release. It assumes trusted internal deployment, exposes an unauthenticated internal query endpoint, and redirects active development to a separately owned fork. See [[source-github-sync-engine]] and [[changelog-github-sync-engine]].

### Stripe Apps

`stripe/stripe-apps` provides manifest schemas and examples for embedding custom UI extensions in the Stripe Dashboard. The retained `default-branch@9b14b71` baseline covers standard, local-development, and extension manifests plus a full-page React example. The example is fully mock-backed, its manifest drifts from the retained standard schema, and payment-related permission enums do not establish a live Checkout flow or merchant eligibility. See [[source-github-stripe-apps]], [[changelog-github-stripe-apps]], and [[stripe-apps]].

### Stripe CLI

Latest curated release: `stripe-cli@1.55.3`; parent-grouped account lists, explicit stale-context authorization and invalid_scope re-login handling, preserving all earlier releases. History and limitations: [[source-github-stripe-cli]], [[changelog-github-stripe-cli]].

`stripe-cli@1.50.0` is Stripe's command-line developer and test tool for direct API requests, fixtures, synthetic event triggers, local webhook forwarding, request-log streaming, and account or sandbox contexts. Its embedded trigger payloads are test recipes rather than canonical API lifecycle evidence. The exact `1.50.0` release note adds agent identity metadata to telemetry; it does not establish the rest of the baseline as new in that release. See [[source-github-stripe-cli]], [[changelog-github-stripe-cli]], and [[stripe-cli]].

The additive `1.50.1` ingest adds exact OAuth access-service destination checks, disabled redirects and trusted browser-host checks, attempted old-session revocation on `--new-session`, error categories, raw agent-host telemetry, and internal proxy/Unix-socket routing. It does not establish a new merchant checkout capability. Feedback-command and credential-RPC details remain outside the retained capsule. See [[source-github-stripe-cli]] and [[changelog-github-stripe-cli]].

### Link CLI for Agents

`@stripe/link-cli@0.13.0` is a separate consumer-wallet tool for agents, not the merchant developer Stripe CLI. It uses user-approved Link spend requests to issue a virtual card for standard checkout, a one-time Shared Payment Token for Stripe MPP `402` payments, or a merchant-bound Link Pay Token for supported AI-agent steering surfaces. It also exposes read-only financial-insight commands, local and HTTP MCP modes, and credential-file protections. The internal `@stripe/link-sdk` is private, and the retained Web Bot Auth code is not registered as a CLI command. See [[source-github-link-cli]], [[changelog-github-link-cli]], and [[stripe-link-cli]].

### Stripe PHP SDK

Latest additive ingest: `stripe-php@22.0.0`; PHP7.4/API `2026-09-30.endive`, callback account-context fix, singleton/thin event expansion and request/Billing migration contracts. All 21.2.x/21.3.x history remains, including the original 21.2.0 paragraph below. See [[source-github-stripe-php]], [[changelog-github-stripe-php]] and [[stripe-php-sdk]].

`stripe-php@21.2.0` is Stripe's retained server-side PHP SDK baseline, pinned to Stripe API `2026-07-29.dahlia` and requiring PHP 7.2+. It covers Checkout, PaymentIntents, SetupIntents, Payment Links, subscriptions, webhooks and event notifications, and Terminal server operations. Public webhooks still require signature verification; the v21.2.0 `WithoutVerification` helpers are only for previously verified or trusted payloads. See [[source-github-stripe-php]], [[changelog-github-stripe-php]], and [[stripe-php-sdk]].

### Stripe Node SDK

The cumulative Node server SDK evidence preserves v22 through `stripe@22.6.2` and now adds a full `stripe@23.0.0` baseline: Node20+, Endive API `2026-09-30.endive`, selected request-field/API removals, callback-client context binding fix, explicit subscription pause and generated checkout/Billing contracts. V22 webhook guards, request/upload hardening, coercion and idempotency findings remain versioned history. The v23 exact-SHA handler supplement addresses the earlier shallow-copy issue; source tracing is not live routing proof. Webhook zero-tolerance behavior differs between snapshot and thin parsers, and stale retry/pause comments remain flagged. See [[source-github-stripe-node]], [[changelog-github-stripe-node]], [[stripe-node-sdk]] and [[stripe-subscriptions]]. No account or payment-method eligibility is inferred.

### Express Checkout Element

Single component that renders multiple one-click payment buttons (Link, Apple Pay, Google Pay, PayPal, Klarna, Amazon Pay). Buttons are dynamically sorted by customer location. New payment methods activate from the Dashboard — no frontend changes needed. See [[stripe-express-checkout-element]].

### Stripe Checkout

Hosted payment page. Stripe creates the PaymentIntent and handles confirmation, events, and responses.

### Payment Links

Stripe-hosted shareable payment URLs, with no-code Dashboard creation and separate embedded/API integration routes. The captured create guide broadly describes Adaptive Pricing as enabled; the API-only US automatic-surcharge private preview is incompatible with it and excludes subscriptions. Payment-method availability and preview access remain qualified. See [[source-stripe-payment-links]].

> [!warning] Contradiction
> The create guide’s broad Adaptive Pricing wording must retain the separate dated surcharge-preview exception. Link creation, a persistent QR code and checkout completion alone do not establish payment success or settlement; delayed methods require the documented payment confirmation and fulfillment handling. See [[stripe-payment-links]] and [[source-stripe-payment-links]].

**3 sharing surfaces**: direct URL (email/SMS/social), embeddable buy button (`<stripe-buy-button>` web component), QR code (never expires).

**Key customization**: payment limits (`restrictions.completed_sessions.limit`), adjustable quantities, custom fields (text/number/dropdown), address/phone/name collection, Stripe Tax, ToS consent, custom domain (`pay.example.com` instead of `buy.stripe.com`), UTM tracking + `client_reference_id` for reconciliation.

**Supports subscriptions** via recurring price; Smart Retries + reminders apply to subscription links only.

See [[stripe-payment-links]].

### Subscriptions & Invoicing

Recurring billing via Subscription objects. Also supports standalone Invoicing.

### Events & Webhooks

`Event` objects represent activity such as a Charge succeeding or failing. The API tour describes prewritten responses for parts of Checkout and Payment Links, while merchant fulfillment still follows documented payment-outcome handling; a completed Session may precede success for delayed methods. See [[source-stripe-api-tour]] and [[source-stripe-payment-links]].

## Android SDK 23.25.0 Update

The additive `stripe-android@23.25.0` delta adds Touch 'n Go/TrueMoney API declarations and an Onramp card-funding display getter. PaymentSheet method support and address-discard confirmation remain announcement-qualified; eligibility, request routing and UI behavior are not execution-tested. The newer changelog backdates Link email OTP/MFA support to 23.24.0; preserve that attribution without calling it a new 23.25.0 feature. All earlier SDK history remains in [[source-github-stripe-android]], [[changelog-github-stripe-android]] and [[stripe-android-sdk]].

The following `23.25.1` delta announces a Link-return PaymentSheet error-display fix and adds a retained AndroidX WebKit dependency declaration, not a new payment/authentication API. The relevant fix implementation and exact resolved WebKit version remain outside the capsule; all earlier Android history is preserved. [[source-github-stripe-android]] [[changelog-github-stripe-android]]

## API Deprecations

| API | Dated documentation |
| --- | --- |
| Sources API for local payment methods | The April and November 2026 Older APIs captures describe planned removal of acceptance through Sources and direct users to migrate. |
| Sources API for cards and legacy Cards | The November Older APIs overview says Sources card acceptance is deprecated with no then-current shutoff plan. The separate November transition guide describes planned removal and required migration. |
| Charges API | The November Charges guides describe planned removal of card-payment creation and direct new integrations to Checkout or PaymentIntents. Charge reads and refunds have separate documentation. |
| Legacy ACH | The November dedicated legacy ACH guide bars new onboarding, directs new integrations to ACH Direct Debit, and recommends migration for existing integrations. |

See [[source-stripe-legacy-apis]] for exact dates, source discrepancies, and migration routes.

## Core Philosophy

- **Everything is an object** — all activity (balance, subscriptions, payment methods) maps to an API object, even Dashboard actions
- **Objects are state machines** — track process state via `status` field
- **Integrations are cooperating objects** — combine PaymentIntent + PaymentMethod + Charge + Event + Customer etc.

## Integration guide routes

| Path | Who controls flow |
| --- | --- |
| Payment Intents (direct) | Developer |
| Stripe Elements | Developer (UI) + Stripe (PCI) |
| Stripe Checkout | Stripe |
| Payment Links | Stripe (no-code) |
| Subscriptions/Invoicing | Developer + Stripe |

The API tour links five guides—Payment Links, Checkout, Subscriptions, Invoicing and Payment Intents—and describes Elements separately as UI within integrations. The table groups products for orientation; it is not an exhaustive taxonomy. See [[source-stripe-api-tour]].

### Stripe.js 10.1.0 Loader and Typed Delta

`@stripe/stripe-js@10.1.0` fixes 10.0.0 shared-loader concurrency by caching the in-flight constructor load including its single retry. Public calls still create separate Stripe instances; payment operations are not retried. Adds accordion trigger normal/selected/hover appearance colors and WeChat Pay direct-confirmation `mobile_web` typing. Endive and runtime/eligibility boundaries remain unchanged. README train table is corrected but its manual Dahlia URL remains stale. See [[source-github-stripe-js]], [[changelog-github-stripe-js]], [[stripe-elements]] and [[stripe-wallets]].

### Stripe.js 10.0.0 Endive Baseline

`@stripe/stripe-js@10.0.0` targets Endive, removes Payment Request Button declarations and explicit mode-based Elements payment-method-list fields, and adds Pay by Bank confirmation/BLIK setup typing. The lower-level PaymentRequest API remains. Its single script-load retry does not retry payment operations; a missing shared in-flight cache creates a version-specific concurrency risk, separate from the standard entrypoint cache. README train guidance is stale. Existing v8/v9 history, source count, eligibility and hosted-runtime boundaries remain. See [[source-github-stripe-js]] and [[changelog-github-stripe-js]].

### Stripe.js 9.17.0 Consent Types

`@stripe/stripe-js@9.17.0` adds optional beta pre-collected consent evidence to four Financial Connections/bank-account collection methods. It does not guarantee skipping the consent pane, establish an ACH mandate, or change the loader. See [[source-github-stripe-js]] and [[stripe-ach-direct-debit]].

## React Stripe.js 7.0.0 Update

The full `@stripe/react-stripe-js@7.0.0` baseline removes the Payment Request Button React wrapper/types/demos and requires Stripe JS `>=10.0.0 <11.0.0`. React/React DOM peers still permit `>=16.8.0 <20.0.0`; React 19 is the development baseline, not the sole allowed consumer version. Standard Elements gains a scoped initialization guard and Checkout hooks retain provider-kind errors. Deprecated `useCheckout()` is still exported despite its stale promised-v7-removal comment; prefer provider-specific hooks. Migration to retained Express Checkout is not just a component rename. Prior history, source count and underlying hosted-runtime/eligibility limits remain intact. See [[source-github-react-stripe-js]], [[changelog-github-react-stripe-js]] and [[stripe-express-checkout-element]].

## React Stripe.js 6.11.0 Update

React binding update: `@stripe/react-stripe-js@6.11.0` improves Checkout initialization-error reporting and separates SDK context from session changes, with memoized hook results. Peer ranges remain unchanged; no automatic retry or new payment capability is added. Earlier release history is retained in [[source-github-react-stripe-js]].

## Sources

The `@stripe/react-stripe-js@6.12.0` delta adds standalone `TreasuryDisclosure` for Financial Accounts, with unchanged checkout code and dependencies. Returned-error callbacks do not cover rejected promises, and the wrapper lacks post-await unmount/race guards. This is not eligibility or compliance proof. See [[stripe-financial-account-disclosures]] and [[source-github-react-stripe-js]].

- [[source-github-stripe-js]] — cumulative `stripe/stripe-js` v8.11.0 through v10.1.0: Endive full baseline, loader concurrency fix, versioned Elements/Checkout/payment contracts and historical evidence
- [[changelog-github-stripe-js]] — package-qualified Stripe JS release history
- [[source-metronome-integrations-tax-integrations-stripe-tax]] — Stripe Tax on Metronome-created Stripe invoices, including customer and product mapping
- [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-manual-payment-gated-commits]] — Stripe product mapping, invoice voiding, and retry boundary for a Metronome-gated commit
- [[source-metronome-guides-customers-billing-manage-customers-schedule-billing-provider-change]] — contract invoice-routing transitions between Stripe, NetSuite, and marketplaces
- [[source-github-stripe-postman]] — Stripe API Postman collection: 107 endpoint groups, 4 versioned collections in public workspace, fork/import setup, 2024-04-15 changelog
- [[source-github-stripe-android]] — cumulative Android SDK through v23.25.1: method/display declarations, Link error-display announcement, dependency and historical attribution limits; older knowledge retained
- [[changelog-github-stripe-android]] — package-qualified Android history through v23.25.1; contracts, announcements and retrospective attribution distinguished
- [[source-github-stripe-ios]] — cumulative SDK through v26.15.1: CocoaPods-to-SPM/XCFramework migration, announced initialization fix and internal Checkout/SPI changes; all earlier baselines and evidence limits preserved
- [[changelog-github-stripe-ios]] — package-qualified iOS history through v26.15.1; migration, compatibility, release announcements and preserved historical attribution
- [[source-github-stripe-terminal-ios]] — `StripeTerminal@6.0.0` additive major: SPM, iOS 16, capture/consent/model/delegate migration; v5.8.0/5.8.1 retained
- [[changelog-github-stripe-terminal-ios]] — package-qualified v5/v6 Terminal iOS history, previews and divergent-branch/runtime evidence limits
- [[source-github-stripe-terminal-android]] — `stripeterminal@6.0.0` additive major: capture/consent/models/listeners/build migration; 5.8.0/5.8.1/5.8.2 retained
- [[changelog-github-stripe-terminal-android]] — package-qualified v5/v6 Android Terminal history, UnionPay deltas, migration and runtime/evidence limits
- [[source-github-stripe-react-native]] — cumulative SDK through v0.84.0, mandatory SPM/RN floor, internal Checkout boundary, callback/Connect fixes and native pins; all older knowledge preserved
- [[changelog-github-stripe-react-native]] — package-qualified release history through v0.84.0, including migrations, release attribution and implementation boundaries
- [[source-github-ai]] — exact-SHA Stripe AI evidence: hosted MCP, active skills/plugins, benchmarks, and historical packages
- [[changelog-github-ai]] — August component baseline and November exact-SHA migration
- [[source-github-stripe-cli]] — additive Stripe CLI history from `1.50.0` through `1.55.3`, including authentication, account grouping, request encoding and tooling evidence boundaries
- [[changelog-github-stripe-cli]] — package-qualified Stripe CLI history through `1.55.3`, retaining baseline and evidence gaps
- [[source-github-link-cli]] — `@stripe/link-cli@0.13.0` agent wallet baseline: virtual cards, SPT/MPP, Link Pay Token, spend requests, MCP, and financial insights
- [[changelog-github-link-cli]] — package-qualified Link CLI baseline and exact `0.13.0` financial-insight and duplicate-request messaging changes
- [[source-github-sync-engine]] — `default-branch@93321ab` operational data baseline: Stripe discovery, backfill, live events, Postgres destination, state, and Temporal workflows
- [[changelog-github-sync-engine]] — commit-qualified Sync Engine baseline, documentation drift, trust boundaries, and future comparison rule
- [[source-github-stripe-apps]] — `default-branch@9b14b71` Stripe Apps baseline: manifest schemas, Dashboard UI extensions, full-page example, and mock-data boundaries
- [[changelog-github-stripe-apps]] — commit-qualified Stripe Apps baseline, schema/example drift, and future comparison rule
- [[source-github-stripe-php]] — cumulative Stripe PHP through `22.0.0`: PHP7.4/Endive, event context, Checkout/Billing migrations and all retained v21 history
- [[changelog-github-stripe-php]] — package-qualified Stripe PHP release history through `22.0.0`, with exact-SHA evidence and separate full/delta entries
- [[source-stripe-billing-benchmarks]] — billing benchmarking: k-NN peer matching, ≥5 subs access, peer eligibility ≥100 subs, 7 metrics benchmarked, percentile display
- [[source-stripe-billing-analytics]] — Stripe Billing's Dashboard analytics guide defines recurring-revenue, subscriber, trial, churn, retention, and usage metrics. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-subscriptions-backdate]] — backdating: classic vs flexible line items, 3 patterns (charge/no-charge/anchor), coupon duration counts from backdate not API call
- [[source-stripe-subscriptions-schedules]] — Stripe's subscription schedules create a subscription or attach to an existing one, then apply sequential phases to automate changes over time. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-billing-taxes-migration]] — The May 13 and November 7, 2026 captures describe two ways to migrate existing [[stripe]] Billing subscriptions to [[stripe-tax]]: automated Dashboard tooling and manual updates through Dashboard or API. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-billing-customer-tax-ids]] — Stripe Billing's customer tax ID guide covers storing, validating, and rendering customer tax IDs. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-billing-taxes-collect]] — The 2026-05-13 capture of this Stripe Billing guide contains two complete variants for recurring-payment tax collection: Stripe Tax, an automated paid product, and manually defined Tax Rates, a free feature. (S02 reviewed update, 2026-11-09; dated source qualifications apply.) The November capture supplies variant navigation; functional details remain attributed to earlier full captures.
- [[source-stripe-subscriptions-third-party]] — Stripe's combined 2026-05-13 guide documents two ways to use Billing subscriptions and invoices with a third-party processor: an own-processor path with custom PaymentMethods and PaymentRecords, and a separate out-of-band invoice path. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-subscriptions-pause-payment]] — Guide to `pause_collection` on a subscription. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-subscriptions-ideal]] — The 2026-11-07 capture of this canonical URL is an index to hosted and Direct API variants, not either variant's instructions. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-subscriptions-twint]] — The May 13, 2026 guide describes three TWINT subscription examples: Stripe-hosted Checkout, Setup Intents API, and Subscriptions API. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-subscriptions-stablecoins]] — The May 13, 2026 full guide covers subscription payments from a customer's crypto wallet through three paths: Stripe-hosted Checkout, Payment Intents API, and Setup Intents API. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-subscriptions-sepa-debit]] — The May 13, 2026 guide documents two SEPA Direct Debit subscription examples: a hosted Checkout page and an advanced web integration. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-subscriptions-acss-debit]] — Stripe's Canadian pre-authorized debit (ACSS/PAD) subscription guide describes server-side Subscription creation and client-side Stripe.js `stripe.confirmAcssDebitPayment` for bank details and mandate acknowledgment. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-subscriptions-naver-pay]] — The 2026-05-13 capture is a full Naver Pay subscription guide with SetupIntents-labeled, Subscriptions API, and Stripe-hosted Checkout variants. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-subscriptions-kakao-pay]] — The 2026-05-13 capture is a full Kakao Pay subscription guide with SetupIntents-labeled, Subscriptions API, and Stripe-hosted Checkout variants. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-subscriptions-kr-card]] — Stripe's 2026-05-13 capture explains three `kr_card` subscription integration variants: SetupIntents, direct Subscriptions API with PaymentIntent confirmation, and a Stripe-hosted Checkout page. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-subscriptions-revolut-pay]] — The May 13, 2026 full guide documents three Revolut Pay subscription paths: SetupIntents API, direct Subscriptions API plus PaymentIntent confirmation, and a Stripe-hosted Checkout page. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-subscriptions-pix]] — The 2026-11-07 capture of this canonical URL is a 15-line navigation index pointing to Stripe-hosted Checkout, Setup Intents API, and Subscriptions API variants. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-subscriptions-paypal]] — Stripe's May 2026 PayPal subscription guide describes two paths: Stripe-hosted Checkout and a Direct API flow using a SetupIntent and PayPal billing agreement. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-subscriptions-klarna]] — The 2026-05-13 Klarna subscription guide contains two paths: Stripe-hosted Checkout, which it recommends for saving Klarna as a payment method, and an advanced Payment Element integration. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-subscriptions-cash-app-pay]] — The 2026-05-13 combined guide describes three Cash App Pay subscription paths: Setup Intents API (save a payment method, then subscribe), Subscriptions API (create and confirm separately), and a Stripe-hosted Checkout page. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-subscriptions-becs-debit]] — Stripe's Australian BECS Direct Debit subscription guide uses a Dashboard Product and recurring Price, a server-created SetupIntent, client-side Australia Bank Account Element and DDR authorization, then a saved default payment method on a customer-configured Account or Customer before server-side subscription creation. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-subscriptions-bank-transfers]] — Bank transfer subscription: send_invoice+customer_balance required, days_until_due, cash balance auto-pay, Accounts v2 path
- [[source-stripe-subscriptions-bacs-debit]] — Stripe's Bacs Direct Debit subscription guide uses Checkout: a client checkout button calls a server endpoint that creates a subscription-mode Checkout Session with at least one recurring Price. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-subscriptions-amazon-pay]] — The 2026-05-13 Stripe guide describes three Amazon Pay subscription paths: Setup Intents API, Payment Intents API, and a Stripe-hosted Checkout page. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-subscriptions-ach-debit]] — ACH subscription setup: 10-day microdeposit window, default PM webhook step, trial SetupIntent flow, Checkout delayed events, 11 test scenarios
- [[source-stripe-subscriptions-payment-methods-setting]] — Stripe's November 7, 2026 guide explains that subscription `payment_settings.payment_method_types` limits the **types allowed** to pay subscription invoices; it does not select a single saved default payment method. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-billing-collection-method]] — Stripe's Billing collection-method guide describes `charge_automatically` and `send_invoice` for invoices and subscriptions. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-subscriptions-invoices]] — Stripe's subscription-invoice guide covers first invoices, renewals, saved-default payment-method fallback, draft invoice changes, voiding, and metadata propagation. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-billing-ios-sdk]] — BillingSDK for iOS (private preview): Customer Sessions auth, buy buttons, hasEntitlement, getCustomerPortal, vs stripe-ios comparison
- [[source-stripe-subscriptions-prebilling]] — Prebilling uses `billing_schedules` on a subscription to invoice licensed-price items for future service periods when creating or updating the subscription. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-subscriptions-pause]] — The November 7 Stripe guide describes true subscription pause: `POST /v1/subscriptions/:id/pause` suspends service delivery and new invoice generation without canceling the subscription. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-subscriptions-cancel]] — Stripe's [[stripe-subscriptions-cancel]] guide covers manual immediate and period-end cancellation, custom cancel dates, subscription schedules, and configured dispute-triggered cancellation. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-subscriptions-pending-updates]] — Stripe's pending updates normally defer an invoice-generating subscription change until payment succeeds. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-subscriptions-prorations]] — Stripe's same-URL May and November 2026 guides explain proration invoice items for subscription changes, discount treatment, credit calculation in classic versus flexible billing mode, preview, and `proration_behavior`. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-subscriptions-change-price]] — Stripe's Subscriptions API guide describes changing a subscription item's price to upgrade or downgrade an existing subscription. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-subscriptions-modify]] — Modify subscriptions hub: billing-related vs non-billing updates, discount+proration mixed-call behavior, pending updates
- [[source-stripe-billing-entitlements]] — As documented in Stripe's 2026-05-13 Dashboard and API guide, Stripe Entitlements maps internal product features to Stripe Products and tracks customer entitlements through subscriptions. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-products-prices]] — Products & Prices: custom product IDs, price immutability (archive+new), price_data, compatibility table (tiered/usage-based Disallowed in Payment Links), 3yr max interval
- [[source-stripe-payment-records]] — Payment Records API: unified on+off-Stripe ledger, 3-level hierarchy (PaymentRecord→Attempt→Entry), 4 reporting methods, requires Orchestration
- [[source-stripe-payment-methods]] — Payment Methods API: 3 customer action types, immediate (cards) vs delayed (ACH/SEPA) notification, single-use vs reusable, PaymentMethod object structure
- [[source-stripe-checkout-sessions]] — The April and November 2026 Stripe overviews recommend the Checkout Sessions API for most payments integrations. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-payment-intents]] — PaymentIntents and SetupIntents lifecycle, status and cancellation. See the November full lifecycle and asynchronous capture guides and dated API-version conditions.
- [[source-stripe-api-tour]] — Conceptual tour of how Stripe API objects cooperate across payment integrations, including an illustrative PaymentIntent path and the roles of PaymentMethod, Charge, and Event. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-legacy-apis]] — Legacy Charges, Tokens and Sources APIs. The dated sources distinguish migration, ACH onboarding and read-side authentication evidence.
- [[source-stripe-glossary]] — Dated Stripe terminology reference. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-building-with-ai]] — AI developer tools: MCP server, agent skills (npx/Claude Code/Cursor), AI coding platforms, plain text docs, VS Code AI assistant
- [[source-stripe-accept-a-payment]] — Stripe integration choices. The November Accept a Payment base page links variants, and the separate full November Online Payments overview compares the documented UI and API paths.
- [[source-stripe-payment-links]] — Payment Links provide shareable URLs for Stripe-hosted checkout pages. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-build-payments-page]] — Build a payments page: Checkout Page vs Elements comparison, feature matrix, hosting modes, maintenance tradeoffs
- [[source-stripe-checkout-quickstart]] — This entry routes two Stripe Checkout quickstarts: the **Stripe-hosted redirect** guide captured at this canonical URL on 2026-04-20 and 2026-11-07, and a separately captured **embedded page** guide from 2026-04-20. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-checkout-form]] — Checkout form (custom path): single iframe, 100+ methods, built-in returning UI, Appearance API, 2 layouts (single-page + multi-step)
- [[source-stripe-how-checkout-works]] — The April 20, 2026 full guide captured hosted page, embedded page, and Checkout Elements bodies: their Checkout Session lifecycles, 26-row Hosted feature table, mixed carts, saving, expiration, webhooks, and agentic checkout. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-stripe-checkout-appearance]] — The full guide captured on 2026-04-20 describes Dashboard branding defaults and per-Checkout Session `branding_settings` for its Hosted page and Embedded page variants. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-stripe-checkout-card-brands]] — Card brand blocking: brands_blocked param, 4 brands (discover_global_network covers Discover/Diners/JCB/UnionPay/Elo), filters Link/Apple Pay/Google Pay/saved PMs
- [[source-stripe-checkout-product-images]] — Product images: products.create images param, inline price_data.product_data, drives conversion
- [[source-stripe-checkout-shipping]] — Charge for shipping: ShippingRate API, shipping_options, delivery estimates, shipping tax, payment mode only
- [[source-stripe-checkout-taxes]] — Collect taxes: automatic_tax param, new/existing customer flows, Accounts v2 + Customers v1, customer_update, wallet constraints
- [[source-stripe-checkout-manual-tax-rates]] — Manual Tax Rates: TaxRate API, fixed + dynamic rates, 30-country list, wallet constraints, Dashboard reporting exports
- [[source-stripe-checkout-custom-shipping-options]] — Historical April 2026 Embedded Checkout shipping callback and related line-item guide. Stripe.js 9.14.0 deprecates `onShippingDetailsChange`; retain the historical pattern for version-specific maintenance and verify a current replacement before new implementation. (S03 reviewed update, 2026-11-15; dated qualifications apply.)
- [[source-stripe-checkout-custom-components]] — Custom fields (3 types), custom text (4 placements), ToS consent, payment method reuse agreement, localization, Dashboard policies
- [[source-stripe-checkout-build-subscriptions]] — Full subscription integration: product/price setup, Checkout Session, webhook provisioning, customer portal, flexible billing mode
- [[source-stripe-checkout-dashboard-payment-methods]] — Dashboard payment methods: migration guide, Apple Pay/Google Pay defaults, delayed notification PM webhook pattern, test table
- [[source-stripe-adaptive-pricing]] — Adaptive Pricing: 150+ countries, 20 local PMs, presentment_details, 0% merchant / 2–4% customer fee, restrictions, refunds
- [[source-stripe-checkout-discounts]] — Discounts: Coupon API, session apply, promotion codes, restriction params, uniqueness rules, lifecycle
- [[source-stripe-checkout-optional-items]] — Optional items: optional_items API, adjustable_quantity, cross-sells, limitations table
- [[source-stripe-checkout-save-and-reuse]] — Setup mode: session creation, SetupIntent retrieval, off-session charging, 402 handling
- [[source-stripe-checkout-save-during-payment]] — Save during payment: setup_future_usage vs payment_method_save, allow_redisplay, customer_creation, PM removal, GDPR note
- [[source-stripe-checkout-fulfillment]] — Fulfill orders: dual-trigger pattern, fulfill_checkout function, webhook handler, delayed PMs, landing page config
- [[source-stripe-checkout-receipts]] — Receipts + paid invoices: automatic setup, branding, invoice_creation param, invoice_data hash, delayed PM behavior, localization
- [[source-stripe-checkout-custom-success-page]] — Redirect behavior: hosted success page, embedded return page + session status, redirect_on_completion (3 modes), onComplete callback
- [[source-stripe-checkout-abandoned-carts]] — Abandoned cart recovery: consent + after_expiration.recovery, checkout.session.expired, recovery URL, anti-spam, conversion tracking
- [[source-stripe-checkout-conversion-funnel]] — GA4 conversion funnel: gtag instrumentation, begin_checkout event, Measurement Protocol, client ID linking
- [[source-stripe-checkout-embedded-analytics]] — Embedded analytics (private preview): onAnalyticsEvent, 6 event types, client_metadata, failureReason, TypeScript types
- [[source-stripe-elements-advanced-payments]] — Checkout Sessions vs Payment Intents for Elements: feature matrix, IC+ scenarios, integration effort comparison
- [[source-stripe-checkout-elements-quickstart]] — Checkout Elements quickstart: CheckoutElementsProvider, useCheckout hook, 4 elements, return page, Adaptive Pricing, Stripe Tax
- [[source-stripe-payment-intents-quickstart]] — Payment Intents quickstart: Elements wiring, confirmPayment, return page status, Stripe Tax, email receipts, off-session charging
- [[source-stripe-web-elements-overview]] — Stripe Elements overview: 7 elements, Checkout Sessions vs Payment Intents API comparison, features
- [[source-stripe-payment-element]] — Payment Element: layout (3 options), Appearance API, 8 options, element combining, 17 auto-handled error codes
- [[source-stripe-payment-element-best-practices]] — Payment Element best practices: LLM instruction, HTML confirm pattern, 7-item + 5-item checklists
- [[source-stripe-payment-element-vs-card-element]] — Payment Element vs Card Element: 7 comparison tables, Card Element legacy status, migration guide
- [[source-stripe-payment-element-migration]] — Payment Element migration: CardElement → PaymentElement (PI + SI paths), 11 Elements options, elements.submit() pattern
- [[source-stripe-payment-element-migration-ewcs]] — Payment Element migration to Checkout Sessions (recommended): one-time + future paths, 12 session options, actions.confirm()
- [[source-stripe-express-checkout-element]] — The Express Checkout Element presents one-click buttons for six built-in methods: Link, Apple Pay, Google Pay, PayPal, Klarna, and Amazon Pay. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-express-checkout-element-accept-payment]] — The 2026-04-21 capture is a combined Express Checkout Element integration guide for Checkout Sessions API and Payment Intents API. (S02 reviewed update, 2026-11-09; dated source qualifications apply.) The November capture supplies variant navigation; functional details remain attributed to earlier full captures.
- [[source-stripe-express-checkout-element-migration]] — The guide captured on 2026-04-21 describes migration from the **Payment Request Button Element** (PRB) to the **Express Checkout Element** (ECE) using the Payment Intents API. (S02 reviewed update, 2026-11-09; dated source qualifications apply.) The November capture supplies variant navigation; functional details remain attributed to earlier full captures.
- [[source-stripe-address-element]] — Address Element: shipping/billing modes, PaymentIntent field routing, autocomplete (26 countries), Link autofill, combining with other elements
- [[source-stripe-currency-selector-element]] — The Currency Selector Element is an embeddable UI toggle for presenting Adaptive Pricing currency options to customers. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-link-authentication-element]] — Link Authentication Element: dual-purpose email + Link auth, onChange event, defaultValues prefill, combining with other elements
- [[source-stripe-payment-method-messaging-element]] — The Payment Method Messaging Element is a web Stripe UI component that displays localized information about available buy now, pay later (BNPL) plans on product, cart, and payment pages. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-tax-id-element]] — The Tax ID Element is an embeddable UI component for collecting customer business tax IDs for tax calculation and invoice display. (S02 reviewed update, 2026-11-09; dated source qualifications apply.) The November capture supplies variant navigation; functional details remain attributed to earlier full captures.
- [[source-stripe-checkout-sessions-vs-payment-intents]] — Checkout Sessions vs Payment Intents: 11-row feature matrix, session expiration, webhook lifecycle, Adaptive Pricing exclusivity
- [[source-stripe-payment-element-design-integration]] — Payment Element design. Compare the dated choices for creating intents and confirming on the client or server.
- [[source-stripe-payment-element-custom-payment-methods]] — Web Payment Element custom payment methods. See dated creation, confirmation, reporting and platform qualifications.
- [[source-stripe-payment-element-customize-payment-methods]] — Stripe's November 7, 2026 Payment Element guide covers **four** display controls: enabled methods, ordering, card brand/funding filters, and accordion count. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-migrate-payment-methods-dashboard]] — The April 21, 2026 capture contains separate Checkout Sessions (embedded-components) and Payment Intents (Elements) migration guides under this URL. (S02 reviewed update, 2026-11-09; dated source qualifications apply.) The November capture supplies variant navigation; functional details remain attributed to earlier full captures.
- [[source-stripe-collect-addresses]] — Collect addresses: Checkout Sessions vs Payment Intents API diff, syncAddressCheckbox, getValue(), blockPoBox, autocomplete with own Maps key + CSP
- [[source-stripe-payment-element-billing-details]] — Control billing details: auto/never/if_required modes, never requires manual injection at confirm, if_required trade-offs (network fees, auth rate)
- [[source-stripe-charge-shipping]] — The 2026-04-21 guide covers two distinct API paths. (S02 reviewed update, 2026-11-09; dated source qualifications apply.) The November capture supplies variant navigation; functional details remain attributed to earlier full captures.
- [[source-stripe-build-subscriptions-elements]] — The 2026-04-21 capture at this URL contains **two distinct web subscription integrations** using Elements: Checkout Sessions API with embedded components and a lower-level Payment Intents API route. (S02 reviewed update, 2026-11-09; dated source qualifications apply.) The November capture supplies variant navigation; functional details remain attributed to earlier full captures.
- [[source-stripe-checkout-dynamic-shipping]] — The April 21, 2026 full guide documents a beta Checkout Sessions `ui_mode: 'elements'` path for address-based server updates to shipping details and options. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-stripe-checkout-dynamic-line-items]] — The 2026-04-21 full guide demonstrates a subscription interval toggle in Checkout Sessions with `ui_mode: "elements"`: the client requests a server update, the server changes the Session's line items, and `runServerUpdate` refreshes the client Session. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-stripe-checkout-dynamic-trials]] — Dynamic trial durations (private preview): trial_period_days/trial_end mutual exclusion, removal rules, subscription mode only
- [[source-stripe-checkout-dynamic-discounts]] — Dynamic discounts (private preview): permissions.update_discounts=server_only, inline coupon_data, remove via [], loyalty/cart/promo use cases
- [[source-stripe-checkout-dynamic-amounts]] — The April 21, 2026 full guide describes two dated paths for changing totals while a customer changes selections: Checkout Sessions with client `runServerUpdate` and server `line_items`/`price_data`, and PaymentIntents with server `paymentIntents.update({ amount })` followed by client refresh. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-stripe-checkout-adjustable-quantities]] — The full 2026-04-21 guide describes quantity adjustment for Checkout Session line items. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-stripe-checkout-update-customer]] — April/November 2026 guide to attaching a Customer to an existing Checkout Session during checkout. The November guide marks preview access; an access request or registration does not establish entitlement. (S03 reviewed update, 2026-11-15; dated qualifications apply.)
- [[source-stripe-checkout-add-discounts]] — The 2026-04-21 and 2026-11-07 captures document coupons and customer-facing promotion codes for discounts in Checkout Sessions with the Elements UI. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-checkout-collect-taxes]] — The April 21, 2026 full guide covers custom Elements tax collection through Checkout Sessions and Payment Intents. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-stripe-checkout-redeem-credits]] — Access-gated Checkout Session credits overview for applying store credit or prepaid gift card amounts. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-checkout-local-currency]] — Local currency hub: Adaptive Pricing vs FX Quotes API vs Manual currency prices (FX Quotes and Manual not yet ingested)
- [[source-stripe-adaptive-pricing-elements]] — Stripe's April and November 2026 guides describe Adaptive Pricing for Checkout Sessions with Elements: Stripe chooses a relevant presentment currency, calculates a localized price, and handles conversion. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-fx-quotes-api]] — Stripe offers the FX Quotes API as a **preview** service to retrieve live exchange-rate information or extended rate quotes for currency pairs. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-manual-currency-prices]] — Manual multi-currency pricing lets merchants set exact amounts for additional currencies with `Price.currency_options` and pass that Price to a Checkout Session. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-payment-element-saved-pms]] — Saved PMs: allow_redisplay values, CVC re-collection, subscription removal warning, unspecified legacy PMs, consent override
- [[source-stripe-save-during-payment-elements]] — Save during payment: both API paths, CustomerSession setup for PI, setup_future_usage vs payment_method_save_usage, Bancontact→SEPA conversion
- [[source-stripe-save-and-reuse-elements]] — Save without payment: CS mode=setup + Setup Intents, confirmSetup, retrieveSetupIntent, Apple Pay MPANs, Radar note, Link prefill
- [[source-stripe-email-receipts]] — Email receipts: CS (invoice_creation, invoice_data) vs PI (receipt_email additional, no invoices, no browser locale), Charge update rule
- [[source-stripe-checkout-manual-approval]] — Manual approval (CS only): server-side fraud/inventory/PM checks before finalizing, compatible with dynamic line items
- [[source-stripe-auth-and-capture]] — Auth+capture: validity windows (Visa MIT=5d, Japan JPY=30d), per-PM windows, per-PM capture_method, automatic_delayed preview, partial capture
- [[source-stripe-checkout-elements-beta-changelog]] — Dated migration history for the Elements with Checkout Sessions API beta, covering `custom_checkout_beta_*` through Basil and Clover. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-inapp-payments-overview]] — In-app payments. See the dated UI paths, payment outcome handling and Android-only NFC tap-to-add scope.
- [[source-stripe-inapp-payment-sheet]] — Payment Sheet. Dated documentation and November 2026 changes.
- [[source-stripe-inapp-custom-payment-methods]] — Mobile custom payment methods. See dated platform-specific handlers and reporting. The FlowController cancellation example applies to Android.
- [[source-stripe-inapp-appearance-api]] — Mobile Appearance API: fonts/colors/shapes/primary button across iOS/Android/RN, dark mode patterns, font name conventions (7 images)
- [[source-stripe-inapp-finalize-payments-server]] — Server finalization for in-app payments. Compare the dated ConfirmationToken flow, wallet configuration and CustomerSession setup across platforms.
- [[source-stripe-inapp-save-during-payment]] — Saving during a mobile payment. See the dated supported-method scope, applicable consent and redisplay requirements, and off-session reuse.
- [[source-stripe-inapp-set-up-future-payments]] — Mobile setup (no initial charge): SetupIntent supports card/Bancontact/iDEAL/Link/SEPA/Sofort/US bank, setupIntentClientSecret, FlowController
- [[source-stripe-inapp-filter-card-brands]] — PaymentSheet card-brand filters. See dated platform wallet, client filtering and server confirmation scope.
- [[source-stripe-inapp-payment-element]] — Mobile Payment Element: embeds in app screen (vs Payment Sheet full-screen), radio/checkmark/floating layouts, inline wallets
- [[source-stripe-inapp-accept-payment-embedded]] — Embedded Payment Element mobile integration. See dated platform flows, saving and redisplay, and the separate per-method configuration preview.
- [[source-stripe-inapp-embedded-appearance-api]] — Embedded Appearance API: selectedBorderWidth, 4 row styles, flatWithDisclosure requires immediateAction, per-style separators/colors
- [[source-stripe-inapp-embedded-custom-payment-methods]] — Custom payment methods in Embedded Payment Element. See the dated platform handlers, result reporting and example differences.
- [[source-stripe-inapp-embedded-filter-card-brands]] — Mobile Embedded Payment Element card-brand filters. See the April guide, retained iOS 26.11.0 type aliases and wallet behavior by platform.
- [[source-stripe-inapp-address-element]] — Mobile Address Element. See the April platform-specific PaymentSheet, Payment Element and Link pairings and the November platform selector.
- [[source-stripe-inapp-collect-addresses]] — Mobile Address Element integration. The guide compares platform-specific collection, requirements, address prefill and payment handoff.
- [[source-stripe-inapp-payment-method-messaging-element]] — Mobile payment-method messaging. Compare April iOS and Android guidance, November platform navigation and separately dated React Native preview scope.
- [[source-stripe-inapp-display-bnpl-messaging]] — Display BNPL Messaging — Mobile Integration Guide. November 2026 variant navigation and earlier detailed guidance.
- [[source-stripe-inapp-ios-android-purchases]] — Stripe's April 22, 2026 mobile digital-goods overview is a short **US-scoped navigation page**. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-inapp-digital-goods-checkout]] — Stripe's 2026-11-07 capture describes a US iOS digital-goods and subscription app-to-web Checkout path: model credits with Products and Prices, use a customer-configured Account (Accounts v2) or Customer (Customers v1), open Checkout in Safari, return through a Universal Link, and update server-owned entitlements from payment events. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-inapp-digital-goods-payment-links]] — The April and November 2026 captures describe an iOS digital-goods and subscription path that opens a **Stripe-hosted Payment Link page in Safari** and returns to the app through a universal link. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-inapp-digital-goods-custom-checkout]] — The April and November 2026 captures describe an **iOS app-to-web subscription checkout**: the app opens the merchant's own Elements/Payment Element checkout page in Safari, then uses a universal link to return to the app. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-inapp-digital-goods-customer-portal]] — Guide for **managing** iOS digital-goods subscriptions through a Stripe-hosted customer portal opened from the app in Safari. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-inapp-customer-sheet]] — CustomerSheet (Payment Method Settings Sheet): app settings PM management, CustomerSession+SetupIntent endpoints, iOS UIKit/SwiftUI/Android/RN, ACH optional
- [[source-stripe-inapp-migrate-confirmation-tokens]] — Mobile ConfirmationToken migration. See the April examples for conditional context and optional saved-card CVC and the November platform selector.
- [[source-stripe-inapp-without-card-auth]] — Basic mobile card acceptance. See the dated geographic scope and the distinction between an authentication-required error and an integration that handles customer actions.
- [[source-stripe-inapp-save-card-without-auth]] — Basic mobile card saving. The dated guide distinguishes Customer attachment, future use and later on-session or off-session confirmation.
- [[source-stripe-inapp-upgrade-to-handle-actions]] — Basic mobile card integration upgrade. The dated guide explains manual confirmation, required customer action, reconfirmation and a conflicting historical sandbox row.
- [[source-stripe-managed-payments-overview]] — Stripe Managed Payments as merchant of record. See the dated merchant eligibility, tax coverage and hosted, embedded and mobile Checkout scope.
- [[source-stripe-managed-payments-eligibility]] — Managed Payments eligibility. The November capture lists 37 merchant locations and describes conditional Stripe refund authority within 60 days.
- [[source-stripe-managed-payments-tax-compliance]] — Managed Payments tax coverage and exceptions. See seller and buyer scope and the no-additional-fee rule for automatic Stripe Tax calculation on these transactions.
- [[source-stripe-managed-payments-how-it-works]] — How Managed Payments Works. Dated documentation and November 2026 changes.
- [[source-stripe-managed-payments-changelog]] — Managed Payments release history. See the dated Pay Invoice rollout, future-usage support, eligibility counts and new-subscription migration scope.
- [[source-stripe-managed-payments-setup]] — Managed Payments Checkout setup. See the dated product eligibility, consent, tax behavior and webhook requirements.
- [[source-stripe-managed-payments-update-checkout]] — Update a Checkout Integration to Use Managed Payments. Dated documentation and November 2026 changes.
- [[source-stripe-managed-payments-mobile]] — Managed Payments for digital goods in mobile apps. See the dated storefront, hosted Checkout, and external purchase flow guidance.
- [[source-stripe-managed-payments-payment-links]] — Use Payment Links with Managed Payments. Dated documentation and November 2026 changes.
- [[source-stripe-recurring-payments-overview]] — Recurring payments overview: 3 types, 6-product comparison, subscription creation patterns, flexible billing_mode, Accounts v2 customer_account
- [[source-stripe-terminal-overview]] — Terminal: in-person card readers, 5 integration paths (custom POS/Tap to Pay/apps on readers/third-party POS/gateway), 4 SDKs, offline payments, Connect-compatible
- [[source-stripe-terminal-collect-tips]] — Terminal tipping: on-reader (reader-prompted, wide country support) vs on-receipt (US only, tip added at capture); mandatory tips in original amount
- [[source-stripe-terminal-on-receipt-tipping]] — On-receipt tipping detail: overcapture flow, 50%/50 USD limit, eligible MCCs, fallback via incremental auth or generated_card
- [[source-stripe-terminal-on-reader-tipping]] — On-reader tipping detail: Configuration API (smart/pct/fixed), tip lifecycle, skip tipping, tip-eligible amounts, 38-country list
- [[source-stripe-terminal-save-payment-details]] — Save payment details: generated_card for online reuse, off-session charging, card fingerprints, compliance requirements
- [[source-stripe-terminal-save-directly]] — Save directly (SetupIntent): CNP caveat, card network support, allow_redisplay consent, SDK compatibility, mobile wallet caveats
- [[source-stripe-terminal-save-after-payment]] — Save after payment (PaymentIntent): setup_future_usage, allow_redisplay at collect, generated_card retrieval, fallback when absent
- [[source-stripe-terminal-incremental-authorizations]] — Incremental authorizations: Visa/MC/Amex (all MCCs), Discover (restricted), max 10 attempts, setup, API, auto-increment at capture
- [[source-stripe-terminal-extended-authorizations]] — Extended authorizations: capture up to 30 days later, card/MCC eligibility, capture_before field, Amex caveat
- [[source-stripe-terminal-refunds]] — Refunds and cancellations: cancel pre-capture, online vs in-person refunds, Interac mandatory in-person
- [[source-stripe-terminal-receipts]] — Receipts: prebuilt email receipts via receipt_email, custom receipts with required EMV fields, cardholder preferred_locales
- [[source-stripe-terminal-display-cart]] — Display cart details: setReaderDisplay API, display-only amounts, pre-dip (US only)
- [[source-stripe-terminal-collect-inputs]] — Collect on-screen inputs: 6 input types, up to 5 per call, customization, webhooks, 7-day signature storage
- [[source-stripe-terminal-collect-data]] — Collect swiped data (private preview): magstripe non-PCI data, gift cards, token + server-side retrieval, 24h storage
- [[source-stripe-terminal-collect-nfc-data]] — Collect NFC tapped data (private preview): NFC UID from non-payment instruments, offline-capable, S700/S710/M2 only
- [[source-stripe-terminal-apps-on-devices]] — Apps on Devices: deploy Android POS on smart readers, two integration modes, AOSP differences, permissions allowlist
- [[source-stripe-terminal-apps-on-devices-build]] — Apps on Devices build/test: DevKit setup, SDK deps, serverless init, discovery, transition animations, adb testing
- [[source-stripe-terminal-apps-on-devices-app-review]] — Apps on Devices app review: automated vs manual, 2-5 day timeline, guidelines (no keyed input, sandbox, self-contained instructions)
- [[source-stripe-terminal-apps-on-devices-submit]] — Apps on Devices submit: Dashboard upload flow, compatible device types, status via email/Dashboard/webhook
- [[source-stripe-terminal-apps-on-devices-deploy-dashboard]] — Apps on Devices deploy: deploy groups, three entry points, progressive rollout, Alpha/Beta/General best practice
- [[source-stripe-terminal-apps-on-devices-deploy-api]] — Apps on Devices deploy via API (private preview): deploy groups + locations, same behavior as Dashboard
- [[source-stripe-terminal-apps-on-devices-monitor]] — Apps on Devices monitor: Dashboard deployment status per release version (Pending/Served/Installed/Failed)
- [[source-stripe-terminal-apps-on-devices-troubleshooting]] — Apps on Devices troubleshooting: upload timeout, sandbox/live resubmit, admin settings, IPC limit, crash loops
- [[source-stripe-terminal-order-and-return-readers]] — Hardware orders: ordering, statuses, self-service returns (33 countries), shipping table, permissions, Hardware Orders API
- [[source-stripe-terminal-warranty-claims]] — Warranty claims: 1-year coverage on readers, Dashboard flow, 48h review, replacement warranty carryover
- [[source-stripe-terminal-register-readers]] — Register readers: 3 smart reader methods (pairing code/serial/order), mobile reader locationId at connect time
- [[source-stripe-terminal-locations-and-zones]] — Locations and zones: address requirements by country, zone hierarchy, connection token scoping, Connect patterns
- [[source-stripe-terminal-configurations]] — Terminal configurations: account→location hierarchy, 10-min propagation, API CRUD, zone config preview
- [[source-stripe-terminal-admin-menu-passcode]] — Admin menu passcode: default 07139, 5-digit, same hierarchy, permission tiers for view/modify
- [[source-stripe-terminal-splash-screen]] — Splash screen: per-reader-type, resolutions, image limits, WisePad 3 PNG/B&W, Files API upload + Configuration object
- [[source-stripe-terminal-offline-mode-config]] — Offline mode config: enable/disable via Configuration object `offline.enabled`, 10-min propagation
- [[source-stripe-terminal-reboot-time]] — Reboot time window: default midnight, custom `reboot_window` per location timezone, staggered reboots, midnight-crossing logic
- [[source-stripe-terminal-tipping-config]] — On-reader tips (fleet): 3 tip types, `tipping.{currency}` Configuration API field, smart_tip_threshold, 10-min propagation
- [[source-stripe-terminal-wifi-config]] — WiFi network config: remote push to smart readers, 3 security types (PSK/EAP-PEAP/EAP-TLS), no validation, EAP-TLS via Files API
- [[source-stripe-terminal-cellular-config]] — Cellular config: S710 only, WiFi fallback, monthly billing if enabled, `cellular.enabled` on Configuration object
- [[source-stripe-terminal-monitor-readers]] — Monitor readers: Dashboard readers list, smart reader health/connectivity details, 30-day event log (public preview)
- [[source-stripe-terminal-js-sdk-reference]] — JS SDK API reference: 29 methods, 17 error codes, changelog (surcharge consent, print preview, cancelable operations)
- [[source-stripe-terminal-mobile-readers]] — Mobile readers overview: M2/Chipper 2X BT (US), WisePad 3 (25 non-US countries), BLE/USB, auto-updates, 24h reboot
- [[source-stripe-terminal-bbpos-wisepad3]] — WisePad 3 firmware reference: software version format, latest 4.01.03.00, config regions, key identifiers (APAC/EU/NA)
- [[source-stripe-terminal-stripe-m2]] — M2 firmware reference: latest 2.01.01.00, power button 4s/14s, NFC UID added 2.01.00.31, LED status tables
- [[source-stripe-terminal-smart-readers]] — Smart readers overview: availability table (S700/S710/WisePOS E/Verifone), internet-connected, midnight PCI restart
- [[source-stripe-terminal-s700-s710]] — S700/S710 firmware reference: 4-component software, latest 2.41.2.0/1.00.03.00, diagnostics, payment sounds, changelog
- [[source-stripe-terminal-bbpos-wisepos-e]] — WisePOS E firmware reference: 4-component, latest 2.41.2.0/5.01.03.00, tap sounds same for success+failure, Ethernet dock rule
- [[source-stripe-terminal-tap-to-pay-readers]] — Tap to Pay overview: iPhone 38 countries (JP not GI), Android 38 countries (GI not JP), MPoC compliance status
- [[source-stripe-terminal-sdk-migration-guide]] — SDK v5 migration: unified process methods, customer cancel default, easyConnect, iOS 15 min, Handoff→AppsOnDevices rename
- [[source-stripe-terminal-sdk-v4-migration-guide]] — SDK v4 migration: consolidated connectReader, auto-reconnect default, allow_redisplay global, iOS 14 min, LocalMobile→TapToPay
- [[source-stripe-terminal-sdk-v3-migration-guide]] — SDK v3 migration: processPayment→confirmPaymentIntent, readReusableCard removed, per-type DiscoveryConfig, iOS 13/Android 26 min
- [[source-stripe-terminal-deployment-checklist]] — Deployment checklist: 10 items (ConnectionToken, capture, receipts, reconcile, Chipper updates, registration, Locations, reader UI, SDK, passcode)
- [[source-stripe-terminal-reader-product-sheets]] — Reader product sheets index: S700/S710/M2/BBPOS/Verifone PDF specs and operating info
- [[source-stripe-payment-methods-overview]] — All Stripe payment methods: 8 categories (cards/bank debits/redirects/transfers/BNPL/real-time/vouchers/wallets), regional tables
- [[source-stripe-payment-method-integration-options]] — Integration options: 5 paths (Payment Links→Advanced), dynamic vs manual, wallet domain registration
- [[source-stripe-automatic-payment-methods]] — Aug 2023 API change: dynamic payment methods as default, allow_redirects option, 3 server-side confirmation paths
- [[source-stripe-cards]] — Stripe's cards guide covers bank-linked debit and credit cards entered at online checkout, brand capability by Stripe account country and customer country, possible additional authentication, and regional card rules. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-cit-mit]] — CIT/MIT: definitions, MIT compliance requirements, card brand change blocks MIT, Card Account Updater event
- [[source-stripe-how-cards-work]] — Stripe explains an online card payment as **format check → possible customer authentication → bank authorization hold → capture**. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-card-product-codes]] — Card product codes: brand_product field, Visa 41 + Mastercard 200+ codes, test card PMs
- [[source-stripe-cartes-bancaires]] — Stripe's **2026-05-01 full capture** describes Cartes Bancaires (CB), France's local card network. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-stripe-mastercard-tlid]] — Mastercard TLID: 2026 requirement (Jun 2 retain, Oct 23 send with MIT), 22-char identifier, Stripe auto-handles
- [[source-stripe-eftpos-australia]] — eftpos is Australia's local debit card network. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-co-badged-cards-compliance]] — The 2026-05-01 Stripe guide explains cardholder network choice for co-badged cards, including regional applicability, Stripe integration variants, Connect merchant-of-record conditions, and test examples. (S02 reviewed update, 2026-11-09; dated source qualifications apply.) The November capture supplies variant navigation; functional details remain attributed to earlier full captures.
- [[source-stripe-installments]] — Installments index: Mastercard Installments (4×), Mexico meses sin intereses, Japan 分割払い
- [[source-stripe-jp-installments]] — Stripe's May 1 and November 7, 2026 captures describe Japanese credit-card installments (分割払い): the customer splits a purchase over billing statements while the card issuer extends credit and collects installments. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-jp-installments-accept-payment]] — The full guide captured **2026-05-01** describes Japan installment card payments through Checkout, Payment Element, Direct Payment Intents API, Invoices, and Payment Links, with sandbox card examples. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-stripe-mastercard-installments]] — Mastercard Installments. Compare separately dated customer and Stripe-account locations, prohibited business categories and availability for recurring payments.
- [[source-stripe-mx-installments]] — Mexico meses sin intereses. Compare dated consumer card eligibility, available installment terms and issuer lists.
- [[source-stripe-mx-installments-accept-payment]] — Accept Meses Sin Intereses Card Payments. November 2026 variant navigation and earlier detailed guidance.
- [[source-stripe-balance-pay]] — Pay with Stripe Balance: Connect subscriptions only, Accounts V2 preview, T+0/T+1 settlement, insufficient_funds handling, consent required
- [[source-stripe-stablecoin-payments]] — Stablecoin payments: USDC/USDP/USDG, US businesses only, settles in USD, no chargebacks, refunds in stablecoins
- [[source-stripe-accept-stablecoin-payments]] — The May 1, 2026 capture is a detailed, bundled guide for enabling Pay with Crypto and integrating through **six variant routes**: Checkout, Elements with Checkout Sessions API, Elements with Payment Intents API, Direct API, iOS, and Android. (S02 reviewed update, 2026-11-09; dated source qualifications apply.) The November capture supplies variant navigation; functional details remain attributed to earlier full captures.
- [[source-stripe-crypto-deposit-mode]] — Crypto deposit mode: API-only, USDC Tempo/Base/Solana, exact amount, auto-capture, access required
- [[source-stripe-bank-debits]] — Stripe describes bank debits as mandate-authorized pulls from a customer's bank account for one-time or recurring purchases. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-ach-direct-debit]] — ACH Direct Debit is a reusable, delayed-notification, nonguaranteed debit from a customer's US bank account, presented in USD. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-ach-accept-payment]] — The guide captured 2026-05-02 at this URL covers ACH Direct Debit through Checkout, Elements with the Checkout Sessions API, Elements with the Payment Intents API, Direct API, iOS, Android, React Native, and Webview. (S02 reviewed update, 2026-11-09; dated source qualifications apply.) The November capture supplies variant navigation; functional details remain attributed to earlier full captures.
- [[source-stripe-ach-set-up-payment]] — The 2026-11-07 base-URL capture is a variant index for Checkout, Elements, iOS, Android, and React Native. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-ach-migration]] — Stripe's 2026-05-02 and 2026-11-07 captures say merchants creating legacy ACH Direct Debit payments must migrate to the Payment Intents API or Checkout Sessions API. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-ach-migrate-bank-accounts]] — The 2026-05-02 guide at this canonical URL explains how to reuse existing ACH `BankAccount` objects collected through Stripe's Tokens API with Checkout Sessions or the Payment Intents API. (S02 reviewed update, 2026-11-09; dated source qualifications apply.) The November capture supplies variant navigation; functional details remain attributed to earlier full captures.
- [[source-stripe-ach-migrate-from-processor]] — ACH migrate from another processor: Stripe-managed vs self-service, verification skip, raw bank details SetupIntent
- [[source-stripe-twint]] — TWINT: Switzerland mobile payment, CHF/5000 CHF max, mobile redirect + QR code flows, disputes, refunds, onboarding requirements, Connect
- [[source-stripe-twint-accept-payment]] — TWINT integration: Checkout + Direct API (confirmTwintPayment), redirect flow, save-during-payment
- [[source-stripe-twint-save-during-payment]] — TWINT save during payment: setup_future_usage, off-session charging, return_url not required for saved method
- [[source-stripe-twint-set-up-future-payments]] — TWINT setup-only (no payment): SetupIntent via Checkout/Elements/Direct API, confirmTwintSetup, mandate_data
- [[source-stripe-wero]] — Wero: Germany/EUR, QR+app auth, under 10s, no disputes/recurring, 2-year refunds, 30 business countries
- [[source-stripe-wero-accept-payment]] — Wero integration: Checkout + Elements + Direct API (confirmWeroPayment), server-side manual path, 1-hour auth expiry, error codes
- [[source-stripe-usage-based-billing-how-it-works]] — This guide explains **basic usage-based billing with Stripe Billing Meters**: its four-part lifecycle and six core objects. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-usage-based-billing-use-cases]] — Usage-based pricing models: pay-as-you-go, flat fee+overages (v1 only), credit-based
- [[source-stripe-usage-based-billing-payg]] — Dated basic Billing Meters pay-as-you-go workflow. The November guide recommends Metronome for new usage-based integrations, while existing Billing Meters integrations need not migrate; it does not establish account access. (S02 reviewed update, 2026-11-09.)
- [[source-stripe-usage-based-billing-flat-fee-overages]] — End-to-end Hypernian example for a flat fee plus overages: a sum meter, graduated metered price with the first 1,000 units included, separate $100 monthly licensed price, and both prices on one subscription. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-usage-based-billing-credits]] — Dated basic Billing Meters and Credit Grants pricing guide, with invoice-time credit application and scoped Account/Customer examples. November recommends Metronome for new integrations without deprecating existing Billing Meters or proving account access. (S02 reviewed update, 2026-11-09.)
- [[source-stripe-usage-based-billing-recording-usage]] — Stripe's dated recording-usage hub for basic [[stripe-usage-based-billing|Billing Meters]] explains how existing Billing Meters users record customer usage and routes to the API, Dashboard CSV, and Amazon S3 guides. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-usage-based-billing-meters-configure]] — Meter config attributes, Raw vs Pre-aggregated ingestion, immutability, Meter Event Adjustment API
- [[source-stripe-usage-based-billing-recording-usage-api]] — Stripe's May 5 and November 7, 2026 captures of this API guide explain recording usage for [[stripe]] Billing Meters. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-usage-based-billing-recording-usage-dashboard]] — Dashboard ingestion: manual input + CSV upload (5 MB limit, field schema, error file workflow)
- [[source-stripe-usage-based-billing-recording-usage-s3]] — Stripe's May 5 and November 7, 2026 captures of the same guide describe bulk meter-event ingestion from Amazon S3 through a Stripe Dashboard connector. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-usage-based-billing-configure-grace-period]] — The May 5 and November 7, 2026 same-URL guides describe a configurable invoice **finalization** grace period. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-usage-based-billing-credits-overview]] — Stripe describes Credit Grants for prepaid or promotional billing credits allocated to a customer for usage-based merchant offerings. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-usage-based-billing-credits-setup]] — Billing credits setup: create grant, price-level scoping via billable_items, funding flow
- [[source-stripe-usage-based-billing-monitor-usage-alerts]] — UBB monitoring: usage alerts vs billing thresholds, limits and constraints
- [[source-stripe-usage-based-billing-alerts-setup]] — The November 7, 2026 guide describes **usage alerts** that notify an application when meter usage reaches a configured threshold. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-usage-based-billing-thresholds-setup]] — Billing thresholds: monetary + usage APIs, reset_billing_cycle_anchor, volume tiers negative line item edge case
- [[source-stripe-usage-based-billing-manage-setup]] — UBB management: transform_quantity, mid-cycle price updates, backdated subscriptions, cancellation
- [[source-stripe-bank-transfers]] — Stripe's bank transfer overview describes a push-payment method. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-bank-transfers-accept-payment]] — Stripe's November 7, 2026 capture of this URL is a variant index. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-stripe-customer-balance]] — Stripe distinguishes a customer's cash balance, a per-currency reconciliation layer for bank transfers, from an invoice balance, a liability offset for future invoices. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-customer-balance-reconciliation]] — Stripe documents how incoming bank transfer funds in a customer's cash balance are applied to incomplete PaymentIntents and open invoices. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-customer-balance-funding-instructions]] — This guide shows how to give a customer bank-transfer funding details before their first payment **without creating a PaymentIntent**. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-bank-transfers-vban]] — VBAN permanence, allocation triggers, best practices, per-region daily/lifetime limits
- [[source-stripe-bank-transfers-refunds]] — The November 7, 2026 full guide and the older capture describe three destinations or origins: refund a bank-transfer payment to the customer's bank, refund that payment to the customer's **cash balance**, or return available customer cash balance to the customer's bank. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-fr-meal-vouchers]] — France Titres-Restaurant (Meal Vouchers). Dated documentation and November 2026 changes.
- [[source-stripe-fr-meal-vouchers-accept-payment]] — French meal voucher acceptance. Compare May SIRET handling with November preview PaymentLocations, confirmation and benefit details.
- [[source-stripe-fr-meal-vouchers-connect]] — Connect for French meal vouchers. See the dated location and SIRET onboarding requirements, confirmation-time identification and fee routing.
- [[source-stripe-fr-meal-vouchers-check-balance]] — Check French Meal Vouchers Balances. Dated documentation and November 2026 changes.
- [[source-stripe-fr-meal-vouchers-save-payment]] — Save a French Meal Voucher Payment Method. Dated documentation and November 2026 changes.
- [[source-stripe-fr-meal-vouchers-setup-restaurant]] — French meal voucher SIRET setup. Compare dated Dashboard and Connect paths, location checks and the Dashboard immutability scope.
- [[source-stripe-bnpl-overview]] — November 2026 BNPL overview: eleven product rows versus ten API rows, method-specific support and dated conflicts. Its immediate/full merchant-payment wording does not establish bank payout; the Klarna overview instead specifies acceptance credit minus fees and standard payout timing. See [[source-stripe-klarna]]. (S03 reviewed update, 2026-11-15; dated qualifications apply.)
- [[source-stripe-affirm]] — Stripe describes Affirm as a single-use, domestic B2C buy now, pay later method. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-affirm-accept-payment]] — The detailed guide captured on May 6, 2026 describes four Affirm web/API integration variants: Checkout (hosted or embedded), Checkout Sessions API with Elements, Payment Intents API with Elements, and Direct API. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-stripe-affirm-messaging]] — Legacy affirmMessage Element (deprecated); Payment Method Messaging Element is recommended
- [[source-stripe-afterpay-clearpay]] — Afterpay (Clearpay in the UK) is a single-use buy now, pay later method. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-afterpay-clearpay-accept-payment]] — Stripe's Afterpay/Clearpay acceptance guide. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-stripe-afterpay-clearpay-messaging]] — Legacy afterpayClearpayMessage Element (deprecated); auto-localizes Clearpay for UK
- [[source-stripe-alma]] — Stripe's Alma overview describes a single-use buy now, pay later method for eligible European B2C purchases. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-alma-accept-payment]] — The 2026-11-07 capture of Stripe's Alma acceptance guide is a variant index. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-stripe-billie]] — Billie is a **B2B, single-use, Pay in 30** buy now, pay later method. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-billie-accept-payment]] — The May 6, 2026 full guide describes integrating Billie's single-use, business Pay by Invoice method across hosted Checkout, Checkout Sessions with Elements, Payment Intents with Elements, Direct API, iOS, and Android. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-stripe-klarna]] — Stripe's Klarna payment-method overview covers customer payment options, geographic and amount conditions, cross-border presentment, refunds, Connect, and country filtering. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-klarna-accept-payment]] — May 6, 2026 Klarna acceptance guide for Stripe, with Checkout, Elements, Direct API, iOS, Android, and React Native variants. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-stripe-klarna-set-up-future-payments]] — The 2026-05-06 full Stripe guide describes saving a Klarna PaymentMethod for later subscription renewals or on-demand purchases. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-stripe-klarna-best-practices]] — Stripe's May and November 2026 Klarna best-practices guides recommend early Express Checkout Element placement, product-page Payment Method Messaging, relevant cart line items, and optional shipping and billing data. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-klarna-compliance]] — This Stripe page records Klarna network eligibility, marketing, termination and merchant duties. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-klarna-disputes]] — Stripe guide to Klarna payment disputes: a customer files a complaint or return request in the Klarna app; most cases pass through an inquiry before a chargeback, while some reach chargeback directly. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-klarna-supplementary-data]] — The May 6 and November 7, 2026 captures describe the same Klarna-only public preview for sending industry-specific supplementary purchase data on a PaymentIntent. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-kriya]] — Kriya B2B BNPL for the UK and GBP. The November method page lists Connect support and an early-access request. See the dated payout, dispute and refund terms.
- [[source-stripe-kriya-accept-payment]] — Kriya acceptance. The May guide describes redirects and seven-day manual capture. The November selector lists separate Checkout, Elements and Direct API routes.
- [[source-stripe-mondu]] — Mondu B2B BNPL. Compare dated business and currency coverage, the November Connect label and waitlist, and the dispute filing and evidence terms.
- [[source-stripe-mondu-accept-payment]] — Mondu acceptance. See the dated May checkout, redirect and manual-capture rules and November implementation routes.
- [[source-stripe-payment-on-invoice]] — Payment on invoice: consumer BNPL DE/AT, 14-day terms, risk-based, branded invoice, T+2
- [[source-stripe-scalapay]] — Scalapay: consumer BNPL, EUR-only all countries, 90-day refunds, no Connect, approval-based categories
- [[source-stripe-scalapay-accept-payment]] — Scalapay integration: return_url required, 7-day capture, Checkout limited to 8 EU countries
- [[source-stripe-sequra]] — SeQura: consumer BNPL Spain-only, Pay in 3/12, most extensive prohibited list (~160+ categories)
- [[source-stripe-sequra-accept-payment]] — SeQura integration: 7-120 day terms, return_url required, 7-day manual capture
- [[source-stripe-sunbit]] — Sunbit: US-only, 3/6/12/18-month installments, Connect supported, no manual capture, $60-$20k
- [[source-stripe-sunbit-accept-payment]] — Sunbit integration: return_url required, no manual capture, $60-$20k Checkout enforcement
- [[source-stripe-zip]] — Zip: AU+US, 3 products (Zip Pay/Money/Pay-in-4), 14-day direct resolution, 180-day disputes/refunds
- [[source-stripe-zip-accept-payment]] — Zip integration: return_url required, no manual capture, Direct API deprecated
- [[source-stripe-real-time-payments]] — Real-time payments: Pay by Bank/PayNow/PayTo/PromptPay/Swish, PayTo standout (SetupIntents)
- [[source-stripe-pay-by-bank]] — Pay by Bank Payments. Dated documentation and November 2026 changes.
- [[source-stripe-pay-by-bank-accept-payment]] — Pay by Bank acceptance. The May guide documents Checkout and Elements and dates the manual statement-descriptor requirement. The November capture links variants.
- [[source-stripe-p24]] — Przelewy24 Payments. Dated documentation and November 2026 changes.
- [[source-stripe-p24-accept-payment]] — Przelewy24 acceptance. The May guide details variant-specific fields and flows. The November selector lists Checkout, Elements and mobile routes.
- [[source-stripe-paynow]] — PayNow: SG-only QR code, 1.3% pricing, T+1 payout, 90-day refunds, no statement descriptor, Terminal
- [[source-stripe-paynow-accept-payment]] — PayNow integration: Checkout + Direct API, confirmPayNowPayment(), inline QR (no redirect)
- [[source-stripe-payto]] — PayTo: AU mandate-based, disputes (final), recurring, 44 banks, mandate field details
- [[source-stripe-pix]] — Pix: Brazil QR/string, Ebanx partner, IOF 3.5%, Pix Automático, non-challengeable disputes
- [[source-stripe-pix-accept-payment]] — Pix integration: 3 paths, setup/subscription Checkout mode, expires_after_seconds, CPF/CNPJ required
- [[source-stripe-pix-save-payment-details]] — Pix save/recurring: Checkout + Direct API, confirmPixSetup/Payment, QR code data fields, mandate revocation
- [[source-stripe-pix-automatico]] — Pix Automático: 3-day pre-debit notification, mandate fields, retry logic, daily schedule prohibited
- [[source-stripe-promptpay]] — PromptPay: TH-only QR, refund requires customer bank input, duplicate QR risk, send_invoice only
- [[source-stripe-promptpay-accept-payment]] — PromptPay integration: Checkout + Direct API, confirmPromptPayPayment(), email only billing field
- [[source-stripe-swish]] — Swish: SE-only mobile redirect + desktop QR, Stripe as MoR, 365-day refunds, no billing
- [[source-stripe-swish-accept-payment]] — Swish integration: 3 paths + mobile SDK, Direct API legal notice, next_action QR data, 20 refreshes, cancelable
- [[source-stripe-upi]] — UPI: India QR/redirect, 60-day refunds, 15k INR recurring limit, non-contestable disputes, UPI AutoPay
- [[source-stripe-upi-accept-payment]] — UPI integration: 4 paths, Checkout setup/subscription mode, 5-min QR expiry, delayed off-session notifications
- [[source-stripe-upi-set-up-future-payments]] — UPI save/recurring: confirmUpiSetup(), full address required, next_action QR data, on-session still redirects
- [[source-stripe-upi-autopay]] — UPI AutoPay: RBI AFA + 24-hour pre-debit notification, mandate defaults (15k INR, 10yr), Adaptive Pricing caveat
- [[source-stripe-vouchers]] — Vouchers hub: Boleto/Konbini/Multibanco/OXXO, cash in-person, 1-day confirmation, no immediate delivery
- [[source-stripe-boleto]] — Stripe describes Boleto as a reusable, regulated Brazil voucher method. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-boleto-accept-payment]] — The 2026-05-07 Boleto guide covers four ways to create and display a Brazil/BRL cash voucher: hosted or embedded Checkout, Elements with the Checkout Sessions API, Elements with the Payment Intents API, and Direct API. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-stripe-boleto-subscription]] — May/November 2026 Boleto subscription invoice collection through `send_invoice` or `charge_automatically`, with dated Customer/Account routes. The customer still actively pays each voucher; invoice collection is not cash auto-debit or proof of a successful off-session payment. (S03 reviewed update, 2026-11-15; dated qualifications apply.)
- [[source-stripe-boleto-invoices]] — May/November 2026 Boleto invoice collection, Customer versus customer-configured Account defaults, invoice due date versus voucher expiry, and send/finalize states. Automatic invoice collection still requires the customer to pay the voucher. (S03 reviewed update, 2026-11-15; dated qualifications apply.)
- [[source-stripe-konbini]] — Konbini is a single-use, Japan-domestic JPY cash voucher method for Japan-based businesses and customers. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-konbini-accept-payment]] — Konbini Checkout and Direct API. The May guide documents voucher issuance, later fulfillment, expiry and refunds. The November selector links both routes.
- [[source-stripe-multibanco]] — Multibanco in Portugal. Compare dated voucher confirmation, payout scope, payment amount and refund terms.
- [[source-stripe-multibanco-accept-payment]] — Multibanco acceptance. The May guide documents voucher instructions, expiry and async payment confirmation. The November capture routes to integration variants.
- [[source-stripe-oxxo]] — OXXO cash vouchers for Mexico buyers in MXN. See the dated merchant-location, preview, payment-confirmation, payout and expiry distinctions.
- [[source-stripe-oxxo-accept-payment]] — OXXO acceptance. The May guide documents voucher creation and later cash payment confirmation. The November capture links implementation variants.
- [[source-stripe-wallets]] — Wallets hub: 17 methods, Samsung Pay Terminal-only, MoMo/GCash waitlist, subscription caveats
- [[source-stripe-alipay]] — Stripe describes Alipay as a single-use China-based wallet with more than a billion active users worldwide. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-alipay-accept-payment]] — The detailed 2026-05-07 guide describes a single-use Alipay payment: the customer authenticates through Alipay after a website or app redirect, then returns for a payment-status notification. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-stripe-amazon-pay]] — Amazon Pay is a reusable wallet that lets customers check out with information held in their Amazon account. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-amazon-pay-accept-payment]] — The May 7, 2026 full guide describes one-time Amazon Pay acceptance through hosted or embedded Checkout, Payment Element, Direct API, iOS, and Android. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-stripe-amazon-pay-set-up-future-payments]] — The May 7, 2026 guide describes saving Amazon Pay details for later charges through hosted Checkout, Direct API, iOS, and Android. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-stripe-apple-pay]] — Apple Pay: iOS/RN/Web, Stripe CSR required, domain registration, merchant tokens (iOS 16+), real card test only
- [[source-stripe-apple-pay-best-practices]] — Stripe's Apple Pay best-practices guide covers express checkout placement, moving registration until after purchase, default payment selection, Apple Pay setup prompts, certificate renewal, testing changes, and merchant tokens for recurring transactions. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-apple-pay-cartes-bancaires]] — Cartes Bancaires + Apple Pay: EUR only, iOS one-line config, web automatic
- [[source-stripe-apple-pay-recurring]] — Stripe's May 7, 2026 guide describes the customer-initiated transaction (CIT) that consumes an Apple Pay cryptogram before later off-session merchant-initiated transactions (MITs). [[stripe]] Checkout and Elements automatically apply the guide's best practices; its manual implementation sequence is for API integrations. (S02 reviewed update, 2026-11-09; dated source qualifications apply.) The November capture supplies variant navigation; functional details remain attributed to earlier full captures.
- [[source-stripe-apple-pay-merchant-tokens]] — The May 7 and November 7, 2026 [[stripe]] guide captures describe requesting Apple Pay merchant tokens (MPANs) for future merchant-initiated recurring, automatic-reload or deferred payments. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-apple-pay-disputes-refunds]] — This short [[stripe]] guide covers Apple Pay disputes, liability shift, and refunds. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-cash-app-pay]] — Cash App Pay is a reusable US wallet method funded by a customer's Cash App balance or linked debit card. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-cash-app-pay-accept-payment]] — Stripe Cash App Pay acceptance guide. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-stripe-cash-app-pay-set-up-payment]] — Stripe's 2026-05-07 detailed guide describes four Cash App Pay setup variants: Checkout, Direct API, iOS, and Android. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-stripe-google-pay]] — The 2026-11-07 base URL capture is a navigation index linking Android, React Native, and Web variants; those variant bodies were not fetched in this job. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-grabpay]] — Stripe describes GrabPay as a single-use Southeast Asian stored-balance wallet. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-grabpay-accept-payment]] — Stripe's archived GrabPay acceptance guide describes five variants: Checkout, Direct API, iOS, Android, and React Native. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-stripe-link]] — Link: two PM type paths (link vs card+wallet), Instant Bank Payments exclusive, Thailand/Brazil caveat
- [[source-stripe-mb-way]] — MB WAY in Portugal. Compare dated account, refund and dispute terms and the May statement-descriptor wording.
- [[source-stripe-mb-way-accept-payment]] — MB WAY acceptance. The May guide documents app approval, delayed outcomes and dated configuration. The November capture links implementation variants.
- [[source-stripe-mobilepay]] — MobilePay in Denmark and Finland. Compare dated business locations, Connect activation, capture limits and fees.
- [[source-stripe-mobilepay-accept-payment]] — MobilePay acceptance. See the May authorization, redirect and capture distinctions and the November implementation selector.
- [[source-stripe-paypal]] — PayPal via Stripe: EU merchants only, marketplace Connect, 180-day refunds, fees not in Stripe tax invoice
- [[source-stripe-paypal-button]] — PayPal button: Stripe decides button vs redirect, blockers for ECE + Checkout, PayPal must not be sole PM type
- [[source-stripe-paypal-activate]] — PayPal activation: EU (ex Hungary), settlement preference, Connect manual onboarding, account switch disables recurring
- [[source-stripe-paypal-accept-payment]] — PayPal accept-a-payment: 5 platforms, auth windows by settlement type, preferred locale, statement descriptor, payer fields
- [[source-stripe-paypal-set-up-future-payments]] — PayPal save/recurring: Checkout setup mode, confirmPayPalSetup(), Fraudnet risk_correlation_id, mandate BAID, on-session return_url rules
- [[source-stripe-paypal-settlement]] — PayPal settlement preference: Stripe vs PayPal balance, Dashboard reporting, reconciliation, support ticket to change
- [[source-stripe-paypal-disputes]] — PayPal disputes: 180-day window, 2–19 day evidence, 30-day decision, no Stripe appeals, multiple disputes per payment
- [[source-stripe-paypal-reconciliation]] — PayPal reconciliation: reference field (Invoice ID) vs transaction_id (Transaction ID), PayPal settlement report
- [[source-stripe-paypal-import]] — PayPal billing agreement import: billing_agreement_id on SetupIntent, offline mandate, no cancellation webhooks for imported BAIDs
- [[source-stripe-revolut-pay]] — Revolut Pay: UK/EU, 6 currencies, full feature set, 120-day disputes, 35-day Revolut decision
- [[source-stripe-revolut-pay-accept-payment]] — Revolut Pay integration: 6 platforms, mobile redirect + desktop QR (20× refresh), 7-day manual capture, live auto-approves
- [[source-stripe-revolut-pay-set-up-future-payments]] — Revolut Pay save/recurring: on-session always redirects, confirmRevolutPaySetup(), authorization text, detach triggers mandate.updated
- [[source-stripe-paypay]] — PayPay: Japan/JPY only, no recurring/Connect/disputes, 365-day instant refunds, 50–1M JPY limits
- [[source-stripe-paypay-accept-payment]] — PayPay integration: 6 platforms, payment mode only, redirect-based, live mode no approve/decline, 5 error codes
- [[source-stripe-satispay]] — Satispay: Italy/EUR only, 20 eurozone merchant countries, 12-day dispute evidence, 180-day refunds, 14 prohibited categories
- [[source-stripe-satispay-accept-payment]] — Satispay integration: 4 web paths + iOS/Android, payment mode only, manual capture 7-day, confirmSatispayPayment(), 5 error codes
- [[source-stripe-secure-remote-commerce]] — SRC/Click to Pay: US only, replaces Visa Checkout + Masterpass, card.masterpass PM type, Masterpass deprecated
- [[source-stripe-vipps]] — Vipps: Norway/NOK card wallet, private preview, card transaction underneath, daily Vipps fee billing, BankAxept→Visa/MC
- [[source-stripe-vipps-accept-payment]] — Vipps integration: 3 paths (Checkout/Elements/Direct API), 5-min auth window, full-amount-only capture, card retry in app
- [[source-stripe-wechat-pay]] — WeChat Pay: 800M+ users, CNY+12 currencies, 22 merchant countries, no disputes/recurring/manual capture, partial Connect
- [[source-stripe-wechat-pay-accept-payment]] — WeChat Pay integration: Checkout + Direct API (web only), confirmWechatPayPayment(), QR from next_action, 37 business locations
- [[source-stripe-local-payment-methods-by-country]] — hub: Nigeria (Naira cards) + South Korea (KakaoPay, local cards), no local entity required
- [[source-stripe-nigeria-payment-methods]] — May/November 2026 Nigerian local-payment overviews: a Nigerian partner acts as merchant of record. November access is invite-only; wallet prose conflicts with its unsupported product/API cells, so the source preserves both rather than inferring availability. (S03 reviewed update, 2026-11-15; dated qualifications apply.)
- [[source-stripe-ng-bank-transfer-accept-payment]] — Nigeria bank transfer. See the May PaymentIntent redirect and fulfillment guidance and the November implementation selector.
- [[source-stripe-ng-card-accept-payment]] — Accept a payment using local cards in Nigeria. November 2026 variant navigation and earlier detailed guidance.
- [[source-stripe-ng-card-set-up-future-payments]] — Set up future payments with Naira card. November 2026 variant navigation and earlier detailed guidance.
- [[source-stripe-korea-payment-methods]] — The May 8 and November 7, 2026 Stripe overviews describe KRW payments from South Korean customers through local cards and wallets, using Stripe and a local processor partner without requiring a local South Korean entity. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-kr-card-accept-payment]] — South Korea card acceptance. See the May Direct API disclosure, eligibility and redirect scope and the November selector.
- [[source-stripe-kr-card-set-up-future-payments]] — South Korea card setup and recurring charges. The May guide separates Accounts v2 and Customers v1 and scopes the automatic-capture rule to recurring use. November links variants.
- [[source-stripe-kakao-pay-accept-payment]] — The full 2026-05-08 guide describes one-time Kakao Pay (`kakao_pay`) acceptance through Checkout or a Direct API PaymentIntent, with a redirect to Stripe's local processor partner for authentication and authorization. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-stripe-kakao-pay-set-up-future-payments]] — The full guide captured on 2026-05-08 describes saving Kakao Pay (`kakao_pay`) for later payments through Checkout setup mode or a Direct API SetupIntent, and a separate PaymentIntent route for saving during a payment. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-stripe-naver-pay-accept-payment]] — One-time Naver Pay acceptance. The May guide covers Checkout, Elements and Direct API. November links variants.
- [[source-stripe-naver-pay-set-up-future-payments]] — Naver Pay setup and recurring charges. The May guide limits recurring capture to automatic and contains a dated currency example discrepancy. November links setup variants.
- [[source-stripe-payco-accept-payment]] — Accept a payment using PAYCO in South Korea. November 2026 variant navigation and earlier detailed guidance.
- [[source-stripe-custom-payment-methods]] — Custom PMs overview: type:'custom'/cpmt_ IDs, integration matrix, marks compliance, crypto restriction (ID/TH), Stripe disclaimer
- [[source-stripe-paypal-custom-payment-method]] — PayPal as CPM: low-code adapter for Checkout, EU→standard PM vs global→CPM adapter decision rule
- [[source-stripe-payment-method-support]] — comprehensive reference: 36 PMs country/currency + product support matrices + API support (setup_future_usage, return_url)
- [[source-stripe-payment-method-connect-support]] — Connect reference for 31 PMs: capability names, MoR tables, notable restrictions (Alma/PayPal marketplace-only, ACH cloning, iDEAL compliance)
- [[source-stripe-pmd-registration]] — Domain registration: 6 PMs (Apple Pay required), PaymentMethodDomain API, iframe Safari 17+ rules, Connect charge-type routing
- [[source-stripe-dynamic-payment-methods]] — Dynamic PMs: migration guide, excluded_payment_method_types (wallets exception), 6 eligibility criteria, AI ordering models
- [[source-stripe-a-b-testing-payment-methods]] — Stripe's captured guide describes a no-code Dashboard experiment that offers selected payment methods to treatment traffic and compares outcomes with control traffic. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-payment-method-rules]] — PM rules: amount/location conditions, no-code Dashboard setup, subscription caveat, currency auto-conversion, location testing via email
- [[source-stripe-payment-method-configurations]] — PM configurations: named pmc_ sets, Web/iOS/Android integration, Apple Pay on/Google Pay off defaults, config vs exclusion decision rule
- [[source-stripe-link-payment-methods]] — Link payment methods (US-only): Instant Bank Payments/Klarna/Pix/UPI/Stablecoins, zero integration, 5 eligibility criteria, BNPL individually configurable
- [[source-stripe-instant-bank-payments]] — Instant Bank Payments. Compare dated dynamic amount limits, settlement conditions, bank returns and the mobile documentation discrepancy.
- [[source-stripe-klarna-on-link]] — Klarna on Link. Compare the dated eligibility, buyer flow and Stripe-balance and payout wording.
- [[source-stripe-pix-on-link]] — Pix on Link for BRL payments. Compare the November USD-equivalent range, the May minimum and dated US eligibility and non-US preview scope.
- [[source-stripe-stablecoins-on-link]] — Stablecoins on Link for eligible one-time, on-session USD payments. See dated merchant and buyer eligibility, payment limits and completed USD balance settlement.
- [[source-stripe-upi-on-link]] — UPI on Link. The November INR range starts at the USD 0.50 equivalent and is capped at INR 100,000. See the dated May minimum and eligibility qualifications.
- [[source-stripe-checkout-link]] — Link in Checkout. See the dated dynamic and manual setup examples, embedded domain registration, Connect and sandbox scope.
- [[source-stripe-elements-link]] — Link with Web Elements. Dated documentation and November 2026 changes.
- [[source-stripe-express-checkout-link]] — Link in Express Checkout Element. The guide names six built-in methods and qualifies when eligible buttons appear.
- [[source-stripe-payment-element-link]] — Link in web Payment Element. See dated email collection, accelerated signup, domain registration and funding scope.
- [[source-stripe-payment-request-button-link]] — Historical Link integration for Payment Request Button. See the versioned Endive cutoff and the dedicated migration paths.
- [[source-stripe-card-element-link]] — Adding Link to existing Card Element integrations. See typical field dimensions, Connect scope and the separately dated Contact Details Element guidance.
- [[source-stripe-mobile-payment-element-link]] — Link in the Mobile Payment Element. Dated documentation and November 2026 changes.
- [[source-stripe-invoicing-link]] — Link on Stripe-hosted invoices. Enabling Link on the Hosted Invoice Page requires no extra implementation code. See dated account defaults, API overrides and invoice states.
- [[source-stripe-link-payment-integrations]] — Standalone and card-specific Link integration. See the dated routing and request fields, response shapes, pricing and retry conditions.
- [[source-stripe-add-link-elements-integration]] — Custom Link checkout with PaymentIntents. November shows Contact Details Element and CustomerSession redisplay. May retains Link Authentication Element and Ephemeral Key examples.
- [[source-stripe-link-save-and-reuse]] — Link payment method reuse. Compare dated contact and account examples with server confirmation and later off-session use.
- [[source-stripe-payments-optimization]] — The Optimization Dashboard reports **estimated** effects of Authorization Boost features on card-not-present (CNP) payment attempts: recovered payment volume and count, success-rate increase, and network cost savings. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-authorization-boost-ab-test]] — Auth Boost A/B test: 30-day free test, CAU runs on both groups, 12-month cooldown, 37-day results, paid add-on
- [[source-stripe-payments-recommendations]] — The May 8 and November 7, 2026 full captures describe **Payments analytics recommendations** as suggestions shown on the Stripe Dashboard **Acceptance** page to help a business consider revenue or fraud-protection changes. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-3d-secure-authentication-flow]] — Stripe's 3D Secure (3DS) authentication guide covers Web, iOS, Android, and React Native, with automatic and manual triggering, web display, mobile customization, test cases, and conditional fraud-dispute liability shift. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-sca-exemptions]] — The 2026-05-08 and 2026-11-07 captures describe SCA exemptions and Data Only for EEA, Switzerland, and UK card payments. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-standalone-3ds]] — Stripe's standalone 3DS API runs EMV 3D Secure authentication separately from payment authorization. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-3ds-import]] — Import 3DS results: travel/third-party 3DS, confirm+error_on_requires_action, exemption import, Cartes Bancaires cb_avalgo
- [[source-stripe-3ds-sigma-query]] — Sigma authentication_report_attempts: is_final_attempt dedup, auth rate calc, SCA exemption columns
- [[source-stripe-sca-readiness]] — SCA readiness: EEA scope, grandfathering (EU Dec 2020/UK Sep 2021), off-session checklist, MIT mandate, Charges API not SCA-ready
- [[source-stripe-currencies]] — Stripe's supported-currencies guide describes 135+ charge currencies, payment-method/presentment/settlement currencies, API amount formatting, special currency rules, charge minima and maxima, and its EEA card-pricing grouping. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-react-stripejs]] — React Stripe.js reference: CheckoutElementsProvider/useCheckoutElements + Elements/useStripe/useElements/ElementsConsumer
- [[source-github-stripe-node]] — cumulative `stripe` Node SDK through `23.0.0`: Endive migration, context fix, webhook/transport and checkout/Billing contracts; v22 retained
- [[changelog-github-stripe-node]] — package-qualified stripe-node release history through `23.0.0`, preserving all ingested v22 entries
- [[source-github-react-stripe-js]] — cumulative react-stripe-js history through `@stripe/react-stripe-js@7.0.0`: wrapper removal, Stripe JS v10 peer contract, React 19 lifecycle guard and preserved v6 knowledge
- [[changelog-github-react-stripe-js]] — package-qualified react-stripe-js release history
- [[source-stripe-bizum]] — Bizum is a customer-initiated, real-time payment method for customers in Spain: the customer enters a Bizum-registered phone number and approves the payment in their bank app. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-declines-overview]] — Stripe's May 9 and November 7, 2026 guides distinguish issuer or payment-provider declines, Stripe-blocked payments, and invalid API calls. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-card-declines]] — The May 9 and November 7, 2026 [[stripe]] guide captures explain card-issuer declines, their network and Stripe advice fields, retry guidance, and on-session versus off-session handling. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-decline-codes]] — This is Stripe's decline-code reference for card and local payment method (LPM) failures, captured on May 9 and November 7, 2026. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-network-decline-codes]] — The May 9, 2026 [[stripe]] reference lists raw response codes for seven payment-method groupings: ACH Direct Debit, Australia BECS, Bacs, Cash App Pay, New Zealand BECS, Canadian pre-authorized debit, and SEPA Direct Debit. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-disputes-how-disputes-work]] — Stripe's guide to the card dispute lifecycle: early fraud warnings (EFWs) and inquiries before a chargeback, formal dispute timing and fees, issuer decisions, and local payment method differences. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-disputes-responding]] — Stripe's November 7, 2026 responding guide covers the Dashboard response window, inquiries, Visa and Mastercard compliance disputes, eligible Visa CE 3.0 and possible 3D Secure liability shift, final evidence submission, fees, and issuer-decided outcomes. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-disputes-categories]] — Stripe's dispute category guide maps the listed card, wallet, and Buy now, Pay Later reason codes to category-specific defense guidance. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-disputes-reason-codes]] — Stripe's 2026-11-07 guide describes common Visa, Mastercard, and American Express dispute reason codes in seven categories, with possible evidence examples for each code. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-disputes-visual-evidence]] — Stripe gives **illustrative, non-exhaustive** evidence-packet examples for seven dispute categories. **Credit not processed** and **Duplicate** explicitly show paired **Approved** and **Denied** packet sections; the other categories give counter-evidence examples without that paired structure. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-disputes-best-practices]] — Stripe's November 7, 2026 capture describes evidence organization, estimated win likelihood, dispute-specific page limits and the API page-limit error, authorization and delivery proof, partial refunds, and Visa compelling evidence. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-disputes-api]] — Stripe's May 9 and November 7, 2026 guides describe API-based dispute retrieval, evidence updates, listing by a PaymentIntent or Charge, and webhook events. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-disputes-visa-ce3]] — API-level details for submitting Visa Compelling Evidence 3.0 (CE 3.0) to fight friendly fraud disputes. (S02 reviewed update, 2026-11-09; dated source qualifications apply.) The November capture supplies variant navigation; functional details remain attributed to earlier full captures.
- [[source-stripe-disputes-visa-compliance]] — Stripe's API guide for identifying, closing, and responding to Visa compliance disputes, called pre-compliance disputes by Visa. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-disputes-withdrawals]] — Stripe's guide to cardholder withdrawals of financial chargebacks, evidence after a withdrawal request, refund limits, fees, and late issuer adjustments. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-disputes-high-risk-lists]] — MATCH (code 4: >1% MC chargebacks + $5k) and VMSS (code 22: 1000 disputes + 1.8%) criteria, removal rules
- [[source-stripe-disputes-measuring]] — The May 10 and November 7, 2026 captures distinguish dispute activity by dispute date from dispute rate by original charge date, each using successful payments as its denominator. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-disputes-monitoring-programs]] — Stripe's dated general monitoring guide adds Visa MERP for Asia Pacific, effective October 2026, alongside VAMP and other programs; this is not authoritative current network-rule or account-status proof. (S02 reviewed update, 2026-11-09.)
- [[source-stripe-disputes-prevention]] — Dispute prevention: resolution (Radar rules, no rate impact), deflection (Verifi/Order Insights), Smart Disputes (AI evidence)
- [[source-stripe-disputes-prevention-how-it-works]] — Stripe's 2026-11-07 guide covers Visa/Verifi Rapid Dispute Resolution (RDR) and Order Insights (OI), and Mastercard/Ethoca Alerts and Consumer Clarity (CC). (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-smart-disputes]] — Smart Disputes uses an AI rules engine to collect, compile, and submit evidence for **eligible card disputes**. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-smart-disputes-setup]] — The 2026-11-07 setup guide describes Smart Disputes enrollment, evidence packet submission choices, data-quality guidance at charge and dispute time, and `smart_disputes.status` packet availability. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-smart-disputes-auto-respond]] — Smart Disputes auto-respond: direct/Connect/connected account config, preference (on/off/inherit) API field
- [[source-stripe-radar-how-it-works]] — Radar: 3 tiers (base/Fraud Teams/Platforms), pricing, screened payment methods, 6 core features
- [[source-stripe-radar-optimize-risk-factors]] — Risk factors: advanced +36%, IP +12%, email +11%; integration ranking; Stripe.js on every page; Customer object best practices
- [[source-stripe-radar-sessions]] — Radar Sessions: for direct API/third-party tokenization; createRadarSession(); on/off-session attachment strategy
- [[source-stripe-radar-risk-evaluation]] — Risk levels (highest/elevated/normal), 0-99 score, outcome fields, object support, feedback loop, 92%/82%/71% network coverage
- [[source-stripe-radar-custom-fraud-models]] — Custom fraud models: business metadata + global signals, per-merchant training, no integration changes needed
- [[source-stripe-radar-customer-evaluation]] — Customer Evaluation API: multi_accounting + account_sharing upfunnel signals, same Customer ID constraint
- [[source-stripe-radar-free-trial-abuse]] — Free trial abuse: blocks high-risk trial starts, auto-detected, Sigma monitoring via rule_decisions table
- [[source-stripe-radar-payg-abuse]] — PAYG abuse: non_payment_abuse signal for usage-based billing, fail-open Payment Evaluation API
- [[source-stripe-radar-bot-abuse]] — Bot score (0-99, Checkout only): anti-scripting enforcement via Dashboard/Sigma/:bot_score: rules
- [[source-stripe-radar-multiprocessor]] — Multiprocessor: evaluate non-Stripe payments with Radar; 3 signals; card-only PaymentMethod required
- [[source-stripe-radar-issuing]] — Radar for Issuing: IssuingAuthorizationEvaluation API, real-time fraud scoring before authorization decision
- [[source-stripe-radar-risk-settings]] — Risk settings (3 presets), 4 risk controls, 5 scores (fraudulent_dispute/EFW/bot/risk_score deprecated)
- [[source-stripe-radar-supported-payment-methods]] — Radar PM coverage: cards/ACH/SEPA fully supported; BNPL/wallets/stablecoin in preview
- [[source-stripe-radar-reviews]] — Review queue: Smart Refunds (72% very high), actions, assignments, review.opened/closed webhooks
- [[source-stripe-radar-risk-insights]] — Risk insights: fraud factor multipliers, top factors, related payments, 6-month data limit
- [[source-stripe-radar-reviews-auth-capture]] — Auth-capture review: approve ≠ capture; review.closed webhook auto-capture pattern
- [[source-stripe-radar-lists]] — Lists: default (Cards/ACH/SEPA), 11 custom types, 50k limit, 30-day allowlist max, fraud report auto-populates block lists
- [[source-stripe-radar-rules]] — Rules: 4 actions, built-in rules, syntax, 3DS attributes, Radar Assistant, 200 rule limit
- [[source-stripe-radar-rules-reference]] — Rules reference: processing order, attribute types, operators, velocity buckets, missing attributes, metadata scopes
- [[source-stripe-radar-rules-supported-attributes]] — Supported attributes: 5 categories, 827-line reference (risk/IP/email/distance/fingerprint/time/crypto)
- [[source-stripe-radar-testing]] — Test cards for highest/elevated risk, rule backtesting (6-month historical), when to implement each rule type
- [[source-stripe-radar-rules-disputes]] — Dispute resolution rules: Resolve dispute action, is_fraudulent + network_reason_code attributes
- [[source-stripe-radar-analytics]] — Radar analytics: fraud/dispute/block rate charts, benchmarks, rule match breakdown, 24hr delay
- [[source-stripe-radar-fraud-alerts]] — Fraud alerts: auto-detected attack patterns, email+bell, investigation page, Fraud Teams extra actions
- [[source-stripe-radar-fraud-insights]] — Fraud insights: Insights tab, default filters (risk>65+velocity), pivot chart, drill-down transaction list
- [[source-stripe-radar-for-platforms]] — Radar for Platforms: connected account risk scores (highest≥90%/elevated 50-89%), investigation, reject (7 codes), reserves
- [[source-stripe-radar-account-risk-signals]] — Account Signals API: 3 signal types (fraudulent merchant/delinquency/website), webhook-driven
- [[source-stripe-disputes-prevention-overview]] — Dispute prevention nav page (links to fraud types, card testing, identify fraud, best practices)
- [[source-stripe-disputes-fraud-types]] — The May 10 and November 7, 2026 captures describe the same online-fraud patterns, actors, possible loss, and prevention ideas. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-disputes-card-testing]] — Stripe's card-testing prevention guide describes how stolen or enumerated card details can be tested through card setup or small payments, how to recognize possible attacks, and mitigations for integrations that save cards or make payments. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-disputes-identifying-fraud]] — Stripe's guide lists possible payment-fraud indicators and merchant review steps for physical shipping, digital goods, and donations. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-disputes-verification]] — The May and November 2026 captures give substantively the same guidance on CVC and address verification. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-disputes-prevention-best-practices]] — The May 10 and November 7, 2026 same-URL captures organize dispute and fraud prevention practices into tools for everyone, tools for users of Radar, and developer tools. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-disputes-advanced-fraud-detection]] — Stripe's November 7, 2026 guide describes device and activity signals collected through Stripe.js and the iOS and Android SDKs for fraud detection. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-disputes-customer-abuse]] — Customer abuse: refund/resale/trial abuse, Sigma refund query, Radar velocity rules for resellers
- [[source-stripe-payouts]] — Payouts: initial timing (7-14d), schedule options, multi-currency settlement, 80+ country bank account formats
- [[source-stripe-payouts-reconciliation]] — Payout reconciliation: API flow (BalanceTransactions), expand pattern, manual payout caveat
- [[source-stripe-payouts-trace-ids]] — Payout trace IDs: 3 statuses, 10-day window, unsupported countries, Connect support
- [[source-stripe-payouts-statement-descriptors]] — Payout statement descriptors: 2 levels, precedence (payout>account>STRIPE), bank display caveat
- [[source-stripe-payouts-multicurrency]] — Multi-currency settlement: 10 regions, no FX fees, 1 bank account per currency, minimum balance
- [[source-stripe-payouts-next-day]] — Next-day settlement: US only, 0.6%/month, ACH excluded, >$1M adds 1 day, vs Instant Payouts
- [[source-stripe-payouts-instant]] — Instant Payouts: 37 countries, within 30 min, 1–1.5% fee, 10/day limit, instant_available balance
- [[source-stripe-payouts-start-of-day]] — Customized start of day: APAC only (10 countries), local timezone grouping, not retroactive
- [[source-stripe-payouts-minimum-balance]] — Minimum balance: retain fixed amount after payout, 4-5× daily vol, Connect API, not BR/IN/TH
- [[source-stripe-receipts]] — Receipts: 30-day expiry, auto/manual send, refund receipts, invoice itemized, Connect branding rules
- [[source-stripe-refunds]] — Refunds: reversal vs refund, ARN tracing, 7 failed reasons, cancel rules, Connect behavior, events
- [[source-stripe-payments-existing-customers]] — Stripe's 2026-11-07 canonical capture identifies charging an existing payment method while the customer is on-session and lists five web variants. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-stripe-two-step-confirmation]] — The 2026-11-07 full capture describes a two-step web payment checkout: collect details in the Payment Element before creating a PaymentIntent, create a ConfirmationToken, optionally show a review page or run validation and tax calculation, then create the PaymentIntent on the server and confirm it from the client with the token. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-surcharge]] — The public-preview PaymentIntent surcharge guide describes how merchants, and connected accounts on platforms that set and collect payment fees, can offset some card acceptance costs. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-accept-payment-deferred]] — The 2026-05-11 retained guide describes rendering the Payment Element before creating an Intent, with separate web payment, setup, and subscription variants. (S02 reviewed update, 2026-11-09; dated source qualifications apply.) The November capture supplies variant navigation; functional details remain attributed to earlier full captures.
- [[source-stripe-finalize-payments-server]] — The 2026-11-07 canonical capture describes rendering the Payment Element before creating a PaymentIntent or SetupIntent and confirming the Intent on the server. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-stripe-moto]] — MOTO: SCA out-of-scope exemption, PCI compliance required, moto parameter on PI/SI
- [[source-stripe-payments-without-auth]] — Legacy US/CA-only: CardElement + createPaymentMethod, error_on_requires_action=true, synchronous
- [[source-stripe-save-card-without-auth]] — Legacy save card (US/CA): createPaymentMethod→Customer, error_on_requires_action, setup_future_usage=on_session
- [[source-stripe-migrate-basic-card-integration]] — Migrate legacy to auth-handling: remove error_on_requires_action, confirmation_method='manual', handleCardAction
- [[source-stripe-vault-and-forward]] — Vault and Forward API: forward card details to 30+ processors, replacement fields, wallet support, PGP encryption
- [[source-stripe-forwarding-third-party]] — This Stripe guide describes collecting card details with Payment Element, creating a Stripe PaymentMethod on the client, then asking a merchant server to create a ForwardingRequest for a configured third-party processor. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-forwarding-token-vault]] — The 2026-05-11 and 2026-11-07 guides describe a support-gated path for forwarding card details stored in Stripe's vault from a PaymentMethod to an in-house token vault. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-payment-line-items]] — Payment line items: L2/L3 interchange savings, Klarna/PayPal auth rates, field requirements, MCC eligibility, arithmetic validation
- [[source-stripe-payment-line-items-flexible]] — Payment line items with flexible payments: multicapture aggregation rules, overcapture, incremental auth, partial auth mismatch handling, surcharge
- [[source-stripe-industry-metadata]] — Industry metadata is structured travel and entertainment transaction data passed through the Payment Intents API. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-multicapture]] — Multicapture. Compare dated feature availability, request and final-capture rules, and integration-specific behavior.
- [[source-stripe-overcapture]] — Overcapture. Compare dated availability, network and category limits, authentication constraints and integration-specific behavior.
- [[source-stripe-extended-authorization]] — The May 11, 2026 full guide describes an IC+ online card feature that can extend an uncaptured authorization beyond the usual seven-day online window, up to 30 days under qualifying network and merchant-category rules. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-stripe-incremental-authorization]] — Stripe incremental authorization increases the authorized amount on a **confirmed, uncaptured PaymentIntent** before capture. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-stripe-partial-authorization]] — Partial Authorization for eligible cards. See dated network, issuer, approval and capture conditions, including the overcapture limit after partial approval.
- [[source-stripe-flexible-features-migration]] — The **2026-05-11 full guide** describes migration of four non-card-present flexible payment scenarios from private beta to general release: incremental authorization, overcapture, extended authorization and multicapture. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-stripe-off-session-payments-api]] — Stripe Off-Session Payments API. See the dated consent, version and private-preview boundaries for smart retries and multi-processor routing.
- [[source-stripe-orchestration]] — Stripe Payment Orchestration. Compare dated preview access, rule-based processor routing, retry and payment-method exclusions.
- [[source-stripe-orchestration-route-payments]] — Orchestration: Route Payments to Multiple Processors. Dated documentation and November 2026 changes.
- [[source-stripe-orchestration-rules]] — Payment Orchestration rules. See dated account routing, independent retry selection, and separate sandbox and live rule-set scope.
- [[source-stripe-orchestration-retries]] — Cross-processor retry. See dated authentication and retry-processor compatibility rules, including the separate Stripe-main block-as-decline case.
- [[source-stripe-orchestration-feature-support]] — Payment Orchestration feature matrix. See dated processor, account-override, fallback and wallet limits.
- [[source-stripe-orchestration-wallet-payments]] — Apple Pay and Google Pay routing with Orchestration. See the dated saved-method, authentication and processor compatibility limits.
- [[source-stripe-crypto-onramp]] — The May 11 and November 7, 2026 captures describe [[stripe]]'s fiat-to-crypto onramp, where customers can purchase and exchange crypto through Stripe-hosted, embedded web, or embedded mobile components paths. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-crypto-onramp-stripe-hosted]] — The May 11 and November 7, 2026 captures describe the Stripe-hosted standalone crypto onramp at `crypto.link.com`: platforms redirect users there through either a frontend-generated URL or a backend-created onramp session with a redirect URL. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-crypto-onramp-embedded]] — Embedded onramp: credit/debit/ApplePay/ACH, instant delivery post-KYC, Link for returning users, webhook per status change
- [[source-stripe-crypto-onramp-embedded-quickstart]] — Stripe's [[stripe]] embedded fiat-to-crypto onramp quickstart describes a test-key integration that creates an `OnrampSession` on a server, returns its client secret, and mounts a client-side iframe. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-crypto-onramp-embedded-setup]] — The May 11 and November 7, 2026 captures are an extended embedded onramp setup guide for [[stripe]]'s fiat-to-crypto widget, distinct from the simpler quickstart and from the private-preview headless Embedded Components flow in [[stripe-crypto-onramp]]. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-crypto-onramp-embedded-components]] — The May 2026 headless quickstart remains historical guidance; the November 2026 capture is an Embedded Components hub with a separate quickstart URL and platform/KYC routes. The hub does not renew the older API, preview or eligibility claims. (S02 reviewed update, 2026-11-09.)
- [[source-stripe-crypto-onramp-embedded-components-integration]] — The May 2026 capture is the full Embedded Components (headless) onramp integration guide for Web, React Native, Android, and iOS. (S02 reviewed update, 2026-11-09; dated source qualifications apply.) The November capture supplies variant navigation; functional details remain attributed to earlier full captures.
- [[source-stripe-crypto-onramp-kyc-integration]] — Stripe's Embedded Components onramp KYC guide describes L0/L1/L2 identity tiers, asynchronous verification, CryptoCustomer status checks, and how to respond to token or session errors. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-agentic-commerce-for-sellers]] — Agentic Commerce Suite: catalog feed (v2 API), order fulfillment, order approval + customization hooks, manual capture
- [[source-stripe-agentic-commerce-custom-integration]] — ACS custom integration (third-party processors): reverse API hooks, SPT resolve + credential types, payment recording
- [[source-stripe-mcp-monetize]] — MCP app monetization: Redirect (public) vs Instant Checkout (OpenAI private beta), feature comparison
- [[source-stripe-mcp-accept-payment]] — MCP accept payment: Redirect (Checkout Session) + Instant Checkout (window.openai.requestCheckout + SPT) integration
- [[source-stripe-agentic-commerce-for-agents]] — ACS for agents: OCA lifecycle, SFTP product feeds, RequestedSession checkout, payment methods, next actions, mobile SDK
- [[source-stripe-machine-payments]] — Machine Payments (Frontier): agent-to-API pay-per-use, MPP + x402 protocols, Base/Solana/Tempo, min 0.01 USDC, NY+TX excluded
- [[source-stripe-machine-payments-mpp]] — MPP implementation: mppx library, HTTP 402 middleware, crypto + SPT flows, link-cli testing
- [[source-stripe-machine-payments-mpp-quickstart]] — MPP quickstarts. Compare the dated May Hono example with the November profile-backed guide for card SPTs and Tempo stablecoins.
- [[source-stripe-machine-payments-x402-quickstart]] — x402 Base USDC quickstarts. Compare May deposit-mode payment with November precreated recipients and recording verified on-chain settlement.
- [[source-stripe-machine-payments-x402]] — x402 integration guide: USDC contract addresses for Tempo/Base/Solana, CDP mainnet facilitator
- [[source-stripe-shared-payment-tokens]] — The full 2026-05-12 Stripe guide describes Shared Payment Tokens (SPTs) from both roles: an agent issues a scoped grant of a customer's payment method to a seller, and the seller receives a granted token for payment processing. (S02 reviewed update, 2026-11-09; dated source qualifications apply.) The November capture supplies variant navigation; functional details remain attributed to earlier full captures.
- [[source-stripe-agentic-commerce-product-feed]] — ACS catalog feed: 4 feed types, field reference (shipping/tax/variants/relationships/compliance), upsert vs replace
- [[source-stripe-agentic-commerce-sftp-catalog]] — ACS SFTP ingestion (agent side): directory structure, manifest pattern, deletion rules, idempotency
- [[source-stripe-ucp]] — Universal Commerce Protocol: open standard, 4 capabilities, Stripe as UCP Tech Council member
- [[source-stripe-acp]] — Agentic Commerce Protocol: co-built by Stripe/OpenAI/Meta, 5 capabilities (checkout/cart/payment/auth/orders)
- [[source-stripe-billing-apis]] — Stripe's Billing API overview relates the 11 subscription, billing, payment, customer, and entitlement objects. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-subscriptions-overview]] — Stripe subscription lifecycle guide covering creation, initial and recurring invoices, eight statuses, payment recovery, status resolution, cancellation and access provisioning. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-checkout-subscriptions-quickstart]] — Stripe Billing's hosted [[stripe-checkout]] subscription quickstart demonstrates a product with a recurring Price, a Checkout Session in `subscription` mode, a customer portal, and webhook and entitlement guidance. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-subscriptions-design-integration]] — Stripe's subscriptions design guide helps choose a pricing model, checkout interface, and payment timing, then routes six example combinations to deeper implementation guides. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-build-subscriptions]] — Full subscriptions integration guide: 3 UI paths, billing_mode:flexible, provision access, test payment methods
- [[source-stripe-recurring-pricing-models]] — Recurring pricing models reference: flat rate, per-seat, tiered, usage-based
- [[source-stripe-flat-rate-pricing]] — Flat rate pricing setup: Product + monthly/yearly Price + Subscription API, can't edit after subscription created
- [[source-stripe-per-seat-pricing]] — Per-seat pricing: flat rate API + quantity param in subscription items (seats = units)
- [[source-stripe-usage-based-pricing]] — Usage-based pricing: fixed fee+overage (licensed+metered prices), pay-as-you-go, credit burndown via billing.creditGrants
- [[source-stripe-tiered-pricing]] — Tiered pricing: volume vs graduated math, flat_amount per tier, quantity=0 edge case
- [[source-stripe-pricing-table]] — The May 12 and November 7, 2026 captures describe a Dashboard-created embeddable subscription pricing table. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-subscriptions-setup-intents]] — SetupIntents for zero-payment subs: auto-created, auth vs authorization failures, doesn't auto-cancel
- [[source-stripe-subscriptions-migration]] — Subscription migration: Zuora/Recurly/Chargebee → toolkit or APIs, PAN import, decision matrix
- [[source-stripe-subscriptions-migration-toolkit]] — Stripe's Dashboard Billing migration toolkit imports subscription data from a third-party, home-grown, or another Stripe account through CSV and creates scheduled Stripe subscriptions. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-subscriptions-migration-api]] — API-based guide for migrating subscriptions from another processor, an in-house system, or an existing Stripe account into Stripe Billing. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-subscriptions-webhooks]] — Stripe's May 12 and November 7, 2026 captures explain subscription event handling, payment and status monitoring, access decisions, invoice finalization, and optional Amazon EventBridge or Azure Event Grid delivery. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-subscriptions-billing-cycle]] — Stripe's billing-cycle guide explains how recurring price intervals and billing-cycle anchors align future renewal dates. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-subscriptions-trial-offers]] — Trial Offers API (preview): 4 use cases, flexible billing required, status behavior, opt-in cancellation, billing anchor
- [[source-stripe-subscriptions-trial-compliance]] — Trial compliance: 7-day reminder emails, statement descriptor 22-char limit + * TRIAL OVER, manual path
- [[source-stripe-subscriptions-free-trials]] — Both the May 12 and November 7, 2026 captures call `trial_end` free-trial periods a **legacy** integration path and recommend Trial Offers for new integrations. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-subscriptions-billing-mode]] — Stripe's subscription billing mode guide documents the `classic` and `flexible` modes, their version-dependent defaults, creation and migration routes, and proration discount display. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-subscriptions-billing-mode-compare]] — Stripe compares classic and flexible subscription billing to help an integration assess a migration. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-subscriptions-mixed-interval]] — The 2026-05-13 combined Stripe guide describes mixed interval subscriptions: one subscription with items that have different prices and billing periods. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-subscriptions-coupons]] — Stripe's subscription-discount guide distinguishes coupons, which define a discount and can be applied by a backend, from customer-facing promotion codes that reference a coupon and inherit its product restrictions. (S01 reviewed update, 2026-11-08; dated source qualifications apply.)
- [[source-stripe-bizum-accept-payment]] — Stripe's Bizum acceptance guide. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-metronome-guides-customers-billing-optimize-customer-experience-india-e-mandates]] — Metronome-documented Indian-card flow in which Stripe creates and manages the SetupIntent mandate, reports action-required handling, and owns mandate lifecycle
- [[source-stripe-ach-sec-codes]] — Standard Entry Class (SEC) codes describe how a customer or business authorized an ACH transaction. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-acss-accept-payment]] — The 2026-05-02 guide covers Canadian pre-authorized debit (PAD/ACSS Debit) through Checkout and a Direct API PaymentIntent flow, including mandate options, bank verification, delayed payment status, testing, and target debit dates. (S02 reviewed update, 2026-11-09; dated source qualifications apply.) The November capture supplies variant navigation; functional details remain attributed to earlier full captures.
- [[source-stripe-acss-custom-pad-agreement]] — Guide for businesses considering a custom Canadian PAD mandate agreement for ACSS. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-acss-debit]] — Stripe's Canadian pre-authorized debit (PAD/ACSS) guide covers CA/US business accounts taking bank debits from customers with Canadian accounts, in CAD or USD. (S02 reviewed update, 2026-11-09; dated source qualifications apply.)
- [[source-stripe-acss-set-up-payment]] — The retained 2026-05-02 guide explains saving Canadian pre-authorized debit (PAD/ACSS Debit) bank details for later payments through Checkout setup mode or the Direct API SetupIntent flow. (S02 reviewed update, 2026-11-09; dated source qualifications apply.) The November capture supplies variant navigation; functional details remain attributed to earlier full captures.

- [[source-stripe-au-becs-debit]] — Australia BECS Direct Debit is a reusable, delayed-notification, domestic AUD debit for an Australian business and a customer with an Australian bank account. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-au-becs-accept-payment]] — This Stripe integration guide covers accepting AU BECS Direct Debit payments through Checkout, web Elements with either the Checkout Sessions API or Payment Intents API, iOS, Android, and React Native. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-stripe-au-becs-set-up-payment]] — This Stripe guide covers using the Setup Intents API to save AU BECS Direct Debit details and a mandate for future payments. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-stripe-nz-becs-debit]] — New Zealand BECS Direct Debit. Compare dated mandate and notice requirements, delayed payment and settlement, and documented off-session scope.
- [[source-stripe-nz-becs-accept-payment]] — NZ BECS acceptance. See the dated PaymentIntent, mandate and scheduled-debit guidance and November implementation routes.
- [[source-stripe-nz-becs-set-up-payment]] — NZ BECS future-payment setup. See the dated SetupIntent and advance-notice guidance and the separate November product-matrix qualification.
- [[source-stripe-nz-becs-migrate-from-processor]] — NZ BECS migration from another processor. See the dated consent, notification, debit setup and stored payment-method guidance.
- [[source-stripe-bacs-direct-debit]] — Stripe Bacs Direct Debit is a reusable, delayed GBP debit from a customer's UK bank account, authorized by a Direct Debit Instruction (DDI) mandate. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-bacs-accept-payment]] — The May 2, 2026 full guide describes UK-bank-account Bacs Direct Debit payments in GBP through Checkout and web Elements with a PaymentIntent. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-stripe-bancontact]] — Stripe's Bancontact overview describes a single-use, customer-authenticated bank redirect for customers in Belgium paying in EUR with a Bancontact card or app linked to a Belgian bank account. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-bancontact-accept-payment]] — Bancontact is a single-use, customer-authenticated payment method in the detailed 2026-05-03 guide. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-stripe-bank-redirects]] — Stripe's bank-redirect overview compares product and API support by method. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-blik]] — The November 7, 2026 BLIK overview describes a Polish-customer, PLN bank-debit method in which a customer enters a six-digit bank-app code and approves a bank push notification. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-blik-accept-payment]] — The November 7, 2026 capture of this Stripe URL is a **variant index** for Checkout, Direct API, iOS and Android. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-stripe-blik-save-during-payment]] — The detailed 2026-05-03 guide shows how to save a BLIK PaymentMethod while processing a payment, so a later recurring off-session charge need not collect another BLIK code. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-stripe-blik-set-up-payment]] — The May 3, 2026 detailed guide describes saving a customer's BLIK PaymentMethod for recurring use through mandate authorization **without an initial payment**. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-stripe-eps]] — May/November 2026 EPS method overviews: Austrian EUR payments, eligibility, payment/refund timing, invoice-collection restrictions and captured support conflicts. (S03 reviewed update, 2026-11-15; dated qualifications apply.)
- [[source-stripe-eps-accept-payment]] — Stripe acceptance guide for EPS, an Austrian bank-redirect method. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-stripe-fpx]] — The November 7, 2026 FPX overview describes a single-use Malaysian bank redirect for MY customers and MYR domestic payments. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-fpx-accept-payment]] — The May 3, 2026 detailed guide describes FPX Checkout and a legacy Elements `fpxBank` integration, with a short Mobile Payment Element pointer. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-stripe-ideal]] — The May 3 and November 7, 2026 full captures describe iDEAL | Wero (formerly iDEAL) as a Netherlands-based, customer-initiated online bank payment method. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.)
- [[source-stripe-ideal-accept-payment]] — Stripe's archived iDEAL | Wero acceptance guide covers Checkout, iOS, Android, React Native, and web Elements. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-stripe-ideal-save-during-payment]] — The 2026-05-03 guide describes saving a customer's IBAN from an initial iDEAL | Wero payment as a generated SEPA Direct Debit PaymentMethod for later payments. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.
- [[source-stripe-ideal-set-up-payment]] — The detailed 2026-05-03 guide uses an iDEAL | Wero SetupIntent to collect a mandate and bank details for later SEPA Direct Debit. (S03 reviewed update, 2026-11-15; capture-dated qualifications apply.) November capture is variant navigation; detailed behavior remains dated to earlier full captures.

## [2026-11-08] Stripe S01 documentation curation

The approved S01 update revises 48 existing Billing/subscription source summaries and 31 existing concepts. Thirty-two November captures provide factual evidence; sixteen variant indexes remain navigation only while older functional guidance stays dated. No source pages were added. Start with [[stripe-subscriptions]], [[source-stripe-billing-apis]], [[source-stripe-subscriptions-migration-toolkit]], and [[stripe-usage-based-billing]].

## [2026-11-09] Stripe S02 documentation curation

The approved update revises 86 existing source summaries from 91 reviewed contributions and audits 29 existing concepts. New factual evidence and navigation-only captures stay distinct; historical raw references and dated qualifications remain. No source pages were added. See [[source-stripe-payment-links]], [[stripe-inapp-payments]], [[stripe-declines]] and [[stripe-crypto-onramp]].

## [2026-11-15] Stripe S03 documentation curation

The approved S03 update revises 98 existing source summaries from 97 raw contributions and audits 45 existing concepts. Fifty-four November captures provide factual evidence; 43 variant indexes remain navigation only while earlier functional guidance stays dated. No source pages were added and the recorded source count is unchanged. Start with [[stripe-bank-redirects]], [[stripe-bnpl]], [[stripe-checkout]], and [[stripe-customer-balance]].
