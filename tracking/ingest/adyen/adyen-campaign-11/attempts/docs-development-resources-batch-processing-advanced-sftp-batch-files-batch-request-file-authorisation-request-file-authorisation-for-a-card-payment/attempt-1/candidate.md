---
title: "Adyen SFTP batch authorisation for a card payment"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/authorisation-request-file/authorisation-for-a-card-payment"
raw_files:
  - "adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/authorisation-request-file/authorisation-for-a-card-payment/2026-09-15.md"
tags: [adyen, batch-processing, sftp, card-authorisation, file-format]
---

## Overview

This dated Adyen Docs page (last-modified metadata 2019-04-29; captured 2026-09-15) specifies the sub-line layout for a card payment **Authorisation request** in an advanced SFTP batch request file. It is a record-format reference, not a result or proof that an authorization succeeded. Route general file structure and batch processing through [[adyen-batch-processing]] and [[adyen]].

## Key takeaways

- Adyen says these card-payment sub-lines may be submitted only when the batch file is PGP-encrypted. Both `PaymentDetails` and `Card` are mandatory; `Card` must be sub-line 2. Sub-line numbering starts at 1 and increments sequentially within the parent line. [Raw lines 18–20, 30–32, 42–51]
- `PaymentDetails` positions 4–6 are numeric amount, numeric currency exponent, and three-character ISO currency code. The page gives `100,2,SEK` as a **sample**, not a general authorization result or a standalone currency-conversion rule. Position 7 shopper reference is otherwise optional in the table but required for recurring payments and recurring-contract creation. Blank optional positions still need commas to retain the fixed field count. [Raw lines 24–40, 62–70]
- `Card` positions 4–8 hold card number, expiry month (`MM`), expiry year (`YYYY`), CVC, and cardholder name. The source specifies three-digit CVC/CVV for Visa, Mastercard, and Discover and four-digit for American Express; positions 9–11 are optional UK Maestro start date and issue number. This is a sensitive card-data file format, subject to the PGP submission condition above. [Raw lines 47–60]
- `Address`, `MerchantOrderReference`, and `ShopperInteraction` are conditional sub-lines. Billing and delivery addresses use separate `Address` sub-lines; an invalid two-letter ISO country code rejects the transaction/request. `ShopperInteraction` allows `Moto` or `ContAuth` and is required for MOTO or recurring transactions. [Raw lines 72–96, 109–137]

## Detail locators

- Mandatory positional schemas and first sample: raw lines 28–70. The examples include `FH`, `BH`, `L`, `SL`, `BT`, and `FT` records; use the parent batch-request-file reference for their common record structure.
- Optional sub-line schemas and examples: raw lines 72–150. The Address example joins `FH` and `BH` on line 99, while the ShopperInteraction example jumps from `SL,4` to `SL,6` at lines 146–147 despite the sequential-counter rule. Treat these snippets as examples and follow the field tables; this page does not resolve those sample inconsistencies.
- This page defines request content. File acknowledgment, acceptance, and per-payment authorization results require their separate batch ACK and result sources; do not infer an authorized payment from a prepared file or ACK.

## Related

- [[adyen-batch-processing]]
- [[adyen]]
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file]]

## Raw Sources

- [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/authorisation-request-file/authorisation-for-a-card-payment/2026-09-15|Adyen authorisation for a card payment, 2026-09-15 snapshot]]
