---
title: "Adyen Platforms reconcile fund transfers"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/reconciliation-use-cases/reconcile-transfers"
raw_files:
  - "adyen/docs/platforms/reconciliation-use-cases/reconcile-transfers/2026-09-15.md"
tags: [adyen, platforms, reporting, reconciliation, transfers, payouts]
---

## Overview

This 2026-09-15 Adyen for Platforms guide uses the Balance Platform Accounting Report to track internal balance-account transfers and payouts to a user's external bank account or other transfer instrument. It identifies report categories, statuses, transfer and transaction identifiers, reference fields, and an illustrative two-leg internal transfer. Report booking is a balance-platform event, not independent proof that a beneficiary bank received a payout.

## Key takeaways

- The report distinguishes internal balance-account moves (`category=internal`, `type=internalTransfer`) from payouts (`category=bank`, `type=bankTransfer`). A payout is described as funds moving from an account holder's balance account toward an external bank account or other transfer instrument; the reporting method does not establish that external receipt occurred.
- A **Transfer Id** links report events for a transfer leg, but its presence alone does not establish real money movement: the guide treats the pre-booked credit/debit as pending. A populated **Transaction Id** with **Status=booked** marks a balance or payment-instrument booking; if Transaction Id is absent, the guide says money movement has not yet taken place. Match the Transfer Id to relate pre-booked and booked events. Read the account, category/type, status and signed Balance (PC) together rather than equating any one identifier with settlement.
- The internal-transfer example shows a negative EUR 15.00 source-account leg and a positive EUR 15.00 destination-account leg. Each account leg has its own Transfer Id; the two booked rows share a Transaction Id. Earlier `received` and `authorised` rows have empty Transaction Ids and zero Balance (PC), while booked rows carry signed balance changes. The 2022 CEST booking/value timestamps are example data, not a universal same-day rule; retain each report date and timezone when reconciling.
- To identify a specific payout, the guide points to **Description**, **Reference**, or **Reference For Beneficiary**; for a specific internal transfer, **Reference For Beneficiary**. These optional fields should be populated in API requests or sweep configurations for reconciliation, then compared with transfer.created/updated webhooks or Customer Area; sweep configuration can be looked up separately. They are matching aids, not a guarantee of unique bank-side identification.
- The Balance Platform Statement Report is an alternative payout-tracking view showing accounts with balance changes on a day and contributing events. It does not replace independent evidence of beneficiary receipt, nor does either report alone prove final bank settlement.

## Detail locators

- Opening and `## Track a transfer`: movement types, category/type/status and Transfer Id versus Transaction Id.
- `## Track a transfer`, specific-transfer columns: request/sweep references and webhook/Customer Area cross-checks.
- `### Balance Platform Accounting Report`: two-leg EUR 15.00 example, signed Balance (PC), distinct leg Transfer IDs, shared booked Transaction ID, booking/value dates and timezone.
- `## Track payouts using the Statement report`: balance-change alternative.

## Related

- [[adyen-reporting]] — main reporting/reconciliation concept.
- [[adyen-platforms]] — parent Platforms context.
- [[adyen]] — provider profile.

## Raw Sources

- [[raw/adyen/docs/platforms/reconciliation-use-cases/reconcile-transfers/2026-09-15|Adyen reconcile fund transfers (fetched 2026-09-15)]]
