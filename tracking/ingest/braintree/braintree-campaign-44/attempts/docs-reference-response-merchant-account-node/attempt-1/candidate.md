---
title: "Braintree Merchant Account Result Response Reference (Node.js)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/response/merchant-account/node"
raw_files:
  - "braintree/docs/reference/response/merchant-account/node-2026-09-16.md"
tags: [braintree, node-js, merchant-accounts, marketplace, response-objects]
---

## Overview

This collected 2026-09-16 Braintree website page is the Node.js response-reference route for a Merchant Account result object. It distinguishes successful and unsuccessful results: the shown successful sub-merchant result is returned with `pending` status and its master merchant account, while validation failures return `success` as false with errors. In production, the page describes third-party verification after the pending result and directs the integrator to use a confirmation webhook for the later response.

## Key takeaways

- A successful result exposes the sub-merchant and master merchant account and shows the sub-merchant as `pending`; the page says to expect a confirmation webhook within several minutes and separately describes a minute-or-two production delay, so those captured timings are guidance rather than a guaranteed completion time.
- The production explanation attributes the pending state to third-party verification, risk checks and underwriting; webhook handling is the documented way to receive and confirm the later outcome.
- An unsuccessful result has `success` set to false when validations prevent onboarding, and invalid parameters place validation errors on the result object.
- The status reference calls `pending` transitory and says verification leads to `active` or `suspended`: `active` can process transactions, while `suspended` cannot.

## Detail locators

- Result-object identity and successful/unsuccessful split: `## Result Object`, lines 17-20.
- Successful pending result, confirmation-webhook expectation and returned sub/master merchant accounts: `### Successful result`, lines 20-26; Node example at lines 29-36.
- Production verification rationale, stated timing and webhook handoff: `### Successful result`, line 28.
- Unsuccessful validation condition, sandbox-test navigation and validation-error behavior: `### Unsuccessful result`, lines 38-48.
- Pending, active and suspended status meanings and processing consequences: `### Statuses`, lines 53-64.

## Scope and boundaries

> [!warning] This is a captured Node.js documentation-family response page, not evidence for an exact SDK package or version, current Marketplace availability, or merchant eligibility. It describes result states and a later confirmation handoff rather than an account-create or update request; neither a returned object nor the captured timing text proves account creation, approval, webhook delivery, processing readiness, a transaction outcome, settlement or funding for an individual account.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-marketplace]]
- Separate confirmation-step guide: [[source-braintree-marketplace-guide-confirmation-node]]
- Separate webhook event reference: [[source-braintree-webhooks-sub-merchant-account-node]]

## Raw Sources

- [[raw/braintree/docs/reference/response/merchant-account/node-2026-09-16|Braintree Merchant Account response reference - Node.js]] - complete collected page covering result success/failure, pending verification and the three documented status consequences
