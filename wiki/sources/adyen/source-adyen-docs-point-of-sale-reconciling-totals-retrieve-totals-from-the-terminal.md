---
title: "Retrieve totals from the terminal | Adyen Docs"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/reconciling-totals/retrieve-totals-from-the-terminal"
raw_files:
  - "adyen/docs/point-of-sale/reconciling-totals/retrieve-totals-from-the-terminal/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, terminal-totals, reconciliation]
---

## Overview

Adyen's Terminal API `GetTotals` guide shows how a merchant POS retrieves payment totals from a terminal, optionally filtered or grouped by terminal, sale system, operator, shift, or totals group. It says this read does **not start a new reconciliation period**. The pinned webpage was fetched 2026-09-15 and reports `last_modified` 2019-08-20; the worked result is illustrative, not evidence of current terminal state or settled funds. [[adyen]] [[adyen-terminal-api]]

## Key takeaways

- A Terminal API integration with payment terminals is the stated requirement. The procedure first directs the operator to log in to the terminal, then has the POS send a `SaleToPOIRequest` with `MessageCategory: GetTotals`, `MessageClass: Service`, and `GetTotalsRequest`. The page's request table requires a `ServiceID` unique for the terminal `POIID` over 48 hours. The linked login procedure is separate evidence; this page does not define its credentials or period effects.
- `GetTotalsRequest.TotalFilter` limits which totals are returned, whereas `TotalDetails` groups the results. The page lists terminal `POIID`, sale system, operator, shift number, and totals group for both purposes. Its examples filter one terminal, filter that terminal plus `TotalsGroupID`, and group one terminal's results by `OperatorID`.
- Read `GetTotalsResponse.TransactionTotals` for totals. The sample `Success` response also shows `POIReconciliationID`, payment instrument type and currency, optional operator/group/shift descriptors, and `PaymentTotals` entries with transaction type, count, and amount. The introduction describes totals by payment instrument and transaction type; the sample numbers are examples, not live counts or financial-settlement records.
- The page does not specify a time-window selector, reset/close action, receipt payload, payout, capture, bank deposit, or accounting finality. It establishes a terminal-total read; use the separate login/logout and reconciliation-period authorities for period transitions and financial reports for settlement.

## Detail locators

- Purpose, no new period, value/count dimensions, and integration requirement: pinned raw, introduction and `## Requirements` (lines 15–27).
- Login direction, `GetTotals` header and `ServiceID` requirement: pinned raw, `## Get the totals of a terminal` (lines 29–47).
- Filter versus group fields and terminal/group/operator request examples: pinned raw, `GetTotalsRequest` table and three example tabs (lines 47–219).
- `TransactionTotals`, `POIReconciliationID`, instrument/currency and transaction count/amount sample: pinned raw, response example (lines 221–278).

## Related

- [[adyen-terminal-api]] — provider Terminal API message concept.
- [[source-adyen-docs-point-of-sale-reconciling-totals]] — terminal-total reconciliation navigation hub.
- [[adyen]] — provider hub.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/reconciling-totals/retrieve-totals-from-the-terminal/2026-09-15|Retrieve totals from the terminal — 2026-09-15 snapshot]]
