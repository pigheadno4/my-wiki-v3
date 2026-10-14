---
title: "Adyen Docs: Activate a gift card at point of sale"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/alternative-payment-methods/gift-cards-terminal-api/activate"
raw_files:
  - "adyen/docs/point-of-sale/alternative-payment-methods/gift-cards-terminal-api/activate/2026-09-15.md"
tags: [adyen, point-of-sale, gift-cards, activation, stored-value, terminal-api]
---

## Overview

This Adyen POS guide describes activating a newly issued gift card before it can be redeemed. The activation can add an initial balance or use zero for an active card without loaded value. It is a Terminal API `StoredValue` operation and must be distinguished from a `Payment` request. The page was last modified in 2019 and captured on 2026-09-15; its provider examples, protocol fields, and sample successful response do not prove current enablement or an executed activation. [[adyen]] [[adyen-pos-gift-cards]] [[adyen-terminal-api]]

## Key takeaways

- A newly issued card cannot be redeemed until activated in the described flow; activation is presented as fraud protection. The prerequisites are a Terminal API integration with payment terminals, adding the method to the Adyen account, and completing gift-card-provider onboarding. This guide does not claim that activation alone loads spendable funds. See pinned raw lines 19–31.
- For scan entry, the POS obtains card details before sending the request; for swipe or manual key entry, send the request first and the terminal prompts for card details. The request uses `MessageClass: Service`, `MessageCategory: StoredValue`, and `StoredValueData.StoredValueTransactionType: Activate`. `Payment` is a different message category used for spending the gift card. See **Make an activation request**, pinned raw lines 37–50 and 64–84.
- `StoredValueData.ItemAmount` is the initial amount to load and must be `0` when activating without balance; `Currency` is the currency of that amount. The request identifies a `GiftCard` stored-value account, provider, PAN identification and entry-specific fields. The page names `givex`, `svs`, `valuelink`, and Intersolve-supported types as provider examples, not a current acceptance guarantee. The sample GBP 10.00 request is illustrative. See pinned raw lines 64–86 and 90–130.
- `SaleToAcquirerData` may contain an `ssc` of up to eight digits for Stored Value Solutions (SVS) gift cards specifically. This is a provider-specific optional secondary security code, not a universal gift-card PIN requirement. The overview's PIN options and terminal-prompt behavior belong to their separate source. See pinned raw line 62.
- The guide says `ServiceID` must be unique within 48 hours for the terminal `POIID`, while `SaleTransactionID.TransactionID` is recommended unique and the timestamp is UTC. These identities do not establish idempotent replay or a safe retry for an activation whose outcome is unknown. See pinned raw lines 52–62.
- The `StoredValueResponse` supplies a terminal transaction identifier, `StoredValueResult` with type `Activate` and current value/currency, and `Response.Result`. The guide says `Success` indicates that activation succeeded; that status is about activation, not a payment authorization or proof that the example occurred in a live account. See pinned raw lines 176–223.

## Detail locators

- **Activate a gift card / Requirements** (pinned raw lines 15–31) — pre-redemption activation, fraud role, integration and onboarding.
- **Make an activation request → card entry and MessageHeader** (pinned raw lines 33–54) — scan versus terminal capture, `StoredValue` category and request identifiers.
- **Make an activation request → SaleData and StoredValueData** (pinned raw lines 56–84) — transaction reference, optional SVS `ssc`, `Activate`, amount/currency, provider and entry-mode fields.
- **JSON / Java examples** (pinned raw lines 86–174) — illustrative GBP 10.00 scanned-card request and sample implementation, not a current SDK contract.
- **StoredValueResponse** (pinned raw lines 176–223) — transaction ID, result amount/currency, and `Success` interpretation.

## Related

- [[adyen-pos-gift-cards]] — primary POS gift-card lifecycle.
- [[adyen-terminal-api]] — underlying terminal message structure.
- [[adyen-pos-alternative-payment-methods]] — POS method-family overview.

## Related raw API references

The following are linked navigation, not evidence independently reviewed for this entry:

- POS gift-card overview — https://docs.adyen.com/point-of-sale/gift-cards-terminal-api
- Gift-card payment — https://docs.adyen.com/point-of-sale/gift-cards-terminal-api/payment
- Gift-card deactivation — https://docs.adyen.com/point-of-sale/gift-cards-terminal-api/deactivate
- Terminal API Stored Value request — https://docs.adyen.com/api-explorer/terminal-api/latest/post/storedvalue

## Raw Sources

- [[raw/adyen/docs/point-of-sale/alternative-payment-methods/gift-cards-terminal-api/activate/2026-09-15|Adyen POS gift-card activation guide, fetched 2026-09-15]]
