---
title: "Marketplace account-statement guidelines for Business accounts and Issuing"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/compliance-financial-products/account-statements"
raw_files:
  - "adyen/docs/marketplaces/compliance-financial-products/account-statements/2026-09-15.md"
tags: [adyen, marketplaces, financial-products, business-accounts, issuing, compliance, statements]
---

## Overview

This 2023-12-12-modified, 2026-09-15-captured [[adyen]] Marketplace page states Adyen's compliance-guideline requirements for user-facing account statements for Business accounts and Issuing. It expressly says it is **not legal advice**. Requirements vary by product and EU, US or UK context; this snapshot does not establish current law, a particular account's coverage, template approval or delivery. [[adyen-financial-products]]

## Key takeaways

- The platform is to present statements for Business accounts and issued cards, preserve Adyen API-provided statement data **unchanged**, add platform-provided items that the APIs do not supply, and submit its template for Adyen review and approval. The guide separately says an Issuing sample is submitted **before issuing cards**. Its later prepaid-program exception qualifies the opening's general periodic-statement wording. See raw lines 19–27, 148–152, 307–313 and 355–357.
- EU/US Adyen Bank Accounts and UK Business Accounts have different institution/account descriptions and disclosures. The lists cover platform contact information, account holder and masked account details, statement period, opening/closing balances, transaction/fee lines and period totals; interest-bearing EU/US accounts have conditional APYE/interest fields. The EU section calls for a depositor sheet and Dutch DGS disclosure; the US section states the described Business Bank Accounts are **not FDIC-insured** and describes only conditional cash-sweep coverage; the UK section says an FSCS disclosure is not required for those UK Business Accounts. These are dated source statements, not present-day coverage determinations. See raw lines 25–146 and 219–303.
- For Issuing, card-program type and region change the statement information. The page says an EU downloadable statement is not required if all listed information is in the UI, whereas a UK user must be able to download a PDF or another durable format. That passage supplies no matching US download rule. See raw lines 148–211.
- For **prepaid card programs**, the later Required data section says periodic statements need not be sent, but users must have on-demand access to all card transactions. If those transactions appear in the UI, the platform must capture and submit screenshots for Adyen review/approval and keep them as replacement statement records. This is narrower than exempting all Issuing programs or all statement information. See raw lines 307–313.
- The Business-account regional table also conflicts with the earlier region-specific institution prose: its Amsterdam `Adyen N.V.` row is marked for EU, US and UK, while separate San Francisco and London branch rows are marked for US and UK. The UK prose names `Adyen N.V.` at the London address, but the table names `Adyen N.V. London branch`. Preserve all of these source wordings; the table does not resolve current institution identity or legal wording. See raw lines 25–43, 96–105 and 225–245.

## Detail locators

- **Disclaimer, unchanged API data and template approval:** raw lines 15–23, 355–357.
- **EU/US Business Bank Account fields and disclosures:** raw lines 25–94, 219–303.
- **UK Business Account fields, FSCS note and regional institution-table conflict:** raw lines 96–146, 239–245.
- **Issuing program/region content and EU UI versus UK durable download:** raw lines 148–211.
- **Prepaid on-demand transaction access and screenshot-review records:** raw lines 307–313.

## Related

- [[adyen-financial-products]]
- [[adyen-business-accounts]]
- [[adyen-issuing]]
- [[source-adyen-docs-platforms-compliance-financial-products-account-statements|Parallel Platforms-path statement guideline]]

## Raw Sources

- [[raw/adyen/docs/marketplaces/compliance-financial-products/account-statements/2026-09-15|Adyen Marketplace account-statement guideline — collected 2026-09-15]]
