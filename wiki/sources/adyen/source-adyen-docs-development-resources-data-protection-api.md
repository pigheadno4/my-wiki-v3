---
title: "Adyen Data Protection API"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/data-protection-api"
raw_files:
  - "adyen/docs/development-resources/data-protection-api/2026-09-15.md"
tags: [adyen, data-protection, gdpr, erasure, shopper-data, recurring-payments]
---

## Overview

This Adyen guide describes the Data Protection API route for submitting a GDPR subject-erasure request for shopper-related data associated with an **original payment authorisation**. The page was captured 2026-09-15 and carries 2023-05-31 last-modified metadata. It documents an Adyen-side request and Customer Area redaction check; it is not proof of a completed erasure, cancellation of recurring activity, or deletion of merchant-held records.

## Key takeaways

- Submit `POST /requestSubjectErasure` with `merchantAccount` and the original payment's `pspReference`. The guide says the request targets shopper-related data **for that payment**, including payment details and examples such as delivery address or email. Its curl example uses an API key against `ca-test.adyen.com`; it says to switch the domain to `ca-live.adyen.com` for live. The page does not define a shopper-facing client flow.
- `SUCCESS` means Adyen received the request for **asynchronous processing**; it is not a completed-deletion receipt. `ACTIVE_RECURRING_TOKEN_EXISTS` means shopper data cannot be deleted because a recurring transaction is associated with the payment details. Optional `forceErasure: true` permits deletion of shopper-related data for the specified payment despite that condition, but **does not cancel the existing recurring transaction**. Other listed results are `PAYMENT_NOT_FOUND` and `ALREADY_PROCESSED`.
- After receiving a request, Adyen says it will delete transaction data **in accordance with the Merchant Agreement** and redact shopper-related data in Customer Area. The optional verification step checks that payment's fields show `REDACTED` and a redaction date. The page does not promise blanket erasure of every financial or compliance record, nor does this Adyen API itself delete data held on a merchant's systems.
- This erasure route is distinct from managing a stored payment token through Checkout API `DELETE /storedPaymentMethods/{storedPaymentMethodId}`. The linked token-management source separately addresses merchant-server cleanup after token deletion; do not substitute one operation for the other.

## Detail locators

- `# Data Protection API` — GDPR subject-erasure purpose and shopper-data examples.
- `## Submit a Subject Erasure Request`, step 1 — endpoint, required payment/account selectors, optional force flag and TEST request sample.
- Step 2 — `result` meanings, asynchronous acceptance, Merchant Agreement qualification and Customer Area redaction.
- Step 3 and final sentence — optional redaction check and TEST-to-live host change.

## Related

- Company: [[adyen]]
- Recurring-token context and separate stored-payment-method deletion: [[adyen-tokenization]]
- Token management source: [[source-adyen-docs-online-payments-tokenization-managing-tokens]]

## Raw Sources

- [[raw/adyen/docs/development-resources/data-protection-api/2026-09-15|2026-09-15 Adyen Data Protection API snapshot]]
