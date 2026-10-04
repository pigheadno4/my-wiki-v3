---
title: "Braintree Forward API Overview"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/forward-api/overview"
raw_files:
  - "braintree/docs/reference/forward-api/overview-2026-09-16.md"
tags: [braintree, braintree-extend, forward-api, vault, payment-data-forwarding]
---

## Overview

This collected, unversioned Braintree Forward API overview describes forwarding raw payment data from the Braintree Vault to a third-party destination. The destination need not be a Braintree merchant, but the page defines it as a PCI-compliant entity that requires raw payment data. Production Forward API use is subject to eligibility. See [[braintree]] and [[braintree-forward-api]].

This is a retrieval entry for the forwarding model, not a replacement API specification. It does not establish that a destination authorized a merchant, accepted or processed a request, or created, authorized, captured, settled or funded a payment. Forward API is also separate from the processor-connection and transaction-lifecycle route indexed at [[braintree-orchestration]].

## Key takeaways

- Before forwarding, the developer writes a destination config that describes the HTTPS request the Forward API will make. Once that config exists, a caller sends an HTTPS request to Forward API that references the config and supplies a payment-method nonce or token used to look up Vault data.
- Forward API then makes the configured destination API request on the caller's behalf with the specified payment data and relays the destination response. The page says that, when the forwarding request succeeds, the Forward API response body includes the destination's full HTTPS response.
- The overview names transaction, loyalty/rewards and processing services as examples and says other integrations requiring raw payment information can potentially use the route. These are use-case orientations, not guarantees that a destination supports an operation or that a particular merchant is eligible.

> [!warning] Eligibility and account authority remain separate
> The 2026-09-16 snapshot says production use is subject to eligibility and routes inquiries to an Account Manager or Business Development. It does not prove current enablement, a usable production config, or the account/role permission required for a particular merchant.

> [!warning] Raw payment data requires an independently established security boundary
> The page identifies destinations as PCI-compliant entities and describes sending sensitive Vault-derived payment data over configured HTTPS requests. This sparse overview does not define credential handling, logging/redaction controls, client-versus-server placement, or how PCI compliance is established; do not treat forwarding or a relayed HTTP response as destination approval or payment-lifecycle evidence.

## Detail locators

- Forward API identity, Vault source and destination qualification: `# Forward API`, raw line 16.
- Example transaction, loyalty/rewards, processing and other use cases: `# Forward API`, raw lines 20-28.
- Production eligibility and Account Manager or Business Development inquiry route: `**AVAILABILITY**`, raw lines 31-36.
- Destination config purpose and setup-before-request sequence: `## How it works`, raw lines 41-47.
- Caller request, config reference and Vault lookup through a payment-method nonce or token: `## How it works`, raw lines 50-52.
- Destination request delegation, specified payment data and response relay: `## How it works`, raw lines 55-62.
- Simplified `httpbin.org` request/response illustration: `## Example`, raw lines 67-104.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-forward-api]]
- Distinct processor-connection route: [[braintree-orchestration]]

## Related raw API references

The following linked pages are navigation targets and were not read as factual evidence for this entry:

- [[raw/braintree/articles/control-panel/vault/overview-2026-09-16|Braintree Vault overview]]
- [[raw/braintree/docs/reference/forward-api/config-2026-09-16|Forward API configuration reference]]

## Raw Sources

- [[raw/braintree/docs/reference/forward-api/overview-2026-09-16|Braintree Forward API overview]] - fully read 2026-09-16 snapshot covering Vault-to-destination identity, production eligibility, config-based HTTPS forwarding and destination-response relay
