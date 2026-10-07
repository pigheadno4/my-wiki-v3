---
title: "Braintree How Network Tokens Work"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/network-tokens/how-it-works"
raw_files:
  - "braintree/docs/guides/network-tokens/how-it-works-2026-09-16.md"
tags: [braintree, network-tokens, vault, cards, lifecycle-management]
---

## Overview

This unversioned Braintree website snapshot explains how Braintree acts as Token Service Provider and Acquirer to provision a merchant-specific network token from a card PAN, use the token with a one-time cryptogram for a payment, and receive card-network lifecycle updates for Vault card details. It is retrieval evidence for the described flow, not proof of current availability, account or card eligibility, merchant enablement, exact SDK/package behavior, or successful payment processing. See [[braintree]] and [[braintree-payment-methods]].

## Key takeaways

- For provisioning, Braintree sends a PAN from the merchant's Braintree Vault to a card network; the network provisions a token tied to that card and merchant, returns it to Braintree, and Braintree stores it in that merchant's Vault.
- For a transaction, Braintree sends the merchant's vaulted token and a one-time-use cryptogram to the card network; the network exchanges the token for a PAN and sends the PAN to the issuer for processing. The described path does not establish an approval or other transaction outcome.
- Lifecycle Management updates can pass issuer card-detail changes through the card network to Braintree, which updates the details in the merchant's Vault. The page says this can help avoid a failed transaction; it does not guarantee continuity or success.
- Tokenization remains subject to each card network's eligibility criteria. A network may run a $0 verification that can appear on the cardholder's statement but is not a monetary charge; Braintree says it does not control whether the network runs that verification.

## Detail locators

- Provisioning roles, PAN submission, token storage and merchant-specific binding: raw line 16.
- Payment request, one-time cryptogram and token-to-PAN exchange: raw line 18.
- Reissue, theft or loss lifecycle updates and the qualified failed-transaction benefit: raw line 20.
- Network eligibility criteria and network-controlled $0 verification behavior: raw line 22.

## Related

- [[braintree-payment-methods]]
- [[source-braintree-docs-guides-network-tokens-bring-your-own-token-node]] - separate route for submitting externally tokenized or self-vaulted network tokens through Transaction Sale

## Raw Sources

- [[raw/braintree/docs/guides/network-tokens/how-it-works-2026-09-16|Braintree How Network Tokens Work (2026-09-16)]]
