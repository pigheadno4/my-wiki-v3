---
title: "Braintree Merchant Account All (Node.js)"
type: source
date_ingested: 2026-09-21
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/merchant-account/all/node"
raw_files:
  - "braintree/docs/reference/request/merchant-account/all/node-2026-09-16.md"
tags: [braintree, node-js, merchant-accounts, retrieval]
---

## Overview

This Braintree Node.js reference documents `gateway.merchantAccount.all()` returning a collection of Merchant Account objects through a callback. Its example iterates that collection and reads each account's `currencyIsoCode`.

## Key takeaways

- The page describes the result as a collection of Merchant Account objects and routes readers to the separate response-object reference for object details.
- The callback receives `err` and `merchantAccounts`; the example calls `forEach` on `merchantAccounts` and logs each `merchantAccount.currencyIsoCode`.
- The displayed callback does not inspect `err` or show an empty, failed, filtered, ordered, or paginated result. Do not infer those behaviors from this example.
- This is collection retrieval only. It does not establish merchant-account creation, updating, onboarding eligibility, approval, activation, or funding behavior.

> [!warning] Retrieval-only boundary
> Use this page to locate the Node.js all-accounts call and its displayed callback consumption. Do not import request inputs, eligibility rules, side effects, or lifecycle behavior from separate create or update operations.

## Detail locators

- Collection purpose and Merchant Account response-object route: `# Merchant Account: All`, line 15.
- Sandbox gateway setup placeholders: `# Merchant Account: All > ### Node`, lines 18-23.
- Callback arguments, collection iteration and `currencyIsoCode` access: `# Merchant Account: All > ### Node`, lines 25-29.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Related raw API references

- [[raw/braintree/docs/reference/response/merchant-account/node-2026-09-16|Braintree Node.js Merchant Account response reference]] - navigation-only response-object route linked by this page; not used as factual evidence here

## Raw Sources

- [[raw/braintree/docs/reference/request/merchant-account/all/node-2026-09-16|Braintree Node.js merchant-account all reference]] - complete collected page covering collection retrieval, callback arguments, account iteration, and displayed currency access
