---
title: "Braintree APAC Change Your Bank Account"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/apac/change-your-bank-account"
raw_files:
  - "braintree/articles/apac/change-your-bank-account-2026-09-16.md"
tags: [braintree, apac, bank-account, payouts, control-panel, business-documents]
---

## Overview

This collected [[braintree]] APAC article documents the checking account supplied with the original business application and a Control Panel document-upload procedure for updating the business bank account used for settled-transaction payouts. The article prefers a voided check, with a direct-deposit form or a bank statement issued within the last three months as alternatives.

The page is a captured APAC-route snapshot, not a complete country-eligibility catalog. It gives country-specific bank-sort-code requirements only for Hong Kong, Malaysia and Singapore; it does not mention Australia or authorize transferring this procedure or its document rules to another regional or processor-specific article.

## Key takeaways

- To update the business bank account information, the page directs the merchant to upload supporting documentation through the Business Uploads Tool in the Control Panel. This is the procedure the page documents; it neither establishes that an API route is absent nor states which Control Panel role or permission is required.
- A voided check is preferred. The documented alternatives are a direct-deposit form or a bank statement issued within the last three months. Screenshots of an online-banking profile are not accepted.
- The document must state the bank name and address, its issue date, the account holder's name matching the business's legal name, the bank account number, BIC/SWIFT code and applicable bank sort code.
- The sort-code detail varies by bank domicile: Hong Kong requires the Interbank Clearing Code and Branch Code, Malaysia requires the IBG Routing Number, and Singapore requires the ACH Bank/Institution Code and Branch Code. The page does not state the corresponding requirement for Australia or any other country.
- The replacement account must be a business checking account domiciled in the same country as the business. Savings, deposit-only and prepaid debit accounts are not accepted.

> [!warning] APAC route, permission and country boundary
> Apply these statements only to this captured Braintree APAC article. The page does not enumerate all eligible APAC countries, mention Australia, or state the Control Panel permission needed for the Business Uploads Tool. Do not import role requirements or bank-document rules from sibling regional or processor pages.

> [!warning] Snapshot and outcome boundary
> This 2026-09-16 snapshot records a documented request procedure and account prerequisites. It is not proof of current country or merchant eligibility, acceptance or completion of a bank-account change, settlement of a transaction, or arrival of a payout.

## Detail locators

- Original-application checking account, settled-transaction payout destination and settlement-timeline navigation: opening paragraph, raw line 16.
- Business Uploads Tool and Control Panel procedure, preferred voided check, alternative direct-deposit form, and three-month bank-statement limit: opening section, raw line 18.
- Online-banking-profile screenshot rejection: first `NOTE`, raw lines 21-22.
- Required document fields: raw lines 26-34.
- Hong Kong, Malaysia and Singapore sort-code variations: raw line 36.
- Same-country business-checking prerequisite and rejected account types: final `NOTE`, raw lines 39-40.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- Administration context: [[braintree-control-panel]]

## Related raw documentation

- [[raw/braintree/articles/apac/transactions/settlement-funding-timeline-2026-09-16|Braintree APAC settlement and funding timeline]] - unread navigation-only destination linked for payout timing; not used as evidence for timing details here
- [[raw/braintree/articles/guides/account-information-2026-09-16|Braintree account information guide]] - unread navigation-only destination linked for the Business Uploads Tool; not used as evidence for permissions or procedure details here

## Raw Sources

- [[raw/braintree/articles/apac/change-your-bank-account-2026-09-16|Braintree APAC Change Your Bank Account article]] - complete collected snapshot covering the documented account-update upload, accepted supporting-document alternatives, required bank details, country-qualified sort codes and rejected account types
