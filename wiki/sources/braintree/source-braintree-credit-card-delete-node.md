---
title: "Braintree Credit Card Delete (Node.js)"
type: source
date_ingested: 2026-09-20
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/credit-card/delete/node"
raw_files:
  - "braintree/docs/reference/request/credit-card/delete/node-2026-09-16.md"
tags: [braintree, node-js, credit-cards, vault, deletion]
---

## Overview

This Braintree Node.js reference shows `gateway.creditCard.delete()` deleting a credit card identified by a supplied token. Its callback receives only an `err` argument in the displayed example; the page does not document a returned result object, success condition, or effects on associated records.

## Key takeaways

- The example passes a variable named `creditCardToken` to `gateway.creditCard.delete()` and supplies a callback with an `err` argument. No result value or response fields are shown.
- The page says this operation **typically requires** PCI SAQ D compliance. Preserve that qualification: the page does not state that every credit-card deletion always requires SAQ D.
- Braintree recommends using `payment_method` functions to avoid PCI concerns associated here with raw credit-card data being present on the merchant server. The linked payment-method guide and PCI page are navigation only in this source; they do not establish specific alternative behavior, a compliance guarantee, or a current independent compliance assessment.
- This page itself does not state that deletion cancels subscriptions, forfeits paid service, removes billing relationships, or produces any other downstream effect. Those consequences must not be imported from a separate payment-method deletion operation.

> [!warning] Qualified guidance and bounded deletion evidence
> The PCI statement is Braintree's collected advisory and is qualified as `Typically requires`. The recommendation to use `payment_method` functions must not be broadened into a guarantee of compliance. This page supports the displayed credit-card deletion call only; it does not establish subscription or other association consequences.

## Detail locators

- Qualified PCI SAQ D statement and recommended payment-method alternative: `# Credit Card: Delete > **IMPORTANT**`, lines 16-17.
- Token variable, deletion invocation, and error-only callback: `# Credit Card: Delete > ### Node`, lines 20-22.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/request/credit-card/delete/node-2026-09-16|Braintree Node.js credit-card delete reference]] - complete collected page covering token-based deletion, the error-only callback, and qualified PCI guidance
