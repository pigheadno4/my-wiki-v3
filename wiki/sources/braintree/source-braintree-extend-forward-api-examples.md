---
title: "Braintree Forward API Examples"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/extend/forward-api/examples"
raw_files:
  - "braintree/docs/guides/extend/forward-api/examples-2026-09-16.md"
tags: [braintree, braintree-extend, forward-api, transformations, vault, sandbox]
---

## Overview

This Braintree Extend guide is an examples catalog for constructing Forward API destination requests with functions, transformations, caller-supplied values, Vault-derived payment data and request overrides. Its calls target the Braintree forwarding sandbox and `httpbin.org`; they illustrate request construction and returned debug output, not successful payment execution, downstream acceptance, or merchant authority at a destination. Production use of the Forward API remains eligibility-gated. See [[braintree]] and [[braintree-forward-api]].

## Key takeaways

- Forward API functions can be nested to construct values such as destination HTTP Basic authorization, and global variables used by that example are supplied per forwarding request under `sensitive_data` or `data`. The page does not establish a complete credential-handling policy or destination permission model.
- Transformations can populate body, header and URL-parameter paths. An `override` supplies a request baseline: non-empty override values take precedence over conflicting transformations, while unaffected content passes through to the destination.
- Conditional transformations use `if_defined`; the guide also demonstrates XML sibling indices and attributes, multi-payment-method suffixes or aliases, and append index `-1`. These are example configurations, not guarantees about a particular destination API.
- Braintree states that it does not store CVVs for vaulted payment methods. When a destination requires CVV with vaulted card data, the documented example combines the long-lived payment-method token with a CVV-only payment-method nonce and reads the suffixed CVV variable.
- `/var` binds an intermediate value only for the current transformation. It can be reused in later rules but is not itself emitted to an outbound body, header or URL parameter.

## Detail locators

- `## Functions` and `### Nested functions` — `join`, `array` and `base64` composition examples.
- `## HTTP basic auth` — destination Authorization-header construction, per-request variable placement, sandbox request and debug output.
- `## Trace-ID` — request tracer header and log-correlation statement.
- `## Hashed data` — hash/template/override example and XML serialization.
- `## Transformations and overrides` — precedence and pass-through behavior.
- `## Conditional transformations` — `if_defined` behavior and captured test-nonce qualification.
- `## XML sibling elements sharing a name` and `## XML attributes` — XML path examples.
- `## CVV with vaulted card data` — token plus CVV-only nonce route and variable suffixing.
- `## Forwarding multiple payment methods` and `## Forwarding multiple payment methods with aliases` — suffix, alias, conditional membership and append-index examples.
- `## Variable binding` — transformation-local `/var` lifetime and reuse.

## Related raw API references

The following are navigation targets named by this page and were not read as evidence for this entry:

- [[raw/braintree/docs/reference/forward-api/overview-2026-09-16|Forward API overview]]
- [[raw/braintree/docs/reference/forward-api/functions-2026-09-16|Forward API function reference]]
- [[raw/braintree/docs/reference/forward-api/variables-2026-09-16|Forward API variables reference]]
- [[raw/braintree/docs/reference/forward-api/forward-2026-09-16|Forward request reference]]
- [[raw/braintree/docs/reference/forward-api/config-2026-09-16|Forward configuration reference]]
- [[raw/braintree/docs/guides/extend/forward-api/transformations-2026-09-16|Forward transformations guide]]
- [[raw/braintree/docs/guides/extend/forward-api/cryptography-2026-09-16|Forward cryptography guide]]

## Raw Sources

- [[raw/braintree/docs/guides/extend/forward-api/examples-2026-09-16|Braintree Forward API examples (2026-09-16 snapshot)]]
