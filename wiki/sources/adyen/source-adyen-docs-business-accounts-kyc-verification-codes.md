---
title: "Verification codes | Adyen Business Accounts"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/kyc-verification-codes"
raw_files:
  - "adyen/docs/business-accounts/kyc-verification-codes/2026-09-15.md"
tags: [adyen, business-accounts, verification, kyc, platforms]
---

## Overview

This 2021-modified, 2026-09-15-captured Adyen verification-code overview explains how to locate and interpret verification errors for an account holder's capabilities. It names Adyen for Platforms or Adyen Issuing integration scope despite its Business Accounts URL. It distinguishes broad general error codes, more specific linked suberror codes, and possible remediating action codes; an action is sent for an error whenever possible, not guaranteed. [[adyen]] [[adyen-business-accounts]]

## Key takeaways

- Inspect the account holder's capabilities in Customer Area, a Configuration API `GET /accountHolders/{id}` response, or `balancePlatform.accountHolder.created` / `updated` webhooks. The codes are in the capability `problems` array. API viewing requires an API web service user credential; Customer Area viewing requires the **Manage account holder capabilities** role. See raw lines 27–61.
- A problem identifies the legal entity with the verification error. Each `verificationErrors` item can carry a type (`invalidInput` or `dataMissing`), general code/message, common `remediatingActions`, and `subErrors` with their own type, code, message and action array. The page's JSON is an illustrative problem, not a complete code catalog or evidence of a successful remediation. See raw lines 69–144.
- For API-only onboarding, Adyen recommends designing handling for the codes relevant to the use case while supporting possible verification codes. Use the linked child catalogs for actual general, suberror and action meanings. A code or suggested action does not itself establish verified capability, account opening, automatic retry, or a completed financial operation. See raw lines 63–67 and 146–160.

## Detail locators

- Code hierarchy and non-guaranteed action availability: raw lines 19–25.
- Prerequisites and channels: raw lines 27–61.
- `problems` object shape and example values: raw lines 69–144.
- Child code catalogs: raw lines 146–160.

## Related

- [[source-adyen-docs-business-accounts-kyc-verification-codes-general-verification-errors]] — general-code catalog.
- [[source-adyen-docs-business-accounts-kyc-verification-codes-sub-errors]] — specific suberror catalog.
- [[source-adyen-docs-business-accounts-kyc-verification-codes-remediating-actions]] — remediating-action catalog.
- [[adyen-business-accounts]] — Business Accounts product and verification context.

## Raw Sources

- [[raw/adyen/docs/business-accounts/kyc-verification-codes/2026-09-15|Verification codes raw capture]]
