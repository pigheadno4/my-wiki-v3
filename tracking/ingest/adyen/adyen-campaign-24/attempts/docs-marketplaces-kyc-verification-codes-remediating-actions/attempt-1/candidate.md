---
title: "Adyen Marketplace-path remediating action codes"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/kyc-verification-codes/remediating-actions"
raw_files:
  - "adyen/docs/marketplaces/kyc-verification-codes/remediating-actions/2026-09-15.md"
tags: [adyen, marketplaces, platforms, issuing, verification, remediation-codes]
---

## Overview

This 2021-modified, 2026-09-15-captured Marketplace-path catalog maps Adyen verification remediating-action codes to messages. Its stated integration scope is Adyen for Platforms or Adyen Issuing, so the Marketplace URL alone does not establish a separate Classic Platforms workflow. An error can have multiple actions; when possible, Adyen sends actions on a parent `verificationErrors` item only when common to its `subErrors`, or on individual `subErrors`. See [[adyen]] and [[adyen-platforms]] for provider and current-platform context. Match an actual error payload and affected resource before using a row; the catalog is neither a universal onboarding checklist nor proof of verification, capability approval or payout.

## Key takeaways

- The lookup groups `1_1xx` general, `1_3xx` individual, `1_5xx` organization, `1_6xx` legal arrangement, `1_7xx` bank account, `1_8xx` proof of signatory, and `1_9xx` business-line actions. `2_1xx`–`2_2xx` cover missing data, `2_9xx` missing contracts, and `3_1xx` data review. These are code families, not claims that every field or document is required for every user, country or product.
- The messages identify different responses and objects: `1_100` says no remediation possible, `1_101` says contact Support, `1_700` asks to update bank account details, and `1_701` says use a different bank account. Individual, organization, legal-arrangement, signatory and business-line rows identify further data or document actions; an upload request is not a completed verification check.
- Missing-data codes may be returned when error type is `dataMissing`; the row identifies the target object. For example, `2_101` adds `individual.identificationData` to a legal entity, whereas `2_113` adds `bankAccount.iban` to a bank account. The snapshot prints `2_198` twice, once for `organization.registeredAddress.stateOrProvince` and once for `organization.principalPlaceOfBusiness.street`; the mapping is unresolved here.
- Missing-contract messages include `2_901` Sign PCI and `2_902` Accept TOS. The `3_100` message points to `/legalEntities/{id}/confirmDataReview` to indicate confirmation of data; the catalog does not say that confirming it automatically approves verification.
- The final JSON illustrates `verificationErrors`, `subErrors` and nested `remediatingActions`. Its parent error code `1_30`, suberror codes `1_3001` and `1_3000`, and action codes `1_300` and `1_301` occupy distinct fields. The example is not evidence of a live account state or a mandatory action sequence.

## Detail locators

- Purpose, parent/suberror placement and integration-scope statement: raw lines 14–23; code-family index: lines 25–38.
- General, individual, organization and legal-arrangement rows: lines 40–113; bank-account, signatory and business-line rows: lines 115–145.
- Conditional `dataMissing` rows and object-specific field names, including duplicate `2_198`: lines 147–281. Missing contracts and data review: lines 283–296. Example error-array structure and distinct code positions: lines 298–357.

## Related

- [[adyen]] — provider context.
- [[adyen-platforms]] — Adyen for Platforms and Marketplace integration context.
- [[source-adyen-docs-platforms-kyc-verification-codes-remediating-actions]] — separately pinned Platforms-path version of this code catalog.

## Related raw API references

- The raw catalog links to Adyen for Platforms, Issuing and the data-review confirmation endpoint; those linked guides own their detailed behavior until read separately.

## Raw Sources

- [[raw/adyen/docs/marketplaces/kyc-verification-codes/remediating-actions/2026-09-15|Adyen Docs: Remediating action codes (2026-09-15 snapshot; page last modified 2021-01-19)]]
