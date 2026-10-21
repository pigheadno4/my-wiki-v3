---
title: "Reconcile Marketplace fund transfers"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/reconciliation-use-cases/reconcile-transfers"
raw_files:
  - "adyen/docs/marketplaces/reconciliation-use-cases/reconcile-transfers/2026-09-15.md"
tags: [adyen, marketplaces, reconciliation, transfers, payouts]
---

## Overview

This pinned Marketplace guide uses the **Balance Platform Accounting Report** to track internal balance-account transfers and payouts from an account holder's balance account to an external bank account or other transfer instrument. It identifies internal transfers as `Category: internal` / `Type: internalTransfer`, and payouts as `Category: bank` / `Type: bankTransfer`. This is balance-platform accounting evidence, not beneficiary-bank receipt evidence. See [[adyen]] and [[adyen-reporting]] (raw lines 15–33).

## Key takeaways

- **Transfer Id** links a transfer's pending credit/debit events. A populated **Transaction Id** on a `booked` row marks a booked balance change; without it, the guide says no money movement has yet taken place. Match the Transaction Id to the Transfer Id for the relevant event. **Balance (PC)** holds the signed balance change (raw lines 24–33).
- For a specific payout, search **Description**, **Reference** or **Reference For Beneficiary**; for a specific internal transfer, use **Reference For Beneficiary**. These values come from request/sweep configuration and are available in transfer created/updated webhooks or Customer Area. The guide recommends populating `description`, `reference` and `referenceForBeneficiary` even though optional, to support reconciliation (raw lines 35–42).
- The EUR 15.00 internal-transfer example shows sender `-15.00` and recipient `+15.00` booked **Balance (PC)** rows. Their **Transfer Ids differ by balance-account leg**, while the booked **Transaction Id** is the same in both sample rows; use the account, sign, status and IDs together rather than assuming one transfer ID across both legs. The table records booking and value dates with **CEST** timezone labels (raw lines 44–55).
- A Balance Platform Statement Report is an alternative payout-tracking route for accounts with a balance change on a given day and the contributing events (raw lines 57–59). A booked `bankTransfer` accounting row records platform-side movement; it does not independently show a beneficiary bank's final credit or exclude a later return.

## Detail locators

- Internal versus bank transfers, Transfer/Transaction IDs and booked-state meanings: raw lines 15–33.
- Specific-transfer reference lookup and webhook routes: raw lines 35–42.
- Signed two-sided internal-transfer example and CEST dates: raw lines 44–55.
- Statement Report alternative: raw lines 57–59.

## Related

- [[adyen]]
- [[adyen-reporting]]
- [[adyen-platforms]]
- [[adyen-platform-internal-transfers]]

## Raw Sources

- [[raw/adyen/docs/marketplaces/reconciliation-use-cases/reconcile-transfers/2026-09-15|Pinned transfer-reconciliation guide]]
