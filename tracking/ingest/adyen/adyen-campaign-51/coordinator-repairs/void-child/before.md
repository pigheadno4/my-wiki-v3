---
title: "Adyen Stored Value API void transaction"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/gift-cards/stored-value-api/void"
raw_files:
  - "adyen/docs/payment-methods/gift-cards/stored-value-api/void/2026-09-15.md"
tags: [adyen, gift-cards, stored-value, void, online-payments]
---

## Overview

This 2026-09-15-captured Adyen guide describes the synchronous Stored Value API `POST /voidTransaction` operation for undoing eligible gift-card or other stored-value transactions made with that API in the past 24 hours. It distinguishes this reversal from canceling a gift-card payment or refunding to a gift card. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Scope and time limit:** `/voidTransaction` can undo eligible `/issue`, `/changeStatus`, `/load`, or `/mergeBalance` Stored Value API transactions from the preceding 24 hours. The page says the operation is synchronous. Eligibility still depends on the original transaction, provider and channel; the table is the detailed route. [Raw: lines 19, 30–56]
- **Payment boundary:** This operation is unrelated to a payment. It cannot cancel a gift-card payment or make a refund to a gift card; the guide links separate online and in-person cancellation and refund documentation. [Raw: lines 21–28]
- **Provider/channel restrictions:** The captured table allows voiding online load amounts for Givex, SVS, Fiserv (formerly ValueLink) and Intersolve, and online balance merges only for Fiserv. For in-person transactions, it allows load amount for all four and activation or activation-with-load only for SVS; it marks in-person issue and merge as unavailable. Consult each row before selecting an operation; the 24-hour window alone does not confer eligibility. [Raw: lines 32–52]
- **Request identity:** The POST uses `merchantAccount`, `originalReference` equal to the `pspReference` of the transaction to undo, and a unique `reference` of at most 80 characters; `store` is optional for transactions flagged as in-store. The JSON request is an illustrative payload. [Raw: lines 54–80]
- **Response lifecycle:** The response describes `currentBalance` currency and total value, a new 16-character `pspReference` for this request, and `resultCode` for request state; additional merchant-setting-dependent fields may appear. The sample shows `Success`, but is not evidence of a performed reversal or the balance of a real card. [Raw: lines 82–103]
- **Cross-page conflict:** The broader Stored Value API overview's provider/channel matrix marks void broadly available for all four providers in online and in-person channels, whereas this operation-specific page excludes several transaction rows, especially issue, deactivate and merge. The overview also differs from this page on availability of some underlying actions. Preserve both matrices and use the operation-specific rows for the documented void conditions; see [[source-adyen-docs-payment-methods-gift-cards-stored-value-api]].

> [!WARNING] Void is not payment cancellation or refund
> A successful Stored Value API void response is about undoing an eligible stored-value operation; it does not establish cancellation or refund of a gift-card payment. [Raw: lines 19–28, 82–103]

## Detail locators

- Endpoint purpose, 24-hour window and payment boundary: pinned raw lines 15–28.
- Online versus in-person provider/transaction eligibility matrix: pinned raw lines 30–52.
- Request fields and example: pinned raw lines 54–80.
- Response fields, merchant additional-data qualification and sample: pinned raw lines 82–103.
- Links to related Stored Value API transactions: pinned raw lines 105–123.

## Related

- [[adyen-online-payments]] — provider online-payment and payment-method route.
- [[source-adyen-docs-payment-methods-gift-cards-stored-value-api]] — broader Stored Value API overview with a less specific provider/channel matrix that conflicts with this page.

## Raw Sources

- [[raw/adyen/docs/payment-methods/gift-cards/stored-value-api/void/2026-09-15|Stored Value API void guide, captured 2026-09-15]]
