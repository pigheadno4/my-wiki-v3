---
title: "Braintree Forward API Transformation Errors"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/forward-api/transformation-errors"
raw_files:
  - "braintree/docs/reference/forward-api/transformation-errors-2026-09-16.md"
tags: [braintree, braintree-extend, forward-api, transformation-errors, api-errors]
---

## Overview

This collected, unversioned Braintree Forward API reference describes transformation errors returned in the response body to the caller's application. The page illustrates a JSON response with a top-level `error`, a nested `message` object, and a `request-uuid`; because it says the format merely resembles the example, the illustration is not treated as a complete required response schema. See [[braintree]] and [[braintree-forward-api]].

This is a failure-reference route for Forward API request transformations, not PayPal Orchestration documentation. A transformation error or request UUID does not establish that a destination received, accepted, or processed a request, or that any payment was created, authorized, captured, settled, reconciled, or funded.

## Key takeaways

- Production Forward API use is subject to eligibility; the snapshot directs readers to an Account Manager or Business Development rather than establishing current merchant eligibility or production enablement.
- Before performing a transformation, Forward API type-checks it. The type-error section identifies the common top-level error as `Received invalid transformation. Does not type check`; its `message` includes `"transformation_error?": true`, the triggering `expression`, and a `type_errors` list. These are transformation-failure fields, not evidence of destination processing.
- The catalog says transformation results must be serializable as boolean, nil, number, or string. It also lists failures for invalid expiration-year or expiration-month inputs, unsupported character encoding, a non-numeric string passed for integer conversion, and an out-of-bounds slice range. Exact error strings and additional `message` fields remain in the raw table.
- The three documented type-error categories are invalid function arity, invalid argument type, and invalid function name. Function arguments are described as zero-indexed, and one transformation may return multiple type errors when multiple argument types are invalid or when arity and argument types are both invalid.

> [!warning] Example shape is not a required-schema claim
> The page says the body format resembles its JSON example. Do not infer additional requiredness, exclusivity, field ordering, or completeness beyond the explicitly described transformation-error fields and catalog entries.

> [!warning] No retry, downstream-success, or enablement contract
> This snapshot does not define a general retry policy, guarantee that correcting a transformation will produce destination success, establish downstream processing, or prove current production enablement.

## Detail locators

- Production eligibility and Account Manager or Business Development inquiry route: `**AVAILABILITY**`, raw lines 17-20.
- Illustrative response-body shape with `error`, nested `message`, transformation flag, expression, type-error list and `request-uuid`: opening JSON example, raw lines 22-34.
- Transformation-error catalog, serializable return-type constraint, function-input failures and error-specific additional fields: raw lines 35-45.
- Pre-transformation type check and common type-error fields: `## Type errors`, raw lines 48-54.
- Invalid-arity, invalid-argument-type and invalid-function-name categories, including zero-indexed arguments: type-error table, raw lines 54-58.
- Condition under which a transformation may return multiple type errors: raw line 60.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-forward-api]]
- General forwarding model: [[source-braintree-reference-forward-api-overview]]
- Distinct processor-connection route: [[braintree-orchestration]]

## Related raw API references

The following linked pages are navigation targets and were not read as factual evidence for this entry:

- [[raw/braintree/docs/reference/forward-api/functions-2026-09-16|Forward API function reference]]
- [[raw/braintree/docs/guides/extend/forward-api/transformations-2026-09-16|Forward API transformations guide]]

## Raw Sources

- [[raw/braintree/docs/reference/forward-api/transformation-errors-2026-09-16|Braintree Forward API transformation errors]] - fully read 2026-09-16 snapshot covering the response example, transformation-error catalog, pre-execution type checking and type-error categories
