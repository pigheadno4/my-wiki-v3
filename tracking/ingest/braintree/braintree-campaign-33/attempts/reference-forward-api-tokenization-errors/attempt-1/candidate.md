---
title: "Braintree Forward API Tokenization Errors Reference"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/forward-api/tokenization-errors"
raw_files:
  - "braintree/docs/reference/forward-api/tokenization-errors-2026-09-16.md"
tags: [braintree, braintree-extend, forward-api, tokenization, errors, testing]
---

## Overview

This collected, unversioned Braintree Forward API reference catalogs errors returned by Forward API tokenization. It places the error in a JSON response body shaped with `error`, `message` and `request-uuid` fields, and maps named failures to HTTP 400, 422 or 500 responses. Production Forward API use is subject to eligibility. See [[braintree]] and [[braintree-forward-api]].

This is the Forward API tokenization failure catalog, not an [[braintree-orchestration]] transaction-lifecycle reference. It does not establish that a destination processed a request, nor does it specify downstream retry, authorization, capture, settlement or funding behavior.

## Key takeaways

- The catalog distinguishes an unsupported payment-instrument type (HTTP 400), a set of validation, issuer, risk, network, PayPal and token-state failures (HTTP 422), and an unhandled tokenization exception (HTTP 500). The individual error names, explanations and optional message fields remain in the raw table.
- A risk-denial explanation explicitly says its reason must never be displayed to the customer to prevent information disclosure. This customer-display restriction is specific to that catalog entry; the page does not define a general remediation or retry policy.
- The page supplies sandbox-only card numbers and nonces for selected unsuccessful tokenization responses. A separate negative-testing table maps two PayPal mock rejection cases to `max_amount` values; these are test triggers, not production outcome rules.
- Some entries describe conditions involving cryptogram eligibility, issuer support, network validation, token state or token presence. Treat those descriptions as error classifications, not proof of a particular account's enablement, token history or corrective action.

> [!warning] Production availability is separately gated
> The snapshot states that production Forward API use is subject to eligibility and routes questions to an Account Manager or Business Development. The error catalog and sandbox fixtures do not prove production enablement.

> [!warning] Preserve the risk-reason disclosure restriction
> The `Denied due to risk` reason is marked as information that should never be shown to the customer. Do not surface that reason in customer-facing messages.

## Detail locators

- Production eligibility and inquiry route: `**AVAILABILITY**`, raw lines 17-20.
- Example response-body structure and `error`, `message` and `request-uuid` fields: introductory paragraph and JSON block, raw lines 22-32.
- Full error, explanation, message and HTTP-status catalog: main table, raw lines 33-54.
- Risk-denial disclosure warning: `Denied due to risk`, raw line 38.
- Sandbox card-number and nonce fixtures for unsuccessful tokenization: `### Test credit card numbers and nonces`, raw lines 59-69.
- PayPal mock rejection testing through `max_amount`: `### Negative testing with PayPal tokenization`, raw lines 72-77.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-forward-api]]
- Distinct processor-connection route: [[braintree-orchestration]]

## Related raw API references

The following linked pages are navigation targets and were not read as factual evidence for this entry:

- [[raw/braintree/docs/reference/forward-api/tokenization-2026-09-16|Forward API tokenization reference]]
- [[raw/braintree/docs/reference/forward-api/overview-2026-09-16|Forward API overview]]

## Raw Sources

- [[raw/braintree/docs/reference/forward-api/tokenization-errors-2026-09-16|Braintree Forward API tokenization errors reference]] - fully read 2026-09-16 snapshot covering response-body shape, error/status catalog, disclosure warning and sandbox negative-testing fixtures
