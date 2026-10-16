---
title: "Adyen balance transfers in settlement batches"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/reporting/balance-transfers"
raw_files:
  - "adyen/docs/reporting/balance-transfers/2026-09-15.md"
tags: [adyen, reporting, balance-transfer, settlement-batch, payout-reconciliation]
---

## Overview

This Adyen guide describes how to investigate a balance transfer between settlement batches during payout-batch reconciliation. It routes the **reason** to the Company Payout report's `BalanceTransfer` sheet and the **batch direction and amount** to a `Balancetransfer` entry in the Settlement details report. The page was last modified in 2023 and captured 2026-09-15. A transfer entry or blocked-payout reason is a dated report observation, not proof of a bank transfer, completed payout, resolved configuration, or final settlement. See [[adyen]] and [[adyen-reporting]].

## Key takeaways

- **Two report scopes:** The Company Payout report provides a `Reason Code` on its `BalanceTransfer` sheet; the Settlement details report identifies the batch the balance moved to or from. Balance notices may also be available by email or the Customer Area Notification center. The guide's workflow is to identify the reason and then the settlement entry; one report alone does not supply both meanings.
- **Why balances move:** Listed reason codes cover missing/incorrect deposit configuration, missing liability-risk configuration, settlement-flow configuration error, increased required deposit due to exposure, negative Next Payout or in-process funds, payout-account details/currency problems, and blocked payouts. Several codes explicitly move a payout balance to a **next** settlement batch. `MPL_EXCEEDED` instead describes moving an amount from the balance to reach a required deposit. Use the exact code and raw section; do not collapse all transfers into a payout attempt or bank rejection.
- **Actions and qualifications:** For missing deposit, liability-risk, or settlement-flow setup, the guide directs the merchant to an Account Manager or Support. For increased required deposit it points a **Merchant financial** role holder to the Customer Area Deposit tab. Negative-balance sections discuss adding funds to Reserve; payout-account sections discuss checking account details and, where the payout currency is unsupported, conversion to the primary payout currency at the creation-date exchange rate. These are code-specific troubleshooting directions, not evidence that the issue was fixed.
- **Settlement-entry reading:** `Type=Balancetransfer` identifies the entry; `Modification Merchant Reference` states whether it is to a following or from a previous batch. `Net Currency` gives the net-amount currency; positive transfers use `Net Credit`, negative transfers use `Net Debit` per the page. The example shows a EUR 4.19 `Net Debit` in batch 123 with “to batch 124,” and a corresponding `Net Debit` example in batch 124 with “from batch 123.” Do not infer a universal opposite-sign or debit/credit pairing from those illustrative rows.
- **Financial boundary:** The next-batch designation and payout-account or bank-detail reason codes explain report movement or blockage in this guide. They do not establish when or whether money reached a bank account, the ownership of funds, or the merchant's final accounting treatment.

## Detail locators

- Lines 15–31: definition, Company Payout versus Settlement details versus notice routes, and two-step reconciliation workflow.
- `## 1. Find the balance transfer reason`, lines 33–46: `BalanceTransfer` sheet and reason-code index.
- Reason-code subsections, lines 48–133: code-specific cause, next-batch/deposit effects, role and follow-up guidance, primary payout-currency conversion.
- `## 2. Find the balance transfer entry in the Settlement details report`, lines 135–149: type, net currency, batch-direction reference, and debit/credit fields.
- `### Example`, lines 151–163: illustrative paired batch rows, not a settlement or bank-receipt guarantee.

## Related

- [[adyen-reporting]] — reciprocal reporting concept.
- [[source-adyen-docs-reporting-settlement-reconciliation-transaction-level-settlement-details-report]] — separate report-grain and field authority.
- [[adyen-account-structure]] — distinct Company and Merchant account scopes.

## Raw Sources

- [[raw/adyen/docs/reporting/balance-transfers/2026-09-15|Balance transfers, captured 2026-09-15]]
