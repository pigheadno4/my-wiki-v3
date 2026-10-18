---
title: "Capital repayment | Adyen"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/capital/repayment"
raw_files:
  - "adyen/docs/capital/repayment/2026-09-15.md"
tags: [adyen, capital, repayment, scheduled, unscheduled, platforms]
---

## Overview

This [[adyen]] Capital guide, captured 2026-09-15, distinguishes default sale-volume-linked **scheduled** repayment from optional user-initiated **unscheduled** repayment toward an outstanding grant. Both modes are described for component and API-only integrations, subject to the unscheduled region and component-version conditions below. The page describes mechanisms, not any particular grant's terms, actual repayment or final debt state. See [[adyen-capital]].

## Key takeaways

- Scheduled repayment reserves a fixed percentage of **net captured volume** immediately on capture; the page defines net captured volume as captured funds minus refunded or charged-back funds. At the end of each sales day, Adyen deducts the reserved amount from the user's balance account. A day with negative net captured volume instead releases that day's reserved amount and triggers no repayment from that release. The exact percentage and grant terms are not supplied here. [Raw: lines 19, 25–29]
- Adyen calculates a threshold amount as the minimum expected repayment per 30-day period for the maximum repayment term. If a period's repayment is below that threshold, Adyen **may** take additional steps to secure timely repayment; this page neither specifies those steps nor proves a particular user is delinquent. [Raw: line 31]
- The captured page limits unscheduled repayments to users operating in **Europe, the United Kingdom and the United States**. A user can make one by transferring funds to the **dedicated bank account assigned to each disbursement**, from the user's verified bank account/transfer instrument. API-only platforms retrieve and share those dedicated details; component users can view/copy details for an active grant from component library version **1.4.0**. A visible account detail or initiated bank transfer is not evidence of a booked Capital repayment. [Raw: lines 33–44]
- Unscheduled repayment can support early payoff or covering missed payments and requires additional platform steps. The guide does not itself show bank-credit confirmation, allocation to principal/fee, a `Repaid` grant status or the live user-specific amount owed; follow the linked reporting and grant-status guides for those separate evidence questions. [Raw: lines 19–23, 46–50]

## Detail locators

- Repayment modes and implementation-method scope: raw lines 17–23.
- Scheduled reservation, negative-volume release and 30-day threshold: raw lines 25–31.
- Unscheduled region restriction, per-disbursement bank details, API-only/component paths, version and verified source account: raw lines 33–44.
- Related reconciliation/status/webhook guide routes: raw lines 46–50.

## Related

- [[adyen-capital]] — Capital financing context and evidence boundary
- [Reporting and reconciliation](https://docs.adyen.com/capital/reporting-and-reconciliation) — linked booking/report route
- [Grant lifecycle and status](https://docs.adyen.com/capital/grant-lifecycle-and-status) — linked grant-state route
- [Manage disbursements](https://docs.adyen.com/capital/manage-disbursements) — linked dedicated-account detail route

## Raw Sources

- [[raw/adyen/docs/capital/repayment/2026-09-15|Adyen Capital repayment — collected 2026-09-15]]
