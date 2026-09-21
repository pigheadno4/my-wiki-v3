---
title: "GitHub changelog: stripe/stripe-node"
type: source
date_ingested: 2026-08-08
date_updated: 2026-09-21
original_format: github-repo
raw_files:
  - "github/stripe/stripe-node/snapshots/2026-09-21-d9d0927/manifest.json"
  - "github/stripe/stripe-node/snapshots/2026-09-21-9f82c46/manifest.json"
  - "github/stripe/stripe-node/snapshots/2026-09-21-2f64e7a/manifest.json"
  - "github/stripe/stripe-node/supplements/2026-09-21-2f64e7a-f49df03e/manifest.json"
  - "github/stripe/stripe-node/snapshots/2026-09-21-65d99a2/manifest.json"
  - "github/stripe/stripe-node/snapshots/2026-08-08-57626dc/manifest.json"
tags: [stripe, stripe-node, node-js, changelog, github-repository]
---

## Overview

Package-qualified retained release history for `stripe/stripe-node`. Cumulative implementation knowledge belongs in [[source-github-stripe-node]].

## `stripe@22.6.2` - Change Set `d9d0927` (2026-09-09)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `stripe` | `22.6.1` | `22.6.2` | `d9d092737b4a891f0beaf47c26c222972a4c7b0f` | Delta; approved focused reading |

**Change:** Both signature verification methods explicitly reject falsy secrets before HMAC computation, after payload/header parsing. Empty/null/undefined values produce StripeSignatureVerificationError when the guard is reached. The message mentions `whsec_`, but prefix and whitespace-only validation are not implemented by this guard. WithoutVerification and tolerance behavior remain unchanged.

**Developer impact:** Configure the endpoint's signing secret explicitly. Examples no longer fall back silently to empty strings: Express/Koa/snippet exit, NestJS throws, Next.js Pages returns 500 and App Router returns 400 through its catch. These are example-specific behaviors. Earlier parser/context caveats remain; no new checkout fields, API pin, exports or dependencies.

**Reading/validation boundary:** Eleven modified and 57 unchanged retained files. Both 68-file snapshots hash/size checked; historical changelog unchanged. Webhooks and six changed retained examples read fully, full diff reviewed, version-only core/package changes mechanically checked under the explicit exception. No SDK or upstream tests executed. Prior source/changelog history retained, existing concept updated first, company/index/logs updated; no source count change or cross-company comparison.

**Evidence:** [Release](../../../../raw/github/stripe/stripe-node/releases/stripe/22.6.2/2026-09-21/manifest.json), [notes](../../../../raw/github/stripe/stripe-node/releases/stripe/22.6.2/2026-09-21/release-notes.md), [snapshot](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-d9d0927/manifest.json), [comparison](../../../../tracking/github/repos/stripe/stripe-node/comparisons/stripe/22.6.1--22.6.2/comparison.json), [diff](../../../../tracking/github/repos/stripe/stripe-node/comparisons/stripe/22.6.1--22.6.2/diff.patch), [review](../../../../tracking/github/repos/stripe/stripe-node/ingest-review-c5fa7a03.md). Implementation/example links: [[source-github-stripe-node]].

## `stripe@22.6.1` - Change Set `9f82c46` (2026-09-01)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `stripe` | `22.6.0` | `22.6.1` | 2026-09-01 | `9f82c466c0a5913906ab1bf39790edd4d231ee5d` | Delta; approved focused reading |

**Important changes:** Cryptographically secure multipart boundaries; CR/LF replacement in file MIME Content-Type; shared request-path validation; encoded thin-event fetch IDs; schema coercion for GET/DELETE query parameters. Open-enum documentation clarifies existing OtherString behavior. API pin `2026-08-26.dahlia`, OpenAPI `v2442`, generated checkout files and runtime dependencies unchanged.

**Developer impact:** Upload generation fails without secure UUID support; Node uses imported crypto.randomUUID. Automatic idempotency keys alone keep a weaker fallback. Name/filename escaping already existed and must not be reported as new. Paths must be strings beginning with a single slash; this is not general URL validation or webhook authentication. Schema-marked Decimal/int64 query values are coerced before serialization; GET/DELETE bodies stay null. rawRequest still does not accept nonempty non-POST params.

**Migration and limits:** Check custom runtimes' secure randomness and callers supplying request paths. Preserve explicit business-operation idempotency and webhook verification. Existing notification-handler context, parser-entrypoint and retry-default caveats are not resolved here. CI action pinning/security checks are maintenance-only. No SDK build, upstream test execution or live integration verification.

**Reading boundary:** Both 68-file snapshots hash/size verified; 13 modified and 55 unchanged. Changed retained implementation and complete 1,093-line diff read. Unchanged historical changelog and manifest inventories mechanically verified under this release's explicit exception. Earlier ingested history preserved.

**Updated sections:** Stripe Node concept first; cumulative source, this changelog, company/provider catalog and logs. No new source or cross-company comparison; source count unchanged.

**Evidence:** [Release](../../../../raw/github/stripe/stripe-node/releases/stripe/22.6.1/2026-09-21/manifest.json), [notes](../../../../raw/github/stripe/stripe-node/releases/stripe/22.6.1/2026-09-21/release-notes.md), [snapshot](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-9f82c46/manifest.json), [comparison](../../../../tracking/github/repos/stripe/stripe-node/comparisons/stripe/22.6.0--22.6.1/comparison.json), [diff](../../../../tracking/github/repos/stripe/stripe-node/comparisons/stripe/22.6.0--22.6.1/diff.patch), [review receipt](../../../../tracking/github/repos/stripe/stripe-node/ingest-review-2402efbb.md). Exact implementation links in [[source-github-stripe-node]].

## `stripe@22.6.0` - Change Set `2f64e7a` (2026-08-26)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `stripe` | `22.5.0` | `22.6.0` | Changelog 2026-08-26; GitHub 2026-08-27 UTC | `2f64e7ac920bd6863fdb851f4fb1fcc6190d963f` | Full; user-approved focused reading |

**Important changes:** API pin `2026-08-26.dahlia`, OpenAPI `v2442`; typed thin-notification handlers; V2 discriminated-union coercion; response-body timeout/failure handling; automatic V1 POST idempotency even with zero configured retries; Checkout funding-type restrictions; Payment Links update-time Connect fields; required-but-nullable PaymentIntent/SetupIntent response allowlists; Billie/cancellation feedback typing. Broader `OtherString` enum changes coexist with removal of `OtherString` from WebhookEndpoint create/update enabled-events types.

**Developer impact:** Register handlers before first use, including before a failing parse; authenticate public webhook ingress; implement durable, failure-aware deduplication and HTTP acknowledgement yourself. Verified handler uses synchronous crypto. Request discriminators must be strings for non-null polymorphic objects; unknown strings still pass through. Recheck typed mocks and exhaustive switches. No new merchant eligibility is inferred from generated types.

**Implementation caveats:** Callback client is shallow-copied, leaving resource/RequestSender bindings on the original client; implicit event-context routing is a source-level risk, not runtime-tested. Event fetch helpers explicitly pass context. Body timeouts become StripeConnectionError; other body-read failures and malformed JSON remain StripeAPIError. Body failures do not enter a new automatic retry loop. Fetch timer is released on streaming handoff; Node stream timeout error shape changes. The diff-only sample's early Set insertion can suppress failed-event retries and its HTTP handlers omit a response.

**Migration:** Prefer `stripe.webhooks.constructEventWithoutVerification` over the now-deprecated client alias. Use explicit per-request context when needed and stable application-operation idempotency keys across separate calls. PaymentIntent/SetupIntent request allowlists remain optional: the newly required fields are response fields. Preserve all 22.1.1/22.4.0/22.5.0 history and historical parser/entrypoint caveats.

**Reading boundary:** 68 retained files, 33 modified/35 unchanged; both snapshot inventories/hashes and unchanged historical changelog verified mechanically. Changed behavior, relevant prior diff context and dependencies reviewed under the explicit exception; two supplemental files read fully. Excluded non-checkout areas are release-note overview only. No full-repository read, SDK execution, upstream test run or live payment proof.

**Updated sections:** Source package/evidence status, retries, new 22.6.0 handler/transport/coercion/API sections, retained history; Stripe Node, Payment Intents and Checkout concepts; company/provider index and logs. Source count unchanged.

**Evidence:**

- [Release manifest](../../../../raw/github/stripe/stripe-node/releases/stripe/22.6.0/2026-09-21/manifest.json), [release notes](../../../../raw/github/stripe/stripe-node/releases/stripe/22.6.0/2026-09-21/release-notes.md), [snapshot](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-2f64e7a/manifest.json)
- [Comparison](../../../../tracking/github/repos/stripe/stripe-node/comparisons/stripe/22.5.0--22.6.0/comparison.json), [diff](../../../../tracking/github/repos/stripe/stripe-node/comparisons/stripe/22.5.0--22.6.0/diff.patch)
- [Supplement](../../../../raw/github/stripe/stripe-node/supplements/2026-09-21-2f64e7a-f49df03e/manifest.json), [handler](../../../../raw/github/stripe/stripe-node/supplements/2026-09-21-2f64e7a-f49df03e/files/src/StripeEventNotificationHandler.ts), [coercion](../../../../raw/github/stripe/stripe-node/supplements/2026-09-21-2f64e7a-f49df03e/files/src/V2Coercion.ts)
- [Review receipt](../../../../tracking/github/repos/stripe/stripe-node/ingest-review-436c32c5.md); exact per-topic implementation links in [[source-github-stripe-node]]

## `stripe@22.5.0` - Change Set `65d99a2` (2026-08-10)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `stripe` | `22.4.0` | `22.5.0` | 2026-08-10 | `65d99a2b76d0786d7cec8544920affadccc8b670` | Delta; approved focused reading |

**Important changes:** Adds snapshot/thin-event `WithoutVerification` helpers with AWS EventBridge and Azure CloudEvents extraction, static `Stripe.MAJOR_API_VERSION` (`dahlia`), an opt-in extensibility export condition and runtime transport, direct runtime-error propagation, shared response JSON parsing, and an environment-triggered Claude Code stderr hint. API pin `2026-07-29.dahlia`, OpenAPI marker `v2349`, generated checkout resources and runtime dependencies are unchanged.

**Developer impact:** Authenticate incoming events before queuing, then use the appropriate unverified parser only behind the trusted boundary. Shape recognition does not verify sender, timestamp or schema. Thin notifications retain lazy context-aware fetch helpers. The new transport is Stripe Script-specific, not a keyless regular Node integration: `api.stripe.com` only, no response headers/streaming, no local timeout enforcement in the adapter, and no default crypto provider.

**Migration and contradictions:** Existing verified methods remain available. Comments incorrectly name `webhooks.verifySignatureHeader`; use the actual `webhooks.signature.verifyHeader`/Async with an explicit positive tolerance if using the low-level API. High-level verified parsers retain a 300-second fallback. Release notes name lowercase `stripe.major_api_version`, but source/type-test diffs expose static `Stripe.MAJOR_API_VERSION`. Shared core permits missing/null `object` in the thin builder, while Node ESM requires `v2.core.event`; unexpected non-null object values now throw. Do not assume malformed/omitted-object input parity. The source-vs-README retry conflict persists: base platform default 2, extensibility configured default 0, README 1. Set the retry budget explicitly; the existing first connection-closed retry exception is separate.

**History clarification:** The new raw changelog rewrites the older 22.4.0 `OtherString` explanation to emphasize open enums. This is retrospective documentation, not a new 22.5.0 enum feature.

**Updated source sections:** Package status, evidence boundary, event parsing, runtime/metadata additions, retained history; Stripe Node concept, company/index and logs. Existing `22.1.1` and `22.4.0` history preserved; source count unchanged.

**Reading boundary:** Read all changed retained implementation and the complete comparison. Under the user-approved exception, unchanged historical changelog blocks and manifests were verified mechanically. Two added, 12 modified, 54 unchanged retained files. ESM entrypoint/emitter/test changes are comparison-only evidence; no SDK build, upstream test execution or live payment verification.

**Evidence:**

- [Release manifest](../../../../raw/github/stripe/stripe-node/releases/stripe/22.5.0/2026-09-21/manifest.json) and [release notes](../../../../raw/github/stripe/stripe-node/releases/stripe/22.5.0/2026-09-21/release-notes.md)
- [Snapshot manifest](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-65d99a2/manifest.json)
- [Comparison manifest](../../../../tracking/github/repos/stripe/stripe-node/comparisons/stripe/22.4.0--22.5.0/comparison.json) and [complete diff](../../../../tracking/github/repos/stripe/stripe-node/comparisons/stripe/22.4.0--22.5.0/diff.patch)
- [Webhooks](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-65d99a2/files/src/Webhooks.ts), [core](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-65d99a2/files/src/stripe.core.ts), [utilities](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-65d99a2/files/src/utils.ts)
- [Extensibility platform](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-65d99a2/files/src/platform/ExtensibilityPlatformFunctions.ts), [endpointFetch](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-65d99a2/files/src/net/EndpointFetchHttpClient.ts), [request sender](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-65d99a2/files/src/RequestSender.ts)
- [Repository changelog](../../../../raw/github/stripe/stripe-node/snapshots/2026-09-21-65d99a2/files/CHANGELOG.md)
- [Review receipt](../../../../tracking/github/repos/stripe/stripe-node/ingest-review-fdb611aa.md)

## `stripe@22.4.0` — Change Set `57626dc` (2026-07-29)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `stripe` | retained `22.1.1` baseline | `22.4.0` | 2026-07-29 | `57626dcdfb94164fc9f112dfaa3c57aec5130e4f` | Full |

**Important change:** The package pins Stripe API `2026-07-29.dahlia` and OpenAPI marker `v2349`. Checkout-focused changes remove limited-use Checkout line-item `dynamic_tax_rates`; add Payco and Samsung Pay future-usage typing; add allowed-payment-method controls to PaymentIntents and SetupIntents; add Alipay and MB WAY to invoice/subscription payment method enums; add subscription-schedule phase trial data; and add refund customer/account/payment-method attribution.

**Developer or merchant impact:** TypeScript consumers can see compile-time changes even within the v22 major because generated response enums are intentionally non-exhaustive across minor releases. Checkout integrations using `dynamic_tax_rates` must remove it. Integrations can configure the new fields only where Stripe product availability and merchant eligibility also permit them.

**Migration action:** Pin both the `stripe` package and API version in deployment records, remove `dynamic_tax_rates`, re-run TypeScript checks, review webhook event handling for new event types, and set `maxNetworkRetries` explicitly because the 22.4.0 README and constructor source disagree about its fallback.

**Updated source sections:** package status; evidence boundary; package/runtime shape; retries and idempotency; errors; webhooks; Checkout/PaymentIntent/SetupIntent/Payment Links; billing/refunds; TypeScript versioning; Stripe company/index; Stripe Node concept.

**Evidence boundary:** This is a full cumulative refresh from the retained 22.1.1 baseline, not a claim that every described SDK behavior was introduced in 22.4.0. Release-specific attribution is limited to the upstream 22.4.0 notes and fields verified in the exact-SHA capsule.

**Evidence:**

- [Release manifest](../../../../raw/github/stripe/stripe-node/releases/stripe/22.4.0/2026-08-08/manifest.json)
- [Release notes](../../../../raw/github/stripe/stripe-node/releases/stripe/22.4.0/2026-08-08/release-notes.md)
- [Snapshot manifest](../../../../raw/github/stripe/stripe-node/snapshots/2026-08-08-57626dc/manifest.json)
- [Package manifest](../../../../raw/github/stripe/stripe-node/snapshots/2026-08-08-57626dc/files/package.json)
- [API marker](../../../../raw/github/stripe/stripe-node/snapshots/2026-08-08-57626dc/files/src/apiVersion.ts)
- [OpenAPI marker](../../../../raw/github/stripe/stripe-node/snapshots/2026-08-08-57626dc/files/OPENAPI_VERSION)
- [Repository changelog](../../../../raw/github/stripe/stripe-node/snapshots/2026-08-08-57626dc/files/CHANGELOG.md)

## `stripe@22.1.1` — Retained Baseline (2026-05-06)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `stripe` | initial retained baseline | `22.1.1` | 2026-05-06 | `1899375db06ae1e102a93637e193f8c9cb1de831` | Legacy full |

**Important change:** This historical ingest established the Node SDK architecture, typed error handling, webhook verification, automatic pagination, retries/idempotency, and PaymentIntent/Checkout Session resource methods against OpenAPI marker `v2252`.

**Evidence boundary:** The legacy collector retained 14 key files rather than the current source-capsule structure. Its validated findings remain in the cumulative source, but it has no package-qualified release manifest or exact comparison packet in the current tracking system.

**Evidence:**

- [Legacy navigation record](../../../../raw/github-stripe-node.md)
- [Legacy source directory](../../../../raw/github-stripe-node/)
