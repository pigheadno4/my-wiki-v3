---
title: "Braintree Masterpass Server-Side Implementation (Node.js)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/masterpass/server-side/node"
raw_files:
  - "braintree/docs/guides/masterpass/server-side/node-2026-09-16.md"
tags: [braintree, masterpass, nodejs, server-side, transactions, vaulting]
---

## Overview

This 2026-09-16 snapshot of an unversioned [[braintree]] website guide documents historical Node.js server-side routes for creating a Masterpass transaction from a client nonce and device data, and for approval-gated Vault use limited to recurring transactions. The page says Masterpass was replaced by Secure Remote Commerce (SRC); it is historical website guidance, not proof of current availability, exact Node package behavior, merchant approval or payment execution. See [[braintree-payment-methods]] for the provider-wide payment-method route.

> [!warning] Unresolved SRC support conflict
> This snapshot directs former Masterpass users to limited-release SRC, while the separately retained SRC authority carries a January 20, 2026 end-of-support notice. The retained routes do not establish present Masterpass or SRC support or a safe executable migration path; consult [[source-braintree-payment-methods-secure-remote-commerce]] before relying on the replacement direction.

## Key takeaways

- Under **Creating transactions**, the page says a Masterpass transaction is created like another nonce transaction. Its callback and Promise examples pass an amount, the client nonce, client-collected device data and `submitForSettlement: true` to `gateway.transaction.sale()`. These are request examples, not evidence of authorization, submission, settlement or funding.
- Masterpass Vault use is restricted to recurring transactions and requires Masterpass approval. The page says attempting to vault without approval produces the validation error `Nonce is not vaultable.`
- After approval, the page routes storage through `gateway.paymentMethod.create()` with a customer ID and client nonce, or through transaction-time Vault options. It separately routes recurring use through `Transaction: Sale` with `recurring`; exact option names and examples remain in the raw locators.
- The page says vaulted Masterpass information does not support split shipments or one-off transactions. It gives a validation error for a non-recurring transaction using a vaulted Masterpass card.
- Gateway card verification is not supported with Masterpass; the page instead says Masterpass verifies a card when the customer adds it to the wallet. This is a page-scoped historical statement, not current wallet or gateway behavior proof.

## Material boundaries

> [!warning] Historical website and runtime boundary
> The route is labeled Node.js but states no exact Node SDK package version. The retained page does not establish current Masterpass or SRC availability, account eligibility, Masterpass approval, client-side nonce or device-data behavior, exact SDK runtime behavior, successful vaulting, authorization, settlement or funding.

## Detail locators

- Masterpass replacement direction, SRC limited-release eligibility, API-change warning, client-SDK introduction and access request: opening `**AVAILABILITY**`, raw lines 17-18.
- Transaction instruction plus callback and Promise examples: `## Creating transactions`, raw lines 21-61.
- Recurring-only Vault restriction and approval prerequisite: `## Vaulting Masterpass`, raw lines 63-71.
- Callback and Promise examples for `gateway.paymentMethod.create()`: `## Vaulting Masterpass`, raw lines 72-90.
- Transaction-time storage navigation, recurring flag, split-shipment and vaulted one-off exclusions, and validation error: `## Vaulting Masterpass`, raw lines 91-95.
- Card-verification exclusion and wallet-verification statement: `## Card verification`, raw lines 96-99.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Separate SRC support-status authority: [[source-braintree-payment-methods-secure-remote-commerce]]
- Complementary client route: [[source-braintree-docs-guides-masterpass-client-side-javascript-v3]]

## Raw Sources

- [[raw/braintree/docs/guides/masterpass/server-side/node-2026-09-16|Braintree Masterpass server-side Node.js guide (captured 2026-09-16)]] - fully read pinned website snapshot covering transaction creation, approval-gated recurring Vault use, unsupported vaulted uses and card-verification behavior
