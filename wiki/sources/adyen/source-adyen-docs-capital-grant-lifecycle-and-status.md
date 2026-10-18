---
title: "Capital grant lifecycle and status | Adyen"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/capital/grant-lifecycle-and-status"
raw_files:
  - "adyen/docs/capital/grant-lifecycle-and-status/2026-09-15.md"
tags: [adyen, capital, grants, lifecycle, statuses, webhooks]
---

## Overview

This [[adyen]] Capital status reference, captured 2026-09-15, separates **grant initiation** from **grant management** and defines status meanings. A platform can inspect a grant's `status.code` through the Capital API or subscribe to Capital webhooks; grant management also produces transfer and transaction webhook types. The page defines status semantics, not the observed state of any particular grant. See [[adyen-capital]].

## Key takeaways

- Grant initiation prepares a requested offer while the user applies. Its status updates trigger Capital webhooks only, with **no transfers or transactions** during that stage. Grant management concerns funds disbursed to the user and can trigger Capital, transfer and transaction webhooks. An `Approved` grant is automatically activated by background processing that initiates disbursement, but approval alone is not proof of a booked transfer or beneficiary receipt. [Raw: lines 19–32]
- Initiation statuses are `Requested` (formal request submitted), `Reviewing` (offer accepted and secondary Adyen review), `Approved` (Adyen final approval), `Rejected` (declined) and `Cancelled` (user withdrew the request). In `Reviewing`, changed finances/eligibility may require more business information; the page cites a typical EUR 25,000 total-exposure threshold and says required information for a higher grant must arrive before offer expiry. Do not treat offer acceptance or a typical threshold as guaranteed approval. [Raw: lines 36–44]
- The page describes `Pending` as an accepted offer awaiting required user actions, booking of the grant transaction to the user's balance account, and any security cooldown; signing Terms of Service is called out. A changed bank account has a **72-hour cooldown example**, not a universal timing promise. The `Cancelled` row says cancellation is possible until the grant transaction is booked and transitions to `Pending`, whereas the `Pending` row says the grant remains pending until booking. That booking/status boundary is inconsistent within this captured page; verify the observed API/webhook state and current provider guidance before using it as a transition rule. [Raw: lines 44, 46–52]
- `Failed` means unsuccessful disbursement, including missed required actions before offer expiry or technical/administrative issues; the page says it does not affect future eligibility. `Active` means Adyen says the grant has been disbursed to the user. `Repaid` means repayment obligations were met. `Revoked` is a user-requested, region-rule-dependent legal revocation within a specified post-acceptance window, with principal paid off and fees waived; the page says future eligibility is unaffected. `Written Off` denotes a low-likelihood-of-recovery classification and a period of ineligibility based on risk appetite. These are provider status definitions, not legal advice, current eligibility or evidence of a specific user's final financing/debt outcome or bank receipt. [Raw: lines 53–57]

## Detail locators

- API/webhook observation route and initiation versus management event classes: raw lines 19–34.
- Initiation status table, secondary review, information threshold/expiry and cancellation: raw lines 36–44.
- Management status table, Terms of Service/cooldown, failure, disbursement, repayment, revocation and write-off: raw lines 46–57.
- Related webhook and reconciliation guides: raw lines 59–62.

## Related

- [[adyen-capital]] — Capital product and financing evidence boundary
- [Capital webhook types](https://docs.adyen.com/capital/webhook-types) — linked event structures
- [Capital reporting and reconciliation](https://docs.adyen.com/capital/reporting-and-reconciliation) — linked booked-repayment evidence
- [Collect user data](https://docs.adyen.com/capital/collect-user-data) — linked secondary-review information route

## Raw Sources

- [[raw/adyen/docs/capital/grant-lifecycle-and-status/2026-09-15|Adyen Capital grant lifecycle and status — collected 2026-09-15]]
