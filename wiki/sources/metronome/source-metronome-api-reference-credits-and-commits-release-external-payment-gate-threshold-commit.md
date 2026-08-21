---
title: "Metronome API: Release External Payment Gate Threshold Commit"
type: source
date_ingested: 2026-08-21
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/credits-and-commits/release-external-payment-gate-threshold-commit.md"
raw_files:
  - "metronome/api-reference/credits-and-commits/release-external-payment-gate-threshold-commit-2026-07-13.md"
tags: [metronome, api, threshold-billing, payment-gating, commits, webhooks]
---

## Overview

This API reference documents the bearer-authenticated `POST /v1/contracts/commits/threshold-billing/release` operation for a threshold-billing workflow that uses an external payment gateway. The merchant, rather than Metronome, performs the payment transaction, then reports its outcome so Metronome can release or cancel the pending commit. The request correlates to `payment_gate.external_initiate` through a saved `workflow_id`; the page defines the accepted payload and a bare `200` response but leaves replay, failure recovery, ordering, and state-propagation behavior unspecified.

## Key takeaways

- External-gateway collection is merchant-owned: Metronome does not perform the payment-gating transaction for the client.
- The integrator must consume `payment_gate.external_initiate`, retain its `workflow_id`, and return that workflow ID to this endpoint.
- The endpoint is used to continue the pending workflow by releasing or cancelling the commit according to the reported external-payment outcome.
- Both `workflow_id` and `outcome` are required properties. `workflow_id` is a UUID, while `outcome` accepts `paid`, `PAID`, `failed`, or `FAILED`.
- The operation documents only `200 Success` and no response body, error response, or operation-specific retry behavior.

## Endpoint contract

| Item | Documented value |
| --- | --- |
| Method and path | `POST /v1/contracts/commits/threshold-billing/release` |
| Operation ID | `releaseExternalPaymentGateThresholdCommit-v1` |
| Authentication | Top-level HTTP bearer authentication through `bearerAuth` |
| Request media type | `application/json` |
| Required properties | `workflow_id`, `outcome` |
| `workflow_id` | String with UUID format; identifies the workflow to continue |
| `outcome` | One of `paid`, `PAID`, `failed`, or `FAILED` |
| Documented success | `200 Success`; no response-body schema is supplied |

The request-body description says the payload identifies the workflow in progress and tells Metronome which action to take to complete it. Although the referenced payload schema requires both properties, the OpenAPI `requestBody` object itself is not marked `required: true`. The page therefore does not establish runtime behavior for an omitted body, a missing property, a malformed UUID, an unsupported outcome spelling, a null value, or an extra property.

## State transition and webhook correlation

The external gateway path begins when the integrator receives `payment_gate.external_initiate`. Its `workflow_id` is the documented correlation handle for the later API call and must be saved. The endpoint then uses the external-payment outcome to release or cancel the commit that remains pending. The schema's four outcome values show accepted case variants for the two outcomes, but the page does not define a normalization rule beyond that enum.

The page does not define whether one workflow ID always maps to exactly one pending commit, whether it is single-use or expires, or how the pending commit can be queried before completion. It also does not say whether a generic webhook notification ID can substitute for the workflow ID; only the `workflow_id` named by this event is documented for correlation.

## Idempotency, retries, and failures

This endpoint page does not document a uniqueness field, an `Idempotency-Key` example, or operation-specific replay semantics. The separate API-wide idempotency reference says POST operations can use `Idempotency-Key`, but this page does not resolve what happens when the same workflow is submitted twice, when identical and conflicting outcomes race, or when a caller changes keys after an ambiguous response. Implementers should therefore apply the API-wide idempotency guidance without inferring that the workflow itself is safely repeatable.

Only `200 Success` is listed. No validation, authentication, authorization, not-found, conflict, rate-limit, or server-error response is attached to this operation, and there is no error-body schema here. The page gives no recovery procedure when external payment succeeds but the API call times out or fails, when delivery of `payment_gate.external_initiate` is duplicated or delayed, or when a failed report must be corrected. Webhook-delivery retry, payment retry, and this API call's retry are separate concerns.

## Ordering, concurrency, and propagation boundaries

The source supplies no ordering guarantee between the external-initiation event, the payment provider's result, this API call, and any later Metronome event. It does not define concurrent calls for one workflow, first-writer versus last-writer behavior, atomicity, conflicting outcomes, or a lock on the pending commit.

A successful `200` has no documented response body and no timing guarantee for when release or cancellation becomes visible. The page does not define propagation to available commit balance, ledger entries, invoices, contract reads, usage rating, product access, dashboards, exports, or follow-up webhooks. A transport-level success must therefore not be generalized into a documented downstream-settlement or visibility guarantee.

## Documentation boundaries

This endpoint is specifically for threshold billing with a payment gateway Metronome does not support. It does not describe the Stripe-managed gate, payment-provider object lifecycle, amount or currency charged, how the pending commit was created, payment authentication, refunds, chargebacks, or merchant application access control. The existing spend-threshold guide agrees on the external release-or-cancel flow; no contradiction was found.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-spend-threshold-billing]], [[metronome-credits-and-commits]], [[metronome-webhooks]], [[metronome-api-idempotency]]
- Related sources: [[source-metronome-guides-customers-billing-optimize-customer-experience-set-customer-spend-control]], [[source-metronome-guides-platform-configuration-setup-webhooks]], [[source-metronome-api-reference-idempotency]], [[source-metronome-api-reference-status-codes]]

## Raw Sources

- [[raw/metronome/api-reference/credits-and-commits/release-external-payment-gate-threshold-commit-2026-07-13|2026-07-13 snapshot — external-payment outcome endpoint, workflow correlation, and request schema]]
