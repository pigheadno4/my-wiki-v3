---
title: "Adyen Business Accounts: Transfer funds internally"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/transfer-funds-internally"
raw_files:
  - "adyen/docs/business-accounts/transfer-funds-internally/2026-09-15.md"
tags: [adyen, business-accounts, internal-transfers, direct-debit]
---

## Overview

This [[adyen]] Business Accounts guide describes an internal direct debit between balance accounts on the same balance platform. The initiating *source* balance account requests a debit from the *target* counterparty balance account: for example, a platform's liable account pulling a user's fee, or a debit between two users' balance accounts. This is an internal balance-account movement, not an external bank debit or payout. The 2026-09-15 capture is marked modified the same day; examples use the TEST environment.

## Key takeaways

- Before initiating, the server must receive and accept Transfer webhooks, the Customer Area subscription must be in place, and Adyen Support must enable transfers for the account that debits funds. The initiating account holder needs `sendToBalanceAccount`; the account holder receiving the debit request needs `receiveFromBalanceAccount`. Keep these named roles distinct from the later credit/debit effect.
- Initiate with `POST /transfers`. The page's request table marks `amount`, source `balanceAccountId`, target `counterparty.balanceAccountId`, and `category: internal` as required; it says to set `type: internalDirectDebit` for a counterparty debit, although its Required cell for `type` is blank. Optional references/description aid webhook matching. The page says `referenceForBeneficiary` supports only a-z, A-Z and 0-9 (raw line 47), yet its request examples use hyphens (for example, lines 71, 103 and 225). Do not infer that the sample value is accepted by the API; verify the current API reference before implementing it. See the raw table and examples for the other request fields.
- The response gives transfer `id`, `status`, and `reason`; inspect `reason` when status is not `authorised` (the page offers `refused`/`notEnoughBalance` as an example). Do not treat an authorised response as booked funds. Transfer webhooks separately cover the initiating source as an outgoing request and target as an incoming request. `balancePlatform.transfer.created` reports `received`; `balancePlatform.transfer.updated` tracks `authorised` reservation and `booked` movement, or failure. The Customer Area displays two transfer entries, one per balance account.
- The page uses collecting monthly/subscription fees without SCA or payment fees as an example of this internal debit, not as a blanket claim about other payment or bank-transfer flows. Its JSON examples illustrate TEST records; the target booked example omits a comma before `sequenceNumber`, and examples are not proof of a live booked transfer.

## Detail locators

- `Before you begin` (raw lines 21–30): webhook subscription, Support enablement and account-holder capabilities.
- `Initiate an internal direct debit` (raw lines 32–49): Transfers API fields, account roles and `type` table marking; code examples at lines 51–371.
- Response notes (raw lines 373–415): `id`, `status`, `reason` and an authorised example.
- `Get status updates` (raw lines 417–447): two account-side webhook series and the received/authorised/booked distinction; detailed TEST examples at lines 453–953.

## Related

- [[adyen-business-accounts]] — Business Accounts product and verification context.
- [[adyen-platform-internal-transfers]] — broader platform internal-funds context.

## Raw Sources

- [[raw/adyen/docs/business-accounts/transfer-funds-internally/2026-09-15|Adyen Business Accounts internal direct debits, captured 2026-09-15]]
