---
title: "Adyen Platforms KYC suberror codes"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/kyc-verification-codes/sub-errors"
raw_files:
  - "adyen/docs/platforms/kyc-verification-codes/sub-errors/2026-09-15.md"
tags: [adyen, platforms, kyc, verification, error-codes]
---

## Overview

Adyen's suberror-code reference maps granular KYC verification causes to messages and, where applicable, remediating action codes for Adyen for Platforms or Adyen Issuing integrations. The page says those integrations have no additional preparation for this reference. It is a documented diagnostic lookup, not a determination of a legal entity's current verification, capability, or account eligibility. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- The example puts `subErrors` inside a `verificationErrors` entry in a `problems` array. Its suberror objects show `code`, `message`, applicable `remediatingActions` entries, and `type`; the parent verification error also has its own code, message, and possible remediating actions. Treat the example as an illustration, not a guaranteed payload for every error. See **Suberrors array example**, raw lines 356–415.
- The reference groups codes by check: `1_1xxx` general, `1_3xxx` individual, `1_5xxx` organization, `1_6xxx` legal arrangement, `1_7xxx` bank account, `1_8xxx` proof of signatory, and `1_9xxx` business line. Match the exact suberror code and its row; action codes are conditional and link to a separate remediating-actions reference. See **Types of error codes**, raw lines 22–32, and the tables below.
- The table distinguishes conditions with materially different responses. For example, `1_5052` says the affiliation document verifies the payout entity is not 100% affiliated and setup cannot continue; its listed action code is `1_100`. Do not generalize one row's action to an entire category or promise successful verification after taking it. See **Organization check**, raw line 194.

## Detail locators

- **General issues** (raw lines 34–42): declined entity, technical issue, further questions, sensitive data, and missing information.
- **Individual identity check** (raw lines 44–137): identity, document, residence, tax, selfie, and motion-related suberrors; use the exact row's linked action codes.
- **Organization check** (raw lines 138–234): registry, tax, ownership, affiliation, VAT, address, and other organization-specific rows.
- **Legal arrangement check** (raw lines 235–290): the displayed message corresponds to the specific arrangement type; the table maps name, registration, constitutional-document, trustee, beneficiary, and related conditions.
- **Bank account check** (raw lines 291–316): bank data and supporting-document mismatches, including currency mismatch at `1_7017`.
- **Proof of signatory check** (raw lines 317–337): signatory and director document conditions.
- **Business lines check** (raw lines 338–355): industry, website, proof-of-industry, and proof-of-funds conditions.
- **Suberrors array example** (raw lines 356–415): example object nesting and an individual-check `1_3001` / `1_3000` pair, with `invalidInput` type.

## Related

- [[adyen-platforms]] — platform integration and verification context.
- [Adyen remediating actions](https://docs.adyen.com/platforms/kyc-verification-codes/remediating-actions) — action-code definitions referenced by the table; a separate page, not evidence read for this entry.

## Raw Sources

- [[raw/adyen/docs/platforms/kyc-verification-codes/sub-errors/2026-09-15|Adyen Suberror codes, fetched 2026-09-15]]
