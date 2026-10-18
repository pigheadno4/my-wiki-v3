---
title: "Remediating action codes | Adyen Business accounts"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/kyc-verification-codes/remediating-actions"
raw_files:
  - "adyen/docs/business-accounts/kyc-verification-codes/remediating-actions/2026-09-15.md"
tags: [adyen, business-accounts, verification, kyc, remediation]
---

## Overview

This 2021-modified, 2026-09-15-captured [[adyen]] Business accounts reference maps **remediating action codes** to suggested responses for verification problems. Adyen may send actions within a `verificationErrors` item when shared across its suberrors, and within individual `subErrors`; one error can have multiple actions. See [[adyen-business-accounts]] for the product route. An action code is not the verification error or suberror code, does not itself prove a failed or passed check for a user, and does not authorize an automatic retry or guarantee approval.

## Key takeaways

- The guide says remediating actions instruct how to resolve an error, possibly with multiple actions. Outer `verificationErrors[].remediatingActions` appears only when actions are common to its `subErrors`; suberrors may also carry their own actions. In the example, outer error `1_30`, suberrors `1_3001`/`1_3000`, and action codes `1_300`/`1_301` are different namespaces and object positions. Match the received action to its error/suberror, entity and message before deciding what information or document to provide. [Raw: lines 14–19, 298–357]
- For an existing Adyen for Platforms **or Adyen Issuing** integration, the page states no additional requirements, limitations or preparations for these remediation codes. That statement is scoped to using this reference and does not remove onboarding, verification, capability, document, consent or Business accounts eligibility requirements from other guides. [Raw: lines 21–23]
- The catalog groups action codes by issue: general `1_1xx`; individual `1_3xx`; organization `1_5xx`; legal arrangement `1_6xx`; bank account `1_7xx`; signatory `1_8xx`; business line `1_9xx`; missing data `2_1xx–2_2xx`; missing contracts `2_9xx`; and data review `3_1xx`. Examples include `1_100` “No remediation possible,” `1_101` contact Support, `2_902` accept TOS, and `3_100` a data-review confirmation endpoint. These are catalog messages, not proof any action was performed or accepted. [Raw: lines 25–46, 283–296]
- The missing-data section says its codes **may** be returned for error type `dataMissing` and names the target resource/field: legal entity individual/organization/tax/association fields, bank-account fields, business-line fields, documents and source-of-funds data. This is conditional, not a global required-field list; the exact code, affected entity and country/product verification context govern an actual remediation. [Raw: lines 147–281]
- **Catalog conflict:** code `2_198` is listed twice, once for `organization.registeredAddress.stateOrProvince` and once for `organization.principalPlaceOfBusiness.street`. Do not use this captured table alone to map `2_198` to one field; inspect the actual returned action message/current API reference or obtain provider clarification. Other listed actions, including a Japan-script formatting message and a US SSN example, are conditional code text, not universal requirements. [Raw: lines 62–68, 247–250]

## Detail locators

- Action location and shared-versus-suberror scope: raw lines 14–19; example object path and codes: raw lines 298–357.
- Integration prerequisite statement and code-family navigation: raw lines 21–39.
- General, individual, organization, legal arrangement, bank, signatory and business-line action tables: raw lines 40–145.
- Conditional missing-data table and duplicate `2_198`: raw lines 147–281.
- Missing-contract and data-review action tables: raw lines 283–296.

## Related

- [[adyen-business-accounts]] — Business accounts product and verification context
- [Business accounts verification overview](https://docs.adyen.com/business-accounts/verification-overview) — linked verification lifecycle
- [Legal Entity Management API](https://docs.adyen.com/api-explorer/legalentity/latest/overview) — linked API family

## Raw Sources

- [[raw/adyen/docs/business-accounts/kyc-verification-codes/remediating-actions/2026-09-15|Adyen Business accounts remediating actions — collected 2026-09-15]]
