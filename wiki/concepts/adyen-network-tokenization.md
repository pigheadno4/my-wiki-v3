---
title: "Adyen Network Tokenization"
type: concept
category: technology
tags: [adyen, network-tokenization, cards, recurring-payments]
---

## Definition

Adyen network tokenization uses a card-network-issued token as an alternative to the PAN for online card payments. It is distinct from [[adyen-tokenization]], where Adyen stores payment details in its Vault and returns a token for later payments. The retained guide limits network tokenization to payments acquired by Adyen, not external acquirer connections.

## Implementation boundary

Adyen can manage network tokens and automatically substitute them for card details or a `storedPaymentMethodId`; that route can be combined with Adyen Vault tokenization. Alternatively, a merchant can supply existing card-network tokens, but the guide says that self-managed route cannot be combined with Adyen tokenization and requires a saved `networkTxReference` for subsequent payments.

The snapshot contains two ambiguities that require current-contract confirmation: an enablement sentence under the Adyen-managed heading says "manage network tokens yourself", and the subsequent one-off request table omits `paymentMethod.networkPaymentReference` even though the surrounding text says to use the saved reference. The snapshot does not prove current enablement, eligibility, transaction success, or authorization-rate improvement.

## Sources

- [[source-adyen-docs-online-payments-tokenization-forward-payment-details]] — 2026-09-15 Adyen webpage guide to forwarding network tokens to a PCI-compliant third party through `/forward`, with a same-card Adyen token and conditional fallback.


- [[source-adyen-docs-online-payments-network-tokenization]] - 2026-09-15 guide to network-token identity, Adyen-managed and merchant-managed routes, acquisition limits, retry behavior, routing, and request-contract ambiguities
