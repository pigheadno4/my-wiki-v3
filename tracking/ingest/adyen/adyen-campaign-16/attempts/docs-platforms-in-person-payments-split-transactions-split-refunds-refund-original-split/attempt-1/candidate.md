---
title: "Adyen Platforms in-person refund original split"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/in-person-payments/split-transactions/split-refunds/refund-original-split"
raw_files:
  - "adyen/docs/platforms/in-person-payments/split-transactions/split-refunds/refund-original-split/2026-09-15.md"
tags: [adyen, platforms, in-person-payments, refunds, split-transactions]
---

## Overview

This Adyen for Platforms guide (last modified 2024-01-24; captured 2026-09-15) describes a referenced Terminal API reversal that uses the original payment-request split allocation without sending new split instructions. Its worked request is a full refund. The page does not specify partial-refund ratio arithmetic or how a later capture-time override would affect an inherited split. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- **Prerequisites and reference:** The guide assumes the general Platforms in-person requirements, a Terminal API terminal or mobile integration, and CANCEL_OR_REFUND webhook handling. Read the original payment response's POIData.POITransactionID.TransactionID and TimeStamp; the identifier contains tenderReference.pspReference. Send a Terminal API Reversal request with OriginalPOITransaction.POITransactionID, MessageCategory Reversal, ProtocolVersion 3.0 in the example, and ReversalReason MerchantCancel. Do not add split instructions when requesting the same original payment-request allocation.
- **Outcome boundary:** ReversalResponse.Response.Result Success means Adyen received the request; the receipt says REFUND REQUESTED, and posOriginalAmountValue/posAuthAmountValue are minor-unit amounts in AdditionalResponse. It does not mean the refund succeeded. The refund is asynchronous, and the CANCEL_OR_REFUND webhook reports the outcome. Failure response messages can indicate missing original PSP reference or that a full reversal was already received. The original payment PSP reference differs from the refund-request PSP reference.
- **Balance movement:** The example maps the refunded sale share to a debit from a user's balance account and refunded commission to a debit from the platform liable balance account; Transfer created/updated and Transaction created webhooks trace per-split received, authorised, refunded and booked stages. Those ledger states do not themselves prove customer bank/card receipt. The page does not state a nonexistent/closed target-account fallback for this refund path.
- **Example conflicts:** The request example says full USD 188, but later sample debits show USD 75 user share and inconsistent commission values (USD 10 in one received event versus USD 5 later). Fee prose first says the account specified in the request, although this request has no new split instructions; it then says liable balance, while fee sample payloads identify a user's second balance account. Treat these as inconsistent test examples, not a definitive fee-account or full/partial refund formula. Confirm actual allocation through current schema and observed per-split events.

## Detail locators

- Original-split purpose, Terminal API and webhook requirements: pinned raw lines 15-28.
- Original transaction ID/time, reversal fields and full-refund request example: pinned raw lines 30-85.
- Success-as-receipt, minor-unit response values, failure examples and asynchronous CANCEL_OR_REFUND: pinned raw lines 87-138.
- Per-split transfer/transaction status and user/liable example roles: pinned raw lines 140-155, 157-767.
- Conflicting fee-account prose and test payloads: pinned raw lines 768-1074.

## Related

- [[adyen-platforms]] — platform payments concept and reciprocal source route.
- [[source-adyen-docs-platforms-in-person-payments-split-transactions-split-payments-at-authorization]] — separate initial split request.
- [[source-adyen-docs-platforms-in-person-payments-split-transactions-split-payments-at-capture]] — separate capture-time override.

## Raw Sources

- [[raw/adyen/docs/platforms/in-person-payments/split-transactions/split-refunds/refund-original-split/2026-09-15|Adyen Refund with original split ratio, captured 2026-09-15]]
