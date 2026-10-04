---
title: "Braintree AIB AF At-Most-Once Processing (LR)"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/aib-af/idempotency-LR"
raw_files:
  - "braintree/articles/aib-af/idempotency-LR-2026-09-16.md"
tags: [braintree, aib-af, at-most-once, idempotency, api-request-key]
---

## Overview

This Braintree-hosted AIB AF/LR document describes At-Most-Once Processing, its logical-intent idempotency model for preventing duplicate API requests from producing duplicate payment actions. Merchants supply an `ApiRequestKey` that uniquely identifies the intended logical action; identical keys within 30 days are treated as duplicates. The document says this feature is mutually exclusive with transaction duplicate checking and distinguishes it from network-level response replay.

The collected route places the document under AIB AF and labels the slug `idempotency-LR`; the body does not explain those labels or identify a processor, region, or pricing model. Treat this as Braintree snapshot documentation for that route, not independent current bank policy or proof of availability for another account variant.

## Key takeaways

- For identical requests within the 30-day window, the model returns the current state of the request's logical intent rather than necessarily replaying an original network response. That current state may have advanced or may be unsuccessful.
- Matching request details can produce a retryable validation error while the original is in progress or the current result after completion; reusing a key with changed request details produces a validation error.
- Generating a new key is not uniformly safe. The action-specific tables and footnotes condition retries on record presence and operation state, and some charge outcomes require investigation and potentially Braintree intervention.

> [!warning] Restricted captured audience
> The captured page says it is limited to a select group or specific audience, is not generally public, and should not be shared without contacting the product team. It does not establish current merchant eligibility, enablement, SDK support, or successful payment execution.

> [!warning] Do not treat a new key as a blanket retry
> A changed key can cause a functional duplicate if the first request may already have succeeded. Follow the exact action and state-specific matrix in the raw evidence.

## Detail locators

- Restricted-audience and sharing notice: raw lines 14-15.
- Logical-intent purpose, mutual exclusion with transaction duplicate checking, and 30-day current-state behavior: `## At-Most-Once Processing`, raw lines 20-30.
- `ApiRequestKey` requirement and duplicate-key window: `## Details`, raw lines 33-35.
- Matching, in-progress, completed, and changed-request outcomes: `## Details`, raw lines 37-42.
- Supported action families and exact operation names: `## Supported Actions`, raw lines 45-57 and the action sections that follow.
- Authorize, charge, refund, settlement, partial-settlement, and credit matrices, including action-specific retry qualifications: raw lines 59-175.
- Validation errors `915232`, `915233`, and `915234`: `## Error Codes`, raw lines 178-184.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-at-most-once-processing]]

## Raw Sources

- [[raw/braintree/articles/aib-af/idempotency-LR-2026-09-16|Braintree AIB AF At-Most-Once Processing (LR)]] - complete captured document with logical-intent semantics, duplicate handling, action-specific scenarios, retry qualifications, and error codes
