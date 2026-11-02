---
title: "Adyen Terminal API latest Reconciliation request"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/terminal-api/latest/post/reconciliation"
raw_files:
  - "adyen/api-explorer/terminal-api/latest/post/reconciliation/2026-09-15.md"
tags: [adyen, terminal-api, api-explorer, reconciliation, transaction-totals]
---

## Overview

This 2026-09-15 API Explorer **Terminal API latest** `POST /reconciliation` snapshot describes a Reconciliation request from the Sale System and a response about a reconciliation transaction processed by the POI System. The listed cloud endpoints are TEST `/v1/merchants/{merchantAccount}/devices/{deviceId}/sync` and `/async`; local hosting is represented only by `<local-terminal-IP-address>`. The page does not pin a numbered Terminal API schema version. [[adyen]] [[adyen-terminal-api]]

## Key takeaways

- The request-body table requires `ReconciliationType`: `SaleReconciliation`, `AcquirerSynchronisation`, `AcquirerReconciliation`, or `PreviousReconciliation`. Optional `AcquirerID` is an integer array allowed only for the two Acquirer types. Optional integer `POIReconciliationID` is absent unless the type is `PreviousReconciliation`. The table does not define the actions or period transition performed by each type; see raw lines 23–28.
- The response-body table requires `Response`, its `Result` (`Success`, `Failure`, or `Partial`), and `ReconciliationType`. The prose says `ErrorCondition` is absent or unused for `Success` and must be present otherwise, while the table marks that field “No.” The `200 Success` heading therefore does not guarantee a successful message result. Optional response `POIReconciliationID` is absent for `AcquirerReconciliation`; see raw lines 30–44.
- Optional `TransactionTotals` is described as the Sale-to-POI reconciliation result if `Response.Result` is `Success`. Within each present item, `PaymentInstrumentType` is required; acquirer, host-period, card-brand, terminal, sale, operator, shift, totals-group, currency, and `PaymentTotals` fields are optional or conditional. The response describes `POIID`, `SaleID`, `OperatorID`, `ShiftNumber`, and `TotalsGroupID` as sent if requested, but the captured request-body table shows no corresponding selector fields. If a `PaymentTotals` item is present, its `TransactionType`, `TransactionCount`, and `TransactionAmount` are required; the `PaymentTotals` description says it is present if both count and amount are nonzero. See raw lines 45–59.
- This operation describes POI reconciliation processing and aggregate transaction totals. It provides no full Terminal API message envelope, caller credential or role, request correlation rule, session lifetime, timeout, retry or reversal procedure, asynchronous delivery contract, or evidence of payment authorization, capture, financial settlement, or bank receipt.

## Detail locators

- TEST cloud and local-hosting server labels: raw lines 10–19.
- Request types and conditional identifiers: raw lines 21–28.
- Response status and period ID: raw lines 30–44.
- Transaction totals, nested required properties, and conditional fields: raw lines 45–59.

## Related

- [[adyen-terminal-api]] — provider concept and reciprocal source route.

## Raw Sources

- [[raw/adyen/api-explorer/terminal-api/latest/post/reconciliation/2026-09-15|Adyen API Explorer Reconciliation raw snapshot]]
