---
title: "Braintree Forward API Transformations"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/extend/forward-api/transformations"
raw_files:
  - "braintree/docs/guides/extend/forward-api/transformations-2026-09-16.md"
tags: [braintree, braintree-extend, forward-api, transformations, dsl]
---

## Overview

This collected Braintree Extend guide explains how a Forward API configuration uses ordered transformations and a small domain-specific language (DSL) to construct parts of an outbound destination request from payment-method data, caller values and intermediate variables. It documents request-construction semantics, not evidence that the destination authorized the merchant, accepted or processed the request, executed a payment, or settled funds. Production use of Forward API is subject to eligibility. See [[braintree]] and [[braintree-forward-api]].

## Key takeaways

- A config's `transformations` key controls where payment-method data is inserted into outbound forwarding requests. Transformations run in listed order, so later rules can use values produced for further transformation; the guide's PAN/CVV and authorization-header snippets are construction examples, not destination requirements or successful-request evidence.
- Transformation paths target four base locations: `/body`, `/header`, `/urlparam` and `/var`. The first three build the destination body, headers and query string, while `/var` temporarily stores a transformation result for reuse. Nested body paths depend on the configured request format.
- Hierarchical path output is content-type aware. The page shows JSON, XML and URL-encoded results, but says hierarchy is undefined for URL encoding; bracketed PHP-style field names must instead be written explicitly in the path.
- Numeric path indices are zero-based for JSON-array elements or XML siblings. An index of `-1` appends to an array or sibling set; the page identifies variable-count payment-method forwarding as a primary use and routes the full example elsewhere.
- In the DSL, JSON primitives generally evaluate to themselves, arrays represent function calls, and all arguments are evaluated before the function runs. Literal arrays therefore use the `array` function. Strings beginning with `$` resolve variables or parts of the outbound forwarding request.
- The outermost transformation function must return a boolean, number, null or string. A transformation writing to a local variable is the exception and may return any type. Exact function signatures and variable behavior remain in their separate reference pages.

> [!warning] Production eligibility is separate
> The collected page states that production Forward API use is subject to eligibility. A configuration example, raw snapshot or sandbox capability does not establish production approval or current account enablement.

> [!warning] Forwarding configuration is not payment or settlement proof
> These transformations construct outbound request content. They do not establish destination-side merchant authority, credential validity, acceptance, payment authorization or capture, settlement, payout or funding. Destination-specific permissions and behavior require their own current authority and execution evidence.

> [!warning] Treat transformed values as sensitive
> The page demonstrates transformations involving PAN, CVV, usernames and passwords. It does not provide a complete secret-handling policy. Keep real credentials and payment data out of source, logs and evidence artifacts, and use the applicable destination and Braintree security requirements.

## Detail locators

- Production eligibility qualification and contact routes: `**AVAILABILITY**`, raw lines 16-17.
- Ordered transformation semantics, config key and PAN/CVV encoding example: introduction below `# Transformations`, raw lines 19-27.
- Four base paths, request-construction roles, temporary `/var` storage and request-format-dependent nested paths: `## Path`, raw lines 30-55.
- Zero-based indices, JSON-array/XML-sibling examples and append index `-1`: `### Numerical indices`, raw lines 58-94.
- Authorization-header construction example, function-array syntax, eager argument evaluation and literal-array rule: `## Functions`, raw lines 97-115.
- `$` variable references and outermost return-type constraint, including the local-variable exception: `## Types`, raw lines 118-120.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-forward-api]]

## Related raw API references

The following are navigation targets named by this page and were not read as factual evidence for this entry:

- [[raw/braintree/docs/reference/forward-api/overview-2026-09-16|Forward API overview]]
- [[raw/braintree/docs/reference/forward-api/config-2026-09-16|Forward configuration reference]]
- [[raw/braintree/docs/guides/extend/forward-api/cryptography-2026-09-16|Forward cryptography guide]]
- [[raw/braintree/docs/guides/extend/forward-api/examples-2026-09-16|Forward API examples]]
- [[raw/braintree/docs/reference/forward-api/functions-2026-09-16|Forward API function reference]]
- [[raw/braintree/docs/reference/forward-api/variables-2026-09-16|Forward API variables reference]]
- [[raw/braintree/docs/guides/extend/forward-api/tokenization-support-2026-09-16|Forward API tokenization-support guide]]

## Raw Sources

- [[raw/braintree/docs/guides/extend/forward-api/transformations-2026-09-16|Braintree Forward API transformations guide]] - fully read 2026-09-16 snapshot covering eligibility, paths, indices, DSL function evaluation and type constraints
