---
title: "GitHub changelog: paypal-examples/paypal-sdk-server-side-integration"
type: source
date_ingested: 2026-08-05
original_format: github-repo
raw_files:
  - "github/paypal/paypal-sdk-server-side-integration/snapshots/2026-08-04-5409a3b/manifest.json"
tags: [paypal, checkout, subscriptions, server-side, samples, changelog, github-repository]
---

## Overview

Commit-qualified history for `paypal-examples/paypal-sdk-server-side-integration`. Durable architecture and implementation findings belong in [[source-github-paypal-sdk-server-side-integration]].

## `default-branch@5409a3b` - Full Historical Baseline (2023-09-28)

| Ref | Prior reviewed SHA | Current SHA | Ingest mode |
| --- | --- | --- | --- |
| `main` | Baseline | `5409a3b9c0b6d0049fc3be9386092759fd6a1d5c` | Full |

The accepted 2026-08-04 capsule retains 36 selected files totaling 101,281 bytes. Two tests totaling 4,537 bytes are excluded by policy. This is the first collector-managed baseline, so no prior commit comparison exists.

### Baseline scope

- Fastify/TypeScript server with configuration, OAuth, client-token, Orders, shipping-patch, and Subscriptions routes.
- Browser examples for Buttons, Hosted Fields, subscription creation, post-approval activation, and plan revision.
- Server-owned product catalog and amount construction.
- Partner migration guidance covering attribution and connected-merchant headers.
- One-key capture retry after 5xx and guidance to validate captured amounts before fulfillment.

### Historical and migration impact

The repository declares PayPal JS SDK 5.1.x and was last committed in September 2023. It is useful when maintaining or explaining this older sample, but it is not an upgrade target and must not replace current JS SDK v6 documentation or the newer `paypal-examples/v6-web-sdk-sample-integration` repository.

For production migration, retain the client/server security boundary and server-owned totals, then revalidate APIs, SDK initialization, eligibility, Hosted Fields/Card Fields behavior, and subscription lifecycle against current documentation. Do not carry forward the sample's API-base precedence bug, order-retrieval mismatch, duplicate response parsing, shipping-schema gap, discount arithmetic, missing subscription requirements, revise-response handling, or incomplete idempotency coverage.

### Evidence and updated wiki areas

**Updated wiki areas:** cumulative repository source; PayPal Checkout; Expanded Checkout; Subscriptions; PayPal company and provider index.

**Evidence:**

- `raw/github/paypal/paypal-sdk-server-side-integration/snapshots/2026-08-04-5409a3b/manifest.json`
- `raw/github/paypal/paypal-sdk-server-side-integration/snapshots/2026-08-04-5409a3b/files/README.md`
- `raw/github/paypal/paypal-sdk-server-side-integration/snapshots/2026-08-04-5409a3b/files/docs/update-from-client-side-helpers-to-server-side-for-partners.md`
- `raw/github/paypal/paypal-sdk-server-side-integration/snapshots/2026-08-04-5409a3b/files/src/controller/order-controller.ts`
- `raw/github/paypal/paypal-sdk-server-side-integration/snapshots/2026-08-04-5409a3b/files/src/controller/subscription-controller.ts`
- `raw/github/paypal/paypal-sdk-server-side-integration/snapshots/2026-08-04-5409a3b/files/src/order/capture-order.ts`
