---
title: "Adyen Marketplace-path KYC suberror codes"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/kyc-verification-codes/sub-errors"
raw_files:
  - "adyen/docs/marketplaces/kyc-verification-codes/sub-errors/2026-09-15.md"
tags: [adyen, marketplaces, platforms, kyc, verification, error-codes]
---

## Overview

This Marketplace-path Adyen reference (last modified 2023-02-28; captured 2026-09-15) maps granular KYC verification suberror codes to messages and, where applicable, separate remediating-action codes. Its requirements sentence names **Adyen for Platforms or Adyen Issuing** integrations despite the Marketplace URL; it does not state a separate Classic Platforms requirement. Use a received code's exact row as a diagnostic lookup, not as proof of current onboarding eligibility, verification approval or an enabled capability. [[adyen]] [[adyen-platforms]]

## Key takeaways

- The page says no additional requirements, limitations or preparation **if** an Adyen for Platforms or Issuing integration already exists. That conditional statement does not establish that a particular platform or legal entity is onboarded, and the URL alone does not authorize applying these codes to Classic Account API notifications. See raw lines 14-20.
- The seven check families are `1_1xxx` general, `1_3xxx` individual, `1_5xxx` organization, `1_6xxx` legal arrangement, `1_7xxx` bank account, `1_8xxx` proof of signatory and `1_9xxx` business lines. Match an exact suberror row and its listed action code(s); family prefixes alone are not a complete diagnosis and action codes are distinct from suberrors. See raw lines 22-32 and the tables at 34-354.
- Some rows are consequential rather than ordinary missing-data fixes: `1_3082` says the individual fails the minimum-age requirement (raw line 130), and `1_5052` says an affiliation document proves the payout entity is not 100% affiliated and **setup cannot be continued**, even though the row links action `1_100` (raw line 194). Do not describe every suberror as automatically retryable or promise success from a listed action.
- The opening says general error codes and messages are sent in `subErrors`, but the page's example places general `1_30` in a `verificationErrors` item and specific `1_3001`/`1_3000` in its `subErrors`. This internal wording conflict and the example's ellipses/hint markup mean it is an illustration, not a complete parseable runtime contract. Check the actual response and applicable current schema. See raw lines 16 and 356-415.
- Legal-arrangement error messages can vary by arrangement type (raw line 237); document, bank, signatory and business-line rows carry different action mappings. The raw tables provide the precise cause and action for each code; do not generalize one table row's remediation to a whole check family.

## Detail locators

- **Opening, Requirements and Types of error codes**, raw lines 14-32: purpose, conditional product scope and seven family prefixes.
- **General issues**, raw lines 34-42; **Individual identity check**, raw lines 44-136: general and person/ID/address/tax/selfie/motion causes, including age row `1_3082`.
- **Organization check**, raw lines 138-233: registry, tax, ownership, affiliation, VAT and address causes; setup stop `1_5052`.
- **Legal arrangement check**, raw lines 235-289: arrangement-specific wording and constitutional-document, trustee, beneficiary and partner/UBO rows.
- **Bank account check**, raw lines 291-315; **Proof of signatory check**, raw lines 317-336; **Business lines check**, raw lines 338-354: exact code/message/action mappings.
- **Suberrors array example**, raw lines 356-415: illustrated `problems[].verificationErrors[].subErrors[]` placement and action arrays; not a complete payload.

## Related

- [[adyen-platforms]] — current Platforms integration and verification context.
- [[source-adyen-docs-platforms-kyc-verification-codes-sub-errors]] — separately pinned Platforms-path catalog; its raw governs its own version and line numbers.

## Raw Sources

- [[raw/adyen/docs/marketplaces/kyc-verification-codes/sub-errors/2026-09-15|Adyen Marketplace-path KYC suberror catalog, captured 2026-09-15]]
