---
title: "GitHub changelog: stripe/stripe-php"
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
tags: [stripe, stripe-php, php, changelog, github-repository]
---

## Overview

Package-qualified retained release history for `stripe/stripe-php`. Cumulative implementation knowledge belongs in [[source-github-stripe-php]].

## `stripe-php@22.0.0` - Full (2026-09-30)

From `stripe-php@21.3.2` to `stripe-php@22.0.0`, SHA `c4c1f658483e717519935222e47af224ef4a508b`; GitHub published 2026-10-01, ingested 2026-10-18. Approved full/focused reading: exact-SHA changelog rather than mutable master release link; 916-file capsule, 443 added/172 modified/301 unchanged, all 1,488 upstream changes classified, no gaps. No older knowledge replaced.

**Changes:** PHP7.4 minimum and Endive API; expanded union PHPDoc/static-analysis shapes; callback clients clear inherited account before applying event context; singleton related-object support; expanded typed thin events; guarded notice suppression. Selected Checkout/PaymentIntent/SetupIntent request-side method-list fields removed, while allowed fields and Payment Links remain version-qualified. PayPay/SeQura/BLIK and tax/payment-record annotations extend contracts, not availability. Explicit subscription pause/schedule plans, object-shaped anchors, item trials and status details expand Billing.

**Migration:** upgrade PHP first, review Endive request shapes/Financial Connections filters, test webhook account-context routing and subscription lifecycle, keep signature verification/idempotency, and do not equate PHPDoc changes with runtime validation. Preserve the explicit contradiction between the trial-only status comment and the pause endpoint. Concepts first (PHP, Checkout, Subscriptions, Payment Links); source/company/catalog/logs updated; count unchanged. No SDK tests/build/payment execution.

[Release](../../../../raw/github/stripe/stripe-php/releases/stripe-php/22.0.0/2026-10-18/manifest.json), [snapshot](../../../../raw/github/stripe/stripe-php/snapshots/2026-10-18-c4c1f65/manifest.json), [exact changelog](../../../../raw/github/stripe/stripe-php/snapshots/2026-10-18-c4c1f65/files/CHANGELOG.md), [comparison](../../../../tracking/github/repos/stripe/stripe-php/comparisons/stripe-php/21.3.2--22.0.0/comparison.json). Implementation/quotes: [[source-github-stripe-php]].

## `stripe-php@21.3.2` - Delta (2026-09-09)

From `stripe-php@21.3.1` to `stripe-php@21.3.2`, SHA `0d8b075e1a97d15c5324353a5277d0ea686ea525`; ingested 2026-10-18 with approved focused reading. Verifier rejects PHP-empty webhook secrets before HMAC calculation. This does not enforce `whsec_` or reject whitespace-only strings. Existing timestamp semantics remain: low-level null/zero disables the timestamp test, public helpers normally use 300 seconds. Verify configured signing secrets before rollout. PHP/API unchanged; older knowledge preserved. Updated PHP concept/source/company/index/logs; no SDK execution.

[Release](../../../../raw/github/stripe/stripe-php/releases/stripe-php/21.3.2/2026-10-18/manifest.json), [snapshot](../../../../raw/github/stripe/stripe-php/snapshots/2026-10-18-0d8b075/manifest.json), [comparison](../../../../tracking/github/repos/stripe/stripe-php/comparisons/stripe-php/21.3.1--21.3.2/comparison.json). Exact runtime quotes: [[source-github-stripe-php]].

## `stripe-php@21.3.1` - Delta (2026-09-01)

From `stripe-php@21.3.0` to `stripe-php@21.3.1`, SHA `12986995cd5e229cc094d4b57de056f8e2e6e5a9`; ingested 2026-10-18 under approved focused reading. Origin-relative path checks, CR/LF/NUL header checks and event-ID URL encoding harden request construction. Custom raw paths must begin with one slash; custom API bases and webhook authentication remain caller responsibilities. PHP/API unchanged; all older chapters preserved. Updated PHP concept/source/company/catalog/logs; no SDK execution.

[Release](../../../../raw/github/stripe/stripe-php/releases/stripe-php/21.3.1/2026-10-18/manifest.json), [snapshot](../../../../raw/github/stripe/stripe-php/snapshots/2026-10-18-1298699/manifest.json), [comparison](../../../../tracking/github/repos/stripe/stripe-php/comparisons/stripe-php/21.3.0--21.3.1/comparison.json). Implementation/quotes: [[source-github-stripe-php]].

## `stripe-php@21.3.0` - Full (2026-08-26)

From `stripe-php@21.2.1` to `stripe-php@21.3.0`, SHA `fe99159b9ee0a74be3c12c0305e5338e0b9905c3`; GitHub published 2026-08-27; ingested 2026-10-18. User-approved full overrides the delta recommendation, with approved focused reading and all prior history preserved. PHP7.2/API `2026-08-26.dahlia`; typed verified/unverified thin handlers, pre-dispatch hook/fallback, nullable/polymorphic V2 coercion and array-element fix. Checkout funding restrictions, cancellation feedback resources, Billie annotations and Connect Payment Link updates expand the contract. Register handlers at startup, retain public signature verification, and test coercion/context boundaries before upgrading.

Updated PHP, Checkout, Payment Links and Subscriptions concepts first, then cumulative source/company/catalog/logs. Source records discriminator passthrough, inbound decimal limits and callback account-context behavior. [Release](../../../../raw/github/stripe/stripe-php/releases/stripe-php/21.3.0/2026-10-18/manifest.json), [snapshot](../../../../raw/github/stripe/stripe-php/snapshots/2026-10-18-fe99159/manifest.json), [comparison](../../../../tracking/github/repos/stripe/stripe-php/comparisons/stripe-php/21.2.1--21.3.0/comparison.json). Exact implementation links and quotes: [[source-github-stripe-php]]. No upstream SDK tests executed.

## `stripe-php@21.2.1` - Delta (2026-08-20)

From `21.2.0` to `21.2.1`, SHA `da798f6224c5ff6f89d8d78025044f418ee27db8`; ingested 2026-10-18, approved delta with focused reading. Plugin hints move from module loading to client/request initialization, with CLI/nonempty CLAUDECODE/loaded-PHPUnit checks and a one-attempt-per-process boundary. Payment API pin and PHP floor remain unchanged. Ten upstream changes classified; no gaps. Historical baseline preserved, no upstream tests/payment execution.

Updated PHP concept, cumulative source, company/catalog and logs. [Release](../../../../raw/github/stripe/stripe-php/releases/stripe-php/21.2.1/2026-10-18/manifest.json), [snapshot](../../../../raw/github/stripe/stripe-php/snapshots/2026-10-18-da798f6/manifest.json), [comparison](../../../../tracking/github/repos/stripe/stripe-php/comparisons/stripe-php/21.2.0--21.2.1/comparison.json). Implementation and quotes: [[source-github-stripe-php]].

## `stripe-php@21.2.0` - Initial Baseline (2026-08-10)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `stripe/stripe-php` | initial retained baseline | `21.2.0` | 2026-08-10 | `edf8118f0b96d69f06f372da9168d613d1aed072` | Full |

**Important change:** The initial baseline pins Stripe API `2026-07-29.dahlia` and requires PHP 7.2+. The exact 21.2.0 release surfaces `object` on `EventNotification`, adds event parsers that deliberately skip verification for previously verified or trusted payloads, adds test signature-header generation, corrects V2 timestamp annotations, and exposes a major API version constant.

**Developer or merchant impact:** Existing PHP integrations gain explicit helpers for queued or cloud-delivered event processing, but ordinary webhook endpoints must continue authenticating the exact payload. The SDK's broad generated API does not itself establish merchant access to a payment method or preview feature.

**Migration action:** Pin the Composer package and API version in deployment records; verify PHP runtime compatibility; keep raw webhook bodies; use `WithoutVerification` helpers only after a documented trust step; and test checkout, subscription, event, and idempotency behavior before a major SDK upgrade.

**Updated source sections:** package/runtime shape; request encoding; retries/idempotency; webhooks and thin events; Checkout, PaymentIntents, Payment Links, subscriptions, and Terminal; Stripe company/index; Stripe PHP concept.

**Evidence boundary:** This is an initial full cumulative baseline. Only the items in the 21.2.0 release notes are attributed to 21.2.0; the broader client and API behavior is baseline evidence rather than a claim that it was introduced in this release.

**Evidence:**

- [Release manifest](../../../../raw/github/stripe/stripe-php/releases/stripe-php/21.2.0/2026-08-15/manifest.json)
- [Release notes](../../../../raw/github/stripe/stripe-php/releases/stripe-php/21.2.0/2026-08-15/release-notes.md)
- [Snapshot manifest](../../../../raw/github/stripe/stripe-php/snapshots/2026-08-15-edf8118/manifest.json)
- [Package manifest](../../../../raw/github/stripe/stripe-php/snapshots/2026-08-15-edf8118/files/composer.json)
- [API version](../../../../raw/github/stripe/stripe-php/snapshots/2026-08-15-edf8118/files/lib/Util/ApiVersion.php)
- [Repository changelog](../../../../raw/github/stripe/stripe-php/snapshots/2026-08-15-edf8118/files/CHANGELOG.md)
