---
title: "Adyen ACH Direct Debit batch authorisation sub-lines"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/authorisation-request-file/authorisation-for-ach-direct-debit"
raw_files:
  - "adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/authorisation-request-file/authorisation-for-ach-direct-debit/2026-09-15.md"
tags: [adyen, batch-processing, ach-direct-debit, authorisation, bank-account]
---

## Overview

This 2019-last-modified Adyen SFTP batch reference defines `SL` sub-lines for a bank-transfer or ACH Direct Debit authorisation **request**. It identifies `PaymentDetails`, `BankAccount`, and `Address` as mandatory sub-lines and supplies field tables and a short example. It does not record ACH customer consent or mandate evidence, file acceptance, payment approval, bank debit completion, or settlement. The page was captured 2026-09-15; see [[adyen]] and [[adyen-batch-processing]].

## Key takeaways

- `PaymentDetails` carries the request amount, numeric currency exponent and three-character ISO currency code as required fields, alongside the `SL` record number and type. The shopper reference is optional in this table but required for recurring payments and creation of recurring contracts. Blank optional fields still need delimiting commas to preserve the fixed field count. The sample's amount/exponent/currency are illustrative, not an actual debit outcome.
- `BankAccount` is required and the page places it at **sub-line 2** for bank-account authorisation. Its table marks owner name, two-letter country code, bank account number and ABA routing/branch number as required. It says an invalid ISO 3166-1 alpha-2 country code causes request/transaction rejection. The owner-name row says a two-letter format (`AA`), yet the example uses `Adyen Inc`; the exact accepted owner-name format is unresolved from this page.
- An `Address` sub-line is also named mandatory. The address section says billing and delivery details belong on separate `Address` sub-lines, and its type field allows `Billing` or `Delivery`. Yet the sample shows only a `Billing` line. Do not infer from that example that a delivery address can always be omitted, or from the prose that a two-address sample is shown; the source is internally inconsistent about the example.
- This is file-shape guidance. Supplying bank details, address and amount does **not** demonstrate the shopper's ACH authorization/consent, a valid mandate, an accepted batch, successful authorisation, funds movement, or a final financial result. Consult the common request, ACK and result-file guides for their distinct stages.

## Detail locators

- `## Mandatory sub-lines`, lines 16–18: named required sub-lines and bank-transfer/ACH DD request scope.
- `### PaymentDetails`, lines 20–38: required amount/exponent/currency and record fields, conditional shopper reference, optional commas.
- `### BankAccount`, lines 40–53: sub-line 2, required bank fields, country-code rejection and owner-name table value.
- `### Address`, lines 55–75: billing/delivery separate-line instruction and required address fields.
- Lines 77–83: three-line sample with `PaymentDetails`, a full bank-owner name and only a billing address.

## Related

- [[adyen-batch-processing]] — batch transport, validation and result boundaries.
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file]] — common SFTP batch request-file structure.

## Raw Sources

- [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/authorisation-request-file/authorisation-for-ach-direct-debit/2026-09-15|ACH Direct Debit authorisation request sub-lines, captured 2026-09-15]]
