---
title: "Braintree Credit Card Create (Node.js)"
type: source
date_ingested: 2026-09-20
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/credit-card/create/node"
raw_files:
  - "braintree/docs/reference/request/credit-card/create/node-2026-09-16.md"
tags: [braintree, node-js, credit-cards, vault, payment-method-nonce, pci-dss]
---

## Overview

This Braintree Node.js reference documents `gateway.creditCard.create()` for creating a credit card with the server SDK. It shows a raw-card callback example, preserves the page's qualified PCI warning and payment-method recommendation, and explains how raw card fields interact with a payment-method nonce when both are supplied.

## Key takeaways

- The Node example constructs credit-card parameters containing a customer ID and raw card details, then passes them to `gateway.creditCard.create()` in callback form.
- The page says this approach **typically requires** PCI SAQ D compliance and recommends using `payment_method` functions so raw credit-card data is not present on the merchant's server. This collected advisory is not a guarantee that using those functions establishes compliance.
- Although the operation accepts raw card data and a payment-method nonce in the same call, the page recommends supplying only a nonce. If both are supplied, explicitly passed fields take precedence and the remaining attributes come from the nonce.

> [!warning] Qualified PCI guidance
> Preserve the provider's wording: direct credit-card creation **typically requires** PCI SAQ D compliance. The recommendation to use `payment_method` functions does not establish a compliance guarantee, and this page does not say that every credit-card-method use always requires SAQ D.

## Detail locators

- Qualified PCI warning and recommendation to use `payment_method` functions: `# Credit Card: Create`, lines 16-17.
- Node raw-card callback example and `gateway.creditCard.create()` invocation: `### Node`, lines 20-31.
- Nonce-versus-raw-card recommendation and attribute precedence: `## Payment method nonces vs. raw card data`, lines 33-40.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]
- Related source: [[source-braintree-payment-method-nonces]]

## Related raw API references

- [[raw/braintree/docs/guides/payment-methods/node-2026-09-16|Braintree Node.js payment-methods guide]] - navigation-only destination linked by the PCI advisory; not used as factual evidence here

## Raw Sources

- [[raw/braintree/docs/reference/request/credit-card/create/node-2026-09-16|Braintree Node.js credit-card-create request reference]] - complete collected page covering the qualified PCI advisory, raw-card callback example, and nonce-versus-raw-card recommendation and precedence
