---
title: "Braintree Merchant Advice Codes"
type: source
date_ingested: 2026-09-23
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/general/merchant-responses/merchant-advice-codes"
raw_files:
  - "braintree/docs/reference/general/merchant-responses/merchant-advice-codes-2026-09-16.md"
tags: [braintree, mastercard, merchant-advice-code, declines, retries]
---

## Overview

This Braintree reference explains Mastercard Merchant Advice Codes (MACs), which may accompany a declined transaction with a reason or merchant action. When present, the transaction response returns a merchant advice code and corresponding text; some codes prohibit or stop an action, while others suggest whether and when a retry may be considered.

## Key takeaways

- The page names the response values as `merchant_advice_code` and `merchant_advice_code_text`; the collected prose renders those names without surrounding spaces. A MAC is optional, so its absence does not establish a retry instruction.
- Code `03` means "Do not try again", and code `21` means "Stop recurring payment". Code `02` says "Cannot approve at this time, try again later" but supplies no waiting duration.
- The duration-specific retry codes are `24` after 1 hour, `25` after 24 hours, `26` after 2 days, `27` after 4 days, `28` after 6 days, `29` after 8 days and `30` after 10 days. These are the exact durations in this table; the page does not define an attempt count or guarantee that a later retry will succeed.
- The remaining listed meanings identify new account information (`01`), an unsupported token (`04`), a non-reloadable prepaid card (`40`), a single-use virtual card number (`41`) or a multi-use virtual card number (`43`). Consult the raw table for the authoritative code-to-text mapping.

## Retry boundary

A MAC communicates Mastercard decline advice when it is present. This page does not say that a retry-oriented MAC overrides processor-response prohibitions, recurring-payment restrictions, operation state checks or other payment-method rules. Use [[source-braintree-authorization-responses]] for the separately documented authorization-response and retry restrictions before repeating a transaction.

## Detail locators

- Mastercard purpose, optional presence and possible retry-duration information: `# Merchant Advice Codes`, line 16.
- Transaction-response field names: `# Merchant Advice Codes`, line 18.
- Account, later-retry, do-not-retry, token and stop-recurring meanings: code table, lines 22-28.
- Exact retry durations for codes `24` through `30`: code table, lines 29-35.
- Prepaid and virtual-card meanings for codes `40`, `41` and `43`: code table, lines 36-38.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]
- Authorization decline and retry restrictions: [[source-braintree-authorization-responses]]

## Raw Sources

- [[raw/braintree/docs/reference/general/merchant-responses/merchant-advice-codes-2026-09-16|Braintree Merchant Advice Codes]] - complete collected page containing the Mastercard purpose, response-field route and full code-to-text table
