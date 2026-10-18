---
title: "Adyen account statements for Business Accounts and Issuing"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/compliance-guidelines/account-statements"
raw_files:
  - "adyen/docs/business-accounts/compliance-guidelines/account-statements/2026-09-15.md"
tags: [adyen, business-accounts, issuing, statements, compliance]
---

## Overview

This 2023-12-12-modified, 2026-09-15-captured [[adyen]] compliance-guidelines page describes user-facing account statement templates for EU/US Adyen Bank Accounts, UK Business Accounts, and Adyen Issuing. It explicitly says the material is not legal advice. It instructs platforms offering business accounts or issuing cards to give users statements, keep Adyen API data unchanged, and submit statement templates for Adyen review and approval. The required content varies by product and jurisdiction; the page does not attest to any specific user's opened account, transactions, or statement delivery.

## Key takeaways

- The page separates `Adyen Bank Accounts (EU & US)`, `Adyen Business Accounts (UK)`, and `Adyen Issuing`. Each section gives institution/issuer and platform information, account holder and account details, statement period and beginning/end balances, transaction entries, and debit/credit totals. Bold items, including platform contact details, are to be supplied by the platform rather than Adyen APIs. See each section and the country table for exact fields and conditional items.
- EU/US bank-account statements include EU IBAN/BIC and deposit-information/disclosure items or US FDIC disclosure wording as applicable; the page limits APYE/interest details to interest-bearing accounts. UK Business Accounts are described as e-money accounts and the page says Financial Services Compensation Scheme disclosure is not required there because it is confirmed during onboarding. Treat these as dated Adyen guideline statements, not an independent assessment of legal protection or current product eligibility.
- For Issuing, platforms must submit a sample statement to Adyen before issuing cards. The page distinguishes prepaid, debit, and credit account-type examples by region and program. It says a downloadable statement is unnecessary for EU Issuing if all listed information appears in the UI; UK Issuing must offer a PDF or other durable downloadable format. These are Issuing-specific qualifications, not a general exemption for Business Accounts.
- `Required data` (business accounts) repeats EU/US/UK country columns and the unchanged-API-data rule; `Review by Adyen` requires template submission for approval. The UK prose calls the PSP `Adyen N.V.` while the country table names `Adyen N.V. London branch`; the table's first Adyen N.V. institution row is marked for EU, US and UK despite separate US/UK branch rows. Resolve exact legal-entity/branch wording with Adyen before using a template; do not silently merge the conflicting rows.

## Detail locators

- Opening scope/disclaimer (raw lines 15–23): statements, unchanged API data, Adyen approval, product/region variation and non-legal-advice boundary.
- `Adyen Bank Accounts (EU & US)` (raw lines 25–94): bank details, platform-supplied items, balances, activity, interest-bearing conditional items, EU/US disclosures.
- `Adyen Business Accounts (UK)` (raw lines 96–146): PSP, e-money account details, activity and UK disclosure qualification.
- `Adyen Issuing` (raw lines 148–211): sample pre-issuance review, program/region account-type rows and EU UI versus UK download rule.
- `Required data` and `Review by Adyen` (raw lines 213–301): EU/US/UK comparison table, API-data integrity and final template review.

## Related

- [[adyen-business-accounts]] — Business Accounts product context.
- [[adyen-issuing]] — Issuing context for the separate card-program statement section.

## Raw Sources

- [[raw/adyen/docs/business-accounts/compliance-guidelines/account-statements/2026-09-15|Adyen account statements compliance guidelines, captured 2026-09-15]]
