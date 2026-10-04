---
title: "Braintree Chase Change Your Bank Account"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/chase/change-your-bank-account"
raw_files:
  - "braintree/articles/chase/change-your-bank-account-2026-09-16.md"
tags: [braintree, chase, bank-account, funding, control-panel]
---

## Overview

This collected Braintree-owned Chase article describes changing the business checking account used for payouts of settled transactions. The account supplied during the original application is the existing payout destination; the article documents the change procedure as a Control Panel document upload and does not document an API route; it is not evidence that any individual transaction settled, funded or reached a bank account.

The procedure and document conditions are specific to this Chase article. They should not be transferred to the separate Adyen processor route.

## Key takeaways

- To update the business bank account information, the page directs the merchant to upload a completed Chase bank change request form in the Control Panel together with either a voided check or a bank letter for the new account.
- Screenshots of an online banking profile are not accepted. For a voided check, the account-holder name must be the business DBA or legal name; any listed address must match the business address on file; starter checks, temporary checks and screenshots of sample checks are invalid.
- A bank letter must be on bank letterhead; identify the account holder with the matching DBA or legal business name; include the account number or IBAN and the applicable routing identifier; be signed by a named bank representative with title; and have a clearly stated issue date within the prior six months.
- The submitted account must be a business checking account. The page rejects savings, deposit-only and prepaid debit accounts.

> [!warning] Processor-specific procedure and payout boundary
> This page documents the Chase bank-account-change route captured on 2026-09-16. It does not establish that the procedure applies to another processor, that a submitted change was accepted, or that any individual payout arrived.

## Detail locators

- Original-application checking account and settled-transaction payout destination: `# Change Your Bank Account`, line 16.
- Control Panel upload procedure, bank change request form, and required supporting-document alternatives: `# Change Your Bank Account`, line 18.
- Online-banking-profile screenshot rejection: `# Change Your Bank Account`, lines 21-22.
- Voided-check requirements and invalid check forms: `## Voided check`, lines 29-34.
- Bank-letter content, signature and recency requirements: `## Bank Letter`, lines 37-45.
- Business-checking requirement and rejected account types: `# Change Your Bank Account`, lines 48-49.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- Administration concept: [[braintree-control-panel]]

## Related raw API references

- [[raw/braintree/articles/chase/transactions/settlement-funding-timeline-2026-09-16|Braintree Chase settlement and funding timeline]] - unread navigation-only destination linked for payout timing; not used as factual evidence here
- [[raw/braintree/articles/guides/account-information-2026-09-16|Braintree account information guide]] - unread navigation-only destination linked for the Business Uploads Tool; not used as factual evidence here

## Raw Sources

- [[raw/braintree/articles/chase/change-your-bank-account-2026-09-16|Braintree Chase Change Your Bank Account article]] - complete collected page covering the Chase account-change upload, supporting-document conditions and rejected document or account types
