---
title: "Braintree Merchant Account Create For Currency (Node.js)"
type: source
date_ingested: 2026-09-21
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/merchant-account/create-for-currency/node"
raw_files:
  - "braintree/docs/reference/request/merchant-account/create-for-currency/node-2026-09-16.md"
tags: [braintree, node-js, merchant-accounts, braintree-auth, multi-currency]
---

## Overview

This Braintree Node.js reference documents the currency-specific `gateway.merchantAccount.createForCurrency()` operation. The method is available only to merchants using Braintree Auth; this source does not establish general merchant onboarding eligibility.

## Key takeaways

- The callback and Promise examples initialize `BraintreeGateway` with a merchant access token, pass a currency to `createForCurrency()`, and, on a successful result, access the created merchant account's `currencyIsoCode`.
- The operation is specifically merchant-account creation for a currency under Braintree Auth. It should not be treated as the general merchant-account creation operation or as evidence that every merchant can create accounts for arbitrary currencies.
- An unsupported currency returns a validation error. The linked validation-error and currency-support guides own the supported-currency and error details; they were not read as factual evidence for this source.

## Detail locators

- Braintree Auth availability restriction: `# Merchant Account: Create For Currency > AVAILABILITY`, lines 18-19.
- Callback input and result handling: `# Merchant Account: Create For Currency > ### Callback`, lines 24-39.
- Promise input and result handling: `# Merchant Account: Create For Currency > ### Promise`, lines 41-56.
- Unsupported-currency validation and currency-support routes: `# Merchant Account: Create For Currency`, line 57.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Related raw API references

- [[raw/braintree/docs/reference/response/merchant-account/node-2026-09-16|Braintree Node.js Merchant Account response reference]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/guides/braintree-auth/overview-2026-09-16|Braintree Auth overview]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/guides/braintree-auth/reference/node-2026-09-16|Braintree Auth Node.js validation-error reference]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/guides/braintree-auth/multi-currency/node-2026-09-16|Braintree Auth Node.js multi-currency guide]] - navigation only; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/reference/request/merchant-account/create-for-currency/node-2026-09-16|Braintree Node.js merchant-account create-for-currency reference]] - complete collected page covering Braintree Auth availability, currency input, callback and Promise result handling, and the unsupported-currency validation route
