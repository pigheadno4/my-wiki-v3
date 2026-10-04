---
title: "Braintree Forward API Config"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/forward-api/config"
raw_files:
  - "braintree/docs/reference/forward-api/config-2026-09-16.md"
tags: [braintree, forward-api, configuration, api-reference]
---

## Overview

This collected 2026-09-16 unversioned Braintree reference page defines a Forward API config as the description of a third-party destination's request encoding, HTTP method, and payment-data injection. It is a configuration reference for [[braintree-forward-api]], not the processor-connection and transaction-lifecycle model documented under [[braintree-orchestration]]. Production Forward API use is subject to eligibility; the page directs readers to an Account Manager or the Business Development inquiry route for more information.

## Key takeaways

- In production, a JSON file is sent for each config for Braintree review, approval, and loading. In sandbox, the config may instead be included inline with a forwarding request, or supplied as a JSON file.
- A loaded config can be identified by name in both sandbox and production.
- The page's JSON example illustrates one config containing method, name, request-format, transformation, payment-type, and URL-pattern fields. It is an example, not a complete or universally required schema, and it does not establish destination acceptance or a payment outcome.
- This page does not document credential exchange, client-versus-server integration, authorization, capture, void, refund, settlement, or other destination lifecycle behavior; those claims require separate authority and evidence.

## Detail locators

- `AVAILABILITY` (lines 17-20): production eligibility and contact routes.
- Introductory config text and bullets (lines 22-28): config identity, production review/load, sandbox inline option, and post-load name lookup.
- `Example` / `json` (lines 36-55): illustrative config object and field values.

## Related

- [[braintree]] - provider company and broader source catalog
- [[braintree-forward-api]] - Forward API request-construction, transformation, and security retrieval hub
- [[source-braintree-reference-forward-api-overview]] - Forward API identity, HTTPS delegation, and destination-response boundary
- [[source-braintree-reference-forward-api-forward]] - incoming forwarding-request reference, including config selection and environment-qualified controls

## Raw Sources

- [[raw/braintree/docs/reference/forward-api/config-2026-09-16|Braintree Forward API Config (collected 2026-09-16)]]
