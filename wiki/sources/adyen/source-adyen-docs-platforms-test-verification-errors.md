---
title: "Test verification/KYC scenarios | Adyen Docs"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/test-verification-errors"
raw_files:
  - "adyen/docs/platforms/test-verification-errors/2026-09-15.md"
tags: [adyen, platforms, verification, kyc, testing]
---

## Overview

This 2026-09-15 Adyen for Platforms/Issuing test-environment guide shows how to force verification suberrors and exercise a remediation flow for legal entities, documents, and transfer instruments. It is a historical test procedure, not evidence of a live user's KYC outcome or current eligibility. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- When the required fields and documents are provided, verification checks pass by default in test. A Legal Entity Management API request can use one `x-requested-verification-code` suberror in a header to force a failed check. The header is test-only and cannot be used with hosted onboarding (raw lines 19–23, 35–47).
- The guide covers POST `/legalEntities`, `/documents`, and `/transferInstruments` to trigger errors; it then requires an account holder for the relevant owning legal entity and observes errors through `balancePlatform.accountHolder.updated` or a GET for the affected resource (raw lines 41–47, 1162–1177).
- To simulate remediation, use `x-requested-verification-code: 0_0001` on the corresponding PATCH resource in test. The guide conditions suberror resolution on successful error handling; it does not establish that an arbitrary live KYC decision can be overridden (raw lines 1507–1523, 1998–2000, 2290–2292).
- Requirements include an Adyen for Platforms or Issuing integration, a legal-entity-management API credential, an API web-service credential for Configuration API requests if checking errors through that API, and the account-holder-updated webhook subscription if using webhook updates (raw lines 25–33). The SDK POST/PATCH snippets omit `x-requested-verification-code` even though the prose and cURL calls include it for forced errors and `0_0001` remediation; supply the header separately in test. The snippets are incomplete examples of the requested-code flow and are language/version-specific, not a current SDK contract (raw lines 56–66, 98–537, 1509–1533, 1564–1995).

## Detail locators

- Legal-entity example `1_3004`, document `1_3008`, and transfer-instrument `1_7002`: raw lines 49–56, 540–544, 881–885.
- GET responses and webhook examples show nested verification errors, suberrors, remediating actions, and capability problems; these are examples, not a canonical join or guaranteed current status: raw lines 1175–1505. The transfer-instrument webhook sample around raw lines 1436–1503 also has malformed JSON punctuation.
- PATCH remediation endpoints and examples: raw lines 1507–1519, 1521–2529.

## Related

- [[adyen-platforms]]
- [[source-adyen-docs-platforms-kyc-verification-codes]]
- [[source-adyen-docs-platforms-verification-overview]]

## Raw Sources

- [[raw/adyen/docs/platforms/test-verification-errors/2026-09-15|Pinned Adyen test verification/KYC scenarios]]
