---
title: "Braintree AIB BF Change Your Bank Account"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/aib-bf/change-your-bank-account"
raw_files:
  - "braintree/articles/aib-bf/change-your-bank-account-2026-09-16.md"
tags: [braintree, aib-bf, bank-account, disbursement, control-panel]
---

## Overview

This collected [[braintree]] AIB BF article documents the business checking account associated with a merchant account, the Control Panel route for viewing limited account details, and the documented request path for changing that account by uploading a qualifying bank statement or signed bank letter. It says settled transactions are paid to the account supplied during the original application according to a separately linked settlement-and-funding timeline; that local statement is not proof that an individual transaction settled or that a deposit arrived, and the linked page is navigation rather than evidence for its details.

The page is scoped to the captured AIB BF route. It does not define the label's meaning, establish that the procedure applies to AIB AF or another account configuration, or serve as independent current bank policy. Its stated geographic condition is that a replacement account be a business checking account based in the same country as the merchant's business. The documented Control Panel flow does not establish whether an API route exists.

## Key takeaways

- In the Control Panel, the merchant can choose a merchant account and view the associated disbursement account's BIC and last four account-number digits. Access is limited to users whose role permissions include that merchant account; otherwise, an account admin must add it to the user's permissions.
- To request an update, the article directs the merchant to upload either a bank statement or a signed bank letter for the new account through the Business Uploads Tool in the Control Panel. Screenshots of an online-banking profile are not accepted.
- A bank statement must identify the legal business account holder, include the IBAN and BIC/SWIFT code, state the account currency, use only English-alphabet letters and characters, and have a clearly stated issue date within the prior three months.
- A bank letter must be on official bank letterhead; identify the legal business account holder; include the IBAN and BIC/SWIFT code; state the account currency; be signed by a bank representative; use only English-alphabet letters and characters; and have a clearly stated issue date within the prior six months.
- The submitted account must be a business checking account based in the same country as the business. Savings, deposit-only and prepaid debit accounts are not accepted.

> [!warning] AIB BF and snapshot scope
> Apply these account and document conditions only to the captured Braintree AIB BF article. Do not transfer them to AIB AF or another account configuration, treat them as independent current bank policy, or present the snapshot as proof of current eligibility, acceptance or completion of an account-change request, settlement of a transaction, or arrival of a deposit. A Control Panel procedure does not prove the presence or absence of an API route.

## Detail locators

- Original-application account and settled-transaction payout statement: opening paragraph, raw line 16.
- Control Panel viewing steps: `## Viewing your bank account`, raw lines 19-28.
- Displayed BIC and last four account digits: `## Viewing your bank account`, raw line 30.
- Merchant-account role-permission condition and account-admin route: first `NOTE`, raw lines 33-34.
- Business Uploads Tool update route: `## Updating your bank account`, raw line 41.
- Online-banking-profile screenshot rejection: second `NOTE`, raw lines 44-45.
- Bank-statement content, character-set and three-month recency requirements: `### Bank Statement`, raw lines 52-59.
- Bank-letter content, signature, character-set and six-month recency requirements: `### Bank Letter`, raw lines 62-71.
- Same-country business-checking requirement and rejected account types: final `NOTE`, raw lines 74-75.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- Administration concept: [[braintree-control-panel]]

## Related raw documentation

- [[raw/braintree/articles/aib-bf/transactions/settlement-funding-timeline-2026-09-16|Braintree AIB BF settlement and funding timeline]] - unread navigation-only destination linked for payout timing; not used as evidence for timing details here
- [[raw/braintree/articles/control-panel/users-roles/managing-users-roles-2026-09-16|Braintree managing users and roles article]] - unread navigation-only destination linked for editing merchant-account permissions; not used as evidence here
- [[raw/braintree/articles/guides/account-information-2026-09-16|Braintree account information guide]] - unread navigation-only destination linked for the Business Uploads Tool; not used as evidence here

## Raw Sources

- [[raw/braintree/articles/aib-bf/change-your-bank-account-2026-09-16|Braintree AIB BF Change Your Bank Account article]] - complete collected snapshot covering role-scoped account viewing, the documented update request, supporting-document conditions and rejected account types
