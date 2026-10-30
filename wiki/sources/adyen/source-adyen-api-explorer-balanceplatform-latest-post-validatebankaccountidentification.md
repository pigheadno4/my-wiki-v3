---
title: "POST /validateBankAccountIdentification — Validate bank account details | Adyen Balance Platform API"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/post/validateBankAccountIdentification"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/post/validateBankAccountIdentification/2026-09-15.md"
tags: [adyen, balance-platform, bank-account-validation, transfer-instruments, api-explorer]
---

## Overview

This [[adyen]] Balance Platform API Explorer snapshot documents `POST /validateBankAccountIdentification`, a check of bank account identification details that can precede a separate transfer or transfer-instrument creation. The captured server is TEST `https://balanceplatform-api-test.adyen.com/bcl/v2`; the URL says `latest` while the listed server path identifies `v2`. The check is for identification details, not proof of account ownership, transfer-instrument verification, payout permission or funds delivery. See [[adyen-platforms]].

## Key takeaways

- The request-body table marks `accountIdentification` required but does not expand its nested schema or state that either illustrated shape is exhaustive. Request examples show `iban` and `usLocal` objects; their values are sample inputs, and later 422 examples show them rejected. The page does not mark individual nested fields required in its request table. [Raw: lines 14–41, 169–208]
- The 200 heading says to look at the actual response code for request status, but supplies no success response-body schema or success example. It does not define an ownership match, verification status, registered transfer instrument or completed transfer as a result. [Raw: lines 42–46, 127–222]
- The documented errors are 401 authentication required, 403 insufficient permissions, 422 request validation error and 500 server processing failure. Specific 422 examples identify invalid IBAN and invalid US account/routing values. A separate generic 422 example concerns changing a payment instrument's balanceAccountId, and the generic 500 example concerns creating a payment instrument; neither defines this validation endpoint's account-ownership or instrument lifecycle behavior. [Raw: lines 48–125, 155–222]

## Detail locators

- Purpose, preceding-use links and TEST v2 server: pinned raw lines 5–10.
- Required top-level request field and illustrative IBAN/US payloads: lines 12–41.
- 200 heading, error schemas and status descriptions: lines 42–125.
- Error examples, including endpoint-specific invalid-detail 422s and unrelated generic payment-instrument examples: lines 127–222.

## Related

- [[adyen-platforms]] — resource context and evidence boundary.
- [[source-adyen-docs-platforms-manage-transfer-instruments]] — separate transfer-instrument creation, verification and payout prerequisites.
- [[adyen-platform-internal-transfers]] — separate transfer operation context; this validation call does not move funds.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/post/validateBankAccountIdentification/2026-09-15|POST /validateBankAccountIdentification — captured 2026-09-15]]
