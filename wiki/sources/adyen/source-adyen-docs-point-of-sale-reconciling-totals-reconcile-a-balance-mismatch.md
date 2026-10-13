---
title: "Reconcile a balance mismatch | Adyen Docs"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/reconciling-totals/reconcile-a-balance-mismatch"
raw_files:
  - "adyen/docs/point-of-sale/reconciling-totals/reconcile-a-balance-mismatch/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, reconciliation, balance-mismatch]
---

## Overview

Adyen's Terminal API reconciliation guide shows how a merchant POS gets a terminal reconciliation-period total when its balance differs from the terminal's, for example after a dropped connection leaves the POS without a final payment response. The pinned webpage was fetched 2026-09-15 and reports `last_modified` 2019-08-20. It documents a terminal-totals request and example response, not a bank settlement, funds adjustment, or automated mismatch resolution. [[adyen]] [[adyen-terminal-api]]

## Key takeaways

- A Terminal API integration with payment terminals is required, and the procedure directs login to the terminal first. The POS sends a `SaleToPOIRequest` with `MessageCategory: Reconciliation` and a `ReconciliationRequest`. The request table requires `ServiceID` unique within 48 hours for the terminal `POIID`. The linked login guide owns any operator/group/shift login behavior; this page does not define that procedure.
- **Choose the reconciliation type deliberately:** `SaleReconciliation` gets the current period's terminal totals **and starts a new reconciliation period**. `PreviousReconciliation` gets a report for a previous period **without starting a new period** and calls for `POIReconciliationID`. The raw instructions show the literal value `NNN` for that field; this page does not define it as a usable real period identifier or a full ID-format contract.
- The POS checks `ReconciliationResponse.TransactionTotals`. The `SaleReconciliation` sample shows `POIReconciliationID`, `Response.Result: Success`, instrument type/currency, transaction type/count/amount, and sale/operator/totals-group/shift descriptors. Use actual terminal totals to investigate a POS-versus-terminal mismatch; the sample values are not a live balance.
- This guide does not provide a detailed comparison algorithm, identify which individual transaction was missed, describe a Balances report, or authorize automatically replaying a missing payment. It also does not describe settlement, payout, bank funds correction, or accounting sign-off. The separate `GetTotals` source is a terminal-total read that does not start a new period; these `ReconciliationType` operations have different period effects.

## Detail locators

- Purpose, missing-response example, and `SaleReconciliation` versus `PreviousReconciliation` effects: pinned raw, introduction (lines 15–25).
- Terminal API requirement, login direction, header IDs and required `ReconciliationType`: pinned raw, `## Requirements` and `## Make a reconciliation request` (lines 27–59).
- `SaleReconciliation` JSON/Java request examples: pinned raw, `## Make a reconciliation request` (lines 61–104).
- `ReconciliationResponse.TransactionTotals` sample, `POIReconciliationID`, operator/group/shift and count/amount: pinned raw, response example (lines 106–147).

## Related

- [[adyen-terminal-api]] — Terminal API operational message concept.
- [[source-adyen-docs-point-of-sale-reconciling-totals-retrieve-totals-from-the-terminal]] — read terminal totals without starting a new period.
- [[source-adyen-docs-point-of-sale-reconciling-totals]] — reconciliation topic hub.
- [[adyen]] — provider hub.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/reconciling-totals/reconcile-a-balance-mismatch/2026-09-15|Reconcile a balance mismatch — 2026-09-15 snapshot]]
