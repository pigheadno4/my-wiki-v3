---
title: "Braintree Forward API Server Errors"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/forward-api/server-errors"
raw_files:
  - "braintree/docs/reference/forward-api/server-errors-2026-09-16.md"
tags: [braintree, braintree-extend, forward-api, server-errors, api-errors]
---

## Overview

This collected, unversioned Braintree Forward API reference describes server errors returned when Forward API cannot complete a request. It is a failure-reference route for [[braintree-forward-api]], not a [[braintree-orchestration]] transaction-lifecycle reference, and it does not establish destination acceptance, payment execution, settlement, funding, or current production enablement. See [[braintree]].

## Key takeaways

- Production Forward API use is subject to eligibility; the snapshot routes readers to an Account Manager or Business Development rather than establishing current merchant eligibility or enablement.
- The page shows an example JSON body containing `error`, `message`, and `request-uuid`, but describes its format only as resembling the example. Treat the object as an illustration, not a guaranteed required response schema.
- The catalog maps connection-establishment, request-processing, and between-packet timeouts to HTTP 504, and a failed TLS handshake with the destination API to HTTP 502. Use the raw table for the exact error names, explanations, additional `message` fields, and status mappings.
- A destination-originated 5xx is handled differently: the page says the Forward API response has status code 200 while the response body shows the destination response error in its `status` field. An HTTP 200 from Forward API therefore does not by itself establish destination success.
- This page does not define a retry policy, remediation sequence, destination processing result, or payment-lifecycle outcome.

> [!warning] Distinguish Forward API HTTP status from destination status
> When the destination returns a 5xx, the documented Forward API response status is 200 and the destination response error is represented in the body. Inspect the destination status carried in the response body rather than interpreting the Forward API HTTP 200 as a successful destination or payment outcome.

## Detail locators

- Production eligibility and Account Manager or Business Development inquiry route: `**AVAILABILITY**`, raw lines 16-17.
- Server-error identity and illustrative JSON response body: introductory paragraph and JSON block, raw lines 19-30.
- Exact timeout and TLS error catalog, additional fields, and HTTP 502/504 mappings: error table, raw lines 32-37.
- Destination 5xx represented by a Forward API HTTP 200 with the destination error in the body `status` field: `**NOTE**`, raw lines 39-40.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-forward-api]]
- General forwarding model: [[source-braintree-reference-forward-api-overview]]
- Distinct processor-connection route: [[braintree-orchestration]]

## Related raw API references

The following linked pages are navigation targets and were not read as raw factual evidence for this entry:

- [[raw/braintree/docs/reference/forward-api/overview-2026-09-16|Forward API overview]]
- [[raw/braintree/docs/reference/forward-api/config-2026-09-16|Forward API configuration reference]]

## Raw Sources

- [[raw/braintree/docs/reference/forward-api/server-errors-2026-09-16|Braintree Forward API server errors]] - fully read 2026-09-16 snapshot covering production eligibility, the illustrative error body, timeout/TLS server-error catalog, HTTP status mappings, and destination-5xx relay behavior
