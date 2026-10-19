---
title: "Adyen Issuing: Remediating action codes"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/kyc-verification-codes/remediating-actions"
raw_files:
  - "adyen/docs/issuing/kyc-verification-codes/remediating-actions/2026-09-15.md"
tags: [adyen, issuing, kyc, verification, remediation]
---

## Overview

This Adyen Issuing-path reference (last modified 2021-01-19; captured 2026-09-15) maps **remediating action codes** to messages for verification problems. An action code gives an instruction associated with a received error; it is distinct from the verification error and suberror code, and the table alone neither proves a specific user's status nor completion or success of a remediation. See [[adyen]] and [[adyen-issuing]].

## Key takeaways

- Adyen may include multiple actions for one error. `verificationErrors[].remediatingActions` is sent only when the action is common to the `subErrors`; individual `subErrors[].remediatingActions` can carry their own actions. The example separates outer error `1_30`, suberrors `1_3001` and `1_3000`, and action codes `1_300` and `1_301`. Use the received error/suberror, action message, and affected entity together; do not treat a catalog action as an automatic retry instruction.
- For an existing Adyen for Platforms **or Adyen Issuing** integration, the page states no additional requirements, limitations, or preparations for these codes. This statement does not establish onboarding completion, capability approval, current eligibility, document sufficiency, or legal compliance.
- The tables cover general, individual, organization, legal-arrangement, bank-account, business-line, missing-data, missing-contract and data-review actions. General actions include `1_100` **No remediation possible** and `1_101` **Contact Support**. `2_901` says **Sign PCI**, `2_902` says **Accept TOS**, and `3_100` points to `/legalEntities/{id}/confirmDataReview` to indicate that data is confirmed. These are conditional catalog messages, not proof that a given integration must take every action or that Adyen accepted an action.
- Missing-data codes **may** be returned for error type `dataMissing` and point to fields or documents on a legal entity, bank account, business line, or document. They are not a universal required-field schema. The table includes country-specific examples such as a nine-digit SSN action; apply only the received code in its verification context.
- **Catalog ambiguity:** the captured missing-data table assigns `2_198` to both `organization.registeredAddress.stateOrProvince` and `organization.principalPlaceOfBusiness.street`. Do not infer a unique field from that code alone; inspect the returned action message and current provider reference or seek clarification. The introductory range list also omits the separately tabulated legal-arrangement and business-line families.

## Detail locators

- Action placement, shared versus suberror scope, and Issuing/Platforms integration statement: pinned raw lines 16–23; illustrative nested response: lines 278–337.
- Code-family navigation and general/individual/organization action tables: pinned raw lines 25–94.
- Legal-arrangement, bank-account and business-line tables: pinned raw lines 95–126.
- Conditional missing-data table, including duplicate `2_198`: pinned raw lines 127–262.
- Missing-contract and data-review action messages: pinned raw lines 263–277.

## Related

- [[source-adyen-docs-issuing-kyc-verification-codes-sub-errors]] — linked suberror catalog for more specific verification causes and associated actions.
- [[source-adyen-docs-issuing-manage-account-holders]] — account-holder capability and KYC views; a status view does not establish that a listed action succeeded.

## Raw Sources

- [[raw/adyen/docs/issuing/kyc-verification-codes/remediating-actions/2026-09-15|Adyen Issuing remediating action codes, captured 2026-09-15]]
