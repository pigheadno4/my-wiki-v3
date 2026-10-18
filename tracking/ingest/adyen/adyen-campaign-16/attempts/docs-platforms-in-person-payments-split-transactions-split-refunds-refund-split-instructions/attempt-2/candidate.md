---
title: "Split an in-person refund with Terminal API instructions"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/in-person-payments/split-transactions/split-refunds/refund-split-instructions"
raw_files:
  - "adyen/docs/platforms/in-person-payments/split-transactions/split-refunds/refund-split-instructions/2026-09-15.md"
tags: [adyen, platforms, in-person-payments, refunds, split-payments]
---

## Overview

This Adyen for Platforms page, last modified 2024-01-24 and captured 2026-09-15, explains how to supply split instructions in a *referenced* in-person Terminal API reversal refund. It can allocate refunded sale value, platform commission and refund transaction fees among balances originally credited by the payment. This is a Terminal API procedure for a terminal or Mobile solution, not an unreferenced refund flow or proof that a refund reached a shopper.

## Key takeaways

- General in-person Platforms requirements also apply. The guide requires a Terminal API integration with payment terminals or a Mobile solution, and listening for `CANCEL_OR_REFUND` outcome events. A standalone solution cannot add split instructions to individual referenced refund requests. Some payment methods do not support partial or repeated partial refunds. Refund deductions are limited to balance accounts credited by the original payment.
- For a partial refund, obtain the original payment's `POIData.POITransactionID.TransactionID` and `TimeStamp`, plus its original `split.item[ITEM_NUMBER].reference` values from transfer webhooks. The refund reversal must reuse those split references. Build the instructions as ampersand-separated key-value pairs or Base64-encoded JSON in `SaleData.SaleToAcquirerData`; include a separate partial-refund `currency` matching the original payment currency. The raw USD 80-to-USD 40 example debits USD 37.50 from a user balance account and USD 2.50 commission from the platform liable account; those values and currency are illustrative.
- Send a Terminal API `ReversalRequest`, not a payment request, with a Service/Reversal request header (ProtocolVersion 3.0), the original `POITransactionID` and UTC timestamp, and `ReversalReason=MerchantCancel`. Partial refunds require `ReversedAmount` as a decimal amount in major units, not minor units, and `SaleData.SaleTransactionID` with refund reference and UTC timestamp; a unique reference per partial refund is recommended. `SaleToAcquirerData` carries the split instructions and matching currency. The ServiceID must be 1–10 alphanumeric characters and unique for that terminal within 48 hours.
- For a full referenced refund with custom split instructions, the page omits `ReversedAmount` and says a separate `currency` parameter is unnecessary; the full amount of the referenced payment is used. Its full-refund example uses different split values from the original payment. A separate “original split ratio” guide is linked under See also; this page does not establish that guide's fallback behavior for omitted split instructions.
- `ReversalResponse.Response.Result=Success` means Adyen received the request. The receipt says `REFUND REQUESTED`; `ReversedAmount` in the partial response is an amount to attempt authorization, and the response table labels `POIData.POITransactionID.TransactionID` a refund PSP reference. But the displayed response has `TF995R5G6L2GWR82` there and a different `AdditionalResponse.pspReference` (`KHLWK3Z3FZTQ7RT5`). These illustrative values do not establish one-to-one refund-reference matching. A failed request returns `Failure` with an explanation. Refunds are processed asynchronously; wait for `CANCEL_OR_REFUND` to learn the refund outcome.
- Transfer and transaction webhooks are described per split item, with outgoing `BalanceAccount`, `PaymentFee` and `Commission` examples progressing through received, authorised, refunded and booked balance movements. The page explicitly says these transfer and transaction webhook payload examples are based on an online refund request. Their stages and identifiers illustrate balance-platform booking, not an observed Terminal reversal trace. The online-derived examples use `modificationPspReference=QFQTPCQ8HXSKGK82`, distinct from both PSP-reference values in the displayed Terminal response; the examples do not establish that all three identify one refund or which field matches a real reversal. Reconcile actual event payloads using the relevant current API and webhook contracts. The examples are test-environment illustrations, not live customer-refund proof. The fund-tracking prose says funds are “credited,” while its refund examples show outgoing deductions; follow the specific event direction and amount rather than that general wording. A commission transaction example also names user-account IDs despite the surrounding liable-account narrative.

## Detail locators

- `## Requirements`: Terminal API/Mobile scope, standalone exclusion, `CANCEL_OR_REFUND`, payment-method limits and original credited-account restriction.
- `## Make a partial refund with split instructions`: original references, key-value/Base64 formats, currency, Terminal API reversal fields, decimal `ReversedAmount`, response and asynchronous outcome.
- `## Full refund with split instructions`: reduced field set, no separate currency or `ReversedAmount`, different split example.
- `## Track fund movements`: transfer/transaction webhooks and split-item status examples, with wording/example inconsistencies noted above.
- `## See also`: referenced refund, outcome webhook and separate original-split-ratio route; linked pages are navigation.

## Related

- [[adyen-platforms]] — provider platform concept and source route.
- [[adyen]] — provider profile.

## Raw Sources

- [[raw/adyen/docs/platforms/in-person-payments/split-transactions/split-refunds/refund-split-instructions/2026-09-15|Adyen refund with split instructions (fetched 2026-09-15)]]
