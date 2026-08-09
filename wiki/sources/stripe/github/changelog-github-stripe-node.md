---
title: "GitHub changelog: stripe/stripe-node"
type: source
date_ingested: 2026-08-08
date_updated: 2026-08-08
original_format: github-repo
raw_files:
  - "github/stripe/stripe-node/snapshots/2026-08-08-57626dc/manifest.json"
tags: [stripe, stripe-node, node-js, changelog, github-repository]
---

## Overview

Package-qualified retained release history for `stripe/stripe-node`. Cumulative implementation knowledge belongs in [[source-github-stripe-node]].

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
