---
title: "Braintree Extend OAuth Shared Vault (Node.js)"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/extend/oauth/shared-vault/node"
raw_files:
  - "braintree/docs/guides/extend/oauth/shared-vault/node-2026-09-16.md"
tags: [braintree, braintree-extend, oauth, shared-vault, node-js, connected-merchants]
---

## Overview

This collected Node.js-route guide documents Braintree Extend OAuth's Shared Vault model. It says a platform owner can keep credit cards and customer data in the platform's own Braintree Vault and use that data when creating a transaction for a connected merchant. The page describes a scope and transaction-creation route; it does not prove merchant consent, tokenization, a successful transaction, current production access or account eligibility.

## Key takeaways

- The collected snapshot labels OAuth closed beta in production and open beta in sandbox, and routes readers to express interest in the production beta. That snapshot statement is not proof of current availability or enablement for a particular platform or merchant.
- The `shared_vault_transactions` right is described as allowing the platform to use tokens and IDs from its own Vault while creating a transaction for a connected merchant. The guide links to the OAuth reference for the scope and to the Node.js transaction-sale reference for the permitted parameters; those linked pages remain separate navigation, not evidence read into this source.
- Payment methods used for Shared Vault transactions cannot be updated by the connected merchant or stored in that merchant's Vault. The same line then ends with the incomplete fragment `or cloned via.` Because the qualification after `via` is absent, this snapshot does not establish a universal prohibition on all cloning, and no cloning mechanism or route is reconstructed.
- A Shared Vault transaction cannot use a granted nonce or a payment method created from a granted nonce. This is a stated input restriction, not evidence of transaction authorization, capture, settlement or any payment outcome.

## Evidence boundaries

> [!warning] Collected rendering defect
> The sentence at line 28 is damaged (`bothand`), and line 31's cloning clause ends with the incomplete fragment `or cloned via.` No fact is inferred from the damaged sentence; the absent qualification after `via` is not reconstructed, and the fragment is not treated as a universal prohibition on all cloning.

> [!warning] Extend OAuth and beta scope
> This page is collected under Braintree Extend OAuth despite its production-interest link pointing to a Braintree Auth contact URL. Shared OAuth terminology or that contact link does not make this a [[braintree-auth]] source or establish current production access.

## Detail locators

- Production closed-beta and sandbox open-beta statement: `# Shared Vault`, lines 14-17.
- Platform-owned Vault, retained credit-card/customer data and connected-merchant transaction purpose: `# Shared Vault`, line 19.
- `shared_vault_transactions` right, platform-Vault tokens/IDs and linked parameter reference: `## Creating a Shared Vault transaction`, lines 22-24.
- Damaged collected sentence omitted from claims: `## Creating a Shared Vault transaction`, line 28.
- Connected-merchant update/storage restrictions, incomplete `or cloned via.` fragment and granted-nonce exclusions: `## Restrictions`, lines 29-31.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-extend-oauth]]
- Product orientation: [[braintree-payment-platform]]
- Separate OAuth product route: [[braintree-auth]]

## Related raw API references

- [[raw/braintree/docs/guides/extend/oauth/reference-2026-09-16|Braintree Extend OAuth reference]] - unread navigation-only route for the `shared_vault_transactions` scope
- [[raw/braintree/docs/reference/request/transaction/sale/node-2026-09-16|Braintree Transaction Sale reference (Node.js)]] - unread navigation-only route for Shared Vault transaction parameters
- The granted-nonce link in the primary raw does not have a retained exact-dated raw target in this collection and is not used as independent evidence.

## Raw Sources

- [[raw/braintree/docs/guides/extend/oauth/shared-vault/node-2026-09-16|Braintree Extend OAuth Shared Vault (Node.js)]] - fully read collected guide for the Shared Vault scope, platform-owned Vault data, connected-merchant transaction route, beta availability and payment-method restrictions
