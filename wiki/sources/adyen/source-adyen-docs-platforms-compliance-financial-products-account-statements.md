---
title: "Account statements for business accounts and Issuing | Adyen for Platforms"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/compliance-financial-products/account-statements"
raw_files:
  - "adyen/docs/platforms/compliance-financial-products/account-statements/2026-09-15.md"
tags: [adyen, platforms, financial-products, business-accounts, issuing, compliance, statements]
---

## Overview

This [[adyen]] for Platforms page, last modified 2023-12-12 and captured 2026-09-15, describes Adyen's compliance-guideline requirements for user-facing account statements associated with business accounts and issued cards. It is an overview, expressly **not legal advice**. Requirements vary by product and EU, US or UK context. See [[adyen-financial-products]].

## Key takeaways

- For business accounts and Issuing, the platform prepares the user-facing statement, preserves Adyen API-provided data unchanged, supplies information the APIs do not provide (the page marks such items in bold), and submits the statement template for Adyen review and approval. The page does not prove approval of a particular template or delivery of a statement. [Raw: lines 19–27, 98, 150, 355–357]
- The Adyen Bank Accounts (EU/US) and UK Business Accounts sections use different institution/account descriptions and disclosures. Both include platform contact details, account-holder and masked account details, statement period, opening/closing balances, transaction and fee lines, and period totals. EU/US interest-bearing accounts have additional APYE/interest fields when applicable. Use the relevant jurisdiction/product table rather than treating a field list as universal. [Raw: lines 25–146, 219–303]
- The EU bank-account section includes a Depositor Information Sheet reference and a dated Dutch DGS disclosure; the US section expressly states these Adyen Business Bank Accounts are **not FDIC insured**, with only a conditional cash-sweep possibility. The UK section says an FSCS disclosure is not required for those UK Business Accounts. These are 2023-modified source statements, not current coverage or legal advice for any account. [Raw: lines 84–94, 144–146, 301–303]
- For Issuing, account/card-program type and region change the statement content. The guide asks platforms to submit a sample statement before issuing cards. It says EU Issuing need not have downloadable statements if all listed information is displayed in the UI; UK Issuing must offer a PDF or other durable download. It gives no corresponding US download rule in that passage. [Raw: lines 148–211]
- The later Issuing section qualifies the general statement language: **prepaid card programs** need not send periodic statements, but must provide on-demand access to all card transactions. If transaction information appears in the UI, the platform must capture and submit feature screenshots to Adyen for review and approval, and retain them as replacement statement records. This is distinct from the debit/credit-program rows in the earlier Issuing list. [Raw: lines 173–211, 307–313]

## Detail locators

- Scope, disclaimer, unchanged API data and template approval: raw lines 15–23 and 355–357.
- EU/US Adyen Bank Accounts requirements and disclosures: raw lines 25–94; region comparison table lines 219–303.
- UK Business Accounts requirements and FSCS note: raw lines 96–146; table lines 239–291. The institution naming differs between the UK prose (Adyen N.V.) and table (London branch); retain the source's separate wording and seek current Adyen clarification for implementation. The Business-account table also marks the Amsterdam Adyen N.V. institution row for EU, US and UK alongside separate US San Francisco and UK London branch rows (raw lines 225–245); neither this Platforms page nor the parallel Marketplace page resolves the applicable institution wording.
- Issuing program types, region/UI-download conditions and statement contents: raw lines 148–211 and 307–353.
- Prepaid periodic-statement exception, on-demand transaction access and screenshot-review/record condition: raw lines 307–313.

## Related

- [[adyen-financial-products]] — umbrella for Business accounts and Issuing
- [[adyen-platforms]] — platform/user context
- [Compliance guidelines overview](https://docs.adyen.com/platforms/compliance-financial-products) — related guide
- [User interface](https://docs.adyen.com/platforms/compliance-financial-products/user-interface) — linked UI requirements
- [Keeping records](https://docs.adyen.com/platforms/compliance-financial-products/keeping-records) — linked record requirements

## Raw Sources

- [[raw/adyen/docs/platforms/compliance-financial-products/account-statements/2026-09-15|Adyen Platforms account statements for business accounts and Issuing — collected 2026-09-15]]
