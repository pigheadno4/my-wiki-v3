---
title: "Braintree SEPA Direct Debit Server-Side Implementation (Node.js)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/sepa-direct-debit/server-side/node"
raw_files:
  - "braintree/docs/guides/sepa-direct-debit/server-side/node-2026-09-16.md"
tags: [braintree, sepa, direct-debit, node-js, server-sdk, transactions]
---

## Overview

This 2026-09-16 Braintree website snapshot is a Node.js-routed server-side implementation guide for creating a SEPA Direct Debit transaction through Transaction Sale with a nonce or vaulted payment method and client-collected device data. It reports EUR-only support and routes transaction-status webhook setup. The page names no exact Node package version and does not establish current availability, merchant enablement, environment success, a completed debit, settlement or funding.

## Key takeaways

- The page says transaction creation accepts a nonce or vaulted payment method and instructs the merchant to include device data collected on the client side. This is the server-processing step after a separate client collection flow; it does not document client tokenization or mandate acceptance.
- Callback and Promise examples invoke `gateway.transaction.sale()` with amount, payment-method nonce, EUR merchant-account identifier, order and descriptor values, client-collected device data and `submitForSettlement: true`. Both examples label settlement submission `Required`; because that wording is an inline example comment rather than a separately stated universal rule, retain it as specific to this SEPA guide rather than generalizing it to every Braintree transaction.
- The prose identifies merchant-generated order ID and the bank-statement descriptor as optional fields. Exact field spellings and both complete request/result-handling examples remain at the raw locators.
- The captured page says SEPA Direct Debit supports only EUR and points to general and transaction-specific webhook documentation for transaction status changes, including sales and refunds. Those links are navigation rather than evidence that a webhook is configured, delivered or successfully handled.

## Material warning

> [!warning] Method-specific settlement instruction
> Both displayed SEPA sale examples mark `submitForSettlement: true` as required, while the generic [[braintree-server-sdk]] concept says immediate settlement submission is optional across the broader transaction model. Treat the example annotation as this guide's SEPA-specific instruction unless a fully read authority resolves the scope; do not convert it into a provider-wide SDK requirement.

## Detail locators

- Nonce-or-vaulted-method transaction creation and client-collected device-data instruction: `## Creating transactions`, raw line 19.
- Optional order ID and statement-descriptor fields: `### Optional fields`, raw lines 20–26.
- Callback Transaction Sale example and its settlement-submission annotation: `### Callback`, raw lines 27–50.
- Promise Transaction Sale example and its settlement-submission annotation: `### Promise`, raw lines 52–75.
- EUR-only statement: `## Currency support`, raw lines 77–79.
- Status-change webhook statement and sales/refunds reference routes: `## SEPA Direct Debit webhooks`, raw lines 80–84.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Supporting server concept: [[braintree-server-sdk]]
- Supporting notification concept: [[braintree-webhooks]]
- SEPA lifecycle and mandate overview: [[source-braintree-docs-guides-sepa-direct-debit-overview]]
- Complementary client route: [[source-braintree-docs-guides-sepa-direct-debit-client-side-javascript-v3]]

## Related raw API references

The linked Transaction Sale and webhook targets were not read for this entry and are navigation only; they do not establish exact request or response contracts beyond this page's displayed examples.

## Raw Sources

- [[raw/braintree/docs/guides/sepa-direct-debit/server-side/node-2026-09-16|Braintree SEPA Direct Debit server-side implementation for Node.js]] - complete collected page covering transaction creation, displayed callback and Promise examples, EUR currency scope and webhook navigation
