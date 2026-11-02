---
title: "Adyen Terminal API POST /gettotals — GetTotals Request"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/terminal-api/latest/post/gettotals"
raw_files:
  - "adyen/api-explorer/terminal-api/latest/post/gettotals/2026-09-15.md"
tags: [adyen, terminal-api, api-explorer, reconciliation, totals]
---

## Overview

This 2026-09-15 API Explorer snapshot documents the Terminal API `POST /gettotals` GetTotals request: the Sale System specifies the scope and format of totals for the POI System to compute. It lists test cloud Device API sync and async endpoints with `{merchantAccount}` and `{deviceId}`, plus a local-terminal-IP route; it gives no separate numeric Terminal API protocol or software version. [[adyen]] [[adyen-terminal-api]]

## Key takeaways

- The request body table marks `TotalDetails` and `TotalFilter` optional. `TotalDetails` selects a totals hierarchy from `OperatorID`, `POIID`, `SaleID`, `ShiftNumber`, and `TotalsGroupID`; `TotalFilter` can restrict the computation by those optional values. These identify cashier/operator, POI or sale system/terminal, shift, and totals group; the cloud URL's merchant account and device ID identify the transport target.
- The documented `200 Success` body is a Reconciliation Response about POI processing. It requires `Response` with `Result` (`Success`, `Failure`, or `Partial`) and `POIReconciliationID`, the Sale-to-POI reconciliation-period identifier. The `Response` description makes `ErrorCondition` present in non-success cases; `AdditionalResponse` is optional logging detail.
- `TransactionTotals` is optional and described for `Response.Result=Success`. Its `PaymentInstrumentType` is required within an item. `PaymentTotals` is optional within an item and described when both count and amount are nonzero; its entries require `TransactionType`, `TransactionCount`, and `TransactionAmount`. The listed transaction types include debit, credit, reversals, reservations, declined, and failed transactions. These are period totals, not proof of capture, settlement, payout, or bank receipt.
- This page does not specify request-body envelope/header fields, authentication, credential handling, response correlation, async delivery timing, retry rules, period rollover effects, numeric limits, or defaults. The sync/async endpoint labels alone do not establish a final financial outcome.

## Detail locators

- Servers and routing: [[raw/adyen/api-explorer/terminal-api/latest/post/gettotals/2026-09-15#L10|raw lines 10–19]].
- Request fields and optional filters: [[raw/adyen/api-explorer/terminal-api/latest/post/gettotals/2026-09-15#L21|raw lines 21–32]].
- Response result, error conditions, period ID, and totals nesting: [[raw/adyen/api-explorer/terminal-api/latest/post/gettotals/2026-09-15#L34|raw lines 34–62]].

## Related

- [[adyen-terminal-api]] — in-person Terminal API architecture and reconciliation routes.
- [[source-adyen-docs-point-of-sale-reconciling-totals-retrieve-totals-from-the-terminal]] — separate website procedure for retrieving terminal totals.
- [[adyen]] — provider overview.

## Raw Sources

- [[raw/adyen/api-explorer/terminal-api/latest/post/gettotals/2026-09-15|Adyen Terminal API GetTotals API Explorer capture, 2026-09-15]]
