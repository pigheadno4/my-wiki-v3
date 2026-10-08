---
title: "Braintree Dispute Response Reference (Node.js)"
type: source
date_ingested: 2026-10-08
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/response/dispute/node"
raw_files:
  - "braintree/docs/reference/response/dispute/node-2026-09-16.md"
tags: [braintree, node-js, disputes, response-objects]
---

## Overview

This collected Braintree website page is a Node.js-route response reference for the Dispute object. The captured body contains no response attributes; it preserves only a results-limitation notice and an account-access qualification.

## Key takeaways

- The page identifies itself as the Dispute response reference, but the captured body does not enumerate fields, statuses, methods, or request parameters.
- It states that results are limited according to the linked PayPal Data Protection Addendum for Card Processing Products. Because that external policy was not part of this source, this entry does not infer which results or fields are limited.
- It states that managing disputes through the API is available only to merchants who can access disputes in the Braintree Control Panel. This is an access qualification, not proof that a particular merchant currently has access.

> [!warning] Response object, not request operation or outcome proof
> This response-reference snapshot does not itself document how to find, search, accept, evidence, finalize, or otherwise change a dispute. It also does not prove a successful API call, lifecycle transition, evidence acceptance, bank review, settlement, or dispute outcome. The website's Node.js route label does not identify an exact SDK package or version.

## Detail locators

- Dispute response-reference heading: `# Dispute`, line 14.
- Results-limitation notice: `# Dispute > NOTE`, lines 17-18.
- Control Panel access qualification for API dispute management: `# Dispute > AVAILABILITY`, lines 21-22.

## Related

- Company: [[braintree]]
- Main concept: [[disputes]]

## Related raw API references

- [[raw/braintree/docs/reference/request/dispute/find/node-2026-09-16|Braintree Node.js Dispute find request reference]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/reference/request/dispute/search/node-2026-09-16|Braintree Node.js Dispute search request reference]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/reference/request/dispute/accept/node-2026-09-16|Braintree Node.js Dispute accept request reference]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/reference/request/dispute/add-text-evidence/node-2026-09-16|Braintree Node.js Dispute add-text-evidence request reference]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/reference/request/dispute/remove-evidence/node-2026-09-16|Braintree Node.js Dispute remove-evidence request reference]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/reference/request/dispute/finalize/node-2026-09-16|Braintree Node.js Dispute finalize request reference]] - navigation only; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/reference/response/dispute/node-2026-09-16|Braintree Dispute response reference - Node.js route]] - complete collected page containing the response-reference identity, results-limitation notice and Control Panel access qualification
