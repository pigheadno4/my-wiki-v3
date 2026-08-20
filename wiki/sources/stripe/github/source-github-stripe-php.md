---
title: "GitHub: stripe/stripe-php"
type: source
date_ingested: 2026-08-15
date_updated: 2026-08-15
original_format: github-repo
raw_files:
  - "github/stripe/stripe-php/snapshots/2026-08-15-edf8118/manifest.json"
tags: [stripe, stripe-php, php, server-sdk, checkout, payment-intents, subscriptions, webhooks, terminal, github-repository]
---

## Overview

`stripe/stripe-php` publishes the `stripe/stripe-php` Composer package, Stripe's server-side PHP SDK. This initial full ingest covers `stripe-php@21.2.0` at exact SHA `edf8118f0b96d69f06f372da9168d613d1aed072`, released on 2026-08-10.

Repository: <https://github.com/stripe/stripe-php>

## Evidence Boundary

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
| `stripe/stripe-php` | `21.2.0` | `2026-07-29.dahlia` | PHP 7.2+ | Initial approved full ingest |

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

## Related

- Company: [[stripe]]
- Concepts: [[stripe-php-sdk]], [[stripe-payment-intents]], [[stripe-checkout]], [[stripe-payment-links]]
- Parallel server SDK: [[source-github-stripe-node]]
- History: [[changelog-github-stripe-php]]

## Raw Sources

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
