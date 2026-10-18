---
title: "GitHub: stripe/stripe-php"
type: source
date_ingested: 2026-08-15
date_updated: 2026-10-18
original_format: github-repo
raw_files:
  - "github/stripe/stripe-php/snapshots/2026-10-18-c4c1f65/manifest.json"
  - "github/stripe/stripe-php/snapshots/2026-10-18-0d8b075/manifest.json"
  - "github/stripe/stripe-php/snapshots/2026-10-18-1298699/manifest.json"
  - "github/stripe/stripe-php/snapshots/2026-10-18-fe99159/manifest.json"
  - "github/stripe/stripe-php/snapshots/2026-10-18-da798f6/manifest.json"
  - "github/stripe/stripe-php/snapshots/2026-08-15-edf8118/manifest.json"
tags: [stripe, stripe-php, php, server-sdk, checkout, payment-intents, subscriptions, webhooks, terminal, github-repository]
---

## Overview

`stripe/stripe-php` publishes the `stripe/stripe-php` Composer package, Stripe's server-side PHP SDK. This initial full ingest covers `stripe-php@21.2.0` at exact SHA `edf8118f0b96d69f06f372da9168d613d1aed072`, released on 2026-08-10.

Repository: <https://github.com/stripe/stripe-php>

## Evidence Boundary

**Latest routing:** the latest ingested full baseline is 22.0.0, API `2026-09-30.endive`, PHP7.4+. Sections describing the initial 21.2.0 capsule below are historical, not current defaults. Read the separately labeled version chapters and [[changelog-github-stripe-php]] for upgrades; all six retained release ingests occurred at their recorded dates.

- The retained repository proves PHP client behavior, generated resource models and services, request encoding, webhook helpers, and release history. It does not prove merchant eligibility, geographic availability, Dashboard configuration, or production enablement.
- This is a server SDK. Browser or native collection of customer payment details belongs to Stripe.js or Stripe's mobile SDKs.
- Generated objects and services follow the API version pinned by the package. Version-specific answers should identify both `stripe-php@21.2.0` and Stripe API `2026-07-29.dahlia`.
- The capsule is checkout-focused but broad: it retains 467 public source and history files. Tests are excluded. A rough query outside checkout can trigger a fresh clone and targeted source search.
- Methods whose names include `WithoutVerification` do not authenticate event payloads. Use them only after separate signature verification or with an explicitly trusted event source.

## Grounding Excerpts

> "The Stripe PHP library provides convenient access to the Stripe API from applications written in the PHP language."
>
> `raw/github/stripe/stripe-php/snapshots/2026-08-15-edf8118/files/README.md:11-12`

> "PHP 7.2.0 and later."
>
> `raw/github/stripe/stripe-php/snapshots/2026-08-15-edf8118/files/README.md:17-19`

> "We recommend that you create exactly one PaymentIntent for each order or customer session in your system."
>
> `raw/github/stripe/stripe-php/snapshots/2026-08-15-edf8118/files/lib/PaymentIntent.php:8-11`

> "Idempotency keys are added to requests to guarantee that retries are safe."
>
> `raw/github/stripe/stripe-php/snapshots/2026-08-15-edf8118/files/README.md:187-195`

> "Should be used after calling WebhookSignature::verifyHeader() or with input from a trusted source."
>
> `raw/github/stripe/stripe-php/snapshots/2026-08-15-edf8118/files/lib/Webhook.php:36-39`

## Package Status

| Package | Latest ingested release | Pinned API | PHP support | Evidence status |
| --- | --- | --- | --- | --- |
| `stripe/stripe-php` | `22.0.0` | `2026-09-30.endive` | PHP 7.4+ | Approved full; all v21 history retained |

This table reports wiki ingest progress, not the latest release currently published upstream.

## Installation and Client Shape

Install with `composer require stripe/stripe-php`. Composer maps the `Stripe\` namespace to `lib/`; projects without Composer can load `init.php`. The package requires PHP 7.2+, `ext-curl`, `ext-json`, and `ext-mbstring`.

The recommended service pattern constructs `StripeClient` with a secret key and calls nested services such as `paymentIntents`, `setupIntents`, `checkout->sessions`, `paymentLinks`, `subscriptions`, `subscriptionSchedules`, and `terminal->readers`. Legacy static resource methods remain available, so old and new integration styles can coexist in a migration.

Client configuration covers API key, application identity, Connect account, Stripe context, API version, retry count, telemetry, and API, files, OAuth, and meter endpoint bases. API key, connected account, and API version can also be overridden per request.

## Requests, Encoding, and Errors

V1 requests use form encoding; V2 requests use JSON. Null is therefore not interchangeable across modes: V1's encoder represents a null field as an empty string while V2 sends JSON `null`. File operations use multipart encoding.

`ApiRequestor` builds headers, dispatches through `CurlClient`, decodes responses, and maps failures by HTTP status and Stripe error type. The exception hierarchy includes authentication, invalid request, card, rate-limit, permission, idempotency, signature-verification, connection, OAuth, temporary-session, and unknown API errors.

`rawRequest()` is available from SDK v16 for APIs not yet represented by generated services, including preview endpoints. It bypasses method definitions but not the need to authenticate, select an API version, parse the response deliberately, and verify feature access.

## Retries, Idempotency, and Telemetry

Automatic network retries are opt-in through `setMaxNetworkRetries()` or client configuration. Retryable requests receive idempotency keys so a transport retry does not intentionally duplicate an operation. A local timeout does not prove Stripe stopped processing the request, so low timeouts on mutations require stable idempotency handling and reconciliation.

The library sends request-latency and feature-use telemetry by default. `Stripe::setEnableTelemetry(false)` disables it.

## Webhooks and Event Destinations

`Webhook::constructEvent()` verifies a V1 snapshot payload before constructing an `Event`; its default timestamp tolerance is 300 seconds. `WebhookSignature` verifies the exact payload and `Stripe-Signature` header.

Stripe PHP 21.2.0 adds unverified construction and parsing helpers for payloads already verified before queueing or delivered by trusted cloud event destinations. It also adds signature-header generation for tests. These helpers must not replace verification for an ordinary public webhook endpoint.

V2 `EventNotification` objects represent thin event payloads and can fetch the full event or related object through the client. Event destinations can deliver snapshot or thin payloads, so handlers must distinguish the two contracts instead of assuming every event embeds a complete resource.

## Checkout and Payment APIs

### PaymentIntents and SetupIntents

A PaymentIntent tracks one order or customer session through payment attempts and produces at most one successful charge. Services support create, retrieve, update, list, confirm, capture, cancel, search, incremental authorization, customer-balance application, and microdeposit verification. `setup_future_usage` signals later reuse, but its allowed values and recurring suitability remain payment-method-specific.

SetupIntents collect and authenticate a payment method without charging it. Payment method configurations and payment method domains control eligible methods and domain registration; their presence in the SDK does not establish merchant enablement.

### Checkout Sessions and Payment Links

Checkout Sessions support payment, setup, and subscription modes and hosted, embedded, custom/elements, and form UI modes in the retained generated model. A Session coordinates its PaymentIntent or Subscription and the customer-facing checkout lifecycle. Payment Links create reusable hosted checkout entrypoints backed by Checkout Sessions.

### Charges and Payment Records

The retained Charge model documents direct charges as a legacy path and recommends PaymentIntents for new integrations. Payment Records and Payment Attempt Records provide a separate on- and off-Stripe processing record model; their generated presence does not imply that every account has product access.

## Billing and Subscription Semantics

Products and Prices define what is sold; subscriptions, invoices, invoice payments, quotes, plans, and schedules model recurring and invoiced billing. Subscription schedules apply phased changes rather than replacing historical subscription evidence.

`pause_collection` is not the same as a subscription whose status is `paused`: pause collection changes invoice handling while the subscription status remains otherwise active. Subscription updates expose `proration_behavior` values such as `always_invoice`, `create_prorations`, and `none`; callers must choose the intended billing result rather than assume every update immediately invoices a proration.

## Terminal Surface

The server SDK exposes Terminal locations, configurations, connection tokens, readers, and server-driven reader actions. Reader operations can collect and confirm PaymentIntents, collect SetupIntents, process payments, and initiate refunds. Reader `status` is observational and must not be used as the sole blocking signal for payment fulfillment; final payment state remains authoritative.

## Version History Boundaries

- v7.33 introduced the client-and-services pattern that coexists with legacy resource methods.
- v11 is explicitly discouraged in upstream history.
- v12 began pinning the API version sent by the SDK rather than inheriting the account default implicitly.
- v16 introduced `rawRequest()`.
- v20 dropped PHP versions below 7.2 and pins `2026-03-25.dahlia`.
- v21.0 is a major nullability annotation change without a stated runtime behavior change.
- v21.1 pins API `2026-07-29.dahlia`.
- v21.2 adds event-notification object exposure, pre-verified event parsers, signature generation, and a major API version constant.

These are retained historical landmarks, not a substitute for a release-by-release migration review.

## 21.2.1 Delta: Agent Hint Initialization

Approved delta at SHA `da798f6224c5ff6f89d8d78025044f418ee27db8`, released 2026-08-20, ingested 2026-10-18. Current changed runtime, README/package/init and deleted prior helper read fully; unchanged generated inventories/history checked mechanically under the explicit five-release focused-reading approval. Both 467-file snapshots hash/size verified: one added, seven modified, one removed, 459 unchanged; all ten upstream changes classified, no gaps.

Composer and manual init stop executing the old `lib/agent_plugin_hint.php` at load time. A new utility is called from `BaseStripeClient` construction and `ApiRequestor::_prepareRequest`. It only emits under CLI, nonempty `CLAUDECODE`, and no already-loaded PHPUnit test class. `CLAUDE_CODE_CHILD_SESSION` alone is no longer sufficient. The static flag is set before these checks: this is one attempt per process, not a promise to emit whenever the environment later becomes eligible. Exceptions are caught. The patch does not suppress all SDK warnings or alter the pinned payment API.

**Grounding** (`files/lib/Util/AgentPluginHint.php`): line 28 `self::$emitted = true;`; line 49 ``if ('' === (string) \getenv('CLAUDECODE')) {``; line 55 ``if (\class_exists('PHPUnit\Framework\TestCase', false)) {``; line 61 ``return 'cli' === \PHP_SAPI;``. The tests themselves are excluded; no PHP/SDK execution is claimed. No cross-company comparison or new contradiction warranted.

**Evidence:** [Snapshot](../../../../raw/github/stripe/stripe-php/snapshots/2026-10-18-da798f6/manifest.json), [release](../../../../raw/github/stripe/stripe-php/releases/stripe-php/21.2.1/2026-10-18/manifest.json), [notes](../../../../raw/github/stripe/stripe-php/releases/stripe-php/21.2.1/2026-10-18/release-notes.md), [comparison](../../../../tracking/github/repos/stripe/stripe-php/comparisons/stripe-php/21.2.0--21.2.1/comparison.json), [hint utility](../../../../raw/github/stripe/stripe-php/snapshots/2026-10-18-da798f6/files/lib/Util/AgentPluginHint.php), [client](../../../../raw/github/stripe/stripe-php/snapshots/2026-10-18-da798f6/files/lib/BaseStripeClient.php), [requestor](../../../../raw/github/stripe/stripe-php/snapshots/2026-10-18-da798f6/files/lib/ApiRequestor.php).

## 21.3.0 Full Ingest: Thin Handlers and V2 Encoding

SHA `fe99159b9ee0a74be3c12c0305e5338e0b9905c3`; upstream changelog date 2026-08-26, GitHub publication 2026-08-27; ingested 2026-10-18 in user-approved **full** mode despite the packet's delta recommendation. Focused reading covers new/changed runtime, affected prior code, new resource/service and changed generated contract sections; unchanged generated files, historical changelog and inventories checked mechanically. Both snapshots hash/size verified: 473 current files, 430 unchanged. No gaps/unclassified changes. Full ingest adds this baseline and does not replace 21.2.x knowledge.

### Runtime and Migration

- API pin is `2026-08-26.dahlia`, PHP floor remains 7.2. Client/services, retries, V1 form/V2 JSON encoding and public-webhook verification remain baseline integration responsibilities.
- `StripeClient::notificationHandler($secret, $fallback)` creates a verified thin-event handler; its `handle($payload, $signature)` verifies before dispatch. The sibling without-verification handler accepts only payload and is reserved for authenticated channels. Register typed callbacks before handling starts; duplicates and registration after the first handle attempt throw. `preHandle` can deduplicate using application storage but the SDK itself does not persist delivery IDs. Any falsy hook return stops typed and fallback callbacks.
- Unknown event types invoke fallback, with `UnhandledNotificationDetails::$isKnownEventType` distinguishing unknown from known-but-unregistered types. Callback clients are reconstructed rather than mutating the shared client. In this version, reconstruction retains the original `stripe_account` while assigning event `stripe_context`; do not assume later context-isolation fixes already exist here. The notification's own fetch helpers separately attach its context and event-trigger header.
- `Util\Int64` adds nullable/discriminated-union recursion and uses array schema `element` instead of the prior `items`. Outbound ints/decimals convert to strings where the schema requires; missing or non-string discriminators throw `InvalidArgumentException`, while unknown string variants pass through. Inbound numeric int64 strings become ints; the implementation does not add an inbound decimal-to-float conversion. Test large integer/platform-width and polymorphic request cases in the consuming application.

### Checkout and Billing Contracts

New `billing->feedbackOptions` operations support custom cancellation reasons; deactivation prevents reuse in portal configurations. Portal configurations accept `feedback_options`; subscriptions expose `cancellation_details.feedback_option`; the portal response flow adds `customer_update`. Checkout card restrictions add `funding_types_blocked`. Customer Sessions add `active_entitlements`/`customer_portal`; ConfirmationToken exposes metadata; Financial Connections filters add country. Invoice/subscription payment settings expose Billie. Payment Link update definitions add application fees, `on_behalf_of` and `transfer_data`.

Payment-record 3DS `cryptogram` is removed from generated annotations, not evidence that every card cryptogram field disappears. Release notes also describe `allowed_payment_method_types` changes on PaymentIntent/SetupIntent; those files are unchanged in the retained PHP diff, so do not reinterpret that release-note phrase as a new mandatory create-request field. Tax/Climate/Treasury and other generated changes remain available for a version-qualified deep dive; SDK declarations alone do not prove product availability.

### Grounding and Evidence

Four exact runtime excerpts: `files/lib/Util/Int64.php:64` ``if (!\is_string($discriminatorValue)) {``; line 83 ``if ('array' === $schema['kind'] && isset($schema['element'])) {``; `files/lib/AbstractEventNotificationHandler.php:101` `$config['stripe_context'] = $context;`; `files/lib/BaseStripeClient.php:570` `public function notificationHandler($webhookSecret, $fallbackCallback)`.

[Snapshot](../../../../raw/github/stripe/stripe-php/snapshots/2026-10-18-fe99159/manifest.json), [release](../../../../raw/github/stripe/stripe-php/releases/stripe-php/21.3.0/2026-10-18/manifest.json), [notes](../../../../raw/github/stripe/stripe-php/releases/stripe-php/21.3.0/2026-10-18/release-notes.md), [comparison](../../../../tracking/github/repos/stripe/stripe-php/comparisons/stripe-php/21.2.1--21.3.0/comparison.json), [handler](../../../../raw/github/stripe/stripe-php/snapshots/2026-10-18-fe99159/files/lib/AbstractEventNotificationHandler.php), [coercion](../../../../raw/github/stripe/stripe-php/snapshots/2026-10-18-fe99159/files/lib/Util/Int64.php), [feedback service](../../../../raw/github/stripe/stripe-php/snapshots/2026-10-18-fe99159/files/lib/Service/Billing/FeedbackOptionService.php), [Payment Link](../../../../raw/github/stripe/stripe-php/snapshots/2026-10-18-fe99159/files/lib/PaymentLink.php). Examples/tests excluded by policy; no SDK execution claimed. No new cross-company comparison or contradiction required: annotations/release notes are scoped explicitly above.

## 21.3.1 Delta: Request Path and Header Hardening

SHA `12986995cd5e229cc094d4b57de056f8e2e6e5a9`, released 2026-09-01, ingested 2026-10-18. Approved delta/focused reading; current requestor and changed event retrieval plus affected prior code reviewed; unchanged generated files/history/inventories verified mechanically. Both 473-file snapshots hash/size verified; four changed, 469 unchanged; nine upstream changes classified, no gaps. API/PHP floors unchanged.

`ApiRequestor::validatePath()` requires a string beginning with one `/` (not `//`); failed `parse_url` or any scheme/host/user component throws before API-base concatenation. `assertNoHeaderInjection()` rejects CR, LF or NUL in string header names/values before header serialization. Both normal and streaming request preparation pass these checks. `EventNotification::fetchEvent()` URL-encodes its body-derived ID rather than interpolating path/query delimiters. These are specific credential-routing/header protections, not an API-base allowlist, full URL canonicalizer or replacement for authenticating public webhooks. Review custom raw-request paths for the required leading slash when upgrading.

**Grounding:** `files/lib/ApiRequestor.php:500` `Request path must be a string beginning with a single "/".`; line 507 `Request path may not contain a scheme or authority.`; line 536 `Header names and values may not contain CR, LF or NUL characters.` Exact message strings are inside thrown `InvalidArgumentException` constructors. Event retrieval: [current code](../../../../raw/github/stripe/stripe-php/snapshots/2026-10-18-1298699/files/lib/V2/Core/EventNotification.php).

[Snapshot](../../../../raw/github/stripe/stripe-php/snapshots/2026-10-18-1298699/manifest.json), [release](../../../../raw/github/stripe/stripe-php/releases/stripe-php/21.3.1/2026-10-18/manifest.json), [notes](../../../../raw/github/stripe/stripe-php/releases/stripe-php/21.3.1/2026-10-18/release-notes.md), [comparison](../../../../tracking/github/repos/stripe/stripe-php/comparisons/stripe-php/21.3.0--21.3.1/comparison.json), [requestor](../../../../raw/github/stripe/stripe-php/snapshots/2026-10-18-1298699/files/lib/ApiRequestor.php). No tests collected/executed; no new contradiction or cross-company comparison. All historical chapters retained.

## 21.3.2 Delta: Empty Webhook Secret Rejection

SHA `0d8b075e1a97d15c5324353a5277d0ea686ea525`, released 2026-09-09, ingested 2026-10-18. Approved focused-reading delta: current verifier and affected prior implementation reviewed, inventories/unchanged generated files and history mechanically verified. Both 473-file snapshots hash/size checked; three changed, 470 unchanged; seven upstream changes classified without gaps. API `2026-08-26.dahlia` and PHP7.2 floor remain.

`WebhookSignature::verifyHeader()` now rejects `empty($secret)` with `SignatureVerificationException`, after parsing the timestamp and finding a v1 signature but before computing the expected HMAC. This includes PHP-empty values such as `"0"`; it does not trim a whitespace-only string or enforce a `whsec_` prefix despite recommending that prefix in the message. Validating deployment configuration remains necessary. The existing signature comparison and timestamp rules are unchanged. Null/zero tolerance skips the timestamp check in the low-level verifier; `Webhook::constructEvent()` and normal thin parsers use the 300-second default. The signature-generation helper is not given this new guard. Unverified parsers remain explicitly unverified.

**Grounding** (`files/lib/WebhookSignature.php`): line 45 `if (empty($secret)) {`; line 47, exact string content: "No webhook secret value was provided. It should start with `whsec_`"; line 74 ``if (($tolerance > 0) && (\abs(\time() - $timestamp) > $tolerance)) {``. No new general prefix validator is inferred from message wording.

[Snapshot](../../../../raw/github/stripe/stripe-php/snapshots/2026-10-18-0d8b075/manifest.json), [release](../../../../raw/github/stripe/stripe-php/releases/stripe-php/21.3.2/2026-10-18/manifest.json), [notes](../../../../raw/github/stripe/stripe-php/releases/stripe-php/21.3.2/2026-10-18/release-notes.md), [comparison](../../../../tracking/github/repos/stripe/stripe-php/comparisons/stripe-php/21.3.1--21.3.2/comparison.json), [verifier](../../../../raw/github/stripe/stripe-php/snapshots/2026-10-18-0d8b075/files/lib/WebhookSignature.php). All older history retained; no SDK execution, new contradiction or cross-company comparison.

## 22.0.0 Full Ingest: Endive and PHP7.4

SHA `c4c1f658483e717519935222e47af224ef4a508b`; exact-SHA changelog date 2026-09-30, GitHub publication 2026-10-01; ingested 2026-10-18. Approved **full** mode with the five-release focused-reading exception: runtime changes, affected prior code and changed checkout/Billing/generated API sections reviewed; unchanged generated files, inventories, repeated mappings and duplicated diff checked mechanically. The release-note file only links mutable `master`; this chapter uses the retained SHA's changelog instead.

Both snapshots hash/size verified: 916 current files, 443 added/172 modified/301 unchanged, no removals. All 1,488 upstream changes have dispositions, with no evidence gaps or unclassified changes. The 432 added `lib/Events` files are typed full-event/notification classes, not 432 new payment products. The broader capsule budget preserves checkout and non-checkout raw evidence; it does not turn non-checkout navigation into a fully analyzed product guide. No tests, builds or provider payments executed. All v21 chapters and raw snapshots remain intact.

### Runtime and Event Handling

- Composer and `lib/version_check.php` require PHP7.4; PHP7.2/7.3 support is removed. `ApiVersion::CURRENT` is `2026-09-30.endive`, `CURRENT_MAJOR` is `endive`. Curl/JSON/mbstring extension requirements remain. Review the API migration separately from the runtime upgrade.
- Expanded union PHPDoc now describes complete array/object/list shapes. This can produce new static-analysis/IDE diagnostics; it is not runtime validation of every documented shape. V1 form/V2 JSON modes, explicit retry/idempotency decisions and the 21.3.x security guards remain applicable.
- `AbstractEventNotificationHandler::createClientWithContext()` now sets the captured config's `stripe_account` to null before assigning event `stripe_context`. It reconstructs a new client using captured API key/version, app/client identity, endpoints and retry settings without mutating the original. This fixes the prior inherited-account boundary, including when the event context is null; it is not a blanket clone of every mutable global or per-request setting.
- `EventNotification::RELATED_OBJECT_CLASS` enables late-bound singleton deserialization. Singleton notifications use `RelatedSingletonObject` containing type and URL, not a required ID; null related-object payloads are skipped. Typed Checkout Session, PaymentIntent and subscription lifecycle notifications extend registration/fetch surfaces. Fetching the full event or related resource performs API requests; typed events are not proof that the resource is already embedded, that delivery is unique, or that payment succeeded.
- Notice suppression uses case-insensitive exact `true` in `STRIPE_SUPPRESS_NOTICES` and requires no detected AI agent. Whitespace is not trimmed; detected-agent notices remain enabled. README guidance describes test/sandbox use, but the local suppression branch does not inspect API-key mode. It suppresses Stripe-Notice warnings, not every SDK warning and not the independent plugin hint.

### Request Contract Changes

| Surface | Endive definition | Migration boundary |
| --- | --- | --- |
| Checkout Session create | `allowed_payment_method_types` added; `payment_method_types` removed | Review dynamic-method filtering semantics rather than mechanically rename every field |
| PaymentIntent create/update/confirm | `payment_method_types` removed; `allowed_payment_method_types` retained | The allowed field already existed in the preceding snapshot |
| SetupIntent create/update | `payment_method_types` removed; allowed field retained | Confirm already used the allowed field in the prior snapshot |
| Payment Links create/update | `payment_method_types` retained | No global deletion/rename; Billing payment-setting/response fields remain separately versioned |
| Financial Connections Session filters | `countries` removed; singular `country` used | Audit plural filters in consuming requests |
| Subscription update/resume | `billing_cycle_anchor` is an array with `type` | Invoice preview also permits a timestamp field |

Checkout's shipping-permission comment now refers to `ui_mode=elements` rather than `custom`. New PayPay/SeQura shapes, BLIK mandate/off-session options, expandable card mandates/ECI, Billie company details, PaymentIntent payment records and inline product `tax_details` expand annotations. These are SDK contracts, not merchant access or geographic availability guarantees. PaymentMethod update removes PayTo parameters specifically; it does not remove PayTo from the entire SDK. Legacy Charge create/capture comments now explicitly deprecate those paths; prefer PaymentIntents, without claiming their methods have already been deleted.

### Subscription Lifecycle

`$stripe->subscriptions->pause($id, $params)` POSTs to `/v1/subscriptions/{id}/pause`. The comment describes true paused status: no invoices or advancement to new periods, resumable later, but no attached schedule. This is distinct from `pause_collection`. SubscriptionSchedule adds a separate `pause_schedules` request/response surface with pause/resume timing, settings and statuses. Subscription items add `current_trial`; invoice/subscription responses add `status_details`; resume adds `payment_behavior`; trial-end behavior adds a billing anchor and makes the missing-payment-method request setting optional.

> [!warning] Contradiction
> `lib/Subscription.php:54` still says paused status can only follow a trial without a payment method, while `lib/Service/SubscriptionService.php:123-138` describes and implements an explicit pause operation. Keep the historical comment as versioned evidence, not an exhaustive eligibility rule. Product prerequisites still require product documentation. Reciprocal warning: [[stripe-subscriptions]].

Non-checkout resource additions (`Apps.Install`, `ProductCatalog.TrialOffer`, `Tax.Location`, `ThreeDSecure.Authentication`) and broader Tax/Reserve/Treasury changes remain discoverable in the immutable capsule and exact-SHA changelog. Their existence here is navigation, not a detailed integration or availability claim. A detailed future query must read the relevant retained implementation, or collect an approved exact-SHA supplement if evidence is missing.

### Grounding and Evidence

Five exact excerpts under this snapshot: `files/composer.json:18` `"php": ">=7.4.0",`; `files/lib/Util/ApiVersion.php:9` `const CURRENT = '2026-09-30.endive';`; `files/lib/AbstractEventNotificationHandler.php:101` `$config['stripe_account'] = null;`; `files/lib/ApiRequestor.php:648` `$suppressionValue = $getEnv('STRIPE_SUPPRESS_NOTICES');`; `files/lib/Service/SubscriptionService.php:136` `public function pause($id, $params = null, $opts = null)`.

[Snapshot](../../../../raw/github/stripe/stripe-php/snapshots/2026-10-18-c4c1f65/manifest.json), [release](../../../../raw/github/stripe/stripe-php/releases/stripe-php/22.0.0/2026-10-18/manifest.json), [exact-SHA changelog](../../../../raw/github/stripe/stripe-php/snapshots/2026-10-18-c4c1f65/files/CHANGELOG.md), [comparison](../../../../tracking/github/repos/stripe/stripe-php/comparisons/stripe-php/21.3.2--22.0.0/comparison.json), [requestor](../../../../raw/github/stripe/stripe-php/snapshots/2026-10-18-c4c1f65/files/lib/ApiRequestor.php), [callback handler](../../../../raw/github/stripe/stripe-php/snapshots/2026-10-18-c4c1f65/files/lib/AbstractEventNotificationHandler.php), [notification runtime](../../../../raw/github/stripe/stripe-php/snapshots/2026-10-18-c4c1f65/files/lib/V2/Core/EventNotification.php), [singleton](../../../../raw/github/stripe/stripe-php/snapshots/2026-10-18-c4c1f65/files/lib/RelatedSingletonObject.php), [Checkout service](../../../../raw/github/stripe/stripe-php/snapshots/2026-10-18-c4c1f65/files/lib/Service/Checkout/SessionService.php), [PaymentIntent service](../../../../raw/github/stripe/stripe-php/snapshots/2026-10-18-c4c1f65/files/lib/Service/PaymentIntentService.php), [SetupIntent service](../../../../raw/github/stripe/stripe-php/snapshots/2026-10-18-c4c1f65/files/lib/Service/SetupIntentService.php), [subscription service](../../../../raw/github/stripe/stripe-php/snapshots/2026-10-18-c4c1f65/files/lib/Service/SubscriptionService.php), [schedule](../../../../raw/github/stripe/stripe-php/snapshots/2026-10-18-c4c1f65/files/lib/SubscriptionSchedule.php), [typed Checkout notification](../../../../raw/github/stripe/stripe-php/snapshots/2026-10-18-c4c1f65/files/lib/Events/V1CheckoutSessionCompletedEventNotification.php). No new cross-company comparison is warranted.

## Related

- Company: [[stripe]]
- Concepts: [[stripe-php-sdk]], [[stripe-payment-intents]], [[stripe-checkout]], [[stripe-payment-links]]
- Parallel server SDK: [[source-github-stripe-node]]
- History: [[changelog-github-stripe-php]]

## Raw Sources

- [22.0.0 snapshot](../../../../raw/github/stripe/stripe-php/snapshots/2026-10-18-c4c1f65/manifest.json) - approved focused-reading full Endive ingest; exact runtime/contracts above

- [21.3.2 snapshot](../../../../raw/github/stripe/stripe-php/snapshots/2026-10-18-0d8b075/manifest.json) - focused-reading webhook-secret delta; implementation above

- [21.3.1 snapshot](../../../../raw/github/stripe/stripe-php/snapshots/2026-10-18-1298699/manifest.json) - focused-reading security delta; exact runtime evidence above

- [21.3.0 snapshot](../../../../raw/github/stripe/stripe-php/snapshots/2026-10-18-fe99159/manifest.json) - approved focused-reading full ingest; version-qualified evidence links above

- [21.2.1 snapshot](../../../../raw/github/stripe/stripe-php/snapshots/2026-10-18-da798f6/manifest.json) - changed runtime fully read, unchanged inventory verified under approval; implementation/release/comparison links in its chapter

- [Snapshot manifest](../../../../raw/github/stripe/stripe-php/snapshots/2026-08-15-edf8118/manifest.json) - exact-SHA source capsule and file hashes
- [Release manifest](../../../../raw/github/stripe/stripe-php/releases/stripe-php/21.2.0/2026-08-15/manifest.json) - package-qualified release record
- [Release notes](../../../../raw/github/stripe/stripe-php/releases/stripe-php/21.2.0/2026-08-15/release-notes.md) - exact 21.2.0 notes
- [README](../../../../raw/github/stripe/stripe-php/snapshots/2026-08-15-edf8118/files/README.md) - installation, support, retries, telemetry, and custom requests
- [Repository changelog](../../../../raw/github/stripe/stripe-php/snapshots/2026-08-15-edf8118/files/CHANGELOG.md) - complete upstream package history
- [Stripe client](../../../../raw/github/stripe/stripe-php/snapshots/2026-08-15-edf8118/files/lib/StripeClient.php) - generated service surface
- [API requestor](../../../../raw/github/stripe/stripe-php/snapshots/2026-08-15-edf8118/files/lib/ApiRequestor.php) - request construction, headers, responses, and errors
- [Curl client](../../../../raw/github/stripe/stripe-php/snapshots/2026-08-15-edf8118/files/lib/HttpClient/CurlClient.php) - transport, timeouts, retries, and telemetry
- [Webhook](../../../../raw/github/stripe/stripe-php/snapshots/2026-08-15-edf8118/files/lib/Webhook.php) - verified and pre-verified V1 event construction
- [PaymentIntent](../../../../raw/github/stripe/stripe-php/snapshots/2026-08-15-edf8118/files/lib/PaymentIntent.php) - payment lifecycle contract
- [Checkout Session](../../../../raw/github/stripe/stripe-php/snapshots/2026-08-15-edf8118/files/lib/Checkout/Session.php) - Checkout modes and associated objects
- [Subscription](../../../../raw/github/stripe/stripe-php/snapshots/2026-08-15-edf8118/files/lib/Subscription.php) - status, pause, and update semantics
