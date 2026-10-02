---
title: "Braintree Credit Cards Overview"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/credit-cards/overview"
raw_files:
  - "braintree/docs/guides/credit-cards/overview-2026-09-16.md"
tags: [braintree, credit-cards, debit-cards, card-fields, tokenization, payment-method-nonce]
---

## Overview

This unversioned [[braintree]] website-guide snapshot, collected 2026-09-16, describes Card Fields as the page's recommended card-entry route for merchants building a custom checkout, but does not identify supported client platforms or SDK versions. The collected page says credit cards are enabled automatically when a merchant signs up for a Braintree merchant account, then outlines a client-to-server integration in which Card Fields tokenizes card details into a payment method nonce and the server uses that nonce to create a transaction.

## Key takeaways

- Within the overview's unversioned scope, the page covers credit and debit card acceptance through Card Fields. It assigns card number, expiration date and CVV entry, formatting, validation, card-brand detection and tokenization to the SDK while leaving the rest of checkout under merchant control.
- Before Card Fields initialization, the merchant generates a client token on the server; an already available client token can be reused. Card Fields uses that authorization to tokenize the submitted card details and return a payment method nonce.
- The integration sequence is account configuration, client-side Card Fields, and server-side transaction creation using the resulting nonce. Tokenization and receipt of a nonce do not establish that a transaction was authorized, settled or funded.

## Evidence limitations

> [!warning] Platform and SDK-version boundary
> This overview does not identify supported platforms or SDK versions. The separately retained JavaScript v3 client guide explicitly says JavaScript v3 does not support Card Fields and routes JavaScript merchants to Hosted Fields; that collected guide names Card Fields only for Android v5 and iOS v7. Those native version statements are snapshot-scoped and do not prove current support. Use [[source-braintree-credit-cards-client-javascript-v3]] and [[braintree-web-sdk]] to resolve the JavaScript selection boundary.

The automatic-enable and recommendation statements are evidence from the pinned 2026-09-16 snapshot, not proof of current product support, merchant-account enablement, card or buyer eligibility, or successful payment execution. This website guide describes integration responsibilities but is not exact-version SDK or GitHub implementation evidence; version-specific behavior must remain tied to separately retained implementation sources.

## Detail locators

- Credit-card acceptance and automatic merchant-account enablement statement: `# Overview`, line 16.
- Card Fields purpose, managed fields and SDK responsibilities: `# Overview`, line 18.
- Account configuration, client-side Card Fields and nonce-to-server transaction sequence: `# Overview`, lines 20-22.
- Server-generated client-token prerequisite, token reuse and nonce return: `# Overview` note, lines 25-26.
- Next configuration route: line 32.

## Related

- Company: [[braintree]]
- Payment-method concept: [[braintree-payment-methods]]
- Platform concept: [[braintree-payment-platform]]
- JavaScript v3 Card Fields/Hosted Fields boundary: [[source-braintree-credit-cards-client-javascript-v3]]
- Browser SDK concept: [[braintree-web-sdk]]

## Related raw API references

- [[raw/braintree/docs/guides/credit-cards/configuration-2026-09-16|Braintree credit-card configuration guide]] - next-page navigation only; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/guides/credit-cards/overview-2026-09-16|Braintree Credit Cards Overview]] - fully read pinned website snapshot covering Card Fields responsibilities, client-token authorization and nonce handoff
