---
title: "Braintree Bring Your Own Token (Node.js)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/network-tokens/bring-your-own-token/node"
raw_files:
  - "braintree/docs/guides/network-tokens/bring-your-own-token/node-2026-09-16.md"
tags: [braintree, nodejs, network-tokens, byot, cit, mit]
---

## Overview

This 2026-09-16 collected, unversioned [[braintree]] website guide is a Node-routed Bring Your Own Token (BYOT) path for merchants that already have network tokens because another payment service provider tokenized the cards or because the merchants vault network tokens themselves. It describes passing those existing tokens in a Braintree Transaction Sale request. The snapshot does not establish a Node SDK package version, current availability, merchant-account enablement, token validity, or a successful authorization, payment, capture, settlement or funding outcome.

## Key takeaways

- The guide creates a BYOT transaction through Transaction Sale. It lists amount, the token as the card number, the token expiration date and a cryptogram as always required; exact request-field paths and the separately listed optional ecommerce indicator and token requestor ID remain in **Required parameters** and **Optional parameters**, raw lines 19–45.
- For a customer-initiated transaction (CIT), including the first transaction in a recurring series, the page requires a network-issued cryptogram. It recommends an `external_vault` object whose status is `vaulted`, while explicitly saying that object is optional in this snapshot and may become required in a future update; the recommendation is not a present requirement or proof of Vault state. The Node examples render that object as `externalVault`. See **Customer initiated transactions**, raw lines 48–100.
- For a merchant-initiated transaction (MIT) or a subsequent transaction, the page requires a network transaction identifier and related parameters. The cryptogram field must still be present, but the guide directs the integration to use `STATIC_RECURRING` instead of a network-issued cryptogram. Exact required fields and allowed transaction-source values remain in **Merchant initiated transactions / Required parameters**, raw lines 102–114.
- The callback and Promise blocks are illustrative Node request shapes. They are not a complete API contract, package-qualified implementation evidence, confirmation that an account is enabled for BYOT, or evidence that any displayed request was accepted or processed with a network token.

## Detail locators

- BYOT identity and externally tokenized or self-vaulted network-token scope: raw lines 14–16.
- Transaction Sale action and type-dependent network-token parameters: raw lines 19–21.
- Always-required and always-optional field lists: raw lines 24–45.
- CIT or first-recurring network-issued cryptogram and snapshot-optional `external_vault.status = vaulted` recommendation: raw lines 48–50.
- CIT callback and Promise examples, including Node `externalVault`: raw lines 53–100.
- MIT or subsequent-transaction NTI, related-parameter and `STATIC_RECURRING` cryptogram conditions: raw lines 102–114.
- MIT callback and Promise examples: raw lines 116–170.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]

## Related raw API references

The page links to the Node Transaction Sale request reference for field definitions, complete transaction options and examples. That target was not read for this entry and is navigation only; it does not establish exact schema, package behavior, current BYOT availability, merchant-account enablement or payment outcomes.

## Raw Sources

- [[raw/braintree/docs/guides/network-tokens/bring-your-own-token/node-2026-09-16|Braintree Bring Your Own Token Node guide]] - complete collected page covering BYOT Transaction Sale parameters and distinct CIT/first-recurring and MIT/subsequent cryptogram context
