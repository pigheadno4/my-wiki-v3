---
title: "Braintree At-Most-Once Processing Guide"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/at-most-once"
raw_files:
  - "braintree/articles/guides/at-most-once-2026-09-16.md"
tags: [braintree, at-most-once, idempotency, api-request-key, duplicate-requests]
---

## Overview

This collected Braintree guide describes At-Most-Once Processing, Braintree's logical-intent idempotency model for preventing duplicate API requests from causing duplicate payment actions. The merchant supplies an `ApiRequestKey` that uniquely identifies the intended logical action; identical keys within a 30-day window are treated as duplicate requests. The guide distinguishes this feature from network-level idempotency and says it is mutually exclusive with transaction duplicate checking.

The captured page labels itself as limited to a select group or specific audience, not generally public, and directs readers to the product team before sharing it. This 2026-09-16 snapshot therefore does not establish current general availability, account enablement, SDK support or successful payment execution.

## Key takeaways

- For the documented model, Braintree returns the current state of the original logical intent for an identical request within the 30-day window; this is not a promise to replay the same network response, and a returned transaction state may be unsuccessful or may have advanced since the original request.
- When the key and other request details match, an in-progress original request produces a retryable validation error, while a completed original request returns the action's current result. Reusing the key with changed amount, customer, payment-method or other request details produces a validation error.
- The captured supported-action list includes authorize, charge, partial capture, settlement submission, credit, refund and reverse. Exact API operations, status-dependent results, legacy HTTP codes, error codes and action-specific scenarios remain in the raw tables.
- A validation error is not blanket permission to generate a new key and retry. The guide's action-specific footnotes make safety depend on whether a transaction or refund record exists and on the operation's state; some outcomes require further investigation and potentially Braintree intervention.

> [!warning] Restricted captured audience
> The source says the page is not generally public and should be discussed with the product team before sharing. Treat it as snapshot documentation, not proof that the feature is available or enabled for a particular merchant.

> [!warning] Do not equate this with response replay
> Braintree describes this as logical-intent At-Most-Once Processing rather than network-level idempotency. Duplicate requests can return a retryable validation error or the current action state, not necessarily the original response.

> [!warning] Do not rotate the key blindly
> Before generating a new `ApiRequestKey`, use the operation-specific state and record-presence rules in the raw guide. A new key can create a functional duplicate when the first request may already have succeeded.

## Detail locators

- Restricted-audience notice and product-team sharing direction: notice before `## At-Most-Once Processing`, raw lines 14-15.
- Feature purpose, unique-request-key requirement and mutual exclusion with transaction duplicate checking: `## At-Most-Once Processing`, raw lines 20-30.
- `ApiRequestKey` identity and 30-day duplicate window: `## Details`, raw lines 33-35.
- Same-details in-progress and completed outcomes, plus changed-details validation: `## Details`, raw lines 37-42.
- Supported action families: `## Supported Actions`, raw lines 45-57.
- Authorize and charge scenario matrices and consequential changed-request/new-key footnotes: `### Authorize` and `### Charge`, raw lines 59-106.
- Refund, settlement, partial-settlement, credit and reverse matrices with action-specific retry qualifications: raw lines 109-194.
- Validation error codes `915232`, `915233` and `915234`: `## Error Codes`, raw lines 197-203.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-at-most-once-processing]]
- Server gateway operations: [[braintree-server-sdk]]
- Distinct, mutually exclusive mechanism: [[source-braintree-control-panel-duplicate-checking]]

## Raw Sources

- [[raw/braintree/articles/guides/at-most-once-2026-09-16|Braintree At-Most-Once Processing guide]] - complete collected guide covering logical-intent semantics, request-key identity, duplicate outcomes, supported actions, action-specific retry qualifications and error codes
