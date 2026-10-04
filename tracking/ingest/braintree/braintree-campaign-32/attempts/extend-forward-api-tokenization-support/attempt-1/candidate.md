---
title: "Braintree Forward API Tokenization Support"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/extend/forward-api/tokenization-support"
raw_files:
  - "braintree/docs/guides/extend/forward-api/tokenization-support-2026-09-16.md"
tags: [braintree, braintree-extend, forward-api, tokenization, network-tokens, tpan]
---

## Overview

This collected, unversioned Braintree developer guide describes optional Forward API conversion of a referenced payment method into Discover or Mastercard tokenized primary account number (TPAN) information for forwarding to a third party. It documents Braintree-side tokenization selection and restriction controls, not the third party's API contract or proof that a destination authorization, charge, settlement or funding action executed.

The snapshot was collected on 2026-09-16. It preserves the guide's eligibility notice, supported-network and region qualifications, conditional tokenization behavior, TSP restriction route and sandbox examples, but does not establish current availability, merchant approval, linked credentials or successful production execution.

## Key takeaways

- Production Forward API use is subject to eligibility. The guide separately says production tokenization requires approval and linked PayPal credentials, so possession of API keys, sandbox access or collection of this page does not establish production enablement.
- The snapshot states support for Discover and Mastercard TPANs. Discover is restricted to US-issued credit cards, PayPal accounts and Venmo accounts; Mastercard is restricted to credit cards issued in the European Union or United Kingdom and PayPal accounts. These are captured qualifications, not current eligibility proof.
- A Forward API config that supports `NetworkTokenizedCard` but not the supplied payment-method token or nonce's payment-method type causes tokenization to be attempted automatically. When the config supports both types, `tokenize_on_forward: true` selects tokenized-card information for forwarding. An attempt is not a guarantee that tokenization or the downstream request succeeds.
- Optional TSP options can limit what a third party can do with a TPAN; the guide illustrates `max_amount` by saying a much larger attempted charge would fail. The tokenization reference remains the route for the complete option and field contract.
- The captured capability table says neither network supports cryptogram-based authorizations. It says CVV-based authorization is required unless `expire_at` is specified, multiple authorizations are supported only when `expire_at` is specified, PayPal support is currently limited to channel-initiated billing agreements, and Venmo support is listed only for Discover.
- The Discover and Mastercard snippets call the Braintree sandbox forwarding endpoint with public/private-key authentication, a fake nonce, `debug_transformations` and inline test configuration. They demonstrate request shape and synthetic output only; they do not establish OAuth authority, production credential safety, current destination acceptance or a completed payment.

> [!warning] Eligibility and credentials are independent prerequisites
> The collected page makes production Forward API eligibility, tokenization approval and linked PayPal credentials separate conditions. Confirm current enablement and credential linkage with Braintree before production use.

> [!warning] Tokenization selection is not downstream execution
> `NetworkTokenizedCard`, `tokenize_on_forward` and TSP options govern Braintree's attempted tokenization and the information or restrictions used when forwarding. They do not establish that the third party accepted the request or performed an authorization, charge, settlement or funding action.

> [!warning] Keep live credentials and payment data out of examples and evidence
> The captured snippets use environment-variable placeholders, a fake nonce and sandbox debug transformations. Do not substitute or retain live keys, merchant IDs, nonces, card numbers or CVVs in source, logs or evidence artifacts.

## Detail locators

- Production Forward API eligibility and contact route: `**AVAILABILITY**`, raw lines 16-17.
- Supported TPAN networks, account/card geography and production approval plus linked-PayPal-credential prerequisite: paragraph after `**AVAILABILITY**`, raw line 19.
- Network capability matrix, including amount/TTL controls, authorization modes, multiple-use condition and PayPal/Venmo scope: `## Capabilities`, raw lines 22-33.
- `NetworkTokenizedCard` config type and `$cvv` variable: opening list under `## Usage`, raw lines 38-42.
- Automatic versus `tokenize_on_forward` selection and optional TSP restrictions: final paragraph under `## Usage`, raw line 44.
- Discover sandbox request and synthetic transformed output: `## Example - Discover TPAN`, raw lines 47-81.
- Mastercard sandbox request, EUR TSP option and synthetic transformed output: `## Example - Mastercard TPAN`, raw lines 84-119.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- Related destination example: [[source-braintree-extend-forward-api-hyperwallet]]

## Related raw API references

- [[raw/braintree/docs/reference/forward-api/overview-2026-09-16|Braintree Forward API overview]] - linked navigation-only route for general Forward API behavior and eligibility; not read as factual evidence for this source
- [[raw/braintree/docs/reference/forward-api/tokenization-2026-09-16|Braintree Forward API tokenization reference]] - linked navigation-only field and TSP option contract; not read as factual evidence for this source
- [[raw/braintree/docs/reference/forward-api/config-2026-09-16|Braintree Forward API config reference]] - linked navigation-only route for config `types`; not read as factual evidence for this source
- [[raw/braintree/docs/reference/forward-api/variables-2026-09-16|Braintree Forward API variables reference]] - linked navigation-only route for `$cvv`; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/guides/extend/forward-api/tokenization-support-2026-09-16|Braintree Forward API tokenization-support guide]] - complete collected guide covering eligibility, supported TPAN networks and regions, capability conditions, tokenization selection, TSP restrictions and sandbox examples
