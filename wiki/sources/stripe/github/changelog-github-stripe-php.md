---
title: "GitHub changelog: stripe/stripe-php"
type: source
date_ingested: 2026-08-15
date_updated: 2026-08-15
original_format: github-repo
raw_files:
  - "github/stripe/stripe-php/snapshots/2026-08-15-edf8118/manifest.json"
tags: [stripe, stripe-php, php, changelog, github-repository]
---

## Overview

Package-qualified retained release history for `stripe/stripe-php`. Cumulative implementation knowledge belongs in [[source-github-stripe-php]].

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
