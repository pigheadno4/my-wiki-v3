---
title: "Capital fund transfer-related webhooks | Adyen"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/capital/webhook-types/fund-transfers-webhooks"
raw_files:
  - "adyen/docs/capital/webhook-types/fund-transfers-webhooks/2026-09-15.md"
tags: [adyen, capital, webhooks, transfers, transactions, disbursements, repayments]
---

## Overview

This [[adyen]] Capital page, captured 2026-09-15, illustrates balance-platform **transfer** events for grant disbursement and scheduled/unscheduled repayment, then a separate **transaction.created** event for recorded fund movement. Examples focus on successfully processed cases; the page directs readers to the Transfer webhook `status` reference for other outcomes. The samples show event structure and joins, not any live grant, final debt balance or bank receipt. See [[adyen-capital]].

## Key takeaways

- Grant disbursement transfer events use `category=grants`, `type=grant`, **incoming** direction and a `reference` holding the related grant ID. The illustrated sequence is `balancePlatform.transfer.created` at `received`, then `balancePlatform.transfer.updated` at authorised/booked stages. A `received` or authorised transfer is not a booked credit; a booked transfer is a balance-platform accounting state, not proof of an external beneficiary bank deposit. [Raw: lines 34–42, 104–112, 188–196]
- Scheduled repayment transfer events use `category=grants`, `type=repayment`, **outgoing** direction and grant-ID `reference`. The guide shows received, authorised and booked stages, with example balance mutations moving from received through reserved to a negative booked balance change. The `description` prose shows grant/account/date material, but its JSON samples mask the date differently; use IDs and actual event fields rather than parsing the prose example as a guaranteed format. [Raw: lines 289–298, 359–368, 443–536]
- Unscheduled repayment has **two legs**: an incoming `capitalFundsCollection` transfer associated with Adyen's internal Capital collection account, then an outgoing `repayment` transfer that follows the scheduled repayment flow. The collection leg's `reference` is an internal Capital collection ID, not the grant ID; match the later repayment leg separately. The captured page illustrates received, authorised and booked stages for the collection leg. A booked collection leg alone is not final repayment of the grant. [Raw: lines 544–554, 615–625, 700–710]
- Once a grant disbursement or repayment transfer is recorded, the page describes a distinct `balancePlatform.transaction.created` carrying its own transaction `id`, `transferId`, grant `reference`, balance account, amount and booking/value dates. Use the transfer ID and grant ID to relate transaction and transfer events; the transaction is a booking-level record, not a grant-balance/status check or bank-receipt confirmation. [Raw: lines 802–836]
- **Sample conflicts:** the authorised-stage prose spells `authorized` while JSON status values spell `authorised`; scheduled-repayment booked prose says `transfer.updated` but its JSON envelope says `transfer.created`; the sample labelled a grant-disbursement transaction shows a **negative** amount on the balance account although the grant transfer is marked incoming, and its booking date is 2023 while its value date is 2025. Do not derive a universal status spelling, event type, disbursement sign or chronology from those conflicting examples; consult the current API schema and actual events. [Raw: lines 106–123, 359–379, 443–463, 538–540, 804–836]

## Detail locators

- Event list and successful-example limitation: raw lines 15–32.
- Grant disbursement transfer received/authorised/booked stages and IDs: raw lines 34–287.
- Scheduled repayment transfer stages, sign mutations and example-description conflict: raw lines 289–542.
- Unscheduled collection leg and its distinct reference: raw lines 544–800.
- Separate transaction event and conflicting illustrative amount/dates: raw lines 802–836.

## Related

- [[adyen-capital]] — Capital grant/repayment context
- [[adyen-reporting]] — booking and reconciliation evidence boundary
- [Webhook structures and types for Capital](https://docs.adyen.com/capital/webhook-types) — broader event reference
- [Grant lifecycle and status](https://docs.adyen.com/capital/grant-lifecycle-and-status) — grant-state meanings
- [Capital reporting and reconciliation](https://docs.adyen.com/capital/reporting-and-reconciliation) — report/ID joins

## Raw Sources

- [[raw/adyen/docs/capital/webhook-types/fund-transfers-webhooks/2026-09-15|Adyen Capital fund transfer-related webhooks — collected 2026-09-15]]
