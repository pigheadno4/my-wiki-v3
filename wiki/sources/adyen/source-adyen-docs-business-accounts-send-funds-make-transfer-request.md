---
title: "Adyen Business Accounts: Make a third-party bank transfer request"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/send-funds/make-transfer-request"
raw_files:
  - "adyen/docs/business-accounts/send-funds/make-transfer-request/2026-09-15.md"
tags: [adyen, business-accounts, transfers, send-funds]
---

## Overview

This 2026-09-15 capture of Adyen's Business Accounts guide explains how a platform submits a Transfers API request to send funds from a source balance account to a third-party bank account. The transfer request and its returned ID are distinct from the later transfer status conveyed by outgoing bank-transfer webhooks. This is a dated guide, not evidence of current eligibility, a completed transfer, or receipt by the bank.

## Key takeaways

- Scope is Adyen Business Accounts sending to third-party **bank accounts**. The captured limitation does not include third-party wallets or cards. The API credential needs Transfers API roles; the user needs `sendToThirdParty` allowed and enabled; transfer and transaction webhooks are listed; and Adyen says to arrange source-balance-account transfer enablement with its contact. The guide recommends route lookup and account validation before a new counterparty transfer.
- A POST `/transfers` starts the bank transfer request. Its table specifies amount/currency, source `balanceAccountId`, `category: bank`, counterparty `bankAccount` and transfer priority. The recipient account holder's full name and account identification are required; cross-border transfers additionally require the holder's address. Bank identification fields vary by type. The source balance account, counterparty bank account and returned transfer-request ID are different resources.
- An HTTP 200 response with an `id` signals a successful **request**; follow outgoing bank-transfer webhooks for status. The guide also documents an optional `review.numberOfApprovalsRequired: 1` path that requires team approval before Adyen continues processing. The review prose contains dropped words, so consult the raw and the linked approval guide before implementing that path.

## Detail locators

- `## Requirements` (raw lines 21–38): roles, `sendToThirdParty`, webhook subscriptions, third-party-bank limitation, account enablement and recommended route/validation checks. `## Get transfer routes` (40–42) and `## Validate a third-party bank account` (44–158): `POST /validateBankAccountIdentification`, IBAN/US/AU examples, 200 success and illustrative 422 `33_01` invalid-field errors. Validation is a preflight check, not a delivery guarantee.
- `## Make a transfer` (160–174): request field table, cross-border address condition, internal `reference` versus recipient `referenceForBeneficiary`, and priority's speed/fee relevance. Example tabs at 178–1557 show local IBAN, US-local and cross-border number-and-BIC requests in TEST with dated SDK versions; do not generalize example values into eligibility or route guarantees.
- Raw line 1559 gives request response and webhook status route. `### Trigger additional reviews` (1563–2120) includes the one-approval option, example SDK idempotency keys and 2XX review response. The idempotency keys are examples here, not a stated retry/duplicate-processing contract. Several review sentences have missing nouns; the review workflow cannot be fully derived from this snapshot alone.

## Related

- [[adyen-business-accounts]] — product and resource context.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/business-accounts/send-funds/make-transfer-request/2026-09-15|Make a transfer request (captured 2026-09-15)]]
