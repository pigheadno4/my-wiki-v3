---
title: "Adyen SFTP batch authorisation for an IBAN payment"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/authorisation-request-file/authorisation-for-an-iban-payment"
raw_files:
  - "adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/authorisation-request-file/authorisation-for-an-iban-payment/2026-09-15.md"
tags: [adyen, batch-processing, sftp, iban, authorisation, file-format]
---

## Overview

This Adyen Docs snapshot (2019-04-30 last-modified metadata; captured 2026-09-15) specifies the sub-lines of an advanced-SFTP batch **Authorisation request** for a bank transfer or SEPA Direct Debit payment using IBAN details. It is a request-record schema, not evidence of batch acceptance, authorization, debit settlement, or any payment outcome. For file framing and outcome routes see [[adyen-batch-processing]] and [[adyen]].

## Key takeaways

- `PaymentDetails` and `IBAN` sub-lines are mandatory; `IBAN` must be sub-line 2. The `SL` counter starts at 1 within its parent line and increments sequentially. Empty optional positions still require commas because the line has a fixed field count. [Raw lines 18–29, 40–49]
- `PaymentDetails` positions 4–6 are the numeric amount, numeric currency exponent, and three-character ISO currency code. Position 7 shopper reference is optional in the base table but required for recurring payments and creation of recurring contracts; positions 8–11 cover optional email, statement descriptor, IP address, and fraud offset. The sample `100,2,SEK` illustrates field placement, not a general conversion or financial-result rule. [Raw lines 26–38, 55–63]
- `IBAN` positions 4–6 require bank account owner name, two-letter ISO 3166-1 alpha-2 country, and IBAN code; position 7 is optional BIC. The owner name must be alphanumeric, contain at least three characters, and not consist only of numbers; the page identifies error 203 for an invalid owner-name format. An invalid country code rejects the transaction/request. [Raw lines 45–53]
- Optional `Address` sub-lines carry billing and delivery addresses separately, with a two-letter country code. `MerchantOrderReference` may carry an order reference. [Raw lines 65–110]

## Detail locators

- Mandatory `PaymentDetails` and `IBAN` positional schemas, including sample: raw lines 20–63. The sample contains `FH`, `BH`, `L`, `SL`, `BT`, and `FT`; their common framing belongs to the parent batch-request-file reference.
- Optional `Address` schema and sample: raw lines 65–101. Optional `MerchantOrderReference` schema and example: raw lines 103–121. The latter **IBAN-page example uses a `Card` sub-line** at line 117, so do not treat that snippet as an IBAN-specific validated file template; use the mandatory `IBAN` table for the IBAN sub-line.
- Format validation or request rejection is distinct from a final financial result. Consult the separately routed batch acknowledgement and result-file sources for validation and per-payment outcomes; this page does not report a live payment.

## Related

- [[adyen-batch-processing]]
- [[adyen]]
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file]]

## Raw Sources

- [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/authorisation-request-file/authorisation-for-an-iban-payment/2026-09-15|Adyen authorisation for an IBAN payment, 2026-09-15 snapshot]]
