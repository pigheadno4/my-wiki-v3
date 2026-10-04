---
title: "Braintree Forward API Variables Reference"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/forward-api/variables"
raw_files:
  - "braintree/docs/reference/forward-api/variables-2026-09-16.md"
tags: [braintree, braintree-extend, forward-api, variables, transformations]
---

## Overview

This collected, unversioned Braintree Forward API reference defines how transformation strings resolve global, template and local variables while constructing an outbound destination request. It documents substitution and request-construction behavior, not destination authority, request acceptance, payment execution or transaction lifecycle state. Production Forward API use is subject to eligibility. See [[braintree]] and [[braintree-forward-api]].

This route is distinct from [[braintree-orchestration]], whose retained pages concern processor connections and Braintree transaction lifecycle operations.

## Key takeaways

- Most strings evaluate to themselves. Strings beginning with `$` instead perform global-variable or template lookups.
- Global lookups use `$variable_name`. When a name exists in multiple sources, precedence increases from Forward API-provided values, to the forwarding request's `data`, to its `sensitive_data`; therefore `sensitive_data` wins a same-name collision.
- Template lookups use a path such as `$/section/nested_section` to fetch part of the partially constructed request, serialize it under `request_format`, and return a string. Local lookups use `$/var/name`; `/var` is a non-serialized template section that cannot be supplied by either the config or forwarding request, and transformations can write values there for later lookup.
- For Apple Pay cards, this page says the underlying card information is unavailable: the card number is the DPAN and its expiration date is the DPAN expiration date, not the underlying card's.
- With multiple payment-method tokens, variables bind by 1-indexed token position. An unsuffixed variable and its `_1` form resolve to the first payment method. The captured sentence for forwarding both a payment method and a nonce is malformed, but indicates the nonce variables receive the `_2` suffix; use the linked example and forwarding-request reference for the complete request shape.

> [!warning] Production availability is qualified
> The 2026-09-16 snapshot says production Forward API use is subject to eligibility and routes inquiries to an Account Manager or Business Development. It does not establish current enablement, configuration approval or destination acceptance for a merchant.

> [!warning] Treat substituted data according to its sensitivity
> The precedence model includes a `sensitive_data` section, and substitutions may expose payment-method-derived values in a constructed destination request. This sparse page does not define client/server placement, credential storage, logging or redaction controls; those boundaries require the applicable Forward API configuration, destination and security authority.

> [!note] The captured global-variable inventory is empty
> The snapshot ends immediately after the `### Available Global Variables` heading. It therefore supports the lookup rules above but does not provide a recoverable name-by-name global-variable catalog.

## Detail locators

- Production eligibility and inquiry route: `**AVAILABILITY**`, raw lines 17-20.
- Literal-string behavior and `$` lookup trigger: below `# Variables`, raw line 22.
- Global lookup syntax, sources and collision precedence: below `# Variables`, raw line 26.
- Template lookup syntax, partial-request access and `request_format` serialization: below `# Variables`, raw line 30.
- Local `$/var/name` lookups, non-serialization and prohibition on config/request provision: below `# Variables`, raw lines 34-38.
- Local-variable definition and reuse examples: `### json`, raw lines 41-49.
- Apple Pay DPAN and expiration-date qualification: below the local-variable example, raw line 50.
- Multiple-payment-method suffix binding, 1-based positions and unsuffixed/`_1` equivalence: `### Variable suffixes`, raw line 55.
- Captured malformed nonce-suffix sentence: `### Variable suffixes`, raw line 59.
- Empty captured inventory heading: `### Available Global Variables`, raw lines 62-65.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-forward-api]]
- Distinct processor-connection route: [[braintree-orchestration]]

## Related raw API references

The following linked pages are navigation targets and were not read as factual evidence for this entry:

- [[raw/braintree/docs/reference/forward-api/overview-2026-09-16|Forward API overview]]
- [[raw/braintree/docs/guides/extend/forward-api/examples-2026-09-16|Forward API examples]]
- [[raw/braintree/docs/reference/forward-api/forward-2026-09-16|Forwarding request reference]]
- [[raw/braintree/docs/reference/forward-api/config-2026-09-16|Forward configuration and request-format reference]]

## Raw Sources

- [[raw/braintree/docs/reference/forward-api/variables-2026-09-16|Braintree Forward API variables reference]] - fully read 2026-09-16 snapshot covering production eligibility, global/template/local lookup behavior, precedence, DPAN qualification, suffix rules and the missing captured global-variable inventory
