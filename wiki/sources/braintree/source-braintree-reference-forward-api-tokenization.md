---
title: "Braintree Forward API Tokenization Reference"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/forward-api/tokenization"
raw_files:
  - "braintree/docs/reference/forward-api/tokenization-2026-09-16.md"
tags: [braintree, braintree-extend, forward-api, tokenization, network-tokens, tpan]
---

## Overview

This collected, unversioned Braintree Forward API reference shows sandbox request examples that ask Braintree to tokenize a payment-method nonce on forward and place network-tokenized-card number and CVV values into a JSON request body. The examples cover Discover and Mastercard TPAN shapes, use Braintree public/private-key authentication and a merchant ID, enable debug transformations, and send to `httpbin.org`; they are request-construction examples rather than evidence of a destination authorization or completed payment. Production Forward API use is subject to eligibility. See [[braintree]] and [[braintree-forward-api]].

This Forward API operation is distinct from [[braintree-orchestration]], whose retained route concerns processor connections and Braintree transaction lifecycle operations. Nothing in this tokenization reference establishes Orchestration configuration or execution.

## Key takeaways

- Both captured examples POST to the Braintree sandbox forwarding endpoint with `tokenize_on_forward: true`, an inline config accepting `NetworkTokenizedCard`, and transformations that write `$number` and `$cvv` into the outbound JSON body. The returned number/CVV snippets are debug-example output, not proof that a destination accepted or processed a payment.
- The Mastercard example adds `tsp.currency_code: "EUR"`; this page presents that value in an example and does not state that it is a universal requirement.
- For a Discover TPAN authorization, the page says the generated CVV is required unless `expire_at` was set and omission results in a decline. It also says a TPAN has no associated postal code and that supplying any postal code produces AVS response `M (matches)`.
- Attempting tokenization for an unsupported or invalid payment instrument returns the linked Forward API error response. The complete error catalog remains in that separate reference.

> [!warning] Production eligibility is separate from the sandbox examples
> The page states that production Forward API use is subject to eligibility. A captured request shape, sandbox response, API key pair or merchant ID does not establish production enablement.

> [!warning] Protect credentials and transformed payment data
> The examples contain private-key authentication and transformed card/CVV fields. Keep live credentials, merchant IDs, nonces, card data and CVVs out of source pages, logs and evidence artifacts. This sparse reference does not define a client/server integration boundary.

## Detail locators

- Production eligibility and contact route: `**AVAILABILITY**`, raw lines 17-20.
- Discover sandbox endpoint, curl authentication placeholders, merchant ID, fake nonce, debug/tokenization flags, inline config and `$number`/`$cvv` transformations: `## Example - Discover TPAN`, raw lines 27-68.
- Mastercard sandbox request, example EUR TSP currency and transformed output: `## Example - Mastercard TPAN`, raw lines 70-112.
- Discover generated-CVV requirement, `expire_at` exception and postal-code/AVS behavior: `## AVS and CVV`, raw lines 117-119.
- Unsupported or invalid instrument error route: `## Errors`, raw lines 122-124.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-forward-api]]
- Distinct processor-connection route: [[braintree-orchestration]]

## Related raw API references

The following linked pages are navigation targets and were not read as factual evidence for this entry:

- [[raw/braintree/docs/reference/forward-api/overview-2026-09-16|Forward API overview]]
- [[raw/braintree/docs/reference/forward-api/tokenization-errors-2026-09-16|Forward API tokenization errors]]
- [[raw/braintree/docs/reference/general/processor-responses/avs-cvv-responses-2026-09-16|AVS and CVV processor responses]]

## Raw Sources

- [[raw/braintree/docs/reference/forward-api/tokenization-2026-09-16|Braintree Forward API tokenization reference]] - fully read 2026-09-16 snapshot covering production eligibility, Discover and Mastercard sandbox TPAN examples, Discover CVV/AVS behavior and the invalid-instrument error route
