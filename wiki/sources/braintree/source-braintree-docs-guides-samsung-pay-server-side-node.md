---
title: "Braintree Samsung Pay Server-Side Implementation (Node.js)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/samsung-pay/server-side/node"
raw_files:
  - "braintree/docs/guides/samsung-pay/server-side/node-2026-09-16.md"
tags: [braintree, samsung-pay, nodejs, server-side, deprecated]
---

## Overview

This 2026-09-16 Braintree website snapshot is a Node.js-routed server-side Samsung Pay guide. Its retained body marks Samsung Pay and the guide as deprecated, redirects readers to the distinct Pay Later offers guide, and provides no Node code or complete transaction procedure. [[braintree]] [[braintree-payment-methods]]

## Key takeaways

- Do not use this page as a current Samsung Pay implementation guide: it explicitly says Samsung Pay has been deprecated and directs readers to Pay Later offers. The redirect is replacement direction, not evidence that Pay Later is technically equivalent or that a migration procedure is supplied.
- The only remaining action-oriented content lists three places where a payment method could be stored: a separate payment-method create request; a separate customer create or update request; or a transaction sale request using `options.store_in_vault` or `options.store_in_vault_on_success`. The captured link labels are rendered as `linkToReferenceRequest` placeholders, so they identify navigation targets but do not establish exact Node SDK syntax or request schema.
- The page also navigates to a GraphQL server-side implementation, but that linked target was not read for this entry and supplies no behavioral evidence here.
- This snapshot does not document Samsung Pay client collection or Android behavior, merchant/account eligibility, enablement, environment configuration, an exact Node package or version, GitHub implementation/history, current support, or successful payment, vaulting, settlement, or funding.

## Detail locators

- Alternate GraphQL server-side route: raw line 18.
- Samsung Pay and guide deprecation plus Pay Later direction: raw lines 20-22.
- Listed payment-method storage request contexts and option names: raw lines 25-27.

## Related

- [[braintree]]
- [[braintree-payment-methods]]

## Related raw API references

The following are navigation targets named by the captured list; they were not read as evidence for this entry:

- [[raw/braintree/docs/reference/request/payment-method/create/node-2026-09-16|Payment Method Create request (Node.js)]]
- [[raw/braintree/docs/reference/request/customer/create/node-2026-09-16|Customer Create request (Node.js)]]
- [[raw/braintree/docs/reference/request/customer/update/node-2026-09-16|Customer Update request (Node.js)]]
- [[raw/braintree/docs/reference/request/transaction/sale/node-2026-09-16|Transaction Sale request (Node.js)]]

## Raw Sources

- [[raw/braintree/docs/guides/samsung-pay/server-side/node-2026-09-16|Braintree Samsung Pay Server-Side Implementation (Node.js), fetched 2026-09-16]]
