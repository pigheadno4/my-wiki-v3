---
title: "Braintree Result Objects (Node.js)"
type: source
date_ingested: 2026-09-23
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/general/result-objects/node"
raw_files:
  - "braintree/docs/reference/general/result-objects/node-2026-09-16.md"
tags: [braintree, node-js, result-objects, validation-errors, processor-responses]
---

## Overview

This Braintree Node.js reference explains result objects as API-call wrappers that report success and, on successful calls, contain the requested target data. It distinguishes that wrapper from the collection returned by calls without validations, such as searches, and separates validation-error details from other unsuccessful-result causes.

## Key takeaways

- A result object indicates whether the API call succeeded and includes the requested data when successful. On a successful result, `result.success` is true and the target object is a member of the result object.
- Calls that do not have validations, with searches given as the example, return a collection of requested objects instead of a result object. This page does not establish that every Braintree call returns the same shape.
- For an unsuccessful call, `result.success` is false. The page identifies invalid-parameter validation errors, processor declines, gateway rejections, and other exceptional conditions as possible causes.
- `result.errors` is populated only when the failure is caused by validation. Therefore, a false `success` value does not by itself establish that validation errors or `deepErrors()` are available for a processor decline, gateway rejection, or exceptional condition.
- The full callback and Promise validation examples, nested error traversal, message and submitted-parameter behavior, and transaction-specific error route remain at the raw locators below.

## Evidence limitation

> [!warning] Damaged collected version text
> The Message section's version sentence contains the unresolved template `{{sdkVersionForDate "Jul09_2010"}}`. This source does not reconstruct an SDK version or turn the damaged text into a current-version requirement.

## Detail locators

- Result-wrapper purpose and collection return for calls without validations: `# Result Objects`, lines 14-18.
- Successful `result.success` value and target-object membership: `## Success results`, lines 21-27.
- Unsuccessful `success` value and validation, processor-decline, gateway-rejection and exceptional-condition categories: `## Error results`, lines 29-34.
- Node false-result and validation-error access plus the validation-only `errors` qualification: `## Error results > ### Node.js`, lines 37-42.
- Callback and Promise examples for flattened and nested validation errors: `## Error results > ### Callback` and `### Promise`, lines 43-113.
- Transaction-specific error-result route: `## Error results`, line 114.
- Human-readable message, multiple-message behavior and damaged SDK-version template: `### Message`, lines 115-124.
- Submitted-parameter behavior and omitted credit-card number/CVV qualification: `### Params`, lines 127-134.
- Ruby-specific result-object links plus validation and search navigation: `## See Also`, lines 135-141.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/general/result-objects/node-2026-09-16|Braintree Node.js result-objects reference]] - complete collected page covering result success, non-result search collections, failure categories, validation-error access, examples, and damaged version text
