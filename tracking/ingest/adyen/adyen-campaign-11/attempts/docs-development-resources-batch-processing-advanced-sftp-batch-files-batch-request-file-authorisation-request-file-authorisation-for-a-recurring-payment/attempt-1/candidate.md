---
title: "Adyen SFTP recurring authorisation request sub-lines"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/authorisation-request-file/authorisation-for-a-recurring-payment"
raw_files:
  - "adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/authorisation-request-file/authorisation-for-a-recurring-payment/2026-09-15.md"
tags: [adyen, batch-processing, sftp, recurring-payments, authorisation]
---

## Overview

This [[adyen]] SFTP batch reference defines sub-lines for an `Authorisation` request that charges using stored recurring details. Its mandatory `PaymentDetails`, `Recurring`, and `ShopperInteraction` records specify a new authorization request tied to a shopper and stored-detail selection; `RECURRING` and a token or `LATEST` select existing recurring data rather than creating a new token. The page is a file-format guide under [[adyen-batch-processing]], not evidence that a submitted record passed validation or that a payment was authorized.

## Key takeaways

- The `PaymentDetails` sub-line uses fixed-position comma-separated fields: positions 1–3 identify `SL`, sequence and type; positions 4–7 are amount, currency exponent, three-character ISO currency code and unique shopper reference. Its email, statement, IP and fraud-offset positions are optional, but their commas must remain to preserve the fixed field count. Do not merge amount and exponent or shift later fields when an optional value is blank.
- The `Recurring` sub-line uses `RECURRING` at field 4 and either a 16-character selected recurring-detail token or `LATEST` at field 5. The token targets a specific stored data set; `LATEST` selects the most recent set for use. Neither value proves the stored credential is valid or that a new charge succeeded.
- `ShopperInteraction` is listed among the three mandatory sub-lines for this recurring authorization request. The page says to use `ContAuth` unless performing MOTO; it also lists other allowed interaction values in the field table. The dedicated recurring example shows `SL,1,PaymentDetails,100,2,SEK,Ref123`, `SL,2,Recurring,RECURRING,LATEST`, and `SL,3,ShopperInteraction,ContAuth` under one `Authorisation` parent line. These are structure examples, not actual payment outcomes.
- Optional `Address` uses separate Billing and Delivery sub-lines and an invalid country code causes transaction/request rejection. Optional `MerchantOrderReference` carries the merchant's order reference at field 4. Its final sample instead includes a `Card` sub-line with card number and CVC, and omits the page's mandatory `Recurring` and `ShopperInteraction` sub-lines (raw lines 139–148). Treat that fragment as an order-reference illustration, not a complete recurring request or proof that CVC/card fields are required when using a stored detail.

## Detail locators

- **Mandatory recurring sub-lines and fixed delimiter rule:** raw lines 14–24, under `# Authorisation for a recurring payment` and `## Mandatory sub-lines`.
- **`PaymentDetails` field positions, requiredness, amount/exponent/currency and shopper reference:** raw lines 20–38, under `### PaymentDetails`.
- **`Recurring` contract and stored-detail selector:** raw lines 40–50, under `### Recurring`.
- **`ShopperInteraction` condition, field values and dedicated recurring example:** raw lines 52–89, under `### ShopperInteraction`.
- **Optional Billing/Delivery address fields and country-code warning:** raw lines 91–128, under `## Optional sub-lines` and `### Address`.
- **Merchant order reference and inconsistent `Card` illustration:** raw lines 130–148, under `### MerchantOrderReference`.

## Related

- [[adyen]]
- [[adyen-batch-processing]]
- [[adyen-tokenization]]
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file]]

## Raw Sources

- [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/authorisation-request-file/authorisation-for-a-recurring-payment/2026-09-15|Adyen SFTP recurring authorisation file reference — collected 2026-09-15]]
