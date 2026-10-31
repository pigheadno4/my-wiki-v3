---
title: "Adyen Account API v6: POST /deleteBankAccounts"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Account/latest/post/deleteBankAccounts"
raw_files:
  - "adyen/api-explorer/Account/latest/post/deleteBankAccounts/2026-09-15.md"
tags: [adyen, classic-platforms, account-api, bank-accounts]
---

## Overview

This 2026-09-15-captured API Explorer page documents `POST /deleteBankAccounts` on the Account API v6 TEST server (`https://cal-test.adyen.com/cal/services/Account/v6`). It deletes bank accounts associated with a Classic Platforms account holder. The request table marks `accountHolderCode` (the account holder whose bank accounts are targeted) and `bankAccountUUIDs` (an array of bank-account codes to delete) as required properties. The page does not separately specify request-body requiredness.

## Key takeaways

- This is a destructive bank-account deletion request for the identified account holder and listed bank-account UUIDs. The captured page does not establish effects on payouts, account-holder verification, existing transfers, or how to confirm that each deletion completed.
- A 200 response says the request succeeded; a 202 says it was accepted for processing and processing has not completed. The optional success-response fields include `invalidFields`, `pspReference` (a request reference), and `resultCode`. Neither status alone establishes an eventual downstream payout or bank outcome.
- The listed errors are 400 (request reading/understanding), 401 (authentication), 403 (insufficient permissions), 422 (request validation), and 500 (server processing). The example bodies are illustrative, not an exhaustive error-code catalog.
- The TEST URL and captured `latest` page do not establish current live availability, merchant eligibility, or a live endpoint.

## Detail locators

- Request property descriptions and required flags: pinned raw, `## Parameters > ### Request body`, lines 12–18; example payload: `## Request examples > ### basic`, lines 20–30.
- 200 and 202 status descriptions and optional result fields: `## Responses`, lines 31–64.
- Error descriptions and response fields: `## Responses`, lines 67–129; illustrative 400 and 403 JSON: `## Response examples`, lines 131–155.

## Related

- [[adyen-classic-platforms]] — Classic account-holder and account context; keep this Account API v6 resource separate from newer balance-platform resources.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/api-explorer/Account/latest/post/deleteBankAccounts/2026-09-15|Account API v6 POST /deleteBankAccounts capture]]
