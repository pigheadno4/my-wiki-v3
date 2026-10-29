---
title: "Adyen Stored Value API issue virtual gift card"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/gift-cards/stored-value-api/issue"
raw_files:
  - "adyen/docs/payment-methods/gift-cards/stored-value-api/issue/2026-09-15.md"
tags: [adyen, gift-cards, stored-value, issue, online-payments]
---

## Overview

This 2023-04-21-modified, 2026-09-15-captured Adyen guide describes Stored Value API `POST /issue` for creating a new **virtual** gift card or other stored-value card. The newly issued card is activated automatically; some providers preload it. The page gives provider/channel availability, request fields and response shape, with a specific exception for existing SVS integrations. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Virtual issuance and availability:** The guide says plastic gift cards cannot be issued through Stored Value API. Its provider matrix checks new-card issuance online for Givex and Fiserv (formerly ValueLink), and marks it unavailable in person for all four listed providers. Some providers automatically preload; that does not mean every issued card has the same balance. [Raw: lines 19–40]
- **SVS legacy exception:** A *new* Stored Value API integration cannot issue SVS gift cards. An *existing* integration that has issued SVS cards can continue doing so. The accepted request type list and SVS amount rule below must be read with this integration-age restriction; neither establishes availability for a new merchant. [Raw: lines 35–40, 54–56]
- **Request fields:** POST `/issue` with `merchantAccount`, `paymentMethod.type` and a unique `reference` (maximum 80 characters). The page lists `givex`, `svs` and `valuelink` as accepted types and says not to send other `paymentMethod` fields. `amount` is optional for Givex, must be greater than zero for SVS, and must not be sent for other cards. `giftCardPromoCode` is required only for Fiserv virtual cards and must not be used for other cards. The optional `store` field applies to transactions flagged as in-store and has a 16-character maximum. [Raw: lines 44–57]
- **Response lifecycle:** The response lists card `currentBalance`, request `pspReference`, `resultCode` state, and newly issued `paymentMethod.number` and `paymentMethod.type`; merchant additional-data settings may add fields. A sample `Success` response is illustrative, not evidence of a created card or observed balance. [Raw: lines 90–118]
- **Sample mismatch:** The prose labels the sample response as an SVS card, but its `paymentMethod.type` is `givex`. Do not use this inconsistent example to infer provider-specific output or eligibility. [Raw: lines 102–116]

> [!WARNING] New SVS integrations cannot issue SVS cards
> The source expressly limits continued SVS issuance to existing integrations that have issued SVS cards. Its accepted `svs` type and example do not override this restriction. [Raw: lines 35–38, 54–56, 102–116]

## Detail locators

- Virtual-card behavior, provider/channel matrix and SVS legacy exception: pinned raw lines 15–40.
- Request fields and illustrative Givex/Fiserv examples: pinned raw lines 42–88.
- Response fields, additional data and mislabeled SVS/Givex sample: pinned raw lines 90–118.
- Load, balance, activation, merge and void navigation: pinned raw lines 120–135.

## Related

- [[adyen-online-payments]] — provider online-payment and payment-method route.
- [[source-adyen-docs-payment-methods-gift-cards-stored-value-api]] — broader Stored Value API scope and provider matrix.

## Raw Sources

- [[raw/adyen/docs/payment-methods/gift-cards/stored-value-api/issue/2026-09-15|Stored Value API issue guide, captured 2026-09-15]]
