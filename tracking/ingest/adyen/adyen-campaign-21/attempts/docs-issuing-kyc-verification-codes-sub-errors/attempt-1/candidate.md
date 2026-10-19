---
title: "Adyen Issuing KYC suberror codes"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/kyc-verification-codes/sub-errors"
raw_files:
  - "adyen/docs/issuing/kyc-verification-codes/sub-errors/2026-09-15.md"
tags: [adyen, issuing, kyc, verification, error-codes]
---

## Overview

This Adyen Issuing-path suberror reference (last modified 2021-01-19; fetched 2026-09-15) maps granular KYC verification causes to messages and, when applicable, separate remediating-action codes. Its stated requirement scope is an existing Adyen for Platforms or Adyen Issuing integration. Use an observed suberror's exact row to investigate a reported verification issue; the catalog does not establish current eligibility, an account or card state, a successful fix, or payment outcome. See [[adyen]] and [[adyen-issuing]].

## Key takeaways

- The opening calls suberrors granular, but says general codes and messages are in `subErrors`; its own example instead places a general `1_30` error in `verificationErrors` and granular `1_3001` and `1_3000` entries in `subErrors`. Treat that wording conflict as unresolved by this page and check the actual response/current schema before parsing. The example has ellipses and hint markup, so it is illustrative rather than a complete JSON payload. See raw lines 14-16 and 330-389.
- The short family list names `1_1xxx` general, `1_3xxx` individual, `1_5xxx` organization and `1_7xxx` bank account; the tables also contain legal arrangement `1_6xxx`, proof of signatory `1_8xxx` and business lines `1_9xxx`. These are categories, not a diagnosis. Table rows can point to multiple action codes; a suberror code and an action code serve different purposes. See raw lines 22-29 and the check tables at lines 31-328.
- The no-additional-preparation statement is conditional on already having a Platforms or Issuing integration. It does not establish onboarding, verification approval or an enabled capability for a particular entity. See raw lines 18-20.
- Some rows mark hard limits rather than routine document correction: individual `1_3082` says the person does not meet the minimum age requirement (raw line 124); organization `1_5052` says a payout entity is not 100% affiliated and setup cannot be continued, despite a linked action `1_100` (raw line 188). Neither should be generalized into an automatic retry or a promise of approval.

## Detail locators

- **General issues**, raw lines 31-39: declined legal entity, technical issues, questions, sensitive data and missing information, each with its row's action link.
- **Individual identity check**, raw lines 41-130: names, ID/tax data, documents, address, selfies and motion capture; minimum-age row `1_3082` at line 124.
- **Organization check**, raw lines 132-227: registry and tax data, ownership, affiliation, VAT and address evidence; stop condition `1_5052` at line 188.
- **Legal arrangement check**, raw lines 229-263: arrangement-specific message wording and constitutional-document/registration rows.
- **Bank account check**, raw lines 265-289: bank details and document mismatch or quality; `1_7007` concerns an unentered verification code at line 274.
- **Proof of signatory check** and **Business lines check**, raw lines 291-328: signatory/director evidence, website/industry and proof-of-funds rows.
- **Suberrors array example**, raw lines 330-389: parent verification error, nested suberrors and action-code placements; example only.

## Related

- [[adyen-issuing]] — Issuing product and evidence boundary.
- [[source-adyen-docs-business-accounts-kyc-verification-codes-sub-errors]] — separately captured Business Accounts-path variant; use its own raw for its claims.
- [[source-adyen-docs-platforms-kyc-verification-codes-sub-errors]] — separately captured Platforms-path variant; use its own raw for its claims.

## Raw Sources

- [[raw/adyen/docs/issuing/kyc-verification-codes/sub-errors/2026-09-15|Adyen Issuing KYC suberror reference, fetched 2026-09-15]]
