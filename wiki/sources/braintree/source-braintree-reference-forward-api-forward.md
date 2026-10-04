---
title: "Braintree Forward API Forward Request Reference"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/forward-api/forward"
raw_files:
  - "braintree/docs/reference/forward-api/forward-2026-09-16.md"
tags: [braintree, braintree-extend, forward-api, api-reference, request-parameters, sandbox]
---

## Overview

This collected Braintree reference page lists the available keys on an incoming Forward API request and identifies the sandbox forwarding endpoint. It documents request construction and routing inputs, not an exhaustive end-to-end operation contract and not evidence that a destination received or accepted a request or that a payment was created, authorized, captured, settled, reconciled, or funded. This is Forward API evidence, not PayPal Orchestration evidence. See [[braintree]] and [[braintree-forward-api]].

## Key takeaways

- Production Forward API use is subject to eligibility; the page directs readers to an Account Manager or Business Development. The snapshot does not establish a merchant's current eligibility, production enablement, account readiness, role permissions, destination credentials, or usable production configuration.
- A caller can supply a `Trace-Id` header, whose value the page says appears in all logs for that request. Treat trace values as operational identifiers and avoid placing secrets or payment data in them.
- `merchant_id` and `method` are marked required. The merchant identifier selects the merchant whose Vault will be accessed, while `method` identifies the HTTP method for the destination request. `name` is the name of the endpoint receiving the card information and is used to look up which config applies to the request; it is required in production. The page lists these request fields but does not state the authentication scheme for the incoming call or guarantee destination delivery.
- Several controls are explicitly sandbox-only: per-request `client_cert` and `client_key`, inline `config` or `configs`, and `debug_transformations`. When `debug_transformations` is present, no request is sent to the destination; the API instead returns a representation of the request that otherwise would have been executed, with the prospective query string in `X-Query-String`.
- `cse_data` applies only to payment data captured through Braintree's deprecated client-side encryption integration. `sensitive_data` makes values available to transformations while the page says those values are not logged by Forward API; this statement is not a broader credential-storage, destination-logging, or response-redaction guarantee.
- The page routes nonce/token inputs, one-or-many configs, one-or-many destination URLs, overrides, request body/header/query-string maps, and variable aliases through parameter entries. Those routine schemas remain in the pinned raw rather than being reproduced here.

> [!warning] Eligibility and environment boundary
> The captured endpoint is the sandbox forwarding endpoint, and several fields are explicitly sandbox-only. Production use is eligibility-gated, `name` is required in production, and this page alone does not establish production access, configuration approval, credentials, permissions, or environment alignment.

> [!warning] Debug and logging boundaries
> `debug_transformations` deliberately does not send a destination request, so its returned representation is not delivery or payment evidence. The page's no-logging statement is limited to values supplied through `sensitive_data`; it should not be generalized to every request field, destination system, response, or external log.

## Detail locators

- Production eligibility and Account Manager or Business Development inquiry route: `# Forward > AVAILABILITY`, raw lines 17-18.
- Incoming-request identity, `POST`, and sandbox forwarding endpoint: `# Forward`, raw lines 20-23.
- Optional `Trace-Id` request tracer and its log correlation: `#### Trace-ID`, raw lines 26-28.
- Sandbox-only mutual-TLS certificate/private-key fields and inline single/multiple configuration selection: `#### Parameters`, raw lines 33-39.
- Deprecated client-side encryption qualification and `cse_data` transformation binding: `#### Parameters > cse_data`, raw lines 41-45.
- Caller `data` variables and sandbox-only `debug_transformations` no-send behavior: `#### Parameters`, raw lines 49-51.
- Required merchant Vault identity and destination HTTP method: `#### Parameters > merchant_id` and `method`, raw lines 53-61.
- Production-required endpoint/config name, override behavior, and body/header/query-string maps: `#### Parameters`, raw lines 65-73.
- Payment-method nonce/token inputs, one-indexed multiple-token binding, and Forward API no-logging statement for `sensitive_data`: `#### Parameters`, raw lines 75-81.
- Single or type-selected candidate destination URLs and variable aliases: `#### Parameters`, raw lines 83-87.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-forward-api]]
- Distinct processor-connection route: [[braintree-orchestration]]

## Related raw API references

- [[raw/braintree/docs/reference/forward-api/overview-2026-09-16|Forward API overview]] - navigation-only route linked for general Forward API context and production eligibility; not read as factual evidence for this source
- [[raw/braintree/docs/reference/forward-api/config-2026-09-16|Forward API config reference]] - navigation-only route for named/inline config and template details; not read as factual evidence for this source
- [[raw/braintree/docs/reference/forward-api/functions-2026-09-16|Forward API functions reference]] - navigation-only route for transformation variable lookup; not read as factual evidence for this source
- [[raw/braintree/docs/guides/extend/forward-api/cryptography-2026-09-16|Forward API cryptography guide]] - navigation-only route for mutual-TLS details; not read as factual evidence for this source
- [[raw/braintree/docs/guides/extend/forward-api/examples-2026-09-16|Forward API examples guide]] - navigation-only route for multiple-payment-method aliases; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/reference/forward-api/forward-2026-09-16|Braintree Forward API Forward request reference]] - complete collected request-reference snapshot covering production eligibility, sandbox endpoint, trace identity, request/config inputs, no-send debugging, required merchant/method fields, production naming and sensitive-data logging qualification
