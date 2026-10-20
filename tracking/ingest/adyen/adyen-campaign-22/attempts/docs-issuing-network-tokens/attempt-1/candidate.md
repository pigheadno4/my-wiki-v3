---
title: "Adyen Issuing: Network tokens"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/network-tokens"
raw_files:
  - "adyen/docs/issuing/network-tokens/2026-09-15.md"
tags: [adyen, issuing, network-tokens, cards]
---

## Overview

Adyen's 2026-09-15-captured Issuing overview explains network tokens for Adyen-issued cards: a digital wallet or merchant requests a token that can stand in for sensitive card details. It distinguishes wallet provisioning from merchant-specific card-on-file use and describes token statuses. This is an issuer-side guide; Adyen's separate [[adyen-network-tokenization]] concept covers online payment acquisition. [[adyen]] [[adyen-issuing]]

## Key takeaways

- The stated prerequisites are an integration supporting Issuing and contact-led confirmation that a card manufacturing profile is set up. The overview describes tokens replacing PAN, CVC and expiry; for an Adyen-issued-card payment, it says the merchant receives a network token, sends it to the card scheme and Adyen, and Adyen decodes and validates the corresponding card details. See raw lines 19 and 21-38.
- Two token types are described: digital-wallet tokens let a cardholder add a card to a wallet; card-on-file tokens support single or recurring payments to a specific merchant. The page routes to separate implementation guides for each type and to lifecycle webhooks. See raw lines 46-49 and 89-101.
- A wallet or merchant requests creation. A newly created token is `inactive` and unusable while provisioning is incomplete. Following Adyen risk analysis, approval makes it `active`; decline makes it `closed`. An active token can later be suspended or closed by the platform or cardholder. See raw lines 51-68 and 76-87.
- `suspended` temporarily prevents payment use and can return to `active` or become `closed`; `closed` is permanent and cannot be updated. The status table lists PATCH updates, wallet actions, removal of a wallet card, and deletion of merchant card-on-file as possible transitions. See raw lines 78-87.
- The page presents reduced friction, higher authorization rates and one-time cryptograms as benefits. These are source claims, not proof that any specific token request, authorization or payment succeeds. See raw lines 40-44.

## Detail locators

- Token definition and merchant/scheme/Adyen handoff: raw lines 30-44.
- Wallet versus card-on-file type links: raw lines 46-49; separate guides and webhook navigation: raw lines 89-101.
- Status transition narrative and status-specific actors/actions: raw lines 51-87.

## Related

- [[adyen-issuing]] — Issuing program context and reciprocal source route.
- [[adyen-network-tokenization]] — separate acquiring-side network-tokenization context.

## Raw Sources

- [[raw/adyen/docs/issuing/network-tokens/2026-09-15|Adyen Issuing network tokens, captured 2026-09-15]]
