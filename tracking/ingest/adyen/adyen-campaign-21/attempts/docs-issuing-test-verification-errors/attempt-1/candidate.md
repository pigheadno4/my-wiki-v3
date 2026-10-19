---
title: "Adyen Issuing: Test verification/KYC scenarios"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/test-verification-errors"
raw_files:
  - "adyen/docs/issuing/test-verification-errors/2026-09-15.md"
tags: [adyen, issuing, verification, kyc, testing]
---

## Overview

This 2026-09-15 Adyen guide describes test-environment error handling for verification of legal entities, documents, and transfer instruments in an Adyen for Platforms or Adyen Issuing integration. With required fields and documents, test checks pass by default; the requested-code header forces a failed check so the integrator can inspect the verification error and test remediation. It does not establish live KYC results or eligibility.

## Key takeaways

- Requirements: an Adyen for Platforms or Issuing integration and a Legal Entity Management API credential; the guide also calls for a Configuration API web-service credential to check errors through API requests and subscription to `balancePlatform.accountHolder.updated` to receive failed-verification updates (raw lines 25-33).
- In the **test environment only**, send one suberror code per `x-requested-verification-code` header on Legal Entity Management API `POST /legalEntities`, `POST /documents`, or `POST /transferInstruments`. Requested verification codes cannot be used with hosted onboarding (raw lines 35-47). The guide illustrates `1_3004` for individual details/residency, `1_3008` for an incomplete ID image, and `1_7002` for an invalid bank-account number; these are examples, not an exhaustive code list (raw lines 49-56, 540-544, 881-885).
- Create an account holder for the organization's, individual's, or sole proprietor's legal entity when testing legal-entity errors, or for the legal entity that owns the document or transfer instrument when testing those resources (raw lines 1162-1166). Then inspect `balancePlatform.accountHolder.updated` or GET the particular legal entity, document, or transfer instrument; the examples show verification errors, suberrors and remediating actions (raw lines 1168-1505).
- To **simulate** successful remediation in test, send `x-requested-verification-code: 0_0001` on the corresponding `PATCH /legalEntities/{id}`, `/documents/{id}`, or `/transferInstruments/{id}`. The guide says it resolves associated suberrors **if the error-handling flow succeeds**; this is a test-flow instruction, not proof of live verification or any card/payment capability (raw lines 1507-1523, 1998-2000, 2290-2292).

## Detail locators

- Complete curl and language-specific request examples: raw lines 58-1160 for forced failures and 1521-2529 for simulated remediation. The guide's prose and curl examples supply `x-requested-verification-code`, while several SDK examples omit that header in their shown call; follow the documented header requirement rather than assuming those SDK snippets themselves force the scenario.
- Example GET responses and account-holder webhook payloads: raw lines 1175-1505. A sample can show `enabled: true` alongside `allowed: false` and invalid verification status; these are example values, not evidence that a capability is usable. The transfer-instrument webhook example also has JSON punctuation omissions (raw lines 1436-1503), so do not use it as a parse-ready fixture without correction.
- Verification suberror catalogue: the guide's `See also` link at raw line 2533.

## Related

- [[adyen]] — provider.
- [[adyen-issuing]] — Issuing concept and source route.

## Raw Sources

- [[raw/adyen/docs/issuing/test-verification-errors/2026-09-15|2026-09-15 Adyen test verification/KYC scenarios]]
