---
title: "Adyen verification suberror codes"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/kyc-verification-codes/sub-errors"
raw_files:
  - "adyen/docs/business-accounts/kyc-verification-codes/sub-errors/2026-09-15.md"
tags: [adyen, business-accounts, platforms, issuing, kyc, verification]
---

## Overview

This Adyen verification suberror reference was last modified 2023-02-28 and captured 2026-09-15. It maps granular suberror codes to messages and, when applicable, separate remediating-action codes for verification problems. Despite its Business Accounts URL, the stated requirement scope covers existing Adyen for Platforms **or Adyen Issuing** integrations. A code explains a reported verification problem; it does not itself prove Business Account approval, current eligibility, a completed fix, or the result of a later verification check.

## Key takeaways

- The page groups suberrors by check: `1_1xxx` general, `1_3xxx` individual identity, `1_5xxx` organization, `1_6xxx` legal arrangement, `1_7xxx` bank account, `1_8xxx` proof of signatory, and `1_9xxx` business lines. Use the exact observed suberror and its table row, rather than treating a family prefix as a diagnosis. Table links give **remediating-action codes**, which are a separate code namespace and may contain more than one action for one suberror.
- The requirement statement says no additional requirements, limitations or preparations **if** the reader already has an Adyen for Platforms or Issuing integration. It does not waive product onboarding, entity verification, Business Account eligibility, permissions or compliance obligations in other guides.
- The tables distinguish data mismatch from missing/expired/unsupported/low-quality evidence across individuals, organizations, legal arrangements, bank documents, signatories and business lines. For example, individual identity rows include ID and residence/tax-ID issues; bank rows distinguish invalid routing/account data from document mismatch/age; business-line rows include industry/site and proof-of-funds issues. The specific code and matching action link control the next investigation; do not infer a universal retry or document request from a broad family.
- A material organization row, `1_5052`, says the affiliation document verifies that the payout entity is **not 100% affiliated** with the company and that **setup cannot be continued**; its table points to action `1_100`. Preserve that stop condition rather than presenting every KYC suberror as an ordinary resubmission. Other entries also name sensitive documents or minimum-age failure, but their handling remains code-specific.
- The example places `subErrors` inside an item of `problems[].verificationErrors[]`; it illustrates general error `1_30` and suberrors `1_3001`/`1_3000` with their own messages, remediating actions and `type=invalidInput`. It contains ellipses and literal hint markup, so it is an explanatory shape, not a complete parseable payload or evidence of a live user's verification result. Use observed API/webhook data and current schema for implementation.

## Detail locators

- Opening, `## Requirements`, `## Types of error codes`: purpose, conditional Platforms/Issuing scope and family map.
- `## General issues` and `## Individual identity check`: generic and person/data/document/biometric examples.
- `## Organization check`: registry, tax, affiliation, VAT, ownership and evidence errors; `1_5052` stop condition.
- `## Legal arrangement check`: entity-type wording and constitutional/participant evidence rows.
- `## Bank account check`, `## Proof of signatory check`, `## Business lines check`: respective problem/action-code mappings.
- `## Suberrors array example`: nested problem/error/suberror illustration; not a full valid runtime envelope.

## Related

- [[adyen-business-accounts]] — main Business Accounts concept and verification context.
- [[adyen-financial-products]] — product-family context.
- [[adyen-platforms]] — Platforms integration context.
- [[adyen]] — provider profile.

## Raw Sources

- [[raw/adyen/docs/business-accounts/kyc-verification-codes/sub-errors/2026-09-15|Adyen verification suberror code table (last modified 2023-02-28; fetched 2026-09-15)]]
