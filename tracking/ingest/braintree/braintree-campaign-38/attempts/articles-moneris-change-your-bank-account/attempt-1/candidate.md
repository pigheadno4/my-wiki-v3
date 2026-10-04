---
title: "Braintree Moneris Change Your Bank Account"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/moneris/change-your-bank-account"
raw_files:
  - "braintree/articles/moneris/change-your-bank-account-2026-09-16.md"
tags: [braintree, moneris, bank-account, control-panel, authorized-signer, cad]
---

## Overview

This collected Braintree-hosted Moneris article documents a merchant-account bank-change route. It says settled transactions are paid to the business-associated checking account supplied during the original application, and directs a requested replacement through the Business Uploads Tool in the Braintree Control Panel for Support review and authorized-signer follow-up.

This is a 2026-09-16 documentation snapshot of a Braintree account route, not independent or current Moneris authority. It does not prove that a document was accepted, a bank-account change was completed, a transaction settled, or a deposit arrived.

## Key takeaways

- To request updated business bank-account information, the article directs the merchant to upload either an embossed voided cheque or a signed bank letter for the new account on official bank letterhead through the Control Panel's Business Uploads Tool. Screenshots of an online-banking profile are not accepted.
- An embossed voided cheque must include the account holder's DBA or legal business name; screenshots of sample cheques are invalid. A bank letter must include that account-holder name, the account number and transit number, be printed on official bank letterhead, be typed and signed by a branch officer with contact details, and state an issue date within the preceding six months. Handwritten letters are not accepted.
- The submitted account must be a Canadian-based business checking account. The page rejects savings, deposit-only and prepaid debit accounts.
- Support reviews the uploaded document and follows up with the account's authorized signer. The authorized signer is the only person the article permits to request access to or change sensitive account information, including bank-account information; this person is distinct from an Account Admin and cannot be managed in the Control Panel. The linked contact route is required to change or add signers.
- The article permits two bank accounts on one merchant account: one for fees and one for settlement funding. The merchant must provide documentation for each and identify its purpose. Fees must be debited from a CAD account; for a merchant account presenting in USD, the documented arrangement therefore requires a USD checking account for deposits and a CAD checking account for fees.

## Material warnings

> [!warning] Submission and completion boundary
> The page documents a Control Panel document-upload route followed by Support review. That route is not evidence that an API route is absent, that the documents were accepted, that the account change was approved or completed, or that any transaction settled or deposit arrived.

> [!warning] Provider, account and snapshot scope
> Apply the stated document, signer, Canadian-account and CAD/USD conditions only to the Braintree-hosted Moneris route captured on 2026-09-16. Do not transfer them to a sibling Braintree processor route or treat them as current independent Moneris policy or universal merchant eligibility.

## Detail locators

- Original-application checking account and settled-transaction payout statement: opening paragraph, raw line 16.
- Control Panel Business Uploads Tool route and accepted document alternatives: `## Documentation requirements`, raw line 21.
- Rejected online-banking screenshots: first `NOTE`, raw lines 24-25.
- Embossed voided-cheque name condition and invalid sample-cheque screenshots: `### Embossed voided cheque`, raw lines 32-36.
- Bank-letter account, transit, letterhead, branch-officer signature and six-month issue-date conditions: `### Bank letter`, raw lines 39-47.
- Support review and authorized-signer follow-up: raw line 49.
- Canadian-based business-checking requirement and excluded account types: second `NOTE`, raw lines 52-53.
- Authorized-signer authority, Account Admin distinction, signer-change route and call-in security questions: `### Authorized signer`, raw lines 58-66.
- Separate fee and settlement-funding accounts plus documentation and purpose designation: `## Multiple bank accounts`, raw lines 71-73.
- CAD fee account and USD-presentment deposit-account condition: `### Bank accounts for fees`, raw lines 76-78.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]

## Related raw API references

- [[raw/braintree/articles/moneris/transactions/settlement-funding-timeline-2026-09-16|Braintree Moneris settlement and funding timeline]] - unread navigation-only destination linked for payout timing; not used as factual evidence here
- [[raw/braintree/articles/guides/account-information-2026-09-16|Braintree account information guide]] - unread navigation-only destination linked for Business Uploads Tool details; not used as factual evidence here
- [[raw/braintree/articles/control-panel/users-roles/managing-users-roles-2026-09-16|Braintree managing users and roles guide]] - unread navigation-only destination linked for Account Admin role details; not used as factual evidence here

## Raw Sources

- [[raw/braintree/articles/moneris/change-your-bank-account-2026-09-16|Braintree Moneris Change Your Bank Account]] - complete collected snapshot for the Control Panel bank-change submission, document and authorized-signer conditions, Canadian business-checking scope, and CAD/USD account routing
