---
title: "Adyen batch StoreToken request for payout"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/storetoken-request-file/storetoken-request-for-payout"
raw_files:
  - "adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/storetoken-request-file/storetoken-request-for-payout/2026-09-15.md"
tags: [adyen, batch-processing, storetoken, payout, sensitive-data]
---

## Overview

This [[adyen]] reference specifies the sub-lines and field tables for a payout-oriented `StoreToken` request inside Adyen's advanced SFTP batch-file format. The record concerns storing payment details for a payout use; it is not a payout instruction or proof that an alias is usable for later charges. Route the file format through [[adyen-batch-processing]]; [[adyen-payouts]] and [[adyen-tokenization]] cover separate payout and online-payment-token contexts.

## Key takeaways

- A `StoreToken` request needs both `ShopperDetails` and `Recurring` sub-lines and **one** of `Card`, `BankAccount`, or `IBAN`. The `Recurring` table fixes its type to `PAYOUT` and next value to `Latest`. The page says only payment requests submitted after sending the `StoreToken` request are tokenised; it does not state an immediate successful storage outcome. See **Mandatory sub-lines** and **Recurring**, raw lines 16–21 and 37–47.
- `ShopperDetails` requires a shopper reference and email address, as shown in its field table. Empty optional fields still need delimiter commas because each sub-line has a fixed number of fields. The payment-instrument tables include sensitive card or bank identifiers and beneficiary/holder names; handle these as sensitive data, not a verified identity or a settled payout. See raw lines 23–35, 49–70, 83–103, and 116–133.
- For this `StoreToken` use, the page says a user role with permission to **store payout details** is needed. The captured page does not name a specific role, prove a merchant has that permission, or define cross-merchant token reuse. Its test examples use `TEST` and a sample `MerchantAccount` line; they are sample records, not live enablement evidence. See raw lines 53, 72–81, 87, 105–114, 120, and 135–144.
- The `Card` table marks CVC optional and explicitly says **leave it blank**. The `IBAN` owner-name field requires at least three characters and cannot be only numbers; invalid formatting produces error 203. The `BankAccount` and `IBAN` country-code descriptions say an invalid ISO alpha-2 country code rejects the request. These are field-level warnings, not guarantees that a valid-looking record will be accepted or any payout completed. See raw lines 63–70, 97–103, and 130–133.

## Detail locators

- Mandatory record composition and no retroactive tokenisation: **Mandatory sub-lines**, raw lines 16–21.
- `ShopperDetails` fixed-field, shopper-reference and email contract: raw lines 23–35.
- `Recurring` `PAYOUT,Latest` values: raw lines 37–47.
- Card fields, blank CVC and test example: raw lines 49–81.
- BankAccount fields, country validation and test example: raw lines 83–114.
- IBAN owner-name/country checks, fields and test example: raw lines 116–144.

## Related

- Company: [[adyen]]
- Main concept: [[adyen-batch-processing]]
- Adjacent concepts: [[adyen-payouts]], [[adyen-tokenization]]

## Raw Sources

- [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/storetoken-request-file/storetoken-request-for-payout/2026-09-15|Adyen StoreToken request for payout]] — full pinned 2026-09-15 snapshot of payout-oriented batch sub-line tables and examples; page metadata says last modified 2019-04-30
