---
title: "Braintree Credit Card Find (Node.js)"
type: source
date_ingested: 2026-09-20
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/credit-card/find/node"
raw_files:
  - "braintree/docs/reference/request/credit-card/find/node-2026-09-16.md"
tags: [braintree, node-js, credit-cards, vault, retrieval]
---

## Overview

This Braintree Node.js reference shows `gateway.creditCard.find()` looking up a credit card by a supplied token. The callback exposes `err` and a `creditCard` argument, but this page does not document the returned object's fields or a success condition.

## Key takeaways

- The example passes a variable named `creditCardToken` to `gateway.creditCard.find()` and receives `err` and `creditCard` in the callback. It does not show how the callback result is consumed.
- The page says this operation **typically requires** PCI SAQ D compliance. Preserve that qualification: the page does not state that every credit-card lookup always requires SAQ D.
- Braintree recommends using `payment_method` functions to avoid PCI concerns associated here with raw credit-card data being present on the merchant server. The linked payment-method guide and PCI page are navigation only in this source; they do not establish specific alternative behavior, a compliance guarantee, or a current independent compliance assessment.
- This page documents lookup only. It does not establish credit-card creation, update, deletion, authorization, or subscription effects.

> [!warning] Qualified collected PCI guidance
> The PCI statement is Braintree's collected advisory and is qualified as `Typically requires`. The recommendation to use `payment_method` functions must not be broadened into a guarantee of compliance or into a claim that every use of `gateway.creditCard.find()` always requires SAQ D.

## Detail locators

- Qualified PCI SAQ D statement and recommended payment-method alternative: `# Credit Card: Find > **IMPORTANT**`, lines 16-17.
- Token variable, Node lookup invocation, and callback arguments: `# Credit Card: Find > ### Node`, lines 20-23.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/request/credit-card/find/node-2026-09-16|Braintree Node.js credit-card find reference]] - complete collected page covering token-based lookup, callback arguments, and the qualified PCI advisory
