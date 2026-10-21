---
title: "Adyen Marketplaces general verification error codes"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/kyc-verification-codes/general-verification-errors"
raw_files:
  - "adyen/docs/marketplaces/kyc-verification-codes/general-verification-errors/2026-09-15.md"
tags: [adyen, marketplaces, platforms, kyc, verification, error-codes]
---

## Overview

This 2023-modified general error-code reference, captured 2026-09-15 under the Marketplaces URL, helps identify broad causes of verification errors for Adyen for Platforms and Adyen Issuing integrations. Adyen sends general codes and messages in the `verificationErrors` array, which usually also has corresponding suberrors. It is a lookup in the [[adyen-platforms]] route from [[adyen]], not a current account-specific verification or capability decision.

## Key takeaways

- The page says there are no additional requirements, limitations, or preparations for an Adyen for Platforms or Adyen Issuing integration to use these codes. Code ranges group general, individual, organization, legal-arrangement, bank-account, signatory, business-line, missing-data, missing-contract, and data-review checks. See raw lines 16–35.
- Use the exact general code and its **possible** suberrors to locate a more specific cause. Possible suberrors are not guaranteed in every error. The general-issues rows distinguish capability disallowance for an individual type (`1_14`), legal-entity/associated-individual country (`1_15`), and entity type (`1_16`). See raw lines 37–47.
- Two table links disagree with their displayed suberror codes: organization row `1_50` displays `1_5054` but links to `#1_5042`; proof-of-signatory row `1_85` displays `1_8015` but links to `#1_8008`. Resolve the exact code in the separate suberror reference before selecting any remediation; do not treat the target anchor as the displayed code. See raw lines 77 and 122.
- Missing-data rows identify absent inputs and remediating-action codes in particular error cases, not universal required properties for every request. Missing contracts are a separate category (`2_901` unsigned PCI forms, `2_902` unaccepted Terms of Service, `2_904` incomplete integration); data review has `3_10`. See raw lines 136–307.
- The example nests `verificationErrors` beneath a `problems` entry for a `LegalEntity` and illustrates `code`, `message`, a common `remediatingActions` array, and `subErrors`. It is an example shape, not evidence of a particular live payload, successful remediation, or final verification. See raw lines 309–338.

## Detail locators

- General issues and capability-related messages: raw lines 37–48.
- Individual identity, organization, legal arrangement, bank account, proof of signatory, and business-line code tables: raw lines 49–135.
- Missing-data field/action mappings: raw lines 136–294.
- Missing contracts and data-review codes: raw lines 295–308.
- Illustrative `problems[].verificationErrors` object: raw lines 309–338.

## Related

- [[adyen]] — provider profile.
- [[adyen-platforms]] — modern Platforms and Marketplaces route.
- [[source-adyen-docs-marketplaces-kyc-verification-codes-sub-errors]] — distinct Marketplace-path suberror catalog for exact-code lookup.
- [[source-adyen-docs-platforms-kyc-verification-codes-general-verification-errors]] — separate Platforms URL with closely related error-code content; keep provenance distinct.
- [[adyen-classic-platforms]] — legacy Classic Platforms, a different resource model.

## Raw Sources

- [[raw/adyen/docs/marketplaces/kyc-verification-codes/general-verification-errors/2026-09-15|General error codes — pinned 2026-09-15 raw snapshot]]
