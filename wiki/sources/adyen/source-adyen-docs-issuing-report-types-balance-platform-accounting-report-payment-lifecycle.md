---
title: "Adyen Balance Platform Accounting Report payment lifecycle examples"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/report-types/balance-platform-accounting-report/payment-lifecycle"
raw_files:
  - "adyen/docs/issuing/report-types/balance-platform-accounting-report/payment-lifecycle/2026-09-15.md"
tags: [adyen, issuing, accounting-report, payment-lifecycle]
---

## Overview

This 2022-modified guide, captured 2026-09-15 on Adyen's Issuing path, illustrates how to follow issued-card payment events in the Balance Platform Accounting Report. It points to `Category`, `Type`, `Status`, and `Booking Date` to distinguish event rows and their reporting dates; these are report illustrations, not evidence that any particular payment reached capture, refund, or settlement. [[adyen]] [[adyen-issuing]]

## Key takeaways

- For this report, `issuedCard` is the category illustrated for an activity using a physical or virtual issued card. `Type` names the event kind and `Status` its state. Events appear on the day of the status update; inspect `Booking Date` rather than assuming authorization and capture appear together (raw lines 19–27). The sentence giving the August 15/18 example contains duplicated/garbled received-status wording, so rely on the stated date principle and actual report rows, not that sentence's status enumeration (raw line 25).
- The worked purchase uses original GBP 4 and EUR 4.46 in a EUR default balance account. Its captured example shows `received`, `authorised`, then `captured` rows sharing a Transfer Id, while the captured row adds a Transaction Id; this is the example's row pattern, not a universal identifier or booking rule (raw lines 31–44).
- A partial-capture example shows a GBP 2 / EUR 2.15 captured row and a later `expired` row for the outstanding amount; the prose says the outstanding amount expires after seven days (raw lines 46–55). Separate tables illustrate cancellation, `authAdjustmentAuthorised` and refund rows (raw lines 57–89).
- The cancellation prose says the cafe cancels instead of partially capturing, yet its table includes both a `cancelled` row and a `captured` row for the same Transfer Id (raw lines 57–66). Preserve that mismatch; do not infer that cancellation prevents every capture or that this table is a general rule. The refund sample also mixes original GBP amount signs with positive EUR `received`/`authorised` values, so use it as a located example rather than a sign-convention specification (raw lines 79–89).

## Detail locators

- Report column purpose, status-update date, and cross-currency premise: raw lines 19–36. Captured example and row identifiers/register columns: raw lines 38–44.
- Partial capture plus expiry: raw lines 46–55. Cancellation table discrepancy: raw lines 57–66. Authorization adjustment: raw lines 68–77. Refund example: raw lines 79–89.

## Related

- [[adyen-issuing]] — Issuing program and reciprocal source route.
- [[source-adyen-docs-issuing-report-types-balance-platform-accounting-report]] — parent report definition, scope and column reference.
- [[adyen-reporting]] — broader report-navigation context.

## Raw Sources

- [[raw/adyen/docs/issuing/report-types/balance-platform-accounting-report/payment-lifecycle/2026-09-15|Payment lifecycle examples, captured 2026-09-15]]
