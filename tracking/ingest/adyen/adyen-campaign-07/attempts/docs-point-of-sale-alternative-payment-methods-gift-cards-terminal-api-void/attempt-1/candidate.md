---
title: "Undo a gift-card load transaction | Adyen Docs"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/alternative-payment-methods/gift-cards-terminal-api/void"
raw_files:
  - "adyen/docs/point-of-sale/alternative-payment-methods/gift-cards-terminal-api/void/2026-09-15.md"
tags: [adyen, point-of-sale, gift-cards, terminal-api, stored-value, void]
---

## Overview

This Adyen Terminal API guide describes **undoing a gift-card load**, which takes the loaded amount off the card balance. It is limited to the **most recent** load transaction on that card and that load must be from the **past 24 hours**. The guide explicitly says this undo request cannot cancel a gift-card payment or make a refund to a gift card; deactivation is a separately linked operation. The page was fetched 2026-09-15 and records a 2020-01-07 last-modified timestamp. [[adyen]] [[adyen-pos-gift-cards]] [[adyen-terminal-api]]

## Key takeaways

- The operation requires a Terminal API integration with a payment terminal, the gift-card payment method added to the Adyen account, and completed onboarding with the gift-card provider. The described undo uses the original load's `POITransactionID.TimeStamp` and `POITransactionID.TransactionID`; the amount removed is the amount of that qualifying load, not a freely specified partial refund. See **Requirements** and **Undo a transaction**, pinned raw lines 19–40.
- Send a Terminal API **StoredValue** service request with `StoredValueTransactionType: Reverse` and `OriginalPOITransaction` identifying the original load. The documented header uses protocol version 3.0, `MessageClass: Service`, `MessageCategory: StoredValue`, and a terminal-scoped `ServiceID` of 1–10 alphanumeric characters unique within the last 48 hours for the `POIID`. `SaleTransactionID.TransactionID` is the merchant's undo-request reference; Adyen recommends a unique value. These identities do not establish safe retry or a general idempotency guarantee. See pinned raw lines 43–70.
- The original `POITransactionID.TransactionID` can use the recommended `tenderReference.pspReference` form, a `pspReference` with its **leading dot**, or `tenderReference` alone **only when using the same terminal** as the original transaction. The original timestamp is also required. See pinned raw lines 40–41 and 64–76.
- Check the `StoredValueResponse`: `StoredValueTransactionType: Reverse` together with `Response.Result: Success` indicates the loaded funds were reversed. `StoredValueAccountStatus.CurrentBalance` reports the remaining card balance after undo; `POIData.POITransactionID.TransactionID` identifies the undo transaction. `Response.AdditionalResponse` may be form-encoded pairs or Base64-encoded JSON. The illustrative payload includes an `AdditionalResponse` field `transactionType=REFUND`, but the guide's requested and checked operation remains a load reversal, not the separate refund-to-card flow. See pinned raw lines 154–199.
- The JSON/Java snippets demonstrate request construction, and the response JSON is illustrative. The guide does not show a live operation, merchant/provider eligibility, settlement impact, or a verified current account balance. See pinned raw lines 78–152 and 164–199.

## Detail locators

- **Undo a load transaction to a gift card** (pinned raw lines 15–24) — qualifying latest-load/24-hour limit and exclusions of payment cancellation and refund.
- **Requirements** (pinned raw lines 26–34) — Terminal API/payment-terminal integration, Adyen method addition and provider onboarding.
- **Undo a transaction** (pinned raw lines 36–76) — original transaction identity, header and StoredValue request fields, reference format limitations.
- **JSON; Java** (pinned raw lines 78–152) — illustrative request construction, not a new provider or result rule.
- **StoredValueResponse** (pinned raw lines 154–199) — success check, balance and identifier fields, AdditionalResponse encoding, illustrative response.
- **See also** (pinned raw lines 201–206) — separate load, refund, cancel and deactivation routes.

## Related

- [[adyen-pos-gift-cards]] — primary gift-card operation hub.
- [[adyen-terminal-api]] — Terminal API message architecture.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/alternative-payment-methods/gift-cards-terminal-api/void/2026-09-15|Adyen gift-card load undo guide, fetched 2026-09-15]]
