---
title: "Braintree Forward API Validation Errors"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/forward-api/validation-errors"
raw_files:
  - "braintree/docs/reference/forward-api/validation-errors-2026-09-16.md"
tags: [braintree, braintree-extend, forward-api, validation-errors, api-errors]
---

## Overview

This collected, unversioned Braintree Forward API reference describes validation errors returned in the response body to the caller's application. Its example response has a top-level `error`, a nested `message` object containing `"validation_error?": true` and error-specific context, and a `request-uuid`. The page says all validation errors include the validation flag in `message`; the remaining catalog supplies error names, explanations, and selected additional `message` fields. See [[braintree]] and [[braintree-forward-api]].

This is a retrieval route for Forward API request-validation failures. It is not Braintree Orchestration documentation, and a validation response or request UUID does not establish that a destination accepted or processed a request or that a payment was created, authorized, captured, settled, reconciled, or funded.

## Key takeaways

- Production Forward API use is subject to eligibility; the snapshot directs readers to an Account Manager or Business Development rather than establishing current merchant eligibility or production enablement.
- The catalog covers configuration shape, request syntax and required inputs, mutual-TLS certificate/key validation, HTTP method and header constraints, destination URL and network restrictions, and selected payment-method/tokenization conditions. Use the raw table for the complete error-name, explanation, and additional-field inventory rather than treating these categories as exhaustive runtime behavior.
- Environment boundaries are consequential: inline client certificates are sandbox-only; inline configurations are disallowed in production and production configs must be submitted and approved. `debug_transformations` is also disallowed in production because it might return PCI-sensitive data.
- Mutual TLS requires both `client_cert` and `client_key`; the catalog separately identifies invalid X.509 certificate and PEM-encoded PKCS 8 private-key inputs. These validation rules do not establish how credentials should be provisioned, stored, rotated, or authorized for a destination.
- The destination/network entries include DNS lookup failure, malformed or non-HTTP(S) URLs, private-network rejection, and config-regex mismatch. They describe validation failures, not downstream retry policy or a guarantee that correcting an input will produce destination or payment success.
- Two final catalog entries explicitly say to retry after updating, respectively, the customer-vault email/phone for AMEX network tokenization or the payment method for an endpoint limited to `PayPalBillingAgreement` and `VenmoAccount`. Preserve those subject-specific conditions; they are not a general retry guarantee for other Forward API errors.

> [!warning] Production and sensitive-debug boundaries
> The 2026-09-16 snapshot gates production use on eligibility, requires submitted and approved production configs, and prohibits production `debug_transformations` because they might return PCI-sensitive data. Collection of this page, sandbox behavior, or possession of credentials does not prove production approval or safe handling of sensitive output.

> [!warning] Validation is not downstream execution evidence
> These errors concern Forward API request validation. The page does not establish destination-side authorization, acceptance, processing, or any payment-lifecycle result, and it supplies no general automatic-retry or eventual-success contract.

## Detail locators

- Production eligibility and Account Manager or Business Development inquiry route: `**AVAILABILITY**`, raw lines 17-20.
- Example response body's `error`, nested `message`, validation flag, method context and `request-uuid`: opening JSON example, raw lines 22-33.
- Shared `message` validation flag and start of the error catalog: raw line 34.
- Configuration, inline production restrictions, certificate/key, conditional transformation, header, request-format and JSON Schema entries: error table, raw lines 36-48.
- Missing config, payment type, URL and request format; config URL-regex, JSON shape and HTTP-method entries: error table, raw lines 49-57.
- DNS, private-network, URL/protocol and production debug-transformation entries: error table, raw lines 58-62.
- Merchant, override and payment-method input requirements plus the two subject-specific retry entries: error table, raw lines 63-69.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-forward-api]]
- General forwarding model: [[source-braintree-reference-forward-api-overview]]
- Distinct processor-connection route: [[braintree-orchestration]]

## Related raw API references

The following linked pages are navigation targets and were not read as factual evidence for this entry:

- [[raw/braintree/docs/reference/forward-api/config-2026-09-16|Forward API configuration reference]]
- [[raw/braintree/docs/reference/forward-api/forward-2026-09-16|Forward API forwarding-request reference]]
- [[raw/braintree/docs/guides/extend/forward-api/examples-2026-09-16|Forward API examples guide]]

## Raw Sources

- [[raw/braintree/docs/reference/forward-api/validation-errors-2026-09-16|Braintree Forward API validation errors]] - fully read 2026-09-16 snapshot covering the response shape, common validation marker, validation-error catalog, production restrictions and subject-specific retry text
