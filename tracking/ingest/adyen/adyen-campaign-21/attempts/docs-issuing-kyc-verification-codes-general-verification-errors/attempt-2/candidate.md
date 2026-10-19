---
title: "Adyen Issuing general verification error codes"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/kyc-verification-codes/general-verification-errors"
raw_files:
  - "adyen/docs/issuing/kyc-verification-codes/general-verification-errors/2026-09-15.md"
tags: [adyen, issuing, verification, kyc, error-codes]
---

## Overview

Adyen's general verification error-code reference (last modified 2021-01-19, captured 2026-09-15) maps broad verification failure codes to messages and, where listed, possible suberrors or remediating-action codes. For Adyen for Platforms or Issuing integrations, the page states no extra preparation is needed to use this reference. General codes and messages appear in `verificationErrors`; that array usually also contains corresponding suberrors. Use the specific returned code and linked detail rather than treating the broad category as a full diagnosis or a guaranteed remedy. [[adyen-issuing]] [[adyen]]

## Key takeaways

- The catalog covers general issues (`1_10`–`1_16`), individual identity, organization, legal arrangement, bank account, proof of signatory, and business-line checks; missing-data codes, missing-contract (`2_9xx`), and data-review (`3_10`) entries follow. The opening range summary omits the later legal-arrangement and business-line sections, so the actual sections are the safer navigation route. See raw lines 22–33 and 35–130.
- Some broad errors are consequential: `1_12` is legal entity declined; `1_14`–`1_16` say a capability is not allowed for an individual, country, or entity type. These are not evidence of an available workaround or eligibility. See raw lines 35–45.
- Missing-data rows identify a missing field, document, or entity association and link a remediating-action code; they include individual, bank-account, organization, tax, business-line, source-of-funds, ownership and signatory data. The table lists conditional verification errors, not a universal schema of fields required for every entity or region. See raw lines 133–290.
- Missing-contract entries include unsigned PCI forms (`2_901`), unaccepted Terms of Service (`2_902`), and an integration not fully implemented (`2_904`); `3_10` says data review is required. See raw lines 292–304.
- The `problems` JSON block is an example with `entity`, `verificationErrors`, `remediatingActions`, and `subErrors`; it does not itself show a real entity or completed resolution. See raw lines 306–335.

## Detail locators

- Individual identity codes, including ID documents, residency, tax ID, live selfie and biometrics: raw lines 47–68.
- Organization, legal arrangement, bank, signatory, and business-line checks: raw lines 70–130.
- Complete missing-data code-to-action mapping: raw lines 133–290; follow the source's remediating-action links for action definitions.
- Contracts, review, and sample array shape: raw lines 292–335.

## Related

- [[adyen-issuing]] — Issuing concept and verification context.
- [[adyen-platforms]] — Adyen for Platforms context.

## Raw Sources

- [[raw/adyen/docs/issuing/kyc-verification-codes/general-verification-errors/2026-09-15|General error codes, captured 2026-09-15]]
