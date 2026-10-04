---
title: "Braintree Forward API Direct Tokenization Reference"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/forward-api/direct-tokenization"
raw_files:
  - "braintree/docs/reference/forward-api/direct-tokenization-2026-09-16.md"
  - "braintree/docs/guides/extend/forward-api/tokenization-support-2026-09-16.md"
tags: [braintree, forward-api, direct-tokenization, tpan, network-token, pci]
---

## Overview

This collected, unversioned Braintree reference documents direct tokenization through a Forward API `/tsp` endpoint: a request identifies the merchant Vault and a payment instrument by nonce or token, and the endpoint generates tokenized PAN data. It is a token-data retrieval operation, not a destination payment request and not evidence of authorization, capture, settlement or funding. It is also distinct from [[braintree-orchestration]], where transaction operations and processor-connection lifecycle are documented separately.

The snapshot was collected on 2026-09-16. It documents the sandbox endpoint and synthetic sandbox output, while production Forward API use remains subject to eligibility and this endpoint separately requires pre-approval. It does not establish current availability, merchant approval, production credentials or a successful tokenization.

## Key takeaways

- The captured operation is `POST https://forwarding.sandbox.braintreegateway.com/tsp`. The required `merchant_id` identifies the merchant whose Vault is accessed; `payment_method_nonce` and `payment_method_token` are the documented payment-instrument selectors.
- The endpoint requires pre-approval; the page says an unapproved request receives HTTP 403. Production Forward API use is independently subject to eligibility, so sandbox access, credentials or this snapshot do not establish production enablement.
- Braintree warns that PCI treats tokenized PANs (TPANs) as PANs. Handle returned numbers with the same care and compliance as credit-card numbers; do not retain them in logs, examples or review artifacts.
- `expire_at` allows any number of uses until an ISO 8601 date/time but does not set the card expiration month or year. `currency_code`, `expire_at` and `max_amount` are stated to be enforced only for Discover TPANs.
- `require_cryptogram: true` returns a cryptogram instead of a dynamic CVV and is stated to be compatible only with Visa network tokens; its default is false. The direct endpoint includes a Visa network-token example, while the fully read Forward API tokenization-support guide says Forward API currently supports Discover and Mastercard TPANs. Treat these as different documented surfaces and do not infer Visa forwarding support from the direct-tokenization example; confirm current product scope with Braintree.
- In sandbox, the TSP returns test values for card number, CVV, expiration month and expiration year. The examples authenticate with Braintree public/private key environment variables in curl; the page does not document a browser/client-side credential flow.

> [!warning] Approval and eligibility are separate gates
> Production Forward API use is subject to eligibility, and this direct-tokenization endpoint separately requires pre-approval. A 403 is the documented result when endpoint approval is absent.

> [!warning] Returned TPANs remain payment-card data
> The page explicitly says PCI views TPANs as PANs. Keep live credentials, nonces, tokens, TPANs, CVVs and cryptograms out of source, browser code, logs and evidence artifacts.

> [!warning] Preserve the product-surface boundary
> This direct `/tsp` operation returns tokenized PAN data. It does not itself document a forwarded destination request, a payment outcome or an Orchestration processor transaction. Its Visa example must not be generalized into Visa support for the sibling Forward API tokenization-support flow.

## Detail locators

- Production Forward API eligibility and contact route: `# Direct Tokenization > AVAILABILITY`, raw lines 16-17.
- Direct-tokenization purpose and sandbox `/tsp` POST endpoint: opening paragraph, raw lines 19-22.
- Endpoint pre-approval, HTTP 403 behavior and PCI treatment of TPANs: `IMPORTANT`, raw lines 23-24.
- `device_data`, required `merchant_id`, payment-method nonce/token selectors and TSP options: `#### Parameters`, raw lines 27-41.
- Discover-qualified `currency_code`, `expire_at` and `max_amount` behavior: TSP fields, raw lines 43-47.
- Visa-only cryptogram option and false default: `require_cryptogram`, raw line 49.
- Synthetic sandbox-return boundary: `### Tokenization in the sandbox environment`, raw lines 54-56.
- Discover sandbox curl request and example response: `## Example - Discover TPAN`, raw lines 59-70.
- Visa network-token sandbox curl request and example response: `## Example - Visa network token`, raw lines 74-89.
- Related Forward API guide's Discover/Mastercard scope and production prerequisites: tokenization-support raw, lines 16-19; capability qualifications at lines 22-33.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-forward-api]]
- Related support guide: [[source-braintree-extend-forward-api-tokenization-support]]
- Distinct processor-connection lifecycle: [[braintree-orchestration]]

## Related raw API references

- [[raw/braintree/docs/reference/forward-api/overview-2026-09-16|Braintree Forward API overview]] - linked navigation-only route for general Forward API behavior and eligibility; not read as factual evidence for this source
- [[raw/braintree/docs/guides/payment-method-nonces-2026-09-16|Braintree payment-method nonce guide]] - linked navigation-only route for nonce lifecycle; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/reference/forward-api/direct-tokenization-2026-09-16|Braintree Forward API direct-tokenization reference]] - complete collected reference for endpoint identity, approval and PCI warnings, inputs, TSP controls and sandbox examples
- [[raw/braintree/docs/guides/extend/forward-api/tokenization-support-2026-09-16|Braintree Forward API tokenization-support guide]] - complete related authority used only to preserve the direct-endpoint versus forwarding-support scope boundary
