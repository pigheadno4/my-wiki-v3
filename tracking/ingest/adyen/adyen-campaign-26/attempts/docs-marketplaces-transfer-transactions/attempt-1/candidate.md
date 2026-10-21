---
title: "Track Adyen Marketplace balance-platform transactions and transfers"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/transfer-transactions"
raw_files:
  - "adyen/docs/marketplaces/transfer-transactions/2026-09-15.md"
tags: [adyen, marketplaces, platforms, transfers, transactions, reconciliation]
---

## Overview

This 2026-09-15 Marketplace-path tracking hub says that each fund movement on the balance platform results in a transaction. It routes readers to real-time Transfers/Transactions webhooks or on-demand Transfers API tracking and summarizes transfer lifecycle states. It describes balance-platform reconciliation signals, not a payment-initiation or payout-execution endpoint; source-account deduction, a transaction row or a report entry does not independently prove recipient-bank credit. [[adyen]] [[adyen-platforms]]

## Key takeaways

- The transfer-lifecycle table says `authorised` means a valid request with funds reserved; `booked` means funds deducted from the **source balance account**; `failed` means initiation failed, for example insufficient funds; `refused` means clearing-system or recipient-bank rejection; and `returned` means funds were sent but returned by the receiving bank. `booked` is not a bank-receipt or irreversible-finality guarantee. See raw lines 21-31.
- For tracking, this hub links a real-time Transfers and Transactions webhook guide and an on-demand Transfers API guide. It provides no endpoint parameters, correlation-key specification or full transaction-status schema itself; follow the child guides for those details. See raw lines 33-47.
- For `failed` or `refused`, the page states that funds are not deducted from the balance account and advises notifying the user and checking bank-account details or balance status. This is a diagnostic step, not automatic retry authorization. See raw lines 49-53.
- A receiving bank can return a transfer **several days after initiation**. In that case Adyen says it sends `balancePlatform.transfer.updated` with `returned`, credits the original balance account, and records a **separate** Balance Platform Accounting Report entry. Continue monitoring after any prior source-side debit; the page does not state a fixed return deadline or bank-receipt proof. See raw lines 55-61.

## Detail locators

- `# Track transactions`, raw lines 15-19: balance-platform movement/transaction framing and tracking purpose.
- `## Transfer lifecycle`, raw lines 21-31: status definitions and source-versus-bank boundary.
- `## Choose a tracking method`, raw lines 33-47: webhook and Transfers API child routes.
- `## Handle exceptions`, raw lines 49-61: failed/refused non-deduction, possible later return, original-account credit and separate accounting-report entry.
- `## See also`, raw lines 63-66: payout reconciliation and transfer-detail navigation.

## Related

- [[adyen-platforms]] — owning modern Platforms/Marketplace context.
- [[source-adyen-docs-marketplaces-transfer-transactions-track-webhooks]] — separately pinned webhook method guide.
- [[source-adyen-docs-marketplaces-transfer-transactions-track-api]] — separately pinned Transfers API query guide.
- [[source-adyen-docs-platforms-transfer-transactions]] — separately pinned Platforms-path tracking hub.
- [[adyen-reporting]] — report context; this hub alone does not define accounting report row grain.

## Raw Sources

- [[raw/adyen/docs/marketplaces/transfer-transactions/2026-09-15|Adyen Marketplace track-transactions hub, captured 2026-09-15]]
