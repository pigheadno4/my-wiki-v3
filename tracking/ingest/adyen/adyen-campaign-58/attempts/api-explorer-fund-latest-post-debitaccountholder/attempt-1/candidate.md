---
title: "Adyen Fund API: POST /debitAccountHolder"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Fund/latest/post/debitAccountHolder"
raw_files:
  - "adyen/api-explorer/Fund/latest/post/debitAccountHolder/2026-09-15.md"
tags: [adyen, classic-platforms, fund-api, direct-debit, top-up]
---

## Overview

This 2026-09-15 Fund API Explorer capture documents `POST /debitAccountHolder` on the listed TEST Fund v6 server. It sends a direct debit request against an account holder's identified bank account; successful debit funds are settled to platform accounts specified in split instructions. Adyen says the debit result is sent in a `DIRECT_DEBIT_INITIATED` notification webhook. See [[adyen]] and [[adyen-classic-platforms]].

## Key takeaways

- Required request fields are `accountHolderCode`, `amount` (`currency` and minor-unit integer `value`), `bankAccountUUID`, `merchantAccount`, and `splits` with at least one item. The account holder and bank account are the debit source; the split accounts are destinations. A split `type` is required, with conditional `account`, `amount`, and `reference` rules by integration and type. In Classic Platforms, split `amount` is required for every type and `reference` for `MarketPlace`; see raw lines 26–33 for the full matrix.
- The page also includes Balance Platform-specific split-field descriptions. Its Classic type list spells `Marketplace` while the same schema's reference condition and its example use `MarketPlace`. Preserve that casing discrepancy; the sample does not settle which token the API accepts. The example's USD 6200 debit split into 6000 and 200 is illustrative, not evidence of a completed debit or settlement.
- HTTP 200 says the request succeeded; HTTP 202 says accepted for processing but not complete. The response schema's `accountHolderCode`, `bankAccountUUID`, `merchantReferences`, `pspReference`, `resultCode`, and validation fields are optional. The 200 example includes `pspReference` and `submittedAsync` string `false`, but `submittedAsync` is absent from the listed response schema; neither receipt nor that example proves successful bank collection, final split credit, or receipt of funds. Follow the stated notification-result route for outcome.
- Error classes listed are 400 request reading/understanding, 401 authentication, 403 insufficient permissions, 422 validation, and 500 server processing. This endpoint page does not specify a named role, debit mandate/consent, bank eligibility, limits, a live server, or a successful real transaction. The linked Classic top-up guide is the separate route for operational prerequisites.

## Detail locators

- Purpose, webhook and TEST v6 server: raw lines 5–12.
- Request requiredness, conditional split rules and Classic/Balance Platform distinctions: raw lines 14–33.
- Illustrative request and `MarketPlace` spelling: raw lines 35–66.
- 200/202 response semantics and schemas: raw lines 67–106; errors: 109–171; 200 response example: 173–183.

## Related

- [[adyen-classic-platforms]] — older platform account and Fund API routes.
- [[source-adyen-docs-classic-platforms-top-up-accounts]] — linked Classic direct-debit top-up guide for separate operational context.

## Raw Sources

- [[raw/adyen/api-explorer/Fund/latest/post/debitAccountHolder/2026-09-15|Fund API Explorer POST /debitAccountHolder capture]]
