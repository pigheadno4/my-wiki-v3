---
title: "Braintree AU Change Your Bank Account"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/au/change-your-bank-account"
raw_files:
  - "braintree/articles/au/change-your-bank-account-2026-09-16.md"
tags: [braintree, au, control-panel, bank-account, disbursements, business-uploads]
---

## Overview

This collected AU-routed Braintree article explains how to view the disbursement bank account associated with a selected merchant account and how to submit supporting documents for a new business bank account through the Control Panel. In this snapshot, the article says settled transactions are paid out to the business checking account supplied during the original application, according to a separate settlement-and-funding timeline.

## Key takeaways

- The Control Panel's Disbursement Bank Account page shows the routing number and last four account-number digits for the selected merchant account. Access is limited to merchant accounts included in the user's role permissions; the article routes missing access to an account-admin user edit.
- To request an update, the article directs the merchant to upload either a bank statement or a signed bank letter for the new account through the Business Uploads Tool in the Control Panel. This is a document-submission route, not evidence that Braintree accepted the documents or completed the bank-account change.
- Both document types must identify the business account holder, BSB and account number, and business address. A bank statement must have been issued within the last three months; a bank letter must be on bank letterhead, signed by a bank representative, and issued within the last six months.
- Screenshots of an online-banking profile are not accepted. The submitted account must be a business checking account; savings, deposit-only and prepaid debit accounts are not accepted.

## Material warnings

> [!warning] Submission and interface boundary
> The page documents a Control Panel upload path. It does not establish an API update operation, document acceptance, processing time, approval, or completion of the bank-account change.

> [!warning] Regional, account and currency scope
> This is a 2026-09-16 capture of an AU-routed article. It does not prove current Australian policy or eligibility, does not transfer to another region or merchant account, and names no settlement currency or per-currency bank-account mapping.

## Detail locators

- Original-application checking account and settled-transaction payout statement: opening paragraph, line 16.
- Control Panel viewing path, displayed routing/account details and merchant-account permission condition: `## Viewing your bank account`, lines 19-34.
- Business Uploads Tool route and rejected online-banking screenshots: `## Updating your bank account`, lines 39-49.
- Bank-statement contents and three-month issue-date requirement: `### Bank statement`, lines 52-58.
- Bank-letter contents, representative signature and six-month issue-date requirement: `### Bank letter`, lines 61-69.
- Required business-checking account type and excluded account types: note at lines 72-73.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]
- General account-information and Business Uploads route: [[source-braintree-articles-guides-account-information]]

## Raw Sources

- [[raw/braintree/articles/au/change-your-bank-account-2026-09-16|Braintree AU Change Your Bank Account]] - complete collected AU-routed article for viewing a selected merchant account's disbursement bank details and submitting bank-change documents
