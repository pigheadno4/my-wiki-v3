---
title: "Adyen Issuing: Funds transfers"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/add-manage-funds/funds-transfers"
raw_files:
  - "adyen/docs/issuing/add-manage-funds/funds-transfers/2026-09-15.md"
tags: [adyen, issuing, balance-accounts, transfers, funding]
---

## Overview

This 2020-modified, 2026-09-15-captured Issuing guide describes funding balance accounts linked to Adyen-issued cards. It distinguishes a transfer from a verified external bank account to Adyen's bank account, followed by Adyen settlement to the linked balance account after receipt, from an internal transfer among balance accounts on the same balance platform. [[adyen]] [[adyen-issuing]]

## Key takeaways

- For external funding, create a transfer instrument for the balance account and send the bank transfer from that verified bank account to Adyen's bank account. The page directs readers to their Adyen contact for Adyen's bank details and to a separate external-bank-transfer guide for preparation and webhooks. Its settlement statement is conditional on Adyen receiving the funds; the guide does not evidence receipt of a particular transfer.
- For internal transfers, the balance accounts must belong to the same balance platform. A push credits the target balance account; a pull debits the target. To fund a user's balance account from the company-owned liable balance account, the page describes first depositing into the liable account by external bank transfer, then pushing funds from it to the user's account.
- Before an internal transfer, the guide says to contact Adyen for a Transfers API credential role and to enable transfers for the source balance account. POST `/transfers` uses an amount, initiating `balanceAccountId`, `counterparty.balanceAccountId`, and `category: internal`; the example pushes EUR 100 from the liable to the user balance account on a test host. It is an example, not proof of a completed movement.
- The sample response has `status: received` and `reason: pending`. This guide says to follow webhooks or GET `/balanceAccounts/{id}` to know whether the internal transfer completed; a refused result can have reason `notEnoughBalance`. Its linked fund-transfer webhook guide describes bank transfers (`category: bank`, `type: bankTransfer`), so do not apply that guide's sample event/status sequence to this `internalTransfer` example. The response here alone does not prove completion.

## Detail locators

- Card/balance-account relationship and two funding routes: raw lines 19–35. Same-platform push/pull definitions and liable-account funding direction: raw lines 37–46.
- Contact-led role and source enablement: raw lines 48–53. Transfer request fields, source/target IDs and test-host push example: raw lines 55–94. Language SDK samples and version labels: raw lines 96–381.
- `referenceForBeneficiary` table allows only a-z, A-Z, 0-9 at line 67, but the example value has hyphens at line 90; the guide does not reconcile this field-format conflict.
- Response ID/status/reason, possible refusal and `received`/`pending` sample: raw lines 383–425. This guide's completion instruction: raw line 428. The linked webhook guide's bank-transfer scope appears in its raw `Webhook types` table (`category: bank`, `type: bankTransfer`, lines 28–38), while this guide's example says `category: internal` and `type: internalTransfer` (lines 411–424).

## Related

- [[adyen]] — provider.
- [[adyen-issuing]] — Issuing card and balance-account context.
- [[source-adyen-docs-issuing-webhook-types-fund-transfers-webhooks]] — bank-transfer webhook guide; its event sequence is not established for the internal transfer here.

## Raw Sources

- [[raw/adyen/docs/issuing/add-manage-funds/funds-transfers/2026-09-15|Funds transfers — 2026-09-15 snapshot]]
