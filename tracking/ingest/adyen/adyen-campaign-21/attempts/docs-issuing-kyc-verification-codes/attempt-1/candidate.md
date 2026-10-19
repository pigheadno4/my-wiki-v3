---
title: "Adyen Issuing: Verification code structure and retrieval"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/kyc-verification-codes"
raw_files:
  - "adyen/docs/issuing/kyc-verification-codes/2026-09-15.md"
tags: [adyen, issuing, kyc, verification, error-codes]
---

## Overview

This Adyen Issuing/Platforms guide (last modified 2024-06-04; captured 2026-09-15) explains where verification codes appear and how general error codes, granular suberrors and suggested remediating-action codes relate. Codes convey failed-check causes and possible user actions; a remediating action is sent whenever possible, not guaranteed for every error. This is an error-handling and navigation guide, not a full code catalogue or proof that a capability is allowed. [[adyen]] [[adyen-issuing]]

## Key takeaways

- The guide applies to an Adyen for Platforms or Adyen Issuing integration. API viewing requires a Configuration API web-service user credential; Customer Area viewing requires the **Manage account holder capabilities** role (raw lines 27-35).
- In Customer Area, find the account holder and inspect its **Capabilities** tab for enabled, allowed and verification status. Through API/webhooks, GET `/accountHolders/{id}` or follow `balancePlatform.accountHolder.created` and `.updated`; verification codes appear in a capability's `problems` array (raw lines 37-61).
- A `problems` entry identifies the affected legal entity and has `verificationErrors`; an error can contain `type` (`invalidInput` or `dataMissing`), general `code` and `message`, optional common `remediatingActions`, and `subErrors` with their own type/code/message/actions (raw lines 69-81). The sample shows an invalid verification status with one general `1_30` error and granular `1_3001`/`1_3000` suberrors; the `...` markers mean it is illustrative, not parse-ready JSON (raw lines 83-144).
- For API-only onboarding, Adyen recommends choosing error-handling flows appropriate to the use case and development resources while building the implementation to handle all possible verification codes (raw lines 63-67). Use suberror codes to construct specific flows or to test scenarios; do not assume every error has one definitive action (raw lines 19-25).

## Detail locators

- Separate code lists: [[source-adyen-docs-issuing-kyc-verification-codes-general-verification-errors]] for broad causes, [[source-adyen-docs-issuing-kyc-verification-codes-sub-errors]] for specific causes, and [[source-adyen-docs-issuing-kyc-verification-codes-remediating-actions]] for possible solutions. These are linked in the guide's Next steps at raw lines 146-164.
- Test failure and remediation flow: [[source-adyen-docs-issuing-test-verification-errors]], linked at raw lines 25 and 150-152. The present page alone does not authorize a live verification result.

## Related

- [[adyen]] — provider.
- [[adyen-issuing]] — Issuing concept.
- [[source-adyen-docs-issuing-kyc-verification-codes-general-verification-errors]] — general code list.
- [[source-adyen-docs-issuing-kyc-verification-codes-sub-errors]] — granular code list.
- [[source-adyen-docs-issuing-kyc-verification-codes-remediating-actions]] — action code list.
- [[source-adyen-docs-issuing-test-verification-errors]] — test-only scenario flow.

## Raw Sources

- [[raw/adyen/docs/issuing/kyc-verification-codes/2026-09-15|2026-09-15 capture of Adyen verification codes guide]]
