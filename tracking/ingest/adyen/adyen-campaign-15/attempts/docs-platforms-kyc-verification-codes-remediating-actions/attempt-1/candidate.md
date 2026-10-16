---
title: "Adyen Platforms remediating action codes"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/kyc-verification-codes/remediating-actions"
raw_files:
  - "adyen/docs/platforms/kyc-verification-codes/remediating-actions/2026-09-15.md"
tags: [adyen, platforms, issuing, verification, remediation-codes]
---

## Overview

This Adyen code catalog maps remediating action codes to messages for verification errors in Adyen for Platforms or Adyen Issuing integrations. An error may have multiple actions. Adyen sends them, when possible, on a parent `verificationErrors` item only when common to its `subErrors`, or on individual `subErrors`. The action is guidance for the reported error, not a universal onboarding requirement, proof that submitted data is valid, or a guarantee that verification or a financial capability will be approved. See [[adyen]] and [[adyen-platforms]] for provider and platform context. The page was last modified in 2021 and captured in 2026; use the actual error payload and current applicable verification route for an account-specific decision.

## Key takeaways

- Match the received code and message to its error level and affected resource before acting. The catalog groups `1_1xx` general, `1_3xx` individual, `1_5xx` organization, `1_6xx` legal arrangement, `1_7xx` bank account, `1_8xx` proof of signatory, and `1_9xx` business-line checks. `2_1xx`–`2_2xx` list missing data, `2_9xx` missing contracts, and `3_1xx` data review. These headings and rows are lookup locations, not a statement that every listed field is required for every entity, country or product.
- Actions have distinct objects and effects: `1_100` says no remediation possible; `1_101` says contact Support; individual/organization rows request data updates or specific documents; bank-account rows can request bank details, a different account or bank documents; business-line rows address industry/web information. Do not translate a bank-account action into a legal-entity field update or treat a listed upload as a completed check.
- Missing-data rows are described as possible when error type is `dataMissing` and name the target object, for example `2_101` adds `individual.identificationData` to a legal entity while `2_113` adds `bankAccount.iban` to a bank account. The `2_198` code is printed twice with different organization address fields at raw lines 248–249; do not resolve that conflict from this snapshot alone.
- Missing-contract rows include `2_901` Sign PCI and `2_902` Accept TOS; these are remediation messages, not evidence the merchant has signed or accepted. `3_100` points to `/legalEntities/{id}/confirmDataReview` to indicate data confirmation; invoking that endpoint is not represented here as automatic verification approval.
- The final JSON is an illustrative error payload with `verificationErrors`, `subErrors` and action arrays. Its `1_30` parent verification code and `1_3001`/`1_3000` suberror codes are different from the nested `1_300`/`1_301` remediation codes. The example does not establish a live account state or a universal sequence of actions.

## Detail locators

- Purpose, multiple actions and parent-versus-suberror placement: raw lines 15–19. Historical Platforms/Issuing scope statement and code-family index: `## Requirements` and `## Types of error codes`, lines 21–38.
- General, individual, organization and legal-arrangement messages: lines 40–113. Bank, signatory and business-line messages: lines 115–145.
- Conditional `dataMissing` table and object-specific fields, including duplicated `2_198`: `## Missing data`, lines 147–281. Contract and data-review messages: lines 283–296. Error-array example and distinct parent/suberror/remediation code positions: lines 298–357.

## Related

- [[adyen]] — provider context.
- [[adyen-platforms]] — Platforms onboarding and verification route.
- [[source-adyen-docs-platforms-manage-legal-entities]] — distinct legal-entity create/view/update operations and verification-rerun conditions.

## Related raw API references

- The raw catalog links to Adyen for Platforms, Issuing and the data-review confirmation endpoint; those linked guides own current permissions, status semantics and verification criteria until read separately.

## Raw Sources

- [[raw/adyen/docs/platforms/kyc-verification-codes/remediating-actions/2026-09-15|Adyen Docs: Remediating action codes (2026-09-15 snapshot; page last modified 2021-01-19)]]
