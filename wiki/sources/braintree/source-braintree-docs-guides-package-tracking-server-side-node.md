---
title: "Braintree Package Tracking Server-Side Configuration (Node.js)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/package-tracking/server-side/node"
raw_files:
  - "braintree/docs/guides/package-tracking/server-side/node-2026-09-16.md"
tags: [braintree, package-tracking, nodejs, server-sdk, paypal, transactions]
---

## Overview

This collected Braintree server-side Node.js guide shows a three-step package-tracking example: place a transaction with line items and immediate settlement submission, call `gateway.transaction.packageTracking()` with a transaction ID and package metadata, then retrieve the transaction with `gateway.transaction.find()` to inspect package trackers and the later-populated PayPal tracker ID.

This is a 2026-09-16 unversioned website snapshot. It is not current availability, merchant or transaction eligibility, product enablement, exact Node package-version or runtime evidence, a complete runnable integration, or proof of payment authorization, capture, settlement, funding, shipment, carrier acceptance, delivery, buyer notification, dispute resolution or hold release.

## Key takeaways

- The displayed sale request sets `submitForSettlement: true` and includes transaction line items. The next displayed step creates a package object with example carrier and tracking-number values, `notifyPayer: true`, and optional line items, then passes `transactionId` and that object to `gateway.transaction.packageTracking()`. These are examples, not universal required values or proof that the request succeeded.
- The package-tracking callback reads `response.transaction.packages[0].id`, `.carrier`, and `.trackingNumber`. Its comment says the PayPal tracker ID is not immediately available in the package-tracking response and should instead be present after a later transaction lookup; that timing is snapshot guidance, not a guaranteed propagation time or outcome.
- The retrieval example calls `gateway.transaction.find()` and reads the first package's `id`, `carrier`, `trackingNumber`, and `paypalTrackerId`. Array index `0`, the placeholder identifiers, the carrier value, notification choice, quantities and product fields are example details; use the raw locators for their exact rendering.
- The snippets depend on surrounding values not defined inside the shown functions: `transactionId` is referenced by `sampleIntegration()`, and `response.transaction.id` is referenced by `retrievePackageTrackers()` even though `response` is not introduced in that function. The page therefore does not establish a standalone executable program, error-path safety, exact SDK signature for a specific package version, or a successful provider response.

> [!warning] Preserve the settlement-state conflict
> This Node page labels tracking creation as occurring "after submitting for settlement," while the fully read package-tracking overview says to add tracking details "after the transaction settles." Do not use the example's looser wording to weaken the overview's settled-state condition. This snapshot does not resolve which transaction statuses the gateway currently accepts.

> [!warning] Metadata submission is not fulfillment or payment proof
> A package-tracking request, returned package entry or later PayPal tracker ID does not itself prove shipment, carrier acceptance, delivery, buyer notice, dispute outcome, hold release, authorization, capture, settlement or funding.

## Detail locators

- Transaction-sale request, immediate settlement-submission option and line-item example: raw lines 18-60 under `1. Place transaction`.
- Package object, example carrier/tracking values, payer notification and optional line items: raw lines 63-96 under `2. Create tracking for transaction after submitting for settlement`.
- `gateway.transaction.packageTracking()` invocation, callback package fields and delayed PayPal tracker-ID comment: raw lines 98-111.
- Later `gateway.transaction.find()` lookup and package fields, including `paypalTrackerId`: raw lines 115-130 under `3. Retrieve transactions with package trackers`.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]
- Package-tracking lifecycle, eligibility, request/response fields and captured SDK-version prerequisites: [[source-braintree-docs-guides-package-tracking-overview]]

## Raw Sources

- [[raw/braintree/docs/guides/package-tracking/server-side/node-2026-09-16|Braintree package-tracking server-side Node.js guide]] - complete collected snapshot of the transaction, package-tracking and later transaction-lookup examples
