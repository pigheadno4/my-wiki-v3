---
title: "Braintree Merchant Account Find (Node.js)"
type: source
date_ingested: 2026-09-21
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/merchant-account/find/node"
raw_files:
  - "braintree/docs/reference/request/merchant-account/find/node-2026-09-16.md"
tags: [braintree, node-js, merchant-accounts, lookup]
---

## Overview

This Braintree Node.js reference documents `gateway.merchantAccount.find()` for looking up one merchant account by an identifier. The callback exposes `err` and `merchantAccount`, while separate linked references route readers to response-object and not-found details.

## Key takeaways

- The example passes the literal `theMerchantAccountId` to `gateway.merchantAccount.find()`. It illustrates an account-ID lookup but does not define the identifier's format, origin, or validation rules.
- The callback receives `err` and `merchantAccount`; its body contains only the comment `handle result`. No response fields, success check, or error-handling implementation is shown.
- If the merchant account cannot be found, the page routes that outcome to Braintree's Node.js `notFoundError` reference. The exact exception details remain in the linked raw reference.
- This page documents single-account lookup only. It does not establish collection retrieval, account creation or updating, onboarding eligibility, approval, activation, funding, or other lifecycle behavior.

## Detail locators

- Merchant Account response-object route: `# Merchant Account: Find`, line 16.
- Identifier, lookup invocation and callback arguments: `# Merchant Account: Find > ### Node`, lines 21-23.
- Missing-account error route: line 25.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Related raw API references

- [[raw/braintree/docs/reference/response/merchant-account/node-2026-09-16|Braintree Node.js Merchant Account response reference]] - navigation-only response-object route linked by this page; not used as factual evidence here
- [[raw/braintree/docs/reference/general/exceptions/node-2026-09-16|Braintree Node.js exceptions reference]] - navigation-only destination for the linked `notFoundError`; not used as factual evidence here

## Raw Sources

- [[raw/braintree/docs/reference/request/merchant-account/find/node-2026-09-16|Braintree Node.js merchant-account find reference]] - complete collected page covering ID-based lookup, callback arguments, and the linked response and not-found routes
