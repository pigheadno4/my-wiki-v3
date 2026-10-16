---
title: "Adyen Manage payout bank account details"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/account/manage-payout-account-details"
raw_files:
  - "adyen/docs/account/manage-payout-account-details/2026-09-15.md"
tags: [adyen, merchant-account, payout-account, bank-details, account-access]
---

## Overview

This [[adyen]] Customer Area guide covers bank-account details for receiving merchant-account-level payouts from Adyen. A payout account must be configured for each merchant account; a merchant accepting payments in multiple currencies may link multiple bank accounts to one merchant account. It distinguishes submitting new or edited live details for Adyen review from copying already approved details across merchant accounts under the same legal entity. The guide does not prove that a specific account is approved or that a payout reached a bank. See [[adyen-account-structure]] for merchant-account scope.

## Key takeaways

- To add a live payout account, **Merchant manage bank accounts** is required. In the selected merchant account, choose the bank account country/region and a supported payout currency, enter details, upload a bank statement, and submit. The page says Adyen reviews new details within two business days and emails the result; submission itself is a request, not approval or activation. The linked supported-currency page owns any current country/currency list. [Raw: Add your payout account > Live, lines 23–39]
- In test, create a test payout account by currency. The page frames this as testing reconciliation and additionally calls for automatic generation of the Settlement details report. It does not establish a live payout destination or bank movement. [Raw: Add your payout account > Test, lines 41–51]
- Approved payout details can be copied to other merchant accounts under the same legal entity with **Merchant manage bank accounts**. The copy flow accepts **Submit** and, according to the guide, applies the change automatically without another approval wait. Copying is limited to already approved details; it is not the same as submitting a new bank account for review. [Raw: Copy payout account details, lines 57–73]
- Viewing configured payout accounts requires **Merchant financial** or **Merchant admin**. Editing requires **Merchant manage bank accounts**, is unavailable while an account is pending approval, and sends the submitted change to Adyen for approval; the page says its team reviews changes within two to three business days and emails the result. [Raw: Check payout account details, lines 75–87; Edit your payout account, lines 89–103]
- Removal also requires **Merchant manage bank accounts**. Choosing **Close this account** and confirming **Yes, close** removes the payout account without Adyen approval; this is a consequential change to payout configuration, not a payment or refund operation. [Raw: Remove a payout account, lines 105–119]
- This 2026-09-15 snapshot has embedded last-modified metadata from 2023. Its stated review periods and supported-currency navigation do not establish current account eligibility, approval status, successful verification, payout execution, or bank receipt.

## Detail locators

- Payout destination and merchant-account/multiple-currency scope: opening, lines 15–21.
- Live add role, country/currency selection, bank statement and review: `Add your payout account > Live`, lines 23–39.
- Test account and Settlement details report prerequisite for reconciliation testing: `Add your payout account > Test`, lines 41–51.
- Approved-detail copy, same-legal-entity scope and automatic change: `Copy payout account details`, lines 57–73.
- View permissions: `Check payout account details`, lines 75–87.
- Pending-approval editing block and reviewed change request: `Edit your payout account`, lines 89–103.
- Removal action and lack of approval step: `Remove a payout account`, lines 105–119.

## Related

- [[adyen]] — provider page.
- [[adyen-account-structure]] — company and merchant-account scope.
- [[source-adyen-docs-reporting-settlement-reconciliation-transaction-level-settlement-details-report]] — reconciliation report referred to by the test procedure.

## Raw Sources

- [[raw/adyen/docs/account/manage-payout-account-details/2026-09-15|Adyen Manage your bank account details (2026-09-15)]]
