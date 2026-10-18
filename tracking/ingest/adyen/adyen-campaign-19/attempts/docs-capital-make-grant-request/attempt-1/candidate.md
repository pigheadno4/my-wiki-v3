---
title: "Adyen Capital grant request and disbursement updates"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/capital/make-grant-request"
raw_files:
  - "adyen/docs/capital/make-grant-request/2026-09-15.md"
tags: [adyen, capital, platforms, grants, disbursement, webhooks]
---

## Overview

This 2026-09-15 Adyen Capital guide describes submitting a grant request after a user selects an offer and signs the Terms of Service, then observing configuration and funds-transfer updates. A successful request prompts Adyen to initiate a transfer; the `Requested` response and the guide's sample webhooks are not proof that a particular grant was funded or that a bank received money. Renewal of an active grant is routed to a separate guide.

## Key takeaways

- Prerequisites are an Adyen for Platforms integration supporting Capital, Balance Platform Capital Configuration and Grant Initiation API roles, user `getGrantOffers` and `receiveGrants` capabilities, subscribed Capital and Transfer webhooks, operation in a supported Capital country/region, Capital compliance steps, a user-selected grant offer, and signed Terms of Service. The page states **one disbursement per grant** at this snapshot; it does not itself enumerate supported countries or establish a user's current eligibility.
- POST `/grants` uses required `grantAccountId` (obtained from Adyen) and `grantOfferId` (selected by the user). The guide describes `counterparty.balanceAccountId` for the receiving account holder's balance account; if omitted, it says the account holder's `primaryBalanceAccount` is used. It separately describes `counterparty.transferInstrumentId` for a transfer instrument belonging to that account holder's legal entity. Do not conflate a balance-account settlement with external bank receipt or infer a universal combination of optional recipient fields from the example.
- The example API response carries grant/counterparty IDs, a `Requested` status and zero balances. POST `/grants` is processed **asynchronously**: the response alone does not establish final configuration or payout; wait for actual webhook results.
- The guide maps `balancePlatform.grants.created` to grant configuration; transfer-created and transfer-updated events to received, authorised and booked transfer stages; `balancePlatform.transaction.created` to the described payout to a balance account or payment instrument; and a later `balancePlatform.grants.updated` to repayment/reconfiguration/write-off updates. Keep these event subjects and stages distinct. Its configured-grant sample still has `Requested` status and zero balances, so neither that sample nor a booked-transfer example alone proves funds reached the user.
- The webhook JSON blocks are **test illustrations**, not one coherent transaction trace. The incoming transfer examples show a positive 2025 amount, while the “Grant paid out” transaction example has a negative amount, 2023 booking/creation dates and a 2025 value date. Those differences prevent treating the snippets as an actual matched payout or a universal sign/date convention. Verify a real case with its own grant, transfer and transaction records; this page provides no bank-receipt proof.

## Detail locators

- Opening and `## Requirements`: offer/ToS order, roles, capabilities, webhooks, country gate and one-disbursement limit.
- `## 1. Configure a grant`: POST recipient and required grant/offer IDs, test request/response and asynchronous `Requested` boundary.
- `## 2. Get updates`: grant, transfer and transaction webhook event map and reception/acceptance requirement.
- Five tab examples under `## 2`: configured grant, transfer received/authorised/booked, payout transaction and repaid grant; compare their subjects, signs and dates before joining.

## Related

- [[adyen-capital]] — main Capital concept.
- [[source-adyen-docs-capital-terms-of-service]] — separately documented acceptance prerequisite.
- [[source-adyen-docs-capital-grant-lifecycle-and-status]] — grant-status reference.
- [[adyen-platforms]] — platform and balance-account context.
- [[adyen]] — provider profile.

## Raw Sources

- [[raw/adyen/docs/capital/make-grant-request/2026-09-15|Adyen Capital disburse-a-grant guide (fetched 2026-09-15)]]
