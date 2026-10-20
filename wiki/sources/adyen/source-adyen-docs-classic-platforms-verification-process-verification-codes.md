---
title: "Adyen Classic Platforms: Verification error codes"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/verification-process/verification-codes"
raw_files:
  - "adyen/docs/classic-platforms/verification-process/verification-codes/2026-09-15.md"
tags: [adyen, classic-platforms, verification, error-codes, onboarding]
---

## Overview

This 2019-modified, 2026-09-15-captured **Classic Adyen for Platforms** reference catalogs account-holder verification error codes for **version 5 and later**. Adyen returns codes and descriptions in Classic notification webhooks or API responses. Its linked version 4-and-earlier catalog is separate, and the page directs new implementations to the newer integration guide. Keep these Classic codes and account-holder workflow separate from modern Balance Platform verification resources. See [[adyen]] and [[adyen-classic-platforms]].

## Key takeaways

- The descriptions are for the platform and **should not be shared with account holders** because they may expose information useful to malicious parties. Adyen recommends communicating general failures and asking account holders to re-upload details. The raw catalog groups codes by identity, document, bank-account and company verification; use the exact category/code row to interpret a response.
- Several rows impose an explicit retry boundary: identity `1304`, document `1107`, bank `3110` and company `2102` say the maximum retries were exceeded and **do not retry**. Bank code `8000` instead says a technical issue occurred and **a retry has been scheduled**; that is a source-stated Adyen workflow, not authorization for the platform to replay a request. Manual-review rows (`1320`, `1120`, `3120`, `2120`) report review or risk evaluation, not an approved result.
- Bank-account rows distinguish owner/number mismatch, invalid or incomplete statement, incorrect routing/account numbers, institution coverage, and `3114` institution ineligibility for **payouts on Platforms**. Company rows include business details, shareholder relationship, PO box, extract contents and entity-type mismatches. A code describes a verification failure or state; it does not prove current eligibility, a successful payout, or receipt of funds.

## Detail locators

- Pinned raw lines 15–25: Classic/version scope, webhook/API delivery and sensitive-description handling.
- Pinned raw lines 27–38: identity codes, including max retries and manual review; lines 40–75: document codes including quality, unsupported format, sensitive information and no-retry state.
- Pinned raw lines 77–110: bank-account codes, statement checks, institution coverage, payout ineligibility, scheduled retry and manual review.
- Pinned raw lines 112–140: company verification, retry stop, risk evaluation, registration/shareholder/entity-type problems.

## Related

- [[adyen-classic-platforms]] — main Classic integration route.
- [[adyen-platforms]] — newer model, separate verification and resources.
- [[source-adyen-docs-classic-platforms-error-codes]] — broader Classic response/notification error catalog.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/verification-process/verification-codes/2026-09-15|Classic Platforms verification-code catalog, captured 2026-09-15]]
