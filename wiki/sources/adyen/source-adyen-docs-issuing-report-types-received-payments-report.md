---
title: "Adyen Issuing: Received Payments Report (deprecated)"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/report-types/received-payments-report"
raw_files:
  - "adyen/docs/issuing/report-types/received-payments-report/2026-09-15.md"
tags: [adyen, issuing, reports, received-payments, deprecated]
---

## Overview

This 2021-modified Issuing report guide, captured 2026-09-15, describes the **deprecated Received Payments Report** for card-user payments made on a selected day. Adyen directs readers to the [[source-adyen-docs-issuing-report-types-balance-platform-accounting-report|Balance Platform Accounting Report]] instead. The legacy report can be generated on a schedule or manually for a selected day or consecutive days in Customer Area; this snapshot does not establish current generation availability. See [[adyen]] and [[adyen-issuing]].

## Key takeaways

- Each report row represents one payment and its latest state at generation time. Adyen recommends generating it **two weeks after** the reported day because an `Authorised` payment may later become `Captured` or `Expired`. The `Journal Type` column says to **expect** final states (`Captured`, `Refused`, `Expired`, `Cancelled`, `Refunded`) at that interval; earlier reports can contain non-final `Authorised`. Thus the report-structure prose calling every row a “final state” must be read with that timing qualification, not as a guarantee.
- The first three lines are a report label, date and “Payments”; the fourth is the header. The named columns identify balance platform, account holder, card-linked balance account, accounting `Transaction Id`, `Journal Type`, an `Authorisation PSP Reference`, `Payment Reference` (described as the payment-instrument identifier), dates/time zones, original acquirer amount/currency and instructed amount/currency deducted from the balance account, entry mode, auth code and merchant details. These identifiers and money amounts have different meanings and should not be collapsed into one payment ID or amount.
- The guide says to include the `Auth Code` when cancelling or refunding a payment. The sample may omit data or columns present in a platform-specific generated report. Its table repeats ordinal **24** for `Counterparty Country` and `MCC`; use column names, not the displayed ordinal, when inspecting this captured schema.
- This is a report description and historical timing recommendation. It does not demonstrate a live report run, a particular payment's final outcome, successful refund, bank receipt or settlement.

## Detail locators

- Pinned raw lines 15–25: deprecated notice, selected-day scope, two-week recommendation and generation routes.
- Pinned raw lines 27–34: sample variation and one-row-per-payment description; lines 36–45: first four report rows.
- Pinned raw lines 46–66: account/payment identifiers, status, dates, original versus instructed amount and auth code; lines 67–85: shopper/merchant fields, repeated column number and reserved columns.

## Related

- [[source-adyen-docs-issuing-report-types-balance-platform-accounting-report]] — recommended replacement.
- [[adyen-issuing]] — Issuing payment/account context.
- [[source-adyen-docs-issuing-payment-stages]] — payment-stage definitions (navigation only).

## Raw Sources

- [[raw/adyen/docs/issuing/report-types/received-payments-report/2026-09-15|Adyen Received Payments Report guide, captured 2026-09-15]]
