---
title: "Braintree Extend Forward API Configuration"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/extend/forward-api/configuration"
raw_files:
  - "braintree/docs/guides/extend/forward-api/configuration-2026-09-16.md"
tags: [braintree, braintree-extend, forward-api, configuration, payment-data, sandbox]
---

## Overview

This collected Braintree Extend guide is a retrieval entry for configuring a Forward API request. It describes two JSON inputs: an incoming forward request that identifies the merchant, outgoing payment-method nonce or token, and destination URL; and a config that controls the outgoing request's format, structure, and transformations. The snapshot permits inline configs in sandbox but says production configs are reviewed and imported by Braintree and then referenced by name. This is request-construction and payment-data-forwarding documentation, not evidence that a destination accepted a request or that a payment was executed, authorized, captured, settled, or funded.

## Key takeaways

- Production Forward API use is subject to eligibility. The page directs the reader to an Account Manager or Business Development, so this snapshot does not establish a merchant's current access, approval, account readiness, or applicable role permission. See the separate Control Panel permission route below for collected role-level evidence.
- The incoming JSON request carries destination and payment-method references, while the config defines allowed request shape and transformations. In sandbox, a config can be supplied inline; in production, Braintree reviews and imports each config and the request references the stored config by name.
- The inline example uses Braintree public/private-key Basic authentication and shows a `$number` transformation placeholder replaced with credit-card data from the Vault. The named sandbox `braintree` config example separately places a private key under `sensitive_data`; these are illustrative request fields, not a general security, storage, redaction, or permission contract.
- In sandbox, setting `debug_transformations` to true prevents the outgoing request and returns the data that would have been sent. The displayed response includes a full test card number, so debug output can contain payment-card data and must not be treated as safe-to-log evidence. A debug response also does not prove destination reachability, payment execution, authorization, settlement, or funding.
- The page routes exact incoming-request parameters, config parameters, test nonces, and formatting, encoding, and encryption transformations to separate references. Those unread pages are navigation only here.

> [!warning] Eligibility, permission, and account scope
> This immutable 2026-09-16 snapshot says production Forward API use is subject to eligibility and that production configs are reviewed and imported. It does not establish current product availability, approval for a particular merchant, the Control Panel role needed to forward payment methods, or a usable production account/config. Verify those separately; the collected permission route is [[source-braintree-control-panel-users-roles-role-permissions]].

> [!warning] Forwarding is not payment outcome evidence
> Sending or previewing transformed payment data is not proof that the destination accepted the request or that any payment was created, authorized, captured, settled, reconciled, or funded. Even the page's named `braintree` sandbox config is an example described as creating transactions in Braintree sandbox, not retained runtime evidence of a successful transaction.

## Detail locators

- Production eligibility and Account Manager or Business Development inquiry route: `# Configuration > AVAILABILITY`, lines 16-17.
- Two JSON sources for configuration: `# Configuration`, lines 19-24.
- Incoming request identity and merchant, payment-method, and destination fields: `## Incoming Forward Request`, lines 26-30.
- Config purpose, sandbox inline-config behavior, production review/import, and name-based reference: `## Configs`, line 35.
- Inline curl request, Basic-auth environment keys, URL/method restrictions, request formatting, payment-method type, and `$number` transformation: `## Configs`, lines 36-59.
- Returned destination status, headers, body, and request time plus the Vault replacement explanation and config-reference route: `## Configs`, lines 60-70.
- Named `braintree` sandbox config example, including transaction destination, amount, `data`, and `sensitive_data`: `## Configs`, lines 70-87.
- Sandbox-only debug behavior, illustrative request, and returned full test card number: `## Debug Transformations`, lines 90-126.
- Postman collection navigation: `## Debug Transformations`, line 127.
- Test-nonce navigation: `## Test Nonces`, lines 130-132.
- Transformation formatting, encoding, and encryption navigation: `## Transformations`, lines 135-137.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- Role-permission route: [[source-braintree-control-panel-users-roles-role-permissions]]

## Related raw API references

- [[raw/braintree/docs/reference/forward-api/forward-2026-09-16|Forward API incoming request reference]] - navigation-only route for incoming-request parameters; not used as factual evidence here
- [[raw/braintree/docs/reference/forward-api/config-2026-09-16|Forward API config reference]] - navigation-only route for config parameters; not used as factual evidence here
- [[raw/braintree/docs/guides/extend/forward-api/transformations-2026-09-16|Forward API transformations guide]] - navigation-only route for formatting, encoding, and encryption; not used as factual evidence here
- [[raw/braintree/docs/reference/general/testing/node-2026-09-16|Braintree testing reference (Node.js route)]] - navigation-only route for test nonces; not used as factual evidence here

## Raw Sources

- [[raw/braintree/docs/guides/extend/forward-api/configuration-2026-09-16|Braintree Extend Forward API Configuration guide]] - complete collected guide for incoming-request and config composition, sandbox versus production config handling, debug transformations, and qualified production availability
