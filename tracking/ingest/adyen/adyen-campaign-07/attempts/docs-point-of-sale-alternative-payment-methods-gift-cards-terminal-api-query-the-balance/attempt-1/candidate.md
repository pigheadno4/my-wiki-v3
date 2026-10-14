---
title: "Adyen Terminal API gift-card balance inquiry"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/alternative-payment-methods/gift-cards-terminal-api/query-the-balance"
raw_files:
  - "adyen/docs/point-of-sale/alternative-payment-methods/gift-cards-terminal-api/query-the-balance/2026-09-15.md"
tags: [adyen, point-of-sale, gift-cards, stored-value, terminal-api, balance-inquiry]
---

## Overview

Adyen's POS guide, last modified 2019 and captured 2026-09-15, shows how a merchant with a Terminal API payment-terminal integration checks remaining funds on an **activated** gift card before a payment. A balance inquiry can inform whether another tender is needed; it does not itself authorize a gift-card payment. The page belongs to [[adyen-pos-gift-cards]] and uses the [[adyen-terminal-api]] Service/BalanceInquiry message route.

## Key takeaways

- **Account and provider setup precede inquiry.** The guide requires the gift-card payment method on the Adyen account and completed onboarding with the gift-card provider. Its provider field names givex, svs, valuelink or an Intersolve-supported card type; that list and the dated guide do not prove present provider, region, account or terminal eligibility.
- **Card entry controls request order and fields.** For a scanned card, scan first and include `EntryMode: Scanned`, card number in `StoredValueID`, and `ExpiryDate`. For swipe or manual keyed entry, send the inquiry first so the terminal prompts for details; include `EntryMode: MagStripe` or `Keyed` and include `StoredValueID` without a value. The guide does not establish a universal gift-card PIN rule.
- **The request is a Terminal API balance message.** `SaleToPOIRequest.MessageHeader` uses protocol 3.0, `MessageClass: Service`, `MessageCategory: BalanceInquiry` and `MessageType: Request`, with SaleID, POIID and a terminal-scoped ServiceID unique within the previous 48 hours. `PaymentInstrumentData` identifies `StoredValue` and a `GiftCard` account with provider and PAN identification. The optional `ProtectedCardData` description concerns an SVS secondary security code encoded in Base64 if required; its example is not a blanket requirement or encryption claim.
- **Read balance and currency from the response.** The guide points to `BalanceInquiryResponse.PaymentAccountStatus.CurrentBalance` and `.Currency`; its sample shows `Response.Result: Success` and GBP 98.75. That sample is an illustrative balance-query outcome, not authorization, capture, settlement, a guarantee of funds at later payment, or a safe-retry rule. A subsequent gift-card payment is a separate operation.

## Detail locators

- Raw opening and `## Requirements` (lines 15–29): activated-card purpose, Terminal API terminal integration, Adyen account method and provider onboarding.
- Raw `## Make a balance inquiry` (lines 31–75): scan versus swipe/manual request order, MessageHeader fields and 48-hour ServiceID uniqueness, provider/account identifiers, entry-mode fields, optional SVS SSC.
- Raw JSON and Java examples (lines 77–148): illustrative scanned SVS card request; sample identifiers, expiry, SSC and terminal are examples, not universal values.
- Raw response instructions and JSON example (lines 150–183): `CurrentBalance`, `Currency`, sample `Result: Success`, GBP 98.75 and response MessageHeader.
- Raw `## See also` (lines 185–190): separate activation, load and payment routes; follow those sources for their own behavior.

## Related

- [[adyen-pos-gift-cards]] — gift-card lifecycle and partial-payment boundary.
- [[adyen-terminal-api]] — Nexo Terminal API message architecture.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/alternative-payment-methods/gift-cards-terminal-api/query-the-balance/2026-09-15|Check the balance of a gift card, fetched 2026-09-15]]
