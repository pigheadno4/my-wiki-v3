---
title: "Braintree NAB Change Your Bank Account"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/nab/change-your-bank-account"
raw_files:
  - "braintree/articles/nab/change-your-bank-account-2026-09-16.md"
tags: [braintree, nab, control-panel, bank-account, business-uploads, australia]
---

## Overview

This collected Braintree-hosted NAB-path article documents a request route for replacing the business checking account supplied during the original application. It directs the merchant to submit specified evidence for the new account through the Control Panel's Business Uploads Tool and states that settled transactions are paid to the original account according to a separately linked settlement-and-funding timeline.

## Key takeaways

- To request updated business bank-account information, the article directs the merchant to upload either a bank statement or a signed bank letter for the new account through the Business Uploads Tool in the Control Panel.
- A bank statement must include the account holder's DBA or legal business name, BSB and account number, and business address, and must show a clearly stated issue date within the preceding three months.
- A bank letter must be printed on bank letterhead, include the same account-holder, BSB/account-number and business-address information, be signed by a bank representative, and show a clearly stated issue date within the preceding six months.
- Screenshots of an online-banking profile are not accepted. The submitted account must be an Australia-based business checking account; savings, deposit-only and prepaid debit accounts are not accepted.

> [!warning] Request and completion boundary
> The page documents a Control Panel document-upload request. Uploading the evidence does not establish that the documents were accepted, the request was approved, or the bank-account change was completed.

> [!warning] Snapshot and route scope
> Apply these document and account conditions only to this Braintree-hosted NAB-path snapshot captured on 2026-09-16. The explicit Australia-based account condition does not establish current policy or eligibility, transfer to a sibling account or processor route, or imply a settlement currency.

## Detail locators

- Original-application checking account and settled-transaction payout statement: opening paragraph, raw line 16.
- Business Uploads Tool request route and accepted document alternatives: raw line 18.
- Rejected online-banking screenshots: first `NOTE`, raw lines 21-22.
- Bank-statement contents and three-month issue-date requirement: `### Bank Statement`, raw lines 29-35.
- Bank-letter contents, bank-representative signature and six-month issue-date requirement: `### Bank letter`, raw lines 38-46.
- Australia-based business-checking requirement and excluded account types: second `NOTE`, raw lines 49-50.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]

## Related raw API references

- [[raw/braintree/articles/nab/transactions/settlement-funding-timeline-2026-09-16|Braintree NAB settlement and funding timeline]] - unread navigation-only destination linked for payout timing; not used as factual evidence for this source
- [[raw/braintree/articles/guides/account-information-2026-09-16|Braintree account information guide]] - unread navigation-only destination linked for Business Uploads Tool details; not used as factual evidence for this source

## Raw Sources

- [[raw/braintree/articles/nab/change-your-bank-account-2026-09-16|Braintree NAB Change Your Bank Account]] - complete collected snapshot for the Control Panel bank-change request, document conditions and Australia-based business-checking-account requirement
