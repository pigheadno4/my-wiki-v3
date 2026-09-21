---
title: "Braintree Credit Card Update (Node.js)"
type: source
date_ingested: 2026-09-20
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/credit-card/update/node"
raw_files:
  - "braintree/docs/reference/request/credit-card/update/node-2026-09-16.md"
tags: [braintree, node-js, credit-card, vault, payment-method-nonce]
---

## Overview

This Braintree Node.js reference documents updating a stored credit card by token through `gateway.creditCard.update()`. Its example supplies update attributes and receives `err` and `result` through a callback.

## Key takeaways

- The page says this operation **typically** requires PCI SAQ D compliance and recommends using `payment_method` functions to avoid PCI concerns from raw credit-card data being present on the merchant server. This is the page's qualified advisory and recommendation, not a guarantee of compliance or a claim that every use of a credit-card method requires SAQ D.
- When card verification is enabled, the page says credit-card updates are subject to those verification rules. It does not describe those linked rules on this page.
- The Node example identifies the stored card with `creditCardToken`, supplies card, billing-address, and verification-option inputs, and exposes `err` and `result` in its callback; the page does not describe result fields or a success condition.
- The page permits raw card data and a payment-method nonce in the same call but recommends passing only a nonce. If both are supplied, the resulting payment method mixes their attributes: individually supplied fields take precedence, and remaining attributes come from the nonce.

## Detail locators

- Qualified PCI SAQ D advisory and `payment_method` recommendation: `# Credit Card: Update > **IMPORTANT**`, lines 16-17.
- Conditional card-verification note: `# Credit Card: Update > **NOTE**`, lines 20-21.
- Node token, example input categories, `verifyCard` option, and callback shape: `# Credit Card: Update > ### Node`, lines 24-40.
- Nonce-versus-raw-card recommendation and attribute precedence: `## Payment method nonces vs. raw card data`, lines 42-49.

## Related

- Company: [[braintree]]
- Concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/request/credit-card/update/node-2026-09-16|Braintree Node.js credit-card update reference]] - complete page covering the update example, qualified PCI advisory, card-verification condition, and nonce-versus-raw-card guidance
