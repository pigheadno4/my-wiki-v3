---
title: "Braintree Payment Methods Guide (Node.js)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/payment-methods/node"
raw_files:
  - "braintree/docs/guides/payment-methods/node-2026-09-16.md"
tags: [braintree, payment-methods, nodejs, vault, customers]
---

## Overview

This 2026-09-16 snapshot of an unversioned [[braintree]] website guide describes a payment method as transactable payment information that belongs to a customer, is stored in the Braintree Vault, and has a payment-method token that can be retained with reduced PCI compliance burden for later transaction creation. It routes Node.js readers through create, update, find and delete operations. See [[braintree-payment-methods]] for the provider-wide payment-method route.

## Key takeaways

- The create route is for an existing customer and takes a payment-method single-object token received from the client. The page separately points to Customer Create when creating a new customer together with a payment method. See **Create** (raw lines 19-43).
- After successful creation, the page routes transaction creation through Transaction Sale with the stored `payment_method_token`. This is a documented transition, not proof that a transaction was attempted or succeeded. See **Create** (raw lines 41-43).
- Braintree strongly recommends verifying all cards before Vault storage by enabling account-wide card verification in the Control Panel. The recommendation is card-specific and does not itself prove that verification is enabled or that a card passed verification. See the note after the create examples (raw lines 46-47).
- The update section routes changes through Payment Method Update. It includes making the method the customer's default and updating a billing address; when `update_existing` is omitted in the displayed billing-address route, the page says a new billing address is created for the payment method. See **Update**, **Make default** and **Billing address** (raw lines 52-114).
- The find route returns a `payment_method` response object. The delete section exposes Payment Method Delete, but this captured page states no cascade, reversibility or recovery semantics beyond deleting the payment method, so none should be inferred. See **Find** and **Delete** (raw lines 117-147).

## Material boundaries

> [!warning] Snapshot, SDK and execution boundaries
> This retained Braintree website page is routed to Node.js but gives no exact Node SDK package or version. It is snapshot documentation, not evidence of current availability, merchant or customer eligibility, account configuration, runtime behavior, successful Vault storage, card verification or payment execution. The callback and Promise snippets are examples, not execution results.

> [!warning] Delete scope
> Deletion is destructive at the named payment-method level. Because this raw page does not describe related-object cascades, merchant connections, recovery or reversibility, use the linked delete reference before making claims about those effects.

## Detail locators

- Payment-method identity, customer ownership, Vault storage and reusable token purpose: opening paragraph, raw line 16.
- Existing-customer creation from a client-supplied single-object token, callback and Promise examples, alternative Customer Create route, and post-create Transaction Sale transition: `## Create`, raw lines 19-43.
- Account-wide card-verification recommendation: note after the create examples, raw lines 46-47.
- Update operation orientation: `## Update`, raw lines 52-54.
- Default-method option and callback/Promise examples: `### Make default`, raw lines 57-80.
- Billing-address update examples, `update_existing` behavior, and Customer Update route: `### Billing address`, raw lines 82-114.
- Find invocation and returned response-object type: `## Find`, raw lines 117-131.
- Delete callback and Promise invocation examples: `## Delete`, raw lines 134-147.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- SDK boundary: [[braintree-server-sdk]]

## Related raw API references

- [[raw/braintree/docs/reference/request/payment-method/create/node-2026-09-16|Braintree Node.js Payment Method Create reference]] - unread navigation-only operation detail
- [[raw/braintree/docs/reference/request/payment-method/update/node-2026-09-16|Braintree Node.js Payment Method Update reference]] - unread navigation-only operation detail
- [[raw/braintree/docs/reference/request/payment-method/find/node-2026-09-16|Braintree Node.js Payment Method Find reference]] - unread navigation-only operation detail
- [[raw/braintree/docs/reference/request/payment-method/delete/node-2026-09-16|Braintree Node.js Payment Method Delete reference]] - unread navigation-only operation detail
- [[raw/braintree/docs/reference/request/transaction/sale/node-2026-09-16|Braintree Node.js Transaction Sale reference]] - unread navigation-only post-create transaction route

## Raw Sources

- [[raw/braintree/docs/guides/payment-methods/node-2026-09-16|Braintree Payment Methods guide for Node.js (captured 2026-09-16)]] - fully read pinned website snapshot covering payment-method identity and create, update, find and delete routes
