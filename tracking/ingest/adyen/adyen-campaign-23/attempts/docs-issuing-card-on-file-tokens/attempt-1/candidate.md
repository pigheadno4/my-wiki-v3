---
title: "Adyen Issuing: Card-on-file network tokens"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/card-on-file-tokens"
raw_files:
  - "adyen/docs/issuing/card-on-file-tokens/2026-09-15.md"
tags: [adyen, issuing, network-tokens, card-on-file]
---

## Overview

This 2026-09-15-captured Issuing guide describes **merchant card-on-file network tokens** created when a cardholder saves an Adyen-issued card with a merchant, for example for later purchases or recurring charges. The merchant requests a network token through the card scheme; the scheme forwards the request to Adyen. This is a merchant-stored credential route, distinct from adding a card to a digital wallet.

## Key takeaways

- The guide requires an Issuing-supporting integration, subscription to the **Network token webhook**, and an Adyen-contact check that a card manufacturing profile is set up. The merchant-PCI statement is conditional: it says a merchant that is not PCI compliant does not store raw card details and requests a network token instead. See raw lines 19–31.
- Provisioning starts with an **inactive** network token. Adyen verifies the merchant against the card scheme's allowlist. An allowlisted merchant leads to automatic token approval/activation; a merchant outside the allowlist leads to token closure. Created and outcome webhooks are distinct stages, so creation is not proof of activation. See raw lines 64–117.
- The illustrated merchant/card-scheme/Adyen path describes the scheme passing an activated token to the merchant for storage, then checking token status through Adyen when it is used. The page's sentence that a valid token makes the scheme approve a transaction is a simplified sketch; the separate [[source-adyen-docs-issuing-authorisation|Issuing authorisation guide]] still describes card, balance, transaction-rule and possible relayed-authorisation checks before a payment is approved or refused ([[raw/adyen/docs/issuing/authorisation/2026-09-15|related raw lines 19–41, 63–77]]). Token validity alone does not establish payment approval or capture. See this raw lines 33–62.

## Detail locators

- Merchant card-on-file context, conditional card-data handling and setup requirements: [[raw/adyen/docs/issuing/card-on-file-tokens/2026-09-15|raw lines 19–31]].
- High-level provisioning/payment actors and status-validation sketch: [[raw/adyen/docs/issuing/card-on-file-tokens/2026-09-15|raw lines 33–62]].
- Inactive creation, merchant allowlist, activation/closure and webhooks: [[raw/adyen/docs/issuing/card-on-file-tokens/2026-09-15|raw lines 64–117]].

## Related

- [[adyen-issuing]] — issuer-side card and token source catalog.
- [[adyen]] — provider context.
- [[source-adyen-docs-issuing-network-tokens]] — broader wallet and card-on-file token overview.

## Raw Sources

- [[raw/adyen/docs/issuing/card-on-file-tokens/2026-09-15|Card-on-file network tokens (captured 2026-09-15)]]
