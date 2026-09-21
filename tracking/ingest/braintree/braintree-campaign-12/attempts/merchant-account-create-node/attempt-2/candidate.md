---
title: "Braintree Merchant Account Create (Node.js)"
type: source
date_ingested: 2026-09-21
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/merchant-account/create/node"
raw_files:
  - "braintree/docs/reference/request/merchant-account/create/node-2026-09-16.md"
tags: [braintree, node-js, merchant-accounts, marketplace, onboarding]
---

## Overview

This Braintree Node.js reference demonstrates `gateway.merchantAccount.create()` with callback and Promise forms. Its worked examples group individual and business identity, funding, terms acceptance, master-merchant association, and a requested merchant-account ID into one parameter object.

## Key takeaways

- Both examples supply individual and business identity categories, bank-oriented funding information, `tosAccepted`, `masterMerchantAccountId`, and `id`, then pass that example object to `gateway.merchantAccount.create()`. Use the raw locators for the exact example fields and values.
- The callback form exposes `err` and `result`; the Promise form resolves to `result`. Both handler bodies are empty, so this page does not show result fields, success validation, failure handling, or subsequent account state.
- These are worked examples, not a universal merchant-onboarding contract. The page does not state that every merchant can create merchant accounts, that every displayed field is universally required, or that invocation guarantees approval, activation, funding readiness, or transaction eligibility.
- The page links to a Merchant Account response object, a Braintree Marketplace overview, and service-fee transaction creation. Those references are navigation routes; their behavior is not imported into this fully read source.

> [!warning] Worked-example and eligibility boundary
> Preserve the examples as one documented Node.js request shape. Do not convert their sample identity, funding, agreement, master-merchant, or account-ID values into universal eligibility or required-field rules, and do not treat an empty callback or Promise handler as proof of a successful or usable account.

## Detail locators

- Merchant Account response-object route: `# Merchant Account: Create`, line 15.
- Callback example identity, business, funding, agreement, master-merchant and requested-ID inputs plus invocation/result arguments: `# Merchant Account: Create > ### Callback`, lines 21-60.
- Promise example with the same input categories and resolved `result`: `# Merchant Account: Create > ### Promise`, lines 67-106.
- Marketplace overview and service-fee transaction navigation routes: `## See also`, lines 113 and 115.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Related raw API references

- [[raw/braintree/docs/reference/response/merchant-account/node-2026-09-16|Braintree Node.js Merchant Account response reference]] - navigation-only response-object route linked by this page; not used as factual evidence here
- [[raw/braintree/docs/guides/braintree-marketplace/overview-2026-09-16|Braintree Marketplace overview]] - navigation-only marketplace route linked by this page; not used as factual evidence here
- [[raw/braintree/docs/guides/braintree-marketplace/create/node-2026-09-16|Braintree Marketplace service-fee transaction guide for Node.js]] - navigation-only service-fee route linked by this page; not used as factual evidence here

## Raw Sources

- [[raw/braintree/docs/reference/request/merchant-account/create/node-2026-09-16|Braintree Node.js merchant-account create reference]] - complete collected page covering callback and Promise creation examples, identity/business/funding/agreement input categories, result arguments, and related navigation
